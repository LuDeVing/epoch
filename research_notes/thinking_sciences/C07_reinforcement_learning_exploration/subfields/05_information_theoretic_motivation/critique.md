# C07.05 Information-theoretic motivation: cross-check critique

## Numbers re-opened this session (full text via pdftotext)
Confirmed unchanged:
1. EELMA (2509.22504): CoT removal drops empowerment 0.19 to 0.01 bits (Gridworld, 99%) and 0.29 to 0.09 (Hanoi, 65%); 43/106 Qwen jailbreak trajectories; NL RMSE 0.302 / 0.438.
2. UoT (2402.03271): 38.1% average, 46.6% Llama3-70B, GPT-4 troubleshooting 43.7 to 67.3, CoT-SC 33.8, Reflexion 29.9, Original-ToT 28.3.
3. BED-LLM (2508.21184): +37.4 percentage points, more than doubling in over half of setups, never decreasing.
4. Pan et al. (2501.18009): 720 elements, 500 trials; 9 / 25 / 35 / 42 (human) / 85 / 177; o1 t = 9.71; empowerment beta 0.196, z = 1.067, p = 0.286; empowerment signal peaks at layer 72 (r = 0.55).
5. Ellis et al. (2510.13709): 78% preferred, p = 0.015; acceptance 8.08% vs 6.18%, p = 0.0002; 208 vs 333 suggestions; 192% average gain over SFT; 554 LiveCodeBench questions.
6. Krishnamurthy et al. (2403.15371): only one configuration explored well; basic GPT-4 suffix failure in over 60% of replicates.
7. Massari et al. (2107.07031): no significant time-to-success difference with all runs kept; significance appears only after removing one 1e7-frame outlier.
8. Shoot First (2510.20886): Scout F1 0.367 to 0.764, GPT-4o 0.450 to 0.782, GPT-5 0.716, win rate 0.67 vs GPT-5, 1% of cost.
9. Hartmann et al. (2607.03426): +4.2 and +1.8 points on the 14B model; 25x to 36x faster than BED-LLM.
10. Lidayan et al. (2503.23631): 51 children; goal-statement correlation 0.8, p = 0.005.

Corrections and qualifiers:
- a25/b05 UoT 38.1%: evidence line a25 called it "relative". The paper text says only "improvement of 38.1% in the rate of successful task completion". Treat as unspecified (relative or absolute) and do not compare it with BED-LLM's +37.4 percentage points. The other UoT gaps (33.8, 29.9, 28.3) have the same ambiguity.
- c07 correlation r = 0.8: the paper itself says "p = 0.005 unadjusted". It is based on the 17 children who produced private speech. Treat as a hypothesis, not a result.
- c10 "more than doubles Pass@1" and "192% average gain" are different statements from different tables (Llama-8B vs average over models). Both are in the paper; do not merge them.
- b03 Spearman 0.83-0.94: these are per-domain values; b04 shows the overall WebArena figure is only 0.39 and visitation entropy is close behind in places. The headline correlation is domain-selective.

## Contradictions between sources
- Empowerment as exploration driver: strong in gridworld demos (a02, a09, a11) and in human play (c05) but weak or null in deep RL comparisons (b19, c08, b23, b24). The positive results are mostly qualitative figures; the negative ones are small-N statistics. Neither side is decisive.
- Explicit EIG helps in LLM question asking (b07, c12), while whole-pipeline "reasoning wrappers" hurt (b06). The common reading is that computation outside the model matters, not reasoning inside it.
- Pan et al.: LLMs ignore empowerment; EELMA: empowerment tracks LLM-agent success. These are not in conflict (different questions), but nobody has tested whether prompting a model to follow empowerment changes performance; Pan found prompts did not.
- Expected free energy (a18, b26) is contested by its own community, while a20 uses it successfully; practice outruns theory.

## Weak spots
- Almost every LLM EIG result is on 20 Questions style closed sets (animals, celebrities, things), 100 targets or fewer per cell. Generalisation to open reasoning probes is untested.
- BED-LLM, UoT and Shoot First use extra model calls and code. None reports results at equal total tokens, which is the comparison our agent needs.
- Empowerment-based LLM studies (b01, c01) are each single-lab single-source.
- Results in 2026 preprints (b11, b13, b22, b24, c12, c19) have not been through peer review.
- No study tests a probe-selection step inside a long chain of thought on maths, code or ARC items.

## Seen only in snippets or not opened
a21 (Tschantz scaling), a23 (Still and Precup), b28 (Klyubin 2005 founding paper), b29 (Friston), b30 (Ruggeri and Lombrozo), c24 (Demircan), c25 (Brandle et al.). Lindley (1956) was read via secondary citation only (a24). The a16 RND table row is unlabelled. The b17 numeric results were not extracted. No claim in claims.jsonl rests only on these, except that K01 relies on reviews rather than the 2005 paper.

## GAPS
1. At equal total tokens, does explicit EIG probe selection (sample hypotheses, score partition) beat self-consistency voting on open reasoning tasks, not just 20 Questions?
2. How many sampled hypotheses are needed for a stable EIG estimate before more samples stop paying, and what is the token cost curve?
3. Where does the cheap proxy (predictive entropy of the answer) fail versus full EIG when probe answers are noisy, as with code execution or tool output?
4. Does adding an explicit option-count (empowerment) hint to probe choice help LLMs, given that prompting alone did not fix Little Alchemy 2 behaviour?
5. Is the UoT 38.1% relative or absolute, and does it survive when the baseline gets the same number of calls (self-consistency at matched budget)?
6. Can EELMA-style empowerment estimated from our own reasoning traces serve as a cheap monitor (G-level) that predicts failure, and does it beat simple trace statistics outside WebArena?
7. Do free-play findings (goal-stating improves exploration, c07) replicate in larger samples, and does a goal-stating step help an LLM agent?
8. Which probe-selection failure appears first in long contexts: poor hypothesis sampling, miscalibrated answer model, or ignoring history (raw in-context beliefs were incoherent)?
9. Does the EIG advantage vanish for soft-target tasks (b09), and how do we detect at runtime that a task is soft?
10. What is the right stopping rule: when does the expected information gain of the best probe fall below the cost of asking it?

## Gap search results (evidence_d.jsonl, d01-d17)
Method: full text of 11 papers read via arXiv PDFs and pdftotext. WebSearch quota was exhausted and arXiv/OpenAlex/Semantic Scholar search APIs returned 429, so I followed citations from papers already in the folder; no new literature search was possible. Papers not named in this folder (for example other work on self-consistency for question asking) may exist.

Closed or mostly closed
- Gap 5 (UoT 38.1%): closed. Recomputing Llama3-70B from Table 1 gives a mean per-cell RELATIVE gain of 46.61%, the paper's 46.6%; the mean absolute gain is about 10.1 points (d01). So 38.1% is relative. Do not compare it with BED-LLM's +37.4 percentage points. The 33.8, 29.9, 28.3 gaps were not recomputed (the GPT-4 table rows are garbled in the PDF text) but are very probably the same type. The matched-budget part is partly answered: at about 4.6k tokens, pruned UoT scored 48.1/88.4/63.2 against CoT-SC (k=33) 32.6/37.6/42.5 (d02). That SC votes on the next question, not on the final answer, so it is not the baseline our agent needs.
- Gap 3 (proxy vs full EIG): mostly closed for 20Q. Entropy-only was below full EIG in 18 of 18 BED-LLM cells (mean 57.6 vs 70.7) and full EIG costs no extra calls (d03, d05). Derivation (mine, from d09 eq. 4): with one constant noise rate, entropy and EIG rank probes identically; the proxy fails only when noise differs by probe, as with crashing code or unreliable tools. With an execution oracle noise is near zero (d08). Not tested: mixed-reliability tool outputs.
- Gap 2 (hypothesis count): partly closed. Ranking of 5 candidates was stable at 10 hypotheses vs 85 (one game, d04); papers use N=15 to 20 hypotheses and M=5 to 15 candidates (d04, d07); best-of-M scoring keeps paying up to about M=10 (d09). No token-cost curve exists in any paper.
- Gap 8 (first failure in long contexts): partly closed. The hypothesis set breaks first: unfiltered in-context beliefs gave 26.8 vs 30.3 prompt-only; 200 samples mode-collapse (d06); history-ignoring is general (d16). Not isolated one by one, and contexts are 20 turns or less.
- Gap 7 (free play): corrected, not replicated. The r=0.8 uses N=10 children (at least 5 utterances), not 17; 17 had transcripts, 26 were analysed, 51 recruited; goals labelled by gpt-3.5-turbo (d13). ELLM found no significant gain from goal-conditioning the policy (d14). No test of a goal-stating step in an LLM scaffold found.

Still open
- Gap 1 (EIG vs self-consistency at equal tokens on open reasoning): open. Only closed-set 20Q/diagnosis (d02) and code with an oracle (d08, no token-matched baseline). Strong models gain less (GPT-4o-mini, GPT-5: d07, d09).
- Gap 4 (option-count hint): open. The Pan et al. prompt test used verbal advice on GPT-4o only (43 vs 35 elements, p=0.304; d10). A computed count shown per candidate is untested.
- Gap 6 (empowerment as failure monitor): not supported yet. Beats simple statistics in aggregate (WebArena 0.39 vs 0.16, N=16; tau-bench 0.71, N=6) but no per-run prediction, and it inverts at floor performance (d11, d12).
- Gap 9 (soft targets): partly open. Entropy gave no gain and Prompt-Only was a stronger baseline in preference elicitation, with the BED-LLM boost clearest across different model classes (d05); size not extracted. The runtime softness test is my proposal, not tested.
- Gap 10 (stopping rule): open. Only CuriosiTree gives a rule (confidence threshold plus cost weight lambda=0.1, 50 trials, one diagnosis; d15). Theory covers noiseless cases only (d17). Kobalczyk et al. name it as future work.

Claims changed: K10, K11 (rewritten: relative, matched-budget table), K13 (noisy vs constant noise), K16 (strong-model boundary), K18 (what the prompt test did), K19 (baseline comparison), K21 (N corrected to 10), K22 and K14 (evidence added). New: K26 to K30.
