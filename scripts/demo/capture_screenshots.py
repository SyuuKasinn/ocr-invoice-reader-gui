#!/usr/bin/env python3
"""
Automatic Screenshot Capture Script
Captures screenshots of the GUI in different states
"""

import sys
import time
from pathlib import Path
import tkinter as tk

def capture_screenshots():
    """Capture screenshots of different GUI states"""
    print("Starting GUI screenshot capture...")

    # Import after print to show we're starting
    from ocr_gui import OCRInvoiceGUI
    from tkinterdnd2 import TkinterDnD

    # Try to import screenshot tool
    try:
        from PIL import ImageGrab
        import pygetwindow as gw
    except ImportError:
        print("Installing screenshot dependencies...")
        import subprocess
        subprocess.run([sys.executable, "-m", "pip", "install", "pygetwindow", "Pillow"])
        from PIL import ImageGrab
        import pygetwindow as gw

    # Create output directory
    demo_dir = Path("demo")
    demo_dir.mkdir(exist_ok=True)

    root = TkinterDnD.Tk()
    app = OCRInvoiceGUI(root)

    # Position window nicely
    root.geometry("1100x850+100+50")
    root.update()

    # Give window time to render
    time.sleep(1)

    def capture_window(filename, description):
        """Capture the current window"""
        try:
            root.update()
            time.sleep(0.5)

            # Get window position
            x = root.winfo_rootx()
            y = root.winfo_rooty()
            w = root.winfo_width()
            h = root.winfo_height()

            # Capture screenshot
            screenshot = ImageGrab.grab(bbox=(x, y, x + w, y + h))

            # Save
            filepath = demo_dir / filename
            screenshot.save(filepath)
            print(f"OK Captured: {filename} - {description}")

        except Exception as e:
            print(f"ERROR capturing {filename}: {e}")

    # Screenshot 1: Empty GUI
    print("\n[1/5] Capturing empty GUI...")
    capture_window("screenshot-01-empty.png", "Empty GUI with drop zone")

    # Screenshot 2: File loaded
    print("\n[2/5] Loading sample file...")
    sample_files = [
        Path("../ocr-invoice-reader/examples/142816_structure.jpg"),
        Path("demo/sample-input.jpg"),
        Path("C:/Users/kants/Desktop/ocr-invoice-reader/examples/142816_structure.jpg"),
    ]

    sample_file = None
    for f in sample_files:
        if f.exists():
            sample_file = str(f.resolve())
            break

    if sample_file:
        app.load_file(sample_file)
        time.sleep(1)
        capture_window("screenshot-02-loaded.png", "File loaded, ready to process")
    else:
        print("WARNING: No sample file found, skipping loaded state")

    # Screenshot 3: Processing
    print("\n[3/5] Starting processing...")
    if app.current_file:
        # Start processing in a way that we can capture it
        def process_and_capture():
            time.sleep(1)  # Let processing start
            capture_window("screenshot-03-processing.png", "Processing in progress")

        # Schedule screenshot during processing
        root.after(500, process_and_capture)

        # Start processing
        app.process_document()

        # Wait for processing to complete
        print("   Waiting for processing to complete (may take 5-10 seconds)...")

        # Keep checking if processing is done
        def check_and_capture_results(attempt=0):
            if attempt > 20:  # Max 20 seconds wait
                print("   Timeout waiting for results")
                root.quit()
                return

            # Check if results are available
            if app.current_result_dir and app.current_result_dir.exists():
                print("\n[4/5] Processing complete! Capturing results...")
                time.sleep(1)

                # Screenshot 4: Visualization tab
                app.notebook.select(0)
                root.update()
                time.sleep(1)
                capture_window("screenshot-04-visualization.png", "Visualization tab with OCR boxes")

                # Screenshot 5: JSON tab
                print("\n[5/5] Capturing other tabs...")
                app.notebook.select(1)
                root.update()
                time.sleep(0.5)
                capture_window("screenshot-05-json.png", "JSON data tab")

                # Screenshot 6: Text tab
                app.notebook.select(2)
                root.update()
                time.sleep(0.5)
                capture_window("screenshot-06-text.png", "Extracted text tab")

                # Screenshot 7: Tables tab
                app.notebook.select(3)
                root.update()
                time.sleep(0.5)
                capture_window("screenshot-07-tables.png", "HTML tables tab")

                print("\n" + "="*60)
                print("SUCCESS: All screenshots captured!")
                print("="*60)
                print(f"\nScreenshots saved to: {demo_dir.resolve()}")
                print("\nFiles created:")
                for img in sorted(demo_dir.glob("screenshot-*.png")):
                    size = img.stat().st_size / 1024
                    print(f"  • {img.name} ({size:.1f} KB)")

                # Close GUI
                root.after(2000, root.quit)
            else:
                # Check again in 1 second
                root.after(1000, lambda: check_and_capture_results(attempt + 1))

        # Start checking for results
        root.after(3000, check_and_capture_results)
    else:
        print("WARNING: No file loaded, cannot process")
        root.quit()

    # Run GUI
    root.mainloop()

    print("\nScreenshot capture complete!")
    print("\nNext steps:")
    print("1. Review screenshots in demo/ folder")
    print("2. git add demo/screenshot-*.png")
    print("3. git commit -m 'Add GUI screenshots'")
    print("4. git push origin main")

if __name__ == "__main__":
    print("="*60)
    print("  OCR Invoice Reader GUI - Screenshot Capture")
    print("="*60)
    print("")
    print("This script will:")
    print("1. Launch the GUI")
    print("2. Load a sample file")
    print("3. Process it with OCR")
    print("4. Capture screenshots of all tabs")
    print("")
    print("WARNING: DO NOT MOVE YOUR MOUSE during capture!")
    print("")

    input("Press Enter to start (process takes ~30 seconds)...")

    try:
        capture_screenshots()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
    except Exception as e:
        print(f"\n\nERROR: {e}")
        import traceback
        traceback.print_exc()
