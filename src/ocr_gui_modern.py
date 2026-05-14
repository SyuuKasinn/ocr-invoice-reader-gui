#!/usr/bin/env python3
"""
OCR Invoice Reader - Modern GUI
Beautiful, professional desktop application with PaddleOCR v4
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
import os
import sys
import json
import threading
from pathlib import Path
from PIL import Image, ImageTk
import tempfile
from datetime import datetime


# Modern color scheme
class Theme:
    # Primary colors
    PRIMARY = "#6366f1"  # Indigo
    PRIMARY_DARK = "#4f46e5"
    PRIMARY_LIGHT = "#818cf8"

    # Background colors
    BG_DARK = "#1e1b4b"  # Dark indigo
    BG_MEDIUM = "#312e81"
    BG_LIGHT = "#3730a3"
    BG_CARD = "#ffffff"

    # Text colors
    TEXT_PRIMARY = "#1e293b"
    TEXT_SECONDARY = "#64748b"
    TEXT_LIGHT = "#f1f5f9"

    # Accent colors
    SUCCESS = "#10b981"  # Green
    WARNING = "#f59e0b"  # Amber
    ERROR = "#ef4444"    # Red
    INFO = "#3b82f6"     # Blue

    # UI elements
    BORDER = "#e2e8f0"
    SHADOW = "#0f172a20"


class ModernSplash:
    """Modern loading splash screen"""
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("OCR Invoice Reader")
        self.root.overrideredirect(True)

        # Window setup
        width, height = 600, 400
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

        # Modern gradient background
        self.canvas = tk.Canvas(
            self.root,
            width=width,
            height=height,
            bg=Theme.BG_DARK,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Logo/Icon
        self.canvas.create_text(
            300, 120,
            text="📄",
            font=('Segoe UI Emoji', 72),
            fill=Theme.PRIMARY_LIGHT
        )

        # App title
        self.canvas.create_text(
            300, 200,
            text="OCR Invoice Reader",
            font=('Segoe UI', 28, 'bold'),
            fill=Theme.TEXT_LIGHT
        )

        # Version
        self.canvas.create_text(
            300, 240,
            text="v2.1.0 - Powered by PaddleOCR v4",
            font=('Segoe UI', 11),
            fill=Theme.PRIMARY_LIGHT
        )

        # Status text
        self.status_text = self.canvas.create_text(
            300, 300,
            text="Loading OCR engine...",
            font=('Segoe UI', 12),
            fill=Theme.TEXT_LIGHT
        )

        # Modern progress bar
        self.progress_bg = self.canvas.create_rectangle(
            150, 320, 450, 330,
            fill=Theme.BG_MEDIUM,
            outline=""
        )
        self.progress_bar = self.canvas.create_rectangle(
            150, 320, 150, 330,
            fill=Theme.PRIMARY,
            outline=""
        )

        # Animate progress
        self.progress_width = 0
        self.animation_id = None
        self._animate()

    def _animate(self):
        """Animate the progress bar"""
        try:
            if self.progress_width < 300:
                self.progress_width += 3
                self.canvas.coords(
                    self.progress_bar,
                    150, 320, 150 + self.progress_width, 330
                )
                self.animation_id = self.root.after(20, self._animate)
            else:
                # Loop back
                self.progress_width = 0
                self.animation_id = self.root.after(20, self._animate)
        except tk.TclError:
            # Widget destroyed, stop animation
            pass

    def update_status(self, message):
        """Update status message"""
        self.canvas.itemconfig(self.status_text, text=message)
        self.root.update()

    def destroy(self):
        """Close splash screen"""
        try:
            if hasattr(self, 'animation_id') and self.animation_id:
                self.root.after_cancel(self.animation_id)
        except:
            pass
        self.root.destroy()


class ModernOCRGUI:
    """Modern OCR Invoice Reader GUI"""

    def __init__(self, root, ocr_analyzer=None):
        self.root = root
        self.root.title("OCR Invoice Reader")
        self.root.geometry("1400x900")
        self.root.minsize(1000, 700)

        # Configure modern styling
        self.setup_styles()

        # Pre-loaded OCR analyzer
        self.ocr_analyzer = ocr_analyzer

        # State
        self.current_file = None
        self.current_result = None
        self.processing = False

        # Build UI
        self.create_ui()

    def setup_styles(self):
        """Configure modern ttk styles"""
        style = ttk.Style()
        style.theme_use('clam')

        # Configure modern button style
        style.configure(
            'Primary.TButton',
            background=Theme.PRIMARY,
            foreground='white',
            borderwidth=0,
            focuscolor='none',
            padding=(20, 12),
            font=('Segoe UI', 10, 'bold')
        )
        style.map('Primary.TButton',
            background=[('active', Theme.PRIMARY_DARK)]
        )

        # Secondary button
        style.configure(
            'Secondary.TButton',
            background=Theme.BG_CARD,
            foreground=Theme.TEXT_PRIMARY,
            borderwidth=1,
            focuscolor='none',
            padding=(15, 10),
            font=('Segoe UI', 9)
        )

        # Modern frame
        style.configure(
            'Card.TFrame',
            background=Theme.BG_CARD,
            relief='flat'
        )

        # Configure notebook (tabs)
        style.configure(
            'Modern.TNotebook',
            background=Theme.BG_CARD,
            borderwidth=0
        )
        style.configure(
            'Modern.TNotebook.Tab',
            background=Theme.BG_CARD,
            foreground=Theme.TEXT_SECONDARY,
            padding=(20, 12),
            font=('Segoe UI', 10)
        )
        style.map('Modern.TNotebook.Tab',
            background=[('selected', Theme.BG_CARD)],
            foreground=[('selected', Theme.PRIMARY)],
            expand=[('selected', [1, 1, 1, 0])]
        )

    def create_ui(self):
        """Create the main UI"""
        # Set background
        self.root.configure(bg='#f8fafc')

        # Header
        self.create_header()

        # Main content area
        main_frame = tk.Frame(self.root, bg='#f8fafc')
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Split view: Upload on left, Results on right
        paned = tk.PanedWindow(
            main_frame,
            orient=tk.HORIZONTAL,
            sashwidth=8,
            bg='#e2e8f0',
            bd=0
        )
        paned.pack(fill=tk.BOTH, expand=True)

        # Left panel - Upload & Settings
        left_panel = self.create_left_panel(paned)
        paned.add(left_panel, width=450)

        # Right panel - Results
        right_panel = self.create_right_panel(paned)
        paned.add(right_panel)

        # Status bar
        self.create_status_bar()

    def create_header(self):
        """Create modern header"""
        header = tk.Frame(self.root, bg=Theme.BG_DARK, height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)

        # Left side - Logo and title
        left_frame = tk.Frame(header, bg=Theme.BG_DARK)
        left_frame.pack(side=tk.LEFT, padx=30, pady=15)

        # Icon
        icon_label = tk.Label(
            left_frame,
            text="📄",
            font=('Segoe UI Emoji', 32),
            bg=Theme.BG_DARK,
            fg=Theme.PRIMARY_LIGHT
        )
        icon_label.pack(side=tk.LEFT, padx=(0, 15))

        # Title and subtitle
        title_frame = tk.Frame(left_frame, bg=Theme.BG_DARK)
        title_frame.pack(side=tk.LEFT)

        title = tk.Label(
            title_frame,
            text="OCR Invoice Reader",
            font=('Segoe UI', 18, 'bold'),
            bg=Theme.BG_DARK,
            fg=Theme.TEXT_LIGHT
        )
        title.pack(anchor=tk.W)

        subtitle = tk.Label(
            title_frame,
            text="Powered by PaddleOCR v4 • 30% Faster",
            font=('Segoe UI', 9),
            bg=Theme.BG_DARK,
            fg=Theme.PRIMARY_LIGHT
        )
        subtitle.pack(anchor=tk.W)

        # Right side - Status indicator
        right_frame = tk.Frame(header, bg=Theme.BG_DARK)
        right_frame.pack(side=tk.RIGHT, padx=30)

        status_indicator = tk.Label(
            right_frame,
            text="● Ready" if self.ocr_analyzer else "○ Not Loaded",
            font=('Segoe UI', 11),
            bg=Theme.BG_DARK,
            fg=Theme.SUCCESS if self.ocr_analyzer else Theme.WARNING
        )
        status_indicator.pack()

    def create_left_panel(self, parent):
        """Create left panel with upload area"""
        panel = tk.Frame(parent, bg='#f8fafc')

        # Upload card
        upload_card = tk.Frame(
            panel,
            bg=Theme.BG_CARD,
            relief='flat',
            bd=0
        )
        upload_card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add shadow effect
        self.add_shadow(upload_card)

        # Card title
        title = tk.Label(
            upload_card,
            text="Upload Document",
            font=('Segoe UI', 16, 'bold'),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_PRIMARY
        )
        title.pack(pady=(20, 10), padx=20, anchor=tk.W)

        # Drop zone
        self.create_drop_zone(upload_card)

        # Settings section
        self.create_settings_section(upload_card)

        # Process button
        self.process_btn = tk.Button(
            upload_card,
            text="🚀 Process Document",
            font=('Segoe UI', 13, 'bold'),
            bg=Theme.PRIMARY,
            fg='#FFFFFF',  # Pure white for better contrast
            activebackground=Theme.PRIMARY_DARK,
            activeforeground='#FFFFFF',
            disabledforeground='#94a3b8',  # Light gray when disabled
            relief='flat',
            bd=0,
            padx=30,
            pady=15,
            cursor='hand2',
            state='disabled',
            command=self.process_document
        )
        self.process_btn.pack(pady=20, padx=20, fill=tk.X)

        return panel

    def create_drop_zone(self, parent):
        """Create modern drop zone"""
        drop_frame = tk.Frame(
            parent,
            bg='#f8fafc',
            relief='flat'
        )
        drop_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Drop zone with dashed border
        self.drop_zone = tk.Text(
            drop_frame,
            height=10,
            wrap=tk.WORD,
            bg='#f8fafc',
            fg=Theme.TEXT_SECONDARY,
            font=('Segoe UI', 11),
            relief='flat',
            bd=2,
            highlightthickness=2,
            highlightbackground=Theme.BORDER,
            highlightcolor=Theme.PRIMARY,
            cursor='hand2'
        )
        self.drop_zone.pack(fill=tk.BOTH, expand=True)

        # Placeholder text
        self.drop_zone.insert('1.0',
            "\n\n"
            "         🎯 Drag & Drop Your Document\n\n"
            "         or click to browse\n\n\n"
            "         Supported formats:\n"
            "         • PDF documents\n"
            "         • Images (JPG, PNG)\n"
        )
        self.drop_zone.configure(state='disabled')
        self.drop_zone.tag_configure('center', justify='center')
        self.drop_zone.tag_add('center', '1.0', 'end')

        # Drag and drop binding
        self.drop_zone.drop_target_register(DND_FILES)
        self.drop_zone.dnd_bind('<<Drop>>', self.on_drop)
        self.drop_zone.bind('<Button-1>', lambda e: self.browse_file())

    def create_settings_section(self, parent):
        """Create settings section"""
        settings_frame = tk.Frame(parent, bg=Theme.BG_CARD)
        settings_frame.pack(fill=tk.X, padx=20, pady=10)

        # Settings title
        title = tk.Label(
            settings_frame,
            text="Settings",
            font=('Segoe UI', 12, 'bold'),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_PRIMARY
        )
        title.pack(anchor=tk.W, pady=(10, 10))

        # Language
        lang_frame = tk.Frame(settings_frame, bg=Theme.BG_CARD)
        lang_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            lang_frame,
            text="Language:",
            font=('Segoe UI', 10),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_SECONDARY
        ).pack(side=tk.LEFT)

        self.lang_var = tk.StringVar(value="ch")
        lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.lang_var,
            values=["ch", "en", "japan", "korean"],
            state="readonly",
            width=15,
            font=('Segoe UI', 10)
        )
        lang_combo.pack(side=tk.RIGHT)

        # Mode
        mode_frame = tk.Frame(settings_frame, bg=Theme.BG_CARD)
        mode_frame.pack(fill=tk.X, pady=5)

        tk.Label(
            mode_frame,
            text="Mode:",
            font=('Segoe UI', 10),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_SECONDARY
        ).pack(side=tk.LEFT)

        self.mode_var = tk.StringVar(value="ocr-enhanced")
        mode_combo = ttk.Combobox(
            mode_frame,
            textvariable=self.mode_var,
            values=["ocr-simple", "ocr-extract", "ocr-enhanced"],
            state="readonly",
            width=15,
            font=('Segoe UI', 10)
        )
        mode_combo.pack(side=tk.RIGHT)

        # GPU checkbox
        self.use_gpu_var = tk.BooleanVar(value=False)
        gpu_check = tk.Checkbutton(
            settings_frame,
            text="🚀 Use GPU Acceleration (if available)",
            variable=self.use_gpu_var,
            font=('Segoe UI', 10),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_SECONDARY,
            activebackground=Theme.BG_CARD,
            selectcolor=Theme.BG_CARD,
            bd=0,
            highlightthickness=0
        )
        gpu_check.pack(anchor=tk.W, pady=10)

        # Visualize checkbox
        self.visualize_var = tk.BooleanVar(value=True)
        viz_check = tk.Checkbutton(
            settings_frame,
            text="📊 Generate visualization",
            variable=self.visualize_var,
            font=('Segoe UI', 10),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_SECONDARY,
            activebackground=Theme.BG_CARD,
            selectcolor=Theme.BG_CARD,
            bd=0,
            highlightthickness=0
        )
        viz_check.pack(anchor=tk.W, pady=5)

    def create_right_panel(self, parent):
        """Create right panel with results"""
        panel = tk.Frame(parent, bg='#f8fafc')

        # Results card
        results_card = tk.Frame(
            panel,
            bg=Theme.BG_CARD,
            relief='flat'
        )
        results_card.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add shadow
        self.add_shadow(results_card)

        # Card title
        title = tk.Label(
            results_card,
            text="Results",
            font=('Segoe UI', 16, 'bold'),
            bg=Theme.BG_CARD,
            fg=Theme.TEXT_PRIMARY
        )
        title.pack(pady=(20, 10), padx=20, anchor=tk.W)

        # Notebook for tabs
        self.notebook = ttk.Notebook(results_card, style='Modern.TNotebook')
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))

        # Tab: Visualization
        self.create_viz_tab()

        # Tab: Structured Data
        self.create_data_tab()

        # Tab: Text
        self.create_text_tab()

        # Tab: Tables
        self.create_tables_tab()

        return panel

    def create_viz_tab(self):
        """Create visualization tab"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="📊 Visualization")

        # Scrollable canvas
        canvas_frame = tk.Frame(tab, bg='white')
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        v_scroll = tk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        h_scroll = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)

        self.viz_canvas = tk.Canvas(
            canvas_frame,
            bg='white',
            yscrollcommand=v_scroll.set,
            xscrollcommand=h_scroll.set
        )

        v_scroll.config(command=self.viz_canvas.yview)
        h_scroll.config(command=self.viz_canvas.xview)

        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.viz_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def create_data_tab(self):
        """Create structured data tab"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="📋 Structured Data")

        self.data_text = tk.Text(
            tab,
            wrap=tk.WORD,
            font=('Consolas', 10),
            bg='#f8fafc',
            fg=Theme.TEXT_PRIMARY,
            padx=15,
            pady=15,
            relief='flat'
        )
        self.data_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add scrollbar
        scrollbar = tk.Scrollbar(self.data_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.data_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.data_text.yview)

    def create_text_tab(self):
        """Create extracted text tab"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="📝 Extracted Text")

        self.text_display = tk.Text(
            tab,
            wrap=tk.WORD,
            font=('Segoe UI', 11),
            bg='#f8fafc',
            fg=Theme.TEXT_PRIMARY,
            padx=15,
            pady=15,
            relief='flat'
        )
        self.text_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add scrollbar
        scrollbar = tk.Scrollbar(self.text_display)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_display.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_display.yview)

    def create_tables_tab(self):
        """Create tables tab"""
        tab = tk.Frame(self.notebook, bg='white')
        self.notebook.add(tab, text="🔢 Tables")

        self.tables_text = tk.Text(
            tab,
            wrap=tk.WORD,
            font=('Consolas', 9),
            bg='#f8fafc',
            fg=Theme.TEXT_PRIMARY,
            padx=15,
            pady=15,
            relief='flat'
        )
        self.tables_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Add scrollbar
        scrollbar = tk.Scrollbar(self.tables_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tables_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.tables_text.yview)

    def create_status_bar(self):
        """Create modern status bar"""
        self.status_bar = tk.Frame(
            self.root,
            bg='white',
            height=40,
            relief='flat'
        )
        self.status_bar.pack(fill=tk.X, side=tk.BOTTOM)
        self.status_bar.pack_propagate(False)

        # Status text
        self.status_var = tk.StringVar(
            value="⚡ Ready! First scan loads OCR (~10s), then 5x faster (2-3s)!"
        )
        status_label = tk.Label(
            self.status_bar,
            textvariable=self.status_var,
            font=('Segoe UI', 9),
            bg='white',
            fg=Theme.TEXT_SECONDARY,
            anchor=tk.W
        )
        status_label.pack(side=tk.LEFT, padx=20)

        # Progress indicator (hidden by default)
        self.progress = ttk.Progressbar(
            self.status_bar,
            mode='indeterminate',
            length=200
        )

    def add_shadow(self, widget):
        """Add shadow effect to widget"""
        # This is a visual hint - actual shadow would need custom rendering
        widget.configure(relief='flat', bd=1, highlightthickness=1, highlightbackground='#e2e8f0')

    def on_drop(self, event):
        """Handle file drop"""
        files = self.root.tk.splitlist(event.data)
        if files:
            file_path = files[0].strip('{}')
            self.load_file(file_path)

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
        """Load file"""
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "File not found!")
            return

        ext = Path(file_path).suffix.lower()
        if ext not in ['.pdf', '.jpg', '.jpeg', '.png']:
            messagebox.showerror("Error", "Unsupported file format!")
            return

        self.current_file = file_path
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path) / 1024  # KB

        # Update drop zone
        self.drop_zone.configure(state='normal')
        self.drop_zone.delete('1.0', tk.END)
        self.drop_zone.insert('1.0',
            f"\n\n"
            f"         ✅ File Loaded\n\n"
            f"         📄 {file_name}\n"
            f"         📦 {file_size:.1f} KB\n\n"
            f"         Click 'Process Document' to start"
        )
        self.drop_zone.tag_add('center', '1.0', 'end')
        self.drop_zone.configure(state='disabled')

        # Enable process button
        self.process_btn.configure(state='normal', cursor='hand2')
        self.status_var.set(f"📄 File loaded: {file_name}")

    def process_document(self):
        """Process document with OCR"""
        if not self.current_file:
            messagebox.showwarning("Warning", "Please load a file first!")
            return

        if self.processing:
            return

        self.processing = True
        self.process_btn.configure(state='disabled', text="⏳ Processing...")
        self.progress.pack(side=tk.RIGHT, padx=20)
        self.progress.start(10)
        self.status_var.set("⚡ Processing with PaddleOCR v4...")

        # Process in background thread
        thread = threading.Thread(target=self._process_thread, daemon=True)
        thread.start()

    def _process_thread(self):
        """Background processing thread"""
        try:
            if self.ocr_analyzer:
                # Use pre-loaded analyzer (fast!)
                # Extract from document
                document = self.ocr_analyzer.extract(
                    self.current_file,
                    visualize=self.visualize_var.get()
                )

                # Convert to dict for display
                result = document.model_dump() if hasattr(document, 'model_dump') else document.__dict__

                self.current_result = result
                self.root.after(0, self._display_results, result)
            else:
                # Try to load analyzer now if not pre-loaded
                self.root.after(0, lambda: self.status_var.set("⚠️ Loading OCR engine..."))
                try:
                    from ocr_invoice_reader import DocumentExtractor

                    lang = self.lang_var.get()
                    self.ocr_analyzer = DocumentExtractor(
                        use_gpu=self.use_gpu_var.get(),
                        lang=lang
                    )

                    # Now process with newly loaded analyzer
                    document = self.ocr_analyzer.extract(
                        self.current_file,
                        visualize=self.visualize_var.get()
                    )

                    # Convert to dict for display
                    result = document.model_dump() if hasattr(document, 'model_dump') else document.__dict__

                    self.current_result = result
                    self.root.after(0, self._display_results, result)
                except Exception as load_error:
                    error_msg = f"Failed to load OCR engine: {load_error}"
                    self.root.after(0, lambda msg=error_msg: self._show_error(msg))

        except Exception as e:
            error_msg = str(e)
            import traceback
            traceback.print_exc()
            self.root.after(0, lambda msg=error_msg: self._show_error(msg))
        finally:
            self.root.after(0, self._processing_complete)

    # Removed _process_cli() - now always use pre-loaded analyzer for better performance

    def _display_results(self, result):
        """Display OCR results"""
        # Display structured data
        self.data_text.delete('1.0', tk.END)
        formatted = json.dumps(result, indent=2, ensure_ascii=False)
        self.data_text.insert('1.0', formatted)

        # Display extracted text
        self.text_display.delete('1.0', tk.END)
        if 'text' in result:
            self.text_display.insert('1.0', result['text'])
        elif 'regions' in result:
            text = '\n\n'.join(r.get('text', '') for r in result['regions'])
            self.text_display.insert('1.0', text)

        self.status_var.set("✅ Processing complete!")

    def _display_cli_results(self, result_dir):
        """Display results from CLI mode"""
        # Find and display files
        json_files = list(result_dir.glob("*.json"))
        if json_files:
            with open(json_files[0], 'r', encoding='utf-8') as f:
                data = json.load(f)
                formatted = json.dumps(data, indent=2, ensure_ascii=False)
                self.data_text.delete('1.0', tk.END)
                self.data_text.insert('1.0', formatted)

        txt_files = list(result_dir.glob("*_all_pages.txt"))
        if txt_files:
            with open(txt_files[0], 'r', encoding='utf-8') as f:
                text = f.read()
                self.text_display.delete('1.0', tk.END)
                self.text_display.insert('1.0', text)

        viz_files = list(result_dir.glob("*_viz.jpg"))
        if viz_files:
            self._display_image(viz_files[0])

        self.status_var.set("✅ Processing complete!")

    def _display_image(self, image_path):
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

    def _show_error(self, error_msg):
        """Show error dialog"""
        messagebox.showerror("Error", f"Processing failed:\n\n{error_msg}")
        self.status_var.set("❌ Error occurred")

    def _processing_complete(self):
        """Cleanup after processing"""
        self.processing = False
        self.process_btn.configure(state='normal', text="🚀 Process Document", cursor='hand2')
        self.progress.stop()
        self.progress.pack_forget()


def load_ocr_engine(splash):
    """Load OCR engine with splash screen - Always attempt to pre-load for 5x faster performance"""
    import time

    try:
        splash.update_status("Loading OCR modules...")
        time.sleep(0.2)

        # Import from ocr-invoice-reader
        from ocr_invoice_reader import DocumentExtractor

        splash.update_status("Initializing PaddleOCR engine...")
        time.sleep(0.2)

        # Initialize document extractor with CPU by default
        extractor = DocumentExtractor(use_gpu=False, lang='ch')

        splash.update_status("✅ OCR engine ready! (Pre-loaded)")
        time.sleep(0.3)
        return extractor

    except ImportError as ie:
        splash.update_status("⚠️ OCR library not found, will load on-demand...")
        print(f"Import error: {ie}")
        print(f"Full error: {ie.__class__.__name__}: {ie}")
        time.sleep(1)
        return None
    except Exception as e:
        splash.update_status(f"⚠️ Engine load error, will retry on first use")
        print(f"Error loading OCR: {e}")
        print(f"Full error: {e.__class__.__name__}: {e}")
        import traceback
        traceback.print_exc()
        time.sleep(1)
        return None


def main():
    """Main entry point"""
    # Show splash screen
    splash = ModernSplash()
    splash.root.update()

    # DON'T load OCR engine at startup - load on-demand to avoid packaging issues
    splash.update_status("Ready! OCR engine will load on first use...")
    import time
    time.sleep(0.5)

    # Close splash
    splash.destroy()

    # Create main window
    try:
        root = TkinterDnD.Tk()
    except Exception:
        messagebox.showerror(
            "Missing Dependency",
            "TkinterDnD2 is required.\nInstall: pip install tkinterdnd2"
        )
        return

    # Pass None - will load on first use
    app = ModernOCRGUI(root, None)
    root.mainloop()


if __name__ == "__main__":
    main()
