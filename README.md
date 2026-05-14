# OCR Invoice Reader GUI

**Drag-and-Drop Desktop Application for Invoice OCR Processing**

A user-friendly graphical interface for [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader) with **5x faster** OCR performance!

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Performance](https://img.shields.io/badge/performance-5x%20faster-brightgreen)](docs/guides/performance-optimization.md)

## ⚡ v1.2 - Optimized Edition!

**Latest Release:** OCR recognition now **5x faster** from 2nd scan onward!

- 🚀 **Startup:** 5s → 2s (2.5x faster)
- ⚡ **OCR Recognition:** 15s → 3s (5x faster, 2nd time onward)
- 💡 **Pre-loaded Engine:** Load model once, reuse forever
- 📚 **Complete Docs:** README.txt, VERSION.txt included

[See what's new in v1.2 →](docs/releases/v1.2_notes.md) | [Test Report →](docs/releases/v1.2-test-report.md)

---

## ✨ Features

### Core Features
- 🎯 **Drag & Drop Interface** - Simply drag PDF or image files
- 📊 **Real-time Visualization** - See OCR detection with color-coded regions
- 🌍 **Multi-language Support** - Chinese, English, Japanese, Korean
- 🔄 **Multiple OCR Modes** - Simple, Raw, Extract, Enhanced
- 📋 **Rich Output Formats** - JSON, Text, Tables (HTML)

### Performance Features (v1.2)
- ⚡ **5x Faster OCR** - Pre-loaded model, no repeated initialization
- 🚀 **Fast Startup** - Directory packaging, no extraction needed
- 💫 **Splash Screen** - Visual loading progress
- 🎮 **GPU Support** - Optional GPU acceleration
- 📚 **Complete Documentation** - User guides and troubleshooting included

---

## 📥 Download

### Windows Executable (Recommended)

**Latest Release:** v1.2 - Optimized Edition ⚡

[📦 Download OCR-Invoice-Reader-Optimized-v1.2.tar.gz](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/latest) (193MB)

**What's included:**
- ✅ Standalone executable (no Python required)
- ✅ All dependencies bundled
- ✅ Sample files
- ✅ Complete documentation

**System Requirements:**
- Windows 7 or higher
- 4GB RAM minimum (8GB+ recommended)
- 1GB disk space
- Internet connection (first run only, to download OCR model)

### Python Source

```bash
# Clone repository
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Install dependencies
pip install -r requirements.txt

# Run optimized version
python src/ocr_gui_optimized.py

# Or run original version
python src/ocr_gui.py
```

---

## 🚀 Quick Start

### From Executable

1. Extract `OCR-Invoice-Reader-v1.1.tar.gz`
2. Double-click `OCR-Invoice-Reader-Optimized.exe`
3. Wait for splash screen (first run: ~10s)
4. Drag & drop a PDF or image file
5. Click "Process Document"
6. View results in tabs

### From Source

```bash
# Install dependencies
pip install tkinterdnd2 Pillow paddleocr opencv-python

# Run optimized version (faster)
python src/ocr_gui_optimized.py

# Or run original version
python src/ocr_gui.py
```

**First Run Note:** PaddleOCR will download model files (~300MB) automatically. This happens once and is cached locally.

---

## 📊 Performance Comparison

| Scenario | Original | Optimized (v1.1) | Improvement |
|----------|----------|------------------|-------------|
| App Startup | 5 seconds | 2 seconds | **2.5x faster** ⚡ |
| First OCR | 15 seconds | 15 seconds | Same |
| 2nd OCR | 15 seconds | **3 seconds** | **5x faster** ⚡⚡⚡ |
| 10 files batch | 150 seconds | **42 seconds** | **3.6x faster** ⚡⚡ |

**Key Improvement:** Pre-loaded OCR engine - model loads once at startup, subsequent scans reuse the loaded model.

---

## 🎯 Usage Guide

### Supported Formats
- **PDF** (.pdf) - Multi-page supported
- **Images** (.jpg, .jpeg, .png)

### OCR Modes
| Mode | Speed | Accuracy | Use Case |
|------|-------|----------|----------|
| `ocr-simple` | ⚡⚡⚡ Fastest | Medium | Quick preview |
| `ocr-raw` | ⚡⚡ Fast | Good | Simple documents |
| `ocr-extract` | ⚡ Medium | High | Invoices (recommended) |
| `ocr-enhanced` | 🐌 Slow | Highest | High-quality needs |

### Languages
- 🇨🇳 Chinese (`ch`)
- 🇺🇸 English (`en`)
- 🇯🇵 Japanese (`japan`)
- 🇰🇷 Korean (`korean`)

### Output Tabs
- 📊 **Visualization** - Annotated image with bounding boxes
- 📋 **JSON Data** - Structured OCR results
- 📝 **Extracted Text** - Plain text output
- 🔢 **Tables** - HTML table data

---

## 💡 Tips & Tricks

### Speed Optimization

**1. Process Multiple Files**
```
Don't close the app! Process files continuously:
- File 1: 15s (model loads)
- File 2: 3s  ⚡ (5x faster!)
- File 3: 3s  ⚡
```

**2. Choose Right Mode**
```
Quick check → ocr-simple (1-2s)
Daily use   → ocr-extract (3-5s)
High quality → ocr-enhanced (5-8s)
```

**3. Enable GPU (Optional)**
```
☑ Check "Use GPU (if available)"
Requirements: NVIDIA GPU + CUDA
Result: 3s → 1.5s (2x faster!)
```

---

## 📁 Project Structure

```
ocr-invoice-reader-gui/
├── README.md                 # This file
├── LICENSE                   # MIT License
├── requirements.txt          # Python dependencies
│
├── src/                      # Source code
│   ├── ocr_gui.py           # Original GUI
│   ├── ocr_gui_optimized.py # Optimized GUI (v1.1)
│   └── common/              # Shared components
│
├── build/                    # Build configuration
│   ├── specs/               # PyInstaller configs
│   └── build.bat            # Build script
│
├── docs/                     # Documentation
│   ├── guides/              # User guides
│   ├── development/         # Dev docs
│   └── releases/            # Release notes
│
├── scripts/                  # Utility scripts
│   ├── run.bat              # Quick run script
│   ├── demo/                # Demo scripts
│   └── utils/               # Utility tools
│
├── demo/                     # Sample files
├── tests/                    # Test files
└── archive/                  # Old versions
```

---

## 🛠️ Development

### Building from Source

```bash
# Install build dependencies
pip install pyinstaller

# Build optimized version (faster)
cd build
./build.bat

# Or build original version
pyinstaller specs/ocr_gui.spec

# Or build simple version (smallest)
pyinstaller specs/ocr_gui_simple.spec
```

See [Build Guide](docs/development/building.md) for details.

### Running Tests

```bash
# Performance test
python tests/test_optimized.py

# Run all tests
pytest tests/
```

### Project Documentation

- [Installation Guide](docs/guides/installation.md)
- [Quick Start](docs/guides/quick-start.txt)
- [Performance Tips](docs/guides/performance-optimization.md)
- [Building Guide](docs/development/building.md)
- [Packaging Guide](docs/development/packaging.md)

---

## 🔧 Troubleshooting

### First Run is Slow
**Normal!** First run downloads PaddleOCR models (~300MB). After download, models are cached at `%USERPROFILE%\.paddleocr\`.

### Antivirus Warning
**False positive.** PyInstaller executables may trigger warnings. Add to whitelist or build from source.

### OCR Recognition Fails
- Check "Use GPU" is unchecked if you don't have NVIDIA GPU
- Ensure internet connection on first run (for model download)
- Try different OCR mode

### Still Slow After v1.1 Update
- Make sure you're using `ocr_gui_optimized.py` or the v1.1 exe
- First recognition is always slow (model loading)
- 2nd recognition onward should be 5x faster

---

## 📋 Changelog

### v1.1 (2024-05-13) - Performance Optimized
- ⚡ **5x faster OCR** - Pre-loaded engine, no repeated model loading
- 🚀 **2.5x faster startup** - Directory packaging instead of onefile
- 💫 **Splash screen** - Visual loading progress
- 📝 **Complete documentation** - Guides, tips, troubleshooting

### v1.0 (2024-05-01) - Initial Release
- 🎯 Drag & drop interface
- 📊 Multi-tab result display
- 🌍 Multi-language support
- 🔄 Multiple OCR modes

[Full Changelog →](docs/releases/)

---

## 🙏 Acknowledgments

This project is built upon:
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - Powerful multilingual OCR toolkit
- [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader) - Base OCR engine
- [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2) - Drag & drop support
- [Pillow](https://python-pillow.org/) - Image processing

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **GitHub**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui
- **Issues**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
- **Releases**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases
- **Base OCR Engine**: https://github.com/SyuuKasinn/ocr-invoice-reader

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 💬 Support

Need help? 
- 📖 Check the [Documentation](docs/)
- 🐛 [Report a Bug](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues)
- 💡 [Request a Feature](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues)
- 💬 [Discussions](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/discussions)

---

**⚡ Enjoy 5x faster OCR!**
