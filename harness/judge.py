"""Blind judge (ARCHITECTURE.md section 3, /judge; section 4 step `J = judge(C)`).

A fresh call scores candidates blind: it sees problem.md (goal, facts, constraints), the
key-stripped item data, and candidates stripped to {id, text, testable_claim} under opaque
per-run aliases. It never sees rationales (ARC programs are stripped of comments and
docstrings, EVL-16), cards, seeds, generator identity or serial position. Batches of at most
5 are scored under two permutations (perm_a, perm_b) and averaged; a batch of one is scored
pointwise. p_raw is logged and steers nothing at P0 (EVL-08).

The prompt is strategies/templates/judge.txt, rendered and linted through run_card.render_prompt
(prompts/<call_id>.txt and a routing.jsonl row per call). est_cost() gives the driver the
token estimate it reserves before judging (section 4 Spend accounting).
"""
from __future__ import annotations

import ast
import json
import math
import random
import re
from pathlib import Path

from . import config, llm
from .schemas import Candidate, Judgment, Usage, new_id, strip_key

BATCH_MAX = 5
TEXT_CAP_CHARS = 4000          # deterministic truncation of candidate text
CLAIM_CAP_CHARS = 600
FALLBACK_P = 0.5
ARM = "scaffold"
TEMPLATE = "judge"
_ALIAS_CHARS = "abcdefghjkmnpqrstuvwxyz23456789"
_NUM = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
_COMMENT_LINE = re.compile(r"(?m)^[ \t]*#.*\n?")
_TRAILING_COMMENT = re.compile(r"(?m)[ \t]+#[^\n'\"]*$")


# ---------------------------------------------------------------- prompt pieces
def item_data(problem, benchmark: str) -> str:
    """Key-stripped item data as plain text (section 3 /encode step 2: prompts use strip_key)."""
    item = strip_key({**dict(problem.item), "benchmark": benchmark})
    if benchmark == "arc":
        data = {"train": item.get("train", []), "test_input": item.get("test_input")}
        return json.dumps(data, separators=(",", ":"))
    lines = [str(item.get("question", ""))]
    for i, ch in enumerate(item.get("choices", [])):
        lines.append(f"{'ABCD'[i]}. {ch}")
    return "\n".join(lines)


def strip_rationale(src: str) -> str:
    """A program without its comments and docstrings (the judge never sees rationales).
    ast.unparse drops comments; docstring expression statements are removed explicitly. A
    program that does not parse loses its comment lines by regex instead."""
    try:
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        text = _COMMENT_LINE.sub("", src or "")
        return _TRAILING_COMMENT.sub("", text).strip()

    class _Drop(ast.NodeTransformer):
        def _strip_body(self, node):
            body = [b for b in node.body
                    if not (isinstance(b, ast.Expr) and isinstance(b.value, ast.Constant)
                            and isinstance(b.value.value, str))]
            node.body = body or [ast.Pass()]
            return node

        def visit_Module(self, node):
            self.generic_visit(node)
            node.body = [b for b in node.body
                         if not (isinstance(b, ast.Expr) and isinstance(b.value, ast.Constant)
                                 and isinstance(b.value.value, str))]
            return node

        def visit_FunctionDef(self, node):
            self.generic_visit(node)
            return self._strip_body(node)

        visit_AsyncFunctionDef = visit_FunctionDef
        visit_ClassDef = visit_FunctionDef

    return ast.unparse(_Drop().visit(tree)).strip()


def blind_view(cand: Candidate, alias: str, benchmark: str | None = None) -> dict:
    """Strip a candidate to {id, text, testable_claim}, truncated (section 3 /judge Input).
    ARC candidates are programs: their comments and docstrings are removed first."""
    text = cand.text or ""
    if benchmark == "arc" or cand.program:
        text = strip_rationale(cand.program or text)
    view = {"id": alias, "text": text[:TEXT_CAP_CHARS]}
    if cand.testable_claim:
        view["testable_claim"] = cand.testable_claim[:CLAIM_CAP_CHARS]
    return view


def prompt_values(problem, benchmark: str, views: list[dict]) -> dict:
    return {"problem_md": problem.problem_md, "data": item_data(problem, benchmark),
            "cands": json.dumps(views, ensure_ascii=True, indent=1)}


def build_prompt(problem, benchmark: str, views: list[dict]) -> str:
    """The judge prompt text (tight template, section 3 preamble) without writing files."""
    from .run_card import load_template, render
    return render(load_template(TEMPLATE), prompt_values(problem, benchmark, views))[0]


# ---------------------------------------------------------------- batching and permutations
def make_batches(n: int, rng: random.Random) -> list[list[int]]:
    """Shuffle indices, split into ceil(n/5) near-equal batches (section 3 /judge step 1)."""
    order = list(range(n))
    rng.shuffle(order)
    k = math.ceil(n / BATCH_MAX) if n else 0
    return [order[i::k] for i in range(k)]


def second_perm(batch: list[int]) -> list[int]:
    """perm_b rotates perm_a by half its length, so every position changes when size >= 2."""
    h = len(batch) // 2
    return batch[h:] + batch[:h]


def make_aliases(cands: list[Candidate], rng: random.Random) -> list[str]:
    """Opaque ids that carry no card, seed or position information (section 3 /judge Rules)."""
    seen: set[str] = set()
    out = []
    for _ in cands:
        a = "x" + "".join(rng.choice(_ALIAS_CHARS) for _ in range(5))
        while a in seen:
            a += rng.choice(_ALIAS_CHARS)
        seen.add(a)
        out.append(a)
    return out


def n_calls(n: int) -> int:
    """Calls one judge round makes for n candidates: 1 per batch of one, else 2 per batch."""
    if n <= 0:
        return 0
    k = math.ceil(n / BATCH_MAX)
    sizes = [len(range(n)[i::k]) for i in range(k)]
    return sum(1 if s == 1 else 2 for s in sizes)


def est_cost(cands: list[Candidate], problem, backend: str | None = None) -> int:
    """Tokens one judge round is expected to cost: per call the prompt (problem.md, item data
    and the capped candidate texts of its batch) at chars / 4, the judge max_tokens, and the
    CLI overhead on cli_json (section 4 Spend accounting; reserved before judging)."""
    n = len(cands)
    if n == 0:
        return 0
    benchmark = problem.benchmark
    fixed = len(problem.problem_md or "") + len(item_data(problem, benchmark)) + 600
    per_cand = [min(len(blind_view(c, "xxxxxx", benchmark)["text"]), TEXT_CAP_CHARS) + 40 for c in cands]
    mean_cand = sum(per_cand) / n
    k = math.ceil(n / BATCH_MAX)
    overhead = config.CLI_OVERHEAD_TOKENS_EST if backend in (None, "cli_json") else 0
    total = 0
    for i in range(k):
        size = len(range(n)[i::k])
        prompt_chars = fixed + size * mean_cand
        per_call = int(prompt_chars // 4) + config.PARAMS["max_tokens"]["judge"] + overhead
        total += per_call * (1 if size == 1 else 2)
    return int(total)


# ---------------------------------------------------------------- parsing
def _clamp(x, lo: float, hi: float) -> float | None:
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    if math.isnan(v):
        return None
    return max(lo, min(hi, v))


def _percent(x):
    """'80%' -> 0.8; other values unchanged."""
    if isinstance(x, str) and x.strip().endswith("%"):
        try:
            return float(x.strip()[:-1]) / 100.0
        except ValueError:
            return None
    return x


def _json_value(text: str):
    """Outermost JSON object or list in text, tolerating code fences and surrounding prose."""
    t = re.sub(r"```(?:json)?", "", text or "")
    starts = [i for i in (t.find("{"), t.find("[")) if i >= 0]
    if not starts:
        return None
    start = min(starts)
    end = max(t.rfind("}"), t.rfind("]"))
    if end <= start:
        return None
    try:
        return json.loads(t[start:end + 1])
    except json.JSONDecodeError:
        return None


def _json_object(text: str) -> dict | None:
    """Reply as {alias: {p, score}}: a JSON object, or a list of {id, p, score} objects."""
    obj = _json_value(text)
    if isinstance(obj, list):
        out = {}
        for e in obj:
            if isinstance(e, dict) and e.get("id") is not None:
                out[str(e["id"])] = {k: v for k, v in e.items() if k != "id"}
        return out or None
    return obj if isinstance(obj, dict) else None


def _regex_entry(text: str, alias: str) -> dict | None:
    """Salvage one alias entry from malformed JSON (numbers with exponents and percentages)."""
    m = re.search(re.escape(alias) + r'"?\s*:\s*\{([^{}]*)\}', text or "")
    if not m:
        return None
    body = m.group(1)
    p = re.search(r'"?\bp"?\s*:\s*(' + _NUM + r')\s*(%?)', body)
    s = re.search(r'"?score"?\s*:\s*(' + _NUM + r')', body)
    return {"p": (p.group(1) + p.group(2)) if p else None, "score": s.group(1) if s else None}


def parse_reply(text: str, aliases: list[str]) -> dict[str, dict]:
    """Map alias -> {"p", "score", "ok"}; missing or malformed entries fall back to p = 0.5."""
    obj = _json_object(text) or {}
    if len(aliases) == 1 and "p" in obj and aliases[0] not in obj:
        obj = {aliases[0]: obj}                       # pointwise reply without the id wrapper
    out = {}
    for a in aliases:
        entry = obj.get(a) if isinstance(obj.get(a), dict) else _regex_entry(text, a)
        p = _clamp(_percent(entry.get("p")), 0.0, 1.0) if entry else None
        s = _clamp(entry.get("score"), 1.0, 5.0) if entry else None
        out[a] = {"p": FALLBACK_P if p is None else p, "score": s, "ok": p is not None}
    return out


# ---------------------------------------------------------------- calls
def _call_specs(problem, benchmark, cands, aliases, batches, backend, log_dir):
    """One call spec per (batch, permutation); pointwise (one call) for a batch of one.
    Prompts are rendered through run_card.render_prompt into runs/<id>/prompts/ and linted."""
    from .run_card import render_prompt
    run_dir = Path(log_dir).parent if log_dir is not None else None
    specs, plan = [], []
    for bi, batch in enumerate(batches):
        perms = [("a", batch)] if len(batch) == 1 else [("a", batch), ("b", second_perm(batch))]
        for tag, order in perms:
            views = [blind_view(cands[i], aliases[i], benchmark) for i in order]
            cid = new_id("c")
            meta = {"benchmark": benchmark, "item_id": problem.item_id, "batch": bi, "perm": tag,
                    "n": len(order)}
            values = prompt_values(problem, benchmark, views)
            if run_dir is not None:
                prompt = render_prompt(TEMPLATE, values, role="judge", run_dir=run_dir, call_id=cid,
                                       meta=meta)
            else:
                prompt = build_prompt(problem, benchmark, views)
            specs.append(dict(prompt=prompt, role="judge", call_id=cid, backend=backend,
                              log_dir=log_dir, max_tokens=config.PARAMS["max_tokens"]["judge"],
                              meta=meta))
            plan.append((bi, tag, order))
    return specs, plan


def _judgment(cand: Candidate, res_a: dict, res_b: dict | None, call_ids: list[str],
              size: int) -> Judgment:
    """p_raw = mean of the two permutations; spread = |perm_a - perm_b| (MSR-13, EVL-03)."""
    pa = res_a["p"]
    pb = res_b["p"] if res_b else None
    p_raw = pa if pb is None else (pa + pb) / 2.0
    rubric = {"score_a": res_a["score"], "score_b": res_b["score"] if res_b else None,
              "parse_a": res_a["ok"], "parse_b": res_b["ok"] if res_b else None,
              "batch_size": size}
    return Judgment(id=cand.id, p_raw=round(p_raw, 4), rubric=rubric, perm_a=pa, perm_b=pb,
                    spread=None if pb is None else round(abs(pa - pb), 4), call_ids=call_ids)


def judge(cands: list[Candidate], problem, *, backend: str, log_dir: Path,
          replicate: int) -> tuple[list[Judgment], Usage]:
    """Score candidates blind (section 3 /judge steps 1-2). Returns Judgments in input order and
    the summed usage of every judge call. The caller writes judgments.jsonl."""
    if not cands:
        return [], Usage()
    benchmark = problem.benchmark
    rng = random.Random(f"{problem.item_id}:{ARM}:{replicate}:judge")
    aliases = make_aliases(cands, rng)
    batches = make_batches(len(cands), rng)
    specs, plan = _call_specs(problem, benchmark, cands, aliases, batches, backend, log_dir)
    results = llm.call_many(specs)
    usage = Usage()
    parsed: dict[tuple[int, str], dict] = {}
    ids: dict[int, list[str]] = {}
    for (bi, tag, order), res in zip(plan, results):
        usage = usage.add(res.usage)
        parsed[(bi, tag)] = parse_reply("" if res.error else res.text, [aliases[i] for i in order])
        ids.setdefault(bi, []).append(res.call_id)
    by_index: dict[int, Judgment] = {}
    for bi, batch in enumerate(batches):
        for i in batch:
            ra = parsed[(bi, "a")][aliases[i]]
            rb = parsed[(bi, "b")][aliases[i]] if (bi, "b") in parsed else None
            by_index[i] = _judgment(cands[i], ra, rb, ids[bi], len(batch))
    return [by_index[i] for i in range(len(cands))], usage
