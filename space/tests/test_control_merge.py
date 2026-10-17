"""The 12 merge rules of docs/MULTIPLAYER_DESIGN.md section 6.2, overlay_file and render_control_json.
Every test builds raw envelopes by hand (section 4.1). No server, no network, no lab root."""
from __future__ import annotations

import json
import os
import random
import threading
import time

import pytest

from space.contract import CONTROL_KEYS, FILE_ONLY_KEYS
from space.control import consume_step, merge, overlay_file, render_control_json

_seq = [0]


def ev(kind, by="ana", data=None, subject=None, seq=None, **extra):
    """One envelope. by_kind and owner follow section 4.2 from the actor id."""
    if seq is None:
        _seq[0] += 1
        seq = _seq[0]
    if by == "server":
        by_kind, owner = "system", "server"
    elif by.startswith("team."):
        by_kind, owner = "system", "team"
    elif by.endswith(".agent"):
        by_kind, owner = "agent", by.split(".")[0]
    else:
        by_kind, owner = "human", by
    e = {"seq": seq, "ts": "2026-10-17T10:00:00.000Z", "kind": kind, "by": by, "by_kind": by_kind, "owner": owner,
         "subject": subject, "label": None, "data": dict(data or {}), "op": f"{by}-1-{seq}", "base": None,
         "round": None, "stage": None, "claim": None, "cause": None}
    e.update(extra)
    return e


def seqd(*events):
    """Number the events 1..n in the given order."""
    for i, e in enumerate(events, 1):
        e["seq"] = i
    return list(events)


# ---- rule 1: only people and delegates count; other loops' claims are the exception

def test_rule_1_only_person_and_delegate_events_count():
    evs = seqd(ev("node_skipped", "team.loop", subject="node:a"),
               ev("node_skipped", "bot", subject="node:b", by_kind="agent", owner="bot"),
               ev("note_posted", "team.bridge", {"text": "from the bridge"}),
               ev("node_skipped", "ana", subject="node:c"),
               ev("node_skipped", "ben.agent", subject="node:d"),
               ev("run_step", "ben.agent", {"round": 1, "stage": "planned"}))   # run_step: person only
    out = merge(evs)
    assert out["control"]["skip_nodes"] == ["c", "d"]
    assert out["control"]["note"] == ""
    assert out["steps"] == []
    assert out["refs"] == [4, 5]


def test_rule_1_other_loops_claims_add_and_release_removes():
    evs = seqd(ev("claim_granted", "server", {"owner": "team.loop2", "ttl_s": 90}, "node:x"),
               ev("claim_granted", "server", {"owner": "team.loop", "ttl_s": 90}, "node:mine"),   # this loop's own
               ev("claim_granted", "server", {"owner": "ana.agent", "ttl_s": 90}, "node:ana"),    # a delegate's
               ev("claim_granted", "server", {"owner": "team.loop2", "ttl_s": 90}, "node:y"),
               ev("claim_released", "server", {"owner": "team.loop2"}, "node:y"),
               ev("claim_granted", "team.loop2", {"owner": "team.loop2"}, "node:forged"))        # not the server
    out = merge(evs, loop="team.loop")
    assert out["control"]["skip_nodes"] == ["x"]
    assert out["refs"] == [1, 4, 5]
    out = merge(evs, loop="team.loop2")              # seen from the other loop: team.loop's claim is the other one
    assert out["control"]["skip_nodes"] == ["mine"]


def test_rule_1_expired_and_taken_over_claims():
    evs = seqd(ev("claim_granted", "server", {"owner": "team.loop2"}, "node:x"),
               ev("claim_expired", "server", {"owner_was": "team.loop2", "reason": "restart"}, "node:x"),
               ev("claim_granted", "server", {"owner": "ana"}, "node:z"),
               ev("claim_taken_over", "server", {"from": "ana", "to": "team.loop2"}, "node:z"),
               ev("claim_granted", "server", {"owner": "team.loop2"}, "node:w"),
               ev("claim_taken_over", "server", {"from": "team.loop2", "to": "ben"}, "node:w"))
    assert merge(evs)["control"]["skip_nodes"] == ["z"]


def test_rule_1_live_claims_list():
    claims = [{"subject": "node:p", "owner": "team.loop2"}, {"subject": "node:q", "owner": "ana.agent"},
              {"subject": "node:r", "owner": "team.loop"}]
    assert merge([], claims=claims)["control"]["skip_nodes"] == ["p"]
    rel = [ev("claim_released", "server", {"owner": "team.loop2"}, "node:p", seq=9)]
    assert merge(rel, claims=claims)["control"]["skip_nodes"] == []


# ---- rule 2: skip_nodes, latest per node, sorted, plus other loops' claims

def test_rule_2_skip_nodes_latest_wins_sorted_union():
    evs = seqd(ev("node_skipped", "ana", {"reason": "slow"}, "node:stats"),
               ev("node_skipped", "ben", {}, "node:open"),
               ev("node_unskipped", "ben.agent", {}, "node:open"),
               ev("node_skipped", "ana", {}, "node:ties"),
               ev("node_unskipped", "ana", {}, "node:ties"),
               ev("node_skipped", "ben", {}, "node:ties"),
               ev("claim_granted", "server", {"owner": "team.loop2"}, "node:choice"))
    random.Random(3).shuffle(evs)
    out = merge(evs)
    assert out["control"]["skip_nodes"] == ["choice", "stats", "ties"]


# ---- rule 3: veto, latest per question, sorted

def test_rule_3_veto_union_with_unveto():
    evs = seqd(ev("question_vetoed", "ana", {"question": "u3"}, "question:u3"),
               ev("question_vetoed", "ben", {"question": "u1"}, "question:u1"),
               ev("question_vetoed", "ana.agent", {"question": "u2"}, "question:u2"),
               ev("question_unvetoed", "ben", {"question": "u2"}, "question:u2"),
               ev("question_vetoed", "ana", {}, "question:u0"))                      # id from the subject
    out = merge(evs)
    assert out["control"]["veto"] == ["u0", "u1", "u3"]
    assert out["refs"] == [1, 2, 3, 4, 5]


# ---- rule 4: choose, highest seq; overwrote names the earlier choices of other authors

def test_rule_4_choose_highest_seq_and_overwrote():
    evs = seqd(ev("question_chosen", "ben", {"question": "ua"}),
               ev("question_chosen", "ana.agent", {"question": "ub"}),
               ev("question_chosen", "ana", {"question": "uc"}),
               ev("question_chosen", "ben", {"question": "ud"}))
    evs[0]["seq"], evs[3]["seq"] = 88, 90
    evs[1]["seq"], evs[2]["seq"] = 70, 89
    out = merge(evs)
    assert out["control"]["choose"] == "ud"
    assert out["overwrote"]["choose"] == [{"seq": 70, "by": "ana"}, {"seq": 89, "by": "ana"}]
    assert merge([])["control"]["choose"] is None and merge([])["overwrote"] == {"choose": []}


# ---- rule 5: the newest five notes, newest first, authors kept, 300 then 600 characters

def test_rule_5_notes_newest_five_with_authors_under_600():
    evs = seqd(*[ev("note_posted", "ana" if i % 2 else "ben.agent", {"text": f"note {i} " + "x" * 200})
                 for i in range(7)])
    note = merge(evs)["control"]["note"]
    lines = note.split("\n")
    assert len(note) <= 600
    assert lines[0].startswith("ben: note 6 ") and lines[1].startswith("ana: note 5 ")
    assert not any(ln.startswith(("ben: note 1 ", "ana: note 1 ", "ben: note 0 ")) for ln in lines)
    long = seqd(ev("note_posted", "ana", {"text": "y" * 900}))
    assert merge(long)["control"]["note"] == "ana: " + "y" * 300
    short = seqd(ev("note_posted", "ben", {"text": "check ties"}), ev("note_posted", "ana", {"text": "order first"}))
    assert merge(short)["control"]["note"] == "ana: order first\nben: check ties"


# ---- rule 6: one opinion per (owner, target), latest wins, candidate ids go under candidate

def test_rule_6_one_opinion_per_who_and_target():
    evs = seqd(ev("opinion_given", "ana", {"target": "best fit", "score": 4, "note": "meh"}),
               ev("opinion_given", "ana.agent", {"target": "best fit", "score": 7, "note": "fair and cheap"}),
               ev("opinion_given", "ben", {"target": "best fit", "score": 2}),
               ev("opinion_given", "ben", {"target": "n0123456789", "score": 9, "note": "fast"}))
    ops = merge(evs)["control"]["opinions"]
    assert ops == [{"cluster": "best fit", "score": 7, "note": "fair and cheap", "who": "ana"},
                   {"cluster": "best fit", "score": 2, "note": "", "who": "ben"},
                   {"candidate": "n0123456789", "score": 9, "note": "fast", "who": "ben"}]


# ---- rule 7: add_nodes, first id wins with by and by_seq, the second is dropped as id_taken

def test_rule_7_add_nodes_first_wins_second_dropped():
    spec = {"id": "Item Order!", "name": "item order", "parent": "root", "origin": "human", "frame": "how items are sorted",
            "assumptions": ["a"], "directions": ["inward", "outward"], "test": "t", "kind": "part"}
    evs = seqd(ev("node_added", "ana.agent", spec),
               ev("node_added", "ben", {**spec, "id": "itemorder", "name": "other"}),
               ev("node_added", "team.loop", {**spec, "id": "planned_one", "origin": "map"}),
               ev("node_added", "ben", {**spec, "id": "a_very_long_identifier_here"}),
               ev("node_added", "ben", {**spec, "id": "!!!"}))
    out = merge(evs)
    nodes = out["control"]["add_nodes"]
    assert [n["id"] for n in nodes] == ["itemorder", "a_very_long_iden"]
    assert nodes[0] == {**spec, "id": "itemorder", "by": "ana", "by_seq": 1}
    assert nodes[1]["by"] == "ben" and nodes[1]["by_seq"] == 4
    assert {"seq": 2, "reason": "id_taken"} in out["dropped"]
    assert {"seq": 5, "reason": "bad_id"} in out["dropped"]
    assert 2 not in out["refs"] and 3 not in out["refs"] and {1, 4} <= set(out["refs"])


# ---- rule 8: pause holds while any holder has not resumed

def test_rule_8_pause_holders():
    evs = seqd(ev("run_paused", "ana", {"reason": "look"}),
               ev("run_paused", "ben.agent", {}),
               ev("run_resumed", "ben", {}))
    out = merge(evs)
    assert out["control"]["pause"] is True and out["holders"] == ["ana"]
    evs.append(ev("run_resumed", "ana.agent", {}, seq=4))
    out = merge(evs)
    assert out["control"]["pause"] is False and out["holders"] == []
    assert out["refs"] == [1, 2, 3, 4]


# ---- rule 9: every run_step after since, in order, none dropped

def test_rule_9_steps_in_order_none_dropped():
    evs = seqd(ev("run_step", "ben", {"round": 1, "stage": "planned"}),
               ev("run_step", "ben", {"round": 1, "stage": "planned"}),
               ev("run_step", "ana", {"round": 1, "stage": "ideated"}),
               ev("run_step", "ana", {"round": 1, "stage": "clustered"}))
    random.Random(1).shuffle(evs)
    out = merge(evs, since=1)
    assert out["steps"] == [{"seq": 2, "round": 1, "stage": "planned", "by": "ben"},
                            {"seq": 3, "round": 1, "stage": "ideated", "by": "ana"},
                            {"seq": 4, "round": 1, "stage": "clustered", "by": "ana"}]
    assert out["refs"] == []                          # the merge does not know the boundary
    st = consume_step(out, 1, "ideated")              # the loop consumes the one for its boundary
    assert st["seq"] == 3 and out["refs"] == [3]
    assert consume_step(out, 2, "planned") is None and len(out["steps"]) == 3


def test_rule_9_round_from_envelope():
    evs = [ev("run_step", "ben", {"stage": "built"}, seq=7, round=2)]
    assert merge(evs)["steps"] == [{"seq": 7, "round": 2, "stage": "built", "by": "ben"}]


# ---- rule 10: disputes and seeds after since, in order

def test_rule_10_disputes_and_seeds():
    evs = seqd(ev("fact_disputed", "ana", {"node": "choice", "fact": "f0", "reason": "r0", "tag": "belief"}),
               ev("fact_disputed", "ben.agent", {"node": "choice", "fact": "f1", "reason": "r1", "tag": "measured"}),
               ev("seed_added", "ben", {"node": "ties", "text": "try reverse order"}),
               ev("fact_disputed", "ana", {"node": "open", "fact": "f2", "reason": "r2", "tag": "web"}))
    out = merge(evs, since=1)
    assert out["disputes"] == [{"seq": 2, "node": "choice", "fact": "f1", "reason": "r1", "tag": "measured", "by": "ben"},
                               {"seq": 4, "node": "open", "fact": "f2", "reason": "r2", "tag": "web", "by": "ana"}]
    assert out["seeds"] == [{"seq": 3, "node": "ties", "text": "try reverse order", "by": "ben"}]
    assert out["refs"] == [2, 3, 4]


# ---- rule 11: refs name every folded seq after since

def test_rule_11_refs_name_every_folded_seq():
    evs = seqd(ev("node_added", "ana", {"id": "item_order", "name": "item order", "parent": "root", "origin": "human"}),
               ev("note_posted", "ben", {"text": "ties first"}),
               ev("question_vetoed", "ana.agent", {"question": "u1"}),
               ev("vote_cast", "ben", {"idea": "c1", "value": 1}),               # display only: not folded
               ev("chat_posted", "ana", {"to": "ana.agent", "text": "hi"}),      # not a control kind
               ev("opinion_given", "ben", {"target": "best fit", "score": 6}),
               ev("run_paused", "ana", {}),
               ev("fact_disputed", "ben", {"node": "choice", "fact": "f", "reason": "r", "tag": "belief"}),
               ev("seed_added", "ana", {"node": "ties", "text": "s"}),
               ev("question_chosen", "ben", {"question": "u2"}),
               ev("node_skipped", "ana", {}, "node:stats"),
               ev("run_step", "ben", {"round": 1, "stage": "planned"}))
    out = merge(evs)
    assert out["refs"] == [1, 2, 3, 6, 7, 8, 9, 10, 11]
    consume_step(out, 1, "planned")
    assert out["refs"] == [1, 2, 3, 6, 7, 8, 9, 10, 11, 12]
    later = merge(evs, since=9)                       # level keys still hold; refs only for the new events
    assert later["refs"] == [10, 11]
    assert later["control"]["note"] == "ben: ties first" and later["control"]["veto"] == ["u1"]
    assert later["control"]["add_nodes"][0]["id"] == "item_order"
    assert later["disputes"] == [] and later["seeds"] == []


# ---- rule 12: file-only keys pass through; a server key replaces the file key

def test_rule_12_file_only_keys_pass_server_keys_replace():
    file_ctl = {"budget_add": 500, "k_impl": 3, "stop_after_stage": "built", "exclude_clusters": ["x"],
                "note": "from the file", "skip_nodes": ["file_skip"], "veto": ["uf"], "choose": "uf", "pause": True,
                "opinions": [{"cluster": "f"}], "add_nodes": [{"id": "fromfile"}], "unknown_key": 1}
    evs = seqd(ev("note_posted", "ana", {"text": "from the server"}))
    ctl = merge(evs, file_ctl=file_ctl)["control"]
    for k in ("budget_add", "k_impl", "stop_after_stage", "exclude_clusters"):
        assert ctl[k] == file_ctl[k]
    assert ctl["note"] == "ana: from the server" and ctl["skip_nodes"] == [] and ctl["veto"] == []
    assert ctl["choose"] is None and ctl["pause"] is False and ctl["opinions"] == [] and ctl["add_nodes"] == []
    assert "unknown_key" not in ctl
    assert set(ctl) == set(CONTROL_KEYS) | {"budget_add", "k_impl", "stop_after_stage", "exclude_clusters"}


def test_merge_sorts_unsorted_input_and_tolerates_junk():
    evs = seqd(ev("node_skipped", "ana", {}, "node:a"), ev("node_unskipped", "ana", {}, "node:a"))
    assert merge(list(reversed(evs)))["control"]["skip_nodes"] == []
    junk = [None, "x", {"kind": "note_posted"}, {"seq": 5, "kind": "nope", "by": "ana", "by_kind": "human"},
            {"seq": 6, "kind": "note_posted", "by": "ana", "by_kind": "human", "data": None}]
    out = merge(junk)
    assert out["control"]["note"] == "ana: " and out["refs"] == [6]


def test_merge_output_shape_matches_section_6_2():
    out = merge([])
    assert set(out) == {"control", "refs", "steps", "holders", "disputes", "seeds", "overwrote", "dropped"}
    assert list(out["control"]) == list(CONTROL_KEYS)
    json.dumps(out)


# ---- overlay_file

def test_overlay_file_takes_file_only_keys_from_disk():
    server = merge(seqd(ev("node_skipped", "ana", {}, "node:s")))
    file_ctl = {"budget_add": 500, "skip_nodes": ["ignored"], "note": "ignored", "leap_share": 0.2}
    ctl = overlay_file(server["control"], file_ctl)
    assert ctl["budget_add"] == 500 and ctl["leap_share"] == 0.2
    assert ctl["skip_nodes"] == ["s"] and ctl["note"] == ""
    assert "budget_add" not in server["control"]                       # a new dict, the input is untouched
    whole = overlay_file(server, file_ctl)                              # a whole merge result works too
    assert whole["control"] == ctl and whole["refs"] == server["refs"]
    stale = overlay_file({**server["control"], "budget_add": 100, "k_impl": 2}, {"budget_add": 500})
    assert stale["budget_add"] == 500 and "k_impl" not in stale        # the disk is the only source
    assert overlay_file(server["control"], None) == server["control"]
    assert set(FILE_ONLY_KEYS) & set(overlay_file({}, {k: 1 for k in FILE_ONLY_KEYS})) == set(FILE_ONLY_KEYS)


# ---- render_control_json

def test_render_control_json_writes_and_replaces(tmp_path):
    p = tmp_path / "control.json"
    render_control_json(p, {"note": "a", "skip_nodes": ["x"]})
    assert json.loads(p.read_text(encoding="ascii")) == {"note": "a", "skip_nodes": ["x"]}
    render_control_json(str(p), {"note": "b"})
    assert json.loads(p.read_text(encoding="ascii")) == {"note": "b"}
    assert not (tmp_path / "control.json.tmp").exists()


@pytest.mark.skipif(os.name != "nt", reason="an open reader blocks os.replace only on Windows")
def test_render_control_json_retries_under_an_open_reader(tmp_path):
    p = tmp_path / "control.json"
    render_control_json(p, {"note": "old"})
    opened, done = threading.Event(), threading.Event()

    def hold():
        with open(p, "rb"):
            opened.set()
            time.sleep(0.4)
        done.set()

    t = threading.Thread(target=hold)
    t.start()
    opened.wait(5)
    t0 = time.perf_counter()
    render_control_json(p, {"note": "new"})
    took = time.perf_counter() - t0
    t.join(5)
    assert done.is_set()
    assert 0.2 < took < 3.0                           # it waited for the reader, then wrote
    assert json.loads(p.read_text(encoding="ascii")) == {"note": "new"}


@pytest.mark.skipif(os.name != "nt", reason="an open reader blocks os.replace only on Windows")
def test_render_control_json_gives_up(tmp_path):
    p = tmp_path / "control.json"
    render_control_json(p, {"note": "old"})
    with open(p, "rb"):
        t0 = time.perf_counter()
        with pytest.raises(PermissionError):
            render_control_json(p, {"note": "new"}, retries_ms=20, give_up_s=0.3)
        assert time.perf_counter() - t0 < 2.0
    assert json.loads(p.read_text(encoding="ascii")) == {"note": "old"}
    assert not (tmp_path / "control.json.tmp").exists()
