# Critique: Soar chunking and learning from impasses (cross-check)

Cross-checker pass over evidence_a, evidence_b, evidence_c (93 lines). Claims are in claims.jsonl (K01 to K21).

## Sources re-opened this pass (text read)

Laird 1984 (AAAI), Doorenbos 1992, Kim and Rosenbloom 1996, AWM (arXiv 2409.07429, PDF text), ASI (arXiv 2504.06821, HTML), SkillWeaver (2504.07079, HTML), SkillsBench (2602.12670, HTML), Xiong memory management (2505.16067, HTML), Break It Down (2608.20274, PDF), Voyager (2305.16291v2, HTML).

## Numbers confirmed

- Laird 1984: 232 rules, 1731 decisions; 485 decisions and 59 chunks with learning; 7 on rerun. With 10 added control rules: 150, 90, 7. Correct.
- Doorenbos 1992: 10,112 chunks, 6.3 decision cycles per chunk, 20.5 firings per cycle (130 per chunk), 3,143 cycles and 556 chunks on problem 1, factor 7 speed-up, 10.3% transfer, 42 of 200, 55 chunks never transferring, 1.28 s plus 0.47 s per 10,000 chunks. All correct.
- Kim and Rosenbloom 1996: 0.46 / 1.42 / 0.34 s; over eight million tokens; factor nine. Correct.
- AWM: 35.5 vs 23.5, +12.0, +51.1%; Mind2Web table (36.2, 45.1, 43.6; 2.0, 4.8, 4.0; cross-domain 18.6, 32.6, 35.5); rule 35.6 / 6.3 vs LM 35.5 / 5.9; utility 0.94 and 0.91. Correct.
- ASI: Claude 32.7 / 36.3 / 40.4; steps 5.6 / 5.9 / 5.0; GPT-4 vanilla 12.3. Correct.
- Xiong: all four add-all / fixed / strict rows correct.
- Voyager: -93% (random curriculum), -73% (no self-verification), 5.7x (GPT-4 vs GPT-3.5), 3.3x, 2.3x, 15.3x. Correct.
- Break It Down: 11-model averages 22.1 / 20.9 / 18.0 and 24.8 / 26.7 / 25.3; GPT-OSS 27.3 to 1.0. Correct.
- SkillsBench: 24.3, 40.6, +16.2, 7,308 trajectories, 16 of 84 negative, Haiku 4.5 27.7 vs Opus 4.5 22.0, +4.5 to +51.9 by domain. Correct.

## Corrections made

1. c04 (AWM): the human-workflow baseline SteP is 33.0 total, not 32.0. The 7.6% relative gain only works against 33.0 (35.5/33.0 = 1.076; 35.5/32.0 would be +10.9%). SkillWeaver's table also lists SteP 33.0 overall. The 32.0 in the AWM table is a per-site column. Claim K08 uses no SteP figure; do not cite 32.0.
2. c08 (ASI): "main table gives 40.4" is wrong as a comparison. 40.1 is the Shopping success in Table 1 and equals the "verified program as action" ablation row (40.1). 40.4 is the all-WebArena total. The ablation is Shopping-only.
3. c08 (ASI): the paper's text says verification raised success by 4.2 points; its own table gives 36.4 - 32.6 = 3.8. The paper is internally inconsistent. Also, the "unverified, text" row (32.6) equals Claude vanilla on Shopping (32.6) and is below AWM on Shopping (34.8), so that row may not be an AWM-equivalent arm. Treat the ablation as one site, one run.
4. b30 (SkillsBench): the self-generated delta is -1.3 in one table and -1.8 in another; the self-generated column has 5 configs, not 7 (two Gemini configs were not run). The self-generated mean 21.0 vs 24.3 is a raw gap of 3.3, so the delta is probably computed on matched configs. Use "about -1 to -2 points, no benefit".
5. b25 / c10 (SkillWeaver): 31.8% (WebArena) and 39.8% (live sites) are abstract figures; tables show 22.6 to 29.8 (+32%) and 40.2 to 56.2 (+40%). No conflict, only rounding. The abstract's 54.3% for weaker agents is not visible in the GPT-4o-mini row (9.2 to 14.1 is +53% rounded); not resolved.
6. c15 (Break It Down): "skills from whole tasks often hurt" is true for code skills (-4.1 on the average) but the text drop (-1.2) lies inside the 95% intervals (22.1 [20.2,24.2] vs 20.9 [18.9,22.9]). K13 says so.
7. a14: the measured quantity is token changes per decision cycle (Rete work), not tokens. Wording fixed in K05.
8. b16 and others show a broken character where the plus-minus sign was lost (6?2). The values are Voyager's 6+-2 etc.; no numeric damage.
9. a27 / b17 / c02 and a26 / b16 / c01 are the same Voyager tables. Counted once for independence.

## Contradictions between sources

- AWM baseline: AWM reports the BrowserGym baseline at 23.5 for GPT-4. ASI reports GPT-4 vanilla at 12.3 on the same benchmark and copies AWM at 35.5. So the relative gain is +51% or +189% depending on baseline. Absolute AWM numbers are comparable, relative ones are not.
- AWM vs ReasoningBank: ReasoningBank puts AWM below no-memory for Claude-3.7 (40.8 vs 41.7), and failures hurt AWM there; ASI has AWM +3.6 for Claude-3.5. Suggests AWM gain is model- and harness-dependent.
- Self-written skills: SkillsBench says no gain; ASI, SkillWeaver and ExpeL report gains from self-induced procedures. Difference: those systems execute and verify or select by outcome; SkillsBench self-generation does not. Not a clean experiment, so left as contested.
- Soar utility problem: Minton and Tambe et al. predict slowdown; Doorenbos found no average growth in match work at 10k chunks but wall-clock growth. The match-cost fix (restrict rule form) is the one thing both camps agree on.
- Power law: Doorenbos and Rosenbloom and Newell show straight log-log lines; Heathcote and Evans say exponential in unaveraged data. The Soar curves are single-system, with no fitting comparison.
- Voyager ablation order: the library is not the biggest ablation (curriculum -93%, verification -73%), but the paper's title story is the library.

## Weak spots

- Most Soar-era claims come from one group (Laird, Rosenbloom, Newell, Tambe). Only Taatgen (ACT-R) and Minton and Etzioni (EBL) are outside, and Minton and Etzioni were not opened.
- Doorenbos probes: 10 problems from one generator, one dispatching domain.
- Voyager uses 3 runs per cell; the diamond result is 1 of 3. Zero-shot transfer is 4 tasks in one game.
- AWM Mind2Web task success is 0.7 to 4.8%; differences of 1 to 3 points on small N are noise-level.
- SkillsBench and Break It Down are 2026 preprints; each is single-source for its key effect.
- CogRec numbers are read from figures; the headline table was not recoverable.
- None of these studies equalise tokens. Authoring cost (the model writing the skill) is rarely counted. K10 to K14 need an equal-token re-test before we rely on them.
- No source tests the Soar idea that matters most to us: compile only on an impasse, with the accessed-fact conditions, and measure the cache hit rate over a stream.

## Seen only in snippets or abstracts

Heathcote, Brown and Mewhort 2000 (40 datasets, 7910 series, 475 subjects: repository abstract only); Evans et al. 2018 (abstract); Rickard 1997 (abstract); Tambe, Newell and Rosenbloom 1990 (abstract only, pages 299 to 348 not read); Minton 1990 (not read); Etzioni 1990 (abstract); Laird 1986 Machine Learning (abstract only); Newell and Rosenbloom 1981 (not read, via citations); Mitchell, Keller and Kedar-Cabelli 1986 (abstract); "More Skills, Worse Agents?" 21% drop (search summary only, c29); Kirk, Wray and Laird 2023 (abstract); Fan and Lan 2026 review (read as arXiv abstract page, mapping tables not checked). Claims that rest on these are marked contested or single-source.

## GAPS

1. Does an equal-token store-and-reuse arm beat no memory for our agent when the stored items are keyed by accessed facts and written only on an impasse resolution? (No source tests the impasse-triggered write; all LLM systems write after any success.)
2. What does it cost, in tokens, to author and to check a stored procedure, and is the net saving positive after 20, 50 and 200 items? Literature mostly ignores authoring cost.
3. Which admission rule is best at equal tokens: execution-verified, outcome-verified by an independent check, or reuse-count threshold (the ACT-R experience threshold)? Xiong, ASI and Voyager each test one rule on different tasks.
4. Does the failure mode of over-general stored rules (applied outside their conditions) occur with LLM agents, and does an explicit precondition check before reuse remove it? No LLM study measures wrong-application rate of retrieved skills directly.
5. What is the right grain: per-subgoal vs per-task procedures, and does the Break It Down effect hold on reasoning tasks (not tool/code environments)?
6. How fast does a store go stale or harmful: can a wrong or outdated entry be detected and removed (repair, utility-based deletion)? Xiong found a noisy judge deletes good records; Soar has no solved answer either (chunk inhibition only).
7. Do the Soar learning curves, and ours, follow power or exponential form when fitted per run? Decides whether to expect diminishing returns early and where to stop adding entries.
8. Does the gain from workflow memory vanish as the base model gets stronger (AWM +12 at GPT-4 level, +3.6 at Claude-3.5, negative at Claude-3.7 in one report)? We need a measurement on our own base model before building the store.
9. Does a stored library transfer across task families without being rewritten (SkillWeaver strong-to-weak, Voyager to AutoGPT), and what share is lost vs a per-task rewrite (Skills-in-the-wild refinement results, c14)?
10. Can a compiled entry reduce LLM calls on repeated impasse types (CogRec) without lowering accuracy on a non-recommendation task? CogRec data are read from figures only.

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d16). New claims are K22 to K30; K02, K08, K11, K16, K17 and K20 gained evidence ids and a short "Gap search" note. Web search was out of quota, so sources were opened directly as arXiv PDFs (Dynamic Cheatsheet 2504.07952, LATM 2305.17126, Buffer of Thoughts 2406.04271, Agentic Plan Caching 2506.14852, Memp 2508.06433, AutoManual 2405.16247, Agent KB 2507.06229, ACE 2510.04618, Evo-Memory 2511.20857). The human power-law papers stayed at abstract level (Europe PMC; the journals are paywalled). Several tables came out of the PDF text with scrambled columns; those figures are marked "uncertain" in the evidence lines and are not used in claim text.

### Gap status

1. Impasse-triggered write: PARTLY CLOSED. Agentic Plan Caching (write only after a miss and a verified success) and Buffer of Thoughts (write only if novel) already use miss-triggered writes (K22). Neither tests it against write-after-every-success, and neither keys by accessed facts. The comparison itself stays open.
2. Authoring cost and net saving at 20, 50, 200 items: PARTLY CLOSED. Cheap authoring costs about 1.2 to 1.3 percent of total cost (APC), a rule manual cost about $14 for 36 ALFWorld tasks, LATM gives O(nc + C) (K24). Break-even near a 1 percent hit rate is my derivation from APC tables. No source reports tokens per entry for reasoning items; stays open for our agent.
3. Best admission rule at equal tokens: OPEN. Memp is the only same-task comparison (error-driven revision beat append-all and success-only). Count-threshold admission was not found in any LLM system (K26).
4. Over-general reuse in LLM agents: MOSTLY CLOSED for occurrence (K25, established). Hits score below misses under semantic and full-history caches; looser matching lowers accuracy; raw replay beats nothing but loses 3.0 points to adapted reuse; LATM's dispatcher errs 4 to 5 percent. NOT closed: no study measures a precondition check directly, so "does the check remove it" is open.
5. Grain on reasoning tasks: OPEN. BoT uses task-class templates, DC uses per-query insights, LATM uses per-family tools; none compares per-subgoal with per-task grain on reasoning. Break It Down remains tool and code only.
6. Staleness and removal: PARTLY CLOSED (K27). ACE shows tolerance to occasional bad updates and collapse under full rewrites; counters exist but false deletions were not counted. Natural staleness is unmeasured.
7. Power or exponential: OPEN. Human abstracts favour exponential or delayed exponential per participant (d15, d16); Soar curves were never refit; the only LLM per-run numbers (APC cold start, 5 points) fit a line best (K30, derived and weak). Full texts of Heathcote and Evans are still unread.
8. Gain versus base-model strength: PARTLY CLOSED as a pattern (K28, K08): small models cannot write entries, strong models gain less when the stream does not repeat. Not closed for our model; needs our own measurement.
9. Transfer without rewrite: PARTLY CLOSED. Strong-to-weak works for tools and procedures (LATM, Memp, K16) but the maker must be strong (K29). The loss against a per-task rewrite is still unmeasured; Agent KB's raw-versus-adapted gap (3.0 points) is the nearest number.
10. Compiled entry cutting LLM calls outside recommendation: PARTLY CLOSED (K20). APC cut cost 50.31 percent at 96.61 percent of accuracy on five non-recommendation workloads. It is a plan-template cache, not a Soar impasse rule, and accuracy loss reached 5.5 points on FinanceBench.

### New cautions for the agent test plan

- Add a same-instruction empty-memory arm and a random-entry arm. Dynamic Cheatsheet's empty arm captured about half the gain on Sonnet AIME 2024 and Memp's random retrieval captured about 65 percent of one gain (K23).
- Memp shows memory can raise commonsense scores and lower hard-constraint scores on TravelPlanner. Report constraint-type breakdowns, not one score.
- Single-run cells on 30-question sets move 3.3 points per question; the Dynamic Cheatsheet differences between DC-Cu and DC-RS are inside that noise.

### Still unread after this pass

Heathcote 2000 and Evans 2018 full texts; Rickard 1997; Tambe 1990; Minton 1990; Etzioni 1990. K02 therefore stays contested. A CRAFT (2309.17428) download was damaged and not read.
