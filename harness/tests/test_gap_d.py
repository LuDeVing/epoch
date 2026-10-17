"""Gap D: fetch on demand. A builder or reviser missing one fact writes `NEED: <fact>`; the loop fetches it with a
source (research.fetch_fact, cached per run in facts_fetched.jsonl) and re-prompts the same builder once.
Tests: NEED parsing and the cap of 2, the cache, the re-prompt-once rule, the default-off rule without the web,
and a mock run on binpack_nobase that asserts facts_fetched.jsonl and the report counts."""
from __future__ import annotations

import json
import sys
import threading
import types
from pathlib import Path

from harness import config, llm


def test_parse_needs_and_cap():
    from nano import research
    text = ("HYPOTHESIS: x\nNEED: what is the worst-case ratio of first fit?\n**NEED:** which bound holds for best fit online?\n"
            "NEED: a third fact that is over the cap\nNEED: omit\nNEED: <one specific fact>\n"
            "```python\n# NEED: inside the code block is not a request\n```")
    needs, over = research.parse_needs(text)
    assert needs == ["what is the worst-case ratio of first fit?", "which bound holds for best fit online?"]
    assert over == 1
    assert research.parse_needs("HYPOTHESIS: x\nNEED: omit\n```python\nx=1\n```") == ([], 0)
    assert research.parse_needs("NEED: same fact here please\nNEED: Same fact, here please!") == (["same fact here please"], 0)


def test_need_line_goes_before_the_code_block():
    from nano import loop
    fmt = loop._GENERIC_OUTPUT_FORMAT
    out = loop.with_need_line(fmt)
    lines = out.splitlines()
    i_need = next(i for i, x in enumerate(lines) if x.startswith("NEED:"))
    i_code = next(i for i, x in enumerate(lines) if x.startswith("```"))
    assert i_need == i_code - 1 and lines[i_need - 1].startswith("FIDELITY:")
    assert loop.with_need_line("no fence here").endswith(loop.NEED_LINE + "\n")


def test_parse_fetch():
    from nano import research
    ok = research.parse_fetch("ANSWER: 1.7 asymptotically.\nSOURCE: https://example.org/ff\nCONFIDENCE: high", "q")
    assert ok == {"question": "q", "answer": "1.7 asymptotically.", "source_url": "https://example.org/ff",
                  "confidence": "high", "tag": "web"}
    assert research.parse_fetch("ANSWER: not found\nSOURCE: none", "q")["answer"] is None
    nosrc = research.parse_fetch("ANSWER: 1.7, I think\nSOURCE: memory\nCONFIDENCE: low", "q")
    assert nosrc["answer"] is None and nosrc["reason"] == "no source URL"


def test_fetch_cache(tmp_path):
    from nano import research
    calls = []

    def call(p):
        calls.append(p)
        return "ANSWER: 1.7\nSOURCE: https://example.org/ff\nCONFIDENCE: medium"
    a = research.fetch_fact("What is the ratio of First Fit?", {"id": "choice", "name": "the bin choice"}, call, cache_dir=tmp_path)
    b = research.fetch_fact("what is the ratio of first fit", None, call, cache_dir=tmp_path)
    assert len(calls) == 1 and a["answer"] == "1.7" and a["tag"] == "web" and b.get("cached") and b["source_url"] == a["source_url"]
    rows = [json.loads(x) for x in (tmp_path / research.FETCH_CACHE_NAME).read_text(encoding="utf-8").splitlines()]
    assert len(rows) == 1 and rows[0]["node"] == "choice"
    nf = research.fetch_fact("an unknowable fact about bins", None, lambda p: "ANSWER: not found", cache_dir=tmp_path)
    again = research.fetch_fact("an unknowable fact about bins", None, lambda p: 1 / 0, cache_dir=tmp_path)
    assert nf["answer"] is None and again["answer"] is None and again.get("cached")      # not found is cached too
    failed = research.fetch_fact("a fetch that raises", None, lambda p: 1 / 0)
    assert failed["answer"] is None and "fetch failed" in failed["reason"]


def _stub_loop(tmp_path, replies):
    """A NanoLoop with only what _handle_needs touches; _call returns the queued replies in order."""
    from nano import loop as L
    lp = L.NanoLoop.__new__(L.NanoLoop)
    lp.lock, lp.decisions, lp.run_dir = threading.RLock(), [], tmp_path
    lp.fetch_on_demand, lp.clusters, lp.tree, lp.research_model = True, [], [], "sonnet"
    lp.fetch_stats = {"requests": 0, "answered": 0, "reprompts": 0, "logged_only": 0, "ignored_after_reprompt": 0, "over_cap": 0}
    lp.calls, lp.ledger_rows = [], []
    queue = list(replies)

    def _call(prompt, role, max_tokens, meta, **kw):
        lp.calls.append((role, meta.get("card"), prompt))
        text = ("ANSWER: 1.7\nSOURCE: https://example.org/ff\nCONFIDENCE: high" if meta.get("card") == "fetch_fact"
                else queue.pop(0))
        return types.SimpleNamespace(text=text, call_id=f"c{len(lp.calls)}", usage=L.Usage())
    lp._call = _call
    lp._ledger = lambda card, *a, **k: lp.ledger_rows.append((card, k.get("status")))
    lp._afford = lambda *a, **k: True
    lp._aux_ok = lambda *a, **k: True
    return lp


def test_reprompt_once_and_second_need_ignored(tmp_path):
    from nano import loop as L
    code = "HYPOTHESIS: h\nCHANGE: c\nFIDELITY: exact\n```python\nx = 1\n```"
    lp = _stub_loop(tmp_path, ["NEED: a second fact after the re-prompt\n" + code])
    first = types.SimpleNamespace(text="HYPOTHESIS: h\nNEED: what is the ratio of first fit?\nNEED: and of best fit online?\n"
                                       "NEED: and a third one over cap", call_id="c0", usage=L.Usage())
    r, parsed, refetched = lp._handle_needs(first, None, "PROMPT", "implement", "k1", "", None, 1, "first", 1000,
                                            {"card": "implement"})
    assert refetched and r.call_id != "c0" and "x = 1" in r.text          # the re-prompted reply is the one built
    gens = [c for c in lp.calls if c[0] == "generate"]
    assert len(gens) == 1 and "FACTS YOU ASKED FOR" in gens[0][2] and "https://example.org/ff" in gens[0][2]
    assert sum(1 for c in lp.calls if c[1] == "fetch_fact") == 2                   # the cap: two fetches, not three
    s = lp.fetch_stats
    assert (s["requests"], s["answered"], s["reprompts"], s["over_cap"], s["ignored_after_reprompt"]) == (2, 2, 1, 1, 1)
    assert any(d.get("action") == "ignored_after_reprompt" for d in lp.decisions)
    assert ("implement", "need") in lp.ledger_rows                                 # the request call is on the ledger


def test_need_with_code_is_built_and_only_logged(tmp_path):
    from nano import loop as L
    lp = _stub_loop(tmp_path, [])
    text = "HYPOTHESIS: h\nCHANGE: c\nFIDELITY: exact\nNEED: a fact I would like\n```python\nx = 1\n```"
    r = types.SimpleNamespace(text=text, call_id="c0", usage=L.Usage())
    out, parsed, refetched = lp._handle_needs(r, {"source": "x = 1"}, "P", "revise", "fix", "", None, 1, "revise", 1000, {"card": "revise"})
    assert out is r and parsed and not refetched and lp.calls == []
    assert lp.fetch_stats["logged_only"] == 1 and lp.fetch_stats["requests"] == 0


def test_default_off_without_web():
    from nano import loop as L
    assert L.fetch_on_demand_default(None, "off") is False
    assert L.fetch_on_demand_default(None, "delegate") is True and L.fetch_on_demand_default(None, "self") is True
    assert L.fetch_on_demand_default(False, "delegate") is False and L.fetch_on_demand_default(True, "off") is True


def test_mock_run_fetches_and_reports(monkeypatch):
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", config.VENV_PYTHON, raising=False)     # the CPU scorer runs on the lab's python
    dry_run._need_sent.clear()
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", "mock-gap-d", "--implement", "2",
                                      "--rounds", "1", "--max-sketch-calls", "8"])
    try:
        dry_run.main()
    finally:
        llm.set_mock(None)
    run = next(config.RUNS_DIR.glob("mock-gap-d__*"))
    rows = [json.loads(x) for x in (run / "facts_fetched.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert len(rows) == 1 and rows[0]["answer"] and rows[0]["source_url"].startswith("https://") and rows[0]["tag"] == "web"
    ff = json.loads((run / "report.json").read_text(encoding="utf-8"))["fetched_facts"]
    assert (ff["requests"], ff["answered"], ff["reprompts"]) == (1, 1, 1)
    ledger = Path(config.LEDGER_PATH).read_text(encoding="utf-8")
    assert '"card": "impl:refetch"' in ledger and '"card": "fetch_fact"' in ledger
