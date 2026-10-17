"""Choosing the team's next question (docs/TEAM_GAPS_SPEC.md, agent C; research_notes/team_gaps/04_problem_finding.md).

    score(q) = P(resolve) x gain x novelty / cost x learning-progress bonus

- Hard gates first (candidates): a question enters only with a test (metric and rung), a threshold and a failure
  condition (tree.add_failure_question sets them, or marks the node `enterable: False`); a question that has had
  `max_rounds_focus` rounds of focus, or was answered, is not pickable again (the budget cap).
- P(resolve): past yield of the question's branch (the top-level part it hangs under) with a Beta(1, 1) prior:
  (1 + resolved) / (2 + tried). Little data stays near 0.5.
- gain: the parent's priority (its share of the idea contexts last round, 1.0 when unknown) times
  (1 + the open child questions the answer would unblock).
- novelty: 1 minus the largest token Jaccard similarity with the questions chosen in earlier rounds.
- cost: the parent's mean build tokens, or the profile's default.
- learning-progress bonus per branch: absolute change of the branch's checked count over the last 2 rounds;
  moving gets up to x1.5, flat for 2 rounds gets x0.8.
- Exploration: every `explore_every`-th round the highest-novelty candidate takes the chosen slot (Hamming's 10%,
  so the formula does not collapse onto cheap questions).
- Upward proposals enter as pseudo-questions with their NEW MEASURE as the test. They are proposals only:
  `requires_human` is True, and nothing here or in the loop changes the success measure.
- A person sees the top 3 (next_questions.json) and may veto ids or choose one through control.json
  (`veto: [ids]`, `choose: id`); the default is to proceed with the top one. The chooser never rewrites a test.
"""
from __future__ import annotations

import re

PRIOR_A, PRIOR_B = 1.0, 1.0          # Beta(1, 1) on the yield per branch
DEFAULT_COST = 8000.0                # build tokens when neither the parent nor the profile gives an estimate
LP_GAIN = 0.5                        # the most the learning-progress bonus adds (x1.5)
LP_FLAT = 0.8                        # a branch flat for 2 rounds
TOP_K = 3

_STOP = {"the", "a", "an", "of", "to", "in", "on", "and", "or", "is", "it", "by", "for", "with", "at", "did", "why",
         "how", "what", "which", "when", "does", "do", "be", "this", "that", "from", "as", "not", "fail"}


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[a-z0-9]+", str(text or "").lower()) if w not in _STOP and len(w) > 1}


def jaccard(a: str, b: str) -> float:
    ta, tb = tokens(a), tokens(b)
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)


def _branch(nodes: list[dict], node_id: str) -> str:
    """The top-level part a node hangs under (path[0] below the root), or the node itself."""
    from nano import tree
    chain = tree._chain(nodes, node_id)
    return chain[-1]["id"] if chain else node_id


def _question_text(n: dict) -> str:
    return f"{n.get('name', '')} {n.get('frame', '')}".strip()


def _past_rounds(history: list[dict]) -> dict[str, int]:
    """Rounds of focus each question id has had (chosen and not vetoed)."""
    out: dict[str, int] = {}
    for rec in history or []:
        ch = rec.get("chosen") or {}
        if ch.get("id"):
            out[ch["id"]] = out.get(ch["id"], 0) + 1
    return out


def candidates(tree_nodes: list[dict], upward: list[dict], history: list[dict] | None = None, *,
               max_rounds_focus: int = 2) -> list[dict]:
    """Enterable question nodes plus upward proposals as pseudo-questions. Dropped (never scored): a question with
    `enterable` False or no test/threshold/fails_if; one answered in an earlier round; one at the focus cap; a
    duplicate upward proposal (same text)."""
    from nano import tree
    history = history or []
    focus = _past_rounds(history)
    answered = {(r.get("chosen") or {}).get("id") for r in history if r.get("answered")}
    out = []
    for n in tree_nodes or []:
        if tree.kind(n) != "question" or not n.get("enterable"):
            continue
        if not n.get("test") or n.get("threshold") is None or not n.get("fails_if"):
            continue
        if n["id"] in answered or focus.get(n["id"], 0) >= max_rounds_focus:
            continue
        out.append({"id": n["id"], "kind": "question", "text": _question_text(n), "node": n["id"],
                    "parent": n.get("parent"), "branch": _branch(tree_nodes, n["id"]),
                    "test": n["test"], "threshold": n["threshold"], "fails_if": n["fails_if"],
                    "requires_human": False, "path": ["goal"] + tree.path(tree_nodes, n["id"]),
                    "path_ids": ["root"] + [k["id"] for k in reversed(tree._chain(tree_nodes, n["id"]))],
                    "open_children": sum(1 for k in tree.children(tree_nodes, n["id"])
                                         if tree.kind(k) == "question" and k["id"] not in answered)})
    seen = set()
    for u in upward or []:
        measure = str(u.get("new_measure") or "").strip()
        text = " ".join(f"{u.get('proposal', '')} {u.get('reframing', '')}".split())
        key = " ".join(tokens(text + " " + measure))
        if not u.get("id") or not measure or key in seen:
            continue
        seen.add(key)
        if u["id"] in answered or focus.get(u["id"], 0) >= max_rounds_focus:
            continue
        out.append({"id": u["id"], "kind": "upward", "text": text, "node": "root", "parent": "root", "branch": "upward",
                    "test": {"metric": measure, "rung": None, "op": "proposed", "what": "a new success measure (proposal only)"},
                    "threshold": "a person approves the new measure; until then the current check decides",
                    "fails_if": "a person rejects the measure, or ideas under it do not move the current check",
                    "requires_human": True, "path": ["goal"], "path_ids": ["root"], "open_children": 0})
    return out


def branch_stats(nodes: list[dict], builds: list[dict], contexts: dict[str, int] | None, history: list[dict] | None,
                 default_cost: float = DEFAULT_COST, round_no: int = 0) -> dict:
    """The inputs `score` reads, from plain records. builds: [{node, round, status, tokens}] (one per built
    candidate); contexts: node id -> idea contexts last round; history: earlier pick records."""
    yield_: dict[str, list[int]] = {}
    tok: dict[str, list[float]] = {}
    per_round: dict[str, dict[int, int]] = {}
    for b in builds or []:
        nid = b.get("node")
        if not nid:
            continue
        br = _branch(nodes, nid)
        y = yield_.setdefault(br, [0, 0])
        y[1] += 1
        if b.get("status") == "checked":
            y[0] += 1
            r = int(b.get("round") or 0)
            d = per_round.setdefault(br, {})
            d[r] = d.get(r, 0) + 1
        if b.get("tokens"):
            tok.setdefault(nid, []).append(float(b["tokens"]))
    picked_up = [r for r in history or [] if (r.get("chosen") or {}).get("kind") == "upward"]
    yield_["upward"] = [sum(1 for r in picked_up if r.get("answered")), len(picked_up)]
    ctx = {k: float(v) for k, v in (contexts or {}).items() if v}
    top = max(ctx.values(), default=0.0)
    progress = {}
    last = max([round_no - 1] + [r for d in per_round.values() for r in d])
    for br in set(per_round) | set(yield_):
        d = per_round.get(br, {})
        progress[br] = [d.get(r, 0) for r in range(1, max(1, last) + 1)]
    asked = [(r.get("round", 0), (r.get("chosen") or {}).get("id"), (r.get("chosen") or {}).get("text", ""))
             for r in history or [] if r.get("chosen")]
    return {"yield": yield_, "share": {k: v / top for k, v in ctx.items()} if top else {},
            "cost": {k: sum(v) / len(v) for k, v in tok.items()}, "default_cost": float(default_cost or DEFAULT_COST),
            "progress": progress, "asked": asked, "round": round_no}


def lp_bonus(series: list[float]) -> tuple[float, str]:
    """Absolute change over the last 2 rounds: moving (either way) earns up to x(1 + LP_GAIN); flat for 2 rounds
    is down-weighted; too little history is neutral."""
    if len(series) < 2:
        return 1.0, "no history"
    ref = series[-3] if len(series) >= 3 else series[0]
    change = abs(series[-1] - ref)
    if change > 0:
        return 1.0 + LP_GAIN * min(1.0, change), f"moving ({ref}->{series[-1]})"
    if len(series) >= 3:
        return LP_FLAT, "flat for 2 rounds"
    return 1.0, "flat for 1 round"


def novelty(q: dict, asked: list) -> float:
    """1 minus the largest token Jaccard with the questions chosen in earlier rounds (its own past picks excluded)."""
    sims = [jaccard(q["text"], t) for _, qid, t in asked or [] if qid != q["id"]]
    return round(1.0 - max(sims, default=0.0), 4)


def score(q: dict, stats: dict) -> dict:
    """The formula, with every factor and a one-line reason kept on the returned copy of q."""
    a, n = (stats.get("yield") or {}).get(q["branch"], [0, 0])
    p = (PRIOR_A + a) / (PRIOR_A + PRIOR_B + n)
    share = (stats.get("share") or {}).get(q.get("parent") or "", None)
    pri = 1.0 if share is None else max(0.05, share)
    gain = pri * (1 + int(q.get("open_children") or 0))
    nov = novelty(q, stats.get("asked") or [])
    cost = (stats.get("cost") or {}).get(q.get("parent") or "") or stats.get("default_cost") or DEFAULT_COST
    lp, lp_why = lp_bonus((stats.get("progress") or {}).get(q["branch"], []))
    s = p * gain * nov / (float(cost) / 1000.0) * lp
    out = dict(q)
    out.update({"score": round(s, 6), "p_resolve": round(p, 4), "gain": round(gain, 4), "novelty": nov,
                "cost": round(float(cost)), "lp_bonus": round(lp, 3),
                "reason": (f"P(resolve) {p:.2f} ({a} of {n} on {q['branch']}, Beta(1,1)); gain {gain:.2f} (priority {pri:.2f}"
                           f" x (1 + {q.get('open_children') or 0} open children)); novelty {nov:.2f}; cost {float(cost):.0f} tokens;"
                           f" learning progress x{lp:.2f} ({lp_why})")})
    return out


def pick(cands: list[dict], round_no: int, explore_every: int = 5, stats: dict | None = None) -> dict:
    """The top 3 by score (cands are scored here when they carry no score yet). On every `explore_every`-th round
    the highest-novelty candidate (an upward proposal wins a tie) takes the first place as the exploration slot."""
    scored = [c if "score" in c else score(c, stats or {}) for c in cands]
    ranked = sorted(scored, key=lambda c: (-c["score"], c["id"]))
    explore = bool(explore_every) and round_no > 0 and round_no % explore_every == 0 and bool(ranked)
    if explore:
        ex = max(ranked, key=lambda c: (c.get("novelty", 0.0), c["kind"] == "upward", c["score"]))
        ranked = [ex] + [c for c in ranked if c is not ex]
    top = []
    for i, c in enumerate(ranked[:TOP_K]):
        slot = "explore" if explore and i == 0 else "score"
        top.append({**c, "rank": i + 1, "slot": slot,
                    "reason": (("exploration round (1 in %d): highest novelty. " % explore_every) if slot == "explore" else "")
                              + c.get("reason", "")})
    return {"round": round_no, "top3": top, "explore": explore, "n_candidates": len(cands)}


def apply_veto(top3: list[dict], control: dict | None) -> dict:
    """control.json `veto: [question ids]` removes picks; `choose: <id>` takes one of the top 3. Default: the top one
    left. Returns {chosen, vetoed, by}."""
    ctl = control or {}
    veto = {str(v) for v in (ctl.get("veto") or [])}
    left = [q for q in top3 or [] if q["id"] not in veto]
    vetoed = [q["id"] for q in top3 or [] if q["id"] in veto]
    want = str(ctl.get("choose") or "")
    chosen = next((q for q in left if want and q["id"] == want), None)
    by = "person" if chosen is not None else "default"
    if chosen is None:
        chosen = left[0] if left else None
        if vetoed and chosen is not None:
            by = "default after veto"
    return {"chosen": chosen, "vetoed": vetoed, "by": by if chosen is not None else "none left"}
