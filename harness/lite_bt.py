"""Lite test of the thinking method on BrainTeaser: idea generation and blind judging only, no setup, no verification
rounds. Per puzzle, on the same model:
  plain  one direct answer (the baseline)
  lite   four thinkers, each made to think in a different human way (doubt the first instinct, read literally,
         question the hidden assumption, eliminate options), then one blind judge picks among their reasoning
  vote   (optional, --vote) five direct answers, majority wins: the same number of calls as lite, no method
Answers are scored against the key, which only this scorer reads; prompts never contain it.

    $env:HTSA_LAB_ROOT = "$PWD\\lab"; $env:HTSA_MODEL = "haiku"
    python -m harness.lite_bt --items 48 --batch lite-bt [--vote] [--effort max] [--workers 4]
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import threading
import time
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from . import config, llm

LETTERS = "ABCD"
FORMAT = "\n\nEnd your reply with one line of the form\nANSWER: <letter>\nwhere <letter> is one of A, B, C, D."

THINKERS = {
    "doubt": ("Read the riddle and note your first instinct. Then assume that first instinct is the trap the riddle "
              "was built to set, and look for the reading that makes it wrong. Decide only after both."),
    "literal": ("Read every word of the riddle literally: spelling, letters, sounds, double meanings and puns. Riddles "
                "often hide the answer in the words themselves rather than in the situation they describe."),
    "assumption": ("Name the assumption the riddle quietly makes you accept (about who, what, when or how), then drop "
                   "it and ask what answer fits once it is gone."),
    "eliminate": ("Test each option in turn against every detail of the riddle. For each, state the strongest reason it "
                  "could be wrong. Keep the one that survives."),
}


def puzzle_text(item: dict) -> str:
    opts = "\n".join(f"{LETTERS[i]}. {c}" for i, c in enumerate(item["choices"]))
    return f"Riddle: {item['question']}\n\nOptions:\n{opts}"


def parse(text: str) -> str | None:
    m = re.findall(r"ANSWER:\s*\(?([ABCD])\)?", text or "")
    return m[-1] if m else None


def call(prompt: str, args, tag: str, log_dir: Path) -> tuple[str, int]:
    r = llm.call(prompt, role="plain", call_id=f"{tag}_{int(time.time() * 1000) % 10**9}", backend=args.backend,
                 log_dir=log_dir, meta={"card": tag}, effort=args.effort or None)
    return (r.text or ""), int(r.usage.total_tokens)


def run_item(item: dict, args, out_dir: Path) -> dict:
    log_dir = out_dir / "calls" / item["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    q = puzzle_text(item)
    res = {"id": item["id"], "group": item.get("group", item["id"]), "key": LETTERS[int(item["label"])]}
    # plain: reused from --plain-from when given (never re-run), else one call
    reused = getattr(args, "plain_answers", None)
    if reused is not None and item["id"] in reused:
        ans = reused[item["id"]]
        res["plain"] = str(ans).strip().upper()[:1] if ans else None
        res["plain_tokens"], res["plain_reused"] = args.plain_tokens.get(item["id"], 0), True
    else:
        t, tok = call("Solve this riddle. Reason step by step." + "\n\n" + q + FORMAT, args, "plain", log_dir)
        res["plain"], res["plain_tokens"] = parse(t), tok
    # lite: four thinkers then a blind judge
    outs, tokens = [], 0
    for name, how in THINKERS.items():
        t, tok = call(f"Solve this riddle. {how} Keep your reasoning short.\n\n{q}{FORMAT}", args, f"lite_{name}", log_dir)
        outs.append((name, t.strip()[-1500:], parse(t)))
        tokens += tok
    order = list(range(len(outs)))
    random.Random(item["id"]).shuffle(order)                     # the judge sees no strategy names, in random order
    shown = "\n\n".join(f"--- Reasoning {k + 1} ---\n{outs[i][1]}" for k, i in enumerate(order))
    judge = (f"{q}\n\nFour people reasoned about this riddle independently:\n\n{shown}\n\nThe majority is not decisive. "
             "Judge which reasoning actually resolves the riddle's trick and is consistent with every word of it, "
             "then give the final answer." + FORMAT)
    t, tok = call(judge, args, "lite_judge", log_dir)
    tokens += tok
    votes = Counter(o[2] for o in outs if o[2])
    res["lite"] = parse(t) or (votes.most_common(1)[0][0] if votes else None)
    res["lite_thinkers"] = {o[0]: o[2] for o in outs}
    res["lite_tokens"] = tokens
    # vote: five direct answers, majority
    if args.vote:
        answers, vtok = [], 0
        for k in range(5):
            t, tok = call("Solve this riddle. Reason step by step.\n\n" + q + FORMAT, args, f"vote{k}", log_dir)
            answers.append(parse(t))
            vtok += tok
        c = Counter(a for a in answers if a)
        res["vote"], res["vote_tokens"] = (c.most_common(1)[0][0] if c else None), vtok
    return res


def load_plain(folder) -> tuple[dict, dict, list]:
    """Plain answers of an earlier harness.bench batch: the last runs.jsonl row per run_id, replicate 0 (else the
    lowest replicate) per item; returns (answers, tokens, item ids in first-seen order, each once)."""
    last = {}
    for l in (Path(folder) / "runs.jsonl").read_text(encoding="utf-8").splitlines():
        if l.strip():
            r = json.loads(l)
            if r.get("arm") == "plain":
                last[r["run_id"]] = r
    pick: dict = {}
    for r in last.values():
        cur = pick.get(r["item_id"])
        if cur is None or int(r.get("replicate", 0)) < int(cur.get("replicate", 0)):
            pick[r["item_id"]] = r
    return ({k: r.get("answer") for k, r in pick.items()}, {k: int(r.get("spent_tokens") or 0) for k, r in pick.items()},
            list(pick))


def bootstrap_diff(rows, a, b, n=2000):
    groups = defaultdict(list)
    for r in rows:
        groups[r["group"]].append((r[a] == r["key"]) - (r[b] == r["key"]))
    keys = list(groups)
    rng = random.Random(0)
    stats = []
    for _ in range(n):
        smp = [rng.choice(keys) for _ in keys]
        vals = [v for g in smp for v in groups[g]]
        stats.append(sum(vals) / len(vals))
    stats.sort()
    return sum(v for g in keys for v in groups[g]) / len(rows), stats[int(0.025 * n)], stats[int(0.975 * n)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--items", type=int, default=48)
    ap.add_argument("--split", default="dev-tune")
    ap.add_argument("--batch", required=True)
    ap.add_argument("--backend", default=None)
    ap.add_argument("--effort", default=os.environ.get("HTSA_PLAIN_EFFORT", ""))
    ap.add_argument("--vote", action="store_true")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--plain-from", default=None,
                    help="results folder of an earlier harness.bench batch: its plain answers and its exact puzzle list are reused, plain is not re-run")
    args = ap.parse_args()
    args.plain_answers, args.plain_tokens = None, {}
    plain_ids = None
    if args.plain_from:
        args.plain_answers, args.plain_tokens, plain_ids = load_plain(args.plain_from)
    args.backend = args.backend or config.default_backend()
    data = Path(config.DATA_DIR) / "brainteaser_sp.jsonl"
    items = [json.loads(l) for l in data.read_text(encoding="utf-8").splitlines() if l.strip()]
    if plain_ids is not None:
        by_id = {it["id"]: it for it in items}
        missing = [i for i in plain_ids if i not in by_id]
        if missing:
            raise SystemExit(f"[lite] {len(missing)} of the earlier batch's puzzles are not in {data} (first: {missing[:3]}); "
                             "point HTSA_LAB_ROOT at the same lab folder the earlier batch used")
        items = [by_id[i] for i in plain_ids]
    else:
        items = [it for it in items if it.get("split") == args.split][: args.items]
    out_dir = Path(config.RESULTS_DIR) / args.batch
    out_dir.mkdir(parents=True, exist_ok=True)
    rows_path = out_dir / "lite_runs.jsonl"
    done = {}
    if rows_path.exists():
        for l in rows_path.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                done[r["id"]] = r
    todo = [it for it in items if it["id"] not in done]
    lock = threading.Lock()
    print(f"[lite] {len(items)} puzzles, {len(done)} already done, model {config.DEFAULT_MODEL}, effort {args.effort or 'default'}", flush=True)

    def work(it):
        r = run_item(it, args, out_dir)
        with lock:
            with rows_path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r) + "\n")
            done[r["id"]] = r
            print(f"[lite] {len(done)}/{len(items)} {r['id']}: key {r['key']} plain {r['plain']} lite {r['lite']}"
                  + (f" vote {r['vote']}" if 'vote' in r else ""), flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        list(ex.map(work, todo))
    rows = [done[it["id"]] for it in items if it["id"] in done]
    arms = ["plain", "lite"] + (["vote"] if args.vote else [])
    lines = [f"# Lite thinking test on BrainTeaser ({len(rows)} puzzles, {len({r['group'] for r in rows})} puzzle groups), model {config.DEFAULT_MODEL}", "",
             "| arm | solved | tokens per puzzle |", "|---|---|---|"]
    for a in arms:
        rs = [r for r in rows if a in r]
        sol = sum(r[a] == r["key"] for r in rs) / len(rs)
        tok = sum(r.get(f"{a}_tokens", 0) for r in rs) / len(rs)
        lines.append(f"| {a} | {sol:.1%} | {tok:,.0f} |")
    lines.append("")
    for b in arms[1:]:
        rs = [r for r in rows if b in r]
        d, lo, hi = bootstrap_diff(rs, b, "plain")
        lines.append(f"{b} minus plain: {d * 100:+.1f} points, 95% interval [{lo * 100:+.1f}, {hi * 100:+.1f}] (bootstrap over puzzle groups)")
    if args.vote:
        rs = [r for r in rows if "vote" in r]
        d, lo, hi = bootstrap_diff(rs, "lite", "vote")
        lines.append(f"lite minus vote: {d * 100:+.1f} points, 95% interval [{lo * 100:+.1f}, {hi * 100:+.1f}]")
    th = defaultdict(int)
    for r in rows:
        for k, v in (r.get("lite_thinkers") or {}).items():
            th[k] += (v == r["key"])
    lines.append("")
    lines.append("each thinker alone: " + ", ".join(f"{k} {v / len(rows):.0%}" for k, v in th.items()))
    (out_dir / "lite_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
