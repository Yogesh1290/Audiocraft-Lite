@echo off
echo Creating desktop shortcut...

set SCRIPT_DIR=%~dp0
set SHORTCUT_PATH=%USERPROFILE%\Desktop\AudioCraft Lite.lnk

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%SHORTCUT_PATH%'); $Shortcut.TargetPath = '%SCRIPT_DIR%START_APP.bat'; $Shortcut.WorkingDirectory = '%SCRIPT_DIR%'; $Shortcut.Description = 'AudioCraft Lite - AI Music Generation'; $Shortcut.Save()"

if exist "%SHORTCUT_PATH%" (
    echo.
    echo [SUCCESS] Shortcut created on your desktop!
    echo.
    echo You can now double-click "AudioCraft Lite" on your desktop to start the app.
    echo.
) else (
    echo.
    echo [ERROR] Failed to create shortcut.
    echo.
)

pause
