// The reducer over fixtures/log_sample.ndjson with the trivial layout (section 12.1 row P4).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { makeReducer, trivialLayout, SENTENCES, FEED_EXTRA, NOT_IN_FEED, chipText, hashLayout, hashState, nextBoundary,
  groupFeed, whoText, q } from '../../reduce.mjs';
import { loadContract, loadLog, pythonKinds } from './contract_src.mjs';

const LOG = loadLog();
const run = (log, R = makeReducer(trivialLayout)) => log.reduce((s, e) => R.reduce(s, e), R.init());
const upTo = (seq) => LOG.filter((e) => e.seq <= seq);
const seqOf = (pred) => LOG.find(pred).seq;

test('the fixture has 300 events with seq 1..300 and covers every day-one kind of the contract', () => {
  assert.equal(LOG.length, 300);
  LOG.forEach((e, i) => assert.equal(e.seq, i + 1));
  const { json, src } = loadContract();
  const kinds = Object.keys(json.kinds);
  assert.equal(kinds.length, 37, `37 day-one kinds in ${src}`);
  const seen = new Set(LOG.map((e) => e.kind));
  assert.deepEqual(kinds.filter((k) => !seen.has(k)), [], 'every kind appears in the fixture');
  assert.deepEqual([...seen].filter((k) => !kinds.includes(k)), [], 'no kind outside the contract');
  for (const e of LOG) for (const key of ['obvious', 'obvious_match', 'private']) assert.ok(!JSON.stringify(e.data).includes(`"${key}"`));
});

test('reduce gives the expected counts', () => {
  const s = run(LOG);
  assert.equal(s.head, 300);
  // nodes: root, six planned parts, Ana's item_order
  assert.equal(s.nodes.size, 8);
  assert.equal(s.nodes.get('item_order').status, 'applied');
  assert.deepEqual(s.nodes.get('item_order').appliedAt, { round: 1, stage: 'planned', seq: 19 });
  assert.equal(s.nodes.get('item_order').owner, 'ana');
  assert.equal(s.nodes.get('item_order').origin, 'human');
  assert.equal(s.nodes.get('item_order').name, 'item order rule', 'node_edited renamed it');
  assert.equal(s.nodes.get('choice').status, 'map');
  assert.deepEqual(s.nodes.get('choice').disputed.map((d) => d.by), ['ben']);
  assert.deepEqual(s.nodes.get('ties').disputed.map((d) => [d.by, d.tag]), [['ben', 'belief']]);
  assert.equal(s.nodes.get('stats').skippedBy, null, 'skipped then restored');
  assert.equal(s.nodes.get('item_order').claim, null, 'taken over then released');
  assert.equal(s.nodes.get('choice').counts.inward.built, 2);
  assert.equal(s.nodes.get('choice').counts.inward.checked, 2);
  assert.equal(s.nodes.get('choice').counts.inward.clusters, 3);
  // clusters: 7 live keys; the regrouping of choice gives one born (v8 from v2) and one dead (v3 into v1)
  assert.deepEqual([...s.clusters.keys()].sort(), ['v1', 'v2', 'v4', 'v5', 'v6', 'v7', 'v8']);
  const born = [...s.clusters.values()].filter((c) => c.bornFrom);
  assert.deepEqual(born.map((c) => [c.key, c.bornFrom]), [['v8', 'v2']]);
  assert.deepEqual([...s.retired.values()].map((c) => [c.key, c.mergedInto]), [['v3', 'v1']]);
  assert.equal(s.clusters.get('v1').name, 'best fit');
  assert.equal(s.clusters.get('v1').n, 7);
  assert.equal(s.clusters.get('v1').clusterId, 'choice-in-k01', 'the positional id moved, the key held');
  assert.deepEqual(s.clusters.get('v4').contributors, { ana: 3 }, 'sketches from Ana\'s seed count for Ana');
  assert.equal(s.clusters.get('v1').status, 'win');
  assert.equal(s.clusters.get('v2').status, 'loss');
  assert.equal(s.clusters.get('v8').status, 'open');
  // chains: two objections on best fit, the author's reply, a person's reply, two marks
  assert.equal(s.chains.size, 1);
  const chain = s.chains.get('v1');
  assert.equal(chain.length, 2);
  assert.equal(chain[0].reply.kind, 'measure');
  assert.equal(chain[0].mark.verdict, 'resolved');
  assert.equal(chain[1].reply.owner, 'ana');
  assert.equal(chain[1].reply.cls, 'person');
  assert.equal(chain[1].mark.verdict, 'standing');
  // results with hit and miss
  assert.equal(s.results.length, 3);
  const byCand = Object.fromEntries(s.results.map((r) => [r.cand, r]));
  assert.equal(byCand.n00000000a1.status, 'win');
  assert.deepEqual(byCand.n00000000a1.voters, { ana: 'hit', ben: 'miss' });
  assert.deepEqual(byCand.n00000000a2.voters, { ben: 'miss' });
  assert.equal(byCand.n00000000a3.status, 'tie');
  assert.equal(byCand.n00000000a3.key, 'v4');
  assert.deepEqual(s.clusters.get('v1').votes, { ana: 1, ben: -1 });
  // questions: a preview, a pick with the veto, a chosen with overwrote
  assert.equal(s.questions.preview.top3.length, 3);
  assert.equal(s.questions.preview.roundNext, 2);
  assert.equal(s.questions.picked.chosen, 'q_00000001');
  assert.deepEqual(s.questions.picked.vetoed, ['u0000000003']);
  assert.equal(s.questions.chosen.id, 'q_00000001');
  assert.equal(s.questions.chosen.by, 'ana');
  assert.deepEqual(s.questions.chosen.overwrote.map((o) => o.by), ['ben']);
  assert.equal(s.questions.chosen.status, 'applied');
  assert.deepEqual([...s.questions.vetoes.keys()], ['u0000000003'], 'the unveto removed q_00000002');
  // people, run, chat, intents, memory, digests
  assert.deepEqual([...s.people.values()].map((p) => [p.name, p.hue]), [['ana', 'a'], ['ben', 'b']]);
  assert.equal(s.run.round, 2);
  assert.equal(s.run.stepMode, true);
  assert.deepEqual(s.run.pausedBy, []);
  assert.equal(s.intents.get('i1').decision, 'apply');
  assert.equal(s.chat.get('ana')[0].kind, 'chat');
  assert.equal(s.chat.get('ana')[1].kind, 'ack');
  assert.ok(s.chat.get('ben').some((l) => l.kind === 'intent' && l.card.will));
  assert.equal(s.memory.get('choice').length, 2);
  assert.ok(s.digests.length > 10);
  assert.equal(s.digests[0].agent, 'team.loop');
  // the feed: every event except the chat kinds, in seq order
  assert.equal(s.feed.length, LOG.filter((e) => !NOT_IN_FEED.has(e.kind)).length);
  for (let i = 1; i < s.feed.length; i++) assert.ok(s.feed[i].seq > s.feed[i - 1].seq);
  // layout: tree slots for all nodes, a bubble per live cluster, one anchor per island
  assert.equal(s.layout.tree.size, 8);
  assert.equal(s.layout.clusters.size, 7);
  assert.deepEqual([...s.layout.anchors.keys()], ['choice', 'state', 'item_order']);
  assert.match(s.layout.hash, /^[0-9a-f]{8}$/);
  assert.equal(s.layout.hash, hashLayout(s.layout));
});

test('the same log reduced twice gives the same layout hash and the same state hash', () => {
  const a = run(LOG), b = run(LOG);
  assert.equal(a.layout.hash, b.layout.hash);
  assert.equal(hashState(a), hashState(b));
  const c = run(LOG.slice(0, 30));
  assert.notEqual(c.layout.hash, a.layout.hash, 'the hash moves with the layout');
});

test('reduce is pure: the input state never changes', () => {
  const R = makeReducer(trivialLayout);
  let s = R.init();
  for (const e of LOG.slice(0, 120)) {
    const before = { nodes: [...s.nodes], clusters: [...s.clusters], feed: s.feed.slice(), hash: s.layout.hash, head: s.head };
    const next = R.reduce(s, e);
    assert.deepEqual([...s.nodes], before.nodes);
    assert.deepEqual([...s.clusters], before.clusters);
    assert.deepEqual(s.feed, before.feed);
    assert.equal(s.layout.hash, before.hash);
    assert.equal(s.head, before.head);
    s = next;
  }
  assert.equal(R.reduce(s, LOG[5]), s, 'a repeated seq returns the same state');
});

test('the layout passes through the injected functions', () => {
  const calls = { tree: 0, clusters: 0, anchors: [] };
  const R = makeReducer({
    layoutTree: (nodes, firstSeen) => { calls.tree++; assert.ok(nodes instanceof Map && firstSeen instanceof Map); return trivialLayout.layoutTree(nodes, firstSeen); },
    layoutClusters: (prev, island, anchor, bornFrom) => { calls.clusters++; assert.ok(prev instanceof Map && Array.isArray(island) && typeof bornFrom === 'object'); return trivialLayout.layoutClusters(prev, island, anchor); },
    anchorFor: (i, n) => { calls.anchors.push([i, n]); return { x: i * 440, y: 0 }; },
  });
  LOG.reduce((s, e) => R.reduce(s, e), R.init());
  assert.equal(calls.tree, 8, 'once per new node');
  assert.equal(calls.clusters, 4, 'once per cluster_snapshot');
});

test('feed texts equal the contract sentences', () => {
  const { kinds, src } = pythonKinds();
  assert.equal(Object.keys(kinds).length, 37, `parsed 37 kinds from ${src}`);
  for (const [k, v] of Object.entries(kinds)) assert.equal(SENTENCES[k], v.sentence, `sentence of ${k} (from ${src})`);
  assert.deepEqual(Object.keys(SENTENCES).sort(), Object.keys(kinds).sort());
  const s = run(LOG);
  const esc = (t) => t.replace(/[.*+?^$()|[\]\\]/g, '\\$&');
  for (const line of s.feed) {
    const tpl = SENTENCES[line.kind] || FEED_EXTRA[line.kind];
    const re = new RegExp('^' + esc(tpl).replace(/\\?\{\w+\\?\}/g, '(.*)') + '$', 's');
    assert.match(line.text, re, `${line.kind} at ${line.seq}`);
    assert.ok(!/\{\w+\}/.test(line.text), `no open placeholder in ${line.text}`);
  }
  const byseq = Object.fromEntries(s.feed.map((l) => [l.seq, l.text]));
  assert.equal(byseq[12], 'added part "item order" under "bin packing": "how items are sorted before packing"');
  assert.equal(byseq[13], 'is working on part "item order": ideas for item order; do not touch it');
  assert.equal(byseq[15], 'noted: "check tie-breaking before the choice rule"');
  assert.equal(byseq[47], 'test of "best fit" on "bin choice rule": win learn_gap -0.12, learn_z -2.5');
  // a contract.json that carries sentences wins over the built-in table
  const R = makeReducer({ ...trivialLayout, contract: { kinds: { note_posted: { sentence: 'said "{text}"' } } } });
  const t = LOG.slice(0, 15).reduce((st, e) => R.reduce(st, e), R.init());
  assert.equal(t.feed.find((l) => l.kind === 'note_posted').text, 'said "check tie-breaking before the choice rule"');
});

test('one op moves pending, queued, applied (and a dropped add is shown as dropped)', () => {
  const R = makeReducer(trivialLayout);
  let s = upTo(9).reduce((st, e) => R.reduce(st, e), R.init());
  const ev = { kind: 'node_added', by: 'ana', by_kind: 'human', owner: 'ana', op: 'ana-1-9', data: { id: 'order2', name: 'order two', parent: 'root', origin: 'human' } };
  const pending = R.reduce(s, ev);
  assert.equal(pending.nodes.get('order2').status, 'pending');
  assert.equal(chipText(pending.feed.at(-1), pending.run), 'sending');
  s = R.reduce(s, { ...ev, seq: 10 });
  assert.equal(s.nodes.get('order2').status, 'queued');
  assert.equal(chipText(s.feed.at(-1), s.run), 'waits for planned, round 1', 'the loop waits at planned r1');
  assert.equal(R.reduce(s, ev), s, 'the pending copy of a numbered op adds nothing');
  s = R.reduce(s, { seq: 11, kind: 'control_applied', by: 'team.loop', by_kind: 'system', owner: 'team', data: { refs: [10], round: 1, stage: 'planned', dropped: [] } });
  assert.equal(s.nodes.get('order2').status, 'applied');
  assert.equal(chipText(s.feed.find((l) => l.seq === 10), s.run), 'applied in round 1, stage planned');
  s = R.reduce(s, { seq: 12, kind: 'node_added', by: 'ben', by_kind: 'human', owner: 'ben', op: 'ben-1-1', data: { id: 'x2', name: 'x', parent: 'root', origin: 'human' } });
  s = R.reduce(s, { seq: 13, kind: 'control_applied', by: 'team.loop', by_kind: 'system', owner: 'team', data: { refs: [], round: 1, stage: 'ideated', dropped: [{ seq: 12, reason: 'id_taken' }] } });
  assert.equal(s.nodes.get('x2').status, 'rejected');
  assert.equal(chipText(s.feed.find((l) => l.seq === 12), s.run), 'dropped: id in use');
});

test('a veto stays "acts at the next pick" until question_picked lists it', () => {
  const vetoSeq = seqOf((e) => e.kind === 'question_vetoed');
  const pickSeq = seqOf((e) => e.kind === 'question_picked');
  const R = makeReducer(trivialLayout);
  let s = R.init();
  for (const e of LOG) {
    if (e.seq > pickSeq) break;
    s = R.reduce(s, e);
    if (e.seq >= vetoSeq && e.seq < pickSeq) {
      const v = s.questions.vetoes.get('u0000000003')[0];
      assert.equal(v.status, 'queued', `still queued at ${e.seq} (${e.kind})`);
      assert.equal(chipText(v, s.run), 'acts at the next pick, round 2');
      assert.equal(chipText(s.feed.find((l) => l.seq === vetoSeq), s.run), 'acts at the next pick, round 2');
    }
  }
  const v = s.questions.vetoes.get('u0000000003')[0];
  assert.equal(v.status, 'applied');
  assert.equal(chipText(v, s.run), 'applied at the pick of round 1');
  // Ben's earlier choice was replaced by Ana's, then the pick took Ana's
  const benChoice = s.feed.find((l) => l.kind === 'question_chosen' && l.owner === 'ben');
  assert.equal(chipText(benChoice, s.run), `replaced by Ana's choice at #${benChoice.seq + 1}`);
  assert.equal(chipText(s.questions.chosen, s.run), 'applied at the pick of round 1');
  // a choice that is not in the top 3 at the pick says so
  const R2 = makeReducer(trivialLayout);
  let t = LOG.filter((e) => e.seq < pickSeq && !(e.kind === 'question_chosen' && e.owner === 'ana')).reduce((st, e) => R2.reduce(st, e), R2.init());
  t = R2.reduce(t, { seq: 900, kind: 'question_chosen', by: 'ana', by_kind: 'human', owner: 'ana', data: { question: 'u0000000009', text: 'far away' } });
  t = R2.reduce(t, { ...LOG[pickSeq - 1], seq: 901 });
  assert.equal(chipText(t.questions.chosen, t.run), 'not in the top 3 at the pick of round 1');
});

test('chip texts of section 4.7 and the next boundary', () => {
  assert.deepEqual(nextBoundary({ round: 0, stage: null }), { stage: 'planned', round: 1 });
  assert.deepEqual(nextBoundary({ round: 1, stage: 'planned', waiting: true }), { stage: 'planned', round: 1 });
  assert.deepEqual(nextBoundary({ round: 3, stage: 'deepened', waiting: false }), { stage: 'built', round: 3 });
  assert.deepEqual(nextBoundary({ round: 3, stage: 'verified', waiting: false }), { stage: 'ideated', round: 4 });
  const run = { round: 3, stage: 'deepened', waiting: false };
  assert.equal(chipText({ status: 'pending', kind: 'note_posted' }, run), 'sending');
  assert.equal(chipText({ status: 'queued', kind: 'seed_added' }, run), 'waits for built, round 3');
  assert.equal(chipText({ status: 'queued', kind: 'question_vetoed' }, run), 'acts at the next pick, round 4');
  assert.equal(chipText({ status: 'queued', kind: 'question_chosen' }, run), 'acts at the next pick, round 4');
  assert.equal(chipText({ status: 'applied', kind: 'node_skipped', appliedAt: { round: 3, stage: 'built' } }, run), 'applied in round 3, stage built');
  assert.equal(chipText({ status: 'applied', kind: 'question_vetoed', pickRound: 3 }, run), 'applied at the pick of round 3');
  assert.equal(chipText({ status: 'rejected', reason: 'id_taken' }, run), 'dropped: id in use');
  assert.equal(chipText({ status: 'rejected', reason: 'bad_envelope' }, run), 'rejected: bad_envelope');
});

test('who wrote it, bursts, quotes', () => {
  assert.equal(whoText({ cls: 'person', owner: 'ana' }), 'Ana');
  assert.equal(whoText({ cls: 'delegate', owner: 'ben' }), 'Ben via agent');
  assert.equal(whoText({ cls: 'team', owner: 'team' }), 'the team');
  const g = groupFeed([{ seq: 1, by: 'team.loop', kind: 'sketch_batch', node: 'a' }, { seq: 2, by: 'team.loop', kind: 'sketch_batch', node: 'a' },
    { seq: 3, by: 'ana', kind: 'note_posted', node: null }, { seq: 4, by: 'ana', kind: 'note_posted', node: null }]);
  assert.deepEqual(g.map((x) => [x.seq, x.count]), [[2, 2], [3, 1], [4, 1]]);
  assert.equal(q('<b>hi</b>\n  there'), 'hi there');
  assert.equal(q('x'.repeat(200)).length, 160);
});

test('private keys never reach the view state', () => {
  const R = makeReducer(trivialLayout);
  let s = LOG.slice(0, 25).reduce((st, e) => R.reduce(st, e), R.init());
  s = R.reduce(s, { seq: 26, kind: 'cluster_snapshot', by: 'team.loop', by_kind: 'system', owner: 'team', data: { node: 'open', direction: 'inward', round: 1,
    clusters: [{ cluster_id: 'open-in-k00', name: 'lazy', members: ['sx1'], n: 1, obvious: true, obvious_match: 'first answers' }] } });
  const json = JSON.stringify([...s.clusters.values()]);
  assert.ok(!json.includes('obvious'));
});
