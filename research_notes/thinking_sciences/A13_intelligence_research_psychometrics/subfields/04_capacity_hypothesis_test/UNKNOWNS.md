# Capacity hypothesis test: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A13.04-U1 | Does a budget set by fitted (1PL) difficulty beat one set by rule count? | Budget by fitted difficulty from a running class record | G12, S9 | K24, K17, d16, d17: single-source, coding-agent data only | Arms: A tokens by rule count, B by fitted difficulty, C both; our task bank, 1PL from 4+ agent variants; pass rate at equal total tokens | B beats A by 3+ points absolute, with 95% CI above 0 | High |
| A13.04-U2 | Does the best token cap rise with item difficulty on our bench? | Per-difficulty-class cap instead of one global cap | G11, G12 | K23, d13: single-source, math only, two distilled models | Caps 1x, 2x, 4x, 8x across 4-5 difficulty bands; metric pass rate by band; also overthinking flips | Optimal cap differs by 2x or more between easiest and hardest band, and per-band caps beat the best global cap by 2+ points | High |
| A13.04-U3 | Does the collapse point of our agent move with added capacity (notes slot, code decomposition, size)? | A capacity-by-demand check before claiming any capacity fix | G12, G7 | K19, K21, d06, d18: single-source, no study exists | Three capacity levels, items by fitted difficulty; metric: item demand where pass rate falls below 50% | Break point moves by 1+ difficulty band between levels, repeated on 2 item sets | High |
| A13.04-U4 | Does jointly-bound item count (relational complexity) trigger decomposition better than length? | RC estimate in S2 that triggers O3 | S2, O3 | K10, b25, b26, d06: two 2026 preprints, 3 models, synthetic tasks | Items with RC fixed and size varied, and the reverse; arms: decompose by RC, by length, never | RC trigger beats length trigger by 3+ points on high-RC items and costs no more than 10% extra tokens | Med |
| A13.04-U5 | Does code do the binding (not only the counting) at high load, or must the model still hold a joint set? | Rule: code takes enumeration and indexing; joint-binding steps get compression | O3, G5 | K22, d10, d11, d12: contested, tool arm not paired | Same model with and without code on high-RC items; log which step fails | Code arm gains 5+ points on high-RC items, with failure logs showing the step moved to code | Med |
| A13.04-U6 | Does a fixed notes slot for the current rule cut set-maintenance errors? | Notes slot of the current rule in revision | S5 | K18, c20, c21: single-source, p=.052, 10 LLMs, small human N | Notes vs none on rule-switching items; perseveration count and pass rate | Perseveration errors fall 20%+ and pass rate does not fall | Med |
| A13.04-U7 | Is distractor count a separate dial from load, and does it hurt our agent? | Input hygiene rule that trims same-format distractors | S1, G1 | K08, d08, d09: contested, retrieval only | Distractor-length sweep at fixed reasoning load; accuracy against distractor count and load | Distractor slope significant (p<.05) after controlling for load, and trimming recovers 3+ points | Med |
| A13.04-U8 | Does reasoning off beat reasoning on for text multiple-choice matrix-style items? | Mode choice at S0 for matrix-type classes | G11, S0 | K15, c20: single-source, p=.021 on 4 models, older prompts | Reasoning on, off, capped at equal tokens on our matrix items | Off or capped beats on by 3+ points on the class, replicated on 2 item sets | Med |
| A13.04-U9 | Does unique-rule diversity (not total rule count) predict failure for current reasoning models? | Unique-rule count as a difficulty feature | S2 | K11, a20: single-source, GPT-3 only | Items with fixed total rules, varied unique rules; accuracy | Odds ratio below 0.7 per added unique rule, with CI excluding 1 | Low |
| A13.04-U10 | Are apparent capacity failures really task misreadings or output cut-offs on our bench? | Comprehension check and truncation flag in S1/S4 | S1, S4 | K14, K13, c11, d12: contested | Audit failed runs by code: truncation flag, answer fits a different task | 10%+ of failures are cut-offs or misreadings; then add the check | High |
| A13.04-U11 | Does one long attempt or several short ones win at high load? | Short-attempt default confirmed or limited at high RC | G11 | K13, c15, d10, d13: contested | Equal total tokens: 1 long vs 4 short attempts on high-RC items | Several short win by 3+ points, or long wins by 3+ (then a limit is added) | Med |
| A13.04-U12 | Is a perception-free (symbolic) input worth it, since perception errors can dwarf rule errors? | Code converts images or text to symbols before rule search | S1, S2 | K12, b28, a23: single-source, two models | Same items as symbolic and as raw; error split into perception vs rule | Symbolic arm gains 5+ points and the conversion costs under 20% of tokens | Low |
| A13.04-U13 | Does a novelty-only penalty exist for our agent? | Nothing (confirms a null so we do not add a novelty rule) | O6 | K05: refuted in humans | Novel vs repeated rule combinations at equal difficulty | No difference larger than 2 points; if larger, add a novelty flag | Low |

## Open questions we cannot test on our bench yet
- Dokic 2025 study count, inclusion rule and coding: needs the paywalled full text. Unblock by getting the PDF via a library.
- Little 2014 second study (RSPM) supplement: not read. Unblock by opening the supplementary file.
- Carpenter 1990 and Kyllonen and Christal 1990 original numbers: never opened. Unblock by scanning the originals.
- A true capacity-by-demand sweep on frontier models needs several model sizes with the same scaffold; we only have one agent, so only notes and decomposition levels are reachable.
- Fitted difficulty across models: whether different models rank items alike. Needs responses from 4+ models on one bank.
- Whether humans fail like LLMs on our items: no human control group.
- Attention control versus capacity as the better account of LLM failure: needs a design that separates them on one reasoning task.
- Backward digit span versus Raven in 15 LLMs (snippet only): needs the paper.

## Order to run
1. A13.04-U10 (truncation and misreading audit): cheapest, uses existing runs, and protects every other test from a confound.
2. A13.04-U1 (fitted-difficulty budget vs rule-count budget): directly answers the correction to our first draft, and G12 is the largest lever.
3. A13.04-U2 (cap-by-difficulty grid): the same difficulty labels from U1, and it settles whether G11 needs a per-class cap.
