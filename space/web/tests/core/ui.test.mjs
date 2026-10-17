// The rail renders every tab over the reduced fixture, in Node, on a 60-line DOM stub (no browser).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { makeReducer, trivialLayout } from '../../reduce.mjs';
import { loadLog } from './contract_src.mjs';

class N {
  constructor(type, name) { this.nodeType = type; this.nodeName = name; this.localName = String(name).toLowerCase(); this.childNodes = [];
    this.parentNode = null; this.attributes = {}; this.listeners = {}; this.style = { setProperty(k, v) { this[k] = v; } }; this.data = ''; }
  get firstChild() { return this.childNodes[0] || null; }
  get lastChild() { return this.childNodes[this.childNodes.length - 1] || null; }
  get nextSibling() { const p = this.parentNode; if (!p) return null; return p.childNodes[p.childNodes.indexOf(this) + 1] || null; }
  get children() { return this.childNodes.filter((c) => c.nodeType === 1); }
  appendChild(c) { return this.insertBefore(c, null); }
  insertBefore(c, ref) {
    if (c.parentNode) c.parentNode.removeChild(c);
    const i = ref ? this.childNodes.indexOf(ref) : -1;
    if (i < 0) this.childNodes.push(c); else this.childNodes.splice(i, 0, c);
    c.parentNode = this; return c;
  }
  removeChild(c) { const i = this.childNodes.indexOf(c); if (i >= 0) this.childNodes.splice(i, 1); c.parentNode = null; return c; }
  remove() { if (this.parentNode) this.parentNode.removeChild(this); }
  setAttribute(k, v) { this.attributes[k] = String(v); }
  removeAttribute(k) { delete this.attributes[k]; }
  getAttribute(k) { return k in this.attributes ? this.attributes[k] : null; }
  addEventListener(t, f) { this.listeners[t] = f; }
  removeEventListener(t) { delete this.listeners[t]; }
  querySelector() { return null; }
  get textContent() { return this.nodeType === 3 ? this.data : this.childNodes.map((c) => c.textContent).join(''); }
  set textContent(v) { this.childNodes = []; if (v) this.appendChild(globalThis.document.createTextNode(v)); }
  find(pred) { if (pred(this)) return this; for (const c of this.childNodes) { const r = c.find(pred); if (r) return r; } return null; }
  findAll(pred, out = []) { if (pred(this)) out.push(this); for (const c of this.childNodes) c.findAll(pred, out); return out; }
}
globalThis.document = {
  createElement: (n) => new N(1, n.toUpperCase()), createElementNS: (ns, n) => new N(1, n),
  createTextNode: (d) => { const t = new N(3, '#text'); t.data = String(d); return t; },
};
const tick = () => new Promise((r) => setTimeout(r, 150));   // Preact runs effects up to 100 ms after a render without rAF

const LOG = loadLog();
const R = makeReducer(trivialLayout);
const state = LOG.reduce((s, e) => R.reduce(s, e), R.init());

function makeApi(me, fetched) {
  const subs = new Set(), bus = new Map();
  return {
    view: () => ({ ...state, presence: { clients: [], claims: [] } }),
    subscribe: (fn) => { subs.add(fn); return () => subs.delete(fn); },
    bus: { on: (n, f) => { bus.set(n, f); return () => bus.delete(n); }, emit: (n, p) => bus.get(n) && bus.get(n)(p) },
    post: async () => null, claim: async () => null, me, flags: { stage: false, key: '' }, base: '',
    following: () => '', selected: () => 'choice', setView: () => {},
  };
}

test('every rail tab renders over the reduced fixture', async () => {
  const fetched = [];
  globalThis.fetch = async (url) => { fetched.push(url); return { ok: true, status: 200, json: async () => ({ part: 'choice', clock: 3,
    sections: { FACTS: [{ id: 'm000a01', date: '2026-10-17', run: 'r', round: 1, source: 'measured', text: 'a fact', used: 3 }] }, archive: [] }) }; };
  const { mountRail } = await import('../../rail.js');
  const el = new N(1, 'ASIDE');
  const api = makeApi('ana', fetched);
  mountRail(el, api);
  await tick();
  let text = el.textContent;
  assert.match(text, /Next question/);
  assert.match(text, /measure bins used, not time/);
  assert.match(text, /applied at the pick of round 2/);
  assert.match(text, /is working on part/);
  assert.match(text, /applied in round 1, stage planned/);
  assert.match(text, /Ana via agent/);
  assert.match(text, /told to the team at planned r1/);
  for (const [tab, want] of [['args', /A reply never gates a build/], ['results', /won/], ['memory', /Added in this run/], ['agent', /What my agent was told/]]) {
    api.bus.emit('tab', tab);
    await tick();
    text = el.textContent;
    assert.match(text, want, tab);
    if (tab === 'args') { assert.match(text, /hidden_cost/); assert.match(text, /Ana/); assert.match(text, /standing/); }
    if (tab === 'results') { assert.match(text, /Ana: hit/); assert.match(text, /Ben: miss/); assert.match(text, /rung|loss/); }
    if (tab === 'memory') { assert.ok(fetched.some((u) => u.includes('/api/memory?part=choice'))); assert.match(text, /a fact/); }
    if (tab === 'agent') { assert.match(text, /Got it/); assert.match(text, /Send/); }
  }
  // Ben sees his intent card, already decided
  const el2 = new N(1, 'ASIDE');
  const api2 = makeApi('ben', fetched);
  mountRail(el2, api2);
  await tick();
  api2.bus.emit('tab', 'agent');
  await tick();
  assert.match(el2.textContent, /mark "ties never matter" as disputed/);
  assert.match(el2.textContent, /apply/);
});
