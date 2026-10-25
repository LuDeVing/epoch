# Critique and cross-check: A04.03 Accuracy and dissociation of monitoring

## Re-checked numbers (PDF text re-read this session)
Confirmed against the source text or tables:
- Xiong et al. 2024: GPT-4 average AUROC 62.7%; ~22.2% AUROC gain GPT-3 to GPT-4; ECE above 0.377 for GPT-3, GPT-3.5, Vicuna; GSM8K GPT-4 CoT 93.6% accuracy with ECE 0.064 from all-100% confidence; GPT-3.5 GSM8K AUROC 54.8 to 92.7 with 5 samples plus consistency; best ECE 0.028; five-dataset average 56.4 to 73.0.
- Tian et al. 2023 gpt-3.5 table: TriviaQA label prob ECE 0.140, verbal top-1 0.068, top-2 0.050; SciQ 0.256 vs 0.234/0.132/0.065; TruthfulQA 0.451 vs 0.389/0.361/0.203; 2-stage CoT TriviaQA 0.110. GPT-4: TriviaQA label 0.078 vs verbal top-1 0.024 (AUC .950 vs .937); SciQ label 0.219 vs top-4 0.056; TruthfulQA AUC label .462.
- Kuhn et al. 2023 Table: CoQA 1.27 vs 1.77 distinct answers, AUROC .77 vs .66; TriviaQA 1.89 vs 3.89, .83 vs .79.
- Zhou et al. 2024: 53% correct with strengtheners, 32% with weakeners, 17% of wrong answers had strengtheners, 47% error among confident responses, reward scores 4.03 / 0.82 / -1.86, 125,244 queries, 284 questions.
- Steyvers et al. 2025: AUC .751, .746, .781 (model) vs .589, .602, .592 (humans, default explanations); per-experiment ECE values in c20 match the table (human .264 / .291 default; model .104 / .154).
- Yoon et al. 2025 ablation (Table 4): original TriviaQA ECE .042, non-linear reasoning removed .161, no CoT .150; NonambigQA .195 / .341 / .359. GLM-4-32B TriviaQA ECE .150 to .029 appears in Table 6.

## Corrections and cautions
1. b17 pairs "model ECE 0.104, human default 0.291, human modified 0.225" as one example. In the source table 0.104 is GPT-3.5 model confidence while 0.291 and 0.225 belong to the PaLM2 experiments (1b, 2b). Use c20 (per-model) instead of b17 for ECE.
2. c13 Qwen3 and Qwen2.5 TriviaQA ECE pairs (.207 vs .063; .129 vs .042): the pdftotext table is misaligned, and identical rows (0.768 / 0.063) appear under several model names. The direction (reasoning mode lower ECE) is clear; the exact model-to-row pairing is NOT confirmed. Do not quote the pairs without opening the PDF figure/table image.
3. a22/b09: the 92.7% AUROC cell appears in both the "Prompt (M=5)" and the "Self-Random + consistency (M=5)" rows. Say "5 samples with consistency", not a specific aggregator.
4. a05: Koriat's within-person gamma .47 (consistently correct) vs .24 (consistently wrong) conflicts with the claim of a negative correlation for consistently wrong items; this is probably within-person vs across-item statistics. Unreconciled; kept K05 as single-source.
5. Not re-opened (still unverified): Rhodes and Tauber g=0.93 / 0.08 (a14, b25: only snippet-level or abstract; Crossref gave no abstract), Kruger and Dunning 12th vs 62nd percentile (a11), Gigerenzer 53/56 vs 72/75 and Juslin 95/35 points (a08, a09: secondary summaries), Healy and Moore (b21 read, but the z=22.83 looks like a score-difference test, not a bias statistic).

## Contradictions between sources
- Hard-easy effect: Gigerenzer / Juslin (selection artefact) vs Moore and Healy (noise plus Bayesian) vs Koriat (reliability-validity gap). All explain overconfidence on hard sets but disagree on cause; no source tested them head to head on LLMs.
- Dunning-Kruger: Kruger and Dunning (quartile pattern) vs Gignac and Zajenkowski, Dunkel et al. (mostly artefact, linear). Gignac still found a large mean gap (d = 1.71), so "mostly artefact" is not "no bias".
- Verbalised confidence: Tian says verbal beats token probs (RLHF models), Kapoor says verbal discriminates but is badly calibrated, Xiong says verbal discriminates little (AUROC ~ chance). These differ by model, dataset and metric (ECE vs AUROC).
- Reasoning models: Yoon (reasoning improves calibration) vs Hiremath (accuracy and ECE move apart in one small model; only 47 questions) vs Ghosh and Panday (strong reasoning-class models still show ECE .185 with 99.5% confidence).
- Self-correction: Huang (hurts without oracle) vs ConfTuner and the verbal-self-verification preprint (gains after training).

## Weak spots
- Most LLM evidence is from 2022-2024 models (GPT-3.5, GPT-4, LLaMA 2). Only c17-c19 and c22 cover newer models, and these are single preprints.
- Human literature is entered mainly from abstracts and theory (a01, a03, a12, a15, a16, a17 not opened or numbers not extracted). Coverage of Thompson's feeling of rightness has few numbers.
- Evidence entries b01-b05 are the same Kadavath paper split by finding; counted as ONE independent source in claims.
- Several 2026 entries (c15, c17-c19, c30, b23) are unreviewed preprints; treat sizes as provisional.
- Nothing here tests confidence signals inside an agent loop (multi-step), only single-question QA.

## GAPS (most decision-relevant first)
1. At equal tokens, does agreement among k short samples beat one long reasoning trace with verbalised confidence as a trigger for verification, on multi-step tasks like ours (not QA)?
2. How well does confidence given AFTER reasoning (and after a fresh re-solve, the LLM analogue of the delayed-JOL effect) discriminate compared with confidence given before or immediately after the answer, for current reasoning models?
3. Is there a cheap fluency or conflict signal (token entropy, early-sample disagreement) that plays the role of the feeling of rightness and can gate re-examination without extra samples?
4. How large is the confidently-wrong-and-consistent failure (reliability without validity) in current models, and what catches it (external check, different-method re-solve)?
5. How stable is calibration across task type and distribution shift for the same model, and how many held-out items does a post-hoc recalibration map need (no training allowed)?
6. Does the hard-easy effect appear in LLMs on representative item mixes, or is it a sampling artefact as in humans? Needed to decide whether a difficulty-dependent confidence correction is worth building.
7. Do the Qwen3/Qwen2.5 thinking-vs-non-thinking ECE pairs in Yoon et al. hold when read from the actual table image or released data, and does the effect hold on closed frontier models?
8. What do the original sizes in Rhodes and Tauber (delay meta-analysis) and Kruger and Dunning look like when read in full, and do they transfer to LLM judge-of-own-answer setups?
9. When confidence is wrong, does the agent's action actually change with it (confidence faithfulness in decisions), in a multi-step agent rather than single abstain decisions?

## Gap search results
Evidence in evidence_d.jsonl (d01 to d18). Web search quota ran out partway; Semantic Scholar and OpenAlex were rate limited, so the search was limited to papers already known or reached through direct links. Several PDF downloads were truncated, so many entries were read through page extraction (marked in the limits field).

1. Agreement of k samples vs one long trace at equal tokens: PARTLY CLOSED, QA only. On fact retrieval one long trace with a stated score matches 10-sample semantic entropy at about equal tokens (d01, one model, 270 items). In agent tasks agreement of 3 to 5 runs beats verbalised confidence (AUROC 0.65 to 0.74 vs 0.48 to 0.55, d09) but costs k times the tokens, and no paper compares at equal tokens on multi-step tasks. Open.
2. Confidence after reasoning vs before or right after: PARTLY CLOSED. Confidence after no reasoning is near chance (AUROC 0.56), after 100 to 500 tokens 0.80 (d01); thinking mode raises AUROC 0.650 to 0.807 on Qwen3 (d02). In agents, asking before the work was as good as asking after (d07, not significant). No test of a blind re-solve with a current reasoning model; the human cue result (d17) says the re-solve should not see the first answer. Open.
3. Cheap fluency or conflict signal: PARTLY CLOSED. Local token-confidence and early-window agreement work as stop triggers (d06, d12), but neither was tested as a gate for re-examination, and both are fluency cues that miss confident-wrong traces. Hidden-state probes (d13) need internals. Open for a scaffold-only agent.
4. Size of confidently-wrong-and-consistent failure: CLOSED enough. 5.5% to 10% of agent tasks (d09); 8% to 28% of GPQA items by tier, and 48% wrong at consistency 0.8 or above for gpt-4.1 (d10); cross-family wrong answers overlap more than chance. Not fixed by more samples or another model family. What catches it was not measured; the argument is for an outside check or a different-method re-solve. Catch rate: open.
5. Stability across task type and shift, and map size: PARTLY CLOSED. Per-slice beats global (d11); agent calibrators transfer partly (d05). The number of held-out items for a count-table map without training is not measured anywhere; 5 to 20 per slice helps a trained recalibrator, several hundred trajectories per domain used for a trained one. Open.
6. Hard-easy effect in LLMs: PARTLY CLOSED. Appears in 11 models (d04), with a much smaller slope for reasoning models (0.168 vs 0.732). Cause untested, item sets not representative, no coefficients' uncertainty. K03 stays contested.
7. Yoon et al. pairs: CLOSED for the open models. Table read: Qwen3 0.207 to 0.063; Qwen2.5 0.129 to 0.042 (d02). Caveat: the Qwen3 Thinking row equals the QwQ row cell for cell. Closed frontier models: still open; d03 shows the effect is not universal (factual QA, small models).
8. Rhodes and Tauber, Kruger and Dunning: PARTLY CLOSED. Headline numbers confirmed from abstract records (g=0.93 on 4,554 people, g=0.08 on 3,807; 12th vs 62nd percentile). Full text and moderator tables not read. Transfer to LLM self-judging: no direct test.
9. Does action change with stated confidence in a multi-step agent: PARTLY CLOSED. Yes in coding agents: decisions follow a threshold on stated probability (d08), and overconfidence rises with steps. Not tested for verify or abstain choices inside a single long agent loop.

Corrections to earlier cross-check items: item 2 above is resolved (see gap 7). Item 5 is partly resolved (Rhodes and Tauber and Kruger and Dunning headline numbers now confirmed from abstracts).

## New contradictions and cautions
- Michael et al. (d04) say regression to the mean is the likely cause of the hard-easy effect but test nothing. Consistent with Moore and Healy, still no head-to-head test.
- Yoon (d02) vs Zeng (d03): reasoning improves calibration vs worsens it on factual QA for small open models. Task and model set differ.
- Kaddour (d07): pre-run prediction was as good as post-run review, which conflicts with the idea that checking after work gives more information; differences were not significant at N=100.
- Behavioural consistency (d09) vs the GPQA audit (d10): agreement is useful in agent tasks (AUROC up to 0.78) but only weakly tied to correctness on hard multiple-choice items (Spearman 0.20 to 0.59).

## Still open after the gap search
Equal-token comparison on multi-step tasks; blind re-solve with a reasoning model; whether a cheap trigger gates re-examination; catch rate for consistent-wrong failures; held-out size for a counting-table recalibration; closed frontier models for the thinking-vs-non-thinking effect; LLM transfer of delayed-judgment effects. These need our own tests; the agent_test lines of K20 to K27 describe them.
