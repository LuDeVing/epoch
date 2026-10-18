// memory.js: the Memory tab (section 2, read only by the owner's decision 9). The part's memory file from
// GET /api/memory?part= (sections, source tag, date, run, round, ARCHIVE) next to the memory_added lines of this
// run (state.memory). The file is re-read when the part changes or when this run adds to it.
import { html, useState, useEffect } from './vendor/standalone.module.js';
import { MEMORY_HEADINGS } from './words.mjs';

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

function Knowledge({ api, head }) {
  const [files, setFiles] = useState([]);
  const [open, setOpen] = useState('');
  const [text, setText] = useState('');
  const [dir, setDir] = useState('');
  const q = api.flags && api.flags.key ? `&key=${encodeURIComponent(api.flags.key)}` : '';
  const load = async () => {
    try {
      const r = await fetch(`${api.base}/api/knowledge?x=1${q}`, { credentials: 'same-origin', cache: 'no-store' });
      if (!r.ok) return;
      const j = await r.json(); setFiles(j.files || []); setDir(j.dir || '');
    } catch (e) { /* offline */ }
  };
  const show = async (path) => {
    if (open === path) { setOpen(''); setText(''); return; }
    try {
      const r = await fetch(`${api.base}/api/knowledge?path=${encodeURIComponent(path)}${q}`, { credentials: 'same-origin', cache: 'no-store' });
      const j = await r.json(); setOpen(path); setText(j.text || '');
    } catch (e) { setText('Could not read the file.'); }
  };
  useEffect(() => { load(); }, [head]);
  const group = (pre) => files.filter((f) => f.path.startsWith(pre));
  const top = files.filter((f) => !f.path.includes('/'));
  return html`<div class="know">
    <div class="caption">What is known, as Markdown files in the space's knowledge folder. The researchers read facts.md; you can open any file here or in a text editor.${dir ? html` <span class="mono muted know__dir" title=${dir}>${dir}</span>` : null}</div>
    <div class="know__files">
      ${top.map((f) => html`<button class=${`know__file${open === f.path ? ' is-on' : ''}`} onClick=${() => show(f.path)}>${f.title}</button>`)}
      ${group('findings/').length ? html`<div class="know__group">Findings</div>${group('findings/').map((f) => html`<button class=${`know__file${open === f.path ? ' is-on' : ''}`} onClick=${() => show(f.path)}>${f.title}</button>`)}` : null}
      ${group('parts/').length ? html`<div class="know__group">Parts</div>${group('parts/').map((f) => html`<button class=${`know__file${open === f.path ? ' is-on' : ''}`} onClick=${() => show(f.path)}>${f.title}</button>`)}` : null}
      ${!files.length ? html`<div class="muted">No files yet. Describe a problem or share a finding and they appear here.</div>` : null}
    </div>
    ${open ? html`<div class="know__view"><div class="card__head">${open} <a class="btn btn--small" style="float:right" download=${open.split('/').pop()} href=${`data:text/markdown;charset=utf-8,${encodeURIComponent(text)}`}>Download</a></div><pre class="know__text">${text}</pre></div>` : null}
  </div>`;
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
    <${Knowledge} api=${api} head=${view.head} />
    <div class="caption" style="margin-top:12px">What the team has learned about each part, kept across runs: facts, what was tried, what to expect, dead ends, and what people shared. Every entry names its evidence. Read only.</div>
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
        return html`<div class="mem__sec"><div class="mem__title">${MEMORY_HEADINGS[sec] || sec} <span class="muted">${rows.length}</span></div>
          ${rows.length ? html`<ul class="mems">${rows.map((e) => html`<${Entry} e=${e} />`)}</ul>` : null}</div>`; })}
      <button class="btn btn--small" onClick=${() => setShowArchive(!showArchive)}>Archive (${(file.archive || []).length})</button>
      ${showArchive ? html`<ul class="mems mems--archive">${(file.archive || []).map((e) => html`<${Entry} e=${e} />`)}</ul>` : null}
    </div>` : null}
  </div>`;
}
