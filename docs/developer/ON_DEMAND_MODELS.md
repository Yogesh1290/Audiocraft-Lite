# 🔧 On-Demand Model Download - Developer Guide

## Overview

Implemented on-demand model downloading to improve user experience and reduce initial setup time.

---

## Changes Made

### Backend Changes

#### 1. `model_manager.py`
**New Methods:**
- `get_downloaded_models()` - Check which models are in cache
- `get_model_status()` - Get status of all models (downloaded/loaded)
- `download_model(size)` - Download model without loading into memory
- `unload_model(size)` - Unload specific model from memory

**Modified Methods:**
- `load_model()` - Now downloads if not cached (backward compatible)

#### 2. `main.py`
**New Endpoints:**
- `GET /models/status` - Get detailed status of all models
- `POST /models/download/{model_size}` - Download specific model
- `POST /models/load/{model_size}` - Load model into memory
- `POST /models/unload/{model_size}` - Unload model from memory

**Modified Endpoints:**
- `GET /models` - Now includes model status

#### 3. `config.py`
**Added:**
- `size_gb` field to `AVAILABLE_MODELS` dictionary

### Frontend Changes

#### 1. `App.js`
**New State:**
```javascript
const [showModelManager, setShowModelManager] = useState(false);
const [modelStatus, setModelStatus] = useState({});
const [downloadingModel, setDownloadingModel] = useState(null);
const [loadingModel, setLoadingModel] = useState(null);
```

**New Functions:**
- `fetchModelStatus()` - Fetch model status from API
- `handleDownloadModel(size)` - Download specific model
- `handleLoadModel(size)` - Load model into memory
- `handleUnloadModel(size)` - Unload model from memory

**New Component:**
- Model Manager collapsible section with model cards

#### 2. `App.css`
**New Styles:**
- `.model-manager-card` - Container for model manager
- `.model-card` - Individual model card
- `.status-badge` - Status indicators (downloaded/loaded/not-downloaded)
- `.model-action-btn` - Action buttons (download/load/unload)

---

## API Reference

### Get Model Status
```http
GET /models/status
```

**Response:**
```json
{
  "small": {
    "name": "Small (Fast)",
    "params": "300M",
    "quality": "60-70%",
    "speed": "Fast",
    "description": "Fastest generation...",
    "downloaded": true,
    "loaded": false,
    "size_gb": "~2GB"
  },
  "medium": { ... },
  "large": { ... }
}
```

### Download Model
```http
POST /models/download/{model_size}
```

**Parameters:**
- `model_size`: "small" | "medium" | "large"

**Response:**
```json
{
  "success": true,
  "model_size": "medium",
  "download_time": 123.45,
  "message": "Model medium downloaded successfully"
}
```

### Load Model
```http
POST /models/load/{model_size}
```

**Response:**
```json
{
  "success": true,
  "model_size": "medium",
  "message": "Model medium loaded successfully"
}
```

### Unload Model
```http
POST /models/unload/{model_size}
```

**Response:**
```json
{
  "success": true,
  "model_size": "medium",
  "message": "Model medium unloaded successfully"
}
```

---

## Implementation Details

### Model Detection

Models are detected by checking the HuggingFace cache structure:
```
~/.cache/audiocraft-lite/
└── models/
    └── models--facebook--musicgen-{size}/
        └── snapshots/
            └── {hash}/
                ├── config.json
                ├── pytorch_model.bin
                └── ...
```

### Download Process

1. User clicks "Download" button
2. Frontend calls `POST /models/download/{size}`
3. Backend downloads using HuggingFace `from_pretrained()`
4. Model is cached automatically
5. Frontend refreshes status

### Load Process

1. User clicks "Load into Memory" button
2. Frontend calls `POST /models/load/{size}`
3. Backend loads model into RAM
4. Model is ready for generation
5. Frontend shows "Loaded" badge

### Generation Process

1. User selects quality level (model size)
2. User generates audio
3. Backend checks if model is loaded
4. If not loaded, loads automatically (downloads if needed)
5. Generates audio
6. Returns result

---

## Backward Compatibility

### Existing Behavior Preserved
- Models are still auto-downloaded on first use
- No breaking changes to generation API
- Existing cached models are detected automatically

### New Behavior Added
- Users can pre-download models
- Users can manage loaded models
- Better visibility into model status

---

## Performance Considerations

### Download Times
- Small: ~5-10 minutes (2GB)
- Medium: ~10-15 minutes (4GB)
- Large: ~15-20 minutes (6GB)

*Times vary based on internet speed*

### Load Times
- Small: ~10-15 seconds
- Medium: ~20-30 seconds
- Large: ~40-60 seconds

### Memory Usage
- Small: ~2GB RAM
- Medium: ~4GB RAM
- Large: ~6GB RAM

### Disk Usage
- Small: ~2GB
- Medium: ~4GB
- Large: ~6GB
- Total (all): ~12GB

---

## Testing

### Manual Testing

1. **Test Model Detection:**
```bash
curl http://localhost:8000/models/status
```

2. **Test Model Download:**
```bash
curl -X POST http://localhost:8000/models/download/small
```

3. **Test Model Load:**
```bash
curl -X POST http://localhost:8000/models/load/small
```

4. **Test Model Unload:**
```bash
curl -X POST http://localhost:8000/models/unload/small
```

5. **Test Generation:**
```bash
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{"prompt": "test", "duration": 5, "model_size": "small"}'
```

### UI Testing

1. Open Model Manager
2. Verify status badges are correct
3. Download a model
4. Verify download progress
5. Load the model
6. Verify "Loaded" badge appears
7. Generate audio with that model
8. Unload the model
9. Verify badge changes

---

## Future Enhancements

### Possible Improvements

1. **Progress Bars**
   - Show download progress percentage
   - Show loading progress

2. **Model Preloading**
   - Preload models in background
   - Smart caching based on usage

3. **Model Switching**
   - Quick switch between loaded models
   - Keep multiple models in memory

4. **Disk Space Monitoring**
   - Show available disk space
   - Warn before downloading large models

5. **Download Queue**
   - Queue multiple downloads
   - Download in background

6. **Model Variants**
   - Support melody models
   - Support stereo models
   - Support different sample rates

---

## Troubleshooting

### Common Issues

**Issue**: Model status shows "Not Downloaded" but model exists in cache

**Solution**: Check cache path structure. Ensure `snapshots/` directory exists and contains files.

**Issue**: Download fails with timeout

**Solution**: Increase timeout in axios config or retry download.

**Issue**: Model loads but generation fails

**Solution**: Check model files are complete. Re-download if corrupted.

**Issue**: Out of memory when loading large model

**Solution**: Unload other models first. Close other applications.

---

## Code Examples

### Check if Model is Downloaded
```python
downloaded_models = model_manager.get_downloaded_models()
if "medium" in downloaded_models:
    print("Medium model is downloaded")
```

### Download Model Programmatically
```python
result = model_manager.download_model("medium")
if result["success"]:
    print(f"Downloaded in {result['download_time']:.2f}s")
```

### Load Model with Error Handling
```python
try:
    model_manager.load_model("large")
    print("Model loaded successfully")
except Exception as e:
    print(f"Failed to load model: {e}")
```

### Get Model Status
```python
status = model_manager.get_model_status()
for size, info in status.items():
    print(f"{size}: Downloaded={info['downloaded']}, Loaded={info['loaded']}")
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                      Frontend (React)                    │
│  ┌──────────────────────────────────────────────────┐  │
│  │           Model Manager Component                 │  │
│  │  - Show model status                              │  │
│  │  - Download buttons                               │  │
│  │  - Load/Unload buttons                            │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ HTTP API
                           ▼
┌─────────────────────────────────────────────────────────┐
│                   Backend (FastAPI)                      │
│  ┌──────────────────────────────────────────────────┐  │
│  │              API Endpoints                        │  │
│  │  - GET /models/status                             │  │
│  │  - POST /models/download/{size}                   │  │
│  │  - POST /models/load/{size}                       │  │
│  │  - POST /models/unload/{size}                     │  │
│  └──────────────────────────────────────────────────┘  │
│                           │                              │
│                           ▼                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │           ModelManager Class                      │  │
│  │  - get_downloaded_models()                        │  │
│  │  - get_model_status()                             │  │
│  │  - download_model(size)                           │  │
│  │  - load_model(size)                               │  │
│  │  - unload_model(size)                             │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
                           │
                           │ HuggingFace API
                           ▼
┌─────────────────────────────────────────────────────────┐
│              HuggingFace Model Hub                       │
│  - facebook/musicgen-small                               │
│  - facebook/musicgen-medium                              │
│  - facebook/musicgen-large                               │
└─────────────────────────────────────────────────────────┘
                           │
                           │ Download & Cache
                           ▼
┌─────────────────────────────────────────────────────────┐
│              Local Cache Directory                       │
│  ~/.cache/audiocraft-lite/models/                        │
└─────────────────────────────────────────────────────────┘
```

---

## Summary

The on-demand model download feature provides:
- ✅ Better user experience (faster startup)
- ✅ Reduced disk usage (download only what's needed)
- ✅ More control (manage models explicitly)
- ✅ Backward compatible (existing behavior preserved)
- ✅ Well documented (user and developer guides)

---

**Questions?** Check the [User Guide](../user-guides/MODEL_DOWNLOAD_GUIDE.md) or [Troubleshooting](../user-guides/TROUBLESHOOTING.md)
