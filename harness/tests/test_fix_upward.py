"""Issue 7: upward (reframing) contexts are dealt, answered in their own format, parsed, and read.

The arch-2 run produced no upward proposal: the test-mode cap kept only research and diagnosis contexts, and
an upward reply could not have parsed anyway (parse_sketches needs IDEA and MECHANISM). These tests check the
format, the parser, the cap guarantee, and a tiny mock run end to end (stopped after ideation, so nothing trains
beyond the mock diagnostics)."""
from __future__ import annotations

import json
import sys

from harness import config, llm


def test_upward_format_and_parser():
    from nano import dry_run, loop, tree
    for key in ("PROPOSAL:", "REFRAMING:", "NEW MEASURE:", "WHY:", "COST:"):
        assert key in tree.UPWARD_FORMAT
    reply = dry_run.mock("x Direction UPWARD: question the framing", "generate", {"card": "sketch:seeded", "seed": "s"})
    n = iter(range(100))
    recs = loop.parse_upward(reply, round_no=2, call_id="c1", idgen=lambda: f"u{next(n)}")
    assert len(recs) == 2
    r = recs[0]
    assert set(r) == {"id", "proposal", "reframing", "new_measure", "why", "cost", "round", "call_id"}
    assert r["round"] == 2 and r["call_id"] == "c1" and "rare tokens" in r["proposal"] and r["new_measure"] and r["cost"]
    # markdown bold and a multi-line field still parse; a block with only a PROPOSAL does not count
    md = "**PROPOSAL:** a\n**NEW MEASURE:** b\ncontinued\n\nPROPOSAL: lonely"
    out = loop.parse_upward(md, round_no=1, call_id="c", idgen=lambda: "u")
    assert len(out) == 1 and out[0]["new_measure"] == "b continued"
    # a sketch-format reply is not a proposal
    assert loop.parse_upward("IDEA: x\nMECHANISM: y", round_no=1, call_id="c", idgen=lambda: "u") == []


def test_cap_keeps_one_upward_context():
    from nano import ideate, loop
    root = {"id": "root"}
    specs = [("seeded", "", root, "upward"), ("formal", "", root, "upward")]
    for p in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        specs += [("research", "", {"id": p}, "inward"), ("research", "", {"id": p}, "outward"),
                  ("diagnosis", "", {"id": p}, "inward")]
    prio = {"owner": -1, "research": 0, "diagnosis": 1, "analogy": 2}
    ups = [sp for sp in specs if sp[3] == "upward"]
    capped = ideate.deal_by_part(specs, 6, lambda sp: prio.get(sp[0], 3), lambda sp: sp[2]["id"])
    assert not any(sp[3] == "upward" for sp in capped)          # the bug: a cap below the part count drops upward
    kept = loop.keep_upward(capped, ups)
    assert len(kept) == 6 and sum(sp[3] == "upward" for sp in kept) == 1
    owners = [("owner", "x", {"id": "a"}, "inward")]
    assert loop.keep_upward(owners, ups) == owners + [ups[0]]   # owner seeds are never replaced
    assert loop.keep_upward([], ups) == []                       # nothing dealt, nothing added
    assert loop.keep_upward(capped, []) == capped


def test_mock_run_reports_upward_proposals(monkeypatch):
    from pathlib import Path
    from nano import check, dry_run
    real = Path(r"D:\AGI-lab")                 # the run folder is the test's temp lab; the interpreter and data are the lab's
    monkeypatch.setattr(check, "PY", real / ".venv" / "Scripts" / "python.exe")
    monkeypatch.setattr(check, "DATA_FULL", real / "data" / "fineweb")
    monkeypatch.setattr(check, "DATA_TRAIN", real / "data" / "fineweb_train_only")
    monkeypatch.setattr(sys, "argv", ["dry_run", "--batch", "mock-fix-upward", "--max-sketch-calls", "6",
                                      "--implement", "1", "--rounds", "1", "--stop-after", "ideated"])
    try:
        dry_run.main()
    finally:
        llm.set_mock(None)
    run = next(config.RUNS_DIR.glob("mock-fix-upward__*"))
    props = [json.loads(x) for x in (run / "proposals_upward.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert props and all(p.get("proposal") and p.get("new_measure") for p in props)
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))
    assert rep["upward"] and rep["upward"][0]["proposal"] == props[0]["proposal"]
    md = (run / "REPORT.md").read_text(encoding="utf-8")
    assert "## Proposals for a new verifier (upward)" in md and props[0]["proposal"] in md and "human decision" in md
    pt = json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))
    root = next(n for n in pt["nodes"] if n["id"] == "root")
    assert [p["id"] for p in root["proposals"]] == [p["id"] for p in props]
    ideas = (run / "ideas.jsonl").read_text(encoding="utf-8") if (run / "ideas.jsonl").exists() else ""
    assert '"direction": "upward"' not in ideas                  # proposals never enter the build pipeline
