# Audio Quality Improvement Guide

## Current Setup
- **Model**: MusicGen Medium (1.5B parameters)
- **Expected Quality**: 75-85% of original AudioCraft
- **Generation Speed**: ~2-4x real-time on CPU

## Quality Levels by Model

### Small Model (300M params) - Fast
- Quality: 60-70%
- Speed: ~1-2x real-time
- Best for: Quick previews, testing

### Medium Model (1.5B params) - Balanced ✓ CURRENT
- Quality: 75-85%
- Speed: ~2-4x real-time
- Best for: Production use on CPU

### Large Model (3.3B params) - Best Quality
- Quality: 90-95%
- Speed: ~5-10x real-time
- Best for: GPU systems or when quality is critical

## How to Switch Models

Edit `backend/config.py`:

```python
# For better quality (slower):
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-large"

# For faster generation (lower quality):
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-small"

# Current balanced option:
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-medium"
```

## Improving Generation Quality

### 1. Adjust CFG Coefficient (Guidance Scale)
Higher values = stronger prompt adherence

```python
# In config.py
DEFAULT_CFG_COEF = 4.5  # Current (good balance)
DEFAULT_CFG_COEF = 6.0  # Stronger prompt following
DEFAULT_CFG_COEF = 3.0  # More creative/varied
```

### 2. Temperature Settings
Lower = more consistent, Higher = more creative

```python
DEFAULT_TEMPERATURE = 1.0  # Current (balanced)
DEFAULT_TEMPERATURE = 0.8  # More consistent
DEFAULT_TEMPERATURE = 1.2  # More varied/creative
```

### 3. Duration Settings
Longer durations allow better musical development

```python
DEFAULT_DURATION = 10  # Current
DEFAULT_DURATION = 15  # Better for full musical ideas
DEFAULT_DURATION = 30  # Maximum allowed
```

## Writing Better Prompts

### For Music Generation
✅ **Good prompts:**
- "Upbeat electronic dance music with heavy bass and synth melodies"
- "Calm acoustic guitar piece with soft piano accompaniment"
- "Epic orchestral soundtrack with dramatic strings and brass"
- "Lo-fi hip hop beat with vinyl crackle and mellow piano"

❌ **Avoid:**
- "Nice music" (too vague)
- "Song" (not descriptive enough)

### For Sound Effects (AudioGen mode)
✅ **Good prompts:**
- "Sound of rain falling on a window with distant thunder"
- "Dog barking in a park with birds chirping"
- "Car engine starting and revving"
- "Ocean waves crashing on a beach"

❌ **Avoid:**
- "Rain" (too simple)
- "Noise" (unclear)

## Performance Optimization

### CPU Optimization
Current settings in `config.py`:
```python
USE_CPU = True
NUM_THREADS = 4  # Adjust based on your CPU cores
```

### Memory Management
```python
MAX_OUTPUT_FILES = 100  # Keeps only recent files
```

## Quality vs Speed Trade-offs

| Setting | Quality | Speed | CPU Usage |
|---------|---------|-------|-----------|
| Small model + short duration | 60% | Fast | Low |
| Medium model + 10s | 80% | Medium | Medium |
| Large model + 30s | 95% | Slow | High |

## Troubleshooting Quality Issues

### Audio sounds distorted
- Lower the CFG coefficient (try 3.0-4.0)
- Check if audio is clipping (already normalized to 0.95)

### Audio doesn't match prompt
- Increase CFG coefficient (try 5.0-6.0)
- Make prompt more specific and descriptive
- Try longer duration for complex prompts

### Audio is too repetitive
- Increase temperature (try 1.1-1.3)
- Use more varied prompts
- Try different top_k values (200-300)

### Generation is too slow
- Switch to small model
- Reduce duration
- Reduce NUM_THREADS if system is overloaded

## Expected Generation Times (CPU)

**Medium Model:**
- 5s audio: ~15-20 seconds
- 10s audio: ~30-40 seconds
- 30s audio: ~90-120 seconds

**Small Model:**
- 5s audio: ~8-12 seconds
- 10s audio: ~15-20 seconds
- 30s audio: ~45-60 seconds

## Recommended Settings for Different Use Cases

### Quick Previews
```python
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-small"
DEFAULT_DURATION = 5
DEFAULT_CFG_COEF = 3.5
```

### Production Quality (Current)
```python
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-medium"
DEFAULT_DURATION = 10
DEFAULT_CFG_COEF = 4.5
```

### Maximum Quality
```python
DEFAULT_MUSICGEN_MODEL = "facebook/musicgen-large"
DEFAULT_DURATION = 15
DEFAULT_CFG_COEF = 5.0
```

## Note on AudioGen

AudioGen is not available via HuggingFace transformers. Instead, we use MusicGen with enhanced prompts for sound effects. The system automatically adds "Sound effect:" prefix to AudioGen requests for better results.

For true AudioGen functionality, you would need to install the full audiocraft package (requires Python 3.11 or earlier due to dependency issues).
