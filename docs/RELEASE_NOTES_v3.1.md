# 🎉 AudioCraft Lite v3.1 - Release Notes

## 🆕 What's New

### On-Demand Model Downloads (Major Feature!)

**No more waiting for all models to download!**

Users can now choose which AI models to download based on their needs:
- ✅ **Faster first run** - Start using in 5-15 minutes instead of 30-45 minutes
- ✅ **Save disk space** - Download only what you need (2-6GB instead of 12GB)
- ✅ **More control** - Manage models through the UI
- ✅ **Better experience** - See download status and manage loaded models

### Model Manager UI

New collapsible "Model Manager" section in the app:
- 📊 **View model status** - See which models are downloaded/loaded
- ⬇️ **Download models** - One-click download for each model
- 🔄 **Load/Unload** - Manage which models are in memory
- 📦 **Model info** - See size, quality, and speed for each model

### Three Model Options

| Model | Size | Quality | Speed | Best For |
|-------|------|---------|-------|----------|
| **Small** | ~2GB | 60-70% | Fast | Quick tests, previews |
| **Medium** | ~4GB | 75-85% | Medium | Most use cases ✓ |
| **Large** | ~6GB | 90-95% | Slow | Final production |

---

## 🔧 Technical Changes

### Backend
- Added `get_downloaded_models()` method to check cached models
- Added `get_model_status()` to get detailed model information
- Added `download_model()` for on-demand downloading
- Added `unload_model()` to free memory
- New API endpoints: `/models/status`, `/models/download/{size}`, `/models/load/{size}`, `/models/unload/{size}`

### Frontend
- New Model Manager component with collapsible UI
- Real-time model status display
- Download progress indicators
- Load/Unload buttons for memory management
- Status badges (Downloaded/Loaded/Not Downloaded)

### Documentation
- New [Model Download Guide](docs/user-guides/MODEL_DOWNLOAD_GUIDE.md) for users
- New [On-Demand Models](docs/developer/ON_DEMAND_MODELS.md) for developers
- Updated README with new feature information

---

## 📊 Comparison: v3.0 vs v3.1

### First Run Experience

**v3.0 (Old):**
- ❌ Downloads all 3 models automatically
- ❌ Takes 30-45 minutes
- ❌ Uses 12GB disk space
- ❌ No choice in what to download

**v3.1 (New):**
- ✅ Download only what you need
- ✅ Takes 5-15 minutes (one model)
- ✅ Uses 2-6GB disk space (one model)
- ✅ Full control through UI

### User Experience

**v3.0:**
- Models downloaded in background
- No visibility into download status
- All models loaded automatically

**v3.1:**
- Model Manager UI for full control
- See download progress and status
- Choose which models to load
- Manage memory usage

---

## 🚀 How to Use

### For New Users

1. **Launch the app** - Double-click `AudioCraft-Lite.bat`
2. **Open Model Manager** - Click "Model Manager" at the top
3. **Download a model** - Start with Medium (recommended)
4. **Wait for download** - 5-15 minutes depending on internet
5. **Start creating!** - Generate your first audio

### For Existing Users

- **Existing models detected automatically** - No need to re-download
- **Model Manager shows status** - See which models you have
- **Everything works as before** - Backward compatible

---

## 💡 Recommended Workflow

### Beginners
1. Download **Medium model** only (~4GB)
2. Learn the interface
3. Generate some audio
4. Download other models if needed

### Content Creators
1. Download **Small** for quick tests (~2GB)
2. Download **Medium** for most work (~4GB)
3. Download **Large** for final production (~6GB)

### Limited Disk Space
1. Download **Small model** only (~2GB)
2. Still produces good quality
3. Fastest generation times

---

## 🔄 Migration Guide

### If You Already Have v3.0

**Good News:** No migration needed!

- Existing models are automatically detected
- Model Manager shows "Downloaded" status
- Everything works exactly as before
- New features are optional

### If Starting Fresh

- No models downloaded initially
- Choose and download what you need
- Faster first-time experience
- More control over disk usage

---

## 📦 Package Information

### Distribution Package
- **Size (zipped)**: ~50-100MB
- **Size (extracted)**: ~100-200MB
- **With models**: ~2-12GB (user's choice)

### System Requirements
- **OS**: Windows 10/11
- **Python**: 3.10 or 3.11
- **RAM**: 4-8GB
- **Disk**: 2-12GB (depending on models)
- **Internet**: Required for first run

---

## 🐛 Bug Fixes

- Fixed model loading on first run
- Improved error handling for downloads
- Better memory management
- Fixed cache detection issues

---

## 🎯 Performance Improvements

### Download Times
- **Small**: ~5-10 minutes (2GB)
- **Medium**: ~10-15 minutes (4GB)
- **Large**: ~15-20 minutes (6GB)

### Load Times
- **Small**: ~10-15 seconds
- **Medium**: ~20-30 seconds
- **Large**: ~40-60 seconds

### Generation Times (10s audio)
- **Small**: ~15-20 seconds
- **Medium**: ~30-40 seconds
- **Large**: ~60-90 seconds

---

## 📚 New Documentation

### User Guides
- **[Model Download Guide](docs/user-guides/MODEL_DOWNLOAD_GUIDE.md)** - Complete guide to on-demand downloads
  - How to download models
  - Which model to choose
  - Troubleshooting downloads
  - Disk space management

### Developer Guides
- **[On-Demand Models](docs/developer/ON_DEMAND_MODELS.md)** - Technical implementation
  - API reference
  - Code examples
  - Architecture diagram
  - Testing guide

---

## 🔮 Future Plans

### Planned Features
- Download progress bars with percentage
- Background model preloading
- Model switching without reload
- Disk space monitoring
- Download queue system
- Support for melody models
- Support for stereo models

---

## 🆘 Support

### Documentation
- [User Guide](docs/user-guides/README_FOR_USERS.md)
- [Model Download Guide](docs/user-guides/MODEL_DOWNLOAD_GUIDE.md)
- [Troubleshooting](docs/user-guides/TROUBLESHOOTING.md)
- [Developer Guide](docs/developer/COMPLETE_GUIDE.md)

### Common Issues
- **Download fails**: Check internet connection and disk space
- **Model won't load**: Ensure model is downloaded first
- **Out of memory**: Use smaller model or close other apps
- **Slow download**: Check internet speed, be patient

---

## 📜 Credits

### Powered By
- **Meta's AudioCraft** - AI models (MusicGen & AudioGen)
- **MIT License** - Free and open source
- **GitHub**: https://github.com/facebookresearch/audiocraft

### Presented By
- **AI Music Studio .pro** - User interface and packaging
- **Community** - Feedback and testing

---

## 📝 License

MIT License - Free to use, modify, and distribute

**Attribution Required**: Credit Meta AudioCraft and AI Music Studio .pro

---

## 🎉 Thank You!

Thank you for using AudioCraft Lite!

This release brings significant improvements to the user experience with on-demand model downloads. We hope you enjoy the faster startup and better control over your models.

**Happy Creating!** 🎵🎶

---

**Version**: 3.1  
**Release Date**: February 2, 2026  
**Platform**: Windows 10/11  
**License**: MIT  

---

## Quick Links

- [Download Guide](docs/user-guides/MODEL_DOWNLOAD_GUIDE.md)
- [User Guide](docs/user-guides/README_FOR_USERS.md)
- [Developer Guide](docs/developer/ON_DEMAND_MODELS.md)
- [Troubleshooting](docs/user-guides/TROUBLESHOOTING.md)
- [GitHub - Meta AudioCraft](https://github.com/facebookresearch/audiocraft)
