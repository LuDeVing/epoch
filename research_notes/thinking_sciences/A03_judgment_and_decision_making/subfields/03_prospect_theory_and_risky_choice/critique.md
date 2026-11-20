# Critique: A03.03 Prospect theory and risky choice (cross-check)

## Re-opened sources and results (13 checks)
Confirmed against the source text this session:
1. K&T 1979 (MIT PDF): Problem 1 82% (N=72), Problem 2 83% (N=72), Problems 3/4 80% and 65% (N=95), 3' 92%, 7/8 86% and 73% (N=66), Problem 10 78% of 141, Problem 14 72% and 14' 83% (N=72), Problem 13/13' 82% (N=68) and 70% (N=64). All correct.
2. Brown et al. (OSF PDF): 607 estimates, 150 articles, mean lambda 1.955 CrI [1.820, 2.105]; M1 1.809 [1.740, 1.878]; bias-corrected 1.742 [1.674, 1.811]; 15.5% variance explained; Tversky and Kahneman 1992 used 25 graduate students, median 2.25, alpha=beta=0.88. Correct.
3. Ruggeri et al. 2020 (Nature page abstract): n=4,098, 19 countries, 13 languages, 94% of items, 12 of 13 contrasts. Correct.
4. Walasek and Stewart 2015 (PMC table 1): median lambda 1.79 [1.55, 2.00] Exp 1a; 1.59 Exp 1b; 2.28 Exp 2; 1.81 Exp 3; about 1.0 or below 1 in loss-wide ranges (0.88, 0.81, 0.93). Correct.
5. Tarabeih 2026 (arXiv 2610.33103): 102 estimates, 11 studies, 32 models, lambda 1.26 [1.06, 1.46], prediction interval 0.20-2.31, symmetric 1.15 vs 1.07, asymmetric 1.46 vs 2.3 (p=.004), curvature 1.01 vs 0.52, Gemini +0.69, release year -0.16. Correct.
6. Wang et al. (arXiv 2508.08992): human benchmark 0.670/2.630/0.685; 35 lottery pairs, 8,960 choices per condition; MAE > 0.20 and R2 < 0.10 failure rule. Correct.
7. Binz and Schulz (arXiv 2206.14576): 3 of 6 K&T biases; t(29134) = -16.85 and -11.50. Correct.
8. Liu et al. (arXiv 2406.17055): GPT-4o 0.94 vs humans 0.48 with max EV. Correct.
9. Yechiam and Tarabeih (arXiv 2608.12339, abstract): loss aversion in report predicts the model's own level. Direction confirmed, numbers not re-read.
10. Ross et al. (arXiv 2408.02784, abstract), Chen et al. (2305.12763), Suri et al. (2305.04400), Wang abstract: headline claims confirmed.

## Corrections
- c17: the 0.41 and 0.28 figures are zero-shot correlations between LLM direct choices and max expected value (low, because LLMs sometimes ignore probabilities). They are NOT the same quantity as the 0.93/0.94 prediction-mode figures. Claim K21 separates the two.
- b03 / "1.73": 1.73 is the working-paper estimate (0.25 below published). The bias-corrected mean is 1.742. Neumann and Bockenholt (2014) also report 1.73 on a different dataset, which is a coincidence not to be confused.
- a08: only alpha, beta, lambda 2.25 and the 25-student sample are now verified. gamma 0.61 and delta 0.69 remain from memory.
- a09 and b01 are the same paper (OSF preprint versions 2020 and 2022); counted as one source. a10 and b04 are the same Ruggeri paper. Several LLM items are duplicated across files (Ross a15/b09/c08; Jia a17/b13/c07; Suri a19/b16/c13; Binz a18/b17/c12; Ge b20/c15). Independent-source counts in claims.jsonl take this into account.
- K01: the Problem 7/8 pair is 86% vs 73% (not 86% vs 27%).

## Contradictions and tensions
- Human lambda: 2.25 (1992) vs 1.95 (meta-mean) vs 1.74 (bias-corrected) vs 1.07 or 1.31 (conservative meta-analyses cited by Tarabeih). The LLM 1.26 sits inside this spread, so "LLMs are less loss averse than humans" depends on which human number is used.
- Chen et al. (GPT highly rational) vs Payne (framing effects) vs Binz (3 of 6 biases): not contradictory. Rationality on budget tasks does not carry over to wording-sensitive tasks.
- Ross: GPT-4 Turbo risk-seeking for losses like humans; Jia: ChatGPT weights probabilities opposite to humans (parameter above 1); Hartley: GPT-4o near risk-neutral. Model, method and elicitation differ, so no single "LLM prospect-theory profile" exists.
- Reasoning models near EV (Ge) vs LLMs more loss averse after priming (Yechiam and Tarabeih): consistent only if the reasoning model also ignores the priming; untested.

## Weak spots
- Almost all LLM evidence uses old models (GPT-3 to GPT-4o, Claude 3 to 3.5, Llama 2/3). Few tests of 2025-2026 reasoning models.
- Fitted parameters depend on the elicitation (TK vs Tanaka), temperature, and prompt wording; the pooled lambda mixes designs.
- Evidence is hypothetical-choice throughout; no LLM test has real stakes.
- Payne's single-scenario flips (85.6% vs 0.8%) are scenario-specific and cannot be pooled.
- Replication evidence for the human core is strong (one large study), but the "weak spots" literature (loss aversion critique, Oprea mirror) was read only at review level.
- The relevance for the agent is "background only": no schema change is justified by this subfield alone.

## Only seen in snippets or not opened
a22 (title only), b21 Wulff et al. 2018 (no numbers), b22 Gal and Rucker, b23 Yechiam 2019, b24 Hertwig et al. 2019, a11 Hertwig 2004 abstract only, a08 CPT 1992 (memory), a12 accountability replication (abstract), c14 Echterhoff (abstract), a21 awareness numbers (uncertain reading of two-column text), Payne and Ge and Saeedi numbers were not re-opened by me.

## GAPS
1. Do current reasoning models (o3, Claude 4-class, Gemini 2.5, GPT-5) still show the K&T certainty, reflection and isolation effects when the 1979 items are given verbatim? Only GPT-3 has been tested on the full six-bias set.
2. Does a "re-express in final outcomes / neutral wording" step reduce framing flips at equal tokens, and by how much compared with plain chain of thought?
3. How large is the LLM description-experience gap for reasoning models given 20 vs 100 simulated draws (Ge et al. report a gap but the size per model class is unclear)?
4. Does priming by literature (Yechiam and Tarabeih) affect decisions inside an agent that reads papers during a task, and can a guardrail remove it?
5. What do Wulff et al. 2018 (effect size of the description-experience gap), Gal and Rucker 2018 and Yechiam 2019 actually report for small-stake designs, and are they relevant to LLM stakes?
6. Does the Oprea no-risk mirror pattern appear in LLMs? If yes, LLM "probability weighting" may be a complexity heuristic.
7. Do LLMs show reference-point shifts (status-quo or expectation-based) in multi-step agentic tasks, not one-shot gambles?
8. Is LLM loss aversion in asymmetric designs (losses smaller than gains, human lambda about 2.3) lower because of training data, RLHF, or the way models read the prompt? Compare base vs tuned (Itzhak et al. suggest tuning raises the certainty effect).
9. How stable is fitted lambda across temperature, number of repetitions and elicitation method for a single fixed model (test-retest)?
10. Do the 1992 CPT weighting parameters (gamma 0.61, delta 0.69) hold in the primary text? A quick confirm from the original paper or the Brown appendix is still missing.

## Gap search results
Evidence is in evidence_d.jsonl (d01-d23). New claims K27-K37 are in claims.jsonl; K10, K12, K13, K17, K18, K20, K22, K23 and K26 gained evidence ids. Search note: the shared WebSearch budget was already spent, and the arXiv and OpenAlex search endpoints returned HTTP 429, so most sources came from direct PDF and abstract fetches (arXiv, Crossref, Europe PMC, OpenAlex by DOI).

1. Verbatim K&T 1979 items on current reasoning models: STILL OPEN. No study found. Indirect evidence: reasoning models follow EV on plain numeric gambles (Ge: correlation 0.86-1.0; Marks and Vollberg: 94.3-99.9% higher-EV choices, lambda 1.005-1.28) but o3 and Claude Sonnet 4 with thinking still flip with story framing (Payne: 85.6% vs 0.8% in one scenario, reverse effect in another). The two results fit together by format: numbers versus narrative (K27, K28).
2. Re-express / neutral wording versus plain CoT: PARTLY OPEN. Payne's maths-form control shows 200/200 (o3) and 196/200 (GPT-4o) indifference, so removing the story removes the flip. Ge shows a math explanation does not help conversational models. No head-to-head against plain chain of thought at equal tokens. Human precedent: concrete-number re-expression shrinks the Allais pattern (-39 vs -12 points).
3. Description-history gap size for reasoning models, 20 vs 100 draws: PARTLY CLOSED. Direction and class pattern confirmed (all 20 models; modest for frontier reasoning models, large for conversational and small open reasoning models; 100 draws do not remove it). Per-model numbers are in an appendix not read.
4. Priming by literature inside an agent: PARTLY CLOSED. Same-context priming is large (ChatGPT lambda 1.785 after Brown abstract vs 1.043 after Yechiam and Zeif; full text 1.519 vs 1.082) and independent of sample size. A joint-evaluation prompt reduced the effect in one model, but delayed priming in a long run is untested.
5. Wulff 2018, Gal and Rucker 2018, Yechiam 2019: PARTLY CLOSED. Only abstracts were read (no effect sizes). Wulff: more than 70,000 choices from more than 6,000 participants, robust gap, problem structure moderates it, small samples the largest driver, gap persists without sampling error. Gal and Rucker and Yechiam: loss aversion is conditional, small losses often not overweighted. Their stake argument fits near-1 LLM lambdas in hypothetical tasks.
6. Oprea mirror pattern in LLMs: STILL OPEN. No LLM test found. Hintze et al. (abstract) say LLM weighting mostly lacks the inverse S and GPT-4 looks like decisions from experience.
7. Reference-point shifts in multi-step agent tasks: PARTLY CLOSED. LLM trading agents respond to a peak or trough as a second reference point (GPT-4o sells 97/100 in G+, 85/100 in G-), Qwen-2.5-7B does not; prompted loss-averse agents switch style less in year-long simulations (rank-biserial 0.47-0.67). All with 2024 models and prompted traits.
8. Base versus tuned for LLM loss aversion: STILL OPEN for lambda. For the certainty effect, tuning raises it (pretrained 0.00/0.09/0.03 vs tuned 0.24/0.67/0.17/0.29). Within families lambda falls 0.16 per release year, GPT-3.5 2.72 to GPT-4.1 0.57. Cause (data, tuning, safety training) is not resolved.
9. Test-retest of lambda: PARTLY CLOSED. One preprint appendix: coefficient of variation below 0.15 for T up to 0.7, above 0.30 at T=1.0; probability weighting ICC 0.62. No dedicated test-retest study; Wang et al. fixed T=0.7.
10. CPT gamma 0.61 and delta 0.69: PARTLY CLOSED. Tarabeih uses 0.65 as the 1992 weighting benchmark, the mean of 0.61 and 0.69. Primary text still not retrieved.

New weak spots found: the Payne and Ge results use different task formats and cannot be pooled; Yechiam and Tarabeih and Tarabeih share an author; Yee and Koh stability claims rest on short appendix text; the Oprea reply (Li, Liu, Niu, Wang 2025) was seen by title only.
