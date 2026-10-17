// matchClusters: the key test of note 01 Appendix A, plus identity and shuffle.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { matchClusters } from '../../match.mjs';

test('split, growth, shuffle and a new cluster (note 01 Appendix A)', () => {
  const s1 = [{ vid: 'v1', members: ['a', 'b', 'c', 'd'] }, { vid: 'v2', members: ['e', 'f', 'g'] }, { vid: 'v3', members: ['h', 'i'] }];
  const s2 = [{ members: ['j'] }, { members: ['h', 'i', 'z'] }, { members: ['e', 'f'] },
    { members: ['a', 'b', 'c', 'd', 'k'] }, { members: ['g'] }];
  const r = matchClusters(s1, s2, 3);
  assert.equal(r.vids[1], 'v3');
  assert.equal(r.vids[2], 'v2');
  assert.equal(r.vids[3], 'v1');
  assert.equal(r.born[r.vids[4]], 'v2');
  assert.equal(r.born[r.vids[0]], undefined);
  assert.deepEqual(r.dead, []);
  assert.equal(r.counter, 5);
});

test('identical input keeps every key; a merge marks the loser dead into the survivor', () => {
  const s1 = [{ vid: 'v1', members: ['a', 'b', 'c'] }, { vid: 'v2', members: ['d'] }];
  const same = matchClusters(s1, [{ members: ['d'] }, { members: ['c', 'b', 'a'] }], 2);
  assert.deepEqual(same.vids, ['v2', 'v1']);
  const merged = matchClusters(s1, [{ members: ['a', 'b', 'c', 'd'] }], 2);
  assert.deepEqual(merged.vids, ['v1']);
  assert.deepEqual(merged.dead, [{ vid: 'v2', into: 'v1' }]);
});
