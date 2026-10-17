"""Ideation stage for the nano loop: many independent contexts produce short idea sketches,
the sketches are clustered by meaning, and implementation slots are given across clusters.

Research basis (SYNTHESIS.md): independent contexts with distinct inputs raise originality,
longer lists from one context do not (GEN-06, GEN-10, SOC-01); stated justifications are
post hoc and must not rank ideas (EVL-16), so each sketch carries a PREDICTION and a TEST,
which are claims a cheap check can falsify, and selection favours coverage across clusters
and the cheapest tests, never eloquence. The clusterer is blind to which card wrote what.

A sketch: {"id", "idea", "mechanism", "prediction", "test", "card", "operator", "seed", "call_id"}
A cluster: {"cluster_id", "name", "members": [ids], "cards": [distinct cards], "n": int,
            "representative": sketch id, "selected": bool, "rank": int}
"""
from __future__ import annotations

import json
import re
from collections import defaultdict

# ---------------------------------------------------------------- profile access (shared by the prompt modules)
# Every problem-specific word in the prompts of ideate, deepen, research, critic_check, tune, controls, predict,
# diagnose and anomaly comes from the active profile (docs/GENERIC_SPEC.md section 2). Templates carry {v:key}
# placeholders and are rendered by fill() at call time, never at import time, so switching profiles needs no
# reload. A key the profile does not define falls back to LLM_DEFAULT_VOCAB when the profile is the language-model
# one, else to GENERIC_DEFAULT_VOCAB. {v:key|upper} renders the word in capitals.

LLM_DEFAULT_VOCAB: dict = {
    # section 2 of the spec
    "artifact": "training script",
    "artifact_file": "train.py",
    "language": "python",
    "run": "training run",
    "score_phrase": "lower validation loss at the fixed budget",
    "score_name": "validation loss",
    "parts": "parts of the recipe",
    "recipe": "recipe",
    "cheap_test": "a 1-minute smoke run comparison, a 3-step timing, a parameter count",
    "cost_axes": "the step time, the parameter count, peak memory",
    "first_check": "the first learning check (45 matched steps)",
    "targets": ["loss on rare tokens", "loss at late positions", "attention entropy in deep layers", "residual RMS growth",
                "gradient norm spread", "max attention logit", "first-token attention mass", "recall-token loss",
                "update-norm spread", "validation loss only"],
    "scope_default": "validation loss at 1024",
    "levers": "optimizer, schedule, init, normalisation, attention pattern, embeddings, data order, loss, precision, systems",
    "known_tricks": "",
    "boundary_all": "everything except evaluate() and the data loader",
    # keys Agent A added for tree.py and loop.py that these prompts reuse
    "artifact_short": "script",
    "narrow_examples": "fewer layers, one token class, one phase of training",
    # keys added by the prompt modules (Agent B)
    "observables": "the loss curve, the step time, the parameter count",
    "scope_other": "long context, inference cost, routing balance, robustness",
    "tune_examples": "a learning rate, warmup, decay, clipping, an init scale, a head count",
    "viable": "trainable",
    "win_short": "lowers the loss at this budget",
    "score_short": "the loss",
    "leap_rules": ("what a loss is, what a layer computes, which tokens see which, how an update is made, what is fixed "
                   "across layers or phases, what is shared and what is separate"),
    "field": "machine learning",
    "probe": "a five-minute probe on a saved checkpoint",
    "weak_points": "the positions, the token classes, the layers, the phase of training",
    "adapt_moves": ("the way the public speedrun record adapts ports: zero-initialise the new path so step 0 is the baseline, "
                    "apply it to the last k layers only, use fewer channels, share it across layers, add a learned gate with "
                    "read-out, change where it plugs in"),
    "separations": "by training phase, by layer, by token class, by condition",
    "cheap_words": ["smoke", "1-minute", "one-minute", "60", "3-step", "three step", "step time", "param",
                    "count", "build", "timing", "memory", "vram", "matched"],
    "cost_questions": "compute, memory and step time, parameters and initialisation",
    "full_run": "trained for the full budget",
    "ladder_metrics": "param_ratio, step_ratio, learn_z, long_z, trend, fidelity",
    "sources": "arXiv, lab blogs, the modded-nanoGPT speedrun record log, benchmark write-ups",
    "size_word": "model size",
    "setting_words": ("attention layer layers model loss train training learning learn embedding embeddings token tokens "
                      "block blocks head heads weight weights param params parameter parameters matrix linear "
                      "transformer network nanogpt gpt modded speedrun"),
    "setup": "this exact setup (21M params, 50M tokens)",
    "delta_name": "val_loss",
    "same_change_example": "a different gate on the same tensor is new",
    "problem_brief": ("a small language-model training recipe (a GPT-2-style model with 21M non-embedding parameters trained "
                      "on 50M tokens on one laptop GPU; the measure is validation loss at a fixed token budget)"),
    "measured_numbers": "loss, perplexity, speed, scale",
    # leap operators: an input bundle plus an output schema, never an instruction to be bold
    # (research_notes/creative_genius/00_SYNTHESIS.md, D2). Contexts of the same part get different operators.
    "leap_operators": {
        "rulebreak": "list eight rules of this part as testable sentences (equal weight on every token; every layer computes the same thing; one schedule; one update rule per tensor; the same context for every token; fixed shapes); rank them by how much of the recipe depends on each; drop or invert exactly one and say what must change so training still runs; the leap is that change.",
        "subtract": "for each component of this part write what happens if it is removed or frozen at identity or zero, and what the measurements say it buys; keep the two removals you can defend; reinvest the freed parameters, steps or memory in one named alternative; the leap is a removal plus its reinvestment.",
        "literalize": "find a place where the brief, the findings or the script's comments say one thing behaves like or is analogous to another; set the two sides equal as an identity of named quantities; derive one consequence the source did not state; the leap is the code change that tests that consequence.",
        "remeasure": "list the constants this part inherited from another scale or another recipe (learning-rate rule, warmup, init scale, clipping, softcap, rotary base, head count); pick two; derive or infer from the measurements what the value should be at this size; the leap replaces the inherited value by the derived one or by a learned or scheduled version.",
        "rerepresent": "rewrite what this part does in a different form (the optimiser as descent under a norm; attention as a kernel smoother over positions; the residual stream as a differential equation across depth; the loss as a code length); name one edit that is natural in that form and awkward in the code's own; the leap is that edit, translated back into the script.",
        "limit": "push one quantity of this part to its limit (context of one token, depth one, vocabulary of two, learning rate zero, infinite width, one head); say what breaks first and which measured cell would show it; if the baseline already shows that symptom, the leap is the fix the limit case suggests.",
        "import": "keep the recipe unchanged and add one mechanism from a field far from language modelling (control, ecology, signal processing, economics, immunology) aimed at a measurement that is stuck or unexplained; write the shared structure first (their objects to ours, their relation to ours), then the instantiation and where the correspondence breaks; the leap is the instantiation.",
        "existence": "the recipe has measured headroom against its rules (parameters below the cap, step time below the cap, memory below the card); assume a change exists that recovers a third of the gap between this recipe and a recipe twice its size at no more than two percent extra step time; give three mechanisms that could be it and, for each, what would have to be true at the first learning check; the leaps are those mechanisms.",
    },
}

# Used for a key a non-language-model profile does not define: plain words that fit any artifact with a score.
GENERIC_DEFAULT_VOCAB: dict = {
    "artifact": "program", "artifact_file": "the program file", "language": "python", "run": "run",
    "score_phrase": "improve the score", "score_name": "score", "parts": "parts of the method", "recipe": "method",
    "cheap_test": "a quick run on a few small cases, a timing, a size count",
    "cost_axes": "the run time, the memory, the size", "first_check": "the first quick check",
    "targets": ["score only"], "scope_default": "the score on the test set",
    "levers": "the main rule, the state kept, the thresholds, the order of work, the tie-breaks, the data used",
    "known_tricks": "", "boundary_all": "everything except the scoring code",
    "artifact_short": "program", "narrow_examples": "fewer cases, one class of input, one stage of the run",
    "observables": "the score, the run time, the cost",
    "scope_other": "other inputs, the cost at use time, robustness",
    "tune_examples": "a threshold, a weight, a limit, a size",
    "viable": "runnable", "win_short": "improves the score", "score_short": "the score",
    "leap_rules": ("what the score rewards, what each step computes, what each decision may see, what is fixed across "
                   "stages, what is shared and what is separate"),
    "field": "its home field",
    "probe": "a five-minute probe on a saved run",
    "weak_points": "the cases, the input classes, the stages of the run",
    "adapt_moves": ("the way good ports are adapted: start the new path switched off so the first step is the baseline, "
                    "apply it to a subset of cases only, make it smaller, share it across stages, add a tuned switch "
                    "with a read-out, change where it plugs in"),
    "separations": "by stage, by input class, by case, by condition",
    "cheap_words": ["quick", "small", "few", "minute", "timing", "count", "build", "cheap", "fast", "matched"],
    "cost_questions": "compute, memory and run time, settings and starting state",
    "full_run": "run on the full test",
    "ladder_metrics": "cost_ratio, learn_z, long_z, trend",
    "sources": "papers, technical blogs, benchmark write-ups, code repositories",
    "size_word": "problem size",
    "setting_words": "",
    "setup": "this exact setup",
    "delta_name": "score",
    "same_change_example": "a different rule at the same decision point is new",
    "problem_brief": "",                      # empty: built from the profile's artifact and score at call time
    "measured_numbers": "score, speed, scale",
    "leap_operators": {
        "rulebreak": "list eight rules of this part as testable sentences (what is treated equally, what is the same at every stage, what is fixed, what each decision may see, what is shared); rank them by how much of the {v:recipe} depends on each; drop or invert exactly one and say what must change so the {v:artifact} still runs; the leap is that change.",
        "subtract": "for each component of this part write what happens if it is removed or frozen, and what the measurements say it buys; keep the two removals you can defend; reinvest the freed time, memory or complexity in one named alternative; the leap is a removal plus its reinvestment.",
        "literalize": "find a place where the brief, the findings or the {v:artifact_short}'s comments say one thing behaves like or is analogous to another; set the two sides equal as an identity of named quantities; derive one consequence the source did not state; the leap is the code change that tests that consequence.",
        "remeasure": "list the constants this part inherited from another scale or another setting ({v:tune_examples}); pick two; derive or infer from the measurements what the value should be here; the leap replaces the inherited value by the derived one or by an adaptive version.",
        "rerepresent": "rewrite what this part does in a different form (as an optimisation problem, as a probability model, as a control loop, as a code length); name one edit that is natural in that form and awkward in the code's own; the leap is that edit, translated back into the {v:artifact_short}.",
        "limit": "push one quantity of this part to its limit (zero, one, infinite, the largest input, the smallest input); say what breaks first and which measured quantity would show it; if the baseline already shows that symptom, the leap is the fix the limit case suggests.",
        "import": "keep the {v:recipe} unchanged and add one mechanism from a field far from {v:field} (control, ecology, signal processing, economics, immunology) aimed at a measurement that is stuck or unexplained; write the shared structure first (their objects to ours, their relation to ours), then the instantiation and where the correspondence breaks; the leap is the instantiation.",
        "existence": "the {v:recipe} has measured headroom against its rules (cost below the cap, time below the cap); assume a change exists that recovers a third of the gap between this {v:recipe} and a much stronger one at no more than two percent extra cost; give three mechanisms that could be it and, for each, what would have to be true at {v:first_check}; the leaps are those mechanisms.",
    },
}

try:
    from nano import profile as PF
except ImportError:                                   # nano/profile.py not there yet: a shim with the same calls
    class _ShimProfile:
        name = "llm"
        vocab = LLM_DEFAULT_VOCAB
        score = {"name": "validation loss", "direction": "lower", "unit": "nats", "margin": 0.005, "alpha": 0.01, "min_seeds": 3}
        lower_is_better = True
        constraints: list = []
        diagnostics = ""
        checker = "llm"
        boundary_all = LLM_DEFAULT_VOCAB["boundary_all"]
        artifact = {"path": "nano/train.py"}

        def v(self, key: str, default=""):
            return LLM_DEFAULT_VOCAB.get(key, default)

    class _ShimPF:
        _p = _ShimProfile()

        @staticmethod
        def current():
            return _ShimPF._p

        @staticmethod
        def fill(text: str) -> str:
            return re.sub(r"\{v:([a-z_]+)\}", lambda m: _as_text(LLM_DEFAULT_VOCAB.get(m.group(1), m.group(0))), text)
    PF = _ShimPF


def _as_text(val) -> str:
    if isinstance(val, (list, tuple, set)):
        return ", ".join(str(x) for x in val)
    return "" if val is None else str(val)


def is_llm(p=None) -> bool:
    p = p if p is not None else PF.current()
    return getattr(p, "name", "llm") == "llm"


def vword(key: str, default=None):
    """The profile's word for key (a str, or the list/dict the profile stores), with the fallbacks above."""
    p = PF.current()
    voc = getattr(p, "vocab", None)
    if isinstance(voc, dict) and key in voc and voc[key] is not None:
        return voc[key]
    if key == "score_name":
        nm = (getattr(p, "score", None) or {}).get("name")
        if nm:
            return nm
    if key == "boundary_all" and getattr(p, "boundary_all", None):
        return p.boundary_all
    if is_llm(p) and key in LLM_DEFAULT_VOCAB:
        return LLM_DEFAULT_VOCAB[key]
    if default is not None:
        return default
    if key in GENERIC_DEFAULT_VOCAB:
        return GENERIC_DEFAULT_VOCAB[key]
    try:
        return p.v(key, "")
    except Exception:  # noqa: BLE001
        return ""


def lower_is_better() -> bool:
    p = PF.current()
    v = getattr(p, "lower_is_better", None)
    if isinstance(v, bool):
        return v
    return str((getattr(p, "score", None) or {}).get("direction", "lower")).lower() != "higher"


def has_diagnostics() -> bool:
    """True when the profile measures diagnostic cells (the LLM checker does it in its baseline profile)."""
    p = PF.current()
    return bool(getattr(p, "diagnostics", "")) or getattr(p, "checker", "") == "llm" or is_llm(p)


def targets_choice() -> str:
    """The TARGET choice line: the measured cells and the score-only option."""
    t = vword("targets")
    items = [str(x) for x in t] if isinstance(t, (list, tuple)) else [s.strip() for s in str(t or "").split(",") if s.strip()]
    only = [x for x in items if x.lower().endswith(" only")]
    cells = [x for x in items if x not in only]
    last = only[0] if only else f"{_as_text(vword('score_name'))} only"
    if cells:
        return f"one of the diagnostic cells ({', '.join(cells)}) or \"{last}\""
    return f"\"{last}\""


def problem_brief() -> str:
    b = _as_text(vword("problem_brief"))
    if b:
        return b
    return f"a {_as_text(vword('artifact'))} (the measure is {_as_text(vword('score_name'))})"


_PH = re.compile(r"\{v:([a-z_]+)(\|upper)?\}")
_DERIVED = {"targets_choice": targets_choice, "problem_brief": problem_brief}


def fill(text: str, escape_braces: bool = False) -> str:
    """Render {v:key} placeholders from the active profile. escape_braces doubles braces in the inserted words,
    for a template that is .format()-ed afterwards."""
    def rep(m):
        key = m.group(1)
        s = _DERIVED[key]() if key in _DERIVED else _as_text(vword(key))
        if m.group(2):
            s = s.upper()
        return s.replace("{", "{{").replace("}", "}}") if escape_braces else s
    return _PH.sub(rep, text or "")


def leap_operators() -> dict:
    """The profile's leap operators (name -> text), rendered."""
    ops = vword("leap_operators")
    if not isinstance(ops, dict) or not ops:
        ops = LLM_DEFAULT_VOCAB["leap_operators"] if is_llm() else GENERIC_DEFAULT_VOCAB["leap_operators"]
    return {k: fill(str(v)) for k, v in ops.items()}


def cheap_words() -> tuple:
    w = vword("cheap_words")
    if isinstance(w, str):
        w = [x.strip() for x in w.split(",") if x.strip()]
    return tuple(str(x).lower() for x in (w or ()))


# ---------------------------------------------------------------- templates ({v:key} placeholders, rendered on access)
_SKETCH_FORMAT = """List 5 to 8 distinct idea sketches. Do not write code. Use exactly this form for each:

IDEA: <short name>
MECHANISM: <one or two sentences: what changes and why it should {v:score_phrase}>
PREDICTION: <the observable effect: on {v:observables}>
TEST: <the cheapest check that would falsify it, for example {v:cheap_test}>
SOURCE: <"own" if the idea is yours, else the URL of the paper, post or repo it comes from or builds on>
TARGET: <the measured quantity this should move and in which direction: {v:targets_choice}>
SCOPE: <"{v:scope_default}" if the benefit should show in this exam; otherwise what it is really about ({v:scope_other})>
KIND: <"port" for a known technique adapted to this {v:recipe} (SOURCE must then name where it comes from); "tune" for a change of one or two existing constants only ({v:tune_examples}), with the reason in MECHANISM and the range worth sweeping in TEST; or "leap" for an idea that drops or flips a rule the {v:recipe} takes for granted>
BREAKS: <leaps only: the rule of the {v:recipe} this idea drops or flips, as one testable sentence>
KEEPS: <leaps only: the conventional core left intact, so the change stays {v:viable} and comparable>
P_SUCCESS: <leaps only: your own chance that it {v:win_short}, a number at most 0.2>
KILL: <leaps only: the number at {v:first_check} that discards it>

Separate sketches with a blank line. Vary the part of the system each sketch touches."""

_WEB_ADDENDUM = """Use web search and fetch as much as it takes to check what has already been tried for this part and to look for mechanisms from neighbouring fields that were never applied here. Search is for grounding and departure, not for copying: an idea that is a known technique must say so in SOURCE, and at least half of your sketches must be ones you did not find on the web.

"""

_WEB_DELEGATED_ADDENDUM = """A research assistant will search the web for the questions you ask (you will see its findings before you write the sketches). Use them for grounding and departure, not for copying: an idea that is a known technique must say so in SOURCE, and at least half of your sketches must be ones the findings did not contain.

"""

_LEAP_ADDENDUM = """AMBITIOUS IDEAS, A QUOTA BY CONSTRUCTION: at least {n} of your sketches must be leaps (KIND: leap). A leap drops or flips one rule the current {v:recipe} takes for granted ({v:leap_rules}), keeps the rest of the {v:recipe} as it is, and might well fail. It is judged by whether its mechanism is specific and its test can kill it, never by how bold it sounds. A known technique applied unchanged is a port, not a leap, and is reclassified when found. Before writing your leaps, list twelve one-line seeds that each break a different rule, keep the three farthest from what the brief, the findings and the other seeds already contain, and write only those in full. Put the seed list under a line reading "PASS 1 (scratch):"; everything from the first IDEA: block on is what counts.

YOUR LEAP OPERATOR FOR THIS CONTEXT ({op_name}): {op_text}

"""

_ANALOGY_ADDENDUM = """The analogues above come from other fields. For EACH sketch, transfer the STRUCTURE of one analogue, not its
vocabulary: add a line MAPPING: <their X -> our Y; their mechanism -> this concrete change in the {v:artifact_short}>. A sketch
without a mapping does not count. Prefer analogues whose field is far from {v:field}.

"""

_ANOMALY_ADDENDUM = """ANOMALIES IN THE MEASUREMENTS (each replicated on several seeds and filtered; a cell that sits off the trend of the rest of its family):
{text}

For at least two of your sketches start from one of these rows: restate it in one sentence, name three rival causes including an artifact of the measurement, name {v:probe} that would separate them, and sketch the change that follows if the least popular rival is true. Say in TARGET which cell the sketch is meant to move.

"""

_OWNER_ADDENDUM = """THE OWNER'S SEED, a mechanism the owner wants explored for this part:
{text}

Treat it as an imported mechanism: write its shared structure first (what plays which role here), then at least three sketches that instantiate it in different ways, each saying where the correspondence breaks; the remaining sketches may depart from it. SOURCE for these is "owner".

"""

_DIAGNOSIS_ADDENDUM = """The measurements above are how the baseline actually behaves. Start from the weakest point they show
({v:weak_points}) and sketch changes that target it; say in
MECHANISM which measurement each sketch is meant to move, and in PREDICTION by how much.

"""

_STAGED_ADDENDUM = """Work in three passes inside this reply, then give only the final sketches:
Pass 1 (private): list 20 one-line seeds, each touching a different lever ({v:levers}). Pass 2 (private): rewrite each seed to be bolder
and more different from the others; drop any two that are the same change in different words. Pass 3: choose 6 to 8
and write them in the sketch form below. Mark the private passes PASS 1 and PASS 2 so the script can strip them.

"""

_ADAPT_ADDENDUM = """The techniques above are KNOWN to help elsewhere. Do not propose them as they are: propose an ADAPTED variant for this
{v:artifact_short}, {v:adapt_moves}.
Add a line ADAPTATION: <the move you applied and why it fits this scale>. A sketch without an ADAPTATION line is a copy.

"""

_EXCLUSION_ADDENDUM = """These idea families are ALREADY COVERED this run (do not propose them or their variants):
{names}
Propose ideas outside these categories, wild and unconventional ones included, as long as each has a mechanism and a test.

"""

_CONTRADICTION_ADDENDUM = """A MEASURED TRADE-OFF from this run: {text}
Propose sketches that keep the gain and remove the cost, by separating them: {v:separations}.
Say in MECHANISM which separation you use.

"""

_MAPPING_FORMAT = """For EACH sketch add a typed mapping block (one line each, in this order):
MAPPING: objects: <their X -> our Y; their Z -> our W (mapped by function, not by name)> | relations: <at least 3 source relations
and their target counterparts, one of them higher-order (causes, prevents, trades off)> | inference: <the one source relation with
no target counterpart yet: that is the proposed change> | break: <where the analogy fails>
A sketch whose MAPPING has fewer than two "->" object pairs or no "break" is dropped by the script.

"""

# public name -> (raw template, .format()-ed by the caller afterwards)
TEMPLATES = {
    "SKETCH_FORMAT": (_SKETCH_FORMAT, False), "WEB_ADDENDUM": (_WEB_ADDENDUM, False),
    "WEB_DELEGATED_ADDENDUM": (_WEB_DELEGATED_ADDENDUM, False), "LEAP_ADDENDUM": (_LEAP_ADDENDUM, True),
    "ANALOGY_ADDENDUM": (_ANALOGY_ADDENDUM, False), "ANOMALY_ADDENDUM": (_ANOMALY_ADDENDUM, True),
    "OWNER_ADDENDUM": (_OWNER_ADDENDUM, True), "DIAGNOSIS_ADDENDUM": (_DIAGNOSIS_ADDENDUM, False),
    "STAGED_ADDENDUM": (_STAGED_ADDENDUM, False), "ADAPT_ADDENDUM": (_ADAPT_ADDENDUM, False),
    "EXCLUSION_ADDENDUM": (_EXCLUSION_ADDENDUM, True), "CONTRADICTION_ADDENDUM": (_CONTRADICTION_ADDENDUM, True),
    "MAPPING_FORMAT": (_MAPPING_FORMAT, False),
}


def render(name: str) -> str:
    """A template rendered for the active profile (what ideate.<NAME> returns)."""
    raw, esc = TEMPLATES[name]
    return fill(raw, escape_braces=esc)


def __getattr__(name: str):
    """ideate.SKETCH_FORMAT, ideate.LEAP_OPERATORS ... are rendered for the active profile on every access, so
    callers keep using them as module constants while the words follow the profile."""
    if name in TEMPLATES:
        return render(name)
    if name == "LEAP_OPERATORS":
        return leap_operators()
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


STOP = set("the a an of to in and or for with on at by is are be that this it as from into its their than "
           "more less each per while when so which then using use used than via over under one two".split())


def strip_private_passes(text: str) -> str:
    """Remove the PASS 1 / PASS 2 scratch of a staged reply; keep from the first IDEA: block on."""
    m = re.search(r"^(?:SLOT:[^\n]*\n)?IDEA:", text or "", flags=re.M)
    return text[m.start():] if m else (text or "")


def mapping_ok(mapping: str) -> bool:
    return mapping.count("->") >= 2 and "break" in mapping.lower()


def parse_sketches(text: str, *, card: str, operator: str, seed: str, call_id: str, idgen) -> list[dict]:
    out = []
    score_name = _as_text(vword("score_name")).lower()
    text = strip_private_passes(text)
    blocks = re.split(r"\n\s*\n", text.strip())
    for b in blocks:
        f = {}
        for key in ("IDEA", "MECHANISM", "PREDICTION", "TEST", "SOURCE", "MAPPING", "TARGET", "SCOPE", "ADAPTATION", "PART",
                    "KIND", "BREAKS", "KEEPS", "P_SUCCESS", "KILL", "SLOT"):
            m = re.search(rf"{key}:\s*(.+?)(?=\n[A-Z_]+:|\Z)", b, flags=re.S)
            if m:
                f[key.lower()] = " ".join(m.group(1).split())
        if "idea" in f and "mechanism" in f:
            if card == "analogy" and not mapping_ok(f.get("mapping", "")):
                continue                                    # a decorative analogy: no typed mapping, no sketch
            out.append({"id": idgen(), "idea": f["idea"][:120], "mechanism": f["mechanism"][:600],
                        "prediction": f.get("prediction", "")[:300], "test": f.get("test", "")[:300],
                        "source": f.get("source", "own")[:300], "mapping": f.get("mapping", "")[:600],
                        "target": f.get("target", "")[:200], "scope": f.get("scope", "")[:120], "adaptation": f.get("adaptation", "")[:200],
                        "part": f.get("part", "")[:60], "slot": f.get("slot", "").split()[0].lower()[:12] if f.get("slot") else "",
                        "kind": _kind(f.get("kind", "")), "breaks": f.get("breaks", "")[:300], "keeps": f.get("keeps", "")[:200],
                        "p_success": _prob(f.get("p_success", "")), "kill": f.get("kill", "")[:200],
                        "metric_blind": bool(f.get("scope")) and score_name not in f.get("scope", "").lower(),
                        "card": card, "operator": operator, "seed": seed, "call_id": call_id})
    return out


def _kind(s: str) -> str:
    """"leap" or "port" when the sketch says so, else ""."""
    t = (s or "").strip().lower()
    return "leap" if t.startswith("leap") else ("port" if t.startswith("port") else ("tune" if t.startswith("tun") else ""))


def _prob(s: str):
    m = re.search(r"\d*\.?\d+", s or "")
    if not m:
        return None
    try:
        v = float(m.group(0))
    except ValueError:
        return None
    return v / 100.0 if v > 1.0 else v


def deal_by_part(specs: list, k: int, prio, part) -> list:
    """Cap a list of ideation contexts to k by dealing round-robin across parts: every part's best context
    (lowest prio) first, then every part's second, and so on, so a small test cap still covers all the parts
    instead of spending itself on the first parts in tree order. Owner seeds (prio below 0) are never cut."""
    ranked = sorted(specs, key=prio)                     # stable: the builder's order within a priority
    seen: dict = {}
    keyed = []
    for sp in ranked:
        p = part(sp)
        seen[p] = seen.get(p, 0) + 1
        keyed.append((seen[p], prio(sp), sp))
    keyed.sort(key=lambda t: (t[0], t[1]))
    keep = [sp for _, _, sp in keyed[:k]]
    keep += [sp for sp in specs if prio(sp) < 0 and sp not in keep]
    return keep


def draw_lane(cands: list[dict], k: int, rng, leap_min: int | None = None) -> list[dict]:
    """The long-shot lane: k clusters drawn at random, weighted by exp(score), from the eligible list, with
    at least leap_min of them (default: half of k, rounded up) drawn from leap clusters when enough exist.
    Ambitious ideas are protected in building as well as in writing; they are never forced on the main slots."""
    import math as _math
    cands = list(cands)
    if k <= 0 or not cands:
        return []
    leap_min = _math.ceil(k / 2) if leap_min is None else leap_min
    picks: list[dict] = []

    def _draw(pool):
        weights = [_math.exp(min(10.0, float(c.get("score") or 0.0))) for c in pool]
        r = rng.random() * sum(weights)
        acc = 0.0
        for c, w in zip(pool, weights):
            acc += w
            if acc >= r:
                return c
        return pool[-1]
    leaps = [c for c in cands if float(c.get("leap_share") or 0) >= 0.5]
    while leaps and len(picks) < min(leap_min, k):
        c = _draw(leaps)
        picks.append(c)
        leaps.remove(c)
        cands.remove(c)
    while cands and len(picks) < k:
        c = _draw(cands)
        picks.append(c)
        cands.remove(c)
    return picks


def _tokens(s: str) -> set[str]:
    return {w for w in re.findall(r"[a-z][a-z0-9_-]{2,}", s.lower()) if w not in STOP}


def lexical_clusters(sketches: list[dict], threshold: float = 0.35) -> list[list[str]]:
    """Fallback clustering: union-find over Jaccard similarity of idea + mechanism words."""
    ids = [s["id"] for s in sketches]
    toks = {s["id"]: _tokens(s["idea"] + " " + s["mechanism"]) for s in sketches}
    parent = {i: i for i in ids}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            ta, tb = toks[a], toks[b]
            if not ta or not tb:
                continue
            j = len(ta & tb) / len(ta | tb)
            if j >= threshold:
                parent[find(a)] = find(b)
    groups = defaultdict(list)
    for i in ids:
        groups[find(i)].append(i)
    return list(groups.values())


def cluster_prompt(sketches: list[dict]) -> str:
    """Blind clustering request: ids and text only, no cards, seeds or call ids."""
    lines = [f"[{s['id']}] {s['idea']}: {s['mechanism']}" for s in sketches]
    return ("Group the following idea sketches into clusters of the SAME underlying idea (same mechanism, "
            "even if worded differently). Different parameter choices of one mechanism belong together; "
            "different mechanisms stay apart. Return ONLY a JSON array of objects "
            '{"name": "<short cluster name>", "members": ["<id>", ...]}, every id in exactly one cluster.\n\n'
            + "\n".join(lines))


def parse_cluster_json(text: str, valid_ids: set[str]) -> list[dict] | None:
    m = re.search(r"\[.*\]", text, flags=re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    seen, out = set(), []
    for c in arr:
        if not isinstance(c, dict) or not isinstance(c.get("members"), list):
            continue
        mem = [i for i in (c.get("members") or []) if i in valid_ids and i not in seen]
        if not mem:
            continue
        seen.update(mem)
        out.append({"name": str(c.get("name", ""))[:80], "members": mem})
    missing = valid_ids - seen
    for i in missing:                               # anything the model dropped becomes its own cluster
        out.append({"name": "", "members": [i]})
    return out


def cheapness(sketch: dict) -> int:
    txt = (sketch.get("test", "") + " " + sketch.get("prediction", "")).lower()
    return min(3, sum(1 for w in cheap_words() if w in txt))


def angles(members: list[str], by_id: dict[str, dict]) -> set[str]:
    """Distinct ways in that produced a cluster: the card, or for interrogation offshoots the idea
    they were born from, so two interrogations arriving at one idea count as two angles."""
    out = set()
    for i in members:
        s = by_id.get(i, {})
        out.add(f"deepen:{s.get('parent_cluster')}" if s.get("card") == "deepen" else s.get("card", "?"))
    return out


def build_clusters(groups: list[dict], sketches: list[dict]) -> list[dict]:
    by_id = {s["id"]: s for s in sketches}
    clusters = []
    for k, g in enumerate(groups):
        members = g["members"]
        cards = sorted({by_id[i]["card"] for i in members})
        # representative: the cheapest falsifying test, then the first written; never the longest text
        rep = max(members, key=lambda i: (cheapness(by_id[i]), -members.index(i)))
        n_leap = sum(1 for i in members if by_id[i].get("kind") == "leap")
        clusters.append({"cluster_id": f"k{k:02d}", "name": g.get("name") or by_id[rep]["idea"],
                         "members": members, "cards": cards, "n": len(members), "representative": rep,
                         "n_angles": len(angles(members, by_id)), "selected": False, "rank": None,
                         "leap_share": round(n_leap / max(1, len(members)), 2),
                         "leap_ops": sorted({by_id[i].get("leap_op", "") for i in members if by_id[i].get("kind") == "leap"} - {""})})
    return clusters


# the LLM profile's cheap-test words (vocab "cheap_words"); cheapness() reads the active profile's list
CHEAP_TEST_WORDS = ("smoke", "1-minute", "one-minute", "60", "3-step", "three step", "step time", "param",
                    "count", "build", "timing", "memory", "vram", "matched")

# Selection weights (settable from the loop). Coverage across angles stays the strongest signal,
# novelty against the research brief and the private defaults comes next; a documented failure is
# a strong penalty; departure cards and cheap tests are tie-breakers; size counts slightly against.
# Evidence (research_notes/idea_generation/00_SYNTHESIS.md, C5, X1): gains come mostly from adapted known
# techniques and recombination; novelty is protected in a long-shot lane, not rewarded on the main line.
# These are priors until nano/calibrate.py has ~100 builds; then --weights-from-ledger replaces them.
WEIGHTS = {"angle": 1.0, "new": 0.25, "known": 0.0, "failed": -2.0, "obvious": -0.75,
           "departure": 0.5, "cheap": 0.25, "size": -0.05, "metric_blind": -1.0}
DEPARTURE_CARDS = ("transform", "docs", "low_prior", "research", "deepen", "analogy", "diagnosis", "adapt", "contradiction", "owner")


def cluster_score(c: dict, by_id: dict[str, dict], w: dict | None = None) -> float:
    w = {**WEIGHTS, **(w or {})}
    rep = by_id.get(c["representative"], {})
    n_angles = c.get("n_angles") or len(angles(c["members"], by_id))
    departure = 1 if any(x in c["cards"] for x in DEPARTURE_CARDS) else 0
    prior = c.get("prior", "unknown")
    blind = 1 if rep.get("metric_blind") else 0
    return (w["angle"] * (n_angles - 1) + w.get(prior, 0.0) + w["obvious"] * (1 if c.get("obvious") else 0)
            + w["departure"] * departure + w["cheap"] * cheapness(rep) / 3 + w["size"] * c["n"] + w.get("metric_blind", 0.0) * blind)


def select_clusters(clusters: list[dict], k: int, exclude: set[str] | None = None,
                    sketches: list[dict] | None = None, weights: dict | None = None) -> list[dict]:
    """Rank clusters by cluster_score (a weighted sum, not a strict priority order, so a new idea
    from one angle can beat an old idea from two) and select the top k. Eloquence never counts
    (EVL-16); size alone is convergence, not evidence (EVL-08, SOC-07)."""
    by_id = {s["id"]: s for s in (sketches or [])}
    exclude = exclude or set()
    pool = [c for c in clusters if c["cluster_id"] not in exclude]
    for c in pool:
        c["score"] = round(cluster_score(c, by_id, weights), 3)
    ranked = sorted(pool, key=lambda c: (-c["score"], c["cluster_id"]))
    for r, c in enumerate(ranked):
        c["rank"] = r
    chosen = ranked[:k]
    for c in chosen:
        c["selected"] = True
    return chosen


def implement_brief(cluster: dict, sketches: list[dict], knowledge: str = "") -> str:
    by_id = {s["id"]: s for s in sketches}
    rep = by_id[cluster["representative"]]
    others = [by_id[i] for i in cluster["members"] if i != rep["id"]][:3]
    txt = (f"IDEA: {rep['idea']}\nMECHANISM: {rep['mechanism']}\nPREDICTION: {rep['prediction']}\n"
           f"TEST: {rep['test']}")
    if rep.get("target"):
        txt += f"\nTARGET: {rep['target']}"
    if rep.get("mapping"):
        txt += f"\nMAPPING: {rep['mapping']}"
    if rep.get("adaptation"):
        txt += f"\nADAPTATION: {rep['adaptation']}"
    if rep.get("kind") == "leap":
        txt += f"\nKIND: leap (an ambitious idea: build it faithfully, do not water it down into a known technique)"
        for k, label in (("breaks", "BREAKS"), ("keeps", "KEEPS"), ("kill", "KILL")):
            if rep.get(k):
                txt += f"\n{label}: {rep[k]}"
    if others:
        txt += "\nVARIANTS OF THE SAME IDEA FROM OTHER CONTEXTS (choose the version you judge most likely to work):\n"
        txt += "\n".join(f"- {o['idea']}: {o['mechanism']}" for o in others)
    if knowledge:
        txt += "\n\n" + knowledge
    return txt


# ---------------------------------------------------------------- cross-part duplicate merge
def merge_prompt(clusters: list[dict], sketches_by_id: dict) -> str:
    rows = []
    for c in clusters:
        rep = sketches_by_id.get(c["representative"], {})
        rows.append(f"[{c['cluster_id']}] ({c.get('node')}/{c.get('direction')}) {c['name']}: {rep.get('mechanism', '')[:220]}")
    return (fill("These idea clusters were grouped separately per part of a {v:artifact}. Some describe the SAME ")
            + "change filed under different parts. Return ONLY a JSON array of arrays, each inner array listing the "
            "ids of clusters that are the same change (mechanism, not topic). Leave out clusters that have no twin.\n\n"
            + "\n".join(rows))


def parse_merge(text: str, valid_ids: set[str]) -> list[list[str]]:
    m = re.search(r"\[.*\]", text or "", flags=re.S)
    if not m:
        return []
    try:
        arr = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return []
    out, seen = [], set()
    for g in arr:
        if not isinstance(g, list):
            continue
        ids = [str(i) for i in g if str(i) in valid_ids and str(i) not in seen]
        if len(ids) >= 2:
            seen.update(ids)
            out.append(ids)
    return out


def merge_clusters(clusters: list[dict], groups: list[list[str]], sketches: list[dict]) -> list[dict]:
    """Union each group into its first cluster (keeps that cluster's part and direction); the others
    are dropped and remembered in merged_from."""
    by_cid = {c["cluster_id"]: c for c in clusters}
    by_id = {s["id"]: s for s in sketches}
    drop = set()
    for g in groups:
        head = by_cid[g[0]]
        for cid in g[1:]:
            other = by_cid[cid]
            head["members"] = head["members"] + [m for m in other["members"] if m not in head["members"]]
            head.setdefault("merged_from", []).append({"cluster_id": cid, "node": other.get("node"), "name": other.get("name")})
            drop.add(cid)
        head["cards"] = sorted({by_id[i]["card"] for i in head["members"] if i in by_id})
        head["n"] = len(head["members"])
        head["n_angles"] = len(angles(head["members"], by_id))
    return [c for c in clusters if c["cluster_id"] not in drop]


def parse_defaults(text: str) -> list[str]:
    """The private 'first five changes that come to mind', one per line."""
    out = []
    for l in (text or "").splitlines():
        l = re.sub(r"^\s*\d+[.)]\s*", "", l).strip()
        if l:
            out.append(l[:120])
    return out[:8]
