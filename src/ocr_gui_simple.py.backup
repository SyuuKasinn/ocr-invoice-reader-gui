#!/usr/bin/env python3
"""
Simple OCR Invoice Reader GUI
A minimal, reliable GUI for ocr-invoice-reader

Uses EnhancedStructureAnalyzer directly from ocr-invoice-reader package
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
import threading
import json
from pathlib import Path
from datetime import datetime

class SimpleOCRGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Invoice Reader - Simple Edition")
        self.root.geometry("900x700")

        # State
        self.current_file = None
        self.analyzer = None
        self.processing = False

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

        self.file_label = tk.Label(
            file_frame,
            text="No file selected",
            fg="gray",
            wraplength=700
        )
        self.file_label.pack(side=tk.LEFT, padx=5)

        browse_btn = ttk.Button(
            file_frame,
            text="Browse...",
            command=self.browse_file
        )
        browse_btn.pack(side=tk.RIGHT, padx=5)

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
            self.current_file = file_path
            file_name = os.path.basename(file_path)
            self.file_label.config(text=f"📄 {file_name}", fg="black")
            self.process_btn.config(state="normal")
            self.status_var.set(f"File loaded: {file_name}")

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

            # Step 3: Display results
            self.display_results(result)
            self.update_status("✅ Processing complete!")

        except Exception as e:
            print(f"[ERROR] {e}")
            import traceback
            traceback.print_exc()
            self.show_error(f"Error: {str(e)}")

        finally:
            self.root.after(0, self._processing_complete)

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
    root = tk.Tk()
    app = SimpleOCRGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
