# Changelog

All notable changes to this project will be documented in this file.

---

## [1.0.0] - 2026-05-14

### 🎨 Apple-Style GUI with Advanced Features

**Major Redesign:**
- ✅ **Apple-Style Interface** - Clean, minimalist design inspired by macOS
- ✅ **Split-Pane Layout** - 60% preview canvas + 40% results panel
- ✅ **Professional Color Scheme** - Apple design system colors
- ✅ **Drag & Drop** - File drag-drop onto preview canvas
- ✅ **Real-time Visualization** - Annotated images displayed in canvas

**Multi-Page PDF Support:**
- ✅ **Page Navigation** - Previous/Next buttons for PDF pages
- ✅ **Page Cache System** - Results cached for instant switching
- ✅ **Batch Processing** - "Process All Pages" option
- ✅ **Combined Results** - Multi-page CSV/JSON export

**PDF Quality Control:**
- ✅ **DPI Settings** - 144/216/288/300 DPI options
- ✅ **Auto-Reload** - Preview updates when quality changes
- ✅ **Smart Caching** - OCR results preserved during DPI changes

**Enhanced Results Display:**
- ✅ **Four View Tabs** - Summary, Regions, JSON, CSV
- ✅ **CSV Export** - Built-in CSV generation
- ✅ **Export Options** - Save as JSON or CSV file
- ✅ **Structured Data** - Region type, bbox, confidence, text

**Auto-Processing:**
- ✅ **Settings Watch** - Auto-reprocess when language/GPU changes
- ✅ **Smart Updates** - Only reprocesses if needed
- ✅ **Preserved State** - Maintains zoom and current page

**Code Quality:**
- ✅ **DRY Improvements** - Eliminated duplicate PDF rendering code
- ✅ **Better Resource Management** - Proper temp file cleanup with finally blocks
- ✅ **Memory Optimization** - Removed unnecessary deep copies
- ✅ **Error Handling** - File existence checks and validation

**Core Engine Sync (v2.2.1+):**
- ✅ **Table Detection** - Automatic fallback when tables not detected
- ✅ **OCR Fallback** - Direct OCR for empty table regions
- ✅ **Smart Validation** - Content sufficiency checks
- ✅ **Region Type Stats** - Console output shows region distribution

**Technical:**
- 1177 lines of well-structured code
- tkinterdnd2 for drag-and-drop
- PyMuPDF for PDF rendering
- Thread-based processing for responsive UI
- Comprehensive error handling and logging

**See Also:**
- [SYNC_v2.2.1.md](SYNC_v2.2.1.md) - Core engine updates
- [PDF_DPI_FIX.md](PDF_DPI_FIX.md) - PDF quality improvements

---

## [2.1.0] - 2026-05-14 (Deprecated)

### 🎨 Added Visualization

**New Features:**
- ✅ **Image Visualization** - Annotated images with OCR boxes
- ✅ **Region Highlighting** - Color-coded detection regions
- ✅ **Automatic Export** - Visualization saved to temp folder
- ✅ **File Location Display** - Easy access to visualization image

**Technical:**
- Integrated `OCRVisualizer` from ocr-invoice-reader
- Draw OCR text boxes (red)
- Draw region boxes (colored by type: table/text/title/figure)
- Display confidence scores
- Save annotated image automatically

**Fixed:**
- ✅ API compatibility with LayoutRegion objects
- ✅ Proper JSON serialization
- ✅ Better error handling

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
