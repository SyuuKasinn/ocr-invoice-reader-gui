# OCR Invoice Reader GUI

> Simple, reliable graphical interface for [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-v4-orange)](https://github.com/PaddlePaddle/PaddleOCR)

---

## 🚀 Quick Start

### Prerequisites

1. **Install ocr-invoice-reader first:**
   ```bash
   git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git
   cd ocr-invoice-reader
   pip install -e .
   ```

2. **Clone this repository:**
   ```bash
   git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
   cd ocr-invoice-reader-gui
   ```

### Run the GUI

**Option 1: Double-click**
```
run_gui.bat  (Windows)
```

**Option 2: Command line**
```bash
python src/ocr_gui_simple.py
```

**That's it!** 🎉

---

## ✨ Features

- ✅ **Drag & Drop** - Simply drag files onto the window
- ✅ **Simple & Reliable** - Clean, maintainable code
- ✅ **Fast Startup** - Launches in ~1 second
- ✅ **On-Demand Loading** - OCR engine loads on first use
- ✅ **Image Visualization** - Annotated images with detection boxes
- ✅ **Multi-Language** - Chinese, English, Japanese, Korean
- ✅ **GPU Support** - Optional GPU acceleration
- ✅ **Cross-Platform** - Windows, macOS, Linux

---

## 📊 Performance

| Operation | Time |
|-----------|------|
| GUI Startup | **~1 second** ⚡ |
| First OCR (load engine) | ~10 seconds |
| Subsequent OCR | **2-3 seconds** ⚡⚡⚡ |

**Tip:** Keep GUI open when processing multiple files - 2nd file onwards takes only 2-3 seconds!

---

## 📖 Usage

### Step 1: Select File
**Option A:** Drag and drop a file onto the drop zone  
**Option B:** Click the drop zone or "Browse..." button to select a file

Supported formats: PDF, JPG, JPEG, PNG

### Step 2: Configure Settings
- **Language**: Choose ch/en/japan/korean
- **GPU**: Check if you have NVIDIA GPU

### Step 3: Process
Click **"Process Document"** and view results in the text area.

### Step 4: View Visualization
After processing, an annotated image is saved showing:
- **OCR text boxes** (red) - Individual text detections
- **Region boxes** (colored by type) - Table, text, title regions
- **Confidence scores** - Detection confidence for each region

The visualization file location is shown in the results.

### First-Time Setup
- **First run**: PaddleOCR downloads models (~300MB, one-time)
- **First processing**: OCR engine loads (~10 seconds)
- **Subsequent**: Fast processing (2-3 seconds) ⚡

---

## 📁 Project Structure

```
ocr-invoice-reader-gui/
├── src/
│   └── ocr_gui_simple.py      # Main GUI application (recommended)
├── docs/
│   ├── INSTALL.md             # Detailed installation guide
│   └── TROUBLESHOOTING.md     # Common issues and solutions
├── run_gui.bat                # Quick launch script (Windows)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🔧 System Requirements

- **OS**: Windows 7+, macOS, Linux
- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Disk**: 1GB for models
- **Internet**: First run only (download models)

---

## ⚠️ Important Notes

### No Standalone Executable

**We do not provide .exe files.**

**Reason:** PaddleOCR uses Cython, which cannot be correctly packaged by PyInstaller. This is a known compatibility issue.

**Solution:** Run from source code (simple, fast, reliable).

See [docs/INSTALL.md](docs/INSTALL.md) for detailed instructions.

---

## 💡 Tips & Tricks

### Batch Processing
Keep the GUI open and process files one by one:
```
File 1: 10s  (loads engine)
File 2: 3s   ⚡
File 3: 3s   ⚡
File 4: 3s   ⚡
```

### GPU Acceleration
If you have NVIDIA GPU:
```bash
# Install GPU version
pip install paddlepaddle-gpu==3.0.0

# Check "Use GPU" in GUI
# 3-10x faster! ⚡⚡⚡
```

### Offline Usage
After first run (models downloaded), works completely offline.

---

## 🐛 Troubleshooting

### Module Not Found
```bash
cd /path/to/ocr-invoice-reader
pip install -e .
```

### Python Not Found
Reinstall Python with "Add to PATH" checked.

### Slow Processing
- First processing always slower (loads engine)
- Keep GUI open for subsequent files
- Consider GPU acceleration

### More Issues?
See [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## 📚 Documentation

- [Installation Guide](docs/INSTALL.md) - Complete setup instructions
- [Troubleshooting](docs/TROUBLESHOOTING.md) - Common problems
- [OCR Engine Docs](https://github.com/SyuuKasinn/ocr-invoice-reader) - Backend API

---

## 🆚 Version Comparison

| File | Status | Lines | Description |
|------|--------|-------|-------------|
| `ocr_gui_simple.py` | ✅ **Recommended** | 200 | Clean, simple, reliable |
| `ocr_gui_modern.py` | ❌ Deprecated | 1000+ | Complex, unmaintained |
| `ocr_gui_optimized.py` | ❌ Deprecated | 600+ | Obsolete |
| `ocr_gui.py` | ❌ Deprecated | 550+ | Original, outdated |

**Use `ocr_gui_simple.py`** - it's the only maintained version.

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 🙏 Acknowledgments

- [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader) - Core OCR engine
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR models and framework
- [PaddlePaddle](https://github.com/PaddlePaddle/Paddle) - Deep learning platform

---

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **OCR Engine**: https://github.com/SyuuKasinn/ocr-invoice-reader
- **Issues**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
- **PaddleOCR**: https://github.com/PaddlePaddle/PaddleOCR

---

**Run from source - simple and reliable!** 🚀
