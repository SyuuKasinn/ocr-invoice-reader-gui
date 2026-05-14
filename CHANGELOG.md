# Changelog

All notable changes to this project will be documented in this file.

---

## [2.0.0] - 2026-05-14

### 🎉 Major Refactor

Complete project restructure for simplicity and reliability.

### Added
- ✅ **New Simple GUI** (`ocr_gui_simple.py`) - 200 lines, clean design
- ✅ **Comprehensive Documentation**:
  - `docs/INSTALL.md` - Complete installation guide
  - `docs/TROUBLESHOOTING.md` - Common issues and solutions
  - Updated `README.md` - Clear project overview
- ✅ **Error Handling** - Better error messages and logging
- ✅ **Quick Launch** - `run_gui.bat` with error checking

### Changed
- 📝 **Documentation** - Complete rewrite for clarity
- 🗂️ **Project Structure** - Organized and simplified
- 🏃 **Run Method** - Source code only (no exe)

### Deprecated
- ❌ `ocr_gui.py` - Original version (archived)
- ❌ `ocr_gui_modern.py` - Complex version (archived)
- ❌ `ocr_gui_optimized.py` - Intermediate version (archived)
- ❌ **.exe files** - Cannot package PaddleOCR reliably

### Removed
- 🗑️ Old release notes and documentation
- 🗑️ Unused build scripts
- 🗑️ Deprecated code

### Fixed
- ✅ **Stability** - Direct API usage, no wrapper complexity
- ✅ **Reliability** - Source code runs consistently
- ✅ **Maintainability** - Simple, readable code

### Technical Details

**Architecture:**
- Direct `EnhancedStructureAnalyzer` API usage
- On-demand OCR engine loading
- Minimal dependencies

**Performance:**
- Startup: ~1 second ⚡
- First OCR: ~10 seconds (loads engine)
- Subsequent: 2-3 seconds ⚡⚡⚡

---

## [1.2.0] - 2024-05-13 (Deprecated)

### Added
- Performance optimization with pre-loaded engine
- Splash screen
- 5x faster processing

### Issues
- Complex codebase (1000+ lines)
- Packaging problems
- Multiple bugs

**Status:** Deprecated, use v2.0.0 instead

---

## [1.1.0] - 2024-05-13 (Deprecated)

### Added
- Button visibility improvements
- No popup windows

**Status:** Deprecated, use v2.0.0 instead

---

## [1.0.0] - 2024-05-01 (Deprecated)

### Added
- Initial GUI release
- Drag and drop
- Multi-language support
- Multiple OCR modes

**Status:** Deprecated, use v2.0.0 instead

---

## Migration Guide

### From v1.x to v2.0

**Old way:**
```bash
# Download .exe
# Double-click
```

**New way:**
```bash
# Install dependencies
pip install -e /path/to/ocr-invoice-reader

# Run GUI
python src/ocr_gui_simple.py
```

**Why?**
- More reliable
- Easier to update
- Better error messages
- Cross-platform support

---

## Versioning

We use [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible changes
- **MINOR** version for new features
- **PATCH** version for bug fixes

---

## Links

- **Repository**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui
- **OCR Engine**: https://github.com/SyuuKasinn/ocr-invoice-reader
- **Issues**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
