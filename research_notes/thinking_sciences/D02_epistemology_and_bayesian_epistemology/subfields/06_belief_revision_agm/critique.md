# D02.06 Belief revision (AGM): cross-check critique

## Re-opened sources (numbers checked against full text or abstract, 2026-10-26)
1. Belief-R (arXiv 2406.19764): confirmed. 1912 basic, 1074 BU, 670 BM, 1744 three-premise items. Rows confirmed from the appendix table: Llama-3 70B DP 10.99/92.09/51.54; Mixtral 8x22B DP 35.38/36.57/35.98; Claude-3 Sonnet DP 9.40/88.66/49.03; GPT-4 Turbo DP 19.65/82.69/51.17. The "garbled row" warnings in a16, b11, c02 can be dropped.
2. DeltaLogic (2604.02733): confirmed (Qwen3-1.7B n=30 0.667/0.467/inertia 0.600; Qwen3-4B n=20 0.650/0.450/0.600; Phi-4-mini n=20 0.950/0.850, inertia 0.200). The table text layout is shifted, so over-flip 0.100 and abstain 0.350 for Phi-4-mini remain plausible but not re-verified cell by cell.
3. Chowdhury (2609.37453): confirmed. Per-node judge 0.44, structured 1.00 (60/60), paraphrased 0.90 [0.86, 0.95] (140/150), keep-all 0.67 with 360 stale reuses, per-model rows 0.28/0.00/0.04 vs 1.00, pass rate 0.11 vs 0.52 with 41% fewer tool calls.
4. Hase et al. (2406.19354): confirmed table (pre-edit 0.90 edited, 0.97 downstream; post-edit 1.00 and 0.01; MAE downstream 0.34 to 0.59).
5. Huang et al. (2310.01798): confirmed oracle rows (GPT-3.5 75.9/84.3, 75.8/89.7, 26.0/29.0; GPT-4 95.5/97.5, 82.0/85.5, 49.0/59.0) and 74.7 GSM8K intrinsic.
6. Laban et al. (2311.08596): confirmed 46% flip and 17% mean drop in the abstract text.
7. Walsh and Johnson-Laird (2009): confirmed Exp 1 (17 of 20, p<.01), Exp 2 84%, Exp 3 91%, Exp 4 57% vs 21%, U=22.5.
8. Park Kumiho (2603.17244): confirmed 0.447 F1, 97.5% adversarial refusal, 49 scenarios, 7 postulates, 93.3% LoCoMo-Plus.
9. DERELAB (2608.30413): BiasGap 0.935 confirmed in figure text; GPT-5.1 row "891 OR" present. Other cells not re-derived.
10. Ríos-García et al. (2604.18805) and STALE (2605.06527): PDFs would not download intact; confirmed from the arXiv abstract only (41.4% vs 1.5%, 68%, 26%, 25,000 runs; STALE 400 scenarios, 1,200 queries, best 55.2%). Table cells (premise resistance, CUPMem 8.7 to 68.0) not re-checked.

## Corrections
- a22: author list "Mannan et al." is wrong. The paper is Ríos-García et al. (matches b23). Treat a22 and b23 as one source.
- a18 says "Mistral-7B-style, trained from scratch". The paper trains an 83M-parameter transformer using the Mistral-7B architecture scaled down (b15 is right). The results are for a toy model.
- c28 is not a source. Its url is the DeltaLogic paper and it is an editorial roll-up of other lines. Do not count it as independent evidence.
- a26 (FalsifyBench) was not opened; b24 did open it and carries the numbers. Use b24.
- Duplicate lines: Belief-R is a15/a16/a17/a27/b11/b12/c01/c02/c03 (one source); DeltaLogic is a21/b13/c04/c05 (one source); Hase editing is a18/a19/b15 (one); MEDLEY-BENCH is a25/b26/c21 (one); Singh Nous is a24/b28/c12 (one); Ríos-García is a22/b23 (one); Park is a23/c09 (one). Claims count these as one independent source each.
- Date: today is 2026-10-26, so 2026 arXiv ids up to 2610 are plausible; they resolved where tried. Ids 2606.22030, 2607.21558, 2610.* were not re-resolved.

## Contradictions and tensions
- Self-correction: Huang (no gain without oracle) and Kamoi agree. Tyen shows correction works once the error location is known, so the bottleneck is locating the faulty belief, not rewriting it. This is the S5 question exactly: which belief to drop.
- Belief-R says models under-revise (BU near 0 to 20%); Laban, Xie, MEDLEY and BeliefScope say models over-flip under pressure or follow social cues. Both are true: models fail on evidence-driven revision and succeed at pressure-driven revision. The remedy is a gate on evidence type, not "revise more".
- Ríos-García: scaffold explains 1.5% of variance. Chowdhury and Park show structure helps on their own benchmarks. These measure different things (variance share across many tasks vs targeted ablations by the authors); not a true contradiction.
- Humans: Walsh and Johnson-Laird reject minimal change; AGM and Hase's Bayesian gold standard assume it or probabilistic coherence. No LLM study tested whether LLMs mimic the human explanation-first pattern.

## Weak spots
- The founding AGM and Darwiche-Pearl works were read through secondary sources (SEP, Booth and Meyer, arXiv theory papers), not the 1985 and 1997 papers.
- No human replication of Walsh and Johnson-Laird outside one lab; Elio and Pelletier (1997) not opened (b10).
- Only one direct LLM test of AGM postulates (AGM-Bench), abstract only (b14).
- DeltaLogic uses n=20 to 30 episodes and 0.6B to 4B models; unusable as a ranking.
- Memory-framework papers (Park, Singh, Chowdhury, Chao CUPMem, MOIRA) are self-built benchmarks with self-reported scores, several single-author preprints, and none has an independent replication except Park's note of "mid-80s%" by benchmark authors.
- Most LLM results are 2024-2025 era models; frontier 2026 models appear only in DERELAB, STALE, FalsifyBench, MEDLEY.
- Many tests are zero-shot prompts without tools or executable checks, which is the setting least like our agent.

## Only seen in snippets or abstracts
b14 (AGM-Bench, abstract page), a26 (FalsifyBench abstract), b27 (Wang and Koch, first page), c14 (BeliefShift table cells unreadable), c20 (BeliefScope per-model effects), b10 (Elio and Pelletier, 403), Ríos-García and STALE (abstract only in this check).

## GAPS
1. Does a forced, evidence-gated Revise state (candidate list, ranked by provenance, drop the lowest-ranked contradicting claim) beat plain re-prompting at equal tokens on tasks with a planted defeater? No study tests this scaffold directly.
2. Which entrenchment signal works for an LLM agent: executed-output provenance, stated confidence, recency, or number of dependent claims? Singh shows confidence can be inverted; nothing compares signals head to head.
3. How does AGM-Bench actually score frontier models per postulate (Inclusion, Preservation, DP1-DP4)? Full paper and numbers are missing.
4. Does asking for an explanation of the failure before choosing what to drop (Walsh and Johnson-Laird) improve LLM revision, and does it replicate in humans outside the originating lab?
5. How far does error-location accuracy limit revision? Tyen shows oracle location gives +18 to +44 points; what location accuracy do execution traces (tests, stack traces) give a coding or ARC agent in practice?
6. Is the pressure-versus-evidence asymmetry (under-revise on defeaters, over-flip on bare challenges) stable for 2026 frontier models with tools, and can one gate fix both ends?
7. Does lexicographic (latest wins) or restrained (minimal move) iterated revision give less oscillation across repeated failed checks in an agent loop? Only theory exists.
8. Do the dependency-propagation gains (Chowdhury, Park) replicate on a free-running reasoning or coding agent, with a benchmark not written by the method's authors?
9. How often does revision at equal tokens cost more than it returns, i.e. what is the break-even versus simply restarting with the failed attempt summarised (Chowdhury: reset beat full history 0.52 vs 0.11)?
10. Which of the 2026 memory results (Kumiho, CUPMem, MOIRA, TOKI) hold under independent reproduction and unmodified benchmarks?

## Gap search results (evidence_d.jsonl d01-d22, claims K22-K28 added, K05/K10/K14/K16/K21 updated)
Search note: the web search quota ran out partway; the rest was done with arXiv listing queries, HTML renderings of papers and Crossref. Several PDFs were read only in part (first 100,000 characters), as noted in the evidence lines.

1. Evidence-gated Revise vs plain re-prompting at equal tokens: STILL OPEN. No study tests the staged scaffold. Nearest: Xu and Wu 2026 (d13), a one-sentence provenance rule moved 4.2% to 91.4% code-matching on 320 agent runs with tools, no equal-token arm. Claim K25.
2. Entrenchment signal head to head: PARTLY CLOSED, synthetic only. Singh (d01, d02): recency 67, frequency 46, wording-based confidence 100 (0 if inverted), provenance cap 0% poison success; cost 100% to 54% on true low-tier corrections. No free-running agent comparison and no "number of dependents" signal. Claim K27.
3. AGM-Bench per-postulate numbers: STILL OPEN. Abstract only again; OpenReview blocked (403) (d19).
4. Explanation before dropping: PARTLY CLOSED on the human side. Independent labs show the same non-minimal, rule-first pattern (Elio and Pelletier 1997, d16; Vasileiou et al. 2025, N=62/60/60, 83% non-minimal, d17), so K05 is now established. The causal role of explanation is still one lab (K22), and there is no LLM test.
5. Error-location limit: CLOSED enough to act on. Execution output gives large gains (Self-Debugging, d07), human diagnosis beats model self-diagnosis 52.6% vs 33.3% (d06), model-made hints hurt in 2 of 3 models (d08), step blame in long traces is 17.2% exact (d09). Claim K23. Not measured: location accuracy of stack traces on ARC-style tasks.
6. Pressure vs evidence asymmetry with 2026 models: PARTLY CLOSED. Training or steering fixes one end by damaging the other (d14, r=0.87 to 0.90 in d15, including four 2026 frontier models); a prompt-level evidence rule worked in agents with tools (d13). No test of one gate fixing both ends. Claim K24.
7. Lexicographic vs restrained oscillation: STILL OPEN as a comparison. New indirect evidence that failed loops often become fixed points (78.7 to 90.2% recurrence) and that a history reset helps escape but little at the end (d11, d12). Claim K26.
8. Independent replication of dependency propagation: STILL OPEN. Only related benchmarks (InterventionBench d20, abstract only; PARC d10; DeFA d09). Qian et al. 2026 (d22) audits 15 protocols and finds none covering stale-state handling.
9. Break-even of revise vs restart at equal tokens: STILL OPEN. Olausson (d05) gives 1.05x and 0.97x of resampling for self-repair; Jiang (d12) gives reset effects; neither compares a full revise state with a restart-with-summary at equal tokens.
10. Independent reproduction of 2026 memory results: STILL OPEN. None found. New caution: the LoCoMo judge issue (d03) and a conformance-only evaluation for typed provenance (d04). Claim K28.

Also found: the Ríos-García and STALE table cells remain unchecked; nothing new on them.
