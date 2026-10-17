// people.js: the People button in the top bar. Who is in this space, whether their agent runs, add a person (a name
// and a model: the server starts their agent and hands back the join link), stop an agent, and the link to the hub
// where new spaces are made. Routes: GET /api/people, POST /api/people/add, POST /api/people/stop (space/people.py).
import { html, render, useState, useEffect } from './vendor/standalone.module.js';

export const HUB_URL = 'http://127.0.0.1:8760/';

function PeoplePanel({ api, onClose }) {
  const [data, setData] = useState(null);
  const [name, setName] = useState('');
  const [model, setModel] = useState('mock');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const [made, setMade] = useState(null);
  const base = api.base || '';
  const headers = () => ({ 'Content-Type': 'application/json', ...(api.flags && api.flags.key ? { 'X-Space-Key': api.flags.key } : {}) });
  const refresh = async () => {
    try {
      const r = await fetch(`${base}/api/people${api.flags && api.flags.key ? `?key=${api.flags.key}` : ''}`, { cache: 'no-store' });
      setData(await r.json());
    } catch (e) { setErr('The server is offline.'); }
  };
  useEffect(() => { refresh(); const t = setInterval(refresh, 4000); return () => clearInterval(t); }, []);
  const post = async (path, body) => {
    const r = await fetch(`${base}${path}`, { method: 'POST', headers: headers(), body: JSON.stringify(body) });
    const j = await r.json().catch(() => ({}));
    if (!r.ok) throw new Error(j.error ? `${j.error}${j.hint ? `: ${j.hint}` : ''}` : `HTTP ${r.status}`);
    return j;
  };
  const add = async (e) => {
    e.preventDefault();
    setBusy(true); setErr(''); setMade(null);
    try { const j = await post('/api/people/add', { name, model }); setMade(j); setName(''); await refresh(); }
    catch (ex) { setErr(ex.message); }
    setBusy(false);
  };
  const stop = async (n) => { setBusy(true); setErr(''); try { await post('/api/people/stop', { name: n }); await refresh(); } catch (ex) { setErr(ex.message); } setBusy(false); };
  const people = (data && data.people) || [];
  return html`<div class="start-panel people-panel">
    <div class="start-panel__title">People in this space <span class="muted">${data && data.space_id ? data.space_id : ''}</span>
      <button class="btn btn--small" type="button" style="float:right" onClick=${onClose}>x</button></div>
    ${people.length ? html`<ul class="people__list">${people.map((p) => html`<li class="people__row">
        <strong>${p.name}</strong>
        <span class=${`tag ${p.agent && p.agent.alive ? 'tag--on' : ''}`}>${p.agent ? (p.agent.alive ? `agent on ${p.agent.model}` : 'agent stopped') : 'no agent'}</span>
        ${p.agent && p.agent.alive ? html`<button class="btn btn--small" disabled=${busy} onClick=${() => stop(p.name)}>stop agent</button>`
          : html`<button class="btn btn--small" disabled=${busy} onClick=${() => { setName(p.name); }}>start agent</button>`}
        <a class="muted mono" href=${p.join_url} target="_blank" rel="noopener">open as ${p.name}</a>
      </li>`)}</ul>` : html`<div class="muted">Nobody yet.</div>`}
    <form class="people__add" onSubmit=${add}>
      <input type="text" placeholder="name, like maria" value=${name} onInput=${(e) => setName(e.target.value)} maxlength="24" />
      <select value=${model} onChange=${(e) => setModel(e.target.value)}>
        <option value="mock">agent: canned replies (no model)</option>
        <option value="sonnet">agent: Sonnet (real model)</option>
      </select>
      <button class="btn btn--small btn--primary" type="submit" disabled=${busy || !name.trim()}>Add person and start their agent</button>
    </form>
    ${made ? html`<div class="people__made">Added ${made.name}. Their link: <span class="mono" style="user-select:all">${made.join_url}</span></div>` : null}
    ${err ? html`<div class="error">${err}</div>` : null}
    <div class="muted people__foot">A person can also just open <span class="mono">${base}/?me=&lt;name&gt;</span>. New spaces: <a href=${HUB_URL} target="_blank" rel="noopener">the hub</a>.</div>
  </div>`;
}

export function mountPeople(el, api = {}) {
  if (!el) return null;
  let open = false;
  const paint = () => render(html`<div class="people">
    <button class="btn btn--small" type="button" onClick=${() => { open = !open; paint(); }}>${open ? 'Close people' : 'People'}</button>
    ${open ? html`<${PeoplePanel} api=${api} onClose=${() => { open = false; paint(); }} />` : null}
  </div>`, el);
  paint();
  return { close: () => { open = false; paint(); } };
}
