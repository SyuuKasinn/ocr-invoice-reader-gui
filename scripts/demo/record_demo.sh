#!/bin/bash
# Quick Demo Recording Setup Script
# This script helps set up for recording the demo GIF

echo "========================================"
echo "   OCR Invoice Reader GUI - Demo Setup"
echo "========================================"
echo ""

# Check if recording tools are available
echo "[1/5] Checking for recording tools..."

if command -v peek &> /dev/null; then
    echo "  ✓ Peek found (recommended for Linux)"
    RECORDER="peek"
elif command -v kap &> /dev/null; then
    echo "  ✓ Kap found (recommended for macOS)"
    RECORDER="kap"
elif command -v byzanz-record &> /dev/null; then
    echo "  ✓ Byzanz found"
    RECORDER="byzanz"
else
    echo "  ✗ No recording tool found"
    echo ""
    echo "  Install a recording tool:"
    echo "  Ubuntu/Debian: sudo apt install peek"
    echo "  Fedora:        sudo dnf install peek"
    echo "  macOS:         brew install --cask kap"
    echo "  Arch:          sudo pacman -S peek"
    RECORDER="none"
fi

echo ""

# Check if demo folder exists
echo "[2/5] Checking demo folder..."
if [ -d "demo" ]; then
    echo "  ✓ Demo folder exists"
else
    mkdir -p demo
    echo "  ✓ Demo folder created"
fi

echo ""

# Check if sample file exists
echo "[3/5] Checking for sample file..."
SAMPLE="../ocr-invoice-reader/examples/142816_structure.jpg"
if [ -f "$SAMPLE" ]; then
    echo "  ✓ Sample file found: $SAMPLE"
else
    echo "  ! No sample file found"
    echo "    Please prepare a sample invoice/waybill to drag"
fi

echo ""

# Check if GUI can run
echo "[4/5] Checking GUI dependencies..."
if python3 -c "import tkinter; import PIL" 2>/dev/null; then
    echo "  ✓ GUI dependencies OK"
else
    echo "  ✗ Missing dependencies"
    echo "    Run: pip3 install -r requirements.txt"
fi

echo ""

# Recording instructions
echo "[5/5] Recording Instructions:"
echo ""
echo "  📋 Quick Recording Steps:"
echo "  -------------------------"
echo "  1. Launch recording tool ($RECORDER)"
echo "  2. Launch the GUI (run: python3 ocr_gui.py)"
echo "  3. Position recorder over GUI window"
echo "  4. Start recording"
echo "  5. Perform these actions (~15 seconds):"
echo "     a. Show empty GUI (2s)"
echo "     b. Drag sample file into drop zone (3s)"
echo "     c. Click 'Process Document' (1s)"
echo "     d. Wait for progress (3s)"
echo "     e. Click through result tabs (6s)"
echo "  6. Stop recording"
echo "  7. Save as demo/demo.gif"
echo ""
echo "  🎯 Tips:"
echo "  --------"
echo "  • Set frame rate to 12-15 FPS"
echo "  • Keep file size under 3MB"
echo "  • Pause 1-2s on each result tab"
echo "  • Move mouse smoothly"
echo ""

# Offer to launch tools
if [ "$RECORDER" != "none" ]; then
    echo "Ready to record?"
    echo ""
    echo "[A] Launch $RECORDER"
    echo "[B] Launch GUI (python3 ocr_gui.py)"
    echo "[C] Both"
    echo "[Q] Quit"
    echo ""
    read -p "Your choice (A/B/C/Q): " choice

    case ${choice^^} in
        A)
            echo "Launching $RECORDER..."
            $RECORDER &
            ;;
        B)
            echo "Launching GUI..."
            python3 ocr_gui.py
            ;;
        C)
            echo "Launching $RECORDER..."
            $RECORDER &
            sleep 2
            echo "Launching GUI..."
            python3 ocr_gui.py
            ;;
        Q)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Exiting..."
            exit 1
            ;;
    esac
fi

echo ""
echo "See RECORDING_GUIDE.md for detailed instructions"
echo "========================================"
