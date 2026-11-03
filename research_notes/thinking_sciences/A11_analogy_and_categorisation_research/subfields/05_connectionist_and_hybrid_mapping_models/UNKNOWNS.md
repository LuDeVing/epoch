# Connectionist and hybrid mapping models: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A11.05-U1 | Does an explicit scored mapping step (candidate correspondences scored on structure, meaning, goal; one-to-one check) beat free CoT? | O7 as a typed table step before answering | O7 | K01, K02; single-source, human and ACME-sim only; no LLM test | Free CoT vs scored table. 100+ cross-mapped and far-story items. Metric: accuracy, surface-object error rate | Gain of 5+ points on cross-mapped items, no loss on easy items, tokens within 1.3x | High |
| A11.05-U2 | Does chunked serial mapping (4 to 6 bindings per step) beat single-pass on many-correspondence problems? | Binding cap per step in O7/O3 | G budget, O7 | K04, K26; LISA single-source, indirect LLM support (load collapse) | Single pass vs chunks of 4 vs 6. Generated mappings with 3, 6, 10, 15 correspondences. Metric: accuracy by load | Chunked arm gains 8+ points at 10+ correspondences, no loss at 3 | High |
| A11.05-U3 | Do 2025-26 reasoning models pass counterfactual letter strings, and is a code tool the cause? | Rule: route index and counting steps to code | tools, G3 | K11, K12; contested (Webb vs Hodel/West/Lewis); no data for o-series or Claude 4+ | No tool vs code tool, intervals 1 and 2, symbol alphabet. Metric: accuracy vs human reference, split by lookup-dependent items | Tool arm gains 15+ points on lookup items at equal tokens | High |
| A11.05-U4 | Does a structure check before transfer stop surface-driven wrong-analog use? | Retrieve then verify-by-structure step in memory use | memory, O7 | K05, K25; single study (GPT-4 precision 0.5 with hint) | Retrieve-and-use vs retrieve, structure-check, use. Memory with near, far, surface-distractor analogs. Metric: precision, recall, final accuracy | Precision up 0.2+ with recall loss under 0.1 and accuracy not lower | High |
| A11.05-U5 | Does a 70% importance-weighted coverage gate cut unsupported analogical inferences? | Gate on any inference carried over by analogy | O7, S8 | K08; LISA single-source simulation only | No gate vs 70% vs 50%. Inference questions where support is absent. Metric: unsupported-inference rate, true-inference recall | Unsupported rate down 30% relative with recall loss under 10% | Med |
| A11.05-U6 | Is re-describing while mapping (Copycat style) better than mapping from one fixed description? | Re-describe on failing check inside O6/O7 loop | O6, O7 | K09, K24; ConceptSIR 9/17, no control arm | Fixed description + N resamples vs re-describe after failing check. ConceptARC, ARCANA-like items. Metric: solve rate | 5+ points more solved, same tokens | Med |
| A11.05-U7 | Does anonymising entity names before mapping reduce surface errors? | Neutral-token pass in S1/O6 for relational items | S1, O6 | K19, K28; indirect (relational bottleneck, probing) | Original vs neutral tokens. Cross-mapped and misleading-meaning items. Metric: accuracy on misleading items, accuracy on normal items | Gain 5+ points on misleading items, loss under 2 on normal | Med |
| A11.05-U8 | Are self-generated analogs worth their tokens against self-consistency and verified fixed exemplars? | Keep or drop self-generated analog step in O7/O2 | O7, O2 | K17, K18; contested (Yasunaga +4% vs Qin: relevance hurt on math, 52.4 vs 55.8) | Plain CoT vs self-generated vs verified fixed vs self-consistency, same tokens. GSM8K-style, BBH subsets. Metric: accuracy per token | Beats self-consistency at equal tokens by 2+ points on two item types | Low |
| A11.05-U9 | Does scoring the stated rule (not only the answer) catch spurious passes cheaply? | Log rule + check rule on held-out input as part of S8 | S8, G3 | K22; one benchmark, 27% vs 7% | Answer-only vs answer+rule with held-out application. ConceptARC subset. Metric: wrong-rule share among accepted answers | Wrong-rule share drops by half at under 15% extra tokens | Med |
| A11.05-U10 | Does stating the example input-output correspondence before applying the rule help? | Explicit matching step in S2 | S2 | K27; small-transformer study only | Direct rule vs "list what maps to what" then rule. Letter strings with new alphabets. Metric: accuracy on new alphabets | Gain 5+ points, tokens within 1.2x | Low |
| A11.05-U11 | Does splitting "state the relation" from "apply it" help? | Two-step relation statement and application | S2, S3 | K28; patching in open 7B-14B models | One-pass vs two-step on proportional and story analogies. Metric: accuracy, failure split (missing vs misapplied relation) | Gain 4+ points at equal tokens | Low |
| A11.05-U12 | How large is the surface-overlap shortcut on our own analogy items, and does an invariance gate remove it? | Invariance gate (order swap, paraphrase, symbol permute) as standing check | G3, S1 | K14; established on stories (86% to 72%; 89% vs 61%) but gate cost untested | Gate vs no gate on stories, digit matrices. Metric: accuracy on shortcut-free variants, tokens | Accuracy on shortcut-free variants up 5+ points, cost under 1.5x | High |
| A11.05-U13 | Does an explicit goal statement before mapping change mapping for the better in LLMs? | Goal line feeds the mapping step | S0, O7 | K07; human and LISA only (43% vs 35%; 29% vs 65%); human-only | Goal-blind vs goal-stated mapping on items where goals pick different correspondences. Metric: match to goal-appropriate mapping | Goal-appropriate mapping up 15+ points | Med |

## Open questions we cannot test on our bench yet

- Whether LLM success comes from attention implementing ACME/LISA-like binding: needs mechanistic ablation on open models; our bench has no activation access.
- Whether the human size of effects (Ross mapping, Spellman and Holyoak) holds in LLMs: needs a large item set built from those materials; we have no such set.
- Whether serial-capacity limits in LISA correspond to any LLM limit: needs binding-load sweeps with open models and probes; partial analogue in I-RAVEN-X only.
- Missing original numbers: Holyoak and Thagard 1989 Tables 4 and 5, Ross numbers in the 1997 paper, Lewis and Mitchell Table 2 row order. Needs the printed papers or clean figures.
- Open-domain scale-up of ACME/LISA-style scoring: no system exists; we would need a proposition extractor and a validator for it.
- Reasoning models on counterfactual letter strings: no public result; our own run is the unblocker (U3).
- Copycat-style loops with a matched control: needs us to build both arms at equal tokens (U6).

## Order to run

1. **U12 invariance gate** (with A1/A2 checks). Cheapest, established problem, and every other test depends on trusting its scores.
2. **U1 scored mapping step.** Highest expected gain on the core job of the subfield and cheap to build as a prompt.
3. **U3 code tool on counterfactual letter strings.** Settles the main open dispute and decides whether index work goes to code.
