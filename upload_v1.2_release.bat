@echo off
echo.
echo ========================================
echo   Upload v1.2 Release to GitHub
echo ========================================
echo.

REM Check if logged in
"C:\Program Files\GitHub CLI\gh.exe" auth status >nul 2>&1
if errorlevel 1 (
    echo [Step 1] Login to GitHub...
    echo.
    "C:\Program Files\GitHub CLI\gh.exe" auth login
    echo.
    if errorlevel 1 (
        echo [ERROR] Login failed!
        pause
        exit /b 1
    )
)

echo [OK] Already logged in to GitHub
echo.

REM Check if file exists
if not exist "dist\OCR-Invoice-Reader-Optimized-v1.2.tar.gz" (
    echo [ERROR] Release file not found!
    echo Expected: dist\OCR-Invoice-Reader-Optimized-v1.2.tar.gz
    echo.
    pause
    exit /b 1
)

echo [OK] Release file found (193 MB)
echo.

REM Check if tag already exists
"C:\Program Files\GitHub CLI\gh.exe" release view v1.2 --repo SyuuKasinn/ocr-invoice-reader-gui >nul 2>&1
if not errorlevel 1 (
    echo [WARNING] Release v1.2 already exists!
    echo.
    choice /C YN /M "Delete existing release and recreate"
    if errorlevel 2 goto :cancel
    if errorlevel 1 (
        echo Deleting existing release...
        "C:\Program Files\GitHub CLI\gh.exe" release delete v1.2 --repo SyuuKasinn/ocr-invoice-reader-gui --yes
        echo.
    )
)

echo [Step 2] Creating Release v1.2...
echo.
echo This will:
echo  - Create release tag v1.2
echo  - Upload 193MB file (takes 3-5 minutes)
echo  - Set as latest release
echo.

"C:\Program Files\GitHub CLI\gh.exe" release create v1.2 ^
  dist\OCR-Invoice-Reader-Optimized-v1.2.tar.gz ^
  --repo SyuuKasinn/ocr-invoice-reader-gui ^
  --title "v1.2 - Optimized Edition (5x Faster OCR)" ^
  --notes-file docs\releases\v1.2_notes.md ^
  --latest

if errorlevel 1 (
    echo.
    echo [ERROR] Release creation failed!
    echo.
    echo Possible issues:
    echo  1. Network connection problem
    echo  2. GitHub authentication expired
    echo  3. Tag v1.2 already exists
    echo.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   [SUCCESS] Release v1.2 Created!
echo ========================================
echo.
echo Release URL:
echo https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/tag/v1.2
echo.
echo Download URL:
echo https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/latest
echo.

"C:\Program Files\GitHub CLI\gh.exe" release view v1.2 --repo SyuuKasinn/ocr-invoice-reader-gui --web

pause
exit /b 0

:cancel
echo.
echo [CANCELLED] Upload cancelled
pause
exit /b 1
