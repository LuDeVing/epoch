# Critique: C12.04 Sequential analysis (cross-check)

## Numbers re-opened (arXiv PDFs, text extracted this session)
Confirmed unchanged:
1. Adaptive-Consistency (2305.11860): up to 7.9x, under 0.1% drop; MATH 73.2 vs 73.1 at 13.8 samples (3.3x); commonsense 15.8 (2.9x, -0.2); symbolic 13.1 (3.8x); Vicuna-13B 1.9x; GPT-3.5 4.4x; Cthresh 0.95.
2. ESC (2401.10480): -33.8 / -80.1 / -76.8 / -78.5 / -84.2 / -67.4 percent; MATH cap 64 samples used 42.41 (GPT-4), 52.37 (GPT-3.5), 62.48 (Llama-2-7b), accuracy deltas 0.00 to -0.02.
3. ConSol (2503.17587): AIME24 low 70.0/70.0/70.0/80.0/76.7; token cuts 63.9, 84.8, 86.2, 88.6, 88.7 percent.
4. DeepConf (2508.15260): 99.9 vs 97.0 vs 91.8; up to 84.7% fewer tokens; 43-79% range vs majority.
5. CISC (2502.06233): 41% / 46% at budgets 5 / 10; 18.6 samples to match CISC at 10.
6. Self-consistency (2203.11171): +17.9, +11.0, +12.2.
7. DSC (2408.13457): 65.29%, 56.04%, 24.81%, 21.86%; 84.8% / 96.2% agreement.
8. Johari et al. (1512.04922): fivefold Type I error at 10,000 samples; 20% power loss and 40% run-length loss beyond two orders of mixture misspecification; run-length 20% better in most settings, up to 40% in some.
9. Chen et al. (2403.02419): inverse-U shape for easy/hard mixes confirmed.

Corrections and additions:
- Morandi (2026, 2605.19193): the headline "3.7x fewer calls at 97.0% vs 99.0%" is true but misleading. The paper itself says no pairwise accuracy difference is significant (CI about 4.4 points), and the cheap one-round vote (B1, 3 calls) already scored 99.0% on GSM8K. Against B1 the governor costs more (4.06 vs 3 calls). On MMLU it used 31.96 calls, 2.1x the fixed-5 cost. Claim K22 marked contested. Accuracy order for MMLU: B1 94.4, B2 93.8, B3 94.2.
- Adaptive-Consistency average over three reasoning categories is 3.3x with 0.04% drop (intro); code-davinci-002 is 3.4x (text). c02 lists its accuracy delta as +0.0; b04 gives 69.8 vs 69.7 (-0.1). Treat as -0.1 to 0.0.
- DeepConf "mean 62.9%" token cut (c11/c24) was not found in the text; only the 43-79% range was. Do not quote the mean.
- "Up to 84.7%" is a best case on one model/dataset, not a typical figure.

## Contradictions between sources
- ConSol says SPRT beats Adaptive-Consistency on tokens; its own table shows lower accuracy for SPRT than SC on some cells (GPQA low 66.7 vs 68.2) and mSPRT higher (70.2). Gains are cell-specific, one team.
- ESC (stop at one unanimous window) saves only 33.8% on MATH, while Adaptive-Consistency saves 3.3x on MATH. Different models, caps (64 vs 40) and windows, so not comparable.
- Chen et al. say more calls can hurt; the stopping papers show no accuracy loss from fewer calls. These agree if hard items are the ones that decay with N. No paper tests this directly.
- Evidence a21/b12 says "3.7x fewer calls"; the paper's own limitations paragraph says the contrast rests on a baseline that did no better than a 3-call vote.

## Weak spots
- Wald 1945 and Wald-Wolfowitz 1948 were never opened (publisher blocked). Optimality claim is from secondary texts; the "half the samples" figure is memory.
- Armitage (14% / 19%), Pocock (0.0158), Bassler (0.71, CI 0.65-0.77) are from memory only (b24, b25). They match values I recall, but they were not read this session.
- Nearly all LLM evidence is the same family (Aggarwal, Li, Lee), on short-answer math and multiple choice. Only ConSol and Morandi use real SPRT; ConSol is a single group and a preprint.
- Cost accounting differs: samples, tokens, calls, wall time. No paper reports all four.
- Most savings are measured against a 40-sample ceiling that is itself generous. Against a 5-sample baseline the gain is much smaller.
- No evidence on correlated errors, open-ended tasks, or agent loops (c25).

## Seen only in snippets or not re-opened
RASC (a15/b14/c07), Path-Consistency (c13), Self-certainty (b17/c14), Dynamic Early Exit (c15), Answer Convergence (c16), Pandora UCB (c17), Brown et al. numbers (b19), Snell (b20), Howard et al., Ramdas et al., Grunwald et al. (read by earlier agents, not re-opened). Johari c23 was marked unopened in evidence_c but opened in evidence_a/b.

## GAPS
1. Does an agreement stop hold at equal tokens against a small fixed budget (5 or 8 samples), not just against 40? What is the false-stop rate when the model's errors are correlated (a common wrong answer)?
2. How should the stop threshold be set for our agent without labelled data: textbook SPRT (p0 0.55-0.6) vs ConSol's tuned values vs a mixture SPRT? How sensitive is accuracy to p1?
3. Does the stop rule transfer from short-answer math to open-ended answers and multi-step agent tasks, where "same answer" is not defined? What is the equivalent agreement measure?
4. Can a one-sample difficulty or agreement probe (as in DSC) route items so the stop rule is applied only where it is safe? What is its error on items where CoT and SC disagree?
5. Is the Chen et al. inverse-U real for frontier reasoning models, and where does it peak by difficulty bucket? This sets the cap N.
6. Does SPRT beat the Adaptive-Consistency posterior rule when run by an independent group, with parameter sweeps and multiple seeds? No replication exists.
7. When a verifier or test exists (code, math check), should we stop on verification instead of agreement, and what does agreement add on top (Large Language Monkeys says selection plateaus)?
8. For multi-agent debate or sequential refinement, which signal replaces vote share, and how do we check it separates useful from useless convergence (Morandi's KL diagnostic) before trusting it?
9. Is token-confidence stopping (DeepConf) usable through a hosted API without log-probs, or do verbalised confidences (CISC) match it?
10. What do Wald and Wald-Wolfowitz actually prove about expected sample size under the composite hypotheses and vote-count (non-i.i.d.) setting, and does the optimality survive the dependence between samples?

## Gap search results (evidence_d.jsonl d01-d21, claims K24-K33 added)
Web search quota ran out early; arXiv API, Semantic Scholar and OpenAlex were rate limited. Papers were opened by arXiv ID. Wald (1945) and Wald-Wolfowitz (1948) were blocked by a publisher bot-check and were not opened.

Corrections to this file:
- The DeepConf 62.9% figure is real: 62.88% (low) and 47.67% (high) mean token saving vs majority voting on DeepSeek-8B, text under Figure 7 (d08). The earlier "not found" note was wrong.
- Evidence a21/b12 "3.7x" stays contested (d18 confirms: no pairwise difference significant, MMLU used 2.1x fixed-5 calls).

Gap status:
1. PARTLY CLOSED. Against small fixed budgets (CGES, independent, 10 seeds, 7B models, calls not tokens): ASC saved 0 of 4 calls at B=4, about 1 to 3.5 of 8 at B=8, ESC/ASC about 45% at B=16 (d01, d02). Correlated errors: Helm pairs agree 60% when both wrong (d12, cross-model); Certified SC certifies the model's mode only (d04). No direct single-model false-stop rate was found. OPEN: tokens at equal cost; false-stop under a shared wrong answer.
2. PARTLY CLOSED, answer is negative. No label-free recipe. ConSol's savings used p1=0.5001 and alpha about 0.95, not textbook 0.55-0.6; its mSPRT alpha sweep spans 0.00018 (d05). Rigorous certificates are conservative (d04). Adaptive-Consistency 0.95 is hand-set (d19). OPEN: accuracy vs p1 over a wide grid.
3. PARTLY CLOSED. Free-form agreement is possible via a model-judged pick (USC, d13) but has no vote share or stop rule; agent tasks use final-state equality and agree rarely (tau-bench pass^8 under 25%, d14). OPEN: no paper tests stopping on either.
4. OPEN. DSC ranking Spearman 0.62 / 0.44 (d15); gate cost 1.9 to 3.1pp independently (d01, d02). Miss rate on CoT/SC-disagreement items not published.
5. PARTLY CLOSED. Chen et al. used GPT-3.5-turbo only (d06). Recent models show rising-then-flat, no decline (d07). OPEN: difficulty-bucket peaks for frontier reasoning models. Working cap: 8 to 16.
6. PARTLY CLOSED. Two independent groups re-ran Adaptive-Consistency/ESC/DSC (d01, d16). ASC/ESC savings replicate; ASC is fragile at high budgets. NO independent test of ConSol SPRT or SPRT vs ASC. OPEN.
7. CLOSED for the decision rule, OPEN for the numbers. Stop at first verified pass; agreement plateaus (d10) and tests are imperfect (d11). Nobody measured what agreement adds on top of passing tests.
8. PARTLY CLOSED. KS stability signal (d17) and Morandi's KL calibration check (d18) exist. Neither shown to separate useful from useless convergence on open-ended debate.
9. CLOSED (as far as evidence goes). DeepConf needs engine log-probs (d08). Verbalised 0-100 confidence gives about 30% vs 46% savings at budget 10 for CISC (d09). CISC weights votes, it does not stop.
10. OPEN on primary proofs (d20, d21). Simulation (d18) shows SPRT error rates degrade gracefully under AR(1) correlation (0.065 vs nominal 0.05 at rho 0.6). Still no source on expected sample size for dependent votes.

New cautions: CGES's threshold is tuned on the test data; Blend-ASC's metric is relative to the model's own limiting mode; table text in CGES PDF is garbled, so ESC/ASC call counts are given as ranges.
