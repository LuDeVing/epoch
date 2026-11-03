# C01.06 Cross-check: Learned refinement and self-verification

Checked by re-reading the PDFs (pdftotext) of ReVISE (2502.14565), SCoRe (2409.12917), Huang et al. (2310.01798), Tyen et al. (2311.08516), Snell et al. (2408.03314) and Self-Correction Bench (2507.02778).

## Corrections made
1. a11 labels the SCoRe MATH result as Gemini 1.0 Pro. Wrong. SCoRe fine-tunes Gemini 1.5 Flash for MATH and Gemini 1.0 Pro for code (paper, Models paragraph). b06 and b07 are right.
2. a12 labels SCoRe HumanEval as Gemini 1.5 Flash. Wrong, it is Gemini 1.0 Pro. The numbers (52.4 -> 64.6, +12.2; Self-Refine -1.2; Pair-SFT -1.8) are correct. The base-model row "53.7 -> 56.7 (+3.0)" is the base on HumanEval/MBPP-R table.
3. c08 says "absolute self-correction gain of 15.6% on MATH". It is the gain in the delta (SCoRe +4.4 minus base -11.2), not an accuracy gain. Real accuracy at turn 2: 64.4 vs base turn 2 of 41.4. Do not quote 15.6 as accuracy.
4. a03/c24 (ReVISE headline 27.1 -> 31.1 and 33.2 -> 36.0, Maj@3) confirmed in text, but they compare against a vote baseline and are not the strict Maj@1 control. Use the Table 1 Maj@1 gaps (+1.9 to +2.8) as the honest number.

## Confirmed (re-opened, matches)
- ReVISE Table 1: 1B GSM8K 28.1/32.8, RFT 26.2, STaR+ 26.2/29.9, SFT 22.1; 8B GSM8K 61.6/69.2 vs STaR+ 59.2/64.9; 8B MATH-500 33.6 vs RFT 30.8.
- ReVISE AUROC 76.0 vs V-STaR 69.5; DPO removal -10.3; 22.6 -> 28.1 with curriculum; 33.9 vs 33.2 vs 32.7; Maj@64 37.7; 23.2 vs SCoRe 23.0 at "x30"; 50,000 generations.
- Huang Table 2 oracle (75.9 -> 95.5, GPT-4 84.3 -> 97.5), Table 3 (74.7, 41.8, 89.0), debate table (76.7; 82.5/85.3/88.2; debate 83.2/83.0).
- SCoRe MATH 60.0 -> 64.4, +4.4, ic 5.8%, ci 1.4%.
- Tyen GPT-4 52.87. Snell 38% correct answers turned wrong. Self-Correction Bench 64.5 / 76.0 / 89.3 / 5,306.

## Contradictions between sources
- Huang/Jiang/Tyen (model cannot judge) vs Liu et al. (b14: works at T=0 with fair prompts). Liu's own numbers are flat (+0.08), so they show "no harm" not "gain".
- Self-Correction Bench says the ability exists (fixes user-attributed errors; Wait helps) vs Tyen/Jiang saying it does not. Possible reconciliation: injected obvious errors are easier to spot than natural ones. Unresolved.
- RL papers (S2R, DeepSeek-R1) show large gains; Yue et al. (a28) says pass@k shrinks. Both can be true: pass@1 up, coverage down.
- Evidence a22 (cross-synthesis) says trained triggers recover "about 1 to 5 points"; consistent with ReVISE, SCoRe, but all are single sources each.

## Weak spots
- ReVISE is one paper, small models (1B, 8B, Gemma 2B), gains of 1 to 3 points at Maj@1, no independent replication found, no equal-token comparison against best-of-N with the same number of samples. Its Maj@5 gain mixes refinement with voting.
- Stage 2 trains refinement on gold answers; paper admits it slightly lowers verification accuracy.
- ReVISE and SCoRe need ground-truth labels and training; our agent is a scaffold with no training, so only the idea (a read-out trigger, an asymmetry in right-to-wrong) transfers.
- Many numbers (Fig 4/5/6 bars, Kadavath AUROC, CriticBench, CRITIC, S2R detail) are abstract-level or figure-only.
- Self-Correction Bench is a 2026 single paper.

## Seen only in snippets or abstracts
a21 (Weng, per-dataset), a29 (CriticBench), a30 (CRITIC), a26/b20 beyond abstract, a25 (s1), b17 (Kadavath), b21 detail, c11, c13 (RISE), a27 (R1).

## GAPS
1. Does an independent group replicate ReVISE-style learned [stop/refine] triggers on other model families (Qwen, Mistral) and on larger models, at equal total tokens against best-of-N and majority vote?
2. What is the break-even trigger quality (precision and recall, or AUROC) at which "refine on trigger" beats "never refine" and "always sample N", given right-to-wrong rates of 1.4% to 15.8%?
3. Can a no-training proxy trigger (token logprob of final answer, answer agreement across 2 samples, self-reported P(True)) reach AUROC near or above ReVISE's 76 on reasoning tasks?
4. Does the "Wait" cue (Self-Correction Bench, s1) work as a prompted re-entry in a scaffold on natural (not injected) errors, with measured right-to-wrong cost?
5. Does a code or tool checker as S5 trigger dominate learned triggers in cost-adjusted accuracy, and on which tasks does no checker exist?
6. How do learned triggers behave on reasoning-RL models (R1-style), where long chains already self-check; is the extra refine pass redundant there?
7. Out-of-domain transfer of the trigger (ReVISE trained on MATH, tested on GSM8K gave smaller gains): how robust is it to task shift and to harder benchmarks (AIME, GPQA)?
8. Are there 2025-2026 papers that directly compare learned stop-or-refine against adaptive-compute methods (early exit, budget forcing) at matched tokens?
9. Does the Huang et al. finding hold for current frontier reasoning models (2026), i.e. is intrinsic self-correction still net-negative?

## Gap search results
Evidence: evidence_d.jsonl (d01 to d19, all opened by reading PDF text, no snippet-only lines). New claims K26 to K34; K08 raised to established; K03, K10, K11, K21, K22, K23 extended. Network was flaky (arXiv API rate-limited), so some papers were read through a few passages only; limits are recorded in each line.

1. Independent replication of learned triggers, equal tokens: PARTLY CLOSED. No independent run of ReVISE itself exists in what we found. Xiong et al. 2025 (d12), a second group with a similar learned self-verdict recipe on Qwen2.5-Math-7B and Llama-3, reproduces the size of the gain (about +1 to +3 points over single-turn DPO) but has no equal-token best-of-N arm. Mirzaei 2026 (d01 to d03) gives the equal-token test, but only for prompted methods: all self-inspection methods lose to repeated sampling up to 7B. The equal-token test of a learned trigger is still open.
2. Break-even trigger quality: CLOSED as a derivation (d19, K32), not as a measurement. Needed likelihood ratio (recall on wrong / false alarm on right) = p*d / ((1-p)*c): 0.14 to 1.58 for the earlier 1.4% to 15.8% damage range at p=0.6, c=0.15 (c assumed). The Xiong operating point (50.6% of wrong caught, 8% of right flagged) clears it. We still need our agent's own c and d.
3. No-training proxy trigger with AUROC near 76: CLOSED for math with reasoning models (d07, d08, K29): verbalized confidence at one sample 66.4 to 78.8; 2-sample hybrid adds up to +12.9. OPEN for code and small models: d10 shows entropy and verbalized confidence correlate weakly or negatively on 1B to 3B code models, and acting on them lowered Pass@1.
4. "Wait" cue on natural errors with right-to-wrong cost: PARTLY OPEN. d'Aliberti 2026 (d05) gives the only natural-error cost data: forced cue +8.41 pp net on math in a 1.5B model, but 23,500 right-to-wrong flips and no matched-token resample arm. Tsui (d14) reports no cost on correct answers.
5. Checker versus learned trigger: PARTLY CLOSED for code (d10, d11): verification-based correction was the only policy that reliably gained (+6 to +26 pp) at 2.4x to 5.9x latency; uncertainty triggers lost. Small n (HumanEval n=31). Tasks with no checker: nothing new; still open.
6. Reasoning-RL models: CLOSED in direction (d09, d04): over 90% of reflections only confirm, under 2% fix; R1 spontaneous shifts 0 to 0.25%. The extra refine pass is mostly redundant there. No learned-trigger test on R1-style models found.
7. Out-of-domain transfer: PARTLY CLOSED, weak (d13): ReVISE MATH to GSM8K keeps only +0.6 (1B) and +1.2 (8B). Nothing on AIME or GPQA found for learned triggers. Open.
8. Learned stop-or-refine versus adaptive compute at matched tokens: OPEN. Found training-free stop signals (EAT, d17: 12 to 22% fewer tokens at equal accuracy), probe early exit (a23), verifier-guided allocation (d18), reflection truncation (d09: -24.5% tokens, under -2.9% accuracy), and verify-trained models (d15). None compares against a learned refine trigger at matched tokens.
9. Huang et al. for 2026 frontier models: PARTLY OPEN (d16, d04): intrinsic always-refine still breaks correct answers, less for stronger models (o1-preview 15.6% overturned, o1-mini 34.0%, Llama-3.1-8B 58.8%; table read is uncertain). No test of 2026 frontier models found.

New cautions from this pass
- Several results compare "pass 2" with "pass 1" without a matched-token resample arm (d05); treat their gains as upper bounds.
- Several new papers are 2026 single-author or workshop papers (d01, d10); treat as single-source.
- A self-judged trigger can quietly go to zero (Reflexion on 1.5B, d02): always log trigger rate.
