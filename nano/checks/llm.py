"""The language-model checker: nano/check.py behind the checker protocol (nano/checks/base.py).

A thin wrapper. check.py is not changed; every method passes its keyword arguments straight through,
so the loop can keep calling with learn_steps=, long_steps=, retime=, curves=, diagnostics= and so on.

    baseline_profile(baseline, out, seeds, **kw) -> check.refresh_profile(out, seeds=seeds, **kw)
    refresh_profile(profile_dir, **kw)           -> check.refresh_profile (the old name, kept)
    check(candidate, out, baseline, **kw)        -> check.check   (rungs 0-3)
    long_run(candidate, out, baseline, **kw)     -> check.long_run (rung 4)
    fidelity_probe(candidate, out, baseline, target, steps=60) -> check.fidelity_probe
    final(candidate, out, baseline, seeds, ...)  -> rung 5: full training plus the harness exam per seed
                                                    (nano/batch_verify.py train) and the sequential verdict
Note: check.refresh_profile always measures nano/train.py (check.BASELINE); the `baseline` path argument
of baseline_profile is recorded but cannot redirect it.
"""
from __future__ import annotations

from pathlib import Path

from nano import check as C

CHECKER = "LLMChecker"


class LLMChecker:
    LEARN_STEPS = C.LEARN_STEPS
    LONG_STEPS = C.LONG_STEPS
    PROFILE_SEEDS = C.PROFILE_SEEDS
    PROFILE_SEED = C.PROFILE_SEED

    def __init__(self, profile=None, **args):
        self.profile = profile
        self.args = dict(args)

    # ------------------------------------------------------------ baseline
    def baseline_profile(self, baseline: Path | None, out: Path, seeds=None, **kw) -> dict:
        if seeds is not None:
            kw["seeds"] = tuple(seeds)
        prof = C.refresh_profile(Path(out), **kw)
        if baseline is not None and Path(baseline).resolve() != C.BASELINE.resolve():
            prof.setdefault("notes", []).append(f"baseline {baseline} requested; check.py measures {C.BASELINE}")
        return prof

    def refresh_profile(self, profile_dir: Path, **kw) -> dict:
        return C.refresh_profile(Path(profile_dir), **kw)

    # ------------------------------------------------------------ ladder
    def check(self, candidate: Path, out: Path, baseline: dict, **kw) -> dict:
        return C.check(Path(candidate), Path(out), baseline, **kw)

    def long_run(self, candidate: Path, out: Path, baseline: dict, **kw) -> dict:
        return C.long_run(Path(candidate), Path(out), baseline, **kw)

    def fidelity_probe(self, candidate: Path, out: Path, baseline: dict, target: str, steps: int = 60) -> dict:
        return C.fidelity_probe(Path(candidate), Path(out), baseline, target, steps=steps)

    # ------------------------------------------------------------ full test
    def final(self, candidate: Path, out: Path, baseline: dict, seeds, *, tokens: float = 50e6,
              timeout_s: int = 6 * 3600, wall_cap: float = 0.0, margin: float | None = None,
              alpha: float | None = None) -> dict:
        """Full fixed-budget training plus the exam for each seed, against the pooled baseline seeds of the
        current baseline version (as nano/batch_verify.py does, without its staging and e-BH)."""
        from nano import batch_verify as BV
        from nano import verdict as V
        from nano.version import baseline_version
        score = dict(getattr(self.profile, "score", None) or {})
        margin = score.get("margin", 0.005) if margin is None else margin
        alpha = score.get("alpha", 0.01) if alpha is None else alpha
        runs = []
        for s in seeds:
            runs.append(BV.train(Path(candidate), Path(out) / f"seed{s}", int(s), tokens, timeout_s, wall_cap=wall_cap))
        ok = [(int(s), r["val_loss"]) for s, r in zip(seeds, runs) if r.get("val_loss") is not None]
        cand_vals = [v for _, v in ok]
        base = BV.baseline_runs(baseline_version(), tokens)
        base_vals = [r["val_loss"] for r in base]
        v = V.sequential_verdict(cand_vals, base_vals, margin=margin, alpha=alpha,
                                 min_seeds=score.get("min_seeds", 3),     # seed s meets baseline seed s
                                 cand_seeds=[s for s, _ in ok], base_seeds=[r.get("seed") for r in base])
        return {"status": v["status"], "cand_vals": cand_vals, "base_vals": base_vals, "verdict": v,
                "errors": [r.get("error") for r in runs if r.get("error")]}
