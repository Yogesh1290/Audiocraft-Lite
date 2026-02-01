@echo off
title AudioCraft Lite
color 0B

echo.
echo Starting AudioCraft Lite...
echo.

cd backend
call venv\Scripts\activate.bat

start /B timeout /t 2 /nobreak >nul && start http://localhost:8000

python main.py
