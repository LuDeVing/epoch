// app.js: the page shell (docs/MULTIPLAYER_DESIGN.md sections 2, 5 and 16.5). It wires the connection, the store,
// the per-frame apply queue, the query flags (?me= ?stage=1 ?big=1 ?follow= ?poll=1 ?key=), the top bar (hash chip,
// connection chip Live #seq / Reconnecting / Offline, Go with "server offline"), presence beats every 5 s with a
// sendBeacon bye, follow mode, the Replay banner, the strip, and mounts the views:
// mountTree(el, store, bus) from tree.js and mountClusters(el, store, bus) from clusters.js.
import { html, render } from './vendor/standalone.module.js';
import { connectSpace } from './connect.mjs';
import { makeStore } from './store.mjs';
import { makeReducer, trivialLayout, chipText, whoText } from './reduce.mjs';
import { mountRail } from './rail.js';
import { PresenceChips, focusOf } from './presence.js';
import { mountStart } from './start.js';
import { mountInspector } from './inspect.js';
import { mountPeople } from './people.js';
import { mountSplitters, mountStripResizer } from './splitters.js';
import { accounts, useAccount } from './accounts.js';
import { STAGE_DONE, GO_NEXT, STAGE_RUNNING, stripRefs, LEGEND } from './words.mjs';

const BEAT_MS = 5000, GO_LOCK_MS = 2000, OFFLINE_AFTER_MS = 10000, FOCUS_MIN_MS = 250;

// ---- flags -------------------------------------------------------------------------------------------------------
const params = new URLSearchParams(location.search);
const flags = {
  me: (params.get('me') || '').toLowerCase().replace(/[^a-z0-9_]/g, '').slice(0, 24),
  stage: params.get('stage') === '1' || params.get('big') === '1',
  follow: (params.get('follow') || '').toLowerCase(),
  poll: params.get('poll') === '1',
  key: params.get('key') || '',
};
const base = location.origin;
const START_MS = Date.now();
const CLIENT = `c-${Math.random().toString(16).slice(2, 6)}`;
if (flags.stage) document.body.classList.add('stage');

// ---- a tiny bus: state, hover, select, follow, fit, tab, reset ----------------------------------------------------
function makeBus() {
  const m = new Map();
  return {
    on(name, fn) { if (!m.has(name)) m.set(name, new Set()); m.get(name).add(fn); return () => m.get(name).delete(fn); },
    emit(name, payload) { for (const fn of [...(m.get(name) || [])]) { try { fn(payload); } catch (e) { console.error(e); } } },
  };
}
const bus = makeBus();

// ---- small storage helpers (per-viewer conveniences only) ---------------------------------------------------------
const ls = {
  get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
  set(k, v) { try { localStorage.setItem(k, v); } catch (e) { /* private window */ } },
};

// ---- state of the page ---------------------------------------------------------------------------------------------
let R = null, store = null, conn = null, contract = null, layout = trivialLayout, layoutName = 'trivial';
let presence = { clients: [], claims: [] };
let net = { status: 'connecting', since: Date.now(), epoch: null, replay: null, spaceId: null, offsetMs: 0 };
let current = null, queue = [], scheduled = false, opN = 0, goLockUntil = 0;
let loadHead = null;                                         // the log head the server announced; loading ends when the page has it
let following = flags.follow || '';
let focus = null, viewName = 'tree', lastFocusBeat = 0, focusTimer = null, selected = null;
const myClaims = new Map();                                  // subject -> token (takeovers made by this browser)
let lastSeen = Number(ls.get(`htsa.seen.${flags.me}`) || 0);

const serverNow = () => Date.now() + net.offsetMs;

function compose() {
  const v = store.view();
  current = { ...v, presence, me: flags.me ? { name: flags.me, lastSeen } : null, net: { ...net }, layoutName,
    winnerWord: (contract && contract.winner_word) || v.winnerWord, serverNow: serverNow() };
  return current;
}
function publish() {
  compose();
  bus.emit('state', current);
  renderChrome();
  if (loadHead !== null && current.head >= loadHead) loaded();
}
function loaded() {                                          // the loading screen goes once, when the log is read
  loadHead = null;
  document.body.classList.remove('is-loading');
  bus.emit('fit');                                           // the panes had no size while hidden: fit them now
}
setTimeout(() => { if (document.body.classList.contains('is-loading')) loaded(); }, 12000);   // never stuck on it

// ---- the per-frame apply queue: a burst of 300 events paints once -------------------------------------------------
const raf = typeof requestAnimationFrame === 'function' ? requestAnimationFrame : (fn) => setTimeout(fn, 16);
function schedule() {
  if (scheduled) return;
  scheduled = true;
  if (document.hidden) setTimeout(flush, 250); else raf(flush);       // hidden tabs get no frames
}
function flush() {
  scheduled = false;
  const batch = queue; queue = [];
  let changed = false;
  for (const ev of batch) changed = store.applyServer(ev) || changed;
  if (changed) publish();
}

// ---- boot and reset -------------------------------------------------------------------------------------------------
async function loadContract() {
  try { const r = await fetch('contract.json', { cache: 'no-store' }); if (r.ok) return await r.json(); } catch (e) { /* optional */ }
  return null;
}
async function loadLayout() {
  try {
    if (typeof globalThis.d3 === 'undefined') throw new Error('vendor/d3.min.js is not loaded');
    const m = await import('./layout.mjs');
    if (typeof m.layoutTree === 'function' && typeof m.layoutClusters === 'function' && typeof m.anchorFor === 'function') {
      layoutName = 'd3';
      return { layoutTree: m.layoutTree, layoutClusters: m.layoutClusters, anchorFor: m.anchorFor };
    }
  } catch (e) { console.warn('layout.mjs not available, using the trivial layout', e); }
  layoutName = 'trivial';
  return trivialLayout;
}

function start() {
  R = makeReducer({ ...layout, contract });
  store = makeStore(R.reduce, R.init);
  queue = [];
  compose();
  conn = connectSpace({ base, key: flags.key, since: 0, poll: flags.poll,
    onEvent: (ev) => { queue.push(ev); schedule(); }, onStatus, onReset });
  bus.emit('reset', current);
  publish();
}
function onReset() {
  if (conn) conn.close();
  toast('The server has a new log. Reloading from the start.');
  start();
}
function onStatus(kind, info) {
  if (kind === 'live') { if (net.status !== 'rejected') { net.status = 'live'; net.since = Date.now(); } }
  else if (kind === 'reconnecting') {                         // Offline stays until the line is live again
    if (net.status !== 'reconnecting' && net.status !== 'offline' && net.status !== 'rejected') { net.since = Date.now(); net.status = 'reconnecting'; }
  }
  else if (kind === 'hello') {
    if (document.body.classList.contains('is-loading')) { loadHead = Number(info.head || 0); if (!loadHead) loaded(); else if (current && current.head >= loadHead) loaded(); }
    net.epoch = info.epoch || net.epoch;
    net.replay = info.replay || null;
    net.spaceId = info.space_id || net.spaceId;
    if (typeof info.server_time_ms === 'number') net.offsetMs = info.server_time_ms - Date.now();
    if (info.roster || info.claims) presence = { clients: info.roster || presence.clients, claims: info.claims || presence.claims };
  } else if (kind === 'presence') {
    presence = { clients: info.clients || [], claims: info.claims || [] };
    followTick();
  }
  publish();
}
window.addEventListener('htsa-run', () => renderChrome());  // the run chip learned something new: the top bar follows
setInterval(() => {                                          // Reconnecting turns Offline after 10 s
  if (net.status === 'reconnecting' && Date.now() - net.since > OFFLINE_AFTER_MS) { net.status = 'offline'; publish(); }
}, 1000);

// ---- writes ------------------------------------------------------------------------------------------------------------
function headers() {
  const h = { 'Content-Type': 'application/json', 'X-Space-Actor': flags.me, 'X-Space-Kind': 'human' };
  if (flags.key) h['X-Space-Key'] = flags.key;
  return h;
}
const ENVELOPE = ['subject', 'label', 'base', 'round', 'stage', 'claim', 'cause'];

let loginShown = false;
function needLogin() { if (loginShown) return; loginShown = true; toast('Sign in to take part.'); const u = new URL(location.href); u.searchParams.delete('me'); setTimeout(() => location.replace(u.toString()), 900); }
export async function post(kind, data, extra = {}) {
  if (!flags.me) { toast('Join with your name first.'); return null; }
  if (flags.stage) return null;                              // the projector never writes
  const op = `${flags.me}-${START_MS}-${++opN}`;
  const body = { kind, data, op, base: store.last() };
  for (const k of ENVELOPE) if (extra[k] !== undefined) body[k] = extra[k];
  store.addPending(op, { ...body, by: flags.me, by_kind: 'human', owner: flags.me });
  publish();
  let res = null;
  try {
    const r = await fetch(`${base}/api/events`, { method: 'POST', headers: headers(), body: JSON.stringify(body) });
    res = await r.json().catch(() => ({}));
    if (r.ok) {
      store.queued(op, res.seq);
      if (res.warn === 'claimed_by_other') toast('Someone else holds a claim here. Your change is kept and marked.');
      if (Array.isArray(res.overwrote) && res.overwrote.length) {
        const o = res.overwrote[0];
        toast(`Your change replaced ${whoText({ cls: 'person', owner: String(o.by || '').split('.')[0] })}'s at #${o.seq}.`);
      }
    } else {
      store.reject(op);
      if (r.status === 401) needLogin();
      else toast(chipText({ status: 'rejected', reason: res.error || `http ${r.status}` }));
    }
  } catch (e) {
    store.reject(op);
    toast('rejected: server offline');
  }
  publish();
  return res;
}

export async function claim(action, subject, extra = {}) {
  if (!flags.me || flags.stage) return null;
  const body = { action, subject, ttl_s: 90, ...extra };
  if (myClaims.has(subject)) body.token = myClaims.get(subject);
  try {
    const r = await fetch(`${base}/api/claims`, { method: 'POST', headers: headers(), body: JSON.stringify(body) });
    const res = await r.json().catch(() => ({}));
    if (r.ok && res.token != null && action !== 'release') myClaims.set(subject, res.token);
    if (action === 'release') myClaims.delete(subject);
    if (!r.ok) toast(`claim: ${res.error || r.status}${res.held_by ? ` (held by ${res.held_by})` : ''}`);
    return res;
  } catch (e) { toast('claim: server offline'); return null; }
}

// ---- presence: a beat every 5 s, at once on a focus change (at most 4 a second), a bye on pagehide ----------------
function beatBody(bye = false) {
  return { client: CLIENT, name: flags.me, owner: flags.me, kind: 'human', view: viewName, focus,
    activity: { state: 'watching', text: '', stage: current && current.run.stage }, cursor: store ? store.last() : 0,
    claims: [...myClaims].map(([subject, token]) => ({ subject, token })), bye };
}
async function beat() {
  if (!flags.me || flags.stage) return;
  lastFocusBeat = Date.now();
  try {
    const r = await fetch(`${base}/api/presence`, { method: 'POST', headers: headers(), body: JSON.stringify(beatBody()) });
    const res = await r.json().catch(() => ({}));
    if (r.status === 403 && res.error === 'bad_key') { if (net.status !== 'rejected') { net.status = 'rejected'; publish(); } return; }
    if (net.status === 'rejected' && r.ok) { net.status = 'live'; publish(); }
    for (const it of res.interrupts || []) {
      if (it.type === 'claim_lost') { myClaims.delete(it.subject); toast(`You lost the claim on ${it.subject}.`); }
    }
  } catch (e) { /* the connection chip already says so */ }
}
setInterval(beat, BEAT_MS);
function focusChanged(f) {
  focus = f ? { type: f.type, id: f.id } : null;
  clearTimeout(focusTimer);
  const wait = Math.max(0, FOCUS_MIN_MS - (Date.now() - lastFocusBeat));
  focusTimer = setTimeout(beat, wait);
}
bus.on('hover', focusChanged);
bus.on('select', (sel) => { focusChanged(sel); if (sel && sel.type === 'node') selected = sel.id; });
addEventListener('pagehide', () => {
  if (!flags.me || flags.stage) return;
  const url = `${base}/api/presence?me=${encodeURIComponent(flags.me)}&kind=human${flags.key ? `&key=${encodeURIComponent(flags.key)}` : ''}`;
  try { navigator.sendBeacon(url, new Blob([JSON.stringify(beatBody(true))], { type: 'application/json' })); } catch (e) { /* best effort */ }
});
document.addEventListener('visibilitychange', () => {
  if (!document.hidden && current) { lastSeen = current.head; ls.set(`htsa.seen.${flags.me}`, String(lastSeen)); }
});

// ---- follow mode: a coloured frame; stops on click or wheel ----------------------------------------------------------
let lastFollowFocus = '';
function setFollow(who) {
  following = who || '';
  lastFollowFocus = '';
  document.body.classList.toggle('following', !!following);
  const owner = following.replace(/\.agent$/, '');
  const hue = current && current.people.get(owner) ? current.people.get(owner).hue : 'team';
  document.body.dataset.followHue = hue;
  const banner = document.getElementById('follow-banner');
  if (banner) {
    banner.hidden = !following;
    banner.textContent = following ? `Following ${whoText({ cls: following.endsWith('.agent') ? 'delegate' : 'person', owner })}${flags.stage ? '' : '. Click or scroll to stop.'}` : '';
  }
  followTick();
  renderChrome();
}
function followTick() {
  if (!following || !current) return;
  const f = focusOf({ ...current, presence }, following);
  const k = JSON.stringify(f);
  if (f && k !== lastFollowFocus) { lastFollowFocus = k; bus.emit('follow', { who: following, focus: f }); }
}
const stopFollow = () => { if (following && !flags.stage) setFollow(''); };
document.addEventListener('wheel', stopFollow, { passive: true });
document.addEventListener('mousedown', (e) => { if (!e.target.closest || !e.target.closest('.chip')) stopFollow(); });

// ---- Go -------------------------------------------------------------------------------------------------------------------
function goState() {
  const run = current ? current.run : null;
  const down = net.status !== 'live';
  if (down) return { label: 'server offline', disabled: true, hidden: true };
  if (!run || !run.waiting || !run.lastBoundary) return { label: 'Go', disabled: true, hidden: true };
  const next = GO_NEXT[run.stage] || 'continue';
  if (Date.now() < goLockUntil) return { label: `Go: ${next}`, disabled: true };
  return { label: `Go: ${next}`, disabled: !flags.me || flags.stage, title: `The team waits here so people can steer. Go releases it to ${next}.` };
}
async function pressGo() {
  const b = current && current.run.lastBoundary;
  if (!b) return;
  goLockUntil = Date.now() + GO_LOCK_MS;
  setTimeout(renderChrome, GO_LOCK_MS + 20);
  renderChrome();
  await post('run_step', { round: b.round, stage: b.stage }, { round: b.round, stage: b.stage });
}

// ---- top bar, banners, strip -----------------------------------------------------------------------------------------
// the dashboard (space/hub.py) on the same host, port 8760 unless the page was opened with ?hub=<url>
function hubUrl() {
  try {
    if (params.get('hub')) return params.get('hub');
    return `${location.protocol}//${location.hostname}:8760/`;
  } catch (e) { return 'http://127.0.0.1:8760/'; }
}
function connText() {
  if (net.status === 'live') return `Live #${current ? current.head : 0}`;
  if (net.status === 'offline') return 'Offline';
  if (net.status === 'rejected') return 'This link is out of date: open the space from the hub again';
  if (net.status === 'reconnecting') return 'Reconnecting';
  return 'Connecting';
}
function runText(run) {
  if (!run.stage) {
    const ph = typeof document !== 'undefined' ? document.body.dataset.phase || '' : '';
    if (ph) {
      const m = /^round (\d+): (\w+)/.exec(ph);
      const word = m ? ({ researching: 'reading up before the ideas', ideating: 'inventing', clustering: 'grouping', deepening: 'arguing', building: 'building', verifying: 'testing', planning: 'planning' }[m[2]] || m[2]) : ph;
      return m ? `Round ${m[1]}: ${word}` : `Research running: ${ph}`;
    }
    if (typeof document !== 'undefined' && document.body.dataset.run === 'running') return 'Research starting';
    return 'No research running';
  }
  if (typeof document !== 'undefined' && document.body.dataset.run === 'finished' && !run.waiting) return `Finished after round ${run.round}`;
  if (typeof document !== 'undefined' && (document.body.dataset.run === 'failed' || document.body.dataset.run === 'stopped') && !run.waiting) return `Stopped in round ${run.round}`;
  const paused = run.pausedBy.length ? `, paused by ${run.pausedBy.map((p) => whoText({ cls: 'person', owner: p })).join(' and ')}` : '';
  if (run.waiting) return `Round ${run.round}: ${STAGE_DONE[run.stage] || run.stage}. Waiting for Go${paused}`;
  return `Round ${run.round}: ${STAGE_RUNNING[run.stage] || run.stage}${paused}`;
}
function Topbar({ v }) {
  const run = v.run;
  const g = goState();
  const space = v.spaceId || net.spaceId || 'space';
  const others = [...v.people.keys()].filter((p) => p !== flags.me);
  return html`<div class="topbar__line">
      <a class="brand brand--link" href=${hubUrl()} title="back to the dashboard: all your spaces">Epoch</a><span class="dot-sep">.</span><span class="space-name">${space}</span>
      <a class="btn btn--small topbar__back" href=${hubUrl()} title="all your spaces">Dashboard</a>
      <span class="dot-sep">.</span><span class=${`runstate${run.waiting ? ' runstate--waiting' : ''}`} title=${run.stage ? `stage ${run.stage}, event #${v.head}` : ''}>${runText(run)}</span>
      ${!g.hidden ? html`<button class="btn btn--primary btn--go" disabled=${g.disabled} title=${g.title || ''} onClick=${pressGo}>${g.label}</button>` : null}
      <span class=${`conn conn--${net.status}`} title=${`connection: ${connText()}`}>${net.status === 'live' ? '' : connText()}</span>
    </div>
    <div class="topbar__line">
      <${PresenceChips} view=${v} nowMs=${serverNow()} following=${following} onFollow=${(who) => setFollow(following === who ? '' : who)} />
      ${others.length || following ? html`<button class=${`btn btn--small${following ? ' btn--on' : ''}`} title="See what another person is looking at; your view follows theirs until you click or scroll"
        onClick=${() => setFollow(following ? '' : (flags.follow || others[0] || ''))}>${following ? `Stop following ${whoText({ cls: 'person', owner: following.replace(/\.agent$/, '') })}` : `Follow ${whoText({ cls: 'person', owner: others[0] })}`}</button>` : null}
    </div>`;
}
function Strip({ v }) {
  const mine = flags.me ? v.digests.filter((d) => d.agent === `${flags.me}.agent`).at(-1) : null;
  const latest = mine || v.digests.at(-1);
  const receipt = flags.me ? v.feed.filter((l) => l.owner === flags.me && l.receipt).at(-1) : v.feed.filter((l) => l.receipt).at(-1);
  const agentLines = flags.stage ? [...v.chat.values()].flat().filter((l) => l.from && l.from.endsWith('.agent')).sort((a, b) => a.seq - b.seq).slice(-3) : [];
  const rName = (a) => (a === 'team.loop' ? 'the team' : a.endsWith('.agent') ? `${whoText({ cls: 'person', owner: a.slice(0, -6) })}'s agent` : a);
  const plain = (t) => t.replace(/ via agent/g, "'s agent").replace(/\bsketches\b/g, 'ideas').replace(/\bsketch\b/g, 'idea')
    .replace(/\bclusters\b/g, 'groups').replace(/\bcluster\b/g, 'group').replace(/the team team question is now/g, "the team's next question is").replace(/^- /gm, '');
  const body = latest && latest.text ? plain(stripRefs(latest.text.split('\n').slice(1).join('\n'))).trim() : '';
  return html`<div class="strip__digest">${latest ? html`<strong>What ${rName(latest.agent)} was told</strong><span class="muted"> before its last step (round ${latest.round}, ${STAGE_DONE[latest.stage] || latest.stage}): ${latest.n} change${latest.n === 1 ? '' : 's'} by teammates</span>`
      : html`<span class="muted">Before each step, every agent is told what the others changed. That note shows here.</span>`}</div>
    ${body ? html`<pre class="strip__text">${body}</pre>` : null}
    ${receipt && !flags.stage ? html`<div class="muted">Your "${receipt.text}" reached ${rName(receipt.receipt.agent)} in round ${receipt.receipt.round}.</div>` : null}
    ${agentLines.map((l) => html`<div class="strip__agent"><span class="spark" aria-hidden="true"></span>${l.from}: ${l.text}</div>`)}`;
}
function renderChrome() {
  if (!current) return;
  const top = document.getElementById('topbar');
  if (top && (flags.me || flags.stage)) render(html`<${Topbar} v=${current} />`, top);   // else the join form stays
  const strip = document.getElementById('strip');
  if (strip) render(html`<${Strip} v=${current} />`, strip);
  const rb = document.getElementById('replay-banner');
  if (rb) {
    const rp = net.replay;
    rb.hidden = !rp;
    rb.textContent = rp ? `Replay of a recorded round${rp.file ? ` (${String(rp.file).split(/[\\/]/).pop()}` : ''}${rp.speed ? `, speed ${rp.speed}x` : ''}${rp.file ? ')' : ''}` : '';
  }
}

// ---- toasts ----------------------------------------------------------------------------------------------------------
export function toast(text) {
  const box = document.getElementById('toasts');
  if (!box) return;
  const el = document.createElement('div');
  el.className = 'toast';
  el.textContent = text;
  box.appendChild(el);
  setTimeout(() => el.remove(), 5000);
}

// ---- join: names are typed, no login ----------------------------------------------------------------------------------
// Local use: nobody types a name. The browser remembers who you are; the first time, the server offers the OS
// login of this PC. The page then reopens itself with ?me=<name>, which the rest of the code reads as before.
async function autoJoin() {
  const clean = (x) => String(x || '').toLowerCase().replace(/[^a-z0-9_]/g, '').slice(0, 24);
  const kq = flags.key ? `?key=${encodeURIComponent(flags.key)}` : '';
  let name = '';
  try {
    const r = await fetch(`${base}/api/me${kq}`, { cache: 'no-store', credentials: 'same-origin' });
    if (r.ok) name = clean((await r.json()).name);
  } catch (e) { name = ''; }
  if (!name) return false;
  if (!accounts.list().some((a) => a.name === name)) { /* signed in by cookie only: nothing to save without its token */ }
  const code = params.get('invite');
  if (code) {                                            // signed in and holding an invitation: join this space
    try { await fetch(`${base}/api/invites/accept${kq}`, { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ code }) }); } catch (e) { /* shown later */ }
  }
  const u = new URL(location.href); u.searchParams.set('me', name); u.searchParams.delete('invite');
  location.replace(u.toString());
  return true;
}

// Sign in with a password, register, continue as a saved account, or join with an invitation (?invite=).
function askLogin() {
  const top = document.getElementById('topbar');
  const invite = params.get('invite') || '';
  let mode = invite ? 'register' : 'login', err = '';
  const saved = accounts.list();
  const go = async (e) => {
    e.preventDefault();
    const f = e.target.elements;
    const body = { name: f.name.value, password: f.password.value };
    if (invite) body.invite = invite;
    try {
      const r = await fetch(`${base}/api/${mode}${flags.key ? `?key=${encodeURIComponent(flags.key)}` : ''}`, { method: 'POST', credentials: 'same-origin',
        headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(body) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) { err = j.hint || j.error || `HTTP ${r.status}`; draw(); return; }
      accounts.save(j.name, j.token);
      const u = new URL(location.href); u.searchParams.set('me', j.name); u.searchParams.delete('invite'); u.searchParams.delete('switch'); location.replace(u.toString());
    } catch (ex) { err = 'The server is offline.'; draw(); }
  };
  const draw = () => render(html`<form class="join" onSubmit=${go}>
    <span class="brand">Epoch space</span>
    ${saved.length ? html`<span class="join__saved">${saved.map((a) => html`<button class="btn btn--small" type="button" onClick=${() => useAccount(a).catch((ex) => { err = ex.message; draw(); })}>Continue as ${a.name}</button>`)}</span>` : null}
    ${invite ? html`<span class="tag">invitation ${invite.slice(0, 6)}...</span>` : null}
    <label>Name <input name="name" autocomplete="username" autofocus /></label>
    <label>Password <input name="password" type="password" autocomplete=${mode === 'login' ? 'current-password' : 'new-password'} /></label>
    <button class="btn btn--primary" type="submit">${mode === 'login' ? 'Sign in' : 'Create account'}</button>
    <button class="btn" type="button" onClick=${() => { mode = mode === 'login' ? 'register' : 'login'; err = ''; draw(); }}>${mode === 'login' ? 'New here? Register' : 'I have an account'}</button>
    ${err ? html`<span class="error">${err}</span>` : null}
    <span class="muted">or open with ?stage=1 to watch</span></form>`, top);
  draw();
}


// Signed in, but not a member of this space: say so plainly, with the way back, instead of an empty space.
function notMember(name) {
  flags.me = '';
  document.body.classList.remove('is-loading');
  const hub = `${location.protocol}//${location.hostname}:8760/`;
  const box = document.getElementById('loading');
  if (box) { box.innerHTML = ''; document.body.classList.add('is-loading'); }
  render(html`<div class="notmember"><span class="loading__text">This space is private</span>
    <span class="loading__sub">You are signed in as ${name}, who is not a member. Ask a member to invite you by name; the invitation then appears on your dashboard's bell.</span>
    <a class="btn btn--primary" href=${hub}>Back to the dashboard</a></div>`, box || document.body);
}

function askName() {
  const top = document.getElementById('topbar');
  const done = (name) => {
    const n = String(name || '').toLowerCase().replace(/[^a-z0-9_]/g, '').slice(0, 24);
    if (!n) return;
    const u = new URL(location.href); u.searchParams.set('me', n);
    location.replace(u.toString());
  };
  render(html`<form class="join" onSubmit=${(e) => { e.preventDefault(); done(e.target.elements.name.value); }}>
    <span class="brand">Epoch space</span> <label>Your name <input name="name" autocomplete="off" autofocus /></label>
    <button class="btn btn--primary" type="submit">Join</button>
    <span class="muted">or open with ?stage=1 to watch</span></form>`, top);
}

// ---- the views: tree.js and clusters.js (owned by the views part); a plain list until they are installed -------------
const viewApi = {
  view: () => current,
  last: () => (store ? store.last() : 0),
  status: (op) => (store ? store.status(op) : undefined),
  subscribe: (fn) => bus.on('state', fn),
  me: flags.me, flags, base, bus, post, claim, toast,
  following: () => following,
  selected: () => selected,
  setView: (name) => { viewName = name; },
};

function fallbackTree(el) {
  const box = document.createElement('div');
  box.className = 'fallback';
  el.appendChild(box);
  const draw = (v) => {
    const kids = new Map();
    for (const n of v.nodes.values()) { const p = n.parent == null ? '' : n.parent; if (!kids.has(p)) kids.set(p, []); kids.get(p).push(n); }
    const rows = [];
    const walk = (p, d) => { for (const n of (kids.get(p) || []).sort((a, b) => a.firstSeen - b.firstSeen)) { rows.push([n, d]); if (d < 6) walk(n.id, d + 1); } };
    walk('', 0);
    render(html`<ul class="fallback__list">${rows.map(([n, d]) => html`<li style=${`padding-left:${d * 16}px`}
      class=${`hue-${n.owner && v.people.get(n.owner) ? v.people.get(n.owner).hue : 'team'} st--${n.status}`}
      onClick=${() => bus.emit('select', { type: 'node', id: n.id })}>${n.name}
      ${n.status !== 'map' ? html` <span class="state-chip">${chipText(n, v.run)}</span>` : null}
      ${n.claim ? html` <span class="tag">${n.claim.holder}</span>` : null}${n.skippedBy ? html` <span class="tag">skipped</span>` : null}</li>`)}</ul>`, box);
  };
  bus.on('state', draw);
  if (current) draw(current);
}
function fallbackClusters(el) {
  const box = document.createElement('div');
  box.className = 'fallback';
  el.appendChild(box);
  const draw = (v) => {
    const byNode = new Map();
    for (const c of v.clusters.values()) { if (!byNode.has(c.node)) byNode.set(c.node, []); byNode.get(c.node).push(c); }
    render(html`${[...byNode].map(([node, cs]) => html`<div class="fallback__island"><div class="muted">${(v.nodes.get(node) || { name: node }).name}</div>
      ${cs.map((c) => html`<span class=${`bubble-chip st--${c.status}`} title=${c.key}>${c.name} (${c.n})${c.status !== 'open' ? ` . ${c.status}` : ''}</span>`)}</div>`)}`, box);
  };
  bus.on('state', draw);
  if (current) draw(current);
}
function mountLegend(pane, which, title) {
  if (!pane) return;
  const btn = document.createElement('button');
  btn.className = 'pane__help';
  btn.type = 'button';
  btn.title = title;
  btn.textContent = '?';
  const box = document.createElement('div');
  box.className = 'legend';
  box.style.display = 'none';
  pane.appendChild(btn);
  pane.appendChild(box);
  const rows = LEGEND[which] || [];
  box.innerHTML = `<div class="legend__head"><strong>${title}</strong><button class="btn btn--small" type="button">x</button></div>` +
    rows.map(([k, v]) => `<div class="legend__row"><span class="legend__k">${k}</span><span class="legend__v">${v}</span></div>`).join('');
  const toggle = () => { box.style.display = box.style.display === 'none' ? '' : 'none'; };
  btn.addEventListener('click', toggle);
  box.querySelector('button').addEventListener('click', toggle);
}

async function mountViews() {
  const tree = document.getElementById('tree-pane'), clusters = document.getElementById('clusters-pane');
  try { const m = await import('./tree.js'); m.mountTree(tree, viewApi, bus); }
  catch (e) { console.warn('tree.js not available, showing a plain list', e); fallbackTree(tree); }
  try { const m = await import('./clusters.js'); m.mountClusters(clusters, viewApi, bus); }
  catch (e) { console.warn('clusters.js not available, showing a plain list', e); fallbackClusters(clusters); }
  try { mountInspector(tree, clusters, viewApi, bus); } catch (e) { console.warn('inspector not mounted', e); }
  try { mountLegend(tree, 'tree', 'How to read the map'); mountLegend(clusters, 'clusters', 'How to read the ideas'); } catch (e) { console.warn('legend not mounted', e); }
}

// ---- main -------------------------------------------------------------------------------------------------------------
async function main() {
  [contract, layout] = await Promise.all([loadContract(), loadLayout()]);
  start();
  if (!flags.me && !flags.stage) { if (params.get('switch') !== '1' && await autoJoin()) return; askLogin(); return; }
  if (flags.me && !flags.stage) {                            // a link with a name but no session behind it: sign in first
    try {
      const r = await fetch(`${base}/api/me${flags.key ? `?key=${encodeURIComponent(flags.key)}` : ''}`, { cache: 'no-store', credentials: 'same-origin' });
      if (r.status === 401) { flags.me = ''; askLogin(); return; }   // the top bar then leaves the form alone
      const j = r.ok ? await r.json().catch(() => ({})) : {};
      if (j.member === false) { notMember(j.name); return; }
    } catch (e) { /* offline: the page says so itself */ }
  }
  if (flags.me) ls.set('htsa.me', flags.me);
  mountRail(document.getElementById('rail'), viewApi);
  mountStart(document.getElementById('start-run'), viewApi);
  mountPeople(document.getElementById('people-panel'), viewApi);
  await mountViews();
  try { mountSplitters(document.getElementById('panes')); mountStripResizer(document.getElementById('strip')); } catch (e) { console.warn('splitters not mounted', e); }
  if (following) setFollow(following);
  publish();
  beat();
}
main();
