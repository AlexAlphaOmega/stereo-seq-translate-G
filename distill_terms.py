"""用 Gemini 从新译文中提取术语对照（自动蒸馏核心）。

输入：一批 {zh, en} 对照样本
输出：新增的高频术语对照 {中文术语: 英文标准译法}

让 Gemini 自己读样本、抽术语，天然准确。增量合并进种子术语库。
"""

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

# gemini-cli 走已登录的网页会话，无需 API key
GEMINI_MODEL = os.environ.get("GEMINI_TRANSLATE_MODEL", "gemini-3.1-flash-lite")

EXTRACT_PROMPT = """你是一名专业术语提取专家。下面是若干条 {中文, 英文} 对照样本（来自 STOmics/Stereo-seq 技术文档翻译）。

请从中提取**高频专业术语对照**：中文术语 → 英文标准译法。

规则：
1. 只提取专业术语（生物技术、仪器、试剂、操作、单位），不提取通用虚词（的/了/进行）或普通句子。
2. 同一中文术语在样本中多次出现时，取统一的英文标准译法。
3. 输出为 JSON 数组，每项是 {"zh": "中文术语", "en": "英文译法"}。
4. 提取 10-30 条即可，选最高频、最有代表性的。
5. 只输出 JSON，不要其他文字。

样本：
{样本}
"""


def _run_gemini(prompt: str, timeout: int = 120) -> str:
    import shutil
    env = dict(os.environ)
    env.setdefault("GEMINI_CLI_TRUST_WORKSPACE", "true")
    bin_path = shutil.which("gemini") or "gemini"
    proc = subprocess.run(
        [bin_path, "-m", GEMINI_MODEL],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=timeout,
        env=env,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"gemini-cli exit {proc.returncode}: {proc.stderr[-300:]}")
    # 去掉 banner
    return "\n".join(
        ln for ln in (proc.stdout or "").splitlines()
        if ln.strip() and "Loaded cached credentials" not in ln
    ).strip()


def _parse_json(text: str) -> list:
    """容忍 markdown 围栏和前后杂物，提取 JSON 数组。"""
    import re
    text = re.sub(r"```(json)?", "", text).strip()
    # 找第一个 [ 到最后一个 ]
    start, end = text.find("["), text.rfind("]")
    if start != -1 and end > start:
        text = text[start:end + 1]
    return json.loads(text)


def extract_terms_from_pairs(pairs: list, max_samples: int = 60) -> list:
    """让 Gemini 从样本中提取术语对照。pairs: [{zh, en}, ...]"""
    sample_txt = "\n".join(
        f"中文: {d['zh'][:120]}\n英文: {d['en'][:120]}\n"
        for d in pairs[:max_samples]
    )
    prompt = EXTRACT_PROMPT.replace("{样本}", sample_txt)
    out = _run_gemini(prompt)
    terms = _parse_json(out)

    # 校验结构
    clean = []
    for t in terms if isinstance(terms, list) else []:
        if isinstance(t, dict) and t.get("zh") and t.get("en"):
            clean.append({"zh": t["zh"].strip(), "en": t["en"].strip()})
    return clean


def dump_terms(terms: list, out_path: Path):
    """以 markdown 追加/合并方式写入术语库。"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # 读已有术语，避免重复
    existing = {}
    if out_path.exists():
        for line in out_path.read_text(encoding="utf-8").splitlines():
            if "→" in line:
                zh, en = line.split("→", 1)
                existing[zh.strip()] = en.strip()

    new_terms = []
    for t in terms:
        if t["zh"] not in existing:
            existing[t["zh"]] = t["en"]
            new_terms.append(t)

    if not new_terms:
        print(f"无新增术语（{out_path.name}）")
        return

    # 追加到文件末尾（追加区块）
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(f"\n## 自动蒸馏新增（{len(new_terms)} 条）\n")
        f.write(f"> 由 Gemini 于 {sys_date()} 自动提取\n\n")
        for t in new_terms:
            f.write(f"- {t['zh']} → **{t['en']}**\n")
    print(f"新增 {len(new_terms)} 条术语 → {out_path.name}")


def sys_date():
    from datetime import date
    return str(date.today())


if __name__ == "__main__":
    # 测试：从最干净的样本里提取
    pairs = [json.loads(l) for l in open(ROOT / "corpus" / "clean_pairs.jsonl", encoding="utf-8")]
    print(f"读入 {len(pairs)} 对样本")
    terms = extract_terms_from_pairs(pairs, max_samples=60)
    print(f"Gemini 提取到 {len(terms)} 条术语")
    for t in terms[:15]:
        print(f"  {t['zh']} → {t['en']}")