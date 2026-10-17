"""Gap A: per-part persistent memory (nano/memory.py and its hooks in nano/loop.py).

Unit tests for parse, curate, dedupe, the read cap and archive; then one small mock run (binpack_nobase,
2 rounds) with memory on, and one with --no-memory (the control arm)."""
from __future__ import annotations

import json
import re
import sys

from harness import config
from nano import memory as M

ART = {"cand_ids": {"n93f5235b01", "nfc5e00e7bb"}, "sketch_ids": {"s0e851c44a9"},
       "numbers": [1.091795, 0.010339, 9.88], "urls": {"https://arxiv.org/abs/2010.04245"}}

DELTA = """FACTS:
- measured | best fit used fewer bins than first fit | n93f5235b01
- web | a 2020 paper reports the same trend | https://arxiv.org/abs/2010.04245
- belief | an invented rule would win | n0000dead00
TRIED:
- worst fit | 1.0918 | lost to best fit on the quick score | nfc5e00e7bb
PRIORS:
- greedy rules pass the quick score about 3 in 4 times | n93f5235b01
- greedy rules usually pass | n93f5235b01
CUES:
- when a rule ties the reference -> change the tie-break | s0e851c44a9
OPEN QUESTIONS:
- does it hold on 2000 items? | nothing cited here
FAILED FRAMINGS:
- **treating all items alike** | gap 0.0103 | nfc5e00e7bb
USED:
- none
"""


def test_parse_delta():
    d = M.Memory.propose_delta("choice", DELTA)
    secs = [e["section"] for e in d["entries"]]
    assert secs.count("FACTS") == 3 and secs.count("PRIORS") == 2 and "FAILED FRAMINGS" in secs
    f = d["entries"][0]
    assert f["source"] == "measured" and f["text"].startswith("best fit")
    assert d["entries"][1]["source"] == "web"
    assert "**" not in d["entries"][-1]["text"] and d["used"] == []
    assert M.Memory.propose_delta("x", "USED: m1a2b3c, m4d5e6f")["used"] == ["m1a2b3c", "m4d5e6f"]


def test_curate_rule_and_file(tmp_path):
    mem = M.Memory(tmp_path, "prof")
    res = mem.curate("choice", M.Memory.propose_delta("choice", DELTA), ART, run="runx", round_no=1)
    reasons = {r["text"][:20]: r["reason"] for r in res["rejected"]}
    assert any("does not exist" in r and "n0000dead00" in r for r in reasons.values())     # made-up id
    assert any(r == "cites no run artefact" for r in reasons.values())                     # no citation
    assert any(r == "a prior needs a number" for r in reasons.values())
    kept = {e["section"] for e in res["added"]}
    assert kept == {"FACTS", "TRIED", "PRIORS", "CUES", "FAILED FRAMINGS"}
    assert len(res["added"]) == 6                         # 2 facts, tried (number 1.0918 and id), prior, cue, framing
    text = mem.path("choice").read_text(encoding="utf-8")
    assert text.startswith("# Memory: choice\nCLOCK: 1\n## FACTS")
    for h in M.SECTIONS + (M.ARCHIVE,):
        assert f"## {h}\n" in text
    line = next(x for x in text.splitlines() if "best fit used fewer" in x)
    assert re.match(r"- \[m[0-9a-f]{6}\] \d{4}-\d{2}-\d{2} \| runx r1 \| measured \| ", line) and line.endswith("| used 1")
    # the file round-trips through load/save unchanged
    data = mem.load("choice")
    mem.save("choice", data)
    assert mem.path("choice").read_text(encoding="utf-8") == text
    # a measured number counts only at its shown precision
    assert M.Memory.cites("gap was 0.0103", ART)[0] and not M.Memory.cites("gap was 0.0200", ART)[0]


def test_dedupe_bumps_instead_of_adding(tmp_path):
    mem = M.Memory(tmp_path, "prof")
    mem.curate("p", M.Memory.propose_delta("p", "FACTS:\n- measured | best fit used fewer bins than first fit | n93f5235b01"), ART)
    again = "FACTS:\n- measured | best fit used fewer bins than first fit did | n93f5235b01\n- measured | worst fit opened many more bins | nfc5e00e7bb"
    res = mem.curate("p", M.Memory.propose_delta("p", again), ART)
    assert len(res["added"]) == 1 and res["rejected"][0]["reason"].startswith("near-duplicate of m")
    data = mem.load("p")
    assert data["clock"] == 2 and len(data["sections"]["FACTS"]) == 2
    assert all(e["used"] == 2 for e in data["sections"]["FACTS"])     # the duplicate re-confirmed the old entry
    assert M.jaccard("a b c d", "a b c e") == 0.6


def test_read_cap_drops_from_view_not_file(tmp_path):
    mem = M.Memory(tmp_path, "prof", max_tokens=4000)
    data = mem.load("p")
    for i in range(60):
        src = "belief" if i < 30 else "measured"
        data["sections"]["FACTS"].append({"id": f"m{i:06x}", "date": "2026-10-01", "run": "r r1", "source": src,
                                          "text": f"fact number {i} " + "word " * 20, "used": i})
    data["sections"]["FAILED FRAMINGS"].append({"id": "mffffff", "date": "2026-01-01", "run": "r r1", "source": "belief",
                                                "text": "an old dead end", "used": 0})
    mem.save("p", data)
    full = mem.read("p")
    small = mem.read("p", max_tokens=300)
    assert len(small) // 4 <= 300 < len(full) // 4
    assert "left out of this view" in small
    assert "mffffff" in small                             # failed framings go last
    assert "m00003b" in small and "m000000" not in small  # newest measured stays, oldest belief goes
    assert len(mem.load("p")["sections"]["FACTS"]) == 60 # the file keeps everything
    b = mem.block("p")
    assert b.startswith(M.BLOCK_HEAD) and "evidence, not rules" in b
    assert mem.block("empty_part") == ""


def test_archive(tmp_path):
    mem = M.Memory(tmp_path, "prof")
    mem.curate("p", M.Memory.propose_delta("p", "FACTS:\n- measured | old fact about bins | n93f5235b01"), ART)
    first = mem.load("p")["sections"]["FACTS"][0]["id"]
    for k in range(5):
        mem.curate("p", M.Memory.propose_delta("p", f"CUES:\n- when case {k} {'x' * k} appears -> check thing {k} | nfc5e00e7bb"), ART)
    assert mem.archive("p", unused_rounds=5) == [first]
    data = mem.load("p")
    assert not data["sections"]["FACTS"] and data["sections"]["ARCHIVE"][0]["text"].startswith("(FACTS) old fact")
    assert "old fact" not in mem.read("p")


def _mock_run(monkeypatch, batch, rounds, *flags):
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", config.VENV_PYTHON, raising=False)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", batch, "--max-sketch-calls", "8",
                                      "--implement", "2", "--rounds", str(rounds), *flags])
    assert dry_run.main() == 0
    runs = [p for p in config.RUNS_DIR.iterdir() if p.name.startswith(batch + "__")]
    assert len(runs) == 1
    return runs[0]


def test_mock_run_with_memory(monkeypatch):
    run = _mock_run(monkeypatch, "mock-gap-a", 2)
    memdir = config.MEMORY_DIR / "_mock" / "binpack_nobase"
    files = sorted(memdir.glob("*.md"))
    assert files
    with_entries = {}
    for f in files:
        lines = [x for x in f.read_text(encoding="utf-8").splitlines() if x.startswith("- [m")]
        with_entries[f.stem] = lines
        for x in lines:                                   # date and source on every entry
            assert re.match(r"- \[m[0-9a-f]{6}\] \d{4}-\d{2}-\d{2} \| \S+ r\d \| (script|measured|web|belief) \| ", x), x
    assert any(with_entries.values())
    log = [json.loads(x) for x in (run / "memory_log.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    rejected = [r for row in log for r in row["rejected"]]
    assert any("n0000dead00" in r["reason"] and "does not exist" in r["reason"] for r in rejected)
    assert not any("n0000dead00" in x for xs in with_entries.values() for x in xs)
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))
    assert rep["memory"]["parts"] >= 1 and rep["memory"]["entries_added"] >= 1 and rep["memory"]["entries_rejected"] >= 1
    # round 2: on-map prompts of parts with memory carry the block, except the one ignores-memory context per part
    r1_parts = {row["part"] for row in log if row["round"] == 1}
    assert r1_parts
    parent = {n["id"]: n.get("parent") for n in json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))["nodes"]}

    def part_of(nid):
        while parent.get(nid) not in (None, "root"):
            nid = parent[nid]
        return nid
    seen = {}
    for f in (run / "calls").glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        m = d.get("meta") or {}
        if m.get("round") != 2 or not m.get("memory") or str(m.get("card", "")).endswith(":questions"):
            continue
        text = (run / "prompts" / f"{d['call_id']}.txt").read_text(encoding="utf-8")
        seen.setdefault(part_of(m["node"]), []).append((m["memory"], M.BLOCK_HEAD in text))
    for part in r1_parts:
        states = seen.get(part, [])
        assert sorted(s for s, _ in states) == ["block", "free"], (part, states)
        assert all(has == (s == "block") for s, has in states)
    st = json.loads((run / "state.json").read_text(encoding="utf-8"))
    free = [d for d in st["decisions"] if d.get("step") == "memory_free"]
    assert {d["part"] for d in free if d["round"] == 2} == r1_parts      # logged, one per part


def test_mock_run_no_memory(monkeypatch):
    run = _mock_run(monkeypatch, "mock-gap-a-off", 1, "--no-memory")
    assert not (config.MEMORY_DIR / "_mock").exists() and not (config.MEMORY_DIR / "binpack_nobase").exists()
    assert not (run / "memory_log.jsonl").exists()
    assert json.loads((run / "report.json").read_text(encoding="utf-8"))["memory"] == "off"
    for f in (run / "calls").glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        assert d["meta"].get("card") != "memory_curator" and "memory" not in d["meta"]
