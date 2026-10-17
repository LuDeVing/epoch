// Makes `node --test space/web/tests/views` run every *.test.mjs in this folder.
// Node 25 treats a positional argument of --test as a file (a bare directory fails with MODULE_NOT_FOUND), and a
// directory resolves to its index.js. node:test refuses a recursive run() inside a test file, so this file runs
// the real test files through a child `node --test` and fails with the child's report when any test fails.
// `node --test "space/web/tests/views/*.test.mjs"` runs the same files directly.
'use strict';
const { test } = require('node:test');
const assert = require('node:assert/strict');
const { readdirSync } = require('node:fs');
const { join } = require('node:path');
const { spawnSync } = require('node:child_process');

const files = readdirSync(__dirname).filter((f) => f.endsWith('.test.mjs')).sort().map((f) => join(__dirname, f));

test(`views: ${files.length} test files`, (t) => {
  const env = { ...process.env };
  delete env.NODE_TEST_CONTEXT;
  const r = spawnSync(process.execPath, ['--test', '--test-reporter=spec', ...files], { encoding: 'utf8', env, timeout: 120000 });
  const out = (r.stdout || '') + (r.stderr || '');
  const m = /tests (\d+)[\s\S]*?pass (\d+)[\s\S]*?fail (\d+)/.exec(out);
  t.diagnostic(m ? `${m[2]} passed, ${m[3]} failed of ${m[1]} tests in ${files.length} files` : 'no summary found');
  if (r.status !== 0) process.stderr.write(out);
  assert.equal(r.status, 0, `node --test exited ${r.status}`);
});
