@echo off
title AudioCraft Lite - AI Music Generation
color 0B

echo.
echo ============================================================
echo            AudioCraft Lite - AI Music Generation
echo ============================================================
echo.
echo Powered by Meta's AudioCraft
echo Presented by AI Music Studio .pro
echo.
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed!
    echo.
    echo Please install Python 3.10 or 3.11 from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

REM Check if virtual environment exists
if not exist "backend\venv" (
    echo [2/3] Setting up for first time...
    echo This will take a few minutes...
    echo.
    
    cd backend
    python -m venv venv
    call venv\Scripts\activate.bat
    
    echo Installing PyTorch CPU version...
    pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
    
    echo Installing other dependencies...
    pip install -r requirements-simple.txt
    
    cd ..
    echo.
    echo [SUCCESS] Setup complete!
    echo.
) else (
    echo [2/3] Environment ready!
    echo.
)

echo [3/3] Starting AudioCraft Lite...
echo.
echo ============================================================
echo  The app will open in your browser automatically
echo  Keep this window OPEN while using the app
echo  Close this window to STOP the server
echo ============================================================
echo.

REM Start backend
cd backend
call venv\Scripts\activate.bat

REM Open browser after 3 seconds
start /B timeout /t 3 /nobreak >nul && start http://localhost:8000

REM Start the server
python main.py

REM If server stops
echo.
echo ============================================================
echo  AudioCraft Lite has stopped
echo ============================================================
echo.
pause
