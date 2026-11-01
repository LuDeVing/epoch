# Combinational creativity: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C04.03-U1 | Does extracting and code-checking a shared abstraction before blending beat just sampling more? | S2 step "name the shared relation" inside O7 | O7, S2 | K01, K02; a05 single-source, LLM judges | A direct; B abstraction-first; C direct with samples matched to B. 60 cross-domain items with a check. Valid-blend or pass rate | B beats C by at least 5 points on 3 seeds | High |
| C04.03-U2 | Do far sources beat near or none when scored by execution? | Rule for when O7 picks far vs near | O7 | K28 open; K06, K07 human-only; critique gap 1 | A none; B near; C far; D random. 60 items with unit tests. Pass rate and held-out pass | C above B by at least 3 points on impasse items, or no loss with higher diversity | High |
| C04.03-U3 | Is "mostly near plus one far element" better than all-near or all-far? | Bounded-insert rule for O7 | O7 | K23; d01 citation data, human, single-source | A all-near; B all-far; C near base plus one far. Same items as U2. Pass rate, distinct passing solutions | C beats both by at least 2 points | Med |
| C04.03-U4 | How many iterations on a far combination pay at equal tokens? | Cap of N rounds for O7 children | S5, O7 | K06 marginal p=.07 human; K26 Nova, not equal tokens | 1,2,3,4 rounds with the failing output shown, far source in all arms. Pass rate per token | Round 2 or 3 beats round 1 by 3 points and later rounds add under 1 | Med |
| C04.03-U5 | Does a purpose/mechanism-keyed memory beat full-text embedding for finding a useful earlier solution? | Typed index for the subgoal library | Memory | K08; a14, d08, d09 humans, same group, no replication | A full-text embedding; B purpose plus mechanism fields; C none. Items sharing mechanism but not wording. Top-3 hit rate and downstream pass | B beats A by 10 points on hit rate and 2 on pass | High |
| C04.03-U6 | Does a code-drawn source domain per branch raise unique ideas without lowering validity? | Source forcing in S3 open mode | S3, O7 | K12 convergence established; fix only a09 (toy tasks) | A temperature only; B random source per branch; C B plus dedup. Unique ideas per 1,000 tokens at cosine 0.8; best-of-8 pass | B raises unique yield by 30% with pass rate within 1 point | High |
| C04.03-U7 | Does running the mapping on a counterfactual or reordered variant catch wrong mappings? | Variant-consistency check on every O7 mapping | G3, O7 | K04 contested, K24; older models only (GPT-3 to 4) | A trust mapping; B accept only if variant answer is consistent. 80 mapping items with permuted twins. Wrong-acceptance rate, final accuracy | B cuts wrong acceptances by 30% and costs under 15% extra tokens | High |
| C04.03-U8 | Does a forced conflict list and repair raise validity of a mapping? | Conflict-and-repair slot in O7 | O7 | b04 cited theory, untested | A map; B map plus conflicts and repair. Cross-domain design items with execution or hidden-reference rubric | B beats A by at least 3 points | Med |
| C04.03-U9 | Does facet decomposition (purpose, mechanism, evaluation) improve novelty checking against prior art? | Facet-based prior-art check in open mode | S7 | K17; b12 43 items, small | A holistic check; B facet check. Known-copy and known-novel ideas. Detection accuracy | B beats A by 10 points on 40 or more items | Low |
| C04.03-U10 | Does recalling 2 related solved problems before solving help our backbone? | Near-analogue pre-step | O7 (near), Memory | K15; b17 GPT-3.5 only, +1 to +3 | A plain; B recall then solve. Exact-answer items. Accuracy | B beats A by 2 points on a mid-strength backbone | Low |
| C04.03-U11 | Does a counted tried-pairs list widen exploration of combinations? | Tried-pair record in memory | Memory | K20; a19 not an LLM scaffold | A none; B list shown after first attempt. Repeated runs on one class. Distinct pairs and pass rate | B gives 20% more distinct pairs, pass rate not lower | Low |
| C04.03-U12 | Does the model use far candidates when offered, or silently skip them? | Usage log plus forcing step if skipped | O7, logging | K16; Scideator humans, self-report | Log the fraction of far candidates cited in the final answer in the U2 far arm | Under 50% used and U2 shows far helps: add a forcing step | Med |
| C04.03-U13 | Does a cheap far-association probe predict O7 gain for a given backbone? | Probe in S0 to decide whether to run O7 | S0 | K14 weak; a08 r=0.73 across models, correlational | Run the probe on 3 backbones; correlate with U2 gain | Rank agreement on all 3 backbones | Low |

## Open questions we cannot test on our bench yet
- Open-ended ideas with no check: we have no cheap validity test. The only strong one is human execution (100+ hours). Would unblock: a proxy such as held-out tests built from the idea's own claims, validated against a small human-rated set.
- Counterfactual analogy on Claude-class and reasoning models: published results stop at GPT-4. Our own run of the U7 items on current backbones would answer it.
- Replication of Hope et al. (purpose/mechanism) and Gu et al. (matched references): needs their code or corpus. Gu et al. have no ablation of L1 to L4.
- Whether Uzzi's "conventional plus a little atypical" survives newer data, and how it squares with Shi and Evans (primary not opened).
- Which abstraction level (L1 to L4) works best: needs four levels built per stored item in our memory first.
- Human diversity as a source (KOMBINE: humans use different regions of concept space): needs the multiplayer data layer.
- Mixing backbones to cut homogeneity: same-family excess was +12.2 pp for DeepSeek, +11.1 for Anthropic, -1.4 for OpenAI. Needs a cross-family run.

## Order to run
1. **C04.03-U2 (far vs near vs none, executable score).** The central gap: no study answers it, and it decides whether O7 uses far sources at all.
2. **C04.03-U1 (abstraction-first vs matched extra samples).** Cheap, and KOMBINE says the shared abstraction is the bottleneck. The matched-sample arm guards against a pure token effect.
3. **C04.03-U7 (variant-consistency guard).** Cheapest to run, uses items we already have, and tests the best-supported weakness (brittle mapping) on current models.
