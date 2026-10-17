// reduce.mjs: the ordered log -> the view state of docs/MULTIPLAYER_DESIGN.md section 6.4.
// Pure: reduce(state, ev) never changes `state`; it copies only the Maps and objects it touches, because the store
// (store.mjs) replays my pending edits on top of the server state. Order is `seq` only, never `ts`.
// makeReducer({layoutTree, layoutClusters, anchorFor, contract}) returns {init(), reduce(state, ev)}.
// The layout functions come from layout.mjs (owned by the views part); core tests inject `trivialLayout`.
// `contract` is space/web/contract.json (optional): stages, winner words, and the per-kind sentence when the export
// carries one. The built-in SENTENCES below are section 6.1 word for word, so the feed and the digest say the same.

import { matchClusters } from './match.mjs';

export const STAGES = ['planned', 'ideated', 'clustered', 'deepened', 'built', 'verified'];
export const WINNER_WORD = { check_only: 'won', baseline: 'won', no_check: 'preferred' };
export const QUOTE_CAP = 160;

// kind -> digest sentence (contract.KINDS[kind][4]); null = never in a digest. Section 6.1 verbatim.
export const SENTENCES = {
  space_opened: null,
  node_added: 'added part "{label}" under "{parent}": "{frame}"',
  node_edited: 'edited part "{label}"',
  node_skipped: 'skipped part "{label}": no ideas or builds there until it is restored',
  node_unskipped: 'restored part "{label}"',
  sketch_batch: 'added {count} sketches to part "{label}"',
  cluster_snapshot: 'regrouped part "{label}" into {n} clusters',
  objection_raised: 'raised a {severity} objection on "{label}": "{text}"',
  reply_posted: 'replied ({kind}) on "{label}": "{text}"',
  objection_marked: 'marked an objection on "{label}" {verdict}',
  candidate_built: 'built "{label}" on part "{node}"',
  test_result: 'test of "{label}" on "{node}": {status} {metric}',
  memory_added: 'added {n_added} memory entries to part "{label}"',
  question_preview: null,
  question_picked: 'team question is now "{label}" ({by})',
  question_vetoed: 'vetoed question "{label}"',
  question_unvetoed: 'withdrew the veto on question "{label}"',
  question_chosen: 'chose question "{label}" as next',
  opinion_given: 'scored "{label}" {score}/10 ({note})',
  vote_cast: 'voted {value} on "{label}"',
  fact_disputed: 'disputed a fact on "{label}": "{fact}". Reason: "{reason}" ({tag}). It stays on the map, marked',
  note_posted: 'noted: "{text}"',
  seed_added: 'seeded part "{label}": "{text}"',
  run_paused: 'paused the run',
  run_resumed: 'resumed the run',
  run_step: null,
  stage_entered: null,
  control_applied: null,
  digest_taken: null,
  claim_granted: 'is working on part "{label}"{why}; do not touch it',
  claim_released: 'released part "{label}"',
  claim_expired: 'claim of {owner_was} on part "{label}" ended',
  claim_taken_over: 'took over part "{label}"',
  chat_posted: null,
  agent_said: null,
  intent_proposed: null,
  intent_decided: null,
};

// Feed lines for kinds that have no digest sentence (they are never in a digest, but the feed shows them).
export const FEED_EXTRA = {
  space_opened: 'opened the space',
  question_preview: 'previewed the next questions for round {round_next}',
  run_step: 'pressed Go at {stage}, round {round}',
  stage_entered: '{reached} {stage}, round {round}',
  control_applied: 'applied {n_refs} changes at {stage}, round {round}',
  digest_taken: 'told {agent} {n} changes (e{from_seq} to e{to_seq})',
};
// Kinds the feed leaves to the My agent tab.
export const NOT_IN_FEED = new Set(['chat_posted', 'agent_said', 'intent_proposed', 'intent_decided']);
// Kinds whose author is a person or a delegate and that the loop folds at a boundary (they carry a status chip).
export const CONTROL_KINDS = new Set(['node_added', 'node_skipped', 'node_unskipped', 'question_vetoed',
  'question_unvetoed', 'question_chosen', 'opinion_given', 'fact_disputed', 'note_posted', 'seed_added',
  'run_paused', 'run_resumed', 'run_step']);
export const PICK_KINDS = new Set(['question_vetoed', 'question_unvetoed', 'question_chosen']);
const HUES = ['a', 'b', 'c'];
const POSITIVE = new Set(['win', 'preferred']);
const NEGATIVE = new Set(['loss', 'not_preferred', 'failed_check']);

// ---- small pure helpers -------------------------------------------------------------------------------------

export function actorClass(by, byKind, owner) {          // contract.actor_class, in JS
  if (by === 'server') return 'server';
  if (byKind === 'system' || String(by || '').startsWith('team.')) return 'team';
  if (byKind === 'agent' && owner !== by) return 'delegate';
  if (byKind === 'human') return 'person';
  return 'agent';
}

export function ownerOf(by) { return String(by || '').split('.')[0]; }

// The loop's cleaning (nano/loop.py _add_human_nodes, space/store.py clean_id): drop every other character.
export function cleanId(raw) { return String(raw || '').toLowerCase().replace(/[^a-z0-9_]/g, '').slice(0, 16); }

export function q(text, cap = QUOTE_CAP) {               // a person's words: tags stripped, whitespace folded, cut
  let t = String(text == null ? '' : text).replace(/<[^>]*>/g, '').replace(/\s+/g, ' ').trim();
  if (t.length > cap) t = t.slice(0, cap - 3).trimEnd() + '...';
  return t;
}

export function fnv1a(str) {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) { h ^= str.charCodeAt(i); h = Math.imul(h, 0x01000193) >>> 0; }
  return h.toString(16).padStart(8, '0');
}

const byFirst = (a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0);

// FNV-1a 32 over the JSON of [[id, x, y] sorted by id] plus [[key, x, y, r] sorted by key], 8 hex (section 6.5).
export function hashLayout(layout) {
  const t = [...(layout.tree || new Map())].map(([id, p]) => [id, p.x, p.y]).sort(byFirst);
  const c = [...(layout.clusters || new Map())].map(([k, p]) => [k, p.x, p.y, p.r]).sort(byFirst);
  return fnv1a(JSON.stringify(t) + JSON.stringify(c));
}

const round2 = (v) => Math.round(v * 100) / 100;
export const clusterRadius = (n) => 7.8 * Math.sqrt((n || 0) + 0.5) + 6;

// The trivial layout of section 6.5 for core tests and for the page before layout.mjs lands:
// tree x = depth * 250, y = order * 56 (order = first-seen rank); clusters in a row at their island anchor.
export const trivialLayout = {
  layoutTree(nodes, firstSeen) {
    const ids = [...nodes.keys()].sort((a, b) => (firstSeen.get(a) - firstSeen.get(b)) || (a < b ? -1 : a > b ? 1 : 0));
    const depth = (id) => { let d = 0, cur = nodes.get(id); const seen = new Set();
      while (cur && cur.parent != null && nodes.has(cur.parent) && !seen.has(cur.parent)) { seen.add(cur.parent); d++; cur = nodes.get(cur.parent); }
      return d; };
    return new Map(ids.map((id, i) => [id, { x: depth(id) * 250, y: i * 56 }]));
  },
  anchorFor(partIndex) { return { x: partIndex * 440, y: 0 }; },
  layoutClusters(prevIsland, islandClusters, anchor) {
    return new Map(islandClusters.map((c, i) => [c.key, { x: round2(anchor.x + i * 40), y: round2(anchor.y), r: round2(clusterRadius(c.n)) }]));
  },
};

// The boundary at which the loop folds a queued item: the stage it waits at, else the next one (section 4.7).
export function nextBoundary(run) {
  const r = run || {};
  if (!r.stage) return { stage: 'planned', round: Math.max(1, r.round || 1) };
  if (r.waiting) return { stage: r.stage, round: r.round || 1 };
  const i = STAGES.indexOf(r.stage);
  if (i < 0) return { stage: 'planned', round: Math.max(1, r.round || 1) };
  if (i === STAGES.length - 1) return { stage: 'ideated', round: (r.round || 1) + 1 };
  return { stage: STAGES[i + 1], round: r.round || 1 };
}

// Chip text of section 4.7 for a feed item, a node, a veto or a choice: {status, kind, appliedAt, pickRound, reason}.
export function chipText(item, run) {
  if (!item) return '';
  const pick = PICK_KINDS.has(item.kind);
  switch (item.status) {
    case 'pending': return 'sending';
    case 'queued': {
      if (pick) return `acts at the next pick, round ${((run && run.round) || 1) + 1}`;
      const b = nextBoundary(run);
      return `waits for ${b.stage}, round ${b.round}`;
    }
    case 'applied':
      if (pick) return `applied at the pick of round ${item.pickRound}`;
      return item.appliedAt ? `applied in round ${item.appliedAt.round}, stage ${item.appliedAt.stage}` : 'applied';
    case 'not_in_top3': return `not in the top 3 at the pick of round ${item.pickRound}`;
    case 'overwritten': return item.overwrittenBy
      ? `replaced by ${whoText({ cls: 'person', owner: item.overwrittenBy.by })}'s choice at #${item.overwrittenBy.seq}` : 'replaced';
    case 'withdrawn': return 'withdrawn';
    case 'rejected': return item.reason === 'id_taken' ? 'dropped: id in use' : `rejected: ${item.reason || 'error'}`;
    default: return '';
  }
}

// Who wrote a line: "Ana" for a person, "Ana via agent" for a delegate, "the team" for the loop, "" for the server.
export function whoText(item) {
  const cap = (s) => (s ? s[0].toUpperCase() + s.slice(1) : s);
  if (item.cls === 'person') return cap(item.owner);
  if (item.cls === 'delegate') return `${cap(item.owner)} via agent`;
  if (item.cls === 'team') return 'the team';
  if (item.cls === 'server') return '';
  return item.by;
}

// Bursts: consecutive lines with the same author, kind and node fold into one ("x N").
export function groupFeed(feed) {
  const out = [];
  for (const it of feed) {
    const top = out[out.length - 1];
    if (top && top.by === it.by && top.kind === it.kind && top.node === it.node && !CONTROL_KINDS.has(it.kind)) {
      out[out.length - 1] = { ...it, count: top.count + 1, first: top.first };
    } else out.push({ ...it, count: 1, first: it.seq });
  }
  return out;
}

export function hitOf(value, status) {
  if (POSITIVE.has(status)) return value > 0 ? 'hit' : 'miss';
  if (NEGATIVE.has(status)) return value > 0 ? 'miss' : 'hit';
  return 'open';
}

function metricText(d) {
  const m = d.metrics || {};
  const nums = Object.keys(m).filter((k) => typeof m[k] === 'number' && Number.isFinite(m[k])).slice(0, 2);
  if (nums.length) return nums.map((k) => `${k} ${round2(m[k])}`).join(', ');
  return d.reason || '';
}

export function fill(template, vals) {
  return template.replace(/\{(\w+)\}/g, (_, k) => (vals[k] == null || typeof vals[k] === 'object' ? '' : String(vals[k])));
}

// ---- the reducer ----------------------------------------------------------------------------------------------

export function makeReducer({ layoutTree, layoutClusters, anchorFor, contract } = {}) {
  const L = {
    layoutTree: layoutTree || trivialLayout.layoutTree,
    layoutClusters: layoutClusters || trivialLayout.layoutClusters,
    anchorFor: anchorFor || trivialLayout.anchorFor,
  };
  const sentences = { ...SENTENCES };
  if (contract && contract.kinds) {
    for (const [k, v] of Object.entries(contract.kinds)) if (v && typeof v.sentence === 'string') sentences[k] = v.sentence;
  }
  const stages = (contract && contract.stages) || STAGES;
  const winnerWord = (contract && contract.winner_word) || WINNER_WORD;

  function init() {
    const layout = { tree: new Map(), clusters: new Map(), anchors: new Map(), hash: '' };
    layout.hash = hashLayout(layout);
    return {
      head: 0, epoch: null, replay: null, spaceId: null,
      run: { round: 0, stage: null, waiting: false, stepMode: false, pausedBy: [], mode: 'check_only', lastBoundary: null },
      people: new Map(), nodes: new Map(), clusters: new Map(), chains: new Map(), results: [],
      questions: { preview: null, picked: null, vetoes: new Map(), chosen: null },
      feed: [], chat: new Map(), intents: new Map(), digests: [], memory: new Map(),
      presence: { clients: [], claims: [] },
      layout, match: { prev: new Map(), counter: 0 },
      // bookkeeping beyond section 6.4 (read only by this module, the rail and the tests)
      retired: new Map(),        // key -> a cluster that a regrouping removed, with mergedInto (the latest per island)
      ops: new Map(),            // op -> seq for every numbered event of a person or a delegate
      sketches: new Map(),       // sketch id -> {owner, seq}
      cands: new Map(),          // candidate id -> cluster key
      seedOwners: new Map(),     // node -> owner of the latest seed
      islands: [],               // nodes with clusters, in first-seen order (the anchor order)
      stages, winnerWord,
    };
  }

  function reduce(state, ev) {
    if (!ev || !ev.kind) return state;
    const seq = typeof ev.seq === 'number' ? ev.seq : null;
    if (seq !== null && seq <= state.head) return state;                     // a repeat: ignore
    if (seq === null && ev.op && state.ops.has(ev.op)) return state;         // my pending copy, already numbered
    const s = { ...state, head: seq !== null ? seq : state.head };
    const cls = actorClass(ev.by, ev.by_kind, ev.owner);
    const owner = ev.owner || (cls === 'team' ? 'team' : ownerOf(ev.by));
    const ctx = { seq, cls, owner, pending: seq === null, copied: new Set(), tree: false, islands: new Set(),
      human: cls === 'person' || cls === 'delegate', layoutChanged: false };
    if (ctx.human && seq !== null) {
      if (!s.people.has(owner)) mapOf(s, ctx, 'people').set(owner, { name: owner, hue: HUES[s.people.size % HUES.length], firstSeen: seq });
      if (ev.op) mapOf(s, ctx, 'ops').set(ev.op, seq);
    }
    const h = HANDLERS[ev.kind];
    if (h) h(s, ev, ctx);
    if (!NOT_IN_FEED.has(ev.kind)) addFeed(s, ev, ctx);
    relayout(s, ctx);
    return s;
  }

  // ---- copy-on-write helpers
  function mapOf(s, ctx, name) {
    if (!ctx.copied.has(name)) { s[name] = new Map(s[name]); ctx.copied.add(name); }
    return s[name];
  }
  function objOf(s, ctx, name) {
    if (!ctx.copied.has(name)) { s[name] = { ...s[name] }; ctx.copied.add(name); }
    return s[name];
  }
  function questionsOf(s, ctx) { return objOf(s, ctx, 'questions'); }
  function patchNode(s, ctx, id, patch) {
    const n = s.nodes.get(id);
    if (!n) return null;
    const next = { ...n, ...(typeof patch === 'function' ? patch(n) : patch) };
    mapOf(s, ctx, 'nodes').set(id, next);
    return next;
  }
  const halo = (ctx) => ({ by: ctx.owner, seq: ctx.seq });
  const zero = () => ({ sketches: 0, clusters: 0, built: 0, checked: 0 });
  function bumpCount(s, ctx, id, dir, field, by = 1, set = null) {
    patchNode(s, ctx, id, (n) => {
      const counts = { ...(n.counts || {}) };
      const d = dir === 'outward' ? 'outward' : (dir === 'upward' ? 'upward' : 'inward');
      const c = { ...(counts[d] || zero()) };
      c[field] = set !== null ? set : (c[field] || 0) + by;
      counts[d] = c;
      return { counts, halo: halo(ctx) };
    });
  }
  const subjectId = (ev) => {
    const m = /^[a-z]+:(.+)$/.exec(ev.subject || '');
    return m ? m[1] : null;
  };
  const nodeName = (s, id) => (id != null && s.nodes.get(id) ? s.nodes.get(id).name : (id == null ? '' : String(id)));

  // A cluster key for an event that names an idea: the key itself, the best member overlap, the positional
  // cluster_id on the same part, or the name.
  function clusterKeyFor(s, node, idea, members, name) {
    if (idea != null && s.clusters.has(idea)) return idea;
    const live = [...s.clusters.values()].filter((c) => node == null || c.node === node);
    if (members && members.length) {
      const set = new Set(members);
      let best = null, bestN = 0;
      for (const c of live) {
        const n = c.members.reduce((a, m) => a + (set.has(m) ? 1 : 0), 0);
        if (n > bestN) { bestN = n; best = c.key; }
      }
      if (best) return best;
    }
    if (idea != null) { const c = live.find((x) => x.clusterId === idea); if (c) return c.key; }
    const nm = name != null ? name : idea;
    if (nm != null) { const c = live.find((x) => x.name === nm); if (c) return c.key; }
    return null;
  }

  function votersFor(cluster, status) {
    const out = {};
    for (const [who, v] of Object.entries((cluster && cluster.votes) || {})) out[who] = hitOf(v, status);
    return out;
  }

  function setResults(s, ctx, fn) {
    if (!ctx.copied.has('results')) { s.results = s.results.slice(); ctx.copied.add('results'); }
    fn(s.results);
  }

  function pushChat(s, ctx, person, line) {
    const chat = mapOf(s, ctx, 'chat');
    chat.set(person, [...(chat.get(person) || []), line]);
  }

  // ---- one handler per kind (37 on day one)
  const HANDLERS = {
    space_opened(s, ev) { const d = ev.data || {}; s.epoch = d.epoch || s.epoch; s.spaceId = d.space_id || s.spaceId;
      if (d.mode) s.run = { ...s.run, mode: d.mode }; },

    node_added(s, ev, ctx) {
      const d = ev.data || {};
      const id = cleanId(d.id || d.name || ev.label);
      if (!id) return;
      const old = s.nodes.get(id);
      if (old) {                                     // the loop mirrors a node that already exists: fill gaps only
        if (ctx.cls === 'team') patchNode(s, ctx, id, (n) => ({
          frame: n.frame ?? d.frame ?? null, test: n.test ?? d.test ?? null, threshold: n.threshold ?? d.threshold ?? null,
          failsIf: n.failsIf ?? d.fails_if ?? null, kind: n.kind || d.kind || 'part' }));
        return;
      }
      const parent = d.parent === undefined ? null : d.parent;
      mapOf(s, ctx, 'nodes').set(id, {
        id, name: d.name || ev.label || id, parent, kind: d.kind || (parent == null ? 'root' : 'part'),
        origin: d.origin || (ctx.human ? 'human' : 'map'), by: ev.by, owner: ctx.owner, seq: ctx.seq,
        status: ctx.human ? (ctx.pending ? 'pending' : 'queued') : 'map', appliedAt: null, reason: null,
        skippedBy: null, lowered: d.priority === 'low', disputed: [], claim: null,
        counts: { inward: zero(), outward: zero() }, frame: d.frame ?? null, assumptions: d.assumptions || [],
        directions: d.directions || null, test: d.test ?? null, threshold: d.threshold ?? null, failsIf: d.fails_if ?? null,
        halo: halo(ctx), firstSeen: ctx.seq !== null ? ctx.seq : s.head + 0.5, op: ev.op || null,
      });
      ctx.tree = true;
    },
    node_edited(s, ev, ctx) {
      const d = ev.data || {}, f = d.fields || {};
      const id = subjectId(ev) || d.node || d.id;
      patchNode(s, ctx, id, (n) => ({ name: f.name || n.name, frame: f.frame ?? n.frame,
        lowered: f.priority ? f.priority === 'low' : n.lowered, halo: halo(ctx) }));
    },
    node_skipped(s, ev, ctx) { patchNode(s, ctx, subjectId(ev) || (ev.data || {}).node, { skippedBy: ctx.owner, halo: halo(ctx) }); },
    node_unskipped(s, ev, ctx) { patchNode(s, ctx, subjectId(ev) || (ev.data || {}).node, { skippedBy: null, halo: halo(ctx) }); },

    sketch_batch(s, ev, ctx) {
      const d = ev.data || {};
      const items = d.items || [];
      const sk = mapOf(s, ctx, 'sketches');
      for (const it of items) {
        const who = it.owner || (it.card === 'owner' && s.seedOwners.get(d.node)) || 'team';
        if (it.id && !sk.has(it.id)) sk.set(it.id, { owner: who, seq: ctx.seq });
      }
      bumpCount(s, ctx, d.node, d.direction, 'sketches', d.count != null ? d.count : items.length);
    },

    cluster_snapshot(s, ev, ctx) {
      const d = ev.data || {};
      const node = d.node, dir = d.direction || 'inward', k = `${node}/${dir}`;
      const next = (d.clusters || []).map((c) => ({ ...c, members: c.members || [] }));
      const match = objOf(s, ctx, 'match');
      const prev = match.prev.get(k) || [];
      const r = matchClusters(prev, next, match.counter, 0.3);
      match.prev = new Map(match.prev).set(k, next.map((c, i) => ({ vid: r.vids[i], members: c.members })));
      match.counter = r.counter;
      const clusters = mapOf(s, ctx, 'clusters');
      const retired = mapOf(s, ctx, 'retired');
      for (const [key, c] of retired) if (c.node === node && c.direction === dir) retired.delete(key);
      for (const dd of r.dead) {
        const old = clusters.get(dd.vid);
        clusters.delete(dd.vid);
        if (old) retired.set(dd.vid, { ...old, mergedInto: dd.into, retiredAt: ctx.seq });
      }
      next.forEach((c, i) => {
        const key = r.vids[i], old = clusters.get(key);
        const contributors = {};
        for (const m of c.members) { const w = (s.sketches.get(m) || {}).owner || 'team'; contributors[w] = (contributors[w] || 0) + 1; }
        clusters.set(key, {
          key, clusterId: c.cluster_id ?? null, node, direction: dir, name: c.name || (old && old.name) || key,
          members: c.members.slice(), n: c.n != null ? c.n : c.members.length, rank: c.rank ?? null, score: c.score ?? null,
          selected: !!c.selected, lane: c.lane ?? null, prior: c.prior ?? null, contributors,
          votes: old ? old.votes : {}, status: old ? old.status : 'open',
          bornFrom: old ? null : (r.born[key] || null), mergedInto: null,
          firstSeen: old ? old.firstSeen : ctx.seq, seq: ctx.seq, index: i, round: d.round ?? null,
        });
      });
      bumpCount(s, ctx, node, dir, 'clusters', 0, next.length);
      ctx.islands.add(node);
      ctx.born = r.born;
    },

    objection_raised(s, ev, ctx) {
      const d = ev.data || {};
      const key = clusterKeyFor(s, d.node, d.idea, d.members) || `${d.node}:${d.idea}`;
      const chains = mapOf(s, ctx, 'chains');
      chains.set(key, [...(chains.get(key) || []), {
        objection: { n: d.objection, cls: d.cls, severity: d.severity, text: d.text, ifTrue: d.if_true ?? null, by: ev.by, seq: ctx.seq },
        reply: null, mark: null }]);
    },
    reply_posted(s, ev, ctx) {
      const d = ev.data || {};
      const key = clusterKeyFor(s, d.node, d.idea, d.members) || `${d.node}:${d.idea}`;
      const chains = mapOf(s, ctx, 'chains');
      const list = [...(chains.get(key) || [])];
      const reply = { kind: d.kind, text: d.text, fact: d.fact ?? null, source: d.source ?? null, by: ev.by, owner: ctx.owner,
        seq: ctx.seq, cls: ctx.cls };
      const i = list.findIndex((e) => e.objection && e.objection.n === d.objection);
      if (d.kind === 'objection' || i < 0) {                 // a person's objection joins the list as a new line
        const n = d.objection != null && i < 0 ? d.objection : list.length + 1;
        list.push(d.kind === 'objection'
          ? { objection: { n, cls: 'person', severity: null, text: d.text, ifTrue: null, by: ev.by, seq: ctx.seq }, reply: null, mark: null }
          : { objection: null, reply, mark: null });
      } else if (!list[i].reply) list[i] = { ...list[i], reply };
      else list[i] = { ...list[i], more: [...(list[i].more || []), reply] };
      chains.set(key, list);
    },
    objection_marked(s, ev, ctx) {
      const d = ev.data || {};
      const key = clusterKeyFor(s, d.node, d.idea, d.members) || `${d.node}:${d.idea}`;
      const chains = mapOf(s, ctx, 'chains');
      const list = [...(chains.get(key) || [])];
      const i = list.findIndex((e) => e.objection && e.objection.n === d.objection);
      if (i >= 0) { list[i] = { ...list[i], mark: { verdict: d.verdict, reason: d.reason ?? null, seq: ctx.seq } }; chains.set(key, list); }
    },

    candidate_built(s, ev, ctx) {
      const d = ev.data || {};
      const key = clusterKeyFor(s, d.node, d.idea, d.members, d.cluster_name);
      mapOf(s, ctx, 'cands').set(d.cand, key);
      const c = key && s.clusters.get(key);
      if (c) mapOf(s, ctx, 'clusters').set(key, { ...c, status: 'built' });
      bumpCount(s, ctx, d.node, (c && c.direction) || d.direction, 'built');
      setResults(s, ctx, (rs) => {
        if (rs.some((x) => x.cand === d.cand)) return;
        rs.push({ cand: d.cand, key, node: d.node, status: 'built', rung: null, metrics: {}, reason: null, reference: false,
          seq: ctx.seq, voters: votersFor(c, 'built'), name: d.cluster_name || (c && c.name) || null,
          hypothesis: d.hypothesis ?? null, lane: d.lane ?? null, round: d.round ?? null });
      });
    },
    test_result(s, ev, ctx) {
      const d = ev.data || {};
      const key = s.cands.get(d.cand) || clusterKeyFor(s, d.node, d.idea, d.members);
      const c = key && s.clusters.get(key);
      if (c) mapOf(s, ctx, 'clusters').set(key, { ...c, status: d.status });
      let first = true;
      setResults(s, ctx, (rs) => {
        const i = rs.findIndex((x) => x.cand === d.cand);
        const row = { cand: d.cand, key, node: d.node, status: d.status, rung: d.rung ?? null, metrics: d.metrics || {},
          reason: d.reason ?? null, reference: !!d.reference, seq: ctx.seq, voters: votersFor(c, d.status) };
        if (i >= 0) { first = rs[i].status === 'built'; rs[i] = { ...rs[i], ...row }; } else rs.push({ ...row, name: (c && c.name) || null });
      });
      if (first) bumpCount(s, ctx, d.node, c && c.direction, 'checked');
    },
    vote_cast(s, ev, ctx) {
      const d = ev.data || {};
      const key = clusterKeyFor(s, d.node, d.idea, null);
      const c = key && s.clusters.get(key);
      if (!c) return;
      const votes = { ...c.votes };
      if (!d.value) delete votes[ctx.owner]; else votes[ctx.owner] = d.value > 0 ? 1 : -1;
      mapOf(s, ctx, 'clusters').set(key, { ...c, votes });
      if (s.results.some((r) => r.key === key)) {
        setResults(s, ctx, (rs) => { rs.forEach((r, i) => { if (r.key === key) rs[i] = { ...r, voters: votersFor({ votes }, r.status) }; }); });
      }
    },
    memory_added(s, ev, ctx) {
      const d = ev.data || {};
      const mem = mapOf(s, ctx, 'memory');
      mem.set(d.node, [...(mem.get(d.node) || []), ...(d.added || []).map((a) => ({ id: a.id, section: a.section,
        source: a.source, text: a.text, round: d.round ?? null, seq: ctx.seq }))]);
    },

    question_preview(s, ev, ctx) {
      const d = ev.data || {};
      questionsOf(s, ctx).preview = { roundNext: d.round_next, top3: d.top3 || [], explore: d.explore ?? null,
        nCandidates: d.n_candidates ?? null, seq: ctx.seq };
    },
    question_picked(s, ev, ctx) {
      const d = ev.data || {};
      const qs = questionsOf(s, ctx);
      const vetoed = d.vetoed || [];
      qs.picked = { round: d.round, top3: d.top3 || [], chosen: d.chosen ?? null, by: d.by, vetoed, seq: ctx.seq };
      const vetoes = new Map(qs.vetoes);
      for (const id of vetoed) {
        if (vetoes.has(id)) vetoes.set(id, vetoes.get(id).map((v) => (v.status === 'applied' ? v : { ...v, status: 'applied', pickRound: d.round })));
      }
      qs.vetoes = vetoes;
      const ids = new Set((d.top3 || []).map((t) => t.id));
      if (qs.chosen && qs.chosen.status === 'queued') {
        if (d.chosen === qs.chosen.id) qs.chosen = { ...qs.chosen, status: 'applied', pickRound: d.round };
        else if (!ids.has(qs.chosen.id)) qs.chosen = { ...qs.chosen, status: 'not_in_top3', pickRound: d.round };
      }
      ctx.pick = { round: d.round, vetoed: new Set(vetoed), chosen: d.chosen, ids };
    },
    question_vetoed(s, ev, ctx) {
      const d = ev.data || {};
      const id = d.question || subjectId(ev);
      const qs = questionsOf(s, ctx);
      qs.vetoes = new Map(qs.vetoes).set(id, [...(qs.vetoes.get(id) || []),
        { by: ctx.owner, seq: ctx.seq, status: ctx.pending ? 'pending' : 'queued', pickRound: null, text: d.text ?? null, kind: 'question_vetoed' }]);
    },
    question_unvetoed(s, ev, ctx) {
      const id = (ev.data || {}).question || subjectId(ev);
      const qs = questionsOf(s, ctx);
      const v = new Map(qs.vetoes); v.delete(id); qs.vetoes = v;
    },
    question_chosen(s, ev, ctx) {
      const d = ev.data || {};
      const qs = questionsOf(s, ctx);
      const prev = qs.chosen;
      let overwrote = Array.isArray(d.overwrote) && d.overwrote.length ? d.overwrote : [];
      if (!overwrote.length && prev && prev.by !== ctx.owner && prev.status !== 'applied') overwrote = [{ field: 'choose', seq: prev.seq, by: prev.by }];
      qs.chosen = { id: d.question || subjectId(ev), text: d.text ?? null, by: ctx.owner, seq: ctx.seq, overwrote,
        status: ctx.pending ? 'pending' : 'queued', pickRound: null, kind: 'question_chosen',
        prev: prev ? { id: prev.id, by: prev.by, seq: prev.seq, text: prev.text } : null };
    },
    opinion_given() {},
    fact_disputed(s, ev, ctx) {
      const d = ev.data || {};
      patchNode(s, ctx, d.node || subjectId(ev), (n) => ({ disputed: [...n.disputed,
        { by: ctx.owner, reason: d.reason ?? null, tag: d.tag ?? null, seq: ctx.seq, fact: d.fact ?? null }], halo: halo(ctx) }));
    },
    note_posted() {},
    seed_added(s, ev, ctx) { const d = ev.data || {}; if (d.node) mapOf(s, ctx, 'seedOwners').set(d.node, ctx.owner); },
    run_paused(s, ev, ctx) { if (!s.run.pausedBy.includes(ctx.owner)) s.run = { ...s.run, pausedBy: [...s.run.pausedBy, ctx.owner] }; },
    run_resumed(s, ev, ctx) { s.run = { ...s.run, pausedBy: s.run.pausedBy.filter((p) => p !== ctx.owner) }; },
    run_step() {},
    stage_entered(s, ev, ctx) {
      const d = ev.data || {};
      const round = d.round ?? ev.round ?? s.run.round, stage = d.stage ?? ev.stage ?? s.run.stage;
      s.run = { ...s.run, round, stage, waiting: !!d.waiting, stepMode: d.step_mode ?? s.run.stepMode,
        mode: d.mode || s.run.mode, lastBoundary: { round, stage, seq: ctx.seq } };
    },
    control_applied(s, ev, ctx) {
      const d = ev.data || {};
      const at = { round: d.round ?? ev.round, stage: d.stage ?? ev.stage, seq: ctx.seq };
      const refs = new Set(d.refs || []);
      const dropped = new Map((d.dropped || []).map((x) => [x.seq, x.reason]));
      for (const n of s.nodes.values()) {
        if (n.seq == null) continue;
        if (dropped.has(n.seq)) patchNode(s, ctx, n.id, { status: 'rejected', reason: dropped.get(n.seq) });
        else if (refs.has(n.seq) && (n.status === 'queued' || n.status === 'pending')) patchNode(s, ctx, n.id, { status: 'applied', appliedAt: at });
      }
      ctx.applied = { refs, dropped, at };
      // the loop folds only after the Go: the wait at this boundary is over, so new items wait for the next one
      if (s.run.waiting && at.round === s.run.round && at.stage === s.run.stage) s.run = { ...s.run, waiting: false };
    },
    digest_taken(s, ev, ctx) {
      const d = ev.data || {};
      const round = ev.round ?? d.round ?? s.run.round, stage = ev.stage ?? d.stage ?? s.run.stage;
      s.digests = [...s.digests, { agent: ev.by, role: d.role, round, stage, fromSeq: d.from_seq, toSeq: d.to_seq,
        n: d.n, chars: d.chars, text: d.text ?? '', seq: ctx.seq }];
      ctx.receipt = { agent: ev.by, owner: ctx.owner, round, stage, seq: ctx.seq, from: d.from_seq, to: d.to_seq };
    },
    claim_granted(s, ev, ctx) {
      const d = ev.data || {};
      const ms = Date.parse(ev.ts || '');
      patchNode(s, ctx, subjectId(ev), { claim: { holder: d.owner, owner: ownerOf(d.owner), token: ctx.seq,
        untilMs: Number.isFinite(ms) ? ms + 1000 * (d.ttl_s || 90) : null, purpose: d.purpose ?? null },
        halo: { by: ownerOf(d.owner), seq: ctx.seq } });
    },
    claim_released(s, ev, ctx) { patchNode(s, ctx, subjectId(ev), { claim: null }); },
    claim_expired(s, ev, ctx) { patchNode(s, ctx, subjectId(ev), { claim: null }); },
    claim_taken_over(s, ev, ctx) {
      const d = ev.data || {};
      const ms = Date.parse(ev.ts || '');
      patchNode(s, ctx, subjectId(ev), { claim: { holder: d.to, owner: ownerOf(d.to), token: ctx.seq,
        untilMs: Number.isFinite(ms) ? ms + 1000 * (d.ttl_s || 90) : null, purpose: d.purpose ?? null },
        halo: { by: ownerOf(d.to), seq: ctx.seq } });
    },
    chat_posted(s, ev, ctx) {
      const d = ev.data || {};
      pushChat(s, ctx, ctx.owner, { seq: ctx.seq, from: ev.by, kind: 'chat', text: d.text ?? '', canned: false, card: null,
        cause: ev.cause ?? null, shared: d.shared !== false, to: d.to ?? null });
    },
    agent_said(s, ev, ctx) {
      const d = ev.data || {};
      pushChat(s, ctx, ctx.owner, { seq: ctx.seq, from: ev.by, kind: d.kind, text: d.text ?? '', canned: !!d.canned, card: null,
        cause: ev.cause ?? null });
    },
    intent_proposed(s, ev, ctx) {
      const d = ev.data || {};
      mapOf(s, ctx, 'intents').set(d.intent_id, { action: d.action || {}, card: d.card || {}, decision: null, seq: ctx.seq, by: ev.by, owner: ctx.owner });
      pushChat(s, ctx, ctx.owner, { seq: ctx.seq, from: ev.by, kind: 'intent', text: (d.card && d.card.will) || '', canned: false,
        card: d.card || {}, cause: ev.cause ?? null, intentId: d.intent_id, action: d.action || {} });
    },
    intent_decided(s, ev, ctx) {
      const d = ev.data || {};
      const it = s.intents.get(d.intent_id);
      mapOf(s, ctx, 'intents').set(d.intent_id, { ...(it || { action: {}, card: {}, seq: null }), decision: d.decision,
        decidedSeq: ctx.seq, action: d.action || (it && it.action) || {} });
    },
  };

  // ---- the feed: one typed line per event, then the status changes that this event causes
  function addFeed(s, ev, ctx) {
    const d = ev.data || {};
    const kind = ev.kind;
    let feed = s.feed;
    let copied = false;
    const edit = (i, patch) => { if (!copied) { feed = feed.slice(); copied = true; } feed[i] = { ...feed[i], ...patch }; };

    if (ctx.applied) {                                // control_applied: queued -> applied, dropped -> rejected
      const { refs, dropped, at } = ctx.applied;
      feed.forEach((it, i) => {
        if (it.seq == null) return;
        if (dropped.has(it.seq)) edit(i, { status: 'rejected', reason: dropped.get(it.seq) });
        else if (refs.has(it.seq) && it.status === 'queued' && !PICK_KINDS.has(it.kind)) edit(i, { status: 'applied', appliedAt: at });
      });
    }
    if (kind === 'question_chosen' || kind === 'question_unvetoed') {   // a later choice replaces; an unveto withdraws
      const qid = d.question || subjectId(ev);
      feed.forEach((it, i) => {
        if (it.status !== 'queued' && it.status !== 'pending') return;
        if (kind === 'question_chosen' && it.kind === 'question_chosen') edit(i, { status: 'overwritten', overwrittenBy: { by: ctx.owner, seq: ctx.seq } });
        if (kind === 'question_unvetoed' && it.kind === 'question_vetoed' && it.question === qid) edit(i, { status: 'withdrawn' });
      });
    }
    if (ctx.pick) {                                   // question_picked: a veto or a choice acts only here
      const p = ctx.pick;
      feed.forEach((it, i) => {
        if (it.status !== 'queued') return;
        const qid = it.question;
        if (it.kind === 'question_vetoed' && p.vetoed.has(qid)) edit(i, { status: 'applied', pickRound: p.round });
        if (it.kind === 'question_unvetoed') edit(i, { status: 'applied', pickRound: p.round });
        if (it.kind === 'question_chosen') {
          if (p.chosen === qid) edit(i, { status: 'applied', pickRound: p.round });
          else if (!p.ids.has(qid)) edit(i, { status: 'not_in_top3', pickRound: p.round });
        }
      });
    }
    if (ctx.receipt) {                                // digest_taken: a receipt on every person's line it carried
      const r = ctx.receipt;
      feed.forEach((it, i) => {
        if (it.seq == null || !(it.cls === 'person' || it.cls === 'delegate')) return;
        if (r.from != null && it.seq < r.from) return;
        if (r.to != null && it.seq > r.to) return;
        if (it.owner === r.owner) return;
        edit(i, { receipt: r, receipts: [...(it.receipts || []), r] });
      });
    }

    const tpl = sentences[kind] || FEED_EXTRA[kind];
    if (tpl) {
      const vals = valuesFor(s, ev, ctx);
      const human = ctx.human;
      const line = {
        seq: ctx.seq, kind, by: ev.by, byKind: ev.by_kind, owner: ctx.owner, cls: ctx.cls, via: ctx.cls === 'delegate' ? 'agent' : null,
        cause: ev.cause ?? null, text: fill(tpl, vals), receipt: null, receipts: [],
        status: human && CONTROL_KINDS.has(kind) ? (ctx.pending ? 'pending' : 'queued') : null,
        appliedAt: null, pickRound: null, reason: null, node: d.node || subjectId(ev) || null, subject: ev.subject || null,
        question: d.question || null, round: ev.round ?? null, stage: ev.stage ?? null, op: ev.op || null, label: vals.label,
      };
      if (!copied) { feed = feed.slice(); copied = true; }
      if (ctx.pending) feed.push(line);
      else {                                          // numbered lines stay in seq order before any pending line
        let i = feed.length;
        while (i > 0 && feed[i - 1].seq == null) i--;
        feed.splice(i, 0, line);
      }
    }
    if (copied) s.feed = feed;
  }

  function valuesFor(s, ev, ctx) {
    const d = ev.data || {};
    const kind = ev.kind;
    const vals = {};
    for (const [k, v] of Object.entries(d)) if (v == null || typeof v !== 'object') vals[k] = v;
    if (ctx.human) for (const k of ['text', 'frame', 'fact', 'reason', 'note']) if (typeof d[k] === 'string') vals[k] = q(d[k]);
    const clusterName = (key) => (key && s.clusters.get(key) ? s.clusters.get(key).name : null);
    let label = ev.label || null;
    if (!label) {
      switch (kind) {
        case 'node_added': label = d.name || d.id; break;
        case 'node_edited': case 'node_skipped': case 'node_unskipped':
        case 'claim_granted': case 'claim_released': case 'claim_expired': case 'claim_taken_over':
          label = nodeName(s, subjectId(ev) || d.node); break;
        case 'sketch_batch': case 'cluster_snapshot': case 'memory_added': case 'seed_added': case 'fact_disputed':
          label = nodeName(s, d.node || subjectId(ev)); break;
        case 'objection_raised': case 'reply_posted': case 'objection_marked':
          label = clusterName(clusterKeyFor(s, d.node, d.idea, d.members)) || d.idea; break;
        case 'candidate_built': label = d.cluster_name || clusterName(s.cands.get(d.cand)) || d.hypothesis || d.cand; break;
        case 'test_result': label = clusterName(s.cands.get(d.cand)) || (s.results.find((r) => r.cand === d.cand) || {}).name || d.cand; break;
        case 'question_picked': label = ((d.top3 || []).find((t) => t.id === d.chosen) || {}).text || d.chosen; break;
        case 'question_vetoed': case 'question_unvetoed': case 'question_chosen': {
          const pv = s.questions.preview && s.questions.preview.top3.find((t) => t.id === d.question);
          label = d.text || (pv && pv.text) || d.question; break;
        }
        case 'opinion_given': label = d.target; break;
        case 'vote_cast': label = clusterName(clusterKeyFor(s, d.node, d.idea, null)) || d.idea; break;
        default: label = null;
      }
    }
    vals.label = ctx.human && label != null ? q(label, 80) : label;
    if ('parent' in d) vals.parent = nodeName(s, d.parent);
    if ('node' in d) vals.node = nodeName(s, d.node);
    if (kind === 'cluster_snapshot') vals.n = (d.clusters || []).length;
    if (kind === 'memory_added') vals.n_added = (d.added || []).length;
    if (kind === 'test_result') vals.metric = metricText(d);
    if (kind === 'claim_granted') vals.why = d.purpose ? `: ${d.purpose}` : '';
    if (kind === 'stage_entered') vals.reached = d.waiting ? 'waits for Go at' : 'reached';
    if (kind === 'control_applied') vals.n_refs = (d.refs || []).length;
    if (kind === 'digest_taken') vals.agent = ev.by;
    if (vals.round == null && ev.round != null) vals.round = ev.round;
    if (vals.stage == null && ev.stage != null) vals.stage = ev.stage;
    return vals;
  }

  // ---- layout: the tree after a node arrives; one island after its cluster_snapshot (section 6.5)
  function relayout(s, ctx) {
    if (!ctx.tree && !ctx.islands.size) return;
    const layout = { ...s.layout };
    if (ctx.tree) {
      const firstSeen = new Map([...s.nodes].map(([id, n]) => [id, n.firstSeen]));
      layout.tree = L.layoutTree(s.nodes, firstSeen);
    }
    if (ctx.islands.size) {
      const firstOf = (id) => (s.nodes.get(id) ? s.nodes.get(id).firstSeen : Infinity);
      let islands = s.islands;
      const added = [...ctx.islands].filter((id) => !islands.includes(id));
      if (added.length) {
        const seenAt = new Map(islands.map((id, i) => [id, i]));
        islands = [...islands, ...added].sort((a, b) => (firstOf(a) - firstOf(b)) ||
          ((seenAt.has(a) ? seenAt.get(a) : 1e9) - (seenAt.has(b) ? seenAt.get(b) : 1e9)) || (a < b ? -1 : a > b ? 1 : 0));
        s.islands = islands;
      }
      const anchors = new Map(islands.map((id, i) => [id, L.anchorFor(i, islands.length)]));
      let clusters = new Map(layout.clusters);
      // an island whose anchor moved (a new island joined the grid) is carried along by the same offset
      for (const [id, a] of anchors) {
        const old = layout.anchors.get(id);
        if (!old || (old.x === a.x && old.y === a.y) || ctx.islands.has(id)) continue;
        const dx = a.x - old.x, dy = a.y - old.y;
        for (const [key, p] of clusters) {
          const c = s.clusters.get(key);
          if (c && c.node === id) clusters.set(key, { ...p, x: round2(p.x + dx), y: round2(p.y + dy) });
        }
      }
      for (const id of ctx.islands) {
        const prevIsland = new Map();
        for (const [key, p] of layout.clusters) {
          const c = s.clusters.get(key) || s.retired.get(key);
          if (c && c.node === id) prevIsland.set(key, p);
        }
        const island = [...s.clusters.values()].filter((c) => c.node === id)
          .sort((a, b) => (a.direction < b.direction ? -1 : a.direction > b.direction ? 1 : 0) || a.index - b.index);
        const placed = L.layoutClusters(prevIsland, island, anchors.get(id), ctx.born || {});
        for (const key of prevIsland.keys()) clusters.delete(key);
        for (const [key, p] of placed) clusters.set(key, p);
      }
      layout.clusters = clusters;
      layout.anchors = anchors;
    }
    layout.hash = hashLayout(layout);
    s.layout = layout;
  }

  return { init, reduce, winnerWord: (mode) => winnerWord[mode] || 'won', stages };
}

// The view state's hash for the replay test (section 12.4): FNV-1a over the JSON of nodes, clusters, chains,
// results and questions, Maps sorted by key.
export function hashState(state) {
  const sortMap = (m) => [...m].sort(byFirst);
  const qs = state.questions;
  return fnv1a(JSON.stringify([sortMap(state.nodes), sortMap(state.clusters), sortMap(state.chains), state.results,
    { preview: qs.preview, picked: qs.picked, vetoes: sortMap(qs.vetoes), chosen: qs.chosen }]));
}
