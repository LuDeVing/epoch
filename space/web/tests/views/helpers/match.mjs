// Test-only copy of matchClusters from research_notes/product/multiplayer/01_visualization.md Appendix A (tested there).
// The page's copy lives in space/web/match.mjs (P4); the views tests never import another part's code.
export function matchClusters(prev, next, counter, minJ) {
  minJ = minJ == null ? 0.3 : minJ;
  counter = counter || 0;
  const owner = new Map();
  prev.forEach((p, i) => p.members.forEach((m) => owner.set(m, i)));
  const pairs = [];
  next.forEach((n, ni) => {
    const cnt = new Map();
    n.members.forEach((m) => { if (owner.has(m)) cnt.set(owner.get(m), (cnt.get(owner.get(m)) || 0) + 1); });
    cnt.forEach((inter, pi) => {
      const uni = prev[pi].members.length + n.members.length - inter;
      pairs.push({ pi, ni, inter, j: inter / uni });
    });
  });
  pairs.sort((a, b) => b.j - a.j || b.inter - a.inter || a.pi - b.pi || a.ni - b.ni);
  const prevTaken = new Array(prev.length).fill(false);
  const vids = new Array(next.length).fill(null);
  for (const p of pairs) {
    if (p.j < minJ || prevTaken[p.pi] || vids[p.ni] !== null) continue;
    prevTaken[p.pi] = true;
    vids[p.ni] = prev[p.pi].vid;
  }
  const born = {};
  next.forEach((n, ni) => {
    if (vids[ni] !== null) return;
    vids[ni] = 'v' + (++counter);
    const cnt = new Map();
    n.members.forEach((m) => { if (owner.has(m)) cnt.set(owner.get(m), (cnt.get(owner.get(m)) || 0) + 1); });
    let best = null, bestN = 0;
    cnt.forEach((c, pi) => { if (c > bestN) { bestN = c; best = pi; } });
    if (best !== null) born[vids[ni]] = prev[best].vid;
  });
  const dead = [];
  const nextOwner = new Map();
  next.forEach((n, ni) => n.members.forEach((m) => nextOwner.set(m, ni)));
  prev.forEach((p, pi) => {
    if (prevTaken[pi]) return;
    const cnt = new Map();
    p.members.forEach((m) => { if (nextOwner.has(m)) cnt.set(nextOwner.get(m), (cnt.get(nextOwner.get(m)) || 0) + 1); });
    let best = null, bestN = 0;
    cnt.forEach((c, ni) => { if (c > bestN) { bestN = c; best = ni; } });
    dead.push({ vid: p.vid, into: best === null ? null : vids[best] });
  });
  return { vids, born, dead, counter };
}
