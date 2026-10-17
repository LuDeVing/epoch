"""Card loader and executor (ARCHITECTURE.md section 3 /generate, P0 cards; Pr10, Pr13).

A card is YAML {name, role, steps: [{id, template, inputs, max_tokens, n, ...}],
operator_choices, applies_to} validated against strategies/schema.json. The runner resolves
each step's routed inputs from the Problem (never private/*, other candidates, graph or
cluster files), renders a fixed template, writes the prompt to prompts/<call_id>.txt, lints
it, writes the routed inputs into calls/<call_id>/in/ and calls llm.call. Output is parsed
into Candidate rows by script; one converter call runs only on parse failure.
"""
from __future__ import annotations

import json
import os
import random
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

from . import config, encode, lint, llm
from .schemas import KEY_FIELDS, Candidate, Usage, append_jsonl, new_id

# values the harness writes itself; lint findings inside them block the call
TRUSTED_KEYS = {"format", "operator", "seed", "n"}
OPERATOR_TEXT = {
    "none": "",
    "drop": "drop: remove one deep constraint from the problem.",
    "negate": "negate: replace one deep constraint with its negation.",
    "vary": "vary: change one quantity, object or condition of the problem to a different value.",
    "oppose": "oppose: reverse the goal so that the problem asks for the opposite outcome.",
    "fix": "fix: change the candidates only where they break a hard constraint or the feedback record, and keep the rest.",
    "specialize": "specialize: add one condition to the parent so that it separates the cases listed in the feedback record.",
    "recurse": "recurse: apply the parent's rule again to its own output, or to each part of the input separately.",
}
MAX_BT_CHARS = 200
MAX_PROGRAM_CHARS = 8000
JUSTIFICATION = re.compile(r"\b(?:because|since|this works|this is why|which is why|therefore)\b",
                           re.IGNORECASE)
_PH = re.compile(r"\{\{\s*([a-z_]+)\s*\}\}")
# Fenced code blocks: any info string (python, python3, Python, py, none), the rest of the
# fence line ignored; a final fence left unclosed (a reply cut at max_tokens) ends at the text end.
_CODE = re.compile(r"```[ \t]*[A-Za-z0-9_+.-]*[^\n]*\r?\n(.*?)(?:```|\Z)", re.DOTALL)
# Option letter at the start of a list item. "A man carries..." starts with an article, not
# option A (the probe parser makes the same choice: no first-word fallback). So a bare letter
# needs a delimiter (". ) : , - * ]" or the end), except B, C and D (never English words) and
# a capital A followed by a capitalised word or a justification word ("A The ...",
# "A because ..."). After an "option/answer/choice" prefix, or inside "(A)" / "[A]", a space
# may follow. An item equal to one option's text is matched to that option first.
_LETTER = re.compile(
    r"^[\s*_]*(?:(?i:option|answer|choice)\s*[:\-]?\s*\(?([A-Da-d])\)?(?=$|[\s.):,\-*\]])"
    r"|\(([A-Da-d])\)|\[([A-Da-d])\]"
    r"|([A-Da-d])(?=$|[.):,*\]]|\s*[-:]\s)"
    r"|([B-D])(?=\s)"
    r"|(A)(?=\s+(?:[A-Z]|(?i:because|since|as|therefore|which)\b)))")
_TRANSFORMED = re.compile(r"TRANSFORMED PROBLEM\s*\**\s*:?\s*\**", re.IGNORECASE)


class CardError(ValueError):
    pass


class LintError(RuntimeError):
    pass


@dataclass
class CardSpec:
    card: str
    operator: str = "none"
    seed: str = ""
    perm: int = 0
    variant: str | None = None
    parent_id: str | None = None


@dataclass
class CardRun:
    cands: list[Candidate]
    usage: Usage
    call_ids: list[str]
    contract: dict


# ---------------------------------------------------------------- card schema (section 6)
def _type_ok(v, t: str) -> bool:
    if t == "integer":
        return isinstance(v, int) and not isinstance(v, bool)
    if t == "boolean":
        return isinstance(v, bool)
    return isinstance(v, {"object": dict, "array": list, "string": str, "null": type(None)}[t])


def validate(obj, schema: dict, path: str = "$") -> list[str]:
    """Subset JSON-schema validator: type, enum, required, properties, additionalProperties,
    items, minItems, minimum (no jsonschema package in the venv)."""
    t = schema.get("type")
    if t and not any(_type_ok(obj, x) for x in (t if isinstance(t, list) else [t])):
        return [f"{path}: expected {t}"]
    errs = []
    if "enum" in schema and obj not in schema["enum"]:
        errs.append(f"{path}: {obj!r} not in {schema['enum']}")
    if "minimum" in schema and _type_ok(obj, "integer") and obj < schema["minimum"]:
        errs.append(f"{path}: {obj} < {schema['minimum']}")
    if isinstance(obj, dict):
        props = schema.get("properties", {})
        errs += [f"{path}: missing {k}" for k in schema.get("required", []) if k not in obj]
        for k, v in obj.items():
            if k in props:
                errs += validate(v, props[k], f"{path}.{k}")
            elif schema.get("additionalProperties") is False:
                errs.append(f"{path}: unexpected key {k}")
    if isinstance(obj, list):
        if len(obj) < schema.get("minItems", 0):
            errs.append(f"{path}: fewer than {schema['minItems']} items")
        for i, v in enumerate(obj):
            errs += validate(v, schema.get("items", {}), f"{path}[{i}]")
    return errs


@lru_cache(maxsize=1)
def _schema() -> dict:
    return json.loads((config.STRATEGIES_DIR / "schema.json").read_text(encoding="utf-8"))


def check_card(card: dict, name: str = "") -> list[str]:
    """Schema errors plus template existence and template/inputs agreement (Pr13)."""
    errs = validate(card, _schema())
    if errs:
        return errs
    if name and card["name"] != name:
        errs.append(f"name {card['name']!r} != file {name!r}")
    for st in card["steps"]:
        p = config.TEMPLATES_DIR / f"{st['template']}.txt"
        if not p.exists():
            errs.append(f"step {st['id']}: missing template {p.name}")
        elif placeholders(p.read_text(encoding="utf-8")) != set(st["inputs"]):
            errs.append(f"step {st['id']}: template placeholders != inputs")
    return errs


def load_card(name: str) -> dict:
    """Read strategies/<name>.yaml and validate it; raises CardError on any problem."""
    path = config.STRATEGIES_DIR / f"{name}.yaml"
    if not path.exists():
        raise CardError(f"no card {name}")
    card = yaml.safe_load(path.read_text(encoding="utf-8"))
    errs = check_card(card, name)
    if errs:
        raise CardError(f"card {name}: " + "; ".join(errs))
    return card


# ---------------------------------------------------------------- templates and dispatch
def load_template(name: str) -> str:
    return (config.TEMPLATES_DIR / f"{name}.txt").read_text(encoding="utf-8")


def placeholders(text: str) -> set[str]:
    return set(_PH.findall(text))


def render(text: str, values: dict[str, str]) -> tuple[str, list[tuple[int, int, str]]]:
    """Fill {{name}} placeholders; returns the prompt and the span of each inlined value.
    The routed values must equal the template's placeholders exactly."""
    need = placeholders(text)
    if need != set(values):
        raise CardError(f"routed inputs {sorted(values)} != placeholders {sorted(need)}")
    out, spans, pos, n = [], [], 0, 0
    for m in _PH.finditer(text):
        lit, val = text[pos:m.start()], str(values[m.group(1)])
        out += [lit, val]
        n += len(lit)
        spans.append((n, n + len(val), m.group(1)))
        n += len(val)
        pos = m.end()
    out.append(text[pos:])
    return "".join(out), spans


def lint_prompt(prompt: str, spans: list[tuple[int, int, str]]) -> list[dict]:
    """Pr10 lint of a rendered prompt; findings inside inlined item or model text are tagged
    in_input and never block, everything else (template and harness text) can block."""
    out = []
    for f in lint.lint_text(prompt):
        s, e = f["span"]
        f["in_input"] = any(a <= s and e <= b for a, b, k in spans if k not in TRUSTED_KEYS)
        out.append(f)
    return out


def code_blocks(text: str) -> list[str]:
    """Bodies of every fenced code block (shared by run_card, probe and the arms)."""
    return list(_CODE.findall(text or ""))


def lint_domain_prompt(prompt: str, spans: list[tuple[int, int, str]], nouns: list[str]) -> list[dict]:
    """Pr5 domain lint of a rendered low_prior prompt: the original item's domain nouns
    searched in every routed input span (template and harness text are fixed wording, not
    item cues). Every finding blocks."""
    out = []
    for a, b, k in spans:
        if k in TRUSTED_KEYS:
            continue
        for f in lint.lint_domain(prompt[a:b], nouns):
            s, e = f["span"]
            out.append(dict(f, span=[a + s, a + e], input=k, in_input=False))
    return out


def render_prompt(template: str, values: dict, *, role: str, run_dir: Path, call_id: str,
                  meta: dict | None = None, domain_nouns: list[str] | None = None) -> str:
    """Render a template from strategies/templates, write prompts/<call_id>.txt, lint it
    (blocking on template text, logged on inlined input), and append the routing row.
    Used by every role that is not a card step (judge, probe, plain) so the Pr10 lint and the
    section 3 routing audit cover them too. With domain_nouns (a low_prior step) the routed
    inputs are also linted against the original item's domain nouns, and a hit blocks (Pr5).
    A prompt over config.MAX_PROMPT_CHARS is cut by llm.fit_prompt before the file is
    written, so prompts/<call_id>.txt is exactly what is sent; the cut is logged."""
    run_dir = Path(run_dir)
    prompt, spans = render(load_template(template), {k: str(v) for k, v in values.items()})
    findings = lint_prompt(prompt, spans)
    if domain_nouns:
        findings += lint_domain_prompt(prompt, spans, domain_nouns)
    sent, truncated = llm.fit_prompt(prompt)
    pdir = run_dir / "prompts"
    pdir.mkdir(parents=True, exist_ok=True)
    (pdir / f"{call_id}.txt").write_text(sent, encoding="utf-8")
    blocking = [f for f in findings if f["severity"] == "fail" and not f["in_input"]]
    if findings:
        append_jsonl(pdir / "lint.jsonl", {"call_id": call_id, "template": template,
                                           "findings": findings, "blocked": bool(blocking)})
    if blocking:
        raise LintError(f"{template}: {[f['pattern'] for f in blocking]}")
    append_jsonl(run_dir / "routing.jsonl", {"call_id": call_id, "template": template, "role": role,
                                             "inputs": sorted(values), "meta": meta or {},
                                             **({"prompt_truncated": truncated} if truncated else {})})
    return sent


def write_sandbox(calls_dir: Path, call_id: str, values: dict) -> Path:
    """calls/<call_id>/in/ with one file per routed input: the call's cwd, so the model sees
    only its routed inputs and never the repo (Pr1, section 3 /generate)."""
    in_dir = Path(calls_dir) / call_id / "in"
    in_dir.mkdir(parents=True, exist_ok=True)
    for k, v in values.items():
        (in_dir / f"{k}.txt").write_text(str(v), encoding="utf-8")
    return in_dir


def dispatch(template: str, values: dict, *, role: str, run_dir: Path, log_dir: Path | None,
             backend: str, meta: dict, max_tokens: int | None = None,
             domain_nouns: list[str] | None = None) -> llm.CallResult:
    """Render, write prompts/<call_id>.txt, lint, write the sandbox in/, log routing, call.
    A private role (config.PRIVATE_ROLES, the defaults call) keeps its call record, sandbox
    and reply under runs/<id>/private/calls/ (Pr5: default answers live only in private/)."""
    run_dir = Path(run_dir)
    call_id = new_id("c")
    private = role in config.PRIVATE_ROLES
    calls_dir = (run_dir / "private" / "calls") if private else (run_dir / "calls")
    if private and log_dir is not None:
        log_dir = calls_dir
    prompt = render_prompt(template, values, role=role, run_dir=run_dir, call_id=call_id,
                           meta=dict(meta, private=True) if private else meta,
                           domain_nouns=domain_nouns)
    in_dir = write_sandbox(calls_dir, call_id, values)
    res = llm.call(prompt, role=role, call_id=call_id, max_tokens=max_tokens, cwd=in_dir,
                   backend=backend, log_dir=log_dir, meta=meta)
    append_jsonl(calls_dir / call_id / "out.jsonl",
                 {"call_id": call_id, "text": res.text, "error": res.error})
    return res


# ---------------------------------------------------------------- parsing and post-check
def post_check(text: str, benchmark: str) -> str | None:
    """Deterministic post-check (EVL-16). BT: keep the first sentence cut before any
    justification marker in it ("The driver is the reader because ..." keeps "The driver is
    the reader"), drop later sentences with justification markers, cap the length. ARC: reject
    programs over the cap."""
    text = (text or "").strip()
    if benchmark == "arc":
        return text if text and len(text) <= MAX_PROGRAM_CHARS else None
    sents = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    while sents and JUSTIFICATION.match(sents[0]):      # a leading "because ..." is not an answer
        sents.pop(0)
    if not sents:
        return ""
    m = JUSTIFICATION.search(sents[0])
    first = sents[0][:m.start()].rstrip(" ,;:-") if m else sents[0]
    if m and first and first[-1] not in ".!?":
        first += "."
    kept = [first] + [s for s in sents[1:] if not JUSTIFICATION.search(s)]
    out = " ".join(kept)
    if len(out) > MAX_BT_CHARS:
        out = out[:MAX_BT_CHARS].rsplit(" ", 1)[0].rstrip(" ,;:")
    return out


def _bt_item(item: str, choices: list[str] | None) -> dict | None:
    """One BT list item -> {text, program, pred}; letter first, else exact choice text."""
    item = item.replace("**", "").strip()
    norm = encode.norm_item(item)
    hits = [i for i, c in enumerate(choices or []) if encode.norm_item(str(c)) == norm]
    m = None if len(hits) == 1 else _LETTER.match(item)
    if len(hits) == 1:
        letter, rest = "ABCD"[hits[0]], ""
    elif m:
        letter = next(g for g in m.groups() if g).upper()
        rest = item[m.end():].lstrip(" .):-]").strip()
    else:
        return None
    rest = post_check(rest, "bt") if rest else ""
    return {"text": f"{letter}. {rest}" if rest else letter, "program": None, "pred": letter}


def parse_candidates(text: str, benchmark: str, choices: list[str] | None = None) -> list[dict]:
    """Script split of a generator reply: [{"text", "program"|None, "pred"|None}].
    ARC: python code blocks defining transform (pred left None for the verifier).
    BT: numbered items, each an option letter with optional one-line text."""
    if benchmark == "arc":
        out = []
        for block in code_blocks(text):
            src = post_check(block, "arc")
            if src and "def transform" in src:
                out.append({"text": src, "program": src, "pred": None})
        return out
    rows = [_bt_item(i, choices) for i in encode.numbered(text)]
    return [r for r in rows if r]


def extract_transformed(text: str) -> str:
    """Text after the TRANSFORMED PROBLEM header, else the whole reply."""
    m = _TRANSFORMED.search(text or "")
    return (text[m.end():] if m else (text or "")).strip()


# ---------------------------------------------------------------- routed context
def _rng(problem, replicate: int, purpose: str) -> random.Random:
    return random.Random(f"{problem.item_id}:scaffold:{replicate}:{purpose}")


def read_seed_file(path: Path) -> tuple[str, ...]:
    """Seed words, one per line; blank lines and "#" comment lines are skipped. The one
    reader for the card runner and the probe."""
    lines = (w.strip() for w in Path(path).read_text(encoding="utf-8").splitlines())
    return tuple(w for w in lines if w and not w.startswith("#"))


@lru_cache(maxsize=1)
def load_seeds() -> tuple[str, ...]:
    return read_seed_file(config.SEEDS_PATH)


def pick_operator(card: dict, spec: CardSpec, problem, replicate: int, round_no: int) -> str:
    """The allocator's operator if the card allows it, else uniform by script (GEN-12)."""
    choices = card["operator_choices"]
    if spec.operator in choices:
        return spec.operator
    if choices == ["none"]:
        return "none"
    return _rng(problem, replicate, f"operator:{card['name']}:{round_no}:{spec.seed}:{spec.perm}").choice(choices)


def pick_seed(spec: CardSpec, problem, replicate: int, round_no: int) -> str:
    return spec.seed or _rng(problem, replicate, f"seed:{round_no}:{spec.perm}").choice(load_seeds())


def resolve_view(card: dict, spec: CardSpec, problem, flags: dict | None = None) -> tuple[str, int]:
    """(variant, perm): spec.variant overrides the card view; a shuffled view with perm 0
    takes the problem's replicate permutation (REP-08). The run's flags decide: with
    flags.shuffle_facts off (pre-gate flag 4) every spec renders the canonical order, perm 0.
    `flags` is the run's merged flag dict; config.flags() is the fallback for callers without one."""
    flags = flags if flags is not None else config.flags()
    variant = spec.variant or card.get("view", "canonical")
    perm = int(spec.perm or 0)
    shuffle = bool(flags.get("shuffle_facts", True))
    if variant == "shuffled":
        variant = "canonical"
        if not perm and shuffle:
            perm = int(problem.meta.get("shuffled_perm", 0))
    if not shuffle:
        perm = 0
    if variant not in ("canonical", "low_prior"):
        raise CardError(f"unknown view {variant}")
    return variant, perm


def format_text(benchmark: str, n: int, flags: dict | None = None) -> str:
    """The format instruction. flags.experimental_think_aloud_self_check ("1" or "2", env
    HTSA_THINK_ALOUD) swaps in format_think[2].arc, written reasoning before the code that
    includes checking the rule against the examples: generator self-checking, which Pr1 bans
    for generators, so it is an experimental arm only, off by default and recorded in the run
    header and every call record."""
    flags = flags if flags is not None else config.flags()
    ta =str(flags.get("experimental_think_aloud_self_check") or "off")
    on = ta not in ("off", "0", "", "False", "false")
    name = ((f"format_think2.{benchmark}" if ta == "2" else f"format_think.{benchmark}")
            if (on and benchmark == "arc") else f"format.{benchmark}")
    return render(load_template(name), {"n": str(n)})[0].strip()


def cand_block(texts: list[str], benchmark: str) -> str:
    """Candidate texts as a numbered list; ARC programs go inside python code fences."""
    if benchmark == "arc":
        return "\n\n".join(f"{i}. ```python\n{t.strip()}\n```" for i, t in enumerate(texts, 1))
    return encode.numbered_block(texts, empty="")


def parent_text(parent: Candidate | None, benchmark: str) -> str:
    """The one routed parent artifact (Pr18): its program on ARC, its text otherwise."""
    if parent is None:
        return ""
    return cand_block([parent.program or parent.text or ""], benchmark)


def feedback_text(feedback: dict | None) -> str:
    return json.dumps(feedback, ensure_ascii=True, indent=1) if feedback else "No feedback record."


def build_context(card: dict, problem, *, variant: str, perm: int, operator: str, seed: str,
                  parent: Candidate | None, feedback: dict | None, n: int,
                  flags: dict | None = None) -> dict[str, str]:
    """Every value a step may route; built only from the Problem, the spec, the one parent
    and its feedback record (routing table, section 6)."""
    ctx = encode.view_parts(problem, variant, perm, card.get("data_style", "compact"))
    ctx.update(operator=OPERATOR_TEXT[operator], seed=seed, parent=parent_text(parent, problem.benchmark),
               feedback=feedback_text(feedback), format=format_text(problem.benchmark, n, flags),
               transformed="")
    return ctx


def _assert_stripped(problem) -> None:
    key = KEY_FIELDS.get(problem.benchmark)
    if key in (problem.item or {}):
        raise CardError(f"problem.item carries the key field {key}")


# ---------------------------------------------------------------- execution
def _max_tokens(step: dict, role: str, benchmark: str) -> int:
    if step.get("max_tokens"):
        return int(step["max_tokens"])
    mt = config.PARAMS["max_tokens"]
    if benchmark == "arc" and step.get("parser", "candidates") == "candidates":
        return mt["program"]
    return mt.get(role, mt["generate"])


def _parse_or_convert(res: llm.CallResult, problem, run_dir: Path, log_dir, backend: str,
                      meta: dict) -> tuple[list[dict], list[llm.CallResult]]:
    """Parse by script; on failure one converter call copies the text into a numbered list."""
    b, choices = problem.benchmark, problem.item.get("choices")
    parsed = parse_candidates(res.text, b, choices)
    if parsed or not (res.text or "").strip():
        return parsed, []
    conv = dispatch(f"converter.{b}", {"raw": res.text}, role="converter", run_dir=run_dir,
                    log_dir=log_dir, backend=backend, meta=dict(meta, step=meta["step"] + ":converter"))
    return parse_candidates(conv.text, b, choices), [conv]


def _rows(parsed: list[dict], *, card: dict, step: dict, call_id: str, operator: str, seed: str,
          perm: int, round_no: int, variant: str, parents: list[Candidate]) -> list[Candidate]:
    pid = [p.id for p in parents]
    lineage = (parents[0].lineage_id or parents[0].id) if parents else ""
    island = parents[0].island_id if parents else "main"
    out = []
    for p in parsed:
        cid = new_id("cd")
        out.append(Candidate(id=cid, text=p["text"], card=card["name"], operator=operator, seed=seed,
                             perm=perm, round=round_no, call_id=call_id, parent_ids=list(pid),
                             island_id=island, lineage_id=lineage or cid, program=p["program"],
                             pred=p["pred"], extra={"step": step["id"], "variant": variant}))
    return out


def _script_feedback(parent: Candidate, problem) -> dict | None:
    """Deterministic feedback record for a scripted parent (ARC: demo_match by the runner,
    0 tokens); None where no external check exists (BT)."""
    if problem.benchmark != "arc" or not parent.program:
        return None
    from . import arc_exec, feedback
    try:
        demo = arc_exec.demo_match(parent.program, problem.item.get("train", []))
    except Exception:  # noqa: BLE001 - an unrunnable parent gets no record, not a crash
        return None
    return feedback.record_for(parent, demo, "arc", config.PARAMS["feedback_cap_tokens"])


def _write_cands(run_dir: Path, root: str, cands: list[Candidate]) -> Path:
    path = run_dir / "cands" / f"{root}.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(c.to_dict(), ensure_ascii=False) + "\n" for c in cands),
                    encoding="utf-8")
    return path


def run_card(spec: CardSpec, problem, run_dir: Path, *, backend: str, round_no: int,
             log_dir: Path, replicate: int, parent: Candidate | None = None,
             feedback: dict | None = None, flags: dict | None = None) -> CardRun:
    """Execute one card (section 3 /generate). Writes cands/<id>.jsonl and returns the
    candidates plus the return contract {id, path, n_cands} (REP-16).

    `flags` is the run's flag dict (shuffle_facts and experimental_think_aloud_self_check are
    read here). Errors before the first model call raise (CardError, LintError); an error after
    a call returned is not raised but reported in contract["error"], with the usage and call
    ids of the completed steps, so the driver can charge the spend (section 4: every call is
    charged). Other errors keep the completed steps' candidates; a LintError drops them all
    (contract["lint_blocked"]), so a blocking lint blocks the card at any step."""
    card, run_dir, b = load_card(spec.card), Path(run_dir), problem.benchmark
    if b not in card["applies_to"]:
        raise CardError(f"card {spec.card} does not apply to {b}")
    _assert_stripped(problem)
    needs_parent = any("parent" in st["inputs"] for st in card["steps"][:1])
    if needs_parent and parent is None:
        raise CardError(f"card {spec.card} needs a parent candidate")
    operator = pick_operator(card, spec, problem, replicate, round_no)
    uses_seed = any("seed" in st["inputs"] for st in card["steps"])
    seed = pick_seed(spec, problem, replicate, round_no) if uses_seed else ""
    variant, perm = resolve_view(card, spec, problem, flags)
    n_default = int(os.environ.get("HTSA_CANDS_PER_GEN") or config.BENCHMARKS[b]["cands_per_generator"])
    ctx = build_context(card, problem, variant=variant, perm=perm, operator=operator, seed=seed,
                        parent=parent, feedback=feedback, n=n_default, flags=flags)
    # Pr5: a low_prior step is linted against the original item's domain nouns
    nouns = list((problem.meta or {}).get("domain_nouns") or []) if variant == "low_prior" else None
    usage, call_ids, cands, root = Usage(), [], [], None
    parents = [parent] if parent else []
    error, lint_blocked = None, False
    try:
        for step in card["steps"]:
            if any(k in ("parent", "transformed") and not ctx[k].strip() for k in step["inputs"]):
                append_jsonl(run_dir / "routing.jsonl", {"skipped": step["id"], "card": card["name"],
                                                         "reason": "empty routed input"})
                continue
            n = step.get("n") or n_default
            values = {k: ctx[k] for k in step["inputs"]}
            if "format" in values:
                values["format"] = format_text(b, n, flags)
            if step.get("operator"):
                values["operator"] = OPERATOR_TEXT[step["operator"]]
            role = step.get("role", card["role"])
            meta = {"benchmark": b, "item_id": problem.item_id, "card": card["name"], "step": step["id"],
                    "round": round_no, "operator": operator}
            res = dispatch(step["template"], values, role=role, run_dir=run_dir, log_dir=log_dir,
                           backend=backend, meta=meta, max_tokens=_max_tokens(step, role, b),
                           domain_nouns=nouns)
            root = root or res.call_id
            call_ids.append(res.call_id)
            usage = usage.add(res.usage)
            if step.get("parser", "candidates") == "transformed":
                ctx["transformed"] = extract_transformed(res.text)
                path = run_dir / "variants" / f"transformed_{res.call_id}.md"
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(ctx["transformed"], encoding="utf-8")
                continue
            parsed, extra = _parse_or_convert(res, problem, run_dir, log_dir, backend, meta)
            for c in extra:
                call_ids.append(c.call_id)
                usage = usage.add(c.usage)
            rows = _rows(parsed[:n], card=card, step=step, call_id=res.call_id, operator=operator,
                         seed=seed, perm=perm, round_no=round_no, variant=variant, parents=parents)
            if step.get("emit", True):
                cands.extend(rows)
            if rows:
                # the next step gets one parent (Pr18): the first candidate of this step, by
                # script, with its deterministic feedback record (ARC demo_match, 0 tokens)
                parents = rows[:1]
                ctx["parent"] = parent_text(parents[0], b)
                ctx["feedback"] = feedback_text(_script_feedback(parents[0], problem))
    except Exception as e:  # noqa: BLE001
        if not call_ids:
            raise
        error = f"{type(e).__name__}: {str(e)[:300]}"
        if isinstance(e, LintError):
            # A blocking lint stays blocking mid-card: the failed step is never called and the
            # card emits no candidates, while the spend of the calls already made is still
            # returned so the driver charges it (section 4: every call is charged).
            lint_blocked = True
            cands = []
    root = root or new_id("c")
    path = _write_cands(run_dir, root, cands)
    contract = {"id": root, "path": str(path), "n_cands": len(cands)}
    if error:
        contract["error"] = error
    if lint_blocked:
        contract["lint_blocked"] = True
    return CardRun(cands=cands, usage=usage, call_ids=call_ids, contract=contract)
