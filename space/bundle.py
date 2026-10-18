"""space/bundle.py: spaces that travel with the repository.

A bundle is a folder under examples/spaces/<name>/ holding a space's event log as ndjson, its shared files and
knowledge folder, its run records with the parts of each run folder the page reads (the report, the proposals,
the map, the ideas), and the custom profile the runs used. Anyone who pulls the repository and starts the hub
gets the space installed into their lab folder on the first start (install_all, called by space/hub.py), as an
open room: every signed-in account on that PC can open it. A space that already exists in the lab is left alone.

    python -m space.bundle export <name>      write examples/spaces/<name>/ from the lab's space of that name
    python -m space.bundle install            install every bundle the lab does not have yet

Standard library only."""
from __future__ import annotations

import json
import os
import shutil
import sqlite3
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
BUNDLES = REPO / "examples" / "spaces"
RUN_PARTS = ("REPORT.md", "report.json", "answer.json", "problem.md", "problem_tree.json", "ideas.jsonl", "idea_clusters.json",
             "deepen.json", "live.json", "state.json", "selection.jsonl", "next_questions.json", "commitments.json")
RUN_DIRS = ("pool", "cands")                      # the proposals and the build records (cands/src is skipped)
SKIP_IN_CANDS = ("src",)


def _lab() -> Path:
    sys.path.insert(0, str(REPO))
    from harness.labroot import lab_root
    return lab_root()


def _copy_tree(src: Path, dst: Path, skip=()) -> None:
    if not src.exists():
        return
    for p in src.rglob("*"):
        rel = p.relative_to(src)
        if any(part in skip for part in rel.parts):
            continue
        q = dst / rel
        if p.is_dir():
            q.mkdir(parents=True, exist_ok=True)
        else:
            q.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, q)


# ---------------------------------------------------------------- export
def export(name: str, lab: Path | None = None) -> Path:
    from space.store import read_db, write_ndjson
    lab = lab or _lab()
    src = lab / "spaces" / name
    if not (src / "space.db").exists():
        raise SystemExit(f"no space named {name} in {lab / 'spaces'}")
    dest = BUNDLES / name
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    rows = read_db(src / "space.db")
    write_ndjson(dest / "events.ndjson", rows)
    _copy_tree(src / "files", dest / "files")
    _copy_tree(src / "knowledge", dest / "knowledge")
    # the run records, with each run folder's readable parts beside them
    recs = []
    try:
        recs = json.loads((src / "runs" / "runs.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        recs = []
    out_recs = []
    profiles = set()
    for r in recs if isinstance(recs, list) else []:
        rd = Path(r.get("run_dir") or "")
        rec = dict(r, pid=None, created=None)
        if rd.exists():
            tag = rd.name
            rec["run_dir"] = "run/" + tag                 # relative inside the bundle; install makes it absolute
            for part in RUN_PARTS:
                if (rd / part).exists():
                    (dest / "run" / tag).mkdir(parents=True, exist_ok=True)
                    shutil.copy2(rd / part, dest / "run" / tag / part)
            for d in RUN_DIRS:
                _copy_tree(rd / d, dest / "run" / tag / d, skip=SKIP_IN_CANDS)
        log = Path(r.get("log") or "")
        if log.exists():
            (dest / "runs").mkdir(exist_ok=True)
            shutil.copy2(log, dest / "runs" / log.name)
            rec["log"] = "runs/" + log.name
        if r.get("profile"):
            profiles.add(r["profile"])
        out_recs.append(rec)
    (dest / "runs").mkdir(exist_ok=True)
    (dest / "runs" / "runs.json").write_text(json.dumps(out_recs, indent=1), encoding="utf-8")
    for pf in sorted(profiles):
        p = REPO / "nano" / "profiles" / f"{pf}.py"
        if p.exists():
            (dest / "profiles").mkdir(exist_ok=True)
            shutil.copy2(p, dest / "profiles" / p.name)
    (dest / "README.md").write_text(
        f"# Bundled space: {name}\n\nInstalled into the lab folder by the hub on its first start (space/bundle.py). "
        f"events.ndjson is the space's log; files/ and knowledge/ are what people shared and what the team kept; "
        f"run/ holds the readable parts of each research run; profiles/ the problem the runs used.\n", encoding="utf-8")
    return dest


# ---------------------------------------------------------------- install
def install(name: str, lab: Path | None = None) -> Path | None:
    """Install one bundle into the lab if the lab has no space of that name. Returns the space folder, or None."""
    from space.store import BODY_KEYS, read_ndjson
    lab = lab or _lab()
    src = BUNDLES / name
    dst = lab / "spaces" / name
    if not (src / "events.ndjson").exists() or (dst / "space.db").exists():
        return None
    dst.mkdir(parents=True, exist_ok=True)
    # the log, with its seq numbers kept
    con = sqlite3.connect(str(dst / "space.db"))
    try:
        con.execute("CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, "
                    "by TEXT NOT NULL, by_kind TEXT NOT NULL, kind TEXT NOT NULL, subject TEXT, label TEXT, "
                    "base INTEGER, op TEXT, body TEXT NOT NULL, UNIQUE(by, op))")
        con.execute("CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT)")
        for ev in read_ndjson(src / "events.ndjson"):
            body = {k: ev[k] for k in BODY_KEYS if ev.get(k) is not None}
            body.setdefault("data", {})
            con.execute("INSERT OR IGNORE INTO events(seq,ts,by,by_kind,kind,subject,label,base,op,body) VALUES(?,?,?,?,?,?,?,?,?,?)",
                        (ev.get("seq"), ev.get("ts"), ev.get("by"), ev.get("by_kind"), ev.get("kind"), ev.get("subject"),
                         ev.get("label"), ev.get("base"), ev.get("op"), json.dumps(body, separators=(",", ":"), ensure_ascii=False)))
        con.commit()
    finally:
        con.close()
    _copy_tree(src / "files", dst / "files")
    _copy_tree(src / "knowledge", dst / "knowledge")
    # the runs: records point at folders under the lab's runs
    recs = []
    try:
        recs = json.loads((src / "runs" / "runs.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        recs = []
    out = []
    for r in recs if isinstance(recs, list) else []:
        rec = dict(r)
        rd = str(r.get("run_dir") or "")
        if rd.startswith("run/"):
            tag = rd[4:]
            target = lab / "runs" / tag
            _copy_tree(src / "run" / tag, target)
            rec["run_dir"] = str(target)
        lg = str(r.get("log") or "")
        if lg.startswith("runs/"):
            (dst / "runs").mkdir(exist_ok=True)
            if (src / lg).exists():
                shutil.copy2(src / lg, dst / "runs" / Path(lg).name)
            rec["log"] = str(dst / "runs" / Path(lg).name)
        out.append(rec)
    (dst / "runs").mkdir(exist_ok=True)
    (dst / "runs" / "runs.json").write_text(json.dumps(out, indent=1), encoding="utf-8")
    (dst / "bundle.json").write_text(json.dumps({"name": name, "from": "examples/spaces/" + name}), encoding="utf-8")
    for p in (src / "profiles").glob("*.py") if (src / "profiles").exists() else []:
        q = REPO / "nano" / "profiles" / p.name
        if not q.exists():
            shutil.copy2(p, q)
    return dst


def install_all(lab: Path | None = None) -> list[str]:
    """Every bundle the lab does not have yet. Never raises: a broken bundle is skipped."""
    done = []
    if not BUNDLES.exists():
        return done
    for d in sorted(BUNDLES.iterdir()):
        if d.is_dir() and (d / "events.ndjson").exists():
            try:
                if install(d.name, lab):
                    done.append(d.name)
            except Exception as e:  # noqa: BLE001
                print("bundle %s not installed: %s" % (d.name, str(e)[:200]), file=sys.stderr)
    return done


def main(argv=None) -> int:
    a = list(sys.argv[1:] if argv is None else argv)
    if a[:1] == ["export"] and len(a) == 2:
        print(export(a[1]))
        return 0
    if a[:1] == ["install"]:
        print("installed: %s" % (", ".join(install_all()) or "nothing new"))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
