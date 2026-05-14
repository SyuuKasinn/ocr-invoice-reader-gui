# Bug Fixes - Auto-Reprocessing

## 修复的问题

### 1. 自动重新处理不工作
**问题**：切换语言或GPU设置后，需要手动点击"Process"按钮才能重新处理

**原因**：
- `on_settings_changed` 检查 `self.current_result` 是否存在
- 但 `self.current_result` 只在 `display_results()` 中设置
- `display_results()` 在处理线程完成后才调用
- 导致第一次处理后，`current_result` 才被设置，但此时已经错过了设置改变的时机

**修复**：
```python
# 在 _process_thread 中，分析完成后立即设置 current_result
result = self.analyzer.analyze(self.current_file)
self.current_result = result  # ← 添加这一行
```

---

### 2. 可视化结果不正确显示
**问题**：设置改变后重新处理，但canvas没有显示新的可视化结果

**原因**：
- 当设置改变时，只重置了 `self.analyzer = None`
- 但没有重置 `self.visualizer = None`
- 在Unicode错误回退逻辑中，如果 `visualizer` 为 None，会导致AttributeError
- 错误处理不完善，导致可视化失败时没有正确的fallback

**修复**：
```python
def on_settings_changed(self, *args):
    if self.current_file and self.current_result and not self.processing:
        self.analyzer = None
        self.visualizer = None  # ← 添加这一行
        self.process_document()
```

同时改进了错误处理：
```python
except UnicodeEncodeError as e:
    try:
        if self.visualizer:  # ← 检查visualizer是否存在
            self.annotated_image = self.visualizer.visualize_regions(...)
        else:
            # Fallback to original image
```

---

## 测试步骤

### 测试自动重新处理

1. **启动GUI**
   ```bash
   python src/ocr_gui_apple_style.py
   ```

2. **加载文件**
   - 拖拽图片到canvas，或点击"Browse"选择文件

3. **首次处理**
   - 点击"Process Document"按钮
   - 等待处理完成，查看可视化结果

4. **切换设置触发自动重新处理**
   - 在Language下拉框中选择不同语言（如从"ch"切换到"en"）
   - **预期结果**：GUI自动开始重新处理，无需手动点击Process按钮
   - 观察console输出，应该看到新的分析过程

5. **切换GPU设置**
   - 勾选/取消"Use GPU"复选框
   - **预期结果**：同样自动触发重新处理

6. **验证可视化更新**
   - 观察canvas区域，应该显示新的可视化结果（带有检测框）
   - 切换"Summary/Regions/JSON"标签页，可视化结果应该保持显示

---

## 技术细节

### 设置监听机制
使用Tkinter的变量trace功能：
```python
self.lang_var.trace_add('write', self.on_settings_changed)
self.gpu_var.trace_add('write', self.on_settings_changed)
```

### 处理流程
```
用户改变设置
    ↓
trace回调触发
    ↓
检查条件：current_file存在 && current_result存在 && 不在处理中
    ↓
重置analyzer和visualizer（应用新配置）
    ↓
调用process_document()
    ↓
创建新的analyzer（使用新设置）
    ↓
分析文档
    ↓
创建可视化
    ↓
更新canvas显示
```

### 防止重复处理
- 检查 `self.processing` 标志，确保不会在处理过程中再次触发
- 只在已有处理结果时才自动重新处理

---

## 已知限制

1. **Unicode可视化问题**
   - Windows console编码(cp932)无法显示某些Unicode字符
   - 当前fallback：显示检测框但不显示文字标签
   - 不影响OCR识别准确性，只影响可视化效果

2. **PDF多页处理**
   - 当前每次只处理当前显示的页面
   - 切换PDF页面后需要重新点击Process按钮

---

## 下次改进建议

1. **批量处理**：支持处理PDF的所有页面
2. **结果缓存**：缓存不同设置下的处理结果，切换设置时无需重新计算
3. **进度指示**：显示更详细的处理进度（加载模型 → OCR → 结构分析 → 可视化）
4. **Unicode支持**：使用PIL替代cv2.putText来渲染文字，支持所有Unicode字符
