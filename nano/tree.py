"""Problem tree for the nano loop: decompose the goal into parts, and at every part generate in
two directions, inward (improve within the current paradigm) and outward (replace the paradigm),
plus upward at the root (question the framing itself, logged as proposals for a new verifier).

Research basis: Boden's exploratory vs transformational creativity; constraint transformation
and counterfactual framing (GEN-12, REP-11); frames create blind spots (REP-13); value-guided
construal and decomposition (REP-05, I2). Every idea, however radical, is still judged by the
same verifier at the same budget; the tree changes where the search looks, never what counts.

Node schema: {"id", "name", "parent", "frame", "assumptions": [...], "boundary": "...",
              "directions": ["inward", "outward"] or ["upward"], optional "kind": "part" (default) | "question" | "win"}

The nodes form a real tree through "parent" (docs/TEAM_OF_RESEARCHERS.md, docs/mapper/02 and 03): the root
(depth 0), parts (1), sub-parts (2), questions (3), helper questions (4). A fifth level never exists: a deeper
node is attached to its depth-3 ancestor (enforce_depth, logged by the loop). Children come from the planner
(a "parent" field on a sub-part), from promote_win (an off-map win hangs under the part its sketch named) and
from failures (add_failure_question: a failed check with a reason becomes a question under its part).
"""
from __future__ import annotations

import copy
import json
import re

from nano import profile as PF

# The default tree, the lenses, the direction texts and the off-map card words come from the active profile
# (nano/profiles/<name>.py, docs/GENERIC_SPEC.md). DEFAULT_TREE, LENSES, INWARD, OUTWARD, UPWARD, INWARD_FREE,
# OUTWARD_FREE and OFF_TREE_NODE stay readable as module attributes (see __getattr__ at the end), so callers
# that wrote tree.DEFAULT_TREE keep working and see the profile that is active when they read it.


def default_tree() -> list[dict]:
    """The active profile's default tree (a planner call may refine it; this is the fallback)."""
    return PF.current().tree


def lenses() -> dict:
    return PF.current().lenses


# Wording for a profile that brings no direction or off-map texts of its own; {v:key} is filled from its vocab.
_GENERIC_DIRECTIONS = {
    "inward": ("Direction INWARD: keep the paradigm of this part. Treat the assumptions below as FIXED and propose "
               "improvements inside them."),
    "outward": ("Direction OUTWARD: replace the paradigm of this part. Each sketch must remove or invert at least one "
                "of the assumptions below and say which. Ideas that merely tune the current mechanism do not count."),
    "upward": ("Direction UPWARD: question the framing of the whole problem. Sketch alternative formulations of what is "
               "being solved or measured. These will be logged as proposals for a new verifier, not implemented now, "
               "so include what the new success measure would be."),
    "inward_free": ("Direction INWARD: keep the overall paradigm of the current {v:recipe} and improve inside it, in "
                    "whichever part you choose."),
    "outward_free": ("Direction OUTWARD: replace a paradigm of your choice. Each sketch must remove or invert at least one "
                     "design assumption of the current {v:recipe} and say which."),
}
_GENERIC_OFF_MAP = {
    "node_name": "off the map (whole problem, no part assigned)",
    "node_frame": "The whole {v:recipe}, read without the problem map.",
    "blank": ("NO MAP: you are given the whole problem and the {v:artifact}, with no decomposition and no list of "
              "weak spots. Build your own picture of what holds the {v:score_name} back, then sketch. Nothing here "
              "tells you where to look; that is the point."),
    "gaps": ("WHAT DID THE MAP MISS? Sketch ideas about parts, interactions between parts, or failure modes "
             "the map has no branch for. Start each sketch with one line MISSING: <the branch the map lacks>."),
    "doubt": ("DOUBT THE MAP: pick one or two facts or assumptions in it that could be wrong, or where the opposite "
              "is the real weak spot. Start each sketch with one line DOUBT: <what the map gets wrong and why>, then "
              "sketch ideas that only make sense if the map is wrong there."),
}


def direction_text(direction: str) -> str:
    """inward, outward, upward, inward_free or outward_free, in the active profile's words."""
    p = PF.current()
    own = (p.get("directions") or {}).get(direction)
    return PF.fill(own if own else _GENERIC_DIRECTIONS[direction], p)


def _off_map(key: str) -> str:
    p = PF.current()
    own = (p.get("off_map") or {}).get(key)
    return PF.fill(own if own else _GENERIC_OFF_MAP[key], p)


def _plain(name: str) -> str:
    return " ".join(re.sub(r"\(.*?\)", "", str(name or "").lower()).split())


def resolve_scope(only, nodes) -> set[str]:
    """The ids in `nodes` (the planned map) that the part ids in `only` refer to. The planner may rename or
    split the default parts, but it keeps each default name as the first words of its names, so a default id
    also resolves through its name ('mix' -> every node named 'Sequence mixing: ...')."""
    only = {str(x).strip().lower() for x in (only or ()) if str(x).strip()}
    if not only:
        return set()
    default_names = {n["id"]: _plain(n["name"]) for n in default_tree()}
    out = set()
    for n in nodes or []:
        nid = str(n.get("id", "")).lower()
        nm = _plain(n.get("name", ""))
        head = nm.split(":")[0].strip()
        for o in only:
            dn = default_names.get(o, o)
            if nid == o or nid.startswith(o + "_") or head == dn or head == o or nm.startswith(dn + ":") or nm == dn \
                    or (len(dn) >= 8 and dn in nm):
                out.add(n["id"])
    return out


def scope_text(only) -> str:
    """For a run restricted to some parts: the parts that may change, with their boundaries, and the parts
    that stay as they are. Goes into the problem statement, so every agent reads it."""
    only = set(only or ())
    if not only:
        return ""
    allowed = [n for n in default_tree() if n["id"] in only and n["id"] != "root"]
    frozen = [n["name"] for n in default_tree() if n["id"] not in only and n["id"] != "root"]
    recipe = PF.current().v("recipe", "recipe")
    return ("SCOPE OF THIS RUN: only these parts may change" + (f"; the rest of the {recipe} ({', '.join(frozen)}) stays exactly as it is" if frozen else "") + ":\n"
            + "\n".join(f"- {n['name']}: {n.get('boundary', '')}" for n in allowed))


def _code_block(source: str) -> str:
    p = PF.current()
    return ((p.v("artifact_short") or p.v("artifact", "artifact")).upper() + ":\n```" + p.v("language", "") + "\n" + source + "\n```")


def planner_prompt(goal: str, source: str, lens: str = "parts", diagnostics: str = "") -> str:
    p = PF.current()
    ls = p.lenses
    view = ls.get(lens, ls["parts"])
    hint = p.v("planner_hint") or f"boundaries name the functions or sections of the {p.v('artifact', 'artifact')} a part may change"
    return ("Decompose the following problem into parts for a research search. Return ONLY a JSON array of nodes "
            '{"id", "name", "frame", "assumptions": [3-5 short sentences], "boundary": "<which functions or classes '
            f'a change may touch>"}} with 6 to 9 parts. Draw the map through this lens: {view}. '
            "Frames describe the CURRENT design in one or two sentences; assumptions are the design choices a "
            f"different paradigm could remove; {hint}.\n\nGOAL:\n" + goal
            + (f"\n\nHOW THE BASELINE BEHAVES (measured):\n{diagnostics}" if diagnostics else "")
            + "\n\n" + _code_block(source))


def parse_planner(text: str) -> list[dict] | None:
    """The planner's JSON array as nodes. A node may name a "parent": a sub-part, accepted when the parent id is
    another node of the same reply or a node of the default tree (that default node is then kept in the map);
    any other parent becomes the root."""
    m = re.search(r"\[.*\]", text, flags=re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    nodes, raw_parents = [], []
    for n in arr:
        if not isinstance(n, dict) or not all(k in n for k in ("id", "name", "frame", "assumptions")):
            continue
        if not isinstance(n.get("assumptions"), list):
            continue
        nodes.append({"id": re.sub(r"[^a-z0-9_]", "", str(n["id"]).lower())[:16] or f"n{len(nodes)}",
                      "name": str(n["name"])[:60], "parent": "root", "frame": str(n["frame"])[:400],
                      "assumptions": [str(a)[:160] for a in n["assumptions"]][:5],
                      "boundary": str(n.get("boundary", ""))[:200], "directions": ["inward", "outward"]})
        raw_parents.append(n.get("parent"))
    if len(nodes) < 4:
        return None
    base = default_tree()
    root = next((n for n in base if n["id"] == "root"), base[0])
    recipe = [n for n in base if n["id"] == "recipe"]          # the cross-part node, when the profile has one
    ids = {n["id"] for n in nodes}
    base_by_id = {n["id"]: n for n in base}
    kept = []                                                  # default parts a sub-part of this reply hangs under
    for n, rp in zip(nodes, raw_parents):
        pid = re.sub(r"[^a-z0-9_]", "", str(rp or "").lower())[:16]
        if not pid or pid in ("root", n["id"]) or (pid not in ids and pid not in base_by_id):
            continue
        n["parent"] = pid
        if pid not in ids and pid != "recipe" and all(k["id"] != pid for k in kept):
            kept.append(copy.deepcopy(base_by_id[pid]))
    return [copy.deepcopy(root)] + nodes + kept + copy.deepcopy(recipe)


MAP_NOTE = ("This map is one reader's notes, not an order: if a fact, an assumption or the weak spot named here looks "
            "wrong or incomplete, say so in the sketch and sketch what you think matters instead.")


def node_prompt(node: dict, direction: str, common: str, nodes: list[dict] | None = None) -> str:
    """With `nodes` (the map), a node below depth 1 shows its path from the root and its parent's frame; a part
    (depth 1) reads exactly as before."""
    assumptions = "\n".join(f"- {a}" for a in node["assumptions"])
    head = direction_text(direction)
    name, within = node["name"], ""
    if nodes is not None and depth(nodes, node["id"]) > 1:
        name = " > ".join(path(nodes, node["id"]))
        par = _by_id(nodes).get(node.get("parent"))
        if par is not None and par.get("frame"):
            within = "WITHIN: " + " ".join(str(par["frame"]).split()) + "\n"
    return (common + f"PART UNDER STUDY: {name}\n{within}CURRENT DESIGN OF THIS PART: {node['frame']}\n"
            f"CODE THIS PART MAY TOUCH: {node['boundary']}\nASSUMPTIONS OF THIS PART:\n{assumptions}\n\n{head}\n\n"
            + MAP_NOTE + "\n\n")


# ---------------------------------------------------------------- off the map (docs/TEAM_OF_RESEARCHERS.md, "a map, not a fence")
# A share of every round's idea contexts work without a branch: blank (no map at all), gaps (what did the map
# miss?) and doubt (which fact in the map is wrong?). Their sketches hang under this pseudo-node so clustering,
# selection and the per-part round robin treat "off the map" as one more part. Yield is logged per origin
# (tree / off) and the share moves with it; an off-map idea that wins becomes a new branch (promote_win).
OFF_TREE_ID = "offtree"
OFF_TREE_CARDS = ("blank", "gaps", "doubt")


def off_tree_node() -> dict:
    """The off-map pseudo-node in the active profile's words (a fresh dict each call)."""
    return {"id": OFF_TREE_ID, "name": _off_map("node_name"), "parent": "root",
            "frame": _off_map("node_frame"), "assumptions": [],
            "boundary": PF.current().boundary_all, "directions": ["inward", "outward"]}


def tree_text(nodes: list[dict], diagnostics: str = "") -> str:
    """The map as a list, parent before children, two spaces of indent per level below the parts."""
    lines = []
    for n in _dfs(nodes):
        if n["id"] in ("root", OFF_TREE_ID):
            continue
        lines.append("  " * max(0, depth(nodes, n["id"]) - 1) + f"- {n['name']}: {n['frame']}"
                     + (" Assumptions: " + "; ".join(n["assumptions"]) + "." if n.get("assumptions") else ""))
    return "\n".join(lines) + (f"\n\nMEASUREMENTS BEHIND THE MAP:\n{diagnostics}" if diagnostics else "")


def off_tree_prompt(card: str, nodes: list[dict], common: str, diagnostics: str, direction: str) -> str:
    head = direction_text("inward_free" if direction == "inward" else "outward_free")
    scope = f"CODE A SKETCH MAY TOUCH: {PF.current().boundary_all}\n\n{head}\n\n"
    if card == "blank":
        return common + _off_map("blank") + "\n\n" + scope
    if card == "gaps":
        return (common + "THE PROBLEM MAP THE OTHER IDEA AGENTS WORK FROM:\n" + tree_text(nodes, diagnostics)
                + "\n\n" + _off_map("gaps") + "\n\n" + scope)
    return (common + "THE PROBLEM MAP THE OTHER IDEA AGENTS WORK FROM:\n" + tree_text(nodes, diagnostics)
            + "\n\n" + _off_map("doubt") + "\n\n" + scope)


def promote_win(nodes: list[dict], cand_id: str, cluster_name: str, hypothesis: str, change: str,
                part: str = "") -> dict | None:
    """An off-map idea that passed its checks becomes a branch of the map, so later rounds see it. It hangs under
    the part `part` names (the winning sketch's PART field, or a node id) when that is a real part of the map,
    under the root otherwise."""
    nid = "win_" + "".join(ch for ch in str(cand_id).lower() if ch.isalnum())[:8]
    if any(n["id"] == nid for n in nodes):
        return None
    node = {"id": nid, "name": ("from an off-map win: " + str(cluster_name or hypothesis))[:60],
            "parent": find_part(nodes, part) or "root",
            "frame": str(hypothesis or "")[:400], "assumptions": [str(change)[:160]] if change else [],
            "boundary": PF.current().boundary_all, "directions": ["inward", "outward"], "origin": OFF_TREE_ID,
            "kind": "win"}
    nodes.append(node)
    return node


def split_select(clusters_by_node: dict[str, list[dict]], k: int, inward_share: float, exclude: set[str],
                 sketches: list[dict], select_fn, new_share: float = 0.5, counts: dict[str, int] | None = None,
                 order_seed: str = "") -> list[dict]:
    """Round-robin across nodes within each direction so one part cannot take every slot, with a
    quota: at least `new_share` of each direction's slots go to clusters tagged "new" against the
    research brief when enough of them exist.

    Every pass visits the parts in order of how many slots they have had so far (`counts`, which the
    caller may carry across directions and rounds; ties broken by a seeded shuffle), so the parts at
    the end of the map are not starved when there are fewer slots than parts."""
    import random as _random
    counts = counts if counts is not None else {}
    tie = list(clusters_by_node)
    _random.Random(order_seed or "split").shuffle(tie)
    tie_rank = {nid: i for i, nid in enumerate(tie)}
    k_in = max(1, round(k * inward_share)) if k > 1 else k
    k_out = max(0, k - k_in)
    chosen: list[dict] = []
    for direction, kk in (("inward", k_in), ("outward", k_out)):
        per_node = {}
        for nid, cl in clusters_by_node.items():
            cands = [c for c in cl if c.get("direction") == direction and c["cluster_id"] not in exclude]
            if cands:
                ranked = select_fn(cands, len(cands), exclude=set(), sketches=sketches)
                for c in ranked:              # select_fn ranks; only the round-robin below selects
                    c["selected"] = False
                per_node[nid] = ranked
        picked = 0
        quota = int(round(kk * new_share))

        def take(pred) -> bool:
            nonlocal picked
            got = False
            for nid in sorted(per_node, key=lambda n: (counts.get(n, 0), tie_rank.get(n, 0))):
                if picked >= kk:
                    break
                idx = next((i for i, c in enumerate(per_node[nid]) if pred(c)), None)
                if idx is not None:
                    c = per_node[nid].pop(idx)
                    c["selected"] = True
                    chosen.append(c)
                    counts[nid] = counts.get(nid, 0) + 1
                    picked += 1
                    got = True
            return got

        while picked < quota and take(lambda c: c.get("prior") == "new"):
            pass
        while picked < kk and take(lambda c: True):
            pass
    return chosen


# ---------------------------------------------------------------- the tree structure (docs/mapper/02, 1.4; 03, maintenance)
MAX_DEPTH = 4            # parts (1), sub-parts (2), questions (3), helper questions (4); the root is depth 0
FAIL_QUESTIONS_PER_PART = 2


def _by_id(nodes: list[dict]) -> dict[str, dict]:
    return {n["id"]: n for n in nodes or []}


def kind(node: dict) -> str:
    """part (default), question or win."""
    return node.get("kind") or "part"


def children(nodes: list[dict], node_id: str) -> list[dict]:
    """The nodes whose parent is `node_id`, in map order."""
    return [n for n in nodes or [] if n.get("parent") == node_id and n["id"] != node_id]


def _chain(nodes: list[dict], node_id: str) -> list[dict]:
    """The node and its ancestors below the root, nearest first (a cycle or a missing parent ends the walk)."""
    by, out, seen = _by_id(nodes), [], set()
    cur = by.get(node_id)
    while cur is not None and cur["id"] != "root" and cur["id"] not in seen:
        seen.add(cur["id"])
        out.append(cur)
        cur = by.get(cur.get("parent")) if cur.get("parent") else None
    return out


def depth(nodes: list[dict], node_id: str) -> int:
    """0 for the root (and an unknown id), 1 for a part, 2 for a sub-part, ..."""
    return len(_chain(nodes, node_id))


def path(nodes: list[dict], node_id: str) -> list[str]:
    """The names from the top-level part down to the node (the root itself is left out)."""
    return [n["name"] for n in reversed(_chain(nodes, node_id))]


def leaves(nodes: list[dict]) -> list[dict]:
    """The nodes without children (the root is never a leaf)."""
    parents = {n.get("parent") for n in nodes or []}
    return [n for n in nodes or [] if n["id"] != "root" and n["id"] not in parents]


def _dfs(nodes: list[dict]) -> list[dict]:
    """Every node once, parent before children, siblings in map order. For a flat map this is the map order."""
    ids = {n["id"] for n in nodes or []}
    out, seen = [], set()

    def walk(n):
        if n["id"] in seen:
            return
        seen.add(n["id"])
        out.append(n)
        for k in children(nodes, n["id"]):
            walk(k)
    for n in nodes or []:
        if not n.get("parent") or n.get("parent") not in ids or n.get("parent") == n["id"]:
            walk(n)
    for n in nodes or []:                       # anything left on a parent cycle
        walk(n)
    return out


def subtree(nodes: list[dict], node_id: str) -> list[dict]:
    """The node and all its descendants, parent before children."""
    return [n for n in _dfs(nodes) if n["id"] == node_id or any(a["id"] == node_id for a in _chain(nodes, n["id"])[1:])]


def nested(nodes: list[dict]) -> dict:
    """The map as one nested dict {id, name, kind, children: [...]} from the root."""
    def view(n):
        return {"id": n["id"], "name": n.get("name", ""), "kind": "root" if n["id"] == "root" else kind(n),
                "children": [view(k) for k in children(nodes, n["id"])]}
    ids = {n["id"] for n in nodes or []}
    tops = [n for n in _dfs(nodes) if not n.get("parent") or n.get("parent") not in ids]
    if len(tops) == 1 and tops[0]["id"] == "root":
        return view(tops[0])
    return {"id": "root", "name": "", "kind": "root", "children": [view(n) for n in tops if n["id"] != "root"]}


def enforce_depth(nodes: list[dict], max_depth: int = MAX_DEPTH) -> list[dict]:
    """Depth at most `max_depth`: a deeper node is attached to its ancestor at depth max_depth - 1 (so it sits
    at the last level). Changes the nodes in place; returns one decision record per moved node for the log."""
    moved = []
    for n in _dfs(nodes):
        ch = _chain(nodes, n["id"])
        if len(ch) <= max_depth:
            continue
        to = ch[-(max_depth - 1)]               # the chain is nearest first: this is the depth-(max_depth-1) ancestor
        moved.append({"step": "tree_depth", "node": n["id"], "depth_was": len(ch), "from_parent": n.get("parent"),
                      "to_parent": to["id"]})
        n["parent"] = to["id"]
    return moved


def find_part(nodes: list[dict], text: str) -> str | None:
    """The id of the part (kind part, not the root or the off-map node) a free-text name or an id refers to."""
    t = " ".join(str(text or "").lower().split())
    if not t:
        return None
    for n in nodes or []:
        if n["id"] in ("root", OFF_TREE_ID) or kind(n) != "part":
            continue
        name = " ".join(str(n.get("name", "")).lower().split())
        if t == n["id"].lower() or t == name or (len(t) >= 4 and (t in name or name in t)):
            return n["id"]
    return None


def add_failure_question(nodes: list[dict], parent_id: str, cand_id: str, idea_name: str, reason: str) -> dict | None:
    """A failed check with a reason becomes a child question under the node the idea worked on
    (docs/mapper/03, 'a failure spawns a child question'). None for a duplicate name or id, or no reason."""
    par = _by_id(nodes).get(parent_id)
    if par is None or not str(reason or "").strip():
        return None
    name = f"why did {' '.join(str(idea_name or cand_id).split())[:80]} fail?"
    nid = "q_" + "".join(ch for ch in str(cand_id).lower() if ch.isalnum())[:8]
    if any(n["id"] == nid or n.get("name") == name for n in nodes):
        return None
    node = {"id": nid, "name": name, "parent": parent_id, "frame": " ".join(str(reason).split())[:400],
            "assumptions": [], "boundary": par.get("boundary", ""), "directions": ["inward"],
            "origin": "failure", "kind": "question", "from": [cand_id]}
    nodes.append(node)
    return node


def deal_contexts(nodes: list[dict], per: int, round_no: int = 1, skip=None) -> dict[tuple[str, str], int]:
    """Idea contexts per (node id, direction), so depth does not multiply cost. Every top-level part gets `per`
    contexts per direction (the root's upward contexts are dealt by the loop). A node with children (that take
    the direction and are not skipped) shares its budget with them: it keeps 1 and the rest go round-robin to
    the children; a child with children passes its share down by the same rule; a question takes at most 1 and
    what it cannot take goes back to its parent. A budget of 1 rotates over the node and its children by round,
    so children are still reached. A flat map gets `per` for every part and direction, as before."""
    skip = skip or (lambda nid: False)
    out: dict[tuple[str, str], int] = {}

    def give(n, d, b):
        if kind(n) == "question":
            b = min(b, 1)
        kids = [k for k in children(nodes, n["id"]) if d in k.get("directions", []) and not skip(k["id"])]
        if not kids or b <= 0:
            out[(n["id"], d)] = max(0, b)
            for k in kids:
                give(k, d, 0)
            return
        if b == 1:
            order = [n] + kids
            pick = order[(max(1, round_no) - 1) % len(order)]
            out[(n["id"], d)] = 1 if pick is n else 0
            for k in kids:
                give(k, d, 1 if k is pick else 0)
            return
        share = {k["id"]: 0 for k in kids}
        rest, own = b - 1, 1
        while rest > 0:
            open_ = [k for k in kids if kind(k) != "question" or share[k["id"]] < 1]
            if not open_:
                own += rest
                break
            for k in open_:
                if rest <= 0:
                    break
                share[k["id"]] += 1
                rest -= 1
        out[(n["id"], d)] = own
        for k in kids:
            give(k, d, share[k["id"]])

    ids = {n["id"] for n in nodes or []}
    for n in nodes or []:
        if n["id"] == "root" or skip(n["id"]):
            continue
        if not n.get("parent") or n.get("parent") == "root" or n.get("parent") not in ids:
            for d in n.get("directions", []):
                if d != "upward":
                    give(n, d, per)
    return out


# ---------------------------------------------------------------- backward-compatible module attributes
_ALIASES = {
    "DEFAULT_TREE": default_tree,
    "LENSES": lenses,
    "INWARD": lambda: direction_text("inward"),
    "OUTWARD": lambda: direction_text("outward"),
    "UPWARD": lambda: direction_text("upward"),
    "INWARD_FREE": lambda: direction_text("inward_free"),
    "OUTWARD_FREE": lambda: direction_text("outward_free"),
    "OFF_TREE_NODE": off_tree_node,
}


def __getattr__(name: str):
    """tree.DEFAULT_TREE, tree.LENSES, tree.INWARD, ... read the active profile at access time (PEP 562)."""
    if name in _ALIASES:
        return _ALIASES[name]()
    raise AttributeError(f"module 'nano.tree' has no attribute {name!r}")
