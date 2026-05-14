# OCR Invoice Reader GUI

> Professional Apple-style desktop interface for [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-v4-orange)](https://github.com/PaddlePaddle/PaddleOCR)
[![Core Version](https://img.shields.io/badge/core-v2.4.0-brightgreen)](https://github.com/SyuuKasinn/ocr-invoice-reader)

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

```bash
python src/ocr_gui_apple_style.py
```

**That's it!** 🎉

---

## ✨ Features

### UI & UX
- ✅ **Apple-Style Design** - Clean, minimalist interface inspired by macOS
- ✅ **Drag & Drop** - Simply drag files onto the preview canvas
- ✅ **Split View** - 60% preview + 40% results panel
- ✅ **Real-time Visualization** - Live annotated images with detection boxes
- ✅ **Zoom Controls** - Zoom in/out and reset for detailed inspection

### Document Processing
- ✅ **Multi-Page PDF** - Page navigation with previous/next controls
- ✅ **Batch Processing** - Process all PDF pages at once
- ✅ **Smart Caching** - Page results are cached for instant switching
- ✅ **Auto-Reprocess** - Automatically updates when settings change
- ✅ **PDF Quality Control** - 144/216/288/300 DPI rendering options

### OCR Features
- ✅ **Enhanced Table Detection** - Automatic fallback for better table recognition
- ✅ **OCR Fallback** - Handles empty tables with direct OCR extraction
- ✅ **Multi-Language** - Chinese, English, Japanese, Korean
- ✅ **GPU Support** - Optional GPU acceleration
- ✅ **Text Processing** - Automatic word splitting and text enhancement

### Export & Results
- ✅ **Multiple Formats** - JSON, CSV, and Text export
- ✅ **Four View Tabs** - Summary, Regions, JSON, CSV
- ✅ **Structured Data** - Region type, bbox, confidence, text content
- ✅ **Batch CSV Export** - Combined CSV for all PDF pages

### System
- ✅ **Fast Startup** - Launches instantly
- ✅ **On-Demand Loading** - OCR engine loads on first use
- ✅ **Cross-Platform** - Windows, macOS, Linux
- ✅ **Latest Core** - Automatically benefits from ocr-invoice-reader v2.2.1+ improvements

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
│   └── ocr_gui_apple_style.py # Main GUI application (Apple-style)
├── docs/
│   ├── INSTALL.md             # Detailed installation guide
│   └── TROUBLESHOOTING.md     # Common issues and solutions
├── SYNC_v2.2.md               # Sync notes for v2.2.0
├── SYNC_v2.2.1.md             # Latest sync notes for v2.2.1+
├── PDF_DPI_FIX.md             # PDF quality/DPI fix documentation
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

## 📋 Latest Updates (2026-05-14)

### 🚨 Critical Bug Fix (v2.4.0)

**Language Parameter Bug Fixed** (Commit `1a0eb35`)
- ✅ Fixed hard-coded `lang='ch'` in structure analyzer (line 78)
- ✅ Language selection in GUI now works correctly
- ✅ **Significantly improved recognition for Japanese/English/Korean documents**
- ✅ No GUI code changes required - automatic fix

**Impact**: Users selecting non-Chinese languages will see dramatically better OCR results!

### Core Engine Improvements (v2.4.0)

1. **🚨 Language Bug Fix** (Critical)
   - GUI language selector now actually changes the OCR language
   - Japanese: `lang='japan'` now uses Japanese models ✅
   - English: `lang='en'` now uses English models ✅
   - Korean: `lang='korean'` now uses Korean models ✅

2. **🤖 LLM Integration** (CLI only, not in GUI)
   - Optional AI post-processing with Ollama
   - OCR text correction, field extraction, classification
   - Auto-setup command: `ocr-setup-ollama`
   - Enhanced CSV output for database import

3. **📚 Documentation** (10+ new guides)
   - Complete LLM integration guide
   - Auto-setup guide for Ollama
   - Quick reference and fixes
   - Code review reports

### Previous Updates (v2.3.0)

- 🚀 Smart GPU detection & auto-fallback
- 🖼️ Image optimizer (optional)
- 🐛 Unicode encoding fix
- ✅ Full verification (11 pages tested)

### GUI Features (v1.0.2)
- ✅ Apple-style interface with split-pane layout
- ✅ Multi-page PDF support with navigation
- ✅ Smart page caching system
- ✅ Auto-reprocessing on settings change
- ✅ CSV export alongside JSON
- ✅ PDF quality control (144-300 DPI)
- ✅ **Working language selection** (Bug fixed!)
- ✅ Automatic GPU detection

**See [SYNC_v2.4.0.md](SYNC_v2.4.0.md) for detailed update information.**

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
