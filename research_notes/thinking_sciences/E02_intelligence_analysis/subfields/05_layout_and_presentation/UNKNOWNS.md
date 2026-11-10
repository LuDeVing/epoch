# Layout and presentation: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| E02.05-U1 | Does showing hypotheses as rows (one line per hypothesis) beat hypotheses as columns or prose for an LLM's evidence verdict? | Row-per-hypothesis rendering of the S4 evidence table | S4 | K01, K20; human-only, single-source (Dhami 2024, N=161); no LLM test | Dhami Task 1 port, 30+ item variants; HypRow vs HypCol vs HypText; 3 seeds, 5 wordings; metric: share choosing balanced answer and accuracy | Rows beat columns by 5 or more points on 2 of 3 item sets, with the format-spread interval not overlapping | High |
| E02.05-U2 | Is the row effect really processing order (one hypothesis at a time)? | Per-hypothesis sequential calls with code tally, on any layout | S4 / O | K06, K29; untested mechanism, human-only | One-shot matrix vs one call per hypothesis vs one call per evidence item, code tallies; same T1 items; metric: accuracy, tokens | Sequential arm wins by 3 or more points at equal tokens | High |
| E02.05-U3 | Does holistic per-hypothesis scoring beat cell-by-cell scoring? | Holistic scoring, code aggregates | S4 / G5 | K21, K30; argued only; nearest data essay scoring (QWK 0.6 vs 0.3) | Same items, cell-by-cell vs one holistic score per hypothesis; metric: accuracy against gold | Holistic wins or ties by 2 or more points and uses fewer tokens | High |
| E02.05-U4 | How big is the format spread of our S4 prompt on current reasoning models, and does thinking shrink it? | A standing rule: pick format per model by pilot; report ranges | G7 / O7, S4 | K11, K26; older models and typo-style perturbations only | 4 equivalent serializations x thinking on/off on our bench items; metric: max minus min accuracy | Spread above 3 points: adopt per-model pilot and range reporting. Under 2: drop the rule | High |
| E02.05-U5 | Does an ACH consistency matrix step add anything on our tasks beyond filtering and profiling? | Matrix step in S4 for evidence-weighing items | S4 | K18, K19; PRISM +0.8 on MuSR only; two human RCTs mixed | Filter-and-profile vs plus matrix on ARC, BrainTeaser, MuSR-style items; metric: accuracy | Matrix adds 3 or more points at equal tokens on 2 of 3 sets | Med |
| E02.05-U6 | Does a layout-normalizing step (fix orientation, order) before S4 cut variance? | Normalizer in code | S4 | K10, K30; table-only evidence (58.66 vs 59.50), GPT-3.5 | Scrambled orientation and row order vs normalized; metric: accuracy variance across layouts | Variance across layouts drops by half or more, mean not lower | Med |
| E02.05-U7 | Does ordering evidence in proof order help? | Order evidence by dependency in S4 | S4 | K13; single-source, synthetic deduction, older models | Proof order vs random vs reversed; metric: accuracy | Proof order beats random by 3 or more points | Med |
| E02.05-U8 | Does decisive-evidence position matter in short tables for current models? | Edge placement or position shuffle with vote | S4 | K14; contested, long-context work, older or open models | Decisive item at first, middle, last row of 6-20 rows; metric: accuracy, citation of decisive item | Middle loses 4 or more points versus edges | Low |
| E02.05-U9 | Do label slot bias and ID priors affect our hypothesis choice? | Neutral labels plus permutation vote | S4 / G5 | K15; single-source, multiple choice, older models | A-D labels vs neutral names, with and without permutation vote; metric: accuracy; slot-choice spread | Slot skew above 10 points between best and worst slot, and vote removes it | Med |
| E02.05-U10 | Does a disconfirming-test instruction at S4 raise success? | Dual-Goal line in S4 prompt | S4 / G3 | K25; single-source, synthetic rule game | Plain vs Dual-Goal on items where the right answer needs a falsifying test; metric: I:C ratio, success | Success up 4 or more points and no loss on other items (watch G1: doubt only on a signal) | Med |
| E02.05-U11 | Does free-text reasoning then code-built table beat structured-only output? | Free reasoning first, structure second | S4 | K16; single-source, GPT-3.5 and small models | Structured-only JSON vs free text then code parse; metric: accuracy | Free text wins by 2 or more points at equal tokens | Med |
| E02.05-U12 | Does an evidence graph store beat a flat table for evidence? | Graph evidence store | S2 / memory | K23; single-source, small analyst datasets | Graph vs table on multi-document items; metric: F1 or accuracy | Graph wins by 5 or more points and costs under 20% more tokens | Low |
| E02.05-U13 | Does orientation break code-execution mode on tables for current models? | Orientation guard for code-run tables | S4 | K09; GPT-3.5 only (-77.73% transposed) | Code mode with and without normalizer on transposed tables; metric: accuracy | Transposed loss above 10 points without guard | Low |

## Open questions we cannot test on our bench yet

- Per-layout counts behind Dhami's 61.8/39.2/67.3%: the 2024 raw data is not on OSF. Unblock: ask the authors for the data. Until then the percentages stay unverified.
- Any replication of the row effect, in non-students or preregistered: none exists. Unblock: wait for or commission a human study; we cannot do this.
- Which human mechanism (working memory, eye movement, reading direction) is right: needs eye tracking and cross-language readers. Only the order mechanism has an LLM analogue (U2).
- Full texts of Schkade and Kleinmuntz (1993, 1994) and Larkin and Simon (1987): paywalled or blocked. Unblock: library access.
- Format spread on frontier reasoning models for layout (not typos): no study; U4 would produce our own data, but only on our models.
- Whether results hold for 2026 frontier models at all: published layout studies are mostly GPT-3.5 and GPT-4 era.

## Order to run

1. **U4 (format spread with thinking on/off).** Cheap, and it sets the noise floor that every other test must beat.
2. **U1 (rows vs columns vs prose, Dhami Task 1 port).** The direct question nobody has answered; high value if the human effect carries over.
3. **U2 (sequential vs one-shot).** Tells us whether any row effect is layout or order, which decides what we would actually add.
