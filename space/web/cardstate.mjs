// space/web/cardstate.mjs: the tree card states, a pure function (docs/MULTIPLAYER_DESIGN.md section 6.6).
// cardState(node, run, me, ctx) -> {classes: [], chips: [{text, icon}], ring: {...} | null, hue, dot}
// Every input is passed in; nothing is read from the DOM or the clock. ctx is optional:
//   ctx.nowMs       server time in ms, for the claim countdown
//   ctx.people      Map(name -> {hue}) (state.people), for the owner and holder hues
//   ctx.focus       [{name, hue}] people whose presence focus is this node (state 12)
//   ctx.lastSeenSeq the viewer's last-seen seq (state 13)
//   ctx.stages      the contract's STAGES, when the caller has contract.json loaded

export const STAGES = ['planned', 'ideated', 'clustered', 'deepened', 'built', 'verified'];

// The boundary a queued item waits for. The loop folds pulled control at the Go of the boundary it waits at
// (run.waiting), else at the stage after run.stage; `planned` before the loop starts; `ideated` of the next
// round after `verified`.
export function nextBoundary(run, stages = STAGES) {
  const round = run && Number.isFinite(run.round) && run.round > 0 ? run.round : 1;
  if (!run || !run.stage) return { stage: 'planned', round };
  const i = stages.indexOf(run.stage);
  if (i < 0) return { stage: 'planned', round };
  if (run.waiting) return { stage: run.stage, round };
  if (i === stages.length - 1) return { stage: stages[1], round: round + 1 };
  return { stage: stages[i + 1], round };
}

export function hueOf(owner, people) {
  if (!owner || owner === 'team' || owner === 'server' || String(owner).startsWith('team.')) return 'team';
  const base = String(owner).replace(/\.agent$/, '');
  const p = people instanceof Map ? people.get(base) : people ? people[base] : undefined;
  return p && p.hue ? p.hue : 'team';
}

export function initialOf(name) {
  const s = String(name || '').replace(/\.agent$/, '').trim();
  return s ? s[0].toUpperCase() : '?';
}

function fmtTest(node) {
  const t = node.test;
  const metric = t && typeof t === 'object' ? t.metric : typeof t === 'string' ? t : '';
  const op = t && typeof t === 'object' && t.op ? t.op : '<=';
  const thr = node.threshold;
  return `test: ${metric} ${op} ${thr}`;
}

export function cardState(node, run, me, ctx = {}) {
  const classes = [];
  const chips = [];
  let ring = null;
  const origin = node.origin || 'map';
  const status = node.status || null;
  const hue = hueOf(node.owner || node.by, ctx.people);

  if (node.kind === 'question' && origin === 'failure') {                       // 6 failure question
    classes.push('card--question');
    chips.push({ text: `fails if ${node.failsIf != null ? node.failsIf : node.fails_if || ''}`, icon: 'flask' });
    chips.push({ text: fmtTest(node), icon: 'flask' });
  } else if (node.kind === 'win' && origin === 'offtree') {                      // 7 off-map win
    classes.push('card--win');
    chips.push({ text: 'won off the map', icon: 'trophy' });
  } else if (origin === 'human') {
    classes.push('card--human');
    if (status === 'pending') {                                                 // 2
      classes.push('card--pending');
      chips.push({ text: 'sending', icon: 'clock' });
    } else if (status === 'queued') {                                           // 3
      classes.push('card--queued');
      const b = nextBoundary(run, ctx.stages || STAGES);
      chips.push({ text: `waits for ${b.stage}, round ${b.round}`, icon: 'clock' });
    } else if (status === 'applied') {                                          // 4
      classes.push('card--applied');
      const a = node.appliedAt || {};
      chips.push({ text: `applied in round ${a.round}, stage ${a.stage}`, icon: 'check' });
    } else if (status === 'rejected') {                                         // 5
      classes.push('card--dropped');
      const reason = node.reason || (node.error && node.error.reason) || node.error || '';
      chips.push({ text: reason === 'id_taken' ? 'dropped: id in use' : `rejected: ${reason}`, icon: 'x' });
    }
  } else {                                                                      // 1 planned part
    classes.push('card--map');
  }

  if (Array.isArray(node.disputed) && node.disputed.length) {                   // 8
    classes.push('card--disputed');
    for (const d of node.disputed) chips.push({ text: `disputed by ${d.by}: ${d.reason} (${d.tag})`, icon: 'flag' });
  }
  if (node.skippedBy) {                                                         // 9
    classes.push('card--skipped');
    chips.push({ text: `skipped by ${initialOf(node.skippedBy)}`, icon: 'pause' });
  }
  if (node.lowered) {                                                           // 10
    classes.push('card--lowered');
    chips.push({ text: 'lowered', icon: 'arrow-down' });
  }
  if (node.claim && node.claim.holder) {                                        // 11
    const nowMs = Number.isFinite(ctx.nowMs) ? ctx.nowMs : 0;
    const until = Number.isFinite(node.claim.untilMs) ? node.claim.untilMs : nowMs;
    const secondsLeft = Math.max(0, Math.ceil((until - nowMs) / 1000));
    ring = { kind: 'claim', hue: hueOf(node.claim.owner || node.claim.holder, ctx.people),
             holder: node.claim.holder, tag: `${node.claim.holder} ${secondsLeft} s`, icon: 'lock', focus: [] };
    classes.push('card--claimed');
  }
  if (Array.isArray(ctx.focus) && ctx.focus.length) {                           // 12
    const focus = ctx.focus.map((f) => ({ name: f.name, hue: f.hue || hueOf(f.name, ctx.people) }));
    if (!ring) ring = { kind: 'focus', hue: focus[0].hue, tag: null, icon: null, focus };
    else ring.focus = focus;
    classes.push('card--focused');
  }
  let dot = false;
  if (Number.isFinite(ctx.lastSeenSeq) && Number.isFinite(node.seq) && node.seq > ctx.lastSeenSeq) {   // 13
    classes.push('card--unseen');
    dot = true;
  }
  if (me && (node.owner === me || node.by === me)) classes.push('card--mine');
  return { classes, chips, ring, hue, dot };
}

export const ICONS = ['clock', 'check', 'x', 'flask', 'trophy', 'flag', 'pause', 'arrow-down', 'lock', 'dot'];
