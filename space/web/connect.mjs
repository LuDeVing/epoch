// connect.mjs: the live connection to the space server.
// connectStream is note 02 Appendix A.3 verbatim (research_notes/product/multiplayer/02_realtime_sync.md), only renamed so
// that connectSpace can choose between it and the long-poll mode (?poll=1, design section 2).
// One addition to A.3: an error while the browser retries by itself (readyState 0) reports 'reconnecting', so a
// killed server shows Reconnecting at once instead of after the 25 s watchdog. Delivery is unchanged.
// Both modes give the same callbacks: onEvent(ev) once per seq in order, onStatus('live' | 'reconnecting' |
// 'hello' | 'presence', info), onReset() when the server's epoch changed or it sent `reset`.

export function connectSpace(opts) {
  return opts && opts.poll ? connectPoll(opts) : connectStream(opts);
}

// Browser-side live connection to the space. Plain JS, no libraries.
export function connectStream({ base, key = '', since = 0, silentMs = 25000, onEvent, onStatus, onReset }) {
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
    es.onerror = () => { if (es.readyState === 2) restart('closed_by_browser');   // 0 = browser retries itself
      else if (!stopped) onStatus('reconnecting', 'browser_retry'); };            // P4 addition: show it (section 13.3)
  }

  open();
  return { close() { stopped = true; if (es) es.close(); clearTimeout(timer); clearTimeout(wd); }, last: () => last };
}

// Long-poll mode (?poll=1): GET /api/events?since=N&limit=500&wait=25 in a loop. Same rules as the stream:
// in order, no duplicate, a changed epoch resets, a failure backs off with jitter and reopens. Presence comes
// from the answers of POST /api/presence in this mode (the app does that), not from here.
export function connectPoll({ base, key = '', since = 0, waitS = 25, onEvent, onStatus, onReset }) {
  let last = since, stopped = false, tries = 0, epoch = null, timer = null, live = false, ctl = null;
  const q = () => `since=${last}&limit=500&wait=${waitS}` + (key ? `&key=${key}` : '');

  function stop() { stopped = true; clearTimeout(timer); try { ctl && ctl.abort(); } catch (e) { /* ignore */ } }

  async function once() {
    if (stopped) return;
    ctl = typeof AbortController === 'function' ? new AbortController() : null;
    let d;
    try {
      const r = await fetch(`${base}/api/events?${q()}`, ctl ? { signal: ctl.signal } : undefined);
      if (!r.ok) throw new Error('http ' + r.status);
      d = await r.json();
    } catch (e) {
      if (stopped) return;
      live = false;
      const wait = Math.min(5000, 500 * 2 ** tries++) * (0.7 + Math.random() * 0.6);
      onStatus('reconnecting', 'poll_failed');
      timer = setTimeout(once, wait);
      return;
    }
    if (stopped) return;
    if (epoch && d.epoch && d.epoch !== epoch) { stop(); onReset && onReset(); return; }
    if (!epoch) {
      epoch = d.epoch || null;
      onStatus('hello', { epoch: d.epoch, head: d.head, replay: d.replay || null, server_time_ms: d.server_time_ms });
    }
    tries = 0;
    if (!live) { live = true; onStatus('live'); }
    if (typeof d.head === 'number' && d.head < last) { stop(); onReset && onReset(); return; }   // since ahead of head
    const before = last, got = d.events || [];
    for (const ev of got) {
      if (stopped) return;
      if (ev.seq === last + 1) { last = ev.seq; onEvent(ev); }
    }
    timer = setTimeout(once, got.length && last === before ? 1000 : 0);   // no progress: do not spin
  }

  once();
  return { close: stop, last: () => last };
}
