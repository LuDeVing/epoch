# Critique: A13.07 Item difficulty modelling (cross-check)

Checker re-opened the arXiv abstracts and the full text (pdftotext) of the sources behind the key numbers. Scratch files are in D:/research_scratch/A13.07/.

## Numbers re-checked against the source text

Confirmed as written:
1. Peters et al. 2025 review (2509.23486): r 0.040-0.870, N=17, mean 0.545, SD 0.225; R2 mean 0.478 (N=13); RMSE on Rasch b mean 0.740 (N=8); accuracy 0.325-0.806, mean 0.567 (N=3); expert-rating r as low as 0.38 (cited from Conejo 2014).
2. Acquaye et al. 2026 (2601.09953): correlations up to 0.75, 0.76, 0.82 (grades 4, 8, 12); Gemma beats Llama and Qwen. Direct-prompt range (-0.139 to 0.137) is from evidence text; only the abstract-level claim "poor direct judges" was re-read.
3. Brant et al. 2026 (2602.06631): mean predictor RMSE 1.19 with rho 0; o3 0.37, Claude-4-Sonnet 0.33, GPT-4o 0.31; image items RMSE rise 1.26 (SD 0.95), 56/76 pairs.
4. An and Wang 2026 (2609.27063): label rho 0.06, Bloom rho 0.02, label vs Bloom 0.90; 378 authored, 311 deployed, 7,888 responses.
5. Kapoor et al. 2026 (2502.20663): RMSE 0.59 vs 0.92, r 0.77; 1,076 items. The abstract confirms embeddings add only marginally.
6. Razavi and Powers 2025/26 (2504.08804): r up to 0.87; RMSE 0.83 for the RF; dummy reduction 18.5%; r=.83 pooled.
7. Li et al. 2026 (2512.18880, ACL 2026 camera-ready): SAT Math ensemble 0.56 to peak 0.66, dilution after K=14; Savant Rate 70.4% (USMLE), 32.2% (SAT Math), rho 0.386.
8. Zhu et al. 2025 (2509.12886): ROC-AUC 93.09 and Macro-F1 79.48 (these are the same 7B-model figures quoted in the text).
9. Zotos et al. 2025 (2412.11831): 0.1361 (Biopsychology, first-token), 0.2868 (USMLE), 0.1654 (CMCQRD), 8.2763 (CMCQRD IRT).
10. Wang et al. 2026 (2607.28634): QWK 0.578 (GPT-4.1, temperature 0, accuracy 0.618 in the prompt comparison) and ConvBERT 0.625.
11. Also confirmed: Scarlatos SMART PCC 0.649 / zero-shot 0.2651 / CodeWorkout 0.308; Hoyl Pearson 0.7791 vs embeddings-only 0.6822; Easy2Hard GPT-4 vs IRT Spearman 0.612 / 0.218 / 0.164; ARC-AGI-2 407 participants, 515 sessions, 1,848 pairs, 13,405 attempts; EIP 30 models, 35,550 questions; Liu et al. 76.2%.

## Corrections made (applied in claims.jsonl, not in the evidence files)

- a18 (Wang et al. 2026) misreads the confusion table. Rows are the true level; columns are the predicted level (easy, medium, hard). For GPT-5 the rows read: easy 100/0/0; medium 89.33/10.67/0; hard 56.92/43.08/0. So GPT-5 labelled 89.3% of medium items easy and none of the hard items hard (hit rate on hard 0%, on medium 10.7%). The evidence says "medium 89.3%, hard 43.1%" as hit rates. That is wrong. GPT-4.1 hard hit rate 43.1% and medium hit rate 85.3% are right. The GPT-5.4 figures (easy 96.1%, medium 92.0%) were not re-checked and are probably also the share predicted easy. Treat a18's GPT-5 and GPT-5.4 hit rates as wrong. The conclusion (stronger models call most items easy) stands and is stronger than stated.
- a13 gives within-grade math adjusted R2 as ".11 (grade 5) to .23 (grade 4)". Table 4 of Razavi shows math grade 1 R2 = 0.003 (p = .369) and reading grade 1 R2 = 0.019; so the range is .003 to .231 for math, and the lowest values are in grade 1, not grade 5. Also, those R2 values are for the direct LLM estimate regressed on true difficulty; they are not the feature model.
- a13/c03: "math grade K worse than the grade-average dummy" concerns RMSE after rescaling; the regression R2 for grade K is .132 (positive). Both are true; do not quote one as if it were the other.
- a15 vs c01 give different dates and RMSE for Kapoor (v1 RMSE 0.52, v2 0.59). Use the later (0.59).
- b14/a24 disagree on GPT-4.1 accuracy (0.535 vs 0.618). Both are right for different settings: 0.535 is the default setting (temperature 1), 0.618 is temperature 0.
- b15 says "o3 0.37, Gemini-2.5-Flash 0.35". The Table 3 text shows o3 0.37, Claude 0.33, GPT-4o 0.31, Gemini-2.0-Flash 0.31 at its best prompt; Gemini-2.0-Flash reaches 0.37 only in the math subset. The Gemini-2.5-Flash 0.35 was not found in Table 3 and is unverified.

## Contradictions between sources

- Direct LLM difficulty rating: Razavi r .81-.83 (K-5, pooled across grades) vs Acquaye r about 0 (NAEP math, within grades 4/8/12) vs Brant rho .3. Likely reconciliation: pooling over grades. Not tested directly.
- Persona or simulated students: Acquaye (up to .82) vs Li (persona changes accuracy under 1%, single personas unstable) vs SMART (zero-shot .265). Reconciliation is aggregation over many runs plus weak models, but this is a reading, not a test.
- Model size: Acquaye says weaker Gemma beats stronger Llama and Qwen; Li says scaling does not help; Wang says GPT-4.1 beat GPT-5.4. Consistent, but all point to "stronger means worse", which is a ceiling effect, not an understanding effect.
- Sources disagree on what is predictable: Sun 2019 LLTM explains 77% of number-series variance in-sample, yet the generated-matrix set (307 participants) was predicted "far from enough". Rule-based synthetic items vs. human-designed items.

## Weak spots

- Carpenter, Just and Shell (1990) numbers (57% of error variance, r=.87, Tower of Hanoi r=.77) were taken from the evidence files; the checker did not re-open them (kilthub page only). Treat as unchecked. Sample sizes are tiny (12 and 22 students).
- Nothing primary from Embretson (1995, 1998, 2004) was opened. All CDS content is via the Yang et al. reviews. The 40% variance figure belongs to an early bank, not CDS; the "attrition up to 50%" is second-hand.
- Many evidence lines are the same paper several times (Razavi x4, Wang x3, Acquaye x4, Peters x6). Independent-source counts in claims.jsonl count papers, not lines.
- Zotos et al. papers (3) are one lab. Wang, Jiao, Li, Peters, Zhou and Li, Jiao, Zhou share authors; independence is partial.
- The professor study (b05) has about 10 test items per exam; the Spearman .853 is not stable.
- Seen only at abstract or in snippets: Webb et al. r(30)=.39 (grep only), Kolesnikova pairwise (exact tables not recorded), Jain et al. (no correlation recorded), RIDE (no human validation), Hoyl single dataset, EIP (relative to model pool; "90% agreement" definition not re-read).
- Evidence c26 is a synthesis line, not a source.
- No evidence tests S0 gating on an agent at equal tokens. Liu 2025 and Zhu 2025 are the nearest and use their own models and metrics. Net token savings are reported by the authors; not independently replicated.
- The difficulty target differs by study (p-value, Rasch b, human pass rate, model pass rate). Cross-study comparison of r values is loose.

## GAPS

1. Does a cheap pre-solve difficulty gate (3-5 samples, absolute pass-rate thresholds) save tokens at equal accuracy for an API-only agent, compared with fixed-depth search? (No study found with equal total tokens including the probe cost.)
2. How well do rule-count and perceptual features (Carpenter/Embretson style) predict difficulty for current frontier models on ARC-AGI-1/2 tasks, as opposed to human difficulty? Is there a measured correlation between ARC-AGI-2 human pass rate and model pass rate?
3. Is within-family accuracy of LLM-extracted feature models reproduced (Razavi's gains are pooled over grades)? Are there replications that report within-level rank correlation?
4. How many samples are needed for a stable pass-rate rank (Acquaye says n=50 is enough for humans' difficulty; what about difficulty for the model itself)? Does sampling from varied prompts beat repeated samples?
5. What do the Embretson primary papers (1995, 1998, 2004) report in numbers (variance explained, cross-validation, item attrition), and has the Carpenter 57% result been replicated with larger samples?
6. Can the model's own first-pass cost (tokens, loops, uncertainty) be read with an API-only agent and does it beat a feature count? (Zhu needs hidden states; Epi2Diff needs a full solve.)
7. Does difficulty-based routing fail on the hardest items (Jain: extremes compressed; Wang: hard items mislabelled easy)? What is the miss rate on items the model rates easy but fails?
8. Does a difficulty estimate transfer across task families or across model versions, and how fast does it go stale when the base model changes?
9. Are there 2020-2026 papers using IRT or Glicko difficulty to allocate reasoning budget in agents (the second search sweep that was cut off by the web quota)?
10. How do the explained-variance requirements (about 75% R2 in the CAT simulation) translate to an agent: what R2 or rho makes a difficulty prior worth its cost compared with simply spending a standard budget?

## Gap search results

Gap searcher pass. Evidence is in evidence_d.jsonl (d01-d20, all opened as full text; PDFs in D:/research_scratch/A13.07/). Claims K01, K02, K10, K11, K16, K19 and K20 were extended; K21-K27 are new. The WebSearch quota ran out after three calls, and the arXiv API, Semantic Scholar and OpenAlex rate-limited or returned nothing, so most discovery went through arXiv listing pages. Every "none found" below is under that limited search.

1. Cheap pre-solve gate at equal tokens: MOSTLY CLOSED for math, OPEN for agent tasks. Equal-budget gains exist: UAB +2.3 points average (probe samples reused in the vote; no significant gain at N=16), AdaCompute +4 to +6 points on MATH with 16 text features (API models DeepSeek-V3 and GPT-4o-mini; not exactly equal cost at B=3), Predictive Scheduling +7.9 points on GSM8K (hidden states). Pishehvar et al. show the probe can cost more than always calling the big model (k=10: 1.38x). No study gates depth in a multi-step agent loop (K21, K22).
2. Rule-count and perceptual features for frontier models on ARC-AGI-1/2, and human-vs-model pass-rate correlation: OPEN. The ARC-AGI-2 paper reports no per-task human-vs-model correlation, and model scores were 1-3%. On ARC-AGI-1, grid size predicts human difficulty weakly (r -0.16, -0.02) and trace length correlates 0.16-0.30 with human item time. A symbolic-solver study (not LLM) finds a mid-run grid signal. Nobody has tested Carpenter-style rule counts against model pass rates (K24).
3. Within-level reproduction of Razavi's gains: OPEN. No replication reporting within-level rank correlation was found. K06 stays single-source.
4. Samples needed for a stable rank: CLOSED for the model's own signal, OPEN for prompt variety. Two samples gave AUROC .780 (UAB); five matched ten (.865 vs .862) and three lost about .07 (Pishehvar). No test of varied prompts vs repeated samples was found (K23).
5. Embretson primary numbers and Carpenter replication: PARTLY CLOSED. Embretson and Daniel 2008: R2 .451/.435, 101 GRE items, 534 students, delta fit .724. Embretson 1995, 1998, 2004 were not opened. Carpenter 57% and r=.87 confirmed in the 1990 text, but from 12 students and 32 items; no larger-sample replication found.
6. First-pass cost of an API-only agent vs feature count: PARTLY CLOSED. Reasoning-token count correlates only 0.16-0.30 with human difficulty and signals failure within an item (K25). Follow-up-question features reach AUROC .73-.79 for answer correctness while verbal confidence is at chance (K27). No head-to-head against a feature count was found.
7. Failure on the extremes: PARTLY CLOSED. UAB gains peak at middle levels and are smaller at the hardest because the right answer is never sampled. No paper reports the miss rate on items rated easy that fail. K09 stands.
8. Transfer across families or model versions: PARTLY CLOSED, answer is "poorly". Agent difficulty model on a held-out benchmark: AUC .67-.74 vs base rate .57-.64 vs oracle .91. Probes lose accuracy across datasets and as the reasoning level changes (AUROC .78 to .64). No staleness-over-time measurement across model versions was found (K19).
9. IRT or Glicko difficulty used to allocate reasoning budget: CLOSED as "not found". IRT is used for model routing (IRT-Router: +3% over GPT-4o alone at 1/30 cost) and for predicting agent success; budget allocation uses pass rate, sampling disagreement or text features (K20). A NeurIPS 2026 reasoning-aware IRT paper is an evaluation method only (abstract-level, not opened).
10. R2 or rho needed to beat a standard budget: OPEN. No paper translates the 75% R2 CAT figure to agents. Weak signals already pay in allocation: a prompt-length heuristic gave only +0.3 to +1.2 points, while a 16-feature classifier gave +4 to +6. This points to rank quality, not R2, as the working measure; it is an inference, not a test.

Still open after this pass: gaps 2, 3, 10 fully; gaps 1 (agent loops), 4 (prompt variety), 5 (Embretson 1995/1998/2004), 6, 7 (easy-but-fail miss rate), 8 (staleness) in part.
