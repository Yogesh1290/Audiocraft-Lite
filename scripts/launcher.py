"""
AudioCraft Lite Launcher
Single-click launcher that starts both backend and opens browser
"""

import os
import sys
import time
import webbrowser
import subprocess
import threading
from pathlib import Path

def get_resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def start_backend():
    """Start the FastAPI backend server"""
    print("🚀 Starting AudioCraft Lite Backend...")
    
    # Get the backend directory
    backend_dir = get_resource_path("backend")
    
    # Start the backend server
    backend_script = os.path.join(backend_dir, "main.py")
    
    # Run the backend
    subprocess.run([sys.executable, backend_script], cwd=backend_dir)

def wait_for_server(url="http://localhost:8000", timeout=30):
    """Wait for the server to be ready"""
    import urllib.request
    import urllib.error
    
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            urllib.request.urlopen(url + "/health", timeout=1)
            return True
        except (urllib.error.URLError, Exception):
            time.sleep(0.5)
    return False

def open_browser():
    """Open the web browser to the app"""
    print("⏳ Waiting for server to start...")
    
    if wait_for_server():
        print("✅ Server is ready!")
        print("🌐 Opening browser...")
        time.sleep(1)
        webbrowser.open("http://localhost:8000")
        print("\n" + "="*60)
        print("🎵 AudioCraft Lite is running!")
        print("="*60)
        print("\n📍 URL: http://localhost:8000")
        print("\n⚠️  Keep this window open while using the app")
        print("❌ Close this window to stop the server\n")
    else:
        print("❌ Server failed to start. Please check for errors above.")

def main():
    """Main launcher function"""
    print("\n" + "="*60)
    print("🎵 AudioCraft Lite - AI Music Generation")
    print("="*60)
    print("\nPowered by Meta's AudioCraft")
    print("Presented by AI Music Studio .pro\n")
    
    # Start browser opener in a separate thread
    browser_thread = threading.Thread(target=open_browser, daemon=True)
    browser_thread.start()
    
    # Start backend (this will block)
    try:
        start_backend()
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down AudioCraft Lite...")
        print("Thank you for using AudioCraft Lite!\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        input("\nPress Enter to exit...")
        sys.exit(1)

if __name__ == "__main__":
    main()
