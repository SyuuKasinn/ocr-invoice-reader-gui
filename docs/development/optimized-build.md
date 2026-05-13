# 优化版 OCR Invoice Reader - 使用说明

## 📦 文件说明

构建完成后，会生成以下文件结构:

```
dist/
└── OCR-Invoice-Reader-Optimized/
    ├── OCR-Invoice-Reader-Optimized.exe  ← 主程序 (双击运行)
    ├── _internal/                         ← 依赖库 (不要删除)
    │   ├── paddleocr/
    │   ├── PIL/
    │   ├── tkinter/
    │   └── ... (其他依赖)
    ├── demo/                              ← 示例文件
    │   ├── sample_invoice.pdf
    │   └── sample_image.jpg
    ├── README.md                          ← 项目说明
    ├── INSTALLATION.md                    ← 安装指南
    └── PERFORMANCE_OPTIMIZATION.md        ← 性能优化说明
```

## 🚀 快速开始

### 方式1: 运行EXE文件 (推荐)

1. 打开 `dist\OCR-Invoice-Reader-Optimized` 文件夹
2. 双击 `OCR-Invoice-Reader-Optimized.exe`
3. 等待启动画面 (首次约10秒,加载OCR模型)
4. 拖放PDF或图片文件到窗口
5. 点击 "Process Document" 按钮

**首次运行:**
- 会下载PaddleOCR模型 (~300MB) 到 `C:\Users\你的用户名\.paddleocr\`
- 模型下载完成后会自动缓存,之后无需重复下载

### 方式2: 运行Python源码

```bash
# 安装依赖
pip install tkinterdnd2 Pillow paddleocr opencv-python

# 运行优化版
python ocr_gui_optimized.py
```

## ⚡ 性能对比

| 版本 | 启动时间 | 首次识别 | 第2次识别 | 第10次识别 |
|------|---------|---------|----------|-----------|
| **原版** (subprocess) | 5秒 | 15秒 | 15秒 | 15秒 |
| **优化版** (预加载) | 2秒 | 15秒 | **3秒** ⚡ | **3秒** ⚡ |
| **优化版+GPU** | 2秒 | 8秒 | **1.5秒** ⚡⚡ | **1.5秒** ⚡⚡ |

### 关键改进

1. **目录模式打包** (`--onedir`)
   - 不需要每次启动都解压文件
   - 启动速度提升 5-10倍

2. **预加载OCR引擎**
   - 程序启动时加载一次模型
   - 后续识别直接使用,无需重新加载
   - 第2次起识别速度提升 5倍

3. **启动画面**
   - 显示加载进度
   - 改善用户体验

## 📊 功能特性

### 支持的文件格式
- ✅ PDF文档 (`.pdf`)
- ✅ JPG图片 (`.jpg`, `.jpeg`)
- ✅ PNG图片 (`.png`)

### OCR模式
- `ocr-simple`: 最快,适合快速预览
- `ocr-raw`: 快,适合简单文档
- `ocr-extract`: 中等,适合复杂发票
- `ocr-enhanced`: 最慢但最准确

### 支持语言
- 中文 (`ch`)
- 英文 (`en`)
- 日文 (`japan`)
- 韩文 (`korean`)

### 输出结果
- 📊 可视化图像 (带标注)
- 📋 JSON结构化数据
- 📝 提取的文本
- 🔢 表格数据 (HTML)

## 🎯 使用技巧

### 1. 提高识别速度

**方法1:** 使用GPU加速
```
勾选 "Use GPU (if available)" 复选框
需要: NVIDIA显卡 + CUDA
```

**方法2:** 选择合适的OCR模式
```
快速预览: ocr-simple
日常使用: ocr-extract
高精度: ocr-enhanced
```

### 2. 批量处理

连续拖放多个文件,无需重启程序:
```
文件1 → 处理 (15秒)
文件2 → 处理 (3秒)  ← 快5倍!
文件3 → 处理 (3秒)
...
```

### 3. 查看结果

处理完成后,切换不同标签页:
- **Visualization**: 查看标注的图像
- **JSON Data**: 查看结构化数据
- **Extracted Text**: 查看纯文本
- **Tables**: 查看表格数据

## 📦 分发方式

### 方式1: ZIP压缩包

```bash
# 压缩整个文件夹
cd dist
zip -r OCR-Invoice-Reader-Optimized-v1.1.zip OCR-Invoice-Reader-Optimized/
```

用户解压后直接运行exe即可。

### 方式2: 安装程序

使用 [Inno Setup](https://jrsoftware.org/isinfo.php) 制作安装程序:

```inno
[Setup]
AppName=OCR Invoice Reader
AppVersion=1.1
DefaultDirName={pf}\OCR Invoice Reader
DefaultGroupName=OCR Invoice Reader
OutputBaseFilename=OCR-Invoice-Reader-Setup-v1.1

[Files]
Source: "dist\OCR-Invoice-Reader-Optimized\*"; DestDir: "{app}"; Flags: recursesubdirs

[Icons]
Name: "{group}\OCR Invoice Reader"; Filename: "{app}\OCR-Invoice-Reader-Optimized.exe"
Name: "{commondesktop}\OCR Invoice Reader"; Filename: "{app}\OCR-Invoice-Reader-Optimized.exe"
```

## 🔧 常见问题

### Q1: 首次运行很慢?
A: 正常现象。首次运行需要下载PaddleOCR模型 (~300MB),下载完成后会缓存到本地。

### Q2: 模型存储在哪里?
A: `C:\Users\你的用户名\.paddleocr\`

可以手动复制模型文件夹到其他电脑,避免重复下载。

### Q3: 如何启用GPU加速?
A: 
1. 确保有NVIDIA显卡
2. 安装CUDA 11.2+ 和 cuDNN 8.2+
3. 重新安装GPU版Paddle:
   ```bash
   pip uninstall paddlepaddle
   pip install paddlepaddle-gpu
   ```
4. 在GUI中勾选 "Use GPU"

### Q4: exe文件太大?
A: 这是正常的。包含了以下组件:
- Python运行时
- PaddleOCR库
- OpenCV
- Pillow图像处理
- Tkinter GUI框架

可以考虑:
- 使用单文件模式 (更小但启动慢)
- 使用在线安装程序 (只打包核心,运行时下载依赖)

### Q5: 杀毒软件报警?
A: PyInstaller打包的exe可能被误报。解决方法:
1. 添加到杀毒软件白名单
2. 使用代码签名证书签名exe
3. 提供源码让用户自行构建

## 📝 更新日志

### v1.1 (优化版)
- ✅ 改用目录模式打包,启动快5-10倍
- ✅ 预加载OCR引擎,识别快5倍
- ✅ 添加启动画面
- ✅ 优化依赖包,减少冗余

### v1.0 (原版)
- 基础OCR功能
- 拖放文件上传
- 多标签页结果展示

## 🔗 相关链接

- **项目仓库**: https://github.com/SyuuKasinn/ocr-invoice-reader-gui
- **OCR引擎**: https://github.com/SyuuKasinn/ocr-invoice-reader
- **PaddleOCR**: https://github.com/PaddlePaddle/PaddleOCR

## 📧 反馈与支持

遇到问题? 
1. 查看 `PERFORMANCE_OPTIMIZATION.md` 性能优化指南
2. 提交Issue到GitHub仓库
3. 查看PaddleOCR官方文档

---

**享受快速的OCR体验! ⚡**
