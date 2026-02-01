# 🚀 Quick Start Guide

## Start Backend

```bash
cd audiocraft-lite/backend
python main.py
```

Backend will run on: **http://localhost:8000**

## Start Frontend

Open a new terminal:

```bash
cd audiocraft-lite/frontend
npm start
```

Frontend will open automatically at: **http://localhost:3000**

## Using the App

1. **Choose Model Quality**:
   - ⚡ **Small** - Fast (60-70% quality)
   - ⚖️ **Medium** - Balanced (75-85% quality) ✓ Recommended
   - 🎯 **Large** - Best (90-95% quality)

2. **Select Model Type**:
   - 🎹 **MusicGen** - For music generation
   - 🔊 **AudioGen** - For sound effects

3. **Enter Your Prompt**:
   - Be specific and descriptive
   - Example: "Upbeat electronic dance music with heavy bass"

4. **Adjust Settings** (optional):
   - Duration: 1-30 seconds
   - Temperature: 0.1-2.0 (creativity)
   - CFG: 1-10 (prompt adherence)

5. **Click Generate** and wait!

## First Time Setup

The first generation will be slower because:
- Model needs to download (~1-13GB depending on size)
- Model needs to load into memory

After that, it's much faster!

## Recommended Settings

### For Quick Tests
- Model: Small
- Duration: 5s
- CFG: 3.5

### For Production
- Model: Medium
- Duration: 10-15s
- CFG: 4.5

### For Best Quality
- Model: Large
- Duration: 15-30s
- CFG: 5.5

## Troubleshooting

### Backend won't start
```bash
# Make sure you're in the venv
cd audiocraft-lite/backend
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-simple.txt
```

### Frontend won't start
```bash
cd audiocraft-lite/frontend
npm install
npm start
```

### Port already in use
Kill the process:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /F /PID <PID>

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

## Need Help?

- See [MODEL_SELECTION_GUIDE.md](MODEL_SELECTION_GUIDE.md) for model details
- See [QUALITY_GUIDE.md](QUALITY_GUIDE.md) for quality optimization
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues

## System Requirements

- **CPU**: Any modern CPU (4+ cores recommended)
- **RAM**: 
  - Small model: 2GB
  - Medium model: 4GB
  - Large model: 6-8GB
- **Disk**: 15GB free space (for models)
- **OS**: Windows, Mac, or Linux

No GPU required! 🎉
