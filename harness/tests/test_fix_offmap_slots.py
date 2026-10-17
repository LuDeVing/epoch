"""Issue 4: selection deals build slots in the same shares as ideation dealt idea contexts, so the off-map node
gets its context share of the slots instead of one slot in nine; with no (or equal) weights the order is unchanged."""
import copy
import importlib.util
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

PARTS = ["io", "mix", "ffn", "depth", "opt", "data", "recipe", "objective", "offtree"]


def _by_node(n_per_dir: int = 12, prior: str = "known") -> dict:
    out = {}
    for nid in PARTS:
        out[nid] = [{"cluster_id": f"{nid}-{d[:2]}-{j}", "direction": d, "score": 10 - j, "node": nid,
                     "prior": ("new" if (prior == "mixed" and j % 3 == 0) else "known")}
                    for d in ("inward", "outward") for j in range(n_per_dir)]
    return out


def _ranked(cands, k, exclude=set(), sketches=None):
    return sorted(cands, key=lambda c: -c["score"])


def _old_tree():
    """nano/tree.py as committed before this fix, loaded under another module name."""
    src = subprocess.run(["git", "show", "HEAD~0:nano/tree.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
    if src.returncode != 0 or "weights" in src.stdout.split("def split_select", 1)[-1].split("return chosen", 1)[0]:
        src = subprocess.run(["git", "log", "--format=%H", "-n", "50", "--", "nano/tree.py"], cwd=ROOT,
                             capture_output=True, text=True)
        for sha in src.stdout.split():          # the newest commit whose split_select has no weights
            body = subprocess.run(["git", "show", f"{sha}:nano/tree.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8").stdout
            if "weights" not in body.split("def split_select", 1)[-1].split("return chosen", 1)[0]:
                src = subprocess.CompletedProcess([], 0, body, "")
                break
    spec = importlib.util.spec_from_loader("nano_tree_old", loader=None)
    mod = importlib.util.module_from_spec(spec)
    mod.__dict__["__package__"] = "nano"            # its relative imports resolve against the live package
    sys.modules["nano_tree_old"] = mod
    exec(compile(src.stdout, "nano_tree_old.py", "exec"), mod.__dict__)
    return mod


def test_offtree_gets_its_context_share_of_slots():
    from nano import tree
    other = 0.6 / 8
    weights = {nid: (0.4 if nid == "offtree" else other) for nid in PARTS}
    chosen = tree.split_select(_by_node(), 20, 0.6, set(), [], _ranked, new_share=0.0, counts={},
                               order_seed="t", weights=weights)
    per = Counter(c["node"] for c in chosen)
    assert len(chosen) == 20
    assert 7 <= per["offtree"] <= 9, per
    assert set(per) == set(PARTS), per                       # no part with candidates starves
    # the same with integer context counts (what the loop passes): 6 per part, offtree 32 = 0.4 of 80
    ctx = {nid: (32 if nid == "offtree" else 6) for nid in PARTS}
    chosen2 = tree.split_select(_by_node(), 20, 0.6, set(), [], _ranked, new_share=0.0, counts={},
                                order_seed="t", weights=ctx)
    per2 = Counter(c["node"] for c in chosen2)
    assert 7 <= per2["offtree"] <= 9 and set(per2) == set(PARTS), per2


def test_no_or_equal_weights_match_the_old_function():
    from nano import tree
    old = _old_tree()
    for k, share, counts, prior in ((20, 0.6, {}, "known"), (8, 0.6, {"recipe": 5, "data": 2}, "known"),
                                     (13, 0.5, {"offtree": 1}, "mixed"), (3, 0.6, {}, "mixed")):
        for weights in (None, {}, {nid: 2.0 for nid in PARTS}):
            a_in, b_in = _by_node(prior=prior), _by_node(prior=prior)
            ca, cb = dict(counts), dict(counts)
            kw = {} if weights is None else {"weights": weights}
            new = tree.split_select(a_in, k, share, {"io-in-0"}, [], _ranked, new_share=0.5, counts=ca, order_seed="s", **kw)
            ref = old.split_select(b_in, k, share, {"io-in-0"}, [], _ranked, new_share=0.5, counts=cb, order_seed="s")
            assert [c["cluster_id"] for c in new] == [c["cluster_id"] for c in ref], (k, weights)
            assert ca == cb and a_in == b_in


def test_missing_node_weight_falls_back_to_the_floor():
    from nano import tree
    by_node = _by_node()
    w = {"offtree": 4.0, "io": 1.0}                           # other parts unknown: they get the smallest weight
    chosen = tree.split_select(copy.deepcopy(by_node), 18, 0.6, set(), [], _ranked, new_share=0.0, counts={},
                               order_seed="t", weights=w)
    per = Counter(c["node"] for c in chosen)
    assert set(per) == set(PARTS) and per["offtree"] >= 4, per
