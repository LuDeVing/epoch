"""The second profile: an online bin-packing rule (docs/GENERIC_SPEC.md section 4).

Deliberately far from language models. The artifact is nano/profiles/binpack/baseline.py, which defines
choose_bin(item, bins, capacity) -> int (first fit). The harness's scorer (nano/profiles/binpack/scorer.py,
never shown to the candidate) packs seeded instances of uniform (0, 1] items into bins of capacity 1.0 and
reports the mean of bins used / ceil(total size); lower is better. Checked by nano/checks/script.py.

Note: nano/profiles/binpack/ must not get an __init__.py, or it would shadow this module on import.
"""
from __future__ import annotations

_FILE = "baseline.py"

OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: what you change in the packing rule and why it should use fewer bins on the benchmark instances>
CHANGE: <one line naming the functions touched or added>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be built within the rules, say why (then return the file unchanged)>
```python
<the COMPLETE modified baseline.py, every line, ready to run>
```
Keep everything not related to your change identical to the given file."""

_BOUNDARY_ALL = "choose_bin and any new helper functions or module-level constants in baseline.py"

TREE = [
    {"id": "root", "name": "use fewer bins on the benchmark instances", "parent": None,
     "frame": "An online packing rule places each arriving item, once and for good, into an open bin or a new bin; "
              "it is judged by the bins used relative to the total size, averaged over seeded instances.",
     "assumptions": ["items must be placed the moment they arrive", "a placed item never moves",
                     "the rule sees only the current item and the current bin fills"],
     "boundary": "everything", "directions": ["upward"]},
    {"id": "choice", "name": "choice rule", "parent": "root",
     "frame": "First fit: scan the open bins in the order they were opened and take the first one with room.",
     "assumptions": ["the first bin with room is as good as any other", "bins are scanned in opening order",
                     "the choice looks only at whether the item fits, not at the room left after it"],
     "boundary": "choose_bin (the selection among bins that fit)", "directions": ["inward", "outward"]},
    {"id": "state", "name": "bin state kept", "parent": "root",
     "frame": "The rule keeps nothing between calls; it sees the list of current fills and nothing else, so every "
              "decision is made from scratch.",
     "assumptions": ["a fill level is all that matters about a bin", "nothing needs remembering between items",
                     "all open bins are equally available"],
     "boundary": "choose_bin, new module-level state and helper functions", "directions": ["inward", "outward"]},
    {"id": "open", "name": "when to open a bin", "parent": "root",
     "frame": "A new bin is opened only when the item fits in no open bin.",
     "assumptions": ["opening a bin is always worse than using one with room", "the decision to open depends only on fit",
                     "an item never gets a bin of its own on purpose"],
     "boundary": "choose_bin (the condition for returning -1)", "directions": ["inward", "outward"]},
    {"id": "stats", "name": "use of item statistics", "parent": "root",
     "frame": "The rule ignores the history of item sizes; it treats every item the same whatever came before.",
     "assumptions": ["the size distribution is unknown and stays unknown", "past items say nothing about future items",
                     "large and small items need no different treatment"],
     "boundary": "choose_bin, new module-level counters of item sizes, helper functions", "directions": ["inward", "outward"]},
    {"id": "ties", "name": "tie-breaking", "parent": "root",
     "frame": "When several bins would serve, the earliest opened wins; no secondary criterion exists.",
     "assumptions": ["ties are rare enough not to matter", "opening order is a fair tie-breaker",
                     "near-equal fits are treated as different"],
     "boundary": "choose_bin (the ordering among candidate bins)", "directions": ["inward", "outward"]},
    {"id": "recipe", "name": "the whole rule (cross-part changes)", "parent": "root",
     "frame": "The parts above are changed one at a time; a rule that changes the choice and the opening together, "
              "or keeps state to steer both, has no single owner.",
     "assumptions": ["each part can be improved on its own", "the parts interact only through the bin fills",
                     "the best rule is a sum of the best parts"],
     "boundary": _BOUNDARY_ALL, "directions": ["inward", "outward"]},
]

PROFILE = {
    "name": "binpack",
    "goal": ("Improve an online bin-packing rule. Items of size in (0, 1] arrive one at a time and must each be placed "
             "at once into an open bin of capacity 1.0 or into a new bin; nothing moves afterwards. The rule is the "
             "function choose_bin(item, bins, capacity) in baseline.py, which returns the index of an open bin or -1 "
             "for a new one; the baseline is first fit. Success is a lower mean ratio of bins used to the lower bound "
             "(the total size rounded up), measured by the harness on seeded benchmark instances (quick: 20 instances "
             "of 200 items; full: 100 instances of 1000 items), with a margin and a sequential test over seeds, at no "
             "more than twice the baseline's time per item."),
    "aim": ("Learn whether a research loop built for language models can find real improvements on a problem it was "
            "not built for, judged by the same kind of objective check."),
    "score": {"name": "bins used over the lower bound", "direction": "lower", "unit": "ratio", "margin": 0.002,
              "alpha": 0.01, "min_seeds": 3},
    "vocab": {
        "artifact": "packing rule", "artifact_file": _FILE, "language": "python",
        "run": "scoring run", "score_phrase": "use fewer bins per instance on the benchmark",
        "parts": "parts of the packing rule", "recipe": "packing heuristic",
        "cheap_test": "a quick score on 20 small instances",
        "cost_axes": "the time per item",
        "first_check": "the quick score (20 instances of 200 items, same seed as the baseline)",
        "targets": ["bins used on instances with many small items", "bins used on instances with many large items",
                    "wasted space in the last bins opened", "bins left nearly empty", "packing ratio only"],
        "scope_default": "bins used over the lower bound on the full benchmark",
        "levers": "choice rule, bin state, opening rule, item statistics, tie-breaking",
        "known_tricks": ("Classic online rules: next fit, first fit, best fit, worst fit, almost-worst fit, harmonic "
                         "classes (items grouped by size class), refined first fit, and rules that reserve room for "
                         "items expected later."),
        "boundary_all": _BOUNDARY_ALL,
        # keys the prompt modules use (nano/ideate.py GENERIC_DEFAULT_VOCAB); packing words where the default reads wrong
        "artifact_short": "rule",
        "narrow_examples": "small items only, one phase of an instance, the bins opened last",
        "field": "combinatorial optimisation",
        "observables": "the packing ratio, the number of bins, the fill of the bins at the end, the time per item",
        "scope_other": "other item-size distributions, adversarial item orders, offline packing, the time per item",
        "tune_examples": "a fill threshold, a size class boundary, a slack tolerance, a reserve for large items",
        "viable": "a valid packing rule",
        "win_short": "uses fewer bins per instance",
        "score_short": "the packing ratio",
        "leap_rules": ("which bin an item may go to, what the rule remembers, when a bin is opened, whether item sizes "
                       "are treated alike, how ties are broken, whether all open bins are equal"),
        "probe": "a quick per-instance breakdown of where the bins are wasted",
        "weak_points": "small items, large items, items just over half a bin, the start and the end of an instance",
        "adapt_moves": ("the way good ports are adapted: make the new rule fall back to first fit so the start is the "
                        "baseline, apply it to one size class only, add a tuned threshold with a read-out, change the "
                        "point in the choice where it acts"),
        "separations": "by item size class, by phase of the instance, by how full the bins are",
        "cheap_words": ["quick", "20 instances", "small instances", "few instances", "timing", "time per item", "build",
                        "cheap", "fast", "matched", "same seed"],
        "cost_questions": "time per item, memory kept between items, how many bins are scanned per item",
        "full_run": "scored on the full benchmark (100 instances of 1000 items)",
        "ladder_metrics": "cost_ratio, learn_z, long_z, trend",
        "sources": "papers on online bin packing, algorithm textbooks, competitive-analysis surveys, code repositories",
        "size_word": "instance size",
        "setting_words": ("bin bins packing pack item items capacity fill fit first best worst next harmonic online "
                          "offline heuristic rule instance instances"),
        "setup": "this exact setup (items uniform in (0, 1], capacity 1.0, 1000 items per instance)",
        "delta_name": "packing ratio",
        "same_change_example": "a different threshold on the same choice is new",
        "problem_brief": ("an online bin-packing rule (choose_bin places each arriving item in an open bin or a new one; "
                          "items uniform in (0, 1], capacity 1.0; the measure is the mean of bins used over the total size "
                          "rounded up, lower is better)"),
        "measured_numbers": "packing ratio, bins used, time per item, instance size",
        "leap_operators": {
            "rulebreak": "list eight rules of this part as testable sentences (every item is treated alike; any bin with room is acceptable; a bin is opened only when nothing fits; nothing is remembered between items; all open bins are equal; ties go to the oldest bin); rank them by how much of the rule depends on each; drop or invert exactly one and say what must change so the packing stays valid; the leap is that change.",
            "subtract": "for each component of this part write what happens if it is removed or fixed (no scan order, no fit test beyond validity, no new bin until forced) and what the measurements say it buys; keep the two removals you can defend; reinvest the freed time per item in one named alternative; the leap is a removal plus its reinvestment.",
            "literalize": "find a place where the brief, the findings or the rule's comments say one thing behaves like or is analogous to another (a bin as a container, a gap as a slot, items as a stream); set the two sides equal as an identity of named quantities; derive one consequence the source did not state; the leap is the code change that tests that consequence.",
            "remeasure": "list the constants this part inherited from textbook rules (the fit tolerance, a size class boundary at one half or one third, a reserve fraction, the scan order); pick two; derive from the measured item sizes and bin fills what the value should be here; the leap replaces the inherited value by the derived one or by one that adapts to the items seen so far.",
            "rerepresent": "rewrite what this part does in a different form (the bin fills as a histogram of gaps; the choice as an assignment cost; the instance as a random walk of total size; the rule as a policy in a Markov decision process); name one edit that is natural in that form and awkward in the code's own; the leap is that edit, translated back into the rule.",
            "limit": "push one quantity of this part to its limit (all items tiny, all items just over half, one open bin, infinitely many bins, items sorted ascending or descending); say what breaks first and which measured quantity would show it; if the baseline already shows that symptom, the leap is the fix the limit case suggests.",
            "import": "keep the rule unchanged and add one mechanism from a field far from combinatorial optimisation (control, ecology, signal processing, economics, immunology) aimed at a measurement that is stuck or unexplained, such as gaps that are never filled; write the shared structure first (their objects to ours, their relation to ours), then the instantiation and where the correspondence breaks; the leap is the instantiation.",
            "existence": "first fit has measured headroom (the time per item is far below the 2x cap, and the packing ratio is above 1.0); assume a change exists that recovers a third of the gap between first fit and the lower bound at no more than two percent extra time per item; give three mechanisms that could be it and, for each, what would have to be true at the quick score; the leaps are those mechanisms.",
        },
    },
    "constraints": [
        "C1. Same artifact interface: baseline.py keeps choose_bin(item, bins, capacity) -> int, returning the index of an "
        "open bin the item fits in or -1 to open a new bin; it must not change the bins list it is given.",
        "C2. Same benchmark: the harness's scorer generates the instances from fixed seeds and computes the score; the "
        "scorer is never visible to the rule, and the rule may not try to read it, its instances or its state.",
        "C3. Online: the rule sees one item at a time and the current bin fills; nothing about future items.",
        "C4. Time per item at most 2x the baseline's, measured by the harness on the same instances.",
        "C5. Standard library only; socket, urllib, http, subprocess, ctypes, multiprocessing, importlib, pickle and "
        "shutil are denied, and so are introspection and files (sys, os, inspect, gc, open, exec, eval); no network; no "
        "subprocesses. The process runs under a tripwire that fails the candidate on any of these.",
        "C6. The metric is the mean of bins used over the lower bound on the full benchmark; a change counts only if it "
        "beats the baseline by more than 0.002 with the sequential test at alpha 0.01 over at least 3 seeds.",
    ],
    "assumptions": [
        "the first bin with room is as good as any other",
        "a bin's fill level is all that matters about it",
        "nothing needs remembering between items",
        "a new bin is opened only when nothing else fits",
        "past item sizes say nothing about future ones",
        "the earliest opened bin should win a tie",
        "every item gets the same treatment whatever its size",
        "the rule must decide from the fills alone, without classes of bins",
    ],
    "tree": TREE,
    "lenses": {
        "parts": "the parts of the packing rule: choice rule, bin state kept, when to open a bin, use of item statistics, "
                 "tie-breaking",
        "dataflow": "the path of one item: it arrives, the rule reads the fills, filters the bins it fits, ranks them, "
                    "chooses or opens, and the fill changes for every later item",
        "dynamics": "phases of an instance: the first items when few bins are open, the bulk, the end when many bins "
                    "are nearly full; what wastes space in each phase",
        "bottlenecks": "where space is wasted: bins left with gaps no later item fits, large items opening bins alone, "
                       "small items spread thin, time spent scanning many bins",
        "failures": "the ways an online rule fails: adversarial orders, many items just over half a bin, a run of small "
                    "items followed by large ones, gaps that are never filled",
    },
    "boundary_all": _BOUNDARY_ALL,
    "artifact": {"path": "nano/profiles/binpack/baseline.py", "output_format": OUTPUT_FORMAT,
                 "entry": "choose_bin(item, bins, capacity)"},
    "checker": "script",
    "checker_args": {
        "scorer": "python nano/profiles/binpack/scorer.py --candidate {candidate} --out {out} --level {level} --seed {seed}",
        "seeds": [0, 1, 2],
        "wall_cap": 120,
    },
    "docs": {},
    "diagnostics": "",
}
