# Retrieval as a bandit: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C08.09-U1 | Does a learned per-case success value beat top-1 similarity on a frontier model? | Utility term in case choice | memory (S0 read, S9 write) | K01, K21; d01 (5 seeds, gpt-4o-mini, +1/+2/+8), c02 (+0.6 to +1.0, no seeds); older or weaker models | A: top-1 similarity. B: top-1 by 0.5 z(sim)+0.5 z(Q). Recurring-class items, 5 seeds, frozen bank | Paired gain >= 2 points, CI above 0, tokens equal | High |
| C08.09-U2 | Is the 50/50 blend better than pure similarity or pure utility? | Blend weight 0.5 | memory | K06; single source (MemRL, figure only) | Sweep lambda {0,.25,.5,.75,1}, same items as U1 | Best lambda beats both ends by >= 1 point | Med |
| C08.09-U3 | Does an exploration rule help case choice at all (greedy vs epsilon vs Thompson vs UCB)? | Thompson or epsilon step on per-case counts | memory | K03, K24; contested: CASCADE alpha=0 loses 0.31 (noise), classic sims favour epsilon/softmax/Thompson, no LLM case-bank regret study | Four rules over a long stream (300+ items); regret vs oracle best case and final pass rate | Rule beats greedy by >= 1.5 points or regret drops >= 20%; else keep greedy | Med |
| C08.09-U4 | How much of learned-value gain is memorisation of repeated items rather than transfer? | A "no repeated items" rule for all bank claims | G7, bench protocol | K20; single (MemRL cross-table: 8.15 vs 2.8) | Same arms on repeated vs unseen items, frozen bank | Repeated gain minus unseen gain over 3 points means report only unseen | High |
| C08.09-U5 | Where is the task-similarity break-even for value learning? | Class gate: use utility only above a similarity or recurrence threshold | S0 gate | K05; MemRL HLE tie at similarity 0.186, Evo-Memory r 0.717/0.563; no threshold measured | Streams with 5 levels of within-class similarity; gain of B over A | Gain >= 1.5 points above threshold t and <= 0 below; adopt t | High |
| C08.09-U6 | Does a window or discount on value beat a running mean under a task switch? | Windowed value estimate | memory | K25; theory (d13), one shift test (d09), no case-level test | Switch task family mid-stream; running mean vs window; regret over next 100 items | Window cuts post-switch regret >= 25% with no loss before the switch | Med |
| C08.09-U7 | How accurate must the success label be before a learned value beats similarity? | A minimum label accuracy for bank writes | G2, G3, S9 | K15, K22; d07 (untuned judge below fixed memory; tuned recovers); d14 (lessons tolerate noise); no threshold for selection | Inject label noise at 100/90/80/70/60% accuracy; compare with similarity-only | Report break-even; require label accuracy above it (or code-verified only) | High |
| C08.09-U8 | Under a learned selector, do raw failures, failure lessons, or success-only banks do best? | Failure-lesson store attached to class | memory, S9 | K26; indirect (d14, d16, d19); no learned-selector ablation | Three banks, same selector, same tokens | Lessons beat success-only by >= 1.5 points and raw failures do not | Med |
| C08.09-U9 | Does a redundancy penalty (set-level selection) help when K>1 and the bank has near duplicates? | Marginal-relevance term | memory | K09, K10; b08, b09, d17 (old models, semantic parsing) | Duplicate-heavy bank, K=3, top-K vs greedy with penalty | Gain >= 1.5 points on duplicate-heavy, no loss on diverse | Med |
| C08.09-U10 | At equal tokens, is one sample with a learned-value case better than N samples with a verifier? | Rule on when to spend tokens on bank vs on sampling | G7, G12 | K27; d03 (call counts, oracle verifier), d18; no equal-token study | Match total tokens; checkable and non-checkable items | Learned-value arm wins on non-checkable items by >= 2 points; else sample when a verifier exists | High |
| C08.09-U11 | Is the spread between random case sets large on our model (is there anything to win)? | Skip value learning where spread is small | S0 gate, G7 | K11; GPT-2 spread over 30 points (old); frontier spread unknown | 20 random K-sets per class; max minus min and SD | Spread >= 5 points on a class means value learning is worth testing there | High |
| C08.09-U12 | Does utility-based deletion keep quality at a quarter of the bank size? | Periodic prune plus utility eviction | memory hygiene | K23; single source (d08), works only with strict evaluator | Full bank vs retrieval-count prune vs utility eviction at 25% size | Within 1 point of full bank | Low |
| C08.09-U13 | Does successive halving over a case shortlist per class pick better cases cheaply? | Shortlist-and-halve step for class cases | O/memory | K16; TRIPLE, INSTINCT are prompt pools; gains fade with budget | Shortlist of 8 cases per class, 3 probe items each, halve, compare with top-1 similarity | Gain >= 2 points with probe cost inside the token budget | Low |
| C08.09-U14 | Can credit be assigned when several cases are shown together? | Shared-credit update rule | memory | Gap 6; unsolved (MemRL admits it); Sarukkai uses retrieval-frequency weighting | K=3 shown; compare equal split, leave-one-out probes, frequency weighting | A scheme beats equal split by >= 1 point in value calibration and pass rate | Low |

## Open questions we cannot test on our bench yet

- Independent replication of CASCADE: needs its code, data and a Qwen3 backbone; we have none of these on our bench. Unblock: wait for released code or reimplement on one public task.
- Frontier-model results with seeds and CIs for any published method: published numbers are single runs. Unblock: our own multi-seed runs (U1).
- Effect of 1990s case-based reinforcement learning and retention-policy work (Smyth and Keane, Thompson 1933): sources not obtained. Unblock: a targeted literature pass.
- Whether random-label insensitivity (format over content) holds for current frontier models: only older models tested. Unblock: a label-corruption run on our bench.
- Learned reranker trained from LM feedback (EPR style): needs a training set and a scoring pass per candidate; the agent is training-free. Unblock: a small offline run to see if any gain justifies breaking the no-training rule.
- Human-subject evidence on outcome-weighted case retrieval: not in these files. Unblock: pull from the related human-memory subfields.

## Order to run

1. C08.09-U11 (spread check): costs only sampling, and tells us per class whether any case-value test can pay.
2. C08.09-U1 with U4 (learned value vs similarity, repeated vs unseen items): the core question and the memorisation control; every later test builds on it.
3. C08.09-U7 (label accuracy break-even): decides whether bank writes can use a model judge or only code-verified outcomes, which affects every other item.
