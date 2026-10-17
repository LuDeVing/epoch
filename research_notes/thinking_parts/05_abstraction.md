# 05. Abstraction: moving between levels ("what is this an instance of")

*Prepared 2026-10-13 for part 5 of the thinking decomposition. Analogy as an idea source is covered in `idea_generation/02_analogy.md` (structure mapping, distance bands, typed mapping) and is not repeated. This brief covers abstraction as a faculty: restating a problem one level up, keeping abstractions across problems, retrieving by structure, and choosing the level. Grades follow 02: **H** meta-analysis, large preregistered or independently replicated; **M** peer-reviewed or documented, single study; **L** preprint-only, abstract-only, author-asserted or anecdotal. "(inference)" marks my reasoning. The shared search quota ran out mid-task, so some items were read only as abstracts or search summaries (flagged), and Gowers, Tao and Feynman could not be opened. Bracketed numbers are Sources.*

## Bottom line

1. **Abstracting is cheap; what follows it is the bottleneck.** Step-Back fixed 20.5% of baseline errors on MMLU-Physics and created 11.9% new ones; over 90% of remaining errors sat in the reasoning step [1] (M). An abstraction needs a check on the way back down.
2. **Abstractions pay when verified, typed, short and selected by structure.** Typed concept memory lifted o4-mini on 100 ARC puzzles from 55.2 to 59.3 [16] (L); distilled strategy memory gave +4.6 to +8.3 points on WebArena [18] (L). Prompting alone is unreliable: most RLAD prompt configurations showed no gain, and abstractions cut a base model's AMC score from 86.4 to 78.0 [6] (M).
3. **Self-written libraries are mostly not reused.** LEGO-Prover reused one lemma verbatim; TroVE had 3 successful reuses in 3,201 questions and, at matched compute, an edge of about 1% on MATH [13][14][15] (L). Agent skills written by the model changed pass rate by -1.3 points; curated ones by +16.6 [20] (L). Positive library results are on closed synthetic domains [11][12] (M).
4. **Retrieval by wording fails where abstraction is needed.** The top MTEB retriever scored 59.0 nDCG@10 on its home benchmark and 18.0 on BRIGHT's reasoning-intensive queries [22] (M); embedding retrieval of concepts hurt ArcMemo [16]; LILO's similarity-based example choice gave no significant gain over random [11]. Experts sort problems by principle, novices by surface [25][26] (M).
5. **The level is a choice with costs.** Abstract construal drops features "deemed incidental" and, in construal-level theory, moves weight from feasibility (means) to desirability (end states) [31] (M, theory); the best-known "abstract beats concrete" result vanished once the concrete examples were improved [29] (M).
6. **For the loop** (Section 3): a signature step by the strongest model, a typed "move" on every sketch and ledger row, retrieval by signature against a random control, library entries admitted only with two instantiations and logged for reuse. No trained abstraction generator; no large library.

## 1. What the evidence says

**Abstraction inside reasoning**
- Step-Back (one exemplar, PaLM-2L): MMLU Physics +7, Chemistry +11, TimeQA +27, MuSiQue +7; with retrieval it fixed 39.9% of TimeQA baseline errors and caused 5.6%; the authors call abstraction "an easy skill" and reasoning the bottleneck [1] (M).
- Stored high-level templates: Self-Discover (up to +32% over chain of thought, 10-40x less compute than self-consistency) [3], Buffer of Thoughts (+11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One, about 12% of multi-query cost) [4], ReasonFlux (about 500 templates, hierarchical RL, MATH 91.2%) [5], Abstraction-of-Thought (abstract-then-concrete finetuning on 348k samples beats CoT-aligned models on many of 23 BBH tasks) [2]. All author-run; no replication found (L, abstracts).
- RLAD trains a proposer of abstractions and a solver [6] (M). Qwen3-1.7B, AIME 2025: 33.8 base, 42.5 RLAD with abstractions; at equal compute n abstractions x n solutions beat n^2 solutions (0.71 vs 0.65 at n=16). Gains needed long abstractions from a strong generator (o4-mini) and a capable solver. AbstRaL's symbolic abstraction cut a 0.5B model's GSM-Symbolic drop from 10.6% to -1.3% [7] (M).
- Large Concept Models predict the next sentence embedding, a "concept" being a sentence; a 1.6B-7B feasibility study [8] (L, abstract). Accuracy can mislead: on ConceptARC o3 was right with the intended rule on 55.0% of tasks (humans 53.7%) and right through unintended shortcuts on 15.8% (humans 2.7%) [9] (L).

**Library learning and concept memory**
- Stitch compresses 3-4 orders of magnitude faster than DreamCoder with 2 orders less memory [10] (M, abstract). LILO online solve rates (REGEX, CLEVR, LOGO): 77.1, 96.8, 49.0 vs DreamCoder 43.9, 94.5, 28.5 and an LLM solver 76.1, 88.7, 32.1; against the solver with search the gap is within one SD on two domains; auto-documentation added 9.7, 2.3 and 0.0 points [11] (M). ReGAL: CodeLlama-13B +11.5 (LOGO), +26.1 (dates), +8.1 (TextCraft) [12] (M, abstract).
- Agent concept memory: ArcMemo's typed, parameterised concepts 59.3 vs 55.2 with no memory, open-ended notes 56.7, a cheatsheet 57.7; the edge is largest at low compute and gone at two retries (71.3 cheatsheet vs 70.8) [16] (L). Workflow induction: +24.6% (Mind2Web) and +51.1% (WebArena) relative, the edge growing from 8.9 to 14.0 points as train-test distance widens [17] (L, abstract). ReasoningBank on WebArena: 40.5 to 48.8, 46.7 to 53.9, 41.7 to 46.3 over three backbones; on the Shopping subset failure traces helped it (46.5 to 49.7) and hurt workflow memory (44.4 to 42.2) [18] (L).
- SkillsBench: curated skills 33.9 to 50.5 (+16.6 points, 18 configurations); self-generated -1.3 on five; 2-3 skills +18.6, four or more +5.9, comprehensive documents -2.9 [20] (L).

**Retrieval by structure**
- BRIGHT: reasoning-written queries gave up to +12.2 nDCG@10 [22] (M, abstract); ReasonIR, trained on synthetic reasoning queries with hard negatives, reaches 29.9 (36.9 reranked) [23] (L, abstract). AnaloBench: the human-GPT-4 gap in picking the analogous story grows from 6.9% (1 sentence) to 28.8% (30 sentences); scale does not fix retrieval from a large bank [24] (M, summary).
- People: physics PhD students sorted 24 problems by governing principle, undergraduates by objects and configuration [25]; novices' mathematics sorting turned method-based after a month-long course [26] (M, both read as summaries).

**How mathematicians and physicists move levels**
- Pólya: generalise, specialise, analogise; "the more ambitious plan may have more chances of success", because narrowing a problem often leaves awkward parameters [27] (L, secondary summary; 06_mathematics.md notes AlphaProof's variant generator emulates these moves). Nothing beyond Pólya is claimed.
- Abstract versus concrete: abstract symbols gave better transfer than concrete examples in Science [28], but improved concrete examples matched or beat them in a critical replication [29]; concreteness fading (start concrete, fade to abstract) is the compromise a systematic review proposes [30] (M, abstract only; effect sizes not read).

## 2. What did NOT work, or misled

- Step-Back's 11.9% new errors [1]; abstractions that lowered a base model's AMC score and that on-policy RL can teach the solver to ignore; one model trained as both proposer and solver lost the ability to propose [6].
- Library reuse near zero, gains explained by self-correction and self-consistency [13][14][15]; self-written skills no better than none; comprehensive bundles worse than none (-2.9) [20].
- Retrieval by wording or embedding: ArcMemo 0.26 to 0.22 [16]; LILO similarity selection no significant gain over random [11]; BRIGHT [22].
- Compression that discards detail: brevity bias and context collapse [19]; ArcMemo's detailed concepts solved more puzzles but retrieved worse (n=10) [16]; AbstRaL without intermediate context fell from 44.6 to 23.1 [7].
- Reused experience can mislead: error propagation and misaligned replay [21] (L, abstract).
- Accuracy is not abstraction [9]; LILO's edge over a search-augmented LLM is within noise on two of three domains [11].

## 3. Improvement ideas for this part

**Have, keep:** per-part frame and assumptions as the abstract level (`tree.py`); typed MAPPING lint (`ideate.mapping_ok`); blind clustering with names and cross-part merge (`loop.cluster_sketches`); TF-IDF novelty gate with audit (`novelty.gate`); ladder rungs 0-2 (`check.py`) and the fidelity probe as concretisation checks. **Gaps in code:** the "same structure" step happens implicitly inside `research.analogy_prompt`; `parse_sketches` keeps TARGET and MAPPING but no move type or level; `research.ledger_entries` keeps hypothesis text and pastes every row into every part because part ids change between runs.

A *move* below is a typed record: operator, object role, precondition, target cell, direction, level (purpose, mechanism or parameter). Example: start-as-identity / new residual path / trained from scratch / residual RMS growth / inward / mechanism.

1. **Problem signature before search (new).** *Mechanism:* one call per part to the strongest model writes a content-free signature: the part's purpose in the whole, 3-6 typed relations, invariants from the seven rules of the problem file, and 2-3 generic problem classes it is an instance of; a script validates the JSON. It replaces the frame as the query to `analogy_prompt` and to idea 4, and heads each sketch context. *Effect:* better retrieval (reasoning-written queries up to +12.2 [22]); framing gain unknown, since Step-Back's gains came with 11.9% new errors [1]. *Cost:* about 1k tokens x 8 parts per run. *Measure:* with vs without; precision of retrieved analogues by rename audit (02-M5); share of sketches citing a signature relation (ignored-abstraction rate [6]).
2. **Move line on every sketch and ledger row (new).** *Mechanism:* add MOVE to `SKETCH_FORMAT`; the clustering judge back-fills old ledger rows in one batched call; `calibrate.py` gets level as a feature bucket, so slots follow measured yield per level (inference from synthesis C5: ports dominate real gains). *Effect:* enabling; makes "what worked where" queryable. *Cost:* about 60 tokens per sketch plus one batch. *Measure:* agreement of two judge passes on move equality (kappa 0.7, my threshold); coverage of old rows.
3. **Schema library with an admission test (new).** *Mechanism:* aggregate moves into entries with n built, n verified, mean delta and seeds, failure preconditions, a name, a docstring and one example (documentation helped REGEX +9.7, LOGO 0.0 [11]). Admit only moves instantiated by two or more rows from different parts or runs (compression, the criterion that best matched human preference for refactorings [33], L); update by append and merge, never rewrite [19]; at most 3 entries per context [20]. *Effect:* floor about zero if entries go unreused [13][14]; ceiling ArcMemo-like (+4 points, L). *Cost:* a JSONL plus one admission call per run. *Measure:* reuse rate (idea 8); verified per build for entry-citing vs other sketches.
4. **Structural retrieval instead of "paste every row" (partial).** *Mechanism:* stage one filters on signature relations, target cell and direction (typed match, not wording); stage two has a judge read the top 15 and check preconditions (ArcMemo without selection 55.2 vs 59.3; embeddings alone hurt [16]); return at most 3 successes and 3 failures with preconditions. A third of contexts get random rows, a third none, because retrieved experience is copied [21]. *Effect:* bounded prompt growth, ports surface across parts; risk is anchoring. *Cost:* one judge call per part. *Measure:* leave-one-out recall on documented speedrun ports (pose the later technique's problem; is the earlier one retrieved?), which needs no GPU; then hit rate per arm.
5. **Lift and specialise after a win (new; synthesis item 21 is the weak precursor).** *Mechanism:* for each verified or stackable candidate, one call states why it helped at schema level, lists sibling parts where the precondition holds (from signatures) and writes 2-3 specialisations as ordinary sketches in a "lift" lane [27][17]. *Effect:* more ports of own wins. *Cost:* one call per win plus builds. *Measure:* wins per build in the lift lane vs matched slots.
6. **Go up a level on repeated failure (new).** *Mechanism:* when 3 or more sketches of a cluster fail, one call anti-unifies them (what the failed moves share; which assumption would have to hold) and writes a failure schema with its precondition into the library; "tried before" shows the schema, not names. *Effect:* fewer repeats in new words. *Cost:* small. *Measure:* repeat-failure rate (new builds matching a failure schema without meeting its precondition).
7. **Schema-level duplicates and exclusion (partial).** *Mechanism:* sketches with the same operator, role and direction form one family however worded; the exclusion list and discovery curve count families, not cluster names; keep the 10% audit. *Effect:* catches disguised duplicates that TF-IDF misses (MEM-15: wording-level matching misses shared structure). *Cost:* small. *Measure:* families per 10 contexts; duplicate-build rate; audited false-reject rate.
8. **Reuse log, retirement and anti-fixation share (partial; cards and exclusion arms exist, no reuse log).** *Mechanism:* per entry log shown, cited, built, verified; retire entries shown 10 times and never cited; keep at least 25% of contexts schema-free, give different contexts different entries (disjoint inputs), add an outward card that must violate a named schema. *Effect:* reuse is what failed in [13][14]; this makes it visible. *Cost:* small. *Measure:* reuse rate; clusters per context, schema vs schema-free.

**Order and design (inference).** Logging first (2, 8; no behaviour change), then 1, 4, 3; ideas 5-7 after about 50 ledger rows. Arms at matched tokens: current loop; +signature; +signature+library; random-row control; schema-free. Outcomes are executed only: hit rate per build, distinct families, repeat-failure rate, reuse rate, tokens per verified idea. n=30 could not separate conditions in the analogy literature (02), so plan 100 or more builds per arm or lean on the leave-one-out recall proxy.

## 4. Gaps

No test of abstraction libraries on ML-recipe search; RLAD, AbstRaL and Step-Back are QA or maths, ArcMemo is 100 puzzles with SDs of 1.5-3 points. No controlled study shows a multi-level problem representation beats a flat one for idea generation. I could not search for LLM fixation on retrieved schemas (Einstellung) once the quota ran out; [21] is the nearest evidence. Chi and Schoenfeld were read as summaries.

## Sources

1. Step-Back Prompting (ICLR 2024): https://arxiv.org/abs/2310.06117 ; error analysis: https://ar5iv.labs.arxiv.org/html/2310.06117
2. Abstraction-of-Thought: https://arxiv.org/abs/2406.12442
3. Self-Discover: https://arxiv.org/abs/2402.03620
4. Buffer of Thoughts: https://arxiv.org/abs/2406.04271
5. ReasonFlux: https://arxiv.org/abs/2502.06772
6. RLAD (ICLR 2026): https://arxiv.org/abs/2510.02263 ; full text: https://arxiv.org/html/2510.02263
7. AbstRaL (ICLR 2026): https://arxiv.org/abs/2506.07751
8. Large Concept Models: https://arxiv.org/abs/2412.08821
9. Beger et al. 2025, ConceptARC across modalities: https://arxiv.org/abs/2510.02125
10. Stitch (POPL 2023): https://arxiv.org/abs/2211.16605
11. LILO (ICLR 2024): https://arxiv.org/abs/2310.19791
12. ReGAL (ICML 2024): https://arxiv.org/abs/2401.16467
13. Library Learning Doesn't: https://arxiv.org/abs/2410.20274
14. LLM Library Learning Fails (LEGO-Prover): https://arxiv.org/abs/2504.03048
15. Compute-matched TroVE: https://arxiv.org/abs/2507.22069
16. ArcMemo: https://arxiv.org/abs/2509.04439 ; full text: https://arxiv.org/html/2509.04439v3
17. Agent Workflow Memory: https://arxiv.org/abs/2409.07429
18. ReasoningBank: https://arxiv.org/abs/2509.25140
19. ACE, Agentic Context Engineering: https://arxiv.org/abs/2510.04618
20. SkillsBench: https://arxiv.org/abs/2602.12670
21. Experience-following in agent memory: https://arxiv.org/abs/2505.16067
22. BRIGHT (ICLR 2025): https://arxiv.org/abs/2407.12883
23. ReasonIR: https://arxiv.org/abs/2504.20595
24. AnaloBench (EMNLP 2024): https://arxiv.org/abs/2402.12370
25. Chi, Feltovich, Glaser 1981: https://doi.org/10.1207/s15516709cog0502_2
26. Schoenfeld, Herrmann 1982: https://doi.org/10.1037/0278-7393.8.5.484
27. Pólya's inventor's paradox: https://en.wikipedia.org/wiki/Inventor%27s_paradox
28. Kaminski, Sloutsky, Heckler 2008: https://news.osu.edu/concrete-examples-dont-help-students-learn-math-study-finds/
29. Trninic, Kapur, Sinha 2020: https://edrl.berkeley.edu/publications/trninic-d-kapur-m-sinha-t-2020-the-disappearing-advantage-of-abstract-examples-in-learning-math/
30. Fyfe et al. 2014, concreteness fading: https://www.doi.org/10.1007/S10648-014-9249-3
31. Trope, Liberman 2010, construal level: https://pmc.ncbi.nlm.nih.gov/articles/PMC3152826/
32. Repo notes: `research_notes/idea_generation/02_analogy.md`, `06_mathematics.md`, `00_SYNTHESIS.md`; `research_notes/catalog_parts/05_memory.md` (MEM-15)
33. Refactoring Codebases through Library Design (Librarian): https://arxiv.org/abs/2506.11058
