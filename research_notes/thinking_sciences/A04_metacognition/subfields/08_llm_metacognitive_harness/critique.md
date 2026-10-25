# Cross-check: A04.08 LLM metacognitive harness

Checked 2026-10-26. I re-opened the PDFs (Cao 2605.14186, Huang 2310.01798, Xiong 2306.13063, Early-Stopping SC 2401.10480, Adaptive-RAG 2403.14403, Cacioli 2604.15702 and the 33-model atlas 2605.06673) and compared the numbers with evidence_a, evidence_b and evidence_c.

Note on independence: the three evidence files cover the same papers, so agreement between a, b and c is not independent confirmation. Counting is by distinct papers in claims.jsonl.

## Corrections made

1. Huang et al. debate vs self-consistency (a19, c12). Table 7 reads: debate round 1 = 6 responses, 83.2; debate round 2 = 9 responses, 83.0; self-consistency 3/6/9 = 82.5/85.3/88.2. a19 said "round 2 with 6 responses 83.2" (wrong round). c12 said "debate with 3 responses about 83.2 vs SC 3 responses 82.5" (wrong). b12 was right on the 9-response comparison. Claim K11 uses the corrected numbers.
2. Cacioli leaderboard (a12). The raw text gives Gemini 3.1 Pro accuracy rank 6, not 4 (rank 4 is Qwen 80B Think at +1.5). Gemini 3.1 Pro monitoring is -1.0, meta rank 19, last of the ranked models. Sonnet 4.6 is accuracy rank 9. The layout extraction of this table is scrambled; use raw mode.
3. Adaptive-RAG (b22). "3.33x time" is wrong. In the GPT-3.5 columns, 3.33 is the multi-step Time value, 1.46 is Adaptive-RAG and 0.86 is single-step. The ratio to single-step would be about 3.9x and 1.7x, if the units are comparable, which I could not confirm. The table rows are misaligned in extraction. Treat the cost claim as approximate.
4. Cao Table 2 reading (a04, b04, c04). Confirmed, with one addition the evidence files missed: the aggregation and context rows (last answer, max-JOL, no prior state) all use K = 4.00, so "no prior metacognitive state 45.0" is independent 4-attempt sampling and is the nearest equal-compute comparator. The "random retry" CI [43,48] is far narrower than the others, which suggests it is over random seeds, not over items, so it is not comparable with the item-bootstrap CIs. The hand rule (K 2.40, 42.0), FOK-only (42.0) and full-context (40.0) all fall below pass@1 (44.0).
5. Cao per-benchmark tables (b25). The text extraction offsets rows by one line. The mapping that matches the pooled Table 1B (Self-Refine K about 1.5, Budget forcing K = 1.0) is the right one. Corrected readings: HLE Self-Refine 53.0 ($0.41), Budget forcing 51.0, Verifier 52.0 ($2.21), Aggregator 57.0 ($2.31), Harness 60.0 (K 1.4, $0.98). LCB Self-Refine 80.6, Budget forcing 80.0, Verifier 78.9, Aggregator 83.4 ($0.94), Harness 84.3 ($0.56, K 2.6). R-Bench-V Aggregator 36.5 ($0.90), Harness 41.1 ($0.72, K 3.2). I could not fully confirm every cell, but the size-weighted sums reproduce the pooled results: accuracy 48.35 / 53.66 / 56.9, cost $0.294 and $0.78, K about 2.43 (reported 2.4). That check is strong support for the table values.
6. Table 1B oracle for budget forcing equals its accuracy (51.5), since it makes one attempt. Not an error, but the "oracle" column means different things across rows.

## Numbers confirmed unchanged

Cao pooled 48.3 to 56.9; N 1,859 (668/388/803); cost per question; JOL band numbers 0.16 to 0.42, 0.36 to 0.55, 0.67 to 0.64; within-problem SD 0.048 vs across 0.270; anchor AUROC and ECE for Sonnet (0.612/0.745/0.757; ECE 0.132/0.112); Gemma 4 FOK 0.534; Huang Tables 2, 3 and 7 (other than item 1); Xiong GPT-4 AUROC 62.7, ECE above 0.377, GSM8K 54.8 to 92.7; Early-Stopping SC sample reductions; Cacioli +39.4, +31.6, +27.9, r = .17 with CI [-.29, .57], 98.6% direct, 17 of 20 on foils, alpha 0.54.

## Contradictions and tensions between sources

- Cao says metacognitive control beats parallel and vertical scaling. Its own ablation shows independent 4-attempt sampling with the aggregator reaches 45.0 vs 47.0 and the hand-built controller falls below pass@1. The headline gain is real against pass@1 but the cause (directed control vs just more attempts plus a selector) is unresolved.
- Cao's LCB data: the Aggregator reaches 83.4 vs harness 84.3, so most of the code gain comes from multi-attempt aggregation and the harness mainly saves cost ($0.56 vs $0.94). On HLE the harness leads the Aggregator by 3 points (60 vs 57) at about 40% of the cost.
- Huang/Kamoi (self-correction fails) vs Cao (self-reported confidence helps): not truly in conflict. Cao uses confidence only to decide whether to retry and hides it from the selector, and retries are independent-ish with compact history. But Cao's models are 2026 reasoning models, Huang's are 2023 ones, and nobody has re-run the Huang protocol on a reasoning model.
- Cacioli: Sonnet 4.6 has the best retrospective monitoring but almost never acts on it. Cao: the same model's JOL is usable when a code controller acts for it. These fit together, and both point to code-level control. They are different tasks, so this is inference, not a tested claim.
- Kadavath (models mostly know what they know) vs Xiong (verbalized confidence near chance for GPT-4): different formats (logprob P(True) vs verbalized) and different model generations.

## Weak spots

- Everything about the harness rests on one preprint from the team that built it, one solver model, one run per cell, no seeds and no CIs on the full benchmarks, and code not yet released.
- The controller is a per-model SVM fitted on 100 anchor items, selected from 134 configurations by out-of-fold AUROC. Overfitting to the anchor is possible. FOK is also passed into the solve prompt, so FOK may change the solve, not only gate it.
- Leaderboard comparisons use April 2026 snapshots and mix single-model entries with a multi-attempt system.
- "Low-confidence gain" uses bands built from first-attempt JOL; regression to the mean can inflate this. No placebo (random re-ask in the same band) is shown.
- Tasks are single-turn question answering and code. Nothing on long-horizon agents (authors say so).
- Cacioli's battery: single administration, thresholds are conventions, n = 20, T6 exploratory, from a hackathon. The 33-model atlas (new, found in this check, only the abstract read) shows verbalized-confidence monitoring is domain-dependent (Type-2 AUROC .742 for applied knowledge vs .658 formal reasoning, .652 natural science) and Anthropic's profile shape varied across four generations.
- Older studies (Huang, Xiong, Kadavath, ESC, Adaptive-RAG, Self-Refine) use 2022 to 2023 models; effect sizes should not be carried over to Sonnet-class reasoning models.

## Only seen in snippets (not opened)

a28 Judge, Retrieve, or Abstain; a29 Learning When to Escalate; a30 Answer instability as a black-box signal. No claim uses them. Semantic Scholar lists two citing papers for Cao, "Thinking Before Thinking: Scaling Agentic Inference Through Meta-Reasoning" and "Metacognition in LLMs: Foundations, Progress, and Opportunities"; only titles seen, neither is a replication by title. Snell, s1, Self-Refine, Reflexion, DeepConf, FLARE, Self-RAG, Chen overthinking, Kamoi, Tyen and Wen numbers were not re-opened in this pass (they were marked opened by their original agents).

## GAPS

1. Does the harness beat plain best-of-K and majority vote at the same total tokens, per benchmark, with seeds and paired tests? (Decides whether directed control earns its complexity.)
2. Is directed retry better than random retry at matched K on a large sample (N of at least 500)? Cao's 47.0 vs 45.7 on N=100 says nothing yet.
3. How much of the gain comes from the stop decision (saving tokens on confident items) and how much from the retry-with-compact-history and selector (extra attempts)? A full factorial ablation is missing.
4. Do the confidence signals stay usable (AUROC at least 0.6, ECE below 0.15) on our agent and tasks, and how many labelled anchor items are needed before the controller stops overfitting?
5. Does the low-confidence gain survive after correcting for regression to the mean (bands set by an independent first read, or by a separate split)?
6. Does compact-history retry beat full-context retry and no-history retry on reasoning models with adequate N? Is the anchoring effect real, and can it be reduced by other means?
7. Does intrinsic self-correction (the Huang protocol) still fail on 2026 reasoning models? Without this, G1/G3 guardrails rest on 2023 evidence.
8. What stopping signal works without logprobs: verbalized JOL, sample agreement, or a verifier? A same-model comparison at equal tokens is missing (ESC and DeepConf need agreement or logprobs; Cao uses a trained SVM).
9. Does any of this transfer to multi-step agent tasks, where the stop/abstain decision carries action costs and where feedback is external? No published result found.
10. Is there an independent replication or a forward-citation test of Cao's harness (code release pending as of this check)? Read the two citing papers to see whether either tests it.

## Gap search results (2026-10-26, evidence_d.jsonl d01 to d19)

The web search quota ran out partway through, so the later checks used direct arXiv PDFs only. Two PDFs (AgentAbstain, Lost at the Beginning of Reasoning) could not be downloaded; AgentAbstain was read as an abstract page only.

Status per gap:

1. Harness vs best-of-K and majority vote at equal tokens: OPEN. Re-read of Cao confirms no such arm (d03). Adjacent matched-budget tests of adaptive allocation found smaller gains: +2.5 average over uniform self-consistency in small open models, shrinking with budget, with a simple early-stop rule as good for larger models (d11); +3 to +4 over random allocation on MATH N=200 (d13). Nothing on a 2026 frontier model.
2. Directed vs random retry at N of 500 or more: OPEN for retry with feedback. Cao's random-retry CI [43,48] is far narrower than its other arms, so 47.0 vs 45.7 is not a like-for-like test (d02). Independent evidence for directed allocation of samples exists (d13) but uses text features and N=200.
3. Stop decision vs extra attempts: OPEN. No factorial ablation anywhere. The Meta agentic paper also says it cannot attribute its gain to any component (d06).
4. Signals usable on our agent, anchor size: PARTLY. Raw verbalized confidence on 9 open reasoning models averaged ECE 0.268 and AUROC 0.635 (d15), so the bar is not met by default and recalibration is needed. ECE alone can pass a nearly empty signal (d04). Anchor size needed: still unknown.
5. Regression to the mean in the low-confidence band: OPEN. No placebo re-ask arm found in Cao or in the Illusion of Insight study (d10). The concern is structural: JOL is a judgment of the same attempt, so a low-JOL band is enriched for failed first attempts and a fresh second draw will look better (my inference, untested).
6. Compact vs full vs no history: OPEN and now contested. One matched-token study found sequential refinement with full prior reasoning beats parallel in 43 of 45 cells (d16), the opposite sign to Cao's 40.0 vs 45.0; a 4,096-token cap per step may explain it.
7. Intrinsic self-correction on 2026 reasoning models: PARTLY. Reasoning models fix errors in their own context (blind spot near zero or negative, d08); prompted revision adds little at its token price for R1-class models (d09); spontaneous pivots are rare and hurt, while a cued second pass gated on high entropy helps in small models (d10). The Huang review-your-answer protocol has still not been run on Sonnet 4.6. G1/G3 should be scoped to non-reasoning settings until tested.
8. Stopping signal without logprobs: MOSTLY CLOSED for open reasoning models. One verbalized confidence plus 2-sample agreement beats either alone even at K=8 (d14); two-sample disagreement beats single-sample logprob signals (d12); agreement alone can fail for over-confident models (d19). No verifier arm and no Claude model in these tests.
9. Transfer to multi-step agents: PARTLY. A controller with compact state beats flat history at matched call budgets but loses at small budgets (d06); escalation thresholds are model-specific and unstable (d17); abstention is independent of solving and often comes after irreversible steps (d18). None tests a confidence-gated stop on an agent with external feedback.
10. Independent replication: CLOSED as "none found". arXiv lists v1 only, no code link (d01). Both Semantic Scholar citers were read: the Yale survey cites it once (d07) and the Meta paper cites it as related work (d06). Neither is a replication.

New claims K23 to K29 were added to claims.jsonl; K02, K03, K04, K06, K08, K09, K10 and K21 got extra evidence ids, and K06 changed to contested.

Decision for the agent design: the safe reading is that confidence-gated control probably helps modestly at fixed cost, but the +8.6 headline should not be the planning number. Plan on +1.5 to +4 until a matched-token factorial test says otherwise.
