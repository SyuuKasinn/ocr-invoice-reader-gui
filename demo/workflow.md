# Workflow Visualization

## 📋 Step-by-Step Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Input Document                                     │
│  ─────────────────────                                      │
│  • Drag & drop PDF or image file                            │
│  • Or click "Browse Files" button                           │
│  • Supported: .pdf, .jpg, .png                              │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Configure Settings                                 │
│  ──────────────────────                                     │
│  • Language: ch / en / japan / korean                       │
│  • Mode: ocr-enhanced (recommended)                         │
│  • GPU: Enable if available                                 │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Process                                            │
│  ─────────────                                              │
│  • Click "Process Document" button                          │
│  • Watch progress bar                                       │
│  • Wait for completion (2-10 seconds)                       │
└─────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────┐
│  Step 4: View Results (Multi-Tab Interface)                 │
│  ──────────────────────────────────────                     │
│                                                              │
│  Tab 1: 📊 Visualization                                    │
│  ├─ OCR text boxes (red polygons)                          │
│  ├─ Table regions (orange boxes)                           │
│  ├─ Title regions (blue boxes)                             │
│  └─ Text regions (green boxes)                             │
│                                                              │
│  Tab 2: 📋 JSON Data                                        │
│  ├─ Structured extraction results                          │
│  ├─ Region coordinates                                      │
│  ├─ Confidence scores                                       │
│  └─ Table structure info                                    │
│                                                              │
│  Tab 3: 📝 Extracted Text                                   │
│  ├─ Plain text from all pages                              │
│  ├─ Line by line output                                     │
│  └─ Multi-language text                                     │
│                                                              │
│  Tab 4: 🔢 Tables                                           │
│  ├─ HTML formatted tables                                   │
│  ├─ Structured table data                                   │
│  └─ Cell-level information                                  │
└─────────────────────────────────────────────────────────────┘
```

## 🎯 Example Processing Time

| Document Type | Pages | Processing Time (CPU) |
|---------------|-------|-----------------------|
| Single image  | 1     | 2-3 seconds          |
| Simple invoice| 1-2   | 3-5 seconds          |
| Complex waybill| 1    | 4-6 seconds          |
| Multi-page PDF| 10    | 20-40 seconds        |

## 🖼️ Visual Output Features

### Color Coding in Visualization

| Color | Element | Purpose |
|-------|---------|---------|
| 🔴 Red | Text Polygons | Character-level OCR detection |
| 🟧 Orange | Table Boxes | Detected table regions |
| 🔵 Blue | Title Boxes | Header and title areas |
| 🟢 Green | Text Boxes | Plain text regions |

### JSON Structure Example

```json
{
  "method": "coordinate_based",
  "total_pages": 1,
  "pages": [
    {
      "page_number": 1,
      "regions": [
        {
          "type": "table",
          "bbox": [30, 170, 540, 460],
          "confidence": 0.95,
          "rows": 8,
          "columns": 3
        }
      ]
    }
  ]
}
```

## 🚀 Quick Start Command

```bash
# Launch GUI
python ocr_gui.py

# Or use quick start scripts
# Windows:
run.bat

# Linux/macOS:
./run.sh
```
