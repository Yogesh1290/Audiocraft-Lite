# 🔨 Building AudioCraft Lite Standalone Executable

## Overview

This guide will help you create a single-click Windows executable (.exe) that bundles everything together - no VS Code, no terminal, no setup required!

## Prerequisites

Before building, make sure you have:

1. ✅ **Python 3.10 or 3.11** installed
2. ✅ **Node.js** installed (for building React frontend)
3. ✅ All dependencies installed:
   ```bash
   cd backend
   pip install -r requirements-simple.txt
   pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
   ```

## Quick Build (Easiest)

### Option 1: Using Batch File (Windows)

Simply double-click:
```
BUILD.bat
```

That's it! The script will:
1. Build the React frontend
2. Install PyInstaller
3. Create the executable
4. Show you where to find it

### Option 2: Using Python Script

```bash
python build_exe.py
```

## What Gets Built

The build process creates:

```
dist/
└── AudioCraft-Lite/
    ├── AudioCraft-Lite.exe  ← Double-click this!
    ├── backend/             (bundled)
    ├── frontend/build/      (bundled)
    └── [other dependencies]
```

## How to Use the Executable

### For End Users:

1. **Navigate** to `dist/AudioCraft-Lite/` folder
2. **Double-click** `AudioCraft-Lite.exe`
3. **Wait** for the console window to show "Server is ready!"
4. **Browser opens** automatically to http://localhost:8000
5. **Start generating** audio!

### Important Notes:

- ⚠️ **Keep the console window open** while using the app
- ⚠️ **First run** will download AI models (~1-6GB depending on model)
- ⚠️ **Subsequent runs** will be much faster
- ❌ **Close the console** to stop the server

## Distribution

### To Share with Others:

1. **Zip the entire folder**:
   ```
   dist/AudioCraft-Lite/  → AudioCraft-Lite.zip
   ```

2. **Share the zip file** with users

3. **Users extract** and double-click the .exe

### What Users Need:

- ✅ Windows 10/11
- ✅ 4-8GB RAM (depending on model size)
- ✅ 10-20GB free disk space (for models)
- ✅ Internet connection (first run only, to download models)

## Troubleshooting Build Issues

### Issue: "npm not found"
**Solution**: Install Node.js from https://nodejs.org/

### Issue: "PyInstaller not found"
**Solution**: Run `pip install pyinstaller`

### Issue: "Frontend build failed"
**Solution**: 
```bash
cd frontend
npm install
npm run build
```

### Issue: "Module not found" errors
**Solution**: Make sure all backend dependencies are installed:
```bash
cd backend
pip install -r requirements-simple.txt
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
```

### Issue: Executable is too large
**Solution**: This is normal! The exe includes:
- Python runtime
- PyTorch (CPU version)
- All dependencies
- Frontend build
- Typically 500MB-1GB

## Advanced: Custom Icon

To add a custom icon:

1. Create or download an `.ico` file
2. Name it `icon.ico`
3. Place it in the root directory (next to `launcher.py`)
4. Rebuild

## Advanced: Reducing Size

To reduce executable size:

1. **Use UPX compression** (already enabled)
2. **Exclude unused modules** in the spec file
3. **Use smaller PyTorch build** (already using CPU-only)

## Build Output Structure

```
audiocraft-lite/
├── launcher.py              # Main launcher script
├── build_exe.py            # Build automation script
├── BUILD.bat               # Windows batch file
├── audiocraft-lite.spec    # PyInstaller configuration
├── backend/                # Backend code (bundled)
├── frontend/build/         # Frontend build (bundled)
├── build/                  # Temporary build files
└── dist/
    └── AudioCraft-Lite/    # Final distributable
        └── AudioCraft-Lite.exe  # The executable!
```

## Testing the Executable

Before distributing:

1. **Test on your machine**:
   - Double-click the .exe
   - Verify it opens browser
   - Generate a test audio
   - Check all features work

2. **Test on a clean machine** (if possible):
   - No Python installed
   - No dependencies
   - Fresh Windows install

3. **Check file paths**:
   - Models download correctly
   - Outputs save properly
   - No hardcoded paths

## Updating the Executable

When you make changes:

1. **Update the code** (backend or frontend)
2. **Run the build script** again
3. **Test the new executable**
4. **Redistribute** to users

## Performance Notes

### Executable Performance:
- ✅ Same performance as running from source
- ✅ No overhead from bundling
- ✅ Models cached after first download

### Startup Time:
- First run: ~30-60 seconds (model download)
- Subsequent runs: ~5-10 seconds

## Security Notes

### Antivirus Warnings:
- Some antivirus software may flag the .exe
- This is a **false positive** (common with PyInstaller)
- Users may need to add an exception

### Code Signing (Optional):
To avoid antivirus warnings:
1. Get a code signing certificate
2. Sign the executable
3. Costs money but improves trust

## Alternative: Installer

To create a proper installer:

1. Use **Inno Setup** or **NSIS**
2. Create an installer that:
   - Installs to Program Files
   - Creates desktop shortcut
   - Adds to Start Menu
   - Handles uninstall

Example Inno Setup script available on request.

## FAQ

**Q: Can I build for Mac/Linux?**
A: Yes! Use PyInstaller on those platforms. The process is similar.

**Q: How big is the final executable?**
A: ~500MB-1GB including all dependencies.

**Q: Do users need Python installed?**
A: No! Everything is bundled.

**Q: Can I update models without rebuilding?**
A: Yes! Models are downloaded at runtime, not bundled.

**Q: How do I add more features?**
A: Update the code, rebuild, redistribute.

**Q: Can I sell this?**
A: Check the MIT license. Attribution required.

## Support

For build issues:
1. Check this documentation
2. Verify all prerequisites
3. Check error messages carefully
4. Try building on a clean Python environment

## Credits

- **Meta's AudioCraft** - AI models
- **PyInstaller** - Executable bundling
- **React** - Frontend framework
- **FastAPI** - Backend framework

---

**Happy Building!** 🎵

For questions or issues, refer to the main documentation.
