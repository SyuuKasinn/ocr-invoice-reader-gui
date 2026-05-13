#!/bin/bash
# Quick launch script for OCR Invoice Reader GUI
# Linux/macOS shell script

echo "Starting OCR Invoice Reader GUI..."
echo ""

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed or not in PATH"
    echo "Please install Python 3.8 or higher"
    exit 1
fi

# Run the GUI
python3 ocr_gui.py
