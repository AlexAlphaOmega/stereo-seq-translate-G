---
name: gemini-style-translate
description: 用 Gemini 翻译风格把中文翻译成英文。当用户要求「像 Gemini 一样翻译」「用 Gemini 风格翻译」「按语料库翻译 STOmics/Stereo-seq 文档」时触发。内置 710 对 Gemini 真实译文样本 + 专业术语库，翻译时自动参照，产出地道、专业、符合目标语言母语者习惯的英文。
trigger: When the user asks to translate Chinese to English and wants it to sound like Gemini — or translate any STOmics/Stereo-seq/生物技术 technical document.
---

# Gemini 风格翻译 Skill

把中文翻译成英文，翻译效果对齐 Gemini：地道、自然、专业、符合英文母语者习惯，而不是逐字直译。

## 数据来源

本 skill 内置三块蒸馏数据（位于本目录 `distilled_data/`），全部来自 710 对 Gemini 真实译文（STOmics 官方中文说明书 + Gemini 网页版翻译）：

1. **`pairs.jsonl`** — 710 对 Gemini 真实译文样本（`{zh, en}`）。翻译时从中挑最相关的范例注入，让模型参照 Gemini 的实际译法。
2. **`terminology.md`** — 高频术语表（芯片/载体/载具、实验操作、试剂溶液、通用技术词、动词风格、数字格式），保证术语准确。
3. **`sentence_patterns.md`** — 句式模板（由 `analyze_patterns.py` 对 710 对样本统计生成，含真实例句）。这是「翻得像 Gemini」的核心——按 Gemini 的实际句式组织英文，不是逐字直译。

翻译时必须：先查 `terminology.md` 定术语，再按 `sentence_patterns.md` 的句式组织英文，必要时从 `pairs.jsonl` 挑同句式范例参照。

## Gemini 翻译风格特征（从 710 对样本蒸馏得出）

翻译时严格遵循以下风格，这是 Gemini 与普通模型译文的差别：

1. **意译优先，不逐字直译** — 平均英/中长度比约 2.9，Gemini 会展开补充英文必需的成分（冠词、主语、连接），让译文读起来像英文母语者写的，而不是「中文句子的英文单词替换」。
2. **拆分长句** — 约 55% 的样本把中文长句拆成一个或多个英文短句，用句号/分号分隔，避免一句到底。中文的逗号长句 → 英文拆成多句。
3. **补全冠词** — 中文没有冠词，Gemini 会正确补上 `the`/`a`/`an`（约 46% 的句子含 `the`）。
4. **术语先查语料库** — 翻译 STOmics/Stereo-seq 专业术语时，先查 `terminology/` 里的标准译法，用官方译法而不是直译。例如：
   - `Stereo-seq 芯片 T 载体` → `Stereo-seq Chip T Slide`（NOT carrier/vector）
   - `透化` → `permeabilization`（生物专业术语）
   - `载玻片/载具` 按语境选 `slide`/`cassette`/`carrier`
5. **格式保留** — 保留章节编号、表格、`Cat. No.`、型号、单位、温度（`−25℃`）等原样。
6. **语气专业客观** — 说明书/技术文档用客观第三人称，避免口语化。操作步骤用祈使句（`Place...`、`Add...`、`Do not...`）。

## 翻译流程（必须按此执行）

### 第 1 步：识别术语
扫描待翻译文本，找出 STOmics/Stereo-seq/生物专业术语。查 `distilled_data/terminology/` 里的语料库，确定标准译法。

### 第 2 步：挑范例
从 `distilled_data/pairs.jsonl` 里挑 3-5 条与待翻译内容**最相关**的 `{zh, en}` 范例（同领域、同句式、含相同术语），作为 few-shot 注入。

### 第 3 步：翻译
按「Gemini 风格特征」翻译，遵循术语库译法，风格上参照挑出的范例。

## 输出格式

- 只输出译文，不输出解释、备注、`<<pN>>` 标记。
- 保留原文的段落结构、标题层级、编号。
- 若原文是表格/列表，输出对应的表格/列表（英文）。

## 示例

输入：
> Stereo-seq 芯片 T 载体（1 cm*1 cm）芯片盒中包含 4 片载体，4 张芯片载体上均贴有 1 张 Stereo-seq 芯片 T。

正确输出（Gemini 风格）：
> The Stereo-seq Chip T Slide (1 cm×1 cm) cassette contains 4 slides, and each slide is affixed with one Stereo-seq Chip T.

（对照：直译会写成 "Stereo-seq chip T carrier box contains 4 carriers, 4 chip carriers are each pasted with 1 Stereo-seq chip T" —— 这是错的。要用 slide、cassette，补冠词，拆分长句。）

## 使用方式

- 用户在 Claude Code 里说「用 Gemini 风格翻译：<中文>」或「像 Gemini 那样翻这段」→ 触发本 skill。
- 其他 agent / 模型通过 skill 调用协议调用本 skill，获得同样的翻译能力。