# Critique: inductive, category-based and probabilistic reasoning (cross-check)

Cross-checker pass over evidence_a, evidence_b, evidence_c (86 lines). Claims are in claims.jsonl (28 claims).

## Numbers re-opened and checked (this session, from the PDFs or page text)

Confirmed unchanged:
1. Gigerenzer and Hoffrage 1995 (a11, a24): Bayesian algorithms 16% / 28% (probability, standard / short menu) vs 46% / 50% (frequency); 620 of 1,774 coded solutions (34.9%); 43.3% gave 8 out of 103 on mammography.
2. Weber, Binder, Krauss 2018 (b01, b03): 20% vs 36% correct; heroin 51% vs car 22% with frequencies; 49% of those shown frequencies still chose probability calculation, 18% switched the other way; marginal R2 .065, conditional .685. The 4% to 24% meta-analysis figure is quoted by them from McDowell and Jacobs; we did not open that meta-analysis.
3. Chapman and Liu 2009 (a13): high numerates n=190, low n=156; 27% / 31% vs 7% / 10% correct with frequencies.
4. Wang et al. 2024 (a20-a22, b17-b19, c10-c11): 17 / 23 / 30 / 33 / 45% on ARC, 49 of 100 tasks with a correct hypothesis, 33 of 49 (67%) converted by human selection, 19% for CoT-without-code, 1D-ARC 39.6 / 61.1 / 73.1, SyGuS 94.3, Parsel 47.5.
5. Han et al. 2023 (a18, c01): 792 pairs, 120 recruited, 110 kept, about 9.17 ratings per cell; Spearman .65 is between 40 people rating the 36 original Osherson arguments and the 1990 rankings.
6. Li and Rui 2024 (b15): odds ratios 9, 9, 8.86, 6.36, 3, 9, humans 2.25.
7. Li et al. 2024 (c13): induction 2048 samples 18.78%, transduction 15.25%, ensemble 26.50%, 56.75% vs 60.2% average human, about 9% of train-fit programs fail on test.
8. Bazigaran and Sohn 2025 (c15): 255 sets, divergence 0.87, rule bias 0.9 human vs 1 GPT, maximum-likelihood inference.
9. Greenblatt 2024 (c12): 50% test, 72% held-out train vs human 85% on train (the 85% is a TRAIN-set human figure; there is no known human baseline on the test set), +3% per doubling, revision fixes about 20% of the remaining wrong.

Corrections made (apply to the evidence files when merged):
- a12: "Bayesian algorithms 60 with relative frequencies vs 66 with probabilities" are COUNTS of coded solutions in Study 2, not percentages. The 6.4% figure is the standard-menu probability share in Study 2.
- c06: MiniARC under refinement is not uniformly worse. T=1,N=1 gives 3.8 and T=1,N=5 gives 9.2, but T=3,N=5 gives 14.6 vs plain 13.8, a negligible gain. Also the List Functions gain (39.6 to 52.0) is at T=1,N=1; at T=3,N=1 it is 42.4, so more iterations did not help there. Some Table 1 rows are garbled by text extraction (the rows 86.6/98.2 appear to be oracle-interpreter settings); treat them as unread.
- a13: the paper's abstract says 342 students, its method and tables say 346 (190 + 156). Both are in the paper; use 346 for the group tables.
- a11: format and menu are confounded. The "short menu" (give only the two numbers needed) lifts probability-format performance from 16% to 28%, so part of the frequency benefit is just a cleaner problem statement. Any test on the agent must hold the menu fixed.
- a18/c01: the .65 is a human-vs-1990 replication check, not a model score; do not cite it as a model correlation.

## Contradictions and tensions between sources

- Frequency format: a11 reports 46% Bayesian algorithms, b01 reports 36% correct, b02 reports 24% in a meta-analysis, a13 reports 27-31% for the numerate and 7-10% for the rest. These differ because they measure different things (algorithm used vs correct final answer), different populations, and in a11 the coding scheme counted algorithms, not correctness. The headline "frequencies fix Bayesian reasoning" is true only against a floor near 0-16%.
- Conjunction fallacy: a15/a16 show frequency wording drops the error from 65% to 25%, supporting the polysemy / pragmatic account (b26, not opened). b10-b12 show the error survives betting and hidden-sentence controls. Both are true: wording reduces it, no wording removes it. The sizes are not comparable across papers (rank tests vs per-item rates).
- LLMs and Linda: c19 reports GPT-4 correct 0.98 on Linda variants; c23 and c24 report the same models failing novel items; b23/c20 report that most errors are illogical rather than human-like. These fit together as memorisation of famous items plus fragile general skill, but no paper tested this directly.
- Number game: c14 reports an LLM-proposed hypothesis set fits human curves; c15 reports a reasoning model does not generalise from one example; c16 (2026) reports prompt conditions change how close LLM predictions are to a two-parameter model. Different models and prompts; unresolved.
- Hypothesis search value: a22 shows hypotheses add a lot on 1D-ARC and List Functions, b19 shows they add nothing on SyGuS (94.3 both ways). The value depends on whether direct coding already works.

## Weak spots

- Independence is thin. Most LLM claims rest on one paper each: Wang et al., Qiu et al. (b20 and c06-c09 are the same paper split across agents), Han et al. (a18, a19, a28, b22, c01-c05 are one paper counted up to nine times). b23 and c20 are the same paper; b24 and c22 are the same author. I counted independent sources, not lines.
- Kemp/Tenenbaum models (a01-a06, a30) are by one lab, fit to averaged ratings, with hand-chosen structures; strong on fit, weak as a mechanism claim.
- All LLM results are GPT-4-era or earlier model versions (plus a few 2025-26 items); numbers will not transfer to current models without retesting.
- Human samples are small or unusual: Ellis number game uses 8 participants; Weber students from one university; Chapman and Liu college students.
- Hypothesis-search "human-written / human-selected" arms use human oracle hypotheses (LARC) and are upper bounds, not usable methods.
- Greenblatt's 50% is a blog post, not peer-reviewed; the ARC public test set is not the held-out test.
- Nothing in the set tests the key design question directly: does an agent that extracts numbers and computes Bayes in code beat plain CoT on base-rate items at equal tokens.

## Seen only in snippets or abstracts (not opened in full)

a09 (Tenenbaum 1999), a25 (Osherson et al. 1990), a26 (Heit 1998), b25 (Tversky and Kahneman 1983 original Linda; a14-a16 did open the 1983 paper, so b25 is redundant), b26 (Hertwig and Gigerenzer 1999), b27 (McDowell and Jacobs 2017), c28 (2025 frontier-reasoning snippet), c29 (Hagendorff 2023 abstract). c25 (Wong et al.) was read only in abstract, introduction and framework; no experiment tables. c08 human control in an appendix not read in detail. I did not re-open Tversky and Kahneman 1983, Sides 2002, Heit 2000, Kemp and Tenenbaum 2009, or the Han and Budescu 2022 paper this session, so their numbers stand on the other agents' reading only.

## GAPS (most decision-relevant first)

1. Does extracting the base rate, hit rate and false-alarm rate into a structured form and computing Bayes in code beat plain chain of thought and a natural-frequency prompt at equal tokens, on base-rate problems with current models? (No source tests this arm.)
2. How often does a correct hypothesis exist in a pool of N proposals versus get selected, for current models on our own tasks, and which selector in code (held-out example, agreement, size prior) closes the gap? (Wang et al. selection gap 49 vs 30 of 100.)
3. Does the frequency-format advantage survive for current LLMs when menu is held fixed, or is the whole effect a cleaner statement of the numbers? (Format/menu confound in Gigerenzer and Hoffrage.)
4. Do current frontier models still fail on freshly written Linda-form and base-rate items, or only on the famous versions, and does a mutated-input check (G3) catch the failures?
5. Does asking the agent why a premise set was chosen (pragmatic teacher assumption) repair non-monotonicity and diversity failures in current models? (Han et al. only studied GPT-3.5 and GPT-4 and offered the explanation untested.)
6. What is the best use of a held-out example when inducing a rule: how many of the given examples should be reserved before the 9%-fail rate (train-fit, test-fail) falls, and at what token cost?
7. Does calibrating the agent's stated probabilities with a one-parameter recalibration on log odds fit in code improve Brier score, and how much data does it need before it beats raw confidence? (Evidence is from human forecasters only.)
8. Is the explicit-candidate-list prompt (c16) enough to fix one-example overgeneralisation in the number game, and does it transfer to rule induction beyond the number game?
9. Are noisy or wrong examples detectable by the scaffold (one bad example out of 8 in Qiu et al.), and does outlier-aware induction recover accuracy?
10. Do structured priors (name the taxonomy, causal graph or threshold first) help LLM property induction relative to similarity-only prompts at equal tokens? (Only human and model-fit evidence exists.)

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). Claims K02, K04, K09, K14, K16, K19, K22, K23, K25 and K27 were updated; K29 to K36 are new. Sources were opened as PDF or HTML text, except d18 (Han et al., snippet only).

Closed or mostly closed:
- Gap 3 (menu confound), for humans only. Gigerenzer and Hoffrage crossed format and menu: frequency 46% (standard) and 50% (short) vs probability 16% and 28%. The format effect survives at fixed menu (22 to 30 points) but the short menu alone is worth 12 points. Neace et al. add that the Linda frequency benefit was confounded with giving a reference class. No LLM study crosses the two factors, so the LLM half of the gap stays open.
- Gap 6 (how much fit is not proof), partly. The 9% figure is not stable: CodeARC shows 28.7% of o3-mini first attempts fit all 10 examples and fail the oracle. How many examples to hold out and the token cost are still untested.
- Gap 4 (fresh Linda items), partly. GPT-4 scored .98 on 1024 fresh Linda-form items (Yax et al.), so the claim that models fail all novel rewrites is too strong. Token-perturbation tests (Jiang et al.) and a flipped-logic Linda item (o1, Unpuzzles) still show failures. The mutated-input check is the right tool, but nobody has measured how many failures it catches. Fresh base-rate items on 2025-26 frontier models: no source found.

Partly answered:
- Gap 2 (pool vs selection). Parab et al. (GPT-4o, list functions): a correct hypothesis in 46.4% of generator pools, 34.5% after a model-written summary; the summary drops 26% of correct ones; executing programs on the examples rescued 37% of front-end failures. Held-out vs agreement vs size prior was not compared. Still open for our tasks.
- Gap 7 (recalibration). Platt scaling cut Brier for four LLMs on 1614 forecasting questions (Claude-Sonnet-4 .146 to .129), trained on 7,824 items. A second paper warns that ECE-only gains can hide lost resolution. Minimum data and the one-parameter version: untested.
- Gap 8 (number game). Anchoring on one example is confirmed (Bazigaran and Sohn; Xiong). A weak-sampling prompt and thinking mode shift behaviour but do not remove it. Candidate-list prompt and transfer beyond the number game: still untested.
- Gap 9 (noisy examples). SRR (subset sampling plus code check) kept accuracy within about 2 points at 10% noise. No method found that names the bad example.

Still open:
- Gap 1 (extract numbers and compute Bayes in code vs CoT and natural frequencies at equal tokens). Searches found only indirect support: a code interpreter nearly restored counting accuracy (Pournemat et al.), and bias-avoidance prompts did not help judgment biases (CogBias). The arm has to be built in-house and is the top priority for G5.
- Gap 5 (teacher-assumption prompt). No test found.
- Gap 10 (structured priors in prompts). No test found; Rodriguez et al. only show base models already use both taxonomy and similarity.

Caveats on this pass: arXiv search by API returned poor results, so coverage rests on web search plus follow-up reading. Several sources are 2026 preprints not yet peer reviewed. The Li et al. noise table was garbled in text extraction, so only the average gap is quoted. The numbers for Williams et al. (Unpuzzles) rest on one worked example.
