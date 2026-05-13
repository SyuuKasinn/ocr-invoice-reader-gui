#!/usr/bin/env python3
"""
Automated Demo Script
This script automatically demonstrates the GUI functionality.
Record this with ScreenToGif or similar tool.
"""

import tkinter as tk
from tkinter import ttk
import time
import sys
from pathlib import Path

def auto_demo():
    """Run automated demonstration"""
    print("🎬 Starting Automated Demo...")
    print("Please start your screen recorder NOW!")
    print("Recording will begin in 5 seconds...")

    for i in range(5, 0, -1):
        print(f"  {i}...")
        time.sleep(1)

    print("▶️ RECORDING STARTED - Starting GUI...")

    # Import GUI (after countdown)
    from ocr_gui import OCRInvoiceGUI
    from tkinterdnd2 import TkinterDnD

    root = TkinterDnD.Tk()
    app = OCRInvoiceGUI(root)

    # Position window nicely
    root.geometry("1000x800+200+100")
    root.update()

    def demo_sequence():
        """Execute demo sequence with delays"""
        try:
            # Step 1: Show empty GUI (2 seconds)
            print("Step 1: Showing empty GUI (2s)")
            root.after(2000, step2)

        except Exception as e:
            print(f"Error in demo: {e}")

    def step2():
        """Step 2: Simulate file load"""
        print("Step 2: Loading sample file (3s)")

        # Find sample file
        sample_files = [
            Path("../ocr-invoice-reader/examples/142816_structure.jpg"),
            Path("../ocr-invoice-reader/results/20260512_183659/142816_structure_viz.jpg"),
            Path("C:/Users/kants/Desktop/ocr-invoice-reader/examples/142816_structure.jpg"),
        ]

        sample_file = None
        for f in sample_files:
            if f.exists():
                sample_file = str(f.resolve())
                break

        if sample_file:
            # Simulate file load
            app.load_file(sample_file)
            print(f"  Loaded: {sample_file}")
            root.after(3000, step3)
        else:
            print("  ⚠️ No sample file found! Please manually drag a file.")
            print("  Waiting 5 seconds for manual file drop...")
            root.after(5000, step3)

    def step3():
        """Step 3: Configure settings (optional)"""
        print("Step 3: Configuring settings (1s)")

        # Set language to ch (Chinese - best for mixed documents)
        app.lang_var.set("ch")

        root.after(1000, step4)

    def step4():
        """Step 4: Process document"""
        print("Step 4: Processing document (3-5s)")

        if app.current_file:
            # Trigger processing
            app.process_document()
            print("  Processing started...")
            # Wait for processing (estimated 5s)
            root.after(5000, step5)
        else:
            print("  ⚠️ No file loaded, skipping processing")
            root.after(1000, step5)

    def step5():
        """Step 5: Show results tabs"""
        print("Step 5: Showing results (7s)")

        # Switch to Visualization tab (already active)
        print("  → Visualization tab (2s)")
        root.after(2000, lambda: step5_json())

    def step5_json():
        """Switch to JSON tab"""
        print("  → JSON Data tab (1.5s)")
        app.notebook.select(1)  # JSON tab
        root.after(1500, lambda: step5_text())

    def step5_text():
        """Switch to Text tab"""
        print("  → Extracted Text tab (1.5s)")
        app.notebook.select(2)  # Text tab
        root.after(1500, lambda: step5_tables())

    def step5_tables():
        """Switch to Tables tab"""
        print("  → Tables tab (2s)")
        app.notebook.select(3)  # Tables tab
        root.after(2000, lambda: end_demo())

    def end_demo():
        """End demonstration"""
        print("\n✅ Demo completed!")
        print("You can stop recording now.")
        print("\nPress Ctrl+C or close window to exit.")

    # Start demo sequence after GUI is fully loaded
    root.after(1000, demo_sequence)

    # Run GUI
    root.mainloop()

if __name__ == "__main__":
    print("="*50)
    print("  OCR Invoice Reader GUI - Automated Demo")
    print("="*50)
    print("")
    print("This script will automatically demonstrate the GUI.")
    print("")
    print("📋 Instructions:")
    print("1. Launch ScreenToGif (Windows) or Peek (Linux)")
    print("2. Position the recording frame over this window")
    print("3. Press Enter to start")
    print("4. Start recording when countdown finishes")
    print("5. Stop recording when demo completes")
    print("")

    input("Press Enter when ready...")

    auto_demo()
