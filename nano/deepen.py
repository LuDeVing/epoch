"""Deepening stage for the nano loop: before an idea is built, it is interrogated.

One call asks every question that matters about the idea (mechanism, interactions with the other
parts, compute and memory, parameters, silent assumptions, failure modes, prior work), with the
actual script and the part's research brief in front of it, answers each with facts (web allowed),
lists what the builder must know, what the idea silently assumes, the NEW ideas that came up on the
way, and the questions it could not answer. Open questions marked as build-relevant are followed
recursively: each child call focuses on one of them with the facts gathered so far.

Research basis (SYNTHESIS.md): elaboration and self-questioning raise the quality of what is built,
not what is believed (EVL-16): answers are facts for the builder and never rank ideas. Ideas that
appear while answering are ordinary sketches with card "deepen" and compete under the same rules.
Numbers without a source are dropped, like unsourced entries in a research brief.

A node: {"id", "cluster_id", "cluster_name", "gen", "depth", "parent", "root", "focus", "qa": [{"q","a"}],
         "known": [str], "assumes": [str], "offshoots": [sketch ids], "open": [{"q", "build"}],
         "dropped_unsourced": int, "call_id", "node", "direction"}
"""
from __future__ import annotations

import re

from nano.ideate import PF, fill  # noqa: F401  (PF: nano/profile.py, or the shim with the LLM defaults in ideate.py)

URL_RE = re.compile(r"https?://[^\s\"'<>)]+")
CLAIM_RE = re.compile(r"%|\bnats?\b|\bppl\b|perplexity|\bbpb\b|faster|slower|speed-?up|improv|reduc|\bgain|accuracy|"
                      r"\bpaper\b|reported|achiev|outperform|\bsota\b|benchmark", re.I)

CHAIN_FORMAT = """CHAIN (the causal path from the change to {v:score_short}, 3 to 6 links, one per line; this is what gets tested, so write what could be measured; directions and bands, never point estimates):
L1: <cause> -> <effect> | quantity: <the measured cell or quantity this link moves> | baseline: <its value in the measurements above, or "unmeasured"> | expect: <direction and rough band> | breaks if: <the observation that would refute this link>
L2: ...
WEAKEST: <the link id you are least sure of>

"""

LINK_STATUS_FORMAT = """LINK STATUS (for each link of the chain you were given, after your answers):
- L1: confirmed|refuted|open | <the fact that settles it, or why it is still open>

"""

DEEPEN_FORMAT = """Use exactly this form:
{head}QUESTIONS, aimed at the weakest links first. Ask only questions whose answer would change how the idea is built, and say which two build choices each one decides:
Q1: <question> | decides: <choice A vs choice B>
A1: <answer, one to three sentences, facts not hopes; write "unknown" when you do not know; put the URL in the answer when a fact comes from the web>
Q2: ...
A2: ...
(as many pairs as needed, at least 6)

KNOWN:
- <one fact per line that whoever builds this must know: sizes, orderings, where it plugs in, what to initialise, what to watch; a fact with a number must end with its source URL> [script|measured|web|belief]
(tag every fact with where it comes from: script = read from the script above; measured = from the measurements above; web = from a page, with its URL; belief = your own reasoning, not yet checked)

ASSUMES:
- <one line per thing this idea silently takes for granted (a design choice a different idea could drop)>

NEW IDEAS (4 to 6, each in this block form, blank line between blocks, one per slot in this order: DROP one of the ASSUMES lines and build what follows; STRENGTHEN the mechanism; SPECIALISE it to {v:narrow_examples}; PORT it to another part, naming the part; COMBINE it with a named known technique; and at least one must be a leap. Each must differ in mechanism from the idea under interrogation):
SLOT: <drop|strengthen|specialise|port|combine|other>
IDEA: <short name>
MECHANISM: <one or two sentences>
PREDICTION: <the observable effect>
TEST: <the cheapest falsifying check>
SOURCE: <"own" or a URL>
PART: <the part of the map this idea belongs to, by its name: the part under interrogation unless the idea is for another part>
KIND: <"port" or "leap"; at least one of the new ideas must be a leap: it drops or flips a rule the {v:recipe} takes for granted, keeps the rest, and might fail>
BREAKS: <leaps only: the rule it drops or flips>
KILL: <leaps only: the number at {v:first_check} that discards it>

OPEN:
- <one unanswered question per line> | build: <yes if the answer would change how this is built, else no> | decides: <the two build choices it would separate>"""

# raw templates with {v:key} placeholders; deepen.ROOT_FORMAT / CHILD_FORMAT / PREMORTEM_FORMAT render them on access
_ROOT_FORMAT = DEEPEN_FORMAT.replace("{head}", CHAIN_FORMAT)
_CHILD_FORMAT = DEEPEN_FORMAT.replace("{head}", "") + "\n\n" + LINK_STATUS_FORMAT.strip()


def _search(web: bool) -> str:
    return "Use web search and fetch as much as it takes to answer with facts rather than guesses. " if web else ""


def root_prompt(brief: str, part_name: str, part_frame: str, constraints: str, web: bool,
                code: str = "", research: str = "", history: str = "") -> str:
    lang = fill("{v:language}")
    return (fill("Interrogate ONE idea before anyone builds it. The idea belongs to this part of the {v:recipe}: ")
            + f"{part_name}. Current design of that part: {part_frame}\n\nCONSTRAINTS:\n{constraints}\n\n"
            + (f"THE CURRENT SCRIPT (the idea will be built into this file):\n```{lang}\n{code}\n```\n\n" if code else "")
            + (f"{research}\n\n" if research else "")
            + (f"{history}\n\n" if history else "")
            + f"THE IDEA:\n{brief}\n\n"
            + fill("Ask yourself as many questions as it takes to cover EVERY aspect of it (at least 6, no upper limit): the exact "
                   "mechanism in terms of the script above, how it interacts with each other part of the {v:recipe}, "
                   "{v:cost_questions}, what it silently assumes, how it could fail or do nothing, and what is already known "
                   "about it. ") + _search(web)
            + fill("First write the chain of links from the change to {v:score_short}, each "
                   "with what would refute it; then the questions, aimed at the weakest links; answer each. Then list what the "
                   "builder must know, what the idea assumes, the new ideas that came up while answering, and the questions you could not answer.\n\n"
                   + _ROOT_FORMAT))


def child_prompt(brief: str, focus: str, known: list[str], part_name: str, constraints: str, web: bool,
                 code: str = "", history: str = "", chain: str = "") -> str:
    facts = "\n".join(f"- {k}" for k in known[:40]) or "- (nothing yet)"
    return (f"Go one level deeper into ONE open question about an idea for the part '{part_name}'.\n\n"
            f"CONSTRAINTS:\n{constraints}\n\n"
            + (f"THE CURRENT SCRIPT:\n```{fill('{v:language}')}\n{code}\n```\n\n" if code else "")
            + (f"{history}\n\n" if history else "")
            + f"THE IDEA:\n{brief}\n\n" + (f"{chain}\n\n" if chain else "") + f"WHAT IS ALREADY ESTABLISHED:\n{facts}\n\n"
            f"THE OPEN QUESTION TO SETTLE: {focus}\n\n"
            "Break this question into as many sub-questions as it takes to settle it (at least 6, no upper limit), covering "
            f"every aspect, and answer each. {_search(web)}Then list what the builder must know, what the idea assumes, "
            "the new ideas that came up while answering, what is still open, and the status of each link of the chain.\n\n" + fill(_CHILD_FORMAT))


def _lines(block: str) -> list[str]:
    return [" ".join(l.lstrip("-* ").split())[:300] for l in block.splitlines() if l.strip().lstrip("-* ")]


def parse(text: str) -> dict:
    """Tolerant parse of the DEEPEN_FORMAT reply."""
    text = text or ""
    qa = []
    for m in re.finditer(r"^Q(\d+):\s*(.+?)\n\s*A\1:\s*(.+?)(?=\n\s*Q\d+:|\n\s*KNOWN:|\n\s*ASSUMES:|\n\s*NEW IDEAS|\n\s*OPEN:|\Z)",
                         text, flags=re.S | re.M):
        qa.append({"q": " ".join(m.group(2).split())[:300], "a": " ".join(m.group(3).split())[:600]})
    for p in qa:                                              # fork test: which build choice the answer decides
        q, _, dec = p["q"].partition("| decides:")
        p["q"], p["decides"] = q.strip(), dec.strip()[:200]
    heads = ("KNOWN:", "ASSUMES:", "NEW IDEAS", "OPEN:", "IDEA:", "LINK STATUS", "CHAIN", "QUESTIONS")

    def section(name: str) -> str:
        stops = "|".join(re.escape(h) for h in heads if h != name and not (name == "NEW IDEAS" and h == "IDEA:"))
        m = re.search(rf"^{re.escape(name)}[^\n]*\n(.*?)(?=^(?:{stops})|\Z)", text, flags=re.S | re.M)
        return m.group(1) if m else ""

    known_raw = _lines(section("KNOWN:"))
    known, dropped, known_tagged = [], 0, []
    for k in known_raw:
        if k.lower().startswith("(tag every fact"):
            continue                                        # the echoed instruction line
        prov = "untagged"
        m = re.search(r"\[(script|measured|web|belief)\]\s*$", k, flags=re.I)
        if m:
            prov = m.group(1).lower()
            k = k[: m.start()].rstrip()
        # a MEASURED claim (a gain, a percentage, a paper's number) needs a source; a fact about the script
        # itself (head dim 64, eps 1e-6, 12 layers) does not
        if re.search(r"\d", k) and not URL_RE.search(k) and CLAIM_RE.search(k) and prov not in ("script", "measured"):
            dropped += 1
            continue
        known_tagged.append({"text": k, "prov": prov})
        if prov != "belief":
            known.append(k)                                 # beliefs never travel as facts
    chain = []
    for cm in re.finditer(r"^L(\d+):\s*(.+)$", section("CHAIN") or text.split("QUESTIONS")[0], flags=re.M):
        parts = [x.strip() for x in cm.group(2).split("|")]
        link = {"id": f"L{cm.group(1)}", "text": parts[0][:200]}
        for pt in parts[1:]:
            k_, _, v_ = pt.partition(":")
            link[k_.strip().lower().replace(" ", "_")[:12]] = v_.strip()[:160]
        chain.append(link)
    wm = re.search(r"^WEAKEST:\s*(L\d+)", text, flags=re.M)
    link_status = []
    for lm in re.finditer(r"^-\s*(L\d+):\s*(confirmed|refuted|open)\s*\|?\s*(.*)$", section("LINK STATUS"), flags=re.M | re.I):
        link_status.append({"id": lm.group(1), "status": lm.group(2).lower(), "why": lm.group(3).strip()[:200]})
    unknown = sum(1 for p in qa if p["a"].lower().startswith("unknown") or p["a"].lower() == "unknown.")
    assumes = _lines(section("ASSUMES:"))
    sketch_text = section("NEW IDEAS")
    if not sketch_text and "IDEA:" in text:                      # model skipped the header
        m = re.search(r"(IDEA:.*?)(?=^OPEN:|\Z)", text, flags=re.S | re.M)
        sketch_text = m.group(1) if m else ""
    open_q = []
    for l in _lines(section("OPEN:")):
        q, _, flag = l.partition("|")
        build = "yes" in flag.lower().split("decides")[0] if flag else True
        dec = flag.lower().partition("decides:")[2].strip()[:200] if "decides:" in flag.lower() else ""
        open_q.append({"q": q.strip()[:300], "build": build, "decides": dec})
    return {"qa": qa[:60], "known": known[:80], "known_tagged": known_tagged[:80], "assumes": assumes[:10], "sketch_text": sketch_text,
            "open": open_q[:12], "dropped_unsourced": dropped, "chain": chain[:8], "weakest": (wm.group(1) if wm else ""),
            "link_status": link_status[:8], "unknown_share": round(unknown / len(qa), 2) if qa else 0.0}


def follow(open_q: list[dict], fanout: int, weakest_text: str = "") -> list[str]:
    """Which open questions to recurse into: build-relevant ones that bear on the weakest link first, then the
    other build-relevant ones; all of them if none is marked."""
    rel = [o for o in open_q if o.get("build")] or list(open_q)
    words = {w for w in re.findall(r"[a-z][a-z0-9_-]{3,}", (weakest_text or "").lower())}
    if words:
        rel.sort(key=lambda o: -len(words & set(re.findall(r"[a-z][a-z0-9_-]{3,}", (o["q"] + " " + o.get("decides", "")).lower()))))
    return [o["q"] for o in rel][:fanout]


def stop_here(parsed: dict, depth: int) -> str | None:
    """Why a chain stops going deeper, or None: half the answers were "unknown" (more questions will not help),
    or a child added no fact and settled no link (the chain has drifted into text)."""
    if parsed.get("unknown_share", 0.0) >= 0.5 and len(parsed.get("qa") or []) >= 4:
        return "half the answers were unknown"
    if depth >= 1 and not parsed.get("known") and not any(s.get("status") != "open" for s in parsed.get("link_status") or []):
        return "no new fact and no link settled"
    return None


def chain_text(chain: list[dict], statuses: list[dict] | None = None) -> str:
    """The mechanism chain as a block for the child calls, the builder and the critic, with link status."""
    if not chain:
        return ""
    st = {}
    for s in statuses or []:
        st[s["id"]] = s
    lines = ["MECHANISM CHAIN (each link names the quantity it moves and what would refute it):"]
    for l in chain:
        tail = " | ".join(f"{k}: {v}" for k, v in l.items() if k not in ("id", "text"))
        s = st.get(l["id"])
        lines.append(f"{l['id']}: {l['text']}" + (f" | {tail}" if tail else "") + (f" | status: {s['status']} ({s['why']})" if s else ""))
    return "\n".join(lines)


def knowledge_text(nodes: list[dict], cap_chars: int = 4000) -> str:
    """Facts and answered questions for the builder, most general first, capped."""
    if not nodes:
        return ""
    lines = []
    roots = [n for n in nodes if not n.get("parent")]
    for n in roots:
        if n.get("chain"):
            statuses = [s for m in nodes if m.get("root") == n.get("id") or m.get("id") == n.get("id") for s in (m.get("link_status") or [])]
            lines.append(chain_text(n["chain"], statuses))
        if n.get("revised_idea"):                       # the author conceded an objection and changed the idea
            lines.append(f"THE IDEA AS REVISED BY ITS AUTHOR AFTER THE PRE-MORTEM (build this version): {n['revised_idea']}")
    lines.append("WHAT IS KNOWN ABOUT THIS IDEA (from interrogating it before building; facts, not instructions; tagged by source):")
    seen = set()
    beliefs = []
    for n in sorted(nodes, key=lambda x: x.get("depth", 0)):
        tagged = n.get("known_tagged") or [{"text": k, "prov": "untagged"} for k in n.get("known", [])]
        for t in tagged:
            key = t["text"].lower()[:80]
            if key in seen:
                continue
            seen.add(key)
            if t.get("prov") == "belief" or t.get("check") == "not supported":
                beliefs.append(t["text"] + (" (its source does not support it)" if t.get("check") == "not supported" else ""))
            else:
                lines.append(f"- {t['text']}" + (f" [{t['prov']}]" if t.get("prov") not in (None, "untagged") else "")
                             + (" [checked against its source]" if t.get("check") == "supported" else ""))
    lines.append("QUESTIONS ALREADY ANSWERED (each with the build choice it decided):")
    for n in sorted(nodes, key=lambda x: x.get("depth", 0)):
        for p in n.get("qa", []):
            lines.append(f"- {p['q']} -> {p['a']}" + (f" [decides: {p['decides']}]" if p.get("decides") else ""))
    if beliefs:
        lines.append("UNVERIFIED BELIEFS of the interrogator (its own reasoning, not facts; do not build on them without a check):")
        lines += [f"- {b}" for b in beliefs[:8]]
    out, total = [], 0
    for l in lines:
        if total + len(l) + 1 > cap_chars:
            break
        out.append(l)
        total += len(l) + 1
    return "\n".join(out)


def calls_per_idea(depth: int, fanout: int) -> int:
    """Interrogation calls one idea costs: 1 + fanout + fanout^2 + ... down to `depth`."""
    return sum(fanout ** d for d in range(depth + 1))


# ---------------------------------------------------------------- pre-mortem: a separate call whose only job is to make the idea fail
OBJECTION_CLASSES = ("breaks_constraint", "hidden_cost", "interaction_cancels", "early_only", "below_noise", "impl_slip", "metric_blind", "scale_only")
LADDER_METRICS = {"param_ratio": "candidate parameters / original (the cap is 1.10)", "step_ratio": "candidate step time / original (the cap is 2.0)",
                  "learn_z": "loss gap to the original at 45 steps in noise units, positive = worse",
                  "long_z": "loss gap at 240 steps in noise units, positive = worse", "trend": "growth of the gap between 120 and 240 steps, positive = losing ground",
                  "fidelity": "1 if the measurement the sketch named moved as stated, else 0"}
_PREMORTEM_FORMAT = """Use exactly this form:
OBJECTIONS:
- <one objection per line: what breaks, why, and the cheapest check that would show it> | severity: high|medium|low | class: breaks_constraint|hidden_cost|interaction_cancels|early_only|below_noise|impl_slip|metric_blind|scale_only | if_true: <metric> <above|below> <number>
(as many as you can find; at least 3. The ladder will measure each objection: if_true names the measurement that would confirm it, from {v:ladder_metrics}, and the threshold; an objection the ladder cannot measure says "if_true: none". Spend your effort on what only the long run, the scale or the exam would reveal: the ladder answers the cheap ones anyway.)
VERDICT: <one sentence: the single most likely way this idea does nothing or hurts>"""


def premortem_prompt(brief: str, part_name: str, constraints: str, code: str, known: list[str], chain: str = "",
                     failed: list[str] | None = None, findings: str = "") -> str:
    """`failed`: the research brief's published failures for the part, with URLs (failed_pack). `findings`: the web
    answers to the critic's own questions (--premortem-web), numbered Q1..Q3."""
    facts = "\n".join(f"- {k}" for k in known[:30]) or "- (none)"
    failed_block = ("PUBLISHED FAILURES FOR THIS PART (from the research brief; each line has its source):\n"
                    + "\n".join(f"- {x}" for x in failed) + "\n\n") if failed else ""
    web_block = (WEB_FINDINGS_HEADER + "\n" + findings.strip() + "\n\nWhen an objection rests on one of these findings, "
                 "end it with '| cite: Q<n>' and keep the finding's URL in the objection.\n\n") if findings and findings.strip() else ""
    return (f"Pre-mortem. Assume this idea for the part '{part_name}' was built, "
            + fill("{v:full_run}, and did NOT "
                   "beat the baseline. Your only job is to explain why, as concretely as possible, in terms of the script below. "
                   "Look for: a constraint it silently breaks, a cost it hides ({v:cost_axes}), an interaction with "
                   "another part that cancels its effect, a reason it only helps early in the {v:run}, a reason the effect is smaller "
                   "than the seed-to-seed noise, and a mistake a builder would make implementing it.\n\n")
            + f"CONSTRAINTS:\n{constraints}\n\nTHE CURRENT SCRIPT:\n```{fill('{v:language}')}\n{code}\n```\n\n"
            f"THE IDEA:\n{brief}\n\n" + (f"{chain}\n\nWhen an objection attacks a link of the chain, end it with '| link: L<n>'.\n\n" if chain else "")
            + f"WHAT THE INTERROGATION ESTABLISHED:\n{facts}\n\n" + failed_block + web_block + fill(_PREMORTEM_FORMAT))


def parse_premortem(text: str) -> dict:
    text = text or ""
    m = re.search(r"OBJECTIONS:\s*\n(.*?)(?=^VERDICT:|\Z)", text, flags=re.S | re.M)
    objections = []
    # raw lines, not the 300-character cut of _lines: the typed fields sit at the END of a long objection
    raw_lines = [" ".join(l.lstrip("-* ").split())[:2000] for l in (m.group(1) if m else "").splitlines() if l.strip().lstrip("-* ")]
    for l in raw_lines:
        if l.startswith("(") or l.lower().startswith("as many"):
            continue                                        # an echoed instruction line, not an objection
        fields = [x.strip() for x in l.split("|")]
        body = fields[0]
        o = {"text": body.strip()[:300], "severity": "medium", "cls": "", "link": "", "if_true": None, "cite": ""}
        for f_ in fields[1:]:
            k_, _, v_ = f_.partition(":")
            k_, v_ = k_.strip().lower(), v_.strip()
            if k_ == "severity":
                sev = v_.lower()[:6]
                o["severity"] = sev if sev in ("high", "medium", "low") else "medium"
            elif k_ == "class":
                c_ = v_.lower().replace(" ", "_")[:24]
                o["cls"] = c_ if c_ in OBJECTION_CLASSES else ""
            elif k_ == "link":
                o["link"] = v_[:6]
            elif k_ == "cite":
                o["cite"] = ",".join(re.findall(r"Q\d", v_.upper()))[:12]
            elif k_ == "if_true":
                mm = re.match(r"(param_ratio|step_ratio|cost_ratio|learn_z|long_z|trend|fidelity)\s+(above|below|>|<)\s*([-+]?\d*\.?\d+)", v_, flags=re.I)
                if mm:
                    o["if_true"] = {"metric": mm.group(1).lower(), "op": "above" if mm.group(2) in ("above", ">") else "below",
                                    "threshold": float(mm.group(3))}
        objections.append(o)
    v = re.search(r"^VERDICT:\s*(.+)$", text, flags=re.M)
    return {"objections": objections[:12], "verdict": (v.group(1).strip()[:300] if v else "")}


FAILED_CAP = 12             # published failures in the critic's default pack


def failed_pack(brief: dict | None, cap: int = FAILED_CAP) -> list[str]:
    """The research brief's "failed" entries (reported not to help or not to transfer) as pack lines with their
    URLs. Entries from this lab's own ledger (ledger://) are left out: the pack already has the measured rows."""
    out = []
    for e in (brief or {}).get("failed", []) or []:
        url = str(e.get("url", ""))
        if not url.startswith(("http://", "https://")):
            continue
        out.append(f"reported not to help: {e.get('name', '')}: {e.get('why', '')} {url}"[:400])
        if len(out) >= cap:
            break
    return out


# ---------------------------------------------------------------- pre-mortem with the web (--premortem-web, default off)
# Before writing objections the critic may ask up to three questions of one shape; the research model answers all
# of them in one delegated call, with URLs. Self-correction helps mainly with reliable external feedback
# (Kamoi et al. 2024, TACL, https://aclanthology.org/2024.tacl-1.78; CRITIC, https://arxiv.org/abs/2305.11738).
PREMORTEM_WEB_CAP = 3
WEB_FINDINGS_HEADER = ("WEB FINDINGS FOR YOUR QUESTIONS (a research assistant searched the web; every claim carries its URL; "
                       "'no source found' means exactly that):")
_PM_QUESTION_RE = re.compile(r"^has\s+(?P<mech>.{3,160}?)\s+been reported to fail or fade\s+"
                             r"(?:at small scale(?:\s+or under\s+(?P<cond>.{3,160}?))?|under\s+(?P<cond2>.{3,160}?))\s*\??$", re.I)


def premortem_questions_prompt(brief: str, part_name: str, constraints: str, chain: str = "") -> str:
    return (f"Pre-mortem, step one. An idea for the part '{part_name}' is about to be built and tested. Before you write "
            "objections against it, a research assistant with web access can check up to three things for you. "
            "Ask only about the mechanisms this idea relies on, and only in this exact shape:\n"
            "has <mechanism> been reported to fail or fade at small scale or under <condition>?\n"
            "Ask nothing if the reported record would not change your objections.\n\n"
            f"CONSTRAINTS:\n{constraints}\n\nTHE IDEA:\n{brief}\n\n" + (f"{chain}\n\n" if chain else "")
            + "Use exactly this form, at most three lines, or the single line NONE:\n"
            "QUESTIONS:\n1. has <mechanism> been reported to fail or fade at small scale or under <condition>?")


def parse_premortem_questions(text: str, cap: int = PREMORTEM_WEB_CAP) -> list[str]:
    """The critic's questions, kept only when they have the required shape; at most `cap`, repeats once."""
    m = re.search(r"QUESTIONS:(.*)", text or "", flags=re.S)
    block = m.group(1) if m else (text or "")
    out, seen = [], set()
    for line in block.splitlines():
        q = re.sub(r"^\s*(?:\d+[.)]|-|\*)\s*", "", line).strip().replace("**", "")
        if not _PM_QUESTION_RE.match(q):
            continue
        q = q.rstrip("?").strip() + "?"
        if q.lower() in seen:
            continue
        seen.add(q.lower())
        out.append(q[:300])
        if len(out) >= cap:
            break
    return out


def premortem_summary(resolved: list[dict], web: bool, web_questions: int = 0) -> dict:
    """report.json "premortem": the objections the ladder judged, the share it confirmed, and whether the critic
    had the web, so a run with --premortem-web can be compared with one without. Each objection counts once
    (by idea and text), a measured status before a pending one."""
    seen, rows = set(), []
    for o in sorted(resolved or [], key=lambda x: x.get("status") in (None, "pending")):
        key = (o.get("idea") or (o.get("dialogue") or {}).get("idea") or "", (o.get("text") or "").lower()[:60])
        if key in seen:
            continue
        seen.add(key)
        rows.append(o)
    by = {k: sum(1 for o in rows if (o.get("status") or "pending") == k) for k in ("confirmed", "refuted", "pending", "untestable")}
    judged = by["confirmed"] + by["refuted"]
    return {"objections": len(rows), **by, "confirmed_share": round(by["confirmed"] / judged, 3) if judged else None,
            "web": "on" if web else "off", "web_questions": int(web_questions),
            "web_cited_objections": sum(1 for o in rows if o.get("cite"))}


def resolve_objections(objections: list[dict], metrics: dict) -> list[dict]:
    """Mark each objection confirmed, refuted, pending (its metric not measured yet) or untestable, from the
    ladder's measurements of the build. Returns copies with status and the measured value."""
    out = []
    for o in objections:
        r = dict(o)
        it = o.get("if_true")
        if not it:
            r["status"] = "untestable"
        else:
            m = it["metric"]
            val = metrics.get(m)
            if m == "fidelity":
                fid = metrics.get("fidelity")
                val = (1.0 if fid.get("ok") else 0.0) if isinstance(fid, dict) and fid.get("checkable") else None
            if val is None:
                r["status"] = "pending"
            else:
                hit = (float(val) > it["threshold"]) if it["op"] == "above" else (float(val) < it["threshold"])
                r["status"], r["measured"] = ("confirmed" if hit else "refuted"), round(float(val), 4)
        out.append(r)
    return out


def standing_classes(roots: list[dict], share: float = 0.4, min_roots: int = 3) -> set[str]:
    """Objection classes the critic raises against most ideas in a run: a checklist the ladder handles once, not
    information about any one idea (research_notes/thinking_parts/07_critique.md C3)."""
    with_obj = [n for n in roots if n.get("objections")]
    if len(with_obj) < min_roots:
        return set()
    counts: dict[str, int] = {}
    for n in with_obj:
        for c in {o.get("cls") for o in n["objections"] if o.get("cls")}:
            counts[c] = counts.get(c, 0) + 1
    return {c for c, k in counts.items() if k / len(with_obj) > share}


def objections_text(objections: list[dict], verdict: str = "", standing: set[str] | None = None) -> str:
    if not objections:
        return ""
    standing = standing or set()
    # an objection of a standing class is collapsed unless the ladder confirmed it on this very idea
    specific = [o for o in objections if o.get("status") == "confirmed" or o.get("cls") not in standing]
    collapsed = [o for o in objections if o not in specific]
    lines = ["WATCH FOR (a pre-mortem tried to make this idea fail; address each, do not dismiss them; a resolved one says what the ladder measured):"]
    order = {"confirmed": 0, "pending": 1, "untestable": 1, "refuted": 2}
    for o in sorted(specific, key=lambda x: (order.get(x.get("status", "pending"), 1), {"high": 0, "medium": 1, "low": 2}.get(x["severity"], 1))):
        tag = f"[{o['severity']}" + (f", {o['cls']}" if o.get("cls") else "") + (f", {o['link']}" if o.get("link") else "")
        st = o.get("status")
        if st in ("confirmed", "refuted"):
            it = o.get("if_true") or {}
            tag += f" | {st.upper()}: {it.get('metric')} measured {o.get('measured')} ({it.get('op')} {it.get('threshold')} would confirm)"
        elif o.get("if_true"):
            it = o["if_true"]
            tag += f" | test: {it['metric']} {it['op']} {it['threshold']}"
        d = o.get("dialogue") or {}
        if d.get("reply") == "concede":
            tag += f" | author conceded, idea changed: {d.get('change') or 'see the revised idea'}"
        elif d.get("reply") == "rebut":
            tag += f" | author rebutted: {d.get('fact', '')[:160]} [{d.get('source') or 'untagged'}], critic: {d.get('verdict')}"
        elif d.get("reply") == "measure":
            tag += f" | author asks to measure: {d.get('test')}"
        lines.append(f"- {tag}] {o['text']}")
    if collapsed:
        cls = sorted({o.get("cls") for o in collapsed if o.get("cls")})
        lines.append(f"- standing objections, raised against most ideas in this run and checked by the ladder for every build, so not specific to this one: {', '.join(cls)} ({len(collapsed)} collapsed)")
    if verdict:
        lines.append(f"- most likely failure: {verdict}")
    return "\n".join(lines)


# ---------------------------------------------------------------- one anchored reply round: the author answers the critic
# research_notes/team_gaps/01_dialogue.md: free debate gives small, unreliable gains; an anchored reply helps. The author
# may only concede (and change the idea), rebut with a quoted fact, or propose a measurement. The critic marks each
# objection resolved, revised or standing. Nothing is dropped: the critic is a checklist, never a gate. Standing
# objections keep their if_true test, so the ladder settles them as before. At most two exchanges; stop early when
# an update changes nothing. The critic sees the ladder's results only after its first objections (in the calibration).
REPLY_KINDS = ("concede", "rebut", "measure")
VERDICTS = ("resolved", "revised", "standing")
MAX_EXCHANGES = 2

_REPLY_FORMAT = """Use exactly this form. One block per objection, by its number, in the order given:
REPLY <i>: concede | rebut | measure
then exactly one line:
CHANGE: <concede only: what the idea changes to, one line>
FACT: <rebut only: a quoted fact that answers the objection> [script|measured|web|belief]
TEST: <measure only: <metric> <above|below> <number> at <ladder rung>>
After the last block, if you conceded anything:
REVISED IDEA: <the idea as it now stands, one or two sentences>
Rules: no other prose. A rebut needs a FACT line, tagged with where the fact comes from (script = read from the script; measured = from a measurement; web = from a page, with its URL; belief = your own reasoning). A belief cannot settle an objection. A TEST names one of these measurements: {v:ladder_metrics}."""

_CRITIC_UPDATE_FORMAT = """Use exactly this form, one line per objection, by its number:
UPDATE <i>: resolved | revised | standing | <one reason>
Rules: resolved only when the reply quotes a fact that settles the objection. A rebut without a FACT line, or with a fact tagged belief, cannot resolve it. A measure reply leaves the objection standing, with its test. A concede makes it revised. Judge the facts, not the tone or the confidence of the reply."""


def test_text(t: dict | None) -> str:
    if not t:
        return ""
    return f"{t['metric']} {t['op']} {t['threshold']:g}" + (f" at {t['rung']}" if t.get("rung") else "")


def reply_prompt(brief: str, chain: str, objections: list[dict], indices: list[int] | None = None) -> str:
    """The author's reply: a fresh call that sees the idea, its chain and the objections, nothing else."""
    idx = indices if indices is not None else list(range(1, len(objections) + 1))
    lines = []
    for i in idx:
        o = objections[i - 1]
        it = o.get("if_true")
        lines.append(f"OBJECTION {i}: {o['text']}" + (f" | if true: {it['metric']} {it['op']} {it['threshold']:g}" if it else ""))
    return ("You proposed the idea below. A critic raised objections against it. Answer each objection with one move: "
            "concede it and change the idea, rebut it with a quoted fact, or propose the measurement that would settle it. "
            "Do not argue. Do not defend the idea with confidence or rhetoric.\n\n"
            f"THE IDEA:\n{brief}\n\n" + (f"{chain}\n\n" if chain else "")
            + "THE OBJECTIONS:\n" + "\n".join(lines) + "\n\n" + fill(_REPLY_FORMAT))


def critic_update_prompt(objections: list[dict], replies: dict[int, dict]) -> str:
    """The critic sees its own objections and the replies, and marks each one."""
    lines = []
    for i in sorted(replies):
        o, r = objections[i - 1], replies[i]
        lines.append(f"OBJECTION {i}: {o['text']}")
        lines.append(f"REPLY {i}: {r['kind']}" + (f" | CHANGE: {r['change']}" if r.get("change") else "")
                     + (f" | FACT: {r['fact']} [{r.get('source') or 'untagged'}]" if r.get("fact") else "")
                     + (f" | TEST: {test_text(r['test'])}" if r.get("test") else ""))
    return ("You raised these objections against an idea. Its author replied to each. Mark each objection. "
            "You are a checklist, not a gate: nothing is dropped because of your marks, and a standing objection is measured later.\n\n"
            + "\n".join(lines) + "\n\n" + _CRITIC_UPDATE_FORMAT)


def _parse_test(v: str) -> dict | None:
    mm = re.match(r"\s*<?\s*([a-z][a-z0-9_]*)\s+(above|below|>|<)\s*([-+]?\d*\.?\d+)\s*(?:at\s+(.+?))?\s*>?\s*$", v or "", flags=re.I)
    if not mm:
        return None
    return {"metric": mm.group(1).lower(), "op": "above" if mm.group(2) in ("above", ">") else "below",
            "threshold": float(mm.group(3)), "rung": (mm.group(4) or "").strip()[:60]}


def parse_replies(text: str) -> dict:
    """REPLY_FORMAT -> {"replies": {i: {"kind", "change", "fact", "source", "test"}}, "revised": str}."""
    text = text or ""
    replies: dict[int, dict] = {}
    for block in re.split(r"(?=^\s*REPLY\s+\d+\s*:)", text, flags=re.M | re.I):
        m = re.match(r"\s*REPLY\s+(\d+)\s*:\s*(concede|rebut|measure)\b", block, flags=re.I)
        if not m:
            continue
        r = {"kind": m.group(2).lower(), "change": "", "fact": "", "source": "", "test": None}
        cm = re.search(r"^\s*CHANGE:\s*(.+)$", block, flags=re.M | re.I)
        fm = re.search(r"^\s*FACT:\s*(.+)$", block, flags=re.M | re.I)
        tm = re.search(r"^\s*TEST:\s*(.+)$", block, flags=re.M | re.I)
        if cm:
            r["change"] = " ".join(cm.group(1).split())[:300]
        if fm:
            f_ = " ".join(fm.group(1).split())
            sm = re.search(r"[\[(]\s*(?:source:\s*)?(script|measured|web|belief)\s*[\])]\s*$", f_, flags=re.I)
            if sm:
                r["source"], f_ = sm.group(1).lower(), f_[: sm.start()].rstrip()
            r["fact"] = f_[:400]
        if tm:
            r["test"] = _parse_test(tm.group(1))
        replies.setdefault(int(m.group(1)), r)
    rv = re.search(r"^\s*REVISED IDEA:\s*(.+)$", text, flags=re.M | re.I)
    return {"replies": replies, "revised": (" ".join(rv.group(1).split())[:400] if rv else "")}


def parse_updates(text: str) -> dict[int, dict]:
    """CRITIC_UPDATE_FORMAT -> {i: {"verdict", "reason"}}."""
    out: dict[int, dict] = {}
    for m in re.finditer(r"^\s*UPDATE\s+(\d+)\s*:\s*(resolved|revised|standing)\b\s*\|?\s*(.*)$", text or "", flags=re.M | re.I):
        out.setdefault(int(m.group(1)), {"verdict": m.group(2).lower(), "reason": m.group(3).strip()[:300]})
    return out


def apply_rules(reply: dict | None, said: dict | None) -> str:
    """The verdict the rules allow, whatever the critic wrote. A concede is revised; a measure is standing with its test;
    a rebut resolves only with a FACT not tagged belief, and only if the critic accepts it; no reply leaves it standing."""
    if not reply:
        return "standing"
    if reply["kind"] == "concede":
        return "revised"
    if reply["kind"] == "measure":
        return "standing"
    ok_fact = bool(reply.get("fact")) and reply.get("source") != "belief"
    return "resolved" if (ok_fact and (said or {}).get("verdict") == "resolved") else "standing"


def run_dialogue(objections: list[dict], ask_author, ask_critic, max_exchanges: int = MAX_EXCHANGES) -> dict:
    """The reply round. ask_author(indices) -> REPLY_FORMAT text; ask_critic(replies) -> CRITIC_UPDATE_FORMAT text;
    either may return None when the budget is out. Returns {"objections": copies, each with a "dialogue" field, and a
    measure reply's test as if_true when the objection had none; "rows"; "exchanges"; "revised"; "stop"}.
    Never drops an objection and never removes an if_true: the critic is a checklist, not a gate."""
    objs = [dict(o) for o in objections]
    state = {i: {"verdict": "standing", "reply": None, "reason": "", "exchange": 0} for i in range(1, len(objs) + 1)}
    rows, revised, stop, ex = [], [], "", 0
    todo = sorted(state)
    cap = max(0, min(max_exchanges, MAX_EXCHANGES))
    while todo and ex < cap:
        rtext = ask_author(todo)
        if rtext is None:
            stop = "budget"
            break
        ex += 1
        pr = parse_replies(rtext)
        replies = {i: r for i, r in pr["replies"].items() if i in todo}
        if pr["revised"]:
            revised.append(pr["revised"])
        utext = ask_critic(replies) if replies else ""
        said = parse_updates(utext or "")
        changed = False
        for i in todo:
            r = replies.get(i)
            v = apply_rules(r, said.get(i))
            new_test = bool(r and r["kind"] == "measure" and r.get("test"))
            if new_test and not objs[i - 1].get("if_true"):
                objs[i - 1]["if_true"] = {k: r["test"][k] for k in ("metric", "op", "threshold")}
            if v != state[i]["verdict"] or new_test:
                changed = True
            state[i] = {"verdict": v, "reply": r, "reason": (said.get(i) or {}).get("reason", ""), "exchange": ex}
            rows.append({"objection": i, "cls": objs[i - 1].get("cls", ""), "reply": (r or {}).get("kind", "none"),
                         "fact": (r or {}).get("fact", ""), "source": (r or {}).get("source", ""),
                         "test": test_text((r or {}).get("test")), "change": (r or {}).get("change", ""),
                         "verdict": v, "reason": state[i]["reason"], "exchange": ex})
        if not changed:
            stop = "nothing changed"
            break
        # a second reply only for objections still standing with no test of any kind attached
        todo = [i for i in todo if state[i]["verdict"] == "standing" and not objs[i - 1].get("if_true")]
    if not stop:
        stop = "cap" if todo else "done"
    for i, o in enumerate(objs, 1):
        st, r = state[i], state[i]["reply"] or {}
        o["dialogue"] = {"reply": r.get("kind", "none"), "verdict": st["verdict"], "fact": r.get("fact", ""),
                         "source": r.get("source", ""), "test": test_text(r.get("test")), "change": r.get("change", ""),
                         "reason": st["reason"], "exchange": st["exchange"]}
    return {"objections": objs, "rows": rows, "exchanges": ex, "revised": revised[-1] if revised else "", "stop": stop}


def dialogue_summary(rows: list[dict], resolved_objs: list[dict] | None = None) -> dict:
    """report.json "dialogue": counts by reply kind and final verdict, and the critic's calibration after the ladder:
    of the objections it marked resolved, how many the metric later confirmed (so the resolution was wrong)."""
    final: dict[tuple, dict] = {}
    exchanges: dict = {}
    for r in rows:
        final[(r.get("idea"), r.get("objection"))] = r          # the last exchange wins
        exchanges[r.get("idea")] = max(exchanges.get(r.get("idea"), 0), int(r.get("exchange") or 0))
    by_reply = {k: 0 for k in REPLY_KINDS + ("none",)}
    by_verdict = {k: 0 for k in VERDICTS}
    for r in final.values():
        by_reply[r.get("reply", "none")] = by_reply.get(r.get("reply", "none"), 0) + 1
        by_verdict[r.get("verdict", "standing")] = by_verdict.get(r.get("verdict", "standing"), 0) + 1
    calib = {v: {"confirmed": 0, "refuted": 0, "pending": 0, "untestable": 0} for v in VERDICTS}
    seen = set()
    for o in sorted(resolved_objs or [], key=lambda x: x.get("status") in (None, "pending")):   # a measured build first
        d = o.get("dialogue") or {}
        key = (d.get("idea") or "", (o.get("text") or "").lower()[:60])
        if d.get("verdict") not in calib or key in seen:
            continue
        seen.add(key)
        st = o.get("status") or "pending"
        calib[d["verdict"]][st] = calib[d["verdict"]].get(st, 0) + 1
    res = calib["resolved"]
    judged = res["confirmed"] + res["refuted"]
    return {"ideas": len(exchanges), "objections": len(final), "exchanges": sum(exchanges.values()),
            "by_reply": by_reply, "by_verdict": by_verdict, "after_ladder": calib,
            "resolved_later_confirmed": res["confirmed"], "resolved_later_refuted": res["refuted"],
            "resolved_wrong_share": round(res["confirmed"] / judged, 3) if judged else None}


_RENDERED = {"ROOT_FORMAT": "_ROOT_FORMAT", "CHILD_FORMAT": "_CHILD_FORMAT", "PREMORTEM_FORMAT": "_PREMORTEM_FORMAT",
             "REPLY_FORMAT": "_REPLY_FORMAT", "CRITIC_UPDATE_FORMAT": "_CRITIC_UPDATE_FORMAT"}


def __getattr__(name: str):
    """deepen.ROOT_FORMAT, CHILD_FORMAT, PREMORTEM_FORMAT, REPLY_FORMAT and CRITIC_UPDATE_FORMAT are rendered for the active profile on access."""
    if name in _RENDERED:
        return fill(globals()[_RENDERED[name]])
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
