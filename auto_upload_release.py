#!/usr/bin/env python3
"""
自动创建压缩包并准备上传到GitHub Release
"""

import os
import sys
import tarfile
import shutil
from pathlib import Path
import subprocess

# 配置
DIST_DIR = Path("dist/OCR-Invoice-Reader-Optimized")
ARCHIVE_NAME = "OCR-Invoice-Reader-Optimized-v1.1.tar.gz"
ARCHIVE_PATH = Path("dist") / ARCHIVE_NAME

def create_tarball():
    """创建压缩包"""
    if not DIST_DIR.exists():
        print(f"❌ 错误: {DIST_DIR} 不存在")
        print("请先运行构建脚本")
        return False

    print(f"📦 创建压缩包...")
    print(f"   源: {DIST_DIR}")
    print(f"   目标: {ARCHIVE_PATH}")

    # 删除旧压缩包
    if ARCHIVE_PATH.exists():
        print(f"   删除旧文件...")
        ARCHIVE_PATH.unlink()

    # 创建压缩包
    with tarfile.open(ARCHIVE_PATH, "w:gz") as tar:
        # 切换到dist目录
        original_dir = os.getcwd()
        os.chdir("dist")

        # 添加整个文件夹
        tar.add(DIST_DIR.name, recursive=True)

        os.chdir(original_dir)

    # 检查结果
    if ARCHIVE_PATH.exists():
        size_mb = ARCHIVE_PATH.stat().st_size / (1024 * 1024)
        print(f"✅ 压缩包创建成功!")
        print(f"   文件: {ARCHIVE_PATH}")
        print(f"   大小: {size_mb:.1f} MB")
        return True
    else:
        print("❌ 压缩包创建失败")
        return False

def check_git_status():
    """检查git状态"""
    print("\n📋 检查Git状态...")

    try:
        # 检查是否有未提交的更改
        result = subprocess.run(
            ["git", "status", "--short"],
            capture_output=True,
            text=True
        )

        if result.stdout.strip():
            print("⚠️  有未提交的更改:")
            print(result.stdout)
            print("\n建议先提交更改:")
            print("  git add -A")
            print("  git commit -m 'build: 重新构建v1.1优化版'")
            print("  git push origin main")
            return False
        else:
            print("✅ Git状态干净")
            return True

    except Exception as e:
        print(f"⚠️  无法检查Git状态: {e}")
        return True

def create_release_instructions():
    """创建上传说明"""
    instructions = f"""
========================================
  🎉 准备完成! 现在上传到GitHub
========================================

✅ 已完成:
  [✓] 构建优化版exe
  [✓] 创建压缩包 ({ARCHIVE_PATH})
  [✓] 大小: {ARCHIVE_PATH.stat().st_size / (1024 * 1024):.1f} MB

🚀 上传步骤:

1️⃣  打开GitHub Release页面
   https://github.com/SyuuKasinn/ocr-invoice-reader-gui/releases/new

2️⃣  填写信息
   Tag:    v1.1
   Title:  v1.1 - 性能优化版 ⚡ (OCR识别快5倍)

3️⃣  上传文件
   拖放: {ARCHIVE_PATH}

4️⃣  复制描述 (见 上传Release步骤.txt)

5️⃣  发布
   ☑ Set as the latest release
   点击 "Publish release"

========================================

📂 压缩包位置: {ARCHIVE_PATH.absolute()}

📖 详细步骤: 上传Release步骤.txt

========================================
"""

    print(instructions)

    # 保存到文件
    with open("UPLOAD_INSTRUCTIONS.txt", "w", encoding="utf-8") as f:
        f.write(instructions)

    print("说明已保存到: UPLOAD_INSTRUCTIONS.txt")

def main():
    print()
    print("=" * 60)
    print("  GitHub Release 准备工具")
    print("=" * 60)
    print()

    # 1. 检查dist目录
    if not DIST_DIR.exists():
        print("❌ 错误: dist目录不存在")
        print("请先运行构建:")
        print("  build\\build_from_root.bat")
        print("或:")
        print("  pyinstaller build/specs/ocr_gui_optimized_fixed.spec")
        return 1

    # 2. 创建压缩包
    if not create_tarball():
        return 1

    # 3. 检查Git状态
    print()
    check_git_status()

    # 4. 创建上传说明
    print()
    create_release_instructions()

    # 5. 打开文件位置
    print("\n📂 正在打开文件位置...")
    try:
        if os.name == 'nt':  # Windows
            subprocess.run(["explorer", "/select,", str(ARCHIVE_PATH.absolute())])
        else:  # Linux/Mac
            subprocess.run(["xdg-open", str(ARCHIVE_PATH.parent)])
    except:
        pass

    print()
    print("=" * 60)
    print("  ✅ 准备完成! 现在可以上传到GitHub了")
    print("=" * 60)
    print()

    return 0

if __name__ == "__main__":
    sys.exit(main())
