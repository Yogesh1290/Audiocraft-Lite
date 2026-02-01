"""Model management and inference for AudioCraft Lite"""

import logging
import time
import uuid
from pathlib import Path
from typing import Optional, Dict, List
import os

import torch
import torchaudio
import scipy.io.wavfile
import numpy as np
from transformers import AutoProcessor, MusicgenForConditionalGeneration

import config

logger = logging.getLogger(__name__)


class ModelManager:
    """Manages model loading and audio generation using HuggingFace transformers"""
    
    def __init__(self):
        self.models = {}  # Cache for multiple models {model_id: (processor, model)}
        self.current_model_id = None
        
        # Set CPU mode
        if config.USE_CPU:
            torch.set_num_threads(config.NUM_THREADS)
            self.device = "cpu"
            logger.info(f"Using CPU with {config.NUM_THREADS} threads")
        else:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
            logger.info(f"Using device: {self.device}")
    
    def get_downloaded_models(self) -> List[str]:
        """Check which models are already downloaded in cache"""
        downloaded = []
        cache_dir = config.CACHE_DIR
        
        if not cache_dir.exists():
            return downloaded
        
        # Check for each model in cache
        for size, info in config.AVAILABLE_MODELS.items():
            model_id = info["id"]
            # HuggingFace cache structure: models--facebook--musicgen-{size}
            model_cache_name = model_id.replace("/", "--")
            model_path = cache_dir / "models" / model_cache_name
            
            # Check if model files exist
            if model_path.exists():
                # Check for key model files
                snapshots_dir = model_path / "snapshots"
                if snapshots_dir.exists() and any(snapshots_dir.iterdir()):
                    downloaded.append(size)
                    logger.debug(f"Model {size} found in cache")
        
        return downloaded
    
    def get_model_status(self) -> Dict:
        """Get status of all models (downloaded, loaded, size)"""
        downloaded = self.get_downloaded_models()
        loaded = [size for size, info in config.AVAILABLE_MODELS.items() 
                  if info["id"] in self.models]
        
        status = {}
        for size, info in config.AVAILABLE_MODELS.items():
            status[size] = {
                "name": info["name"],
                "params": info["params"],
                "quality": info["quality"],
                "speed": info["speed"],
                "description": info["description"],
                "downloaded": size in downloaded,
                "loaded": size in loaded,
                "size_gb": info.get("size_gb", "~2-6GB")
            }
        
        return status
    
    def is_loaded(self) -> bool:
        """Check if any model is loaded"""
        return len(self.models) > 0
    
    def download_model(self, model_size: str = "medium") -> Dict:
        """Download model without loading into memory (for on-demand download)"""
        if model_size not in config.AVAILABLE_MODELS:
            raise ValueError(f"Unknown model size: {model_size}")
        
        model_id = config.AVAILABLE_MODELS[model_size]["id"]
        
        logger.info(f"Downloading MusicGen model: {model_size} ({model_id})")
        start_time = time.time()
        
        try:
            # Download processor (small, fast)
            AutoProcessor.from_pretrained(
                model_id,
                cache_dir=config.CACHE_DIR
            )
            
            # Download model (large, takes time)
            MusicgenForConditionalGeneration.from_pretrained(
                model_id,
                cache_dir=config.CACHE_DIR,
                torch_dtype=torch.float32
            )
            
            download_time = time.time() - start_time
            logger.info(f"Model {model_size} downloaded in {download_time:.2f}s")
            
            return {
                "success": True,
                "model_size": model_size,
                "download_time": download_time,
                "message": f"Model {model_size} downloaded successfully"
            }
        except Exception as e:
            logger.error(f"Error downloading model {model_size}: {e}")
            return {
                "success": False,
                "model_size": model_size,
                "error": str(e)
            }
    
    def load_model(self, model_size: str = "medium"):
        """Load MusicGen model from HuggingFace by size (downloads if needed)"""
        # Get model ID from config
        if model_size not in config.AVAILABLE_MODELS:
            logger.warning(f"Unknown model size '{model_size}', using medium")
            model_size = "medium"
        
        model_id = config.AVAILABLE_MODELS[model_size]["id"]
        
        # Check if already loaded
        if model_id in self.models:
            logger.info(f"Model {model_size} already loaded")
            self.current_model_id = model_id
            return
        
        logger.info(f"Loading MusicGen model: {model_size} ({model_id})")
        start_time = time.time()
        
        # Load processor and model (will download if not cached)
        processor = AutoProcessor.from_pretrained(
            model_id,
            cache_dir=config.CACHE_DIR
        )
        model = MusicgenForConditionalGeneration.from_pretrained(
            model_id,
            cache_dir=config.CACHE_DIR,
            torch_dtype=torch.float32  # Use float32 for CPU
        ).to(self.device)
        
        # Optimize for CPU
        if config.USE_CPU:
            model.eval()
            # Disable gradient computation
            for param in model.parameters():
                param.requires_grad = False
        
        # Cache the model
        self.models[model_id] = (processor, model)
        self.current_model_id = model_id
        
        load_time = time.time() - start_time
        logger.info(f"MusicGen {model_size} loaded in {load_time:.2f}s")
    
    def get_model(self, model_size: str = "medium"):
        """Get or load a model by size"""
        model_id = config.AVAILABLE_MODELS.get(model_size, config.AVAILABLE_MODELS["medium"])["id"]
        
        if model_id not in self.models:
            self.load_model(model_size)
        
        self.current_model_id = model_id
        return self.models[model_id]
    
    async def generate(
        self,
        prompt: str,
        duration: float,
        model_type: str = "musicgen",
        model_size: str = "medium",
        top_k: int = config.DEFAULT_TOP_K,
        top_p: float = config.DEFAULT_TOP_P,
        temperature: float = config.DEFAULT_TEMPERATURE,
        cfg_coef: float = config.DEFAULT_CFG_COEF
    ) -> Path:
        """Generate audio from text prompt"""
        
        # For AudioGen requests, enhance the prompt for better sound effects
        if model_type == "audiogen":
            # Add sound effect context to the prompt
            if not any(word in prompt.lower() for word in ["sound", "audio", "sfx", "effect"]):
                prompt = f"Sound effect: {prompt}"
            logger.info(f"AudioGen mode - Enhanced prompt: '{prompt}'")
        
        # Load model by size
        processor, model = self.get_model(model_size)
        
        logger.info(f"Generating {duration}s audio with {model_size} model: '{prompt[:50]}...'")
        start_time = time.time()
        
        # Process inputs
        inputs = processor(
            text=[prompt],
            padding=True,
            return_tensors="pt",
        ).to(self.device)
        
        # Calculate max_new_tokens based on duration
        # MusicGen generates at 50 Hz (50 tokens per second)
        max_new_tokens = int(duration * 50)
        
        # Generate audio with optimized parameters
        with torch.no_grad():
            audio_values = model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=True,
                guidance_scale=cfg_coef,
                temperature=temperature,
                top_k=top_k,
                top_p=top_p if top_p > 0 else None,
                num_beams=1,  # Faster generation
            )
        
        generation_time = time.time() - start_time
        logger.info(f"Generation completed in {generation_time:.2f}s")
        
        # Save audio file
        filename = f"{model_type}_{model_size}_{uuid.uuid4().hex[:8]}.wav"
        output_path = config.OUTPUT_DIR / filename
        
        # Get sample rate from model config
        sampling_rate = model.config.audio_encoder.sampling_rate
        
        # Convert to numpy and save
        audio_data = audio_values[0, 0].cpu().numpy()
        
        # Normalize audio to prevent clipping while maintaining dynamics
        max_val = np.max(np.abs(audio_data))
        if max_val > 0:
            audio_data = audio_data / max_val * 0.95
        
        # Save as WAV file with 16-bit PCM
        scipy.io.wavfile.write(
            output_path,
            rate=sampling_rate,
            data=(audio_data * 32767).astype(np.int16)
        )
        
        logger.info(f"Audio saved to {output_path} (sample rate: {sampling_rate}Hz)")
        
        # Clean up old files
        self._cleanup_old_files()
        
        return output_path
    
    def _cleanup_old_files(self):
        """Remove old generated files to save disk space"""
        try:
            files = sorted(
                config.OUTPUT_DIR.glob("*.wav"),
                key=lambda x: x.stat().st_mtime,
                reverse=True
            )
            
            # Keep only the most recent files
            for old_file in files[config.MAX_OUTPUT_FILES:]:
                old_file.unlink()
                logger.debug(f"Cleaned up old file: {old_file.name}")
        except Exception as e:
            logger.error(f"Error during cleanup: {e}")
    
    def unload_model(self, model_size: str):
        """Unload a specific model to free memory"""
        model_id = config.AVAILABLE_MODELS.get(model_size, {}).get("id")
        
        if model_id and model_id in self.models:
            del self.models[model_id]
            logger.info(f"Model {model_size} unloaded")
            
            if torch.cuda.is_available():
                torch.cuda.empty_cache()
            
            return True
        return False
    
    def unload_models(self):
        """Unload all models to free memory"""
        for model_id in list(self.models.keys()):
            del self.models[model_id]
        
        self.models = {}
        self.current_model_id = None
        
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        
        logger.info("All models unloaded")
