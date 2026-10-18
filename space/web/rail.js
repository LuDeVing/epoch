// rail.js: the right rail (section 2): tabs Feed, Arguments, Results, Memory, My agent.
// Feed: the next-question card (preview, veto, choose, the overwrote chip with Undo), then typed lines (who, via,
// what, where, cause link, receipt) newest first, bursts grouped, an "N new" pill while scrolled.
// Arguments: one chain per idea. Results: one row per candidate. Chip texts come from reduce.chipText (section 4.7).
import { html, render, useState, useEffect, useRef } from './vendor/standalone.module.js';
import autoAnimate from './vendor/auto-animate.mjs';
import { chipText, groupFeed, whoText, WINNER_WORD } from './reduce.mjs';
import { hueOf } from './presence.js';
import { MemoryTab } from './memory.js';
import { ChatTab } from './chat.js';
import { plainStatus, STATUS_WORDS } from './words.mjs';
import { FindingsTab } from './findings.js';

export const TABS = [['feed', 'Feed'], ['args', 'Arguments'], ['results', 'Results'], ['findings', 'Findings'], ['memory', 'Knowledge'], ['agent', 'Agent']];
const FEED_CAP = 200;
const cap = (s) => (s ? String(s)[0].toUpperCase() + String(s).slice(1) : '');
const STATUS_ICON = { pending: 'clock', queued: 'clock', applied: 'check', rejected: 'x', not_in_top3: 'x', overwritten: 'x', withdrawn: 'x' };
const RESULT_WORD = STATUS_WORDS;
const RESULT_ICON = { win: 'trophy', preferred: 'trophy', tie: 'equal', split: 'equal', loss: 'down', not_preferred: 'down',
  failed_check: 'x', not_built: 'x', built: 'clock' };

export function useView(api) {
  const [view, setView] = useState(api.view());
  useEffect(() => api.subscribe((v) => setView(v)), []);
  return view;
}

function useAutoAnimate() {
  const ref = useRef(null);
  useEffect(() => { if (ref.current) { try { autoAnimate(ref.current); } catch (e) { /* motion is optional */ } } }, []);
  return ref;
}

export function Chip({ item, run }) {
  const text = chipText(item, run);
  if (!text) return null;
  return html`<span class=${`state-chip state-chip--${item.status}`}><i class=${`icon icon--${STATUS_ICON[item.status] || 'dot'}`} aria-hidden="true"></i>${text}</span>`;
}

function receiptText(r) {
  if (!r) return '';
  const who = r.agent === 'team.loop' ? 'the team' : r.agent.endsWith('.agent') ? `${cap(r.agent.slice(0, -6))}'s agent` : r.agent;
  return `reached ${who} in round ${r.round}`;
}

function QuestionCard({ view, api }) {
  const qs = view.questions;
  const pv = qs.preview;
  const me = api.me;
  const canAct = me && !api.flags.stage;
  const vetoOf = (id) => (qs.vetoes.get(id) || [])[0] || null;
  const chosen = qs.chosen;
  const lost = chosen && me && chosen.by !== me && chosen.prev && chosen.prev.by === me && chosen.status !== 'applied';
  return html`<div class="card qcard">
    <div class="card__head">What the team asks next${pv ? ` (round ${pv.roundNext})` : ''}</div>
    ${!pv ? html`<div class="muted">After the first round is tested, the team proposes its next three questions here. You can veto one or pick one; the team takes your choice at the start of the next round.</div>` : html`
    <div class="muted qhelp">Veto removes a question from the pick; Choose makes it the next one. Either takes effect when the next round starts.</div>
    <ol class="qlist">${pv.top3.map((t) => {
      const v = vetoOf(t.id);
      const isChosen = chosen && chosen.id === t.id;
      return html`<li class=${`q${v ? ' q--vetoed' : ''}${isChosen ? ' q--chosen' : ''}`}>
        <span class="q__text">${t.text}</span>
        ${t.requires_human ? html`<span class="tag" title="the team cannot answer this one alone; it needs a person's measurement or decision">needs a person</span>` : null}
        ${v ? html`<span class=${`tok hue-${hueOf(view, v.by)}`}>vetoed by ${cap(v.by)}</span><${Chip} item=${v} run=${view.run} />` : null}
        ${isChosen ? html`<span class=${`tok hue-${hueOf(view, chosen.by)}`}>chosen by ${cap(chosen.by)}</span><${Chip} item=${chosen} run=${view.run} />` : null}
        ${canAct ? html`<span class="q__actions">
          ${v ? html`<button class="btn btn--small" onClick=${() => api.post('question_unvetoed', { question: t.id, text: t.text }, { subject: `question:${t.id}` })}>Unveto</button>`
            : html`<button class="btn btn--small" onClick=${() => api.post('question_vetoed', { question: t.id, text: t.text }, { subject: `question:${t.id}` })}>Veto</button>`}
          <button class="btn btn--small" onClick=${() => api.post('question_chosen', { question: t.id, text: t.text }, { subject: `question:${t.id}` })}>Choose</button>
        </span>` : null}
      </li>`; })}</ol>`}
    ${chosen && pv && !pv.top3.some((t) => t.id === chosen.id) ? html`<div class="q">
      <span class=${`tok hue-${hueOf(view, chosen.by)}`}>chosen by ${cap(chosen.by)}</span> ${chosen.text || chosen.id} <${Chip} item=${chosen} run=${view.run} /></div>` : null}
    ${lost ? html`<div class="state-chip state-chip--overwritten"><i class="icon icon--x" aria-hidden="true"></i>
      ${cap(chosen.by)}'s choice replaced yours.
      <button class="btn btn--small" onClick=${() => api.post('question_chosen', { question: chosen.prev.id, text: chosen.prev.text }, { subject: `question:${chosen.prev.id}` })}>Undo</button></div>` : null}
    ${qs.picked ? html`<div class="muted">Picked in round ${qs.picked.round}: ${(qs.picked.top3.find((t) => t.id === qs.picked.chosen) || {}).text || qs.picked.chosen || 'none'} (${qs.picked.by})</div>` : null}
  </div>`;
}

function FeedLine({ it, view, onCause }) {
  const hue = it.cls === 'person' || it.cls === 'delegate' ? hueOf(view, it.owner) : 'team';
  return html`<li class=${`feed__line hue-${hue}${it.cls === 'delegate' ? ' feed__line--agent' : ''}${it.flash ? ' feed__line--flash' : ''}`} data-seq=${it.seq}>
    <span class="feed__who">${whoText(it)}</span>
    <span class="feed__text">${it.text}${it.count > 1 ? html` <span class="tag">x${it.count}</span>` : null}</span>
    ${it.status ? html`<${Chip} item=${it} run=${view.run} />` : null}
    <span class="feed__meta">${it.cause != null ? html`<a href="#" class="cause" title="jump to what this answers" onClick=${(e) => { e.preventDefault(); onCause(it.cause); }}>why</a>` : null}</span>
    ${it.receipt ? html`<span class="receipt">${receiptText(it.receipt)}</span>` : null}
  </li>`;
}

function FeedTab({ view, api }) {
  const box = useRef(null);
  const list = useAutoAnimate();
  const [seenHead, setSeenHead] = useState(view.head);
  const [flash, setFlash] = useState(null);
  const scrolled = () => box.current && box.current.scrollTop > 8;
  useEffect(() => { if (!scrolled() || api.following()) setSeenHead(view.head); }, [view.head]);
  const lines = groupFeed(view.feed.slice(-FEED_CAP * 2)).slice(-FEED_CAP).reverse();
  const fresh = view.feed.filter((l) => l.seq != null && l.seq > seenHead).length;
  const toTop = () => { if (box.current) box.current.scrollTop = 0; setSeenHead(view.head); };
  const onCause = (seq) => {
    setFlash(seq);
    const el = box.current && box.current.querySelector(`[data-seq="${seq}"]`);
    if (el && el.scrollIntoView) el.scrollIntoView({ block: 'center' });
    setTimeout(() => setFlash(null), 2000);
  };
  return html`<div class="tab-body" ref=${box} onScroll=${() => { if (!scrolled()) setSeenHead(view.head); }}>
    ${fresh > 0 && scrolled() ? html`<button class="pill" onClick=${toTop}>${fresh} new</button>` : null}
    <${QuestionCard} view=${view} api=${api} />
    <ul class="feed" ref=${list}>${lines.map((it) => html`<${FeedLine} key=${it.seq != null ? it.seq : `p-${it.op}`}
      it=${flash === it.seq ? { ...it, flash: true } : it} view=${view} onCause=${onCause} />`)}</ul>
  </div>`;
}

function ArgsTab({ view }) {
  const list = useAutoAnimate();
  const chains = [...view.chains.entries()];
  const nameOf = (key) => (view.clusters.get(key) || (view.retired && view.retired.get(key)) || { name: key }).name;
  return html`<div class="tab-body">
    <div class="caption">The critics attack each idea; its author answers once with a fact, a change or a test. An answer never blocks a build: the tests decide.</div>
    ${!chains.length ? html`<div class="muted">No arguments yet. They start once the ideas are grouped.</div>` : null}
    <ul class="chains" ref=${list}>${chains.map(([key, entries]) => html`<li key=${key} class="chain">
      <div class="chain__idea">${nameOf(key)}</div>
      ${entries.map((e) => html`<div class="exchange">
        ${e.objection ? html`<div class="objection">
          <span class=${`tag sev--${e.objection.severity || 'person'}`}>${e.objection.cls}${e.objection.severity ? ` . ${e.objection.severity}` : ''}</span>
          ${e.objection.text}</div>` : null}
        ${[e.reply, ...(e.more || [])].filter(Boolean).map((r) => {
          const person = r.cls === 'person' || r.cls === 'delegate';
          return html`<div class=${`reply${person ? ` reply--person hue-${hueOf(view, r.owner)}` : ''}`}>
            ${person ? html`<span class="badge">${whoText({ cls: r.cls, owner: r.owner })}</span>` : html`<span class="badge badge--team">author</span>`}
            <span class="tag">${r.kind}</span> ${r.text}${r.fact ? html` <span class="muted">(fact: ${r.fact}${r.source ? `, ${r.source}` : ''})</span>` : null}
          </div>`; })}
        ${e.mark ? html`<div class=${`mark mark--${e.mark.verdict}`}><i class=${`icon icon--${e.mark.verdict === 'resolved' ? 'check' : e.mark.verdict === 'revised' ? 'edit' : 'flag'}`} aria-hidden="true"></i>${e.mark.verdict}${e.mark.reason ? `: ${e.mark.reason}` : ''}</div>` : null}
      </div>`)}
    </li>`)}</ul>
  </div>`;
}

function Rungs({ rung }) {
  const n = typeof rung === 'number' ? rung : 0;
  return html`<span class="rungs" title=${`rung ${n} of 4`}>${[1, 2, 3, 4].map((i) => html`<i class=${i <= n ? 'rung rung--on' : 'rung'}></i>`)}</span>`;
}

const GOOD = new Set(['win', 'preferred']);
function bestOf(results) {
  const good = results.filter((r) => GOOD.has(r.status));
  if (!good.length) return null;
  const score = (r) => { const m = r.metrics || {}; const k = Object.keys(m).find((x) => typeof m[x] === 'number'); return k ? m[k] : null; };
  return good.slice().sort((a, b) => (b.seq || 0) - (a.seq || 0))[0] || null;
}
export function summaryMarkdown(view) {
  const L = [];
  L.push(`# ${view.spaceId || 'Epoch space'}: results`, '');
  L.push(`Round ${view.run.round || 0}, stage ${view.run.stage || 'not started'}. ${view.results.length} candidates built, ${view.findings.length} findings shared.`, '');
  const best = bestOf(view.results);
  if (best) { L.push('## Best so far', '', `${best.name || best.cand}: ${best.status}${best.reason ? `. ${best.reason}` : ''}`, ''); }
  L.push('## Results', '', '| candidate | part | status | metrics | reason |', '|---|---|---|---|---|');
  for (const r of view.results) {
    const part = view.nodes.get(r.node) ? view.nodes.get(r.node).name : (r.node || '');
    const m = Object.entries(r.metrics || {}).filter(([, v]) => typeof v === 'number').map(([k, v]) => `${k} ${Math.round(v * 1000) / 1000}`).join(', ');
    L.push(`| ${r.name || r.cand} | ${part} | ${r.status} | ${m} | ${(r.reason || '').replace(/\|/g, '/')} |`);
  }
  L.push('', '## The map', '');
  for (const n of view.nodes.values()) L.push(`- ${n.name}${n.frame ? `: ${n.frame}` : ''}`);
  if (view.findings.length) { L.push('', '## Findings from people', ''); for (const f of view.findings) L.push(`- ${f.by}: ${f.title}${f.text && f.text !== f.title ? ` . ${f.text}` : ''}${f.file ? ` (file ${f.file.name})` : ''}`); }
  return L.join('\n');
}

async function latestBatch(api) {
  try {
    const q = api.flags && api.flags.key ? `?key=${encodeURIComponent(api.flags.key)}` : '';
    const r = await fetch(`${api.base}/api/run/status${q}`, { credentials: 'same-origin', cache: 'no-store' });
    const j = await r.json();
    const runs = (j.runs || []);
    return runs.length ? runs[0].batch : null;
  } catch (e) { return null; }
}

function CandDetail({ api, cand }) {
  const [data, setData] = useState(null);
  const [err, setErr] = useState('');
  const [showArt, setShowArt] = useState(true);
  useEffect(() => {
    let live = true;
    (async () => {
      const batch = await latestBatch(api);
      if (!batch) { if (live) setErr('No run started from this page yet; use Browse run files on the run chip.'); return; }
      try {
        const q = api.flags && api.flags.key ? `&key=${encodeURIComponent(api.flags.key)}` : '';
        const r = await fetch(`${api.base}/api/run/cand?batch=${encodeURIComponent(batch)}&cand=${encodeURIComponent(cand)}${q}`, { credentials: 'same-origin', cache: 'no-store' });
        const j = await r.json();
        if (!r.ok) throw new Error(j.hint || j.error || r.status);
        if (live) setData(j);
      } catch (e) { if (live) setErr(`Could not load: ${e.message}`); }
    })();
    return () => { live = false; };
  }, [cand]);
  if (err) return html`<div class="muted cand__err">${err}</div>`;
  if (!data) return html`<div class="muted">loading...</div>`;
  const art = data.artifacts && data.artifacts[0];
  return html`<div class="cand">
    ${data.record && data.record.hypothesis ? html`<div class="cand__hyp"><strong>Claim:</strong> ${data.record.hypothesis}${data.record.change ? html`<div class="muted">Changes: ${data.record.change}</div>` : null}</div>` : null}
    ${art ? html`<div class="cand__head">What was built <span class="mono muted">${art.path}</span> <button class="btn btn--small" onClick=${() => setShowArt(!showArt)}>${showArt ? 'hide' : 'show'}</button></div>
      ${showArt ? html`<pre class="cand__text">${art.text}</pre>` : null}` : html`<div class="muted">No built file found for this candidate.</div>`}
    ${data.tests && data.tests.length ? html`<div class="cand__head">How it was tested</div>
      <ul class="cand__tests">${data.tests.map((t) => html`<li>
        <span class=${`tag ${t.status === 'pass' || t.status === 'win' ? 'tag--ok' : 'tag--warn'}`}>${t.status}${t.rung != null ? ` . level ${t.rung}` : ''}</span>
        ${t.reason ? html` <span>${t.reason}</span>` : null}
        ${Object.keys(t.metrics || {}).length ? html` <span class="mono muted">${Object.entries(t.metrics).filter(([, v]) => typeof v === 'number').map(([k, v]) => `${k} ${Math.round(v * 1000) / 1000}`).join(', ')}</span>` : null}
        ${t.stderr ? html`<pre class="cand__log">${t.stderr}</pre>` : null}
        ${t.stdout ? html`<pre class="cand__log">${t.stdout}</pre>` : null}
      </li>`)}</ul>` : html`<div class="muted">No test record yet.</div>`}
  </div>`;
}

function ResultsTab({ view, api }) {
  const list = useAutoAnimate();
  const [openCand, setOpenCand] = useState(null);
  const winner = (view.winnerWord && view.winnerWord[view.run.mode]) || WINNER_WORD[view.run.mode] || 'won';
  const rows = view.results.slice().reverse();
  const metrics = (m) => Object.entries(m || {}).filter(([, v]) => typeof v === 'number').slice(0, 3)
    .map(([k, v]) => `${k} ${Math.round(v * 100) / 100}`).join(', ');
  const best = bestOf(view.results);
  const exportMd = () => {
    const blob = new Blob([summaryMarkdown(view)], { type: 'text/markdown' });
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = `${view.spaceId || 'space'}-results.md`; a.click();
    setTimeout(() => URL.revokeObjectURL(a.href), 2000);
  };
  return html`<div class="tab-body">
    <div class="best card">
      <div class="card__head">Best so far <button class="btn btn--small" style="float:right" onClick=${exportMd} title="download a markdown summary of the map, the results and the findings">Export</button></div>
      ${best ? html`<div class="best__name">${best.name || best.cand}</div>
        <div class="muted">${plainStatus(best.status)} on ${view.nodes.get(best.node) ? view.nodes.get(best.node).name : best.node || 'the whole problem'}${metrics(best.metrics) ? ` . ${metrics(best.metrics)}` : ''}${best.rung != null ? ` . rung ${best.rung}` : ''}</div>
        ${best.reason ? html`<div class="best__why">${best.reason}</div>` : null}`
        : html`<div class="muted">${rows.length ? 'No candidate has beaten the reference yet.' : 'Nothing built yet. The first results land at built, round 1.'}</div>`}
    </div>
    ${!rows.length ? html`<div class="muted">No builds yet.</div>` : null}
    <ul class="results" ref=${list}>${rows.map((r) => {
      const grey = ['loss', 'not_preferred', 'failed_check', 'not_built'].includes(r.status);
      return html`<li key=${r.cand} class=${`result result--${r.status}${grey ? ' result--grey' : ''}`}>
        <span class=${`status status--${r.status}`}><i class=${`icon icon--${RESULT_ICON[r.status] || 'dot'}`} aria-hidden="true"></i>${RESULT_WORD[r.status] || r.status}</span>
        <span class="result__name">${r.name || r.key || r.cand}</span>
        <${Rungs} rung=${r.rung} />
        <span class="mono metrics" title="the test's numbers">${metrics(r.metrics) || r.reason || ''}</span>
        <button class="btn btn--small" onClick=${() => setOpenCand(openCand === r.cand ? null : r.cand)} title="what was built, and how the test went">${openCand === r.cand ? 'close' : 'open'}</button>
        ${openCand === r.cand ? html`<${CandDetail} api=${api} cand=${r.cand} />` : null}
        <span class="voters">${Object.entries(r.voters || {}).map(([who, hm]) => html`<span class=${`tok hue-${hueOf(view, who)} vote--${hm}`}>${cap(who)}: ${hm}</span>`)}</span>
      </li>`; })}</ul>
  </div>`;
}

function Rail({ api }) {
  const view = useView(api);
  const [tab, setTab] = useState(api.initialTab || 'feed');
  useEffect(() => api.bus.on('tab', (t) => setTab(t)), []);
  const tabs = api.flags.stage ? TABS.filter(([k]) => k !== 'agent') : TABS;
  return html`<nav class="tabs" role="tablist">${tabs.map(([k, label]) => html`<button role="tab" aria-selected=${tab === k}
      class=${`tab${tab === k ? ' tab--on' : ''}`} onClick=${() => { setTab(k); api.setView && api.setView(k); }}>${label}</button>`)}</nav>
    ${tab === 'feed' ? html`<${FeedTab} view=${view} api=${api} />` : null}
    ${tab === 'args' ? html`<${ArgsTab} view=${view} />` : null}
    ${tab === 'results' ? html`<${ResultsTab} view=${view} api=${api} />` : null}
    ${tab === 'findings' ? html`<${FindingsTab} view=${view} api=${api} />` : null}
    ${tab === 'memory' ? html`<${MemoryTab} view=${view} api=${api} />` : null}
    ${tab === 'agent' ? html`<${ChatTab} view=${view} api=${api} />` : null}`;
}

// api: {view(), subscribe(fn) -> unsubscribe, bus, post(kind, data, extra), claim(action, subject, extra), me, flags,
//       base, following(), setView(name)}
export function mountRail(el, api) {
  render(html`<${Rail} api=${api} />`, el);
}
