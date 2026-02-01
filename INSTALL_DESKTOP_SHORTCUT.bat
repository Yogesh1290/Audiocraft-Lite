@echo off
title Create Desktop Shortcut
color 0B

echo.
echo ============================================================
echo  Creating Desktop Shortcut for AudioCraft Lite
echo ============================================================
echo.

set SCRIPT_DIR=%~dp0
set SHORTCUT_NAME=AudioCraft Lite.lnk
set SHORTCUT_PATH=%USERPROFILE%\Desktop\%SHORTCUT_NAME%
set TARGET=%SCRIPT_DIR%AudioCraft-Lite.bat

echo Creating shortcut on your desktop...
echo.

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%TARGET%'; $Shortcut.WorkingDirectory = '%SCRIPT_DIR%'; $Shortcut.Description = 'AudioCraft Lite - AI Music Generation - Double-click to start'; $Shortcut.Save()"

if exist "%SHORTCUT_PATH%" (
    echo ============================================================
    echo  SUCCESS!
    echo ============================================================
    echo.
    echo A shortcut has been created on your desktop!
    echo.
    echo Look for: "AudioCraft Lite"
    echo.
    echo To use the app:
    echo  1. Double-click the shortcut on your desktop
    echo  2. Wait for the browser to open
    echo  3. Start creating music!
    echo.
    echo To stop the app:
    echo  - Close the black window that appears
    echo.
) else (
    echo ============================================================
    echo  ERROR
    echo ============================================================
    echo.
    echo Failed to create shortcut.
    echo.
    echo Please try:
    echo  1. Run this file as Administrator
    echo  2. Or manually create a shortcut to AudioCraft-Lite.bat
    echo.
)

echo.
pause
