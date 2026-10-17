"""The scorecard: what a run did, as numbers, written as REPORT.md and report.json in the run folder.

Funnel: sketches -> clusters -> tagged new / known / failed / obvious -> interrogated -> built ->
each rung -> checked -> long-run ranked -> overnight verdicts. Plus cost, time, idea sources (own vs
web), per-card and per-part outcomes, prediction accuracy where predictions were checkable, the
upward proposals, and a novelty note per verified winner (the closest known technique from the
brief match). `--runs A B ...` writes a comparison table across runs (arms, ablations).

Usage: python -m nano.report --run <folder>      or      python -m nano.report --runs <f1> <f2> ... --out compare.md
"""
from __future__ import annotations

import argparse
import json
import time
from collections import Counter
from pathlib import Path


def _json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return default


def _jsonl(p: Path) -> list[dict]:
    out = []
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        try:
            out.append(json.loads(line))
        except Exception:  # noqa: BLE001
            pass
    return out


def collect(run: Path) -> dict:
    state = _json(run / "state.json", {})
    answer = _json(run / "answer.json", {})
    ideas = _jsonl(run / "ideas.jsonl")
    icl = _json(run / "idea_clusters.json", {}).get("clusters", [])
    deepen = _json(run / "deepen.json", {}).get("nodes", [])
    cands = [r for f in sorted((run / "cands").glob("*.jsonl")) for r in _jsonl(f)] if (run / "cands").exists() else []
    verify = {}
    for v in _jsonl(run / "verify.jsonl"):
        verify[v["id"]] = v                            # the last row per id wins (long-run rows update)
    pool = [_json(p, {}) for p in sorted((run / "pool").glob("*.json"))] if (run / "pool").exists() else []
    rung5 = _json(run / "rung5" / "results.json", {})
    calls = [_json(p, {}) for p in (run / "calls").glob("*.json")] if (run / "calls").exists() else []
    briefs = {p.stem: _json(p, {}) for p in (run / "research").glob("*.json")} if (run / "research").exists() else {}

    tokens = sum((c.get("total_tokens") or (c.get("usage") or {}).get("total_tokens") or 0) for c in calls)
    main_model = state.get("model")
    tokens_main = sum((c.get("total_tokens") or (c.get("usage") or {}).get("total_tokens") or 0) for c in calls
                      if (c.get("model") or main_model) == main_model)
    cost = sum((c.get("cost_usd") or 0) for c in calls)
    by_role = Counter()
    for c in calls:
        by_role[(c.get("meta") or {}).get("card", c.get("role", "?"))] += 1
    src = Counter("web" if str(s.get("source", "own")).startswith("http") else "own" for s in ideas)
    by_card = Counter(s.get("card", "?") for s in ideas)
    tags = Counter(c.get("prior", "unknown") for c in icl)
    obvious = sum(1 for c in icl if c.get("obvious"))
    gens = Counter(n.get("gen", 0) for n in deepen)
    offshoots = sum(len(n.get("offshoots", [])) for n in deepen)
    facts = sum(len(n.get("known", [])) for n in deepen)
    dropped = sum(n.get("dropped_unsourced", 0) for n in deepen)
    built = [c for c in cands if c.get("id")]
    parse_failed = sum(1 for c in cands if c.get("parse_failed"))
    dup_ids = {r.get("members", [None])[0] for r in _jsonl(run / "clusters.jsonl") if r.get("rule") == "source_hash"}
    rung_hist = Counter()
    for c in built:
        v = verify.get(c["id"])
        if not v:
            rung_hist["duplicate" if c["id"] in dup_ids else "unverified"] += 1
            continue
        if v.get("status") == "checked":
            rung_hist["checked"] += 1
        else:
            rung_hist[f"fail@{(v.get('feedback_record') or {}).get('rung', v.get('details', {}).get('rung_reached'))}"] += 1
    checked = [c for c in built if verify.get(c["id"], {}).get("status") == "checked"]
    by_card_built = Counter(c.get("card", "?").split(":")[0] for c in built)
    by_card_checked = Counter(c.get("card", "?").split(":")[0] for c in checked)
    by_part_built = Counter((c.get("extra") or {}).get("node", "?") for c in built)
    by_part_checked = Counter((c.get("extra") or {}).get("node", "?") for c in checked)
    pool_rows = []
    for p in pool:
        m = p.get("metrics") or {}
        pool_rows.append({"id": p.get("id"), "part": p.get("node"), "card": p.get("card"), "arm": p.get("arm", "scaffold"),
                          "learn_z": m.get("learn_z"), "long_z": m.get("long_z"), "trend": m.get("trend"),
                          "extrap_z": m.get("extrap_z"), "step_ratio": m.get("step_ratio"), "param_ratio": m.get("param_ratio"),
                          "hypothesis": p.get("hypothesis")})
    pool_rows.sort(key=lambda r: (r["extrap_z"] is None, r["extrap_z"] or 0.0))
    # verdicts
    verdicts = {}
    if rung5.get("candidates"):
        for cid, s in rung5["candidates"].items():
            verdicts[cid] = {"status": s.get("status"), "n": s.get("n"), "mean": s.get("mean"), "delta": s.get("delta"),
                             "p": s.get("p"), "hypothesis": s.get("hypothesis"), "part": s.get("node")}
    # novelty note per verified winner: the brief entry it matched, if any
    novelty = []
    cl_by_rep = {}
    for c in icl:
        for mid in c.get("members", []):
            cl_by_rep[mid] = c
    for cid, v in verdicts.items():
        if v["status"] != "verified":
            continue
        cand = next((c for c in built if c["id"] == cid), {})
        cl_name = (cand.get("extra") or {}).get("cluster")
        cl = next((c for c in icl if c.get("name") == cl_name), {})
        novelty.append({"id": cid, "hypothesis": v["hypothesis"], "tag": cl.get("prior", "unknown"),
                        "closest_known": cl.get("prior_match"), "obvious": cl.get("obvious", False),
                        "source": cl.get("prior_source")})
    controls = _json(run / "controls.json", {})
    discovery = _json(run / "discovery.json", {}).get("rounds", [])
    lanes = {}
    for p in pool:
        lane = p.get("lane", "main")
        d = lanes.setdefault(lane, {"pooled": 0, "verified": 0, "stackable": 0})
        d["pooled"] += 1
        st = (rung5.get("candidates", {}).get(p.get("id"), {}) or {}).get("status")
        if st in ("verified", "stackable"):
            d[st] += 1
    # critique: objections typed and resolved by the ladder; the critic's hit rate among the resolvable ones
    crit = Counter()
    by_cls = {}
    for v in verify.values():
        for o in ((v.get("details") or {}).get("metrics") or {}).get("objections") or []:
            st = o.get("status") or "pending"
            crit[st] += 1
            c = o.get("cls") or "untyped"
            by_cls.setdefault(c, Counter())[st] += 1
    n_obj = sum(len(n.get("objections") or []) for n in deepen)
    critique = {"objections": n_obj, "resolvable": sum(1 for n in deepen for o in (n.get("objections") or []) if o.get("if_true")),
                "confirmed": crit["confirmed"], "refuted": crit["refuted"], "pending": crit["pending"], "untestable": crit["untestable"],
                "by_class": {k: dict(v) for k, v in by_cls.items()}} if n_obj else None
    commitments = _json(run / "commitments.json", {}) or None
    control_changes = len(_jsonl(run / "control_log.jsonl"))
    sel = _jsonl(run / "selection.jsonl")
    selection = dict(Counter(r.get("reason") for r in sel)) if sel else None
    repro = []
    for cid, v in (rung5.get("candidates") or {}).items():
        if v.get("status") in ("verified", "stackable"):
            pm = next((p for p in pool if p.get("id") == cid), {})
            repro.append({"id": cid, "status": v.get("status"), "src_hash": pm.get("src_hash"), "changed": (pm.get("metrics") or {}).get("changed_symbols"),
                          "closest_known": next((n.get("closest_known") for n in novelty if n.get("id") == cid), None),
                          "command": f"python -m nano.batch_verify --run {run} --only {cid}"})
    tuning = _json(run / "tuning.json", {}) or None
    if tuning is not None:
        tuning["model_tune_sketches"] = sum(1 for s in ideas if s.get("kind") == "tune")
    # anomalies: how many were flagged, how many sketches aimed at one, and whether the sham row was chased
    anomalies = None
    an = _json(run / "anomalies.json", {})
    if an:
        from nano import anomaly as _an
        sham = _json(run / "private" / "anomaly_sham.json", {}) or None
        anomalies = {"flagged": len(an.get("anomalies") or []), "n_cells": an.get("n_cells"), "n_seeds": an.get("n_seeds"),
                     "cells": [a.get("cell") for a in (an.get("anomalies") or [])],
                     "aimed": _an.aimed(ideas, an.get("anomalies") or []), "sham": bool(sham), "sham_chased": _an.chased(ideas, sham)}
    # the ambitious lane, by counts: sketches, clusters, builds, checked and verified, per operator
    leap_ideas = [s for s in ideas if s.get("kind") == "leap"]
    leap_clusters = [c for c in icl if float(c.get("leap_share") or 0) >= 0.5]
    leap_built = [c for c in built if (c.get("extra") or {}).get("kind") == "leap"]
    leap_checked = [c for c in leap_built if (verify.get(c["id"]) or {}).get("status") == "checked"]
    leap_verified = [c for c in leap_built if (rung5.get("candidates", {}).get(c["id"], {}) or {}).get("status") in ("verified", "stackable")]
    by_op = {}
    for s in leap_ideas:
        by_op.setdefault(s.get("leap_op") or "?", {"sketches": 0, "built": 0, "checked": 0, "verified": 0})["sketches"] += 1
    for c in leap_built:
        o = by_op.setdefault((c.get("extra") or {}).get("leap_op") or "?", {"sketches": 0, "built": 0, "checked": 0, "verified": 0})
        o["built"] += 1
        o["checked"] += 1 if c in leap_checked else 0
        o["verified"] += 1 if c in leap_verified else 0
    leaps = {"sketches": len(leap_ideas), "of_sketches": len(ideas), "clusters": len(leap_clusters), "built": len(leap_built),
             "checked": len(leap_checked), "verified": len(leap_verified), "by_op": by_op} if ideas else None
    fidelity = [v["details"]["metrics"].get("fidelity") for v in verify.values()
                if (v.get("details") or {}).get("metrics", {}).get("fidelity")]
    fid_checkable = [f for f in fidelity if f.get("checkable")]
    metric_blind = sum(1 for c in built if (c.get("extra") or {}).get("metric_blind"))
    # prediction accuracy (filled by the prediction tracker when present)
    preds = [v.get("prediction_check") for v in verify.values() if v.get("prediction_check")]
    pred_acc = None
    if preds:
        checkable = [p for p in preds if p.get("checkable")]
        if checkable:
            pred_acc = {"checkable": len(checkable), "within_tolerance": sum(1 for p in checkable if p.get("ok"))}
    return {"run": run.name, "arm": state.get("arm", "scaffold"), "model": state.get("model"), "backend": state.get("backend"),
            "baseline_version": state.get("baseline_version", "v1"), "lens": state.get("lens"),
            "lens_design": state.get("lens_design"), "budget": state.get("B"), "tokens": tokens, "tokens_main": tokens_main, "tokens_aux": tokens - tokens_main,
            "cost_usd": round(cost, 2), "wall_s": answer.get("wall_s"),
            "calls": sum(by_role.values()), "calls_by_card": dict(by_role),
            "sketches": len(ideas), "sketch_sources": dict(src), "sketches_by_card": dict(by_card),
            "clusters": len(icl), "tags": dict(tags), "obvious": obvious,
            "interrogation": {"calls": len(deepen), "by_generation": dict(gens), "offshoots": offshoots, "facts": facts,
                              "unsourced_dropped": dropped},
            "built": len(built), "parse_failed": parse_failed, "rungs": dict(rung_hist), "checked": len(checked),
            "built_by_card": dict(by_card_built), "checked_by_card": dict(by_card_checked),
            "built_by_part": dict(by_part_built), "checked_by_part": dict(by_part_checked),
            "cost_per_checked": round(cost / len(checked), 2) if checked and cost else None,
            "pool": pool_rows, "verdicts": verdicts, "verified": sum(1 for v in verdicts.values() if v["status"] == "verified"),
            "novelty": novelty, "prediction_accuracy": pred_acc,
            "controls": controls, "discovery": discovery, "lanes": lanes, "metric_blind_built": metric_blind, "leaps": leaps,
            "anomalies": anomalies, "tuning": tuning, "critique": critique,
            "commitments": {"hash": state.get("commitments_hash"), "budget": (commitments or {}).get("budget"), "win": (commitments or {}).get("win"),
                            "slots": (commitments or {}).get("slots"), "models": (commitments or {}).get("models"), "baseline_hash": (commitments or {}).get("baseline_hash"),
                            "control_changes": control_changes} if commitments else None,
            "selection": selection, "reproduction": repro, "run_dir": str(run),
            "fidelity": {"checkable": len(fid_checkable), "held": sum(1 for f in fid_checkable if f.get("ok"))} if fidelity else None,
            "upward": answer.get("upward_proposals", []), "briefs": {k: {"known": len(b.get("known", [])), "failed": len(b.get("failed", [])),
                                                                         "open": len(b.get("open", [])), "source": b.get("source")} for k, b in briefs.items()},
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S")}


def _pct(a: int, b: int) -> str:
    return f"{100.0 * a / b:.0f}%" if b else "-"


GLOSSARY = [("learn z", "the loss gap to the original at 45 training steps, in units of the seed-to-seed spread; negative is better"),
            ("long z", "the same gap at 240 steps"), ("extrap z", "the long gap projected forward along its trend; the pool is ranked by it"),
            ("step ratio", "candidate step time over the original's; the cap is 2"), ("lane", "main = chosen by score; longshot = the ambitious lane; family = a variant of a near miss; tune = a scripted constant change"),
            ("rung", "the ladder of cheap checks: 0 boundary, 1 build and reach, 2 timing, 3 learning, 4 long comparison; 5 is the overnight exam")]


def newcomer_brief(d: dict) -> list[str]:
    """The page a newcomer reads first: result, trust, what it needs from you, next action, glossary. Numbers only."""
    pool = d.get("pool") or []
    best = pool[0] if pool else None
    L = ["## Read this first", ""]
    L.append(f"**Result.** {d['checked']} of {d['built']} builds passed the cheap checks; {d['verified']} verified overnight so far"
             + (f". Best projected gap: `{best['id']}` ({best.get('part')}, {best.get('card')}), extrapolated z {best.get('extrap_z')}: {str(best.get('hypothesis', ''))[:120]}" if best else ".")
             + f" Cost: {d['tokens_main']:,} tokens of the inventing model (the budgeted part) plus {d['tokens_aux']:,} of the cheap model's retrieval and clerical work, ${d['cost_usd']}, {d.get('wall_s') or 0:.0f} s.")
    trust = []
    if d.get("controls"):
        okc = sum(1 for v in d["controls"].values() if v.get("ok"))
        trust.append(f"controls {okc}/{len(d['controls'])} behaved")
    pa = d.get("prediction_accuracy") or {}
    if pa.get("checkable"):
        trust.append(f"predictions held {pa['within_tolerance']}/{pa['checkable']}")
    if d.get("fidelity"):
        trust.append(f"named measurements moved {d['fidelity']['held']}/{d['fidelity']['checkable']}")
    cr = d.get("critique") or {}
    if cr and (cr.get("confirmed", 0) + cr.get("refuted", 0)):
        trust.append(f"the critic was right {100 * cr['confirmed'] / (cr['confirmed'] + cr['refuted']):.0f}% of the time it could be checked")
    an = d.get("anomalies") or {}
    if an.get("sham"):
        trust.append(f"the fabricated anomaly row was chased by {an['sham_chased']} sketches")
    cm = d.get("commitments") or {}
    if cm.get("hash"):
        trust.append(f"commitments hash {cm['hash']}, {cm.get('control_changes', 0)} control-file changes")
    L.append("**Can I trust this?** " + ("; ".join(trust) + "." if trust else "no controls or predictions recorded."))
    needs = []
    if not d.get("verdicts"):
        n_pool = len(pool)
        needs.append(f"Run the overnight verdict on the {n_pool} pooled scripts: `python -m nano.batch_verify --run {d.get('run_dir')} --baseline-seeds 5`; "
                     f"about {31 * (3 * n_pool + 5) / 60:.1f} GPU hours if every candidate goes to three seeds.")
    elif d.get("verified"):
        needs.append("Promote a verified winner to become the new original: `python -m nano.promote`.")
    needs.append("You can seed the ambitious lane yourself: a JSON list of {part, text} at memory/owner_seeds.json.")
    L.append("**What it needs from you.** " + " ".join(needs))
    L.append("**Glossary.** " + "; ".join(f"*{k}*: {v}" for k, v in GLOSSARY) + ".")
    L.append("")
    return L


def markdown(d: dict) -> str:
    L = [f"# Run report: {d['run']}", "",
         f"arm **{d['arm']}** · model {d['model']} via {d['backend']} · baseline {d['baseline_version']}"
         + (f" · map lens {d['lens']}" if d.get("lens") else "") + f" · {d['ts']}", ""]
    L += newcomer_brief(d)
    L += ["## The funnel", "", "| stage | count | of previous |", "|---|---|---|",
         f"| model calls | {d['calls']} | |",
         f"| sketches | {d['sketches']} | own {d['sketch_sources'].get('own', 0)} / web {d['sketch_sources'].get('web', 0)} |",
         f"| clusters | {d['clusters']} | {_pct(d['clusters'], d['sketches'])} |",
         f"| tagged new | {d['tags'].get('new', 0)} | {_pct(d['tags'].get('new', 0), d['clusters'])} |",
         f"| tagged known / known failure | {d['tags'].get('known', 0)} / {d['tags'].get('failed', 0)} | |",
         f"| matching the private obvious answers | {d['obvious']} | {_pct(d['obvious'], d['clusters'])} |",
         f"| interrogation calls | {d['interrogation']['calls']} | gens {d['interrogation']['by_generation']}; {d['interrogation']['offshoots']} new ideas, {d['interrogation']['facts']} facts, {d['interrogation']['unsourced_dropped']} unsourced numbers dropped |",
         f"| built | {d['built']} | parse failures {d['parse_failed']} |",
         f"| checked (rungs 0-3) | {d['checked']} | {_pct(d['checked'], d['built'])}; failures {d['rungs']} |",
         f"| verified overnight | {d['verified']} | of {len(d['verdicts'])} examined |", "",
         "## Cost", "", f"inventing model {d['tokens_main']:,} tokens of budget {d['budget']}; cheap model {d['tokens_aux']:,} more for retrieval and clerical calls, outside the budget (a web search re-reads its pages on every turn); cost ${d['cost_usd']}"
         + (f"; ${d['cost_per_checked']} per checked candidate" if d.get("cost_per_checked") else "")
         + (f"; wall {d['wall_s']} s" if d.get("wall_s") else ""), ""]
    L += ["## By card and by part", "", "| card | built | checked |", "|---|---|---|"]
    for k in sorted(set(d["built_by_card"]) | set(d["checked_by_card"])):
        L.append(f"| {k} | {d['built_by_card'].get(k, 0)} | {d['checked_by_card'].get(k, 0)} |")
    L += ["", "| part | built | checked |", "|---|---|---|"]
    for k in sorted(set(d["built_by_part"]) | set(d["checked_by_part"])):
        L.append(f"| {k} | {d['built_by_part'].get(k, 0)} | {d['checked_by_part'].get(k, 0)} |")
    L += ["", "## Pool (ranked by the extrapolated long-run gap in seed spreads; negative is better)", "",
          "| id | part | card | learn z | long z | trend | extrap z | step ratio | params | hypothesis |", "|---|---|---|---|---|---|---|---|---|---|"]
    for r in d["pool"]:
        L.append(f"| {r['id']} | {r['part']} | {r['card']} | {r['learn_z']} | {r['long_z']} | {r['trend']} | {r['extrap_z']} | {r['step_ratio']} | {r['param_ratio']} | {(r['hypothesis'] or '')[:100]} |")
    if d["verdicts"]:
        L += ["", "## Overnight verdicts", "", "| id | part | seeds | mean | delta | p | status | hypothesis |", "|---|---|---|---|---|---|---|---|"]
        for cid, v in sorted(d["verdicts"].items(), key=lambda kv: (kv[1]["mean"] is None, kv[1]["mean"] or 9)):
            L.append(f"| {cid} | {v['part']} | {v['n']} | {v['mean']} | {v['delta']} | {v['p']} | **{v['status']}** | {(v['hypothesis'] or '')[:100]} |")
    if d["novelty"]:
        L += ["", "## Novelty of the verified winners", ""]
        for n in d["novelty"]:
            L.append(f"- {n['id']}: tagged **{n['tag']}**" + (f", closest known: {n['closest_known']}" if n.get("closest_known") else "")
                     + (" (one of the obvious first answers)" if n.get("obvious") else "") + f" — {n['hypothesis']}")
    if d.get("prediction_accuracy"):
        pa = d["prediction_accuracy"]
        L += ["", f"## Predictions: {pa['within_tolerance']} of {pa['checkable']} checkable predictions were within tolerance", ""]
    if d.get("fidelity"):
        L += ["", f"## Fidelity: {d['fidelity']['held']} of {d['fidelity']['checkable']} named diagnostic targets moved as the sketch said", ""]
    if d.get("controls"):
        L += ["", "## Controls (the run's own false-positive rate and power)", ""]
        for k, v in d["controls"].items():
            L.append(f"- {k}: {'ok' if v.get('ok') else ('PROBLEM' if v.get('ok') is False else 'n/a')}: {v.get('note')}")
    if d.get("lanes"):
        L += ["", "## Lanes", "", "| lane | pooled | verified | stackable |", "|---|---|---|---|"]
        for k, v in d["lanes"].items():
            L.append(f"| {k} | {v['pooled']} | {v['verified']} | {v['stackable']} |")
    if d.get("commitments"):
        cm = d["commitments"]
        L += ["", "## Commitments (fixed before any idea existed)", "",
              f"hash {cm.get('hash')}; baseline {cm.get('baseline_hash')}; budget {cm.get('budget'):,} tokens; win rule {cm.get('win')}; slots {cm.get('slots')}; "
              f"models {cm.get('models')}; control-file changes during the run: {cm.get('control_changes', 0)}."]
    if d.get("selection"):
        L += ["", "## Selection (why groups were chosen or dropped)", "", "| reason | groups |", "|---|---|"]
        for k, v in sorted(d["selection"].items(), key=lambda kv: -kv[1]):
            L.append(f"| {k} | {v} |")
        L.append("Per-group rows with scores, cuts and lane propensities are in selection.jsonl.")
    if d.get("reproduction"):
        L += ["", "## Reproduction cards", ""]
        for r in d["reproduction"]:
            L.append(f"- `{r['id']}` ({r['status']}): script hash {r.get('src_hash')}; changed {r.get('changed')}; closest known technique: {r.get('closest_known') or 'none found'}; rerun: `{r['command']}`")
    if d.get("critique"):
        cr = d["critique"]
        n_res = cr["confirmed"] + cr["refuted"]
        L += ["", "## Critique (pre-mortem objections, resolved by the ladder)", "",
              f"{cr['objections']} objections raised, {cr['resolvable']} with a measurable test; on built ideas {cr['confirmed']} confirmed, "
              f"{cr['refuted']} refuted, {cr['pending']} pending, {cr['untestable']} untestable"
              + (f"; the critic was right {100 * cr['confirmed'] / n_res:.0f}% of the time it could be checked." if n_res else ".")]
        if cr.get("by_class"):
            L += ["", "| class | confirmed | refuted | pending | untestable |", "|---|---|---|---|---|"]
            for k, v in sorted(cr["by_class"].items()):
                L.append(f"| {k} | {v.get('confirmed', 0)} | {v.get('refuted', 0)} | {v.get('pending', 0)} | {v.get('untestable', 0)} |")
    if d.get("tuning"):
        tn = d["tuning"]
        L += ["", "## Tuning (single-knob moves by script, up the same ladder)", "",
              f"{len(tn.get('knobs', []))} knobs swept; kept for the long run: {', '.join(tn.get('kept', [])) or 'none'}; "
              f"tuning ideas from the agents: {tn.get('model_tune_sketches', 0)}.", "",
              "| knob | change | ladder | learn z | kept |", "|---|---|---|---|---|"]
        for r in sorted(tn.get("knobs", []), key=lambda r: (r.get("learn_z") if r.get("learn_z") is not None else 99)):
            L.append(f"| {r['knob']} | {r['field']} {r['old']:g} -> {r['new']:g} | {r['status']} (rung {r['rung']}) | {r['learn_z']} | {'yes' if r['kept'] else ''} |")
    if d.get("anomalies"):
        an = d["anomalies"]
        L += ["", "## Anomalies (measured cells off their family's trend, replicated across seeds)", "",
              f"{an['flagged']} flagged of {an['n_cells']} cells on {an['n_seeds']} seeds ({', '.join(an['cells']) or 'none'}); "
              f"{an['aimed']} sketches aimed at one. Sham row present: {'yes' if an['sham'] else 'no'}"
              + (f"; chased by {an['sham_chased']} sketches." if an["sham"] else ".")]
    if d.get("leaps"):
        lp = d["leaps"]
        L += ["", "## Leaps (the ambitious lane, by counts)", "",
              f"{lp['sketches']} of {lp['of_sketches']} sketches were leaps; {lp['clusters']} leap clusters; built {lp['built']}, checked {lp['checked']}, verified or stackable {lp['verified']}.",
              "", "| operator | sketches | built | checked | verified |", "|---|---|---|---|---|"]
        for op, v in sorted(lp["by_op"].items(), key=lambda kv: -kv[1]["sketches"]):
            L.append(f"| {op} | {v['sketches']} | {v['built']} | {v['checked']} | {v['verified']} |")
    if d.get("discovery"):
        L += ["", "## Discovery curve", "", "| round | contexts | sketches | new clusters | per context | top-2 share |", "|---|---|---|---|---|---|"]
        for r in d["discovery"]:
            L.append(f"| {r['round']} | {r['contexts']} | {r['sketches']} | {r['new_clusters']} | {r['new_per_context']} | {r['top2_share']} |")
    if d.get("metric_blind_built"):
        L += ["", f"Built ideas whose benefit lies outside this exam (metric-blind): {d['metric_blind_built']}", ""]
    if d["upward"]:
        L += ["", "## Proposals to reframe the problem (logged, not built)", ""] + [f"- {u.get('idea')}: {u.get('mechanism')}" for u in d["upward"][:10]]
    return "\n".join(L) + "\n"


def compare(runs: list[Path]) -> str:
    rows = [collect(r) for r in runs]
    L = ["# Comparison across runs", "", "| run | arm | lens | calls | tokens | cost $ | sketches | new | obvious | built | checked | verified | $ per checked |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in rows:
        L.append(f"| {d['run']} | {d['arm']} | {d.get('lens') or ''} | {d['calls']} | {d['tokens']:,} | {d['cost_usd']} | {d['sketches']} | "
                 f"{d['tags'].get('new', 0)} | {d['obvious']} | {d['built']} | {d['checked']} | {d['verified']} | {d.get('cost_per_checked') or ''} |")
    return "\n".join(L) + "\n"


def write(run: Path) -> dict:
    d = collect(run)
    (run / "report.json").write_text(json.dumps(d, indent=1), encoding="utf-8")
    (run / "REPORT.md").write_text(markdown(d), encoding="utf-8")
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", default=None)
    ap.add_argument("--runs", nargs="*", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.runs:
        text = compare([Path(r) for r in a.runs])
        if a.out:
            Path(a.out).write_text(text, encoding="utf-8")
        print(text)
        return 0
    if not a.run:
        ap.error("--run or --runs")
    d = write(Path(a.run))
    print((Path(a.run) / "REPORT.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
