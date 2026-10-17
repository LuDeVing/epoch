// accounts.js: the accounts this browser has signed into, [{name, token}], so a person can switch between them
// without typing a password again. Shared by the space page, the People panel and the hub. The token is the
// session the server issued at sign-in; switching asks the server to set its cookie to that session.
export const accounts = {
  list() { try { const v = JSON.parse(localStorage.getItem('htsa.accounts') || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; } },
  save(name, token) {
    if (!name || !token) return;
    const rows = this.list().filter((a) => a.name !== name);
    rows.unshift({ name, token });
    try { localStorage.setItem('htsa.accounts', JSON.stringify(rows.slice(0, 8))); } catch (e) { /* storage blocked */ }
  },
  drop(name) { try { localStorage.setItem('htsa.accounts', JSON.stringify(this.list().filter((a) => a.name !== name))); } catch (e) { /* ignore */ } },
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
