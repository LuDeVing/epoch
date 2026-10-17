"""Tests for harness/think.py (ARCHITECTURE.md section 4) on the mock backend, temp lab root.

Two modes:
- contract tests: every dependency is replaced by a small stand-in that honours the README
  interface (preloaded into think._MODS), so the driver logic is tested alone and exactly;
- end-to-end tests: the real modules, skipped while any of them is missing.
The mock LLM returns a correct ARC program (verified answer), a wrong one (abstain), or a fixed
BT option. No real tokens are spent. Every test runs under its own temporary lab root.
"""
from __future__ import annotations

import importlib
import itertools
import json
import os
import tempfile
from dataclasses import dataclass
from pathlib import Path
from types import SimpleNamespace

os.environ.setdefault("HTSA_LAB_ROOT", tempfile.mkdtemp(prefix="htsa_think_"))

import pytest  # noqa: E402

from harness import config, llm  # noqa: E402

_pkg = importlib.import_module("harness.think")      # package (forwards) or the driver itself
think = _pkg.load_driver() if hasattr(_pkg, "load_driver") else _pkg
from harness.schemas import (Candidate, Judgment, Usage, VerifyResult, append_jsonl,  # noqa: E402
                             new_id, read_json, read_jsonl, strip_key, write_json)

CORRECT = "def transform(grid):\n    return [row[::-1] for row in grid]\n"
WRONG = "def transform(grid):\n    return [row[:] for row in grid]\n"
KEY_GRID = [[9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9, 9, 9, 9]]   # sentinel no candidate can predict
DEFAULTS_REPLY = "\n".join(f"{i}. zqdflt-{w}" for i, w in enumerate(
    ["alpha", "beta", "gamma", "delta", "epsilon"], 1))
GEN_ROLES = ("generate", "transform", "plain", "program", "revise", "formal")


def arc_item(item_id: str) -> dict:
    return {"id": item_id, "benchmark": "arc", "family": "arc", "split": "dev-tune",
            "train": [{"input": [[1, 2, 3], [4, 5, 6]], "output": [[3, 2, 1], [6, 5, 4]]},
                      {"input": [[7, 0], [0, 8]], "output": [[0, 7], [8, 0]]}],
            "test_input": [[1, 0, 2, 0], [3, 0, 4, 0]], "test_output": KEY_GRID}


def bt_item(item_id: str) -> dict:
    return {"id": item_id, "benchmark": "bt", "family": "bt_sp", "split": "dev-tune",
            "question": "A man shaves many times a day and still has a beard. How can that be?",
            "choices": ["He shaves other people.", "He forgets.", "He has two faces.",
                        "None of the above."], "label": 0}


def make_mock(benchmark: str, program: str = CORRECT, letter: str = "B"):
    def fn(prompt: str, role: str, meta: dict) -> str:
        if role == "defaults":
            return DEFAULTS_REPLY
        if role == "probe":
            return f"```python\n{program}```" if benchmark == "arc" else f"ANSWER: {letter}"
        if role in GEN_ROLES:
            return f"1. ```python\n{program}```" if benchmark == "arc" else f"1. {letter}"
        return llm._default_mock(prompt, role, meta)
    return fn


def wrong_program(n: int) -> str:
    """A distinct wrong program per n (adds n to every cell), so predictions never collide."""
    return f"def transform(grid):\n    return [[(v + {n}) % 10 for v in row] for row in grid]\n"


def make_varied_mock():
    """Probe always answers wrong_program(1); generator calls answer wrong_program(1), (2), ...
    so the first candidate agrees with the probe (conf 1.0, a surprise when it fails)."""
    counter = itertools.count(1)

    def fn(prompt: str, role: str, meta: dict) -> str:
        if role == "defaults":
            return DEFAULTS_REPLY
        if role == "probe":
            return f"```python\n{wrong_program(1)}```"
        if role in GEN_ROLES:
            return f"1. ```python\n{wrong_program(next(counter))}```"
        return llm._default_mock(prompt, role, meta)
    return fn


# ---------------------------------------------------------------- stand-ins (README interfaces)
@dataclass
class Spec:
    card: str
    operator: str = "none"
    seed: str = ""
    perm: int = 0
    variant: str | None = None
    parent_id: str | None = None


def _exec(src: str, grid):
    ns: dict = {}
    try:
        exec(src, ns)                      # test-only: the two fixed programs above
        return ns["transform"](grid)
    except Exception:  # noqa: BLE001
        return None


def _prompt(run_dir: Path, cid: str, text: str) -> None:
    (Path(run_dir) / "prompts").mkdir(parents=True, exist_ok=True)
    (Path(run_dir) / "prompts" / f"{cid}.txt").write_text(text, encoding="utf-8")


def _parse(text: str, benchmark: str, item: dict) -> list[dict]:
    if benchmark == "arc":
        if "def transform" not in text:
            return []
        src = text[text.index("def transform"):].split("```")[0]
        return [{"text": src, "program": src, "pred": _exec(src, item["test_input"])}]
    out = []
    for line in text.splitlines():
        line = line.strip()
        letter = line.split(".", 1)[-1].strip()[:1] if line[:1].isdigit() else line[-1:]
        if letter in "ABCD" and letter:
            out.append({"text": letter, "program": None, "pred": letter})
    return out


def _key(c, benchmark):
    return json.dumps(c.pred) if c.pred is not None else c.text


class Stubs:
    """Container whose attributes are the stand-in modules; records what encode received."""

    def __init__(self):
        self.encoded: list[dict] = []
        self.mods = {
            "encode": SimpleNamespace(encode=self.encode),
            "verify": SimpleNamespace(build=self.v_build, run=self.v_run),
            "probe": SimpleNamespace(run_probe=self.run_probe, agreement=self.agreement,
                                     calibrate=lambda a, p, f: a),
            "judge": SimpleNamespace(judge=self.judge),
            "run_card": SimpleNamespace(run_card=self.run_card),
            "ledger": SimpleNamespace(append=lambda row: append_jsonl(
                config.LEDGER_PATH, row.to_dict() if hasattr(row, "to_dict") else row)),
            "graph": SimpleNamespace(write=self.g_write),
            "stats": SimpleNamespace(load_views=lambda b: None),
            "dedup": SimpleNamespace(rate=self.d_rate, drop=self.d_drop),
            "allocate": SimpleNamespace(
                initial=lambda b, cls, v, n0, rep, r: [Spec("seeded", seed="river", perm=1), Spec("low_prior"),
                                                       Spec("transform", "drop"), Spec("formal")][:n0],
                fresh_tuples=self.fresh,
                reallocate=lambda specs, mult: [s for s in specs if s.card != "revise"],
                est_cost=lambda s, v, b: 1000, est_verify=lambda k, mean: 0,
                revise_specs=lambda parents, rep: [Spec("revise", "fix", parent_id=c.id)
                                                   for c, _ in parents]),
            "admit": SimpleNamespace(update=self.admit),
            "arc_exec": SimpleNamespace(predict=_exec),
            "stop": SimpleNamespace(p_correct=lambda vt, a, calib=None: a,
                                    partial_gain=lambda prev, new: new - prev),
            "stagnation": SimpleNamespace(should_reset=lambda stale, dup, R, Rs, d:
                                          R > 2 and (stale >= Rs or dup > d)),
            "tournament": SimpleNamespace(pick_parents=lambda q, conf, hi, n, rep: list(q[:n])),
        }

    def fresh(self, benchmark, cls, used, variants, replicate, round_no, n, cards=None):
        self.n_fresh = getattr(self, "n_fresh", 0) + n
        return [Spec((cards or ["seeded"])[0], seed=f"w{round_no}_{self.n_fresh}_{i}") for i in range(n)]

    # encode
    def encode(self, item, run_dir, *, backend, replicate, log_dir):
        self.encoded.append(dict(item))
        data = json.dumps({k: v for k, v in item.items() if k not in ("id", "split", "family")})
        total = 0
        for role in ("encode", "defaults"):
            cid = new_id("c")
            prompt = f"Problem data:\n{data}\nList the facts."
            _prompt(run_dir, cid, prompt)
            res = llm.call(prompt, role=role, call_id=cid, backend=backend, log_dir=log_dir)
            total += res.usage.total_tokens
            if role == "defaults":
                write_json(Path(run_dir) / "private" / "defaults.json", {"defaults": res.text})
        (Path(run_dir) / "problem.md").write_text(f"GOAL: solve.\n{data}\n", encoding="utf-8")
        return SimpleNamespace(item_id=item["id"], benchmark=item["benchmark"], goal="solve",
                               facts=[], resources=[], checklist=[], bar={}, views={},
                               problem_md=f"GOAL: solve.\n{data}", encode_tokens=total, item=item)

    # generation
    def run_card(self, spec, problem, run_dir, *, backend, round_no, log_dir, replicate,
                 parent=None, feedback=None, flags=None):
        cid = new_id("c")
        prompt = f"{problem.problem_md}\nCard: {spec.card} {spec.operator} seed {spec.seed}"
        if parent is not None:
            prompt += f"\nParent:\n{parent.text}\nFeedback: {json.dumps(feedback)}"
        _prompt(run_dir, cid, prompt)
        res = llm.call(prompt, role="generate", call_id=cid, backend=backend, log_dir=log_dir,
                       meta={"benchmark": problem.benchmark})
        cands = [Candidate(id=new_id("k"), text=p["text"], card=spec.card, operator=spec.operator,
                           seed=spec.seed, perm=spec.perm, round=round_no, call_id=cid,
                           program=p["program"], pred=None if p["program"] else p["pred"],
                           parent_ids=[parent.id] if parent else [])
                 for p in _parse(res.text, problem.benchmark, problem.item)]
        if cands:
            append_jsonl(Path(run_dir) / "cands" / f"{cid}.jsonl", [c.to_dict() for c in cands])
        return SimpleNamespace(cands=cands, usage=res.usage, call_ids=[cid],
                               contract={"id": cid, "path": "", "n_cands": len(cands)})

    def run_probe(self, problem, *, n, backend, log_dir, replicate, run_dir):
        usage, clusters, cands = Usage(), {}, []
        for i in range(n):
            cid = new_id("c")
            prompt = f"{problem.problem_md}\nSeed {i}"
            _prompt(run_dir, cid, prompt)
            res = llm.call(prompt, role="probe", call_id=cid, backend=backend, log_dir=log_dir)
            usage = usage.add(res.usage)
            for p in _parse(res.text, problem.benchmark, problem.item)[:1]:
                c = Candidate(id=new_id("p"), text=p["text"], card="probe", operator="none", seed="",
                              perm=0, round=0, call_id=cid, origin="probe", pred=p["pred"])
                cands.append(c)
                clusters[_key(c, problem.benchmark)] = clusters.get(_key(c, problem.benchmark), 0) + 1
        return SimpleNamespace(clusters=clusters, n=n, usage=usage, cands=cands)

    @staticmethod
    def agreement(probe, cand, benchmark):
        return probe.clusters.get(_key(cand, benchmark), 0) / probe.n if probe.n else 0.0

    @staticmethod
    def judge(cands, problem, *, backend, log_dir, replicate):
        return [Judgment(id=c.id, p_raw=0.5, call_ids=["cj"]) for c in cands], Usage(40, 10)

    # verify
    @staticmethod
    def v_build(problem, benchmark):
        vtype = "demo_match" if benchmark == "arc" else "agreement"
        return SimpleNamespace(type=vtype, hash="h" + benchmark, data=dict(problem.item))

    @staticmethod
    def v_run(cand, handle, *, attempts, benchmark, agreement, run_dir):
        if benchmark == "arc":
            train = handle.data["train"]
            ok = sum(_exec(cand.program or "", p["input"]) == p["output"] for p in train)
            res = VerifyResult(id=cand.id, status="verified" if ok == len(train) else "fail",
                               verification_type="demo_match", attempts=1,
                               partial_score=ok / len(train),
                               feedback_record=None if ok == len(train) else {"matched": ok})
        else:
            res = VerifyResult(id=cand.id, status="unverified", verification_type="agreement",
                               partial_score=agreement or 0.0)
        append_jsonl(Path(run_dir) / "verify.jsonl", res.to_dict())
        return res

    # control
    @staticmethod
    def d_rate(new, prior, benchmark):
        seen, dups = {_key(c, benchmark) for c in prior}, 0
        for c in new:
            dups += _key(c, benchmark) in seen
            seen.add(_key(c, benchmark))
        return dups / len(new) if new else 0.0

    @staticmethod
    def d_drop(new, prior, benchmark, round_no):
        rep = {_key(c, benchmark): c.id for c in prior}
        kept, members = [], {}
        for c in new:
            k = _key(c, benchmark)
            if k not in rep:
                rep[k] = c.id
                kept.append(c)
            members.setdefault(k, []).append(c.id)
        return kept, [{"cluster_id": f"k{abs(hash(k)) % 10**8}", "rule": "exact", "members": m,
                       "representative_id": rep[k], "round": round_no} for k, m in members.items()]

    @staticmethod
    def admit(pop, cands, conf, verified_ids, k_pop, theta):
        keep = [c for c in pop + cands if c.id in verified_ids or conf.get(c.id, 0) >= theta]
        return sorted(keep, key=lambda c: -conf.get(c.id, 0))[:k_pop]

    @staticmethod
    def g_write(run_dir):
        ids = [r["id"] for f in sorted((Path(run_dir) / "cands").glob("*.jsonl")) for r in read_jsonl(f)]
        Path(run_dir, "graph.jsonl").write_text("".join(json.dumps({"kind": "node", "cand_id": i}) + "\n"
                                                        for i in ids), encoding="utf-8")
        return {"nodes": len(ids)}


def stub_check(run_dir: Path) -> dict:
    nodes = {r["cand_id"] for r in read_jsonl(run_dir / "graph.jsonl")}
    ids = {r["id"] for f in (run_dir / "cands").glob("*.jsonl") for r in read_jsonl(f)}
    return {"ok": ids <= nodes and bool(ids)}


@pytest.fixture(autouse=True)
def lab_root(tmp_path, monkeypatch):
    """Repoint every lab path to tmp_path: harness.config may already have been imported by
    another test file with the real D: root, so the env var alone does not isolate."""
    root = tmp_path / "lab"
    paths = {"LAB_ROOT": root, "RUNS_DIR": root / "runs", "MEMORY_DIR": root / "memory",
             "VIEWS_DIR": root / "memory" / "views", "LEDGER_PATH": root / "memory" / "ledger.jsonl",
             "DATA_DIR": root / "data", "RESULTS_DIR": root / "results"}
    for name, p in paths.items():
        monkeypatch.setattr(config, name, p)
        if name != "LEDGER_PATH":
            p.mkdir(parents=True, exist_ok=True)
    assert Path(config.RUNS_DIR).is_relative_to(tmp_path)
    assert Path(config.LEDGER_PATH).is_relative_to(tmp_path)
    yield root


@pytest.fixture
def stubs(monkeypatch):
    s = Stubs()
    monkeypatch.setattr(think, "_MODS", s.mods)
    # these tests pin the section 4 loop with m_verify capping every benchmark. The judge stays
    # at its default (off for decisions when the check is a free script) and runs on every item
    # as calibration only, so the default path and the EVL-08 calibration log are both exercised
    monkeypatch.setitem(config.FLAGS, "judge_calibration_sample", 1.0)
    monkeypatch.setitem(config.PARAMS, "verify_all_when_free", False)
    yield s
    llm.set_mock(None)


# ---------------------------------------------------------------- helpers
def run_dir_of(batch, item, arm="scaffold", rep=0) -> Path:
    return Path(config.RUNS_DIR) / think.make_run_id(batch, item["benchmark"], item["id"], arm, rep)


def ledger_rows(run_id: str) -> list[dict]:
    return [r for r in read_jsonl(config.LEDGER_PATH) if r.get("run_id") == run_id]


def assert_no_leak(run_dir: Path, item: dict) -> None:
    prompts = list((run_dir / "prompts").glob("*.txt"))
    assert prompts, "no prompts were written"
    if item["benchmark"] == "arc":
        k = item["test_output"]
        needles = [json.dumps(k), json.dumps(k, separators=(",", ":")),
                   " ".join(map(str, k[0])), "".join(map(str, k[0])), "test_output"]
    else:
        needles = ['"label": 0', "'label': 0", '"label":0']
    defaults = read_json(run_dir / "private" / "defaults.json", default={})
    needles += ["zqdflt"]
    for p in prompts:
        text = p.read_text(encoding="utf-8")
        for n in needles:
            assert n not in text, f"{n!r} leaked into {p.name}"
        if isinstance(defaults, dict):
            for v in defaults.values():
                if isinstance(v, str) and len(v) > 20:
                    assert v not in text, f"private/defaults content leaked into {p.name}"


def assert_run_folder(run_dir: Path) -> dict:
    for name in ("state.json", "answer.json", "problem.md", "private/defaults.json",
                 "clusters.jsonl", "graph.jsonl"):
        assert (run_dir / name).exists(), name
    assert list((run_dir / "calls").glob("*.json")), "no call usage records"
    st = read_json(run_dir / "state.json")
    for k in ("run_id", "item_id", "benchmark", "arm", "backend", "model", "m", "B", "flags",
              "params", "replicate", "verifier_hash"):
        assert k in st, k
    assert st["decisions"] and st["decisions"][-1]["step"] == "final"
    for row in st["decisions"]:
        for k in ("step", "action", "signal", "spent", "round", "T", "pop", "conf", "verifier_hash"):
            assert k in row, k
    return st


def spent_matches_ledger(run_id: str, answer_spent: int) -> None:
    rows = [r for r in ledger_rows(run_id) if not r.get("calibration_only")]   # outside B
    assert sum(r["tokens"]["total_tokens"] for r in rows) == answer_spent


# ---------------------------------------------------------------- contract tests
def test_arc_correct_program_is_verified(stubs):
    item = arc_item("t_arc_ok")
    llm.set_mock(make_mock("arc", CORRECT))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_arc_ok")
    rd = run_dir_of("tc_arc_ok", item)
    assert ans.status == "solved" and ans.verification_type == "demo_match"
    assert ans.answer == [[0, 2, 0, 1], [0, 4, 0, 3]]
    st = assert_run_folder(rd)
    assert st["B_source"].startswith("cold-start")
    assert st["B"] == int(20 * config.PARAMS["max_tokens"]["plain"] * 1.5)
    cycles = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    assert len(cycles) == 1 and cycles[0]["action"] == "stop_verified"
    assert read_json(rd / "answer.json")["status"] == "solved"
    rows = ledger_rows(st["run_id"])
    card_rows = [r for r in rows if r["cand_id"] is None and r["round_type"] == "first"]
    assert len(card_rows) == config.BENCHMARKS["arc"]["n0"] - 1   # 4 stand-in specs
    vrows = [r for r in rows if r["status"] == "verified"]
    assert len(vrows) == 1 and vrows[0]["round_type"] == "first" and vrows[0]["agreement"] == 1.0
    assert {r["round_type"] for r in rows} >= {"encode", "probe", "first", "judge"}
    spent_matches_ledger(st["run_id"], ans.spent_tokens)
    assert stub_check(rd)["ok"]
    assert "test_output" not in stubs.encoded[0]
    assert_no_leak(rd, item)
    runs = read_jsonl(Path(config.RESULTS_DIR) / "tc_arc_ok" / "runs.jsonl")
    assert runs[-1]["run_id"] == st["run_id"] and runs[-1]["status"] == "solved"


def test_arc_identical_wrong_programs_reset_on_dup_rate(stubs):
    item = arc_item("t_arc_dup")
    llm.set_mock(make_mock("arc", WRONG))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_arc_dup")
    rd = run_dir_of("tc_arc_dup", item)
    assert ans.status == "abstain" and ans.answer is None
    assert ans.best_guess == [[1, 0, 2, 0], [3, 0, 4, 0]]
    st = assert_run_folder(rd)
    cycles = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    assert [d["action"] for d in cycles] == ["reset", "reset", "continue"]
    assert cycles[0]["signal"]["dup_rate"] > config.PARAMS["d_max"]
    rts = {r["round_type"] for r in ledger_rows(st["run_id"]) if r["card"] not in
           ("encode", "probe", "judge")}
    assert rts == {"first", "post_reset"}
    clusters = read_jsonl(rd / "clusters.jsonl")
    assert any(len(c["members"]) > 1 for c in clusters)
    assert read_jsonl(rd / "surprises.jsonl"), "conf 1.0 and fail must be a surprise"
    spent_matches_ledger(st["run_id"], ans.spent_tokens)
    assert stub_check(rd)["ok"]
    assert_no_leak(rd, item)


def test_arc_varied_wrong_programs_revise_then_stale_reset(stubs):
    item = arc_item("t_arc_bad")
    llm.set_mock(make_varied_mock())
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_arc_bad")
    rd = run_dir_of("tc_arc_bad", item)
    assert ans.status == "abstain" and ans.rounds == 3
    st = assert_run_folder(rd)
    cycles = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    assert [d["action"] for d in cycles] == ["continue", "reset", "continue"]
    assert [d["signal"]["stale"] for d in cycles[:2]] == [1, 2]
    rows = ledger_rows(st["run_id"])
    rts = {r["round_type"] for r in rows if r["card"] not in ("encode", "probe", "judge")}
    assert rts == {"first", "revise", "post_reset"}
    assert len([r for r in rows if r["round_type"] == "revise" and r["cand_id"] is None]) <= 2
    revised = [r for f in (rd / "cands").glob("*.jsonl") for r in read_jsonl(f) if r["parent_ids"]]
    assert revised, "revise children carry parent_ids"
    vrows = [r for r in rows if r["status"] == "fail"]
    assert len([r for r in vrows if r["round"] == 0]) == config.PARAMS["m_verify"]
    assert read_jsonl(rd / "surprises.jsonl")
    spawned = [t for d in cycles for t in d["signal"]["spawned"] if not t.startswith("revise")]
    assert len(spawned) == len(set(spawned)), "no (card, operator, seed, perm) tuple repeats"
    spent_matches_ledger(st["run_id"], ans.spent_tokens)
    assert_no_leak(rd, item)


def test_bt_returns_unverified_best_guess(stubs):
    item = bt_item("t_bt")
    llm.set_mock(make_mock("bt", letter="B"))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_bt")
    rd = run_dir_of("tc_bt", item)
    assert ans.status == "unverified" and ans.answer == "B"
    assert ans.verification_type == "agreement"
    st = assert_run_folder(rd)
    assert not [r for r in ledger_rows(st["run_id"]) if r["round_type"] == "revise"]   # never on BT
    assert "label" not in stubs.encoded[0]
    assert_no_leak(rd, item)


def test_budget_from_cost_jsonl_and_budget_stop(stubs):
    item = arc_item("t_arc_budget")
    append_jsonl(Path(config.RESULTS_DIR) / "tc_budget" / "cost.jsonl",
                 [{"benchmark": "arc", "backend": "mock", "item_id": f"i{i}", "total_tokens": t}
                  for i, t in enumerate((10, 20, 30))])
    llm.set_mock(make_mock("arc", CORRECT))
    ans = think.think(item, m=5, replicate=0, backend="mock", batch="tc_budget")
    st = read_json(run_dir_of("tc_budget", item) / "state.json")
    assert st["B"] == 100 and st["B_source"].startswith("cost.jsonl")
    assert ans.status == "abstain"
    assert st["decisions"][-1]["signal"]["cause"] == "budget_stop"


def test_early_stop_off_keeps_running_and_still_solves(stubs):
    item = arc_item("t_arc_noes")
    llm.set_mock(make_mock("arc", CORRECT))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_noes",
                      flags={"early_stop": False})
    assert ans.status == "solved" and ans.rounds > 1


def test_p1_flags_are_noop_hooks(stubs):
    item = arc_item("t_arc_p1")
    llm.set_mock(make_varied_mock())
    flags = {"lemmas": True, "card_decompose": True, "harvest_unspoken": "capture",
             "gap_pack": "goal_keyed", "frontier": "smc", "verify_order": "top_conf_plus_explore",
             "restructure": True, "signature": True}
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="tc_p1", flags=flags)
    st = read_json(run_dir_of("tc_p1", item) / "state.json")
    hooks = st["p1_hooks_skipped"]
    for name in ("lemmas.lemma_check", "card_decompose.compose_parts", "harvest_unspoken",
                 "gap_pack.gaps_write", "frontier.smc", "verify_order.top_conf_plus_explore",
                 "restructure", "signature", "lemmas.cross_lint"):
        assert name in hooks, name
    assert ans.status == "abstain"


def test_unknown_flag_and_existing_run_folder(stubs):
    with pytest.raises(ValueError):
        think.think(arc_item("t_x"), m=1, replicate=0, backend="mock", batch="tc_x",
                    flags={"no_such_flag": 1})
    item = arc_item("t_twice")
    llm.set_mock(make_mock("arc", CORRECT))
    think.think(item, m=20, replicate=0, backend="mock", batch="tc_twice")
    with pytest.raises(FileExistsError):
        think.think(item, m=20, replicate=0, backend="mock", batch="tc_twice")


def test_cli_value_parsing():
    assert think._kv(["early_stop=false", "R_max=4", "T=0.5", "gap_pack=off", "snapshot=none"]) == {
        "early_stop": False, "R_max": 4, "T": 0.5, "gap_pack": "off", "snapshot": None}


def test_driver_forwarding_and_submodules():
    assert _pkg.think is think.think and _pkg.main is think.main
    assert importlib.import_module("harness.think.dedup").dedup_key


# ---------------------------------------------------------------- end-to-end on the real modules
def _real_modules_missing() -> list[str]:
    missing = []
    for name in think._DEP_NAMES.values():
        try:
            importlib.import_module(f"harness.{name}")
        except Exception:  # noqa: BLE001
            missing.append(name)
    return missing


@pytest.fixture
def real(monkeypatch):
    missing = _real_modules_missing()
    if missing:
        pytest.skip(f"real modules not yet available: {missing}")
    monkeypatch.setattr(think, "_MODS", {})
    yield
    llm.set_mock(None)


@pytest.mark.parametrize("expect", ["solved", "abstain"])
def test_e2e_arc(real, expect):
    item = arc_item(f"e2e_arc_{expect}")
    llm.set_mock(make_mock("arc", CORRECT) if expect == "solved" else make_varied_mock())
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="e2e")
    rd = run_dir_of("e2e", item)
    assert ans.status == expect
    st = assert_run_folder(rd)
    rows = ledger_rows(st["run_id"])
    assert any(r["round_type"] == "first" and r["cand_id"] is None for r in rows)
    assert any(r["status"] in ("verified", "fail") for r in rows)
    assert importlib.import_module("harness.graph").check(rd)["ok"]
    cycles = [d for d in st["decisions"] if d["step"].startswith("cycle")]
    if expect == "solved":
        assert cycles[0]["action"] == "stop_verified" and ans.rounds == 1
    else:
        assert read_jsonl(rd / "surprises.jsonl"), "probe-agreeing failed program is a surprise"
    assert_no_leak(rd, item)


def test_e2e_bt(real):
    item = bt_item("e2e_bt")
    llm.set_mock(make_mock("bt", letter="B"))
    ans = think.think(item, m=20, replicate=0, backend="mock", batch="e2e")
    rd = run_dir_of("e2e", item)
    assert ans.status in ("unverified", "abstain")
    assert_run_folder(rd)
    assert importlib.import_module("harness.graph").check(rd)["ok"]
    assert_no_leak(rd, item)
