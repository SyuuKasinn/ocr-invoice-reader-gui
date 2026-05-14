# PDF Page Cache Feature

## 问题

用户报告的两个问题：
1. **多页PDF只显示第一页结果**：切换到第2页后，第1页的处理结果看不到了
2. **返回已处理页面结果消失**：第1页处理后 → 切换到第2页 → 返回第1页，之前的结果消失了

## 原因

原始实现没有保存每个页面的处理状态。每次切换页面时：
- `self.original_image` 被新页面覆盖
- `self.annotated_image` 被清空
- `self.current_result` 被清空

导致之前处理的结果丢失。

## 解决方案：页面状态缓存

### 1. 添加缓存数据结构

```python
# 在 __init__ 中添加
self.page_cache = {}  # {page_num: {'result': result, 'annotated_image': img, 'original_image': img}}
```

### 2. 保存页面状态

```python
def save_current_page_state(self):
    """保存当前页面状态到缓存"""
    if self.current_file and self.current_file.lower().endswith('.pdf'):
        self.page_cache[self.current_page] = {
            'result': self.current_result,
            'annotated_image': self.annotated_image.copy() if self.annotated_image is not None else None,
            'original_image': self.original_image.copy() if self.original_image is not None else None
        }
```

**何时保存**：
- 处理完成后自动保存
- 切换页面前保存当前页状态

### 3. 恢复页面状态

```python
def load_pdf_page(self, page_num):
    """加载PDF页面"""
    # 先检查缓存
    if page_num in self.page_cache:
        cached = self.page_cache[page_num]
        self.original_image = cached['original_image']
        self.annotated_image = cached['annotated_image']
        self.current_result = cached['result']
        
        # 显示缓存的图像
        display_img = self.annotated_image if self.annotated_image is not None else self.original_image
        self.display_image(display_img)
        
        # 恢复结果显示
        if self.current_result:
            self.display_results(self.current_result)
        
        return
    
    # 如果不在缓存中，从PDF渲染新页面
    # ...
```

## 工作流程

### 场景1：处理第1页

```
用户加载PDF
    ↓
显示第1页预览
    ↓
用户点击Process
    ↓
OCR分析第1页
    ↓
创建可视化
    ↓
显示结果
    ↓
自动保存到 page_cache[0] ✓
```

### 场景2：切换到第2页

```
用户点击"下一页▶"
    ↓
next_page() 触发
    ↓
save_current_page_state() - 保存第1页状态 ✓
    ↓
load_pdf_page(1) - 加载第2页
    ↓
检查 page_cache[1] - 不存在
    ↓
从PDF渲染第2页
    ↓
显示第2页预览（未处理）
```

### 场景3：返回第1页

```
用户点击"◀上一页"
    ↓
prev_page() 触发
    ↓
save_current_page_state() - 保存第2页状态
    ↓
load_pdf_page(0) - 加载第1页
    ↓
检查 page_cache[0] - 存在！✓
    ↓
从缓存恢复：
  - original_image (原始图片)
  - annotated_image (可视化结果)
  - current_result (OCR结果)
    ↓
显示 annotated_image ✓
    ↓
恢复结果文本显示 ✓
```

## 缓存管理

### 何时清空缓存

```python
def load_file(self, path):
    # 加载新文件时清空缓存
    self.page_cache = {}
```

### 内存考虑

每个页面缓存包含：
- `original_image`: ~5-10MB (取决于PDF分辨率)
- `annotated_image`: ~5-10MB
- `result`: ~100KB (JSON数据)

10页PDF ≈ 100-200MB内存占用

**优化建议**：
- 限制缓存大小，使用LRU策略
- 只缓存最近访问的N页（例如N=5）
- 压缩图像数据

## 用户体验提升

### 之前
❌ 第1页处理 → 切换第2页 → 返回第1页 → **结果丢失**  
❌ 需要重新点击Process按钮  
❌ 浪费时间重新处理

### 现在
✅ 第1页处理 → 切换第2页 → 返回第1页 → **结果保留**  
✅ 立即显示之前的OCR结果和可视化  
✅ 无需重新处理

## 测试步骤

1. **加载多页PDF**（使用test_document.pdf，有2页）

2. **处理第1页**
   - 点击Process按钮
   - 等待处理完成
   - 验证可视化和结果显示

3. **切换到第2页**
   - 点击"下一页▶"按钮
   - 验证显示第2页（未处理状态）

4. **返回第1页**
   - 点击"◀上一页"按钮
   - **验证**：应该立即显示第1页的可视化结果
   - **验证**：结果文本应该恢复显示

5. **处理第2页**
   - 在第2页点击Process
   - 验证第2页处理结果

6. **来回切换**
   - 多次在第1页和第2页之间切换
   - 验证两页的结果都能正确保留和恢复

## 技术细节

### 图像深拷贝

```python
self.annotated_image.copy()  # 创建numpy数组副本
```

为什么需要copy()？
- 如果不复制，缓存中存储的是引用
- 后续修改会影响缓存的数据
- copy()确保缓存数据独立

### 结果恢复

```python
if self.current_result:
    self.display_results(self.current_result)
```

恢复包括：
- Summary标签页内容
- Regions标签页内容
- JSON标签页内容

### 性能优化

- 只在切换页面前保存（懒保存）
- 使用字典O(1)查找
- 图像数据在内存中，无磁盘I/O

## 未来改进

### LRU缓存策略

```python
from collections import OrderedDict

class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        super().__init__()
    
    def __setitem__(self, key, value):
        if key in self:
            self.move_to_end(key)
        super().__setitem__(key, value)
        if len(self) > self.capacity:
            oldest = next(iter(self))
            del self[oldest]
```

### 进度指示

```python
# 在页面导航显示哪些页面已处理
self.page_label.config(text=f"{page_num + 1} / {total_pages} {'✓' if processed else ''}")
```

### 批量处理

```python
def process_all_pages(self):
    """处理PDF所有页面"""
    for i in range(self.total_pages):
        self.load_pdf_page(i)
        self.process_document()
        # 等待处理完成
```
