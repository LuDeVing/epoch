// index.js: lets `node --test space/web/tests/core` run this folder. Node 25 takes a directory argument as a module
// path, and a directory resolves to its index.js, so this file imports every core test file.
import './match.test.mjs';
import './reduce.test.mjs';
import './store.test.mjs';
import './connect.test.mjs';
import './assets.test.mjs';
import './ui.test.mjs';
