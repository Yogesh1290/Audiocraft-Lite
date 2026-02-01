"""
Build script to create standalone Windows executable
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and print output"""
    print(f"\n▶ Running: {cmd}")
    result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=False)
    if result.returncode != 0:
        print(f"❌ Command failed with code {result.returncode}")
        sys.exit(1)
    return result

def main():
    print("\n" + "="*60)
    print("🔨 Building AudioCraft Lite Standalone Executable")
    print("="*60)
    
    root_dir = Path(__file__).parent
    frontend_dir = root_dir / "frontend"
    backend_dir = root_dir / "backend"
    dist_dir = root_dir / "dist"
    
    # Step 1: Build React frontend
    print("\n📦 Step 1: Building React frontend...")
    if not (frontend_dir / "node_modules").exists():
        print("Installing npm dependencies...")
        run_command("npm install", cwd=frontend_dir)
    
    print("Building React app...")
    run_command("npm run build", cwd=frontend_dir)
    
    if not (frontend_dir / "build").exists():
        print("❌ Frontend build failed!")
        sys.exit(1)
    
    print("✅ Frontend built successfully!")
    
    # Step 2: Install PyInstaller
    print("\n📦 Step 2: Installing PyInstaller...")
    run_command(f"{sys.executable} -m pip install pyinstaller")
    
    # Step 3: Create PyInstaller spec file
    print("\n📦 Step 3: Creating PyInstaller configuration...")
    
    spec_content = f"""
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['launcher.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('backend', 'backend'),
        ('frontend/build', 'frontend/build'),
    ],
    hiddenimports=[
        'uvicorn.logging',
        'uvicorn.loops',
        'uvicorn.loops.auto',
        'uvicorn.protocols',
        'uvicorn.protocols.http',
        'uvicorn.protocols.http.auto',
        'uvicorn.protocols.websockets',
        'uvicorn.protocols.websockets.auto',
        'uvicorn.lifespan',
        'uvicorn.lifespan.on',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='AudioCraft-Lite',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if Path('icon.ico').exists() else None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='AudioCraft-Lite',
)
"""
    
    spec_file = root_dir / "audiocraft-lite.spec"
    spec_file.write_text(spec_content)
    print("✅ PyInstaller spec created!")
    
    # Step 4: Build executable
    print("\n📦 Step 4: Building executable with PyInstaller...")
    print("⏳ This may take several minutes...")
    
    run_command(f"pyinstaller audiocraft-lite.spec --clean", cwd=root_dir)
    
    # Step 5: Verify build
    exe_path = dist_dir / "AudioCraft-Lite" / "AudioCraft-Lite.exe"
    if exe_path.exists():
        print("\n" + "="*60)
        print("✅ BUILD SUCCESSFUL!")
        print("="*60)
        print(f"\n📍 Executable location:")
        print(f"   {exe_path}")
        print(f"\n📦 Distribution folder:")
        print(f"   {dist_dir / 'AudioCraft-Lite'}")
        print("\n💡 To run:")
        print("   1. Navigate to the dist/AudioCraft-Lite folder")
        print("   2. Double-click AudioCraft-Lite.exe")
        print("   3. The app will start and open in your browser!")
        print("\n⚠️  Note: First run will download AI models (~6GB)")
        print("   Subsequent runs will be much faster.\n")
    else:
        print("\n❌ Build failed! Executable not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
