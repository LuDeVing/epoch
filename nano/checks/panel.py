"""The panel checker: Mode 3, no objective check (docs/GENERIC_SPEC.md section 6).

A candidate is a written proposal (markdown) with five sections: CLAIM, FROM THE FACTS TO THE IDEA, FROM THE IDEA
TO THE RESULT, WEAK POINTS, PROPOSED TEST. Instead of running it, K judges read it blind: each judge is a separate
model call that sees the question, the known facts, the constraints, the criteria and this one proposal under a
random alias, never the other proposals, the other judges or the author. People's opinions from control.json
("opinions") are added with a bounded weight.

checker_args:
    criteria       list of short sentences, one per criterion (required)
    judges         K, the number of blind judge calls per proposal (default 3)
    people_weight  the weight of people's mean score (default 0.25; never more than 0.5, and scaled down when
                   fewer than three people gave an opinion)
    min_score      rung 2 fails a proposal whose panel score is below this (default 4.0; one point lower in the
                   long-shot lane)
    judge_model    optional model name for the judges (default: the loop's model)
    sd_floor       the smallest spread used for learn_z (default 0.5 points)

Ladder (stop at the first failure):
  0 lint   : the five sections are present, in order, and not empty; the proposal names at least one known fact
             (by its id, such as [F4], or by most of the fact's words)
  1 panel  : K blind judge calls; at least half must return a usable score
  2 floor  : the panel score is at least min_score
Metrics: panel_score (judges' mean, mixed with people's mean at the bounded weight), panel_sd (the judges' spread),
judge_mean, judge_scores, criteria (mean per criterion), people_score, people_n, people_weight, panel_notes,
learn_score (= panel_score), learn_gap = reference score minus candidate score (so negative is better, as for every
checker), learn_sd (pooled judges' spread), learn_z, cost_ratio 1.0.

The loop passes its own model call in with set_caller(fn), fn(prompt, meta) -> reply text, so the judges go through
the same llm.call layer, budget and logs as every other call. Without a caller, harness.llm is called directly.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import re
import statistics
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from nano import verdict as V

CHECKER = "PanelChecker"
SECTIONS = ("CLAIM", "FROM THE FACTS TO THE IDEA", "FROM THE IDEA TO THE RESULT", "WEAK POINTS", "PROPOSED TEST")
_STOP = {"the", "and", "for", "with", "that", "this", "from", "have", "each", "about", "than", "they", "their", "there",
         "when", "what", "which", "into", "over", "more", "most", "less", "only", "does", "will", "would", "could",
         "after", "before", "same", "other", "teams", "team"}


def _words(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", str(text).lower()) if len(w) >= 4 and w not in _STOP}


def sections(text: str) -> dict[str, str]:
    """The five sections of a proposal, by header at the start of a line ('HEADER:' optionally with # or **)."""
    heads = "|".join(re.escape(s) for s in SECTIONS)
    pat = re.compile(rf"^[ \t#*>-]*({heads})[ \t*]*:[ \t*]*", re.I | re.M)
    marks = [(m.start(), m.end(), m.group(1).upper()) for m in pat.finditer(text or "")]
    out: dict[str, str] = {}
    for i, (_, end, name) in enumerate(marks):
        stop = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        if name not in out:
            out[name] = text[end:stop].strip()
    return out


def lint(text: str, facts: list[dict]) -> dict:
    """Rung 0 for proposals: every section present, in order, not empty; at least one known fact named."""
    sec = sections(text)
    problems = []
    missing = [s for s in SECTIONS if s not in sec]
    if missing:
        problems.append("missing sections: " + ", ".join(missing))
    empty = [s for s in SECTIONS if s in sec and len(sec[s].split()) < 4]
    if empty:
        problems.append("sections with almost nothing in them: " + ", ".join(empty))
    order = [s for s in SECTIONS if s in sec]
    found_order = sorted(order, key=lambda s: text.upper().find(s + ":") if (s + ":") in text.upper() else 1e9)
    if not missing and order != found_order:
        problems.append("sections out of order (expected " + ", ".join(SECTIONS) + ")")
    cited = set(re.findall(r"\[(F\d+)\]", text or ""))
    ids = {str(f.get("id")) for f in facts if f.get("id")}
    named = sorted(cited & ids)
    body = _words(text)
    for f in facts:
        fw = _words(f.get("text", ""))
        if f.get("id") not in named and fw and len(fw & body) >= max(3, math.ceil(0.6 * len(fw))):
            named.append(str(f.get("id") or f.get("text", "")[:40]))
    if facts and not named:
        problems.append("the proposal names no known fact (cite one by its id, for example [" + (sorted(ids) or ["F1"])[0] + "])")
    return {"ok": not problems, "problems": problems, "sections": {k: len(v.split()) for k, v in sec.items()},
            "facts_named": named}


def parse_judge(text: str, n_criteria: int) -> dict | None:
    """'K1: 7 | reason' lines, one per criterion, and a NOTE line. None when fewer than half the criteria parse."""
    scores: dict[int, float] = {}
    reasons: dict[int, str] = {}
    for m in re.finditer(r"^\s*\**K(\d+)\**\s*[:=]\s*(\d+(?:\.\d+)?)(?:\s*/\s*10)?\s*(?:[|:-]\s*(.*))?$", text or "", re.M):
        k = int(m.group(1))
        if 1 <= k <= n_criteria and k not in scores:
            scores[k] = max(1.0, min(10.0, float(m.group(2))))
            reasons[k] = (m.group(3) or "").strip()[:200]
    if len(scores) * 2 < n_criteria:
        m = re.search(r"SCORE\s*:\s*(\d+(?:\.\d+)?)", text or "", re.I)
        if not m:
            return None
        v = max(1.0, min(10.0, float(m.group(1))))
        scores = {k: v for k in range(1, n_criteria + 1)}
    note = re.search(r"^\s*NOTE\s*:\s*(.+)$", text or "", re.M | re.I)
    return {"scores": scores, "reasons": reasons, "mean": statistics.mean(scores.values()),
            "note": note.group(1).strip()[:300] if note else ""}


def _sha(text: str) -> str:
    return hashlib.sha256((text or "").encode("utf-8", "replace")).hexdigest()[:16]


class PanelChecker:
    LEARN_STEPS = 1            # informational: the cheap check is the panel's reading
    LONG_STEPS = 0             # no long check: a proposal is read, not run
    PROFILE_SEEDS = (0,)

    def __init__(self, profile=None, *, criteria=(), judges: int = 3, people_weight: float = 0.25,
                 min_score: float = 4.0, judge_model: str | None = None, sd_floor: float = 0.5, **extra):
        self.profile = profile
        self.criteria = [str(c) for c in (criteria or [])] or ["Overall quality: the proposal is sound and useful."]
        self.k = max(1, int(judges))
        self.people_weight = max(0.0, min(0.5, float(people_weight)))
        self.min_score = float(min_score)
        self.judge_model = judge_model
        self.sd_floor = float(sd_floor)
        self.extra = extra
        self._caller = None
        self._cache: dict[str, dict] = {}          # proposal text hash -> panel metrics (the reference reuses its own)
        self._lock = threading.Lock()

    # ------------------------------------------------------------ wiring
    def set_caller(self, fn) -> None:
        """fn(prompt, meta) -> reply text. The loop passes its own call so judges are logged and charged."""
        self._caller = fn

    def _ask(self, prompt: str, meta: dict) -> str:
        if self._caller is not None:
            return self._caller(prompt, meta) or ""
        from harness import llm                              # fallback: the same call layer, no loop accounting
        r = llm.call(prompt, role="judge", model=self.judge_model, max_tokens=1200, meta=meta)
        return r.text or ""

    # ------------------------------------------------------------ facts and the judge prompt
    def known_facts(self, extra=None) -> list[dict]:
        facts = [dict(f) for f in (getattr(self.profile, "get", lambda *_: None)("facts") or []) if isinstance(f, dict)]
        for t in extra or []:
            if isinstance(t, dict):
                facts.append(t)
            elif str(t).strip():
                facts.append({"id": None, "text": str(t)})
        return facts

    def judge_prompt(self, proposal: str, alias: str, order: list[int]) -> str:
        p = self.profile
        goal = str(getattr(p, "goal", "") or "")
        facts = [f for f in self.known_facts() if f.get("id")]
        cons = list(getattr(p, "constraints", []) or [])
        crit = "\n".join(f"K{i + 1}. {self.criteria[i]}" for i in order)
        form = "\n".join(f"K{i + 1}: <score 1-10> | <one short reason>" for i in order)
        return ("You are one judge on a review panel. You read ONE proposal and score it on your own. You do not see "
                "the other proposals, the other judges or the author.\n\n"
                f"THE QUESTION:\n{goal}\n\n"
                + ("KNOWN FACTS:\n" + "\n".join(f"[{f['id']}] {f.get('text', '')}" for f in facts) + "\n\n" if facts else "")
                + ("HARD CONSTRAINTS:\n" + "\n".join(cons) + "\n\n" if cons else "")
                + f"PROPOSAL {alias}:\n```markdown\n{proposal.strip()}\n```\n\n"
                "Score the proposal from 1 (poor) to 10 (excellent) on each criterion below. Judge what is written, "
                "not what could be added. A step that does not follow from the facts, a cost the proposal hides, or a "
                "weak point it leaves out lowers the score. Length is not merit.\n\n"
                f"CRITERIA:\n{crit}\n\nReply in exactly this form:\n{form}\n"
                "NOTE: <one or two sentences: the strongest point and the weakest point>")

    # ------------------------------------------------------------ the panel
    def _panel(self, text: str, cand_name: str) -> dict:
        key = _sha(text)
        rng = random.Random(f"panel:{key}")
        n = len(self.criteria)
        prompts = []
        for j in range(self.k):
            order = list(range(n))
            rng.shuffle(order)                             # each judge reads the criteria in its own order
            alias = "P-" + "".join(rng.choice("ABCDEFGHJKLMNPQRSTUVWXYZ") for _ in range(4))
            prompts.append((j, self.judge_prompt(text, alias, order)))

        def one(jp):
            j, prompt = jp
            try:
                reply = self._ask(prompt, {"card": "panel", "operator": cand_name, "seed": str(j),
                                           "note": f"blind judge {j + 1}/{self.k} on {cand_name}"})
            except Exception as e:  # noqa: BLE001
                return {"judge": j, "error": str(e)[:200]}
            parsed = parse_judge(reply, n)
            return {"judge": j, **(parsed or {"error": "unparseable reply", "reply": reply[:300]})}
        with ThreadPoolExecutor(max_workers=min(self.k, 4)) as ex:
            return {"key": key, "judges": list(ex.map(one, prompts))}

    def _people(self, opinions) -> tuple[float | None, int, list[dict]]:
        vals, kept = [], []
        for o in opinions or []:
            try:
                s = max(1.0, min(10.0, float(o.get("score"))))
            except (TypeError, ValueError, AttributeError):
                continue
            vals.append(s)
            kept.append({"score": s, "note": str(o.get("note", ""))[:300], "who": str(o.get("who", ""))[:60]})
        return (statistics.mean(vals) if vals else None), len(vals), kept

    def _metrics(self, panel: dict, opinions) -> dict:
        ok = [j for j in panel["judges"] if "mean" in j]
        means = [j["mean"] for j in ok]
        judge_mean = statistics.mean(means) if means else None
        sd = statistics.stdev(means) if len(means) >= 2 else None
        crit = {}
        for i in range(len(self.criteria)):
            vs = [j["scores"][i + 1] for j in ok if (i + 1) in j["scores"]]
            crit[self.criteria[i].split(":")[0][:40]] = round(statistics.mean(vs), 2) if vs else None
        people, n_people, kept = self._people(opinions)
        w = self.people_weight * min(1.0, n_people / 3.0) if people is not None else 0.0
        score = None if judge_mean is None else ((1 - w) * judge_mean + w * people if people is not None else judge_mean)
        return {"panel_score": None if score is None else round(score, 3),
                "panel_sd": None if sd is None else round(sd, 3),
                "judge_mean": None if judge_mean is None else round(judge_mean, 3),
                "judge_scores": [round(x, 2) for x in means], "judges_ok": len(ok), "judges": self.k,
                "criteria": crit, "people_score": None if people is None else round(people, 2),
                "people_n": n_people, "people_weight": round(w, 3), "people_notes": kept[:10],
                "panel_notes": [j.get("note", "") for j in ok if j.get("note")],
                "panel_reasons": [{f"K{k}": v for k, v in (j.get("reasons") or {}).items() if v} for j in ok],
                "cost_ratio": 1.0}

    def relabel(self, metrics: dict, baseline: dict) -> dict:
        """Gaps of a scored proposal against a (new) reference: learn_gap = reference minus candidate."""
        ref, ref_sd = (baseline or {}).get("panel_score"), (baseline or {}).get("panel_sd")
        cand, cand_sd = metrics.get("panel_score"), metrics.get("panel_sd")
        if ref is None or cand is None:
            return {"learn_gap": None, "learn_sd": None, "learn_z": None, "learn_base": ref}
        sds = [s for s in (ref_sd, cand_sd) if s is not None]
        pooled = math.sqrt(sum(s * s for s in sds) / len(sds)) if sds else None
        pooled = max(self.sd_floor, pooled or 0.0)
        gap = round(float(ref) - float(cand), 3)
        return {"learn_gap": gap, "learn_sd": round(pooled, 3), "learn_z": V.z_of(gap, pooled, floor=self.sd_floor),
                "learn_base": ref}

    # ------------------------------------------------------------ protocol
    def baseline_profile(self, baseline: Path | None, out: Path, seeds=None, **kw) -> dict:
        """The reference proposal's panel reading: reused from its own check when the text is unchanged."""
        if baseline is None:
            return {"ok": False, "checker": "panel", "errors": ["no reference proposal yet"]}
        text = Path(baseline).read_text(encoding="utf-8")
        with self._lock:
            m = self._cache.get(_sha(text))
        if m is None:
            m = self._metrics(self._panel(text, Path(baseline).stem), kw.get("opinions"))
        prof = {"ok": m.get("panel_score") is not None, "checker": "panel", "baseline": str(baseline),
                "panel_score": m.get("panel_score"), "panel_sd": m.get("panel_sd"), "judge_scores": m.get("judge_scores"),
                "quick": {"mean": m.get("panel_score"), "sd": m.get("panel_sd")}}
        if out is not None:
            Path(out).mkdir(parents=True, exist_ok=True)
            (Path(out) / "baseline_profile.json").write_text(json.dumps(prof, indent=1), encoding="utf-8")
        return prof

    def refresh_profile(self, profile_dir: Path, **kw) -> dict:
        return {"ok": False, "checker": "panel", "errors": ["a panel profile has no baseline; the reference is chosen in the run"]}

    def check(self, candidate: Path, out: Path, baseline: dict, *, rung_max: int = 3, boundary: str | None = None,
              baseline_src: str | None = None, lenient: bool = False, audit: bool = True, facts=None,
              opinions=None, **_ignored) -> dict:
        candidate, out = Path(candidate), Path(out)
        out.mkdir(parents=True, exist_ok=True)
        rec: dict = {"candidate": str(candidate), "rungs": [], "status": "fail", "rung_reached": 0,
                     "partial_score": 0.0, "feedback": {}, "metrics": {}}
        text = candidate.read_text(encoding="utf-8")
        # rung 0: lint
        lt = lint(text, self.known_facts(facts))
        rec["rungs"].append({"rung": 0, "ok": lt["ok"], **lt})
        rec["metrics"].update({"facts_named": lt["facts_named"], "sections": lt["sections"], "changed_symbols": []})
        if not lt["ok"]:
            rec["feedback"] = {"rung": 0, "reason": "the proposal does not have the required form: " + "; ".join(lt["problems"]),
                               "problems": lt["problems"], "sections": list(SECTIONS)}
            return rec
        # rung 1: the blind panel
        panel = self._panel(text, candidate.stem)
        m = self._metrics(panel, opinions)
        (out / "panel.json").write_text(json.dumps({"panel": panel, "metrics": m}, indent=1), encoding="utf-8")
        need = math.ceil(self.k / 2)
        ok = m["judges_ok"] >= need and m["panel_score"] is not None
        rec["rungs"].append({"rung": 1, "ok": ok, "judges_ok": m["judges_ok"], "judge_scores": m["judge_scores"]})
        if not ok:
            errs = [j.get("error") for j in panel["judges"] if j.get("error")]
            rec["feedback"] = {"rung": 1, "reason": f"only {m['judges_ok']} of {self.k} judges returned a usable score",
                               "errors": errs[:4]}
            return rec
        with self._lock:
            self._cache[panel["key"]] = m
        rec["rung_reached"], rec["partial_score"] = 1, 1 / 4
        rec["metrics"].update(m)
        rec["metrics"]["learn_score"] = m["panel_score"]
        rec["metrics"].update(self.relabel(m, baseline))
        if rung_max < 2:
            rec["status"] = "checked"
            return rec
        # rung 2: the floor
        floor = self.min_score - (1.0 if lenient else 0.0)
        ok = m["panel_score"] >= floor
        rec["rungs"].append({"rung": 2, "ok": ok, "panel_score": m["panel_score"], "floor": floor,
                             "gap": rec["metrics"].get("learn_gap"), "z": rec["metrics"].get("learn_z")})
        rec["rung_reached"], rec["partial_score"] = 2, 2 / 4
        if not ok:
            rec["feedback"] = {"rung": 2, "reason": f"the panel scored the proposal {m['panel_score']} of 10, below the floor of {floor}",
                               "notes": m["panel_notes"][:3], "criteria": m["criteria"]}
            return rec
        rec["status"] = "checked"
        return rec

    def long_run(self, candidate: Path, out: Path, baseline: dict, **_ignored) -> dict:
        return {"ok": False, "reason": "a proposal has no long check"}

    def fidelity_probe(self, candidate: Path, out: Path, baseline: dict, target: str, steps: int = 60) -> dict:
        return {"checkable": False, "note": "a proposal has no diagnostics probe"}

    def final(self, candidate: Path, out: Path, baseline: dict, seeds=None, **kw) -> dict:
        """A second, independent panel reading; 'promising' when it still beats the reference by the margin."""
        text = Path(candidate).read_text(encoding="utf-8")
        m = self._metrics(self._panel(text + "\n", Path(candidate).stem + "-final"), kw.get("opinions"))
        gap = self.relabel(m, baseline)
        margin = float((getattr(self.profile, "score", None) or {}).get("margin", 0.5))
        status = "error" if m["panel_score"] is None else (
            "promising" if gap["learn_gap"] is not None and gap["learn_gap"] < -margin else "close_call")
        return {"status": status, "cand_vals": m["judge_scores"], "base_vals": (baseline or {}).get("judge_scores") or [],
                "verdict": {"panel": m, **gap}}
