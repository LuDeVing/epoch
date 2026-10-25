# Critique: Verification design (C01.04)

Cross-check done by re-opening PDFs (pdftotext) this session. Scratch copies are under the scratchpad folder xc_v04, not in the project.

## Numbers re-opened and confirmed

- Brown 2024 (Large Language Monkeys): 15.9% to 56% (SWE-bench Lite, 250 samples); coverage 82.9% to 98.44%; vote or reward model 40.50% to 41.41%; 11.3% flaky; 35 of 122 CodeContests problems; over 90% of 105 graded GSM8K chains faithful. All confirmed.
- Lightman 2023: 78.2 / 72.4 / 69.6 (best-of-1860); 63.8 / 72.9 / 61.3 on 234 OOD problems (from 224 questions); 2.6x active learning. Confirmed.
- Singhi 2025: "up to 8x" compute for GenRM to match SC; S_opt ~ C^0.57, V_opt ~ C^0.39; up to 30% relative on MATH level 5 (Llama-3.1-8B GenRM-FT, 32 verifications). Confirmed. Note the 30% is for the hardest level only.
- Huang 2023: 75.9 / 75.1 / 74.7; oracle 84.3; GPT-4 95.5 / 91.5 / 89.0; CSQA 75.8 / 38.1 / 41.8. Confirmed.
- Uesato 2022: 16.8 to 12.7 final-answer, 14.0 to 3.4 trace, 22.3 vs 23.5, 14.8 vs 16.6, 85% vs 77% agreement. Confirmed. The 3.4 and 12.7 are for SFT+PRM-RL with PRM reranking.
- Zheng 2023: 65.0 / 46.2 / 23.8 consistency; 91.3 / 91.3 / 8.7; 14/20, 6/20, 3/20; 85% vs 81%; 65.0 to 77.5. Confirmed.
- Zhang 2024 GenRM: 5 to 45.3, 73 to 93.4, 28 to 44.6, 37.9 to 53.5, 2.5x fewer solutions. Confirmed.
- ProcessBench: all F1 cells in a21 and b15 confirmed (Math-Shepherd 47.9/29.5/24.8; PRM800K model 68.2/62.6/50.7; GPT-4o 79.2/63.6/51.4; o1-mini 93.2/88.9/87.2; averages 87.9, 71.5, 61.9).
- Lessons paper: ProcessBench mean F1 28.9 / 40.1 / 46.5 / 56.5 and best-of-8 64.3 / 65.9 / 65.3 / 64.9; about 40% kept after consensus filtering. Confirmed.
- Cobbe 2021: 30x boost, peak at 400 completions then decline, 20.6% to 5.2% without intermediate steps. Confirmed.
- Snell 2024: "up to 4x less test-time compute", 14x larger model comparison. Confirmed in the text (not each sub-claim).
- Panickssery 2024: 73.5% and over 90% after 500 examples. Confirmed.

## Corrections made

1. a11: debate rows were given as 3 responses (round 1) and 9 responses (round 2). The PDF table (raw text mode) gives debate round 1 = 6 responses (83.2) and round 2 = 9 responses (83.0). b26 had it right on 6 and 9. The paper text says 3 agents, 2 rounds. Claim K15 uses the corrected values.
2. a12 (Stechly 2024): the table text is garbled and the Blocksworld row cannot be right. Counts show Blocksworld has 345 negatives and 155 positives. Accuracy 71.8% (359/500) means 141 errors. FPR 64/345 plus FNR 24/155 gives only 88 errors. So "FNR 15.48%" does not match the accuracy for that row. Rows for graph colouring (362/500, FPR 25/382, FNR 113/118) and Mystery Blocksworld (398/500, FPR 2/397, FNR 100/103) add up. Game of 24 adds up (3567/4100). Use only those three; drop Blocksworld.
3. a12 also said Mystery accuracy 79.6 and FPR 0.5%. That is consistent with 398/500 and 2/397. The appendix variant Mystery-CoT shows 79.0 / 1.3%. Keep 79.6 with the "main prompt" label.
4. a02: the line "12.4% vs 4.4% (ORM) and 3.5% (PRM)" mixes a few-shot final-answer-RL baseline (12.4) with SFT rows (4.4 ORM, 3.5 PRM reranking). The settings differ. The statement that RM reranking cuts trace error is right, but the 12.4 is not an SFT number.
5. a19 said "improves efficiency over best-of-N by more than 4x". The paper says "up to 4x less test-time compute" (for example 16 vs 64 generations). "Up to" is a ceiling, not a typical gain. Used the paper's wording in K16.
6. b17 and a21 both use 56.5 for the PRM800K-trained Qwen2.5-Math-7B on ProcessBench. It is the authors' own model, not the released PRM800K reward model of Lightman. Treat as one number from one training run.
7. a09 says optimal attempts "often below 10 (about 5 or fewer)". c07 says "about 3 or less (Fig 13)". b12 says "small K". These differ and were not re-checked (Stroebl PDF not downloaded). K03 states the direction only and gives the range.
8. c07 lists year 2026 (v3) for Stroebl while a09 and b11 use 2024. Same paper, later version. Findings may differ between versions; v1 numbers were not compared.
9. c11 says "Zhong et al." for ProcessBench; the author is Zheng et al. Citation fix only.

## Independence problem

Most evidence lines across the three files repeat the same 12 papers. The count of independent sources in the claims counts papers and groups, not lines. Cobbe, Brown, Stroebl, Snell, Lightman, Zheng, Huang appear in two or three files each. Stechly 2024 and Stechly 2023 are one group. This is why many claims are "single-source" despite many ids.

## Contradictions and tensions

- Process labels vs outcome labels. Lightman finds PRM > ORM, but also calls the final-answer false-positive problem "over-emphasised" on MATH. Uesato finds final-answer error equal for both. Lessons shows best-of-8 does not separate good from bad PRMs. These agree on the main point (answer-only checks hide trace errors) but disagree on how much it matters for selection accuracy.
- Learned verifier vs vote. Lightman: PRM beats majority by 3 to 11 points at best-of-100 to best-of-1860. Brown: vote and reward model both plateau near 100 samples. Math-Shepherd (a04): self-consistency + verifier 92.5 on GSM8K is below verifier alone 93.3. Singhi: SC wins at most budgets. Not a clean contradiction; the settings differ (verifier type, N, model).
- GenRM claim vs compute cost. Zhang reports big gains vs discriminative RMs. Singhi, charging for verifier tokens, finds SC cheaper until about 8x compute. Both are right under their own accounting.
- Self-preference. Panickssery finds a causal-looking link to self-recognition. Wataoka (c17) says familiarity (low perplexity) drives it. The two are not tested head to head.
- Snell found the PRM800K-trained PRM easy to exploit with best-of-N on PaLM 2 and used its own PRM. Lightman's PRM800K gains were with a GPT-4 base. A released PRM may not transfer across generators.

## Weak spots

- Almost all numbers are math (GSM8K, MATH) or code (HumanEval, SWE-bench). No evidence on open-ended, planning-with-constraints, or non-numeric tasks except Stechly (few domains, 100 instances each) and judge studies on chat.
- Judge-bias numbers are from 2023 models (GPT-4, Claude-v1, GPT-3.5). Sample sizes: 23 answers, 20 trials, 10 math questions, 80 questions.
- Huang 2023 and Stechly are pre-reasoning-model. No evidence here on whether modern RL-trained reasoners self-verify better.
- Gao 2022 is a synthetic gold model setup. It supports the shape of overoptimisation, not the size on real tasks.
- No source tests a training-free scaffold with a verifier step at equal tokens against voting. Singhi comes closest, with fine-tuned verifiers.
- Reward hacking in RL verifiable rewards is nearly uncovered (c27 unread).

## Only seen in snippets, abstracts or not opened

- c25 Math-Shepherd (opened:false in c; a04 has numbers but "Table 1" cells were not re-checked here).
- c26 Weaver: not read.
- c27 Pitfalls of rule- and model-based verifiers: not read.
- c13 ThinkPRM: abstract and intro numbers only.
- c17 Wataoka: effect sizes not extracted.
- c12 Free Process Rewards: abstract-level.
- c15 Wang (fair evaluators), c19 Stechly 2023, c20 Tyen, c23 Setlur, c24 IFEval, a22 V-STaR, a23 CodeT, a24 survey: not re-opened by the cross-checker.
- b27 is a synthesis written by an agent (opened:false), not a source.
- a15 numbers come from figure captions, not tables.

## GAPS

1. At equal tokens, does a training-free "k short check chains plus code vote" verifier beat plain self-consistency for a scaffold agent, and at what N and difficulty does it cross? (Only fine-tuned verifiers were tested; Singhi says SC wins below about 8x compute.)
2. What is the false-negative and false-positive rate of a prompted verifier from a current reasoning model (not GPT-4 in 2023) on reasoning tasks outside math and code, such as constraint puzzles or planning? Do Stechly's 95%+ false-negative rates still hold?
3. Do modern RL-trained reasoning models self-correct or self-verify without external feedback? Huang 2023 results are from GPT-3.5 and GPT-4. Any 2025-2026 replication?
4. How correlated are errors between a model's solution and its own generated tests or checks (CodeT-style), and does a different model family as checker cut that correlation? What is the measured number?
5. How should the number of tries be capped given a measured checker false-positive rate? Stroebl's fitted K ranges from about 3 to under 10 depending on the cost ratio. Is there an empirical rule?
6. Is there a published head-to-head of self-preference (self-recognition) versus perplexity familiarity in judges, with effect sizes, on correctness tasks rather than summaries and dialogue?
7. How much does step-level checking add over answer-level checking on tasks that are not math, where right-answer-wrong-reasoning may be rarer or more common? Lightman and Uesato both say the effect may be dataset specific.
8. What do the unread papers (Weaver weak-verifier ensembles, Pitfalls of rule- and model-based verifiers, Setlur) show on ensembling weak checks and on reward hacking of model verifiers? Do ensembles of diverse checks cut correlated error?
9. Can difficulty be estimated cheaply enough (for example from agreement across 3 to 4 pilot samples) that routing between voting, beam search and verification still beats uniform allocation, as Snell's predicted-difficulty results shrink?
10. Does a judge with a reference answer from independent samples (not its own earlier output) keep the 14/20 to 3/20 improvement at larger N than 20 trials, and with current judge models?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d28, all opened this session as PDF or HTML text). WebSearch ran out of budget partway; the rest was done through the arXiv API and direct PDF downloads. Claims K03, K05, K06, K07, K08, K13, K14, K16, K17 were updated and K22 to K31 added.

| Gap | Status | What the new evidence says |
|---|---|---|
| 1. Training-free verify-then-vote vs self-consistency at equal tokens | Partly closed | Zhao 2025 (d01): Gemini 1.5 Pro with 50 checks per candidate beat Consistency@1000 on AIME (8/15 vs 3/15) and LiveBench Reasoning (97 vs 73 of 140), but cost about 130M tokens per AIME question, and tie-breaking gave most of the gain on MATH (457/500 without it, below Cons@200 at 460). SETS (d03): best-of-N with self-verification beat majority vote by 10.7 points on Trip Planning and 6.9 on Meeting Planning, and lost on AIME (28.3 vs 32.2). No paper tests a true equal-token cross-over curve with a code vote over short check chains. |
| 2. Prompted verifier error rates outside math and code | Partly closed | Plan checking is good for Claude-3.5 and Gemini-1.5: error recall 91.85 and 94.04, precision 93.74 and 97.51 on Trip Planning (d04). On math, 7 to 23 percent error each way with 20 averaged checks (d02). o1-preview failed to flag impossible goals 73 to 84 percent of the time (d15). Stechly's 95%+ false-negative rate was not replicated with a current model and no constraint-puzzle measurement was found. K06 is now contested. |
| 3. RL-trained reasoning models self-correct without feedback? | Partly closed | No for small and mid models: spontaneous shifts in 6.31% of traces and mildly harmful (d11); 85 to 95% of rechecks in Qwen3-8B confirm only (d13); prompting-only correction on Qwen2.5-Math-7B 71.6 to 70.4 (d12). A triggered second look under high entropy gives +8.41 points (d11). Frontier-size reasoning models (o-series, full R1) remain untested. |
| 4. Error correlation between solution and own tests | Mostly closed | Writing tests after seeing faulty code: 14% fault detection vs 25% independently; seeing the implementation costs 13.2% on average across five models; CoT and chain-of-verification do not fix it (d18). Different model for tests: no difference in Elixir (d19). The measure is fault detection, not a correlation coefficient. Shared context matters more than shared model on current evidence. |
| 5. Resample cap from checker false-positive rate | Partly closed | Stroebl re-opened (d20): K about 5 at cost ratio 4, K = 0 at ratio 10, rate of false positives rises with K because remaining tasks are the hard ones. No closed-form rule in the paper; the marginal rule (continue while P(right) x benefit > P(false pass) x cost) is my reading of their model. Two model families (Code Llama, Command) had much higher optimal K with no explanation. |
| 6. Self-recognition vs perplexity as cause of judge self-preference | Closed (direction) | Pombal 2026 (d16): on LiveCodeBench ratio 1.88 when recognised vs 0.72 when not; ratio 1.48 remains in the lowest-perplexity quartile. Recognition is the stronger correlate; observational only. K14 moved from contested to established. |
| 7. Step-level vs answer-level outside math | Still open | VersaPRM (d21): math PRMs add at most +0.71 over voting outside math; a multi-domain PRM adds more (Law +7.9%). That shows step-level scorers do not transfer, not that step checks add over answer checks outside math. No clean comparison found. |
| 8. Weaver, Pitfalls, Setlur; do diverse checks cut correlated error? | Partly closed | Weaver (d05, d06): weighted ensemble 87.7 vs vote 72.2 and naive top-10 ensemble 69.1; needs a small labelled dev set; flattens from correlated bias on hard items; mean pairwise score correlation about 0.03 but not measured on hard items. Pitfalls (d07, d08): rule recall 86%, static accuracy did not predict hackability, generative verifiers more fooled. Setlur (d28): theory and training results only. Nitarach (d23): voting errors are not positively correlated; prompt diversity hurt. |
| 9. Cheap difficulty routing | Partly closed | Pilot agreement saves 33 to 65 percent of calls at equal vote accuracy on a 3B model, n of 30 to 50 (d24), and up to 75 percent on GPQA against the infinite-budget vote (d25). Routing between vote, search and verify by this signal has not been tested; Snell's predicted-difficulty shrinkage is still the only test of that. |
| 10. Independently sampled reference answer for judges | Still open | No paper found that tests a sampled reference at more than 20 trials or with a current judge. Related: a labeler without gold answer or step definitions agreed only 7% with its own correct labels (d22); reference-based judges reach 89 to 96% in chemistry and biology but are weaker in math (d26). |

### New cautions from this pass

- Weaver (d05) contradicts itself in the headline gap (13.5, 12.3 and 15.5 points in different places) and Table 3 does not match Table 1. Use the Table 1 averages only with care.
- Zhao 2025 labels its error columns the wrong way round (FPR defined as correct marked incorrect). Treat the names as unreliable.
- SETS Table 2 and Pitfalls Table 4 were scrambled in pdftotext; only cells that matched the surrounding text were used.
- d25 (PETS) targets agreement with the voting limit, not truth. d24 (TrACE) has n of 30 to 50 and a 3B model.
- d27 (V1) and d28 (Setlur) were read at abstract, introduction and heading level only.
- The scratch PDFs are under the scratchpad folder d, not in the project.
