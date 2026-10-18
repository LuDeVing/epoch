"""The knowledge folder of a space: what is known, as Markdown files people and agents can open.

<space folder>/knowledge/
  README.md            the index
  problem.md           the problem as described (title, goal, situation, criteria, limits, parts, scope)
  facts.md             every fact, numbered, with its source: from the description and from what people shared
  questions.md         the open questions, and the questions the team picked round by round
  results.md           every candidate built and how its test went
  findings/<n>-<slug>.md   one file per thing a person shared (its note, its file, the readable start of it)
  parts/<part>.md      per part of the problem: frame, facts, findings, results, what the team remembers

problem.md and facts.md are written when a described problem is used; the rest is rebuilt from the event log
when the page asks (GET /api/knowledge) or a run starts. The generated profile points the researchers' "docs" idea
card at facts.md, so the team reads the same file. Standard library only."""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path

_SLUG = re.compile(r"[^a-z0-9]+")


def slug(text: str, n: int = 40) -> str:
    return (_SLUG.sub("-", str(text or "").lower()).strip("-")[:n]) or "item"


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _now() -> str:
    return time.strftime("%Y-%m-%d %H:%M")


class Knowledge:
    def __init__(self, space_dir):
        self.dir = Path(space_dir) / "knowledge"
        self.space_dir = Path(space_dir)

    # ---------------------------------------------------------------- the described problem
    def write_problem(self, spec: dict) -> dict:
        """problem.json, problem.md, facts.md and questions.md from the wizard's spec. Returns the file paths."""
        self.dir.mkdir(parents=True, exist_ok=True)
        _write(self.dir / "problem.json", json.dumps(spec, indent=1, ensure_ascii=False))
        title = str(spec.get("title") or "the problem").strip()
        L = [f"# {title}", "", f"_Described on {_now()}._", "", "## Goal", "", str(spec.get("goal") or "").strip(), ""]
        if spec.get("context"):
            L += ["## Situation", "", str(spec["context"]).strip(), ""]
        crit = spec.get("criteria") or []
        if crit:
            L += ["## What a good answer looks like", ""]
            for c in crit:
                if isinstance(c, dict) and c.get("name"):
                    L.append(f"- **{c['name']}**: {c.get('how') or ''}".rstrip(": "))
            L.append("")
        lim = spec.get("limits") or []
        if lim:
            L += ["## Limits", ""] + [f"- {l.get('text') if isinstance(l, dict) else l}" for l in lim] + [""]
        parts = spec.get("partsList") or []
        if parts:
            L += ["## Parts", ""] + [f"- {p.get('name') if isinstance(p, dict) else p}" for p in parts] + [""]
        if spec.get("field") or spec.get("scope"):
            L += ["## Field and scope", ""]
            if spec.get("field"):
                L.append(f"- Field: {spec['field']}")
            if spec.get("scope"):
                L.append(f"- Scope: {spec['scope']}")
            L.append("")
        mat = spec.get("material") or []
        if mat:
            L += ["## Material shared with the team", ""] + [f"- {m.get('name') if isinstance(m, dict) else m}" for m in mat] + [""]
        _write(self.dir / "problem.md", "\n".join(L))
        self._write_facts(spec)
        self._write_questions(spec, [])
        return {"problem": str(self.dir / "problem.md"), "facts": str(self.dir / "facts.md")}

    def _write_facts(self, spec: dict, findings: list | None = None) -> None:
        L = ["# Facts", "", "Numbered so a proposal can cite them, like [F3]. Each one names where it came from.", ""]
        n = 0
        for f in spec.get("facts") or []:
            if not isinstance(f, dict) or not f.get("text"):
                continue
            n += 1
            L.append(f"- **[F{n}]** {f['text'].strip()}" + (f"  \n  _source: {f['source'].strip()}_" if f.get("source") else ""))
        if findings:
            L += ["", "## Shared by people during the research", ""]
            for fd in findings:
                n += 1
                d = fd.get("data") or {}
                fl = d.get("file") if isinstance(d.get("file"), dict) else None
                line = f"- **[F{n}]** {d.get('title') or ''}: {' '.join(str(d.get('text') or '').split())[:400]}".rstrip(": ")
                line += f"  \n  _by {fd.get('owner') or fd.get('by')}, {str(fd.get('ts') or '')[:16]}" + (f", file {fl.get('name')}" if fl else "") + "_"
                L.append(line)
        if n == 0:
            L.append("_Nothing yet. Share files or notes in the Findings tab and they appear here._")
        _write(self.dir / "facts.md", "\n".join(L) + "\n")

    def _write_questions(self, spec: dict, picks: list) -> None:
        L = ["# Questions", ""]
        oq = spec.get("open_questions") or []
        if oq:
            L += ["## Open from the start", ""] + [f"- {q}" for q in oq] + [""]
        if picks:
            L += ["## What the team asked, round by round", ""]
            for p in picks:
                d = p.get("data") or {}
                chosen = d.get("chosen")
                text = chosen.get("text") if isinstance(chosen, dict) else next((t.get("text") for t in (d.get("top3") or []) if isinstance(t, dict) and t.get("id") == chosen), chosen)
                L.append(f"- Round {d.get('round')}: {text}" + (f" _(chosen by {d.get('by')})_" if d.get("by") else ""))
            L.append("")
        if len(L) == 2:
            L.append("_None yet._")
        _write(self.dir / "questions.md", "\n".join(L) + "\n")

    # ---------------------------------------------------------------- from the event log
    def rebuild(self, events: list) -> dict:
        """findings/, results.md, parts/, questions.md and README.md from the log; facts.md gains the shared facts."""
        spec = {}
        try:
            spec = json.loads((self.dir / "problem.json").read_text(encoding="utf-8"))
        except (OSError, ValueError):
            pass
        nodes, findings, results, picks, memory = {}, [], {}, [], {}
        cands = {}
        for ev in events:
            k = ev.get("kind")
            d = ev.get("data") if isinstance(ev.get("data"), dict) else {}
            if k == "node_added" and d.get("id"):
                nodes.setdefault(d["id"], {"id": d["id"], "name": d.get("name") or d["id"], "frame": d.get("frame") or "",
                                           "parent": d.get("parent"), "by": ev.get("owner") or ev.get("by")})
            elif k == "finding_posted":
                findings.append(ev)
            elif k == "candidate_built":
                cands[d.get("cand")] = {"cand": d.get("cand"), "name": d.get("cluster_name") or d.get("idea") or d.get("cand"), "node": d.get("node"),
                                       "hypothesis": d.get("hypothesis") or "", "round": d.get("round"), "status": "built", "metrics": {}, "reason": ""}
            elif k == "test_result":
                c = cands.setdefault(d.get("cand"), {"cand": d.get("cand"), "name": d.get("idea") or d.get("cand"), "node": d.get("node"), "hypothesis": "", "round": None, "status": "", "metrics": {}, "reason": ""})
                c.update({"status": d.get("status") or c["status"], "metrics": d.get("metrics") or {}, "reason": d.get("reason") or "", "rung": d.get("rung")})
            elif k == "question_picked":
                picks.append(ev)
            elif k == "memory_added":
                memory.setdefault(d.get("node"), []).extend([a for a in (d.get("added") or []) if isinstance(a, dict)])
        name_of = lambda nid: (nodes.get(nid) or {}).get("name") or (nid or "the whole problem")   # noqa: E731
        self.dir.mkdir(parents=True, exist_ok=True)
        # facts and questions
        self._write_facts(spec, findings)
        self._write_questions(spec, picks)
        # one file per finding
        fdir = self.dir / "findings"
        for ev in findings:
            d = ev.get("data") or {}
            fl = d.get("file") if isinstance(d.get("file"), dict) else None
            L = [f"# {d.get('title') or 'finding'}", "", f"_Shared by {ev.get('owner') or ev.get('by')} on {str(ev.get('ts') or '')[:16]}; part: {name_of(d.get('part'))}; kind: {d.get('kind') or 'note'}; source: {d.get('source') or 'own work'}._", ""]
            if d.get("text") and d.get("text") != d.get("title"):
                L += [str(d["text"]).strip(), ""]
            if d.get("values"):
                L += ["## Numbers", ""] + [f"- {k} = {v}" for k, v in d["values"].items()] + [""]
            if fl:
                L += ["## File", "", f"- {fl.get('name')} ({fl.get('bytes')} bytes" + (f", {fl.get('lines')} lines" if fl.get("lines") else "") + f"), kept as files/{fl.get('id')}-{fl.get('name')}", ""]
            if d.get("excerpt"):
                L += ["## Readable start of the file", "", "```", str(d["excerpt"])[:3000], "```", ""]
            if d.get("replaces"):
                L += [f"_Replaces finding {d['replaces']}._", ""]
            _write(fdir / f"{ev.get('seq')}-{slug(d.get('title'))}.md", "\n".join(L))
        # results
        L = ["# Results", "", "| candidate | part | round | outcome | numbers | reason |", "|---|---|---|---|---|---|"]
        rows = sorted(cands.values(), key=lambda c: (c.get("round") or 0, str(c.get("cand"))))
        for c in rows:
            m = ", ".join(f"{k} {round(v, 4) if isinstance(v, float) else v}" for k, v in (c.get("metrics") or {}).items() if isinstance(v, (int, float)))
            L.append(f"| {c.get('name')} | {name_of(c.get('node'))} | {c.get('round') or ''} | {c.get('status') or 'built'} | {m} | {str(c.get('reason') or '').replace('|', '/')[:160]} |")
        if not rows:
            L.append("| _nothing built yet_ | | | | | |")
        best = [c for c in rows if c.get("status") in ("win", "preferred")]
        if best:
            L += ["", "## Best so far", ""] + [f"- **{c['name']}** on {name_of(c.get('node'))}: {c['status']}" + (f". {c['reason']}" if c.get("reason") else "") for c in best[-3:]]
        _write(self.dir / "results.md", "\n".join(L) + "\n")
        # per part
        pdir = self.dir / "parts"
        for nid, n in nodes.items():
            L = [f"# {n['name']}", "", (n.get("frame") or "").strip(), ""]
            fs = [ev for ev in findings if (ev.get("data") or {}).get("part") == nid]
            if fs:
                L += ["## Shared by people", ""] + [f"- {(ev.get('data') or {}).get('title')} (findings/{ev.get('seq')}-{slug((ev.get('data') or {}).get('title'))}.md)" for ev in fs] + [""]
            rs = [c for c in rows if c.get("node") == nid]
            if rs:
                L += ["## Results", ""] + [f"- {c['name']}: {c.get('status') or 'built'}" + (f" ({c['reason'][:120]})" if c.get("reason") else "") for c in rs] + [""]
            ms = memory.get(nid) or []
            if ms:
                L += ["## What the team remembers", ""] + [f"- {a.get('text')}" + (f" _({a.get('section')})_" if a.get("section") else "") for a in ms[-30:]] + [""]
            _write(pdir / f"{slug(nid, 32)}.md", "\n".join(L))
        # index
        L = [f"# Knowledge: {spec.get('title') or self.space_dir.name}", "", f"_Rebuilt {_now()}. Every file here is plain Markdown; the team's researchers read facts.md too._", "",
             "- [problem.md](problem.md): the problem as described", "- [facts.md](facts.md): every fact with its source, numbered for citing",
             "- [questions.md](questions.md): open questions and what the team asked", "- [results.md](results.md): what was built and how it tested", ""]
        if findings:
            L += ["## Findings", ""] + [f"- [{(ev.get('data') or {}).get('title')}](findings/{ev.get('seq')}-{slug((ev.get('data') or {}).get('title'))}.md) by {ev.get('owner') or ev.get('by')}" for ev in findings] + [""]
        if nodes:
            L += ["## Parts", ""] + [f"- [{n['name']}](parts/{slug(nid, 32)}.md)" for nid, n in nodes.items()] + [""]
        _write(self.dir / "README.md", "\n".join(L))
        return {"dir": str(self.dir), "files": self.listing()}

    # ---------------------------------------------------------------- reading
    def listing(self) -> list[dict]:
        out = []
        if not self.dir.exists():
            return out
        for p in sorted(self.dir.rglob("*.md")):
            rel = p.relative_to(self.dir).as_posix()
            try:
                first = p.read_text(encoding="utf-8", errors="replace").splitlines()[0].lstrip("# ").strip() if p.stat().st_size else rel
                out.append({"path": rel, "title": first or rel, "bytes": p.stat().st_size, "updated": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime(p.stat().st_mtime))})
            except OSError:
                continue
        order = {"README.md": 0, "problem.md": 1, "facts.md": 2, "questions.md": 3, "results.md": 4}
        out.sort(key=lambda r: (order.get(r["path"], 5 if r["path"].startswith("findings/") else 6), r["path"]))
        return out

    def read(self, rel: str) -> dict:
        rel = str(rel or "").replace("\\", "/").lstrip("/")
        p = (self.dir / rel).resolve()
        if self.dir.resolve() not in p.parents or p.suffix != ".md" or not p.is_file():
            from space.store import Reject
            raise Reject(404, "no_file")
        return {"path": rel, "text": p.read_text(encoding="utf-8", errors="replace")[:400_000]}
