# Critique: software, spreadsheet, KB debugging (C09.10)

## Re-checks (cross-checker, 2026-11-10)
Re-opened arXiv abstract pages this session:
- Agentless (2407.01489): 32.00%, 96 fixes, $0.70 on SWE-bench Lite. CONFIRMED (b14). The 4.3 / 10.0 / 5.0% audit split is not in the abstract; not re-verified.
- Who&When (2505.00212): 127 systems, 53.5% agent, 14.2% step. CONFIRMED (b22).
- AutoFL (2308.05487): 798 bugs, up to 233.3% acc@1. CONFIRMED (b08, c14). b08 and c14 are the SAME paper; count as one source. b09, b10 also AutoFL.
- SpreadsheetBench (2406.14991): 912 real questions. CONFIRMED (b19). Per-model percentages not re-verified.
- Huang et al. (2310.01798): abstract confirms self-correction fails without external feedback and can degrade. Table numbers (b15) not re-verified.
- Olausson et al. (2306.09896): abstract confirms gains modest, feedback is bottleneck, stronger or human feedback helps. 52.60 vs 33.30 not re-verified.
Not re-verified (rate limits, no PDF read): Jannach & Schmitz N=24 results (b01), Rodler user studies (a06-a08), SpreadsheetBench 2 numbers (a23, c10), DRAGO (c01-c03), SemLoc (c12-c13). Treat as one-read numbers.

## Corrections / dedup
- Duplicate entries: a21/c05 (FoRepBench), a22/c06, a23/c10, b08/c14, b12/b11, b23/b24/b22 (Who&When). They are not independent confirmations. Claims count them once.
- a17, c24 both point at Jannach & Schmitz 2016; a17 is blocked (opened true but no numbers). b01 is the only source for the human spreadsheet result.
- b25, b26 (Parnin & Orso 2011; Pearson 2017) are from memory, opened:false. Not used in claims.
- Dates: a06 is listed 2019/2022; cite as the 2022 journal version after checking.

## Contradictions and tensions
- Self-correction: b15 says it hurts; b16, b17, b18 say it helps with external feedback; c03 shows self-review 159 fixes vs 254 breaks. Consistent once "external signal" is the split, but b17 (explanations, no tests) gains only 1-3 points on Spider.
- b11: ChatGPT +46.9% at function level but -49.9% at class level versus SmartFL. Gain depends on granularity and on the error log (-25.6% without it).
- b13 AgentFL Top-1 157 vs c15 LLM4FL 326 of 675: different benchmarks (395 vs 675 faults); not comparable.
- c07 Gemini 2.5 Pro 12/12 detection vs c08 Triangle sheet most models score 0: detection of seeded errors is not repair of tangled ones.
- a23 (12% debugging) vs c20 (up to 89.7% on KB validation): different task shape (end-to-end sheet with 600 cells vs small constraint sets).

## Weak spots
- The central human evidence (Jannach 2016) is one sheet, 16 cells, one fault, 24 students.
- Most KB-debugging results use simulated oracles and injected faults (a01, a02, a04). Real-user study (a06) shows oracle errors and overconfidence.
- LLM-for-MBD proper (an LLM running the hitting-set loop) has almost no direct study; evidence is adjacent (DRAGO, SemLoc, ORLoopBench).
- 2026 results (c01, c12, c17, c18, c20) are preprints, single-lab, not replicated.
- Snippet-only or skimmed: b05, b27, a19, a20, a25-a27, c25.

## GAPS
1. Does an LLM that proposes ranked fault candidates and picks the next probe by expected information beat free-form debugging at equal tokens, on real (not injected) faults?
2. How often does an LLM oracle or the agent's own check give a wrong answer, and how much does a 10-25% wrong-answer rate hurt entropy-based probing versus robust (re-ask) strategies?
3. Why do right-to-wrong regressions occur in revision, and which gate (test, solver, second model) removes them at the lowest token cost?
4. Does Jannach and Schmitz spreadsheet result replicate with more sheets, more fault types, and practicing spreadsheet users (not students)?
5. What is the real LLM performance on spreadsheet debugging for error-value cases (#REF!, #NUM!), and which tool-use pattern (formula tracing, dependency graph) lifts it?
6. Is verification-based confidence (counterfactual checks) better than self-consistency for deciding when to re-open S5, and what does it cost?
7. Can fragment or block-level localization (coarse then fine) be reproduced by an LLM, and does it cut tokens versus cell-level search?
8. How does long-context failure attribution (Who&When step-level 14.2%) improve with chunked search or bisection?
9. Do the best-first and sampling findings (a11) matter when candidates are LLM-generated, not hitting-set-derived?
10. Does keeping multiple faults (double-fault cases) in play break single-fault assumptions in LLM repair loops?

## Gap search results (gap searcher, 2026-11-10)
Constraint: WebSearch budget was exhausted by other agents, and arXiv, Semantic Scholar, OpenAlex and dblp all returned 429 or access denied. Work was done from arXiv abstract pages and three full PDFs (Who&When, Agentless, UoT, BED-LLM). Evidence in evidence_d.jsonl (d01-d23).

- Gap 1 (EIG probing vs free-form on real faults): PARTLY CLOSED. UoT (+38.1% relative) and BED-LLM (+37.4 points) show EIG-based question choice beats direct prompting, but only on toy tasks with simulated answerers; no equal-token test on real faults. Still open for real bugs (claim K19).
- Gap 2 (wrong oracle answers): STAYED OPEN. Adjacent only: BED-LLM says entropy fails with noisy answers; only 94 of 213 LLM reproduction tests verified a correct fix (d13). No measured 10-25% noise sweep (K23).
- Gap 3 (revision regressions, cheapest gate): MOSTLY CLOSED. Agentless: voting 77, +regression tests 81, +reproduction tests 96 (cost $0.25); DRAGO solver gate 1.3% vs 11.8% regressions. The model's own tests are unreliable, so use a regression gate first (K20).
- Gap 4 (Jannach replication): STAYED OPEN. Nothing found.
- Gap 5 (spreadsheet error-value cases, tool patterns): STAYED OPEN. FLAME and SpreadsheetBench abstracts give nothing on #REF!/#NUM! or tracing tools (K25).
- Gap 6 (verification vs self-consistency): PARTLY CLOSED. Verbalized confidence is overconfident (Xiong 2024); TRACE shows confidence separates right from wrong poorly for 6 of 7 models; A2P counterfactual step lifts step accuracy 2.4-2.9x. No head-to-head cost comparison with self-consistency on debugging.
- Gap 7 (coarse-to-fine by an LLM): CLOSED for code. Agentless hierarchy beats direct line localization; skeleton 58.33% at $0.02 vs full file 53.67% at $0.15 (K21). Not tested on spreadsheet cells.
- Gap 8 (long-log attribution, bisection): CLOSED. Bisection does not help step accuracy (6.90 vs 4.39 all-at-once, at 2x tokens); the agent-then-step hybrid gives 12.28% at about 9x tokens; scaffolds (A2P 47.46% / 29.31%) do better (K13).
- Gap 9 (best-first and sampling with LLM candidates): PARTLY CLOSED by BED-LLM, where asking the LLM to rank candidate probes still beat plain prompting; not tested with hitting-set best-first as in a11.
- Gap 10 (double faults): STAYED OPEN. EDGE gives qualitative multi-error gains; no repair-loop test (K26).

Caveats: most new items are abstract-level reads (d03-d08, d14-d23); d08 is snippet-only (opened:false). Who&When and A2P share one small benchmark.
