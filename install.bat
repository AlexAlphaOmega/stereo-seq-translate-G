@echo off
REM ============================================
REM  Gemini Style Translate skill 安装脚本 (Windows)
REM  用法: 双击 install.bat 或命令行运行
REM ============================================
setlocal
set SKILL_NAME=gemini-style-translate
set SRC_DIR=%~dp0%SKILL_NAME%
set DEST_DIR=%USERPROFILE%\.claude\skills\%SKILL_NAME%

echo === 安装 gemini-style-translate skill ===
echo 来源: %SRC_DIR%
echo 目标: %DEST_DIR%

REM 备份已有
if exist "%DEST_DIR%" (
  echo 检测到已有安装，备份到 %DEST_DIR%.bak
  if exist "%DEST_DIR%.bak" rmdir /s /q "%DEST_DIR%.bak"
  move "%DEST_DIR%" "%DEST_DIR%.bak" >nul
)

REM 复制
if not exist "%USERPROFILE%\.claude\skills" mkdir "%USERPROFILE%\.claude\skills"
xcopy /e /i /q "%SRC_DIR%" "%DEST_DIR%" >nul
echo 已安装到 %DEST_DIR%

echo.
echo === 验证 ===
if exist "%DEST_DIR%\SKILL.md" (
  echo SKILL.md 存在
) else (
  echo SKILL.md 缺失，安装失败
  exit /b 1
)
echo.
echo === 使用 ===
echo 重启 Claude Code 后，说「用 Gemini 风格翻译：中文」即可触发该 skill。
echo.
endlocal