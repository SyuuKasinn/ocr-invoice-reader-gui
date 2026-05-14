# GUI Upgrade Plan

## Current Status (v2.1.0)
- ✅ Working OCR processing
- ✅ Visualization generation
- ✅ Image saved to temp folder
- ✅ Text results displayed

## Upgrade to Apple Style (v2.2.0)

### Changes Needed:

1. **Layout** - Split view
   - Left panel (60%): Image canvas with visualization
   - Right panel (40%): Results tabs

2. **Image Display**
   - Add Canvas widget in left panel
   - Display self.annotated_image directly in GUI
   - Add zoom controls (+/−/Reset)

3. **Apple Colors**
   - Background: #FFFFFF (pure white)
   - Accent: #007AFF (Apple blue)
   - Secondary: #F5F5F7 (light gray)
   - Text: #1D1D1F (near black)

4. **Typography**
   - Headers: SF Pro Display (fallback: Arial)
   - Body: SF Pro Text (fallback: Arial)
   - Code: SF Mono (fallback: Courier)

### Implementation Approach:

Since full rewrite is time-consuming, best approach is:
1. Test current version works (already done)
2. Add canvas-based image display
3. Refactor layout to split view
4. Apply Apple styling

Estimated time: ~2-3 hours for complete Apple-style GUI

### Quick Win Option:
Add image display to current GUI first, then refine styling later.

