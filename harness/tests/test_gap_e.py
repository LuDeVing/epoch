"""Gap E (evidence): NoveltyBench intervals, IQM, rejudge file naming, judge agreement; the bin-packing arms dry run."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest

try:
    from harness import noveltybench as nb
except (FileNotFoundError, KeyError, OSError) as e:   # the official prompts live in the lab's ext folder
    pytest.skip(f"NoveltyBench sources unavailable: {e}", allow_module_level=True)


def _write(path: Path, rows: list[dict]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r) + "\n" for r in rows), encoding="utf-8")
    return path


def _rows(distinct, utility, prefix="p"):
    return [{"id": f"{prefix}{i}", "prompt": f"prompt {i}", "generations": ["a"] * 10, "distinct": d, "utility": u,
             "gen_tokens": 100} for i, (d, u) in enumerate(zip(distinct, utility))]


def test_iqm_cuts_a_quarter_from_each_end():
    assert nb.iqm(range(1, 9)) == pytest.approx(4.5)              # middle of 1..8: 3, 4, 5, 6
    assert nb.iqm([1, 2, 3, 4, 1000]) == pytest.approx(3.0)       # int(0.25 * 5) = 1 cut each side
    assert nb.iqm([7.0]) == 7.0


def test_paired_bootstrap_constant_shift_and_seed():
    b = np.arange(20, dtype=float)
    r = nb.paired_bootstrap(b + 1.0, b, n_boot=2000, seed=0)
    assert r["n"] == 20 and r["mean"] == pytest.approx(1.0) and r["lo"] == pytest.approx(1.0) and r["hi"] == pytest.approx(1.0)
    rng = np.random.default_rng(3)
    a, c = rng.normal(0.5, 1, 50), rng.normal(0, 1, 50)
    r1, r2 = nb.paired_bootstrap(a, c, seed=0), nb.paired_bootstrap(a, c, seed=0)
    assert r1 == r2 and r1["lo"] < r1["mean"] < r1["hi"]
    assert nb.win_loss_tie([3, 2, 5], [1, 2, 6]) == (1, 1, 1)


def test_summary_reports_iqm_intervals_and_wlt(tmp_path):
    base = _rows([3, 4, 5, 3], [3.0, 4.0, 5.0, 3.0])
    meth = _rows([9, 9, 5, 2], [5.0, 4.0, 6.0, 2.0])
    _write(tmp_path / "x-plain" / "scores.jsonl", base)
    _write(tmp_path / "x-method" / "scores.jsonl", meth + [{**meth[0], "distinct": 1}])   # a later duplicate is ignored
    text = nb.summary([tmp_path / "x-plain", tmp_path / "x-method"], n_boot=500)
    assert "IQM distinct" in text and "| x-method | 4 |" in text
    row = next(l for l in text.splitlines() if l.startswith("| x-plain | 4 |") and "[" in l)
    assert "+2.50 [" in row and "| 2/1/1 |" in row          # distinct diffs 6, 5, 0, -1
    c = nb.compare(nb.load_scores(tmp_path / "x-method" / "scores.jsonl"), base, n_boot=500)
    assert c["distinct"]["mean"] == pytest.approx(2.5) and c["utility"]["wlt"] == (2, 1, 1)


def test_rejudge_writes_a_suffixed_file_and_leaves_scores_alone(tmp_path):
    assert nb.rejudge_path(tmp_path, "sonnet").name == "scores.sonnet.jsonl"
    assert nb.rejudge_path(tmp_path, "a/b c").name == "scores.a_b_c.jsonl"
    with pytest.raises(ValueError):
        nb.rejudge_path(tmp_path, "")
    gens = _rows([0] * 30, [0.0] * 30)
    _write(tmp_path / "generations.jsonl", gens)
    orig = _write(tmp_path / "scores.jsonl", _rows([5] * 30, [5.0] * 30)).read_text(encoding="utf-8")
    seen = []

    def fake_judge(row, judge_model, out, seed=0, log_name="judge_calls"):
        seen.append((judge_model, log_name))
        return {**row, "distinct": 4, "utility": 4.5, "judge_model": judge_model}
    dest = nb.rejudge(tmp_path, "sonnet", 20, 0, "sonnet", judge=fake_judge)
    assert dest == tmp_path / "scores.sonnet.jsonl"
    got = nb.load_scores(dest)
    assert len(got) == 20 and all(r["judge_model"] == "sonnet" for r in got)
    assert set(seen) == {("sonnet", "judge_calls_sonnet")}
    assert (tmp_path / "scores.jsonl").read_text(encoding="utf-8") == orig
    ids1 = [r["id"] for r in nb.rejudge_sample(gens, 20, 0)]
    assert ids1 == [r["id"] for r in nb.rejudge_sample(list(reversed(gens)), 20, 0)][::-1]   # same set, file order
    assert ids1 != [r["id"] for r in nb.rejudge_sample(gens, 20, 1)]


def test_agreement_on_shared_prompts(tmp_path):
    a = _write(tmp_path / "a.jsonl", _rows([5, 6, 7, 8, 9], [1.0, 2.0, 3.0, 4.0, 5.0]))
    b = _write(tmp_path / "b.jsonl", _rows([5, 6, 8, 8, 9, 1], [1.5, 2.5, 3.5, 4.5, 9.0, 0.0]))
    r = nb.agreement(a, b)
    assert r["n"] == 5 and r["utility_spearman"] == pytest.approx(1.0)
    assert r["distinct_exact"] == pytest.approx(0.8) and r["distinct_within1"] == pytest.approx(1.0)
    assert r["distinct_mean_abs_diff"] == pytest.approx(0.2)
    c = _write(tmp_path / "c.jsonl", _rows([5, 6, 7, 8, 9], [5.0, 4.0, 3.0, 2.0, 1.0]))
    assert nb.agreement(a, c)["utility_spearman"] == pytest.approx(-1.0)
    assert nb.spearman([1, 1, 2], [1, 2, 3]) == pytest.approx(np.corrcoef([1.5, 1.5, 3], [1, 2, 3])[0, 1])
    assert "Spearman" in nb.agreement_text(r)


def test_binpack_arms_commands_and_prereg(tmp_path):
    from nano.experiments import binpack_arms as BA
    pre = BA.write_prereg(tmp_path)
    assert pre["prediction"]["ordering"] == ["full", "best_of_n", "profile_only"] and pre["hash"]
    assert BA.write_prereg(tmp_path)["written"] == pre["written"]          # kept, not rewritten
    with pytest.raises(SystemExit):
        BA.write_prereg(tmp_path, {**BA.PREREG, "seeds": [9]})            # a changed prediction is refused
    po = BA.arm_commands("profile_only", 1, "x", pre)
    assert po[1:3] == ["-m", "nano.loop"] and "--no-planner" in po and "--no-deepen" in po
    assert po[po.index("--off-tree-share") + 1] == "0" and po[po.index("--replicate") + 1] == "1"
    full = BA.arm_commands("full", 1, "x", pre)
    assert not {"--no-planner", "--no-deepen", "--off-tree-share"} & set(full)
    bon = BA.arm_commands("best_of_n", 1, "x", pre)
    assert "bestofn" in bon and bon[bon.index("--scorer-cap") + 1] == str(pre["scorer_cap_per_arm"])
    assert BA.arm_commands("full", 0, "x", pre, dry=True)[2] == "nano.dry_run"


def test_binpack_arms_dry_mode(tmp_path):
    """Every arm on the mock backend for one short round, then the report with the five checks."""
    from nano.experiments import binpack_arms as BA
    out = tmp_path / "arms"
    rc = BA.main(["dry", "--out", str(out)])
    man = json.loads((out / "arms.json").read_text(encoding="utf-8"))
    assert rc == 0 and [r["arm"] for r in man["runs"]] == list(BA.ARMS) and all(r["rc"] == 0 for r in man["runs"])
    assert json.loads((out / "prereg.json").read_text(encoding="utf-8"))["hash"] == man["prereg_hash"]
    rep = (out / "binpack_arms_report.md").read_text(encoding="utf-8")
    for k in range(1, 6):
        assert f"## Check {k}:" in rep
    assert "Rejected 3/3 planted wrong rules; the control was accepted" in rep
    for r in man["runs"]:
        rd = Path(man["lab_root"]) / "runs" / r["run_id"]
        assert (rd / "answer.json").exists() and BA.scorer_calls(rd), r["arm"]
    bon = Path(man["lab_root"]) / "runs" / man["runs"][2]["run_id"]
    assert len(BA.scorer_calls(bon)) <= 9 + 3                              # the cap; a candidate started under it may finish
    assert not any(BA.prompt_hits(bon)[0].values())                        # best-of-N prompts: profile words only
