"""纯数据提取术语表 v2：用 jieba 分词 + 词性过滤 + 位置对齐。

改进点：
1. jieba 正确分词，不再切碎标题
2. 词性过滤：只保留专业名词/专有名词（排除虚词、动词、形容词）
3. 位置对齐：中文词的位置比例映射到英文，取最近的英文短语
4. 输出干净的中文术语 → 英文译法映射
"""

import json
import re
import sys
from collections import Counter, defaultdict

import jieba
import jieba.posseg as pseg

sys.stdout.reconfigure(encoding='utf-8')

pairs = [json.loads(l) for l in open('corpus/clean_pairs.jsonl', encoding='utf-8')]

# 虚词词性过滤：只保留名词类
KEEP_FLAG = ('n', 'nz', 'nrt', 'ns', 'nt', 'nw', 'nr', 'eng', 'vn')
# 明显非术语的通用词
STOP_WORDS = {
    '进行','使用','加入','取出','放置','覆盖','清洗','保存','储存','检测','反应',
    '操作','步骤','说明','内容','信息','方法','标准','要求','条件','情况','过程',
    '结果','方式','方面','问题','作用','影响','需要','能够','可能','应该','必须',
    '不要','禁止','避免','保持','确保','准备','完成','开始','结束','继续','按照',
    '根据','参照','参考','例如','如果','以及','并且','或者','因为','所以','但是',
    '然后','之后','之前','其中','本次','同时','随时','尽快','立即','本设备','产品',
    '试剂','组分','样本','样品','实验','工作液','储存液','工作','使用','请','勿',
    '将','于','在','对','为','从','向','被','把','的','了','和','与','或','及','其',
    '已经被','后','前','中','上','下','内','外','适当','适量','充分','完全','轻轻',
    '立即','说明','指导','指南','内容','部分','相关','文件','文档','材料','设备',
}

def tokenize_zh(text):
    """用 jieba 分词，返回 (word, pos) 列表，过滤虚词和停用词。"""
    out = []
    for w, flag in pseg.cut(text):
        w = w.strip()
        if not w or len(w) < 2:
            continue
        if flag[:1] not in KEEP_FLAG and flag[:2] != 'nz':
            # 保留专业名词（nz 专有名词）
            if not (flag.startswith('n')):
                continue
        if w in STOP_WORDS:
            continue
        if re.match(r'^[\d°℃μXxXⅩ]+$', w):
            continue
        out.append(w)
    return out

# 统计中文词频
word_zh_count = Counter()
# 中文词 -> 对应英文段落（位置对齐）
word_trans_map = defaultdict(Counter)

for d in pairs:
    zh, en = d['zh'], d['en']
    zh_words = tokenize_zh(zh)
    en_words = re.findall(r'[A-Za-z][A-Za-z\-]+|μL|[0-9\.]+', en)
    if not zh_words or not en_words:
        continue
    zh_len = len(zh)
    for w in zh_words:
        word_zh_count[w] += 1
        idx = zh.find(w)
        if idx < 0:
            continue
        pos_ratio = idx / max(zh_len, 1)
        en_idx = min(int(pos_ratio * len(en_words)), len(en_words) - 1)
        # 取位置最近的英文词对（2-4 个词的短语）
        start = max(0, en_idx - 1)
        end = min(len(en_words), en_idx + 3)
        phrase = ' '.join(en_words[start:end])
        word_trans_map[w][phrase] += 1

# 输出
print("=== 纯数据提取术语表 v2（jieba 分词）===\n")
print("| 中文 | 英文译法（样本最高频） | 频次 |")
print("|---|---|---|")
for w, cnt in word_zh_count.most_common():
    if cnt < 3:
        continue
    top = word_trans_map[w].most_common(1)
    if not top:
        continue
    phrase = top[0][0]
    print(f"| {w} | **{phrase}** | {cnt} |")