@echo off
REM ============================================
REM  完整构建和打包流程
REM ============================================

echo.
echo ============================================
echo   OCR Invoice Reader - 完整构建流程
echo ============================================
echo.

REM 检查是否在项目根目录
if not exist "src\ocr_gui_optimized.py" (
    echo [错误] 必须从项目根目录运行!
    echo 当前目录: %CD%
    pause
    exit /b 1
)

echo [1/4] 清理旧版本...
if exist "dist" rmdir /s /q dist
if exist "build\ocr_gui_optimized" rmdir /s /q build\ocr_gui_optimized
echo 清理完成

echo.
echo [2/4] 检查依赖...
pip show pyinstaller >nul 2>&1 || (
    echo 安装 PyInstaller...
    pip install pyinstaller
)

echo.
echo [3/4] 构建exe...
echo 这需要 5-10 分钟, 请耐心等待...
echo.
pyinstaller --clean build\specs\ocr_gui_optimized.spec

if errorlevel 1 (
    echo.
    echo [错误] 构建失败!
    pause
    exit /b 1
)

echo.
echo [4/4] 创建压缩包...
python auto_upload_release.py

if errorlevel 1 (
    echo [警告] 压缩包创建失败, 但exe已构建成功
)

echo.
echo ============================================
echo   [成功] 构建完成!
echo ============================================
echo.
echo EXE位置: dist\OCR-Invoice-Reader-Optimized\
echo 压缩包:   dist\OCR-Invoice-Reader-Optimized-v1.1.tar.gz
echo.
echo 下一步: 上传到GitHub Release
echo 说明: UPLOAD_INSTRUCTIONS.txt
echo.
pause
explorer dist
