// tree.js, clusters.js and motion.mjs import under Node with a 40-line DOM stub; a missing d3 global throws a
// clear message; views.css and the modules carry no raw hex colour (docs/MULTIPLAYER_DESIGN.md 12.1 row P5).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';
import { installDom } from './helpers/dom_stub.mjs';

const here = dirname(fileURLToPath(import.meta.url));
const web = join(here, '..', '..');
installDom();

test('the modules import under Node without d3 (no DOM call at import time)', async () => {
  delete globalThis.d3;
  const motion = await import('../../motion.mjs');
  assert.equal(typeof motion.smoothDamp, 'function');
  assert.equal(typeof motion.clock.kick, 'function');
  const tree = await import('../../tree.js');
  const clusters = await import('../../clusters.js');
  const layout = await import('../../layout.mjs');
  const cardstate = await import('../../cardstate.mjs');
  assert.equal(typeof tree.mountTree, 'function');
  assert.equal(typeof clusters.mountClusters, 'function');
  assert.equal(typeof layout.layoutTree, 'function');
  assert.equal(typeof cardstate.cardState, 'function');
});

test('a missing d3 global throws a clear message from the layout and from both mounts', async () => {
  delete globalThis.d3;
  const { layoutTree, layoutClusters, requireD3 } = await import('../../layout.mjs');
  const { mountTree } = await import('../../tree.js');
  const { mountClusters } = await import('../../clusters.js');
  const re = /d3 is missing: load vendor\/d3\.min\.js as a classic script before the modules/;
  assert.throws(() => requireD3(), re);
  assert.throws(() => layoutTree(new Map([['root', { id: 'root', parent: null }]])), re);
  assert.throws(() => layoutClusters(new Map(), [{ key: 'v1', n: 2 }], { x: 0, y: 0 }, new Map()), re);
  const store = { view: () => null, last: () => 0 };
  assert.throws(() => mountTree(document.createElement('div'), store, null), re);
  assert.throws(() => mountClusters(document.createElement('div'), store, null), re);
});

test('ensureD3 loads the vendored file under Node and the mounts then work against the stub', async () => {
  const { ensureD3 } = await import('../../layout.mjs');
  const d3 = await ensureD3();
  assert.equal(d3.version, '7.9.0');
  assert.equal(globalThis.d3, d3);
  const { mountTree } = await import('../../tree.js');
  const { mountClusters } = await import('../../clusters.js');
  const state = {
    run: { round: 1, stage: 'planned', waiting: true, mode: 'check_only' },
    people: new Map([['ana', { name: 'ana', hue: 'a' }]]),
    nodes: new Map([['root', { id: 'root', name: 'root', parent: null, origin: 'map', status: 'map', seq: 1, owner: 'team' }],
                    ['choice', { id: 'choice', name: 'choice rule', parent: 'root', origin: 'map', status: 'map', seq: 2, owner: 'team' }],
                    ['item_order', { id: 'item_order', name: 'item order', parent: 'root', origin: 'human', status: 'queued', seq: 41, owner: 'ana', by: 'ana.agent', halo: { by: 'ana', seq: 41 } }]]),
    clusters: new Map([['v1', { key: 'v1', node: 'choice', direction: 'inward', name: 'best fit', members: ['s1', 's2', 's3'], n: 3, prior: 'known', contributors: { team: 3 }, votes: { ana: 1 }, status: 'open', selected: true }],
                       ['v2', { key: 'v2', node: 'choice', direction: 'outward', name: 'lone', members: ['s9'], n: 1, prior: 'new', contributors: { team: 1 }, votes: {}, status: 'open' }]]),
    layout: { tree: new Map(), clusters: new Map(), anchors: new Map(), hash: '00000000' },
    presence: { clients: [{ client: 'c1', name: 'ben', owner: 'ben', kind: 'human', focus: { type: 'node', id: 'choice' } }], claims: [] },
    results: [],
  };
  const events = [];
  const bus = { handlers: {}, on(n, f) { (this.handlers[n] = this.handlers[n] || []).push(f); }, emit(n, p) { events.push([n, p]); (this.handlers[n] || []).forEach((f) => f(p)); } };
  const store = { view: () => state, last: () => 41 };
  const treeEl = document.createElement('div');
  const tree = mountTree(treeEl, store, bus, { me: 'ana' });
  assert.equal(tree.cards.size, 3);
  const human = tree.cards.get('item_order');
  assert.ok(human.el.classList.contains('card--queued'));
  assert.ok(human.el.classList.contains('hue-a'));
  assert.ok(human.el.classList.contains('is-halo'), 'a halo in the actor hue');
  const chipTexts = human.el.find('chip__text').map((e) => e.textContent);
  assert.deepEqual(chipTexts, ['waits for planned, round 1']);
  assert.equal(tree.cards.get('choice').parts.tag.textContent, 'ben', 'a focus ring names the person');
  // the card was born at its parent (x 0) and glides to its slot one column right; under Node the mount's kick
  // ran one synchronous frame already, so it has left the parent but not arrived
  assert.equal(tree.cards.get('root').x, 0);
  assert.equal(human.tx, 250);
  assert.ok(human.x > 0 && human.x < 250, `born at the parent, on its way: ${human.x}`);
  const { clock } = await import('../../motion.mjs');
  const before = human.x;
  clock.frame(performance.now() + 16);
  assert.ok(human.x > before && human.x <= 250, `glides on: ${before} -> ${human.x}`);
  assert.equal(human.el.style.transform, `translate(${human.x}px, ${human.y}px)`);
  // the bus: hover from the tree, select
  human.el.dispatch('mouseenter');
  assert.deepEqual(events.at(-1), ['hover', { type: 'node', id: 'item_order', source: 'tree' }]);
  human.el.dispatch('click');
  assert.deepEqual(events.at(-1), ['select', { type: 'node', id: 'item_order' }]);
  assert.ok(human.el.classList.contains('is-selected'));

  const clEl = document.createElement('div');
  const clusters = mountClusters(clEl, store, bus, { me: 'ana', contract: { winner_word: { check_only: 'carried', baseline: 'won', no_check: 'preferred' } } });
  assert.equal(clusters.bubbles.size, 2);
  assert.equal(clusters.islands.size, 1);
  const b1 = clusters.bubbles.get('v1');
  assert.equal(b1.parts.dots.children.length, 3, 'one dot per member');
  assert.ok(b1.el.classList.contains('prior-known'));
  assert.ok(b1.el.classList.contains('is-selected'));
  assert.equal(b1.parts.votes.children.length, 1, 'a vote dot in the person hue');
  assert.ok(b1.parts.votes.children[0].classList.contains('hue-a'));
  assert.equal(clusters.bubbles.get('v2').lod, false, 'a singleton folds into the long tail');
  assert.equal(clusters.islands.get('choice').tailText.textContent, '+1');
  assert.ok(b1.tr > 0, 'a local settle gave a radius when the reducer passed none');
  // linked hover: a tree hover lights the island's bubbles
  bus.emit('hover', { type: 'node', id: 'choice', source: 'tree' });
  assert.ok(b1.el.classList.contains('is-hot'));
  // the winner moment uses the contract word, never a word of the view
  state.clusters.get('v1').status = 'win';
  clusters.update(true);
  assert.equal(b1.parts.badgeText.textContent, 'carried', 'the badge word is contract.winner_word[run.mode]');
  assert.ok(b1.el.classList.contains('is-winner'));
  state.run.mode = 'no_check';
  clusters.update(true);
  assert.equal(b1.parts.badgeText.textContent, 'preferred');
  const src = readFileSync(join(web, 'clusters.js'), 'utf8');
  assert.ok(!/['"]won['"]/.test(src), 'no winner word is written in clusters.js');
  assert.ok(!/[.[]\s*['"]?obvious/.test(src), 'no code path reads obvious or obvious_match in the cluster module');
  tree.destroy(); clusters.destroy();
});

test('views.css and the modules carry no raw hex colour', () => {
  const files = ['views.css', 'tree.js', 'clusters.js', 'motion.mjs', 'layout.mjs', 'cardstate.mjs'];
  const hex = /#[0-9a-fA-F]{3,8}(?![\w-])/;
  for (const f of files) {
    const text = readFileSync(join(web, f), 'utf8');
    const m = hex.exec(text);
    assert.equal(m, null, `${f} has a raw colour ${m && m[0]}`);
    assert.ok(!/[^\x00-\x7f]/.test(text), `${f} is ASCII only`);
  }
  const css = readFileSync(join(web, 'views.css'), 'utf8');
  assert.ok(/var\(--owner-a\)/.test(css) && /var\(--bg-card\)/.test(css));
  assert.ok(!/https?:\/\//.test(css), 'no network url in the css');
});

test('the DOM stub is about 40 lines', () => {
  const lines = readFileSync(join(here, 'helpers', 'dom_stub.mjs'), 'utf8').split('\n').filter((l) => l.trim()).length;
  assert.ok(lines <= 45, `${lines} lines`);
});
