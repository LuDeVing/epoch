"""Bug pass 2026-10-17 (night): checkers, verdict, check.py timing, launcher, exam. CPU only; tiny stand-ins,
never real training."""
import json
import math
import os
import subprocess
import sys
import textwrap
import time
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from nano import verdict as V  # noqa: E402

BASE6 = [3.30, 3.31, 3.29, 3.30, 3.32, 3.28]


# ---------------------------------------------------------------- verdict
def test_identical_baseline_values_do_not_crash_and_verify_nothing():
    # sigma 0 from identical baseline runs: tau = 1.5 x 0 used to divide by zero inside e_value
    v = V.sequential_verdict([3.29, 3.29, 3.29], [3.3] * 6, lower_is_better=True)
    assert v["status"] == "error" and v["e"] is None


def test_e_value_with_zero_tau_is_finite():
    assert math.isfinite(V.e_value([0.01, 0.01], 0.0, 0.005, tau=0.0))


def test_nan_candidate_value_fails():
    # a diverged run (NaN val_loss) used to come out close_call with gain NaN
    v = V.sequential_verdict([float("nan"), 3.0, 3.0], BASE6, lower_is_better=True)
    assert v["status"] == "fail" and v["e"] is None


def test_nan_baseline_value_is_an_error_not_a_crash():
    v = V.sequential_verdict([3.29, 3.29, 3.29], [3.3, 3.31, float("nan"), 3.29, 3.3, 3.32], lower_is_better=True)
    assert v["status"] == "error"


# ---------------------------------------------------------------- LLMChecker.final pairs by seed number
def test_llm_checker_final_pairs_by_seed(monkeypatch, tmp_path):
    from nano import batch_verify as BV
    from nano.checks.llm import LLMChecker
    base = {s: 3.0 + 0.1 * s for s in range(6)}

    def fake_train(script, out, seed, tokens, timeout_s, wall_cap=0.0, extra=None):
        if seed == 1:
            return {"error": "wall-clock cap", "seed": seed}
        return {"val_loss": base[seed] - 0.01, "seed": seed}
    monkeypatch.setattr(BV, "train", fake_train)
    monkeypatch.setattr(BV, "baseline_runs", lambda version, tokens: [{"val_loss": v, "seed": s} for s, v in base.items()])
    r = LLMChecker(None).final(tmp_path / "c.py", tmp_path / "out", {}, seeds=(0, 1, 2))
    # seed 0 meets baseline seed 0 and seed 2 meets baseline seed 2: both 0.01 better
    assert r["verdict"]["gain"] == pytest.approx(0.01, abs=1e-9)


# ---------------------------------------------------------------- panel
def _proposal(order):
    body = {"CLAIM": "the claim is that judges should rotate tables [F1] each round",
            "FROM THE FACTS TO THE IDEA": "fact one says judges choose tables freely so bias grows",
            "FROM THE IDEA TO THE RESULT": "rotation spreads each judge over many teams evenly",
            "WEAK POINTS": "more walking time between tables for every judge",
            "PROPOSED TEST": "run one round with rotation and compare score spread"}
    return "\n\n".join(f"**{k}**: {body[k]}" for k in order)


def test_panel_lint_catches_bold_headers_out_of_order():
    from nano.checks import panel as P
    facts = [{"id": "F1", "text": "judges pick tables"}]
    assert P.lint(_proposal(P.SECTIONS), facts)["ok"]
    swapped = list(P.SECTIONS)
    swapped[0], swapped[4] = swapped[4], swapped[0]
    lt = P.lint(_proposal(swapped), facts)
    assert not lt["ok"] and any("order" in p for p in lt["problems"])


def test_panel_lint_inline_mention_of_a_header_is_not_out_of_order():
    from nano.checks import panel as P
    text = _proposal(P.SECTIONS).replace("the claim is that", "the claim (see PROPOSED TEST: below) is that")
    assert P.lint(text, [{"id": "F1", "text": "judges pick tables"}])["ok"]


def test_panel_people_nan_score_is_not_a_ten():
    from nano.checks.panel import PanelChecker
    pc = PanelChecker(None, criteria=["a"])
    mean, n, _ = pc._people([{"score": "nan", "who": "x"}, {"score": "inf", "who": "y"}, {"score": 4, "who": "z"}])
    assert n == 1 and mean == 4.0


# ---------------------------------------------------------------- check.py timing
def _fake_run_factory(plan):
    """plan(args, out) -> (rc, metrics or None, violations)."""
    from nano import check as C

    def fake_run(script, args, out, timeout, *, wall_cap=0.0, audit_name="audit.json"):
        out.mkdir(parents=True, exist_ok=True)
        rc, m, viol, stdout = plan(script, args, out)
        if m is not None:
            (out / "metrics.json").write_text(json.dumps(m), encoding="utf-8")
        return {"rc": rc, "stdout": stdout, "stderr": "", "wall": 1.0, "timed_out": False, "audit": {},
                "violations": viol}
    return C, fake_run


def test_step_time_warmup_run_violations_are_not_dropped(monkeypatch, tmp_path):
    def plan(script, args, out):
        if args[1] == "1":        # the separate one-step warm-up run
            return 0, {"steps": 1, "wall_s": 0.5, "tokens": 100}, ["open: val.bin"], ""
        return 0, {"steps": 4, "wall_s": 2.0, "tokens": 400}, [], ""     # no step-1 line: the warm-up run is needed
    C, fake = _fake_run_factory(plan)
    monkeypatch.setattr(C, "_run", fake)
    step_s, m, r = C._step_time(tmp_path / "cand.py", tmp_path / "steps")
    assert r["violations"], r


def test_check_tolerates_null_peak_vram(monkeypatch, tmp_path):
    def plan(script, args, out):
        if "--build-only" in args:
            return 0, {"params_nonembed": 1000}, [], ""
        if args[:2] == ["--smoke-steps", "4"]:
            return 0, {"steps": 4, "wall_s": 2.0, "tokens": 400, "peak_vram_gb": None}, [], "[nano] step 1/4 loss 1 lr x1 0.4k tok/s"
        return 1, None, [], ""
    C, fake = _fake_run_factory(plan)
    monkeypatch.setattr(C, "_run", fake)
    rec = C.check(tmp_path / "cand.py", tmp_path / "v", {"params_nonembed": 1000, "step_s": 0.5,
                                                          "step_s_method": C.STEP_METHOD}, rung_max=2, audit=False)
    assert rec["status"] == "checked", rec


# ---------------------------------------------------------------- launcher: the wall cap kills the whole tree
def _alive(pid: int) -> bool:
    if os.name == "nt":
        out = subprocess.run(["tasklist", "/FI", f"PID eq {pid}", "/NH"], capture_output=True, text=True).stdout
        return str(pid) in out
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False


def test_kill_tree_ends_grandchildren(tmp_path):
    from nano import launch
    pidf = tmp_path / "gc.pid"
    code = textwrap.dedent(f"""
        import subprocess, sys, time
        p = subprocess.Popen([sys.executable, "-c", "import time; time.sleep(120)"])
        open({str(pidf)!r}, "w").write(str(p.pid))
        time.sleep(120)
    """)
    proc = subprocess.Popen([sys.executable, "-c", code], **({} if os.name == "nt" else {"start_new_session": True}))
    t0 = time.time()
    while not pidf.exists() or not pidf.read_text().strip():
        assert time.time() - t0 < 60
        time.sleep(0.1)
    gpid = int(pidf.read_text())
    try:
        launch._kill_tree(proc)
        proc.wait(timeout=30)
        t0 = time.time()
        while _alive(gpid) and time.time() - t0 < 15:
            time.sleep(0.2)
        assert not _alive(gpid)
    finally:
        if _alive(gpid):
            os.kill(gpid, 9)


def test_wall_cap_goes_through_kill_tree(monkeypatch, tmp_path):
    from nano import launch
    called = []
    real = launch._kill_tree
    monkeypatch.setattr(launch, "_kill_tree", lambda p: (called.append(p.pid), real(p)))
    (tmp_path / "data").mkdir()
    script = tmp_path / "s.py"
    script.write_text("import time\ntime.sleep(120)\n", encoding="utf-8")
    rc = launch.main(["--out", str(tmp_path / "out"), "--data-dir", str(tmp_path / "data"), "--wall-cap", "2",
                      "--audit", str(tmp_path / "audit.json"), str(script)])
    assert rc == 124 and called


# ---------------------------------------------------------------- exam: a NaN loss is an error, not a pass
def test_exam_nan_loss_is_an_error(monkeypatch, tmp_path):
    import numpy as np
    import torch
    from nano import exam
    cand = tmp_path / "cand.py"
    cand.write_text(textwrap.dedent("""
        import torch, torch.nn as nn
        from dataclasses import dataclass
        @dataclass
        class Config:
            d: int = 4
        class GPT(nn.Module):
            def __init__(self, cfg):
                super().__init__()
                self.w = nn.Linear(cfg.d, cfg.d, bias=False)
            def forward(self, idx):
                B, T = idx.shape
                return torch.full((B, T, 50257), float("nan")) + 0 * self.w.weight.sum()
    """), encoding="utf-8")
    sys.modules.pop("htsa_candidate", None)
    torch.save({"state_dict": {"w.weight": torch.zeros(4, 4)}, "config": {"d": 4}}, tmp_path / "model.pt")
    monkeypatch.setattr(torch.cuda, "is_available", lambda: False)        # CPU only
    monkeypatch.setattr(exam, "val_tokens", lambda *a, **k: np.arange(200, dtype=np.uint16))
    monkeypatch.setattr(exam, "val_windows", lambda data, *a, **k: iter([(torch.zeros(2, 8, dtype=torch.long),
                                                                          torch.zeros(2, 8, dtype=torch.long))]))
    res = exam.run_exam(cand, tmp_path / "model.pt", params_base=10_000)
    assert res.get("error") and res.get("val_loss") is None, res


# ---------------------------------------------------------------- exam: only the token table is not counted
def test_exam_counts_an_extra_embedding_table_as_train_py_does():
    import torch
    import torch.nn as nn
    from nano import exam

    class M(nn.Module):
        def __init__(self):
            super().__init__()
            self.tok = nn.Embedding(100, 8)
            self.tok2 = nn.Embedding(100, 4)          # a bigram table: capacity, counted by param_counts
            self.mid = nn.Linear(8, 8, bias=False)
            self.head = nn.Linear(8, 100, bias=False)
            self.head.weight = self.tok.weight        # tied: one tensor
    m = M()
    total = sum(p.numel() for p in m.parameters())
    assert exam.nonembed_params(m) == total - m.tok.weight.numel() == 400 + 64


# ---------------------------------------------------------------- batch_verify: a failed run is not a result
def test_batch_verify_train_rejects_a_nonzero_exit_with_metrics(monkeypatch, tmp_path):
    from nano import batch_verify as BV
    from nano import check as C

    def fake_run(script, args, out, timeout, *, wall_cap=0.0, audit_name="audit.json"):
        out.mkdir(parents=True, exist_ok=True)
        (out / "metrics.json").write_text(json.dumps({"tokens": 1000, "steps": 1, "wall_s": 1.0}), encoding="utf-8")
        return {"rc": 3, "stdout": "", "stderr": "", "wall": 1.0, "timed_out": False, "audit": {}, "violations": []}
    monkeypatch.setattr(C, "_run", fake_run)
    monkeypatch.setattr(BV, "_exam", lambda script, out: {"val_loss": 3.0})
    r = BV.train(tmp_path / "c.py", tmp_path / "seed0", 0, 1000, 60)
    assert r.get("error") and r.get("val_loss") is None, r


# ---------------------------------------------------------------- check.py: the re-timing run is audited too
def test_check_retiming_run_violations_fail_the_candidate(monkeypatch, tmp_path):
    def plan(script, args, out):
        if "--build-only" in args:
            return 0, {"params_nonembed": 1000}, [], ""
        slow = "base" not in str(out)
        line = "[nano] step 1/4 loss 1 lr x1 {}k tok/s".format("0.1" if slow else "0.4")
        viol = ["open: val.bin"] if out.name == "steps2" else []
        wall = 8.0 if slow else 2.0
        return 0, {"steps": 4, "wall_s": wall, "tokens": 400, "peak_vram_gb": 1.0}, viol, line
    C, fake = _fake_run_factory(plan)
    monkeypatch.setattr(C, "_run", fake)
    rec = C.check(tmp_path / "cand.py", tmp_path / "v", {"params_nonembed": 1000, "step_s": 0.5,
                                                          "step_s_method": C.STEP_METHOD}, rung_max=2, audit=False)
    assert rec["status"] == "fail" and "integrity" in rec["feedback"].get("reason", ""), rec


# ---------------------------------------------------------------- ScriptChecker: long_run never reuses a failed run
SCORER = '''
import argparse, json, math, sys
from pathlib import Path
ap = argparse.ArgumentParser()
ap.add_argument("--candidate"); ap.add_argument("--out"); ap.add_argument("--level"); ap.add_argument("--seed")
a = ap.parse_args()
mode = Path(a.candidate).read_text(encoding="utf-8").strip()
score = float("inf") if mode == "inf" else 1.0
Path(a.out, "metrics.json").write_text(json.dumps({"score": score, "cost": {"t": 1.0}, "n": 1}).replace("Infinity", "1e999"))
sys.exit(3 if mode == "crash" else 0)
'''


def _script_checker(tmp_path, monkeypatch):
    from nano.checks import script as S
    monkeypatch.setattr(S, "PY", Path(sys.executable))       # the test lab root has no venv
    (tmp_path / "scorer.py").write_text(SCORER, encoding="utf-8")
    return S.ScriptChecker(None, scorer=f"python {(tmp_path / 'scorer.py').as_posix()} --candidate {{candidate}} --out {{out}} "
                                       f"--level {{level}} --seed {{seed}}", wall_cap=120)


def test_script_long_run_does_not_reuse_a_failed_full_run(tmp_path, monkeypatch):
    ck = _script_checker(tmp_path, monkeypatch)
    cand = tmp_path / "cand.txt"
    cand.write_text("crash", encoding="utf-8")
    out = tmp_path / "v"
    base = {"quick": {"scores": {"0": 1.0}, "sd": 0.1}, "full": {"scores": {"0": 1.0}, "sd": 0.1}}
    r = ck._score(cand, out / "full", "full", 0)       # rung 3's run: it wrote metrics.json, then exited 3
    assert r["metrics"] is None
    res = ck.long_run(cand, out, base)
    assert res["ok"] is False, res


def test_script_infinite_score_is_not_a_score(tmp_path, monkeypatch):
    ck = _script_checker(tmp_path, monkeypatch)
    cand = tmp_path / "cand.txt"
    cand.write_text("inf", encoding="utf-8")
    r = ck._score(cand, tmp_path / "v" / "quick", "quick", 0)
    assert r["metrics"] is None and r.get("bad_metrics"), r
