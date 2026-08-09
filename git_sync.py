"""把完整 skill 同步到 GitHub 仓库。

每次自动蒸馏后运行：将完整 skill（SKILL.md + distilled_data/）复制到仓库的
gemini-style-translate/ 子目录，提交并推送到 GitHub。
别人 clone 下来即可用 install.sh / install.bat 安装。

用法：python git_sync.py
"""

import logging
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILL_DIR = Path(r"C:\Users\Lc\.claude\skills\gemini-style-translate")
# 仓库里的 skill 子目录
REPO_SKILL = ROOT / "gemini-style-translate"

logger = logging.getLogger(__name__)


def _collect():
    """把完整 skill 复制到仓库的子目录。"""
    if not SKILL_DIR.exists():
        logger.error("skill 目录不存在: %s", SKILL_DIR)
        return False

    # 清空旧的仓库 skill 目录（排除 .git）
    if REPO_SKILL.exists():
        shutil.rmtree(REPO_SKILL)
    REPO_SKILL.mkdir(parents=True, exist_ok=True)

    # 复制 SKILL.md
    shutil.copy2(SKILL_DIR / "SKILL.md", REPO_SKILL / "SKILL.md")

    # 复制 distilled_data/
    src_data = SKILL_DIR / "distilled_data"
    dst_data = REPO_SKILL / "distilled_data"
    dst_data.mkdir(parents=True, exist_ok=True)
    for f in src_data.glob("*.jsonl"):
        shutil.copy2(f, dst_data / f.name)
    for f in src_data.glob("*.md"):
        shutil.copy2(f, dst_data / f.name)
    # 复制 terminology/ 子目录
    src_term = src_data / "terminology"
    if src_term.exists():
        dst_term = dst_data / "terminology"
        if dst_term.exists():
            shutil.rmtree(dst_term)
        shutil.copytree(src_term, dst_term)

    logger.info("已同步完整 skill → %s", REPO_SKILL)
    return True


def _git(cmd: list, timeout: int = 120):
    r = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, timeout=timeout)
    if r.returncode != 0:
        logger.warning("git %s 失败: %s", cmd[0], r.stderr.strip()[:200])
    return r


def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    if not _collect():
        return

    # git add skill + 安装脚本 + marketplace + README + 蒸馏产物
    _git(["git", "add", "gemini-style-translate/", "install.sh", "install.bat",
          ".claude-plugin/", "README.md", "dist/"])

    msg = f"auto-distill {date.today()}: sync full skill to repo"
    r = _git(["git", "commit", "-m", msg])
    if "nothing to commit" in r.stdout or "nothing to commit" in r.stderr:
        logger.info("无新变化，跳过提交")
        return

    logger.info("推送至 GitHub...")
    r = _git(["git", "push", "origin", "HEAD"])
    if r.returncode == 0:
        logger.info("✅ 已推送完整 skill 到 GitHub")
    else:
        logger.error("推送失败: %s", r.stderr.strip()[:300])


if __name__ == "__main__":
    main()