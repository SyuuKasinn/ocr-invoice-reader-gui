@echo off
echo ========================================
echo   Testing OCR Invoice Reader Optimized
echo ========================================
echo.

cd /d "%~dp0.."

if not exist "dist\OCR-Invoice-Reader-Optimized\OCR-Invoice-Reader-Optimized.exe" (
    echo [ERROR] Executable not found!
    echo Expected: dist\OCR-Invoice-Reader-Optimized\OCR-Invoice-Reader-Optimized.exe
    pause
    exit /b 1
)

echo [OK] Executable found
echo.
echo Checking file size...
dir dist\OCR-Invoice-Reader-Optimized\OCR-Invoice-Reader-Optimized.exe | findstr "OCR-Invoice-Reader-Optimized.exe"
echo.

echo Starting application...
echo.
start "" "dist\OCR-Invoice-Reader-Optimized\OCR-Invoice-Reader-Optimized.exe"

echo.
echo ========================================
echo Application launched!
echo.
echo Performance tips:
echo - First scan: ~15s (loads model)
echo - 2nd scan onward: ~3s (5x faster!)
echo.
echo Keep the app open to process multiple
echo files continuously for best performance.
echo ========================================
pause
