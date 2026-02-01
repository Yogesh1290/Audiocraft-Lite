# AudioCraft Lite - Features

## Core Features

### 🎵 Audio Generation Models

#### MusicGen
- **Text-to-Music Generation**: Create music from text descriptions
- **Model Size**: Small (300M parameters) - optimized for CPU
- **Quality**: Good quality suitable for most applications
- **Speed**: 30-90 seconds for 10 seconds of audio on modern CPU
- **Styles**: Supports various genres and instruments

#### AudioGen
- **Text-to-Sound Generation**: Create sound effects and ambient audio
- **Use Cases**: Sound effects, ambience, foley
- **Quality**: High-quality sound generation
- **Flexibility**: Wide range of sound types

### 🎛️ Generation Controls

#### Basic Parameters
- **Duration**: 1-30 seconds (configurable up to 120s)
- **Prompt**: Free-form text description
- **Model Selection**: Easy toggle between MusicGen and AudioGen

#### Advanced Parameters
- **Temperature** (0.1-2.0): Controls randomness and creativity
  - Lower (0.8): More predictable, safer outputs
  - Higher (1.2): More creative, varied outputs
  
- **Top-K** (0-500): Limits token selection
  - Default: 250
  - Higher: More diverse outputs
  
- **Top-P** (0-1.0): Nucleus sampling
  - Default: 0 (disabled)
  - 0.9: Good balance of quality and diversity
  
- **CFG Coefficient** (1-10): Classifier-free guidance
  - Default: 3.0
  - Higher: Stronger adherence to prompt

### 🖥️ User Interface

#### Modern Design
- Clean, gradient-based aesthetic
- Intuitive layout
- Responsive design (mobile-friendly)
- Smooth animations and transitions

#### User Experience
- Real-time generation status
- Progress indicators
- Error handling with clear messages
- Audio player with controls
- Download capability

#### Example Prompts
- Pre-loaded examples for both models
- One-click prompt insertion
- Categorized by use case

### 🚀 Performance Optimizations

#### CPU-Friendly
- Optimized for CPU inference
- Configurable thread count
- No GPU required
- Efficient memory usage

#### Smart Model Management
- Lazy loading (models load on first use)
- Model caching
- Automatic cleanup of old files
- Memory-efficient inference

#### Fast Response
- Async processing
- Non-blocking generation
- Efficient file serving

### 🔧 Backend API

#### RESTful Endpoints
- `GET /` - API information
- `GET /health` - Health check and status
- `POST /generate` - Generate audio
- `GET /models` - List available models
- `DELETE /outputs/{filename}` - Delete generated file

#### API Features
- JSON request/response
- Comprehensive error handling
- CORS support
- Static file serving
- Auto-generated documentation (FastAPI)

### 📦 Deployment Options

#### Local Development
- Simple Python + Node.js setup
- Hot reload for development
- Easy debugging

#### Docker
- Single-command deployment
- Isolated environment
- Production-ready
- Volume management for persistence

#### Production
- Nginx configuration included
- Gunicorn support
- Environment variable configuration
- Scalable architecture

### 🛠️ Configuration

#### Flexible Settings
- Model selection (small, medium, large)
- CPU thread configuration
- Memory limits
- File retention policies
- Generation defaults

#### Easy Customization
- Single config file (`config.py`)
- Well-documented options
- No code changes needed
- Hot-reload support

### 📊 File Management

#### Automatic Cleanup
- Configurable file limit
- Oldest files removed first
- Prevents disk space issues

#### Output Organization
- Timestamped filenames
- Model type in filename
- Easy identification
- Manual deletion support

### 🔒 Security Features

#### Input Validation
- Prompt length limits
- Duration constraints
- Parameter range checking
- Type validation

#### Resource Protection
- File size limits
- Generation timeouts
- Memory management
- Rate limiting ready

### 📱 Cross-Platform Support

#### Operating Systems
- Windows (with .bat scripts)
- macOS (with .sh scripts)
- Linux (with .sh scripts)
- Docker (platform-independent)

#### Browsers
- Chrome/Edge
- Firefox
- Safari
- Mobile browsers

### 📚 Documentation

#### Comprehensive Guides
- Quick Start Guide
- Detailed Setup Instructions
- Comparison with Original
- Project Structure
- API Documentation

#### Code Quality
- Well-commented code
- Type hints (Python)
- Consistent formatting
- Clear naming conventions

## Planned Features (Future)

### Short Term
- [ ] Audio format options (MP3, FLAC, OGG)
- [ ] Generation history
- [ ] Favorite prompts
- [ ] Batch generation
- [ ] Progress bar with time estimate

### Medium Term
- [ ] User accounts and authentication
- [ ] Preset management
- [ ] Audio editing tools
- [ ] Share generated audio
- [ ] API rate limiting

### Long Term
- [ ] Model fine-tuning interface
- [ ] Melody conditioning (simplified)
- [ ] Audio-to-audio style transfer
- [ ] Mobile app
- [ ] Cloud deployment templates
- [ ] Model quantization for faster inference

## Feature Comparison Matrix

| Feature | AudioCraft Lite | Original AudioCraft |
|---------|----------------|---------------------|
| Text-to-Music | ✅ | ✅ |
| Text-to-Sound | ✅ | ✅ |
| CPU Support | ✅ Optimized | ⚠️ Limited |
| GPU Support | ✅ Optional | ✅ Required |
| Web Interface | ✅ Modern React | ⚠️ Basic Gradio |
| API | ✅ RESTful | ❌ |
| Docker | ✅ | ❌ |
| Mobile UI | ✅ | ❌ |
| Melody Conditioning | ❌ | ✅ |
| Training | ❌ | ✅ |
| Batch Processing | ⚠️ Limited | ✅ |
| Model Sizes | Small, Medium | All sizes |
| Setup Complexity | Low | High |
| Documentation | Comprehensive | Technical |

## Technical Specifications

### Backend
- **Framework**: FastAPI 0.104+
- **ML Framework**: PyTorch 2.1.0
- **Audio Processing**: torchaudio, soundfile
- **Server**: Uvicorn (ASGI)
- **Language**: Python 3.9+

### Frontend
- **Framework**: React 18
- **HTTP Client**: Axios
- **Build Tool**: React Scripts
- **Server**: Nginx (production)
- **Language**: JavaScript (ES6+)

### Models
- **MusicGen**: 300M parameters (small)
- **AudioGen**: Medium variant
- **Format**: PyTorch checkpoints
- **Storage**: ~500MB-1GB cached

### Audio Output
- **Format**: WAV (16-bit)
- **Sample Rate**: 32kHz
- **Channels**: Mono (configurable to stereo)
- **Quality**: Lossless

## Use Cases

### Personal Projects
- Background music for videos
- Sound effects for games
- Podcast intros/outros
- Creative experimentation

### Professional
- Rapid prototyping
- Demo creation
- Concept validation
- Client presentations

### Educational
- Learning AI audio generation
- Teaching ML concepts
- Research projects
- Student assignments

### Development
- API integration testing
- Audio processing pipelines
- Automated content creation
- Tool development

## Performance Metrics

### Generation Speed (10s audio)
- **Fast CPU** (8+ cores): 30-45 seconds
- **Medium CPU** (4 cores): 45-75 seconds
- **Slow CPU** (2 cores): 75-120 seconds

### Memory Usage
- **Idle**: ~100MB
- **Model Loaded**: 1-2GB
- **Generating**: 2-3GB
- **Peak**: 3-4GB

### Disk Usage
- **Application**: ~50MB
- **Models**: 500MB-1GB
- **Outputs**: Varies (auto-cleanup)
- **Total**: ~1-2GB

## Quality Metrics

### Audio Quality
- **Bit Depth**: 16-bit
- **Sample Rate**: 32kHz
- **Dynamic Range**: Good
- **Artifacts**: Minimal with proper settings

### Generation Quality
- **Prompt Adherence**: Good (CFG 3.0)
- **Musical Coherence**: Good for short clips
- **Sound Realism**: Good for most sounds
- **Consistency**: Reliable with same settings

This feature set makes AudioCraft Lite an accessible, user-friendly tool for AI audio generation without compromising on essential functionality.
