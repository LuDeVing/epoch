# Conceptual blending: what we don't know and should test
*Candidates for the schema that are not established. Nothing here goes into SCHEMA.md until its test passes. Source: DEEP.md, claims.jsonl, critique.md in this folder.*

## Test before adding
| ID | What we don't know | If it works, we add | Schema part | Evidence so far | Test (arms at equal tokens; items; metric) | Add if | Priority |
|---|---|---|---|---|---|---|---|
| C04.08-U1 | Does a blend of two failed approaches solve stuck items better than restart or best-of-N? | Operator "merge two failed attempts" in the idea tree | O7 / S6 | K25: no measured result; MoA is aggregation only (d12) | Arms: restart, best-of-N, generic-space-first blend, plain "combine". Stuck items from our bench. Metric: solve rate | Blend arm beats both restart and best-of-N by 3+ points at equal tokens on 2 batches | High |
| C04.08-U2 | Does writing the generic space first raise valid-blend rate? | Mandatory generic-space line before any merge | O7 | K06, a15, b09: single-source (bottleneck seen, no intervention tested) | Plain vs generic-space-first, Schapiro-style entity pairs, blind rubric + code role check. Metric: valid-blend rate | +5 points valid rate, 95% CI above 0, on 100+ items | High |
| C04.08-U3 | Does a verifier on the stated abstraction help or only add errors? | Check step on the generic space | G (verification) | K24, d10: Step-Back adds 11.9% new errors; single-source, other task | With vs without verify step; metric: valid rate and fraction wrongly rejected | Net valid-rate gain 2+ points and wrong-rejection under 12% | High |
| C04.08-U4 | Do persona or constraint injection reduce blend reuse across attempts? | Random persona / constraint per attempt when sampling several blends | O7 | K22, d03: single-source, ideas not blends | k=5 blends per item: T=1 vs persona vs constraint. Metric: property reuse (a16 definition) and valid rate | Reuse down 25% relative, validity down at most 3 points | Med |
| C04.08-U5 | Does an exclusion list of used properties cut reuse? | "Already tried" list in memory | memory | K07, a16: reuse real (19.9%), exclusion never tested | k=5 blends with vs without list. Metric: reuse and distinct valid ideas per token | Reuse down 30% relative with token cost under +15% | Med |
| C04.08-U6 | Does explicit keep/drop projection beat plain combination? | Selective-projection table in the blend step | O7 | K23, d07, d08: recipes only, single domain, rater alpha about 0.2 | Keep/drop table vs "combine these" vs equal-token best-of-N. Blind judges plus 20-item human check. Metric: novelty and validity | Novelty +0.3 on 5-point scale with valid rate not lower by more than 5 points | Med |
| C04.08-U7 | Does generate-five-then-filter beat single generation? | Connector generate and filter step | O7 | K12, c16, b15: human users N=10, older GPT-3, ideas counted not rated | Single connector vs 5 plus cheap relevance filter. Metric: valid blends per 1k tokens | 20% more valid blends per token | Med |
| C04.08-U8 | How often do claimed emergent properties exist in one input alone (false emergents)? | Check "not retrievable from one input" for any claimed new property | G3 / O7 | K02, K03, K10: human-only base (Hampton 3 of 174), LLM data from older or other models | Hampton-style pairs; LLM vs human lists. Metric: false-emergent rate | LLM false-emergent rate above 2x human rate, and check removes at least half | Med |
| C04.08-U9 | Does running the blend (elaboration) by code catch bad merges? | Execute merged procedure on held-out examples before accepting | G3 / G8 | a06 (theory: elaboration); contested [C]; no LLM test | Merged procedure run vs not run on procedure-style tasks. Metric: solve rate; false accepts | Accepted-merge precision up 10+ points | Med |
| C04.08-U10 | Which judge setup is reliable for blend quality? | A judging protocol (rubric + panel + human spot check) | G5 / G8 | K09, b13, b26, c18: ICC 0.48 to 0.67; no setup above 0.8 | 100 human-rated blends; single LLM vs 3-LLM panel vs rubric. Metric: ICC, agreement | ICC above 0.8 vs humans, else keep code-only selection | High |
| C04.08-U11 | Do abstraction prompts transfer from STEM questions to our items? | Abstraction-first step in S0 / O2 (generalise) | O2 / S0 | K24, d09: PaLM-2L MMLU, older model | Step-Back vs plain at equal tokens on our bench | +3 points net of new errors | Low |
| C04.08-U12 | Is the "LLMs beat humans at blending" gap real for experts? | Nothing now; sets the ceiling for expectations | none | K05, d17: lay humans only, skipped items scored zero | Needs expert-written blends on Schapiro items | Not an add; informs whether blend operators are worth tokens | Low |
| C04.08-U13 | Does a three-step identify, explain, implicate frame beat a two-step frame outside images? | Frame for blend explanation | O7 | K14, c14: image generation only | IEI vs II prompt on text blend items. Metric: blind rank | IEI wins in 4 of 5 blind pairings | Low |

## Open questions we cannot test on our bench yet
- Expert baseline for textual blends: needs expert-written blends and rated by experts; Schapiro lists it as future work.
- Replication of Coulson and Van Petten (2002) and McCubbins and Turner (2013): needs human lab work; also irrelevant to agent performance, so low value.
- Divago / COINVENT against a plain prompt: needs a shared benchmark and a working implementation of the formal systems; neither exists.
- Token cost of blend steps: no study reports it; we must measure it ourselves in every test above.
- Whether LLM blending quality in text predicts blending quality in problem solving: needs paired data from the same model on both.
- A blend-quality judge with ICC above 0.8: needs a human-rated gold set in our domain (U10).

## Order to run
1. C04.08-U1 (stuck-state blend vs restart vs best-of-N): the only test that touches real reasoning accuracy; a null here makes most other rows moot.
2. C04.08-U2 and U3 together (generic-space-first, with and without verifier): cheap, same items, and directly test the one bottleneck the literature identifies (43.4% valid generic space).
3. C04.08-U10 (judge reliability): every other blend test depends on a trustworthy score; build the human-rated gold set first or in parallel.
