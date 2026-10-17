// Review fixes (P5 review): defects found against the design and against the shapes the page shell passes.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { installDom } from './helpers/dom_stub.mjs';
import './helpers/d3.mjs';
import { mountTree, CARD_W, CARD_H, DEEP_W, DEEP_H } from '../../tree.js';
import { mountClusters } from '../../clusters.js';
import { clock } from '../../motion.mjs';
import { ROW_H, COL_W } from '../../layout.mjs';

const here = dirname(fileURLToPath(import.meta.url));
installDom();

const bus = () => ({ handlers: {}, on(n, f) { (this.handlers[n] = this.handlers[n] || []).push(f); }, emit(n, p) { (this.handlers[n] || []).forEach((f) => f(p)); } });
const cl = (key, node, n, extra = {}) => ({ key, node, direction: 'inward', name: key, members: Array.from({ length: n }, (_, i) => `${key}s${i}`), n,
  prior: 'new', contributors: { team: n }, votes: {}, status: 'open', ...extra });
const baseState = (clusters) => ({
  run: { round: 1, stage: 'clustered', waiting: false, mode: 'check_only' }, people: new Map(),
  nodes: new Map([['root', { id: 'root', name: 'root', parent: null, origin: 'map', status: 'map', seq: 1 }],
                  ['choice', { id: 'choice', name: 'choice', parent: 'root', origin: 'map', status: 'map', seq: 2 }]]),
  clusters: new Map(clusters.map((c) => [c.key, c])),
  layout: { tree: new Map(), clusters: new Map(), anchors: new Map(), hash: '00000000' }, presence: { clients: [], claims: [] }, results: [],
});

test('bubbles of a fresh island are visible: no bubble keeps is-arriving after the first paint', () => {
  const state = baseState([cl('v1', 'choice', 3), cl('v2', 'choice', 4)]);
  const view = mountClusters(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { contract: { winner_word: {} } });
  for (const b of view.bubbles.values()) assert.ok(!b.el.classList.contains('is-arriving'), `${b.key} stays invisible (is-arriving)`);
  view.destroy();
});

test('a bubble that arrives in an existing island turns visible when its staged grow starts', () => {
  let state = baseState([cl('v1', 'choice', 3)]);
  const view = mountClusters(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { contract: { winner_word: {} } });
  state = { ...state, clusters: new Map([...state.clusters, ['v2', cl('v2', 'choice', 2)]]) };
  view.update(true);
  const b2 = view.bubbles.get('v2');
  assert.ok(b2.el.classList.contains('is-arriving'), 'waits for the staged relayout');
  clock.frame(performance.now() + 5000);
  assert.ok(!b2.el.classList.contains('is-arriving'), 'visible once it grows');
  view.destroy();
});

test('a merge flies into the survivor when the reducer moved the dead cluster to state.retired', () => {
  let state = baseState([cl('v1', 'choice', 3), cl('v2', 'choice', 4)]);
  const view = mountClusters(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { contract: { winner_word: {} } });
  clock.snap();
  const b1 = view.bubbles.get('v1'), b2 = view.bubbles.get('v2');
  state = { ...state, clusters: new Map([['v1', cl('v1', 'choice', 7)]]), retired: new Map([['v2', { ...cl('v2', 'choice', 4), mergedInto: 'v1' }]]) };
  view.update(true);
  assert.ok(b2.retiring);
  assert.equal(b2.tx, b1.x, 'flies to the survivor (x)');
  assert.equal(b2.ty, b1.y, 'flies to the survivor (y)');
  view.destroy();
});

test('edges attach to the drawn card size: deep cards are smaller', () => {
  const nodes = new Map();
  const chain = ['root', 'a', 'b', 'c', 'd'];
  chain.forEach((id, i) => nodes.set(id, { id, name: id, parent: i ? chain[i - 1] : null, origin: 'map', status: 'map', seq: i + 1 }));
  const state = { run: null, people: new Map(), nodes, clusters: new Map(), layout: { tree: new Map(), clusters: new Map(), anchors: new Map() }, presence: { clients: [] } };
  const tree = mountTree(document.createElement('div'), { view: () => state, last: () => 5 }, bus(), { me: 'ana' });
  tree.open('b'); tree.open('c');
  clock.snap();
  const c = tree.cards.get('c'), d = tree.cards.get('d'), b = tree.cards.get('b');
  assert.ok(c && d, 'the deep levels are open');
  assert.equal(d.edge.getAttribute('d').split(' ')[0], `M${c.x + DEEP_W},${c.y + DEEP_H / 2}`, 'out of a deep card at its right middle');
  assert.ok(d.edge.getAttribute('d').endsWith(` ${d.x},${d.y + DEEP_H / 2}`), 'into a deep card at its left middle');
  assert.equal(c.edge.getAttribute('d').split(' ')[0], `M${b.x + CARD_W},${b.y + CARD_H / 2}`);
  tree.destroy();
});

test('views.css card sizes match tree.js and fit the 250 x 56 layout grid, also on the projector', () => {
  const css = readFileSync(join(here, '..', '..', 'views.css'), 'utf8').replace(/\/\*[\s\S]*?\*\//g, '');
  const sizes = [];
  for (const m of css.matchAll(/([^{}]+)\{([^{}]*)\}/g)) {
    const sel = m[1].trim();
    // rules on the card box itself: the last compound of the selector is .card or .card--deep
    const last = sel.split(/\s+/).at(-1);
    if (!/^\.card(--deep)?(\.[\w-]+)*$/.test(last) || /__/.test(last)) continue;
    const w = /(?:^|;|\s)width:\s*(\d+)px/.exec(m[2]), hh = /(?:^|;|\s)height:\s*(\d+)px/.exec(m[2]);
    if (w || hh) sizes.push({ sel, w: w ? +w[1] : null, h: hh ? +hh[1] : null });
  }
  const base = sizes.find((s) => s.sel === '.card');
  const deep = sizes.find((s) => s.sel === '.card--deep');
  assert.deepEqual([base.w, base.h], [CARD_W, CARD_H]);
  assert.deepEqual([deep.w, deep.h], [DEEP_W, DEEP_H]);
  for (const s of sizes) {
    if (s.w != null) assert.ok(s.w < COL_W, `${s.sel} width ${s.w} overlaps the next column (${COL_W})`);
    if (s.h != null) assert.ok(s.h < ROW_H, `${s.sel} height ${s.h} overlaps the next row (${ROW_H})`);
  }
});

test('follow from the page shell ({who, focus}) is honoured by both views', () => {
  const state = baseState([cl('v1', 'choice', 3)]);
  const b = bus();
  const store = { view: () => state, last: () => 2 };
  const tree = mountTree(document.createElement('div'), store, b, { me: 'ana' });
  const view = mountClusters(document.createElement('div'), store, b, { contract: { winner_word: {} } });
  b.emit('follow', { who: 'ben', focus: { type: 'node', id: 'choice' } });
  assert.equal(tree.follow, 'ben');
  assert.equal(view.follow, 'ben');
  b.emit('follow', null);
  assert.equal(tree.follow, null);
  tree.destroy(); view.destroy();
});

test('the tree honours opts.lastSeenSeq() for the since-you-looked dot', () => {
  const state = baseState([]);
  const tree = mountTree(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { me: 'ana', lastSeenSeq: () => 1 });
  assert.ok(tree.cards.get('choice').el.classList.contains('card--unseen'), 'seq 2 is newer than last seen 1');
  assert.ok(!tree.cards.get('root').el.classList.contains('card--unseen'));
  tree.destroy();
});

test('the claim countdown uses the server offset the page shell keeps (state.net.offsetMs)', () => {
  const state = baseState([]);
  const offset = 600000;
  state.net = { offsetMs: offset };
  state.nodes.set('choice', { ...state.nodes.get('choice'), claim: { holder: 'ben', owner: 'ben', untilMs: Date.now() + offset + 30000 } });
  const tree = mountTree(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { me: 'ana' });
  const tag = tree.cards.get('choice').parts.tag.textContent;
  assert.ok(/^ben (29|30) s$/.test(tag), tag);
  tree.destroy();
});

test('my own focus never draws a ring on my screen, even when the presence name is capitalised', () => {
  const state = baseState([]);
  state.presence = { clients: [{ client: 'c1', name: 'Ana', owner: 'ana', kind: 'human', focus: { type: 'node', id: 'choice' } }], claims: [] };
  const tree = mountTree(document.createElement('div'), { view: () => state, last: () => 2 }, bus(), { me: 'ana' });
  assert.ok(!tree.cards.get('choice').el.classList.contains('card--focused'));
  tree.destroy();
});
