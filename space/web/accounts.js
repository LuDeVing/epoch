// accounts.js: the accounts this browser has signed into, [{name, token}], so a person can switch between them
// without typing a password again. Shared by the space page, the People panel and the hub. The token is the
// session the server issued at sign-in; switching asks the server to set its cookie to that session.
// The list lives in a cookie, not localStorage: a cookie is shared by every port of this host, so the dashboard and
// each space server see the same saved accounts (localStorage is per origin, and every space is another port).
const COOKIE = 'htsa_accounts';
function readCookie() {
  try {
    const m = document.cookie.split(';').map((c) => c.trim()).find((c) => c.startsWith(COOKIE + '='));
    if (!m) return null;
    const v = JSON.parse(decodeURIComponent(m.slice(COOKIE.length + 1)));
    return Array.isArray(v) ? v : null;
  } catch (e) { return null; }
}
function writeCookie(rows) {
  try { document.cookie = `${COOKIE}=${encodeURIComponent(JSON.stringify(rows))}; path=/; max-age=${60 * 60 * 24 * 180}; SameSite=Lax`; } catch (e) { /* ignore */ }
  try { localStorage.setItem('htsa.accounts', JSON.stringify(rows)); } catch (e) { /* storage blocked */ }
}
export const accounts = {
  list() {
    const c = readCookie();
    if (c) return c;
    try { const v = JSON.parse(localStorage.getItem('htsa.accounts') || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; }   // older browsers' list
  },
  save(name, token) {
    if (!name || !token) return;
    const rows = this.list().filter((a) => a.name !== name);
    rows.unshift({ name, token });
    writeCookie(rows.slice(0, 8));
  },
  drop(name) { writeCookie(this.list().filter((a) => a.name !== name)); },
};

function keyQuery() {
  const k = new URLSearchParams(location.search).get('key');
  return k ? `?key=${encodeURIComponent(k)}` : '';
}

// Switch to a saved account on this server. Resolves with the name; throws when the saved session expired.
export async function switchTo(acc, base = location.origin) {
  const r = await fetch(`${base}/api/session/use${keyQuery()}`, { method: 'POST', credentials: 'same-origin',
    headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ token: acc.token }) });
  if (!r.ok) { accounts.drop(acc.name); throw new Error('that saved sign-in expired; sign in again'); }
  return acc.name;
}

// Switch and reopen the space page as that person (accepting an invitation in the address first, if any).
export async function useAccount(acc, base = location.origin) {
  await switchTo(acc, base);
  const params = new URLSearchParams(location.search);
  const code = params.get('invite');
  if (code) {
    try { await fetch(`${base}/api/invites/accept${keyQuery()}`, { method: 'POST', credentials: 'same-origin', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ code }) }); } catch (e) { /* shown later */ }
  }
  const u = new URL(location.href);
  u.searchParams.set('me', acc.name); u.searchParams.delete('invite'); u.searchParams.delete('switch');
  location.replace(u.toString());
}
