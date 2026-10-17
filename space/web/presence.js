// presence.js: people and agent chips in the top bar (section 2): a person is a filled chip in their hue, their
// agent is a ring with a spark in the same hue, with a state ring (thinking, waiting, executing, finished),
// "last heard 12 s ago" and "seen up to #N". Presence is memory only (no seq): it comes from the SSE presence
// message (clients, claims) and is merged into the view by app.js as state.presence.
import { html } from './vendor/standalone.module.js';

export const AGENT_STATES = ['thinking', 'waiting', 'executing', 'finished'];
const cap = (s) => (s ? String(s)[0].toUpperCase() + String(s).slice(1) : '');

export function hueOf(view, owner) {
  const p = view && view.people && view.people.get(owner);
  return p ? p.hue : 'team';
}

// One row per person: {name, hue, online, client, agent: {client, state, text, heardS, cursor} | null}
export function presenceRows(view, nowMs) {
  const clients = (view.presence && view.presence.clients) || [];
  const names = new Set([...(view.people ? view.people.keys() : [])]);
  for (const c of clients) {
    const owner = c.owner || String(c.name || '').toLowerCase();
    if (owner && !String(owner).startsWith('team') && owner !== 'server') names.add(owner);
  }
  const heard = (c) => {
    if (c == null) return null;
    if (typeof c.seen_ms_ago === 'number') return Math.round(c.seen_ms_ago / 1000);
    if (typeof c.last_ms === 'number' && nowMs) return Math.max(0, Math.round((nowMs - c.last_ms) / 1000));
    return null;
  };
  const isAgent = (c) => c.kind === 'agent' || String(c.client || '').endsWith('.agent') || String(c.name || '').toLowerCase().endsWith('.agent');
  const rows = [];
  for (const name of names) {
    const mine = clients.filter((c) => (c.owner || String(c.name || '').toLowerCase()) === name);
    const person = mine.find((c) => !isAgent(c)) || null;
    const agent = mine.find(isAgent) || null;
    rows.push({
      name, hue: hueOf(view, name), online: !!person, client: person, focus: person && person.focus,
      heardS: heard(person), cursor: person ? person.cursor : null,
      agent: agent ? { client: agent, state: (agent.activity && agent.activity.state) || 'waiting', text: (agent.activity && agent.activity.text) || '',
        heardS: heard(agent), cursor: agent.cursor ?? null, focus: agent.focus } : null,
    });
  }
  return rows;
}

export function PresenceChips({ view, nowMs, following, onFollow }) {
  const rows = presenceRows(view, nowMs);
  if (!rows.length) return html`<span class="muted">nobody has joined yet</span>`;
  return html`<span class="chips">${rows.map((r) => html`
    <button class=${`chip chip--person hue-${r.hue}${r.online ? '' : ' chip--away'}${following === r.name ? ' chip--followed' : ''}`}
      title=${`${cap(r.name)}${r.online ? '' : ' (away)'}${r.heardS != null ? `, last heard ${r.heardS} s ago` : ''}${r.cursor != null ? `, seen up to #${r.cursor}` : ''}. Click to follow.`}
      onClick=${() => onFollow && onFollow(r.name)}>${cap(r.name)}</button>
    ${r.agent ? html`
    <button class=${`chip chip--agent hue-${r.hue} state--${AGENT_STATES.includes(r.agent.state) ? r.agent.state : 'waiting'}`}
      title=${`${cap(r.name)}'s agent: ${r.agent.state}${r.agent.text ? ` (${r.agent.text})` : ''}`}
      onClick=${() => onFollow && onFollow(`${r.name}.agent`)}>
      <span class="spark" aria-hidden="true"></span>${cap(r.name)}'s agent
      <span class="chip__meta">${r.agent.state}${r.agent.heardS != null ? ` . last heard ${r.agent.heardS} s ago` : ''}${r.agent.cursor != null ? ` . seen up to #${r.agent.cursor}` : ''}</span>
    </button>` : null}`)}</span>`;
}

// The focus of the person (or agent) being followed, for the follow mode camera.
export function focusOf(view, who) {
  const clients = (view.presence && view.presence.clients) || [];
  const agent = String(who || '').endsWith('.agent');
  const owner = agent ? who.slice(0, -6) : who;
  const c = clients.find((x) => (x.owner || String(x.name || '').toLowerCase()) === owner &&
    (agent === (x.kind === 'agent' || String(x.client || '').endsWith('.agent'))));
  return c ? c.focus || null : null;
}
