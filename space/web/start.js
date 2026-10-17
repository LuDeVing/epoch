// start.js: "Start a research" (part P8, start-run; the routes are in space/launch.py).
// A button in the top bar opens a panel: profile, size with the estimate per preset (calls, tokens, minutes), Mock or
// Real, a confirm step for Real that repeats the estimate in words, Start. A status chip (running, finished, failed,
// stopped) with Stop. GET /api/run/status every 3 s while a run is alive.
// mountStart(el, api): api is app.js's viewApi ({ me, flags, base, subscribe }). Colours come from tokens.css only.
import { html, render } from './vendor/standalone.module.js';
import { mountWizard } from './wizard.js';

export const POLL_MS = 3000;
const IDLE_CHECK_MS = 15000;           // without a live run: look again at most this often, on page activity
const SIZE_TEXT = { demo: 'Demo', small: 'Small', medium: 'Medium', big: 'Big' };

// ---- pure helpers (tested under Node) -----------------------------------------------------------------------------
export function fmtTokens(n) {
  const v = Number(n) || 0;
  if (v >= 1e6) return `${(v / 1e6).toFixed(v % 1e6 === 0 ? 0 : 1)}M`;
  if (v >= 1e3) return `${Math.round(v / 1e3)}k`;
  return String(v);
}

export function estimateLine(e) {
  if (!e) return '';
  return `${e.calls} calls, ${fmtTokens(e.tokens)} tokens${e.capped ? ' (budget cap)' : ''}, about ${e.minutes} min`;
}

export function presetLine(p) {
  if (!p) return '';
  const r = p.rounds === 1 ? '1 round' : `${p.rounds} rounds`;
  const s = p.max_sketch_calls ? `${p.max_sketch_calls} idea agents` : 'no idea cap';
  return `${r}, ${p.implement} builds, ${s} per round`;
}

// The chip of one run: { state, cls, text }.
export function chipOf(run) {
  if (!run) return null;
  const state = run.alive ? 'running' : (run.state || (run.rc === 0 ? 'finished' : 'failed'));
  const what = `${run.preset || ''} ${run.mode || ''}`.trim();
  let text;
  const mins = run.elapsed_s != null ? `${Math.max(1, Math.round(run.elapsed_s / 60))} min` : '';
  const live = run.live || null;
  const spent = live && live.spent ? `${fmtTokens(live.spent)} tokens` : '';
  if (state === 'running') {
    const phase = live && live.phase ? String(live.phase).replace(/^round (\d+): /, 'r$1 ') : 'starting';
    const busy = live && live.inflight ? `${live.inflight} call${live.inflight === 1 ? '' : 's'} out` : '';
    text = ['Running', phase, spent, busy, mins].filter(Boolean).join(' . ');
  } else if (state === 'finished') text = ['Finished', what, spent, mins].filter(Boolean).join(' . ');
  else if (state === 'stopped') text = ['Stopped', what, spent, mins].filter(Boolean).join(' . ');
  else text = ['Failed', what, run.rc == null ? '' : `exit ${run.rc}`, mins].filter(Boolean).join(' . ');
  return { state, cls: `run-chip run-chip--${state}`, text, note: live && live.note ? String(live.note) : '' };
}

// ---- the mount ------------------------------------------------------------------------------------------------------
export function mountStart(el, api = {}) {
  if (!el) return null;
  const flags = api.flags || {};
  const base = api.base || (typeof location !== 'undefined' ? location.origin : '');
  const canStart = !!api.me && !flags.stage;           // the projector never writes; a person joins first
  const S = {
    open: false, loaded: false, profiles: [], presets: {}, order: ['demo', 'small', 'medium', 'big'],
    profile: '', preset: 'demo', mode: 'real', confirming: false, busy: false, error: '',
    runs: [], showLog: false, showReport: false, report: null,
    problem: { title: '', goal: '', success: '', known: '', fixed: '', parts: '', field: '' },
  };
  let timer = null, lastCheck = 0;
  const wizard = mountWizard(api);
  const describe = () => wizard.open(S.problem, (sp) => { S.problem = sp; S.profile = '__custom__'; S.confirming = false; S.open = true; draw(); });

  const headers = () => {
    const h = { 'Content-Type': 'application/json', 'X-Space-Actor': api.me || 'anon', 'X-Space-Kind': 'human' };
    if (flags.key) h['X-Space-Key'] = flags.key;
    return h;
  };
  const q = flags.key ? `?key=${encodeURIComponent(flags.key)}` : '';
  async function getJson(path) {
    const r = await fetch(`${base}${path}${path.includes('?') ? q.replace('?', '&') : q}`, { cache: 'no-store', headers: headers() });
    const b = await r.json().catch(() => ({}));
    if (!r.ok) throw Object.assign(new Error(b.error || `http ${r.status}`), { body: b, status: r.status });
    return b;
  }
  async function postJson(path, body) {
    const r = await fetch(`${base}${path}`, { method: 'POST', headers: headers(), body: JSON.stringify(body) });
    const b = await r.json().catch(() => ({}));
    return { ok: r.ok, status: r.status, body: b };
  }

  const latest = () => S.runs[0] || null;
  const alive = () => S.runs.some((r) => r.alive);

  async function loadProfiles() {
    try {
      const b = await getJson('/api/run/profiles');
      S.profiles = b.profiles || [];
      S.presets = b.presets || {};
      S.order = b.order || S.order;
      if (!S.profile) S.profile = b.default_profile || (S.profiles[0] && S.profiles[0].name) || '';
      S.loaded = true;
    } catch (e) { S.error = `Could not load the profiles: ${e.message}`; }
    draw();
  }

  async function refresh() {
    lastCheck = Date.now();
    try {
      const b = await getJson('/api/run/status');
      S.runs = b.runs || [];
    } catch (e) { /* the connection chip already says when the server is down */ }
    schedule();
    draw();
  }
  function schedule() {
    clearTimeout(timer);
    timer = null;
    if (alive()) timer = setTimeout(refresh, POLL_MS);
  }

  async function start() {
    if (S.busy) return;
    if (S.mode === 'real' && !S.confirming) { S.confirming = true; draw(); return; }
    S.busy = true; S.error = ''; draw();
    const custom = S.profile === '__custom__';
    if (custom && !S.problem.goal.trim() && !S.problem.title.trim()) { S.error = 'Describe the problem first.'; S.busy = false; draw(); return; }
    const res = await postJson('/api/run/start', { preset: S.preset, profile: custom ? '' : S.profile, mode: S.mode, confirm: S.mode === 'real' && S.confirming, problem: custom ? S.problem : undefined });
    if (res.ok && typeof api.toast === 'function') api.toast('Research started. The team is planning; the map appears in a minute or two.');
      .catch(() => ({ ok: false, body: { error: 'server offline' } }));
    S.busy = false;
    if (res.ok) {
      S.confirming = false; S.open = false; S.showLog = true;
      S.runs = [{ ...res.body, alive: true }, ...S.runs.filter((r) => r.batch !== res.body.batch)];
      await refresh();
      return;
    }
    const b = res.body || {};
    if (b.error === 'run_alive') S.error = `A run is still going (${b.batch}). Stop it first.`;
    else if (b.error === 'confirm_needed') { S.confirming = true; S.error = ''; }
    else S.error = `Not started: ${b.error || `http ${res.status}`}`;
    draw();
  }

  async function stop(run) {
    if (!run || !run.alive) return;
    if (typeof confirm === 'function' && !confirm(`Stop run ${run.batch}? The loop and its children end now.`)) return;
    const res = await postJson('/api/run/stop', { batch: run.batch }).catch(() => ({ ok: false, body: {} }));
    if (!res.ok) S.error = `Stop failed: ${(res.body && res.body.error) || 'server offline'}`;
    await refresh();
  }

  function toggle() {
    S.open = !S.open;
    S.confirming = false;
    S.error = '';
    if (S.open && !S.loaded) loadProfiles();
    draw();
  }

  // ---- views
  function Chip({ run }) {
    const c = chipOf(run);
    if (!c) return null;
    return html`<span class=${c.cls} title=${`${run.batch} . ${run.profile || ''}${run.run_dir ? ` . ${run.run_dir}` : ''}`}>
      <span class="run-chip__dot" aria-hidden="true"></span>
      <button class="run-chip__text" onClick=${() => { S.showLog = !S.showLog; draw(); }}>${c.text}</button>
      ${run.alive && canStart ? html`<button class="btn btn--small" onClick=${() => stop(run)}>Stop</button>` : null}
    </span>`;
  }

  async function loadReport(run) {
    try { S.report = await getJson(`/api/run/report?batch=${encodeURIComponent(run.batch)}`); S.showReport = true; }
    catch (e) { S.error = `No report yet: ${e.message}`; }
    draw();
  }

  function Status({ run }) {
    if (!run) return null;
    const c = chipOf(run);
    const failed = c && c.state === 'failed';
    const done = c && c.state === 'finished';
    const best = done && typeof api.view === 'function' ? (api.view().results || []).filter((r) => r.status === 'win' || r.status === 'preferred').slice(-1)[0] : null;
    return html`${done ? html`<div class="start-done" role="status">
        <strong>Done.</strong> ${best ? `Best result: ${best.name || best.cand}${best.reason ? `. ${best.reason}` : ''}` : 'No candidate beat the reference this time.'}
        ${run.report ? html`<button class="btn btn--small" onClick=${() => loadReport(run)}>Read the report</button>` : null}
      </div>` : null}
      ${failed ? html`<div class="start-error start-error--run" role="alert">
        <strong>The run stopped.</strong> ${run.error || 'No reason was logged.'}
        <button class="btn btn--small" onClick=${() => { S.showLog = !S.showLog; draw(); }}>${S.showLog ? 'Hide log' : 'Show log'}</button>
      </div>` : null}
      ${c && c.state === 'running' && c.note ? html`<div class="muted start-note">${c.note}</div>` : null}
      ${run.report ? html`<div class="start-report"><button class="btn btn--small" onClick=${() => (S.showReport ? (S.showReport = false, draw()) : loadReport(run))}>${S.showReport ? 'Hide report' : 'Read the report'}</button>
        ${S.showReport && S.report ? html`<a class="btn btn--small" download=${`${run.batch}-REPORT.md`} href=${`data:text/markdown;charset=utf-8,${encodeURIComponent(S.report.text)}`}>Download</a>` : null}</div>` : null}
      ${S.showReport && S.report ? html`<pre class="start-log__text start-report__text">${S.report.text}</pre>` : null}`;
  }

  function Log({ run }) {
    if (!run || !S.showLog) return null;
    const lines = run.tail || [];
    return html`<div class="start-log" role="log">
      <div class="start-log__head"><span class="mono">${run.batch}</span>
        <button class="btn btn--small" onClick=${() => { S.showLog = false; draw(); }}>Hide</button></div>
      ${run.run_dir ? html`<div class="muted start-log__dir mono">${run.run_dir}</div>` : null}
      <pre class="start-log__text">${lines.length ? lines.join('\n') : 'No output yet.'}</pre>
    </div>`;
  }

  function Panel() {
    const prof = S.profiles.find((p) => p.name === S.profile);
    const pr = S.presets[S.preset];
    const words = pr && (pr.words || '');
    return html`<div class="start-panel" role="dialog" aria-label="Start a research">
      <div class="start-panel__title">Start a research</div>
      ${!S.loaded && !S.error ? html`<div class="muted">Loading...</div>` : null}
      ${S.loaded ? html`
        <label class="start-field"><span class="start-field__name">Problem</span>
          <select value=${S.profile} onChange=${(e) => { S.profile = e.target.value; S.confirming = false; draw(); if (S.profile === '__custom__' && !S.problem.goal) describe(); }}>
            <option value="__custom__">Describe your own problem...</option>
            ${S.profiles.filter((p) => !p.custom).map((p) => html`<option value=${p.name}>${p.name}</option>`)}
            ${S.profiles.some((p) => p.custom) ? html`<optgroup label="Problems you described before">${S.profiles.filter((p) => p.custom).map((p) => html`<option value=${p.name}>${p.goal_short ? p.goal_short.slice(0, 70) : p.name}</option>`)}</optgroup>` : null}
          </select></label>
        ${S.profile === '__custom__' ? html`<div class="start-problem">
          ${S.problem.goal ? html`<div class="start-problem__sum"><strong>${S.problem.title || 'Your problem'}</strong><div class="muted start-problem__goal">${S.problem.goal.slice(0, 220)}${S.problem.goal.length > 220 ? '...' : ''}</div>
              <div class="muted">${(S.problem.criteria || []).length} criteria . ${(S.problem.facts || []).length + (S.problem.files || []).length} known . ${(S.problem.limits || []).length} limits</div>
              <button class="btn btn--small" onClick=${describe}>Edit</button></div>`
            : html`<div class="start-problem__sum"><div class="muted">Six short steps: the goal, what good looks like, what is known, the limits, the shape, a review.</div>
              <button class="btn btn--primary" onClick=${describe}>Describe the problem</button></div>`}
          <div class="muted start-hint">No scorer exists for a described problem, so a blind panel of judges ranks the proposals on your criteria. People's opinions count at a bounded weight.</div>
        </div>` : null}
        ${prof && (prof.goal_short || prof.note) ? html`<div class="muted start-hint">${prof.goal_short}${prof.note ? html`<span class="start-warn"> Note: ${prof.note}.</span>` : null}</div>` : null}
        <fieldset class="start-sizes"><legend class="start-field__name">Size</legend>
          ${S.order.filter((k) => S.presets[k]).map((k) => html`<label class=${`start-size${S.preset === k ? ' start-size--on' : ''}`}>
            <input type="radio" name="start-size" value=${k} checked=${S.preset === k}
              onChange=${() => { S.preset = k; S.confirming = false; draw(); }} />
            <span class="start-size__name">${SIZE_TEXT[k] || k}${k === 'demo' ? html` <span class="tag tag--demo">for demos</span>` : null}</span>
            <span class="muted start-size__what">${k === 'demo' ? '1 round, 1 build, 4 idea agents, all on Haiku' : presetLine(S.presets[k])}</span>
            <span class="mono start-size__est">${k === 'demo' ? `${S.presets[k].estimate.calls} calls, about ${S.presets[k].estimate.minutes} min, cheap` : estimateLine(S.presets[k].estimate)}</span>
          </label>`)}
        </fieldset>
        <div class="start-modes" role="group" aria-label="Spend">
          <span class=${S.preset === 'demo' ? 'start-warn start-hint' : 'muted start-hint'}>${S.preset === 'demo' ? 'Demo only: the whole team on Haiku, fast and cheap, not research quality. Use Small or bigger for real results.' : 'Runs the real team: ideas on Fable, critics and builders on Opus, research on Sonnet. Spends tokens.'}</span>
        </div>
        ${S.confirming ? html`<div class="start-confirm" role="alert">
            <div>${words}</div>
            <div>Start this real run on ${S.profile === '__custom__' ? (S.problem.title || 'your problem') : S.profile}?</div>
            <div class="start-actions">
              <button class="btn btn--primary" disabled=${S.busy} onClick=${start}>Yes, start the real run</button>
              <button class="btn" onClick=${() => { S.confirming = false; draw(); }}>Back</button>
            </div></div>`
          : html`<div class="start-actions">
              <button class="btn btn--primary" disabled=${S.busy || alive() || !S.profile} onClick=${start}>
                ${S.busy ? 'Starting...' : S.confirming ? 'Confirm and start' : 'Start'}</button>
              <button class="btn" onClick=${toggle}>Close</button>
              ${alive() ? html`<span class="muted">A run is going; stop it first.</span>` : null}
            </div>`}` : null}
      ${S.error ? html`<div class="start-error" role="alert">${S.error}</div>` : null}
    </div>`;
  }

  function Root() {
    const run = latest();
    return html`<div class="start-bar">
        <${Chip} run=${run} />
        ${canStart ? html`<button class=${`btn btn--start${S.open ? ' btn--on' : ''}`} aria-expanded=${S.open} onClick=${toggle}>Start a research</button>` : null}
      </div>
      ${S.open && canStart ? html`<${Panel} />` : null}
      ${!S.open ? html`<${Status} run=${run} />` : null}
      ${!S.open ? html`<${Log} run=${run} />` : null}`;
  }

  function draw() {
    render(html`<${Root} />`, el);
    const run = latest();
    const c = chipOf(run);
    if (typeof document !== 'undefined') document.body.dataset.run = c && c.state === 'running' ? 'running' : (c ? c.state : '');
  }

  if (typeof api.subscribe === 'function') {
    api.subscribe(() => { if (!alive() && Date.now() - lastCheck > IDLE_CHECK_MS) refresh(); });
  }
  draw();
  refresh();
  return { refresh, state: S };
}
