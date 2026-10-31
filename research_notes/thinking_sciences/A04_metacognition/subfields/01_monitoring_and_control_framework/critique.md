# Critique and cross-check: A04.01 Monitoring and control framework

Cross-checker pass. Sources re-opened this session (full text): Cao et al. (2026, arXiv 2605.14186), Cacioli (2026, arXiv 2604.15702), Huang et al. (2024, arXiv 2310.01798), Xiong et al. (2024, arXiv 2306.13063), Tyen et al. (2024, arXiv 2311.08516), Nelson and Narens (1990 chapter), Koriat and Goldsmith (1996), Thiede et al. (2003). Claims are in claims.jsonl (A04.01-K01 to K27).

## Numbers re-checked (10 or more)

Confirmed against the text:
1. Cao 2026: pooled N=1,859, pass@1 48.3 to 56.9 (+8.6), LCB 74.3 to 84.3, HLE 48.0 to 60.0, R-Bench-V 36.1 to 41.1, LCB Hard +19.6 (stated in prose; the table text is garbled in extraction).
2. Cao 2026: FOK AUROC .612, JOL .745, joint .757 for Sonnet 4.6; Gemini 3 Flash FOK AUROC .818 but fails calibration.
3. Cao 2026: JOL groups 0.16 to 0.42, 0.36 to 0.55, 0.67 to 0.64; within-problem SD 0.048.
4. Cao 2026 cost table: Aggregator 53.7 ($1.42), Verifier Reranking 49.8 ($1.32), Harness 56.9 ($0.78, 2.4 attempts). Self-Refine 52.4 at $0.45 and Budget Forcing 51.5 at $0.67 are cheaper than the harness (see weak spots).
5. Cacioli 2026: 524 items, 10,480 evaluations, 20 models; GLM-5 1st accuracy / 9th monitoring; Haiku 4.5 13th / 2nd; r=.17; Sonnet 4.6 +39.4% delta but 98.6% answer-direct; 17 of 20 models 0% on the six foils. Power for r=.5 is .62 and for r=.3 is .25 (b03 and c09 quote different ones; both are right).
6. Huang 2024: GPT-3.5 CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle GPT-4 GSM8K 97.5, CSQA 85.5, HotpotQA 59.0.
7. Tyen 2024: BIG-Bench Mistake, oracle-location gains +23.53, +43.92, +36.86, +18.04, +18.06.
8. Nelson and Narens 1990: recall 63.9, 64.5, 64.4, 56.7 for the four study-time groups.
9. Koriat and Goldsmith 1996: standard items 75.0% free accuracy, quantity 22.3, forced 27.9; deceptive 21.0 free, 11.8 forced.
10. Xiong 2024: average GPT-4 AUROC 62.7%, ECE above .377 for GPT-3/3.5/Vicuna.

Corrections made:
- b13 and c16 (Xiong): the GSM8K jump 54.8 to 92.7 AUROC is from Table 3 on GPT-3.5, comparing the single-response row with 5 samples plus consistency. It is not a GPT-4 result. The table rows are garbled in text extraction, so the exact row labels (vanilla verbalised vs Top-K, M=1) were not certain; the paper text states 54.8 to 92.7 as verbalised vs consistency. Claim K07 words it this way.
- a32 and c14/b12 are the same Kadavath paper counted as separate lines; claim K09 counts it as one independent source.
- a34, b06 and c01 are the same Cao paper (three lines); b01, c07 and the b02-b05 lines are the same Cacioli paper. Independent-source counts in claims.jsonl treat them as one source each. Overlap lines (a36/b17 for Rhodes and Tauber; a35/b23 for Mazzoni and Cornoldi) are the same.
- a36 says 98 effect sizes, b17 says 112 effect sizes for accuracy and 98 for memory. These are two separate meta-analyses in one paper; no conflict.
- c02 said the harness is "cheaper than parallel methods". That is true, but the Cao table shows Self-Refine and Budget Forcing cheaper. Claim K02 keeps the cost data in the test.
- c05 and b09 say JOL varies more between problems than within; confirmed (0.270 vs 0.048).

## Contradictions between sources
- Verbal confidence: Xiong 2024 finds it weak and overconfident (GPT-4 AUROC 62.7%); Tian 2023 finds it better calibrated than token probabilities for RLHF models. Difference: models, tasks, and metric (ECE vs AUROC). Marked contested (K08).
- Self-correction: Madaan 2023 reports about 20% gains; Huang 2024 and Kamoi 2024 find none without an oracle. Difference: tasks (style vs reasoning) and weak first prompts. Marked contested (K25).
- Cao 2026 shows a gain from model-reported confidence; Cacioli 2026 shows most models cannot report usable confidence. Both fit if the monitor is gated per model: Cao found only Sonnet 4.6 of nine passed every check.
- Accuracy vs monitoring: Cacioli ranks are inverted, while Xiong finds better models are better monitors "but partially". Not strictly contradictory (different measures).

## Weak spots
- The strongest LLM evidence (Cao 2026, Cacioli 2026) is two 2026 preprints, one lab each, not peer reviewed. Cao uses Sonnet 4.6 as the main model; its gain was measured on a mixed set (HLE-Verified, LiveCodeBench, R-Bench-V), not on our benchmarks.
- Cao compares at "matched or lower cost" but not at equal tokens against best-of-N; cost per question, not tokens, is the unit. Harness uses 2.4 attempts, so token use is above pass@1.
- Cao ablation is on 100 items; differences of 2-5 points (47.0 vs 45.0) are within the CI [37,57] and not evidence.
- Cacioli: n=20 models for the dissociation, CI -.29 to +.57; the sixth task was an exploratory hackathon extension; withdraw delta depends on the KEEP/WITHDRAW prompt format (Dai 2026 reports scale-format sensitivity, seen second-hand only).
- Human results (Nelson and Narens) are 1970s-80s lab studies with word pairs and general knowledge questions. Transfer to LLM reasoning is by analogy.
- No source tests whether the *monitor-acts-on-model* split (code monitors, model acts) beats a model doing both in the same prompt at equal tokens, apart from Cao's single comparison.

## Seen only in snippets or second-hand (opened:false)
a21 (Nelson and Dunlosky 1991), a35/b23 (Mazzoni and Cornoldi 1993), a36/b17 (Rhodes and Tauber 2011; numbers quoted from a review, not the paper, and a Crossref check returned no abstract), b19 (Metcalfe and Finn 2008), b21 (Koriat and Goldsmith 1996 numbers from another read), b24 (Undorf and Ackerman 2017), b25/c28 (Callaway 2024), c29 (Cox 2005, MIDCA), c30 (Steyvers and Peters; Dai 2026). Not re-opened by this pass: Dunlosky and Nelson 1994, Metcalfe and Kornell 2003/2005, Callaway 2023, Kadavath 2022, Tian 2023, Kapoor 2024, Ackerman 2026, Ji-An 2025, Self-RAG, SelfAware; their numbers carry the agents' own reading only.
Practical issue: the C: drive was full during this pass; two large output dumps were deleted and only the scratch files on D: were used.

## GAPS (most decision-relevant first)
1. Does a code-side monitor-and-control loop (Cao-style FOK/JOL gating) beat best-of-N and Self-Refine at equal total tokens on our own benchmarks, and on which confidence bucket does the gain sit?
2. Which monitor is best for our model: verbalised confidence, sample agreement, a trace-reading verifier, or a code check? Measure AUROC per domain at equal tokens.
3. What is the accuracy-quantity curve when the agent may abstain with an accuracy payoff (Koriat-Goldsmith), and does it help on our tasks?
4. Does delayed or re-read monitoring (delayed JOL) improve LLM self-judgment, and has anyone tested it in an LLM? (Not found in sources.)
5. When should retrying stop: fixed K, rate-of-progress (Region of Proximal Learning) or expected-value stopping (Callaway)? Any LLM test of these rules?
6. Does the monitor degrade by domain shift or format change (Dai 2026 scale effect, Cacioli domain spread), and how do we detect an untrustworthy monitor online?
7. Is monitoring accuracy separable from the model's own cue use (fluency, length)? Test cue-stripped items on LLM confidence.
8. Does the high-confidence bucket suffer harm from extra control (Cao 0.67 to 0.64; Huang drops)? How large is the loss at scale and can a code gate prevent it?
9. Are there replications of Cao 2026 or Cacioli 2026 by independent labs, and on open models?
10. For multi-step tasks, can the monitor find the faulty step (Tyen) well enough that location-guided repair pays off at equal tokens?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d23, all opened this session; several only to abstract level, flagged in each line). Web search quota ran out, so I used arXiv PDFs, Crossref and Semantic Scholar citations. Claims K28 to K36 are new; K02, K06, K07, K08, K10, K16, K20, K24, K25, K26 and K03 gained evidence. K07 moved from established to contested.

Closed (as far as the sources allow):
- Gap 9 (replication): closed negative. Cao 2026 has 3 citing papers, none a replication. The Cacioli battery has 4, three by Cacioli himself. No independent lab or open-model replication of either (d18). Small-model data (d14, d15) is his too.
- Gap 5 (stopping), partly: agreement-based stopping works (Adaptive-Consistency up to 7.9x fewer samples at under 0.1% loss; ESC 33.8 to 84.2% fewer; d03, d04). Region of Proximal Learning and Callaway expected-value stopping have no LLM test. Shared misconceptions can fool an agreement stop (d02).
- Gap 2 (best monitor), partly: no single winner. Reasoning models: verbalised confidence plus one extra sample beats either alone at K=8 (d01). Easy facts: verbalised .956/.937 beats 3-sample agreement .765/.790 (d02). Small 4B model: agreement .999 vs verbal ~.55 (d15). Pick per model and domain. No trace-reading verifier or code check was compared at equal tokens.

Stayed open (need our own runs):
- Gap 1 (gate vs best-of-N and Self-Refine at equal tokens): only indirect support. Difficulty-aware allocation beats uniform best-of-N (Snell ~4x less compute; Damani up to 50%; d05, d06), and a Meta controller helps at large budgets but its overhead hurts at small ones (d19). No test of verbalised FOK/JOL gating besides Cao.
- Gap 3 (abstention payoff): Kalai et al. give the t/(1-t) design (d07) but no measured curve; AbstentionBench shows reasoning models abstain 24% less (d08). Decide abstention in code.
- Gap 4 (delayed JOL): the only LLM JOL study shows GPT models fail JOL at all (d16); a July 2026 survey lists no delayed-JOL test (d17). Mei and Yoon give weak analogues (re-reading the trace helps some models, hurts Claude 3.7; calibration improves along the trace; d09, d11).
- Gap 6 (domain shift): monitoring is worst on formal reasoning and natural science (.658, .652 vs .742; d12), and invalid-profile screening exists (d13), but both are from one author and nobody has run them online.
- Gap 7 (surface cues): no cue-stripped LLM test. Related: trace length vs confidence beta -.36 in one small model (d14), prompt wording moves accuracy up to 80% (d22), human trust follows explanation length (d23). Prompt paraphrase flips 4 to 9% of threshold decisions (d02).
- Gap 8 (loss on the high-confidence bucket): no new measurement; Cao's 0.67 to 0.64 still stands alone.
- Gap 10 (step location): ProcessBench shows a large spread in locating the faulty step (GPT-4o 61.9, o1-mini 87.9 F1; d20), so the Tyen weak-locator finding depends on model. Repair payoff at equal tokens untested.

Caveats on this pass: Meyer (d02) is a 100-question workshop paper with 8 to 9 errors per model. The Cacioli papers are one-author preprints. Mei, Zeng, Kamoi, Steyvers and Huff were read at abstract or front-matter level only. ProcessBench per-model table was garbled, so only headline averages are used.
