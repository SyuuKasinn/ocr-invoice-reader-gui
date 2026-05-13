# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Analysis: what files to include
a = Analysis(
    ['ocr_gui.py'],
    pathex=[],
    binaries=[],
    datas=[
        # Include demo folder for examples
        ('demo', 'demo'),
        # Include README and docs
        ('README.md', '.'),
        ('INSTALLATION.md', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinterdnd2',
        'PIL',
        'PIL.Image',
        'PIL.ImageTk',
        'PIL.ImageGrab',
        'subprocess',
        'pathlib',
        'json',
        'tempfile',
        'threading',
        # PaddleOCR related dependencies
        'paddleocr',
        'paddle',
        'shapely',
        'pyclipper',
        'imgaug',
        'lmdb',
        'tqdm',
        'yaml',
        'attrdict',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Only exclude truly unused packages
        'matplotlib',
        'pandas',
        'tensorflow',
        'torch',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# PYZ: Python archive
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE: Executable (directory mode for faster startup)
exe = EXE(
    pyz,
    a.scripts,
    [],  # Don't bundle binaries in EXE
    exclude_binaries=True,  # Extract binaries to separate files
    name='OCR-Invoice-Reader-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon file if you have one
)

# COLLECT: Bundle all files into a directory (MUCH FASTER than onefile)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='OCR-Invoice-Reader-GUI',
)
