# Model Selection Guide

## How to Select Models

You can now choose between **Small**, **Medium**, and **Large** models directly from the frontend!

## Model Options

### ⚡ Small (Fast)
- **Quality**: 60-70%
- **Speed**: Fast (~10-20 seconds for 10s audio)
- **Memory**: ~2GB RAM
- **Best for**: Quick previews, testing prompts, rapid iteration

### ⚖️ Medium (Balanced) - DEFAULT
- **Quality**: 75-85%
- **Speed**: Medium (~30-40 seconds for 10s audio)
- **Memory**: ~4GB RAM
- **Best for**: Production use, good balance of quality and speed

### 🎯 Large (Best Quality)
- **Quality**: 90-95%
- **Speed**: Slow (~60-90 seconds for 10s audio)
- **Memory**: ~6-8GB RAM
- **Best for**: Final production, when quality is critical

## How to Use

### From Frontend (Recommended)
1. Start the backend: `python main.py`
2. Start the frontend: `npm start`
3. Open http://localhost:3000
4. **Select model quality** using the buttons:
   - ⚡ Small (Fast)
   - ⚖️ Medium (Balanced)
   - 🎯 Large (Best)
5. Choose model type (MusicGen or AudioGen)
6. Enter your prompt and generate!

### From API
Send POST request to `/generate` with:
```json
{
  "prompt": "Epic orchestral music",
  "duration": 10,
  "model_type": "musicgen",
  "model_size": "medium"
}
```

**model_size options**: `"small"`, `"medium"`, `"large"`

## Model Caching

The system caches loaded models, so:
- First generation with a model: Slower (downloads + loads model)
- Subsequent generations: Faster (model already loaded)
- You can switch between models without restarting
- Multiple models can be loaded simultaneously (uses more RAM)

## Recommendations by Use Case

### Quick Testing
```
Model: Small
Duration: 5s
CFG: 3.5
```

### Content Creation
```
Model: Medium
Duration: 10-15s
CFG: 4.5
```

### Professional Production
```
Model: Large
Duration: 15-30s
CFG: 5.5
```

## Performance Comparison

| Model | 5s Audio | 10s Audio | 30s Audio | RAM Usage |
|-------|----------|-----------|-----------|-----------|
| Small | ~8-12s | ~15-20s | ~45-60s | ~2GB |
| Medium | ~15-20s | ~30-40s | ~90-120s | ~4GB |
| Large | ~25-35s | ~60-90s | ~180-240s | ~6-8GB |

## Tips

1. **Start with Small** to test your prompt
2. **Use Medium** for most production work
3. **Switch to Large** only when you need the best quality
4. **Longer durations** allow better musical development
5. **Higher CFG** (4.5-6.0) = stronger prompt adherence

## Troubleshooting

### Model download is slow
- First time only, models are cached after download
- Small: ~1.2GB, Medium: ~6GB, Large: ~13GB

### Out of memory error
- Use smaller model
- Close other applications
- Reduce duration
- Restart backend

### Generation is too slow
- Use Small model
- Reduce duration to 5-8s
- Lower CFG to 3.0-3.5

## Example Workflow

1. **Prototype** with Small model (fast iterations)
2. **Refine** with Medium model (good quality)
3. **Finalize** with Large model (best quality)

This approach saves time while ensuring quality!
