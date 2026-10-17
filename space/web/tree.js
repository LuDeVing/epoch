// space/web/tree.js: the animated problem tree (docs/MULTIPLAYER_DESIGN.md section 10.1).
// mountTree(el, store, bus, opts) -> {update, fit, open, destroy, cards, el}
//   store: makeStore (note 02 A.4): store.view() is the view state of section 6.4, store.last() the head seq
//   bus:   {on(name, fn), emit(name, payload)}; events hover, select, follow, fit
//   opts:  {me, contract, lastSeenSeq()}; `me` falls back to ?me= in the page URL
// The host calls handle.update() once per animation frame after it applied events (or emits bus 'state').
// HTML cards over SVG edges, one CSS transform on the world div, d3.zoom for the camera, the shared clock for
// motion. Every DOM call is guarded so the module imports (and mounts against a small stub) under Node.
import { requireD3, layoutTree, nestTree } from './layout.mjs';
import { cardState, hueOf } from './cardstate.mjs';
import { clock, glide, T, animateOnce, later } from './motion.mjs';

export const CARD_W = 210;
export const CARD_H = 48;
export const DEEP_W = 190;            // a card deeper than OPEN_DEPTH (views.css .card--deep)
export const DEEP_H = 40;
export const OPEN_DEPTH = 3;          // root, parts, sub-parts are open; deeper levels fold into a count chip
export const HALO_BURST = 3;          // in a burst only the latest three changes get a halo

const SVG = 'http://www.w3.org/2000/svg';
const GLYPH = { map: 'map', human: 'person', failure: 'flask', offtree: 'trophy' };

// Inline icon symbols (no icon font: the page loads nothing but vendor/ files). Ids never look like hex.
const ICON_PATHS = {
  clock: 'M12 7v5l3 2M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z',
  check: 'M5 12l4 4L19 6',
  x: 'M6 6l12 12M18 6L6 18',
  flask: 'M9 3h6M10 3v6L4 20h16l-6-11V3',
  trophy: 'M7 4h10v5a5 5 0 0 1-10 0V4zM7 6H4v2a3 3 0 0 0 3 3M17 6h3v2a3 3 0 0 1-3 3M12 14v4M8 20h8',
  flag: 'M5 21V4h12l-2 4 2 4H5',
  pause: 'M8 5v14M16 5v14',
  'arrow-down': 'M12 4v16m-6-6l6 6 6-6',
  lock: 'M6 11h12v10H6zM8 11V7a4 4 0 0 1 8 0v4',
  dot: 'M12 12m-3 0a3 3 0 1 0 6 0a3 3 0 1 0-6 0',
  map: 'M4 5h16v14H4zM4 12h16M12 5v14',
  person: 'M12 12a4 4 0 1 0 0-8 4 4 0 0 0 0 8zM4 21a8 8 0 0 1 16 0',
  fold: 'M6 9l6 6 6-6',
};

function h(tag, cls, parent, ns) {
  const el = ns ? document.createElementNS(ns, tag) : document.createElement(tag);
  if (cls) el.setAttribute('class', cls);
  if (parent) parent.appendChild(el);
  return el;
}

function iconSymbols() {
  const svg = h('svg', 'tree__icons', null, SVG);
  svg.setAttribute('aria-hidden', 'true');
  svg.setAttribute('width', '0'); svg.setAttribute('height', '0');
  for (const [name, d] of Object.entries(ICON_PATHS)) {
    const sym = h('symbol', null, svg, SVG);
    sym.setAttribute('id', `ico-${name}`); sym.setAttribute('viewBox', '0 0 24 24');
    const p = h('path', null, sym, SVG);
    p.setAttribute('d', d); p.setAttribute('fill', 'none'); p.setAttribute('stroke', 'currentColor');
    p.setAttribute('stroke-width', '2'); p.setAttribute('stroke-linecap', 'round'); p.setAttribute('stroke-linejoin', 'round');
  }
  return svg;
}

function icon(name, cls) {
  const svg = h('svg', cls || 'ico', null, SVG);
  svg.setAttribute('width', '12'); svg.setAttribute('height', '12'); svg.setAttribute('aria-hidden', 'true');
  const use = h('use', null, svg, SVG);
  use.setAttribute('href', `#ico-${name}`);
  return svg;
}

function queryMe() {
  try {
    if (typeof location === 'undefined' || !location.search) return null;
    const m = /[?&]me=([^&]+)/.exec(location.search);
    return m ? decodeURIComponent(m[1]) : null;
  } catch { return null; }
}

function sameState(a, b) { return a === b; }

// The drawn box of a card: deep cards are smaller (views.css), so edges and the camera use this, never CARD_W alone.
const cardW = (c) => (c.depth >= OPEN_DEPTH ? DEEP_W : CARD_W);
const cardH = (c) => (c.depth >= OPEN_DEPTH ? DEEP_H : CARD_H);

export function mountTree(el, store, bus, opts = {}) {
  const d3 = requireD3();
  if (!el || typeof document === 'undefined') throw new Error('mountTree needs a DOM element');
  const me = opts.me || (store && store.me) || queryMe();
  const emit = (name, payload) => { if (bus && typeof bus.emit === 'function') bus.emit(name, payload); };
  const on = (name, fn) => { if (bus && typeof bus.on === 'function') bus.on(name, fn); };

  // --- DOM skeleton ---
  el.classList.add('tree');
  el.appendChild(iconSymbols());
  const viewport = h('div', 'tree__viewport', el);
  viewport.setAttribute('tabindex', '0');
  viewport.setAttribute('role', 'tree');
  const world = h('div', 'tree__world', viewport);
  const edgesSvg = h('svg', 'tree__edges', world, SVG);
  edgesSvg.setAttribute('width', '1'); edgesSvg.setAttribute('height', '1');
  const edgesG = h('g', null, edgesSvg, SVG);
  const cardsDiv = h('div', 'tree__cards', world);
  const hud = h('div', 'tree__hud', el);
  const empty = h('div', 'tree__empty', hud);
  empty.textContent = 'No parts yet. The map appears at planned, round 1.';

  // --- state ---
  const cards = new Map();           // id -> {id, x, y, vx, vy, tx, ty, el, edge, parent, depth, state, fresh}
  const opened = new Set();          // nodes whose deep children are open
  const haloSeen = new Map();        // id -> halo seq already shown
  let lastState = null, index = new Map(), hoverId = null, linkedId = null, selectedId = null, focusId = null;
  let follow = null, followLast = null, fitted = false, lastSeenSeq = null, lastHeadSeen = 0, destroyed = false;
  let transform = { x: 0, y: 0, k: 1 };
  let zoom = null;
  let claimTimer = 0;

  // --- camera ---
  const applyTransform = (t) => {
    transform = { x: t.x, y: t.y, k: t.k };
    world.style.transform = `translate(${t.x}px, ${t.y}px) scale(${t.k})`;
  };
  try {
    zoom = d3.zoom().scaleExtent([0.25, 2.5]).on('zoom', (e) => { applyTransform(e.transform); if (e.sourceEvent) stopFollow(); });
    d3.select(viewport).call(zoom).on('dblclick.zoom', null);
  } catch { zoom = null; }

  function viewSize() {
    try { const r = viewport.getBoundingClientRect(); return { w: r.width || 0, h: r.height || 0 }; } catch { return { w: 0, h: 0 }; }
  }

  function fit(ids, animate = true) {
    const list = (ids || [...cards.keys()]).map((id) => cards.get(id)).filter((c) => c && !c.retiring);
    const { w, h: vh } = viewSize();
    if (!list.length || !w || !vh) return false;
    let x0 = Infinity, y0 = Infinity, x1 = -Infinity, y1 = -Infinity;
    for (const c of list) { x0 = Math.min(x0, c.tx); y0 = Math.min(y0, c.ty); x1 = Math.max(x1, c.tx + cardW(c)); y1 = Math.max(y1, c.ty + cardH(c)); }
    const pad = 40;
    const k = Math.max(0.25, Math.min(1.25, (w - 2 * pad) / Math.max(1, x1 - x0), (vh - 2 * pad) / Math.max(1, y1 - y0)));
    const tx = w / 2 - k * (x0 + x1) / 2, ty = vh / 2 - k * (y0 + y1) / 2;
    moveCamera(tx, ty, k, animate);
    return true;
  }

  function centerOn(id, animate = true) {
    const c = cards.get(id);
    const { w, h: vh } = viewSize();
    if (!c || !w || !vh) return;
    const k = transform.k;
    moveCamera(w / 2 - k * (c.tx + cardW(c) / 2), vh / 2 - k * (c.ty + cardH(c) / 2), k, animate);
  }

  function moveCamera(tx, ty, k, animate) {
    const t = d3.zoomIdentity.translate(tx, ty).scale(k);
    if (!zoom) { applyTransform(t); return; }
    try {
      if (animate && !clock.reduced.value) d3.select(viewport).transition().duration(T.camera).call(zoom.transform, t);
      else d3.select(viewport).call(zoom.transform, t);
    } catch { applyTransform(t); }
  }

  function stopFollow() { if (follow) { follow = null; followLast = null; emit('follow', null); } }

  // --- cards ---
  function makeCard(id) {
    const card = h('div', 'card', cardsDiv);
    card.setAttribute('data-id', id);
    card.setAttribute('role', 'treeitem');
    h('div', 'card__stripe', card);
    const body = h('div', 'card__body', card);
    const head = h('div', 'card__head', body);
    const glyph = h('span', 'card__glyph', head);
    const name = h('span', 'card__name', head);
    const dot = h('span', 'card__dot', head);
    const row = h('div', 'card__row', body);
    const chips = h('span', 'card__chips', row);
    const counts = h('span', 'card__counts', row);
    const ring = h('div', 'card__ring', card);
    const tag = h('span', 'card__tag', ring);
    const fold = h('button', 'card__fold', card);
    fold.setAttribute('type', 'button');
    fold.setAttribute('title', 'open deeper levels');
    const edge = h('path', 'edge', edgesG, SVG);
    edge.setAttribute('data-to', id);
    const c = { id, x: 0, y: 0, vx: 0, vy: 0, tx: 0, ty: 0, el: card, edge, parent: null, depth: 0, fresh: true,
                retiring: false, parts: { glyph, name, dot, chips, counts, ring, tag, fold }, lastStatus: null, lastStateKey: '' };
    card.addEventListener('mouseenter', () => setHover(id, true));
    card.addEventListener('mouseleave', () => setHover(id, false));
    card.addEventListener('click', (e) => { if (e && e.target === fold) return; select(id); });
    card.addEventListener('dblclick', (e) => { if (e && e.preventDefault) e.preventDefault(); fitBranch(id); });
    fold.addEventListener('click', (e) => { if (e && e.stopPropagation) e.stopPropagation(); toggleOpen(id); });
    cards.set(id, c);
    return c;
  }

  function retire(c) {
    if (c.retiring) return;
    c.retiring = true;
    c.el.classList.add('is-retiring');
    c.edge.classList.add('is-retiring');
    later(() => {
      cards.delete(c.id);
      if (c.el.parentNode) c.el.parentNode.removeChild(c.el);
      if (c.edge.parentNode) c.edge.parentNode.removeChild(c.edge);
    }, T.exit);
  }

  function subtreeIds(id) {
    const out = [];
    const walk = (n) => { if (!cards.has(n) || !index.has(n)) return; out.push(n); for (const ch of index.get(n).children) walk(ch); };
    walk(id);
    return out;
  }

  function fitBranch(id) { fit(subtreeIds(id)); emit('fit', { type: 'tree', id }); }

  function toggleOpen(id) {
    if (opened.has(id)) opened.delete(id); else opened.add(id);
    update(true);
  }

  function openAncestors(id) {
    let changed = false;
    let cur = index.get(id);
    while (cur && cur.parent != null) {
      const p = index.get(cur.parent);
      if (p && p.depth >= OPEN_DEPTH - 1 && !opened.has(p.id)) { opened.add(p.id); changed = true; }
      cur = p;
    }
    return changed;
  }

  function select(id) {
    selectedId = id;
    lastSeenSeq = store && typeof store.last === 'function' ? store.last() : lastSeenSeq;
    for (const c of cards.values()) c.el.classList.toggle('is-selected', c.id === id);
    emit('select', { type: 'node', id });
  }

  function setHover(id, on) {
    hoverId = on ? id : (hoverId === id ? null : hoverId);
    paintHover();
    emit('hover', on ? { type: 'node', id, source: 'tree' } : null);
  }

  function pathToRoot(id) {
    const out = new Set();
    let cur = index.get(id);
    while (cur) { out.add(cur.id); cur = cur.parent != null ? index.get(cur.parent) : null; }
    return out;
  }

  function paintHover() {
    const active = hoverId || linkedId;
    world.classList.toggle('has-hover', !!active);
    const path = active ? pathToRoot(active) : null;
    for (const c of cards.values()) {
      const onPath = !!(path && path.has(c.id));
      c.el.classList.toggle('is-path', onPath);
      c.edge.classList.toggle('is-path', onPath && !!(path && c.parent != null && path.has(c.parent)));
      c.el.classList.toggle('is-linked', !!linkedId && c.id === linkedId);
    }
  }

  // --- the per-frame glide ---
  function step(dt, { snap }) {
    let busy = false;
    for (const c of cards.values()) {
      const px = c.x, py = c.y;
      if (glide(c, 'x', T.tree, dt, snap)) busy = true;
      if (glide(c, 'y', T.tree, dt, snap)) busy = true;
      if (c.fresh || c.x !== px || c.y !== py) {
        c.el.style.transform = `translate(${c.x}px, ${c.y}px)`;
        c.moved = true;
      }
    }
    for (const c of cards.values()) {
      const p = c.parent != null ? cards.get(c.parent) : null;
      if (!p) { if (c.fresh) c.edge.setAttribute('d', ''); continue; }
      if (!(c.moved || p.moved || c.fresh)) continue;
      const x1 = p.x + cardW(p), y1 = p.y + cardH(p) / 2, x2 = c.x, y2 = c.y + cardH(c) / 2, xm = (x1 + x2) / 2;
      c.edge.setAttribute('d', `M${x1},${y1} C${xm},${y1} ${xm},${y2} ${x2},${y2}`);
    }
    for (const c of cards.values()) { c.moved = false; c.fresh = false; }
    return busy;
  }
  const unstep = clock.add(step);

  // --- claim countdown (server time) ---
  function serverNow(state) {
    const off = state && Number.isFinite(state.serverOffsetMs) ? state.serverOffsetMs
      : state && state.net && Number.isFinite(state.net.offsetMs) ? state.net.offsetMs : 0;
    return Date.now() + off;
  }

  function paintClaims() {
    if (!lastState) return;
    const now = serverNow(lastState);
    let any = false;
    for (const c of cards.values()) {
      const n = lastState.nodes.get(c.id);
      if (!n || !n.claim) continue;
      any = true;
      const s = Math.max(0, Math.ceil((n.claim.untilMs - now) / 1000));
      c.parts.tag.textContent = `${n.claim.holder} ${s} s`;
    }
    if (!any && claimTimer) { clearInterval(claimTimer); claimTimer = 0; }
  }

  // --- update from the store ---
  function presenceFocus(state) {
    const byNode = new Map();
    const clients = state.presence && Array.isArray(state.presence.clients) ? state.presence.clients : [];
    for (const cl of clients) {
      if (!cl || !cl.focus || cl.focus.type !== 'node') continue;
      const kind = cl.kind || cl.by_kind || 'human';
      if (kind !== 'human') continue;
      const name = cl.name || cl.owner;
      if (!name || name === me || (me && cl.owner === me)) continue;
      if (!byNode.has(cl.focus.id)) byNode.set(cl.focus.id, []);
      byNode.get(cl.focus.id).push({ name, hue: hueOf(cl.owner || name, state.people) });
    }
    return byNode;
  }

  function update(force) {
    if (destroyed || !store || typeof store.view !== 'function') return;
    const state = store.view();
    if (!state || !(state.nodes instanceof Map)) return;
    if (!force && sameState(state, lastState)) return;
    lastState = state;
    const nodes = state.nodes;
    const head = typeof store.last === 'function' ? store.last() : 0;

    // visibility and depth
    index = new Map();
    for (const root of nestTree(nodes)) {
      const walk = (t, parent) => { index.set(t.id, { id: t.id, depth: t.depth, parent, children: t.children.map((ch) => ch.id) }); for (const ch of t.children) walk(ch, t.id); };
      walk(root, null);
    }
    const focusByNode = presenceFocus(state);
    // activity, a claim or a focus opens the deeper levels
    for (const [id, n] of nodes) {
      const ix = index.get(id);
      if (!ix || ix.depth < OPEN_DEPTH) continue;
      const active = (n.halo && n.halo.seq > (haloSeen.get(id) || 0)) || n.claim || focusByNode.has(id) || id === selectedId;
      if (active) openAncestors(id);
    }
    const visible = new Set();
    const isVisible = (id) => {
      if (visible.has(id)) return true;
      const ix = index.get(id);
      if (!ix) return false;
      if (ix.depth < OPEN_DEPTH) { visible.add(id); return true; }
      if (ix.parent != null && isVisible(ix.parent) && opened.has(ix.parent)) { visible.add(id); return true; }
      return false;
    };
    for (const id of nodes.keys()) isVisible(id);
    const allOpen = visible.size === nodes.size;
    let positions = allOpen && state.layout && state.layout.tree instanceof Map && state.layout.tree.size === nodes.size
      ? state.layout.tree : null;
    if (!positions) {
      const sub = new Map();
      for (const id of visible) sub.set(id, nodes.get(id));
      positions = layoutTree(sub);
    }

    // halos: in a burst only the latest three
    const halos = [];
    for (const [id, n] of nodes) if (n.halo && visible.has(id) && n.halo.seq > (haloSeen.get(id) || 0)) halos.push({ id, seq: n.halo.seq, by: n.halo.by });
    halos.sort((a, b) => b.seq - a.seq);
    for (const hl of halos) haloSeen.set(hl.id, hl.seq);
    const haloNow = new Set(halos.slice(0, HALO_BURST).map((hl) => hl.id));

    const now = serverNow(state);
    const seenSeq = typeof opts.lastSeenSeq === 'function' ? opts.lastSeenSeq() : lastSeenSeq;
    const seen = new Set();
    let anyClaim = false;
    for (const id of visible) {
      const n = nodes.get(id);
      const ix = index.get(id);
      const pos = positions.get(id) || { x: 0, y: 0 };
      seen.add(id);
      let c = cards.get(id);
      if (!c || c.retiring) {
        if (c) { cards.delete(id); if (c.el.parentNode) c.el.parentNode.removeChild(c.el); if (c.edge.parentNode) c.edge.parentNode.removeChild(c.edge); }
        c = makeCard(id);
        const p = ix.parent != null ? cards.get(ix.parent) : null;
        c.x = p ? p.x : pos.x; c.y = p ? p.y : pos.y;           // born at the parent, slides to its slot
        c.el.style.transform = `translate(${c.x}px, ${c.y}px)`;
      }
      c.parent = ix.parent; c.depth = ix.depth;
      c.tx = pos.x; c.ty = pos.y;
      // the card state
      const st = cardState(n, state.run, me, { nowMs: now, people: state.people, focus: focusByNode.get(id),
                                                lastSeenSeq: Number.isFinite(seenSeq) ? seenSeq : undefined,
                                                stages: opts.contract && opts.contract.stages });
      paintCard(c, n, st, ix, nodes, haloNow.has(id));
      if (n.claim) anyClaim = true;
    }
    for (const c of cards.values()) if (!seen.has(c.id) && !c.retiring) retire(c);
    hud.classList.toggle('is-empty', nodes.size === 0);
    paintHover();
    if (anyClaim && !claimTimer && typeof setInterval === 'function') { claimTimer = setInterval(paintClaims, 1000); if (claimTimer && typeof claimTimer.unref === 'function') claimTimer.unref(); }
    if (!fitted && cards.size) fitted = fit(null, false);      // the first paint fits once the pane has a size
    if (follow) followStep(state);
    lastHeadSeen = head;
    clock.kick();
  }

  function paintCard(c, n, st, ix, nodes, halo) {
    const p = c.parts;
    const classes = ['card', ...st.classes, `hue-${st.hue}`];
    if (c.id === selectedId) classes.push('is-selected');
    if (c.id === focusId) classes.push('is-focus');
    if (ix.depth >= OPEN_DEPTH) classes.push('card--deep');
    const deepCount = ix.depth >= OPEN_DEPTH - 1 && !opened.has(c.id) ? countDescendants(ix.id) : 0;
    const key = classes.join(' ') + '|' + st.chips.map((ch) => ch.text).join('|') + '|' + (n.name || '') + '|' + deepCount + '|' + JSON.stringify(n.counts || null) + '|' + (st.ring ? st.ring.tag + st.ring.focus.map((f) => f.name).join(',') : '');
    if (halo) {
      c.el.classList.remove('is-halo');
      void (c.el.offsetWidth);
      c.el.style.setProperty('--actor', `var(--owner-${hueOf(n.halo && n.halo.by, lastState.people)})`);
      c.el.classList.add('is-halo');
      later(() => c.el.classList.remove('is-halo'), T.halo);
    }
    if (key === c.lastStateKey) return;
    c.lastStateKey = key;
    const keepHalo = c.el.classList.contains('is-halo');
    c.el.setAttribute('class', classes.join(' ') + (keepHalo ? ' is-halo' : ''));
    c.el.setAttribute('aria-label', n.name || c.id);
    // glyph
    const g = GLYPH[n.origin || 'map'] || 'map';
    if (p.glyph.getAttribute('data-glyph') !== g) { p.glyph.textContent = ''; p.glyph.appendChild(icon(g)); p.glyph.setAttribute('data-glyph', g); }
    p.name.textContent = n.name || c.id;
    p.name.setAttribute('title', n.frame || n.name || c.id);
    // chips (the first two on the card, every text in the title)
    p.chips.textContent = '';
    for (const ch of st.chips.slice(0, 2)) {
      const chip = h('span', `chip chip--${ch.icon}`, p.chips);
      chip.appendChild(icon(ch.icon));
      const t = h('span', 'chip__text', chip);
      t.textContent = ch.text;
      chip.setAttribute('title', ch.text);
    }
    if (st.chips.length > 2) { const more = h('span', 'chip chip--more', p.chips); more.textContent = `+${st.chips.length - 2}`; more.setAttribute('title', st.chips.map((x) => x.text).join('\n')); }
    if (st.dot) { const d = h('span', 'chip chip--dot', p.chips); d.setAttribute('title', 'changed since you looked'); d.appendChild(icon('dot')); }
    // queued to applied flip
    if (c.lastStatus === 'queued' && n.status === 'applied') animateOnce(p.chips, [{ transform: 'rotateX(90deg)', opacity: 0.4 }, { transform: 'none', opacity: 1 }], { duration: T.chipFlip, easing: 'ease-out' });
    c.lastStatus = n.status || null;
    // counts per direction
    p.counts.textContent = '';
    const counts = n.counts || {};
    for (const dir of ['inward', 'outward']) {
      const k = counts[dir];
      if (!k || !(k.sketches || k.clusters || k.built || k.checked)) continue;
      const s = h('span', `count count--${dir}`, p.counts);
      s.textContent = `${dir === 'inward' ? 'in' : 'out'} ${k.sketches || 0}/${k.clusters || 0}/${k.built || 0}/${k.checked || 0}`;
      s.setAttribute('title', `${dir}: sketches/clusters/built/checked`);
    }
    // ring (claim or focus)
    if (st.ring) {
      p.ring.style.display = '';
      p.ring.setAttribute('class', `card__ring card__ring--${st.ring.kind} hue-${st.ring.hue}`);
      p.tag.textContent = st.ring.tag || '';
      const names = st.ring.focus.map((f) => f.name);
      p.ring.setAttribute('data-focus', names.join(', '));
      p.tag.textContent = [st.ring.tag, ...names].filter(Boolean).join(' . ');
    } else { p.ring.style.display = 'none'; p.tag.textContent = ''; }
    // fold chip
    if (deepCount > 0) { p.fold.style.display = ''; p.fold.textContent = `+${deepCount}`; p.fold.setAttribute('title', `${deepCount} deeper nodes, click to open`); }
    else if (ix.depth >= OPEN_DEPTH - 1 && opened.has(c.id) && ix.children.length) { p.fold.style.display = ''; p.fold.textContent = '-'; p.fold.setAttribute('title', 'fold the deeper levels'); }
    else p.fold.style.display = 'none';
  }

  function countDescendants(id) {
    const ix = index.get(id);
    if (!ix) return 0;
    let n = 0;
    for (const ch of ix.children) n += 1 + countDescendants(ch);
    return n;
  }

  function followStep(state) {
    const clients = state.presence && Array.isArray(state.presence.clients) ? state.presence.clients : [];
    const cl = clients.find((x) => x && (x.name === follow || x.owner === follow || x.client === follow));
    if (cl) followTo(cl.focus);
  }

  function followTo(f) {
    if (!f || f.type !== 'node') return;
    if (followLast === f.id) return;
    followLast = f.id;
    if (!cards.has(f.id) && openAncestors(f.id)) update(true);
    centerOn(f.id, true);
  }

  // --- keyboard ---
  function moveFocus(dir) {
    const cur = focusId && cards.has(focusId) ? focusId : (selectedId || [...cards.keys()][0]);
    if (!cur) return;
    const ix = index.get(cur);
    let next = cur;
    if (!ix) return;
    if (dir === 'left' && ix.parent != null) next = ix.parent;
    else if (dir === 'right' && ix.children.length) { if (!cards.has(ix.children[0])) { opened.add(cur); update(true); } next = ix.children[0]; }
    else if ((dir === 'up' || dir === 'down') && ix.parent != null) {
      const sib = index.get(ix.parent).children.filter((s) => cards.has(s));
      const i = sib.indexOf(cur);
      next = sib[Math.max(0, Math.min(sib.length - 1, i + (dir === 'up' ? -1 : 1)))];
    }
    focusId = next;
    for (const c of cards.values()) c.el.classList.toggle('is-focus', c.id === next);
    hoverId = next; paintHover();
    emit('hover', { type: 'node', id: next, source: 'tree' });
  }
  viewport.addEventListener('keydown', (e) => {
    const k = e && e.key;
    if (k === 'ArrowLeft') moveFocus('left'); else if (k === 'ArrowRight') moveFocus('right');
    else if (k === 'ArrowUp') moveFocus('up'); else if (k === 'ArrowDown') moveFocus('down');
    else if (k === 'Enter' && focusId) select(focusId);
    else if (k === 'f' || k === 'F') fit(null);
    else return;
    if (e.preventDefault) e.preventDefault();
  });
  viewport.addEventListener('click', () => { if (typeof store.last === 'function') lastSeenSeq = null; });

  // --- bus ---
  on('hover', (e) => {
    if (e && e.source === 'tree') return;
    linkedId = e && e.type === 'cluster' && e.node ? e.node : (e && e.type === 'node' ? e.id : null);
    paintHover();
  });
  on('fit', (e) => { if (!e || e.type === 'tree' || !e.type) fit(e && e.id ? subtreeIds(e.id) : null); });
  on('follow', (e) => {
    const who = e && (e.who || e.person || e.name || e.owner);
    if (!who) { follow = null; followLast = null; return; }
    if (who !== follow) { follow = who; followLast = null; }
    if (e.focus) followTo(e.focus);                      // the page shell sends {who, focus}
    else if (lastState) followStep(lastState);
  });
  on('state', () => update());
  on('select', (e) => { if (e && e.type === 'node' && e.source !== 'tree' && e.id !== selectedId) { selectedId = e.id; for (const c of cards.values()) c.el.classList.toggle('is-selected', c.id === e.id); } });
  if (typeof document.addEventListener === 'function') {
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden' && typeof store.last === 'function') lastSeenSeq = store.last();
      else if (document.visibilityState === 'visible') update(true);
    });
  }
  if (typeof store.subscribe === 'function') store.subscribe(() => update());

  const handle = {
    el, cards, update, fit, centerOn, open: (id) => { opened.add(id); update(true); }, select,
    get follow() { return follow; }, set follow(v) { follow = v || null; followLast = null; },
    destroy() { destroyed = true; unstep(); if (claimTimer) clearInterval(claimTimer); if (el.contains && el.contains(viewport)) el.removeChild(viewport); },
  };
  update(true);
  return handle;
}
