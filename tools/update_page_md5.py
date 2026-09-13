#!/usr/bin/env python3
from pathlib import Path
import argparse
import hashlib
import re

PAGE_RE = re.compile(r"%<PAGE-CONTENT:(\d+)>\n(.*?)\n%</PAGE-CONTENT:\1>", re.S)
DESC_RE = re.compile(r"%<PAGE-DESC:(\d+)>(.*)")
HASH_DEF_RE = re.compile(
    r"\\expandafter\\def\\csname PageMDfive(\d+)\\endcsname\{([0-9a-fA-F]{32})\}"
)


def normalize(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    return "\n".join(ln.rstrip() for ln in s.split("\n")).strip() + "\n"


def md5(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def parse_pages(text: str):
    pages = {int(n): payload for n, payload in PAGE_RE.findall(text)}
    if not pages:
        raise RuntimeError("No PAGE-CONTENT markers found")
    nums = sorted(pages)
    if nums != list(range(1, max(nums) + 1)):
        raise RuntimeError(f"PAGE-CONTENT ids must be contiguous from 1: found {nums}")
    return pages


def parse_descriptions(text: str, pages: dict[int, str]):
    desc = {int(n): d.strip() for n, d in DESC_RE.findall(text)}
    missing = [n for n in pages if n not in desc]
    if missing:
        raise RuntimeError(f"Missing PAGE-DESC markers for pages: {missing}")
    return desc


def current_hashes(text: str):
    return {int(n): h.lower() for n, h in HASH_DEF_RE.findall(text)}


def find_index_page(pages: dict[int, str]) -> int:
    matches = [n for n, p in pages.items() if "%<PAGE-INTEGRITY-ROWS>" in p]
    if len(matches) != 1:
        raise RuntimeError("Exactly one page must contain PAGE-INTEGRITY-ROWS markers")
    return matches[0]


def build_rows(pages: dict[int, str], desc: dict[int, str]) -> str:
    return "\n".join(
        rf"\IntegrityRow{{{n}}}{{{desc[n]}}}{{\PageMDfive{{{n}}}}}" for n in sorted(pages)
    )


def replace_integrity_rows(text: str, rows: str) -> str:
    pattern = re.compile(r"(%<PAGE-INTEGRITY-ROWS>\n).*?(\n%</PAGE-INTEGRITY-ROWS>)", re.S)
    new_text, count = pattern.subn(lambda m: m.group(1) + rows + m.group(2), text, count=1)
    if count != 1:
        raise RuntimeError("Could not update PAGE-INTEGRITY-ROWS")
    return new_text


def replace_hash_defs(text: str, hashes: dict[int, str]) -> str:
    defs = "\n".join(
        rf"\expandafter\def\csname PageMDfive{n}\endcsname{{{hashes[n]}}}" for n in sorted(hashes)
    )
    pattern = re.compile(r"(%<PAGE-HASH-DEFS>\n).*?(\n%</PAGE-HASH-DEFS>)", re.S)
    new_text, count = pattern.subn(lambda m: m.group(1) + defs + m.group(2), text, count=1)
    if count != 1:
        raise RuntimeError("Could not update PAGE-HASH-DEFS")
    return new_text


def canonical_payload(payload: str, page: int, index_page: int, hashes: dict[int, str]) -> str:
    p = payload
    p = re.sub(r"^.*MD5 contenuto pagina\s+\d+:.*$", "", p, flags=re.MULTILINE)
    p = re.sub(r"^\\PageHashFooter\{.*?\}\s*$", "", p, flags=re.MULTILINE)
    if page == index_page:
        def repl(m):
            n = int(m.group(1))
            return "<SELF>" if n == index_page else hashes[n]
        p = re.sub(r"\\PageMDfive\{(\d+)\}", repl, p)
    return normalize(p)


def compute_hashes(text: str):
    pages = parse_pages(text)
    desc = parse_descriptions(text, pages)
    index_page = find_index_page(pages)
    text = replace_integrity_rows(text, build_rows(pages, desc))
    pages = parse_pages(text)
    old = current_hashes(text)
    hashes: dict[int, str] = {}
    for n in sorted(pages):
        if n != index_page:
            hashes[n] = md5(canonical_payload(pages[n], n, index_page, hashes))
    hashes[index_page] = md5(canonical_payload(pages[index_page], index_page, index_page, hashes))
    return text, pages, desc, index_page, old, hashes


def write_index(index_path: Path, title: str, desc: dict[int, str], index_page: int, hashes: dict[int, str]):
    lines = [
        f"{title} - Page MD5 Index",
        "Canonical payload: LaTeX content between PAGE-CONTENT markers; own printed MD5 excluded.",
        "Integrity-index page resolves all other page hashes and canonicalizes its own hash as <SELF>.",
        "",
    ]
    for n in sorted(hashes):
        suffix = " [INTEGRITY INDEX]" if n == index_page else ""
        lines.append(f"Page {n}  {hashes[n]}  {desc[n]}{suffix}")
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main():
    parser = argparse.ArgumentParser(description="Update per-page MD5 hashes for PAGE-CONTENT-marked DDTA LaTeX documents.")
    parser.add_argument("tex", nargs="?", help="LaTeX source. Defaults to the single DDTA*.tex file beside this script.")
    parser.add_argument("--index", help="Output text index path. Defaults to PAGE_MD5_INDEX.txt beside the TeX file.")
    parser.add_argument("--title", help="Title used in the text index. Defaults to the TeX stem.")
    args = parser.parse_args()

    root = Path(__file__).resolve().parent
    if args.tex:
        tex = Path(args.tex).resolve()
    else:
        candidates = sorted(p for p in root.glob("DDTA*.tex") if p.is_file())
        if len(candidates) != 1:
            raise RuntimeError("Specify the TeX path explicitly when zero or multiple DDTA*.tex files are present")
        tex = candidates[0]
    index_path = Path(args.index).resolve() if args.index else tex.with_name("PAGE_MD5_INDEX.txt")
    title = args.title or tex.stem

    text = tex.read_text(encoding="utf-8")
    text, pages, desc, index_page, old, hashes = compute_hashes(text)
    text = replace_hash_defs(text, hashes)
    tex.write_text(text, encoding="utf-8", newline="\n")
    write_index(index_path, title, desc, index_page, hashes)

    for n in sorted(hashes):
        status = "UNCHANGED" if old.get(n) == hashes[n] else "UPDATED"
        print(f"PAGE {n}: {hashes[n]}  {status}")


if __name__ == "__main__":
    main()
