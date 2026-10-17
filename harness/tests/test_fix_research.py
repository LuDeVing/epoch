"""Fix pass 2026-10-17, research items: N3 (a whole-problem reading call before the map, --no-preread control),
I4 (ledger rows go to parts only and never make a research or adapt card), I5 (no web brief or analogy call for
the off-map pseudo-node or question nodes), I9 (research cache key), F6 (fact-check verdicts reach the memory,
append-only), E3/I7 (no persona text in the research prompts).

Two mock dry runs (stopped after ideation, baseline measurement stubbed); everything else is unit level."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace

import yaml

from harness import config

REPO = Path(__file__).resolve().parents[2]

PREREAD_REPLY = ("PARTS:\n- attention: how tokens mix https://arxiv.org/abs/1706.03762\n"
                 "- optimization: the update rule and schedule https://arxiv.org/abs/2010.04245\n"
                 "an unsourced line that must be dropped\n"
                 "WEAK SPOTS:\n- the schedule matters more than it looks https://example.org/sched\n")


def _run(monkeypatch, batch: str, extra: list[str]):
    from nano import dry_run, loop as L

    def light_profile(self):                     # no baseline measurement: ideation only needs the text
        self.diagnostics_text = "measured: validation loss 6.63 at 45 steps; step time 0.12 s"
        return {"params_nonembed": 21_000_000, "step_s": 0.12, "smoke_loss_first": 10.8, "smoke_loss_last": 6.6,
                "smoke_steps": 12}
    monkeypatch.setattr(L.NanoLoop, "_load_profile", light_profile)
    base = dry_run.mock

    def mock(prompt, role, meta):
        if meta.get("card") == "preread":
            return PREREAD_REPLY
        return base(prompt, role, meta)
    monkeypatch.setattr(dry_run, "mock", mock)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--batch", batch, "--max-sketch-calls", "40", "--implement", "1",
                                      "--rounds", "1", "--stop-after", "ideated", "--no-diagnostics"] + extra)
    dry_run.main()
    run_dir = next(p for p in config.RUNS_DIR.iterdir() if p.name.startswith(batch + "__"))
    st = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    ideas = [json.loads(x) for x in (run_dir / "ideas.jsonl").read_text(encoding="utf-8").splitlines()] \
        if (run_dir / "ideas.jsonl").exists() else []
    prompts = [p.read_text(encoding="utf-8") for p in (run_dir / "prompts").glob("*.txt")]
    return run_dir, st.get("decisions", []), ideas, prompts


def test_preread_feeds_the_planner_and_offtree_gets_no_research(monkeypatch):
    run_dir, dec, ideas, prompts = _run(monkeypatch, "mock-fix-research", [])
    pre = [d for d in dec if d.get("step") == "preread"]
    assert pre and pre[0]["source"] == "web" and pre[0]["sourced_lines"] == 3, pre
    saved = json.loads((run_dir / "preread.json").read_text(encoding="utf-8"))
    assert "unsourced" not in saved["text"] and len(saved["urls"]) == 3
    planner = [t for t in prompts if t.startswith("Decompose the following problem")]
    assert planner and "WHAT THE FIELD SAYS ABOUT THIS PROBLEM" in planner[0]
    if "HOW THE BASELINE BEHAVES" in planner[0]:
        assert planner[0].index("WHAT THE FIELD SAYS") < planner[0].index("HOW THE BASELINE BEHAVES")
    # the preread runs before the planner, the per-part research after it
    order = sorted((p.stat().st_mtime_ns, p.read_text(encoding="utf-8")[:40]) for p in (run_dir / "prompts").glob("*.txt"))
    first = [t for _, t in order]
    i_pre = next(i for i, t in enumerate(first) if t.startswith("Read what is known"))
    i_plan = next(i for i, t in enumerate(first) if t.startswith("Decompose the following"))
    i_part = next(i for i, t in enumerate(first) if t.startswith("Research ONE part"))
    assert i_pre < i_plan < i_part
    # I5: the off-map pseudo-node gets no brief and no analogy call
    files = {p.name for p in (run_dir / "research").glob("*.json")}
    assert files and not any(f.startswith("offtree") for f in files), files
    assert not any(s.get("node") == "offtree" and s.get("card") in ("research", "analogy", "adapt") for s in ideas)
    assert not any("PART UNDER STUDY: " + "off the map" in t.lower() for t in prompts)


def test_no_preread_and_no_research_deal_no_research_contexts(monkeypatch):
    from nano import version as V
    led = config.MEMORY_DIR / "experiments" / "ledger.jsonl"
    led.parent.mkdir(parents=True, exist_ok=True)
    rows = [{"run": f"night{i}", "cand_id": f"c{i}", "hypothesis": f"earlier hypothesis number {i} about the schedule",
             "status": "verified", "delta": -0.01, "n_seeds": 3, "baseline_version": V.baseline_version()} for i in range(4)]
    led.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")
    run_dir, dec, ideas, prompts = _run(monkeypatch, "mock-fix-research-off", ["--no-research", "--no-preread"])
    pre = [d for d in dec if d.get("step") == "preread"]
    assert pre and pre[0]["source"] == "off"
    assert not (run_dir / "preread.json").exists()
    assert not any("WHAT THE FIELD SAYS ABOUT THIS PROBLEM" in t for t in prompts)
    # I4: ledger rows alone are memory, not research: no research or adapt contexts, no KNOWN TECHNIQUES from ledger://
    assert ideas
    assert not any(s.get("card") in ("research", "adapt") for s in ideas), sorted({s.get("card") for s in ideas})
    assert not any("KNOWN TECHNIQUES FOR THIS PART" in t for t in prompts)
    # the ledger reached parts only
    briefs = {p.stem for p in (run_dir / "research").glob("*.json")}
    assert briefs and "offtree" not in briefs and "root" not in briefs


def _fake_loop(tree_nodes, run_dir):
    from nano import loop as L
    f = SimpleNamespace(tree=tree_nodes, skip_nodes=set(), only_nodes=None, briefs={}, run_dir=run_dir,
                        baseline_version="v1", lens="parts")
    for name in ("_skipped", "_researchable", "inject_ledger", "_research_key", "_literature_known"):
        setattr(f, name, getattr(L.NanoLoop, name).__get__(f))
    return f


def test_question_and_offtree_nodes_get_no_ledger_brief(tmp_path):
    led = config.MEMORY_DIR / "experiments" / "ledger.jsonl"
    led.parent.mkdir(parents=True, exist_ok=True)
    led.write_text(json.dumps({"run": "night1", "cand_id": "c1", "hypothesis": "an earlier idea", "status": "fail",
                               "delta": 0.01, "n_seeds": 3, "baseline_version": "v1"}) + "\n", encoding="utf-8")
    nodes = [{"id": "root", "name": "", "parent": None}, {"id": "attn", "name": "attention", "parent": "root"},
             {"id": "q_attn", "name": "why did it fail", "parent": "attn", "kind": "question"},
             {"id": "offtree", "name": "off the map", "parent": "root"}]
    (tmp_path / "research").mkdir()
    f = _fake_loop(nodes, tmp_path)
    assert [n["id"] for n in nodes if f._researchable(n)] == ["attn"]
    f.inject_ledger(nodes)
    assert set(f.briefs) == {"attn"}
    assert f.briefs["attn"]["failed"][0]["url"].startswith("ledger://")
    assert f._literature_known("attn") == []
    f.briefs["attn"]["known"] = [{"name": "lit", "url": "https://x.org"}, {"name": "mine", "url": "ledger://r/c"}]
    assert [e["name"] for e in f._literature_known("attn")] == ["lit"]


def test_cache_key_holds_profile_lens_baseline_and_frame():
    from nano import research
    node = {"id": "attn", "frame": "softmax attention over 1024 tokens", "assumptions": ["a1"], "boundary": "Block"}
    k = research.cache_key(node, "llm", "parts", "v1")
    assert k.startswith("attn__") and k == research.cache_key(dict(node), "llm", "parts", "v1")
    others = {research.cache_key(node, "binpack_nobase", "parts", "v1"), research.cache_key(node, "llm", "dataflow", "v1"),
              research.cache_key(node, "llm", "parts", "v2"), research.cache_key({**node, "frame": "linear attention"}, "llm", "parts", "v1"),
              research.cache_key({**node, "assumptions": ["a2"]}, "llm", "parts", "v1")}
    assert k not in others and len(others) == 5


def test_merge_facts_keeps_the_verdict_and_appends(tmp_path):
    from nano import research
    cache = tmp_path / "research"
    research.save_cache(cache, {"node": "attn", "known": [], "failed": [], "open": [], "backend": "cli_json"}, "attn__k")
    brief_bytes = (cache / "attn__k.json").read_bytes()
    facts = [{"text": "QK-norm gave -0.02 loss at 124M https://a.org/1", "prov": "web", "check": "supported", "check_quote": "q"},
             {"text": "gating gave -0.5 loss at 21M https://b.org/2", "prov": "web", "check": "not supported", "check_quote": "page says 0.05"},
             {"text": "I think this works https://c.org/3", "prov": "belief"},
             "plain string fact 1.5x faster https://d.org/4"]
    assert research.merge_facts(cache, "attn__k", facts, run="r1") == 3
    assert research.merge_facts(cache, "attn__k", facts, run="r2") == 0          # dedup
    assert (cache / "attn__k.json").read_bytes() == brief_bytes                  # the brief is never rewritten
    rows = research.read_facts(cache, "attn__k")
    assert [r["check"] for r in rows] == ["supported", "not supported", ""]
    assert all(r["run"] == "r1" and r["url"].startswith("https://") and r["prov"] for r in rows)
    research.merge_facts(cache, "attn__k", ["new fact 2% https://e.org/5"], run="r3")
    assert len(research.read_facts(cache, "attn__k")) == 4                       # appended, earlier rows kept
    d = research.load_cached(cache, "attn__k", 7)
    known_urls = [e["url"] for e in d["known"]]
    assert "https://b.org/2" not in known_urls and "https://a.org/1" in known_urls
    assert [x["url"] for x in d["disputed"]] == ["https://b.org/2"]
    assert "b.org" not in research.brief_text(d)
    assert research.merge_facts(cache, "missing", facts) == 0


def test_preread_parse_and_block():
    from nano import research
    pre = research.parse_preread(PREREAD_REPLY)
    assert pre["n_sourced"] == 3 and "unsourced" not in pre["text"] and pre["text"].startswith("PARTS:")
    assert research.parse_preread("PARTS:\n- one line https://a.org\nno url here") is None
    assert len(research.parse_preread("\n".join(f"- p{i} https://a.org/{i} " + "x" * 200 for i in range(100)))["text"]) <= research.PREREAD_CHARS
    blk = research.preread_block(pre)
    assert "WHAT THE FIELD SAYS ABOUT THIS PROBLEM" in blk and "measurements win" in blk
    assert research.preread_block(None) == ""
    assert "Do not propose changes" in research.preread_prompt("make it better")


def test_research_prompts_carry_no_persona():
    from nano import research
    pats = yaml.safe_load((REPO / "harness" / "lint_patterns.yaml").read_text(encoding="utf-8"))["fail"]
    persona = [re.compile(p["pattern"], re.I) for p in pats if p["id"].startswith("persona")]
    node = {"id": "attn", "name": "attention", "frame": "softmax", "assumptions": ["a"]}
    texts = [research.research_prompt(node, "goal"), research.analogy_prompt(node, "goal"),
             research.findings_prompt(["what is known about x at small scale?"], "attention"),
             research.fetch_prompt("the eps of RMSNorm", node), research.preread_prompt("goal"),
             research.QUESTIONS_ADDENDUM, research.FINDINGS_HEADER, research.preread_block({"text": "x"})]
    for t in texts:
        hits = [p.pattern for p in persona if p.search(t)]
        assert not hits, (hits, t[:120])
    src = (REPO / "nano" / "research.py").read_text(encoding="utf-8")
    assert not re.search(r"\bYou\s+are\b", src)          # the persona opener; "facts you are unsure of" is not one
