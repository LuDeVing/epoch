"""Mode 2 test profile (docs/GENERIC_SPEC.md section 6): online bin packing with a scorer and no baseline.

Same problem and the same harness scorer as nano/profiles/binpack.py, but nothing is solved yet: artifact.path
is None, so the builders write a complete file from the interface and the skeleton
(nano/profiles/templates/binpack_skeleton.py). The first checked candidate becomes the reference; a later one
that beats it by the margin takes its place.
"""
from __future__ import annotations

import copy

from nano.profiles import binpack as _bp

INTERFACE = ("def choose_bin(item: float, bins: list[float], capacity: float) -> int\n"
             "  item: the size of the arriving item, in (0, capacity]\n"
             "  bins: the current fill of each open bin, in opening order (a copy)\n"
             "  returns: the index of an open bin the item fits in (bins[i] + item <= capacity), or -1 to open a new bin\n"
             "One Python file, standard library only. The harness imports it fresh for every instance and calls "
             "choose_bin once per item.")

OUTPUT_FORMAT = """Reply in exactly this form:
HYPOTHESIS: <one sentence: the packing rule you write and why it should use few bins on the benchmark instances>
CHANGE: <one line naming the functions and module-level state the file defines>
FIDELITY: <exact | partial | substituted | cannot, then one clause: exact = the idea as specified; partial = a piece left out, say which; substituted = a different mechanism with the same aim, say what; cannot = it could not be built within the rules, say why>
```python
<the COMPLETE file that implements choose_bin(item, bins, capacity) -> int, every line, ready to run>
```
There is no baseline file to keep identical: write the whole file from the interface and the skeleton."""

_BOUNDARY_ALL = "choose_bin and any helper functions or module-level state in the file"

_FRAMES = {
    "root": "Nothing is solved yet. A rule must place each arriving item, once and for good, into an open bin or a new "
            "bin; it is judged by the bins used relative to the total size, averaged over seeded instances.",
    "choice": "Which of the open bins with room the item goes to. No rule is chosen yet.",
    "state": "What the rule remembers between calls, beyond the bin fills it is given. Nothing is chosen yet.",
    "open": "When the rule opens a new bin instead of using one with room. Nothing is chosen yet.",
    "stats": "Whether the rule uses the sizes of the items seen so far. Nothing is chosen yet.",
    "ties": "How the rule decides between bins that serve equally well. Nothing is chosen yet.",
    "recipe": "Rules that decide the choice, the opening and the state together, as one design.",
}


def _tree() -> list[dict]:
    nodes = copy.deepcopy(_bp.TREE)
    for n in nodes:
        n["frame"] = _FRAMES.get(n["id"], n["frame"])
        if n["id"] == "recipe":
            n["boundary"] = _BOUNDARY_ALL
        elif n["id"] != "root":
            n["boundary"] = "the whole file (" + n["boundary"] + ")"
    return nodes


_vocab = copy.deepcopy(_bp.PROFILE["vocab"])
_vocab.update({
    "artifact": "packing rule file",
    "artifact_file": "choose_bin.py",
    "first_check": "the quick score (20 instances of 200 items, the same seed as the reference)",
    "boundary_all": _BOUNDARY_ALL,
    "artifact_short": "rule",
    "artifact_long": "online bin-packing rule written from scratch",
    "goal_short": "writing a packing rule that uses as few bins as possible",
})
_vocab["leap_operators"] = dict(_vocab["leap_operators"])
_vocab["leap_operators"]["existence"] = (
    "assume a rule exists that comes within a third of the gap between a simple rule and the lower bound at little "
    "extra time per item; give three mechanisms that could be it and, for each, what would have to be true at the quick "
    "score; the leaps are those mechanisms.")

PROFILE = {
    "name": "binpack_nobase",
    "mode": "check_only",
    "title": "write an online bin-packing rule from scratch",
    "goal": ("Write an online bin-packing rule. Items of size in (0, 1] arrive one at a time and must each be placed at "
             "once into an open bin of capacity 1.0 or into a new bin; nothing moves afterwards. There is no baseline: "
             "the rule is a new file that defines choose_bin(item, bins, capacity), returning the index of an open bin "
             "or -1 for a new one. Success is a low mean ratio of bins used to the lower bound (the total size rounded "
             "up), measured by the harness on seeded benchmark instances (quick: 20 instances of 200 items; full: 100 "
             "instances of 1000 items). The best checked rule so far is the reference; a new rule counts when it beats "
             "the reference by the margin."),
    "aim": ("Learn whether the research loop can work without a baseline: invent, check and rank solutions when only a "
            "scorer and an interface exist."),
    "score": dict(_bp.PROFILE["score"]),
    "vocab": _vocab,
    "constraints": [
        "C1. The file defines choose_bin(item, bins, capacity) -> int, returning the index of an open bin the item fits "
        "in or -1 to open a new bin; it must not change the bins list it is given.",
        "C2. Same benchmark: the harness's scorer generates the instances from fixed seeds and computes the score; the "
        "scorer is never visible to the rule, and the rule may not try to read it, its instances or its state.",
        "C3. Online: the rule sees one item at a time and the current bin fills; nothing about future items.",
        "C4. Time per item at most 5x the reference rule's, measured by the harness on the same instances.",
        "C5. Standard library only; socket, urllib, http, subprocess, ctypes, multiprocessing, importlib, pickle and "
        "shutil are denied, and so are introspection and files (sys, os, inspect, gc, open, exec, eval); no network; no "
        "subprocesses. The process runs under a tripwire that fails the candidate on any of these.",
        "C6. The metric is the mean of bins used over the lower bound on the full benchmark; a rule replaces the "
        "reference only if it beats it by more than 0.002.",
    ],
    "assumptions": list(_bp.PROFILE["assumptions"]),
    "tree": _tree(),
    "lenses": dict(_bp.PROFILE["lenses"]),
    "boundary_all": _BOUNDARY_ALL,
    "artifact": {"path": None, "interface": INTERFACE, "skeleton": "nano/profiles/templates/binpack_skeleton.py",
                 "output_format": OUTPUT_FORMAT, "entry": "choose_bin(item, bins, capacity)"},
    "checker": "script",
    "checker_args": dict(_bp.PROFILE["checker_args"], cost_tol=5.0),
    "docs": {},
    "diagnostics": "",
}
