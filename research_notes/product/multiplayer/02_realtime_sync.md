# 02. Real-time shared state: several people, several agent processes, no conflicts

Task R2. Web research plus small local checks. Date: 2026-10-17. For the hackathon track "Multiplayer agentic experiences".

## How this was done

- Web: I read about 30 pages with the fetch tool and ran 6 searches. The fetch tool returns a short extract of a page, not the full text, so quotes are short. The pages are listed in section 11.
- Repo: I read the three earlier notes in this folder (`00_requirements.md`, `00_artifacts.md`, `00_environment.md`) so that names and limits match the real loop. I also read the sibling notes 01 (R1), 03 (R3) and 04 (R4), which other tasks wrote at the same time, only to match names and rules. Section 5.9 maps them.
- Local checks: Python and Node scripts, one process each, loopback only (127.0.0.1), OS-chosen ports. No browser, no model call, no GPU, no loop run, nothing installed. They ran on this PC: Windows 10 build 19045, Python 3.12.12 (lab venv), SQLite 3.50.4, Node 25.9.0. Total run time was under two minutes. The scripts sit in the session scratchpad (folder `r2rt`), not in the repo. The code that matters is copied into Appendix A.
- Nothing in the repo was changed except this file.

Tags on facts:

| Tag | Meaning |
|---|---|
| [page] | Verified on the web page named in section 11, read through the fetch tool. |
| [snippet] | Seen only in a search result summary. I did not open the page. |
| [memory] | From my memory. Not checked. |
| [tested] | Run or measured on this PC today. |
| [repo] | From the repo's own notes or code, read today. |
| [design] | My choice or inference. Not an outside fact. |

The hackathon wording (what the judges want) comes from the workflow brief. I searched for the track page and found none, so it is not verified.

## 0. Short answer

1. **Shape.** An append-only event log in SQLite (WAL mode) behind one Python process that is the only writer. The server gives every event a number, `seq`, with no gaps. The order is the number, never the clock. [design] Test: 4 writers, 240 events, 3 readers. Every reader saw exactly 1 to 240. [tested]
2. **Transport.** Server-Sent Events (SSE) from `ThreadingHTTPServer` push to browsers. Browsers send changes with POST. Python agents use plain HTTP: POST to write, GET with a cursor to read. A long-poll route is the fallback. Everything is standard library. [tested]
3. **Not CRDT, not WebSocket, not cloud.** Yjs needs a Node server and `pycrdt` needs pip [page]. The stdlib has no WebSocket module [tested]. Liveblocks needs internet and a key, Supabase needs internet or Docker, and PartyKit is JavaScript on Cloudflare [page]. Figma itself uses server order and last-writer-wins per property, not a document merge [page]. We copy that.
4. **Three kinds of data, three rules.** Facts (ideas, objections, results) are appended and cannot conflict. Single fields (a name, a flag) are last-writer-wins by server order, and the answer says whom you overwrote. [tested] Exclusive work (a branch) uses claims: server-granted, with expiry and a fencing token. [design]
5. **Agents pull, at stage boundaries.** Each agent keeps a cursor. Before its next step it asks for a digest: a short text (cap 1200 characters) of what others did since the cursor. Its own events are removed. Human steering comes first. The text goes into the next prompt. [tested]
6. **Presence is not in the log.** It is an in-memory list with a 20 s time-to-live, fed by a 5 s heartbeat. [design]
7. **Optimistic UI has three visible states.** Pending (only on my screen), queued (the server numbered it), applied (the loop picked it up at round r, stage s). [design, store tested]
8. **Windows traps, measured here.** `localhost` cost a Python client 2.03 s per connect, so use 127.0.0.1. Two stdlib servers could bind one port. A dead SSE client is noticed only after 1 to 2 heartbeats. `ON CONFLICT DO NOTHING` burns sequence numbers. `os.replace` on `control.json` needs a retry loop. [tested]
9. **Size.** 7 routes and 36 event names (26 needed on day one). Section 5 has them. Section 9 has a one-day build order.
10. **Not verified.** A real Chrome or Edge, two machines on Wi-Fi, the hackathon page. Section 10.

**Reading guide.** To choose between the options: sections 0 and 1. To build the server and the agent side: sections 3, 5, 6 and Appendix A. To build the browser side or the design: sections 4, 5.3, 8 and Appendix A.3 and A.4. To run the demo: sections 6.5 and 9. To merge with the other notes: section 5.9. The appendix is long. Skip it unless you are coding.

## 1. The four options, side by side

### 1.1 Table

| | (a) Event log + SSE | (b) CRDT (Yjs, Automerge) | (c) WebSocket | (d) Managed service |
|---|---|---|---|---|
| Server in stdlib Python only | Yes [tested] | No. The usual Yjs server is Node: `npx y-websocket`, and the page names no non-JS server [page]. The Python port `pycrdt` is a pip package built on a Rust core, Windows wheels exist, Python 3.11 or newer [page]. The Automerge docs page lists JavaScript, Rust and Swift, and no Python [page]. | No stdlib module exists [tested]. You can hand-write RFC 6455 (about 120 lines) [design]. | No. Hosted services, or Node or Docker stacks. |
| Browser side | `EventSource` and `fetch`, built in | Yjs in the page (a CDN file exists) [repo] | `WebSocket`, built in | Vendor SDK |
| Python agent side | `urllib`, stdlib [tested] | needs `pycrdt` (pip) | hand-written client | REST API with a secret key [page] |
| How conflicts end | Server order, per-field last-writer-wins, claims | Automatic merge, also for text | Same as (a). Only the pipe differs. | Vendor's model |
| Works on an offline laptop | Yes [tested] | Yes, with a local relay | Yes | No: internet needed. Supabase local needs Docker [page]. |
| Build time (my estimate) | 4 to 6 h | 1 to 2 days | (a) plus 3 to 4 h | 0.5 day plus accounts, but risky on venue Wi-Fi |
| Verdict | **Choose** | No | Fallback only | No |

### 1.2 (a) Event log, one writer, server-assigned numbers

**Why this shape.** Two well-known sync systems use the same two ideas: a number that only the server hands out, and a client that remembers the last number it saw.

- Linear's sync engine, from an unofficial reverse-engineering write-up: a transaction carries a "monotonically increasing" sync id. Clients compare their `lastSyncId` with the server's and ask for the missed delta packets. The server also sends the delta back to the client that made the change. [page, unofficial]
- Replicache: a "poke" is "a contentless hint" that tells the client to pull again. The pull is computed from an opaque cookie that names the state the client has. The server's state is "the canonical source of truth". [page]
- Our `seq` does both jobs: it is the order and the cursor. [design]

**One writer.** The numbers need one place that hands them out. SQLite allows only one writer at a time anyway: "there can only be one writer at a time" [page]. So the server process is the only writer. Agents are HTTP clients of the server. They never open the SQLite file. [design]

**Store.** Rules that I tested or read:

- SQLite in WAL mode with `synchronous=NORMAL`. Readers do not block the writer and the writer does not block readers. WAL needs all processes on one host: "WAL does not work over a network filesystem". `NORMAL` can lose the last commits after a power cut, which is fine for a demo. [page] Keep the file on `D:\AGI-lab\spaces\<space_id>\`, not on a synced Desktop folder. [design; the repo notes already suggest this folder, `00_artifacts.md` section 10 option C]
- `seq INTEGER PRIMARY KEY AUTOINCREMENT`. Numbers are never reused and always rise. [page] After a rolled-back insert the next number follows with no gap. [tested]
- **Do not** handle duplicate retries with `ON CONFLICT DO NOTHING` or `INSERT OR IGNORE`. Both burn a number: the log read 1, 3. [tested] Two safe ways: look the `op` key up first under the writer lock, or let a plain `INSERT` fail with `IntegrityError` and roll back (log read 1, 2). [tested]
- Write with `BEGIN IMMEDIATE`, inside one Python lock. A deferred transaction that reads first and then writes fails at once with "database is locked" (0.19 ms, although the busy timeout was 5000 ms). [tested]
- Keep the log in memory too (a list, index = `seq - 1`). SSE handlers read the list. SQLite is for restart and audit. A reader on the writer's connection sees uncommitted rows, so do not read through it. [tested]
- Notify waiting handlers only after the commit. Check `head > last` inside the condition lock before you wait, so no wake-up is lost. [design, tested]

**Three ways to deliver the log.**

| Way | How | Good | Bad | Use it for |
|---|---|---|---|---|
| Plain polling | `GET /api/events?since=N` every 1 to 2 s | Simplest. The existing dashboard polls every 2 s [repo]. | 1 to 2 s lag, wasted requests | Python agents, at stage boundaries |
| Long-poll | same GET with `wait=25`; the server holds it until an event or timeout | Near instant, plain HTTP, no streaming traps | One request per batch (p50 9 to 11 ms in the test, p95 29 to 34 ms) | Fallback for browsers |
| SSE | one open GET, the server writes frames | Instant. Reconnect and resume are built in. One-way fits, since writes go by POST. | 6 connections per browser and host on HTTP/1.x [page]. No custom headers [page]. Needs heartbeats and a watchdog. | Browsers |

Measured on this PC, all in one process, so these are floors and not stage numbers: SSE p50 2.3 to 2.7 ms and p95 about 28 ms during a burst of 240 events from 4 writers. With 30 SSE clients and a quiet writer, p50 2.5 to 3.2 ms and p95 4.2 to 8.9 ms. [tested]

**SSE rules that matter here.**

- Frame: `id: <seq>`, then `data: <one line of JSON>`, then a blank line. A line that starts with `:` is a comment. `retry: 1000` sets the reconnect wait. The type is `text/event-stream`, UTF-8. [page]
- `Last-Event-ID` is sent only when the browser reconnects by itself. A new `EventSource` object sends none. [page] Tested with Node's spec-based `EventSource`: the first request had no header, the reconnect after a reset sent `Last-Event-ID: 15` and got events 16 to 41 with no gap and no duplicate. [tested] So a fresh page load must pass `?since=<last seq>` in the URL. The server prefers the header when both exist. [design, tested]
- After a network error the browser waits the `retry` time and reconnects. Measured: 1.0 s with `retry: 1000`. [tested]
- If the status is not 200, or the type is not `text/event-stream`, the connection fails for good: "Once the user agent has failed the connection, it does not attempt to reconnect." [page] Tested: after a 503 on a reconnect, `readyState` was 2 and no further request came. [tested] So the page needs its own watchdog (Appendix A.3).
- Comment lines never reach JavaScript. [page] So liveness uses a named `ping` event, not a comment.
- `EventSource` has no option for custom headers, only `withCredentials`. [page] A key must go in the query string.
- The spec warns that HTTP chunking can hurt reliability for event streams. [page] So the stream is a plain close-delimited HTTP/1.0 response: `Connection: close`, no `Content-Length`. [design] It worked with Python's `http.client` and with Node's `EventSource`. It was not tried in Chrome or Edge. [tested]
- `ThreadingHTTPServer` gives one thread per connection (Python 3.7 or newer). [page] Each SSE client holds one thread. 30 clients (67 threads in the test process) were fine. [tested]
- Python's docs say: "`http.server` is not recommended for production." [page] For a stage demo that is acceptable.

### 1.3 (b) CRDTs, and how Figma really does it

What Figma says about its own multiplayer system [page]:

- It did not use operational transforms. Its approach is "inspired by" CRDTs. Because there is a central server that is the authority and defines the order of events, it can drop the overhead that decentralised CRDTs need.
- The document is `Map<ObjectID, Map<Property, Value>>`. Conflicts are settled per property: the server keeps the last value any client sent, like a last-writer-wins register. The server's order replaces timestamps. Different properties, or the same property on different objects, never conflict.
- Text properties are atomic. Two people editing the same text property do not get a merge.
- Local changes show at once. If a server change arrives for a property that has an unacknowledged local change, the client discards the server change. The aim is to avoid flicker.
- Reparenting is a property change on the child. The server rejects a parent change that would make a cycle. Child order uses fractional indexes: a position is a number between its neighbours, and the parent link and the position are one property. For two inserts at the same spot, the server gives the second a unique position. [page, second article]
- On reconnect the client downloads a fresh copy and applies its offline edits on top.
- The article says nothing about presence or cursors.

What this means for us [design]: our data is short records and flags. It is not shared rich text. There is one server. So **append-only facts plus last-writer-wins per field** is enough. A CRDT would add a Node server or a pip package, and its main gains (offline merge, shared text) are not needed. If a long shared text field ever appears, give each person a separate append-only note instead of one shared field.

Yjs has one idea worth copying: **awareness** for presence. It is a small JSON state per client with an increasing clock. A client marks a peer offline after 30 s without an update, so every client must re-broadcast on a regular beat. [page] Section 4 uses the same shape.

### 1.4 (c) WebSocket without a library

- Python's stdlib has `socket`, `socketserver`, `selectors`, `ssl`, `asyncio` and `wsgiref`, but no WebSocket module. [tested] A search found only third-party packages. [snippet]
- A hand-written server is possible. RFC 6455 [page]: the server joins the client's `Sec-WebSocket-Key` with the GUID `258EAFA5-E914-47DA-95CA-C5AB0DC85B11`, takes SHA-1, encodes base64, and answers `101` with `Sec-WebSocket-Accept`. Frames carry a FIN bit, an opcode (text 1, close 8, ping 9, pong 10), a mask bit and a length (7, 16 or 64 bits). Client frames must be masked and server frames must not. A server must close on an unmasked client frame. Control frames are at most 125 bytes and are never fragmented. Fragmented messages can be interleaved with control frames.
- Estimate: about 120 lines on top of `BaseHTTPRequestHandler`, plus a second hand-written client for Python agents. [design]
- Why not: SSE plus POST covers the need. Pushes go server to browser. Writes come at human speed. The remaining gains are not needed: no 6-connection cap (WebSocket has a per-host limit of 255 in Chromium and 200 in Firefox [page]) and cheaper two-way cursor traffic (a POST at 4 per second is enough). The risks are real: partial reads, ping and pong, the close handshake, fragmentation. [design]
- If the stdlib-only rule is relaxed: `aiohttp` 3.14.4 is already in the lab venv and served WebSocket clients in a test on 2026-10-17. `C:\Python314` has `websockets` 15.0.1 and FastAPI. [repo]

### 1.5 (d) Managed services, and why they are out for an offline laptop demo

| Service | Facts | Problem for us |
|---|---|---|
| Liveblocks | Free plan: 10 simultaneous connections per room. Self-hosting is "Available as paid add-on", Enterprise only. The pricing page has no date and does not mention offline mode. [page] The REST call in their agent-feeds post goes to `https://api.liveblocks.io/v2/...` with a secret key. [page] Presence is temporary, Storage persists after everyone leaves. [page] | Needs internet, an account and a key. Free cap of 10 connections per room is tight when agents are also clients. |
| PartyKit | "An open source platform for deploying real-time, collaborative, multiplayer applications." "Is now a part of Cloudflare." Runs on Durable Objects. Post metadata date 2024-04-05. [page] | Server code is JavaScript. Python agents would be WebSocket clients of someone else's runtime. |
| Supabase Realtime | Broadcast, Presence, Postgres Changes. Local development needs a Docker-compatible container manager; the Docker-less stack is experimental and for Linux and Apple-silicon macOS. [page] | Docker on a PC that had 4.9 GB RAM free [repo] and has crashed under load. |

Common reasons to say no for the demo [design]: venue Wi-Fi may fail; accounts and keys cost setup time on the day; the Python stdlib-only rule; research data would leave the laptop. These services do show what to copy: **Presence is temporary, Storage is permanent**, and agent activity is a feed. Liveblocks sells "Feeds" for exactly that. [page]

A search also found a YC Fall 2026 request for a "multiplayer AI workspace" with Figma-like live collaboration, teammates watching an agent's progress live, and a clean hand-off of a running task. [snippet] It shows what a judge will find convincing.

### 1.6 Verdict

Take (a). Borrow: per-property last-writer-wins and the "ignore server echoes for fields I am editing" rule from Figma; the poke-and-pull and rebase ideas from Replicache; the single rising number from Linear; the temporary-versus-permanent split and the heartbeat from Liveblocks and Yjs.

## 2. The picture

```
 Browser (Maya)    Browser (Ben)     Agent process (maya.agent)    Agent process (ben.agent)
 EventSource+POST  EventSource+POST  urllib: digest, emit,         same
                                     claim, heartbeat
        \               |                     |                        /
         +--------------+---------------------+-----------------------+
                                  |  HTTP on 127.0.0.1:8766
                    +-------------v---------------+
                    | space_server.py  (stdlib)   |   the only writer
                    |  event log: SQLite WAL + the same list in memory
                    |  claims (memory) + reaper thread
                    |  presence roster (memory)
                    |  digest builder
                    +-------------+---------------+
                                  | files (the loop stays unchanged)
                    +-------------v---------------+
                    | bridge (a thread or a file) |
                    |  run files  -> events       |
                    |  human events -> control.json (single writer)
                    +-----------------------------+
```

Port 8766, because `nano/dashboard.py` already uses 8765. [repo] Always use `http://127.0.0.1:8766`, never `localhost` (pitfall 1).

## 3. The agent side

### 3.1 Learn what others changed: cursor, stage-boundary read, digest

- **Pull, not push.** A busy agent cannot act on a push in the middle of a model call. The loop already looks outside at five places per round, the `_stage` boundaries `ideated`, `clustered`, `deepened`, `built` and `verified`. It reads `control.json` there, and again every 10 s while paused. [repo] The feed is read at the same places. The repo notes also propose a `planned` boundary and an in-stage tick. [repo]
- **Cursor.** The last `seq` the agent has taken into a prompt. It moves in two steps: `digest()` reads, `commit_cursor()` moves the cursor after the text is in the prompt. If the process dies between the two, it sees the events again. That is "at least once", and a digest shown twice is harmless. [design, tested] The client saves the cursor in its run folder and reports it in every heartbeat, so the UI can show "Ben's agent has seen up to #131". If the file is lost, a new `digest()` with cursor 0 returns the last 60 events. [design, tested]
- **Receipt.** `commit_cursor(round, stage)` writes a `digest_taken` event: from, to, how many events, how many characters. The log then shows what each agent was told, and at which step. R3 and R4 both ask for this receipt. [tested]
- **Digest on the server.** One format for all agents. The server knows claims and closed items. No model call, so no cost and no new failure. [design]
- **What the tested digest function does** (Appendix A.1, `make_digest`): drops the agent's own events; drops kinds that have no sentence; merges repeats by (author, kind, subject); sorts by tier (human steering first, then claims, test results and the team question, then arguments, then bulk) and by newest; fills lines until the cap, with room for a footer; prints in time order; the footer says how many lines were left out and where to read them. With caps of 400, 800 and 1200 it produced 332, 735 and 731 characters, kept every human line, and hid the agent's own events. [tested]
- **Where it goes in the prompt.** Today the loop has no slot for "what another person or agent changed". The nearest are the part memory block, `history_text` and the map text. The repo notes propose `self.peer_digest` with its own cap, set in `_space_pull` and appended wherever `history_text()` is used, and in the builder prompts. [repo] Never add it to blind stages: clustering and the Mode 3 panel judge are blind to authors on purpose. Keep `obvious`, `obvious_match` and anything under `private/` out of events and digests. [repo]
- **Zero-code path for the demo.** The bridge writes the digest into the `note` key of `control.json`. The cap is 600 characters. It appears as "NOTE FROM THE OWNER" for idea agents from round 2, for interrogation and for the re-plan. It does not reach builders or critics. [repo]
- **Cost.** Anthropic reports that multi-agent systems "use about 15x more tokens than chats". [page] A 1200-character digest is about 300 tokens at 4 characters per token [design]. The mock run made 823 model calls [repo]. So put the digest where `history_text()` already goes, not into every call. [design]
- **Why share decisions and not only files.** "Actions carry implicit decisions, and conflicting decisions carry bad results." [page, Cognition] "Without detailed task descriptions, agents duplicate work, leave gaps, or fail to find necessary information." [page, Anthropic] Claude Code's agent teams deliver messages to teammates automatically, give each teammate its own context window, and keep one shared task list. [page] All point the same way: tell each agent what the others decided, and split the work.
- **Interrupts.** The heartbeat answer can carry `interrupts`. The reference code sends `claim_lost` and `subject_closed`. A `pause` or `stop` would follow the same way. The agent acts on an interrupt at the next safe point. It never aborts a model call halfway. [design; the first two tested]

### 3.2 Two agents, one branch: claims with expiry, granted by the server

- **Unit.** A tree node, subject `node:<id>`. A claim covers the node and everything below it. The server keeps a parent map built from `node_added` events and checks the node and its ancestors. [design]
- **Life cycle.** `acquire` (granted if free or expired, else 409 with the holder and the time left), then `renew` (TTL 90 s; the 5 s presence heartbeat lists the claims the caller believes it holds, and the server renews those that match and reports `claim_lost` for the others), then `release` when done. If the holder goes silent, a reaper thread (every 5 s) writes `claim_expired`. Only a person can `takeover`, and that writes `claim_taken_over`. [design]
- **Fencing token = the `seq` of the `claim_granted` event.** Tokens rise and survive a server restart without any extra table. [design, tested]
- **Why a token.** An expiring lease cannot stop a paused holder, for example a frozen PC, from writing after it lost the lease. Kleppmann: "a fencing token is simply a number that increases"; the resource rejects writes that carry an older token; and checking the expiry just before the write does not help, because the pause can come between the check and the write. [page] Our server is the resource, so it can check the token on every guarded write.
- **Test.** 8 claimers raced for one node: 1 won and 7 got 409. After expiry a second owner got a higher token. The first owner's write and renew then both got 409 `claim_lost`. [tested]
- **Efficiency or correctness.** Kleppmann separates locks that save repeated work from locks that protect state. [page] Ours is both: it saves duplicate model spend, and a stale write would also corrupt a branch's records. So we check the token. [design]
- **TTL for a slow PC.** 90 s, with the heartbeat in a daemon thread that is separate from the model call. The owner's PC has crashed under load. [repo] Expiry uses `time.monotonic()` on the server, because wall clocks jump. Clients receive `ttl_left_s`, never an absolute time, because client clocks differ. [design]
- **A claim that is never released is the common failure.** In Claude Code's agent teams, "teammates sometimes fail to mark tasks as completed, which blocks dependent tasks". [page] So expiry is a must.
- **Same advice from Claude Code.** Task claiming "uses file locking to prevent race conditions", and "Two teammates editing the same file leads to overwrites. Break the work so each teammate owns a different set of files." [page]
- **Advisory mode.** R4 recommends claims that warn and never block (`04_multiplayer_ux.md`, recommendation 10). `ENFORCE_CLAIMS = False` does that for agents too. Reason to enforce: a stale write would corrupt a branch's records. Reason to go advisory: a rejected write wastes model spend that was already paid. One answer fits both: take the claim BEFORE the work starts, so a conflict shows at claim time and not at write time. [design, tested]
- **Hard for agents, soft for people.** People are never blocked, because people steer. A person who edits inside a claimed branch sees a warning chip, and can take over with one click. [design]
- **Zero-code mapping into the loop.** Nodes claimed by other agents go into this loop's `skip_nodes`. That key is "level": the loop applies it at the next boundary, so the part and everything under it get no idea contexts, no brief, no seed, and its clusters count as done. A release removes the entry. [repo for the loop's behavior, design for the mapping]
- **Guarded kinds.** For agent events about a node (`sketch_batch`, `cluster_snapshot`, `objection_raised`, `reply_posted`, `objection_marked`, `candidate_built`, `test_result`, `memory_added`) the server requires the holder's token. Events from people are never blocked by a claim. [design]

### 3.3 Keep every record: append-only, with owner and time

- Every record is an event row: `seq`, `ts` (server clock, UTC), `by`, `by_kind`, `owner`, `kind`, `subject`, `data`, `op`, `base`. That meets the repo's rules: id, author and time on every row (R17), rows never overwritten (R28), UTC times (R31), owner and timestamp on every record (R36). [repo]
- An edit is a new event. A delete is a new event (`event_retracted`) that hides and does not remove. This is event sourcing: "all changes to application state are stored as a sequence of events", and state can be rebuilt by replay. [page, Fowler] Azure's guide: "you should never update the event data"; undo with a compensating event. [page]
- **Retries are safe** because the client chooses an `op` key. Delivery is "at least once", so handlers must be idempotent. [page, Azure] Tested: 36 retried POSTs returned the original `seq` and added no row. [tested]
- **Say the intent.** `question_vetoed` is better than a state diff. "State-focused events reduce the event store to a change log that has no business meaning." [page, Azure]
- **`base`** is the head the author had seen. It is a hint, not a lock. Azure describes optimistic concurrency, which rejects an append if the stream changed since it was read. [page] We only annotate with it (`overwrote`), because people must never be blocked. [design]
- **Snapshots are an optimisation.** "The eventstream remains the source of truth." [page, Azure] Day one: the browser downloads the whole log and replays it. Keep events small: titles, not full texts, and `sketch_batch` for bulk. The mock run had 739 sketches, 135 clusters and 81 decisions [repo], which is a few thousand events.
- Azure also warns that event sourcing is a poor fit for short-lived prototypes. [page] We use only the cheap part: an immutable list with numbers and idempotent writes, with no per-entity rehydration. [design]
- A new `epoch` id is made with a new database. A client that holds an old epoch, or a `since` ahead of the head, gets `reset` and reloads. [design; the `since` case tested]

### 3.4 How it plugs into the existing loop (no change to `nano/loop.py` for day one)

The loop treats its disk files as output and re-reads only `control.json`, memory and a few ledgers. [repo, `00_artifacts.md` 9.4] So the push side can be a sidecar that follows the files, and the pull side is a rendered `control.json`.

| Run file (how it changes) | Becomes event | Follow it by |
|---|---|---|
| `problem_tree.json` (rewritten whole) | `node_added` for new ids, `node_edited` for changed fields | content hash, then diff |
| `ideas.jsonl` (appended) | `sketch_batch` (group by node and direction, up to 50 items) | byte offset |
| `idea_clusters.json` (rewritten whole; cluster ids are positional and move) | `cluster_snapshot` per node and direction. Each cluster gets a stable `key` by matching member overlap with the last snapshot. Do it once: R1's `ViewLib` does it in the browser, so the bridge may send the loop's own ids. | content hash |
| `deepen.json`, `dialogue.jsonl` | `objection_raised`, `reply_posted`, `objection_marked` | byte offset, hash |
| `cands/*.jsonl`, `verify.jsonl` | `candidate_built`, `test_result` | byte offset |
| `next_questions.json` | `question_picked` | content hash |
| `memory_log.jsonl` | `memory_added` | byte offset |
| `control_log.jsonl` (each row is a whole control state, with no author) | `control_applied`, by matching the new state against queued human events | byte offset |
| `live.json` (rewritten at every model call) | not events. It becomes the agent's presence `activity`. | poll |
| Never mirror: `state.json`, `private/`, `calls/`, `prompts/`, `obvious`, `obvious_match` | | |

Sources: `00_artifacts.md` sections 9.2, 9.5, 11.4. [repo] A JSONL line can be torn, so skip a line that does not parse. A whole-file JSON can be cut mid-write, so try again at the next poll. [repo]

**The `control.json` writer** (one writer, the bridge) [repo for the file's behavior, design for the rules]:

- Render one whole file from all folded human events. Write a temp file, then `os.replace`. On Windows `os.replace` raises `PermissionError` while a reader holds the target open. Tested: 8 retries over 410 ms, then success. [tested; the same finding is in `00_environment.md`] Retry every 50 ms for up to 3 s.
- Merge rules: `skip_nodes` is the union (plus nodes claimed by other agents); `veto` is the union; `choose` is the last writer by `seq`; `note` is joined with names, newest first, cut to 600 characters; `opinions` are keyed by (who, target); `add_nodes` is deduped by id and the author stays as an extra key, which the loop keeps. [repo]
- The loop drops a second `add_nodes` with a used id without a message. [repo] So the server refuses the second `node_added` with 409 `id_taken`, and the person is told. [design]
- `veto` and `choose` act at the next question pick, so a veto set after a pick only acts on the next one. [repo] The UI must say so (section 4.2).
- Do not mirror `budget_add` and similar run controls on day one. The loop applies each key and value pair once, and a resume applies it again. [repo]

## 4. Presence and optimistic UI

### 4.1 Presence: who is online and what each one is looking at

- **Temporary data, not in the log.** No `seq`. Yjs awareness is "an increasing clock attached to a schemaless JSON object", an inactive peer is dropped after 30 s, and every client must re-broadcast on a regular beat. [page] Liveblocks splits Presence (temporary) from Storage (persistent). [page]
- **Roster entry:**

```json
{"client":"c-7f3a","name":"Maya","kind":"human","owner":"maya","color":"#e8590c",
 "view":"clusters","focus":{"type":"cluster","id":"c12"},
 "activity":{"state":"executing","stage":"deepened","node":"optimizer","text":"pre-mortem on 3 ideas"},
 "cursor":131,"seen_ms_ago":1200}
```

- **Beat** every 5 s, and at once on a focus change (throttled to 4 per second). The server drops an entry after 20 s (four missed beats). On `pagehide` the page sends a `bye` with `navigator.sendBeacon`. [design; sendBeacon from memory]
- **Do not infer presence from the SSE connection.** The server notices a dead client only on its first or second write after the close. With a 0.3 s heartbeat: 0.31 s after a reset and 0.62 s after a clean close. With a 10 s ping that is up to 20 s of ghost user. [tested]
- **Agents** appear too. `focus` is the branch they hold a claim on. `activity.state` is one of thinking, waiting, executing, finished (R4's agent status chip). `activity` comes from `live.json` (`phase`, `note`, `inflight[]`). [repo]
- **Broadcast** the whole roster, with the live claims, in an SSE `presence` event: once per change, merged per wake-up. Clients throttle their own focus updates to 4 per second. About 10 entries, 1.5 KB. Each message is a full snapshot, so a lost message is healed by the next. [design, tested]
- **What a person sees** [design]: a colored dot per person in the header; a colored outline on the node or cluster each one is looking at; on a claimed branch the label "Maya's agent is working here, 61 s left"; per agent a "seen up to #131" tick that moves when the agent takes a digest; optional "follow" on a person's chip.

### 4.2 Optimistic UI

- **What the sources say.** Figma: local changes apply immediately, and a server change for a property with an unacknowledged local change is discarded, to avoid flicker. [page] Replicache: apply the change to a local copy and queue it; when new server state arrives, rewind to the last server version, apply the patch, then replay the pending changes on top; pending changes with an id up to `lastMutationID` are dropped. [page] Linear, from the unofficial write-up: a rejected transaction runs its rollback. [page, unofficial]
- **Our version.** `view = server state, with my pending edits on top`. Tested in Node with a small reducer: my edit shows at once; Ben's edit arrives while mine is pending and the view does not flicker; the echo of mine arrives (server order: Ben, then me) and the view stays; a rejected edit rolls back; a repeated event is ignored. [tested] Code in Appendix A.4.
- **Three visible states, and one for failure.** The loop reads `control.json` only at stage boundaries [repo], so "queued" can last minutes. The UI must say that, or the person thinks the click was lost.

| State | Meaning | Suggested look |
|---|---|---|
| pending | Only on my screen. The POST has not returned. | dashed outline, 60% opacity |
| queued | The server numbered it (`seq`). Everyone sees it. The loop has not used it yet. | solid, small clock, "waits for the next step" |
| applied | A `control_applied` event lists this `seq`, with round and stage. | solid, check mark, tip "used by Maya's agent, round 2, ideated" |
| rejected | The server answered 409 or 422. | revert, toast with the reason |

- **Matching.** My own echo carries the same `op`. `control_applied.data.refs` lists `seq` numbers.
- **Honest wording for veto and choose.** They act at the next question pick, and the top 3 cannot be seen before the veto is applied. [repo, `00_requirements.md` section 5 item 1] The UI should say "acts at the next pick (round r+1)".
- **Smoothness.** Collect incoming events and apply them once per animation frame (`requestAnimationFrame`), so a burst of 50 events paints once. Keep DOM nodes keyed by stable ids so CSS transitions can run. Show a "Live, #seq" chip and a "Reconnecting" state. [design; rAF from memory]

## 5. The protocol for a one-day build

### 5.1 Envelope (one JSON object per event)

| Field | Type | Meaning |
|---|---|---|
| `seq` | int | Set by the server. Starts at 1. No gaps. The only order. Never sort by `ts`. |
| `ts` | string | Set by the server. UTC, ISO-8601, milliseconds, `Z`. |
| `kind` | string | The event name (section 5.2). |
| `by` | string | Actor id from the `X-Space-Actor` header, or `?me=` in the URL: `maya`, `maya.agent`, `server`. The body cannot override it. |
| `by_kind` | string | `human`, `agent` or `system`, from `X-Space-Kind` or `?kind=`. The demo does not prove identity: any client can say it is a human. |
| `owner` | string | The person the actor works for. Set by the server: from the roster entry, else the part of `by` before the first dot (`maya.agent` gives `maya`). A value in the body is ignored. [tested] |
| `subject` | string | Typed id of the thing: `node:<id>`, `sketch:<id>`, `cluster:<key>`, `idea:<id>`, `obj:<id>`, `cand:<id>`, `question:<id>`. |
| `label` | string | Human-readable name of the subject when written, up to 80 characters. Digests use it without a lookup. |
| `data` | object | Fields for this kind. Up to 64 KB per event. |
| `op` | string | Client idempotency key. Unique per `by`. Example `maya.agent-1792257346086-12`. |
| `base` | int | The head `seq` the author had seen. |
| `round`, `stage` | int, string | Loop clock. Agents only. |
| `claim` | int | Fencing token. Agent writes to a claimed branch. |
| `cause` | int | Optional. The `seq` of the event this one reacts to, so a screen can say "because Ana vetoed Q3". |

The client sends `kind`, `subject`, `label`, `data`, `op`, `base` and optionally `round`, `stage`, `claim`, `cause`. The server adds `seq`, `ts`, `by`, `by_kind`, `owner`. Ids reuse the loop's ids. Cluster ids are positional and move between groupings [repo], so clusters get a stable `key` from their member lists. Do that in one place. R1's `ViewLib` already matches cluster identity in the browser (Jaccard 0.3, greedy), and because every client replays the same ordered log, every client computes the same keys. Then the bridge can send the loop's own ids and member lists.

### 5.2 Event names (36, of which 26 are needed on day one)

"Loop key" shows which `control.json` key the bridge fills from a person's event. [repo for the keys]

| `kind` | Written by | `data` keys | Loop key | Day 1 |
|---|---|---|---|---|
| `space_opened` | server | `space_id, epoch` | | yes |
| `node_added` | bridge, person | `id, name, parent, frame?, origin (map, human, off, fail_q), directions?` | `add_nodes` | yes |
| `node_edited` | person | `fields {name?, frame?, note?}`. The server may add `overwrote [{field, seq, by}]`. | none, display only | yes |
| `node_skipped`, `node_unskipped` | person | none (the subject is the node) | `skip_nodes` | yes |
| `sketch_batch` | agent | `node, direction, count, items [{id, idea, mechanism?}]` | none | yes |
| `cluster_snapshot` | agent | `node, direction, clusters [{key, name, members[], rank?, selected?, lane?, prior?}]`. It replaces the last snapshot of the same node and direction. | `exclude_clusters` (by name) | yes |
| `objection_raised` | agent | `node, idea, id, cls, severity, text, if_true?` | none | yes |
| `reply_posted` | agent, person | `node, objection, kind (concede, rebut, measure), text, fact?, source? (script, measured, web, belief)` | none | yes |
| `objection_marked` | agent | `node, objection, verdict (resolved, revised, standing), reason` | none | yes |
| `comment_posted` | person | `target, text` | proposed in the repo, not built | later |
| `candidate_built` | agent | `node, cand, idea, cluster?, lane?` | none | later |
| `test_result` | agent | `node, cand, status (win, tie, loss, failed_check, not_built), rung?, metrics{}, reason?` | none | yes |
| `memory_added` | agent | `node, section, text, source` | none | later |
| `question_picked` | agent | `top3 [{id, name, score}], chosen, by_rule (default, person, default_after_veto), vetoed[]` | none | yes |
| `question_vetoed`, `question_unvetoed` | person | none (the subject is the question) | `veto` | yes |
| `question_chosen` | person | none. The server may add `overwrote` (the person it replaced). | `choose` | yes |
| `opinion_given` | person | `target, score (1 to 10), note` | `opinions` (who = `by`) | yes |
| `note_posted` | person | `text` (up to 600 characters) | `note` | yes |
| `seed_added` | person | `node, text` (up to 1500) | owner-seeds file, round 1 only | later |
| `run_paused`, `run_resumed` | person | none. A pause has holders: the loop stays paused while any person holds one, and a resume removes only the sender's hold. | `pause` | yes |
| `run_stop_requested` | person | none | `stop_after_stage` | later |
| `stage_entered` | agent | `round, stage` | none | yes |
| `control_applied` | agent, bridge | `refs [seq...], round, stage, effect?` | none, this is the ack | yes |
| `digest_taken` | agent | `from_seq, to_seq, n, chars` (and `round`, `stage` on the envelope). The receipt: what this agent was told, and at which step. | none | yes |
| `vote_cast` | person | `idea, value (+1 or -1)` | proposed in the repo, not built | later |
| `fact_disputed` | person, agent | `node, fact, reason, source?` | proposed in the repo, not built | later |
| `question_asked` | person | `node, text, test?, threshold?` | `add_nodes` (a question node) | later |
| `node_merged` | server, bridge | `id, into, similarity` | none | later |
| `claim_granted` | server only | `owner, ttl_s, purpose?` (a line of plain words about what the agent will do, for R4's intent card). `cause` on the envelope. | other loops' `skip_nodes` | yes |
| `claim_released` | server only | `owner, reason (done, abort)` | | yes |
| `claim_expired` | server only | `owner_was, reason?` | | yes |
| `claim_taken_over` | server only | `from, to` | | yes |
| `event_retracted` | person, agent | `target_seq, reason` | none | later |

The server reads only these kinds: `node_added` (parent map, `id_taken`), `node_edited` and `question_chosen` (the overwrote hint), `node_skipped`, `node_unskipped`, `question_vetoed`, `question_unvetoed` (the closed set), and the `claim_*` and `space_opened` kinds (server only: posting them is refused). Every other kind passes through after the envelope check, and `event_retracted` is handled by the views. That keeps the server small. Every agent event about a branch must carry `data.node`, because the claim check reads it. The `claim_granted`, `claim_released` and `claim_taken_over` events carry the holder as `by`. `claim_expired` is written by `server` with `by_kind` `system`. [design, tested]

### 5.3 Messages on the SSE stream

| SSE `event:` | `data` | When |
|---|---|---|
| (none, so `message`) | one envelope. The `id:` line is the `seq`. | each durable event |
| `hello` | `{space_id, epoch, head, server_time_ms, claims [], roster []}` | right after connect |
| `presence` | `{clients [...], claims [...]}`, the full roster and the live claims | once per change, merged per wake-up |
| `ping` | `{head, claims []}` | every 10 s when idle. Lets the page check that nothing was missed and refresh claim times. |
| `reset` | `{reason}` | `since` is ahead of the head. The page drops its state and reloads from `seq` 0. (A changed `epoch` in `hello` has the same effect. The browser module checks it.) |

The first line of a stream is `retry: 1000`. `data:` is always one line of JSON. [tested]

### 5.4 Routes (7)

| # | Route | Who | What |
|---|---|---|---|
| 1 | `GET /` and any path that does not start with `/api/` | browser | The UI files, from the web folder. Same origin as the API, so no CORS. Path traversal is blocked. [tested] |
| 2 | `GET /api/events?since=N&limit=500&wait=0..25` | browser, agent | Read the log after `N` (up to 2000 per call). Used for catch-up, long-poll and by agents. Answer `{epoch, head, events}`. |
| 3 | `GET /api/stream?since=N` | browser | SSE. `Last-Event-ID` wins over `since` when both are present. |
| 4 | `POST /api/events` | browser, agent | Append one event, or `{"events":[...]}` (up to 100; consecutive numbers, one result per event). Answer `{seq, dup, overwrote?}`, or `{results: [...]}` for a batch. |
| 5 | `POST /api/claims` | agent, person | `{action: acquire, renew, release, takeover; subject; ttl_s?; token?; purpose?; cause?}`. Answer `{token, ttl_s}` or 409. `takeover` is for people only. |
| 6 | `POST /api/presence` | everyone | Heartbeat: `{client, name, owner?, view, focus, activity, cursor, claims [{subject, token}], bye?}`. Answer `{head, claims_ok, interrupts []}`. Renews the claims the caller lists, and reports the ones it lost. |
| 7 | `GET /api/digest?agent=ID&since=N&cap=1200` | agent | Answer `{text, from_seq, to_seq, n}`. Empty `text` when there is nothing to say. With `since=0` it looks at the last 60 events. |

Errors are JSON: `{error, ...}`. Codes: 422 `bad_envelope` or `unknown_kind`; 409 `claimed_by_other` (with `held_by`, `ttl_left_s`), `claim_lost`, `subject_closed`, `id_taken`; 415 `bad_content_type`; 413 `too_big`; 403 `bad_key` or `humans_only`. Add `Cache-Control: no-store` to every JSON answer. [design; the header from memory]

### 5.5 Rules the server enforces

1. Check the envelope. Cut unknown top-level fields. Remove `obvious`, `obvious_match` and `private` keys anywhere in `data`. Refuse a body over 64 KB (413). [tested; the private fields come from the repo]
2. Be idempotent on (`by`, `op`). A repeat returns the first `seq` with `dup: true`. Look the key up first. Never use `ON CONFLICT DO NOTHING`. [tested]
3. Under one lock: `BEGIN IMMEDIATE`, insert, commit, add to the in-memory list, then notify the waiting handlers. [tested]
4. Refuse `claim_*` kinds posted by clients (422). Claims are the server's business. [design]
5. Guarded kinds from agents: for a node under another actor's claim, 409 `claimed_by_other`. A wrong or expired token gets 409 `claim_lost`. [tested]
6. Closed subjects: an agent event under a node a person skipped gets 409 `subject_closed`. A person's event is never refused for this reason. (A veto acts at the next question pick, so the reference code does not check vetoed questions.) This follows "people steer, tests decide" and "nothing is deleted" (R34, R35). [repo, design]
7. Last-writer-wins fields (`node_edited`, and `question_chosen` as the single slot "next question") are always accepted. If another actor changed the same field after `base`, the answer and the stored `data` carry `overwrote [{field, seq, by}]`, so the UI can offer an undo. The author's own earlier edits, and edits made after seeing the other one (`base` at or past it), do not count. [tested]
8. `node_added` with a used id gets 409 `id_taken`. The loop would drop it silently. [repo, design]
9. A reaper thread runs every 5 s and writes `claim_expired`. [design; `reap()` tested, the timer thread only smoke-tested]
10. At start: load the log. For every claim still open in the log, write `claim_expired` with reason `restart`. Make a new `epoch` only for a new database. [tested]
11. Presence stays in memory. An entry drops after 20 s without a beat. [design]
12. The server never calls a model. [design]
13. Read the whole request body before any early reply (403, 413, 415). If a reply goes out with the body unread, Windows resets the connection and the client sees WinError 10053 instead of the error. It showed up once in two runs, which is the sign of a race. [tested]
14. `ENFORCE_CLAIMS` (default True) can be set to False. Claims are then advisory for agents too: the write is accepted, `data.warn` and the answer carry the reason, and the UI shows a chip. A skipped node still blocks agents in both modes. [tested]
15. Bind to 127.0.0.1. For a second laptop start with `--lan`: bind 0.0.0.0, print a random key, and require it as the header `X-Space-Key` on POST and as `?key=` on the stream, because `EventSource` cannot set headers [page]. Require `Content-Type: application/json` on POST. A page on another site cannot send that type without a CORS preflight, which the server never answers, so drive-by posts fail. [design; the CORS reasoning from memory]

### 5.6 Rules for the browser

1. Boot: open `connectSpace` with `since: 0`. The stream replays the whole log in order. Paint once `last` reaches the `head` in `hello`. (`GET /api/events` pages of up to 2000 also work.)
2. Use the `connectSpace` module (Appendix A.3). It drops duplicates by `seq`, fills gaps, reopens after a 503 or after 25 s of silence (with backoff and jitter), and stops on a changed epoch. [tested in Node]
3. On `reset`, or a changed `epoch` in `hello`, the module stops and calls `onReset`. The page drops its state and calls `connectSpace` again with `since: 0`. The module also ignores late events after it stops: Node's `EventSource` delivered events from a swapped database after `close()` until I added that guard. [tested]
4. One `EventSource` per tab, one tab per person. The limit is 6 per browser and host on HTTP/1.x [page]. A starved page shows "Waiting for available socket". [page] The spec names a shared worker or unique domains as relief. [page] `127.0.0.1` and `localhost` count as two hosts. [memory]
5. Keep the pending overlay (A.4) and show the four states.
6. Apply incoming events once per animation frame.
7. Show a connection chip: Live #seq, Reconnecting, Offline.
8. Presence beat every 5 s. `sendBeacon` a `bye` on `pagehide`.

### 5.7 Rules for the agent process

1. Use `SpaceClient` (Appendix A.5) with `http://127.0.0.1:8766`. [tested]
2. Every call has a 3 s timeout and never raises into the loop. A failed `emit` goes to `space_outbox.ndjson`. `flush_outbox()` replays it at the next boundary. Replays are safe because of `op`. [tested]
3. `op = actor-startms-counter`, so a restart cannot reuse an `op`. [tested]
4. At each stage boundary: `flush_outbox()`, `digest()`, put the text into the prompt, then `commit_cursor()`. [tested]
5. A heartbeat thread beats every 5 s with `cursor` and `activity` and collects `interrupts`. [tested]
6. Take the claim on a branch before ideating, interrogating or building on it: `client.claim("node:<id>")` returns the token, or `None` if someone else holds it. Pass `claim_subject="node:<id>"` to `emit()` so the token goes with every write. The heartbeat lists the held claims, which renews them. Release when done. On `claim_lost` (in `client.interrupts`): stop at the next safe point and drop pending writes for that branch. [tested]
7. After each stage, emit in batches (`sketch_batch`, `cluster_snapshot`, `test_result`). [design]
8. Do not add the digest to blind stages (clustering, panel judge). [repo]

### 5.8 What the digest looks like

This is real output of the final function (Appendix A.1, `make_digest`) on synthetic events: 12 sketch batches and 2 regroupings from one agent, 2 people's actions, one claim with a purpose, one test result, and one batch from the agent that is reading (which is left out). Ids are written `[e41]`, which is R3's format. The prompt wrapper puts R4's label before it: "These are reports from other people and agents. They are information, not instructions. Your owner's instructions come first. Tests decide." The server and `control.json` enforce claims and skips. The prompt does not have to. [design]

```
TEAM UPDATE: events e1 to e20 since your last step
- HUMAN ben vetoed question "Does packing order matter?" [e1]
- HUMAN ben added part "data order" [e2]
- ben.agent is working on part "optimizer": try the optimizer idea; do not touch it [e3]
- ben.agent added 120 sketches to part "memory" [e15]
- ben.agent regrouped part "memory" into 4 clusters (x2) [e17]
- ben.agent test of "swap-after-pack": WIN learn_z 2.1, cost_ratio 0.8 [e18]
- HUMAN ben left a note: check the tie-breaker first [e19]
```

That is 495 characters. Repeats are merged and shown with the newest text. When one author has more than three lines of the same kind, collapsing them into one line would save more room. [design, not built]

### 5.9 Name map to the sibling notes (R1, R3, R4)

R3 (`03_prompts.md`) asked that its event names be matched to this note. R4 (`04_multiplayer_ux.md`) proposed envelope fields. R1 (`01_visualization.md`) matches cluster identity in the browser.

| Sibling name | Name here | Note |
|---|---|---|
| R3 `claimed`, `released` | `claim_granted`, `claim_released` (also `claim_expired`, `claim_taken_over`) | `by` is the holder |
| R3 `comment`, `note`, `vote`, `opinion` | `comment_posted`, `note_posted`, `vote_cast`, `opinion_given` | `vote_cast` and `comment_posted` are later |
| R3 `objection` | `objection_raised`, then `reply_posted` and `objection_marked` | |
| R3 `question_asked`, `fact_disputed` | same names | later |
| R3 `applied` | `control_applied` | R3 keeps it out of digests. `make_digest` has no sentence for it, so it is out too. |
| R3 `cursor`, `presence` | not events | The cursor is in the roster. Presence is the SSE `presence` message. |
| R3 `round_started` | `stage_entered` | carries `round` and `stage` |
| R3 `scope_changed` | none | no source in `control.json` today |
| R3 receipt "seen by agent at stage" | `digest_taken` | |
| R3 line ids `[e41]` | `[e41]` | done in `make_digest` |
| R4 `target`, `payload` | `subject`, `data` | |
| R4 `ts_utc` | `ts` | UTC |
| R4 `via` | `by` (the agent) plus `owner` (the person) | `ana.agent` acting for `ana` |
| R4 `cause_seq` | `cause` | |
| R4 `stage_applied`, `status` | not stored | `control_applied` names round and stage. A 409 is "rejected". Status is derived, so the log stays append-only. |
| R4 "a pause has holders" | `run_paused`, `run_resumed` per person | `pause` is true while any person holds one |
| R4 intent card | `claim_granted.data.purpose` and `cause` | the card is a view over the claim |
| R4 recommendation 10, advisory claims | `ENFORCE_CLAIMS = False` | section 3.2 |
| R4 `merged` | `node_merged` | later |
| R1 cluster identity (Jaccard 0.3, greedy) | `cluster_snapshot.clusters[].key` | do it once, in the browser |

Two digest renderers now exist. `make_digest` here is generic, runs on the server and has no roles. R3's renderer (`03_prompts.md` section 8.3) has per-role closing lines, quoting rules and a checker. Both take the same input: events after a cursor, the reader's own events removed, private keys stripped. Suggested split: use R3's for prompts, and keep `make_digest` for the "what my agent was told" panel and as the default for an agent with no renderer. `GET /api/events?since=N` returns the rows R3's renderer needs. [design]

## 6. Pitfalls

Each row: what goes wrong, the fix, and the evidence.

### 6.1 Windows and `http.server`

| # | What goes wrong | Fix | Evidence |
|---|---|---|---|
| 1 | **`localhost` is slow from Python.** A connect to `localhost` took 2.03 s (127.0.0.1: 0.3 ms). `urlopen` took 2063 ms against 1.4 ms. `localhost` resolves to `::1` first, and a closed IPv6 port is refused only after about 2.05 s. | Use `127.0.0.1` in every URL. Print the URL at start. | [tested]. Stenberg: Windows keeps resending SYN to a closed port, "can easily take a few seconds" on localhost. His update says curl and Chrome added a workaround in 2026, so a browser may not show it. Python did. [page] |
| 2 | **Zombie server.** `HTTPServer.allow_reuse_address` is 1. A second server bound the same port without error and all 20 test requests went to the old one. | Set `allow_reuse_address = False`: the second bind then fails with WinError 10048. Optional: `SO_EXCLUSIVEADDRUSE` (WinError 10013 for the intruder). A restart right after close still worked in both cases. | [tested]. Microsoft: after a forced bind "the behavior for all sockets bound to that port is indeterminate". [page] |
| 3 | **Small listen backlog.** `request_queue_size` is 5. | Set 64. | [tested]. Python 3.15 changes the default to `SOMAXCONN`. [page] |
| 4 | **Dead SSE clients are found late.** The server learns only on the first or second write after the close. Errors: `ConnectionResetError` (WinError 10054) or `ConnectionAbortedError` (10053). | Catch `OSError`. Ping every 5 to 10 s. Take presence from heartbeats. | [tested] 0.31 s and 0.62 s with a 0.3 s ping |
| 5 | **Coarse clocks.** `time.monotonic()` and `time.time()` tick every 15.6 ms here. My first latency run showed only 0, 16 and 32 ms. | Use `time.perf_counter()` to time things. `monotonic()` is fine for 90 s leases. | [tested] |
| 6 | **HTTP/1.1 keep-alive trap.** Every reply then needs an exact `Content-Length`, and a request body you do not read breaks the next request. | Stay on the default HTTP/1.0 for the demo. The stream sends `Connection: close`. | "your server must then include an accurate Content-Length header ... in all of its responses". [page] |
| 7 | **Ctrl+C does not stop the server** if the main thread sits in a wait with no timeout. | Keep `serve_forever()` in the main thread. Give every wait in other threads a timeout. | [memory] |
| 8 | **One thread per connection.** | Fine at 30 clients (67 threads). Do not plan for hundreds. | [tested] |
| 9 | **Firewall prompt.** Listening on all interfaces usually triggers it the first time. Loopback does not. | Run once before the event. Or add a rule as admin: `netsh advfirewall firewall add rule name="HTSA space" dir=in action=allow protocol=TCP localport=8766 profile=private`. | [repo, memory] |
| 10 | **Reply before reading the request body.** A 403 or 413 sent while the POST body was still unread: Windows reset the connection and the client saw WinError 10053 instead of the error. It showed up once in two runs, so it is a race. | Read the whole body first, then check key, type and size. 20 repeats of the 403 now pass. | [tested] |

### 6.2 SQLite and the log

| # | What goes wrong | Fix | Evidence |
|---|---|---|---|
| 11 | **`ON CONFLICT DO NOTHING` and `INSERT OR IGNORE` burn a sequence number.** The log read 1, 3. | Look the `op` up first under the writer lock. Or plain `INSERT`, catch `IntegrityError`, `ROLLBACK` (read 1, 2). | [tested] |
| 12 | **Deferred transaction that reads, then writes.** "database is locked" after 0.19 ms, with a 5000 ms timeout. | `BEGIN IMMEDIATE` inside one Python lock. | [tested] |
| 13 | **A shared writer connection sees uncommitted rows.** | Readers use the in-memory list, never the writer connection. | [tested] |
| 14 | **Notify before commit.** A reader can miss the event or read stale data. | Notify after commit. Check `head > last` inside the condition lock before waiting. | [design, tested] |
| 15 | **New database, same URL.** `seq` restarts and old clients hold a bigger number. | `epoch` in `hello`: the module stops when it changes. `reset` when `since` is ahead of the head. The module ignores events that arrive after it stopped. | [tested] both cases |
| 16 | **Python `sqlite3` implicit transactions.** `executescript` commits first. The default busy `timeout` is 5 s. | `isolation_level=None` and explicit `BEGIN IMMEDIATE`. | [page] |
| 17 | **WAL file grows** when readers always overlap. `synchronous=NORMAL` can lose the last commits on power loss. | Not an issue here because readers use memory. Checkpoint at start. Accept the loss for a demo. | [page] |
| 18 | **Big events.** | Cap at 64 KB. Send titles, not full texts. Use `sketch_batch`. | [design] |

### 6.3 SSE and the browser

| # | What goes wrong | Fix | Evidence |
|---|---|---|---|
| 19 | **A non-200 on reconnect kills `EventSource` for good.** After a 503 the state was CLOSED and no more requests came. | The `connectSpace` watchdog: reopen with backoff and `?since=<last>`. | [page]; [tested] with Node's `EventSource` |
| 20 | **A new `EventSource` sends no `Last-Event-ID`.** Only the browser's own reconnect does. | Pass `?since=<last seq>` on every open. The server prefers the header. | [page]; [tested] |
| 21 | **Comment lines (`:`) are invisible to JavaScript.** A comment keeps a proxy awake but tells the page nothing. | Send a named `ping` event with `head`. | [page] |
| 22 | **No custom headers on `EventSource`.** | Put the key in the query string. | [page] |
| 23 | **6 connections per browser and host on HTTP/1.x.** Chrome and Firefox closed the bug as "Won't fix". Each open stream holds one. One site had five tabs starve all other requests. | One tab per person. A shared worker, or unique domains, if needed. | [page] MDN, spec, Lawrence |
| 24 | **Proxies and antivirus may buffer or cut idle streams.** One forum report had heartbeats arrive while data events did not. | Ping every 5 to 10 s. Test on the real network. Keep the long-poll fallback. | [memory]; the spec suggests a comment about every 15 s [page]; the forum report [snippet] |
| 25 | **Nagle and delayed ACK** can add tens of milliseconds over a real network. Not seen on loopback: p95 was 1.4 ms or less in all four combinations (one or three writes per event, Nagle on or off). | Build each frame as one `bytes` and make one `write()`. Set `disable_nagle_algorithm = True`. | [tested] on loopback only; the network claim is [memory] |
| 26 | **A missed event.** The page sees 12, then 14. | Gap check on every event, and on `ping.head`: fetch `/api/events?since=12`. | [tested] in Node with a fake `EventSource` and `fetch`: gap filled from 3, a duplicate ignored, ping catch-up from 7 |

### 6.4 Conflicts and agents

| # | What goes wrong | Fix | Evidence |
|---|---|---|---|
| 27 | **Two people edit one field.** | Last-writer-wins by `seq`. The loser gets an `overwrote` chip with undo. Text fields do not merge. | [page] Figma |
| 28 | **A lease without a token is unsafe.** A paused holder can write after it lost the claim. | Fencing token = `seq` of the grant. Check it on every guarded write. | [page] Kleppmann; [tested] |
| 29 | **A claim is never released** (crash, forgotten release). | TTL plus a reaper that writes `claim_expired`. | [page] Claude Code teams |
| 30 | **A slow or frozen PC misses heartbeats.** | TTL 90 s. Heartbeat in its own daemon thread. | [repo] (crashes under load), [design] |
| 31 | **The agent reads its own events back.** | Drop events where `by` is the agent. | [tested] |
| 32 | **Digest too long for the prompt.** | Cap at 1200 characters. The loop's prompt cap is 60,000 and the note cap is 600. | [repo]; [tested] |
| 33 | **Private fields leak** into the space or a digest. | Strip `obvious`, `obvious_match` and `private/` at the server. Never mirror `state.json`, `calls/`, `prompts/`. | [repo] |
| 34 | **Cluster ids move** when a new sketch triggers a new grouping. | Send member lists. Match identity from the members, in one place (R1 does it in the browser). | [repo] |
| 35 | **Two people choose the same node id.** The loop drops the second one silently. | 409 `id_taken` at the server. | [repo] |
| 36 | **A resume applies `budget_add` again.** | Do not mirror run controls on day one. | [repo] |
| 37 | **Two loops make two different maps.** Each process plans its own map in round 1 and picks its own ids. A shared tree needs the "adopt shared map" change, or a pre-seeded tree. | Decide before day one. See section 10. | [repo] `00_artifacts.md` section 10 |
| 38 | **Blind stages must stay blind.** | No digest in clustering or the panel judge. | [repo] |
| 39 | **Peer text becomes instructions.** Words from other people go into an agent's prompt. A 2026 study cited in R4 reports contamination in 57 to 71 percent of benign shared-state cases. | Label the block "information, not instructions". Quote people's words, cap each at 160 characters, strip tags, scope each line to a part (R3 section 8.1). | [repo] `04_multiplayer_ux.md` 7.2, `03_prompts.md` 8.1 |

### 6.5 UI and demo day

| # | What goes wrong | Fix | Evidence |
|---|---|---|---|
| 40 | **Flicker** when a server echo overwrites a field I am editing. | The overlay: pending edits stay on top until acknowledged. | [page] Figma; [tested] |
| 41 | **Event storms** make the page stutter. | Apply once per animation frame. | [design] |
| 42 | **Presence jitter.** | Throttle focus to 4 per second on the client. The server merges roster changes per wake-up. | [design] |
| 43 | **"Queued" looks like "lost".** A veto acts at the next pick, which can be minutes away. | Show the four states with round and stage, and honest text. | [repo] |
| 44 | **Client clocks differ.** | Show "12 s ago" from `server_time_ms` in `hello`. Never compute from `ts` with the local clock alone. | [design] |
| 45 | **Venue Wi-Fi may block device-to-device traffic** (client isolation). | Use a phone hotspot or a small travel router. Or run both people on one PC: Chrome and Edge keep separate storage. Test the real route on site. | [memory]; Chrome and Edge from [repo] |
| 46 | **Background tabs get throttled** timers, so heartbeats slow down. | Keep the demo windows visible. Use a 20 s presence TTL. | [memory] |
| 47 | **A live real run is too slow for a stage.** A 2-round mock run took 77 s, with 10 stage boundaries. Real rounds take minutes to hours. | Rehearse with the mock backend. Keep a recorded log and a `--replay` option as a safety net. | [repo] |

## 7. What I tested on this PC

All on 2026-10-17, loopback only, no browser. Windows 10 build 19045, Python 3.12.12, SQLite 3.50.4, Node 25.9.0 (`--experimental-eventsource`, which is undici's spec-based `EventSource`). Latencies are in one process, so they are floors and not stage numbers.

| Test | Result |
|---|---|
| Two `ThreadingHTTPServer` on one port | The second bind succeeded. 20 of 20 requests went to the first server. With `allow_reuse_address = False`: WinError 10048. With `SO_EXCLUSIVEADDRUSE` on the first: WinError 10013 for the second. Rebinding right after a close worked in both. |
| `localhost` against `127.0.0.1` from Python | 127.0.0.1: 0.26 to 0.37 ms. `localhost`: 2027 and 2039 ms. `::1`: refused after 2053 ms. `urlopen`: 2063 ms against 1.4 ms. `localhost` resolves to `::1` first. |
| Event log, SSE, long-poll, resume | 4 writers, 240 events, 36 retried POSTs, 3 readers. Each reader saw exactly 1 to 240. One SSE reader was reset in the middle and resumed with `Last-Event-ID`: no gap, no duplicate. All 36 retries returned the original `seq`. Database rows 240, distinct ops 240. A client with `since` ahead of the head got `reset`. |
| Dead client detection, 0.3 s ping | After a reset: 0.31 s (`ConnectionResetError`, WinError 10054). After a clean close: 0.62 s (`ConnectionAbortedError`, 10053). |
| Nagle, one or three writes per event, 40 events 3 ms apart | p95 between 0.4 and 1.4 ms in all four combinations. No effect on loopback. |
| Claims race, fencing, expiry | 8 racers, 1 winner. After expiry a new owner got a higher token. The stale write and renew got 409. |
| SQLite | See pitfalls 11 to 14 in section 6. |
| Digest function | Caps 400, 800, 1200 gave 332, 735, 731 characters. Human lines kept. Own events hidden. |
| `os.replace` with an open reader | 8 retries, 410 ms, then success. |
| 30 SSE clients | All connected within 0.03 s. 67 threads. Broadcast p50 2.5 to 3.2 ms, p95 4.2 to 8.9 ms. Every client got exactly 1 to 5. |
| Node `EventSource` against the server | First request had no `Last-Event-ID`. After a reset: `error` event, reconnect after 1.0 s with `Last-Event-ID: 15`, events 16 to 41, no gap. A 503 on reconnect: `readyState` 2, no more requests. Manual reopen with `?since=41`: events 42 to 102, contiguous. |
| `connectSpace` module in Node | Reset (browser reconnects), 503 (module reopens), 3 s of silence (watchdog reopens): ended 161 of 161, contiguous. Run again against the reference core: reset and 503, ended contiguous, 162 events. A server that swapped to a different database (new epoch, head 61 against the client's 31): one `onReset`, no event from the other database accepted. |
| Gap and ping paths of `connectSpace` | Fake `EventSource` and `fetch` in Node. Events 1, 2, 3, then 5: the module fetched from 3 and delivered 4 and 5 in order. A repeated 5 was ignored. A `ping` with head 10 at 7 made it fetch from 7. Delivered 1 to 10 exactly once. |
| Client store (overlay) in Node | Pending shows at once. No flicker when another person's edit arrives. Echo moves it to queued. `control_applied` moves it to applied. A reject rolls back. A repeated event is ignored. |
| `SpaceClient` | Emit, digest with the two-step cursor, claim, renewal by heartbeat (a 1 s claim survived 2.4 s), expiry after the beats stopped, outbox while the server was down (1 event), replay (flushed 1, then 0), a restarted process starting from its saved cursor, and the `digest_taken` receipt written by `commit_cursor(round, stage)`. |
| **Reference core** (Appendix A.1) | 68 checks, 3 runs in a row, 0 failures: subtree claims, fencing, human override, closed nodes, `id_taken`, the overwrote hint (also for `choose`), `cause`, claim `purpose`, advisory mode, private-key stripping, owner stamping, idempotency, batch, 415/413/422, presence on the stream, digest, resume, long-poll, static files and path traversal, restart, key. Stress: 320 events and 64 retries from 4 writers, 4 readers (one reset): each saw exactly 1 to 321. Database and memory log agree. |
| Stdlib facts read at run time | `HTTPServer.allow_reuse_address` is 1. `ThreadingHTTPServer.daemon_threads` is True. `TCPServer.request_queue_size` is 5. `StreamRequestHandler.wbufsize` is 0 and `disable_nagle_algorithm` is False. `protocol_version` is `HTTP/1.0`. No WebSocket module. `time.monotonic()` and `time.time()` have 15.625 ms resolution here, `perf_counter()` has 100 ns. |

The test scripts are in the session scratchpad, folder `r2rt` (`checks_a.py`, `checks_b.py`, `check_core_a.py`, `stress_core.py`, `es_test2.mjs`, and others). They are not in the repo. The tested code is in Appendix A.

## 8. Handoff to the design stage: what the views can rely on

The owner asked that the design part use the `fable` model (this came with the request that started this workflow). This note is research only and calls no model. Section 8 is the contract between the sync layer and the views. `00_environment.md` section 6 says each fable call has a large fixed cost (about 48k tokens), so a few big calls beat many small ones. [repo]

1. **The screen is a function of the log.** `state = reduce(events)`, then the pending overlay on top (Appendix A.4). Ids are stable: node ids, sketch ids, objection ids, candidate ids, and cluster `key`. Use `ts` for display only. Never sort by it.
2. **Clusters can animate.** Each `cluster_snapshot` replaces the last one for the same node and direction. Keys are stable across regroupings because identity is matched from member lists (R1's `ViewLib` does this in the browser). Diffing two snapshots gives: appeared, disappeared, members moved from key A to key B (a merge or a split), rank changed, `selected` changed. Animate with FLIP (measure, change, play) and keep DOM nodes keyed by `key`. [design]
3. **The tree.** `node_added` order is creation order. `origin` styles a node (map, human, off, failure question). `node_skipped` fades it. A claim outlines it in the holder's color and shows time left. Counts per direction come from `sketch_batch.count`, `cluster_snapshot`, `candidate_built` and `test_result`. [repo for the fields: `00_artifacts.md` 9.5]
4. **Arguments.** One chain per idea: `objection_raised`, then `reply_posted`, then `objection_marked`. At most two exchanges, nothing dropped. [repo R6]
5. **Results.** `test_result.status` gives the color. Losses and failed checks stay visible, because they are evidence. [repo R7]
6. **Live parts.** Presence chips, focus outlines, "seen up to #N" ticks, the four edit states, and a connection chip. Section 4 has the data for each.
7. **Bursts, then silence.** A stage writes its events at the end of the stage, so the screen gets a burst and then nothing for minutes. A mock run does ideation in about one second [repo], so animations must cope with a burst of hundreds of events. Between bursts, show the agents' `activity` text from presence so the screen does not look dead. [design]
8. **Offline libraries.** A CDN may fail on stage. Copy the libraries into the repo and serve them from the same server. `curl.exe` is on the PC. [repo, `00_environment.md` section 8]
9. **What the digest panel can show.** A "what my agent was told" box with the digest text is cheap and makes the idea of "each agent knows what the others changed" visible to a judge. [design]

## 9. One-day build order, and the moments to show

### 9.1 Build order (about 9 hours of work, so one long day with a buffer)

| Step | Hours | Done when |
|---|---|---|
| 1. Server | 1.0 | Appendix A.1 runs with `python space_core.py`. Two scripts post events, two readers see the same numbers, and a reader that is cut off and reconnects sees no gap. (The 68 checks are in the session scratchpad, folder `r2rt`, file `check_core_a.py`. They are not in the repo.) |
| 2. Agent client and loop hook | 1.0 | `SpaceClient` is called at each `_stage` boundary: flush, digest, prompt, commit (with round and stage, which writes the receipt). A mock run shows digests in the prompt. If the loop cannot be changed, use the `note` path (600 characters). |
| 3. Bridge | 2.0 | Run files become events (start with `node_added`, `sketch_batch`, `cluster_snapshot`, `test_result`). Human events become `control.json` with the merge rules. `control_applied` is written from `control_log.jsonl`. `pause` is true while any person holds a pause. |
| 4. Browser | 3.0 | Reducer, store, `connectSpace`, two views fed by the store (the design stage supplies the look), presence chips, four edit states, connection chip. |
| 5. Rehearsal | 1.5 | Mock backend, zero tokens [repo]. Chrome and Edge play two people [repo]. Drills: kill and restart the server; kill an agent; pull the network for 10 s; two vetoes at the same moment; reload a page in the middle of a burst. |
| 6. Safety net | 0.5 | Dump the log. A `--replay` option feeds a recorded log into a fresh server, as fast as you want. |

### 9.2 Moments that make the sync visible to a judge

1. Two people join. Two colored dots appear on both screens.
2. Maya's agent takes the branch "optimizer". Ben's screen outlines it in Maya's color with "61 s left".
3. Ben vetoes a question. On Maya's screen it appears at once as queued, then turns to applied when her agent picks it up.
4. The "what my agent was told" box shows the digest that starts with Ben's veto.
5. Ben tries to add a part with Maya's id, or edits a field Maya just changed. A chip says "overwrote Maya's change, undo".
6. The network drops for 5 s. A "Reconnecting" chip shows, then the screen catches up with no lost event.
7. Optional: someone takes over a claim with one click.
A search found that a YC Fall 2026 request describes the same story: teammates see the agent's progress live and can hand off a running task. [snippet]

## 10. Not checked, and open decisions

**Not checked**

- A real Chrome or Edge talking to this server. I used Python's `http.client` and Node's spec-based `EventSource`, which is marked experimental. A 1-minute manual check is cheap.
- Two machines on Wi-Fi: the firewall, client isolation, Nagle over a real network, antivirus buffering.
- A long soak test (hours). A reducer holding thousands of events in a real page.
- HTTP/1.1 keep-alive mode. The reference core stays on HTTP/1.0.
- `fetch` streaming as a replacement for `EventSource` (it allows headers and POST) [memory].
- Python 3.14. Only 3.12.12 was tested.
- The hackathon page and the judges' wording.
- The fetch tool gives short extracts made by a small model. Long claims were not cross-checked unless two sources agree.

**Open decisions** (for the owner or the next stage)

1. **One tree for two agents.** Each loop plans its own map in round 1 and picks its own ids. A shared tree needs the "adopt shared map" change or a pre-seeded tree. Or one loop with two people steering. [repo, `00_artifacts.md` section 10]
2. **Digest slot.** A `peer_digest` field in the loop (small code change), or the `note` path (600 characters, no change).
3. **Names and identity.** A name typed at join is fine for a demo, but the server does not prove who is a human or an agent. A named login is still open (R30). [repo]
4. **Who may take over a claim.** The reference code lets any person.
5. **The numbers.** Claim TTL 90 s, heartbeat 5 s, presence TTL 20 s, digest cap 1200 characters are guesses. Tune them in rehearsal.
6. **Where the space lives.** `D:\AGI-lab\spaces\<space_id>\space.db` is suggested. [repo]

## 11. Sources

Pages I opened through the fetch tool ([page]) and what each backed:

| Page | Backed |
|---|---|
| https://www.figma.com/blog/how-figmas-multiplayer-technology-works/ | Server authority, per-property last-writer-wins, ignore echoes for unacked fields, cycles, reconnect |
| https://www.figma.com/blog/realtime-editing-of-ordered-sequences/ | Fractional indexes, unique position on a tie |
| https://html.spec.whatwg.org/multipage/server-sent-events.html | Stream format, `Last-Event-ID`, `retry`, failing the connection, no headers, chunking warning, connection limit advice |
| https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events | 6-connection limit, comments hidden from JavaScript, named events |
| https://textslashplain.com/2019/12/04/the-pitfalls-of-eventsource-over-http-1-1/ | Five tabs starved requests, workarounds, WebSocket per-host limits |
| https://docs.python.org/3/library/http.server.html | `ThreadingHTTPServer`, `protocol_version`, "not recommended for production" |
| https://docs.python.org/3/library/socketserver.html | `daemon_threads`, `request_queue_size`, `handle_error` |
| https://docs.python.org/3/library/sqlite3.html | `check_same_thread`, `timeout`, `isolation_level`, `autocommit`, `executescript` |
| https://www.sqlite.org/wal.html | One writer, same host only, `synchronous=NORMAL`, WAL growth |
| https://www.sqlite.org/autoinc.html | `AUTOINCREMENT` never reuses numbers |
| https://www.sqlite.org/lang_transaction.html | Deferred, immediate, exclusive |
| https://martin.kleppmann.com/2016/02/08/how-to-do-distributed-locking.html | Leases, pauses, fencing tokens, efficiency against correctness |
| https://code.claude.com/docs/en/agent-teams | Shared task list, claiming with file locking, stuck tasks, one owner per file, automatic message delivery |
| https://www.anthropic.com/engineering/multi-agent-research-system | Duplicate work without clear boundaries, 15x tokens, coordination limits |
| https://cognition.com/blog/dont-build-multi-agents | "Actions carry implicit decisions" |
| https://doc.replicache.dev/concepts/how-it-works | Optimistic mutations, rebase, `lastMutationID`, poke and pull |
| https://github.com/wzhudev/reverse-linear-sync-engine | Sync id, delta packets, rollback. Unofficial write-up. |
| https://martinfowler.com/eaaDev/EventSourcing.html | Event sourcing, replay, snapshots, reversal |
| https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing | Immutable events, compensating events, idempotency, event design, when not to use |
| https://docs.yjs.dev/api/about-awareness | Presence as small JSON state, 30 s timeout, regular beat |
| https://docs.yjs.dev/ecosystem/connection-provider/y-websocket | Node server for Yjs |
| https://pypi.org/project/pycrdt/ | pip package, Rust core, Windows wheels, Python 3.11 or newer |
| https://automerge.org/docs/hello/ | Languages listed, network-agnostic sync |
| https://liveblocks.io/pricing | Free plan: 10 connections per room. Self-hosting on Enterprise only. |
| https://liveblocks.io/docs/collaboration-features/multiplayer/sync-engine/liveblocks-storage | Presence temporary, Storage persistent |
| https://liveblocks.io/blog/introducing-feeds-and-apis-for-agent-workflows | Feeds for agent logs, cloud REST with a secret key |
| https://blog.cloudflare.com/cloudflare-acquires-partykit/ | PartyKit is part of Cloudflare, Durable Objects |
| https://supabase.com/docs/guides/realtime and https://supabase.com/docs/guides/local-development | Broadcast, Presence, Postgres Changes. Local needs a Docker-compatible runtime. |
| https://datatracker.ietf.org/doc/html/rfc6455 | WebSocket handshake and framing |
| https://daniel.haxx.se/blog/2024/08/14/slow-tcp-connect-on-windows/ | Windows resends SYN to a closed port, IPv6 localhost |
| https://learn.microsoft.com/en-us/windows/win32/winsock/using-so-reuseaddr-and-so-exclusiveaddruse | `SO_REUSEADDR` binds a port in use, behavior indeterminate |

Seen only in search summaries ([snippet]): the search for a stdlib WebSocket server (only third-party packages); SSE pitfall write-ups (tessl.io, a Gravitee mirror, connected.app, a ServiceStack forum thread); the YC Fall 2026 "multiplayer AI" request (modelence.com/yc-rfs-fall-2026/multiplayer-ai); Liveblocks presence wording. Not opened: those pages.

Tried and failed: `https://docs.liveblocks.io/platform/presence` (redirected, then 404 on the new path). The hackathon track page: not found by search.

Repo notes used ([repo]): `research_notes/product/multiplayer/00_requirements.md`, `00_artifacts.md`, `00_environment.md`.

## Appendix A. Tested code

All of this ran on this PC (section 7). It is plain standard-library Python and plain browser JavaScript. Copy it as it is. Suggested file names: `space_core.py`, `space_client.py`, `web/space_connect.mjs`, `web/store.mjs`.

### A.1 `space_core.py`: the server

The log, claims, presence, digest, SSE and all routes in one file. 68 checks passed on it 3 times in a row (section 7). Start it with `python space_core.py --db D:\AGI-lab\spaces\demo\space.db --port 8766 --web web`. Add `--lan` for a second laptop: it binds 0.0.0.0 and prints the key.

```python
"""space_core.py - shared space server core. Standard library only. Written for Windows + Python 3.12."""
import http.server, json, secrets, sqlite3, threading, time, urllib.parse

GUARDED = {"sketch_batch", "cluster_snapshot", "objection_raised", "reply_posted", "objection_marked",
           "candidate_built", "test_result", "memory_added"}          # agent events about a branch: they carry data.node
SERVER_ONLY = {"claim_granted", "claim_released", "claim_expired", "claim_taken_over", "space_opened"}
CLAIM_TTL, PRESENCE_TTL = 90.0, 20.0
ENFORCE_CLAIMS = True      # False = advisory: a claim conflict is accepted and flagged in data.warn; a skipped node still blocks agents
PRIVATE_KEYS = {"obvious", "obvious_match", "private"}      # the repo keeps these out of every shared view

def _strip(x):
    if isinstance(x, dict): return {k: _strip(v) for k, v in x.items() if k not in PRIVATE_KEYS}
    if isinstance(x, list): return [_strip(v) for v in x]
    return x

class Reject(Exception):
    def __init__(self, code, error, **extra):
        self.code, self.body = code, {"error": error, **extra}

class Space:
    def __init__(self, path, space_id="demo"):
        self.space_id = space_id
        self.db = sqlite3.connect(path, isolation_level=None, check_same_thread=False)
        self.db.execute("PRAGMA journal_mode=WAL"); self.db.execute("PRAGMA synchronous=NORMAL")
        self.db.execute("CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT NOT NULL, by TEXT NOT NULL, "
                        "by_kind TEXT NOT NULL, kind TEXT NOT NULL, subject TEXT, label TEXT, base INTEGER, op TEXT, body TEXT NOT NULL, "
                        "UNIQUE(by, op))")
        self.db.execute("CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT)")
        self.db.execute("INSERT OR IGNORE INTO meta VALUES('epoch', ?)", (secrets.token_hex(4),))
        self.epoch = self.db.execute("SELECT v FROM meta WHERE k='epoch'").fetchone()[0]
        self.lock, self.cond = threading.RLock(), threading.Condition()
        self.log, self.ops, self.parent, self.closed, self.names, self.last_edit = [], {}, {}, set(), {}, {}
        self.claims, self.roster, self.roster_ver = {}, {}, 0
        for r in self.db.execute("SELECT seq,ts,by,by_kind,kind,subject,label,base,op,body FROM events ORDER BY seq"):
            ev = dict(zip(("seq", "ts", "by", "by_kind", "kind", "subject", "label", "base", "op"), r[:9]), **json.loads(r[9]))
            self._fold(ev); self.log.append(ev)
            if ev["op"]: self.ops[(ev["by"], ev["op"])] = ev["seq"]
        last = {}
        for e in self.log:                                   # claims do not survive a restart: close those still open in the log
            if e["kind"].startswith("claim_"): last[e["subject"]] = e
        for s, e in last.items():
            if e["kind"] in ("claim_granted", "claim_taken_over"):
                self._write("server", "system", {"kind": "claim_expired", "subject": s, "label": self.names.get(s[5:]),
                                                 "data": {"owner_was": e["data"].get("owner") or e["data"].get("to"), "reason": "restart"}})
        if not self.log:
            self._write("server", "system", {"kind": "space_opened", "data": {"space_id": space_id, "epoch": self.epoch}})

    # ---- log
    def _fold(self, ev):
        d, k = ev.get("data") or {}, ev["kind"]
        if k == "node_added" and d.get("id"): self.parent[d["id"]] = d.get("parent"); self.names[d["id"]] = d.get("name") or d["id"]
        elif k == "node_edited":
            for f in d.get("fields") or {}: self.last_edit[(ev["subject"], f)] = (ev["seq"], ev["by"])
        elif k == "question_chosen": self.last_edit[("slot:next_question", "choose")] = (ev["seq"], ev["by"])
        elif k in ("node_skipped", "question_vetoed"): self.closed.add(ev["subject"])
        elif k in ("node_unskipped", "question_unvetoed"): self.closed.discard(ev["subject"])

    def _write(self, by, by_kind, e):
        with self.lock:
            ts = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + ".%03dZ" % (int(time.time() * 1000) % 1000)
            body = {k: e[k] for k in ("data", "owner", "round", "stage", "claim", "cause") if k in e}
            self.db.execute("BEGIN IMMEDIATE")
            try:
                cur = self.db.execute("INSERT INTO events(ts,by,by_kind,kind,subject,label,base,op,body) VALUES(?,?,?,?,?,?,?,?,?)",
                                      (ts, by, by_kind, e["kind"], e.get("subject"), e.get("label"), e.get("base"), e.get("op"),
                                       json.dumps(body, separators=(",", ":"))))
                seq = cur.lastrowid
                self.db.execute("COMMIT")
            except BaseException:
                self.db.execute("ROLLBACK"); raise
            assert seq == len(self.log) + 1
            ev = dict({"seq": seq, "ts": ts, "by": by, "by_kind": by_kind, "kind": e["kind"], "subject": e.get("subject"),
                       "label": e.get("label"), "base": e.get("base"), "op": e.get("op")}, **body)
            self._fold(ev); self.log.append(ev)
            if e.get("op"): self.ops[(by, e["op"])] = seq
        with self.cond:                      # notify only after the commit
            self.cond.notify_all()
        return ev

    def _owner(self, by):                                  # the person an actor works for
        for r in self.roster.values():
            if r["by"] == by and r.get("owner"): return r["owner"]
        return by.split(".")[0]

    def since(self, n, limit=500):
        with self.lock:
            return self.log[n:n + limit]

    def head(self):
        return len(self.log)

    def post(self, by, by_kind, e):
        if not isinstance(e, dict) or not e.get("kind") or not isinstance(e.get("data", {}), dict):
            raise Reject(422, "bad_envelope")
        if e["kind"] in SERVER_ONLY: raise Reject(422, "unknown_kind", detail="server only")
        with self.lock:
            if e.get("op") and (by, e["op"]) in self.ops:                       # look up first, never ON CONFLICT DO NOTHING
                return {"seq": self.ops[(by, e["op"])], "dup": True}
            e = dict(e, data=_strip(e.get("data") or {}), owner=self._owner(by))      # the server stamps the owner
            d, node = e["data"], e["data"].get("node")
            warn = None
            if by_kind == "agent" and e["kind"] in GUARDED and node:
                try: self._guard(by, node, e)
                except Reject as r:
                    if ENFORCE_CLAIMS or r.body["error"] == "subject_closed": raise
                    warn = r.body["error"]                                       # advisory mode: accept, but flag it
            if e["kind"] == "node_added":                                         # validate BEFORE the write: a commit cannot be undone
                if not d.get("id"): raise Reject(422, "bad_envelope", detail="node_added needs data.id")
                if d["id"] in self.parent: raise Reject(409, "id_taken", id=d["id"])
            over = []
            if e["kind"] in ("node_edited", "question_chosen"):     # last writer wins, but tell the loser whom they overwrote
                slots = [(e.get("subject"), f) for f in d.get("fields") or {}] if e["kind"] == "node_edited" else [("slot:next_question", "choose")]
                for key in slots:
                    le = self.last_edit.get(key)
                    if le and le[1] != by and le[0] > (e.get("base") or 0): over.append({"field": key[1], "seq": le[0], "by": le[1]})
            if over or warn: e = dict(e, data=dict(d, **({"overwrote": over} if over else {}), **({"warn": warn} if warn else {})))
            res = {"seq": self._write(by, by_kind, e)["seq"], "dup": False}
            if over: res["overwrote"] = over
            if warn: res["warn"] = warn
            return res

    # ---- claims (the server is the only authority; the fencing token is the seq of the grant event)
    def _chain(self, node):
        out = []
        while node is not None and node not in out:
            out.append(node); node = self.parent.get(node)
        return out

    def _closed(self, node):
        return any("node:" + n in self.closed for n in self._chain(node))

    def _guard(self, by, node, e):
        now = time.monotonic()
        if self._closed(node): raise Reject(409, "subject_closed", subject="node:" + node)
        for n in self._chain(node):
            c = self.claims.get("node:" + n)
            if c and c["exp"] > now:
                if c["owner"] != by: raise Reject(409, "claimed_by_other", held_by=c["owner"], ttl_left_s=round(c["exp"] - now, 1))
                if e.get("claim") != c["token"]: raise Reject(409, "claim_lost")
                return
        if e.get("claim") is not None: raise Reject(409, "claim_lost")

    def _conflict(self, node, by, now):                    # another live claim on this node, an ancestor, or a descendant
        for s, c in self.claims.items():
            if c["exp"] > now and c["owner"] != by:
                other = s[5:]
                if other in self._chain(node) or node in self._chain(other):
                    return {"held_by": c["owner"], "subject": s, "ttl_left_s": round(c["exp"] - now, 1)}

    def claim(self, by, by_kind, action, subject, token=None, ttl=CLAIM_TTL, purpose=None, cause=None):
        if not isinstance(subject, str) or not subject.startswith("node:"): raise Reject(422, "bad_envelope", detail="subject must be node:<id>")
        with self.lock:
            now, c = time.monotonic(), self.claims.get(subject)
            live = bool(c and c["exp"] > now)
            if action == "acquire":
                if live and c["owner"] == by:
                    c["exp"], c["ttl"] = now + ttl, ttl; return {"token": c["token"], "ttl_s": ttl}
                other = self._conflict(subject[5:], by, now)
                if other: raise Reject(409, "claimed_by_other", **other)
                ev = self._write(by, by_kind, {"kind": "claim_granted", "subject": subject, "label": self.names.get(subject[5:]), "owner": self._owner(by),
                                               **({"cause": cause} if cause else {}), "data": dict({"owner": by, "ttl_s": ttl}, **({"purpose": purpose} if purpose else {}))})
                self.claims[subject] = {"owner": by, "token": ev["seq"], "exp": now + ttl, "ttl": ttl}
                return {"token": ev["seq"], "ttl_s": ttl}
            if action == "takeover":
                if by_kind != "human": raise Reject(403, "humans_only")
                ev = self._write(by, by_kind, {"kind": "claim_taken_over", "subject": subject, "label": self.names.get(subject[5:]), "owner": self._owner(by),
                                               "data": {"from": c["owner"] if live else None, "to": by}})
                self.claims[subject] = {"owner": by, "token": ev["seq"], "exp": now + ttl, "ttl": ttl}
                return {"token": ev["seq"], "ttl_s": ttl}
            if not (live and c["owner"] == by and c["token"] == token): raise Reject(409, "claim_lost")
            if action == "renew":
                c["exp"] = now + c["ttl"]; return {"token": token, "ttl_s": c["ttl"]}
            if action == "release":
                del self.claims[subject]
                self._write(by, by_kind, {"kind": "claim_released", "subject": subject, "label": self.names.get(subject[5:]), "owner": self._owner(by), "data": {"owner": by, "reason": "done"}})
                return {"ok": True}
            raise Reject(422, "bad_envelope", detail="action")

    def reap(self):                                        # run every 5 s from a daemon thread
        with self.lock:
            now = time.monotonic()
            for s, c in list(self.claims.items()):
                if c["exp"] <= now:
                    del self.claims[s]
                    self._write("server", "system", {"kind": "claim_expired", "subject": s, "label": self.names.get(s[5:]), "data": {"owner_was": c["owner"]}})
            gone = [k for k, r in self.roster.items() if now - r["seen"] > PRESENCE_TTL]
            for k in gone: del self.roster[k]
            if gone: self.roster_ver += 1
        if gone:
            with self.cond: self.cond.notify_all()

    # ---- presence (memory only, no seq)
    def roster_list(self):
        now = time.monotonic()
        return [dict({k: v for k, v in r.items() if k != "seen"}, seen_ms_ago=int((now - r["seen"]) * 1000)) for r in self.roster.values()]

    def beat(self, by, by_kind, p):
        with self.lock:
            now, cid = time.monotonic(), p.get("client") or by
            old = self.roster.get(cid, {})
            if p.get("bye"):
                changed = self.roster.pop(cid, None) is not None
            else:
                new = {"client": cid, "by": by, "kind": by_kind, "name": p.get("name") or old.get("name") or by,
                       "owner": p.get("owner") or old.get("owner") or by.split(".")[0], "view": p.get("view", old.get("view")),
                       "focus": p.get("focus", old.get("focus")), "activity": p.get("activity", old.get("activity")),
                       "cursor": p.get("cursor", old.get("cursor")), "seen": now}
                changed = {k: v for k, v in new.items() if k != "seen"} != {k: v for k, v in old.items() if k != "seen"}
                self.roster[cid] = new
            out = {"head": len(self.log), "interrupts": []}
            for c in p.get("claims") or []:                # the caller lists the claims it believes it holds; we renew or object
                cl = self.claims.get(c["subject"])
                if cl and cl["owner"] == by and cl["token"] == c["token"] and cl["exp"] > now:
                    cl["exp"] = now + cl["ttl"]
                    if self._closed(c["subject"][5:]): out["interrupts"].append({"type": "subject_closed", "subject": c["subject"]})
                else:
                    out["interrupts"].append({"type": "claim_lost", "subject": c["subject"]})
            out["claims_ok"] = not any(i["type"] == "claim_lost" for i in out["interrupts"])
            if changed: self.roster_ver += 1
        if changed:
            with self.cond: self.cond.notify_all()
        return out

    def hello(self):
        return {"space_id": self.space_id, "epoch": self.epoch, "head": len(self.log), "server_time_ms": int(time.time() * 1000),
                "claims": self.claims_list(), "roster": self.roster_list()}

    def claims_list(self):
        now = time.monotonic()
        return [{"subject": s, "owner": c["owner"], "token": c["token"], "ttl_left_s": round(c["exp"] - now, 1)}
                for s, c in self.claims.items() if c["exp"] > now]


# ---- digest: what changed since your cursor, as short text for the next prompt
TIER = {"question_vetoed": 0, "question_chosen": 0, "node_skipped": 0, "node_unskipped": 0, "opinion_given": 0, "note_posted": 0,
        "comment_posted": 0, "node_added": 0, "claim_granted": 1, "claim_taken_over": 1, "claim_released": 1, "claim_expired": 1,
        "test_result": 1, "question_picked": 1, "objection_marked": 2, "objection_raised": 2, "reply_posted": 2,
        "cluster_snapshot": 3, "sketch_batch": 3, "memory_added": 3}
FMT = {"node_added": 'added part "{label}"', "node_skipped": 'skipped part "{label}"', "node_unskipped": 'un-skipped part "{label}"',
       "question_vetoed": 'vetoed question "{label}"', "question_chosen": 'chose question "{label}" as next',
       "opinion_given": 'scored "{label}" {score}/10 ({note})', "note_posted": "left a note: {text}",
       "comment_posted": 'commented on "{label}": {text}', "claim_granted": 'is working on part "{label}"{why}; do not touch it',
       "claim_released": 'released part "{label}"', "claim_expired": 'claim of {owner_was} on part "{label}" ended (expired)',
       "claim_taken_over": 'took over part "{label}"', "test_result": 'test of "{label}": {status} {metric}',
       "question_picked": 'team question is now "{label}"', "objection_raised": 'raised a {severity} objection on "{label}"',
       "reply_posted": 'replied ({kind}) on "{label}"', "objection_marked": 'marked an objection on "{label}" {verdict}',
       "cluster_snapshot": 'regrouped part "{label}" into {n} clusters', "sketch_batch": 'added {count} sketches to part "{label}"',
       "memory_added": 'added a memory entry to part "{label}"'}

class D(dict):
    def __missing__(self, k):
        return "?"

def make_digest(events, me, cap=1200):
    rows = [e for e in events if e["by"] != me and e["kind"] in FMT]
    if not rows:
        return "", (events[-1]["seq"] if events else 0)
    merged = {}
    for e in rows:
        k, c = (e["by"], e["kind"], e.get("subject")), (e.get("data") or {}).get("count", 0)
        if k in merged:
            m = merged[k]; m["n"] += 1; m["last"] = e["seq"]; m["count"] += c; m["e"] = e       # show the newest
        else:
            merged[k] = {"e": e, "n": 1, "last": e["seq"], "count": c}
    def render(m):
        e = m["e"]; d = D(e.get("data") or {})
        d["label"] = e.get("label") or e.get("subject") or "?"
        if e["kind"] == "sketch_batch":
            d["count"] = m["count"]
        d["why"] = (": " + d["purpose"]) if d.get("purpose") else ""
        if e["kind"] == "test_result":
            mt = d.get("metrics") or {}
            d["metric"] = ", ".join("%s %s" % (k, round(v, 2)) for k, v in list(mt.items())[:2] if isinstance(v, (int, float))) or d.get("reason", "")
        who = "" if e.get("by_kind") == "system" else ("HUMAN " if e.get("by_kind") == "human" else "") + e["by"]
        extra = " (x%d)" % m["n"] if m["n"] > 1 and e["kind"] != "sketch_batch" else ""
        return "- %s%s%s [e%d]" % (who + " " if who else "", FMT[e["kind"]].format_map(d), extra, m["last"])
    order = sorted(merged.values(), key=lambda m: (TIER.get(m["e"]["kind"], 5), -m["last"]))
    first, last_ = events[0]["seq"], events[-1]["seq"]
    head = "TEAM UPDATE: events e%d to e%d since your last step" % (first, last_)
    chosen, used = [], len(head) + 90
    for m in order:
        line = render(m)
        if used + len(line) + 1 <= cap:
            chosen.append((m["last"], line)); used += len(line) + 1
    left = len(order) - len(chosen)
    foot = ["(+%d more lines left out; GET /api/events?since=%d for all)" % (left, first - 1)] if left else []
    return "\n".join([head] + [l for _, l in sorted(chosen)] + foot), last_


# ---- HTTP
def frame(r):
    return ("id: %d\ndata: %s\n\n" % (r["seq"], json.dumps(r, separators=(",", ":")))).encode()

class Handler(http.server.SimpleHTTPRequestHandler):       # static files come from directory=
    protocol_version = "HTTP/1.0"                          # no keep-alive traps; the stream sends Connection: close
    disable_nagle_algorithm = True
    def log_message(self, *a): pass

    def _send(self, code, obj):
        b = json.dumps(obj, separators=(",", ":")).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(b)))
        self.send_header("Cache-Control", "no-store"); self.end_headers(); self.wfile.write(b)

    def _who(self, q):
        return (self.headers.get("X-Space-Actor") or q.get("me", ["anon"])[0], self.headers.get("X-Space-Kind") or q.get("kind", ["human"])[0])

    def _key(self, q):
        k = self.server.key
        if k and (self.headers.get("X-Space-Key") or q.get("key", [""])[0]) != k: raise Reject(403, "bad_key")

    def do_POST(self):
        u = urllib.parse.urlsplit(self.path); q = urllib.parse.parse_qs(u.query); sp = self.server.space
        try:
            n = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(min(n, 1 << 20))        # read the body FIRST: if a reply goes out with the body unread,
            self._key(q)                                  # Windows resets the connection and the client never sees the 403/413
            if self.headers.get_content_type() != "application/json": raise Reject(415, "bad_content_type")
            if n > 65536: raise Reject(413, "too_big")
            d, (by, kind) = json.loads(raw or b"{}"), self._who(q)
            if u.path == "/api/events":
                if "events" in d:
                    res = []
                    with sp.lock:
                        for e in d["events"][:100]:
                            try: res.append(sp.post(by, kind, e))
                            except Reject as r: res.append(r.body)
                    return self._send(200, {"results": res})
                return self._send(200, sp.post(by, kind, d))
            if u.path == "/api/claims":
                return self._send(200, sp.claim(by, kind, d.get("action", "acquire"), d["subject"], d.get("token"), d.get("ttl_s", CLAIM_TTL), d.get("purpose"), d.get("cause")))
            if u.path == "/api/presence":
                return self._send(200, sp.beat(by, kind, d))
            raise Reject(404, "no_route")
        except Reject as r:
            self._send(r.code, r.body)
        except (KeyError, ValueError):
            self._send(422, {"error": "bad_envelope"})

    def do_GET(self):
        u = urllib.parse.urlsplit(self.path); q = urllib.parse.parse_qs(u.query); sp = self.server.space
        if not u.path.startswith("/api/"):
            return super().do_GET()
        try:
            self._key(q)
            if u.path == "/api/events":                    # first load, catch-up, long-poll, agents
                since, wait = int(q.get("since", ["0"])[0]), min(25.0, float(q.get("wait", ["0"])[0]))
                lim, end = min(2000, int(q.get("limit", ["500"])[0])), time.monotonic() + wait
                while True:
                    rows = sp.since(since, lim)
                    if rows or time.monotonic() >= end: break
                    with sp.cond:
                        if sp.head() <= since: sp.cond.wait(timeout=max(0.0, min(1.0, end - time.monotonic())))
                return self._send(200, {"epoch": sp.epoch, "head": sp.head(), "events": rows})
            if u.path == "/api/stream":
                return self._stream(q)
            if u.path == "/api/digest":
                since = int(q.get("since", ["0"])[0])
                if since == 0: since = max(0, sp.head() - 60)       # a new agent sees the last 60 events
                rows = sp.since(since, 1000)
                text, to = make_digest(rows, q["agent"][0], int(q.get("cap", ["1200"])[0])) if rows else ("", since)
                return self._send(200, {"text": text, "from_seq": since + 1, "to_seq": to, "n": len(rows)})
            raise Reject(404, "no_route")
        except Reject as r:
            self._send(r.code, r.body)
        except (KeyError, ValueError):
            self._send(422, {"error": "bad_envelope"})

    def _stream(self, q):
        sp, last = self.server.space, int(self.headers.get("Last-Event-ID") or q.get("since", ["0"])[0] or 0)   # header wins
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-cache"); self.send_header("Connection", "close")
        self.end_headers()
        w, rv = self.wfile.write, -1
        try:
            w(b"retry: 1000\n\n")
            if last > sp.head():
                w(b'event: reset\ndata: {"reason":"since_ahead_of_head"}\n\n'); return
            w(("event: hello\ndata: %s\n\n" % json.dumps(sp.hello(), separators=(",", ":"))).encode())
            while True:
                rows = sp.since(last)
                if rows:
                    w(b"".join(frame(r) for r in rows)); last = rows[-1]["seq"]; continue      # one write per batch
                if sp.roster_ver != rv:
                    rv = sp.roster_ver
                    w(("event: presence\ndata: %s\n\n" % json.dumps({"clients": sp.roster_list(), "claims": sp.claims_list()}, separators=(",", ":"))).encode()); continue
                with sp.cond:
                    quiet = sp.head() <= last and sp.roster_ver == rv       # check again under the lock, then wait
                    if quiet: sp.cond.wait(timeout=10.0)
                    quiet = quiet and sp.head() <= last and sp.roster_ver == rv
                if quiet:
                    w(("event: ping\ndata: %s\n\n" % json.dumps({"head": sp.head(), "claims": sp.claims_list()}, separators=(",", ":"))).encode())
        except OSError:
            pass                  # client went away: ConnectionResetError, ConnectionAbortedError (Windows), BrokenPipeError

class SpaceServer(http.server.ThreadingHTTPServer):
    request_queue_size = 64
    allow_reuse_address = False   # on Windows the default (1) lets a second server share the port
    def __init__(self, addr, space, web_dir=".", key=""):
        import functools
        self.space, self.key = space, key
        super().__init__(addr, functools.partial(Handler, directory=web_dir))
    def handle_error(self, request, client_address):
        import sys, traceback
        if not isinstance(sys.exc_info()[1], OSError): traceback.print_exc()

def _reaper(sp):
    while True:
        time.sleep(5.0)
        try: sp.reap()
        except Exception: pass

def serve(db_path, port=8766, host="127.0.0.1", web_dir="web", key=""):
    import os
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    sp = Space(db_path)
    threading.Thread(target=_reaper, args=(sp,), daemon=True).start()
    srv = SpaceServer((host, port), sp, web_dir, key)
    print("space on http://%s:%d/  epoch %s" % (host, port, sp.epoch), flush=True)
    srv.serve_forever(poll_interval=0.25)

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", default="space.db"); ap.add_argument("--port", type=int, default=8766)
    ap.add_argument("--web", default="web"); ap.add_argument("--lan", action="store_true")
    a = ap.parse_args()
    key = secrets.token_urlsafe(6) if a.lan else ""
    if key: print("key:", key, flush=True)
    serve(a.db, a.port, "0.0.0.0" if a.lan else "127.0.0.1", a.web, key)
```

### A.2 The digest function

It is inside A.1: `TIER`, `FMT` and `make_digest`. Add a sentence per event kind in `FMT` and the tier in `TIER` to teach it a new kind.

### A.3 `web/space_connect.mjs`: the live connection in the browser

Tested in Node against a spec-based `EventSource`: reset, 503, silence and a swapped database (section 7). In a page use `import { connectSpace } from './space_connect.mjs'`. Open it with `since: 0` and the stream replays the whole log in order. Paint once `last` reaches the `head` from `hello`.

```js
// Browser-side live connection to the space. Plain JS, no libraries.
export function connectSpace({ base, key = '', since = 0, silentMs = 25000, onEvent, onStatus, onReset }) {
  let es = null, last = since, timer = null, wd = null, tries = 0, stopped = false, catching = false, epoch = null;
  const q = () => `since=${last}` + (key ? `&key=${key}` : '');
  const arm = () => { clearTimeout(wd); wd = setTimeout(() => restart('silent'), silentMs); };

  function restart(why) {                       // used when the browser gave up, or the line went silent
    if (stopped) return;
    if (es) es.close();
    clearTimeout(timer);
    const wait = Math.min(5000, 500 * 2 ** tries++) * (0.7 + Math.random() * 0.6);   // backoff + jitter
    onStatus('reconnecting', why);
    timer = setTimeout(open, wait);
  }

  async function catchUp() {                    // fetch what we missed, in order, then go on
    if (catching || stopped) return;
    catching = true;
    try {
      for (;;) {
        const d = await (await fetch(`${base}/api/events?${q()}&limit=500`)).json();
        if (stopped) break;
        for (const ev of d.events) if (ev.seq === last + 1) { last = ev.seq; onEvent(ev); }
        if (!d.events.length || last >= d.head) break;
      }
    } catch (e) { /* the stream or the watchdog will try again */ } finally { catching = false; }
  }

  function reset() {                            // the app must drop its state and call connectSpace again with since: 0
    stopped = true; if (es) es.close(); clearTimeout(timer); clearTimeout(wd); onReset && onReset();
  }

  function open() {
    es = new EventSource(`${base}/api/stream?${q()}`);
    es.onopen = () => { tries = 0; onStatus('live'); arm(); };
    es.onmessage = (e) => {                     // one durable event, id = seq
      if (stopped) return;                      // after reset() or close(), late events in the same chunk must not get in
      arm();
      const ev = JSON.parse(e.data);
      if (ev.seq <= last) return;               // duplicate: ignore
      if (ev.seq > last + 1) return catchUp();  // gap: fill it first
      last = ev.seq; onEvent(ev);
    };
    es.addEventListener('ping', (e) => { if (stopped) return; arm(); if (JSON.parse(e.data).head > last) catchUp(); });
    es.addEventListener('hello', (e) => {        // a different epoch means a different database: never splice two histories
      const h = JSON.parse(e.data);
      if (epoch && h.epoch !== epoch) return reset();
      epoch = h.epoch; arm(); onStatus('hello', h);
    });
    es.addEventListener('presence', (e) => { if (stopped) return; arm(); onStatus('presence', JSON.parse(e.data)); });
    es.addEventListener('reset', reset);
    es.onerror = () => { if (es.readyState === 2) restart('closed_by_browser'); };   // 0 = browser retries itself
  }

  open();
  return { close() { stopped = true; if (es) es.close(); clearTimeout(timer); clearTimeout(wd); }, last: () => last };
}
```

### A.4 `web/store.mjs`: server truth plus my pending edits

`makeStore(reduce, init)` takes a pure `reduce(state, event)`. Call `addPending(op, ev)` when the person acts, `queued(op, seq)` when the POST returns, `applyServer(ev)` for every event from `connectSpace`, and `reject(op)` on a 409. `status(op)` gives pending, queued or applied.

```js
// Client store: server truth + a thin layer of your own un-confirmed edits on top.
export function makeStore(reduce, init) {
  let server = init(), view = server, last = 0;
  const mine = new Map();                    // op -> { ev, state: 'pending' | 'queued' | 'applied', seq }
  const bySeq = new Map();                   // seq -> op, for control_applied
  const rebuild = () => { view = server; for (const m of mine.values()) if (m.state !== 'applied') view = reduce(view, m.ev); };
  return {
    view: () => view, last: () => last, status: (op) => mine.get(op)?.state,
    addPending(op, ev) { mine.set(op, { ev: { ...ev, op }, state: 'pending' }); rebuild(); },
    queued(op, seq) { const m = mine.get(op); if (m) { m.state = 'queued'; m.seq = seq; bySeq.set(seq, op); } },
    reject(op) { mine.delete(op); rebuild(); },                       // 409: roll back
    applyServer(ev) {                                                  // events arrive in seq order
      if (ev.seq <= last) return false;
      last = ev.seq; server = reduce(server, ev);
      const m = ev.op && mine.get(ev.op);
      if (m) { m.state = 'queued'; m.seq = ev.seq; bySeq.set(ev.seq, ev.op); }   // our own echo
      if (ev.kind === 'control_applied') for (const s of ev.data.refs || []) {
        const o = bySeq.get(s); if (o) mine.get(o).state = 'applied';
      }
      rebuild(); return true;
    },
  };
}
```

### A.5 `space_client.py`: the agent side

Order of calls at a loop boundary (a sketch, not run inside the loop):

```python
client = SpaceClient("maya.agent", run_dir)       # once, at start
client.start_heartbeat(activity=lambda: {"stage": stage_name})
token = client.claim("node:optimizer", purpose="pre-mortem on the optimizer ideas")   # None if someone else holds it
# at each _stage boundary:
client.flush_outbox()
text = client.digest()                            # "" when there is nothing new
if text: peer_digest = text                       # goes into the next prompts, not into blind stages
client.commit_cursor(round=r, stage=name)         # only after the text is stored for the prompt; writes the receipt
# after a stage:
client.emit("sketch_batch", "node:optimizer", "optimizer", {"node": "optimizer", "count": 12, "items": [...]},
            claim_subject="node:optimizer")
```

The class itself (tested, section 7):

```python
"""Agent-side client for the shared space. Standard library only. It must never block the research loop."""
import json, os, threading, time, urllib.error, urllib.request

class SpaceClient:
    def __init__(self, actor, run_dir, base="http://127.0.0.1:8766", kind="agent", timeout=3.0, key=""):
        # 127.0.0.1, never "localhost": on Windows "localhost" cost 2 s per connect from Python (measured).
        self.base, self.actor, self.kind, self.timeout, self.key = base.rstrip("/"), actor, kind, timeout, key
        self.outbox = os.path.join(run_dir, "space_outbox.ndjson")
        self.state_path = os.path.join(run_dir, "space_cursor.json")
        try: self.cursor = int(json.load(open(self.state_path))["cursor"])      # survives a restart of the agent process
        except (OSError, ValueError, KeyError): self.cursor = 0
        self._next, self._last = self.cursor, {}
        self.t0, self.n = int(time.time() * 1000), 0          # op = actor-startms-counter: unique across restarts
        self.claims, self.interrupts, self.beats = {}, [], 0   # claims: subject -> fencing token
        self._stop = threading.Event()

    def _call(self, method, path, body=None):
        h = {"Content-Type": "application/json", "X-Space-Actor": self.actor, "X-Space-Kind": self.kind}
        if self.key: h["X-Space-Key"] = self.key
        req = urllib.request.Request(self.base + path, method=method, data=None if body is None else json.dumps(body).encode(), headers=h)
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return r.status, json.loads(r.read() or b"{}")
        except urllib.error.HTTPError as e:                    # 409 and 422 come back as data, not as exceptions
            return e.code, json.loads(e.read() or b"{}")

    # ---- events
    def emit(self, kind, subject=None, label=None, data=None, claim_subject=None, **extra):
        self.n += 1
        ev = {"op": "%s-%d-%d" % (self.actor, self.t0, self.n), "kind": kind, "subject": subject, "label": label,
              "data": data or {}, "base": self.cursor, **extra}
        if claim_subject in self.claims: ev["claim"] = self.claims[claim_subject]
        return self._send(ev)

    def _send(self, ev):
        try:
            st, d = self._call("POST", "/api/events", ev)
        except (OSError, ValueError):                          # server down or slow: keep the event and go on
            with open(self.outbox, "a", encoding="utf-8") as f: f.write(json.dumps(ev) + "\n")
            return None
        return d if st == 200 else dict(d, status=st)

    def flush_outbox(self):                                    # safe to call twice: the server dedupes on (actor, op)
        try: lines = open(self.outbox, encoding="utf-8").read().splitlines()
        except OSError: return 0
        left = []
        for ln in lines:
            try:
                st, _ = self._call("POST", "/api/events", json.loads(ln))
                if st >= 500: left.append(ln)
            except (OSError, ValueError):
                left.append(ln)
        with open(self.outbox, "w", encoding="utf-8") as f: f.write("".join(x + "\n" for x in left))
        return len(lines) - len(left)

    # ---- digest: read first, move the cursor only after the text is in the prompt
    def digest(self, cap=1200):
        try: st, d = self._call("GET", "/api/digest?agent=%s&since=%d&cap=%d" % (self.actor, self.cursor, cap))
        except (OSError, ValueError): return ""
        if st != 200: return ""
        self._next = d.get("to_seq", self.cursor)
        self._last = {"from_seq": d.get("from_seq"), "to_seq": d.get("to_seq"), "n": d.get("n", 0), "chars": len(d.get("text", ""))} if d.get("text") else {}
        return d.get("text", "")

    def commit_cursor(self, round=None, stage=None):
        self.cursor = max(self.cursor, self._next)
        if self._last:                                         # a receipt in the log: what this agent was told, and when
            self.emit("digest_taken", None, None, self._last, round=round, stage=stage)
            self._last = {}
        try:
            with open(self.state_path + ".tmp", "w") as f: json.dump({"cursor": self.cursor}, f)
            os.replace(self.state_path + ".tmp", self.state_path)
        except OSError:
            pass                                               # a lost cursor only means the same digest again

    # ---- claims and heartbeat
    def claim(self, subject, ttl_s=90, purpose=None, cause=None):
        try: st, d = self._call("POST", "/api/claims", {"action": "acquire", "subject": subject, "ttl_s": ttl_s, "purpose": purpose, "cause": cause})
        except (OSError, ValueError): return None
        if st == 200: self.claims[subject] = d["token"]; return d["token"]
        return None                                            # 409: d["held_by"] says who has it

    def release(self, subject):
        tok = self.claims.pop(subject, None)
        try: return self._call("POST", "/api/claims", {"action": "release", "subject": subject, "token": tok})[0] == 200
        except (OSError, ValueError): return False

    def start_heartbeat(self, every=5.0, activity=lambda: {}):
        def beat():
            while not self._stop.wait(every):
                body = {"cursor": self.cursor, "activity": activity(), "claims": [{"subject": s, "token": t} for s, t in self.claims.items()]}
                try:
                    st, d = self._call("POST", "/api/presence", body)
                except (OSError, ValueError):
                    continue
                self.beats += 1
                for i in d.get("interrupts", []) if st == 200 else []:
                    self.interrupts.append(i)
                    if i["type"] == "claim_lost": self.claims.pop(i["subject"], None)
        threading.Thread(target=beat, daemon=True).start()

    def stop(self):
        self._stop.set()
```
