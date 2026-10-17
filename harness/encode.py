"""/encode at P0 (ARCHITECTURE.md section 3 /encode steps 1-3, 5, 6; Pr5, Pr14).

Two fresh encode calls each write goal, facts, resources, a hard-constraint checklist and a
domain-noun list from the key-stripped item; a script merges the checklists and a third call
resolves them only when they differ by more than half. A separate defaults call writes
private/defaults.json, which no generator ever receives. A script writes the views
(canonical, shuffled, low_prior) to variants/. Files: problem.md, constraints.json,
private/defaults.json, private/noun_map.json, variants/*.md, encode.json.
"""
from __future__ import annotations

import random
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import config, lint
from .schemas import option_letter, strip_key, write_json


@dataclass
class Problem:
    item_id: str
    benchmark: str
    goal: str
    facts: list[str]
    resources: list[str]
    checklist: list[str]
    bar: dict
    views: dict[str, str]
    problem_md: str
    encode_tokens: int
    item: dict                      # key-stripped item (train pairs / question + choices)
    meta: dict = field(default_factory=dict)   # shuffled_perm, low_prior parts, encode log


GOAL_DEFAULT = {
    "arc": "Find the rule that maps each example input grid to its output grid and apply it to the test input grid.",
    "bt": "Choose the option (A, B, C or D) that answers the question.",
}
BASE_CONSTRAINT = {
    "arc": "The rule must reproduce every example output grid exactly from its input grid.",
    "bt": "The answer must be exactly one of the options A, B, C or D.",
}
REQUIRED_VERIFICATION = {"arc": "demo_match", "bt": "agreement"}
ARC_COLORS = ["black", "blue", "red", "green", "yellow", "gray", "grey", "magenta", "pink",
              "orange", "cyan", "azure", "brown", "maroon", "purple", "teal"]
# words the item renderer and the view schema use; never treated as domain nouns
RESERVED = {"example", "input", "output", "test", "question", "options", "option", "data",
            "facts", "fact", "goal", "resources", "resource", "constraints", "constraint",
            "answer", "problem", "entities", "none", "listed"}
STOPWORDS = {
    "the", "and", "for", "are", "but", "not", "you", "your", "with", "this", "that", "they",
    "them", "their", "there", "what", "when", "where", "which", "who", "whom", "why", "how",
    "have", "has", "had", "was", "were", "will", "would", "could", "should", "can", "does",
    "did", "doing", "done", "from", "into", "onto", "over", "under", "than", "then", "also",
    "only", "just", "very", "much", "many", "more", "most", "some", "any", "all", "each",
    "every", "both", "few", "other", "such", "same", "own", "about", "after", "before",
    "again", "once", "here", "being", "been", "because", "while", "since", "until", "without",
    "within", "upon", "these", "those", "his", "her", "hers", "him", "its", "she", "our",
    "ours", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
    "make", "made", "get", "got", "give", "gave", "take", "took", "come", "came", "goes",
    "went", "know", "knew", "said", "says", "even", "still", "though", "although", "like",
    "out", "off", "down", "away", "back", "way", "yet", "able",
}
_HEADER = re.compile(r"^\s*(?:#+\s*)?\**\s*(GOAL|FACTS|RESOURCES|CHECKLIST|NOUNS)\s*\**\s*:?\s*\**\s*(.*)$",
                     re.IGNORECASE)
_ITEM = re.compile(r"^\s*(?:\d{1,3}[.)]|[-*])\s+(.*)$")


# ---------------------------------------------------------------- item rendering
def grid_compact(g) -> str:
    """One row per line, one digit per cell (cells are ints 0-9)."""
    return "\n".join("".join(str(int(c)) for c in row) for row in g)


def grid_python(g) -> str:
    return "[" + ", ".join("[" + ", ".join(str(int(c)) for c in row) + "]" for row in g) + "]"


def grid_spaced(g) -> str:
    """Rows of space-separated digits, as the plain arm shows them."""
    return "\n".join(" ".join(str(c) for c in row) for row in g)


def raw_view() -> bool:
    """The run's effective raw_view flag (config.flags(): env HTSA_RAW_VIEW or think --flag;
    recorded in the run header and every call record): no decomposition, every view is the raw
    item with spaced grids and no X-renaming, so low_prior is the raw item too."""
    return bool(config.flags().get("raw_view"))


def render_item(item: dict, style: str = "compact") -> str:
    """Key-stripped item as plain text from explicit fields only (section 3 /encode step 2)."""
    item = strip_key(item)
    if item.get("benchmark") == "arc":
        fmt = grid_python if style == "python" else (grid_spaced if style == "spaced" else grid_compact)
        sep = " = " if style == "python" else ":\n"
        parts = []
        for i, pair in enumerate(item.get("train", []), 1):
            parts.append(f"Example {i} input{sep}{fmt(pair['input'])}")
            parts.append(f"Example {i} output{sep}{fmt(pair['output'])}")
        parts.append(f"Test input{sep}{fmt(item['test_input'])}")
        return "\n\n".join(parts)
    lines = [f"Question: {str(item.get('question', '')).strip()}", "Options:"]
    lines += [f"{option_letter(i)}. {str(c).strip()}" for i, c in enumerate(item.get("choices", []))]
    return "\n".join(lines)


# ---------------------------------------------------------------- parsing encode replies
def numbered(text: str) -> list[str]:
    """Items of a numbered or bulleted list; continuation lines join the open item."""
    items: list[str] = []
    for line in (text or "").splitlines():
        m = _ITEM.match(line)
        if m:
            items.append(m.group(1).strip())
        elif items and line.strip():
            items[-1] = (items[-1] + " " + line.strip()).strip()
    return [i for i in items if i]


def split_sections(text: str) -> dict[str, str]:
    """Header -> body for the GOAL / FACTS / RESOURCES / CHECKLIST / NOUNS sections."""
    out: dict[str, list[str]] = {}
    cur = None
    for line in (text or "").splitlines():
        m = _HEADER.match(line)
        if m:
            cur = m.group(1).upper()
            out[cur] = [m.group(2)] if m.group(2).strip() else []
        elif cur:
            out[cur].append(line)
    return {k: "\n".join(v).strip() for k, v in out.items()}


def _noun_list(body: str) -> list[str]:
    raw = numbered(body) or [ln for ln in body.splitlines() if ln.strip()]
    words = []
    for chunk in raw:
        for w in chunk.split(","):
            w = re.sub(r"[^A-Za-z \-]", "", w).strip().lower()
            if w:
                words.append(w)
    return words


def parse_encode(text: str) -> dict:
    """{goal, facts, resources, checklist, nouns} from one encode reply (step 1)."""
    s = split_sections(text)
    goal = " ".join((s.get("GOAL") or "").split())
    return {"goal": goal, "facts": numbered(s.get("FACTS", "")),
            "resources": numbered(s.get("RESOURCES", "")),
            "checklist": numbered(s.get("CHECKLIST", "")), "nouns": _noun_list(s.get("NOUNS", ""))}


# ---------------------------------------------------------------- checklist merge (script)
def norm_item(s: str) -> str:
    return " ".join(re.sub(r"[^a-z0-9 ]", " ", (s or "").lower()).split())


def _same(a: str, b: str, thr: float = 0.7) -> bool:
    na, nb = norm_item(a), norm_item(b)
    if na == nb:
        return True
    ta, tb = set(na.split()), set(nb.split())
    return bool(ta and tb) and len(ta & tb) / len(ta | tb) >= thr


def merge_checklists(a: list[str], b: list[str]) -> tuple[list[str], float]:
    """Normalize, union, keep order (A first); disagreement = 1 - shared / union (step 1)."""
    merged: list[str] = []
    for x in list(a) + list(b):
        if norm_item(x) and not any(_same(x, y) for y in merged):
            merged.append(x.strip())
    if not merged:
        return [], 0.0
    shared = sum(1 for m in merged if any(_same(m, x) for x in a) and any(_same(m, x) for x in b))
    return merged, 1.0 - shared / len(merged)


def with_base(items: list[str], benchmark: str) -> list[str]:
    """Prepend the benchmark's fixed hard constraint unless an equivalent item exists."""
    base = BASE_CONSTRAINT[benchmark]
    out = [i for i in items if norm_item(i)]
    return out if any(_same(base, i) for i in out) else [base] + out


def numbered_block(items: list[str], empty: str = "(none listed)") -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(items, 1)) if items else empty


# ---------------------------------------------------------------- views (step 5)
def shuffled_perm_id(item_id: str, replicate: int, arm: str = "scaffold") -> int:
    """Permutation id for this replicate's shuffled view (README determinism rule)."""
    return random.Random(f"{item_id}:{arm}:{replicate}:perm").randint(1, 999999)


def perm_order(item_id: str, perm: int, n: int, replicate: int = 0, arm: str = "scaffold") -> list[int]:
    """Fact order for a permutation id; 0 is the canonical order. Every other id is seeded by
    the replicate as well (README Determinism: the replicate seeds every permutation), so the
    same perm id gives a different order in another replicate (REP-08)."""
    order = list(range(n))
    if perm:
        random.Random(f"{item_id}:{arm}:{replicate}:perm:{perm}").shuffle(order)
    return order


def view_parts(problem: Problem, variant: str = "canonical", perm: int = 0,
               data_style: str = "compact") -> dict[str, str]:
    """Routed text blocks {facts, resources, goal, constraints} for one view (step 5).
    facts carries the item data then the numbered facts in view order."""
    if raw_view():
        return {"facts": "Data:\n" + render_item(problem.item, "spaced"), "resources": "", "goal": problem.goal,
                "constraints": numbered_block(problem.checklist)}
    if variant == "low_prior":
        lp = problem.meta["low_prior"]
        goal, facts, res, chk = lp["goal"], lp["facts"], lp["resources"], lp["checklist"]
        data = lp["data_python"] if data_style == "python" else lp["data_compact"]
        head = f"Entities: {', '.join(lp['tokens'])}\n\n" if lp.get("tokens") else ""
    else:
        goal, facts, res, chk = problem.goal, problem.facts, problem.resources, problem.checklist
        data = render_item(problem.item, data_style)
        head = ""
    replicate = int((problem.meta or {}).get("replicate", 0))
    facts = [facts[i] for i in perm_order(problem.item_id, perm, len(facts), replicate)]
    block = f"{head}Data:\n{data}\n\nFacts:\n{numbered_block(facts)}"
    return {"facts": block, "resources": numbered_block(res), "goal": goal,
            "constraints": numbered_block(chk)}


def view_text(parts: dict[str, str]) -> str:
    """A view as markdown with goal and constraints last (REP-08)."""
    return (f"## Data and facts\n{parts['facts']}\n\n## Resources\n{parts['resources']}\n\n"
            f"## Goal\n{parts['goal']}\n\n## Hard constraints\n{parts['constraints']}\n")


def domain_nouns(parsed: list[dict], item: dict) -> list[str]:
    """Per-item domain-noun list from the original item: the encode NOUNS sections, ARC colour
    names, and for BT a content-word fallback from the question and every option when the
    encode calls list none (REP-02)."""
    nouns = [n for p in parsed for n in p.get("nouns", [])]
    if item.get("benchmark") == "arc":
        nouns += ARC_COLORS
    elif not nouns:
        text = " ".join([str(item.get("question", ""))] + [str(c) for c in item.get("choices", [])])
        nouns = [w.lower() for w in re.findall(r"[A-Za-z]{4,}", text)]
    out: list[str] = []
    for n in nouns:
        n = n.strip().lower()
        if len(n) >= 3 and n not in STOPWORDS and n not in RESERVED and n not in out:
            out.append(n)
    return out


def neutralize(text: str, noun_map: dict[str, str]) -> str:
    """Replace each domain noun (every surface form: regular and irregular plurals) with its
    neutral token, longest first. lint.lint_domain checks the result with its own matcher."""
    for noun in sorted(noun_map, key=len, reverse=True):
        text = lint.noun_regex(noun).sub(noun_map[noun], text)
    return text


def build_low_prior(problem: Problem, nouns: list[str]) -> tuple[dict, dict[str, str]]:
    """Low_prior parts from the fixed schema with nouns replaced by X1, X2, ... (Pr5)."""
    noun_map = {n: f"X{i}" for i, n in enumerate(nouns, 1)}

    def f(s: str) -> str:
        return neutralize(s, noun_map)

    item = dict(problem.item)
    if item.get("benchmark") == "bt":
        item["question"] = f(str(item.get("question", "")))
        item["choices"] = [f(str(c)) for c in item.get("choices", [])]
    lp = {"goal": f(problem.goal), "facts": [f(x) for x in problem.facts],
          "resources": [f(x) for x in problem.resources], "checklist": [f(x) for x in problem.checklist],
          "data_compact": render_item(item, "compact"), "data_python": render_item(item, "python")}
    if item.get("benchmark") == "arc":
        lp["data_compact"], lp["data_python"] = f(lp["data_compact"]), f(lp["data_python"])
    seen = " ".join([lp["goal"], lp["data_compact"]] + lp["facts"] + lp["resources"] + lp["checklist"])
    lp["tokens"] = [t for t in noun_map.values() if re.search(rf"\b{t}\b", seen)]
    return lp, noun_map


# ---------------------------------------------------------------- problem.md
def problem_markdown(p: Problem) -> str:
    """problem.md: goal, numbered facts, numbered resources, checklist, solve bar (steps 1-2).
    The item data is not repeated here; prompts render it from the stripped item. The item id
    is not written either: public benchmark ids are recall cues, and problem.md reaches the
    judge and probe prompts."""
    bar = p.bar
    return (f"# Problem\n\n## Goal\n{p.goal}\n\n## Facts\n{numbered_block(p.facts)}\n\n"
            f"## Resources\n{numbered_block(p.resources)}\n\n## Hard constraints\n"
            f"{numbered_block(p.checklist)}\n\n## Solve bar\nrequired verification: "
            f"{bar['required_verification']}; all checklist items must hold: {str(bar['all_items']).lower()}\n")


# ---------------------------------------------------------------- the encode step
def parse_defaults(text: str, benchmark: str) -> list[str]:
    """5 first answers (step 3): ARC rule sentences, BT option letters."""
    items = numbered(text)
    if benchmark == "bt":
        letters = [m.group(1) for m in (re.match(r"^\W*([A-D])\b", i) for i in items) if m]
        return letters[:5]
    return items[:5]


def encode(item: dict, run_dir: Path, *, backend: str, replicate: int, log_dir: Path) -> Problem:
    """Section 3 /encode at P0. Writes problem.md, constraints.json, private/defaults.json,
    private/noun_map.json, variants/{canonical,shuffled,low_prior}.md and encode.json.
    Step 6 cap: cap = encode_cap_mult x max_tokens["plain"] (2 x 16000 = 32000 tokens at the
    defaults). This is a fixed proxy, not 2x a measured plain CoT call. It is consulted only
    before the optional resolve call, which is skipped once encode tokens reach the cap; the
    two checklist calls and the defaults call always run, whatever they cost."""
    from . import run_card as rc   # lazy: run_card imports this module
    s = strip_key(item)
    b, run_dir = s["benchmark"], Path(run_dir)
    problem_text = render_item(s, "compact")
    cap = int(config.PARAMS["encode_cap_mult"] * config.PARAMS["max_tokens"]["plain"])
    log = {"call_ids": [], "encode_tokens": 0, "cap": cap, "cap_hit": False, "resolved": False}

    def _call(template: str, values: dict, role: str, purpose: str) -> str:
        res = rc.dispatch(template, values, role=role, run_dir=run_dir, log_dir=log_dir,
                          backend=backend, meta={"benchmark": b, "item_id": s["id"], "purpose": purpose})
        log["call_ids"].append(res.call_id)
        log["encode_tokens"] += res.usage.total_tokens
        return res.text

    if raw_view():                                 # decomposition off: no encode or defaults calls
        bar = {"required_verification": REQUIRED_VERIFICATION[b], "all_items": True}
        checklist = with_base([], b)
        write_json(run_dir / "constraints.json", {"checklist": checklist, "bar": bar})
        write_json(run_dir / "private" / "defaults.json", {"benchmark": b, "answers": [], "call_id": None})
        p = Problem(item_id=s["id"], benchmark=b, goal=GOAL_DEFAULT[b], facts=[], resources=[], checklist=checklist,
                    bar=bar, views={}, problem_md="", encode_tokens=0, item=s)
        p.meta["replicate"] = int(replicate)
        _write_views(p, run_dir, replicate, [])
        p.problem_md = problem_markdown(p)
        (run_dir / "problem.md").write_text(p.problem_md, encoding="utf-8")
        p.meta["encode"] = log
        write_json(run_dir / "encode.json", {**log, "raw_view": True, "shuffled_perm": p.meta["shuffled_perm"]})
        return p
    pa = parse_encode(_call("encode", {"problem": problem_text}, "encode", "encode_a"))
    pb = parse_encode(_call("encode", {"problem": problem_text}, "encode", "encode_b"))
    merged, log["disagreement"] = merge_checklists(pa["checklist"], pb["checklist"])
    if log["disagreement"] > 0.5:
        if log["encode_tokens"] >= cap:
            log["cap_hit"] = True
        else:
            resolved = numbered(_call("encode.resolve", {"problem": problem_text,
                                      "checklist_a": numbered_block(pa["checklist"]),
                                      "checklist_b": numbered_block(pb["checklist"])}, "encode", "resolve"))
            if resolved:
                merged, _ = merge_checklists(resolved, [])
                log["resolved"] = True
    bar = {"required_verification": REQUIRED_VERIFICATION[b], "all_items": True}
    checklist = with_base(merged, b)
    write_json(run_dir / "constraints.json", {"checklist": checklist, "bar": bar})
    defaults_text = _call(f"defaults.{b}", {"problem": problem_text}, "defaults", "defaults")
    write_json(run_dir / "private" / "defaults.json",
               {"benchmark": b, "answers": parse_defaults(defaults_text, b), "call_id": log["call_ids"][-1]})
    p = Problem(item_id=s["id"], benchmark=b, goal=pa["goal"] or pb["goal"] or GOAL_DEFAULT[b],
                facts=pa["facts"] or pb["facts"], resources=pa["resources"] or pb["resources"],
                checklist=checklist, bar=bar, views={}, problem_md="",
                encode_tokens=log["encode_tokens"], item=s)
    p.meta["replicate"] = int(replicate)
    _write_views(p, run_dir, replicate, domain_nouns([pa, pb], s))
    p.problem_md = problem_markdown(p)
    (run_dir / "problem.md").write_text(p.problem_md, encoding="utf-8")
    p.meta["encode"] = log
    write_json(run_dir / "encode.json", {**log, "raw_view": False, "shuffled_perm": p.meta["shuffled_perm"],
                                         "low_prior_lint": p.meta["low_prior_lint"]})
    return p


def _write_views(p: Problem, run_dir: Path, replicate: int, nouns: list[str]) -> None:
    """Step 5: canonical, shuffled (perm id logged) and linted low_prior views in variants/."""
    perm = shuffled_perm_id(p.item_id, replicate)
    lp, noun_map = build_low_prior(p, nouns)
    p.meta.update(shuffled_perm=perm, low_prior=lp, n_domain_nouns=len(nouns), domain_nouns=list(nouns))
    p.views = {"canonical": view_text(view_parts(p, "canonical", 0)),
               "shuffled": view_text(view_parts(p, "canonical", perm)),
               "low_prior": view_text(view_parts(p, "low_prior", 0))}
    p.meta["low_prior_lint"] = lint.lint_domain(p.views["low_prior"], nouns)
    write_json(run_dir / "private" / "noun_map.json", noun_map)
    for name, text in p.views.items():
        path = run_dir / "variants" / f"{name}.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
