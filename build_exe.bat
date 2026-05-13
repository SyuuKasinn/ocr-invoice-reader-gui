@echo off
REM Build executable for OCR Invoice Reader GUI
REM This creates a standalone .exe file

echo ============================================
echo   Building OCR Invoice Reader GUI EXE
echo ============================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found!
    echo Please install Python 3.8 or higher
    pause
    exit /b 1
)

echo Step 1: Checking dependencies...
echo.

REM Install PyInstaller if not present
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo Installing PyInstaller...
    pip install pyinstaller
)

REM Install required packages
echo Installing GUI dependencies...
pip install tkinterdnd2 Pillow >nul 2>&1

echo.
echo Step 2: Cleaning previous builds...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "__pycache__" rmdir /s /q __pycache__

echo Step 3: Building executable...
echo.
echo This may take 2-5 minutes, please wait...
echo.

REM Build with PyInstaller
pyinstaller --clean ocr_gui.spec

if errorlevel 1 (
    echo.
    echo ERROR: Build failed!
    echo Check the output above for errors.
    pause
    exit /b 1
)

echo.
echo ============================================
echo   Build Complete!
echo ============================================
echo.

REM Check if exe was created
if exist "dist\OCR-Invoice-Reader-GUI.exe" (
    echo SUCCESS: Executable created at:
    echo   dist\OCR-Invoice-Reader-GUI.exe
    echo.
    echo File size:
    dir "dist\OCR-Invoice-Reader-GUI.exe" | findstr "OCR-Invoice-Reader-GUI.exe"
    echo.
    echo You can now copy this .exe to any Windows computer.
    echo No Python installation required on target machine!
    echo.
    echo IMPORTANT: The OCR engine (ocr-invoice-reader) must be
    echo installed on the target computer for processing to work:
    echo   pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git
    echo.
) else (
    echo ERROR: Executable not found in dist folder!
    echo Build may have failed.
)

echo.
echo Press any key to open dist folder...
pause >nul

explorer dist

exit /b 0
