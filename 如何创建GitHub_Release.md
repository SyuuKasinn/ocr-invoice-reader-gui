# 如何创建GitHub Release v1.1

## 📍 压缩包位置

```
C:\Users\kants\ocr-invoice-reader-gui\dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz
```

**大小:** 193MB  
**包含:** 完整的优化版程序 + 所有依赖库

---

## 🚀 创建Release步骤

### 方式1: 通过GitHub网页 (推荐)

1. **打开项目页面**
   ```
   https://github.com/SyuuKasinn/ocr-invoice-reader-gui
   ```

2. **点击 "Releases"**
   - 在右侧边栏找到 "Releases"
   - 或直接访问: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases

3. **创建新Release**
   - 点击 "Create a new release" 或 "Draft a new release"

4. **填写Release信息**

   **Tag version (标签):**
   ```
   v1.1
   ```

   **Release title (标题):**
   ```
   v1.1 - 性能优化版 (OCR识别快5倍)
   ```

   **Description (描述):**
   - 复制 `RELEASE_v1.1.md` 的内容
   - 或使用下面的简化版本

5. **上传文件**
   - 点击 "Attach binaries by dropping them here or selecting them"
   - 选择: `dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz`
   - 等待上传完成 (193MB可能需要几分钟)

6. **发布**
   - 勾选 "Set as the latest release" 
   - 点击 "Publish release"

---

### 方式2: 通过GitHub CLI (如果已安装gh命令)

```bash
# 1. 登录 (首次使用)
gh auth login

# 2. 创建Release并上传文件
gh release create v1.1 \
  dist/OCR-Invoice-Reader-Optimized-v1.1.tar.gz \
  --title "v1.1 - 性能优化版 (OCR识别快5倍)" \
  --notes-file RELEASE_v1.1.md

# 3. 查看Release
gh release view v1.1 --web
```

---

## 📝 Release描述 (简化版)

可以复制下面的内容到GitHub Release描述:

```markdown
# 🎉 v1.1 - 性能优化版

## ⚡ 重大更新

OCR识别速度提升 **5倍**！启动速度提升 **2.5倍**！

## 📊 性能对比

| 场景 | 原版 | 优化版 | 提升 |
|------|------|--------|------|
| 程序启动 | 5秒 | 2秒 | **2.5倍** ⚡ |
| 首次识别 | 15秒 | 15秒 | - |
| 第2次识别 | 15秒 | **3秒** | **5倍** ⚡⚡ |
| 批量10个文件 | 150秒 | **42秒** | **3.6倍** ⚡⚡ |

## 🔑 核心改进

### 1. 预加载OCR引擎
- 启动时加载一次模型
- 后续识别直接调用
- 第2次起快5倍

### 2. 目录模式打包
- 不需要每次解压
- 启动快2.5倍

### 3. 启动画面
- 显示加载进度
- 改善用户体验

## 📦 下载

### Windows EXE (推荐)

**文件:** `OCR-Invoice-Reader-Optimized-v1.1.tar.gz` (193MB)

**使用方法:**
1. 下载并解压
2. 双击 `OCR-Invoice-Reader-Optimized.exe`
3. 等待启动画面 (首次约10秒)
4. 拖放文件开始识别

### Python源码

```bash
git clone https://github.com/SyuuKasinn/ocr-invoice-reader-gui.git
cd ocr-invoice-reader-gui
pip install tkinterdnd2 Pillow paddleocr opencv-python
python ocr_gui_optimized.py
```

## 💡 使用技巧

### 连续处理多个文件
```
不要关闭程序,连续拖放:
- 文件1: 15秒 (首次)
- 文件2: 3秒 ⚡ (快5倍!)
- 文件3: 3秒 ⚡
```

### 选择合适的OCR模式
```
ocr-simple   → 最快 (1-2秒)
ocr-extract  → 推荐 (3-5秒)
ocr-enhanced → 最准确 (5-8秒)
```

### 启用GPU加速
```
勾选 "Use GPU"
需要: NVIDIA显卡 + CUDA
效果: 3秒 → 1.5秒 (再快1倍!)
```

## 📖 完整文档

- [性能优化指南](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/blob/main/PERFORMANCE_OPTIMIZATION.md)
- [打包指南](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/blob/main/PACKAGING_GUIDE.md)
- [项目说明](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/blob/main/README.md)

## 🆕 完整变更

查看 [RELEASE_v1.1.md](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/blob/main/RELEASE_v1.1.md) 获取详细信息。

## 🐛 反馈

遇到问题? [提交Issue](https://github.com/SyuuKasinn/ocr-invoice-reader-gui/issues)

---

**🎉 享受快速的OCR体验！**
```

---

## ✅ 完成后

Release创建完成后,用户可以:

1. **直接下载exe**
   ```
   访问: https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/latest
   下载: OCR-Invoice-Reader-Optimized-v1.1.tar.gz
   ```

2. **查看下载统计**
   - GitHub会自动统计下载次数
   - 可以看到有多少人使用

3. **分享链接**
   ```
   最新版下载:
   https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/latest
   ```

---

## 📸 创建Release的截图示例

1. **找到Releases**
   ```
   项目页面 → 右侧 "Releases" → "Create a new release"
   ```

2. **填写信息**
   ```
   Tag: v1.1
   Title: v1.1 - 性能优化版 (OCR识别快5倍)
   Description: [复制上面的内容]
   ```

3. **上传文件**
   ```
   拖放: OCR-Invoice-Reader-Optimized-v1.1.tar.gz
   ```

4. **发布**
   ```
   勾选: "Set as the latest release"
   点击: "Publish release"
   ```

---

## 🎯 下一步

创建Release后,可以:

1. **更新README**
   - 在README中添加下载链接
   - 添加Performance徽章

2. **宣传**
   - 在相关社区分享
   - 更新项目介绍

3. **收集反馈**
   - 监控Issues
   - 收集用户建议
   - 准备下一个版本

---

**需要帮助?** 如果遇到问题,随时问我!
