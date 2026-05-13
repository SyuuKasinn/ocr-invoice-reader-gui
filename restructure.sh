#!/bin/bash
# 项目重构脚本

echo "=== 开始重构项目结构 ==="

# 1. 创建目录结构
echo "创建目录..."
mkdir -p src/common
mkdir -p build/specs
mkdir -p docs/{guides,development,releases}
mkdir -p scripts/{demo,utils}
mkdir -p tests
mkdir -p archive

# 2. 移动源码
echo "移动源码..."
mv ocr_gui.py src/ 2>/dev/null || true
mv ocr_gui_optimized.py src/ 2>/dev/null || true
mv test_optimized.py tests/ 2>/dev/null || true

# 3. 移动构建配置
echo "移动构建配置..."
mv ocr_gui.spec build/specs/ 2>/dev/null || true
mv ocr_gui_optimized.spec build/specs/ 2>/dev/null || true
mv ocr_gui_simple.spec build/specs/ 2>/dev/null || true
mv build_exe.bat build/build_original.bat 2>/dev/null || true
mv build_optimized.bat build/build.bat 2>/dev/null || true

# 4. 移动运行脚本
echo "移动运行脚本..."
mv run.bat scripts/ 2>/dev/null || true
mv run.sh scripts/ 2>/dev/null || true
mv run_optimized.bat scripts/run.bat 2>/dev/null || true

# 5. 移动演示脚本
echo "移动演示脚本..."
mv auto_demo.py scripts/demo/ 2>/dev/null || true
mv capture_screenshots.py scripts/demo/ 2>/dev/null || true
mv create_demo_gif.py scripts/demo/ 2>/dev/null || true
mv record_demo.ps1 scripts/demo/ 2>/dev/null || true
mv record_demo.sh scripts/demo/ 2>/dev/null || true

# 6. 移动工具脚本
echo "移动工具脚本..."
mv 打开压缩包位置.bat scripts/utils/open_dist.bat 2>/dev/null || true

# 7. 移动文档
echo "移动文档..."
# 用户指南
mv INSTALLATION.md docs/guides/installation.md 2>/dev/null || true
mv 快速开始.txt docs/guides/quick-start.txt 2>/dev/null || true
mv PERFORMANCE_OPTIMIZATION.md docs/guides/performance-optimization.md 2>/dev/null || true

# 开发文档
mv BUILD_GUIDE.md docs/development/building.md 2>/dev/null || true
mv PACKAGING_GUIDE.md docs/development/packaging.md 2>/dev/null || true
mv BUILD_SUCCESS.md docs/development/build-success.md 2>/dev/null || true
mv BUILD_OPTIMIZED_README.md docs/development/optimized-build.md 2>/dev/null || true

# 发布说明
mv RELEASE_NOTES.md docs/releases/v1.0.md 2>/dev/null || true
mv RELEASE_v1.1.md docs/releases/v1.1.md 2>/dev/null || true

# 其他文档
mv GITHUB_SETUP.md docs/development/ 2>/dev/null || true
mv PROJECT_SUMMARY.md docs/development/ 2>/dev/null || true
mv SCREENSHOT_GUIDE.md docs/development/ 2>/dev/null || true
mv RECORDING_GUIDE.md docs/development/ 2>/dev/null || true
mv 如何创建GitHub_Release.md docs/development/github-release.md 2>/dev/null || true
mv 文件位置说明.txt docs/development/file-locations.txt 2>/dev/null || true
mv 🎉_完成总结.txt docs/development/completion-summary.txt 2>/dev/null || true

# 8. 归档旧文件
echo "归档旧文件..."
mv OCR-Invoice-Reader-GUI-v1.0-Windows.zip archive/ 2>/dev/null || true

echo ""
echo "=== 重构完成 ==="
echo "新的目录结构:"
tree -L 2 -I 'build|dist|.git|__pycache__|*.pyc' || ls -R

