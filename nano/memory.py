"""Per-part persistent memory: what the team already knows about one part of the problem, kept across runs.

Design: research_notes/team_gaps/02_persistent_expertise.md. One structured markdown file per part,
read whole (no top-k retrieval), capped in the rendered view. After each round a curator model proposes
a delta in the same headers; `curate` keeps an entry only if it cites a run artefact that exists and is
not a near-duplicate, then appends it with date, run and round. Entries are never rewritten by a model;
the only edits are the "used" counter and moving stale entries to ARCHIVE.

File: <lab>/memory/<profile>/<part>.md (profile key `memory_dir` overrides the folder).

    # Memory: <part>
    CLOCK: 3
    ## FACTS
    - [m1a2b3c] 2026-10-17 | run-x r2 | measured | best fit used 1.08 bins per unit size (n062cd9b5c8) | used 3
    ## TRIED
    ...

CLOCK counts the curations of this part; "used N" is the clock value when the entry was last confirmed
(added, re-proposed as a near-duplicate, or listed under USED by the curator).
"""
from __future__ import annotations

import datetime as _dt
import hashlib
import re
import threading
from pathlib import Path

SECTIONS = ("FACTS", "TRIED", "PRIORS", "CUES", "OPEN QUESTIONS", "FAILED FRAMINGS")
ARCHIVE = "ARCHIVE"
SOURCES = ("script", "measured", "web", "belief")

BLOCK_HEAD = ("WHAT THIS TEAM ALREADY KNOWS ABOUT THIS PART (evidence, not rules; "
              "dispute it if the facts say otherwise):")

# what a delta entry looks like, per section (shown to the curator model)
DELTA_FORMAT = """Reply with a memory delta under these six headers, one bullet per entry, nothing else:
FACTS:
- <script|measured|web|belief> | <one fact> | <evidence: a candidate id, a sketch id, a measured number from above, or a URL>
TRIED:
- <idea> | <result number> | <why it failed or won> | <evidence>
PRIORS:
- <a calibrated statement with a number, like "rules of type X won 1 in 4 here"> | <evidence>
CUES:
- when <condition> -> <action> | <evidence>
OPEN QUESTIONS:
- <a question the results raise> | <evidence>
FAILED FRAMINGS:
- <a way of seeing the part that did not pay off> | <why> | <evidence>
USED:
- <ids of existing memory entries that this round's results bear on, comma-separated, or none>
Rules: every entry must cite at least one artefact listed above, by its exact id, number or URL. Entries
without a real citation are dropped. Write evidence, not rules. Leave a header empty if nothing fits.
Short plain sentences."""

_ID_RE = re.compile(r"\b([ns][0-9a-f]{10})\b")          # candidate ids n..., sketch ids s... (harness ids.new_id)
_URL_RE = re.compile(r"https?://[^\s|,)>\]]+")
_NUM_RE = re.compile(r"(?<![\w.])[-+]?\d+\.(\d+)(?![\w.])")
_LINE_RE = re.compile(r"^- \[(\w+)\] (\S+) \| (.*?) \| (" + "|".join(SOURCES) + r") \| (.*) \| used (\d+)$")
_TOKEN_RE = re.compile(r"[a-z0-9]+")
_LOCK = threading.Lock()


def _today() -> str:
    return _dt.date.today().isoformat()


def tokens(text: str) -> set[str]:
    return set(_TOKEN_RE.findall(text.lower()))


def jaccard(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def _num_tokens(s: str) -> int:
    return max(1, len(s) // 4)


def _infer_source(text: str) -> str:
    if _URL_RE.search(text):
        return "web"
    if _ID_RE.search(text) or _NUM_RE.search(text):
        return "measured"
    return "belief"


def _safe(part: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", str(part)) or "part"


class Memory:
    """One profile's memory folder; one markdown file per part id."""

    def __init__(self, root_dir, profile_name: str, max_tokens: int = 4000):
        self.dir = Path(root_dir) / _safe(profile_name)
        self.profile = profile_name
        self.max_tokens = max_tokens

    # ---------------------------------------------------------------- file io
    def path(self, part: str) -> Path:
        return self.dir / f"{_safe(part)}.md"

    def load(self, part: str) -> dict:
        """{"clock": int, "sections": {name: [entry]}}; entry = {id, date, run, source, text, used}."""
        data = {"clock": 0, "sections": {s: [] for s in SECTIONS + (ARCHIVE,)}}
        p = self.path(part)
        if not p.exists():
            return data
        cur = None
        for line in p.read_text(encoding="utf-8").splitlines():
            line = line.rstrip()
            if line.startswith("CLOCK:"):
                try:
                    data["clock"] = int(line.split(":", 1)[1].strip())
                except ValueError:
                    pass
            elif line.startswith("## "):
                name = line[3:].strip().upper()
                cur = name if name in data["sections"] else None
            elif cur and line.startswith("- "):
                m = _LINE_RE.match(line)
                if m:
                    data["sections"][cur].append({"id": m.group(1), "date": m.group(2), "run": m.group(3),
                                                  "source": m.group(4), "text": m.group(5), "used": int(m.group(6))})
        return data

    def save(self, part: str, data: dict) -> None:
        self.dir.mkdir(parents=True, exist_ok=True)
        lines = [f"# Memory: {part}", f"CLOCK: {data['clock']}"]
        for s in SECTIONS + (ARCHIVE,):
            lines.append(f"## {s}")
            for e in data["sections"][s]:
                lines.append(f"- [{e['id']}] {e['date']} | {e['run']} | {e['source']} | {e['text']} | used {e['used']}")
        self.path(part).write_text("\n".join(lines) + "\n", encoding="utf-8")

    def parts(self) -> list[str]:
        return sorted(p.stem for p in self.dir.glob("*.md")) if self.dir.exists() else []

    # ---------------------------------------------------------------- read (whole file, capped view)
    def read(self, part: str, max_tokens: int | None = None) -> str:
        """The file's live sections as text. Over the cap, the oldest low-value entries are left out of this
        view (never out of the file): beliefs before web before measured, least recently used first."""
        cap = self.max_tokens if max_tokens is None else max_tokens
        data = self.load(part)
        entries = [(s, e) for s in SECTIONS for e in data["sections"][s]]
        if not entries:
            return ""
        value = {"belief": 0, "web": 1, "measured": 2, "script": 2}
        guard = {"FAILED FRAMINGS": 1}                    # the dead-end map is the anti-fixation guard: drop it last
        order = sorted(entries, key=lambda se: (guard.get(se[0], 0), value.get(se[1]["source"], 0), se[1]["used"], se[1]["date"]))
        keep = list(entries)
        dropped = 0

        def render(es) -> str:
            out = []
            for s in SECTIONS:
                rows = [e for (ss, e) in es if ss == s]
                if rows:
                    out.append(s + ":")
                    out += [f"- [{e['id']}] {e['text']} ({e['source']}, {e['date']}, {e['run']})" for e in rows]
            if dropped:
                out.append(f"({dropped} older low-value entries left out of this view; they stay in the file)")
            return "\n".join(out)

        text = render(keep)
        for se in order:
            if _num_tokens(text) <= cap:
                break
            keep.remove(se)
            dropped += 1
            text = render(keep)
        return text

    def block(self, part: str) -> str:
        """The prompt block, or "" when the part has no memory yet."""
        body = self.read(part)
        return f"{BLOCK_HEAD}\n{body}\n\n" if body else ""

    # ---------------------------------------------------------------- delta -> entries
    @staticmethod
    def propose_delta(part: str, text: str) -> dict:
        """Parse a curator reply (the six headers plus USED) into {"entries": [{section, source, text}], "used": [ids]}."""
        out = {"part": part, "entries": [], "used": []}
        cur = None
        heads = {h: h for h in SECTIONS}
        heads.update({"OPEN QUESTION": "OPEN QUESTIONS", "QUESTIONS": "OPEN QUESTIONS", "FAILED FRAMING": "FAILED FRAMINGS",
                      "PRIOR": "PRIORS", "CUE": "CUES", "FACT": "FACTS", "USED": "USED"})
        for raw in (text or "").splitlines():
            line = raw.strip().replace("**", "")
            if not line:
                continue
            m = re.match(r"^#*\s*([A-Z][A-Z ]+?)\s*:\s*(.*)$", line)
            if m and m.group(1).strip() in heads:
                cur = heads[m.group(1).strip()]
                rest = m.group(2).strip()
                if cur == "USED" and rest:
                    out["used"] += re.findall(r"\bm[0-9a-f]{6}\b", rest)
                continue
            if cur is None or not re.match(r"^[-*\d]", line):
                continue
            body = re.sub(r"^(?:[-*]|\d+[.)])\s*", "", line).strip()
            if not body or body.lower() in ("none", "n/a", "-"):
                continue
            if cur == "USED":
                out["used"] += re.findall(r"\bm[0-9a-f]{6}\b", body)
                continue
            source = ""
            first = body.split("|", 1)[0].strip().lower()
            if cur == "FACTS" and first in SOURCES and "|" in body:
                source, body = first, body.split("|", 1)[1].strip()
            body = re.sub(r"\s+", " ", body)
            out["entries"].append({"section": cur, "source": source or _infer_source(body), "text": body[:600]})
        return out

    # ---------------------------------------------------------------- curator rule
    @staticmethod
    def cites(text: str, artefacts: dict) -> tuple[bool, str]:
        """True when the entry cites at least one artefact that exists and no id-shaped citation is made up.
        artefacts: {"cand_ids": set, "sketch_ids": set, "numbers": iterable of floats, "urls": set}."""
        cands, sketches = set(artefacts.get("cand_ids") or ()), set(artefacts.get("sketch_ids") or ())
        urls = {u.rstrip("/.") for u in (artefacts.get("urls") or ())}
        nums = [float(x) for x in (artefacts.get("numbers") or ()) if isinstance(x, (int, float))]
        hits, fakes = [], []
        for i in _ID_RE.findall(text):
            (hits if (i in cands or i in sketches) else fakes).append(i)
        for u in _URL_RE.findall(text):
            (hits if u.rstrip("/.") in urls else fakes).append(u)
        for m in _NUM_RE.finditer(text):
            d = len(m.group(1))
            if d < 2:
                continue                                  # "1.5x" or "round 2.0" is not a measured citation
            x = float(m.group(0))
            if any(abs(round(v, d) - x) < 10 ** (-d) / 2 + 1e-12 for v in nums):
                hits.append(m.group(0))
        if fakes:
            return False, "cites an artefact that does not exist: " + ", ".join(fakes[:3])
        if not hits:
            return False, "cites no run artefact"
        return True, "cites " + ", ".join(hits[:3])

    def curate(self, part: str, delta: dict, artefacts: dict, run: str = "", round_no: int = 0,
               sim: float = 0.6) -> dict:
        """Check each proposed entry against the run's artefacts and the existing entries; append the kept ones.
        Returns {"added": [entry], "rejected": [{text, section, reason}], "bumped": [ids]}."""
        with _LOCK:
            data = self.load(part)
            data["clock"] += 1
            clock = data["clock"]
            existing = [e for s in SECTIONS + (ARCHIVE,) for e in data["sections"][s]]
            res = {"added": [], "rejected": [], "bumped": []}
            by_id = {e["id"]: e for e in existing}
            for i in delta.get("used", []):
                if i in by_id:
                    by_id[i]["used"] = clock
                    res["bumped"].append(i)
            for d in delta.get("entries", []):
                ok, why = self.cites(d["text"], artefacts)
                if ok and d["section"] == "PRIORS" and not re.search(r"\d", _ID_RE.sub("", d["text"])):
                    ok, why = False, "a prior needs a number"
                if ok and d["section"] == "CUES" and "->" not in d["text"]:
                    ok, why = False, "a cue needs the form: when <condition> -> <action>"
                if not ok:
                    res["rejected"].append({"section": d["section"], "text": d["text"], "reason": why})
                    continue
                dup = next((e for e in existing if jaccard(e["text"], d["text"]) > sim), None)
                if dup is not None:
                    dup["used"] = clock
                    res["bumped"].append(dup["id"])
                    res["rejected"].append({"section": d["section"], "text": d["text"],
                                            "reason": f"near-duplicate of {dup['id']}"})
                    continue
                eid = "m" + hashlib.sha1(f"{part}|{d['section']}|{d['text']}|{run}|{round_no}".encode()).hexdigest()[:6]
                e = {"id": eid, "date": _today(), "run": f"{run} r{round_no}".strip(), "source": d["source"],
                     "text": d["text"].replace("\n", " "), "used": clock}
                data["sections"][d["section"]].append(e)
                existing.append(e)
                res["added"].append({**e, "section": d["section"]})
            self.save(part, data)
            return res

    # ---------------------------------------------------------------- decay
    def archive(self, part: str, unused_rounds: int = 5) -> list[str]:
        """Move entries not confirmed in the last `unused_rounds` curations of this part to ARCHIVE (kept, not read)."""
        with _LOCK:
            data = self.load(part)
            moved = []
            for s in SECTIONS:
                stay = []
                for e in data["sections"][s]:
                    if data["clock"] - e["used"] >= unused_rounds:
                        data["sections"][ARCHIVE].append({**e, "text": f"({s}) {e['text']}"})
                        moved.append(e["id"])
                    else:
                        stay.append(e)
                data["sections"][s] = stay
            if moved:
                self.save(part, data)
            return moved


def curator_prompt(part_name: str, part_id: str, memory_text: str, results: list[dict], urls: list[str]) -> str:
    """The curator's prompt: this round's results on one part, the current memory, and the delta format."""
    lines = [f"You keep the team's memory for one part of the problem: '{part_name}' (id {part_id}).",
             "Below are this round's checked results on this part. Propose what the team should remember.",
             "", "THIS ROUND'S RESULTS (the only artefacts you may cite):"]
    for r in results:
        ms = ", ".join(f"{k} {v}" for k, v in (r.get("metrics") or {}).items() if isinstance(v, (int, float)))
        lines.append(f"- candidate {r['cand_id']} | status {r.get('status')} | hypothesis: {r.get('hypothesis', '')}"
                     + (f" | metrics: {ms}" if ms else "") + (f" | reason: {r['reason']}" if r.get("reason") else "")
                     + (f" | from sketches {', '.join(r['sketches'][:3])}" if r.get("sketches") else ""))
    if urls:
        lines += ["", "SOURCES FROM THE RESEARCH BRIEF:"] + [f"- {u}" for u in urls[:12]]
    lines += ["", "THE MEMORY AS IT STANDS (do not repeat these; list the ones this round bears on under USED):",
              memory_text or "(empty)", "", DELTA_FORMAT]
    return "\n".join(lines)
