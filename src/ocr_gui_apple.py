#!/usr/bin/env python3
"""
OCR Invoice Reader - Apple Design Style
Clean, minimalist interface with integrated image visualization
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
import threading
import json
from datetime import datetime


class AppleStyleOCRGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OCR Invoice Reader")
        self.root.geometry("1600x1000")
        self.root.minsize(1400, 800)
        
        # Apple Design Colors (macOS Big Sur / Monterey style)
        self.colors = {
            'bg': '#FFFFFF',
            'bg_secondary': '#F5F5F7', 
            'accent': '#007AFF',
            'accent_hover': '#0051D5',
            'success': '#34C759',
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
        
        self.setup_ui()
