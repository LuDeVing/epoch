# Critique: E06.05 Expert-novice schemas (cross-check)

## Corrections and confirmations (sources re-opened this session)
Re-opened arXiv full texts: Step-Back (2310.06117), GSM-Symbolic (2410.05229), Metacognitive skills (2405.12205), Han et al. (2411.19456), Shi et al. GSM-IC (2302.00093), Zheng personas (2311.10054).
1. Step-Back: PaLM-2L physics 66.4 -> 73.2, chemistry 70.9 -> 81.8, GPT-4 +Step-Back 84.5 / 85.6; 20.5% fixed, 11.9% new errors; "more than 90%" of remaining errors at the reasoning step. CONFIRMED (b24, c14, c15, a20).
2. GSM-NoOp drops: o1-preview -17.5, o1-mini -29.1, GPT-4o -32.0, GPT-4o-mini -40.0, Phi-3-mini -65.7; 25 models, 100 templates x 50 = 5000. CONFIRMED. GSM8K above the symbolic centre for 21 of 25 models CONFIRMED (b18).
3. Skills paper: about 5000 skills reduced to 117; CoT 42.2 -> 53.88 (+11.6); +7.52 over PAL. CONFIRMED (c05, b26). Note: the "+3.5 over topic-based" line in c05 and "+3.5 over Complex CoT" are both stated; the paper text gives 3.5 over Complex CoT; the topic-based figure was not re-checked.
4. Han et al.: abstract confirms closed models rely on deep structure, open models more surface-sensitive, decreasing with scale. The "12 models" count and the random-weight Llama-3-70b control were not re-checked.
5. Shi et al.: 99.7% answer-in-samples, +35.5 for 0-shot CoT, 18% consistently solved, 45% best macro CONFIRMED. a18 says "macro 6.0" for CoT; the table row suggests 6.0 may belong to a different column (the abstract-level claim "macro under 30%" is safe). Treat the 6.0 figure as UNCERTAIN.
6. Personas: 162 roles, 2,410 questions, in-domain coefficient 0.004 (p<0.01) CONFIRMED. Wording "about 0.4 points" is the agent's own reading.
7. a22 and b23 / c16: GSM8K rows for analogical prompting come from a garbled table; c16 gives GPT-3.5 76.7 -> 77.8, which agrees with a22. Use c16.
No numeric correction was needed for the 10 checked items; two items flagged uncertain (Shi macro 6.0; skills +3.5 topic-based).

## Contradictions between sources
- Chi 1981 (novices 0% on expert categories) vs Mason and Singh 2011 (18-44% of novices chose expert categories). Different problems, different students, paper vs cards. Not a refutation but a large softening.
- Pattern-matching (Mirzadeh) vs orderly schema pipeline (Qu and Gomes; Han et al.). Unresolved; may both be true (stage fails, not absent).
- Step-back helps GPT-4 above CoT only slightly (84.5 vs 82.9) and for chemistry GPT-4 CoT 85.3-ish vs 85.6: gain over CoT is small for strong models.
- Training the sort (Schoenfeld course) vs tool training (Mestre 1988): sort improved in both, solving improved only with full course.

## Weak spots
- Founding paper never opened (paywall). All its numbers are second hand.
- Hardiman 1989, Silver, Chi-Glaser-Rees, Larkin, Gick-Holyoak, Quilici-Mayer, Rottman, Cole were only partially or not opened; some are ERIC abstracts.
- LLM results mostly arithmetic word problems (GSM8K family), not physics sorting. Link from "surface pull" to "expert vs novice schema" is analogy, not test.
- Many gains are prompt papers with reported, not independently re-run, numbers, on different models and token budgets. No equal-token comparison anywhere.
- Veldhuis detail comes via Wolf et al. only.

## Only seen in snippets/abstracts
a01, a10-a16, b06, b11, b13, b14, c22, c23 (one search).

## GAPS
1. Does an LLM sort the Mason-Singh/Chi problems by principle like experts, and does sort quality predict its solve accuracy on the same items (never tested)?
2. At equal tokens, does a principle-first step (Step-Back, skill label) beat plain CoT on frontier reasoning models, or only on weaker ones?
3. Does skill/template-keyed memory retrieval beat surface-similarity retrieval at equal tokens, and by how much on hard math (not GSM8K)?
4. Does a restate-in-canonical-form or distractor-filter step recover GSM-NoOp/GSM-IC losses on current reasoning models, and what does it cost in tokens?
5. Does the novice-expert sort gap reproduce with crossed surface x principle items in large samples (Veldhuis-style) outside physics?
6. Does training the sort transfer to solving (conflict between Schoenfeld and Mestre) and what is the analogue for an agent without training?
7. Is surface sensitivity in models falling with scale and reasoning-mode (Han et al.) for 2025-2026 reasoning models?
8. What is the failure rate of wrongly named principles (38% in human principle group) in LLM principle-naming, and does a wrong principle hurt more than none?
9. Which of the 2020-2026 studies reproduce with contamination controls (GSM8K above centre for 21 of 25 models)?

## Gap search results (evidence_d.jsonl d01-d20, claims K20-K26)
Search note: WebSearch quota ran out; the OpenAlex and Semantic Scholar APIs were rate limited; arXiv search via page fetch and direct PDF and PMC full text worked. Gaps 2, 6 and 8 got only indirect evidence.

1. LLM sort of the Chi set (PARTLY CLOSED, open on the predictive half). Kortemeyer 2025 (d01, d02) had GPT-5 Thinking sort 60 exam items by solution similarity: topic-and-solution groups, not surface. Single author, single run, no human baseline, original cards not used, and no per-item link to solving (27/30 and 25/30 solved). Whether sort quality predicts solve accuracy: still untested.
2. Principle-first step vs CoT at equal tokens on frontier reasoning models (OPEN). No Step-Back test on reasoning models found. Indirect: plain CoT prompting adds marginal gain on o3-mini, o4-mini (+0.056 at 51% metric) and hurts Gemini Flash 2.5 at strict metrics (d10). Expect a small ceiling.
3. Skill-keyed vs surface-keyed memory on hard math (PARTLY CLOSED, weak). Dynamic Cheatsheet (d11, d12): curated abstract memory 50.0 vs raw similarity retrieval 43.3 vs baseline 23.3 on AIME 2024 (Claude 3.5 Sonnet, 30 questions), but the instruction-only control already reached 36.7, GPT-4o results were mixed, and tokens were not matched. ReasoningBank (d13) agrees on web tasks (48.8 vs 44.1 vs 40.5). No direct skill-key vs surface-key test.
4. Restate or distractor-filter recovery on reasoning models (PARTLY CLOSED, wrong setting). DAGGER (d17) and AbstRaL (d18) show a structured, abstract first step recovers much of the loss (AbstRaL GSM-Plus distractor 82.3 vs CoT 76.3, original 91.8/89.2), but only with training on small models. Reasoning models recover at 5.2x tokens (d17) and CatAttack costs 1.5x to 3x tokens (d09). A prompt-only recipe at frontier scale: untested.
5. Crossed items, large samples, outside physics (CLOSED for biology). Smith 2013 and Bissonnette 2017 (d05, d06): faculty n=23 deep pairs 71.7% vs non-majors n=101 29.2%; framing lifted novices only to 39.6%; advanced and entering majors did not differ in free sort. Veldhuis (d03, 94 / 5 / 20) still second hand. Maths and non-extreme groups: open.
6. Training the sort transfers to solving (OPEN). Bissonnette: a revealed framework released expert-like sorting in advanced majors (cueing). No new data on solving. The untrained-agent analogue is still just the cue-then-solve test in claim K23/K26.
7. Surface sensitivity falling with scale and reasoning (MIXED). For name-and-number variants yes: Haiku 4.5 -1.3 (d16), only 8 of 20 open models significant (d15). For distractors no: reasoning models still degrade 14-20 points (d17) and error multiplies 3x to 5x under adversarial triggers (d08), though from low bases. Frontier 2026 NoOp numbers: not found.
8. Wrongly named principle (OPEN). Only PHYBench (d19): 79-96% of first errors are in deriving relations, 4-21% in reading the scenario; wrong-versus-none not measured.
9. Contamination (PARTLY CLOSED). GSM1k (d14): up to 8% drops in Phi, Mistral and some Llama; GPT, Gemini, Claude families show little gap. Dlugosz 2026 (d15): the GSM-Symbolic drop is significant for only 8 of 20 open models, with a number-size confound (K-S 0.12). Claim K09 should lean on NoOp and distractor results.

Corrections to earlier lines: K18 "no study found" changed to one preprint (single-source). K09 and K11 notes added. Uncertain figures (Shi macro 6.0; skills +3.5 over topic-based) remain unresolved. Not opened: Veldhuis original, Chi 1981, Dynamic Cheatsheet per-token costs, GSM-DC figures.
