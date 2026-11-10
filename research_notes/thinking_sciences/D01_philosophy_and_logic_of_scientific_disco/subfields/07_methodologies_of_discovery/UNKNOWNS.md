# Methodologies of discovery: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| D01.07-U1 | Does a cheap held-out probe predict final success better than the model's own pre-score? | Probe-then-allocate rule for candidate ideas | S0 / pursuit | K02, K18, d01: single-source, humans and 2025 models; no head-to-head | 50 items x 8 candidates. Arms: model self-score pick; random pick; probe pick. Metric: executed pass rate of chosen; Spearman score vs outcome | Probe arm beats self-score arm by 5+ points with paired CI excluding 0 | High |
| D01.07-U2 | Which allocation rule best splits tokens over candidates: uniform, random-k, MMR-k, halving, UCB? | The winning rule as the pursuit policy | S0 / S6 | K06, K19, d06, d08: verifiable queries or proxy-judged only | 30 items x 20 candidates, executed check. Five arms. Metric: solved per 100k tokens | A non-uniform arm beats uniform by 3+ points or 15% fewer tokens in 2 of 3 item sets | High |
| D01.07-U3 | Does a two-tier weak/strong gate cut wasted tokens? | Stage-1 probe before full check | S0 / S3 | K12, K23, d15, d18: no ablation for ideas; EarlyEval analogue (26% fewer steps, 1.1 pt) | Same ideas with vs without stage 1. Metric: tokens spent on ideas that fail, final accuracy | At least 15% fewer wasted tokens with accuracy loss under 2 points | High |
| D01.07-U4 | Does reading retrieved papers cut false-novel calls for 2026 models? | Mandatory reranked-retrieval novelty check | S0 gate | K09, K20, d10, d11: 2024 models, n=32 | 30 hand-labelled known-vs-novel items. Arms: keyword; opinion; reranked retrieval. Metric: false-novel rate, accuracy | Retrieval arm false-novel rate under 20% and accuracy 15+ points above opinion arm | Med |
| D01.07-U5 | Does schema-seeded generation yield more distinct valid ideas than best-of-N plain? | Template library for generation | S3 / O1-O8 | K21, d17: confounded 5-vs-1, no Darden test | 20 samples plain vs 20 template-seeded, dedup at cosine 0.8. Metric: distinct directions, pass@k | Template arm beats best-of-N on pass@k by 5+ points | Med |
| D01.07-U6 | Is the diversity ceiling (about 5% unique) real for our generator, and does changing the source beat more samples? | Cap on same-prompt sampling; force changed prompt or operator | G4 / S3 | K05, b04: one generator, one embedding | Dedup curve for 4 to 200 samples, plain vs operator-varied | Plain unique share under 25% at 50 samples and varied arm 2x more distinct | Med |
| D01.07-U7 | Does a reachability (generative justification) check improve idea quality? | Cited-premise existence check | S0 | a01, K12: philosophy only | With vs without premise-exists check, same tokens. Metric: pass rate, hallucinated-premise rate | Check lowers hallucinated premises by 30% and does not cut pass rate | Med |
| D01.07-U8 | Is surprise-triggered idea search cheaper than timer-triggered? | Formal trigger for idea search | G1 | K17, a06: philosophy; G1 supported elsewhere | Trigger on check fail or disagreement vs every n tokens. Metric: tokens to correct | Trigger arm uses 10%+ fewer tokens at equal accuracy | Low |
| D01.07-U9 | Do isolated early answers raise final diversity and accuracy (Zollman) in LLM branches? | Isolation window before merge | G4 | K13, d16: contested; GPT-3.5, 100 questions, no early isolation | K branches isolated for first third then merged, vs shared from start | Isolated arm 3+ points better, or 1.5x distinct answers at equal accuracy | Low |
| D01.07-U10 | Can a logistic predictor on our own logged ideas beat chance? | Outcome predictor as memory | memory | K04, d03, d04: needs thousands of pairs, falls cross-domain | Log features and outcomes; fit after 100+ runs. Metric: held-out AUC | AUC at least 0.65 on held-out items from a new item type | Low |
| D01.07-U11 | Does a sequential-falsification wrapper lower false accepts of our ideas? | Multi-implication test with e-value rule | G3 / S8 | K08, c15: single paper, table cells unverified | Same candidates with plain self-check vs sequential test. Metric: Type-I error, power | False-accept rate halves with power loss under 10 points | Med |
| D01.07-U12 | Does the ideation-execution gap exist on our items (pre-score overrates ideas)? | Discount on model pre-scores; confirmation of G8 | G8 | K02, K18: N=43, NLP, 2025 models | Pre-run model score vs probe outcome on 100 own ideas. Metric: Spearman | Rho under 0.2 confirms; rho above 0.4 would relax G8 for this item type | Med |

## Open questions we cannot test on our bench yet
- Whether the gap holds for real research ideas: our items are checkable puzzles, not 100-hour experiments. Unblock: a small executed-idea set with outside experts.
- Whether Nickles, Schaffner, Darden or Laudan say what the SEP summaries say: primary texts were never opened (PhilSci and PhilArchive returned 403). Unblock: library access, then re-read.
- 2026 reasoning models on idea-pair forecasting with full-paper retrieval: needs a held-out pair set after training cutoff.
- Zollman-type early isolation in LLM ensembles: needs a branching harness with controlled visibility.
- A large expert-labelled novelty set (n well above 32) to calibrate novelty gates.
- Whether LLM-panel idea scores (LiveIdeaBench, Chain of Ideas) survive execution.

## Order to run
1. **D01.07-U1 (probe vs self-score):** cheapest, and its result decides whether U2 and U3 are worth running; tests the main claim that model opinion is near chance.
2. **D01.07-U2 (allocation rule):** directly fills the pursuit decision and reuses the U1 candidates and probes.
3. **D01.07-U3 (two-tier gate):** same ideas as U1 with one extra arm; settles the Schaffner mapping, which has no direct evidence today.
