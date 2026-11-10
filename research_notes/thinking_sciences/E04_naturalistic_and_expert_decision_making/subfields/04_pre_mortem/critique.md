# Critique: E04.04 Pre-mortem (cross-check)

## Sources re-opened this session (PDF text read)
1. InvThink (arXiv 2510.01569): 3.22 zero-shot, 2.62 SafetyPrompt, 2.19 InvThink, 32.0 percent lower; PROTHINK control 1.01 vs 1.23 harmfulness, same 23,063 targets. CONFIRMED.
2. BTF-2 (arXiv 2604.26106): Brier SOTA 0.119, Opus 4.6 0.130, cost $1.68 vs $0.55, 24 of 130 expert-flagged, Pre/Post-mortem 37.8 percent vs 12.1 and 10.8. CONFIRMED. CORRECTION: the Brier table uses N = 1367 (a05/a25 imply 1,417); 1,417 is the question set before timing exclusions.
3. Huang et al. (arXiv 2310.01798): GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CommonSenseQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0. CONFIRMED. CORRECTION: the table columns are "# calls" (1, 3, 5), not rounds; c13's "round 1/round 2" wording should read calls 3 and 5.
4. Wang et al. 2024 (arXiv 2405.16334): 23.5 vs 22.7 vs 19.8 percent, plan revisions 0.64 vs 1.16, 3.5 points, 45 percent. CONFIRMED.
5. Reflexion (arXiv 2303.11366): 91 vs 80 HumanEval, +22, +20, +8 abstract numbers. CONFIRMED.
6. PreFlect (arXiv 2602.07187): 58.18, 59.39, 38.46 Level 3 present. PARTIAL. The pdftotext table layout is scrambled. In the GAIA table I read ReAct+Reflexion 46.06 total and Smolagents plain 49.70, whereas a20 labels 46.06 as Smolagents and 49.70 as Reflexion. Row labels in a20 may be swapped; baseline totals should be treated as 46 to 50 until checked against the HTML. Also the leaderboard rows suggest 58.18 may be paired with the Gemini-2.5-pro backbone, not GPT-4.1. Backbone assignment UNRESOLVED. Level-3 baseline 19.23 confirmed; a21's "23.08" for the ablated Level 3 also appears in table.
7. Veinott 2010 numbers: could not re-open (Semantic Scholar 429, OpenAlex gave no abstract). NOT verified.

## Contradictions between sources
- a02/b02 (30 percent more reasons) vs a01/b01 (abstract: temporal perspective had little influence; certainty was the active factor). The popular claim of a time-shift effect rests on secondhand reports. Treated as contested (K01).
- a06 says "about 25 points more than baseline" confidence fall (unverified); b04 says "about twice that of pros/cons or cons-only". Both secondhand; unreconciled.
- a20 baseline labels vs PreFlect table layout (above).
- Reasoning in a15 (Posavac 2008: temporal frame effect vanishes when certainty primed) supports the certainty explanation, but only a snippet was read.

## Weak spots
- The human evidence base is tiny: Veinott (N=178 students), Gallop (N=101), Peabody (N=52/72/82 thesis), none preregistered, none with real plan outcomes. Klein 2007 cites only Mitchell 1989.
- Veinott, Gallop, Mitchell full text, Koriat, Hoch were never opened (opened:false): numbers there are all secondary.
- LLM evidence has no true premortem prompt test at equal tokens. InvThink's own control shows direction may not matter. BTF-2 is correlational. PreFlect and Wang bundle many components; "pre/post-mortem" in BTF-2 includes post-mortem.
- Model-based self-critique result (Huang) is the strongest negative boundary: ungated self-critique can hurt.
- Single-run, small benchmarks (GAIA validation about 165 tasks, so one task is about 0.6 points) make 8-point gaps fragile.

## Seen only in snippets or search summaries
a02, a06, a07, a09, a10, a15, b04, b08, b09, b13, b18, b19, b20.

## GAPS
1. Does the failure frame ("it has failed") beat a matched "it may fail, list reasons against" prompt on LLM accuracy and calibration at equal tokens? No study crosses these (K01, K06).
2. What do the Veinott 2010 means, SDs and effect sizes actually show, and did premortem change plan quality or only confidence?
3. Can premortem be gated by a cheap signal (task complexity, low self-consistency, tool disagreement) so it only fires when it helps, given Peabody's complexity moderator and Huang's ungated-harm result?
4. Does a premortem step with an external check (tool, test, retrieval) avoid the self-critique accuracy drop, versus a purely internal one?
5. Does listing failure causes overshoot the agent's stated failure probability (Hill's subadditivity) and cost accuracy through over-refusal or over-hedging (InvThink FRR 0.361)?
6. Is the BTF-2 Pre/Post-mortem association causal? Ablate it in the forecaster and compare Brier at equal cost.
7. Do stored post-mortem lessons (Reflexion, PreFlect error prior) beat imagined premortem failures, and do they combine?
8. Are there any 2025-2026 LLM studies that prompt a literal premortem on planning or coding tasks with measured results (missed by arXiv title search; try full-text and agent-planning venues)?
9. Do group or individual formats matter (Elizabeth 2020 SJDM poster, Veinott)? For a single agent, does multiple independent failure samples then pooling beat one pass?

## Gap search results (evidence_d.jsonl, d01-d17; claims K18-K24 added)

Tools: arXiv, Semantic Scholar and OpenAlex APIs were rate-limited; web search budget was spent. Work was done by reading full PDFs of arXiv papers and arXiv search pages.

- Gap 1 (failure frame vs reasons-against, equal tokens): OPEN. No study crosses them. InvThink's matched forward-vs-failure control (d10) and Devil's Advocate (d12, bundled) give no support for the frame itself.
- Gap 2 (Veinott 2010 numbers): OPEN. Paper not reachable (404/403/rate limits). Klein's blog gives only N = 178 and "greatest reduction in overconfidence" (d13). Outcome is confidence, not plan quality.
- Gap 3 (cheap trigger): PARTLY CLOSED on mechanism. Sample agreement (Adaptive-Consistency 3.3x fewer samples, <0.1% loss, d06), P(True) (d07), Peabody complexity (d17). No premortem-specific gated test. PreFlect flags 74% of plans risky (d01), so an ungated check is nearly always on.
- Gap 4 (external check): CLOSED as to direction. Tool-backed critique gains (CRITIC +6 to +10 F1 on QA) while internal-only gives 0 to +3 or losses; Huang and Kamoi agree (d02-d04). Not tested for a premortem step specifically (K19).
- Gap 5 (overshoot, over-refusal): OPEN. No LLM measure of failure-probability inflation. InvThink FRR 0.361 only on safety tasks (d10, d16).
- Gap 6 (BTF-2 causality): OPEN, and weaker. Authors say causal isolation is hard; rationale format and 3x cost are confounds (d11).
- Gap 7 (stored lessons vs imagined): PARTLY CLOSED. PreFlect's error prior is worth 7.88 of 12.12 points (d01); ExpeL and CoMem show stored or retrieved lessons help and stack (d08, d09). No head-to-head with a plain imagined-failure prompt.
- Gap 8 (2025-26 literal premortem LLM studies): CLOSED as "none found" across arXiv all-field searches, Crossref, Europe PMC (d14). Nearest are trained or bundled methods (K22).
- Gap 9 (pooling failure samples): OPEN. Pooling answers works (self-consistency +17.9 on GSM8K, d05) but pooling failure lists is untested.

Corrections resolved: PreFlect 58.18 is the GPT-4.1 backbone, baseline Smolagents 46.06; 49.70 is HF-ODR with o1, not a Reflexion row (d01). Table row labels for Reflexion/Self-Refine GAIA totals stay unread because pdftotext scrambled that table. Status change: K14 (BTF-2) set to contested.
