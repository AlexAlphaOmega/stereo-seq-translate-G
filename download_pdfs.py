"""从 STOmics 官网批量下载中文说明书 PDF 到 pending/。

来源：https://www.stomics.tech/resources/Documents/list.html
接口：POST /ajax/searchZiyuanWdkPage（分页）
下载：PDF 存到 pending/ 供自动翻译+蒸馏。

用法：python download_pdfs.py [--limit N] [--column 56]
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PENDING = ROOT / "pending"

API_URL = "https://www.stomics.tech/ajax/searchZiyuanWdkPage"
REFERER = "https://www.stomics.tech/resources/Documents/list.html"
SITE_ID = "1"


def _fetch_page(page_index: int, page_size: int, column_id: str) -> list:
    """调接口拿一页文档列表。"""
    body = json.dumps({
        "siteId": SITE_ID,
        "pageIndex": page_index,
        "pageSize": page_size,
        "columnId": column_id,
        "searchFields": {
            "keyword": "",
            "types": "",
            "order": " PUBLISHDATE DESC,SORT DESC"
        }
    }).encode("utf-8")
    req = urllib.request.Request(
        API_URL, data=body,
        headers={
            "Content-Type": "application/json",
            "Referer": REFERER,
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8")).get("info", {}).get("list", [])


def _safe_filename(title: str, url: str) -> str:
    """从标题或 URL 生成安全的文件名。"""
    # 优先用 URL 末尾的文件名（含英文编号）
    m = re.search(r"/([^/]+\.pdf)$", url, re.I)
    if m:
        name = urllib.parse.unquote(m.group(1))
    else:
        name = title
    # 去掉非法文件名字符
    name = re.sub(r'[\\/:*?"<>|\s]+', '_', name).strip("_")
    if not name.lower().endswith(".pdf"):
        name += ".pdf"
    return name


def download_pdf(url: str, dest: Path) -> bool:
    """下载 PDF 到 dest，返回是否成功。"""
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0", "Referer": REFERER}
        )
        with urllib.request.urlopen(req, timeout=60) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        return dest.exists() and dest.stat().st_size > 1000
    except Exception as e:
        print(f"下载失败 {url}: {e}")
        return False


def _encode_url(url: str) -> str:
    """编码 URL 里的中文/空格，保留已编码的 %、/、:、.。"""
    from urllib.parse import quote
    return quote(url, safe="/:%.?=&@")


def main():
    import urllib.parse
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="最大下载数量（0=全部）")
    parser.add_argument("--column", default="56", help="文档分类 columnId")
    parser.add_argument("--page-size", type=int, default=20)
    args = parser.parse_args()

    PENDING.mkdir(parents=True, exist_ok=True)
    # 清理 pending 里可能残留的 .part 或损坏文件
    for stale in PENDING.glob("*.part"):
        stale.unlink()

    downloaded = 0
    skipped = 0
    page = 1
    while True:
        items = _fetch_page(page, args.page_size, args.column)
        if not items:
            break
        print(f"第 {page} 页: {len(items)} 条")
        for it in items:
            title = it.get("TITLE", "")
            url = it.get("OUT_LINK") or it.get("FILE", "")
            if not url or ".pdf" not in url.lower():
                continue
            # OUT_LINK 和 FILE 都可能含未编码中文，统一编码
            raw_url = _encode_url(url)
            fname = _safe_filename(title, raw_url)
            dest = PENDING / fname
            if dest.exists():
                print(f"  跳过(已存在): {fname}")
                skipped += 1
                continue
            print(f"  下载: {fname}")
            if download_pdf(raw_url, dest):
                downloaded += 1
            else:
                if dest.exists():
                    dest.unlink()
            if args.limit and downloaded + skipped >= args.limit:
                print(f"达到上限 {args.limit}")
                break
        if args.limit and downloaded + skipped >= args.limit:
            break
        if len(items) < args.page_size:
            break
        page += 1

    print(f"\n完成: 下载 {downloaded} 个, 跳过(已存在) {skipped} 个")
    print(f"pending/ 现有 {len(list(PENDING.glob('*.pdf')))} 个 PDF")


if __name__ == "__main__":
    main()