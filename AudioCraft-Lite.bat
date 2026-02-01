@echo off
setlocal enabledelayedexpansion
title AudioCraft Lite - AI Music Generation
color 0B

REM ============================================================
REM  AudioCraft Lite - One-Click Launcher
REM  Handles: Setup, Dependencies, Frontend, Backend, Exit
REM ============================================================

:MAIN_MENU
cls
echo.
echo ============================================================
echo            AudioCraft Lite - AI Music Generation
echo ============================================================
echo.
echo  Powered by Meta's AudioCraft
echo  Presented by AI Music Studio .pro
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
    echo IMPORTANT: Check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo [CHECK] Python found: 
python --version
echo.

REM Check if Node.js is installed
where node >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Node.js not found - Frontend will not be built
    echo You can still use the app if frontend is already built
    echo.
    set NODEJS_INSTALLED=0
) else (
    echo [CHECK] Node.js found:
    node --version
    echo.
    set NODEJS_INSTALLED=1
)

REM Check if setup is needed
if not exist "backend\venv" (
    echo [SETUP REQUIRED] First time setup needed
    echo.
    goto FIRST_TIME_SETUP
)

if not exist "frontend\build" (
    if !NODEJS_INSTALLED! equ 1 (
        echo [SETUP REQUIRED] Frontend build needed
        echo.
        goto BUILD_FRONTEND
    )
)

echo [READY] All dependencies installed
echo.
goto START_APP

:FIRST_TIME_SETUP
echo ============================================================
echo  FIRST TIME SETUP
echo ============================================================
echo.
echo This will:
echo  1. Create Python virtual environment
echo  2. Install backend dependencies (~2GB download)
echo  3. Build frontend (if Node.js available)
echo.
echo This takes 5-10 minutes. Please be patient...
echo.
pause

echo.
echo [1/4] Creating virtual environment...
cd backend
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)
echo [SUCCESS] Virtual environment created
echo.

echo [2/4] Installing PyTorch (CPU version)...
echo This is a large download (~2GB), please wait...
call venv\Scripts\activate.bat
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cpu
if errorlevel 1 (
    echo [ERROR] Failed to install PyTorch
    pause
    exit /b 1
)
echo [SUCCESS] PyTorch installed
echo.

echo [3/4] Installing other dependencies...
pip install -r requirements-simple.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [SUCCESS] Dependencies installed
echo.

cd ..

if !NODEJS_INSTALLED! equ 1 (
    goto BUILD_FRONTEND
) else (
    echo [SKIP] Node.js not found, skipping frontend build
    echo.
    goto SETUP_COMPLETE
)

:BUILD_FRONTEND
echo [4/4] Building frontend...
cd frontend

if not exist "node_modules" (
    echo Installing npm packages...
    call npm install
    if errorlevel 1 (
        echo [ERROR] Failed to install npm packages
        cd ..
        pause
        exit /b 1
    )
)

echo Building React app...
call npm run build
if errorlevel 1 (
    echo [ERROR] Failed to build frontend
    cd ..
    pause
    exit /b 1
)
echo [SUCCESS] Frontend built
echo.

cd ..

:SETUP_COMPLETE
echo.
echo ============================================================
echo  SETUP COMPLETE!
echo ============================================================
echo.
echo AudioCraft Lite is ready to use!
echo.
pause
goto START_APP

:START_APP
cls
echo.
echo ============================================================
echo            Starting AudioCraft Lite
echo ============================================================
echo.
echo [INFO] Starting backend server...
echo [INFO] Browser will open automatically in 5 seconds
echo.
echo ============================================================
echo  IMPORTANT INSTRUCTIONS:
echo ============================================================
echo.
echo  - Keep this window OPEN while using the app
echo  - The app will open in your browser
echo  - To STOP the app: Close this window or press Ctrl+C
echo  - No background processes will remain after closing
echo.
echo ============================================================
echo.

REM Create a PID file to track the process
set PID_FILE=%TEMP%\audiocraft_lite.pid
echo %RANDOM% > "%PID_FILE%"

REM Start backend in background and capture PID
cd backend
call venv\Scripts\activate.bat

REM Open browser after 5 seconds
start /B cmd /c "timeout /t 5 /nobreak >nul && start http://localhost:8000"

REM Start the server (this will block until Ctrl+C or window closed)
echo [RUNNING] Server starting on http://localhost:8000
echo.
python main.py

REM If we reach here, server was stopped
goto CLEANUP

:CLEANUP
echo.
echo ============================================================
echo  Shutting down AudioCraft Lite...
echo ============================================================
echo.

REM Kill any remaining Python processes related to this app
taskkill /F /FI "WINDOWTITLE eq AudioCraft Lite*" >nul 2>&1

REM Clean up PID file
if exist "%PID_FILE%" del "%PID_FILE%"

REM Make sure no port 8000 processes remain
for /f "tokens=5" %%a in ('netstat -aon ^| find ":8000" ^| find "LISTENING"') do (
    taskkill /F /PID %%a >nul 2>&1
)

echo [SUCCESS] All processes stopped
echo [SUCCESS] No background processes remaining
echo.
echo ============================================================
echo  AudioCraft Lite has been closed safely
echo ============================================================
echo.
echo Thank you for using AudioCraft Lite!
echo.
timeout /t 3 /nobreak >nul
exit /b 0
