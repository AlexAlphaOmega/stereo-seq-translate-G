"""从 710 对 Gemini 真实译文样本中统计句式模式。

目的：用数据决定 Gemini 翻译的句式规律，而不是人工归纳。
输出：按中英文句法特征统计的高频模式 + 具体真实例句。
"""

import json
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

pairs = [json.loads(l) for l in open('corpus/clean_pairs.jsonl', encoding='utf-8')]

def zh_sentences(text):
    # 中文句号/分号/问号/感叹号切分
    return [s.strip() for s in re.split(r'[。；!?！？]', text) if s.strip()]

def en_sentences(text):
    # 英文句号/分号/问号切分（保留缩写如 5°C 不误切）
    return [s.strip() for s in re.split(r'(?<=[.;!?])\s+', text) if s.strip()]

# ========== 1. 句式长度对比 ==========
split_stats = Counter()  # 英文句数 vs 中文句数
for d in pairs:
    zs, es = len(zh_sentences(d['zh'])), len(en_sentences(d['en']))
    if es > zs:
        split_stats['en_more_split'] += 1
    elif es < zs:
        split_stats['en_merged'] += 1
    else:
        split_stats['same'] += 1

print("=== 1. 中文长句是否被拆成英文多句 ===")
total = len(pairs)
for k, v in split_stats.most_common():
    print(f"  {k}: {v} ({v/total*100:.0f}%)")

# ========== 2. 英文句首动词（祈使句检测） ==========
verb_starts = Counter()
for d in pairs:
    for s in en_sentences(d['en']):
        m = re.match(r"^(Do not|Add|Place|Remove|Wash|Dry|Incubate|Cover|Tilt|Use|Take|Ensure|Refer|Repeat|Keep|Store|Prepare|Transfer|Mix|Centrifuge|Aspirate|Pipette|Carefully|Gently|Then|After|Before|If|When|For|It is|The|A|This)", s)
        if m:
            verb_starts[m.group(1)] += 1

print("\n=== 2. 英文句首模式（祈使句/连接词）===")
for k, v in verb_starts.most_common(20):
    print(f"  {k}: {v}")

# ========== 3. 高频英文句式片段 ==========
pattern_counter = Counter()
for d in pairs:
    en = d['en']
    # 常见句式：do not ... while ..., after ..., if ..., at ... for ..., 量词 /chip
    for pat in [
        r"Do not \w+",
        r"after \w+",
        r"if \w+",
        r"\bat \d+[°C℃]",
        r"\bfor \d+ min",
        r"/chip",
        r"μL",
        r"refer to",
        r"repeat steps",
        r"ensure",
        r"it is recommended",
        r"must be stored",
        r"is suitable for",
        r"protect from light",
        r"at room temperature",
        r"carefully",
        r"gently",
    ]:
        if re.search(pat, en, re.I):
            pattern_counter[pat] += 1

print("\n=== 3. 高频句式片段出现次数 ===")
for k, v in pattern_counter.most_common():
    print(f"  {k}: {v}")

# ========== 4. 真实例句抽样（按句式分类） ==========
print("\n=== 4. 真实例句（含特定句式的 {zh,en} 对）===")
examples = {
    "祈使句(Place/Add/Remove)": r"^(Place|Add|Remove|Wash|Dry|Incubate|Cover|Tilt|Use)",
    "禁止(Do not)": r"^Do not",
    "条件(If/When)": r"^(If|When)",
    "建议(It is recommended)": r"it is recommended",
    "步骤衔接(After/Then)": r"^(After|Then)",
    "用量(/chip, μL)": r"/chip|μL",
    "温度时间(at..for)": r"at \d+[°C℃].*for \d+ min",
}
seen = set()
for label, pat in examples.items():
    print(f"\n--- {label} ---")
    count = 0
    for d in pairs:
        if re.search(pat, d['en'], re.I):
            key = (d['zh'][:20], d['en'][:20])
            if key not in seen:
                seen.add(key)
                print(f"  ZH: {d['zh'][:40]}")
                print(f"  EN: {d['en'][:70]}")
                count += 1
                if count >= 3:
                    break