// connectSpace against a fake EventSource and a fake fetch: a gap, a duplicate, a ping catch-up, a 503 reopen,
// an epoch reset (note 02 section 6.3), and the long-poll mode. No network.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { connectSpace } from '../../connect.mjs';

class FakeES {
  static all = [];
  constructor(url) { this.url = url; this.readyState = 0; this.handlers = {}; this.closed = false; FakeES.all.push(this); }
  addEventListener(name, fn) { (this.handlers[name] ||= []).push(fn); }
  close() { this.readyState = 2; this.closed = true; }
  // test drivers
  open() { this.readyState = 1; this.onopen && this.onopen(); }
  send(ev) { this.onmessage && this.onmessage({ data: JSON.stringify(ev) }); }
  emit(name, data) { for (const fn of this.handlers[name] || []) fn({ data: JSON.stringify(data) }); }
  fail() { this.readyState = 2; this.onerror && this.onerror(); }
}

const evs = (a, b) => Array.from({ length: b - a + 1 }, (_, i) => ({ seq: a + i, kind: 'note_posted', data: { text: `n${a + i}` } }));
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
const until = async (fn, ms = 3000) => { const t = Date.now(); while (!fn()) { if (Date.now() - t > ms) throw new Error('timeout'); await sleep(5); } };

function fakeFetch(log, calls, server) {
  return async (url) => {
    calls.push(url);
    const since = Number(/since=(\d+)/.exec(url)[1]);
    const events = log.filter((e) => e.seq > since && e.seq <= server.head).slice(0, 2);   // small pages: the catch-up loops
    return { ok: true, status: 200, json: async () => ({ epoch: 'E1', head: server.head, events }) };
  };
}

test('stream: gap filled, duplicate ignored, ping catch-up, 503 reopen with since, epoch reset', async () => {
  FakeES.all = [];
  const log = evs(1, 9);
  const calls = [], got = [], status = [];
  let resets = 0;
  globalThis.EventSource = FakeES;
  const server = { head: 5 };
  globalThis.fetch = fakeFetch(log, calls, server);
  const c = connectSpace({ base: 'http://127.0.0.1:8766', since: 0, silentMs: 60000,
    onEvent: (e) => got.push(e.seq), onStatus: (s, info) => status.push(s), onReset: () => resets++ });
  const es = FakeES.all[0];
  assert.match(es.url, /\/api\/stream\?since=0$/);
  es.open();
  es.emit('hello', { epoch: 'E1', head: 9, server_time_ms: 0, claims: [], roster: [], replay: null });
  es.send(log[0]); es.send(log[1]);
  es.send(log[4]);                                       // a gap: 3 and 4 are missing
  await until(() => got.length >= 5);
  assert.deepEqual(got, [1, 2, 3, 4, 5]);
  assert.match(calls[0], /\/api\/events\?since=2&limit=500$/);
  es.send(log[2]);                                       // a duplicate
  assert.deepEqual(got, [1, 2, 3, 4, 5]);
  server.head = 9;
  es.emit('ping', { head: 9, claims: [] });              // catch-up from the ping
  await until(() => got.length >= 9);
  assert.deepEqual(got, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
  assert.equal(c.last(), 9);
  // the server answered 503 on reconnect: the browser gives up (readyState 2); the module reopens with since
  es.fail();
  assert.ok(status.includes('reconnecting'));
  await until(() => FakeES.all.length === 2, 3000);
  const es2 = FakeES.all[1];
  assert.match(es2.url, /since=9$/);
  es2.open();
  es2.emit('hello', { epoch: 'E1', head: 9 });
  assert.equal(resets, 0);
  // a different database: the epoch changed, the module stops and the app must reload from 0
  es2.fail();
  await until(() => FakeES.all.length === 3, 3000);
  const es3 = FakeES.all[2];
  es3.open();
  es3.emit('hello', { epoch: 'E2', head: 3 });
  assert.equal(resets, 1);
  assert.equal(es3.closed, true);
  es3.send({ seq: 10, kind: 'note_posted', data: {} });  // late events after the reset never get in
  assert.equal(got.length, 9);
  c.close();
  assert.deepEqual(status.filter((s) => s === 'live').length, 3);
});

test('stream: the browser retrying by itself (readyState 0) shows reconnecting, then live again', () => {
  FakeES.all = [];
  globalThis.EventSource = FakeES;
  const status = [];
  const c = connectSpace({ base: '', since: 0, silentMs: 60000, onEvent: () => {}, onStatus: (s) => status.push(s), onReset: () => {} });
  const es = FakeES.all[0];
  es.open();
  es.readyState = 0; es.onerror();                      // the server went away; the browser reconnects by itself
  assert.deepEqual(status, ['live', 'reconnecting']);
  assert.equal(FakeES.all.length, 1, 'no second EventSource while the browser retries');
  es.open();
  assert.deepEqual(status, ['live', 'reconnecting', 'live']);
  c.close();
});

test('stream: a server reset message stops the module and calls onReset', () => {
  FakeES.all = [];
  globalThis.EventSource = FakeES;
  let resets = 0;
  const c = connectSpace({ base: '', since: 5, onEvent: () => {}, onStatus: () => {}, onReset: () => resets++ });
  FakeES.all[0].open();
  FakeES.all[0].emit('reset', { reason: 'since_ahead_of_head' });
  assert.equal(resets, 1);
  assert.equal(FakeES.all[0].closed, true);
  c.close();
});

test('long-poll mode: in order, no duplicate, a failure backs off and reopens, an epoch change resets', async () => {
  const answers = [
    { ok: true, body: { epoch: 'E1', head: 3, events: evs(1, 3) } },
    { ok: false, status: 503 },
    { ok: true, body: { epoch: 'E1', head: 5, events: [...evs(3, 5)] } },  // 3 repeated: ignored
    { ok: true, body: { epoch: 'E2', head: 1, events: evs(1, 1) } },
  ];
  const calls = [], got = [], status = [];
  let resets = 0;
  globalThis.fetch = async (url) => {
    calls.push(url);
    const a = answers.shift();
    if (!a) return new Promise(() => {});               // hold forever, like a long poll with nothing new
    return { ok: a.ok, status: a.status || 200, json: async () => a.body };
  };
  const c = connectSpace({ base: 'http://127.0.0.1:8766', poll: true, since: 0,
    onEvent: (e) => got.push(e.seq), onStatus: (s) => status.push(s), onReset: () => resets++ });
  await until(() => resets === 1, 4000);
  assert.deepEqual(got, [1, 2, 3, 4, 5]);
  assert.match(calls[0], /\/api\/events\?since=0&limit=500&wait=25$/);
  assert.match(calls[2], /since=3&/);
  assert.ok(status.includes('reconnecting'));
  assert.equal(status[0], 'hello');
  c.close();
});
