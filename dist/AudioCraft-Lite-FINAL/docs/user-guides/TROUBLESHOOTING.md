# AudioCraft Lite - Troubleshooting Guide

## Common Issues and Solutions

### Installation Issues

#### Python Version Error
```
ERROR: Python 3.9 or higher is required
```

**Solution:**
```bash
# Check your Python version
python --version

# If too old, download Python 3.9+ from python.org
# Or use pyenv to manage multiple versions
```

#### Node.js Version Error
```
ERROR: Node.js 16 or higher is required
```

**Solution:**
```bash
# Check your Node version
node --version

# Download latest from nodejs.org
# Or use nvm to manage versions
```

#### pip install fails
```
ERROR: Could not find a version that satisfies the requirement torch==2.1.0
```

**Solution:**
```bash
# Update pip first
python -m pip install --upgrade pip

# Install PyTorch separately
pip install torch==2.1.0 --index-url https://download.pytorch.org/whl/cpu

# Then install other requirements
pip install -r requirements.txt
```

### Backend Issues

#### Port 8000 Already in Use
```
ERROR: [Errno 48] Address already in use
```

**Solution 1 - Change Port:**
Edit `backend/config.py`:
```python
PORT = 8001  # Use different port
```

**Solution 2 - Kill Process:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

#### Module Not Found Error
```
ModuleNotFoundError: No module named 'audiocraft'
```

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

# Reinstall requirements
pip install -r requirements.txt
```

#### Out of Memory Error
```
RuntimeError: [enforce fail at alloc_cpu.cpp:114] . DefaultCPUAllocator: not enough memory
```

**Solution:**
Edit `backend/config.py`:
```python
# Use smaller model
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-small"

# Reduce threads
NUM_THREADS = 2

# Generate shorter audio
DEFAULT_DURATION = 5
```

Also:
- Close other applications
- Restart your computer
- Increase system swap/page file

#### Model Download Fails
```
HTTPError: 403 Client Error: Forbidden for url
```

**Solution:**
```bash
# Check internet connection
# Try manual download
python -c "from audiocraft.models import MusicGen; MusicGen.get_pretrained('facebook/musicgen-small')"

# If behind proxy, set environment variables
export HTTP_PROXY=http://proxy:port
export HTTPS_PROXY=http://proxy:port
```

#### FFmpeg Not Found
```
FileNotFoundError: [Errno 2] No such file or directory: 'ffmpeg'
```

**Solution:**
```bash
# Windows: Download from ffmpeg.org and add to PATH
# Or use chocolatey
choco install ffmpeg

# Mac
brew install ffmpeg

# Linux
sudo apt-get install ffmpeg
```

### Frontend Issues

#### npm install fails
```
npm ERR! code ERESOLVE
```

**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Install with legacy peer deps
npm install --legacy-peer-deps
```

#### Port 3000 Already in Use
```
Something is already running on port 3000
```

**Solution:**
```bash
# Use different port
PORT=3001 npm start

# Or kill process on port 3000
# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F

# Mac/Linux
lsof -ti:3000 | xargs kill -9
```

#### Proxy Error
```
Proxy error: Could not proxy request
```

**Solution:**
1. Make sure backend is running on port 8000
2. Check `package.json` has correct proxy:
```json
"proxy": "http://localhost:8000"
```
3. Restart frontend: `npm start`

#### Blank Page After Build
```
White screen, no errors in console
```

**Solution:**
Check `package.json` for correct homepage:
```json
"homepage": ".",
```

Then rebuild:
```bash
npm run build
```

### Runtime Issues

#### Slow Generation
```
Generation takes 5+ minutes
```

**Solution:**
This is normal on slower CPUs. To improve:

1. **Use smaller model:**
```python
# config.py
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-small"
```

2. **Reduce duration:**
```python
DEFAULT_DURATION = 5  # Start with 5 seconds
```

3. **Optimize CPU:**
```python
NUM_THREADS = 4  # Match your CPU cores
```

4. **Close other apps** to free CPU resources

5. **First generation is slowest** (model loading)

#### Poor Audio Quality
```
Audio sounds distorted or low quality
```

**Solution:**
1. **Adjust temperature:**
```
Try values between 0.8 and 1.2
```

2. **Increase CFG coefficient:**
```
Try values between 3.0 and 5.0
```

3. **Use better prompts:**
```
Bad:  "music"
Good: "Upbeat electronic dance music with synthesizers and drums"
```

4. **Try medium model** (if you have RAM):
```python
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-medium"
```

#### Generation Fails Silently
```
Button says "Generating..." but nothing happens
```

**Solution:**
1. Check browser console (F12) for errors
2. Check backend terminal for errors
3. Test backend directly:
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"test","duration":5,"model_type":"musicgen"}'
```

#### CORS Error
```
Access to fetch blocked by CORS policy
```

**Solution:**
Edit `backend/config.py`:
```python
CORS_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:3001",  # Add your port
]
```

Restart backend.

### Docker Issues

#### Docker Compose Fails
```
ERROR: Service 'backend' failed to build
```

**Solution:**
```bash
# Check Docker is running
docker --version

# Clean up and rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

#### Container Out of Memory
```
Container killed due to memory limit
```

**Solution:**
Increase Docker memory limit:
- Docker Desktop → Settings → Resources → Memory
- Increase to 8GB minimum

Or edit `docker-compose.yml`:
```yaml
services:
  backend:
    mem_limit: 8g
```

#### Volume Permission Issues
```
Permission denied: '/root/.cache'
```

**Solution:**
```bash
# Linux: Fix permissions
sudo chown -R $USER:$USER ./backend/outputs

# Or run with user
docker-compose run --user $(id -u):$(id -g) backend
```

### Performance Issues

#### High CPU Usage
```
CPU at 100% constantly
```

**Solution:**
This is normal during generation. To reduce:

1. **Lower thread count:**
```python
NUM_THREADS = 2
```

2. **Generate shorter audio**

3. **Wait between generations**

4. **Use task manager to set process priority to "Below Normal"**

#### High Memory Usage
```
System becomes unresponsive
```

**Solution:**
1. **Use smaller model**
2. **Reduce NUM_THREADS**
3. **Close other applications**
4. **Increase system swap space**
5. **Restart backend between generations**

#### Disk Space Issues
```
No space left on device
```

**Solution:**
1. **Clean old outputs:**
```bash
rm backend/outputs/*.wav
```

2. **Reduce MAX_OUTPUT_FILES:**
```python
MAX_OUTPUT_FILES = 10  # Keep fewer files
```

3. **Clear model cache if needed:**
```bash
rm -rf ~/.cache/audiocraft-lite
```

### API Issues

#### 422 Validation Error
```json
{
  "detail": [
    {
      "loc": ["body", "duration"],
      "msg": "value is not a valid float"
    }
  ]
}
```

**Solution:**
Check your request format:
```json
{
  "prompt": "string",
  "duration": 10.0,
  "model_type": "musicgen",
  "temperature": 1.0,
  "top_k": 250,
  "cfg_coef": 3.0
}
```

#### 500 Internal Server Error
```
Internal Server Error
```

**Solution:**
1. Check backend logs for detailed error
2. Common causes:
   - Out of memory
   - Model not loaded
   - Invalid parameters
   - Disk full

### Audio Playback Issues

#### Audio Won't Play in Browser
```
Audio element shows but no sound
```

**Solution:**
1. **Check browser console** for errors
2. **Verify file exists:**
```bash
ls backend/outputs/
```
3. **Check file permissions**
4. **Try different browser**
5. **Check audio format support**

#### Choppy Audio Playback
```
Audio stutters or skips
```

**Solution:**
1. **Download file** instead of streaming
2. **Check CPU usage** during playback
3. **Try different browser**
4. **Convert to MP3** if needed

## Debugging Tips

### Enable Debug Logging

**Backend:**
Edit `backend/main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Frontend:**
Add to `src/App.js`:
```javascript
console.log('State:', { prompt, duration, modelType });
```

### Test Backend Directly

```bash
# Health check
curl http://localhost:8000/health

# List models
curl http://localhost:8000/models

# Generate (simple)
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt":"test music","duration":5,"model_type":"musicgen"}'
```

### Check System Resources

```bash
# CPU and Memory
# Windows
taskmgr

# Mac
Activity Monitor

# Linux
htop
```

### Verify Installation

```bash
# Backend
cd backend
source venv/bin/activate
python -c "import torch; import audiocraft; print('OK')"

# Frontend
cd frontend
npm list react
```

## Getting Help

### Before Asking for Help

1. ✅ Check this troubleshooting guide
2. ✅ Read error messages carefully
3. ✅ Check backend and frontend logs
4. ✅ Try with default settings
5. ✅ Test with example prompts
6. ✅ Verify system requirements

### When Asking for Help

Include:
- Operating system and version
- Python version (`python --version`)
- Node version (`node --version`)
- Error messages (full text)
- Steps to reproduce
- What you've already tried

### Useful Commands

```bash
# System info
python --version
node --version
npm --version
docker --version

# Check processes
# Windows
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Mac/Linux
lsof -i :8000
lsof -i :3000

# Check disk space
df -h  # Mac/Linux
dir    # Windows

# Check memory
free -h  # Linux
vm_stat  # Mac
```

## Still Having Issues?

1. **Try Docker** - Eliminates many environment issues
2. **Fresh install** - Delete everything and start over
3. **Check original AudioCraft** - See if issue exists there too
4. **Simplify** - Test with minimal settings first
5. **Update** - Make sure all dependencies are latest versions

## Known Limitations

- **CPU-only**: Slower than GPU (expected)
- **Memory**: Needs 4GB+ RAM minimum
- **Duration**: Long generations (30s+) take time
- **Quality**: Small model has limitations
- **Concurrent**: One generation at a time
- **Melody**: No melody conditioning (by design)

These are not bugs - they're trade-offs for CPU-friendly operation.

---

If you've tried everything and still have issues, consider:
- Using the original AudioCraft with GPU
- Upgrading your hardware
- Using a cloud service with better resources
