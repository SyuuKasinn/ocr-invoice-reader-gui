#!/usr/bin/env python3
"""
OCR Invoice Reader GUI
A drag-and-drop interface for OCR invoice processing with real-time visualization
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import sys
import json
import subprocess
import threading
from pathlib import Path
from PIL import Image, ImageTk
import tempfile

class OCRInvoiceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Invoice Reader - Drag & Drop Interface")
        self.root.geometry("1200x800")

        # Set minimum window size
        self.root.minsize(800, 600)

        # Current processing info
        self.current_file = None
        self.current_result_dir = None

        # Create UI
        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface"""
        # Main container
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="🖼️ OCR Invoice Reader",
            font=("Arial", 20, "bold")
        )
        title_label.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)

        # Create paned window for split view
        paned = ttk.PanedWindow(main_frame, orient=tk.HORIZONTAL)
        paned.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Left panel - Drop zone and controls
        left_panel = ttk.Frame(paned, padding="5")
        paned.add(left_panel, weight=1)

        # Right panel - Results display
        right_panel = ttk.Frame(paned, padding="5")
        paned.add(right_panel, weight=2)

        # Setup left panel
        self.setup_left_panel(left_panel)

        # Setup right panel
        self.setup_right_panel(right_panel)

        # Status bar
        self.status_var = tk.StringVar(value="Ready. Drag & drop a PDF or image file to start.")
        status_bar = ttk.Label(
            main_frame,
            textvariable=self.status_var,
            relief=tk.SUNKEN,
            anchor=tk.W
        )
        status_bar.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(5, 0))

    def setup_left_panel(self, parent):
        """Setup left panel with drop zone and controls"""
        # Drop zone
        drop_frame = ttk.LabelFrame(parent, text="📥 Drop Zone", padding="10")
        drop_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        # Drop area
        self.drop_area = tk.Text(
            drop_frame,
            height=8,
            wrap=tk.WORD,
            background="#f0f0f0",
            font=("Arial", 11),
            relief=tk.SOLID,
            borderwidth=2
        )
        self.drop_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        drop_frame.rowconfigure(0, weight=1)
        drop_frame.columnconfigure(0, weight=1)

        # Initial message
        self.drop_area.insert("1.0",
            "🎯 Drag & Drop Files Here\n\n"
            "Supported formats:\n"
            "• PDF documents (.pdf)\n"
            "• Images (.jpg, .png, .jpeg)\n\n"
            "Or click 'Browse' button below"
        )
        self.drop_area.configure(state="disabled")

        # Enable drag and drop
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind('<<Drop>>', self.on_drop)

        # Browse button
        browse_btn = ttk.Button(
            drop_frame,
            text="📁 Browse Files",
            command=self.browse_file
        )
        browse_btn.grid(row=1, column=0, pady=(10, 0))

        # Settings frame
        settings_frame = ttk.LabelFrame(parent, text="⚙️ Settings", padding="10")
        settings_frame.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Language selection
        ttk.Label(settings_frame, text="Language:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.lang_var = tk.StringVar(value="ch")
        lang_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.lang_var,
            values=["ch", "en", "japan", "korean"],
            state="readonly",
            width=15
        )
        lang_combo.grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=2)

        # OCR mode selection
        ttk.Label(settings_frame, text="Mode:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.mode_var = tk.StringVar(value="ocr-enhanced")
        mode_combo = ttk.Combobox(
            settings_frame,
            textvariable=self.mode_var,
            values=["ocr-enhanced", "ocr-extract", "ocr-raw", "ocr-simple"],
            state="readonly",
            width=15
        )
        mode_combo.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=2)

        # Use GPU checkbox
        self.use_gpu_var = tk.BooleanVar(value=False)
        gpu_check = ttk.Checkbutton(
            settings_frame,
            text="Use GPU (if available)",
            variable=self.use_gpu_var
        )
        gpu_check.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Process button
        self.process_btn = ttk.Button(
            parent,
            text="🚀 Process Document",
            command=self.process_document,
            state="disabled"
        )
        self.process_btn.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

        # Progress bar
        self.progress = ttk.Progressbar(parent, mode='indeterminate')
        self.progress.grid(row=3, column=0, sticky=(tk.W, tk.E))

    def setup_right_panel(self, parent):
        """Setup right panel for results display"""
        # Notebook for tabs
        self.notebook = ttk.Notebook(parent)
        self.notebook.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

        # Tab 1: Visualization
        viz_frame = ttk.Frame(self.notebook)
        self.notebook.add(viz_frame, text="📊 Visualization")

        # Image display with scrollbar
        viz_scroll_frame = ttk.Frame(viz_frame)
        viz_scroll_frame.pack(fill=tk.BOTH, expand=True)

        v_scrollbar = ttk.Scrollbar(viz_scroll_frame, orient=tk.VERTICAL)
        h_scrollbar = ttk.Scrollbar(viz_scroll_frame, orient=tk.HORIZONTAL)

        self.viz_canvas = tk.Canvas(
            viz_scroll_frame,
            yscrollcommand=v_scrollbar.set,
            xscrollcommand=h_scrollbar.set,
            background="#ffffff"
        )

        v_scrollbar.config(command=self.viz_canvas.yview)
        h_scrollbar.config(command=self.viz_canvas.xview)

        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.viz_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Tab 2: JSON Data
        json_frame = ttk.Frame(self.notebook)
        self.notebook.add(json_frame, text="📋 JSON Data")

        self.json_text = scrolledtext.ScrolledText(
            json_frame,
            wrap=tk.WORD,
            font=("Courier", 10)
        )
        self.json_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tab 3: Extracted Text
        text_frame = ttk.Frame(self.notebook)
        self.notebook.add(text_frame, text="📝 Extracted Text")

        self.text_display = scrolledtext.ScrolledText(
            text_frame,
            wrap=tk.WORD,
            font=("Arial", 10)
        )
        self.text_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Tab 4: HTML Tables
        html_frame = ttk.Frame(self.notebook)
        self.notebook.add(html_frame, text="🔢 Tables")

        self.html_text = scrolledtext.ScrolledText(
            html_frame,
            wrap=tk.WORD,
            font=("Courier", 9)
        )
        self.html_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def on_drop(self, event):
        """Handle file drop event"""
        files = self.root.tk.splitlist(event.data)
        if files:
            file_path = files[0].strip('{}')
            self.load_file(file_path)

    def browse_file(self):
        """Browse for file"""
        file_path = filedialog.askopenfilename(
            title="Select Invoice or Document",
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
        """Load and display file info"""
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "File not found!")
            return

        # Validate file type
        ext = Path(file_path).suffix.lower()
        if ext not in ['.pdf', '.jpg', '.jpeg', '.png']:
            messagebox.showerror("Error", "Unsupported file format!\nPlease use PDF or image files.")
            return

        self.current_file = file_path
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path) / 1024  # KB

        # Update drop area
        self.drop_area.configure(state="normal")
        self.drop_area.delete("1.0", tk.END)
        self.drop_area.insert("1.0",
            f"✅ File Loaded\n\n"
            f"📄 Name: {file_name}\n"
            f"📦 Size: {file_size:.1f} KB\n"
            f"📂 Path: {file_path}\n\n"
            f"Ready to process!"
        )
        self.drop_area.configure(state="disabled")

        # Enable process button
        self.process_btn.configure(state="normal")
        self.status_var.set(f"File loaded: {file_name}")

    def process_document(self):
        """Process the document with OCR"""
        if not self.current_file:
            messagebox.showwarning("Warning", "Please load a file first!")
            return

        # Start processing in background thread
        self.process_btn.configure(state="disabled")
        self.progress.start(10)
        self.status_var.set("Processing... Please wait.")

        thread = threading.Thread(target=self._process_thread, daemon=True)
        thread.start()

    def _process_thread(self):
        """Background thread for OCR processing"""
        try:
            # Build command
            mode = self.mode_var.get()
            lang = self.lang_var.get()
            use_gpu = self.use_gpu_var.get()

            # Create temp output directory
            output_dir = tempfile.mkdtemp(prefix="ocr_result_")

            cmd = [
                mode,
                "--image", self.current_file,
                "--lang", lang,
                "--output-dir", output_dir,
                "--visualize"
            ]

            if not use_gpu:
                cmd.append("--use-cpu")

            # Run OCR command
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                cwd=Path(__file__).parent
            )

            if result.returncode != 0:
                self.root.after(0, lambda: self._show_error(result.stderr))
                return

            # Find result directory
            result_dirs = [d for d in Path(output_dir).iterdir() if d.is_dir()]
            if not result_dirs:
                self.root.after(0, lambda: self._show_error("No results generated"))
                return

            self.current_result_dir = result_dirs[0]

            # Load and display results
            self.root.after(0, self._display_results)

        except Exception as e:
            self.root.after(0, lambda: self._show_error(str(e)))
        finally:
            self.root.after(0, self._processing_complete)

    def _display_results(self):
        """Display OCR results in UI"""
        if not self.current_result_dir or not self.current_result_dir.exists():
            return

        # Load visualization image
        viz_files = list(self.current_result_dir.glob("*_viz.jpg"))
        if viz_files:
            self._display_visualization(viz_files[0])

        # Load JSON data
        json_files = list(self.current_result_dir.glob("*.json"))
        if json_files:
            self._display_json(json_files[0])

        # Load extracted text
        txt_files = list(self.current_result_dir.glob("*_all_pages.txt"))
        if txt_files:
            self._display_text(txt_files[0])

        # Load HTML tables
        html_files = list(self.current_result_dir.glob("*.html"))
        if html_files:
            self._display_html(html_files[0])

        self.status_var.set(f"✅ Processing complete! Results: {self.current_result_dir}")

    def _display_visualization(self, image_path):
        """Display visualization image"""
        try:
            img = Image.open(image_path)
            # Resize if too large
            max_width = 1000
            if img.width > max_width:
                ratio = max_width / img.width
                new_size = (max_width, int(img.height * ratio))
                img = img.resize(new_size, Image.LANCZOS)

            self.viz_photo = ImageTk.PhotoImage(img)
            self.viz_canvas.delete("all")
            self.viz_canvas.create_image(0, 0, anchor=tk.NW, image=self.viz_photo)
            self.viz_canvas.configure(scrollregion=self.viz_canvas.bbox("all"))
        except Exception as e:
            print(f"Error displaying image: {e}")

    def _display_json(self, json_path):
        """Display JSON data"""
        try:
            with open(json_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            formatted = json.dumps(data, indent=2, ensure_ascii=False)
            self.json_text.delete("1.0", tk.END)
            self.json_text.insert("1.0", formatted)
        except Exception as e:
            self.json_text.delete("1.0", tk.END)
            self.json_text.insert("1.0", f"Error loading JSON: {e}")

    def _display_text(self, text_path):
        """Display extracted text"""
        try:
            with open(text_path, 'r', encoding='utf-8') as f:
                text = f.read()
            self.text_display.delete("1.0", tk.END)
            self.text_display.insert("1.0", text)
        except Exception as e:
            self.text_display.delete("1.0", tk.END)
            self.text_display.insert("1.0", f"Error loading text: {e}")

    def _display_html(self, html_path):
        """Display HTML tables"""
        try:
            with open(html_path, 'r', encoding='utf-8') as f:
                html = f.read()
            self.html_text.delete("1.0", tk.END)
            self.html_text.insert("1.0", html)
        except Exception as e:
            self.html_text.delete("1.0", tk.END)
            self.html_text.insert("1.0", f"Error loading HTML: {e}")

    def _show_error(self, error_msg):
        """Show error message"""
        messagebox.showerror("Processing Error", f"An error occurred:\n\n{error_msg}")
        self.status_var.set("Error occurred during processing.")

    def _processing_complete(self):
        """Clean up after processing"""
        self.progress.stop()
        self.process_btn.configure(state="normal")

def main():
    """Main entry point"""
    try:
        root = TkinterDnD.Tk()
    except Exception:
        # Fallback to regular Tk if TkinterDnD not available
        messagebox.showerror(
            "Missing Dependency",
            "TkinterDnD2 is required for drag-and-drop functionality.\n"
            "Install it with: pip install tkinterdnd2"
        )
        return

    app = OCRInvoiceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
