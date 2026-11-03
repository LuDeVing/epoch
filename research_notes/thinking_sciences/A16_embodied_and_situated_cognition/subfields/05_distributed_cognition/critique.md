# Critique: A16.05 Distributed cognition (cross-check)

## Re-opened sources (full PDF text, this session)
Du 2023 (arXiv 2305.14325), Huang 2024 (2310.01798), Yang SWE-agent 2024 (2405.15793), Zhang 2025 Stop Overvaluing MAD (2502.08788), Cemri 2025 MAST (2503.13657), Li Agent Forest (2402.05120), Kim 2026 scaling (2512.08296), Kosmyna 2025 (2506.08872). PDFs deleted after extraction.

## Confirmed
- Du: arithmetic 67.0/72.1/69.0/81.8, GSM8K 77.0/75.0/81.0/85.0, chess 91.4/102.1/102.2/122.9 (single/reflection/majority/debate; 3 agents, 2 rounds). Matches a19, b17, c05.
- Huang: GPT-3.5 GSM8K 75.9 to 75.1 to 74.7; CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle 97.5. Matches b18.
- Zhang MAD: 36 settings; SoM, EoT, ChatEval, AgentVerse beat CoT in about 15%; Heter-SoM +6.4%, Heter-EoT +8.2%, up to 5.8% over CoT-average. Matches a21, b15, c08, c09.
- MAST: kappa 0.88 and 0.77; 41% to 86.7%; 41.8/36.9/21.3; +9.4% role fix; +15.6% verifier; ChatDev 86.7% failure. Matches a23, b12, c10, c11.
- Agent Forest: GSM8K +12 to +24, MATH +6 to +10, Llama2-13B 59% vs 70B 54%. Matches a20, b19.
- Kim scaling: 260 configurations, +80.8% to -70.0%, ceiling beta=-0.236 p=0.004 (single-agent above about 45%), error amplification 17.2 independent vs 4.4 centralized (these are trace-based error-amplification factors). Matches a24, b14.
- Kosmyna: 54 participants, 18 per group, 83.3% (15/18) of the LLM group failed to quote vs 11.1% (2/18) in the other groups. Matches c21, b06.

## Corrections
1. c19 (SWE-agent): evidence says Shell-only 7.3% and +10.7 points. Wrong. In Table 1, Shell-only with GPT-4 Turbo on SWE-bench Lite is 11.00%; 7.33% is the SWE-agent run without demonstration. The correct gap is 18.00 vs 11.00 = +7.0 points, which is the paper's 64% relative increase. The claim K11 uses the corrected figure. Full SWE-bench 12.47% (286/2294) and Lite 18.00% (54/300) are right. Claude 3 Opus: 10.46% full, 13.00% Lite (c19 says 10.5 only).
2. c19 HumanEvalFix: evidence says 87.7 pass@1; the paper text says 88.3% (the table gives per-language scores, so 87.7 may be one language). Use 88.3 as the text figure; unresolved.
3. b13 and c11 both call the +15.6% a ProgramDev gain from a verifier; confirmed in the MAST text, but the +9.4% refers to ChatDev with a better role prompt. Do not merge them.
4. a21 and b15 say "no method wins more than 20%"; the paper text also says the four named methods win in about 15%. Both hold; they are not different results.
5. a24/b14/a23/b12/c10/a19/b17/c05 are duplicate evidence of the same papers. Independent source counts in claims.jsonl count papers, not lines.

## Not re-opened (carried as read by the earlier agents, not checked by me)
Zhang & Norman 1994 numbers (a08-a11), Kirsh & Maglio 1994 timings (a12, a13, b07), Camerer 2018 p-values (b01), Harris 2011 (a17), Fansher 2020 (a18, b08), Ngai & Gilbert 2026 (b03, b04), Zhu 2026 (b05), Park 2023 (c03), MATM (c16), Hong 2023 (c12; table layout garbled). The Kirsh & Maglio 800-1200 ms mental figure is a pilot estimate from three players, not a main result.

## Seen only in snippets or not read
- Wegner, Erber, Raymond 1991 (a16): snippet only, N=118 unchecked.
- Hutchins 1995 Cognition in the Wild (a14): not read; only SEP summary.
- Sparrow 2011 (b02): not opened. Risko & Gilbert 2016 (b25): 403. Hollan 2000 (b24): not read in depth.
- Smit 2024 (a22, b16): no per-method numbers extracted.
- Wu 2026 LLMA-Mem (a27): no exact numbers.

## Contradictions between sources
- Debate: Du 2023 shows large gains; Zhang 2025 and Smit 2024 show no reliable gain under matched compute. Du compared against single sample, reflection and majority at unspecified token cost; Zhang matched cost against self-consistency. The disagreement is mainly about the baseline.
- Heterogeneity: Zhang 2025 says mixing models is the fix; Self-MoA (b20) says mixing lowers average quality and one strong model sampled repeatedly wins.
- CoThinker (a25/b22/c18) reports big gains on high-load tasks but a pooled loss of 3.8% on one task group, and weak results on small models.
- Kim 2026: multi-agent hurts sequential planning by 39-70% while helping decomposable finance by up to 80.8%; this fits "task structure decides" and contradicts a blanket "more agents is better" (Agent Forest).

## Weak spots
- The human DC literature (Hutchins) has no effect sizes and no LLM paper tests it. Everything the agent can use is a design analogy.
- Most human experiments are small (N=12 to 36 per cell); the Google effect already failed to replicate.
- Many LLM results mix model generations (ChatGPT 2023 to GPT-5 2026) and token budgets are rarely matched.
- Offloading harm results (Kosmyna N=54, preprint; Lee 2025 survey self-report) are weak causal evidence.

## GAPS
1. Does a debate or critic operator beat self-consistency at equal tokens on current frontier models, with an external verifier present?
2. Does a redundant second representation (Hutchins-style cross-check) catch injected errors in an LLM agent more than a single self-check?
3. How much of SWE-agent-type interface gain (+7 points) holds for current models and for non-code tasks (observation format, windowed view, linter feedback)?
4. What is the break-even for decomposing a task across agents: which task features (sequential vs parallel) predict the sign in Kim's +80.8% to -70.0% range, and can it be predicted before running?
5. Does predict-then-check before tool calls (the Ngai & Gilbert intervention) reduce over-use of tools and retrieval in an LLM agent without losing accuracy?
6. Do epistemic actions (cheap probes, running a test) beat deliberation at equal tokens, and what is the LLM analogue of the Tetris 100 ms vs 800+ ms gap?
7. Does shared trajectory memory (MATM) transfer to our tasks, and does gated retrieval beat always-retrieve?
8. Does the Sparrow location-memory result replicate, and does an agent that stores where to find facts instead of facts lose or gain accuracy?
9. Does heterogeneous mixing (different models) help or hurt versus best-single-model resampling, with token budgets matched?
10. What are the exact HumanEvalFix and Zhang & Norman numbers if re-opened (unresolved discrepancy in correction 2)?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d18, all opened this session as full PDF text or page text). Web search and the Semantic Scholar, OpenAlex and arXiv search APIs were rate-limited or out of budget, so papers were fetched by known arXiv id only; no new papers were discovered by search.

1. Debate vs self-consistency at equal tokens: PARTLY CLOSED. Choi 2025 (d01, d02), Smit 2024 (d03) and Zhang 2025 (d04) agree: voting equals or beats debate on small and mid models (Qwen2.5-7B average 0.7691 vote vs 0.7377 best debate vs 0.7205 single). Still open: frontier reasoning models, and debate with an external verifier present.
2. Redundant second representation catches injected errors: STILL OPEN as a direct test. Indirect support: same-model error finding is weak (Tyen d05, GPT-4 52.87), true-location repair is strong (d06), tool critique beats tool-free (CRITIC d07).
3. SWE-agent interface gain for current models and non-code tasks: PARTLY CLOSED. Ablation numbers extracted (d08, d09). A README claims a bash-only agent above 74% on Verified (d10), which suggests the gain has shrunk, but it is not a controlled test and non-code tasks are untested.
4. Break-even for decomposition: PARTLY CLOSED. Kim 2026 (d11, d12) gives the 45% single-agent threshold and the decomposable-vs-sequential split, and 87% held-out choice accuracy, but its predictors need runs; a pure pre-run predictor is not shown.
5. Predict-then-check before tool calls: STILL OPEN. Only tool over-use itself is measured (SMART, d15); prompt-level predict-then-check has no LLM test.
6. Epistemic actions vs deliberation at equal tokens: STILL OPEN. ReAct (d18) shows probes ground reasoning but does not match tokens.
7. MATM transfer and gated vs always-retrieve: PARTLY CLOSED. Relevance matters (same task type > cross type, d13). Gating beats always-retrieve in Mallen 2023 (d14) with an external gate on large models; no LLM-agent test with a self-judged gate.
8. Sparrow location-memory replication: STILL OPEN. No source found or opened this run.
9. Heterogeneous mixing vs best-single resampling: PARTLY CLOSED, leaning toward resampling the best model (Self-MoA d16: 65.7 vs 59.1; quality weight larger than diversity). AgentNet (d17) is mixed and small (N=100). Token-matched frontier test still missing.
10. HumanEvalFix and Zhang & Norman numbers: HumanEvalFix CLOSED (Python 87.7, JS 89.7, Java 87.9; text 88.3 is an unstated aggregation, d09). Zhang & Norman 1994 numbers STILL NOT RE-OPENED.

New claims K20-K24 added; K05, K06, K08, K10, K11, K12, K16 extended; K10 kept single-source; K20 marked established (three independent papers).
