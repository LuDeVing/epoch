"""Critic calibration on planted flaws.

Five mutants of the baseline, each with a known failure class, plus the known winners and the placebo, go
through the pre-mortem blind (the critic sees an honest proposal and the baseline script, not the label).
The critic is scored on: recall of the planted class among its high or medium objections, the severity gap
between mutants and winners, and false alarms on the placebo. A critic with no gap is annotation, not evidence.
With --ladder, every mutant also goes up the ladder, as a mutation test of the rungs. Run once per baseline
version and critic model, about ten calls:

    python -m nano.critic_check --model fable --backend cli_json

Design: research_notes/thinking_parts/07_critique.md (C4); creative_genius/00_SYNTHESIS.md.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

_labroot.lab_root()
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nano.ideate import PF, fill  # noqa: E402  (PF: nano/profile.py, or the shim with the LLM defaults in ideate.py)
from harness import labroot as _labroot  # noqa: E402  (the lab folder, on any computer)

HERE = Path(__file__).resolve().parent
BASELINE = HERE / "train.py"                 # the LLM profile's artifact; main() reads the active profile's
SEV = {"high": 2, "medium": 1, "low": 0}

# name: (planted classes that count as a hit, the honest proposal the critic sees, the edits)
# These edits are written against the LLM baseline (nano/train.py); on another profile's artifact the anchors do not
# match and build_mutants() leaves them out, so the calibration runs on whatever mutants apply.
MUTANTS = {
    "hidden_cost": ({"hidden_cost"},
                    "Add a learned full-width linear mixing of the residual stream at the end of every block, initialised to the identity, so each block can re-mix channels before the next one.",
                    [("        self.attn, self.mlp = Attention(cfg), MLP(cfg)",
                      "        self.attn, self.mlp = Attention(cfg), MLP(cfg)\n        self.extra = nn.Linear(cfg.d_model, cfg.d_model, bias=False)\n        nn.init.eye_(self.extra.weight)"),
                     ("        return self.combine(x, branch, 1)", "        return self.extra(self.combine(x, branch, 1))")]),
    "early_only": ({"early_only"},
                   "Remove the learning-rate cooldown entirely so the model keeps learning at full speed to the end of the budget instead of coasting through the last third.",
                   [("    cooldown_frac: float = 0.30", "    cooldown_frac: float = 0.0")]),
    "silent_noop": ({"impl_slip"},
                    "Add a per-block gate that scales the attention branch, stored on the block, so the optimiser can learn how much each layer relies on attention.",
                    [("        self.attn, self.mlp = Attention(cfg), MLP(cfg)", "        self.attn, self.mlp = Attention(cfg), MLP(cfg)\n        self.attn_gate = 1.0")]),
    "below_noise": ({"below_noise"},
                    "Raise the initialisation scale of the two residual output projections by five percent so the residual branches start slightly stronger.",
                    [("            nn.init.normal_(b.attn.wo.weight, std=0.02 / math.sqrt(2 * cfg.n_layer))",
                      "            nn.init.normal_(b.attn.wo.weight, std=0.021 / math.sqrt(2 * cfg.n_layer))"),
                     ("            nn.init.normal_(b.mlp.w_down.weight, std=0.02 / math.sqrt(2 * cfg.n_layer))",
                      "            nn.init.normal_(b.mlp.w_down.weight, std=0.021 / math.sqrt(2 * cfg.n_layer))")]),
    "wrong_scale": ({"interaction_cancels", "impl_slip", "breaks_constraint"},
                    "Halve the attention branch's contribution to the residual stream in every block, to keep the residual norm from growing with depth.",
                    [("        branch = self.attn(self.n1((x * weights[None, None, :, None]).sum(2)), cos, sin)",
                      "        branch = 0.5 * self.attn(self.n1((x * weights[None, None, :, None]).sum(2)), cos, sin)")]),
}


def build_mutants(src: str) -> dict[str, dict]:
    out = {}
    for name, (classes, proposal, edits) in MUTANTS.items():
        s = src
        ok = True
        for old, new in edits:
            if s.count(old) != 1:
                ok = False
                break
            s = s.replace(old, new, 1)
        if ok:
            out[name] = {"source": s, "proposal": proposal, "classes": set(classes), "kind": "mutant"}
    return out


def score(results: list[dict]) -> dict:
    """results: [{"name", "kind": mutant|winner|placebo, "classes": set, "objections": [{"severity", "cls"}]}]."""
    def sev_mean(objs):
        return sum(SEV.get(o.get("severity"), 1) for o in objs) / len(objs) if objs else 0.0

    def sev_max(objs):
        return max((SEV.get(o.get("severity"), 1) for o in objs), default=0)
    mut = [r for r in results if r["kind"] == "mutant"]
    win = [r for r in results if r["kind"] == "winner"]
    pla = [r for r in results if r["kind"] == "placebo"]
    hits = []
    for r in mut:
        flagged = {o.get("cls") for o in r["objections"] if o.get("severity") in ("high", "medium")}
        hits.append({"name": r["name"], "hit": bool(flagged & set(r["classes"])), "flagged": sorted(c for c in flagged if c)})
    recall = sum(1 for h in hits if h["hit"]) / len(hits) if hits else None
    # precision: of the classes the critic flags on a mutant, how many were planted (a critic that flags everything scores low)
    flagged_all = sum(len(h["flagged"]) for h in hits)
    precision = (sum(1 for h, r in zip(hits, mut) for c in h["flagged"] if c in set(r["classes"])) / flagged_all) if flagged_all else None
    gap = (sum(sev_max(r["objections"]) for r in mut) / len(mut) - sum(sev_max(r["objections"]) for r in win) / len(win)) if mut and win else None
    false_alarms = sum(1 for r in pla for o in r["objections"] if o.get("severity") == "high")
    verdict = ("useful" if (recall or 0) >= 0.6 and (gap or 0) > 0.3 and false_alarms <= 1
               else ("weak" if (recall or 0) >= 0.4 else "annotation only"))
    return {"recall": recall, "precision": round(precision, 2) if precision is not None else None, "hits": hits, "severity_gap": round(gap, 2) if gap is not None else None,
            "placebo_high_objections": false_alarms, "mean_severity": {r["name"]: round(sev_mean(r["objections"]), 2) for r in results},
            "verdict": verdict}


def baseline_path() -> Path:
    """The active profile's baseline artifact (repo-relative path in profile.artifact), else nano/train.py."""
    art = getattr(PF.current(), "artifact", None) or {}
    rel = art.get("path") if isinstance(art, dict) else None
    if rel:
        p = HERE.parent / rel
        if p.exists():
            return p
    return BASELINE


def constraints_list() -> list[str]:
    """The active profile's hard constraints; the loop's CONSTRAINTS when the profile has none."""
    cons = list(getattr(PF.current(), "constraints", None) or [])
    if not cons:
        try:
            from nano.loop import CONSTRAINTS
            cons = list(CONSTRAINTS)
        except Exception:  # noqa: BLE001
            cons = []
    return cons


def main() -> int:
    from harness import llm
    from nano import controls, deepen
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="fable")
    ap.add_argument("--backend", default="cli_json")
    ap.add_argument("--out", default=None)
    ap.add_argument("--ladder", action="store_true", help="also send each mutant up the ladder (GPU) as a mutation test of the rungs")
    a = ap.parse_args()
    src = baseline_path().read_text(encoding="utf-8")
    cases = build_mutants(src)
    ctl = controls.build(src)
    for name, kind in (("zero_init_proj", "winner"), ("relu2_mlp", "winner"), ("placebo_order", "placebo")):
        if ctl.get(name, {}).get("source"):
            cases[name] = {"source": ctl[name]["source"], "proposal": ctl[name]["hypothesis"].replace("control: ", ""), "classes": set(), "kind": kind}
    constraints = "\n".join(f"- {c}" for c in constraints_list())
    if not cases:
        print("[critic] no planted flaw applies to this profile's baseline; nothing to calibrate", flush=True)
        return 1
    out_dir = Path(a.out) if a.out else Path(os.environ["HTSA_LAB_ROOT"]) / "memory" / "critic"
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for name, c in cases.items():
        brief = (f"IDEA: {name.replace('_', ' ')}\nMECHANISM: {c['proposal']}\n"
                 + fill("PREDICTION: {v:score_phrase}\nTEST: {v:first_check} against the original"))
        prompt = deepen.premortem_prompt(brief, fill("the whole {v:recipe}"), constraints, src, [])
        r = llm.call(prompt, role="generate", call_id=f"critic_{name}_{int(time.time())}", model=a.model, max_tokens=2500,
                     backend=a.backend, log_dir=out_dir / "calls", meta={"card": "critic_check", "operator": name})
        pm = deepen.parse_premortem(r.text or "")
        results.append({"name": name, "kind": c["kind"], "classes": sorted(c["classes"]), "objections": pm["objections"], "verdict": pm["verdict"],
                        "tokens": r.usage.total_tokens})
        print(f"[critic] {name:14s} {c['kind']:8s} objections {len(pm['objections'])} classes {sorted({o.get('cls') for o in pm['objections'] if o.get('cls')})}", flush=True)
    sc = score([{**r, "classes": set(r["classes"])} for r in results])
    if a.ladder:
        from nano import check as C
        prof_p = Path(os.environ["HTSA_LAB_ROOT"]) / "runs" / "nano_baseline_profile" / "baseline_profile.json"
        prof = json.loads(prof_p.read_text(encoding="utf-8"))
        kill = {}
        for name, c in cases.items():
            if c["kind"] != "mutant":
                continue
            p = out_dir / "mutants" / f"{name}.py"
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(c["source"], encoding="utf-8")
            rec = C.check(p, out_dir / "ladder" / name, prof, rung_max=3, baseline_src=src, boundary=None)
            kill[name] = {"status": rec["status"], "rung": rec["rung_reached"], "reason": (rec.get("feedback") or {}).get("reason", "")[:120]}
            print(f"[ladder] {name:14s} -> {rec['status']} at rung {rec['rung_reached']}", flush=True)
        sc["ladder"] = kill
    report = {"model": a.model, "backend": a.backend, "ts": time.strftime("%Y-%m-%dT%H:%M:%S"), "results": results, "score": sc}
    (out_dir / f"{a.model}.json").write_text(json.dumps(report, indent=1), encoding="utf-8")
    print(json.dumps(sc, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
