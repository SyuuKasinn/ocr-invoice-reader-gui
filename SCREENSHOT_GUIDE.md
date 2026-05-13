# Screenshot Capture Guide

Quick guide to capture GUI screenshots manually.

## Method 1: Windows Snipping Tool (Recommended)

### Step 1: Launch GUI
```bash
python ocr_gui.py
```

### Step 2: Take Screenshots

Press `Win + Shift + S` to activate Snipping Tool, then capture:

#### Screenshot 1: Empty GUI
**File**: `demo/screenshot-01-empty.png`
- Show the application just after launching
- Focus on the drop zone and settings panel

#### Screenshot 2: File Loaded  
**File**: `demo/screenshot-02-loaded.png`
- Drag `demo/sample-input.jpg` into the drop zone
- Capture after file info appears
- Shows "File loaded" status

#### Screenshot 3: Processing
**File**: `demo/screenshot-03-processing.png`
- Click "Process Document"
- Quickly capture while progress bar is running
- (Optional - if too fast to capture, skip this)

#### Screenshot 4: Visualization Tab
**File**: `demo/screenshot-04-visualization.png`
- Wait for processing to complete
- Capture the Visualization tab showing OCR boxes
- This is the MOST IMPORTANT screenshot!

#### Screenshot 5: JSON Data Tab
**File**: `demo/screenshot-05-json.png`
- Click on "JSON Data" tab
- Capture the structured JSON output

#### Screenshot 6: Extracted Text Tab
**File**: `demo/screenshot-06-text.png`
- Click on "Extracted Text" tab
- Capture the plain text output

#### Screenshot 7: HTML Tables Tab
**File**: `demo/screenshot-07-tables.png`
- Click on "Tables" tab
- Capture the HTML table output

### Step 3: Save Screenshots

Save each screenshot to the `demo/` folder with the names above.

### Step 4: Optimize Images (Optional)

If screenshots are too large (>500KB each):
```bash
# Using Python PIL (if installed)
python -c "from PIL import Image; import sys; img=Image.open(sys.argv[1]); img.save(sys.argv[2], quality=85, optimize=True)" input.png output.png
```

Or use online tools:
- https://tinypng.com/
- https://compressor.io/

## Method 2: Using Snip & Sketch

1. Press `Win + Shift + S`
2. Select "Rectangular Snip"
3. Draw around the GUI window
4. Screenshot is copied to clipboard
5. Open Paint (`Win + R`, type `mspaint`)
6. Paste (`Ctrl + V`)
7. Save to `demo/` folder

## Method 3: Print Screen

1. Click on GUI window to focus it
2. Press `Alt + Print Screen` (captures active window only)
3. Open Paint
4. Paste
5. Save to demo/ folder

## Quick Checklist

- [ ] Screenshot 1: Empty GUI (initial state)
- [ ] Screenshot 2: File loaded (after drag & drop)
- [ ] Screenshot 4: Visualization tab (**MOST IMPORTANT**)
- [ ] Screenshot 5: JSON tab
- [ ] Screenshot 6: Text tab
- [ ] Screenshot 7: Tables tab

Minimum: Just capture screenshot 1 (empty) and screenshot 4 (visualization).

## After Capturing

```bash
# Check files
ls -lh demo/screenshot-*.png

# Add to git
git add demo/screenshot-*.png

# Commit
git commit -m "Add GUI screenshots showing all tabs"

# Push
git push origin main
```

## Tips

- **Window Size**: Set GUI to ~1000x800 for consistent screenshots
- **Clean Background**: Close unnecessary windows
- **Focus**: Make sure GUI window is in focus
- **Quality**: PNG format is best (lossless)
- **Size**: Try to keep each screenshot under 500KB
- **Timing**: For processing screenshot, start capture immediately after clicking "Process"

## Sample File

Use this file for demonstration:
```
demo/sample-input.jpg
```
or
```
C:\Users\kants\Desktop\ocr-invoice-reader\examples\142816_structure.jpg
```

## Expected Results

After capturing all screenshots, the `demo/` folder should contain:

```
demo/
├── sample-input.jpg              (341 KB) - Input example
├── screenshot-01-empty.png       (~200 KB) - Empty GUI
├── screenshot-02-loaded.png      (~250 KB) - File loaded
├── screenshot-04-visualization.png (~400 KB) - OCR result ⭐
├── screenshot-05-json.png        (~300 KB) - JSON data
├── screenshot-06-text.png        (~250 KB) - Text output
└── screenshot-07-tables.png      (~300 KB) - HTML tables
```

Total size: ~2 MB

---

**Need the screenshots now?** Just capture these 2 minimum:
1. `screenshot-01-empty.png` - Empty GUI
2. `screenshot-04-visualization.png` - OCR result with colored boxes

That's enough to show the project's capabilities!
