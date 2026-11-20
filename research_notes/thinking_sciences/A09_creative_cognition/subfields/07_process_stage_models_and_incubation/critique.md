# Critique: A09.07 Process stage models and incubation (cross-check)

## Re-opened this session (abstract or API text, not full PDF)
Confirmed:
- Sio and Ormerod (2009): abstract confirms positive incubation effect, divergent tasks > insight tasks, longer preparation helps, high-demand fillers shrink it, low-demand beats rest on linguistic insight. The abstract gives no d.
- Wagner et al. (2004): "more than twice as many subjects gained insight into the hidden rule after sleep" (8 h sleep vs nocturnal or daytime wake). Matches a25 and b06 (about 60% vs 23%).
- Lacaux et al. (2021): N = 103; abstract says 83% (N1) vs 30% (awake), effect vanished in deeper sleep. Matches a26 (20/24 vs 15/49; 24+49+14 = 87 = 103 minus 16 early solvers, consistent).
- Smith and Beda (2020, JEP:G 149(1), online 2019): abstract confirms incubation effect and larger gain in new contexts. Year in a20/a21 is the online year.
- Lin et al. (2025) sleep-time compute: abstract confirms ~5x less test-time compute, +13% and +18%, 2.5x cost per query.
- Muennighoff et al. (2025) s1: abstract confirms 50% to 57% on AIME24 via budget forcing.
- Ghosal et al. (2025): abstract confirms rise then decline from overthinking and parallel thinking up to 20% better.
- Huang et al. (2024): abstract confirms LLMs cannot self-correct reasoning without external feedback and can degrade. Per-model numbers (c17) were not re-opened.
- Gilhooly (2016): abstract confirms support for unconscious work over intermittent work and beneficial forgetting.

Not re-opened (publisher pages returned shells or rate limits): Nieuwenstein et al. (2015) numbers (g .15, trim-and-fill .018, BF 7.83). Three evidence lines (a15, b02, b20 context) agree, so they are kept, but they come from one paper.

## Corrections and discrepancies
1. Sio and Ormerod mean d: a04 says unweighted unbiased d = 0.41 (median 0.26); a09, b07, b08 (via Gilhooly) say about 0.29. The abstract gives neither. Most likely 0.41 is unweighted and 0.29 weighted, but this was not verified. Claim K02 reports the range. b08 is marked opened:false and its number is second-hand.
2. Nieuwenstein replication: a16 reports 58.2% (deliberation) vs 61.9% (distraction) within subjects; b01 reports 55.61% vs 55.17% first-done between subjects. Same N = 399, different analyses. Both are null. Do not quote one as "the" figure without the condition.
3. a14/b09 Strick meta-analysis g = 0.224 is second-hand (via Gilhooly); b03 quotes d = .218. Treat as about 0.22.
4. c13: "13.8 to 5.7 per the table" for switch tokens is flagged as uncertain in the evidence line; unverified.
5. c11 quotes 20%, 22% and 47%; only 20% confirmed from the abstract.
6. a31 and b22 are the same Orru et al. (2023) paper counted twice; independent_sources for K20 counts it once.
7. b24 and c01 are the same Lin et al. paper, counted once in K13.
8. Smith and Beda: the abstract says incubation is greater in new contexts, but the interaction test was not significant in either experiment (F = 1.31, p = .255; F = 2.89, p = .092). The claim rests on simple effects. K07 is marked contested.

## Contradictions between sources
- Sleep helps (Wagner, Lacaux) vs no REM or TMR effect (b18, b19). Likely due to task type, difficulty (a27) and small cells (b18 cells of 17 to 44).
- Mind wandering helps (Baird 2012; b14, b15) vs repeated null replications (a23, b12). The original is the outlier by count of labs.
- Unconscious thought gives small effects (Strick g .22) vs publication-bias-corrected zero (g .018).
- Sequential extension helps (s1) vs hurts (Ghosal, Gema, Thoughtology): a non-monotonic curve, not a contradiction.

## Weak spots
- Most human incubation numbers come from small studies (median N 25).
- Many primary studies (a10 Segal, a11, a12, a13, a17, a22, a28, a29, b05, b06 details, b09, b10, b13, b16, b17) were seen only through reviews or snippets, opened:false.
- No LLM paper directly implements Wallas stages or an incubation step. LLM evidence is by analogy (sleep-time compute, Wait, parallel sampling). Frame K21 as a research gap, not a finding.
- Human incubation effects depend on unsolved-impasse selection; LLM "impasse" is undefined.
- Creative-domain LLM claims (b23, c22) measure divergence against averages, not incubation.

## GAPS (most decision-relevant first)
1. Does a "set aside, do unrelated filler, return with fresh context" step improve an LLM on problems it failed once, at equal tokens, versus simply resampling from scratch?
2. How much of the human incubation effect is forgetting a misleading context (Smith/Beda, Ward) and does an LLM context reset reproduce it (the interaction test was not significant)?
3. At equal tokens, is sleep-time (offline) compute better than the same tokens spent at test time for unpredictable queries, and where is the crossover on agentic tasks?
4. What is the true weighted vs unweighted Sio and Ormerod mean d, and what are the exact moderator effects (open the full paper)?
5. Does Wait-style continuation beat independent restarts on insight and lateral-thinking tasks (BRAINTEASER), not just math?
6. Are there 2024 to 2026 LLM papers explicitly testing "incubation", "aha", or stage-model prompts (Wallas) on creativity benchmarks with measured gains? Not found here.
7. Do immediate-incubation designs (pause before first attempt) have any LLM analogue, such as planning-before-reading, with measured effect?
8. Do the sleep results (N1 sweet spot, 83% vs 30%) replicate independently, and does a lighter "partial consolidation" analogue exist for models?
9. How should an agent detect impasse (the human selection step) cheaply and reliably?
10. Is the Smith/Beda context effect replicable outside Smith's lab with preregistration?

## Gap search results (gap searcher, 2026-11-19)
Limits this session: WebSearch budget exhausted, arXiv/OpenAlex/Semantic Scholar APIs returned 429 or timed out. Work used direct arXiv abs/PDF fetches only. Evidence in evidence_d.jsonl (d01-d19).

Closed or mostly closed:
- Gap 3 (sleep-time vs test-time at equal tokens): mostly closed. Offline compute wins at low test-time budgets (about 5x fewer tokens; 1.5x on agentic SWE) but test-time-only slightly wins at high budgets; benefit grows with query predictability (d01-d06, new claim K22). Offline tokens are extra spend, so equal total token superiority is not shown.
- Gap 9 (impasse detection): answered in the negative. Intrinsic self-judgement is unreliable (74.7% answer retention, oracle labels drive the gain, no-test Reflexion 52% vs 60%). Needs an external test (d11, d12, d15, K24).

Partly answered:
- Gap 1 (return step vs resampling): Reflexion shows resampling stalled on failed items and a written lesson helped, but not at equal tokens and not with unrelated filler. No direct test of an incubation step (d13, d14, K23). Open for the exact design.
- Gap 5 (Wait vs restarts): on math, restarts with voting beat Wait by up to 22% at 16K tokens (d07, d08). No BRAINTEASER or insight test found (d09, d10 give only base rates). Open for lateral thinking.
- Gap 2 (forgetting misleading context): LLM fixation analogues exist (R1 rumination, inverse scaling, d16, d17) and distilled lesson beat full memory by 8% (d14). No context reset test. Open.

Stayed open:
- Gap 4 (Sio and Ormerod d): publisher PDF unreachable, still a 0.29 to 0.41 range (d19, K26).
- Gap 6 (2024-2026 LLM papers testing incubation, aha or Wallas prompts): none found; search tools were blocked, so this is "not found with the budget available", not "does not exist". K21 unchanged.
- Gap 7 (immediate incubation analogue), Gap 8 (independent replication of N1 sleep effect), Gap 10 (preregistered Smith/Beda replication): not searched, tools blocked.
