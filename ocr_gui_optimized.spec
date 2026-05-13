# -*- mode: python ; coding: utf-8 -*-
# PyInstaller spec for OCR Invoice Reader GUI - Optimized Version
# 优化版配置: 使用目录模式,加载速度提升5-10倍

import sys
import os
from pathlib import Path

# Increase recursion limit for complex dependencies (PaddleOCR, scipy, etc.)
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

# Analysis: what files to include
a = Analysis(
    ['ocr_gui_optimized.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Include demo folder for examples
        ('demo', 'demo'),
        # Include README and docs
        ('README.md', '.'),
        ('INSTALLATION.md', '.'),
        ('PERFORMANCE_OPTIMIZATION.md', '.'),
    ],
    hiddenimports=[
        # GUI dependencies
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.scrolledtext',
        'tkinterdnd2',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageGrab',

        # Standard library
        'subprocess',
        'pathlib',
        'json',
        'tempfile',
        'threading',
        'time',

        # OCR dependencies - 添加所有PaddleOCR相关依赖
        'paddle',
        'paddleocr',
        'shapely',
        'shapely.geometry',
        'pyclipper',
        'imgaug',
        'lmdb',
        'tqdm',
        'yaml',
        'pyyaml',
        'attrdict',
        'opencv-python',
        'opencv-contrib-python',
        'cv2',
        'lxml',
        'premailer',
        'openpyxl',
        'python-docx',
        'Cython',
        'numpy',
        'scipy',
        'scikit-image',
        'skimage',

        # OCR Invoice Reader
        'ocr_invoice_reader',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # 只排除确定不需要的包
        'matplotlib',
        'pandas',
        'tensorflow',
        'torch',
        'pytest',
        'IPython',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# PYZ: Python archive
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE: Executable (directory mode for FAST startup - no extraction needed!)
exe = EXE(
    pyz,
    a.scripts,
    [],  # Empty - we use COLLECT for directory mode
    exclude_binaries=True,  # Don't bundle everything in one file
    name='OCR-Invoice-Reader-Optimized',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window for clean UI
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # TODO: Add icon file if you have one
)

# COLLECT: Bundle all files into a directory
# This is the KEY for fast startup - no extraction needed!
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='OCR-Invoice-Reader-Optimized',
)
