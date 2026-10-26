# Creative cognition: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl (two or more independent sources). "Contested" and "single-source" claims are named only where they matter for a contradiction or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most established human findings here are design hints for the agent until tested on our model (section 5). Claim ids are global, for example A09.06-K32; unknown ids look like A09.06-U4. Several established claims carry an "update" in their text that adds LLM evidence from 2024 to 2026 preprints; those updates are single papers and are noted where they matter.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Geneplore model | [DEEP](subfields/01_geneplore/DEEP.md) | 31 | 9 |
| 06 Fixation, functional fixedness and structured imagination | [DEEP](subfields/06_fixation_and_structured_imagination/DEEP.md) | 40 | 15 |
| **Total** | | **71** | **24** |

Contested: 9 (6 + 3). Single-source: 38 (16 + 22). Each subfield has a UNKNOWNS.md with 14 test rows (28 in all).

Not yet researched (from `SUBFIELDS.md`): dual-process view of creativity; conceptual blending and integration; conceptual combination (noun-noun); process stage models and incubation; divergent thinking; ordinary-cognition and implicit-explicit theories (Weisberg, Helie and Sun, Gabora); analogy and distant sources (covered by A11, not here). The numbering gap (01 and 06 only) suggests 02 to 05 were planned and are not done. Structured imagination (Ward) was folded into subfield 06.

## 2. Established findings, merged

Only status established. "Schema part" is the claims' own tag. Human results are marked (H), LLM results (L).

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| M1 | (H) Shown example designs are copied: feature overlap rises, output count does not fall. Conformity, not fluency, is the cost. Copying grows with the number of examples (that trend is single-source, A09.06-K04). (L) Own-output anchoring is documented for a code model (33-68% near copies vs 2-14% blind, a 2026 preprint). Conformity on creative tasks by feature overlap is not yet shown for LLMs. | A09.01-K03, A09.06-K03 | G4, S3 | partly (S3 fresh contexts; lessons shown only after the first attempt, section 5) |
| M2 | (H) Conformity is not removed by a delay (23 minutes: no fade; one day: it rose) or by a "be different" instruction. It behaves like unintended memory activation. "Not bound by Earth" wording did cut reliance (48% vs 62-66%). Chat-template tokens also lower output diversity. | A09.01-K04, A09.06-K30 | G4, S3 | partly (same as M1; nothing on instruction wording) |
| M3 | (H) New ideas inherit the standard properties of the known category (aliens: sense organ 99%, appendage 97%, symmetry 91%, N=71; classroom replication 72% legs). Constrained designs adapt Earth tools rather than drop them. | A09.06-K06 | S3 | no |
| M4 | (H) Showing an object in its usual role slows use in a new role (candle problem: 11.08 min and 16 of 32 failed vs 3.67 min and 2 of 32). About 25% find the solution unprompted. | A09.06-K01 | S2, O6 | partly (O6 change representation; no input-framing rule) |
| M5 | (H) Prior knowledge fixates: experts do worse on items where their strong association is wrong; extra working memory does not help. (L) Reasoning-trained models are not immune (R1 52%, V3 50%, o1 48% vs 66% physicians; the R1 vs V3 gap is two points with no separate test). | A09.06-K08, A09.06-K34 | S2, G3 | partly (G3 held-out pass; G11 says think briefly, nothing on strong-prior traps) |
| M6 | (L) Default models solve far fewer fixedness-style problems than people (MacGyver 35-42% vs 65.1%; BrainTeaser 63% and 53% vs 92%; part-level correctness .19 vs entity .51). Models pick a plausible object and miss the right part. | A09.06-K22 | S2, O6 | no (a test bed, not a rule) |
| M7 | (L) Open-ended output collapses inside one model and across models: 79% of queries had mean pairwise similarity above 0.8; 1.76 distinct answers in 10 samples for Claude-3.5 Sonnet; LLM pools are less diverse than human pools (GPT-4 cosine .255 to .432 vs .243); larger models in a family were less diverse. | A09.01-K15, A09.06-K15 | G4, S3 | yes (G4 samples not independent; S3 fresh contexts) |
| M8 | (L) Different models share one semantic region even under defixation prompts (cross-model distance .21 to .34). Mixing vendors is not a free escape. | A09.06-K16 | G4 | partly (G4 says samples from one model are correlated; nothing on cross-model) |
| M9 | (L) Structured multi-step prompting raises idea diversity (title, revise to bolder, expand: slope 1.013 to 1.363, categories 18.45 to 24.84; critique-and-edit best of eight; method-inspired prompts +10% to +41% novelty). Most arms were not token-matched and none scores the single best pick. The same chain did nothing for humans. | A09.06-K18 | S3, O2 | no |
| M10 | (L) Generic "be creative", "think outside the box" or "think like X" prompts do little. Asking for novelty in the prompt does little. (H) A "be creative" instruction left reliance on Earth fruit at 62% vs 66%. | A09.06-K19, A09.01-K16 (prompt part), A09.01-K04 (Ward Exp 4) | none | partly (4b rejects "slow down" prompts and creativity training; this exact item is not listed) |
| M11 | (L) Temperature is a weak lever. Higher temperature raises rated novelty (beta .308) but incoherence too (beta .240); GPT-4o categories 22 to 23 at 1.5 vs 28 for humans; at 2.0 output is garbled. | A09.01-K16, A09.06-K38 | S3, G7 | no |
| M12 | (L) Hard constraints trade correctness for novelty: GPT-4 pass@1 fell 16.1% to 2.1% across five technique bans while divergent creativity rose 4.5% to 15.3%. Standard reasoning scaffolds shifted divergent for convergent gains. | A09.01-K19 | O4, S6 | partly (O4 drop a constraint; no ban operator, no correctness-cost warning) |
| M13 | (L) A short unrelated random fact raised judged creativity (88.1 vs 69.6) and flexibility across four open-weight models; associative prompting raised diversity in a 24-person study. Judged by a model, so weak. | A09.06-K26 | O7 | partly (O7 maps analogues; far sources lower the mean and raise spread, F05) |
| M14 | (L) Over-generation saturates on open ideas: of 4000 seeds per topic only about 200 (5%) were non-duplicates; a chain-of-thought generate-and-revise prompt only delayed exhaustion. | A09.01-K09 | G12, S3, S6 | partly (S3 "many draws, then code selects" assumes more draws help) |
| M15 | (L) On checkable tasks coverage keeps growing roughly log-linearly with samples (MATH 82.9% at 100 to 98.44% at 10,000; SWE-bench Lite 15.9% to 56% at 250) while verifier-free selection plateaus. Use marginal coverage per doubling, not duplicate rate, as the stop signal. | A09.01-K28, A09.01-K09 (update) | S3, G12 | partly (G12 search only with a foothold; no stop rule) |
| M16 | (L) LLM judges do not rank ideas better than chance or than experts (best LLM 53.3% vs expert inter-reviewer 56.1%; GPT-4o pairwise 45.0%); no LLM assessor correlated positively with experts on a Torrance-style rubric. | A09.01-K14 | G5, G8, S7 | yes (G8, G5) |
| M17 | (L) Loops that generate with a model and judge with an external executable evaluator find new results; removing a novelty filter halved distinct novel models (455 vs 220); FunSearch improved cap set bounds. The evaluator is code. | A09.01-K20 | G8, S4, S7 | partly (G8 yes; the validated-candidate archive with k=2 is not in the schema) |
| M18 | (L) Errors left in context raise later errors: odds of a mistake rose with the share of earlier wrong turns; thinking mode removed the effect; a sliding window reduced it; models relied on first attempts and wrote 20% to 300% longer answers. Scope is one-key tasks, not idea generation. | A09.06-K32 | G1, S6 | partly (S3 fresh contexts per attempt; S5 revise appends failing output, no restart rule) |
| M19 | (H and L) AI-generated examples fix people too (image generator: fixation +0.32, Bayes factor 124, N=60; an LLM partner helped on simple tasks and hurt on complex ones; assisted gains did not carry to solo work). | A09.06-K21 | none | no (belongs to the multiplayer layer, section 6) |

## 3. Contradictions between subfields

| # | Tension | Claims | Reading |
|---|---|---|---|
| C1 | Showing earlier output causes copying, yet showing earlier answers with a request for something new gave the best diversity in NoveltyBench. | A09.01-K03, A09.01-K04, A09.06-K03, A09.06-K30 vs A09.01-K15 (and contested A09.01-K30, single-source A09.06-K31) | Probably instruction wording: examples with an avoid or recombine line help (George and Wiley d=0.58), examples alone do not, visual examples hurt. Never measured in one experiment. Test M-T1. |
| C2 | Over-generation saturates (5% unique) vs coverage keeps growing (MATH 82.9% to 98.44%). | A09.01-K09 vs A09.01-K28 | Different task classes: open ideas vs checkable tasks. Not a true conflict; the stop rule must be per class. |
| C3 | Chain-of-thought generate-and-revise only delayed exhaustion vs structured title-revise-expand raised diversity. | A09.01-K09 vs A09.06-K18 | Different measures (duplicate pool size vs category slope), different models, most arms not token-matched. Unresolved. |
| C4 | Thinking mode removed error carry-over (Qwen3) vs reasoning models are not immune to Einstellung traps. | A09.06-K32 vs A09.06-K34 | Different failure types: carried-over wrong turns vs a strong prior in the first step. Both can hold. |
| C5 | A random remote fact helps vs far analogues lower the mean and raise spread. | A09.06-K26 vs SCHEMA O7 (F05) | The remote-fact result is model-judged and judges are near chance (A09.01-K14). Treat as a hint. |
| C6 | A validated-candidate archive in the prompt helps (FunSearch, k=2) vs examples in context anchor. | A09.01-K20 vs A09.01-K03, A09.06-K03 | Archive entries come from an external evaluator and may be other-problem; the anchoring studies show same-problem examples. Test M-T1 includes both. |
| C7 | A09.06-K18 says critique-and-edit gave the biggest diversity gain; single-source A09.06-K33 and SCHEMA 4b say same-model critique without a check does not help. | A09.06-K18 vs A09.06-K33, SCHEMA 4b | Diversity is not accuracy. Critique may spread the pool but not improve the pick. No source scores the best pick. |
| C8 | With other fields: A01 F10 (independent breadth beats refinement; refinement patches and plateaus after about 2 rounds) agrees with A09.06-K32, but A09.01-K18 (contested) says revise beats resample when feedback is specific. | A01.09-K18 etc. vs A09.01-K18 | Feedback quality is the likely switch. Test M-T4. |
| C9 | With SCHEMA G11 (think briefly) vs A09.06-K32 (thinking mode removes carry-over) and A09.06-K34 (extra thinking does not remove traps). | G11 vs A09.06-K32, K34 | No contradiction on accuracy; thinking is not the defixation tool. Keep G11. |

## 4. Recurring mechanisms

1. **Memory activation without intent.** Earlier text, shown examples, a usual object role and strong domain knowledge all pull output toward themselves, and neither delay nor "be different" removes the pull. Seen in people (A09.01-K04, A09.06-K01, A09.06-K08, A09.06-K30) and in models (A09.06-K32, A09.01-K03 update). The remedy that works is not to have the material in context, or to name what to avoid.
2. **Path of least resistance.** Ideas start from the most available category members and keep their standard properties (A09.06-K06). Models do the same at pool level (A09.01-K15, A09.06-K15, A09.06-K16).
3. **Code selects, model generates.** Judges are near chance (A09.01-K14); executable evaluators find new results (A09.01-K20). Same rule as G8.
4. **Diversity costs correctness.** Bans, constraints and temperature buy novelty and lose correctness or coherence (A09.01-K19, A09.01-K16, A09.06-K38). Spend them only where a check can catch the loss.
5. **Saturation depends on task class.** Open ideas run out fast; checkable tasks keep paying for more samples (A09.01-K09, A09.01-K28). Budget must be set per class (G12).
6. **Structure beats exhortation.** Procedures with steps raise diversity; generic "be creative" lines do not (A09.06-K18 vs A09.06-K19).

## 5. Merged tests

All arms at equal total tokens, setup counted (G7). Thresholds are proposals from the UNKNOWNS files. Each unknown id appears once.

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| M-T1 What earlier output may enter context | A09.01-U2, A09.06-U3, A09.06-U8, A09.01-U8 | Arms: nothing shown; shown, no instruction; shown plus avoid or recombine; fresh context plus code dedup; sliding window; function summaries instead of full text; same-problem vs other-problem archive. Metrics: feature overlap by code, distinct count, category slope, pass rate. | High |
| M-T2 Open-mode generator shootout | A09.06-U1, A09.01-U11, A09.06-U11, A09.06-U9 | Best-of-n vs k answers in one call vs title-revise-expand vs verbalized sampling vs code-assigned seeds, random facts, personas, and a code-listed invariant to break. Score the best pick by key or run, pool categories secondary. | High |
| M-T3 Ban the default | A09.01-U5, A09.06-U2, A09.06-U12 | Free "avoid" line vs code-held banned list with regeneration vs ban-after-impasse vs ban of last technique. Metrics: banned-feature rate, correctness on the stuck subset. | High |
| M-T4 Retry context and revise vs resample | A09.01-U3, A09.06-U4, A09.06-U10, A09.06-U14 | On one-key tasks: revise with located failure vs fresh resample vs bandit mix; append drafts vs task plus no-good list vs sliding window; plateau restart; restart vs continue after impasse. Metric: held-out pass rate, tokens per solve. | High |
| M-T5 Stop rule by coverage slope | A09.01-U4 | Fixed N vs stop on duplicate rate vs stop on coverage slope fitted from the first 8 to 32 samples, per puzzle class. Cheapest; uses logs we already have. | High |
| M-T6 Strong-prior trap probe | A09.06-U7, A09.01-U12 | Counterfactual pairs and red-herring items. Plain vs extended thinking vs n plus vote vs n plus code harvest plus held-out check vs mutated restatement at impasse. Doubles as the standing fixation probe. | High |
| M-T7 Form-first generation | A09.01-U1, A09.01-U14 | Random triples of code primitives with hidden checked targets; purpose-first vs form-first vs build-run-read vs plain. Report originality and practicality as two axes, 3 seeds. The only direct test of Geneplore. | High |
| M-T8 Selection by run, prior art, audit | A09.01-U7, A09.01-U6, A09.01-U13 | Model-opinion rank vs random vs run-based vs prior-art-checked pick; audit own logs for scores the checker did not produce (cheap, do with the next run). | Med (U13 cheap, do first) |
| M-T9 Parts and affordance operators | A09.06-U5, A09.06-U6, A09.01-U10 | MacGyver, tool substitution, BrainTeaser: plain vs zero-shot CoT vs parts tree with usage-free redescription vs affordance reflection vs self-check vs code execution. | Med |
| M-T10 Far analogue timing | A09.01-U9 | Far analogue always vs near only vs switch on a code-detected runnable construct. Metric: pass rate and spread across seeds. | Med |
| M-T11 Fixation-label steering | A09.06-U13 | Add 0% and 20% label error to a per-idea steering signal; check the net gain stays positive. | Low |

Order from the UNKNOWNS files: M-T5, M-T4, M-T1 then M-T7 for subfield 01; M-T2, M-T6, M-T4 then M-T3 and M-T1 for subfield 06. Combined: M-T5, M-T2, M-T6, M-T4, M-T1.

## 6. Not to add

| Idea | Why not | Claims |
|---|---|---|
| "Be creative", "think outside the box", "think like X" lines | No effect in people or models; short wild prompts did not match method prompts. | A09.06-K19, A09.01-K16, A09.01-K04 |
| Temperature sweeps as a defixation method | Weak lever, coherence falls, output garbled at 2.0. | A09.06-K38, A09.01-K16 |
| A model judge or critic as selector of ideas | Near chance, rewrites of prior work rated as novel. Already G8. | A09.01-K14 |
| Mixing vendors as a free diversity fix | Models share one semantic region. Only inside a measured test. | A09.06-K16 |
| Counting duplicate rate as the stop signal on checkable tasks | Coverage keeps growing; use marginal coverage per doubling (still to be tested, M-T5). | A09.01-K28 |
| Raw bans of the approach in every attempt | Correctness collapses (16.1% to 2.1%). Allowed only at S6 and only after M-T3. | A09.01-K19 |
| Showing the agent its own first draft as inspiration without a defixation step | AI-made examples fix the user; own failed attempts anchor the code model. | A09.06-K21, A09.01-K03 |
| Anything from the multiplayer side (AI examples fixing people, group homogenization) | Out of scope for the single agent; belongs to the planned people layer. | A09.06-K21, A09.01-K21 (single-source) |
| Personality, mood, "aha", brain-network results | About people; no transfer. | SUBFIELDS.md |

Items already in SCHEMA 4b and confirmed here: creativity training as prompts, same-model critique without a check (A09.06-K33 is single-source, so only supporting).

## 7. Gaps

- **Single-source claims carry much of the field.** 38 of 71 claims are single-source, including the generic parts technique (A09.06-K13, N=14 per arm), the break benefit (A09.06-K10), verbalized sampling (A09.06-K20), the within-run category slope (A09.06-K14), the plausible-but-wrong-part finding (A09.06-K27) and denial prompting (A09.06-K25). They are in UNKNOWNS, not in section 2.
- **Contested: examples help or hurt overall.** The Sio, Kotovsky and Cagan 2015 meta-analysis (43 studies) was never opened (A09.06-K11). It decides whether "examples cause harm" is the right frame.
- **Contested: form-first (preinventive) generation.** One human replication shows more original and less practical, no net gain (A09.01-K06). No LLM run exists (A09.01-K25).
- **Contested: refine vs resample (A09.01-K18) and the reflection result (A09.06-K23).** Depend on feedback quality and model.
- **No judge-free originality score.** Our bench has code checks only. Open-mode tests must use keyed or runnable items, or a small human-rated sample to calibrate any model rater.
- **Open-domain results may not carry to checkable tasks.** Stories, proposals and jokes dominate the LLM evidence.
- **2026 preprints are unreplicated** (Verma, Bilal, Heuresis, Grammenos and Lubart). The established updates inside A09.01-K03 and A09.01-K09 lean on single papers.
- **Original human papers unread:** Ward 1994, McKnight 2006, Jansson and Smith 1991, Chrysikou and Weisberg 2005, Agogue 2014, Ezzat 2020, Atilola 2016.
- **Unresearched subfields:** blending, conceptual combination, incubation, divergent thinking, ordinary-cognition theories (section 1). The divergent-thinking and blending work would feed operator O7 and the open-mode metrics.
- **Model scale and reasoning:** larger models gave fewer distinct answers in one family; whether more knowledgeable models fixate more is untested.
- **Judge noise differs by probe** (A09.06-K36, single-source): agreement was 0.86 for jokes, 0.87 for stories and 0.54 for poems. Diversity scores must name the probe.
