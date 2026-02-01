"""FastAPI backend for AudioCraft Lite"""

import logging
import uuid
import time
from pathlib import Path
from typing import Optional

import torch
import uvicorn
from fastapi import FastAPI, HTTPException, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import config
from model_manager import ModelManager

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(title="AudioCraft Lite API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=config.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize model manager
model_manager = ModelManager()

# Mount frontend static files (for standalone exe)
frontend_build_dir = Path(__file__).parent.parent / "frontend" / "build"
if frontend_build_dir.exists():
    app.mount("/static", StaticFiles(directory=str(frontend_build_dir / "static")), name="static")

# Mount outputs directory AFTER frontend static (important for priority)
app.mount("/outputs", StaticFiles(directory=str(config.OUTPUT_DIR), html=True), name="outputs")

# Frontend routes (must be last)
if frontend_build_dir.exists():
    @app.get("/")
    async def serve_frontend():
        """Serve the React frontend"""
        return FileResponse(str(frontend_build_dir / "index.html"))
    
    # This must come BEFORE the catch-all route
    @app.get("/files")
    async def view_files_route():
        """Redirect to view_files function"""
        return await view_files()
    
    @app.get("/{full_path:path}")
    async def serve_frontend_routes(full_path: str):
        """Serve frontend for all routes (SPA support)"""
        # Skip if it's an outputs request
        if full_path.startswith("outputs/"):
            return FileResponse(str(config.OUTPUT_DIR / full_path.replace("outputs/", "")))
        
        file_path = frontend_build_dir / full_path
        if file_path.exists() and file_path.is_file():
            return FileResponse(str(file_path))
        return FileResponse(str(frontend_build_dir / "index.html"))


class GenerationRequest(BaseModel):
    prompt: str
    duration: float = config.DEFAULT_DURATION
    model_type: str = "musicgen"  # "musicgen" or "audiogen"
    model_size: str = "medium"  # "small", "medium", or "large"
    top_k: int = config.DEFAULT_TOP_K
    top_p: float = config.DEFAULT_TOP_P
    temperature: float = config.DEFAULT_TEMPERATURE
    cfg_coef: float = config.DEFAULT_CFG_COEF


class GenerationResponse(BaseModel):
    audio_url: str
    filename: str
    duration: float
    model_used: str


@app.get("/")
async def root():
    return {
        "message": "AudioCraft Lite API",
        "version": "1.0.0",
        "status": "running"
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "cpu_available": torch.cuda.is_available() == False or config.USE_CPU,
        "models_loaded": model_manager.is_loaded()
    }


@app.post("/generate", response_model=GenerationResponse)
async def generate_audio(request: GenerationRequest):
    """Generate audio from text prompt"""
    try:
        # Validate duration
        if request.duration < config.MIN_DURATION or request.duration > config.MAX_DURATION:
            raise HTTPException(
                status_code=400,
                detail=f"Duration must be between {config.MIN_DURATION} and {config.MAX_DURATION} seconds"
            )
        
        # Validate prompt
        if not request.prompt or len(request.prompt.strip()) == 0:
            raise HTTPException(status_code=400, detail="Prompt cannot be empty")
        
        logger.info(f"Generating {request.model_type} audio: '{request.prompt[:50]}...'")
        
        # Generate audio
        audio_path = await model_manager.generate(
            prompt=request.prompt,
            duration=request.duration,
            model_type=request.model_type,
            model_size=request.model_size,
            top_k=request.top_k,
            top_p=request.top_p,
            temperature=request.temperature,
            cfg_coef=request.cfg_coef
        )
        
        # Return response
        filename = audio_path.name
        audio_url = f"/outputs/{filename}"
        
        return GenerationResponse(
            audio_url=audio_url,
            filename=filename,
            duration=request.duration,
            model_used=request.model_type
        )
        
    except Exception as e:
        logger.error(f"Generation error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/models")
async def list_models():
    """List available models with download status"""
    return {
        "model_types": {
            "musicgen": {
                "name": "MusicGen",
                "description": "Music generation from text prompts"
            },
            "audiogen": {
                "name": "AudioGen",
                "description": "Sound effects and audio generation"
            }
        },
        "model_sizes": config.AVAILABLE_MODELS,
        "model_status": model_manager.get_model_status()
    }


@app.get("/models/status")
async def get_model_status():
    """Get detailed status of all models"""
    return model_manager.get_model_status()


@app.post("/models/download/{model_size}")
async def download_model(model_size: str):
    """Download a specific model"""
    if model_size not in config.AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail=f"Invalid model size: {model_size}")
    
    try:
        logger.info(f"Starting download for model: {model_size}")
        result = model_manager.download_model(model_size)
        
        if result["success"]:
            return result
        else:
            raise HTTPException(status_code=500, detail=result.get("error", "Download failed"))
    except Exception as e:
        logger.error(f"Error downloading model: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/models/load/{model_size}")
async def load_model(model_size: str):
    """Load a specific model into memory"""
    if model_size not in config.AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail=f"Invalid model size: {model_size}")
    
    try:
        logger.info(f"Loading model: {model_size}")
        model_manager.load_model(model_size)
        return {
            "success": True,
            "model_size": model_size,
            "message": f"Model {model_size} loaded successfully"
        }
    except Exception as e:
        logger.error(f"Error loading model: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/models/unload/{model_size}")
async def unload_model(model_size: str):
    """Unload a specific model from memory"""
    if model_size not in config.AVAILABLE_MODELS:
        raise HTTPException(status_code=400, detail=f"Invalid model size: {model_size}")
    
    try:
        success = model_manager.unload_model(model_size)
        if success:
            return {
                "success": True,
                "model_size": model_size,
                "message": f"Model {model_size} unloaded successfully"
            }
        else:
            return {
                "success": False,
                "model_size": model_size,
                "message": f"Model {model_size} was not loaded"
            }
    except Exception as e:
        logger.error(f"Error unloading model: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/open-folder")
async def open_folder():
    """Open the outputs folder in Windows Explorer"""
    try:
        import subprocess
        import platform
        
        folder_path = str(config.OUTPUT_DIR.absolute())
        
        if platform.system() == "Windows":
            subprocess.Popen(f'explorer "{folder_path}"')
            return {"success": True, "message": "Folder opened"}
        else:
            return {"success": False, "message": "Only supported on Windows"}
    except Exception as e:
        logger.error(f"Error opening folder: {e}")
        return {"success": False, "message": str(e)}


@app.delete("/outputs/{filename}")
async def delete_output(filename: str):
    """Delete a generated audio file"""
    try:
        file_path = config.OUTPUT_DIR / filename
        if file_path.exists():
            file_path.unlink()
            return {"message": "File deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/outputs")
async def list_outputs():
    """List all generated audio files"""
    try:
        files = []
        for file_path in config.OUTPUT_DIR.glob("*.wav"):
            stat = file_path.stat()
            files.append({
                "filename": file_path.name,
                "url": f"/outputs/{file_path.name}",
                "size": stat.st_size,
                "created": stat.st_mtime
            })
        
        # Sort by creation time (newest first)
        files.sort(key=lambda x: x["created"], reverse=True)
        
        return {"files": files, "count": len(files)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/files")
async def view_files():
    """View all generated files in a simple HTML page"""
    try:
        files = []
        for file_path in config.OUTPUT_DIR.glob("*.wav"):
            stat = file_path.stat()
            files.append({
                "filename": file_path.name,
                "url": f"/outputs/{file_path.name}",
                "size": round(stat.st_size / 1024 / 1024, 2),  # MB
                "created": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stat.st_mtime))
            })
        
        # Sort by creation time (newest first)
        files.sort(key=lambda x: x["created"], reverse=True)
        
        # Generate HTML
        html = """
<!DOCTYPE html>
<html>
<head>
    <title>My Audio Files - AudioCraft Lite</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
        }
        h1 {
            color: #667eea;
            margin-bottom: 0.5rem;
            font-size: 2rem;
        }
        .subtitle {
            color: #666;
            margin-bottom: 2rem;
            font-size: 1rem;
        }
        .file-count {
            background: #667eea;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 8px;
            display: inline-block;
            margin-bottom: 1.5rem;
            font-weight: 600;
        }
        .files-grid {
            display: grid;
            gap: 1rem;
        }
        .file-card {
            background: white;
            border: 2px solid #e5e7eb;
            border-radius: 12px;
            padding: 1.5rem;
            display: flex;
            align-items: center;
            gap: 1rem;
            transition: all 0.2s;
        }
        .file-card:hover {
            border-color: #667eea;
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
        }
        .file-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
            flex-shrink: 0;
        }
        .file-info {
            flex: 1;
            min-width: 0;
        }
        .file-name {
            font-weight: 600;
            color: #1f2937;
            margin-bottom: 0.25rem;
            word-break: break-all;
        }
        .file-meta {
            color: #6b7280;
            font-size: 0.875rem;
        }
        .file-actions {
            display: flex;
            gap: 0.5rem;
        }
        .btn {
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 8px;
            font-weight: 500;
            cursor: pointer;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
            font-size: 0.875rem;
        }
        .btn-primary {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
        }
        .btn-secondary {
            background: #f3f4f6;
            color: #374151;
        }
        .btn-secondary:hover {
            background: #e5e7eb;
        }
        .empty-state {
            text-align: center;
            padding: 4rem 2rem;
            color: #6b7280;
        }
        .empty-state-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
        }
        .back-link {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: #667eea;
            text-decoration: none;
            font-weight: 500;
            margin-bottom: 1.5rem;
        }
        .back-link:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <a href="/" class="back-link">← Back to Generator</a>
        <h1>🎵 My Audio Files</h1>
        <p class="subtitle">All your generated audio files</p>
        <div class="file-count">📁 {count} files</div>
        
        <div class="files-grid">
        """.format(count=len(files))
        
        if files:
            for file in files:
                html += f"""
            <div class="file-card">
                <div class="file-icon">🎵</div>
                <div class="file-info">
                    <div class="file-name">{file['filename']}</div>
                    <div class="file-meta">{file['size']} MB • {file['created']}</div>
                </div>
                <div class="file-actions">
                    <audio controls style="height: 32px;">
                        <source src="{file['url']}" type="audio/wav">
                    </audio>
                    <a href="{file['url']}" download class="btn btn-primary">
                        ⬇️ Download
                    </a>
                </div>
            </div>
                """
        else:
            html += """
            <div class="empty-state">
                <div class="empty-state-icon">📭</div>
                <h2>No files yet</h2>
                <p>Generate some audio to see your files here!</p>
            </div>
            """
        
        html += """
        </div>
    </div>
</body>
</html>
        """
        
        return HTMLResponse(content=html)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    logger.info(f"Starting AudioCraft Lite server on {config.HOST}:{config.PORT}")
    logger.info(f"CPU mode: {config.USE_CPU}")
    logger.info(f"Output directory: {config.OUTPUT_DIR}")
    
    uvicorn.run(
        "main:app",
        host=config.HOST,
        port=config.PORT,
        reload=False,
        log_level="info"
    )
