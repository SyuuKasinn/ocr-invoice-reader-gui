# Building Standalone EXE Guide

This guide explains how to create a standalone executable for Windows.

## 🚨 Important Note

The GUI application requires the OCR engine to function. There are two approaches:

### Approach 1: GUI Only (Recommended for Distribution)

Build the GUI as an exe, but require users to install the OCR engine separately.

**Advantages:**
- Smaller exe size (~50MB)
- Easier to update OCR engine
- Users can install via pip

**Disadvantages:**
- Requires Python on target machine
- Users must run: `pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git`

### Approach 2: All-in-One Portable (Complex)

Package everything including PaddleOCR and models.

**Advantages:**
- Completely standalone
- No Python needed
- True portable app

**Disadvantages:**
- VERY large (~500MB-1GB with models)
- Complex build process
- Slower startup (model loading)

---

## 📦 Quick Build (Approach 1)

### Prerequisites

1. **Install dependencies:**
   ```bash
   pip install pyinstaller tkinterdnd2 Pillow
   ```

2. **Ensure OCR engine is installed:**
   ```bash
   pip install -e ../ocr-invoice-reader
   ```

### Build Steps

#### Option A: Automatic Build (Recommended)

Simply run:
```bash
build_exe.bat
```

This will:
1. Check dependencies
2. Clean previous builds
3. Build the executable
4. Show the result

#### Option B: Manual Build

```bash
# Clean previous builds
rmdir /s /q build dist

# Build with spec file
pyinstaller --clean ocr_gui.spec

# Result will be in dist/OCR-Invoice-Reader-GUI.exe
```

### Output

After building, you'll find:
```
dist/
└── OCR-Invoice-Reader-GUI.exe  (~50-80 MB)
```

---

## 🚀 Distribution

### Package for Distribution

Create a distribution package:

```
OCR-Invoice-Reader-GUI-v1.0/
├── OCR-Invoice-Reader-GUI.exe    # Main executable
├── README.txt                     # Installation instructions
└── sample-invoice.jpg             # Example file
```

### README.txt for Distribution

```
OCR Invoice Reader GUI v1.0
============================

INSTALLATION:

1. Install Python 3.8 or higher from https://www.python.org/

2. Install OCR Engine:
   Open Command Prompt and run:
   
   pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

3. Run OCR-Invoice-Reader-GUI.exe

USAGE:

1. Launch OCR-Invoice-Reader-GUI.exe
2. Drag and drop an invoice or waybill PDF/image
3. Click "Process Document"
4. View results in tabs

SYSTEM REQUIREMENTS:

- Windows 10/11 (64-bit)
- 4GB RAM minimum
- Internet connection for first-time model download

SUPPORT:

GitHub: https://github.com/SyuuKasinn/ocr-invoice-reader-gui
Issues: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
```

---

## 🔧 Advanced: All-in-One Build

For a truly portable version (no Python required), use this spec:

### Step 1: Install All Dependencies Locally

```bash
pip install paddlepaddle paddleocr opencv-python-headless
```

### Step 2: Modified Spec File

Create `ocr_gui_portable.spec`:

```python
# -*- mode: python ; coding: utf-8 -*-
import os
import sys

# Get OCR package location
import ocr_invoice_reader
ocr_path = os.path.dirname(ocr_invoice_reader.__file__)

a = Analysis(
    ['ocr_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('demo', 'demo'),
        # Include OCR engine
        (ocr_path, 'ocr_invoice_reader'),
        # Include PaddleOCR
        (os.path.join(sys.prefix, 'Lib', 'site-packages', 'paddleocr'), 'paddleocr'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinterdnd2',
        'PIL',
        'ocr_invoice_reader',
        'paddleocr',
        'paddle',
        'cv2',
    ],
    # ... rest of spec
)
```

### Step 3: Build

```bash
pyinstaller --clean ocr_gui_portable.spec
```

**Warning:** This creates a VERY large exe (~500MB-1GB)!

---

## 🐛 Troubleshooting

### Issue: "Module not found" error

**Solution:** Add the missing module to `hiddenimports` in the spec file.

### Issue: Exe is too large

**Solutions:**
1. Exclude unnecessary packages in spec file
2. Use UPX compression (already enabled)
3. Remove demo files from datas

### Issue: "OCR command not found"

**Solution:** This is expected in Approach 1. User must install OCR engine:
```bash
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git
```

### Issue: Slow startup

**Solution:** This is normal for first run. PaddleOCR downloads models (~200MB) on first use.

---

## 📊 Build Size Comparison

| Approach | Size | Python Required | OCR Included |
|----------|------|----------------|--------------|
| GUI Only | ~50MB | Yes (with pip) | No |
| Portable | ~500MB-1GB | No | Yes |
| Installer | ~100MB | Installs Python | Yes |

---

## 🎯 Recommended Distribution Method

**For End Users:**
1. Build GUI exe (Approach 1)
2. Create installer with Inno Setup or NSIS
3. Installer includes:
   - GUI exe
   - Python installer (if needed)
   - OCR engine installation script
   - Desktop shortcut

**For Developers:**
- Just share the GitHub repo
- Users can run: `python ocr_gui.py`

---

## 📝 Testing Checklist

Before distributing:

- [ ] Test on clean Windows machine
- [ ] Verify OCR engine installation works
- [ ] Test with sample invoice
- [ ] Check all tabs display correctly
- [ ] Verify error messages are clear
- [ ] Test without Python installed (if portable)

---

## 🔄 Update Process

When releasing updates:

1. Update version in `ocr_gui.py`
2. Rebuild exe: `build_exe.bat`
3. Test thoroughly
4. Create GitHub release
5. Upload exe to releases

---

## 🆘 Support

For build issues:
- Check PyInstaller docs: https://pyinstaller.org/
- Open issue: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues

For OCR issues:
- Check main repo: https://github.com/SyuuKasinn/ocr-invoice-reader
