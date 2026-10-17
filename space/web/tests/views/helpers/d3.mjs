// Loads the vendored D3 7.9.0 UMD under Node and puts it on the global, as the browser's classic script does.
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
export const d3 = require('../../../vendor/d3.min.js');
globalThis.d3 = d3;
