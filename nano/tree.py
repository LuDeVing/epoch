"""Problem tree for the nano loop: decompose the goal into parts, and at every part generate in
two directions, inward (improve within the current paradigm) and outward (replace the paradigm),
plus upward at the root (question the framing itself, logged as proposals for a new verifier).

Research basis: Boden's exploratory vs transformational creativity; constraint transformation
and counterfactual framing (GEN-12, REP-11); frames create blind spots (REP-13); value-guided
construal and decomposition (REP-05, I2). Every idea, however radical, is still judged by the
same verifier at the same budget; the tree changes where the search looks, never what counts.

Node schema: {"id", "name", "parent", "frame", "assumptions": [...], "boundary": "...",
              "directions": ["inward", "outward"] or ["upward"], optional "kind": "part" (default) | "question" | "win",
              "idea_assumptions": [{"from", "text", "round", "kind": "silent"|"could_not_build"}],
              optional "disputed": [{"round", "text", "sketch_id", "status"}] (facts a doubt card disputed),
              optional "priority": "low" (kept by a re-plan that no longer drew it; one context per direction)}

"assumptions" are the part's design choices as the planner or the profile wrote them; they never grow during
a run. "idea_assumptions" are what tested ideas on the part assumed (interrogation, or a builder's
could-not-build note); context only, never material for the outward direction or the transform card.

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
from collections import Counter


from nano import profile as PF

# The default tree, the lenses, the direction texts and the off-map card words come from the active profile
# (nano/profiles/<name>.py, docs/GENERIC_SPEC.md). DEFAULT_TREE, LENSES, INWARD, OUTWARD, UPWARD, INWARD_FREE,
# OUTWARD_FREE and OFF_TREE_NODE stay readable as module attributes (see __getattr__ at the end), so callers
# that wrote tree.DEFAULT_TREE keep working and see the profile that is active when they read it.
# LENSES: ways the planner draws the map. The lens is a factor separate from the replicate: every replicate uses
# "parts" (or --lens) unless a lens experiment opts in with --lens-by-replicate (lens = LENSES[replicate % n]);
# state.json, problem_tree.json, answer.json and report.json record "lens" and "lens_design" (fixed | by_replicate).


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


def default_parts() -> list[dict]:
    """The default parts a planned node may refine: the profile tree without the root and the cross-part node."""
    return [n for n in default_tree() if n["id"] not in ("root", "recipe")]


def resolve_scope(only, nodes) -> set[str]:
    """The ids in `nodes` (the planned map) that the part ids in `only` refer to. The planner may rename or
    split the default parts; every planned node names the default part it refines in "refines" (planner_prompt
    asks for it), and that decides. A node without a valid "refines" (missing or "new") falls back to its id
    and name: the planner is also asked to start each name with the default name and a colon, so a default id
    resolves through its name ('mix' -> every node named 'Sequence mixing: ...')."""
    only = {str(x).strip().lower() for x in (only or ()) if str(x).strip()}
    if not only:
        return set()
    default_names = {n["id"]: _plain(n["name"]) for n in default_tree()}
    out = set()
    for n in nodes or []:
        ref = str(n.get("refines") or "").strip().lower()
        if ref in default_names:                 # explicit mapping onto a default part decides
            if ref in only:
                out.add(n["id"])
            continue
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
    view = ls.get(lens) or ls.get("parts") or next(iter(ls.values()), "")
    hint = p.v("planner_hint") or f"boundaries name the functions or sections of the {p.v('artifact', 'artifact')} a part may change"
    return ("Decompose the following problem into parts for a research search. Return ONLY a JSON array of nodes "
            '{"id", "name", "refines": "<default part id this node refines or splits, or \\"new\\" if it is none of them>", '
            '"parent": "<for a sub-part: the id of the node (in this reply) it sits under; omit for a part>", '
            '"frame", "assumptions": [3-5 short sentences], "boundary": "<which functions or classes '
            f'a change may touch>"}} with 6 to 9 parts, plus their sub-parts. Draw the map through this lens: {view}. '
            "Frames describe the CURRENT design in one or two sentences; assumptions are the design choices a "
            f"different paradigm could remove; {hint}.\n\n" + _default_parts_text() + "\n\nGOAL:\n" + goal
            + (f"\n\nHOW THE BASELINE BEHAVES (measured):\n{diagnostics}" if diagnostics else "")
            + "\n\n" + _code_block(source))


def _default_parts_text() -> str:
    """The default parts the planner maps onto, and the rule that keeps a run's --only-nodes scope resolvable."""
    dp = default_parts()
    tops = [n for n in dp if n.get("parent") in (None, "root")]
    subs = {}
    for n in dp:
        if n.get("parent") not in (None, "root"):
            subs.setdefault(n["parent"], []).append(n)
    lines = []
    for n in tops:
        lines.append(f"- {n['id']}: {n['name']}")
        for c in subs.get(n["id"], []):
            lines.append(f"    - {c['id']}: {c['name']}  (sub-part of {n['id']})")
    text = ("DEFAULT PARTS (id: name):\n" + "\n".join(lines) + "\nEvery node must say in \"refines\" which default part id it "
            "refines or splits (several nodes may refine the same part), or \"new\" if it is none of them. A node that "
            "refines a default part also starts its name with that part's name, then a colon.")
    if subs:
        text += ("\nThe indented sub-parts stay in the map: return each one as its own node (same id, the name refined if "
                 "you see it better) with \"parent\" set to the id of your node that refines its part, and \"refines\" "
                 "set to its own id. You may add a sub-part the files call for; the map is at most two levels deep.")
    return text


def repair_prompt(unresolved, nodes: list[dict]) -> str:
    """One re-ask when the planned map leaves requested default parts unmapped (loop.plan_tree)."""
    names = {n["id"]: n["name"] for n in default_parts()}
    missing = ", ".join(f"{u} ({names[u]})" if u in names else str(u) for u in sorted(unresolved))
    keep = [{k: n.get(k) for k in ("id", "name", "refines", "frame", "assumptions", "boundary")}
            for n in nodes or [] if n.get("parent") == "root" and n["id"] != "recipe"]
    return ("A planner decomposed a problem into the parts below but did not say which default part each one refines. "
            f"These default parts were not mapped: {missing}. Return the same nodes as ONLY a JSON array, unchanged "
            'except that every node has "refines" filled: the default part id it refines or splits, or "new" if it is '
            "none of them.\n\n" + _default_parts_text() + "\n\nNODES:\n" + json.dumps(keep, indent=1))


ID_LEN = 16
RESERVED_IDS = ("root", "recipe", "offtree")     # the root, the cross-part node, the off-map pseudo-node


def _clean_id(raw) -> str:
    return re.sub(r"[^a-z0-9_]", "", str(raw or "").lower())


def _unique_id(full: str, taken: set[str], fallback: str) -> str:
    """`full` cut to ID_LEN characters; on a clash with an id already taken (two long ids with a common prefix,
    or the same id twice) a numbered suffix keeps it unique within ID_LEN."""
    nid = full[:ID_LEN] or fallback
    k = 2
    while nid in taken or nid in RESERVED_IDS:
        sfx = f"_{k}"
        nid = (full or fallback)[:ID_LEN - len(sfx)] + sfx
        k += 1
    return nid


def parse_planner(text: str) -> list[dict] | None:
    """The planner's JSON array as nodes. A node may name a "parent": a sub-part, accepted when the parent id is
    another node of the same reply or a node of the default tree (that default node is then kept in the map);
    any other parent becomes the root. Ids are unique: a node whose id is reserved (root, recipe, offtree) is
    dropped, and ids that clash after cutting to ID_LEN characters get a numbered suffix; a parent reference
    resolves by the full id first, so it follows the renamed node."""
    m = re.search(r"\[.*\]", text, flags=re.S)
    if not m:
        return None
    try:
        arr = json.loads(m.group(0))
    except Exception:  # noqa: BLE001
        return None
    nodes, raw_parents = [], []
    part_ids = {d["id"] for d in default_parts()}
    base = default_tree()
    base_by_id = {n["id"]: n for n in base}
    full_to_id: dict[str, str] = {}                            # the planner's full (cleaned) id -> the id given here
    taken: set[str] = set()
    for n in arr if isinstance(arr, list) else []:
        if not isinstance(n, dict) or not all(k in n for k in ("id", "name", "frame", "assumptions")):
            continue
        if not isinstance(n.get("assumptions"), list):
            continue
        full = _clean_id(n["id"])
        if full in RESERVED_IDS:
            continue                                           # a second root, recipe or off-map node: never
        nid = _unique_id(full, taken | (set(base_by_id) - part_ids), f"n{len(nodes)}")
        taken.add(nid)
        full_to_id.setdefault(full, nid)
        ref = str(n.get("refines") or "").strip().lower()
        nodes.append({"id": nid,
                      "name": str(n["name"])[:60], "parent": "root", "refines": ref if ref in part_ids else "new",
                      "frame": str(n["frame"])[:400],
                      "assumptions": [str(a)[:160] for a in n["assumptions"]][:5],
                      "boundary": str(n.get("boundary", ""))[:200], "directions": ["inward", "outward"]})
        raw_parents.append(n.get("parent"))
    if len(nodes) < 4:
        return None
    root = next((n for n in base if n["id"] == "root"), base[0])
    recipe = [n for n in base if n["id"] == "recipe"]          # the cross-part node, when the profile has one
    ids = {n["id"] for n in nodes}
    kept = []                                                  # default parts a sub-part of this reply hangs under
    for n, rp in zip(nodes, raw_parents):
        full = _clean_id(rp)
        pid = full_to_id.get(full) or full[:ID_LEN]
        if not pid or pid in ("root", n["id"]) or (pid not in ids and pid not in base_by_id):
            continue
        n["parent"] = pid
        if pid not in ids and pid != "recipe" and all(k["id"] != pid for k in kept):
            kept.append(copy.deepcopy(base_by_id[pid]))
    return [copy.deepcopy(root)] + nodes + kept + copy.deepcopy(recipe)


MAP_NOTE = ("This map is one reader's notes, not an order: if a fact, an assumption or the weak spot named here looks "
            "wrong or incomplete, say so in the sketch and sketch what you think matters instead.")


IDEA_ASSUMPTIONS_HEAD = ("WHAT TESTED IDEAS ON THIS PART ASSUMED (not design choices; context only, do not treat as "
                         "rules to break):")
IDEA_ASSUMPTIONS_CAP = 8

# A fact of the map a doubt card disputed (loop._record_doubts). It stays on the map, marked, until it is
# re-measured (docs/mapper/03: "Until then inventors see it marked disputed"); re-measurement is not built yet.
DISPUTED_MARK = "disputed, re-measure before relying on it"
DISPUTED_HEAD = f"FACTS ABOUT THIS PART THAT A TEAM MEMBER DISPUTED ({DISPUTED_MARK}):"
DISPUTED_CAP = 3


def disputed_lines(node: dict) -> list[str]:
    """The disputed facts on a node, newest first, at most DISPUTED_CAP."""
    out = [" ".join(str(x.get("text", "")).split()) for x in reversed(node.get("disputed") or []) if isinstance(x, dict)]
    return [t for t in out if t][:DISPUTED_CAP]


def idea_assumptions(node: dict) -> list[dict]:
    """What tested ideas on this part assumed. Reads the old "assumptions_added" field of earlier runs too."""
    if isinstance(node.get("idea_assumptions"), list):
        return node["idea_assumptions"]
    out = []
    for a in node.get("assumptions_added") or []:
        text = str(a.get("text", "")) if isinstance(a, dict) else str(a)
        kind = "could_not_build" if text.startswith("could not be built") else "silent"
        out.append({"from": a.get("from", "") if isinstance(a, dict) else "", "text": text, "round": None, "kind": kind})
    return out


def migrate_node(node: dict) -> dict:
    """An old node (assumptions_added, idea texts appended to "assumptions") in the new shape, in place: the
    idea texts move out of "assumptions" into "idea_assumptions"."""
    if not isinstance(node.get("idea_assumptions"), list):
        ia = idea_assumptions(node)
        moved = {x["text"].lower()[:60] for x in ia}
        node["assumptions"] = [a for a in node.get("assumptions", []) if str(a).lower()[:60] not in moved]
        node["idea_assumptions"] = ia
    node.pop("assumptions_added", None)
    return node


# The upward reply format. An upward context proposes a new verifier, not a code change, so the sketch form
# (IDEA, MECHANISM, PREDICTION, TEST) does not fit it; nano.loop.parse_upward reads these five fields.
UPWARD_FORMAT = """List 1 to 3 distinct proposals. Do not write code. Use exactly this form for each, one blank line between proposals:

PROPOSAL: <one line: the reframed problem>
REFRAMING: <what would be modelled or measured differently from the current framing>
NEW MEASURE: <the new success measure and how it would be computed>
WHY: <what the current framing cannot see that this one can>
COST: <what a run judged by the new measure would need: data, compute, code, people>
"""


def node_prompt(node: dict, direction: str, common: str, nodes: list[dict] | None = None) -> str:
    """With `nodes` (the map), a node below depth 1 shows its path from the root and its parent's frame; a part
    (depth 1) reads exactly as before. What tested ideas assumed is a separate block, newest first, only when
    there is any (the design assumptions above stay the only material the direction text tells the agent to
    keep or break)."""
    assumptions = "\n".join(f"- {a}" for a in node["assumptions"])
    head = direction_text(direction)
    name, within = node["name"], ""
    if nodes is not None and depth(nodes, node["id"]) > 1:
        name = " > ".join(path(nodes, node["id"]))
        par = _by_id(nodes).get(node.get("parent"))
        if par is not None and par.get("frame"):
            within = "WITHIN: " + " ".join(str(par["frame"]).split()) + "\n"
    ideas = [str(x.get("text", "")) for x in reversed(node.get("idea_assumptions") or []) if str(x.get("text", "")).strip()]
    idea_block = ("\n" + IDEA_ASSUMPTIONS_HEAD + "\n" + "\n".join(f"- {t}" for t in ideas[:IDEA_ASSUMPTIONS_CAP]) + "\n"
                  if ideas else "")
    dis = disputed_lines(node)
    idea_block += ("\n" + DISPUTED_HEAD + "\n" + "\n".join(f"- {t} ({DISPUTED_MARK})" for t in dis) + "\n" if dis else "")
    return (common + f"PART UNDER STUDY: {name}\n{within}CURRENT DESIGN OF THIS PART: {node['frame']}\n"
            f"CODE THIS PART MAY TOUCH: {node['boundary']}\nASSUMPTIONS OF THIS PART:\n{assumptions}\n{idea_block}\n{head}\n\n"
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
                     + (" Assumptions: " + "; ".join(n["assumptions"]) + "." if n.get("assumptions") else "")
                     + "".join(f" Disputed ({DISPUTED_MARK}): {t}" for t in disputed_lines(n)))
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
                 order_seed: str = "", weights: dict[str, float] | None = None,
                 log: list | None = None) -> list[dict]:
    """Round-robin across nodes within each direction so one part cannot take every slot, with a
    quota: at least `new_share` of each direction's slots go to clusters tagged "new" against the
    research brief when enough of them exist.

    Every pass visits the parts in order of how many slots they have had so far (`counts`, which the
    caller may carry across directions and rounds; ties broken by a seeded shuffle), so the parts at
    the end of the map are not starved when there are fewer slots than parts.

    `weights` (node id -> weight, e.g. the idea contexts each part got this round) switches to weighted
    fairness: one slot at a time to the part with the smallest (counts + 0.5) / weight (Sainte-Lague
    divisor; ties by the seeded shuffle), so a part with weight w gets about w / sum(weights) of the slots
    and a light part is still reached. Parts missing from `weights` get the smallest given weight. With no
    weights, or all equal, the old pass-by-pass order is used unchanged.

    Shortfall: when one direction has fewer eligible clusters than its slots (no outward cluster at all, say),
    the empty slots are refilled from the clusters left in the other direction, best score first, so a round
    still fills k slots when k clusters exist. Each shortfall is logged in `log` (step "split_shortfall")."""
    import random as _random
    counts = counts if counts is not None else {}
    w = None
    if weights:
        floor = min((float(v) for v in weights.values() if float(v) > 0), default=1.0)
        w = {nid: (float(weights[nid]) if float(weights.get(nid) or 0) > 0 else floor) for nid in clusters_by_node}
        if len(set(w.values())) <= 1:
            w = None                                   # equal weights: the unweighted order, byte for byte
    tie = list(clusters_by_node)
    _random.Random(order_seed or "split").shuffle(tie)
    tie_rank = {nid: i for i, nid in enumerate(tie)}
    k_in = max(1, round(k * inward_share)) if k > 1 else k
    k_out = max(0, k - k_in)
    chosen: list[dict] = []
    left: list[dict] = []                              # ranked but not taken, both directions: the refill pool
    short: dict[str, int] = {}
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
            if w is not None:                          # weighted: one slot per call, lowest (counts + 0.5) / weight first
                for nid in sorted(per_node, key=lambda n: ((counts.get(n, 0) + 0.5) / w[n], tie_rank.get(n, 0))):
                    if picked >= kk:
                        break
                    idx = next((i for i, c in enumerate(per_node[nid]) if pred(c)), None)
                    if idx is not None:
                        c = per_node[nid].pop(idx)
                        c["selected"] = True
                        chosen.append(c)
                        counts[nid] = counts.get(nid, 0) + 1
                        picked += 1
                        return True
                return False
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
        if picked < kk:
            short[direction] = kk - picked
        left += [c for cl in per_node.values() for c in cl]
    if short:
        pool = sorted(enumerate(left), key=lambda ic: (-float(ic[1].get("score") or 0.0), ic[0]))
        refill = [c for _, c in pool[:max(0, k - len(chosen))]]
        for c in refill:
            c["selected"], c["refill"] = True, True
            chosen.append(c)
            nid = c.get("node", "root")
            counts[nid] = counts.get(nid, 0) + 1
        if log is not None:
            log.append({"step": "split_shortfall", "k": k, "short": short, "refilled": len(refill),
                        "from": dict(Counter(c.get("direction") for c in refill)),
                        "still_empty": max(0, k - len(chosen))})
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


# The metric each rung of the ladder reads, for the test a failure question enters with (docs/TEAM_GAPS_SPEC.md, C).
# Rungs 0 and 1 are pass/fail: the test is reaching the next rung. Rung 2 reads the quick gap (or the cost ratio),
# rung 3 the full gap; a gap is negative when better, so the threshold is an upper bound.
_RUNG_TESTS = {0: ("rung_reached", "the static and boundary rule (rung 0)"), 1: ("rung_reached", "the build (rung 1)"),
               2: ("learn_gap", "the quick score (rung 2)"), 3: ("long_gap", "the full score (rung 3)")}


def failure_test(feedback: dict | None, metrics: dict | None = None) -> dict | None:
    """The test, threshold and failure condition a failure question enters with, derived from the failed
    candidate's feedback (its rung and reason) and metrics. None when nothing can be derived (no rung)."""
    fb = feedback or {}
    m = metrics or {}
    try:
        rung = int(fb.get("rung"))
    except (TypeError, ValueError):
        return None
    if rung not in _RUNG_TESTS:
        return None
    reason = " ".join(str(fb.get("reason") or "").split())[:200]
    metric, what = _RUNG_TESTS[rung]
    if rung in (0, 1):
        thr = rung + 1
        return {"test": {"metric": metric, "rung": rung, "op": ">=", "what": what},
                "threshold": thr,
                "fails_if": f"the next idea built for this question fails {what} again" + (f" ({reason})" if reason else "")}
    if rung == 2 and re.search(r"\bcost is\b", reason):
        cap = re.search(r"at most ([0-9.]+)x", reason)
        thr = float(cap.group(1).rstrip(".")) if cap else 1.0
        return {"test": {"metric": "cost_ratio", "rung": 2, "op": "<=", "what": "the cost ratio at the quick score (rung 2)"},
                "threshold": thr, "fails_if": f"cost_ratio above {thr:g} at rung 2"}
    if rung == 2 and m.get("learn_gap") is None and m.get("learn_z") is not None:
        metric = "learn_z"
    allowed = re.search(r"allowed ([-+0-9.eE]+)", reason)
    try:
        thr = float(allowed.group(1).rstrip(".")) if allowed else 0.0
    except ValueError:
        thr = 0.0
    seen = m.get(metric)
    return {"test": {"metric": metric, "rung": rung, "op": "<=", "what": what},
            "threshold": thr,
            "fails_if": f"{metric} above {thr:g} at rung {rung}, or the run fails at rung {rung} again"
                        + (f" (the failed idea read {seen})" if seen is not None else "")}


def add_failure_question(nodes: list[dict], parent_id: str, cand_id: str, idea_name: str, reason: str,
                         feedback: dict | None = None, metrics: dict | None = None) -> dict | None:
    """A failed check with a reason becomes a child question under the node the idea worked on
    (docs/mapper/03, 'a failure spawns a child question'). None for a duplicate name or id, or no reason.
    The question carries `test` (metric and rung that would answer it), `threshold` and `fails_if`, derived from
    the failed candidate's feedback and metrics (failure_test); when none can be derived it is `enterable: False`
    and the question chooser (nano/pick.py) never picks it."""
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
    ft = failure_test(feedback if feedback is not None else {}, metrics)
    if ft:
        node.update(ft)
        node["enterable"] = True
    else:
        node.update({"test": None, "threshold": None, "fails_if": "", "enterable": False})
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
        if not n.get("parent") or n.get("parent") == "root" or n.get("parent") not in ids or skip(n["parent"]):
            # a live node under a skipped parent (a scope that names a sub-part only) is dealt as a part
            for d in n.get("directions", []):
                if d != "upward":
                    give(n, d, min(per, 1) if n.get("priority") == "low" else per)   # kept by a re-plan, no longer drawn
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
