"""N8: the pre-mortem's knowledge. (a) the research brief's published failures in the critic's default pack;
(b) --premortem-web: at most three questions of one shape, answered in one research call; (c) report.json "premortem"."""
from __future__ import annotations

import json
import sys
import threading
from types import SimpleNamespace

from harness import config, llm
from nano import deepen
from nano.loop import NanoLoop

BRIEF = {"failed": [{"name": f"trick {i}", "why": "no gain at 124M", "url": f"https://example.org/f{i}"} for i in range(15)]
         + [{"name": "own row", "why": "tried here", "url": "ledger://abc"}]}


def test_failed_pack_has_urls_cap_and_no_ledger_rows():
    pack = deepen.failed_pack(BRIEF)
    assert len(pack) == deepen.FAILED_CAP == 12
    assert all("https://example.org/f" in x for x in pack)
    assert not any("ledger://" in x for x in pack)
    assert deepen.failed_pack(None) == [] and deepen.failed_pack({}) == []
    p = deepen.premortem_prompt("idea", "mix", "- c1", "code", ["a fact"], failed=pack)
    assert "PUBLISHED FAILURES FOR THIS PART" in p and "https://example.org/f0" in p and "https://example.org/f11" in p
    assert "PUBLISHED FAILURES" not in deepen.premortem_prompt("idea", "mix", "- c1", "code", ["a fact"])


def test_no_creativity_nudges_in_premortem_prompts():
    texts = [deepen.premortem_prompt("idea", "mix", "- c", "code", []), deepen.premortem_questions_prompt("idea", "mix", "- c")]
    for t in texts:
        low = t.lower()
        assert not any(w in low for w in ("be creative", "creative", "bold", "wild", "unconventional", "you are a"))


def test_question_shape_and_cap():
    text = ("QUESTIONS:\n1. has gated attention been reported to fail or fade at small scale or under short training?\n"
            "2. what is the best optimizer?\n"
            "3. has value residual learning been reported to fail or fade at small scale?\n"
            "4. has QK norm been reported to fail or fade under a high learning rate?\n"
            "5. has relu squared been reported to fail or fade at small scale or under bf16?\n")
    qs = deepen.parse_premortem_questions(text)
    assert len(qs) == 3
    assert all(q.lower().startswith("has ") and "been reported to fail or fade" in q and q.endswith("?") for q in qs)
    assert not any("optimizer" in q for q in qs)
    assert deepen.parse_premortem_questions("NONE") == []


def test_cite_field_parsed():
    pm = deepen.parse_premortem("OBJECTIONS:\n- fades past 1k steps | severity: high | class: early_only | if_true: trend above 0 | cite: Q2\n"
                                "- costs a matmul | severity: low | class: hidden_cost | if_true: step_ratio above 1.2\nVERDICT: fades")
    assert pm["objections"][0]["cite"] == "Q2" and pm["objections"][1]["cite"] == ""


def _fake(web: bool, critic_reply: str):
    calls = []

    def _call(prompt, role, max_tokens, meta, model=None, tools=None, max_turns=None, timeout=None):
        calls.append({"prompt": prompt, "role": role, "card": meta["card"], "model": model, "tools": tools})
        text = critic_reply if meta["card"] == "premortem_web:questions" else "FINDINGS:\n1. fades below 100M https://arxiv.org/abs/1\n2. no source found."
        return SimpleNamespace(text=text, call_id="c" + str(len(calls)), usage=None)

    fake = SimpleNamespace(premortem_web=web, premortem_web_questions=0, lock=threading.Lock(), research_model="cheap",
                           _aux_ok=lambda note="": True, _afford=lambda *a, **k: True, _call=_call, _ledger=lambda *a, **k: None)
    return fake, calls


def test_web_flag_asks_at_most_three_questions_in_one_research_call():
    reply = "QUESTIONS:\n" + "\n".join(f"{i}. has mechanism {i} been reported to fail or fade at small scale or under condition {i}?"
                                       for i in range(1, 6))
    fake, calls = _fake(True, reply)
    qs, findings = NanoLoop._premortem_web(fake, {"cluster_id": "k1", "name": "gate", "node": "mix"}, {"name": "mix"},
                                           "idea", "- c", "", 1)
    assert len(qs) == 3 and fake.premortem_web_questions == 3
    research_calls = [c for c in calls if c["role"] == "research"]
    assert len(research_calls) == 1 and research_calls[0]["model"] == "cheap" and research_calls[0]["tools"]
    assert "Q1:" in findings and "https://arxiv.org/abs/1" in findings
    p = deepen.premortem_prompt("idea", "mix", "- c", "code", [], findings=findings)
    assert deepen.WEB_FINDINGS_HEADER in p and "cite: Q<n>" in p


def test_web_flag_off_makes_no_call():
    fake, calls = _fake(False, "")
    assert NanoLoop._premortem_web(fake, {"cluster_id": "k1", "name": "g"}, {}, "idea", "- c", "", 1) == ([], "")
    assert calls == []


def test_summary_fields():
    objs = [{"idea": "a", "text": "x", "status": "confirmed", "cite": "Q1"}, {"idea": "a", "text": "x", "status": "pending"},
            {"idea": "a", "text": "y", "status": "refuted"}, {"idea": "b", "text": "x", "status": "refuted"},
            {"idea": "b", "text": "z", "status": "untestable"}]
    s = deepen.premortem_summary(objs, True, 2)
    assert s["objections"] == 4 and s["confirmed"] == 1 and s["refuted"] == 2 and s["untestable"] == 1
    assert s["confirmed_share"] == round(1 / 3, 3)
    assert s["web"] == "on" and s["web_questions"] == 2 and s["web_cited_objections"] == 1
    assert deepen.premortem_summary([], False)["confirmed_share"] is None


def test_mock_run_default_pack_and_report(monkeypatch):
    """One mock run, flag not given: the default pack carries the brief's failed entries with URLs; the web is off."""
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", config.VENV_PYTHON, raising=False)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--profile", "binpack_nobase", "--batch", "mock-n8", "--max-sketch-calls", "6",
                                      "--implement", "1", "--rounds", "1"])
    try:
        assert dry_run.main() == 0
    finally:
        llm.set_mock(None)
    run = next(p for p in config.RUNS_DIR.iterdir() if p.name.startswith("mock-n8__"))
    briefs = [json.loads(p.read_text(encoding="utf-8")) for p in (run / "research").glob("*.json") if "_analogy" not in p.name]
    urls = {e["url"] for b in briefs for e in b.get("failed", []) if str(e.get("url", "")).startswith("http")}
    prompts = [p.read_text(encoding="utf-8") for p in (run / "prompts").glob("*.txt")]
    pm = [t for t in prompts if t.startswith("Pre-mortem. Assume")]
    assert pm
    assert urls
    assert all("PUBLISHED FAILURES FOR THIS PART" in t and any(u in t for u in urls) for t in pm)
    assert not any(t.startswith("Pre-mortem, step one") for t in prompts)       # off by default: no questions asked
    rep = json.loads((run / "report.json").read_text(encoding="utf-8"))["premortem"]
    assert {"objections", "confirmed_share", "web", "web_questions", "web_cited_objections"} <= set(rep)
    assert rep["web"] == "off" and rep["web_questions"] == 0
