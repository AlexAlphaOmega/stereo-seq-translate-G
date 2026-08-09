---
name: stereo-seq-translate
description: Stereo-seq/STOmics 专业翻译语料库与翻译规则。基于 6 份官方英文标准文档提取的 ~800+ 条术语，用于 CN↔EN 翻译检验与执行。
trigger: When the user asks to translate a Stereo-seq or STOmics document, or to check translation accuracy against the corpus.
---

# Stereo-seq / STOmics 专业翻译 Skill

基于 6 份 STOmics 官方英文文档构建的双语翻译语料库。

## 核心术语规则

### 产品名
| 中文 | 英文 |
|---|---|
| Stereo-seq 转录组试剂套装 | **Stereo-seq Transcriptomics Set** (NOT Kit) |
| Stereo-seq 芯片 T 载体 | **Stereo-seq Chip T Slide** (NOT Carrier/Vector) |
| Stereo-seq 芯片 N 载体 | **Stereo-seq Chip N Slide** |
| Stereo-seq V3 载具上盖 | **Stereo-seq V3 Cassette Lid** |
| Stereo-seq V3 载具底座 | **Stereo-seq V3 Cassette Base** |
| Stereo-seq V3 载具垫圈 | **Stereo-seq V3 Gasket** |
| 时空组学配件套装 | **STOmics Accessory Kit** |
| 0.5 mL 管盖 | **0.5 mL Tube Cap** (NOT Cassette) |

### 禁用词
- permease → **PR Enzyme**
- feeding zone → **loading area**
- conformation → **confirmation**
- Device engine room → **Cleanup**
- chip patches → **tissue mounting**
- cut out sections → **section** / **obtain sections**
- deep plate → **deep well plate**
- BOM → **User-supplied Materials**
- mother liquor → **stock solution**
- Stomics → **STOmics**
- Single Step Operation → **Single Stepping**

### 界面词（加引号）
"Initialization", "Cooling", "Start", "OK", "Scanning", "Sorting", "Loading", "Pause instrument", "Single Stepping", "Close Door", "Open Door"

### 风格
- 温度：`4°C`（无空格）
- 单位：`3 μL`（有空格）
- 标题：`Chapter N: <Title>`, `N.N <Title>`
- 图表：`Figure N-N. <desc>`, `Table N-N <desc>`

完整语料库见同目录下的 corpus_*.md 文件。

### 语料库补充操作
- 如果用户说想补充语料库之类的话，并提供了相应的文件或者语句调整建议，也需要咬碎了它，每个词每个句子都嚼碎了，跟用户确认一下，然后完整地整理进语料库，
