# OCR Invoice Reader - Simple GUI

**全新简单可靠的 GUI** - 直接使用 ocr-invoice-reader API

## ✨ 特点

- ✅ **简单可靠** - 最小化设计，专注核心功能
- ✅ **直接 API** - 使用 `EnhancedStructureAnalyzer` 直接调用
- ✅ **无复杂依赖** - 只依赖 ocr-invoice-reader
- ✅ **快速启动** - 1 秒启动
- ✅ **按需加载** - 第一次使用时加载 OCR 引擎

## 📥 下载

### Windows 可执行文件

[下载 OCR-Invoice-Reader-Simple-v1.0.tar.gz](#)

### 从源代码运行

```bash
# 安装依赖
pip install -e path/to/ocr-invoice-reader

# 运行
python src/ocr_gui_simple.py
```

## 🚀 使用方法

1. 运行 `OCR-Invoice-Reader-Simple.exe`
2. 点击 "Browse..." 选择文件（PDF 或图片）
3. 选择语言和设置
4. 点击 "Process Document"
5. 查看结果

### 第一次使用

- 第一次处理文件时会加载 OCR 引擎（~10 秒）
- PaddleOCR 会下载模型文件（~300MB，一次性）
- 之后处理速度很快（2-3 秒）

## 📊 性能

| 操作 | 时间 |
|------|------|
| 启动 | ~1 秒 |
| 首次OCR | ~10 秒（加载引擎）|
| 后续OCR | 2-3 秒 |

## 🔧 技术细节

### 使用的 API

```python
from ocr_invoice_reader.processors.enhanced_structure_analyzer import EnhancedStructureAnalyzer

# 创建分析器
analyzer = EnhancedStructureAnalyzer(
    use_gpu=False,  # CPU 模式
    lang='ch'       # 中文
)

# 分析文档
result = analyzer.analyze('document.pdf', visualize=False)

# 访问结果
for region in result['regions']:
    print(region['type'], region['text'])
```

### 依赖项

- ocr-invoice-reader (必须)
- PaddleOCR v4
- tkinter (Python 自带)

## 🆚 与旧版本的区别

| 特性 | 旧 GUI (ocr_gui_modern.py) | 新 GUI (ocr_gui_simple.py) |
|------|---------------------------|---------------------------|
| 复杂度 | ❌ 1000+ 行 | ✅ 200 行 |
| 依赖 | ❌ 多个自定义模块 | ✅ 只依赖 ocr-invoice-reader |
| 启动 | ❌ 可能失败 | ✅ 可靠启动 |
| 打包 | ❌ 复杂 | ✅ 简单 |
| 维护 | ❌ 困难 | ✅ 容易 |

## 📝 系统要求

- Windows 7+
- Python 3.8+ (源代码运行)
- 4GB RAM
- Internet (首次运行下载模型)

## 🔗 相关链接

- OCR 引擎：https://github.com/SyuuKasinn/ocr-invoice-reader
- 问题反馈：https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues

## 📄 许可证

MIT License
