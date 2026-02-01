@echo off
setlocal enabledelayedexpansion
title Prepare AudioCraft Lite for Distribution
color 0B

cls
echo.
echo ============================================================
echo  Preparing AudioCraft Lite for Distribution
echo ============================================================
echo.
echo This will create a clean package ready to share with users.
echo.
pause

REM Create distribution folder
set DIST_FOLDER=AudioCraft-Lite-Distribution
if exist "%DIST_FOLDER%" (
    echo Removing old distribution folder...
    rmdir /s /q "%DIST_FOLDER%"
)

echo.
echo [1/5] Creating distribution folder...
mkdir "%DIST_FOLDER%"

REM Copy main files
echo [2/5] Copying main files...
copy AudioCraft-Lite.bat "%DIST_FOLDER%\"
copy OPEN_MY_AUDIO_FILES.bat "%DIST_FOLDER%\"
copy INSTALL_DESKTOP_SHORTCUT.bat "%DIST_FOLDER%\"
copy README.md "%DIST_FOLDER%\"
copy FOLDER_STRUCTURE.txt "%DIST_FOLDER%\"

REM Copy documentation
echo [3/5] Copying documentation...
xcopy /E /I /Y docs "%DIST_FOLDER%\docs"

REM Copy backend (excluding venv and outputs)
echo [4/5] Copying backend...
mkdir "%DIST_FOLDER%\backend"
xcopy /E /I /Y backend "%DIST_FOLDER%\backend" /EXCLUDE:exclude_list.txt

REM Create exclude list temporarily
echo venv > exclude_list.txt
echo __pycache__ >> exclude_list.txt
echo *.pyc >> exclude_list.txt
echo .pytest_cache >> exclude_list.txt

REM Copy backend files manually to avoid venv
for %%F in (backend\*.py backend\*.txt) do (
    copy "%%F" "%DIST_FOLDER%\backend\"
)

REM Create empty outputs folder
mkdir "%DIST_FOLDER%\backend\outputs"
echo Your generated audio files will be saved here > "%DIST_FOLDER%\backend\outputs\README.txt"

REM Copy frontend build
echo [5/5] Copying frontend...
if exist "frontend\build" (
    xcopy /E /I /Y frontend\build "%DIST_FOLDER%\frontend\build"
) else (
    echo [WARNING] Frontend build not found!
    echo Please run: cd frontend && npm run build
)

REM Clean up
del exclude_list.txt

REM Create a README for distribution
echo Creating distribution README...
(
echo ============================================================
echo  AudioCraft Lite - Ready for Distribution
echo ============================================================
echo.
echo This package is ready to share with users!
echo.
echo WHAT TO DO:
echo  1. Zip the entire "%DIST_FOLDER%" folder
echo  2. Share the zip file with users
echo  3. Users extract and double-click AudioCraft-Lite.bat
echo.
echo WHAT USERS NEED:
echo  - Windows 10/11
echo  - Python 3.10 or 3.11 installed
echo  - 4-8GB RAM
echo  - 10-20GB disk space
echo.
echo FIRST RUN:
echo  - Takes 10-15 minutes (downloads AI models)
echo  - Subsequent runs are fast (5-10 seconds)
echo.
echo INCLUDED:
echo  - Main launcher (AudioCraft-Lite.bat)
echo  - File viewer (OPEN_MY_AUDIO_FILES.bat)
echo  - Desktop shortcut creator
echo  - Complete documentation
echo  - Backend code
echo  - Frontend build
echo.
echo NOT INCLUDED (Downloaded on first run):
echo  - Python virtual environment
echo  - AI models (~2-6GB)
echo  - Dependencies
echo.
echo ============================================================
) > "%DIST_FOLDER%\DISTRIBUTION_README.txt"

echo.
echo ============================================================
echo  SUCCESS!
echo ============================================================
echo.
echo Distribution package created: %DIST_FOLDER%\
echo.
echo NEXT STEPS:
echo  1. Test the package (run AudioCraft-Lite.bat inside)
echo  2. Zip the folder: %DIST_FOLDER%.zip
echo  3. Share with users!
echo.
echo Package size: ~50-100MB (without models)
echo With models: ~7-20GB (downloaded by users)
echo.
pause
