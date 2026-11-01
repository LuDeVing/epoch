# Satisfiability and SMT solving: deep document

*Subfield D03.02 of formal logic. Written 2026-11-01 from evidence_a-d.jsonl (a01-a28, b01-b25, c01-c34, d01-d15), claims.jsonl (K01-K33) and critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Claim ids are D03.02-Kxx, shortened to Kxx. Sibling subfields in this run (Counterexample finding, Probabilistic and test-based reasoning, Test-time compute scaling, Hierarchical task networks) are only linked, not covered.*

## 1. What it is

SAT asks one question. Given a set of constraints, is there an assignment of values that makes all of them true? If yes, the solver returns the assignment (a model). If no, it says UNSAT, and a good solver can name a small subset of constraints that already clash (an unsat core).

SMT extends SAT. The constraints can use integers, reals, bit-vectors, arrays and functions. Z3 and cvc5 are the common SMT solvers. CP-SAT and MiniZinc are close cousins for finite-domain puzzles.

Why it matters to our agent. Our schema has two states that need a trustworthy check: S4 TEST (run candidates on a check) and S7 SELECT (look for a counterexample when two rules still fit). A SAT/SMT call is a check that code runs, not the model. Two uses:

1. Find a model. "Is there an assignment that meets every constraint?" The model is a witness that code can plug back in and verify.
2. Find a counterexample. "Is there an input where rule A and rule B differ?" Ask the solver to satisfy "A(x) != B(x)". A model is the counterexample. UNSAT means the rules agree on the whole domain.

The pattern in the literature is always the same. The language model translates a problem into a formal spec. The solver does the search. The model reads the result. The science is about where this gains, where it breaks (translation, fuzzy tasks) and what it costs.

## 2. History and theories in depth

**Random 3-SAT and the phase transition (1990s).** Mitchell, Selman and Levesque (1992, a01-a03) studied random 3-SAT with a simple Davis-Putnam solver at 20, 50 and 140 variables. Cost is low when there are few clauses per variable (many solutions, easy to find one) and low when there are many (a clash shows up fast). Cost peaks where about half of formulas are satisfiable. The 50%-satisfiable ratio of clauses to variables was 4.55 at 20 variables, 4.3 at 50 and 4.3 at 140. They conjectured about 4.25 for very large N. They also argued that earlier "SAT is easy on average" results came from a bad instance distribution (constant-probability model), so benchmark choice decides what a solver test means (a03). Split by outcome (a02): UNSAT instances near the peak are hardest, because proving no model exists needs the whole tree. Medians hide a heavy tail.

**Why the transition is sharp (1999-2021).** Monasson, Zecchina, Kirkpatrick, Selman and Troyansky (1999, a04, a05) used statistical physics. The SAT/UNSAT change is continuous for 2-SAT-like mixes and discontinuous (first-order) for 3-SAT; the discontinuous kind goes with exponential cost growth. Their non-rigorous replica estimate for the 3-SAT threshold was about 4.60 against about 4.27 from experiments. Friedgut's theorem gives a sharp threshold but leaves open whether it converges to a fixed value. Ding, Sly and Sun (2021, a06) proved the exact threshold for random k-SAT for all k above an absolute constant k0, by a one-step replica-symmetry-breaking formula. The k = 3 case (about 4.26) is still not proved. Status [E] for the shape of the curve (K01).

**Engineering that made SAT practical (2001).** Moskewicz et al. (Chaff, a07, a08) added three ideas. Two watched literals per clause make unit propagation cheap (over 90% of run time was propagation). VSIDS counts literals in recent conflict clauses and decays the counts, so search follows the conflicts. Restarts clear decisions but keep learned clauses. On the authors' hard EDA sets Chaff was 1 to 2 orders of magnitude faster than SATO and GRASP: on VLIW-SAT.1.0 it finished all 100 instances in under 10,000 s while the others aborted the first 19 of 20 tried. These are the authors' own runs (K02, [S]).

**SMT (2008).** de Moura and Bjorner's Z3 (a09, a10) joins a DPLL-style SAT core with theory solvers (linear arithmetic, bit-vectors, arrays, tuples) and E-matching for quantifiers. A prototype won 4 first and 7 second places in SMT-COMP 2007. It reads SMT-LIB and can return a model. Clients: Pex (test generation), Spec#/Boogie (verification). Quantified or nonlinear problems can return "unknown".

**Learned SAT (2019).** NeuroSAT (Selsam et al., a11, a12, b20) trains a message-passing net on only the sat/unsat bit. On SR(40) it reached 85% accuracy (96% on unsat, 73% on sat) and decoded a working assignment for 70% of satisfiable cases. At SR(200) with 4x iterations it reached 25%. A variant trained on unsat data clusters unsat-core literals together 98% of the time. It is not competitive with real solvers (K14, [S]).

**Language models enter (2022-2026).**
- Faithful CoT (Lyu et al. 2023, b16, c25): the model writes a symbolic chain (Python, Datalog, PDDL), a deterministic solver runs it. Relative gain over CoT: +6.3% math, +3.4% planning, +5.5% multi-hop QA, +21.4% CLUTRR. StrategyQA stays below CoT.
- SatLM (Ye et al. 2023, a13-a16, b04-b06, c01-c04): declarative spec plus Z3.
- Logic-LM (Pan et al. 2023; a17, a18, b01-b03, c05-c07) and LINC (Olausson et al. 2023; a19, a20, b07, b08, c08-c12): first-order logic plus a prover.
- Lemur (Wu et al. 2024; a27, b18, c24): the LLM proposes loop invariants, an SMT-based verifier checks them.
- Logic-LM++ (a28, b11, c28), LoGiPT (c27), Proof of Thought (b17, c29, d14), FLARE (c30), VeriCoT (b19, d13).
- Benchmarks that stress solvers: SATBench (a21-a24), ZebraLogic (a25, a26, b12, b13, c18-c20), MathConstraint (d01-d06), DCP-Bench-Open (c31).
- Planning with Z3 (Hao et al. 2025; c21-c23) and the LLM-Modulo position paper (Kambhampati et al. 2024; b21, d15).

**Competing views.** (a) "Solver is the engine, model is the translator": SatLM, Logic-LM. (b) "Strong models do not need the crutch": LINC finds no gain for GPT-4 on FOLIO (K06). (c) "Simulate the solver inside the model": FLARE (c30) reports state of the art on 7 of 9 reasoning sets without an external solver, but simulated search is not sound. (d) "Train the model to imitate the solver": LoGiPT (c27). We do not train, so (d) is out of scope.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Random 3-SAT is hardest where about half of formulas are satisfiable | 50% point at ratio 4.55 (20 vars), 4.3 (50), 4.3 (140); about 4.25 conjectured at large N | Mitchell 1992 (a01); Monasson 1999 (a04); Ding 2021 (a06) | [E] K01 |
| UNSAT proofs cost more than finding models | Near the peak, short UNSAT formulas are the hardest; medians hide a heavy tail | a02 | [E] with K01 |
| Chaff engineering gives huge speed-ups | 1 to 2 orders of magnitude over SATO/GRASP; VLIW-SAT.1.0: 100 solved in under 10,000 s vs 19 of 20 aborted | Moskewicz 2001 (a07) | [S] K02 |
| Spec + solver beats CoT and program-of-thought on constraint tasks | GSM-Sys: standard 21.0, CoT 46.5, ProgLM 43.4, SatLM 69.4. LSAT 35.0; BoardgameQA 79.4; CLUTRR 68.3; ProofWriter 99.7 | SatLM (a13, b04) | [E] K03 |
| Parity on plain arithmetic | GSM: SatLM 71.8 vs ProgLM 72.7 | SatLM (a13) | [E] K03 |
| The solver call is the active ingredient | SATNOSOLVER 26.6 / 23.7 / 40.7 vs STANDARD 21.0 / 22.2 / 41.2 (GSM-Sys / GSM / CLUTRR). SATCOTSOLVER 54.5 / 63.2 / 48.9 (about +8 over CoT) | SatLM (c02, a15) | [E] K04 |
| Logic-LM, GPT-4 (columns: standard / CoT / Logic-LM) | PrOntoQA 77.40 / 98.79 / 83.20; ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04 | Logic-LM Table 2 (b01, c05) | [C] K06 |
| LINC: no gain over CoT for GPT-4 on FOLIO | LINC 72.5 vs CoT 75.3, McNemar p = 0.58; ProofWriter 96.4 (GPT-3.5), 98.3 (GPT-4); StarCoder+ FOLIO 56.0 vs 41.8 CoT; GPT-3.5 62.6 vs 54.9 | LINC (b07, c08) | [C] K06 |
| Translation is the bottleneck | GPT-4 executable rate 79.9% FOLIO, 32.6% AR-LSAT (about 100% on synthetic sets); LINC syntax errors 38/24/13%; AR-LSAT executable 11.3 to 21.8 (GPT-3.5) and 32.6 to 39.8 (GPT-4) after self-refinement | Logic-LM, LINC (b02, c07, a20, c10) | [E] K05 |
| Self-refinement raises executability, not correctness | Mean executable gain +5.01; FOLIO accuracy +0.5. Logic-LM++ adds about 6 (GPT-4) and 3 (GPT-3.5); nothing on ProofWriter; GPT-3.5 FOLIO 62.80 to 62.25 as reported | Logic-LM, Logic-LM++ (b03, b11) | [E] K07 |
| Solver result types are usable signals | Selective accuracy GSM-Sys 77.1 vs 45.2 (ProgLM), coverage 90.0 vs 95.8; GSM 77.2 vs 73.8; CLUTRR 89.9 vs 73.7; wrong answers 52.5 vs 20.6 | SatLM (b05, b25) | [E] K08 |
| Unsat-core repair in planning | 78.6% repaired; 81.6% with 20 iterations; only 12 modified TravelPlanner queries | Hao 2025 (c23) | [E] K08, small N |
| LLMs are weak at UNSAT and hard search | SATBench hard SAT 66.7, hard UNSAT 39.3, hard overall 53.0 (averages; chance 50). o4-mini 89.3 overall, 78.0 hard, 65.0 hard UNSAT. DeepSeek-R1 83.6 and V3 74.3 on hard UNSAT | SATBench (a21, a22, c13-c16) | [E] K09 |
| Non-reasoning models fall to near zero on big grids | ZebraLogic overall: o1-full 81.0 (by size 97.2 / 92.1 / 78.0 / 42.5), R1 78.7, o1-preview 71.4 (x-large 17.0), o1-mini 59.7, Sonnet 3.5 36.2, GPT-4o 31.7 (x-large 0.5); Llama-405B 32.6 (medium 22.5, large 1.5, x-large 0.0) | ZebraLogic (b12, c18, a25) | [E] K09, K10 |
| Scale plateaus on hard instances | SATBench hard accuracy near 50-53% across Qwen3 and Llama families | SATBench (b15, c15) | [E] K10 |
| Selection is the bottleneck | GPT-4o greedy 31.7; best-of-N with oracle picker 60.3 (N=32), 69.1 (N=128); majority vote 38.0 (N=32), 37.6 (N=128); reward-model best-of-N 34.8. The oracle used the gold answer, not a code checker | ZebraLogic (b13, d09) | [S] K11 |
| Hidden tokens track solver conflicts | o1-mini 5,144.6 and o1-preview 5,346.3 mean hidden tokens vs 502.9 (GPT-4o-mini) and 543.7 (GPT-4o); about 400 tokens per Z3 conflict below 20 conflicts, plateau above 30 | ZebraLogic (c20, d10) | [S] K13 |
| Right label, wrong trace | Trace vs prediction accuracy: o4-mini SAT 94.7 vs 74.6; Claude-3.7 SAT 83.2 vs 47.4. Trace accuracy o4-mini 74.4, R1 78.0, V3 68.4, Claude-3.7 54.2, QwQ 52.4 | SATBench (a23, c17, b15) | [E] K12 |
| SAT-bias is the main error | 68.7% of o4-mini errors, 40.5% of R1 errors; context inconsistency 17.0% / 44.7%; condition omission 14.3% / 12.6%. Error-aware prompt fixed 60.4% (o4-mini) and 73.2% (R1) of previously failed cases | SATBench (b15, a24, d11) | [E] K29 |
| Text framing costs accuracy | Puzzle vs raw formula: gpt-4o-mini 53.6 vs 54.8; gpt-4o 58.2 vs 59.2; V3 84.0 vs 87.3; o4-mini 89.4 vs 94.3. LoRA on 1,100 traces: Qwen2.5-14B 51.9 to 53.6 | SATBench (a24) | [S] |
| Witness gap persists with tools | MathConstraint (329 items): claim-vs-verified gap 12 to 54 pp without tools (Sonnet +53.5, Llama +54.4, GPT-5.5 +12.1); 13 to 21 pp for GPT-5.5 and Sonnet with tools | MathConstraint (d04) | [E] K29 |
| Frontier models still gain from a sandbox with SAT/SMT libraries | Mean +28 pp over 12 models. GPT-5.5 66.9 to 80.9; Opus-4.7 42.6 to 77.5; Gemini-3.1-Pro 51.7 to 72.9; Claude-4.6-Sonnet (no thinking budget) 18.5 to 70.5 | MathConstraint (d01) | [S] K26 |
| Tool-use cost for thinkers | GPT-5.5 10,880 tokens ($0.282) no tools vs 12,081 ($0.151) tools; Opus-4.7 18,170 ($0.425) vs 23,441 ($0.208); Gemini-3.1-Pro 5,420 vs 23,181; Sonnet 35,046 with tools | MathConstraint (d02) | [S] K27 |
| Tool accuracy is round-budget sensitive | Halving 8 to 4 rounds costs up to 37 pp; SIM@1 is 0 to 20%, SIM@8 is 36 to 81% | MathConstraint (d03) | [S] K28 |
| Solver time does not rank items inside a hard set | Log solver time vs accuracy r = -0.15 (no tools), -0.14 (tools); median solver time easy 0.20 s vs hard 2.52 s | MathConstraint (d05) | [S] K30 |
| Small model plus a constraint DSL beats a reasoning model | Logic.py: Llama-70B 91.4 (hard 88.89) vs o1-preview 71.4 (hard 60.83); base Llama-70B 24.9 | Kesseli 2025 (d07) | [S] |
| Language of the spec matters | GPT-4o ZebraLogic easy/hard/avg: CoT 77.9/8.9/28.2; Prolog zero-shot 64.6/15.0/28.9; Prolog one-shot 96.8/44.0/58.8; Python zero-shot 69.7/26.5/38.1; Python one-shot 96.4/62.1/71.7. Free choice: Grok uses z3 in 44% of calls; Claude Sonnet and Opus use brute-force loops in 60% and 54% | He and Wang 2025 (d08); MathConstraint (d06) | [S] K31 |
| Python frameworks beat MiniZinc | DCP-Bench-Open: up to 75% vs 57.3% zero-shot; up to 91% with prompting and inference-time compute | Michailidis 2026 (c31) | [S] K19 |
| Wrong routing is costly both ways | Hard grid on CoT 8.9 vs 62.1 with Python (GPT-4o); EntailmentBank CoT 81.8 vs Prolog 27.4; GSM8K CoT 94.6 vs Prolog 85.8 | He and Wang (d08) | [E] K32 |
| Pipelines fail on fuzzy tasks | Proof of Thought on StrategyQA: 82.4% compiled, precision 58.22%, false-positive rate 53.98% | Ganguly 2024 (b17, d14) | [E] K17 |
| Sound solver, incomplete spec | LINC GPT-4 predicts "Uncertain" 57% vs CoT 41% (label split 24/17/57); FOLIO screen found 39.2% of stories needed rewriting | LINC, FOLIO (b08, b09) | [E] K18 |
| LLM proposes, verifier checks | Lemur: Code2Inv 133 tasks: ESBMC 68, GPT-3.5 103, GPT-4 107; SV-COMP 47: 1 / 14 / 25; average proposals 4.7 (Code2Inv), 7.2 (SV-COMP) | Lemur (a27, b18, c24) | [S] K15 |
| Z3 as planning engine | TravelPlanner final pass 93.9% (test, Claude-3) vs GPT-4 direct 4.4%; no-solver ablation 25.2%; zero-shot four-task optimal rates 72-100% vs 0-4% | Hao 2025 (c21, c22) | [S] K16 |
| Planning vs execution errors | When CoT fails where Z3 succeeds, planning errors are 72.5% (GSM-Sys), 47.5% (CLUTRR), 42.5% (GSM) | SatLM (a15, c03) | [S] K21 |
| Self-consistency stacks on the solver | SatLM + self-consistency: GSM-Sys 69.4 to 80.9; GSM 71.8 to 84.8; LSAT 37.4; BoardgameQA 80.7; CLUTRR 80.1; ProofWriter 99.7 | SatLM (b06) | [S] K22 |
| The solver can be wrong | Fuzz4All found 98 bugs over 9 systems, 64 confirmed new; Z3 14 reported, cvc5 9 | Xia 2024 (c26) | [S] K24 |

## 4. Mechanisms and models

**4.1 Phase transition as a difficulty model.** For random k-SAT, define alpha = clauses / variables. Cost against alpha is an easy-hard-easy bump near the threshold (about 4.3 for k = 3). Below it: plenty of solutions, unit propagation or local search finds one. Above it: many clauses clash, a short refutation exists. At it: neither. An engineer can use this to build test instances of tunable hardness: generate random 3-SAT at alpha = 3.0, 4.3 and 6.0 with the same variable count. It does not predict LLM accuracy, which has not been tested against alpha (section 10). SATBench varies clause count only (d12).

**4.2 CDCL in six steps (what Chaff-style solvers do).**
1. Pick a decision literal by VSIDS (highest decayed conflict count).
2. Propagate unit clauses using two watched literals per clause.
3. If a clause is falsified (conflict), analyse the implication graph, derive a learned clause, backjump.
4. Add the learned clause. Bump counts of its literals. Decay all counts.
5. Restart now and then; keep learned clauses.
6. Stop with SAT (full assignment) or UNSAT (conflict at decision level 0). The UNSAT proof is the chain of learned clauses; an unsat core is the set of original clauses it used.

SMT adds a theory check in step 2: theory solvers (for example linear arithmetic) test the partial assignment and report theory conflicts the same way.

**4.3 The spec-then-solve loop (SatLM and relatives).** An engineer can implement it as follows.
1. Prompt: restate the task, list the unknowns, write constraints in Z3Py. Few-shot examples show declarative style ("say what, not how").
2. Run in a sandbox with a timeout. Capture the result type: SAT with model, UNSAT, unknown/timeout, AMBIGUOUS (more than one value for the query variable), ERROR (parse or runtime).
3. Route by result type (K08):
   - SAT with one value for the query: read the answer.
   - AMBIGUOUS: add the missing constraint, or abstain. SatLM saw AMBIG 15.5% vs UNSAT 3.5% on CLUTRR.
   - UNSAT: the spec has a clash. Get the unsat core, show it to the model, revise the spec (Hao: 78.6% repaired).
   - ERROR: show the error text and reformat. In Logic-LM this raises executability (+5.01 points), accuracy little.
   - Timeout: never read as SAT. It is its own state (a02).
4. Keep best-so-far; stop at 4 to 8 rounds (K28).
5. Verify: plug the model back into the original text constraints with a separate check; require the answer to carry a witness that code checks (K29).

**4.4 Counterexample search with a solver (for S7).** When two candidate rules R1 and R2 both fit all examples, encode "exists x in the input domain with R1(x) != R2(x)" and ask the solver. SAT gives the discriminating input x. UNSAT proves the rules agree on that domain, so pick the shorter one. This needs both rules in a solver-readable form. For simple arithmetic-like rules that works; for general Python programs use random or enumerated testing (section 9). No source in this folder tests this use. It is our extrapolation from the witness pattern (d04) and Lemur's propose-and-verify (a27).

**4.5 Propose-and-verify (Lemur).** The model proposes loop invariants. The SMT-based verifier checks three conditions: the invariant holds on entry, is preserved by the loop body, and implies the post-condition. If a check fails, the counterexample goes back to the model. Averages of 4.7 and 7.2 proposals per solved task. The gain exists because the verifier is sound, so any accepted invariant is right.

**4.6 Where translation fails, and checks that might catch it.** The solver is sound for the formula, not for the problem (K18). Candidate detectors, none tested head to head (K33): (a) plug the returned model into the original text; (b) back-translate the spec to English and compare; (c) translate twice independently and compare solver outputs; (d) vote over many translations (LINC uses 10); (e) list implicit premises the spec lacks and see if adding them changes the answer.

**4.7 Budget model.** Hidden reasoning tokens in o1-class models rise with Z3 conflict count (about 400 tokens per conflict under 20 conflicts, flat above 30; d10). Conflict count or solver time does not predict which individual items a model fails once the set is already hard (r about -0.15; d05). So solver time is a coarse hardness class (easy 0.20 s vs hard 2.52 s median), not an item-level gate.

## 5. What holds up

**Holds (two or more sources).**
- Spec plus solver beats CoT on constraint-heavy tasks and ties on plain arithmetic (K03: SatLM, Logic-LM, Faithful CoT, Logic.py, He and Wang).
- The solver call is the active ingredient; the spec alone adds little (K04: SatLM ablation, LINC scratchpad).
- Translation, not solving, is the bottleneck (K05).
- Self-refinement on error text mostly helps executability (K07).
- Solver result types are useful signals (K08).
- LLMs are weak at UNSAT and at large search spaces (K09, K10); scale alone does not fix it.
- A right answer with a wrong trace is common (K12). This backs G10.
- SAT-bias is a main failure and a checked witness exposes it (K29).
- Fuzzy tasks break the fixed formal pipeline, and wrong routing costs 50+ points either way (K17, K32).
- A sound solver can still be incomplete because the spec drops premises (K18).

**Contested.** Solver pipelines versus CoT with a strong model on human-written logic (K06). Logic-LM GPT-4 FOLIO 78.92 vs CoT 70.58 (+8.3). LINC GPT-4 FOLIO 72.5 vs CoT 75.3 (-2.8, p = 0.58). The same CoT baseline moves by 4.7 points between papers (70.58 vs 75.3). Reasons: different prompts, different FOLIO splits, LINC samples at temperature 0.8 with a 10-way vote. Logic-LM++ (84.80 on FOLIO, 204 test examples) reuses Logic-LM code, so it is not independent. Rule: ignore cross-paper gaps below about 5 points; use paired McNemar tests on one set.

**Failed or weak results.**
- Logic-LM refinement on FOLIO: +0.5. Logic-LM++ slightly hurts GPT-3.5 on FOLIO (62.80 to 62.25 as reported).
- LoRA on 1,100 solver-checked traces: Qwen2.5-14B 51.9 to 53.6 on SATBench (a24). LoGiPT (c27) reports a 13B model at 81.17 on ProofWriter vs Logic-LM GPT-4 79.66, a different setup; we do not train.
- Faithful CoT on StrategyQA stays below CoT; with self-consistency its math gains shrink (GSM8K from 9.0% to 2.6%).
- Compile success is not a quality signal (Proof of Thought).
- The biggest solver wins are on synthetic sets (ProofWriter 98 to 99.7), where translation is easy.
- The "best model 65.0%" headline in SATBench is o4-mini on hard UNSAT, not the best model on UNSAT. Use per-model rows.

**Moderators.**
- Task type: constraint search with little implicit knowledge gains; commonsense loses (d08).
- Model type: the largest tool gain (Sonnet, +52 pp) is for a model run without a thinking budget. Strong thinkers gain less (GPT-5.5, +14 pp) (d01, critique).
- Round budget: 4 vs 8 rounds changes accuracy by up to 37 pp (d03).
- Spec language: Python beats Prolog and MiniZinc; one-shot declarative examples beat zero-shot by large margins (d08).
- Data source: synthetic text translates easily; human-written text translates poorly (FOLIO NL-to-FOL execution accuracy 75.43 on Wikipedia-seeded vs 53.10 on hybrid template stories, b10).
- Framing: text puzzles are harder than the same raw formula (a24).

**Interventions that worked.** Declarative few-shot examples. Unsat-core repair on small planning sets. Error-aware prompts (fixed 60.4% and 73.2% of previously failed SATBench cases; selection-effect caveat). Model proposes, sound solver verifies (Lemur). Abstaining on UNSAT, AMBIG and ERROR (SatLM).

**Interventions that did not.** Spec without a solver. Scratchpad-only variant. Naive retry on error, for accuracy. Scale on hard instances. Fine-tuning on traces (small gain, one source). Majority vote and reward models for ZebraLogic selection (38.0 and 34.8 vs oracle 60.3 to 69.1).

## 6. Language models

**Without tools.** Non-reasoning models fail on large search spaces: GPT-4o 31.7 overall and 0.5 on x-large ZebraLogic; Llama-405B 0.0 on x-large. Reasoning models do much better but still degrade: o1-full 97.2 / 92.1 / 78.0 / 42.5 across size classes, R1 28.5 on x-large, o1-preview 17.0. On SATBench hard UNSAT the average model scores 39.3, below chance (50), because of SAT-bias. o4-mini reaches 65.0, R1 83.6, V3 74.3.

**With a declarative solver.** SatLM (code-davinci-002 era) gained 23 to 26 points on GSM-Sys over CoT and ProgLM (69.4 vs 46.5 and 43.4) and reached 99.7 on ProofWriter. Logic-LM average gain over CoT is 10.44 points (GPT-4) and 18.4 (GPT-3.5) across five sets (c06). CoT itself hurt on AR-LSAT (-3.2%). With GPT-4 the gain on human-written FOLIO is contested.

**Small model plus solver beats large model.** StarCoder+ with LINC 56.0 vs 41.8 CoT on FOLIO. Llama-70B plus Logic.py 91.4 vs o1-preview 71.4 on ZebraLogic.

**What changed it, by how much.**
- CoT to Python spec: GPT-4o hard grids 8.9 to 62.1 (+53).
- Zero-shot to one-shot declarative: Python 38.1 to 71.7; Prolog 28.9 to 58.8.
- Prolog to Python with one-shot: +12.9.
- Adding a sandbox with pysat and z3 for 2026 models: +28 pp mean over 12 models; Opus-4.7 +34.9; Gemini-3.1-Pro +21.2; GPT-5.5 +14.0 (d01).
- Cost: for strong thinkers tools cost about the same tokens or less (GPT-5.5 12,081 vs 10,880 tokens; $0.151 vs $0.282). For weaker or non-thinking models tokens rise sharply (Gemini 5,420 to 23,181; Sonnet 35,046).

**Behaviour with free tool choice.** Models often avoid the solver. Grok called z3 in 44% of calls. Claude Sonnet and Opus used brute-force loops in 60% and 54% (d06). A scaffold that wants a solver has to ask for it.

**Failure modes.**
- SAT-bias: claim "satisfiable" with an invalid assignment. 68.7% of o4-mini's SATBench errors. With tools the claim-vs-verified gap is still 13 to 21 pp for GPT-5.5 and Sonnet (d04).
- Context inconsistency and condition omission (17.0% and 14.3% of o4-mini errors; 44.7% and 12.6% for R1).
- Wrong trace behind a right label (Claude-3.7 SAT: trace 83.2 vs prediction 47.4).
- Syntax and parse errors: 13 to 38% in LINC; Prolog worse than Python.
- Over-use of "Uncertain": LINC GPT-4 57% vs CoT 41%.
- Silent wrong translation: acknowledged by VeriCoT, unmeasured for model-written specs.

**Caveats.** All pre-2025 LLM numbers use GPT-3.5, GPT-4 or code-davinci-002. Only MathConstraint (2026) tests current models with tools, and on a different task (SAT/UNSAT with a witness) than ZebraLogic and SATBench. No study reports equal-token curves. The LLM-Modulo figures (20%, 65%) that earlier notes carried are not in the position paper. What it cites is Blocks World 82% in 15 rounds, Logistics 70%, Mystery BW about 10% (d15). Treat the old figures as unverified.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | For tasks with crisp constraints (puzzles, scheduling, consistency, "is there an input where..."), let the model write a declarative spec and let code run a solver in S4. The solver, not the model, gives the verdict. | S4, O (tool) | [E] | K03, K04; a13, b04, c02, b01, b07, d07, d08 |
| A2 | Do not let the model answer from the spec alone. The solver call must happen; a spec without a run adds almost nothing. | S4, G10 | [E] | K04; c02, a15 |
| A3 | Route on solver result type. SAT gives a witness. UNSAT gives a core to show the model in S5. AMBIGUOUS means add a constraint or abstain. ERROR means show the error text once. TIMEOUT is its own state and is never read as SAT. | S4, S5, S6 | [E] | K08; b05, b25, c23, a02 |
| A4 | Require a witness. Any SAT claim must carry an assignment, and code plugs it back into the original constraints. Never accept "satisfiable" from prose. | G2, G10 (new wording), S8 | [E] | K29, K12; d04, d11, a23 |
| A5 | Log parse-and-run rate. Allow one repair on error text, but judge by accuracy, not executability. Keep the better of old and new spec. | S5 | [E] | K05, K07; b02, b03, b11 |
| A6 | Use the solver path only for crisp-constraint tasks. Send fuzzy or commonsense items to plain reasoning. Compile success is not a gate. | S0 | [E] for the cost of mis-routing; the gate itself is untested | K17, K32; d08, b17, d14 |
| A7 | A verdict is sound for the spec only. Add a check for dropped premises before accepting an UNSAT or "uncertain" result on human-written text. | S8, G | [E] on the problem, [S] on the fix | K18; b08, b09, c10 |
| A8 | Prefer Python-embedded declarative tools (Z3Py or CP-SAT through Python) over a separate modelling language or Prolog. | O (tool) | [S] on Z3Py specifically; direction Python over Prolog has two sources | K19, K31; d08, c31 |
| A9 | Cap spec-run-debug rounds at about 4 to 8, keep best-so-far, and submit a fallback answer when rounds end (G6). | S5, G6, G7 | [S] | K28; d03 |
| A10 | Never treat a model's "UNSAT" or "no solution" as proof without a solver. Hard UNSAT is where models are below chance. | G10 | [E] | K09; a21, a22, c14 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code checker as selector: filter N samples with a checker instead of voting. | S7 | [S] | K11; b13, d09 |
| T2 | Solver counterexample search in S7 when two rules still fit. | S7 | extrapolation, no direct source | a27, d04 |
| T3 | Solver tool with thinking models at equal tokens. | S4 | [S] | K26, K27; d01, d02 |
| T4 | Detectors for silent wrong formalisation: round trip, double translation, plug-in, premise listing. | G, S8 | [S] | K18, K33; d12, d13 |
| T5 | Three-question crispness gate. | S0 | [S] | K32; d08, d14 |
| T6 | Error-aware prompt against SAT-bias. | G | [S] | K29; a24, d11 |
| T7 | Z3Py vs CP-SAT vs brute force. | O (tool) | [S] | K31; d06, d08 |
| T8 | Unsat core in the repair step vs generic retry. | S5 | [S] | K08; c23 |
| T9 | Solver-time class as a coarse budget class (not an item gate). | G12 | [S], partly negative | K13, K30; d05, d10 |
| T10 | Propose-and-verify with a sound checker, counting proposals per solved item. | S3, S4 | [S] | K15; a27 |
| T11 | Solver plus 5-way vote. | S7 | [S] | K22; b06 |
| T12 | Step-level SMT checking of the trace. | S4 | [S] | K25; b19 |

## 8. Concrete tests on our bench

All arms get the same total token budget. Spec writing, retries and solver output reading count. Report accuracy, tokens per item and cost per correct answer. Use paired McNemar on identical items. Use at least 100 items per arm for any claim under 10 points.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T3 | 60 hard puzzles: ZebraLogic large and x-large, SATBench hard UNSAT | (a) thinking only; (b) spec + solver tool; (c) thinking + free tool | Accuracy, verified-witness accuracy, tokens | (b) beats (a) by 15+ points on x-large and UNSAT for a mid-size model; smaller for a strong thinker (MathConstraint +14 to +35) |
| A1/A2 ablation | 100 constraint puzzles + 100 plain word problems | CoT; Python imperative; Z3 spec + run; Z3 spec, no run | Accuracy | Z3 run wins on puzzles; ties on word problems; no-run arm near CoT (K04) |
| T1 | 100 puzzles where clues are cheap to code, or SAT items with a witness | Majority of N; N filtered by code checker; N + plain model verification | Accuracy at equal tokens | Checker arm recovers most of the 22 to 31 point oracle gap (60.3 to 69.1 vs 38.0) |
| T4 | 20 problems with one seeded dropped constraint, 20 clean | No check; plug-in; round trip; second translation; premise list | Detection rate and false-alarm rate | At least one check catches 60% of seeded drops with under 10% false alarms |
| T5 | 40 mixed items (20 crisp, 20 fuzzy) | Always solver; always think; 3-question gate | Accuracy | Gate within 3 points of the better arm per type; always-solver loses 50+ on fuzzy items (K32) |
| T6 | 60 SAT/UNSAT items | Plain; error-aware reminder; witness required; both | SAT-bias rate | Reminder cuts bias errors by a third or more; witness requirement cuts unverified SAT claims |
| T7 | 20 puzzles per language | Z3Py; CP-SAT; brute-force loop | Executable rate, accuracy | Z3Py or CP-SAT above brute force on large grids; brute force wins on tiny ones |
| T8 | 40 items that return UNSAT from the first spec | Retry with error; retry with unsat core; core plus original text | Repair rate within 2 rounds | Core arm beats generic retry by 10+ points |
| T2 | 30 ARC-like rule pairs that fit all examples | Random inputs; enumerated inputs; solver "A != B" | Discriminating input found per call | Solver finds a discriminating input where random testing misses it on rules with narrow differences |
| T9 | 100 puzzles with solver time known | Fixed budget; budget set by solver-time class | Accuracy per token | Small gain at best; drop if under 3 points |
| Rounds | 60 hard items | 4 vs 8 rounds, with and without forced submit | Accuracy | 4 rounds costs up to 37 points; forced submit rescues part |
| T10 | 40 verification-style tasks | Model-only; verifier-only; propose and verify | Solved count; proposals per solved | Propose-and-verify beats both; 4 to 8 proposals per task |

## 9. What does not transfer, and why

- **The phase-transition constant.** 4.3 is for uniform random 3-SAT. Real tasks are structured. It tells us how to build tunable test sets, not how hard an agent item is (K01; no LLM-accuracy-vs-ratio test exists).
- **Chaff speed-ups.** They matter to solver users, not to the agent. Solver time is small next to model tokens (K02, [S]).
- **NeuroSAT and learned solvers.** Not competitive with real solvers (K14).
- **LoGiPT-style imitation of solvers and LoRA on traces.** Needs training (K23).
- **Fuzzy and open tasks.** Strategy, commonsense, open creative work, perception-heavy ARC. The formal pipeline loses 50+ points there (K17, K32). Open mode (NoveltyBench) has no constraint set to satisfy.
- **ARC rules as SAT.** Rules written as general Python programs are not solver-readable, and program equivalence is undecidable. For those use generated test inputs, not SMT (section 4.4).
- **Synthetic gains.** ProofWriter at 98 to 99.7 comes from short templated sentences. Gains shrink on human-written text (K06).
- **Soundness.** "Sound" means sound for the spec, not for the user's problem (K18).
- **Small planning tables.** Hao's repair table has 12 queries; too small to design on (K08).
- **The biggest tool gains.** Sonnet without thinking +52 pp is not a prediction for a thinking model (critique).

## 10. Open questions

1. Do solver gains hold for current reasoning models on ZebraLogic x-large and SATBench hard UNSAT at equal total tokens? MathConstraint is partial and a different task.
2. What is the full cost of spec-then-solve (spec tokens, retries, output reading) against extended thinking on the same items? No equal-budget curve exists.
3. How often does a silently wrong formalisation pass, and which cheap check catches it?
4. Is there a reliable crispness gate? No gate with measured accuracy was found. Compile success is not usable.
5. What is the best use of solver output: unsat core to revise the spec, extra models to add constraints, or the model as the answer?
6. Can a code checker close the best-of-N oracle gap? ZebraLogic's oracle used gold answers.
7. Which constraint language works best in 2025-26: Z3Py, CPMpy, OR-Tools, MiniZinc, raw SMT-LIB?
8. Does requiring a checked witness remove SAT-bias? MathConstraint shows a 13 to 21 pp gap persists with tools; no clean A/B exists.
9. Does LLM accuracy track the clause-to-variable ratio around 4.3? Untested.
10. Is solver conflict count or time a useful per-item budget probe? Early data say no (r about -0.15).
11. Does the 4.7-point CoT baseline spread between papers hide real effects of the pipeline on FOLIO?
12. Does a solver help counterexample finding for rule selection in ARC-like tasks? No source tests it.

## 11. Sources

[V] opened (full text read by a researcher this run); [M] snippet only.

- [V] Mitchell, Selman, Levesque (1992) Hard and easy distributions of SAT problems. https://cdn.aaai.org/AAAI/1992/AAAI92-071.pdf (a01-a03, c33)
- [V] Monasson, Zecchina, Kirkpatrick, Selman, Troyansky (1999) 2+p-SAT: typical-case complexity. https://arxiv.org/abs/cond-mat/9910080 (a04, a05)
- [V] Ding, Sly, Sun (2021) Proof of the satisfiability conjecture for large k. https://arxiv.org/abs/1411.0650 (a06)
- [V] Moskewicz, Madigan, Zhao, Zhang, Malik (2001) Chaff. https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf (a07, a08; not re-checked in the critique pass)
- [V] de Moura, Bjorner (2008) Z3: an efficient SMT solver. https://link.springer.com/content/pdf/10.1007/978-3-540-78800-3_24.pdf (a09, a10; not re-checked; c32 is snippet only, [M])
- [V] Selsam, Lamm, Bunz, Liang, de Moura, Dill (2019) Learning a SAT solver from single-bit supervision. https://arxiv.org/abs/1802.03685 (a11, a12, b20)
- [V] Ye, Chen, Dillig, Durrett (2023) SatLM. https://arxiv.org/abs/2305.09656 (a13-a16, b04-b06, b25, c01-c04)
- [V] Pan, Albalak, Wang, Wang (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (a17, a18, b01-b03, c05-c07)
- [V] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 (a19, a20, b07, b08, b23, c08-c12)
- [V] Wei et al. (2025) SATBench. https://arxiv.org/abs/2505.14615 (a21-a24, b14, b15, b24, c13-c17, d11, d12)
- [V] Lin et al. (2025) ZebraLogic. https://arxiv.org/abs/2502.01100 (a25, a26, b12, b13, c18-c20, d09, d10)
- [V] Wu, Barrett, Narodytska (2024) Lemur. https://arxiv.org/abs/2310.04870 (a27, b18, c24)
- [V] Kirtania, Gupta, Radhakrishna (2024) Logic-LM++. https://arxiv.org/abs/2407.02514 (a28, b11, c28)
- [V] Han et al. (2022, rev. 2024) FOLIO. https://arxiv.org/abs/2209.00840 (b09, b10; not re-checked)
- [V] Lyu et al. (2023) Faithful chain-of-thought reasoning. https://arxiv.org/abs/2301.13379 (b16, c25; not re-checked)
- [V] Ganguly et al. (2024) Proof of Thought. https://arxiv.org/abs/2409.17270 (b17, c29, d14)
- [V] Feng et al. (2025) VeriCoT. https://arxiv.org/abs/2511.04662 (b19, d13; table values loosely extracted, not relied on)
- [V] Kambhampati et al. (2024) LLMs can't plan, but can help planning in LLM-Modulo frameworks. https://arxiv.org/abs/2402.01817 (b21, d15)
- [V] Dziri et al. (2023) Faith and fate. https://arxiv.org/abs/2305.18654 (b22; context only)
- [V] Hao, Chen, Zhang, Fan (2025) Large language models can solve real-world planning rigorously with formal verification tools. https://arxiv.org/abs/2404.11891 (c21-c23)
- [V] Xia et al. (2024) Fuzz4All. https://arxiv.org/abs/2308.04748 (c26; not re-checked)
- [V] Feng et al. (2023) LoGiPT, Language models can be logical solvers. https://arxiv.org/abs/2311.06158 (c27; not re-checked)
- [V] Arakelyan et al. (2025) FLARE. https://arxiv.org/abs/2410.11900 (c30)
- [V] Michailidis, Tsouros, Guns (2026) DCP-Bench-Open. https://arxiv.org/abs/2506.06052 (c31; arXiv id is 2506, journal version 2026)
- [V] Pati, Li, Jha, Garg, Sejpal, Ganesh (2026) MathConstraint. https://arxiv.org/abs/2605.08498 (d01-d06)
- [V] Kesseli, O'Hearn, Cabral (2025) Logic.py. https://arxiv.org/abs/2502.15776 (d07)
- [V] He and Wang (2025) When do symbolic solvers enhance reasoning in LLMs? https://arxiv.org/abs/2512.03272 (d08)
- [M] LLM-Modulo figures as cited inside Hao et al. (c34): not read at source; superseded by d15.
