#!/usr/bin/env bash
# ============================================
#  Gemini Style Translate skill 安装脚本 (Mac/Linux)
#  用法: bash install.sh
# ============================================
set -e

SKILL_NAME="gemini-style-translate"
SRC_DIR="$(cd "$(dirname "$0")" && pwd)/$SKILL_NAME"
DEST_DIR="$HOME/.claude/skills/$SKILL_NAME"

echo "=== 安装 $SKILL_NAME skill ==="
echo "来源: $SRC_DIR"
echo "目标: $DEST_DIR"

# 备份已有
if [ -d "$DEST_DIR" ]; then
  echo "检测到已有安装，备份到 $DEST_DIR.bak"
  [ -d "$DEST_DIR.bak" ] && rm -rf "$DEST_DIR.bak"
  mv "$DEST_DIR" "$DEST_DIR.bak"
fi

# 复制
mkdir -p "$HOME/.claude/skills"
cp -r "$SRC_DIR" "$DEST_DIR"
echo "✅ 已安装到 $DEST_DIR"

echo ""
echo "=== 验证 ==="
if [ -f "$DEST_DIR/SKILL.md" ]; then
  echo "✅ SKILL.md 存在"
else
  echo "❌ SKILL.md 缺失，安装失败"
  exit 1
fi
N_PAIRS=$(wc -l < "$DEST_DIR/distilled_data/pairs.jsonl" 2>/dev/null || echo 0)
echo "✅ 样本库: $N_PAIRS 对"

echo ""
echo "=== 使用 ==="
echo "重启 Claude Code 后，说「用 Gemini 风格翻译：<中文>」即可触发该 skill。"
echo "skill 目录: $DEST_DIR"