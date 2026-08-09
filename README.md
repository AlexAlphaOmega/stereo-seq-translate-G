# Gemini Style Translate Skill

用 **Gemini 翻译风格**把中文翻译成英文的 Claude Code skill。内置**自动化蒸馏**的样本库、术语表、句式模板——让任何模型翻译时都能像 Gemini 一样地道、专业。

## 特点

- **翻得像 Gemini**：从 1464+ 对 Gemini 真实译文中蒸馏出句式规律和术语对照，翻译时自动参照
- **STOmics/Stereo-seq 专业术语**：内置官方术语库，`芯片T载体 → Chip T Slide`、`透化 → permeabilization` 等术语强制正确
- **持续进化**：蒸馏数据会随使用不断增长（样本库、术语、句式每天更新）

## 快速安装

### 方式一：克隆 + 安装脚本（推荐）

```bash
git clone https://github.com/AlexAlphaOmega/stereo-seq-translate-G.git
cd stereo-seq-translate-G

# Windows
install.bat

# Mac / Linux
bash install.sh
```

### 方式二：手动复制

```bash
# 把 skill 目录复制到 Claude 的 skills 目录
cp -r stereo-seq-translate-G/gemini-style-translate ~/.claude/skills/
# (Windows: 复制到 %USERPROFILE%\.claude\skills\)
```

### 方式三：通过 Claude Code marketplace

1. `/plugin marketplace add AlexAlphaOmega/stereo-seq-translate-G`
2. `/plugin install gemini-style-translate`

## 使用

重启 Claude Code 后，对 Claude 说：

> **用 Gemini 风格翻译：**<中文文本>

或翻译 STOmics / Stereo-seq 技术文档时，会自动触发本 skill。

## 能翻什么

- 中文技术说明书 → 英文
- STOmics / Stereo-seq / 生物技术文档
- 任何需要地道英文翻译的中文内容

## 目录结构

```
stereo-seq-translate-G/
├── gemini-style-translate/       # skill 本体
│   ├── SKILL.md                  # skill 入口（触发规则 + 翻译流程）
│   └── distilled_data/           # 蒸馏数据
│       ├── pairs.jsonl           # Gemini 真实译文样本库
│       ├── terminology.md        # 自动蒸馏专业术语表
│       ├── sentence_patterns.md  # Gemini 句式规律
│       └── terminology/          # 官方术语库（种子）
├── install.sh                    # Mac/Linux 安装脚本
├── install.bat                   # Windows 安装脚本
└── .claude-plugin/               # marketplace 配置
```

## 数据来源

蒸馏数据来自 STOmics 官方中文说明书 + Gemini 网页版翻译，经自动化蒸馏流水线持续更新。