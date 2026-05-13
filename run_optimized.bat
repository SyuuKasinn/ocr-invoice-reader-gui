@echo off
REM Quick launcher for optimized version

echo Starting OCR Invoice Reader (Optimized)...
echo.

if exist "dist\OCR-Invoice-Reader-Optimized\OCR-Invoice-Reader-Optimized.exe" (
    cd dist\OCR-Invoice-Reader-Optimized
    start OCR-Invoice-Reader-Optimized.exe
) else if exist "ocr_gui_optimized.py" (
    echo EXE not found, running Python version...
    python ocr_gui_optimized.py
) else (
    echo Error: Neither EXE nor Python file found!
    pause
)
