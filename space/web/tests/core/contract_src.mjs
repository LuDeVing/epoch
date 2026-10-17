// contract_src.mjs: the contract the core tests check against, read from disk (never from another part's code path).
// Kinds come from space/web/contract.json when it exists (P0's export), else from the KINDS table of
// space/contract.py, else from section 6.1 of docs/MULTIPLAYER_DESIGN.md. The per-kind sentences are read from the
// Python table (contract.py, else the design doc), because the JSON export does not carry them.
import { existsSync, readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, resolve } from 'node:path';

export const HERE = dirname(fileURLToPath(import.meta.url));
export const WEB = resolve(HERE, '..', '..');
export const REPO = resolve(WEB, '..', '..');

function kindsBlock() {
  const py = join(REPO, 'space', 'contract.py');
  if (existsSync(py)) return { src: 'space/contract.py', text: readFileSync(py, 'utf8') };
  const doc = readFileSync(join(REPO, 'docs', 'MULTIPLAYER_DESIGN.md'), 'utf8');
  const start = doc.indexOf('### 6.1 space/contract.py');
  return { src: 'docs/MULTIPLAYER_DESIGN.md 6.1', text: doc.slice(start, doc.indexOf('### 6.2', start)) };
}

export function pythonKinds() {
  const { src, text } = kindsBlock();
  const body = text.slice(text.indexOf('KINDS = {'), text.indexOf('\n}', text.indexOf('KINDS = {')));
  const out = {};
  const re = /^\s+"(\w+)":\s+\((.*)\),\s*$/gm;
  let m;
  while ((m = re.exec(body))) {
    const tail = /,\s*(None|'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)")\s*$/.exec(m[2]);
    const writers = /^\s*"([^"]*)"/.exec(m[2]);
    out[m[1]] = { sentence: !tail || tail[1] === 'None' ? null : (tail[2] ?? tail[3]), by: writers ? writers[1].split(/\s+/) : [] };
  }
  return { src, kinds: out };
}

export function loadContract() {
  const p = join(WEB, 'contract.json');
  if (existsSync(p)) return { src: 'space/web/contract.json', json: JSON.parse(readFileSync(p, 'utf8')) };
  const { src, kinds } = pythonKinds();
  return { src, json: { kinds: Object.fromEntries(Object.entries(kinds).map(([k, v]) => [k, { by: v.by }])) } };
}

export function loadLog(name = 'log_sample.ndjson') {
  return readFileSync(join(WEB, 'fixtures', name), 'utf8').split('\n').filter(Boolean).map((l) => JSON.parse(l));
}
