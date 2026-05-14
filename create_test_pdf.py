#!/usr/bin/env python3
"""Create a simple test PDF with text"""

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    pdf_path = "test_document.pdf"

    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Page 1
    c.setFont("Helvetica", 20)
    c.drawString(100, 750, "Test Document - Page 1")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "This is a test PDF for OCR processing.")
    c.drawString(100, 680, "It contains multiple lines of text.")
    c.drawString(100, 660, "Invoice Number: INV-2024-001")
    c.drawString(100, 640, "Date: 2024-01-15")
    c.drawString(100, 620, "Amount: $1,234.56")
    c.showPage()

    # Page 2
    c.setFont("Helvetica", 20)
    c.drawString(100, 750, "Test Document - Page 2")
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "This is the second page.")
    c.drawString(100, 680, "More test content here.")
    c.showPage()

    c.save()
    print(f"Created test PDF: {pdf_path}")

except ImportError:
    print("reportlab not installed. Installing...")
    import subprocess
    subprocess.check_call(["pip", "install", "reportlab"])
    print("Please run this script again.")
