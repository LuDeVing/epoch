# Critique: A05.04 Desirable difficulties (cross-check, second pass with evidence_c)

Inputs: evidence_a (29 lines), evidence_b (30), evidence_c (27), evidence_d (17, the earlier gap search). Output: claims.jsonl (35 claims, K01-K35). Earlier claims were kept and extended; K28-K35 are new.

## Numbers re-opened and confirmed or corrected
Human numbers were re-checked in the first pass (Simon and Bjork 2001, Shea and Morgan 1979, Cepeda 2008, Rowland 2014, Sana and Yan 2022, Verkoeijen, Sigayret). This pass re-opened the machine and AI numbers that now carry the most weight.
1. c19/b22 Bastani 2025 (PMC full text, regression table): practice +0.137 (SE 0.031) and +0.361 (0.032); exam -0.054 (SE 0.022) and -0.004 (SE 0.013); control means 0.284 and 0.321; 2,848 observations; text says 48%, 127%, 17%. CONFIRMED.
2. c01/c02/d02 Atreya 2026 (arXiv full text): uniform 25.2 and 46.2, SRT 49.0 and 51.6, PPL-prioritised old 27.4 and new 38.8. CONFIRMED. The abstract adds "5 to 37 points" of old accuracy recovered, consistent with 49.0 minus 11.7.
3. c08/c09 Chen 2026 (abstract and full text): floor 0.019, freedoms 0.010-0.021, 0.0619 then +0.010 and -0.015, interleaving +0.0483, t=8.06, 6 of 6, 76% forgetting. CONFIRMED. New detail: order is "a transient whose sign crosses zero three times inside a single run", and the scorecard grades 18 of 26 pre-registered claims supported, 5 failed.
4. d08 SkillsBench: self-generated -8.1, -11.3, -11.5; curated +18.2 to +24.8 on three harnesses. CONFIRMED in full text. CORRECTION: the current abstract reports +16.6 pp over 18 configurations (33.9 to 50.5), so +18 to +25 is not the global average. The authors say the self-generated deficit mixes quality with creator-solver interference.
5. d09 More Memory, Worse Agents: anti-persistence 59.9, trajectory 53.5, abstraction 49.0, joint 49.3. CONFIRMED. CORRECTION: the text says anti-persistence won 7 of 9 settings and beat trajectory and abstraction memory in all 9. The line "abstraction lost to trajectory in 7 of 9 settings" in d09 was not found; do not use it.
6. c21 Fan 2024: abstract confirms the pattern (essay score up; knowledge gain and transfer not different; metacognitive laziness). F-values not re-read. Abstract-level.
7. c24 Huff and Ulakci: abstract confirms humans predicted memory and three GPT models did not. B values not re-read. Abstract-level.
8. c13 Muennighoff 2023: 4 epochs negligible change confirmed in the abstract. CORRECTION: R_D* is a learned decay constant (value of repeated tokens saturates as 1 minus e^(-R/R*)), not a literal half-life. Wording fixed in K18.
9. c22 Eleftheriou 2026: abstract confirms baseline had highest perceived and lowest objective learning, guided hints largest gain. d=1.14 not re-read. Abstract-level.
10. a14 Donenfeld 2026 (first pass): the source prints swapped means; use t and dz only.

## Other corrections to the record
- a27, a28, a29, b10, b12, b17, b19 are duplicates or have wrong urls; do not count them as evidence.
- a24, b20, b21, c06, c07 and d06 are all the Russin, Pavlick and Frank work (and its CCN version): ONE source.
- c01, c02, c03, d02, a25 are all Atreya 2026: ONE source. a26 (Prakriya) is data selection, a different construct.
- c19, c20, b22, b23 are all Bastani 2025.
- b07 Hattie (interleaving d = 0.21, 12 studies) is older and smaller than Brunmair (g = 0.42, 59 studies); use Brunmair.
- The arXiv ids 2604-2610 are 2026 preprints; none seen peer reviewed.

## Contradictions between sources
- Interleaving in LLM fine-tuning: Chen finds order effects inside noise in one domain, yet +0.0483 when scored on both skills. The difference is the scoring rule, not the effect.
- Atreya: perplexity-prioritised replay gives best new knowledge (38.8) but poor old (27.4); SRT gives the reverse (49.0 old, about 20 new). No method wins on both.
- Curricula: Zhang finds up to 3.5% sustained gain, Mordig finds no robust gain. Metric choice and model family differ; unresolved.
- Bastani finds harm from unrestricted help, Fan finds a null on knowledge and transfer, Kestin finds a large gain with no delayed test. Different outcomes, not necessarily a conflict.
- Human spacing size: d 1.1 (Cepeda), 0.46 (Donovan), 0.60 (Hattie); depends on task and lag.
- Generation effect fails in 0 of 7 recall experiments while testing and spacing hold: "difficulty" is not one thing.

## Weak spots
- No LLM or agent study tests the real design (harder practice, delayed held-out test). K34 states this. All machine evidence is by analogy.
- Most 2026 LLM results are single preprints from one lab (Atreya, Chen, Eleftheriou, Kang, SkillsBench).
- Human evidence is mostly college students on verbal or simple motor tasks.
- Circularity: "desirable" is defined by later benefit.
- The agent-relevant human result (Bastani) has humans using the LLM, not the LLM learning.
- c18 MemoryBank (Ebbinghaus forgetting rule) has no ablation, so it supports nothing about forgetting schedules.
- c25 (Cao 2026) and c27 (talk page) were not used: unclear scope.

## Only seen in snippets or abstracts
a27-a29, b10-b21 (except as noted), b26-b30, c26, c27, c04 and c05 (qualitative figures only), c21, c22, c24 (numbers beyond the abstract not re-read), d15, d17.

## GAPS (most decision-relevant first)
1. Does any study give an LLM harder, interleaved or attempt-first lessons and score a delayed, held-out test (after N unrelated tasks) against easy or blocked, with ground truth rather than perplexity? K34 says none found.
2. Does the immediate pass rate of a stored lesson predict its delayed benefit for an agent? Need a per-lesson correlation (immediate vs held-out gain); none found.
3. Is attempt-before-lesson better than lesson-first for an LLM at equal tokens (pretesting and unsuccessful retrieval, K08 and K24)? Only human evidence exists.
4. What revisit gap (in tasks or tokens) is best for re-surfacing a stored lesson, and does an SM-2-like schedule (K28) beat most-failed-first and uniform retrieval for in-context lesson memory, not weight replay?
5. How large is the run-to-run floor for our own agent at equal tokens, and how many reruns are needed to tell two schemas apart (K29, K35)?
6. Which Brunmair moderators (similar categories, varied exemplars) predict where interleaved lesson order helps on ARC-like versus brainteaser-like items (K27)? A prediction exists; no LLM measurement.
7. Does an LLM's judgment of which schema or lesson will do better later show the same bias toward the easy condition as human learners (K02, K25)? Only indirect evidence (Huff, Moran).
8. Does desirable difficulty reverse for weaker models or complex tasks (expertise reversal, link to A08.04), and can S0 pick the class from baseline pass rate (K20)?
9. Do conflicting conventions across stored lessons make order matter (K30), and does tagging lesson conditions remove the effect in an agent memory?
10. Are there large preregistered multi-site replications of the interleaving and testing effects after 2020 beyond Higham, Zhao, Rogers, Donenfeld and Sigayret?

## Gap search results (pass 2, evidence_d d18-d34)

Note on ids: evidence_d.jsonl was rewritten in this step. The earlier lines d01-d17 are kept as reconstructed index lines (source, url and claim text; the original numbers were lost on overwrite, so re-open before reuse) because claims.jsonl and DEEP.md cite them. The new evidence is d18-d34. Search tools: 8 WebSearch calls or fewer; the arXiv, Semantic Scholar and OpenAlex APIs all returned HTTP 429, so most reading was by direct page fetches (several are abstract pages only, noted in the lines).

1. Harder lessons for an LLM, delayed held-out test: STAYS OPEN. Nearest are TraceRetain (d18), faulty-memory (d19, d20) and IBM tips (d21); all score held-out tasks, none varies difficulty or order. K34 kept as single-source.
2. Immediate pass rate vs delayed gain per lesson: PARTLY ADDRESSED, still open. Aggregate only: seen-task gain 12.3 vs held-out 3.6 pp (d21, K36). SeqMem-Eval (d23) and Hu et al. (d24) could not be read; they are the next sources.
3. Attempt-first vs lesson-first for an LLM: STAYS OPEN. Only human studies (d29, d13): d = 1.54 in the favourable task, no difference between pretest formats.
4. Revisit gap, SM-2 vs most-failed-first vs uniform for in-context lessons: STAYS OPEN. TraceRetain (d18) cannot separate policies at 50 tasks; faulty-memory (d19) shows the consolidation schedule matters, not revisit timing. New K37, K38.
5. Run-to-run floor: CLOSED as to general magnitude, open for our own agent. SD above 1.5 pp at temperature 0, 2.2 to 6.0 pp spread, 77% head-to-head win rate (d25, d26, K39). Our own floor must be measured.
6. Brunmair moderators on ARC vs brainteaser order: STAYS OPEN. No LLM measurement found.
7. LLM forecast bias toward the easy condition: PARTLY ADDRESSED. Verbalised confidence is overoptimistic (d32); prompt-quality predictors do not transfer (d33, snippet level). No pairwise-schema test.
8. Reversal for weaker models, S0 gating: PARTLY ADDRESSED. Reflection helps most at low initial correctness (d30); CoT can hurt (d31); Nigeria RCT gains only in low achievers (d28). The baseline-pass-rate gate stays a hypothesis; K20 stays contested.
9. Conflicting conventions, tagging lessons: PARTLY ADDRESSED. Faulty-memory (d19, d20) names stripped applicability conditions as the mechanism and shows about 5x over-generalised entries; tagging was not tested directly. K30 and K37.
10. Large preregistered multi-site replications after 2020: STAYS OPEN. Only a year-long field RCT was added (d28, K40); no Many-Labs-style replication of interleaving or testing found.

Net: 1 closed (gap 5, general magnitude), 3 partly addressed (2, 7, 8) plus gap 9, so 4 partly addressed in all, 5 open (1, 3, 4, 6, 10). New claims K36-K41; K20, K22, K24, K25, K30, K34, K35 extended. Single seed and single lab dominate the new 2026 agent-memory sources (d18, d19, d21).
