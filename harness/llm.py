"""LLM call layer with three backends: cli_json (claude -p), messages_api (anthropic SDK), mock.

Every model call in the harness goes through `call()`. It returns text plus exact usage so
the driver and the harness can charge every token (ARCHITECTURE.md section 8, Cost).

Isolation at P0: no tools for any role. The CLI backend runs with --tools "" and --max-turns 1
(measured overhead about 3k tokens per call) plus config.CLI_EXTRA_ARGS (safe mode: no
CLAUDE.md, hooks, plugins or MCP servers); the API backend has no tools; the runner, not the
model, executes candidate programs (formal card, exec_feedback = final-only).

Spend accounting rules of this module:
- usage is parsed before any error is raised, and an error carries it (CallError.usage);
- call() sums the usage of every attempt, failed ones included;
- a call that times out is charged a conservative estimate: prompt chars / 4 + the CLI
  overhead + the real output cap the backend was given (output_cap: on cli_json that is
  max(4 x max_tokens, 32000), not max_tokens), and the log record says usage_estimated = true;
- a timeout is retried at most once, and the reason is logged in retry_reasons; a second
  timeout ends the call (a call that timed out twice would most likely time out again);
- the CLI output cap is passed through CLAUDE_CODE_MAX_OUTPUT_TOKENS and every record logs
  max_tokens beside output_tokens (over_cap when the reply exceeded it).

Prompt length: a prompt over config.MAX_PROMPT_CHARS is cut in the middle with a visible
marker by fit_prompt (run_card.render_prompt applies it before writing prompts/<id>.txt, so
the file matches what was sent) and the record carries prompt_truncated. A CLI call without a
cwd runs in a fresh empty folder, never in the repo (no git context reaches the model).
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable

from . import config
from .schemas import Usage, new_id, write_json


class CallError(RuntimeError):
    """A backend error that still consumed tokens; `usage` is charged by call()."""

    def __init__(self, msg: str, usage: Usage | None = None, raw: dict | None = None,
                 estimated: bool = False):
        super().__init__(msg)
        self.usage = usage or Usage()
        self.raw = raw or {}
        self.estimated = estimated


@dataclass
class CallResult:
    call_id: str
    role: str
    backend: str
    model: str
    text: str
    usage: Usage
    cost_usd: float | None
    duration_ms: int
    stop_reason: str | None = None
    error: str | None = None
    attempts: int = 1
    raw_path: str | None = None
    max_tokens: int | None = None
    usage_estimated: bool = False          # a timeout was charged by estimate, not measured
    attempt_errors: list | None = None     # errors of retried attempts (usage already summed)
    retry_reasons: list | None = None      # why each retry was (or was not) made
    prompt_truncated: dict | None = None   # fit_prompt info when the prompt was cut

    @property
    def total_tokens(self) -> int:
        return self.usage.total_tokens

    @property
    def over_cap(self) -> bool:
        return bool(self.max_tokens) and self.usage.output_tokens > int(self.max_tokens)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["usage"] = self.usage.to_dict()
        d["total_tokens"] = self.total_tokens
        d["over_cap"] = self.over_cap
        return d


# ---------------------------------------------------------------- mock backend
MockFn = Callable[[str, str, dict], str]   # (prompt, role, meta) -> text
_mock_fn: MockFn | None = None
_mock_lock = threading.Lock()


def set_mock(fn: MockFn | None) -> None:
    """Install a mock responder for tests. fn(prompt, role, meta) returns the reply text; it
    may raise CallError(msg, usage=...) to simulate a backend error that consumed tokens."""
    global _mock_fn
    with _mock_lock:
        _mock_fn = fn


def _default_mock(prompt: str, role: str, meta: dict) -> str:
    """Deterministic canned replies so every module can be exercised without tokens."""
    if role in ("generate", "transform", "plain", "probe"):
        if meta.get("benchmark") == "arc":
            return ("1. ```python\ndef transform(grid):\n    return [row[:] for row in grid]\n```\n"
                    "2. ```python\ndef transform(grid):\n    return [row[::-1] for row in grid]\n```")
        return "1. A\n2. B\n3. C"
    if role == "judge":
        return '{"score": 3, "p": 0.5}'
    if role == "encode":
        return ("GOAL: solve the item.\nFACTS:\n1. fact one.\nRESOURCES:\n1. resource one.\n"
                "CHECKLIST:\n1. the answer must be consistent with every given example.")
    if role == "defaults":
        return "1. default one\n2. default two\n3. default three\n4. default four\n5. default five"
    if role == "verify":
        return "NO COUNTEREXAMPLE FOUND"
    if role == "converter":
        return "1. A"
    return "OK"


def _estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def output_cap(max_tokens: int, backend: str | None, thinking_budget: int | None = None) -> int:
    """The output cap the backend is really given for a call with this max_tokens. cli_json:
    max(4 x max_tokens, 32000) (see _call_cli); messages_api: max_tokens plus any thinking
    budget; mock: max_tokens. Timeouts are charged at this cap and estimators reserve it."""
    if backend in (None, "cli_json"):
        return max(int(max_tokens) * 4, 32000)
    if backend == "messages_api":
        return int(max_tokens) + int(thinking_budget or 0)
    return int(max_tokens)


def timeout_estimate(prompt: str, max_tokens: int, backend: str,
                     thinking_budget: int | None = None) -> Usage:
    """Conservative charge for a call that never returned a usage record: the prompt, the CLI
    overhead and the full output cap the backend was allowed to spend."""
    overhead = config.CLI_OVERHEAD_TOKENS_EST if backend == "cli_json" else 0
    return Usage(_estimate_tokens(prompt) + overhead, output_cap(max_tokens, backend, thinking_budget), 0, 0)


PROMPT_CUT_MARKER = ("\n\n[... {n} characters removed here by the harness: the prompt was over "
                     "its length cap ...]\n\n")


def fit_prompt(prompt: str, limit: int | None = None) -> tuple[str, dict | None]:
    """(prompt, info): a prompt over the cap is cut in the middle, keeping the head and the
    tail (the format instruction), with a marker that says how much was removed. info is None
    when nothing was cut."""
    limit = int(limit or config.MAX_PROMPT_CHARS)
    if len(prompt) <= limit:
        return prompt, None
    room = max(0, limit - len(PROMPT_CUT_MARKER.format(n=len(prompt))))
    head, tail = room // 2, room - room // 2
    removed = len(prompt) - head - tail
    out = prompt[:head] + PROMPT_CUT_MARKER.format(n=removed) + (prompt[-tail:] if tail else "")
    return out, {"original_chars": len(prompt), "sent_chars": len(out), "removed_chars": removed,
                 "limit": limit}


# ---------------------------------------------------------------- cost
def cost_usd(logical_model: str, usage: Usage) -> float | None:
    p = config.PRICE_PER_M.get(logical_model)
    if not p:
        return None
    return round((usage.input_tokens * p["input"] + usage.output_tokens * p["output"]
                  + usage.cache_read_input_tokens * p["cache_read"]
                  + usage.cache_creation_input_tokens * p["cache_create"]) / 1e6, 6)


# ---------------------------------------------------------------- CLI backend
def cli_binary() -> str:
    """Resolve config.CLI_BIN on PATH (also finds .cmd/.exe shims on Windows); the bare name
    when nothing resolves, so the error message names it."""
    return shutil.which(config.CLI_BIN) or config.CLI_BIN


def _kill_tree(proc: subprocess.Popen) -> None:
    """Kill the CLI and every descendant (a killed cmd/shim would otherwise leave the real
    process generating tokens with the pipes open)."""
    try:
        if os.name == "nt":
            subprocess.run(["taskkill", "/T", "/F", "/PID", str(proc.pid)], capture_output=True,
                           timeout=15)
        else:
            import signal
            os.killpg(os.getpgid(proc.pid), signal.SIGKILL)
    except Exception:  # noqa: BLE001 - best effort; fall through to proc.kill
        pass
    try:
        proc.kill()
    except OSError:
        pass


def _usage_from(u: dict) -> Usage:
    return Usage(int(u.get("input_tokens", u.get("inputTokens", 0)) or 0),
                 int(u.get("output_tokens", u.get("outputTokens", 0)) or 0),
                 int(u.get("cache_read_input_tokens", u.get("cacheReadInputTokens", 0)) or 0),
                 int(u.get("cache_creation_input_tokens", u.get("cacheCreationInputTokens", 0)) or 0))


def cli_usage(data: dict) -> tuple[Usage, dict]:
    """Usage of one claude -p JSON record: the larger of data["usage"] and the sum over
    data["modelUsage"] (which also lists background model calls), so nothing consumed goes
    uncharged. Returns (usage, {"usage": ..., "model_usage_sum": ..., "source": ...})."""
    main = _usage_from(data.get("usage") or {})
    per_model = data.get("modelUsage") or {}
    summed = Usage()
    for v in per_model.values():
        if isinstance(v, dict):
            summed = summed.add(_usage_from(v))
    info = {"usage": main.to_dict(), "model_usage_sum": summed.to_dict() if per_model else None,
            "source": "usage"}
    if per_model and summed.total_tokens > main.total_tokens:
        info["source"] = "modelUsage"
        return summed, info
    return main, info


def parse_cli_json(out: str) -> dict:
    """The last JSON object in the CLI's stdout (warnings may precede it; text may follow)."""
    dec = json.JSONDecoder()
    last = None
    i = out.find("{")
    while i >= 0:
        try:
            obj, end = dec.raw_decode(out, i)
        except json.JSONDecodeError:
            i = out.find("{", i + 1)
            continue
        if isinstance(obj, dict) and ("result" in obj or "usage" in obj or "is_error" in obj):
            last = obj
        i = out.find("{", end)
    if last is None:
        raise CallError(f"no JSON result in claude -p output: {out[-400:]!r}")
    return last


def _call_cli(prompt: str, model_id: str, max_tokens: int, cwd: Path | None, timeout: int,
              max_turns: int, tools=None, effort: str | None = None) -> tuple[str, Usage, dict]:
    """claude -p in JSON mode, prompt on stdin, no tools, fresh session, cwd = sandbox.
    No shell: the binary is resolved by shutil.which and runs in its own process group so a
    timeout kills the whole tree before the pipes are read."""
    cmd = [cli_binary(), "-p", "--output-format", "json", "--model", model_id,
           "--tools", (",".join(tools) if tools else ""), "--max-turns", str(max_turns),
           *(["--allowedTools", ",".join(tools)] if tools else []), *config.CLI_EXTRA_ARGS]
    env = dict(os.environ)
    env.pop("CLAUDECODE", None)          # allow nested non-interactive calls
    env.pop("CLAUDE_CODE_ENTRYPOINT", None)
    # The CLI's output cap. When a reply hits it the CLI continues in a new turn and its JSON result keeps only
    # the last continuation, so the head of the reply is lost (a sketch call lost its first four sketches to a
    # 2500 cap, thinking included). The cap is therefore set well above the expected length; max_tokens stays
    # the accounting intent (over_cap is reported when the reply exceeds it).
    env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = str(output_cap(max_tokens, "cli_json"))   # thinking counts against it
    if effort:
        env["CLAUDE_CODE_EFFORT_LEVEL"] = str(effort)          # reasoning effort per role: high for builders, low for clerks
    popen_kw: dict = {}
    if os.name == "nt":
        popen_kw["creationflags"] = getattr(subprocess, "CREATE_NEW_PROCESS_GROUP", 0)
    else:
        popen_kw["start_new_session"] = True
    scratch = None
    if cwd is None:                      # never the repo: an empty folder, removed afterwards
        scratch = tempfile.mkdtemp(prefix="htsa_call_")
        cwd = Path(scratch)
    try:
        return _run_cli(cmd, prompt, cwd, env, timeout, popen_kw)
    finally:
        if scratch:
            shutil.rmtree(scratch, ignore_errors=True)


def _run_cli(cmd: list, prompt: str, cwd: Path, env: dict, timeout: int,
             popen_kw: dict) -> tuple[str, Usage, dict]:
    try:
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, text=True, encoding="utf-8",
                                errors="replace", cwd=str(cwd), env=env,
                                shell=False, **popen_kw)
    except OSError as e:
        raise CallError(f"cannot start {cmd[0]}: {e}") from e
    try:
        out, err = proc.communicate(prompt, timeout=timeout)
    except subprocess.TimeoutExpired:
        _kill_tree(proc)
        try:
            proc.communicate(timeout=10)
        except Exception:  # noqa: BLE001
            pass
        raise CallError(f"Timeout after {timeout}s (process tree killed)", estimated=True)
    out = (out or "").strip()
    if proc.returncode != 0 and not out:
        raise CallError(f"claude -p failed rc={proc.returncode}: {(err or '')[-800:]}")
    try:
        data = parse_cli_json(out)
    except CallError as e:
        raise CallError(f"{e} (rc={proc.returncode}, stderr={(err or '')[-300:]!r})") from e
    usage, info = cli_usage(data)
    data["_usage_info"] = info
    if data.get("is_error"):
        raise CallError(f"claude -p returned error: {str(data.get('result'))[:400]}",
                        usage=usage, raw=data)
    text = data.get("result") or ""
    return text, usage, data


# ---------------------------------------------------------------- API backend
_api_client = None
_api_lock = threading.Lock()


def _get_api_client():
    global _api_client
    with _api_lock:
        if _api_client is None:
            import anthropic  # local import so the CLI/mock backends need no SDK
            _api_client = anthropic.Anthropic()
        return _api_client


def _call_api(prompt: str, model_id: str, max_tokens: int, timeout: int,
              thinking_budget: int | None) -> tuple[str, Usage, dict]:
    client = _get_api_client()
    kwargs: dict = dict(model=model_id, max_tokens=max_tokens,
                        messages=[{"role": "user", "content": prompt}], timeout=timeout)
    if thinking_budget:
        kwargs["thinking"] = {"type": "enabled", "budget_tokens": int(thinking_budget)}
        kwargs["max_tokens"] = max_tokens + int(thinking_budget)
    resp = client.messages.create(**kwargs)
    text = "".join(getattr(b, "text", "") for b in resp.content if getattr(b, "type", "") == "text")
    u = resp.usage
    usage = Usage(int(getattr(u, "input_tokens", 0) or 0), int(getattr(u, "output_tokens", 0) or 0),
                  int(getattr(u, "cache_read_input_tokens", 0) or 0),
                  int(getattr(u, "cache_creation_input_tokens", 0) or 0))
    raw = {"id": resp.id, "stop_reason": resp.stop_reason, "model": resp.model, "usage": usage.to_dict()}
    return text, usage, raw


# ---------------------------------------------------------------- public entry point
TRANSIENT = ("rate_limit", "overloaded", "529", "503", "502", "timeout", "Timeout", "connection")
MAX_TIMEOUT_RETRIES = 1          # a timed-out call is retried once at most, with a logged reason


def _is_timeout(e: Exception) -> bool:
    """A call that ran out of time: the CLI kill path, or an SDK / socket timeout."""
    if isinstance(e, CallError):
        return bool(e.estimated)
    return "timeout" in type(e).__name__.lower() or "timed out" in str(e).lower()
RAW_KEYS = ("usage", "stop_reason", "model", "id", "num_turns", "total_cost_usd", "session_id",
            "modelUsage", "_usage_info", "duration_ms", "duration_api_ms")


def call(prompt: str, *, role: str, tools: list[str] | None = None, call_id: str | None = None, model: str | None = None,
         max_tokens: int | None = None, cwd: Path | None = None, backend: str | None = None,
         log_dir: Path | None = None, meta: dict | None = None, timeout: int | None = None,
         max_turns: int | None = None, thinking_budget: int | None = None,
         retries: int = 2, effort: str | None = None) -> CallResult:
    """One model call. Never raises on model errors after retries; returns error in the result
    with the summed usage of every attempt (failed ones included), so the driver can charge
    it and continue."""
    meta = dict(meta or {})
    call_id = call_id or new_id("c")
    logical = model or config.DEFAULT_MODEL
    backend = backend or config.default_backend()
    model_id = config.MODEL_IDS.get(backend, {}).get(logical, logical)
    max_tokens = max_tokens or config.PARAMS["max_tokens"].get(role, 3000)
    timeout = timeout or config.PARAMS["call_timeout_s"]
    max_turns = max_turns or config.PARAMS["max_turns"]
    prompt, truncated = fit_prompt(prompt)
    if truncated:
        print(f"[llm] {call_id}: prompt over {truncated['limit']} chars, cut in the middle "
              f"({truncated['removed_chars']} removed)", file=sys.stderr)
    t0 = time.time()
    text, total, raw, err, stop = "", Usage(), {}, None, None
    attempts, estimated, attempt_errors, retry_reasons, timeouts = 0, False, [], [], 0
    while attempts <= retries:
        attempts += 1
        try:
            if backend == "mock":
                fn = _mock_fn or _default_mock
                text = fn(prompt, role, meta)
                usage = Usage(_estimate_tokens(prompt), _estimate_tokens(text), 0, 0)
                raw = {"mock": True}
                stop = "end_turn"
            elif backend == "cli_json":
                text, usage, raw = _call_cli(prompt, model_id, max_tokens, cwd, timeout, max_turns, tools=tools, effort=effort)
                stop = raw.get("stop_reason")
            elif backend == "messages_api":
                text, usage, raw = _call_api(prompt, model_id, max_tokens, timeout, thinking_budget)
                stop = raw.get("stop_reason")
            else:
                raise ValueError(f"unknown backend {backend}")
            total = total.add(usage)
            err = None
            break
        except Exception as e:  # noqa: BLE001
            err = f"{type(e).__name__}: {str(e)[:500]}"
            attempt_errors.append(err)
            timed_out = _is_timeout(e)
            if timed_out:                             # charge the real output cap, not max_tokens
                timeouts += 1
                total = total.add(timeout_estimate(prompt, max_tokens, backend, thinking_budget))
                estimated = True
            elif isinstance(e, CallError):
                total = total.add(e.usage)
            if isinstance(e, CallError):
                raw = e.raw or raw
            if attempts > retries or not (timed_out or any(t in err for t in TRANSIENT)):
                break
            if timed_out and timeouts > MAX_TIMEOUT_RETRIES:
                retry_reasons.append(f"attempt {attempts}: timeout again; not retried")
                break
            retry_reasons.append(f"attempt {attempts}: " + (
                "timeout; retried once in case the stall was transient" if timed_out
                else f"transient error ({err[:120]})"))
            time.sleep(min(30, 2 ** attempts))
    res = CallResult(call_id=call_id, role=role, backend=backend, model=logical, text=text,
                     usage=total, cost_usd=cost_usd(logical, total),
                     duration_ms=int((time.time() - t0) * 1000), stop_reason=stop, error=err,
                     attempts=attempts, max_tokens=int(max_tokens), usage_estimated=estimated,
                     attempt_errors=attempt_errors, retry_reasons=retry_reasons,
                     prompt_truncated=truncated)
    if log_dir is not None:
        log_dir = Path(log_dir)
        log_dir.mkdir(parents=True, exist_ok=True)
        rec = res.to_dict()
        rec["meta"] = meta
        rec["prompt_chars"] = len(prompt)
        rec["flags"] = {k: config.flags().get(k) for k in config.ENV_FLAGS}   # the run's effective flags
        rec["raw"] = {k: v for k, v in raw.items() if k in RAW_KEYS}
        p = log_dir / f"{call_id}.json"
        write_json(p, rec)
        res.raw_path = str(p)
    return res


def call_many(specs: list[dict], max_workers: int = 6) -> list[CallResult]:
    """Run several independent calls concurrently. Each spec is kwargs for call() plus 'prompt'."""
    import contextvars
    from concurrent.futures import ThreadPoolExecutor
    def _one(spec: dict) -> CallResult:
        spec = dict(spec)
        prompt = spec.pop("prompt")
        return call(prompt, **spec)
    with ThreadPoolExecutor(max_workers=max_workers) as ex:   # each worker sees the run's flags
        futs = [ex.submit(contextvars.copy_context().run, _one, s) for s in specs]
        return [f.result() for f in futs]
