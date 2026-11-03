# B02.10 Confidence and metacognition: cross-check critique

## Numbers re-opened this session (all from the source PDF or PMC text)
Confirmed unchanged:
1. Xiong 2024 (arXiv 2306.13063): GPT-4 mean AUROC 62.7%; ECE above 0.377 for weaker models; about 22.2% AUROC gain GPT-3 to GPT-4; GSM8K 93.6% accuracy with ECE 0.064 at 100% confidence; Top-K (M=1) 54.8 to Prompt (M=5)+consistency 92.7 on GSM8K.
2. Kuhn 2023 (2302.09664): TriviaQA 0.83 vs 0.79, CoQA 0.77 vs 0.66; distinct meanings 3.89 vs 1.89 and 1.77 vs 1.27.
3. Tian 2023 (2305.14975): TriviaQA label-prob ECE 0.140 / AUC 0.869; Verb 1S top-1 0.068 / 0.879; top-4 0.054 / 0.896; SciQ 0.256 to 0.065; TruthfulQA 0.451 / AUC 0.418.
4. Huang 2024 (2310.01798): GPT-3.5 CSQA 75.8, 38.1, 41.8; GSM8K 75.9, 75.1, 74.7; GPT-4 GSM8K 95.5, 91.5, 89.0; SC 82.5/85.3/88.2 at 3/6/9.
5. DeepConf (2508.15260): 99.9 vs 97.0 vs 91.8; 84.7% fewer tokens.
6. CISC (2502.06233): over 40% fewer paths; 18.6 samples, 46%.
7. Kadavath 2022 (2207.05221): P(IK) AUROC/Brier 0.864/0.151, 0.928/0.194, 0.606/0.431.
8. Wang 2023 (2203.11171): +17.9% GSM8K (that is the best model, PaLM-540B row), LaMDA 17.1 to 27.7 (+10.6), imperfect prompt 17.1 to 14.9.
9. Kumaran 2025 (2507.03120): 32.5% vs 13.1%; 39.2% vs 85.0%.
10. Fleming 2010 (PMC3173849): split-half r=0.69, P=0.00001; BA10 peak [24,65,18], tmax=4.8, P<0.05 corrected. Steyvers 2025 (2401.13835): AUC .751/.746/.781 model, .589/.602/.592 human. Binder 2024 (2410.13787): 48.5% vs 31.8% (about +17 points, absolute).

## Corrections and clarifications
- a15 headline "GSM8K +17.9%" is the best model in Wang et al., not LaMDA; the LaMDA figure is +10.6 (a15 already gives it, keep both labelled).
- b12/a20 disagree on the starting point of the GSM8K jump (a20: 88.6 to 92.7; b12 and the paper text: 54.8 to 92.7). The paper text says 54.8 to 92.7. 54.8 is the Top-K (M=1) cell, GPT-3.5, GSM8K, not a plain vanilla prompt. The 88.6 figure was not found; treat as wrong.
- a18 "62.7%" is the GPT-4 average over datasets; 92.7 and 54.8 are GSM8K only. Do not mix.
- Binder "+17%" is absolute percentage points (48.5 vs 31.8), not relative.
- c14 debate figure "about 83" not re-checked.
- Kuhn's model identity (not recorded in evidence) was not re-opened; semantic entropy numbers are for a mid-size open model, not frontier chat models.

## Contradictions between sources
- Verbalized confidence: Tian (RLHF models, ECE cut by half or more, AUC .87-.90 on TriviaQA) versus Xiong (GPT-4 AUROC 62.7%, constant 80-100%). Differences: metric (ECE vs AUROC), dataset mix, prompts. Not a true contradiction: calibration can improve while discrimination stays weak.
- Chain of thought: Xiong finds CoT does not improve discrimination; Yoon finds reasoning models improve both. Likely depends on whether the chain is trained to revise itself. Marked contested.
- Introspection: Binder (+17 points) and Anthropic 2025 (about 20% detection) versus Huang (self-correction hurts) and Kapoor (prompted confidence lags). Self-prediction of short behaviours works; judging a long solution does not.

## Weak spots
- Almost all LLM results are 2022-2024 models, mostly GPT-3.5, LLaMA-2, 52B Anthropic; very few frontier reasoning models (only Yoon, DeepConf).
- Human data in the pack is thin: only Fleming 2010 and Rollwage 2018 plus procedure papers. Replications of the BA10 structural finding were not collected.
- Several claims rest on one paper (K04, K05, K09, K10, K13, K14, K16) and are marked single-source.
- Aggregation numbers (Taubenfeld, DeepConf, Aggarwal) are the authors' own and benchmark-specific (MATH, AIME, GSM8K).

## Only seen in snippets or not opened
a07 (Meyniel 2015), b27 (Geng survey, abstract only), c12 (Farquhar 2024 Nature), c25 (Griot 2025), c20 (first 100k of 403k chars), a16 (no scores extracted), a24 (no data), c05 and c16 (no numbers), a26 (no numbers).

## GAPS
1. Does sample agreement (k=3 to 10) still beat self-report as a failure predictor for current reasoning models (2025-2026) on hard tasks, and where does the gain saturate at equal tokens?
2. What is the AUROC of end-of-chain verbalized confidence versus agreement for frontier reasoning models, and does it hold across domains (code, math, open-ended)?
3. Does an external check (tests, tool) beat any internal confidence for deciding when to revise, and can confidence gate when a check is worth its cost?
4. Does hiding the model's own earlier answer during review reduce the overconfidence/anchoring effect (Kumaran) in an agent loop, and by how much?
5. How well do semantic-entropy or cluster-agreement signals work for long, multi-step agent outputs where answers cannot be matched exactly?
6. Is calibration stable across task types so that a per-type calibration table (memory) transfers, or does it need re-fitting per task?
7. Has the human BA10 / metacognitive-efficiency finding replicated at larger N, and what does that imply about confidence being a separable skill rather than a by-product of accuracy?
8. Can confidence-weighted early stopping (CISC, DeepConf-style) be done on a black-box API without token logprobs, and what is the loss?
9. Do final-answer hedging and tone track internal uncertainty after RLHF, or only after explicit alignment (Steyvers, Zhou)?

## Gap search results (evidence_d.jsonl d01-d19; claims K19-K27 added, K02, K06, K13 updated)
1. Agreement vs self-report for reasoning models: CLOSED, answer reversed. For three 2026 reasoning models (Del d01) single verbalized confidence beats self-consistency at equal samples (math SC@2 70.5 vs VC@2 73.5; VC@1 78.8); agreement helps mainly in combination (+12 AUROC with 2 samples, d02); gains saturate near K=5 outside math. In small open models SC (0.82) still beats VC (0.67) (d05). K06 set to contested. Still open: equal-token comparison beyond gpt-oss-20b, and non-math hard tasks (code agents).
2. End-of-chain verbalized confidence vs agreement across domains: MOSTLY CLOSED. VC@1 AUROC 78.8 math, 73.8 STEM, 68.5 humanities (d01); code agents near chance 0.51-0.64 (d09); 33-model atlas shows large domain spread (d04). Open: no frontier open-ended or code-chain head-to-head with agreement.
3. External check vs internal confidence: PARTLY CLOSED. Execution gating cuts error 65% to 2% (d11); revise with checkable constraints works, open reasoning flips up to 13.25% (d08); agents' own success estimates near chance (d09). Open: no paper found that prices a check against a confidence-gated trigger.
4. Hiding own earlier answer: STAYS OPEN. Only indirect support: bug-finding framing cuts overconfident failures 72% to 45% (d10); multi-turn self-anchoring drift is model-specific (d12). No isolated hide-vs-show test beyond Kumaran 2025 found. Needs our own A/B.
5. Semantic entropy for long, multi-step outputs: PARTLY CLOSED. Claim-level methods work for long-form facts (SeSE, d16) and ranking collapses at atomic level but works at line level (SALT, d15); no test on multi-step agent trajectories except TrACE (3B model, n=30-50, d06). Open.
6. Calibration stability across task types: CLOSED as "does not transfer evenly" (d04: domain AUROC .742 vs .652-.658, cell CI width .199, profile shape varies even within Anthropic generations). A table needs coarse types and per-model refits.
7. Human BA10 replication: PARTLY CLOSED. Lesion study (n=7, d17) shows causal but domain-specific role; N=308 fMRI (d18, abstract only) shows prefrontal link but as activation decrease. No direct large-N structural replication found. Implication: monitoring is a separable, domain-specific component, not a by-product of accuracy; still evidence is small-N.
8. Black-box early stopping without logprobs: PARTLY CLOSED. CGES (d07) saves 58% of calls but needs logprobs or a reward model; count-based Adaptive-Consistency (earlier evidence) is the logprob-free option; verbalized-scalar loss untested. Open.
9. Hedging/tone vs internal uncertainty: CLOSED for 2024 models (d13: cMFG 0.52-0.57 vs 0.5 baseline) and models do not act on stated confidence (d14). Open: no post-2025 re-test of Yona's metric on current RLHF/reasoning models.

Caveats on the new evidence: mostly single-author or preprint 2026 papers, small n for agent studies (d06, d19), and Molenberghs (d18) read as abstract only. Not re-opened: Steyvers, Zhou.
