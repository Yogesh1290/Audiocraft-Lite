@echo off
title Open My Audio Files
color 0B

echo.
echo ============================================================
echo  Opening Your Generated Audio Files
echo ============================================================
echo.

set OUTPUT_DIR=%~dp0backend\outputs

REM Create outputs directory if it doesn't exist
if not exist "%OUTPUT_DIR%" (
    mkdir "%OUTPUT_DIR%"
    echo [INFO] Creating outputs folder...
    echo.
)

REM Check if folder has any files
dir /b "%OUTPUT_DIR%\*.wav" >nul 2>&1
if errorlevel 1 (
    echo [INFO] No audio files found yet.
    echo.
    echo Generate some audio first, then your files will appear here!
    echo.
) else (
    echo [SUCCESS] Opening your audio files folder...
    echo.
)

REM Open the folder in Windows Explorer
start "" "%OUTPUT_DIR%"

echo.
echo ============================================================
echo  Folder Location:
echo  %OUTPUT_DIR%
echo ============================================================
echo.
echo You can:
echo  - Listen to your audio files
echo  - Copy them to another location
echo  - Delete old files you don't need
echo.
timeout /t 3 /nobreak >nul
