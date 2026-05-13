# GIF Recording Guide - OCR Invoice Reader GUI

This guide will help you create a professional demo GIF for the project.

## 🎬 What to Record

Create a GIF showing:
1. **Launch**: Application starting up
2. **Drag & Drop**: Dragging a PDF/image file into the drop zone
3. **Configure**: Selecting language and mode (optional)
4. **Process**: Clicking "Process Document" and showing progress
5. **Results**: Switching between tabs (Visualization, JSON, Text, Tables)

**Duration**: 10-20 seconds (keep it concise)

## 🛠️ Recommended Tools

### Windows

#### Option 1: ScreenToGif (Best for Windows)
```powershell
# Install via winget
winget install NickeManarin.ScreenToGif

# Or download from
# https://www.screentogif.com/
```

**Steps:**
1. Launch ScreenToGif
2. Click "Recorder"
3. Position the recording frame over your GUI window
4. Click "Record" (or press F7)
5. Perform the demo actions
6. Click "Stop" (F8)
7. Edit/trim if needed
8. Click "Save As" → Choose GIF format
9. Optimize: Set to ~15 FPS, reduce colors if needed
10. Save as `demo.gif`

#### Option 2: ShareX
```powershell
winget install ShareX.ShareX
```

### macOS

#### Option 1: GIPHY Capture
- Download from Mac App Store
- Simple and free
- Drag to select area, record, save as GIF

#### Option 2: Kap
```bash
brew install --cask kap
```

### Linux

#### Option 1: Peek
```bash
# Ubuntu/Debian
sudo apt install peek

# Fedora
sudo dnf install peek

# Arch
sudo pacman -S peek
```

#### Option 2: Gifski + ffmpeg
```bash
# Record with ffmpeg
ffmpeg -f x11grab -s 1280x720 -i :0.0 -r 15 output.mp4

# Convert to GIF with gifski
gifski -o demo.gif output.mp4
```

## 📝 Recording Checklist

### Before Recording

- [ ] Clean desktop background (minimize distractions)
- [ ] Set GUI window to a good size (~800x600 to 1000x800)
- [ ] Close unnecessary notifications
- [ ] Prepare a sample file to drag (invoice.pdf or waybill.jpg)
- [ ] Test the workflow once before recording
- [ ] Set recording frame rate to 10-15 FPS (smaller file size)

### During Recording

1. **Start Clean** (2 seconds)
   - Show the empty GUI with drop zone visible

2. **Drag File** (3 seconds)
   - Drag a PDF/image file from a folder
   - Drop it into the drop zone
   - Show file info appearing

3. **Configure** (2 seconds, optional)
   - Quickly show language/mode selection
   - Keep it brief

4. **Process** (3 seconds)
   - Click "Process Document" button
   - Show progress bar animating
   - Wait for completion

5. **Show Results** (5-8 seconds)
   - Click "Visualization" tab - pause 2 seconds
   - Click "JSON Data" tab - pause 1 second
   - Click "Extracted Text" tab - pause 1 second
   - Click "Tables" tab - pause 1 second

6. **End** (1 second)
   - Show final result briefly

### After Recording

- [ ] Trim any dead time at start/end
- [ ] Optimize GIF size (target: under 5MB, ideally 2-3MB)
- [ ] Test GIF plays smoothly in browser
- [ ] Verify text is readable

## 🎨 Recording Tips

### Window Size
- **Recommended**: 1000x800 or 1200x900
- Not too large (huge file size)
- Not too small (text unreadable)

### Frame Rate
- **10-15 FPS**: Smooth enough, smaller files
- **20 FPS**: Smoother but larger files
- Avoid 30+ FPS (unnecessary for demos)

### Colors
- **256 colors**: Usually sufficient for GUI
- **Reduce palette**: Makes GIF smaller

### Timing
- **Pause on important screens**: 1-2 seconds
- **Quick transitions**: Don't linger too long
- **Total duration**: Aim for 10-20 seconds

### Sample File
Use a visually interesting document:
- The international waybill example (142816_structure.jpg)
- Or a multi-page invoice with tables
- Something that shows off the OCR capabilities

## 📐 Optimization

### ScreenToGif Optimization Settings
```
- Frame rate: 15 FPS
- Repeat: Forever
- Quality: 80-90%
- Color quantization: Enabled
- Size: Target 2-3 MB
```

### Command Line (gifski)
```bash
# High quality, reasonable size
gifski --fps 15 --quality 90 -o demo.gif input.mp4

# Smaller file size
gifski --fps 10 --quality 80 --fast -o demo.gif input.mp4
```

### Online Optimization (if needed)
- https://ezgif.com/optimize
- Upload your GIF
- Set compression level 35-50
- Optimize

## 📁 File Organization

Create this structure:
```
ocr-invoice-reader-gui/
├── demo/
│   ├── demo.gif                  # Main demo (10-20s)
│   ├── demo-full.gif             # Full demo (optional, longer)
│   ├── screenshot-main.png       # Main interface
│   ├── screenshot-viz.png        # Visualization tab
│   └── screenshot-results.png    # Results tabs
```

## 📝 README Integration

After creating the GIF, update README.md:

```markdown
## 🎥 Demo

![OCR Invoice Reader GUI Demo](demo/demo.gif)

*Drag & drop a document, select settings, and view OCR results in real-time*
```

## 🎯 Quick Recording Script

**5-Step Demo (Total: ~15 seconds)**

1. **0:00-0:02** - Show empty GUI
2. **0:02-0:05** - Drag and drop file
3. **0:05-0:06** - Click "Process Document"
4. **0:06-0:09** - Watch progress bar (speed up this part if needed)
5. **0:09-0:15** - Click through tabs showing results

## 🔄 Alternative: Screenshots + Arrows

If GIF is too large or difficult:
1. Take 4-5 key screenshots
2. Add arrows/annotations with tools like:
   - Windows: Paint 3D, Snip & Sketch
   - macOS: Preview
   - Linux: GIMP, Krita
3. Create a collage with arrows showing workflow

## ✅ Final Checks

Before committing:
- [ ] GIF file size under 5MB (preferably 2-3MB)
- [ ] GIF plays correctly in browser
- [ ] Text/UI elements are readable
- [ ] Demonstration is clear and smooth
- [ ] No sensitive information visible
- [ ] File is optimized for web

## 🚀 Quick Start Command

**Using ScreenToGif (Windows):**
```
1. Open ScreenToGif
2. Recorder → Position over GUI window
3. Press F7 to start recording
4. Perform demo actions (15 seconds)
5. Press F8 to stop
6. File → Save As → GIF
7. Save to demo/demo.gif
```

**Using Peek (Linux):**
```bash
# Install
sudo apt install peek

# Run
peek

# 1. Position window over GUI
# 2. Click record
# 3. Perform demo
# 4. Stop and save as demo.gif
```

**Using Kap (macOS):**
```bash
# Install
brew install --cask kap

# Run and record
open -a Kap

# 1. Select area
# 2. Record demo
# 3. Export as GIF
```

---

**Need help?** Check example GIFs on similar projects:
- https://github.com/topics/gui-application
- https://github.com/topics/drag-and-drop

**File too large?** 
- Reduce frame rate to 10 FPS
- Reduce resolution
- Use https://ezgif.com/optimize
