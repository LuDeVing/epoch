// people.js: the People button in the top bar. Who is in this space, whether their agent runs, add a person (a name
// and a model: the server starts their agent and hands back the join link), stop an agent, and the link to the hub
// where new spaces are made. Routes: GET /api/people, POST /api/people/add, POST /api/people/stop (space/people.py).
import { html, render, useState, useEffect } from './vendor/standalone.module.js';
import { accounts, useAccount } from './accounts.js';

export const HUB_URL = 'http://127.0.0.1:8760/';

function PeoplePanel({ api, onClose }) {
  const [data, setData] = useState(null);
  const [name, setName] = useState('');
  const [model, setModel] = useState('mock');
  const [busy, setBusy] = useState(false);
  const [err, setErr] = useState('');
  const [made, setMade] = useState(null);
  const base = api.base || '';
  const headers = () => ({ 'Content-Type': 'application/json', 'X-Space-Actor': api.me || '', 'X-Space-Kind': 'human',   // a POST says who sends it: the session must match
    ...(api.flags && api.flags.key ? { 'X-Space-Key': api.flags.key } : {}) });
  const refresh = async () => {
    try {
      const r = await fetch(`${base}/api/people${api.flags && api.flags.key ? `?key=${api.flags.key}` : ''}`, { cache: 'no-store' });
      setData(await r.json());
    } catch (e) { setErr('The server is offline.'); }
  };
  useEffect(() => { refresh(); const t = setInterval(refresh, 4000); return () => clearInterval(t); }, []);
  const post = async (path, body) => {
    const r = await fetch(`${base}${path}`, { method: 'POST', credentials: 'same-origin', headers: headers(), body: JSON.stringify(body) });
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
  const [invites, setInvites] = useState([]);
  const [members, setMembers] = useState(null);
  const [pw, setPw] = useState('');
  const [toName, setToName] = useState('');
  const inviteByName = async (e) => { e.preventDefault(); setBusy(true); setErr(''); try { const j = await post('/api/invites/send', { to: toName }); setMade({ name: j.to, invited: true, again: j.again }); setToName(''); } catch (ex) { setErr(ex.message); } setBusy(false); };
  const kq = api.flags && api.flags.key ? `?key=${encodeURIComponent(api.flags.key)}` : '';   // a --lan space wants its key on GETs too
  const loadInvites = async () => { try { const r = await fetch(`${base}/api/invites${kq}`, { credentials: 'same-origin', cache: 'no-store' }); if (r.ok) setInvites(((await r.json()).invites) || []); } catch (e) { /* offline */ } };
  const loadMembers = async () => { try { const r = await fetch(`${base}/api/members${kq}`, { credentials: 'same-origin', cache: 'no-store' }); if (r.ok) setMembers(await r.json()); } catch (e) { /* offline */ } };
  useEffect(() => { loadInvites(); loadMembers(); }, []);
  const makeInvite = async () => { setBusy(true); setErr(''); try { await post('/api/invites', {}); await loadInvites(); } catch (ex) { setErr(ex.message); } setBusy(false); };
  const setPassword = async (e) => { e.preventDefault(); setBusy(true); setErr(''); try { await post('/api/password', { password: pw }); setPw(''); setMade({ name: api.me, join_url: '', password: true }); } catch (ex) { setErr(ex.message); } setBusy(false); };
  const inviteBase = (data && data.invite_url) ? data.invite_url.split('?')[0] : `${base}/`;
  return html`<div class="start-panel people-panel">
    <div class="start-panel__title">People <span class="muted">${data && data.space_id ? data.space_id : ''}</span>
      <button class="btn btn--small" type="button" style="float:right" onClick=${onClose}>x</button></div>
    <div class="people__me">You are <strong>${api.me || 'not joined'}</strong>
      ${accounts.list().filter((a) => a.name !== api.me).length ? html` <label class="muted">switch to <select onChange=${(e) => { const a = accounts.list().find((x) => x.name === e.target.value); if (a) useAccount(a, base).catch((ex) => setErr(ex.message)); }}>
        <option value="">another account</option>${accounts.list().filter((a) => a.name !== api.me).map((a) => html`<option value=${a.name}>${a.name}</option>`)}</select></label>` : null}
      <button class="btn btn--small" type="button" onClick=${() => { const u = new URL(location.href); u.searchParams.delete('me'); u.searchParams.set('switch', '1'); location.href = u.toString(); }}>add account</button>
      <button class="btn btn--small" type="button" onClick=${async () => { try { await post('/api/logout', { forget: true }); } catch (e) { /* ignore */ } accounts.drop(api.me); const u = new URL(location.href); u.searchParams.delete('me'); location.href = u.toString(); }}>sign out</button></div>
    <div class="people__invite">
      <div class="muted">${members && members.open_to_all ? 'This space is open to every signed-in account.' : `Members: ${((members && members.members) || []).join(', ') || 'none yet'}`}</div>
      <form class="people__add" onSubmit=${inviteByName}><input placeholder="invite by account name, like gio" value=${toName} onInput=${(e) => setToName(e.target.value)} autocomplete="off" />
        <button class="btn btn--small btn--primary" type="submit" disabled=${busy || !toName.trim()}>Invite</button>
        <span class="muted">they see it on their dashboard's bell and accept there; no link needed</span></form>
      ${made && made.invited ? html`<div class="muted">${made.again ? `${made.name} already has an open invitation to this space.` : `Invited ${made.name}. It shows on their dashboard.`}</div>` : null}
      <div><button class="btn btn--small" type="button" disabled=${busy} onClick=${makeInvite}>Make an invitation link instead</button>
        <span class="muted">for someone without an account here yet: they register when they open it</span></div>
      ${invites.length ? html`<ul class="people__list">${invites.slice(0, 6).map((i) => html`<li class="people__row">
          <span class="mono" style="user-select:all">${inviteBase}?invite=${i.code}${data && data.lan ? `&key=${data.invite_url.split('key=')[1] || ''}` : ''}</span>
          <span class=${`tag ${i.used_by ? 'tag--on' : ''}`}>${i.used_by ? `used by ${i.used_by}` : 'open'}</span></li>`)}</ul>` : null}
      ${!(data && data.lan) ? html`<div class="muted">Links work on this PC; for other laptops start the space from the hub with "open to other laptops".</div>` : null}
      <form class="people__add" onSubmit=${setPassword}><input type="password" placeholder="set your password (to sign in elsewhere)" value=${pw} onInput=${(e) => setPw(e.target.value)} />
        <button class="btn btn--small" type="submit" disabled=${busy || pw.length < 4}>Save password</button></form>
    </div>
    ${people.length ? html`<ul class="people__list">${people.map((p) => html`<li class="people__row">
        <strong>${p.name}</strong>
        ${p.account === false ? html`<span class="tag" title="took part in this record; has no account on this PC">author of this record</span>` : html`
        <span class=${`tag ${p.agent && p.agent.alive ? 'tag--on' : ''}`}>${p.agent ? (p.agent.alive ? `agent on ${p.agent.model}` : 'agent stopped') : 'no agent'}</span>
        ${p.agent && p.agent.alive ? html`<button class="btn btn--small" disabled=${busy} onClick=${() => stop(p.name)}>stop agent</button>`
          : html`<button class="btn btn--small" disabled=${busy} onClick=${() => { setName(p.name); }}>start agent</button>`}
        <a class="muted mono" href=${p.join_url} target="_blank" rel="noopener">open as ${p.name}</a>`}
      </li>`)}</ul>` : html`<div class="muted">Nobody yet.</div>`}
    <form class="people__add" onSubmit=${add}>
      <input type="text" placeholder="name, like maria" value=${name} onInput=${(e) => setName(e.target.value)} maxlength="24" />
      <select value=${model} onChange=${(e) => setModel(e.target.value)}>
        <option value="mock">agent: canned replies (no model)</option>
        <option value="sonnet">agent: Sonnet (real model)</option>
      </select>
      <button class="btn btn--small btn--primary" type="submit" disabled=${busy || !name.trim()}>Add a second person on this PC</button>
    </form>
    ${made ? html`<div class="people__made">${made.password ? 'Password saved.' : html`Added ${made.name}. Their link: <span class="mono" style="user-select:all">${made.join_url}</span>`}</div>` : null}
    ${err ? html`<div class="error">${err}</div>` : null}
    <div class="muted people__foot">A second person on this PC opens another browser (Edge next to Chrome) with their link. New spaces: <a href=${HUB_URL} target="_blank" rel="noopener">the hub</a>.</div>
  </div>`;
}

export function mountPeople(el, api = {}) {
  if (!el) return null;
  let open = false;
  const paint = () => render(html`<div class="people">
    <button class="btn btn--small" type="button" onClick=${() => { open = !open; if (open) window.dispatchEvent(new Event('htsa-close-run')); paint(); }}>${open ? 'Close people' : 'People'}</button>
    ${open ? html`<${PeoplePanel} api=${api} onClose=${() => { open = false; paint(); }} />` : null}
  </div>`, el);
  paint();
  window.addEventListener('htsa-close-people', () => { if (open) { open = false; paint(); } });
  return { close: () => { open = false; paint(); } };
}
