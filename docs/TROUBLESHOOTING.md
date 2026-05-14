# Troubleshooting Guide

Common issues and solutions for OCR Invoice Reader GUI.

---

## Table of Contents

- [Installation Issues](#installation-issues)
- [Running Issues](#running-issues)
- [Performance Issues](#performance-issues)
- [Processing Issues](#processing-issues)
- [Platform-Specific](#platform-specific)

---

## Installation Issues

### ❌ `ModuleNotFoundError: No module named 'ocr_invoice_reader'`

**Cause:** OCR engine not installed.

**Solution:**
```bash
cd /path/to/ocr-invoice-reader
pip install -e .
```

**Verify:**
```bash
python -c "import ocr_invoice_reader; print('OK')"
```

---

### ❌ `'python' is not recognized`

**Cause:** Python not in PATH.

**Solutions:**

**Option 1:** Reinstall Python
- Check "Add Python to PATH" during installation

**Option 2:** Use full path
```bash
C:\Python310\python.exe src\ocr_gui_simple.py
```

**Option 3:** Add to PATH manually
1. Search "Environment Variables" in Windows
2. Edit PATH
3. Add Python installation directory

---

### ❌ `pip install` fails with permission error

**Solution:**
```bash
pip install --user -e .
```

---

### ❌ Slow installation in China

**Solution:** Use Chinese mirror
```bash
pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

---

## Running Issues

### ❌ GUI doesn't start

**Check 1:** Python version
```bash
python --version  # Should be 3.8+
```

**Check 2:** Dependencies installed
```bash
python -c "import tkinter; print('OK')"
```

**Check 3:** Run with console
```bash
python src/ocr_gui_simple.py
```
Look for error messages in console.

---

### ❌ GUI starts but crashes on processing

**Check 1:** Import test
```bash
python -c "from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer; print('OK')"
```

**Check 2:** Reinstall OCR engine
```bash
cd /path/to/ocr-invoice-reader
pip uninstall ocr-invoice-reader
pip install -e .
```

---

## Performance Issues

### ⏰ First processing very slow (10+ seconds)

**Normal!** This happens once:
1. PaddleOCR downloads models (~300MB)
2. OCR engine loads

**Subsequent processing:** 2-3 seconds ⚡

---

### ⏰ Every processing slow (10+ seconds)

**Cause:** Engine reloading each time.

**Solution:** Keep GUI open between files!
- File 1: 10s (loads engine)
- File 2: 3s ⚡ (reuses engine)
- File 3: 3s ⚡

---

### ⏰ Want faster processing

**Option 1:** GPU Acceleration
```bash
# Requires NVIDIA GPU + CUDA
pip uninstall paddlepaddle
pip install paddlepaddle-gpu==3.0.0
```
Check "Use GPU" in GUI.

**Option 2:** Batch processing
- Process multiple files in one session
- Engine loads once, reuses for all files

---

## Processing Issues

### ❌ "Failed to load OCR engine"

**Check Python console** for detailed error.

**Common causes:**

**1. Missing dependencies**
```bash
pip install paddleocr paddlepaddle opencv-python
```

**2. Corrupted installation**
```bash
pip uninstall paddleocr paddlepaddle
pip install paddleocr paddlepaddle
```

**3. Wrong Python version**
```bash
python --version  # Must be 3.8-3.10
```

---

### ❌ Results are empty or garbled

**Check 1:** Language setting
- Chinese text → Use "ch"
- English text → Use "en"
- Japanese text → Use "japan"

**Check 2:** Image quality
- Image too blurry
- Resolution too low
- Try higher quality scan

**Check 3:** File format
- Supported: PDF, JPG, PNG
- Try converting to different format

---

### ❌ PDF processing fails

**Check 1:** PDF not corrupted
```bash
# Try opening in PDF reader
```

**Check 2:** PDF has text layer
- Some PDFs are already OCR'd
- This tool works best on scanned documents

**Check 3:** Multi-page PDF
- Tool processes all pages
- May take longer for large PDFs

---

## Platform-Specific

### Windows

#### ❌ Antivirus blocks Python

**Solution:**
1. Add Python to antivirus exceptions
2. Or use different antivirus

#### ❌ Long path issues

**Solution:** Use shorter path
```bash
# BAD: C:\Users\Username\Very\Long\Path\To\Project
# GOOD: C:\Projects\ocr-gui
```

---

### macOS

#### ❌ "python" not found, but "python3" works

**Solution:** Use `python3`
```bash
python3 src/ocr_gui_simple.py
```

#### ❌ tkinter not installed

**Solution:**
```bash
brew install python-tk@3.10
```

---

### Linux

#### ❌ tkinter not found

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora/RHEL:**
```bash
sudo dnf install python3-tkinter
```

#### ❌ OpenCV issues

**Solution:**
```bash
sudo apt-get install libgl1-mesa-glx
```

---

## Network Issues

### ❌ Cannot download PaddleOCR models

**Check 1:** Internet connection
```bash
ping baidu.com  # or google.com
```

**Check 2:** Proxy settings
If behind corporate proxy, configure:
```bash
set HTTP_PROXY=http://proxy:port
set HTTPS_PROXY=http://proxy:port
```

**Check 3:** Use alternative mirror
```bash
# Edit ~/.paddleocr/config.json
# Change model download URL
```

---

## Debug Mode

### Enable detailed logging

**Edit `ocr_gui_simple.py`:**

Change:
```python
# At top of file
import logging
logging.basicConfig(level=logging.DEBUG)
```

Run again and check console output.

---

## Still Having Issues?

### Gather Information

1. **Python version:**
   ```bash
   python --version
   ```

2. **Installed packages:**
   ```bash
   pip list | grep -E "(paddle|ocr)"
   ```

3. **Error message:**
   - Full error from console
   - Screenshot if needed

4. **System info:**
   - OS version
   - RAM amount
   - GPU (if using)

### Report Issue

Create issue at: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues

Include:
- Error message
- Steps to reproduce
- System information
- What you've tried

---

## Common Error Messages

### "FileNotFoundError: Cython/Utility/CppSupport.cpp"

**This is expected in .exe!**

We don't provide .exe because PaddleOCR cannot be packaged.

**Solution:** Run from source (this guide).

---

### "CUDA not available"

**Not an error!** Just means GPU not available.

App works fine with CPU. To use GPU:
```bash
pip install paddlepaddle-gpu==3.0.0
```

---

### "Model download failed"

**Cause:** Network timeout.

**Solution:**
1. Check internet connection
2. Try again (resume download)
3. Use mirror site (see Network Issues)

---

## FAQ

**Q: Do I need to install anything else?**

A: No. Just Python 3.8+ and ocr-invoice-reader.

**Q: Can I run offline?**

A: Yes, after first run (models downloaded).

**Q: Does it work on Python 3.11?**

A: Use Python 3.8-3.10 for best compatibility.

**Q: Why no .exe file?**

A: PaddleOCR cannot be packaged by PyInstaller (Cython issue).

---

## Resources

- [Installation Guide](INSTALL.md)
- [Main README](../README.md)
- [OCR Engine](https://github.com/SyuuKasinn/ocr-invoice-reader)
- [Issue Tracker](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues)
