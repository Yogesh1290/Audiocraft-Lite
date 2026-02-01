# AudioCraft Lite - Setup Guide

## Prerequisites

- Python 3.9 or higher
- Node.js 16 or higher
- 4GB+ RAM (8GB recommended for better performance)
- ~2GB disk space for models

## Quick Start

### Option 1: Automated Setup (Recommended)

#### Windows
```bash
cd audiocraft-lite/backend
start.bat
```

In a new terminal:
```bash
cd audiocraft-lite/frontend
npm install
npm start
```

#### Linux/Mac
```bash
cd audiocraft-lite/backend
chmod +x start.sh
./start.sh
```

In a new terminal:
```bash
cd audiocraft-lite/frontend
npm install
npm start
```

### Option 2: Manual Setup

#### Backend Setup

1. Navigate to backend directory:
```bash
cd audiocraft-lite/backend
```

2. Create virtual environment:
```bash
python -m venv venv
```

3. Activate virtual environment:
- Windows: `venv\Scripts\activate`
- Linux/Mac: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Start the server:
```bash
python main.py
```

The backend will be available at `http://localhost:8000`

#### Frontend Setup

1. Navigate to frontend directory:
```bash
cd audiocraft-lite/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm start
```

The frontend will open automatically at `http://localhost:3000`

## First Run

On the first run, the application will download the AI models (~500MB-1GB). This may take a few minutes depending on your internet connection.

Models are cached in `~/.cache/audiocraft-lite/` for future use.

## Configuration

Edit `backend/config.py` to customize:

- **Model Selection**: Change `DEFAULT_MUSICGEN_MODEL` to use different model sizes
  - `facebook/musicgen-small` (300M) - Fastest, good quality
  - `facebook/musicgen-medium` (1.5B) - Better quality, slower
  - `facebook/musicgen-large` (3.3B) - Best quality, slowest

- **CPU Threads**: Adjust `NUM_THREADS` based on your CPU
  - 2-4 threads for dual-core CPUs
  - 4-8 threads for quad-core CPUs
  - 8+ threads for high-end CPUs

- **Memory Management**: Adjust `MAX_OUTPUT_FILES` to control disk usage

## Performance Tips

### For Better CPU Performance:

1. Close other applications to free up CPU resources
2. Use smaller models (musicgen-small)
3. Generate shorter audio clips (5-10 seconds)
4. Reduce `NUM_THREADS` if system becomes unresponsive

### For Better Quality:

1. Use larger models (musicgen-medium or large)
2. Increase generation duration
3. Adjust temperature (0.8-1.2 for more creative outputs)
4. Fine-tune CFG coefficient (2.5-4.0 for better prompt adherence)

## Troubleshooting

### Backend won't start
- Ensure Python 3.9+ is installed: `python --version`
- Check if port 8000 is available
- Try reinstalling dependencies: `pip install -r requirements.txt --force-reinstall`

### Frontend won't start
- Ensure Node.js is installed: `node --version`
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`

### Out of Memory errors
- Use smaller model in `config.py`
- Reduce generation duration
- Close other applications
- Restart the backend

### Slow generation
- This is normal on CPU! Generation can take 30s-2min depending on:
  - CPU speed
  - Model size
  - Audio duration
- Consider using a GPU-enabled machine for faster generation

### Audio quality issues
- Try different temperature values (0.8-1.2)
- Adjust CFG coefficient (2.5-4.0)
- Use more descriptive prompts
- Try the medium or large models

## API Documentation

Once the backend is running, visit:
- API docs: `http://localhost:8000/docs`
- Health check: `http://localhost:8000/health`

## Building for Production

### Frontend
```bash
cd frontend
npm run build
```

The optimized build will be in `frontend/build/`

### Backend
Use a production ASGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn main:app -w 1 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## Support

For issues and questions:
- Check the main README.md
- Review the original AudioCraft documentation
- Open an issue on GitHub
