# ACT-R: production selection: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C02.05-U1 | Does count-based utility choice of operators beat fixed order and random? | Per-class operator statistics; softmax(P*G - C) at S6/impasse | O, S6, memory | K01, K08, K18, K19; single-source; no ablation exists; MACLA control is similarity | Arms: fixed O1-O8 order, random, utility. 100+ impasse items (ARC, BRAINTEASER). Metric: solve rate on held-out checks, tokens per solve | Utility beats both by >= 2 points with 95% CI excluding 0 | High |
| C02.05-U2 | Is a token-cost term worth having in the score? | C (mean tokens) in the score | O, G7 | K03; human-only (Gray); d09 trained | Utility with vs without C, items as U1. Metric: solves per 1k tokens | >= 10% more solves per 1k tokens, accuracy not lower by > 1 point | Med |
| C02.05-U3 | Do decayed counts catch an operator that stops working? | Count decay (gamma .95 or .99) | O | K21; model-level arms only; window 50 / .95 untested | Stream of 100 items, operator X breaks at item 50. Arms: no decay, .95, .99. Metric: trials to switch; accuracy after break | Switches in <= 10 trials and costs <= 1 point when stable | High |
| C02.05-U4 | How strong should the prior be? | Prior pseudo-counts per operator | O, memory | K22; single-source; no sweep | Prior 0, 2, 5, 20, 255. Metric: accuracy after 5, 20, 50 observations per class | A setting beats uniform prior by >= 2 points at 20 observations | Med |
| C02.05-U5 | Which softmax temperature, and should it decay? | Fixed or decayed temperature | O | K04, K26; human fits 0.44-0.75; d17 abstract only | t in 0.1, 0.25, 0.5, 1.0, decayed. Metric: solve rate; sensitivity | Best setting beats worst by >= 2 points; pick the flattest region | Med |
| C02.05-U6 | Does discounted credit beat equal credit for operator chains? | TD-style credit across a chain | O, memory | K05, K25; human single-step fits; Fu and Anderson 2006 unopened | 3-step chains. Arms: end-of-episode equal share, gamma .95 TD, last-operator only. Metric: solve rate; rank accuracy | TD beats equal share by >= 2 points | Low |
| C02.05-U7 | Is a cap on negative updates and a minimum probability needed? | Floor on probability and cap on penalty | O, G | K09, K20; trained router only | Arms: no negative update on abandon, full, capped. Metric: solve rate; share of calls to the cheapest operator | No operator collapse (> 80% share) and no loss | Med |
| C02.05-U8 | Does scaffold count beat model-rated operator success? | Size of the gain (counts already in "Add now") | O, G | K13, K23 established for self-estimates, not for operators | Arms: model-rated, counts. Metric: solve rate; calibration gap | Counts win by >= 2 points | Low |
| C02.05-U9 | Does a summary table of operator stats in the prompt help? | Show win/cost table to the strong model | O | K11; EVOLvE 2023-24 models; small models lose | Arms: no table, raw log, summary table; strong and weak model. Metric: solve rate | Table beats no table by >= 2 points on the strong model | Med |
| C02.05-U10 | Can operator stats be shared across problem classes? | Subtask-grain sharing | memory | K15, K24; similarity-based; whole-task sharing hurt | Arms: per-class only, subtask-level shared, whole-task shared. Metric: solve rate | Subtask sharing beats per-class by >= 1 point; whole-task never | Low |
| C02.05-U11 | How coarse should contexts be? | Number of problem classes | memory | K06; tabular RL needed thousands of episodes | Context sets of 2, 4, 8, 16 classes. Metric: accuracy at 50 total observations | Coarsest set within 1 point of best | Med |
| C02.05-U12 | Do the two ACT-R forms (success/cost vs reward-difference) differ for operators? | Choice of update rule | O | K17; toy game only | Both rules, same stream. Metric: solve rate; stability | Difference >= 2 points, otherwise take the simpler counts | Low |
| C02.05-U13 | Does utility choice help most in particular modes (O4 vs O3 vs O6)? | Mode-specific priors | O | no data | Per-mode analysis of U1 | Mode effect >= 3 points | Low |

## Open questions we cannot test on our bench yet
- Original Lovett and Anderson (1996) data (N, fit, overshoot-stayers): needs the journal PDF.
- Fu and Anderson (2006) fits for recurrent choice and credit assignment: full text was blocked.
- ICCM and MathPsych 2024-26 LLM + ACT-R utility papers: search APIs were rate limited; needs a proceedings sweep.
- Outcome-based (not similarity-based) shared utility across tasks: needs a multi-task bench with logged outcomes.
- Human replication of the utility equation itself: needs new human data, outside our scope.
- Why Qwen3-4B is a TextBandit outlier (89.2%): needs replication.

## Order to run
1. C02.05-U1: the core claim has no ablation anywhere; a null result removes most of this subfield from the schema.
2. C02.05-U3: drift handling is the cheapest likely gain once U1 passes and has a clear threshold.
3. C02.05-U4 (with U5 in the same sweep): cold-start prior and temperature decide whether the rule works with few outcomes.
