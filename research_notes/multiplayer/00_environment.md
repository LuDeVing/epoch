# 00. Environment: what this PC can run for the multiplayer demo

Task U3. Checks run on 2026-10-17 on the owner's PC (Windows 10 Pro, build 19045).

How the checks were done. Small CPU-only commands. No model call, no GPU run, no research loop, nothing installed.
Two probe web servers were started and stopped inside single Python processes, bound to 127.0.0.1 only
(ports 8765 and 8766). No browser was launched, because of the "no heavy parallel load" rule.

Tags for web facts. [verified] means I fetched or tested it on this PC today. [memory] means I am recalling it
and did not check it.

## Short answer

1. A stdlib-only Python server works now. `http.server.ThreadingHTTPServer` served a page to two clients and pushed
   one Server-Sent Event to both (0.4 and 0.7 ms, in process). Port 8765 is free.
2. A real WebSocket server needs no install either. The lab venv already has `aiohttp` 3.14.4. It served a page and
   broadcast one message to two WebSocket clients (about 0.1 ms, in process).
3. `fastapi`, `uvicorn`, `starlette` and `websockets` are NOT in the lab venv. They ARE in system Python 3.14.0
   (`C:\Python314`). `harness.llm` and `harness.config` use only the standard library, so they import and run
   under 3.14 as well (checked with the mock backend). A FastAPI server under 3.14 could drive the same call layer.
4. `pip` is missing from the lab venv. Installs are still possible. I installed nothing. See section 8.
5. CDN libraries are reachable from this PC today [verified]. For a stage demo, copy them into the repo first
   (`curl.exe` is on the PC), so a bad venue network cannot break the page.
6. Model layer: `harness/llm.py` runs `claude -p` once per call, a fresh session each time, no streaming.
   A person-agent can use it as is. Section 6.
7. Git is clean on `master`.

## 1. Python

Lab venv interpreter: `D:\AGI-lab\.venv\Scripts\python.exe` (run with `HTSA_LAB_ROOT=D:/AGI-lab`).

`sys.version`: `3.12.12 (main, Dec 17 2025, 21:10:14) [MSC v.1944 64 bit (AMD64)]`

The venv was built by uv 0.9.20 (`pyvenv.cfg`). Base interpreter: `D:\AGI-lab\python\cpython-3.12.12-windows-x86_64-none`.
`include-system-site-packages = false`, so the venv cannot see system packages. `uv` itself is not on PATH
(`where.exe uv` finds nothing).

Installed packages in the lab venv (exact output of the `importlib.metadata` command):

```
['Flask', 'Jinja2', 'MarkupSafe', 'PyYAML', 'Pygments', 'Werkzeug', 'aiohappyeyeballs', 'aiohttp', 'aiosignal', 'annotated-types', 'anthropic', 'anyio', 'arc-agi', 'arc-agi-3', 'arcengine', 'attrs', 'blinker', 'certifi', 'charset-normalizer', 'click', 'colorama', 'contourpy', 'cycler', 'datasets', 'dill', 'docstring_parser', 'filelock', 'fonttools', 'frozenlist', 'fsspec', 'h11', 'hf-xet', 'httpcore2', 'httpx2', 'huggingface_hub', 'idna', 'iniconfig', 'itsdangerous', 'jiter', 'kiwisolver', 'matplotlib', 'mpmath', 'multidict', 'multiprocess', 'networkx', 'numpy', 'packaging', 'pandas', 'pillow', 'pluggy', 'propcache', 'pyarrow', 'pydantic', 'pydantic_core', 'pyparsing', 'pytest', 'python-dateutil', 'python-dotenv', 'regex', 'requests', 'setuptools', 'six', 'sniffio', 'sympy', 'tiktoken', 'torch', 'tqdm', 'truststore', 'typing-inspection', 'typing_extensions', 'tzdata', 'urllib3', 'xxhash', 'yarl']
```

The ones you asked about (lab venv):

| Package | In lab venv | Version / note |
|---|---|---|
| fastapi | no | |
| uvicorn | no | |
| starlette | no | |
| websockets | no | |
| aiohttp | yes | 3.14.4. Has a WebSocket server. Tested. |
| flask | yes | 3.1.3 (Werkzeug 3.1.9, Jinja2 3.1.6). `flask-sock` and `flask-socketio` are not installed. |
| sqlite3 (stdlib) | yes | SQLite library 3.50.4. JSON functions work. WAL mode works on a real file, and a reader was not blocked by an open writer (tested). |
| http.server (stdlib) | yes | `ThreadingHTTPServer` exists. Tested. |
| pydantic | yes | 2.14.0 |
| numpy | yes | 2.5.3 |
| torch | yes | 2.11.0+cu128 (a CUDA 12.8 build). Found with `find_spec`. Not imported, because that is heavy. |

Other relevant packages in the lab venv: anthropic 1.13.0, requests 2.34.2, anyio 4.15.1, h11 0.16.0,
networkx 3.6.1, PyYAML 6.0.3, pytest 9.1.1, pandas 3.0.6, matplotlib 3.11.2.
Not in the lab venv: httpx (but `httpx2` and `httpcore2` are), wsproto, simple-websocket, flask-sock,
flask-socketio, sse-starlette, watchdog, playwright, selenium, pyppeteer.

pip and ensurepip (lab venv):

- `python -m pip --version` -> `No module named pip`. So there is no pip in the venv.
- `python -m ensurepip --version` -> `pip 25.0.1`. It works and only prints the bundled version. Nothing was installed.

Other Pythons on this PC:

- `C:\Python314\python.exe`, Python 3.14.0. It is the first `python` on PATH, so a bare `python` is NOT the lab venv.
  pip 26.0.1 (in `C:\Users\User\AppData\Roaming\Python\Python314\site-packages`). 406 distributions.
  Has: fastapi 0.128.0, uvicorn 0.40.0, starlette 0.50.0, websockets 15.0.1, wsproto 1.3.2, aiohttp 3.13.2,
  flask 3.1.2, pydantic 2.12.5, numpy 2.4.3, torch 2.11.0, httpx 0.28.1, anthropic 0.92.0, watchfiles 1.1.1,
  python-multipart 0.0.21, sse-starlette 0.10.3, playwright 1.58.0.
  `import fastapi, uvicorn, starlette, websockets` works there. Playwright has no browser download present.
- `C:\Users\User\AppData\Local\Programs\Python\Python312\python.exe`, Python 3.12.10, pip 25.0.1.
  None of the web packages.

## 2. Node

- `node --version` -> `v25.9.0`
- `npm --version` -> `11.7.0`
- `npx --version` -> `11.7.0`
- Location: `C:\Program Files\nodejs`. Global npm root: `C:\Users\User\AppData\Roaming\npm\node_modules`.
- `npm ls -g --depth=0`: `claude-code-usage@2.8.3`, `npm@11.7.0`, `openclaw@2026.7.1-2`.
- No playwright, no puppeteer, no chromium download:
  `npx --no-install playwright --version` stops with
  `npx canceled due to missing packages and no YES option: ["playwright@1.64.1"]`.
  Puppeteer is the same (`puppeteer@25.14.0`). Nothing was installed.
  No `ms-playwright`, `.cache\puppeteer` or `Chromium` folder exists.
- The repo has no `package.json` and no `node_modules`.

## 3. Browsers

| Browser | Path | Version |
|---|---|---|
| Chrome | `C:\Program Files\Google\Chrome\Application\chrome.exe` | 155.0.8059.80 |
| Edge | `C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe` | 155.0.4283.45 |
| Firefox | not installed | |
| Brave | not installed | |

The default browser for http links is Chrome (`ChromeHTML`). Versions were read from the file properties. I did not
start either browser.

Useful for two "people" on one PC [memory, not tested here]: Chrome and Edge keep separate storage, so they can
play person A and person B. Two windows of the same Chrome profile share cookies and `localStorage`. A second
Chrome profile can be started with `--user-data-dir=<new folder>`, and `--app=<url>` opens a window without tabs.

## 4. Free TCP ports (bind test on 127.0.0.1, without SO_REUSEADDR)

- 8760 to 8775: all free, including 8765.
- 5170 to 5180: all free, including 5173.
- An OS-chosen port works. Binding `::1` (IPv6 loopback) on 8765 also works.
- `localhost` resolves to both `127.0.0.1` and `::1`.
- The PC has 2 non-loopback IPv4 addresses (not recorded here). A second device could in principle connect over
  the local network if the server listens on `0.0.0.0`. Not tested.
- Collision warning: `nano/dashboard.py` (the existing live dashboard) defaults to port 8765. Use another port
  for the new server, for example 8766 (tested free), if both can run at the same time.

## 5. Can this PC serve a page to two viewers?

Yes on the server side. Tested inside one Python process each, localhost only:

- Test A, stdlib only: `ThreadingHTTPServer` on `127.0.0.1:8765` with `GET /` (HTML page), `GET /events`
  (Server-Sent Events) and `POST /change`. Two clients fetched the page (200) and opened the event stream.
  One POST was pushed to both. Delay from POST to receipt: 0.70 ms and 0.42 ms. Server closed cleanly.
- Test B, aiohttp 3.14.4 on `127.0.0.1:8766` with a page and a WebSocket endpoint. Two WebSocket clients
  connected. One sent a message, the server broadcast it, both received it in 0.09 ms and 0.11 ms. Server closed.
- These are in-process times, so they are a floor, not a stage number.
- Not tested: a real browser window opening the page. A one-minute manual check before the demo is cheap:
  start the server, open `http://127.0.0.1:8765` in Chrome and in Edge.

Browser-side notes [memory, not tested here]: `EventSource` reconnects by itself and can send `Last-Event-ID`,
which is a way to catch up after a drop. A browser allows about 6 simultaneous HTTP/1.1 connections per host, and an
open event stream uses one, so keep tabs per browser few. Binding to loopback does not trigger the Windows
Firewall prompt. Listening on all interfaces usually does, the first time.

## 6. The model call layer (`harness/llm.py`, read from source today; nothing was called)

One entry point:

```
llm.call(prompt, *, role, tools=None, call_id=None, model=None, max_tokens=None, cwd=None, backend=None,
         log_dir=None, meta=None, timeout=None, max_turns=None, thinking_budget=None, retries=2,
         effort=None) -> CallResult
```

`CallResult` has `text`, `usage` (input, output, cache read, cache create), `cost_usd`, `duration_ms`, `error`,
`attempts`, `call_id`, `stop_reason`. `call()` does not raise on model errors after its retries. It returns the
error in `.error` and the summed usage of every attempt. `llm.call_many(specs, max_workers=6)` runs independent
calls in a thread pool.

Backends. `HTSA_BACKEND` forces one. Otherwise `messages_api` if `ANTHROPIC_API_KEY` is set, else `cli_json`.
On this PC the key is not set, so the default is `cli_json`.

- `cli_json`: runs the Claude Code CLI.
- `messages_api`: the `anthropic` SDK. The import is lazy.
- `mock`: canned replies, no tokens. `llm.set_mock(fn)` installs `fn(prompt, role, meta) -> str`.

How the CLI is called (`_call_cli` and `_run_cli`):

- argv: `[<claude path>, "-p", "--output-format", "json", "--model", <model id>, "--tools", "", "--max-turns", "1",
  "--safe-mode", "--strict-mcp-config"]`. With `tools=[...]` it passes `--tools a,b` and `--allowedTools a,b`.
  The last two flags come from `config.CLI_EXTRA_ARGS` (env `HTSA_CLI_EXTRA_ARGS` overrides).
- The prompt goes in on stdin. No shell (`shell=False`). The binary is found with `shutil.which("claude")`.
  On this PC it resolves to `C:\Users\User\.local\bin\claude.EXE`. Installed CLI version: `2.1.302 (Claude Code)`.
- Child environment: `CLAUDECODE` and `CLAUDE_CODE_ENTRYPOINT` are removed, so a nested call works from inside a
  Claude Code session (this shell has `CLAUDECODE=1`). `CLAUDE_CODE_MAX_OUTPUT_TOKENS` = max(4 x max_tokens, 32000).
  `CLAUDE_CODE_EFFORT_LEVEL` is set when `effort` is given.
- Working directory: a fresh empty temp folder `htsa_call_*`, deleted afterwards, unless `cwd` is passed.
- Output: it takes the last JSON object in stdout (keys such as `result`, `usage`, `modelUsage`, `is_error`).
- Timeout: `config.PARAMS["call_timeout_s"]` = 600 s (env `HTSA_CALL_TIMEOUT`). On timeout it kills the whole
  process tree with `taskkill /T /F`, charges an estimate, and retries once. Transient errors (rate_limit,
  overloaded, 502, 503, 529, connection) are retried after 2, 4, ... seconds, up to 30 s. `retries=2` means up to
  3 attempts.
- Prompt cap: `config.MAX_PROMPT_CHARS` = 60000 (env `HTSA_MAX_PROMPT_CHARS`). A longer prompt is cut in the
  middle with a visible marker. So a "what the others changed" digest must stay short.
- Logging: with `log_dir` it writes `<call_id>.json` (usage, retries, prompt length, `meta`). `meta` is free-form,
  so `meta={"person": "ana", "step": 12}` tags each call.
- The research loop wraps this in `Loop._call(prompt, role, max_tokens, meta, model=None, tools=None,
  max_turns=None, timeout=None)` in `nano/loop.py` (around line 2267). The wrapper saves the prompt under
  `run_dir/prompts/`, tracks in-flight calls, logs to `run_dir/calls/`, and charges the budget.

What this means for a person-agent:

- Each call is a fresh session. The argv has no `--resume` and no `--session-id`. The layer keeps no memory between
  calls. So "tell each agent what the others changed" means putting a change digest in the next prompt. That fits
  the layer as it is.
- No streaming. `--output-format json` returns once, at the end. The installed CLI also offers `stream-json`,
  `--include-partial-messages`, `--input-format stream-json`, `--session-id`, `--resume`, `--json-schema`,
  `--max-budget-usd` and `--no-session-persistence` [verified in `claude --help`, 2.1.302]. Using them would
  need a new function next to `_call_cli`. It does not exist now.
- Pass `role` and `max_tokens` yourself for a new role. `config.ROLES` lists encode, defaults, generate, transform,
  judge, probe, verify, plain, converter. For an unknown role `max_tokens` falls back to 3000.
- Parallel load. `call_many` defaults to 6 workers, and each worker is a separate `claude.EXE`. This PC has
  16 logical CPUs (i5-13450HX, 10 cores) and 15.7 GB RAM, with 4.9 GB free at check time, and it has crashed under
  heavy parallel load before. Suggestion (mine, not measured): at most 2 calls at once during a demo.
- Safe rehearsal: `backend="mock"` returns canned text with zero tokens and no network. Verified: a call with
  `role="plain"`, `backend="mock"`, `model="fable"` returned `1. A / 2. B / 3. C` under both Python 3.12.12
  (lab venv) and Python 3.14.0.

`config.MODEL_IDS` (exact):

```
MODEL_IDS = {
    "cli_json":     {"sonnet": "sonnet", "opus": "opus", "haiku": "haiku", "fable": "claude-fable-5-1"},
    "messages_api": {"sonnet": "claude-sonnet-5-5", "opus": "claude-opus-5-5", "haiku": "claude-haiku-5-5",
                     "fable": "claude-fable-5-1"},
    "mock":         {"sonnet": "mock", "opus": "mock", "haiku": "mock", "fable": "mock"},
}
DEFAULT_MODEL = os.environ.get("HTSA_MODEL", "sonnet")
```

- The default logical model is `sonnet`. `model="fable"` selects fable. `claude --help` also lists the alias `fable`
  for `--model` [verified].
- Price table in `config.PRICE_PER_M` (USD per million tokens, input / output): sonnet 3 / 15, opus 15 / 75,
  haiku 1 / 5, fable 16 / 80. The fable row is an estimate from one measured call on 2026-10-11
  (48,614 cache-creation tokens cost $0.97), per the comment in `config.py`.
- Fixed CLI overhead per call with `--tools ""`, measured by the lab (comments in `config.py`): sonnet about 3k
  tokens, fable about 48k tokens. With tools enabled, about 26k (measured on 2026-10-10, model not stated).
  So many small fable calls are costly. A few large fable calls are cheaper. Use fable for the design work in a
  few big calls, and sonnet or haiku for the high-volume person-agent steps.
- Import check. `harness.llm` and `harness.config` import with the standard library only. They work under the lab
  venv (3.12.12) and under `C:\Python314` (3.14.0). Same `cli_binary()` result in both.

## 7. Git

- `git status --short | wc -l` -> `0` (clean) before this file was written.
- Branch: `master`. HEAD: `74abcaf Vote and dedup tolerate a state without cluster_members`.
- The only local branch is `master`. There is no local `main`.
- This notes file is new, so after it was written the tree has one untracked folder (`research_notes/multiplayer/`).
  `.gitignore` covers `__pycache__/`, `*.pyc`, `.pytest_cache/` and `.claude/` only.

## 8. Stdlib-only server + static page with CDN libraries: what is available, what needs installs

Available now, no install:

| Need | What to use | Status |
|---|---|---|
| HTTP server with threads | `http.server.ThreadingHTTPServer` | tested |
| Push to every viewer | Server-Sent Events from that server; edits go back by POST | tested |
| Two-way socket | aiohttp 3.14.4 in the lab venv (`web.WebSocketResponse`) | tested |
| Shared store | `sqlite3` in WAL mode, or JSON / JSONL files like the rest of the lab | tested (WAL) |
| Watch the run folder | poll file times every 0.3 to 1 s (no `watchdog` in the venv) | not tested |
| Check payloads | `pydantic` 2.14.0 | present |
| Model calls | `harness.llm` (stdlib only) | mock tested |
| Front end | one static HTML + JS file served by the same server | tested (page) |

CDN libraries that answered HTTP 200 to a HEAD request from this PC on 2026-10-17 [verified]:

- d3 7.9.0: `https://cdn.jsdelivr.net/npm/d3@7.9.0/dist/d3.min.js` (279,706 bytes). The same file also answered 200 on
  unpkg and on cdnjs (`https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js`). d3 covers force layouts (idea
  clusters), hierarchy and tree layouts, transitions and zoom.
- jsDelivr, all 200: `htm@3.1.1/dist/htm.module.js`, `preact@10.24.3/dist/preact.min.js`,
  `alpinejs@3.14.9/dist/cdn.min.js`, `gsap@3.12.5/dist/gsap.min.js` (72,214 bytes),
  `elkjs@0.9.3/lib/elk.bundled.js` (1,606,238 bytes), `@dagrejs/dagre@1.1.4/dist/dagre.min.js` (96,038 bytes),
  `cytoscape@3.30.2/dist/cytoscape.min.js` (373,304 bytes), `yjs@13.6.20/dist/yjs.mjs` (298,212 bytes).
- Google Fonts stylesheet (Inter) answered 200.
- I only checked that the files exist. I did not download or run them, and I did not check whether they fit the
  design.
- Reliability: a CDN needs internet at the venue. To avoid that, download the files once into the repo (for example
  a `web/vendor/` folder) and serve them from the same server. `curl.exe` 8.13.0 does it with no pip and no npm:
  `curl.exe -L -o d3.min.js` followed by the URL. Python `urllib.request` can do the same.

Needs an install, or a different interpreter:

| Need | Why | Way around |
|---|---|---|
| FastAPI + uvicorn + websockets in the lab venv | not installed, no pip in the venv | run the server with `C:\Python314\python.exe` (has all of them, no install), or use aiohttp |
| Playwright / Puppeteer for scripted UI checks | not installed in node; Python playwright 1.58.0 exists only in 3.14 and has no browser | could drive the installed Chrome or Edge by channel [memory, not tested]; or test by hand |
| A JS build tool such as Vite (port 5173) | no `package.json`, nothing installed | not needed for one static page |
| watchdog / watchfiles | not in the lab venv (watchfiles is in 3.14) | poll file times with stdlib |

Are installs possible without pip? Yes, in four ways. I used none of them.

1. No Python install at all: stdlib plus aiohttp (already in the venv).
2. The 3.14 interpreter already has the web stack, and has its own pip 26.0.1.
3. `python -m ensurepip` works in the lab venv (bundled pip 25.0.1) and would add pip. It changes the lab venv, so
   avoid it unless the owner agrees.
4. JavaScript libraries need neither pip nor npm: copy the files with `curl.exe` or `urllib`.

The network is open from this PC today [verified]: HEAD requests returned 200 from PyPI (`pypi.org/simple/websockets/`)
and from the npm registry (`registry.npmjs.org/d3/7.9.0`). `uv` is not installed, so the uv route is not available.

## 9. Windows details that can bite

1. Replacing `control.json` can fail while someone reads it. Tested in a temp folder: `os.replace(tmp, target)` while
   a reader had the target open raised `PermissionError` (WinError 5). It worked once the reader closed it. So a
   server that writes `control.json` by temp file plus rename needs a short retry loop.
   In `nano/loop.py`, `_stage` reads `control.json` at every stage boundary, and every 10 s while paused. It keeps
   the last good copy if a read fails to parse, and logs changes by content hash to `control_log.jsonl`.
   The file is written whole, so two people editing it at once would overwrite each other. One server process
   should be its only writer.
2. A bind test must not set `SO_REUSEADDR` on Windows, or it can succeed on a port that is in use [memory]. My test
   did not set it.
3. Use `127.0.0.1` in URLs, not `localhost`. `localhost` also resolves to `::1` here (tested), and some browsers try
   IPv6 first [memory].
4. The repo already has a working pattern for "tiny local server + static page": `nano/dashboard.py` is stdlib
   only, binds `127.0.0.1`, defaults to port 8765, serves the page, and the page polls `/api/state` every 2 s
   (`setInterval(tick,2000)`). It is read-only. Its docstring says the loop writes `live.json` (in-flight calls).
   I read its header and routes only.
5. Memory is the tight resource: 4.9 GB free of 15.7 GB at check time. Browsers, `claude.EXE` processes and
   the server all share it.

## 10. Not checked

- A real browser opening the page, and two real browser windows side by side.
- A second device on the local network, and Windows Firewall rules.
- Speed or output of a real `claude -p` call (model calls were not allowed).
- Whether `--output-format stream-json` works in this install. It is listed in `--help` only.
- Whether the Playwright package in 3.14 can drive the installed Chrome.
- Whether the owner ran `nano/dashboard.py` live before.
