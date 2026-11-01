# F02.03 Cognitive offloading: cross-check critique

Checker re-opened sources this session (PDF or HTML text): PAL (2211.10435), Toolformer (2302.04761), Chain of Code (2312.04474), Kosmyna (2506.08872), Dziri (2305.18654), Hesselmann (PMC7651475), Grinschgl (PMC8358584), Tool-Induced Myopia (arXiv 2511.10899, abstract page).

## Corrections made
1. Toolformer table (a20, b20 wrong; c05 right). The text extraction is garbled. Correct rows, ASDiv/SVAMP/MAWPS: GPT-J 7.5/5.2/9.9; Toolformer with API calls disabled 9.6/5.0/9.3; Toolformer 40.4/29.4/44.0; OPT-66B 6.0/4.9/7.9; GPT-3 175B 14.0/10.0/19.8. The triple 14.8/6.3/15.0 is the GPT-J + CC (finetuned without API calls) row, not Toolformer-disabled and not Toolformer. a20 wrongly says "GPT-J + tools disabled 14.8/6.3/15.0"; b20 wrongly gives Toolformer as 14.8/6.3/15.0. Text confirms 97.9% calculator use and "more than doubles" (9.6 to 40.4).
2. PAL comparison (a18, b16, c01). 72.0 vs 56.9 (+15) compares Codex-PAL with PaLM-540B CoT, so model and method both change. Same-model comparison: Codex CoT 65.6, so +6.4. Minerva-540B CoT is 58.8. The GSM-HARD result (PAL 61.5, Codex CoT 20.1, direct 5.0; confirmed) is the cleaner evidence. The table text is garbled, but the numbers 72.0, 56.9, 61.5, 20.1, 19.7 to 5.0 are confirmed.
3. Tool-Induced Myopia (c10-c13): the paper is arXiv 2511.10899 (Nov 2025 first submission), not 2026. The abstract says TIM in about 55% of high-risk cases (evidence says 54.3%, consistent). Title of record: "From Proof to Program: Characterizing Tool-Induced Reasoning Hallucinations in LLMs". Dose-response bins and DPO numbers (c11, c12) were not re-checked.
4. a15: authors missing; keep as "Let it go" 2026.
5. Confirmed unchanged: Dziri 55% / 59% on 3-digit multiplication; Chain of Code 84% (+12 over CoT) and 91% with GPT-4; Kosmyna 15/18 (83.3%) vs 2/18 (11.1%); Hesselmann RTs 830/901 ms easy, 825/821 ms hard, 73% (57/78) would look up; Grinschgl Exp 1 numbers (3.61 vs 2.31 openings, 49.33 vs 55.06 s, 5.91 vs 7.07 bindings, 10.55 vs 10.93 identity).

## Contradictions between sources
- Offloading and memory: Grinschgl (worse memory) vs Storm & Stone (saving improves later memory). Resolved partly by learning goal and trust, but not tested in one design.
- Photo-taking: impairment in person, benefit online (b08); Exp1 interaction did not replicate in Exp2.
- Tool use: PAL, PoT, Toolformer show large accuracy gains; Tool-Induced Myopia shows the final answer improves while reasoning gets worse. Not contradictory but two different metrics.
- Metacognitive feedback: Ngai & Gilbert find a small effect; Engeler & Gilbert and Grinschgl find none or a null on offloading itself.
- Google-effects: original significant, two failed replications; yet people still say they would look up answers (73%).

## Weak spots
- Founding works (Salomon 1997, Risko & Gilbert 2016, Kirsh & Maglio 1994, Salomon et al. 1991, Dunn & Risko 2016) were never opened; only definitions seen. Numbers for the "founding studies" are therefore from Gilbert-lab studies, not Salomon.
- Burnett & Richmond 2026 meta-analysis (a08): abstract only; no effect sizes. It is the key quantitative claim for "forced beats chosen".
- No LLM paper tests offloading of state or counts in a long agent loop (the closest are MemGPT, a self-reported benchmark, and Illusion of Thinking, disputed).
- Almost all LLM evidence is arithmetic or math; little on counting, list-keeping or state across turns at equal tokens.
- Kosmyna: N=54, preprint, EEG not read; b22/b23 (Liu 2026, Zhu 2026) are single studies, not checked here.
- Independent-source counts for human work overstate independence: Gilbert lab wrote a02-a05, b01, b02, b14 (one lab).
- OccamLLM (c07), ToRA (c09), OTC-PO (c14), MemGPT (c15) were not re-opened.

## Only seen in snippets or secondhand
a01, a04, a07, a08, a10, a11, a13, a16, a17, a24, a26; b07, b10, b11, b24; c19-c25 (all unopened).

## GAPS
1. Does a program-forced code store (counters, lists, running totals) beat a model-chosen store at equal tokens in multi-turn agent runs? No direct LLM test found.
2. How large is the same-model effect (not cross-model) of code offloading on frontier 2025-2026 models, whose arithmetic is already good? PAL-era numbers are from Codex.
3. Does Tool-Induced Myopia hold when the code only holds state and counts, not solution steps? Needs the dose-response and mitigation numbers checked.
4. Burnett & Richmond 2026: what are the effect sizes, k, and the forced vs chosen difference? Needed to size the human analogue.
5. Does clearing content from model context after writing it to a store help later steps (saving-enhanced memory analogue), or hurt (Grinschgl)? Test with and without an explicit re-read step.
6. What did Salomon (1997) and Salomon, Perkins & Globerson (1991) actually report (effects with vs of a tool), and is there any measurable "effect of" in LLM scaffolds when the scaffold is removed (Florean 2026 removal cost)?
7. How do tool-call budgets and over-calling (OTC-PO, Qian 2025) trade accuracy against tokens for a frozen API model with prompt-only control?
8. Are models more reliable at following an instructed offloading strategy than inventing one (Boldt & Gilbert: instructed 90.5% vs spontaneous 86.0%, p=.06)? Check LLM tool-use studies for the same comparison.
9. Is a stale or corrupted store a real failure mode for agents (a15, b12 analogue)? Look for LLM studies that corrupt memory and measure detection.
10. Do the Illusion of Thinking results survive the token-limit critique when the algorithm is executed by code rather than text?

## Gap search results (evidence_d.jsonl d01-d20, claims K23-K30)

Search limits: WebSearch quota was used up, OpenAlex and Semantic Scholar rate-limited, arXiv API empty; work was done by opening arXiv PDFs and Europe PMC records directly.

1. Forced code store vs model-chosen store at equal tokens: OPEN. No direct LLM test. Nearest: Chen 2025 (d10) forced code vs chosen code for solution code (chosen wins for 2 of 3 models). MEM1, MemAct (d18, d19) are model-chosen and trained.
2. Same-model effect on frontier models: PARTLY CLOSED. Tool-Induced Myopia Table 2 (d05): o4-mini +19.3, GPT-4.1 +2.4, GPT-4.1-mini -1.3. Hard competition math, not arithmetic only. CodeAct (d12) gives older-model same-model numbers. No 2026 frontier test of pure counting/state tasks.
3. TIM when code only holds state: OPEN. Dose-response (d06) is on solution code; bins by call count, per-bin values are in a figure only. Mitigation (d07): prompt-only costs 1.9 of 2.4 accuracy points; DPO is single-model. Numbers c11/c12 now re-checked against the paper: 54.3% audit, 99.8%/73.7% tool use rates, win rate 45.6 to 52.7.
4. Burnett & Richmond 2026: OPEN for numbers. Abstract confirms forced > choice and within > between designs (d01). No effect sizes, k or gap found; paper is paywalled.
5. Clearing after writing: PARTLY. Vendor figure (d17): context editing +29%, with memory tool +39%, 84% fewer tokens (no N). Human side: store loss hurts (d02), freed capacity not always reused (d03). No controlled LLM test with vs without re-read.
6. Salomon 1991/1997: OPEN. SAGE 403, ERIC no record. No LLM study of scaffold removal found.
7. Call budgets on frozen API: OPEN. OTC-PO (68.3% fewer calls, comparable accuracy) and SMART (24% less tool use, about one-fifth the calls on GSM8K) are trained (d08, d09). Only prompt-only datum is d07. Table cells for OTC were garbled; only abstract numbers trusted.
8. Instructed vs invented: PARTLY. Chen 2025 (d11): GPT-4o skips code in the medium range it should use it; no controlled instructed-vs-spontaneous contrast with a p value. Thinking models use code far more often (d06).
9. Stale or corrupted store: PARTLY CLOSED. Real failure mode: MINJA 98.2% injection, 76.8% attack success (d15); error propagation (d16). No measure of the agent detecting corruption by itself.
10. Illusion of Thinking with code: PARTLY. Lawsen (d14) reports a Lua generator for 15 disks works on four frontier models, unquantified and preliminary. Original paper gave the algorithm in text only (d13).

Status changes: K18 gets the per-model spread; K19, K21, K20, K07, K15, K02 gain evidence ids. New claims K23-K30. Remaining open: 1, 3, 4 (numbers), 6, 7 (prompt-only), and the detection half of 9.
