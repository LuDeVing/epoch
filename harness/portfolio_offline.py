"""Offline replay of a portfolio_arc batch: re-run every saved program (no model calls) and score other selection
rules on the same candidates. Usage:
    HTSA_ARC_SET=arc1mid python -m harness.portfolio_offline D:/AGI-lab/results/arc1mid-portfolio
"""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from . import arc_exec as EX
from . import config
from .arms.plain import parse_program
from .schemas import strip_key


def rot(g):
    return [list(r) for r in zip(*g[::-1])]


def flip(g):
    return [r[::-1] for r in g]


def tr(g):
    return [list(r) for r in zip(*g)]


SYMS = {"rot90": rot, "rot180": lambda g: rot(rot(g)), "rot270": lambda g: rot(rot(rot(g))), "flip": flip,
        "flipv": lambda g: g[::-1], "transpose": tr}


def load(batch: Path, items: dict):
    out = {}
    rows = {json.loads(l)["id"]: json.loads(l) for l in (batch / "portfolio_runs.jsonl").read_text().splitlines() if l.strip()}
    for pid in rows:
        it = items[pid]
        clean = strip_key(it)
        train = clean["train"]
        ins = [p["input"] for p in train]
        t = clean["test_input"]
        # symmetries under which every example is equivariant: f(s(x)) == s(f(x)) holds for the expected outputs?
        cands = []
        for f in sorted((batch / "calls" / pid).glob("*.json")):
            d = json.loads(f.read_text(encoding="utf-8"))
            prog = parse_program(d.get("text") or "")
            if not prog:
                continue
            kind = f.name.split("_")[0]
            sym_in = {k: [s(x) for x in ins + [t]] for k, s in SYMS.items()}
            allin = ins + [t] + [x for k in SYMS for x in sym_in[k]]
            res = EX.execute(prog, allin)
            o = res["outputs"]
            n = len(ins) + 1
            demo = EX.demo_from_outputs(train, o[: len(ins)], res["errors"][: len(ins)])
            base = o[:n]
            equiv = {}
            for j, k in enumerate(SYMS):
                so = o[n * (j + 1): n * (j + 2)]
                s = SYMS[k]
                equiv[k] = all(b is not None and x == s(b) for b, x in zip(base, so))
            cands.append({"kind": kind, "name": f.stem, "len": len(prog), "pass": demo["matched"] == demo["total"],
                          "passed": demo["matched"], "pred": base[-1], "right": base[-1] == it["test_output"], "equiv": equiv})
        # which symmetries the task itself respects (on the examples): s(out) is consistent with s(in) under the correct map
        out[pid] = {"cands": cands, "row": rows[pid], "key": it["test_output"]}
    return out


def pick(cands, rule):
    P = [c for c in cands if c["pass"] and c["pred"] is not None]
    if not P:
        pl = [c for c in cands if c["kind"] == "plain" and c["pred"] is not None]
        v = Counter(json.dumps(c["pred"]) for c in pl)
        return [json.loads(a) for a, _ in v.most_common(2)]
    if rule == "plain_weighted":
        w = Counter()
        for c in P:
            w[json.dumps(c["pred"])] += 1.0 if c["kind"] in ("plain", "revise") else 0.25
    elif rule == "plain_only_if_any":
        pp = [c for c in P if c["kind"] != "divergent"] or P
        w = Counter(json.dumps(c["pred"]) for c in pp)
    elif rule == "sym_consistent":
        w = Counter()
        for c in P:
            w[json.dumps(c["pred"])] += 1 + sum(c["equiv"].values()) * 0.01
    else:  # by test answer
        w = Counter(json.dumps(c["pred"]) for c in P)
    short = {}
    for c in P:
        k = json.dumps(c["pred"])
        short[k] = min(short.get(k, 10**9), c["len"])
    order = sorted(w, key=lambda k: (-w[k], short[k]))
    return [json.loads(k) for k in order[:2]]


def main():
    batch = Path(sys.argv[1])
    items = {json.loads(l)["id"]: json.loads(l) for l in Path(config.BENCHMARKS["arc"]["file"]).read_text().splitlines() if l.strip()}
    data = load(batch, items)
    rules = ["by_test_answer", "plain_weighted", "plain_only_if_any", "sym_consistent"]
    print(f"{len(data)} puzzles; recorded method {sum(d['row']['solved'] for d in data.values())}, "
          f"plain one answer {sum(next((c['right'] for c in d['cands'] if c['kind'] == 'plain'), False) for d in data.values())}, "
          f"any right {sum(any(c['right'] for c in d['cands']) for d in data.values())}")
    for r in rules:
        top1 = sum(1 for d in data.values() if (p := pick(d["cands"], r)) and p[0] == d["key"])
        top2 = sum(1 for d in data.values() if any(x == d["key"] for x in pick(d["cands"], r)))
        print(f"  {r:20s} top1 {top1}  top2 {top2}")
    # plain with two samples (fair two-answer baseline): first two plain attempts
    p2 = sum(1 for d in data.values() if any(c["right"] for c in [c for c in d["cands"] if c["kind"] == "plain"][:2]))
    print(f"  plain, two answers (first two plain attempts): {p2}")
    for pid, d in data.items():
        P = [c for c in d["cands"] if c["pass"]]
        if len({json.dumps(c["pred"]) for c in P}) > 1 or (P and not any(c["right"] for c in P) and any(c["right"] for c in d["cands"])):
            print(" ", pid, [(c["name"].rsplit("_", 1)[0], c["right"], sum(c["equiv"].values())) for c in P])


if __name__ == "__main__":
    main()
