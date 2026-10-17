"""Tests for llm.py spend accounting and schemas.py JSONL helpers (review fixes): usage is
charged on error paths and summed over retries, timeouts are charged by estimate, the CLI JSON
parser takes the last result object and the larger of usage / modelUsage, output caps are
logged, and concurrent JSONL appends never tear lines."""
from __future__ import annotations

import json
import threading
from pathlib import Path

import pytest

from harness import config, llm
from harness.schemas import Usage, append_jsonl, read_jsonl


@pytest.fixture(autouse=True)
def _reset():
    yield
    llm.set_mock(None)


def test_error_with_usage_is_charged(tmp_path):
    def fn(prompt, role, meta):
        raise llm.CallError("claude -p returned error: error_max_turns", usage=Usage(1200, 300, 0, 0))
    llm.set_mock(fn)
    res = llm.call("hello", role="generate", backend="mock", log_dir=tmp_path, retries=0)
    assert res.error and "error_max_turns" in res.error
    assert res.usage.total_tokens == 1500 and res.text == ""
    rec = json.loads((tmp_path / f"{res.call_id}.json").read_text(encoding="utf-8"))
    assert rec["total_tokens"] == 1500 and rec["error"]


def test_usage_summed_across_retry_attempts(monkeypatch):
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)
    calls = {"n": 0}

    def fn(prompt, role, meta):
        calls["n"] += 1
        if calls["n"] < 3:
            raise llm.CallError("overloaded 529", usage=Usage(100, 10, 0, 0))
        return "final reply"
    llm.set_mock(fn)
    res = llm.call("p" * 40, role="generate", backend="mock", retries=2)
    assert res.error is None and res.text == "final reply" and res.attempts == 3
    # two failed attempts (110 each) plus the successful one (10 input + 2 output)
    assert res.usage.total_tokens == 2 * 110 + (10 + len("final reply") // 4)
    assert len(res.attempt_errors) == 2


def test_timeout_is_charged_by_estimate(monkeypatch):
    monkeypatch.setattr(llm.time, "sleep", lambda s: None)

    def fn(prompt, role, meta):
        raise llm.CallError("Timeout after 1s (process tree killed)", estimated=True)
    llm.set_mock(fn)
    res = llm.call("x" * 400, role="judge", backend="mock", max_tokens=1200, retries=1)
    assert res.error and res.usage_estimated
    # mock backend: no CLI overhead; two attempts each charged prompt/4 + max_tokens
    assert res.usage.total_tokens == 2 * (100 + 1200)
    assert res.max_tokens == 1200


def test_parse_cli_json_takes_last_result_object():
    out = ('warning {not json}\n{"type":"system","foo":1}\n'
           '{"type":"result","result":"hi","usage":{"input_tokens":5,"output_tokens":2},"is_error":false}\n'
           'trailing text')
    data = llm.parse_cli_json(out)
    assert data["result"] == "hi"
    with pytest.raises(llm.CallError):
        llm.parse_cli_json("no braces here")


def test_cli_usage_prefers_larger_model_usage_sum():
    data = {"usage": {"input_tokens": 10, "output_tokens": 5},
            "modelUsage": {"claude-a": {"inputTokens": 10, "outputTokens": 5},
                           "claude-haiku": {"inputTokens": 300, "outputTokens": 20}}}
    u, info = llm.cli_usage(data)
    assert u.total_tokens == 335 and info["source"] == "modelUsage"
    u2, info2 = llm.cli_usage({"usage": {"input_tokens": 10, "output_tokens": 5}})
    assert u2.total_tokens == 15 and info2["source"] == "usage"


def test_cli_command_has_no_shell_and_passes_output_cap(monkeypatch):
    seen = {}

    class _Proc:
        returncode = 0
        pid = 1

        def communicate(self, inp, timeout=None):
            seen["input"] = inp
            return ('{"result":"ok","usage":{"input_tokens":3,"output_tokens":1}}', "")

    def popen(cmd, **kw):
        seen["cmd"], seen["kw"] = cmd, kw
        return _Proc()
    monkeypatch.setattr(llm.subprocess, "Popen", popen)
    text, usage, raw = llm._call_cli("prompt", "sonnet", 777, None, 5, 1)
    assert text == "ok" and usage.total_tokens == 4
    assert seen["kw"]["shell"] is False and seen["input"] == "prompt"
    assert seen["kw"]["env"]["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] == "32000"     # the cap sits well above max_tokens: no continuations
    assert "--tools" in seen["cmd"] and all(a in seen["cmd"] for a in config.CLI_EXTRA_ARGS)


def test_over_cap_logged(tmp_path):
    llm.set_mock(lambda p, r, m: "y" * 4000)        # 1000 output tokens
    res = llm.call("q", role="judge", backend="mock", max_tokens=100, log_dir=tmp_path)
    assert res.over_cap
    rec = json.loads((tmp_path / f"{res.call_id}.json").read_text(encoding="utf-8"))
    assert rec["over_cap"] is True and rec["max_tokens"] == 100


# ---------------------------------------------------------------- JSONL helpers
def test_append_jsonl_concurrent_writers_never_tear(tmp_path):
    p = tmp_path / "rows.jsonl"

    def worker(k):
        for i in range(400):
            append_jsonl(p, {"k": k, "i": i, "pad": "x" * 200})

    ts = [threading.Thread(target=worker, args=(k,)) for k in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    rows = read_jsonl(p, strict=True)
    assert len(rows) == 3200 and len({(r["k"], r["i"]) for r in rows}) == 3200


def test_read_jsonl_skips_torn_lines(tmp_path, capsys):
    p = tmp_path / "t.jsonl"
    p.write_text('{"a": 1}\n{"a": 2, "b": "tor\n{"a": 3}\n', encoding="utf-8")
    rows = read_jsonl(p)
    assert [r["a"] for r in rows] == [1, 3]
    assert "skipping undecodable line 2" in capsys.readouterr().err
    with pytest.raises(json.JSONDecodeError):
        read_jsonl(p, strict=True)
