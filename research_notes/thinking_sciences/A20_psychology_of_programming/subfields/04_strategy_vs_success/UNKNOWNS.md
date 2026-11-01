# Strategy vs success: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A20.04-U1 | Does strategy matter once information is held fixed? | A rule on whether to invest in procedure or in information | all | K24, K18; no study; single-source | 2x2 fixed vs free procedure x info on/off; debug items with real output; fix rate, interaction term | Information main effect >= 5 points and procedure effect < 2 points, or an interaction >= 3 points | High |
| A20.04-U2 | Does a fixed locate-fix-validate route still beat a free agent for a strong model? | Fixed phases S3-S5 as default for debug items | S | K10, K23; contested; leaderboard 75.2 vs 73.2 | Same model; leak-filtered items incl. multi-file; fix rate with CI | Fixed arm >= free arm + 3 points with non-overlapping CI, also on multi-file items | High |
| A20.04-U3 | Is one retrieved bug-class lesson worth it, and what does a wrong one cost? | One-lesson cap; lesson-conflict drop rule | memory | K20; d02, d03; single-source, older model | Arms 0/1/2 lessons + 1 wrong lesson; before vs after first attempt; fix rate, wrong-lesson follow rate | 1 lesson >= +2 points over 0; wrong lesson loses < 2 points or is dropped on contradicting output | High |
| A20.04-U4 | Does forcing output inspection before the first edit raise fix rate on silent bugs? | Pre-edit inspect step | S5 | K04; b06, b10; human-only | Forced inspect vs edit-first; silent-wrong-output items; fix rate, tokens | >= +4 points on silent items, no loss elsewhere | High |
| A20.04-U5 | Does a stop-and-rediagnose trigger beat continued editing? | Trigger after k failed edits (k=2 or 3) | S5, S6, G1 | K25, K17; b15 (90.5% to 57.2%), d13; single-source | k=2, k=3, none; multi-step repair items; fix rate and tokens on failed items | >= +3 points at equal tokens | High |
| A20.04-U6 | Does a fixation cap with round-robin over suspects help? | Per-suspect probe cap | S5, S6 | K14; contested; b04, c11, d01 | Cap k vs unlimited; multi-bug and decoy items; bugs fixed per item | >= +0.2 bugs per item on multi-bug items, loss < 2 points on single-cause items | Med |
| A20.04-U7 | Does an action guardrail beat a sentence guardrail against misleading comments? | Verify-before-trust action | G | K05, K21; d06, d07; single-source, output prediction only | Misleading comment at true site and at decoy; none/sentence/action; first-edit-at-comment rate, fix rate | Action guardrail cuts decoy-first-edit rate by >= 30% relative with no fix-rate loss | Med |
| A20.04-U8 | Does routing feedback by bug class beat uniform trace feedback? | Class-routed probes | O | K13; b17, c17; single-source, Fig. 4 unread | Uniform trace vs routed; items labelled syntax/reference/logic; fix rate by class | >= +3 points on logic items | Med |
| A20.04-U9 | Does the hypothesis-prediction-experiment format add anything beyond real execution? | Prediction step before a probe | O | K09; b16; single-source, older model | Format vs free-form, real execution in both; fix rate, precision of the done signal | >= +2 points fix rate or calibration gain | Low |
| A20.04-U10 | Does the strategy effect grow with familiarity (Ko and Uttl hypothesis)? | A familiarity input to the S0 gate | S0 | K19, K22; d04, d10, d11; indirect only | Strategy arms on common vs rare-language or unseen-API items; strategy effect by stratum | Strategy effect differs by >= 3 points between strata, same sign in two models | Med |
| A20.04-U11 | Do agent behaviours (repeat actions, fix without test) predict failure when knowledge is held fixed? | Run-time anti-pattern monitors | S6, G1 | K14, K25; d01; confounded by agent identity | Log our own trajectories on one model; label anti-patterns; compare fix rate within item | Anti-pattern present predicts failure with odds ratio >= 2 within item | Med |
| A20.04-U12 | Does a flip counter plus no-evidence-no-revision rule cut correct-to-wrong changes in code? | Hard enforcement of the revise gate | G2 | K07 is [E] for reasoning, not fully tested on code | Revise-on vs gated; count flips; fix rate | Flips fall >= 50% with no fix-rate loss | Low |
| A20.04-U13 | What is the best number of failed edits before widening search? | Value of k | S5 | b15 (57.2% after first failure); single-source | Same as U5 with k = 1, 2, 3, 4 | Best k beats continued editing by >= 3 points; adopt that k | Low |

## Open questions we cannot test on our bench yet
- A human replication of Ko and Uttl needs participants and a coded think-aloud pipeline. It would unblock the "knowledge vs strategy" claim, which is single-source and contested (thesis vs paper).
- Google Scholar forward citations (56 found in Semantic Scholar only). A fuller pass would unblock "no replication exists".
- Clean agent-identity control for trajectory clustering. We need many runs of one agent and one model on the same items.
- Current frontier models on self-correction without a signal. We need our own run on the latest models.
- DebugBench Fig. 4 values and exact SWT-Bench precision figures were not extracted. Reading them would firm up U8 and the verifier-role claim.
- Deliberately false retrieved facts have not been tested by anyone. We need a labelled wrong-lesson set.

## Order to run
1. U1 (the 2x2): it decides whether the headline holds for our agent and sets the weight of every other row.
2. U5 (stop-and-rediagnose trigger): cheap, strongest single hook (90.5% to 57.2% after one failed edit), fits S5/S6 with no new parts.
3. U3 (lesson store with one wrong lesson): memory design depends on it; one vs many lessons (42.0 vs 39.0) is the nearest measured cost of bad retrieval.
