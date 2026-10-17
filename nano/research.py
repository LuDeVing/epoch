"""Web research stage for the nano loop: one research call per part of the problem tree, with web
search and fetch enabled, returning a structured brief with URLs. Briefs are material for
ideation and a prior-art check at selection; they never rank ideas and never replace verification.

Brief schema (JSON from the model, filtered by script):
  {"known":  [{"name", "mechanism", "effect", "where", "url"}],   # tried, with a measured effect
   "failed": [{"name", "why", "url"}],                             # tried, did not help or transfer
   "open":   [{"direction", "why", "url"}],                        # named but untested at small scale
   "queries": [...], "node": id, "ts": ...}
Every entry without an http(s) URL is dropped, so the brief cannot carry invented citations.
Cached per part under memory/research/<key>.json, where the key (cache_key) holds the part id plus a hash of
the profile, lens, baseline version and the part's frame, so a same-id part from another map never reuses a brief.
Facts found later (merge_facts) go to an append-only <key>.facts.jsonl beside it, each row with its run, source and
fact-check verdict; the brief file itself is written once per research call.

Order of reading (see NanoLoop.plan_tree): measurements first, then one whole-problem reading call (preread_prompt:
how the field splits this kind of problem and where it is known to be weak), then the map, then one brief per part,
then doubt. The preread informs the parts; it never lists fixes, and the measurements outrank it.
"""
from __future__ import annotations

import hashlib
import json
import re
import threading
import time
from pathlib import Path

from nano.ideate import LLM_DEFAULT_VOCAB, PF, fill, vword  # noqa: F401  (PF: nano/profile.py, or the shim with the LLM defaults in ideate.py)

URL_RE = re.compile(r"https?://[^\s\"'<>]+")
RESEARCH_TOOLS = ["WebSearch", "WebFetch"]


def research_prompt(node: dict, goal_md: str, year: int = 2026) -> str:
    assumptions = "\n".join(f"- {a}" for a in node["assumptions"])
    return (fill("Research ONE part of a problem in {v:field} before anyone proposes ideas. ")
            + f"Use web search as much as needed (prefer {year} and {year - 1} sources: " + fill("{v:sources}). ")
            + "Read the most relevant results.\n\n"
            f"GOAL OF THE WHOLE PROBLEM:\n{goal_md[:1500]}\n\nPART UNDER STUDY: {node['name']}\n"
            f"CURRENT DESIGN OF THIS PART: {node['frame']}\nASSUMPTIONS OF THIS PART:\n{assumptions}\n\n"
            "Return ONLY a JSON object with keys:\n"
            '  "known": list of {"name", "mechanism" (one sentence), "effect" (what was measured, with numbers if '
            'given), "where" (' + fill("{v:size_word}") + ' / setting), "url"}  -- techniques that were tried for this part\n'
            '  "failed": list of {"name", "why", "url"}  -- techniques reported not to help or not to transfer\n'
            '  "open": list of {"direction", "why", "url"}  -- directions named but untested at small scale\n'
            '  "queries": the search queries you used\n'
            "Rules: every entry needs a real URL from your search or reading; do not include anything you cannot "
            "source; 4 to 10 known entries, 0 to 5 failed, 0 to 5 open; no commentary outside the JSON.")


def _str_list(v, cap: int = 8) -> list[str]:
    """A model's "queries" value as a list of strings: a list, one string, or anything else (null, a number) as []."""
    if isinstance(v, str):
        v = [v]
    return [str(q)[:200] for q in v][:cap] if isinstance(v, list) else []


def parse_brief(text: str, node_id: str) -> dict | None:
    m = re.search(r"\{.*\}", text or "", flags=re.S)
    if not m:
        return None
    try:
        d = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    out = {"node": node_id, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "queries": _str_list(d.get("queries"))}
    for key, fields in (("known", ("name", "mechanism", "effect", "where", "url")),
                        ("failed", ("name", "why", "url")), ("open", ("direction", "why", "url"))):
        rows = []
        for e in (d.get(key) if isinstance(d.get(key), list) else []):
            if not isinstance(e, dict):
                continue
            url = str(e.get("url", ""))
            if not URL_RE.match(url):
                continue                                    # unsourced entries are dropped
            rows.append({f: str(e.get(f, ""))[:400] for f in fields})
        out[key] = rows[:10]
    if not (out["known"] or out["failed"] or out["open"]):
        return None
    return out


TRIED_MAX = 12          # ledger lines per brief: the literature comes first, own results after it, once


def _is_ledger(e: dict) -> bool:
    return str(e.get("url", "")).startswith("ledger://")


def brief_text(brief: dict) -> str:
    lines = ["RESEARCH BRIEF for this part (sourced; every line has a URL):"]
    for e in brief.get("known", []):
        if not _is_ledger(e):
            lines.append(f"- KNOWN: {e['name']}: {e['mechanism']} Effect: {e['effect']} ({e['where']}) {e['url']}")
    for e in brief.get("failed", []):
        if not _is_ledger(e):
            lines.append(f"- DID NOT HELP: {e['name']}: {e['why']} {e['url']}")
    for e in brief.get("open", []):
        lines.append(f"- OPEN: {e['direction']}: {e['why']} {e['url']}")
    tried = brief.get("tried", [])
    if tried:
        order = {"verified": 0, "stackable": 1, "close_call": 2, "promising": 2, "fail": 3}
        rank = lambda e: next((v for k, v in order.items() if k in str(e.get("why", ""))), 4)   # noqa: E731
        shown = sorted(tried, key=rank)[:TRIED_MAX]
        lines.append(f"MEASURED HERE in earlier runs ({len(shown)} of {len(tried)} rows; the same setup, the same exam):")
        for e in shown:
            lines.append(f"- TRIED: {e['name']}: {e['why']} {e['url']}")
    return "\n".join(lines)


STOP = set("the a an of to in and or for with on at by is are be that this it as from into its than via".split())
# words that name the setting rather than the technique: they never count as evidence of a match. The setting's
# own words (for the LLM: attention, layer, token ...) come from the profile (vocab "setting_words").
GENERIC_BASE = set("output input after before specific quality gain growth mixed mix into across shared single value values "
                   "small scale record run".split())
GENERIC = GENERIC_BASE | set(LLM_DEFAULT_VOCAB["setting_words"].split())        # the LLM set, as before


def generic_words() -> set[str]:
    """GENERIC_BASE plus the active profile's setting words."""
    w = vword("setting_words")
    return GENERIC_BASE | set((" ".join(w) if isinstance(w, (list, tuple)) else str(w or "")).lower().split())


def _stem(w: str) -> str:
    for suf in ("ization", "isation", "ing", "ed", "es", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            return w[: -len(suf)]
    return w


def _words(s: str) -> set[str]:
    """Lower-case content words, hyphens split, light stemming; keeps short tokens like qk, kv."""
    return {_stem(w) for w in re.findall(r"[a-z][a-z0-9]+", (s or "").lower().replace("-", " ")) if w not in STOP}


def _match(a: str, b: str) -> bool:
    if a == b:
        return True
    return len(a) >= 4 and len(b) >= 4 and (a.startswith(b) or b.startswith(a))


def _present(name_w: set[str], cw: set[str]) -> int:
    return sum(1 for n in name_w if any(_match(n, c) for c in cw))


def prior_art_tag(cluster_text: str, brief: dict | None, threshold: float = 0.3) -> tuple[str, str | None]:
    """Lexical match of a cluster against the brief: ('known'|'failed'|'new', matched name or None).
    A technique matches when its distinctive name words (generic words removed) are all present in
    the cluster text, or at least two of them and two thirds for long names, or when the whole
    name+mechanism text overlaps the cluster by Jaccard >= threshold. Lexical only: a soft signal
    for selection (bonus for new, penalty for failed), never a verdict."""
    if not brief:
        return "unknown", None
    cw = _words(cluster_text)
    if not cw:
        return "new", None
    generic = generic_words()
    best, best_tag, best_score = None, "new", 0.0
    for tag, key, name_f in (("failed", "failed", "name"), ("known", "known", "name")):
        for e in brief.get(key, []):
            name_w = {w for w in _words(e.get(name_f, "")) if w not in generic}
            full_w = _words(e.get(name_f, "")) | _words(e.get("mechanism", e.get("why", "")))
            score = 0.0
            if name_w:
                hit = _present(name_w, cw)
                frac = hit / len(name_w)
                if hit == len(name_w) or (hit >= 2 and frac >= 0.66):
                    score = 0.5 + 0.5 * frac
            if full_w:
                inter = sum(1 for f in full_w if any(_match(f, c) for c in cw))
                j = inter / len(cw | full_w)
                if j >= threshold:
                    score = max(score, j)
            if score > best_score:
                best, best_tag, best_score = e.get(name_f), tag, score
    return (best_tag, best) if best_score > 0 else ("new", None)


def _brief_time(d: dict, p: Path) -> float:
    """When the brief was researched: its own ts (a number, or an ISO date string), else the file time."""
    ts = d.get("ts")
    if isinstance(ts, (int, float)):
        return float(ts)
    if isinstance(ts, str):
        try:
            from datetime import datetime
            return datetime.fromisoformat(ts).timestamp()
        except ValueError:
            pass
    return p.stat().st_mtime


def cache_key(node: dict, profile: str = "", lens: str = "", baseline_version: str = "") -> str:
    """The research cache key of a part: its id plus a hash of the profile name, the lens, the baseline version and
    the part's frame (frame, assumptions, boundary). A part with the same id on another map gets its own brief."""
    frame = json.dumps([str(profile or ""), str(lens or ""), str(baseline_version or ""), str(node.get("frame", "")),
                        [str(a) for a in node.get("assumptions") or []], str(node.get("boundary", ""))], sort_keys=True)
    nid = re.sub(r"[^A-Za-z0-9_-]+", "_", str(node.get("id", "x")))[:40]
    return f"{nid}__{hashlib.sha1(frame.encode('utf-8')).hexdigest()[:12]}"


def load_cached(cache_dir: Path, node_id: str, max_age_days: float) -> dict | None:
    """The cached brief under `node_id` (a cache key) if young enough, with the facts merged into it since:
    supported or unchecked facts as known entries, "not supported" ones under "disputed" (never shown as known)."""
    p = cache_dir / f"{node_id}.json"
    if not p.exists():
        return None
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None
    age = time.time() - _brief_time(d, p)         # own timestamp: merge_facts rewrites the file
    if d.get("backend") == "mock":
        return None                                   # never reuse a brief made without the web
    if age > max_age_days * 86400:
        return None
    for row in read_facts(cache_dir, node_id):
        if row.get("check") == "not supported":
            d.setdefault("disputed", []).append(row)
            continue
        effect = f"fact check: {row['check']}" if row.get("check") else "not checked against its page"
        d.setdefault("known", []).append({"name": row["text"][:80], "mechanism": row["text"][:400], "effect": effect,
                                          "where": "found while interrogating an idea", "url": row["url"],
                                          "check": row.get("check") or "", "prov": row.get("prov") or ""})
    return d


def save_cache(cache_dir: Path, brief: dict, key: str | None = None) -> None:
    """Write a brief once, under `key` (cache_key) or its node id. Later facts never rewrite it (merge_facts)."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    brief.setdefault("ts", time.strftime("%Y-%m-%dT%H:%M:%S"))   # the research time; later fact merges do not renew it
    if key:
        brief["cache_key"] = key
    (cache_dir / f"{key or brief['node']}.json").write_text(json.dumps(brief, indent=1), encoding="utf-8")


# ---------------------------------------------------------------- memory across runs (experiments ledger)
def ledger_entries(ledger_path: Path, node_id: str | None = None, baseline_version: str | None = None) -> tuple[list[dict], list[dict]]:
    """Previous overnight verdicts shaped like brief entries (known / failed). With node_id None, every
    row is returned (planner-made part ids differ between runs, so memory goes to every part)."""
    known, failed = [], []
    if not ledger_path.exists():
        return known, failed
    delta, setup = fill("{v:delta_name} delta"), fill("{v:setup}")
    for line in ledger_path.read_text(encoding="utf-8").splitlines():
        try:
            row = json.loads(line)
        except Exception:  # noqa: BLE001
            continue
        if not row.get("hypothesis"):
            continue
        if node_id is not None and row.get("node") != node_id:
            continue
        if baseline_version is not None and row.get("baseline_version", "v1") != baseline_version:
            continue
        if str(row.get("run", "")).startswith("mock") or str(row.get("cand_id", "")).startswith("ctl_") or str(row.get("hypothesis", "")).lower().startswith("control:"):
            continue                                      # mock runs and control candidates are not memory
        url = f"ledger://{row.get('run')}/{row.get('cand_id')}"
        name = str(row["hypothesis"])[:90]
        if row.get("status") == "verified":
            known.append({"name": name, "mechanism": str(row["hypothesis"])[:400],
                          "effect": f"verified in a previous run: {delta} {row.get('delta')} over {row.get('n_seeds')} seeds",
                          "where": setup, "url": url})
        elif row.get("status") == "fail":
            failed.append({"name": name, "url": url,
                           "why": f"tried in a previous run: failed, delta {row.get('delta')} over {row.get('n_seeds')} seeds"})
        elif row.get("status") == "stackable":
            known.append({"name": name, "mechanism": str(row["hypothesis"])[:400],
                          "effect": f"stackable in a previous run: a small real gain, delta {row.get('delta')} over {row.get('n_seeds')} seeds; it combines with others",
                          "where": setup, "url": url})
        elif row.get("status") in ("close_call", "promising"):
            known.append({"name": name, "mechanism": str(row["hypothesis"])[:400],
                          "effect": f"tried in a previous run: {row.get('status')} (better than the baseline mean but not yet by 2 SD), delta {row.get('delta')} over {row.get('n_seeds')} seeds",
                          "where": setup, "url": url})
    return known, failed


def facts_path(cache_dir: Path, key: str) -> Path:
    return cache_dir / f"{key}.facts.jsonl"


def read_facts(cache_dir: Path, key: str) -> list[dict]:
    """The append-only fact rows of a brief, in order; unreadable lines are skipped."""
    p = facts_path(cache_dir, key)
    out = []
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(row, dict) and row.get("url") and row.get("text"):
                out.append(row)
    return out


def merge_facts(cache_dir: Path, node_id: str, facts: list, run: str = "") -> int:
    """Append sourced facts from an interrogation to the brief `node_id` (a cache key) as rows of the append-only
    <key>.facts.jsonl: text, url, provenance, the fact-check verdict (_check_web_facts: supported, not supported,
    unclear, or "" when not checked) with its quote, the run and the time. `facts` holds strings or the
    interrogation's known_tagged dicts {"text", "prov", "check", "check_quote"}; beliefs are not facts and are
    skipped. Dedup by URL + text. The brief must exist; nothing is ever rewritten. Returns rows added."""
    if not (cache_dir / f"{node_id}.json").exists():
        return 0
    with _facts_lock(facts_path(cache_dir, node_id)):     # read, dedup and append as one step (threads and runs)
        return _merge_facts_locked(cache_dir, node_id, facts, run)


_merge_lock = threading.Lock()


class _facts_lock:
    """One writer at a time for a facts file: a thread lock plus a lock file beside it (O_EXCL) for concurrent runs.
    A lock file older than 60 s is taken as left behind by a dead run; after 30 s of waiting the append goes ahead."""

    def __init__(self, path: Path):
        self.lock_path = Path(str(path) + ".lock")
        self.held = False

    def __enter__(self):
        import os
        _merge_lock.acquire()
        t0 = time.time()
        while True:
            try:
                os.close(os.open(str(self.lock_path), os.O_CREAT | os.O_EXCL | os.O_WRONLY))
                self.held = True
                return self
            except FileExistsError:
                try:
                    if time.time() - self.lock_path.stat().st_mtime > 60:
                        self.lock_path.unlink()
                except OSError:
                    pass
                if time.time() - t0 > 30:
                    return self
                time.sleep(0.05)
            except OSError:
                return self

    def __exit__(self, *exc):
        try:
            if self.held:
                self.lock_path.unlink()
        except OSError:
            pass
        finally:
            _merge_lock.release()
        return False


def _merge_facts_locked(cache_dir: Path, node_id: str, facts: list, run: str) -> int:
    have = {(r.get("url"), str(r.get("text", ""))[:60]) for r in read_facts(cache_dir, node_id)}
    rows = []
    for f in facts:
        t = f if isinstance(f, dict) else {"text": str(f)}
        text = str(t.get("text", ""))
        if t.get("prov") == "belief":
            continue
        m = URL_RE.search(text)
        if not m:
            continue
        key = (m.group(0), text[:60])
        if key in have:
            continue
        have.add(key)
        rows.append({"ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "run": run, "text": text[:400], "url": m.group(0),
                     "prov": str(t.get("prov") or "untagged"), "check": str(t.get("check") or ""),
                     "check_quote": str(t.get("check_quote") or "")[:200], "source": "interrogation"})
    if rows:
        with facts_path(cache_dir, node_id).open("a", encoding="utf-8") as fh:
            fh.write("".join(json.dumps(r) + "\n" for r in rows))
    return len(rows)


# ---------------------------------------------------------------- reading before the map (whole problem)
PREREAD_CHARS = 8000            # about 2000 tokens of the summary reach the planner


def preread_prompt(goal_md: str, year: int = 2026) -> str:
    """One reading call on the whole problem before the planner draws the map: how the field splits this kind of
    problem and where it is known to be weak. It reports structure, not fixes, so the map is not anchored on ideas."""
    return (fill("Read what is known about this problem in {v:field} before anyone splits it into parts. ")
            + f"Use web search and fetch as much as it takes. Prefer {year} and {year - 1} sources, "
            "then the best-supported older work.\n\n"
            f"THE PROBLEM:\n{goal_md[:3000]}\n\n"
            "Report two things.\n"
            "1. HOW THE FIELD SPLITS IT: the parts or stages that papers, surveys and strong practitioners use to "
            "describe this kind of problem, and which of them they treat as separate or coupled.\n"
            "2. KNOWN WEAK SPOTS: where measured gains have come from, where they stopped, and which parts are "
            "reported to matter more than they look.\n"
            "Rules: every line carries the URL of its source on the same line; a line without a source is dropped. "
            "Do not propose changes or ideas; report how the field sees the problem. Under 1200 words.\n\n"
            "Answer in this form:\nPARTS:\n- <part>: <what it covers> <URL>\nWEAK SPOTS:\n- <spot>: <what is reported> <URL>")


_PREREAD_HEADS = ("PARTS", "WEAK SPOTS", "HOW THE FIELD SPLITS IT", "KNOWN WEAK SPOTS")


def parse_preread(text: str, cap: int = PREREAD_CHARS) -> dict | None:
    """Keep the sourced lines (and the two headings) of a preread reply, capped to `cap` characters.
    None when fewer than two sourced lines survive."""
    keep, used, n_src = [], 0, 0
    for line in str(text or "").replace("**", "").splitlines():
        line = line.rstrip()
        if not line.strip():
            continue
        head = line.strip().lstrip("#0123456789. ").rstrip(":").upper() in _PREREAD_HEADS
        if not head and not URL_RE.search(line):
            continue
        if used + len(line) + 1 > cap:
            break
        keep.append(line)
        used += len(line) + 1
        n_src += 0 if head else 1
    if n_src < 2:
        return None
    body = "\n".join(keep)
    return {"text": body, "n_sourced": n_src, "urls": sorted(set(URL_RE.findall(body)))[:40],
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}


def preread_block(pre: dict | None) -> str:
    """The planner's block. The measurements outrank it; it names parts and weak spots, not fixes."""
    if not pre or not pre.get("text"):
        return ""
    return ("\n\nWHAT THE FIELD SAYS ABOUT THIS PROBLEM (read before drawing the map; every line has a source; "
            "use it to name parts and weak spots the map should show, not as a list of fixes; where it disagrees "
            "with the measurements below, the measurements win):\n" + pre["text"])


# ---------------------------------------------------------------- model-based prior-art tagging
def tag_prompt(clusters: list[dict], sketches_by_id: dict, brief: dict) -> str:
    rows = []
    for c in clusters:
        rep = sketches_by_id.get(c["representative"], {})
        rows.append(f"[{c['cluster_id']}] {c['name']}: {rep.get('mechanism', '')[:300]}")
    entries = [f"K{i}: {e['name']}: {e.get('mechanism', '')[:200]}" for i, e in enumerate(brief.get("known", []))]
    entries += [f"F{i}: {e['name']}: {e.get('why', '')[:200]}" for i, e in enumerate(brief.get("failed", []))]
    return ("Match idea clusters against a list of techniques from the literature. For every cluster decide: "
            "\"known\" if it is the same mechanism as a K entry, \"failed\" if it is the same mechanism as an F entry, "
            "\"new\" otherwise. Same mechanism means the same change, not the same topic: " + fill("{v:same_change_example}") + ". Return ONLY a JSON array of {\"id\": \"<cluster id>\", \"tag\": \"new|known|failed\", "
            "\"match\": \"<entry label or empty>\"}.\n\nTECHNIQUES:\n" + "\n".join(entries)
            + "\n\nCLUSTERS:\n" + "\n".join(rows))


def parse_tags(text: str, valid_ids: set[str], brief: dict) -> dict[str, tuple[str, str | None]] | None:
    m = re.search(r"\[.*\]", text or "", flags=re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    out = {}
    for row in arr:
        if not isinstance(row, dict):
            continue
        cid, tag = str(row.get("id", "")), str(row.get("tag", "")).lower()
        if cid not in valid_ids or tag not in ("new", "known", "failed"):
            continue
        label = str(row.get("match") or "")
        name = None
        mm = re.match(r"([KF])(\d+)", label)
        if mm:
            lst = brief.get("known" if mm.group(1) == "K" else "failed", [])
            idx = int(mm.group(2))
            if 0 <= idx < len(lst):
                name = lst[idx].get("name")
        out[cid] = (tag, name)
    return out or None


# ---------------------------------------------------------------- structured analogy (cross-domain research)
def analogy_prompt(node: dict, goal_md: str) -> str:
    assumptions = "\n".join(f"- {a}" for a in node["assumptions"])
    return (fill("Find ANALOGIES in OTHER fields to one part of a {v:recipe} from {v:field}. The point is ")
            + f"to transfer structure, not to copy a technique.\n\nGOAL OF THE WHOLE PROBLEM:\n{goal_md[:1200]}\n\n"
            f"PART: {node['name']}\nCURRENT DESIGN: {node['frame']}\nASSUMPTIONS:\n{assumptions}\n\n"
            "Use web search as much as needed. Find 5 problems in other fields (biology, control, signal "
            "processing, economics, logistics, physics, ecology, linguistics, operations research...) that have the "
            "SAME STRUCTURE as this part: the same kind of constraint, flow, allocation, feedback or trade-off. For each, "
            "give the mechanism that field uses, the correspondence (what maps to what), and ONE documented case with "
            "a real URL.\n\nReturn ONLY a JSON object:\n"
            '{"analogues": [{"field": ..., "problem": "<the analogous problem in that field, one sentence>", '
            '"mechanism": "<how that field solves it>", "correspondence": "<their X is our Y; their Z is our W>", '
            '"case": "<the documented case>", "url": "<real URL>"}], "queries": [...]}\n'
            "Rules: structural similarity, not vocabulary; no entry without a URL; 5 entries from 5 different fields.")


def parse_analogies(text: str, node_id: str) -> dict | None:
    m = re.search(r"\{.*\}", text or "", flags=re.S)
    if not m:
        return None
    try:
        d = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    rows = []
    for e in (d.get("analogues") if isinstance(d.get("analogues"), list) else []):
        if not isinstance(e, dict) or not URL_RE.match(str(e.get("url", ""))):
            continue
        rows.append({k: str(e.get(k, ""))[:400] for k in ("field", "problem", "mechanism", "correspondence", "case", "url")})
    if not rows:
        return None
    return {"node": node_id, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "analogues": rows[:8],
            "queries": _str_list(d.get("queries"))}


def analogy_text(an: dict) -> str:
    lines = ["ANALOGUES FROM OTHER FIELDS (structure to transfer, not techniques to copy; each has a source):"]
    for e in an.get("analogues", []):
        lines.append(f"- {e['field']}: {e['problem']} MECHANISM THERE: {e['mechanism']} CORRESPONDENCE: {e['correspondence']} "
                     f"CASE: {e['case']} {e['url']}")
    return "\n".join(lines)


# ---------------------------------------------------------------- web by delegation
# The strong model never runs a search turn: it lists the questions it would look up, the research
# model answers them with sources, and the strong model then writes with the findings in front of it.
QUESTIONS_ADDENDUM = """

BEFORE ANYTHING ELSE: a research assistant with web access will look things up for you. List the web questions whose answers would change what you write: the newest (2025-2026) techniques for this part and their measured effects, what was tried and failed, measured facts you are unsure of, mechanisms from other fields you want checked. Each question specific enough to search, one per line, at most 8. Output ONLY this block and nothing else:
QUESTIONS:
1. <question>
2. <question>
"""

FINDINGS_HEADER = ("WEB FINDINGS (a research assistant searched the web for the questions you listed; every claim carries its URL; "
                   "'no source found' means exactly that; treat these as facts to build on or depart from, not as a list to copy):")


def parse_questions(text: str, cap: int = 8) -> list[str]:
    """The numbered questions under QUESTIONS:, in order, at most cap."""
    m = re.search(r"QUESTIONS:(.*)", text or "", flags=re.S)
    block = m.group(1) if m else (text or "")
    out = []
    for line in block.splitlines():
        mm = re.match(r"^\s*(?:\d+[.)]|-|\*)\s*(.+?)\s*$", line)
        if mm and len(mm.group(1)) > 12:
            out.append(mm.group(1)[:300])
        if len(out) >= cap:
            break
    return out


def findings_prompt(questions: list[str], context: str = "", year: int = 2026) -> str:
    qs = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(questions))
    return (fill("An idea agent that is improving {v:problem_brief} listed the questions below. ")
            + (f"The agent is working on: {context}. " if context else "")
            + f"Answer each question below with facts from the web. Use web search and fetch as much as it takes. "
            f"Newest first ({year} and {year - 1}), then the best-supported older work. "
            + fill("Give measured numbers ({v:measured_numbers}) whenever the source has them, and say at what {v:size_word} they were measured. ")
            + "Every claim carries the URL of its source on the same line; a claim without a source is not an answer. "
            "If nothing can be found, write 'no source found' for that question. Do not propose ideas; report what exists. "
            "Keep each answer to 3-8 lines; the whole reply under 1500 words.\n\n"
            "QUESTIONS:\n" + qs + "\n\nAnswer in this form:\nFINDINGS:\n1. <answer with URLs>\n2. <answer with URLs>")


# ---------------------------------------------------------------- fetch on demand (one fact, mid-task)
# A builder or reviser that lacks one specific fact writes `NEED: <fact>` instead of guessing. The loop asks the
# research model for that one fact (web search, a source on the line), caches it per run, and re-prompts once.
# Other stages (the interrogation chain in deepen.py) may import fetch_fact and pass their own `call`.
FETCH_CACHE_NAME = "facts_fetched.jsonl"
NEED_CAP = 2                    # NEED lines honoured per reply
_NEED_EMPTY = {"", "none", "omit", "omitted", "n/a", "na", "-", "nothing", "no"}
_fetch_lock = threading.Lock()
_fetch_key_locks: dict[str, threading.Lock] = {}


def parse_needs(text: str, cap: int = NEED_CAP) -> tuple[list[str], int]:
    """The NEED lines of a reply, outside code blocks, in order: (the first `cap`, the number dropped by the cap).
    Placeholders ('omit', 'none', '<...>') do not count; repeats (same normalised text) count once."""
    outside = re.sub(r"```.*?(```|\Z)", "", str(text or ""), flags=re.S).replace("**", "")
    out, seen = [], set()
    for line in outside.splitlines():
        m = re.match(r"^\s*(?:[-*]\s*)?NEED\s*:\s*(.*?)\s*$", line, flags=re.I)
        if not m:
            continue
        q = m.group(1).strip()
        if q.lower().strip(" .") in _NEED_EMPTY or q.startswith("<") or len(q) < 6:
            continue
        k = normalise_question(q)
        if k in seen:
            continue
        seen.add(k)
        out.append(q[:300])
    return out[:cap], max(0, len(out) - cap)


def normalise_question(q: str) -> str:
    """Lower case, punctuation dropped, whitespace collapsed: the cache key of a fetched fact."""
    return " ".join(re.sub(r"[^a-z0-9%.+-]+", " ", str(q or "").lower()).split()).strip(" .")


def fetch_prompt(question: str, node: dict | None = None, year: int = 2026) -> str:
    part = (f" The agent is working on this part: {node.get('name')} ({node.get('frame', '')})."
            if isinstance(node, dict) and node.get("name") else "")
    return ("An agent that is writing code is missing one fact." + part
            + f" Find this one fact on the web. Use web search and fetch as much as it takes. Prefer {year} and {year - 1} "
            "sources, then the best-supported older work. Give the measured number or the exact rule when the source has it. "
            "Do not propose ideas. Report what the source says.\n\n"
            f"QUESTION: {question}\n\n"
            "Answer in exactly this form:\n"
            "ANSWER: <the fact, one to four sentences, or 'not found'>\n"
            "SOURCE: <the URL the answer comes from>\n"
            "CONFIDENCE: <high | medium | low>\n"
            "Rules: an answer without a real URL is not an answer. If nothing can be found, write ANSWER: not found.")


def parse_fetch(text: str, question: str) -> dict:
    """A fetch reply -> {question, answer, source_url, confidence, tag: "web"} or {question, answer: None, reason}."""
    t = str(text or "").replace("**", "")
    a = re.search(r"ANSWER:[ \t]*(.*?)(?=\n\s*(?:SOURCE|CONFIDENCE)\s*:|\Z)", t, flags=re.S | re.I)   # an empty one stays empty
    s = re.search(r"SOURCE:[ \t]*(\S+)", t, flags=re.I)
    c = re.search(r"CONFIDENCE:\s*(high|medium|low)\b", t, flags=re.I)
    ans = " ".join(a.group(1).split())[:800] if a else ""
    url = s.group(1).strip("<>()[],;") if s else ""
    if not ans or ans.lower().startswith(("not found", "no source")):
        return {"question": question, "answer": None, "reason": "not found"}
    if not URL_RE.match(url):
        m = URL_RE.search(ans)                          # a URL inside the answer still counts as its source
        if not m:
            return {"question": question, "answer": None, "reason": "no source URL"}
        url = m.group(0).rstrip(".,;)")
    return {"question": question, "answer": ans, "source_url": url.rstrip("."),
            "confidence": c.group(1).lower() if c else "low", "tag": "web"}


def _read_fetch_cache(path: Path) -> dict[str, dict]:
    out: dict[str, dict] = {}
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            try:
                row = json.loads(line)
            except Exception:  # noqa: BLE001
                continue
            if isinstance(row, dict) and row.get("key"):
                out[row["key"]] = row
    return out


def fetch_fact(question: str, node: dict | None, call, cache_dir: Path | str | None = None) -> dict:
    """One delegated web call for one missing fact. `call(prompt) -> str` (or a result with .text) runs the
    research model with web tools; the caller logs and charges it. Returns {question, answer, source_url,
    confidence: high|medium|low, tag: "web"} or {question, answer: None, reason}. With cache_dir (the run folder)
    results, "not found" included, are cached by normalised question in facts_fetched.jsonl, so the same question
    is never fetched twice in a run; a result read from the cache carries "cached": True."""
    key = normalise_question(question)
    if not key:
        return {"question": question, "answer": None, "reason": "empty question"}
    path = Path(cache_dir) / FETCH_CACHE_NAME if cache_dir is not None else None
    with _fetch_lock:
        klock = _fetch_key_locks.setdefault(f"{path}|{key}", threading.Lock())
    with klock:                                         # two builders asking the same thing: one fetch
        if path is not None:
            hit = _read_fetch_cache(path).get(key)
            if hit is not None:
                return {**{k: v for k, v in hit.items() if k not in ("key", "ts", "node")}, "cached": True}
        try:
            text = call(fetch_prompt(question, node))
        except Exception as e:  # noqa: BLE001
            return {"question": question, "answer": None, "reason": f"fetch failed: {str(e)[:120]}"}
        res = parse_fetch(text if isinstance(text, str) else getattr(text, "text", ""), question)
        if path is not None:
            row = {"key": key, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
                   "node": node.get("id") if isinstance(node, dict) else None, **res}
            with _fetch_lock:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("a", encoding="utf-8") as fh:
                    fh.write(json.dumps(row) + "\n")
        return res


def facts_block(facts: list[dict]) -> str:
    """The re-prompt block: every fact asked for, with its source, or 'not found'."""
    lines = ["FACTS YOU ASKED FOR (a research assistant looked each one up on the web):"]
    for f in facts:
        if f.get("answer"):
            lines.append(f"- {f['question']}\n  ANSWER: {f['answer']} (source: {f['source_url']}; "
                         f"confidence: {f.get('confidence', 'low')})")
        else:
            lines.append(f"- {f['question']}\n  not found ({f.get('reason', 'no source')})")
    return "\n".join(lines)
