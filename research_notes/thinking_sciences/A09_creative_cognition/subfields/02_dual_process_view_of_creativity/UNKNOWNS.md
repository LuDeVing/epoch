# Dual-process view of creativity: what we don't know and should test

*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding

| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| A09.02-U1 | Does diverge (constraints hidden) then bind-and-check in code beat one prompt and best-of-N? | Open-mode S3 split into "diverge" and "bind" sub-steps | S3 open, S4, S7 | K04, K18 single-source (a26, d07, c17); no token parity, no ablation | A one prompt; B best-of-N; C diverge then bind. NoveltyBench-style, design/story, code-with-tests. Distinct valid per token, blind non-same-family judge | C beats B by >=15% distinct valid outputs at equal tokens, and validity not lower by >3 points | High |
| A09.02-U2 | Does one k-candidate call with probabilities beat k separate calls? | Batch-of-k diverge call | S3 open | K20 single-source (d01, d02); matched responses, not tokens | A k separate calls T 1.0; B one k-call. Same prompts. Semantic entropy, valid fraction | B entropy >=1.3x A and valid fraction within 3 points | High |
| A09.02-U3 | Does a code-held ban list of used concepts, plus a quality gate, raise net novelty? | Direction history + "forbid these" line | S3 open, memory | K08 established for small gain (b23: +3.7 to +9.6%, -18% once); gate untested | A none; B ban list; C ban list + quality gate. Novelty = originality x quality | C beats A by >=8% net novelty and B quality not worse by >5% | High |
| A09.02-U4 | Does a signal-driven breadth/depth rule beat free sampling? | Force category switch after m same-cluster candidates; deepen productive category | O (diverge) | K02 single-source, human-only (a11-a13); LLM evidence abstract only (c07) | A free; B forced switch; C depth only; D mixed by signal. Valid originality per token | D >= B and D beats A by >=10% valid originality | Med |
| A09.02-U5 | Do interleaved generate-judge cycles beat one generate then one judge? | 2-3 cycles with failing-output feedback only | S3-S4 loop | K13, K14 human neural/EEG (a23, a24); K25 open for LLMs | A generate-all then judge; B 2-3 cycles with separate judge. Best valid novel score | B beats A by >=5% score, judge flip rate right-to-wrong < wrong-to-right | Med |
| A09.02-U6 | Does showing prior candidates cause fixation in models? | Rule for what the diverge call may see | S3 | K16 contested: human fixation (a07, d08) vs NoveltyBench abstract (d10) | A isolated; B shown earlier answers plus "differ". Semantic entropy, repeat rate | If B entropy >= A, drop "isolated" for open mode; if A beats B by >=10%, keep S3 isolation as is and mark [E] | High |
| A09.02-U7 | Does a diverge-converge stage help closed verifiable items (ARC, math)? | Diverge framing step at impasse | S6, G12 | K23 single-source; ToT 4 to 74% uses evaluator and many calls (d11); data gains only (d02) | A best-of-N + code selector; B diverge framings then test all. By plain pass-rate band | B beats A by >=3 points in the mid band at equal tokens, no loss elsewhere | Med |
| A09.02-U8 | Does a context reset (incubation analogue) help? | Optional reset-and-regenerate step on a stall | S6 | K10 contested; human g .29 (b05); no LLM source (d17) | A continue context; B reset, restate task, withhold earlier answer. Distinct valid per token | B beats A by >=5% on stalled items | Low |
| A09.02-U9 | Is code-side semantic entropy / dedup better than an LLM critic for choosing among near-equal candidates? | Entropy/coverage rule as the S7 tie-breaker | S7, G5 | K17 contested, K24 established that critics differ from humans (d04, d05, d13) | A LLM critic scalar; B entropy + dedup + coverage; labelled pools. Regret vs best available | B regret <= A and cost lower | High |
| A09.02-U10 | Are novelty and validity better scored in separate calls than in one critic? | Two rubric calls combined in code | G5, S7 | K24 (d05: GPT-4 r .13 vs human -.39); no test of the split | A one combined critic; B two calls. Agreement with human novelty-fit r | B restores negative novelty-fit r (<= -.2) or improves selection regret by >=10% | Med |
| A09.02-U11 | Do reasoning models generate worse than non-reasoning twins? | Route generate mode to the cheaper non-reasoning call | S3 | K22 single-source; no paired data (d02); c25/d16 unusable | A reasoning model; B non-reasoning twin; same selector. Semantic entropy, valid fraction | B entropy >=1.2x A at <=half tokens | Low |
| A09.02-U12 | Does extra effort on remote links (by code-measured distance) pay? | Distance-scaled thinking budget | G11, G12 | K15 contested, human only (a18: +12 vs +4.3; a19 null cue) | A fixed budget; B more tokens on remote links. Accuracy by distance | B beats A by >=5 points on remote items, no loss on near | Low |
| A09.02-U13 | Does a strategy lens (etymology, thesaurus, far persona) raise valid novelty? | Code-chosen lens per diverge attempt | O (diverge) | single-source, task-specific (b18, d06); persona conflicts with G4 on single-answer items | A plain; B lens rotated by code. Open-mode only. Valid distinct per token | B beats A by >=10% valid distinct, no gain on single-answer items (expected) | Med |

## Open questions we cannot test on our bench yet

- Token-matched comparison of LLM two-stage creative designs: no published baseline. Our bench must supply it (U1).
- Human-rated novelty with a non-same-family judge: we need a small human rating pool (about 100 items) or a trusted cross-family judge before any open-task result counts.
- Interleaving schedule and flexibility-vs-persistence in LLM search: searches hit rate limits (d17). A fresh literature pass would unblock U4, U5, U8.
- Reasoning twins for U11: need a matched pair of models on our API.
- Whether results from 2024-25 models (gpt-3.5, GPT-4, OLMo) carry to our current model: re-run before trusting any number (K05, K18 are from small or preprint settings).
- Whether the open-task gains survive when the judge is a code check (run, not opinion; G8). Needs tasks with executable validity.
- Two unread leads: Nusbaum and Silvia 2011 and Said-Metwaly 2017 (instruction effects on divergent thinking); would inform U13.

## Order to run

1. **U1** (diverge-bind vs best-of-N at equal tokens): the central question for the schema, and nobody has controlled it.
2. **U9** (code-side entropy/dedup vs LLM critic): cheap, reuses the same candidate pools as U1, and guards G5/G8.
3. **U6** (shown vs isolated candidates): one prompt change, and its answer decides how S3 open mode is built.
