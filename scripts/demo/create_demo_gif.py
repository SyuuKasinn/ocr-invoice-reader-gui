#!/usr/bin/env python3
"""
Automated GIF Creation Script
This script uses pyautogui to automate the demo and record it simultaneously.
"""

import os
import sys
import time
import subprocess
from pathlib import Path

def check_dependencies():
    """Check if required tools are available"""
    print("Checking dependencies...")

    # Check Python packages
    required = ['pyautogui', 'Pillow']
    missing = []

    for pkg in required:
        try:
            __import__(pkg)
            print(f"  ✓ {pkg} found")
        except ImportError:
            print(f"  ✗ {pkg} missing")
            missing.append(pkg)

    if missing:
        print(f"\nInstalling missing packages: {', '.join(missing)}")
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing)

    # Check for recording tool
    screentogif_paths = [
        "C:\\Program Files\\ScreenToGif\\ScreenToGif.exe",
        "C:\\Program Files (x86)\\ScreenToGif\\ScreenToGif.exe",
    ]

    screentogif_found = any(Path(p).exists() for p in screentogif_paths)

    if not screentogif_found:
        print("\n⚠️ ScreenToGif not found")
        print("Installing via winget...")
        try:
            subprocess.run(["winget", "install", "NickeManarin.ScreenToGif"], check=False)
        except Exception as e:
            print(f"Could not install automatically: {e}")
            print("Please install from: https://www.screentogif.com/")
            return False

    return True

def find_sample_file():
    """Find a sample file to use"""
    candidates = [
        "../ocr-invoice-reader/examples/142816_structure.jpg",
        "../ocr-invoice-reader/results/20260512_183659/142816_structure_viz.jpg",
        "C:/Users/kants/Desktop/ocr-invoice-reader/examples/142816_structure.jpg",
    ]

    for path in candidates:
        p = Path(path)
        if p.exists():
            return str(p.resolve())

    return None

def manual_recording_guide():
    """Show manual recording instructions"""
    print("\n" + "="*60)
    print("  MANUAL RECORDING GUIDE")
    print("="*60)
    print("")
    print("Since automated recording is complex, here's the easiest way:")
    print("")
    print("1️⃣  Install ScreenToGif:")
    print("   winget install NickeManarin.ScreenToGif")
    print("")
    print("2️⃣  Launch both programs:")
    print("   Terminal 1: ScreenToGif")
    print("   Terminal 2: python ocr_gui.py")
    print("")
    print("3️⃣  In ScreenToGif:")
    print("   • Click 'Recorder'")
    print("   • Position frame over GUI window")
    print("   • Click 'Record' (or press F7)")
    print("")
    print("4️⃣  Perform demo (15 seconds):")
    print("   a. Show empty GUI (2s)")
    print("   b. Drag file into drop zone (3s)")
    print(f"      Sample file: {find_sample_file()}")
    print("   c. Click 'Process Document' (1s)")
    print("   d. Wait for processing (3s)")
    print("   e. Click through tabs: Viz→JSON→Text→Tables (6s)")
    print("")
    print("5️⃣  In ScreenToGif:")
    print("   • Click 'Stop' (or press F8)")
    print("   • Review/edit frames")
    print("   • File → Save As → GIF")
    print("   • Set Frame Rate: 12-15 FPS")
    print("   • Save to: demo/demo.gif")
    print("")
    print("6️⃣  Commit and push:")
    print("   git add demo/demo.gif")
    print("   git commit -m 'Add demo GIF'")
    print("   git push")
    print("")
    print("="*60)
    print("")

def quick_start():
    """Quick start the tools"""
    print("Quick Start Option:")
    print("")
    print("[1] Launch ScreenToGif")
    print("[2] Launch GUI")
    print("[3] Launch both")
    print("[4] Show detailed guide")
    print("[Q] Quit")
    print("")

    choice = input("Your choice: ").strip().upper()

    if choice == "1":
        print("Launching ScreenToGif...")
        # Try to launch
        for path in [
            "C:\\Program Files\\ScreenToGif\\ScreenToGif.exe",
            "C:\\Program Files (x86)\\ScreenToGif\\ScreenToGif.exe",
        ]:
            if Path(path).exists():
                subprocess.Popen([path])
                print("✓ ScreenToGif launched!")
                break
        else:
            print("✗ ScreenToGif not found")

    elif choice == "2":
        print("Launching GUI...")
        subprocess.Popen([sys.executable, "ocr_gui.py"])
        print("✓ GUI launched!")

    elif choice == "3":
        print("Launching both...")
        # Launch ScreenToGif
        for path in [
            "C:\\Program Files\\ScreenToGif\\ScreenToGif.exe",
            "C:\\Program Files (x86)\\ScreenToGif\\ScreenToGif.exe",
        ]:
            if Path(path).exists():
                subprocess.Popen([path])
                print("✓ ScreenToGif launched!")
                break

        time.sleep(2)

        # Launch GUI
        subprocess.Popen([sys.executable, "ocr_gui.py"])
        print("✓ GUI launched!")

        print("\n📋 Now follow the recording steps:")
        print("1. In ScreenToGif: Click 'Recorder' and position over GUI")
        print("2. Press F7 to start recording")
        print("3. Perform the demo actions")
        print("4. Press F8 to stop")
        print("5. Save as demo/demo.gif")

    elif choice == "4":
        manual_recording_guide()

    else:
        print("Exiting...")

if __name__ == "__main__":
    print("="*60)
    print("  OCR Invoice Reader GUI - Demo GIF Creator")
    print("="*60)
    print("")

    # Check dependencies
    if not check_dependencies():
        print("\n⚠️ Please install missing dependencies first")
        sys.exit(1)

    print("\n✓ All dependencies OK!")
    print("")

    # Show options
    quick_start()

    print("\n💡 See RECORDING_GUIDE.md for detailed instructions")
    print("="*60)
