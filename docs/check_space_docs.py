"""The docs check of the shared research space (docs/MULTIPLAYER_DESIGN.md section 12.3).

    python docs/check_space_docs.py          prints one line per check and exits 1 when any fails

Checks:
1. every route string in docs/SPACE.md and docs/MULTIPLAYER_DESIGN.md appears in space/server.py (or in
   space/launch.py, whose /api/run/* routes the server registers), and every route in contract.ROUTES and every
   /api/run/* route of space/launch.py appears in docs/SPACE.md (the ROUTES also in the design doc);
2. every kind in the kinds table of docs/SPACE.md is in contract.KINDS and every KINDS entry is in that table;
3. every kind that nano/space.py, space/bridge.py and space/actions.py emit (emit( and _ev( calls with a literal
   first argument) is in KINDS;
4. space/web/contract.json equals contract.export();
5. the docs are ASCII only, with no em-dash or en-dash;
6. every relative link in the docs resolves;
7. every control.json key in CONTROL_KEYS appears in nano/loop.py inside _stage, _pick_question or _opinions_for;
8. the person-agent action names in docs/SPACE.md match actions.ACTIONS, and every slash command is documented;
9. docs/DEMO_RUNBOOK.md names every beat of section 13.3 with its time.
Standard library only. Every check is a function that returns a list of problems, so the tests can feed it text.
"""
from __future__ import annotations

import ast
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

DOCS = REPO / "docs"
SPACE_MD = DOCS / "SPACE.md"
PITCH_MD = DOCS / "SPACE_PITCH.md"
RUNBOOK_MD = DOCS / "DEMO_RUNBOOK.md"
DESIGN_MD = DOCS / "MULTIPLAYER_DESIGN.md"
OWN_DOCS = (SPACE_MD, PITCH_MD, RUNBOOK_MD)
ASCII_DOCS = OWN_DOCS + (DESIGN_MD,)
ROUTE_RE = re.compile(r"/api/[a-z_]+(?:/[a-z_]+)*")
EMIT_RE = re.compile(r"\b(?:emit|_ev)\(\s*[\"']([A-Za-z_]+)[\"']")
KIND_ROW_RE = re.compile(r"^\|\s*`([a-z_]+)`\s*\|")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TIME_RE = re.compile(r"^\d:\d\d$")
KINDS_HEADING = "## Every kind"
ACTIONS_HEADING = "## The person-agent's actions"
LOOP_FUNCS = ("_stage", "_pick_question", "_opinions_for")


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8")


def section(text: str, heading: str) -> str:
    """The text under a markdown heading, up to the next heading of the same or a higher level."""
    lines = text.splitlines()
    level = len(heading) - len(heading.lstrip("#"))
    out, inside = [], False
    for line in lines:
        if line.strip() == heading:
            inside = True
            continue
        if inside and line.startswith("#"):
            lv = len(line) - len(line.lstrip("#"))
            if lv <= level:
                break
        if inside:
            out.append(line)
    return "\n".join(out)


# ---------------------------------------------------------------- 1 routes
def launch_routes(launch_src: str) -> set[str]:
    return set(re.findall(r"\(\"(?:GET|POST)\",\s*\"(/api/run/[a-z_]+)\"\)", launch_src))


def check_routes(space_md: str, design_md: str, server_src: str, launch_src: str, routes: dict) -> list[str]:
    bad = []
    code = server_src + "\n" + launch_src + "\n" + read(Path(__file__).resolve().parent.parent / "space" / "people.py")
    for name, text in (("docs/SPACE.md", space_md), ("docs/MULTIPLAYER_DESIGN.md", design_md)):
        for r in sorted(set(ROUTE_RE.findall(text))):
            if r not in code:
                bad.append(f"{name} names route {r}, which is not in space/server.py or space/launch.py")
    for key, (_method, path) in routes.items():
        if path == "/":
            continue
        for name, text in (("docs/SPACE.md", space_md), ("docs/MULTIPLAYER_DESIGN.md", design_md)):
            if path not in set(ROUTE_RE.findall(text)):
                bad.append(f"contract.ROUTES[{key}] {path} is missing from {name}")
    for path in sorted(launch_routes(launch_src)):
        if path not in set(ROUTE_RE.findall(space_md)):
            bad.append(f"the start-run route {path} (space/launch.py) is missing from docs/SPACE.md")
    return bad


# ---------------------------------------------------------------- 2 and 3 kinds
def doc_kinds(space_md: str) -> list[str]:
    return [m.group(1) for line in section(space_md, KINDS_HEADING).splitlines() if (m := KIND_ROW_RE.match(line))]


def check_kinds(space_md: str, kinds: dict) -> list[str]:
    listed = doc_kinds(space_md)
    if not listed:
        return [f"docs/SPACE.md has no kinds table under '{KINDS_HEADING}'"]
    bad = [f"docs/SPACE.md lists kind {k}, which is not in contract.KINDS" for k in listed if k not in kinds]
    bad += [f"contract.KINDS has {k}, which docs/SPACE.md does not list" for k in kinds if k not in listed]
    dup = sorted({k for k in listed if listed.count(k) > 1})
    if dup:
        bad.append("docs/SPACE.md lists these kinds twice: " + ", ".join(dup))
    return bad


def emitted_kinds(src: str) -> set[str]:
    return set(EMIT_RE.findall(src))


def check_emits(sources: dict, kinds: dict) -> list[str]:
    bad = []
    for name, src in sources.items():
        for k in sorted(emitted_kinds(src)):
            if k not in kinds:
                bad.append(f"{name} emits {k}, which is not in contract.KINDS")
    return bad


# ---------------------------------------------------------------- 4 contract.json
def check_contract_json(text: str, export: dict) -> list[str]:
    try:
        got = json.loads(text)
    except ValueError as e:
        return [f"space/web/contract.json is not JSON: {e}"]
    want = json.loads(json.dumps(export, sort_keys=True))
    return [] if got == want else ["space/web/contract.json differs from contract.export(): run "
                                   "python -m space.contract > space/web/contract.json"]


# ---------------------------------------------------------------- 5 ASCII, 6 links
def check_ascii(name: str, text: str) -> list[str]:
    bad = []
    for i, line in enumerate(text.splitlines(), 1):
        for ch in line:
            if ch in "\u2014\u2013":
                bad.append(f"{name}:{i} has an {'em' if ch == chr(0x2014) else 'en'}-dash")
                break
            if ord(ch) > 127:
                bad.append(f"{name}:{i} has a non-ASCII character U+{ord(ch):04X}")
                break
    return bad


def check_links(name: str, text: str, base: Path) -> list[str]:
    bad = []
    for target in LINK_RE.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        if path and not (base / path).exists():
            bad.append(f"{name} links to {target}, which does not exist")
    return bad


# ---------------------------------------------------------------- 7 control keys in the loop
def loop_function_text(loop_src: str, names=LOOP_FUNCS) -> str:
    tree = ast.parse(loop_src)
    parts = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names:
            parts.append(ast.get_source_segment(loop_src, node) or "")
    return "\n".join(parts)


def check_control_keys(loop_src: str, keys) -> list[str]:
    body = loop_function_text(loop_src)
    if not body:
        return ["nano/loop.py has none of " + ", ".join(LOOP_FUNCS)]
    return [f"control key {k} does not appear in nano/loop.py {'/'.join(LOOP_FUNCS)}"
            for k in keys if not re.search(r"\b%s\b" % re.escape(k), body)]


# ---------------------------------------------------------------- 8 actions and slash commands
def doc_actions(space_md: str) -> list[str]:
    return [m.group(1) for line in section(space_md, ACTIONS_HEADING).splitlines() if (m := KIND_ROW_RE.match(line))]


def check_actions(space_md: str, actions: list, slash) -> list[str]:
    listed = doc_actions(space_md)
    want = [a[0] for a in actions]
    bad = []
    if listed != want:
        bad.append(f"docs/SPACE.md actions {listed} do not match actions.ACTIONS {want}")
    for s in slash:
        if not re.search(r"`/%s\b" % re.escape(s), space_md):
            bad.append(f"docs/SPACE.md does not document the slash command /{s}")
    return bad


# ---------------------------------------------------------------- 9 the runbook names every beat with its time
def design_beats(design_md: str) -> list[tuple[str, str]]:
    """(time, does) for every row of the run-of-show table in section 13.3."""
    out = []
    for line in section(design_md, "### 13.3 Run of show, 4:00 (every beat is a slash command or a Go; no beat waits "
                                   "on a model)").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and TIME_RE.match(cells[0]):
            out.append((cells[0], cells[2]))
    return out


def beat_tokens(does: str) -> list[str]:
    """The words a runbook row must carry for one beat: each slash command and each Go (stage rN)."""
    toks = re.findall(r"`?(/[a-z]+)\b", does)
    toks += [f"Go ({m.group(1)} r{m.group(2)})" for m in re.finditer(r"Go \((\w+) r(\d)\)", does)]
    return toks


def check_runbook(runbook_md: str, beats: list[tuple[str, str]]) -> list[str]:
    if not beats:
        return ["section 13.3 of docs/MULTIPLAYER_DESIGN.md has no beats (the heading changed?)"]
    rows = {}
    for line in runbook_md.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if line.lstrip().startswith("|") and cells and TIME_RE.match(cells[0]):
            rows.setdefault(cells[0], []).append(line)
    bad = []
    for t, does in beats:
        if t not in rows:
            bad.append(f"docs/DEMO_RUNBOOK.md has no run-of-show row for the beat at {t} ({does[:50]})")
            continue
        text = "\n".join(rows[t])
        for tok in beat_tokens(does):
            if tok not in text:
                bad.append(f"docs/DEMO_RUNBOOK.md row {t} does not name {tok}")
    return bad


# ---------------------------------------------------------------- all
def run_all() -> dict[str, list[str]]:
    from space import actions as A
    from space import contract as C
    space_md, design_md = read(SPACE_MD) if SPACE_MD.exists() else "", read(DESIGN_MD)
    res = {}
    missing = [str(p.relative_to(REPO)) for p in OWN_DOCS if not p.exists()]
    res["docs exist"] = [f"{m} is missing" for m in missing]
    res["routes"] = check_routes(space_md, design_md, read(REPO / "space" / "server.py"),
                                 read(REPO / "space" / "launch.py"), C.ROUTES)
    res["kinds"] = check_kinds(space_md, C.KINDS)
    srcs = {p: read(REPO / p) for p in ("nano/space.py", "space/bridge.py", "space/actions.py") if (REPO / p).exists()}
    res["emitted kinds"] = check_emits(srcs, C.KINDS)
    res["contract.json"] = check_contract_json(read(REPO / "space" / "web" / "contract.json"), C.export())
    res["ascii"] = [x for p in ASCII_DOCS if p.exists() for x in check_ascii(str(p.relative_to(REPO)), read(p))]
    res["links"] = [x for p in ASCII_DOCS if p.exists() for x in check_links(str(p.relative_to(REPO)), read(p), p.parent)]
    res["control keys"] = check_control_keys(read(REPO / "nano" / "loop.py"), C.CONTROL_KEYS)
    res["actions"] = check_actions(space_md, A.ACTIONS, C.SLASH)
    res["runbook beats"] = check_runbook(read(RUNBOOK_MD) if RUNBOOK_MD.exists() else "", design_beats(design_md))
    return res


def main() -> int:
    res = run_all()
    for name, bad in res.items():
        print(("ok    " if not bad else "FAIL  ") + name)
        for b in bad:
            print("      " + b)
    failed = [n for n, b in res.items() if b]
    print("docs check: " + ("all passed" if not failed else "FAILED: " + ", ".join(failed)))
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
