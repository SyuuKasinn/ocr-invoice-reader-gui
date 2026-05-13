# Installation Guide - OCR Invoice Reader GUI

This guide will help you install and set up the OCR Invoice Reader GUI application.

## 📋 Prerequisites

- **Python**: 3.8 or higher
- **pip**: Python package manager
- **Git**: For cloning repositories

### Check Python Version

```bash
python --version
# or
python3 --version
```

You should see Python 3.8.x or higher.

## 🚀 Quick Installation

### Option 1: Full Installation (Recommended)

```bash
# Step 1: Install the core OCR engine
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Step 2: Clone the GUI repository
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Step 3: Install GUI dependencies
pip install -r requirements.txt

# Step 4: Run the application
python ocr_gui.py
```

### Option 2: Local Development Setup

If you have both repositories locally:

```bash
# Step 1: Clone and install OCR engine
git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git
cd ocr-invoice-reader
pip install -e .
cd ..

# Step 2: Clone and setup GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui
pip install -r requirements.txt

# Step 3: Run the application
python ocr_gui.py
```

## 🔧 Detailed Installation Steps

### 1. Install Core Dependencies

The GUI relies on the main OCR engine. Install it first:

```bash
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git
```

This will install:
- PaddleOCR
- PaddlePaddle
- OpenCV
- PyMuPDF
- Other required packages

### 2. Install GUI-Specific Dependencies

```bash
cd ocr-invoice-reader-gui
pip install tkinterdnd2 Pillow
```

### 3. Verify Installation

Test that the OCR commands are available:

```bash
ocr-enhanced --help
```

If this works, you're ready to use the GUI!

## 🐳 Docker Installation (Alternative)

If you prefer Docker, you can run the OCR engine in a container. Note that GUI applications in Docker require X11 forwarding.

```bash
# Pull or build the OCR engine container
cd ocr-invoice-reader
docker-compose up --build
```

Then run the GUI on your host system pointing to the Docker container.

## 🪟 Windows-Specific Instructions

### Using Command Prompt

```cmd
REM Install OCR engine
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

REM Clone GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

REM Install dependencies
pip install -r requirements.txt

REM Run GUI
python ocr_gui.py
```

### Using PowerShell

```powershell
# Install OCR engine
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Clone GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Install dependencies
pip install -r requirements.txt

# Run GUI
python ocr_gui.py
```

### Quick Launch

Double-click `run.bat` in the project folder.

## 🍎 macOS-Specific Instructions

```bash
# Install OCR engine
pip3 install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Clone GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Install dependencies
pip3 install -r requirements.txt

# Run GUI
python3 ocr_gui.py
```

### Quick Launch

```bash
chmod +x run.sh
./run.sh
```

## 🐧 Linux-Specific Instructions

### Ubuntu/Debian

```bash
# Install system dependencies
sudo apt-get update
sudo apt-get install python3 python3-pip python3-tk git

# Install OCR engine
pip3 install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Clone GUI
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui

# Install dependencies
pip3 install -r requirements.txt

# Run GUI
python3 ocr_gui.py
```

### Fedora/RHEL

```bash
# Install system dependencies
sudo dnf install python3 python3-pip python3-tkinter git

# Follow same steps as Ubuntu above
```

## 🔍 Troubleshooting Installation

### Issue: "tkinterdnd2" not found

```bash
pip install tkinterdnd2
```

If that fails, try:
```bash
pip install --upgrade pip
pip install tkinterdnd2
```

### Issue: "ocr-enhanced: command not found"

The OCR engine is not installed or not in PATH.

```bash
# Reinstall the engine
pip uninstall ocr-invoice-reader
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Or install locally
cd ocr-invoice-reader
pip install -e .
```

### Issue: PaddleOCR installation fails

PaddleOCR requires specific system libraries:

**Windows**: Install Visual C++ Redistributable
**Linux**: Install build tools
```bash
sudo apt-get install build-essential python3-dev
```

**macOS**: Install Xcode Command Line Tools
```bash
xcode-select --install
```

### Issue: Tkinter not available

**Linux**:
```bash
sudo apt-get install python3-tk
```

**macOS**: Tkinter should be included with Python. If not, reinstall Python from python.org

**Windows**: Tkinter is included with the official Python installer

### Issue: "No module named 'PIL'"

```bash
pip install Pillow
```

### Issue: GPU-related errors

If you don't have CUDA:
- Use `--use-cpu` flag in the GUI settings
- Or install CPU-only PaddlePaddle:
```bash
pip install paddlepaddle
```

For GPU support:
```bash
pip install paddlepaddle-gpu
```

## ✅ Verify Installation

Run this quick test:

```bash
# Test OCR engine
ocr-enhanced --help

# Test Python imports
python -c "import tkinter; import PIL; print('GUI dependencies OK')"

# Run the GUI
python ocr_gui.py
```

If all commands work, you're ready to go!

## 🔄 Updating

To update to the latest version:

```bash
# Update OCR engine
pip install --upgrade git+https://github.com/SyuuKasinn/ocr-invoice-reader.git

# Update GUI
cd ocr-invoice-reader-gui
git pull origin main
pip install --upgrade -r requirements.txt
```

## 📦 Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

```bash
# Create virtual environment
python -m venv ocr_env

# Activate it
# Windows:
ocr_env\Scripts\activate
# Linux/macOS:
source ocr_env/bin/activate

# Install everything
pip install git+https://github.com/SyuuKasinn/ocr-invoice-reader.git
cd ocr-invoice-reader-gui
pip install -r requirements.txt

# Run GUI
python ocr_gui.py
```

## 🆘 Getting Help

If you encounter issues:

1. Check this guide thoroughly
2. Review the [main OCR documentation](https://github.com/SyuuKasinn/ocr-invoice-reader)
3. Open an issue on GitHub with:
   - Your Python version
   - Your OS
   - Full error message
   - Steps to reproduce

---

**Happy OCR Processing! 🎉**
