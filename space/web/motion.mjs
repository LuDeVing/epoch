// space/web/motion.mjs: the one animation clock the two views share (docs/MULTIPLAYER_DESIGN.md section 10.3).
// smoothDamp is the critically damped helper of research_notes/product/multiplayer/01_visualization.md Appendix A.
// The clock runs one requestAnimationFrame loop, calls every registered step with the frame's dt, and stops when
// no step reports work left (zero CPU when idle). It snaps on visibilitychange and under prefers-reduced-motion.
// Every DOM call is guarded, so the module imports under Node.

export const T = {
  tree: 0.12,        // s, card positions (95 percent at 300 ms, no overshoot)
  bubble: 0.15,      // s, bubble positions and radii
  pointer: 0.08,     // s, other people's focus rings
  camera: 700,       // ms, follow and fit
  halo: 2000,        // ms, change highlight
  ripple: 900,       // ms, winner
  enter: 280,        // ms, card and bubble arrival
  exit: 200,         // ms, retire
  chipFlip: 200,     // ms, queued to applied
  relayoutFade: 200, // ms, staged cluster relayout: leaving fade
  relayoutMove: 700, // ms, moves
  relayoutGrow: 300, // ms, arrivals grow
};

export const REST = 0.1;          // a value is settled when within 0.1 of its target with velocity under 0.1
export const MAX_DT = 0.05;       // s, a long frame (tab switch, GC pause) is clamped so nothing jumps

// Critically damped smoothing (no overshoot, keeps velocity when the target moves). smoothTime in seconds.
// Returns [value, velocity].
export function smoothDamp(cur, vel, target, smoothTime, dt) {
  const omega = 2 / Math.max(1e-4, smoothTime);
  const x = omega * dt;
  const e = 1 / (1 + x + 0.48 * x * x + 0.235 * x * x * x);
  const change = cur - target;
  const temp = (vel + omega * change) * dt;
  return [target + (change + temp) * e, (vel - omega * temp) * e];
}

export function settled(value, target, vel, eps = REST) {
  return Math.abs(value - target) <= eps && Math.abs(vel) <= eps;
}

// Glide one scalar field of an object toward its target: o[k] toward o['t' + k] with velocity o['v' + k].
// With snap, the value jumps to the target. Returns true while the value is still moving.
export function glide(o, k, smoothTime, dt, snap) {
  const tk = 't' + k, vk = 'v' + k;
  const target = o[tk];
  if (snap || !Number.isFinite(o[k])) { o[k] = target; o[vk] = 0; return false; }
  const [v, vel] = smoothDamp(o[k], o[vk] || 0, target, smoothTime, dt);
  if (settled(v, target, vel)) { o[k] = target; o[vk] = 0; return false; }
  o[k] = v; o[vk] = vel;
  return true;
}

const hasDoc = () => typeof document !== 'undefined' && document && typeof document.addEventListener === 'function';

export function prefersReducedMotion() {
  try {
    return typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches;
  } catch { return false; }
}

// makeClock({raf, caf, now, reduced}) -> {add, remove, kick, stop, running, snap, frame, reduced}
//   add(step)   step(dt, {snap, now}) returns true while it still has work
//   kick()      start the loop if it is not running (call after any target changes)
//   snap()      the next frame snaps every value to its target (tab becomes visible again)
//   frame(now)  run one frame by hand (tests, or a host that drives its own loop)
export function makeClock(opts = {}) {
  const raf = opts.raf || (typeof requestAnimationFrame === 'function' ? (f) => requestAnimationFrame(f) : null);
  const caf = opts.caf || (typeof cancelAnimationFrame === 'function' ? (h) => cancelAnimationFrame(h) : null);
  const now = opts.now || (typeof performance !== 'undefined' && performance.now ? () => performance.now() : () => Date.now());
  const steps = new Set();
  let handle = 0, last = 0, pendingSnap = false, running = false;
  const reducedFlag = { value: opts.reduced != null ? !!opts.reduced : prefersReducedMotion() };

  function frame(t) {
    handle = 0;
    const tNow = Number.isFinite(t) ? t : now();
    const dt = Math.min(MAX_DT, Math.max(0, (tNow - last) / 1000));
    last = tNow;
    const snap = pendingSnap || reducedFlag.value;
    pendingSnap = false;
    let busy = false;
    for (const s of steps) {
      try { if (s(dt, { snap, now: tNow })) busy = true; }
      catch (err) { steps.delete(s); if (typeof console !== 'undefined') console.error('motion step failed', err); }
    }
    if (busy && !snap && raf) { running = true; handle = raf(frame); }
    else running = false;
    return busy;
  }

  const clock = {
    reduced: reducedFlag,
    add(step) { steps.add(step); return () => steps.delete(step); },
    remove(step) { steps.delete(step); },
    kick() {
      if (handle || !raf) { if (!raf) frame(now()); return; }
      last = now();
      running = true;
      handle = raf(frame);
    },
    stop() { if (handle && caf) caf(handle); handle = 0; running = false; },
    running() { return running; },
    snap() { pendingSnap = true; clock.kick(); },
    frame,
    steps() { return steps.size; },
  };

  if (hasDoc() && !opts.noListeners) {
    document.addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') clock.snap(); });
    try {
      if (typeof matchMedia === 'function') {
        const mq = matchMedia('(prefers-reduced-motion: reduce)');
        const onChange = () => { reducedFlag.value = mq.matches; clock.kick(); };
        if (mq.addEventListener) mq.addEventListener('change', onChange);
      }
    } catch { /* no matchMedia: keep the start value */ }
  }
  return clock;
}

export const clock = makeClock();
export const kick = () => clock.kick();

// One-shot helpers for the small WAAPI pops and ripples. No-ops when the element cannot animate (Node, old browsers).
export function animateOnce(el, keyframes, options) {
  if (!el || typeof el.animate !== 'function' || clock.reduced.value) return null;
  try { return el.animate(keyframes, options); } catch { return null; }
}

export function later(fn, ms) {
  if (clock.reduced.value || ms <= 0) { fn(); return 0; }
  const t = setTimeout(fn, ms);
  if (t && typeof t.unref === 'function') t.unref();      // under Node a pending timer never holds a test open
  return t;
}
