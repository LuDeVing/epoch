"""Dry run of nano.loop with a content-aware mock backend: no model tokens, real check.py rungs.

Usage: python -m nano.dry_run [--batch mock-dry] [--implement 3] [--budget 1500000] [--profile llm] [extra loop flags]
Exercises every stage: planner (falls back to the default tree), research briefs, sketches, blind
clustering, cross-part merge, prior-art tags, interrogation chains with offshoots and assumptions,
implementation (one candidate deliberately breaks its part boundary), dedup, verification, revision,
long runs. Uses short step counts so the whole thing takes a few minutes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import threading

os.environ.setdefault("HTSA_LAB_ROOT", "D:/AGI-lab")
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from harness import llm                                           # noqa: E402
from nano import loop as L                                        # noqa: E402
from nano import profile as PF                                    # noqa: E402
from nano import tree as TREE                                     # noqa: E402

BASE = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "train.py"), encoding="utf-8").read()
TOPICS = ["gated attention", "value residual", "sliding window", "qk norm", "untied embeddings",
          "sparse attention", "relu squared", "parallel blocks", "token dropping", "lr warmdown"]


# ---------------------------------------------------------------- replies for the no-baseline test profiles
# (docs/GENERIC_SPEC.md section 6). The LLM replies below are unchanged; these answer only on binpack_nobase
# (Mode 2: complete bin-packing files) and review_process (Mode 3: five-section proposals and judge score lines).
PACK_TOPICS = ["first fit", "best fit", "worst fit", "next fit", "harmonic classes", "reserve for large items"]
REVIEW_TOPICS = ["anchored rubric", "pairwise comparison", "judge z-scores", "rotating demo order",
                 "conflict declarations", "public criteria"]
_RULES = {
    "first": ("first fit: the first open bin with room",
              ["    for i, fill in enumerate(bins):",
               "        if fill + item <= capacity + EPS:",
               "            return i",
               "    return -1"]),
    "best": ("best fit: the open bin left fullest by the item",
             ["    best, best_room = -1, capacity + 1.0",
              "    for i, fill in enumerate(bins):",
              "        room = capacity - fill - item",
              "        if room >= -EPS and room < best_room:",
              "            best, best_room = i, room",
              "    return best"]),
    "worst": ("worst fit: the open bin left emptiest by the item",
              ["    worst, worst_room = -1, -1.0",
               "    for i, fill in enumerate(bins):",
               "        room = capacity - fill - item",
               "        if room >= -EPS and room > worst_room:",
               "            worst, worst_room = i, room",
               "    return worst"]),
}
# the first builds are first fit and worst fit; best fit comes later, so the reference is set first, then moves
_PACK_ORDER = ["first", "worst", "first", "best", "first", "worst", "best"]
_counter: dict[str, int] = {}
_counter_lock = threading.Lock()


def _next(key: str) -> int:
    with _counter_lock:
        n = _counter.get(key, 0)
        _counter[key] = n + 1
        return n


def pack_file(rule: str, variant: int) -> str:
    """A complete bin-packing file: the named rule, with a constant that keeps each candidate's source distinct."""
    desc, body = _RULES[rule]
    return "\n".join([f'"""Online bin packing, {desc}."""', "", "EPS = 1e-9", f"_VARIANT = {variant}", "", "",
                      "def choose_bin(item: float, bins: list[float], capacity: float) -> int:"] + body) + "\n"


def proposal(n: int, complete: bool = True) -> str:
    """A five-section proposal; versions cite different numbers of facts, so the mock panel ranks them apart."""
    facts = [["[F2]", "[F3]", "[F6]"], ["[F4]"], ["[F1]", "[F5]"], ["[F6]", "[F7]", "[F8]", "[F9]"]][n % 4]
    topic = REVIEW_TOPICS[n % len(REVIEW_TOPICS)]
    parts = ["CLAIM:", f"Use {topic} so every team gets the same chance and judges stay within four hours (version {n}).", "",
             "FROM THE FACTS TO THE IDEA:",
             f"{' '.join(facts)} show where the current process leaks fairness. "
             f"So the process should apply {topic} at the step where the leak happens.", "",
             "FROM THE IDEA TO THE RESULT:",
             "Each project is seen by three judges in a rotated order. Scores are put on one scale before they are "
             "combined. Teams see the rubric in advance and a short note afterwards.", "",
             "WEAK POINTS:",
             "Teams may still polish what the rubric rewards. Judges may not follow the order on the day.", ""]
    if complete:
        parts += ["PROPOSED TEST:",
                  "Run the process on five past projects with two volunteer judges and compare the agreement with last "
                  "year's; fewer than 7 agreements in 10 refutes it.", ""]
    return "\n".join(parts)


def _mock_profiles(prompt: str, role: str, meta: dict, name: str) -> str | None:
    card = str(meta.get("card", ""))
    topics = PACK_TOPICS if name == "binpack_nobase" else REVIEW_TOPICS
    if card.startswith("sketch:"):
        h = int(hashlib.md5((meta.get("seed", "") + meta.get("node", "") + card).encode()).hexdigest(), 16)
        out = []
        for i in range(5):
            t = topics[(h + i) % len(topics)]
            out.append(f"IDEA: {t} variant {i}\nMECHANISM: apply {t} to the {meta.get('node')} part.\n"
                       f"PREDICTION: a better score at the first check\nTEST: {PF.current().v('cheap_test')}\nSOURCE: own"
                       + ("\nKIND: leap\nBREAKS: every case is treated alike\nKEEPS: the interface\nP_SUCCESS: 0.1\n"
                          "KILL: a worse score at the first check" if i % 3 == 0 else "\nKIND: port"))
        return "\n\n".join(out)
    if role == "judge" and card == "panel" and name == "review_process":
        k = len(re.findall(r"^K\d+\. ", prompt, flags=re.M)) or 4
        body = prompt.split("PROPOSAL ", 1)[-1]
        cited = len(set(re.findall(r"\[F\d+\]", body)))
        j = int(str(meta.get("seed", "0")) or 0)
        base = min(9.0, 4.5 + cited)
        lines = [f"K{i}: {max(1, min(10, round(base + ((i + j) % 3 - 1) * 0.5)))} | mock reason {i}" for i in range(1, k + 1)]
        return "\n".join(lines) + f"\nNOTE: cites {cited} facts; the rotated order is the strongest point."
    if role == "generate" and card in ("implement", "revise", "program", "seeded", "formal", "docs", "low_prior", "transform"):
        n = _next(name)
        if name == "binpack_nobase":
            rule = _PACK_ORDER[n % len(_PACK_ORDER)]
            return (f"HYPOTHESIS: {_RULES[rule][0]} should use few bins.\nCHANGE: choose_bin\n"
                    "FIDELITY: exact, the idea as specified\n```python\n" + pack_file(rule, n) + "```")
        complete = not (card == "implement" and n == 1)       # one proposal misses a section: rung 0 lint, then a fix
        return (f"HYPOTHESIS: proposal {n} makes the review fairer.\nCHANGE: assignment and rubric\n"
                "FIDELITY: exact, as specified\n```markdown\n" + proposal(n, complete) + "```")
    return None


def mock_upward(meta: dict) -> str:
    """An upward context's reply in tree.UPWARD_FORMAT: two proposals for a new verifier."""
    tag = str(meta.get("seed", ""))[:24] or "x"
    return ("PROPOSAL: judge by loss on rare tokens, not mean loss (" + tag + ")\n"
            "REFRAMING: the mean over all tokens hides the tail; model the tail separately.\n"
            "NEW MEASURE: validation loss on the 10 percent rarest tokens, from the same held-out file.\n"
            "WHY: mean loss is dominated by frequent tokens, so tail gains are invisible.\n"
            "COST: a token-frequency table and one extra pass of the eval.\n\n"
            "PROPOSAL: judge by loss after a fixed wall-clock budget (" + tag + ")\n"
            "REFRAMING: fixed time instead of fixed tokens.\n"
            "NEW MEASURE: validation loss at 10 minutes of training on the reference GPU.\n"
            "WHY: a fixed token budget cannot see a faster step.\n"
            "COST: a timed training harness and repeated runs to control timing noise.")


_need_sent: list[bool] = []                 # fetch on demand: one builder asks for a fact once per process


def mock_need(prompt: str, role: str, meta: dict) -> str | None:
    """The first build whose prompt offers the NEED line asks for one fact and writes no code; its re-prompt
    (with FACTS YOU ASKED FOR) falls through to the usual code reply."""
    if role != "generate" or str(meta.get("card", "")) != "implement" or "NEED: <optional" not in prompt:
        return None
    if "FACTS YOU ASKED FOR" in prompt:
        return None
    with _counter_lock:
        if _need_sent:
            return None
        _need_sent.append(True)
    q = ("what is the proven asymptotic worst-case ratio of first fit for online bin packing?"
         if PF.current().name == "binpack_nobase" else
         "what initial value did 2026 work use for the attention gate bias below 100M parameters?")
    return f"HYPOTHESIS: pending one fact.\nCHANGE: none yet\nFIDELITY: exact, waiting for the fact\nNEED: {q}\n"


def mock_fetch(prompt: str) -> str:
    """The delegated research model answering one fetched fact, with a source."""
    q = re.search(r"QUESTION:\s*(.+)", prompt)
    return (f"ANSWER: mock answer to '{(q.group(1) if q else '?')[:80]}': 1.7 in the asymptotic worst case.\n"
            "SOURCE: https://example.org/fetched-fact\nCONFIDENCE: medium")


def mock(prompt: str, role: str, meta: dict) -> str:
    if str(meta.get("card", "")) == "fetch_fact":
        return mock_fetch(prompt)
    need = mock_need(prompt, role, meta)
    if need is not None:
        return need
    if "Direction UPWARD" in prompt:           # upward contexts answer in their own format (tree.UPWARD_FORMAT)
        return mock_upward(meta)
    name = PF.current().name
    if name in ("binpack_nobase", "review_process"):
        r = _mock_profiles(prompt, role, meta, name)
        if r is not None:
            return r
    card = str(meta.get("card", ""))
    if card.endswith(":questions"):           # delegated web: the model lists what to look up
        return ("QUESTIONS:\n1. what did 2026 work measure for gated attention below 100M parameters?\n"
                "2. does value residual learning help at 21M parameters and 50M tokens?\n"
                "3. is there a measured failure of sliding-window attention at 1024 tokens?")
    if card == "fact_check":
        return "1. SUPPORTED | the page states two extra matmuls\n2. NOT SUPPORTED | the page says 8 percent"
    if card.endswith(":findings"):            # delegated web: the research model answers with sources
        return ("FINDINGS:\n1. gated attention: -0.02 loss at 1B https://arxiv.org/abs/2505.06708; untested below 100M.\n"
                "2. value residual: small gain at 124M https://arxiv.org/abs/2410.17897\n3. no source found.")
    if role == "research" and card == "analogy_research":
        node = meta.get("operator", "x")
        return json.dumps({"analogues": [{"field": f"ecology {k}", "problem": f"allocation problem {k} like {node}",
                                          "mechanism": "feedback with a budget", "correspondence": "their X is our Y",
                                          "case": "a documented case", "url": "https://example.org/analogy"} for k in range(5)],
                           "queries": ["q"]})
    if card == "premortem":
        return ("OBJECTIONS:\n- it adds a matmul per layer | severity: high | class: hidden_cost | if_true: step_ratio above 1.2\n"
                "- the effect is within seed noise | severity: medium | class: below_noise | if_true: learn_z above -0.5\n"
                "- it only helps early | severity: low | class: early_only | if_true: trend above 0.001\n"
                "- the exam cannot see it | severity: low | class: metric_blind | if_true: none\nVERDICT: noise")
    if role == "research":
        node = meta.get("operator", "x")
        return json.dumps({"known": [{"name": f"{node} known trick", "mechanism": "mock mechanism", "effect": "-0.01 loss",
                                      "where": "124M", "url": "https://arxiv.org/abs/2010.04245"}],
                           "failed": [{"name": f"{node} failed trick", "why": "no gain", "url": "https://example.org/f"}],
                           "open": [{"direction": f"{node} open direction", "why": "untested", "url": "https://example.org/o"}],
                           "queries": ["q1"]})
    if card == "replan":                      # re-plan arm: a usable map, one frame changed, one assumption added, one new part
        nodes = [{"id": n["id"], "name": n["name"], "frame": n.get("frame", "") + (" (re-planned)" if n["id"] == "mix" else ""),
                  "assumptions": list(n.get("assumptions", [])) + (["the gate is applied after attention"] if n["id"] == "ffn" else []),
                  "boundary": n.get("boundary", "")} for n in TREE.DEFAULT_TREE if n.get("parent") == "root" and n["id"] != "recipe"]
        nodes.append({"id": "sched", "name": "the learning-rate schedule", "frame": "warmup then linear decay",
                      "assumptions": ["no cosine"], "boundary": "Block, lr_mult"})
        return json.dumps(nodes)
    if role == "encode":                      # planner: invalid -> default tree
        return "no"
    if role == "defaults":
        return "1. add QK norm\n2. untie embeddings\n3. raise the learning rate\n4. sliding window attention\n5. relu squared"
    if card.startswith("sketch:"):
        h = int(hashlib.md5((meta.get("seed", "") + meta.get("node", "") + card).encode()).hexdigest(), 16)
        out = []
        for i in range(5):
            t = TOPICS[(h + i) % len(TOPICS)]
            out.append(f"IDEA: {t} variant {i}\nMECHANISM: apply {t} to the {meta.get('node')} part to lower loss.\n"
                       f"PREDICTION: loss curve lower by 0.01 after 45 matched steps\nTEST: 1-minute smoke run comparison\n"
                       f"SOURCE: {'https://arxiv.org/abs/2010.04245' if i == 0 else 'own'}"
                       + "\nTARGET: lower loss on rare tokens\nSCOPE: validation loss at 1024"
                       + ("\nKIND: leap\nBREAKS: every layer computes the same thing\nKEEPS: the residual stream and the loss\nP_SUCCESS: 0.1\nKILL: loss gap above +0.05 at 45 steps" if i % 3 == 0 else "\nKIND: port")
                       + ("\nMAPPING: objects: their queue -> our batch; their clock -> our step | relations: r1; r2; r3 | inference: i | break: none" if card == "sketch:analogy" else "")
                       + ("\nADAPTATION: zero-init the new path" if card == "sketch:adapt" else ""))
        return "\n\n".join(out)
    if role == "judge" and card == "cluster":
        groups: dict[str, list[str]] = {}
        for line in prompt.splitlines():
            m = re.match(r"\[(\S+)\] (.+?) (variant|g\d)", line)
            if m:
                groups.setdefault(m.group(2), []).append(m.group(1))
        return json.dumps([{"name": k, "members": v} for k, v in groups.items()])
    if role == "judge" and card == "merge":
        ids = re.findall(r"^\[(\S+)\] \(\S+\) sliding window", prompt, flags=re.M)
        return json.dumps([ids[:2]] if len(ids) >= 2 else [])
    if role == "judge" and card == "prior":
        ids = re.findall(r"^\[(\S+)\]", prompt, flags=re.M)
        return json.dumps([{"id": i, "tag": "known" if k % 3 == 0 else "new", "match": "K0" if k % 3 == 0 else ""}
                           for k, i in enumerate(ids)])
    if card == "deepen":
        depth, gen, node = int(meta.get("depth", 0)), int(meta.get("gen", 0)), meta.get("node", "x")
        qa = "\n".join(f"Q{i}: what about aspect {i} at depth {depth}? | decides: option A vs option B\nA{i}: fact {i} about {node}." for i in range(1, 7))
        head = ("CHAIN:\nL1: the change -> smaller residual growth | quantity: residual RMS growth | baseline: 2.1 | expect: down, a tenth | breaks if: RMS unchanged at 45 steps\n"
                "L2: smaller growth -> lower loss | quantity: validation loss | baseline: 6.63 | expect: down, under 0.05 | breaks if: loss not below baseline at 240 steps\nWEAKEST: L2\n\n"
                if depth == 0 else "")
        tail = "\n\nLINK STATUS:\n- L1: confirmed | the RMS fell on the probe\n- L2: open | needs the long run" if depth > 0 else ""
        ideas = "\n\n".join(f"SLOT: {['drop', 'strengthen', 'port'][k]}\nIDEA: offshoot {node} {k} g{gen}\nMECHANISM: apply offshoot trick {k} to the {node} part.\n"
                            f"PREDICTION: lower loss\nTEST: 1-minute smoke run comparison\nSOURCE: own" for k in range(3))
        return (head + qa + "\n\nKNOWN:\n- init the new weights to zero [script]\n- costs 2 extra matmuls per layer https://arxiv.org/abs/2010.04245 [web]\n"
                "- about 15 percent slower (unsourced, should be dropped)\n- the gate probably saturates late [belief]\n\nASSUMES:\n- the gate is applied after attention\n\n"
                "NEW IDEAS:\n" + ideas + "\n\nOPEN:\n- does it interact with the warmup? | build: yes | decides: warmup 2% vs 5%\n- is it elegant? | build: no" + tail)
    if card == "program":                     # program search: change only lr_mult
        v = str(meta.get("seed", "0"))
        src = BASE.replace("def lr_mult(step: int, total: int, cfg: Config) -> float:",
                           "def lr_mult(step: int, total: int, cfg: Config) -> float:\n    _variant = " + v, 1)
        return "HYPOTHESIS: schedule variant " + v + "\nCHANGE: lr_mult\n```python\n" + src + "\n```"
    if role == "generate":                    # implementation: a change inside the part, except for 'mix' which breaks out
        node = meta.get("node") or ""
        op = str(meta.get("operator", ""))
        src = BASE
        if card == "revise" and "operator 'fix'" in prompt:            # the fix repairs the boundary violation
            src = BASE.replace("        self.attn, self.mlp = Attention(cfg), MLP(cfg)",
                               "        self.attn, self.mlp = Attention(cfg), MLP(cfg)\n        self.marker = 'fixed'", 1)
        elif card == "revise" and "operator 'variant:" in prompt:   # a near-miss variant: a wiring edit inside Block (allowed)
            src = BASE.replace("        self.attn, self.mlp = Attention(cfg), MLP(cfg)",
                               "        self.attn, self.mlp = Attention(cfg), MLP(cfg)\n        self.marker_variant = " + repr(op[:12]), 1)
        elif op.startswith("mix-") or (card == "revise" and "boundary" in prompt and "MLP" in prompt):
            src = BASE.replace("        self.w_down = nn.Linear", "        self.marker = 1\n        self.w_down = nn.Linear", 1)  # MLP.__init__: outside 'mix'
        elif op.startswith("io-"):            # GPT.__init__ (wiring, allowed): disjoint from the others, so composites can form
            src = BASE.replace("        self.norm = RMSNorm(cfg.d_model)",
                               "        self.norm = RMSNorm(cfg.d_model)\n        self.marker_io = " + repr(op)[:12], 1)
        elif op.startswith("ffn-"):           # MLP.__init__: inside the ffn boundary
            src = BASE.replace("        self.w_down = nn.Linear", "        self.marker_ffn = " + repr(op)[:12] + "\n        self.w_down = nn.Linear", 1)
        else:
            src = BASE.replace("        self.attn, self.mlp = Attention(cfg), MLP(cfg)",
                               "        self.attn, self.mlp = Attention(cfg), MLP(cfg)\n        self.marker = " + repr(op)[:12], 1)  # Block.__init__: wiring, allowed; distinct per idea
        assert src != BASE, "mock anchor missing"
        return ("HYPOTHESIS: mock change lowers loss.\nCHANGE: marker\nFIDELITY: exact, the idea as specified\n```python\n# mock candidate " + card + " " + op
                + "\n" + src + "\n```")
    return "1. A\n2. B\n3. C"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--batch", default="mock-dry")
    ap.add_argument("--implement", type=int, default=3)
    ap.add_argument("--budget", default="3000000")
    ap.add_argument("--rounds", default="2")
    ap.add_argument("--profile", default=os.environ.get("HTSA_PROFILE") or "llm",
                    help="problem profile passed to the loop (nano/profiles/<name>.py); the mock replies are written for llm, "
                         "binpack_nobase (Mode 2) and review_process (Mode 3)")
    a, rest = ap.parse_known_args()
    llm.set_mock(mock)
    sys.argv = ["loop", "--profile", a.profile, "--batch", a.batch, "--model", "fable", "--backend", "mock", "--budget", a.budget,
                "--rounds", a.rounds, "--learn-steps", "12", "--long-steps", "30", "--per-node", "1", "--diag-steps", "30", "--tune-knobs", "lr_x1.4,wd_x3",
                "--implement", str(a.implement)] + rest
    return L.main()


if __name__ == "__main__":
    raise SystemExit(main())
