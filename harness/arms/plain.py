"""Plain chain-of-thought arm and the per-call helpers shared by the best-of-N arms
(ARCHITECTURE.md section 8, Arms and Cost; section 9 step 1).

One call with a plain step-by-step prompt (strategies/templates/plain.<benchmark>.txt, rendered
and linted through run_card.render_prompt) that asks for the final answer in a fixed format:
ARC: one python code block defining transform(grid) -> grid, executed by arc_exec to get the
predicted test grid; BRAINTEASER: a final line "ANSWER: <letter>". Every prompt is built from
schemas.strip_key(item); this module never reads the key fields.

Every run gets a fresh run_instance id (ledger rows and the runs.jsonl row carry it) so a
re-run of the same run_id stays distinguishable. A plain call that errors is written with
status "error" so bench retries it and keeps it out of the cost measurement.

Run folder (section 2): runs/<run_id>/{answer.json, prompts/<call_id>.txt, calls/<call_id>.json,
calls/<call_id>/out.jsonl, cands/<call_id>.jsonl}; one results/<batch>/runs.jsonl row per run and
one ledger row per call.
"""
from __future__ import annotations

import os
import random
import re
import threading
import time
from pathlib import Path

from .. import config, llm
from ..schemas import (Answer, Candidate, LedgerRow, append_jsonl, new_id, now_ts, option_letter,
                       strip_key, write_json)

_WRITE_LOCK = threading.Lock()

TEMPLATES = {"arc": "plain.arc", "bt": "plain.bt"}


# ---------------------------------------------------------------- ids, seeds, folders
def run_id_for(batch: str, benchmark: str, item_id: str, arm: str, replicate: int) -> str:
    """README contract: f"{batch}__{benchmark}__{item_id}__{arm}__r{replicate}"."""
    return f"{batch}__{benchmark}__{item_id}__{arm}__r{replicate}"


def rng_for(item_id: str, arm: str, replicate: int, purpose: str) -> random.Random:
    """README Determinism: every random choice is seeded by (item, arm, replicate, purpose)."""
    return random.Random(f"{item_id}:{arm}:{replicate}:{purpose}")


def prepare_run_dir(run_id: str) -> Path:
    """Fresh run folder; an existing one is moved aside (never deleted)."""
    run_dir = Path(config.RUNS_DIR) / run_id
    if run_dir.exists():
        run_dir.rename(run_dir.with_name(f"{run_id}.old-{time.strftime('%Y%m%d-%H%M%S')}"))
    for sub in ("prompts", "calls", "cands"):
        (run_dir / sub).mkdir(parents=True, exist_ok=True)
    return run_dir


# ---------------------------------------------------------------- prompts
def grid_text(grid) -> str:
    return "\n".join(" ".join(str(c) for c in row) for row in grid)


def arc_data(item: dict, order: list[int]) -> str:
    """Train pairs in presentation order and the test input, as rows of digits."""
    lines = []
    for n, idx in enumerate(order, 1):
        pair = item["train"][idx]
        lines += [f"Example {n} input:", grid_text(pair["input"]),
                  f"Example {n} output:", grid_text(pair["output"]), ""]
    lines += ["Test input:", grid_text(item["test_input"])]
    return "\n".join(lines)


def bt_data(item: dict, order: list[int]) -> str:
    """Question and options; `order[j]` is the original index shown as letter j."""
    lines = ["Question: " + str(item["question"]).strip(), "", "Options:"]
    for j, idx in enumerate(order):
        lines.append(f"{option_letter(j)}. {item['choices'][idx]}")
    return "\n".join(lines)


def prompt_values(item: dict, order: list[int], seed_word: str | None = None) -> dict:
    """The routed values of the plain template: data (key-stripped item) and seed line."""
    item = strip_key(item)
    data = arc_data(item, order) if item["benchmark"] == "arc" else bt_data(item, order)
    seed = f"\nSeed word (a starting point you may use or ignore): {seed_word}\n" if seed_word else ""
    return {"data": data, "seed": seed}


def build_prompt(item: dict, order: list[int], seed_word: str | None = None) -> str:
    """The plain prompt text, no files written (tests and estimates)."""
    from ..run_card import load_template, render
    item = strip_key(item)
    return render(load_template(TEMPLATES[item["benchmark"]]), prompt_values(item, order, seed_word))[0]


def canonical_order(item: dict) -> list[int]:
    n = len(item["train"]) if item["benchmark"] == "arc" else len(item["choices"])
    return list(range(n))


# ---------------------------------------------------------------- parsing
_CODE_RE = re.compile(r"```[ \t]*([A-Za-z0-9_+-]*)[^\n]*\n(.*?)```", re.S)
_ANSWER_RE = re.compile(r"ANSWER\s*[:=\-]?\s*\**\s*\(?\s*([A-D])\b", re.I)
_LONE_RE = re.compile(r"^\s*(?:\d+[.)]\s*)?\**\(?([A-D])\)?\**[.):]?\s*$", re.M)
_PHRASE_RE = re.compile(r"answer\s+is\s*:?\s*\**\s*\(?([A-D])\b", re.I)


def parse_program(text: str) -> str | None:
    """Last fenced code block that defines transform(); else an unfenced def transform tail."""
    blocks = [body for _lang, body in _CODE_RE.findall(text or "")]
    for body in reversed(blocks):
        if "def transform" in body:
            return body.strip() + "\n"
    pos = (text or "").rfind("def transform")
    if pos >= 0:
        return text[pos:].strip() + "\n"
    return None


def parse_letter(text: str) -> int | None:
    """Displayed option index 0-3 from the final answer line; robust fallbacks."""
    text = text or ""
    for rx, pick_last in ((_ANSWER_RE, True), (_LONE_RE, False), (_PHRASE_RE, True)):
        found = rx.findall(text)
        if found:
            return "ABCD".index((found[-1] if pick_last else found[0]).upper())
    return None


# ---------------------------------------------------------------- one call
def _arc_exec():
    from .. import arc_exec  # verify owner's module; imported lazily
    return arc_exec


def _ledger_append(row: LedgerRow) -> None:
    """Ledger writer of the memory owner; plain append to the ledger file if it is absent."""
    try:
        from .. import ledger
    except ImportError:
        ledger = None
    with _WRITE_LOCK:                    # best-of-N calls run in threads
        if ledger is None:
            append_jsonl(Path(config.LEDGER_PATH), row.to_dict())
        else:
            ledger.append(row)


def _to_candidate(item: dict, text: str, order: list[int], check_demo: bool, **fields) -> Candidate:
    """Parse the reply into a Candidate; ARC programs are executed for pred (and demo if asked)."""
    cand = Candidate(id=new_id("k"), text="", round=0, origin="spoken", **fields)
    cand.extra["order"] = order
    if item["benchmark"] == "arc":
        prog = parse_program(text)
        cand.program, cand.text = prog, prog or ""
        if prog:
            ex = _arc_exec()
            cand.pred = ex.predict(prog, item["test_input"])
            if check_demo:
                demo = ex.demo_match(prog, item["train"])
                cand.extra["demo"] = {"matched": int(demo.get("matched", 0)),
                                      "total": int(demo.get("total", 0))}
    else:
        j = parse_letter(text)
        if j is not None and j < len(order):
            cand.pred = option_letter(order[j])
            cand.text = cand.pred
    return cand


def plain_call(item: dict, *, arm: str, run_dir: Path, backend: str, replicate: int, batch: str,
               index: int = 0, seed_word: str = "", shuffle: bool = False, card: str = "plain",
               check_demo: bool = False, run_instance: str | None = None) -> tuple[Candidate, llm.CallResult]:
    """One plain CoT call: render (linted template), log prompt, call, parse, write cands row
    and ledger row."""
    from ..run_card import render_prompt
    item = strip_key(item)
    order = canonical_order(item)
    perm_id = 0
    if shuffle:
        rng_for(item["id"], arm, replicate, f"perm:{index}").shuffle(order)
        perm_id = 0 if order == sorted(order) else index + 1
    call_id = new_id("c")
    meta = {"benchmark": item["benchmark"], "item_id": item["id"], "arm": arm,
            "replicate": replicate, "index": index, "seed": seed_word}
    prompt = render_prompt(TEMPLATES[item["benchmark"]], prompt_values(item, order, seed_word or None),
                           role="plain", run_dir=run_dir, call_id=call_id, meta=meta)
    res = llm.call(prompt, role="plain", call_id=call_id, backend=backend,
                   log_dir=run_dir / "calls", meta=meta,
                   effort=os.environ.get("HTSA_PLAIN_EFFORT") or None,   # e.g. max: the model thinking as hard as it can
                   # HTSA_PLAIN_TOOLS=Agent lets the model work as Claude Code normally would, spawning its own
                   # subagents; no web or file tools, so it cannot look the answer up
                   tools=[t for t in os.environ.get("HTSA_PLAIN_TOOLS", "").split(",") if t.strip()] or None,
                   max_turns=int(os.environ.get("HTSA_PLAIN_TURNS", "0")) or None)
    append_jsonl(run_dir / "calls" / call_id / "out.jsonl", {"text": res.text, "error": res.error})
    cand = _to_candidate(item, res.text, order, check_demo, card=card, operator="none",
                         seed=seed_word, perm=perm_id, call_id=call_id)
    append_jsonl(run_dir / "cands" / f"{call_id}.jsonl", cand.to_dict())
    _ledger_append(LedgerRow(
        run_id=run_dir.name, batch=batch, benchmark=item["benchmark"], item_id=item["id"],
        split=str(item.get("split", "")), family=str(item.get("family", "")),
        cls=str(item.get("family", "")), arm=arm, card=card, operator="none", round_type="first",
        round=0, seed=seed_word, perm=perm_id, call_id=call_id, tokens=res.usage.to_dict(),
        cand_id=cand.id, run_instance=run_instance))
    return cand, res


# ---------------------------------------------------------------- run bookkeeping
def finish_run(item: dict, *, arm: str, replicate: int, batch: str, run_dir: Path,
               answer: Answer, n_calls: int, budget_tokens: int | None,
               run_instance: str | None = None, error: str | None = None) -> Answer:
    """Write answer.json and the results/<batch>/runs.jsonl row (README contract). An errored
    run (no reply at all) gets status "error" in the row so bench retries it; overshoot =
    spend above budget_tokens (0 without a budget)."""
    write_json(run_dir / "answer.json", answer.to_dict())
    status = "error" if error else answer.status
    row = {"batch": batch, "benchmark": item["benchmark"], "item_id": item["id"], "arm": arm,
           "replicate": replicate, "run_id": run_dir.name, "status": status,
           "answer": answer.answer, "spent_tokens": answer.spent_tokens, "rounds": answer.rounds,
           "ts": now_ts(), "n_calls": n_calls, "budget_tokens": budget_tokens,
           "overshoot": max(0, answer.spent_tokens - budget_tokens) if budget_tokens else 0,
           "run_instance": run_instance, "error": error}
    with _WRITE_LOCK:
        append_jsonl(Path(config.RESULTS_DIR) / batch / "runs.jsonl", row)
    return answer


def answer_from(cand: Candidate | None, *, spent: int, status: str | None = None,
                vtype: str | None = None, reason: str = "") -> Answer:
    """Answer record; a run with no parseable prediction abstains."""
    if cand is None or cand.pred is None:
        return Answer(status="abstain", answer=None, verification_type=vtype, cand_id=None,
                      spent_tokens=spent, rounds=1, best_guess=None,
                      reason=reason or "no parseable answer")
    return Answer(status=status or "unverified", answer=cand.pred, verification_type=vtype,
                  cand_id=cand.id, spent_tokens=spent, rounds=1, best_guess=cand.pred,
                  reason=reason)


def run_arm(arm: str, item: dict, *, m: int, replicate: int, backend: str, batch: str,
            budget_tokens: int | None = None) -> Answer:
    """Plain arm: one CoT call (section 8 Arms). m and budget_tokens are recorded, not used."""
    if arm != "plain":
        from .best_of_n import run_arm as bon_run_arm
        return bon_run_arm(arm, item, m=m, replicate=replicate, backend=backend, batch=batch,
                           budget_tokens=budget_tokens)
    item = strip_key(item)
    backend = backend or config.default_backend()
    run_dir = prepare_run_dir(run_id_for(batch, item["benchmark"], item["id"], arm, replicate))
    inst = new_id("i")
    cand, res = plain_call(item, arm=arm, run_dir=run_dir, backend=backend, replicate=replicate,
                           batch=batch, run_instance=inst)
    answer = answer_from(cand, spent=res.usage.total_tokens, reason=res.error or "")
    return finish_run(item, arm=arm, replicate=replicate, batch=batch, run_dir=run_dir,
                      answer=answer, n_calls=1, budget_tokens=budget_tokens, run_instance=inst,
                      error=res.error if (res.error and not res.text) else None)
