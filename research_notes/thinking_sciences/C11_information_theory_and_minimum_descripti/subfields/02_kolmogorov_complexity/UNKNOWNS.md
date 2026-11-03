# Kolmogorov complexity: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C11.02-U1 | Does an explicit "state the shortest consistent rule, then check on all examples" step beat plain CoT? | A shortest-rule step before verification | S7 | K25, K20, K14 (d08, d02, c06); single-source; nothing at equal tokens; CoT on program finding was mixed (-1.3, -5.1, +2.1) | A: plain CoT. B: shortest-rule step in fixed DSL. 100 ARC items + List Functions; paired exact-match | B beats A by >= 3 points, paired CI excludes 0, on both item sets | High |
| C11.02-U2 | Does held-out error rank candidate rules better than rule length, and does length add anything after it? | Rank by held-out error, length as tie-break | S7 | K26 (d09); single-source; length not ablated; human-only theory for length | k=8 passing programs per item. Rank by (a) held-out error, (b) length, (c) a then b. Metric: accuracy on hidden test cases | (a) >= (b); (c) beats (a) by >= 2 points, else add (a) only | High |
| C11.02-U3 | Does "shortest passing program among k" beat majority vote at equal tokens? | Shortest-passing selector in code | S7, G5 | K22 (d03, d04); single-source; math not rule induction; unfinished chains excluded; k-dependent (QwQ-32B declined at large k) | Greenblatt-style filter, then (A) majority vote on outputs, (B) shortest program, (C) first-m finished then vote. ARC subset, equal total tokens; pass@2 | B or C beats A by >= 2 points | High |
| C11.02-U4 | Does a plain-words parsimony prompt close the Occam failure? | One-line parsimony instruction at S3/S7 | S3, S7 | K20 (b22, d02); single-source; CoT, buffer-of-thought, 8 demos failed to close gap; SFT only (+1.5 to +11.0) | Rule-induction items with known simplest rule. A: standard. B: parsimony prompt. Metric: rate choosing the simplest consistent hypothesis | B beats A by >= 5 points in simplest-rule rate with no loss in accuracy | Med |
| C11.02-U5 | Which cheap length proxy best tracks held-out correctness: tokens, operator count, exceptions, model log-loss? | One named proxy for S7 | S7 | K23 (d05, d02, d03, d09); each proxy works in its own setting only; d05 uses n=5 class means | 300+ candidate rules per proxy; Spearman of proxy vs held-out correctness within item | One proxy has mean within-item rho >= 0.3 and beats the others by >= 0.1 | Med |
| C11.02-U6 | How much does rule ranking change across natural language, Python and a small DSL? (invariance constant in practice) | A fixed DSL for all rule comparison | S2, S7 | K01 (a01, d15); theory only; no empirical study | Same candidate rules written in 3 languages; Spearman of rankings; top-1 flip rate | Python vs DSL rho >= 0.8 and top-1 flips <= 15%; else restrict ranking to the DSL | Med |
| C11.02-U7 | Does MDL ranking of LLM-sampled programs beat filter-then-vote on ARC? | MDL ranker after example-filter | S7 | K19 (b20, b21, d10, d14); MDL search is established, the comparison does not exist; CompressARC 20% vs LLM systems far higher | Same sampled programs; A: vote. B: rank by DSL length plus exceptions. Pass@2 at equal tokens | B >= A + 2 points | Med |
| C11.02-U8 | Does reasoning-trace length predict correctness on rule-induction items, not just math? | Cap or prefer short chains at S3 | G11, S3 | K22 (d03); single-source; math/GPQA, correlational; difficulty confound | k=4 full samples per item; accuracy of shortest/random/longest; control for item difficulty (within-item) | Shortest beats random by >= 3 points within item | Med |
| C11.02-U9 | Does an execute-and-check loop beat CoT for rule finding? | Run-compare-revise once | S4 | K14 (c06, b06); single-source; gains small (6.5 to 8.7% on MFCC); G2 already in schema | A: CoT. B: one revision from real mismatches. Rule-finding items; accuracy | B beats A by >= 3 points | Low |
| C11.02-U10 | Is rule length a usable difficulty signal for the S0 gate? | Gate on rule length / spend more tokens on long rules | S0, G12 | K23 (d05); single-source; r -0.85 to -0.96 on n=5 means; Qwen2-72B not significant (p=.065) | 500 generated rules, length 1-5 operators; item-level accuracy vs length | Item-level r <= -0.3 and spend-by-length beats uniform spend at equal tokens | Low |
| C11.02-U11 | Does a model-simplicity bias already exist so the instruction adds nothing? | Skip the parsimony instruction (saves tokens) | G7 | K15 (a16, b10); single-source; restricted expression-tree measure; older models (GPT-2, GPT-3) | Compare model's un-prompted choice among equally fitting candidates with length; correlation of choice rate and length | Un-prompted shorter-choice rate >= 65%: drop U4 | Low |
| C11.02-U12 | Does hypothesis summarisation (64 to 8) act as a filter that helps? | Summarise candidates before selection | S3, S7 | K25 (d08); single-source; GPT-4, compute unequal; 30% vs 23% | A: 8 candidates sampled directly. B: 64 sampled, summarised to 8. Equal total tokens | B beats A by >= 3 points | Low |

## Open questions we cannot test on our bench yet

- **Founding theorem statements.** Solomonoff 1964, Kolmogorov 1965, Chaitin 1966, Levin 1973 were never opened. Unblock: read the originals or the Li and Vitanyi book. Low urgency, does not change the schema.
- **Human concept learning.** Feldman 2000 effect sizes, Lafond 2007 and Vigo's critique were not read in full (d06, d07). Unblock: full text. This affects only whether human evidence supports a shortest-rule step.
- **Wan and Mei numbers.** Only few-shot selection was found (d01). Unblock: full tables; independent test against Zenil 2026 (c19).
- **True K comparison.** K cannot be computed, so no test shows that a rule is the shortest. Unblock: none; use rank agreement between proxies instead.
- **Independent critique of CTM/BDM, 2020-2026.** None found (d12, d13 are snippets). Unblock: a literature search once API limits clear.
- **Logit access.** U5 model log-loss needs token log-probs from the agent's model. Unblock: an API or local model with logprobs.
- **Item bank with known simplest rule.** U4 needs items where the simplest consistent rule is labelled. Unblock: generate from a DSL and verify by code.

## Order to run

1. **C11.02-U2** (held-out error vs length). Cheapest, and it sets the baseline every other length rule must beat.
2. **C11.02-U3** (shortest passing program vs majority vote). Same sampled programs as U2, so almost free to add, with the strongest outside signal (d03, d04).
3. **C11.02-U1** (shortest-rule step vs plain CoT). The central question the critique found nobody has tested at equal tokens.
