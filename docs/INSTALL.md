# Installation Guide

Complete step-by-step guide for setting up OCR Invoice Reader GUI.

---

## Table of Contents

- [Quick Install](#quick-install)
- [Detailed Install](#detailed-install)
- [First-Time Setup](#first-time-setup)
- [Verification](#verification)
- [Next Steps](#next-steps)

---

## Quick Install

For users who already have Python installed:

```bash
# 1. Install OCR engine
git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git
cd ocr-invoice-reader
pip install -e .

# 2. Clone GUI
cd ..
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# 3. Run
python src/ocr_gui_simple.py
```

Done! ✅

---

## Detailed Install

### Step 1: Install Python

**Check if Python is installed:**
```bash
python --version
```

If you see `Python 3.8` or higher, skip to Step 2.

**Install Python:**

1. Download from https://www.python.org/downloads/
2. **Important**: Check "Add Python to PATH" during installation
3. Verify:
   ```bash
   python --version
   pip --version
   ```

### Step 2: Install OCR Engine

```bash
# Clone the repository
git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Navigate to directory
cd ocr-invoice-reader

# Install in editable mode
pip install -e .
```

This installs:
- PaddleOCR 2.8.1+
- PaddlePaddle 3.0.0+
- PyMuPDF, OpenCV, Pydantic, etc.

**Installation time:** 2-5 minutes (depending on internet speed)

### Step 3: Clone GUI Repository

```bash
# Go back to parent directory
cd ..

# Clone GUI repository
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git

# Navigate to GUI directory
cd ocr-invoice-reader-gui
```

### Step 4: Verify Installation

```bash
# Test import
python -c "from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer; print('OK')"
```

If you see `OK`, installation successful! ✅

---

## First-Time Setup

### First Launch

```bash
python src/ocr_gui_simple.py
```

GUI should open in ~1 second.

### First Processing

When you process your first document:
1. **Model Download** - PaddleOCR downloads models (~300MB)
2. **Engine Load** - OCR engine initializes (~10 seconds)
3. **Processing** - Document is analyzed

**Note:** This only happens once. Subsequent files process in 2-3 seconds!

---

## Verification

### Test the Installation

1. **Start GUI:**
   ```bash
   python src/ocr_gui_simple.py
   ```

2. **Process a test file:**
   - Click "Browse..."
   - Select any PDF or image
   - Click "Process Document"

3. **Check results:**
   - Results should appear in text area
   - No error messages

### Expected Performance

| Operation | Time |
|-----------|------|
| GUI Launch | 1 second |
| First OCR | 10-15 seconds |
| Subsequent OCR | 2-3 seconds |

---

## Next Steps

### Create Desktop Shortcut (Windows)

1. Right-click `run_gui.bat`
2. Click "Create shortcut"
3. Move shortcut to Desktop

### Enable GPU Acceleration (Optional)

If you have NVIDIA GPU:

```bash
# Uninstall CPU version
pip uninstall paddlepaddle

# Install GPU version
pip install paddlepaddle-gpu==3.0.0
```

**Requirements:**
- NVIDIA GPU
- CUDA 11.8 or 12.0

### Using Chinese Mirror (Faster in China)

```bash
pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## Alternative: Manual Download

If you can't use Git:

1. **Download OCR Engine:**
   - Go to https://github.com/SyuuKasinn/ocr-invoice-reader
   - Click "Code" → "Download ZIP"
   - Extract to a folder

2. **Install OCR Engine:**
   ```bash
   cd path/to/extracted/ocr-invoice-reader
   pip install -e .
   ```

3. **Download GUI:**
   - Go to https://github.com/SyuuKasinn/ocr-invoice-reader-gui
   - Click "Code" → "Download ZIP"
   - Extract to a folder

4. **Run:**
   ```bash
   cd path/to/extracted/ocr-invoice-reader-gui
   python src/ocr_gui_simple.py
   ```

---

## Troubleshooting

### Issue: `pip` not found

**Solution:**
```bash
python -m pip install -e .
```

### Issue: Permission denied

**Solution:**
```bash
pip install --user -e .
```

### Issue: Module not found

**Solution:**
```bash
# Verify ocr-invoice-reader is installed
pip list | grep ocr-invoice-reader

# If not found, reinstall
cd /path/to/ocr-invoice-reader
pip install -e .
```

### More Issues?

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## Uninstallation

```bash
# Uninstall OCR engine
pip uninstall ocr-invoice-reader

# Uninstall dependencies (optional)
pip uninstall paddleocr paddlepaddle opencv-python pymupdf

# Delete directories
rm -rf ocr-invoice-reader ocr-invoice-reader-gui
```

---

## Support

- **Documentation**: [README.md](../README.md)
- **Issues**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
- **OCR Engine**: https://github.com/SyuuKasinn/ocr-invoice-reader
