// inspect.js: the detail panel. Click a tree card or a cluster bubble to open its data in the pane's corner; click
// the same one again, the x, or press Escape to close it. The panel reads the view only; it changes no layout.
import { html, render } from './vendor/standalone.module.js';

const fmt = (v) => (typeof v === 'number' ? (Number.isInteger(v) ? String(v) : v.toFixed(3)) : String(v));
const nameOf = (v, id) => (id && v.nodes.get(id) ? v.nodes.get(id).name : id || 'the whole problem');

function Row({ k, v }) {
  if (v == null || v === '' || (Array.isArray(v) && !v.length)) return null;
  return html`<div class="inspect__row"><span class="inspect__k">${k}</span><span class="inspect__v">${Array.isArray(v) ? html`<ul>${v.map((x) => html`<li>${x}</li>`)}</ul>` : v}</span></div>`;
}

function NodeDetail({ v, id }) {
  const n = v.nodes.get(id);
  if (!n) return html`<div class="muted">This part is gone from the map.</div>`;
  const counts = n.counts || {};
  const count = (dir) => { const k = counts[dir]; return k ? `${k.sketches || 0} sketches, ${k.clusters || 0} clusters, ${k.built || 0} built, ${k.checked || 0} checked` : null; };
  const clusters = [...v.clusters.values()].filter((c) => c.node === id);
  const results = v.results.filter((r) => r.node === id);
  const findings = v.findings.filter((f) => f.node === id);
  const children = [...v.nodes.values()].filter((x) => x.parent === id).map((x) => x.name);
  return html`<div>
    <${Row} k="id" v=${html`<span class="mono">${n.id}</span>`} />
    <${Row} k="kind" v=${`${n.kind || 'part'}, ${n.origin || 'map'}${n.by ? `, by ${n.by}` : ''}`} />
    <${Row} k="status" v=${n.status === 'map' ? null : n.status} />
    <${Row} k="under" v=${n.parent ? nameOf(v, n.parent) : null} />
    <${Row} k="frame" v=${n.frame} />
    <${Row} k="assumptions" v=${n.assumptions} />
    <${Row} k="test" v=${n.test ? `${n.test}${n.threshold != null ? `, threshold ${n.threshold}` : ''}${n.failsIf ? `, fails if ${n.failsIf}` : ''}` : null} />
    <${Row} k="inward" v=${count('inward')} />
    <${Row} k="outward" v=${count('outward')} />
    <${Row} k="children" v=${children} />
    <${Row} k="claim" v=${n.claim ? `${n.claim.holder}${n.claim.purpose ? `: ${n.claim.purpose}` : ''}` : null} />
    <${Row} k="disputed" v=${(n.disputed || []).map((d) => `${d.by}: ${d.fact || ''}${d.reason ? ` (${d.reason}${d.tag ? `, ${d.tag}` : ''})` : ''}`)} />
    <${Row} k="findings" v=${findings.map((f) => `${f.by}: ${f.title}`)} />
    <${Row} k="ideas" v=${clusters.length ? clusters.slice().sort((a, b) => (b.n || 0) - (a.n || 0)).slice(0, 12).map((c) => `${c.name} (${c.n || 0})${c.status && c.status !== 'open' ? `, ${c.status}` : ''}`) : null} />
    <${Row} k="results" v=${results.map((r) => `${r.name || r.cand}: ${r.status}${Object.keys(r.metrics || {}).length ? ` ${Object.entries(r.metrics).filter(([, x]) => typeof x === 'number').slice(0, 3).map(([k, x]) => `${k} ${fmt(x)}`).join(', ')}` : ''}${r.reason ? ` (${r.reason})` : ''}`)} />
  </div>`;
}

function ClusterDetail({ v, key }) {
  const c = v.clusters.get(key);
  if (!c) return html`<div class="muted">This idea was regrouped.</div>`;
  const results = v.results.filter((r) => r.key === key);
  const votes = c.votes ? Object.entries(c.votes) : [];
  return html`<div>
    <${Row} k="part" v=${nameOf(v, c.node)} />
    <${Row} k="members" v=${`${c.n || (c.members || []).length} sketches${c.direction ? `, ${c.direction}` : ''}`} />
    <${Row} k="rank" v=${c.rank != null ? `${c.rank}${c.score != null ? `, score ${fmt(c.score)}` : ''}` : null} />
    <${Row} k="lane" v=${c.lane} />
    <${Row} k="status" v=${c.status && c.status !== 'open' ? c.status : null} />
    <${Row} k="prior" v=${c.prior} />
    <${Row} k="votes" v=${votes.length ? votes.map(([who, val]) => `${who}: ${val > 0 ? 'up' : 'down'}`) : null} />
    <${Row} k="results" v=${results.map((r) => `${r.status}${r.rung != null ? ` at rung ${r.rung}` : ''}${Object.keys(r.metrics || {}).length ? ` ${Object.entries(r.metrics).filter(([, x]) => typeof x === 'number').slice(0, 3).map(([k, x]) => `${k} ${fmt(x)}`).join(', ')}` : ''}${r.reason ? ` (${r.reason})` : ''}`)} />
    <${Row} k="sketch ids" v=${(c.members || []).length ? html`<span class="mono">${(c.members || []).slice(0, 8).join(' ')}${(c.members || []).length > 8 ? ` +${c.members.length - 8}` : ''}</span>` : null} />
  </div>`;
}

export function mountInspector(treePane, clustersPane, api, bus) {
  const box = document.createElement('div');
  box.className = 'inspect';
  box.style.display = 'none';
  let open = null;                 // {type, id, pane}
  const close = () => { open = null; box.style.display = 'none'; render(null, box); };
  const paint = () => {
    if (!open) return;
    const v = api.view();
    const title = open.type === 'node' ? nameOf(v, open.id) : ((v.clusters.get(open.id) || {}).name || open.id);
    render(html`<div class="inspect__head"><strong>${title}</strong><button class="btn btn--small" type="button" title="close" onClick=${close}>x</button></div>
      ${open.type === 'node' ? html`<${NodeDetail} v=${v} id=${open.id} />` : html`<${ClusterDetail} v=${v} key=${open.id} />`}`, box);
  };
  bus.on('select', (sel) => {
    if (!sel || (sel.type !== 'node' && sel.type !== 'cluster')) return;
    const id = sel.type === 'node' ? sel.id : sel.key;
    if (!id) return;
    if (open && open.type === sel.type && open.id === id) { close(); return; }      // the same one again: shrink
    const pane = sel.type === 'node' ? treePane : clustersPane;
    if (box.parentNode !== pane) pane.appendChild(box);
    open = { type: sel.type, id };
    box.style.display = '';
    paint();
  });
  bus.on('state', () => paint());
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && open) close(); });
  return { close, isOpen: () => !!open };
}
