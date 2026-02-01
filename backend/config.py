"""Configuration for AudioCraft Lite"""

import os
from pathlib import Path

# Server Configuration
HOST = "0.0.0.0"
PORT = 8000
CORS_ORIGINS = ["http://localhost:3000", "http://127.0.0.1:3000"]

# Model Configuration
# Available models for user selection
AVAILABLE_MODELS = {
    "small": {
        "id": "facebook/musicgen-small",
        "name": "Small (Fast)",
        "params": "300M",
        "quality": "60-70%",
        "speed": "Fast",
        "size_gb": "~2GB",
        "description": "Fastest generation, good for quick previews"
    },
    "medium": {
        "id": "facebook/musicgen-medium",
        "name": "Medium (Balanced)",
        "params": "1.5B",
        "quality": "75-85%",
        "speed": "Medium",
        "size_gb": "~4GB",
        "description": "Best balance of quality and speed"
    },
    "large": {
        "id": "facebook/musicgen-large",
        "name": "Large (Best Quality)",
        "params": "3.3B",
        "quality": "90-95%",
        "speed": "Slow",
        "size_gb": "~6GB",
        "description": "Highest quality, slower generation"
    }
}

# Default model (can be overridden by user selection)
DEFAULT_MODEL_SIZE = "medium"
DEFAULT_MUSICGEN_MODEL = AVAILABLE_MODELS[DEFAULT_MODEL_SIZE]["id"]

# Generation Parameters
MAX_DURATION = 300  # Maximum audio duration in seconds (5 minutes)
DEFAULT_DURATION = 10  # Default generation duration
MIN_DURATION = 1

# CPU Optimization
USE_CPU = True  # Force CPU usage
NUM_THREADS = 4  # Number of CPU threads
ENABLE_QUANTIZATION = False  # Enable int8 quantization for even faster inference

# Memory Management
MAX_BATCH_SIZE = 1  # Process one at a time on CPU
CACHE_DIR = Path.home() / ".cache" / "audiocraft-lite"

# Audio Settings
SAMPLE_RATE = 32000
AUDIO_CHANNELS = 1  # Mono for efficiency, set to 2 for stereo

# File Management
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)
MAX_OUTPUT_FILES = 100  # Keep only last N generated files

# Generation Defaults - Optimized for better quality
DEFAULT_TOP_K = 250
DEFAULT_TOP_P = 0.0
DEFAULT_TEMPERATURE = 1.0
DEFAULT_CFG_COEF = 4.5  # Higher guidance for better prompt adherence
