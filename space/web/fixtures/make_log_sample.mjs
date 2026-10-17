// make_log_sample.mjs: writes fixtures/log_sample.ndjson, a synthetic 300-event log that covers every day-one
// kind of contract.json. Deterministic (no clock, no random). Run: node space/web/fixtures/make_log_sample.mjs
// The story: the loop plans 7 parts; Ana adds "item order" at planned r1 and her agent claims it; Ben notes and
// presses Go; round 1 ideates, clusters, regroups "choice" (one cluster born, one dead), argues, builds, tests;
// people vote (hit and miss), veto and choose (Ana's choice overwrites Ben's); the pick for round 2 lists the veto.
// Round 2 fills the rest with sketches, digests and agent lines until the log holds exactly 300 events.

import { writeFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

export const TOTAL = 300;
const T0 = Date.UTC(2026, 9, 17, 14, 0, 0);
const START_MS = 1760709600000;

export function buildLog() {
  const out = [];
  const opn = new Map();
  const sk = (i) => 's' + i.toString(16).padStart(10, '0');
  const KIND = { ana: 'human', ben: 'human', 'ana.agent': 'agent', 'ben.agent': 'agent', 'team.loop': 'system', server: 'system' };
  function ev(by, kind, data, extra = {}) {
    const seq = out.length + 1;
    const owner = by === 'server' ? 'server' : by.startsWith('team.') ? 'team' : by.split('.')[0];
    const e = { seq, ts: new Date(T0 + seq * 1000).toISOString(), kind, by, by_kind: KIND[by], owner,
      subject: null, label: null, data, op: null, base: null, round: null, stage: null, claim: null, cause: null, ...extra };
    if (by !== 'server' && !by.startsWith('team.')) { const n = (opn.get(by) || 0) + 1; opn.set(by, n); e.op = `${by}-${START_MS}-${n}`; }
    out.push(e);
    return seq;
  }
  const team = (kind, data, extra) => ev('team.loop', kind, data, extra);
  const stage = (round, st, waiting = true) => team('stage_entered', { round, stage: st, waiting, step_mode: true }, { round, stage: st });
  const digest = (by, role, from, to, round, st, text) => ev(by, 'digest_taken',
    { from_seq: from, to_seq: to, n: to - from + 1, chars: text.length, role, text }, { round, stage: st });

  // ---- open, plan
  ev('server', 'space_opened', { space_id: 'binpack', epoch: '4f2a9c1e' });
  team('node_added', { id: 'root', name: 'bin packing', parent: null, origin: 'map', kind: 'root', frame: 'pack items into bins' });
  const parts = [['choice', 'bin choice rule'], ['state', 'bin state'], ['open', 'opening bins'], ['stats', 'item statistics'],
    ['ties', 'tie breaking'], ['recipe', 'packing recipe']];
  for (const [id, name] of parts) team('node_added', { id, name, parent: 'root', origin: 'map', frame: `how ${name} works today`, directions: ['inward', 'outward'] });
  stage(1, 'planned');
  // Ana adds a part through chat; her agent acks and adds it, then claims it
  const chat1 = ev('ana', 'chat_posted', { to: 'ana.agent', text: '/branch root "item order": how items are sorted before packing --claim', shared: true });
  ev('ana.agent', 'agent_said', { kind: 'ack', text: 'Got it. I add "item order" under root.', canned: false }, { cause: chat1 });
  const itemOrder = ev('ana.agent', 'node_added', { id: 'item_order', name: 'item order', parent: 'root', origin: 'human',
    frame: 'how items are sorted before packing', assumptions: [], directions: ['inward', 'outward'] }, { cause: chat1, subject: 'node:item_order' });
  ev('server', 'claim_granted', { owner: 'ana.agent', ttl_s: 90, purpose: 'ideas for item order' }, { subject: 'node:item_order' });
  ev('ben.agent', 'agent_said', { kind: 'peer', text: 'Ana added item order. I carry it to the inventors at planned r1.', canned: false }, { cause: itemOrder });
  const note1 = ev('ben', 'note_posted', { text: 'check tie-breaking before the choice rule' });
  const seed1 = ev('ana', 'seed_added', { node: 'item_order', text: 'sort items by size, largest first' });
  const op1 = ev('ben', 'opinion_given', { target: 'choice', score: 7, note: 'fair and cheap' });
  const step1 = ev('ben', 'run_step', { round: 1, stage: 'planned' });
  team('control_applied', { refs: [itemOrder, note1, seed1, op1, step1], round: 1, stage: 'planned',
    keys: { add_nodes: ['item_order'], skip_nodes: [], veto: [], choose: null, notes: 1, opinions: 1, pause: false, disputes: 0 }, dropped: [] }, { round: 1, stage: 'planned' });
  digest('team.loop', 'planner', itemOrder, step1, 1, 'planned', 'WHAT TEAMMATES CHANGED SINCE YOUR LAST STEP (events e10 to e15).');
  // ---- ideated r1
  stage(1, 'ideated');
  let s = 1;
  const items = (n, card = 'seeded') => Array.from({ length: n }, () => ({ id: sk(s++), idea: `idea ${s}`, card, kind: '' }));
  const choiceIn = items(10);                                          // s1..s10
  team('sketch_batch', { node: 'choice', direction: 'inward', round: 1, count: 10, items: choiceIn }, { round: 1, stage: 'ideated' });
  const orderIn = items(4, 'owner');                                    // s11..s14 from Ana's seed
  team('sketch_batch', { node: 'item_order', direction: 'inward', round: 1, count: 4, items: orderIn }, { round: 1, stage: 'ideated' });
  const stateIn = items(5);                                             // s15..s19
  team('sketch_batch', { node: 'state', direction: 'inward', round: 1, count: 5, items: stateIn }, { round: 1, stage: 'ideated' });
  const ids = (arr, a, b) => arr.slice(a, b).map((x) => x.id);
  // ---- clustered r1: first grouping
  stage(1, 'clustered');
  const A = ids(choiceIn, 0, 4), B = ids(choiceIn, 4, 8), C = ids(choiceIn, 8, 10);
  team('cluster_snapshot', { node: 'choice', direction: 'inward', round: 1, stage: 'clustered', clusters: [
    { cluster_id: 'choice-in-k00', name: 'best fit', members: A, n: 4, rank: 0, score: 0.9, selected: true, lane: 'main', prior: 'known' },
    { cluster_id: 'choice-in-k01', name: 'worst fit', members: B, n: 4, rank: 1, score: 0.6, selected: true, lane: 'main', prior: 'new' },
    { cluster_id: 'choice-in-k02', name: 'harmonic', members: C, n: 2, rank: 2, score: 0.3, selected: false, lane: null, prior: 'failed' }] }, { round: 1, stage: 'clustered' });
  team('cluster_snapshot', { node: 'item_order', direction: 'inward', round: 1, stage: 'clustered', clusters: [
    { cluster_id: 'item_order-in-k00', name: 'largest first', members: ids(orderIn, 0, 3), n: 3, rank: 0, score: 0.8, selected: true, lane: 'main', prior: 'known' },
    { cluster_id: 'item_order-in-k01', name: 'random order', members: ids(orderIn, 3, 4), n: 1, rank: 1, score: 0.2, selected: false, lane: null, prior: 'new' }] }, { round: 1, stage: 'clustered' });
  team('cluster_snapshot', { node: 'state', direction: 'inward', round: 1, stage: 'clustered', clusters: [
    { cluster_id: 'state-in-k00', name: 'residual list', members: ids(stateIn, 0, 3), n: 3, rank: 0, score: 0.7, selected: false, lane: null, prior: 'new' },
    { cluster_id: 'state-in-k01', name: 'segment tree', members: ids(stateIn, 3, 5), n: 2, rank: 1, score: 0.5, selected: false, lane: null, prior: 'known' }] }, { round: 1, stage: 'clustered' });
  // votes on the first grouping (keys v1 best fit, v2 worst fit, v3 harmonic)
  ev('ana', 'vote_cast', { idea: 'v1', value: 1 });
  ev('ben', 'vote_cast', { idea: 'v1', value: -1 });
  ev('ben.agent', 'vote_cast', { idea: 'v2', value: 1 });
  // the regrouping: best fit grows and absorbs harmonic (dead), worst fit splits (one born)
  const extra = items(3);                                               // s20..s22
  team('sketch_batch', { node: 'choice', direction: 'inward', round: 1, count: 3, items: extra }, { round: 1, stage: 'clustered' });
  team('cluster_snapshot', { node: 'choice', direction: 'inward', round: 1, stage: 'clustered', clusters: [
    { cluster_id: 'choice-in-k00', name: 'worst fit', members: B.slice(0, 3), n: 3, rank: 1, score: 0.6, selected: true, lane: 'main', prior: 'new' },
    { cluster_id: 'choice-in-k01', name: 'best fit', members: [...A, ...C, extra[0].id], n: 7, rank: 0, score: 0.95, selected: true, lane: 'main', prior: 'known' },
    { cluster_id: 'choice-in-k02', name: 'almost worst fit', members: [B[3], extra[1].id, extra[2].id], n: 3, rank: 2, score: 0.4, selected: false, lane: null, prior: 'new' }] }, { round: 1, stage: 'clustered' });
  // ---- deepened r1: arguments on best fit (k01 now)
  stage(1, 'deepened');
  team('objection_raised', { node: 'choice', idea: 'choice-in-k01', members: [...A, ...C, extra[0].id], objection: 1, cls: 'hidden_cost', severity: 'high',
    text: 'scanning every bin costs O(n) per item', if_true: { metric: 'cost_ratio', op: 'above', threshold: 1.5 } }, { round: 1, stage: 'deepened' });
  team('objection_raised', { node: 'choice', idea: 'choice-in-k01', members: [...A, ...C, extra[0].id], objection: 2, cls: 'below_noise', severity: 'medium',
    text: 'the gain is below the noise of the quick check', if_true: null }, { round: 1, stage: 'deepened' });
  team('reply_posted', { node: 'choice', idea: 'choice-in-k01', members: [...A, ...C, extra[0].id], objection: 1, kind: 'measure',
    text: 'a sorted tree of residuals keeps it at O(log n)', fact: 'O(log n) per insert', source: 'script', test: 'cost_ratio below 1.2', change: null }, { round: 1, stage: 'deepened' });
  ev('ana', 'reply_posted', { node: 'choice', idea: 'choice-in-k01', objection: 2, kind: 'rebut', text: 'best fit beat it on seed 0 by 3 bins', fact: '3 bins on seed 0', source: 'measured', test: null, change: null });
  team('objection_marked', { node: 'choice', idea: 'choice-in-k01', objection: 1, verdict: 'resolved', reason: 'measured' }, { round: 1, stage: 'deepened' });
  team('objection_marked', { node: 'choice', idea: 'choice-in-k01', objection: 2, verdict: 'standing', reason: 'no measurement yet' }, { round: 1, stage: 'deepened' });
  const disp1 = ev('ben', 'fact_disputed', { node: 'choice', fact: 'the first open bin is always best', reason: 'best fit beat it on seed 0', tag: 'measured', ref: 'e40' });
  // ---- built r1
  stage(1, 'built');
  team('candidate_built', { node: 'choice', cand: 'n00000000a1', idea: 'choice-in-k01', cluster_name: 'best fit', members: [...A, ...C, extra[0].id],
    lane: 'main', hypothesis: 'best fit with a residual tree', round: 1 }, { round: 1, stage: 'built' });
  team('candidate_built', { node: 'choice', cand: 'n00000000a2', idea: 'choice-in-k00', cluster_name: 'worst fit', members: B.slice(0, 3),
    lane: 'main', hypothesis: 'worst fit keeps room', round: 1 }, { round: 1, stage: 'built' });
  team('candidate_built', { node: 'item_order', cand: 'n00000000a3', idea: 'item_order-in-k00', cluster_name: 'largest first', members: ids(orderIn, 0, 3),
    lane: 'main', hypothesis: 'sort items largest first', round: 1 }, { round: 1, stage: 'built' });
  // ---- verified r1
  stage(1, 'verified');
  team('test_result', { node: 'choice', cand: 'n00000000a1', idea: 'choice-in-k01', status: 'win', rung: 3, metrics: { learn_gap: -0.123, learn_z: -2.5, cost: 3 }, reason: null, reference: false }, { round: 1, stage: 'verified' });
  team('test_result', { node: 'choice', cand: 'n00000000a2', idea: 'choice-in-k00', status: 'loss', rung: 2, metrics: { learn_gap: 0.4, learn_z: 1.1 }, reason: null, reference: false }, { round: 1, stage: 'verified' });
  team('test_result', { node: 'item_order', cand: 'n00000000a3', idea: 'item_order-in-k00', status: 'tie', rung: 2, metrics: {}, reason: 'within noise', reference: false }, { round: 1, stage: 'verified' });
  team('memory_added', { node: 'choice', round: 1, added: [
    { id: 'm000a01', section: 'FACTS', source: 'measured', text: 'best fit with a residual tree wins on seed 0 (n00000000a1)' },
    { id: 'm000a02', section: 'TRIED', source: 'measured', text: 'worst fit loses by 0.4 (n00000000a2)' }], rejected: 1, archived: 0 }, { round: 1, stage: 'verified' });
  team('question_preview', { round_next: 2, top3: [
    { id: 'q_00000001', kind: 'question', text: 'does item order matter for best fit?', node: 'item_order', score: 0.8, reason: 'open', requires_human: false },
    { id: 'q_00000002', kind: 'question', text: 'is the residual tree worth its cost?', node: 'choice', score: 0.6, reason: 'cost', requires_human: false },
    { id: 'u0000000003', kind: 'upward', text: 'measure bins used, not time', node: 'root', score: 0.4, reason: 'measure', requires_human: true }],
    explore: null, n_candidates: 5 }, { round: 1, stage: 'verified' });
  const veto = ev('ana', 'question_vetoed', { question: 'u0000000003', text: 'measure bins used, not time' }, { subject: 'question:u0000000003' });
  ev('ben', 'question_vetoed', { question: 'q_00000002', text: 'is the residual tree worth its cost?' }, { subject: 'question:q_00000002' });
  ev('ben', 'question_unvetoed', { question: 'q_00000002', text: 'is the residual tree worth its cost?' }, { subject: 'question:q_00000002' });
  const benChoice = ev('ben', 'question_chosen', { question: 'q_00000002', text: 'is the residual tree worth its cost?', overwrote: [] }, { subject: 'question:q_00000002' });
  ev('ana', 'question_chosen', { question: 'q_00000001', text: 'does item order matter for best fit?', overwrote: [{ field: 'choose', seq: benChoice, by: 'ben' }] },
    { subject: 'question:q_00000001', base: benChoice - 1 });
  // a pause by Ana with a resume, a skip with a restore, an edit, a claim handover
  const pause1 = ev('ana', 'run_paused', { reason: 'look at the result' });
  ev('ana', 'run_resumed', { reason: 'done' });
  const skip = ev('ben', 'node_skipped', { reason: 'not now' }, { subject: 'node:stats' });
  ev('ben', 'node_unskipped', { reason: 'back on' }, { subject: 'node:stats' });
  ev('ana', 'node_edited', { fields: { name: 'item order rule', priority: 'normal' }, overwrote: [] }, { subject: 'node:item_order' });
  ev('server', 'claim_taken_over', { from: 'ana.agent', to: 'ben' }, { subject: 'node:item_order' });
  ev('server', 'claim_released', { owner: 'ben' }, { subject: 'node:item_order' });
  ev('server', 'claim_granted', { owner: 'ben.agent', ttl_s: 90, purpose: 'ties' }, { subject: 'node:ties' });
  ev('server', 'claim_expired', { owner_was: 'ben.agent', reason: 'ttl' }, { subject: 'node:ties' });
  // an intent card (a dispute needs OK) and its decision
  const chat2 = ev('ben', 'chat_posted', { to: 'ben.agent', text: 'I doubt the tie rule fact', shared: true });
  ev('ben.agent', 'agent_said', { kind: 'reply', text: 'I can mark it disputed. Apply?', canned: true }, { cause: chat2 });
  ev('ben.agent', 'intent_proposed', { intent_id: 'i1', action: { type: 'dispute_fact', fact: 'ties never matter', reason: 'seed 3 differs', evidence_tag: 'belief', evidence_ref: '' },
    card: { will: 'mark "ties never matter" as disputed', on: 'ties', because: 'Ben doubts it (event ' + chat2 + ')', apply_at: 'at once' } }, { cause: chat2 });
  ev('ben', 'intent_decided', { intent_id: 'i1', decision: 'apply', action: { type: 'dispute_fact', fact: 'ties never matter', reason: 'seed 3 differs', evidence_tag: 'belief', evidence_ref: '' } });
  const disp2 = ev('ben.agent', 'fact_disputed', { node: 'ties', fact: 'ties never matter', reason: 'seed 3 differs', tag: 'belief', ref: '' }, { cause: chat2 });
  // the pick for round 2 (the loop's pick record names the round it picks for) lists Ana's veto and takes Ana's choice
  const step2 = ev('ana', 'run_step', { round: 1, stage: 'verified' });
  team('question_picked', { round: 2, top3: [{ id: 'q_00000001', kind: 'question', text: 'does item order matter for best fit?', score: 0.8 },
    { id: 'q_00000002', kind: 'question', text: 'is the residual tree worth its cost?', score: 0.6 }],
  chosen: 'q_00000001', by: 'person', vetoed: ['u0000000003'] }, { round: 1, stage: 'verified' });
  team('control_applied', { refs: [disp1, pause1, pause1 + 1, skip, skip + 1, disp2, step2], round: 1, stage: 'verified',
    keys: { add_nodes: [], skip_nodes: [], veto: ['u0000000003'], choose: 'q_00000001', notes: 0, opinions: 0, pause: false, disputes: 2 }, dropped: [] }, { round: 1, stage: 'verified' });
  digest('ana.agent', 'person', veto, step2, 1, 'verified', 'WHAT TEAMMATES CHANGED SINCE YOUR LAST STEP (events e60 to e80).');
  // ---- round 2: filler until 300 (sketches on the other parts, stage boundaries with digests and peer lines)
  const fillParts = ['state', 'open', 'stats', 'ties', 'recipe', 'item_order', 'choice'];
  const stages = ['planned', 'ideated', 'clustered', 'deepened', 'built', 'verified'];
  let k = 0;
  while (out.length < TOTAL) {
    const st = stages[Math.floor(k / 8) % stages.length];
    const j = k % 4;
    if (k % 8 === 0 && out.length < TOTAL) stage(2, st);
    else if (j === 1) team('sketch_batch', { node: fillParts[k % fillParts.length], direction: k % 3 ? 'inward' : 'outward', round: 2, count: 2, items: items(2) }, { round: 2, stage: st });
    else if (j === 2) ev(k % 2 ? 'ana.agent' : 'ben.agent', 'agent_said', { kind: 'peer', text: `peer line ${k}`, canned: false });
    else digest('team.loop', 'builder', Math.max(1, out.length - 5), out.length, 2, st, `digest ${k}`);
    k++;
  }
  return out;
}

if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const here = dirname(fileURLToPath(import.meta.url));
  const log = buildLog();
  writeFileSync(join(here, 'log_sample.ndjson'), log.map((e) => JSON.stringify(e)).join('\n') + '\n');
  console.log(`wrote ${log.length} events`);
}
