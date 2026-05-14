# Batch PDF Processing Feature

## 功能概述

新增"Process All Pages"选项，一次性处理PDF的所有页面。

## 问题

用户反馈：
> "多页pdf传入，只识别了第一页"

原始行为：
- 加载PDF后只显示第一页
- 点击Process只处理当前显示的页面
- 需要手动切换到每一页并分别点击Process
- 对于50页的PDF，需要切换50次

## 解决方案

添加"Process All Pages (PDF)"复选框，勾选后一次性处理所有页面。

### UI变化

```
Settings:
  Language: [ch ▼]  Use GPU ☐  Process All Pages (PDF) ☐
```

- 加载PDF时自动启用此复选框
- 加载图片时自动禁用此复选框
- 默认不勾选（保持原有行为）

## 使用方法

### 单页处理（原有模式）

1. 加载PDF
2. 不勾选"Process All Pages"
3. 点击Process按钮 → 只处理当前页
4. 切换到其他页面，再次点击Process处理该页

### 批量处理（新功能）

1. 加载PDF
2. **勾选"Process All Pages (PDF)"**
3. 点击Process按钮 → **自动处理所有页面**
4. 等待处理完成
5. 使用◀ ▶按钮浏览各页的结果

## 处理流程

### 批量处理时的步骤

```
点击Process按钮（Process All Pages已勾选）
    ↓
_process_all_pdf_pages() 执行
    ↓
对每一页：
  1. 检查缓存（如果已处理，跳过）
  2. 从PDF渲染页面图像
  3. 保存为临时JPG
  4. OCR分析
  5. 创建可视化
  6. 保存到page_cache
  7. 更新进度："Processing page X/Y..."
    ↓
编译所有页面结果
    ↓
显示汇总报告
    ↓
加载第一页的可视化结果
```

### 进度显示

状态栏实时更新：
- 🔄 Loading OCR engine...
- 🔍 Processing page 1/10...
- 🔍 Processing page 2/10...
- ...
- 📊 Compiling results...
- ✓ Processed 10 pages

## 结果显示

### Summary标签页

```
PDF Document: 10 pages
================================================================================

Page 1: 5 regions detected
Page 2: 3 regions detected
Page 3: 7 regions detected
...
Page 10: 4 regions detected

Total regions across all pages: 52
```

### Regions标签页

显示所有页面的详细区域信息：

```
================================================================================
PAGE 1
================================================================================

Region 1:
  Type: table
  BBox: [100, 200, 500, 400]
  Confidence: 95.34%
  Text: Invoice Number: INV-001...

Region 2:
  ...

================================================================================
PAGE 2
================================================================================

Region 1:
  ...
```

### JSON标签页

完整的结构化数据：

```json
{
  "document": "invoice_multi_page.pdf",
  "total_pages": 10,
  "pages": [
    {
      "page": 1,
      "regions": [
        {
          "type": "table",
          "bbox": [100, 200, 500, 400],
          "confidence": 0.9534,
          "text": "..."
        }
      ]
    },
    {
      "page": 2,
      "regions": [...]
    }
  ]
}
```

## 技术实现

### 关键函数

```python
def _process_all_pdf_pages(self):
    """处理PDF所有页面"""
    all_results = []
    
    for page_num in range(self.total_pages):
        # 更新状态
        self.update_status(f"🔍 Processing page {page_num + 1}/{self.total_pages}...")
        
        # 检查缓存
        if page_num in self.page_cache:
            # 使用缓存的结果
            all_results.append(self.page_cache[page_num]['result'])
            continue
        
        # 渲染页面
        page_image = render_pdf_page(page_num)
        
        # 分析
        result = self.analyzer.analyze(page_image)
        
        # 可视化
        annotated = self.visualizer.visualize_regions(page_image, result)
        
        # 缓存
        self.page_cache[page_num] = {
            'result': result,
            'annotated_image': annotated,
            'original_image': page_image
        }
        
        all_results.append(result)
    
    # 显示汇总结果
    self._display_all_pages_results(all_results)
```

### 缓存利用

如果某些页面已经单独处理过：
- 批量处理时会跳过这些页面
- 直接使用缓存的结果
- 节省处理时间

示例：
```
用户先处理了第1、3、5页
然后勾选"Process All Pages"再次点击Process
→ 只处理第2、4、6-10页
→ 第1、3、5页使用缓存结果
```

## 性能考虑

### 处理时间

假设单页处理时间 = 3秒

| 页数 | 预计时间 | 实际体验 |
|------|---------|---------|
| 5页  | 15秒    | 可接受   |
| 10页 | 30秒    | 良好     |
| 50页 | 2.5分钟 | 需要耐心 |
| 100页| 5分钟   | 较慢     |

### 内存占用

每页缓存 ≈ 15-20MB

| 页数 | 内存占用 |
|------|---------|
| 10页 | ~150-200MB |
| 50页 | ~750MB-1GB |
| 100页| ~1.5-2GB   |

### 优化建议

1. **进度条改进**：使用确定性进度条（0-100%）
2. **后台导出**：处理完成后自动保存结果
3. **增量保存**：每处理N页保存一次中间结果
4. **并行处理**：如果有多核CPU，可以并行处理多页

## 错误处理

### 单页失败

如果某一页处理失败：
- 记录错误信息
- 继续处理其他页面
- 在结果中标注失败页面

```
Page 1: 5 regions detected
Page 2: ERROR - Cannot read image
Page 3: 7 regions detected
```

### 完全失败

如果OCR引擎加载失败：
- 显示错误对话框
- 停止处理
- 保留已处理页面的结果

## 用户体验优化

### 推荐工作流程

**场景1：快速预览**
1. 不勾选"Process All Pages"
2. 只处理几个关键页面
3. 快速查看文档内容

**场景2：完整分析**
1. 勾选"Process All Pages"
2. 批量处理所有页面
3. 导出完整JSON结果
4. 用于后续数据分析

### 取消处理

目前不支持中途取消批量处理。

**未来改进**：
```python
# 添加取消按钮
self.cancel_btn = tk.Button(text="Cancel", command=self.cancel_processing)

# 在处理循环中检查标志
for page_num in range(self.total_pages):
    if self.cancel_requested:
        break
    # ... 处理页面
```

## 测试方法

### 准备测试PDF

使用提供的`create_test_pdf.py`创建多页测试文档：

```python
# 修改脚本创建更多页面
for i in range(10):  # 创建10页
    c.setFont("Helvetica", 20)
    c.drawString(100, 750, f"Test Document - Page {i+1}")
    c.showPage()
```

### 测试步骤

1. **加载多页PDF**
   ```bash
   python src/ocr_gui_apple_style.py
   # 加载test_document.pdf（2页）或其他多页PDF
   ```

2. **测试单页模式**
   - 不勾选"Process All Pages"
   - 点击Process
   - 验证只处理当前页

3. **测试批量模式**
   - 勾选"Process All Pages"
   - 点击Process
   - 观察状态栏进度
   - 验证Summary显示所有页面
   - 切换页面查看各页可视化

4. **测试缓存**
   - 先处理第1页（单页模式）
   - 切换到第2页，勾选"Process All Pages"
   - 点击Process
   - 验证第1页使用缓存（console应显示"using cached result"）

5. **测试结果导出**
   - 批量处理后
   - 点击Export按钮
   - 验证JSON包含所有页面数据

## 限制和注意事项

1. **不可中断**：处理开始后无法取消（除非关闭程序）
2. **内存占用**：大文档（>50页）可能占用较多内存
3. **UI冻结**：虽然使用线程，但大量页面时仍可能感觉卡顿
4. **错误恢复**：如果程序崩溃，已处理结果会丢失

## 与现有功能的兼容性

### 页面缓存

✅ 完全兼容
- 批量处理的结果会保存到page_cache
- 可以正常切换页面查看结果

### 设置变更自动重处理

✅ 部分兼容
- 如果勾选了"Process All Pages"，改变设置会触发所有页面重新处理
- 警告：可能需要较长时间

### 可视化显示

✅ 完全兼容
- 每页都有独立的可视化结果
- 切换页面时正确显示对应页面的可视化

## 未来改进方向

1. **真正的进度条**：显示确切百分比
2. **取消按钮**：允许中途停止
3. **后台任务队列**：不阻塞UI
4. **并行处理**：利用多核CPU
5. **增量导出**：处理一页保存一页
6. **页面选择**：只处理指定页面（如1-10, 15, 20-25）
