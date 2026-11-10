# Morphological analysis: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E07.04-U1 | Does an LLM-built box, code-sampled cells, one cell per fresh call, beat free sampling and verbalized sampling? | "Box mode" in S3 open mode | S3 | K13, K21, K24; single-source, analogues only (c13, d04, d01) | 3 arms: free, verbalized, box; 10-20 open design items with reference solutions; metric: distinct ideas at cosine 0.8, reference coverage, validity | Box beats free by 20 percent or more on distinct ideas and is not worse than verbalized on validity | High |
| E07.04-U2 | Does a random-cell or random-constraint injection alone match the full box? (cheaper) | One-line "assign a random constraint per attempt" rule | S3 | K21; single-source, GPT-4o, one task (d04: 0.735 vs 0.679) | Arms: plain, random constraint, full box; same items as U1; metric: pairwise diversity and validity | Constraint arm within 10 percent of box on coverage at lower token cost | High |
| E07.04-U3 | Are LLM pair-compatibility judgments good enough to prune? Do triple conflicts slip through? | Pair CCA step, both orders, "unknown" label, plus verification pass | S3, G | K01, K03, K23; advocate-only (a02) plus order-instability 0.07-0.44 (d03) | Toy boxes with seeded pair and 3-way conflicts; arms: no pruning, single-order, both-orders plus rubric, plus survivor check; metric: conflicts removed, valid configs wrongly removed | At least 70 percent pair conflicts removed with under 10 percent false removal; survivor check catches over half of triples | High |
| E07.04-U4 | How stable is LLM construction of parameters and values across runs? | Repeat build 3-5 times, keep majority items | G, S3 | K20, K25; proxy only (d07: 0.285 sibling pairs repeat; c21) | 5 builds on 10 problems, 2 models; metric: share of values recurring; reference coverage of consensus vs single build | Single-run recurrence under 50 percent and consensus raises coverage by 10 percent or more | High |
| E07.04-U5 | Which cell-selection rule is best when the box exceeds a cap? | Rule in code: random, covering array or diversity-greedy | S3/O | K26; untested proposals (d11, d10) | Boxes of 10^4-10^6 cells; equal number of cells; metric: reference coverage, diversity | Winner beats random by 10 percent or more on coverage; otherwise keep random | Med |
| E07.04-U6 | Is category-first (classify then combine) better than combine-first for an LLM? | A classify step before combining | S3, O3/O6 | K06; human-only, one lab (b07-b09), contested | Open design items; arms: combine-first, classify-first; metric: unique ideas, blind originality | Classify-first beats combine-first by 10 percent or more on unique ideas | Med |
| E07.04-U7 | Does an alternatives-forcing instruction reduce fixation on early concepts? | One line in the S3 attempt prompt | G, S3 | K16; anecdotal (c17-c19), recommendation untested | With and without instruction; metric: count of distinct concepts carried to S4, distinct ideas | Gain of 15 percent or more distinct concepts with no validity loss | Med |
| E07.04-U8 | Does varying model or persona across cells beat single-model enumeration on cross-run diversity? | Rotate model or persona per cell | S3, memory | K22; single-source (d05: pool 0.763 vs best single 0.756), b17 | Arms: single model, rotated persona, rotated model; 3 runs per item; metric: cross-run similarity | Cross-run diversity up 0.03 or more at equal tokens | Med |
| E07.04-U9 | Does box generation help on non-design tasks (ARC, BRAINTEASER hypothesis spaces)? | Box mode outside open mode | S3 | K28 gap 9; no study; d02 shows many-constraint degradation | Box over (object, relation, operation) vs plain attempts on our items | Pass rate gain of 3 points or more at equal tokens; otherwise keep open-mode only | Low |
| E07.04-U10 | Does logging why each option is dropped improve final quality? | Required drop log | S3, G | K07; human misuse finding (b03, b06), benefit single-source (b01, 8 teams) | Same items with and without the drop log; metric: quality of final pick, combinations carried | Quality up 5 percent or more, or log catches wrong drops | Low |
| E07.04-U11 | Do facet-wise judgments agree with human labels better than holistic ones for our candidates? | Facet-wise check in selection | S3/S5, G8 | K14; single-source (c15, c16: 0.78 vs 0.47) | Judge candidates facet-wise vs holistic against blind human labels | Agreement up 0.10 or more | Low |
| E07.04-U12 | Does the box raise or lower cross-run homogeneity (hivemind)? | A diversity guard in memory | S3, memory | K17, K22; partly (d05, c10) | 3 runs per prompt: box, persona, verbalized; metric: cross-run similarity | Box at or below persona arm on similarity | Med |

## Open questions we cannot test on our bench yet
- Chen 2024 and Park and Geum 2025 numbers: full texts are behind publisher blocks. Unblock with manual download or an institutional copy.
- Independent measurement of CCA reduction on real fields: needs a set of expert-built fields with expert compatibility labels. None found. A small expert-labelled set built by us would unblock it.
- Triple-wise conflict frequency in real boxes: no data. Needs expert labels of full configurations.
- Effect on human users of an LLM-built box (cognitive load): needs human participants.
- Whether the 2026 Terwiesch diversity result replicates across tasks: needs more tasks than one product problem.
- Quality (not just diversity) of box cells: needs blind human or outcome-based raters; model judges are near chance.
- Zwicky's "unconsidered configurations" claim: needs a count; we can only measure it in our own tests.
- Dating of Zwicky's 576 box (1947 or 1962): original sources not opened.

## Order to run
1. U1 (box vs free vs verbalized): the main question; there is no direct study, and everything else builds on it.
2. U2 (random constraint vs full box): cheap and decides whether the box is worth its setup cost under G7.
3. U3 (pair CCA accuracy with seeded conflicts): decides whether LLM pruning can be trusted, since the only reduction numbers come from the method's advocate.
