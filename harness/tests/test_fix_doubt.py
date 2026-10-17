"""Fix 3: the doubt card comes after reading (measure, map, read, then doubt).

Mock runs of the loop through nano.dry_run, stopped after ideation, with the baseline measurement stubbed
so nothing is trained: with research on, doubt cards are dealt and their prompts carry the literature block,
and DOUBT: lines land on the sketches and in disputed_facts.jsonl; with --no-research, round 1 deals no doubt
card and the decision says why."""
from __future__ import annotations

import json
import sys

from harness import config


def _run(monkeypatch, batch: str, extra: list[str]):
    from nano import dry_run, loop as L

    def light_profile(self):                     # no baseline measurement: ideation only needs the text
        self.diagnostics_text = "measured: validation loss 6.63 at 45 steps; step time 0.12 s"
        return {"params_nonembed": 21_000_000, "step_s": 0.12, "smoke_loss_first": 10.8, "smoke_loss_last": 6.6,
                "smoke_steps": 12}
    monkeypatch.setattr(L.NanoLoop, "_load_profile", light_profile)

    base = dry_run.mock

    def mock(prompt, role, meta):                # the doubt card answers with a DOUBT: line per sketch
        text = base(prompt, role, meta)
        if meta.get("card") == "sketch:doubt":
            text = "\n\n".join("DOUBT: optimization: the map says the schedule is fine; https://arxiv.org/abs/2010.04245 disagrees\n" + b
                               for b in text.split("\n\n"))
        return text
    monkeypatch.setattr(dry_run, "mock", mock)
    monkeypatch.setattr(sys, "argv", ["dry_run", "--batch", batch, "--max-sketch-calls", "12", "--implement", "1",
                                      "--rounds", "1", "--stop-after", "ideated", "--no-diagnostics"] + extra)
    dry_run.main()
    run_dir = next(p for p in config.RUNS_DIR.iterdir() if p.name.startswith(batch + "__"))
    st = json.loads((run_dir / "state.json").read_text(encoding="utf-8"))
    return run_dir, [d for d in st.get("decisions", []) if d.get("step") == "doubt_cards"]


def test_doubt_cards_read_the_literature(monkeypatch):
    run_dir, dec = _run(monkeypatch, "mock-fix-doubt", [])
    assert dec and dec[0]["dealt"] >= 1, dec
    assert dec[0]["reason"].startswith("briefs for ")
    prompts = [p.read_text(encoding="utf-8") for p in (run_dir / "prompts").glob("*.txt")]
    doubt = [t for t in prompts if "DOUBT THE MAP" in t]
    assert doubt
    for t in doubt:
        assert "WHAT THE LITERATURE SAYS ABOUT THIS MAP (from the research briefs):" in t
        assert "you are the first to compare the two" in t
        assert "https://" in t.split("WHAT THE LITERATURE SAYS")[1]
    blank_or_gaps = [t for t in prompts if "NO MAP:" in t or "WHAT DID THE MAP MISS?" in t]
    assert all("WHAT THE LITERATURE SAYS" not in t for t in blank_or_gaps)
    ideas = [json.loads(l) for l in (run_dir / "ideas.jsonl").read_text(encoding="utf-8").splitlines()]
    doubted = [s for s in ideas if s.get("card") == "doubt"]
    assert doubted and all(s.get("doubt", "").startswith("optimization:") for s in doubted)
    rows = [json.loads(l) for l in (run_dir / "disputed_facts.jsonl").read_text(encoding="utf-8").splitlines()]
    assert {r["sketch_id"] for r in rows} == {s["id"] for s in doubted}
    assert all(r["round"] == 1 and r["node"] == "opt" and "arxiv" in r["text"] for r in rows)


def test_no_doubt_before_reading(monkeypatch):
    run_dir, dec = _run(monkeypatch, "mock-fix-doubt-noread", ["--no-research"])
    assert dec and dec[0]["dealt"] == 0, dec
    assert "briefs for 0 of" in dec[0]["reason"] and "waits" in dec[0]["reason"]
    off = [d for d in json.loads((run_dir / "state.json").read_text(encoding="utf-8"))["decisions"] if d.get("step") == "off_tree"]
    assert off and off[0]["off_map"] >= 1                     # the off-map count is unchanged: blank and gaps fill it
    prompts = [p.read_text(encoding="utf-8") for p in (run_dir / "prompts").glob("*.txt")]
    assert not any("DOUBT THE MAP" in t for t in prompts)
    assert not (run_dir / "disputed_facts.jsonl").exists()
