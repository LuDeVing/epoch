# Shannon information, entropy: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C11.01-U1 | Does EIG over a filtered hypothesis list beat plain probe choice on open tasks? | S7 step: list hypotheses, filter in code, score probes by EIG, run best | S7, memory | K12, K13, K14; a21, b16. Single-source, closed sets only | A: model picks probe in one call. B: hypotheses + code filter + 5 probes + code EIG. Equal total tokens incl. setup. 100+ ARC/BrainTeaser items. Accuracy | B beats A by 5+ points, 95% interval above 0 | High |
| C11.01-U2 | Below what hypothesis-list coverage does EIG stop helping or hurt? | A coverage check at S0/S7 that skips EIG when coverage is low | S0, S7 | K14, K28; d04 (49 of 100 ARC tasks had the truth in the list). Single-source | Run U1, bin items by truth-in-list. Compare B minus A per bin | A coverage threshold exists where B-A is 0 or below; use it as the gate | High |
| C11.01-U3 | Does filtering the belief set against all outputs matter outside 20 Questions? | Mandatory code filter on hypotheses | S7, G3, memory | K14; b17, b25 (93 vs 25). Single-source | B with vs without filter, equal tokens, same items as U1 | Filtered beats unfiltered by 10+ points | High |
| C11.01-U4 | Is EIG (predictive minus likelihood entropy) better than raw answer entropy as the probe score? | EIG formula, not raw entropy | S7 | K13; a22, b17, d09. Single-source | Two scoring rules, same list, equal tokens. Include noisy-answer probes. Accuracy | EIG beats entropy by 4+ points, or equals it at lower cost | Med |
| C11.01-U5 | Does probability gain (expected error drop) beat Shannon EIG for an LLM agent? | Probability gain as probe score | S7 | K23; b05-b08, b26. Contested, human-only, abstracts only | Same list, score by expected error drop vs expected entropy drop. Fixed probe count. Accuracy | Probability gain wins by 3+ points on 100+ items, or ties at lower cost | Med |
| C11.01-U6 | Does a static likelihood prompt (no history) beat a history-conditioned one outside 20 Questions? | Rule: history in belief set only, never in scoring prompt | S7, memory | K29; d07 (13 of 15 cells). Single-source, one task type | Static vs history-conditioned scoring, equal tokens, 100+ items | Static is equal or better and cheaper | Med |
| C11.01-U7 | How many candidate probes (k) are worth scoring at equal tokens? | Fixed k in S7 (likely 5-10) | S7, G12 | K15; b21, c14-c16 (Battleship k=1,5,10,50). Single-source | k = 1, 3, 5, 10 at equal total tokens. Accuracy and EIG of chosen probe | Smallest k within 2 points of the best k | Med |
| C11.01-U8 | Which stop rule ends probing best: top weight, EIG floor, Beta test or fixed budget? | Stop rule in S7 | S7, G7 | K20, K26; a20, d02, d03. Established for answer sampling, untested for probes | Four rules, same items, equal budget cap. Accuracy vs tokens; wasted probes after resolution | Rule saves 30%+ tokens with accuracy within 1 point of fixed budget | High |
| C11.01-U9 | Does cluster (semantic) entropy or top-answer share gate multi-step reasoning, and how many confident-wrong items pass? | A calibrated gate that routes low-share items to O1-O8 | S7, G1, G4 | K06-K08, K10, K27; a15, a17, d14. Single-source group; factual QA only | 5-8 samples per item. AUROC for correctness: cluster entropy vs share vs verbalised confidence. Plus accuracy among share above 0.8 | AUROC 0.75+ on ARC/BrainTeaser and confident-wrong rate under 10% of passed items | High |
| C11.01-U10 | Do verbalised top-3 probabilities calibrate better than agreement on reasoning items? | Verbalised confidence as gate input | S7, G | K30; d05. Single-source, factual QA | Ask for top-3 with probabilities; compute ECE on held-out ARC/BrainTeaser slice vs agreement share | ECE lower by 25%+ relative to share, at no extra samples | Low |
| C11.01-U11 | Is per-item log-loss or compression of the agent's answer a usable correctness proxy? | Cheap item-level check for open models | S0, S7 | K04; c21. Model-level only, single-source | Open model: AUROC of answer log-loss for correctness vs agreement share | AUROC 0.7+ and adds to agreement share | Low |
| C11.01-U12 | Does unaided probe choice on logic-style items improve if the agent builds an explicit hypothesis tree first? | Tree-first probe choice for logic items | S7, O3 | K31; d10 (40-50% on Logic-Q, Planning-Q). Single-source | Plain choice vs tree-first, equal tokens, logic items. Accuracy of chosen probe | Tree-first wins by 10+ points | Med |
| C11.01-U13 | Does information gain per reasoning step work as an online step score (no gold answer)? | Step score for S6 control | S6 | K21; c19. Single-source, toy arithmetic, needs gold answer | Replace gold with majority answer as target; compare to outcome-only scoring on our traces | Separates right from wrong steps with AUROC 0.8+ | Low |

## Open questions we cannot test on our bench yet

- **Open-ended hypothesis generation quality.** We have no way yet to know whether the true rule is in the list without gold labels at run time. Unblock: label the true rule for a held-out item set and measure coverage offline.
- **Accuracy of p(y | h).** How noisy are LLM-estimated outcome likelihoods? No paper measured it. Unblock: use probes with deterministic outcomes (code runs) as ground truth, compare to LLM-estimated likelihood.
- **Independent replication of semantic entropy.** All evidence is one group. Unblock: our own replication in U9 would serve as the first outside check.
- **Cover-King 1978 and Oaksford-Chater 1994 numbers, and any failed replications.** Pages could not be opened. Unblock: open the papers; low value for the schema.
- **Hoffmann E unit.** Inferred as nats, not stated. Unblock: check the paper's loss definition. Context only, no schema effect.
- **Semantic entropy probes and entropy-preserving RL.** Need weights or training. Unblock: an open-weight track, outside the scaffold-only agent.
- **Human probe choice (Shannon gain vs probability gain vs impact).** Review-level evidence only. Unblock: read Nelson 2005/2010 and Crupi 2018 in full; U5 gives the agent-side answer.

## Order to run

1. **U1 with U2 and U3 as sub-analyses.** It is the main question: does EIG-over-filtered-hypotheses beat plain probe choice at equal tokens on open items? One run answers three rows, and it decides whether the rest matters.
2. **U9.** Cheap (samples only, no new machinery), tests the confident-wrong risk that guards G1/G4, and gives the first outside check of semantic entropy.
3. **U8.** Stop rules save tokens whether or not EIG wins, and LLMs are known to keep probing after resolution (K20).
