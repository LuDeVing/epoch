# Critique: Readings in model-based diagnosis (cross-check)

## Numbers re-opened (10 sources, text re-extracted this session)
1. Sztyber-Betley 2025 (DX 2025): confirmed 4o-mini incidence F1 0.47 +/-0.15, accuracy 0.00; o3-mini conflicts F1 0.917 +/-0.249, diagnoses 0.784 +/-0.322; 10 repeats; "$30 per iteration". OK.
2. Jha 2026 EoG (arXiv 2601.17915) Table: GPT-5.1 ReAct pass@3 F1 22.9 / maj@3 8.6; EoG 88.9 / 86.1; GPT-OSS ReAct maj 5.7, EoG 79.4; Kimi 28.6 vs 83.0; Gemini 3 Flash 74.3 vs 92.1; "7x average gain in Majority@k F1" in abstract. OK.
   CORRECTION: evidence a20 says Gemini 3 Flash is "89% Pass@k but only 51% consistently correct". The text says 89% Pass@k and 74% Majority@k. The 51% is a figure-1 caption number for a different measure; use 74%.
3. Wu 2023 (2308.15276): 23.13 is the mean Top-1 count (not a percent); 46.9% over SmartFL, 49.9% worse at class level, 25.6% loss without error log, 12.00% variance, 52.9% on StuDefects. OK (b19 wording "mean Top-1 of 23.13" is fine, but it is a count of bugs).
4. Tyen 2024 (2311.08516): GPT-4 52.87 overall is the middle (step-level) prompt column; 2186 traces; 255 of 300 (85%) per task are incorrect. Backtracking gains +18.04 to +43.92 with true location; random location +5.16 to +21.57, losses up to -15.91. OK.
5. Huang 2024 (2310.01798): GPT-3.5 CommonSenseQA 75.8 to 41.8, GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0, CSQA 82.0 to 80.0, HotpotQA 49.0 to 43.0; oracle rows 84.3/89.7/29.0 and 97.5/85.5/59.0. OK.
6. ITBench (2502.05352): gpt-4o diagnosis pass@1 13.81% in the main text/Table 4, but the appendix (Tables 19-20) says 18.10% with traces falling to 9.52% without. CORRECTION: c12 pairs 13.81 with 9.52, which mixes two tables. Mitigation 11.43% to 2.86% is consistent with the main table. Treat the trace-removal drop as 18.10 to 9.52 (appendix) and flag that the two tables disagree.
7. Kim 2026 OpenRCA (2602.09937): 1,675 runs, 3.9-12.5%, 71.2%, 63.9%, 39.9%, 18.6%, 27.2% confirmed. CORRECTION: c13 says code-generation error is "1.8% Gemini 2.5 Pro". Table 3 gives Gemini 2.5 Pro code-gen 40.0%; the 1.8% is its Timestamp Error. Claude Sonnet 4 code-gen 65.5% is right. Symptom-as-Cause Gemini 68.4% is right.
8. SAFARI (1401.3848): complete-method success rates (c432 CDA 74.1, HA 71.1; c1908 HA 6.1; c3540 HA 1.1; c6288 3.5; c7552 3.9) and SAFARI 100 everywhere confirmed. Each method has three variants in the table; the evidence lines quote the first variant only.
9. Reiter 1987 numbers (a02-a05, a24): not re-opened (OCR scan); taken from the first agent. Internal consistency check passes (full adder has 3 diagnoses; Davis device 4 diagnoses).
10. Gainer-Dewar and Vera-Licona, Jannach 2016, Ignatiev 2017, Plank and Wotawa 2026: not re-opened here; numbers rest on one reading each.

## Contradictions between sources
- ITBench 13.81 vs 18.10 (above). Different tables in one paper.
- b05 says conflict-score trend rises with complexity "only because of zero-conflict cases"; c03 reports the same. Consistent, but both from one paper.
- Cross-file ID drift: b06 cites "b23" for AutoFL, but b23 is Tyen. AutoFL is b21/b22/c19. b18 says the 2008 and 2010 SAFARI versions are a "replication"; it is the same group, not independent.
- b15 vs a09/a11: SAFARI success at 100% means "found a diagnosis", not "found the optimal one"; quality is separate (b16).
- Plank 2026 (c04) hallucination for Mistral 7B: 61.5% in a14 (not "over 70%"). The "most small models over 70%" statement is true of most, not all.

## Weak spots
- The book itself (Hamscher, Console, de Kleer 1992) was never opened. Its content is known through Reiter 1987 (opened), de Kleer-Williams via citations (a10, a11, c25), and later reviews. No numbers from the book are used.
- Only one paper (Sztyber-Betley) tests LLMs on real MBD objects, with OpenAI models, hand-made small circuits, o1 run once.
- Plank 2026: manual single-scorer, 3 runs, no frontier models. Phi-2 textbook-memory reading is untested.
- Most "LLM plus MBD engine" evidence (Dave, FLEX, FaultExplainer) is a demonstration or short-paper result without baselines.
- RCA failure rates in c13 were coded by an LLM; mitigation tests had 2 to 3 successes.
- TN-AutoRCA and HypoAgent gains are on tuned benchmarks; held-out generalisation not shown. HypoAgent figures not extracted (a23).
- EoG used 35 scenarios and domain code (~5,000 lines of Rust); input tokens higher than ReAct for 3 of 4 models (Gemini 3 Flash 3390K vs 5376K is lower). Equal-token comparisons are not made in the paper.
- Statuses: only claims with two or more independent groups are "established"; several lean on papers from related groups (Jha et al. EoG and ITBench share authors; Kang AutoSD and AutoFL share authors), so independence is generous in K10, K11, K12, K16, K18.

## Seen only in snippets or secondhand
Readings book (Semantic Scholar record only, 703 citations); Merkelbach 2024, FD-LLM, AAD-LLM, LLMAO, Qaid, Lukens (citation entries only); Greiner 1989 and Wotawa 2001 (via the Gainer-Dewar review); de Kleer-Williams 1987 (via Grastien and citations).

## GAPS (most decision-relevant first)
1. Does an LLM-proposed conflict set, mechanically checked, then hit by a vetted solver, beat free-form hypothesis listing at equal tokens on unfamiliar systems? (No published test found; arXiv API was rate-limited, so absence is not certain.)
2. Does the Sztyber-Betley result (conflicts F1 0.92, diagnoses 0.78 for o3-mini) hold for current non-OpenAI frontier models and larger circuits, and with the code tool for hitting sets?
3. Which probe-selection method (GDE entropy, minimum-cardinality split) can an LLM imitate, and does it pick discriminating tests better than a plain "what next?" prompt? Reiter's own result that naive divide-and-conquer fails because measurements add supersets needs a test.
4. Does a "candidate-exists" and "all-components-considered" code check remove the small-model hallucination (70%+) and the missed-double-fault failure (1 of 13 models)?
5. Does forced alternative-explanation (anti Symptom-as-Cause) work when it is a structural step rather than a prompt warning? (OpenRCA says prompt warnings failed.)
6. Do the EoG gains hold at equal total tokens, and which part (traversal, belief propagation, local labelling) is portable to a text-only reasoning task with no dependency graph?
7. What do Reiter 1987 and Greiner 1989 actually say about the HS-tree bug, and does an LLM-written hitting-set routine reproduce it? (Both original papers not independently read for this point.)
8. How well does the weak-fault versus strong-fault distinction (SAFARI, de Kleer-Williams) map onto reasoning problems where failure modes are unknown? Any LLM evidence on fault-model choice?
9. Is the AutoSD finding (real debugger output beats model-simulated output) replicated with current models, and what is the equal-token cost of real execution?
10. What is the true failure rate of intrinsic self-review with 2025-2026 reasoning models on diagnosis tasks (Huang 2024 used GPT-3.5/GPT-4 and 100-item HotpotQA)?


## Gap search results (d-file: evidence_d.jsonl, 17 lines; 13 opened lines including negative-result lines, 4 search-summary-only lines)

Search budget: 6 web searches used, plus OpenAlex, Semantic Scholar and arXiv API calls (arXiv and Semantic Scholar often returned empty or 429). Absence findings are therefore probable, not certain.

1. LLM-proposed conflicts then hitting-set solver vs free-form: STAYED OPEN. No paper found (d04). Still the cleanest experiment to run.
2. Sztyber-Betley on non-OpenAI models and larger circuits: STAYED OPEN. Only a related weak result: GEMMA-FD heat-pump detection macro-F1 0.252 vs 0.69 supervised (d05). Detection, not diagnosis.
3. Probe selection an LLM can imitate: PARTLY CLOSED. ACTMED (d11) shows a code-scored information-gain choice beats the model's own test choice on three tabular clinical datasets; SDBench (d09) shows structure improves cost-efficiency. The GDE-specific and circuit version is untested (d13). New claim K25.
4. Candidate-exists and all-components code check vs hallucination and missed double faults: STAYED OPEN. No new source.
5. Structural alternative-explanation step: PARTLY CLOSED. MAI-DxO uses a challenger and hypothesis tracker and shows gains in cost at equal accuracy (79.9% at $2,397 vs 78.6% at $7,850), but there is no per-role ablation (d09, d10). New claim K26 (single source, vendor).
6. EoG at equal tokens and portability: STAYED OPEN. No new source read.
7. Reiter 1987 and Greiner 1989 on the HS-tree bug: CLOSED. Greiner 1989 opened (d01, d02): pruning by edge removal plus closing rules loses paths, and a missing parent relabel can leave an unlabeled root; fixed by HS-DAG with a proof. K03 moves to established (2 papers, one correcting the other). Whether an LLM-written routine reproduces the bug is still untested.
8. Weak vs strong fault models and LLM fault-model choice: STAYED OPEN (d17). No LLM study found.
9. AutoSD replication with current models, equal-token cost of real execution: STAYED OPEN, with side evidence. AutoSD journal version 2025 exists (d16); a 93% token saving for execution-log-anchored localisation (d14); trained debugger imitators above 90% next-state accuracy (d15). New claim K28 single-source.
10. Intrinsic self-review in 2025-26 reasoning models: MOSTLY CLOSED for general tasks, OPEN for diagnosis. CorrectBench (d06) and Li 2026 (d07) agree with Huang 2024. New claim K27 (established, two sources; Li is a single-author preprint). Three further papers listed but not opened (d08).

Status changes: K03 single-source to established; K15 and K21, K24 got notes; K25 to K29 added (K29 records unsupported items).
Correction carried from this pass: the HS-DAG survey (arXiv 1601.02939) was seen only as a search summary and is not used for numbers.
