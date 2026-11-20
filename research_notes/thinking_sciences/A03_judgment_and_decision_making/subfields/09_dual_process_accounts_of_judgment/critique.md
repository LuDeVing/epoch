# Critique: A03.09 Dual-process accounts of judgment (cross-check)

## Re-opened sources (this session, from arXiv full text via pdftotext)
Confirmed unchanged:
1. Sprague et al. (2409.12183): CoT mean gains 14.2 / 12.3 / 6.9; up to 95% of MMLU gain on equals-sign questions. Confirmed.
2. Liu et al. (2410.21333): GPT-4o 87.5 to 64.4 (-23.1); subset 94.00 vs o1-preview, 36.3 drop; face 64.0 to 51.2 (-12.8, -20% rel.); 331% rounds. Confirmed.
3. Chen et al. (2412.21187): 1,953% more tokens; 48.6% token cut; first round correct in over 92% of cases. Confirmed.
4. Weston and Sukhbaatar (2311.11829): 62.8 to 80.3, oracle 82.0, 51.7 to 61.3, 57.4%. Confirmed.
5. Yu et al. (2407.06023): 30.0 / 39.5 / 98.0; coin 56.1 / 75.69; 1-step RaR 77.2. Confirmed.
6. Lin et al. SwiftSage (2305.17390): 84.7 vs 33.8 / 36.4 / 45.3; 757.07 vs 2,983.46 tokens per action. Confirmed.
7. Su et al. Dualformer (2410.09918): 97.6 vs 93.3; 45.5% and 59.9% fewer steps; 96.6 auto. Confirmed.
8. Hagendorff et al. (2212.05206): 38% vs 41% (n=3,428); 59% / 96% / 80% / 0% / 55%; 72% semantic illusion; CoT 5 to 28 and 80 to 29; 95 to 88 without CoT. Confirmed.

Corrections and nuances recorded:
- Liu et al.: the "36.3 point drop" is o1-preview compared with GPT-4o on a subset, not CoT vs direct on one model. The matched same-model drop is -23.1 (GPT-4o). Evidence lines a23/b21/c10 should not be read as a controlled CoT effect for the 36.3 figure.
- Hagendorff: the paper reports ChatGPT-4 CRT correct as 96% in one place and 95% in another (95% is the baseline in the CoT-blocking ablation, 96% in Study 1). Treat as one number with rounding between studies.
- Yu et al.: "System 2" in a26 lists 39.5% for 2-step RaR and 44.5% for 1-step RaR on last-letter; both are recorded. Coin flip 1-step RaR 77.2 is higher than the distilled 75.69, so distillation did not beat the best System 2 variant on coin flip.
- Chen et al. exists as b18 (year 2024) and a24/c17 (year 2025): same paper, counted once.
- Duplicates: the Hagendorff paper (a19, a20, b12-b14, c01-c03, c25) and Liu et al. (a23, b21-b23, c10, c11), Yu (a26, b19, c14), Weston (a25, b20, c13), Dualformer (a28, b25, c15) are each one source. This inflates apparent corroboration across files A, B and C. Independent-source counts in claims.jsonl count papers, not lines.
- Not re-opened (time and API budget): Bouwmeester RRR (b01, b02) and Rehren meta-analysis (b03, b04), which the evidence files mark as opened; Otero et al. (b10, b11); Sinayev and Peters; De Neys et al. 2011. I did not have a second copy of these. Their numbers stand on their own file's reading.

## Contradictions between sources
- CRT human baseline: 41% (original, n=3,428) vs 38% (Hagendorff's Prolific sample); difference p=.06, so not clearly different, but the "humans 38%" line in one place compares different samples.
- Moral dual-process: Bago and De Neys two-response data (about 74% UU pairs) fit an "intuition is already utilitarian" story, while load/time-pressure studies split (Tinghog null; Gawronski and Beer reanalysis in opposite direction). Both come from one review (b05-b08) and have not been read at primary level.
- CoT effect: Sprague finds near-zero gain outside math and logic, while Kojima (a22) found large gains (MultiArith 17.7 to 78.7) on older models. The gap is a model-generation effect, not a contradiction, but it means older-model numbers should not be used for current models.
- Overthinking: Chen reports more tokens with no accuracy gain; the Hagendorff Dualformer-style results report real gains from slow mode. Task type separates them (mazes need search; 2+3 does not).

## Weak spots
- File A: 13 of 30 lines (a01-a13) are marked opened:false and rest on memory (Evans 1983 acceptance rates, Wason and Evans, Frederick 2005 per-site means, Hagger et al. 2016 d about 0.04, Bago and De Neys 90%). None of those numbers were verified. In claims they only support status "single-source" or "contested".
- Human-side evidence is thin on primary founding studies: Kahneman and Tversky 1983 Linda, Frederick 2005, Stanovich and West and the Evans and Stanovich 2013 debate are cited as reviews or from memory, not opened.
- Moral-judgment section depends on one 2025 review (Untested Assumptions...), not on its primary papers.
- LLM studies use different model families, mostly closed models (GPT-3 to GPT-4, o1) that have since changed; no study holds tokens constant between fast and slow arms, so the agent test must do so.
- Claims of the kind "System 1/System 2 for LLM" mostly define System 2 as "more tokens", which is not an independent test of the dual-process theory.
- Snippets only: none of the files were from snippets alone as far as the opened flags show, but the 2026 Zhang et al. (c18), Ziabari (c20), Lin (c21) and Li (c22) lines were not re-opened here.

## GAPS
1. At equal total tokens, does a routed fast/slow scheme beat both always-fast and always-slow on a mixed task set, and how much does mis-routing cost? (No study holds tokens equal.)
2. Which cheap signal best predicts that slow reasoning will hurt (implicit-pattern, perception, exception-heavy tasks): model confidence, task class, or a direct-vs-CoT disagreement check?
3. Do first-answer-then-verify steps change correct answers to wrong ones in modern reasoning models, and how often does verification fix a wrong first answer? (The 90% intuitive-correct human figure was not verified.)
4. Is the confidence drop on conflict items (De Neys) reproduced as a usable trigger in LLM verbalised or logit confidence, and is it calibrated after instruction tuning?
5. Can System 2 Attention style context cleaning be matched by a single-pass instruction at equal tokens on current frontier models? (Original gap: 80.3 vs 71.7 on LLaMA-2-70B.)
6. How does contamination affect CRT and heuristics-and-biases items for current LLMs, and do perturbed or novel items restore a measurable trap rate?
7. Verify the founding numbers in file A that were from memory: Evans et al. 1983 belief bias rates, Frederick 2005 per-site scores, Hagger et al. 2016 ego depletion effect, Bago and De Neys 2017 two-response percentages.
8. Does the moral-judgment null pattern (g=0.06, trim-and-fill -0.02) extend to non-moral reasoning load and time-pressure manipulations, and does a token-budget limit on LLMs behave like time pressure for humans?
9. Which dual-process variant (default-interventionist, parallel-competitive, three-stage) predicts LLM error patterns better, using the same items for humans and models?

## Gap search results
Search tools were limited: WebSearch budget ran out after two calls, and the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. Sources were opened by direct arXiv PDF download (evidence_d.jsonl, d01-d16).

- Gap 1 (equal-token routing): STILL OPEN. ThinkSwitcher, SynapseRoute and ADR show routing saves 20-60% tokens at about equal accuracy, but none holds total tokens fixed against always-fast and always-slow. Mis-routing cost is visible only as the BERT router's accuracy loss (d09). Claim K20.
- Gap 2 (cheap signal that slow will hurt): PARTLY CLOSED. Verbalised confidence is weak (GPT-4 AUROC 62.7%); 5-sample agreement is strong (GSM8K 92.7%) but costs 5x tokens and was not tested for predicting CoT harm (d05, d13). Claim K19.
- Gap 3 (verify flips): PARTLY CLOSED for 2023-24 models. Self-verification lowers accuracy and flips right answers to wrong; external verifiers help (d01-d04, d15). Modern RL-trained reasoning models and the human 90% figure remain untested. Claim K18.
- Gap 4 (confidence drop trigger): OPEN. Average calibration after RLHF is fine (d06) but failure separation is poor (d05); no LLM replication of the De Neys conflict-item drop found.
- Gap 5 (S2A vs single instruction): PARTLY CLOSED. A one-line ignore-irrelevant instruction matches example-based prompting on old models (d07, d14); no equal-token test on a frontier model. Claim K06 amended.
- Gap 6 (CRT contamination): PARTLY CLOSED. GPT-3 evidence of brittleness on perturbed items (d08); no systematic perturbed-CRT study on current models was reached. Claim K22.
- Gap 7 (verify founding numbers): STILL OPEN. Frederick, Evans, Hagger and Bago and De Neys PDFs were not reachable (d16). K17 stays single-source.
- Gap 8 (time pressure vs token budget): PARTLY CLOSED on the LLM side only. Prompted budgets are overshot (d12); a hard cap analogue is untested. Claim K21.
- Gap 9 (which dual-process variant fits LLM errors): OPEN. Nothing new found.
