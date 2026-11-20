# Critique: E12.04 Technical and physical red teams

## Corrections and confirmations (sources re-opened this session)
Re-opened: arXiv abstract pages for PentestGPT (2308.06782), Fang one-day (2404.08144), HPTSA (2406.01637, full text), Cybench (2408.08926), Incalmo (2501.16466), ARTEMIS (2512.09882); ABC News page for TSA 67/70.
1. TSA 67 of 70 confirmed (ABC page: "67 out of 70 tests", "95 percent of trials"). 67/70 = 95.7%. a01 and b01 agree; press rounds to 95 or 96.
2. Fang one-day 87% (13/15) with CVE text, 7% without, 0% for GPT-3.5, open models, ZAP, Metasploit: confirmed from abstract. The "11 of 15 past cutoff" and $3.52 cost in a11 were not re-checked.
3. HPTSA confirmed from full text: 42% pass@5, 18% pass@1, 4.3x over GPT-4 without description at pass@1, 2.0x at pass@5, within 1.8x of the with-description agent at pass@5, ZAP/Metasploit 0%. Correction to a13: the "4.3x" is against GPT-4 with no description, not "prior frameworks" in general (the abstract says prior frameworks). Added facts: benchmark has 14 vulnerabilities; open models got 0 with Llama refusals 31%; ablations: no task-specific agents 2.1x lower pass@1 and 50% lower pass@5; no documents 2.1x and 20% lower; no hierarchy 13x and 6x lower. a25 confirmed.
4. Cybench: abstract confirms 8 models, 4 scaffolds, tasks solved up to 11 minutes human time, hardest 24h54m. Per-model percentages were not re-opened.
5. Incalmo: 37/40 vs 3/40, 12-54 minutes, under $15: confirmed. Correction: the abstract names the failed prior systems as PentestGPT and CyberSecEval3 with Sonnet 4 and Gemini 2.5 Pro, so the 3/40 was measured with strong models. a16 and b15 and b24 are one source.
6. ARTEMIS: ~8,000 hosts, 12 subnets, 9 valid vulnerabilities, 82% valid rate, 9 of 10 humans beaten, $18/h vs $60/h, GUI weakness, false positives: confirmed. a17, a18, a19, b06, b07, b18 are one source. The "first 10 of 16 hours scored" and cost split ($291.47, $944.07) were not re-checked.
7. PentestGPT: 228.6% over GPT-3.5 confirmed. Note the arXiv title is "An LLM-empowered Automatic Penetration Testing Tool"; "Evaluating and Harnessing" is a later version, so a08/a09/a10/b03/c01-c03 are one source under two titles. The 58.6% over GPT-4 figure is in the later version only.
8. GAO radioactive-source test (a03, a04): gao.gov blocked this session (Access Denied), so not re-confirmed. Keep as read earlier.
9. Not re-checked: Baselines Before Architecture numbers (c13-c16), CHECKMATE, PentestEval, honeypot paper. arXiv API returned empty and Semantic Scholar rate-limited.

## Contradictions between sources
- Cybench GPT-4o unguided: 15.0% (b08) vs 12.5% (c19). Likely different attempt counts (3 attempts vs 1). Scaffold table figures (a15, c20) use 3 attempts. Read all Cybench rows as attempt-specific.
- Cybench human-time ratio: 136x (b08, hardest vs 11 min) vs 747x (c19, hardest vs easiest task). Both arithmetically right, different denominators.
- Baseline strength: PentestGPT V2 (b14) reports baselines of 27-49% and 91% for itself on XBOW; the plain-agent paper (c13-c16) gets 67.3% from a plain Codex agent and 92.3% with GPT-5.5. Either the V2 baselines were weak or model version drives the gap. Contested (K06).
- Press number for TSA follow-up (about 80%, 2017) is unopened (b22).
- a07: DSB 2003 red-team report not opened, no numbers.

## Weak spots
- Almost all LLM results are benchmark-owner results (own scaffold, own benchmark, small N: 13 to 15 targets, 40 networks, 14 zero-days). One target is 6.7 to 7.7 points.
- Only ARTEMIS is a live human comparison (n=10, one network). Humans were not given equal time per hour of agent scoring.
- Pass@k choices differ across papers; headline figures are not comparable.
- Physical red-team evidence is two leaked or press-level items (TSA, GAO). No controlled evidence that red teaming improves defence (b20).
- Model versions move fast; results from 2023-24 (GPT-4) are dated against 2026 scores.

## Only seen in snippets or not opened
a02, a07, b21, b22, b23 (not opened); b17, c06, c09 (numbers not extracted); c14 table garbled by PDF extraction; b11 had no headline number.

## GAPS
1. Does a separate adversary role (blue/red split) in one LLM agent beat self-critique at equal tokens, on tasks with a checkable ground truth? No source gives this controlled comparison.
2. When a plain strong model is tuned, how much of the scaffold gain (planner, sub-agents, memory) survives? Need same-model, equal-token, tuned-baseline comparisons beyond Dhakal et al.
3. Does extra prompt or documentation guidance ever help or hurt strong agents (c14, c26 point to hurt or no effect)? Find more replications.
4. What fraction of LLM red-team failures are context loss versus planning versus tool errors, with a consistent coding scheme across papers?
5. Do red-team findings reduce later defence failure (before and after retest)? Look for TSA/GAO follow-ups, DoD red team reports and any retest data.
6. How often do agents refuse, or report false positives, and how does this change the valid-finding rate per dollar? ARTEMIS is the only measure.
7. How well do agents detect decoys, traps and out-of-scope targets (honeypot paper is single-source)?
8. Are there LLM studies of purple-team or white-team (rules of engagement, scoping) functions, not only attackers?
9. What do pass@1 vs pass@k and cost per success look like for the same agents on one common benchmark with confidence intervals?
10. Is there physical-security red-team data beyond TSA and GAO (bank, facility, inspector tests) with exact counts?

## Gap search results
Tool limits this run: WebSearch budget ran out after one search; arXiv API, Semantic Scholar and OpenAlex all rate-limited. Sources came from arXiv abs/html/pdf pages and OIG. Evidence in evidence_d.jsonl (d01-d20); claims K18-K22 added, K16 upgraded to established, K02/K06/K07/K09/K15/K17 extended.

1. Red/blue role split vs self-critique at equal tokens: PARTLY CLOSED. No red-team-specific study exists. General results: self-critique without an outside check does not help (d01), debate loses to self-consistency at equal responses (d02), and debate is not reliably better (d03). Debate helps when the judge lacks the evidence (d04). The controlled test for our agent is still to be run (K18).
2. Scaffold gain vs tuned plain baseline: PARTLY CLOSED. Spread narrows with model strength (GPT-4o 27-39%, GPT-5 40-49%, d08) and gains in d09 were against weak baselines. Still no same-model equal-token tuned comparison beyond Dhakal et al.; the V2 vs plain-agent conflict stays open.
3. Does extra prompt or documentation hurt strong agents: OPEN. Found only a gain for a weak scaffold (tool docs 27% to 38%, d08). No new replication of the hurt or null effect.
4. Failure mix: PARTLY CLOSED. One coding scheme gives context forgetting 18%, planning modes 40%, tool errors 26% (d07). Single author group, 200 traces, not replicated across papers (K19).
5. Red team findings reduce later failure: OPEN. DHS OIG 2017 publishes no counts (d19). GAO still blocked. No retest data found.
6. Refusals and false positives per dollar: PARTLY CLOSED. Refusal rates 14.1% and 11.2% under a strict system prompt, about 0 otherwise (d12). False prune rate 2.8% in one search design (d08). No valid-finding-per-dollar figure beyond ARTEMIS.
7. Decoy, trap and scope detection: PARTLY CLOSED. Mantis and CAI hijack show agents fall for decoys and injected text (d13, d15). Out-of-scope detection is not measured anywhere found.
8. Purple/white team LLM studies: MOSTLY OPEN. Only indirect: patch task (d10), PenHeal remediation (abstract in K21), human-assisted AutoPenBench (d16). No scoping or rules-of-engagement study.
9. Common benchmark with CIs and cost: PARTLY CLOSED. BountyBench gives pass@3 with bootstrap CIs and cost per task (d10, d11); CVE-Bench 13% and CyberGym 20% against 67-92% on XBOW show benchmark choice dominates (d18). No single common benchmark across all agents.
10. Physical red-team data beyond TSA and GAO: OPEN. Only the 2012 Y-12 real intrusion (d20). NRC, GAO and a news source were blocked or missing.

Caveats: several d-lines (d04, d05, d06, d14, d15, d16, d17, d18) rest on abstract pages only. d02 row pairing for 9 responses is inferred from a garbled table.
