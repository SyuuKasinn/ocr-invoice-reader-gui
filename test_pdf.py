#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test PDF loading"""

import sys
import os
import io

# Fix console encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Test 1: Import fitz
try:
    import fitz
    print("[OK] fitz imported successfully")
    print(f"  PyMuPDF version: {fitz.__version__}")
except ImportError as e:
    print(f"[FAIL] Failed to import fitz: {e}")
    sys.exit(1)

# Test 2: Check for PDF files
test_paths = [
    r"C:\Users\kants\Desktop\ocr-invoice-reader\examples",
    r"C:\Users\kants\Desktop",
    os.getcwd()
]

pdf_files = []
for path in test_paths:
    if os.path.exists(path):
        for file in os.listdir(path):
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(path, file))

if not pdf_files:
    print("\n[WARN] No PDF files found in test directories")
    print("Please specify a PDF file path to test:")
    if len(sys.argv) > 1:
        pdf_files = [sys.argv[1]]
    else:
        print("Usage: python test_pdf.py <path_to_pdf>")
        sys.exit(0)

# Test 3: Try to open a PDF
pdf_path = pdf_files[0]
print(f"\n[PDF] Testing PDF: {pdf_path}")

try:
    pdf = fitz.open(pdf_path)
    print(f"[OK] PDF opened successfully")
    print(f"  Total pages: {len(pdf)}")

    # Test page rendering
    page = pdf[0]
    print(f"[OK] Got first page")
    print(f"  Page size: {page.rect}")

    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    print(f"[OK] Rendered pixmap")
    print(f"  Pixmap size: {pix.width}x{pix.height}")

    img_data = pix.tobytes("ppm")
    print(f"[OK] Got image data ({len(img_data)} bytes)")

    # Convert to PIL
    import io
    from PIL import Image
    pil_img = Image.open(io.BytesIO(img_data))
    print(f"[OK] Converted to PIL Image")
    print(f"  Image size: {pil_img.size}")
    print(f"  Image mode: {pil_img.mode}")

    # Convert to numpy/cv2
    import numpy as np
    import cv2
    np_img = np.array(pil_img)
    cv_img = cv2.cvtColor(np_img, cv2.COLOR_RGB2BGR)
    print(f"[OK] Converted to OpenCV format")
    print(f"  Array shape: {cv_img.shape}")

    pdf.close()
    print("\n[SUCCESS] All PDF tests passed!")

except Exception as e:
    print(f"\n[ERROR] PDF test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
