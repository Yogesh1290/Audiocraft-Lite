# 📦 On-Demand Model Download Guide

## What's New?

AudioCraft Lite now supports **on-demand model downloading**! Instead of downloading all models at once, you can choose which models to download based on your needs.

---

## 🎯 Benefits

### Save Time
- **First run is faster** - No need to wait for all models to download
- **Start using immediately** - Download only the model you need right now

### Save Disk Space
- **Small model only**: ~2GB
- **Medium model only**: ~4GB  
- **Large model only**: ~6GB
- **All models**: ~12GB

### Flexible Usage
- Download models as you need them
- Try different quality levels
- Unload models to free RAM

---

## 🚀 How It Works

### Step 1: Open Model Manager
1. Launch AudioCraft Lite
2. Click **"Model Manager"** at the top
3. See all available models and their status

### Step 2: Download a Model
1. Choose a model based on your needs:
   - **Fast (Small)**: Quick tests, 60-70% quality, ~2GB
   - **Balanced (Medium)**: Normal use, 75-85% quality, ~4GB ✓ Recommended
   - **Premium (Large)**: Best quality, 90-95% quality, ~6GB

2. Click **"Download"** button
3. Wait 5-15 minutes (depends on internet speed)
4. Model is now ready to use!

### Step 3: Use the Model
1. Select the quality level in the main interface
2. Enter your prompt
3. Generate audio!

---

## 📊 Model Comparison

| Model | Size | Quality | Speed | Best For |
|-------|------|---------|-------|----------|
| **Small** | ~2GB | 60-70% | Fast | Quick previews, testing prompts |
| **Medium** | ~4GB | 75-85% | Medium | Most use cases, balanced quality |
| **Large** | ~6GB | 90-95% | Slow | Final production, highest quality |

---

## 💡 Usage Tips

### For Beginners
- **Start with Medium model** - Best balance of quality and speed
- Download only one model initially
- Try it out before downloading others

### For Power Users
- **Download all models** - Switch between them as needed
- Use Small for quick tests
- Use Large for final production

### For Limited Disk Space
- **Download Small model only** - Still produces good results
- Delete models you don't use (from cache folder)

---

## 🔧 Model Management

### Check Model Status
- **Not Downloaded** (Gray badge) - Model needs to be downloaded
- **Downloaded** (Blue badge) - Model is cached, ready to load
- **Loaded** (Green badge) - Model is in memory, ready to use

### Load/Unload Models
- **Load**: Loads model into RAM for faster generation
- **Unload**: Frees RAM when not using the model
- Models stay downloaded even when unloaded

### Re-downloading
- Models are cached permanently
- No need to re-download unless you delete cache
- Cache location: `~/.cache/audiocraft-lite/`

---

## ⚡ Performance Tips

### First-Time Download
- **Time**: 5-15 minutes per model
- **Internet**: Requires stable connection
- **Disk**: Ensure enough free space

### Loading Models
- **Small**: ~10-15 seconds
- **Medium**: ~20-30 seconds
- **Large**: ~40-60 seconds

### Generation Speed
- **Small**: ~15-20 seconds for 10s audio
- **Medium**: ~30-40 seconds for 10s audio
- **Large**: ~60-90 seconds for 10s audio

---

## 🆘 Troubleshooting

### Download Failed
**Problem**: Model download interrupted or failed

**Solutions**:
1. Check internet connection
2. Check disk space (need 2-6GB free)
3. Try again - downloads resume automatically
4. Check firewall/antivirus settings

### Model Won't Load
**Problem**: "Failed to load model" error

**Solutions**:
1. Ensure model is downloaded first
2. Check RAM availability (need 4-8GB free)
3. Close other applications
4. Try restarting the app

### Out of Memory
**Problem**: "Out of memory" error during generation

**Solutions**:
1. Use a smaller model (Small instead of Large)
2. Close other applications
3. Unload unused models
4. Reduce generation duration

### Slow Download
**Problem**: Download taking too long

**Solutions**:
1. Check internet speed (need 10+ Mbps)
2. Pause other downloads
3. Try during off-peak hours
4. Be patient - large files take time

---

## 📁 File Locations

### Model Cache
```
Windows: C:\Users\YourName\.cache\audiocraft-lite\
```

### Cache Structure
```
.cache/audiocraft-lite/
├── models/
│   ├── models--facebook--musicgen-small/
│   ├── models--facebook--musicgen-medium/
│   └── models--facebook--musicgen-large/
```

### Clearing Cache
To free disk space, you can delete models you don't use:
1. Close AudioCraft Lite
2. Navigate to cache folder
3. Delete specific model folders
4. Models will need to be re-downloaded

---

## 🎓 Best Practices

### Recommended Workflow

**For Beginners:**
1. Download Medium model only
2. Learn the interface
3. Generate some audio
4. Download other models if needed

**For Content Creators:**
1. Download Small for quick tests
2. Download Medium for most work
3. Download Large for final production

**For Developers:**
1. Download all models
2. Test quality differences
3. Choose based on use case

### Disk Space Management
- Keep only models you actively use
- Delete unused models from cache
- Medium model is usually sufficient

### RAM Management
- Unload models when not in use
- Only keep one model loaded at a time
- Close other applications during generation

---

## 📊 Comparison: Old vs New

### Old Behavior (Before)
- ❌ All models downloaded on first run
- ❌ Takes 30-45 minutes initially
- ❌ Uses ~12GB disk space
- ❌ No choice in what to download

### New Behavior (Now)
- ✅ Download only what you need
- ✅ Start using in 5-15 minutes
- ✅ Use as little as 2GB disk space
- ✅ Full control over models

---

## 🔄 Migration Guide

### If You Already Have Models
- Existing models are automatically detected
- No need to re-download
- Model Manager shows "Downloaded" status
- Everything works as before

### If Starting Fresh
- No models downloaded initially
- Choose and download what you need
- Faster first-time experience

---

## ❓ FAQ

### Q: Do I need to download all models?
**A:** No! Download only what you need. Medium model is recommended for most users.

### Q: Can I delete models later?
**A:** Yes, delete from cache folder. You can re-download anytime.

### Q: Will models be deleted when I close the app?
**A:** No, models stay cached permanently until you manually delete them.

### Q: Can I use the app without downloading any models?
**A:** No, you need at least one model downloaded to generate audio.

### Q: Which model should I download first?
**A:** Medium model - best balance of quality and speed for most users.

### Q: How much internet data will this use?
**A:** Small: ~2GB, Medium: ~4GB, Large: ~6GB download size.

### Q: Can I download models on mobile hotspot?
**A:** Yes, but be aware of data usage (2-6GB per model).

### Q: Do models update automatically?
**A:** No, models are cached permanently. Updates require manual re-download.

---

## 🎉 Summary

The new on-demand model download feature gives you:
- **Faster startup** - No waiting for all models
- **Less disk space** - Download only what you need
- **More control** - Choose your quality level
- **Better experience** - Start using immediately

**Recommended**: Download Medium model first, then add others as needed!

---

**Need Help?** Check the [Troubleshooting Guide](TROUBLESHOOTING.md) or [User Guide](README_FOR_USERS.md)

**Happy Creating!** 🎵🎶
