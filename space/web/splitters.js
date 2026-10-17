// splitters.js: drag the two dividers between the problem tree, the idea clusters and the rail to make a pane bigger
// or smaller. Double-click a divider to go back to the default split. The split is kept per browser (localStorage).
const KEY = 'htsa.panes';
const DEFAULT = [40, 35, 25];
const MIN = 12;                 // a pane never shrinks below this percent

function load() {
  try {
    const v = JSON.parse(localStorage.getItem(KEY) || 'null');
    if (Array.isArray(v) && v.length === 3 && v.every((x) => Number.isFinite(x) && x >= MIN)) return v;
  } catch (e) { /* storage may be blocked */ }
  return DEFAULT.slice();
}
function save(v) { try { localStorage.setItem(KEY, JSON.stringify(v)); } catch (e) { /* ignore */ } }

export function mountSplitters(panes) {
  if (!panes || panes.querySelector('.splitter')) return null;
  let cols = load();
  const apply = (notify = true) => {
    panes.style.gridTemplateColumns = cols.map((c) => `${c}fr`).join(' ');
    place();
    if (notify) window.dispatchEvent(new Event('resize'));   // the views refit once the drag ends, never on every move
  };
  const handles = [0, 1].map((i) => {
    const h = document.createElement('div');
    h.className = 'splitter';
    h.setAttribute('role', 'separator');
    h.setAttribute('aria-orientation', 'vertical');
    h.setAttribute('title', 'drag to resize, double-click to reset');
    h.dataset.index = String(i);
    panes.appendChild(h);
    return h;
  });
  function place() {
    const total = cols.reduce((a, b) => a + b, 0);
    let acc = 0;
    handles.forEach((h, i) => { acc += cols[i]; h.style.left = `calc(${(acc / total) * 100}% - 4px)`; });
  }
  handles.forEach((h, i) => {
    h.addEventListener('dblclick', () => { cols = DEFAULT.slice(); save(cols); apply(); });
    h.addEventListener('pointerdown', (e) => {
      e.preventDefault();
      h.setPointerCapture(e.pointerId);
      h.classList.add('is-dragging');
      document.body.classList.add('is-resizing');
      const rect = panes.getBoundingClientRect();
      const total = cols.reduce((a, b) => a + b, 0);
      const before = cols.slice(0, i).reduce((a, b) => a + b, 0);           // share left of this divider
      const pair = cols[i] + cols[i + 1];
      const move = (ev) => {
        const x = Math.min(Math.max(ev.clientX - rect.left, 0), rect.width);
        let left = (x / rect.width) * total - before;                       // the share of pane i
        left = Math.min(Math.max(left, MIN), pair - MIN);
        cols[i] = left; cols[i + 1] = pair - left;
        apply(false);
      };
      const up = () => {
        h.classList.remove('is-dragging');
        document.body.classList.remove('is-resizing');
        h.removeEventListener('pointermove', move);
        h.removeEventListener('pointerup', up);
        h.removeEventListener('pointercancel', up);
        cols = cols.map((c) => Math.round(c * 10) / 10);
        save(cols);
        apply();
      };
      h.addEventListener('pointermove', move);
      h.addEventListener('pointerup', up);
      h.addEventListener('pointercancel', up);
    });
  });
  apply();
  window.addEventListener('resize', place);
  return { reset: () => { cols = DEFAULT.slice(); save(cols); apply(); }, get: () => cols.slice() };
}

// ---- the bottom strip: drag its top edge to make it taller or shorter, a chevron collapses it to one line
const STRIP_KEY = 'htsa.strip';
export function mountStripResizer(strip) {
  if (!strip || !strip.parentNode || strip.parentNode.querySelector('.strip-handle')) return null;
  let st = { h: 0, open: true };                      // h in px, 0 = the default (22vh)
  try { const v = JSON.parse(localStorage.getItem(STRIP_KEY) || 'null'); if (v && typeof v === 'object') st = { ...st, ...v }; } catch (e) { /* ignore */ }
  const save = () => { try { localStorage.setItem(STRIP_KEY, JSON.stringify(st)); } catch (e) { /* ignore */ } };
  const handle = document.createElement('div');
  handle.className = 'strip-handle';
  handle.setAttribute('role', 'separator');
  handle.setAttribute('aria-orientation', 'horizontal');
  handle.title = 'drag to resize the strip, double-click to reset';
  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'strip-handle__btn';
  handle.appendChild(btn);
  strip.parentNode.insertBefore(handle, strip);
  const apply = (notify = true) => {
    strip.classList.toggle('is-collapsed', !st.open);
    strip.style.height = st.open && st.h > 0 ? `${st.h}px` : '';
    strip.style.maxHeight = st.open && st.h > 0 ? `${st.h}px` : '';
    btn.textContent = st.open ? 'v' : '^';
    btn.title = st.open ? 'collapse the strip to one line' : 'expand the strip';
    if (notify) window.dispatchEvent(new Event('resize'));
  };
  btn.addEventListener('click', (e) => { e.stopPropagation(); st.open = !st.open; save(); apply(); });
  handle.addEventListener('dblclick', () => { st = { h: 0, open: true }; save(); apply(); });
  handle.addEventListener('pointerdown', (e) => {
    if (e.target === btn) return;
    e.preventDefault();
    handle.setPointerCapture(e.pointerId);
    document.body.classList.add('is-resizing-y');
    const startY = e.clientY, startH = strip.getBoundingClientRect().height;
    const maxH = Math.max(80, window.innerHeight * 0.7);
    const move = (ev) => { st.h = Math.min(Math.max(startH + (startY - ev.clientY), 28), maxH); st.open = true; apply(false); };
    const up = () => {
      document.body.classList.remove('is-resizing-y');
      handle.removeEventListener('pointermove', move); handle.removeEventListener('pointerup', up); handle.removeEventListener('pointercancel', up);
      save();
      apply();
    };
    handle.addEventListener('pointermove', move); handle.addEventListener('pointerup', up); handle.addEventListener('pointercancel', up);
  });
  apply();
  return { toggle: () => { st.open = !st.open; save(); apply(); } };
}
