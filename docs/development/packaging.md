# EXE打包完整指南

## 🎯 三种打包方案

### 方案1: 简化版 (推荐 - 最稳定)

**特点:** 只打包GUI,OCR功能通过subprocess调用外部命令

```bash
# 1. 清理旧版本
rm -rf build dist

# 2. 构建
pyinstaller --clean ocr_gui_simple.spec

# 3. 结果
dist/OCR-Invoice-Reader/OCR-Invoice-Reader.exe
```

**优点:**
- ✅ 构建稳定,不会失败
- ✅ 文件较小 (~50MB)
- ✅ 启动快 (目录模式)

**缺点:**
- ❌ OCR识别速度慢 (每次重新加载模型)

---

### 方案2: 优化版 (推荐 - 最快)

**特点:** 打包GUI + OCR引擎,预加载模型

```bash
# 1. 安装所有依赖
pip install paddleocr opencv-python pyyaml attrdict lmdb tqdm shapely pyclipper imgaug

# 2. 清理旧版本
rm -rf build dist

# 3. 构建
pyinstaller --clean ocr_gui_optimized.spec

# 4. 结果
dist/OCR-Invoice-Reader-Optimized/OCR-Invoice-Reader-Optimized.exe
```

**优点:**
- ✅ OCR识别超快 (预加载模型)
- ✅ 第2次起快5倍
- ✅ 启动快 (目录模式)

**缺点:**
- ❌ 构建复杂,可能失败 (依赖多)
- ❌ 文件很大 (~500MB+)

---

### 方案3: 单文件版 (分发方便但慢)

**特点:** 打包成单个exe文件

```bash
# 修改spec文件,使用onefile模式
pyinstaller --onefile --windowed ocr_gui.py
```

**优点:**
- ✅ 只有一个文件,分发方便

**缺点:**
- ❌ 启动很慢 (每次解压)
- ❌ OCR识别慢
- ❌ 不推荐使用

---

## 📝 完整构建步骤

###  方案1: 简化版 (最稳定)

```bash
# Step 1: 检查环境
python --version  # 需要3.8+
pip --version

# Step 2: 安装PyInstaller
pip install pyinstaller

# Step 3: 安装基础依赖
pip install tkinterdnd2 Pillow

# Step 4: 清理并构建
rm -rf build dist __pycache__
pyinstaller --clean ocr_gui_simple.spec

# Step 5: 测试
cd dist/OCR-Invoice-Reader
./OCR-Invoice-Reader.exe

# Step 6: 打包分发
cd ..
zip -r OCR-Invoice-Reader-v1.0.zip OCR-Invoice-Reader/
```

### 方案2: 优化版 (最快)

```bash
# Step 1-2: 同上

# Step 3: 安装所有依赖
pip install tkinterdnd2 Pillow
pip install paddleocr opencv-python
pip install pyyaml attrdict lmdb tqdm shapely pyclipper imgaug

# Step 4: 清理并构建
rm -rf build dist __pycache__
pyinstaller --clean ocr_gui_optimized.spec

# 如果构建失败 (RecursionError):
# spec文件已经包含了 sys.setrecursionlimit() 的修复

# Step 5-6: 同上
```

---

## ⚠️ 常见构建问题

### 问题1: RecursionError

**症状:**
```
RecursionError: maximum recursion depth exceeded
```

**解决:**
```python
# 在spec文件开头添加:
import sys
sys.setrecursionlimit(sys.getrecursionlimit() * 5)
```

已在 `ocr_gui_optimized.spec` 中修复。

---

### 问题2: 缺少模块

**症状:**
```
ModuleNotFoundError: No module named 'xxx'
```

**解决:**
```python
# 在spec文件的hiddenimports中添加:
hiddenimports=[
    'xxx',  # 缺少的模块名
]
```

---

### 问题3: DLL加载失败

**症状:**
```
ImportError: DLL load failed
```

**解决:**
```bash
# 重新安装OpenCV
pip uninstall opencv-python opencv-contrib-python
pip install opencv-python
```

---

### 问题4: exe文件太大

**原因:** 包含了所有依赖库 (PaddleOCR, scipy, numpy等)

**解决方案:**

**选项A:** 使用简化版 (不打包OCR引擎)
```bash
pyinstaller ocr_gui_simple.spec
```

**选项B:** 排除不必要的依赖
```python
# 在spec中添加:
excludes=[
    'matplotlib',
    'pandas', 
    'tensorflow',
    'torch',
]
```

**选项C:** 使用UPX压缩
```bash
# 安装UPX: https://upx.github.io/
# spec文件中设置:
upx=True
```

---

## 🔧 手动构建 (不使用spec)

### 简化版
```bash
pyinstaller \
    --onedir \
    --windowed \
    --name="OCR-Invoice-Reader" \
    --add-data="demo:demo" \
    --add-data="README.md:." \
    --hidden-import=tkinterdnd2 \
    --hidden-import=PIL.Image \
    --hidden-import=PIL.ImageTk \
    --exclude-module=matplotlib \
    --exclude-module=pandas \
    ocr_gui.py
```

### 优化版
```bash
pyinstaller \
    --onedir \
    --windowed \
    --name="OCR-Invoice-Reader-Optimized" \
    --add-data="demo:demo" \
    --hidden-import=tkinterdnd2 \
    --hidden-import=paddleocr \
    --hidden-import=paddle \
    --hidden-import=cv2 \
    --hidden-import=yaml \
    ocr_gui_optimized.py
```

---

## 📦 分发指南

### Windows用户

**方式1: ZIP压缩包**
```bash
cd dist
zip -r OCR-Invoice-Reader.zip OCR-Invoice-Reader/
```

用户解压后运行exe即可。

**方式2: Inno Setup安装程序**

1. 下载 [Inno Setup](https://jrsoftware.org/isinfo.php)
2. 创建 `installer.iss`:

```inno
[Setup]
AppName=OCR Invoice Reader
AppVersion=1.0
DefaultDirName={autopf}\OCR Invoice Reader
DefaultGroupName=OCR Invoice Reader
OutputDir=output
OutputBaseFilename=OCR-Invoice-Reader-Setup
Compression=lzma2
SolidCompression=yes

[Files]
Source: "dist\OCR-Invoice-Reader\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\OCR Invoice Reader"; Filename: "{app}\OCR-Invoice-Reader.exe"
Name: "{autodesktop}\OCR Invoice Reader"; Filename: "{app}\OCR-Invoice-Reader.exe"

[Run]
Filename: "{app}\OCR-Invoice-Reader.exe"; Description: "Launch OCR Invoice Reader"; Flags: postinstall nowait skipifsilent
```

3. 编译生成 Setup.exe

---

## 🎯 推荐方案总结

### 个人使用
- 使用 **简化版** (`ocr_gui_simple.spec`)
- 文件小,构建稳定

### 分发给他人  
- 优先 **简化版** + Inno Setup安装程序
- 备选 **优化版** (如果构建成功)

### 追求极致性能
- 使用 **优化版** (`ocr_gui_optimized.spec`)
- 第2次识别快5倍

---

## 🚀 快速命令

```bash
# 简化版 (稳定)
pyinstaller --clean ocr_gui_simple.spec

# 优化版 (快速)
pyinstaller --clean ocr_gui_optimized.spec

# 原版目录模式 (中等)
pyinstaller --clean ocr_gui.spec

# 单文件模式 (不推荐)
pyinstaller --onefile --windowed ocr_gui.py
```

---

## 📊 性能 vs 文件大小对比

| 方案 | 文件大小 | 启动速度 | OCR速度 | 构建难度 |
|------|---------|---------|---------|---------|
| 简化版 (目录) | ~50MB | ⚡⚡⚡ | 🐌 | ⭐ 简单 |
| 优化版 (目录) | ~500MB | ⚡⚡⚡ | ⚡⚡⚡ | ⭐⭐⭐ 复杂 |
| 原版 (单文件) | ~40MB | 🐌 | 🐌 | ⭐⭐ 中等 |
| 原版 (目录) | ~50MB | ⚡⚡⚡ | 🐌 | ⭐ 简单 |

**推荐:** 简化版 (目录) - 性价比最高
