"""用 Gemini 从新译文中提炼句式规律（自动蒸馏句法）。

输入：一批 {zh, en} 对照样本
输出：高频句式规律 {句式描述: 英文模板 + 真实例句}
增量合并进 sentence_patterns.md。
"""

import json
import os
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

GEMINI_MODEL = os.environ.get("GEMINI_TRANSLATE_MODEL", "gemini-3.1-flash-lite")

EXTRACT_PROMPT = """你是一名翻译风格分析专家。下面是若干条 {中文, 英文} 对照样本（来自 STOmics/Stereo-seq 技术文档翻译）。

请分析 Gemini 的**翻译句式规律**，提炼出高频、可复用的句式模板。

规则：
1. 找出样本中反复出现的句式（操作指令、条件句、步骤衔接、建议、用量表达、禁止等）。
2. 每条给出：句式名称、英文模板（用占位符如 <verb>/<object>）、1-2 条真实例句。
3. 输出为 JSON 数组，每项是 {"name": "句式名", "template": "英文模板", "example": "真实例句"}。
4. 提取 5-12 条句式即可。
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
    return "\n".join(
        ln for ln in (proc.stdout or "").splitlines()
        if ln.strip() and "Loaded cached credentials" not in ln
    ).strip()


def _parse_json(text: str) -> list:
    import re
    text = re.sub(r"```(json)?", "", text).strip()
    start, end = text.find("["), text.rfind("]")
    if start != -1 and end > start:
        text = text[start:end + 1]
    return json.loads(text)


def extract_patterns_from_pairs(pairs: list, max_samples: int = 60) -> list:
    sample_txt = "\n".join(
        f"中文: {d['zh'][:120]}\n英文: {d['en'][:120]}\n"
        for d in pairs[:max_samples]
    )
    prompt = EXTRACT_PROMPT.replace("{样本}", sample_txt)
    out = _run_gemini(prompt)
    patterns = _parse_json(out)
    clean = []
    for p in patterns if isinstance(patterns, list) else []:
        if isinstance(p, dict) and p.get("name") and p.get("template"):
            clean.append({
                "name": p["name"].strip(),
                "template": p["template"].strip(),
                "example": (p.get("example") or "").strip(),
            })
    return clean


def dump_patterns(patterns: list, out_path: Path):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if not patterns:
        print("无新句式")
        return
    with open(out_path, "a", encoding="utf-8") as f:
        f.write(f"\n## 自动蒸馏新增句式（{date.today()}）\n")
        for p in patterns:
            f.write(f"\n### {p['name']}\n")
            f.write(f"- 模板: `{p['template']}`\n")
            if p["example"]:
                f.write(f"- 例句: {p['example']}\n")
    print(f"新增 {len(patterns)} 条句式 → {out_path.name}")


if __name__ == "__main__":
    pairs = [json.loads(l) for l in open(ROOT / "corpus" / "clean_pairs.jsonl", encoding="utf-8")]
    print(f"读入 {len(pairs)} 对样本")
    patterns = extract_patterns_from_pairs(pairs, max_samples=60)
    print(f"Gemini 提取到 {len(patterns)} 条句式")
    for p in patterns[:12]:
        print(f"  {p['name']}: {p['template']}")