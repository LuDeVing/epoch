// wizard.js: "Describe your problem", step by step. Six short steps with an explanation, an example and a check
// on each, so a person gives the team enough to work with instead of one line. The result is the spec that
// space/launch.py turns into a profile (title, goal, success, known, fixed, parts, field), plus files shared as
// findings right away. mountWizard(api) returns open(initialSpec, onDone).
import { html, render, useState, useEffect, useRef } from './vendor/standalone.module.js';

const STEPS = ['Your material', 'The problem', 'What good looks like', 'What is known', 'Limits', 'Shape', 'Review'];
const CRITERIA_IDEAS = [
  ['Correctness', 'the answer follows from the facts and does not contradict them'],
  ['Cost', 'cheaper in money, time or effort than what is done today'],
  ['Speed', 'the result arrives sooner, or the process takes less time'],
  ['Safety', 'no harm, no data loss, nothing irreversible'],
  ['Simplicity', 'fewer parts, easier to explain and to run'],
  ['Robustness', 'still works when inputs are messy or conditions change'],
  ['Fairness', 'no group or case is treated worse without a reason'],
  ['Measurable', 'a number or a test says whether it worked'],
];
const MIN_GOAL = 120;

function words(s) { return String(s || '').trim().split(/\s+/).filter(Boolean).length; }

// ---- list editors ------------------------------------------------------------------------------------------------
// the parts as one line for the profile: "part > sub one | sub two, part two" (nano/profiles/_custom.py reads it back)
export function partsText(rows, deep = true) {
  return (rows || []).map((p) => {
    const name = String(p.name || '').trim().replace(/[,>|]/g, ' ');
    if (!name) return '';
    const subs = deep ? String(p.sub || '').split(',').map((s) => s.trim().replace(/[>|]/g, ' ')).filter(Boolean) : [];
    return subs.length ? `${name} > ${subs.join(' | ')}` : name;
  }).filter(Boolean).join(', ');
}

function Rows({ rows, setRows, fields, addLabel, empty }) {
  const add = () => setRows([...rows, Object.fromEntries(fields.map((f) => [f.key, '']))]);
  const set = (i, k, v) => setRows(rows.map((r, j) => (j === i ? { ...r, [k]: v } : r)));
  const del = (i) => setRows(rows.filter((_, j) => j !== i));
  return html`<div class="wz-rows">
    ${rows.length ? rows.map((r, i) => html`<div class="wz-row" key=${i}>
      ${fields.map((f) => (f.multi
        ? html`<textarea class="wz-input" rows="2" placeholder=${f.placeholder} value=${r[f.key]} onInput=${(e) => set(i, f.key, e.target.value)}></textarea>`
        : html`<input class="wz-input" placeholder=${f.placeholder} value=${r[f.key]} onInput=${(e) => set(i, f.key, e.target.value)} />`))}
      <button class="btn btn--small wz-row__del" type="button" title="remove" onClick=${() => del(i)}>x</button>
    </div>`) : html`<div class="muted wz-empty">${empty}</div>`}
    <button class="btn btn--small" type="button" onClick=${add}>+ ${addLabel}</button>
  </div>`;
}

// ---- the wizard --------------------------------------------------------------------------------------------------
function Wizard({ api, initial, onDone, onClose }) {
  const [step, setStep] = useState(0);
  const [title, setTitle] = useState(initial.title || '');
  const [goal, setGoal] = useState(initial.goal || '');
  const [context, setContext] = useState(initial.context || '');
  const [criteria, setCriteria] = useState(initial.criteria || []);
  const [facts, setFacts] = useState(initial.facts || []);
  const [limits, setLimits] = useState(initial.limits || []);
  const [parts, setParts] = useState(initial.partsList || []);
  const [deep, setDeep] = useState(!!initial.deep);            // two-level map: off by default, so research keeps its one-level map
  const [field, setField] = useState(initial.field || '');
  const [scope, setScope] = useState(initial.scope || '');
  const [files, setFiles] = useState([]);
  const [material, setMaterial] = useState(initial.material || []);
  const [notes, setNotes] = useState(initial.notes || '');
  const [drafting, setDrafting] = useState(false);
  const [draftNote, setDraftNote] = useState(initial.draftNote || '');
  const [openQs, setOpenQs] = useState(initial.open_questions || []);
  const folderInput = useRef(null);
  const [busy, setBusy] = useState(0);
  const [err, setErr] = useState('');
  const fileInput = useRef(null);
  const base = api.base || '';
  useEffect(() => { const h = (e) => { if (e.key === 'Escape') onClose(); }; document.addEventListener('keydown', h); return () => document.removeEventListener('keydown', h); }, []);

  const goalOk = goal.trim().length >= MIN_GOAL;
  const titleOk = title.trim().length >= 3;
  const checks = [
    true,
    titleOk && goalOk,
    true, true, true, true, true,
  ];
  const nudges = [
    material.length || notes.trim() ? '' : 'Pick the folder with your research, or drop the files that matter. Claude reads them and drafts the whole problem; you only correct it. Or skip ahead and write it yourself.',
    !titleOk ? 'Give it a title.' : !goalOk ? `Say more about the goal: ${Math.max(0, MIN_GOAL - goal.trim().length)} more characters. A few sentences give the team far more to work with than one line.` : '',
    criteria.length ? '' : 'Without criteria the judges fall back to correctness, usefulness, feasibility and clarity. One or two of your own are better.',
    facts.length || files.length || material.length ? '' : 'Nothing known yet: the team will start from the goal alone. Even two facts or one file help a lot.',
    '', '', '',
  ];

  const uploadMaterial = async (list) => {
    const arr = Array.from(list || []).filter((f) => f.size > 0 && f.size <= 8 * 1024 * 1024).slice(0, 40);
    if (!arr.length) { setErr('No files of a usable size (up to 8 MB each, 40 files at most).'); return; }
    if (!api.me) { setErr('Sign in to share files.'); return; }
    setBusy((b) => b + 1); setErr('');
    const got = [];
    for (const file of arr) {
      try {
        const h = { 'X-Space-Actor': api.me, 'X-Space-Kind': 'human', 'Content-Type': file.type || 'application/octet-stream', 'X-Space-Filename': encodeURIComponent(file.webkitRelativePath || file.name) };
        if (api.flags && api.flags.key) h['X-Space-Key'] = api.flags.key;
        const r = await fetch(`${base}/api/upload`, { method: 'POST', credentials: 'same-origin', headers: h, body: file });
        const j = await r.json().catch(() => ({}));
        if (r.ok) got.push(j); else if (r.status !== 415) setErr(`${file.name}: ${j.hint || j.error || r.status}`);
      } catch (ex) { setErr(`${file.name}: ${ex.message}`); }
    }
    setMaterial((m) => [...m, ...got]);
    setBusy((b) => b - 1);
  };

  const draft = async () => {
    setDrafting(true); setErr('');
    try {
      const h = { 'Content-Type': 'application/json', 'X-Space-Actor': api.me || '', 'X-Space-Kind': 'human' };
      if (api.flags && api.flags.key) h['X-Space-Key'] = api.flags.key;
      const r = await fetch(`${base}/api/run/structure`, { method: 'POST', credentials: 'same-origin', headers: h, body: JSON.stringify({ file_ids: material.map((m) => m.id), notes }) });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.hint || j.error || `HTTP ${r.status}`);
      const sp = j.spec || {};
      setTitle(sp.title || title); setGoal(sp.goal || goal); setContext(sp.context || context);
      setCriteria(sp.criteria && sp.criteria.length ? sp.criteria : criteria);
      setFacts(sp.facts && sp.facts.length ? sp.facts : facts);
      setLimits(sp.limits && sp.limits.length ? sp.limits : limits);
      setParts(sp.partsList && sp.partsList.length ? sp.partsList : parts);
      setField(sp.field || field); setScope(sp.scope || scope); setOpenQs(sp.open_questions || []);
      const readable = (j.manifest || []).filter((m) => m.used > 0).length;
      setDraftNote(`Drafted by Claude from ${readable} readable file${readable === 1 ? '' : 's'} of ${(j.manifest || []).length}. Check every line; it marks guesses with "(guess)".`);
      setStep(STEPS.length - 1);
    } catch (ex) { setErr(`Could not draft: ${ex.message}`); }
    setDrafting(false);
  };

  const upload = async (file) => {
    if (!api.me) { setErr('Sign in to share files.'); return; }
    setBusy((b) => b + 1); setErr('');
    try {
      const h = { 'X-Space-Actor': api.me, 'X-Space-Kind': 'human', 'Content-Type': file.type || 'application/octet-stream', 'X-Space-Filename': encodeURIComponent(file.name) };
      if (api.flags && api.flags.key) h['X-Space-Key'] = api.flags.key;
      const r = await fetch(`${base}/api/upload`, { method: 'POST', credentials: 'same-origin', headers: h, body: file });
      const j = await r.json().catch(() => ({}));
      if (!r.ok) throw new Error(j.hint || j.error || `HTTP ${r.status}`);
      setFiles((f) => [...f, j]);
    } catch (ex) { setErr(`${file.name}: ${ex.message}`); }
    setBusy((b) => b - 1);
  };

  const spec = () => {
    const succ = criteria.filter((c) => c.name.trim()).map((c) => `${c.name.trim()}: ${(c.how || '').trim() || c.name.trim()}`).join('\n');
    const known = [...facts.filter((f) => f.text.trim()).map((f) => `${f.text.trim()}${f.source && f.source.trim() ? ` (source: ${f.source.trim()})` : ''}`),
      ...files.map((f) => `File ${f.name}${f.excerpt ? `: ${f.excerpt.slice(0, 300).replace(/\s+/g, ' ')}` : ''}`)].join('\n');
    const fixed = limits.filter((l) => l.text.trim()).map((l) => l.text.trim()).join('\n');
    const goalText = [goal.trim(), context.trim() ? `Situation: ${context.trim()}` : '', scope.trim() ? `Scope: ${scope.trim()}` : '', openQs.length ? `Open questions: ${openQs.join('; ')}` : ''].filter(Boolean).join(' ');
    return { title: title.trim(), goal: goalText, success: succ, known, fixed, parts: partsText(parts, deep), deep, field: field.trim(),
      // kept for editing
      context, criteria, facts, limits, partsList: parts, scope, files: [...material, ...files].map((f) => f.name), material, notes, draftNote, open_questions: openQs };
  };

  const finish = async () => {
    const sp = spec();
    // files become findings now, so the team reads them from the first step
    for (const f of [...material, ...files]) {
      try { await api.post('finding_posted', { title: f.name.slice(0, 120), text: `Shared when describing the problem: ${title.trim()}`.slice(0, 400), kind: f.kind || 'data', source: f.name, values: {}, part: null, excerpt: f.excerpt || '', file: { id: f.id, name: f.name, bytes: f.bytes, type: f.type, lines: f.lines ?? null, text: !!f.text } }, { subject: 'run:main' }); }
      catch (e) { /* the file stays uploaded; the finding can be shared from the tab */ }
    }
    onDone(sp);
  };

  // rendered as a plain call, not as a component: a component made inside render is a new one each time, so
  // Preact would rebuild the inputs on every keystroke and the focus would be lost after one character
  const Step = () => {
    switch (step) {
      case 0: return html`<div class="wz-step">
        <p class="wz-why">Most of what the team needs is already in your research folder: notes, data, drafts, results, the papers you work from. Pick that folder, or drop the files that matter, and Claude reads them and drafts the problem for you. You then correct it, step by step.</p>
        <div class="wz-drop wz-drop--big" onClick=${() => folderInput.current && folderInput.current.click()}
          onDragOver=${(e) => e.preventDefault()} onDrop=${(e) => { e.preventDefault(); uploadMaterial(e.dataTransfer.files); }}>
          <input ref=${folderInput} type="file" multiple webkitdirectory style="display:none" onChange=${(e) => { uploadMaterial(e.target.files); e.target.value = ''; }} />
          <strong>Pick your research folder</strong><div class="muted">or drop files here. Text, Markdown, CSV, JSON and code are read in full; PDFs and images by name for now. Up to 40 files, 8 MB each.</div>
          ${busy ? html`<div class="muted">uploading...</div>` : null}
        </div>
        <div class="wz-row wz-row--files"><button class="btn btn--small" type="button" onClick=${(e) => { e.stopPropagation(); if (fileInput.current) fileInput.current.click(); }}>+ single files</button>
          <input ref=${fileInput} type="file" multiple style="display:none" onChange=${(e) => { uploadMaterial(e.target.files); e.target.value = ''; }} /></div>
        ${material.length ? html`<ul class="wz-files">${material.map((f) => html`<li><span>${f.name}</span><span class="muted">${f.lines ? `${f.lines} lines` : f.text ? `${f.bytes} B` : 'name only'}</span><button class="btn btn--small" type="button" onClick=${() => setMaterial(material.filter((x) => x.id !== f.id))}>x</button></li>`)}</ul>` : null}
        <label class="wz-label">Anything the files do not say <span class="muted">optional: what you want, in a few words</span></label>
        <textarea class="wz-input" rows="2" value=${notes} onInput=${(e) => setNotes(e.target.value)} placeholder="We want to cut the morning wait without hiring; the spreadsheet has last month's arrival times."></textarea>
        <div class="wz-row"><button class="btn btn--primary" type="button" disabled=${drafting || busy || (!material.length && !notes.trim())} onClick=${draft}>${drafting ? 'Claude is reading...' : 'Let Claude draft the problem'}</button>
          <button class="btn" type="button" onClick=${() => setStep(1)}>Write it myself</button></div>
      </div>`;
      case 1: return html`<div class="wz-step">
        <p class="wz-why">Say what you want to find out or improve, and the situation it lives in. The team plans from this text alone, so a short paragraph beats a line. Write it the way you would explain it to a colleague who does not know your work.</p>
        <label class="wz-label">Title <span class="muted">a few words</span></label>
        <input class="wz-input" value=${title} onInput=${(e) => setTitle(e.target.value)} maxlength="120" placeholder="Cut waiting time at the clinic front desk" autofocus />
        <label class="wz-label">The goal <span class="muted">${goal.trim().length} characters, ${words(goal)} words</span></label>
        <textarea class="wz-input" rows="5" value=${goal} onInput=${(e) => setGoal(e.target.value)} placeholder="Patients wait 25 minutes on average at check-in, and the morning queue spills into the corridor. I want a check-in process that cuts the average wait to under 10 minutes without hiring anyone, keeping the same two receptionists and the current software."></textarea>
        <label class="wz-label">The situation <span class="muted">optional: what is done today, who is involved, what has been tried</span></label>
        <textarea class="wz-input" rows="3" value=${context} onInput=${(e) => setContext(e.target.value)} placeholder="Today every patient fills a paper form at the desk and the receptionist types it in. We tried a second desk last year; it helped a little but we could not staff it."></textarea>
      </div>`;
      case 2: return html`<div class="wz-step">
        <p class="wz-why">How will the team know a proposal is good? Each line here becomes something the judges score. Name it, then say how to tell. Pick from the list or write your own.</p>
        <div class="wz-chips">${CRITERIA_IDEAS.filter(([n]) => !criteria.some((c) => c.name === n)).map(([n, how]) => html`<button class="wz-chip" type="button" onClick=${() => setCriteria([...criteria, { name: n, how }])}>+ ${n}</button>`)}</div>
        <${Rows} rows=${criteria} setRows=${setCriteria} addLabel="criterion" empty="No criteria yet."
          fields=${[{ key: 'name', placeholder: 'Name, like Shorter wait' }, { key: 'how', placeholder: 'How to tell, like the average wait at check-in drops below 10 minutes', multi: true }]} />
      </div>`;
      case 3: return html`<div class="wz-step">
        <p class="wz-why">Facts, numbers, past results, what the literature says. The inventors reason from these, the critics check against them, and they are cited by number in every proposal. Files are shared with the team as findings right away.</p>
        <${Rows} rows=${facts} setRows=${setFacts} addLabel="fact" empty="No facts yet."
          fields=${[{ key: 'text', placeholder: 'A fact, like: mornings are the busiest, 60 percent of arrivals come before 10', multi: true }, { key: 'source', placeholder: 'Source (optional): a measurement, a paper, own observation' }]} />
        <div class="wz-drop" onClick=${() => fileInput.current && fileInput.current.click()}
          onDragOver=${(e) => e.preventDefault()} onDrop=${(e) => { e.preventDefault(); for (const f of Array.from(e.dataTransfer.files || [])) upload(f); }}>
          <input ref=${fileInput} type="file" multiple style="display:none" onChange=${(e) => { for (const f of Array.from(e.target.files || [])) upload(f); e.target.value = ''; }} />
          <strong>Drop files here or click to choose</strong><div class="muted">data, measurements, papers, notes: CSV, JSON, text, Markdown, PDF, images, up to 8 MB each</div>
          ${busy ? html`<div class="muted">uploading...</div>` : null}
        </div>
        ${files.length ? html`<ul class="wz-files">${files.map((f) => html`<li><span>${f.name}</span><span class="muted">${f.lines ? `${f.lines} lines` : `${f.bytes} B`}</span><button class="btn btn--small" type="button" onClick=${() => setFiles(files.filter((x) => x.id !== f.id))}>x</button></li>`)}</ul>` : null}
      </div>`;
      case 4: return html`<div class="wz-step">
        <p class="wz-why">What must stay as it is, what must never happen, and the limits on time, money and people. Every proposal is checked against these, so a limit written here saves a wasted idea later.</p>
        <${Rows} rows=${limits} setRows=${setLimits} addLabel="limit" empty="No limits yet."
          fields=${[{ key: 'text', placeholder: 'A limit, like: the two receptionists stay; no new software this year; results within a month', multi: true }]} />
      </div>`;
      case 5: return html`<div class="wz-step">
        <p class="wz-why">Optional shape. If you already see the parts of the problem, name them and the map starts from yours; otherwise the mapper draws them. The field tells the research step where to look. Scope says what is in and out.</p>
        <label class="wz-label">Parts <span class="muted">optional</span></label>
        <label class="wz-check"><input type="checkbox" checked=${deep} onChange=${(e) => setDeep(e.target.checked)} />
          Two-level map: keep the sub-parts under each part <span class="muted">(for demonstrations; off, the map is the parts only and the sub-parts are ignored)</span></label>
        <${Rows} rows=${parts} setRows=${setParts} addLabel="part" empty="The mapper will draw the parts from the goal."
          fields=${deep ? [{ key: 'name', placeholder: 'A part, like: the forms' }, { key: 'sub', placeholder: 'its sub-parts, separated by commas, like: which fields to drop, who fills it in' }] : [{ key: 'name', placeholder: 'A part, like: the forms; the queue order; the desk layout' }]} />
        <label class="wz-label">Field <span class="muted">optional</span></label>
        <input class="wz-input" value=${field} onInput=${(e) => setField(e.target.value)} maxlength="80" placeholder="clinic operations, compiler design, event organisation..." />
        <label class="wz-label">Scope <span class="muted">optional: what is in, what is out</span></label>
        <textarea class="wz-input" rows="2" value=${scope} onInput=${(e) => setScope(e.target.value)} placeholder="In: check-in on weekday mornings. Out: the appointment system, the phone line."></textarea>
      </div>`;
      default: {
        const sp = spec();
        return html`<div class="wz-step">
          <p class="wz-why">This is what the team gets. Go back to any step to change it. Then choose a size in the panel and start.</p>
          ${draftNote ? html`<div class="wz-draftnote">${draftNote}</div>` : null}
          <div class="wz-review">
            <div class="wz-review__k">Title</div><div>${sp.title || html`<span class="muted">none</span>`}</div>
            <div class="wz-review__k">Goal</div><div class="wz-review__v">${sp.goal}</div>
            <div class="wz-review__k">Judged on</div><div>${criteria.length ? html`<ul>${criteria.map((c) => html`<li><strong>${c.name}</strong>${c.how ? `: ${c.how}` : ''}</li>`)}</ul>` : html`<span class="muted">the default four: correctness, usefulness, feasibility, clarity</span>`}</div>
            <div class="wz-review__k">Known</div><div>${facts.length || files.length ? html`<ul>${facts.map((f) => html`<li>${f.text}${f.source ? html` <span class="muted">(${f.source})</span>` : null}</li>`)}${files.map((f) => html`<li>file ${f.name}</li>`)}</ul>` : html`<span class="muted">nothing yet</span>`}</div>
            <div class="wz-review__k">Limits</div><div>${limits.length ? html`<ul>${limits.map((l) => html`<li>${l.text}</li>`)}</ul>` : html`<span class="muted">none</span>`}</div>
            <div class="wz-review__k">Parts</div><div>${parts.length ? parts.map((p) => deep && p.sub ? `${p.name} (${p.sub})` : p.name).join('; ') : html`<span class="muted">drawn by the mapper</span>`}${deep ? html` <span class="muted">two-level map</span>` : null}</div>
            ${field ? html`<div class="wz-review__k">Field</div><div>${field}</div>` : null}
            ${openQs.length ? html`<div class="wz-review__k">Open questions</div><div><ul>${openQs.map((q) => html`<li>${q}</li>`)}</ul></div>` : null}
            ${material.length ? html`<div class="wz-review__k">Material</div><div>${material.length} file${material.length === 1 ? '' : 's'} shared with the team</div>` : null}
          </div>
        </div>`;
      }
    }
  };

  return html`<div class="wz-backdrop" onClick=${(e) => { if (e.target === e.currentTarget) onClose(); }}>
    <div class="wz" role="dialog" aria-label="Describe your problem">
      <div class="wz-head"><div class="wz-title">Describe your problem</div><button class="btn btn--small" type="button" onClick=${onClose}>x</button></div>
      <ol class="wz-steps">${STEPS.map((s, i) => html`<li class=${`wz-stepname${i === step ? ' is-on' : ''}${i < step ? ' is-done' : ''}`} onClick=${() => { if (i <= 1 || i <= step || checks[1]) setStep(i); }}>${i + 1}. ${s}</li>`)}</ol>
      <div class="wz-body">${Step()}</div>
      ${nudges[step] ? html`<div class="wz-nudge">${nudges[step]}</div>` : null}
      ${err ? html`<div class="error">${err}</div>` : null}
      <div class="wz-foot">
        <button class="btn" type="button" disabled=${step === 0} onClick=${() => setStep(step - 1)}>Back</button>
        <span class="muted wz-count">${step + 1} of ${STEPS.length}</span>
        ${step < STEPS.length - 1
          ? html`<button class="btn btn--primary" type="button" disabled=${!checks[step]} onClick=${() => setStep(step + 1)}>Next</button>`
          : html`<button class="btn btn--primary" type="button" disabled=${!checks[1] || busy} onClick=${finish}>Use this problem</button>`}
      </div>
    </div>
  </div>`;
}

export function mountWizard(api) {
  let host = document.getElementById('wizard-host');
  if (!host) { host = document.createElement('div'); host.id = 'wizard-host'; document.body.appendChild(host); }
  const close = () => render(null, host);
  return {
    open(initial, onDone) {
      render(html`<${Wizard} api=${api} initial=${initial || {}} onClose=${close} onDone=${(sp) => { close(); onDone(sp); }} />`, host);
    },
    close,
  };
}
