@echo off

REM Start script for AudioCraft Lite Backend (Windows)

echo Starting AudioCraft Lite Backend...

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Install/update dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Create outputs directory
if not exist "outputs" mkdir outputs

REM Start the server
echo Starting FastAPI server...
python main.py
