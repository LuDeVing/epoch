// The store: server truth plus my pending edits (note 02 A.4), driven by the real reducer.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { makeStore } from '../../store.mjs';
import { makeReducer, trivialLayout } from '../../reduce.mjs';
import { loadLog } from './contract_src.mjs';

const LOG = loadLog();
const base = LOG.slice(0, 9);                       // the planned map, the loop waits at planned r1

function boot() {
  const R = makeReducer(trivialLayout);
  const st = makeStore(R.reduce, R.init);
  for (const e of base) st.applyServer(e);
  return st;
}
const mine = { kind: 'node_added', by: 'ana', by_kind: 'human', owner: 'ana', data: { id: 'item_order', name: 'item order', parent: 'root', origin: 'human', frame: 'f' } };
const peer = (seq) => ({ seq, kind: 'note_posted', by: 'ben', by_kind: 'human', owner: 'ben', op: `ben-1-${seq}`, data: { text: 'hello' } });

test('a pending edit shows at once', () => {
  const st = boot();
  st.addPending('ana-1-1', mine);
  assert.equal(st.view().nodes.get('item_order').status, 'pending');
  assert.equal(st.status('ana-1-1'), 'pending');
  assert.equal(st.view().feed.at(-1).status, 'pending');
});

test('a peer event does not make my pending edit flicker; my echo keeps it, once', () => {
  const st = boot();
  st.addPending('ana-1-1', mine);
  const seen = [];
  assert.equal(st.applyServer(peer(10)), true);
  seen.push(st.view().nodes.get('item_order')?.status);
  st.queued('ana-1-1', 11);
  assert.equal(st.status('ana-1-1'), 'queued');
  seen.push(st.view().nodes.get('item_order')?.status);
  st.applyServer({ ...mine, seq: 11, op: 'ana-1-1' });
  seen.push(st.view().nodes.get('item_order')?.status);
  assert.deepEqual(seen, ['pending', 'pending', 'queued'], 'never missing between frames');
  assert.equal(st.view().feed.filter((l) => l.op === 'ana-1-1').length, 1, 'my line is not doubled');
  assert.equal(st.view().feed.some((l) => l.op === 'ben-1-10'), true);
  assert.equal(st.view().head, 11);
  // the loop applies it
  st.applyServer({ seq: 12, kind: 'control_applied', by: 'team.loop', by_kind: 'system', owner: 'team', data: { refs: [11], round: 1, stage: 'planned' } });
  assert.equal(st.status('ana-1-1'), 'applied');
  assert.equal(st.view().nodes.get('item_order').status, 'applied');
});

test('a rejected edit rolls back; a repeated event is ignored', () => {
  const st = boot();
  st.addPending('ana-1-1', mine);
  assert.ok(st.view().nodes.has('item_order'));
  st.reject('ana-1-1');
  assert.ok(!st.view().nodes.has('item_order'));
  assert.equal(st.view().feed.some((l) => l.status === 'pending'), false);
  assert.equal(st.applyServer(base[3]), false);
  assert.equal(st.last(), 9);
});

test('the whole fixture through the store equals the reducer alone', () => {
  const R = makeReducer(trivialLayout);
  const st = makeStore(R.reduce, R.init);
  for (const e of LOG) st.applyServer(e);
  const direct = LOG.reduce((s, e) => R.reduce(s, e), R.init());
  assert.equal(st.view().layout.hash, direct.layout.hash);
  assert.equal(st.view().feed.length, direct.feed.length);
});
