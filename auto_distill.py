"""自动蒸馏主入口：翻译新说明书 → 提取术语/句式 → 更新 skill。

完整闭环（无人值守）：
1. 翻译 pending/ 里的新中文说明书（走 gemini-cli + 语料注入）
2. 从新增译文里用 Gemini 提取术语对照 → 合并进 skill 的 terminology/
3. 从新增译文里用 Gemini 提炼句式 → 合并进 skill 的 sentence_patterns.md
4. 新译文追加进 skill 的 pairs.jsonl（样本库持续增长）

运行：python auto_distill.py
"""

import json
import os
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

# skill 的蒸馏数据目录
SKILL_DIR = Path(r"C:\Users\Lc\.claude\skills\gemini-style-translate\distilled_data")

from run_translation import (                   # noqa: E402
    translate_one_manual, translate_pdf_manual,
    CheckpointStore, RateLimiter, Corpus, load_term_rules,
)
from distill_terms import (                     # noqa: E402
    extract_terms_from_pairs, dump_terms,
)
from distill_patterns import (                  # noqa: E402
    extract_patterns_from_pairs, dump_patterns,
)

import logging
logger = logging.getLogger(__name__)


def _load_clean_pairs(limit: int = 60) -> list:
    """从 corpus 读最近干净样本。"""
    p = ROOT / "corpus" / "clean_pairs.jsonl"
    if not p.exists():
        return []
    lines = p.read_text(encoding="utf-8").splitlines()
    return [json.loads(l) for l in lines[-limit:]]


def _clean_corpus():
    """重新清洗 raw pairs → clean_pairs，让样本库跟随新译文增长。"""
    from src.corpus_cleaner import clean_pairs
    clean_pairs(ROOT / "corpus" / "pairs.jsonl", ROOT / "corpus" / "clean_pairs.jsonl")


def _sync_skill_data():
    """确保 skill 的蒸馏数据与 corpus 同步。"""
    SKILL_DIR.mkdir(parents=True, exist_ok=True)

    # 1. 同步样本库（追加新译文）
    src = ROOT / "corpus" / "clean_pairs.jsonl"
    dst = SKILL_DIR / "pairs.jsonl"
    if src.exists():
        dst.write_bytes(src.read_bytes())
    logger.info("同步样本库 → %s (%d 行)", dst.name, len(dst.read_bytes().splitlines()) if dst.exists() else 0)

    # 2. 同步术语库目录（种子语料库）
    src_terms = ROOT / "corpus" / "terminology"
    dst_terms = SKILL_DIR / "terminology"
    dst_terms.mkdir(parents=True, exist_ok=True)
    for f in src_terms.glob("*.md"):
        (dst_terms / f.name).write_bytes(f.read_bytes())
    logger.info("同步术语库种子 → %s", dst_terms)

    # 3. 同步自动蒸馏产物（terminology.md / sentence_patterns.md）回项目，供 git 提交
    for fname in ("terminology.md", "sentence_patterns.md"):
        src_f = SKILL_DIR / fname
        dst_f = ROOT / "corpus" / fname
        if src_f.exists():
            dst_f.parent.mkdir(parents=True, exist_ok=True)
            dst_f.write_bytes(src_f.read_bytes())
    logger.info("同步蒸馏产物回项目 corpus/")


def _write_daily_report(stats: dict):
    """生成每日总结报告（不立即弹窗，由 9:00 的通知任务弹窗）。"""
    report_path = ROOT / "daily_report.md"
    lines = [
        f"# Gemini 自动蒸馏日报（{date.today()}）",
        "",
        f"- 待翻译说明书: {stats['pending']}",
        f"- 翻译段数: {stats['translated']}",
        f"- 翻译失败段数: {stats['failed']}",
        f"- 新增术语: {stats['new_terms']}",
        f"- 新增句式: {stats['new_patterns']}",
        f"- 样本库累计: {stats['corpus_pairs']} 对",
        "",
    ]
    report_path.write_text("\n".join(lines), encoding="utf-8")
    logger.info("日报已生成 → %s", report_path)
    return report_path


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    stats = {"pending": 0, "translated": 0, "failed": 0,
             "new_terms": 0, "new_patterns": 0, "corpus_pairs": 0}

    # 每日翻译段数上限（0=无限制）。防止一次翻太多撞订阅限流。
    MAX_PARAGRAPHS = int(os.environ.get("GEMINI_DAILY_PARAGRAPHS", "200"))

    # 1. 翻译新说明书
    from queue_manager import list_pending
    checkpoint = CheckpointStore(ROOT / "logs" / "checkpoints.json")
    rate_limiter = RateLimiter(ROOT / "logs" / "usage.json")
    corpus = Corpus(ROOT / "corpus")
    rules = load_term_rules()
    term_block = rules.to_prompt_block()

    pending = list_pending(ROOT / "pending")
    stats["pending"] = len(pending)
    if pending:
        logger.info("待翻译 %d 份说明书（每日段数上限 %d）", len(pending), MAX_PARAGRAPHS)
        daily_budget = MAX_PARAGRAPHS
        for mfile in pending:
            if daily_budget <= 0:
                logger.info("达到每日总段数上限，剩余说明书留待下次")
                break
            try:
                if mfile.suffix.lower() == ".pdf":
                    fn = translate_pdf_manual
                else:
                    fn = translate_one_manual
                # 每本传固定上限，让一本书尽量翻一大块；全局 daily_budget 控制总段数
                res = fn(
                    mfile, checkpoint, rate_limiter, corpus, ROOT / "done",
                    prompt_prefix=term_block, max_paragraphs=MAX_PARAGRAPHS,
                )
                translated_now = res.get("translated", 0)
                stats["translated"] += translated_now
                stats["failed"] += res.get("failed", 0)
                daily_budget -= translated_now
                logger.info("翻译完成: %s", res)
            except Exception as e:
                logger.error("翻译失败 %s: %s", mfile.name, e)
                stats["failed"] += 1
    else:
        logger.info("无待翻译说明书，跳过翻译步骤")

    # 2. 重新清洗语料，让样本库包含最新译文
    _clean_corpus()

    # 3. 用 Gemini 提取术语 + 句式（从最近样本）
    pairs = _load_clean_pairs(limit=60)
    if pairs:
        logger.info("从 %d 对样本蒸馏...", len(pairs))
        terms = extract_terms_from_pairs(pairs, max_samples=60)
        if terms:
            dump_terms(terms, SKILL_DIR / "terminology.md")
            stats["new_terms"] = len(terms)
            logger.info("新增术语 %d 条", len(terms))

        patterns = extract_patterns_from_pairs(pairs, max_samples=60)
        if patterns:
            dump_patterns(patterns, SKILL_DIR / "sentence_patterns.md")
            stats["new_patterns"] = len(patterns)
            logger.info("新增句式 %d 条", len(patterns))
    else:
        logger.warning("无样本可蒸馏")

    # 3. 同步样本库和种子术语库
    _sync_skill_data()
    stats["corpus_pairs"] = corpus.count()
    logger.info("自动蒸馏完成，skill 已更新")

    # 4. 每日总结报告
    _write_daily_report(stats)

    # 5. 同步 skill 蒸馏数据到 GitHub
    try:
        from git_sync import main as git_main
        git_main()
    except Exception as e:
        logger.error("GitHub 同步失败: %s", e)


if __name__ == "__main__":
    main()