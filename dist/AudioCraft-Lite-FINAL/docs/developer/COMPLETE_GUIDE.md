# 🎵 AudioCraft Lite - Complete User Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Model Selection](#model-selection)
3. [Using the Interface](#using-the-interface)
4. [Writing Good Prompts](#writing-good-prompts)
5. [Advanced Settings](#advanced-settings)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### 1. Start Backend
```bash
cd audiocraft-lite/backend
python main.py
```
✅ Backend running at http://localhost:8000

### 2. Start Frontend
```bash
cd audiocraft-lite/frontend
npm start
```
✅ Frontend opens at http://localhost:3000

### 3. Generate Audio!
1. Select model quality (Small/Medium/Large)
2. Choose model type (MusicGen/AudioGen)
3. Enter your prompt
4. Click "Generate Audio"
5. Wait and enjoy!

---

## Model Selection

### ⚡ Small (Fast)
- **Quality**: 60-70%
- **Speed**: 10-20 seconds for 10s audio
- **RAM**: ~2GB
- **Use when**: Testing prompts, quick iterations

### ⚖️ Medium (Balanced) ✓ RECOMMENDED
- **Quality**: 75-85%
- **Speed**: 30-40 seconds for 10s audio
- **RAM**: ~4GB
- **Use when**: Production work, most use cases

### 🎯 Large (Best Quality)
- **Quality**: 90-95%
- **Speed**: 60-90 seconds for 10s audio
- **RAM**: ~6-8GB
- **Use when**: Final production, maximum quality needed

### How to Choose?
```
Quick test → Small
Normal use → Medium
Best quality → Large
```

---

## Using the Interface

### Model Type Selection

#### 🎹 MusicGen
For generating music:
- Songs
- Instrumentals
- Background music
- Musical compositions

#### 🔊 AudioGen
For generating sounds:
- Sound effects
- Ambient sounds
- Nature sounds
- Environmental audio

### Main Controls

#### Prompt (Required)
- Describe what you want to generate
- Be specific and detailed
- Use descriptive adjectives

#### Duration (1-30 seconds)
- **5s**: Quick previews
- **10s**: Standard length
- **15-30s**: Full musical ideas

#### Temperature (0.1-2.0)
- **0.5-0.8**: More consistent, predictable
- **1.0**: Balanced (default)
- **1.2-1.5**: More creative, varied

#### Top-K (0-500)
- **250**: Default, good balance
- **Lower (100-200)**: More focused
- **Higher (300-400)**: More diverse

#### CFG Coefficient (1-10)
- **3.0-4.0**: More creative freedom
- **4.5**: Balanced (default)
- **5.0-6.0**: Stronger prompt adherence

---

## Writing Good Prompts

### For Music (MusicGen)

#### ✅ Good Prompts
```
"Upbeat electronic dance music with heavy bass and synth melodies"
"Calm acoustic guitar piece with soft piano accompaniment"
"Epic orchestral soundtrack with dramatic strings and brass"
"Lo-fi hip hop beat with vinyl crackle and mellow piano"
"Energetic rock song with electric guitar and heavy drums"
```

#### ❌ Bad Prompts
```
"Nice music" (too vague)
"Song" (not descriptive)
"Something good" (unclear)
```

#### Tips for Music
- Mention genre (electronic, rock, classical)
- Describe instruments (guitar, piano, drums)
- Add mood (upbeat, calm, epic, sad)
- Include tempo (fast, slow, moderate)
- Specify style (lo-fi, orchestral, acoustic)

### For Sounds (AudioGen)

#### ✅ Good Prompts
```
"Sound of rain falling on a window with distant thunder"
"Busy city street with cars passing and people talking"
"Forest ambience with birds chirping and leaves rustling"
"Ocean waves crashing on a beach with seagulls"
"Dog barking loudly in an outdoor park"
```

#### ❌ Bad Prompts
```
"Rain" (too simple)
"Noise" (unclear)
"Sound" (not specific)
```

#### Tips for Sounds
- Describe the main sound source
- Add environmental context
- Include background sounds
- Mention intensity (loud, soft, distant)
- Specify location (indoor, outdoor, park)

---

## Advanced Settings

### Optimizing for Quality

#### Maximum Quality Setup
```
Model: Large
Duration: 15-30s
Temperature: 1.0
CFG: 5.5
Prompt: Very detailed and specific
```

#### Fast Generation Setup
```
Model: Small
Duration: 5s
Temperature: 1.0
CFG: 3.5
Prompt: Clear and concise
```

### Generation Time Estimates

| Model | 5s Audio | 10s Audio | 30s Audio |
|-------|----------|-----------|-----------|
| Small | 8-12s | 15-20s | 45-60s |
| Medium | 15-20s | 30-40s | 90-120s |
| Large | 25-35s | 60-90s | 180-240s |

### Memory Usage

| Model | RAM Required | Disk Space |
|-------|--------------|------------|
| Small | 2GB | ~1.2GB |
| Medium | 4GB | ~6GB |
| Large | 6-8GB | ~13GB |

---

## Troubleshooting

### Backend Issues

#### "Module not found" error
```bash
cd audiocraft-lite/backend
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements-simple.txt
```

#### Port 8000 already in use
```bash
# Windows
netstat -ano | findstr :8000
taskkill /F /PID <PID>

# Mac/Linux
lsof -ti:8000 | xargs kill -9
```

#### Out of memory
- Use smaller model (Small instead of Large)
- Close other applications
- Reduce duration
- Restart backend

### Frontend Issues

#### "Cannot find module" error
```bash
cd audiocraft-lite/frontend
npm install
```

#### Port 3000 already in use
```bash
# It will ask to use another port, press Y
# Or kill the process like backend
```

### Generation Issues

#### Audio quality is poor
- Switch to larger model
- Increase CFG coefficient (5.0-6.0)
- Use longer duration (15-30s)
- Write more detailed prompts

#### Generation is too slow
- Switch to smaller model
- Reduce duration (5-8s)
- Lower CFG coefficient (3.0-3.5)

#### Audio doesn't match prompt
- Increase CFG coefficient (5.0-6.0)
- Make prompt more specific
- Try different wording
- Use longer duration

#### Audio is distorted
- Lower CFG coefficient (3.0-4.0)
- Check if using appropriate model type
- Try different prompt wording

---

## Best Practices

### Workflow Recommendations

#### 1. Prototype Phase
```
Model: Small
Duration: 5s
Goal: Test multiple prompts quickly
```

#### 2. Development Phase
```
Model: Medium
Duration: 10-15s
Goal: Refine your best prompts
```

#### 3. Production Phase
```
Model: Large
Duration: 15-30s
Goal: Generate final high-quality audio
```

### Prompt Writing Tips

1. **Start broad, then refine**
   - First: "Electronic music"
   - Better: "Upbeat electronic dance music"
   - Best: "Upbeat electronic dance music with heavy bass and synth melodies"

2. **Use reference styles**
   - "Lo-fi hip hop style"
   - "Orchestral like movie soundtracks"
   - "Acoustic folk music"

3. **Combine elements**
   - Genre + Instruments + Mood + Tempo
   - "Calm (mood) acoustic (style) guitar and piano (instruments) at slow tempo"

4. **Test variations**
   - Try different adjectives
   - Reorder descriptions
   - Add or remove details

### Performance Tips

1. **Model caching**: First generation with a model is slower (downloads + loads)
2. **Subsequent generations**: Much faster (model already loaded)
3. **Multiple models**: Can load all three, but uses more RAM
4. **Restart backend**: If memory issues occur

---

## Keyboard Shortcuts

- **Enter** in prompt field: Generate audio
- **Ctrl+C** in terminal: Stop backend/frontend

---

## API Usage (Advanced)

### Generate Audio
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Epic orchestral music",
    "duration": 10,
    "model_type": "musicgen",
    "model_size": "medium",
    "cfg_coef": 4.5
  }'
```

### List Available Models
```bash
curl http://localhost:8000/models
```

### Health Check
```bash
curl http://localhost:8000/health
```

---

## System Requirements

### Minimum
- CPU: 4 cores
- RAM: 4GB
- Disk: 10GB free
- OS: Windows 10, macOS 10.15, Ubuntu 20.04

### Recommended
- CPU: 8+ cores
- RAM: 8GB
- Disk: 20GB free (SSD preferred)
- OS: Latest version

### No GPU Required!
This system runs entirely on CPU - no expensive GPU needed!

---

## Getting Help

### Documentation
- [START_HERE.md](START_HERE.md) - Quick start
- [MODEL_SELECTION_GUIDE.md](MODEL_SELECTION_GUIDE.md) - Model details
- [QUALITY_GUIDE.md](QUALITY_GUIDE.md) - Quality optimization
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common issues

### Common Questions

**Q: Which model should I use?**
A: Start with Medium for best balance. Use Small for testing, Large for final quality.

**Q: How long does generation take?**
A: Medium model takes ~30-40s for 10s audio on average CPU.

**Q: Can I use GPU?**
A: Yes, but this version is optimized for CPU. GPU support can be added.

**Q: Why is first generation slow?**
A: Model needs to download first time (~1-13GB depending on size).

**Q: Can I generate longer audio?**
A: Maximum is 30s per generation. Generate multiple clips and combine them.

**Q: Is this free?**
A: Yes! MIT licensed, completely free and open source.

---

## Tips for Best Results

1. ✅ Use descriptive, detailed prompts
2. ✅ Start with Small model for testing
3. ✅ Use Medium model for production
4. ✅ Switch to Large for final quality
5. ✅ Experiment with CFG coefficient
6. ✅ Try different prompt variations
7. ✅ Use appropriate duration for content
8. ✅ Match model type to content (Music vs Sound)

---

**Happy generating!** 🎵🎶🔊
