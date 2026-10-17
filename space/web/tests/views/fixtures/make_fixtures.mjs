// Builds the two cluster_snapshot fixtures of the views tests (docs/MULTIPLAYER_DESIGN.md section 16.6).
// snapshot_1.json: the clusters of the mock run's idea_clusters.json, private keys stripped
//   (obvious, obvious_match, prior_match, prior_source, representative, leap_ops never leave the run folder).
// snapshot_2.json: the same clusters after moving 10 percent of the members between clusters of the same part
//   and shuffling the order, with a fixed seed. Run once by hand:
//   node space/web/tests/views/fixtures/make_fixtures.mjs <path to idea_clusters.json>
import { readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const src = process.argv[2];
if (!src) { console.error('usage: node make_fixtures.mjs <idea_clusters.json>'); process.exit(2); }
const KEEP = ['cluster_id', 'name', 'members', 'n', 'node', 'direction', 'score', 'rank', 'selected', 'lane', 'prior', 'cards'];

function lcg(seed) { let s = seed >>> 0; return () => { s = (Math.imul(s, 1664525) + 1013904223) >>> 0; return s / 4294967296; }; }

const raw = JSON.parse(readFileSync(src, 'utf8'));
const clean = raw.clusters.map((c) => {
  const o = {};
  for (const k of KEEP) if (c[k] !== undefined) o[k] = c[k];
  if (o.lane === undefined) o.lane = 'team';
  return o;
});
const snap1 = { round: raw.round, clusters: clean };

const rnd = lcg(20261017);
const copy = clean.map((c) => ({ ...c, members: [...c.members] }));
const byPart = new Map();
copy.forEach((c, i) => { const k = `${c.node}/${c.direction}`; if (!byPart.has(k)) byPart.set(k, []); byPart.get(k).push(i); });
const total = copy.reduce((s, c) => s + c.members.length, 0);
let moved = 0;
const target = Math.round(total * 0.10);
const parts = [...byPart.values()].filter((idx) => idx.length > 1);
let guard = 0;
while (moved < target && guard++ < 100000) {
  const idx = parts[Math.floor(rnd() * parts.length)];
  const from = copy[idx[Math.floor(rnd() * idx.length)]];
  const to = copy[idx[Math.floor(rnd() * idx.length)]];
  if (from === to || from.members.length < 3) continue;
  const m = from.members.splice(Math.floor(rnd() * from.members.length), 1)[0];
  to.members.push(m);
  moved++;
}
for (const c of copy) c.n = c.members.length;
for (let i = copy.length - 1; i > 0; i--) { const j = Math.floor(rnd() * (i + 1)); [copy[i], copy[j]] = [copy[j], copy[i]]; }
const snap2 = { round: raw.round + 1, clusters: copy, moved, total };

writeFileSync(join(here, 'snapshot_1.json'), JSON.stringify(snap1, null, 1) + '\n');
writeFileSync(join(here, 'snapshot_2.json'), JSON.stringify(snap2, null, 1) + '\n');
console.log(`wrote ${clean.length} clusters, ${total} members; moved ${moved} (${(100 * moved / total).toFixed(1)} percent)`);
