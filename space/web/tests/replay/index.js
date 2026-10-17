// index.js: lets `node --test space/web/tests/replay` run this folder. Node 25 takes a directory argument as a
// module path, and a directory resolves to its index.js, so this file imports the replay test file.
import './replay.test.mjs';
