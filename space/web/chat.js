// chat.js: the My agent tab (section 2). Chat to your own agent (chat_posted to <me>.agent), slash hints from the
// grammar of section 6.7, the agent's lines (the 2 s ack, peer lines, "waiting for the model", replies marked
// canned), intent cards with Apply, Edit and Cancel (they post intent_decided; a takeover is posted by this browser,
// because only a person may take over), the "what my agent was told" box, and the private-draft switch
// (data.shared false). Nothing here calls a model.
import { html, useState, useRef, useEffect } from './vendor/standalone.module.js';

// contract.SLASH with the grammar of section 6.7
export const SLASH_HINTS = [
  ['branch', '/branch <parent> "<name>": <frame> [--claim]', 'add a part under a parent'],
  ['vote', '/vote up|down <cluster key or name>', 'vote on an idea'],
  ['claim', '/claim <node>', 'mark a part as yours for a while'],
  ['release', '/release <node>', 'remove your claim'],
  ['dispute', '/dispute <node>: <fact> | <reason> [measured|script|web|belief]', 'mark a fact as disputed'],
  ['ask', '/ask <node>: <question>', 'put an open question to the team'],
  ['skip', '/skip <node>', 'no ideas or builds there until restored'],
  ['unskip', '/unskip <node>', 'restore a part'],
  ['veto', '/veto <question id>', 'acts at the next pick'],
  ['unveto', '/unveto <question id>', 'withdraw a veto'],
  ['choose', '/choose <question id>', 'acts at the next pick'],
  ['note', '/note <text>', 'a note every agent reads'],
  ['reply', '/reply <cluster key> <objection n> concede|rebut|measure: <text> [tag]', 'answer an objection'],
  ['seed', '/seed <node>: <text>', 'a mechanism for the idea agents'],
  ['pause', '/pause', 'hold the run'],
  ['resume', '/resume', 'release your pause'],
  ['go', '/go', 'press Go for the boundary the loop waits at'],
];

export function slashMatches(text) {
  if (!text || text[0] !== '/') return [];
  const word = text.slice(1).split(/\s/)[0].toLowerCase();
  if (/\s/.test(text) && SLASH_HINTS.some(([k]) => k === word)) return SLASH_HINTS.filter(([k]) => k === word);
  return SLASH_HINTS.filter(([k]) => k.startsWith(word));
}

const KIND_TAG = { ack: 'ack', reply: '', ask: 'asks', waiting: 'waiting for the model', canned: 'canned', late: 'late',
  peer: 'peer', digest: 'told', error: 'error' };

function IntentCard({ line, view, api }) {
  const it = view.intents.get(line.intentId) || {};
  const [editing, setEditing] = useState(false);
  const [text, setText] = useState(JSON.stringify(line.action || {}, null, 1));
  const [err, setErr] = useState('');
  const card = line.card || {};
  const decide = async (decision, action) => {
    await api.post('intent_decided', { intent_id: line.intentId, decision, action }, { cause: line.seq });
    if (decision !== 'cancel' && action && action.type === 'claim_branch' && action.takeover && api.claim) {
      await api.claim('takeover', `node:${action.branch}`, { purpose: action.why || 'taken over by a person', cause: line.seq });
    }
  };
  const save = () => {
    try { const a = JSON.parse(text); setErr(''); setEditing(false); decide('edit', a); } catch (e) { setErr('not valid JSON'); }
  };
  return html`<div class=${`intent${it.decision ? ` intent--${it.decision}` : ''}`}>
    <div><span class="intent__k">will:</span> ${card.will || line.text}</div>
    ${card.on ? html`<div><span class="intent__k">on:</span> ${card.on}</div>` : null}
    ${card.because ? html`<div><span class="intent__k">because:</span> ${card.because}</div>` : null}
    ${card.apply_at ? html`<div><span class="intent__k">applies:</span> ${card.apply_at}</div>` : null}
    ${it.decision ? html`<div class="state-chip state-chip--applied"><i class="icon icon--check" aria-hidden="true"></i>${it.decision}</div>`
      : editing ? html`<div><textarea class="mono" rows="6" value=${text} onInput=${(e) => setText(e.target.value)}></textarea>
          ${err ? html`<div class="error">${err}</div>` : null}
          <button class="btn btn--small" onClick=${save}>Save and apply</button> <button class="btn btn--small" onClick=${() => setEditing(false)}>Back</button></div>`
      : html`<div class="intent__actions">
          <button class="btn btn--small btn--primary" onClick=${() => decide('apply', line.action)}>Apply</button>
          <button class="btn btn--small" onClick=${() => setEditing(true)}>Edit</button>
          <button class="btn btn--small" onClick=${() => decide('cancel', line.action)}>Cancel</button></div>`}
  </div>`;
}

export function ChatTab({ view, api }) {
  const me = api.me;
  const [text, setText] = useState('');
  const [priv, setPriv] = useState(false);
  const box = useRef(null);
  const lines = (me && view.chat.get(me)) || [];
  useEffect(() => { if (box.current) box.current.scrollTop = box.current.scrollHeight; }, [lines.length]);
  if (!me) return html`<div class="tab-body muted">Join with your name to talk to your agent.</div>`;
  const told = view.digests.filter((d) => d.agent === `${me}.agent`).at(-1);
  const hints = slashMatches(text);
  const send = async (e) => {
    e.preventDefault();
    const t = text.trim();
    if (!t) return;
    setText('');
    await api.post('chat_posted', { to: `${me}.agent`, text: t.slice(0, 1500), shared: !priv }, { subject: `person:${me}` });
  };
  return html`<div class="tab-body chat">
    <div class="told card">
      <div class="card__head">What my agent was told</div>
      ${told ? html`<pre class="told__text">${told.text || `${told.n} changes`}</pre>
        <div class="muted mono">e${told.fromSeq} to e${told.toSeq}, at ${told.stage} r${told.round} [e${told.seq}]</div>`
        : html`<div class="muted">Nothing yet. Your agent reads what teammates changed at each stage.</div>`}
    </div>
    <ul class="chat__lines" ref=${box}>${lines.map((l) => html`<li key=${l.seq != null ? l.seq : l.text}
        class=${`chat__line chat__line--${l.from === me ? 'me' : 'agent'} kind--${l.kind}`}>
      ${l.from === me ? html`<span class="chat__who">You${l.shared === false ? html` <span class="tag">private</span>` : null}</span>`
        : html`<span class="chat__who"><span class="spark" aria-hidden="true"></span>Your agent${KIND_TAG[l.kind] ? html` <span class="tag">${KIND_TAG[l.kind]}</span>` : null}${l.canned ? html` <span class="tag">(canned)</span>` : null}</span>`}
      ${l.kind === 'intent' ? html`<${IntentCard} line=${l} view=${view} api=${api} />` : html`<span class="chat__text">${l.text}</span>`}
    </li>`)}</ul>
    ${hints.length ? html`<ul class="hints">${hints.map(([k, g, what]) => html`<li class="mono" onClick=${() => setText(`/${k} `)}>${g} <span class="muted">${what}</span></li>`)}</ul>` : null}
    <form class="chat__form" onSubmit=${send}>
      <input class="chat__input" placeholder="Message your agent, or / for commands" value=${text} maxlength="1500"
        onInput=${(e) => setText(e.target.value)} />
      <button class="btn btn--primary" type="submit">Send</button>
    </form>
    <label class="switch"><input type="checkbox" checked=${priv} onChange=${(e) => setPriv(e.target.checked)} /> Private draft (not shared with the team)</label>
  </div>`;
}
