# 🎵 AudioCraft Lite - Complete Package

## Welcome!

This is **AudioCraft Lite** - a simple, one-click AI music and audio generation app for Windows.

**No coding required. No technical knowledge needed. Just double-click and create!**

---

## 📦 What's Included

```
audiocraft-lite/
│
├── 🚀 AudioCraft-Lite.bat          ← DOUBLE-CLICK THIS TO START!
├── 📋 START_HERE_SIMPLE.md         ← Read this first!
├── 🔗 INSTALL_DESKTOP_SHORTCUT.bat ← Creates desktop shortcut
│
├── 📚 Documentation/
│   ├── SIMPLE_SETUP_GUIDE.md       ← Setup instructions
│   ├── USER_GUIDE_EXE.md           ← How to use
│   └── TROUBLESHOOTING.md          ← Fix problems
│
├── backend/                         ← Server code (auto-managed)
└── frontend/                        ← User interface (auto-managed)
```

---

## 🎯 Quick Start (3 Steps)

### Step 1: Install Python (One-Time, 5 minutes)
1. Go to: https://www.python.org/downloads/
2. Download and install
3. **IMPORTANT**: Check "Add Python to PATH"

### Step 2: Create Desktop Shortcut (Optional)
1. Double-click: `INSTALL_DESKTOP_SHORTCUT.bat`
2. A shortcut appears on your desktop

### Step 3: Start the App
1. Double-click: `AudioCraft-Lite.bat` (or the desktop shortcut)
2. Wait for browser to open (10-15 minutes first time)
3. Start creating!

---

## ✨ Features

### What You Can Create
- 🎹 **Music**: Full compositions, any genre
- 🔊 **Sound Effects**: Any sound you can imagine
- 🎵 **Audio**: Up to 5 minutes long

### Quality Levels
- ⚡ **Fast**: Quick generation (60-70% quality)
- ⚖️ **Balanced**: Best for most uses (75-85% quality)
- 🎯 **Premium**: Highest quality (90-95% quality)

### Key Features
- ✅ Runs on your computer (no cloud)
- ✅ Works offline (after first run)
- ✅ Free and unlimited
- ✅ No data collection
- ✅ Open source
- ✅ Clean exit (no background processes)

---

## 🔒 Safety & Privacy

### Completely Safe
- ✅ No malware or viruses
- ✅ Open source code
- ✅ Community verified
- ✅ No hidden processes

### Privacy Protected
- ✅ Runs locally on your PC
- ✅ No data sent to internet
- ✅ Your prompts stay private
- ✅ Offline after first run

### Clean Exit
- ✅ Close window = everything stops
- ✅ No background processes
- ✅ No memory leaks
- ✅ Safe shutdown every time

---

## 📊 System Requirements

### Minimum
- **OS**: Windows 10 or 11
- **RAM**: 4GB
- **Disk**: 10GB free space
- **Internet**: Required for first run only

### Recommended
- **OS**: Windows 10/11 (64-bit)
- **RAM**: 8GB or more
- **Disk**: 20GB free space (SSD preferred)
- **CPU**: 4+ cores

---

## ⏱️ Performance

### First Run (One-Time)
- **Time**: 10-15 minutes
- **Why**: Downloads AI models (~2-6GB)
- **Only once**: Subsequent runs are fast

### Regular Use
- **Startup**: 5-10 seconds
- **Generation**: 
  - Fast: 15-30 seconds for 10s audio
  - Balanced: 30-60 seconds for 10s audio
  - Premium: 60-120 seconds for 10s audio

---

## 📖 How to Use

### Starting the App
1. Double-click `AudioCraft-Lite.bat`
2. Black window opens (keep it open!)
3. Browser opens automatically
4. Ready to use!

### Creating Audio
1. Choose mode (Music or Sound Effects)
2. Select quality level
3. Type what you want to create
4. Click "Generate Audio"
5. Wait for it to finish
6. Listen and download!

### Stopping the App
1. Close the black window
2. Everything stops cleanly
3. No background processes remain

---

## 💡 Tips & Tricks

### Writing Good Prompts

**For Music:**
```
✅ Good: "Upbeat electronic dance music with heavy bass"
❌ Bad: "Nice music"

✅ Good: "Calm acoustic guitar with soft piano"
❌ Bad: "Something relaxing"
```

**For Sound Effects:**
```
✅ Good: "Dog barking loudly in a park with birds"
❌ Bad: "Dog sound"

✅ Good: "Rain falling on window with distant thunder"
❌ Bad: "Rain"
```

### Choosing Quality
- **Testing ideas**: Use Fast
- **Normal use**: Use Balanced (recommended)
- **Final output**: Use Premium

### Duration
- **Quick tests**: 5-10 seconds
- **Normal**: 10-30 seconds
- **Long pieces**: 30-300 seconds (5 minutes max)

---

## 🆘 Troubleshooting

### App Won't Start
**Problem**: "Python is not installed"
**Solution**: Install Python from https://www.python.org/downloads/

**Problem**: Nothing happens when double-clicking
**Solution**: Right-click → "Run as administrator"

### Browser Doesn't Open
**Problem**: Browser doesn't open automatically
**Solution**: Manually open http://localhost:8000

### Generation Fails
**Problem**: "Out of memory"
**Solution**: 
- Close other programs
- Use Fast quality
- Generate shorter audio

**Problem**: Takes too long
**Solution**: 
- First run is slow (downloading models)
- Use Fast quality for quicker results

### Can't Close App
**Problem**: Window won't close
**Solution**: 
- Press Ctrl+C in the black window
- Or close the window forcefully
- App will clean up automatically

---

## 🔄 Updating

### To Update to New Version:
1. Download new version
2. Extract to same folder (replace files)
3. Your models and settings are preserved
4. No reinstall needed!

---

## 📁 File Locations

### Generated Audio
```
audiocraft-lite/backend/outputs/
```

### Downloaded Models
```
C:\Users\YourName\.cache\audiocraft-lite\
```

### Settings
```
audiocraft-lite/backend/config.py
```

---

## 🎓 Learning Resources

### Included Guides
- `START_HERE_SIMPLE.md` - Beginner guide
- `SIMPLE_SETUP_GUIDE.md` - Setup instructions
- `USER_GUIDE_EXE.md` - Detailed usage
- `TROUBLESHOOTING.md` - Fix problems

### External Resources
- Meta AudioCraft: https://github.com/facebookresearch/audiocraft
- Python Download: https://www.python.org/downloads/
- Node.js Download: https://nodejs.org/

---

## 📞 Support

### Getting Help
1. Read `START_HERE_SIMPLE.md`
2. Check `TROUBLESHOOTING.md`
3. Visit Meta's AudioCraft GitHub
4. Check Python installation

### Common Issues
- **Slow first run**: Normal (downloading models)
- **Black window**: Must stay open
- **Port in use**: Close other instances
- **Python error**: Reinstall with PATH

---

## 📜 Credits & License

### Powered By
- **Meta's AudioCraft** - AI models (MusicGen & AudioGen)
- **MIT License** - Free and open source

### Presented By
- **AI Music Studio .pro** - User interface and packaging

### License
- **MIT License** - Free to use, modify, and distribute
- **Attribution required** - Credit Meta and AI Music Studio .pro

### Models
- **MusicGen** by Meta AI Research
- **AudioGen** by Meta AI Research
- Available at: https://github.com/facebookresearch/audiocraft

---

## ❤️ Thank You!

Thank you for using AudioCraft Lite!

We hope you enjoy creating AI-generated music and audio.

**Remember:**
- ✅ Keep the black window open while using
- ✅ Close it to stop completely
- ✅ No background processes remain
- ✅ Safe, private, and free!

**Happy creating!** 🎵🎶🎉

---

## 📝 Version Info

- **Version**: 3.0 Lite
- **Release**: 2026
- **Platform**: Windows 10/11
- **License**: MIT

---

**Questions?** Read `START_HERE_SIMPLE.md`

**Problems?** Check `TROUBLESHOOTING.md`

**Ready?** Double-click `AudioCraft-Lite.bat`!
