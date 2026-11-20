# Judicial bias and noise: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*
## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E11.08-U1 | Does a both-orders check (keep consistent verdicts only) raise accuracy of our pairwise selection steps? | Code-side swap-order check at every pairwise comparison | G5 / S7 | K11 established for flips; accuracy gain at equal tokens untested; LLM-only | 100 pairs with known winner; one call vs two orders plus tie-break; accuracy, flip rate | Accuracy up 3 points or more, or flip rate halved | High |
| E11.08-U2 | Does a vote of k fresh-context repeats cut occasion noise on legal vignettes without hurting accuracy? | k-sample vote for numeric and verdict answers | S3 / O | K13, K21 established for noise; K24 single-source; no legal test | 40 vignettes, k = 1, 3, 5 at fixed total tokens; disagreement with modal verdict; accuracy vs panel | Disagreement down 30% relative, accuracy not lower | High |
| E11.08-U3 | Does moving a planted number into a marked block (S1 hygiene) cut LLM anchoring? | Promote S1 hygiene remedy to [E] | S1 | K10, K14 (harm established, size contested); remedy untested | 40 anchored estimation items; plain vs hygiene vs Anti-DP vs bracketing pair; anchored share | Anchored share down 8 points or more vs plain | High |
| E11.08-U4 | Does Anti-DP (own criteria before any number) work on our model? | A criteria-first step in S1 | S1 | K15 single paper; Llama-3.1-8B 34.7% to 24.7%, none on Qwen2.5-7B; small models only | Same battery as U3; criteria-first vs plain | Anchored share down 5 points or more for at most 128 added tokens | Med |
| E11.08-U5 | Does hiding the candidate label when auditing reasoning cut conformity? | Blind judging rule in S8 | G5 / S8 | K16 single-source; five 7-9B judges, revision 76-85% vs 5-22% | 60 audit items with true and wrong labels; label visible vs hidden; revision rate and error detection | Label-aligned revision down 30 points, detection not lower | High |
| E11.08-U6 | Does verdict-first output reduce order flips for our model? | Output-format rule per model | O (format) | K12 contested; helped 1 judge of 5, hurt 3 | Swap-order test, 100 pairs, both formats | Flip rate down 5 points or more, accuracy not lower | Low |
| E11.08-U7 | Does an agent show decision-rate drift by position in a long context (hungry judge analogue)? | Fresh-context-per-item guard or periodic reset | G (late-run default) | K18, K27 contested; no direct study; Lost in the Middle only | 40 equal-difficulty yes/no cases, random order; continuous vs fresh context; slope of accept rate on position | Slope significant (p < 0.05) and fresh arm removes it | Med |
| E11.08-U8 | Does the previous answer bias the next (gambler's fallacy analogue)? | Rule: decide items in isolation | G (sequence) | K06 single-source; human only | 100 binary items, random truth; previous answer visible vs hidden; P(same) minus base rate | Dependence of 3 points or more in visible arm | Med |
| E11.08-U9 | Do irrelevant attributes (wealth, prestige, victim) move our agent's verdicts, and does blinding remove it? | Attribute-blinding step in S1 for judgment tasks | G / S1 | K17 single-source; synthetic vignettes only | 40 vignettes; original vs swapped attribute; blind vs plain; paired shift | Shift of 0.5 SD or more in plain arm; blind arm halves it | Med |
| E11.08-U10 | Is LLM numeric variance mostly from the scale-use step rather than ranking? | Ranked or relative output for numeric judgments | O | K20 single-source; human only | 40 cases; absolute number vs rank among 5 reference cases; run-to-run SD; agreement with panel | Rank arm SD down 30%, panel agreement not lower | Med |
| E11.08-U11 | How does LLM variance split into level, pattern and occasion on legal tasks? | Pick the noise tool by component (vote for occasion, diversify for pattern) | measurement | K25 single-source; human labelling template only | cases x variants x repeats matrix; variance decomposition | Occasion share over 20% of total (then voting pays) | Med |
| E11.08-U12 | Does a sawtooth appear in our own bench logs purely from outcome-dependent stopping? | Rule: fixed item count, no outcome-based cut-offs | bench method | K03 established, K04 single-source | Simulate our stopping rule on random data; compare with logs | Simulated sawtooth over 10 points | Low |

## Open questions we cannot test on our bench yet
- Danziger residual effect after controls. Needs supplementary tables S1-S15 and the reply body (blocked this run), or the raw data.
- Preregistered or randomised order experiments in real courts. None found; would need a court partner.
- Real-court anchoring size versus the vignette value d = 0.58. Needs real case files; only archival coding exists (V = 0.186).
- Cause of LLM anchoring (context attention vs training). Needs interpretability tooling we lack.
- Real-court validity of LLM judicial audits. Needs real case files with outcomes.
- Full-text check of Englich 2006, Tversky and Kahneman 1974, Bystranowski 2021, Hagger 2016, Vohs 2021 numbers.

## Order to run
1. E11.08-U1 (swap-order check): cheapest, flip rates already measured, changes S7 and any judge step directly.
2. E11.08-U3 (anchor hygiene vs Anti-DP vs bracketing): tests the one S1 remedy still marked [S], with a ready battery.
3. E11.08-U2 (k-sample vote on legal vignettes): decides whether repeat-and-vote applies to noisy judgment tasks, and feeds U11.
