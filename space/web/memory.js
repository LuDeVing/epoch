// memory.js: the Memory tab (section 2, read only by the owner's decision 9). The part's memory file from
// GET /api/memory?part= (sections, source tag, date, run, round, ARCHIVE) next to the memory_added lines of this
// run (state.memory). The file is re-read when the part changes or when this run adds to it.
import { html, useState, useEffect } from './vendor/standalone.module.js';

export const SECTIONS = ['FACTS', 'TRIED', 'PRIORS', 'CUES', 'OPEN QUESTIONS', 'FAILED FRAMINGS', 'FACTS FROM PEOPLE'];

export function memoryUrl(base, part, key) {
  return `${base}/api/memory?part=${encodeURIComponent(part)}${key ? `&key=${encodeURIComponent(key)}` : ''}`;
}

function Entry({ e }) {
  return html`<li class="mem">
    <span class="mono muted">${e.id || ''}</span>
    ${e.source ? html`<span class=${`tag src--${e.source}`}>${e.source}</span>` : null}
    <span class="mem__text">${e.text}</span>
    <span class="muted mem__meta">${[e.date, e.run, e.round != null ? `r${e.round}` : null, e.used != null ? `used ${e.used}` : null].filter(Boolean).join(' . ')}</span>
  </li>`;
}

export function MemoryTab({ view, api }) {
  const parts = [...view.nodes.values()].filter((n) => n.kind !== 'root');
  const [part, setPart] = useState(api.selected && api.selected() ? api.selected() : (parts[0] && parts[0].id) || '');
  const [file, setFile] = useState(null);
  const [err, setErr] = useState('');
  const [showArchive, setShowArchive] = useState(false);
  const added = (part && view.memory.get(part)) || [];
  useEffect(() => api.bus.on('select', (sel) => { if (sel && sel.type === 'node' && sel.id) setPart(sel.id); }), []);
  useEffect(() => {
    if (!part) return undefined;
    let live = true;
    setErr('');
    fetch(memoryUrl(api.base, part, api.flags.key), { cache: 'no-store' })
      .then(async (r) => {
        const body = await r.json().catch(() => ({}));
        if (!live) return;
        if (r.status === 404) { setFile(null); setErr('No memory file for this part yet.'); }
        else if (!r.ok) { setFile(null); setErr(`Could not read the memory file (${body.error || r.status}).`); }
        else setFile(body);
      })
      .catch(() => { if (live) { setFile(null); setErr('The server is offline.'); } });
    return () => { live = false; };
  }, [part, added.length]);
  return html`<div class="tab-body memory">
    <label class="muted">Part <select value=${part} onChange=${(e) => setPart(e.target.value)}>
      ${parts.map((n) => html`<option value=${n.id}>${n.name}</option>`)}</select></label>
    <span class="tag">read only</span>
    <div class="card">
      <div class="card__head">Added in this run</div>
      ${added.length ? html`<ul class="mems">${added.map((e) => html`<${Entry} e=${e} />`)}</ul>` : html`<div class="muted">Nothing yet.</div>`}
    </div>
    ${err ? html`<div class="muted">${err}</div>` : null}
    ${file ? html`<div class="card">
      <div class="card__head">${file.part}.md${file.clock != null ? html` <span class="muted">clock ${file.clock}</span>` : null}</div>
      ${SECTIONS.map((sec) => {
        const rows = (file.sections && file.sections[sec]) || [];
        return html`<div class="mem__sec"><div class="mem__title">${sec} <span class="muted">${rows.length}</span></div>
          ${rows.length ? html`<ul class="mems">${rows.map((e) => html`<${Entry} e=${e} />`)}</ul>` : null}</div>`; })}
      <button class="btn btn--small" onClick=${() => setShowArchive(!showArchive)}>ARCHIVE (${(file.archive || []).length})</button>
      ${showArchive ? html`<ul class="mems mems--archive">${(file.archive || []).map((e) => html`<${Entry} e=${e} />`)}</ul>` : null}
    </div>` : null}
  </div>`;
}
