// space/web/layout.mjs: the deterministic layout of the tree and the cluster islands.
// docs/MULTIPLAYER_DESIGN.md section 6.5, word for word. Pure functions of their inputs:
// the same log gives the same picture in every window, and the reducer hashes it.
//
// d3 (vendor/d3.min.js, D3 7.9.0 UMD) must be loaded as a classic script before the modules in the browser.
// Under Node, set the global first:
//   globalThis.d3 = createRequire(import.meta.url)('../vendor/d3.min.js');
// or call `await ensureD3()` from this module, which does that for you when it can.

export const ROW_H = 56;            // d3.tree nodeSize breadth (screen y)
export const COL_W = 250;           // d3.tree nodeSize depth (screen x)
export const CELL_W = 440;          // anchor grid cell, world units
export const CELL_H = 400;
export const SPACING = 7.8;         // sunflower spacing: (2 * 5 + 2) / 1.5456
export const DOT_R = 5;
export const DOT_GAP = 2;
export const PAD = 6;               // radius padding
export const COLLIDE_PAD = 3;
export const TICKS = 120;
export const PRECISION = 100;       // positions rounded to 0.01

export const D3_MISSING = 'd3 is missing: load vendor/d3.min.js as a classic script before the modules ' +
  "(under Node: globalThis.d3 = createRequire(import.meta.url)('./vendor/d3.min.js'), or await ensureD3())";

export function requireD3() {
  const d3 = globalThis.d3;
  if (!d3 || typeof d3.tree !== 'function' || typeof d3.forceSimulation !== 'function') throw new Error(D3_MISSING);
  return d3;
}

// Under Node only: load the vendored d3 through createRequire and keep it on the global. A no-op in a browser.
export async function ensureD3() {
  if (globalThis.d3 && typeof globalThis.d3.tree === 'function') return globalThis.d3;
  const isNode = typeof process !== 'undefined' && process.versions && process.versions.node;
  if (!isNode) throw new Error(D3_MISSING);
  const { createRequire } = await import('node:module');
  const req = createRequire(import.meta.url);
  globalThis.d3 = req('./vendor/d3.min.js');
  return globalThis.d3;
}

// Seeded LCG fallback for d3.randomLcg (owner decision 10): same contract, a function that returns [0, 1).
// Used only when the vendored d3 has no randomLcg. Park-Miller minimal standard, seed scaled from [0, 1).
export function seededLcg(seed = 1) {
  let state = Math.floor((seed % 1 === 0 ? seed : seed * 2147483646) || 1) % 2147483647;
  if (state <= 0) state += 2147483646;
  return () => {
    state = (state * 16807) % 2147483647;
    return (state - 1) / 2147483646;
  };
}

export function randomSourceFor(d3, seed = 1) {
  return typeof d3.randomLcg === 'function' ? d3.randomLcg(seed) : seededLcg(seed);
}

const round2 = (v) => Math.round(v * PRECISION) / PRECISION;

// Sunflower (phyllotaxis) slot k, in arrival order. A new dot never moves the old ones.
const GOLDEN = Math.PI * (3 - Math.sqrt(5));
export function sunflower(k, spacing = SPACING) {
  const r = spacing * Math.sqrt(k + 0.5);
  const a = k * GOLDEN;
  return { x: r * Math.cos(a), y: r * Math.sin(a) };
}

export function clusterRadius(n, spacing = SPACING, pad = PAD) {
  return spacing * Math.sqrt(Math.max(0, n) + 0.5) + pad;
}

// The deterministic start jitter for a bubble with no parent: k is the cluster's index in the snapshot.
export function jitter(k) {
  return { x: ((k * 7) % 23) - 11, y: ((k * 11) % 29) - 14 };
}

// --- tree ---------------------------------------------------------------------------------------------------------

function asMap(x) {
  if (x instanceof Map) return x;
  const m = new Map();
  if (Array.isArray(x)) for (const n of x) m.set(n.id, n);
  else if (x && typeof x === 'object') for (const k of Object.keys(x)) m.set(k, x[k]);
  return m;
}

function seenOf(firstSeen, nodes, id) {
  if (firstSeen instanceof Map) { const v = firstSeen.get(id); if (v != null) return v; }
  else if (firstSeen && typeof firstSeen === 'object') { const v = firstSeen[id]; if (v != null) return v; }
  const n = nodes.get(id);
  if (n && n.firstSeen != null) return n.firstSeen;
  if (n && n.seq != null) return n.seq;
  return Number.MAX_SAFE_INTEGER;
}

// Children sorted by first-seen order (then id, for a tie), never by name or score.
function childOrder(nodes, firstSeen) {
  return (a, b) => (seenOf(firstSeen, nodes, a) - seenOf(firstSeen, nodes, b)) || (a < b ? -1 : a > b ? 1 : 0);
}

// Build the nested tree(s) from the flat node map. A node whose parent is unknown is a root.
export function nestTree(nodes, firstSeen) {
  nodes = asMap(nodes);
  const children = new Map();
  const roots = [];
  for (const [id, n] of nodes) {
    const p = n.parent;
    if (p != null && p !== id && nodes.has(p)) {
      if (!children.has(p)) children.set(p, []);
      children.get(p).push(id);
    } else roots.push(id);
  }
  const cmp = childOrder(nodes, firstSeen);
  roots.sort(cmp);
  for (const list of children.values()) list.sort(cmp);
  const build = (id, depth) => ({ id, depth, children: (children.get(id) || []).map((c) => build(c, depth + 1)) });
  return roots.map((r) => build(r, 0));
}

// layoutTree(nodes, firstSeen) -> Map(id -> {x, y}), world units, the first root at (0, 0).
// Screen x is the d3 node's y (depth), screen y is its x (breadth). Levels deeper than 3 are laid out too.
export function layoutTree(nodes, firstSeen) {
  const d3 = requireD3();
  nodes = asMap(nodes);
  const out = new Map();
  if (nodes.size === 0) return out;
  const roots = nestTree(nodes, firstSeen);
  const tree = d3.tree().nodeSize([ROW_H, COL_W]);
  let offsetY = 0;
  for (const root of roots) {
    const h = d3.hierarchy(root, (d) => d.children);
    tree(h);
    let minX = Infinity, maxX = -Infinity;
    h.each((d) => { if (d.x < minX) minX = d.x; if (d.x > maxX) maxX = d.x; });
    const shift = roots.length > 1 ? offsetY - minX : 0;     // a second root tree stacks below the first
    h.each((d) => out.set(d.data.id, { x: round2(d.y), y: round2(d.x + shift) }));
    offsetY += (maxX - minX) + 2 * ROW_H;
  }
  return out;
}

// --- anchors ------------------------------------------------------------------------------------------------------

// anchorFor(partIndex, nParts) -> {x, y}: parts in first-seen order on a centred grid, cell 440 x 400 world units.
export function anchorFor(partIndex, nParts) {
  const n = Math.max(1, nParts | 0);
  const i = Math.max(0, partIndex | 0);
  const cols = Math.ceil(Math.sqrt(n));
  const rows = Math.ceil(n / cols);
  const col = i % cols;
  const row = Math.floor(i / cols);
  return { x: round2((col - (cols - 1) / 2) * CELL_W), y: round2((row - (rows - 1) / 2) * CELL_H) };
}

// --- clusters -----------------------------------------------------------------------------------------------------

function lookup(coll, key) {
  if (!coll) return undefined;
  if (coll instanceof Map) return coll.get(key);
  return coll[key];
}

// layoutClusters(prevIsland, islandClusters, anchor, bornFrom) -> Map(key -> {x, y, r})
//   prevIsland:     Map(key -> {x, y, r}) of the island's bubbles before this snapshot (or a plain object)
//   islandClusters: the island's clusters in snapshot order, each with `key` and `n`
//   anchor:         {x, y} of the island
//   bornFrom:       Map(key -> parent key) for bubbles that split off an existing one (or a plain object)
// An existing bubble starts from its previous position; a new one at its bornFrom parent's position, else at the
// anchor plus a deterministic jitter. One seeded simulation, exactly 120 ticks, positions rounded to 0.01.
export function layoutClusters(prevIsland, islandClusters, anchor, bornFrom) {
  const d3 = requireD3();
  const ax = anchor && Number.isFinite(anchor.x) ? anchor.x : 0;
  const ay = anchor && Number.isFinite(anchor.y) ? anchor.y : 0;
  const list = Array.isArray(islandClusters) ? islandClusters : [...asMap(islandClusters).values()];
  const out = new Map();
  if (list.length === 0) return out;
  const bubbles = list.map((c, k) => {
    const key = c.key != null ? c.key : c.clusterId != null ? c.clusterId : String(k);
    const n = Number.isFinite(c.n) ? c.n : Array.isArray(c.members) ? c.members.length : 1;
    const r = clusterRadius(n);
    const prev = lookup(prevIsland, key);
    if (prev && Number.isFinite(prev.x) && Number.isFinite(prev.y)) return { key, r, x: prev.x, y: prev.y };
    const parentKey = lookup(bornFrom, key);
    const parent = parentKey != null ? lookup(prevIsland, parentKey) : undefined;
    if (parent && Number.isFinite(parent.x) && Number.isFinite(parent.y)) return { key, r, x: parent.x, y: parent.y };
    const j = jitter(k);
    return { key, r, x: ax + j.x, y: ay + j.y };
  });
  const sim = d3.forceSimulation(bubbles)
    .randomSource(randomSourceFor(d3, 1))
    .force('collide', d3.forceCollide((d) => d.r + COLLIDE_PAD).iterations(2))
    .force('x', d3.forceX(ax).strength(0.05))
    .force('y', d3.forceY(ay).strength(0.05))
    .alpha(1).alphaDecay(0.05).velocityDecay(0.4).stop();
  for (let i = 0; i < TICKS; i++) sim.tick();
  for (const b of bubbles) out.set(b.key, { x: round2(b.x), y: round2(b.y), r: round2(b.r) });
  return out;
}

// Group a snapshot's clusters into islands (one per part, both directions), in first-seen part order.
// A helper for callers that hold a whole snapshot; the reducer may do its own grouping.
export function islandsOf(clusters, partOrder) {
  const byPart = new Map();
  const order = partOrder ? [...partOrder] : [];
  for (const c of clusters instanceof Map ? clusters.values() : clusters) {
    const part = c.node == null ? 'offtree' : c.node;
    if (!byPart.has(part)) { byPart.set(part, []); if (!order.includes(part)) order.push(part); }
    byPart.get(part).push(c);
  }
  return order.filter((p) => byPart.has(p)).map((part, i) => ({ part, index: i, clusters: byPart.get(part) }));
}

// FNV-1a 32 over a string, printed as 8 hex characters (the reducer's hashLayout uses the same function).
export function fnv1a(str) {
  let h = 0x811c9dc5;
  for (let i = 0; i < str.length; i++) {
    h ^= str.charCodeAt(i);
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h.toString(16).padStart(8, '0');
}

export function hashPositions(treeMap, clusterMap) {
  const t = [...(treeMap || new Map())].map(([id, p]) => [id, p.x, p.y]).sort((a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0));
  const c = [...(clusterMap || new Map())].map(([k, p]) => [k, p.x, p.y, p.r]).sort((a, b) => (a[0] < b[0] ? -1 : a[0] > b[0] ? 1 : 0));
  return fnv1a(JSON.stringify(t) + JSON.stringify(c));
}
