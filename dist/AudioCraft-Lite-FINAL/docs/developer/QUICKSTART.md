# AudioCraft Lite - Quick Start Guide

Get up and running in 5 minutes!

## Prerequisites Check

```bash
# Check Python version (need 3.9+)
python --version

# Check Node.js version (need 16+)
node --version

# If missing, install from:
# Python: https://www.python.org/downloads/
# Node.js: https://nodejs.org/
```

## Installation

### Step 1: Clone or Download
```bash
cd audiocraft-lite
```

### Step 2: Start Backend (Terminal 1)

**Windows:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

**Mac/Linux:**
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py
```

Wait for: `INFO: Uvicorn running on http://0.0.0.0:8000`

### Step 3: Start Frontend (Terminal 2)

```bash
cd frontend
npm install
npm start
```

Browser will open automatically at `http://localhost:3000`

## First Use

1. **Choose Model**: Click "MusicGen" for music or "AudioGen" for sound effects

2. **Enter Prompt**: Describe what you want
   - Example: "Upbeat electronic dance music with synthesizers"

3. **Adjust Settings** (optional):
   - Duration: 5-10 seconds recommended for first try
   - Keep other settings at defaults

4. **Generate**: Click "Generate Audio"
   - First generation downloads models (~500MB)
   - Takes 30-90 seconds on CPU
   - Subsequent generations are faster

5. **Listen**: Audio player appears when ready

## Example Prompts

### Music (MusicGen)
```
"Calm piano melody perfect for studying"
"Energetic rock song with electric guitar"
"Lo-fi hip hop beats with jazzy elements"
"Epic orchestral soundtrack with strings"
```

### Sounds (AudioGen)
```
"Rain falling with distant thunder"
"Busy coffee shop ambience"
"Ocean waves on a beach"
"Forest with birds chirping"
```

## Tips for Better Results

1. **Be Specific**: "Upbeat jazz piano with walking bass" > "jazz music"
2. **Include Instruments**: Mention specific instruments you want
3. **Set the Mood**: Add descriptors like "calm", "energetic", "dark"
4. **Start Short**: Try 5-10 seconds first, then increase
5. **Experiment**: Try different temperature values (0.8-1.2)

## Troubleshooting

### "Connection refused" error
- Make sure backend is running (Terminal 1)
- Check `http://localhost:8000/health` in browser

### Slow generation
- Normal on CPU! First generation is slowest
- Close other applications
- Try shorter duration (5 seconds)

### Out of memory
- Edit `backend/config.py`
- Change to `DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-small"`
- Restart backend

### Port already in use
- Backend: Change `PORT = 8000` in `backend/config.py`
- Frontend: Set `PORT=3001 npm start`

## Docker Quick Start (Alternative)

If you have Docker installed:

```bash
docker-compose up
```

That's it! Access at `http://localhost:3000`

## Next Steps

- Read [SETUP.md](SETUP.md) for detailed configuration
- Check [COMPARISON.md](COMPARISON.md) to understand differences from original
- Explore API at `http://localhost:8000/docs`

## Common Questions

**Q: How long does generation take?**
A: 30-90 seconds for 10 seconds of audio on a modern CPU.

**Q: Can I use GPU?**
A: Yes! Edit `config.py` and set `USE_CPU = False`

**Q: Where are models stored?**
A: `~/.cache/audiocraft-lite/` (about 500MB-1GB)

**Q: Can I generate longer audio?**
A: Yes, up to 30 seconds. Edit `MAX_DURATION` in `config.py` for more.

**Q: Is this free?**
A: Yes! MIT licensed, free to use and modify.

## Support

Having issues? Check:
1. Both terminals are running
2. No error messages in terminals
3. Correct Python/Node versions
4. Enough disk space (2GB+)
5. Enough RAM (4GB+)

Enjoy creating AI-generated audio! 🎵
