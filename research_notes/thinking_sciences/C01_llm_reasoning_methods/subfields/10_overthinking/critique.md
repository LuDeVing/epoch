# C01.10 Overthinking: cross-check critique

Sources re-opened (full text, this session): Zhou et al. 2026 (arXiv 2604.10739), Gema 2025 (2507.14417), Ghosal 2025 (2506.04210), Hassid 2025 (2505.17813), Ma 2025 (2504.09858), Cuadron 2025 (2502.08235), Chen 2024/25 (2412.21187), Wu 2025 (2502.07266).

## Confirmed
Zhou: Table 1 accuracies (37.8/46.5/50.2/53.8/55.8/54.9 R1; 33.2/41.8/44.5/47.1/47.6/45.8 s1), Table 2 flip counts and ratios (0.22 at 1K ... 7.55 at 16K), Table 3 CIs, Table 4 indicators, Table 5 GPQA (peak 55.6 at 10K), Table 6 natural vs forced, Table 7 (54/16/10 of 80). Ghosal 82.2->87.3->70.3 and 11.8% drop. Hassid LN-Super 69.1 vs 57.6, 75.8 vs 63.1, 34.5 gap, 40% and 33%. Ma 51.3 vs 28.9 at 700 tokens. Cuadron 29.1%/$1,400, 21.0%/$400, 27.3%/$800, 43%, Spearman 0.800. Chen 1,953%, 92%, 287 tokens/38.7%, ASDIV 741.8->381.6. Wu 14 -> 4 steps. Gema Sonnet 4 60%->47%, 2,500 questions, study-hours correlation 0.73.

## Corrections
1. a02: the 7K "p=0.038" is not in Zhou Table 3; the p-value cell for 7K is blank and the CI is [1.01, 1.18]. c02 repeats p=0.038. Treat as unsupported. The 6K CI [0.71,1.05] is correct.
2. Zhou Table 2 vs Table 3 ratios at 2K: 0.32 (not 0.22); 0.22 is at 1K. b02 is right; a-line summaries that quote 0.22 at 2K should not.
3. Gema model count: a07 and b07 say nine, c05 says ten. Paper text says "all nine models tested" in one place. Use nine, flag the ambiguity.
4. Ghosal parallel gain: abstract says "up to 20%", intro says "up to 22%". Both appear in the paper.
5. Chen token cuts: 22.3% (SimPO, MATH500, preference-method comparison) and 48.6% (abstract, FCS+Reflection with QwQ) are different quantities; a12 conflates them as one result. Also the first-round-correct statement is "more than 92% of cases", not of all items.
6. Cuadron count: 4,018 trajectories analysed, 3,908 scored (a24 flags the survey mismatch; confirmed).
7. a03 vs c03: MATH-500 optima are read from a figure (L2 about 3.0K in a03; c03 groups L1-2 as 1-1.5K). Figure-read; treat as approximate. Text only guarantees L1 = 1.0K and L5 = 7.5K.

## Contradictions and weak spots
- The headline effect in Zhou is tiny: 55.8 -> 54.9 from 12K to 16K is 0.9 points, about half of one problem of 60 on AIME. The flip ratio rises steeply because positive flips shrink (83 -> 11) while negative stay low in absolute terms. Ratios are cumulative from the threshold, and one problem can count many times, so the bootstrap CIs understate uncertainty. The paper has no paired test on accuracy itself.
- Flip ratio exceeds 1 at 7K while accuracy still climbs to 12K. So "ratio above 1" is not "accuracy falling". Do not use 7K as a stop point on this basis.
- Two models, one family of base weights (32B), greedy decoding, one budget-forcing method. The 80-case audit and indicator correlations come from one model and the same sample defines and tests the indicators.
- Natural-long samples (N=312) are selected by being long, which correlates with hard problems; "natural == forced" does not remove the difficulty confound.
- Gema constructed tasks show large drops, but they are adversarial by design (distractors, famous-puzzle framing). Not representative of ordinary workloads. Effects are model-specific (Claude distracted; o-series framing-sensitive).
- Evidence for "longer helps" is also strong: s1 (50 -> 57 on AIME24), o1 high effort 29.1% vs low 21.0% single-run. Overthinking is a late-budget, task-specific flattening, not a general law.
- Illusion of Thinking collapse is disputed (Lawsen); keep out of the established set.
- Wu and Ghosal rest on stylised theory plus small samples (30 questions per model; 100 GPQA questions).
- Hassid compares chains within a question, but shorter chains may be shorter because the model was confident; this is correlational selection, not proof that cutting length helps.
- Survey-type claims (a24, c26, b28) were not used for numbers.

## Only seen in snippets / not read
- a25 Jurayj (confidence thresholds): not opened.
- b28 / c25 / c26: s1 (c25) and Sui survey not read for findings in those lines (a23 and a24 did open them).
- c19 TALE: abstract only, no percentages.
- c20-c22 (early exit, answer convergence, probing): read but I did not re-open their PDFs; numbers are taken from the evidence files.
- Thoughtology (c23) magnitudes not re-checked.

## GAPS
1. Does the drop from 12K to 16K survive a paired test over several seeds and temperatures>0, and on models other than R1-32B and s1-32B (Qwen3, o-series, Claude)?
2. Is there any measured case where a scaffold with a stop rule (answer convergence, oscillation) beats a fixed budget at equal mean tokens on a held-out set, rather than only cutting tokens?
3. How much of the "overthinking" decline is difficulty selection in natural long traces versus the effect of length itself (matched-difficulty natural experiment)?
4. Does a "verify before revising" gate (do not overwrite a stable intermediate answer without new evidence) reduce negative flips, and what does it cost in positive flips?
5. What is the real equal-token comparison of one long chain, k short chains with vote, short-m@k and NoThinking-first on one benchmark and model?
6. Are trace indicators (answer oscillation r=0.78) predictive on held-out problems and other models, not on the sample used to define them?
7. Do overthinking effects appear in non-math domains (code repair, planning, open-ended judgment, tool-using agents) with matched controls, beyond Cuadron's SWE-bench analysis and GPQA?
8. How do overthinking and underthinking (thought switching) trade off in the same budget sweep, and can one control (switch penalty plus stop rule) address both?
9. Do the Gema safety/behaviour shifts with reasoning length replicate across budgets and models outside Anthropic's own evaluation?
10. Does any 2026 paper replicate or fail to replicate Zhou et al.'s flip-ratio findings?

## Gap search results (evidence_d.jsonl, d01-d23; claims K20-K26 added)
Search note: WebSearch quota and the arXiv, OpenAlex and Semantic Scholar search APIs were rate-limited. Sources were found by following Zhou's reference list and a Semantic Scholar citation listing, then read as full-text PDFs.

1. Seeds, temperature, other models: OPEN, partly bounded. Zhou used greedy decoding, one pass, no paired test (d01). No paper repeats the 12K to 16K test with seeds. On other models: GPT-5, o3, Gemini 2.5 plateau on basic maths (d03); Qwen3-235B rises smoothly to 32K on vendor plots (d04); Gema used 3 seeds with CIs on constructed tasks (d02). So the drop is model- and task-specific, not general.
2. Stop rule beats a fixed budget on held-out data: PARTLY CLOSED, contested. DEER beat full length at lower tokens on three models in math (d11). An independent 7-benchmark test with Qwen3-4B/8B found DEER and Dynasor did not (d12). A learned stop head beat validation-chosen fixed budgets in two agent tasks (d14); MetaCtrl transferred to unseen reasoners (d15). Simple rules win in math only; wins elsewhere need training or tuning.
3. Difficulty versus length: PARTLY CLOSED. Within the same question and within each difficulty tercile, correct chains are shorter (d07, d08, d10). This shows length is a symptom of going wrong. No paper separates symptom from cause with matched difficulty and forced extension together. Still open.
4. Verify-before-revise gate: OPEN, with a warning. Nobody tested the gate. A same-model judge picks the later answer in over 95% of disagreements (d13), so self-comparison fails. Revision success is under 10% for strong models, and failed revision beats success for weak ones (d10). Use external checks and log rescued vs harmed answers (d22).
5. Equal-token comparison of one long chain, k short chains, short-m@k and NoThinking: PARTLY CLOSED. short-m@k vs majority at equal compute (d07), NoThinking at matched tokens (d09), parallel thinking vs extension (d06) are each measured. No single table has all four arms on one model and benchmark. Still open.
6. Held-out validation of trace indicators: OPEN. Zhou's early stopping used the same data (d01). Bulut shows pooled scores can be difficulty (d16). Cross-model support only that switching goes with lower accuracy (d17).
7. Non-math domains: PARTLY OPEN. StreamStop gives controlled agent evidence (d14), the deterministic-state paper gives a non-math failure from abstract only (d20), and DEER/Dynasor lose outside math (d12). Matched controls in code repair, planning and judgment are still missing. d23 is descriptive only.
8. Over- and underthinking in one budget sweep: OPEN. Wang's switch penalty has no budget sweep (d21).
9. Gema replication: PARTLY. Same paper shows seeds and budgets, and o3 and R1 do not show the Sonnet shift (d02). No outside replication found.
10. Replication of Zhou's flip ratio: CLOSED as "none found". 21 citing papers listed; the five closest cite it as motivation only (d19).

Corrections to existing claims: K01 and K02 now carry a model-dependence caveat; K05 and K06 are now "contested"; Jurayj (a25) is now read in full (d05): its budget range stops at 8K, below Zhou's peak. d20 was read from the abstract page only (opened:false).
