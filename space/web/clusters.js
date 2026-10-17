// space/web/clusters.js: the animated idea clusters (docs/MULTIPLAYER_DESIGN.md section 10.2).
// mountClusters(el, store, bus, opts) -> {update, fit, setColorBy, bubbles, islands, el, destroy}
//   store: makeStore (note 02 A.4): store.view() is the view state of section 6.4
//   bus:   {on(name, fn), emit(name, payload)}; events hover, select, follow, fit
//   opts:  {me, contract}; the winner badge word is contract.winner_word[run.mode] (contract.json), never a
//          word written here. Without opts.contract the browser fetches ./contract.json once.
// Bubbles sit at the layout targets of section 6.5 (state.layout.clusters) and the shared clock glides the
// drawn values toward them; nothing here moves a target. Sunflower dots in arrival order never move.
// `obvious` and `obvious_match` never reach this module: the view state has no such keys.
import { requireD3, layoutClusters, anchorFor, sunflower, clusterRadius, islandsOf, SPACING, DOT_R } from './layout.mjs';
import { hueOf } from './cardstate.mjs';
import { clock, glide, T, animateOnce, later } from './motion.mjs';

const SVG = 'http://www.w3.org/2000/svg';
export const TOP_LABELS = 5;            // labels on the top 5 by n per island, the others on hover
export const TAIL_ZOOM = 1.6;           // the long-tail ring opens at this zoom
export const ISLAND_R = 190;            // the soft island disc
export const COLOR_BY = ['owner', 'part', 'prior', 'card', 'status'];
const WINNER_STATUSES = new Set(['win', 'preferred']);
const DIM_HOLD = 1500;

function h(tag, cls, parent) {
  const el = document.createElementNS(SVG, tag);
  if (cls) el.setAttribute('class', cls);
  if (parent) parent.appendChild(el);
  return el;
}
function hh(tag, cls, parent) {
  const el = document.createElement(tag);
  if (cls) el.setAttribute('class', cls);
  if (parent) parent.appendChild(el);
  return el;
}
function queryMe() {
  try {
    if (typeof location === 'undefined' || !location.search) return null;
    const m = /[?&]me=([^&]+)/.exec(location.search);
    return m ? decodeURIComponent(m[1]) : null;
  } catch { return null; }
}

export function dominantOwner(contributors) {
  let best = null, bestN = -1;
  for (const [owner, n] of Object.entries(contributors || {})) if (n > bestN || (n === bestN && owner < best)) { best = owner; bestN = n; }
  return best;
}

export function mountClusters(el, store, bus, opts = {}) {
  const d3 = requireD3();
  if (!el || typeof document === 'undefined') throw new Error('mountClusters needs a DOM element');
  const me = opts.me || (store && store.me) || queryMe();
  const emit = (name, payload) => { if (bus && typeof bus.emit === 'function') bus.emit(name, payload); };
  const on = (name, fn) => { if (bus && typeof bus.on === 'function') bus.on(name, fn); };
  let winnerWord = opts.contract && opts.contract.winner_word ? opts.contract.winner_word : null;
  if (!winnerWord && typeof fetch === 'function' && typeof window !== 'undefined') {
    fetch('contract.json').then((r) => r.json()).then((c) => { winnerWord = c.winner_word || null; update(true); }).catch(() => {});
  }

  // --- DOM skeleton ---
  el.classList.add('clusters');
  const svg = h('svg', 'clusters__svg', el);
  svg.setAttribute('width', '100%'); svg.setAttribute('height', '100%');
  svg.setAttribute('tabindex', '0');
  const defs = h('defs', null, svg);
  const grad = h('radialGradient', null, defs);
  grad.setAttribute('id', 'island-glow');
  const s0 = h('stop', 'island-glow__in', grad); s0.setAttribute('offset', '0');
  const s1 = h('stop', 'island-glow__out', grad); s1.setAttribute('offset', '1');
  const world = h('g', 'clusters__world', svg);
  const islandsG = h('g', 'clusters__islands', world);
  const bubblesG = h('g', 'clusters__bubbles', world);
  const fxG = h('g', 'clusters__fx', world);
  const hud = hh('div', 'clusters__hud', el);
  const empty = hh('div', 'clusters__empty', hud);
  empty.textContent = 'No ideas yet. Islands form at clustered, round 1.';
  const colorWrap = hh('label', 'clusters__colorby', hud);
  const colorLabel = hh('span', null, colorWrap);
  colorLabel.textContent = 'colour by';
  const colorSel = hh('select', null, colorWrap);
  for (const c of COLOR_BY) { const o = hh('option', null, colorSel); o.setAttribute('value', c); o.textContent = c; }
  colorSel.addEventListener('change', () => setColorBy(colorSel.value));

  // --- state ---
  const bubbles = new Map();        // key -> bubble record
  const islands = new Map();        // part -> {part, index, anchor, el, label, tail, tailText, tailOpen, count, dimUntil}
  let lastState = null, hoverKey = null, linkedNode = null, selectedKey = null, follow = null, followLast = null;
  let colorBy = 'owner', fitted = false, destroyed = false, winnerSeen = new Map();
  let transform = { x: 0, y: 0, k: 1 };
  let zoom = null;

  // --- camera ---
  const applyTransform = (t) => {
    const was = transform.k;
    transform = { x: t.x, y: t.y, k: t.k };
    world.setAttribute('transform', `translate(${t.x},${t.y}) scale(${t.k})`);
    if ((was < TAIL_ZOOM) !== (t.k < TAIL_ZOOM)) paintLod();
  };
  try {
    zoom = d3.zoom().scaleExtent([0.2, 4]).on('zoom', (e) => { applyTransform(e.transform); if (e.sourceEvent) stopFollow(); });
    d3.select(svg).call(zoom).on('dblclick.zoom', null);
  } catch { zoom = null; }
  function viewSize() {
    try { const r = svg.getBoundingClientRect(); return { w: r.width || 0, h: r.height || 0 }; } catch { return { w: 0, h: 0 }; }
  }
  function moveCamera(tx, ty, k, animate) {
    const t = d3.zoomIdentity.translate(tx, ty).scale(k);
    if (!zoom) { applyTransform(t); return; }
    try {
      if (animate && !clock.reduced.value) d3.select(svg).transition().duration(T.camera).call(zoom.transform, t);
      else d3.select(svg).call(zoom.transform, t);
    } catch { applyTransform(t); }
  }
  function fit(part, animate = true) {
    const { w, h: vh } = viewSize();
    if (!w || !vh) return false;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    const list = part != null ? [...bubbles.values()].filter((b) => b.node === part) : [...bubbles.values()];
    for (const b of list) { x0 = Math.min(x0, b.tx - b.tr); y0 = Math.min(y0, b.ty - b.tr); x1 = Math.max(x1, b.tx + b.tr); y1 = Math.max(y1, b.ty + b.tr); }
    if (!list.length) {
      for (const is of islands.values()) { x0 = Math.min(x0, is.anchor.x - ISLAND_R); y0 = Math.min(y0, is.anchor.y - ISLAND_R); x1 = Math.max(x1, is.anchor.x + ISLAND_R); y1 = Math.max(y1, is.anchor.y + ISLAND_R); }
    }
    if (!Number.isFinite(x0)) return false;
    const pad = 48;
    const k = Math.max(0.2, Math.min(1.5, (w - 2 * pad) / Math.max(1, x1 - x0), (vh - 2 * pad) / Math.max(1, y1 - y0)));
    moveCamera(w / 2 - k * (x0 + x1) / 2, vh / 2 - k * (y0 + y1) / 2, k, animate);
    return true;
  }
  function centerOn(key, animate = true) {
    const b = bubbles.get(key);
    const { w, h: vh } = viewSize();
    if (!b || !w || !vh) return;
    const k = Math.max(transform.k, 1);
    moveCamera(w / 2 - k * b.tx, vh / 2 - k * b.ty, k, animate);
  }
  function stopFollow() { if (follow) { follow = null; followLast = null; emit('follow', null); } }

  // --- islands ---
  function island(part, index, anchor, name) {
    let is = islands.get(part);
    if (!is) {
      const g = h('g', 'island', islandsG);
      const disc = h('circle', 'island__disc', g);
      disc.setAttribute('r', String(ISLAND_R));
      disc.setAttribute('fill', 'url(#island-glow)');
      const label = h('text', 'island__label', g);
      label.setAttribute('text-anchor', 'middle');
      const tail = h('g', 'island__tail', g);
      const tailRing = h('circle', 'island__tail-ring', tail);
      tailRing.setAttribute('r', '16');
      const tailText = h('text', 'island__tail-text', tail);
      tailText.setAttribute('text-anchor', 'middle'); tailText.setAttribute('dy', '0.35em');
      tail.addEventListener('click', () => { is.tailOpen = !is.tailOpen; paintLod(); });
      is = { part, index, anchor, el: g, label, tail, tailText, tailOpen: false, count: 0, dimUntil: 0 };
      islands.set(part, is);
    }
    is.index = index; is.anchor = anchor;
    is.el.setAttribute('transform', `translate(${anchor.x},${anchor.y})`);
    is.el.style.setProperty('--part-mix', `${30 + ((index * 23) % 60)}%`);
    is.label.setAttribute('y', String(-ISLAND_R + 14));
    is.label.textContent = name || part;
    is.tail.setAttribute('transform', `translate(${ISLAND_R * 0.72},${ISLAND_R * 0.72})`);
    return is;
  }

  // --- bubbles ---
  function makeBubble(key) {
    const g = h('g', 'bubble', bubblesG);
    g.setAttribute('data-key', key);
    const halo = h('circle', 'bubble__halo', g);
    const body = h('circle', 'bubble__body', g);
    const rim = h('g', 'bubble__rim', g);
    const dots = h('g', 'bubble__dots', g);
    const ring = h('circle', 'bubble__ring', g);
    const votes = h('g', 'bubble__votes', g);
    const label = h('text', 'bubble__label', g);
    label.setAttribute('text-anchor', 'middle');
    const badge = h('g', 'bubble__badge', g);
    const badgeBg = h('rect', 'bubble__badge-bg', badge);
    badgeBg.setAttribute('rx', '7'); badgeBg.setAttribute('height', '14');
    const badgeText = h('text', 'bubble__badge-text', badge);
    badgeText.setAttribute('text-anchor', 'middle'); badgeText.setAttribute('dy', '0.35em');
    const b = { key, node: null, x: 0, y: 0, vx: 0, vy: 0, r: 0, vr: 0, tx: 0, ty: 0, tr: 0, pending: null, el: g,
                parts: { halo, body, rim, dots, ring, votes, label, badge, badgeBg, badgeText }, dotCount: 0, rimKey: '', rimR: -1,
                voteKey: '', status: null, fresh: true, retiring: false, lod: true, top: false, n: 0, paintKey: '' };
    g.addEventListener('mouseenter', () => setHover(key, true));
    g.addEventListener('mouseleave', () => setHover(key, false));
    g.addEventListener('click', () => select(key));
    g.addEventListener('dblclick', () => { fit(b.node); emit('fit', { type: 'clusters', node: b.node }); });
    bubbles.set(key, b);
    return b;
  }

  function retire(b, into) {
    if (b.retiring) return;
    b.retiring = true;
    b.el.classList.add('is-retiring');
    const target = into ? bubbles.get(into) : null;
    if (target) { b.tx = target.x; b.ty = target.y; b.tr = Math.max(2, target.r * 0.3); b.pending = null; }   // a merge flies into the survivor
    later(() => { bubbles.delete(b.key); if (b.el.parentNode) b.el.parentNode.removeChild(b.el); }, T.relayoutFade);
  }

  function setHover(key, onIt) {
    hoverKey = onIt ? key : (hoverKey === key ? null : hoverKey);
    paintHover();
    const b = bubbles.get(key);
    emit('hover', onIt ? { type: 'cluster', key, node: b ? b.node : null, source: 'clusters' } : null);
  }
  function select(key) {
    selectedKey = key;
    for (const b of bubbles.values()) b.el.classList.toggle('is-selected-by-me', b.key === key);
    const b = bubbles.get(key);
    paintLod();
    emit('select', { type: 'cluster', key, node: b ? b.node : null });
  }
  function paintHover() {
    const active = hoverKey || (linkedNode ? 'node' : null);
    el.classList.toggle('has-hover', !!active);
    for (const b of bubbles.values()) {
      const hot = hoverKey ? b.key === hoverKey : (linkedNode ? b.node === linkedNode : false);
      b.el.classList.toggle('is-hot', hot);
      b.el.classList.toggle('is-cold', !!active && !hot);
      b.el.classList.toggle('is-labelled', b.top || hot || b.key === selectedKey);
    }
  }
  function paintLod() {
    const zoomedIn = transform.k >= TAIL_ZOOM;
    const tails = new Map();
    for (const b of bubbles.values()) {
      const is = islands.get(b.node);
      const open = zoomedIn || (is && is.tailOpen);
      const show = b.n >= 2 || b.selected || b.key === hoverKey || b.key === selectedKey || b.hasVotes || b.winner || open;
      b.lod = show;
      b.el.style.display = show ? '' : 'none';
      if (!show) tails.set(b.node, (tails.get(b.node) || 0) + 1);
    }
    for (const is of islands.values()) {
      const n = tails.get(is.part) || 0;
      is.count = n;
      is.tail.style.display = n ? '' : 'none';
      is.tailText.textContent = `+${n}`;
      is.tail.classList.toggle('is-open', !!is.tailOpen);
    }
  }

  // --- the per-frame glide ---
  function step(dt, { snap, now }) {
    let busy = false;
    for (const b of bubbles.values()) {
      if (b.pending) {
        if (snap || now >= b.pending.at) { b.tx = b.pending.x; b.ty = b.pending.y; b.tr = b.pending.r; b.pending = null; if (b.arriving) { b.arriving = false; b.el.classList.remove('is-arriving'); } }
        else busy = true;
      }
      const px = b.x, py = b.y, pr = b.r;
      if (glide(b, 'x', T.bubble, dt, snap)) busy = true;
      if (glide(b, 'y', T.bubble, dt, snap)) busy = true;
      if (glide(b, 'r', T.bubble, dt, snap)) busy = true;
      if (b.fresh || b.x !== px || b.y !== py) b.el.setAttribute('transform', `translate(${b.x},${b.y})`);
      if (b.fresh || b.r !== pr) paintRadius(b);
      b.fresh = false;
    }
    return busy;
  }
  const unstep = clock.add(step);

  function paintRadius(b) {
    const r = Math.max(0, b.r);
    const p = b.parts;
    p.body.setAttribute('r', String(r));
    p.halo.setAttribute('r', String(r + 10));
    p.ring.setAttribute('r', String(r + 5));
    p.label.setAttribute('y', String(r + 13));
    p.badge.setAttribute('transform', `translate(0,${-r - 12})`);
    if (Math.abs(b.rimR - r) > 0.25) { b.rimR = r; paintRim(b); paintVotes(b); }
  }

  function paintRim(b) {
    const p = b.parts;
    p.rim.textContent = '';
    const entries = Object.entries(b.contributors || {}).filter(([, n]) => n > 0).sort((a, c) => (a[0] < c[0] ? -1 : 1));
    if (!entries.length || b.r < 4) return;
    const arcs = d3.pie().value((d) => d[1]).sort(null)(entries);
    const arc = d3.arc().innerRadius(b.r - 1.2).outerRadius(b.r + 1.8);
    for (const a of arcs) {
      const path = h('path', `rim hue-${hueOf(a.data[0], lastState && lastState.people)}`, p.rim);
      path.setAttribute('d', arc(a));
    }
  }

  function paintVotes(b) {
    const p = b.parts;
    p.votes.textContent = '';
    const entries = Object.entries(b.votes || {}).sort((a, c) => (a[0] < c[0] ? -1 : 1));
    entries.forEach(([owner, v], i) => {
      const a = -Math.PI / 2 + i * (Math.PI / 4.5);
      const rr = b.r + 7;
      const dot = h('circle', `vote hue-${hueOf(owner, lastState && lastState.people)} ${v > 0 ? 'vote--up' : 'vote--down'}`, p.votes);
      dot.setAttribute('cx', String(rr * Math.cos(a))); dot.setAttribute('cy', String(rr * Math.sin(a))); dot.setAttribute('r', '3.5');
      const t = h('title', null, dot); t.textContent = `${owner} voted ${v > 0 ? 'up' : 'down'} (shown by name)`;
    });
  }

  function paintDots(b, members) {
    const p = b.parts;
    const n = members.length;
    if (n < b.dotCount) { p.dots.textContent = ''; b.dotCount = 0; }
    for (let k = b.dotCount; k < n; k++) {
      const s = sunflower(k, SPACING);
      const dot = h('circle', 'dot', p.dots);
      dot.setAttribute('cx', String(s.x.toFixed(2))); dot.setAttribute('cy', String(s.y.toFixed(2))); dot.setAttribute('r', String(DOT_R));
      dot.setAttribute('data-sketch', members[k]);
      if (!b.fresh) animateOnce(dot, [{ transform: 'scale(0)' }, { transform: 'scale(1)' }], { duration: T.relayoutGrow, easing: 'cubic-bezier(.2,.9,.3,1.15)' });
    }
    b.dotCount = n;
  }

  function winnerMoment(b, word) {
    const p = b.parts;
    if (b.el.parentNode) b.el.parentNode.appendChild(b.el);                         // raise
    b.el.classList.add('is-winner');
    const ripple = h('circle', 'ripple', fxG);
    ripple.setAttribute('cx', String(b.x)); ripple.setAttribute('cy', String(b.y)); ripple.setAttribute('r', String(b.tr + 4));
    animateOnce(ripple, [{ transform: 'scale(1)', opacity: 0.6 }, { transform: 'scale(1.7)', opacity: 0 }], { duration: T.ripple, easing: 'ease-out' });
    later(() => { if (ripple.parentNode) ripple.parentNode.removeChild(ripple); }, T.ripple);
    p.badgeText.textContent = word;
    p.badge.style.display = '';
    const w = Math.max(28, 8 + 6.5 * word.length);
    p.badgeBg.setAttribute('width', String(w)); p.badgeBg.setAttribute('x', String(-w / 2)); p.badgeBg.setAttribute('y', '-7');
    const is = islands.get(b.node);
    for (const o of bubbles.values()) if (o !== b && o.node === b.node) { o.el.classList.add('is-dim'); o.el.classList.remove('is-dim-soft'); }
    if (is) is.dimUntil = (typeof performance !== 'undefined' ? performance.now() : Date.now()) + DIM_HOLD;
    later(() => { for (const o of bubbles.values()) if (o !== b && o.node === b.node && o.el.classList.contains('is-dim')) { o.el.classList.remove('is-dim'); o.el.classList.add('is-dim-soft'); } }, DIM_HOLD);
  }

  // --- update from the store ---
  function update(force) {
    if (destroyed || !store || typeof store.view !== 'function') return;
    const state = store.view();
    if (!state || !(state.clusters instanceof Map)) return;
    if (!force && state === lastState) return;
    lastState = state;
    const nodes = state.nodes instanceof Map ? state.nodes : new Map();
    const layout = state.layout || {};
    const anchors = layout.anchors instanceof Map ? layout.anchors : new Map();
    const positions = layout.clusters instanceof Map ? layout.clusters : new Map();
    const now = typeof performance !== 'undefined' ? performance.now() : Date.now();
    const mode = state.run && state.run.mode;
    const word = winnerWord && mode && winnerWord[mode] ? winnerWord[mode] : null;

    // islands in first-seen part order
    const partOrder = [...anchors.keys()];
    const grouped = islandsOf([...state.clusters.values()].filter((c) => !c.mergedInto), partOrder);
    const seenParts = new Set();
    for (const g of grouped) {
      const anchor = anchors.get(g.part) || anchorFor(g.index, grouped.length);
      const nn = nodes.get(g.part);
      island(g.part, g.index, anchor, nn ? nn.name : g.part);
      seenParts.add(g.part);
    }
    for (const [part, is] of islands) if (!seenParts.has(part)) { if (is.el.parentNode) is.el.parentNode.removeChild(is.el); islands.delete(part); }

    // bubbles: targets from the layout, local settle only when the reducer gave none
    const seen = new Set();
    for (const g of grouped) {
      const is = islands.get(g.part);
      let local = null;
      const missing = g.clusters.some((c) => !positions.has(c.key));
      if (missing) {
        const prev = new Map();
        for (const c of g.clusters) { const b = bubbles.get(c.key); if (b && !b.retiring) prev.set(c.key, { x: b.tx, y: b.ty, r: b.tr }); }
        const born = new Map();
        for (const c of g.clusters) if (c.bornFrom) born.set(c.key, c.bornFrom);
        local = layoutClusters(prev, g.clusters, is.anchor, born);
      }
      const byN = [...g.clusters].sort((a, c) => (c.n - a.n) || (a.key < c.key ? -1 : 1)).slice(0, TOP_LABELS).map((c) => c.key);
      const existing = g.clusters.filter((c) => { const b = bubbles.get(c.key); return b && !b.retiring; });
      const moves = existing.some((c) => { const b = bubbles.get(c.key); const p = positions.get(c.key) || (local && local.get(c.key)); return !p || b.tx !== p.x || b.ty !== p.y || b.tr !== p.r; });
      const changed = moves || existing.length !== g.clusters.length;
      if (changed && is.dimUntil && now > is.dimUntil) {                       // the dim after a winner moment ends with the next snapshot
        is.dimUntil = 0;
        for (const o of bubbles.values()) if (o.node === g.part) o.el.classList.remove('is-dim-soft');
      }
      for (const c of g.clusters) {
        seen.add(c.key);
        const pos = positions.get(c.key) || (local && local.get(c.key)) || { x: is.anchor.x, y: is.anchor.y, r: clusterRadius(c.n || 1) };
        let b = bubbles.get(c.key);
        let isNew = false;
        if (!b || b.retiring) {
          if (b) { bubbles.delete(c.key); if (b.el.parentNode) b.el.parentNode.removeChild(b.el); }
          b = makeBubble(c.key);
          isNew = true;
          const from = c.bornFrom ? bubbles.get(c.bornFrom) : null;
          b.x = from ? from.x : is.anchor.x; b.y = from ? from.y : is.anchor.y; b.r = 0;
          b.tx = b.x; b.ty = b.y; b.tr = 0;
          b.el.setAttribute('transform', `translate(${b.x},${b.y})`);
          b.el.classList.add('is-arriving'); b.arriving = true;
        }
        b.node = g.part; b.n = c.n || 0; b.selected = !!c.selected; b.contributors = c.contributors || {}; b.votes = c.votes || {};
        b.hasVotes = Object.keys(b.votes).length > 0;
        b.top = byN.includes(c.key);
        // staged relayout: leaving fade 200 ms, moves after it, arrivals grow after the moves.
        // A fresh island (no bubble yet) paints at once.
        const delay = clock.reduced.value || existing.length === 0 ? 0
          : isNew ? (moves ? T.relayoutFade + T.relayoutMove : T.relayoutFade) : T.relayoutFade;
        if (b.tx !== pos.x || b.ty !== pos.y || b.tr !== pos.r) {
          if (delay > 0) b.pending = { x: pos.x, y: pos.y, r: pos.r, at: now + delay };
          else { b.tx = pos.x; b.ty = pos.y; b.tr = pos.r; b.pending = null; }
        }
        if (delay === 0 && b.arriving) { b.arriving = false; b.el.classList.remove('is-arriving'); }
        paintBubble(b, c, state, word);
      }
    }
    for (const b of bubbles.values()) if (!seen.has(b.key) && !b.retiring) {
      const c = state.clusters.get(b.key) || (state.retired instanceof Map ? state.retired.get(b.key) : null);
      retire(b, c && c.mergedInto ? c.mergedInto : null);
    }
    hud.classList.toggle('is-empty', state.clusters.size === 0);
    paintLod();
    paintHover();
    if (!fitted && (bubbles.size || islands.size)) fitted = fit(null, false);   // the first paint fits once the pane has a size
    if (follow) followStep(state);
    clock.kick();
  }

  function paintBubble(b, c, state, word) {
    const p = b.parts;
    const owner = dominantOwner(c.contributors);
    const hue = hueOf(owner, state.people);
    const status = c.status || 'open';
    const winner = WINNER_STATUSES.has(status);
    const classes = ['bubble', `prior-${c.prior || 'unknown'}`, `status-${status}`, `hue-${hue}`, `lane-${c.lane || 'team'}`, `card-${c.card || (Array.isArray(c.cards) && c.cards[0]) || 'none'}`];
    if (c.selected) classes.push('is-selected');
    if (winner) classes.push('is-winner');
    if (b.arriving) classes.push('is-arriving');
    if (b.el.classList.contains('is-dim')) classes.push('is-dim');
    if (b.el.classList.contains('is-dim-soft')) classes.push('is-dim-soft');
    if (b.key === selectedKey) classes.push('is-selected-by-me');
    const key = classes.join(' ') + '|' + c.name + '|' + (c.members ? c.members.length : 0) + '|' + JSON.stringify(c.contributors || null) + '|' + JSON.stringify(c.votes || null) + '|' + word;
    b.winner = winner;
    if (key === b.paintKey) return;
    b.paintKey = key;
    b.el.setAttribute('class', classes.join(' '));
    const is = islands.get(b.node);
    if (is) b.el.style.setProperty('--part-mix', `${30 + ((is.index * 23) % 60)}%`);
    p.label.textContent = c.name || b.key;
    const title = p.body.querySelector ? p.body.querySelector('title') : null;
    const t = title || h('title', null, p.body);
    t.textContent = `${c.name || b.key}: ${c.n || 0} ideas, ${c.prior || 'unknown'} prior, ${status}`;
    paintDots(b, Array.isArray(c.members) ? c.members : []);
    const rimKey = JSON.stringify(c.contributors || null);
    if (rimKey !== b.rimKey) { b.rimKey = rimKey; paintRim(b); }
    const voteKey = JSON.stringify(c.votes || null);
    if (voteKey !== b.voteKey) { b.voteKey = voteKey; paintVotes(b); }
    if (winner && word && winnerSeen.get(b.key) !== status) { winnerSeen.set(b.key, status); winnerMoment(b, word); }
    else if (!winner) { p.badge.style.display = 'none'; winnerSeen.delete(b.key); }
    else if (winner && word) { p.badgeText.textContent = word; p.badge.style.display = ''; }
    b.status = status;
  }

  function followStep(state) {
    const clients = state.presence && Array.isArray(state.presence.clients) ? state.presence.clients : [];
    const cl = clients.find((x) => x && (x.name === follow || x.owner === follow || x.client === follow));
    if (cl) followTo(cl.focus);
  }
  function followTo(f) {
    if (!f || f.type !== 'cluster') return;
    if (followLast === f.id) return;
    followLast = f.id;
    centerOn(f.id, true);
  }

  function setColorBy(mode) {
    if (!COLOR_BY.includes(mode)) return;
    colorBy = mode;
    for (const m of COLOR_BY) el.classList.toggle(`color-by-${m}`, m === mode);
    if (colorSel.value !== mode) colorSel.value = mode;
  }
  setColorBy(colorBy);

  // --- bus ---
  on('hover', (e) => { if (e && e.source === 'clusters') return; linkedNode = e && e.type === 'node' ? e.id : null; paintHover(); });
  on('fit', (e) => { if (!e || e.type === 'clusters') fit(e && e.node != null ? e.node : null); });
  on('follow', (e) => {
    const who = e && (e.who || e.person || e.name || e.owner);
    if (!who) { follow = null; followLast = null; return; }
    if (who !== follow) { follow = who; followLast = null; }
    if (e.focus) followTo(e.focus);                      // the page shell sends {who, focus}
    else if (lastState) followStep(lastState);
  });
  on('state', () => update());
  on('select', (e) => { if (e && e.type === 'cluster' && e.source !== 'clusters' && e.key !== selectedKey) { selectedKey = e.key; paintLod(); } });
  svg.addEventListener('keydown', (e) => { if (e && (e.key === 'f' || e.key === 'F')) { fit(null); if (e.preventDefault) e.preventDefault(); } });
  if (typeof store.subscribe === 'function') store.subscribe(() => update());

  const handle = {
    el, bubbles, islands, update, fit, centerOn, select, setColorBy,
    get colorBy() { return colorBy; },
    get follow() { return follow; }, set follow(v) { follow = v || null; followLast = null; },
    destroy() { destroyed = true; unstep(); if (el.contains && el.contains(svg)) el.removeChild(svg); },
  };
  update(true);
  return handle;
}
