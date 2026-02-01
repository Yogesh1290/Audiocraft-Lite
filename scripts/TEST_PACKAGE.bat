@echo off
title Test AudioCraft Lite Package
color 0B

cls
echo.
echo ============================================================
echo  Testing AudioCraft Lite Package
echo ============================================================
echo.

REM Check Python
echo [TEST 1/6] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [FAIL] Python is not installed
    echo Install from: https://www.python.org/downloads/
    goto END
) else (
    python --version
    echo [PASS] Python is installed
)
echo.

REM Check Node.js (optional)
echo [TEST 2/6] Checking Node.js installation...
where node >nul 2>&1
if errorlevel 1 (
    echo [SKIP] Node.js not found (optional)
) else (
    node --version
    echo [PASS] Node.js is installed
)
echo.

REM Check main files
echo [TEST 3/6] Checking main files...
set MISSING=0

if not exist "AudioCraft-Lite.bat" (
    echo [FAIL] AudioCraft-Lite.bat not found
    set MISSING=1
) else (
    echo [PASS] AudioCraft-Lite.bat found
)

if not exist "OPEN_MY_AUDIO_FILES.bat" (
    echo [FAIL] OPEN_MY_AUDIO_FILES.bat not found
    set MISSING=1
) else (
    echo [PASS] OPEN_MY_AUDIO_FILES.bat found
)

if not exist "README.md" (
    echo [FAIL] README.md not found
    set MISSING=1
) else (
    echo [PASS] README.md found
)

if %MISSING%==1 goto END
echo.

REM Check backend
echo [TEST 4/6] Checking backend files...
if not exist "backend\main.py" (
    echo [FAIL] backend\main.py not found
    goto END
) else (
    echo [PASS] backend\main.py found
)

if not exist "backend\model_manager.py" (
    echo [FAIL] backend\model_manager.py not found
    goto END
) else (
    echo [PASS] backend\model_manager.py found
)

if not exist "backend\config.py" (
    echo [FAIL] backend\config.py not found
    goto END
) else (
    echo [PASS] backend\config.py found
)

if not exist "backend\requirements-simple.txt" (
    echo [FAIL] backend\requirements-simple.txt not found
    goto END
) else (
    echo [PASS] backend\requirements-simple.txt found
)
echo.

REM Check frontend
echo [TEST 5/6] Checking frontend build...
if not exist "frontend\build\index.html" (
    echo [FAIL] Frontend build not found
    echo Run: cd frontend && npm run build
    goto END
) else (
    echo [PASS] Frontend build found
)
echo.

REM Check documentation
echo [TEST 6/6] Checking documentation...
if not exist "docs\user-guides\START_HERE_SIMPLE.md" (
    echo [FAIL] User guides not found
    goto END
) else (
    echo [PASS] User guides found
)

if not exist "docs\technical\ARCHITECTURE.md" (
    echo [FAIL] Technical docs not found
    goto END
) else (
    echo [PASS] Technical docs found
)

if not exist "docs\developer\BUILD_INSTRUCTIONS.md" (
    echo [FAIL] Developer docs not found
    goto END
) else (
    echo [PASS] Developer docs found
)
echo.

REM All tests passed
echo ============================================================
echo  ALL TESTS PASSED!
echo ============================================================
echo.
echo Your package is ready!
echo.
echo NEXT STEPS:
echo  1. Run PREPARE_FOR_DISTRIBUTION.bat to create clean package
echo  2. Or test locally by running AudioCraft-Lite.bat
echo.
goto SUCCESS

:END
echo.
echo ============================================================
echo  TESTS FAILED
echo ============================================================
echo.
echo Please fix the issues above before distributing.
echo.
pause
exit /b 1

:SUCCESS
pause
exit /b 0
