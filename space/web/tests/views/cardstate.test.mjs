// cardState: the documented classes and exact chip texts for all 13 states (docs/MULTIPLAYER_DESIGN.md 6.6).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { cardState, nextBoundary, hueOf, initialOf, STAGES } from '../../cardstate.mjs';

const people = new Map([['ana', { name: 'ana', hue: 'a', firstSeen: 3 }], ['ben', { name: 'ben', hue: 'b', firstSeen: 9 }]]);
const run = (stage, round = 1, waiting = false) => ({ round, stage, waiting, stepMode: true, pausedBy: [], mode: 'check_only' });
const base = { id: 'choice', name: 'choice rule', parent: 'root', kind: 'part', origin: 'map', by: 'team.loop', owner: 'team', seq: 12, status: 'map', disputed: [], claim: null, lowered: false, skippedBy: null };
const chips = (st) => st.chips.map((c) => c.text);
const icons = (st) => st.chips.map((c) => c.icon);

const TABLE = [
  ['1 planned part', { ...base }, run('planned'), ['card--map'], [], []],
  ['2 human part, pending', { ...base, origin: 'human', owner: 'ana', status: 'pending' }, run('planned'), ['card--human', 'card--pending'], ['sending'], ['clock']],
  ['3 human part, queued', { ...base, origin: 'human', owner: 'ana', status: 'queued' }, run('clustered', 4), ['card--human', 'card--queued'], ['waits for deepened, round 4'], ['clock']],
  ['4 human part, applied', { ...base, origin: 'human', owner: 'ana', status: 'applied', appliedAt: { round: 3, stage: 'built', seq: 90 } }, run('built', 3), ['card--human', 'card--applied'], ['applied in round 3, stage built'], ['check']],
  ['5 dropped', { ...base, origin: 'human', owner: 'ben', status: 'rejected', reason: 'id_taken' }, run('planned'), ['card--human', 'card--dropped'], ['dropped: id in use'], ['x']],
  ['6 failure question', { ...base, id: 'q_n44a9d66', kind: 'question', origin: 'failure', failsIf: 'the gap stays above the margin', test: { metric: 'learn_gap', op: '<=', rung: 2 }, threshold: 0.0367 }, run('verified'), ['card--question'], ['fails if the gap stays above the margin', 'test: learn_gap <= 0.0367'], ['flask', 'flask']],
  ['7 off-map win', { ...base, id: 'win_1', kind: 'win', origin: 'offtree' }, run('verified'), ['card--win'], ['won off the map'], ['trophy']],
  ['8 disputed', { ...base, disputed: [{ by: 'ana', reason: 'best fit beat it on seed 0', tag: 'measured', seq: 42 }] }, run('ideated'), ['card--map', 'card--disputed'], ['disputed by ana: best fit beat it on seed 0 (measured)'], ['flag']],
  ['9 skipped', { ...base, skippedBy: 'ben' }, run('ideated'), ['card--map', 'card--skipped'], ['skipped by B'], ['pause']],
  ['10 lowered', { ...base, lowered: true }, run('ideated'), ['card--map', 'card--lowered'], ['lowered'], ['arrow-down']],
];

for (const [name, node, r, classes, texts, ics] of TABLE) {
  test(`state ${name}`, () => {
    const st = cardState(node, r, 'ana', { people, nowMs: 0 });
    for (const c of classes) assert.ok(st.classes.includes(c), `${name}: missing class ${c} in ${st.classes}`);
    assert.deepEqual(chips(st), texts);
    assert.deepEqual(icons(st), ics);
    if (!name.startsWith('11') && !name.startsWith('12')) assert.equal(st.ring, null);
  });
}

test('state 3 queued: the chip names the boundary the loop folds at', () => {
  const node = { ...base, origin: 'human', owner: 'ana', status: 'queued' };
  // the loop waits at planned r1 (step mode): "waits for planned, round 1" as on the screen of section 2
  assert.deepEqual(chips(cardState(node, run('planned', 1, true), 'ana')), ['waits for planned, round 1']);
  // the loop is running the stage after planned: the next boundary is ideated
  assert.deepEqual(chips(cardState(node, run('planned', 1), 'ana')), ['waits for ideated, round 1']);
  assert.deepEqual(chips(cardState(node, run('clustered', 4), 'ana')), ['waits for deepened, round 4']);
  // before the loop starts: planned, round 1; after verified: ideated of the next round
  assert.deepEqual(chips(cardState(node, { round: 0, stage: null }, 'ana')), ['waits for planned, round 1']);
  assert.deepEqual(chips(cardState(node, null, 'ana')), ['waits for planned, round 1']);
  assert.deepEqual(chips(cardState(node, run('verified', 2), 'ana')), ['waits for ideated, round 3']);
  assert.deepEqual(nextBoundary(run('built', 5)), { stage: 'verified', round: 5 });
  assert.deepEqual(STAGES, ['planned', 'ideated', 'clustered', 'deepened', 'built', 'verified']);
});

test('state 5 rejected with another error says rejected: {error}', () => {
  const st = cardState({ ...base, origin: 'human', owner: 'ben', status: 'rejected', reason: 'bad_parent' }, run('planned'), 'ana');
  assert.deepEqual(chips(st), ['rejected: bad_parent']);
  assert.ok(st.classes.includes('card--dropped'));
});

test('state 11 claimed: ring in the holder owner hue, tag "{holder} {secondsLeft} s" from server time, lock icon', () => {
  const node = { ...base, claim: { holder: 'ana.agent', owner: 'ana', token: 44, untilMs: 100000 + 89000 } };
  const st = cardState(node, run('planned'), 'ben', { people, nowMs: 100000 });
  assert.ok(st.classes.includes('card--claimed'));
  assert.deepEqual(st.ring, { kind: 'claim', hue: 'a', holder: 'ana.agent', tag: 'ana.agent 89 s', icon: 'lock', focus: [] });
  assert.deepEqual(chips(st), []);
  const late = cardState(node, run('planned'), 'ben', { people, nowMs: 100000 + 88600 });
  assert.equal(late.ring.tag, 'ana.agent 1 s');
  const over = cardState(node, run('planned'), 'ben', { people, nowMs: 100000 + 95000 });
  assert.equal(over.ring.tag, 'ana.agent 0 s');
});

test('state 12 focus: ring with a name tag per person', () => {
  const st = cardState({ ...base }, run('planned'), 'ana', { people, focus: [{ name: 'ben' }, { name: 'cy', hue: 'c' }] });
  assert.ok(st.classes.includes('card--focused'));
  assert.deepEqual(chips(st), []);
  assert.equal(st.ring.kind, 'focus');
  assert.deepEqual(st.ring.focus, [{ name: 'ben', hue: 'b' }, { name: 'cy', hue: 'c' }]);
  // a claim and a focus share the ring: the claim gives the hue and the tag, the focus adds the names
  const both = cardState({ ...base, claim: { holder: 'ben.agent', owner: 'ben', untilMs: 5000 } }, run('planned'), 'ana', { people, nowMs: 0, focus: [{ name: 'ben' }] });
  assert.equal(both.ring.kind, 'claim');
  assert.equal(both.ring.tag, 'ben.agent 5 s');
  assert.deepEqual(both.ring.focus, [{ name: 'ben', hue: 'b' }]);
});

test('state 13 since you looked: card--unseen dot when seq is greater than the last-seen seq, no chip', () => {
  const st = cardState({ ...base, seq: 50 }, run('planned'), 'ana', { lastSeenSeq: 40 });
  assert.ok(st.classes.includes('card--unseen'));
  assert.equal(st.dot, true);
  assert.deepEqual(chips(st), []);
  const seen = cardState({ ...base, seq: 50 }, run('planned'), 'ana', { lastSeenSeq: 50 });
  assert.ok(!seen.classes.includes('card--unseen'));
  assert.equal(seen.dot, false);
  const noCtx = cardState({ ...base, seq: 50 }, run('planned'), 'ana');
  assert.ok(!noCtx.classes.includes('card--unseen'));
});

test('states add up: a skipped, lowered, disputed human part keeps every class and chip', () => {
  const node = { ...base, origin: 'human', owner: 'ana', status: 'applied', appliedAt: { round: 1, stage: 'planned' }, skippedBy: 'ana', lowered: true,
                 disputed: [{ by: 'ben', reason: 'wrong', tag: 'belief', seq: 7 }] };
  const st = cardState(node, run('ideated'), 'ana', { people });
  for (const c of ['card--human', 'card--applied', 'card--disputed', 'card--skipped', 'card--lowered', 'card--mine']) assert.ok(st.classes.includes(c), c);
  assert.deepEqual(chips(st), ['applied in round 1, stage planned', 'disputed by ben: wrong (belief)', 'skipped by A', 'lowered']);
  assert.equal(st.hue, 'a');
});

test('hues and initials', () => {
  assert.equal(hueOf('ana', people), 'a');
  assert.equal(hueOf('ana.agent', people), 'a');
  assert.equal(hueOf('ben', people), 'b');
  assert.equal(hueOf('team.loop', people), 'team');
  assert.equal(hueOf('team', people), 'team');
  assert.equal(hueOf('nobody', people), 'team');
  assert.equal(hueOf(null, people), 'team');
  assert.equal(initialOf('ben.agent'), 'B');
  assert.equal(initialOf(''), '?');
  const plain = cardState({ ...base, owner: 'ben' }, run('planned'), 'ana', { people: { ben: { hue: 'b' } } });
  assert.equal(plain.hue, 'b');
});
