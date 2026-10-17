"""A profile written from what a person typed on the page (space/launch.py, "your own problem").

The person gives a title, the goal in plain words, what a good answer looks like, what is known, what must stay
fixed, and optionally the parts. This builds a no-check profile (docs/GENERIC_SPEC.md section 6, Mode 3): candidates
are written proposals, a blind panel judges them on the criteria the person gave, the mapper draws the parts from
the goal when none were given. `write_profile(spec)` stores it as nano/profiles/custom_<slug>.py so the loop loads
it like any other profile (`--profile custom_<slug>`)."""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
_SLUG_RE = re.compile(r"[^a-z0-9]+")

OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: the claim of your proposal>
CHANGE: <one line naming the parts of the problem the proposal changes>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be written within the rules, say why>
```markdown
CLAIM:
<one or two sentences: what you propose and what it achieves>

FROM THE FACTS TO THE IDEA:
<the chain from what is known, cited by id like [F2] when a fact has one, to this proposal; one step per line>

FROM THE IDEA TO THE RESULT:
<the chain from the proposal to the outcome on each criterion; one step per line>

WEAK POINTS:
<where the proposal could fail, and what would show it>

PROPOSED TEST:
<a small, cheap test that would show whether the proposal works, and what result would refute it>
```
Write the whole proposal. Plain words, short sentences."""

DEFAULT_CRITERIA = [
    "Correctness: the proposal follows from what is known and does not contradict a stated fact or rule.",
    "Usefulness: if it works, it clearly serves the goal, not a side issue.",
    "Feasibility: it can be done with the means at hand, and the proposal says how.",
    "Clarity: a newcomer can understand it in two minutes and see why it should work.",
]


def slug(text: str, n: int = 24) -> str:
    s = _SLUG_RE.sub("_", str(text or "").strip().lower()).strip("_")[:n]
    return s or "problem"


def _lines(text) -> list[str]:
    out = []
    for raw in str(text or "").replace("\r", "").split("\n"):
        t = raw.strip().lstrip("-*0123456789.) ").strip()
        if t:
            out.append(t[:400])
    return out


def _parts(spec: dict) -> list[dict]:
    names = [p.strip() for p in str(spec.get("parts") or "").replace("\n", ",").split(",") if p.strip()]
    out = []
    seen = set()
    for name in names[:9]:
        pid = slug(name, 20)
        if pid in seen or pid == "root":
            continue
        seen.add(pid)
        out.append({"id": pid, "name": name[:60], "parent": "root", "frame": "", "assumptions": [],
                    "boundary": name[:60], "directions": ["inward", "outward"], "refines": pid})
    return out


def make_profile(spec: dict) -> dict:
    title = " ".join(str(spec.get("title") or "your problem").split())[:120]
    goal = " ".join(str(spec.get("goal") or "").split())[:4000] or title
    field = " ".join(str(spec.get("field") or "this problem's field").split())[:80]
    crit_lines = _lines(spec.get("success"))
    criteria = [c if ":" in c else f"{c.split()[0].capitalize() if c.split() else 'Goal'}: {c}" for c in crit_lines][:6] or DEFAULT_CRITERIA
    crit_names = ", ".join(c.split(":", 1)[0].strip().lower() for c in criteria)
    facts = [{"id": f"F{i + 1}", "node": "root", "text": t} for i, t in enumerate(_lines(spec.get("known"))[:40])]
    fixed = _lines(spec.get("fixed"))[:12]
    parts = _parts(spec)
    known_text = " ".join(f"[{f['id']}] {f['text']}" for f in facts)
    root = {"id": "root", "name": title, "parent": None,
            "frame": (goal[:600] + (" Known: " + known_text[:1200] if known_text else "")),
            "assumptions": [], "boundary": "everything", "directions": ["upward"], "refines": "root"}
    tree = [root] + parts
    boundary_all = f"the whole of {title}" + (": " + ", ".join(p["name"] for p in parts) if parts else "")
    constraints = ["C1. A proposal has the five sections CLAIM, FROM THE FACTS TO THE IDEA, FROM THE IDEA TO THE RESULT, "
                   "WEAK POINTS and PROPOSED TEST" + (", and cites at least one known fact by its id." if facts else
                                                      ", and states which facts it relies on and which are assumptions.")]
    constraints += [f"C{i + 2}. {t}" for i, t in enumerate(fixed)]
    constraints.append(f"C{len(constraints) + 1}. There is no objective score: proposals are ranked by a blind panel on "
                       f"{crit_names}, with people's opinions at a bounded weight.")
    interface = ("A proposal in markdown with exactly these five sections, in this order: CLAIM, FROM THE FACTS TO THE IDEA, "
                 "FROM THE IDEA TO THE RESULT, WEAK POINTS, PROPOSED TEST. It "
                 + ("cites at least one known fact by its id (for example [F1]). " if facts else "says what it relies on. ")
                 + f"It describes something that can be done for: {title}.")
    parts_phrase = ", ".join(p["name"] for p in parts) if parts else "the parts the map draws from the goal"
    vocab = {
        "artifact": "proposal", "artifact_file": "proposal.md", "language": "markdown",
        "run": "panel review", "score_phrase": f"a better answer on {crit_names}",
        "parts": f"parts of {title}", "recipe": "proposal",
        "cheap_test": "a small, cheap check that would show whether the proposal works",
        "cost_axes": "effort, time, money, risk",
        "first_check": "the blind panel's reading",
        "targets": [c.split(":", 1)[0].strip().lower() for c in criteria] + ["panel score only"],
        "scope_default": title,
        "levers": parts_phrase,
        "known_tricks": "Known practices of the field, adapted only when they fit this setting.",
        "boundary_all": boundary_all,
        "artifact_short": "proposal", "artifact_long": f"proposal for {title}",
        "goal_short": goal[:160],
        "system": "the problem", "narrow_examples": "one part, one case, one step",
        "planner_hint": "boundaries name the parts of the problem a proposal may change",
        "boundary_rules": "", "identity_rule": "",
        "reference_what": f"practices and results from {field}",
        "reference_use": "adapt a practice only if it fits this setting",
        "gain_phrase": "the panel score", "field": field,
        "observables": "what can be measured, counted or shown about the result",
        "scope_other": "other settings, larger or smaller cases, other fields",
        "tune_examples": "sizes, thresholds, counts, durations",
        "viable": "something that can actually be done here", "win_short": "is judged better by the panel",
        "score_short": "the panel score",
        "leap_rules": "what is assumed fixed, who does what, when things happen, what is measured, what is shown",
        "probe": "a quick small check",
        "weak_points": "the places where the facts are thin, where assumptions hide, where the proposal could fail",
        "adapt_moves": "try it small first, keep the old way as a fallback, make it shorter, add a check that shows whether it worked",
        "separations": "by part, by case, by time, by size",
        "cheap_words": ["small", "quick", "pilot", "cheap", "one case", "dry run"],
        "cost_questions": "effort, time, money, what could go wrong",
        "full_run": "used for real",
        "ladder_metrics": "panel_score, panel_sd, learn_z",
        "sources": f"studies, reports and guides from {field}",
        "size_word": "size",
        "setting_words": " ".join(sorted(set(re.findall(r"[a-z]{4,}", (title + " " + goal).lower())))[:40]),
        "setup": f"this exact setting: {title}",
        "delta_name": "panel score",
        "same_change_example": "a different mechanism for the same part is new",
        "problem_brief": f"{title}: {goal[:300]}",
        "measured_numbers": "whatever the facts and the test can count",
        "leap_operators": {
            "rulebreak": "list eight rules of this part as testable sentences; rank them by how much depends on each; drop or invert exactly one and say what must change so the whole still works; the leap is that change.",
            "subtract": "for each step of this part write what happens if it is removed, and what the facts say it buys; keep the two removals you can defend; reinvest what is freed in one named alternative; the leap is a removal plus its reinvestment.",
            "literalize": "find a place where the facts or the frame say one thing behaves like another; set the two sides equal; derive one consequence nobody stated; the leap is the change that tests it.",
            "remeasure": "list the numbers this part took over from habit; pick two; derive from the facts what the value should be here; the leap replaces the habit by the derived value.",
            "rerepresent": "describe this part in a different form (as a market, a tournament, a measurement with noise, a schedule); name one change that is natural in that form and awkward in the current one; the leap is that change, brought back.",
            "limit": "push one quantity of this part to its limit; say what breaks first and which fact would show it; the leap is the fix the limit case suggests.",
            "import": "keep the whole and add one mechanism from a far field aimed at a known weakness; write the shared structure first, then the instantiation and where the correspondence breaks; the leap is the instantiation.",
            "existence": "assume a proposal exists that does much better at no extra cost; give three mechanisms that could be it and, for each, what a small test would have to show; the leaps are those mechanisms.",
        },
    }
    lenses = {
        "parts": f"the parts of {title}: {parts_phrase}",
        "dataflow": f"the path of one case through {title}, from its start to its outcome",
        "dynamics": f"how {title} behaves over time: the start, the middle, the end, and what changes between them",
        "bottlenecks": f"where {title} loses the most: time, effort, accuracy, trust",
        "failures": f"the ways {title} fails: " + (", ".join(f["text"][:40] for f in facts[:4]) if facts else "the weak points named in the goal"),
    }
    return {
        "name": f"custom_{slug(title)}",
        "mode": "no_check",
        "title": title,
        "goal": goal + (" There is no objective score: each proposal is judged blind by a panel on " + crit_names + ", and people may add their opinions." if "panel" not in goal.lower() else ""),
        "aim": f"Find the best answer to: {title}.",
        "score": {"name": "panel score", "direction": "higher", "unit": "points of 10", "margin": 0.5, "alpha": 0.05, "min_seeds": 1},
        "facts": facts,
        "vocab": vocab,
        "constraints": constraints,
        "assumptions": [],
        "tree": tree,
        "lenses": lenses,
        "boundary_all": boundary_all,
        "artifact": {"path": None, "interface": interface, "skeleton": "nano/profiles/templates/proposal_skeleton.md",
                     "output_format": OUTPUT_FORMAT, "entry": "a markdown proposal"},
        "checker": "panel",
        "checker_args": {"criteria": criteria, "judges": 3, "people_weight": 0.25, "min_score": 4.0},
        "docs": {},
        "diagnostics": "",
    }


def write_profile(spec: dict) -> str:
    """Write nano/profiles/custom_<slug>.py from the spec and return the profile name."""
    prof = make_profile(spec)
    name = prof["name"]
    body = ('"""A problem typed on the page (space/launch.py): built by nano/profiles/_custom.py. Generated file."""\n'
            "from nano.profiles._custom import make_profile\n\n"
            f"SPEC = {json.dumps(spec, indent=1, ensure_ascii=False)}\n\n"
            "PROFILE = make_profile(SPEC)\n")
    (HERE / f"{name}.py").write_text(body, encoding="utf-8")
    return name
