# AudioCraft Lite - Project Structure

## Directory Overview

```
audiocraft-lite/
├── backend/                    # FastAPI backend server
│   ├── config.py              # Configuration settings
│   ├── main.py                # FastAPI application entry point
│   ├── model_manager.py       # Model loading and inference logic
│   ├── requirements.txt       # Python dependencies
│   ├── Dockerfile            # Docker configuration for backend
│   ├── start.sh              # Linux/Mac startup script
│   ├── start.bat             # Windows startup script
│   └── outputs/              # Generated audio files (created at runtime)
│
├── frontend/                  # React frontend application
│   ├── public/               # Static files
│   │   └── index.html       # HTML template
│   ├── src/                 # React source code
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styling
│   │   ├── index.js        # React entry point
│   │   └── index.css       # Global styles
│   ├── package.json         # Node.js dependencies
│   ├── Dockerfile          # Docker configuration for frontend
│   └── nginx.conf          # Nginx configuration for production
│
├── audiocraft/              # Original AudioCraft repository (cloned)
│   └── [original files]    # Reference implementation
│
├── README.md               # Main project documentation
├── QUICKSTART.md          # Quick start guide
├── SETUP.md               # Detailed setup instructions
├── COMPARISON.md          # Comparison with original AudioCraft
├── LICENSE                # MIT License
├── .gitignore            # Git ignore rules
└── docker-compose.yml    # Docker Compose configuration
```

## Component Details

### Backend (`/backend`)

#### `config.py`
- Server configuration (host, port, CORS)
- Model selection and parameters
- CPU optimization settings
- File management settings
- Generation defaults

#### `main.py`
- FastAPI application setup
- API endpoints:
  - `GET /` - API info
  - `GET /health` - Health check
  - `POST /generate` - Generate audio
  - `GET /models` - List available models
  - `DELETE /outputs/{filename}` - Delete generated file
- CORS middleware
- Static file serving

#### `model_manager.py`
- Model loading (MusicGen, AudioGen)
- CPU optimization
- Audio generation logic
- File cleanup
- Memory management

#### `requirements.txt`
Minimal dependencies:
- FastAPI & Uvicorn (web server)
- PyTorch & torchaudio (ML framework)
- audiocraft (core library)
- Supporting libraries (numpy, soundfile, etc.)

### Frontend (`/frontend`)

#### `src/App.js`
Main React component with:
- Model selection (MusicGen/AudioGen)
- Prompt input
- Parameter controls (duration, temperature, etc.)
- Generation button
- Audio player
- Example prompts
- Error handling

#### `src/App.css`
Modern, responsive styling:
- Gradient background
- Card-based layout
- Smooth animations
- Mobile-responsive design
- Clean, professional look

#### `package.json`
React dependencies:
- React 18
- Axios (HTTP client)
- React Scripts (build tools)

### Docker Setup

#### `docker-compose.yml`
Orchestrates both services:
- Backend on port 8000
- Frontend on port 3000
- Shared volume for model cache
- Automatic restart

#### `backend/Dockerfile`
- Python 3.9 slim base
- FFmpeg installation
- Python dependencies
- Application code

#### `frontend/Dockerfile`
Multi-stage build:
1. Build stage: Compile React app
2. Production stage: Serve with Nginx

## Data Flow

```
User Browser
    ↓
React Frontend (localhost:3000)
    ↓ HTTP POST /generate
FastAPI Backend (localhost:8000)
    ↓
Model Manager
    ↓
AudioCraft Models (MusicGen/AudioGen)
    ↓
Generated Audio File
    ↓ URL returned
Audio Player in Browser
```

## API Flow

1. **User Input**: User enters prompt and settings
2. **Frontend**: Sends POST request to `/generate`
3. **Backend**: Validates request
4. **Model Manager**: Loads model if needed
5. **Generation**: Creates audio using AudioCraft
6. **File Save**: Saves to `outputs/` directory
7. **Response**: Returns audio URL
8. **Frontend**: Displays audio player with file

## Configuration Flow

```
config.py
    ↓
main.py (reads config)
    ↓
model_manager.py (uses config)
    ↓
AudioCraft models (configured)
```

## File Lifecycle

1. **Generation**: Audio created in `backend/outputs/`
2. **Serving**: Accessible via `/outputs/{filename}`
3. **Cleanup**: Old files removed when limit reached
4. **Manual Delete**: User can delete via API

## Development Workflow

### Local Development
1. Start backend: `python backend/main.py`
2. Start frontend: `npm start` in `frontend/`
3. Edit code with hot reload
4. Test at `localhost:3000`

### Production Build
1. Build frontend: `npm run build`
2. Serve with Nginx or similar
3. Run backend with Gunicorn
4. Or use Docker Compose

## Extension Points

### Adding New Models
1. Update `config.py` with model ID
2. Add loading logic in `model_manager.py`
3. Update frontend model selector
4. Add to `/models` endpoint

### Adding Features
1. **Backend**: Add endpoint in `main.py`
2. **Model Logic**: Extend `model_manager.py`
3. **Frontend**: Add UI in `App.js`
4. **Styling**: Update `App.css`

### Custom Configuration
1. Edit `config.py` for backend settings
2. Edit `package.json` for frontend proxy
3. Edit `docker-compose.yml` for deployment

## Security Considerations

- CORS configured for local development
- File cleanup prevents disk filling
- Input validation on all endpoints
- No authentication (add if needed for production)
- Rate limiting not included (add if needed)

## Performance Optimization

### Backend
- CPU thread configuration
- Model caching
- Lazy model loading
- File cleanup
- No gradient computation

### Frontend
- React production build
- Nginx compression
- Static file caching
- Lazy loading

## Monitoring

### Health Check
- `GET /health` endpoint
- Returns system status
- Check model loading state

### Logs
- Backend: Console logs via uvicorn
- Frontend: Browser console
- Docker: `docker-compose logs`

## Backup & Recovery

### Important Files
- `config.py` - Settings
- `outputs/` - Generated audio (if needed)
- Model cache - `~/.cache/audiocraft-lite/`

### Recovery
- Models re-download automatically
- Outputs can be regenerated
- No database to backup

This structure provides a clean separation of concerns, easy deployment, and straightforward extension points for future enhancements.
