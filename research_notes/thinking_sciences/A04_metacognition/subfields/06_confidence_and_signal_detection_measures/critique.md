# Critique: Confidence and signal-detection measures (A04.06)

Cross-check done 2026-11-01. Sources re-opened as full text (PDF or PMC XML): Xiong 2023/24, Tian 2023, Wang 2022, Taubenfeld 2025, Kuhn 2023, Steyvers 2025, Guo 2017, Leng 2025, Guggenmos 2021, Cacioli 2026, Servajean 2026. Abstract only: none relied on.

## Corrections and confirmations (10+ key numbers)
1. Xiong GSM8K AUROC 54.8 to 92.7 (GPT-3.5): CONFIRMED in text and tables, but the table is garbled and labels differ (Table 3 calls the 92.7 row "Prompt (M=5)", the appendix "Self-Random+Consistency"). Correction: this is the best dataset. The five-dataset average goes only from 69.2 (CoT, M=1) to 69.6 (self-random M=5) or 73.0 (prompt-varied M=5). Claims must say "largest on arithmetic", not "92.7 in general". Evidence b14 and a18 overstate if read alone.
2. Xiong ECE above 0.377, GPT-4 AUROC 62.7, GPT-4 GSM8K ECE 0.064 at 93.6 percent accuracy, white-box 0.605 vs black-box 0.522, Pair-Rank ECE 0.028: CONFIRMED.
3. Tian ChatGPT TriviaQA: label prob ECE 0.140 AUC 0.869; verbal 1-stage top-1 ECE 0.068 AUC 0.879; top-2 0.050 AUC 0.894; TruthfulQA verbal top-1 ECE 0.389 AUC 0.545 vs label prob AUC 0.418: CONFIRMED. Note: on TruthfulQA the verbal ECE (0.389) is still poor; "50 percent ECE cut" is "often", not always.
4. Wang +17.9, +11.0, +12.2: CONFIRMED (+17.9 and 78.0 with code-davinci-002; 74.4 for the PaLM-540B row). The agreement-accuracy link is shown only as a figure; no coefficient.
5. Taubenfeld cost reduction at budget 10 (10, 30, 31, 46 percent) and WQD (52.2 to 62.3): CONFIRMED. The 46 percent means self-consistency needed 18.6 samples to match CISC with 10.
6. Kuhn AUROC: CoQA 0.77 vs 0.66, TriviaQA 0.83 vs 0.79; distinct answers 1.27 vs 1.77 and 1.89 vs 3.89: CONFIRMED (row mapping now certain). Note the comparison is against a count of distinct answers, a fairly strong baseline, so the gain is 4 to 11 AUROC points, not huge.
7. Steyvers: 301 participants, model AUC 0.751/0.746/0.781, human 0.589/0.602/0.592: CONFIRMED. Venue is Nature Machine Intelligence.
8. Guo: CIFAR-100 ResNet-110 16.53 to 1.26; ImageNet ResNet-152 5.48 to 1.86; DenseNet-161 6.28 to 1.99: CONFIRMED.
9. Guggenmos (it is Neuroscience of Consciousness 2021, PMC8633424): N=6912 is the TOTAL pool; the main analyses use 1757 subjects (at least 400 trials, d' above 0.5). Hierarchical M-ratio beta -0.19 +/- 0.05 CONFIRMED; log M-ratio beta 0.01 +/- 0.02 (dependence gone in the hierarchical fit) but pooled log M-ratio rs is still -0.073, p=0.003, and the author says more data are needed. Reliability r about 0.7 (400-600 trials), 0.85 (600-800): CONFIRMED. 2.4 and 4 percent extreme values; 4 and 10 percent under 200 trials: CONFIRMED. Evidence b04 should not say "log M-ratio removes dependence" without these qualifiers.
10. Cacioli (arXiv 2603.25112v3, July 2026): 224,000 trials, 4 models, 1.98-fold, rho -0.80 / 0.00, scorer missed 53 and 26 percent, agreement 0.76 to 0.86, 1,200 adjudications: CONFIRMED. Correction: the confidence variable is token log-probability, not verbalized, and the measure is meta-I2r, not M-ratio; models are 8-9B. Single author, independent, not peer reviewed; v1/v2 claim already retracted by him.
11. Servajean: rs=0.9 p<0.002 and Mratio difference 0.16 CONFIRMED; the paper also reports LLM M-ratios from moderate (0.65) to near-optimal (0.90), which supports Dai's second-hand 0.62-0.92.
12. Leng: PPO-M on Llama3-8B: ECE down 6.44 and accuracy up 2.73 on GSM8K vs vanilla PPO: CONFIRMED (a23 should name PPO-M, not both).

## Contradictions between sources
- Calibration ranking: Xiong finds verbalized confidence bad (AUROC 62.7 for GPT-4); Tian finds verbalized better calibrated than token probabilities (ECE halved) on different benchmarks (TriviaQA, SciQ, TruthfulQA vs 8 datasets). Different metrics (ECE vs AUROC), different prompts. Not a real contradiction on discrimination, which is modest in both. Marked contested.
- AUROC2 and M-ratio can rank two LLMs oppositely (Servajean); Cacioli finds accuracy-efficiency coupling weak. Guggenmos finds M-ratio itself depends on accuracy. So no single metric is neutral.
- Kadavath (well calibrated on multiple choice) vs Xiong/Yona (overconfident, faithfulness near 0.5): format and model family differ.

## Weak spots
- No source tests Koriat's self-consistency model on an LLM directly. The core link (human consistency confidence to LLM agreement confidence) is an analogy asserted by Steyvers and Peters review. Koriat 2012, 2008, 1997, Maniscalco and Lau 2012, Galvin 2003, Masson and Rotello 2009, Nelson 1984 were never opened (paywalled; known only through Fleming and Lau 2014). Crossref confirms the Koriat 2012 record only.
- Founding human numbers (effect sizes, N) for Koriat and Fleming/Lau are missing. Fleming and Lau is a review with no data.
- No failed replication of the human measures found; the closest is Guggenmos (type-1 dependence) and the Dunning-Kruger dual reading.
- Most LLM studies use small or older models (OPT, GPT-3.5, 7-9B); few test frontier reasoning models. DeepConf, CISC and Cacioli are 2025-26 preprints.
- Whether agreement-based confidence beats verbal confidence for open-ended, long-form or code tasks is shown mainly on short-answer QA and arithmetic.
- Farquhar 2024 (Nature semantic entropy) not opened; the 0.79 vs 0.69 figure is from memory. Dai 2026 and Griot 2025 seen second-hand only.
- Evidence files have duplicates (Kadavath, Tian, Xiong, Kuhn, Wang appear in two or three files); independence in claims counts them once.

## Seen only in snippets or second-hand
Dai 2026 M-ratio 0.62-0.92 (b28), Cash et al. 2025 (c03), Griot 2025 (c27), Farquhar 2024 (c13), Koriat papers (a12-a14, b29, c26), Maniscalco and Lau (a09, b30, c25), Galvin, Nelson, Masson and Rotello.

## GAPS
1. Does agreement share across k samples of a frontier reasoning model (not GPT-3.5/OPT) beat verbalized confidence and token confidence at equal total tokens on open-ended and code tasks (AUROC2 and ECE)?
2. How often is high agreement wrong (Koriat's consensually wrong items) for current LLMs, and what cheap check (different framing, tool, test) breaks the false consensus?
3. What is the original Koriat 2012 evidence (effect sizes, N) that confidence tracks consistency, and was it replicated or contradicted (e.g., Koriat-related failures when the majority answer is wrong)?
4. Is agreement-to-accuracy mapping stable across tasks and models, so one held-out calibration map (temperature-scaling style) transfers, or must it be fitted per task type?
5. Which metric should grade the agent: AUROC2, log M-ratio or within-question discrimination, given type-1 dependence and AUROC2/M-ratio disagreement? What item count per arm (Guggenmos says 400+) is affordable?
6. Does weighting votes by a P(True)-style self-check (CISC, 46 percent sample saving) still pay once the cost of the extra self-check calls is counted?
7. Does sliding-window or tail token confidence (DeepConf) generalise to API models without logprobs, and can a proxy (agreement among partial traces) replace it?
8. Do metacognitive-efficiency results from small open models (Cacioli, 8-9B) hold for large instruction-tuned models with reasoning traces, and is the claimed accuracy independence real after fixing scorer bias?
9. What are the original numbers for Dai 2026 (M-ratio 0.62-0.92) and Farquhar 2024 (semantic entropy AUROC on long text)?
10. Does reporting confidence to a human reader (matched wording) change human accuracy and overconfidence when the confidence comes from agreement rather than from the model's own words?


## Gap search results (evidence_d.jsonl, d01-d20)

Search tools: WebSearch quota was used up, so I used PubMed, PMC, Nature, arXiv PDFs by known id. The arXiv, Semantic Scholar and OpenAlex search APIs were rate-limited. Papers found only by id mean some relevant work may be missed.

1. Agreement vs verbalized vs token confidence for a current frontier reasoning model, open-ended and code, equal tokens, AUROC2 and ECE: STILL OPEN. No source runs this head to head. Pieces found: Yoon 2025 (verbalized is better in 32B reasoning models, 33 of 36 settings), Mei 2025 (API reasoning models overconfident), Dai 2026 (GPT-5.2 and Gemini 3.1 Pro verbalized M-ratio 0.92 and 0.74; Gemini says 100 on 68.4% of items, right on 79%). Kang 2025 notes exact-match agreement does not exist for code, so agreement must be defined by test behaviour. We must run this ourselves.
2. High agreement but wrong, and the cheap breaker: PARTLY CLOSED. The failure class is established (Koriat consensually wrong items; TruthfulQA; the semantic-entropy authors say the method fails on systematic errors). The breaker for code is clear: tests (Large Language Monkeys: SWE-bench Lite 15.9 to 56% with verification; MATH voting stuck at 40.50 to 41.41% while coverage reached 98.44%). The current-LLM rate and the best non-code breaker (framing, tool) remain unmeasured.
3. Koriat 2012 evidence and replications: PARTLY CLOSED. Mechanism and direction confirmed by the 2012, 2011, 2008 and 1976 abstracts and by the 2025 open review: 16 tasks, CC positive and CW negative, repeated by Brewer and colleagues, Sampaio 2017, Bajsanski 2019, Litvinova 2022 (mammograms), plus Caziot and Mamassian 2021. Exact effect sizes and N for the 2012 paper were not obtained (paywalled; supplementary tables of the 2025 paper not read). No failed replication found; none was actively located either. The 2015 amplification paper adds a warning for confidence-weighted voting.
4. Stability of the agreement-to-accuracy map: PARTLY CLOSED, negative side. For code token confidence, a map transfers only between tasks of similar kind and base rate (skill 0.14 to 0.12), and fails across kinds (0.12 to -1.28); above 64 labelled points are needed. No test of agreement-based maps across tasks or models was found. Plan per-task-family maps.
5. Metric and item count: STILL OPEN, narrowed. AUROC2 is inflated by few confidence levels (Yoon), M-ratio from a single threshold is crude (Dai), Guggenmos needs 400 or more trials. My rough budget: 400 items x 10 samples x 3,000 tokens is about 12 million tokens per arm, affordable for one or two arms, not for a wide sweep. Practical rule: AUROC2 with many-level scores plus ECE as the main pair, within-question discrimination for the vote-weighting test, M-ratio only at 400 or more items.
6. P(True) weighting after self-check cost: MOSTLY CLOSED for self-hosted or cached-prefix serving. The check adds about 20 input tokens and 1 output token, so 46% fewer samples is close to a real saving there. Without prefix caching the cost may be near one extra input pass per sample (my reading, untested). No reasoning-model test.
7. Sliding-window confidence for API models without logprobs: CLOSED NEGATIVE for the token filter (DeepConf needs token log-probabilities; best cell 84.7%, range 43.8 to 84.7% for low and 18.8 to 59.0% for high). A logprob-free agreement stop rule exists (Adaptive-Consistency: up to 7.9x, average 3.3x fewer samples, 0.04% accuracy drop, 2023 models). Agreement among partial traces: still untested.
8. Cacioli results at large scale: STILL OPEN. Cacioli himself says frontier scale is unknown; the scorer still rejects 18.4% of correct answers, varying 2.4-fold by model. Dai 2026 gives a verbalized frontier data point but with a different measure.
9. Original Dai and Farquhar numbers: CLOSED. Dai (arXiv 2603.09309 v4): six models, M-ratio 0.62 (Qwen3-30B) to 0.92 (GPT-5.2) at 0-100; 0-20 scale raises it; binarised single-threshold meta-d; preprint. Farquhar (Nature 2024): AUROC 0.790 vs 0.691 naive entropy, 0.698 P(True), 0.687 embedding regression over 30 combinations with 10 generations; GPT-4 paragraph results use a discrete variant and a claim-by-claim question rebuild.
10. Reader effect of agreement-derived confidence: PARTLY CLOSED. Wording matters: first-person hedges raised accuracy 63.9 to 72.8% and cut agreement 80.9 to 74.8% (Kim 2024, N=404); matched wording narrowed calibration and discrimination gaps (Steyvers 2025, N=301). But the hedge in Kim was assigned by the experimenters and in Steyvers it came from token likelihood. No study uses agreement counts. Long explanations hurt: confidence up, discrimination flat (AUC 0.54).

New corrections to earlier notes:
- Evidence a-c should not describe 84.7% as a general DeepConf figure: it is the best of 12 cells.
- Steyvers: modified-explanation human ECE (0.225) is read from a figure and tied to one panel, approximate.
- Taubenfeld's overhead claim relies on reusing the cached prefix.
- Koriat evidence d01-d04 and d06 are abstract-only, so they are marked opened:false.

New claims added: K22-K30. Changed: K07 (now established for human side, LLM rate split off to K23), K08, K09, K11, K13, K16, K19.
