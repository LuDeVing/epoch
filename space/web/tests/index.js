// index.js: lets `node --test space/web/tests/` run every page test. Node 25 takes a directory argument as a module
// path, and a directory resolves to its index.js, so this file loads the index.js of each test folder.
import './core/index.js';
import './replay/index.js';
import './views/index.js';
