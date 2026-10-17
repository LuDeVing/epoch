"""The docs check (docs/MULTIPLAYER_DESIGN.md section 12.3): docs/check_space_docs.py on the real docs, and each
check on a small bad input so a broken rule is caught. No network, no model, no lab root."""
from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[2]


def _load():
    spec = importlib.util.spec_from_file_location("check_space_docs", REPO / "docs" / "check_space_docs.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


D = _load()


def test_the_docs_check_passes_on_the_real_docs(capsys):
    res = D.run_all()
    bad = {k: v for k, v in res.items() if v}
    assert not bad, "\n".join(f"{k}: {x}" for k, v in bad.items() for x in v)
    assert D.main() == 0
    assert "docs check: all passed" in capsys.readouterr().out


def test_every_contract_route_and_every_start_run_route_is_in_the_guide():
    from space import contract as C
    text = (REPO / "docs" / "SPACE.md").read_text(encoding="utf-8")
    for _k, (_m, path) in C.ROUTES.items():
        if path != "/":
            assert path in text
    launch = (REPO / "space" / "launch.py").read_text(encoding="utf-8")
    runs = D.launch_routes(launch)
    assert runs == {"/api/run/profiles", "/api/run/estimate", "/api/run/start", "/api/run/status", "/api/run/stop"}
    for r in runs:
        assert r in text


def test_route_check_catches_an_unknown_route_and_a_missing_one():
    routes = {"events": ("GET", "/api/events"), "memory": ("GET", "/api/memory")}
    bad = D.check_routes("see /api/events and /api/teleport", "/api/events /api/memory", "x /api/events /api/memory",
                         "", routes)
    assert any("/api/teleport" in b for b in bad)
    assert any("/api/memory is missing from docs/SPACE.md" in b for b in bad)


def test_kind_check_both_ways():
    kinds = {"node_added": (), "note_posted": ()}
    md = "## Every kind\n\n| Kind | x |\n|---|---|\n| `node_added` | a |\n| `vote_magic` | b |\n\n## Next\n| `note_posted` | c |\n"
    bad = D.check_kinds(md, kinds)
    assert any("vote_magic" in b for b in bad)
    assert any("note_posted" in b and "does not list" in b for b in bad)
    assert D.check_kinds("no table here", kinds)


def test_emit_check_reads_literal_kinds_of_emit_and_ev_calls():
    src = 'c.emit("node_added", x)\nself._ev( "made_up_kind", s)\nemit(kind)\n'
    assert D.emitted_kinds(src) == {"node_added", "made_up_kind"}
    bad = D.check_emits({"nano/space.py": src}, {"node_added": ()})
    assert bad == ["nano/space.py emits made_up_kind, which is not in contract.KINDS"]


def test_contract_json_check():
    assert D.check_contract_json('{"a": 1}', {"a": 1}) == []
    assert D.check_contract_json('{"a": 2}', {"a": 1})
    assert D.check_contract_json("not json", {"a": 1})


@pytest.mark.parametrize("ch", [chr(0x2014), chr(0x2013), chr(0xE9)])
def test_ascii_check_catches_dashes_and_non_ascii(ch):
    assert D.check_ascii("x.md", "fine line\nbad " + ch + " line\n") != []
    assert D.check_ascii("x.md", "plain ASCII - with a hyphen\n") == []


def test_link_check(tmp_path):
    (tmp_path / "there.md").write_text("x", encoding="utf-8")
    text = "[a](there.md) [b](there.md#part) [c](missing.md) [d](https://example.com) [e](#local)"
    assert D.check_links("doc.md", text, tmp_path) == ["doc.md links to missing.md, which does not exist"]


def test_control_key_check_looks_only_inside_the_three_functions():
    src = ("def _stage(self):\n    ctl.get('note')\n\ndef _pick_question(self):\n    '''obeys `veto`'''\n\n"
           "def other():\n    ctl.get('pause')\n")
    assert D.check_control_keys(src, ("note", "veto")) == []
    assert D.check_control_keys(src, ("pause",)) == [
        "control key pause does not appear in nano/loop.py _stage/_pick_question/_opinions_for"]


def test_action_check_wants_the_registry_order_and_every_slash_command():
    from space import actions as A
    from space import contract as C
    md = (REPO / "docs" / "SPACE.md").read_text(encoding="utf-8")
    assert D.doc_actions(md) == [a[0] for a in A.ACTIONS]
    assert D.check_actions(md, A.ACTIONS, C.SLASH) == []
    assert D.check_actions(md.replace("`/seed", "`seed"), A.ACTIONS, C.SLASH) == [
        "docs/SPACE.md does not document the slash command /seed"]


def test_runbook_check_names_every_beat_with_its_time():
    design = (REPO / "docs" / "MULTIPLAYER_DESIGN.md").read_text(encoding="utf-8")
    beats = D.design_beats(design)
    times = [t for t, _ in beats]
    assert times[0] == "0:00" and times[-1] == "3:50" and len(beats) == 15
    assert "/branch" in D.beat_tokens(dict(beats)["0:15"])
    assert D.beat_tokens("Go (deepened r1), then Go (built r1)") == ["Go (deepened r1)", "Go (built r1)"]
    runbook = (REPO / "docs" / "DEMO_RUNBOOK.md").read_text(encoding="utf-8")
    assert D.check_runbook(runbook, beats) == []
    cut = "\n".join(line for line in runbook.splitlines() if not line.startswith("| 1:45 |"))
    assert any("1:45" in b for b in D.check_runbook(cut, beats))
