# 🎨 Apple Style GUI - 使用说明

## ✨ 新版本特点

### 完整的苹果设计风格
- ✅ **纯白背景** (#FFFFFF)
- ✅ **系统蓝色** (#007AFF) - 按钮和强调色
- ✅ **简洁布局** - 分栏设计
- ✅ **清晰字体** - Arial 系列

### 关键功能
1. **左右分栏布局**
   - 左侧（60%）：大图像预览区域
   - 右侧（40%）：结果展示

2. **图像可视化集成**
   - 选择文件后立即显示原图预览
   - 处理后自动显示可视化结果
   - OCR检测框和区域标注直接显示在界面中

3. **缩放控制**
   - 放大按钮（+）
   - 缩小按钮（−）
   - 重置按钮（Reset）

4. **标签页结果**
   - Summary：摘要信息
   - Regions：区域详情
   - JSON：原始数据

## 🚀 使用方法

### 1. 更新代码
```bash
cd C:\Users\kants\PycharmProjects\PythonProject\ocr-invoice-reader-gui
git pull origin main
```

### 2. 运行新版GUI
```bash
python src/ocr_gui_apple_style.py
```

### 3. 使用流程
1. 点击 "Select File" 选择文件
2. 左侧会显示图像预览
3. 点击 "Process Document"
4. 等待处理（首次约10秒，之后2-3秒）
5. **可视化结果自动显示在左侧Canvas中**
6. 右侧查看详细结果

## 📊 界面布局

```
┌──────────────────────────────────────────────────────────────┐
│  OCR Invoice Reader                    [Lang] [GPU] [Select] │
│  Enhanced structure analysis...                    [Process] │
├──────────────────────────┬───────────────────────────────────┤
│                          │  Results              [Export]    │
│     Preview              │  [Summary][Regions][JSON]         │
│  [−][Reset][+]           │  ┌─────────────────────────────┐ │
│                          │  │                             │ │
│  ┌────────────────────┐  │  │  ANALYSIS SUMMARY          │ │
│  │                    │  │  │                             │ │
│  │   可视化图像显示    │  │  │  File: xxx.jpg             │ │
│  │   Visualization    │  │  │  Method: coordinate_based  │ │
│  │   显示在这里        │  │  │  Regions: 3                │ │
│  │                    │  │  │                             │ │
│  └────────────────────┘  │  │  REGION TYPES               │ │
│                          │  │    • table: 2              │ │
│  📄 filename.jpg         │  │    • text: 1               │ │
└──────────────────────────┴───────────────────────────────────┘
```

## ⚡ 性能

- GUI启动：<1秒
- 图像预览：即时显示
- OCR处理：首次10秒，之后2-3秒
- 可视化显示：即时更新

## 🆚 版本对比

| 特性 | ocr_gui_simple.py | ocr_gui_apple_style.py |
|------|------------------|------------------------|
| 布局 | 单列垂直 | 分栏水平 |
| 图像显示 | ❌ 保存到文件 | ✅ 直接在GUI中 |
| 配色 | 默认灰色 | 苹果白+蓝 |
| 可视化 | 需要打开文件 | 自动显示 |
| 缩放 | ❌ | ✅ |

## 推荐

**立即使用新版本！**

```bash
python src/ocr_gui_apple_style.py
```

体验完整的苹果风格设计和集成的图像可视化！

