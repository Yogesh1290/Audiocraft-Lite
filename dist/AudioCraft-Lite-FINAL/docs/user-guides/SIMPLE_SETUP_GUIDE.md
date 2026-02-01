# 🎵 AudioCraft Lite - Simple Setup Guide

## ⚠️ Why Not PyInstaller?

We **don't recommend** the PyInstaller .exe approach because:
- ❌ Can cause file corruption issues
- ❌ Large file size (500MB-1GB)
- ❌ Antivirus false positives
- ❌ Difficult to update
- ❌ Can have runtime issues

## ✅ Better Solution: Batch File Launcher

Instead, we provide a **simple batch file** that:
- ✅ No corruption issues
- ✅ Easy to update
- ✅ No antivirus warnings
- ✅ Smaller download
- ✅ More reliable

## 📋 One-Time Setup (5 Minutes)

### Step 1: Install Python

1. Download Python 3.10 or 3.11 from: https://www.python.org/downloads/
2. **IMPORTANT**: Check "Add Python to PATH" during installation
3. Click "Install Now"

### Step 2: Download AudioCraft Lite

1. Download the zip file
2. Extract to any folder (e.g., `C:\AudioCraft-Lite`)

### Step 3: First Run

1. **Double-click**: `START_APP.bat`
2. Wait for automatic setup (2-5 minutes)
3. Browser opens automatically
4. Done!

## 🚀 Daily Use (After Setup)

### Option 1: Full Launcher (Recommended)
```
Double-click: START_APP.bat
```
- Shows progress
- Checks everything
- Opens browser automatically

### Option 2: Quick Start
```
Double-click: QUICK_START.bat
```
- Faster startup
- For experienced users
- Assumes setup is done

## 📁 What You Get

```
audiocraft-lite/
├── START_APP.bat        ← Double-click this! (First time & daily use)
├── QUICK_START.bat      ← Faster version (after setup)
├── backend/
│   ├── venv/           (created automatically)
│   ├── main.py
│   └── ...
└── frontend/
    └── ...
```

## 🎯 How It Works

### First Run:
```
[You double-click START_APP.bat]
         ↓
[Checks Python installed]
         ↓
[Creates virtual environment]
         ↓
[Installs dependencies]
         ↓
[Starts server]
         ↓
[Opens browser]
         ↓
[You generate audio!]
```

### Subsequent Runs:
```
[You double-click START_APP.bat]
         ↓
[Starts server immediately]
         ↓
[Opens browser]
         ↓
[Ready in 5-10 seconds!]
```

## ✅ Advantages Over .exe

### Reliability
- ✅ No corruption issues
- ✅ No file system problems
- ✅ Standard Python environment
- ✅ Easy to troubleshoot

### Updates
- ✅ Just replace files
- ✅ No rebuild needed
- ✅ Keep your settings
- ✅ Keep downloaded models

### Size
- ✅ Smaller download (~50MB vs 500MB)
- ✅ Models downloaded once
- ✅ Shared Python installation

### Security
- ✅ No antivirus warnings
- ✅ Standard Python code
- ✅ Easy to verify
- ✅ No false positives

## 🔧 Troubleshooting

### "Python is not installed"
**Solution**: Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH"

### "pip is not recognized"
**Solution**: Reinstall Python with "Add Python to PATH" checked

### Port 8000 already in use
**Solution**: 
1. Close other instances
2. Or change port in `backend/config.py`

### Browser doesn't open
**Solution**: Manually open http://localhost:8000

### Setup takes too long
**Solution**: This is normal for first run (downloading PyTorch ~2GB)

## 📊 Comparison

### PyInstaller .exe
```
Pros:
- Single file
- No Python needed

Cons:
- Can corrupt files ❌
- Large size (500MB-1GB)
- Antivirus warnings
- Hard to update
- Runtime issues
```

### Batch File Launcher
```
Pros:
- Reliable ✅
- No corruption ✅
- Easy to update ✅
- Smaller download ✅
- No antivirus issues ✅

Cons:
- Requires Python
- Slightly more setup
```

## 🎓 For Non-Technical Users

### What is a Batch File?
- A `.bat` file is a simple script for Windows
- Just double-click to run
- Like a shortcut that does multiple things
- Safe and standard Windows feature

### Is It Safe?
- ✅ Yes! Batch files are standard Windows scripts
- ✅ You can open it in Notepad to see what it does
- ✅ No hidden code or malware
- ✅ Open source and transparent

### Do I Need to Know Coding?
- ❌ No! Just double-click the .bat file
- ❌ No terminal commands needed
- ❌ No technical knowledge required
- ✅ Works like any other app

## 📦 Sharing with Others

### What to Share:
1. The entire `audiocraft-lite` folder (zipped)
2. This guide (SIMPLE_SETUP_GUIDE.md)
3. Python download link

### What Users Need:
1. Windows 10/11
2. Python 3.10 or 3.11 installed
3. 4-8GB RAM
4. 10-20GB disk space

### Instructions for Users:
1. Install Python (if not installed)
2. Extract the zip file
3. Double-click `START_APP.bat`
4. Wait for setup (first time only)
5. Start using!

## 🔄 Updating

### To Update:
1. Download new version
2. Extract to same folder (replace files)
3. Models and settings are preserved
4. No reinstall needed!

## 💡 Tips

### First Time Users:
1. Be patient during first setup (2-5 minutes)
2. Keep the console window open
3. Don't close the black window
4. Browser opens automatically

### Daily Users:
1. Use QUICK_START.bat for faster startup
2. Bookmark http://localhost:8000
3. Keep console window minimized
4. Close console to stop server

## 🆘 Getting Help

### If Something Goes Wrong:
1. Check this guide
2. Try restarting your computer
3. Delete `backend/venv` folder and run again
4. Check Python is installed correctly

### Common Issues:
- **Slow first run**: Normal (downloading models)
- **Console window**: Must stay open
- **Port in use**: Close other instances
- **Python error**: Reinstall Python with PATH

## 🎉 Success!

Once setup is complete:
- ✅ Double-click START_APP.bat
- ✅ Wait 5-10 seconds
- ✅ Browser opens
- ✅ Generate audio!

No VS Code, no terminal, no hassle!

---

## 📝 Summary

### Best Approach: Batch File Launcher

**Why?**
- More reliable than .exe
- No corruption issues
- Easy to update
- Smaller download
- No antivirus problems

**How?**
1. Install Python once
2. Double-click START_APP.bat
3. Done!

**For Users?**
- Simple as any app
- No technical knowledge needed
- Just double-click and go!

---

**Questions?** Check the troubleshooting section above.

**Ready to start?** Double-click `START_APP.bat`!

🎵 **Enjoy creating AI-generated music!** 🎶
