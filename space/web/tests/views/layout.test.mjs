// Layout determinism and stability (docs/MULTIPLAYER_DESIGN.md sections 6.5 and 12.1 row P5).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import './helpers/d3.mjs';
import { layoutTree, anchorFor, layoutClusters, sunflower, clusterRadius, hashPositions, jitter, nestTree,
         seededLcg, randomSourceFor, CELL_W, CELL_H, SPACING, DOT_R, DOT_GAP } from '../../layout.mjs';

function lcg(seed) { let s = seed >>> 0; return () => { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; }

function seededTree(n, seed) {
  const rnd = lcg(seed);
  const nodes = new Map([['root', { id: 'root', parent: null, firstSeen: 0 }]]);
  const ids = ['root'];
  for (let i = 1; i < n; i++) {
    const depthCap = ids.filter((id) => depthOf(nodes, id) < 4);
    const parent = depthCap[Math.floor(rnd() * depthCap.length)];
    const id = `n${i}`;
    nodes.set(id, { id, parent, firstSeen: i });
    ids.push(id);
  }
  return nodes;
}
function depthOf(nodes, id) { let d = 0; let cur = nodes.get(id); while (cur && cur.parent != null) { d++; cur = nodes.get(cur.parent); } return d; }

function island(count, seed, ideas) {
  const rnd = lcg(seed);
  const out = [];
  let left = ideas;
  for (let k = 0; k < count; k++) {
    const n = k === count - 1 ? Math.max(1, left) : Math.max(1, Math.min(left - (count - k - 1), 1 + Math.floor(rnd() * 14)));
    left -= n;
    out.push({ key: `v${seed}_${k}`, n });
  }
  return out;
}

test('layoutClusters twice on the same input gives identical positions (hash equal)', () => {
  const cl = island(20, 7, 120);
  const a = layoutClusters(new Map(), cl, { x: 440, y: -400 }, new Map());
  const b = layoutClusters(new Map(), cl, { x: 440, y: -400 }, new Map());
  assert.equal(hashPositions(null, a), hashPositions(null, b));
  assert.deepEqual([...a], [...b]);
  for (const p of a.values()) {
    assert.equal(p.x, Math.round(p.x * 100) / 100);
    assert.equal(p.y, Math.round(p.y * 100) / 100);
    assert.equal(p.r, Math.round(p.r * 100) / 100);
  }
  // a plain object for prevIsland and bornFrom works too
  const c = layoutClusters({}, cl, { x: 440, y: -400 }, {});
  assert.equal(hashPositions(null, c), hashPositions(null, a));
});

test('growing one cluster by one idea moves the other bubbles under 15 px on average', () => {
  const cl = island(20, 11, 100);
  const settled = layoutClusters(new Map(), cl, { x: 0, y: 0 }, new Map());
  const grown = cl.map((c) => (c.key === cl[5].key ? { ...c, n: c.n + 1 } : c));
  const next = layoutClusters(settled, grown, { x: 0, y: 0 }, new Map());
  let sum = 0, count = 0, worst = 0;
  for (const [k, p] of next) {
    if (k === cl[5].key) continue;
    const q = settled.get(k);
    const d = Math.hypot(p.x - q.x, p.y - q.y);
    sum += d; count++; worst = Math.max(worst, d);
  }
  assert.ok(sum / count < 15, `average move ${(sum / count).toFixed(2)} px (worst ${worst.toFixed(1)})`);
  assert.equal(next.get(cl[5].key).r, Math.round(clusterRadius(cl[5].n + 1) * 100) / 100);
});

test('a new bubble starts at its bornFrom parent, else at the anchor plus the deterministic jitter', () => {
  const cl = island(6, 3, 30);
  const settled = layoutClusters(new Map(), cl, { x: 100, y: 50 }, new Map());
  const withSplit = [...cl, { key: 'child', n: 2 }];
  const born = new Map([['child', cl[2].key]]);
  const next = layoutClusters(settled, withSplit, { x: 100, y: 50 }, born);
  const parent = settled.get(cl[2].key);
  const child = next.get('child');
  assert.ok(Math.hypot(child.x - parent.x, child.y - parent.y) < 2 * (parent.r + child.r) + 10, 'the child stays near its parent');
  assert.deepEqual(jitter(0), { x: -11, y: -14 });
  assert.deepEqual(jitter(1), { x: -4, y: -3 });
  assert.deepEqual(jitter(7), { x: -8, y: 5 });
  assert.deepEqual(jitter(23), { x: -11, y: (253 % 29) - 14 });
});

test('150 clusters with 800 ideas lay out under 100 ms per snapshot', () => {
  const islands = [];
  for (let i = 0; i < 15; i++) islands.push(island(10, 100 + i, Math.floor(800 / 15)));
  layoutClusters(new Map(), islands[0], anchorFor(0, 15), new Map());             // warm up
  let worst = 0;
  const settled = [];
  for (let i = 0; i < 15; i++) {
    const t0 = performance.now();
    settled.push(layoutClusters(new Map(), islands[i], anchorFor(i, 15), new Map()));
    worst = Math.max(worst, performance.now() - t0);
  }
  assert.ok(worst < 100, `worst island settle ${worst.toFixed(1)} ms`);
  // the whole 150 as one island is the pathological case and still fits the cap
  const all = islands.flat();
  const t1 = performance.now();
  layoutClusters(new Map(), all, { x: 0, y: 0 }, new Map());
  const dt = performance.now() - t1;
  assert.ok(dt < 100, `one island of 150 bubbles took ${dt.toFixed(1)} ms`);
  // bubbles of one island do not overlap after the settle
  let overlaps = 0;
  const pts = [...settled[0].values()];
  for (let a = 0; a < pts.length; a++) for (let b = a + 1; b < pts.length; b++) {
    if (Math.hypot(pts[a].x - pts[b].x, pts[a].y - pts[b].y) < pts[a].r + pts[b].r - 1) overlaps++;
  }
  assert.equal(overlaps, 0);
});

test('layoutTree on a seeded 60-node tree with 3 added leaves moves old nodes under 60 px on average and never swaps siblings', () => {
  const nodes = seededTree(60, 42);
  const before = layoutTree(nodes);
  assert.equal(before.size, 60);
  assert.deepEqual(before.get('root'), { x: 0, y: 0 });
  const rnd = lcg(99);
  const ids = [...nodes.keys()];
  const grown = new Map(nodes);
  for (let i = 0; i < 3; i++) {
    const parent = ids[Math.floor(rnd() * ids.length)];
    grown.set(`leaf${i}`, { id: `leaf${i}`, parent, firstSeen: 1000 + i });
  }
  const after = layoutTree(grown);
  assert.equal(after.size, 63);
  let sum = 0;
  for (const id of nodes.keys()) sum += Math.hypot(after.get(id).x - before.get(id).x, after.get(id).y - before.get(id).y);
  assert.ok(sum / 60 < 60, `average move ${(sum / 60).toFixed(1)} px`);
  // sibling order by y is the first-seen order, before and after
  const children = new Map();
  for (const n of grown.values()) if (n.parent != null) { if (!children.has(n.parent)) children.set(n.parent, []); children.get(n.parent).push(n.id); }
  for (const [, kids] of children) {
    const old = kids.filter((k) => before.has(k));
    const byBefore = [...old].sort((a, b) => before.get(a).y - before.get(b).y);
    const byAfter = [...old].sort((a, b) => after.get(a).y - after.get(b).y);
    assert.deepEqual(byAfter, byBefore);
    const bySeen = [...old].sort((a, b) => grown.get(a).firstSeen - grown.get(b).firstSeen);
    assert.deepEqual(byBefore, bySeen);
  }
  // depth is x: every child sits one column right of its parent
  for (const n of grown.values()) if (n.parent != null) assert.equal(after.get(n.id).x, after.get(n.parent).x + 250);
  // the same input gives the same map
  assert.deepEqual([...layoutTree(grown)], [...after]);
});

test('layoutTree uses firstSeen, never name or score, and tolerates an explicit firstSeen map', () => {
  const nodes = new Map([
    ['root', { id: 'root', parent: null, name: 'z' }],
    ['b', { id: 'b', parent: 'root', name: 'a', score: 9 }],
    ['a', { id: 'a', parent: 'root', name: 'b', score: 1 }],
  ]);
  const seen = new Map([['root', 1], ['b', 2], ['a', 3]]);
  const pos = layoutTree(nodes, seen);
  assert.ok(pos.get('b').y < pos.get('a').y, 'b was seen first, so it sits above a');
  const roots = nestTree(nodes, seen);
  assert.equal(roots.length, 1);
  assert.deepEqual(roots[0].children.map((c) => c.id), ['b', 'a']);
  assert.equal(layoutTree(new Map()).size, 0);
});

test('anchorFor: first-seen order on a centred grid of 440 x 400 cells', () => {
  assert.deepEqual(anchorFor(0, 1), { x: 0, y: 0 });
  assert.deepEqual(anchorFor(0, 9), { x: -CELL_W, y: -CELL_H });
  assert.deepEqual(anchorFor(4, 9), { x: 0, y: 0 });
  assert.deepEqual(anchorFor(8, 9), { x: CELL_W, y: CELL_H });
  assert.deepEqual(anchorFor(0, 2), { x: -CELL_W / 2, y: 0 });
  assert.deepEqual(anchorFor(1, 2), { x: CELL_W / 2, y: 0 });
  // 7 parts: 3 columns, 3 rows, the last row has one island
  assert.deepEqual(anchorFor(6, 7), { x: -CELL_W, y: CELL_H });
  assert.equal(CELL_W, 440); assert.equal(CELL_H, 400);
});

test('sunflower slots have no overlap for n up to 40 and sit inside the radius', () => {
  const minGap = 2 * DOT_R + DOT_GAP;
  for (let n = 1; n <= 40; n++) {
    const pts = []; for (let k = 0; k < n; k++) pts.push(sunflower(k, SPACING));
    const R = clusterRadius(n);
    for (let a = 0; a < n; a++) {
      assert.ok(Math.hypot(pts[a].x, pts[a].y) + DOT_R <= R + 1e-9, `dot ${a} of ${n} outside r=${R.toFixed(2)}`);
      for (let b = a + 1; b < n; b++) {
        const d = Math.hypot(pts[a].x - pts[b].x, pts[a].y - pts[b].y);
        assert.ok(d >= minGap - 1e-9, `dots ${a} and ${b} of ${n} overlap (${d.toFixed(2)} < ${minGap})`);
      }
    }
  }
  assert.ok(Math.abs(clusterRadius(1) - (7.8 * Math.sqrt(1.5) + 6)) < 1e-9);
  assert.ok(Math.abs(clusterRadius(15) - (7.8 * Math.sqrt(15.5) + 6)) < 1e-9);
});

test('d3.randomLcg and randomSource exist in the vendored D3, and the seeded LCG fallback is deterministic', () => {
  const d3 = globalThis.d3;
  assert.equal(d3.version, '7.9.0');
  assert.equal(typeof d3.randomLcg, 'function');
  assert.equal(typeof d3.forceSimulation().stop().randomSource, 'function');
  const a = d3.randomLcg(1), b = d3.randomLcg(1);
  assert.equal(a(), b());
  const f1 = seededLcg(1), f2 = seededLcg(1);
  const s1 = [f1(), f1(), f1()], s2 = [f2(), f2(), f2()];
  assert.deepEqual(s1, s2);
  for (const v of s1) assert.ok(v >= 0 && v < 1);
  assert.notEqual(seededLcg(2)(), s1[0]);
  // a d3 without randomLcg gets the fallback and the layout still settles the same way twice
  const fake = Object.assign(Object.create(null), d3, { randomLcg: undefined });
  assert.equal(typeof randomSourceFor(fake, 1), 'function');
  assert.equal(randomSourceFor(fake, 1)(), seededLcg(1)());
  const cl = island(12, 5, 60);
  const saved = globalThis.d3;
  globalThis.d3 = fake;
  try {
    const x = layoutClusters(new Map(), cl, { x: 0, y: 0 }, new Map());
    const y = layoutClusters(new Map(), cl, { x: 0, y: 0 }, new Map());
    assert.equal(hashPositions(null, x), hashPositions(null, y));
  } finally { globalThis.d3 = saved; }
});
