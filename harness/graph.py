"""Run graph: nodes, edges, cluster root counts, HTML view, completeness check.

Implements ARCHITECTURE.md section 2 (graph.jsonl, graph.html), section 8 (Graph metrics:
node and edge completeness must be 100%; per cluster n_members, n_independent_roots,
n_independent_nonseeded) and section 11 v0.3 entry I3. 0 LLM tokens. graph.py is the only
writer of graph.jsonl; the graph is an owner view and is never routed into any prompt.

Sources (all inside runs/<id>/): cands/*.jsonl, verify.jsonl, judgments.jsonl,
clusters.jsonl, optional state.json (header flags) and optional defaults_match.json
({cand_id: bool} or [cand_id, ...]; absent at P0, so matches_default is false).

Rows of graph.jsonl:
  {kind: node, cand_id, card, operator, round, island_id, lineage_id, root_ids, parent_ids,
   status, vtype, partial_score, p_raw, origin, cluster_id, matches_default}
  {kind: edge, src, dst, kind2: parent_of | same_cluster | covers_constraint}
  {kind: cluster, cluster_id, rule, representative_id, members, n_members,
   n_independent_roots, n_independent_nonseeded, probe_members, n_independent_roots_pooled}

covers_constraint edges (candidate -> "constraint:<id>") come from a verify row's "covers" list
(or details.covers), the /verify step 5 coverage mapping. That mapping is not built at P0, so
P0 runs have no such edges. Probe candidates never pass through dedup, so they are not cluster
members; a probe node gets the cluster_id of the cluster whose members share its pred, and the
cluster row pools them in n_independent_roots_pooled (each probe call is its own root).
A parent id with no cands row is a dangling reference: no edge, no root, and check() fails.

CLI: python -m harness.graph --write RUN_DIR | --render RUN_DIR | --check RUN_DIR
(RUN_DIR may also be a bare run id under config.RUNS_DIR).
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

from . import config
from .schemas import read_json, read_jsonl

SEEDED_CARDS = ("seeded", "probe")     # excluded from n_independent_nonseeded (probe only reaches a
                                       # cluster through the pooled count, which keeps it out too)


# ---------------------------------------------------------------- loading
def resolve(run_dir) -> Path:
    """Accept a run folder path or a bare run id under config.RUNS_DIR."""
    p = Path(run_dir)
    if not p.exists() and (Path(config.RUNS_DIR) / str(run_dir)).exists():
        p = Path(config.RUNS_DIR) / str(run_dir)
    return p


def load_cands(run_dir: Path) -> list[dict]:
    """All cands rows (first occurrence per id), ordered by round then file then line."""
    seen: dict[str, dict] = {}
    order = 0
    for f in sorted((Path(run_dir) / "cands").glob("*.jsonl")):
        for r in read_jsonl(f):
            cid = r.get("id")
            if cid and cid not in seen:
                r = dict(r)
                r["_order"] = order
                seen[cid] = r
            order += 1
    return sorted(seen.values(), key=lambda r: (int(r.get("round") or 0), r["_order"]))


def load_verify(run_dir: Path) -> dict[str, dict]:
    """Last verify row per candidate id (section 2, verify.jsonl)."""
    out: dict[str, dict] = {}
    for r in read_jsonl(Path(run_dir) / "verify.jsonl"):
        if r.get("id"):
            out[r["id"]] = r
    return out


def load_judgments(run_dir: Path) -> dict[str, dict]:
    """Last judgment row per candidate id (section 2, judgments.jsonl)."""
    out: dict[str, dict] = {}
    for r in read_jsonl(Path(run_dir) / "judgments.jsonl"):
        if r.get("id"):
            out[r["id"]] = r
    return out


def load_clusters(run_dir: Path) -> dict[str, dict]:
    """clusters.jsonl membership rows merged by cluster_id (rows may repeat across rounds)."""
    out: dict[str, dict] = {}
    for r in read_jsonl(Path(run_dir) / "clusters.jsonl"):
        cid = str(r.get("cluster_id"))
        c = out.setdefault(cid, {"cluster_id": cid, "rule": r.get("rule"),
                                 "representative_id": r.get("representative_id"), "members": []})
        if not c.get("representative_id"):
            c["representative_id"] = r.get("representative_id")
        for m in [r.get("representative_id")] + list(r.get("members") or []):
            if m and m not in c["members"]:
                c["members"].append(m)
    return out


def load_defaults_match(run_dir: Path) -> set[str]:
    """Candidate ids matching an encode default; empty at P0 (no match file)."""
    d = read_json(Path(run_dir) / "defaults_match.json", default=None)
    if isinstance(d, dict):
        return {k for k, v in d.items() if v}
    if isinstance(d, list):
        return {str(x) for x in d}
    return set()


def dedup_enabled(run_dir: Path) -> bool:
    """flags.dedup from the state.json header if present, else config.FLAGS."""
    try:
        st = read_json(Path(run_dir) / "state.json", default=None)
    except (json.JSONDecodeError, OSError):
        st = None
    if isinstance(st, dict) and isinstance(st.get("flags"), dict) and "dedup" in st["flags"]:
        return bool(st["flags"]["dedup"])
    return bool(config.FLAGS.get("dedup", True))


# ---------------------------------------------------------------- derivation
def root_ids(cands: dict[str, dict]) -> dict[str, list[str]]:
    """Lineage roots per candidate: own lineage root if parentless, else union of parents'."""
    memo: dict[str, list[str]] = {}

    def roots(cid: str, stack: frozenset) -> list[str]:
        if cid in memo:
            return memo[cid]
        c = cands.get(cid)
        if c is None:
            return []                          # dangling parent: no root of its own (check() flags it)
        parents = [p for p in (c.get("parent_ids") or []) if p not in stack and p in cands]
        if not parents:
            res = [c.get("lineage_id") or cid]
        else:
            res = sorted({r for p in parents for r in roots(p, stack | {cid})})
        memo[cid] = res
        return res

    for cid in cands:
        roots(cid, frozenset())
    return memo


def _is_probe(c: dict) -> bool:
    return c.get("card") == "probe" or c.get("origin") == "probe"


def probe_clusters(cands: list[dict], clusters: dict) -> dict[str, str]:
    """Probe cand id -> cluster_id of the cluster whose members have the same pred."""
    by_id = {c["id"]: c for c in cands}
    by_pred: dict[str, str] = {}
    for cl in clusters.values():
        for m in cl["members"]:
            k = _pred_key(by_id.get(m) or {})
            if k is not None:
                by_pred.setdefault(k, cl["cluster_id"])
    out = {}
    for c in cands:
        k = _pred_key(c)
        if _is_probe(c) and k is not None and k in by_pred:
            out[c["id"]] = by_pred[k]
    return out


def build_nodes(cands: list[dict], verify: dict, judg: dict, clusters: dict,
                defaults: set) -> list[dict]:
    """Node rows (section 2 graph.jsonl node fields)."""
    roots = root_ids({c["id"]: c for c in cands})
    member_of: dict[str, str] = {}
    for cl in clusters.values():
        for m in cl["members"]:
            member_of.setdefault(m, cl["cluster_id"])
    for pid, clid in probe_clusters(cands, clusters).items():
        member_of.setdefault(pid, clid)
    nodes = []
    for c in cands:
        v, j, rs = verify.get(c["id"], {}), judg.get(c["id"], {}), roots[c["id"]]
        nodes.append({
            "kind": "node", "cand_id": c["id"], "card": c.get("card"),
            "operator": c.get("operator"), "round": int(c.get("round") or 0),
            "island_id": c.get("island_id", "main"),
            "lineage_id": c.get("lineage_id") or (rs[0] if rs else c["id"]), "root_ids": rs or [c["id"]],
            "parent_ids": list(c.get("parent_ids") or []),
            "status": v.get("status", "unverified"), "vtype": v.get("verification_type"),
            "partial_score": v.get("partial_score"), "p_raw": j.get("p_raw"),
            "origin": c.get("origin", "spoken"), "cluster_id": member_of.get(c["id"]),
            "matches_default": c["id"] in defaults,
        })
    return nodes


def covers_of(v: dict) -> list:
    """Constraint ids a verify row says the candidate covers (/verify step 5); [] when absent."""
    cov = v.get("covers")
    if cov is None:
        cov = (v.get("details") or {}).get("covers")
    return [str(x) for x in cov] if isinstance(cov, list) else []


def build_edges(cands: list[dict], clusters: dict, verify: dict | None = None) -> list[dict]:
    """parent_of edges (parent -> child; only for parents with a cands row), same_cluster edges
    (representative -> member) and covers_constraint edges (candidate -> constraint:<id>)."""
    edges = []
    ids = {c["id"] for c in cands}
    for c in cands:
        for p in c.get("parent_ids") or []:
            if p in ids:
                edges.append({"kind": "edge", "src": p, "dst": c["id"], "kind2": "parent_of"})
    for c in cands:
        for k in covers_of((verify or {}).get(c["id"], {})):
            edges.append({"kind": "edge", "src": c["id"], "dst": "constraint:" + k, "kind2": "covers_constraint"})
    for cl in clusters.values():
        rep = cl.get("representative_id") or (cl["members"][0] if cl["members"] else None)
        for m in cl["members"]:
            if rep and m != rep:
                edges.append({"kind": "edge", "src": rep, "dst": m, "kind2": "same_cluster"})
    return edges


def build_cluster_rows(clusters: dict, nodes: list[dict]) -> list[dict]:
    """Per-cluster member and independent-root counts (section 8, Graph metrics).
    A lineage counts as nonseeded when its root candidate's card is not seeded or probe.
    n_independent_roots_pooled adds the probe calls that gave the cluster's answer (P1 feature
    "pooled with probe clusters"); the other counts are over dedup members only."""
    by_id = {n["cand_id"]: n for n in nodes}
    probes: dict[str, list[str]] = {}
    for n in nodes:
        if (n.get("card") == "probe" or n.get("origin") == "probe") and n.get("cluster_id"):
            probes.setdefault(n["cluster_id"], []).append(n["cand_id"])
    out = []
    for cl in clusters.values():
        lineages: dict[str, str | None] = {}
        for m in cl["members"]:
            n = by_id.get(m)
            lin = n["lineage_id"] if n else m
            root = by_id.get(lin) or n or {}
            lineages[lin] = root.get("card")
        nonseeded = [lin for lin, card in lineages.items() if card not in SEEDED_CARDS]
        out.append({"kind": "cluster", "cluster_id": cl["cluster_id"], "rule": cl.get("rule"),
                    "representative_id": cl.get("representative_id"),
                    "members": list(cl["members"]), "n_members": len(cl["members"]),
                    "n_independent_roots": len(lineages),
                    "n_independent_nonseeded": len(nonseeded),
                    "probe_members": probes.get(cl["cluster_id"], []),
                    "n_independent_roots_pooled": len(set(lineages) | set(probes.get(cl["cluster_id"], [])))})
    return out


def _write_jsonl_atomic(p: Path, rows: list[dict]) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=True) + "\n")
    os.replace(tmp, p)


def write(run_dir: Path) -> dict:
    """Rebuild runs/<id>/graph.jsonl from its sources (section 4 graph.write; I3)."""
    run_dir = resolve(run_dir)
    cands = load_cands(run_dir)
    clusters = load_clusters(run_dir)
    nodes = build_nodes(cands, load_verify(run_dir), load_judgments(run_dir), clusters,
                        load_defaults_match(run_dir))
    edges = build_edges(cands, clusters, load_verify(run_dir))
    crows = build_cluster_rows(clusters, nodes)
    p = run_dir / "graph.jsonl"
    _write_jsonl_atomic(p, nodes + edges + crows)
    return {"nodes": len(nodes), "edges": len(edges), "clusters": len(crows), "path": str(p)}


# ---------------------------------------------------------------- check
def _pred_key(c: dict) -> str | None:
    pred = c.get("pred")
    return None if pred is None else json.dumps(pred, sort_keys=True)


def dropped_ids(run_dir: Path) -> set[str]:
    """Ids the driver dropped as duplicates (the 'dropped' field of clusters.jsonl rows)."""
    out: set[str] = set()
    for r in read_jsonl(Path(run_dir) / "clusters.jsonl"):
        out.update(str(x) for x in (r.get("dropped") or []))
    return out


def expected_drops(cands: list[dict], dedup_on: bool = True, dropped: set | None = None) -> set[str]:
    """Candidates the exact dedup rule (identical pred; section 4 dedup step) must have put
    in a cluster: every member of a pred group of size > 1, rows flagged dropped in their
    extra field, and the ids clusters.jsonl itself lists as dropped. Probe candidates and
    pred-less candidates are not counted in the pred groups."""
    if not dedup_on:
        return set()
    groups: dict[str, list[str]] = {}
    flagged = set(dropped or ())
    for c in cands:
        if c.get("card") == "probe" or c.get("origin") == "probe":
            continue
        ex = c.get("extra") or {}
        if ex.get("dedup_dropped") or ex.get("dropped") or ex.get("dup_of"):
            flagged.add(c["id"])
        k = _pred_key(c)
        if k is not None:
            groups.setdefault(k, []).append(c["id"])
    multi = {cid for ids in groups.values() if len(ids) > 1 for cid in ids}
    return multi | flagged


def _pct(found: int, total: int) -> float:
    return 100.0 if total == 0 else round(100.0 * found / total, 2)


def check(run_dir: Path) -> dict:
    """Completeness of graph.jsonl against its sources (section 8; all must be 100).
    Percentages are on a 0..100 scale."""
    run_dir = resolve(run_dir)
    if not run_dir.is_dir():
        return {"node_completeness": 0.0, "edge_completeness": 0.0, "ok": False,
                "error": f"run folder not found: {run_dir}"}
    g = read_jsonl(run_dir / "graph.jsonl")
    node_ids = {r.get("cand_id") for r in g if r.get("kind") == "node"}
    pedges = {(r.get("src"), r.get("dst")) for r in g
              if r.get("kind") == "edge" and r.get("kind2") == "parent_of"}
    crows = [r for r in g if r.get("kind") == "cluster"]
    in_cluster = {m for r in crows for m in (r.get("members") or []) + [r.get("representative_id")] if m}
    cands = load_cands(run_dir)
    want_nodes = {c["id"] for c in cands}
    want_edges = {(p, c["id"]) for c in cands for p in (c.get("parent_ids") or []) if p in want_nodes}
    dangling = sorted({(p, c["id"]) for c in cands for p in (c.get("parent_ids") or []) if p not in want_nodes})
    drops = expected_drops(cands, dedup_enabled(run_dir), dropped_ids(run_dir))
    src_clusters = set(load_clusters(run_dir))
    res = {
        "node_completeness": _pct(len(want_nodes & node_ids), len(want_nodes)),
        "edge_completeness": _pct(len(want_edges & pedges), len(want_edges)),
        "cluster_completeness": _pct(len(drops & in_cluster), len(drops)),
        "cluster_rows_completeness": _pct(len(src_clusters & {str(r.get("cluster_id")) for r in crows}),
                                          len(src_clusters)),
        "n_nodes": len(want_nodes), "n_parent_edges": len(want_edges), "n_drops": len(drops),
        "missing_nodes": sorted(want_nodes - node_ids)[:20],
        "missing_edges": [list(e) for e in sorted(want_edges - pedges)][:20],
        "missing_drops": sorted(drops - in_cluster)[:20],
        "n_dangling_parents": len(dangling), "dangling_parents": [list(e) for e in dangling][:20],
    }
    res["ok"] = all(res[k] == 100.0 for k in ("node_completeness", "edge_completeness",
                                               "cluster_completeness", "cluster_rows_completeness")) \
        and not dangling
    return res


# ---------------------------------------------------------------- render
_HTML = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Run graph</title>
<style>
:root { --bg: #fafafa; --panel: #ffffff; --fg: #222222; --muted: #666666; --line: #555555; --border: #dddddd; }
@media (prefers-color-scheme: dark) { :root { --bg: #161616; --panel: #1f1f1f; --fg: #e8e8e8; --muted: #a0a0a0; --line: #b0b0b0; --border: #333333; } }
body { margin: 0; padding: 16px; font: 13px/1.4 system-ui, sans-serif; background: var(--bg); color: var(--fg); }
h1 { font-size: 15px; margin: 0 0 4px; }
.meta { color: var(--muted); margin-bottom: 8px; }
.legend span { display: inline-block; margin-right: 14px; }
.sw { display: inline-block; width: 10px; height: 10px; border-radius: 50%; margin-right: 4px; vertical-align: middle; }
#wrap { overflow: auto; border: 1px solid var(--border); background: var(--panel); }
#tip { position: fixed; pointer-events: none; background: #222; color: #fff; padding: 6px 8px;
       border-radius: 4px; font-size: 12px; white-space: pre; display: none; }
</style></head><body>
<h1>Run graph</h1>
<div class="meta" id="meta"></div>
<div class="legend">
<span><i class="sw" style="background:#2e9e4f"></i>verified</span>
<span><i class="sw" style="background:#d9822b"></i>checked</span>
<span><i class="sw" style="background:#d64545"></i>fail</span>
<span><i class="sw" style="background:#9a9a9a"></i>unverified</span>
<span>solid line: parent_of</span><span>dashed line: same cluster</span>
</div>
<div id="wrap"><svg id="g" xmlns="http://www.w3.org/2000/svg"></svg></div>
<div id="tip"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
(function () {
  var D = JSON.parse(document.getElementById("data").textContent);
  var COL = {verified: "#2e9e4f", checked: "#d9822b", fail: "#d64545", unverified: "#9a9a9a"};
  var NS = "http://www.w3.org/2000/svg";
  var svg = document.getElementById("g"), tip = document.getElementById("tip");
  var fg = getComputedStyle(document.body).color;
  document.getElementById("meta").textContent = D.run + " | " + D.nodes.length +
    " candidates, " + D.clusters.length + " clusters";
  var rounds = {}, pos = {};
  D.nodes.forEach(function (n) { (rounds[n.round] = rounds[n.round] || []).push(n); });
  var keys = Object.keys(rounds).map(Number).sort(function (a, b) { return a - b; });
  var colW = 190, rowH = 26, top = 40, left = 60, maxRows = 1;
  keys.forEach(function (r, ci) {
    rounds[r].sort(function (a, b) {
      return (a.lineage_id + a.cand_id).localeCompare(b.lineage_id + b.cand_id); });
    maxRows = Math.max(maxRows, rounds[r].length);
    rounds[r].forEach(function (n, i) { pos[n.cand_id] = {x: left + ci * colW, y: top + i * rowH}; });
  });
  svg.setAttribute("width", left * 2 + Math.max(1, keys.length) * colW);
  svg.setAttribute("height", top + maxRows * rowH + 20);
  function el(name, attrs) {
    var e = document.createElementNS(NS, name);
    for (var k in attrs) { e.setAttribute(k, attrs[k]); }
    svg.appendChild(e); return e;
  }
  keys.forEach(function (r, ci) {
    el("text", {x: left + ci * colW - 20, y: 20, "font-size": 12, fill: fg}).textContent = "round " + r;
  });
  D.edges.forEach(function (e) {
    var a = pos[e.src], b = pos[e.dst];
    if (!a || !b) { return; }
    var dashed = e.kind2 === "same_cluster";
    el("line", {x1: a.x, y1: a.y, x2: b.x, y2: b.y, stroke: dashed ? "#7a6fd0" : fg,
                "stroke-width": dashed ? 1 : 1.5, "stroke-dasharray": dashed ? "4 3" : "none",
                opacity: dashed ? 0.75 : 0.6});
  });
  D.nodes.forEach(function (n) {
    var p = pos[n.cand_id];
    var c = el("circle", {cx: p.x, cy: p.y, r: 8, fill: COL[n.status] || COL.unverified,
                          stroke: n.matches_default ? fg : "none", "stroke-width": 2});
    el("text", {x: p.x + 12, y: p.y + 4, "font-size": 11, fill: fg}).textContent =
      n.card + (n.operator && n.operator !== "none" ? ":" + n.operator : "");
    var ps = (n.partial_score === null || n.partial_score === undefined) ? "n/a" : n.partial_score;
    var text = n.cand_id + "\ncard: " + n.card + "\noperator: " + n.operator +
      "\npartial score: " + ps + "\nstatus: " + n.status + (n.vtype ? " (" + n.vtype + ")" : "") +
      "\nlineage: " + n.lineage_id + (n.cluster_id ? "\ncluster: " + n.cluster_id : "");
    c.addEventListener("mousemove", function (ev) {
      tip.textContent = text; tip.style.display = "block";
      tip.style.left = (ev.clientX + 12) + "px"; tip.style.top = (ev.clientY + 12) + "px";
    });
    c.addEventListener("mouseleave", function () { tip.style.display = "none"; });
  });
})();
</script>
</body></html>
"""


def render(run_dir: Path) -> Path:
    """Write runs/<id>/graph.html, a self-contained owner view with no external resources
    (section 2, graph.html; I3). Writes graph.jsonl first if it is missing."""
    run_dir = resolve(run_dir)
    if not (run_dir / "graph.jsonl").exists():
        write(run_dir)
    g = read_jsonl(run_dir / "graph.jsonl")
    data = {"run": run_dir.name,
            "nodes": [r for r in g if r.get("kind") == "node"],
            "edges": [r for r in g if r.get("kind") == "edge"],
            "clusters": [r for r in g if r.get("kind") == "cluster"]}
    blob = json.dumps(data, ensure_ascii=True).replace("</", "<\\/")
    p = run_dir / "graph.html"
    p.write_text(_HTML.replace("__DATA__", blob), encoding="utf-8")
    return p


# ---------------------------------------------------------------- CLI
def main(argv: list[str] | None = None) -> int:
    """CLI entry point; exit code 1 when --check is not ok."""
    ap = argparse.ArgumentParser(prog="python -m harness.graph",
                                 description="Run graph: write, render or check (I3).")
    ap.add_argument("--write", metavar="RUN_DIR", help="rebuild graph.jsonl")
    ap.add_argument("--render", metavar="RUN_DIR", help="write graph.html")
    ap.add_argument("--check", metavar="RUN_DIR", help="completeness check; exit 1 unless ok")
    a = ap.parse_args(argv)
    if not (a.write or a.render or a.check):
        ap.error("one of --write, --render, --check is required")
    rc = 0
    if a.write:
        print(json.dumps(write(Path(a.write))))
    if a.render:
        print(str(render(Path(a.render))))
    if a.check:
        res = check(Path(a.check))
        print(json.dumps(res, indent=1))
        rc = 0 if res["ok"] else 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
