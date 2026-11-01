# Critique, B04.10 Replay and wake-sleep learning in AI

## Re-checked numbers (sources re-opened this session as full arXiv text)
Confirmed: DreamCoder 3.7% to 79.6%, 235 s to 40 s, CVC4 82.4%, 84.3%, 93% of laws after 8 cycles, r = 0.79, 54.1 s mean / 15.0 s median, "no alternative above 60%" (2006.08381). LILO table values 43.93 / 77.07 / 48.95, max 93.20 and 73.87, -30.60, +9.73, 998/5250 = 19.01%, 48 CPU-hours (2310.19791). Library-learning-doesn't: 20,000 lemmas, 1,233 (6%), one lemma reused once, 15 TroVE functions, 3 reuses in 3,201 (2410.20274). SOAR 14.25 to 36.25, 25.62 to 44.87, 52.00 majority vote, 57.25 oracle, plateau about 5.2k attempts (2507.14172). van de Ven Class-IL 19.90 / 20.01 / 90.79, Domain-IL 59.21 / 63.95 / 95.72 (1904.07734). Sleep-time compute: up to 13% and 18%, 2.5x per query, 60 AIME questions (2504.13171). The "about 5x" figure was not found by text search; treat it as abstract-level.

## Corrections
1. c10 says "Date: 45.6 primitive vs 57.1 ReGAL (13B)". Wrong label. The ReGAL table row is LOGO 45.6 to 57.1 and Date 42.8 to 68.9 (b08 is correct). Use b08.
2. a15/c10 mix test numbers (45.6 to 57.1) with dev numbers (a16/c11: 55.0, 77.0, 34.12). Do not compare across them.
3. a19 row order is ambiguous. From the paper, reproduced TroVE vs no-reuse ablation: counting 0.236 vs 0.250, geometry 0.058 vs 0.050, intermediate algebra 0.120 vs 0.134, number 0.258 vs 0.290. The ablation wins 3 of 4 and loses on geometry. c13 is correct.
4. LAPS is dated 2021 in the id and 2022 in the source string (preprint 2021, ICML 2022).
5. a08 table text was garbled; the sleep-only vs wake-only nats are not safe to quote.
6. "One LLM round equals 48 CPU-hours" (a12) is the LILO authors' own estimate (96 CPUs, about 48 CPU-hours).

## Contradictions and weak spots
- Library helps (LILO, ReGAL, Voyager, DreamCoder) vs library not reused (TroVE, LEGO-Prover). Domain structure is the likely resolver, but no paper tests it directly. K22 is marked contested.
- ReGAL gains shrink for stronger models (GPT-3.5 Date 88.9 to 90.2) and under shift (+3.6%). LILO's REGEX gain over the plain LLM is small (+0.94) and CLEVR modest (+8.1). LILO LOGO std is 9.46 and its max (73.87) is far above its mean (48.95); LAPS best 92.79 beats LILO best 73.87, so LILO does not beat LAPS on LOGO.
- Independent sources are mostly 1. The three evidence files repeat DreamCoder numbers from one paper. LAPS, LILO and Stitch share authors and code with DreamCoder, so they are not independent replications. No outside replication or failed replication of DreamCoder was found.
- AWM, ReasoningBank, Dynamic Cheatsheet, ExpeL are author-reported on different benchmarks and models; no common comparison.
- Dynamic Cheatsheet gains concentrate where the model reuses code (Game of 24); on Claude Game of 24 the gain is 12% to 14%. This looks like a single-trick effect.
- Almost no study uses equal-token accounting between the sleep phase and a longer-thinking arm; sleep-time compute (vs pass@k) is the exception.

## Only seen in snippets or not opened
a07, a09, a23, a24, a25 (Hinton 1995, Dayan 1995, EWC, CLS, Ellis 2018), c25, c26, c27, b27 (CRAFT abstract only). No numeric claim relies on them.

## GAPS
1. Does a no-library arm with equal tokens match library loops for a frontier LLM (the TroVE/LEGO-Prover audit applied to LILO, ReGAL, AWM, Dynamic Cheatsheet)? Nobody ran this audit on them.
2. What per-task reuse rate makes a subgoal library pay for its wake and sleep tokens (break-even)?
3. Which library-entry format works best for an LLM at read time: name plus docstring, worked example, or code only? No direct comparison exists.
4. Has any unrelated lab replicated, or failed to replicate, DreamCoder-style gains on non-DSL, open-ended reasoning tasks?
5. Can verify-before-keeping fix the 19% valid-abstraction rate, and what verifier exists for non-code reasoning steps?
6. Is there a no-weights analogue of "dreaming" (generate practice problems from the library, solve them, keep what verifies) that helps a scaffold? Check 2025-2026 follow-ups to sleep-time compute and self-instruct style work.
7. How should failed attempts be stored (SOAR hindsight relabelling, ReasoningBank failures), and which gives more gain per stored item?
8. How does library size interact with retrieval quality (TroVE 79-98% smaller; CRAFT hundreds of tools)? Where does retrieval noise start to cost accuracy?
9. Does short-to-long curriculum order (ReGAL: -18.7 on LOGO without it) hold for LLM library building outside LOGO?
10. Does sleep-time compute still help when queries are unpredictable from the context, and can the agent tell beforehand?

## Gap search results

Evidence in `evidence_d.jsonl` (d01 to d20, all opened this session). Claims K23 to K30 added; K09, K11, K13, K15, K16 updated. Web search quota ran out partway, and arXiv and OpenAlex APIs were rate limited, so sources were chosen from known papers, not from a fresh sweep.

1. No-library arm (partly closed). Dynamic Cheatsheet's empty-memory arm (same instructions) gets about half of Claude's AIME 2024 gain (23.3 to 36.7 of 50.0) but not GPT-4o's Game of 24 (19 vs 99) (d05). LILO's matched no-library solver with search is within 0.5 points on REGEX and CLEVR; only LOGO shows +11.1 (d19). SkillsBench: one-shot self-written skills are 8 to 11.5 points below no skills (d09). Still not run for ReGAL, AWM or any frontier-model LILO.
2. Break-even (open). Build cost known (about 1M tokens per LILO iteration, d20; sleep-time 2.5x cost saving at 10 queries with a 10x price ratio, d08). No paper reports tokens saved per reuse.
3. Entry format (partly closed). ASI: verified text beat verified program when placed in memory (39.0 vs 36.4); program wins as callable action (d01). ExpeL: insights vs retrieved trajectories split by task (d17). SkillsBench: compact beats comprehensive (d10). No test of name-plus-docstring vs worked example vs code.
4. Outside replication (open). Nothing found from an unrelated lab on open-ended reasoning. Closest are code and web tasks from the CMU group (ASI, SkillWeaver) and the Toronto audit.
5. Verify-before-keeping (partly closed for code). ASI: 15.6% of turns pass verification and verification adds 4.2 points (d01, d02). ReasoningBank: even a random-guess judge kept most gain (d04), so the lesson-writing step may matter more than the check. No verifier for non-code reasoning steps found.
6. No-weights dreaming (partly closed). SkillWeaver gives +31.8% (WebArena) and +39.8% (live) relative (d11), but no equal-token control, and the verifier is an LLM judge plus unit tests.
7. Failure storage (partly closed). Lessons from failures help (ReasoningBank 46.5 to 49.7); raw routines do not (AWM 44.4 to 42.2) (d03). No comparison with SOAR hindsight relabelling.
8. Library size and retrieval (mostly closed in direction). Flat in-prompt lists fall off past about 20 to 30 skills (d14, d15); similarity retrieval plateaus rather than collapses (Memento K=4 best, K=32 only 0.6 F1 lower, d16); ReasoningBank best at the smallest count (d04). Threshold for a reasoning scaffold untested.
9. Curriculum order (partly closed). ReGAL ablation holds in 3 domains: LOGO -18.7, Date -20.4, TextCraft -5.3 (d18). All are code domains from one lab.
10. Unpredictable queries (partly closed). Gain grows with predictability; sleep-time loses to plain test-time scaling at high budgets in SWE-Features (d07). The paper offers no pre-check; a log-prob scorer is the only measured predictor.

Caveats: SkillsBench self-generated delta changed from about -1.3 (early version) to -8.1 to -11.5 (v4), so quote the version. ReasoningBank retrieval-count and SkillWeaver table text were garbled in the PDF; only readable values were used. Several new sources are preprints from the authors of the methods they test.
