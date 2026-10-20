// store.mjs: note 02 Appendix A.4 verbatim (research_notes/product/multiplayer/02_realtime_sync.md).
// makeStore(reduce, init) takes a pure reduce(state, event). Call addPending(op, ev) when the person acts,
// queued(op, seq) when the POST returns, applyServer(ev) for every event from connectSpace, and reject(op) on a 409.
// status(op) gives pending, queued or applied. The reducer (reduce.mjs) ignores a pending copy whose op the
// server state already holds, so a queued edit is never counted twice.

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
