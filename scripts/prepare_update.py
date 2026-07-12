from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "config" / "sources.json"
MANIFEST_PATH = ROOT / "data" / "manifest.json"
TMP_DIR = ROOT / "tmp" / "pdfs"
PUBLIC_DIR = ROOT / "public" / "note-pages"
PLAN_PATH = ROOT / "tmp" / "update-plan.md"


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"\.pdf$", "", value)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "note"


def poppler_exe(name: str) -> str:
    bundled = (
        Path.home()
        / ".cache"
        / "codex-runtimes"
        / "codex-primary-runtime"
        / "dependencies"
        / "native"
        / "poppler"
        / "Library"
        / "bin"
        / f"{name}.exe"
    )
    if bundled.exists():
        return str(bundled)
    found = shutil.which(name)
    if found:
        return found
    raise RuntimeError(f"Cannot find {name}. Install Poppler or use the Codex bundled runtime.")


def render_page(pdf_path: Path, page: int, slug: str) -> Path:
    out_dir = TMP_DIR / slug
    out_dir.mkdir(parents=True, exist_ok=True)
    prefix = out_dir / f"render-{page:02d}"
    cmd = [
        poppler_exe("pdftoppm"),
        "-png",
        "-r",
        "180",
        "-f",
        str(page),
        "-l",
        str(page),
        str(pdf_path),
        str(prefix),
    ]
    subprocess.run(cmd, check=True)
    candidates = sorted(out_dir.glob(f"render-{page:02d}-*.png"))
    if not candidates:
        raise RuntimeError(f"Rendered page missing: {pdf_path.name} page {page}")
    target = out_dir / f"page-{page:02d}.png"
    candidates[-1].replace(target)
    return target


def make_public_webp(source: Path, slug: str, page: int) -> Path | None:
    if source.stat().st_size < 100_000:
        return None
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    target = PUBLIC_DIR / f"{slug}-p{page:02d}.webp"
    image = Image.open(source).convert("RGB")
    image.save(target, "WEBP", quality=82, method=6)
    return target


def main() -> None:
    config = load_json(CONFIG_PATH, {})
    manifest = load_json(MANIFEST_PATH, {"documents": {}})
    documents = manifest.get("documents", {})
    lines = [
        "# 更新计划",
        "",
        "只把 `needs_transcription` 的页面交给 GPT 视觉识别；`processed` 页面不要重复处理。",
        "",
    ]

    for name, doc in sorted(documents.items()):
        if doc.get("status") == "missing":
            continue
        source = ROOT / "input" / name
        if not source.exists():
            continue
        cfg = config.get(name, {})
        slug = cfg.get("slug") or slugify(cfg.get("course") or name)
        total_pages = int(doc.get("pages", 0))
        processed = set(int(p) for p in doc.get("processed_pages", []))
        changed = doc.get("status") == "changed"
        todo = list(range(1, total_pages + 1)) if changed else [
            p for p in range(1, total_pages + 1) if p not in processed
        ]

        lines.append(f"## {name}")
        lines.append("")
        lines.append(f"- slug: `{slug}`")
        lines.append(f"- status: `{doc.get('status')}`")
        lines.append(f"- pages: {total_pages}")
        lines.append(f"- processed_pages: {sorted(processed)}")
        lines.append(f"- needs_transcription: {todo}")
        lines.append("")

        for page in todo:
            png = render_page(source, page, slug)
            webp = make_public_webp(png, slug, page)
            lines.append(f"- page {page}: `{png.relative_to(ROOT)}`")
            if webp:
                lines.append(f"  public: `/{webp.relative_to(ROOT / 'public').as_posix()}`")
            else:
                lines.append("  public: skipped, likely blank or cover-light page")
        lines.append("")

    PLAN_PATH.parent.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Update plan written: {PLAN_PATH}")


if __name__ == "__main__":
    main()
