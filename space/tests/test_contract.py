"""P0 contract checks (docs/MULTIPLAYER_DESIGN.md sections 6.1 and 12.1). No network, no model, no lab root."""
from __future__ import annotations

import ast
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from space import contract as C
from space import control, digest

ROOT = Path(__file__).resolve().parents[2]
SPACE = ROOT / "space"
KERNEL = [SPACE / "__init__.py", SPACE / "contract.py", SPACE / "control.py", SPACE / "digest.py",
          SPACE / "web" / "contract.json", SPACE / "tests" / "__init__.py", SPACE / "tests" / "test_contract.py",
          SPACE / "tests" / "test_control_merge.py", SPACE / "tests" / "test_digest.py"]


def test_export_round_trip_equals_committed_json(tmp_path):
    env = {**os.environ, "PYTHONPATH": str(ROOT)}
    out = subprocess.run([sys.executable, "-m", "space.contract"], cwd=str(tmp_path), env=env,
                         capture_output=True, timeout=60, check=True).stdout.decode("ascii")
    committed = (SPACE / "web" / "contract.json").read_text(encoding="ascii").replace("\r\n", "\n")
    assert out.replace("\r\n", "\n") == committed
    assert json.loads(out) == json.loads(committed) == json.loads(json.dumps(C.export()))
    assert committed == json.dumps(C.export(), indent=1, sort_keys=True)


def test_export_shape():
    ex = C.export()
    assert ex["version"] == C.VERSION == 1
    assert set(ex["kinds"]) == set(C.KINDS)
    assert ex["routes"]["post"] == ["POST", "/api/events"]
    assert ex["caps"] == {"digest": 1200, "note": 600, "quote": 160, "chat": 1500, "seed": 1500}
    assert ex["ttl"] == {"claim_s": 90.0, "presence_s": 20.0, "heartbeat_s": 5.0}
    assert ex["private_keys"] == ["obvious", "obvious_match", "private"]


def test_kinds_day_one():
    assert len(C.KINDS) == 37
    assert C.DAY_ONE == tuple(C.KINDS)
    assert C.SERVER_ONLY == {"space_opened", "claim_granted", "claim_released", "claim_expired", "claim_taken_over"}
    for name in ("GUARDED", "IDEA_SKIPS", "GLOBAL_KINDS", "NO_DIGEST", "HUMAN_KINDS", "TEAM_KINDS"):
        assert getattr(C, name) <= set(C.KINDS), name
    classes = {"person", "delegate", "team", "server"}
    for kind, (writers, data, ckey, tier, sentence) in C.KINDS.items():
        assert set(writers.split()) <= classes, kind
        assert isinstance(data, tuple) and all(isinstance(k, str) for k in data), kind
        assert tier in (None, 0, 1, 2, 3), kind


def test_every_kind_has_a_sentence_or_is_in_no_digest():
    for kind, v in C.KINDS.items():
        assert (v[4] is None) == (kind in C.NO_DIGEST) == (v[3] is None), kind


def test_every_sentence_placeholder_is_filled():
    known = {"label", "parent", "frame", "count", "n", "severity", "text", "kind", "verdict", "node", "status",
             "metric", "n_added", "by", "score", "note", "value", "fact", "reason", "tag", "why", "owner_was"}
    for kind in C.KINDS:
        assert set(digest.placeholders(kind)) <= known, kind


def test_control_keys():
    ckeys = {v[2] for v in C.KINDS.values() if v[2]}
    assert ckeys <= set(C.CONTROL_KEYS) | set(control.SIDE_KEYS)
    assert not set(C.CONTROL_KEYS) & set(C.FILE_ONLY_KEYS)
    out = control.merge([], file_ctl={"budget_add": 5, "note": "x", "bogus": 1})
    assert set(out["control"]) <= set(C.CONTROL_KEYS) | set(C.FILE_ONLY_KEYS)
    assert set(C.CONTROL_KEYS) <= set(out["control"])


def test_closing_lines_cover_every_role():
    assert set(C.CLOSING) == set(C.ROLES)
    assert "{first}" in C.DIGEST_HEAD and "{last}" in C.DIGEST_HEAD


def test_actor_class_table_of_section_4_2():
    assert C.actor_class("ana", "human", "ana") == "person"
    assert C.actor_class("ana.agent", "agent", "ana") == "delegate"
    assert C.actor_class("team.loop", "system", "team") == "team"
    assert C.actor_class("team.bridge", "system", "team") == "team"
    assert C.actor_class("team.loop2", "agent", "team.loop2") == "team"      # the by prefix wins
    assert C.actor_class("bot", "agent", "bot") == "agent"
    assert C.actor_class("server", "system", "server") == "server"


def test_guard_applies_only_to_an_agent_that_acts_for_nobody():
    assert C.guard_applies("bot", "agent", "bot", "sketch_batch")
    assert not C.guard_applies("bot", "agent", "bot", "node_added")           # not a guarded kind
    assert not C.guard_applies("ana.agent", "agent", "ana", "reply_posted")   # a delegate
    assert not C.guard_applies("ana", "human", "ana", "reply_posted")         # a person
    assert not C.guard_applies("team.loop", "system", "team", "sketch_batch")  # the team mirror
    assert not C.guard_applies("team.loop2", "agent", "team.loop2", "test_result")


def test_constants_of_section_6_1():
    assert C.BASE_URL == "http://127.0.0.1:8766"
    assert C.STAGES == ("planned", "ideated", "clustered", "deepened", "built", "verified")
    assert C.CLAIM_TTL_S == 90.0 and C.PRESENCE_TTL_S == 20.0
    assert C.DIGEST_CAP == 1200 and C.NOTE_CAP == 600 and C.NOTES_KEPT == 5 and C.QUOTE_CAP == 160
    assert set(C.WINNER_WORD) == set(C.STATUS_WORDS)


def test_kernel_files_are_ascii():
    for p in KERNEL:
        assert all(b < 128 for b in p.read_bytes()), p


def test_kernel_imports_only_the_standard_library():
    std = set(sys.stdlib_module_names) | {"space", "__future__"}
    for p in KERNEL:
        if p.suffix != ".py" or p.parent.name == "tests":
            continue
        tree = ast.parse(p.read_text(encoding="ascii"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [a.name for a in node.names]
            elif isinstance(node, ast.ImportFrom):
                names = [node.module or ""]
            else:
                continue
            for n in names:
                assert n.split(".")[0] in std, (p.name, n)


def test_contract_is_section_6_1_verbatim():
    doc = (ROOT / "docs" / "MULTIPLAYER_DESIGN.md").read_text(encoding="utf-8")
    m = re.search(r"### 6\.1 .*?```python\n(.*?)```", doc, flags=re.S)
    assert m, "section 6.1 code block not found in docs/MULTIPLAYER_DESIGN.md"
    assert (SPACE / "contract.py").read_text(encoding="ascii").replace("\r\n", "\n") == m.group(1)
