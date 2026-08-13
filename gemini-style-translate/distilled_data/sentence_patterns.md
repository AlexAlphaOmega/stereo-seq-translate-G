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

## 自动蒸馏新增句式（2026-08-12）

### 条件执行
- 模板: `When it is necessary to <action>, follow <instructions>`
- 例句: When it is necessary to replace the V3 gasket during the process, follow the operations in step '1' of 'IV. Disassembly'

### 动作指令
- 模板: `<verb> the <object> with <tool/reagent>`
- 例句: Wipe the upper cover with 75% ethanol to remove residual reagents from the surface

### 操作后确认
- 模板: `After <action>, ensure <condition>`
- 例句: After replacement, ensure that the gasket is not deformed and fits tightly.

### 时长指令
- 模板: `<verb> in <substance> for <time>`
- 例句: First, immerse in 75% ethanol for 10 min

### 用途与限制
- 模板: `This product is for <intended_use>, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic purposes.

### 提示注意事项
- 模板: `Note: <instruction/guidance>`
- 例句: Note: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 重复使用流程
- 模板: `For reuse, the <item> must be subjected to the following <procedure>:`
- 例句: For reuse, the cover and base must be subjected to the following cleaning procedures:

### 修订说明
- 模板: `· <Action> the <item>`
- 例句: · Added reference URL for sample processing videos;

## 自动蒸馏新增句式（2026-08-13）

### 操作指令
- 模板: `<imperative_verb> <object> <optional_complement>`
- 例句: Remove the clamp and gasket from the Stereo-seq Chip Accessory Kit;

### 建议表达
- 模板: `It is [strongly] recommended to <verb> <object>.`
- 例句: It is recommended to take out the reagent components in advance.

### 条件指令
- 模板: `If <condition>, <imperative_verb> <object>.`
- 例句: If the tissue block is completely solidified and has turned white and opaque, gently flex both sides of metal embedding mold A.

### 验证动作
- 模板: `<action> to ensure <target> is <state>.`
- 例句: Finally, inspect the assembled fixture and chip carrier to ensure they are correctly positioned.

### 禁止与警告
- 模板: `Avoid <noun_phrase>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 要求描述
- 模板: `<subject> should not exceed <measurement>.`
- 例句: The tissue size should not exceed 0.9 cm × 0.9 cm × 2 cm.

### 前置准备
- 模板: `Prepare <object> in advance [to <purpose>].`
- 例句: Prepare a foam box of crushed ice in advance and place the OCT on the ice to pre-chill for 10 min;

## 自动蒸馏新增句式（2026-08-13）

### 操作指令式
- 模板: `Please <verb> the <object>.`
- 例句: Please read this manual carefully before installation.

### 否定/禁止式
- 模板: `Do not <verb> the <object>, as <reason>.`
- 例句: Do not remove the casing while the equipment is running, as this may result in electric shock.

### 条件触发式
- 模板: `If <condition> is detected, please <action>.`
- 例句: If abnormal noise is detected, please stop using it immediately and contact the after-sales service center.

### 步骤/行为衔接式
- 模板: `After <event>, please <action>.`
- 例句: After each use, please clean the lens surface with a soft cloth.

### 产品属性声明
- 模板: `This product <verb> <function/feature>.`
- 例句: This product supports timed on/off, temperature curve setting, and energy consumption statistics functions.

### 文档免责声明
- 模板: `This document serves as <purpose>, aiming to provide <content>.`
- 例句: This document serves as general guidance and reference material, aiming to provide operational instructions and methodology.

### 修订说明式
- 模板: `<Action> the <item>.`
- 例句: Update chip storage temperature;

### 版权所有声明
- 模板: `<Year> <Company> All rights reserved.`
- 例句: 2026 Shenzhen BGI Three Arrows Technology Co., Ltd. All rights reserved.

### 用法限定
- 模板: `This product is for <usage> only, not for <negative_usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 步骤标题
- 模板: `<number>.<number>. <Noun> <Noun>`
- 例句: 3.2. Section Preparation

### 功能性提示
- 模板: `<Type>: <Description>.`
- 例句: Tip: Additional operating tips and guidance.

### 试剂/组分表格定义
- 模板: `Table <number>-<number> <Product Name>`
- 例句: Table 1-1 Reagent Components of Stereo-seq Transcriptomics Kit T

### 产品/试剂信息行
- 模板: `<Product Name> Cat. No.: <Catalog Number>`
- 例句: Stereo-seq Transcriptomics Kit T Cat. No.: 201KT13114

### 储存要求
- 模板: `Storage temperature: <temperature_range>`
- 例句: Storage temperature: −25℃~ −15℃

### 操作指导建议
- 模板: `Please <verb> <object> <adverb>.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 替代操作指令
- 模板: `Replace <reagent_a> with <reagent_b> (see <reference>).`
- 例句: In the plant transcriptome experiment, replace the two green-capped reagents with the black-capped reagents from the Stereo-seq plant transcriptome accessory kit (see step 3.9).

### 外部引用/详情指引
- 模板: `For details, please refer to <Document Title>.`
- 例句: For details, please refer to the "Spatio-temporal Transcriptomics FF V1.3 (Plant-adapted) Experimental Protocol".

### 参数规格说明
- 模板: `<Parameter>: <Value>`
- 例句: Storage temperature: 18°C~25°C

### 等效性表述
- 模板: `(or equivalent <noun>)`
- 例句: (or equivalent instrument)

### 操作指令
- 模板: `Please <verb> <object> carefully before use`
- 例句: Please read this manual carefully before use.

### 选择建议
- 模板: `You may choose any one of the listed <items>`
- 例句: You may choose any one of the listed brands

### 用途限制
- 模板: `This product is for <purpose> only`
- 例句: This product is for research use only

### 自备物料清单
- 模板: `User-supplied <Item> List`
- 例句: User-supplied Instruments List

### 组分构成描述
- 模板: `The <container> contains <number> <item>`
- 例句: The Stereo-seq Chip T Slide cassette contains 4 slides

### 图表标题
- 模板: `Table <Number> <Name>`
- 例句: Table 1-4 Stereo-seq Plant Transcriptome Accessory Kit

### 推荐句式
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 动作指令
- 模板: `<Verb> <object>.`
- 例句: Add sufficient methanol to a slide box to ensure that the methanol sufficiently covers the tissue on it.

### 引用句式
- 模板: `Please refer to <source> for <task>.`
- 例句: Please refer to the *Stereo-seq Plant Fresh Sample Embedding Guide* for sample preparation.

### 条件判断与建议
- 模板: `If <condition>, <action> is not recommended.`
- 例句: If the tissue detaches, proceeding with the formal experiment is not recommended.

### 合规要求
- 模板: `<Object> shall be <verb_past_participle> in accordance with <regulations>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### 现配提醒
- 模板: `<Reagent> [Prepare immediately before use].`
- 例句: 1X Permeabilization Reagent Working Solution [Prepare immediately before use].

### 预设指令
- 模板: `Set <parameter> of <instrument> to <value> in advance.`
- 例句: Set the temperature of a metal bath or other equivalent instrument to 37°C in advance.

### 用途说明
- 模板: `<Substance/Method> is used solely for <purpose>.`
- 例句: The FB staining solution is used solely for tissue staining in the FB staining protocol.

### 检查指令
- 模板: `Ensure <condition>.`
- 例句: Ensure no liquid residue remains.

### 条件语句
- 模板: `If <condition>, <action>`
- 例句: If the chip surface is free of impurities, visible marks, liquid residue, or wavy patterns, you may proceed to preparation.

### 建议与备注
- 模板: `It is recommended to <action> to <purpose/avoid_risk>.`
- 例句: It is recommended to aliquot the prepared 10X permeabilization stock solution to avoid repeated freeze-thaw cycles.

### 禁止操作
- 模板: `Do not <action>; <alternative_action>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 试剂配制
- 模板: `To prepare <reagent>, dilute/mix <amount> of <component1> with <component2> to <final_amount>.`
- 例句: To prepare 5X SSC, dilute 100 μL of 20X SSC to 400 μL with Nuclease-Free Water, mix well, and keep at room temperature.

### 暂存条件
- 模板: `Store at <temperature>, <condition>.`
- 例句: Store at room temperature, protected from light.

### 预处理/准备动作
- 模板: `<action> from <temperature> in advance, <process>, and <placement>.`
- 例句: Take the RT Buffer Mix out from −20°C in advance, thaw at room temperature, and shake until no precipitate is observed.

### 时间/温度设定
- 模板: `<action> at <temperature> for <duration>.`
- 例句: Stain at room temperature, protected from light, for 5 min;

### 步骤衔接
- 模板: `<sequence_marker> <action>.`
- 例句: Repeat step 4);

### 用量说明
- 模板: `<action> <amount> <unit>/<target_unit>.`
- 例句: The volume for a 1 cm*1 cm chip is 100 μL/chip, and the volume for a 0.5 cm*0.5 cm chip is 30 μL/chip

### 步骤执行指令
- 模板: `<verb> <object> (e.g., place the carrier on the adapter, incubate for 5 min).`
- 例句: Place the chip with the front side facing up, quickly place the carrier onto the PCR adapter, and incubate at 37°C for 5 min.

### 条件性操作建议
- 模板: `If <condition>, <verb> <action>.`
- 例句: If autofluorescence is chosen, please follow the experimental procedures in section 3.5.1, and ignore section 3.5.2.

### 强调注意事项
- 模板: `Note: <instruction/warning>.`
- 例句: Note: When performing cold mounting on multiple chips, control the mounting time for each section; excessive intervals will cause tissue section shrinkage.

### 参考文档指引
- 模板: `Refer to <section/table> to <verb> <action>.`
- 例句: Refer to Section 3.7 Tissue Permeabilization, Table 3-2, to prepare 1X permeabilization reagent working solution in advance.

### 用量与参数规格说明
- 模板: `(For <object>, the volume/dosage is <quantity>).`
- 例句: (For 1 cm*1 cm chips, the volume is 150 μL/chip; for 0.5 cm*0.5 cm chips, the volume is 50 μL/chip).

### 禁止性操作
- 模板: `<action> must not be <adjective>/<too long/short>, to avoid <negative result>.`
- 例句: The pre-cooling time must not be too long to avoid water condensation on the slide surface.

### 顺序/重复步骤说明
- 模板: `Repeat steps <number> - <number> until <condition>.`
- 例句: Repeat steps 2) - 3) until all tissue sections have adhered to the chip surface.

### 结果描述
- 模板: `After <action>, the <object> becomes <adjective/visible state>.`
- 例句: After the methanol has completely evaporated, the tissue becomes visibly white.

### 操作指令-基础动作
- 模板: `<verb> <object> (e.g., <action>);`
- 例句: Turn on the episcopic light source, adjust the light intensity;

### 操作指令-条件性动作
- 模板: `Once <condition>, <verb> <object>;`
- 例句: Once the required number of points has been selected, click “End Point Selection”;

### 操作指令-用量/浓度表达
- 模板: `<verb> <amount> <unit>/<target_object> of <reagent_name>;`
- 例句: Add 150 μL/chip of 1X Permeabilization Reagent working solution onto the adapter.

### 禁止/警示句
- 模板: `Do not <action> (e.g., during/while <process>);`
- 例句: During the point selection process, do not rotate the mechanical adjustment handwheel.

### 建议/推荐句
- 模板: `It is recommended to <action> to <purpose>;`
- 例句: It is recommended to set the initial image save path on the local computer to improve upload speed.

### 参考引用句
- 模板: `For <information_type>, please refer to <document_name>.`
- 例句: For more specific microscope usage instructions, please refer to the "Go Optical Spatial Microscope Product Manual".

### 步骤衔接/顺序
- 模板: `After <process> is complete, <verb> <object>;`
- 例句: After the scan is complete, click "Create Slice" again to create a new folder;

### 状态确认/确保
- 模板: `Ensure <state> (e.g., <condition>);`
- 例句: Ensure the 8 buckles of the clamp are fastened tightly and both sides of the carrier are flush against the clamp.

### 选项选择
- 模板: `<verb> <reagent_A> or <reagent_B> (select based on <criterion>);`
- 例句: Take out RT Buffer Mix or F RT Buffer Mix in advance (select the specific reagent according to Section 3.8);

### 基本操作指令
- 模板: `Add <reagent> to wash once, <volume>/<unit>;`
- 例句: Add 0.1X SSC wash buffer to wash once, 200 μL/chip;

### 条件性建议
- 模板: `If <condition>, ensure <action>.`
- 例句: If reacting overnight, ensure the plate sealing film is well sealed.

### 提前准备指令
- 模板: `Prepare <item> <time> in advance according to <reference>.`
- 例句: Prepare the cDNA Release Mix 5 minutes in advance according to Table 3-4.

### 预防性操作
- 模板: `Use <tool> to <action>, press <part> firmly to prevent <risk>.`
- 例句: Use sealing film to seal the handheld carrier, press the edges of the reaction wells firmly to prevent evaporation of the reaction solution.

### 产品建议
- 模板: `It is recommended to use <product_a> or <product_b> for <procedure>.`
- 例句: It is recommended to use VAHTS DNA Clean Beads or AMPure® XP for magnetic bead purification.

### 操作前准备/混匀
- 模板: `Before each use, <action_1> or <action_2> to ensure <condition>.`
- 例句: Before each use, vortex or pipette the magnetic beads up and down to ensure they are thoroughly mixed.

### 混合与孵育指令
- 模板: `Mix the <sample> with <reagent> at a volume ratio of <ratio>, vortex to mix, and incubate at <temperature> for <time>.`
- 例句: Mix the recovered solution from the previous step with magnetic beads at a volume ratio of 1:1, vortex to mix, and incubate at room temperature for 10 min;

### 表格标题规范
- 模板: `Table <number> <title>`
- 例句: Table 3-4 cDNA Release Mix Preparation

### 条件判断
- 模板: `If <condition>, it is considered <state>.`
- 例句: if it is less than 20 ng/μL, it is considered an experiment exception.

### 停止点提示
- 模板: `Stop point: <action> can be <verb_past> at this step, or <object> can be stored at <temp> for <time>.`
- 例句: Stop point: PCR can be performed overnight at this step, or the products can be stored at 4°C for up to 16 hours.

### 外部引用
- 模板: `For <purpose>, please refer to <document/table>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the Spatial Transcriptomics FF V1.3.

### 测量与记录
- 模板: `Take <quantity> of <sample>, measure the <parameter> using <method> and record it.`
- 例句: Take 1 μL of cDNA sample, measure the concentration using the Qubit dsDNA HS Kit, and record it.

### 禁止/预防操作
- 模板: `Be careful not to <action>, and <instruction>.`
- 例句: Be careful not to disturb the magnetic beads, and label the chip ID, date, etc.

### Chapter Header
- 模板: `Chapter <Number> <Title>`
- 例句: Chapter 1 Introduction

### Operational Step (Gerund)
- 模板: `<Verb-ing> the <Object>`
- 例句: Thawing the Sample Loading Reagent Plate

### Preparation Instruction
- 模板: `Prepare <Object>`
- 例句: Prepare 0.1 M NaOH reagent

### Compatibility Statement
- 模板: `Compatible with <Object/Process>`
- 例句: Compatible with FF V1.3 library sequencing

### Calculation/Process Description
- 模板: `Calculation of <Process> for <Target>`
- 例句: Calculation of pooling volume for each sample

### Trademark Statement
- 模板: `<Brand> is a trademark of <Company> or its subsidiaries.`
- 例句: TM is a trademark of Thermo Fisher Scientific Inc. or its subsidiaries.

### Release/Revision Summary
- 模板: `<Version> <Action> in <Date>`
- 例句: Product name updated in June 2024

### Specification Requirements
- 模板: `<Subject> <Property> Requirements`
- 例句: Library Insert Size Requirements

### 异常状态描述
- 模板: `<Adjective> <Noun> <Noun>`
- 例句: Low DNB concentration

### 故障/过程描述
- 模板: `<Noun/Process> failure during <Event>`
- 例句: Liquid pumping failure during DNB loading or sequencing

### 强制操作/合规性规定
- 模板: `<Subject> must be <verb(passive)> in accordance with <regulation>`
- 例句: All samples and various types of waste must be treated as hazardous materials in accordance with relevant regulations.

### 严禁/禁止操作
- 模板: `Do not <verb> <object> beyond <limitation>`
- 例句: Do not use products beyond their expiration date.

### 存放/存储操作建议
- 模板: `Please <verb> <object> in <location> until <condition>`
- 例句: Please keep components in the packaging box until they are used up.

### 混合禁令
- 模板: `<Subject> from <source> must not be <verb(passive)>`
- 例句: Reagent components from different batches must not be mixed.

### 表格命名
- 模板: `Table <number> <NounPhrase>`
- 例句: Table 1 Example of Sequencing Cycle Numbers

### 试剂规格表述
- 模板: `<Item>, <quantity>/<unit> × <count>`
- 例句: TE buffer, 480 μL/tube × 1 tube

### 物品包装表达
- 模板: `<ItemName>, <Quantity>/<Unit> × <Count> <Unit>`
- 例句: MDA Polymerase Mix II, 0.60 mL/vial × 1 vial

### 设备耗材清单表达
- 模板: `<ItemName>/<Quantity> <Unit>`
- 例句: Sequencing Reagent Reservoir/1 unit

### 技术文档命名
- 模板: `<ProductSeries> <Category> Manual`
- 例句: Stereo-seq Transcriptomics Set (Cassette version, H&E compatible) User Manual

### 禁令表达
- 模板: `The use of <item> is prohibited; <requirement> must be used.`
- 例句: The use of filter tips is prohibited during DNB preparation and loading; recommended brand catalog numbers must be used.

### 建议表达
- 模板: `For <context>, it is recommended to use <recommendation>.`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### 图表命名
- 模板: `Table <Number> <Title>`
- 例句: Table 4 User-supplied equipment and materials

### 信息字段标注
- 模板: `<Field>: <Value>`
- 例句: Tel: 4000-688-114

### 依赖条件表达
- 模板: `<Process> depends on <factor>.`
- 例句: Sequencing duration depends on the read length and the number of slide platforms used.

### 条件准则表达
- 模板: `If the <source> has special requirements, the <criteria> specified in the <source> shall prevail.`
- 例句: If the library construction kit manual has special requirements, the fragment size requirements specified in the manual shall prevail.

### 换算公式表达
- 模板: `The conversion formula between <unit1> and <unit2> is as follows:`
- 例句: The conversion formula between fmol and ng is as follows:

### 条件指令
- 模板: `If <condition>, the <requirement_type> in the <document_name> shall prevail.`
- 例句: If the library preparation kit manual has special requirements, the library requirements in the library preparation kit manual shall prevail.

### 建议/推荐操作
- 模板: `It is recommended to <action> <time_condition>.`
- 例句: It is recommended to sequence no more than 8 samples per slide.

### 验证/检查操作
- 模板: `Check <object> to ensure that <expected_state>, otherwise it may lead to <issue>.`
- 例句: Check the Barcode of the samples to be pooled to ensure that no two samples share the same Barcode, otherwise it may lead to poor sequencing quality.

### 标准混匀步骤
- 模板: `Vortex <object> to mix well, centrifuge briefly for <time>, and <post_action>.`
- 例句: After the reagent has thawed, vortex for 5 seconds to mix, briefly centrifuge, and place on ice for later use.

### 禁止事项
- 模板: `Do not <action_1>; do not <action_2>.`
- 例句: Do not place the DNB Polymerase Mix II (OS-V4.0) at room temperature; do not hold the tube wall for an extended period.

### 执行反应步骤
- 模板: `Immediately add <volume> of <reagent>, using a <tool> to <action> <count> times.`
- 例句: Immediately add 20 μL of DNB termination buffer, using a wide-bore pipette tip (without filter) to slowly pipette up and down to mix 5 to 8 times.

### 定义/术语说明
- 模板: `<Term_A> represents <meaning_A>, and <Term_B> represents <meaning_B>.`
- 例句: C1 represents the FFPE library concentration (ng/μL) obtained from the "Library Concentration" section on page 9, and C2 represents the FF V1.3 library concentration (fmol/μL) obtained from "Library Concentration" on page 9.

### 存储/保存指南
- 模板: `The prepared <item> can be stored at <temperature> for later use and should be used within <time_limit>.`
- 例句: The prepared DNBs can be stored at 4 °C for later use and should be used within 48 hours.

### 参考引用确认
- 模板: `Confirm <item> according to <section_title>.`
- 例句: Confirm the library volume and the number of preparations according to "Estimating the Required Amount of dsDNA Library".

### 否定限制条件
- 模板: `If <condition>, it is not recommended for <action>, and the <scheme> needs to be <action>.`
- 例句: If it is lower than 5%, it is not recommended for sequencing, and the pooling scheme needs to be re-planned.

### 条件动作要求
- 模板: `If <Condition>, <Action> is required.`
- 例句: If the DNB concentration is unacceptable, re-preparation is required.

### 时间顺序步骤
- 模板: `After <Action> is complete, <Verb> <Object>.`
- 例句: After DNB preparation is complete, take 2 μL of DNB.

### 操作建议
- 模板: `When <Condition>, it is recommended to <Action> to <Goal/Avoidance>.`
- 例句: When the number of samples is large, it is recommended to perform quantification in batches to avoid inaccurate DNB concentration quantification.

### 文档指引
- 模板: `For <Action>, see "<Document Title>" on page <Page Number>.`
- 例句: For operation, see "DNB Quantitative Operation Guide" on page 45.

### 计算步骤指令
- 模板: `<Action> <Target>.`
- 例句: Calculate the theoretical relative quantity of each sample.

### 公式定义
- 模板: `The <Property> of <Object> is: <Variable> = <Formula>.`
- 例句: The theoretical relative quantity of sample A is: A1 = required data amount of sample A / DNB concentration of sample A.

### 使用前准备操作
- 模板: `<Action> <Object> <Frequency/Duration> before use, then <Action> <Duration>.`
- 例句: Gently invert and mix 5 times before use, then centrifuge for 1 minute.

### 目的与约束
- 模板: `To ensure <Goal>, it is recommended that <Subject> <Constraint/Ratio>.`
- 例句: To ensure base balance for sequencing, it is recommended that the mass ratio of the CITE V1.1-cDNA library to the CITE V1.1-ADT library be no less than 1:1.

### 操作流程标题
- 模板: `<Gerund> <Noun>`
- 例句: Placing Samples

### 标准操作指令
- 模板: `<Verb> <Object>`
- 例句: Prepare cleaning reagent tubes

### 禁止性规定
- 模板: `<Subject> must not be <VerbPastParticiple> / It is strictly prohibited to <Verb> <Object>`
- 例句: Reagent components from different batches must not be mixed.

### 条件触发程序
- 模板: `If <Condition>, <Imperative clause>`
- 例句: If this occurs, flush immediately.

### 产品用途说明
- 模板: `This product is <Purpose/Usage restriction>`
- 例句: This product is for scientific research use only

### 文件参考引用
- 模板: `Table/Chapter <Number> <Title>`
- 例句: Table 1 Example of sequencing cycles

### 产品规格描述
- 模板: `<Product Name>, <Volume> × <Quantity> <Unit>`
- 例句: Inactivated MDA Reagent, 3.50 mL × 1 vial

### 步骤动作指令
- 模板: `<Verb> <Object> from <Source>`
- 例句: Take out the DNB Loading Buffer 6 from the DNBSEQ-T7RS DNB Loading Kit.

### 步骤条件设置
- 模板: `<Verb> at <Condition> for <Duration>`
- 例句: Thaw at room temperature for 0.5 hours.

### 多重禁止指令
- 模板: `Do not <Verb>, <Verb>, or <Verb>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 推荐建议
- 模板: `For <Subject>, it is recommended to <Verb>...`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### 条件触发动作
- 模板: `If <Condition>, <Action>.`
- 例句: If crystals are observed in DNB Loading Buffer 6, vortex continuously...

### 强制性要求
- 模板: `For <Process>, <Object> must not be used; you must <Verb>.`
- 例句: For DNB preparation and loading, filter tips must not be used; you must use the recommended brand catalog numbers.

### 文档引用指引
- 模板: `For <Topic>, see "<Section>" on page <Number>.`
- 例句: For the preparation method of 0.1 M NaOH, see "Cleanup Preparation" on page 38.

### 步骤放置
- 模板: `Place the <object> onto the <location>.`
- 例句: Place the prepared sample loading reagent plate onto the reagent plate tray of the MGIDL-T7RS.

### 步骤加液
- 模板: `Add <quantity> of <reagent> to <location>.`
- 例句: add 4 mL of 0.1 M NaOH to well 11

### 条件建议
- 模板: `If <condition>, you can <action>.`
- 例句: If it is not displayed, you can manually enter it according to the prompts.

### 前置要求
- 模板: `Before <action>, ensure <requirement>.`
- 例句: Before placing the slide, ensure that none of the four sealing gaskets on the slide platform are missing.

### 界面指令
- 模板: `Click [<button>], and select [<option>].`
- 例句: Click [Start], and select [Yes].

### 图表说明
- 模板: `Figure <number> <description>`
- 例句: Figure 6 Sample loading reagent plate well position information and liquid addition operation

### 建议操作
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to store the loaded slide in a resealable bag to prevent the edges from drying out.

### 参考声明
- 模板: `The <item> is for reference only; the actual <item> depends on <factor>.`
- 例句: The manual operation time mentioned above is for reference only; the actual time depends on the proficiency of the operator.

### 试剂解冻指令
- 模板: `Remove <reagent> from <kit> and place it on ice to thaw.`
- 例句: Remove DNB Polymerase Mix I (OS-V4.0) from the spatiotemporal visualization reagent kit and place it on ice to thaw.

### 反应体系混匀与离心
- 模板: `After <action>, mix by <method> for <time>, briefly centrifuge, and keep on ice for use.`
- 例句: After thawing, mix by vortexing for 5 seconds, briefly centrifuge, and keep on ice for use.

### 表格引用/标题
- 模板: `Table <number>: <title>`
- 例句: Table 8 Reagent Preparation 2

### 操作指导引用
- 模板: `For specific operations, please refer to page <page>, '<section_title>'.`
- 例句: For specific operations, please refer to page 40, 'Operation Guide for DNB Quantification using Qubit'.

### 条件限制/替代方案
- 模板: `If <condition>, <action>.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the manual shall prevail.

### 负向操作约束
- 模板: `Do not <action>, and avoid <action>.`
- 例句: Do not place the DNB Polymerase Mix II (OS-V4.0) at room temperature, and avoid prolonged contact with the tube wall.

### 保存与使用期限
- 模板: `The prepared <item> can be stored at <temperature> and used within <time>.`
- 例句: The prepared DNB can be stored at 4 °C and used within 48 hours.

### 器材限制与禁止操作
- 模板: `<item> must be mixed using <tool>; do not <action1>, <action2>, or <action3>.`
- 例句: DNB must be mixed using wide-bore pipette tips (without filter); do not centrifuge, vortex, or pipette vigorously.

### 基于文档的计算指令
- 模板: `According to '<section_title>' on page <page>, calculate the <data> required for each <process>.`
- 例句: According to 'Library concentration' on page 6, calculate the volume of dsDNA library required for each DNB preparation.

### 操作步骤序列
- 模板: `<Action_1>, <Action_2>, then <Action_3>.`
- 例句: Take out the DNB Loading Buffer II, place it on an ice box for approximately 30 minutes until thawed, then use a vortex mixer...

### 条件触发操作
- 模板: `If <Condition>, <Action>.`
- 例句: If crystals are found in DNB Loading Buffer II, use a vortex mixer to continuously oscillate vigorously for about 1~2 minutes...

### 强制性约束
- 模板: `<Subject> must be <Action>.`
- 例句: The DNB loading mix must be prepared immediately before use.

### 资源需求说明
- 模板: `<Subject> requires <Quantity> <Unit> of <Material>.`
- 例句: Each flow cell (FCL) requires 266 μL of DNB loading mix 1.

### 文档引用
- 模板: `For <Description>, please refer to <Document_Reference>.`
- 例句: For detailed DNB loading operations, please refer to the MGIDL-200H Portable Pipettor Quick Operation Guide.

### 目的说明
- 模板: `<Action> to ensure <Desired_Outcome>.`
- 例句: ...until the color of Reagent No. 9 is uniform throughout the upper and lower layers, to ensure the reagent is thoroughly mixed.

### 后置处理与储存
- 模板: `After <Action>, <Storage_Action> at <Temperature> for later use.`
- 例句: After complete thawing, store in a 2 °C-8 °C refrigerator for later use.

### 参考引用
- 模板: `For <target>, refer to <location>, "<title>".`
- 例句: For the preparation method, refer to page 38, "Cleaning Preparation".

### 状态检查与预警
- 模板: `Check if <condition>; <consequence> will lead to <failure>.`
- 例句: Check if the water level in the pure water tank is sufficient; insufficient pure water will lead to sequencing failure.

### 必要性要求
- 模板: `This <item> is used in <context>, so its <attribute> must be ensured.`
- 例句: This pure water is used in sequencing, so its cleanliness must be ensured.

### 放置与安置
- 模板: `Place <object> into <location>, ensuring <condition>.`
- 例句: Place the gasket into the gasket groove, ensuring it is flat.

### 时间前置准备
- 模板: `Remove <item> <time> in advance, <action1>, and <action2> for use.`
- 例句: Remove dNTP Mix and dNTP Mix II 1 hour in advance, thaw at room temperature, and place on ice or at 4°C for use.

### Sequential Action Instruction
- 模板: `Add <substance> to <target>, <action_1>, and then <action_2>.`
- 例句: Add DNA polymerase mixture II to the dNTPs mixture in the tube, gently invert 4-6 times to mix, and then transfer the mixture to well No. 1.

### Pre-operation Requirement
- 模板: `<substance> must be <verb_past_participle> for <duration> before <action>ing.`
- 例句: The dNTPs mixture II must be vortexed for 5 seconds to mix before loading, and then briefly centrifuged before use.

### Interface Action Instruction
- 模板: `Click the <icon_description> icon next to [<interface_element>] to <action>.`
- 例句: Click the ⊕ icon next to [DNB ID] to display information for the 4 lanes.

### Prohibition Warning
- 模板: `Do not <verb> <object> to avoid <negative_outcome>.`
- 例句: When using MDA Polymerase Mix II, do not touch the inner wall of the tube where the reagent is contained to avoid affecting the enzymatic activity.

### Diagram Caption
- 模板: `Figure <number>: <Description of figure>`
- 例句: Figure 9: Opening of the reagent trough loading wells

### Data Entry Instruction
- 模板: `Move the cursor to the entry field next to [<interface_element>] and enter <data_description>.`
- 例句: Move the cursor to the entry field next to [DNB ID] and enter the library name or ID.

### Selection Instruction
- 模板: `Select <option> from the [<menu_name>] drop-down menu.`
- 例句: Select the spatial transcriptomics sequencing scheme from the [Sequencing Scheme] drop-down menu.

### 点击指令
- 模板: `Click [<button_name>] to <action>.`
- 例句: Click [Next] to review the information.

### 操作步骤
- 模板: `<step_number>. After <action>, click [<button_name>] and select [<option_name>].`
- 例句: 1. After confirming the information is correct, click [Start] and select [Yes].

### 表格准备指令
- 模板: `Prepare <item> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### 条件选择指令
- 模板: `Select <option> in the following situations:`
- 例句: Select manual cleaning in the following situations:

### 试剂有效期说明
- 模板: `Shelf life: <duration> at <temperature>`
- 例句: Shelf life: 1 month at 4 °C

### 流程结束说明
- 模板: `When <process_name> are finished, the interface shown below will appear.`
- 例句: When the sequencing and cleaning processes are finished, the interface shown below will appear.

### 条件式指令
- 模板: `Skip this step if <condition>.`
- 例句: Skip this step if there is no slide on the MGIDL-T7RS.

### 强制性维护要求
- 模板: `<object> should be <past_participle> <frequency_or_condition>.`
- 例句: each cleaning slide should be replaced every month or after 10 uses.

### 衔接式操作说明
- 模板: `<verb> <object> to <verb> <object>.`
- 例句: Click [Start] on the interface, select [Yes] in the pop-up dialog box to start the DNBSEQ-T7RS manual cleaning,

### 确认式陈述
- 模板: `Confirm that <clause>.`
- 例句: Confirm that the water in the pure water bucket has reached 4.5 L.

### 异常处理建议
- 模板: `If <condition>, please <action>.`
- 例句: If the above methods still cannot resolve the abnormal negative pressure, please contact technical support.

### 状态陈述
- 模板: `<noun_phrase> can be <verb> <location>.`
- 例句: Cleaning slides can be stored at room temperature.

### 流程引导
- 模板: `When <condition>, the operating steps are as follows:`
- 例句: When the negative pressure is abnormal, the negative pressure value will be displayed in red. The operating steps are as follows:

### 动作目的说明
- 模板: `<action>, ensuring <clause>.`
- 例句: Gently wipe the platform surface with a moistened dust-free paper or cloth, and blow the platform clean with a compressed air can, ensuring no visible dust.

### 条件执行句式
- 模板: `When <condition>, <action>.`
- 例句: When pumping failure occurs on DL-T7RS and DNBSEQ-T7RS:

### 步骤衔接句式（结果导向）
- 模板: `If there is still no improvement, please <action>.`
- 例句: If there is still no improvement, please contact technical support.

### 强制禁止句式
- 模板: `Do not <action>.`
- 例句: Do not touch the conical walls of the assay tube.

### 必要条件句式
- 模板: `<subject> must be <verb-past-participle> <time/condition>.`
- 例句: The Qubit working solution must be used within 0.5 hours after preparation.

### 操作步骤描述句式
- 模板: `<imperative-verb> <object> <direction/location>.`
- 例句: Remove the sequencing flow cell, check the seal for dust, and use a compressed air duster to blow away the dust.

### 步骤指引句式
- 模板: `<imperative-verb> <object> according to <reference>.`
- 例句: Prepare reagents for standard tubes and test sample tubes according to the table below:

### 故障处理句式
- 模板: `If <condition> still cannot be resolved by the methods above, please <action>.`
- 例句: If the pumping abnormality still cannot be resolved by the methods above, please contact technical support.

### 检查确认句式
- 模板: `Check if <condition>; if not, <action>.`
- 例句: Check if the reagent needle is moving normally; if not, restart the sequencer's control software.

### 交互操作说明句式
- 模板: `Click [<button_name>]. The instrument will <automatic_action>.`
- 例句: Click [Next]. The instrument will automatically enter the slide ID.

### 注意事项/限制句式
- 模板: `<subject> is fragile; please <action> during operation.`
- 例句: The carrier is fragile; please control the force during operation.

### 动作前置条件
- 模板: `After <action>, click [Action Button].`
- 例句: 1. After confirming that all information is correct, click [Start].

### 结果导向指令
- 模板: `Click [Action Button] to <goal>.`
- 例句: click [Yes] to start sequencing

### 目的/意图表达
- 模板: `To ensure <requirement>, <subject> automatically <verb>.`
- 例句: To ensure sequencing quality, the sequencer automatically performs one additional cycle for calibration

### 条件场景触发
- 模板: `When <condition>, the system will prompt: [Prompt Message].`
- 例句: When using version control software for the first time or after an update, the system will prompt: [Perform maintenance cleanup?].

### 准备工作指引
- 模板: `Prepare <item> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### 有效期与储存要求
- 模板: `Shelf life: <duration> when stored at <temperature>.`
- 例句: Shelf life: 1 month when stored at 2–8 °C

### 包含/组成描述
- 模板: `The <subject>, named by <identifier>, mainly contains <item1>, as well as <item2>.`
- 例句: The data folder, named by the slide ID, mainly contains image data, as well as data generated during the instrument's operation.

### Step-by-step instruction (Start)
- 模板: `<step_number>. Before <action> begins, <subject> <verb> <object>.`
- 例句: 1. Before sequencing begins, log in to your account and click [Clean] on the main interface.

### UI Interaction
- 模板: `Click the <UI_element> to the right of <setting>, and select <option> to <purpose>.`
- 例句: 5. Enter the cleaning interface, click the drop-down list to the right of [Cleaning Type], and select [Routine Cleaning] to start cleaning.

### Conditional Logic
- 模板: `If <condition> appears, select <UI_element>, and the instrument will automatically <action>.`
- 例句: 6. If the following pop-up appears, select [Yes], and the instrument will automatically raise the needle.

### Referencing Documentation
- 模板: `For <purpose>, please refer to <doc_section> on <page_number>.`
- 例句: For detailed steps, please refer to 'Placing the Slide' on page 24.

### Maintenance/Troubleshooting
- 模板: `When <parameter> is <condition>, please perform the following operations to <purpose>:`
- 例句: When the DNB concentration is lower than 8 ng/μL, please perform the following operations to troubleshoot the issue:

### Action Definition
- 模板: `Place <item> into the <holder>, and close the <component_door>.`
- 例句: 3. Place the cleaning reagent tube 1 into the sample tube holder and close the reagent compartment door.

### Requirement Definition
- 模板: `<process> is required for <condition>.`
- 例句: A super deep cleaning is required for the initial installation, upgrade installation, or when it has not been cleaned for over 14 days.

### 条件操作指令
- 模板: `If <condition>, please <action>.`
- 例句: If the reagent needle fails to descend correctly, restart the sequencing software.

### 标准操作步骤
- 模板: `<Imperative verb> the <object> according to <reference>.`
- 例句: Perform a maintenance wash on the sequencer according to "Full Maintenance Wash (approx. 94 minutes)" on page 33.

### 状态定义
- 模板: `<Subject> Status: <Status description>.`
- 例句: Status A: Paused 20.0℃-91.6ka

### 异常处理流程
- 模板: `If <problem condition> persists, please contact an engineer.`
- 例句: If there is no improvement after the maintenance wash, please contact an engineer.

### 负压/环境监测异常提示
- 模板: `When the <metric> value is displayed in <color>, the <metric> is abnormal. Please perform the following operations:`
- 例句: When the negative pressure value is displayed in red, the negative pressure is abnormal. Please perform the following operations:

### 免责声明句式
- 模板: `Nothing herein is intended to or should be understood as <noun_phrase>, expressed or implied.`
- 例句: Nothing herein is intended to or should be understood as any warranty of the performance of any product listed or described herein, expressed or implied.

### 操作建议句式
- 模板: `Note: Please <action> to use with <object>.`
- 例句: Note: Please download the latest version of the instruction manual to use with the corresponding version of the kit.

### 提示与警示句式
- 模板: `Tip/Key Steps/Note: <description>.`
- 例句: Key Steps: Pay special attention to these steps to avoid experimental failure or poor outcomes.

### 暂停建议句式
- 模板: `Stop point: You can <action> here and <action>.`
- 例句: Stop point: You can pause the experiment here and store the samples.

### 产品功能描述句式
- 模板: `The <product_name> enables the <action> of <target>.`
- 例句: The STOmics Stereo-CITE protein-transcriptome reagent kit enables the co-detection of the whole transcriptome and ultra-high-plex proteins.

### 兼容性建议句式
- 模板: `Sequencing libraries constructed using this product can be sequenced using <platform_name>.`
- 例句: Sequencing libraries constructed using this product can be sequenced using the DNBSEQ sequencing platform.

### 组分构成句式
- 模板: `Each reagent kit consists of the following <number> components:`
- 例句: Each reagent kit consists of the following four components:

### 保存建议句式
- 模板: `Please <action> according to the specified conditions as soon as possible.`
- 例句: Please save the product according to the specified conditions as soon as possible.

### 物流异常处理句式
- 模板: `If an abnormal <condition> is discovered, you may <action>.`
- 例句: If an abnormal temperature in the cold chain box is discovered, you may request the logistics provider to print the real-time temperature monitoring record sheet.

### 条件生效句式
- 模板: `When <condition_1>, <condition_2>, and <condition_3> are all correct, <subject> can maintain full activity.`
- 例句: When transportation conditions, storage conditions, and usage methods are all correct, all components can maintain full activity.

### 参考指引句式
- 模板: `After receiving the <object>, please refer to the "<document_title>" to <action>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 产品明细格式
- 模板: `<Component Name> <Cat. No.> <Specification>`
- 例句: Blocking Reagent 1000044666 Transparent 60 µL × 1

### 选择性建议
- 模板: `Choose one from <Subject> with the same <Criteria>.`
- 例句: Choose one from brands with the same superscript number.

### 储存与有效期说明
- 模板: `Storage temperature: <Temp>; <ValidityType>: See label.`
- 例句: Storage temperature: Room temperature; Validity under room temperature transport: See label

### 验证适用声明
- 模板: `This kit has been validated for use with <Product>.`
- 例句: This kit has been validated for use with TotalSeq™-A primary antibodies.

### 术语定义
- 模板: `An <Term> is a <NounPhrase> that <Function>.`
- 例句: An isotype control antibody is an antibody that maintains similar properties to the primary antibody but lacks a specific target.

### 资源引用说明
- 模板: `For <Topic>, please refer to <Source>.`
- 例句: For the selection of isotype control antibodies, please refer to this website: https://www.biolegend.com/en-us/search-results

### 表格头部结构
- 模板: `<Col1> <Col2> <Col3>`
- 例句: Component Information Cat. No. Specification

### 推荐操作
- 模板: `It is recommended to <verb> <object> <time/condition>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 试剂处理
- 模板: `Remove <object> from <source>, <verb>, and keep <condition>.`
- 例句: Remove sheared salmon sperm DNA from -20°C and thaw; use 30 μL per chip and keep on ice.

### 试剂稀释
- 模板: `Dilute <amount> of <reagent> to <amount> with <diluent>.`
- 例句: For 5X SSC, take 5 mL of 20X SSC and dilute to 20 mL with Nuclease-Free Water.

### 步骤前提
- 模板: `Before <step>, <verb> <object> <condition>.`
- 例句: Before conducting experiments, please familiarize yourself with the precautions for the instruments to be used.

### 安全操作
- 模板: `Avoid <action> of <object> with <hazard>; do not <verb> <object>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 器材预处理
- 模板: `Pre-<verb> <instrument> to <temperature>.`
- 例句: Pre-cool the cryostat chamber to -20°C and the specimen head to -15°C ~ -10°C.

### 产品用途声明
- 模板: `This product is for <purpose> only and is not for <prohibited_use>.`
- 例句: This product is for research use only and is not for clinical diagnostic purposes.

### 基础动作指令
- 模板: `<Verb> the <Object> <Location/Modifier> to <Action/Time>.`
- 例句: Take the OCT-embedded tissue block out of the -80°C freezer and place it in the cryostat to equilibrate for 30 min;

### 条件引导操作
- 模板: `During the <Process>, <Action> <Modifier>.`
- 例句: During the tissue temperature equilibration process, take out a sufficient amount of 4% PFA solution from the 4°C refrigerator;

### 溶液添加与孵育
- 模板: `Add <Volume>/chip of <Reagent>, and incubate at <Temperature> for <Time>.`
- 例句: Immediately add 400 μL/chip of Wash Buffer, and incubate at room temperature for 1 min;

### 禁止项与风险预警
- 模板: `Avoid <Action/State> to <Prevent Consequence>.`
- 例句: Strictly avoid tissue drying during the liquid exchange process, as tissue drying can easily generate non-specific signals.

### 步骤重复
- 模板: `Repeat steps <Step A>-<Step B> <Frequency>, for a total of <Total> washes/times.`
- 例句: Repeat steps e.-f. once, for a total of 2 washes.

### Reference to Documentation
- 模板: `Refer to <Location> to <Action>.`
- 例句: Refer to Table 2-5 in section 2.6 DAPI Staining to prepare the DAPI working solution

### Procedural Addition
- 模板: `Add <Volume> of <Reagent> to <Target>, and incubate at <Condition> for <Time>.`
- 例句: Add 200 μL of Wash Buffer to the chip and incubate at room temperature for 1 min;

### Procedural Removal
- 模板: `Aspirate and discard the <Solution> from <Location> using <Tool>, <Constraint>.`
- 例句: Aspirate and discard the secondary antibody incubation solution from one corner of the chip using a pipette, keeping the chip tissue moist

### Process Caution
- 模板: `Ensure <Object> does not <Condition> during <Process>.`
- 例句: Ensure the chip does not dry out during the liquid exchange process

### Reagent Usage Constraint
- 模板: `Preheat only the amount of <Reagent> required; do not <Action> repeatedly.`
- 例句: Preheat only the amount of Decrosslinking Reagent required; do not preheat repeatedly.

### Tool Operation
- 模板: `Use <Tool> to <Action> <Object>.`
- 例句: Use a pipette to slowly draw 5 μL of Glycerol and add it dropwise to the center of the tissue

### Repetition Instruction
- 模板: `Repeat <Step_Range> <Frequency>.`
- 例句: Repeat washing steps c.-d. once;

### 提前配制参考
- 模板: `Prepare <object> in advance by referring to <reference>.`
- 例句: Prepare the 1X Tissue Permeabilization Reagent working solution in advance by referring to Table 2-6.

### 避免接触
- 模板: `Avoid contact between <component A> and <component B>.`
- 例句: Avoid contact between the carrier and the front surface of the chip.

### 倾斜并移除试剂
- 模板: `Slightly tilt the <component> at an angle less than <angle>. Use a pipette to aspirate and discard <substance>.`
- 例句: Slightly tilt the handheld carrier at an angle less than 20°. Use a pipette to aspirate and discard the Wash Buffer.

### 指定用量加液
- 模板: `Add <substance> at a volume of <volume> per chip.`
- 例句: Add PR Rinse Buffer solution (containing 5% RI) at a volume of 200 μL per chip.

### 即时操作以避免降解
- 模板: `Immediately add <substance> after <action/step> to prevent <problem>.`
- 例句: Immediately add RT Mix after completing step i to prevent RNA degradation.

### 反应条件与调整
- 模板: `Perform <reaction> at <temperature> (adjust the <parameter> based on <conditions>).`
- 例句: Perform the permeabilization reaction at 37°C (adjust the permeabilization time based on actual conditions).

### 处理沉淀
- 模板: `If <observation> is observed in the <substance>, dissolve at <temperature> and return to <condition>.`
- 例句: If white precipitate is observed in the buffer, it can be dissolved at 55°C and then returned to room temperature.

### 磁珠混合与分离
- 模板: `After mixing <sample> and <magnetic beads> thoroughly, place them on a <device> for <time>.`
- 例句: After mixing the sample and magnetic beads thoroughly, place them on a magnetic stand for separation.

### 添加并混匀
- 模板: `Add <volume> <reagent> to <target>, vortex to mix, [and] incubate at <temperature> for <time>.`
- 例句: Add 22 μL of Nuclease-Free Water to resuspend, vortex to mix, and incubate at room temperature for 5 min.

### 转移产物
- 模板: `Transfer the <substance> (<volume>) to a new <container>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 重复步骤
- 模板: `Repeat step <number> once;`
- 例句: Repeat step 4) once;

### 条件补足
- 模板: `If the <sample> is less than <volume>, make up to <volume> with <reagent>.`
- 例句: If the volume of the above recovered sample is less than 42 μL, make up to 42 μL with Nuclease-Free Water.

### 存储建议
- 模板: `The <product> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### 依据指引
- 模板: `Prepare <item> according to <table/section> in <context>.`
- 例句: Prepare cDNA PCR Mix following Table 2-9 in section 2.15. Transcriptome cDNA Amplification, for a total volume of 100

### 磁力架操作
- 模板: `Keep the <container> on the magnetic rack [stand], <action>.`
- 例句: Keep the centrifuge tube on the magnetic stand, open the lid, and air-dry at room temperature for 5-8 min

### 操作规范提示
- 模板: `The <item> should be operated against <location>; do not <prohibited_action>.`
- 例句: The pipette tip should be operated against the tube wall away from the magnetic stand; do not pipette up and down or disturb the magnetic beads.

### 表格配制标题
- 模板: `Table <number> Preparation of <object>`
- 例句: Table 2-14 Preparation of Qubit dsDNA Mix

### 技术指标描述
- 模板: `The <subject> is typically <comparative> than <value>`
- 例句: The DNA concentration is typically higher than 5 ng/μL.

### 动作重复
- 模板: `Repeat step <number> once;`
- 例句: Repeat step 3) once;

### 存储条件
- 模板: `<subject> can be stored at <temperature> for <duration>.`
- 例句: ADT amplification products can be stored at −20°C for 1 month.

### 免责声明
- 模板: `This product is for <purpose> only, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 图表引用
- 模板: `Figure <number>. <description> (as shown in <reference>)`
- 例句: Figure 5. 2100 peak profile of the purified ADT library product (as shown in Figure 5)

### Procedural Step
- 模板: `<Verb> <object> <location/manner>.`
- 例句: Add the corresponding reagents into the reaction wells as needed.

### Alignment Instruction
- 模板: `Align <object_A> with <object_B>, and <verb> them together.`
- 例句: Align the positioning holes of the gasket with the positioning posts of the upper cover, and slowly fit them together.

### Soft Prohibition
- 模板: `Do not <verb> <object> to avoid <consequence>.`
- 例句: Do not attach any edge labels or stickers to the chip carrier to avoid leakage due to poor adhesion.

### Conditional Step/Correction
- 模板: `If <condition>, <action>.`
- 例句: If it is difficult to snap together, first check whether the base and the chip carrier are installed correctly.

### Requirement Constraint
- 模板: `The entire operation must be performed in a <condition> to <purpose>.`
- 例句: The entire operation must be performed in a clean environment to prevent environmental impurities from contaminating materials or chips.

### Tool-based Instruction
- 模板: `Use <tool> to <verb> <object> from <location>.`
- 例句: Use an air duster to blow away any impurities or debris from the surfaces of the gasket, top cover, base, and chip carrier.

### Reference Pointer
- 模板: `For further information on <topic>, please refer to <location>.`
- 例句: For further information on the Catalog No. of accessory kit products and their specific components, please refer to Table 1-1 and Table 1-2.

### Note/Reminder
- 模板: `Note: <instruction>.`
- 例句: Note: Please download the latest version of the user manual and use it with the corresponding version of the reagent kit.

### Legal Disclaimer
- 模板: `Nothing herein is intended or shall be construed as <interpretation>.`
- 例句: Nothing herein is intended or shall be construed as regarding this any warranty regarding the performance of any product.

### Procedural Instruction
- 模板: `<Verb> <Object> <Prepositional Phrase/Context>`
- 例句: Use a pipette to aspirate as much reagent as possible from the carrier's reaction well.

### Prohibition
- 模板: `Do not <Verb> <Object>.`
- 例句: Do not bump or shake the carrier.

### Conditional Action
- 模板: `If <Condition>, <Imperative Verb> <Action>.`
- 例句: If it is necessary to disassemble the carrier, do so after reagent removal.

### Recommendation
- 模板: `It is recommended to <Verb> <Object>.`
- 例句: It is recommended to purchase the Stereo-seq V3 Cassette Disassembly Tool.

### State Assurance
- 模板: `Ensure <Object> is <Adjective/State>.`
- 例句: ensuring it is stable and the chip carrier is facing down.

### Header Formatting
- 模板: `<Number>. <Noun Phrase>`
- 例句: 4. Pressure-Sensitive Film Removal

### Regulatory Disclaimer
- 模板: `This product is for <Purpose> only, not for <Negative Purpose>.`
- 例句: This product is for research use only, not for diagnostic purposes.

### Preventive Action
- 模板: `<Action> to prevent <Negative Outcome>.`
- 例句: do so after reagent removal to prevent reagent splashing during the disassembly.

### 外部指引
- 模板: `Regarding <topic>, please refer to the "<document_name>".`
- 例句: Regarding the requirements for microscopes, please refer to the "STOmics® Microscope Evaluation Reference Manual".

### 功能描述
- 模板: `<product_name> is a <kit_type> designed to <objective>.`
- 例句: The STOmics® Stereo-seq Customized Chip Tissue Permeabilization Reagent Kit is a pre-experiment kit designed to optimize tissue permeabilization time.

### 组成说明
- 模板: `Each <kit_name> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 预防措施
- 模板: `To avoid <issue>, <action> is recommended.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended.

### 信息引用
- 模板: `For further information regarding <topic>, please refer to Table <number>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 and Table 1-2.

### 动作指令句
- 模板: `<Verb> <Object> (<Prepositional Phrase>).`
- 例句: Fill metal embedding cassette A with the pre-cooled OCT in advance.

### 禁止性指令
- 模板: `Do not <verb> <object>.`
- 例句: Do not ingest samples or reagents.

### 适用条件描述
- 模板: `This <subject> is suitable for <condition>.`
- 例句: This embedding method is suitable for tissues with dimensions < 2 cm × 3 cm × 0.7 cm.

### 限制条件描述
- 模板: `The <subject> should not <verb> <limit>.`
- 例句: The tissue section should not occupy more than 80% of the chip area.

### 建议性条款
- 模板: `It is (strongly) recommended to <verb> <object>.`
- 例句: It is recommended to cut 10-20 tissue sections of 10 μm thickness.

### 时间顺序约束
- 模板: `Within <time> of <event>, <do_action>.`
- 例句: Within 30 minutes of removing fresh tissue, use sterile non-woven cloth or lint-free paper to wipe the tissue surface liquid dry.

### 条件限定说明
- 模板: `Unless otherwise specified, <statement>.`
- 例句: Unless otherwise specified, Nuclease Free Water is used for all liquids in this experiment to dilute reagents.

### 后置条件动作
- 模板: `After <action> for <duration>, <do_next_action>.`
- 例句: After freezing for 5 min, remove metal embedding mold B and steel ruler.

### 引用跳转提示
- 模板: `Refer to <reference_target>.`
- 例句: Refer to Figure 1: Mouse brain tissue section RNA RIN value peak plot.

### 必要性声明
- 模板: `It is necessary to consider whether <subject> can meet <requirement>.`
- 例句: During sample preparation, in addition to project requirements, it is necessary to consider whether the sample's Z-axis can meet the consumption needs.

### 试剂取用与稀释
- 模板: `Take <volume> of <reagent_name> and add to <volume> of <diluent_name>, volume required is at least <volume>/chip.`
- 例句: Take 7.5 μL of RI and add to 142.5 μL of 0.1X SSC, volume required is at least 150 μL/chip.

### 试剂配置建议
- 模板: `<reagent_name> should be prepared immediately before use. Please check the pH <condition>.`
- 例句: 0.01N HCl should be prepared immediately before use. For pre-made 0.1N HCl and newly purchased HCl, please check the pH value.

### 步骤衔接/流程描述
- 模板: `<action_verb> the <object> to <target> in advance;`
- 例句: a. Adjust the slide dryer temperature to 37°C in advance;

### 操作限制/注意事项
- 模板: `Do not touch the <surface_part> of the chip.`
- 例句: The front side of the chip is the shiny side and contains probes for mRNA capture. Do not touch the surface of the chip.

### 清洗操作
- 模板: `Wash twice with <solution>, <additional_instruction>.`
- 例句: Wash twice with water (for a 2 cm * 3 cm chip, use 4000 μL of Nuclease Free Water in a 6 cm Petri dish and wash twice).

### 孵育/处理要求
- 模板: `Incubate the <reagent> in a <temperature> constant temperature incubator for <time> before use;`
- 例句: Incubate the permeabilization working solution in a 37°C constant temperature incubator for 10 min before use;

### 试剂添加顺序
- 模板: `For the chip with the longest <parameter>, add the <reagent> first, from <location>.`
- 例句: For the chip with the longest permeabilization time, add the permeabilization reagent first, from chip corners.

### 实验条件确保
- 模板: `Ensure <parameter> is in the range of <range>; at least <volume>/sample.`
- 例句: Dilute HCl to 0.01N, pH accurate to 2 (ensure pH value is in the range of 1.9-2.1; at least 5 mL/sample)

### 设备/环境操作
- 模板: `Place the chip in a <container> (sealed with <material>) and let it rewarm for <time>.`
- 例句: Place the chip in a 9 cm culture dish (the bottom is covered with Parafilm) and let it rewarm for 1 min.

### 废液处理/清理
- 模板: `Slightly tilt the chip and use a pipette to aspirate the <reagent> from <location>.`
- 例句: Slightly tilt the chip and use a pipette to aspirate the permeabilization reagent from one corner of the chip;

### 表格标题
- 模板: `Table <Number> <Title>`
- 例句: Table 3-1 Baking time for large chips of various sizes

### 依据表格操作
- 模板: `<Verb> the <Object> according to Table <Number>`
- 例句: Prepare the Total RNA hybridization Mix according to Table 3-4

### 防范措施/目的说明
- 模板: `Immediately <Verb> the <Object> to <Verb/Avoid> <Problem>`
- 例句: Immediately add the RT QC Mix to avoid RNA degradation

### 实验条件设定
- 模板: `<Subject> is <Condition>, <Condition>, <Condition>`
- 例句: Positive control* is mouse brain, 37°C, permeabilized for 12 min

### 操作步骤衔接
- 模板: `Slightly <Verb1> the <Object1>, and <Verb2> <Object2> <Direction/Method>`
- 例句: Slightly tilt the chip, and use a pipette to aspirate the solution from the upper surface

### 严禁/警告
- 模板: `The <Time/Condition> should not be too <Adjective>, so as to <Verb/Avoid> <Result>`
- 例句: The pre-cooling time should not be too long, so as to avoid water mist forming on the chip surface

### 技术规格
- 模板: `<Value>x <Noun>`
- 例句: 4x or 10x objective;

### 禁止要求
- 模板: `<Subject> should only use <Allowed_Items>; the use of <Forbidden_Items> is prohibited.`
- 例句: Folder names should only use letters, numbers, and underscores; the use of special characters such as spaces is prohibited.

### 强制要求
- 模板: `<Subject> must be <Verb_past_participle> under <Condition>.`
- 例句: Chips of the same tissue with different permeabilization times must be scanned under the same exposure conditions.

### 分类警示
- 模板: `<Category>: <Instruction>.`
- 例句: Critical Step: Pay special attention to these steps to avoid experimental failure.

### 变更记录
- 模板: `<Verb_past_tense> <Object> in/for <Component>.`
- 例句: Corrected the catalog numbers for some components of the Stereo-seq Library Preparation Kit.

### 实验结果陈述
- 模板: `At <Time/Condition>, <Subject> <Verb> <Description>.`
- 例句: at 12 min, details are clear, the signal is uniform, and brightness is maximal;

### 建议句式
- 模板: `If <condition>, it is recommended to <verb> <object>.`
- 例句: If the transfer time is long, it is recommended to use temperature-controlled containers for transportation.

### 索引/参考句式
- 模板: `For further information regarding <topic>, please refer to <reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-2.

### 产品功能句式
- 模板: `The <product> can be used to <verb> <target>.`
- 例句: The STOmics Stereo-seq Library Construction Kit can be used to construct whole-transcriptome 3'-end libraries.

### 使用用途限制句式
- 模板: `This product is intended for <purpose> and is not for use in <restriction>.`
- 例句: This product is intended for research use only and is not for use in clinical diagnostic procedures.

### 指令句式
- 模板: `Please <verb> the <object> according to <condition>.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 内容详情句式
- 模板: `This list details the <item> required for this <context>.`
- 例句: This list details the equipment and materials required for this experiment.

### 表格说明句式
- 模板: `Table <number> <information> of the <product>.`
- 例句: Table 1-1 Component information of the library construction kit.

### 条件约束
- 模板: `Unless otherwise specified, <statement>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids for reagent dilution in this experiment.

### 步骤执行
- 模板: `Prepare the <mixture_name> according to <table_reference>.`
- 例句: Prepare the fragmentation Mix according to Table 2-1.

### 警告/禁止
- 模板: `Avoid <action> / Do not <action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 合规处理
- 模板: `<subject> should be disposed of in accordance with relevant regulations.`
- 例句: All samples and all waste materials should be disposed of in accordance with relevant regulations.

### 状态平衡
- 模板: `<verb> to equilibrate to room temperature.`
- 例句: Remove magnetic beads in advance and equilibrate to room temperature.

### 取样操作
- 模板: `Take <amount> of <object> for <reaction>.`
- 例句: Take 20 ng of the cDNA amplification product for the fragmentation reaction.

### 实验室操作步骤
- 模板: `Keep the <Object> on the <Location>, and <Action> for <Duration/Condition>.`
- 例句: Keep the tube on the magnetic stand and add 400 μL of 80% ethanol to wash.

### QC结果描述
- 模板: `<Parameter> is usually <Condition>.`
- 例句: The concentration is usually greater than 10 ng/μL.

### 文档引用指令
- 模板: `Please refer to <Document Title> to <Action>.`
- 例句: Please refer to the "940-000037-00, High-throughput Sequencing Primer Kit (Stereomics)" user manual to prepare the DNBs.

### 浓度测定与记录
- 模板: `Take <Volume> of <Sample>, measure <Parameter> using <Tool>, and record it.`
- 例句: Take 1 μL of PCR product, measure the concentration using the Qubit dsDNA HS Kit, and record it.

### 严格操作提示
- 模板: `Please <Action> carefully, and operate strictly in accordance with the <Reference>.`
- 例句: Please read the corresponding instruction manual carefully before sequencing, and operate strictly in accordance with the content of the manual.

### 处理步骤重复
- 模板: `Repeat step <Step ID> once.`
- 例句: d. Repeat step c once.

### Pre-action Preparation
- 模板: `Before <action>, <imperative action>.`
- 例句: Before using the PCR Barcode Primer Mix, centrifuge it to collect the liquid at the bottom of the tube.

### Instructional Request
- 模板: `Please <action> after <event>.`
- 例句: Please check the following items after opening the aluminum foil bag:

### Procedural Reference
- 模板: `Refer to <source> when <action> (avoid <range>).`
- 例句: Refer to 3 libraries/lane when selecting a combination (avoid 1~4).

### Scope-based Reference
- 模板: `For <scope>, refer to <source>.`
- 例句: For different numbers of samples, refer to the recommended Barcode combination schemes in Appendix Table 2.

### Step-by-Step Procedure
- 模板: `Perform in <number> steps: 1. <action>. 2. <action>.`
- 例句: Perform in two steps: 1. Divide libraries 1-8 into one group... 2. Remaining libraries...

### Storage Condition
- 模板: `When <condition>, <subject> can be stored at <temperature> until <deadline>.`
- 例句: When unopened, the product can be stored at -20 °C or 4 °C until the expiration date on the label.

### Resource Navigation
- 模板: `Please visit the following link to <action>: <url>.`
- 例句: Please visit the following link to view or download: https://www.stomics.tech/resources/Documents/list

### Documentation Identification
- 模板: `Document Number: <id>.`
- 例句: Document Number: STOG04003

### 专用/限制条款
- 模板: `This product is for <purpose> only and not for <restricted_purpose> purposes.`
- 例句: This product is for research use only and not for diagnostic purposes.

### 权利声明
- 模板: `<Year> <Organization>. All rights reserved.`
- 例句: 2023 BGI Research. All rights reserved.

### 关键步骤提示
- 模板: `Key Steps: Pay special attention to these steps to avoid <negative_outcome>.`
- 例句: Key Steps: Pay special attention to these steps to avoid experimental failure or poor results.

### 暂停建议
- 模板: `Stopping point: You can <action> here and <action_continued>.`
- 例句: Stopping point: You can pause the experiment here and store the samples.

### 操作指导（带温度/条件）
- 模板: `<Action> (operated at <temperature_or_condition>).`
- 例句: Tissue fixation and eosin (operated at -20°C)

### 下载提示
- 模板: `Note: Please download the latest version of the instruction manual for use with <context>.`
- 例句: Note: Please download the latest version of the instruction manual for use with the corresponding version of the kit.

### 产品组成描述
- 模板: `Each reagent set consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### 建议/最佳实践
- 模板: `If the transfer time is long, it is recommended to use <method>.`
- 例句: If the transfer time is long, it is recommended to use temperature-controlled containers for transport.

### 排除责任声明
- 模板: `<Organization> makes no guarantee, and hereby disclaims any guarantee regarding the use of <target_content>.`
- 例句: BGI Research makes no guarantee, and hereby disclaims any guarantee regarding the use of any third-party products or protocols mentioned herein.

### 参照文档执行
- 模板: `Please refer to the "<Document>" to <Action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 产品订购标注
- 模板: `(<Requirement>)`
- 例句: (Must be ordered separately)

### 产品及货号定义
- 模板: `<Product Name> Cat. No.: <Number>`
- 例句: Stereo-seq Chip T carrier (1 cm * 1 cm) Cat. No.: 200CT114

### 步骤描述
- 模板: `<Number/Letter>. <Imperative Verb> <Object> from <Source>;`
- 例句: a. Take out the fixture and gasket from the Stereo-seq Slide Accessory Kit;

### 选择性指导
- 模板: `Select one from the listed brands (marked with *).`
- 例句: Select one from the listed brands (marked with *).

### 系统性前提条件
- 模板: `When <Condition A>, <Condition B>, and <Condition C> are correct, <Outcome>.`
- 例句: When transport conditions, storage conditions, and usage methods are correct, all components will maintain full activity.

### 目的/结果描述
- 模板: `To <goal>, <action>.`
- 例句: To avoid cross-contamination of samples, it is recommended to use pipette tips with filters and change tips when aspirating different samples.

### 动作建议
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to take out the reagent components in advance before use.

### 禁止项
- 模板: `Do not <action>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting up and down.

### 预设条件
- 模板: `Unless otherwise specified, <condition>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used as the liquid for diluting reagents in this experiment.

### 仪器设置
- 模板: `<Setting> for <purpose>`
- 例句: 37°C for slide baking and permeabilization (heated lid 42°C)

### Operation Instruction
- 模板: `<Verb> <object> <location/condition> [for <duration>].`
- 例句: Incubate at 37°C for 5 minutes.

### Conditional Consequence
- 模板: `If <condition>, it will cause <result>.`
- 例句: If the specimen head temperature is too low, it will cause cracks in the sections.

### State Verification
- 模板: `When <condition>, it is ready for <next step>.`
- 例句: When the chip surface is free of impurities, visible marks, any liquid residue, or wavy textures, it is ready for mounting.

### Parameter Constraint
- 模板: `<Subject> must not be <too adj>, to avoid <negative result>.`
- 例句: The pre-cooling time must not be too long to avoid condensation on the slide surface.

### Sequential Step
- 模板: `<Number/Letter>) <Imperative verb> <object> <details>.`
- 例句: 1) Place the glass slide face up in the cryostat and pre-cool for 1-6 min;

### 操作指令 - 添加试剂
- 模板: `Add <volume> of <reagent_name> to the <location>.`
- 例句: Add 100 μL of 0.01N HCl solution dropwise onto the chip, then aspirate the liquid from one corner of the chip.

### 操作指令 - 孵育/反应
- 模板: `Incubate at <temperature> for <time>.`
- 例句: Place the carrier on the PCR adapter, close the PCR lid, and incubate at 37°C for 10 min.

### 注意事项 - 确保状态
- 模板: `Ensure that <object> is <status>.`
- 例句: Ensure the chip is completely submerged in the solution.

### 注意事项 - 禁止/避免
- 模板: `Avoid <action>.`
- 例句: Avoid touching the front side of the chip when assembling the carrier.

### 操作指令 - 吸弃液体
- 模板: `Aspirate and discard the <liquid_name> from <location>.`
- 例句: Slightly tilt the holding carrier, use a pipette to aspirate and discard the PR Rinse Buffer solution from one corner of the reaction well.

### 步骤衔接 - 动作完成后
- 模板: `After <action> is complete, <next_action>.`
- 例句: After the incubation is complete, fix the support onto the carrier to assemble into a handheld carrier.

### 建议/推荐 - 操作策略
- 模板: `<Action> is recommended.`
- 例句: Manual focusing is recommended.

### 条件句 - 异常处理
- 模板: `If <condition>, then <action>.`
- 例句: If a large area (exceeding 4 fields of view) is not infiltrated by the H&E Mounting Medium during the mounting process, then you need to add more modeling points to this area.

### 前置准备
- 模板: `<Action> in advance according to <reference>.`
- 例句: Prepare the 1X Permeabilization Reagent working solution in advance according to [Preparation Before Experiment].

### 条件步骤
- 模板: `If <condition>, <verb> the <object>.`
- 例句: If a small amount of liquid remains on the tube wall, briefly centrifuge the tube.

### 混合与操作
- 模板: `Mix <object_A> with <object_B> at a <ratio> ratio, vortex to mix, and incubate at room temperature for <time>.`
- 例句: Mix the PCR product (100 μL) with magnetic beads equilibrated to room temperature at a 1:1 ratio, shake to mix, and incubate for 10 min.

### 使用前准备
- 模板: `Before each use, <verb_1> or <verb_2> the <object> to ensure they are thoroughly mixed.`
- 例句: Before each use, vortex the magnetic beads or pipette them up and down to ensure they are thoroughly mixed.

### 液体转移
- 模板: `Transfer the <substance> (<volume>) to a new <container>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube.

### 平衡要求
- 模板: `Equilibrate <object> to room temperature before use.`
- 例句: Equilibrate the magnetic beads to room temperature before use.

### 参数变更描述
- 模板: `<Parameter> <attribute> changed from <old_value> to <new_value>`
- 例句: Methanol pre-cooling time changed from 10-30 min to 5-30 min

### 操作步骤更新
- 模板: `<Step_name> updated.`
- 例句: Fluorescence imaging procedure updated.

### 步骤/配置修改
- 模板: `<Step/Component> modified to <new_action/specifications>.`
- 例句: Pre-permeabilization incubation step modified to use a carrier (fixture + gasket, excluding slide), incubated at 37°C

### 物料包含关系
- 模板: `Each reagent kit consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following three parts:

### 操作建议/指令
- 模板: `Note: Please <verb> the <object> and use it with the <attribute> of the kit.`
- 例句: Note: Please download the latest version of the instruction manual and use it with the corresponding version of the kit.

### 合规性声明
- 模板: `All <components> provided in this kit have undergone <process>, ensuring the <attribute>.`
- 例句: All reagents provided in this kit have undergone rigorous quality control and functional validation, ensuring the stability and repeatability of library preparation.

### 重要提示/警示
- 模板: `<Type>: Pay special attention; <consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may cause the experiment to fail.

### 建议/提示
- 模板: `If the <condition>, it is recommended to <action>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transportation.

### 条件要求
- 模板: `If <condition> is detected, you may <action>.`
- 例句: If an abnormality in the cold chain box temperature is detected, you may request the logistics provider to print the report.

### 操作指令 (祈使句)
- 模板: `Please refer to the "<document_title>" to <action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to properly save the product.

### 操作限制/禁止
- 模板: `<subject> must not be <action> for more than <duration>.`
- 例句: Resealed chips must not be stored for more than two weeks.

### 物料包含说明
- 模板: `The <kit_name> contains <component1> and <component2>.`
- 例句: The Stereo-seq carrier accessory kit contains fixtures for the chip carriers and detachable gaskets.

### 步骤衔接 (指令)
- 模板: `<action>, ensuring that <condition>.`
- 例句: Insert the gasket into the fixture, ensuring that the hole cutouts of the fixture and gasket are aligned.

### 检查步骤
- 模板: `Finally, inspect the <item1> and <item2> to ensure they are correctly positioned.`
- 例句: Finally, inspect the assembled fixture and chip carrier to ensure they are correctly positioned.

### 选择性操作
- 模板: `You may choose any one of the listed brands (marked with *) to <action>.`
- 例句: You may choose any one of the listed brands (marked with *) to use with the PCR adapter.

### 状态描述
- 模板: `When <condition> are all correct, all components can maintain complete activity within the validity period.`
- 例句: When transportation conditions, storage conditions, and usage methods are all correct, all components can maintain complete activity within the validity period.

### 基础操作指令
- 模板: `<Verb> <object> [prep] <location/target>.`
- 例句: Align the chip with the gasket hole to avoid contact between the fixture and gasket with the chip surface;

### 建议操作指令
- 模板: `It is recommended to <verb> <object> [prep] <location/condition>.`
- 例句: It is recommended to preheat the PCR thermal cycler to the reaction temperature.

### 目的+建议
- 模板: `To <goal>, it is recommended to <verb> <object>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filter tips and to change the tip when pipetting different samples.

### 禁止性指示
- 模板: `Avoid <gerund> <object> [prep] <location> or Do not <verb> <object>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 限制性规则
- 模板: `The <parameter> should not exceed <value>.`
- 例句: The tissue size should not exceed 0.9 cm × 0.9 cm × 2 cm.

### 应急处理指令
- 模板: `In case of <condition>, <action>.`
- 例句: In case of accident, please immediately rinse with plenty of water and seek medical attention in time.

### 一般声明/前置条件
- 模板: `Unless otherwise specified, <statement>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids used to dilute reagents in this experiment.

## 自动蒸馏新增句式（2026-08-14）

### 操作指令（祈使句）
- 模板: `Please <verb> <object> <time/condition>.`
- 例句: Please read this manual carefully before installation.

### 禁止事项
- 模板: `Do not <verb> <object> <condition>, as this may result in <negative_consequence>.`
- 例句: Do not remove the casing while the equipment is running, as this may result in electric shock.

### 条件触发
- 模板: `If <condition>, please <verb> <action>.`
- 例句: If abnormal noise is detected, please stop using it immediately and contact the after-sales service center.

### 声明与限制
- 模板: `This document serves as <purpose>, aiming to provide <function>.`
- 例句: This document serves as general guidance and reference material, aiming to provide operational instructions and methodology.

### 用途声明
- 模板: `This product is for <usage> only, not for <prohibited_usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 产品属性与功能
- 模板: `This product supports <function_list> functions.`
- 例句: This product supports timed on/off, temperature curve setting, and energy consumption statistics functions.

### 变更记录/更新指令
- 模板: `<Action_verb> <item> to <new_item>.`
- 例句: Mounting changed from glycerol mounting to H&E Mounting Medium.

### 时间相关限制
- 模板: `The <attribute> for this product is <duration> from <starting_point>.`
- 例句: The warranty period for this product is twelve months from the date of purchase.

### 免责与权利声明
- 模板: `Nothing herein is intended to or shall be construed as <guarantee/warranty>.`
- 例句: Nothing herein is intended to or shall be construed as any warranty regarding the performance of any product listed or described herein.

### 操作衔接
- 模板: `Before <event>, please <verb> <action>.`
- 例句: Before first use, please download the accompanying application and complete device pairing.

### 提示与注意事项 (Tip/Note)
- 模板: `<Keyword>: <Description>.`
- 例句: Tip: Additional operating tips and guidance.

### 操作指令 (Action/Instruction)
- 模板: `Please <verb> <object> <condition/location>.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 文档引用 (Reference Instruction)
- 模板: `For <details>, please refer to <Document Name>.`
- 例句: For details, please refer to 'Spatial Transcriptomics FF V1.3 (including compatible mIF) Library Construction Operating Manual'.

### 组件规格定义 (Component Specification)
- 模板: `<Component Name> <Cat. No.> <Tube Cap Color> <Specification> × <Quantity>`
- 例句: RI 1000028499 Orange 300 µL × 1

### 储存条件说明 (Storage/Temperature)
- 模板: `<Storage Type>: <Temperature Range/Condition>`
- 例句: Storage temperature: −25℃~ −15℃

### 适用范围说明 (Suitability/Scope)
- 模板: `This <document/guide> is suitable for <Product Name>.`
- 例句: This operation guide is suitable for the Stereo-seq Transcriptomics Kit V1.3 (Chip)...

### 实验警示 (Critical/Warning)
- 模板: `<Critical Step/Note>: <Description>; <potential consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 产品组成列表 (Package Composition)
- 模板: `<Product Name> *<Quantity> (<Specification>)`
- 例句: Stereo-seq Transcriptomics Kit T *1 (4 RXN)

### 温度说明
- 模板: `<Temperature_Type> temperature: <Range>`
- 例句: Shipping temperature: −25°C to −15°C

### 产品描述
- 模板: `<Volume_Size> <Product_Name>`
- 例句: 50 mL Centrifuge Tube

### 等效替代
- 模板: `(or equivalent <Equipment_Type>)`
- 例句: (or equivalent instrument)

### 选项选择
- 模板: `Select any one from <Selection_Criteria>.`
- 例句: Select any one from the brands with the same superscript.

### 按需使用
- 模板: `<Product_Name> is a <Description>; use as needed.`
- 例句: * F RT Buffer Mix is a specialized reagent for fruit-bearing plants; use as needed.

### 储存及有效期
- 模板: `Storage temperature: <Range>. Expiration date: <Expiration_Instruction>.`
- 例句: Storage temperature: −25°C to −15°C. Expiration date: see label.

### 操作准备
- 模板: `Please <Action> before use.`
- 例句: Please read this manual carefully before use.

### 建议/推荐动作
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to take out all reagent components in advance before use.

### 步骤衔接/流程控制
- 模板: `<action>, then <action>.`
- 例句: After thawing, gently invert several times to mix thoroughly, briefly centrifuge, and place on ice for later use.

### 条件性建议
- 模板: `If <condition>, it is recommended that <action>.`
- 例句: If significant tissue detachment occurs in either step 1) or 2), it is recommended that this sample not proceed to the formal experiment.

### 禁止事项/预防警告
- 模板: `To avoid <risk>, it is recommended to <action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filter pipette tips.

### 试剂配制指令
- 模板: `Add <amount> of <reagent_a> to <amount> of <reagent_b> and mix <method>.`
- 例句: Add 1.5 μL of 25% FB stock solution to 148.5 μL Nuclease-Free Water and mix well.

### 即用型试剂说明
- 模板: `<reagent> must be prepared fresh for use.`
- 例句: 0.01N HCl must be prepared fresh for use.

### 仪器参数设置
- 模板: `Set the <instrument> to <temperature>.`
- 例句: Set the temperature of a metal bath or other equivalent instrument to 37°C in advance.

### 步骤前置要求
- 模板: `Please refer to the <document_name> for <task>.`
- 例句: Please refer to the Stereo-seq Plant Fresh Sample Embedding Guide for sample preparation.

### 存储条件说明
- 模板: `Store at <temperature> for <duration>.`
- 例句: Store at −20°C for one month.

### 强制性合规要求
- 模板: `All <items> shall be disposed of in accordance with <regulations>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### Prohibition
- 模板: `Do not <verb> the <object>`
- 例句: Do not vortex the permeabilization enzyme

### Recommendation
- 模板: `It is recommended to <verb> the <object>`
- 例句: It is recommended to aliquot the prepared 10X permeabilization stock solution

### Storage Instruction
- 模板: `Store on ice for <time>`
- 例句: Store on ice for 1 hr

### Pre-processing Instruction
- 模板: `Remove/Take the <object> from <temperature> in advance`
- 例句: Remove the RT Enzyme mix from -20°C in advance

### Maintenance Instruction
- 模板: `Keep on ice during use`
- 例句: Keep on ice during use

### Volume Specification
- 模板: `The volume for <specification> is <volume>/<unit>`
- 例句: The volume for a 1 cm*1 cm chip is 100 μL/chip

### Tool-based Instruction
- 模板: `<verb> the <object> using <tool>`
- 例句: Carefully dry the chip using a gas cylinder

### Sequential Step Instruction
- 模板: `Repeat step <number>`
- 例句: Repeat step 4)

### Procedural Instruction (Item-based)
- 模板: `<item> (<description>): <verb> <object>, <verb> <object>, ...`
- 例句: PR Enzyme (red cap, powder): Briefly centrifuge, add 1 mL of freshly prepared 0.01N HCl

### Parameter Setting
- 模板: `Set the <parameter> to <value> in advance`
- 例句: Set the temperature of the PCR device to 37°C in advance

### 操作指令式
- 模板: `<verb> <object> (e.g., Place the carrier...)`
- 例句: Place the carrier chip in the cryostat with the front side facing up, and pre-cool for 1-6 min;

### 条件衔接式
- 模板: `If <condition>, please <action>; if <condition>, follow <section>.`
- 例句: If autofluorescence is chosen, please follow the experimental procedures in section 3.5.1, and ignore section 3.5.2;

### 顺序强调式
- 模板: `First, <action_1>, then <action_2>, and <action_3>.`
- 例句: First, add one drop of staining solution to each of the four corners of the chip, and then add the remaining staining solution to the center of the chip

### 预防警告式
- 模板: `Do not <action>, to avoid <negative_outcome>.`
- 例句: The pre-cooling time must not be too long to avoid water condensation on the slide surface;

### 限制条件式
- 模板: `Limit <action> to <time/quantity> (e.g., ...not exceed X min/unit).`
- 例句: fixation time should not exceed 1 hr

### 步骤循环式
- 模板: `Repeat steps <step_x> - <step_y> until <goal>.`
- 例句: Repeat steps 2) - 3) until all tissue sections have adhered to the chip surface;

### 参考指向式
- 模板: `Refer to <section>, <table_name>, to <action>.`
- 例句: Refer to Section 3.7 Tissue Permeabilization, Table 3-2, to prepare 1X permeabilization reagent working solution in advance;

### 注意事项式
- 模板: `Note: When <action>, <instruction>.`
- 例句: Note: When performing cold mounting on multiple chips, the interval time must be controlled to avoid tissue shrinkage.

### 用量规格式
- 模板: `(For <size> chips, the volume is <volume>/chip).`
- 例句: (For 1 cm*1 cm chips, the volume is 150 μL/chip; for 0.5 cm*0.5 cm chips, the volume is 50 μL/chip).

### 负面约束式
- 模板: `<subject> must be <condition>, otherwise <negative_consequence>.`
- 例句: The naming of the image storage path must be in English or Arabic numerals and cannot contain Chinese characters; otherwise, the software cannot recognize it during image QC.

### ActionSequence
- 模板: `Ensure <object> is <status>, <action_1>, <action_2>.`
- 例句: Ensure the entire chip is within the selected range, turn on the episcopic light source, adjust the light intensity.

### TriggerAction
- 模板: `Once <condition>, click '<button_name>'.`
- 例句: Once the required number of points has been selected, click 'End Point Selection'.

### EventAction
- 模板: `After <event>, <action>.`
- 例句: After the scan is complete, click 'Create Slice' again to create a new folder.

### Reference
- 模板: `For <topic>, please refer to <document_name>.`
- 例句: For more specific microscope usage instructions, please refer to the 'Go Optical Spatial Microscope Product Manual'.

### Dosage
- 模板: `Add <reagent>, <volume>/chip.`
- 例句: Add Wash Buffer, 200 μL/chip.

### Constraint
- 模板: `Do not <action> while <condition>.`
- 例句: Do not move the carrier while imaging the same chip across different channels.

### 操作指令 - 准备/配制
- 模板: `Prepare the <reagent_name> in advance according to <table_number>.`
- 例句: Prepare the cDNA Release Mix 5 minutes in advance according to Table 3-4

### 操作指令 - 添加/混合
- 模板: `Add <amount> of <reagent_name> and <verb> to mix.`
- 例句: Add cDNA Release Mix, 400 μL/chip

### 条件句 - 遵循指示
- 模板: `According to <section_reference>, <action>.`
- 例句: According to 3.1 Pre-experimental preparation → Preparation of reagents required for the next day: Take out magnetic beads

### 步骤衔接 - 顺序执行
- 模板: `After the <reaction_name> is complete, <action>.`
- 例句: After the reverse transcription reaction is complete, remove the handheld carrier from the PCR instrument

### 建议/最佳实践 - 磁珠操作
- 模板: `It is recommended to use <product_name> for <process_name>.`
- 例句: It is recommended to use VAHTS DNA Clean Beads or AMPure® XP (Agencourt, Cat. No. A63882) for magnetic bead purification

### 禁止/注意事项 - 避免动作
- 模板: `When <action>, avoid <forbidden_action>.`
- 例句: When aspirating the supernatant after elution, avoid touching the magnetic beads

### 建议 - 条件触发
- 模板: `If <condition>, <action>.`
- 例句: If the recovered sample is less than 42 μL, top up with NF-H2O.

### 状态描述 - 实验过程
- 模板: `Let it stand at <temperature_or_condition> for <time>.`
- 例句: let it stand at room temperature.

### 操作指令 - 离心/静置
- 模板: `Briefly centrifuge, and place on a magnetic rack to <action> until <state>.`
- 例句: After a brief centrifugation, place the centrifuge tube on a magnetic rack and let it stand for 3 min until the solution becomes clear

### 操作指令 - 移液/清洗
- 模板: `Use a pipette to <action> <target>.`
- 例句: use a pipette to aspirate and discard the RT from the chip surface

### 停止点提示
- 模板: `Stop point: <action> can be <verb> at this step, or <subject> can be <verb> <condition>.`
- 例句: Stop point: PCR can be performed overnight at this step, or the products can be stored at 4°C for up to 16 hours.

### 操作指令
- 模板: `Perform <object> on <target>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 顺序步骤衔接
- 模板: `<sequence_marker>. After <action>, <imperative_verb> <object> using a <tool>;`
- 例句: d. After the liquid clarifies, carefully remove the supernatant using a pipette;

### 条件分支
- 模板: `If <subject> is <condition>, <imperative_verb> <action>.`
- 例句: if it is less than 20 ng/μL, it is considered an experiment abnormality.

### 注意事项/提醒
- 模板: `Note: Please first <action>. Proceed with <action> only after <condition>.`
- 例句: Note: Please first follow the installation tutorial for cellbin2 published on GitHub. Proceed with the steps above only after successful installation.

### 混合/配制操作
- 模板: `Mix <object_A> with <object_B> (e.g., if <condition>, add <quantity> of <object>), <verb> to mix, and <verb> <duration>.`
- 例句: PCR product 1 : magnetic beads 0.8 (e.g., if PCR product is 100 μL, add 80 μL of magnetic beads), vortex to mix, and incubate for 10 min;

### 状态确认与保持
- 模板: `Keep <object> on the <tool>, <verb> <duration>, until <condition>.`
- 例句: Keep the centrifuge tube on the magnetic stand and air-dry at room temperature for 2-5 min, until the surface of the magnetic beads is free of reflection and cracking;

### 引用/参考
- 模板: `For <information>, refer to <reference_target>.`
- 例句: For resuspension volume, refer to Table 3-8.

### 实验操作确认
- 模板: `Finally, check the <object> to ensure <condition>.`
- 例句: Finally, check the assembled fixture and chip carrier to ensure they are positioned correctly.

### 章标题
- 模板: `Chapter <num> <title>`
- 例句: Chapter 1 Introduction

### 操作类节标题
- 模板: `<Verbing> <object>`
- 例句: Thawing the Sample Loading Reagent Plate

### 具体操作指令
- 模板: `<verb> <object>`
- 例句: Prepare 0.1 M NaOH reagent

### 组分/设备清单
- 模板: `<Component/Tool> List`
- 例句: Visualization Reagent Kit Components List

### 计算操作指令
- 模板: `Calculate <target_value> for <sample_type>`
- 例句: Calculate the theoretical relative quantity for each sample

### 产品适配说明
- 模板: `Compatible with <action> for <product_name>`
- 例句: Compatible with pooling sequencing for CITE V1.1-cDNA and CITE V1.1-ADT libraries

### 定义性陈述
- 模板: `<Subject> is a <Noun Phrase>`
- 例句: TM is a trademark of Thermo Fisher Scientific Inc. or its subsidiaries.

### Sequencing Condition
- 模板: `When <condition>, the <system/software> <action>.`
- 例句: When sequencing is in progress, the control software automatically calls the basecalling software for analysis.

### Reagent Prohibition
- 模板: `<Component> from different batches must not be mixed.`
- 例句: Reagent components from different batches must not be mixed.

### Usage Restriction
- 模板: `Do not <action> until <state>.`
- 例句: Please keep components in the packaging box until they are used up.

### Usage Declaration
- 模板: `This product is for <purpose> use only.`
- 例句: This product is for scientific research use only.

### Preparatory Instruction
- 模板: `Please <action> before <activity>.`
- 例句: Please read the product manual carefully before use.

### Specification Definition
- 模板: `The <parameter> for <process> is <value>.`
- 例句: The calibration cycle for Read 1 is 1.

### Limitation Caveat
- 模板: `The values in <table_name> are <description> in <mode> only; <qualification>.`
- 例句: The values in table y are theoretical sequencing durations in standard mode only; the actual runtime on different instruments may vary.

### Safety Precaution
- 模板: `<Object> should avoid <action>, and must not be <forbidden_action>.`
- 例句: All samples and reagents should avoid direct contact with skin and eyes, and must not be swallowed.

### Product Description
- 模板: `This product is a <description> for <function>.`
- 例句: This product is a universal kit for sequencing spatial transcriptomic libraries.

### Item Quantity Specification
- 模板: `<Item Name>/<Quantity> <Unit>`
- 例句: Sequencing Reagent Reservoir/1 unit

### Material Specification List
- 模板: `<Item Name>, <Brand>, <Cat. No.>`
- 例句: Qubit 4.0 Fluorometer, Thermo Fisher, Q33226

### Prohibition Statement
- 模板: `The use of <item> is prohibited during <context>; <requirement> must be used.`
- 例句: The use of filter tips is prohibited during DNB preparation and loading; recommended brand catalog numbers must be used.

### Recommendation Statement
- 模板: `For <context>, it is recommended to use <requirement>.`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### Key-Value Metadata
- 模板: `<Key>: <Value>`
- 例句: Cat. No.: 940-001904-00

### Table or Figure Labeling
- 模板: `Table <Number> <Title>`
- 例句: Table 4 User-supplied equipment and materials

### Operation Time Specification
- 模板: `<Action>: <Duration>`
- 例句: Thawing reagents: 0.5 hr

### Conditional Requirement
- 模板: `If <condition>, <requirement> applies.`
- 例句: If the library construction kit manual has special requirements, the fragment size requirements specified in the manual apply.

### 建议句式
- 模板: `It is recommended that <clause>.`
- 例句: It is recommended that the relative content of any base is between 5% and 12.5%.

### 操作指令（简单）
- 模板: `<verb> the <object> on ice for later use.`
- 例句: Take out the library and place it on ice for later use.

### 条件指令
- 模板: `If <condition>, <action>.`
- 例句: If the library preparation kit manual has special requirements, the library requirements in the library preparation kit manual shall prevail.

### 试剂准备声明
- 模板: `The table below shows the <object> for a <volume> <system_name>:`
- 例句: The table below shows the required dsDNA library volume for a 100 μL DNB preparation system:

### 步骤衔接
- 模板: `After <action>, <action>, and <action>.`
- 例句: After the reagent has thawed, vortex for 5 seconds to mix, briefly centrifuge, and place on ice for later use.

### 数值/比例定义
- 模板: `<Variable> represents <definition>.`
- 例句: N represents the average nucleotide count (total library fragment length, including adapter sequence length), and C represents the library concentration.

### 操作注意事项
- 模板: `<Subject> must be <action> by <method>; do not <action>, <action>, or <action>.`
- 例句: DNB must be mixed gently by slow pipetting using wide-bore pipette tips (without filters); do not centrifuge, vortex, or pipette vigorously.

### 确认要求
- 模板: `Confirm the <object> and <object> according to <section_reference>.`
- 例句: Confirm the library volume and the number of preparations according to "Estimating the Required Amount of dsDNA Library".

### 即时操作
- 模板: `After the reaction is completed, immediately <action>.`
- 例句: After the reaction is completed, immediately place the samples on ice.

### 操作建议/推荐
- 模板: `It is recommended to <verb> <object> to <purpose>.`
- 例句: It is recommended to perform quantification in batches to avoid inaccurate DNB concentration quantification.

### 条件判定与要求
- 模板: `If <condition>, <action> is required.`
- 例句: If the DNB concentration is unacceptable, re-preparation is required.

### 引用参考
- 模板: `For operation, see "<document_title>" on page <page_number>.`
- 例句: For operation, see "DNB Quantitative Operation Guide" on page 45.

### 顺序指令
- 模板: `After <action_completed>, <subsequent_action>.`
- 例句: After DNB sampling for all samples is completed, use a wide-bore pipette tip.

### 步骤描述
- 模板: `<verb> <object> before use, then <verb> for <duration>.`
- 例句: Gently invert and mix 5 times before use, then centrifuge for 1 minute.

### 结果描述
- 模板: `The <property> of <object> is: <formula>.`
- 例句: The pooling volume of the H sample is: H2=270*H1/V

### 前提条件/范围
- 模板: `When <condition>, <action>.`
- 例句: When the samples to be pooled are of the same application type or have similar insert fragments, calculate the DNB pooling volume.

### 状态声明
- 模板: `After <state>, <action>.`
- 例句: After fully thawed, place in a 2°C~8°C refrigerator for use.

### 目的/准则
- 模板: `To ensure <goal>, it is recommended that <requirement>.`
- 例句: To ensure base balance for sequencing, it is recommended that the mass ratio... be no less than 1:1.

### 章节标题
- 模板: `<Gerund> <Noun>`
- 例句: Placing Samples

### 强力禁止
- 模板: `It is strictly prohibited to <verb> <object>`
- 例句: It is strictly prohibited to use products beyond their expiration date.

### 适用范围限定
- 模板: `This product is for <purpose> use only`
- 例句: This product is for scientific research use only.

### 表格标题
- 模板: `Table <number> <title>`
- 例句: Table 1 Example of sequencing cycles

### 可选步骤
- 模板: `(optional) <step>`
- 例句: (optional) DNB Tube Cleaning

### 礼貌建议
- 模板: `Please <verb> <object>`
- 例句: Please keep components stored in the packaging boxes until they are fully used.

### 数据声明
- 模板: `The values in the table above are <definition> only`
- 例句: The values in the table above are theoretical sequencing durations only.

### 试剂/耗材规格描述
- 模板: `<Item Name>, <Volume> × <Quantity> <Unit>`
- 例句: Inactivated MDA Reagent, 3.50 mL × 1 vial

### 耗材数量简注
- 模板: `<Item Name> / <Quantity>`
- 例句: Sequencing reagent trough / 1

### 条件触发动作
- 模板: `If <condition>, <imperative action>`
- 例句: If crystals are observed in DNB Loading Buffer 6, vortex continuously and vigorously

### 多项禁止操作
- 模板: `Do not <verb>, <verb>, or <verb>`
- 例句: Do not centrifuge, vortex, or pipette vigorously

### 建议事项
- 模板: `It is recommended to <action>`
- 例句: It is recommended to use the recommended brand catalog numbers

### 操作步骤与环境条件
- 模板: `<Action> at <location/condition> for <duration>`
- 例句: Thaw at room temperature for 0.5 hours

### 即时操作指引
- 模板: `<Action> <object> just before <event>`
- 例句: Open the vacuum-sealed package of the flow cell just before use

### 软件交互指令
- 模板: `Click [<Button Name>] to <action>`
- 例句: Click [Load] to enter the interface shown below

### 严格禁止事项
- 模板: `<Subject/Object> must not be <action>`
- 例句: Filter tips must not be used

### 步骤执行指令
- 模板: `<verb> <item> and add <amount> of <substance> to <location>`
- 例句: Peel off the sealing film from the sample loading reagent plate and add 4 mL of 0.1 M NaOH to well 11

### 放置对象指令
- 模板: `Place the <item> onto the <location>`
- 例句: Place the prepared sample loading reagent plate onto the reagent plate tray of the MGIDL-T7RS

### 对齐操作指令
- 模板: `Align the <item> with the <target>`
- 例句: Align the sequencing slide with the RFID scanning area

### 前置条件检查
- 模板: `Before <action>, ensure that <condition>`
- 例句: Before placing the slide, ensure that none of the four sealing gaskets on the slide platform are missing.

### 推荐操作建议
- 模板: `If <condition>, it is recommended to <action>`
- 例句: If the library concentration is unknown, it is recommended to use the Qubit dsDNA Assay Kit

### 界面状态描述
- 模板: `When the interface appears as shown below, it indicates that <process> is complete`
- 例句: When the interface appears as shown below, it indicates that slide loading is complete

### 图表标题命名
- 模板: `Figure <number> <description>`
- 例句: Figure 6 Sample loading reagent plate well position information and liquid addition operation

### 禁止事项警告
- 模板: `Do not <action> to avoid <consequence>`
- 例句: Do not press on the slide glass to avoid damaging the slide or leaving fingerprints

### 步骤描述（命令式）
- 模板: `<verb> <object> <location/condition>`
- 例句: Remove DNB Polymerase Mix I (OS-V4.0) from the spatiotemporal visualization reagent kit and place it on ice to thaw.

### 离心/混匀操作
- 模板: `Mix by <method> for <duration>, briefly centrifuge, and keep on ice for use.`
- 例句: After thawing, mix by vortexing for 5 seconds, briefly centrifuge, and keep on ice for use.

### 试剂/仪器参数列表
- 模板: `Table <number>: <Title>`
- 例句: Table 12 Reaction conditions for DNB preparation 1

### 根据某物计算某物
- 模板: `According to <reference> on page <number>, calculate the <object> required for each <process>.`
- 例句: According to "Library concentration" on page 6, calculate the volume of dsDNA library required for each DNB preparation.

### 条件判定（禁止项）
- 模板: `Do not <action>, and <warning>.`
- 例句: Do not place the DNB Polymerase Mix II (OS-V4.0) at room temperature, and avoid prolonged contact with the tube wall.

### 根据某种方案选择
- 模板: `You can choose the appropriate <action> based on the situation; <consequence>.`
- 例句: You can choose the appropriate loading method based on the situation; different loading methods require different quantities of DNB reaction systems.

### 处理突发情况/条件分支
- 模板: `If <condition>, <action/result>.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the manual shall prevail.

### 操作指导指引
- 模板: `For specific operations, please refer to page <number>, "<Title>".`
- 例句: For specific operations, please refer to page 40, "Operation Guide for DNB Quantification using Qubit".

### 程序后处理
- 模板: `Immediately place the sample on ice for <duration> after the program reaction is complete.`
- 例句: Immediately place the sample on ice for 2 minutes after the program reaction is complete.

### 试剂储存/使用要求
- 模板: `The prepared <reagent> can be stored at <temperature> and used within <duration>.`
- 例句: The prepared DNB can be stored at 4 °C and used within 48 hours.

### 试剂准备步骤
- 模板: `Take out <reagent>, place it on <location> for <time> until <state>.`
- 例句: Take out the DNB Loading Buffer II, place it on an ice box for approximately 30 minutes until thawed.

### 操作混匀
- 模板: `Use <tool> to <action> for <duration/frequency>.`
- 例句: Use a vortex mixer to continuously oscillate vigorously for about 1~2 minutes.

### 储存备用
- 模板: `Place <reagent> at <location/temperature> for later use.`
- 例句: Place it on an ice box for later use.

### 根据表格配制
- 模板: `Prepare <mixture> according to the table below:`
- 例句: Prepare the DNB loading system 1 according to the table below:

### 禁止操作
- 模板: `Do not <action1>, <action2>, or <action3>.`
- 例句: Do not centrifuge, vortex, or vigorously pipette.

### 文档引用
- 模板: `For the next step, refer to <location>, "<title>".`
- 例句: For the next step, refer to page 22, "Placing the Reagent Cartridge".

### 操作强制约束
- 模板: `<item> must not be <action>.`
- 例句: Sealing film must not be reused.

### 物料需求
- 模板: `Each <unit> requires <volume> of <reagent>.`
- 例句: Each flow cell (FCL) requires 266 μL of DNB loading mix 1.

### 移液操作
- 模板: `Use a <tool> to <action> <target>.`
- 例句: Use a clean 1 mL pipette tip to gently poke a loading well with a diameter of approximately 2 cm.

### 参考引用句式
- 模板: `For <content>, refer to <location>.`
- 例句: For the preparation method, refer to page 38, "Cleaning Preparation".

### 操作指令句式
- 模板: `Use <tool> to <action> <object>.`
- 例句: Use an electronic pipette to transfer 45 mL of 0.1 M NaOH and add it to well 2 through the punch hole.

### 状态检查句式
- 模板: `Check if <condition>; <consequence>.`
- 例句: Check if the water level in the pure water tank is sufficient; insufficient pure water will lead to sequencing failure.

### 步骤衔接句式
- 模板: `After <action_past_participle>, <action>.`
- 例句: After replacing the pure water, pass the pure water tube through the holes in the lid and the tank wall until it reaches the bottom.

### 操作建议/要求句式
- 模板: `<action> <adverb> to prevent <unwanted_result>.`
- 例句: When cleaning the inner walls of the low-temperature reagent module, operate carefully to prevent being scratched by the reagent needles.

### 条件禁止句式
- 模板: `Do not <action>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 确保操作句式
- 模板: `Ensure <condition> after <action>, then <next_action>.`
- 例句: Ensure that sample loading is complete, then rotate the tip counter-clockwise to remove it.

### 执行顺序句式
- 模板: `<action_1>, and finally <action_2>.`
- 例句: Close the low-temperature compartment door and the room-temperature compartment door, and finally close the reagent compartment door.

### 步骤指令-移液操作
- 模板: `Using a <pipette>, follow the volumes in the table below to <verb> <substance> into a <container>.`
- 例句: Using a pipette of the appropriate volume range, follow the volumes in the table below to first add the dNTPs mixture

### 预处理-震荡混匀
- 模板: `Mix the <substance> thoroughly by vortexing for <duration> before adding, and briefly centrifuge before use.`
- 例句: Mix the dNTPs mixture thoroughly by vortexing for 5 seconds before adding, and briefly centrifuge before use.

### 预处理-颠倒混匀
- 模板: `Gently invert the <substance> <count> times to mix before adding.`
- 例句: Gently invert the DNA polymerase mixture II 4-6 times to mix before adding.

### 操作警告-防止溢出
- 模板: `When transferring the <substance>, operate carefully to prevent the <substance> from spilling out of the <container>.`
- 例句: When transferring the mixture, operate carefully to prevent the liquid from spilling out of the reagent tube.

### 界面交互-点击选择
- 模板: `Click the 【<option>】 option on the <interface_name> to enter <next_interface>.`
- 例句: Click the 【Sequencing】 option on the main interface to enter the following interface:

### 用户输入-光标定位
- 模板: `Move the cursor to the entry field next to <field_name> and enter <input_data>.`
- 例句: Move the cursor to the entry field next to [DNB ID] and enter the library name or ID.

### 界面配置-下拉选择
- 模板: `Select the <protocol> from the [<menu_name>] drop-down menu.`
- 例句: Select the spatial transcriptomics sequencing scheme from the [Sequencing Scheme] drop-down menu.

### 条件分支-测序选择
- 模板: `If barcode sequencing is required, select the <protocol_A>; if barcode sequencing is not performed, select the <protocol_B>.`
- 例句: If barcode sequencing is required, select the STO_T_50+100+10 sequencing protocol; if barcode sequencing is not performed, select the STO_T_50+100_noBC sequencing protocol.

### 异常处理-提示操作
- 模板: `If <condition> cannot be automatically identified, you can manually enter it according to the prompts.`
- 例句: If it cannot be automatically identified, you can manually enter it according to the prompts.

### 校验要求-格式合规
- 模板: `Please ensure the <field> format is correct; otherwise, an <error_type> will be prompted, and you will not be able to continue.`
- 例句: Please ensure the manually entered ID format is correct; otherwise, an ID error will be prompted, and you will not be able to continue.

### 防误触-使用禁忌
- 模板: `When using <reagent>, do not touch <target_location> to avoid affecting <function>.`
- 例句: When using MDA Polymerase Mix II, do not touch the inner wall of the tube where the reagent is contained to avoid affecting酶活.

### 条件操作指令
- 模板: `After <condition>, click <element> and <action>.`
- 例句: After confirming the information is correct, click [Start] and select [Yes].

### 图示引用
- 模板: `Figure <number> <title>.`
- 例句: Figure 31 FFPE library sequencing information review interface.

### 可视化指引
- 模板: `As shown in the figure below, <action>.`
- 例句: As shown in the figure below, click [▼] within the red box and select the corresponding tag sequence.

### 表格准备指引
- 模板: `Prepare <item> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### 外部文档引用
- 模板: `Please refer to <guide_name> for details.`
- 例句: Please refer to the DNBSEQ-T7 sequencer software operation guide for details.

### 状态/界面提示
- 模板: `When <process> are finished, the interface shown below will appear.`
- 例句: When the sequencing and cleaning processes are finished, the interface shown below will appear.

### 有效期规格
- 模板: `Shelf life: <duration> at <temperature>.`
- 例句: Shelf life: 1 month at 4 °C.

### 条件触发/禁止操作
- 模板: `<verb> <object> if <condition>.`
- 例句: Skip this step if there is no slide on the MGIDL-T7RS.

### 定期维护/更换建议
- 模板: `<object> should be replaced every <frequency> or after <count> uses.`
- 例句: Cleaning slides should be replaced every month or after 10 uses.

### 状态确认/检查
- 模板: `<verb> if there is <noun> in <location>.`
- 例句: Check if there is sufficient water in the pure water container.

### 结果描述/指示
- 模板: `<verb> <object>, indicating that <state>.`
- 例句: press the suction button to show a green light, indicating that the slide is fully attached.

### 故障排查/建议
- 模板: `If <condition>, please contact technical support.`
- 例句: If the above methods still cannot resolve the abnormal negative pressure, please contact technical support.

### 多步骤衔接
- 模板: `<verb> <object>, <verb> <object>, and then <verb> <object>.`
- 例句: Press the slide suction button, wait for the negative pressure to be released, and then remove the slide from the slide stage.

### 被动义务/强制要求
- 模板: `The instrument must be <verb>ed either <adverb> or <adverb>.`
- 例句: the instrument must be cleaned either automatically or manually.

### 试剂准备与操作
- 模板: `Use <object> filled with <reagent>, place it into the <location>, and close <container>.`
- 例句: Use a T7 cleaning reagent trough filled with cleaning reagent, place it into the room temperature compartment on the side requiring a wash, and close the reagent compartment door.

### 界面交互/逻辑选择
- 模板: `Click <button> on the interface, select <option> in the pop-up dialog box, and <verb> <action>.`
- 例句: Click [Start] on the interface, select [Yes] in the pop-up dialog box to start the DNBSEQ-T7RS manual cleaning.

### 条件触发操作
- 模板: `When <condition> occurs, <action>.`
- 例句: When pumping failure occurs on DL-T7RS and DNBSEQ-T7RS:

### 否定操作指令
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the conical walls of the assay tube.

### 必要条件声明
- 模板: `<subject> must be <verb/adj> <condition>.`
- 例句: Air bubbles must not be generated in the assay tube.

### 步骤衔接（顺序）
- 模板: `Next, <verb> <object>.`
- 例句: Next, add 10 μL of Qubit ssDNA standard #1 and 10 μL of Qubit ssDNA standard #2 to the 2 standard assay tubes, respectively.

### 根据参考执行
- 模板: `Perform <action> according to <reference>.`
- 例句: Please perform manual cleaning and maintenance for both MGIDL-T7RS and DNBSEQ-T7RS.

### 排查/建议
- 模板: `If <condition> still cannot be resolved by <method>, please <action>.`
- 例句: If the pumping abnormality still cannot be resolved by the methods above, please contact technical support.

### 物品/用量说明
- 模板: `<subject> requires <amount> of <reagent>.`
- 例句: Each standard requires 190 μL of Qubit Working solution.

### 操作顺序描述
- 模板: `Hold <object> with one hand and <verb> <object> with the other.`
- 例句: Hold the side of the reagent cartridge with one hand and support the bottom of the reagent box with the other.

### 状态确认
- 模板: `Check that <condition> is within the normal range of <value> before proceeding.`
- 例句: Check that the negative pressure is within the normal range of -80 to -99 kPa before proceeding.

### 交互操作
- 模板: `Place the cursor in the <field> input field, and use <tool> to <action>.`
- 例句: Place the cursor in the [Reagent Slot ID] input field, and use a barcode scanner to scan the barcode on the bottom right of the reagent slot label.

### Sequential Action on UI
- 模板: `Click [<element>] to <action>.`
- 例句: Click [Next].

### Document Reference
- 模板: `For details, please refer to the <document_name>.`
- 例句: For details, please refer to the MGISEQ-2000 & MGISEQ-2000RS Gene Sequencer Software Operation Guide.

### Table-based Instruction
- 模板: `Prepare <object> according to the <table_name> below.`
- 例句: Prepare washing reagents according to the table below:

### Figure/Table Labeling
- 模板: `<Type> <number> <Title>`
- 例句: Figure 26 Slide Information Entry

### Storage Condition
- 模板: `Valid for <duration> when stored at <condition>.`
- 例句: Valid for 1 month when stored at 2–8 °C

### Temporal Condition Execution
- 模板: `After <action>, <subject> will <action>.`
- 例句: After sequencing begins, the control software will generate sequencing results on the D drive.

### Verification Instruction
- 模板: `Review <item> to ensure it is <adjective>.`
- 例句: Review all filled-in information to ensure it is accurate.

### System Notification
- 模板: `The system will prompt: [<message>].`
- 例句: The system will prompt: [Perform maintenance cleanup?].

### 操作步骤（指令）
- 模板: `Place the <object> into the <location> and close the <component>.`
- 例句: Place the cleaning reagent tube 1 into the sample tube holder and close the reagent compartment door.

### 条件执行指令
- 模板: `If <condition>, select [<option>], and the instrument will <action>.`
- 例句: If the following pop-up appears, select [Yes], and the instrument will automatically raise the needle.

### 界面操作指令
- 模板: `Enter the <interface>, click the <control> to the right of [<label>], and select [<option>] to start <task>.`
- 例句: Enter the cleaning interface, click the drop-down list to the right of [Cleaning Type] and select [Routine Cleaning] to start cleaning.

### 排查操作引导
- 模板: `When <condition>, please perform the following operations to <goal>:`
- 例句: When the DNB concentration is lower than 8 ng/μL, please perform the following operations to troubleshoot the issue:

### 图表引用
- 模板: `Figure <number> <description>`
- 例句: Figure 31 Schematic diagram of cleaning reagent trough positions

### 检查项表达
- 模板: `Check if the <item> <state>.`
- 例句: Check if the kit used is expired.

### 方向引导操作
- 模板: `Following the direction indicated on the <cover>, slowly push the prepared <object> into the <location>.`
- 例句: Following the direction indicated on the cleaning reagent trough cover, slowly push the prepared cleaning reagent trough 1 into the reagent compartment bottom.

### 状态描述
- 模板: `Status <Identifier>: <State>`
- 例句: Status A: Paused 20.0℃-91.6ka

### 操作请求
- 模板: `<Object> <State>, please resume <TimeAdverb>.`
- 例句: Side A paused, please resume promptly.

### 异常处理指令
- 模板: `When <Condition>, <Result>, please perform the following operations:`
- 例句: When the negative pressure value is displayed in red, the negative pressure is abnormal. Please perform the following operations:

### 强制性要求
- 模板: `<Object> must be <Action> within <TimeConstraint>.`
- 例句: The working solution must be used within 30 minutes of preparation.

### 联系技术支持
- 模板: `If <Issue> cannot be resolved using the methods above, please contact an engineer.`
- 例句: If the anomaly in negative pressure cannot be resolved using the methods above, please contact an engineer.

### 流程参照
- 模板: `Prepare <Object> according to the <Source> below:`
- 例句: Prepare the standard tubes and sample tubes to be tested according to the table below:

### 操作方法
- 模板: `Use <Tool> to <Action> <Object>.`
- 例句: Use a dampened lint-free paper or lint-free cloth to gently wipe the platform surface

### 顺序动作
- 模板: `After <Action1>, <Action2>.`
- 例句: After resuming sequencing, the reagent needle will automatically descend

### 条件执行
- 模板: `If <Condition>, it can be <Action> at most <Frequency>.`
- 例句: If the reagent kit has thawed (including dNTPs) and cannot be used on time, it can be freeze-thawed at most one more time.

### 参考引用
- 模板: `For <details>, please refer to <document>.`
- 例句: For details, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide".

### 条件警告
- 模板: `If <anomaly> is discovered, you may <action> to <purpose>.`
- 例句: If an abnormal temperature in the cold chain box is discovered, you may request the logistics provider to print the record table.

### 关键步骤提示
- 模板: `Pay special attention to <target> to avoid <failure>.`
- 例句: Pay special attention to these steps to avoid experimental failure or poor outcomes.

### 组分说明
- 模板: `Each <product> consists of the following <number> components:`
- 例句: Each reagent kit consists of the following four components:

### 免责声明
- 模板: `Nothing herein is intended to or should be understood as <disclaimer>.`
- 例句: Nothing herein is intended to or should be understood as any warranty of the performance of any product.

### 接收后操作
- 模板: `After receiving the <item>, please refer to <guide> to <action>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 条件满足说明
- 模板: `When <condition 1> and <condition 2> are all correct, <subject> can <outcome>.`
- 例句: When transportation conditions, storage conditions, and usage methods are all correct, all components can maintain full activity.

### 试剂/器材详情
- 模板: `<Component Name> <Cat. No.> <Color/Property> <Spec>`
- 例句: Blocking Reagent 1000044666 Transparent 60 µL × 1

### 储存条件
- 模板: `Storage temperature: <Temperature>; <Valid period/Condition>: See label`
- 例句: Storage temperature: Room temperature; Validity under room temperature transport: See label

### 品牌任选
- 模板: `Choose one from brands with the same <descriptor>.`
- 例句: Choose one from brands with the same superscript number.

### 器材/仪器描述
- 模板: `<Brand> <Description> <Product/Catalog Number>`
- 例句: Eppendorf Refrigerated Centrifuge 5418R

### 仪器等效声明
- 模板: `<Instrument Name> <Catalog No.> (or equipment with equivalent functionality)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or equipment with equivalent functionality)

### 参考链接与引导
- 模板: `For the <topic>, please refer to this website: <URL>`
- 例句: For the selection of isotype control antibodies, please refer to this website: https://www.biolegend.com/en-us/search-results?PageSize=25&Category=ISO_CTRL&Format=TOTALSEQ_A

### 试剂搭配验证声明
- 模板: `This kit has been validated for use with <Component Name> (<Product Description>): <Example Name>`
- 例句: This kit has been validated for use with TotalSeq™-A primary antibodies (pre-mixed cocktails): TotalSeq™-A Mouse Universal Cocktail, V1.0

### 推荐操作
- 模板: `It is recommended to <action> <time/condition>.`
- 例句: It is recommended to remove all reagent components in advance before use.

### 连续动作
- 模板: `<Action1> the <object>, and <action2> <condition>.`
- 例句: Briefly centrifuge the enzyme components and keep on ice for use.

### 目的状语引导建议
- 模板: `To <goal>, it is recommended to <action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use pipette tips with filters.

### 安全警告
- 模板: `Avoid <action/contact> of <object> with <location>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 用量说明
- 模板: `Usage per <unit> is <amount>.`
- 例句: Usage per chip is 15 μL.

### 稀释与配制
- 模板: `Dilute <object> to <target> with <solvent>.`
- 例句: Dilute 15 μL of 10X permeabilization reagent stock solution to 150 μL with 0.01N HCl.

### 温控与储存
- 模板: `Take out <object> from <temp>, <action>, and store at <temp>.`
- 例句: Take 4% PFA out of -20℃, thaw and mix well, aliquot 2 mL per tube, and store at -20℃.

### 通用条件
- 模板: `Unless otherwise specified, <material> should be used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water should be used for all liquids intended for reagent dilution in this experiment.

### 物体转移指令
- 模板: `Take <object> out of <source_location> and place it in <target_location> to <action> for <duration>.`
- 例句: Take the OCT-embedded tissue block out of the -80°C freezer and place it in the cryostat to equilibrate for 30 min;

### 参考指令
- 模板: `Refer to <reference_location> to <action>.`
- 例句: Refer to Chapter 2 of the "Stereo-seq Chip Carrier and Accessories User Manual" to assemble the gasket and fixture in...

### 顺序衔接指令
- 模板: `After <action_completed>, <action1>, then <action2>.`
- 例句: After cleaning, use an air duster to blow-dry the perimeter and surface of the chip, then use a lint-free wiper to absorb excess liquid on the back and around the slide;

### 预防/禁止指令
- 模板: `Avoid <action> / Please do not <action>.`
- 例句: Avoid contact between the carrier and the front side of the chip.

### 操作建议
- 模板: `It is recommended that <action> be <constraint>.`
- 例句: It is recommended that the mounting of tissue sections be controlled to within 5 min;

### 重复循环指令
- 模板: `Repeat <steps> until <condition>.`
- 例句: Repeat steps 2)-3) until all tissue sections are adhered to the chip surface...

### 执行操作/添加试剂
- 模板: `Add <volume> of <reagent> to <location>, and incubate at <temperature> for <time>.`
- 例句: Add 400 μL of Wash Buffer to the chip and incubate at room temperature for 1 min;

### 移除/吸弃液体
- 模板: `Use a pipette to aspirate and discard <solution> from one corner of the <location>, keeping <tissue/chip> moist.`
- 例句: Use a pipette to aspirate and discard the DAPI working solution from one corner of the chip, while keeping the tissue moist;

### 清洗步骤衔接
- 模板: `Repeat the washing steps <step_range> once.`
- 例句: Repeat washing steps c.-d. once;

### 警告/禁止事项
- 模板: `<item/action> is prohibited; do not <action>.`
- 例句: Spaces and other special characters are prohibited; do not use them in folder names.

### 过程注意事项（条件句）
- 模板: `Ensure <item> does not <state> during the <process> process; if it does, it is prone to <consequence>.`
- 例句: Ensure the chip does not dry out during the liquid exchange process; if the tissue dries, it is prone to producing non-specific signals.

### 引用说明书/表格
- 模板: `Refer to <table/chapter> in <section> to prepare <reagent>.`
- 例句: Refer to Table 2-5 in section 2.6 DAPI Staining to prepare the DAPI working solution.

### 滴加试剂（强调方式）
- 模板: `Add <reagent> dropwise from the <location>, with a volume of <volume> / <unit>.`
- 例句: Add 150 μL/chip of DAPI working solution dropwise from the non-tissue area, and incubate at room temperature for 2 min.

### 状态保持/临时存放
- 模板: `<Action>, and keep <item> <state> for <duration>.`
- 例句: Dilute DAPI 50-fold with 5X SSC, keep on ice for use, and store at 4°C protected from light for 1 day.

### 条件句
- 模板: `If <condition>, <imperative_command>.`
- 例句: If the tissue is not completely removed, add 400 μL of 0.1X SSC, pipette gently up and down to remove the tissue from the chip.

### 操作禁忌
- 模板: `Do not <verb> <object> to <purpose/avoid_result>.`
- 例句: Do not press on the upper parts of the clamp latches when peeling off the plate sealing film to prevent the carrier from loosening.

### 操作方式
- 模板: `<imperative_verb> <object> <adverbial_phrase>.`
- 例句: Mix by pipetting, and centrifuge briefly.

### 步骤衔接/流程指引
- 模板: `Repeat step <step_number> once;`
- 例句: 5) Repeat step 4) once;

### 操作指令（配合磁力架）
- 模板: `Keep the <tube_type> on the magnetic rack, <action>.`
- 例句: 6) Keep the 1.5 mL centrifuge tube on the magnetic rack, air-dry at room temperature for 5-8 min

### 试剂准备与条件设置
- 模板: `Prepare <reagent_name> following <table_reference> in section <section_name>.`
- 例句: a. Prepare cDNA PCR Mix following Table 2-9 in section 2.15. Transcriptome cDNA Amplification

### 补充与调整体积
- 模板: `If the recovered sample above is less than <volume>, bring the volume to <volume> with <reagent_name>.`
- 例句: c. If the recovered sample above is less than 42 μL, bring the volume to 42 μL with Nuclease-Free Water.

### 基本实验操作（混匀与离心）
- 模板: `<action> to mix, <next_action>.`
- 例句: vortex to mix, let stand at room temperature for 5 min, pulse centrifuge,

### 物质转移
- 模板: `Transfer the supernatant (<volume>) to a new <tube_type>;`
- 例句: 8) Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 建议与提示
- 模板: `For subsequent <purpose>, we recommend retaining <volume> of the <product_name>.`
- 例句: For subsequent troubleshooting, we recommend retaining 2 μL of the PCR product.

### 操作注意事项（否定/禁止）
- 模板: `Do not <action> or <action>.`
- 例句: do not pipette up and down or disturb the magnetic beads

### 实验产物处理条件
- 模板: `The <product_name> can be stored at <temperature> for <duration>.`
- 例句: • The purified cDNA product can be stored at −20°C for 1 month.

### 浓度测定
- 模板: `Measure the concentration using the <instrument_name> and record it;`
- 例句: f. Take 1 μL of cDNA sample, measure the concentration using the Qubit dsDNA HS Kit, and record it;

### 配制标题
- 模板: `Preparation of <substance>`
- 例句: Table 2-14 Preparation of Qubit dsDNA Mix

### 操作步骤-简单动作
- 模板: `<verb> the <object> to <destination>`
- 例句: Transfer the ADT amplification PCR product (100 μL) to a new 1.5 mL microcentrifuge tube

### 操作步骤-孵育/静置
- 模板: `Incubate at <condition> for <time>`
- 例句: Incubate at room temperature for 5 min

### 操作步骤-磁力架静置
- 模板: `Place the <tube> on a magnetic stand and let it stand for <time> until the liquid becomes clear`
- 例句: Place the PCR tube on a magnetic stand and let it stand for 5 min until the liquid becomes clear

### 试剂存储建议
- 模板: `<product> can be stored at <temperature> for <duration>`
- 例句: ADT amplification products can be stored at −20°C for 1 month.

### 参考指南
- 模板: `For specific procedures regarding subsequent <task>, please refer to the "<manual_name>".`
- 例句: For specific procedures regarding subsequent library construction, please refer to the "Stereo-seq Library Preparation Instruction Manual".

### 参数说明
- 模板: `The <parameter> is typically <comparative_adjective> than <value>.`
- 例句: The DNA concentration is typically higher than 5 ng/μL.

### 用途限制/声明
- 模板: `This product is for <use> only, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 否定指令（禁止/限制）
- 模板: `Do not <verb> <object> to avoid <consequence>.`
- 例句: Do not attach any edge labels or stickers to the chip carrier to avoid leakage due to poor adhesion.

### 条件句（步骤衔接/判断）
- 模板: `If <condition>, <action>.`
- 例句: If it is difficult to snap together, first check whether the base and the chip carrier are installed correctly.

### 要求与义务（必须执行）
- 模板: `The <noun> must be <verb-past-participle> in a <adjective> environment.`
- 例句: The entire operation must be performed in a clean environment to prevent environmental impurities from contaminating materials.

### 目的/结果描述
- 模板: `<action>, to ensure <purpose>.`
- 例句: Use an air duster to blow away any impurities or debris from the surfaces, to ensure material surfaces are free of visible dust.

### 信息参考/引用
- 模板: `For further information on <topic>, please refer to <reference>.`
- 例句: For further information on the Catalog No. of accessory kit products, please refer to Table 1-1.

### 风险/注意事项提示
- 模板: `Critical Note: <action/observation>, as <reason>.`
- 例句: Critical Note: After snapping it into place, visually confirm that the chip carrier is horizontally parallel to the base.

### 过程动作描述
- 模板: `Align the <part-A> of the <object> with the <part-B> of the <object>, and slowly fit them together.`
- 例句: Align the positioning holes of the gasket with the positioning posts of the upper cover, and slowly fit them together.

### 责任声明（法律相关）
- 模板: `Nothing herein is intended or shall be construed as regarding <disclaimer>.`
- 例句: Nothing herein is intended or shall be construed as regarding any warranty regarding the performance of any product.

### 细致操作指令
- 模板: `Carefully <verb> the <object>.`
- 例句: Carefully remove the chip carrier.

### 条件动作
- 模板: `If <condition>, <imperative action> to <prevent/achieve result>.`
- 例句: If it is necessary to disassemble the carrier, do so after reagent removal to prevent reagent splashing during the disassembly.

### 流程引导
- 模板: `<Context> instructions are as follows: <action>.`
- 例句: Usage instructions are as follows: Place the carrier upside down on the table.

### 推荐建议
- 模板: `It is recommended to <action> and <action>.`
- 例句: It is recommended to purchase the Stereo-seq V3 Cassette Disassembly Tool and use the disassembly tool to operate.

### 注意事项
- 模板: `Precautions: The <process> must be <verb-past-participle> based on <condition> to ensure <goal>.`
- 例句: Precautions: The disassembly method must be adjusted based on the actual situation to ensure that the chip surface is not damaged.

### 复用操作步骤
- 模板: `For reuse, the <object> must be subjected to the following <process>:`
- 例句: For reuse, the cover and base must be subjected to the following cleaning procedures:

### 操作提示标注
- 模板: `<Label>: <Description>.`
- 例句: Tip: Additional operation tips and guidance.

### 组成描述
- 模板: `Each <Item> consists of the following <Quantity> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 指令建议
- 模板: `Please <Action> as soon as possible.`
- 例句: Please store the product under the specified conditions as soon as possible.

### 预防性建议
- 模板: `To avoid <Risk>, the use of <Method> is recommended.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended.

### 说明书引用操作
- 模板: `Please refer to the "<DocumentName>" to <Action>.`
- 例句: After receiving the Stereo-seq chip, please refer to the "Stereo-seq Custom Chip Storage Guidelines" to store the product correctly.

### 安全操作警告
- 模板: `Avoid direct contact of <part> with <item>; do not <action>.`
- 例句: Avoid direct contact of skin and eyes with samples and reagents; do not ingest samples or reagents.

### 法规遵循指令
- 模板: `All <item> shall be <action> in accordance with <regulation>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### 适用范围说明
- 模板: `This <method> is suitable for <target>.`
- 例句: This embedding method is suitable for tissues with dimensions < 2 cm × 3 cm × 0.7 cm.

### 实验条件约束
- 模板: `Under <condition>, ensure that <subject> <action>.`
- 例句: Under laboratory conditions, strictly ensure that fresh samples undergo direct embedding within 30 minutes of excision.

### 参数限制指令
- 模板: `<subject> should not exceed <limit>.`
- 例句: The tissue size should not exceed 0.9 cm × 1.8 cm × 0.7 cm.

### 一般性建议
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to cut 10-20 tissue sections of 10 μm thickness.

### 强制性建议
- 模板: `It is strongly recommended to <action>.`
- 例句: It is strongly recommended to only use tissue samples with RIN ≥ 7 for subsequent experimental procedures.

### 通用实验规则
- 模板: `Unless otherwise specified, <material> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease Free Water is used for all liquids in this experiment to dilute reagents.

### 预处理指令
- 模板: `<action> <object> in advance.`
- 例句: Prepare a foam box of crushed ice in advance.

### 稀释操作
- 模板: `Dilute <amount> of <reagent> to <final_amount> with <diluent>.`
- 例句: Dilute 25 μL of 10X permeabilization reagent stock solution to 250 μL with 0.01N HCl.

### 条件要求
- 模板: `Ensure <parameter> is in the range of <range>; at least <amount>/<unit>.`
- 例句: ensure pH value is in the range of 1.9-2.1; at least 5 mL/sample.

### 建议/提醒
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to set 6 min, 12 min, 18 min, 24 min and a positive control*, totaling 5 groups for testing.

### 温度设置
- 模板: `Pre-cool the <device> to <temperature>.`
- 例句: Pre-cool the cryostat chamber to -20°C.

### 用量表达
- 模板: `volume required is at least <amount>/<unit>.`
- 例句: volume required is at least 300 μL/chip.

### 设备调整
- 模板: `Adjust the <device> temperature to <temperature> in advance.`
- 例句: Adjust the slide dryer temperature to 37°C in advance.

### 清洗步骤
- 模板: `Wash twice with <solution>.`
- 例句: Wash twice with water.

### 液体添加指令
- 模板: `<verb> <volume> of <reagent_name> onto the chip surface;`
- 例句: b. Based on the chip size, add the corresponding volume of Total RNA hybridization Mix from Table 3-4 onto the chip surface

### 废液处理（斜倾与吸取）
- 模板: `Slightly tilt the chip, and use a pipette to aspirate and discard <object> from <location>;`
- 例句: b. Slightly tilt the chip, and use a pipette to aspirate and discard the RT QC Mix from the chip surface;

### 结果引用（表格）
- 模板: `<action_or_noun> (refer to <table_reference> for the volume);`
- 例句: j. Add 0.1X SSC solution (refer to Table 3-9 for volume);

### 特殊处理提示（避光/温度/操作）
- 模板: `<action>, <method_or_condition> (protected from light);`
- 例句: b. Prepare the RT QC Mix according to Table 3-5 and equilibrate to room temperature (protected from light);

### 操作目的说明
- 模板: `<action> to <purpose>.`
- 例句: h. Immediately add the RT QC Mix to avoid RNA degradation.

### 设备使用建议
- 模板: `Use <tool> to <action>.`
- 例句: p. Use a canned air duster (MATIN, M-6318) to completely blow-dry the surface of the chip;

### 重复步骤
- 模板: `Repeat steps <step_list>;`
- 例句: e. Repeat steps c and d;

### 表格标题模板
- 模板: `Table <table_number> <description_of_content> for <subject> of various sizes`
- 例句: Table 3-2 Permeabilization working solution volumes for large chips of various sizes

### 操作指令祈使句
- 模板: `<verb> <object> <complement>`
- 例句: Add 1-2 μL of water to the stage, carefully transfer the chip onto the microscope stage, remove the light shield, and...

### 条件限定句
- 模板: `Under the condition that <condition>, <main clause>.`
- 例句: Under the condition that the tissue has been removed cleanly and while maintaining identical imaging conditions (including brightness and exposure, etc.), ...

### 标准判定句
- 模板: `<criterion_1>, <criterion_2>, and <criterion_3> are the criteria for determining the optimal <process>.`
- 例句: Intact morphology, strongest fluorescence, and absence of diffusion are the criteria for determining the optimal permeabilization time.

### 结果呈现与推论句
- 模板: `As shown in <figure>, at <condition>, the tissue exhibits <observation>, suggesting <conclusion>; therefore, the optimal <parameter> is <value>.`
- 例句: As shown in Figure 2, at a permeabilization time of 6 min, the tissue exhibits uneven brightness within the same cortex, suggesting insufficient permeabilization; therefore, the optimal permeabilization time is 12 min.

### 禁止事项声明
- 模板: `The use of <object> is prohibited.`
- 例句: Folder names should only use letters, numbers, and underscores; the use of special characters such as spaces is prohibited.

### 变更记录描述
- 模板: `Change the <item> from "<old_value>" to "<new_value>"`
- 例句: Change the shipping method from "dry ice shipping" to "cold chain shipping"

### 新增内容说明
- 模板: `Added <section_or_item>.`
- 例句: Added section on Antibody-Derived Tag (ADT) library preparation.

### 特别注意事项提示
- 模板: `<Note_type>: Pay special attention <purpose>.`
- 例句: Critical Step: Pay special attention to these steps to avoid experimental failure or undesirable outcomes.

### Referencing Tables/Sections
- 模板: `For further information regarding <topic>, please refer to <Table/Section>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-2.

### Conditional Request
- 模板: `If <condition> is detected, you may request <action>.`
- 例句: If an abnormal temperature in the cold chain box is detected, you may request the logistics provider to print the real-time temperature monitoring record table.

### Product Usage Scope
- 模板: `The <kit_name> can be used to <action> from <source>.`
- 例句: The STOmics Stereo-seq Library Construction Kit can be used to construct whole-transcriptome 3'-end libraries from spatial-temporal cDNA amplification products.

### Compatibility/Exclusion
- 模板: `This kit does not contain <reagent_list>. If used for <application>, please use in combination with <product_name>.`
- 例句: This kit does not contain reagents such as TME, Stop Buffer, or TMB. If used for library construction of fresh samples, please use in combination with "Stereo-seq Library Construction Kit (4 RXN, Cat. No.: 101KL114)".

### Pre-experiment Recommendation
- 模板: `Before beginning the experiment, please familiarize yourself with <requirements>.`
- 例句: Before beginning the experiment, please familiarize yourself with the precautions and operating methods for all instruments.

### General Usage Disclaimer
- 模板: `This product is intended for <purpose> only and is not for use in <prohibited_use>.`
- 例句: This product is intended for research use only and is not for use in clinical diagnostic procedures.

### Handling Components Recommendation
- 模板: `Before use, it is recommended to <action> the reagent components.`
- 例句: Before use, it is recommended to remove the reagent components in advance, briefly centrifuge the enzyme components and place them on ice.

### Functional Adaptability
- 模板: `The <protocols> provided in this manual are general guidelines; they may be adapted according to <variables>.`
- 例句: The experimental protocols provided in this manual are general guidelines; in actual operation, they may be adapted according to specific experimental designs, sample characteristics, sequencing applications, and devices.

### 条件限制
- 模板: `Unless otherwise specified, <subject> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids for reagent dilution in this experiment.

### 参照流程
- 模板: `Prepare the <name> according to <reference>.`
- 例句: Prepare the fragmentation Mix according to Table 2-1.

### 并列操作
- 模板: `<Action 1>, <Action 2>, then <Action 3>.`
- 例句: Vortex to mix, centrifuge briefly, then place in the PCR instrument.

### 前置处理
- 模板: `Take <object> out at least <time> in advance to <action>.`
- 例句: Take the Stop Buffer out at least 30 minutes in advance to equilibrate to room temperature.

### 检测与记录
- 模板: `Take <amount> of <object>, <action 1> using <tool>, and <action 2>.`
- 例句: Take 1 μL of PCR product, measure the concentration using the Qubit dsDNA HS Kit, and record it.

### 安全警示
- 模板: `Avoid <action> of <object> with <target>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 合规处置
- 模板: `<Subject> should be disposed of in accordance with <reference>.`
- 例句: All samples and all waste materials should be disposed of in accordance with relevant regulations.

### 实验操作指令
- 模板: `<verb> <object> (e.g., add/mix/place/centrifuge/incubate).`
- 例句: Mix the PCR product with magnetic beads.

### 步骤引用与衔接
- 模板: `Repeat step <step_number> once.`
- 例句: Repeat step c once.

### 状态或条件建议
- 模板: `Keep the <object> on/at <condition>.`
- 例句: Keep the tube on the magnetic stand.

### 浓度/结果描述
- 模板: `The <property> is usually <comparator> <value>.`
- 例句: The concentration is usually greater than 10 ng/μL.

### 参考说明书引用
- 模板: `Please refer to the <manual_name> to <action>.`
- 例句: Please refer to the manual for the High-throughput Sequencing Primer Kit to prepare DNBs.

### 注意事项/禁止
- 模板: `Note: <action_to_take>.`
- 例句: Note: Remove the supernatant and retain the pellet.

### 实验步骤详细说明
- 模板: `<action>, <action>, <action>, until <result_condition>.`
- 例句: Open the cap, and air-dry at room temperature for 5-8 min, until the surface is dry.

### 测序兼容性描述
- 模板: `<sequencer_name> will provide sequencing support for <library_name>.`
- 例句: MGI genetic sequencers will provide sequencing support for Stereo-seq libraries.

### 操作一致性要求
- 模板: `Please read the <manual_name> carefully and operate strictly in accordance with the instructions.`
- 例句: Please read the corresponding instruction manual carefully before sequencing and operate strictly in accordance with the content.

### 参考与推荐句式
- 模板: `For <number> samples, refer to the recommended <object> in <reference>.`
- 例句: For different numbers of samples, refer to the recommended Barcode combination schemes in Appendix Table 2.

### 操作步骤衔接句式
- 模板: `Perform in <number> steps: 1. <action 1>; 2. <action 2>.`
- 例句: Perform in two steps: 1. Divide libraries 1-8 into one group, and add PCR Barcode Primer Mix using the aforementioned 8 libraries/lane method.

### 条件性禁令/建议句式
- 模板: `If <condition>, <action/result>.`
- 例句: If different libraries use the same barcode combination, they cannot be sequenced in the same lane.

### 试剂处理操作句式
- 模板: `Before using the <reagent>, centrifuge it to collect the liquid at the bottom of the tube. Gently open the <part>.`
- 例句: Before using the PCR Barcode Primer Mix, centrifuge it to collect the liquid at the bottom of the tube. Gently open the tube cap.

### 混合操作说明句式
- 模板: `Mixing method for <object>: Combine <quantity> to prepare the <product>, then add to the <target>.`
- 例句: Mixing method for different PCR Barcode Primer Mixes: Combine equal volumes to prepare the Mix, then add to the sample.

### 存储/运输条件句式
- 模板: `The <product> is packed in a <packaging> and transported via <method>.`
- 例句: The Stereo-seq chip is packed in a vacuum-sealed aluminum bag and transported via cold chain.

### 检查事项提示句式
- 模板: `Please check the following items after opening the <packaging>:`
- 例句: Please check the following items after opening the aluminum foil bag:

### 下载/访问引导句式
- 模板: `Please visit the following link to view or download: <url>`
- 例句: Please visit the following link to view or download: https://www.stomics.tech/resources/Documents/list

### 责任/反馈句式
- 模板: `If you discover any of the <description> with the product, please promptly report the situation to the <person>.`
- 例句: If you discover any of the above-mentioned issues with the product, please promptly report the situation to the research cooperation representative or technical personnel.

### 产品有效性说明句式
- 模板: `When unopened, the product can be stored at <temperature> until the expiration date on the label.`
- 例句: When unopened, the product can be stored at -20 °C or 4 °C until the expiration date on the label.

### 产品合规性声明
- 模板: `This product is for <usage_purpose> use only and not for <restricted_purpose> purposes.`
- 例句: This product is for research use only and not for diagnostic purposes.

### 操作关键点提示
- 模板: `Key Steps: Pay special attention to these steps to avoid <risk_type> or <undesired_outcome>.`
- 例句: Key Steps: Pay special attention to these steps to avoid experimental failure or poor results.

### 注意事项/预警
- 模板: `Note: Pay special attention; <potential_action> may lead to <undesired_outcome>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experimental failure.

### 流程暂停点说明
- 模板: `Stopping point: You can <action> here and <action_on_sample>.`
- 例句: Stopping point: You can pause the experiment here and store the samples.

### 产品组成描述
- 模板: `Each reagent set consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### 知识产权声明
- 模板: `The contents of this manual may be, in whole or in part, subject to <legal_protection_type>.`
- 例句: The contents of this manual may be, in whole or in part, subject to applicable protection by intellectual property laws.

### 产品兼容性与建议
- 模板: `For details, please refer to <document_name>.`
- 例句: For details, please refer to 《Stereo-seq 建库试剂盒使用说明书》.

### 物流异常处理
- 模板: `If an abnormal temperature is detected in the cold chain box, you may <request_action>.`
- 例句: If an abnormal temperature is detected in the cold chain box, you may request the logistics provider to print the real-time temperature monitoring record on-site.

### 存储与运输指导
- 模板: `Please store the product according to the <specified_conditions> as soon as possible.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### Procedural Instruction (Post-receipt)
- 模板: `After receiving the <product_name>, please refer to the <guide_name> to <action>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### Component Table Header
- 模板: `Component Information <catalog_no_col> <specification_col>`
- 例句: Component Information Catalog No. Specification

### Component Specification Entry
- 模板: `<component_name> - <specification>`
- 例句: Stereo-seq Chip T carrier (1 cm * 1 cm) - 4 EA

### Storage and Validity Information
- 模板: `Storage temperature: <temp_range>; <validity_type> validity: see label`
- 例句: Storage temperature: -25°C to 8°C; Shelf life for cold chain transport: see label

### Equipment Equivalency Note
- 模板: `<equipment_name> <catalog_no> (or equivalent instrument)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or equivalent instrument)

### Optional Ordering Note
- 模板: `<item_name> (must be ordered separately)`
- 例句: Stereo-seq PCR adapter (must be ordered separately)

### Selection Instruction
- 模板: `Select one from the listed brands (marked with *).`
- 例句: Select one from the listed brands (marked with *).

### Imperative Procedural Step
- 模板: `<verb> the <object> from the <source>;`
- 例句: a. Take out the fixture and gasket from the Stereo-seq Slide Accessory Kit;

### Reference Instruction
- 模板: `For requirements regarding <topic>, please refer to <doc_name>.`
- 例句: Regarding microscope requirements, please refer to the 'STOmics® Microscope Evaluation Reference Manual'.

### 目的确认
- 模板: `<Verb> <action> to ensure that the <object> <state>.`
- 例句: Press along both sides of the clamp cassette to ensure that the clamp and the chip are securely assembled together;

### 建议操作
- 模板: `It is recommended to <verb> <object> <time/condition>.`
- 例句: It is recommended to take out the reagent components in advance before use.

### 步骤顺序
- 模板: `First, <verb> the <object> into the <target>; then, <verb> <object>.`
- 例句: First, snap the chip carrier into the 4 lower clips of the fixture.

### 禁止与警示
- 模板: `Avoid <action> <object>; do not <verb> <object>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 用量与处理
- 模板: `Take <quantity> of <object> and add to <quantity> of <object>; usage at least <quantity>/chip.`
- 例句: Take 25 μL RI and add to 475 μL 0.1X SSC; usage at least 500 μL/chip.

### 条件引用
- 模板: `Refer to Figure <number>. <description>.`
- 例句: Refer to Figure 1. RNA RIN value peak plot of mouse brain tissue sections.

### 先决条件
- 模板: `<Verb> the <object> in advance and <verb> <object> to pre-cool for <duration>.`
- 例句: Prepare a foam box with crushed ice in advance and place the OCT on the ice to pre-cool for 10 min;

### 操作指令（动词句首）
- 模板: `<verb> <object> (<prep> <adj> <noun>)`
- 例句: Remove the OCT-embedded tissue block from the -80°C freezer and place it in the cryostat to equilibrate for 30 minutes;

### 步骤/动作顺序衔接
- 模板: `<action1>, then <action2> (<duration/condition>);`
- 例句: Place the carrier on the desktop to equilibrate to room temperature for 1 min, then observe whether there are impurities;

### 条件建议（If/When...）
- 模板: `If <condition>, <action>; (while if <condition2>, <action2>;)`
- 例句: If the specimen head temperature is too low, it will cause cracks in the sections, while if it is too high, it will cause wrinkles.

### 用量与试剂配置
- 模板: `<verb> <amount> <reagent> (<container/condition>)`
- 例句: Add 100 μL/chip of Bluing Buffer (containing 5% RI) to the chip.

### 动作范围/时间控制
- 模板: `<action> (<time/frequency>)`
- 例句: Wash 3 times with 100 μL of Wash Buffer.

### 目标状态描述
- 模板: `When <subject> is free of <impurities>, it is ready for <action>.`
- 例句: When the chip surface is free of impurities, visible marks, any liquid residue, or wavy textures, it is ready for mounting;

### 功能描述
- 模板: `The <part> of the <object> is the <adjective> side, which contains <feature>.`
- 例句: The front side of the chip is the glossy side, which contains probes for mRNA capture.

### 参数建议/灵活性
- 模板: `It is recommended to <action> (<time/condition>).`
- 例句: After applying the H&E Mounting Medium, it is recommended to mount the slide immediately.

### 确保要求
- 模板: `Ensure the <object> is <state/condition>.`
- 例句: Ensure the chip is completely submerged in the solution.

### 条件建议
- 模板: `If <condition>, <action>.`
- 例句: If the tissue removal is not complete, add 400 μL of 0.1X SSC.

### 准备工作
- 模板: `Take out <reagents> in advance and <action>.`
- 例句: Take out RT Reagent, RT Additive, and RT Oligo in advance and thaw them at room temperature.

### 强制禁止
- 模板: `<Item> must only use <requirements>; <action/restriction> is prohibited.`
- 例句: Folder names must only use letters, numbers, and underscores; special characters such as spaces are prohibited.

### 频率/用量表达
- 模板: `Use a pipette to <action> the <liquid> from <location>, <restriction>.`
- 例句: With the inclination angle less than 20°, use a pipette to aspirate the permeabilization reagent from one corner of the reaction well, avoiding contact with the chip surface.

### 立即执行
- 模板: `<Reagent> must be added immediately to <purpose>.`
- 例句: RT Mix must be added immediately to avoid RNA degradation.

### Action Instruction
- 模板: `<Action Verb> <Object> <Optional: Method/Conditions>.`
- 例句: Mix the recovery solution from the previous step (450-490 μL) with the magnetic beads equilibrated to room temperature at a 1:1 ratio.

### Conditional Action
- 模板: `If <Condition> is observed/met, <Action Verb> <Object> <Modifier>.`
- 例句: If white precipitate is observed in the cDNA recovery solution, it can be dissolved at 55°C and purified after return to room temperature.

### Precautionary Warning
- 模板: `When <Action>, avoid/take care not to <Prohibited Action>.`
- 例句: When aspirating the supernatant after elution, avoid disturbing the magnetic beads, as drawing them into the pipette tip might affect subsequent purification reactions.

### Reference-based Instruction
- 模板: `<Action Verb> <Object> according to <Table/Reference>.`
- 例句: Prepare PCR Mix according to Table 3-4, 100 μL in total.

### Requirement Expression
- 模板: `It is required that <Parameter> be at <Value/Condition>.`
- 例句: It is required that the main peak of the fragment distribution be at 1000-1500 bp.

### 操作指令建议
- 模板: `Please <verb> <object> and use it with <object>.`
- 例句: Please download the latest version of the instruction manual and use it with the corresponding version of the kit.

### 条件性操作
- 模板: `If <condition>, the <object> may be <verb> up to <time>.`
- 例句: If tissue removal is incomplete, the removal time may be extended up to 16 h.

### 参数变更说明
- 模板: `The <attribute> of <object> has been changed from <value1> to <value2>.`
- 例句: The incubation time for the permeabilization working solution has been changed from 3 min to 10 min.

### 参考说明
- 模板: `<action>; see <table_reference> for details.`
- 例句: The package volumes of the reagent kit components have been increased; see Table 1-1 for details.

### 步骤状态更新
- 模板: `<procedure> updated.`
- 例句: Fluorescence imaging procedure updated.

### 声明与保证
- 模板: `All <object> are set forth in the <object> accompanying the purchase of such product.`
- 例句: and all warranties are set forth in the applicable sale accompanying the purchase of such product

### 警示说明
- 模板: `Note: Pay special attention; <cause> may cause the experiment to fail.`
- 例句: Note: Pay special attention; improper operation or negligence may cause the experiment to fail.

### 参数标准化
- 模板: `<object> volume standardized to <value>.`
- 例句: PR Rinse Buffer solution (containing 5% RI) volume standardized to 200 μL.

### 祈使句操作指令
- 模板: `<verb> <object> (as required)`
- 例句: Place a desiccant in the aluminum sealed bag to maintain dry conditions.

### 条件建议句
- 模板: `If <condition>, you may <action>.`
- 例句: If an abnormality in the cold chain box temperature is detected, you may request the logistics provider to print the report.

### 参照引用句
- 模板: `Please refer to <document_name> to <action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to properly save the product.

### 状态声明句
- 模板: `When <condition1>, <condition2>, and <condition3> are all correct, <subject> can <action>.`
- 例句: When transportation conditions, storage conditions, and usage methods are all correct, all components can maintain complete activity.

### 选择性操作句
- 模板: `Select one from the listed brands (marked with <symbol>).`
- 例句: Select one from the listed brands (marked with * / marked with †).

### 位置/方向描述句
- 模板: `With the <part> of the <object> facing <direction>, <action>.`
- 例句: With the reverse side of the fixture facing up, insert the gasket into the fixture.

### 步骤衔接句
- 模板: `<action_verb> along <location> to ensure <subject> is <state>.`
- 例句: Press along both sides of the fixture cassette to ensure the fixture is securely assembled with the chip slide.

### 有效期与标签声明
- 模板: `Shelf life for <condition>: see label`
- 例句: Shelf life for transport at room temperature: see label

### 包含/成分说明句
- 模板: `The <package_name> contains <component1> and <component2>.`
- 例句: The Stereo-seq carrier accessory kit contains fixtures for the chip carriers and detachable gaskets.

### 检查确认句
- 模板: `Finally, inspect the <subject> to ensure <state>.`
- 例句: Finally, inspect the assembled fixture and chip carrier to ensure they are correctly positioned.

### 直接操作指令
- 模板: `[Verb] [Object] [Modifier]`
- 例句: Align the chip with the gasket hole to avoid contact between the fixture and gasket with the chip surface;

### 标准建议句式
- 模板: `It is recommended to [Verb] [Object/Action] [Modifier]`
- 例句: It is recommended to use filter tips and to change the tip when pipetting different samples.

### 目的状语引导指令
- 模板: `To [Purpose/Condition], [Verb] [Object] [Modifier]`
- 例句: To avoid sample cross-contamination, it is recommended to use filter tips.

### 否定指令与替代操作
- 模板: `Do not [Verb] [Object]; [Instruction] instead.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting instead.

### 成分配制与稀释
- 模板: `Dilute [Amount] of [Component A] to [Final Volume] with [Component B].`
- 例句: Take 5 mL of 20X SSC and dilute to 20 mL.

### 试剂准备与平衡
- 模板: `[Verb] [Object] [Time/Location Modifier] and equilibrate to [Condition].`
- 例句: Take out Glycerol at least 5 minutes before use and equilibrate to room temperature.

### 顺序引导指令
- 模板: `After [Event/Time], [Verb] [Object] [Modifier].`
- 例句: After freezing for 5 min, remove metal embedding mold B and check if the OCT is completely solidified.

### 步骤执行衔接
- 模板: `<verb> <object>, then <verb> <next_action>.`
- 例句: Trim the tissue block to an appropriate size, then proceed with frozen sectioning.

### 条件式要求
- 模板: `If <condition>, <imperative_verb> <action>.`
- 例句: If the specimen chuck temperature is too low, it will cause cracks in the sections.

### 确保性操作描述
- 模板: `<imperative_verb> <action>, ensuring <condition>.`
- 例句: Add sufficient methanol to a slide box, ensuring enough methanol to submerge all chips.

### 过程完成后的状态检查
- 模板: `Once <condition>, <object> is ready for <action>.`
- 例句: Once the chip surface is free of impurities, it is ready for mounting.

### 禁止性表达
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the chip surface.

### 实验前准备引用
- 模板: `In accordance with [<section_name>], <verb> <object> in advance.`
- 例句: In accordance with [Experimental Preparation], prepare 2 mL of 0.01N HCl in advance.

### 建议/推荐操作
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to complete the tissue section mounting within 5 min.

### 用量规格描述
- 模板: `<verb> <quantity> of <substance> to the <object>.`
- 例句: Add the tissue fluorescent staining solution to the chip at a volume of 100 μL/chip.

### 基于条件的持续操作
- 模板: `Repeat <steps> until <condition>.`
- 例句: Repeat steps 2)-3) until all tissue sections are adsorbed onto the chip surface.

### 条件执行建议
- 模板: `If <condition>, <action>.`
- 例句: If tissue removal is incomplete, add 400 μL of 0.1X SSC.

### 步骤前置指令
- 模板: `<action> <target> in advance to <action> at <condition>.`
- 例句: Take out RT Reagent, RT Additive, and RT Oligo in advance to thaw at room temperature.

### 操作顺序衔接
- 模板: `After <process> is complete, <action> <target> from <location>.`
- 例句: After permeabilization is complete, remove the handheld carrier from the PCR instrument (37°C);

### 用量与工具限定
- 模板: `<action> <amount> of <reagent> from <location>.`
- 例句: Add 150 μL/chip of 1X permeabilization reagent working solution from a corner of the reaction well.

### 确保性检查指令
- 模板: `Ensure <target> is <state>.`
- 例句: Ensure the chip is completely covered by the 1X permeabilization reagent working solution.

### 参考规范指令
- 模板: `Refer to <reference> to <action> <target> in advance.`
- 例句: For this reaction step, refer to Table 3-3 to prepare the cDNA Release Mix in advance.

### 特定状态保持
- 模板: `Keep <target> <state> after <action>.`
- 例句: Keep RT Oligo on ice after thawing.

### 物理操作要求
- 模板: `Tilt <target> at an angle of <condition>, and <action> <target>.`
- 例句: Tilt at an angle of less than 20°, and use a pipette to remove the permeabilization reagent.

### 混合与平衡指令
- 模板: `<action> to mix, and <action> to <state>.`
- 例句: Take out the prepared RT Mix, mix by pipetting, and centrifuge briefly.

### 指令式执行步骤
- 模板: `<verb> <object> to <purpose/location>;`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 条件式建议
- 模板: `If <condition>, <action/recommendation>.`
- 例句: If the recovered sample volume mentioned above is less than 42 μL, top it up with Nuclease-Free Water.

### 标准配置建议
- 模板: `Prepare <item> according to <reference>, for a total of <volume>.`
- 例句: Prepare PCR Mix according to Table 3-4, for a total of 100 μL;

### 物料状态说明
- 模板: `<item> equilibrated to <condition> at a <ratio> ratio`
- 例句: Mix the PCR product (100 μL) with magnetic beads equilibrated to room temperature at a 1:1 ratio

### 特定结果要求
- 模板: `<result> is required to be <range>.`
- 例句: The fragment distribution main peak is required to be between 1000-1500 bp

### 存储与有效期建议
- 模板: `The <item> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA product can be stored at -20°C for one month.

### 参考说明书引导
- 模板: `For specific procedures regarding <topic>, please refer to <manual_name>.`
- 例句: For specific procedures regarding subsequent library construction, please refer to the "Stereo-seq Library Preparation"

### 过程一致性修正
- 模板: `The <parameter> has been uniformly changed to <value>.`
- 例句: The volume of PR Rinse Buffer solution (containing 5% RI) has been uniformly changed to 200 μL.

### Noun Phrase Heading
- 模板: `<Adjective/Noun> <Noun>`
- 例句: Sample Requirements

### Action Heading
- 模板: `<Noun/Action> <Noun>`
- 例句: Tissue Fixation

### Instructional Label
- 模板: `<Label>: <Description>`
- 例句: Note: Improper operation or negligence may lead to experimental failure.

### Product Purpose
- 模板: `The <Product Name> is used for <Purpose>.`
- 例句: The STOmics® Stereo-seq Transcriptomic Reagent Kit (Carrier-based) is used for constructing whole-transcriptome 3' end libraries.

### Specification Label
- 模板: `<Specification Name>: <Value>`
- 例句: Storage temperature: −25℃ ~ −18℃.

### Manual Title
- 模板: `Instruction Manual for <Product Name>`
- 例句: Instruction Manual for Stereo-seq Transcriptome Reagent Kit

### Procedural Instruction
- 模板: `[Verb] [Object] [Modifier].`
- 例句: Prepare a foam box of crushed ice in advance.

### Tool-Assisted Action
- 模板: `Use [Tool] to [Action] [Object] [Modifier].`
- 例句: Use a canned air duster to blow away any surface impurities or debris as much as possible.

### Constraint/Threshold
- 模板: `[Subject] should not exceed [Value].`
- 例句: The tissue size should not exceed 0.45 cm × 0.45 cm × 2 cm.

### Safety/Prohibition
- 模板: `Avoid [Action] [Object].`
- 例句: Avoid direct contact of skin and eyes with samples and reagents.

### State Verification
- 模板: `[Action], ensuring [Condition].`
- 例句: With the reverse side of the fixture facing up, insert the washer into the fixture, ensuring the hole cutouts in the fixture and washer are aligned.

### Mandatory Requirement
- 模板: `[Object] must be [Action].`
- 例句: Desiccant must be placed in the resealed aluminum bag to maintain dry conditions.

### 试剂配制/用量说明
- 模板: `Take <volume> of <reagent> and add it to <volume> of <diluent>`
- 例句: Take 5 μL of Wash Buffer and add it to 95 μL of 0.1X SSC, with a required amount of at least 30 μL/chip

### 准备工作提示
- 模板: `Pre-set/Pre-cool <equipment/object> to <temperature/state>`
- 例句: Pre-set the PCR instrument temperature to 37°C and the lid temperature to 42°C

### 时间/温度约束
- 模板: `Equilibrate to <temperature> for <time>`
- 例句: Take out Glycerol at least 5 minutes before use and equilibrate to room temperature.

### 储存/保鲜指令
- 模板: `Store at <temperature> to avoid <process>`
- 例句: Unused RT Oligo can be aliquoted and stored at −80℃ to avoid repeated freeze-thaw cycles.

### 特殊说明/豁免
- 模板: `Unless otherwise specified, <reagent> is used for <purpose>`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for diluting reagents in this experiment.

### 完成检查
- 模板: `Once <object> is <state>, it is ready for <process>`
- 例句: Once the chip surface is free of impurities, obvious marks, residual liquid, or wavy textures, it is ready for mounting

### 操作指令 - 添加试剂
- 模板: `Add <volume> of <substance> onto the <target> (per <unit>).`
- 例句: Add 30 μL of tissue fluorescence staining solution onto the chip per chip.

### 操作指令 - 移除液体
- 模板: `Tilt the <target> and use a pipette to aspirate and discard the <substance> from one corner of the <target>.`
- 例句: Tilt the carrier and use a pipette to aspirate and discard the Wash Buffer from one corner of the chip.

### 操作指令 - 确保条件
- 模板: `Ensure that there is no residual <substance> on the <target>.`
- 例句: Ensure that there is no residual staining solution on the chip.

### 操作指令 - 避免操作
- 模板: `Avoid <action> when <context>.`
- 例句: Avoid touching the front of the chip when assembling the carrier.

### 步骤衔接 - 重复操作
- 模板: `Repeat steps <start>-<end> until <goal> (control the <parameter> to within <limit>).`
- 例句: Repeat steps 2)-3) until all tissue sections are attached to the chip surface (control the attachment time to within 1 min).

### 建议 - 推荐策略
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to use manual focus to simultaneously obtain clear Track lines and staining images.

### 操作指令 - 预处理
- 模板: `<Action> <substance> in advance, ensuring <condition>.`
- 例句: Equilibrate Glycerol at room temperature for 5 minutes in advance and ensure the chip is completely covered by the tissue fluorescence staining solution.

### 操作流程 - 期间操作
- 模板: `During the <process> period, prepare <volume> of <substance> per <unit>.`
- 例句: During the staining period, prepare 30 μL of Wash Buffer per chip.

### 操作指令 - 转移与放置
- 模板: `Transfer the <target> onto a <surface>. Secure the <target> with one hand while <action> in the other.`
- 例句: Transfer the carrier onto a lint-free wipe. Secure the carrier with one hand while holding an air duster in the other.

### 操作指令 - 对齐与定位
- 模板: `Pick up one side of the <target>, position the <component> facing <direction>, and align it with the <target>.`
- 例句: Pick up one side of the carrier, position the chip side facing down, and align it with the section.

### 试剂添加与反应指令
- 模板: `Add <reagent_name> (<dosage>), then place it on <equipment_location> and incubate for <duration>;`
- 例句: Add TR Buffer (400 μL / chip), then place it on the PCR adapter of the PCR instrument (55℃) and incubate for 10 min;

### 试剂准备与条件句
- 模板: `If <condition> is observed in the <reagent_name>, it can be dissolved at <temperature>, and then <subsequent_action>.`
- 例句: If white precipitate is observed in the buffer, it can be dissolved at 55°C, and then returned to room temperature.

### 操作建议句
- 模板: `For this <reaction_step>, refer to <table_name> to prepare the <mixture_name> in advance.`
- 例句: For this reaction step, refer to Table 3-3 to prepare the cDNA Release Mix in advance.

### 磁珠操作步骤
- 模板: `<action_verb> the <sample_type> with the magnetic beads equilibrated to room temperature at a <ratio> ratio, vortex to mix, and incubate at room temperature for <duration>;`
- 例句: Mix the PCR products (100 μL) with magnetic beads equilibrated to room temperature at a 1:1 ratio, vortex to mix, and incubate at room temperature for 10 min;

### 磁珠清洗操作禁止
- 模板: `The pipette tip should be operated against the tube wall away from the magnetic rack; do not <action_forbidden> the magnetic beads.`
- 例句: The pipette tip should be operated against the tube wall away from the magnetic rack; do not pipette up and down or disturb the magnetic beads.

### 液体澄清静置指令
- 模板: `After brief centrifugation, place the <container_type> on a magnetic stand and let it stand for <duration> until the liquid becomes clear;`
- 例句: After brief centrifugation, place the PCR tube on a magnetic stand and let it stand for 3 minutes until the liquid becomes clear;

### 操作顺序指令
- 模板: `Prepare the <mixture_name> according to <table_name> and <storage_condition>.`
- 例句: Prepare the cDNA Release Mix according to Table 3-3 and keep it at room temperature.

### 补足体积指令
- 模板: `If the volume of the recovered sample is less than <volume>, bring it up to <volume> with <reagent_name>.`
- 例句: If the volume of the recovered sample is less than 42 μL, bring it up to 42 μL with Nuclease-Free Water.

### 干燥磁珠检查标准
- 模板: `Keep the centrifuge tube on the magnetic stand and air-dry at room temperature for <duration>, until <condition_description>;`
- 例句: Keep the centrifuge tube on the magnetic stand and air-dry at room temperature for 5-8 min, until the surface of the magnetic beads shows no reflection or cracking;

### 参考文档句式
- 模板: `For <purpose>, please refer to the "<document name>".`
- 例句: For specific procedures for subsequent library construction, please refer to the "Stereo-seq Library Preparation Kit User Manual".

### 储存条件句式
- 模板: `<item> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### 性能要求句式
- 模板: `The <parameter> is required to be at <range> (as shown in <figure>).`
- 例句: The main peak of the fragment distribution is required to be at 1000–1500 bp (as shown in Figure 2).

### 警示说明句式
- 模板: `<Label>: Pay special attention; <explanation>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 信息查询句式
- 模板: `For further information regarding <topic>, see <table_range>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., see Table 1-1 to Table 1-5.

### 合规申明句式
- 模板: `This product is for research use only, not for diagnostic use.`
- 例句: This product is for research use only, not for diagnostic use.

### 引导建议句式
- 模板: `Please <action1> and use it with <object>.`
- 例句: Please download the latest version of the manual and use it with the corresponding version of the kit.

### Refer to Label
- 模板: `<Category>: see label`
- 例句: Cold chain transportation validity: see label

### Catalog Number
- 模板: `Cat. No.: <ID>`
- 例句: Cat. No.: 1000033700

### Imperative Request
- 模板: `Please <verb> <object> <context>`
- 例句: Please store the product under the specified conditions as soon as possible.

### General Recommendation
- 模板: `It is recommended to <verb> <object> in advance`
- 例句: It is recommended to remove all reagent components in advance before use.

### Safety Warning
- 模板: `Avoid <action> of <items>; do not <action> <items>`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### Disposal Instruction
- 模板: `All <items> should be disposed of in accordance with relevant regulations.`
- 例句: All samples and various wastes should be disposed of in accordance with relevant regulations.

### Outline Statement
- 模板: `This list outlines the <items> required for this experiment.`
- 例句: This list outlines the equipment and materials required for this experiment.

### Usage Scope
- 模板: `This product is for research use only and is not intended for <use_case>.`
- 例句: This product is for research use only and is not intended for clinical diagnostic procedures.

### 试剂配制与添加
- 模板: `Add <volume> of <substance> to <target>.`
- 例句: Add 1 mL of freshly prepared 0.01N HCl.

### 储存与状态保持
- 模板: `Keep at <condition>.`
- 例句: keep on ice.

### 禁止性操作与警告
- 模板: `Do not <action>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 步骤重复说明
- 模板: `Repeat steps <start>-<end> <times>, for a total of <total_count> <action>.`
- 例句: Repeat steps e.-f. once, for a total of 2 washes.

### 基本实验步骤
- 模板: `<Imperative Verb> <object> and <action>.`
- 例句: Remove 4% PFA from -20°C, thaw and mix well.

### 液体吸弃操作
- 模板: `Use a pipette to aspirate <substance> from <location>.`
- 例句: Use a pipette to aspirate the blocking buffer from one corner of the chip, keeping the tissue on the chip moist.

### 仪器参数设定
- 模板: `Set <instrument> <parameter> to <value>.`
- 例句: Set the PCR instrument temperature to 37°C.

### 操作指令（添加试剂）
- 模板: `Add <amount> of <reagent_name> per chip,`
- 例句: Add 200 μL of Wash Buffer per chip and incubate for 1 min at room temperature;

### 操作指令（吸弃试剂）
- 模板: `Use a pipette to aspirate and discard the <reagent_name> from <location>,`
- 例句: use a pipette to aspirate and discard the Wash Buffer from one corner of the chip,

### 操作指令（重复步骤）
- 模板: `Repeat steps <step_range> once;`
- 例句: Repeat steps e.-f. once;

### 孵育条件设置
- 模板: `Incubate for <time> at <temperature>,`
- 例句: incubate for 1 min at room temperature;

### 仪器准备与设置
- 模板: `Set the <instrument_name> temperature to <temp> and the <lid_name> temperature to <lid_temp> in advance,`
- 例句: Set the PCR instrument temperature to 70°C and the heated lid temperature to 75°C in advance,

### 试剂配制指引
- 模板: `Prepare the <solution_name> according to Table <table_number> in <section_reference>,`
- 例句: Prepare the Tissue Removal Reagent Mix according to Table 2-5 in Section 2.9, Tissue Removal,

### 状态保持指令
- 模板: `..., keeping the <target_object> <state>.`
- 例句: use a pipette to aspirate the mock secondary antibody incubation solution from one corner of the chip, keeping the tissue moist;

### 顺序执行/衔接
- 模板: `After <action_name> is complete, <next_action>.`
- 例句: After cross-linking reversal is complete, transfer the handheld carrier to the lab bench,

### 操作用量指令
- 模板: `Add <volume> of <reagent>, <dosage>/chip;`
- 例句: Add 400 μL of 0.1X SSC solution per chip;

### 步骤重复衔接
- 模板: `Repeat steps <step_range>;`
- 例句: Repeat steps k.-l.;

### 文献参考指令
- 模板: `Refer to <reference> to <action>.`
- 例句: Refer to Chapter 3 of the "Stereo-seq Chip Carrier and Accessories Instruction Manual" to disassemble the handheld carrier.

### 用途限制声明
- 模板: `This product is for <intended_use> only, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 参数计算规范
- 模板: `<parameter>: <formula>.`
- 例句: Total RNA input: X (μL) = 2 μg / Total RNA concentration (μg/μL).

### 操作禁止事项
- 模板: `<item/action> is prohibited.`
- 例句: Special characters such as spaces are prohibited.

### 流程或参数变更
- 模板: `<item> <parameter> changed from <original_value> to <new_value>`
- 例句: Methanol pre-cooling time changed from 10-30 min to 5-30 min

### 文档或表格参考
- 模板: `For further information regarding <topic>, please refer to <reference>`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-4

### 提示或注意事项
- 模板: `Note: <instruction_or_warning>`
- 例句: Note: Please download the latest version of the manual and use it with the corresponding version of the kit

### 实验停止点
- 模板: `Stopping point: You may pause the experiment here and <action>`
- 例句: Stopping point: You may pause the experiment here and store the samples

### 收到产品后动作
- 模板: `After receiving the <product>, please refer to the "<document>" to <action>`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to store the product

### 目的导向建议
- 模板: `To <goal>, the use of <item> is recommended.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended, and tips must be changed when pipetting different samples.

### 条件操作步骤
- 模板: `Within <time> of <action>, <verb> <object> ...`
- 例句: Within 30 minutes of removing the fresh tissue, blot the surface liquid with sterile non-woven fabric or dust-free paper...

### 步骤确认
- 模板: `Ensure <condition> by <action>.`
- 例句: Ensure the fixture and chip carrier are securely assembled together by pressing along both sides of the fixture.

### 位置/方向描述
- 模板: `With <part> facing <direction>, <verb> <object> ...`
- 例句: With the back of the fixture facing up, insert the gasket into the fixture, ensuring that the hole cutouts of the fixture and gasket are aligned.

### 强烈建议
- 模板: `It is strongly recommended to <verb> ...`
- 例句: It is strongly recommended to proceed with subsequent experimental operations only for tissue samples with RIN ≥7.

### 禁令与声明
- 模板: `<Subject> must not be used for <purpose>.`
- 例句: This product is intended for scientific research purposes only and must not be used for clinical diagnosis.

### 实验前准备
- 模板: `Before <action>, <verb> <reagent/consumable> ...`
- 例句: Before the experiment, please familiarize yourself with the precautions for the various instruments to be used and master their operation methods.

### 祈使句（操作指令）
- 模板: `<verb> the <object> (with <additional_info>)`
- 例句: Place the pre-cooled metal embedding cassette B (acting as a lid) with its opening facing upward

### 条件衔接句
- 模板: `If <condition>, <action>.`
- 例句: If the tissue block is completely solidified and has turned white and opaque, gently pry the sides of the metal embedding cassette A

### 步骤条件说明
- 模板: `<action>; if not, <alternative_action>.`
- 例句: Check if the bottom of the embedded block is completely covered; if not, place the tissue block on the metal block

### 试剂配制描述
- 模板: `Prepare <reagent_name> by adding <amount> of <reagent_A> to <amount> of <reagent_B>.`
- 例句: Prepare Wash Buffer by adding 5 μL of RI to 95 μL of 0.1X SSC

### 时间/条件限制建议
- 模板: `It is recommended to <action> to avoid <consequence>.`
- 例句: It is recommended to aliquot the prepared 10X Permeabilization Reagent stock solution to avoid repeated freezing and thawing.

### 禁止操作指令
- 模板: `Do not <verb> the <object>; <alternative_action>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting up and down.

### 试剂使用要求
- 模板: `<reagent_name> must be freshly prepared before use.`
- 例句: 0.01N HCl (pH = 2.0) must be freshly prepared before use.

### 结果检查指令
- 模板: `After <action> for <duration>, <action> and check if <result_condition>.`
- 例句: After freezing for 5 minutes, remove the metal embedding mold B and check if the OCT has completely solidified

### 实验条件描述
- 模板: `<temperature> for <process_name> (lid heater <temperature>)`
- 例句: 37°C for slide baking and permeabilization (lid heater 42°C)

### 顺序执行操作
- 模板: `Repeat steps <step_x>-<step_y> until <goal>.`
- 例句: Repeat steps 2) and 3) until all tissue sections are adsorbed onto the chip surface

### 添加试剂
- 模板: `Add <quantity> <unit> of <reagent> to <location>.`
- 例句: Add 150 μL of 1X permeabilization reagent to the chip.

### 孵育操作
- 模板: `Incubate at <temperature> for <duration>.`
- 例句: Incubate at 37°C for 20 min.

### 吸弃溶液
- 模板: `Use a pipette to aspirate <solution> from <location>.`
- 例句: Use a pipette to aspirate the permeabilization reagent from one corner of the chip.

### 按表操作
- 模板: `Prepare <reagent> according to Table <table_number>.`
- 例句: Prepare the Total RNA hybridization Mix according to Table 3-1.

### 异常处理
- 模板: `If <condition> is observed, <action>.`
- 例句: If white precipitation is observed in the buffer, it can be dissolved at 55°C.

### 移动载具
- 模板: `Transfer the <item> to the <location>.`
- 例句: Transfer the handheld carrier to the PCR adapter.

### 禁止限制
- 模板: `<Action/Item> is prohibited.`
- 例句: Special characters such as spaces are prohibited.

### 引用图表/数据说明
- 模板: `As shown in Figure <N>, at <condition>, <subject> exhibited <result>.`
- 例句: As shown in Figure 3, at 3 min of permeabilization, the tissue exhibited uneven brightness within the same cortex.

### 动作指令列表
- 模板: `<Verb> <object>;`
- 例句: Revise kit shipping temperature;

### 监管/限制性声明
- 模板: `This product is for <usage> only, not for <negative usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 操作提示/注意事项
- 模板: `<Hint Type>: <Instruction/Warning>.`
- 例句: Note: Please download the latest version of the user manual and use it with the corresponding version of the reagent kit.

### 组成说明
- 模板: `Each <item> consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### 交叉引用
- 模板: `For details, please refer to 《<Document Title>》.`
- 例句: For details, please refer to 《Stereo-seq 16 Barcode Library Preparation Kit V1.0 User Manual》.

### 关键步骤警示
- 模板: `Pay special attention to <steps> to avoid <consequence>.`
- 例句: Pay special attention to these steps to avoid experimental failure or poor results.

### 参数定义
- 模板: `The input parameters for the <pipeline/process> are:`
- 例句: The input parameters for the SAW analysis pipeline adapted for spatiotemporal transcriptomics FFPE are:

### 推荐/建议
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 试剂准备（配制）
- 模板: `Add <amount> of <reagent_A> to <amount> of <reagent_B>, mix well, and store at <condition>.`
- 例句: Add 12.5 mL 20X SSC to 37.5 mL ddH2O, mix well, store at room temperature for 1 week.

### 条件限制（条件句）
- 模板: `If <condition>, <action>.`
- 例句: If the transfer takes a long time, it is recommended to use a temperature-controlled container for transportation.

### 运输/储存条件标注
- 模板: `<type> temperature: <value>.`
- 例句: Storage temperature: -25°C to -18°C.

### 试剂预处理
- 模板: `Take out <object> from <temperature> in advance, equilibrate to <temperature>, and <verb>.`
- 例句: Take TE Buffer (pH 9.0) out from 4℃ in advance to equilibrate to room temperature (≤ 2 hr at room temperature).

### 警告/禁止
- 模板: `Do not <verb> <object>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 物料订购/信息标注
- 模板: `<product_name> Cat. No.: <number>`
- 例句: STOmics FFPE Accessory Kit Cat. No.: 310AK002

### 安全性说明
- 模板: `Avoid direct contact of samples and reagents with <part_of_body>; in case of accident, <action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents. In case of accident, immediately rinse with plenty of water and seek medical attention promptly.

### Reagent Preparation
- 模板: `Remove the <reagent> from <temp> in advance, thaw <method>, and <action> during use.`
- 例句: Remove the FFPE Dimer from -20°C in advance, thaw on ice, and keep on ice during use.

### Temperature Setting
- 模板: `<temp> for <step_name> (heated lid <temp>).`
- 例句: 55°C for cDNA release (heated lid 60°C).

### Conditional Instruction
- 模板: `If <condition>, <action>.`
- 例句: If an integrated slide flotation/drying workstation is unavailable, a slide flotation water bath combined with a PCR instrument can be used as a substitute.

### Constraint/Prohibition
- 模板: `Avoid <problem> on <location>.`
- 例句: Note that after mounting, air bubbles should be avoided on the surface of the chip section.

### Sequential Step Transition
- 模板: `After <action_a>, <action_b>.`
- 例句: After the tissue section is completely flattened, take out the Stereo-seq chip N carrier, record the chip ID, and take care not to touch the chip surface.

### Dosage Specification
- 模板: `<reagent_name> (<dosage_info>).`
- 例句: 30% ethanol solution (300-400mL), microscope slides.

### 操作步骤指令
- 模板: `<Imperative Verb> <Object> <Prepositional Phrase>`
- 例句: Place the unused Stereo-seq chip into the transparent chip box.

### 问题反馈条件句
- 模板: `If <Subject> <Verb> <Condition>, please <Adverb> report the situation to <Role>.`
- 例句: If you find that the product has the above-mentioned issues, please promptly report the situation to your scientific coo.

### 状态确认句
- 模板: `Verify that <Clause>, then <Imperative Verb> <Object> <Prepositional Phrase>.`
- 例句: Verify that the aluminum bag is intact and properly sealed, then immediately store it at -20°C or 4°C.

### 目的说明句
- 模板: `To <Verb> <Object>, <Subject> <Passive Verb> <Adverb>.`
- 例句: To ensure stability during transport, large chips are adhered securely to the bottom of the transparent chip box.

### 负面限制句
- 模板: `<Subject> must not be <Verb(Past Participle)> <Time/Condition Phrase>.`
- 例句: Non-vacuum-sealed chips must not be placed for more than two weeks.

### 文档定义/标签句
- 模板: `<Category/Label>: <Value>`
- 例句: Reagent Kit Version: V1.0

### 通用声明句
- 模板: `This document is intended solely as <Descriptor>, aimed at providing <Purpose>.`
- 例句: This document is intended solely as general guidance reference material, aimed at providing operational guidelines and methods.
