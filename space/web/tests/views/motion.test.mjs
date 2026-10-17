// smoothDamp and the shared clock (docs/MULTIPLAYER_DESIGN.md section 10.3, note 01 Appendix A).
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { smoothDamp, makeClock, glide, settled, T, REST, MAX_DT } from '../../motion.mjs';

function run(smoothTime, fps, seconds) {
  let x = 0, v = 0; const dt = 1 / fps; const trace = [];
  for (let i = 1; i * dt <= seconds + 1e-9; i++) { [x, v] = smoothDamp(x, v, 100, smoothTime, dt); trace.push({ t: i * dt, x }); }
  return trace;
}
const at = (trace, t) => trace.find((p) => Math.abs(p.t - t) < 1e-6).x;

test('smoothDamp reaches 95 percent within 300 ms at smoothTime 0.12 with no overshoot', () => {
  const trace = run(0.12, 60, 1);
  assert.ok(at(trace, 0.3) >= 95, `at 300 ms: ${at(trace, 0.3).toFixed(2)}`);
  assert.ok(at(trace, 0.4) >= 99, `at 400 ms: ${at(trace, 0.4).toFixed(2)}`);
  for (const p of trace) assert.ok(p.x <= 100 + 1e-9, `overshoot at ${p.t.toFixed(3)}: ${p.x}`);
  for (let i = 1; i < trace.length; i++) assert.ok(trace[i].x >= trace[i - 1].x - 1e-9, 'monotonic');
});

test('smoothDamp is frame-rate independent within 2 percent (30, 60, 120 fps, sampled at the same instants)', () => {
  const a = run(0.12, 30, 0.5), b = run(0.12, 60, 0.5), c = run(0.12, 120, 0.5);
  for (const t of [0.1, 0.2, 0.3, 0.4]) {
    const xa = at(a, t), xb = at(b, t), xc = at(c, t);
    assert.ok(Math.abs(xa - xb) <= 2, `30 vs 60 fps at ${t}: ${xa.toFixed(2)} vs ${xb.toFixed(2)}`);
    assert.ok(Math.abs(xc - xb) <= 2, `120 vs 60 fps at ${t}: ${xc.toFixed(2)} vs ${xb.toFixed(2)}`);
  }
  // the bubble and pointer times are the documented ones
  assert.equal(T.tree, 0.12); assert.equal(T.bubble, 0.15); assert.equal(T.pointer, 0.08);
  assert.equal(T.camera, 700); assert.equal(T.halo, 2000); assert.equal(T.ripple, 900); assert.equal(T.enter, 280); assert.equal(T.exit, 200);
});

test('smoothDamp keeps velocity when the target moves mid-flight', () => {
  let x = 0, v = 0;
  for (let i = 0; i < 6; i++) [x, v] = smoothDamp(x, v, 100, 0.12, 1 / 60);
  const vBefore = v;
  [x, v] = smoothDamp(x, v, 150, 0.12, 1 / 60);
  assert.ok(v > vBefore * 0.9, 'velocity carries over');
});

test('glide settles a field to its target and reports rest; snap jumps at once', () => {
  const o = { x: 0, vx: 0, tx: 40 };
  let busy = true, frames = 0;
  while (busy && frames < 200) { busy = glide(o, 'x', 0.12, 1 / 60, false); frames++; }
  assert.equal(o.x, 40); assert.equal(o.vx, 0);
  assert.ok(frames > 5 && frames < 60, `settled in ${frames} frames`);
  const s = { y: 0, vy: 0, ty: -30 };
  assert.equal(glide(s, 'y', 0.12, 1 / 60, true), false);
  assert.equal(s.y, -30);
  assert.ok(settled(10, 10.05, 0.05)); assert.ok(!settled(10, 11, 0));
  assert.equal(REST, 0.1); assert.equal(MAX_DT, 0.05);
});

test('the clock runs while a step has work and stops when everything is settled (zero CPU idle)', () => {
  const queue = [];
  let t = 1000;
  const clock = makeClock({ raf: (f) => { queue.push(f); return queue.length; }, caf: () => {}, now: () => t, reduced: false, noListeners: true });
  const o = { x: 0, vx: 0, tx: 100 };
  let calls = 0;
  clock.add((dt) => { calls++; return glide(o, 'x', 0.12, dt, false); });
  assert.equal(clock.running(), false);
  clock.kick();
  assert.equal(clock.running(), true);
  let frames = 0;
  while (queue.length && frames < 500) { const f = queue.shift(); t += 1000 / 60; f(t); frames++; }
  assert.equal(o.x, 100);
  assert.equal(clock.running(), false, 'stopped when settled');
  assert.equal(queue.length, 0, 'no frame is scheduled while idle');
  assert.ok(frames < 80, `${frames} frames`);
  assert.equal(calls, frames);
  // a second kick while idle starts again, and a long gap is clamped so nothing jumps
  o.tx = 0;
  clock.kick();
  const f = queue.shift(); t += 5000; f(t);
  assert.ok(o.x > 50, `clamped dt: x=${o.x.toFixed(1)}`);
});

test('snap() makes the next frame jump every value to its target; reduced motion snaps every frame', () => {
  const queue = [];
  let t = 0;
  const clock = makeClock({ raf: (f) => { queue.push(f); return 1; }, caf: () => {}, now: () => t, reduced: false, noListeners: true });
  const o = { x: 0, vx: 0, tx: 100 };
  clock.add((dt, { snap }) => glide(o, 'x', 0.12, dt, snap));
  clock.kick(); t += 16; queue.shift()(t);
  assert.ok(o.x > 0 && o.x < 100);
  clock.snap(); t += 16; queue.shift()(t);
  assert.equal(o.x, 100);
  assert.equal(queue.length, 0);
  const reduced = makeClock({ raf: (f) => { queue.push(f); return 1; }, caf: () => {}, now: () => t, reduced: true, noListeners: true });
  const p = { x: 0, vx: 0, tx: 70 };
  reduced.add((dt, { snap }) => glide(p, 'x', 0.12, dt, snap));
  reduced.kick(); t += 16; queue.shift()(t);
  assert.equal(p.x, 70);
  assert.equal(reduced.running(), false);
});

test('a throwing step is dropped and the others keep running', () => {
  const queue = [];
  let t = 0;
  const clock = makeClock({ raf: (f) => { queue.push(f); return 1; }, caf: () => {}, now: () => t, reduced: false, noListeners: true });
  const errs = console.error; console.error = () => {};
  try {
    clock.add(() => { throw new Error('boom'); });
    let n = 0;
    clock.add(() => (++n < 3));
    clock.kick();
    let guard = 0;
    while (queue.length && guard++ < 20) { t += 16; queue.shift()(t); }
    assert.equal(n, 3);
    assert.equal(clock.steps(), 1);
  } finally { console.error = errs; }
});
