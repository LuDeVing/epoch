// hash.mjs: reduce a recorded space log with the real reducer and the real layout (docs/MULTIPLAYER_DESIGN.md 12.4).
//   node space/web/tests/replay/hash.mjs <log.ndjson>
// prints one JSON object: {events, head, layout_hash, state_hash, won, voters, results}. `python -m space.demo
// --rehearse` writes the two hashes to space/recorded/stage_round.hash.json; replay.test.mjs checks them.
import { readFileSync } from 'node:fs';
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';

const require = createRequire(import.meta.url);
globalThis.d3 = globalThis.d3 || require('../../vendor/d3.min.js');   // the page loads it as a classic script
const { makeReducer, hashState } = await import('../../reduce.mjs');
const layout = await import('../../layout.mjs');
const contract = JSON.parse(readFileSync(new URL('../../contract.json', import.meta.url), 'utf8'));

export function readLog(path) {
  return readFileSync(path, 'utf8').split(/\r?\n/).filter((l) => l.trim()).map((l) => JSON.parse(l));
}

// The view state after every event of the log, in seq order, as the page builds it.
export function reduceLog(events) {
  const R = makeReducer({ layoutTree: layout.layoutTree, layoutClusters: layout.layoutClusters,
    anchorFor: layout.anchorFor, contract });
  let s = R.init();
  for (const ev of [...events].sort((a, b) => a.seq - b.seq)) s = R.reduce(s, ev);
  return s;
}

// What the rehearsal checks from the screen's point of view: the hashes, the won clusters, hit or miss per voter.
export function summarize(state, events) {
  const won = [...state.clusters.values()].filter((c) => c.status === 'win' || c.status === 'preferred').length;
  const voters = {};
  for (const r of state.results) {
    for (const [who, word] of Object.entries(r.voters || {})) (voters[who] = voters[who] || []).push(word);
  }
  const c = state.questions.chosen;
  const chosen = c ? { id: c.id, by: c.by, seq: c.seq, overwrote: c.overwrote || [] } : null;
  return { events: events.length, head: state.head, layout_hash: state.layout.hash, state_hash: hashState(state),
    won, voters, results: state.results.length, chosen };
}

export function hashLog(path) {
  const events = readLog(path);
  return summarize(reduceLog(events), events);
}

if (process.argv[1] && pathToFileURL(process.argv[1]).href === import.meta.url) {
  const path = process.argv[2];
  if (!path) {
    process.stderr.write('usage: node space/web/tests/replay/hash.mjs <log.ndjson>\n');
    process.exit(2);
  }
  process.stdout.write(JSON.stringify(hashLog(path)) + '\n');
}
