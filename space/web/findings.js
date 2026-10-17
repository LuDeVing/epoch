// findings.js: the Findings tab. People put in what they know, measured, read or computed; the loop keeps each
// finding in the part's memory (FACTS FROM PEOPLE) and quotes it to the inventors, critics and builders of that
// part as evidence, never as an instruction. Nothing is deleted: a correction is a new finding that replaces one.
import { html, useState } from './vendor/standalone.module.js';
import { hueOf } from './presence.js';

export const KINDS = ['measurement', 'result', 'paper', 'data', 'note'];
const WORD = /[a-z0-9]+/g;

export function parseValues(text) {
  const out = {};
  for (const line of String(text || '').split(/\n|,|;/)) {
    const m = line.match(/^\s*([A-Za-z_][\w .%/-]*?)\s*=\s*([-+]?\d+(?:\.\d+)?)\s*$/);
    if (m) out[m[1].trim()] = Number(m[2]);
  }
  return out;
}

// The part whose name, id and frame share the most words with the text; null when nothing matches.
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

function Finding({ f, view, onCorrect }) {
  const vals = Object.entries(f.values || {});
  return html`<li class=${`finding${f.replacedBy ? ' finding--replaced' : ''}`}>
    <div class="finding__head">
      <span class=${`tok hue-${hueOf(view, f.by)}`}>${f.by}</span>
      <span class="tag">${f.kind}</span>
      <strong class="finding__title">${f.title}</strong>
      ${f.pending ? html`<span class="tag">sending</span>` : html`<span class="mono muted">[e${f.seq}]</span>`}
      ${f.replacedBy ? html`<span class="tag">replaced by e${f.replacedBy}</span>` : null}
    </div>
    <div class="finding__text">${f.text}</div>
    <div class="muted finding__meta">source: ${f.source}${vals.length ? ` . ${vals.map(([k, v]) => `${k}=${v}`).join(', ')}` : ''}${f.ts ? ` . ${String(f.ts).slice(11, 19)}` : ''}
      ${!f.replacedBy && !f.pending ? html` <button class="btn btn--small" onClick=${() => onCorrect(f)}>correct this</button>` : null}</div>
  </li>`;
}

export function FindingsTab({ view, api }) {
  const nodes = [...view.nodes.values()];
  const parts = nodes.filter((n) => n.kind !== 'root');
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');
  const [part, setPart] = useState('');
  const [kind, setKind] = useState('note');
  const [source, setSource] = useState('own work');
  const [values, setValues] = useState('');
  const [replaces, setReplaces] = useState(null);
  const [filter, setFilter] = useState('');
  const [err, setErr] = useState('');
  const suggested = part ? null : suggestPart(nodes, `${title} ${text}`);
  const name = (id) => (id && view.nodes.get(id) ? view.nodes.get(id).name : id || 'the whole problem');
  const submit = async (e) => {
    e.preventDefault();
    const t = title.trim();
    if (!t) { setErr('A title is needed.'); return; }
    if (!api.me) { setErr('Join with your name first.'); return; }
    const p = part || suggested || null;
    const data = { title: t.slice(0, 120), text: (text.trim() || t).slice(0, 4000), kind, source: (source.trim() || 'own work').slice(0, 200),
      values: parseValues(values), part: p };
    if (replaces != null) data.replaces = replaces;
    setErr('');
    try {
      await api.post('finding_posted', data, { subject: p ? `node:${p}` : 'run:main' });
      setTitle(''); setText(''); setValues(''); setReplaces(null);
    } catch (ex) { setErr(`Not posted: ${ex && ex.message ? ex.message : ex}`); }
  };
  const correct = (f) => {
    setTitle(f.title); setText(f.text); setPart(f.node || ''); setKind(f.kind); setSource(f.source); setReplaces(f.seq);
    setValues(Object.entries(f.values || {}).map(([k, v]) => `${k}=${v}`).join('\n'));
  };
  const rows = view.findings.filter((f) => !filter || (f.node || '') === filter);
  const groups = new Map();
  for (const f of [...rows].reverse()) { const k = f.node || ''; if (!groups.has(k)) groups.set(k, []); groups.get(k).push(f); }
  const n = view.findings.length;
  return html`<div class="tab-body findings">
    <form class="card finding-form" onSubmit=${submit}>
      <div class="card__head">${replaces != null ? `Correct finding e${replaces}` : 'Add what you know'} <span class="muted">the team reads it at the next step</span></div>
      <input placeholder="Title (what you found, measured or read)" value=${title} onInput=${(e) => setTitle(e.target.value)} maxlength="120" />
      <textarea rows="4" placeholder="The finding in plain words: what, how measured, what it means for this problem" value=${text} onInput=${(e) => setText(e.target.value)}></textarea>
      <div class="finding-form__row">
        <label class="muted">Part <select value=${part} onChange=${(e) => setPart(e.target.value)}>
          <option value="">${suggested ? `suggested: ${name(suggested)}` : 'the whole problem'}</option>
          ${parts.map((p) => html`<option value=${p.id}>${p.name}</option>`)}</select></label>
        <label class="muted">Kind <select value=${kind} onChange=${(e) => setKind(e.target.value)}>${KINDS.map((k) => html`<option value=${k}>${k}</option>`)}</select></label>
      </div>
      <div class="finding-form__row">
        <input placeholder="Source: a URL, a file name, or own work" value=${source} onInput=${(e) => setSource(e.target.value)} maxlength="200" />
        <input class="mono" placeholder="values: bins_ratio=1.04, n=100" value=${values} onInput=${(e) => setValues(e.target.value)} />
      </div>
      ${err ? html`<div class="error">${err}</div>` : null}
      <div><button class="btn btn--small btn--primary" type="submit">${replaces != null ? 'Post correction' : 'Post finding'}</button>
        ${replaces != null ? html` <button class="btn btn--small" type="button" onClick=${() => { setReplaces(null); setTitle(''); setText(''); }}>Cancel</button>` : null}</div>
    </form>
    <div class="finding-filter"><label class="muted">Show <select value=${filter} onChange=${(e) => setFilter(e.target.value)}>
      <option value="">every part</option>${parts.map((p) => html`<option value=${p.id}>${p.name}</option>`)}</select></label>
      <span class="muted">${n} finding${n === 1 ? '' : 's'}</span></div>
    ${groups.size ? [...groups].map(([node, fs]) => html`<div class="card"><div class="card__head">${name(node)} <span class="muted">${fs.length}</span></div>
        <ul class="findings__list">${fs.map((f) => html`<${Finding} key=${f.seq || f.title} f=${f} view=${view} onCorrect=${correct} />`)}</ul></div>`)
      : html`<div class="muted">No findings yet. Add a measurement, a result, a paper or a note, and the agents of that part read it as evidence.</div>`}
  </div>`;
}
