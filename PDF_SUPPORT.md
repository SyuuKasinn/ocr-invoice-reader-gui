# PDF Support Documentation

## 问题原因

`EnhancedStructureAnalyzer.analyze()` 方法只接受图片路径作为输入：
```python
def analyze(self, image_path: str) -> Dict[str, Any]
```

它不直接支持PDF文件。因此当用户选择PDF时，需要先转换为图片。

## 解决方案

### 1. PDF预览加载
使用PyMuPDF (fitz)将PDF页面渲染为图片：

```python
def load_pdf_preview(self, pdf_path):
    import fitz  # PyMuPDF
    pdf = fitz.open(pdf_path)
    page = pdf[0]  # 获取第一页
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # 2倍分辨率
    img_data = pix.tobytes("ppm")
    
    # 转换为OpenCV格式
    from PIL import Image
    import io
    pil_img = Image.open(io.BytesIO(img_data))
    self.original_image = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
```

### 2. PDF处理
在OCR分析时，将当前页面保存为临时图片：

```python
def _process_thread(self):
    analyze_path = self.current_file
    temp_image_path = None
    
    # 如果是PDF，保存当前页为临时图片
    if self.current_file.lower().endswith('.pdf'):
        if self.original_image is not None:
            temp_image_path = os.path.join(tempfile.gettempdir(),
                                          f"ocr_pdf_page_{self.current_page}.jpg")
            cv2.imwrite(temp_image_path, self.original_image)
            analyze_path = temp_image_path
    
    # 分析图片
    result = self.analyzer.analyze(analyze_path)
    
    # 清理临时文件
    if temp_image_path and os.path.exists(temp_image_path):
        os.remove(temp_image_path)
```

### 3. 多页支持
- 使用◀ ▶ 按钮切换页面
- 页码计数器显示当前页/总页数
- 每次处理时分析当前显示的页面

## 工作流程

```
用户选择PDF文件
    ↓
load_pdf_preview() 渲染第一页
    ↓
显示在canvas中（original_image）
    ↓
用户点击Process按钮
    ↓
_process_thread() 检测到是PDF
    ↓
保存original_image为临时JPG
    ↓
analyzer.analyze(临时JPG路径)
    ↓
获取OCR结果
    ↓
删除临时文件
    ↓
创建可视化并显示结果
```

## 技术细节

### 为什么需要临时文件？
`analyzer.analyze()` 需要文件路径，不接受numpy数组或内存中的图片。因此必须：
1. 将PDF页面渲染为numpy/cv2格式（用于显示）
2. 保存为临时文件（用于OCR分析）

### 临时文件位置
```python
tempfile.gettempdir()  # 系统临时目录
# Windows: C:\Users\<user>\AppData\Local\Temp
# Linux/Mac: /tmp
```

### 文件命名
```python
f"ocr_pdf_page_{self.current_page}.jpg"
# 例如：ocr_pdf_page_0.jpg, ocr_pdf_page_1.jpg
```

### 分辨率设置
```python
fitz.Matrix(2, 2)  # 2倍缩放 = 144 DPI
# 默认DPI: 72
# 2x = 144 DPI (适合OCR)
# 可调整为更高分辨率：Matrix(3, 3) = 216 DPI
```

## 依赖项

### 必需
```bash
pip install PyMuPDF  # PDF渲染
pip install opencv-python  # 图像处理
pip install Pillow  # 图像格式转换
```

### 检查安装
```bash
python -c "import fitz; print(fitz.__version__)"
```

## 限制和改进建议

### 当前限制
1. **每次只处理一页**：需要切换页面后重新点击Process
2. **临时文件开销**：每次处理都要保存/删除临时文件
3. **无批量处理**：不支持一次处理PDF所有页面

### 未来改进
1. **批量处理模式**
   ```python
   def process_all_pages(self):
       results = []
       for page_num in range(self.total_pages):
           self.load_pdf_page(page_num)
           result = self.analyzer.analyze(temp_image)
           results.append(result)
       return results
   ```

2. **内存优化**
   ```python
   # 修改analyzer支持numpy数组输入
   def analyze(self, image_input: Union[str, np.ndarray]):
       if isinstance(image_input, np.ndarray):
           # 直接处理数组
       else:
           # 读取文件
   ```

3. **结果缓存**
   ```python
   # 缓存已处理的页面结果
   self.page_results = {}  # {page_num: result}
   ```

## 测试

### 创建测试PDF
运行 `create_test_pdf.py` 创建包含文本的测试PDF。

### 测试PDF加载
```bash
python test_pdf.py test_document.pdf
```

### 测试GUI
1. 启动GUI：`python src/ocr_gui_apple_style.py`
2. 拖拽或浏览选择PDF文件
3. 查看预览是否正确显示
4. 点击Process按钮
5. 检查OCR结果

## 故障排除

### PyMuPDF导入失败
```bash
pip install --upgrade PyMuPDF
```

### PDF无法打开
- 检查PDF是否损坏
- 某些加密PDF可能无法打开
- 尝试用其他PDF查看器验证文件

### 临时文件未清理
临时文件会在处理完成后自动删除。如果有残留：
```bash
# Windows
del %TEMP%\ocr_pdf_page_*.jpg
```

### OCR结果不准确
- 提高PDF渲染分辨率：`Matrix(3, 3)` 或 `Matrix(4, 4)`
- 尝试不同语言设置（ch/en/japan/korean）
- 启用GPU加速提高质量
