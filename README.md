# OCR Invoice Reader GUI

**Drag-and-Drop Desktop Application for Invoice OCR Processing**

A user-friendly graphical interface for [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader) that provides real-time visualization of OCR results.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Based on](https://img.shields.io/badge/based%20on-ocr--invoice--reader-orange)](https://github.com/SyuuKasinn/ocr-invoice-reader)

## ✨ Features

- **🎯 Drag & Drop Interface**: Simply drag PDF or image files into the application
- **📊 Real-time Visualization**: View OCR text boxes and region detection instantly
- **🌍 Multi-language Support**: Chinese, English, Japanese, Korean
- **⚙️ Multiple OCR Modes**: Enhanced, Extract, Raw, Simple
- **📑 Tabbed Results View**: Visualization, JSON data, extracted text, and HTML tables
- **💻 Cross-platform**: Works on Windows, macOS, and Linux

## 🖼️ Screenshots

### Main Interface
The application features a clean, intuitive interface with:
- **Left Panel**: Drag-and-drop zone, settings, and process button
- **Right Panel**: Tabbed view for visualization and results

### Results Display
- **Visualization Tab**: OCR text boxes with color-coded regions
- **JSON Tab**: Structured data output
- **Text Tab**: Extracted plain text
- **Tables Tab**: HTML formatted tables

## 📦 Installation

### Prerequisites

1. **Install OCR Invoice Reader** (the core engine):
```bash
# Clone the main OCR repository
git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git
cd ocr-invoice-reader
pip install -e .
cd ..
```

2. **Clone this GUI repository**:
```bash
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui
```

3. **Install GUI dependencies**:
```bash
pip install -r requirements.txt
```

### Quick Install (All-in-One)

```bash
# Install OCR engine
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Clone and setup GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui
pip install -r requirements.txt
```

## 🚀 Usage

### Launch the Application

```bash
python ocr_gui.py
```

### Basic Workflow

1. **Load Document**
   - Drag and drop a PDF or image file into the drop zone, OR
   - Click "Browse Files" button to select a file

2. **Configure Settings** (Optional)
   - **Language**: Select `ch`, `en`, `japan`, or `korean`
   - **Mode**: Choose OCR mode
     - `ocr-enhanced`: Best for production (recommended)
     - `ocr-extract`: Structured field extraction
     - `ocr-raw`: PP-Structure raw output
     - `ocr-simple`: Simple text extraction
   - **GPU**: Enable if CUDA is available

3. **Process**
   - Click "Process Document" button
   - Wait for processing to complete (progress bar will show activity)

4. **View Results**
   - **Visualization Tab**: See OCR detection with colored boxes
   - **JSON Data Tab**: View structured output
   - **Extracted Text Tab**: Read plain text
   - **Tables Tab**: View HTML formatted tables

## 🎨 Understanding the Visualization

The visualization shows:
- 🔴 **Red Polygons**: OCR text boxes (character-level detection)
- 🟧 **Orange Boxes**: Table regions
- 🔵 **Blue Boxes**: Title/header regions
- 🟢 **Green Boxes**: Plain text regions

## 📋 OCR Modes Explained

| Mode | Purpose | Best For |
|------|---------|----------|
| **ocr-enhanced** | Enhanced structure + table detection | Production invoices, complex layouts |
| **ocr-extract** | Structured field extraction | Document classification, data entry |
| **ocr-raw** | PP-Structure raw output | Debugging, comparison |
| **ocr-simple** | Simple text extraction | Quick text-only needs |

## 🌍 Language Support

| Language | Code | Quality |
|----------|------|---------|
| Chinese | `ch` | ⭐⭐⭐⭐⭐ |
| Japanese | `japan` | ⭐⭐⭐⭐⭐ |
| English | `en` | ⭐⭐⭐⭐⭐ |
| Korean | `korean` | ⭐⭐⭐⭐ |

**💡 Tip**: Use `ch` for mixed-language documents (e.g., Japanese + English)

## 🛠️ Requirements

- **Python**: 3.8 or higher
- **OCR Invoice Reader**: Latest version from [GitHub](https://github.com/SyuuKasinn/ocr-invoice-reader)
- **TkinterDnD2**: For drag-and-drop functionality
- **Pillow**: For image handling
- **PaddleOCR**: Installed automatically with ocr-invoice-reader

## 🐛 Troubleshooting

### Issue: "TkinterDnD2 is required" error
**Solution**: Install tkinterdnd2
```bash
pip install tkinterdnd2
```

### Issue: "Command not found" error when processing
**Solution**: Ensure ocr-invoice-reader is installed and commands are in PATH
```bash
# Test if commands are available
ocr-enhanced --help
```

### Issue: Visualization not displaying
**Solution**: Check that Pillow is installed
```bash
pip install --upgrade Pillow
```

### Issue: Slow processing on Windows
**Solution**: The first run downloads PaddleOCR models (~200MB). Subsequent runs are faster. Consider using `--use-cpu` flag if GPU issues occur.

## 📁 Project Structure

```
ocr-invoice-reader-gui/
├── ocr_gui.py              # Main GUI application
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── LICENSE                # MIT License
└── screenshots/           # Application screenshots (optional)
```

## 🔗 Related Projects

- [OCR Invoice Reader](https://github.com/SyuuKasinn/ocr-invoice-reader) - Core OCR engine
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR framework

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built on top of [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader)
- Uses [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) for OCR processing
- GUI framework: [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Drag-and-drop: [tkinterdnd2](https://github.com/pmgagne/tkinterdnd2)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

For issues and questions:
- Check the [main OCR documentation](https://github.com/SyuuKasinn/ocr-invoice-reader)
- Open an issue on GitHub

---

**Made with ❤️ using Tkinter and OCR Invoice Reader**
