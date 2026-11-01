# Critique: Algorithmic MDL (C11.07), cross-check

Method: ten sources re-opened this session from arXiv full text or the blog page (Deletang 2309.10668, Huang 2404.09937, Wang Hypothesis Search 2309.05660, Akyurek 2411.07279, Li 2411.02272, Ellis DreamCoder 2006.08381, Grand LILO 2310.19791, Yoran Kolmogorov Test 2503.13992, Liao and Gu CompressARC blog). Rule: confirmed means the number appears in the text I read.

## Confirmed without change
- Deletang: ImageNet 43.4% vs PNG 58.5%, LibriSpeech 16.4% vs FLAC 30.3% (abstract); enwik9 raw 8.3 / 8.9 / 32.3 / 23.0 (Chinchilla 70B, Llama 2 7B, gzip, LZMA2).
- Huang: 31 LLMs, 12 benchmarks, overall Pearson -0.93, RMSE 3.1%, -0.95 per domain, DS-1000 -0.946, corpus saturates at about 3M characters, limits (base models only, short to medium context, well-trained LMs only).
- Hypothesis Search: 17 / 23 / 30 / 33 / 45 (human-written), 33 of 49 (67%), 94.3% SyGuS, exactly one task where a fit program failed the test.
- Akyurek: 80-task subset 17.5 to 45.0; 47.1 own model, 53.0 BARC model, 61.9 ensemble; BBH 50.5 to 57.8.
- Li: 56.75 (TTT, no reranking, Potpourri), 60.2 average human, 97.8 best human, p<.004, small-compute ensemble 26.50 / 18.78 / 15.25.
- DreamCoder: 3.7 to 79.6, 235 s to 40 s, CVC4 82.4, DreamCoder 84.3, mean 54.1 s median 15.0 s, 93% physics after 8 cycles.
- LILO: all deltas in c13 and c14 match; 48 CPU-hours per round.
- Kolmogorov Test: 78%/40%, 99% / 93.5% / 88.7% errors in first 16 characters, over 95% repetition on natural data, CoT -1.3 / -5.1 / +2.1, table cells for Llama and GPT-4o.
- CompressARC: 34.75% train, 20% eval, about 20 min per puzzle on RTX 4070, pass@1 30.25% (train) and 18.5% (eval) at 2000 iterations.

## Corrections made (or required) to the evidence files
1. Huang, individual benchmarks: the three knowledge numbers are HellaSwag -0.881, TriviaQA -0.951, MMLU -0.890. The -0.930 in a20 is the Appendix E textbook-compression variant for MMLU, not the main result. b04 says "about -0.91 to -0.95" for single benchmarks; the true range includes -0.881. Use the exact values in claim K04.
2. b10 mislabels Li's table: 43.0% is "transduction, reranking, no TTT" (Potpourri), not "reranked TTT". TTT without reranking is 56.75%. Also ARC-Heavy: ensemble with TTT is 38.00% and transduction with TTT is 43.25%, so the ensemble is worse than the best single method there. b10/b11 imply the ensemble always helps; it does not.
3. b16 says "human-written hypotheses 47.5% vs 37.5% direct". In the paper the 40-question appendix table is direct 12.5, program only 17.5, summarised 27.5, human-selected 37.5. The 37.5% that 47.5% is compared with is "program generation from hypotheses without Parsel", not direct prompting. The Parsel gain (47.5%) holds only for human-written hypotheses; for LLM hypotheses it hurt.
4. a26 says "without programs GPT-4 dropped to 19%". Correct, but this is a chain-of-thought ablation (intermediate language, no program execution); c11 labels 23% as "program only". Both are fine; do not read 19% as a new condition.
5. Kolmogorov Test synthetic failure rate is internally inconsistent: abstract says 66% and 45%, section 5.1 says "more than 65% and 55%". Also "78% and 40%" is an average over modalities with high variance; GPT-4o accuracy on audio-16bit is 35.6% at length 128, so its failure is about 64% there. Do not quote 40% as a per-modality number.
6. Deletang tables: the extracted table text is garbled. b02's "Chinchilla 1B adjusted 194.0 / 146.6 / 195.5" cannot be matched to columns with confidence (those figures appear in the raw columns of the extraction). Only the abstract figures and the enwik9 raw column are safe. Treat "adjusted rate above 100%" as the authors' qualitative claim, not as table cells.
7. c16 says Akyurek ensemble 61.9% appears in Li's comparison table; confirmed. Note the 61.9% uses the BARC models (Li et al.), so Akyurek and Li are not fully independent for this number. K12 counts 2 sources, not 3.
8. a13 and c10: "no baseline solves over 60%" in LOGO/tower domains is from the paper's text; fine.

## Contradictions and tensions between sources
- Model-cost accounting: Deletang says large pretrained models do not compress once parameters are counted (offline), while Blier and Ollivier say prequential coding makes deep nets compress strongly. Both are right for different code types; this is why K03 is "contested".
- Fit-implies-correct: Wang found one exception in a small subset; Li found about 9% of fitting samples are false positives (largely under 20k-sample pools); our own data had two. Selection effect from sample count explains much of it. K11 is "contested".
- Elmoznino says prequential ICL favours simplicity (trained models); the one pretrained LLM tested on Mastermind did not benefit (c20). No second LLM was tested.
- Compression predicts benchmark score (Huang) but Kolmogorov Test shows these same LLMs cannot write short programs for data. Predicting well is not the same as writing a short explicit program.
- Ellis c15: English hypotheses beat Python for fitting humans, while Wang, Li and ARC Prize all find Python execution the useful route for correctness. Different goals (human fit vs task accuracy), not a real conflict.

## Weak spots
- Many "established" claims rest on one paper family (DreamCoder and LILO share a lab and a library idea; Li, Akyurek and ARC Prize 2024 share BARC models and the ARC benchmark).
- ARC results are on small subsets (80 and 100 tasks, 40 in an appendix) with one model; confidence intervals not given.
- No study here tests a pure prompting scaffold with a code-length selector at equal tokens. The link from algorithmic MDL to our agent is by analogy (S2 representation, S7 select).
- CompressARC numbers are from the author's blog, not a peer-reviewed table; the 20% eval figure is on the public evaluation set.
- Voita and Titov, Elmoznino, Blier and Ollivier, Valle-Perez, Mingard were not re-opened in this pass.

## Seen only in snippets or not opened
- Lake, Salakhutdinov and Tenenbaum 2015: PDF gave HTTP 403; error numbers (3.3% vs 4.5%) are from memory. Do not cite.
- Feldman 2000, Chater and Vitanyi 2003, Rissanen 1978, Gruenwald 2007: memory only.
- ARC Prize 2024 technical report: numbers in b13/c23 were read by earlier agents; I did not re-open them. Greenblatt 43% and ARChitects 53.5% are therefore single-pass.
- Hutter AIXI, Schmidhuber OOPS, Rathmanner and Hutter: read by agent A only.
- Wikipedia articles: read through a fetch summary; background only.
- No ARC Prize 2025 results, no 2025-2026 reasoning-model results on Kolmogorov Test or on compression-based selection were checked; the evidence stops at about March 2025 for LLM studies.

## GAPS
1. Does choosing the shortest consistent rule (code length, with a fixed language) beat choosing by vote or by first-fit among programs that all pass the examples, at equal tokens, on ARC-style or rule-induction tasks? No paper tests this; it is the core S7 question.
2. How often does a program that fits all given examples fail a held-out or mutated input in frontier models of 2025-2026, as a function of the number of samples? (Wang: 1 exception; Li: about 9% false positives.)
3. Do 2025-2026 reasoning models (o3 class, Claude and Gemini thinking models) pass the Kolmogorov Test any better than Llama-3.1-405B and GPT-4o, and do they still just repeat the input?
4. Does an LLM's in-context loss behave like prequential code length across rule families (Elmoznino tested one LLM on one puzzle)? If not, a length-based selector computed from model log-probs is unsafe.
5. Does storing compressed, named helpers (LILO-style) in agent memory help at equal tokens when no weights are updated and tasks share only some subroutines? What is the break-even task count?
6. What does a per-rule cost term (rule length penalty) do to selection when the model proposes rules in free English versus Python? Is there a language-invariance failure (Grunwald's arbitrariness defect) in practice?
7. How much of the induction-versus-transduction complementarity survives without test-time training, i.e. in a prompt-only agent with a router (program first, direct answer as fallback)? Li's own ARC-Heavy numbers show the ensemble can lose to transduction alone.
8. Are the Lake et al. 2015 and Feldman 2000 human-simplicity results replicated, and do human error patterns on Boolean concept difficulty match LLM error patterns?
9. Do later results (ARC Prize 2025, CompressARC follow-ups) show whether pure MDL at test time scales, or only helps on puzzles with simple repeated structure?
10. Does the compression-benchmark line (Huang) hold for fine-tuned and reasoning models, or only base models? This decides whether likelihood can serve as a cheap quality proxy for our agent.


## Gap search results (evidence_d.jsonl, d01-d18)

Search limits: WebSearch hit its shared session budget after one query. The arXiv API, Semantic Scholar and OpenAlex all returned 429 or empty. I used direct arXiv PDF downloads of papers I could name, Europe PMC, and WebFetch. This means the search was narrow: papers I could not name were not found. A fresh pass with working search is needed for gaps 1, 4, 6, 7.

Correction: claim K21 had the Lake 2015 numbers attached to the wrong groups. Lake 2019 (d15) says BPL 3.3% error and humans 4.5%. K21 is fixed.

Closed or mostly closed
- Gap 9 (ARC Prize 2025, MDL at test time): closed enough. CompressARC is 20% on ARC-AGI-1 and 4% on ARC-AGI-2, 76K parameters, about 20 min per puzzle (d02). 2025 winners were test-time-trained models, NVARC 24.03% (d01). TRM at 7M parameters is not MDL and reaches 44.6 / 7.8 (d03). Pure MDL is shown to work on simple puzzles and not shown to scale. New claim K23.

Partly answered
- Gap 2 (fit but fail held-out): indirect only. EvalPlus (d07) gives 12.6-18.5% drops at pass@1 and up to 28.9% at pass@100; CodeContests+ (d08) shows verifier quality depends on test count. No 2025-2026 measurement on rule induction. Claim K25 added; K11 note extended. Still open for ARC-style tasks.
- Gap 3 (reasoning models on Kolmogorov Test): one data point, o1-mini 57.2 vs GPT-4o 56.5 Accuracy (d13). No o3, Claude or Gemini thinking models found. ARC-AGI-2 (d04) shows o3 at 3.0%. Open for 2025-2026 models.
- Gap 5 (helper memory): mixed. ReGAL (d12) gains 8-26 points with no weight updates; "Library Learning Doesn't" (d11) finds reuse near zero in two systems. No equal-token test, no break-even count. K28 marked contested.
- Gap 8: Lake 2015 numbers confirmed second-hand (d15); Feldman 2000 and Planton 2021 abstracts read (d16, d17). No replication study and no LLM-vs-human error comparison found. Feldman's data was not opened beyond the abstract.
- Gap 4 (LM loss vs code length): no new test of Elmoznino. One relevant warning from Coder-Reviewer (d10): model log-prob ranks programs with a length bias. K27 added. Open.

Stayed open
- Gap 1 (shortest consistent vs vote or first-fit at equal tokens): still no paper. Best baselines are SOAR weighted vote with a 9.5-point gap to oracle (d05) and CodeT agreement (d09, +18.8 points on HumanEval). This is still the core S7 experiment and must be run by us.
- Gap 6 (English vs Python rule language): nothing new. Feldman's review (d18) names the fit-versus-simplicity trade-off only.
- Gap 7 (prompt-only router): SOAR (d06) again relies on fine-tuning. Nothing without test-time training found.
- Gap 10 (Huang line for fine-tuned and reasoning models): Huang says base models only (d14). Open; do not use likelihood as a proxy for instruct models. K30.

Still unopened: Lake 2015 (HTTP 403), Feldman 2000 full text, ARC Prize 2024 report, Poetiq's own write-up.
