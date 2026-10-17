// findings.js: the Findings tab. People share files (data, measurements, papers, notes) and short notes with the
// team. Each shared file becomes a finding: the loop keeps it in the part's memory (FACTS FROM PEOPLE) and quotes
// its readable part to the inventors, critics and builders of that part, as evidence, never as an instruction.
// Nothing is deleted: a correction is a new finding that replaces an older one.
import { html, useState, useRef, useEffect } from './vendor/standalone.module.js';
import { hueOf } from './presence.js';

export const KINDS = ['data', 'measurement', 'result', 'paper', 'note'];
const WORD = /[a-z0-9]+/g;
const ICON = { data: 'table', measurement: 'gauge', result: 'flag', paper: 'doc', note: 'pen' };

export function parseValues(text) {
  const out = {};
  for (const line of String(text || '').split(/\n|,|;/)) {
    const m = line.match(/^\s*([A-Za-z_][\w .%/-]*?)\s*=\s*([-+]?\d+(?:\.\d+)?)\s*$/);
    if (m) out[m[1].trim()] = Number(m[2]);
  }
  return out;
}

export function suggestPart(nodes, text) {
  const words = new Set((String(text || '').toLowerCase().match(WORD) || []).filter((w) => w.length > 2));
  let best = null, score = 0;
  for (const n of nodes) {
    if (n.kind === 'root') continue;
    const own = new Set(((`${n.name || ''} ${n.id || ''} ${n.frame || ''}`).toLowerCase().match(WORD) || []));
    let hit = 0;
    for (const w of words) if (own.has(w)) hit += 1;
    if (hit > score) { score = hit; best = n.id; }
  }
  return best;
}

export function fmtBytes(n) {
  const v = Number(n) || 0;
  if (v >= 1e6) return `${(v / 1e6).toFixed(1)} MB`;
  if (v >= 1e3) return `${Math.round(v / 1e3)} kB`;
  return `${v} B`;
}

function Icon({ kind }) {
  const k = ICON[kind] || 'doc';
  return html`<span class=${`fico fico--${k}`} aria-hidden="true">${k === 'table' ? '▦' : k === 'gauge' ? '◔' : k === 'flag' ? '⚑' : k === 'pen' ? '✎' : '□'}</span>`;
}

// One file after upload, before it is shared: the person picks the part, adds a line, presses Share.
function Pending({ up, nodes, parts, name, onShare, onDrop }) {
  const [part, setPart] = useState('');
  const [note, setNote] = useState('');
  const [kind, setKind] = useState(up.kind || 'data');
  const [values, setValues] = useState('');
  const suggested = part ? null : suggestPart(nodes, `${up.name} ${up.excerpt || ''}`);
  return html`<div class="fcard fcard--pending">
    <div class="fcard__head"><${Icon} kind=${kind} /><span class="fcard__name" title=${up.name}>${up.name}</span><span class="muted">${fmtBytes(up.bytes)}${up.lines ? ` . ${up.lines} lines` : ''}</span>
      <button class="btn btn--small" type="button" onClick=${onDrop} title="forget this upload">x</button></div>
    ${up.excerpt ? html`<pre class="fcard__excerpt">${up.excerpt.slice(0, 400)}${up.excerpt.length > 400 ? ' ...' : ''}</pre>` : html`<div class="muted">No readable text inside; the team gets the file name and your note.</div>`}
    <div class="fcard__row">
      <select value=${part} onChange=${(e) => setPart(e.target.value)} title="which part of the problem this is about">
        <option value="">${suggested ? `part: ${name(suggested)} (suggested)` : 'part: the whole problem'}</option>
        ${parts.map((p) => html`<option value=${p.id}>${p.name}</option>`)}</select>
      <select value=${kind} onChange=${(e) => setKind(e.target.value)}>${KINDS.map((k) => html`<option value=${k}>${k}</option>`)}</select>
    </div>
    <input placeholder="one line for the team: what this is and what it shows (optional)" value=${note} onInput=${(e) => setNote(e.target.value)} maxlength="400" />
    <input class="mono" placeholder="numbers to remember, like bins_ratio=1.04, n=100 (optional)" value=${values} onInput=${(e) => setValues(e.target.value)} />
    <div class="fcard__row"><button class="btn btn--small btn--primary" type="button" onClick=${() => onShare({ part: part || suggested || null, note, kind, values: parseValues(values) })}>Share with the team</button></div>
  </div>`;
}

function Finding({ f, view, name, base, onCorrect }) {
  const [open, setOpen] = useState(false);
  const vals = Object.entries(f.values || {});
  const file = f.file;
  return html`<li class=${`fcard${f.replacedBy ? ' fcard--replaced' : ''}`}>
    <div class="fcard__head">
      <${Icon} kind=${f.kind} />
      <span class="fcard__name" title=${f.title}>${f.title}</span>
      <span class=${`tok hue-${hueOf(view, f.by)}`}>${f.by}</span>
      <span class="tag">${name(f.node)}</span>
      ${f.pending ? html`<span class="tag">sending</span>` : null}
      ${f.replacedBy ? html`<span class="tag tag--warn">replaced by e${f.replacedBy}</span>` : null}
    </div>
    ${f.text && f.text !== f.title ? html`<div class="fcard__text">${f.text}</div>` : null}
    <div class="fcard__meta muted">
      ${file ? html`<a class="fcard__file" href=${`${base}/api/files/${file.id}`} target="_blank" rel="noopener">${file.name}</a><span>${fmtBytes(file.bytes)}</span>` : html`<span>${f.source}</span>`}
      ${vals.length ? html`<span class="mono">${vals.map(([k, v]) => `${k}=${v}`).join(', ')}</span>` : null}
      ${f.ts ? html`<span>${String(f.ts).slice(11, 16)}</span>` : null}
      ${f.excerpt ? html`<button class="btn btn--small" type="button" onClick=${() => setOpen(!open)}>${open ? 'hide' : 'preview'}</button>` : null}
      ${!f.replacedBy && !f.pending ? html`<button class="btn btn--small" type="button" onClick=${() => onCorrect(f)}>replace</button>` : null}
    </div>
    ${open && f.excerpt ? html`<pre class="fcard__excerpt">${f.excerpt}</pre>` : null}
  </li>`;
}

export function FindingsTab({ view, api }) {
  const nodes = [...view.nodes.values()];
  const parts = nodes.filter((n) => n.kind !== 'root');
  const base = api.base || '';
  const [uploads, setUploads] = useState([]);          // files uploaded, not yet shared
  const [busy, setBusy] = useState(0);
  const [err, setErr] = useState('');
  const [replaces, setReplaces] = useState(null);
  const [filter, setFilter] = useState('');
  const [noteOpen, setNoteOpen] = useState(false);
  const [noteTitle, setNoteTitle] = useState('');
  const [noteText, setNoteText] = useState('');
  const [drag, setDrag] = useState(false);
  const input = useRef(null);
  const name = (id) => (id && view.nodes.get(id) ? view.nodes.get(id).name : 'whole problem');
  const headers = () => ({ 'X-Space-Actor': api.me || '', 'X-Space-Kind': 'human', ...(api.flags && api.flags.key ? { 'X-Space-Key': api.flags.key } : {}) });

  const upload = async (file) => {
    if (!api.me) { setErr('Sign in to share files.'); return; }
    setBusy((b) => b + 1); setErr('');
    try {
      const r = await fetch(`${base}/api/upload`, { method: 'POST', credentials: 'same-origin',
        headers: { ...headers(), 'Content-Type': file.type || 'application/octet-stream', 'X-Space-Filename': encodeURIComponent(file.name) }, body: file });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.hint || j.error || `HTTP ${r.status}`);
      setUploads((u) => [...u, j]);
    } catch (ex) { setErr(`${file.name}: ${ex.message}`); }
    setBusy((b) => b - 1);
  };
  const onFiles = (list) => { for (const f of Array.from(list || [])) upload(f); };
  const share = async (up, opts) => {
    const data = { title: up.name.slice(0, 120), text: (opts.note || '').slice(0, 4000), kind: opts.kind, source: up.name.slice(0, 200),
      values: opts.values || {}, part: opts.part, excerpt: up.excerpt || '',
      file: { id: up.id, name: up.name, bytes: up.bytes, type: up.type, lines: up.lines ?? null, text: !!up.text } };
    if (replaces != null) data.replaces = replaces;
    try {
      await api.post('finding_posted', data, { subject: opts.part ? `node:${opts.part}` : 'run:main' });
      setUploads((u) => u.filter((x) => x.id !== up.id)); setReplaces(null);
    } catch (ex) { setErr(`Not shared: ${ex && ex.message ? ex.message : ex}`); }
  };
  const shareNote = async (e) => {
    e.preventDefault();
    const t = noteTitle.trim();
    if (!t) { setErr('Give the note a title.'); return; }
    const p = suggestPart(nodes, `${t} ${noteText}`);
    const data = { title: t.slice(0, 120), text: (noteText.trim() || t).slice(0, 4000), kind: 'note', source: 'own work', values: {}, part: p };
    if (replaces != null) data.replaces = replaces;
    try { await api.post('finding_posted', data, { subject: p ? `node:${p}` : 'run:main' }); setNoteTitle(''); setNoteText(''); setNoteOpen(false); setReplaces(null); }
    catch (ex) { setErr(`Not shared: ${ex && ex.message ? ex.message : ex}`); }
  };
  const correct = (f) => { setReplaces(f.seq); setErr(''); if (!f.file) { setNoteOpen(true); setNoteTitle(f.title); setNoteText(f.text); } else if (input.current) input.current.click(); };
  const rows = view.findings.filter((f) => !filter || (f.node || '') === filter);
  const n = view.findings.length;
  return html`<div class="tab-body findings">
    <div class=${`drop${drag ? ' drop--over' : ''}`} onClick=${() => input.current && input.current.click()}
      onDragOver=${(e) => { e.preventDefault(); setDrag(true); }} onDragLeave=${() => setDrag(false)}
      onDrop=${(e) => { e.preventDefault(); setDrag(false); onFiles(e.dataTransfer.files); }}>
      <input ref=${input} type="file" multiple style="display:none" onChange=${(e) => { onFiles(e.target.files); e.target.value = ''; }} />
      <div class="drop__title">${replaces != null ? `Drop the file that replaces e${replaces}` : 'Drop files here, or click to choose'}</div>
      <div class="muted">Data, measurements, papers, notes. CSV, JSON, text, Markdown, PDF, images. The team reads what it can and keeps it in the part's memory.</div>
      ${busy ? html`<div class="muted">uploading...</div>` : null}
    </div>
    ${uploads.map((up) => html`<${Pending} key=${up.id} up=${up} nodes=${nodes} parts=${parts} name=${name} onShare=${(o) => share(up, o)} onDrop=${() => setUploads((u) => u.filter((x) => x.id !== up.id))} />`)}
    <div class="findings__bar">
      <button class="btn btn--small" type="button" onClick=${() => setNoteOpen(!noteOpen)}>${noteOpen ? 'close note' : 'write a note instead'}</button>
      ${replaces != null ? html`<span class="tag tag--warn">replacing e${replaces} <button class="btn btn--small" type="button" onClick=${() => setReplaces(null)}>cancel</button></span>` : null}
      <span class="muted findings__count">${n} shared</span>
      <select value=${filter} onChange=${(e) => setFilter(e.target.value)}><option value="">every part</option>${parts.map((p) => html`<option value=${p.id}>${p.name}</option>`)}</select>
    </div>
    ${noteOpen ? html`<form class="fcard fcard--pending" onSubmit=${shareNote}>
      <input placeholder="Title" value=${noteTitle} onInput=${(e) => setNoteTitle(e.target.value)} maxlength="120" />
      <textarea rows="3" placeholder="What you know, measured or read, in plain words" value=${noteText} onInput=${(e) => setNoteText(e.target.value)}></textarea>
      <div class="fcard__row"><button class="btn btn--small btn--primary" type="submit">Share note</button></div>
    </form>` : null}
    ${err ? html`<div class="error">${err}</div>` : null}
    ${rows.length ? html`<ul class="findings__list">${[...rows].reverse().map((f) => html`<${Finding} key=${f.seq || f.title} f=${f} view=${view} name=${name} base=${base} onCorrect=${correct} />`)}</ul>`
      : html`<div class="muted findings__empty">Nothing shared yet.</div>`}
  </div>`;
}
