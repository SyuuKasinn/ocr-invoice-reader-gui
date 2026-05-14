# OCR Invoice Reader GUI

**简单可靠的图形界面** - 基于 [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader)

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## ⚡ 快速开始

### 运行 GUI

```bash
# 1. 安装依赖
cd path/to/ocr-invoice-reader
pip install -e .

# 2. 运行 GUI
cd path/to/ocr-invoice-reader-gui
python src/ocr_gui_simple.py

# 或双击
run_gui.bat
```

**就这么简单！** 🎉

---

## ⚠️ 关于 exe 打包

**不提供 exe 文件** - PaddleOCR 的 Cython 依赖无法被 PyInstaller 正确打包。

**解决方案**：从源代码运行（简单、快速、可靠）

详见：[INSTALL.md](INSTALL.md)

---

## ✨ 特性

- ✅ **简单可靠** - 200 行代码，直接调用 API
- ✅ **快速启动** - 1 秒启动
- ✅ **按需加载** - 首次处理时加载引擎
- ✅ **多语言** - 中文、英文、日文、韩文
- ✅ **GPU 支持** - 可选 GPU 加速

---

## 📊 性能

| 操作 | 时间 |
|------|------|
| GUI 启动 | ~1 秒 ⚡ |
| 首次 OCR（加载引擎） | ~10 秒 |
| 后续 OCR | **2-3 秒** ⚡⚡⚡ |

**保持 GUI 打开**，处理多个文件时第 2 个起只需 2-3 秒！

---

## 🖼️ 界面预览

简洁的三步操作：
1. **选择文件** - Browse 按钮
2. **选择设置** - 语言、GPU
3. **处理文档** - 一键处理

结果实时显示在文本框中。

---

## 📖 详细文档

- [安装指南](INSTALL.md) - 完整安装步骤
- [简单版 README](README_SIMPLE.md) - 技术细节
- [OCR 引擎](https://github.com/SyuuKasinn/ocr-invoice-reader) - 后端 API

---

## 🆚 两个 GUI 版本

### `ocr_gui_simple.py` ✅ **推荐**

- **简单**：200 行代码
- **可靠**：直接 API 调用
- **维护**：容易更新

### `ocr_gui_modern.py` ❌ 已废弃

- 复杂（1000+ 行）
- 多个问题
- 不推荐使用

---

## 🔧 系统要求

- **操作系统**：Windows 7+, macOS, Linux
- **Python**：3.8 或更高
- **RAM**：4GB（推荐 8GB）
- **网络**：首次运行需要（下载模型）

---

## 💡 使用技巧

### 批量处理

保持 GUI 打开，连续处理：
```
文件 1: 10秒（加载引擎）
文件 2: 3秒 ⚡
文件 3: 3秒 ⚡
文件 4: 3秒 ⚡
```

### GPU 加速

如果有 NVIDIA GPU：
```bash
# 安装 GPU 版本
pip install paddlepaddle-gpu==3.0.0

# GUI 中勾选 "Use GPU"
# 速度提升 3-10 倍！
```

---

## 🐛 故障排除

### 找不到模块？

```bash
cd path/to/ocr-invoice-reader
pip install -e .
```

### Python 找不到？

重新安装 Python，勾选 "Add to PATH"

### 更多问题？

查看 [INSTALL.md](INSTALL.md) 或 [报告问题](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues)

---

## 🙏 致谢

- [ocr-invoice-reader](https://github.com/SyuuKasinn/ocr-invoice-reader) - 核心 OCR 引擎
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) - OCR 模型

---

## 📄 许可证

MIT License

---

## 🔗 相关链接

- **OCR 引擎**：https://github.com/SyuuKasinn/ocr-invoice-reader
- **问题反馈**：https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues
- **PaddleOCR**：https://github.com/PaddlePaddle/PaddleOCR

---

**从源代码运行，简单可靠！** 🚀
