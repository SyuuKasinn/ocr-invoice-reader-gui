# OCR Invoice Reader GUI - 安装指南

## ⚠️ 重要说明

**无法打包成 exe** - PaddleOCR 的 Cython 依赖无法被 PyInstaller 正确打包。

**解决方案**：从源代码运行（简单、可靠）

---

## 📦 方法 1：快速安装（推荐）

### 步骤 1：安装依赖

```bash
# 安装 ocr-invoice-reader
cd C:\Users\kants\Desktop\ocr-invoice-reader
pip install -e .

# 返回 GUI 目录
cd C:\Users\kants\ocr-invoice-reader-gui
```

### 步骤 2：运行 GUI

**方式 A：双击批处理文件**
```
双击：run_gui.bat
```

**方式 B：命令行运行**
```bash
python src\ocr_gui_simple.py
```

### 完成！

GUI 会在 1 秒内启动，第一次处理文件时会加载 OCR 引擎（~10 秒）。

---

## 📦 方法 2：完整安装（从头开始）

### 前提条件

- Windows 7+
- Python 3.8 或更高
- Git（可选）

### 步骤 1：安装 Python

如果还没有 Python：
1. 下载：https://www.python.org/downloads/
2. 安装时勾选 "Add Python to PATH"

### 步骤 2：获取代码

**选项 A：使用 Git**
```bash
# 下载 ocr-invoice-reader
git clone https://github.com/SyuuKasinn/ocr-invoice-reader.git
cd ocr-invoice-reader
pip install -e .

# 下载 GUI
cd ..
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui
```

**选项 B：手动下载**
1. 下载并解压 ocr-invoice-reader
2. 下载并解压 ocr-invoice-reader-gui
3. 记住两个目录的路径

### 步骤 3：安装依赖

```bash
# 进入 ocr-invoice-reader 目录
cd path\to\ocr-invoice-reader
pip install -e .

# 这会自动安装：
# - PaddleOCR
# - PaddlePaddle
# - OpenCV
# - PyMuPDF
# - 等等...
```

### 步骤 4：运行

```bash
cd path\to\ocr-invoice-reader-gui
python src\ocr_gui_simple.py
```

---

## 🎯 使用方法

### 启动

1. 打开命令提示符（CMD）
2. 运行：
   ```bash
   cd C:\Users\kants\ocr-invoice-reader-gui
   python src\ocr_gui_simple.py
   ```
3. 或双击 `run_gui.bat`

### 处理文档

1. 点击 "Browse..." 选择文件
2. 选择语言（ch/en/japan/korean）
3. 点击 "Process Document"
4. 查看结果

### 第一次使用

- **首次运行**：PaddleOCR 会下载模型文件（~300MB）
- **首次处理**：加载 OCR 引擎（~10 秒）
- **后续处理**：快速（2-3 秒）

---

## 🔧 故障排除

### 问题 1：找不到模块

```
ModuleNotFoundError: No module named 'ocr_invoice_reader'
```

**解决**：
```bash
cd path\to\ocr-invoice-reader
pip install -e .
```

### 问题 2：找不到 Python

```
'python' is not recognized as an internal or external command
```

**解决**：
1. 重新安装 Python
2. 勾选 "Add Python to PATH"
3. 或使用完整路径：
   ```bash
   C:\Python310\python.exe src\ocr_gui_simple.py
   ```

### 问题 3：PaddleOCR 下载慢

**解决**：
使用国内镜像：
```bash
pip install paddlepaddle -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install paddleocr -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题 4：想要 GPU 加速

**解决**：
```bash
# 卸载 CPU 版本
pip uninstall paddlepaddle

# 安装 GPU 版本（需要 NVIDIA GPU + CUDA）
pip install paddlepaddle-gpu==3.0.0
```

---

## 📊 性能

| 操作 | 时间 |
|------|------|
| GUI 启动 | ~1 秒 ⚡ |
| 首次 OCR | ~10 秒 |
| 后续 OCR | 2-3 秒 ⚡⚡⚡ |

---

## 💡 提示

### 批量处理

保持 GUI 打开，连续处理多个文件：
- 第 1 个：10 秒
- 第 2 个：3 秒 ⚡
- 第 3 个：3 秒 ⚡
- ...

### 加速技巧

1. **使用 GPU**（如果有 NVIDIA 显卡）
   - 速度提升 3-10 倍
   - 勾选 GUI 中的 "Use GPU"

2. **保持 GUI 打开**
   - OCR 引擎加载一次，重复使用
   - 不要每次处理都重启 GUI

---

## 🆘 获取帮助

如果遇到问题：

1. **查看控制台输出** - 运行时会显示详细信息
2. **报告问题**：https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
3. **包含信息**：
   - 错误信息
   - Python 版本（`python --version`）
   - 操作系统版本

---

## ❓ 常见问题

### Q: 为什么不能打包成 exe？

A: PaddleOCR 使用 Cython，PyInstaller 无法正确打包 Cython 的工具文件。这是已知的兼容性问题。

### Q: 源代码运行会很慢吗？

A: 不会！实际处理速度与 exe 完全相同。只是启动方式不同。

### Q: 需要联网吗？

A: 只有第一次运行需要（下载 PaddleOCR 模型）。之后可以离线使用。

### Q: 可以分享给别人吗？

A: 可以！让他们按照这个指南安装即可。或者发送安装好的 Python 虚拟环境。

---

## 📝 许可证

MIT License
