from __future__ import annotations

import hashlib
import json
from datetime import datetime
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / "input"
CONFIG_PATH = ROOT / "config" / "sources.json"
MANIFEST_PATH = ROOT / "data" / "manifest.json"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def pdf_info(path: Path) -> tuple[int, bool]:
    reader = PdfReader(str(path))
    sample = ""
    for page in reader.pages[: min(3, len(reader.pages))]:
        sample += page.extract_text() or ""
    return len(reader.pages), bool(sample.strip())


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    config = load_json(CONFIG_PATH, {})
    previous = load_json(MANIFEST_PATH, {"version": 1, "documents": {}})
    previous_docs = previous.get("documents", {})
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    documents = {}

    for path in sorted(INPUT_DIR.glob("*.pdf"), key=lambda p: p.name):
        digest = sha256(path)
        old = previous_docs.get(path.name, {})
        pages, has_text_layer = pdf_info(path)
        changed = bool(old) and old.get("sha256") != digest
        source_config = config.get(path.name, {})
        processed_pages = [] if changed else source_config.get(
            "processed_pages", old.get("processed_pages", [])
        )
        if changed:
            status = "changed"
        elif len(processed_pages) >= pages:
            status = "processed"
        elif processed_pages:
            status = "partial"
        else:
            status = old.get("status", "registered")
        documents[path.name] = {
            "subject": source_config.get("subject", "未分类"),
            "course": source_config.get("course", path.stem),
            "pages": pages,
            "size_mb": round(path.stat().st_size / 1024 / 1024, 2),
            "sha256": digest,
            "has_text_layer": has_text_layer,
            "status": status,
            "processed_pages": processed_pages,
            "first_seen": old.get("first_seen", now),
            "last_seen": now,
        }

    for name, old in previous_docs.items():
        if name not in documents:
            documents[name] = {**old, "status": "missing", "last_seen": now}

    payload = {"version": 1, "updated_at": now, "documents": documents}
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"已登记 {len(documents)} 份 PDF：")
    for name, doc in documents.items():
        layer = "含文本层" if doc.get("has_text_layer") else "扫描页"
        print(f"- {name}: {doc['pages']} 页, {layer}, 状态={doc['status']}")


if __name__ == "__main__":
    main()
