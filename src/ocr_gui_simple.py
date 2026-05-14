#!/usr/bin/env python3
"""
Simple OCR Invoice Reader GUI
A minimal, reliable GUI for ocr-invoice-reader

Uses EnhancedStructureAnalyzer directly from ocr-invoice-reader package
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
import threading
import json
import tempfile
from pathlib import Path
from datetime import datetime

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False
    print("[INFO] tkinterdnd2 not available, drag-and-drop disabled")

class SimpleOCRGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Invoice Reader - Simple Edition")
        self.root.geometry("900x700")

        # State
        self.current_file = None
        self.analyzer = None
        self.visualizer = None
        self.processing = False
        self.original_image = None
        self.annotated_image = None
        self.current_result = None
        self.zoom_level = 1.0

        self.setup_ui()

    def setup_ui(self):
        """Setup UI components"""
        # Title
        title = tk.Label(
            self.root,
            text="📄 OCR Invoice Reader",
            font=("Arial", 18, "bold"),
            pady=10
        )
        title.pack()

        # File selection frame
        file_frame = ttk.LabelFrame(self.root, text="1. Select File", padding=10)
        file_frame.pack(fill=tk.X, padx=10, pady=5)

        # Drop zone area (visual indicator)
        drop_zone = tk.Frame(
            file_frame,
            bg="#f0f8ff",
            relief=tk.GROOVE,
            bd=2,
            height=80
        )
        drop_zone.pack(fill=tk.X, padx=5, pady=5)
        drop_zone.pack_propagate(False)

        # Drop zone content
        drop_content = tk.Frame(drop_zone, bg="#f0f8ff")
        drop_content.place(relx=0.5, rely=0.5, anchor='center')

        tk.Label(
            drop_content,
            text="📁",
            font=("Arial", 24),
            bg="#f0f8ff",
            fg="#4CAF50"
        ).pack()

        tk.Label(
            drop_content,
            text="Drag & Drop file here or click Browse",
            font=("Arial", 11),
            bg="#f0f8ff",
            fg="#666"
        ).pack()

        self.file_label = tk.Label(
            drop_content,
            text="",
            font=("Arial", 9, "italic"),
            bg="#f0f8ff",
            fg="gray"
        )
        self.file_label.pack(pady=(5,0))

        # Make drop zone clickable
        def on_drop_zone_click(event):
            self.browse_file()

        drop_zone.bind("<Button-1>", on_drop_zone_click)
        for widget in drop_content.winfo_children():
            widget.bind("<Button-1>", on_drop_zone_click)

        # Enable drag-and-drop if available
        if DND_AVAILABLE:
            self.drop_zone = drop_zone
            drop_zone.drop_target_register(DND_FILES)
            drop_zone.dnd_bind('<<Drop>>', self.on_file_drop)
            drop_zone.dnd_bind('<<DragEnter>>', self.on_drag_enter)
            drop_zone.dnd_bind('<<DragLeave>>', self.on_drag_leave)

        # Browse button
        browse_btn = ttk.Button(
            file_frame,
            text="📂 Browse Files...",
            command=self.browse_file
        )
        browse_btn.pack(pady=(5,0))

        # Settings frame
        settings_frame = ttk.LabelFrame(self.root, text="2. Settings", padding=10)
        settings_frame.pack(fill=tk.X, padx=10, pady=5)

        # Language
        tk.Label(settings_frame, text="Language:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.lang_var = tk.StringVar(value="ch")
        lang_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.lang_var,
            values=["ch", "en", "japan", "korean"],
            state="readonly",
            width=10
        )
        lang_combo.grid(row=0, column=1, padx=5)

        # GPU
        self.gpu_var = tk.BooleanVar(value=False)
        gpu_check = ttk.Checkbutton(
            settings_frame,
            text="Use GPU (if available)",
            variable=self.gpu_var
        )
        gpu_check.grid(row=0, column=2, padx=20)

        # Process button
        process_frame = tk.Frame(self.root)
        process_frame.pack(fill=tk.X, padx=10, pady=10)

        self.process_btn = tk.Button(
            process_frame,
            text="3. 🚀 Process Document",
            command=self.process_document,
            bg="#4CAF50",
            fg="white",
            font=("Arial", 12, "bold"),
            pady=10,
            cursor="hand2",
            state="disabled"
        )
        self.process_btn.pack(fill=tk.X)

        # Progress
        self.progress = ttk.Progressbar(process_frame, mode='indeterminate')

        # Results frame
        results_frame = ttk.LabelFrame(self.root, text="Results", padding=10)
        results_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=("Courier", 9),
            height=20
        )
        self.results_text.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_var = tk.StringVar(value="Ready. Select a file to start.")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W,
            bg="#f0f0f0",
            padx=5
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    def browse_file(self):
        """Browse for file"""
        file_path = filedialog.askopenfilename(
            title="Select Document",
            filetypes=[
                ("All Supported", "*.pdf *.jpg *.jpeg *.png"),
                ("PDF files", "*.pdf"),
                ("Image files", "*.jpg *.jpeg *.png"),
                ("All files", "*.*")
            ]
        )

        if file_path:
            self.load_file(file_path)

    def load_file(self, file_path):
        """Load a file (from browse or drag-drop)"""
        # Validate file type
        valid_extensions = ('.pdf', '.jpg', '.jpeg', '.png')
        if not file_path.lower().endswith(valid_extensions):
            messagebox.showwarning("Invalid File", "Please select a PDF or image file (JPG, PNG)")
            return

        self.current_file = file_path
        file_name = os.path.basename(file_path)
        self.file_label.config(text=f"📄 {file_name}", fg="black")
        self.process_btn.config(state="normal")
        self.status_var.set(f"File loaded: {file_name}")

    def on_file_drop(self, event):
        """Handle file drop event"""
        # Get dropped file path (tkinterdnd2 returns it in curly braces)
        files = self.root.tk.splitlist(event.data)
        if files:
            file_path = files[0]
            # Remove curly braces if present
            file_path = file_path.strip('{}')
            self.load_file(file_path)

    def on_drag_enter(self, event):
        """Visual feedback when drag enters drop zone"""
        if hasattr(self, 'drop_zone'):
            self.drop_zone.config(bg="#e0f0ff", relief=tk.SOLID, bd=3)

    def on_drag_leave(self, event):
        """Reset visual feedback when drag leaves"""
        if hasattr(self, 'drop_zone'):
            self.drop_zone.config(bg="#f0f8ff", relief=tk.GROOVE, bd=2)

    def process_document(self):
        """Process document in background thread"""
        if not self.current_file:
            messagebox.showwarning("No File", "Please select a file first")
            return

        if self.processing:
            return

        self.processing = True
        self.process_btn.config(state="disabled", text="Processing...")
        self.progress.pack(fill=tk.X, pady=5)
        self.progress.start(10)
        self.results_text.delete(1.0, tk.END)
        self.status_var.set("Processing... Please wait.")

        # Process in background
        thread = threading.Thread(target=self._process_thread, daemon=True)
        thread.start()

    def _process_thread(self):
        """Background processing"""
        try:
            # Step 1: Load analyzer if not loaded
            if not self.analyzer:
                self.update_status("Loading OCR engine...")
                print("[INFO] Importing EnhancedStructureAnalyzer...")

                from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer

                print(f"[INFO] Creating analyzer (GPU={self.gpu_var.get()}, Lang={self.lang_var.get()})...")
                self.analyzer = EnhancedStructureAnalyzer(
                    use_gpu=self.gpu_var.get(),
                    lang=self.lang_var.get()
                )
                print("[INFO] Analyzer created successfully")

            # Step 2: Process document
            self.update_status(f"Processing: {os.path.basename(self.current_file)}")
            print(f"[INFO] Analyzing document: {self.current_file}")

            result = self.analyzer.analyze(self.current_file)

            print(f"[INFO] Analysis complete. Regions found: {len(result.get('regions', []))}")

            # Step 3: Create visualization
            self.create_visualization(result)

            # Step 4: Display results
            self.display_results(result)
            self.update_status("✅ Processing complete!")

        except Exception as e:
            print(f"[ERROR] {e}")
            import traceback
            traceback.print_exc()
            self.show_error(f"Error: {str(e)}")

        finally:
            self.root.after(0, self._processing_complete)

    def create_visualization(self, result):
        """Create annotated image with OCR visualization"""
        try:
            # Load visualizer
            if not self.visualizer:
                from ocr_invoice_reader.utils.visualizer import OCRVisualizer
                self.visualizer = OCRVisualizer()

            # Load original image
            if self.original_image is None:
                self.original_image = cv2.imread(self.current_file)

            # Convert regions to dict format for visualizer
            regions_for_viz = []
            for region in result.get('regions', []):
                region_dict = {
                    'type': region.type,
                    'bbox': region.bbox,
                    'confidence': region.confidence,
                    'text': region.text if hasattr(region, 'text') and region.text else ""
                }

                # Add OCR boxes if available
                if hasattr(region, 'ocr_boxes') and region.ocr_boxes:
                    region_dict['ocr_boxes'] = region.ocr_boxes

                regions_for_viz.append(region_dict)

            # Draw visualization
            self.annotated_image = self.visualizer.visualize_regions(
                self.original_image.copy(),
                regions_for_viz,
                show_text=True,
                show_boxes=True
            )

            print("[INFO] Visualization created successfully")

            # Save visualization to temp file for display
            temp_path = os.path.join(tempfile.gettempdir(), f"ocr_viz_{os.path.basename(self.current_file)}")
            cv2.imwrite(temp_path, self.annotated_image)
            print(f"[INFO] Visualization saved to: {temp_path}")

        except Exception as e:
            print(f"[WARN] Visualization failed: {e}")
            import traceback
            traceback.print_exc()

    def display_results(self, result):
        """Display results in text area"""
        self.root.after(0, lambda: self._display_results_ui(result))

    def _display_results_ui(self, result):
        """Update UI with results"""
        self.results_text.delete(1.0, tk.END)

        # Format and display
        self.results_text.insert(tk.END, "="*80 + "\n")
        self.results_text.insert(tk.END, "OCR RESULTS\n")
        self.results_text.insert(tk.END, "="*80 + "\n\n")

        # Metadata
        if 'metadata' in result:
            self.results_text.insert(tk.END, "METADATA:\n")
            self.results_text.insert(tk.END, "-"*80 + "\n")
            for key, value in result['metadata'].items():
                self.results_text.insert(tk.END, f"{key}: {value}\n")
            self.results_text.insert(tk.END, "\n")

        # Regions
        if 'regions' in result:
            self.results_text.insert(tk.END, f"REGIONS FOUND: {len(result['regions'])}\n")
            self.results_text.insert(tk.END, "-"*80 + "\n\n")

            for i, region in enumerate(result['regions'], 1):
                self.results_text.insert(tk.END, f"Region {i}:\n")
                self.results_text.insert(tk.END, f"  Type: {region.type}\n")
                self.results_text.insert(tk.END, f"  BBox: {region.bbox}\n")
                self.results_text.insert(tk.END, f"  Confidence: {region.confidence:.2%}\n")

                # Display text content if available
                text_content = region.text if hasattr(region, 'text') and region.text else ""
                if text_content:
                    preview = text_content[:200]
                    self.results_text.insert(tk.END, f"  Text: {preview}\n")
                    if len(text_content) > 200:
                        self.results_text.insert(tk.END, "  ...\n")

                self.results_text.insert(tk.END, "\n")

        # Full details (serialize LayoutRegion objects)
        self.results_text.insert(tk.END, "\n" + "="*80 + "\n")
        self.results_text.insert(tk.END, "DETAILED OUTPUT:\n")
        self.results_text.insert(tk.END, "="*80 + "\n")

        # Convert LayoutRegion objects to dicts for JSON serialization
        serializable_result = {
            'method': result.get('method', ''),
            'image_path': result.get('image_path', ''),
            'regions': [
                {
                    'type': r.type,
                    'bbox': r.bbox,
                    'confidence': r.confidence,
                    'text': r.text if hasattr(r, 'text') and r.text else ""
                }
                for r in result.get('regions', [])
            ]
        }

        formatted_json = json.dumps(serializable_result, indent=2, ensure_ascii=False)
        self.results_text.insert(tk.END, formatted_json)

        # Add visualization button
        if self.annotated_image is not None:
            self.results_text.insert(tk.END, "\n\n" + "="*80 + "\n")
            self.results_text.insert(tk.END, "💡 Tip: Visualization image saved! View it in your system's image viewer.\n")
            temp_path = os.path.join(tempfile.gettempdir(), f"ocr_viz_{os.path.basename(result.get('image_path', 'result.jpg'))}")
            self.results_text.insert(tk.END, f"📁 Location: {temp_path}\n")

    def update_status(self, message):
        """Update status bar"""
        self.root.after(0, lambda: self.status_var.set(message))

    def show_error(self, message):
        """Show error message"""
        self.root.after(0, lambda: messagebox.showerror("Error", message))
        self.root.after(0, lambda: self.status_var.set("❌ Error occurred"))

    def _processing_complete(self):
        """Cleanup after processing"""
        self.processing = False
        self.process_btn.config(state="normal", text="3. 🚀 Process Document")
        self.progress.stop()
        self.progress.pack_forget()

def main():
    """Main entry point"""
    # Use TkinterDnD if available for drag-and-drop support
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()

    app = SimpleOCRGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
