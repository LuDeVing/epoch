// A 40-line DOM stub so tree.js and clusters.js can import and mount under Node (no browser, no jsdom).
class ClassList {
  constructor(el) { this.el = el; this.set = new Set(); }
  add(...c) { c.forEach((x) => this.set.add(x)); this.sync(); }
  remove(...c) { c.forEach((x) => this.set.delete(x)); this.sync(); }
  toggle(c, force) { const on = force === undefined ? !this.set.has(c) : !!force; if (on) this.set.add(c); else this.set.delete(c); this.sync(); return on; }
  contains(c) { return this.set.has(c); }
  sync() { this.el.attrs.class = [...this.set].join(' '); }
}
class Style { setProperty(k, v) { this[k] = v; } removeProperty(k) { delete this[k]; } getPropertyValue(k) { return this[k] || ''; } }
export class Element {
  constructor(tag, ns) { this.tagName = tag; this.ns = ns || null; this.attrs = {}; this.children = []; this.parentNode = null; this.style = new Style(); this.listeners = {}; this._text = ''; this.classList = new ClassList(this); this.offsetWidth = 0; }
  get textContent() { return this._text; }
  set textContent(v) { this._text = String(v); for (const c of this.children) c.parentNode = null; this.children.length = 0; }
  setAttribute(k, v) { this.attrs[k] = String(v); if (k === 'class') { this.classList.set = new Set(String(v).split(/\s+/).filter(Boolean)); } }
  getAttribute(k) { return k in this.attrs ? this.attrs[k] : null; }
  appendChild(c) { if (c.parentNode) c.parentNode.removeChild(c); c.parentNode = this; this.children.push(c); return c; }
  removeChild(c) { const i = this.children.indexOf(c); if (i >= 0) this.children.splice(i, 1); c.parentNode = null; return c; }
  contains(c) { for (let n = c; n; n = n.parentNode) if (n === this) return true; return false; }
  addEventListener(t, fn) { (this.listeners[t] = this.listeners[t] || []).push(fn); }
  removeEventListener(t, fn) { this.listeners[t] = (this.listeners[t] || []).filter((f) => f !== fn); }
  dispatch(t, ev = {}) { for (const fn of this.listeners[t] || []) fn({ type: t, target: this, preventDefault() {}, stopPropagation() {}, ...ev }); }
  getBoundingClientRect() { return { width: 0, height: 0, left: 0, top: 0 }; }
  querySelector() { return null; }
  querySelectorAll() { return []; }
  get ownerDocument() { return globalThis.document; }
  get childNodes() { return this.children; }
  get firstChild() { return this.children[0] || null; }
  all() { const out = [this]; for (const c of this.children) out.push(...c.all()); return out; }
  find(cls) { return this.all().filter((e) => e.classList.contains(cls)); }
}
export function installDom() {
  const doc = { visibilityState: 'visible', listeners: {},
    createElement: (t) => new Element(t), createElementNS: (ns, t) => new Element(t, ns),
    addEventListener(t, fn) { (this.listeners[t] = this.listeners[t] || []).push(fn); }, removeEventListener() {},
    body: new Element('body'), documentElement: new Element('html') };
  globalThis.document = doc;
  return doc;
}
