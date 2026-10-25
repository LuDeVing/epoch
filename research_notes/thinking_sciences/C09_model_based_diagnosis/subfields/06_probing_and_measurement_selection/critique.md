# Critique and cross-check: C09.06 Probing and measurement selection

## Sources re-opened this pass (full text read, numbers checked)
BED-LLM (arXiv 2508.21184v3), Uncertainty of Thoughts (2402.03271v3), Active Task Disambiguation (2502.04485), Amortizing Sequential Experimental Design (2610.20832), Zhang et al. 20 Questions (2310.01468), Piriyakulkij et al. Zendo (2402.06025), MoBayes (2604.20022), Sequential Diagnosis / MAI-DxO (arXiv 2506.22405 HTML).
Not re-opened: Siddiqi and Huang tables (a03, a04), Golovin and Krause, Rainforth review, Grand et al., QuestBench, GATE, Mazzaccara, MediQ, ASIG, Beck et al. These stay as the original agent reported them.

## Confirmed
- BED-LLM +37.4 points average over Prompt-Only, "more than doubling in over half of setups and never decreasing" (text). Table 1 cells quoted in c01-c07 all match (Animals GPT-4o-mini 44 to 88; Celebrities Mistral-Large 19 to 91; Things GPT-4o 34 to 64; Split, CoT, Implicit, ICL Beliefs cells).
- UoT: 38.1 percent average over direct prompting, 46.6 for Llama3-70B, Llama3-70B open-set numbers (DX 26.0 to 35.6, MedDG 25.7 to 50.6, FloDial 11.1 to 26.1), GPT-4 Common 49.0 to 70.9, DX 89.4 to 97.0.
- Kobalczyk HumanEval table: GPT-3.5 binary 70.8 to 85.6 at 4 questions; GPT-4o-mini binary 79.6 vs 81.5, open 83.5 vs 83.8.
- Kriz: BED-LLM 2376 s, 61.1 times; AR-BED1 38.9 s. Text confirms BED-LLM is modest over the reasoning base and worse than the non-reasoning base on some domains.
- Zhang: GPT-4 0.31 Things, 0.50 Celebrities; Claude-2 0.21/0.31.
- Zendo: Table 3 (LLM 4.52/4.72, Random 5.03/5.84, InfoGain 5.35/6.55) and Table 4 (random proposer 5.84, 6.23, 6.55; LLM proposer 5.73, 6.19, 6.55).
- MoBayes: GPT-5.4-nano sensor 78 / 81.2 / 88.0 vs Gemini 3.1 Pro standalone 60 / 62.5 / 75.7. CIs are wide (for example 78 percent, CI 66 to 90, n=50).
- MAI-DxO: o3 78.6 percent at 7,850 dollars; no-budget 81.9 at 4,735; budget 79.9; ensembling 85.5 at 7,184; physicians 19.9 percent at 2,963 dollars; GPT-4o 49.3 at 2,745.

## Corrections
1. a20/c01 disagree on the number of LLMs. The main figure has 5 LLMs; Table 1 has 6 with Llama-3.1-8B (appendix). The 37.4 average is the paper's claim; our own mean over the 18 Table 1 cells is Prompt-Only 30.3, CoT 39.5, Split 55.4, Entropy 57.6, BED-LLM 70.7, a gain of 40.4. The difference from 37.4 was not explained.
2. c04 ordering "Prompt-Only < CoT < Split < Entropy < EIG" is not strict. CoT beats Split on Things GPT-4o (49 vs 40) and ties on Celebrities GPT-4o (63). Means keep the order.
3. UoT FloDial for GPT-4 has two versions in one paper: main text 43.7 to 67.3, appendix Table 7 42.5 to 67.8. Treat as two runs. Llama 3 FloDial also differs (main table CS 28.8, appendix 29.9).
4. UoT 38.1: the paper writes percent without defining it. Per-cell data suggest relative gains (Llama3-70B MedDG 25.7 to 50.6 is nearly double). Unit stays unresolved; do not quote it as points.
5. c24 "human figures not located": Zhang Table 5 has a Human row: Things 0.24 success, Celebrities 0.31, vs GPT-4 0.31 and 0.50.
6. b24 budget cost is 2,396 in one place and 2,397 in another in the same paper.
7. Kriz 61x is BED-LLM time against their trained AR-BED1, not against a base model.

## Contradictions and tensions
- Strong gains (BED-LLM, UoT, MoBayes) vs weak or negative cases: Kriz reports BED-LLM modest on reasoning models; ASIG medical transfer +0.9; Kobalczyk gains vanish for a strong model; MediQ says asking can hurt. Boundary: gains are large when the base model is weak, a candidate set is enumerable and answers are clean.
- UoT claims information gain is the active ingredient (+5.9 percent swapping reward in ToT) but its own Table 3 shows IG, UR and PFS within 1-3 points. The tree lookahead may be the ingredient.
- Split vs full EIG: BED-LLM authors say their Split is far stronger than earlier versions, so "half-split is weak" from older papers does not carry over.
- Compute: the BED-LLM runtime table shows Prompt-Only about 45 minutes vs BED-LLM about 2.5 hours on one setup. No result in this set compares methods at equal tokens, except UoT vs ToT (GPT-4 tokens only).

## Weak spots
- Almost every LLM result uses an LLM-simulated answerer and closed lists of animals, celebrities or diseases. Real, noisy, open-ended probing (tests of real software or hardware faults) is untested.
- No study here measures probing in an agent that must also carry out repair or reasoning; MAI-DxO is bundled so the probing part is not isolated.
- GDE, Heckerman et al., Hyafil-Rivest, Kadane-Simon were not opened. The key formulas are second-hand.
- Samples are small: Zendo 5 seeds, ActiveACRE 20 tasks, MoBayes n=50, DPO test sets about 45 games.
- Siddiqi and Huang numbers (92.3 vs 42.0 vs 6.7) were not re-checked this pass.
- Snippet-only: MediQ (abstract), Kobalczyk (partly), Laban et al. (citation), Tajwar (part).

## GAPS
1. At equal total tokens, does computed half-split (or full EIG) beat plain reasoning with more thinking tokens on our kind of task? Every paper here uses more compute for the scored method.
2. How much of the BED-LLM gain survives with soft, noisy or free-text answers and an open hypothesis set (real debugging, not 20 Questions)?
3. Does the gain hold for reasoning models (o-series, Claude thinking)? Kriz says it is small; which other papers test this?
4. Which part of MAI-DxO (differential, challenger, cost steward, ensembling) produces the cost savings? Is there an ablation?
5. When should the agent probe at all? Is there a measured trigger (uncertainty threshold, abstention) that avoids the MediQ harm?
6. Cost-weighted probing in LLM agents: any study that uses p/cost ordering or cost per bit with measured accuracy and spend, outside medicine?
7. Do GDE-style priors (failure rate per component) help an LLM agent over uniform priors, and where do the priors come from?
8. Falsification probes: does choosing a probe that targets the leading hypothesis reduce fixation compared to maximum entropy probes (links to the anomaly and fixation subfield)?
9. Original GDE and de Kleer 1992/2006 lookahead results: how close is one-step lookahead to deeper lookahead in numbers?
10. Is the 38.1 percent UoT figure relative or absolute, and what is the replication status of UoT by independent groups?

## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d22). Claims K11, K13, K14, K15, K17 and K19 were edited and K21-K31 added. Web search was out of quota; I used arXiv full texts and the AAAI archive. Semantic Scholar and OpenAlex returned 429, so the original GDE paper (1987), de Kleer 1992, de Kleer 2006 and Raiman and de Kleer 1995 were not read.

**Closed**
- **Gap 10 (UoT 38.1%).** It is a relative figure: the mean of per-cell relative gains. Re-derived from Table 1, Llama3-70B gives 46.6% relative (the paper's own number) but only +10.1 points. The other models gain +9.2 to +12.8 points. Quote it as about +10 points. No independent replication was found (d01, K21).
- **Gap 4 (MAI-DxO ablation).** There is none. Variants differ in budget tracking and ensembling only. Panel alone: -39.7% cost, +3.3 points on o3. Budget tracker: a further -$2,339 for -2.0 points. Ensemble: +3.6 points at the baseline cost. A non-medical study (SIA, d14) has a real ablation: counterfactual role -5.2, follow-up questions -4.2 (d04, d05, K27). Which role saves money remains unknown, but the question is now answered as "not measured".

**Partly closed**
- **Gap 1 (equal compute).** Only UoT matches tokens (d02): scored selection beats tree search and self-consistency at 4.5k and 9.3k GPT-4 tokens. No paper gives a reasoning model the same tokens. BED-LLM costs about 6x the wall-clock of Prompt-Only (d16). SIA found that extra thinking without questions added nothing (67.3 vs 67.5, d14). GuessingGame shows free prompt constraints can match or beat scoring (d17). **Still open for our case.**
- **Gap 2 (noise, free text, open set).** UoT open set keeps the gain (+9.8 vs +10.9 points, d02). BED-LLM keeps it under answerer mismatch and weakens it on a soft film task (d16). No study injects wrong answers (d15 lists it as future work). New negative: with an LLM-proposed open hypothesis space, max-information probes can stall the proposer (d13).
- **Gap 3 (reasoning models).** Other tests: Pedrozo et al. (thinking models choose the max-information candidate in 19-36% of turns, d09), QuestBench (thinking models near 40-50%, BFS depth 10 at 99.8%, d10), MAI-DxO on o3 (cost cut, accuracy gain small and not significant for o3/o4-mini, d05), AbstentionBench abstract (reasoning fine-tuning lowers abstention, d11). No paper runs BED-LLM-style scoring on an o-series model besides Kriz. The picture is consistent, but all sets are small and some are confounded by checkpoint differences.
- **Gap 5 (when to probe).** Two measured triggers: MediQ confidence-with-rationale, thresholded (22.3% over ask-always, closes 51.2% of the gap, threshold tuned, d06), and a separate binary gate in coding agents (61.2 to 69.4 resolve rate, d07). A value-of-information gate beats tuned thresholds except at high cost (d08). Models recognise but rarely act (d12).
- **Gap 8 (falsification vs fixation).** No direct test of a leader-falsifying probe against a max-entropy probe on fixation. Indirect: SIA's counterfactual role (-5.2 when removed, d14), MAI-DxO case studies (d05), and the Number Game where falsifying probes win on compound rules but lose on easy ones (d13). **Open for the fixation subfield.**
- **Gap 9 (lookahead numbers).** de Kleer 1991 gives the design reason for one step and has no comparison numbers (d18). UoT depth results: one step reaches about 84-98% of depth 3 (d03). Theory: log-squared bound, single-log bound open (d20). The original numbers remain unread.

**Still open**
- **Gap 6 (cost-weighted probing outside medicine).** No LLM study orders probes by probability over cost with accuracy and spend measured. Nearest: VoI gating (d08) and a synthetic resume study (d21, low trust). The p/c rule itself is proven under strict assumptions (d19).
- **Gap 7 (GDE-style priors).** No LLM test. Only a low-trust synthetic prior ablation (176 vs 387 errors, d21). Priors in the classic work come from a device model (d19).

**Corrections to earlier notes**
- K13 should read "log-factor competitive in the worst case", not "near optimal".
- K19 was abstract-only; it is now backed by the full MediQ text and a coding study. Abstract-only items in this round: AbstentionBench (d11, `opened:false`).
- Extraction caveats: UoT GPT-4 rows, the Appendix E figure, QuestBench Table 2 and the Number Game table interleave in the PDF text. I used only cells I could read cleanly, or marked the reading as inferred.

**Next experiments, in order**
1. Equal-token test (K22 agent_test) with a thinking model, a non-thinking model plus code scoring, and half-split, plus a no-repeat-type rule (K28).
2. Answer-flip test at 10-20% (K29).
3. Falsifying probe vs max-entropy probe vs positive-test on fixation-prone items (K26).
