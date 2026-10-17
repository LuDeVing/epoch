"""Static checks of the page shell (docs/MULTIPLAYER_DESIGN.md section 12.1 row P4). Standard library only.

    python space/web/tests/core/check_assets.py [WEB_DIR]

1. index.html has the mount ids topbar, tree-pane, clusters-pane, rail, strip.
2. Every script src and every font url starts with vendor/; stylesheets and module imports are local files.
3. No http:// or https:// in index.html or in any css file.
4. Every file in vendor/MANIFEST.json has its pinned size (and sha256 when pinned). d3.min.js is reported as
   pending when it is absent (the views part owns it); any other missing or mis-sized file fails.
5. No raw hex colour outside tokens.css (the files of section 6.6 plus every page module of this part).
6. The page files are ASCII only.
Exit 0 when every check passes, 1 otherwise.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

MOUNT_IDS = ("topbar", "tree-pane", "clusters-pane", "rail", "strip")
D3 = "d3.min.js"
D3_BYTES = 279706
HEX = re.compile(r"(?<![\w&])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b")
NO_HEX = ("cardstate.mjs", "tree.js", "clusters.js", "views.css", "base.css", "rail.js", "chat.js", "memory.js",
          "index.html", "app.js", "presence.js", "reduce.mjs", "connect.mjs", "store.mjs", "match.mjs", "layout.mjs",
          "motion.mjs")
ASCII_FILES = ("index.html", "app.js", "connect.mjs", "store.mjs", "reduce.mjs", "match.mjs", "rail.js", "chat.js",
               "memory.js", "presence.js", "tokens.css", "base.css")


class _Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []
        self.scripts: list[str] = []
        self.links: list[tuple[str, str]] = []
        self.inline: list[str] = []
        self._in_script = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.append(a["id"])
        if tag == "script":
            if a.get("src") is not None:
                self.scripts.append(a["src"])
            else:
                self._in_script = True
        if tag == "link":
            self.links.append((a.get("rel") or "", a.get("href") or ""))

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_script = False

    def handle_data(self, data):
        if self._in_script:
            self.inline.append(data)


def _local(ref: str) -> bool:
    return bool(ref) and not re.match(r"^[a-z][a-z0-9+.-]*:", ref, re.I) and not ref.startswith("//") and not ref.startswith("/")


def check(web: Path) -> tuple[list[str], list[str], list[str]]:
    ok: list[str] = []
    bad: list[str] = []
    pending: list[str] = []
    page_path = web / "index.html"
    html = page_path.read_text(encoding="utf-8")
    page = _Page()
    page.feed(html)
    missing = [i for i in MOUNT_IDS if i not in page.ids]
    (bad if missing else ok).append(f"index.html mount ids {'missing ' + ', '.join(missing) if missing else 'present'}")
    hexy = [i for i in page.ids if re.fullmatch(r"[0-9a-fA-F]{3,8}", i)]
    if hexy:
        bad.append(f"index.html has hex-looking ids: {hexy}")
    for src in page.scripts:
        (ok if src.startswith("vendor/") else bad).append(f"script src {src!r} {'starts with vendor/' if src.startswith('vendor/') else 'does not start with vendor/'}")
    for code in page.inline:
        for spec in re.findall(r"""import\s*(?:[^'"]*from\s*)?['"]([^'"]+)['"]""", code):
            good = spec.startswith("./") and _local(spec[2:]) and (web / spec[2:]).exists()
            (ok if good else bad).append(f"inline module import {spec!r} {'is a local file' if good else 'is not a local file of the page'}")
    for rel, href in page.links:
        if "stylesheet" in rel:
            (ok if _local(href) else bad).append(f"stylesheet {href!r} {'is local' if _local(href) else 'is not local'}")
    css_files = sorted(p for p in web.rglob("*.css") if "tests" not in p.relative_to(web).parts)
    for p in [page_path, *css_files]:
        text = p.read_text(encoding="utf-8")
        if re.search(r"https?://", text):
            bad.append(f"{p.relative_to(web)} contains http:// or https://")
    ok.append(f"no http:// or https:// checked in index.html and {len(css_files)} css files")
    for p in css_files:
        for url in re.findall(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)", p.read_text(encoding="utf-8")):
            if url.startswith("data:"):
                bad.append(f"{p.name} has a data: url")
            elif re.search(r"\.(woff2?|ttf|otf)$", url, re.I):
                (ok if url.startswith("vendor/") else bad).append(f"font url {url!r} in {p.name} {'starts with vendor/' if url.startswith('vendor/') else 'does not start with vendor/'}")
    # vendor manifest
    man_path = web / "vendor" / "MANIFEST.json"
    if not man_path.exists():
        bad.append("vendor/MANIFEST.json is missing")
    else:
        man = json.loads(man_path.read_text(encoding="utf-8"))
        listed = set()
        for f in man.get("files", []):
            name = f["file"]
            listed.add(name)
            p = web / "vendor" / name
            want = D3_BYTES if name == D3 else f["bytes"]
            if name == D3 and f["bytes"] != D3_BYTES:
                bad.append(f"MANIFEST pins d3.min.js at {f['bytes']} bytes, the design says {D3_BYTES}")
            if not p.exists():
                (pending if name == D3 else bad).append(f"vendor/{name} {'pending (owned by the views part)' if name == D3 else 'missing'}")
                continue
            size = p.stat().st_size
            if size != want:
                bad.append(f"vendor/{name} is {size} bytes, pinned {want}")
                continue
            if f.get("sha256"):
                digest = hashlib.sha256(p.read_bytes()).hexdigest()
                if digest != f["sha256"]:
                    bad.append(f"vendor/{name} sha256 {digest} differs from the pin")
                    continue
            ok.append(f"vendor/{name} {size} bytes as pinned")
        for p in sorted((web / "vendor").iterdir()):
            if p.name != "MANIFEST.json" and p.name not in listed and p.is_file():
                bad.append(f"vendor/{p.name} is not listed in MANIFEST.json")
        for src in page.scripts:
            if src.startswith("vendor/") and src[len("vendor/"):] not in listed:
                bad.append(f"script {src} is not listed in MANIFEST.json")
    # hex colours
    hex_hits = []
    for name in NO_HEX:
        p = web / name
        if p.exists():
            for n, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
                for m in HEX.finditer(line):
                    hex_hits.append(f"{name}:{n}: {m.group(0)}")
    if hex_hits:
        bad.append("raw hex colours outside tokens.css: " + "; ".join(hex_hits[:10]))
    else:
        ok.append("no raw hex colour outside tokens.css")
    if not HEX.search((web / "tokens.css").read_text(encoding="utf-8")):
        bad.append("tokens.css carries no colour")
    # ASCII
    for name in ASCII_FILES:
        p = web / name
        if p.exists():
            raw = p.read_bytes()
            if any(b > 127 for b in raw):
                bad.append(f"{name} is not ASCII only")
    ok.append("page files are ASCII only" if not any("ASCII" in b for b in bad) else "")
    return [o for o in ok if o], bad, pending


def main(argv: list[str]) -> int:
    web = Path(argv[1]).resolve() if len(argv) > 1 else Path(__file__).resolve().parents[2]
    ok, bad, pending = check(web)
    for line in ok:
        print("ok      ", line)
    for line in pending:
        print("pending ", line)
    for line in bad:
        print("FAIL    ", line)
    print(f"{len(ok)} ok, {len(pending)} pending, {len(bad)} failed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
