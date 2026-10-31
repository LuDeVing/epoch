# D03.01 Cross-check critique (classical propositional and first-order logic)

## Re-opened sources (this session, PDF text via pdftotext)
Confirmed against paper text: Logic-LM table (GPT-4 PrOntoQA 77.40/98.79/83.20; ProofWriter 52.67/68.11/79.66; FOLIO 69.11/70.58/78.92; LogicalDeduction 71.33/75.25/87.63; AR-LSAT 33.33/35.06/43.04; executable rate FOLIO GPT-4 79.9 to 85.8, GPT-3.5 66.7 to 84.3). LINC (FOLIO GPT-4 CoT 75.3 vs LINC 72.5, p=0.58; StarCoder+ 56.0 vs 41.8; ProofWriter 96.4/98.3; syntax errors 38%). Premise Order (over 30% drop; GPT-4-turbo forward 96.5 vs 76.0 at tau 0.5, fact hallucination 11.5; R-GSM 94.1 to 85.0; Gemini and GPT-3.5 over 65 to below 25). FOLIO (1,430 / 487; majority 38.5; Table 5: 68.4/50.4/93.3/56.0 and 86.1/51.7/93.9/63.8). SatLM (GSM-Sys 69.4, LSAT 35.0, BoardgameQA 79.4, CLUTRR 68.3, ProofWriter 99.7 vs CoT 80.1). Multi-LogiEval (propositional mean 85.42 to 42.96; first-order 83.21 to 32.96; GPT-4 propositional 89.17 to 66.67). JustLogic (human 73.0, R1 80.9, o1 72.9, GPT-4o 65.6, Llama3-8B 49.8, 70B 53.1). LogicBench (ChatGPT 48.04, GPT-4 63.98 Yes-label average; GPT-4 modus tollens Yes 59.05). ProverQA (GPT-4o 94.20/79.40/50.00; Claude-3.5 95.20/83.60/56.40; no-distractor 94.4/82.2/57.4; ordered 95.6/87.4/62.4; 60-item control 58.33 to 43.33 direct, 68.33 to 45.00 CoT).
All ten sets of numbers matched. No numeric corrections needed.

## Clarifications
1. Multi-LogiEval: a21 gives table means (85.4 to 43.0 propositional); c20 gives the abstract (about 68 to about 43). Both are right; they aggregate differently (abstract covers all logic types). Use per-type numbers for logic claims.
2. LogicBench: a20/b13 (48.04, 63.98) are Yes-label accuracy; c18 (81.9, 89.6) is binary-QA average. Not a contradiction. Name the metric every time.
3. Duplicates: ProverQA (a22, b01-b04, c13, c14), FOLIO (a06, a07, b05, b06, c11, c12), Logic-LM, LINC, SatLM, Premise Order, LogicBench, Saparov each appear in several evidence files. They are the same paper, not replications. independent_sources in claims.jsonl counts papers (and distinct research groups), so many claims are "single-source" despite many lines.
4. a08/b17 (Saparov): 93.2 + 2.4 + 5.9 = 101.5; the split is "as printed" and was not re-opened. Treat as approximate.
5. Premise-order effect was tested only on GPT-4-turbo, PaLM 2-L, Gemini 1.0 Pro, GPT-3.5. No 2025 reasoning model, so the size today is unknown.

## Contradictions between sources
- Solver route vs CoT: Logic-LM and SatLM show large wins; LINC on GPT-4 FOLIO and Logic-LM's own PrOntoQA GPT-4 (CoT 98.79 vs 83.20) show CoT equal or better. Depends on model strength and on whether the task is search-like.
- Logic-LM++ shows repair is not reliably helpful (GPT-3.5 FOLIO 62.80 to 62.25), against Logic-LM's gain in executability. Executable is not the same as correct.
- Belief bias: b23 and b24 conflict (reasoning flaw vs response bias); neither opened.

## Weak spots
- Not opened (opened:false): b23 Evans et al. 1983 numbers (recalled), b24, b25. Claim K22 rests on these and is marked contested.
- Snippet-level or not re-checked: a14 "Uncertain predicted 57% vs 41%"; a24 JustLogic Table 4 values; b22 consistency metrics; c27/c28 (DSP, Wu et al.) numbers; ZebraLogic beyond headline; LoGiPT ranges; LogicAsker figures.
- Foundations (Frege, Godel, Church, Turing, Cook) rest on SEP and Wikipedia, not originals. Fine for dates, weak for detail.
- Nearly all LLM results are accuracy on synthetic or semi-synthetic benchmarks, mostly 2023 models. No study measures a scaffold that checks stated rules for contradiction (the D03 use case) at equal tokens.

## GAPS
1. Does a solver or consistency-check step still help reasoning models (o1, R1-class, current frontier) on FOLIO and ProverQA hard, at equal total tokens, or do they already match it?
2. How well can an LLM detect that a set of stated rules is inconsistent (UNSAT) versus merely hard? No benchmark of contradiction detection in natural-language rule sets was found.
3. How often does back-translation (formal to English, then compare) catch translation meaning errors, and at what cost? Logic-LM++ suggests plain repair adds errors.
4. Do premise-order and distractor effects persist in 2025-2026 reasoning models, and does a restate-in-dependency-order step recover them at equal tokens?
5. Can disagreement among CoT samples predict when a solver call is worth making (LINC found complementary errors)?
6. Modus tollens, negation and contrapositive weakness: does an explicit contrapositive step fix it, and for which models?
7. Verify Evans et al. (1983) numbers and the Trippas/Dube response-bias account from the papers themselves, so belief-bias claims are not recalled from memory.
8. Do UNSAT/AMBIG-style abstain signals transfer to a prompt-only scaffold with no real solver (SymbCoT-style verifier)? What is the coverage cost?
9. For semi-decidable first-order checks, does bounded counter-model search catch invalid conclusions better than proof search in S8?

## Gap search results (gap searcher, 2026-10-31)
Search tools: WebSearch quota ran out, and the arXiv, OpenAlex and Semantic Scholar APIs returned 429 after the first calls. I worked from papers I could fetch directly (arXiv PDFs, Springer, OSF) and read the text with pdftotext. 22 evidence lines are in evidence_d.jsonl (d01 to d22, all opened). Claims K12, K13, K15, K16, K22 were updated and K23 to K31 added. Because search failed, I could not look for papers I did not already know; "no source found" below means none among the papers I could open.

- Gap 1 (solver still helps reasoning models?): PARTLY ANSWERED, still open at equal tokens. R1 chain-of-thought alone scores 86.2 on FOLIO (d16), above the GPT-4 solver pipelines (Logic-LM 78.92, d11). On search-heavy puzzles reasoning models use about 10x tokens and still collapse at large size (ZebraLogic X-Large: o1-full 42.5, R1 28.5; d17). On ProverQA Hard, an outcome-RL 7B reaches 91.3% but only 22% of chains are sound (d19). Reasoning models differ a lot (K&K: o3-mini-high 0.94, R1 0.81, o1 0.42; d22). No paper compared solver versus no solver on reasoning models at equal tokens.
- Gap 2 (detect inconsistent rules): ANSWERED in part. SATBench is the benchmark I had missed (d05, d06). Easy UNSAT is near 98% for o4-mini and R1; hard UNSAT is 65.0 (o4-mini), 83.6 (R1), 18.9 (GPT-4o). Naming the conflicting subset is much harder (SATQuest, d08). Caveat: random CNF, not realistic rule sets.
- Gap 3 (back-translation catch rate and cost): STILL OPEN. Nearest evidence is mixed: solver equivalence filter plus human check gave 97/100 faithful clauses (d07); pairwise semantic check +5.9 for GPT-4, neutral for GPT-3.5 (d11); LLM-written tests +6.6 (d21); checker-guided repair raised pass rate but not accuracy (d10). No catch rate per injected error and no token cost.
- Gap 4 (premise order and distractors in reasoning models): STILL OPEN. Only distractor evidence on math (d20: R1 error 1.5% to 4.5%). No premise-order test on a 2025-2026 reasoning model, and no restate-in-order test, was found.
- Gap 5 (sample disagreement to trigger solver): STILL OPEN. ZebraLogic shows large oracle-versus-vote headroom (60.3 vs 38.0; d18) but nobody gated a solver on disagreement.
- Gap 6 (contrapositive step): STILL OPEN, weak evidence. A bundled ablation shows -3.8 points on 135 items without contraposition and GPT-4 gains only +0.6 overall (d15; model labelling in its Table 4 is inconsistent). Modus tollens stays harder in JustLogic (d16). No reasoning-model test.
- Gap 7 (belief bias numbers): CLOSED for Evans 1983 and the response-bias account. Evans numbers now from the paper (d01 to d03; the recalled 89/56/71/10 were close, true Exp 2 values are 88/56/72/13). The Trippas 2018 meta-analysis (d04, 22 studies, N=993) supports response bias at group level with individual-difference moderation. Dube et al. 2010 and Heit and Rotello 2014 were not opened. K22 changed from contested to established with the narrower wording.
- Gap 8 (abstain signals in prompt-only scaffold): PARTLY ANSWERED. A real SMT verifier verifies only 15 to 45% of chains at 84 to 94% precision (d09). A prompt-only verifier costs about 30% extra output tokens and removed unfaithful-correct answers in a small manual check (d14) but reports no coverage. The GSM-Sys UNSAT/AMBIG result (K13) remains single-source and solver-based.
- Gap 9 (counter-model versus proof search): PARTLY ANSWERED. SMT counter-model check beat LLM judging of the same formulas (0.78 vs 0.66 F1; d12, d13), but no test compares it with proof search, and strong end-to-end models won on familiar data.

Other corrections: K16 text "about 90% acceptance of believable invalid syllogisms" is now replaced by the measured 92, 72, 67 across the three experiments. K26 is marked contested because the back-translation sources disagree.
