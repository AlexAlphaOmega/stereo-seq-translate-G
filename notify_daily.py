"""9:00 定时通知脚本：读每日日报 + Windows 弹窗通知。

由 Windows 定时任务在每天早上 9:00 运行，读取 auto_distill 凌晨 1 点生成的
日报，弹窗提醒用户。若日报不存在（凌晨任务没跑），提示异常。
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def _read_report() -> str:
    p = ROOT / "daily_report.md"
    if not p.exists():
        return "日报不存在——凌晨 1:00 的自动蒸馏任务可能未运行。"
    return p.read_text(encoding="utf-8")


def _notify_windows(title: str, body: str):
    """Windows 桌面通知。用 PowerShell 弹窗（有焦点时）或 toast（可后台）。"""
    # 转义单引号，防止 PowerShell 报错
    body_esc = body.replace("'", "''").replace("\n", " ")
    ps_script = (
        "Add-Type -AssemblyName System.Windows.Forms; "
        f"[System.Windows.Forms.MessageBox]::Show('{body_esc}', '{title}', 'OK', 'Information')"
    )
    try:
        subprocess.run(
            ["powershell", "-NoProfile", "-Command", ps_script],
            capture_output=True, timeout=15,
        )
    except Exception as e:
        print(f"弹窗失败: {e}")


def main():
    title = "Gemini 自动蒸馏日报"
    report = _read_report()
    # 提取要点做弹窗摘要
    lines = [l for l in report.splitlines() if l.startswith("- ")]
    summary = " | ".join(l.lstrip("- ").strip() for l in lines[:6])
    print(summary)
    _notify_windows(title, summary or report)
    print(f"已通知，日报: {ROOT / 'daily_report.md'}")


if __name__ == "__main__":
    main()