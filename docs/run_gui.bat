@echo off
title OCR Invoice Reader GUI
echo.
echo ================================================
echo    OCR Invoice Reader - Simple GUI
echo ================================================
echo.
echo Starting application...
echo.

REM Check if Python is available
python --version >/dev/null 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo.
    echo Please install Python 3.8+ from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Run the GUI
python src\ocr_gui_simple.py

if errorlevel 1 (
    echo.
    echo ERROR: Failed to start GUI.
    echo.
    echo Common issues:
    echo 1. ocr-invoice-reader not installed
    echo 2. Missing dependencies
    echo.
    echo See docs\INSTALL.md for help.
    echo.
    pause
)
