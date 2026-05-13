#!/usr/bin/env python3
"""
使用GitHub API创建Release并上传文件
需要: pip install requests
"""

import os
import sys
import json
import requests
from pathlib import Path

# 配置
REPO_OWNER = "SyuuKasinn"
REPO_NAME = "ocr-invoice-reader-gui"
TAG_NAME = "v1.1"
RELEASE_NAME = "v1.1 - 性能优化版 ⚡ (OCR识别快5倍)"
FILE_PATH = "dist/OCR-Invoice-Reader-Optimized-v1.1.tar.gz"

RELEASE_BODY = """# 🎉 v1.1 - 性能优化版

OCR识别速度提升 **5倍**！启动速度提升 **2.5倍**！

## ⚡ 性能提升

| 场景 | v1.0 | v1.1 | 提升 |
|------|------|------|------|
| 程序启动 | 5秒 | 2秒 | **2.5倍** ⚡ |
| 首次识别 | 15秒 | 15秒 | - |
| 第2次识别 | 15秒 | **3秒** | **5倍** ⚡⚡⚡ |
| 10个文件 | 150秒 | **42秒** | **3.6倍** ⚡⚡ |

## 🔑 核心改进

**1. 预加载OCR引擎**
- 启动时加载一次模型
- 后续识别直接调用
- 不重复加载,快5倍

**2. 目录模式打包**
- 不需要每次解压
- 启动快2.5倍

**3. 启动画面**
- 显示加载进度
- 改善用户体验

**4. 项目重构**
- 清晰的目录结构
- 完善的文档

## 📥 下载

**Windows EXE:** OCR-Invoice-Reader-Optimized-v1.1.tar.gz (193MB)

**使用方法:**
1. 下载并解压
2. 双击 `OCR-Invoice-Reader-Optimized.exe`
3. 等待启动画面 (首次约10秒)
4. 拖放文件开始识别

## 💡 使用技巧

**连续处理:**
- 文件1: 15秒 (首次)
- 文件2: 3秒 ⚡
- 文件3: 3秒 ⚡

**选择模式:**
- 快速 → ocr-simple
- 推荐 → ocr-extract
- 精确 → ocr-enhanced

**GPU加速:**
- 勾选 "Use GPU"
- 需要 NVIDIA + CUDA
- 3秒 → 1.5秒

## 📖 文档

- [快速开始](docs/guides/quick-start.txt)
- [性能优化](docs/guides/performance-optimization.md)
- [完整变更](docs/releases/v1.1.md)

## ⚠️ 首次运行

首次运行会下载模型 (~300MB):
- 位置: `C:\\Users\\用户名\\.paddleocr\\`
- 只需下载一次

---

**⚡ 享受5倍速OCR!**
"""

def create_release_with_api():
    """使用GitHub API创建Release"""

    # 从git获取token
    # 你需要创建Personal Access Token: https://github.com/settings/tokens
    # 权限: repo (Full control of private repositories)

    token = os.environ.get('GITHUB_TOKEN')

    if not token:
        print("=" * 60)
        print("需要GitHub Personal Access Token")
        print("=" * 60)
        print()
        print("步骤:")
        print("1. 访问: https://github.com/settings/tokens")
        print("2. 点击 'Generate new token (classic)'")
        print("3. 勾选 'repo' 权限")
        print("4. 复制token")
        print("5. 设置环境变量:")
        print("   Windows: set GITHUB_TOKEN=your_token")
        print("   Linux:   export GITHUB_TOKEN=your_token")
        print()
        print("或者使用GitHub网页手动创建:")
        print(f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/new")
        print()
        return False

    # 检查文件
    if not os.path.exists(FILE_PATH):
        print(f"错误: 文件不存在 {FILE_PATH}")
        return False

    file_size = os.path.getsize(FILE_PATH) / (1024 * 1024)
    print(f"文件: {FILE_PATH}")
    print(f"大小: {file_size:.1f} MB")
    print()

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # 1. 创建Release
    print("[1/2] 创建Release...")

    release_data = {
        "tag_name": TAG_NAME,
        "target_commitish": "main",
        "name": RELEASE_NAME,
        "body": RELEASE_BODY,
        "draft": False,
        "prerelease": False
    }

    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases"

    response = requests.post(url, headers=headers, json=release_data)

    if response.status_code == 201:
        release = response.json()
        print(f"✅ Release创建成功!")
        print(f"   URL: {release['html_url']}")
        upload_url = release['upload_url'].split('{')[0]
    else:
        print(f"❌ 创建失败: {response.status_code}")
        print(response.text)
        return False

    # 2. 上传文件
    print()
    print("[2/2] 上传文件...")
    print(f"   上传 {file_size:.1f} MB, 请稍候...")

    filename = os.path.basename(FILE_PATH)

    upload_headers = headers.copy()
    upload_headers["Content-Type"] = "application/gzip"

    with open(FILE_PATH, 'rb') as f:
        file_data = f.read()

    upload_response = requests.post(
        f"{upload_url}?name={filename}",
        headers=upload_headers,
        data=file_data
    )

    if upload_response.status_code == 201:
        asset = upload_response.json()
        print(f"✅ 文件上传成功!")
        print(f"   下载: {asset['browser_download_url']}")
        print()
        print("=" * 60)
        print("🎉 Release创建完成!")
        print("=" * 60)
        print(f"Release: {release['html_url']}")
        print(f"下载: {asset['browser_download_url']}")
        return True
    else:
        print(f"❌ 上传失败: {upload_response.status_code}")
        print(upload_response.text)
        return False

if __name__ == "__main__":
    print()
    print("=" * 60)
    print("GitHub Release创建工具")
    print("=" * 60)
    print()

    success = create_release_with_api()

    if success:
        print()
        print("下一步:")
        print("1. 访问Release页面确认")
        print("2. 测试下载链接")
        print("3. 分享给用户")
    else:
        print()
        print("创建失败,请使用手动方式:")
        print(f"https://github.com/{REPO_OWNER}/{REPO_NAME}/releases/new")
        print()
        print("详细步骤见: CREATE_RELEASE.md")
