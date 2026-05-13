@echo off
echo.
echo ========================================
echo   打开压缩包位置
echo ========================================
echo.
echo 位置: dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz
echo.

REM 检查压缩包是否存在
if exist "dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz" (
    echo [OK] 压缩包存在
    echo 大小:
    dir "dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz" | findstr "tar.gz"
    echo.
    echo 正在打开文件夹...
    explorer /select,"dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz"
) else (
    echo [错误] 压缩包不存在!
    echo.
    echo 可能原因:
    echo 1. 还未构建
    echo 2. 文件被移动或删除
    echo.
    pause
)
