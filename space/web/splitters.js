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
  const apply = () => {
    panes.style.gridTemplateColumns = cols.map((c) => `${c}fr`).join(' ');
    place();
    window.dispatchEvent(new Event('resize'));            // the views refit to the new pane sizes
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
        apply();
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
