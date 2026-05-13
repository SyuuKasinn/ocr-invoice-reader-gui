# Quick Demo Recording Setup Script
# This script helps set up for recording the demo GIF

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   OCR Invoice Reader GUI - Demo Setup" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if ScreenToGif is installed
Write-Host "[1/5] Checking for ScreenToGif..." -ForegroundColor Yellow

$screenToGifPath = "C:\Program Files\ScreenToGif\ScreenToGif.exe"
$screenToGifInstalled = Test-Path $screenToGifPath

if ($screenToGifInstalled) {
    Write-Host "  ✓ ScreenToGif found!" -ForegroundColor Green
} else {
    Write-Host "  ✗ ScreenToGif not found" -ForegroundColor Red
    Write-Host "  Installing ScreenToGif via winget..." -ForegroundColor Yellow

    try {
        winget install NickeManarin.ScreenToGif
        Write-Host "  ✓ ScreenToGif installed!" -ForegroundColor Green
    } catch {
        Write-Host "  ✗ Failed to install. Please download from:" -ForegroundColor Red
        Write-Host "    https://www.screentogif.com/" -ForegroundColor White
    }
}

Write-Host ""

# Check if demo folder exists
Write-Host "[2/5] Checking demo folder..." -ForegroundColor Yellow
if (Test-Path "demo") {
    Write-Host "  ✓ Demo folder exists" -ForegroundColor Green
} else {
    New-Item -ItemType Directory -Path "demo" | Out-Null
    Write-Host "  ✓ Demo folder created" -ForegroundColor Green
}

Write-Host ""

# Check if sample file exists
Write-Host "[3/5] Checking for sample file..." -ForegroundColor Yellow
$sampleFile = "..\ocr-invoice-reader\examples\142816_structure.jpg"
if (Test-Path $sampleFile) {
    Write-Host "  ✓ Sample file found: $sampleFile" -ForegroundColor Green
} else {
    Write-Host "  ! No sample file found" -ForegroundColor Yellow
    Write-Host "    Please prepare a sample invoice/waybill to drag" -ForegroundColor White
}

Write-Host ""

# Check if GUI can run
Write-Host "[4/5] Checking GUI dependencies..." -ForegroundColor Yellow
try {
    python -c "import tkinter; import PIL; print('OK')" 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "  ✓ GUI dependencies OK" -ForegroundColor Green
    } else {
        Write-Host "  ✗ Missing dependencies" -ForegroundColor Red
        Write-Host "    Run: pip install -r requirements.txt" -ForegroundColor White
    }
} catch {
    Write-Host "  ✗ Python not found" -ForegroundColor Red
}

Write-Host ""

# Recording instructions
Write-Host "[5/5] Recording Instructions:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  📋 Quick Recording Steps:" -ForegroundColor Cyan
Write-Host "  -------------------------" -ForegroundColor Cyan
Write-Host "  1. Launch ScreenToGif (will open automatically)" -ForegroundColor White
Write-Host "  2. Launch the GUI (run: python ocr_gui.py)" -ForegroundColor White
Write-Host "  3. Position ScreenToGif recorder over GUI window" -ForegroundColor White
Write-Host "  4. Press F7 to start recording" -ForegroundColor White
Write-Host "  5. Perform these actions (~15 seconds):" -ForegroundColor White
Write-Host "     a. Show empty GUI (2s)" -ForegroundColor Gray
Write-Host "     b. Drag sample file into drop zone (3s)" -ForegroundColor Gray
Write-Host "     c. Click 'Process Document' (1s)" -ForegroundColor Gray
Write-Host "     d. Wait for progress (3s)" -ForegroundColor Gray
Write-Host "     e. Click through result tabs (6s)" -ForegroundColor Gray
Write-Host "  6. Press F8 to stop recording" -ForegroundColor White
Write-Host "  7. Save as demo/demo.gif" -ForegroundColor White
Write-Host ""
Write-Host "  🎯 Tips:" -ForegroundColor Cyan
Write-Host "  --------" -ForegroundColor Cyan
Write-Host "  • Set frame rate to 12-15 FPS" -ForegroundColor White
Write-Host "  • Keep file size under 3MB" -ForegroundColor White
Write-Host "  • Pause 1-2s on each result tab" -ForegroundColor White
Write-Host "  • Move mouse smoothly" -ForegroundColor White
Write-Host ""

# Offer to launch tools
Write-Host "Ready to record?" -ForegroundColor Green
Write-Host ""
Write-Host "[A] Launch ScreenToGif" -ForegroundColor Yellow
Write-Host "[B] Launch GUI (python ocr_gui.py)" -ForegroundColor Yellow
Write-Host "[C] Both" -ForegroundColor Yellow
Write-Host "[Q] Quit" -ForegroundColor Yellow
Write-Host ""

$choice = Read-Host "Your choice (A/B/C/Q)"

switch ($choice.ToUpper()) {
    "A" {
        if ($screenToGifInstalled) {
            Start-Process $screenToGifPath
            Write-Host "✓ ScreenToGif launched!" -ForegroundColor Green
        } else {
            Write-Host "✗ ScreenToGif not found" -ForegroundColor Red
        }
    }
    "B" {
        Write-Host "Launching GUI..." -ForegroundColor Yellow
        python ocr_gui.py
    }
    "C" {
        if ($screenToGifInstalled) {
            Start-Process $screenToGifPath
            Write-Host "✓ ScreenToGif launched!" -ForegroundColor Green
        }
        Start-Sleep -Seconds 2
        Write-Host "Launching GUI..." -ForegroundColor Yellow
        python ocr_gui.py
    }
    "Q" {
        Write-Host "Exiting..." -ForegroundColor Gray
        exit
    }
    default {
        Write-Host "Invalid choice. Exiting..." -ForegroundColor Red
        exit
    }
}

Write-Host ""
Write-Host "See RECORDING_GUIDE.md for detailed instructions" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
