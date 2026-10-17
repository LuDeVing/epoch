"""Cheap, GPU-free checks of the nano loop's pure parts: controls, the planner parser, the dry-run mock."""
import json
import os
from pathlib import Path

os.environ.setdefault("HTSA_LAB_ROOT", "D:/AGI-lab")
ROOT = Path(__file__).resolve().parents[2]
BASE = (ROOT / "nano" / "train.py").read_text(encoding="utf-8")


def test_every_control_passes_the_boundary_check():
    from nano import boundary, controls
    built = controls.build(BASE)
    assert {"placebo_order", "zero_init_proj", "lr_x10"} <= set(built)
    for name, c in built.items():
        assert c["source"] is not None and c["source"] != BASE, name
        b = boundary.check_boundary(BASE, c["source"], None)
        assert b["ok"], (name, b["violations"])           # the placebo once edited Shards.__init__, which is protected
    assert built["placebo_order"]["source"].count("cfg.seed + 7919") == 1
    assert "Shards.__init__" not in boundary.check_boundary(BASE, built["placebo_order"]["source"], None)["changed"]


def test_control_judgement():
    from nano import controls
    assert controls.judge("placebo_order", "fail")["ok"] and controls.judge("placebo_order", "fail", rung=3)["ok"]
    assert not controls.judge("placebo_order", "fail", rung=0)["ok"]        # stopped before training: broken, not a pass
    assert not controls.judge("lr_x10", "fail", rung=1)["ok"]
    assert controls.judge("placebo_order", "checked", "fail")["ok"]
    assert not controls.judge("placebo_order", "checked", "verified")["ok"]
    assert controls.judge("zero_init_proj", "checked")["ok"] and not controls.judge("zero_init_proj", "fail")["ok"]
    assert controls.judge("lr_x10", "fail")["ok"] and not controls.judge("lr_x10", "checked")["ok"]
    # overnight: no ladder; an error is never a pass, a loser must not place, a winner must, a placebo must not
    assert not controls.judge_overnight("lr_x10", "error")["ok"] and controls.judge_overnight("lr_x10", "fail")["ok"]
    assert not controls.judge_overnight("lr_x10", "close_call")["ok"]
    assert controls.judge_overnight("zero_init_proj", "stackable")["ok"] and not controls.judge_overnight("zero_init_proj", "fail")["ok"]
    assert controls.judge_overnight("placebo_order", "fail")["ok"] and not controls.judge_overnight("placebo_order", "verified")["ok"]


def test_planner_parser_and_mock_replan():
    from nano import dry_run, tree
    assert tree.parse_planner("no") is None
    assert tree.parse_planner(json.dumps([{"id": "a", "name": "a", "frame": "f", "assumptions": []}])) is None   # fewer than 4
    text = dry_run.mock("", "encode", {"card": "replan"})
    nodes = tree.parse_planner(text)
    assert nodes and nodes[0]["id"] == "root" and nodes[-1]["id"] == "recipe"
    ids = [n["id"] for n in nodes]
    assert "sched" in ids and "mix" in ids and len(ids) >= 6
    ffn = next(n for n in nodes if n["id"] == "ffn")
    assert "the gate is applied after attention" in ffn["assumptions"]


def test_split_select_does_not_starve_the_last_parts():
    """Eight parts, eight slots (60% inward): every part gets exactly one slot, in whichever direction,
    and a later call with the carried counts starts from the parts that have had the fewest."""
    from collections import Counter
    from nano import tree
    parts = ["io", "mix", "ffn", "depth", "opt", "data", "recipe", "objective"]
    by_node = {}
    for i, nid in enumerate(parts):
        by_node[nid] = [{"cluster_id": f"{nid}-in-k{j}", "direction": "inward", "score": 10 - j, "prior": "known", "node": nid} for j in range(2)] + \
                       [{"cluster_id": f"{nid}-ou-k{j}", "direction": "outward", "score": 10 - j, "prior": "known", "node": nid} for j in range(2)]
    ranked = lambda cands, k, exclude=set(), sketches=None: sorted(cands, key=lambda c: -c["score"])   # noqa: E731
    counts: dict[str, int] = {}
    chosen = tree.split_select(by_node, 8, 0.6, set(), [], ranked, new_share=0.0, counts=counts, order_seed="t")
    per_part = Counter(c["node"] for c in chosen)
    assert len(chosen) == 8 and set(per_part) == set(parts) and max(per_part.values()) == 1, per_part
    assert sum(1 for c in chosen if c["direction"] == "inward") == 5
    # a second call for 3 slots with the carried counts: nothing is starved across calls either
    counts2 = dict(counts); counts2["io"] = 0; counts2["objective"] = 0          # pretend two parts had no build
    again = tree.split_select(by_node, 3, 0.6, {c["cluster_id"] for c in chosen}, [], ranked, new_share=0.0, counts=counts2, order_seed="t")
    assert {c["node"] for c in again} >= {"io", "objective"}
    # the old behaviour, for contrast: map order every pass would have given the first parts two slots
    old = tree.split_select(by_node, 8, 0.6, set(), [], ranked, new_share=0.0, counts={"recipe": 5, "objective": 5, "data": 5}, order_seed="t")
    assert Counter(c["node"] for c in old)["data"] == 0            # parts with many builds yield their turn


def test_ledger_memory_reaches_briefs_once_and_filtered(tmp_path):
    """Stackable rows reach the briefs; mock runs and controls do not; ledger lines render once, after the
    literature, capped; a brief ages from its own research time, not from the file's last rewrite."""
    import json, time
    from nano import research
    rows = [{"hypothesis": "stackable trick", "status": "stackable", "delta": -0.003, "n_seeds": 3, "run": "real-1", "cand_id": "n1"},
            {"hypothesis": "mock trick", "status": "verified", "delta": -0.01, "n_seeds": 3, "run": "mock-dry9", "cand_id": "n2"},
            {"hypothesis": "control: placebo", "status": "fail", "delta": 0.0, "n_seeds": 1, "run": "real-1", "cand_id": "ctl_placebo_order"},
            {"hypothesis": "failed trick", "status": "fail", "delta": 0.004, "n_seeds": 3, "run": "real-1", "cand_id": "n3"}]
    led = tmp_path / "ledger.jsonl"
    led.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    known, failed = research.ledger_entries(led, None, "v1")
    assert [e["name"] for e in known] == ["stackable trick"] and [e["name"] for e in failed] == ["failed trick"]
    brief = {"node": "mix", "known": [{"name": "lit", "mechanism": "m", "effect": "e", "where": "w", "url": "https://x"}] + known,
             "failed": failed, "open": [],
             "tried": [{"name": e["name"], "why": e.get("effect") or e.get("why", ""), "url": e["url"]} for e in known + failed]}
    txt = research.brief_text(brief)
    assert txt.count("stackable trick") == 1 and txt.count("failed trick") == 1
    assert txt.index("KNOWN: lit") < txt.index("MEASURED HERE") < txt.index("TRIED: stackable trick") < txt.index("TRIED: failed trick")
    # ageing by the brief's own timestamp
    cache = tmp_path / "research"
    research.save_cache(cache, {"node": "mix", "known": [], "failed": [], "open": [], "backend": "cli_json"})
    d = json.loads((cache / "mix.json").read_text(encoding="utf-8"))
    d["ts"] = time.time() - 10 * 86400
    (cache / "mix.json").write_text(json.dumps(d), encoding="utf-8")       # rewritten now: mtime is fresh, ts is old
    assert research.load_cached(cache, "mix", 7) is None
    assert research.load_cached(cache, "mix", 30) is not None
    d["ts"] = "2026-10-11T18:39:40"                                           # the real briefs carry an ISO date
    (cache / "mix.json").write_text(json.dumps(d), encoding="utf-8")
    assert research.load_cached(cache, "mix", 1) is None and research.load_cached(cache, "mix", 3650) is not None


def test_offshoot_part_and_prediction_noise_floor():
    from nano import ideate, predict
    text = ("IDEA: faster warmup\nMECHANISM: shorter warmup for the embedding rows only.\nPREDICTION: lower loss\n"
            "TEST: 1-minute smoke run\nSOURCE: own\nPART: optimization\n\n"
            "IDEA: x\nMECHANISM: y\nPREDICTION: z\nTEST: t\nSOURCE: own")
    sk = ideate.parse_sketches(text, card="deepen", operator="inward", seed="", call_id="c", idgen=lambda: "s1")
    assert sk[0]["part"] == "optimization" and sk[1]["part"] == ""
    # a predicted gain smaller than two seed spreads cannot be tested at this rung: not counted as held
    pred = {"loss": {"gap": -0.001, "claim": "loss lower by 0.001", "steps": 45}}
    r = predict.check_prediction(pred, {"learn_gap": 0.0, "learn_sd": 0.02}, {})
    assert not r.get("checkable") and any("noise floor" in d for d in r.get("details", []))
    r2 = predict.check_prediction({"loss": {"gap": -0.1, "claim": "loss lower by 0.1", "steps": 45}}, {"learn_gap": 0.0, "learn_sd": 0.02}, {})
    assert r2.get("checkable") and r2.get("ok") is False


def test_delegated_web_protocol_parsing():
    from nano import research
    qs = research.parse_questions("Some preamble\nQUESTIONS:\n1. what did 2026 work measure for gated attention?\n2) does value residual help at 21M params?\n- short\n3. is sliding window measured at 1024 tokens?\n\nIDEA: x")
    assert qs == ["what did 2026 work measure for gated attention?", "does value residual help at 21M params?", "is sliding window measured at 1024 tokens?"]
    assert research.parse_questions("") == [] and len(research.parse_questions("QUESTIONS:\n" + "\n".join(f"{i}. question number {i} here" for i in range(1, 12)))) == 8
    fp = research.findings_prompt(qs, "the part 'attention'")
    assert "1. what did 2026 work measure" in fp and "URL" in fp and "attention" in fp and "FINDINGS:" in fp
    from nano import dry_run
    assert research.parse_questions(dry_run.mock("", "generate", {"card": "sketch:research:questions"}))
    assert "https://" in dry_run.mock("", "research", {"card": "sketch:research:findings"})


def test_leap_sketches_parse_and_cluster():
    from nano import ideate
    text = ("PASS 1 (scratch):\n- seed a\n- seed b\n\n"
            "IDEA: per-layer loss weights\nMECHANISM: weight each layer's contribution.\nPREDICTION: lower loss\nTEST: 45 steps\nSOURCE: own\n"
            "TARGET: validation loss only\nSCOPE: validation loss at 1024\nKIND: leap\nBREAKS: every token has equal weight in the loss\n"
            "KEEPS: the model and the optimiser\nP_SUCCESS: 15%\nKILL: gap above +0.05 at 45 steps\n\n"
            "IDEA: qk norm\nMECHANISM: normalise q and k.\nPREDICTION: lower loss\nTEST: 45 steps\nSOURCE: https://x\nKIND: port")
    sk = ideate.parse_sketches(text, card="research", operator="inward", seed="", call_id="c", idgen=iter(["s1", "s2"]).__next__)
    assert len(sk) == 2 and sk[0]["kind"] == "leap" and sk[1]["kind"] == "port"
    assert sk[0]["breaks"].startswith("every token") and sk[0]["keeps"].startswith("the model") and sk[0]["kill"].startswith("gap above")
    assert sk[0]["p_success"] == 0.15 and sk[1]["p_success"] is None
    sk[0]["leap_op"] = "rulebreak"
    cl = ideate.build_clusters([{"name": "g", "members": ["s1", "s2"]}], sk)[0]
    assert cl["leap_share"] == 0.5 and cl["leap_ops"] == ["rulebreak"]
    brief = ideate.implement_brief({"representative": "s1", "members": ["s1"]}, sk)
    assert "KIND: leap" in brief and "BREAKS: every token" in brief and "KILL: gap above" in brief
    add = ideate.LEAP_ADDENDUM.format(n=2, op_name="subtract", op_text=ideate.LEAP_OPERATORS["subtract"])
    assert "at least 2 of your sketches must be leaps" in add and "subtract" in add and len(ideate.LEAP_OPERATORS) == 8


def test_lane_reserves_slots_for_leaps():
    import random
    from nano import ideate
    cands = [{"cluster_id": f"p{i}", "score": 5.0, "leap_share": 0.0} for i in range(6)] + [{"cluster_id": "L1", "score": 0.0, "leap_share": 1.0}]
    picks = ideate.draw_lane(cands, 2, random.Random(1))
    assert len(picks) == 2 and any(c["cluster_id"] == "L1" for c in picks)          # the weak-scored leap still gets a slot
    picks = ideate.draw_lane([c for c in cands if c["cluster_id"] != "L1"], 2, random.Random(1))
    assert len(picks) == 2                                                             # no leaps: the lane still fills
    assert ideate.draw_lane(cands, 0, random.Random(1)) == [] and ideate.draw_lane([], 3, random.Random(1)) == []


def _diag(seed, late_bump=0.0, rms_bump=0.0, rare=10.5):
    """A synthetic diagnostics json: smooth families plus seed noise, with optional injected anomalies."""
    import random
    r = random.Random(seed)
    layers = []
    for i in range(12):
        layers.append({"layer": i, "grad_attn": round(0.6 - 0.02 * i + r.gauss(0, 0.004), 4), "grad_mlp": round(0.3 + 0.01 * i + r.gauss(0, 0.004), 4),
                       "act_rms": round(1.5 + 0.2 * i + r.gauss(0, 0.01) + (rms_bump if i == 7 else 0.0), 4),
                       "attn_entropy": round(1.0 - 0.03 * i + r.gauss(0, 0.004), 4), "max_logit": round(5 + 0.5 * i + r.gauss(0, 0.05), 3),
                       "first_token_mass": round(0.2 - 0.005 * i + r.gauss(0, 0.002), 4)})
    probe = {"step": 100, "probe_loss": 6.4,
             "by_position": {"0-64": round(6.9 + r.gauss(0, 0.01), 4), "64-256": round(6.5 + late_bump + r.gauss(0, 0.01), 4), "256-1024": round(6.2 + r.gauss(0, 0.01), 4)},
             "by_frequency": {"rank 0-100": {"loss": round(3.0 + r.gauss(0, 0.01), 4), "share": 0.4}, "rank 100-1000": {"loss": round(6.0 + r.gauss(0, 0.01), 4), "share": 0.3},
                              "rank 1000-10000": {"loss": round(8.5 + r.gauss(0, 0.01), 4), "share": 0.2}, "rank 10000-50304": {"loss": round(rare + r.gauss(0, 0.02), 4), "share": 0.1}},
             "layers": layers, "grad_embedding": 0.5}
    return {"steps": 100, "seed": seed, "probes": [probe], "ts": "t"}


def test_anomaly_map_flags_injected_cells_and_shams(tmp_path):
    import json, random
    from nano import anomaly
    paths = []
    for s in range(3):
        p = tmp_path / f"d{s}.json"
        p.write_text(json.dumps(_diag(s, late_bump=0.25, rms_bump=0.6, rare=11.2)), encoding="utf-8")
        paths.append(p)
    out = anomaly.compute(paths, run_id="t", sham_share=0.0)
    cells = {a["cell"] for a in out["anomalies"]}
    keys = {a["key"] for a in out["anomalies"]}
    assert out["n_seeds"] == 3 and "layer7:act_rms" in keys and "freq:rank 10000-50304" in keys, out["anomalies"]
    assert "pos:64-256" not in keys                                     # three buckets have no trend to be off
    assert {"rare", "rms"} <= cells and out["sham"] is None and "uniform guessing" in out["text"]
    # a quiet table flags nothing
    for s in range(3):
        (tmp_path / f"d{s}.json").write_text(json.dumps(_diag(s)), encoding="utf-8")
    quiet = anomaly.compute(paths, run_id="t", sham_share=0.0)
    assert quiet["anomalies"] == []
    # a sham row is fabricated from a quiet cell, recorded, and chasing is counted by TARGET cell
    sham = anomaly.compute(paths, run_id="t", sham_share=1.0)
    assert sham["sham"] and sham["sham"]["text"] in sham["text"]
    sk = [{"target": "loss at late positions, down"}, {"target": "validation loss only"}, {"target": "attention entropy in deep layers"}]
    assert anomaly.chased(sk, {"cell": "late"}) == 1 and anomaly.chased(sk, None) == 0
    assert anomaly.aimed(sk, [{"cell": "entropy"}, {"cell": "late"}]) == 2
    assert anomaly.cell_of("first-token attention mass") == "first" and anomaly.cell_of("nothing") is None


def test_owner_and_anomaly_addenda():
    from nano import ideate
    assert "OWNER" in ideate.OWNER_ADDENDUM.format(text="gate the residual") and "gate the residual" in ideate.OWNER_ADDENDUM.format(text="gate the residual")
    assert "rival causes" in ideate.ANOMALY_ADDENDUM.format(text="- row") and "owner" in ideate.DEPARTURE_CARDS


def test_tuning_sweep_builds_single_knob_variants():
    from nano import tune, boundary, ideate
    built = tune.build(BASE)
    assert len(built) == len(tune.DEFAULT) and tune.current(BASE, "lr") == 0.02
    for name, v in built.items():
        diff = [(a, b) for a, b in zip(BASE.splitlines(), v["source"].splitlines()) if a != b]
        assert len(diff) == 1 and v["field"] in diff[0][0], (name, diff)        # exactly one line changes, the knob's
        assert v["new"] != v["old"] and boundary.check_boundary(BASE, v["source"], None)["ok"]
    assert abs(built["lr_x1.4"]["new"] - 0.028) < 1e-9 and built["rope_theta_50k"]["new"] == 50000.0
    assert tune.build(BASE, ["warmup_0.05", "nonsense"]).keys() == {"warmup_0.05"}
    assert tune.build(BASE.replace("warmup_frac: float = 0.02", "warmup_frac: float = 0.05"), ["warmup_0.05"]) == {}   # no change, no variant
    assert ideate._kind("tune") == "tune" and ideate._kind("tuning") == "tune"


def test_mock_variant_build_parses():
    import ast as _ast, re
    from nano import dry_run
    prompt = "The script above is a previous attempt. Apply the operator 'variant:relax': fix = ..."
    out = dry_run.mock(prompt, "generate", {"card": "revise", "operator": "variant:relax", "node": "mix"})
    code = re.search("```python(.*)```", out, flags=re.S).group(1)
    _ast.parse(code)
    assert "marker_variant" in code


def test_interrogation_chain_forks_provenance_and_stop():
    from nano import deepen, dry_run
    root = dry_run.mock("", "generate", {"card": "deepen", "depth": 0, "gen": 0, "node": "mix"})
    p = deepen.parse(root)
    assert [l["id"] for l in p["chain"]] == ["L1", "L2"] and p["weakest"] == "L2" and p["chain"][1]["quantity"] == "validation loss"
    assert p["chain"][0]["breaks_if"].startswith("RMS unchanged")
    assert p["qa"][0]["decides"] == "option A vs option B" and p["qa"][0]["q"].startswith("what about aspect 1")
    provs = {t["prov"] for t in p["known_tagged"]}
    assert {"script", "web", "belief"} <= provs and not any("saturates" in k for k in p["known"])   # beliefs are not facts
    assert p["dropped_unsourced"] == 1 and p["open"][0]["decides"] == "warmup 2% vs 5%" and p["open"][0]["build"] and not p["open"][1]["build"]
    assert deepen.stop_here(p, 0) is None
    child = deepen.parse(dry_run.mock("", "generate", {"card": "deepen", "depth": 1, "gen": 0, "node": "mix"}))
    assert [(s["id"], s["status"]) for s in child["link_status"]] == [("L1", "confirmed"), ("L2", "open")]
    assert deepen.stop_here({"qa": [{"a": "unknown"}] * 3 + [{"a": "fact"}], "unknown_share": 0.75}, 0) == "half the answers were unknown"
    assert deepen.stop_here({"qa": [], "known": [], "link_status": [{"id": "L1", "status": "open"}]}, 1) == "no new fact and no link settled"
    assert deepen.stop_here({"qa": [], "known": ["x"], "link_status": []}, 1) is None
    # the weakest link's questions go first
    oq = [{"q": "is it elegant", "build": True, "decides": ""}, {"q": "does validation loss fall by 240 steps", "build": True, "decides": "long run yes vs no"}]
    assert deepen.follow(oq, 1, "smaller growth -> lower loss validation loss")[0].startswith("does validation loss")
    txt = deepen.knowledge_text([{"id": "d1", "chain": p["chain"], "known_tagged": p["known_tagged"], "known": p["known"], "qa": p["qa"], "depth": 0},
                                 {"id": "d2", "root": "d1", "parent": "d1", "link_status": child["link_status"], "known": [], "qa": [], "depth": 1}])
    assert "MECHANISM CHAIN" in txt and "status: confirmed" in txt and "UNVERIFIED BELIEFS" in txt and "[script]" in txt and "[decides:" in txt
    pm = deepen.premortem_prompt("idea", "mix", "- rules", "code", ["f"], chain=deepen.chain_text(p["chain"]))
    assert "| link: L<n>" in pm and "L2:" in pm


def test_lessons_file_from_a_run(tmp_path):
    import json
    from nano import lessons
    run = tmp_path / "run-1__nano__x"; (run / "cands").mkdir(parents=True)
    rows = [{"id": "n1", "card": "impl", "extra": {"node": "mix"}, "parent_ids": []}, {"id": "n2", "card": "impl", "extra": {"node": "mix"}, "parent_ids": []},
            {"id": "n3", "card": "fix", "extra": {"node": "mix"}, "parent_ids": ["n1"]}, {"id": "n4", "card": "impl", "extra": {"node": "ffn"}, "parent_ids": []}]
    (run / "cands" / "a.jsonl").write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")
    ver = [{"id": "n1", "status": "fail", "feedback_record": {"rung": 0, "reason": "the change reaches outside the part's boundary or touches protected code", "violations": ["MLP.__init__ changed but lies outside this part's boundary (Attention)"]}},
           {"id": "n2", "status": "fail", "feedback_record": {"rung": 0, "reason": "the change reaches outside the part's boundary or touches protected code", "violations": ["MLP.forward changed but lies outside this part's boundary (Attention)"]}},
           {"id": "n3", "status": "checked", "feedback_record": {}}, {"id": "n4", "status": "fail", "feedback_record": {"rung": 3, "reason": "loss did not fall"}}]
    (run / "verify.jsonl").write_text("\n".join(json.dumps(v) for v in ver), encoding="utf-8")
    (run / "rung5").mkdir(); (run / "rung5" / "results.json").write_text(json.dumps({"candidates": {"n9": {"status": "stackable", "hypothesis": "zero-init gate", "delta": -0.003, "n_seeds": 3, "part": "mix"}}}), encoding="utf-8")
    path = tmp_path / "lessons.jsonl"
    out = lessons.update_from_run(run, path, "v1")
    entries = lessons.load(path)
    pits = [e for e in entries if e["kind"] == "pitfall"]
    assert len(pits) == 1 and len(pits[0]["evidence"]) == 2 and pits[0]["helpful"] == 1 and pits[0]["state"] == "hypothesis" and "outside the part's boundary" in pits[0]["text"]
    assert any(e["kind"] == "outcome" and "helped (stackable" in e["text"] for e in entries)
    txt = lessons.render(path, part="mix", kind="pitfall", version="v1")
    assert "PITFALLS" in txt and "seen 2 times, fixed 1x" in txt and lessons.render(path, part="ffn", kind="pitfall") == ""
    # a second run with the same pitfall raises its standing; the file is never rewritten by hand
    run2 = tmp_path / "run-2__nano__x"; (run2 / "cands").mkdir(parents=True)
    (run2 / "cands" / "a.jsonl").write_text(json.dumps({"id": "m1", "card": "impl", "extra": {"node": "mix"}, "parent_ids": []}), encoding="utf-8")
    (run2 / "verify.jsonl").write_text(json.dumps(ver[0] | {"id": "m1"}), encoding="utf-8")
    lessons.update_from_run(run2, path, "v1")
    assert [e for e in lessons.load(path) if e["kind"] == "pitfall"][0]["state"] == "supported"


def test_reach_audit_verdicts(tmp_path):
    """One forward and backward pass on the processor tells a no-op marker, a dead parameter, a trained
    zero-init gate and a constants-only change apart."""
    from nano import audit
    anchor = "        self.attn, self.mlp = Attention(cfg), MLP(cfg)"
    ret = "        return self.combine(x, branch, 1)"                 # the edits below must land on lines that exist
    assert BASE.count(anchor) == 1 and BASE.count(ret) == 1
    cases = {
        "marker": (BASE.replace(anchor, anchor + "\n        self.marker = 1", 1), ["Block.__init__"], "no_effect_suspect"),
        "dead": (BASE.replace(anchor, anchor + "\n        self.dead = nn.Parameter(torch.zeros(1))", 1), ["Block.__init__"], "dead_path"),
        "gate": (BASE.replace(anchor, anchor + "\n        self.g = nn.Parameter(torch.zeros(1))", 1)
                 .replace(ret, "        return self.combine(x, branch * (1 + self.g), 1)", 1),
                 ["Block.__init__", "Block.forward"], "ok"),
        "lr": (BASE.replace("    lr: float = 0.02 ", "    lr: float = 0.028", 1), ["Config"], "ok"),
        # identical at init only: the final gain multiplies the lookup too (a gain of one changes nothing at step 0)
        "gain_tie": (BASE.replace("self.tok(idx).unsqueeze(2)", "(self.tok(idx) * self.norm.weight).unsqueeze(2)", 1), ["GPT.forward"], "ok"),
        # dead at init only: a zero table feeding a projection; the projection gets gradient once the table moves
        "zero_chain": (BASE.replace(anchor, anchor + "\n        self.t2 = nn.Linear(cfg.d_model, 8, bias=False); nn.init.zeros_(self.t2.weight); self.pj = nn.Linear(8, cfg.d_model, bias=False)", 1)
                       .replace(ret, "        return self.combine(x, branch + self.pj(self.t2(branch)), 1)", 1),
                       ["Block.__init__", "Block.forward"], "ok"),
    }
    base = tmp_path / "train.py"; base.write_text(BASE, encoding="utf-8")
    for name, (src, changed, expect) in cases.items():
        assert src != BASE, name
        c = tmp_path / f"{name}.py"; c.write_text(src, encoding="utf-8")
        res = audit.run(str(c), str(base), changed)
        assert res["verdict"] == expect, (name, res)
        if name == "gate":
            assert res["forward_identical"] and res["new_params"] and not res["dead_params"]
        if name == "dead":
            assert res["dead_params"] and res["dead_params"][0].endswith(".dead")


def test_cost_card_and_lane_interleave_and_failure_card():
    from nano import cost, lessons
    b = cost.breakdown(BASE)
    assert b["params_nonembed"] == 21_243_264 and b["n_layer"] == 12 and b["head_dim"] == 64
    txt = cost.card(BASE, {"params_nonembed": 21_243_264, "step_s": 1.1, "peak_vram_gb": 4.07})
    assert "headroom in parameters: +2,124,326" in txt and "up to 2.20s" in txt and "GB free" in txt and "feed-forward" in txt
    pool = [("p1", {"lane": "main"}), ("p2", {"lane": "main"}), ("p3", {"lane": "main"}), ("p4", {"lane": "main"}), ("p5", {"lane": "main"}),
            ("p6", {"lane": "main"}), ("L1", {"lane": "longshot"}), ("L2", {"kind": "leap", "lane": "main"})]
    order = [x[0] for x in cost.interleave_lane(pool, lambda pm: pm[1].get("lane") in ("longshot", "family") or pm[1].get("kind") == "leap", every=5)]
    assert order[4] == "L1" and order[:4] == ["p1", "p2", "p3", "p4"] and set(order) == {x[0] for x in pool} and len(order) == 8
    assert cost.interleave_lane([("a", {})], lambda pm: False) == [("a", {})]
    card = lessons.failure_card({"rung": 0, "reason": "the change reaches outside the part's boundary or touches protected code",
                                 "violations": ["MLP.__init__ changed but lies outside this part's boundary (Attention)"]})
    assert "CHECK FAILED: rung 0 (boundary)" in card and "WHERE: MLP.__init__" in card and "CAUSE TAG: changed code outside" in card
    assert lessons.failure_card({"near_miss": True, "learn_z": -0.4}).startswith("RECORD: passed")


def test_objections_are_typed_and_resolved_by_the_ladder():
    from nano import deepen, dry_run
    pm = deepen.parse_premortem(dry_run.mock("", "generate", {"card": "premortem"}))
    objs = pm["objections"]
    assert [o["cls"] for o in objs] == ["hidden_cost", "below_noise", "early_only", "metric_blind"]
    assert objs[0]["if_true"] == {"metric": "step_ratio", "op": "above", "threshold": 1.2} and objs[3]["if_true"] is None
    res = deepen.resolve_objections(objs, {"step_ratio": 1.31, "learn_z": -0.9})
    assert [r["status"] for r in res] == ["confirmed", "refuted", "pending", "untestable"] and res[0]["measured"] == 1.31
    res2 = deepen.resolve_objections(objs, {"step_ratio": 1.0, "learn_z": 0.2, "trend": 0.003, "fidelity": {"checkable": True, "ok": False}})
    assert [r["status"] for r in res2] == ["refuted", "confirmed", "confirmed", "untestable"]
    txt = deepen.objections_text(res, "noise")
    assert txt.index("CONFIRMED: step_ratio measured 1.31") < txt.index("test: trend above 0.001") < txt.index("REFUTED")
    # a link citation and a free-text severity still parse
    one = deepen.parse_premortem("OBJECTIONS:\n- the gate saturates | severity: high | class: interaction_cancels | link: L2 | if_true: long_z > 0.5\nVERDICT: v")["objections"][0]
    assert one["link"] == "L2" and one["if_true"]["op"] == "above" and one["severity"] == "high"


def test_critic_check_mutants_and_scoring():
    from nano import critic_check, boundary
    muts = critic_check.build_mutants(BASE)
    assert set(muts) == set(critic_check.MUTANTS)
    for name, m in muts.items():
        assert m["source"] != BASE and boundary.check_boundary(BASE, m["source"], None)["ok"], name
    results = [
        {"name": "hidden_cost", "kind": "mutant", "classes": {"hidden_cost"}, "objections": [{"severity": "high", "cls": "hidden_cost"}, {"severity": "low", "cls": "below_noise"}]},
        {"name": "early_only", "kind": "mutant", "classes": {"early_only"}, "objections": [{"severity": "medium", "cls": "early_only"}]},
        {"name": "silent_noop", "kind": "mutant", "classes": {"impl_slip"}, "objections": [{"severity": "low", "cls": "impl_slip"}]},
        {"name": "zero_init_proj", "kind": "winner", "classes": set(), "objections": [{"severity": "low", "cls": "below_noise"}]},
        {"name": "placebo_order", "kind": "placebo", "classes": set(), "objections": [{"severity": "medium", "cls": ""}]},
    ]
    sc = critic_check.score(results)
    assert abs(sc["recall"] - 2 / 3) < 1e-9 and sc["placebo_high_objections"] == 0 and sc["severity_gap"] > 0
    assert [h["hit"] for h in sc["hits"]] == [True, True, False] and sc["verdict"] == "useful"
    assert critic_check.score([r for r in results if r["kind"] != "mutant"])["recall"] is None


def test_scope_resolves_against_a_renamed_and_split_map():
    """arch-1: the planner split 'mix' into two nodes and renamed every id; --only-nodes io,mix,ffn,depth matched nothing."""
    from nano import tree
    planned = [{"id": "root", "name": "lower validation loss at a fixed budget"},
               {"id": "io_embed_head", "name": "Inputs and outputs: token embedding, tied head, final norm"},
               {"id": "attn_positional", "name": "Sequence mixing: rotary positions and attention geometry"},
               {"id": "attn_heads_windo", "name": "Sequence mixing: head layout, KV sharing, sliding window"},
               {"id": "mlp_ffn", "name": "Per-token computation: SwiGLU feed-forward"},
               {"id": "block_residual", "name": "State across depth: pre-norm residual block and norm placement"},
               {"id": "depth_init", "name": "State across depth: layer count, initialization, inter-layer scaling"},
               {"id": "optimization", "name": "Optimization: Muon plus AdamW, schedule, clipping (frozen this run)"},
               {"id": "data_order", "name": "Data: random window sampling from shards (frozen this run)"},
               {"id": "objective", "name": "Objective: plain next-token cross entropy (frozen this run)"},
               {"id": "recipe", "name": "the whole recipe (cross-part changes)"}]
    got = tree.resolve_scope({"io", "mix", "ffn", "depth"}, planned)
    assert got == {"io_embed_head", "attn_positional", "attn_heads_windo", "mlp_ffn", "block_residual", "depth_init"}
    assert tree.resolve_scope({"mix"}, tree.DEFAULT_TREE) == {"mix"}                      # ids still work on the default map
    assert tree.resolve_scope({"data"}, planned) == {"data_order"} and tree.resolve_scope({"opt"}, planned) == {"optimization"}
    assert tree.resolve_scope(set(), planned) == set()


def test_scope_text_names_the_frozen_parts():
    from nano import tree
    t = tree.scope_text({"io", "mix", "ffn", "depth"})
    assert t.startswith("SCOPE OF THIS RUN") and "- sequence mixing (attention): Attention" in t and "- per-token computation: MLP" in t
    assert "optimization" in t.split(":\n")[0] and "data" in t.split(":\n")[0]        # the frozen parts are named up front
    assert "- optimization" not in t
    assert tree.scope_text(set()) == ""


def test_sketch_cap_deals_across_parts():
    from nano import ideate
    parts = ["io", "mix", "ffn"]
    specs = []
    for p in parts:
        specs += [("seeded", "", {"id": p}, "inward"), ("formal", "", {"id": p}, "outward"), ("diagnosis", "", {"id": p}, "inward")]
    specs.append(("owner", "x", {"id": "ffn"}, "inward"))
    prio = {"owner": -1, "research": 0, "diagnosis": 1, "analogy": 2}
    deal = lambda k: ideate.deal_by_part(specs, k, lambda sp: prio.get(sp[0], 3), lambda sp: sp[2]["id"])
    assert [(sp[0], sp[2]["id"]) for sp in deal(4)] == [("owner", "ffn"), ("diagnosis", "io"), ("diagnosis", "mix"), ("diagnosis", "ffn")]
    six = deal(6)
    assert len(six) == 6 and {sp[2]["id"] for sp in six[4:]} == {"io", "mix"}      # the second pass, one more per part
    one = deal(1)
    assert len(one) == 1 and one[0][0] == "owner"
    assert len(deal(100)) == len(specs)


def test_budget_counts_only_the_inventing_model():
    """One Sonnet web-research call counted 564,531 tokens in a real test (pages re-read per turn); it must not
    starve the builds, and past the cheap model's own cap the run stops searching rather than stopping."""
    import threading
    from types import SimpleNamespace
    from nano.loop import NanoLoop
    from harness.llm import Usage
    ns = SimpleNamespace(model="fable", lock=threading.Lock(), spent=0, spent_aux=0, spent_by_stage={})
    NanoLoop._account(ns, None, {"card": "implement"}, Usage(5000, 12000, 0, 0))
    NanoLoop._account(ns, "sonnet", {"card": "sketch:research:findings"}, Usage(436716, 29282, 69830, 28703))
    NanoLoop._account(ns, "sonnet", {"card": "cluster"}, Usage(4000, 1000, 0, 0))
    assert ns.spent == 17000 and ns.spent_by_stage == {"build": 17000}
    assert ns.spent_aux == 564531 + 5000
    ns2 = SimpleNamespace(aux_budget=1000, spent_aux=999, lock=threading.Lock(), _aux_off_logged=False, decisions=[], round_now=1)
    assert NanoLoop._aux_ok(ns2, "x")
    ns2.spent_aux = 1000
    assert not NanoLoop._aux_ok(ns2, "x") and not NanoLoop._aux_ok(ns2, "y")
    assert len(ns2.decisions) == 1 and ns2.decisions[0]["why"] == "aux budget"
    ns2.aux_budget = 0
    assert NanoLoop._aux_ok(ns2, "x")                           # 0 = no cap


def test_budget_envelopes():
    from nano import budget
    assert budget.stage_of("sketch:research:questions") == "ideation" and budget.stage_of("deepen:findings") == "interrogation"
    assert budget.stage_of("cluster") == "judging" and budget.stage_of("implement") == "build" and budget.stage_of("impl:adapt") == "build"
    assert budget.stage_of("research") == "research" and budget.stage_of("tune") == "build" and budget.stage_of("control:lr_x10") == "build"
    B = 1_000_000
    ok, why = budget.afford(spent=600_000, est=50_000, budget=B, stage="ideation", build_spent=0)
    assert not ok and why == "build floor"                       # 400k of builds still owed; 650k + 400k > 1M
    ok, _ = budget.afford(spent=600_000, est=50_000, budget=B, stage="build", build_spent=0)
    assert ok                                                   # a build call only needs the budget itself
    ok, _ = budget.afford(spent=500_000, est=50_000, budget=B, stage="ideation", build_spent=380_000)
    assert ok                                                   # most of the floor already spent on builds
    assert budget.afford(spent=990_000, est=50_000, budget=B, stage="build", build_spent=0) == (False, "budget")
    assert budget.affordable_slots(spent=900_000, budget=B, k=10) == 5 and budget.affordable_slots(spent=995_000, budget=B, k=10) == 1
    assert budget.affordable_slots(spent=B, budget=B, k=10) == 0


def test_long_objections_keep_their_typed_fields():
    from nano import deepen
    long = "x" * 420
    pm = deepen.parse_premortem(f"OBJECTIONS:\n- {long} | severity: high | class: early_only | if_true: trend below 0\nVERDICT: v")
    o = pm["objections"][0]
    assert o["severity"] == "high" and o["cls"] == "early_only" and o["if_true"] == {"metric": "trend", "op": "below", "threshold": 0.0}
    assert len(o["text"]) == 300


def test_standing_objections_collapse():
    from nano import deepen
    roots = [{"objections": [{"cls": "below_noise", "severity": "medium"}, {"cls": "early_only", "severity": "low"}]} for _ in range(4)]
    roots.append({"objections": [{"cls": "hidden_cost", "severity": "high"}]})
    st = deepen.standing_classes(roots)
    assert st == {"below_noise", "early_only"} and deepen.standing_classes(roots[:2]) == set()
    objs = [{"text": "noise", "severity": "medium", "cls": "below_noise"}, {"text": "cost", "severity": "high", "cls": "hidden_cost"},
            {"text": "fades", "severity": "low", "cls": "early_only", "status": "confirmed", "if_true": {"metric": "trend", "op": "above", "threshold": 0.0}, "measured": 0.01}]
    txt = deepen.objections_text(objs, "", st)
    assert "cost" in txt and "fades" in txt and "- [medium, below_noise] noise" not in txt and "standing objections" in txt and "below_noise" in txt
    assert "1 collapsed" in txt


def test_slots_fidelity_effort_and_fact_check_plumbing():
    from types import SimpleNamespace
    from nano import ideate, loop, dry_run, deepen
    text = dry_run.mock("", "generate", {"card": "deepen", "depth": 0, "gen": 0, "node": "mix"})
    sk = ideate.parse_sketches(deepen.parse(text)["sketch_text"], card="deepen", operator="inward", seed="", call_id="c", idgen=iter(["a", "b", "c"]).__next__)
    assert [s["slot"] for s in sk] == ["drop", "strengthen", "port"]
    parsed = loop._parse("HYPOTHESIS: h\nCHANGE: c\nFIDELITY: substituted, used a gate instead of a mask\n```python\ndef main():\n    pass  # metrics.json\n```")
    assert parsed["fidelity"] == "substituted" and parsed["fidelity_note"].startswith("used a gate")
    assert loop._parse("HYPOTHESIS: h\nCHANGE: c\n```python\ndef main():\n    pass  # metrics.json\n```")["fidelity"] == ""
    me = SimpleNamespace(effort_by_role=True, EFFORT=loop.NanoLoop.EFFORT)
    assert loop.NanoLoop.effort_for(me, "implement") == "high" and loop.NanoLoop.effort_for(me, "deepen") == "medium"
    assert loop.NanoLoop.effort_for(me, "cluster") == "low" and loop.NanoLoop.effort_for(me, "sketch:research:questions") == "low"
    assert loop.NanoLoop.effort_for(me, "sketch:research") is None and loop.NanoLoop.effort_for(SimpleNamespace(effort_by_role=False, EFFORT=loop.NanoLoop.EFFORT), "implement") is None
    txt = deepen.knowledge_text([{"id": "d", "known_tagged": [{"text": "two extra matmuls https://x", "prov": "web", "check": "supported"},
                                                               {"text": "8 percent slower https://y", "prov": "web", "check": "not supported"}], "known": [], "qa": [], "depth": 0}])
    assert "[checked against its source]" in txt and "its source does not support it" in txt
