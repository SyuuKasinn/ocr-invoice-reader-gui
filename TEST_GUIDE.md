# Testing Guide

## Quick Test

1. **Start GUI:**
   ```bash
   python src/ocr_gui_simple.py
   ```

2. **Select Test File:**
   - Browse to any PDF or image (JPG/PNG)
   - Or use example from ocr-invoice-reader repo

3. **Configure Settings:**
   - Language: `ch` (Chinese), `en` (English), etc.
   - GPU: Check if you have NVIDIA GPU + CUDA

4. **Process:**
   - Click "🚀 Process Document"
   - Wait for processing (~10s first time, ~3s after)

5. **View Results:**
   - **Text Results:** Displayed in main window
   - **Visualization:** Check file path shown in results

## Expected Output

### Text Results
```
OCR RESULTS
================================================================================

REGIONS FOUND: X
--------------------------------------------------------------------------------

Region 1:
  Type: table
  BBox: [x1, y1, x2, y2]
  Confidence: XX.XX%
  Text: [extracted text content]
  ...
```

### Visualization Image
Saved to: `C:\Users\<username>\AppData\Local\Temp\ocr_viz_<filename>`

**Contains:**
- 🔴 Red boxes: OCR text detections
- 🟧 Orange boxes: Table regions
- 🟢 Green boxes: Text regions
- 🔵 Blue boxes: Title regions
- 🟣 Purple boxes: Figure regions

## Troubleshooting

### GUI doesn't start
```bash
# Check Python version
python --version  # Should be 3.8+

# Check dependencies
python -c "import tkinter; print('OK')"
python -c "from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer; print('OK')"
```

### Processing fails
```bash
# Check OCR engine installation
cd /path/to/ocr-invoice-reader
pip install -e .

# Verify in GUI project
python -c "import ocr_invoice_reader; print(ocr_invoice_reader.__file__)"
```

### Visualization not working
- Check console output for errors
- Verify image file is readable
- Check temp directory permissions

## Performance Benchmarks

| Operation | First Time | Subsequent |
|-----------|------------|------------|
| GUI Launch | ~1 second | ~1 second |
| Engine Load | ~10 seconds | N/A (cached) |
| OCR Process | ~5-8 seconds | ~2-3 seconds |
| Visualization | ~1-2 seconds | ~1-2 seconds |

## Test Cases

### ✅ Basic Functionality
- [x] GUI launches without errors
- [x] File selection works
- [x] Settings can be changed
- [x] Processing completes successfully
- [x] Results display correctly
- [x] Visualization image created

### ✅ Edge Cases
- [x] Large PDF files (100+ pages)
- [x] Low-quality images
- [x] Multiple languages
- [x] Different file formats (PDF, JPG, PNG)

### ✅ Error Handling
- [x] Invalid file selected
- [x] Corrupted image
- [x] No file selected
- [x] OCR engine fails to load

## Test with Example

```bash
# If you have the OCR engine repo cloned:
cd /path/to/ocr-invoice-reader/examples

# Start GUI
cd /path/to/ocr-invoice-reader-gui
python src/ocr_gui_simple.py

# In GUI:
# 1. Browse to ocr-invoice-reader/examples/142816_structure.jpg
# 2. Set Language: ch
# 3. Click Process
# 4. Wait ~10s (first time)
# 5. Check results and visualization path
```

## Success Criteria

✅ GUI launches successfully  
✅ File selection opens dialog  
✅ Processing completes without errors  
✅ Results show extracted text and regions  
✅ Visualization image is created  
✅ Performance meets expectations  

---

**Version:** 2.1.0  
**Last Updated:** 2026-05-14
