# C12.02 Expected value of sample information: cross-check critique

## Numbers re-checked against the local text of the papers (11 checks)
All confirmed unless noted.
1. Dong et al. 2026 (2601.06407): "18 of 20 conditions", up to 1.36 points, Mixed 20Q c=0.01 VoI 14.14 vs 11.49 (threshold 0.90). Confirmed.
2. Dong cost table (Gemini, Mixed 20Q). Confirmed c=0.05 (5.01 vs 3.65, +1.36) and c=0.10 (1.38 vs 2.28, -0.90). CORRECTION: the c=0.20 row is readable in the paper: VoI -0.96, best baseline No Question 0. So VoI loses at two of five costs in this sweep (0.10 and 0.20), not one. Evidence c03 called the row garbled and b09 said "No Question wins" without a margin. The 18 of 20 headline hides this.
3. Calibrate-Then-Act (2602.16699), Pandora's Box: 94.0% match, reward 0.625 vs oracle 0.649; non-CTA 11/23/20%. Confirmed.
4. CTA retrieval: rewards 0.226, 0.213, 0.244, 0.283, 0.293 confirmed. Accuracy row is 0.226, 0.578, 0.619, 0.501, 0.512. Evidence b13 "Prompted 61% retrieve reward 0.283" is the thinking variant; the non-thinking variant retrieves 97.7% and scores 0.244 (c15 is right, b13 is terse).
5. Uncertainty of Thoughts (2402.03271): +38.1% average, +46.6% Llama3-70B, DX 97.0, MedDG 88.0/81.4, 43.7 to 67.3 confirmed. CORRECTION: the significance table (Appendix) gives MedDG 74.9 to 87.9 and FloDial 42.5 to 67.8, a different aggregation from the main table (88.0 and 67.3). Both are in the paper; evidence a14 and b15 mix them. Treat 43.7/67.3 (main table) and 42.5/67.8 (appendix means) as two readings of one result. Also "+38.1%" is a relative or absolute gain in success rate averaged over models; the paper text says "in the rate of successful task completion", which I did not resolve as relative or points. Sub-claims "beats CoT-SC by 33.8%" are in the same unit.
6. UoT 5.9% reward swap and CoT-SC k=33 at 4.6k tokens (32.6/37.6/42.5): confirmed.
7. MediQ (2406.00922): 11.3% relative drop, 22.3% gain, 10.3% gap, 51.2% of gap closed. Confirmed. Note the text prints "11.3 plus or minus 10.3% relative drop", so the 11.3% has a wide spread; the abstract's 10.3% gap and this +-10.3 may be confused. The 11.3% is an average over models and datasets.
8. Sadatsafavi 2024 (2401.01849): Beta(44,458), EVPI 0.00037 / 0.00125 / 0 at thresholds 0.01/0.02/0.05 and 0.10, EVSI 0.00101 at N=1000 and threshold 0.02. Confirmed. The "81% of EVPI" is derived (0.00101/0.00125 = 80.8%), not stated in the paper. "Little gain beyond N=4,000" confirmed.
9. Heath 2021 (2105.05901): "at most 6%", "6 to 60 times faster". Confirmed.
10. Dong 2026 uses "Round (k=15)" for the c=0.01 second baseline (8.10); a fixed-round baseline can be strong at low cost.
11. NOT re-opened (no local copy, network fetch gave nothing): BED-LLM numbers (c06/c07), Bastardi and Shafir 1998 figures (b01-b06), Ren 2023 table, Handa 2024 and Hu appendices beyond those above. These stay as reported by the evidence agents, who marked them opened.

## Contradictions between sources
- UoT 43.7 vs 42.5 baseline and 87.9 vs 88.0 (see 5). Not a real conflict, two tables.
- Dong says VoI "matches or exceeds" in 18 of 20; its own cost sweep shows losses at high cost. Consistent only if the 2 losses are these.
- CTA says thinking mode is required for the 94% match; the non-thinking prior-given condition is 20%. The benefit of priors is not independent of reasoning budget.
- MediQ says asking hurts; UoT, BED-LLM and Dong say a scored question helps. The difference is the scoring rule and the task (20 Questions and diagnosis with a closed hypothesis set vs open medical QA), not a contradiction.

## Weak spots
- The classic literature (Raiffa and Schlaifer 1961, Howard 1966) was never opened; everything about it is via secondary papers. No exact numbers from the founding text.
- Only one behavioural study line (Bastardi and Shafir). The cross-cultural replication (b07) is a snippet. There is no failed-replication search for it, and no LLM version of the useless-information effect.
- Most LLM evidence is 20 Questions or medical dialogue with a simulated answerer (an LLM). Simulated users flatter question-asking.
- Few runs and small N in several papers (UoT paired t-tests with few runs, CTA 100 examples, one model Qwen3-8B).
- VoI results use the LLM's own probabilities; calibration is only fair. No study prices a noisy test with known sensitivity and specificity in an LLM and compares to the exact Bayesian value.
- Evidence is almost all from health-economics EVSI computation and from asking questions. The "quality of a noisy test" angle (sensitivity, specificity, test result then Bayes) has only Chen 2026 (theory) and the retrieval case.
- Equal-token comparisons exist only in UoT (a15). Dong, BED-LLM and CTA do not match tokens to baselines.

## GAPS (most decision-relevant first)
1. Does a value-gated test rule (do the test only if the agent's estimated EVSI exceeds its cost) beat always-test, never-test and a tuned confidence threshold at EQUAL TOKENS on reasoning or coding tasks (not 20 Questions)?
2. How well can an LLM estimate the value of a noisy test with given sensitivity and specificity (post-test probability and decision change) against the exact Bayes answer, and does an explicit probability table fix errors?
3. Does the Bastardi and Shafir pursuit-of-useless-information effect occur in LLM agents (waiting, calling tools, asking for data that cannot change the decision), and does an "could this change my decision?" check remove it?
4. Where does value-of-information gating lose (high cost, wrong belief)? Dong's sweep shows losses at c=0.10 and 0.20; what is the cost range and calibration level where a simple no-ask rule is best?
5. Which EIG or EVSI estimator is cheapest and still beats entropy (BED-LLM shows a badly estimated EIG falls to 18 vs entropy 79)? What sample count of imagined answers is enough?
6. Does one-step EVSI (myopic) fail when several tests are needed together (non-myopic value, interacting tests), and how does UoT's depth 3 compare to myopic at equal tokens?
7. Did the 1998 effect and its cross-cultural replication (Iran, Japan) hold in preregistered or large-N replications (2010-2025), and what are the boundary conditions (stakes, information cost)?
8. How does the information-gain approach transfer from simulated answerers to real noisy sources (real users, real retrieval, real tests)? Any measured gap?
9. What do Raiffa and Schlaifer (1961) and Howard (1966) give as exact results (conjugate closed forms, EVSI bounded by EVPI, upper limit on sample value) that can be turned into a numeric rule of thumb for the agent?
10. Does stating the prior and the cost help without thinking mode (CTA 20% vs 94%)? What is the smallest reasoning budget that unlocks the effect?

## Gap search results (evidence_d.jsonl, d01 to d18)
Search note: WebSearch quota ran out after one query, and the arXiv, Semantic Scholar and OpenAlex APIs returned 429. Papers were found through reference lists of papers already held and through Europe PMC; so coverage of 2025-2026 LLM work is thinner than intended.

Corrections to earlier checks
- BED-LLM re-opened (d01): the 18 for "ICL Beliefs" is a belief-construction ablation (no hypothesis filtering), not a badly estimated EIG formula. K12 reworded. Other values confirmed: BED-LLM 88, Entropy 79, Data-Estimation 64, Implicit Maximization 47 (GPT-4o-mini Animals).
- Dong (d05): Table 1 (Gemini) c=0.01 is 8.64 vs 8.30, not 14.14 vs 11.49. The 14.14 vs 11.49 in the main text is another run. Losses at c=0.10 and c=0.20 confirmed.

Closed or mostly closed
- Gap 9 (partly): the Raiffa and Schlaifer and Howard books were still not opened, but a computed exact table (d17, K31) gives the usable rule: a test only has value if its best result crosses the act threshold; EVSI is capped by EVPI. Status of the book itself: open; the numeric rule: closed.
- Gap 5: closed for the 20 Questions setting. N=15 hypotheses, M=15 questions (N=5, M=8 in preference tasks); question ranking stable at 10 hypotheses vs 85; full EIG costs about the same as entropy (d02, d03). Imagined-answer count not swept.
- Gap 6: partly. Depth 1 gives most of depth 3 in UoT (+9.9, +9.1, +3.8 points for depth 3); a one-step ask-or-act rule gave +0.02 to +0.03 F1 in Battleship (d07, d08). Interacting tests and equal-token depth comparison still untested.
- Gap 4: partly. The cost side is seen: no-ask wins at c=0.20 and a tuned threshold at c=0.10, where the gain per question is of order 1 to 9 utility units (d05). The calibration side is not tested.
- Gap 10: partly. Priors without thinking gave 20% match and reward 0.436, below thinking without priors (d10). Only an on/off switch was tested, so the smallest budget stays unknown.

Still open
- Gap 1: no equal-token test of an EVSI gate on reasoning or coding tasks. Closest: budget-aware coding agent (d11, 55.4% vs 36.8% at equal calls) which is not a value gate.
- Gap 2: no LLM study with a known sensitivity and specificity was found; the exact answer key is now available (d17). A direct test is needed.
- Gap 3: tool overuse is documented (d12: over 50% on GSM8K for Llama-3.1-8B) but the Bastardi and Shafir shift in choice and the "could this change my decision?" check were not tested in any LLM study found.
- Gap 7: no large-N or preregistered replication of the 1998 task found. Related: Shafir (1993) replication failed in most problems at N=1,026 (d15); paying for useless information held with real money (d16); surplus information lowered accuracy (d14). K08 stays contested.
- Gap 8: still open. Answerer noise is modelled but seldom measured with real users (d09, d18, d04).
