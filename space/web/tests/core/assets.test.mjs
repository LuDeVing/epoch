// Static checks of the shell in Node (the same rules as check_assets.py), plus a syntax and import check of the
// page modules: the UI modules import under Node without a DOM, and app.js parses.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { existsSync, readFileSync, readdirSync, statSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';
import { WEB } from './contract_src.mjs';

const read = (name) => readFileSync(join(WEB, name), 'utf8');
const HEX = /(?<![\w&])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b/;

test('index.html: mount ids, scripts and fonts only from vendor/, no http(s) in html or css', () => {
  const html = read('index.html');
  for (const id of ['topbar', 'tree-pane', 'clusters-pane', 'rail', 'strip']) assert.match(html, new RegExp(`id="${id}"`), id);
  const srcs = [...html.matchAll(/<script[^>]*\ssrc="([^"]+)"/g)].map((m) => m[1]);
  assert.ok(srcs.length >= 1);
  for (const s of srcs) assert.ok(s.startsWith('vendor/'), s);
  assert.doesNotMatch(html, /https?:\/\//);
  const css = readdirSync(WEB).filter((f) => f.endsWith('.css'));
  assert.ok(css.includes('tokens.css') && css.includes('base.css'));
  for (const f of css) {
    const t = read(f);
    assert.doesNotMatch(t, /https?:\/\//, f);
    for (const m of t.matchAll(/url\(\s*['"]?([^'")]+)['"]?\s*\)/g)) if (/\.woff2?$/.test(m[1])) assert.ok(m[1].startsWith('vendor/'), m[1]);
  }
});

test('vendor files match MANIFEST.json (d3 pending when absent)', () => {
  const man = JSON.parse(read('vendor/MANIFEST.json'));
  for (const f of man.files) {
    const p = join(WEB, 'vendor', f.file);
    if (f.file === 'd3.min.js') {
      assert.equal(f.bytes, 279706);
      if (!existsSync(p)) continue;                 // pending: the views part owns it
    }
    assert.ok(existsSync(p), `vendor/${f.file} exists`);
    assert.equal(statSync(p).size, f.bytes, `vendor/${f.file} size`);
  }
});

test('no raw hex colour outside tokens.css; page files are ASCII', () => {
  const files = readdirSync(WEB).filter((f) => /\.(m?js|css|html)$/.test(f) && f !== 'tokens.css');
  for (const f of files) assert.doesNotMatch(read(f), HEX, f);
  assert.match(read('tokens.css'), HEX);
  for (const f of ['index.html', 'app.js', 'connect.mjs', 'store.mjs', 'reduce.mjs', 'match.mjs', 'rail.js', 'chat.js',
    'memory.js', 'presence.js', 'tokens.css', 'base.css']) {
    assert.ok(![...readFileSync(join(WEB, f))].some((b) => b > 127), `${f} is ASCII`);
  }
});

test('tokens.css is note 01 section 7.3 (the owner hues and the slate neutrals)', () => {
  const t = read('tokens.css');
  for (const pair of ['--owner-a: #3987e5', '--owner-b: #d95926', '--owner-c: #199e70', '--owner-team: #8b8d98', '--bg-app: #111113',
    '--text-1: #edeef0', '--ok: #0ca30c', '--bad: #d03b3b', '--t-enter: 280ms cubic-bezier(.2,.9,.3,1.15)']) assert.ok(t.includes(pair), pair);
});

test('the UI modules import under Node without a DOM, and app.js parses', async () => {
  for (const f of ['presence.js', 'memory.js', 'chat.js', 'rail.js']) {
    const m = await import(pathToFileURL(join(WEB, f)).href);
    assert.ok(Object.keys(m).length > 0, f);
  }
  const rail = await import(pathToFileURL(join(WEB, 'rail.js')).href);
  assert.deepEqual(rail.TABS.map((t) => t[1]), ['Feed', 'Arguments', 'Results', 'Memory', 'My agent']);
  const chat = await import(pathToFileURL(join(WEB, 'chat.js')).href);
  assert.deepEqual(chat.SLASH_HINTS.map((h) => h[0]), ['branch', 'vote', 'claim', 'release', 'dispute', 'ask', 'skip', 'unskip',
    'veto', 'unveto', 'choose', 'note', 'reply', 'seed', 'pause', 'resume', 'go']);
  assert.deepEqual(chat.slashMatches('/un').map((h) => h[0]), ['unskip', 'unveto']);
  execFileSync(process.execPath, ['--check', join(WEB, 'app.js')], { stdio: 'pipe' });
});

test('index.js imports every core test file (it is what `node --test space/web/tests/core` runs)', () => {
  const idx = read('tests/core/index.js');
  for (const f of readdirSync(join(WEB, 'tests', 'core')).filter((x) => x.endsWith('.test.mjs'))) assert.ok(idx.includes(`'./${f}'`), f);
});

test('presence rows: a person chip and an agent ring with its state', async () => {
  const { presenceRows } = await import(pathToFileURL(join(WEB, 'presence.js')).href);
  const view = { people: new Map([['ana', { name: 'ana', hue: 'a' }], ['ben', { name: 'ben', hue: 'b' }]]),
    presence: { clients: [{ client: 'c-1', name: 'ana', owner: 'ana', cursor: 40, seen_ms_ago: 1200 },
      { client: 'ana.agent', name: 'ana.agent', owner: 'ana', kind: 'agent', activity: { state: 'thinking', text: 'reading' }, cursor: 38, seen_ms_ago: 12000 }], claims: [] } };
  const rows = presenceRows(view, 0);
  assert.deepEqual(rows.map((r) => [r.name, r.hue, r.online]), [['ana', 'a', true], ['ben', 'b', false]]);
  assert.equal(rows[0].agent.state, 'thinking');
  assert.equal(rows[0].agent.heardS, 12);
  assert.equal(rows[0].cursor, 40);
});
