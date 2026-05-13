@echo off
REM Quick launch script for OCR Invoice Reader GUI
REM Windows batch file

echo Starting OCR Invoice Reader GUI...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

REM Run the GUI
python ocr_gui.py

pause
