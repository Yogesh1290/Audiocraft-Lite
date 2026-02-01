# 🎵 AudioCraft Lite - User Guide

## What is AudioCraft Lite?

AudioCraft Lite is a **single-click desktop application** for AI-powered music and audio generation. No installation, no setup, no coding required!

## System Requirements

- **OS**: Windows 10 or 11
- **RAM**: 4-8GB (more is better)
- **Disk Space**: 10-20GB free
- **Internet**: Required for first run only (to download AI models)

## How to Use

### First Time Setup

1. **Extract** the zip file to any folder
2. **Navigate** to the extracted folder
3. **Double-click** `AudioCraft-Lite.exe`
4. **Wait** for the console window (black window) to appear
5. **Wait** for "Server is ready!" message
6. **Browser opens** automatically

⏳ **First run takes 2-5 minutes** to download AI models (~1-6GB)

### Using the App

1. **Choose Generation Mode**:
   - 🎹 **MusicGen** - Create full music compositions
   - 🔊 **AudioGen** - Generate sound effects

2. **Select Quality Level**:
   - ⚡ **Fast** - Quick generation (60-70% quality)
   - ⚖️ **Balanced** - Best for most uses (75-85% quality)
   - 🎯 **Premium** - Highest quality (90-95% quality)

3. **Describe Your Audio**:
   - Type what you want to create
   - Be specific and descriptive
   - Use the example prompts for inspiration

4. **Adjust Settings** (optional):
   - Duration: 1-300 seconds (5 minutes max)
   - Advanced settings available

5. **Click "Generate Audio"**:
   - Wait for generation to complete
   - Listen to your creation
   - Download if you like it!

## Example Prompts

### For Music:
- "Upbeat electronic dance music with heavy bass and synth melodies"
- "Calm acoustic guitar with soft piano accompaniment"
- "Epic orchestral soundtrack with dramatic strings"
- "Lo-fi hip hop beat with vinyl crackle and mellow piano"

### For Sound Effects:
- "Sound of rain falling on a window with distant thunder"
- "Dog barking in a park with birds chirping"
- "Ocean waves crashing on a beach"
- "Busy city street with cars and people"

## Generation Times

Depends on quality level and duration:

| Quality | 10s Audio | 30s Audio | 60s Audio |
|---------|-----------|-----------|-----------|
| Fast | ~15-20s | ~45-60s | ~90-120s |
| Balanced | ~30-40s | ~90-120s | ~180-240s |
| Premium | ~60-90s | ~180-240s | ~360-480s |

## Important Notes

### ⚠️ Keep Console Window Open
- The black console window **must stay open**
- This is the server running in the background
- Closing it will stop the app

### ⚠️ First Run is Slow
- Downloads AI models (~1-6GB)
- Only happens once
- Subsequent runs are much faster

### ⚠️ Internet Required (First Run Only)
- Needed to download models
- After that, works offline!

### ⚠️ Antivirus Warnings
- Some antivirus may flag the .exe
- This is a false positive
- The app is safe and open source

## Troubleshooting

### App Won't Start
1. Check if port 8000 is already in use
2. Try restarting your computer
3. Check antivirus isn't blocking it

### Browser Doesn't Open
1. Manually open: http://localhost:8000
2. Check if server started (console shows "Server is ready!")

### Generation Fails
1. Check your internet connection (first run)
2. Make sure you have enough disk space
3. Try a shorter duration
4. Try the Fast quality level

### Out of Memory
1. Close other applications
2. Use Fast quality instead of Premium
3. Generate shorter audio clips
4. Restart the app

### Models Won't Download
1. Check internet connection
2. Check firewall settings
3. Check disk space (need 10-20GB)

## Where Are Files Saved?

Generated audio files are saved in:
```
AudioCraft-Lite/backend/outputs/
```

You can also download directly from the web interface.

## Keyboard Shortcuts

- **Enter** in prompt field: Generate audio
- **Ctrl+C** in console: Stop the server

## Tips for Best Results

1. **Be Specific**: More details = better results
2. **Use Examples**: Click example prompts to get started
3. **Start Small**: Test with 10-30 seconds first
4. **Experiment**: Try different quality levels
5. **Iterate**: Refine your prompts based on results

## Quality vs Speed

Choose based on your needs:

- **Fast**: Quick tests, previews, iterations
- **Balanced**: Most production work (recommended)
- **Premium**: Final output, best quality

## Updating

To get updates:
1. Download new version
2. Extract to new folder
3. Models are reused (no re-download)

## Uninstalling

To remove:
1. Delete the AudioCraft-Lite folder
2. Delete models cache (optional):
   - Windows: `C:\Users\YourName\.cache\audiocraft-lite`

## Privacy & Data

- ✅ **Runs locally** - No data sent to cloud
- ✅ **Offline** - Works without internet (after first run)
- ✅ **Private** - Your prompts stay on your computer
- ✅ **Free** - No subscriptions, no limits

## Credits

- **Powered by**: Meta's AudioCraft (MusicGen & AudioGen)
- **Presented by**: AI Music Studio .pro
- **License**: MIT (Free & Open Source)
- **Models**: Meta AI Research
- **GitHub**: facebook/audiocraft

## Support

For issues or questions:
1. Check this guide
2. Check BUILD_INSTRUCTIONS.md
3. Visit the GitHub repository
4. Check Meta's AudioCraft documentation

## Legal

- **Open Source**: MIT License
- **Models**: Meta AudioCraft (MIT License)
- **Attribution**: Required (see LICENSE file)
- **Commercial Use**: Allowed with attribution

---

**Enjoy creating AI-generated music and audio!** 🎵🎶

**Version**: 3.0 Lite
**Last Updated**: 2026
