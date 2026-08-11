# 蒸馏句式模板（从 710 对 Gemini 真实译文统计得出）

本文件由 `analyze_patterns.py` 对 710 对真实 `{中文, Gemini译文}` 样本统计生成。
所有句式频率、句首模式、例句都来自真实数据，非人工归纳。

## 数据统计总览

| 指标 | 数值 | 含义 |
|---|---|---|
| 句数相同 | 62% | Gemini 多数保留中文句数，不强行拆句 |
| 中文长句拆成多句 | 38% | 仅一部分长句被拆分 |
| 句首用 A/The | 70 次 | 高频用冠词开头的陈述句 |
| 句首祈使动词 | Use 14 / Add 12 / Place 8 / Remove 6 | 祈使句是真实存在的操作句式 |
| 句首连接词 | After 23 / If 20 / For 21 | 步骤衔接、条件、目的 |

## 真实高频句式（按出现次数排序）

以下句式在样本中真实高频出现，翻译时优先采用：

1. **`μL` 用量表达**（70 次）— 加量词
   - `Add <reagent>, <volume> μL/<unit>`
   - 例：`Add Wash Buffer, 200 μL/chip`

2. **`if ...` 条件句**（44 次）
   - `If <condition>, <result>`
   - 例：`If abnormal noise is detected, stop using it immediately.`

3. **`after ...` 步骤衔接**（41 次）
   - `After <step>, <next>`
   - 例：`After fixation, transfer the carrier to a fume hood.`

4. **`ensure ...` 确保**（28 次）
   - `Ensure that <condition>`
   - 例：`Ensure the RT Mix covers the entire chip.`

5. **`at room temperature` 室温**（27 次）
   - 例：`thaw at room temperature`

6. **`refer to ...` 参见**（24 次）
   - 例：`Refer to Table 3-1` / `Refer to Appendix A`

7. **`It is recommended to ...` 建议**（18 次）
   - 例：`It is recommended to take out all reagent components in advance.`

8. **`Do not ...` 禁止**（17 次）
   - `Do not <verb> <object> while <clause>`
   - 例：`Do not vortex the permeabilization enzyme; mix by pipetting.`

9. **`for <n> min` 时间**（17 次）
   - 例：`Incubate at 37°C for 5 min`

10. **`carefully/gently` 程度副词**（15/10 次）
    - 例：`carefully dry the chip surface` / `gently invert several times`

## 真实例句（从 710 对样本提取）

### 祈使句（操作指令）
```
ZH: RT Enzyme mix提前从−20℃取出，置于冰上使用期间置于冰上
EN: Remove the RT Enzyme mix from -20°C in advance, place it on ice, and keep it on ice during use.
```

### 禁止（Do not）
```
ZH: 请勿在设备运行时拆卸外壳，否则可能导致触电。
EN: Do not remove the casing while the equipment is running, as this may result in electric shock.
```
```
ZH: 不要涡旋透化酶，可通过移液器吹打混匀。
EN: Do not vortex the permeabilization enzyme; mix by pipetting.
```

### 条件（If）
```
ZH: 若组织脱落，也不建议进行正式实验。
EN: If the tissue detaches, proceeding with the formal experiment is not recommended.
```
```
ZH: 如果在FB染色后的清洗过程中有脱片现象，则不建议进行正式实验。
EN: If tissue detachment occurs during the washing process after FB staining, the formal experiment is not recommended.
```

### 建议（It is recommended）
```
ZH: 推荐使用前将各试剂组分提前取出，将酶类组分瞬时离心后置于冰上备用。
EN: It is recommended to take out all reagent components in advance, briefly centrifuge the enzyme components, and place them on ice for later use.
```
```
ZH: 为避免样本交叉污染，推荐使用带滤芯的吸头，吸取不同样本时请更换吸头。
EN: To avoid sample cross-contamination, it is recommended to use filter tips and replace them when aspirating different samples.
```

### 目的（To avoid / to ensure）
```
ZH: 为避免样本交叉污染，推荐使用带滤芯的吸头。
EN: To avoid sample cross-contamination, it is recommended to use filter tips.
```

## 翻译规则（数据驱动的）

1. **句数**：多数保留中文句数（62%），仅当中文长句确实过长时拆短（38%）。不要为了「拆句」而拆句。
2. **句首**：陈述句用冠词开头（A/The），操作句用祈使动词（Use/Add/Place/Remove/Prepare），步骤衔接用连接词（After/If/For）。
3. **用量**：数字 + `μL`/`/chip` 等量词符号，保留原文格式。
4. **禁止**：`Do not <verb>`，长句用分号连接（`;`）而不是硬拆。
5. **建议**：`It is recommended to ...`。
6. **目的**：`To avoid ...` / `To ensure ...` 引出。
7. **温度时间**：`at <temp>` + `for <time>`。
8. **程度**：操作加 `carefully`/`gently` 修饰动作。

## 检查清单

- [ ] 是否多数保留了中文句数（不强行拆句）？
- [ ] 句首是否用了自然的冠词/祈使动词/连接词？
- [ ] 用量/温度/时间是否保留了符号格式（μL/°C/min）？
- [ ] 禁止是否用 `Do not` + 专业动词？
- [ ] 是否存在生硬直译（put/get/take 这类）？
- [ ] 术语是否按 terminology.md 的标准译法？
## 自动蒸馏新增句式（2026-08-06）

### 操作指令
- 模板: `Perform <action> on <object>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 步骤衔接
- 模板: `<action1>, <action2>, and <action3>;`
- 例句: vortex to mix, and incubate at room temperature for 10 min;

### 条件指令
- 模板: `If <condition>, <action>.`
- 例句: If PCR product is 100 μL, add 80 μL of magnetic beads

### 参考指令
- 模板: `For <item>, refer to <reference>.`
- 例句: For resuspension volume, refer to Table 3-8.

### 警示指令
- 模板: `Be careful not to <action>.`
- 例句: Be careful not to disturb the magnetic beads

### 文档引用
- 模板: `For detailed procedures regarding <process>, please refer to <document>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the *Spatial Transcriptomics FF V1.3

### 停止点说明
- 模板: `Stopping point: This step can be stopped; <action>.`
- 例句: Stopping point: This step can be stopped; the cDNA PCR amplified product can be stored at −20°C for 1 month.

### 前置条件说明
- 模板: `Note: Please first follow <tutorial>. Proceed with the steps above only after <condition>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub. Proceed with the steps above only after installation.

### 核对确认
- 模板: `Ensure that <condition>.`
- 例句: Ensure that the hole cutouts on the fixture and gasket are aligned.

### 组件描述
- 模板: `The <system> includes <components>.`
- 例句: The Stereo-seq slide accessory kit includes slide holders, detachable gaskets, and sealing films.

## 自动蒸馏新增句式（2026-08-07）

### 操作指令 (Imperative Command)
- 模板: `Perform <action> on <object>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 试剂准备 (Reagent Preparation/Action)
- 模板: `Add <amount> <reagent> to <object>.`
- 例句: Add 200 μL 80% ethanol, rotate the centrifuge tube on the magnetic rack

### 参考引用 (Reference/Cross-link)
- 模板: `For <information>, refer to <reference_target>.`
- 例句: For resuspension volume, refer to Table 3-8.

### 条件确认 (Condition/Verification)
- 模板: `Ensure <component1> and <component2> are <status>.`
- 例句: Ensure that the hole cutouts on the fixture and gasket are aligned.

### 步骤重复 (Action Repetition)
- 模板: `Repeat steps <step_range> once.`
- 例句: Repeat steps e-f once;

### 静置/孵育操作 (Incubation/Waiting)
- 模板: `<Action> for <duration> until <condition>.`
- 例句: Incubate for 30 s, then carefully aspirate and discard the supernatant

### 停止点说明 (Stopping Point)
- 模板: `Stopping point: This step can be stopped; <object> can be stored at <temperature> for <duration>.`
- 例句: Stopping point: This step can be stopped; the cDNA PCR amplified product can be stored at −20°C for 1 month.

### 数值/比例描述 (Quantitative Description)
- 模板: `<Parameter>: <Description> (value is <value1> for <condition1>, <value2> for <condition2>)`
- 例句: ##--scale_factor: Downsampling ratio (value is 0.5 for 20X images, 0.25 for 40X images)

### 注意事项 (Note/Warning)
- 模板: `Note: Please first <action1>. Proceed with the steps above only <action2>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub. Proceed with the steps above only after successful installation.

## 自动蒸馏新增句式（2026-08-07）

### Laboratory Procedure Instruction
- 模板: `Perform <action> on <target_substance>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### Sequential Step with Time Constraint
- 模板: `After <action_condition>, <imperative_verb> <target_object> on <equipment> and let it stand for <duration> until <result>;`
- 例句: After a brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min until the solution clarifies;

### State Maintenance and Reagent Addition
- 模板: `Keep <target_object> on <equipment>, add <volume> <reagent>, ...;`
- 例句: Keep the centrifuge tube on the magnetic rack, add 200 μL 80% ethanol, rotate the centrifuge tube on the magnetic rack

### Stopping Point Definition
- 模板: `Stopping point: This step can be stopped; <target_product> can be stored at <temperature> for <duration>.`
- 例句: Stopping point: This step can be stopped; the cDNA PCR amplified product can be stored at −20°C for 1 month.

### Document Reference
- 模板: `For <purpose_description>, please refer to <document_title>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the Spatial Transcriptomics FF V1.3( 含兼容mlF) 建库实验操作说明书.

### Validation Instruction
- 模板: `Ensure that <element_a> and <element_b> are <state>.`
- 例句: Ensure that the hole cutouts on the fixture and gasket are aligned.

### Simple Removal/Retrieval
- 模板: `Remove <item> from <source_location>`
- 例句: Remove the clip from the Stereo-seq Chip Kit

## 自动蒸馏新增句式（2026-08-07）

### 步骤执行指令
- 模板: `Perform <action> on <object>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 条件动作衔接
- 模板: `After <action>, <instruction>:`
- 例句: After a brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min until the solution clarifies;

### 保持状态与后续操作
- 模板: `Keep the <object> on <location>, <action>:`
- 例句: Keep the centrifuge tube on the magnetic rack, add 200 μL 80% ethanol, rotate the centrifuge tube on the magnetic rack

### 引用参考资料
- 模板: `For <subject>, refer to <reference>.`
- 例句: For resuspension volume, refer to Table 3-8.

### 详细流程引用
- 模板: `For detailed procedures regarding <subject>, please refer to <reference>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the Spatial Transcriptomics FF V1.3( 含兼容mlF) 建库实验操作说明书.

### 操作注意事项
- 模板: `Be careful not to <action>,`
- 例句: Be careful not to disturb the magnetic beads,

### 操作提示标注
- 模板: `Note: <instruction>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub.

### 中断点说明
- 模板: `Stopping point: <instruction>.`
- 例句: Stopping point: This step can be stopped; the cDNA PCR amplified product can be stored at −20°C for 1 month.

### 举例说明
- 模板: `e.g., if <condition>, <action>,`
- 例句: e.g., if PCR product is 100 μL, add 80 μL of magnetic beads

### 检测与记录操作
- 模板: `Take <quantity> of <object>, <instruction>:`
- 例句: Take 1 μL of cDNA sample, measure the concentration using the Qubit dsDNA HS Kit, and record it;

## 自动蒸馏新增句式（2026-08-08）

### 祈使句操作指令
- 模板: `<verb> <object> (<prep> <details>);`
- 例句: Vortex to mix, and incubate for 30 s;

### 步骤参考/引导
- 模板: `According to <section_id>, <action>:`
- 例句: According to 3.1 Pre-experiment preparation → Prepare reagents required for the next day in advance:

### 条件句/注意事项
- 模板: `Note: <condition/action>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub.

### 包含关系/描述
- 模板: `The <subject> includes <object1>, <object2>, and <object3>.`
- 例句: The Stereo-seq slide accessory kit includes slide holders, detachable gaskets, and sealing films.

### 参数/数值说明
- 模板: `<Parameter>: <Description> (value is <value1> for <condition1>, <value2> for <condition2>)`
- 例句: --scale_factor: Downsampling ratio (value is 0.5 for 20X images, 0.25 for 40X images)

### 停止点设置
- 模板: `Stopping point: <condition>; <object> can be stored at <temperature> for <duration>.`
- 例句: Stopping point: This step can be stopped; the cDNA PCR amplified product can be stored at −20°C for 1 month.

### 时间/温度参数
- 模板: `<temperature>, <time> <unit>`
- 例句: 72°C, 3 min

### 操作预防性警示
- 模板: `Be careful <negative_action>, and <positive_action>.`
- 例句: Be careful not to disturb the magnetic beads, and label the chip ID, date, cDNA concentration, etc.);

### 参考文档引用
- 模板: `For <purpose>, please refer to the *<Document_Title>*.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the *Spatial Transcriptomics FF V1.3( 含兼容mlF) 建库实验操作说明书*.

### 设备/方法举例
- 模板: `Examine the <target> using equipment based on <principle>, such as <examples>.`
- 例句: Examine the cDNA fragment distribution using equipment based on electrophoresis separation principles, such as Bioanalyzer...

## 自动蒸馏新增句式（2026-08-09）

### 操作指令
- 模板: `Perform <action> on <object>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 动作序列
- 模板: `After <action>, place <object> on <device> and <action> for <duration> until <condition>;`
- 例句: After a brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min until the solution clarifies;

### 试剂混合
- 模板: `Mix <object_A> with <object_B> (equilibrated to <condition>), <action>, and <action>;`
- 例句: Mix the PCR amplification product with magnetic beads (equilibrated to room temperature), vortex to mix, and incubate for 10 min;

### 液体处理
- 模板: `After <condition>, carefully <action> the supernatant using a pipette;`
- 例句: After the liquid clarifies, carefully remove the supernatant using a pipette;

### 文档引用
- 模板: `For <subject>, please refer to <document_name>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the *Spatial Transcriptomics FF V1.3( 含兼容mlF) 建库实验操作说明书*.

### 条件准备
- 模板: `Take out <item> and <action> at room temperature.`
- 例句: Take out magnetic beads, equilibrate at room temperature, and prepare 80% ethanol;

### 注意事项
- 模板: `Note: Please first <action>. Proceed with <action> only after <condition>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub. Proceed with the steps above only after...

### 图表引用
- 模板: `For <subject>, refer to <table_figure_name>.`
- 例句: For resuspension volume, refer to Table 3-8.

## 自动蒸馏新增句式（2026-08-09）

### 操作指令（建议/要求）
- 模板: `<subject> is recommended to be <verb_past_participle> to <infinitive_phrase>.`
- 例句: The heated lid temperature is recommended to be set to 35°C, or to the lowest possible temperature close to 35°C.

### 操作指令（绝对禁止）
- 模板: `Do not <verb_base_form_1>, <verb_base_form_2>, or <verb_base_form_3>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 步骤执行条件
- 模板: `Once <subject> <verb_present_simple>, immediately <verb_imperative> <object>.`
- 例句: Once the PCR instrument temperature reaches 4 °C, immediately add 20 μL of DNB stop buffer.

### 物料配制要求
- 模板: `The <noun_phrase> must be <verb_past_participle> immediately before use.`
- 例句: The DNB loading mix must be prepared immediately before use.

### 引用说明
- 模板: `For <adjective_or_noun> <noun_phrase>, please refer to <location_reference>.`
- 例句: For detailed DNB loading operations, please refer to the MGIDL-200H Portable Pipettor Quick Operation Guide.

### 实验条件引用
- 模板: `<noun_phrase> according to the table below:`
- 例句: Take out a 0.5 mL cryotube and prepare the DNB loading system 1 according to the table below:

### 结果检查
- 模板: `Take <quantity> of <substance> and use <instrument_or_kit> to <verb_base_form> <target_metric>.`
- 例句: Take 2 μL of DNB and use the Qubit ssDNA Assay Kit and Qubit 4.0 Fluorometer to detect the concentration.

### 操作顺序说明
- 模板: `Take out <item>, place it on <container> for <duration>, then <verb_base_form_1> and <verb_base_form_2>.`
- 例句: Take out the DNB Loading Buffer II, place it on an ice box for approximately 30 minutes until thawed, then use a vortex mixer to oscillate.

### 状态保持指令
- 模板: `Keep <object> at <temperature_condition> for <purpose>.`
- 例句: Gently mix the DNB loading mix 5–8 times using a wide-bore pipette tip, and keep at 4 °C for later use.

### 条件判定（如果/若）
- 模板: `If <condition>, <action_required_or_suggested>.`
- 例句: If the DNB concentration is unqualified, re-preparation is required.

## 自动蒸馏新增句式（2026-08-10）

### 动作指令
- 模板: `<verb> <object> <optional: complement/instruction>`
- 例句: Click the 【Sequencing】 option on the main interface to enter the following interface.

### 条件判断操作
- 模板: `If <condition>, <imperative action>; otherwise, <alternative imperative action>.`
- 例句: If loading DNB onto the sequencer, check [DNB Loading]; otherwise, do not check.

### 操作前置条件
- 模板: `The <subject> must be <verb-ed> <duration/frequency> to <goal/mix> before <action>.`
- 例句: The dNTPs mixture II must be vortexed for 5 seconds to mix before loading, and then briefly centrifuged before use.

### 禁止操作
- 模板: `Do not <action> <object> <optional: reason>.`
- 例句: Do not reuse the removed sealing film.

### 后续操作引导
- 模板: `For the next step, you can proceed directly to "<target section/page>" on page <number>.`
- 例句: For the next step, you can proceed directly to "Start Sequencing" on page 20.

### 操作目的说明
- 模板: `<imperative action>, <ensuring/to reduce/to ensure> <result>.`
- 例句: Gently tap the sequencing reagent trough to reduce air bubbles in the reagent.

### UI交互操作
- 模板: `Move the cursor to the <field name> and enter <input value>.`
- 例句: Move the cursor to the entry field next to [DNB ID] and enter the library name or ID.

### 安全操作提示
- 模板: `When <action>, <exercise caution/operate carefully> to <prevent/avoid> <negative result>.`
- 例句: When transferring the mixture, exercise caution to prevent it from spilling out of the reagent tube.

## 自动蒸馏新增句式（2026-08-11）

### 操作步骤指令
- 模板: `[Number]. [Action Verb] <object> [preposition] <location> according to <value>.`
- 例句: 8. Take a pipette of the corresponding range, add the dNTPs mix II into a new 5 mL sterile tube according to the volumes

### 强制操作要求
- 模板: `The <subject> must be <verb-ed> [adverb/duration] before <action>.`
- 例句: The dNTPs mixture II must be vortexed for 5 seconds to mix before loading

### 操作注意事项
- 模板: `When <gerund-phrase>, exercise caution to prevent <object> from <action-gerund>.`
- 例句: When transferring the mixture, exercise caution to prevent it from spilling out of the reagent tube.

### 界面交互指令
- 模板: `Click the [<button_name>] [option/icon] on the <interface_name> to <action>.`
- 例句: Click the 【Sequencing】 option on the main interface to enter the following interface

### 菜单选择指令
- 模板: `Select the <item_name> from the [<menu_name>] drop-down menu.`
- 例句: Select the spatial transcriptomics sequencing scheme from the [Sequencing Scheme] drop-down menu.

### 条件配置指令
- 模板: `If <condition> is required, select <option_a>; if <condition> is not performed, select <option_b>.`
- 例句: If barcode sequencing is required, select the STO_T_50+100+10 sequencing protocol; if barcode sequencing is not performed, select the STO_T_50+100_noBC sequencing protocol.

## 自动蒸馏新增句式（2026-08-12）

### 步骤衔接
- 模板: `After <action-done>, <next-action>.`
- 例句: After fixation is complete, remove the sealing film.

### 添加试剂/操作建议
- 模板: `Add <amount> of <reagent>, and incubate at <condition> for <time>.`
- 例句: Immediately add 400 μL/chip of Wash Buffer, and incubate at room temperature for 1 min.

### 参考引用
- 模板: `Refer to <section/document> to <action>.`
- 例句: Refer to Chapter 2 of the "Stereo-seq Chip Carrier and Accessories User Manual" to assemble the gasket and fixture.

### 禁止事项
- 模板: `Avoid <action/condition>.`
- 例句: Avoid contact between the carrier and the front side of the chip.

### 液体吸弃与保持润湿
- 模板: `Aspirate and discard <liquid> from <location> using a pipette, ensuring <condition>.`
- 例句: Aspirate and discard the blocking buffer from one corner of the chip using a pipette, ensuring the tissue on the chip remains moist.

### 重复步骤
- 模板: `Repeat steps <step-range> once, for a total of <number> washes.`
- 例句: Repeat steps e.-f. once, for a total of 2 washes.

### 配制溶液后的处理
- 模板: `<action> after <preparation-step>, and <post-action>.`
- 例句: Prepare the primary antibody incubation solution, vortex to mix, centrifuge briefly, and keep on ice for use.

### 条件警告
- 模板: `Strictly avoid <condition>, as <consequence>.`
- 例句: Strictly avoid tissue drying during the liquid exchange process, as tissue drying can easily generate non-specific signals.
