// The replay hash (docs/MULTIPLAYER_DESIGN.md section 12.4): the recorded round, reduced with makeReducer and the
// real layout.mjs, gives the layout hash and the state hash that --rehearse stored; the same log reduced twice
// gives the same hashes. This proves Replay draws what the live run drew.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { readLog, reduceLog, summarize } from './hash.mjs';

const REC = fileURLToPath(new URL('../../../recorded/', import.meta.url));
const LOG = REC + 'stage_round.ndjson';
const HASH = REC + 'stage_round.hash.json';

test('the recorded round and its hash file exist', () => {
  assert.ok(existsSync(LOG), `missing ${LOG}: run python -m space.demo --rehearse`);
  assert.ok(existsSync(HASH), `missing ${HASH}: run python -m space.demo --rehearse`);
});

test('the recorded round reduces to the stored layout hash and state hash', () => {
  const want = JSON.parse(readFileSync(HASH, 'utf8'));
  const events = readLog(LOG);
  const got = summarize(reduceLog(events), events);
  assert.equal(got.events, want.events);
  assert.equal(got.head, want.head);
  assert.match(got.layout_hash, /^[0-9a-f]{8}$/);
  assert.equal(got.layout_hash, want.layout_hash);
  assert.equal(got.state_hash, want.state_hash);
});

test('the same log reduced twice gives the same hashes', () => {
  const events = readLog(LOG);
  const a = summarize(reduceLog(events), events);
  const b = summarize(reduceLog(events.slice().reverse()), events);   // reduceLog sorts by seq first
  assert.equal(a.layout_hash, b.layout_hash);
  assert.equal(a.state_hash, b.state_hash);
});

test('the recorded round shows a won cluster and a hit or miss for both voters', () => {
  const events = readLog(LOG);
  const s = summarize(reduceLog(events), events);
  assert.ok(s.won >= 1, 'no cluster marked won');
  for (const who of ['ana', 'ben']) {
    assert.ok((s.voters[who] || []).some((w) => w === 'hit' || w === 'miss'), `no hit or miss for ${who}`);
  }
});
