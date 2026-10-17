"""The loop side of the shared space (docs/MULTIPLAYER_DESIGN.md sections 6.9 to 6.11, 7 and 12.1 row P2).

Every test runs in the test's temp lab on the mock backend against harness/tests/fixtures/space_fake_server.py (a
stdlib server in a thread on a free 127.0.0.1 port), never against the real space server. At most one mock dry run
runs at a time (they run one after the other in this file); nothing trains a model or touches the GPU.
"""
from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path

import pytest

from harness import config, llm
from nano import loop as L
from nano import profile as PF
from nano import prompt_style as PS

HERE = Path(__file__).resolve().parent
DIGEST_HEAD = "WHAT TEAMMATES CHANGED"


def _fake_module():
    spec = importlib.util.spec_from_file_location("space_fake_server", HERE / "fixtures" / "space_fake_server.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


FS = _fake_module()


@pytest.fixture(autouse=True)
def _style_reset():
    PS.reset()
    yield
    PS.reset()


def _loop(batch: str, resume: bool = False) -> L.NanoLoop:
    PF.set_current("binpack_nobase")
    lp = L.NanoLoop(batch, 0, "mock", 100_000, 2, 60.0, None)
    lp.resume = resume
    return lp


def _space(lp, url, step=False, poll=0.2):
    from nano.space import LoopSpace
    lp.space = LoopSpace(lp, url, "team.loop", step=step, poll_s=poll)
    lp.poll_s = poll
    return lp.space


def _closed_port() -> int:
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port


def _cards(run: Path) -> dict:
    """prompt file stem -> the call's card (from calls/<id>.json)."""
    out = {}
    for f in (run / "calls").glob("*.json"):
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except ValueError:
            continue
        out[f.stem] = str((d.get("meta") or {}).get("card", ""))
    return out


def _prompts(run: Path, pred) -> list[str]:
    cards = _cards(run)
    return [p.read_text(encoding="utf-8") for p in (run / "prompts").glob("*.txt") if pred(cards.get(p.stem, ""))]


# ---------------------------------------------------------------- the 2-round dry run on the fake server, step mode
class _Driver(threading.Thread):
    """Plays Ben at the Go button: a run_step for every boundary the loop waits at. At planned r1 it first presses Go
    for the wrong boundary and checks that the loop stays put; it disputes a fact before the ideated Go and vetoes the
    first previewed question before the verified Go."""

    def __init__(self, fs):
        super().__init__(daemon=True)
        self.fs, self.stop, self.log = fs, threading.Event(), {"held": None, "veto": None, "dispute": None, "wrong": None, "steps": []}

    def run(self):
        seen = 0
        while not self.stop.is_set():
            evs = self.fs.store.snapshot()
            for e in evs[seen:]:
                if e["by"] != "team.loop":
                    continue
                d = e["data"]
                if e["kind"] == "question_preview" and self.log["veto"] is None and d.get("top3"):
                    q = d["top3"][0]["id"]
                    self.fs.post("question_vetoed", {"question": q, "text": d["top3"][0].get("text", "")},
                                 by="ana", subject=f"question:{q}", label=d["top3"][0].get("text", "")[:80])
                    self.log["veto"] = q
                if e["kind"] == "stage_entered" and d.get("waiting"):
                    r, stg = d["round"], d["stage"]
                    if (r, stg) == (1, "planned"):
                        wrong = self.fs.post("run_step", {"round": 1, "stage": "ideated"}, by="ben")    # the wrong boundary
                        self.log["wrong"] = wrong["seq"]
                        time.sleep(1.2)                                                        # six polls at 0.2 s
                        after = [x for x in self.fs.store.snapshot() if x["by"] == "team.loop" and x["seq"] > e["seq"]]
                        self.log["held"] = not after
                    if (r, stg) == (1, "ideated"):
                        r_ = self.fs.post("fact_disputed", {"node": "choice", "fact": "the first open bin is always best",
                                                            "reason": "best fit beat it on seed 0", "tag": "measured"},
                                          by="ana", subject="node:choice", label="choice")
                        self.log["dispute"] = r_["seq"]
                    st = self.fs.post("run_step", {"round": r, "stage": stg}, by="ben")
                    self.log["steps"].append((r, stg, st["seq"]))
            seen = len(evs)
            time.sleep(0.05)


def test_dry_run_with_space_step_mode(monkeypatch):
    from nano import dry_run
    from nano.checks import script
    monkeypatch.setattr(script, "PY", Path(sys.executable))     # the temp lab has no venv: score with this python
    procs = []
    real_popen = subprocess.Popen

    class _Popen(real_popen):
        def __init__(self, args, *a, **k):
            first = (args[0] if isinstance(args, (list, tuple)) and args else str(args).split(" ")[0])
            procs.append(Path(str(first)).stem.lower())       # the program started (never the paths it is given)
            super().__init__(args, *a, **k)
    monkeypatch.setattr(subprocess, "Popen", _Popen)

    with FS.FakeSpace() as fs:
        node = fs.post("node_added", {"id": "item_order", "name": "item order", "parent": "root", "origin": "human",
                                      "frame": "how items are sorted before packing", "assumptions": [],
                                      "directions": ["inward", "outward"]}, by="ana", subject="node:item_order",
                       label="item order")
        note = fs.post("note_posted", {"text": "check tie-breaking before the choice rule"}, by="ben")
        drv = _Driver(fs)
        drv.start()
        argv = ["dry_run", "--batch", "space-t", "--profile", "binpack_nobase", "--implement", "2", "--rounds", "2",
                "--max-sketch-calls", "12", "--space", fs.url, "--step", "--control-poll-seconds", "0.2"]
        monkeypatch.setattr(sys, "argv", argv)
        t0 = time.perf_counter()
        try:
            assert dry_run.main() == 0
        finally:
            llm.set_mock(None)
            drv.stop.set()
        wall = time.perf_counter() - t0
        evs = fs.store.snapshot()
    assert wall < 300, f"the run took {wall:.0f} s"
    assert "claude" not in procs, "a claude process was started"
    run = next(config.RUNS_DIR.glob("space-t__*"))
    loop_evs = [e for e in evs if e["by"] == "team.loop"]

    # every boundary was entered, waited at and released in order
    stages = [(e["data"]["round"], e["data"]["stage"]) for e in loop_evs if e["kind"] == "stage_entered"]
    want = [(1, "planned")] + [(r, s) for r in (1, 2) for s in ("ideated", "clustered", "deepened", "built", "verified")]
    assert stages == want
    assert all(e["data"]["waiting"] for e in loop_evs if e["kind"] == "stage_entered")
    assert drv.log["held"] is True, "a run_step for the wrong boundary released the loop"

    # the human events before the planned Go are folded at planned r1, and the receipt names exactly them
    applied = [e for e in loop_evs if e["kind"] == "control_applied"]
    first = applied[0]
    assert (first["data"]["round"], first["data"]["stage"]) == (1, "planned")
    step_seqs = {s for _, _, s in drv.log["steps"]}
    planned_go = next(s for r, stg, s in drv.log["steps"] if (r, stg) == (1, "planned"))
    assert planned_go in first["data"]["refs"] and drv.log["wrong"] not in first["data"]["refs"]
    assert set(first["data"]["refs"]) - step_seqs == {node["seq"], note["seq"]}
    assert "item_order" in first["data"]["keys"]["add_nodes"]
    pt = json.loads((run / "problem_tree.json").read_text(encoding="utf-8"))
    io = next(n for n in pt["nodes"] if n["id"] == "item_order")
    assert io["origin"] == "human" and io["by"] == "ana"
    assert any(e["kind"] == "sketch_batch" and e["data"]["node"] == "item_order" and e["data"]["round"] == 1 for e in loop_evs)

    # the veto set before the verified Go acts at the round-2 pick; the preview came first
    q = drv.log["veto"]
    assert q, "no question was previewed"
    nq = json.loads((run / "next_questions.json").read_text(encoding="utf-8"))
    assert nq["round"] == 2 and q in nq["vetoed"]
    prev = next(e for e in loop_evs if e["kind"] == "question_preview")
    pick2 = next(e for e in loop_evs if e["kind"] == "question_picked" and e["data"]["round"] == 2)
    assert prev["seq"] < pick2["seq"] and q in pick2["data"]["vetoed"]

    # the dispute before the ideated Go is in disputed_facts.jsonl and on the node from the next round
    rows = [json.loads(x) for x in (run / "disputed_facts.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    mine = [r for r in rows if r.get("sketch_id") == f"e{drv.log['dispute']}"]
    assert mine and mine[0]["node"] == "choice" and "disputed by ana" in mine[0]["text"]
    choice = next(n for n in pt["nodes"] if n["id"] == "choice")
    assert any(d.get("sketch_id") == f"e{drv.log['dispute']}" for d in choice.get("disputed") or [])

    # digests: receipts by team.loop under the cap; builders read it; idea agents (no A/B flag) and blind stages never
    taken = [e for e in loop_evs if e["kind"] == "digest_taken"]
    assert taken and all(e["data"]["chars"] <= 1200 for e in taken)
    assert {"builder", "critic"} <= {e["data"]["role"] for e in taken}
    assert any(DIGEST_HEAD in p for p in _prompts(run, lambda c: c in ("implement", "revise")))
    assert not any(DIGEST_HEAD in p for p in _prompts(run, lambda c: c.startswith("sketch:")))
    assert not any(DIGEST_HEAD in p for p in _prompts(run, lambda c: c in ("cluster", "merge", "prior", "panel")))

    # nothing private leaves the loop
    blob = json.dumps(evs)
    assert '"obvious"' not in blob and "obvious_match" not in blob
    assert not any("obvious_match" in p or "obvious" in p for p in _prompts(run, lambda c: True))
    mode = json.loads((run / "space_mode.json").read_text(encoding="utf-8"))
    assert mode == {"space": fs.url, "actor": "team.loop", "step": True}
    assert not (run / "space_outbox.ndjson").exists() or not (run / "space_outbox.ndjson").read_text().strip()


def test_peer_digest_ideation_puts_the_digest_in_idea_prompts(monkeypatch):
    """The A/B flag: with --peer-digest-ideation the idea agents read the digest (a short run, stopped after ideation)."""
    from nano import dry_run
    with FS.FakeSpace() as fs:
        fs.post("note_posted", {"text": "try sorting the items first"}, by="ana")
        monkeypatch.setattr(sys, "argv", ["dry_run", "--batch", "space-ab", "--profile", "binpack_nobase", "--implement", "1",
                                          "--rounds", "1", "--max-sketch-calls", "4", "--stop-after", "ideated",
                                          "--space", fs.url, "--peer-digest-ideation", "--control-poll-seconds", "0.2"])
        try:
            assert dry_run.main() == 0
        finally:
            llm.set_mock(None)
        evs = fs.store.snapshot()
    run = next(config.RUNS_DIR.glob("space-ab__*"))
    ideas = _prompts(run, lambda c: c.startswith("sketch:") and not c.endswith(":questions"))
    assert ideas and all(DIGEST_HEAD in p and "try sorting the items first" in p for p in ideas)
    assert any(e["kind"] == "digest_taken" and e["data"]["role"] == "idea" for e in evs)


# ---------------------------------------------------------------- offline: closed port, outbox, one flush
def test_closed_port_keeps_every_stage_fast_and_flushes_once():
    lp = _loop("space-offline")
    sp = _space(lp, f"http://127.0.0.1:{_closed_port()}")
    lp.tree = [dict(n) for n in PF.current().tree]
    lp.sketches = [{"id": f"s{i:010x}", "idea": f"idea {i}", "node": "choice", "direction": "inward", "card": "seeded",
                    "kind": "port", "round": 1} for i in range(7)]
    for name in ("planned", "ideated", "clustered"):
        t0 = time.perf_counter()
        lp._stage(1, name)
        assert time.perf_counter() - t0 < 4.0, f"_stage {name} took too long with the server down"
    n_out = sp.client.outbox_count()
    assert n_out >= 3 + len(lp.tree)                       # three stage_entered, the map, the sketches
    ops = [json.loads(x)["op"] for x in (lp.run_dir / "space_outbox.ndjson").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert len(set(ops)) == len(ops) == n_out
    with FS.FakeSpace() as fs:
        sp.client.base = fs.url
        sp.client.reset_down()
        assert sp.client.flush_outbox() == n_out
        assert sp.client.flush_outbox() == 0                 # emptied: a second flush posts nothing
        sp.client._to_outbox([json.loads(x) for x in [json.dumps({"op": ops[0], "kind": "stage_entered", "data": {}})]])
        sp.client.flush_outbox()                             # a repeated op: the server dedupes it
        assert len(fs.store.snapshot()) == len(set(ops))


# ---------------------------------------------------------------- resume: a budget_add is applied once
def test_resume_applies_a_budget_add_once():
    with FS.FakeSpace() as fs:
        lp = _loop("space-resume")
        _space(lp, fs.url)
        b0 = lp.B
        (lp.run_dir / "control.json").write_text(json.dumps({"budget_add": 500}), encoding="utf-8")
        lp._stage(1, "planned")
        assert lp.B == b0 + 500
        ca = json.loads((lp.run_dir / "control_applied.json").read_text(encoding="utf-8"))
        assert ["budget_add", "500"] in ca["applied"]

        back = _loop("space-resume", resume=True)
        back.load_state()
        _space(back, fs.url)
        assert back.B == b0                                 # restored at the first boundary, not before the commitments
        back._stage(1, "ideated")                            # control.json still says 500: not applied a second time
        assert back.B == b0 + 500
        back._stage(1, "clustered")
        assert back.B == b0 + 500


def test_without_space_nothing_changes():
    lp = _loop("space-off")
    lp._stage(1, "planned")
    lp._stage(1, "ideated")
    for f in ("space_mode.json", "space_outbox.ndjson", "space_cursor.json", "control_applied.json"):
        assert not (lp.run_dir / f).exists()
    assert lp._peer("builder", "choice") == "" and lp._builder_slot("choice", "x") == ""


def test_adopt_space_is_not_built(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["loop", "--profile", "binpack_nobase", "--batch", "x", "--adopt-space"])
    assert L.main() == 2
    assert "not built" in capsys.readouterr().out


def test_step_mode_waits_for_its_own_boundary_and_honours_pause():
    with FS.FakeSpace() as fs:
        lp = _loop("space-step")
        _space(lp, fs.url, step=True, poll=0.05)
        fs.post("run_paused", {"reason": "look"}, by="ana")
        fs.post("run_step", {"round": 1, "stage": "planned"}, by="ben")
        done = threading.Event()
        th = threading.Thread(target=lambda: (lp._stage(1, "planned"), done.set()), daemon=True)
        th.start()
        time.sleep(0.4)
        assert not done.is_set(), "a Go while a person holds a pause released the loop"
        fs.post("run_resumed", {}, by="ana")
        assert done.wait(5.0)
        ap = [e for e in fs.events("control_applied")]
        assert len(ap) == 1 and ap[0]["data"]["stage"] == "planned"
        # a second press at planned cannot release ideated
        fs.post("run_step", {"round": 1, "stage": "planned"}, by="ben")
        done.clear()
        th = threading.Thread(target=lambda: (lp._stage(1, "ideated"), done.set()), daemon=True)
        th.start()
        time.sleep(0.4)
        assert not done.is_set()
        fs.post("run_step", {"round": 1, "stage": "ideated"}, by="ben")
        assert done.wait(5.0)


def test_seed_before_round_one_is_dealt_and_a_late_one_is_logged():
    with FS.FakeSpace() as fs:
        lp = _loop("space-seed")
        _space(lp, fs.url)
        fs.post("seed_added", {"node": "choice", "text": "pack the largest item first"}, by="ana")
        lp._stage(1, "planned")
        assert lp.owner_seeds and lp.owner_seeds[-1]["text"] == "pack the largest item first"
        lp.contexts_by_node[1] = {"choice": 1}
        fs.post("seed_added", {"node": "choice", "text": "a late one"}, by="ana")
        lp._stage(1, "ideated")
        assert any(d.get("step") == "seed_late" for d in lp.decisions)
        assert len(lp.owner_seeds) == 1


def test_prompt_style_is_fixed_once_and_v1_leaves_commitments_alone():
    PS.set_style("v1")
    PS.set_style("v1")
    with pytest.raises(ValueError):
        PS.set_style("v2")
    PS.reset()
    lp = _loop("space-style")
    (lp.run_dir / "problem.md").write_text("GOAL\n\nHARD CONSTRAINTS:\n- x\n", encoding="utf-8")
    lp._write_commitments()
    assert "prompt_style" not in json.loads((lp.run_dir / "commitments.json").read_text(encoding="utf-8"))
    PS.set_style("v2")
    lp._write_commitments()
    assert json.loads((lp.run_dir / "commitments.json").read_text(encoding="utf-8"))["prompt_style"] == "v2"
    assert PS.pick("a", "b") == "b"
    assert PS.notes_block_v2([{"name": "ana", "time": "10:02", "text": "check ties"}]).endswith('- ana, 10:02: "check ties"')
    assert PS.comments_block_v2([]) == "" and PS.changes_block_v2([], []) == "" and PS.parts_block_v2([]) == ""


def test_v2_disputed_block_names_the_person():
    from nano import tree
    PF.set_current("binpack_nobase")
    node = dict(next(n for n in PF.current().tree if n["id"] == "choice"))
    node["disputed"] = [{"round": 1, "text": "an agent doubt", "sketch_id": "s0000000001"},
                        {"round": 1, "text": "x (disputed by ana: y [measured])", "sketch_id": "e7"}]
    p = tree.node_prompt(node, "inward", "C\n")
    assert PS.swap_disputed_block(p, {"id": "z"}) == p                    # nothing disputed: unchanged
    q = PS.swap_disputed_block(p, node, {"e7": {"fact": "first fit is best", "by": "ana", "reason": "seed 0", "tag": "measured"}})
    assert tree.DISPUTED_HEAD not in q and PS.DISPUTED_HEAD_V2 in q
    assert '- first fit is best | disputed by ana: "seed 0" [measured]' in q
    assert "- an agent doubt (disputed, re-measure before relying on it)" in q
    assert q.index("first fit is best") < q.index("an agent doubt")        # newest first, as today
