# Pruning of decision trees: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| B02.09-U1 | Does a code-triggered prune with sibling revival beat a self-score prune and no prune? | Tree rule: prune only on a failing check; revive best pruned sibling when all live branches fail | O3, G1, S5/S6 | K22, K25, d07; single-source (CodeTree) | Arms: A no prune, B test-trigger + revival, C self-score prune. Code and ARC items with checks, 100+ items. Metric: solve rate; right branches lost | B beats A and C by >=3 points with CI excluding 0, and false-prune rate under 10% | High |
| B02.09-U2 | Does an LLM prune after a big early loss in the Huys maze, and how large is the OLL-ONLL gap? | Rule: a bad early outcome never prunes; code sums the full small tree | G1, S0 | K21, K01, d13; human-only (41-point gap); LLM none | Text maze, depth 3-5, loss -70/-100/-140. Arms: plain, scaffold "no single-outcome cut", code full-tree sums. Metric: accuracy ONLL minus OLL | Plain gap >=10 points and a scaffold arm cuts it by half or more | High |
| B02.09-U3 | Is there a minimum hold time before an attempt may be abandoned, and where does it peak? | Code-enforced hold counter before S6 switch or restart | G1, S6 | K24, d02, d03; single-source, decoding-level, thinking models only | Hold 0/300/600/1000 tokens enforced by counter. Math items (AIME-like) plus our bench. Metric: pass@1, correct thought abandoned | Best hold beats 0 by >=2 points; no loss at 1000 vs 0 accepted only if a peak exists | High |
| B02.09-U4 | Does tree pruning beat best-of-N and one long line, split by item difficulty? | Gate: tree pruning on only for medium-hard items | G12, O3 | K23, d05, d06, d08; contested, 2024 models | Arms: plain, best-of-N, one long line, prune-and-expand. Mixed-difficulty set. Metric: solve rate vs tokens per difficulty bin | Prune-and-expand wins by >=3 points in a bin at equal tokens; add the gate for that bin only | High |
| B02.09-U5 | How often does a model scorer discard the eventually correct branch outside Game of 24 and crosswords? | Hard rule banning scorer-only cuts; log-based audit | G5, logging | K13, b23, d04, c06; PAC-CF is a preprint, TSP not an LLM task | Log pruned branches with oracle labels on 3 task families; score noise sweep (R=1, 4, 16). Metric: false-prune rate | False-prune rate >=20% for scorer cuts, vs <=5% for code cuts | Med |
| B02.09-U6 | Does depth-gated verification (more checks deeper) help? | Check budget grows with tree depth | G12 | K04, K26; human-only, LLM depth shallow | Problems with 3-6 step solutions. Arms: fixed checks vs checks scaled by depth. Metric: solve rate by depth | Gain >=3 points at depth 5-6, no loss at depth 3 | Med |
| B02.09-U7 | Is duplicate-merge a safer prune than score cut? | O3 expansion merges near-duplicate children by code similarity, no score cut | O3 | d01 (abstract only); single-source | Arms: score cut, duplicate merge, none. GSM8K/MATH-like trees. Metric: accuracy, node count | Accuracy within 2 points of none with >=50% fewer nodes | Med |
| B02.09-U8 | Does a rule-based legality or constraint pruner pay off outside Tower of Hanoi? | Code legality filter in S3/S4 for rule-bound tasks | G5, S4 | K18, c15, c16; single-source | Rule-bound planning items (Hanoi, Blocksworld, grid). Arms: with/without filter. Metric: invalid-move rate, solve rate | Invalid rate drops >=10 points and solve rate does not fall | Med |
| B02.09-U9 | Does a fragment stop-at-bad-result rule help decomposition? | O3 sub-problems stop at a failing intermediate check | O3 | K05, a18, a19; human-only, one lab | O3 decompose with vs without stop rule. Multi-step items. Metric: solve rate, tokens per solve | Beats plain decompose by >=3 points | Low |
| B02.09-U10 | Is a confidence early stop of an attempt worth it (when logprobs exist)? | Early stop on low group confidence inside the attempt loop | G11 | K17, c13, c14; decoding-level | Arms: full attempts vs early stop at equal total tokens (stopped tokens reinvested as extra attempts). Metric: accuracy | Accuracy equal or higher at same tokens | Low |
| B02.09-U11 | Do unchosen branches in a written trace do any work? | Cut unused branch text from prompts | G10 | K20, c04; single-source, one game | Delete unchosen branches, re-ask. Metric: answer change rate | Change under 3% with tokens saved >=20% and no accuracy loss | Low |
| B02.09-U12 | Does anxious or loss-framed prompt text change an agent's branch dropping? | Nothing; confirm 4b-style exclusion of mood prompts | G1, 4b | K08, K21, c19; contested, human link weak | Anxious, neutral, calm preprompt on U1 trees. Metric: false-prune rate, solve rate | Only if framing changes prune rate >=10 points (then add a guard, not a feature) | Low |

## Open questions we cannot test on our bench yet

- **Independent human paradigm.** Every human result is the Huys maze from one lab lineage. A second paradigm is needed to call loss-triggered pruning general. Needs new human data; not ours.
- **Cost-insensitivity (K02).** One study with groups of 15-16. Needs several groups per loss size. Cannot run here.
- **Resource-rational threshold.** Callaway 2022 was paywalled. Unblock by getting the full text, then compare its optimal threshold with gamma_S about 0.6.
- **Frontier-model ToT versus best-of-N.** Published equal-compute tests use 2024 models. Our bench (U4) is the only way to fill this; hosted frontier models need token accounting that hides thinking tokens.
- **Prompt-only hold.** The one prompt-only test failed; a decoding penalty needs logit access we may lack. Unblock with an open-weight thinking model.
- **LLM depth-by-loss effect.** LLMs search 1.78 plies; no test of loss dependence by depth. Needs U2 first.
- **Meth-study df.** F(1,100) with 89 participants is unexplained; needs the paper's supplement.
- **Depression and state attraction.** Why the 2012 effects vanished in 2022 is unknown; irrelevant to the agent unless U2 shows a state-attraction analogue.

## Order to run

1. **U1 (code-triggered prune with revival).** Cheapest (reuses existing code and ARC checks) and tests the core rule that the schema's tree depends on.
2. **U4 (prune vs best-of-N by difficulty).** Decides whether tree pruning stays on at all and for which items; it gates G12 and O3.
3. **U2 (Huys maze in text).** The one direct test of the topic; a cheap synthetic set, and a large gap would justify a hard "no single-outcome cut" rule.
