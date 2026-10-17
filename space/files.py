"""Files people share with the team: stored under <space folder>/files/, served back by id, and the readable part
(the first characters of a text file) travels with the finding so the agents can quote it. Standard library only."""
from __future__ import annotations

import json
import os
import re
import secrets
import threading
from pathlib import Path

from space.store import Reject

MAX_BYTES = 8 * 1024 * 1024
EXCERPT_CHARS = 3000
TEXT_SUFFIXES = {".txt", ".md", ".csv", ".tsv", ".json", ".jsonl", ".log", ".py", ".yaml", ".yml", ".toml", ".ini",
                 ".tex", ".bib", ".html", ".xml", ".rst", ".sql", ".r", ".jl", ".m", ".c", ".h", ".js", ".ts"}
BINARY_SUFFIXES = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".webp", ".xlsx", ".docx", ".pptx", ".zip", ".npy", ".npz", ".pt", ".pkl"}
KIND_OF = {".csv": "data", ".tsv": "data", ".json": "data", ".jsonl": "data", ".npy": "data", ".npz": "data", ".xlsx": "data",
           ".pdf": "paper", ".tex": "paper", ".bib": "paper", ".docx": "paper", ".md": "note", ".txt": "note", ".log": "measurement"}
MIME = {".txt": "text/plain", ".md": "text/markdown", ".csv": "text/csv", ".json": "application/json", ".pdf": "application/pdf",
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".html": "text/html", ".py": "text/x-python"}
_LOCK = threading.Lock()
_ID_RE = re.compile(r"^[A-Za-z0-9_-]{8,24}$")


def safe_name(raw: str) -> str:
    n = re.sub(r"[^A-Za-z0-9._ -]+", "_", str(raw or "file").strip()).strip("._ ") or "file"
    return n[:80]


class Files:
    def __init__(self, space_dir: Path):
        self.dir = Path(space_dir) / "files"

    def _index_path(self) -> Path:
        return self.dir / "index.json"

    def _index(self) -> dict:
        try:
            d = json.loads(self._index_path().read_text(encoding="utf-8"))
            return d if isinstance(d, dict) else {}
        except (OSError, ValueError):
            return {}

    def _save_index(self, d: dict) -> None:
        tmp = self._index_path().with_suffix(".tmp")
        tmp.write_text(json.dumps(d, indent=1), encoding="utf-8")
        os.replace(tmp, self._index_path())

    def save(self, name: str, data: bytes, by: str, content_type: str = "") -> dict:
        if not data:
            raise Reject(422, "empty_file")
        if len(data) > MAX_BYTES:
            raise Reject(413, "too_big", limit=MAX_BYTES)
        name = safe_name(name)
        suffix = Path(name).suffix.lower()
        if suffix not in TEXT_SUFFIXES and suffix not in BINARY_SUFFIXES:
            raise Reject(415, "bad_type", hint="text, csv, json, markdown, pdf, images and office files only")
        fid = secrets.token_urlsafe(9).replace("-", "a").replace("_", "b")
        self.dir.mkdir(parents=True, exist_ok=True)
        path = self.dir / f"{fid}-{name}"
        path.write_bytes(data)
        excerpt, lines = "", None
        if suffix in TEXT_SUFFIXES:
            text = data.decode("utf-8", "replace")
            lines = text.count("\n") + (1 if text and not text.endswith("\n") else 0)
            excerpt = text[:EXCERPT_CHARS]
        rec = {"id": fid, "name": name, "bytes": len(data), "type": content_type or MIME.get(suffix, "application/octet-stream"),
               "kind": KIND_OF.get(suffix, "data" if suffix in BINARY_SUFFIXES else "note"), "by": by, "path": str(path),
               "excerpt": excerpt, "lines": lines, "text": suffix in TEXT_SUFFIXES}
        with _LOCK:
            idx = self._index()
            idx[fid] = {k: v for k, v in rec.items() if k != "excerpt"}
            self._save_index(idx)
        return rec

    def get(self, fid: str) -> tuple[dict, bytes]:
        if not _ID_RE.match(str(fid or "")):
            raise Reject(404, "no_file")
        rec = self._index().get(fid)
        if not rec:
            raise Reject(404, "no_file")
        try:
            return rec, Path(rec["path"]).read_bytes()
        except OSError:
            raise Reject(404, "no_file")

    def path_of(self, fid: str) -> str | None:
        rec = self._index().get(str(fid or ""))
        return rec.get("path") if rec else None
