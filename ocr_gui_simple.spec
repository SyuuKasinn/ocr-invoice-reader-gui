# -*- mode: python ; coding: utf-8 -*-
# 简化版spec - 如果优化版构建失败,使用这个

import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)

block_cipher = None

a = Analysis(
    ['ocr_gui.py'],  # 使用原版GUI
    pathex=[],
    binaries=[],
    datas=[
        ('demo', 'demo'),
        ('README.md', '.'),
        ('INSTALLATION.md', '.'),
    ],
    hiddenimports=[
        'tkinter',
        'tkinterdnd2',
        'PIL.Image',
        'PIL.ImageTk',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'pandas',
        'tensorflow',
        'torch',
        'pytest',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# 目录模式 - 快速启动
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='OCR-Invoice-Reader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='OCR-Invoice-Reader',
)
