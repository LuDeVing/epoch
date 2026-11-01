# Critique: C01.03 Test-time compute scaling (cross-check)

## Numbers re-opened (PDF text re-read this session)
Confirmed exactly: Brown 2024 (0.02% with one sample and over 300x coverage gain (the 7.1% endpoint was not re-checked); 15.9% to 56% vs SOTA 43%; MATH 82.9% to 98.44%, voting/RM ~40.5 to 41.4); Snell 2024 (4x less compute; 14x larger model; Fig 1 labels +27.8, +21.6, -37.2, -52.9); s1 (50% to 57% AIME24; up to 27% over o1-preview); Chen 2024 (1,953% more tokens; 48.6% cut on MATH500; SimPO alone 22.3%; first round 287 tokens = 38.7% of response on ASDIV; "over 92%" first round correct); Hassid 2025 (34.5% vs longest, 18.8% vs random, 40% fewer tokens, 33% wall time); Yue 2025 (base beats RLVR at large k); Liu 2025 abstract (1B beats 405B, 0.5B beats GPT-4o, 3B beats 405B); Ma 2025 (51.3 vs 28.9 on AMC23 at 700 tokens; 9x); Wu 2025 "Does thinking more" (up to 20% over extended thinking; GSM-8K, MATH-500, AIME 2024).

## Corrections and cautions
1. c06 says Llemma-7B + REBASE matches 34B at "about 2x fewer FLOPs". The paper text found says "7 times less compute" for REBASE vs sampling weighted voting with the 7B model (Tab. 1). No "2x" statement was found. Treat c06's 2x as unverified; use the 7x vs sampling statement.
2. a25 (22.3%) and b17/c10 (48.6%) are different methods: 22.3% is SimPO alone; 48.6% is the full pipeline. Not a conflict, but must not be quoted interchangeably.
3. a07 phrase "over 300x" refers to coverage increase; the 7.1% at 10,000 comes from the same abstract line; consistent.
4. a17 / b06 ablation cells came from garbled PDF tables; only the 1K-random 36.7 value is trusted.
5. b12 percentages are read from figure labels, not a table; bin mapping not verified.
6. Evidence duplicates: the b and c files repeat a-file papers (Snell, Brown, Wu, s1, Hassid, Chen, Zeng). Claim "independent_sources" counts distinct papers, not lines.

## Contradictions between sources
- Sequential vs parallel: s1 (sequential beats majority vote, but different base models) vs Wu 2025 and Zeng 2025 (parallel beats extended thinking). Snell: depends on difficulty. Unresolved.
- Snell's difficulty-bin recipe vs Liu 2025: best search method flips with model size and PRM.
- Illusion of Thinking vs Lawsen: collapse may be an output-limit artefact; Lawsen is a preliminary comment.
- Brown (coverage rises to 98%) vs Chen et al. and Stroebl (selection stalls or falls). Not a contradiction: coverage is not accuracy.

## Weak spots
- Most strong results are math (MATH, AIME, GSM8K) and code with checkable answers. Open-ended, tool-using, or agent tasks are nearly absent.
- Snell's 4x is one model family (PaLM 2-S*), one benchmark, with a finetuned PRM and oracle-style difficulty bins; the model-predicted-difficulty version has smaller gains.
- Liu's headline comparisons are author-reported with a strong PRM; no independent replication found.
- Token cost is mostly counted as samples or FLOPs; few papers compare at equal total tokens including verifier cost.
- Little evidence on closed frontier models with built-in thinking and budget parameters beyond Gema 2025.
- Surveys (a30, b19, c09, c21): abstract and front matter only; no numbers.

## Seen only in snippets or partially
a27 and c11/c25 (Zeng): abstract and intro, per-benchmark numbers not pulled. b25 crossover budgets not extracted. b26 numbers not extracted. c13, c19, c20, c22 not re-opened by the cross-checker; taken from the finder's reading.

## GAPS
1. At equal total tokens (including verifier and thinking tokens), does extended thinking or k parallel short chains win on a frontier thinking model, by difficulty bin? (Resolves the s1 vs Wu/Zeng conflict.)
2. How well can difficulty be predicted cheaply (few samples, confidence, question features) for an S0 gate, and how much of Snell's 4x survives with predicted rather than oracle difficulty?
3. What false-positive rate do realistic verifiers (self-verification, unit tests, LLM judge) have on non-math tasks, and where is the cost-optimal N?
4. Do test-time scaling gains transfer to agentic, tool-using and open-ended tasks, or only to checkable math and code?
5. Is the three-regime result (low, medium, high complexity) robust once output limits and impossible instances are fixed, and does it give a usable routing rule?
6. What stop rules (consistency-based early exit, short-m@k, confidence exit) give the best accuracy per token across models, and do they combine?
7. Does independent replication exist for small-model-beats-large claims (Liu 2025) with a weaker, non-oracle PRM?
8. Inverse scaling (Gema 2025): which of the five failure modes appear in our scaffold, and does a budget cap or distractor filter remove them?
9. How much does sleep-time or cached precomputation help when the same context serves many questions (relevant to memory)?

## Gap search results
Evidence in `evidence_d.jsonl` (d01 to d18, all opened as PDF text). Web search quota ran out partway; search APIs (arXiv, Semantic Scholar, OpenAlex) also returned nothing, so papers were found from memory plus one search that surfaced d02. Claims K03, K04, K05, K07, K09, K11, K12, K13, K19, K20 updated; K21 to K27 added.

1. Equal tokens, extended vs parallel, frontier model, by difficulty: STILL OPEN. New data makes the conflict sharper (d01 parallel +22% at 16K on small distilled models; d02 sequential refinement wins 43 of 45 matched cells on open instruct models) but "sequential" means different things in each, and d02 caps every chain at 4096 tokens. Nobody splits by difficulty on a frontier thinking model.
2. Cheap difficulty prediction: MOSTLY CLOSED. Learned predictors keep a real part of the saving: up to 50% on math/code, 0-10% on chat, 25-50% fewer calls for routing (d03); self-predicted "restart helps" token gets 74% of a 16-sample gain with 1.2 samples (d04, needs fine-tuning). Snell's 4x is not reproduced with predicted difficulty; the oracle curve stays higher. Exact retained fraction is not given in a table.
3. Realistic verifier false-positive rates and optimal N: PARTLY CLOSED. GPT-4 self-verifier: Game of 24 false positive 10.4%, false negatives up to 97% elsewhere (d06); self-correction hurts (d18). Weak-verifier ensembles help (d07). SWE tests saturate at 42-43% (d08). No paper gives a cost-optimal N for non-math tasks; keep the K04 cap.
4. Agentic, tool-using, open-ended: PARTLY CLOSED. Gains exist but are moderate: GAIA +7 points from whole-trajectory best-of-N (d09), SWE-bench 34.4% to 51% with hybrid verifiers (d08), non-math puzzles only when checkable (d10). Truly open-ended tasks remain unmeasured; chat saving was near zero (d03).
5. Three-regime robustness: PARTLY CLOSED, still contested. Authors add controls and River Crossing N=3 (11 moves) still fails (d11); Lawsen shows impossible instances and output caps explain part (d12). No independent re-run with fixed limits found. Usable as a hypothesis for routing, not a rule.
6. Stop rules: PARTLY CLOSED. Each rule works alone (d13 up to 84.7% tokens, d14 19-80%, d15 over 40% on NQ). Combination and cross-model comparison untested (K25 open).
7. Replication of Liu 2025 with weak PRM: STILL OPEN. None found (K27). Weaver (d07) is related, not a replication.
8. Inverse-scaling failure modes in our scaffold: STILL OPEN as to our scaffold; literature side done (d16). Few-shot fixes spurious-feature drift; budget cap and distractor filter untested by the authors.
9. Sleep-time or cached compute: CLOSED enough for design. About 5x at equal accuracy, 2.5x per query at 10 questions per context, little or negative with 2 questions or unpredictable queries, plain test-time wins at high budgets (d17). Still single-paper from one group (K19 stays single-source).

Cross-check notes: the c06 "2x" is marked unverified in K07. The 22.3% and 48.6% Chen figures are separate methods. The 7.1% Brown endpoint was not re-checked. Table-layout caveats: d06 Table 2 rows and d07 baseline rows were garbled in text extraction and are flagged in those lines.
