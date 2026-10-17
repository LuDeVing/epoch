"""Live dashboard for a nano loop run: a tiny local web page that polls the run folder.

Usage:  python -m nano.dashboard --run D:/AGI-lab/runs/<run_id> [--port 8765]
Then open http://127.0.0.1:8765 in a browser. Read-only; stdlib only.

It shows: budget bar and spend, the current round, every agent call (card, operator, seed,
status running/done, tokens, duration, hypothesis), verification results per candidate with the
rung reached, the pool, the decision log, and the idea graph page if graph.py rendered it.
The loop writes live.json (in-flight calls) and the usual files; this page only reads.
"""
from __future__ import annotations

import argparse
import json
import threading
import time
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

RUN: Path = Path(".")


def _read_json(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return default


def _read_jsonl(p: Path) -> list[dict]:
    out = []
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    out.append(json.loads(line))
                except Exception:  # noqa: BLE001
                    pass
    return out


def snapshot() -> dict:
    state = _read_json(RUN / "state.json", {})
    live = _read_json(RUN / "live.json", {"inflight": [], "phase": "", "note": ""})
    calls = []
    for p in sorted((RUN / "calls").glob("*.json"), key=lambda x: x.stat().st_mtime) if (RUN / "calls").exists() else []:
        c = _read_json(p, {})
        meta = c.get("meta") or {}
        calls.append({"call_id": c.get("call_id"), "role": c.get("role"), "card": meta.get("card"),
                      "operator": meta.get("operator"), "seed": meta.get("seed"),
                      "tokens": c.get("total_tokens") or (c.get("usage") or {}).get("total_tokens"),
                      "cost_usd": c.get("cost_usd"), "duration_s": round((c.get("duration_ms") or 0) / 1000),
                      "error": c.get("error"), "model": c.get("model")})
    cands = {}
    for p in (RUN / "cands").glob("*.jsonl") if (RUN / "cands").exists() else []:
        for row in _read_jsonl(p):
            if row.get("id"):
                cands[row["id"]] = {"id": row["id"], "card": row.get("card"), "operator": row.get("operator"),
                                    "seed": row.get("seed"), "round": row.get("round"),
                                    "hypothesis": (row.get("extra") or {}).get("hypothesis"),
                                    "change": (row.get("extra") or {}).get("change"),
                                    "parent_ids": row.get("parent_ids") or [], "lineage_id": row.get("lineage_id"),
                                    "call_id": row.get("call_id")}
            elif row.get("parse_failed"):
                cands[f"parse_fail:{row.get('call_id')}"] = {"id": None, "card": row.get("card"),
                                                             "call_id": row.get("call_id"), "parse_failed": True}
    verify = {v["id"]: v for v in _read_jsonl(RUN / "verify.jsonl")}
    clusters = _read_jsonl(RUN / "clusters.jsonl")
    pool = []
    for p in sorted((RUN / "pool").glob("*.json")) if (RUN / "pool").exists() else []:
        pool.append(_read_json(p, {}))
    answer = _read_json(RUN / "answer.json", None)
    ideas = {s["id"]: s for s in _read_jsonl(RUN / "ideas.jsonl")}
    icl = _read_json(RUN / "idea_clusters.json", {"clusters": []})
    idea_map = []
    for c in sorted(icl.get("clusters", []), key=lambda x: (x.get("rank") is None, x.get("rank") or 0)):
        rep = ideas.get(c.get("representative"), {})
        idea_map.append({"cluster_id": c["cluster_id"], "name": c.get("name"), "n": c.get("n"), "cards": c.get("cards"),
                         "selected": c.get("selected"), "rank": c.get("rank"), "idea": rep.get("idea"), "score": c.get("score"),
                         "obvious": c.get("obvious"), "n_angles": c.get("n_angles"), "merged_from": c.get("merged_from"),
                         "mechanism": rep.get("mechanism"), "prediction": rep.get("prediction"), "test": rep.get("test")})
    deepen = _read_json(RUN / "deepen.json", {"nodes": []}).get("nodes", [])
    gens: dict = {}
    for n in deepen:
        n["offshoot_names"] = [ideas.get(i, {}).get("idea") for i in n.get("offshoots", [])]
        g = gens.setdefault(str(n.get("gen", 0)), {"calls": 0, "offshoots": 0, "facts": 0, "unsourced_dropped": 0})
        g["calls"] += 1; g["offshoots"] += len(n.get("offshoots", [])); g["facts"] += len(n.get("known", []))
        g["unsourced_dropped"] += n.get("dropped_unsourced", 0)
    # where ideas come from: the agent's own, or the web; and how many clusters match the private obvious answers
    src = {"own": 0, "web": 0}
    for s_ in ideas.values():
        src["web" if str(s_.get("source", "own")).startswith("http") else "own"] += 1
    obvious = sum(1 for c in icl.get("clusters", []) if c.get("obvious"))
    merged = sum(len(c.get("merged_from", [])) for c in icl.get("clusters", []))
    tag_src = {}
    for c in icl.get("clusters", []):
        tag_src[c.get("prior_source", "?")] = tag_src.get(c.get("prior_source", "?"), 0) + 1
    ptree = _read_json(RUN / "problem_tree.json", {"nodes": []})
    upward = _read_jsonl(RUN / "proposals_upward.jsonl")
    briefs = {}
    from nano.research import is_part_brief      # analogy files sit beside the briefs and are not briefs
    for p in sorted((RUN / "research").glob("*.json")) if (RUN / "research").exists() else []:
        if not is_part_brief(p):
            continue
        b = _read_json(p, {})
        briefs[p.stem] = {"known": len(b.get("known", [])), "failed": len(b.get("failed", [])),
                          "open": len(b.get("open", [])), "source": b.get("source"),
                          "top": [e.get("name") for e in b.get("known", [])[:3]],
                          "urls": [e.get("url") for e in b.get("known", [])[:3]]}
    for c in icl.get("clusters", []):
        for row in idea_map:
            if row["cluster_id"] == c["cluster_id"]:
                row["prior"], row["prior_match"], row["node"], row["direction"] = c.get("prior"), c.get("prior_match"), c.get("node"), c.get("direction")
    spent = state.get("spent") or sum((c["tokens"] or 0) for c in calls)
    spent_aux = max(int(state.get("spent_aux") or 0), int((live or {}).get("spent_aux") or 0))
    return {"run_id": state.get("run_id") or RUN.name, "model": state.get("model"), "backend": state.get("backend"),
            "arm": state.get("arm", "scaffold"), "baseline_version": state.get("baseline_version"), "lens": state.get("lens"),
            "budget": state.get("B"), "spent": spent, "spent_aux": spent_aux, "aux_budget": state.get("aux_budget"), "rounds": state.get("rounds"),
            "decisions": state.get("decisions") or [], "live": live, "calls": calls,
            "cands": list(cands.values()), "verify": verify, "clusters": clusters, "pool": pool,
            "idea_map": idea_map, "n_sketches": len(ideas), "tree": ptree.get("nodes", []), "upward": upward,
            "briefs": briefs, "deepen": deepen, "gens": gens, "idea_sources": src, "obvious": obvious,
            "merged": merged, "tag_sources": tag_src,
            "answer": answer, "graph_html": (RUN / "graph.html").exists(), "ts": time.strftime("%H:%M:%S")}


PAGE = r"""<!doctype html><html><head><meta charset="utf-8"><title>HTSA nano loop</title>
<style>
body{font:14px/1.4 system-ui,Segoe UI,sans-serif;margin:0;background:#0f1115;color:#e6e6e6}
header{padding:12px 18px;background:#161a22;border-bottom:1px solid #2a2f3a;display:flex;gap:24px;align-items:center;flex-wrap:wrap}
h1{font-size:16px;margin:0}.muted{color:#9aa3b2}.bar{height:14px;background:#262c38;border-radius:7px;overflow:hidden;width:320px}
.fill{height:100%;background:linear-gradient(90deg,#3b82f6,#22c55e)}.grid{display:grid;grid-template-columns:1.1fr 1fr;gap:14px;padding:14px 18px}
.card{background:#161a22;border:1px solid #2a2f3a;border-radius:10px;padding:12px 14px}.card h2{font-size:13px;margin:0 0 8px;color:#9aa3b2;text-transform:uppercase;letter-spacing:.06em}
table{width:100%;border-collapse:collapse;font-size:13px}td,th{padding:5px 6px;border-bottom:1px solid #222733;text-align:left;vertical-align:top}th{color:#9aa3b2;font-weight:600}
.pill{display:inline-block;padding:1px 8px;border-radius:999px;font-size:12px}.run{background:#1d4ed8}.done{background:#166534}.fail{background:#991b1b}.wait{background:#374151}.chk{background:#065f46}
.spin{display:inline-block;width:10px;height:10px;border:2px solid #60a5fa;border-top-color:transparent;border-radius:50%;animation:s 1s linear infinite;margin-right:6px}@keyframes s{to{transform:rotate(360deg)}}
.log{max-height:260px;overflow:auto;font-family:ui-monospace,Consolas,monospace;font-size:12px;white-space:pre-wrap}.wide{grid-column:1/3}
a{color:#60a5fa}
</style></head><body>
<header><h1>HTSA nano loop</h1><span id="run" class="muted"></span><span id="model" class="muted"></span>
<div><div class="bar"><div id="fill" class="fill" style="width:0%"></div></div><span id="spend" class="muted"></span></div>
<span id="phase"></span><span id="ts" class="muted"></span><span id="graph"></span></header>
<div class="grid">
<div class="card"><h2>Agents (model calls)</h2><table><thead><tr><th>status</th><th>card</th><th>operator / seed</th><th>tokens</th><th>time</th><th>result</th></tr></thead><tbody id="calls"></tbody></table></div>
<div class="card"><h2>Candidates and verification</h2><table><thead><tr><th>id</th><th>card</th><th>rung</th><th>status</th><th>hypothesis</th></tr></thead><tbody id="cands"></tbody></table></div>
<div class="card wide"><h2>Problem tree (parts x directions: sketches / clusters / implemented / checked)</h2><table><thead><tr><th>part</th><th>current design</th><th>inward</th><th>outward</th><th>upward</th></tr></thead><tbody id="tree"></tbody></table><div id="upward" class="muted" style="margin-top:8px"></div></div>
<div class="card wide"><h2>Idea map (<span id="nsk">0</span> sketches, clustered by meaning; selected clusters get implemented) <span id="ideastats" class="muted" style="text-transform:none;letter-spacing:0"></span></h2><table><thead><tr><th>#</th><th>idea cluster</th><th>contexts</th><th>cards</th><th>mechanism</th><th>prediction</th><th>test</th><th></th></tr></thead><tbody id="ideas"></tbody></table></div>
<div class="card wide"><h2>Idea interrogation (each chosen idea questioned aspect by aspect before building; offshoots re-enter the idea map)</h2><div id="deepen"></div></div>
<div class="card"><h2>Pool (checked candidates, ranked by the extrapolated long-run gap in seed spreads; negative is better)</h2><table><thead><tr><th>id</th><th>part</th><th>extrap z</th><th>long z</th><th>trend</th><th>learn z</th><th>step s</th><th>change</th></tr></thead><tbody id="pool"></tbody></table></div>
<div class="card"><h2>Decision log</h2><div id="log" class="log"></div></div>
</div>
<script>
const esc=s=>String(s??'').replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));
async function tick(){
  let d; try{ d=await (await fetch('/api/state')).json(); }catch(e){ document.getElementById('phase').innerHTML='<span class="muted">disconnected: the run has ended or the dashboard was closed; the page shows its last state</span>'; for(const el of document.querySelectorAll('.spin')) el.remove(); return; }
  document.getElementById('run').textContent=d.run_id; document.getElementById('model').textContent=(d.model||'')+' / '+(d.backend||'')+' · arm '+(d.arm||'scaffold')+' · baseline '+(d.baseline_version||'')+(d.lens?' · lens '+d.lens:'');
  const pct=d.budget?Math.min(100,100*d.spent/d.budget):0; document.getElementById('fill').style.width=pct+'%';
  document.getElementById('spend').textContent=' '+(d.spent||0).toLocaleString()+' / '+(d.budget||0).toLocaleString()+' tokens (inventing model)'+(d.spent_aux?' · cheap model '+d.spent_aux.toLocaleString()+(d.aux_budget?' / '+d.aux_budget.toLocaleString():'')+', outside the budget':'');
  const L=d.live||{}; document.getElementById('phase').innerHTML=(L.inflight&&L.inflight.length?'<span class="spin"></span>':'')+esc(L.phase||'')+(L.note?' <span class="muted">'+esc(L.note)+'</span>':'');
  document.getElementById('ts').textContent='updated '+d.ts; document.getElementById('graph').innerHTML=d.graph_html?'<a href="/graph.html" target="_blank">idea graph</a>':'';
  const vById=d.verify||{}; const candByCall={}; for(const c of d.cands) if(c.call_id) candByCall[c.call_id]=c;
  const now=Date.now()/1000; const rows=[]; for(const f of (L.inflight||[])) rows.push(`<tr><td><span class="pill run"><span class="spin"></span>running</span></td><td>${esc(f.card||f.role)}</td><td>${esc(f.operator||'')} ${esc(f.seed||'')}</td><td></td><td>${Math.max(0,Math.round(now-f.started))}s</td><td class="muted">${esc(f.note||'')}</td></tr>`);
  for(const c of [...d.calls].reverse()){ const cand=candByCall[c.call_id]; const v=cand&&vById[cand.id]; let res=''; if(c.error) res='<span class="pill fail">error</span> '+esc(c.error.slice(0,80)); else if(c.role==='defaults') res='<span class="muted">defaults written to private/</span>'; else if(cand) res=(v?(v.status==='checked'?'<span class="pill chk">checked rung '+(v.details?.rung_reached??'')+'</span> ':'<span class="pill fail">fail rung '+(v.details?.rung_reached??'')+'</span> '):'<span class="pill wait">awaiting verify</span> ')+esc(cand.change||''); else { const k=String((c.meta&&c.meta.card)||c.role||'').split(':')[0]; const lab={sketch:'idea sketches',deepen:'interrogation chain',premortem:'pre-mortem',research:'web brief',analogy_research:'analogies',cluster:'clustering',prior:'prior-art tags',merge:'merge',plan:'problem map',fact_check:'fact check',implement:'no candidate parsed',revise:'no candidate parsed',fix:'no candidate parsed'}[k]; res='<span class="pill wait">'+esc(lab||('not a build call ('+k+')'))+'</span>'; }
    rows.push(`<tr><td><span class="pill done">done</span></td><td>${esc(c.card||c.role)}</td><td>${esc(c.operator||'')} ${esc(c.seed||'')}</td><td>${(c.tokens||0).toLocaleString()}</td><td>${esc(c.duration_s)}s</td><td>${res}</td></tr>`);}
  document.getElementById('calls').innerHTML=rows.join('');
  document.getElementById('cands').innerHTML=d.cands.filter(c=>c.id).map(c=>{const v=vById[c.id]; const st=v?v.status:'pending'; const cls=st==='checked'?'chk':(st==='fail'?'fail':'wait'); const fb=(v&&v.feedback_record&&v.feedback_record.reason?'<div class="muted">'+esc(v.feedback_record.reason.slice(0,140))+'</div>':'')+(v&&v.prediction_check&&v.prediction_check.checkable?'<div class="muted">prediction '+(v.prediction_check.ok?'held':'missed')+': '+esc((v.prediction_check.details||[]).join('; ').slice(0,160))+'</div>':'')+(v&&v.reused_from?'<div class="muted">verdict reused from '+esc(v.reused_from)+'</div>':''); return `<tr><td>${esc(c.id)}<div class="muted">r${esc(c.round)}${c.parent_ids.length?' child of '+esc(c.parent_ids[0]):''}</div></td><td>${esc(c.card)}<div class="muted">${esc(c.operator)}</div></td><td>${v?esc(v.details?.rung_reached):''}</td><td><span class="pill ${cls}">${esc(st)}</span></td><td>${esc(c.hypothesis||'')}${fb}</td></tr>`;}).join('');
  const cell=s=>s?`${s.sketches} / ${s.clusters} / ${s.implemented} / <b>${s.checked}</b>`:'';
  const bf=d.briefs||{}; const brief=n=>{const b=bf[n.id]; return b?`<div class="muted">research: ${b.known} known, ${b.failed} failed, ${b.open} open (${esc(b.source)})<br>${b.top.map((t,i)=>`<a href="${esc(b.urls[i])}" target="_blank">${esc(t)}</a>`).join(' · ')}</div>`:''};
  document.getElementById('tree').innerHTML=(d.tree||[]).map(n=>`<tr><td><b>${esc(n.name)}</b></td><td class="muted">${esc(n.frame)}${brief(n)}</td><td>${cell(n.stats?.inward)}</td><td>${cell(n.stats?.outward)}</td><td>${cell(n.stats?.upward)}</td></tr>`).join('');
  document.getElementById('upward').innerHTML=(d.upward||[]).length?('<b>Upward proposals (new framings, logged not implemented):</b> '+d.upward.map(u=>esc(u.proposal||u.idea)).join(' · ')):'';
  document.getElementById('ideas').innerHTML='';
  document.getElementById('nsk').textContent=d.n_sketches||0;
  const ptag=c=>c.prior==='new'?'<span class="pill chk">new</span>':(c.prior==='failed'?'<span class="pill fail">known failure</span>':(c.prior==='known'?'<span class="pill wait">known</span>':''));
  const gs=d.gens||{}; const gtxt=Object.keys(gs).sort().map(k=>`gen ${k}: ${gs[k].calls} calls, ${gs[k].offshoots} new ideas, ${gs[k].facts} facts, ${gs[k].unsourced_dropped} unsourced numbers dropped`).join(' · ');
  const is=d.idea_sources||{}; document.getElementById('ideastats').textContent=` — sources: ${is.own||0} own / ${is.web||0} web · ${d.obvious||0} clusters match the private obvious answers · ${d.merged||0} cross-part duplicates merged · tags: ${Object.entries(d.tag_sources||{}).map(([k,v])=>k+' '+v).join(', ')}${gtxt?' · '+gtxt:''}`;
  document.getElementById('ideas').innerHTML=(d.idea_map||[]).map(c=>`<tr><td>${c.rank??''}<div class="muted">${c.score??''}</div></td><td><b>${esc(c.name||c.idea)}</b> ${ptag(c)}${c.obvious?' <span class="pill wait">obvious</span>':''}<div class="muted">${esc(c.node||'')} / ${esc(c.direction||'')}${c.prior_match?' · matches: '+esc(c.prior_match):''}${c.n_angles?' · '+c.n_angles+' angles':''}${(c.merged_from||[]).length?' · merged from '+c.merged_from.map(m=>esc(m.node)).join(', '):''}</div></td><td>${esc(c.n)}</td><td class="muted">${esc((c.cards||[]).join(', '))}</td><td>${esc(c.mechanism||'')}</td><td class="muted">${esc(c.prediction||'')}</td><td class="muted">${esc(c.test||'')}</td><td>${c.selected?'<span class="pill chk">implementing</span>':''}</td></tr>`).join('');
  const dn=d.deepen||[]; const roots=dn.filter(n=>!n.parent);
  const chain=(n)=>{const kids=dn.filter(x=>x.parent===n.id); return `<details ${n.depth===0?'open':''}><summary><b>depth ${n.depth}</b>${n.focus?' · '+esc(n.focus):' · the idea itself'} <span class="muted">(${(n.qa||[]).length} questions, ${(n.known||[]).length} facts, ${(n.offshoots||[]).length} new ideas, ${(n.open||[]).length} open)</span></summary><div style="margin:4px 0 4px 14px">${(n.qa||[]).map(p=>`<div><span class="muted">Q:</span> ${esc(p.q)}<br><span class="muted">A:</span> ${esc(p.a)}</div>`).join('')}${(n.known||[]).length?'<div><b>builder must know:</b><ul>'+(n.known||[]).map(k=>'<li>'+esc(k)+'</li>').join('')+'</ul></div>':''}${(n.offshoot_names||[]).length?'<div><b>new ideas on the way:</b> '+(n.offshoot_names||[]).map(x=>esc(x)).join(' · ')+'</div>':''}${(n.open||[]).length?'<div class="muted"><b>still open:</b> '+(n.open||[]).map(x=>esc(x.q||x)+(x.build?' [build]':'')).join(' · ')+'</div>':''}${kids.map(chain).join('')}</div></details>`};
  document.getElementById('deepen').innerHTML=roots.length?roots.map(r=>`<div style="margin-bottom:10px"><b>${esc(r.cluster_name)}</b> <span class="muted">${esc(r.node||'')} / ${esc(r.direction||'')}</span>${chain(r)}</div>`).join(''):'<span class="muted">not yet</span>';
  document.getElementById('pool').innerHTML=(d.answer?d.answer.ranked:d.pool.map(p=>({id:p.id,node:p.node,extrap_z:p.metrics?.extrap_z,long_z:p.metrics?.long_z,trend:p.metrics?.trend,learn_z:p.metrics?.learn_z,step_s:p.metrics?.step_s,change:p.change}))).map(p=>`<tr><td>${esc(p.id)}</td><td>${esc(p.node||'')}</td><td>${p.extrap_z??''}</td><td>${p.long_z??''}</td><td>${p.trend??''}</td><td>${p.learn_z??''}</td><td>${esc(p.step_s)}</td><td>${esc(p.change||'')}</td></tr>`).join('');
  document.getElementById('log').textContent=(d.decisions||[]).map(x=>JSON.stringify(x)).join('\n')+(d.answer?'\n\nDONE: '+JSON.stringify({n_candidates:d.answer.n_candidates,n_checked:d.answer.n_checked,spent:d.answer.spent_tokens,wall_s:d.answer.wall_s}):'');
}
tick(); setInterval(tick,2000);
</script></body></html>"""


class H(BaseHTTPRequestHandler):
    def log_message(self, *a):  # quiet
        return

    def do_GET(self):
        if self.path.startswith("/api/state"):
            body = json.dumps(snapshot()).encode("utf-8")
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.send_header("Cache-Control", "no-store")
        elif self.path.startswith("/graph.html") and (RUN / "graph.html").exists():
            body = (RUN / "graph.html").read_bytes()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
        else:
            body = PAGE.encode("utf-8")
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)


def serve(run: Path, port: int, open_browser: bool = True) -> None:
    global RUN
    RUN = run
    srv = ThreadingHTTPServer(("127.0.0.1", port), H)
    url = f"http://127.0.0.1:{port}"
    print(f"[dashboard] {url}  (run: {run})", flush=True)
    if open_browser:
        threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", required=True)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--no-browser", action="store_true")
    a = ap.parse_args()
    serve(Path(a.run), a.port, not a.no_browser)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
