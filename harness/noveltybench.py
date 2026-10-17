"""NoveltyBench (curated split) on Claude via the CLI: plain sampling, the paper's in-context baseline, and the HTSA
divergent method, all generating with the same model; judged with the official v1.1 judge prompts (JUDGE_SYSTEM,
SCORE_SYSTEM, patience 0.8 utility) by Opus.

Deviation from official v1.1, stated in every summary: the partition judge is Opus (official: gpt-5.6-luna), and both
judges run through the Claude CLI (prompt text = official system prompt + official user content + a JSON-format line).

Arms:
  plain       10 independent calls with the prompt alone (official "regenerate").
  incontext   one conversation, "Can you generate a different answer?" after each answer (official "in-context",
              the paper's best baseline). The CLI has no multi-turn input, so the conversation is replayed as text.
  method      1 map call (note the default answer, 14 directions that differ in central content via answer change,
              assumption flip, low-prior angle, distant-domain seed, perspective/form; pick the 10 most distinct and
              best-serving, best first) + 10 answer calls, each a normal answer along one direction.

    HTSA_LAB_ROOT=D:/AGI-lab python -m harness.noveltybench gen --arm plain --model haiku --out D:/AGI-lab/results/nb/haiku-plain
    python -m harness.noveltybench judge --out D:/AGI-lab/results/nb/haiku-plain
    python -m harness.noveltybench summary D:/AGI-lab/results/nb/*
"""
from __future__ import annotations

import argparse
import json
import random
import re
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

from . import llm

NB = Path("D:/AGI-lab/ext/novelty-bench")


def _official(file, name):
    """Read a string constant from the official source without importing it (its imports need GPU libraries)."""
    import ast
    tree = ast.parse((NB / "src" / file).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            return ast.literal_eval(node.value)
    raise KeyError(name)


JUDGE_SYSTEM = _official("partition.py", "JUDGE_SYSTEM")   # official v1.1 partition prompt
SCORE_SYSTEM = _official("score.py", "SCORE_SYSTEM")       # official v1.1 score prompt

K = 10
SEEDS = ["harbour", "glacier", "orchestra", "mycelium", "lighthouse", "origami", "desert", "clockwork", "monsoon",
         "beehive", "tram", "volcano", "library", "salt"]

MAP = """You will help answer a prompt in ten genuinely different ways. Do not answer it yet.

<prompt>
{prompt}
</prompt>

1. Write the default: the answer most assistants would give first.
2. List 14 directions a good answer could take. Each must differ from the default and from the others in its central
   content (the actual answer, recommendation, plot, argument or image), not in wording, tone or format. Use a mix of:
   - a different main answer or choice;
   - flipping an assumption the prompt does not force;
   - an unusual but fully valid angle (low prior);
   - an idea borrowed from a distant domain, using one of these seed words: {seeds};
   - a different perspective, setting, genre or form, where the prompt allows it.
   Every direction must still satisfy every requirement of the prompt (length, form, topic, constraints).
3. Choose the 10 directions that are most different from each other and would make the best responses. Order them
   best first.

Reply with JSON only: {{"default": "...", "directions": ["...", ... 10 strings, best first]}}"""

ANSWER = """<prompt>
{prompt}
</prompt>

Respond to the prompt above. Take this direction for the central content of your response: {direction}
Write only the response itself, as a normal, high-quality answer to the prompt that meets all of its requirements. Do
not mention the direction or that alternatives exist."""

lock = threading.Lock()


def gen_call(prompt, model, tag, log_dir, effort=None):
    r = llm.call(prompt, role="plain", model=model, call_id=tag, log_dir=log_dir, meta={"card": tag}, effort=effort)
    return (r.text or "").strip(), int(r.usage.total_tokens), r.error


def parse_json(text):
    m = re.search(r"\{.*\}", text or "", re.S)
    if not m:
        raise ValueError("no JSON")
    return json.loads(m.group(0))


def gen_one(row, arm, model, out, effort):
    log_dir = out / "calls" / row["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    p = row["prompt"]
    gens, tok, extra = [], 0, {}
    if arm == "plain":
        with ThreadPoolExecutor(max_workers=K) as ex:
            res = list(ex.map(lambda i: gen_call(p, model, f"plain_{i}", log_dir, effort), range(K)))
        gens = [t for t, _, _ in res]
        tok = sum(n for _, n, _ in res)
    elif arm == "incontext":
        convo = []
        for i in range(K):
            if not convo:
                text = p
            else:
                text = ("Here is our conversation so far.\n\n" + "\n\n".join(
                    f"User: {u}\n\nAssistant: {a}" for u, a in convo) +
                        "\n\nUser: Can you generate a different answer?\n\nReply as the assistant, with the new answer only.")
            t, n, _ = gen_call(text, model, f"incontext_{i}", log_dir, effort)
            tok += n
            gens.append(t)
            convo.append((p if not convo else "Can you generate a different answer?", t))
    elif arm == "method":
        seeds = ", ".join(random.Random(row["id"]).sample(SEEDS, 5))
        dirs = None
        for attempt in range(2):
            t, n, _ = gen_call(MAP.format(prompt=p, seeds=seeds), model, f"map_{attempt}", log_dir, effort)
            tok += n
            try:
                d = parse_json(t)
                dirs = [str(x) for x in d["directions"]][:K]
                extra = {"default": d.get("default"), "directions": dirs}
                if len(dirs) == K:
                    break
            except Exception:  # noqa: BLE001
                continue
        dirs = (dirs or []) + ["any good answer"] * (K - len(dirs or []))
        with ThreadPoolExecutor(max_workers=K) as ex:
            res = list(ex.map(lambda i: gen_call(ANSWER.format(prompt=p, direction=dirs[i]), model, f"answer_{i}",
                                                 log_dir, effort), range(K)))
        gens = [t for t, _, _ in res]
        tok += sum(n for _, n, _ in res)
    gens = [g if g else "[empty]" for g in gens]
    return {"id": row["id"], "category": row.get("category"), "prompt": p, "generations": gens, "arm": arm,
            "model": model, "gen_tokens": tok, **extra}


def judge_one(row, judge_model, out, seed=0):
    log_dir = out / "judge_calls" / row["id"]
    log_dir.mkdir(parents=True, exist_ok=True)
    gens = row["generations"]
    n = len(gens)
    order = list(range(n))
    random.Random(f"{seed}{row['prompt']}").shuffle(order)          # official shuffled_order with a seed
    shown = [gens[i] for i in order]
    user = "\n\n".join([f"<prompt>\n{row['prompt']}\n</prompt>"] + [f'<response index="{i}">\n{r}\n</response>'
                                                                    for i, r in enumerate(shown)])
    groups, tok, g = None, 0, []
    for attempt in range(3):
        r = llm.call(JUDGE_SYSTEM + "\n\n" + user + '\n\nReply with JSON only: {"groups": [[indices], ...]}, '
                     "every index from 0 to " + str(n - 1) + " exactly once.", role="judge", model=judge_model,
                     call_id=f"partition_{attempt}", log_dir=log_dir, effort="high")
        tok += int(r.usage.total_tokens)
        try:
            g = parse_json(r.text)["groups"]
            if sorted(i for x in g for i in x) == list(range(n)):
                groups = g
                break
        except Exception:  # noqa: BLE001
            continue
    if groups is None:                                                # official lenient fold
        seen = set()
        groups = [[i for i in x if 0 <= i < n and not (i in seen or seen.add(i))] for x in (g if isinstance(g, list) else [])]
        groups += [[i] for i in range(n) if i not in seen]
    part = [0] * n
    for gi, members in enumerate(groups):
        for s in members:
            part[order[s]] = gi
    seen_map = {}
    part = [seen_map.setdefault(x, len(seen_map)) for x in part]   # canonical
    heads = [i for i, c in enumerate(part) if c not in part[:i]]

    def score(i):
        for attempt in range(3):
            r = llm.call(SCORE_SYSTEM + f"\n\n<prompt>\n{row['prompt']}\n</prompt>\n\n<response>\n{gens[i]}\n</response>"
                         '\n\nReply with JSON only: {"score": <integer 1-10>}', role="judge", model=judge_model,
                         call_id=f"score_{i}_{attempt}", log_dir=log_dir, effort="high")
            try:
                s = int(parse_json(r.text)["score"])
                if 1 <= s <= 10:
                    return s, int(r.usage.total_tokens)
            except Exception:  # noqa: BLE001
                continue
        return None, int(r.usage.total_tokens)
    with ThreadPoolExecutor(max_workers=min(3, len(heads))) as ex:   # capped: each call is a CLI process
        sc = list(ex.map(score, heads))
    tok += sum(t for _, t in sc)
    scores = [None] * n
    for i, (s, _) in zip(heads, sc):
        scores[i] = s
    credited = [scores[i] if (i in heads and scores[i] is not None) else 0 for i in range(n)]
    utility = float(np.average(credited, weights=0.8 ** np.arange(n)))   # official utility, patience 0.8
    return {**row, "partition": part, "distinct": len(heads), "generation_scores": scores,
            "partition_scores": [scores[i] for i in heads], "utility": utility, "judge_tokens": tok,
            "judge_model": judge_model}


def run_rows(fn, rows, path, workers):
    done = set()
    if path.exists():
        done = {json.loads(l)["id"] for l in path.read_text(encoding="utf-8").splitlines() if l.strip()}
    todo = [r for r in rows if r["id"] not in done]
    print(f"[nb] {path.name}: {len(done)} done, {len(todo)} to go", flush=True)

    def work(r):
        try:
            out = fn(r)
        except Exception as e:  # noqa: BLE001
            print(f"[nb] {r['id']} error {type(e).__name__}: {e}", flush=True)
            return
        with lock:
            with path.open("a", encoding="utf-8") as f:
                f.write(json.dumps(out) + "\n")
            done.add(r["id"])
            msg = f"distinct {out['distinct']} utility {out['utility']:.2f}" if "utility" in out else f"tokens {out['gen_tokens']:,}"
            print(f"[nb] {len(done)}/{len(rows)} {r['id']} {msg}", flush=True)
    with ThreadPoolExecutor(max_workers=workers) as ex:
        list(ex.map(work, todo))


def summary(dirs):
    lines = ["| arm | prompts | mean distinct (of 10) | mean utility | generation tokens per prompt |", "|---|---|---|---|---|"]
    for d in dirs:
        p = Path(d) / "scores.jsonl"
        if not p.exists():
            continue
        rows = list({r["id"]: r for r in reversed([json.loads(l) for l in p.read_text(encoding="utf-8").splitlines()
                                                     if l.strip()])}.values())   # one row per prompt (first kept)
        lines.append(f"| {Path(d).name} | {len(rows)} | {np.mean([r['distinct'] for r in rows]):.2f} | "
                     f"{np.mean([r['utility'] for r in rows]):.2f} | {np.mean([r['gen_tokens'] for r in rows]):,.0f} |")
    lines += ["", "NoveltyBench curated split, k=10, official v1.1 judge prompts and utility (patience 0.8); judges: Opus "
              "for partition and score via the Claude CLI (official partition judge is gpt-5.6-luna)."]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["gen", "judge", "summary"])
    ap.add_argument("dirs", nargs="*")
    ap.add_argument("--arm", choices=["plain", "incontext", "method"])
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--effort", default=None)
    ap.add_argument("--judge-model", default="opus")
    ap.add_argument("--out")
    ap.add_argument("--limit", type=int, default=100)
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    if a.cmd == "summary":
        print(summary(a.dirs))
        return
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    if a.cmd == "gen":
        rows = [json.loads(l) for l in (NB / "data" / "curated.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()][: a.limit]
        run_rows(lambda r: gen_one(r, a.arm, a.model, out, a.effort), rows, out / "generations.jsonl", a.workers)
    else:
        a.workers = min(a.workers, 2)   # judge stage: at most 2 prompts x 3 score calls per arm in flight
        rows = [json.loads(l) for l in (out / "generations.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()][: a.limit]
        run_rows(lambda r: judge_one(r, a.judge_model, out), rows, out / "scores.jsonl", a.workers)


if __name__ == "__main__":
    main()
