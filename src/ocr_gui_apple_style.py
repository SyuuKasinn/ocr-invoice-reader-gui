#!/usr/bin/env python3
"""
OCR Invoice Reader - Apple Style
Clean, minimalist interface with integrated image visualization
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import os
import threading
import json
from datetime import datetime

try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    DND_AVAILABLE = True
except ImportError:
    DND_AVAILABLE = False


class AppleStyleGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Invoice Reader")
        self.root.geometry("1600x950")

        # Apple Colors
        self.colors = {
            'bg': '#FFFFFF',
            'bg_secondary': '#F5F5F7',
            'accent': '#007AFF',
            'text_primary': '#1D1D1F',
            'text_secondary': '#86868B',
            'separator': '#D2D2D7',
        }

        # State
        self.current_file = None
        self.analyzer = None
        self.visualizer = None
        self.processing = False
        self.original_image = None
        self.annotated_image = None
        self.current_result = None
        self.zoom_level = 1.0

        # PDF multi-page support
        self.pdf_pages = []
        self.current_page = 0
        self.total_pages = 0

        self.setup_ui()

    def setup_ui(self):
        """Setup Apple-style UI"""
        self.root.configure(bg=self.colors['bg'])

        # Top toolbar
        toolbar = tk.Frame(self.root, bg=self.colors['bg'], height=80)
        toolbar.pack(fill=tk.X, padx=30, pady=20)
        toolbar.pack_propagate(False)

        # Title (left)
        title_frame = tk.Frame(toolbar, bg=self.colors['bg'])
        title_frame.pack(side=tk.LEFT)

        tk.Label(title_frame, text="OCR Invoice Reader",
                font=('Arial', 26, 'bold'),
                bg=self.colors['bg'],
                fg=self.colors['text_primary']).pack(anchor='w')

        tk.Label(title_frame, text="Enhanced structure analysis with PaddleOCR v4",
                font=('Arial', 12),
                bg=self.colors['bg'],
                fg=self.colors['text_secondary']).pack(anchor='w', pady=(2,0))

        # Controls (right)
        controls = tk.Frame(toolbar, bg=self.colors['bg'])
        controls.pack(side=tk.RIGHT)

        # Settings row
        settings_row = tk.Frame(controls, bg=self.colors['bg'])
        settings_row.pack(anchor='e', pady=(0,8))

        tk.Label(settings_row, text="Language",
                font=('Arial', 11),
                bg=self.colors['bg'],
                fg=self.colors['text_secondary']).pack(side=tk.LEFT, padx=(0,8))

        self.lang_var = tk.StringVar(value='ch')
        ttk.Combobox(settings_row, textvariable=self.lang_var,
                    values=['ch','en','japan','korean'],
                    state='readonly', width=10).pack(side=tk.LEFT, padx=(0,15))

        self.gpu_var = tk.BooleanVar(value=False)
        tk.Checkbutton(settings_row, text="Use GPU",
                      variable=self.gpu_var,
                      font=('Arial', 11),
                      bg=self.colors['bg']).pack(side=tk.LEFT)

        # Add callbacks to reprocess on settings change
        self.lang_var.trace_add('write', self.on_settings_changed)
        self.gpu_var.trace_add('write', self.on_settings_changed)

        # Buttons
        btn_row = tk.Frame(controls, bg=self.colors['bg'])
        btn_row.pack(anchor='e')

        tk.Button(btn_row, text="Select File",
                 command=self.browse_file,
                 font=('Arial', 12, 'bold'),
                 bg=self.colors['bg_secondary'],
                 fg=self.colors['text_primary'],
                 activebackground='#E8E8ED',
                 activeforeground=self.colors['text_primary'],
                 relief='flat', cursor='hand2',
                 padx=20, pady=10).pack(side=tk.LEFT, padx=(0,10))

        self.process_btn = tk.Button(btn_row, text="Process Document",
                                     command=self.process_document,
                                     font=('Arial', 12, 'bold'),
                                     bg=self.colors['accent'],
                                     fg='#FFFFFF',
                                     activebackground='#0051D5',
                                     activeforeground='#FFFFFF',
                                     disabledforeground='#FFFFFF',
                                     relief='flat', cursor='hand2',
                                     padx=25, pady=10,
                                     state='disabled')
        self.process_btn.pack(side=tk.LEFT)

        # Progress bar (hidden by default)
        self.progress_bar_frame = tk.Frame(btn_row, bg=self.colors['bg'])
        self.progress_bar = ttk.Progressbar(self.progress_bar_frame,
                                           mode='indeterminate',
                                           length=150)
        self.progress_bar.pack(padx=(15,0))

        # Main content - SPLIT VIEW
        content = tk.Frame(self.root, bg=self.colors['bg'])
        content.pack(fill=tk.BOTH, expand=True)

        # LEFT PANEL - Image (60%)
        left_panel = tk.Frame(content, bg=self.colors['bg'])
        left_panel.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Image header
        img_header = tk.Frame(left_panel, bg=self.colors['bg'], height=40)
        img_header.pack(fill=tk.X, padx=30)
        img_header.pack_propagate(False)

        tk.Label(img_header, text="Preview",
                font=('Arial', 18, 'bold'),
                bg=self.colors['bg'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT)

        # Zoom controls
        zoom_frame = tk.Frame(img_header, bg=self.colors['bg'])
        zoom_frame.pack(side=tk.RIGHT)

        for txt, cmd in [("−", lambda: self.zoom(0.8)),
                         ("Reset", self.reset_zoom),
                         ("+", lambda: self.zoom(1.2))]:
            tk.Button(zoom_frame, text=txt, command=cmd,
                     font=('Arial', 13, 'bold'),
                     bg=self.colors['bg_secondary'],
                     fg=self.colors['text_primary'],
                     activebackground='#E8E8ED',
                     relief='flat', cursor='hand2',
                     width=5 if txt=="Reset" else 3,
                     pady=5).pack(side=tk.LEFT, padx=2)

        # File label and page controls
        file_info_frame = tk.Frame(left_panel, bg=self.colors['bg'])
        file_info_frame.pack(fill=tk.X, padx=30, pady=(5,10))

        self.file_label = tk.Label(file_info_frame, text="No file selected",
                                   font=('Arial', 11),
                                   bg=self.colors['bg'],
                                   fg=self.colors['text_secondary'],
                                   anchor='w')
        self.file_label.pack(side=tk.LEFT)

        # Page controls (for PDF)
        self.page_controls = tk.Frame(file_info_frame, bg=self.colors['bg'])

        self.prev_page_btn = tk.Button(self.page_controls, text="◀",
                                       command=self.prev_page,
                                       font=('Arial', 10, 'bold'),
                                       bg=self.colors['bg_secondary'],
                                       fg=self.colors['text_primary'],
                                       relief='flat', cursor='hand2',
                                       width=3, pady=2, state='disabled')
        self.prev_page_btn.pack(side=tk.LEFT, padx=2)

        self.page_label = tk.Label(self.page_controls, text="",
                                   font=('Arial', 10),
                                   bg=self.colors['bg'],
                                   fg=self.colors['text_primary'])
        self.page_label.pack(side=tk.LEFT, padx=8)

        self.next_page_btn = tk.Button(self.page_controls, text="▶",
                                       command=self.next_page,
                                       font=('Arial', 10, 'bold'),
                                       bg=self.colors['bg_secondary'],
                                       fg=self.colors['text_primary'],
                                       relief='flat', cursor='hand2',
                                       width=3, pady=2, state='disabled')
        self.next_page_btn.pack(side=tk.LEFT, padx=2)

        # Canvas for image with drag-drop
        canvas_frame = tk.Frame(left_panel, bg=self.colors['separator'], bd=1)
        canvas_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=(0,30))

        self.canvas = tk.Canvas(canvas_frame,
                               bg=self.colors['bg_secondary'],
                               highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=1, pady=1)

        # Placeholder with drag hint
        self.canvas_placeholder = self.canvas.create_text(
            400, 300,
            text="📄 Drag & Drop file here\n\nor click 'Select File' button",
            font=('Arial', 16),
            fill=self.colors['text_secondary'],
            justify='center')

        # Enable drag-drop on canvas
        if DND_AVAILABLE:
            self.canvas.drop_target_register(DND_FILES)
            self.canvas.dnd_bind('<<Drop>>', self.on_file_drop)
            self.canvas.dnd_bind('<<DragEnter>>', self.on_drag_enter)
            self.canvas.dnd_bind('<<DragLeave>>', self.on_drag_leave)

        # SEPARATOR
        tk.Frame(content, bg=self.colors['separator'], width=1).pack(side=tk.LEFT, fill=tk.Y)

        # RIGHT PANEL - Results (40%)
        right_panel = tk.Frame(content, bg=self.colors['bg_secondary'], width=650)
        right_panel.pack(side=tk.LEFT, fill=tk.BOTH)
        right_panel.pack_propagate(False)

        # Results header
        result_header = tk.Frame(right_panel, bg=self.colors['bg_secondary'], height=60)
        result_header.pack(fill=tk.X, padx=20, pady=(20,0))
        result_header.pack_propagate(False)

        tk.Label(result_header, text="Results",
                font=('Arial', 18, 'bold'),
                bg=self.colors['bg_secondary'],
                fg=self.colors['text_primary']).pack(side=tk.LEFT)

        self.export_btn = tk.Button(result_header, text="Export",
                                    command=self.export_results,
                                    font=('Arial', 11, 'bold'),
                                    bg=self.colors['accent'],
                                    fg='#FFFFFF',
                                    activebackground='#0051D5',
                                    activeforeground='#FFFFFF',
                                    disabledforeground='#FFFFFF',
                                    relief='flat', cursor='hand2',
                                    padx=20, pady=8,
                                    state='disabled')
        self.export_btn.pack(side=tk.RIGHT)

        # Tabs
        tab_frame = tk.Frame(right_panel, bg=self.colors['bg_secondary'])
        tab_frame.pack(fill=tk.X, padx=20, pady=(10,0))

        self.current_tab = 'summary'
        self.tab_buttons = {}

        for tab_id, name in [('summary','Summary'),('regions','Regions'),('json','JSON')]:
            btn = tk.Button(tab_frame, text=name,
                          command=lambda t=tab_id: self.switch_tab(t),
                          font=('Arial', 12),
                          bg=self.colors['bg_secondary'],
                          fg=self.colors['text_primary'],
                          relief='flat', cursor='hand2',
                          padx=12, pady=6)
            btn.pack(side=tk.LEFT, padx=(0,5))
            self.tab_buttons[tab_id] = btn

        self.tab_buttons['summary'].config(fg=self.colors['accent'], font=('Arial', 12, 'bold'))

        # Text area
        text_container = tk.Frame(right_panel, bg=self.colors['bg'], bd=1, relief='solid')
        text_container.pack(fill=tk.BOTH, expand=True, padx=20, pady=(15,20))

        self.text_widgets = {}
        self.text_frames = {}

        for tab_id in ['summary','regions','json']:
            frame = tk.Frame(text_container, bg=self.colors['bg'])
            text = tk.Text(frame, font=('Courier', 9), wrap=tk.WORD,
                          bg=self.colors['bg'], relief='flat',
                          padx=15, pady=15)
            scroll = tk.Scrollbar(frame, command=text.yview)
            text.config(yscrollcommand=scroll.set)
            text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)

            self.text_widgets[tab_id] = text
            self.text_frames[tab_id] = frame

        self.text_frames['summary'].pack(fill=tk.BOTH, expand=True)

        # Status bar
        status = tk.Frame(right_panel, bg=self.colors['bg_secondary'], height=35)
        status.pack(fill=tk.X, side=tk.BOTTOM)
        status.pack_propagate(False)

        self.status_label = tk.Label(status, text="Ready",
                                     font=('Arial', 11),
                                     bg=self.colors['bg_secondary'],
                                     fg=self.colors['text_secondary'],
                                     anchor='w')
        self.status_label.pack(side=tk.LEFT, padx=20)

    def switch_tab(self, tab_name):
        """Switch tabs"""
        self.current_tab = tab_name
        for frame in self.text_frames.values():
            frame.pack_forget()
        for tid, btn in self.tab_buttons.items():
            if tid == tab_name:
                btn.config(fg=self.colors['accent'], font=('Arial', 12, 'bold'))
            else:
                btn.config(fg=self.colors['text_primary'], font=('Arial', 12))
        self.text_frames[tab_name].pack(fill=tk.BOTH, expand=True)

        # Update visualization when switching tabs
        if self.annotated_image is not None:
            self.display_image(self.annotated_image)

    def browse_file(self):
        """Browse file"""
        filename = filedialog.askopenfilename(
            title="Select Document",
            filetypes=[
                ("All Supported", "*.pdf *.jpg *.jpeg *.png"),
                ("PDF Files", "*.pdf"),
                ("Image Files", "*.jpg *.jpeg *.png")
            ]
        )
        if filename:
            self.load_file(filename)

    def load_file(self, path):
        """Load file"""
        self.current_file = path
        self.file_label.config(text=f"📄 {os.path.basename(path)}",
                              fg=self.colors['text_primary'])
        self.update_status(f"Selected: {os.path.basename(path)}")
        self.process_btn.config(state='normal', bg=self.colors['accent'])

        # Reset page controls
        self.page_controls.pack_forget()
        self.pdf_pages = []
        self.current_page = 0
        self.total_pages = 0

        # Load preview
        try:
            if path.lower().endswith('.pdf'):
                # Load PDF pages
                self.load_pdf_preview(path)
            else:
                # Load image
                self.original_image = cv2.imread(path)
                if self.original_image is not None:
                    if self.canvas_placeholder:
                        self.canvas.delete(self.canvas_placeholder)
                        self.canvas_placeholder = None
                    self.display_image(self.original_image)
        except Exception as e:
            print(f"[ERROR] Failed to load file: {e}")

    def load_pdf_preview(self, pdf_path):
        """Load PDF pages for preview"""
        try:
            import fitz  # PyMuPDF
            pdf = fitz.open(pdf_path)
            self.total_pages = len(pdf)
            self.pdf_pages = []

            # Convert first page to image for preview
            page = pdf[0]
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2x scale
            img_data = pix.tobytes("ppm")

            # Convert to cv2 format
            import io
            from PIL import Image
            pil_img = Image.open(io.BytesIO(img_data))
            import numpy as np
            self.original_image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

            pdf.close()

            # Show page controls
            if self.total_pages > 1:
                self.page_controls.pack(side=tk.RIGHT, padx=10)
                self.update_page_controls()

            # Display first page
            if self.canvas_placeholder:
                self.canvas.delete(self.canvas_placeholder)
                self.canvas_placeholder = None
            self.display_image(self.original_image)

        except ImportError:
            messagebox.showinfo("PDF Support", "PDF preview requires PyMuPDF.\nInstall with: pip install PyMuPDF")
        except Exception as e:
            print(f"[ERROR] PDF load failed: {e}")

    def prev_page(self):
        """Go to previous page"""
        if self.current_page > 0:
            self.current_page -= 1
            self.load_pdf_page(self.current_page)
            self.update_page_controls()

    def next_page(self):
        """Go to next page"""
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.load_pdf_page(self.current_page)
            self.update_page_controls()

    def load_pdf_page(self, page_num):
        """Load specific PDF page"""
        try:
            import fitz
            pdf = fitz.open(self.current_file)
            page = pdf[page_num]
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            img_data = pix.tobytes("ppm")

            import io
            from PIL import Image
            import numpy as np
            pil_img = Image.open(io.BytesIO(img_data))
            self.original_image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)

            pdf.close()
            self.display_image(self.original_image)
        except Exception as e:
            print(f"[ERROR] Failed to load page: {e}")

    def update_page_controls(self):
        """Update page control states"""
        self.page_label.config(text=f"{self.current_page + 1} / {self.total_pages}")

        if self.current_page > 0:
            self.prev_page_btn.config(state='normal')
        else:
            self.prev_page_btn.config(state='disabled')

        if self.current_page < self.total_pages - 1:
            self.next_page_btn.config(state='normal')
        else:
            self.next_page_btn.config(state='disabled')

    def on_file_drop(self, event):
        """Handle file drop"""
        try:
            # Handle different formats of dropped data
            data = event.data
            # Remove curly braces and quotes if present
            if data.startswith('{') and data.endswith('}'):
                data = data[1:-1]
            data = data.strip('"').strip("'")

            # Split multiple files (take first one)
            files = data.split('} {')
            if files:
                file_path = files[0].strip('{}').strip()
                print(f"[DEBUG] Dropped file: {file_path}")

                if os.path.exists(file_path) and file_path.lower().endswith(('.pdf', '.jpg', '.jpeg', '.png')):
                    self.load_file(file_path)
                    return
        except Exception as e:
            print(f"[ERROR] Drop failed: {e}")

        messagebox.showwarning("Invalid File", "Please drop a PDF or image file (JPG, PNG)")

    def on_drag_enter(self, event):
        """Drag enter - highlight canvas"""
        self.canvas.config(bg='#e6f2ff')

    def on_drag_leave(self, event):
        """Drag leave - reset canvas"""
        self.canvas.config(bg=self.colors['bg_secondary'])

    def display_image(self, cv_img):
        """Display image on canvas"""
        if cv_img is None:
            return

        rgb = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w = rgb.shape[:2]

        cw = self.canvas.winfo_width() if self.canvas.winfo_width() > 1 else 850
        ch = self.canvas.winfo_height() if self.canvas.winfo_height() > 1 else 700

        scale = min(cw/w, ch/h) * 0.95 * self.zoom_level
        new_w, new_h = int(w*scale), int(h*scale)

        if new_w > 0 and new_h > 0:
            resized = cv2.resize(rgb, (new_w, new_h), interpolation=cv2.INTER_AREA)
            pil_img = Image.fromarray(resized)
            photo = ImageTk.PhotoImage(pil_img)

            self.canvas.delete("all")
            self.canvas.create_image(cw//2, ch//2, image=photo, anchor='center')
            self.canvas.image = photo

    def zoom(self, factor):
        """Zoom"""
        self.zoom_level = max(0.1, min(5.0, self.zoom_level * factor))
        img = self.annotated_image if self.annotated_image else self.original_image
        if img is not None:
            self.display_image(img)

    def reset_zoom(self):
        """Reset zoom"""
        self.zoom_level = 1.0
        img = self.annotated_image if self.annotated_image else self.original_image
        if img is not None:
            self.display_image(img)

    def on_settings_changed(self, *args):
        """Auto-reprocess when settings change"""
        # Only reprocess if we have already processed this file
        if self.current_file and self.current_result and not self.processing:
            # Reset analyzer and visualizer to apply new settings
            self.analyzer = None
            self.visualizer = None
            # Auto-reprocess
            self.process_document()

    def process_document(self):
        """Process"""
        if not self.current_file or self.processing:
            return

        self.processing = True
        self.process_btn.config(state='disabled')

        # Show progress bar
        self.progress_bar_frame.pack(side=tk.LEFT)
        self.progress_bar.start(10)

        self.update_status("⏳ Processing...")

        threading.Thread(target=self._process_thread, daemon=True).start()

    def _process_thread(self):
        """Process thread"""
        try:
            if not self.analyzer:
                self.root.after(0, lambda: self.update_status("🔄 Loading OCR engine..."))
                from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer
                self.analyzer = EnhancedStructureAnalyzer(
                    use_gpu=self.gpu_var.get(),
                    lang=self.lang_var.get()
                )

            self.root.after(0, lambda: self.update_status("🔍 Analyzing document structure..."))
            result = self.analyzer.analyze(self.current_file)

            # Set current_result immediately after analysis
            self.current_result = result

            self.root.after(0, lambda: self.update_status("🎨 Creating visualization..."))
            self.create_visualization(result)

            self.root.after(0, lambda: self.display_results(result))
            self.root.after(0, lambda: self.update_status("✓ Processing complete"))

        except Exception as e:
            print(f"[ERROR] {e}")
            import traceback
            traceback.print_exc()
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
            self.root.after(0, lambda: self.update_status("❌ Processing failed"))
        finally:
            self.processing = False
            self.root.after(0, self._finish_processing)

    def _finish_processing(self):
        """Clean up after processing"""
        self.process_btn.config(state='normal')
        self.progress_bar.stop()
        self.progress_bar_frame.pack_forget()

    def create_visualization(self, result):
        """Create visualization"""
        try:
            if not self.visualizer:
                from ocr_invoice_reader.utils.visualizer import OCRVisualizer
                self.visualizer = OCRVisualizer()

            if self.original_image is None:
                self.original_image = cv2.imread(self.current_file)

            regions_viz = []
            for r in result.get('regions', []):
                rd = {'type': r.type, 'bbox': r.bbox, 'confidence': r.confidence,
                      'text': r.text if hasattr(r, 'text') and r.text else ""}
                if hasattr(r, 'ocr_boxes') and r.ocr_boxes:
                    rd['ocr_boxes'] = r.ocr_boxes
                regions_viz.append(rd)

            self.annotated_image = self.visualizer.visualize_regions(
                self.original_image.copy(), regions_viz,
                show_text=True, show_boxes=True
            )

            # DISPLAY IN GUI
            self.root.after(0, lambda: self.display_image(self.annotated_image))

        except UnicodeEncodeError as e:
            # Fallback: try without text if Unicode issues
            try:
                print(f"[WARN] Unicode error in visualization, retrying without text: {e}")
                if self.visualizer:
                    self.annotated_image = self.visualizer.visualize_regions(
                        self.original_image.copy(), regions_viz,
                        show_text=False, show_boxes=True
                    )
                    self.root.after(0, lambda: self.display_image(self.annotated_image))
                else:
                    print(f"[ERROR] Visualizer not initialized")
                    self.root.after(0, lambda: self.display_image(self.original_image))
            except Exception as e2:
                print(f"[ERROR] Visualization failed completely: {e2}")
                # Show original image instead
                self.root.after(0, lambda: self.display_image(self.original_image))
        except Exception as e:
            print(f"[WARN] Visualization failed: {e}")
            import traceback
            traceback.print_exc()
            # Show original image as fallback
            self.annotated_image = self.original_image
            self.root.after(0, lambda: self.display_image(self.original_image))

    def display_results(self, result):
        """Display results"""
        self.current_result = result

        for text in self.text_widgets.values():
            text.config(state='normal')
            text.delete(1.0, tk.END)

        # Summary
        summary = self.text_widgets['summary']
        summary.insert(tk.END, "ANALYSIS SUMMARY\n\n", 'title')
        summary.insert(tk.END, f"File: {os.path.basename(result.get('image_path', ''))}\n")
        summary.insert(tk.END, f"Method: {result.get('method', 'unknown')}\n")
        summary.insert(tk.END, f"Regions: {len(result.get('regions', []))}\n")
        summary.insert(tk.END, f"Time: {datetime.now().strftime('%H:%M:%S')}\n\n")

        if result.get('regions'):
            summary.insert(tk.END, "REGION TYPES\n\n", 'title')
            types = {}
            for r in result['regions']:
                types[r.type] = types.get(r.type, 0) + 1
            for t, c in types.items():
                summary.insert(tk.END, f"  • {t}: {c}\n")

        summary.tag_config('title', font=('Arial', 12, 'bold'))
        summary.config(state='disabled')

        # Regions
        regions = self.text_widgets['regions']
        for i, r in enumerate(result.get('regions', []), 1):
            regions.insert(tk.END, f"\nREGION {i}\n", 'title')
            regions.insert(tk.END, f"Type: {r.type}\n")
            regions.insert(tk.END, f"Confidence: {r.confidence:.1%}\n")
            text = r.text if hasattr(r, 'text') and r.text else ""
            if text:
                regions.insert(tk.END, f"\nText:\n{text}\n")
            regions.insert(tk.END, "\n" + "─"*50 + "\n")
        regions.tag_config('title', font=('Arial', 11, 'bold'), foreground=self.colors['accent'])
        regions.config(state='disabled')

        # JSON
        json_text = self.text_widgets['json']
        ser = {
            'method': result.get('method', ''),
            'image_path': result.get('image_path', ''),
            'regions': [{'type': r.type, 'bbox': r.bbox, 'confidence': r.confidence,
                        'text': r.text if hasattr(r, 'text') and r.text else ""}
                       for r in result.get('regions', [])]
        }
        json_text.insert(tk.END, json.dumps(ser, indent=2, ensure_ascii=False))
        json_text.config(state='disabled')

        self.export_btn.config(state='normal')

    def export_results(self):
        """Export"""
        if not self.current_result:
            return
        filename = filedialog.asksaveasfilename(
            title="Export Results",
            defaultextension=".json",
            filetypes=[("JSON Files", "*.json"), ("Text Files", "*.txt")]
        )
        if not filename:
            return
        try:
            ser = {
                'method': self.current_result.get('method', ''),
                'image_path': self.current_result.get('image_path', ''),
                'timestamp': datetime.now().isoformat(),
                'regions': [{'type': r.type, 'bbox': r.bbox, 'confidence': r.confidence,
                            'text': r.text if hasattr(r, 'text') and r.text else ""}
                           for r in self.current_result.get('regions', [])]
            }
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(ser, f, indent=2, ensure_ascii=False)
            messagebox.showinfo("Success", "Exported successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Export failed:\n{e}")

    def update_status(self, msg):
        """Update status"""
        self.status_label.config(text=msg)


def main():
    if DND_AVAILABLE:
        root = TkinterDnD.Tk()
    else:
        root = tk.Tk()
    app = AppleStyleGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
