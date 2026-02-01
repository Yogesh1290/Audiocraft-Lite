# 🚀 AudioCraft Lite - Standalone Executable Guide

## Overview

Yes! You can create a **single-click Windows executable** that requires:
- ❌ No VS Code
- ❌ No Python installation
- ❌ No terminal commands
- ❌ No setup
- ✅ Just double-click and go!

## How It Works

The standalone executable bundles:
1. **Python runtime** - No Python installation needed
2. **Backend server** - FastAPI with all dependencies
3. **Frontend UI** - React app (pre-built)
4. **All libraries** - PyTorch, transformers, etc.

When you double-click the .exe:
1. Starts the backend server
2. Opens your browser automatically
3. You're ready to generate audio!

## Building the Executable

### Quick Start

**Option 1: Double-click** (Easiest)
```
BUILD.bat
```

**Option 2: Command line**
```bash
python build_exe.py
```

### What You Need

Before building:
- ✅ Python 3.10 or 3.11
- ✅ Node.js (for React build)
- ✅ All dependencies installed

### Build Process

The script automatically:
1. ✅ Builds React frontend (`npm run build`)
2. ✅ Installs PyInstaller
3. ✅ Creates PyInstaller spec file
4. ✅ Bundles everything into .exe
5. ✅ Creates distribution folder

### Build Output

```
dist/AudioCraft-Lite/
├── AudioCraft-Lite.exe  ← The main executable
├── _internal/           ← Bundled dependencies
│   ├── backend/
│   ├── frontend/build/
│   └── [Python runtime & libraries]
└── [other files]
```

## Using the Executable

### For End Users

1. **Extract** the zip file
2. **Open** the `AudioCraft-Lite` folder
3. **Double-click** `AudioCraft-Lite.exe`
4. **Wait** for browser to open
5. **Start generating** audio!

### What Happens

```
[User double-clicks .exe]
         ↓
[Console window opens]
         ↓
[Backend server starts]
         ↓
[Browser opens automatically]
         ↓
[User generates audio]
```

## Distribution

### Sharing with Others

1. **Zip the folder**:
   ```
   dist/AudioCraft-Lite/ → AudioCraft-Lite.zip
   ```

2. **Upload** to file sharing service

3. **Users download** and extract

4. **Users double-click** the .exe

### What Users Need

- Windows 10/11
- 4-8GB RAM
- 10-20GB disk space
- Internet (first run only)

## File Size

- **Executable**: ~500MB-1GB
- **With models**: ~7-20GB (downloaded on first run)
- **Compressed zip**: ~300-500MB

## Advantages

### For Users
- ✅ **No installation** required
- ✅ **No Python** needed
- ✅ **No setup** hassle
- ✅ **Single click** to run
- ✅ **Portable** - run from USB drive
- ✅ **Offline** - works without internet (after first run)

### For Developers
- ✅ **Easy distribution** - just share a zip
- ✅ **No support** for installation issues
- ✅ **Consistent** - same environment for everyone
- ✅ **Professional** - looks like a real app

## Limitations

### Technical
- ⚠️ **Large file size** (~500MB-1GB)
- ⚠️ **Windows only** (can build for Mac/Linux separately)
- ⚠️ **Slower startup** (~5-10 seconds)
- ⚠️ **Antivirus warnings** (false positives)

### Functional
- ✅ **Same features** as running from source
- ✅ **Same performance** - no overhead
- ✅ **Same quality** - identical output

## Advanced Options

### Custom Icon

Add your own icon:
1. Create `icon.ico` file
2. Place in root directory
3. Rebuild

### Code Signing

To avoid antivirus warnings:
1. Get code signing certificate
2. Sign the executable
3. Costs money but improves trust

### Installer

Create a proper installer:
- Use Inno Setup or NSIS
- Install to Program Files
- Create shortcuts
- Add to Start Menu

## Comparison

### Running from Source
```
Pros:
- Smaller download
- Easy to update
- Easy to modify

Cons:
- Requires Python
- Requires dependencies
- Requires terminal
- Technical knowledge needed
```

### Standalone Executable
```
Pros:
- No installation
- No Python needed
- Single click
- Professional

Cons:
- Large file size
- Harder to update
- Harder to modify
- Antivirus warnings
```

## Best Practices

### For Building
1. ✅ Test on clean machine
2. ✅ Verify all features work
3. ✅ Check file paths
4. ✅ Test model downloads
5. ✅ Document requirements

### For Distribution
1. ✅ Include USER_GUIDE_EXE.md
2. ✅ Mention system requirements
3. ✅ Warn about first-run delay
4. ✅ Provide support contact
5. ✅ Include license info

## Troubleshooting

### Build Issues

**"npm not found"**
- Install Node.js

**"PyInstaller failed"**
- Check Python version (3.10-3.11)
- Install dependencies

**"Frontend build failed"**
- Run `npm install` in frontend
- Run `npm run build`

### Runtime Issues

**"Port 8000 in use"**
- Close other instances
- Change port in config

**"Models won't download"**
- Check internet
- Check disk space
- Check firewall

**"Antivirus blocked"**
- Add exception
- This is a false positive

## Performance

### Startup Time
- First run: 30-60s (model download)
- Subsequent: 5-10s

### Generation Time
- Same as running from source
- No performance penalty

### Memory Usage
- 2-8GB depending on model
- Same as running from source

## Security

### Is it Safe?
- ✅ Open source code
- ✅ No telemetry
- ✅ Runs locally
- ✅ No data sent to cloud

### Antivirus Warnings
- Common with PyInstaller
- False positive
- Code is open source
- Can be verified

## Updates

### Updating the App

For developers:
1. Update code
2. Rebuild executable
3. Redistribute

For users:
1. Download new version
2. Extract to new folder
3. Models are reused

## Commercial Use

### Can I Sell This?
- ✅ Yes (MIT License)
- ✅ Attribution required
- ✅ Include license
- ✅ Credit Meta AudioCraft

### Can I Distribute?
- ✅ Yes, freely
- ✅ Keep attribution
- ✅ Include licenses
- ✅ Don't claim as yours

## Future Improvements

Possible enhancements:
- 🔄 Auto-updater
- 🎨 Custom themes
- 📦 Smaller file size
- 🔐 Code signing
- 📱 Mobile version
- 🌐 Multi-language

## Files Created

For standalone executable:
```
audiocraft-lite/
├── launcher.py              # Main launcher
├── build_exe.py            # Build script
├── BUILD.bat               # Windows batch
├── audiocraft-lite.spec    # PyInstaller config
├── BUILD_INSTRUCTIONS.md   # Build guide
├── USER_GUIDE_EXE.md      # User guide
└── STANDALONE_EXE_GUIDE.md # This file
```

## Summary

### ✅ Yes, You Can!

Create a single-click executable that:
- Requires no installation
- Requires no Python
- Requires no VS Code
- Just double-click and go!

### 📦 How to Build

```bash
# Simple way
BUILD.bat

# Or
python build_exe.py
```

### 🎯 Result

A professional desktop app that anyone can use!

---

**Ready to build?** Follow BUILD_INSTRUCTIONS.md

**Questions?** Check USER_GUIDE_EXE.md

**Happy building!** 🎵
