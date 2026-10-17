// Cluster-key stability on two real snapshots (docs/MULTIPLAYER_DESIGN.md section 16.6): the mock run's
// idea_clusters.json, then the same with 10 percent of the members moved within their part and the order shuffled.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import './helpers/d3.mjs';
import { matchClusters } from './helpers/match.mjs';
import { layoutClusters, anchorFor, islandsOf } from '../../layout.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const snap1 = JSON.parse(readFileSync(join(here, 'fixtures', 'snapshot_1.json'), 'utf8'));
const snap2 = JSON.parse(readFileSync(join(here, 'fixtures', 'snapshot_2.json'), 'utf8'));

const PRIVATE = ['obvious', 'obvious_match', 'private'];
function groups(snap) {
  const g = new Map();
  for (const c of snap.clusters) { const k = `${c.node}/${c.direction}`; if (!g.has(k)) g.set(k, []); g.get(k).push(c); }
  return g;
}

test('the fixtures are real snapshots with no private key', () => {
  assert.equal(snap1.clusters.length, 135);
  assert.equal(snap2.clusters.length, 135);
  for (const snap of [snap1, snap2]) for (const c of snap.clusters) for (const k of PRIVATE) assert.ok(!(k in c), `${k} in a fixture`);
  const m1 = snap1.clusters.reduce((s, c) => s + c.members.length, 0);
  const m2 = snap2.clusters.reduce((s, c) => s + c.members.length, 0);
  assert.equal(m1, 739);
  assert.equal(m2, 739);
  assert.ok(snap2.moved >= 70 && snap2.moved <= 78, `moved ${snap2.moved}`);
  assert.notDeepEqual(snap1.clusters.map((c) => c.cluster_id), snap2.clusters.map((c) => c.cluster_id), 'the order is shuffled');
});

test('two successive snapshots give stable keys for at least 90 percent (Jaccard 0.3, greedy, per node and direction)', () => {
  const g1 = groups(snap1), g2 = groups(snap2);
  let total = 0, kept = 0, counter = 0;
  for (const [k, prevList] of g1) {
    const prev = prevList.map((c, i) => ({ vid: `${k}:${i}`, members: c.members }));
    const next = g2.get(k) || [];
    const r = matchClusters(prev, next, counter, 0.3);
    counter = r.counter;
    total += prev.length;
    kept += r.vids.filter((v) => v && v.startsWith(`${k}:`)).length;
    assert.equal(new Set(r.vids).size, r.vids.length, 'keys are unique within a snapshot');
  }
  assert.equal(total, 135);
  assert.ok(kept / total >= 0.9, `${kept} of ${total} keys survived (${(100 * kept / total).toFixed(1)} percent)`);
});

test('the islands re-settle from the first snapshot to the second with small moves', () => {
  const parts = [...new Set(snap1.clusters.map((c) => c.node))];
  const g1 = groups(snap1), g2 = groups(snap2);
  const keyed = (list, k) => list.map((c, i) => ({ ...c, key: `${k}:${i}` }));
  // keys for snapshot 2 through the matcher, so the same cluster keeps its key
  const keys2 = new Map();
  let counter = 0;
  for (const [k, prevList] of g1) {
    const r = matchClusters(prevList.map((c, i) => ({ vid: `${k}:${i}`, members: c.members })), g2.get(k) || [], counter, 0.3);
    counter = r.counter;
    (g2.get(k) || []).forEach((c, i) => keys2.set(c, { key: r.vids[i], born: r.born[r.vids[i]] || null }));
  }
  const islands1 = islandsOf([...g1.entries()].flatMap(([k, l]) => keyed(l, k)), parts);
  assert.equal(islands1.length, parts.length);
  let sum = 0, count = 0, worst = 0;
  for (const is of islands1) {
    const anchor = anchorFor(is.index, islands1.length);
    const first = layoutClusters(new Map(), is.clusters, anchor, new Map());
    const nextList = snap2.clusters.filter((c) => c.node === is.part).map((c) => ({ ...c, key: keys2.get(c).key }));
    const born = new Map(nextList.filter((c) => keys2.get(snap2.clusters.find((x) => x === c)) && keys2.get(snap2.clusters.find((x) => x === c)).born).map((c) => [c.key, keys2.get(snap2.clusters.find((x) => x === c)).born]));
    const second = layoutClusters(first, nextList, anchor, born);
    for (const [key, p] of second) {
      const q = first.get(key);
      if (!q) continue;
      const d = Math.hypot(p.x - q.x, p.y - q.y);
      sum += d; count++; worst = Math.max(worst, d);
    }
    // every bubble of the island stays within its cell
    for (const p of second.values()) {
      assert.ok(Math.abs(p.x - anchor.x) < 260 && Math.abs(p.y - anchor.y) < 260, `bubble drifted to ${p.x},${p.y} from ${anchor.x},${anchor.y}`);
    }
  }
  assert.ok(count > 100, `${count} surviving bubbles`);
  assert.ok(sum / count < 15, `average move ${(sum / count).toFixed(2)} px, worst ${worst.toFixed(1)}`);
});
