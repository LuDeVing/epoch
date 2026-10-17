"""The person-agent: one delegate process per person (docs/MULTIPLAYER_DESIGN.md section 9).

    python -m space.agent --me ana --space http://127.0.0.1:8766 --model sonnet|haiku|mock --fallback mock|none
                          --space-id <name> [--state-dir DIR] [--exit-after S] [--key K]

It long-polls GET /api/events with a saved cursor and acts as `<me>.agent` (X-Space-Kind: agent, owner <me>):

- a chat_posted to `<me>.agent` from <me> gets an agent_said ack within 2 s with no model. A slash command
  (contract.SLASH) is parsed by regex and its events are posted at once, with cause = the chat seq. It is the
  person's own typed command, so it needs no OK. Free text goes to the model (one call in flight per process):
  the prompt is space/prompts/person_agent.txt with <space> from GET /api/snapshot, <recent_events> from
  GET /api/digest (role person) plus the person's last three actions, and <message>.
- the model's actions go through the policy of section 6.7: auto actions become events at once; confirm actions,
  guesses and takeovers become an intent card (intent_proposed) and wait for the person's intent_decided.
  An unknown id drops the action and says which. At most 3 actions. Never a result or a status.
- timing: "waiting for the model" at 8 s; with --fallback mock the canned reply at 20 s, marked (canned), and a
  real reply after that is posted as kind late with no actions; with --fallback none an error line at 60 s.
- a change by another person or their agent gets one templated peer line, coalesced per 2 s.
- every stage_entered: GET /api/digest, one agent_said digest line, one digest_taken receipt, cursor committed.

State file: <state-dir>/<me>.json (default D:/AGI-lab/spaces/<space-id>/agents/<me>.json): cursors, epoch, the last
three actions, the open intent card, held claims. A failed POST goes to <me>.outbox.ndjson and is replayed later
(the server dedupes on op). Standard library plus harness.llm for the one model call.
"""
from __future__ import annotations

import argparse
import difflib
import json
import os
import queue
import re
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from . import actions as A
from . import contract as C

HERE = Path(__file__).resolve().parent
PROMPT_PATH = HERE / "prompts" / "person_agent.txt"
MOCK_REPLIES_PATH = HERE / "golden" / "mock_replies.json"
TIMINGS = {"waiting_s": 8.0, "canned_s": 20.0, "error_s": 60.0, "peer_window_s": 2.0, "tick_s": 0.1,
           "heartbeat_s": C.HEARTBEAT_S, "poll_wait_s": 25, "http_timeout_s": 3.0}
LLM_ARGS = {"role": "plain", "effort": "medium", "max_tokens": 1500, "timeout": 60}
ACK_FREE = "Got it. Reading the space."
ACK_BUSY = "Got it. I will read it after your last message."
WAITING = "waiting for the model"
NO_MODEL = "I could not reach the model"
NOTHING_CHANGED = "Nothing changed since your last message."
RETRY_NOTE = ("\n\nTHE LAST REPLY FAILED THESE CHECKS\n{errors}\n"
              "Write the one JSON object again with every field filled.")
SLOT_TEXT = {"space": "{space view, rendered by the service}",
             "recent": "{highlight block, or the single line: Nothing changed since your last message.}",
             "from": '<message from="{name}">', "message": "{the person's message}"}
PEER_KINDS = frozenset({"node_added", "node_edited", "node_skipped", "node_unskipped", "note_posted", "seed_added",
                        "question_vetoed", "question_unvetoed", "question_chosen", "vote_cast", "reply_posted",
                        "fact_disputed", "run_paused", "run_resumed", "opinion_given"})


# ---------------------------------------------------------------- the prompt
def load_prompt(path=PROMPT_PATH):
    """The prompt file with its action list re-rendered from actions.ACTIONS (the file holds the same list,
    so the note's text stays verbatim and the table stays the one source)."""
    text = Path(path).read_text(encoding="utf-8")
    head, rest = text.split("ACTIONS (these are the only ones)\n", 1)
    _, tail = rest.split("\nEvery action also has", 1)
    return head + "ACTIONS (these are the only ones)\n" + A.prompt_lines() + "\nEvery action also has" + tail


def build_prompt(template, space_text, recent, name, message):
    """Fill the four slots in one pass, so text put into one slot is never read as another slot."""
    values = {SLOT_TEXT["space"]: space_text, SLOT_TEXT["recent"]: recent or NOTHING_CHANGED,
              SLOT_TEXT["from"]: f'<message from="{A.clean_text(name, 40)}">',
              SLOT_TEXT["message"]: A.clean_text(message, C.CHAT_CAP)}
    rx = re.compile("|".join(re.escape(k) for k in values))
    return rx.sub(lambda m: values[m.group(0)], template)


def message_of(prompt):
    """The person's message: the text of the last <message> block (the examples come before it)."""
    hits = re.findall(r'<message from="[^"]*">\n?(.*?)\n?</message>', prompt or "", re.S)
    return hits[-1].strip() if hits else ""


# ---------------------------------------------------------------- the mock model (and the canned path)
class MockModel:
    """Canned JSON chosen by message pattern from space/golden/mock_replies.json. It serves --model mock through
    llm.set_mock and --fallback mock directly. The closest example wins when no pattern matches."""

    def __init__(self, path=MOCK_REPLIES_PATH, delay_s=0.0):
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        self.rows = [dict(r, rx=re.compile(r["pattern"], re.I)) for r in data["patterns"]]
        self.default = data["default"]
        self.delay_s = delay_s
        self.calls = 0

    def match(self, message):
        """(row id or None, reply dict)."""
        msg = (message or "").strip()
        for r in self.rows:
            if r["rx"].search(msg):
                return r["id"], r["reply"]
        best, score = None, 0.0
        for r in self.rows:
            s = difflib.SequenceMatcher(None, msg.lower(), r["example"].lower()).ratio()
            if s > score:
                best, score = r, s
        if best is not None and score >= 0.6:
            return best["id"], best["reply"]
        return None, self.default

    def __call__(self, prompt, role, meta):
        self.calls += 1
        if self.delay_s:
            time.sleep(self.delay_s)
        return json.dumps(self.match(message_of(prompt))[1])


# ---------------------------------------------------------------- HTTP to the space server
class Http:
    def __init__(self, base, actor, kind="agent", timeout=3.0, key=""):
        self.base, self.actor, self.kind, self.timeout, self.key = base.rstrip("/"), actor, kind, timeout, key

    def call(self, method, path, body=None, timeout=None):
        """(status, json). 4xx answers come back as data; a dead server raises OSError."""
        h = {"Content-Type": "application/json", "X-Space-Actor": self.actor, "X-Space-Kind": self.kind}
        if self.key:
            h["X-Space-Key"] = self.key
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = urllib.request.Request(self.base + path, method=method, data=data, headers=h)
        try:
            with urllib.request.urlopen(req, timeout=timeout or self.timeout) as r:
                raw = r.read()
                return r.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, (json.loads(raw) if raw else {})
            except ValueError:
                return e.code, {"error": raw[:200].decode("utf-8", "replace")}


# ---------------------------------------------------------------- one free-text message
class Job:
    def __init__(self, chat_seq, text, t0):
        self.chat_seq, self.text, self.t0 = chat_seq, text, t0
        self.lock = threading.Lock()
        self.waited = self.canned = self.errored = self.done = self.started = False


# ---------------------------------------------------------------- the agent
class Agent:
    def __init__(self, me, base=C.BASE_URL, model="mock", fallback="mock", state_dir=None, space_id="stage",
                 timings=None, install_mock=True, key="", clock=time.perf_counter, log=None):
        self.me, self.actor = me, f"{me}.agent"
        self.model, self.fallback = model, fallback
        self.backend = "mock" if model == "mock" else None
        self.llm_model = "sonnet" if model == "mock" else model
        self.timings = dict(TIMINGS, **(timings or {}))
        self.http = Http(base, self.actor, "agent", self.timings["http_timeout_s"], key)
        lab = Path(os.environ.get("HTSA_LAB_ROOT", r"D:\AGI-lab"))
        self.state_dir = Path(state_dir) if state_dir else lab / "spaces" / space_id / "agents"
        self.state_path = self.state_dir / f"{me}.json"
        self.outbox_path = self.state_dir / f"{me}.outbox.ndjson"
        self.clock = clock
        self.log = log or (lambda msg: print(f"[agent {self.actor}] {msg}", file=sys.stderr, flush=True))
        self.template = load_prompt()
        self.canned = MockModel()
        if model == "mock" and install_mock:
            from harness import llm
            llm.set_mock(MockModel())
        self.lock = threading.RLock()
        self.stop_event = threading.Event()
        self.jobs: queue.Queue = queue.Queue()
        self.job = None                       # the free-text message being answered
        self.peer_buf, self.last_peer = [], -1e9
        self.t0ms, self.n = int(time.time() * 1000), 0
        self.threads = []
        self.run = {}
        self.last_snap = {}
        self.need_head = False                # True until a fresh agent has seen the server's head once
        self.save_lock = threading.Lock()
        self.state = {"cursor": None, "digest_cursor": 0, "epoch": None, "actions": [], "open_intent": None,
                      "intent_queue": [], "claims": {}, "my_choice": None, "last_chat_seq": 0}
        self._load_state()

    # ---- state file
    def _load_state(self):
        try:
            st = json.loads(self.state_path.read_text(encoding="utf-8"))
            if isinstance(st, dict):
                self.state.update({k: st[k] for k in self.state if k in st})
        except (OSError, ValueError):
            pass

    def save_state(self):
        with self.save_lock:              # threads share one tmp file: one writer at a time
            self._save_state()

    def _save_state(self):
        with self.lock:
            body = json.dumps(self.state, indent=1)
        try:
            self.state_dir.mkdir(parents=True, exist_ok=True)
            tmp = self.state_path.with_suffix(".json.tmp")
            tmp.write_text(body, encoding="utf-8")
            for _ in range(60):                     # a reader may hold the file open on Windows
                try:
                    os.replace(tmp, self.state_path)
                    return
                except PermissionError:
                    time.sleep(0.05)
        except OSError as e:
            self.log(f"state not saved: {e}")

    # ---- posting
    def _op(self):
        with self.lock:
            self.n += 1
            return f"{self.actor}-{self.t0ms}-{self.n}"

    def post(self, kind, data, subject=None, label=None, cause=None, **extra):
        """POST one event as <me>.agent. Returns the answer dict with "status", or None when it went to the outbox."""
        if kind not in A.OUT_KINDS:
            raise ValueError(f"a person-agent never posts {kind}")
        body = {"op": self._op(), "kind": kind, "subject": subject, "label": label, "data": data,
                "base": self.state.get("cursor"), "cause": cause}
        body.update({k: v for k, v in extra.items() if v is not None})
        try:
            st, d = self.http.call("POST", "/api/events", body)
        except (OSError, ValueError):
            self._to_outbox(body)
            return None
        return dict(d, status=st)

    def say(self, kind, text, cause=None, **data):
        return self.post("agent_said", dict({"kind": kind, "text": text}, **data), subject=f"agent:{self.actor}",
                         cause=cause)

    def _to_outbox(self, body):
        try:
            self.state_dir.mkdir(parents=True, exist_ok=True)
            with open(self.outbox_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(body) + "\n")
        except OSError:
            pass

    def flush_outbox(self):
        try:
            lines = self.outbox_path.read_text(encoding="utf-8").splitlines()
        except OSError:
            return 0
        left = []
        for ln in lines:
            try:
                st, _ = self.http.call("POST", "/api/events", json.loads(ln))
                if st >= 500:
                    left.append(ln)
            except (OSError, ValueError):
                left.append(ln)
        try:
            self.outbox_path.write_text("".join(x + "\n" for x in left), encoding="utf-8")
        except OSError:
            pass
        return len(lines) - len(left)

    # ---- reading the space
    def snapshot(self, timeout=None):
        try:
            st, d = self.http.call("GET", f"/api/snapshot?me={urllib.parse.quote(self.me)}", timeout=timeout)
            if st == 200 and isinstance(d, dict):
                with self.lock:
                    self.last_snap = d
                    if d.get("run"):
                        self.run = dict(d["run"])
                return d
        except (OSError, ValueError):
            pass
        return self.last_snap

    def view(self, timeout=None):
        return A.SpaceView(self.snapshot(timeout), self.me)

    def digest(self, since, timeout=None):
        q = urllib.parse.urlencode({"agent": self.actor, "role": "person", "since": since, "cap": C.DIGEST_CAP})
        st, d = self.http.call("GET", f"/api/digest?{q}", timeout=timeout)
        if st != 200 or not isinstance(d, dict):
            raise OSError(f"digest answered {st}")
        return d

    # ---- the loop
    def start(self):
        self._bootstrap()
        for name, fn in (("poll", self._poll_loop), ("worker", self._work_loop), ("tick", self._tick_loop),
                         ("beat", self._beat_loop)):
            t = threading.Thread(target=fn, name=f"{self.actor}-{name}", daemon=True)
            t.start()
            self.threads.append(t)
        return self

    def stop(self, timeout=5.0):
        self.stop_event.set()
        self.jobs.put(None)
        try:
            self.http.call("POST", "/api/presence", self._presence(bye=True), timeout=1.0)
        except (OSError, ValueError):
            pass
        for t in self.threads:
            t.join(timeout)
        self.save_state()

    def alive(self):
        return all(t.is_alive() for t in self.threads) and not self.stop_event.is_set()

    def _bootstrap(self):
        """A fresh agent starts at the head (it never answers old chats); a known epoch resumes at its cursor."""
        snap = self.snapshot(timeout=self.timings["http_timeout_s"])
        if self.state.get("cursor") is not None and self.state.get("epoch") in (None, snap.get("epoch")):
            return
        head = snap.get("head")
        if head is None:
            try:
                st, d = self.http.call("GET", "/api/events?since=0&limit=1&wait=0")
                head = d.get("head") if st == 200 else None
            except (OSError, ValueError):
                head = None
        if head is None:                  # server not up yet: keep the saved cursor; else the first poll sets the head
            self.need_head = self.state.get("cursor") is None
            return
        with self.lock:
            self.state.update(cursor=int(head or 0), epoch=snap.get("epoch"), digest_cursor=0)
        self.save_state()

    def _poll_loop(self):
        wait = int(self.timings["poll_wait_s"])
        while not self.stop_event.is_set():
            since = int(self.state.get("cursor") or 0)
            try:
                st, d = self.http.call("GET", f"/api/events?since={since}&limit=500&wait={wait}", timeout=wait + 5)
            except (OSError, ValueError):
                self.stop_event.wait(1.0)
                continue
            if st != 200 or not isinstance(d, dict):
                self.stop_event.wait(1.0)
                continue
            epoch, head = d.get("epoch"), int(d.get("head") or 0)
            if self.need_head:
                self.need_head = False
                with self.lock:
                    self.state.update(cursor=head, epoch=epoch, digest_cursor=0)
                self.save_state()
                continue
            if (self.state.get("epoch") and epoch and epoch != self.state["epoch"]) or head < since:
                self.log(f"new epoch or head behind the cursor ({head} < {since}): starting again at the head")
                with self.lock:
                    self.state.update(cursor=head, epoch=epoch, digest_cursor=0)
                self.save_state()
                continue
            with self.lock:
                self.state["epoch"] = epoch or self.state.get("epoch")
            for ev in d.get("events") or []:
                try:
                    self.handle(ev)
                except Exception as e:  # noqa: BLE001 - one bad event never stops the agent
                    self.log(f"event {ev.get('seq')} failed: {type(e).__name__}: {e}")
                with self.lock:
                    self.state["cursor"] = max(int(self.state.get("cursor") or 0), int(ev.get("seq") or 0))
            self.save_state()
            if self.outbox_path.exists():
                self.flush_outbox()

    def _tick_loop(self):
        while not self.stop_event.wait(self.timings["tick_s"]):
            try:
                self._tick_job()
                self._tick_peer()
            except Exception as e:  # noqa: BLE001
                self.log(f"tick failed: {type(e).__name__}: {e}")

    def _presence(self, bye=False):
        with self.lock:
            busy = self.job is not None and not self.job.done
            state = "thinking" if busy else ("waiting" if self.state.get("open_intent") else "finished")
            claims = [{"subject": s, "token": t} for s, t in self.state["claims"].items()]
        return {"client": f"{self.actor}-{self.t0ms}", "name": f"{A.display(self.me)}'s agent", "owner": self.me,
                "view": "agent", "focus": None, "activity": {"state": state, "text": WAITING if busy else "",
                                                            "stage": self.run.get("stage")},
                "cursor": self.state.get("cursor"), "claims": claims, "bye": bye}

    def _beat_loop(self):
        while not self.stop_event.wait(self.timings["heartbeat_s"]):
            try:
                st, d = self.http.call("POST", "/api/presence", self._presence())
            except (OSError, ValueError):
                continue
            for i in (d.get("interrupts") or []) if st == 200 else []:
                if i.get("type") == "claim_lost":
                    with self.lock:
                        self.state["claims"].pop(i.get("subject"), None)
                    self.say("reply", f"I lost the claim on {str(i.get('subject', ''))[5:]}.")

    # ---- events
    def handle(self, ev):
        kind, data = ev.get("kind"), ev.get("data") or {}
        by, owner, by_kind = ev.get("by", ""), ev.get("owner", ""), ev.get("by_kind", "")
        cls = C.actor_class(by, by_kind, owner)
        if kind == "stage_entered":
            with self.lock:
                self.run.update(round=data.get("round"), stage=data.get("stage"), waiting=bool(data.get("waiting")))
            self.on_stage(ev)
        elif kind == "chat_posted" and data.get("to") == self.actor:
            if by == self.me and cls == "person":
                self.on_chat(ev)
            else:
                self.log(f"chat from {by} ignored: this agent acts for {self.me} only")
        elif kind == "intent_decided" and by == self.me and cls == "person":
            self.on_decided(ev)
        elif kind == "question_chosen" and owner == self.me:
            with self.lock:
                self.state["my_choice"] = {"seq": ev.get("seq"), "question": data.get("question")}
        elif kind in ("claim_expired", "claim_taken_over", "claim_released"):
            self._on_claim_event(ev)
        if kind in PEER_KINDS and owner and owner != self.me and cls in ("person", "delegate"):
            with self.lock:
                self.peer_buf.append(ev)

    def _on_claim_event(self, ev):
        subj, data = ev.get("subject"), ev.get("data") or {}
        with self.lock:
            mine = subj in self.state["claims"]
        if not mine:
            return
        lost = (ev["kind"] == "claim_expired" and data.get("owner_was") in (self.actor, self.me)) or \
               (ev["kind"] == "claim_taken_over" and data.get("from") in (self.actor, self.me))
        if lost:
            with self.lock:
                self.state["claims"].pop(subj, None)
            why = data.get("reason") or (f"taken over by {data.get('to')}" if ev["kind"] == "claim_taken_over" else "expired")
            self.say("reply", f"My claim on {subj[5:]} ended ({why}).", cause=ev.get("seq"))

    # ---- chat
    def on_chat(self, ev):
        seq, text = ev.get("seq"), str((ev.get("data") or {}).get("text") or "")
        if A.is_slash(text):
            view = self.view(timeout=1.5)
            try:
                ops, ack = A.parse_slash(text, view)
            except A.Dropped as e:
                self.say("ack", f"Not done: {e}", cause=seq)
                return
            self.say("ack", ack, cause=seq)
            self.run_ops(ops, seq, view, source=text)
            return
        with self.lock:
            busy = self.job is not None or not self.jobs.empty()
        self.say("ack", ACK_BUSY if busy else ACK_FREE, cause=seq)
        self.jobs.put(Job(seq, text, self.clock()))

    def recent_events(self, since, snap):
        """The digest since the person's last message plus their last three actions, or the single line."""
        try:
            text = self.digest(since).get("text") or ""
        except (OSError, ValueError):
            text = ""
        acts = list(((snap.get("mine") or {}).get("actions")) or []) or list(self.state.get("actions") or [])
        lines = [f"- {a.get('kind')} \"{A.clean_text(a.get('text'), 80)}\": {A.clean_text(a.get('status'), 60)}"
                 for a in acts[-3:] if isinstance(a, dict)]
        parts = [A.clean_text_block(text, C.DIGEST_CAP)] if text else []
        if lines:
            parts.append("YOUR LAST ACTIONS\n" + "\n".join(lines))
        return "\n".join(parts) if parts else NOTHING_CHANGED

    def make_prompt(self, message, snap=None, recent=None):
        snap = self.snapshot() if snap is None else snap
        with self.lock:
            oi = self.state.get("open_intent")
            held = list(self.state["claims"])
        view = A.SpaceView(snap, self.me)
        open_text = A.clean_text((oi or {}).get("card", {}).get("will"), 120) if oi else None
        space_text = A.render_space(view, open_text, held)
        if recent is None:
            recent = self.recent_events(self.state.get("last_chat_seq") or 0, snap)
        return build_prompt(self.template, space_text, recent, self.me, message), view

    def call_model(self, prompt):
        from harness import llm
        kw = dict(LLM_ARGS, model=self.llm_model)
        if self.backend:
            kw["backend"] = self.backend
        return llm.call(prompt, retries=1, **kw)

    def think(self, prompt):
        """One reply for one prompt: {"out": dict or None, "errors": [...], "json_ok": bool, "calls": n}.
        The last JSON value is parsed and validated; a failed check is retried once with the errors appended;
        max_tokens or a refusal counts as failed (a refusal is not retried)."""
        res = self.call_model(prompt)
        calls, out, errs = 1, None, []
        for attempt in (0, 1):
            stop, out = res.stop_reason, None
            if res.error:
                errs = [f"model error: {res.error[:200]}"]
            elif stop in ("max_tokens", "refusal"):
                errs = [f"stop_reason {stop}"]
            else:
                out = A.parse_last_json(res.text)
                errs = ["no JSON object in the reply"] if out is None else A.validate(out)
            if not errs or attempt == 1 or stop == "refusal" or res.error:
                break
            res = self.call_model(prompt + RETRY_NOTE.format(errors="\n".join(f"- {e}" for e in errs[:10])))
            calls += 1
        json_ok = out is not None and not any(e.startswith(("envelope", "reply not", "ask not", "actions not")) for e in errs)
        if out is not None and errs and json_ok:           # keep the actions that check on their own
            good = [a for a in out.get("actions", []) if not A.validate({"reply": "", "ask": "", "actions": [a]})]
            out = dict(out, actions=good[:A.MAX_ACTIONS])
        elif errs:
            out = None
        return {"out": out, "errors": errs, "json_ok": json_ok, "calls": calls}

    def _work_loop(self):
        while not self.stop_event.is_set():
            job = self.jobs.get()
            if job is None:
                return
            with self.lock:
                self.job = job
            try:
                self._answer(job)
            except Exception as e:  # noqa: BLE001 - the process stays alive
                self.log(f"job {job.chat_seq} failed: {type(e).__name__}: {e}")
                with job.lock:
                    post = not (job.canned or job.errored)
                    job.done = True
                if post:
                    self.say("error", "I could not read that.", cause=job.chat_seq)
            finally:
                with self.lock:
                    self.state["last_chat_seq"] = job.chat_seq
                    self.job = None
                self.save_state()

    def _answer(self, job):
        with job.lock:
            if job.canned or job.errored:          # already answered while it waited in the queue
                job.done = True
                return
            job.started = True
        snap = self.snapshot()
        prompt, _ = self.make_prompt(job.text, snap)
        result = self.think(prompt)
        with job.lock:
            late = job.canned or job.errored
            job.done = True
        out = result["out"]
        if late:
            if out is not None:
                self.say("late", f"Late reply, nothing applied: {out.get('reply', '')}".strip(), cause=job.chat_seq)
            return
        if out is None:
            self.say("error", "I could not read that. " + "; ".join(result["errors"][:2]), cause=job.chat_seq)
            return
        self.apply_reply(out, job.chat_seq, canned=False)

    def _tick_job(self):
        # a queued job's clock runs too: its person waits as long
        for job in [self.job] + list(self.jobs.queue):
            if job is not None:
                self._tick_one(job)

    def _tick_one(self, job):
        el = self.clock() - job.t0
        post_wait = post_canned = post_error = False
        with job.lock:
            if job.done:
                return
            if el >= self.timings["waiting_s"] and not job.waited:
                job.waited = post_wait = True
            if self.fallback == "mock" and el >= self.timings["canned_s"] and not job.canned:
                job.canned = post_canned = True
            if self.fallback != "mock" and el >= self.timings["error_s"] and not job.errored:
                job.errored = post_error = True
        if post_wait:
            self.say("waiting", WAITING, cause=job.chat_seq)
        if post_canned:
            _, reply = self.canned.match(job.text)
            self.apply_reply(reply, job.chat_seq, canned=True)
        if post_error:
            self.say("error", NO_MODEL, cause=job.chat_seq)

    # ---- the policy (6.7)
    def apply_reply(self, out, chat_seq, canned=False):
        suffix = " (canned)" if canned else ""
        kind = "canned" if canned else "reply"
        if out.get("reply"):
            self.say(kind, out["reply"] + suffix, cause=chat_seq, canned=canned)
        if out.get("ask"):
            self.say("ask", out["ask"] + suffix, cause=chat_seq, canned=canned)
        actions = list(out.get("actions") or [])
        if len(actions) > A.MAX_ACTIONS:
            self.say("reply", f"I kept the first {A.MAX_ACTIONS} actions; {len(actions) - A.MAX_ACTIONS} more were left out.",
                     cause=chat_seq)
        view = self.view() if actions else None
        for action in actions[:A.MAX_ACTIONS]:
            self.apply_action(action, view, chat_seq)

    def apply_action(self, action, view, chat_seq):
        try:
            ops = A.to_ops(action, view)
        except A.Dropped as e:
            self.say("reply", f"Dropped {action.get('type')}: {e}.", cause=chat_seq)
            self._remember({"seq": None, "kind": action.get("type"), "text": str(e)[:80], "status": "rejected: unknown id"})
            return
        if A.needs_ok(action):
            self.propose(action, view, chat_seq)
            return
        self.run_ops(ops, chat_seq, view)

    def propose(self, action, view, chat_seq):
        with self.lock:
            self.n += 1
            intent = {"intent_id": f"{self.actor}-{self.t0ms}-i{self.n}", "action": action,
                      "card": A.intent_card(action, view, self.me), "chat_seq": chat_seq, "seq": None}
            if self.state.get("open_intent"):
                self.state["intent_queue"].append(intent)       # one open card at a time
                queued = True
            else:
                self.state["open_intent"] = intent
                queued = False
        if queued:
            self.say("reply", "I have another card for you after you decide the open one.", cause=chat_seq)
        else:
            self._post_intent(intent)
        self.save_state()

    def _post_intent(self, intent):
        r = self.post("intent_proposed", {"intent_id": intent["intent_id"], "action": intent["action"], "card": intent["card"]},
                      subject=f"agent:{self.actor}", label=intent["card"]["will"][:80], cause=intent["chat_seq"])
        with self.lock:
            intent["seq"] = (r or {}).get("seq")
        self._remember({"seq": intent["seq"], "kind": intent["action"]["type"], "text": intent["card"]["will"],
                        "status": "waiting for your OK"})

    def on_decided(self, ev):
        data = ev.get("data") or {}
        with self.lock:
            oi = self.state.get("open_intent")
            if not oi or data.get("intent_id") != oi["intent_id"]:
                return
            self.state["open_intent"] = None
        decision, cause = data.get("decision"), ev.get("seq")
        action = oi["action"]
        if decision == "edit":
            edited = data.get("action")
            errs = A.validate({"reply": "", "ask": "", "actions": [edited]}) if isinstance(edited, dict) else ["no action"]
            if errs:
                self.say("reply", "The edit did not check, so nothing was applied: " + "; ".join(errs[:2]), cause=cause)
                action = None
            else:
                action = edited
        if decision == "cancel":
            self.say("reply", "Cancelled. Nothing was applied.", cause=cause)
            self._remember({"seq": oi.get("seq"), "kind": oi["action"]["type"], "text": oi["card"]["will"], "status": "cancelled"})
        elif action is not None and decision in ("apply", "edit"):
            view = self.view()
            try:
                ops = A.to_ops(action, view)
            except A.Dropped as e:
                self.say("reply", f"Dropped {action.get('type')}: {e}.", cause=cause)
            else:
                self.run_ops(ops, oi.get("chat_seq") or cause, view)     # cause stays the person's chat message
        with self.lock:
            nxt = self.state["intent_queue"].pop(0) if self.state["intent_queue"] else None
            self.state["open_intent"] = nxt
        if nxt:
            self._post_intent(nxt)
        self.save_state()

    def run_ops(self, ops, cause, view, source=None):
        for op in ops:
            if op["op"] == "say":
                self.say("reply", op["text"], cause=cause)
            elif op["op"] == "event":
                r = self.post(op["kind"], op["data"], subject=op.get("subject"), label=op.get("label"), cause=cause)
                self._receipt(op, r, cause)
            elif op["op"] == "claim":
                self._claim(op, cause)

    def _receipt(self, op, r, cause):
        text = op.get("label") or op["kind"]
        if r is None:
            self._remember({"seq": None, "kind": op["kind"], "text": text, "status": "queued offline"})
            self.say("reply", "The space did not answer; I will send it when it is back.", cause=cause)
            return
        st = r.get("status")
        if st == 200:
            self._remember({"seq": r.get("seq"), "kind": op["kind"], "text": text, "status": "queued"})
            if r.get("warn") == "claimed_by_other":
                self.say("reply", f"Done, but {text} is held by someone else; your change is in and marked.", cause=cause)
            for o in r.get("overwrote") or []:
                self.say("reply", f"This replaced {A.display(o.get('by'))}'s {o.get('field', 'choice')} at #{o.get('seq')}.", cause=cause)
            return
        err = r.get("error") or f"status {st}"
        if err == "id_taken":
            self.say("reply", f"dropped: id in use. {text} is already on the map; I can comment on it instead.", cause=cause)
        else:
            self.say("reply", f"rejected: {err}", cause=cause)
        self._remember({"seq": None, "kind": op["kind"], "text": text, "status": f"rejected: {err}"})

    def _claim(self, op, cause):
        subj, name = op["subject"], op["subject"][5:]
        with self.lock:
            token = self.state["claims"].get(subj)
        body = {"action": op["action"], "subject": subj, "ttl_s": C.CLAIM_TTL_S, "purpose": op.get("purpose") or None,
                "cause": cause}
        if token is not None:
            body["token"] = token
        try:
            st, d = self.http.call("POST", "/api/claims", body)
        except (OSError, ValueError):
            self.say("reply", f"The space did not answer; {name} is not claimed.", cause=cause)
            return
        if op["action"] == "release":
            with self.lock:
                self.state["claims"].pop(subj, None)
            self.say("reply", f"Released {name}." if st == 200 else f"Release of {name}: {d.get('error', st)}.", cause=cause)
            return
        if st == 200 and "token" in d:
            with self.lock:
                self.state["claims"][subj] = d["token"]
            self.say("reply", f"Claimed {name} for you ({int(d.get('ttl_s') or C.CLAIM_TTL_S)} s, renewed while I run).", cause=cause)
        elif d.get("error") == "claimed_by_other":
            ttl = d.get("ttl_left_s")
            left = f" for {int(float(ttl))} s more" if ttl is not None else ""
            self.say("ask", f"{name} is held by {d.get('held_by')}{left}. Wait, ask them, or take it over?", cause=cause)
        else:
            self.say("reply", f"Claim of {name}: {d.get('error', st)}.", cause=cause)
        self.save_state()

    def _remember(self, row):
        with self.lock:
            self.state["actions"] = (self.state["actions"] + [row])[-3:]

    # ---- peers
    def _tick_peer(self):
        now = self.clock()
        with self.lock:
            if not self.peer_buf or now - self.last_peer < self.timings["peer_window_s"]:
                return
            evs, self.peer_buf = self.peer_buf, []
            self.last_peer = now
        lines = [self.peer_line(e) for e in evs]
        if len(lines) == 1:
            text = lines[0]
        else:
            who = sorted({A.display(e.get("owner")) for e in evs})
            text = f"{' and '.join(who)} made {len(evs)} changes. Latest: {lines[-1]}"
        self.say("peer", text[:400], cause=evs[-1].get("seq"))

    def peer_line(self, ev):
        kind, data = ev.get("kind"), ev.get("data") or {}
        who = A.display(ev.get("owner"))
        label = A.clean_text(ev.get("label") or data.get("name") or data.get("text") or "", 60)
        r, s = A.next_boundary(self.run)
        at = f"{s} r{r}"
        pick = f"round {int(self.run.get('round') or 1) + 1}"
        if kind == "node_added":
            return f"{who} added {A.clean_text(data.get('name') or label, 60)}. I carry it to the inventors at {at}."
        if kind == "note_posted":
            return f"{who} left a note for the team. The team reads it at {at}."
        if kind == "seed_added":
            return f"{who} seeded {label}. The inventors get it at {at} if round 1 has not ideated yet."
        if kind in ("question_vetoed", "question_unvetoed", "question_chosen"):
            q = self._q_label(data.get("question"), label)
            if kind == "question_vetoed":
                return f"{who} vetoed {q}. It acts at the next pick, {pick}."
            if kind == "question_unvetoed":
                return f"{who} withdrew the veto on {q}. It acts at the next pick, {pick}."
            mine = self.state.get("my_choice") or {}
            if mine.get("seq") and mine["seq"] < (ev.get("seq") or 0) and mine.get("question") != data.get("question"):
                return f"{who}'s choice replaced yours at #{ev.get('seq')}. Choose again to override."
            return f"{who} chose {q} as the next question. It acts at the next pick, {pick}."
        if kind == "reply_posted":
            verb = {"concede": "conceded an objection on", "rebut": "rebutted an objection on",
                    "measure": "answered an objection with a measurement on", "objection": "raised an objection on"}
            return f"{who} {verb.get(data.get('kind'), 'replied on')} {label}."
        if kind == "fact_disputed":
            return f"{who} disputed a fact on {label}. It stays on the map, marked."
        if kind == "vote_cast":
            return f"{who} voted {'up' if data.get('value', 0) > 0 else 'down'} on {label}. Votes are shown by name; tests decide."
        if kind == "node_skipped":
            return f"{who} skipped {label}. No ideas or builds there from {at} until it is restored."
        if kind == "node_unskipped":
            return f"{who} restored {label}. It is back from {at}."
        if kind == "run_paused":
            return f"{who} paused the run. It holds at {at} until {who} resumes."
        if kind == "run_resumed":
            return f"{who} resumed the run."
        if kind == "opinion_given":
            return f"{who} scored {label} {data.get('score')}/10."
        return f"{who} edited {label}."

    def _q_label(self, qid, label):
        top3 = ((((self.last_snap or {}).get("questions") or {}).get("preview") or {}).get("top3")) or []
        for i, row in enumerate(top3, 1):
            if isinstance(row, dict) and row.get("id") == qid:
                return f"Q{i}"
        return label or str(qid)

    # ---- stage boundaries
    def on_stage(self, ev):
        data = ev.get("data") or {}
        rnd, stage = data.get("round"), data.get("stage")
        since = int(self.state.get("digest_cursor") or 0)
        try:
            d = self.digest(since)
        except (OSError, ValueError) as e:
            self.log(f"no digest at {stage} r{rnd}: {e}")
            return
        text = d.get("text") or ""
        to_seq = int(d.get("to_seq") or ev.get("seq") or since)
        n = int(d.get("n") or 0) if text else 0
        bullets = [ln[2:] for ln in text.splitlines() if ln.startswith("- ")]
        more = re.search(r"\((\d+) more changes are in the log\.\)", text)
        k = len(bullets) + (int(more.group(1)) if more else 0)     # n counts every event in the window, not changes
        if text:
            summary = f"At {stage} r{rnd}: {k} change{'s' if k != 1 else ''} from teammates. First: {A.clean_text(bullets[0] if bullets else '', 140)}"
        else:
            summary = f"At {stage} r{rnd}: nothing new from teammates."
        self.say("digest", summary, cause=ev.get("seq"))
        self.post("digest_taken", {"from_seq": d.get("from_seq") if text else since, "to_seq": to_seq, "n": n,
                                   "chars": len(text), "role": "person", "text": text},
                  subject=f"agent:{self.actor}", cause=ev.get("seq"), round=rnd, stage=stage)
        with self.lock:
            self.state["digest_cursor"] = max(since, to_seq)
        self.save_state()
        threading.Thread(target=self.snapshot, daemon=True).start()     # refresh the cached view off this thread


def main(argv=None):
    ap = argparse.ArgumentParser(prog="python -m space.agent", description="The person-agent: one delegate per person.")
    ap.add_argument("--me", required=True, help="the person this agent works for, for example ana")
    ap.add_argument("--space", default=C.BASE_URL, help="the space server, http://127.0.0.1:8766 (never localhost)")
    ap.add_argument("--model", default="mock", choices=("sonnet", "haiku", "mock"))
    ap.add_argument("--fallback", default="mock", choices=("mock", "none"))
    ap.add_argument("--space-id", default="stage", help="names the state folder D:/AGI-lab/spaces/<space-id>/agents")
    ap.add_argument("--state-dir", default=None, help="where <me>.json lives (tests point it at a temp folder)")
    ap.add_argument("--key", default="", help="X-Space-Key for a --lan server")
    ap.add_argument("--exit-after", type=float, default=0.0, help="stop cleanly after this many seconds (0: run until Ctrl-C)")
    a = ap.parse_args(argv)
    if not re.fullmatch(r"[a-z][a-z0-9_]{0,23}", a.me):
        ap.error("--me must be a lower-case name such as ana")
    agent = Agent(a.me, a.space, model=a.model, fallback=a.fallback, state_dir=a.state_dir, space_id=a.space_id, key=a.key)
    agent.start()
    agent.log(f"running on {a.space} with model {a.model}, fallback {a.fallback}, state {agent.state_path}")
    t_end = time.monotonic() + a.exit_after if a.exit_after > 0 else None
    try:
        while t_end is None or time.monotonic() < t_end:
            time.sleep(0.2)
            if not all(t.is_alive() for t in agent.threads):
                agent.log("a worker thread ended; stopping")
                break
    except KeyboardInterrupt:
        pass
    agent.stop()
    agent.log("stopped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
