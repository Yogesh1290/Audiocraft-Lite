# AudioCraft Lite - Architecture

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Browser                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              React Frontend (Port 3000)                 │ │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐            │ │
│  │  │  Model   │  │  Prompt  │  │  Audio   │            │ │
│  │  │ Selector │  │  Input   │  │  Player  │            │ │
│  │  └──────────┘  └──────────┘  └──────────┘            │ │
│  └────────────────────────────────────────────────────────┘ │
└───────────────────────────┬─────────────────────────────────┘
                            │ HTTP/REST API
                            ▼
┌─────────────────────────────────────────────────────────────┐
│              FastAPI Backend (Port 8000)                     │
│  ┌────────────────────────────────────────────────────────┐ │
│  │                    API Endpoints                        │ │
│  │  /generate  /health  /models  /outputs                 │ │
│  └──────────────────────┬─────────────────────────────────┘ │
│                         │                                    │
│  ┌──────────────────────▼─────────────────────────────────┐ │
│  │                 Model Manager                           │ │
│  │  ┌──────────────┐         ┌──────────────┐            │ │
│  │  │  MusicGen    │         │  AudioGen    │            │ │
│  │  │   Loader     │         │   Loader     │            │ │
│  │  └──────────────┘         └──────────────┘            │ │
│  └──────────────────────┬─────────────────────────────────┘ │
└─────────────────────────┼─────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                   AudioCraft Models                          │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │   MusicGen-Small │         │  AudioGen-Medium │         │
│  │   (300M params)  │         │                  │         │
│  └──────────────────┘         └──────────────────┘         │
└─────────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    File System                               │
│  ┌──────────────────┐         ┌──────────────────┐         │
│  │  Model Cache     │         │  Output Files    │         │
│  │  ~/.cache/       │         │  ./outputs/      │         │
│  └──────────────────┘         └──────────────────┘         │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### Frontend Layer

```
App.js (Main Component)
├── State Management
│   ├── Model Selection (musicgen/audiogen)
│   ├── User Input (prompt, parameters)
│   ├── Generation State (loading, result, error)
│   └── UI State (active controls)
│
├── UI Components
│   ├── Header (title, description)
│   ├── Model Selector (toggle buttons)
│   ├── Prompt Input (textarea)
│   ├── Parameter Controls (sliders, inputs)
│   ├── Generate Button
│   ├── Loading Indicator
│   ├── Audio Player (result)
│   ├── Error Display
│   └── Example Prompts (clickable)
│
└── API Integration
    └── Axios HTTP Client
        ├── POST /generate
        ├── GET /health
        └── Error Handling
```

### Backend Layer

```
main.py (FastAPI App)
├── Middleware
│   ├── CORS (cross-origin requests)
│   └── Static Files (outputs directory)
│
├── Endpoints
│   ├── GET /
│   │   └── API information
│   ├── GET /health
│   │   └── System status
│   ├── POST /generate
│   │   ├── Request validation
│   │   ├── Model manager call
│   │   └── Response formatting
│   ├── GET /models
│   │   └── Available models list
│   └── DELETE /outputs/{filename}
│       └── File deletion
│
└── Dependencies
    ├── ModelManager instance
    └── Configuration
```

### Model Manager

```
model_manager.py
├── Initialization
│   ├── Device selection (CPU/GPU)
│   ├── Thread configuration
│   └── Model references
│
├── Model Loading
│   ├── load_musicgen()
│   │   ├── Download if needed
│   │   ├── Load to device
│   │   └── Optimize for CPU
│   └── load_audiogen()
│       ├── Download if needed
│       ├── Load to device
│       └── Optimize for CPU
│
├── Generation
│   └── generate()
│       ├── Model selection
│       ├── Parameter setting
│       ├── Inference (torch.no_grad)
│       ├── Audio writing
│       └── Cleanup
│
└── Utilities
    ├── is_loaded()
    ├── _cleanup_old_files()
    └── unload_models()
```

## Data Flow

### Generation Request Flow

```
1. User Input
   ↓
2. Frontend Validation
   ↓
3. HTTP POST /generate
   {
     "prompt": "...",
     "duration": 10,
     "model_type": "musicgen",
     "temperature": 1.0,
     "top_k": 250,
     "cfg_coef": 3.0
   }
   ↓
4. Backend Validation
   ↓
5. Model Manager
   ├── Load model (if needed)
   ├── Set parameters
   └── Generate audio
   ↓
6. Save to File
   outputs/musicgen_abc123.wav
   ↓
7. HTTP Response
   {
     "audio_url": "/outputs/musicgen_abc123.wav",
     "filename": "musicgen_abc123.wav",
     "duration": 10,
     "model_used": "musicgen"
   }
   ↓
8. Frontend Display
   └── Audio Player with URL
```

### Model Loading Flow

```
First Request
   ↓
Model Manager Check
   ↓
Model Not Loaded
   ↓
Download from HuggingFace
   ├── Model weights
   ├── Configuration
   └── Tokenizer
   ↓
Cache to ~/.cache/audiocraft-lite/
   ↓
Load to Memory
   ├── Initialize model
   ├── Load weights
   └── Move to device (CPU)
   ↓
Optimize
   ├── Set eval mode
   ├── Disable gradients
   └── Configure threads
   ↓
Ready for Inference

Subsequent Requests
   ↓
Model Already Loaded
   ↓
Direct Inference
```

## Technology Stack

### Frontend Stack

```
React 18
├── Core
│   ├── React (UI library)
│   ├── React DOM (rendering)
│   └── React Scripts (build tools)
│
├── HTTP
│   └── Axios (API client)
│
├── Styling
│   └── CSS3 (custom styles)
│
└── Build
    ├── Webpack (bundler)
    ├── Babel (transpiler)
    └── ESLint (linter)
```

### Backend Stack

```
Python 3.9+
├── Web Framework
│   ├── FastAPI (API framework)
│   ├── Uvicorn (ASGI server)
│   └── Pydantic (validation)
│
├── ML Framework
│   ├── PyTorch 2.1.0 (deep learning)
│   ├── torchaudio (audio processing)
│   └── audiocraft (models)
│
├── Audio Processing
│   ├── soundfile (I/O)
│   ├── numpy (arrays)
│   └── einops (tensor ops)
│
└── Utilities
    ├── transformers (tokenizers)
    └── sentencepiece (text processing)
```

## Deployment Architecture

### Development

```
Developer Machine
├── Terminal 1: Backend
│   └── python main.py
│       └── localhost:8000
│
└── Terminal 2: Frontend
    └── npm start
        └── localhost:3000
            └── Proxy to :8000
```

### Docker

```
Docker Compose
├── Backend Container
│   ├── Python 3.9-slim
│   ├── FastAPI app
│   ├── Port 8000
│   └── Volume: model-cache
│
└── Frontend Container
    ├── Node 18 (build)
    ├── Nginx (serve)
    ├── Port 3000
    └── Proxy to backend
```

### Production

```
Server
├── Nginx (Reverse Proxy)
│   ├── Port 80/443
│   ├── SSL/TLS
│   └── Static files
│       ↓
├── Frontend (Static)
│   └── React build
│       ↓
└── Backend (Gunicorn)
    ├── Multiple workers
    ├── Uvicorn workers
    └── Port 8000
```

## Security Architecture

```
Request Flow
├── CORS Validation
│   └── Allowed origins check
│
├── Input Validation
│   ├── Type checking (Pydantic)
│   ├── Range validation
│   └── Length limits
│
├── Resource Protection
│   ├── File size limits
│   ├── Generation timeouts
│   └── Memory management
│
└── Output Sanitization
    └── Filename validation
```

## Scalability Considerations

### Current Architecture
- Single-threaded generation
- One request at a time
- Local file storage
- In-memory model cache

### Scaling Options

```
Horizontal Scaling
├── Load Balancer
│   ├── Backend Instance 1
│   ├── Backend Instance 2
│   └── Backend Instance N
│
├── Shared Storage
│   └── S3/Cloud Storage
│
└── Model Cache
    └── Shared volume or CDN
```

### Performance Optimization

```
Optimization Layers
├── Frontend
│   ├── Code splitting
│   ├── Lazy loading
│   ├── Asset compression
│   └── CDN delivery
│
├── Backend
│   ├── Model caching
│   ├── Response caching
│   ├── Connection pooling
│   └── Async processing
│
└── Infrastructure
    ├── CPU optimization
    ├── Memory management
    ├── Disk I/O
    └── Network optimization
```

## Monitoring Architecture

```
Observability
├── Logging
│   ├── Application logs
│   ├── Access logs
│   └── Error logs
│
├── Metrics
│   ├── Request count
│   ├── Response time
│   ├── Error rate
│   └── Resource usage
│
└── Health Checks
    ├── /health endpoint
    ├── Model status
    └── System resources
```

This architecture provides a clean separation of concerns, easy maintenance, and straightforward scaling paths as needs grow.
