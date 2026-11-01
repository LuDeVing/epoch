# D03.02 Satisfiability and SMT solving: cross-check critique

Cross-checker pass, 2026-11-01. I re-opened (full PDF text via pdftotext) these sources: Mitchell/Selman/Levesque 1992, Selsam et al. 2019 (NeuroSAT), Ye et al. 2023 (SatLM), Pan et al. 2023 (Logic-LM), Olausson et al. 2023 (LINC), Wei et al. 2025 (SATBench), Lin et al. 2025 (ZebraLogic), Hao et al. 2025 (Z3 planning), Wu et al. 2024 (Lemur). Claims file: claims.jsonl (25 claims, D03.02-K01 to K25).

## Numbers re-checked and confirmed

1. Mitchell 1992: 50%-satisfiable point 4.55 (20 vars), 4.3 (50), 4.3 (140), conjecture about 4.25 at large N. Confirmed (a01).
2. SatLM table: STANDARD 21.0, COT 46.5, PROGLM 43.4, SATLM 69.4 on GSM-Sys; LSAT 35.0; BoardgameQA 79.4; CLUTRR 68.3; ProofWriter 99.7; GSM 71.8 vs 72.7; self-consistency row 80.9/84.8/90.9/37.4/80.7/80.1/99.7. Confirmed (a13, b04, b06).
3. SatLM selective accuracy GSM-Sys 77.1 vs 45.2, GSM 77.2 vs 73.8, CLUTRR 89.9 vs 73.7; wrong answers 52.5 vs 20.6. Confirmed (b05, b25). Planning vs execution error split 72.5/42.5/47.5 confirmed (a15, c03).
4. Logic-LM Table 2, GPT-4: PrOntoQA 77.40/98.79/83.20, ProofWriter 52.67/68.11/79.66, FOLIO 69.11/70.58/78.92, LogicalDeduction 71.33/75.25/87.63, AR-LSAT 33.33/35.06/43.04. Confirmed (b01, c05). AR-LSAT executable 11.3 to 21.8 (GPT-3.5) and 32.6 to 39.8 (GPT-4) confirmed.
5. LINC: GPT-4 FOLIO CoT 75.3 vs LINC 72.5, McNemar p = 0.58; ProofWriter 96.4 / 98.3; StarCoder+ 56.0 vs 41.8; GPT-3.5 62.6 vs 54.9; syntax errors 38/24/13%; GPT-4 predicted-label split 24/17/57. Confirmed (b07, b08).
6. SATBench Table 3: o4-mini 89.3 overall, 78.0 hard, 65.0 hard UNSAT; average row hard SAT 66.7, hard UNSAT 39.3, hard overall 53.0; error mix 68.7/17.0/14.3 vs 40.5/44.7/12.6; Table 4 trace numbers. Confirmed (a21 to a23, c13 to c17).
7. ZebraLogic table: o1-full 81.0 (97.2/92.1/78.0/42.5), R1 78.7, o1-preview 71.4 (x-large 17.0), o1-mini 59.7, Sonnet 3.5 36.2, GPT-4o 31.7. BoN-oracle 60.3 (N=32), 69.1 (N=128); majority vote 38.0 (N=32), 37.6 (N=128); BoN-RM 34.8; hidden tokens 5,144.6 and 5,346.3. Confirmed (b12, b13, c19, c20).
8. Hao et al.: TravelPlanner validation/test final pass 93.3/93.9 (Claude-3), GPT-4 91.9-93.3 band, GPT-4 direct 4.4; zero-shot four-task table TwoStage optimal 4/0/0/0. Confirmed (c21, c22).
9. Lemur: Code2Inv 133: ESBMC 68, GPT-3.5 103, GPT-4 107; SV-COMP 47: 1 / 14 / 25; average proposals 4.7 (Code2Inv) and 7.2 (SV-COMP). Confirmed (a27, b18, c24).
10. NeuroSAT Table 1: 85% overall, 96% unsat, 73% sat, assignment decoded 70%; SR(200) 25% at 4x iterations, under 10% at training iterations. Confirmed (a11). The pdftotext table had labels and values scrambled; I matched them against the table caption text.

## Corrections made

- b12 and b24 say GPT-4o scores 0.0 on ZebraLogic x-large. The table gives GPT-4o 0.5 (31.7 overall) and Llama-3.1-405B 0.0 (32.6 overall). Claim K10 uses 0.5. The point (near zero for non-reasoning models) stands.
- b24 says "ZebraLogic x-large: GPT-4o 0.0" and a25 says "Llama-405B medium 22.5, large 1.5". With the table realigned, 22.5/1.5/0.0 are the 405B's medium, large, x-large; a25 is right, b12/b24 are off by one row.
- c02/a15 say the no-solver variant "is on par with standard". Real numbers: SATNOSOLVER 26.6 / 23.7 / 40.7 vs STANDARD 21.0 / 22.2 / 41.2 (GSM-Sys / GSM / CLUTRR). It is +5.6 on GSM-Sys, not exactly equal. SATCOTSOLVER is 54.5 / 63.2 / 48.9, i.e. +8.0 and +8.1 over CoT on GSM-Sys and CLUTRR (paper text says 7.9, 8.1). K04 states the real figures.
- c23 and Hao: "81.6% and 91.7%" mix two things. 81.6% is the "Ours-20" row (20 iterations) on only 12 modified TravelPlanner queries; the base "Ours" row is 78.6%. The 91.7% belongs to the second table (not re-read in full). Both are small-N. K08 carries this caveat.
- a19 puts "StarCoder+ beats GPT-3.5/GPT-4 CoT by 38%/10%" next to FOLIO numbers. The abstract says this is on ProofWriter. Corrected in K06 by wording.
- c32, c33 (Z3 background, Mitchell from memory) are marked opened:false; Mitchell is now opened by me and confirmed, so the "from memory" ratio 4.26 in c33 is replaced by the paper's 4.3 (4.25 conjectured limit).

## Contradictions between sources

- FOLIO with GPT-4: Logic-LM 78.92 vs its CoT 70.58 (+8.3), but LINC 72.5 vs its CoT 75.3 (-2.8, p = 0.58). Different prompts, different FOLIO splits and sampling (LINC uses temperature 0.8, 10-vote), different CoT baselines. Logic-LM++ (84.80 on FOLIO, 204 test examples) is not independent: it builds on Logic-LM code. Status of K06: contested.
- CoT baseline on the same GPT-4/FOLIO moves by 4.7 points between papers (70.58 vs 75.3), which is as large as many claimed gains. Cross-paper accuracy gaps below about 5 points should not be trusted.
- ZebraLogic says hidden tokens track Z3 conflicts, while SATBench says model size plateaus. Not contradictory: different model classes (reasoning vs non-reasoning).
- SATBench hard UNSAT: o4-mini 65.0 but DeepSeek-R1 83.6 and V3 74.3. The "best model 65.0%" framing in the abstract is about overall o4-mini, not the best on UNSAT. Use per-model rows, not the headline.

## Weak spots

- Independence is thin. Most "independent sources" for K03 reuse the same models family (GPT-3.5/4, code-davinci-002) and similar benchmarks (ProofWriter, FOLIO, CLUTRR). All LLM numbers come from 2023-era or early-2025 models; none test current frontier reasoning models with a Z3 tool (R1, o4-mini, GPT-5, Claude 4/5 class) on the same pipelines.
- The solver gains are strongest on synthetic data (ProofWriter 98-99.7) where translation is easy. That is where the benefit is least informative for open-ended agent work.
- No source in this folder measures tokens or cost at equal budget. SatLM uses few-shot greedy single calls; Hao and Lemur use many calls. Our equal-token comparison is untested everywhere.
- Single-source claims: K02, K11, K13, K14, K15, K16, K18, K19 to K25. K15 and K16 are large effects from one group each; Lemur's baselines (ESBMC, UAutomizer under a time limit) are weak tools for those tasks.
- Hao et al.'s no-solver ablation (25.2%) and plan-repair table rest on 12 and 39-query sets.
- LLM-Modulo numbers (20%, 65%, c34) come only from a quotation in Hao et al.; the original was not opened.
- VeriCoT table values were extracted loosely (b19) and are not relied upon.
- Not re-opened this pass (opened by authors earlier, plausible, unchecked): Chaff speed-ups (a07), Z3 SMT-COMP results (a09), Proof of Thought (b17), Faithful CoT (b16), Fuzz4All (c26), DCP-Bench (c31), LoGiPT (c27), FOLIO paper (b09, b10), Dziri (b22), Kambhampati 12% (b21). Snippet-level only: c32, c33, c34 are not read.
- Date oddity: c31 DCP-Bench is arXiv 2506 but listed as 2026 (journal version likely). Not a content problem.

## GAPS

1. Do the solver gains hold with current reasoning models (o-series, R1, GPT-5, Claude 4/5 class) that already do long internal search? Run SatLM-style Z3 tools against a reasoning-only baseline on ZebraLogic x-large and SATBench hard UNSAT at equal total tokens.
2. What is the token cost of the spec-then-solve loop (spec writing, retries, solver output reading) compared with plain extended thinking on the same items? No study reports equal-budget curves.
3. How often do silently wrong formalisations pass (solver says SAT/UNSAT of a formula that does not match the problem), and which cheap check catches them (plug the model back into the original text, second independent translation, majority of translations as in LINC)?
4. Is there a reliable gate that tells, before solving, whether a task is crisp enough for the solver path versus fuzzy (StrategyQA-type)? Measure gate accuracy and the cost of wrong routing.
5. What is the best use of solver outputs inside one loop: unsat core to revise the spec, multiple models to add constraints, model to answer? Compare routing policies on SatLM-style outputs (SatLM reports AMBIG 15.5% vs UNSAT 3.5% on CLUTRR but no routing experiment).
6. Does a solver as oracle for best-of-N selection (ZebraLogic oracle 69.1 vs majority 38.0) recover most of the oracle gap on tasks where the checker can be run by code? Only one paper shows the gap; none closes it with a real checker.
7. Which representation do models write most reliably in 2025-26: Z3Py, CPMpy, OR-Tools, MiniZinc, raw SMT-LIB? DCP-Bench says Python frameworks; no check for logic puzzles and SAT-style tasks, and no study of Z3Py specifically.
8. Does the SAT-bias (answer "satisfiable" with an invalid assignment) disappear when the agent must output a witness that code verifies? SATBench classifies the error but does not intervene with a checker.
9. Do hardness-by-threshold results (easy-hard-easy) transfer to LLM task difficulty? SATBench uses clause count, ZebraLogic uses search space and Z3 conflicts; nobody has tested LLM accuracy against the 4.3 ratio directly.
10. How well does Z3 conflict count or search-space size predict, per instance, whether a scaffold should spend tokens on solver tooling versus thinking (use as difficulty probe for budget allocation)?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d15, all opened). New claims K26 to K33 in claims.jsonl. Web search quota ran out and the arXiv, Semantic Scholar and OpenAlex APIs returned 429, so I could not search freely. I worked from papers found in the first search (MathConstraint 2026, He and Wang 2025, Logic.py 2025) plus direct PDF reads of SATBench, ZebraLogic, VeriCoT, Proof of Thought and LLM-Modulo. Gaps that need a paper search are marked as not found, not as nonexistent.

1. Reasoning models with solvers: PARTLY CLOSED. MathConstraint (2026) runs 12 current models with and without a Python sandbox (pysat, z3). GPT-5.5 at max effort 66.9 to 80.9, Opus-4.7 42.6 to 77.5, Gemini-3.1-Pro 51.7 to 72.9 (d01). Logic.py (Llama-70B plus solver) beat o1-preview on ZebraLogic 91.4 vs 71.4 (hard 88.89 vs 60.83) (d07). Still open: ZebraLogic x-large and SATBench hard UNSAT with R1/o3/GPT-5 at equal tokens.
2. Token cost: PARTLY CLOSED. Per-instance tokens and cost with and without tools exist (d02): GPT-5.5 10,880 vs 12,081 tokens, cost 0.282 vs 0.151 dollars. No equal-budget curve; budgets differ per model. Round-budget sensitivity is measured (d03).
3. Silent wrong formalisation: OPEN. VeriCoT admits a self-consistent wrong translation passes (d13). SATBench measured 97% faithful clause-to-text translation by humans, wrong direction (d12). No study compares round trip, second translation or voting.
4. Routing gate: OPEN, with cost of wrong routing now measured. Fuzzy task to Prolog: EntailmentBank 27.4 vs CoT 81.8; hard grids on CoT: 8.9 vs 62.1 with Python (d08). Compile success is not a usable gate (Proof of Thought 82.4% compiled, precision 58.22%, d14). No gate classifier with accuracy found.
5. Routing of solver outputs (unsat core, models, answer): OPEN. MathConstraint shows multi-round repair matters (d03) but does not compare output types.
6. Code checker as best-of-N picker: OPEN. ZebraLogic's oracle rows use the gold answer, not a checker (d09). No paper found that closes the gap.
7. Constraint language: PARTLY. GPT-4o Python beats Prolog on ZebraLogic (71.7 vs 58.8 declarative; 38.1 vs 28.9 zero-shot) (d08). With free choice models often skip Z3 (d06). No Z3Py vs CPMpy vs MiniZinc test.
8. SAT-bias with a witness checker: PARTLY CLOSED. MathConstraint's verifier requires a witness; the claim-vs-verified gap is 12 to 54 pp without tools and 13 to 21 pp with tools (d04). SATBench: SAT-bias is 68.7% of o4-mini errors; a reminder prompt fixes 60.4% (d11). No clean A/B of witness-required vs not.
9. 3-SAT ratio vs LLM accuracy: OPEN. SATBench varies clause count only (d12). Not found elsewhere in what I could search.
10. Conflict count or solver time as budget predictor: MOSTLY NEGATIVE. Within a hard set, log solver time correlates -0.15 and -0.14 with model accuracy (d05). Conflicts predict hidden-token use in o1 (K13, d10) but not tested for correctness.

Corrections and notes from this pass:
- The LLM-Modulo 20% and 65% in earlier notes are not in the position paper (d15). What it states, citing other work: Blocks World 82% in 15 rounds, Logistics 70%, Mystery BW about 10%. Treat c34 as unverified.
- The 2026 MathConstraint results use a harder, different task (SAT/UNSAT with witness), so they do not replace the ZebraLogic and SATBench tests asked for in gap 1.
- Biggest tool gain (Sonnet, +52 pp) is from a model run without a thinking budget; do not read it as a gain for thinking models.
