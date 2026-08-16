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

## 自动蒸馏新增句式（2026-08-15）

### 标准操作建议
- 模板: `Please <action> <object>.`
- 例句: Please clean the lens surface with a soft cloth.

### 禁止操作提示
- 模板: `Do not <action> <object>, as this may result in <consequence>.`
- 例句: Do not remove the casing while the equipment is running, as this may result in electric shock.

### 条件触发指令
- 模板: `If <condition> is detected, please <action> immediately.`
- 例句: If abnormal noise is detected, please stop using it immediately.

### 步骤前置要求
- 模板: `Before <step>, please <action>.`
- 例句: Before installation, please turn off the power.

### 版本更新条目
- 模板: `<Action_Verb> <item> in section <section_id>.`
- 例句: Add an autofluorescence-based chip pre-staining step in section 3.3;

### 文档功能描述
- 模板: `This document serves as <purpose>.`
- 例句: This document serves as general guidance and reference material.

### 产品用途限制
- 模板: `This product is for <permitted_use> only, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 材料/试剂替换
- 模板: `Replace <item_A> with <item_B>.`
- 例句: Replace DEPC-treated water with Nuclease-Free water;

### 免责声明句式
- 模板: `Nothing herein is intended to or shall be construed as <warranty>.`
- 例句: Nothing herein is intended to or shall be construed as any warranty regarding the performance of any product listed or described herein.

### 步骤标题
- 模板: `<number>.<number>. <noun_phrase>`
- 例句: 3.2. Section Preparation

### 注意事项/提示
- 模板: `<Tip/Note/Critical step>: <instruction/explanation>.`
- 例句: Tip: Additional operating tips and guidance.

### 指令/建议
- 模板: `Please <verb> <object> <adverb/prepositional_phrase>.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 条件句
- 模板: `If <condition>, <main_clause>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transportation.

### 表格标题
- 模板: `Table <number>-<number> <noun_phrase>`
- 例句: Table 1-1 Reagent Components of Stereo-seq Transcriptomics Kit T

### 定义/描述
- 模板: `<Subject> <be_verb> <noun_phrase_complement>.`
- 例句: The Stereo-seq Transcriptomics Reagent Kit V1.3 (Substrate Version) consists of the following three parts:

### 引用/参考
- 模板: `For details, please refer to <document_title>.`
- 例句: For details, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide".

### 规格/货号信息
- 模板: `<Component_Name> <Cat_No_Label>: <Catalog_Number>`
- 例句: Stereo-seq Transcriptomics Kit T Cat. No.: 201KT13114

### 状态描述/要求
- 模板: `<Subject> must be <adjective_or_past_participle>.`
- 例句: All reagents provided in this reagent kit have undergone rigorous quality control and functional validation.

### 暂停建议
- 模板: `Stopping point: You can <verb> <object> here and <verb> <object>.`
- 例句: Stopping point: You can pause the experiment here and store the samples.

### 参数设定
- 模板: `<Parameter>: <Value>`
- 例句: Storage temperature: 18°C~25°C

### 货号标识
- 模板: `Cat. No.: <Number>`
- 例句: Cat. No.: 203KA12114

### 选项选择说明
- 模板: `Select any one from <Scope>.`
- 例句: Select any one from the brands with the same superscript.

### 使用前说明
- 模板: `Please <Verb> before <Action>.`
- 例句: Please read this manual carefully before use.

### 自备物料清单表头
- 模板: `Table <Number> User-supplied <Items> List`
- 例句: Table 1-6 User-supplied Instruments List

### 同等设备说明
- 模板: `(or equivalent instrument)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or equivalent instrument)

### 试剂适用及使用说明
- 模板: `<Item> is a specialized reagent for <Type>; use as needed.`
- 例句: * F RT Buffer Mix is a specialized reagent for fruit-bearing plants; use as needed.

### 用途声明
- 模板: `This product is for research use only, not for clinical diagnosis.`
- 例句: This product is for research use only, not for clinical diagnosis.

### 有效期标识
- 模板: `Expiration date: <Value>.`
- 例句: Expiration date: see label.

### 推荐行为
- 模板: `It is recommended to <verb> <object> [before/after <condition>].`
- 例句: It is recommended to take out all reagent components in advance before use.

### 操作指令
- 模板: `<verb> <object> to <purpose> [using <tool>].`
- 例句: Add sufficient methanol to a slide box to ensure that the methanol covers the tissue.

### 禁止预防
- 模板: `Avoid <action/substance> on <body_part>; do not <action> <object>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples and reagents.

### 条件中断建议
- 模板: `If <condition>, [then] <action> is not recommended.`
- 例句: If the tissue detaches, proceeding with the formal experiment is not recommended.

### 试剂配制指令
- 模板: `Add <amount> of <reagent_a> to <amount> of <reagent_b> and mix well.`
- 例句: Add 1 μL of Qubit ssDNA Reagent to 199 μL of 5X SSC and mix well.

### 仪器参数设置
- 模板: `Set the temperature of <instrument> to <value> in advance.`
- 例句: Set the temperature of a metal bath or other equivalent instrument to 37°C in advance.

### 试剂稳定性限制
- 模板: `<reagent> must be prepared fresh for use [or: used within <time_frame>].`
- 例句: 0.01N HCl must be prepared fresh for use.

### 质量控制确认
- 模板: `Confirm whether the <object> meet the requirements for <purpose>.`
- 例句: Confirm whether the images meet the requirements for subsequent analysis.

### 操作指令 (Simple Command)
- 模板: `<Verb> <Object> (e.g., for <Duration>)`
- 例句: Briefly centrifuge

### 预处理指令 (Pre-treatment)
- 模板: `Remove <Object> from <Temperature> in advance, <Verb> on ice, and <Verb> during use.`
- 例句: Remove the RT Oligo from -20°C in advance, place it on ice, and keep it on ice during use.

### 配制与稀释 (Preparation and Dilution)
- 模板: `Dilute <Volume> of <SourceReagent> with <Solvent> to <Volume>.`
- 例句: Dilute 15 μL of the 10X permeabilization stock solution with 0.01N HCl to 150 μL

### 建议句式 (Recommendation)
- 模板: `It is recommended to <Verb> <Object>.`
- 例句: It is recommended to aliquot the prepared 10X permeabilization stock solution

### 禁止句式 (Prohibition)
- 模板: `Do not <Verb> <Object>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 条件操作 (Conditional Instruction)
- 模板: `If <Condition>, <Verb> <Object>.`
- 例句: If there is debris on the chip, wash twice with 100 μL of Nuclease-Free Water.

### 放置与环境控制 (Placement and Environment)
- 模板: `Place <Object> on <Location> to <Verb>.`
- 例句: Place the slide on the workbench to warm up for 1 min.

### 步骤流程衔接 (Sequential Procedure)
- 模板: `First, <Verb> <Object>; then, <Verb> <Object>.`
- 例句: First, set the microtome parameters to a section thickness of 40 μm; then slowly shake the microtome handwheel.

### 祈使句操作指令
- 模板: `<verb> <object> (<prepositional_phrase>).`
- 例句: Place the carrier chip in the cryostat with the front side facing up, and pre-cool for 1-6 min;

### 步骤衔接（循环）
- 模板: `Repeat steps <step_start> - <step_end> until <condition_achieved>.`
- 例句: Repeat steps 2) - 3) until all tissue sections have adhered to the chip surface;

### 条件触发
- 模板: `If <condition>, please <action>.`
- 例句: If autofluorescence is chosen, please follow the experimental procedures in section 3.5.1, and ignore section 3.5.2;

### 禁止性警告
- 模板: `<subject> must not be <adjective> to avoid <negative_outcome>.`
- 例句: The pre-cooling time must not be too long to avoid water condensation on the slide surface;

### 负面限制
- 模板: `<action> should not exceed <duration/limit>.`
- 例句: fixation time should not exceed 1 hr

### 用量表达
- 模板: `The dosage for a <dimension> chip is <volume>.`
- 例句: the dosage for a 1 cm*1 cm chip is 5 μL/chip

### 动作目的说明
- 模板: `This step is to <purpose>.`
- 例句: This step is to reduce impurities introduced by the coverslip during subsequent imaging;

### 确保性检查
- 模板: `Ensure <state>.`
- 例句: ensuring that no methanol residues

### 参考引用
- 模板: `Refer to <section>, <table_name>, to <action>.`
- 例句: Refer to Section 3.7 Tissue Permeabilization, Table 3-2, to prepare 1X permeabilization reagent working solution in advance;

### 注意事项/提醒
- 模板: `Note: <instruction>.`
- 例句: Note: When performing cold mounting on multiple chips, it is necessary to control the mounting time for each section;

### 操作指令（祈使句）
- 模板: `<verb> <object> (as/using/to...)`
- 例句: Add 150 μL/slide of 1X Permeabilization Reagent working solution onto the adapter.

### 条件衔接
- 模板: `Once <condition>, <action>`
- 例句: Once the required number of points has been selected, click “End Point Selection”, at which point the “Start Scan” button lights up.

### 建议/推荐
- 模板: `It is recommended to <action>, otherwise <consequence>.`
- 例句: It is recommended to set the initial image save path on the local computer to improve upload speed; the save path must be named in English, otherwise it will affect subsequent QC.

### 负面约束（禁止）
- 模板: `Do not <action>.`
- 例句: Do not move the carrier while imaging the same chip across different channels.

### 步骤衔接（处理完成后）
- 模板: `After <process> is complete, <action>.`
- 例句: After the scan is complete, click "Create Slice" again to create a new folder.

### 参考说明/引用
- 模板: `For <information>, please refer to <document title>.`
- 例句: For more specific microscope usage instructions, please refer to the "Go Optical Spatial Microscope Product Manual".

### 数值/参数调整
- 模板: `Adjust <parameter> (to <value>/<condition>).`
- 例句: Adjust parameters such as exposure (take care not to overexpose) and gain (set to maximum first, then adjust appropriately).

### 条件选择
- 模板: `Select <option A> or <option B> (according to <reference>).`
- 例句: Take out RT Buffer Mix or F RT Buffer Mix in advance (select the specific reagent according to Section 3.8).

### Procedural Addition
- 模板: `Add <reagent>, <volume>/<unit>`
- 例句: Add cDNA Release Mix, 400 μL/chip

### Preparation Instruction
- 模板: `Prepare <item> in advance according to <table_reference> and <action>`
- 例句: Prepare the cDNA Release Mix 5 minutes in advance according to Table 3-4 and let it stand at room temperature.

### Sequential Workflow Action
- 模板: `After <condition>, <action_1>, <action_2>`
- 例句: After the reverse transcription reaction is complete, remove the handheld carrier from the PCR instrument

### Prohibition
- 模板: `Do not <action_1> or <action_2> the <target>`
- 例句: Do not pipette up and down or agitate the magnetic beads

### Recommendation
- 模板: `It is recommended to <action>`
- 例句: It is recommended to use VAHTS DNA Clean Beads or AMPure® XP for magnetic bead purification

### Table Reference
- 模板: `Table <table_number> <title> Preparation`
- 例句: Table 3-4 cDNA Release Mix Preparation

### Condition Check
- 模板: `If <condition>, <action>`
- 例句: If reacting overnight, ensure the plate sealing film is tight

### Pipetting Action
- 模板: `Use a pipette to <action_1> and <action_2>`
- 例句: Use a pipette to aspirate and discard the RT from one corner of the chip

### 停止点提示
- 模板: `Stop point: <action> can be performed <condition>, or the products can be stored at <temperature> for <duration>.`
- 例句: Stop point: PCR can be performed overnight at this step, or the products can be stored at 4°C for up to 16 hours.

### 执行操作指令
- 模板: `Perform <action> on <target>:`
- 例句: Perform 0.8X magnetic bead purification on PCR amplification products:

### 混合孵育指令
- 模板: `Vortex to mix, and incubate for <duration> at <condition>.`
- 例句: Vortex to mix, and incubate for 10 min at room temperature.

### 离心管操作
- 模板: `Keep the <container> on the <equipment>, add <volume> <reagent>, and <action_verb> the <container>.`
- 例句: Keep the centrifuge tube on the magnetic rack, add 200 μL 80% ethanol, and rotate the centrifuge tube.

### 文档引用提示
- 模板: `For detailed procedures regarding <topic>, please refer to the <document_name>.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the Spatial Transcriptomics FF V1.3 (含兼容mlF) 建库实验操作说明书.

### 重复步骤指令
- 模板: `Repeat steps <step_range> once;`
- 例句: Repeat steps e-f once;

### 异常条件判断
- 模板: `The <subject> concentration is typically <threshold>; if it is <condition>, it is considered <status>.`
- 例句: The cDNA PCR product concentration is typically higher than 20 ng/μL; if it is less than 20 ng/μL, it is considered an experiment abnormality.

### 章节/标题命名
- 模板: `<Chapter_Number> <Noun_Phrase>`
- 例句: 1.1 Intended Use

### 步骤标题-动名词式
- 模板: `<Gerund_Verb> the <Object>`
- 例句: Thawing the Sample Loading Reagent Plate

### 步骤标题-祈使句式
- 模板: `<Imperative_Verb> <Object>`
- 例句: Start Sequencing

### 计算/处理操作指令
- 模板: `Calculate the <Description_of_Object>`
- 例句: Calculate the theoretical relative quantity for each sample

### 兼容性说明
- 模板: `Compatible with <Object>`
- 例句: Compatible with FF V1.3 library sequencing

### 版权/商标声明
- 模板: `<Subject> is a trademark of <Company>.`
- 例句: TM is a trademark of Thermo Fisher Scientific Inc. or its subsidiaries.

### 操作名词化
- 模板: `Calculation of <Object>`
- 例句: Calculation of pooling volume for each sample

### 否定/禁止指令
- 模板: `<subject> must not be <verb/action>`
- 例句: Reagent components from different batches must not be mixed.

### 适用/适用范围声明
- 模板: `This product is <intended_use/application>.`
- 例句: This product is for scientific research use only.

### 设备/试剂配合使用
- 模板: `It is used in conjunction with <instrument/product>.`
- 例句: It is used in conjunction with the gene sequencer (DNBSEQ-T7RS).

### 操作流程衔接
- 模板: `When <action> is in progress, <subject> automatically <verb> <object>.`
- 例句: When sequencing is in progress, the control software automatically calls the basecalling software for analysis.

### 注意事项/建议
- 模板: `Please <verb> <object> carefully before <action>.`
- 例句: Please read the product manual carefully before use.

### 异常描述
- 模板: `<Noun> <Abnormality_Type>`
- 例句: Negative Pressure Abnormality

### 组分/规格描述
- 模板: `<Component_Name>, <Volume>/<Unit> × <Quantity> <Unit>`
- 例句: TE buffer, 480 μL/tube × 1 tube

### 自动生成说明
- 模板: `<subject> are automatically generated by the system according to <parameter>.`
- 例句: they are automatically generated by the system according to the sequencing read length.

### 意图声明
- 模板: `This page is intentionally left blank.`
- 例句: - - - This page is intentionally left blank - - -

### 物料规格描述
- 模板: `<Item Name>, <Quantity>/<Unit> × <Count> <Unit>`
- 例句: MDA Polymerase Mix II, 0.60 mL/vial × 1 vial

### 货号/编号描述
- 模板: `<Label>: <Value>`
- 例句: Cat. No.: 940-001904-00

### 禁止性指令
- 模板: `The use of <Item> is prohibited during <Process>; <Requirement> must be used.`
- 例句: The use of filter tips is prohibited during DNB preparation and loading; recommended brand catalog numbers must be used.

### 建议性指令
- 模板: `For <Item>, it is recommended to use <Recommendation>.`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### 手册标题
- 模板: `<Product Name> <Document Type>`
- 例句: Stereo-seq Transcriptomics Set (Cassette version, H&E compatible) User Manual

### 联系方式
- 模板: `<Contact Type>: <Value>`
- 例句: Tel: 4000-688-114

### 条件说明
- 模板: `If the <Document> has special requirements, then <Requirement> specified in the manual shall prevail.`
- 例句: If the library construction kit manual has special requirements, then the fragment size requirements specified in the manual shall prevail.

### 条件判断
- 模板: `If <condition>, <result/requirement> shall prevail.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the kit manual shall prevail.

### 动作衔接
- 模板: `<Verb> for <duration> to <purpose>, briefly <verb>, and <verb> <location> for later use.`
- 例句: Vortex for 5 seconds to mix, briefly centrifuge, and place on ice for later use.

### 禁止事项
- 模板: `Do not <verb> <object> <location/condition>; do not <verb> <object> for <duration>.`
- 例句: Do not place the DNB Polymerase Mix II at room temperature; do not hold the tube wall for an extended period.

### 变量定义
- 模板: `<Variable> represents the <definition> (<unit>).`
- 例句: C1 represents the FFPE library concentration (ng/μL).

### 限制条件
- 模板: `If <condition>, it is not recommended for <action>, and <solution> needs to be <verb>.`
- 例句: If it is lower than 5%, it is not recommended for sequencing, and the pooling scheme needs to be re-planned.

### 表格引用
- 模板: `The table below shows the <required item> for <context>:`
- 例句: The table below shows the required dsDNA library volume for a 100 μL DNB preparation system:

### 时间触发
- 模板: `Once <condition>, immediately <verb> <object> using <tool>.`
- 例句: Once the PCR instrument temperature reaches 4 °C, immediately add 20 μL of DNB termination buffer, using a wide-bore pipette tip.

### 建议句式
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to perform quantification in batches to avoid inaccurate DNB concentration quantification.

### 步骤衔接
- 模板: `After <action_completed>, <subsequent_action>.`
- 例句: After DNB preparation is complete, take 2 μL of DNB.

### 引用/导航
- 模板: `For <action>, see "<guide_title>" on page <number>.`
- 例句: For operation, see "DNB Quantitative Operation Guide" on page 45.

### 禁止/限制
- 模板: `Do not <action>.`
- 例句: Any individual or organization shall not reprint, copy, modify, disseminate or publish this product manual in whole or in part without the written permission of MGI.

### 保证/责任声明
- 模板: `<Company> makes no warranties of any kind regarding <subject>, including, but not limited to, <type_of_warranty>.`
- 例句: MGI makes no warranties of any kind regarding this product manual, including, but not limited to, implied warranties of merchantability and fitness for a particular purpose.

### 版本修订
- 模板: `<Version_Number> <Date>: <Description>`
- 例句: 4.0 June 16, 2025: Adapted for CITE V1.1-ADT library sequencing

### 时间/温度处理
- 模板: `<Method> thawing: Place in <environment> to thaw for <duration>.`
- 例句: Room temperature thawing: Place in a room temperature water bath to thaw for 1.5 hours.

### 操作流程标题
- 模板: `<Number> <Gerund> <Noun>`
- 例句: 8.2 Placing Samples

### 规格描述
- 模板: `<Volume/Size> × <Quantity> <Unit>`
- 例句: 160 μL × 1 vial

### 禁止性规定
- 模板: `<Subject> must not be <Verb>.`
- 例句: Reagent components from different batches must not be mixed.

### 操作前要求
- 模板: `Before <Action>, please <Imperative Verb>.`
- 例句: Before the experiment, please familiarize yourself with and master the operating methods and precautions for all instruments.

### 产品功能定义
- 模板: `This product is <Noun Phrase> used for <Action/Purpose>.`
- 例句: This product is a universal kit used for determining spatial library sequences.

### 流程状态描述
- 模板: `During <Process>, <Subject> automatically <Verb>.`
- 例句: During sequencing, the control software automatically invokes the basecalling software for analysis.

### 图表标题
- 模板: `Table <Number> <Title/Description>`
- 例句: Table 1 Example of sequencing cycles

### 试剂组件量化表达
- 模板: `<Component>, <Quantity> × <Unit>`
- 例句: Inactivated MDA Reagent, 3.50 mL × 1 vial

### 禁止操作指令
- 模板: `Do not <Verb>, <Verb>, or <Verb> <AdverbialPhrase>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 条件触发处理流程
- 模板: `If <Condition>, <Verb> <AdverbialPhrase> until <Result>, then <Verb> before use.`
- 例句: If crystals are observed in DNB Loading Buffer 6, vortex continuously and vigorously for 1-2 minutes until the precipitate is completely dissolved, then centrifuge briefly before use.

### 文档引用与导航
- 模板: `For <Subject>, see "<Section>" on page <Number>.`
- 例句: For the preparation method of 0.1 M NaOH, see "Cleanup Preparation" on page 38.

### 建议与推荐
- 模板: `It is recommended to <Verb> <Object>.`
- 例句: It is recommended to use the recommended brand catalog numbers.

### 制备强制要求
- 模板: `The <Object> must be <Verb> fresh before use.`
- 例句: The DNB loading mixture must be prepared fresh before use.

### 动作序列衔接
- 模板: `<Verb> <Object> just before use, and <Verb> <Object>.`
- 例句: Open the vacuum-sealed package of the flow cell just before use, and start DNB loading.

### 表格标题指引
- 模板: `Table <Number> <Title>`
- 例句: Table 15 DNB loading system

### 强约束条件声明
- 模板: `<Object> must not be <Verb>; you must <Verb> the <Constraint>.`
- 例句: For DNB preparation and loading, filter tips must not be used; you must use the recommended brand catalog numbers.

### 操作指令步骤
- 模板: `[Verb] [Object] from [Source] and add [Amount] [Item] to [Location]`
- 例句: Peel off the sealing film from the sample loading reagent plate and add 4 mL of 0.1 M NaOH to well 11

### 放置指令
- 模板: `Place [Object] onto [Location]`
- 例句: Place the prepared sample loading reagent plate onto the reagent plate tray of the MGIDL-T7RS

### 条件执行指令
- 模板: `If [Condition], you can [Action] according to the prompts.`
- 例句: If it is not displayed, you can manually enter it according to the prompts.

### 界面状态结果描述
- 模板: `When the interface appears as shown below, it indicates that [Status/Result].`
- 例句: When the interface appears as shown below, it indicates that slide loading is complete.

### 负面操作警告
- 模板: `Do not [Action] to avoid [Result].`
- 例句: Do not press on the slide glass to avoid damaging the slide or leaving fingerprints and impurities on the slide surface.

### 操作前置条件
- 模板: `Before [Action], ensure [Condition].`
- 例句: Before placing the slide, ensure that none of the four sealing gaskets on the slide platform are missing.

### 界面点击交互
- 模板: `Click [Button], and select [Option].`
- 例句: Click [Start], and select [Yes].

### 建议事项
- 模板: `It is recommended to [Action] to [Purpose].`
- 例句: It is recommended to store the loaded slide in a resealable bag to prevent the edges from drying out.

### 试剂/耗材取出与准备
- 模板: `Remove <reagent_name> from <source> and place it on ice to thaw/for use.`
- 例句: Remove DNB Polymerase Mix I (OS-V4.0) from the spatiotemporal visualization reagent kit and place it on ice to thaw.

### 基础操作步骤
- 模板: `Mix by vortexing for <time> seconds, briefly centrifuge, and keep on ice for use.`
- 例句: After thawing, mix by vortexing for 5 seconds, briefly centrifuge, and keep on ice for use.

### 条件性建议
- 模板: `If <condition>, <action>.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the manual shall prevail.

### 添加组分
- 模板: `Add the following components on ice: <list_of_components>.`
- 例句: After cooling the sample tube and centrifuging for 5 seconds in a mini-centrifuge, add the following components on ice:

### PCR反应后处理
- 模板: `Immediately place the sample on ice for <time> minutes after the program reaction is complete.`
- 例句: Immediately place the sample on ice for 2 minutes after the program reaction is complete.

### 混匀操作规范
- 模板: `Mix using <tool_name> (without filter); do not <prohibited_action_1>, <prohibited_action_2>, or <prohibited_action_3>.`
- 例句: DNB must be mixed using wide-bore pipette tips (without filter); do not centrifuge, vortex, or pipette vigorously.

### 定量/检测指令
- 模板: `After <action_completed>, take <volume> of <sample> and use <kit_name> to determine the concentration.`
- 例句: After the DNB preparation is complete, take 2 μL of DNB and use the Qubit ssDNA Assay Kit and Qubit 4.0 Fluorometer to determine the concentration.

### 存储建议
- 模板: `The prepared <item> can be stored at <temperature> and used within <time_frame>.`
- 例句: The prepared DNB can be stored at 4 °C and used within 48 hours.

### 耗材状态检查
- 模板: `Take out the <item> and check if it is intact.`
- 例句: Take out the slide and check if it is intact.

### Procedural Step (Imperative)
- 模板: `<Action verb> the <object>, <action verb> it <location/duration> <condition/state>, then <final action>.`
- 例句: Take out the DNB Loading Buffer II, place it on an ice box for approximately 30 minutes until thawed, then use a vortex mixer to oscillate.

### Conditional Action
- 模板: `If <condition>, <imperative action>.`
- 例句: If crystals are found in DNB Loading Buffer II, use a vortex mixer to continuously oscillate vigorously for about 1~2 minutes.

### Post-process Storage/Preparation
- 模板: `After <event/process>, <imperative action> for later use.`
- 例句: After complete thawing, store in a 2 °C-8 °C refrigerator for later use.

### Prohibitions (Negative Imperative)
- 模板: `Do not <verb>, <verb>, or <verb>.`
- 例句: Do not centrifuge, vortex, or vigorously pipette.

### Documentation Reference
- 模板: `For <purpose>, please refer to <document/location>.`
- 例句: For detailed DNB loading operations, please refer to the MGIDL-200H Portable Pipettor Quick Operation Guide.

### Requirement (Strict)
- 模板: `The <object> must be <verb (past participle)> <timing/condition>.`
- 例句: The DNB loading mix must be prepared immediately before use.

### Quantity Requirement
- 模板: `Each <item> requires <quantity> of <substance>.`
- 例句: Each flow cell (FCL) requires 266 μL of DNB loading mix 1.

### Component Loading Instruction
- 模板: `Add <substance> into <target location> according to <reference/volumes>.`
- 例句: Use a pipette of the appropriate range to add dNTPs Mix II and DNA Polymerase Mix II according to the volumes in the table into well 10.

### 引用/跳转
- 模板: `For the <Topic>, refer to <Location>, "<SectionName>".`
- 例句: For the preparation method, refer to page 38, "Cleaning Preparation".

### 条件警告
- 模板: `Check if the <Metric> is <Status>; insufficient <Metric> will lead to <Consequence>.`
- 例句: Check if the water level in the pure water tank is sufficient; insufficient pure water will lead to sequencing failure.

### 禁止操作
- 模板: `Do not <ActionVerb1>, <ActionVerb2>, or <ActionVerb3>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 确保符合要求
- 模板: `Ensure that <Process> is <Status>, then <ActionVerb>.`
- 例句: Ensure that sample loading is complete, then rotate the tip counter-clockwise to remove it.

### 连续动作
- 模板: `<ActionVerb1> the <Object1>, and finally <ActionVerb2> the <Object2>.`
- 例句: Close the low-temperature compartment door and the room-temperature compartment door, and finally close the reagent compartment door.

### 步骤动作指令
- 模板: `Click the [<option_name>] to enter the <interface_name>.`
- 例句: 1. Click the 【Sequencing】 option on the main interface to enter the following interface:

### 前置处理条件
- 模板: `Mix the <reagent_name> thoroughly by <method> for <duration_or_cycles> before <adding_or_loading>.`
- 例句: Mix the dNTPs mixture thoroughly by vortexing for 5 seconds before adding, and briefly centrifuge before use.

### 操作预防性建议
- 模板: `When <action>, operate carefully to prevent <substance> from <negative_result>.`
- 例句: When transferring the mixture, operate carefully to prevent the liquid from spilling out of the reagent tube.

### 禁止性行为指令
- 模板: `When using <reagent_name>, do not <action> to avoid <negative_consequence>.`
- 例句: When using MDA Polymerase Mix II, do not touch the inner wall of the tube where the reagent is contained to avoid affecting enzyme activity.

### 界面交互指令
- 模板: `Click the <icon_description> icon next to [<element_name>] to <function_description>.`
- 例句: Click the ⊕ icon next to [DNB ID] to display information for the 4 lanes.

### 菜单选择指令
- 模板: `Select the <option_name> from the [<menu_name>] drop-down menu.`
- 例句: Select the spatial transcriptomics sequencing scheme from the [Sequencing Scheme] drop-down menu.

### 条件判定与警告
- 模板: `Please ensure the <input_field> is correct; otherwise, <error_message> will be prompted.`
- 例句: Please ensure the manually entered ID format is correct; otherwise, an ID error will be prompted, and you will not be able to continue.

### Figure/Table Reference
- 模板: `<Label> <Number> <Title>`
- 例句: Figure 30 Advanced Option Settings for DNBSEQ-T7RS

### Procedural Step
- 模板: `<Number>. After <Condition>, click [<Button>] and select [<Option>].`
- 例句: 1. After confirming the information is correct, click [Start] and select [Yes].

### Interface Display Instruction
- 模板: `Click <Action> to display the interface shown below, which allows you to <Function>.`
- 例句: 4. Click the expansion icon after 'Advanced Options' to display the interface shown below, which allows you to select whether to perform automatic cleaning.

### External Reference
- 模板: `Please refer to <DocumentName> for details.`
- 例句: Please refer to the DNBSEQ-T7 sequencer software operation guide for details.

### Conditional Status
- 模板: `When the interface is as follows, <Process> <Status>.`
- 例句: 2. When the interface is as follows, sequencing begins, at which point the on-instrument operations are complete.

### Situational Choice
- 模板: `Select <Action> in the following situations:`
- 例句: Select manual cleaning in the following situations:

### Post-Action Requirement
- 模板: `After clicking <Button>, please <Action>.`
- 例句: After clicking "Finish", please remove the slide and reagent tray.

### 简单指令
- 模板: `<verb> <object>`
- 例句: Enter the program.

### 条件执行
- 模板: `When <condition> is <verb>ed, <subject> will <action>`
- 例句: When "Yes" is selected for automatic cleaning, the DNBSEQ-T7RS will automatically perform a cleaning operation.

### 维护周期
- 模板: `<noun> should be <verb>ed <frequency>`
- 例句: Cleaning slides should be replaced every month or after 10 uses.

### 故障支持
- 模板: `If <condition>, please contact technical support.`
- 例句: If it still fails to meet requirements after re-preparation, please contact technical support.

### 界面交互
- 模板: `Click [<button>] on the interface, select [<option>] in the pop-up dialog box`
- 例句: Click [Cleaning] on the interface, select [Yes] in the pop-up dialog box

### 状态检查
- 模板: `Check if <noun> is <condition>`
- 例句: Check if the sealing ring is missing.

### 强制要求
- 模板: `<subject> must be <verb>ed <method>`
- 例句: After each run, the instrument must be cleaned either automatically or manually.

### 放置操作
- 模板: `Place <noun> into <location>, and close <location>`
- 例句: Place an empty T7 sequencing reagent cartridge into the refrigerated compartment on the side requiring a wash, and close the reagent compartment door.

### 步骤忽略
- 模板: `Skip this step if <condition>`
- 例句: Skip this step if there is no slide on the MGIDL-T7RS.

### 结果描述
- 模板: `<action>, indicating that <noun> is <condition>`
- 例句: press the slide suction button to show a green light, indicating that the slide is fully attached.

### 条件步骤（若未完成）
- 模板: `If there is still no improvement after <action>, <action>.`
- 例句: If there is still no improvement after manual cleaning and maintenance, re-prepare the cleaning reagent according to...

### 操作指令（简单执行）
- 模板: `<verb> <object>.`
- 例句: Remove the sequencing flow cell, check the seal for dust, and use a compressed air duster to blow away the dust.

### 操作建议（带条件）
- 模板: `Check if <object> is <state>; if not, <action>.`
- 例句: Check if the reagent needle is moving normally; if not, restart the sequencer's control software.

### 必要性约束
- 模板: `<object> must be <verb>ed within <time> after <action>.`
- 例句: The Qubit working solution must be used within 0.5 hours after preparation.

### 流程衔接（顺序）
- 模板: `Prepare <object> for <target> according to the table below:`
- 例句: Prepare reagents for standard tubes and test sample tubes according to the table below:

### 异常处理（兜底）
- 模板: `If the <object> abnormality still cannot be resolved by the methods above, please contact technical support.`
- 例句: If the pumping abnormality still cannot be resolved by the methods above, please contact technical support.

### 多步骤操作（联动）
- 模板: `<verb> <object> with one hand and <verb> <object> with the other.`
- 例句: Hold the side of the reagent cartridge with one hand and support the bottom of the reagent box with the other.

### 前置检查
- 模板: `Check that <object> is within the normal range of <value1> to <value2> before proceeding.`
- 例句: Check that the negative pressure is within the normal range of -80 to -99 kPa before proceeding.

### 步骤执行指令
- 模板: `Click [Button Name].`
- 例句: 8. Click [Next].

### 条件确认与后续操作
- 模板: `After confirming that <condition> is correct, click [Button Name].`
- 例句: 1. After confirming that all information is correct, click [Start].

### 确保准确性建议
- 模板: `Review all <item> to ensure it is accurate.`
- 例句: Review all filled-in information to ensure it is accurate.

### 目的状语说明
- 模板: `To ensure <goal>, <subject> automatically performs <action>.`
- 例句: To ensure sequencing quality, the sequencer automatically performs one additional cycle for calibration.

### 交叉引用指令
- 模板: `For details, please refer to the <Document Name>.`
- 例句: For details, please refer to the MGISEQ-2000 & MGISEQ-2000RS Gene Sequencer Software Operation Guide.

### 条件性操作建议
- 模板: `When <condition>, the system will prompt: [<Prompt Message>].`
- 例句: When using version control software for the first time or after an update, the system will prompt: [Perform maintenance cleanup?].

### 准备指令
- 模板: `Prepare <reagent> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### 保存期限与条件
- 模板: `Valid for <duration> when stored at <temperature>.`
- 例句: Valid for 1 month when stored at 2–8 °C

### 包含/组成描述
- 模板: `The <item>, mainly containing <component1>, <component2>, and <component3>.`
- 例句: The data folder, mainly contains image data, as well as data generated during the instrument's operation (metrics files).

### 命名方式描述
- 模板: `A <item> named by <parameter>.`
- 例句: The data folder, named by the slide ID, mainly contains image data.

### 操作指令-点击
- 模板: `Click [Button] on the [Interface], or click [Button] on the [Interface].`
- 例句: Click [Clean] on the main interface, or click [Clean] on the sequencing completed interface.

### 操作指令-放置
- 模板: `Place [Object] into the [Location].`
- 例句: Place the cleaning reagent tube 1 into the sample tube holder.

### 操作指令-缓慢移动
- 模板: `Following the direction indicated on the [Cover], slowly push/slide the prepared [Object] into the [Location].`
- 例句: Following the direction indicated on the cleaning reagent trough cover, slowly push the prepared cleaning reagent trough 1 into the reagent compartment bottom.

### 条件操作-弹窗响应
- 模板: `If the following [Object] appears, select [Option], and [Result].`
- 例句: If the following pop-up appears, select [Yes], and the instrument will automatically raise the needle.

### 步骤衔接-参考
- 模板: `For detailed steps, please refer to "[Title]" on page [Number].`
- 例句: For detailed steps, please refer to "Placing the Slide" on page 24.

### 问题排查
- 模板: `When [Condition], please perform the following operations to troubleshoot the issue:`
- 例句: When the DNB concentration is lower than 8 ng/μL, please perform the following operations to troubleshoot the issue:

### 图表标注
- 模板: `Figure [Number] [Description]`
- 例句: Figure 32 Cleaning Guidance Interface

### 操作要求-观察
- 模板: `Carefully observe whether [Condition] during the [Process] process.`
- 例句: Carefully observe whether any bubbles appear on the cleaning slide during the cleaning process.

### 状态声明
- 模板: `<Subject> Status: <Status>`
- 例句: Status A: Paused 20.0℃-91.6ka

### 条件指令
- 模板: `If <condition>, please <action>.`
- 例句: If the anomaly in negative pressure cannot be resolved using the methods above, please contact an engineer.

### 依标准操作
- 模板: `<Imperative Verb> <object> according to <reference>.`
- 例句: Perform a maintenance wash on the sequencer according to "Full Maintenance Wash (approx. 94 minutes)" on page 33.

### 礼貌提醒恢复
- 模板: `<Subject> <action>, please <action> promptly.`
- 例句: Side A sequencing paused, please resume promptly.

### 状态要求
- 模板: `There must be no <object> in <location>.`
- 例句: There must be no air bubbles in the detection tube.

### 顺序结果
- 模板: `After <action>, <subject> will <action>.`
- 例句: After resuming sequencing, the reagent needle will automatically descend.

### 操作指令建议
- 模板: `Please <action> to <purpose>.`
- 例句: Please download the latest version of the instruction manual to use with the corresponding version of the kit.

### 操作执行要求
- 模板: `Please <action> <object> according to <conditions>.`
- 例句: Please save the product according to the specified conditions as soon as possible.

### 注意事项/警告
- 模板: `Note: <action_or_condition>; <potential_consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 关键步骤强调
- 模板: `Key Steps: Pay special attention to <target> to avoid <potential_consequence>.`
- 例句: Key Steps: Pay special attention to these steps to avoid experimental failure or poor outcomes.

### 法律责任免除
- 模板: `Nothing herein is intended to or should be understood as <limitation_scope>.`
- 例句: Nothing herein is intended to or should be understood as any warranty of the performance of any product listed or described herein.

### 产品构成描述
- 模板: `Each <item> consists of the following <number> components:`
- 例句: Each reagent kit consists of the following four components:

### 适用平台能力说明
- 模板: `<product/process> can be <action> using <tool/platform>.`
- 例句: Sequencing libraries constructed using this product can be sequenced using the DNBSEQ sequencing platform.

### 储存条件规格
- 模板: `Storage temperature: <temp_range>; <transport_type> <validity_label>.`
- 例句: Storage temperature: -25℃ ~ -18℃; Cold chain transport shelf life: see label.

### 指南索引引用
- 模板: `For details, please refer to the <document_name>.`
- 例句: For details, please refer to the Stereo-seq Chip Carrier Storage Operation Guide.

### 设备/物料列表项
- 模板: `<Brand> <Description> <Catalog Number>`
- 例句: Invitrogen Qubit dsDNA HS Assay Kit Q32854

### 试剂/组分列表项
- 模板: `<Component Name> <Cat. No.> <Color> <Volume> × <Quantity>`
- 例句: Blocking Reagent 1000044666 Transparent 60 µL × 1

### 储存与运输要求
- 模板: `Storage temperature: <Temperature>; Shelf life for <Transport Type> transport: See label.`
- 例句: Storage temperature: −25°C to −18°C. Shelf life for cold chain transportation: See label.

### 品牌/产品选择建议
- 模板: `Choose one from <target> with the same <identifier>.`
- 例句: Choose one from brands with the same superscript number.

### 试剂功能说明
- 模板: `<Reagent Name> is used to <action>, and can be <action> based on <criteria>.`
- 例句: FcR Blocking Reagent is used to block Fc receptors on the cell membrane surface and can be purchased based on the species.

### 外部资源指引
- 模板: `For <topic>, please refer to <resource>: <URL>`
- 例句: For the selection of isotype control antibodies, please refer to this website: https://www.biolegend.com/en-us/search-results?PageSize=25&Category=ISO_CTRL&Format=TOTALSEQ_A

### 通用规格列表项
- 模板: `<Item Name> <Specification>`
- 例句: 50 mL centrifuge tube 430829

### 推荐操作
- 模板: `It is recommended to <action> <object>.`
- 例句: It is recommended to use pipette tips with filters and to change tips when aspirating different samples.

### 试剂配制
- 模板: `Take <quantity> of <source> and dilute to <quantity> with <diluent>; keep at <temperature>.`
- 例句: For 5X SSC, take 5 mL of 20X SSC and dilute to 20 mL with Nuclease-Free Water; keep at room temperature.

### 禁止项
- 模板: `Do not <action> <object>; <alternative_action> instead.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting instead.

### 实验前准备
- 模板: `Before <process>, please <action>.`
- 例句: Before conducting experiments, please familiarize yourself with the precautions for the instruments to be used and master their operation methods.

### 储存要求
- 模板: `<item> must be <condition> / should be stored at <temperature>.`
- 例句: Resealed chips must not be stored for more than two weeks.

### 通用试剂说明
- 模板: `Unless otherwise specified, <material> should be used for all <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water should be used for all liquids intended for reagent dilution in this experiment.

### 用量说明
- 模板: `Use <quantity> <unit> per chip and <status_instruction>.`
- 例句: Remove sheared salmon sperm DNA from -20°C and thaw; use 30 μL per chip and keep on ice.

### 操作指令：取出与准备
- 模板: `Take <object> out of the <source> and <action> to <purpose>.`
- 例句: Take the OCT-embedded tissue block out of the -80°C freezer and place it in the cryostat to equilibrate for 30 min;

### 操作指令：移液与吸弃
- 模板: `Use a pipette to aspirate and discard the <liquid> from one corner of the chip, ensuring the tissue on the chip remains <state>.`
- 例句: use a pipette to aspirate and discard the Wash Buffer from one corner of the chip, keeping the chip tissue moist;

### 操作指令：溶液添加
- 模板: `Add <volume> of <solution> to the chip and incubate at <condition> for <time>.`
- 例句: Add Wash Buffer to the chip at a volume of 200 μL/chip and incubate at room temperature for 1 min;

### 条件句：若/如果
- 模板: `If <condition>, <consequence>.`
- 例句: If the specimen head temperature is too low, it may cause cracks in the sections;

### 警示/禁止
- 模板: `Strictly avoid <action> during <process> to prevent <risk>.`
- 例句: Strictly avoid tissue drying during the liquid exchange process, as tissue drying can easily generate non-specific signals.

### 建议/参考
- 模板: `Refer to <table_or_section> to prepare <reagent_name>, vortex to mix, and centrifuge briefly before use.`
- 例句: refer to 2.5. Blocking and Antibody Incubation to prepare the primary antibody incubation solution, vortex to mix, and centrifuge briefly for use.

### 操作细则：倾斜角度
- 模板: `Slightly tilt the handheld carrier at an angle of less than <angle>°.`
- 例句: Slightly tilt the handheld carrier at an angle of less than 20°,

### 操作确认
- 模板: `If the chip surface is free of <impurities_list>, it is ready for <next_step>.`
- 例句: If the chip surface is free of impurities, obvious marks, residual liquid, and ripple patterns, it is ready for application;

### 步骤循环指令
- 模板: `Repeat <action> steps <range> <frequency>.`
- 例句: Repeat washing steps c.-d. once;

### 温育条件指令
- 模板: `<verb> at <temperature> for <duration>.`
- 例句: incubate at room temperature for 2 min;

### 文档引用指令
- 模板: `Refer to <section/table/document> to <action>.`
- 例句: Refer to Table 2-5 in section 2.6 DAPI Staining to prepare the DAPI working solution;

### 条件保障指令
- 模板: `Ensure <subject> <condition/constraint>; <consequence>.`
- 例句: Ensure the chip does not dry out during the liquid exchange process; if the tissue dries, it is prone to producing non-specific signals.

### 滴加操作指令
- 模板: `Add <volume> of <reagent> dropwise to <location>.`
- 例句: Add 150 μL/chip of DAPI working solution dropwise from the non-tissue area, and incubate at room temperature for 2 min;

### 前置条件说明
- 模板: `Before <action>, <verb> <reagent> at <condition>.`
- 例句: Before use, incubate the Decrosslinking Reagent in a metal bath or other equivalent equipment at 70°C for 10 min (do not exceed 30 min);

### 孵育指令
- 模板: `Incubate <substance> at <temperature> for <time>.`
- 例句: Incubate the permeabilization working solution in a metal bath at 37°C for 10 min.

### 倾斜吸弃操作
- 模板: `Slightly tilt the <carrier> at an angle of less than <angle>. Use a pipette to aspirate and discard the <reagent>.`
- 例句: Slightly tilt the handheld carrier at an angle of less than 20°. Use a pipette to aspirate and discard the Wash Buffer.

### PCR仪设置
- 模板: `Set the <instrument> temperature to <temperature> and the lid temperature to <lid_temperature>.`
- 例句: Set the PCR instrument temperature to 37°C and the lid temperature to 42°C.

### 密封载具
- 模板: `Seal the <carrier> with a <sealing_material>.`
- 例句: Seal the handheld carrier with a new sealing film.

### 接触避免警告
- 模板: `Avoid contact between <object_A> and <object_B>.`
- 例句: Avoid contact between the carrier and the front surface of the chip.

### 试剂加入指令
- 模板: `Add <reagent> at a volume of <volume> per <unit>.`
- 例句: Add PR Rinse Buffer solution (containing 5% RI) at a volume of 200 μL per chip.

### 操作禁令
- 模板: `Do not remove the <object> from <instrument> until <condition>.`
- 例句: After permeabilization is complete, do not remove the Handheld Carrier from the PCR instrument (37°C).

### 移液器操作警告
- 模板: `When <action>, do not touch the <object> to prevent <consequence>.`
- 例句: When aspirating the supernatant after elution, do not touch the magnetic beads.

### 条件操作指令
- 模板: `If <condition>, add <reagent> and <action> to <purpose>.`
- 例句: If the tissue is not completely removed, add 400 μL of 0.1X SSC and pipette gently to remove the tissue.

### 保持状态操作
- 模板: `Keep the <container> on the <device>, <verb> <amount> of <substance>...`
- 例句: Keep the centrifuge tube on the magnetic stand, add 1 mL of 80% ethanol...

### 步骤重复
- 模板: `Repeat step <number> once;`
- 例句: Repeat step 4) once;

### 按指引操作
- 模板: `<verb> according to <table_name> in <section_name>;`
- 例句: Prepare cDNA PCR Mix following Table 2-9 in section 2.15. Transcriptome cDNA Amplification,

### 样本补充
- 模板: `If the recovered sample above is less than <volume>, bring the volume to <volume> with <reagent>.`
- 例句: If the recovered sample above is less than 42 μL, bring the volume to 42 μL with Nuclease-Free Water.

### 混合与静置
- 模板: `<verb> to mix, incubate at room temperature for <time>, pulse centrifuge, place on a magnetic rack for <time> until the liquid clears;`
- 例句: vortex to mix, let stand at room temperature for 5 min, pulse centrifuge, magnetic rack静置 3-5 min，直至液体变澄清；

### 液体转移
- 模板: `Transfer the supernatant (<volume>) to a new <container>;`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 条件限制
- 模板: `Air-dry at room temperature for <time>, until the surface of the magnetic beads is <condition>;`
- 例句: air-dry at room temperature for 5-8 min, until the surface of the magnetic beads is non-reflective and uncracked;

### 警告/注意事项
- 模板: `The pipette tip should be operated against the tube wall away from the magnetic stand; do not <verb> or <verb> the magnetic beads;`
- 例句: The pipette tip should be operated against the tube wall away from the magnetic stand; do not pipette up and down or disturb the magnetic beads;

### 保存条件
- 模板: `The <substance> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### PCR 程序标注
- 模板: `<temperature> for <time>`
- 例句: 98°C for 20 s

### 表格标题模板
- 模板: `Table [X] Preparation of [Object]`
- 例句: Table 2-14 Preparation of Qubit dsDNA Mix

### 描述性说明模板
- 模板: `The [Subject] is typically [comparison] [Value].`
- 例句: The DNA concentration is typically higher than 5 ng/μL.

### 基础操作指令模板
- 模板: `[Imperative verb] [Object] [Prepositional phrase].`
- 例句: Transfer the ADT amplification PCR product (100 μL) to a new 1.5 mL microcentrifuge tube.

### 时间/条件衔接指令模板
- 模板: `After [Action], [Imperative verb] [Object] [Prepositional phrase] [Duration].`
- 例句: After a brief centrifugation, place the PCR tube on a magnetic stand and let it stand for 5 min.

### 重复步骤指令模板
- 模板: `Repeat step [Number] [Frequency].`
- 例句: Repeat step 3) once;

### 储存条件模板
- 模板: `[Subject] can be stored at [Condition] for [Duration].`
- 例句: ADT amplification products can be stored at −20°C for 1 month.

### 操作手册引用模板
- 模板: `For [Topic] regarding [Subject], please refer to [Document Title].`
- 例句: For specific procedures regarding subsequent library construction, please refer to the "Stereo-seq Library Preparation".

### 产品用途限制模板
- 模板: `This product is for [Purpose] only, not for [Prohibited Purpose].`
- 例句: This product is for research use only, not for diagnostic use.

### Requirement
- 模板: `The <process/action> must be performed in/with <requirement>`
- 例句: The entire operation must be performed in a clean environment to prevent environmental impurities from contaminating materials or chips.

### Conditional Instruction
- 模板: `If <condition>, <action/consequence>`
- 例句: If any defects are found, please contact after-sales service for replacement.

### Reference
- 模板: `For further information on <topic>, please refer to <source>`
- 例句: For further information on the Catalog No. of accessory kit products and their specific components, please refer to Table 1-1 and Table 1-2.

### Purpose Definition
- 模板: `<Action> to <prevent/achieve goal>`
- 例句: Avoid contact with the chip surface throughout the process to prevent damage to the probes.

### Polite Instruction
- 模板: `Please <action>`
- 例句: Please download the latest version of the user manual and use it with the corresponding version of the reagent kit.

### 流程条件句
- 模板: `During the <process_name>, the <object> must be <adverb_phrase>.`
- 例句: During the incubation process, the carrier must be placed stably; do not bump or shake the carrier.

### 必要条件引导
- 模板: `If <condition> is required, <action>.`
- 例句: If it is necessary to disassemble the carrier, do so after reagent removal to prevent reagent splashing.

### 建议采购与操作
- 模板: `It is recommended to purchase <item_name> [Cat. No.: <number>] and use <item_name> to <action>.`
- 例句: It is recommended to purchase the Stereo-seq V3 Cassette Disassembly Tool [Cat. No.: 303TA30011] and use the disassembly auxiliary tool to operate.

### 预防性提示
- 模板: `<Action_taken> to prevent <negative_outcome>.`
- 例句: Ensure reaction reagents do not splash to avoid contamination or reagent loss.

### 步骤指导
- 模板: `Use a <tool> to <action> <object>, <clause>.`
- 例句: Use a pipette to aspirate as much reagent as possible from the carrier's reaction well, avoiding contact between the pipette tip and the chip.

### 状态确认
- 模板: `Ensure <object> is <status_description>.`
- 例句: After replacement, ensure a new gasket is free of deformation and fits tightly.

### 注意事项
- 模板: `Note: <instruction>.`
- 例句: Note: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 提示与警示
- 模板: `<Type>: <Description>.`
- 例句: Tip: Additional operation tips and guidance.

### 关键步骤警示
- 模板: `Critical steps: Pay special attention to these steps to avoid <risk>.`
- 例句: Critical steps: Pay special attention to these steps to avoid experimental failure or undesirable results.

### 产品组成描述
- 模板: `Each <product> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 引用参考资料
- 模板: `For further information regarding <topic>, please refer to <Table/Document>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 and Table 1-2.

### 步骤前置引用
- 模板: `After <action>, please refer to the "<Document Name>" to <task>.`
- 例句: After receiving the Stereo-seq chip, please refer to the "Stereo-seq Custom Chip Storage Guidelines" to store the product.

### 条件触发建议
- 模板: `If <condition>, you may <suggested action>.`
- 例句: If any temperature abnormality is detected in the cold chain box, you may request the logistics provider to print the temperature real-time monitoring record sheet.

### 流程推荐操作
- 模板: `It is recommended to <action> before use, <action> and keep on ice.`
- 例句: It is recommended to take out the reagent components in advance before use, briefly centrifuge the enzyme components and keep on ice.

### 防止负面结果建议
- 模板: `To avoid <negative outcome>, the use of <item> is recommended; please <instruction>.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended; please change the tip when aspirating different samples.

### Prohibition/Safety Warning
- 模板: `Avoid <action> of <subject> with <object>; do not <action> <object>.`
- 例句: Avoid direct contact of skin and eyes with samples and reagents; do not ingest samples or reagents.

### Obligation/Compliance
- 模板: `<subject> shall be <action> in accordance with <regulations/standards>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### Applicability
- 模板: `This <method> is suitable for <target_type> with <conditions>.`
- 例句: This embedding method is suitable for tissues with dimensions < 2 cm × 3 cm × 0.7 cm.

### Strict Requirement
- 模板: `Under <conditions>, strictly ensure that <subject> undergoes <action> within <time_limit>.`
- 例句: Under laboratory conditions, strictly ensure that fresh samples undergo direct embedding within 30 minutes of excision,

### Limitation
- 模板: `The <subject> should not exceed <measurement_limit>.`
- 例句: The tissue size should not exceed 0.9 cm × 1.8 cm × 0.7 cm

### Strong Recommendation
- 模板: `It is strongly recommended to only <action> <subject> with <condition> for <purpose>.`
- 例句: It is strongly recommended to only use tissue samples with RIN ≥ 7 for subsequent experimental procedures.

### Instructional Step
- 模板: `Prepare <item> in advance and <action> to pre-cool for <time>.`
- 例句: Prepare a foam box of crushed ice in advance and place the OCT on the ice to pre-cool for 10 min;

### Default Condition
- 模板: `Unless otherwise specified, <material> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease Free Water is used for all liquids in this experiment to dilute reagents.

### Conditional Step
- 模板: `Check if <condition>; if not, <action>.`
- 例句: Check if the bottom of the embedding block is completely covered; if not completely covered, place the tissue block on a metal block

### 浓度/pH稀释调整
- 模板: `Dilute <reagent> to <concentration> according to the <method>, with pH accurate to <value> (ensure pH value is in the range of <range>).`
- 例句: Dilute to 0.01 N according to the HCl concentration gradient, with pH accurate to 2 (ensure pH value is in the range of 1.9-2.1).

### 试剂储存液稀释
- 模板: `Dilute <amount> of <reagent_stock> to <final_amount> with <diluent> (at least <amount>/chip).`
- 例句: Dilute 25 μL of 10X permeabilization reagent stock solution to 250 μL with 0.01N HCl (at least 200 μL/chip).

### 预防性操作/环境准备
- 模板: `Place <item> into the <container> in advance to pre-cool.`
- 例句: Place brushes, blades, forceps, etc., into the chamber in advance to pre-cool.

### 孵育操作
- 模板: `Incubate the <reagent> in a <temperature> constant temperature incubator for <time> before use.`
- 例句: Incubate the permeabilization working solution in a 37°C constant temperature incubator for 10 min before use.

### 结果确认
- 模板: `After the <substance> has evaporated completely, the <sample> will be visibly <state> to the naked eye; transfer the <object> to <location>.`
- 例句: After the methanol has evaporated completely, the tissue will be visibly white to the naked eye; transfer the chip to the experimental table.

### 试剂添加频率控制
- 模板: `Sequentially add the <reagent> at regular intervals (e.g., <time>).`
- 例句: Sequentially add the permeabilization reagent at regular intervals (e.g., 6 min).

### 试剂用量
- 模板: `<ReagentName> volume: <Volume>/chip`
- 例句: 1X Permeabilization working solution volume: 200 μL/chip

### 操作步骤（直接指令）
- 模板: `<ImperativeVerb> <Object> <Optional: Location/Method>`
- 例句: Slightly tilt the chip, and use a pipette to aspirate the solution from the upper surface of the chip from one corner

### 操作步骤（依据表格）
- 模板: `<ImperativeVerb> <Object> according to Table <Number>`
- 例句: Prepare the Total RNA hybridization Mix according to Table 3-4;

### 操作步骤（基于条件）
- 模板: `Based on <Condition>, <ImperativeVerb> <Object>`
- 例句: Based on the chip size, add the corresponding volume of Total RNA hybridization Mix from Table 3-4 onto the chip surface

### 条件建议/提醒
- 模板: `If <Condition>, <Action/Suggestion>`
- 例句: If white precipitate is observed in the buffer, it can be dissolved at 55°C and then returned to room temperature.

### 禁忌/警告
- 模板: `The <Subject> should not be <Adjective>, so as to avoid <NegativeOutcome>`
- 例句: The pre-cooling time should not be too long, so as to avoid water mist forming on the chip surface

### 目的状语
- 模板: `<Action> <Object> to avoid <NegativeOutcome>`
- 例句: Immediately add the RT QC Mix to prevent RNA degradation.

### 祈使句-操作指令
- 模板: `<verb> <object> (optionally: <prepositional_phrase>)`
- 例句: Add 1-2 μL of water to the stage.

### 步骤衔接-序列操作
- 模板: `First, <action_1>, then <action_2> to <purpose>.`
- 例句: First, use the 4x objective lens to locate the target area, then switch to the 10x objective lens to scan the entire chip.

### 条件状语-环境设定
- 模板: `Under the condition that <condition_clause>, <main_clause>.`
- 例句: Under the condition that the tissue has been removed cleanly and while maintaining identical imaging conditions, <main_clause>.

### 判断标准-定义
- 模板: `<criteria_list> are the criteria for determining the <target>.`
- 例句: Intact morphology, strongest fluorescence, and absence of diffusion are the criteria for determining the optimal permeabilization time.

### 结果描述-图表引用
- 模板: `As shown in Figure <number>, at <condition>, the <subject> exhibits <result>.`
- 例句: As shown in Figure 2, at a permeabilization time of 6 min, the tissue exhibits uneven brightness.

### 禁止事项-强制性
- 模板: `<subject> should only <action>; the use of <forbidden_items> is prohibited.`
- 例句: Folder names should only use letters, numbers, and underscores; the use of special characters such as spaces is prohibited.

### 强制性要求-必须
- 模板: `<subject> must be <action_passive> under <condition>.`
- 例句: Chips of the same tissue with different permeabilization times must be scanned under the same exposure conditions.

### 产品说明-限制声明
- 模板: `This product is for <usage_type> only, not for <prohibited_use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 提示信息-建议
- 模板: `Note: Please <action> for use with <target_item>.`
- 例句: Note: Please download the latest version of the instruction manual for use with the corresponding version of the kit.

### 勘误/更新说明
- 模板: `<action_past_tense> the <item_details>.`
- 例句: Corrected the catalog numbers for some components of the Stereo-seq Library Preparation Kit.

### 参考查阅句式
- 模板: `For further information regarding <item1>, <item2>, etc., please refer to <Table/Section ID>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-2.

### 操作建议句式
- 模板: `Please <action> the product according to the specified conditions as soon as possible.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 条件触发句式
- 模板: `If <condition> is detected, you may <action>.`
- 例句: If an abnormal temperature in the cold chain box is detected, you may request the logistics provider to print the real-time temperature monitoring record.

### 组件功能描述句式
- 模板: `The <Kit Name> can be used to <action1> and <action2>.`
- 例句: The STOmics Stereo-seq Library Construction Kit can be used to construct whole-transcriptome 3'-end libraries from spatial-temporal cDNA amplification products.

### 试剂盒配套说明句式
- 模板: `<Kit Name> can also be paired with <Compatible Kit Name> for use.`
- 例句: STOmics Stereo-seq library preparation kits can also be paired with Stereo-seq 16 Barcode Amplification Kit use.

### 规格说明句式
- 模板: `<Quantity>/<Unit> × <Count> <Unit>`
- 例句: 40 μL/vial × 1 vial

### 自备物料说明句式
- 模板: `This list details the equipment and materials required for this experiment. <Table ID> does not include standard laboratory equipment, such as <list of equipment>.`
- 例句: This list details the equipment and materials required for this experiment. Table 1-3 does not include standard laboratory equipment, such as ice machines, biological safety cabinets, pH meters, refrigerators, etc.

### 免责与用途声明句式
- 模板: `This product is intended for research use only and is not for use in clinical diagnostic procedures.`
- 例句: This product is intended for research use only and is not for use in clinical diagnostic procedures.

### 流程灵活性说明句式
- 模板: `The experimental protocols provided in this manual are general guidelines; in actual operation, they may be adapted according to <factor>.`
- 例句: The experimental protocols provided in this manual are general guidelines; in actual operation, they may be adapted according to specific experimental design, sample characteristics, sequencing applications, and equipment.

### 预处理操作指令句式
- 模板: `Before use, it is recommended to <action1>, <action2>, and <action3>.`
- 例句: Before use, it is recommended to remove the reagent components in advance, briefly centrifuge the enzyme components and place them on ice for later use.

### 建议/推荐动作
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 避免/禁止事项
- 模板: `Avoid <doing_something>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 步骤衔接（混合与处理）
- 模板: `Vortex to mix, centrifuge briefly, then <verb> <object>.`
- 例句: Vortex to mix, centrifuge briefly, then place in the PCR instrument and perform amplification according to the reaction program.

### 试剂操作（前提条件）
- 模板: `Unless otherwise specified, <reagent> is used for all <action> in this experiment.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids for reagent dilution in this experiment.

### 离心与收集
- 模板: `Centrifuge briefly to collect the reaction mixture at the bottom of the tube.`
- 例句: After the reaction is complete, remove the reaction tube(s) and centrifuge briefly to collect the reaction mixture at the bottom of the tube.

### 准备工作
- 模板: `Prepare the <object> according to Table <number>.`
- 例句: Prepare the fragmentation Mix according to Table 2-1.

### 磁珠漂洗
- 模板: `Keep the tube on the magnetic rack, add <volume> of <reagent>, and rotate the tube to wash the magnetic beads.`
- 例句: Keep the centrifuge tube on the magnetic rack, add 200 μL of freshly prepared 80% ethanol, and by rotating the centrifuge tube on the magnetic rack to wash the magnetic beads.

### 条件限定
- 模板: `If <condition>, you may <verb> <object>.`
- 例句: If the number of libraries mixed for a single sequencing run is 1-4, you may select the PCR Barcode Primer Mix provided with this kit.

### 结果记录
- 模板: `Measure the concentration using the <method/kit> and record it.`
- 例句: Take 1 μL of PCR product, measure the concentration using the Qubit dsDNA HS Kit, and record it.

### 平衡试剂
- 模板: `Remove <reagent> in advance and equilibrate to room temperature.`
- 例句: Remove magnetic beads in advance and equilibrate to room temperature.

### 步骤保持与添加
- 模板: `Keep the <Tube> on the <Equipment>, and add <Volume> of <Reagent> to <Action>.`
- 例句: Keep the tube on the magnetic stand and add 400 μL of 80% ethanol to wash.

### 条件建议
- 模板: `If <Condition>, <Action/Recommendation>.`
- 例句: If 1-4 libraries are mixed for a single sequencing run, the PCR Barcode Primer Mix can be selected.

### 文档引用
- 模板: `Please refer to the <Manual_Name> to <Action>.`
- 例句: Please refer to the manual for the 'High-throughput Sequencing Primer Kit (Stereo-seq)' to prepare DNBs.

### 常规标准描述
- 模板: `The <Metric> is usually <Comparison/Requirement>.`
- 例句: The concentration is usually greater than 10 ng/μL.

### 重复步骤
- 模板: `Repeat step <Step_Identifier> once.`
- 例句: Repeat step c once.

### 混合操作
- 模板: `Mix the <Object_A> with <Object_B> in a <Ratio> ratio, <Mixing_Action>.`
- 例句: Mix the PCR product with magnetic beads equilibrated to room temperature in a 1:2 ratio, mix by vortexing.

### QC要求
- 模板: `QC requires <Object> to be <State/Requirement>.`
- 例句: QC requires fragments to be distributed around 200-250 bp.

### 操作前准备（离心）
- 模板: `Before using <product>, centrifuge it to collect the liquid at the bottom of the tube.`
- 例句: Before using the PCR Barcode Primer Mix, centrifuge it to collect the liquid at the bottom of the tube.

### 条件限定说明
- 模板: `If <condition>, <consequence>.`
- 例句: If different libraries use the same barcode combination, they cannot be sequenced in the same lane.

### 参考说明
- 模板: `For <condition>, refer to <location>.`
- 例句: For different numbers of samples, refer to the recommended Barcode combination schemes in Appendix Table 2.

### 强制性操作要求
- 模板: `Ensure that <action>.`
- 例句: Ensure that libraries requiring more than 20% of the data in a single lane use a set of PCR Barcode Primer Mixes.

### 分步操作指引
- 模板: `Perform in two steps: 1. <step1>. 2. <step2>.`
- 例句: Perform in two steps: 1. Divide libraries 1-8 into one group... 2. Remaining libraries...

### 产品核查及后续处理
- 模板: `Please promptly verify that <item> is <status>, and then immediately <action>.`
- 例句: Please promptly verify that the aluminum bag is intact and vacuum-sealed, and then immediately store the unopened Stereo-seq chip.

### 操作示例引导
- 模板: `Examples of <action>:`
- 例句: Examples of mixing different PCR Barcode Primer Mixes:

### 操作避让指引
- 模板: `Refer to <location> when selecting a combination (avoid <range>).`
- 例句: Refer to 3 libraries/lane when selecting a combination (avoid 1~4).

### 产品用途限定
- 模板: `This product is for <usage> only and not for <negative_usage> purposes.`
- 例句: This product is for research use only and not for diagnostic purposes.

### 权利声明
- 模板: `<year> <organization>. All rights reserved.`
- 例句: 2023 BGI Research. All rights reserved.

### 免责声明
- 模板: `<Organization> makes no guarantee, and hereby disclaims any guarantee regarding <action>.`
- 例句: BGI Research makes no any guarantee, and hereby disclaims any guarantee regarding the use of any third-party products or protocols mentioned herein.

### 操作提示
- 模板: `Note: Please <verb> the <object> for use with the <object_version>.`
- 例句: Note: Please download the latest version of the instruction manual for use with the corresponding version of the kit.

### 操作注意事项
- 模板: `Note: Pay special attention; <cause> may lead to <result>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experimental failure.

### 组成部分描述
- 模板: `Each reagent set consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### 操作参考指令
- 模板: `After receiving the <object>, please refer to the "<document_name>" to <action>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 额外订购说明
- 模板: `<item> (Must be ordered separately)`
- 例句: Stereo-seq PCR adapter (must be ordered separately)

### 品牌选择建议
- 模板: `Select one from the listed brands (marked with <symbol>).`
- 例句: Select one from the listed brands (marked with *).

### 规格标签标注
- 模板: `<attribute_name>: <value>; <attribute_name_2>: see label`
- 例句: Storage temperature: -25°C to 8°C; Shelf life for cold chain transport: see label

### 步骤动作描述
- 模板: `Take out the <item_1> and <item_2> from the <package_name>;`
- 例句: a. Take out the fixture and gasket from the Stereo-seq Slide Accessory Kit;

### 状态校验指令
- 模板: `<action>, ensuring the <part_1> and <part_2> are <status>.`
- 例句: b. With the fixture upside down, insert the gasket into the fixture, ensuring the hole cutouts of the fixture and the gasket are aligned.

### 紧急储存处理
- 模板: `Upon receipt, must immediately store <subject> at <temperature>.`
- 例句: Upon receipt, must immediately store the unopened Stereo-seq P/T chips at -20°C or 4°C.

### 容器组成描述
- 模板: `The <container> contains <quantity> <item_1>, and each of the <quantity> <item_1> has <item_2> attached to it.`
- 例句: The chip box contains 4 carriers, and each of the 4 chip carriers has one Stereo-seq chip T (1cm*1cm) attached to it.

### 品牌偏好建议
- 模板: `For <component>, <brand_1> is preferred, while <brand_2> is a domestic alternative.`
- 例句: For hematoxylin, Brand 1 is preferred, while Brand 2 is a domestic alternative.

### 目的建议
- 模板: `To <achieve_goal>, it is recommended to <action>.`
- 例句: To avoid cross-contamination of samples, it is recommended to use pipette tips with filters and change tips when aspirating different samples.

### 禁止警告
- 模板: `Avoid <action> and <action>; do not <prohibited_action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 交叉引用
- 模板: `Refer to <figure_name/document_name>.`
- 例句: Refer to Figure 1. RNA RIN value peak plot of mouse brain tissue sections.

### 步骤顺序
- 模板: `<time_condition>, <action_1>, and <action_2>.`
- 例句: After freezing for 5 minutes, remove the metal embedding cassette B and check if the OCT has completely solidified and turned white and opaque.

### 用量限制
- 模板: `<Item_name>: <amount> per <unit>; <condition>.`
- 例句: H&E Mounting Medium: 3.5 μL per chip at room temperature.

### 条件句（建议/警告）
- 模板: `If <condition>, <consequence/action>.`
- 例句: If the specimen head temperature is too low, it will cause cracks in the sections.

### 用量/频次表达
- 模板: `<action> with <volume> <reagent> <frequency>.`
- 例句: Wash 3 times with 100 μL of Wash Buffer.

### 禁止/防错表达
- 模板: `Do not <action>.`
- 例句: Do not touch the chip surface.

### 确保要求
- 模板: `Ensure <condition>.`
- 例句: Ensure that the methanol is immersed over all chips.

### 建议动作
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to complete section mounting within 5 minutes.

### 调整依据
- 模板: `<action> according to <basis>.`
- 例句: Adjust according to the actual operational process.

### 顺序执行步骤
- 模板: `First, <action_1>, then <action_2>.`
- 例句: First, add one drop of staining solution to each corner, then add the rest to the center.

### Imperative Action
- 模板: `<verb> <object> [preposition] <location/context>`
- 例句: Slowly add 100 μL of 0.01N HCl solution dropwise onto the chip, then aspirate the liquid from one corner of the chip.

### Sequential Step
- 模板: `After the <process> is complete, <action>.`
- 例句: After the incubation is complete, fix the support onto the carrier to assemble into a handheld carrier, ensuring the 8 buckles of the clamp are fastened and both sides of the support are closely attached to the clamp.

### Conditional Trigger
- 模板: `Once <action> has <status>, <action>.`
- 例句: Once the H&E Mounting Medium has fully infiltrated the chip, immediately proceed with imaging (if re-imaging is required, it is recommended that the total time from mounting to imaging for each chip does not exceed 30 min).

### Verification Requirement
- 模板: `Ensure <object> is <condition>.`
- 例句: Ensure the chip is completely submerged in the solution.

### Precautionary Constraint
- 模板: `Avoid <action> [when/to avoid] <consequence>.`
- 例句: Avoid touching the front side of the chip when assembling the carrier.

### 操作指令 - 混合
- 模板: `Mix <object1> with <object2> at a <ratio> ratio, <verb_method>, and <verb_action>.`
- 例句: Mix the PCR product (100 μL) with magnetic beads equilibrated to room temperature at a 1:1 ratio, shake to mix, and incubate at room temperature for 10 min.

### 操作指令 - 离心/静置
- 模板: `Briefly centrifuge, then <verb_action1> and <verb_action2>.`
- 例句: Briefly centrifuge, then place the centrifuge tube on a magnetic stand and let it stand for 3 min.

### 操作指令 - 清除上清
- 模板: `After the liquid clears, carefully remove the supernatant with <tool>.`
- 例句: After the liquid clears, carefully remove the supernatant with a pipette (if there is foam on the tube lid, aspirate the foam).

### 操作指令 - 漂洗
- 模板: `Keep the centrifuge tube on the magnetic stand and add <volume> of <reagent>.`
- 例句: While keeping the centrifuge tube on the magnetic stand, add 1 mL of 80% ethanol (use freshly prepared 80% ethanol equilibrated to room temperature).

### 操作指令 - 风干
- 模板: `Air-dry at room temperature for <time> until <state>.`
- 例句: Keep the centrifuge tube on the magnetic rack and air-dry at room temperature for 5-8 minutes until the surface of the beads is free of reflection and cracking.

### 操作指令 - 回溶
- 模板: `Add <volume> of <reagent> to resuspend, <verb_method>, and <verb_action>.`
- 例句: Add 22 μL of Nuclease-Free Water to resuspend, vortex to mix, incubate at room temperature for 5 minutes, spin down briefly, and let stand on the magnetic stand for 3-5 min.

### 条件句 - 若...
- 模板: `If <condition>, <action>.`
- 例句: If white precipitate is observed in the cDNA recovery solution, it can be dissolved at 55°C and purified after returning to room temperature.

### 禁止/警示
- 模板: `Avoid <action> to prevent <consequence>.`
- 例句: When opening or closing the tube cap while on the 1.5 mL magnetic stand, avoid vigorous movements that could cause the magnetic beads or liquid to pop out.

### 指引/参考
- 模板: `For detailed procedures regarding <subject>, please refer to the "<document_title>".`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the "Stereo-seq Library Preparation Kit Instruction Manual".

### Change Notification
- 模板: `The <parameter> for the <process> has been changed from <value> to <value>.`
- 例句: The incubation time for the permeabilization working solution has been changed from 3 min to 10 min.

### Conditional Guidance
- 模板: `If <condition>, the <process> may be extended up to <time>.`
- 例句: If tissue removal is incomplete, the removal time may be extended up to 16 h.

### Operational Warning
- 模板: `Note: Pay special attention; <consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may cause the experiment to fail.

### Critical Risk Warning
- 模板: `Critical Steps: Pay special attention to these steps to avoid <risk> or <result>.`
- 例句: Critical Steps: Pay special attention to these steps to avoid experimental failure or undesirable outcomes.

### Component Specification
- 模板: `<Component> volume <action> to <value>.`
- 例句: PR Rinse Buffer solution (containing 5% RI) volume standardized to 200 μL.

### Procedure Update
- 模板: `<Procedure> updated.`
- 例句: Fluorescence imaging procedure updated.

### Structural Heading
- 模板: `Chapter <number> <Title>`
- 例句: Chapter 1 Product Introduction

### Introductory Clause
- 模板: `Each reagent kit consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following three parts:

### 物品选配/替代建议
- 模板: `Select <number> from the listed brands (marked with <symbol>).`
- 例句: Select one from the listed brands (marked with * / marked with †).

### 包含关系说明
- 模板: `The <object> contains <component>.`
- 例句: The Stereo-seq carrier accessory kit contains fixtures for the chip carriers and detachable gaskets.

### 禁止/约束
- 模板: `<object> must not be <action> for more than <duration>.`
- 例句: Resealed chips must not be stored for more than two weeks.

### 有效期描述
- 模板: `Shelf life for <condition>: see label.`
- 例句: Shelf life for transport at room temperature: see label.

### 流程说明（步骤列表）
- 模板: `<imperative_verb> <object> <direction>.`
- 例句: Remove the clamp and gasket from the Stereo-seq Chip Accessory Kit.

### 检查确认
- 模板: `Inspect the <object> to ensure they are <condition>.`
- 例句: Finally, inspect the assembled fixture and chip carrier to ensure they are correctly positioned.

### 操作对准
- 模板: `Align the <object> with the <object>.`
- 例句: Align the chip with the gasket hole to avoid contact between the fixture and gasket with the chip surface;

### 试剂处理建议
- 模板: `It is recommended to <action> the <reagent_components> in advance.`
- 例句: It is recommended to take out the reagent components in advance.

### 安全警示
- 模板: `Avoid direct contact of <substances> with <parts_of_body>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 废弃物处理要求
- 模板: `<objects> should be disposed of in accordance with <regulations>.`
- 例句: All samples and various types of waste should be disposed of in accordance with relevant regulations.

### 离心操作
- 模板: `Briefly centrifuge the <object> and keep it on ice for use.`
- 例句: Briefly centrifuge the enzyme components and keep them on ice for use.

### 试剂稀释
- 模板: `Take <volume> of <reagent> and dilute to <volume>.`
- 例句: Take 5 mL of 20X SSC and dilute to 20 mL.

### 预处理建议
- 模板: `It is recommended to pre-cool the <object> to <temperature> in advance.`
- 例句: Pre-cool the cryostat chamber to −20°C in advance.

### 分装储存建议
- 模板: `Unused <object> can be aliquoted and stored at <temperature> to avoid <process>.`
- 例句: Unused RT Oligo can be aliquoted and stored at −80℃ to avoid repeated freeze-thaw cycles.

### 祈使句式（操作指令）
- 模板: `<verb> <object> (<prepositional_phrase>)`
- 例句: Mount the tissue block onto the specimen holder using OCT;

### 步骤衔接句式
- 模板: `<action_1>, then <action_2>`
- 例句: Remove the carrier from the slide box or 50 mL centrifuge tube, and use lint-free paper to blot away excess methanol;

### 条件约束句式
- 模板: `If <condition>, <action>; if <condition>, <action>`
- 例句: If the specimen chuck temperature is too low, it will cause cracks in the sections; if the temperature is too high, it will cause wrinkles.

### 量化表达句式
- 模板: `<action> <substance> at a volume of <amount>/<unit>`
- 例句: Add the tissue fluorescent staining solution to the chip at a volume of 100 μL/chip.

### 禁止操作句式
- 模板: `Do not <verb> <object>`
- 例句: Do not touch the chip surface.

### 目的/结果描述句式
- 模板: `<action> to <purpose/result>`
- 例句: Trim the tissue block as necessary to ensure the tissue section properly fits the chip.

### 状态确保句式
- 模板: `Ensure <that_clause>`
- 例句: Ensure that the methanol is enough to submerge all chips.

### 建议/推荐句式
- 模板: `It is recommended to <action>`
- 例句: It is recommended to complete the tissue section mounting within 5 min.

### 重复步骤指引
- 模板: `Repeat steps <step_range> until <result>`
- 例句: Repeat steps 2)-3) until all tissue sections are adsorbed onto the chip surface.

### 时间限制句式
- 模板: `<action>, <time_restriction>`
- 例句: Incubate at 37°C for 5 min.

### 命令句/操作步骤
- 模板: `<verb> <object> (<details>).`
- 例句: Add 150 μL/chip of 1X permeabilization reagent working solution from a corner of the reaction well.

### 条件确保句
- 模板: `Ensure <condition>.`
- 例句: Ensure the chip is completely covered by the 1X permeabilization reagent working solution.

### 引用参考句
- 模板: `Refer to <step_or_table> to <action>.`
- 例句: Refer to step 1.6 to assemble the gasket and clamp into a carrier.

### 温度/时间条件句
- 模板: `Incubate at <temperature> for <time>.`
- 例句: Incubate at 37°C for 10 min.

### 禁止/警告句
- 模板: `Avoid <action_or_state>.`
- 例句: Avoid allowing the chip to dry out completely.

### 状态平衡句
- 模板: `<substance> equilibrated to <state>.`
- 例句: magnetic beads equilibrated to room temperature.

### 步骤衔接句
- 模板: `After <process> is complete, <action>.`
- 例句: After permeabilization is complete, remove the handheld carrier from the PCR instrument.

### 用量描述句
- 模板: `<action> <volume>/<unit> of <substance>.`
- 例句: Add 200 μL/chip of RT Mix to one corner of the chip.

### 试剂添加与处理
- 模板: `Add <quantity> of <reagent> to <action>`
- 例句: Add 22 μL of Nuclease-Free Water to resuspend

### 样本转移
- 模板: `Transfer the <substance> to a <destination>`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 孵育条件
- 模板: `Incubate at <temperature> for <duration>`
- 例句: Incubate at room temperature for 5 min

### 依据指引操作
- 模板: `Prepare <substance> according to <reference>`
- 例句: Prepare PCR Mix according to Table 3-4

### 条件补足
- 模板: `If <condition>, top it up with <reagent>`
- 例句: If the recovered sample volume mentioned above is less than 42 μL, top it up with Nuclease-Free Water.

### 操作禁忌
- 模板: `Do not <action> or <action> the <object>`
- 例句: do not pipette up and down or agitate the magnetic beads

### 操作规范提示
- 模板: `<component> should be operated <location>`
- 例句: Pipette tips should be operated on the tube wall away from the magnetic rack

### 操作建议
- 模板: `For <purpose>, we recommend <action>`
- 例句: For subsequent troubleshooting, we recommend keeping 2 µL of PCR product.

### 外部引用指针
- 模板: `For <topic>, please refer to <reference>`
- 例句: For specific procedures regarding subsequent library construction, please refer to the "Stereo-seq Library Preparation Kit User Manual".

### 表格/图示标题
- 模板: `<identifier> <title>`
- 例句: Table 3-5 PCR Amplification Program

### 步骤命名/标题句式
- 模板: `<number>. <noun phrase>`
- 例句: 3.2. Section Preparation

### 条件建议/指导句式
- 模板: `If <condition>, it is recommended to <action>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transport.

### 指令执行句式
- 模板: `Please <action> according to <reference>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 特殊标注句式（提示/注意/警告）
- 模板: `<Type>: <description/instructions>.`
- 例句: Critical steps: Pay special attention to these steps to avoid experiment failure or poor results.

### 兼容性说明句式
- 模板: `<product> (or an instrument with equivalent functionality)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or an instrument with equivalent functionality)

### 选择性指令句式
- 模板: `Select one of the listed brands (marked with *).`
- 例句: Select one of the listed brands (marked with *).

### 结果确认句式
- 模板: `All components will maintain full activity throughout their shelf life when <conditions> are met.`
- 例句: When transportation, storage, and usage conditions are met, all components will maintain full activity throughout their validity period.

### 必要条件句式
- 模板: `(Must be ordered separately)`
- 例句: (Must be ordered separately) Stereo-seq PCR adapter *1 (2 EA)

### 功能说明句式
- 模板: `<Product> is used for <action>.`
- 例句: The STOmics® Stereo-seq Transcriptomic Reagent Kit (Carrier-based) is used for constructing whole-transcriptome 3' end libraries.

### 文库使用说明句式
- 模板: `Sequencing libraries constructed using this product can be sequenced using the <platform> platform.`
- 例句: Sequencing libraries constructed using this product can be sequenced using the DNBSEQ sequencing platform.

### 目的导向建议
- 模板: `To <purpose>, it is recommended to <action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use pipette tips with filters.

### 动作指令
- 模板: `<Condition/Time>, please <action>.`
- 例句: Before the experiment, please familiarize yourself with the precautions for the instruments.

### 条件要求
- 模板: `If <condition>, <subject> must be <action>.`
- 例句: If unused after opening, it must be re-dried, sealed, and stored at -20°C or 4°C.

### 参考链接
- 模板: `<Content> reference link: <URL>`
- 例句: Assembly method video reference link: https://www.stomics.tech/col113/607

### 强烈建议
- 模板: `It is strongly recommended to <action>.`
- 例句: It is strongly recommended to only proceed with subsequent experiments using tissue samples with an RIN ≥7.

### 操作必须
- 模板: `<Object> must be <action> to <purpose>.`
- 例句: Desiccant must be placed in the resealed aluminum bag to maintain dry conditions.

### 用途说明
- 模板: `This product is for <use> only.`
- 例句: This product is for research use only.

### 选项选择
- 模板: `Select any one from <scope>.`
- 例句: Select any one from the listed brands (marked with * / marked with †).

### 方位指令
- 模板: `Align/Orient the <object> towards <direction>.`
- 例句: Align the chip carrier label towards the direction of the fixture's long side clips.

### 时间约束指令
- 模板: `Within <time_duration> of <action>, <imperative_verb> <object>...`
- 例句: Within 30 minutes of fresh tissue excision, wipe dry the liquid on the tissue surface with sterile non-woven fabric

### 试剂配制流程
- 模板: `<imperative_verb> <amount> of <reagent> and <action> to <volume>...`
- 例句: Take 5 mL of 20X SSC and dilute to 20 mL

### 注意事项/禁止指令
- 模板: `Do not <action>, <imperative_verb> <alternative_action>...`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 设备参数设定
- 模板: `<temperature> for <process> (lid <temperature>)...`
- 例句: 37°C for slide baking and permeabilization (lid 42°C)

### 过程确认/检查
- 模板: `Check <object> for <status/condition>, and <alternative_action> if necessary.`
- 例句: Check the PCR instrument for abnormalities, and replace if necessary.

### 前置条件声明
- 模板: `Unless otherwise specified, <reagent> is used for <action> in this experiment.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for diluting reagents in this experiment.

### 时间提醒/警告
- 模板: `The <duration_type> must not be <adjective> to avoid <consequence>; it must not be <adjective>, otherwise <consequence>.`
- 例句: The pre-cooling time must not be too long to avoid water mist forming on the slide surface; it must not be too short, otherwise the slide cannot reach the pre-cooling temperature.

### 操作指令 - 添加试剂
- 模板: `Add <amount> of <reagent_name> onto the chip.`
- 例句: Add 30 μL of tissue fluorescence staining solution onto the chip per chip.

### 操作指令 - 吸取/移出液体
- 模板: `Use a pipette to aspirate <reagent_name> from one corner of the chip.`
- 例句: use a pipette to aspirate the tissue fluorescent staining solution from one corner of the chip

### 操作指令 - 孵育
- 模板: `Incubate at <temperature> for <time>.`
- 例句: incubate at 37℃ for 5 min.

### 条件句 - 步骤衔接
- 模板: `After <process_completed>, <next_action>.`
- 例句: After track modeling points are completed, set the gain to the minimum.

### 建议 - 确保条件
- 模板: `Ensure that <condition>.`
- 例句: Ensure that there is no residual staining solution on the chip.

### 禁止 - 预防性警告
- 模板: `Avoid <undesired_action>.`
- 例句: Avoid touching the front of the chip when assembling the carrier.

### 操作指令 - 预处理
- 模板: `Equilibrate <reagent_name> at <temperature> for <time> in advance.`
- 例句: Equilibrate Glycerol at room temperature for 5 minutes in advance.

### 步骤衔接 - 重复操作
- 模板: `Repeat steps <step_range> until <condition>.`
- 例句: Repeat steps 2)-3) until all tissue sections are attached to the chip surface.

### 成像策略 - 设置
- 模板: `Set the <parameter> to the <setting_value>.`
- 例句: set the gain to the minimum, determine the final imaging parameters after imaging starts.

### 注意事项 - 避免过曝
- 模板: `Try to avoid overexposure by <method>.`
- 例句: try to avoid overexposure. This can be assessed using image pixel statistics (e.g., histogram).

### 按表格准备试剂
- 模板: `Prepare <reagent_name> according to <table_reference>.`
- 例句: a. Prepare the cDNA Release Mix according to Table 3-3 and keep it at room temperature.

### 加入指定体积试剂
- 模板: `Add <volume> of <reagent_name>.`
- 例句: b. Add the cDNA Release Mix (volume: 400 μL/chip).

### 按照指定程序反应
- 模板: `Incubate for <time> at <temperature> in <device_name>.`
- 例句: d. Add TR Buffer (400 μL / chip), then place it on the PCR adapter of the PCR instrument (55℃) and incubate for 10 min;

### 移除上清/弃去液体
- 模板: `Aspirate and discard the <solution_name> from <location>.`
- 例句: c. Slightly tilt the handheld carrier and use a pipette to aspirate and discard the RT Mix from the chip surface from one corner.

### 离心与静置
- 模板: `Briefly centrifuge, then place on a magnetic stand for <time>.`
- 例句: 2) After brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min;

### 磁珠清洗
- 模板: `Add <volume> of 80% ethanol and wash the magnetic beads by rotating the tube.`
- 例句: 4) While keeping the centrifuge tube on the magnetic stand, add 1 mL of 80% ethanol (use freshly prepared 80% ethanol equilibrated to room temperature), rotate the centrifuge tube on the magnetic stand...

### 空气干燥磁珠
- 模板: `Air-dry at room temperature for <time> until <condition>.`
- 例句: 6) Keep the centrifuge tube on the magnetic stand and air-dry at room temperature for 5-8 min, until the surface of the magnetic beads is non-reflective and crack-free;

### 回溶与收集
- 模板: `Add <volume> of <buffer_name> to resuspend, then transfer the supernatant to <new_container>.`
- 例句: 7) Add 22 μL of Nuclease-Free Water to resuspend, vortex to mix, incubate at room temperature for 5 min, centrifuge briefly, magnetic stand stand for 3-5 min, until the liquid becomes clear;

### 提前准备事项
- 模板: `For this step, <action> in advance.`
- 例句: For this reaction step, refer to Table 3-3 to prepare the cDNA Release Mix in advance.

### 实验操作指令 (Imperative Procedure)
- 模板: `Take <Quantity> of the <Sample>, measure the <Metric> using the <Method/Tool>, and <Action>.`
- 例句: Take 1 µL of the cDNA sample, measure the concentration using the Qubit dsDNA HS Kit, and record the result.

### 条件存储说明 (Passive Storage Instruction)
- 模板: `The <Product> can be stored at <Temperature> for <Duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### 性能要求描述 (Requirement Specification)
- 模板: `The <Feature> of the <Object> is required to be <Condition/Value> (as shown in <Reference>).`
- 例句: The main peak of the fragment distribution is required to be at 1000–1500 bp (as shown in Figure 2).

### 文档引用指引 (Referential Instruction)
- 模板: `For <Specifics> of <Process>, please refer to the "<Document Title>".`
- 例句: For specific procedures for subsequent library construction, please refer to the "Stereo-seq Library Preparation Kit User Manual".

### 用途声明/限制 (Disclaimer)
- 模板: `This <Product/Service> is for <Purpose> only, not for <Prohibited Purpose>.`
- 例句: This product is for research use only, not for diagnostic use.

### 知识产权/禁止条款 (Prohibition)
- 模板: `Without the written consent of <Organization>, no one shall <Verb1>, <Verb2>, or <Verb3> without authorization.`
- 例句: Without the written consent of this unit, no one shall use, modify, reproduce, or disclose them without authorization.

### 提示信息 (Tip/Prompt)
- 模板: `Tip: Please <Action1> and <Action2> with the <Corresponding Item>.`
- 例句: Tip: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 关键步骤/警示 (Criticality/Warning)
- 模板: `<Category>: Pay special attention to <Target>, as <Risk Reason>.`
- 例句: Critical Step: Pay special attention to these steps to avoid experimental failure or undesirable outcomes.

### 信息汇总引用 (Cross-reference)
- 模板: `For further information regarding <Topic>, see <Reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., see Table 1-1 to Table 1-5.

### Catalog Number Statement
- 模板: `<Product Name> Cat. No.: <Number>`
- 例句: Stereo-seq Chip P Carrier (1 cm * 1 cm) Cat. No.: 200CP118

### Storage Condition Statement
- 模板: `Storage temperature: <Temperature_Range>`
- 例句: Storage temperature: -25°C to 8°C

### Validity Period Statement
- 模板: `<Condition> validity period: See label.`
- 例句: Cold chain transport validity period: See label.

### Recommendation Instruction
- 模板: `It is recommended to <Action>.`
- 例句: It is recommended to preheat the PCR thermal cycler to the reaction temperature.

### General Directive
- 模板: `Please <Action>.`
- 例句: Please read this manual before use.

### Selection Instruction
- 模板: `Select <Item> from the listed <Category> (marked with *).`
- 例句: Select any one from the listed brands (marked with *).

### Default Condition Specification
- 模板: `Unless otherwise specified, <Substance/Method> is used for <Process>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids intended for reagent dilution in this experiment.

### Safety Warning
- 模板: `Avoid direct contact of <Substance> with <Body_Part>; do not <Prohibited_Action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### Disposal Instruction
- 模板: `All <Material> should be disposed of in accordance with relevant regulations.`
- 例句: All samples and various wastes should be disposed of in accordance with relevant regulations.

### 分步操作描述
- 模板: `Remove <item> from <source>, <action1> and <action2>, then <action3> and store at <temperature>.`
- 例句: Remove 4% PFA from -20°C, thaw and mix well, then aliquot into 2 mL per tube and store at -20°C.

### 添加与混合操作
- 模板: `Add <amount> of <reagent> to <volume> of <buffer> (minimum volume per chip is <amount>); <action>.`
- 例句: For Wash Buffer: take 105 μL of RI and add to 1995 μL of 0.1X SSC (minimum volume per chip is 2100 μL); keep on ice for

### 负面约束指令
- 模板: `Do not <action1>; <action2>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 实验预防说明
- 模板: `Avoid <action> during <process> to <prevent_consequence>.`
- 例句: Avoid tissue drying during the liquid changing process, and avoid touching the tissue and chip with the pipette or pipette tip.

### 仪器设置参数
- 模板: `Set <instrument> to <value> for <procedure> (lid temperature <value>).`
- 例句: Set in sequence: 37°C for slide baking and permeabilization (lid temperature 42°C)

### 即时操作与孵育
- 模板: `Immediately add <reagent> at <dosage>, and incubate at <temperature> for <duration>.`
- 例句: Immediately add Wash Buffer at 400 μL/chip and incubate at room temperature for 1 min;

### 添加试剂
- 模板: `Add <volume> of <substance> per <container>;`
- 例句: Add 150 μL of mock secondary antibody incubation solution per chip;

### 操作姿态（倾斜）
- 模板: `Slightly tilt the <object> at an angle of <condition>, and use a pipette to <action>;`
- 例句: Slightly tilt the handheld carrier at an angle of less than 20°, and use a pipette to aspirate the Wash Buffer;

### 实验前准备指令
- 模板: `According to [<reference>], <action> in advance;`
- 例句: According to [Pre-experiment preparation], thaw the RT QC Reagent, RT Additive, and RT QC Enzyme in advance;

### 设备参数设置
- 模板: `Set the <instrument> <parameter> to <value> in advance;`
- 例句: Set the PCR instrument temperature to 70°C and the heated lid temperature to 75°C in advance;

### 期间衔接操作
- 模板: `During <event>, <action>;`
- 例句: During the incubation period of the primary antibody, prepare the mock secondary antibody incubation solution;

### 试剂使用限量
- 模板: `Preheat only the amount of <reagent> needed for use; do not <action>;`
- 例句: Preheat only the amount of Decrosslinking Reagent needed for use; do not repeatedly preheat.

### 后续操作衔接
- 模板: `After <event> is complete, <action>;`
- 例句: After the cooling is complete, slightly tilt the handheld carrier;

### 移液冲洗
- 模板: `Gently pipette <substance> up and down <number> times, then aspirate and discard the <substance>;`
- 例句: Gently pipette the 0.1X SSC solution up and down around the chip approximately 5 times, then aspirate and discard the 0.1X SSC solution;

### 按指南制备
- 模板: `Prepare <substance> according to <reference>;`
- 例句: Prepare the Total RNA Hybridization Mix according to Appendix Table 1;

### 禁止行为
- 模板: `<action_subject> are prohibited.`
- 例句: Folder names should only contain letters, numbers, and underscores; special characters such as spaces are prohibited.

### 参考执行
- 模板: `Refer to <reference> to <action>;`
- 例句: Refer to Chapter 3 of the "Stereo-seq Chip Carrier and Accessories Instruction Manual" to disassemble the handheld carrier,

### 操作指令模板
- 模板: `Please <verb> the <object> and use it with the <description>.`
- 例句: Note: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 更名说明模板
- 模板: `<Item> has been renamed to <NewName>.`
- 例句: 0.1X SSC (containing 5% RI) has been renamed to Wash Buffer

### 参数变更模板
- 模板: `<Parameter> changed from <val1> to <val2>.`
- 例句: Methanol pre-cooling time changed from 10-30 min to 5-30 min

### 条件性操作建议模板
- 模板: `If <condition> is <state>, the <parameter> can be extended, not exceeding <limit>.`
- 例句: If tissue removal is incomplete, the removal time can be extended, not exceeding 16 hr

### 文档引用与参考模板
- 模板: `For further information regarding <topic>, please refer to <source>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-4.

### 产品接收后指引模板
- 模板: `After receiving the <object>, please refer to the <guideline> to store the product.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to store the product.

### 存储条件标识模板
- 模板: `Storage temperature: <temperature>.`
- 例句: Storage temperature: −25℃~ −18℃

### 产品组成介绍模板
- 模板: `Each reagent kit consists of the following three parts:`
- 例句: Each reagent kit consists of the following three parts:

### 关键风险提示模板
- 模板: `Note: Pay close attention; improper handling or negligence may result in experimental failure.`
- 例句: Note: Pay close attention; improper handling or negligence may result in experimental failure.

### 实验暂停点说明模板
- 模板: `Stopping point: You may pause the experiment here and store the samples.`
- 例句: Stopping point: You may pause the experiment here and store the samples.

### 步骤描述（祈使句）
- 模板: `<verb> <object> <preposition phrase>`
- 例句: Remove the fixture and gasket from the Stereo-seq carrier accessory kit;

### 条件性操作指令
- 模板: `Ensure <object> <status/position>, <preposition> <object> <state>`
- 例句: ensuring that the hole cutouts of the fixture and gasket are aligned.

### 预防性/警示性指令
- 模板: `Avoid <action> <object>, <verb> <negative condition>`
- 例句: avoiding contact between the fixture or gasket and the chip surface;

### 建议/推荐用语
- 模板: `It is recommended to <verb> <object> <time/frequency>`
- 例句: It is recommended to preheat the PCR thermal cycler to the reaction temperature.

### 禁令/严禁事项
- 模板: `<subject> must not be <verb> <condition>`
- 例句: Resealed chips must not be stored for more than two weeks.

### 区分/识别方法
- 模板: `<subject> can be distinguished by <method>`
- 例句: The Stereo-seq chip P carrier and the Stereo-seq chip T carrier can be distinguished by the tags photolithographed on them.

### 必要条件限制
- 模板: `<subject> should not exceed <measurement/value>`
- 例句: The tissue dimensions should not exceed 0.9 cm × 0.9 cm × 2 cm

### 参考引用句式
- 模板: `Refer to <figure/section>.`
- 例句: Refer to Figure 1. Electropherogram of RNA RIN value in mouse brain tissue sections.

### 存储要求说明
- 模板: `<subject> must be stored at <temperature>`
- 例句: unopened Stereo-seq chip P/T carriers must be stored at −20℃ or 4℃.

### 祈使句操作步骤
- 模板: `<verb> <object> (optionally: <prepositional_phrase>)`
- 例句: Place the pre-cooled metal embedding cassette B (acting as a lid) with its opening facing upward.

### 条件触发动作
- 模板: `If <condition>, <verb> <object>.`
- 例句: If the tissue block is completely solidified and has turned white and opaque, gently pry the sides of the metal embedding cassette A.

### 后续动作衔接
- 模板: `After <action>/<duration>, <verb> <object>.`
- 例句: After freezing for 5 minutes, remove the metal embedding mold B.

### 试剂配制/步骤说明
- 模板: `Prepare <target> by <verb_ing> <substance>.`
- 例句: Prepare Wash Buffer by adding 5 μL of RI to 95 μL of 0.1X SSC.

### 参数设定/推荐
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to aliquot the prepared 10X Permeabilization Reagent stock solution.

### 实验前提/规范
- 模板: `<subject> must be <adjective>/<past_participle> before use.`
- 例句: 0.01N HCl (pH = 2.0) must be freshly prepared before use.

### 持续状态/保存建议
- 模板: `Keep <object> on <condition>.`
- 例句: Keep on ice.

### 连续步骤衔接
- 模板: `Repeat steps <step_number> through <step_number> until <condition>.`
- 例句: Repeat steps 2) and 3) until all tissue sections are adsorbed onto the chip surface.

### 直接操作指令
- 模板: `Add <amount> of <object> to the <location>.`
- 例句: Add 150 μL of 1X permeabilization reagent to the chip.

### 遵循参考指令
- 模板: `<Verb> <object> according to <reference>.`
- 例句: Prepare the Total RNA hybridization Mix according to Table 3-1.

### 动作加方式描述
- 模板: `Slightly tilt the <location>, and use a <tool> to <action> <object>.`
- 例句: Slightly tilt the handheld carrier, and use a pipette to aspirate and discard the RT QC Mix from the chip surface.

### 提前配置与设置
- 模板: `Set <instrument> to <condition> in advance, and <action> to <condition>.`
- 例句: Set the PCR instrument temperature to 55°C and the hot lid temperature to 60°C in advance, and place the PCR adapter to equilibrate temperature.

### 图表引用
- 模板: `As shown in [Figure/Table X], ...`
- 例句: As shown in Figure 3, at 3 min of permeabilization, the tissue exhibited uneven brightness within the same cortex, indic

### 参考指向
- 模板: `For details, please refer to [Document/Section].`
- 例句: For details, please refer to 《Stereo-seq 16 Barcode 建库试剂盒 V1.0 使用说明书》.

### 组成结构描述
- 模板: `Each [Product/Component] consists of the following [number] parts:`
- 例句: Each reagent set consists of the following three parts:

### 流程参数说明
- 模板: `The input parameters for the [pipeline name] are:`
- 例句: The input parameters for the SAW analysis pipeline adapted for spatiotemporal transcriptomics FFPE are:

### 表格标题结构
- 模板: `Table [Table No.] [Product Name] [Component Type] information`
- 例句: Table 1-1 Stereo-seq Transcriptomics Kit N reagent component information

### 非包含项声明
- 模板: `[Component] is not included in the [Product/Kit].`
- 例句: The Stereo-seq 16 Barcode Library Preparation Kit V1.0 is not included in the reagent kit.

### 未经授权禁止条款
- 模板: `Without [Organization]'s written consent, no one shall [Verb] ...`
- 例句: Without our unit's written consent, no one shall, without authorization, use, modify, copy, publicly disseminate, alter, distribute, or publish the

### 参数定义
- 模板: `<Parameter>: <Value>`
- 例句: Storage temperature: −25°C to −18°C. Expiration date: See label.

### 试剂溶解指令
- 模板: `Dissolve <Component> with <Volume> of <Solvent> and mix by pipetting.`
- 例句: Dissolve the PR Enzyme (red cap, in powder form) with 1 mL of freshly prepared 0.01N HCl and mix by pipetting

### 引用文档指令
- 模板: `Please refer to the "<Document Name>" to <Action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product.

### 推荐操作建议
- 模板: `It is recommended to <Action> <Component> <Time/Condition>.`
- 例句: It is recommended to take out all reagent components in advance before use.

### 预防措施指令
- 模板: `To avoid <Problem>, <Action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filtered pipette tips and change tips when aspirating different samples.

### 安全禁令
- 模板: `Avoid <Hazardous Action>; do not <Action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 试剂处理步骤
- 模板: `Take out <Component> from <Condition> in advance, equilibrate to <Condition>, and <Action>.`
- 例句: Take out TE Buffer (pH 9.0) from 4℃ in advance to equilibrate to room temperature (≤ 2 hr at room temperature).

### 试剂预处理操作
- 模板: `Remove/Take out the <reagent> from <temperature>, <action1>, <action2>, and <action3>.`
- 例句: Remove the FFPE RT Buffer Mix from -20°C in advance, thaw at room temperature, shake until no precipitate remains, and keep on ice during use.

### 建议操作规范
- 模板: `It is recommended that <procedure> be performed by <person/condition>.`
- 例句: It is recommended that this procedure be performed by an experienced paraffin section technician.

### 流程参考指引
- 模板: `For <details>, see <document/section>.`
- 例句: For precautions, see "Spatial Experiment Sample Preparation Guidelines".

### 条件分支操作
- 模板: `If <condition> is selected, please <action1> and <action2>.`
- 例句: If opting for H&E staining, please follow Section 2.3.1 for experimental procedures and skip Section 2.3.2.

### 状态触发操作
- 模板: `When <condition>, <action>.`
- 例句: When the wax block consists of high-fat tissue (such as breast tissue), the block can be placed in a -20°C freezer for 10 min.

### 储存条件说明
- 模板: `Store the <item> at <temperature> until <deadline>.`
- 例句: When unopened, the product can be stored at -20 °C or 4 °C until the expiration date on the label.

### 设备替代说明
- 模板: `If <equipment> is unavailable, <alternative> can be used.`
- 例句: If an integrated slide flotation/drying workstation is unavailable, a slide flotation water bath combined with a PCR instrument can be used.

### Procedural Instruction
- 模板: `<verb> <object>, then <verb> <object>.`
- 例句: Place the unused Stereo-seq chip into the transparent chip box, then put it back into the original aluminum bag.

### Pre-check Instruction
- 模板: `Please <verb> the following items after <action>.`
- 例句: Please check the following items after opening the aluminum bag:

### Purpose-driven Statement
- 模板: `To ensure <purpose>, <subject> <be_verb> <adverb>.`
- 例句: To ensure stability during transport, large chips are adhered securely to the bottom of the transparent chip box.

### Numbered Step
- 模板: `Step <number>: <verb> <object> <location>.`
- 例句: Step 1: Click the guide type you want to view in the checkbox column on the right side of the page.

### Reagent Preparation
- 模板: `<substance> <verb> from <condition> in advance, equilibrate to <condition>.`
- 例句: Hematoxylin (Solarbio, G4470) Take out from 4°C in advance, equilibrate to room temperature-

### Volume Guideline
- 模板: `Pour into <container>, the volume should be sufficient to <action>.`
- 例句: Use directly, pour into 2 staining jars (Histo-clear ① & ②). The volume should be sufficient to completely submerge the...

### Prohibition Constraint
- 模板: `<subject> should not be <action> for more than <duration>, and please <action> after <timeframe>.`
- 例句: Non-vacuum-sealed chips should not be stored for more than two weeks, and should be used as soon as possible after opening.

### Preparation
- 模板: `Take out the <reagent> from <temp> in advance and equilibrate it to room temperature for <purpose>.`
- 例句: Take out the FFPE Mounting Medium from -20°C in advance and equilibrate it to room temperature for mounting.

### ReagentMixing
- 模板: `Add <amount> of <reagent> to <reagent/vessel>, mix well, and transfer to <container>.`
- 例句: Add 20 mL of 70% ethanol to 10 mL of Eosin (Abcam 'AB246824'), mix well, and transfer to a staining jar, slide box, or 50 mL centrifuge tube.

### RinseSequence
- 模板: `Immerse the <object> in <container> containing <reagent>, and rinse by <action>.`
- 例句: Immerse the carrier in a staining jar (or slide box, or 50 mL centrifuge tube) containing 5X SSC, and rinse by moving up and down 5 times.

### NegativeWarning
- 模板: `Do not <action> the <reagent>, as this can <consequence>.`
- 例句: Do not preheat the TE buffer, as this can easily cause section detachment.

### ConditionalAction
- 模板: `If <condition> fails, please <action> to ensure <goal>.`
- 例句: If QC fails, please carefully check the image clarity, adjust the imaging method, and retake the photos to ensure clear organization and Track line images.

### StepTiming
- 模板: `When the <machine> reaches the <step>, <action>.`
- 例句: When the PCR machine runs to the 85°C ∞ step, place the handheld carrier onto the PCR adaptor, click Edit and click Next Step to skip the 85°C ∞ step.

### AddReagent
- 模板: `Add <amount> of <reagent> into the <container>, and <action>.`
- 例句: Add 400 μL of TE Buffer (pH 9.0), equilibrated to room temperature, into the wells of the carrier chip, and incubate for 1 min to wash, then aspirate and discard the liquid.

### ProceedInstruction
- 模板: `Immediately after this step is completed, proceed with <action>.`
- 例句: Immediately after this step is completed, proceed with subsequent experiments according to 2.4 Fixing.

### SimpleTakeAndAdd
- 模板: `Take an appropriate amount of <reagent> and add it to <container> for <action>.`
- 例句: Take an appropriate amount of absolute ethanol and add it to a 6 cm or 9 cm petri dish for washing coverslips.

### 操作步骤指令
- 模板: `<imperative_verb> <object> <complement/location/duration>`
- 例句: Remove the Stereo-seq chip N carrier, place it in the 60°C slide dryer, and bake for 1 hr

### 操作命令
- 模板: `<imperative_verb> <object> <method/condition>`
- 例句: Aspirate and discard the ssDNA staining solution, add 150 μL 0.1X SSC dropwise onto the chip

### 实验要求/条件声明
- 模板: `The <object> must pass <QC_process> before <next_step> can be conducted.`
- 例句: The obtained ssDNA staining image must pass QC before further image analysis (register) can be conducted.

### 试剂处理指令
- 模板: `Remove <reagent> from <temperature> in advance and equilibrate to <target_temperature>`
- 例句: Remove FFPE Mounting Medium from -20°C in advance and equilibrate to room temperature

### 试剂添加
- 模板: `Add [Quantity] of [Reagent] to [Target], [Action1], and [Action2].`
- 例句: Add 400 μL of FFPE Decrosslinking Reagent to the wells of the carrier chip, apply the sealing film, and seal

### 位置放置与转移
- 模板: `Place/Transfer [Object] [onto/to] [Target].`
- 例句: Place the handheld carrier onto the PCR adaptor

### 试剂配制衔接
- 模板: `Prepare [Reagent] (in advance/just before use): [Method].`
- 例句: Prepare 1X permeabilization reagent working solution (prepare just before use): use 0.01N HCl to dilute the 10X reagent.

### 移除与废弃
- 模板: `Remove [Object] and discard [Waste].`
- 例句: Remove the holder and discard the gasket and clamp.

### 程序参数标题
- 模板: `Table [Number] [Subject] settings.`
- 例句: Table 2-3 De-crosslinking program settings

### 注意事项提示
- 模板: `[Subject] [Result/Reason]; it must be [Action].`
- 例句: The fixture will deform after being heated to 95°C...; it must be discarded.

### 用量与规格限制
- 模板: `[Object] ([Quantity]/[Unit]).`
- 例句: 0.1X SSC (containing 5% RI)

### 操作指令-添加试剂
- 模板: `Add <reagent_name> (volume: <dosage>), <action_1>, and <action_2>.`
- 例句: Add cDNA Release Mix (volume 400 μL / well), seal the wells with sealing film, and then place on

### 孵育与条件限制
- 模板: `Incubate at <temperature> for <time> (can be held for up to <max_time>).`
- 例句: and incubate at 55℃ for 5 hr (can be held for up to 24 hr)

### 条件判断与处理
- 模板: `If <condition> is observed, <action_1>, and then allowed to <action_2>.`
- 例句: If white precipitate is observed in the buffer, it can be incubated at 55°C to dissolve, and then allowed to return to room temperature.

### 防止操作误差
- 模板: `Be careful not to <negative_action>; you may <action_for_buffer> to avoid <risk>.`
- 例句: Be careful not to touch the magnetic beads with the pipette tip; you may leave 2-3 μL of liquid to avoid aspirating the magnetic beads.

### 步骤衔接与检查
- 模板: `Once <condition>, <action>.`
- 例句: Once the liquid clears, carefully remove the supernatant with a pipette.

### 溶剂补足与校准
- 模板: `If <substance> is less than <volume>, make up the volume to <volume> with <solvent>.`
- 例句: If the recovered sample above is less than 42 μL, make up the volume to 42 μL with NF-H2O.

### 磁珠漂洗操作
- 模板: `Keep the centrifuge tube on the magnetic rack and add <volume> of <solvent>, <action_to_wash>.`
- 例句: Keep the centrifuge tube on the magnetic rack and add 1.5 mL of 80% ethanol, rotate the centrifuge tube on the magnetic rack to wash the beads.

### 预防措施
- 模板: `Avoid <negative_action_1> that may cause <negative_result>, <action_for_stability>.`
- 例句: Avoid vigorous shaking that may cause magnetic beads or liquid to pop out, hold the middle or lower section of the 1.5 mL centrifuge tube, and then open the cap.

### 实验记录与核对
- 模板: `<Action_1> and <action_2> according to <reference_table> to measure and record <target_data>.`
- 例句: Prepare the Qubit dsDNA HS Kit according to Table 2-11 to measure and record the PCR product concentration.

### 步骤条件动作描述
- 模板: `After <action>, <verb> <object> and <verb> for <duration>`
- 例句: After a brief centrifugation, place the PCR tube on a magnetic rack and let it stand for 3 minutes;

### 混合与操作要求
- 模板: `Mix <component_A> with <component_B> at a <ratio> ratio, <action_1>, and <action_2>`
- 例句: Mix the PCR products (100 μL) with room-temperature equilibrated beads at a 1:1 ratio, vortex to mix, and incubate at

### 存储条件建议
- 模板: `<subject> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA products can be stored at −20°C for 1 month.

### 注意事项/限制说明
- 模板: `This product is for <use_case> only, not for <negative_use_case>.`
- 例句: This product is for research use only, not for diagnostic use.

### 物料/步骤变更提示
- 模板: `· <Action> <item_or_process> to <new_state>;`
- 例句: · Shipping for kits and chips has been changed to cold chain transportation;

### 状态变化描述
- 模板: `<subject> until <condition>`
- 例句: air-dry at room temperature for 5-8 min until the surface of the beads is free of reflection and cracking;

### 对应关系描述
- 模板: `<subject> corresponding to <condition>`
- 例句: Fragment distribution of purified cDNA product corresponding to RNA with DV200 < 30%

### 通用标题/章节格式
- 模板: `<Chapter_Number> <Section_Title>`
- 例句: Chapter 1: Product Introduction

### 引用说明
- 模板: `For <details/further information>, please refer to <reference>.`
- 例句: For details, please refer to Library Kit Instruction Manual.

### 套装组成
- 模板: `Each <kit/reagent> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 产品功能描述
- 模板: `The <product> is used for <purpose>.`
- 例句: The STOmics Stereo-seq Customized Chip Transcriptome Reagent Kit is used for the construction of 3' end libraries from whole-transcriptome.

### 风险提示
- 模板: `Note: Pay special attention; <condition> may lead to <consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 质量保证描述
- 模板: `<Subject> have undergone <process>, ensuring <outcome>.`
- 例句: All reagents provided in this kit have undergone rigorous quality control and functional validation, ensuring to the greatest extent the stability and reproducibility of library preparation.

### 可选操作
- 模板: `You may choose any of the listed <items> (marked with *) for use.`
- 例句: You may choose any of the listed brands (marked with *) for use.

### 信息查阅
- 模板: `For further information regarding <topic>, please refer to <reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 and Table 1-2.

### 实验建议
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 目的驱动建议
- 模板: `To <purpose>, it is recommended to <action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filter pipette tips and change tips when aspirating different samples.

### 祈使指令
- 模板: `Before <action>, please <command>.`
- 例句: Before conducting the experiment, please familiarize yourself with the precautions for all instruments to be used.

### 产品用途声明
- 模板: `This product is intended for <usage> only and not for <prohibited_use>.`
- 例句: This product is intended for research use only and not for clinical diagnostic purposes; please read this manual carefully.

### 规避指令
- 模板: `Avoid <action>.`
- 例句: Avoid direct skin and eye contact with samples and reagents, and do not swallow samples or reagents.

### 规格限制
- 模板: `The <object> should not <condition> <value>.`
- 例句: The tissue size should not exceed 0.9 cm × 1.8 cm × 0.7 cm.

### 合规性处理
- 模板: `<subject> should be <action> in accordance with <regulations>.`
- 例句: All samples and various wastes should be disposed of in accordance with relevant regulations.

### 前置准备
- 模板: `<verb> <object> in advance.`
- 例句: Prepare a foam box of crushed ice in advance and pre-cool the OCT on ice for 10 min.

### Imperative Action with Manner/Location
- 模板: `<verb> <object>, <manner/location>.`
- 例句: Place the metal embedding cassette A, containing the tissue, horizontally on a metal block precooled with dry ice;

### Reagent Preparation and Dosage Constraint
- 模板: `Add <quantity> of <reagent_a> to <quantity> of <reagent_b>, requiring at least <dosage_per_unit>.`
- 例句: Add 7.5 μL of RI to 142.5 μL of 0.1X SSC, requiring at least 150 μL/chip.

### Verification/Inspection
- 模板: `Check whether <object> has <status_completed>.`
- 例句: Check whether the OCT has completely solidified and turned white and opaque;

### Pre-treatment with Time Constraint
- 模板: `Remove <object> from storage at least <time> before use and <action_condition>.`
- 例句: Remove from storage at least 5 minutes before use and equilibrate to room temperature.

### Sequential Steps with Risk Prevention
- 模板: `First, <verb> <action_a> (to prevent <risk>), then <verb> <action_b> <manner>.`
- 例句: First, place the pre-chilled steel ruler on the long side of metal embedding cassette A (to prevent the tissue from being deformed), then place metal embedding cassette B with the opening facing upward.

### General Rule / Disclaimer
- 模板: `Unless <condition>, <imperative_verb> <action>.`
- 例句: Unless otherwise specified, use Nuclease Free Water for liquids used to dilute reagents in this experiment.

### Reference to Prior Step
- 模板: `Same as <reference_step>.`
- 例句: Same as for 1*2 chips; room temperature for 1 day.

### 指令式操作
- 模板: `Immediately <verb> <object> into/onto <location> to <action> for <duration>.`
- 例句: Immediately place the chip dried in the previous step into methanol pre-cooled at -20°C to fix for 40 min.

### 序贯式操作
- 模板: `After <condition>, <verb> <object> to <location>.`
- 例句: After fixation, transfer the 6-well plate/6 cm culture dish to a fume hood;

### 条件判定与处理
- 模板: `If <condition>, <verb> <object>.`
- 例句: If there are impurities on the chip, use 3000 μL of Nuclease for 1 cm * 2 cm and 2 cm * 2 cm chips in a 6-well plate

### 文档索引参考
- 模板: `Refer to <table_or_doc> for <parameter>.`
- 例句: refer to Table 3-1 for the baking time;

### 试剂用量表达
- 模板: `Add <amount> of <reagent> to <object>.`
- 例句: Add the tissue fluorescent staining solution to the chip; refer to Table 3-2 for the amount.

### 准备就绪状态判定
- 模板: `When <condition>, it is ready for <step>.`
- 例句: When there is no liquid residue and no ripple-like texture, it is ready for mounting;

### Conditional Requirement
- 模板: `<Subject> must <verb> before <action> can be performed. If <condition> fails, <next_step>.`
- 例句: The obtained ssDNA staining images must pass QC before further image analysis (register) can be performed. If QC fails,

### Imperative Sequence
- 模板: `<Verb> the <object> to <action>, then <verb> in a <container>.`
- 例句: Remove the chip and place it on lint-free paper to blot dry the moisture on the back, then place it in a 9 cm petri dish

### Volume Reference
- 模板: `<Action> the <solution> (refer to Table <number> for volume);`
- 例句: Add PR Rinse Buffer solution (containing 5% RI, refer to Table 3-8 for volume);

### Procedural Avoidance
- 模板: `Please do not <action> for an extended period; turn off <device> when not <action> to avoid <negative_outcome>.`
- 例句: During imaging, please do not expose the chip with the attached tissue to fluorescence for an extended period; turn off laser when not imaging, to avoid

### Sequence-Based Action
- 模板: `While <action_in_progress>, <verb> the <reagent> according to Table <number> and keep it on ice.`
- 例句: While waiting for permeabilization, prepare the RT Mix according to Table 3-7 and keep it on ice;

### Immediate Action
- 模板: `Immediately <action> to <reason>.`
- 例句: Immediately add RT Mix to avoid RNA degradation.

### 条件触发操作
- 模板: `If <condition> is observed in <object>, <verb> by <action>.`
- 例句: If white precipitate is observed in the buffer, it can be dissolved by incubating at 55°C.

### 建议与备注
- 模板: `<action> in advance to <purpose>.`
- 例句: Remove from 4°C 30 minutes in advance, vortex to mix, and equilibrate to room temperature to help ensure recovery efficiency.

### 步骤衔接（动作序列）
- 模板: `<verb> <object> according to <reference>, and <verb> at <condition>.`
- 例句: Prepare the cDNA Release Mix according to Table 3-13 and incubate at room temperature.

### 禁止/注意事项
- 模板: `<verb> <action> to <purpose>.`
- 例句: Prevent the chip from drying out completely.

### 用量/规格表达
- 模板: `<volume>/<unit>.`
- 例句: 1500 μL/chip

### 防止干扰/保护
- 模板: `<verb> <object> to prevent <action>.`
- 例句: Wrap the outside of the 6-well plate with plastic wrap to prevent evaporation.

### 纯化/处理过程
- 模板: `After <action> is completed, <verb> the liquid in the reaction well into a <container>.`
- 例句: After the reaction is completed, completely recover the liquid in the reaction well into a 15 mL centrifuge tube.

### 磁珠操作细节
- 模板: `When <action>, <verb> <object> to ensure <status>.`
- 例句: Before each use, shake or pipette the magnetic beads up and down to ensure they are thoroughly mixed.

### 条件执行与补足
- 模板: `If the volume of <object> is less than <value>, bring the volume to <value> with <reagent>.`
- 例句: If the volume of the recovered sample above is less than 42 μL, bring the volume to 42 μL with Nuclease-Free Water.

### 离心与放置规范
- 模板: `Briefly centrifuge, place on a magnetic stand for <time> until the liquid becomes clear.`
- 例句: Briefly centrifuge, place on a magnetic stand for 3-5 min until the liquid becomes clear.

### 移液操作限制
- 模板: `The pipette tip should be operated against the tube wall away from the magnetic rack; do not pipette up and down or disturb the magnetic beads.`
- 例句: The pipette tip should be operated against the tube wall away from the magnetic rack; do not pipette up and down or disturb the magnetic beads.

### 存储与保留条件
- 模板: `After <action>, the <product> can be stored in <volume> of <reagent> at <temperature> until <condition>.`
- 例句: After purification, the magnetic beads can be stored in 40 μL of Nuclease-free Water at 4℃ until the final cDNA product QC passes.

### 样本干燥观察
- 模板: `Air-dry at room temperature for <time>, until the surface of the magnetic beads shows no reflection.`
- 例句: Air-dry at room temperature for 5-8 min, until the surface of the magnetic beads shows no reflection.

### 样本处理与合并
- 模板: `Transfer the supernatant (<volume>) to <target> to combine for a total volume of <volume>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to the PCR tube shown in step 8 to combine for a total volume of 42 μL.

### 暂停点标记
- 模板: `(This step can be paused; store samples at <temperature>)`
- 例句: (This step can be paused; store samples at -20°C)

### 试剂定容
- 模板: `Add <reagent> to make up to <volume>`
- 例句: Finally, add 0.5X PBS to make up to the corresponding volume

### 步骤序列
- 模板: `First, <action>; Then, <action>; Finally, <action>.`
- 例句: First, prepare a 0.5X PBS solution; Then, weigh the sucrose and add it to a new 15 mL/50 mL centrifuge tube; Finally, add 0.5X PBS to make up to the corresponding volume

### 样本处置
- 模板: `Discard the <liquid>, add fresh <new_liquid>, and <action> at <temperature> for <time>.`
- 例句: Discard the liquid, add fresh pre-cooled 3% sucrose-PBS solution, and incubate at 4°C overnight.

### 材料处理步骤
- 模板: `<Verb> <material>, <action> immediately, and <action> at <temperature> for <time>.`
- 例句: Excise the plant material, immediately place it into pre-cooled Carnoy's fixative, and fix on ice or at -20°C for 1 hr.

### 条件性操作句式
- 模板: `If <condition>, please <verb>.`
- 例句: If using a higher magnification objective (≥20x) or higher numerical aperture (≥1.0), please consider the following:

### 否定限制/预防句式
- 模板: `Do not <verb> <object>, as this will <verb>.`
- 例句: Do not overfill the embedding cassette with tissue, as this will make sectioning difficult.

### 结果描述句式
- 模板: `<subject> will <verb> <adverb>.`
- 例句: After adding sucrose to 0.5X PBS, the volume will change slightly.

### 定义/说明句式
- 模板: `<subject> is <definition>.`
- 例句: The depth of focus is the thickness of the sample that appears in focus within an image plane.

### 差异/对比句式
- 模板: `<subject1> will <verb>, <subject2> will <verb>.`
- 例句: The FOV will become smaller, requiring more FOVs to be acquired and stitched.

### 强制性要求句式
- 模板: `When <condition>, ensure that <subject> matches <object>.`
- 例句: When joint analysis of visualized gene expression data and tissue images is required, ensure that the resolution of the tissue images matches the resolution of the Stereo-seq technology.

### 文档导向句式
- 模板: `For <subject>, please refer to <reference>.`
- 例句: For applicable Stereo-seq solutions and their corresponding user manuals, please refer to the table below.

### 操作指令句
- 模板: `<verb> <object> to <action>.`
- 例句: Gently place the chip on the stage, ensuring it is correctly oriented.

### 条件要求句
- 模板: `If <condition>, <action/recommendation>.`
- 例句: If a larger chip size is required, please confirm the microscope scanning range in advance.

### 必备项说明
- 模板: `<item>: <quantity/detail>.`
- 例句: OCT/FFPE tissue embedding block: 1

### 步骤衔接/参考
- 模板: `For <detail>, please refer to <document_name>.`
- 例句: For details on the assembly, disassembly, and usage of the carrier chip, please refer to the "Stereo-seq Chip Carrier and Accessories User Manual".

### 专业建议句
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to consult the microscope manufacturer to confirm and complete calibration and debugging.

### 功能描述句
- 模板: `<Subject> should <action> <object>.`
- 例句: Camera resolution should match the theoretical resolution of the objective lens.

### 参数/指标定义
- 模板: `<Parameter> must be <value/constraint>.`
- 例句: The scanning area must cover at least 10*10 mm.

### 禁止操作句
- 模板: `Do not <action> <object> before <event>.`
- 例句: Please do not modify any parameters arbitrarily before the formal experiment.

### 故障排查建议
- 模板: `If <issue> occurs, <action> to <purpose>.`
- 例句: If the color deviates significantly from expectations, please contact the microscope manufacturer's engineer for debugging.

### 范围约束句
- 模板: `<Subject> should be kept <adjective> <location>.`
- 例句: The chip should be kept as parallel as possible to the stage.

### 建议/指令表达 (Instruction)
- 模板: `Please <verb> the <object>.`
- 例句: Please immediately perform image QC using the StereoMap software.

### 条件语句 (Conditional Clause)
- 模板: `If <condition>, <instruction>.`
- 例句: If using manual focus, you should select modeling points and focus separately at the four corners.

### 推荐表达 (Recommendation)
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to pre-install the latest version of the StereoMap software.

### 限制/义务表达 (Requirement)
- 模板: `[Subject] should preferably <verb> <object>.`
- 例句: should preferably not exceed half the width of the field of view (FOV).

### 禁止事项 (Prohibition)
- 模板: `Do not <verb> the <object>.`
- 例句: Do not touch the surface where the microscope is placed during slide scanning.

### 注意事项 (Cautionary)
- 模板: `Please be cautious when <verb-ing> <object>, as <reason>.`
- 例句: please be cautious when using the autofocus mode, as most microscopes cannot accurately focus on the tracking lines.

### 参考引用 (Reference)
- 模板: `For <details>, please refer to <source>.`
- 例句: For download links, installation guides, etc., please refer to the StereoMap User Manual -> Download.

### 流程描述 (Procedural Description)
- 模板: `The above are <description>.`
- 例句: The above are general procedural precautions.

### Stitching Instruction
- 模板: `When stitching multiple FOVs into a large image, <action> is required to <purpose>.`
- 例句: When stitching multiple FOVs into a large image, subsequent feature registration is required to correct stitching errors.

### Cause and Effect
- 模板: `<Cause> can lead to <undesirable effect>.`
- 例句: Improper focusing can lead to the failure of Track detection.

### Structural Description
- 模板: `<Subject> are <definition>, and are generally <property>.`
- 例句: Track lines are straight lines arranged on the chip and are generally parallel to the chip edges.

### Image Quality Description
- 模板: `<Condition> images have <property 1> and <property 2>, resulting in <undesirable outcome>.`
- 例句: Underexposed images have low perceived brightness (low pixel values) and low contrast (low image dynamic range), which leads to details loss and resolution impairment.

### Actionable Tip
- 模板: `Please <action 1> and <action 2> with <item>.`
- 例句: Please download the latest version of the manual and use it with the corresponding kit version.

### Usage Restriction
- 模板: `This product is for <intended use>, not for <restricted use>.`
- 例句: This product is for research use only, not for diagnostic use.

### 产品/文档元数据
- 模板: `<label>: <value>`
- 例句: Catalog No.: 1000033700

### 操作指令(祈使句)
- 模板: `<verb> <object> from <source>`
- 例句: Remove the fixture and gasket from the Stereo-seq carrier accessory kit

### 建议/推荐操作
- 模板: `It is recommended to <action>`
- 例句: It is recommended to use filtered pipette tips

### 前置条件/预防措施
- 模板: `Please <action> before <event>`
- 例句: Please read this manual carefully before use

### 状态确认/验证
- 模板: `Ensure that <subject> <verb> securely`
- 例句: Ensure that the fixture and chip carrier are securely assembled together

### 外部引用说明
- 模板: `For further information regarding <topic>, refer to <reference>`
- 例句: For further information regarding the product catalog number and specific components of the carrier accessory kit, refer to Table 1-1

### 环境参数描述
- 模板: `<type> temperature: <value>`
- 例句: Storage temperature: 18°C~25°C

### 键值映射
- 模板: `<Key Name>: <Value>`
- 例句: Document Number: STOG00010

### 前提要求
- 模板: `Ensure <object> is <state> before <action>.`
- 例句: Ensure all reagents are thawed before use.

### 指引参考
- 模板: `Refer to <document> for <details>.`
- 例句: Refer to the user manual for details.

### 重要提示
- 模板: `Note: <information>.`
- 例句: Note: The temperature must be kept at 4°C.

### 工具使用
- 模板: `Use <tool> to <verb> <quantity> of <substance>.`
- 例句: Use a pipette to add 10 µL of sample.

## 自动蒸馏新增句式（2026-08-17）

### 请求式指令
- 模板: `Please <verb> <object> carefully before <event>.`
- 例句: Please read this manual carefully before installation.

### 禁止性警告
- 模板: `Do not <verb> <object> <condition>, as this may result in <risk>.`
- 例句: Do not remove the casing while the equipment is running, as this may result in electric shock.

### 条件式指令
- 模板: `If <condition>, please <verb> <object> immediately and <verb> <target>.`
- 例句: If abnormal noise is detected, please stop using it immediately and contact the after-sales service center.

### 时序动作指令
- 模板: `After <event>, please <verb> <object>.`
- 例句: After each use, please clean the lens surface with a soft cloth.

### 产品描述声明
- 模板: `The <noun> for this product is <value> from <time_reference>.`
- 例句: The warranty period for this product is twelve months from the date of purchase.

### 变更说明
- 模板: `<verb_past> <object>.`
- 例句: Added F RT to the Stereo-seq Plant Transcriptome Accessory Kit.

### 文档范围声明
- 模板: `This document serves as <noun_phrase>, aiming to <verb> <object>.`
- 例句: This document serves as general guidance and reference material, aiming to provide operational instructions and methodology.

### 用途免责声明
- 模板: `This product is for <usage>, not for <disclaimer>.`
- 例句: This product is for research use only, not for diagnostic use.

### Procedural Label
- 模板: `<Label>: <Description>.`
- 例句: Critical step: Pay special attention to these steps to avoid experimental failure or poor results.

### Reference Pointer
- 模板: `For further information on <topic>, see <Table/Reference>.`
- 例句: For further information on catalog numbers, reagent components, etc., see Table 1-1 to Table 1-5.

### Component Composition
- 模板: `The <Item> consists of the following <number> parts:`
- 例句: The Stereo-seq Transcriptomics Reagent Kit V1.3 (Substrate Version) consists of the following three parts:

### Storage Handling Instruction
- 模板: `Please store the product according to <conditions> as soon as possible.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### Attribute Declaration
- 模板: `<Attribute>: <Value>`
- 例句: Storage temperature: −25℃~ −15℃

### Compatibility Declaration
- 模板: `This <Document> is suitable for <Product>.`
- 例句: This operation guide is suitable for the Stereo-seq Transcriptomics Kit V1.3 (Chip)...

### Component Replacement Instruction
- 模板: `Replace <old_component> with <new_component> from <kit>.`
- 例句: In the plant transcriptome experiment, replace the two green-capped reagents with the black-capped reagents from the Stereo-seq plant transcriptome accessory kit.

### Section Header
- 模板: `<Number>. <Noun Phrase>`
- 例句: 3.2. Section Preparation

### 储存条件表达
- 模板: `Storage temperature: <temperature_range>`
- 例句: Storage temperature: 18°C~25°C

### 试剂/产品描述
- 模板: `<product_name>    Cat. No.: <catalog_number>`
- 例句: Stereo-seq Plant Transcriptome Auxiliary Kit    Cat. No.: 203KA12114

### 表格标题
- 模板: `Table <number>-<number> <title>`
- 例句: Table 1-6 User-supplied Instruments List

### 备选/等效设备表达
- 模板: `<instrument_name> <catalog_number> (or equivalent instrument)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or equivalent instrument)

### 操作建议/选择性操作
- 模板: `You may choose any one of the listed brands (marked with *) to use with the <adaptor_name>.`
- 例句: You may choose any one of the listed brands (marked with *) to use with the Stereo-seq PCR Adaptor.

### 条件性试剂使用说明
- 模板: `* <reagent_name> is a specialized reagent for <target_type>; use as needed.`
- 例句: * F RT Buffer Mix is a specialized reagent for fruit-bearing plants; use as needed.

### 耗材/设备列表备注
- 模板: `Tables <range> do not include standard laboratory equipment, such as <list_items>.`
- 例句: Tables 1-6 do not include standard laboratory equipment, such as ice machines, biosafety cabinets, pH meters, refrigerators, and balances.

### 安全与限制声明
- 模板: `• This product is for research use only, not for clinical diagnosis. Please read this manual carefully before use.`
- 例句: • This product is for research use only, not for clinical diagnosis. Please read this manual carefully before use.

### 实验前准备要求
- 模板: `• Before the experiment, please familiarize yourself with the precautions for all instruments to be used and master their operation methods.`
- 例句: • Before the experiment, please familiarize yourself with the precautions for all instruments to be used and master their operation methods.

### 上标/序号选择说明
- 模板: `Select any one from the brands with the same superscript<number>.`
- 例句: Select any one from the brands with the same superscript number.

### 推荐操作
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 条件指令（否定）
- 模板: `If <condition>, it is not recommended to <action>.`
- 例句: If the tissue detaches, proceeding with the formal experiment is not recommended.

### 目的驱动建议
- 模板: `To <purpose>, <action>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filter pipette tips.

### 提前设置指令
- 模板: `Set <parameter> in advance, and <instruction>.`
- 例句: Set the temperature of a metal bath to 37°C in advance, and set the PCR instrument program to 37°C for ∞.

### 合规性要求
- 模板: `<Item> shall be <action> in accordance with <regulation>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### 连续步骤衔接
- 模板: `<Action1>. After <event>, <action2>, and <action3>.`
- 例句: Thaw other components at room temperature. After thawing, gently invert several times to mix thoroughly, briefly centrifuge, and place on ice.

### 安全操作规程
- 模板: `Avoid <risk>. In the event of <accident>, <remedial_action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes. In the event of an accident, rinse immediately with plenty of water and seek medical attention promptly.

### 参考引用
- 模板: `Please refer to <document_name> for <task>.`
- 例句: Please refer to the Stereo-seq Plant Fresh Sample Embedding Guide for sample preparation.

### PreparationStep
- 模板: `To prepare <target_solution>, <verb> <quantity> of <source_solution> to <total_volume> with <solvent>, <verb> <method>, and <verb> <condition>.`
- 例句: To prepare 5X SSC, dilute 100 μL of 20X SSC to 400 μL with Nuclease-Free Water, mix well, and keep at room temperature.

### PreTreatment
- 模板: `<verb> <object> out from <temperature> in advance, <verb> at <temperature>, and <verb> until <condition>.`
- 例句: Take the RT Buffer Mix out from −20°C in advance, thaw at room temperature, and shake until no precipitate is observed.

### OperationalInstruction
- 模板: `<verb> <object> to <setting>.`
- 例句: Pre-cool the cryostat chamber to −20°C and the specimen head to −20°C.

### ConditionalStep
- 模板: `If <condition>, <verb> <action>.`
- 例句: If the chip surface is free of impurities, visible marks, liquid residue, or wavy patterns, you may proceed to prepare...

### NegativeInstruction
- 模板: `Do not <verb> <object>; <verb> by <method>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### Recommendation
- 模板: `It is recommended to <verb> <object> to <purpose>.`
- 例句: It is recommended to aliquot the prepared 10X permeabilization stock solution.

### StorageInstruction
- 模板: `<verb> at <temperature>, <condition>.`
- 例句: Store at room temperature, protected from light.

### PreCondition
- 模板: `Before <action>, <verb> <object>.`
- 例句: Before starting the experiment, check the PCR instrument for any abnormalities.

### 步骤执行指令
- 模板: `<verb> <object> (as required)`
- 例句: Select the objective lens as required

### 顺序与目的连接
- 模板: `<action>, <purpose_verb_phrase>`
- 例句: Centrifuge the mounting medium before use to ensure that it is free of air bubbles.

### 条件性操作指令
- 模板: `If <condition>, <action>`
- 例句: If autofluorescence is chosen, please follow the experimental procedures in section 3.5.1, and ignore section 3.5.2

### 注意事项/限制
- 模板: `Note: <instruction/warning>`
- 例句: Note: When performing cold mounting on multiple chips, the mounting time for each section must be strictly controlled

### 频率与耗时限制
- 模板: `<action>, <duration/frequency_limit>`
- 例句: Incubate at 37°C for 5 min

### 强制性否定指令
- 模板: `<subject> must not be <adjective/action> to avoid <consequence>`
- 例句: The pre-cooling time must not be too long to avoid water condensation on the slide surface

### 参照引用
- 模板: `Refer to <section>, <table_reference>, to <action_verb> <object> in advance`
- 例句: Refer to Section 3.7 Tissue Permeabilization, Table 3-2, to prepare 1X permeabilization reagent working solution in advance

### 状态确认
- 模板: `<action>, ensuring that <condition>`
- 例句: Quickly place the chip carrier into methanol pre-cooled to −20°C for fixation, ensuring that the methanol covers all chips

### 物料用量说明
- 模板: `(For <size> chips, the volume is <dosage>/chip)`
- 例句: (For 1 cm*1 cm chips, the volume is 150 μL/chip; for 0.5 cm*0.5 cm chips, the volume is 50 μL/chip).

### 并行步骤指令
- 模板: `<action_1>, while <action_2>`
- 例句: Carefully place one end of the coverslip on the edge of the chip while holding the other end

### 操作指令
- 模板: `<verb> <object> (e.g., <action>)`
- 例句: Add the RT Mix to one corner of the chip, with 200 μL/chip, ensuring the RT Mix covers the entire chip evenly;

### 步骤衔接（动作后）
- 模板: `After <action> is complete, <action>.`
- 例句: After imaging is complete, fix the Stereo-seq chip T-carrier with one hand...

### 条件要求
- 模板: `Once <condition>, click “<button_name>”.`
- 例句: Once the required number of points has been selected, click “End Point Selection”...

### 警告/禁止
- 模板: `Do not <action>.`
- 例句: During the point selection process, do not rotate the mechanical adjustment handwheel.

### 建议/提示
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to set the initial image save path on the local computer to improve upload speed.

### 用量表达
- 模板: `<action> <amount>/<unit_type> of <reagent>.`
- 例句: Add 150 μL/slide of 1X Permeabilization Reagent working solution onto the adapter.

### 引用参考
- 模板: `For <purpose>, please refer to <manual_name>.`
- 例句: For more specific microscope usage instructions, please refer to the "Go Optical Spatial Microscope Product Manual".

### 并行/后续动作
- 模板: `<action_1>, and <action_2>.`
- 例句: Take out RT Buffer Mix or F RT Buffer Mix in advance (select the specific reagent according to Section 3.8), and RT Plus and RT Oligo to thaw at room temperature.

### Quantity/Volume Addition
- 模板: `Add <Reagent>, <Volume>/chip;`
- 例句: Add cDNA Release Mix, 400 μL/chip;

### Procedural Step with Preparation
- 模板: `Prepare the <Mix> <Time> in advance according to <Table> and <Action>.`
- 例句: Prepare the cDNA Release Mix 5 minutes in advance according to Table 3-4 and let it stand at room temperature.

### Conditional Handling
- 模板: `If <Condition> is observed, <Action>.`
- 例句: If white precipitate is observed, it can be incubated at 55°C to dissolve.

### Instrumental/Procedural Action
- 模板: `After the <Reaction> is complete, <Action>.`
- 例句: After the reverse transcription reaction is complete, remove the handheld carrier from the PCR instrument (45°C);

### Magnetic Rack/Cleaning Procedure
- 模板: `Keep the <Item> on the <Rack>, <Action>.`
- 例句: Keep the centrifuge tube on the magnetic rack, add 1 mL of 80% ethanol.

### Pre-use Precaution
- 模板: `Before each use, <Action> the <Item> to ensure <Result>.`
- 例句: Before each use, vortex or pipette the magnetic beads up and down to ensure they are thoroughly mixed.

### Title Formatting
- 模板: `Table <Number> <Title> Preparation`
- 例句: Table 3-4 cDNA Release Mix Preparation

### Foam Management
- 模板: `If there is <Issue> on the <Location>, <Action>.`
- 例句: If there is foam on the cap, aspirate the foam.

### Step Completion/Repetition
- 模板: `Repeat steps <StepA>-<StepB> once.`
- 例句: Repeat steps f-g once;

### 混合操作描述
- 模板: `Mix <substance1> with <substance2> (e.g., if <condition>, add <amount> of <substance2>), vortex to mix, and incubate for <time> at <temperature>;`
- 例句: Mix the PCR amplification product with magnetic beads (equilibrated to room temperature) at a volume ratio of PCR product 1 : magnetic beads 0.8 (e.g., if PCR product is 100 μL, add 80 μL of magnetic beads), vortex to mix, and incubate for 10 min at room temperature;

### 离心与处理
- 模板: `After a brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for <time> until the solution clarifies;`
- 例句: After a brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min until the solution clarifies;

### 停止点提示
- 模板: `Stop point: <action> can be performed <condition>, or the products can be stored at <temperature> for up to <time>.`
- 例句: Stop point: PCR can be performed overnight at this step, or the products can be stored at 4°C for up to 16 hours.

### 异常判断与警告
- 模板: `The <item> concentration is typically higher than <value>; if it is less than <value>, it is considered an <status>.`
- 例句: The cDNA PCR product concentration is typically higher than 20 ng/μL; if it is less than 20 ng/μL, it is considered an experimental abnormality.

### 设备/方法引用建议
- 模板: `For detailed procedures regarding <topic>, please refer to the *<manual_name>*.`
- 例句: For detailed procedures regarding subsequent library construction, please refer to the *Spatial Transcriptomics FF V1.3( 含兼容mlF) 建库实验操作说明书*.

### 条件确认/保证
- 模板: `Ensure that <item1> and <item2> are aligned. Press down on <item> to seat it securely within <container>;`
- 例句: Ensure that the hole cutouts on the fixture and gasket are aligned. Press down on the gasket to seat it securely within the fixture;

### 实验操作引导
- 模板: `According to <section_reference> → Prepare <reagents> in advance: <instruction>;`
- 例句: According to 3.1 Pre-experiment preparation → Prepare reagents required for the next day in advance: Take out magnetic beads, equilibrate at room temperature, and prepare 80% ethanol;

### 参数/数值参考
- 模板: `Table <number> Reference for <parameter_name> of <target_object>`
- 例句: Table 3-8 Reference for Reconstitution Volume of Purified PCR Amplification Products

### 免责声明句式
- 模板: `MGI makes no warranties of any kind with regard to this product manual, including, but not limited to, the implied warranties of <condition>.`
- 例句: MGI makes no warranties of any kind with regard to this product manual, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose.

### 章节标题
- 模板: `Chapter <number> <title>`
- 例句: Chapter 1 Introduction

### 步骤动作（准备类）
- 模板: `Preparing <object>`
- 例句: Preparing DNB Preparation Reagents

### 操作动作（计算类）
- 模板: `Calculate <object>`
- 例句: Calculate the theoretical relative quantity for each sample

### 技术规范（要求类）
- 模板: `<noun> Requirements`
- 例句: Library Insert Size Requirements

### 兼容性描述
- 模板: `Compatible with <object>`
- 例句: Compatible with FF V1.3 library sequencing

### 版本信息
- 模板: `<property> Version: <value>`
- 例句: Manual Version: A

### 名词性标题定义
- 模板: `<adjective/noun> <noun>`
- 例句: Sequencing Principle

### 归属权声明
- 模板: `<product> is a trademark of <company>.`
- 例句: TM is a trademark of Thermo Fisher Scientific Inc.

### 否定/禁止性指令
- 模板: `Do not <verb> <object>.`
- 例句: Do not remove components; keep them in the packaging until used up.

### 动作的必要/强制要求
- 模板: `<subject> must be <verb-ed> <adverbial>.`
- 例句: All samples and various types of waste must be treated as hazardous materials in accordance with relevant regulations.

### 步骤/动作的自动化特征
- 模板: `<subject> <verb> automatically <adverbial>.`
- 例句: When sequencing is in progress, the control software automatically calls the basecalling software for analysis.

### 适用性/范围说明
- 模板: `<subject> is applicable to <object>.`
- 例句: This reagent set is applicable to Stereo-seq Transcriptomics FF V1.3 libraries.

### 警告/注意事项
- 模板: `Please <verb> <object> before <activity>.`
- 例句: Please read the product manual carefully before use.

### 说明书/文档目的
- 模板: `This manual provides operating instructions for <procedure> using <kit_name>.`
- 例句: This manual provides operating instructions for sequencing procedures using the DNBSEQ-T7RS Visualization Kit.

### 产品用途/限制
- 模板: `This product is for <usage> only.`
- 例句: This product is for scientific research use only.

### 表格/数据项描述
- 模板: `<Subject> <quantity>/<unit> × <count>.`
- 例句: TE buffer, 480 μL/tube × 1 tube.

### 状态说明/异常描述
- 模板: `Presence of <condition>.`
- 例句: Presence of impurities.

### 操作顺序说明
- 模板: `During the <process>, <subject> is performed according to <criteria>.`
- 例句: During the sequencing process, the total number of sequencing cycles is performed according to the selected sequencing read length.

### 物品规格描述
- 模板: `<item_name>/<quantity_unit>`
- 例句: Transparent Sealing Film/2 sheets

### 属性项标示
- 模板: `<label>: <value>`
- 例句: Cat. No.: 940-001904-00

### 禁止操作声明
- 模板: `The use of <item> is prohibited during <context>; <requirement> must be used.`
- 例句: The use of filter tips is prohibited during DNB preparation and loading; recommended brand catalog numbers must be used.

### 建议操作声明
- 模板: `For <context>, it is recommended to use <recommendation>.`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### 步骤耗时描述
- 模板: `<action>: <time>`
- 例句: Thawing reagents: 0.5 hr

### 条件要求声明
- 模板: `If <condition>, the <specification> shall prevail.`
- 例句: If the library construction kit manual has special requirements, the fragment size requirements specified in the manual shall prevail.

### 公式转换说明
- 模板: `The conversion formula between <variable_a> and <variable_b> is as follows:`
- 例句: The conversion formula between fmol and ng is as follows:

### 操作指令 - 建议
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended that the relative content of any base is between 5% and 12.5%, it can be sequenced.

### 操作指令 - 警告/禁止
- 模板: `Do not <verb> <object>.`
- 例句: Do not place the DNB Polymerase Mix II (OS-V4.0) at room temperature; do not hold the tube wall for an extended period.

### 操作指令 - 强制要求
- 模板: `<subject> must be <past_participle> <adverb>.`
- 例句: DNB must be mixed gently by slow pipetting using wide-bore pipette tips (without filters); do not centrifuge, vortex, or violently pipette.

### 条件句 - 规则引用
- 模板: `If the <object> has special requirements, the <object> requirements in the <object> shall prevail.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the kit manual shall prevail.

### 条件句 - 建议上机标准
- 模板: `If <condition>, it is not recommended for <action>, and <object> needs to be <past_participle>.`
- 例句: If it is lower than 5%, it is not recommended for sequencing, and the pooling scheme needs to be re-planned.

### 定义与术语解释
- 模板: `<variable> represents the <description> (<unit>), and <variable> represents the <description> (<unit>).`
- 例句: C1 represents the FFPE library concentration (ng/μL) obtained from the "Library Concentration" section on page 9, and C2 represents the FF V1.3 library concentration (fmol/μL) obtained from "Library Concentration" on page 9.

### 步骤衔接 - 准备与操作
- 模板: `<verb> the <object> from the <source> and place it on ice for later use.`
- 例句: Remove the DNB Polymerase Mix I (OS-V4.0) from the DNBSEQ one-step DNB preparation kit and place it on ice.

### 步骤衔接 - 试剂混匀
- 模板: `After the reagent has thawed, vortex for <number> seconds to mix, briefly centrifuge, and place on ice for later use.`
- 例句: After the reagent has thawed, vortex for 5 seconds to mix, briefly centrifuge, and place on ice for later use.

### 步骤衔接 - 条件反应
- 模板: `Once the <object> reaches <temperature>, immediately <verb> <quantity> of <reagent>, using <tool> to <action>.`
- 例句: Once the PCR instrument temperature reaches 4 °C, immediately add 20 μL of DNB termination buffer, using a wide-bore pipette tip (without filters) to slowly pipette up and down to mix 5 to 8 times.

### 建议 - 策略选择
- 模板: `<subject> are different; select the appropriate <object> based on <condition>.`
- 例句: The reaction programs for the FF V1.3 library and the FFPE library are different; select the appropriate program based on actual needs.

### 建议操作
- 模板: `When <situation>, it is recommended to <action>.`
- 例句: When the number of samples is large, it is recommended to perform quantification in batches.

### 交叉引用
- 模板: `For operation, see "<chapter_title>" on page <page_number>.`
- 例句: For operation, see "DNB Quantitative Operation Guide" on page 45.

### 计算公式表述
- 模板: `The <attribute> of <sample> is: <formula>.`
- 例句: The theoretical relative quantity of sample A is: A1 = required data amount of sample A / DNB concentration of sample A

### 目的状语
- 模板: `To <purpose>, it is recommended that <action>.`
- 例句: To ensure base balance for sequencing, it is recommended that the mass ratio of the CITE V1.1-cDNA library to the CITE V1.1-ADT library be no less than 1:1.

### 步骤衔接
- 模板: `After <process_completed>, <action>.`
- 例句: After DNB sampling for all samples is completed, use a wide-bore pipette tip.

### 条件操作说明
- 模板: `Thaw, and perform the corresponding operations according to the following differences: <itemized_list>`
- 例句: Thaw, and perform the corresponding operations according to the following differences: Room temperature thawing: Place in a room temperature water bath to thaw for 1.5 hours.

### 使用前操作
- 模板: `<action> before use, then <action>.`
- 例句: Gently invert and mix 5 times before use, then centrifuge for 1 minute.

### 产品合规性说明
- 模板: `This product manual is intended for <product_name>, manual version <version_number>.`
- 例句: This product manual is intended for the MGISEQ-2000RS Spatial Visualization Reagent Kit, manual version 4.0.

### 操作类标题
- 模板: `<Gerund> <Object>`
- 例句: Placing Samples

### 操作类指令
- 模板: `<Verb> <Object>`
- 例句: Prepare cleaning reagent tubes

### 条件限定
- 模板: `During <Event/Process>, <Main Clause>`
- 例句: During sequencing, the control software automatically invokes the basecalling software.

### 严格禁止
- 模板: `It is strictly prohibited to <Verb> <Object>`
- 例句: It is strictly prohibited to use products beyond their expiration date.

### 规范性否定
- 模板: `<Object> must not be <Verb-ed>`
- 例句: Reagent components from different batches must not be mixed.

### 操作前建议
- 模板: `Before <Action/Event>, please <Verb> <Object>`
- 例句: Before the experiment, please familiarize yourself with and master the operating methods.

### 使用范围限定
- 模板: `This product is for <Purpose> use only`
- 例句: This product is for scientific research use only.

### 试剂规格描述
- 模板: `<Item Name>, <Volume> × <Unit>`
- 例句: Inactivated MDA Reagent, 3.50 mL × 1 vial

### 操作限制指令
- 模板: `For <Context>, <Object> must not be <Verb>; you must use <Replacement>.`
- 例句: For DNB preparation and loading, filter tips must not be used; you must use the recommended brand catalog numbers.

### 操作建议
- 模板: `For <Context>, it is recommended to use <Recommendation>.`
- 例句: For other consumables, it is recommended to use the recommended brand catalog numbers.

### 基础操作步骤
- 模板: `<Step Number>. <Verb> the <Object> from the <Source>.`
- 例句: 1. Take out the DNB Loading Buffer 6 from the DNBSEQ-T7RS DNB Loading Kit.

### 前置条件操作
- 模板: `After <Condition>, <Verb> for <Duration> to <Purpose>.`
- 例句: After thawing, vortex for 5 seconds to mix well, briefly centrifuge, and place on ice for later use.

### 条件判定与 contingency
- 模板: `If <Condition> is observed in <Object>, <Action>.`
- 例句: If crystals are observed in DNB Loading Buffer 6, vortex continuously and vigorously for 1-2 minutes until the precipitate is completely dissolved, then centrifuge briefly before use.

### 强制合规性约束
- 模板: `The <Object> must be <Action> before <Time/Condition>.`
- 例句: The DNB loading mixture must be prepared fresh before use.

### 禁止操作指令
- 模板: `Do not <Action 1>, <Action 2>, or <Action 3>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 界面交互指令
- 模板: `Click [<Button Name>] to enter the interface shown below:`
- 例句: Click [Load] to enter the interface shown below:

### 数据输入约束
- 模板: `The <Data Name> is limited to <Constraint>.`
- 例句: The DNB information entered is limited to numbers, letters, or a combination of both.

### SequentialInstruction
- 模板: `<Action1> and <Action2>.`
- 例句: Peel off the sealing film from the sample loading reagent plate and add 4 mL of 0.1 M NaOH to well 11.

### InstructionWithResult
- 模板: `Place the <object> onto the <target>; the interface will show <status>.`
- 例句: Place the prepared sample loading reagent plate onto the reagent plate tray of the MGIDL-T7RS; the interface will show reagent plate initialized.

### ConditionalInstruction
- 模板: `If <condition>, you can <action> according to the prompts.`
- 例句: If it is not displayed, you can manually enter it according to the prompts.

### PreConditionInstruction
- 模板: `Before <action>, ensure that <check>.`
- 例句: Before placing the slide, ensure that none of the four sealing gaskets on the slide platform are missing.

### ProhibitionInstruction
- 模板: `Do not <action> to avoid <consequence>.`
- 例句: Do not press on the slide glass to avoid damaging the slide or leaving fingerprints and impurities on the glass surface.

### ConditionalProhibition
- 模板: `Once <action>, do not <action>, as this may cause <consequence>.`
- 例句: Once the slide is placed, do not move it, as this may cause misalignment between the slide flow channel holes and the sealing gasket.

### RecommendationInstruction
- 模板: `It is recommended to <action> to prevent <consequence>.`
- 例句: It is recommended to store the loaded slide in a resealable bag to prevent the edges from drying out.

### StatusNotification
- 模板: `When <condition>, it indicates that <process> is complete, taking approximately <time>.`
- 例句: When the interface appears as shown below, it indicates that slide loading is complete, taking approximately 2.5 hours.

### ReferenceInstruction
- 模板: `If <subject> has specific requirements, please follow <requirement>.`
- 例句: If the library construction kit manual has specific requirements, please follow the fragment requirements stated in that manual.

### Labeling
- 模板: `Figure <number> <description>.`
- 例句: Figure 6 Sample loading reagent plate well position information and liquid addition operation.

### 试剂准备指令
- 模板: `Remove <reagent> from <kit_name> and place it on ice to thaw.`
- 例句: Remove DNB Polymerase Mix I (OS-V4.0) from the spatiotemporal visualization reagent kit and place it on ice to thaw.

### 步骤处理衔接
- 模板: `After <action>, mix by <method> for <duration>, briefly centrifuge, and keep on ice for use.`
- 例句: After thawing, mix by vortexing for 5 seconds, briefly centrifuge, and keep on ice for use.

### 反应体系配制
- 模板: `Take <vessel> and prepare the reaction mixture on ice according to the following system:`
- 例句: Take 0.2 mL 8-strip tubes or PCR tubes and prepare the reaction mixture on ice according to the following system:

### 优先级条件建议
- 模板: `If the <manual_name> has special requirements, the requirements specified in the manual shall prevail.`
- 例句: If the library preparation kit manual has special requirements, the library requirements specified in the manual shall prevail.

### 参数设置建议
- 模板: `It is recommended to set the <item> to <value>.`
- 例句: The heated lid temperature is recommended to be set to 35°C, or to the lowest possible temperature close to 35°C.

### 禁止事项
- 模板: `Do not <action1>, and avoid <action2>.`
- 例句: Do not place the DNB Polymerase Mix II (OS-V4.0) at room temperature, and avoid prolonged contact with the tube wall.

### 文档引用参考
- 模板: `For specific operations, please refer to page <page_number>, '<section_title>'.`
- 例句: For specific operations, please refer to page 40, "Operation Guide for DNB Quantification using Qubit".

### 表格命名规范
- 模板: `Table <number>: <title>`
- 例句: Table 11 DNB preparation reaction system 1

### 用量说明
- 模板: `Each lane requires <amount> of <substance>.`
- 例句: Each lane requires 50 μL of DNB.

### 步骤执行衔接
- 模板: `<verb> <object>, then <verb> <object> for <duration/purpose>.`
- 例句: Take out the DNB Loading Buffer II, place it on an ice box for approximately 30 minutes until thawed.

### 条件性操作建议
- 模板: `If <condition> is found in <object>, <action>.`
- 例句: If crystals are found in DNB Loading Buffer II, use a vortex mixer to continuously oscillate vigorously for about 1~2 minutes.

### 准备工作通用句
- 模板: `<verb> <object>, and keep at <temperature/condition> for later use.`
- 例句: Gently mix the DNB loading mix 5–8 times using a wide-bore pipette tip, and keep at 4 °C for later use.

### 禁止性指令
- 模板: `Do not <verb> <object>.`
- 例句: Do not centrifuge, vortex, or vigorously pipette.

### 基于表格/说明的操作
- 模板: `<verb> <object> according to the table below:`
- 例句: Take out a 0.5 mL cryotube and prepare the DNB loading system 1 according to the table below:

### 时间/温度依赖步骤
- 模板: `For <action>, refer to <reference>.`
- 例句: For the next step, refer to page 22, "Placing the Reagent Cartridge".

### 处理解冻试剂
- 模板: `After complete thawing, store in a <temperature> refrigerator for later use.`
- 例句: After complete thawing, store in a 2 °C-8 °C refrigerator for later use.

### 均匀混合操作
- 模板: `Shake <object> <direction> <count> times to ensure the reagent is thoroughly mixed.`
- 例句: Shake the washing reagent reservoir clockwise 5~10 times, and then counter-clockwise 5~10 times to ensure the reagent is thoroughly mixed.

### 加入试剂标准句
- 模板: `Use a <tool> to transfer <volume> of <reagent> into <target>.`
- 例句: Use a 1 mL pipette to transfer 600 μL of MDA Polymerase Mix II into the reagent tube.

### 强制性要求
- 模板: `<object> must not be reused.`
- 例句: Sealing film must not be reused.

### 操作指令（祈使句）
- 模板: `<verb> <object> <preposition phrase>`
- 例句: Open the door of the reagent compartment, and use lint-free paper or cloth moistened with pure water to wipe the bottom and sides.

### 步骤衔接（目的导向）
- 模板: `<action>, <ensure/confirm/verify> <condition>`
- 例句: Close the cover and confirm that it is tightly fastened.

### 条件句（如...则...）
- 模板: `<condition>, <consequence>`
- 例句: Check if the water level in the pure water tank is sufficient; insufficient pure water will lead to sequencing failure.

### 交叉引用（参考）
- 模板: `For <information/method>, refer to <location/section>, "<title>".`
- 例句: For the preparation method, refer to page 38, "Cleaning Preparation".

### 建议与必须（强制性要求）
- 模板: `<subject> must be <past participle/action>.`
- 例句: This operation must be performed while the sequencer is idle.

### 禁止操作（负面建议）
- 模板: `Do not <verb> <object>.`
- 例句: Do not centrifuge, vortex, or pipette vigorously.

### 图表说明
- 模板: `Figure <number>: <Description>.`
- 例句: Figure 23: Main interface of DNBSEQ-T7RS

### 使用前的准备
- 模板: `Before <action>, <prepare/do> <object>.`
- 例句: Before use, invert the sequencing reagent cartridge 3 times, then vigorously shake up and down 20 times.

### 物料状态检查
- 模板: `After <action>, ensure <state>.`
- 例句: After ensuring there is no visible dust on the front and back of the slide, put the slide into the core drive.

### Sequential Step
- 模板: `<Step>. <Action 1>, then <Action 2>, and finally <Action 3>.`
- 例句: 7. Using a pipette of the appropriate volume range, follow the volumes in the table below to first add the dNTPs mixture, then add DNA polymerase mixture II, gently invert 4-6 times to mix, and finally transfer the mixture to well No. 1.

### Preparation Pre-Use
- 模板: `<Subject> must be <Action> to mix before loading, and then <Action> before use.`
- 例句: The dNTPs mixture II must be vortexed for 5 seconds to mix before loading, and then briefly centrifuged before use.

### Precautionary Action
- 模板: `When <Action>, exercise caution to prevent <Outcome>.`
- 例句: When transferring the mixture, exercise caution to prevent it from spilling out of the reagent tube.

### UI Navigation
- 模板: `Click <UI Element> to enter the <Interface Name> interface.`
- 例句: Click the 【Sequencing】 option on the main interface to enter the following interface:

### Selection Instruction
- 模板: `Select <Item> from the <Dropdown Name> drop-down menu.`
- 例句: Select the spatial transcriptomics sequencing scheme from the [Sequencing Scheme] drop-down menu.

### Conditional Workflow
- 模板: `If <Condition A>, select <Option A>; if <Condition B>, select <Option B>.`
- 例句: If barcode sequencing is required, select the STO_T_50+100+10 sequencing protocol; if barcode sequencing is not performed, select the STO_T_50+100_noBC sequencing protocol.

### Figure Caption
- 模板: `Figure <Number>: <Title>`
- 例句: Figure 9: Opening of the reagent trough loading wells

### Data Input
- 模板: `Enter <Data> in the entry field next to <Label>.`
- 例句: Move the cursor to the entry field next to [DNB ID] and enter the library name or ID.

### Failure Prevention
- 模板: `Ensure <Requirement>; otherwise, <Consequence>.`
- 例句: Please ensure the manually entered ID format is correct; otherwise, an ID error will be prompted, and you will not be able to continue.

### Instructional Step with Visual Reference
- 模板: `As shown in the figure below, <verb> <object> and <verb> <object>.`
- 例句: As shown in the figure below, click [▼] within the red box and select the corresponding tag sequence.

### Action with Purpose
- 模板: `Click <button> to <verb> <object>.`
- 例句: Click [Next] to review the information.

### Conditional Instruction
- 模板: `After <condition>, <verb> <object> and <verb> <object>.`
- 例句: After confirming the information is correct, click [Start] and select [Yes].

### Reference Instruction
- 模板: `Please refer to <document> for details.`
- 例句: Please refer to the DNBSEQ-T7 sequencer software operation guide for details.

### Table-based Instruction
- 模板: `<verb> <object> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### Specification/Metadata
- 模板: `Shelf life: <time> at <temperature>`
- 例句: Shelf life: 1 month at 4 °C

### Condition-based Selection
- 模板: `Select <option> in the following situations:`
- 例句: Select manual cleaning in the following situations:

### Procedural Instruction
- 模板: `<verb> <object> <location_or_detail>`
- 例句: Open the loading chamber door.

### Conditional Action
- 模板: `<verb> <object> if <condition>`
- 例句: Skip this step if there is no slide on the MGIDL-T7RS.

### Maintenance Requirement
- 模板: `<object> should be replaced <frequency_or_usage>`
- 例句: Cleaning slides should be replaced every month or after 10 uses.

### Obligatory Requirement
- 模板: `<subject> must be <action> <manner>`
- 例句: After each run, the instrument must be cleaned either automatically or manually.

### Check Verification
- 模板: `Confirm that <condition_or_status>`
- 例句: Confirm that the water in the pure water bucket has reached 4.5 L.

### Fallback Instruction
- 模板: `If <condition>, please contact technical support.`
- 例句: If the above methods still cannot resolve the abnormal negative pressure, please contact technical support.

### Conditional Obligation
- 模板: `If <condition>, <subject> must be <action>`
- 例句: If the empty sample loading plate has been used, it must be washed 3~5 times with laboratory-grade water before replenishing cleaning reagents.

### UI Action
- 模板: `Click <UI_element> and select <option> to <result>`
- 例句: Click [Start] on the interface, select [Yes] in the pop-up dialog box to start the DNBSEQ-T7RS manual cleaning.

### 条件触发动作
- 模板: `When <condition> occurs on <device>, <action>.`
- 例句: When pumping failure occurs on DL-T7RS and DNBSEQ-T7RS:

### 步骤执行指引
- 模板: `<verb> <object> and <verb> <object>.`
- 例句: Remove the sequencing flow cell, check the seal for dust, and use a compressed air duster to blow away the dust.

### 异常处理与技术支持
- 模板: `If <condition> still cannot be resolved by the methods above, please contact technical support.`
- 例句: If the pumping abnormality still cannot be resolved by the methods above, please contact technical support.

### 操作建议/限制
- 模板: `<subject> must be <verb-ed> within <time> after <action>.`
- 例句: The Qubit working solution must be used within 0.5 hours after preparation.

### 禁止操作
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the conical walls of the assay tube.

### 负面义务
- 模板: `<subject> must not be <verb-ed> in <location>.`
- 例句: Air bubbles must not be generated in the assay tube.

### 操作步骤衔接
- 模板: `<verb> <object> according to <reference>.`
- 例句: Please perform manual cleaning and maintenance for both MGIDL-T7RS and DNBSEQ-T7RS.

### 工具与试剂准备
- 模板: `Use <reagent/tool> to <verb> <target>.`
- 例句: Use Qubit ssDNA Buffer to dilute Qubit ssDNA Reagent 200-fold.

### 确认性提示
- 模板: `Check that <parameter> is within the normal range of <range> before proceeding.`
- 例句: Check that the negative pressure is within the normal range of -80 to -99 kPa before proceeding.

### 界面交互指引
- 模板: `Place the cursor in the <field_name> input field, and use <method> to <verb> <info>.`
- 例句: Place the cursor in the [Reagent Slot ID] input field, and use a barcode scanner to scan the barcode on the bottom right corner.

### 条件步骤衔接
- 模板: `After <gerund> that <clause>, <verb> <object>.`
- 例句: After confirming that all information is correct, click [Start].

### 确保准确性建议
- 模板: `Review <noun_phrase> to ensure it is accurate.`
- 例句: Review all filled-in information to ensure it is accurate.

### 目的/条件句
- 模板: `To ensure <noun_phrase>, <subject> automatically <verb> <object> for <noun_phrase>.`
- 例句: To ensure sequencing quality, the sequencer automatically performs one additional cycle for calibration after completing.

### 操作引导与解释
- 模板: `For <noun_phrase>, the <noun> is <value>, and the <noun> is <value>.`
- 例句: The Barcode read length is 10, the first-strand correction cycle is 1, the second-strand correction cycle is 1.

### 参考说明
- 模板: `For details, please refer to the <document_name>.`
- 例句: For details, please refer to the MGISEQ-2000 & MGISEQ-2000RS Gene Sequencer Software Operation Guide.

### 制备指引
- 模板: `Prepare <noun_phrase> according to the table below:`
- 例句: Prepare washing reagents according to the table below:

### 试剂/耗材状态描述
- 模板: `Shelf life: <time_period> when stored at <temperature>.`
- 例句: Shelf life: 1 month when stored at 2–8 °C.

### 复杂操作步骤衔接
- 模板: `After <verb_ing> <noun>, immediately <verb> <noun>; once <clause>, <verb> <noun>.`
- 例句: After starting sequencing, immediately open the slide chamber door; once the sample or reagent has smoothly entered the slide, close the slide chamber door.

### 系统提示描述
- 模板: `The system will prompt: [<text>].`
- 例句: The system will prompt: [Please perform maintenance cleaning].

### 顺序衔接与操作引导
- 模板: `Following the direction indicated on <object>, slowly <verb> the prepared <target>.`
- 例句: Following the direction indicated on the cleaning reagent trough cover, slowly push the prepared cleaning reagent trough 1 into the reagent compartment bottom.

### 软件界面交互
- 模板: `Enter the <interface_name>, click the <element> to the right of [<label>], and select [<option>] to <action>.`
- 例句: Enter the cleaning interface, click the drop-down list to the right of [Cleaning Type], and select [Routine Cleaning] to start cleaning.

### 条件触发处理
- 模板: `When <condition> occurs, <action>.`
- 例句: If bubbles appear, pause cleaning immediately and replace the slide.

### 检查与排查建议
- 模板: `When <condition>, please perform the following operations to <action>:`
- 例句: When the DNB concentration is lower than 8 ng/μL, please perform the following operations to troubleshoot the issue:

### 状态与限制描述
- 模板: `During <process_name>, <subject> will not <action>, and <object> does not need to be replaced.`
- 例句: During DNB line cleaning, the sample needle will not descend, and there is no need to replace the cleaning reagent trough.

### 列表式排查建议
- 模板: `y Check if <subject> <condition>.`
- 例句: y Check if the kit used is expired.

### 状态描述
- 模板: `<Subject> Status: <Status>`
- 例句: A Status: Paused 20.0℃-91.6ka

### 礼貌性操作指示
- 模板: `<Action>, please <Verb> <Adverb>.`
- 例句: Side A sequencing paused, please resume promptly.

### 步骤标题
- 模板: `<Number>. <Verb> <Object>: <Instruction>`
- 例句: 3. Prepare the sequencing reagent cartridge: Open the reagent compartment door, remove the sequencing reagent cartridge,

### 条件触发操作
- 模板: `If <Condition>, <Action>.`
- 例句: If the reagent kit has thawed (including dNTPs) and cannot be used on time, it can be freeze-thawed at most one more time.

### 异常处理引导
- 模板: `When <Condition>, <Issue>. Please perform the following operations:`
- 例句: When the negative pressure value is displayed in red, the negative pressure is abnormal. Please perform the following operations:

### 禁止性用语
- 模板: `Do not <Verb> <Object>.`
- 例句: Do not touch the conical wall of the detection tube.

### 参考指引
- 模板: `<Verb> <Object> according to <Section> on page <Number>.`
- 例句: Perform a maintenance wash on the sequencer according to "Full Maintenance Wash (approx. 94 minutes)" on page 33.

### 故障排除确认
- 模板: `If the <Issue> persists after <Action>, please contact an engineer.`
- 例句: If there is no improvement after the maintenance wash, please contact an engineer.

### 提示标注
- 模板: `<Label>: <description>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 文档引用
- 模板: `For details, please refer to <Document Name>.`
- 例句: For details, please refer to the "Stereo-seq Library Preparation Kit Instruction Manual".

### 合规声明
- 模板: `Nothing herein is intended to or should be understood as <action>.`
- 例句: Nothing herein is intended to or should be understood as any warranty of the performance of any product listed or described herein.

### 属性定义
- 模板: `<Attribute>: <value>.`
- 例句: Storage temperature: -25℃ ~ -18℃.

### 功能描述
- 模板: `<Subject> enables the <action> of <target>.`
- 例句: The STOmics Stereo-CITE protein-transcriptome reagent kit enables the co-detection of the whole transcriptome and ultra-high-plex proteins.

### 质量保证
- 模板: `<Subject> have undergone <process>, ensuring <result>.`
- 例句: All reagents provided in this kit have undergone strict quality control and functional verification, ensuring the stability and repeatability of library preparation.

### 组分清单开头
- 模板: `Each reagent kit consists of the following <number> components:`
- 例句: Each reagent kit consists of the following four components:

### 参数标注
- 模板: `<Parameter>: <Value>`
- 例句: Storage temperature: Room temperature

### 试剂/耗材清单项
- 模板: `<Name> <Cat. No.> <Color> <Volume> × <Quantity>`
- 例句: Blocking Reagent 1000044666 Transparent 60 µL × 1

### 品牌/产品选择
- 模板: `Choose one from [Source/Condition].`
- 例句: Choose one from brands with the same superscript number.

### 兼容性说明
- 模板: `This kit has been validated for use with <Object>.`
- 例句: This kit has been validated for use with TotalSeq™-A primary antibodies.

### 组分功能描述
- 模板: `<Component> is used to <Purpose>, and can be <Action>.`
- 例句: FcR Blocking Reagent is used to block Fc receptors on the cell membrane surface and can be purchased based on the species.

### 参考链接说明
- 模板: `For <Action>, please refer to this website: <URL>`
- 例句: For the selection of isotype control antibodies, please refer to this website: https://www.biolegend.com/en-us/search-results?PageSize=25&Category=ISO_CTRL&Format=TOTALSEQ_A

### 参考手册说明
- 模板: `Regarding <Requirement>, please refer to <Manual>.`
- 例句: Regarding microscope requirements, please refer to the STOmics Microscope Evaluation Reference Manual.

### 产品信息头
- 模板: `<ProductName> Cat. No.: <ID>`
- 例句: Stereo-seq Proteomics Assistant Kit Cat. No.: 202KA114

### 试剂配制（取用与稀释）
- 模板: `Take <amount> of <reagent_A> and add to <amount> of <reagent_B>.`
- 例句: For 5X SSC, take 5 mL of 20X SSC and dilute to 20 mL with Nuclease-Free Water.

### 解冻与预处理
- 模板: `Remove <object> from <temperature>, thaw, and keep on ice.`
- 例句: Remove RI from -20°C; use 210 μL per chip and keep on ice.

### 操作建议（推荐与条件）
- 模板: `It is recommended to <verb> <object> <condition>.`
- 例句: It is recommended to use pipette tips with filters and to change tips when aspirating different samples.

### 使用限制与警示
- 模板: `This product is for <purpose> only and is not for <negative_purpose>.`
- 例句: This product is for research use only and is not for clinical diagnostic purposes.

### 物料选择与替代
- 模板: `<product_name> (or equivalent substitute).`
- 例句: Biosharp IHC pen BC004 (or equivalent substitute).

### 温度与状态调节
- 模板: `Equilibrate <object> to <temperature>.`
- 例句: Take out the PR Rinse Buffer at least 5 minutes before use and equilibrate to room temperature.

### 废弃物处理
- 模板: `All <samples/waste> should be handled in accordance with relevant regulations.`
- 例句: All samples and waste materials should be handled in accordance with relevant regulations.

### 顺序操作步骤
- 模板: `<ordinal>. <verb> <object> <duration>; <ordinal>. <verb> <object> <duration>.`
- 例句: a. Equilibrate the lyophilized powder tube at room temperature for 5 min; b. Place the lyophilized powder tube into an empty 2 mL EP tube...

### 即时配制要求
- 模板: `<reagent_name> should be prepared fresh before <step>.`
- 例句: 0.01N HCl (pH = 2.0) should be prepared fresh before use.

### 过程条件指令
- 模板: `During <process>, <action>`
- 例句: During the tissue temperature equilibration process, refer to Table 2-1 in 2.5. Blocking and Antibody Incubation to...

### 液体吸弃指令
- 模板: `Aspirate and discard <liquid> from <location> [while keeping <state>]`
- 例句: Aspirate and discard the blocking buffer from one corner of the chip, ensuring the tissue on the chip remains wet;

### 溶液添加与孵育
- 模板: `Add <volume> of <reagent> [to <location>], and incubate at <condition> for <time>`
- 例句: Immediately add 400 μL/chip of Wash Buffer, and incubate at room temperature for 1 min;

### 操作警告
- 模板: `Avoid <action/state> [to prevent <consequence>]`
- 例句: Strictly avoid tissue drying during the liquid exchange process, as tissue drying can easily generate non-specific signals.

### 引用指令
- 模板: `Refer to <reference> to <action>`
- 例句: Refer to Chapter 2 of the "Stereo-seq Chip Carrier and Accessories User Manual" to assemble the gasket and fixture in...

### 重复步骤
- 模板: `Repeat steps <step_range> [frequency], for a total of <total_count> washes.`
- 例句: Repeat steps e.-f. once, for a total of 2 washes.

### 试剂配制
- 模板: `Prepare <reagent> according to <reference>`
- 例句: Prepare the primary antibody incubation solution according to the reagents used...

### 液体弃除指令
- 模板: `Aspirate and discard the <reagent> from <location> using a pipette, keeping <object> <state>;`
- 例句: Aspirate and discard the secondary antibody incubation solution from one corner of the chip using a pipette, keeping the chip tissue wet;

### 步骤重复指令
- 模板: `Repeat <action> steps <step_range> once;`
- 例句: Repeat washing steps c.-d. once;

### 前置条件/准备建议
- 模板: `Before use, <verb> the <reagent> <condition> for <time> (<limitation>);`
- 例句: Before use, incubate the Decrosslinking Reagent in a metal bath or other equivalent equipment at 70°C for 10 min (do not exceed 30 min);

### 操作禁止事项
- 模板: `<action> is prohibited.`
- 例句: Spaces and other special characters are prohibited.

### 引用参考指令
- 模板: `Refer to <section/chapter> in <document_name> to <action>;`
- 例句: Refer to Table 2-5 in section 2.6 DAPI Staining to prepare the DAPI working solution;

### 预防性警示
- 模板: `Ensure <object> does not <action> during <process>; if <condition>, it is prone to <consequence>.`
- 例句: Ensure the chip does not dry out during the liquid exchange process; if the tissue dries, it is prone to producing non-specific signals.

### 可选操作
- 模板: `(Optional) <verb> <equipment> to <action> to <result>;`
- 例句: (Optional) Use a slide centrifuge (mini slide centrifuge LX-700) to centrifuge for 10 s to spin dry the liquid on the chip;

### 参数/规格说明
- 模板: `<parameter_name>: <value> (<reference_value>);`
- 例句: DAPI filter cube (Ref.: Excitation 375/28 nm, Emission 460/50 nm)

### 滴加操作指令
- 模板: `Add <volume> of <reagent> dropwise from the <location>, and incubate at <condition> for <time>;`
- 例句: Add 150 μL/chip of DAPI working solution dropwise from the non-tissue area, and incubate at room temperature for 2 min;

### 操作指令 - 试剂配制
- 模板: `Prepare the <solution_name> in advance by referring to <reference_location>.`
- 例句: k. During decrosslinking, prepare the 1X Tissue Permeabilization Reagent working solution in advance by referring to Table 2-6.

### 操作指令 - 加入试剂
- 模板: `Add <volume> of <reagent_name> per chip.`
- 例句: h. Add PR Rinse Buffer solution (containing 5% RI) at a volume of 200 μL per chip;

### 操作步骤衔接 - 倾斜与吸弃
- 模板: `Slightly tilt the <carrier_name> at an angle less than 20°. Use a pipette to aspirate and discard the <reagent_name>.`
- 例句: b. After cooling, slightly tilt the handheld carrier at an angle less than 20°. Use a pipette to aspirate and discard the Wash Buffer.

### 条件句 - 预防措施
- 模板: `Do not <action> to prevent <negative_outcome>.`
- 例句: Do not press on the upper parts of the clamp latches when peeling off the plate sealing film to prevent the carrier from loosening.

### 孵育建议
- 模板: `Incubate the <solution_name> at <temperature> for <time>.`
- 例句: l. Incubate the permeabilization working solution in a metal bath or other equivalent instrument at 37°C for 10 min before use;

### 仪器设置
- 模板: `Set the <instrument_name> temperature to <temperature> and the lid temperature to <temperature>.`
- 例句: Set the PCR instrument temperature to 37°C and the lid temperature to 42°C, and place the PCR adapter to equilibrate the temperature;

### 操作步骤衔接 - 后续处理
- 模板: `After <action> is complete, <next_action>.`
- 例句: m. After de-crosslinking is complete, transfer the handheld carrier to the laboratory bench, remove and discard the sealing film.

### 磁珠操作 - 混匀与平衡
- 模板: `Remove <reagent_name> from <temperature> in advance, vortex to mix, and equilibrate to room temperature.`
- 例句: Remove from 4°C 30 minutes in advance, vortex to mix, and equilibrate to room temperature to ensure optimal recovery efficiency.

### 警示/禁止
- 模板: `Do not <action>, to avoid <risk>.`
- 例句: When aspirating the supernatant after elution, do not touch the magnetic beads. Aspirating magnetic beads may affect subsequent purification reactions.

### 操作指令 - 密封与处理
- 模板: `Seal the <carrier_name> with sealing film and <next_action>.`
- 例句: d. Seal the handheld carrier with sealing film, pressing firmly around the edges of the reaction wells to prevent evaporation.

### 保持装置位置操作
- 模板: `Keeping the <object> on the <location>, <verb> <amount> <substance>...`
- 例句: Keeping the centrifuge tube on the magnetic rack, add 1 mL of 80% ethanol...

### 步骤重复
- 模板: `Repeat step <number> once;`
- 例句: Repeat step 4 once;

### 干燥或孵育指令
- 模板: `Keep <object> on <location>, <action> at <condition> for <time>...`
- 例句: Keep the 1.5 mL centrifuge tube on the magnetic rack, air-dry at room temperature for 5-8 min...

### 试剂添加与混匀
- 模板: `Add <amount> <reagent> to <action>, vortex to mix...`
- 例句: Add 22 μL Nuclease-Free Water to resuspend, vortex to mix...

### 样本转移
- 模板: `Transfer the <substance> (<amount>) to <target>...`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 条件性体积补足
- 模板: `If the <object> is less than <amount>, bring the volume to <amount> with <reagent>.`
- 例句: If the recovered sample above is less than 42 μL, bring the volume to 42 μL with Nuclease-Free Water.

### 基于参考资料的操作
- 模板: `<action> according to <reference>...`
- 例句: Prepare cDNA PCR Mix following Table 2-9 in section 2.15.

### 产物存储建议
- 模板: `The <substance> can be stored at <temperature> for <duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### 瞬时离心与后续操作
- 模板: `Briefly centrifuge and <action>...`
- 例句: Briefly centrifuge and amplify according to the Transcriptome cDNA PCR Amplification Program...

### 试剂配制表标题
- 模板: `Table <number> Preparation of <reagent_name>`
- 例句: Table 2-1 Preparation of Blocking Buffer

### 条件语句（包含时间/状态）
- 模板: `After <action>, <verb> <object> on <location> and <verb> for <time> until <state>`
- 例句: After a brief centrifugation, place the PCR tube on a magnetic stand and let it stand for 5 min until the liquid becomes clear

### 用途声明
- 模板: `This product is for <usage> only, not for <prohibited_usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 浓度描述
- 模板: `The <analyte> concentration is typically <comparator> than <value>.`
- 例句: The DNA concentration is typically higher than 5 ng/μL.

### 成分列表（表格）
- 模板: `Component <column_headers>`
- 例句: Component 1X (μL) 1X + 10% (μL) 2X + 10% (μL)

### 存储建议
- 模板: `<product> can be stored at <temperature> for <duration>.`
- 例句: ADT amplification products can be stored at −20°C for 1 month.

### 检测与记录
- 模板: `Take <volume> of <sample>, <verb> the concentration using the <method>, and <verb> it;`
- 例句: Take 1 μL of ADT amplification product, measure the concentration using the Qubit dsDNA HS Kit, and record it;

### 祈使句操作指令
- 模板: `<verb> <object> (e.g., <action>)`
- 例句: Use an air duster to blow away any impurities or debris from the surfaces of the gasket...

### 前置条件/背景提示
- 模板: `Before <action>, <ensure/check> <object>...`
- 例句: Inspect the gasket for damage or cracks before use.

### 实验警示（关键步骤）
- 模板: `Critical Note: <action/check>, otherwise <negative_consequence>.`
- 例句: Critical Note: After snapping it into place, visually confirm that the chip carrier is horizontally parallel to the base...

### 参考链接/引用
- 模板: `<subject> reference URL: <URL>`
- 例句: Assembly method video reference URL: https://www.stomics.tech/resources/Videos/3671.html

### 组件/物料包含描述
- 模板: `The <product> includes <component A> (hereinafter referred to as "<short_name>"), <component B>...`
- 例句: The Stereo-seq Cassette accessory kit includes the Stereo-seq V3 Cassette Lid (hereinafter referred to as "Lid")...

### 步骤/逻辑衔接
- 模板: `During the <process>, when <condition>, <result>.`
- 例句: During the process of engaging the upper part of the carrier with the lower part, when it is in the state shown in Fig. 15...

### 条件触发/建议
- 模板: `If <condition>, <action>.`
- 例句: If it is difficult to snap together, first check whether the base and the chip carrier are installed correctly.

### 目的/结果说明
- 模板: `<action>, ensure <state>.`
- 例句: Add the corresponding reagents into the reaction wells as needed. During the reagent addition process, ensure no interference...

### 法律/授权声明
- 模板: `Without <formal_permission>, no one shall <prohibited_actions>.`
- 例句: Without written consent of this organization, no one shall, without authorization, use, modify, reproduce...

### 流程中警告
- 模板: `During the <process>, <object> must be <adjective>; do not <verb> or <verb> <object>.`
- 例句: During the incubation process, the carrier must be placed stably; do not bump or shake the carrier.

### 操作步骤建议
- 模板: `After <process>, carefully <verb> <object>.`
- 例句: After incubation, carefully remove the chip carrier.

### 工具使用推荐
- 模板: `It is recommended to <verb> <object> [Cat. No.: <id>] and use the <tool> to <verb> <object>.`
- 例句: It is recommended to purchase the Stereo-seq V3 Cassette Disassembly Tool [Cat. No.: 303TA30011] (Figure 26) and use the disassembly auxiliary tool.

### 条件式操作指南
- 模板: `If it is necessary to <verb> <object>, do so after <process> to <verb> <object> <verb-ing>.`
- 例句: If it is necessary to disassemble the carrier, do so after reagent removal to prevent reagent splashing during the disassembly.

### 清洁步骤指令
- 模板: `<verb> <object> with <agent> to <verb> <object>, and use a <tool> to <verb> <object>.`
- 例句: Wipe the upper cover with 75% ethanol to remove residual reagents from the surface, and use a clean air duster to blow dry residual 75% ethanol and impurities from the surface.

### 流程衔接说明
- 模板: `When it is necessary to <verb> <object> during the process, follow <section> to <verb> <object>.`
- 例句: When it is necessary to replace the V3 gasket during the process, follow the operations in step '1' of 'IV. Disassembly Procedure' to disassemble the V3 carrier.

### 产品声明
- 模板: `This product is for <usage> only, not for <usage>.`
- 例句: 1. This product is for research use only, not for diagnostic purposes.

### Reference
- 模板: `For [information], please refer to [Table/Section].`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 and Table 1-2.

### Polite Imperative
- 模板: `Please [verb] the [object] [condition].`
- 例句: Please store the product under the specified conditions as soon as possible.

### Conditional Guidance
- 模板: `If [condition], you may [verb] [action].`
- 例句: If any temperature abnormality is detected in the cold chain box, you may request the logistics provider to print the temperature real-time monitoring record sheet.

### Pre-procedural Requirement
- 模板: `Before [activity], please [verb] [object/action].`
- 例句: Before conducting the experiment, please familiarize yourself with the precautions for the various instruments to be used.

### Procedural Recommendation
- 模板: `It is recommended to [verb] [object] [condition].`
- 例句: It is recommended to take out the reagent components in advance before use.

### Purpose + Recommendation
- 模板: `To [goal], the use of [object] is recommended.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended; please change the tip when aspirating different samples.

### Usage Limitation
- 模板: `This product is intended for [scope] only and is not for [limitation].`
- 例句: This product is intended for research use only and is not for clinical diagnosis.

### Emphasis/Warning Label
- 模板: `[Label]: Pay special attention to [reason].`
- 例句: Critical steps: Pay special attention to these steps to avoid experimental failure or undesirable results.

### Structural Description
- 模板: `[Object] consists of the following [number] parts:`
- 例句: Each reagent kit consists of the following two parts:

### 安全操作/警告
- 模板: `Avoid <action_gerund> of <target> with <substance>; do not <verb> <target>.`
- 例句: Avoid direct contact of skin and eyes with samples and reagents; do not ingest samples or reagents.

### 合规处理
- 模板: `All <items> shall be disposed of in accordance with <regulations>.`
- 例句: All samples and various types of waste shall be disposed of in accordance with relevant regulations.

### 条件限制
- 模板: `The <target> should not exceed <dimension>.`
- 例句: The tissue size should not exceed 0.9 cm × 1.8 cm × 0.7 cm.

### 步骤/指令衔接
- 模板: `<verb> <target> with <substance> in advance and <verb> <target> on <location> to <verb> for <time_duration>.`
- 例句: Prepare a foam box of crushed ice in advance and place the OCT on the ice to pre-cool for 10 min.

### 补充/排除条件
- 模板: `Unless otherwise specified, <substance> is used for all <target> in this experiment.`
- 例句: Unless otherwise specified, Nuclease Free Water is used for all liquids in this experiment to dilute reagents.

### 建议/限制条件
- 模板: `It is strongly recommended to only <verb> <target> with <condition> for subsequent experimental procedures.`
- 例句: It is strongly recommended to only use tissue samples with RIN ≥ 7 for subsequent experimental procedures.

### 后续动作
- 模板: `Then, <verb> with <next_step>.`
- 例句: Then proceed with Total RNA extraction and quality assessment.

### 试剂配制/加入
- 模板: `Take <quantity> of <substance A> and add to <quantity> of <substance B>, volume required is at least <quantity>/chip.`
- 例句: Take 7.5 μL of RI and add to 142.5 μL of 0.1X SSC, volume required is at least 150 μL/chip.

### 溶解与混合
- 模板: `Dissolve the <reagent> with <quantity> of <substance>, and mix well by pipetting.`
- 例句: Dissolve the PR Enzyme (red cap, powder) with 1 mL of freshly prepared 0.01N HCl, and mix well by pipetting.

### 稀释操作
- 模板: `Dilute <quantity> of <stock solution> to <quantity> with <diluent> (at least <quantity>/chip).`
- 例句: Dilute 25 μL of 10X permeabilization reagent stock solution to 250 μL with 0.01N HCl (at least 200 μL/chip).

### 设备参数调节
- 模板: `Adjust the <device/parameter> to <value> in advance.`
- 例句: Adjust the slide dryer temperature to 37°C in advance.

### 条件要求（确保）
- 模板: `Ensure <parameter> is in the range of <range>; at least <quantity>/sample.`
- 例句: ensure pH value is in the range of 1.9-2.1; at least 5 mL/sample.

### 试剂储存/状态建议
- 模板: `<Substance> should be prepared immediately before use.`
- 例句: 0.01N HCl should be prepared immediately before use.

### 实验步骤-取物
- 模板: `Retrieve the <item>: remove the <item name> from the <container>, and record the serial number.`
- 例句: Retrieve the chip: remove the Stereo-seq chip P from the vacuum-dried aluminum foil bag, and record the serial number.

### 实验步骤-放置/清洗
- 模板: `Place the <item> in <container>, and wash twice with <liquid>.`
- 例句: Place the chip in a 9 cm culture dish and wash twice with water.

### 操作限制/禁止
- 模板: `Do not touch the <surface> of the <item>.`
- 例句: Do not touch the surface of the chip.

### 结果参照
- 模板: `The <parameter> is as shown in Table <table number>.`
- 例句: The baking time is as shown in Table 3-1.

### 表格引用
- 模板: `Table <TableID> <Content Description>`
- 例句: Table 3-1 Baking time for large chips of various sizes

### 操作步骤指令
- 模板: `<Imperative Verb> the <Object> according to <TableID/Condition>;`
- 例句: a. Prepare the Total RNA hybridization Mix according to Table 3-4;

### 试剂加液指引
- 模板: `Add <Reagent> (refer to Table <TableID> for the volume);`
- 例句: c. Add 0.1X SSC solution (refer to Table 3-7 for the volume);

### 即时操作指令
- 模板: `Immediately add the <Reagent> to <prevent/avoid> <NegativeEffect>.`
- 例句: f. Immediately add the RT QC Mix to prevent RNA degradation.

### 条件限制预警
- 模板: `The <subject> should not be too <condition>, so as to avoid <negative result>`
- 例句: The pre-cooling time should not be too long, so as to avoid water mist forming on the chip surface

### 异常处理与恢复
- 模板: `If <condition> is observed in the <container>, it can be <action1> and then <action2>.`
- 例句: If white precipitate is observed in the buffer, it can be dissolved at 55°C and then returned to room temperature.

### 条件限制（场景/状态）
- 模板: `Under the condition that <condition>, <main clause>.`
- 例句: Under the condition that the tissue has been removed cleanly and while maintaining identical imaging conditions...

### 标准判断（ criteria）
- 模板: `<feature1>, <feature2>, and <feature3> are the criteria for determining the optimal <process>.`
- 例句: Intact morphology, strongest fluorescence, and absence of diffusion are the criteria for determining the optimal permeabilization time.

### 步骤衔接（First... then...）
- 模板: `First, use <tool> to <action1>, then switch to <tool> to <action2>.`
- 例句: First, use the 4x objective lens to locate the target area, then switch to the 10x objective lens to scan the entire chip.

### 禁止事项（prohibited）
- 模板: `The use of <items> is prohibited.`
- 例句: the use of special characters such as spaces is prohibited.

### 必须事项（must）
- 模板: `<subject> must be <action> under <condition>.`
- 例句: Chips of the same tissue with different permeabilization times must be scanned under the same exposure conditions.

### 产品合规性声明（research use only）
- 模板: `This product is for <usage> only, not for <prohibited_usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 引用说明（for details, refer to）
- 模板: `For details, please refer to <chapter/section>.`
- 例句: For details, please refer to this manual Chapter 4...

### 修订/勘误记录（Action + Topic）
- 模板: `<Past_Tense_Verb> <content>.`
- 例句: Corrected the catalog numbers for some components of the Stereo-seq Library Preparation Kit.

### 警告/注意级别（Note/Critical Step）
- 模板: `<Note_Type>: <Explanation>.`
- 例句: Critical Step: Pay special attention to these steps to avoid experimental failure or undesirable outcomes.

### 请求执行动作
- 模板: `Please <verb> <object> <adverb/condition>.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 引用说明
- 模板: `For further information regarding <topic>, please refer to <reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 to Table 1-2.

### 内容概览
- 模板: `This list details the <item> required for this experiment.`
- 例句: This list details the equipment and materials required for this experiment.

### 实验调整说明
- 模板: `The <item> provided in this manual are <description>; in actual operation, they may be adapted according to <condition>.`
- 例句: The experimental protocols provided in this manual are general guidelines; in actual operation, they may be adapted according to specific experimental design, sample characteristics, sequencing applications, and devices.

### 操作前准备建议
- 模板: `Before use, it is recommended to <action> <object>.`
- 例句: Before use, it is recommended to remove the reagent components in advance, briefly centrifuge the enzyme components and place them on ice.

### 试剂限制说明
- 模板: `This kit does not contain reagents such as <list>.`
- 例句: This kit does not contain reagents such as TME, Stop Buffer, or TMB.

### 能力功能说明
- 模板: `The <product_name> can be used to <action> <object>.`
- 例句: The STOmics Stereo-seq Library Construction Kit can be used to construct whole-transcriptome 3'-end libraries from spatial cDNA amplification products.

### 推荐操作建议
- 模板: `To avoid <potential_issue>, it is recommended to <action>.`
- 例句: To avoid cross-contamination of samples, it is recommended to use filtered pipette tips and change tips when aspirating.

### 通用条件限制
- 模板: `Unless otherwise specified, <reagent> is used for <action>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids for reagent dilution in this experiment.

### 混合离心操作
- 模板: `<action_1>, centrifuge briefly, then <action_2>.`
- 例句: Vortex to mix, centrifuge briefly, then place in the PCR instrument and perform amplification according to the reaction program.

### 室温平衡准备
- 模板: `Take <item> out at least <time> in advance to equilibrate to room temperature.`
- 例句: On the day of the experiment, take the Stop Buffer out at least 30 minutes in advance to equilibrate to room temperature.

### 禁止性操作
- 模板: `Do not <action> at once; <reason>.`
- 例句: Do not dilute all TME at once; the amount provided in the kit is sufficient for at least 4 dilutions.

### 体系配制
- 模板: `Prepare the <item_mix> according to Table <table_number>.`
- 例句: Prepare the fragmentation Mix according to Table 2-1.

### 检测记录
- 模板: `Measure the concentration using <kit_name> and record it.`
- 例句: Take 1 μL of PCR product, measure the concentration using the Qubit dsDNA HS Kit, and record it.

### 上清处理
- 模板: `Add <amount> of <item> to the supernatant, mix by vortexing, and incubate at room temperature for <time>.`
- 例句: Add 15 μL of magnetic beads to the supernatant, mix by vortexing, and incubate at room temperature for 5 min;

### 法规处理
- 模板: `All <items> should be disposed of in accordance with relevant regulations.`
- 例句: All samples and all waste materials should be disposed of in accordance with relevant regulations.

### 步骤添加/重悬
- 模板: `Add <quantity> of <component> to <action>.`
- 例句: Add 24 μL of Nuclease-Free water to resuspend

### 磁力架操作
- 模板: `Keep <object> on <location> and <action>.`
- 例句: Keep the tube on the magnetic stand and add 400 μL of 80% ethanol to wash

### 混合比例
- 模板: `Mix <object_a> with <object_b> in a <ratio> ratio.`
- 例句: Mix the PCR product (final volume ~100 μL) with magnetic beads equilibrated to room temperature in a 1:2 ratio

### 质量控制要求
- 模板: `QC requires <object> to be <condition>.`
- 例句: QC requires fragments to be distributed around 200-250 bp

### 注意事项
- 模板: `Note: <action_1> and <action_2>.`
- 例句: Note: Remove the supernatant and retain the pellet.

### 条件句
- 模板: `If <condition>, <result>.`
- 例句: If different libraries use the same barcode combination, they cannot be sequenced in the same lane.

### 方法定义
- 模板: `<Topic> method: <action>.`
- 例句: Mixing method for different PCR Barcode Primer Mixes: Combine equal volumes to prepare the Mix, then add to the sample.

### 预防性禁止
- 模板: `Avoid <action> to prevent <negative_consequence>.`
- 例句: Gently open the tube cap, preventing liquid splashing and avoiding cross-contamination.

### 用途限制
- 模板: `This product is for <purpose_1> only and not for <purpose_2> purposes.`
- 例句: This product is for research use only and not for diagnostic purposes.

### 关键步骤提示
- 模板: `<Label>: Pay special attention to <target> to avoid <risk_1> or <risk_2>.`
- 例句: Key Steps: Pay special attention to these steps to avoid experimental failure or poor results.

### 停止点说明
- 模板: `Stopping point: You can pause the <process> here and <action> the <target>.`
- 例句: Stopping point: You can pause the experiment here and store the samples.

### 存储指令
- 模板: `Please <action> the <item> according to the <conditions> as soon as possible.`
- 例句: Please store the product according to the specified conditions as soon as possible.

### 授权禁止指令
- 模板: `Without the written consent of this organization, no one may <action_list>.`
- 例句: Without the written consent of this organization, no one may use, modify, reproduce, or pub- without authorization.

### 组成说明
- 模板: `Each <item_set> consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### 规格参数
- 模板: `<Spec_Name>: <value_range>.`
- 例句: Storage temperature: -25°C to -18°C.

### 操作指令 - 祈使句
- 模板: `<verb> <object> from <source>;`
- 例句: a. Take out the fixture and gasket from the Stereo-seq Slide Accessory Kit;

### 条件句 - 建议或允许
- 模板: `You may <verb> <object> to <verb> with <tool>.`
- 例句: You may choose any one of the listed brands (marked with *) to use with the PCR adapter.

### 条件句 - 必须或禁止
- 模板: `<subject> must <verb> <condition>.`
- 例句: A desiccant must be placed in the aluminum sealed bag to maintain dry conditions.

### 步骤衔接 - 描述动作状态
- 模板: `With the <object1> <state>, <verb> the <object2> into the <object1>, ensuring <clause>.`
- 例句: b. With the fixture upside down, insert the gasket into the fixture, ensuring the hole cutouts of the fixture and the gasket are aligned.

### 产品说明 - 包含关系
- 模板: `The <product> contains <quantity> <component1>, and each <component1> has <quantity> <component2> attached to it.`
- 例句: The chip box contains 4 carriers, and each of the 4 chip carriers has one Stereo-seq chip T (1cm*1cm) attached to it.

### 建议 - 选择指南
- 模板: `For <item>, <Brand1> is preferred, while <Brand2> is a domestic alternative.`
- 例句: For hematoxylin, Brand 1 is preferred, while Brand 2 is a domestic alternative.

### 用量/规格表达
- 模板: `<item> - <quantity> EA`
- 例句: Sealing film - 6 EA

### 储存/运输说明
- 模板: `Storage temperature: <temp_range>; Validity period for <transport_type> transport: see label.`
- 例句: Storage temperature: -25°C to 8°C; Shelf life for cold chain transport: see label

### 可选配置说明
- 模板: `<Item> (Optional)`
- 例句: Labnet Slide Spinner (Optional) C1303-T

### Action Instruction
- 模板: `Use <object> to <verb> <target>.`
- 例句: Use a canned air duster to blow away any impurities or debris from the surface as thoroughly as possible;

### Condition Assurance
- 模板: `Ensure <condition>.`
- 例句: Ensure the fixture and gasket do not come into contact with the chip surface;

### Pre-procedural Preparation
- 模板: `Prepare <object> in advance.`
- 例句: Prepare a foam box with crushed ice in advance and place the OCT on the ice to pre-cool for 10 min;

### Safety Constraint
- 模板: `Avoid <action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### Freshness Requirement
- 模板: `<object> should be prepared fresh before use.`
- 例句: 0.01N HCl (pH = 2.0) should be prepared fresh before use.

### 前置条件/前提动作
- 模板: `Pre-<verb> <object> to <target> (<prep> <detail>)`
- 例句: Pre-set the PCR instrument temperature to 37°C and the lid temperature to 42°C, then place the PCR adapter to equilibrate

### 条件判定与执行
- 模板: `If <condition>, <verb> <object>; if <condition>, <verb> <object>.`
- 例句: If the specimen head temperature is too low, it will cause cracks in the sections; if the temperature is too high, it will cause wrinkles.

### 结果确认
- 模板: `Ensure <object> is <state> (before <action>)`
- 例句: Ensure the eosin solution immerses all chips (adjust according to tissue staining uniformity, control staining time within 3-5 min).

### 禁止/警示
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the chip surface.

### 建议/推荐
- 模板: `It is recommended to <verb> <object> <time/condition>.`
- 例句: For the same tissue, it is recommended to keep the staining time consistent.

### 数值/用量描述
- 模板: `<verb> <amount> <unit> <object> (to <action>)`
- 例句: Apply 100 μL of hematoxylin staining solution (containing 5% RI) onto the chip surface.

### 持续状态/保持
- 模板: `<verb> <object> <prep> <state> for <duration>`
- 例句: Place the carrier on the desktop to equilibrate to room temperature for 1 min.

### 并列循环操作
- 模板: `Repeat steps <range> until <condition>`
- 例句: Repeat steps 2)-3) until all tissue slices are adsorbed onto the chip surface (control the mounting time to within 1 min).

### 操作指令：动作+对象+方式/量
- 模板: `<verb> <amount/object> <prepositional phrase>`
- 例句: Slowly add 100 μL of 0.01N HCl solution dropwise onto the chip.

### 前置条件/步骤衔接
- 模板: `Once <event>, <verb> <action>.`
- 例句: Once the H&E Mounting Medium has fully infiltrated the chip, immediately proceed with imaging.

### 确保要求
- 模板: `Ensure <subject> <is/are> <condition>.`
- 例句: Ensure the chip is completely submerged in the solution.

### 预防性禁止/避免
- 模板: `Avoid <gerund> <object>.`
- 例句: Avoid touching the front side of the chip when assembling the carrier.

### 准备工作
- 模板: `<Verb> <object> in advance.`
- 例句: Prepare the 1X Permeabilization Reagent working solution in advance.

### 步骤提醒/警示
- 模板: `<Subject> must be <verb-ed> <adverb>.`
- 例句: RT Mix must be added immediately to avoid RNA degradation.

### 条件判定
- 模板: `If <condition>, <verb> <action>.`
- 例句: If a large area is not infiltrated by the H&E Mounting Medium, then you need to add modeling points to this area.

### 状态保持指令
- 模板: `Keep the <container> on the <device> while <action>.`
- 例句: While keeping the centrifuge tube on the magnetic stand, add 1 mL of 80% ethanol...

### 顺序操作衔接
- 模板: `<verb> <object>, then <verb> <object>.`
- 例句: Briefly centrifuge, then place the centrifuge tube on a magnetic stand and let it stand for 3 min;

### 操作注意事项（否定式）
- 模板: `Avoid <gerund> <object>, as <reason>.`
- 例句: When aspirating the supernatant after elution, avoid disturbing the magnetic beads, as drawing them into the pipette tip may affect subsequent purification reactions.

### 结果记录/判断
- 模板: `<verb> <object> and <verb> the result.`
- 例句: Take 1 μL of the cDNA sample, measure the concentration using the Qubit dsDNA HS Kit, and record the result;

### 物料处理/平衡
- 模板: `<verb> <object> <adverbial_phrase_of_time_or_state>.`
- 例句: Mix the recovery solution from the previous step (450-490 μL) with the magnetic beads equilibrated to room temperature...

### 负面限制
- 模板: `Do not <verb> <object>.`
- 例句: Do not pipette up and down or disturb the magnetic beads.

### 参数变更描述
- 模板: `<Parameter> changed from <Value_old> to <Value_new>`
- 例句: Methanol pre-cooling time changed from 10-30 min to 5-30 min

### 产品组成说明
- 模板: `Each reagent kit consists of the following <Number> parts:`
- 例句: Each reagent kit consists of the following three parts:

### 步骤状态更新
- 模板: `<Procedure> updated.`
- 例句: Fluorescence imaging procedure updated.

### 操作建议/条件句
- 模板: `If <Condition>, the <Action> may be <Verb_past_participle> up to <Time>.`
- 例句: If tissue removal is incomplete, the removal time may be extended up to 16 h.

### 强制执行/使用建议
- 模板: `Please download the latest version of the instruction manual and use it with the corresponding version of the kit.`
- 例句: Please download the latest version of the instruction manual and use it with the corresponding version of the kit.

### 物料自备声明
- 模板: `(Sold separately) <Item_name> *<Number> (<Quantity>)`
- 例句: (Sold separately) Stereo-seq PCR Adapter *1 (2 EA)

### 关键步骤警示
- 模板: `Pay special attention; <Risk_description> may cause the experiment to fail.`
- 例句: Note: Pay special attention; improper operation or negligence may cause the experiment to fail.

### 参数标准化描述
- 模板: `<Parameter> standardized to <Value>.`
- 例句: PR Rinse Buffer solution (containing 5% RI) volume standardized to 200 μL.

### 实验点操作引导
- 模板: `In the <Checkpoint>, the volume of <Reagent> has been changed from <Value_old> to <Value_new>.`
- 例句: In the QC checkpoint of the cDNA purification step, the volume of Nuclease-free Water has been changed from 20 μL to 40 μL

### 成品及说明书命名
- 模板: `<Product_name> (<Version>) Instruction Manual`
- 例句: Stereo-seq Transcriptomics Kit (Chip Version) Instruction Manual

### Conditional Recommendation
- 模板: `If <condition>, it is recommended to <action>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transportation.

### Post-receipt Action
- 模板: `After receiving the <object>, please refer to <reference> to <action>.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to properly save the product.

### Conditional Action Suggestion
- 模板: `If <condition> is detected, you may <action>.`
- 例句: If an abnormality in the cold chain box temperature is detected, you may request the logistics provider to print the record table.

### Imperative Step
- 模板: `<Action verb> <object>, ensuring that <condition>.`
- 例句: With the reverse side of the fixture facing up, insert the gasket into the fixture, ensuring that the hole cutouts of the fixture and gasket are aligned.

### Purpose-driven Action
- 模板: `<Action verb> <object> to ensure <desired_state>.`
- 例句: Press along both sides of the fixture cassette to ensure the fixture is securely assembled with the chip slide.

### Requirement Constraint
- 模板: `<Object> must not be <action/state> for more than <duration>.`
- 例句: Resealed chips must not be stored for more than two weeks.

### Document Scope
- 模板: `This list outlines the <items> required for this experiment.`
- 例句: This list outlines the equipment and materials required for this experiment.

### 实验推荐句式
- 模板: `It is recommended to <verb> <object> <time/condition>.`
- 例句: It is recommended to take out the reagent components in advance.

### 目的导向的建议句式
- 模板: `To <purpose>, it is recommended to <verb> <object>.`
- 例句: To avoid sample cross-contamination, it is recommended to use filter tips and to change the tip when pipetting different samples.

### 预处理指令句式
- 模板: `Pre-cool the <object> to <temperature/state> in advance.`
- 例句: Pre-cool the cryostat chamber to −20°C and the specimen head to −15°C to −10°C in advance.

### 试剂处理标准句式
- 模板: `Briefly centrifuge the <object> and keep them on ice for use.`
- 例句: Briefly centrifuge the enzyme components and keep them on ice for use.

### 约束条件句式
- 模板: `The <property> of <object> should not exceed <value>.`
- 例句: The tissue size should not exceed 0.9 cm × 0.9 cm × 2 cm.

### 应急处理句式
- 模板: `In case of <event>, <action> immediately.`
- 例句: In case of accident, please immediately rinse with plenty of water and seek medical attention.

### 默认条件句式
- 模板: `Unless otherwise specified, <material> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids used to dilute reagents in this experiment.

### 空间位置与操作句式
- 模板: `Place <object> <location> and <action> for <duration>.`
- 例句: Place the metal block into dry ice with the flat surface facing up and pre-cool for at least 5 minutes.

### Direct Instruction
- 模板: `<verb> <object> <location/method>.`
- 例句: Mount the tissue block onto the specimen holder using OCT;

### Condition-based Action
- 模板: `Once <condition>, <imperative_action>.`
- 例句: Once the chip surface is free of impurities, visible marks, liquid residue, and ripple-like textures, it is ready for mounting;

### Conditional Consequence
- 模板: `If <condition>, it will cause <consequence>.`
- 例句: If the specimen chuck temperature is too low, it will cause cracks in the sections;

### Sequential Instruction
- 模板: `After <event_completion>, <imperative_action>.`
- 例句: After fixation is complete, transfer the slide box or 50 mL centrifuge tube to a fume hood;

### Prohibition
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the chip surface.

### Dosage Instruction
- 模板: `Add <amount> of <substance> <target>.`
- 例句: Add 100 μL of Wash Buffer to the chip;

### 操作指令（简单动作）
- 模板: `<verb> <object> (<detail>).`
- 例句: Add PR Rinse Buffer solution (containing 5% RI, volume: 200 μL/chip);

### 条件衔接
- 模板: `After <event> is complete, <verb> <object>.`
- 例句: After permeabilization is complete, remove the handheld carrier from the PCR instrument (37°C);

### 确保性声明
- 模板: `Ensure <subject> is <condition>.`
- 例句: Ensure the chip is completely covered by the 1X permeabilization reagent working solution.

### 预处理与平衡
- 模板: `<verb> <object> in advance to <action>.`
- 例句: Take out RT Reagent, RT Additive, and RT Oligo in advance to thaw at room temperature.

### 步骤参考
- 模板: `Refer to <step/table> to <action>.`
- 例句: Refer to step 1.6 to assemble the gasket and clamp into a carrier (without the chip carrier).

### 禁止/警告
- 模板: `Avoid <gerund> <object>.`
- 例句: Avoid contact with the face of the chip when assembling the carrier.

### 温度与时间设置
- 模板: `<temperature>, <time>.`
- 例句: 42°C, 3-16 hr

### 推荐/建议
- 模板: `It is recommended to <verb> <object>.`
- 例句: This reagent kit recommends using VAHTS DNA Clean Beads or AMPure® XP for bead purification.

### 异常处理
- 模板: `If <condition> is observed, <action>.`
- 例句: If white precipitates are observed in the buffer, it can be dissolved at 55°C and the temperature restored to room temperature.

### 过程观察要求
- 模板: `Wait until <condition>, <action>.`
- 例句: Wait until the liquid is thoroughly clear before aspirating the supernatant, which generally takes 2-3 min.

### 操作方式/频率
- 模板: `<verb> <object> by <method>.`
- 例句: After mixing well by vortexing, take 1 μL of PCR product

### 用量/合并表达
- 模板: `<verb> to <location>, combining to a total volume of <volume>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to the PCR tube from step 8, combining to a total volume of ~42 μL.

### 符合性/合规性
- 模板: `Nothing herein is intended or shall be construed as <guarantee>.`
- 例句: Nothing herein is intended or shall be construed as any guarantee of the performance of any product listed or described herein

### Reference_Instruction
- 模板: `Please refer to <document_name> to <action> <object> <adverb>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### Condition_Clause
- 模板: `When <condition> are met, <object> will <action>.`
- 例句: When transportation, storage, and usage conditions are met, all components will maintain full activity throughout their validity.

### Selection_Instruction
- 模板: `Select one of the <item_description> (marked with <symbol>).`
- 例句: Select one of the listed brands (marked with *).

### Warning_Note
- 模板: `<Heading>: Pay special attention to <object> to avoid <consequence>.`
- 例句: Critical steps: Pay special attention to these steps to avoid experiment failure or poor results.

### Detail_Reference
- 模板: `For details, please refer to <document_name>.`
- 例句: For details, please refer to "Stereo-seq Library Preparation Kit Instruction Manual".

### Composition_Description
- 模板: `Each <set_name> consists of the following <number> parts:`
- 例句: Each reagent set consists of the following three parts:

### Recommendation_Conditional
- 模板: `If <condition> is <state>, it is recommended to <action>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transport.

### List_Disclaimer
- 模板: `<Table_reference> do not include standard laboratory equipment, such as <list_of_items>, etc.`
- 例句: Tables 1-5 do not include standard laboratory equipment, such as ice machines, biosafety cabinets, pH meters, refrigerators, etc.

### 强制性要求/规定
- 模板: `[Subject] must <verb> <object> in accordance with <standard>.`
- 例句: All samples and waste materials must be disposed of in accordance with relevant regulations.

### 数值/尺寸限制
- 模板: `[Subject] should not exceed <limit>.`
- 例句: The tissue size should not exceed 0.45 cm × 0.45 cm × 2 cm.

### 安全警示/禁止
- 模板: `Avoid <action> with <substance>.`
- 例句: Avoid direct contact of skin and eyes with samples and reagents.

### 资料引用
- 模板: `For details, please refer to <title>.`
- 例句: For details, please refer to the "Stereo-seq Reagent Kit Recommended Samples".

### 规格描述
- 模板: `<quantity> <unit> <adjective> <noun>`
- 例句: 1000 µL filter pipette tip

### 步骤说明
- 模板: `<verb> <object> <complement>`
- 例句: Place the tissue into the pre-cooled OCT on ice.

### 操作建议/推荐
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to aliquot the prepared 10X Permeabilization Reagent Stock Solution to avoid repeated freeze-thaw cycles.

### 频率/周期提醒
- 模板: `<subject> must be <verb> <time_constraint>.`
- 例句: 0.01N HCl (pH = 2.0) must be prepared fresh before use.

### 预处理/准备工作
- 模板: `<action> <target> <time_frame> before use.`
- 例句: Take out Glycerol at least 5 minutes before use and equilibrate to room temperature.

### 参数/浓度调控
- 模板: `Dilute <reagent> to <concentration> (at least <quantity> per <unit>).`
- 例句: Dilute 0.01N HCl according to the HCl concentration gradient to 0.01N (ensure the pH value is in the 1.9-2.1 range; at least 2 mL/sample).

### Add Reagent
- 模板: `Add <amount> of <reagent> onto the <target>.`
- 例句: Add 30 μL of tissue fluorescence staining solution onto the chip per chip.

### Aspirate Liquid
- 模板: `Use a pipette to aspirate <object> from one corner of the <target>.`
- 例句: Use a pipette to aspirate the tissue fluorescent staining solution from one corner of the chip.

### Ensure Coverage
- 模板: `Ensure the <target> is completely covered by the <solution>.`
- 例句: Ensure the chip is completely covered by the tissue fluorescence staining solution.

### Ensure Cleanliness
- 模板: `Ensure that there is no residual <substance> on the <target>.`
- 例句: Ensure that there is no residual staining solution on the chip.

### Instructional Transfer
- 模板: `Transfer the <object> onto <target>.`
- 例句: Transfer the carrier onto a lint-free wipe.

### Warning Against Dryness
- 模板: `Avoid letting the <target> dry out completely.`
- 例句: Avoid letting the chip dry out completely.

### Equipment Setup
- 模板: `Adjust the <parameter> of <instrument> to <value> in advance.`
- 例句: Adjust the reaction temperature of another PCR instrument to 42℃ in advance.

### Troubleshooting
- 模板: `If <condition> fails, please carefully check <aspect> and <action>.`
- 例句: If QC fails, please carefully check the image clarity and adjust the imaging method.

### Preparation
- 模板: `Prepare <amount> of <reagent> and <reagent> in advance.`
- 例句: Prepare 2 mL of 0.01N HCl and the 1X permeabilization reagent working solution in advance.

### 操作与反应指令
- 模板: `Add <reagent> (<volume>/<unit>), then <verb> it <location> and <verb> for <duration>.`
- 例句: Add TR Buffer (400 μL / chip), then place it on the PCR adapter of the PCR instrument (55℃) and incubate for 10 min;

### 试剂配制指引
- 模板: `Prepare the <mixture> according to <table_reference>.`
- 例句: Prepare the cDNA Release Mix according to Table 3-3 and keep it at room temperature.

### 离心与磁力架分离
- 模板: `After brief centrifugation, place the <tube_type> on a magnetic stand and let it stand for <duration>.`
- 例句: After brief centrifugation, place the centrifuge tube on a magnetic stand and let it stand for 3 min;

### 建议与备注
- 模板: `For <purpose>, we recommend <verb>ing <amount> of <substance>.`
- 例句: For subsequent troubleshooting, we recommend retaining 2 µL of the PCR product.

### 条件性处理指令
- 模板: `If <condition>, <verb> <substance> to <action>.`
- 例句: If tissue removal is incomplete, add 400 μL of 0.1X SSC, gently pipette up and down to remove the tissue from the chip

### 预处理指引
- 模板: `Take out the <reagent> in advance. If <observation> is observed in the buffer, it can be <verb> at <temperature>, and then <verb>.`
- 例句: Take out the TR buffer in advance. If white precipitate is observed in the buffer, it can be dissolved at 55°C, and then restore to room temperature.

### 禁止操作提示
- 模板: `When <verb>ing the <object>, take care not to <verb> the <restricted_object>.`
- 例句: When separating the magnetic beads from the liquid, take care not to let the pipette tip touch the magnetic beads.

### 定量混合操作
- 模板: `Mix the <substance_A> (<amount>) with <substance_B> at a <ratio> ratio, <verb> to mix, and <verb> at <temperature> for <duration>.`
- 例句: Mix the PCR products (100 μL) with magnetic beads equilibrated to room temperature at a 1:1 ratio, vortex to mix, and incubate at room temperature for 10 min;

### 离心管/样本移动
- 模板: `Transfer the <substance> to <destination>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 标准存储建议
- 模板: `<Object> can be stored at <Temperature> for <Duration>.`
- 例句: The purified cDNA product can be stored at −20°C for 1 month.

### 条件存储建议
- 模板: `<Object> can be stored in <Volume> of <Reagent> at <Temperature> until <Condition>.`
- 例句: The beads can be stored in 40 µL of Nuclease-free Water at 4°C until the final cDNA product passes QC.

### 技术指标要求
- 模板: `The <Object> is required to be at <Specification>.`
- 例句: The main peak of the fragment distribution is required to be at 1000–1500 bp.

### 外部引用建议
- 模板: `For <Subject>, please refer to <Reference>.`
- 例句: For specific procedures for subsequent library construction, please refer to the "Stereo-seq Library Preparation Kit User Manual".

### 引用指示
- 模板: `For <Subject>, see <Reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., see Table 1-1 to Table 1-5.

### 用途约束
- 模板: `This product is for <Use>, not for <Restriction>.`
- 例句: This product is for research use only, not for diagnostic use.

### 标签化提示/警告
- 模板: `<Label>: <Instruction>.`
- 例句: Tip: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 组成结构描述
- 模板: `Each <Object> consists of the following <Number> parts:`
- 例句: Each reagent kit consists of the following three parts:

### 条件建议/指导
- 模板: `If <condition>, it is recommended to <action>.`
- 例句: If the transfer time is long, it is recommended to use a temperature-controlled container for transport.

### 信息标注
- 模板: `<attribute>: see label`
- 例句: Cold chain transportation validity: see label

### 组分清单/规格
- 模板: `<Component_Name> <Cat_No_Placeholder> <Specification_Placeholder>`
- 例句: Stereo-seq Chip P Carrier (1 cm * 1 cm) - 8 EA

### 特定选择指令
- 模板: `Select any one from the listed brands (marked with *).`
- 例句: Select any one from the listed brands (marked with *).

### 存储条件说明
- 模板: `Store the product under the specified conditions.`
- 例句: Please store the product under the specified conditions as soon as possible.

### 通用实验流程声明
- 模板: `Unless otherwise specified, <material> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids intended for reagent dilution in this experiment.

### 安全操作警告
- 模板: `Avoid direct contact of <substance> with <part>, do not swallow <substance>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 试剂准备建议
- 模板: `It is recommended to <action> before use.`
- 例句: It is recommended to preheat the PCR thermal cycler to the reaction temperature.

### 产品用途限制
- 模板: `This product is for research use only and is not intended for <application>.`
- 例句: This product is for research use only and is not intended for clinical diagnostic procedures.

### 步骤执行与动作
- 模板: `<verb> <object> at <temperature/time>.`
- 例句: Remove 4% PFA from -20°C, thaw and mix well.

### 试剂配制与稀释
- 模板: `For <reagent_name>: take <volume> of <stock_reagent> and dilute to <total_volume> with <diluent>; keep at <storage_condition>.`
- 例句: For 5X SSC: take 5 mL of 20X SSC and dilute to 20 mL with Nuclease-Free Water; keep at room temperature.

### 操作限制与禁止
- 模板: `Do not <action> the <object>; <alternative_action> instead.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 操作建议与警示
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: It is recommended to aliquot the prepared 10X Permeabilization Reagent stock solution to avoid repeated freeze-thaw cycles.

### 顺序设置
- 模板: `Set in sequence: <temperature> for <process> (lid temperature <temp>), <temperature> for <process> (lid temperature <temp>).`
- 例句: Set in sequence: 37°C for slide baking and permeabilization (lid temperature 42°C), 70°C for de-crosslinking (lid temperature 75°C).

### 液体添加与孵育
- 模板: `Add <volume> of <reagent> per chip and incubate at <temperature> for <time>.`
- 例句: Add 4% PFA solution at a dosage of 400 μL/chip, and incubate for 10 min.

### 液体弃除与润湿
- 模板: `Aspirate <reagent> from <location>, while keeping the tissue on the chip moist.`
- 例句: Aspirate the Wash Buffer solution from one corner of the chip, keeping the tissue on the chip moist.

### 实验预防与风险
- 模板: `Strictly avoid <condition> during <process>, as it can easily lead to <result>.`
- 例句: Strictly avoid tissue desiccation during liquid exchange, as tissue desiccation can easily lead to non-specific signals.

### 使用时机
- 模板: `<reagent_name>: Prepare immediately before use.`
- 例句: 0.01N HCl (pH = 2.0): Prepare immediately before use.

### 操作指令-加液
- 模板: `Add <volume> of <reagent_name> per chip,`
- 例句: Add 200 μL of Wash Buffer per chip and incubate for 1 min at room temperature;

### 操作指令-吸弃
- 模板: `Use a pipette to aspirate and discard the <reagent_name> from one corner of the chip,`
- 例句: Slightly tilt the handheld carrier at an angle of less than 20°, use a pipette to aspirate and discard the Wash Buffer from one corner of the chip,

### 操作条件-倾斜
- 模板: `Slightly tilt the handheld carrier at an angle of less than <angle>°,`
- 例句: Slightly tilt the handheld carrier at an angle of less than 20°,

### 操作条件-孵育
- 模板: `incubate for <time> at <temperature>,`
- 例句: incubate for 1 min at room temperature;

### 步骤衔接-重复
- 模板: `Repeat <steps> once;`
- 例句: Repeat steps e.-f. once;

### 密封操作
- 模板: `Seal the carrier with a <sealing_method>;`
- 例句: Seal the carrier with a plate sealing film;

### 试剂添加指令
- 模板: `Add <volume> of <reagent_name> <dosage_unit>;`
- 例句: Add 400 μL of 0.1X SSC solution per chip;

### 文献引用指令
- 模板: `Refer to <manual_name> to <action>;`
- 例句: Refer to Chapter 3 of the "Stereo-seq Chip Carrier and Accessories Instruction Manual" to disassemble the handheld carrier;

### 限制约束条件
- 模板: `<subject> should only contain <allowed_elements>; <restricted_elements> are prohibited.`
- 例句: Folder names should only contain letters, numbers, and underscores; special characters such as spaces are prohibited.

### 配制参考指令
- 模板: `Prepare the <reagent_mix> according to <reference_source>;`
- 例句: Prepare the Total RNA Hybridization Mix according to Appendix Table 1;

### 条件解决建议
- 模板: `If <condition>, <action> to ensure <goal>;`
- 例句: If tissue removal is found to be incomplete and residual tissue exists, the removal time can be extended to ensure complete removal

### 判断标准定义
- 模板: `When <condition>, <criteria> is the standard for judging <goal>.`
- 例句: When the tissue is removed cleanly and imaging conditions are kept identical, the criteria for judging the optimal permeabilization time is whether the tissue morphology is complete, the fluorescence intensity is strong, and there is no diffusion.

### 计算公式说明
- 模板: `<parameter_name>: <formula>;`
- 例句: Total RNA input: X (μL) = 2 μg / Total RNA concentration (μg/μL).

### 提示/注意
- 模板: `Note: <instruction/warning>`
- 例句: Note: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 变更声明
- 模板: `Change in <object>`
- 例句: Change in chip carrier design format

### 参数变更
- 模板: `<parameter> changed from <old_value> to <new_value>`
- 例句: Methanol pre-cooling time changed from 10-30 min to 5-30 min

### 条件建议
- 模板: `If <condition>, <action/recommendation>`
- 例句: If tissue removal is incomplete, the removal time can be extended, not exceeding 16 hr

### 操作许可
- 模板: `You may <action> <option>`
- 例句: You may select any of the listed brands (marked with *) for use with the PCR adapter.

### 暂停指引
- 模板: `Stopping point: <action>`
- 例句: Stopping point: You may pause the experiment here and store the samples.

### 建议/推荐动作
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to preheat the PCR thermal cycler to the reaction temperature.

### 步骤衔接/指令
- 模板: `<Verb> the <object> to <purpose>.`
- 例句: Use a spatula to ensure the tissue is coated with OCT while avoiding air bubbles.

### 条件句/限制条件
- 模板: `To <purpose>, <action>.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended.

### 注意事项/禁止
- 模板: `Avoid <action/contact>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes.

### 物料清单描述
- 模板: `<Brand/Consumable> <Quantity>`
- 例句: Corning® 35 mm TC-treated Culture Dish 1

### 时间/期限限制
- 模板: `Within <time>, <action>.`
- 例句: Within 30 minutes of removing the fresh tissue, blot the surface liquid.

### 确认/检查动作
- 模板: `Ensure that <condition>.`
- 例句: Ensure that the hole cutouts of the fixture and gasket are aligned.

### 强制性规定
- 模板: `<Subject> must be <past participle>.`
- 例句: Resealed chips must not be stored for more than two weeks.

### 条件判断句
- 模板: `If <condition>, <action>; if not, <alternative_action>.`
- 例句: Check if the bottom of the embedded block is completely covered; if not, place the tissue block on the metal block with the bottom facing upward.

### 配制操作说明
- 模板: `Prepare <Reagent> by adding <amount> of <Component_A> to <amount> of <Component_B>.`
- 例句: Prepare Wash Buffer by adding 5 μL of RI to 95 μL of 0.1X SSC; required volume is at least 100 μL per chip.

### 建议与推荐
- 模板: `It is recommended to <action> <object> to <purpose>.`
- 例句: It is recommended to aliquot the prepared 10X Permeabilization Reagent stock solution to avoid repeated freeze-thaw cycles.

### 异常处理与条件建议
- 模板: `If <symptom>, <action>; <alternative>.`
- 例句: If the specimen head temperature is too low, it will cause cracks in the sections; if the specimen head temperature is too high, it will cause wrinkles.

### 完成条件判定
- 模板: `When <condition_a>, <condition_b>, and <condition_c>, <object> is ready for <process>.`
- 例句: When the chip surface is free of impurities, obvious marks, residual liquid, and rippled textures, it is ready for mounting.

### 临时暂停/特殊步骤
- 模板: `(Optional <step_type>) <action>.`
- 例句: (Optional pause point) Place the incubated chip carrier into a slide box or a 50 mL centrifuge tube, and quickly transfer to a -80°C freezer.

### 使用限制与前提
- 模板: `<Reagent> must be <condition> before use.`
- 例句: 0.01N HCl (pH = 2.0) must be freshly prepared before use.

### 注意事项/警示
- 模板: `Please <action> and <action>.`
- 例句: Please check that all Stereo-seq chip carriers in the slide box are correctly positioned in the slots, and the chip on the carrier is facing up.

### 添加试剂
- 模板: `Add <amount> of <reagent> onto/to <location>.`
- 例句: Add 100 μL of Total RNA Hybridization Mix onto the chip surface.

### 按指南/表格操作
- 模板: `<verb> <object> according to <reference>.`
- 例句: Prepare the Total RNA hybridization Mix according to Table 3-1;

### 器械操作指令
- 模板: `Slightly tilt <object>, and use a pipette to aspirate <substance> from <location>.`
- 例句: Slightly tilt the handheld carrier and use a pipette to aspirate the Total RNA Hybridization Mix from one corner of the chip.

### 试剂用量表达
- 模板: `Add <substance> at <amount>/<unit>.`
- 例句: Add Wash Buffer at 100 μL/chip;

### 实验现象描述
- 模板: `As shown in Figure <number>, at <time> of <process>, the <object> exhibited <phenomenon>.`
- 例句: As shown in Figure 3, at 3 min of permeabilization, the tissue exhibited uneven brightness within the same cortex.

### 产品功能定义
- 模板: `The <Product Name> is a <product type> designed for <purpose>.`
- 例句: The Stereo-seq FFPE Transcriptomics Reagent Kit is a reagent set designed for obtaining full transcriptomes from FFPE samples.

### 操作提示标签
- 模板: `<Label>: <Instruction>`
- 例句: Note: Please download the latest version of the user manual and use it with the corresponding version of the reagent kit.

### 文档引用指引
- 模板: `For details, please refer to <Document Name>.`
- 例句: For details, please refer to 《Stereo-seq 16 Barcode 建库试剂盒 V1.0 使用说明书》.

### 操作修改指令
- 模板: `<Verb> <Object>;`
- 例句: Revise kit shipping temperature;

### 用途限制声明
- 模板: `<Subject> is for <purpose> only, not for <prohibited purpose>.`
- 例句: This product is for research use only, not for diagnostic use.

### 责任免除声明
- 模板: `Nothing herein is intended or should be construed as <description>.`
- 例句: Nothing herein is intended or should be construed as any warranty regarding the performance of any product listed or described herein.

### 储存条件说明
- 模板: `Storage temperature: <temp_range>. Expiration date: <location>.`
- 例句: Storage temperature: −25°C to −18°C. Expiration date: See label.

### 一般操作建议
- 模板: `Please <verb> the <object> under the <condition>.`
- 例句: Please store the product under the specified conditions as soon as possible.

### 试剂配制流程
- 模板: `Add <amount_a> <reagent_a> to <amount_b> <reagent_b>, <method>, <storage_condition>.`
- 例句: Add 12.5 mL 20X SSC to 37.5 mL ddH2O, mix well, store at room temperature for 1 week.

### 引用指南句式
- 模板: `Please refer to the <document_title> to <action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product.

### 禁止操作句式
- 模板: `Do not <verb> the <object>; <alternative_method>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 安全警告句式
- 模板: `Avoid direct contact of <object> with <body_part>; <imperative_action>.`
- 例句: Avoid direct contact of samples and reagents with skin and eyes; do not swallow samples or reagents.

### 产品信息格式
- 模板: `<Component_Name> Cat. No.: <Catalog_Number>`
- 例句: STOmics FFPE Accessory Kit Cat. No.: 310AK002

### 操作指令-动作序列
- 模板: `Remove the <reagent> from <temperature> in advance, thaw <method>, and <post_action> during use.`
- 例句: Remove the FFPE RT Buffer Mix from -20°C in advance, thaw at room temperature, shake until no precipitate remains, and keep on ice during use.

### 实验步骤-条件句
- 模板: `If <condition>, <action>.`
- 例句: If an integrated slide flotation/drying workstation is unavailable, a slide flotation water bath combined with a PCR instrument can be used as a substitute.

### 操作建议-预防/要求
- 模板: `It is recommended that this procedure be performed by <person/condition>.`
- 例句: It is recommended that this procedure be performed by an experienced paraffin section technician.

### 温度设定-用途说明
- 模板: `<temperature> for <application> (hot lid <temperature>).`
- 例句: 85°C for H&E decolorization (hot lid 85°C)

### 禁止/忽略操作
- 模板: `If <selection>, please <action> and skip <section>.`
- 例句: If opting for H&E staining, please follow Section 2.3.1 for experimental procedures and skip Section 2.3.2.

### 设备准备
- 模板: `Turn on the <equipment> in advance, and set the <parameter> to <value>.`
- 例句: Turn on the integrated slide flotation/drying workstation in advance, and set the water bath temperature to 40~48°C.

### 保存条件
- 模板: `When unopened, the product can be stored at <temperature> until <deadline>.`
- 例句: When unopened, the product can be stored at -20 °C or 4 °C until the expiration date on the label.

### 步骤衔接-确认与动作
- 模板: `After <completed_action>, <action>.`
- 例句: After the tissue section is completely flattened, take out the Stereo-seq chip N carrier, record the chip ID, and take care not to touch the chip surface.

### 故障排查-对照表结构
- 模板: `If the <status>, the <reason> is <factor>; <action>.`
- 例句: If the tissue section consistently shows wrinkles, the temperature is too low; increase the water bath temperature by 0.5 -1℃, continue to observe, until the tissue is completely flattened.

### 操作要点提示
- 模板: `Note that after <action>, <warning>.`
- 例句: Note that after mounting, air bubbles should be avoided on the surface of the chip section.

### 条件句（如果...请...）
- 模板: `If <condition>, please <action>.`
- 例句: If you find that the product has the above-mentioned issues, please promptly report the situation to your scientific cooperation representative.

### 步骤衔接（动作序列）
- 模板: `<step1_action>, then <step2_action>.`
- 例句: Verify that the aluminum bag is intact and properly sealed, then immediately store it at -20°C or 4°C.

### 检查事项（引导）
- 模板: `Please check the following items <context>:`
- 例句: Please check the following items after opening the aluminum bag:

### 目的状语（为了保证...）
- 模板: `To ensure <goal>, <subject> are <adverb> <verb_past_participle> <location>.`
- 例句: To ensure stability during transport, large chips are adhered securely to the bottom of the transparent chip box.

### 试剂配制（加法/混合）
- 模板: `Add <amount> <reagent> to <amount> <diluent>, mix well, and <action>.`
- 例句: Add 4 mL of ddH2O to 96 mL of anhydrous ethanol, mix well, and fill 2 staining jars.

### 用量与体积说明
- 模板: `The volume should be sufficient to <action>.`
- 例句: The volume should be sufficient to completely submerge the chip.

### 步骤说明（耗时）
- 模板: `<action> for <duration> <unit>.`
- 例句: Place the baked Stereo-seq chip N carrier into Histo-clear ① for 20 min at room temperature.

### 禁止/警告（不可...）
- 模板: `<subject> must not <verb> <duration>.`
- 例句: Non-vacuum-sealed chips must not be placed for more than two weeks.

### 信息指引（网址/邮箱）
- 模板: `<label>: <content>`
- 例句: Email: services@stomics.tech

### 添加试剂操作
- 模板: `Add <amount> of <reagent> to <container>, <action>, and ...`
- 例句: Add 20 mL of 70% ethanol to 10 mL of Eosin (Abcam 'AB246824'), mix well, and transfer to a staining jar...

### 试剂预平衡操作
- 模板: `Take out the <reagent> from <temp1> in advance and equilibrate it to <temp2> for <purpose>.`
- 例句: Take out the FFPE Mounting Medium from -20°C in advance and equilibrate it to room temperature for mounting.

### 禁止操作与预警
- 模板: `Do not <action>, as this can easily cause <consequence>.`
- 例句: Do not preheat the TE buffer, as this can easily cause section detachment.

### 条件判断与修正
- 模板: `If <condition>, please <action> to <purpose>.`
- 例句: If QC fails, please carefully check the image clarity, adjust the imaging method, and retake the photos to ensure clear...

### 浸入与清洗操作
- 模板: `Immerse the <object> in <container> containing <reagent> and <action>.`
- 例句: Immerse the carrier in a staining jar (or slide box, or 50 mL centrifuge tube) containing 5X SSC, and rinse by moving...

### 直接执行操作
- 模板: `<verb> <amount> of <object> into the <container>, and <action>.`
- 例句: Add 400 μL of TE Buffer (pH 9.0), equilibrated to room temperature, into the wells of the carrier chip, and incubate...

### Reagent Preparation
- 模板: `<reagent_name>: Add <amount1> of <reagent1> to <amount2> of <reagent2>, mix well <purpose>.`
- 例句: 5X SSC: Add 100 μL of 20X SSC to 300 μL of ddH2O, mix well to prepare ssDNA staining solution.

### Imperative Sequential Action
- 模板: `<verb> <object> to/into <target>, <condition/time>; then <verb> <object> to <target2> <purpose/condition>.`
- 例句: Place the baked Stereo-seq chip N substrate into Histo-clear ①, at room temperature for 20 min; then Take it out and place it in Histo-clear ② for 20 min at room temperature.

### Device Setup
- 模板: `Pre-turn on <device> (or <alternative_device>), and set the <parameter> to <value>;`
- 例句: Pre-turn on the slide dryer/spreader (or slide dryer, metal bath, etc.), and set the slide drying temperature to 60°C;

### Prohibitive Instruction
- 模板: `During <process>, do not <action> for an extended period; <action2> to avoid <consequence>;`
- 例句: During imaging, do not expose the chip with tissue attached to fluorescence for an extended period; turn off the laser to avoid prolonged exposure;

### Action with Precaution
- 模板: `Then, add <amount> of <reagent> to <action> (take care to <precaution>);`
- 例句: Then, add 3-5 μL of FFPE Mounting Medium to mount and image (take care to ensure there are no bubbles in the tissue);

### Sequential Washing/Transfer
- 模板: `Remove the <object>, blot off the excess <substance> with <material>, and place it sequentially into <target1> for <time1>, <target2> for <time2>...`
- 例句: Remove the Stereo-seq Chip N carrier, blot off the excess Histo-clear with lint-free paper, and place it sequentially into 100% ethanol ① for 5 min, 100% ethanol ② for 5 min.

### 添加与封口操作
- 模板: `Add <volume> of <reagent> to <location>, <action>, and <action>`
- 例句: Add 400 μL of FFPE Decrosslinking Reagent to the wells of the carrier chip, apply the sealing film, and seal

### 设备交互与步骤跳转
- 模板: `Place <object> onto <target>, click <command1> and click <command2> to <action>`
- 例句: Place the handheld carrier onto the PCR adaptor, click edit and click next step to skip

### 顺序执行动作
- 模板: `After <event> is complete, <action> <object> to <destination>`
- 例句: After the reaction is complete, carefully move the Stereo-seq chip N carrier with the holder to a nearby workbench

### 清洗操作
- 模板: `Wash once with <reagent>, <volume>/well.`
- 例句: Wash once with 0.1X SSC (containing 5% RI), 200 μL/well.

### 试剂预处理
- 模板: `Thaw <reagent1> and <reagent2> on ice in advance.`
- 例句: Thaw FFPE RT Oligo and FFPE Dimer on ice in advance.

### 添加试剂指令
- 模板: `Add <reagent> (volume <amount>/well), <action_1>, and <action_2>.`
- 例句: Add cDNA Release Mix (volume 400 μL / well), seal the wells with sealing film, and then place on

### 条件性溶解说明
- 模板: `If <condition> is observed in the <solution>, it can be <action_1> to dissolve, and then allowed to <action_2>.`
- 例句: If white precipitate is observed in the buffer, it can be incubated at 55°C to dissolve, and then allowed to return to room temperature.

### 反应后处理流程
- 模板: `After the reaction is complete, <action> the liquid from the <source> into a new <container>.`
- 例句: After the reaction is complete, completely recover the liquid from the reaction well into a new 2.0 mL centrifuge tube.

### 磁力架分离步骤
- 模板: `After <action>, place the <container> on a magnetic rack and let it stand for <time> until <state>.`
- 例句: After brief centrifugation, place the centrifuge tube on a magnetic rack and let it stand for 3 min until the liquid clears.

### 产品推荐描述
- 模板: `It is recommended to use <product> with this reagent kit.`
- 例句: It is recommended to use VAHTS with this reagent kit.

### 操作禁止警告
- 模板: `Do not <action> the <object> when <process>. If <object> is <actioned>, it may affect <result>.`
- 例句: Do not touch the magnetic beads when aspirating the supernatant after elution. If beads are aspirated, it may affect subsequent purification reactions.

### 试剂配置指令
- 模板: `Prepare the <solution> according to Table <num>, for a total of <volume>.`
- 例句: Prepare the PCR Mix according to Table 2-9, for a total of 100 μL;

### 补足体积说明
- 模板: `If the recovered <sample> is less than <volume>, make up the volume to <volume> with <reagent>.`
- 例句: If the recovered sample above is less than 42 μL, make up the volume to 42 μL with NF-H2O.

### 样本转移指令
- 模板: `Transfer the <source> (~<volume>) to a new <destination>.`
- 例句: Transfer the supernatant (~42 μL cDNA) to a new 0.2 mL PCR tube;

### 试剂/样本混合与操作
- 模板: `Mix <object> with <agent> at a <ratio> ratio, <action_1>, and <action_2>;`
- 例句: Mix the PCR products (100 μL) with room-temperature equilibrated beads at a 1:1 ratio, vortex to mix, and incubate at

### 离心与放置步骤
- 模板: `After a brief centrifugation, place <object> on a <location> and <action>;`
- 例句: After a brief centrifugation, place the PCR tube on a magnetic rack and let it stand for 3 minutes;

### 条件触发（步骤衔接）
- 模板: `Once <condition>, <action>;`
- 例句: once the solution澄清后去除上清 -> once the solution has cleared, remove the supernatant;

### 强制性参考
- 模板: `For specific procedures on <topic>, please refer to the <document_title>.`
- 例句: For specific procedures on subsequent library construction, please refer to the *Stereo-seq 16 Barcode Library Prep Kit Instruction Manual*.

### 产品合规性声明
- 模板: `This product is for <usage> use only, not for <usage_prohibited> use.`
- 例句: 1. This product is for research use only, not for diagnostic use.

### 材料需求声明
- 模板: `<section_title>: <items_list>`
- 例句: 1.4 Materials Required but Not Provided

### 样本特征对应描述
- 模板: `Fragment distribution of <object> corresponding to <condition>`
- 例句: Fragment distribution of purified cDNA product corresponding to RNA with DV200 < 30%

### 操作手册修改记录
- 模板: `· <action> <object>.`
- 例句: · Correct RT Mix preparation.

### 操作提示句式
- 模板: `Tip: <description>.`
- 例句: Tip: Additional operational hints and guidance.

### 警告/注意事项句式
- 模板: `Note: <description>; <consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experiment failure.

### 关键步骤强调
- 模板: `Key steps: Pay special attention to <target> to <purpose>.`
- 例句: Key steps: Pay special attention to these steps to avoid experimental failure or poor results.

### 操作暂停点
- 模板: `Stop Point: You can <action> at this point.`
- 例句: Stop Point: You can pause the experiment here and store the samples.

### 组成部分描述
- 模板: `Each <item> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 参考说明书/手册
- 模板: `For details, please refer to the "<document_title>".`
- 例句: For requirements regarding microscopes, please refer to the "Microscope Evaluation Manual".

### 进一步信息指引
- 模板: `For further information regarding <subject>, please refer to <reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Table 1-1 and Table 1-2.

### 产品应用描述
- 模板: `The <product_name> is used for <purpose>.`
- 例句: The STOmics Stereo-seq Customized Chip Transcriptome Reagent Kit is used for the construction of 3' end libraries from whole tissue slice samples.

### 操作流程引导
- 模板: `Upon receipt of <product>, please follow the "<guide_title>" to ensure <goal>.`
- 例句: Upon receipt of the Stereo-seq chip, please follow the "Stereo-seq Customized Chip Storage Guide" to ensure proper storage.

### 条件性建议
- 模板: `If <condition>, <action>.`
- 例句: If the transfer time is long, it is recommended to use temperature-controlled containers for transportation.

### 物料选择建议
- 模板: `You may choose any of the listed <items> (marked with *) for use.`
- 例句: You may choose any of the listed brands (marked with *) for use.

### 技术规格列举
- 模板: `<item_name> (<specification>)`
- 例句: Stereo-seq Chip T (1 cm * 2 cm)

### 步骤衔接句式
- 模板: `<verb> <object> to <verb> <target>`
- 例句: Use a spatula to ensure the tissue is encased in OCT

### 条件限制/建议句式
- 模板: `It is recommended to <verb> <object> before <verb>`
- 例句: It is recommended to take out the reagent components in advance, briefly centrifuge

### 操作目的说明句式
- 模板: `To <verb> <object>, <verb> <action>`
- 例句: To avoid sample cross-contamination, it is recommended to use filter pipette tips

### 参数/适用范围描述句式
- 模板: `This <noun> is suitable for <noun> with <noun> <comparison> <value>`
- 例句: This embedding method is suitable for tissues with dimensions < 2 cm × 3 cm × 0.7 cm

### 预处理/准备工作句式
- 模板: `<verb> <object> in advance and <verb> <object> for <time>`
- 例句: Prepare a foam box of crushed ice in advance and pre-cool the OCT on ice for 10 min

### 合规与处置句式
- 模板: `All <plural_noun> should be <verb_past_participle> in accordance with <noun>`
- 例句: All samples and various wastes should be disposed of in accordance with relevant regulations

### 强调/强建议句式
- 模板: `It is strongly recommended to <verb> <object> only on <noun>`
- 例句: It is strongly recommended to perform subsequent experiments only on tissue samples with RIN ≥ 7

### 条件操作
- 模板: `Check if <condition>; if not, <imperative verb> the <object> <condition/direction>.`
- 例句: Check if the bottom of the embedding block is completely covered; if not, place the tissue block on the metal block with the bottom facing upward

### 预处理目的
- 模板: `<Imperative verb> the <object> <adverb> (to <purpose>).`
- 例句: First, place the pre-chilled steel ruler on the long side of metal embedding cassette A (to prevent the tissue from being deformed)

### 最小用量规定
- 模板: `Prepare at least <amount> per <unit>.`
- 例句: Prepare at least 300 μL per chip

### 使用前准备
- 模板: `Remove <object> from storage at least <time duration> before use and <verb> to <state>.`
- 例句: Remove Glycerol from storage at least 5 minutes before use and equilibrate to room temperature.

### 储存与防护
- 模板: `<Temperature>, <precautionary condition>, <time duration>.`
- 例句: 4°C, protected from light, 1 day

### 溶解与混匀
- 模板: `Dissolve the <reagent> with <amount> of <diluent>, then <method>.`
- 例句: Dissolve the PR Enzyme (red cap, powder) with 1 mL of freshly prepared 0.01N HCl, then mix by pipetting

### 操作指令式
- 模板: `<verb> <object> (with <tool>/<method>)`
- 例句: Place the chip in a 9 cm petri dish (bottom lined with parafilm) to warm up for 1 min.

### 条件触发式
- 模板: `If <condition>, <action>.`
- 例句: If there are impurities on the chip, use 3000 μL of Nuclease Free Water to wash twice.

### 步骤衔接式
- 模板: `After <action>/<noun>, <new_action>.`
- 例句: After fixation, transfer the 6-well plate/6 cm culture dish to a fume hood.

### 建议/推荐式
- 模板: `It is recommended to <action> <time_limit>.`
- 例句: It is recommended to complete the tissue section mounting within 5 minutes.

### 用量/频率说明式
- 模板: `<action>, referring to <table_reference> for the <volume>/<quantity>.`
- 例句: Add tissue fluorescent staining solution to the chip; refer to Table 3-2 for the amount.

### 禁止/警示式
- 模板: `<action> should not be <adverb>, to avoid <negative_outcome>.`
- 例句: The pre-cooling time should not be too long to avoid condensation on the chip surface.

### 确保目标达成式
- 模板: `Ensure <state_of_object>.`
- 例句: Ensure there is no residual staining solution on the chip.

### 条件禁止式
- 模板: `<action> is prohibited.`
- 例句: Spaces and other special characters are prohibited.

### 过程伴随说明式
- 模板: `During <process>, <action>.`
- 例句: During the imaging process, it is necessary to ensure that both the track lines of the staining channels and the tissue area are clearly visible.

### 动作目的式
- 模板: `<action>, allowing <action_result>.`
- 例句: Place the chip in a 9 cm Petri dish with sealing film, and air-dry it in a fume hood for 4-6 min to allow the methanol to fully evaporate.

### 条件前置要求句式
- 模板: `The <object> must <verb> before <action> can be performed.`
- 例句: The obtained ssDNA staining images must pass QC before further image analysis (register) can be performed.

### 条件分支操作句式
- 模板: `If <condition> fails, <verb> with the <process>.`
- 例句: If QC fails, proceed with the experiment.

### 吸弃操作句式
- 模板: `Aspirate and discard the <substance> from <location>, repeat step <step> (volume as shown in <reference>).`
- 例句: Aspirate and discard the 0.1X SSC liquid, repeat step i (volume as shown in Table 3-5);

### 加液用量标注句式
- 模板: `Add <substance> (refer to <reference> for volume).`
- 例句: Add PR Rinse Buffer solution (containing 5% RI, refer to Table 3-8 for volume);

### 禁止/警告指令句式
- 模板: `Do not <action> during <process>.`
- 例句: Do not touch the surface where the microscope is placed during scanning

### 建议/风险提示句式
- 模板: `Use <method> with caution, as <reason>.`
- 例句: Use autofocus mode with caution, as most autofocus strategies cannot focus precisely on the track line

### 孵育操作句式
- 模板: `Incubate the <substance> in <environment> for <time> before use.`
- 例句: Incubate the permeabilization working solution in a 37°C incubator for 10 min before use;

### 状态确保句式
- 模板: `Ensure the <object> is <state>.`
- 例句: Ensure the chip is submerged in the liquid.

### 紧急操作句式
- 模板: `Immediately add <substance> to avoid <negative_result>.`
- 例句: Immediately add RT Mix to avoid RNA degradation.

### 放置操作句式
- 模板: `Place the <object> into <container>.`
- 例句: Place the 1 cm * 2 cm and 2 cm * 2 cm chips into a 6-well plate

### 用量与规格描述
- 模板: `<quantity> <unit>/<object>`
- 例句: 1500 μL/chip

### 条件动作描述
- 模板: `If <condition>, <action>.`
- 例句: If white precipitate is observed in the buffer, it can be dissolved by incubating at 55°C.

### 参考文档的操作指令
- 模板: `<Imperative Verb> the <Object> according to <Reference>.`
- 例句: Prepare the cDNA Release Mix according to Table 3-13.

### 禁止与预防指令
- 模板: `Prevent <object> from <action>.`
- 例句: Prevent the chip from drying out completely.

### 动作前置条件
- 模板: `Before <event/action>, <imperative action>.`
- 例句: Before each use, shake or pipette the magnetic beads up and down to ensure they are thoroughly mixed.

### 参数参考提示
- 模板: `<Action> (refer to <Reference> for <parameter>).`
- 例句: Add the cDNA Release Mix (refer to Table 3-13 for volume).

### 温育与处理指令
- 模板: `<Action>, and incubate at <Temperature>.`
- 例句: Prepare the cDNA Release Mix according to Table 3-13 and incubate at room temperature.

### 标准操作步骤
- 模板: `Add <volume> of <reagent> to <target> for <process>`
- 例句: Add 22 μL of Nuclease Free Water to each tube for resuspension

### 条件判定与补救
- 模板: `If <condition>, <action> with <reagent>`
- 例句: If the volume of the recovered sample above is less than 42 μL, bring the volume to 42 μL with Nuclease-Free Water.

### 按比例混合
- 模板: `Mix <object A> with <object B> at a <ratio> ratio, <action>, then <next_action>`
- 例句: Mix the recovered solution from the previous step with magnetic beads equilibrated to room temperature at a 1:1 ratio

### 操作禁止与警告
- 模板: `Avoid <verb>-ing <object>; do not <action>`
- 例句: Avoid touching the magnetic beads; do not pipette up and down or disturb the magnetic beads

### 依据指引
- 模板: `Prepare <object> according to <table/document>`
- 例句: Prepare the PCR Mix according to Table 3-15

### 流程暂停与保存
- 模板: `(This step can be paused; <instruction>)`
- 例句: (This step can be paused; store samples at -20°C)

### 状态监测
- 模板: `Wait for <condition> until <state>`
- 例句: Wait for all the magnetic beads to be adsorbed to the wall of the tube

### 用途描述
- 模板: `Used for <action> during <process>`
- 例句: Used for vacuum filtration during embedding

### 提示与注意
- 模板: `NOTE: Pay special attention; <condition> may <result>.`
- 例句: NOTE: Pay special attention; improper operation or negligence may cause the experiment to fail.

### 建议
- 模板: `It is recommended to <action> <object> at <condition>.`
- 例句: It is recommended to store OCT at 4°C.

### 建议项
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to use the final calibrated volume.

### 步骤指令
- 模板: `<Imperative Verb> <object> <location/context>.`
- 例句: Place the embedding cassette horizontally on ice in a vacuum desiccator.

### 指引引用
- 模板: `For <subject>, please refer to <reference>.`
- 例句: For applicable Stereo-seq solutions and their corresponding user manuals, please refer to the table below.

### 预防警告
- 模板: `Note that <risk condition>; please <action>.`
- 例句: Note that dry ice can cause frostbite; please handle with caution.

### 禁止项
- 模板: `Do not <verb> <object>, as this will <negative outcome>.`
- 例句: Do not overfill the embedding cassette with tissue, as this will make sectioning difficult.

### 结果差异
- 模板: `<Subject> may vary depending on <variable factors>.`
- 例句: Individual results may vary depending on the specific imaging system and/or sample characteristics.

### 步骤建议/说明
- 模板: `For <details>, please refer to the "<document_title>".`
- 例句: For details on the assembly, disassembly, and usage of the carrier chip, please refer to the "Stereo-seq Chip Carrier and Accessories User Manual".

### 操作指导（祈使句）
- 模板: `<verb> the <object> to <purpose>, ensuring <condition>.`
- 例句: Gently place the chip on the stage, ensuring it is correctly oriented so that the serial number (SN) is at the top, and the QR code is at the bottom.

### 功能说明/能力描述
- 模板: `<subject> can be used for <application>.`
- 例句: Any equivalent system with the listed functions can be used for imaging.

### 排查建议
- 模板: `In <context>, <subject> can be improved by <verb>-ing <method>.`
- 例句: In fluorescence imaging, stitching artifacts can be improved by using the microscope's background balance function.

### 一致性说明
- 模板: `The <process> is consistent with the <experimental_workflow>.`
- 例句: The tissue preparation workflow is consistent with the experimental workflows of various Stereo-seq solutions.

### 参考与评估
- 模板: `The above <requirements/recommendations> are relatively specialized; please consult <vendor> to <action>.`
- 例句: The above imaging system requirements and recommendations are relatively specialized. Please consult the microscope manufacturer to confirm and complete calibration and debugging.

### 负面后果
- 模板: `...which easily leads to <negative result>.`
- 例句: ...which easily leads to QC failure.

### 优先推荐
- 模板: `<Method> is preferred.`
- 例句: Large images are preferred as input.

### 替代方案
- 模板: `If <condition>, <alternative method> can be used.`
- 例句: If it fails, manual registration can be used.

### 阈值建议
- 模板: `<Metric> should preferably not exceed <threshold>.`
- 例句: The distance should preferably not exceed half the width of the field of view (FOV).

### 时长控制
- 模板: `To ensure <result>, it is recommended to control the duration within <time>.`
- 例句: To ensure optimal imaging effects, it is recommended to control the duration from mounting to imaging within 30 min.

### 条件结果句
- 模板: `When <condition>, <consequence>.`
- 例句: When the focus is good, cell nuclei and other morphological details can be identified relatively clearly.

### 功能描述句
- 模板: `<subject> <verb> <object>.`
- 例句: Proper exposure provides good brightness and contrast.

### 警告/限制句
- 模板: `<subject> should <verb> <object>.`
- 例句: Background-balanced templates should not contain Track lines; it is recommended to use fixed calibration templates.

### 操作建议句
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to use fixed calibration templates.

### 原因解释句
- 模板: `<subject> results in <noun_phrase>.`
- 例句: Overexposed images exhibit high brightness in some areas, saturated pixels, and low contrast, resulting in data loss and resolution impairment.

### 定义句
- 模板: `<subject> are <noun_phrase>.`
- 例句: Track lines are straight lines arranged on the chip and are generally parallel to the chip edges.

### 禁止/否定句
- 模板: `Do not <verb> <object>.`
- 例句: Do not grant or imply any right or license to use any copyrighted content or trademark.

### 操作指令句
- 模板: `Please <verb> <object>.`
- 例句: Please download the latest version of the manual and use it with the corresponding kit version.

### 用途声明句
- 模板: `This product is for <usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 被动语态描述
- 模板: `<subject> is <verb_past_participle>.`
- 例句: Camera pixel size is 3.45 μm, scale bar is 10 μm (red).

### 动作设定
- 模板: `With the <Object> <State/Position>, <Verb> the <Object> into the <Target>`
- 例句: With the fixture face down, insert the washer into the fixture,

### 建议说明
- 模板: `It is recommended to <Verb> the <Object>`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 目的确保
- 模板: `<Verb> <Area> to ensure <Result/State>`
- 例句: Press along both sides of the fixture cartridge to ensure the fixture and chip carrier are securely assembled together;

### 限制声明
- 模板: `This product is intended for <Scope> only and is not for <Prohibited Use>`
- 例句: This product is intended for research use only and is not for clinical diagnostic use.

### 预防建议
- 模板: `To prevent <Issue>, it is recommended to <Verb> <Object>`
- 例句: To prevent sample cross-contamination, it is recommended to use filtered pipette tips

### 修订记录
- 模板: `· Revised <Section/Item>`
- 例句: · Revised legal notice;

### 引用指南
- 模板: `For further information regarding <Subject>, refer to <Source>`
- 例句: For further information regarding the product catalog number and specific components of the carrier accessory kit, refer...

### 文档标识
- 模板: `Document Number: <id> Version: <v>`
- 例句: Document Number: STOG01024 Version: A

### 产品/试剂清单
- 模板: `<product> * <quantity> (<spec>)`
- 例句: Stereo-seq Transcriptome Kit T for Go Spatial * 1 (8 RXN)

### 指引/参考
- 模板: `For further information regarding <item>, please refer to <reference>.`
- 例句: For further information regarding product catalog numbers, reagent components, etc., please refer to Tables 1-1 to 1-3.

### 操作指令(礼貌型)
- 模板: `Upon <event>, please refer to <document> to <action>.`
- 例句: Upon receiving the Stereo-seq chip, please refer to the "Stereo-seq Chip Transfer and Storage Guidelines for Go Spatial" to correctly store the product.

### 储存条件
- 模板: `Storage Temperature: <range>`
- 例句: Storage temperature: -25°C ~ -18°C

### 构成说明
- 模板: `Each <item> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 声明/责任边界
- 模板: `This document serves solely as <type>, intended to <purpose>.`
- 例句: This document serves solely as general guidance reference material, intended to provide operational guidelines and methods.

### 前置条件/前提
- 模板: `When <conditions> are all appropriate, <result>.`
- 例句: When transportation conditions, storage conditions, and methods of use are all appropriate, all components can maintain full activity within their validity period.

### 物品描述
- 模板: `<volume> <item>`
- 例句: 50 μL clear pipette tip

### 包装规格描述
- 模板: `<quantity> per <container>`
- 例句: 1000 per box

### 平衡操作
- 模板: `Remove <item> from <source> and equilibrate at <condition> for <time>.`
- 例句: Remove magnetic beads from 4°C and equilibrate at room temperature for 30 min.

### 放置操作
- 模板: `Place <item> onto <instrument>`
- 例句: Place the PCR adapter onto the PCR machine

### 义务描述
- 模板: `(must be <action>)`
- 例句: (must be ordered separately)

### 浓度调节
- 模板: `Dilute <item> to <concentration>`
- 例句: Dilute absolute ethanol to 80%

### 试剂操作与预冷
- 模板: `Add <reagent> (dosage: <amount>) and <pre-cool/action> at <temperature> for <time>.`
- 例句: Add methanol to a 24-well plate (dosage: 1 mL/chip/well) and pre-cool at -20°C.

### 条件句（可选操作/注意事项）
- 模板: `If <condition>, <action>; alternatively, <alternative_action>.`
- 例句: If impurities are observed on the chip surface, you may use an air canister to gently blow dry; alternatively, the chip can be placed in a culture dish.

### 排除/忽略条件
- 模板: `If using <status/type>, skip this step; simply <action>.`
- 例句: If using newly opened reagents, skip this step; simply place the PR Enzyme dry powder in the correct position.

### 液体配置建议
- 模板: `Unless otherwise specified, <reagent> is used for <action> in this experiment.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for diluting reagents in this experiment.

### 步骤时间衔接
- 模板: `After <action> is complete, <next_action>.`
- 例句: After the 10-minute tissue fixation is complete, move the 24-well plate to a fume hood.

### 禁止/警告表达
- 模板: `The <parameter> must not be <too_adj/too_adj_neg> to avoid <consequence>.`
- 例句: The pre-cooling time must not be too long to avoid water condensation on the chip surface.

### 物理操作指令
- 模板: `Use <tool> to <action> the <object> from/to <location>.`
- 例句: Use tweezers to remove the chip from the 24-well plate.

### 状态确认提示
- 模板: `After confirming that <status>, <action>.`
- 例句: After confirming that there is no residual methanol, transfer the chip to a clean culture dish.

### 过程目的说明
- 模板: `<action> to <purpose>.`
- 例句: Use your fingertip to warm the back of the chip to ensure the section adheres better to the chip.

### 条件要求式
- 模板: `Please ensure <condition> before <action>.`
- 例句: Please ensure that the coverslip is clean and free of dust before use.

### 用量/频率限定式
- 模板: `<action>, with a volume/frequency of <quantity>.`
- 例句: Add Wash Buffer dropwise to the chip, with a volume of at least 100 μL per chip;

### 状态确认/说明式
- 模板: `<subject> is/are shown in <reference>.`
- 例句: The interface is shown in Figure 2-4:

### 建议/辅助操作式
- 模板: `<action> helps <goal>.`
- 例句: Helps the chip adhere better to the glass slide;

### 顺序执行式
- 模板: `<action1>, then <action2>.`
- 例句: Add a drop of water (~1 μL) onto a clean microscope slide, then carefully use tweezers to transfer the chip onto the slide.

### 必要性说明式
- 模板: `It is necessary to ensure <condition>.`
- 例句: During the imaging process, it is necessary to ensure that the staining channel's Track lines and the tissue area are both clear.

### 步骤描述式
- 模板: `<Action in verb>: <Description of action>.`
- 例句: Reagent Placement: Open the lids of all prepared reagents and place them in the order shown in the diagrams.

### 条件指令式
- 模板: `Unless otherwise specified, <do not/avoid> <action>, as this may lead to <negative outcome>.`
- 例句: Unless otherwise specified, it is not recommended to aliquot the reagents in the kit, as this may lead to insufficient reagents.

### 强制步骤执行式
- 模板: `Please <action> according to <reference>.`
- 例句: Please prepare according to volume configuration, and dispense it into a 5 mL empty tube provided with the reagent kit.

### 条件衔接式
- 模板: `<Action A>, <then/and> <Action B>.`
- 例句: After thawing in a 55°C incubator, invert to mix at least 3 times, and leave at room temperature.

### 操作路径式
- 模板: `Click "<Button Name>" <location description> to <result>.`
- 例句: Click "Process Run" at the bottom left of the page to enter the experiment information entry interface.

### 顺序执行指令式
- 模板: `Please <action> in order of <criterion>.`
- 例句: Please place the chips into wells 1-8 in order of increasing permeabilization time.

### 负面预防/禁止式
- 模板: `Please store <object> at <condition>; do not <action>.`
- 例句: Please store unused NRT Oligo solution at -80°C; do not subject to repeated freeze-thaw cycles.

### 图表引用式
- 模板: `<Noun phrase> (see Figures <Number> and <Number>).`
- 例句: Well positions A-M (see Figures 2-6 and 2-7) have 3 columns per row.

### 确认性指令式
- 模板: `After verifying that <object/condition> is <state>, <next action>.`
- 例句: After verifying that all materials and consumables are placed correctly, close the chamber door.

### 条件限制式
- 模板: `<Object> should only be <action> after <condition>.`
- 例句: Low-temperature reagents (labeled A-J) should only be transferred after the low-temperature reagent zone reaches 4°C.

### 物料操作禁止
- 模板: `Do not <action> the <component> at this time.`
- 例句: Do not click the "Confirm" button on the "Stop all temperature controls?" pop-up at this time.

### 操作建议与频次
- 模板: `It is recommended to <action> <frequency/condition>.`
- 例句: It is recommended to repeat step b, the UV disinfection operation.

### 设备状态指示
- 模板: `As shown in <figure_id>, <subject> will <state_change/action>.`
- 例句: As shown in Figure 2-18, the instrument will beep, and a software pop-up will indicate "Ready for loading."

### 混合与准备动作
- 模板: `Remove <object> from <temperature>, <action1> to mix, and equilibrate to <temperature>.`
- 例句: Remove from 4°C 30 minutes in advance, vortex to mix, and equilibrate to room temperature to help ensure recovery efficiency.

### 精确步骤描述
- 模板: `When <action_verb>ing, ensure <constraint>.`
- 例句: When separating magnetic beads from the liquid, ensure the pipette tip does not touch the beads.

### 使用量计算规则
- 模板: `Please calculate the required volume based on <factor>, using the formula <formula>.`
- 例句: Please calculate the required volume based on the number of chips to be run (n), using the formula 1200 μL + 400 μL × n.

### 错误修正建议
- 模板: `If <error_condition> is accidentally aspirated, <corrective_action>.`
- 例句: If magnetic beads are accidentally aspirated, dispense the beads and liquid back into the tube, perform separation again before aspirating the supernatant.

### 视觉确认指令
- 模板: `Until <observation_condition>, <next_action>.`
- 例句: Until the surface of the magnetic beads no longer reflects light, the product can be eluted using TE Buffer.

### 孵育指令
- 模板: `Incubate for <duration>.`
- 例句: Incubate for 10 min;

### 状态等待
- 模板: `Wait until <condition>.`
- 例句: Wait until all the magnetic beads have adhered to the side of the tube;

### 建议指令
- 模板: `It is recommended to <action>.`
- 例句: For potential troubleshooting, it is recommended to retain 2 μL of the PCR product.

### 禁止指令
- 模板: `Do not <action>.`
- 例句: do not pipette up and down or disturb the magnetic beads;

### 液体转移
- 模板: `Transfer the <source> to a <destination>.`
- 例句: Transfer the supernatant (~21 μL cDNA) to a new 0.2 mL PCR tube;

### 参考文档指引
- 模板: `Please refer to <document_name> to <action>.`
- 例句: Please refer to the "Stereo-seq Chip Handling and Storage Guide for Go Spatial" to store the product.

### 试剂盒组成描述
- 模板: `<kit_name> consists of the following <number> parts:`
- 例句: Each reagent kit consists of the following two parts:

### 单独购买提示
- 模板: `<item_name> (sold separately)`
- 例句: Go Spatial compatible consumables (sold separately)

### 保存条件建议
- 模板: `Please store the <product> under <conditions> as soon as possible.`
- 例句: Please store the product under the specified conditions as soon as possible.

### 实验物料概述
- 模板: `This list details the <equipment_or_materials> required for this experiment.`
- 例句: This list details the equipment and materials required for this experiment.

### 特定要求查询
- 模板: `Regarding <feature> requirements, please refer to <document_name>.`
- 例句: Regarding microscope requirements, please refer to the "STOmics Microscope Evaluation Reference Manual".

### 参数标签说明
- 模板: `<parameter>: see label`
- 例句: Cold chain transport validity period: see label

### 条件操作建议
- 模板: `If <condition>, it is recommended to <action>.`
- 例句: If during transit duration is long, it is recommended to use temperature-controlled containers for transport.

### 规格包装单位
- 模板: `<amount> <unit>/<container>`
- 例句: 96 units/rack

### 安全警告
- 模板: `Direct contact of <subject> with <object> should be avoided; do not <verb> <subject>.`
- 例句: Direct contact of samples and reagents with skin and eyes should be avoided; do not swallow samples or reagents.

### 条件式操作
- 模板: `If <condition> is observed, <action>.`
- 例句: If impurities are observed on the chip surface, after the chip has warmed up, an air duster can be used.

### 流程参照
- 模板: `Please follow <reference> to <action>.`
- 例句: Please follow Chapter 2.1 [Preparation Before Experiment] to set the PCR machine or slide dryer to a baking temperature.

### 目的导向建议
- 模板: `To <purpose>, the use of <object> is recommended.`
- 例句: To avoid sample cross-contamination, the use of filter tips is recommended.

### 操作指令（稀释）
- 模板: `Dilute <amount> of <substance> to <target_volume> <context>.`
- 例句: Dilute 250 μL of 20X SSC to 50 mL, before loading onto the instrument.

### 设置指令
- 模板: `Set <instrument> to <value> <purpose>.`
- 例句: Set to 55°C for reagent incubation.

### 指令操作句式
- 模板: `<imperative_verb> <object> <prepositional_phrase>`
- 例句: Remove the chip container from the vacuum-sealed aluminum foil bag

### 条件执行句式
- 模板: `If <condition>, <imperative_action>.`
- 例句: If performing subsequent Go Spatial experiments on the day of sectioning, you may follow the procedures in [A. On-instrument loading]

### 参考规范句式
- 模板: `Please <imperative_verb> <object> according to <reference_location>.`
- 例句: Please perform the Go Spatial workflow preparation operations according to Chapter 2.5.

### 时长与温度执行句式
- 模板: `<imperative_action> at <temperature> for <duration>.`
- 例句: Quickly place it at 37°C to bake the slice for 3 minutes.

### 负面约束句式
- 模板: `Be careful not to <verb> <object>.`
- 例句: Be careful not to touch the front of the chip.

### 顺序检查句式
- 模板: `After <verb>ing <condition>, <imperative_action>.`
- 例句: After confirming there is no residual methanol, transfer the chip to a clean and dry 24-well plate.

### 状态配置句式
- 模板: `Ensure <object> is <state_or_position>.`
- 例句: Ensure that the front side is facing up.

### 准备工作说明句式
- 模板: `Before <event_or_use>, please <imperative_action>.`
- 例句: Before use, please ensure that STOmics software version V1.4.0 or higher is installed.

### 建议/提醒句式
- 模板: `The <variable> should not be <condition>, to avoid <negative_outcome>.`
- 例句: The pre-cooling time should not be too long, to avoid condensation on the chip surface.

### 操作指令：通用祈使句
- 模板: `<verb> <object> (as shown in <figure_reference>);`
- 例句: Place the chip into a Petri dish with sealing film on the bottom, leave the lid off and place it in a fume hood for 2-3 min

### 条件限制：除非另有说明
- 模板: `Unless otherwise specified, <action_recommendation>, as <reason>.`
- 例句: Unless otherwise specified, it is not recommended to aliquot reagents from the kit for separate use, as this may lead to insufficient reagent redundancy

### 顺序与步骤衔接
- 模板: `After <action_is_complete>, <next_action>;`
- 例句: After methanol fixation is complete, transfer the 24-well plate to a fume hood;

### 建议与合规表达
- 模板: `It is recommended to <action> to <purpose>.`
- 例句: For initial experiments with each tissue block, it is recommended to set 6 min, 12 min, 18 min, and 24 min groups to test.

### 必备条件与禁止禁止
- 模板: `Please <action>, otherwise <consequence>.`
- 例句: Please enter all information on the chip information entry page, otherwise the software will not be able to proceed to the next step.

### 物料位置提示
- 模板: `<location> is for <reagent_name>; <action_instruction>.`
- 例句: The position numbered 2 on the middle left of the room temperature reagent area is for 0.1X SSC; prepare 50 mL accord, and transfer to a 50 mL reagent reservoir before the run.

### 负面警示（注意）
- 模板: `Note: Do not <action> at this time. If <condition>, <consequence>; please <remediation>.`
- 例句: Note: Do not click the "Confirm" button on the "Stop all temperature control?" pop-up window at this time. If you have already clicked it, the low-temperature reagent area will gradually return to room temperature; please retrieve the remaining reagents as soon as possible.

### 对比与前提条件
- 模板: `<procedure> does not require <item>; although <condition>, <instruction>.`
- 例句: The permeabilization procedure does not require the use of a 1.3 mL deep-well plate; although no deep-well plate needs to be placed before the run, the temperature control cover still needs to be placed over the deep-well plate area.

### 后续动作衔接
- 模板: `After <event>, <verb> <object>.`
- 例句: After confirming that the reagents have been recovered, click "OK" to finish the run.

### 禁止事项/提示
- 模板: `Please <verb> <object> <adverb/preposition>.`
- 例句: Please leave the A and G wells empty.

### 被动描述状态
- 模板: `<Subject> is <past_participle> <adjective/preposition>.`
- 例句: Stereo-seq chip carriers are vacuum-sealed in aluminum bags.

### 建议/提示用量
- 模板: `<Verb> <object> (referring to <reference_amount>).`
- 例句: The aliquot volume can be reasonably arranged according to usage habits (refer to the usage amount in step b).

### 并列步骤
- 模板: `<Verb> <object1>, <verb> <object2>, and <verb> <object3>.`
- 例句: Remove all reagents, clear pipette tips and waste from the waste area, and wipe away condensation.

### 数值计算说明
- 模板: `Calculate the required volume as <formula>.`
- 例句: For the number of chips (n), calculate the required volume as 1200 μL + 400 μL × n.

### 操作步骤
- 模板: `<verb> <object> <location/context>`
- 例句: Click on the type of guide you wish to view in the selection panel on the right side of the page.

### 要求或约束
- 模板: `<subject> should not exceed <value>`
- 例句: The tissue size should not exceed 0.45 cm × 0.45 cm × 2 cm.

### 免责/用途声明
- 模板: `This product is for <usage> only and not for <prohibited_usage>`
- 例句: This product is for research use only and not for diagnostic purposes.

### 信息检索引导
- 模板: `Please visit <url> to <action>`
- 例句: Please visit to view or download: www.stomics.tech/resources/Documents

### 条件语句
- 模板: `If you are using <product>, it is recommended to <action>`
- 例句: If you are using Stereo-seq FF (including mIF-compatible) ≥ V1.3, it is recommended to proceed with tissue samples having a RIN ≥ 4.

### 警示/注意事项
- 模板: `Note: <instruction>; <potential_consequence>`
- 例句: Note: Pay special attention; improper handling or negligence may cause the experiment to fail.

### 前置条件/背景设定
- 模板: `Based on <condition>, <verb> <object> in advance.`
- 例句: Based on the tissue size, prepare two appropriately sized metal embedding cassettes A and B in advance.

### 目的/功能说明
- 模板: `<action>, (to <purpose>)`
- 例句: First, place a pre-cooled steel ruler on the long edge of metal embedding cassette A (to prevent the tissue from being deformed)

### 条件判断与后续动作
- 模板: `If <condition>, <action>.`
- 例句: If the tissue block is completely solidified and has turned white and opaque, gently bend the sides of the metal embedding cassette A

### 步骤衔接/流程描述
- 模板: `<sequence_marker> <action>.`
- 例句: After freezing for 5 min, remove the metal embedding cassette B and the steel ruler

### 物料准备/清单项
- 模板: `<item_name> - <quantity>`
- 例句: Blunt-tip forceps - 1

### 免责与合规声明
- 模板: `This product is for <usage_purpose> only, not for <prohibited_usage>.`
- 例句: This product is for research use only, not for diagnostic use.

### 建议与提示
- 模板: `Note: <instruction>.`
- 例句: Note: Please download the latest version of the instruction manual and use it with the corresponding version of the kit.

### 范围与包含项
- 模板: `<subject>, including but not limited to <list_of_items>.`
- 例句: including but not limited to trademark rights, copyrights, etc.

### 操作提示
- 模板: `Tip: Additional operational tips and guidance.`
- 例句: Tip: Additional operational tips and guidance.

### 关键步骤警告
- 模板: `Key Step: Pay special attention to these steps to avoid <risk>.`
- 例句: Key Step: Pay special attention to these steps to avoid experimental failure or undesirable results.

### 一般注意事项
- 模板: `Note: Pay special attention; <potential_issue> may lead to <consequence>.`
- 例句: Note: Pay special attention; improper operation or negligence may lead to experimental failure.

### 实验暂停点
- 模板: `Stopping point: You may <action> here and <action> the samples.`
- 例句: Stopping point: You may pause the experiment here and store the samples.

### 适用范围说明
- 模板: `This manual is applicable to <product_name>.`
- 例句: This manual is applicable to the Stereo-seq Permeabilization Reagent Kit V1.1 (Carrier version).

### 包含组件说明
- 模板: `Each reagent kit consists of the following <number> components:`
- 例句: Each reagent kit consists of the following three components:

### 引用其他文档
- 模板: `For further information on <topic>, please refer to <reference>.`
- 例句: For further information on product catalog numbers, reagent components, etc., please refer to Tables 1-1 through 1-4.

### 储存条件要求
- 模板: `Storage temperature: <temperature_range>`
- 例句: Storage temperature: 2°C ~ 8°C

### 运输条件建议
- 模板: `Transportation temperature: <temperature_range>`
- 例句: Transportation temperature: 0°C~30°C

### 操作前准备/保存
- 模板: `After receiving the <product>, please refer to the "<document_name>" to store the product correctly.`
- 例句: After receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Guidelines" to store the product correctly.

### 设备选择建议
- 模板: `You may choose any one from the listed brands (marked with *) to be used with <equipment>.`
- 例句: You may choose any one from the listed brands (marked with *) to be used with the PCR adapter.

### 例外情况说明
- 模板: `This reagent is used for <application>. If you are not performing the <protocol>, you do not need to use this reagent.`
- 例句: This reagent is used for H&E staining mounting. If you are not performing the Stereo-seq compatible H&E staining protocol, you do not need to use this reagent.

### 必须/禁止动作
- 模板: `<verb> <object> must <verb> <object> / Do not <verb> <object>.`
- 例句: A desiccant must be placed in the sealed aluminum bag to maintain dry conditions.

### 准备/平衡条件
- 模板: `Remove <object> <time> in advance to equilibrate to <condition>.`
- 例句: Remove 5 min in advance to equilibrate to room temperature.

### 用量/浓度描述
- 模板: `Add <amount> of <reagent> to <amount> of <reagent>; the required volume is at least <amount>/<unit>.`
- 例句: Add 10 μL of RI to 190 μL of 0.1X SSC; the required volume is at least 200 μL/sample.

### 仪器预处理/设置
- 模板: `Pre-cool <instrument/part> to <temperature>.`
- 例句: Cryostat chamber pre-cooled to −20°C, specimen holder pre-cooled to −15°C ~ −10°C.

### 因果关系
- 模板: `If <subject> is <condition>, <subject> will <consequence>.`
- 例句: If the specimen head temperature is too low, the sections will crack.

### 合规与处理
- 模板: `All <object> must be disposed of in accordance with <standard>.`
- 例句: All samples and various types of waste must be disposed of in accordance with relevant regulations.

### 注意事项/警告
- 模板: `Note: Do not <verb> <object>.`
- 例句: Note: Do not touch the front of the chip.

### 确保满足条件
- 模板: `Ensure (that) <clause>, <optional:verb phrase>;`
- 例句: Ensure that the glycerol has been pre-equilibrated at room temperature for 5 minutes.

### 建议/推荐做法
- 模板: `It is recommended to <verb> <object> <condition>;`
- 例句: It is recommended to complete the tissue section mounting within 5 min;

### 步骤衔接/重复
- 模板: `Repeat the above steps until <condition>;`
- 例句: Repeat the above steps until all sections are mounted;

### 预防性说明
- 模板: `The <noun> must not be too <adjective> to <verb> <object>, nor too <adjective> to <verb> <object>.`
- 例句: The pre-cooling time must not be too long to prevent condensation on the slide surface, nor too short to ensure the slide can reach the pre-cooling temperature.

### 仪器/环境操作
- 模板: `Set the <noun> of <equipment> to <value>, and <optional:further instruction>;`
- 例句: Set the temperature of a metal bath or other equipment with equivalent functionality to 37°C, and the PCR instrument program remains the same.

### 可选步骤标注
- 模板: `(Optional) <clause>.`
- 例句: (Optional) This step is applicable to product protocols compatible with Stereo-seq H&E staining.

### 时间/容量限制
- 模板: `<verb> <object> <condition> (e.g., within X min, at least X min);`
- 例句: Incubate the 1X permeabilization reagent working solution in a metal bath or other equivalent instrument at 37°C for 10 min (the maximum time should not exceed 30 min);

### 物料使用指南
- 模板: `Refer to <Document Name/Section> to <verb> <object>.`
- 例句: Refer to Appendix B, "Stereo-seq Chip Carrier and Accessory User Manual" to assemble the gasket and fixture into a carrier;

### Sequential Action
- 模板: `After <time_span>, <verb> the <object>, <verb> the <object>, and <verb> the <object>.`
- 例句: After 6 min, open the PCR instrument lid, remove the sealing film, and add 150 μL of 1X permeabilization reagent work

### Imperative Action Sequence
- 模板: `<Verb> the <object>, <verb> the <object>, and <verb> at <parameter>.`
- 例句: Place the sealing film back onto the carrier, close the PCR instrument lid, and incubate at 37℃;

### Loop Instruction
- 模板: `Repeat steps <step_range> until <condition>.`
- 例句: Repeat steps 2) - 5) until the chip with the shortest permeabilization time begins incubation.

### Reagent Addition
- 模板: `Add <reagent_name>, at a volume of <volume>/<unit>.`
- 例句: Add Wash Buffer, at a volume of 200 μL/chip;

### Constraint Rule
- 模板: `<Subject> shall only use <allowed_items>; <prohibited_items> are prohibited.`
- 例句: Folder names shall only use letters, numbers, and underscores; special characters such as spaces are prohibited.

### Mandatory Requirement
- 模板: `<Subject> must be <verb>ed under the same <condition>, including <detail> and <detail>.`
- 例句: Chips of the same tissue with different permeabilization times must be scanned under the same imaging conditions, including brightness and exposure.

### 多步骤操作指令
- 模板: `<verb> <object>, <verb> <object>, and <verb> <object>...`
- 例句: Transfer the container to a fume hood, remove the carrier from the container, and blot dry the back and surrounding excess methanol

### 状态约束条件
- 模板: `..., ensuring <condition_phrase>;`
- 例句: ..., ensuring no liquid residue;

### 建议性操作
- 模板: `It is recommended to <verb> <goal_or_task>.`
- 例句: It is recommended to maintain a consistent staining time for the same tissue.

### 精确剂量加液指令
- 模板: `Add <substance> dropwise onto <target>, with a volume of <amount>/<unit>.`
- 例句: Add Hematoxylin staining solution dropwise onto the chip surface, with a volume of 100 μL/chip.

### 循环执行步骤
- 模板: `Repeat step <step_identifier> an additional <number> times;`
- 例句: Repeat step d. an additional 2 times;

### 预操作环境平衡
- 模板: `Equilibrate <reagent_name> at <temperature> for <time_duration> in advance.`
- 例句: Equilibrate the H&E Mounting Medium at room temperature for 5 minutes in advance.

### 条件警告/预防措施
- 模板: `Please ensure that <condition_to_prevent> remains in <location>; otherwise, <consequence> may occur.`
- 例句: Please ensure that no residual liquid remains in the gap between the chip and the slide; otherwise, applying the H&E Mounting Medium might cause eosin bleeding.

### 操作结果确认
- 模板: `Ensure that <target_object> is <state> in <medium>.`
- 例句: Ensure that the chip is completely submerged in the solution.

### 针对特定条件的执行建议
- 模板: `For <condition_description>, <imperative_verb> immediately to <avoid_consequence>.`
- 例句: For tissues prone to RNA degradation, such as pancreas, immediately perform subsequent operations to avoid RNA degradation.

### 否定限制/禁止
- 模板: `No one shall be permitted to <verb>, <verb>, or <verb> ...`
- 例句: no one shall be permitted to use, modify, reproduce, publicly disseminate, alter, distribute, or publish this manual’s

### 声明/解释句式
- 模板: `Nothing herein is intended to be or shall be construed as <noun_phrase>.`
- 例句: Nothing herein is intended to be or shall be construed as any warranty regarding the performance of any product listed or described herein,

### 操作指令（建议/提示）
- 模板: `Please <verb> the <object> and use it with the <object>.`
- 例句: Please download the latest version of the instruction manual and use it with the corresponding version of the kit.

### 操作指令（常规）
- 模板: `Please <verb> the <object> under the specified conditions as soon as possible.`
- 例句: Please store the product under the specified conditions as soon as possible.

### 注意事项/特别标注
- 模板: `<Signal_Word>: <Action_or_Description>.`
- 例句: Key steps: Pay special attention to these steps to avoid experimental failure or unfavorable results.

### 适用性声明
- 模板: `This <noun> is applicable to the <product_name>.`
- 例句: This operation manual is applicable to the Stereo-seq Transcriptomics Kit V1.3 (Slide Version).

### 产品组成描述
- 模板: `Each <noun> consists of the following <number> components:`
- 例句: Each reagent kit consists of the following three components:

### 权利声明
- 模板: `<Company_Name> does not grant or imply <rights_type>.`
- 例句: Shenzhen BGI Three Arrows Fired Technology Co., Ltd. does not grant or imply the use of any copyrighted content belonging to us or any third party

### 免责声明
- 模板: `<Company_Name> makes no warranties, and hereby disclaims any liability regarding <matter>.`
- 例句: Shenzhen Huada Sanjian Qifa Technology Limited Liability Company makes no warranties, and hereby disclaims any liability regarding any matter described in this document.

### 详细信息查询
- 模板: `For details, please refer to <document_name>.`
- 例句: For details, please refer to Spatiotemporal Transcriptomics FF V1.3 Transcriptome Experimental Operation Manual.

### 操作指引
- 模板: `Upon <event>, please refer to the "<document_title>" for <purpose>.`
- 例句: Upon receiving the Stereo-seq chip carrier, please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" for proper storage.

### 条件限制（特定产品）
- 模板: `This reagent is used for <purpose>; it is not required if the <product_name> is not performed.`
- 例句: This reagent is used for mounting after H&E staining; it is not required if the Stereo-seq compatible H&E staining protocol is not performed.

### 温度数值描述
- 模板: `<Parameter> temperature: <min>°C to <max>°C`
- 例句: Shipping temperature: −25°C to −15°C

### 多选一建议
- 模板: `Select <choice_quantity> from the brands with the same superscript <index_type>.`
- 例句: Select one from the brands with the same superscript index number.

### 优先推荐与备选说明
- 模板: `For <item>, preferably use <brand1>, with <brand2> as a <alternative_type>.`
- 例句: For hematoxylin, preferably use Brand 1, with Brand 2 as a domestic alternative.

### 包含关系描述
- 模板: `The <container> contains <quantity> <items>, and each of the <quantity> <items> has <sub_item> attached to it.`
- 例句: The chip box contains 4 carriers, and each of the 4 chip carriers has one Stereo-seq chip T (1cm*1cm) attached to it.

### 选项可选说明
- 模板: `<Item_name> (optional)`
- 例句: Labnet Slide Spinner (optional)

### 等同功能提示
- 模板: `<Equipment_name> (<purpose>, or equivalent instrument)`
- 例句: Qubit™ 3.0 Fluorometer Q33216 (or equivalent instrument)

### 操作建议与推荐
- 模板: `It is recommended to <verb> <object>.`
- 例句: It is recommended to use aerosol-resistant pipette tips.

### 条件与约束
- 模板: `Unless otherwise specified, <item> is used for <purpose>.`
- 例句: Unless otherwise specified, Nuclease-Free Water is used for all liquids in this experiment to dilute reagents.

### 温度与预冷
- 模板: `Pre-cool the <device_part> to <temperature>.`
- 例句: Pre-cool the cryostat chamber to −20℃ and the specimen head to −15℃ ~ −10℃.

### 禁止与警告
- 模板: `Do not <action> the <object>; <alternative_action>.`
- 例句: Do not vortex the permeabilization enzyme; mix by pipetting.

### 用量与耗材
- 模板: `Take <quantity> of <reagent> and add to <quantity> of <diluent>; use at least <quantity> per <unit>.`
- 例句: Take 15 μL of RI and add to 285 μL of 0.1X SSC; use at least 300 μL per sample.

### 合规与安全
- 模板: `All <items> must be disposed of in accordance with <regulation>.`
- 例句: All samples and various wastes must be disposed of in accordance with relevant regulations.

### 即时操作要求
- 模板: `<reagent> must be prepared fresh before use.`
- 例句: 0.01N HCl must be prepared fresh before use.

### 预处理动作
- 模板: `Take out <item> <time_interval> in advance to equilibrate to <condition>.`
- 例句: Take out Glycerol 5 min in advance to equilibrate to room temperature.

### 否定操作指令
- 模板: `Do not <verb> <object>.`
- 例句: Do not touch the front side of the chip.

### 剂量/频率描述
- 模板: `<verb> <adverb> with <volume> of <substance> (<frequency>).`
- 例句: Wash twice with 100 μL of Nuclease-Free Water.

### 验证与检查
- 模板: `Verify that <clause>.`
- 例句: Verify that all Stereo-seq chip carriers in the slide box are properly positioned in the slots.

### 可选步骤声明
- 模板: `(Optional) <clause>.`
- 例句: (Optional) This step applies to product protocols compatible with Stereo-seq and H&E staining.

### 时间/温度控制
- 模板: `Incubate at <temperature> for <duration>.`
- 例句: Incubate at 37°C for 5 min.

### 禁止事项声明
- 模板: `<subject> are prohibited.`
- 例句: Spaces and other special characters are prohibited.

### 引用/参考建议
- 模板: `For <topic>, please refer to <reference>.`
- 例句: For a demonstration video on mounting tissue sections onto the Stereo-seq chip, please refer to the following link or scan the QR code.

### 状态确保指令
- 模板: `Ensure that <clause>.`
- 例句: Ensure that the methanol submerge all chips on the carrier.

### 条件动作
- 模板: `If <condition>, <action>.`
- 例句: If the microscope does not have a scanning map function, skip this step directly.

### 禁止警告
- 模板: `Avoid <action/state>.`
- 例句: Avoid letting the chip dry out completely.

### 操作序列衔接
- 模板: `<verb> to mix, and <verb> <amount> to <destination>;`
- 例句: After preparation, vortex to mix, and transfer 199 µL to a new assay tube;

### 设备使用/参数设定
- 模板: `<parameter_value> <parameter_unit>, <time_value> <time_unit>`
- 例句: 95°C, 5 min

### 禁止/警告事项
- 模板: `Avoid <action> as it may <consequence>.`
- 例句: When aspirating the supernatant after elution, avoid touching the magnetic beads, as aspirating the beads may affect subsequent reactions.

### 混合与离心
- 模板: `<verb> to mix, <verb> briefly, and <verb> <location>;`
- 例句: Prepare the PCR Mix according to Table 3-5, mix by pipetting, centrifuge briefly, and store on ice;

### 暂停/保存点说明
- 模板: `Pause point: <subject> can be <process> or <storage_condition> for up to <time_limit>.`
- 例句: Pause point: This step can be PCR overnight, or the product of this step can be stored at 4°C for up to 16 hours.

### 预防性操作
- 模板: `When <action>, take care not to <negative_action>, and <recommended_action>.`
- 例句: When separating the magnetic beads from the liquid, take care not to let the pipette tip touch the magnetic beads, and avoid aspirating the magnetic beads.

### 时间条件
- 模板: `About <time> before <event> ends, <action>`
- 例句: About 3 minutes before the permeabilization enzyme incubation ends, use tweezers to gently push the coverslip.

### 禁止限制
- 模板: `Use only <format>; <prohibition> are prohibited.`
- 例句: Use only letters, numbers, and underscores for folder names; spaces and other special characters are prohibited.

### 建议事项
- 模板: `It is recommended to <action> <time/condition>.`
- 例句: It is recommended to seal the slide immediately after adding the H&E Mounting Medium.

### 强制确认
- 模板: `Please ensure <condition>; otherwise, <consequence>.`
- 例句: Please ensure there is no residual liquid in the gap between the chip and the slide; otherwise, it may cause the eosin to bleed.

### 预处理
- 模板: `According to <reference>, <action> in advance.`
- 例句: According to [Pre-experimental Preparation], prepare 2 mL of 0.01N HCl in advance.

### 禁止/规避操作
- 模板: `<verb> the <object>, avoiding <action/noun> between <object1> and <object2>;`
- 例句: Align the chip with the gasket hole, avoiding contact between the fixture and gasket with the chip surface;

### 选择性推荐
- 模板: `Choose one of the two, used for <purpose>;`
- 例句: Choose one of the two, used for RNA extraction from frozen tissue sections;

### 不建议操作
- 模板: `It is not recommended to <verb> <noun/attribute>.`
- 例句: It is not recommended to change the brand item number.

### 耗材规格描述
- 模板: `<size> <adjective1>, <adjective2>, <adjective3> <noun> with <feature>`
- 例句: 20 μL boxed, sterile, short pipette tips with filter

### Alternative Option
- 模板: `Choose one of two, or other <product_type> of the same type.`
- 例句: Choose one of two, or another brand of the same type of PCR product.

### Equipment Specification
- 模板: `<Equipment> device, <Brand> <Model>, or other <equipment_type> of the same type.`
- 例句: Low-temperature centrifuge equipment, Centrifuge  EppendorfR, or other equipment of the same type

### Pre-requisite Action
- 模板: `<Action> at least <number> days in advance.`
- 例句: Serum filtration at least  days in advance

### Usage and Constraint
- 模板: `Used for <purpose>; <requirement>.`
- 例句: Used for tissue fixation; requires low impurities, other brands of chromatography-grade methanol are [alternative]

### Consumable Specification
- 模板: `<Size> boxed sterile <type> pipette tips with filters`
- 例句: 20 μL boxed sterile short pipette tips with filters

### Table Header
- 模板: `Preparation Item, Category, Name, Recommended Brand, Catalog Number, Remarks, Checklist Item`
- 例句: Preparation Items Category Name Recommended Brand Catalog Number Remarks Checklist Item

### Section Heading
- 模板: `Other reagents and consumables without recommended brands — <task>`
- 例句: Other reagents and consumables without recommended brands — Permeabilization time test

### 选择性推荐句式
- 模板: `Choose one of the two, or another <equipment_type> of the same type.`
- 例句: Choose one of the two, or another PCR system of the same type.

### 物料分类标注句式
- 模板: `<item_name> <item_type> <brand_name> <catalog_number>`
- 例句: OCT (Optimal Cutting Temperature compound) Reagent SAKURA Tissue-Tek® O.C.T. compound Sakura

### 功能说明句式
- 模板: `Used for <action>, requiring <requirement>.`
- 例句: Used for tissue fixation, requiring minimal impurities.

### 替代建议句式
- 模板: `It can be replaced by <alternative_criteria>.`
- 例句: it can be replaced by a different brand of the same purity.

### 耗材通用清单句式
- 模板: `<item_name> consumables, <specific_item> <brand> <model>`
- 例句: Slide box consumables, Slide box Beyotime FBX 114

### 限制性建议句式
- 模板: `Select one of the two; it is not recommended to change the <attribute>.`
- 例句: Select one of the two; it is not recommended to change the brand or catalog number.

### 设备分类标注句式
- 模板: `<equipment_name> equipment, <specific_device> <brand> <model>`
- 例句: Cryostat equipment, Cryostat Leica CM1860

### 无推荐品牌说明句式
- 模板: `Other reagents and consumables without recommended brands — <experimental_step>`
- 例句: Other reagents and consumables without recommended brands — tissue removal

### 多选项引导句式
- 模板: `Choose one of two, or other brands of <product_type> of the same type.`
- 例句: Choose one of two, or other brands of PCR reagents of the same type.

### 耗材/设备列举
- 模板: `<item_name> <category>, <item_description> <brand> <catalog_number>`
- 例句: 20 μL pipette tip consumables, 20 μL boxed sterilized short tips with filter, Axygen TXLF-20-L-R-S

### 替代/同类设备建议
- 模板: `<device_name> or other equivalent equipment`
- 例句: refrigerated centrifuge equipment Centrifuge 5429 R, or other equivalent equipment

### 试剂自定义选择说明
- 模板: `<reagent_name>: <specific_item>/selected according to customer requirements`
- 例句: Primary antibody reagent: primary antibody/selected according to customer requirements

### 步骤/前置条件说明
- 模板: `Perform <action> at least <time_period> in advance; <constraint_info>`
- 例句: Perform serum filtration at least 2 days in advance; no needle required, meeting sterile processing requirements.

### 特定试剂补充说明
- 模板: `<reagent_name> reagent: <reagent_description>, <brand> <number>`
- 例句: Horse serum reagent: horse serum, Thermo Fisher Scientific No. 37010081

### 耗材可替换说明
- 模板: `<item_description>, <item_brand> <catalog_number>, replaceable with other brands`
- 例句: Tweezers consumables, Deli tweezers DLxxxxxx, replaceable with other brands

### 试剂特殊纯度/规格更换说明
- 模板: `<item_description> is required, and it can be replaced by the same purity from a different brand`
- 例句: Choose one of the two; nuclease-free water is required, and it can be replaced by the same purity from a different brand

### 设备规格标注
- 模板: `<device_name> (<parameter_1>; <parameter_2>; <parameter_3>)`
- 例句: Pipettes (1000 μL; 200 μL; 20 μL; 2.0 μL)

### 无推荐品牌试剂分类
- 模板: `Other reagents and consumables with no recommended brand — <application_stage>`
- 例句: Other reagents and consumables with no recommended brand — Blocking and antibody incubation

### 二选一/多选一
- 模板: `Choose one of [the two/the options], [condition/reason].`
- 例句: Choose one of the two; it is not recommended to change the brand or catalog number.

### 同类型替代
- 模板: `Or [item/equipment] of the same type.`
- 例句: Or other equipment of the same type.

### 设备/耗材定义
- 模板: `[Item Name] [Category Name], [Item Name] [Brand] [Catalog Number/Model].`
- 例句: Vortex mixer device, Vortex mixer, Kylin-Bell QL-XXXX.

### 组合与建议
- 模板: `[Reagent Name] [Category], [Reagent Name] [Brand] [Catalog Number].`
- 例句: Methanol reagent, Methanol Sigma Aldrich XXXX-XX-R.

### 耗材列举
- 模板: `[Item Name] consumables, [Item Name] [Brand] [Catalog Number].`
- 例句: Tweezers consumables, Deli tweezers DLXXXXX.

### 替换/等价条件
- 模板: `[Condition], can be replaced by [alternative].`
- 例句: Select one; serum filtration at least 2 days in advance; can be replaced by other brands of 1.33 μm filters.

### 实验步骤物料表标题
- 模板: `[Section Number] [Experiment Name] [Third-party] material list [Page Number].`
- 例句: 4.3 mIF pre-experiment third-party material list 22.

### 无推荐品牌备注
- 模板: `Other reagents and consumables [without/with no] recommended brands — [Step Name].`
- 例句: Other reagents and consumables without recommended brands — Tissue fixation.

### 多项选择与条件
- 模板: `Choose one of the two, <condition>`
- 例句: Choose one of the two, requiring the use of nuclease-free water

### 物料使用与替代
- 模板: `Requires the use of <item>; may be substituted with <alternative>`
- 例句: Requires the use of nuclease-free water; may be substituted with the same purity from a different brand

### 无品牌物料标注
- 模板: `Other reagents and consumables with no recommended brand — <step_name>`
- 例句: Other reagents and consumables with no recommended brand — secondary antibody incubation

### 设备配置描述
- 模板: `<device_name> equipment: <device_description>, <brand> <model>`
- 例句: Cryostat equipment: cryostat Leica CM1960

### 同类设备替代
- 模板: `Or <item_name> of the same type from another brand.`
- 例句: Or other brands of the same type for frozen sectioning

### 变更建议
- 模板: `Changing the brand catalog number is not recommended.`
- 例句: Choose one of the two; changing the brand catalog number is not recommended

### 物料用途说明
- 模板: `<item>, used for <purpose>.`
- 例句: Choose one of the two, used for tissue fixation; low impurity content is required

### 准备清单表头
- 模板: `Preparation Item, Category, Name, Recommended Brand, Catalog Number, Remarks, Checklist`
- 例句: Preparation Item, Category, Name, Recommended Brand, Catalog Number, Remarks, Checklist

### Categorization
- 模板: `<Category/Type>: <Description>`
- 例句: Filter consumables: Syringe filter

### Equivalent Equipment
- 模板: `or other <equipment_type> of the same type`
- 例句: or other equipment of the same type

### Item Specification
- 模板: `<Item_Name> reagent, <Detailed_Description>`
- 例句: RI reagent RNase inhibitor

### Replacement Instruction
- 模板: `can be replaced by <alternative_description>`
- 例句: can be replaced by other brands' 0.22 μm filters

### Timing Pre-requisite
- 模板: `<Action> at least <time_period> in advance`
- 例句: Serum filtration at least 2 days in advance

### Requirement Condition
- 模板: `<Requirement> is required; <alternative_action>`
- 例句: Nuclease-free water is required. It can be substituted with the same purity from a different brand.

### Manufacturer Specification
- 模板: `<Brand> <Product_Model>`
- 例句: Leica DM6 M

### 设备/耗材列表项
- 模板: `<Item Name> <Item Specification> <Brand> <Catalog Number>`
- 例句: 20 μL pipette tip consumables, 20 μL racked filter sterile short pipette tips Axygen TXLF-20-L-R-S

### 替代品/同类建议
- 模板: `Choose one of the two, or <another/other> <type/brand> of <device/reagent> of the same type`
- 例句: Choose one of the two, or another brand of PCR of the same type

### 试剂类别描述
- 模板: `Other reagents and consumables without recommended brands — <Procedure Name>`
- 例句: Other reagents and consumables without recommended brands—Reverse transcription reaction

### 功能说明句
- 模板: `Used for <procedure/purpose>; <substitution instruction>`
- 例句: Used for preheating the permeabilization enzyme; other brand catalog numbers (or instruments with equivalent functions) can be substituted

### 推荐使用建议
- 模板: `It is recommended to use the suggested brand catalog number.`
- 例句: It is recommended to use the suggested brand catalog number.

### 设备定义
- 模板: `<Device Name> device, <Device Name>`
- 例句: Vortex mixer device, Vortex mixer

### 耗材包含关系描述
- 模板: `<Item> consumables (<Brand> <Catalog Number>)`
- 例句: Qubit Assay Tube Consumables (Invitrogen Q32856)

### 量具规格表达
- 模板: `<Instrument Name> (<Volume1> μL; <Volume2> μL; <Volume3> μL; <Volume4> μL)`
- 例句: Pipette (1000 μL; 300 μL; 20 μL; 3.6 μL)

### 文件标题映射
- 模板: `<Section Number> <Standard Operating Procedure/Workflow Name>: Third-Party Bill of Materials <Page Number>`
- 例句: 4.4 Standard Operating Procedure for Transcriptome Experiments: Third-Party Bill of Materials 37

### 设备/试剂/耗材定义
- 模板: `<Name> <Category> <Brand/Model>`
- 例句: Vortex Mixer Equipment Vortex Mixer Qilinbeier QL-861

### 二选一说明
- 模板: `Choose one of the two, used for <purpose>.`
- 例句: Choose one of the two, used for library concentration detection

### 同类型设备/耗材提示
- 模板: `<Original_Item>, or other <type> of the same type.`
- 例句: Vortex mixer, or other equipment of the same type

### 推荐品牌货号建议
- 模板: `It is recommended to use the suggested brand catalog number.`
- 例句: It is recommended to use the suggested brand catalog number.

### 物料替代说明
- 模板: `<Requirement> is required. It can be replaced by the same purity from a different brand or a different specification of the same brand.`
- 例句: Nuclease-free water is required. It can be replaced by the same purity from a different brand or a different specification of the same brand.

### 准备项表头
- 模板: `Preparation Item, Category, Name, Recommended Brand, Catalog Number, Remarks, Checklist Item`
- 例句: Preparation Item, Category, Name, Recommended Brand, Catalog Number, Remarks, Checklist Item

### 基础物品描述
- 模板: `<Item_Name> <Category> <Item_Name>`
- 例句: Mini centrifuge equipment mini centrifuge

### 操作提示标识
- 模板: `<Type>: <Content>`
- 例句: Tip: Please download the latest version of the manual and use it with the corresponding version of the kit.

### 物料设备描述
- 模板: `<Item Name> (<Specification/Constraint>)`
- 例句: Magnetic rack (0.1–2 mL)

### 建议/要求表述
- 模板: `Any <item> can be selected; it is recommended to use <recommendation>.`
- 例句: Any magnetic beads can be selected; it is recommended to use the catalog number of the suggested brand.

### 操作步骤动作
- 模板: `<Action> method`
- 例句: Assembly method

### 试剂替换条件
- 模板: `Choose one; requires <condition>, which can be replaced with <alternative>.`
- 例句: Choose one; requires nuclease-free water, which can be replaced with the same purity from a different brand or the same

### 参考指南句式
- 模板: `Please refer to the "<document_name>" to <action>.`
- 例句: Please refer to the "Stereo-seq Chip Carrier Storage Operation Guide" to store the product correctly.

### 建议事项句式
- 模板: `It is recommended to <action>.`
- 例句: It is recommended to preheat the PCR instrument to the reaction temperature.

### 试剂处理操作句式
- 模板: `<Action> (briefly centrifuge/keep on ice/thaw/invert).`
- 例句: Briefly centrifuge the enzyme components and keep on ice for use.

### 禁止与注意事项句式
- 模板: `<Action> should be avoided / <Object> is not required if <condition>.`
- 例句: Direct contact of samples and reagents with skin and eyes should be avoided.

### 参数定义句式
- 模板: `<Parameter>: <Value>.`
- 例句: Storage temperature: 2°C ~ 8°C.

### 试剂稀释句式
- 模板: `Take <amount> of <reagent> and dilute to <volume>.`
- 例句: Take 250 μL of 20X SSC and dilute to 50 mL.

### 信息引用句式
- 模板: `For further information on <topic>, see <reference>.`
- 例句: For further information on product catalog numbers, reagent components, etc., see Tables 1-1 to 1-4.

### 存储条件描述
- 模板: `<Target> storage conditions for <object>: <value>.`
- 例句: Long-term storage conditions for filtered serum: −20°C.

### 设备预冷
- 模板: `Pre-cool the <object> to <temperature>.`
- 例句: Pre-cool the cryostat chamber to −20°C, and the specimen head to −15°C to −10°C.

### 调整建议
- 模板: `Adjust the <parameter> based on <actual_condition>.`
- 例句: Adjust the temperature based on actual operation.

### 异常检查
- 模板: `Check the <object> for <abnormality> and <verb> if necessary.`
- 例句: Check the microscope for any abnormalities and replace if necessary.

### 重复操作
- 模板: `Repeat steps <step_range> <frequency>.`
- 例句: Repeat steps d.-e. once.

### 试剂添加与孵育
- 模板: `Add <amount> of <substance> to the <target>, and incubate at <condition> for <duration>;`
- 例句: Add 200 μL/chip of 0.1X SSC solution to the chip, and incubate at room temperature for 1 minute;

### 操作限制与工具应用
- 模板: `Tilt the <object> at an angle of <condition>, and use a <tool> to <action> the <substance>;`
- 例句: Slightly tilt the hand-held carrier at an angle of less than 20°, and use a pipette to aspirate and discard the 0.1X

### 基于外部引用的流程操作
- 模板: `After <action> the <substance>, refer to <reference> to <process>;`
- 例句: After aspirating the 0.1X SSC solution, refer to the disassembly method in the appendix "Stereo-seq Chip Carrier and Accessories Instruction Manual"

### 安全建议与预防措施
- 模板: `When <action>, <instruction> to avoid <consequence>;`
- 例句: When disassembling, support the back of the carrier by hand to avoid contact between the carrier and the front surface.

### 可选操作提示
- 模板: `Optional: <action> for <duration> using a <device> to <goal>;`
- 例句: Optional: Centrifuge for 10 s using a slide centrifuge (LX-700 micro glass centrifuge) to remove liquid from the chip.

### 状态保持说明
- 模板: `Keeping the <target> <state>;`
- 例句: keeping the tissue on the chip moist;

### 实验方案标题格式
- 模板: `Preparation of <substance_name>`
- 例句: Table 3-2 Preparation of Simulated Secondary Antibody Incubation Solution

### 受控操作序列
- 模板: `Proceed <direction> starting <distance> from <target>, and <action> <speed> at an angle of <angle>.`
- 例句: Proceed sequentially starting 2-3 cm from one corner of the chip, and blow air slowly at an angle of approximately 30°.
