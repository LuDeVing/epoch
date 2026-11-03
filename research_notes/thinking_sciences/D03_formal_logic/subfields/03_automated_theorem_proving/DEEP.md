# Automated theorem proving: deep document

*Subfield D03.03. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K22), critique.md in this folder. Ids like a14 or d05 point to evidence lines. Where critique.md corrected an evidence line, the correction is used here (see section 5, "Corrections").*

## 1. What it is

Automated theorem proving (ATP) is the search for proofs by machine. A program gets a statement and must produce a proof that a checker accepts. Two eras matter.

- **Classic ATP (1954-2015).** Decision procedures, heuristic search, resolution and saturation provers (Vampire, E, Prover9, Waldmeister). Everything is symbolic. Soundness is guaranteed by the calculus.
- **Neural ATP (2020-2026).** A language model proposes proof steps or whole proofs. A proof assistant kernel (Lean, Isabelle, Coq, Metamath) accepts or rejects. Search or sampling wraps the model. Since 2025, general frontier models in agent loops have joined (Hilbert, Aleph, Theo).

The one feature that makes this field useful to us: **the checker is exact.** A kernel never says "looks right". It says accepted or rejected, and it gives error text. Every reported number in this field is believable only because of that (K01). Our agent rarely has a Lean kernel. But the pattern, "model proposes, program checks, error text drives repair, decomposition at impasses, stop by budget", maps onto the schema directly: S4 TEST, S5 REVISE, S6 IMPASSE, S8 VERIFY, G2, G3, G12.

Why it matters for the schema: (1) it shows what a hard verifier buys, with measured numbers; (2) it gives the best-measured case of decomposition into subgoals (O3) with a library of solved lemmas; (3) it shows where the exact-check route breaks: translation from text to formal language (S2).

Scope note. Closely related subfields run in parallel (SAT solving/DPLL, Resolution and saturation, Monte Carlo tree search, Chain-of-thought prompting, Learned refinement and self-verification). This document only notes links to them.

## 2. History and theories in depth

### 2.1 Founding era (1954-1965). Status: mostly [M] snippet only

- **Davis 1954.** First program to prove a theorem: a decision procedure for Presburger arithmetic on JOHNNIAC. Example: sum of two even numbers is even (a02, secondary page). Lesson: decidable fragments are solved exactly by code. Route them to a solver.
- **Newell, Shaw, Simon 1956, Logic Theorist.** Heuristic search over proofs in Principia Mathematica propositional logic, written in IPL. Proved 38 of the first 52 theorems in chapter 2. Found a shorter proof of theorem 2.85 than Russell and Whitehead. A journal refused the new proof as not notable (a01, secondary). Lesson: proof search is guided search, with rules of thumb. This is the ancestor of means-ends analysis and of our O3/O5.
- **Gilmore 1960 and Davis-Putnam 1960.** Generate ground instances, then test propositional unsatisfiability. This blows up combinatorially (a04, secondary).
- **Robinson 1965, resolution.** One inference rule plus unification, on clauses in Skolemised conjunctive normal form. Sound and refutation-complete: a clause set is unsatisfiable exactly when the empty clause is derivable. Unification removes the need to list ground instances (a03, b19; neither opened). Pure resolution still explodes, so later work added orderings, literal selection, indexing and strategies.

### 2.2 Saturation provers and competitions (1970s-2020s)

- First-order logic is semi-decidable: valid formulas can be enumerated, invalid ones are not always recognised. Propositional validity is co-NP-complete (a06).
- **CASC** (CADE ATP System Competition) ranks first-order provers on the TPTP library every year. Vampire has won the first-order-formula division regularly since 2001. Waldmeister won the unit-equality division 14 years in a row (1997-2010) (a06, opened but secondary).
- **Robbins conjecture.** EQP (McCune, Argonne) proved in a run of eight days that Robbins algebras are Boolean algebras, an open question since the 1930s. Reported 10 Dec 1996, paper 1997. Winker's earlier work gave the setup, so human insight was in the loop. Dahn (1998) simplified the machine proof (a05).
- No CASC solve counts were captured (b20 page too large). Claim K15 stays single-source.

### 2.3 Neural proof search (2020-2023)

- **GPT-f (Polu and Sutskever 2020).** Transformer proposes Metamath steps. Best-first search by log-probability, plus a value function trained on its own generated statements. Some proofs were accepted into the Metamath library (c01).
- **HyperTree Proof Search (Lample et al. 2022).** AlphaZero-style search over hypertrees: a goal splits into subgoals that must all be solved. Critic plus online training on unproved theorems (a08).
- **Hammer integration.** Thor (2022) lets the model call Sledgehammer (symbolic premise selection plus ATP/SMT) at chosen steps. Magnushammer (2023) replaces hand-built premise selection with a contrastive retriever.
- **Retrieval.** LeanDojo (2023): open Lean toolkit, 98,734-theorem benchmark, ReProver (retrieval-augmented tactic generator).
- **Whole-proof generation.** Baldur (2023): generate the entire proof, then repair from the proof-assistant error. It beat step-wise search.
- **Informal to formal.** Draft, Sketch, Prove (DSP, 2022/23): informal proof, formal sketch with gaps, automated prover closes gaps.
- **In-context agents.** COPRA (GPT-4 as one-tactic-at-a-time agent with backtracking, no training).

### 2.4 Reasoning-model era (2024-2026)

- **RL from proof-assistant feedback.** DeepSeek-Prover-V1.5 (RL plus RMaxTS tree search), Kimina-Prover (long reasoning inside the proof), DeepSeek-Prover-V2 (subgoal decomposition by DeepSeek-V3, small prover fills, stitched into RL cold-start data), Goedel-Prover(-V2) (expert iteration on 1.64M autoformalised statements, verifier-guided self-correction).
- **Lemma-style heavy systems.** Seed-Prover (ByteDance, 2025): refines from Lean feedback, proved lemmas, self-summaries; IMO 2025 4/6 in time, 5/6 after.
- **Agents on general models, no training.** Hilbert (reasoner + prover + verifier + retriever, recursive decomposition), Aleph (GPT-5.2 agentic), Theo (Claude Opus 4.7 in a Claude Code loop with Lean REPL).
- **Geometry.** AlphaGeometry 2: symbolic engine plus Gemini proposing constructions.
- **Benchmarks.** miniF2F (488 problems; a09) went from 1.3% (GPT-f Metamath pass@1) to 99.6% (Seed-Prover). PutnamBench (640-672 problems; a15) went from 1 of 640 (GPT-4) to 462/660 (Hilbert) and 668/672 (Aleph). The field's main lesson on measurement: saturation and statement errors make old numbers hard to compare (K09).

### 2.5 Theories of why it works

1. **Hard verifier turns generation into search.** With a pass/fail signal, quantity of tries converts into correctness. The cost is tokens (K02, K03).
2. **Decomposition shrinks the horizon.** A sketch with gaps turns one long proof into many short ones that a weak prover or a hammer can close (K07).
3. **Symbolic and neural parts cover different errors.** Thor: 8.2% of problems solved by neither part alone (K04).
4. **Memory of what is already proved.** Premise and proof retrieval, lemma libraries. Works in-distribution, weaker on novel premises (K05).
5. **Translation is the weak link.** Everything above assumes a correct formal statement. Where text must be turned into logic, errors enter silently (K10, K11, K16, K21).

## 3. Core findings with exact numbers

Status: E established (2+ independent sources), S single-source, C contested. Opened status is in section 11.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| First transformer prover with exact checker beat the prior Metamath best | 56.22% vs 21.16% (MetaGen-IL); policy+value 700m 44.59/47.21 vs policy only 42.56 | GPT-f (a07, c01, c02) | E |
| Model size and text pretraining help | 160m 28.96% scratch to 34.79% pretrained; 700m 31.58% to 42.56% | GPT-f (c01) | S |
| More search raises pass rate | GPT-f +9.2 points from more search; DeepSeek-V2-671B 82.4% (pass@32) to 88.9% (pass@8192, 217/244) | a07, a19 | E (K02) |
| Last gain is very costly | 6.5 points cost 256x more samples; CoT mode 6751.9 vs 761.8 tokens per proof (about 9x) | DeepSeek-V2 (a19, b24, c12) | E (K03) |
| Kimina-Prover Preview 72B across budgets | 52.94% pass@1, 65.16% pass@8, 68.85% pass@32, 77.87% pass@1024, 80.74% pass@8192 | Kimina (a18, b13) | S |
| Generator + symbolic tool beats either alone | PISA: LM 39.0%, Sledgehammer 25.7%, union 48.8%, Thor 57.0%; 8.2% solved only by hybrid | Thor (a11, b04) | E (K04) |
| Learned premise selection beats hand-built | PISA 59.5% vs 38.3%; miniF2F 34.0% vs 20.9%; with LM prover PISA 57.0% to 71.0% | Magnushammer (a12, b05) | E |
| Retrieval helps, mostly in-distribution | LeanDojo random split: ReProver 51.2%, no retrieval 47.6%, GPT-4 29.0%. novel_premises: 26.3 / 23.2 / 7.4 | LeanDojo (a10, b06, c07) | E (K05) |
| Benchmark checker errors | earlier lean-gym misjudged 21.1% of correct proofs as wrong; LeanDojo 1.4% | LeanDojo (b06, c07) | S |
| Unseen-project drop is small with in-project retrieval | Rango (Coq) 160/500 (32.0%) unseen projects vs 184/500 (36.8%) file-wise; without retrieval 89 vs 127 | Rango (d10, d11) | S |
| Proof retrieval beats lemma retrieval | Rango ablation (500 thm): full 150, no lemmas 145, no proofs 102, no retrieval 93; +47% from proof retriever | Rango (d10) | S |
| Whole-proof beats step search at small scale | Baldur 47.9% vs 39.0% (6,336 Isabelle theorems); 40.7% at 64 samples (8b) | Baldur (a13, b07, c08) | C (K14) |
| Repair from error text: small gain | Baldur +1.5% at equal compute; Goedel-V2-32B 88.1% to 90.4% (2 rounds, 40,000-token budget) | a13, b07, b14, c14 | E (K06) |
| Tree search adds little over sampling | DeepSeek-V1.5 60.2% whole-proof vs 63.5% with RMaxTS; at 3200 samples V1.5-RL 54.9% vs 54.5% for a tree-search system; RMaxTS under 0.2% over naive retry at 3200 samples (ProofAug) | a16, c27, d04 | C (K14) |
| Informal sketch + formal subgoals | miniF2F-test: Sledgehammer 10.4%, +heuristics 20.9%, Thor 29.9%, Thor+EI 35.2%, DSP 39.3% (human proof) / 37.7% (Minerva 62B) / 38.9% (540B); 200 of 488 | DSP (a14, b03, c04, c24) | E (K07) |
| DSP ablations | no automated prover -9.8 (valid); no informal proof -3.7; no in-line comments -4.9 (valid), -2.8 (test) | DSP (b03, c05) | S |
| Informal drafts are often wrong but still help | 29 of 50 informal proofs correct (58%) | DSP (a14) | S |
| Recursive decomposition (Hilbert) | miniF2F 99.2% (Gemini 2.5 Pro + Goedel-32B) vs 49.1% for Gemini alone at pass@16384; prover only (pass@4) 75%; 98.36% at depth 2; DeepSeek-V2-7B non-CoT +35.4 to 96.7% | Hilbert (b18, c19, d13) | E (K07) |
| Reasoner quality dominates | PutnamBench Hilbert 462/660 (70.0%) with Gemini 2.5 Pro vs 88/660 (13.3%) with gpt-oss-120b | Hilbert (b18) | E (K08) |
| Retrieval cuts tokens and raises accuracy | 99.2% vs 97.9%; reasoner tokens 2.3M vs 4.0M (about 43% fewer); calls 548 vs 862. DeepSeek-7B: 98.4% vs 97.1%, tokens 1.9M vs 2.1M | Hilbert (b18, d14) | S |
| In-context agent without training | COPRA miniF2F-test: few-shot GPT-4 13.52%; COPRA 26.63% (60 queries); +retrieval 29.09%; no backtracking 24.59%; ReProver 25.00% | COPRA (c09) | S |
| Small prover with better data beats huge | Goedel-V2-8B 84.6% pass@32 vs DeepSeek-V2-671B 82.4%; 32B 88.1% | Goedel-V2 (b14, c14) | S (K13) |
| Benchmark saturation | miniF2F-test 29.9% (Thor 2022) to 99.6% (Seed 2025); PutnamBench 1 (GPT-4) to 7 (Goedel SFT) to 47 (DeepSeek-V2) to 86 (Goedel-V2) to 331/657 (Seed) to 462/660 (Hilbert) | a25, b21 | E (K09) |
| Heavy system, IMO-level | Seed-Prover: past IMO 121/155 (78.1%); PutnamBench light 201/657, medium 331/657; CombiBench 30.0% vs 10.0%; MiniCTX-v2 81.8% vs 44.3%; IMO 2025 4/6 then 5/6 | Seed-Prover (a20, c20) | S |
| Uneven by subject | IMO easy 47/55, medium 47/56, hard 27/44; algebra 72/85, number theory 42/55, combinatorics 7/14 | Seed (c26) | S |
| Geometry neuro-symbolic | IMO-AG-50: AG2 42, AG1 27, DDAR alone 16, gold medallist average 40.9; o1 0, Gemini thinking 0; Seed-Geometry 43 | AG2 (a21, b15) | S |
| Training-free frontier agents on PutnamBench | Aleph (GPT-5.2) 637/672 at $54 (pass@2), 668/672 at $68 (pass@3); Theo (Claude Opus 4.7) 32/32 random items; Seed-Prover 1.5 581/672; DeepSeek-V2-671B 47/672 | Theo (d05, d06) | S (K18) |
| Cost per verified proof | Theo about $5 (subscription) to $29 (API list); Hilbert about $39 (24.4M tokens per solved); Aleph $54-68; Seed 1.5 about $168; DeepSeek-V2-671B $18.30 at pass@1024 | d05, d06, d08 | S (K19) |
| Learned stop/restart router | 28.9% cost cut at parity accuracy (or +7.9% accuracy at parity cost); oracle 62.0%; 8B prover with decomposition plus lemma attempts 23 to 48 of 85 | Rognvaldsson et al. (d07) | S (K20) |
| Text-to-logic solver route on shallow tasks | Logic-LM +18.4 over CoT (GPT-3.5), +10.44 (GPT-4); GPT-4 FOLIO 69.11 / 70.58 / 78.92 (standard / CoT / Logic-LM); LINC ProofWriter 98.3% (GPT-4), 96.4% (GPT-3.5) | a22, a23, b10 | E (K10) |
| ...but not uniformly | LINC GPT-4 FOLIO 72.5% vs CoT 75.3%, McNemar p=0.58; StarCoder+ 56.0% vs 41.8% | LINC (a22, b11) | E (K10) |
| Syntax errors in translation | FOL syntax errors 38% StarCoder+, 24% GPT-3.5, 13% GPT-4 | LINC (a22) | S |
| Translation is weak on hard sets | Executable rate GPT-4: FOLIO 79.9% (85.8% after refinement), AR-LSAT 32.6% (39.8%) | Logic-LM (b10, c22) | E (K11) |
| Solver helps on constraints, not on plain arithmetic | SATLM GSM-SYS 69.4 vs program-aided 43.4 vs CoT 46.5; ALGEBRA 77.5 vs 52.3; LSAT 35.0 vs 23.5; ProofWriter 99.7; plain GSM 71.8 vs 72.7 | SATLM (c23, d15) | E (K10) |
| Solver turns errors into refusals | GSM-SYS incorrect 20.6% vs 52.5% (program-aided); selective prediction 77% vs 45% accuracy at equal coverage | SATLM (c23, d16) | S |
| Autoformalisation is lossy | 25.3% of problems perfectly translated; proof rate 29.6% to 35.2% with autoformalised data | Wu et al. (c06) | E (K16) |
| Whole pipeline far below parts | best informal-to-formal-to-proof pipeline about 36% vs 97% (autoformalisation alone) and 69-71% (prover alone); on corrected miniF2F-v2 70% vs 40% on original; discrepancies in more than half of problems | miniF2F-v2 (d01, d03) | S (K16) |
| LLM judge overstates fidelity | Herald @128: LLM judge 97% faithful, human Lean experts 66% | miniF2F-v2 (d02) | S (K21) |
| Neural clause selection in saturation prover | Vampire: Mizar40 test 1543 to 3101 of 5000 (+101%); Isabelle +24.7%; CoqHammer +93.5%; cross-benchmark models score below default; joint model recovers 95-101% | Chvalovsky et al. (d09) | S (K22) |
| Suggest-then-verify tool | Lean Copilot automates 74.2% of steps (search) vs 58.4% (suggest) vs 40.1% (Aesop); 2.08 vs 3.86 manual tactics | Lean Copilot (b17, c17) | E (K17) |
| Formal vs informal | AIME 24-25 (15 problems): DeepSeek-V2 formal 6 vs 8 for DeepSeek-V3 informal majority vote | DeepSeek-V2 (a19) | C (K12) |
| Lifelong learning | LeanAgent 155 sorry theorems in 23 repositories; Formal Book 72.4% vs 20.9% ReProver; several repositories 0-7% | d12 | S |
| Self-correction needs diversity | Goedel-V2: pass@1 rose while pass@N fell in late training until model averaging | c14 | S |
| Early PutnamBench | Lean: GPT-4 1/640, COPRA 1, ReProver 0; Isabelle: DSP 4, Sledgehammer 3, GPT-4 1; Coq: GPT-4 1/412, others 0 | a15, c10 | E |

## 4. Mechanisms and models

Each mechanism is written so an engineer could build a version without a Lean kernel, by swapping the kernel for the best exact check available (unit tests, a solver, a calculator, a held-out example).

### 4.1 The propose-check-repair loop (core)

```
context = task
for attempt in 1..N:
    candidate = model(task, context)      # fresh context per attempt (S3)
    ok, err = checker(candidate)          # exact; program, not model
    if ok: return candidate
    context = err (located, verbatim)     # S5, G2
return best-so-far                        # G6
```

Facts that shape it:
- Pass rate climbs with N, then flattens (K02, K03). Log accuracy vs tokens, find the knee.
- A repair round that shows the real error text adds a small amount: about 1.5 points (Baldur, at equal compute) and about 2 points (Goedel-V2, 88.1 to 90.4%). Baldur reports that the error message was crucial. So repair is worth one or two rounds, not more (S5 already says at most 2).
- Goedel-V2 saw pass@1 improve while pass@N fell late in training; diversity matters for sampling. Lesson for us: do not make attempts more alike (G4, S3 fresh contexts).
- Many cheap samples versus few long ones: DeepSeek CoT mode costs 9x tokens (6751.9 vs 761.8). Goedel-8B at pass@32 beats DeepSeek-671B at pass@32 on miniF2F. Token-matched comparisons are missing (critique, GAPS 6).

### 4.2 Draft, sketch, fill (decompose with gaps)

1. Model writes an informal plan.
2. Model turns it into a formal skeleton where each step is a statement with a hole.
3. A cheap exact tool (Sledgehammer in DSP; the small prover in Hilbert/DeepSeek-V2) tries each hole.
4. Holes that fail go back to the reasoner. It splits them again (Hilbert: recursion to depth 2-3).

Numbers: DSP roughly doubles the baseline (20.9% to 39.3%). The informal draft can be wrong (58% correct in the hand check) and the sketch still works. Dropping the automated filler costs 9.8 points. Which model writes the draft mattered little in DSP (37.7% at 62B, 38.9% at 540B on test) and a lot in Hilbert (13.3% vs 70.0% with two different reasoners). A likely reading: the gap-filling tool matters for easy leaves, the planner for hard structure.

Implementation for our agent (O3 + subgoal): the program, not the model, owns the tree. It holds a list of open subgoals, calls the checker per leaf, and recurses only on failures. Depth cap 2 matches Hilbert (98.36% at depth 2, 98.7% at depth 3) and the schema's depth-2 rule.

### 4.3 Lemma and premise library (memory)

- Hilbert's retriever supplies known lemmas to the reasoner. Result: 99.2% vs 97.9% and about 43% fewer reasoner tokens (single run, no confidence intervals).
- Rango retrieves similar proofs and lemmas from the same project at every step. Proof retrieval matters far more than lemma retrieval (+47% vs about +3%).
- Magnushammer trains a contrastive retriever; it beats Sledgehammer with 0.1% of the data.
- Boundary: LeanDojo's novel_premises split halves the score (51.2% to 26.3%). Retrieval learned on one distribution transfers badly (Vampire neural guidance goes below default off-distribution).

Implementation: keep solved subgoals as (statement, working proof, class). On a new item, retrieve by problem class and by similarity of the failing step. Prefer retrieving full solved examples over bare lemma names. Treat any hit as a hint; the checker decides.

### 4.4 Tool call with exact symbolic helper

Thor: the model chooses when to call the hammer. Premise-selection steps advanced the proof only 1.9% of the time, steps without premises 28.2%, yet the union with the hammer solved 8.2% extra. So the helper is a rare but decisive rescue. Implementation: put solvers (SAT/SMT, CAS, calculator, unit-test runner) in a tool slot. Call them at S4/S5 when a step is exact-checkable.

### 4.5 Translate-to-solver (S2 formalise)

LLM translates text to first-order logic or constraints; Prover9 or SAT/SMT decides (LINC, Logic-LM, SATLM). Logic-LM adds a self-refinement loop driven by solver errors, and falls back to CoT when the logic cannot run. SATLM can abstain on UNSAT or ambiguous specs, which cuts wrong answers (GSM-SYS incorrect 20.6% vs 52.5%).

Where it fails: implicit facts (e.g. "Harry is a person"), syntax (one symbol used with two arities), low executable rate on hard text (AR-LSAT 32.6%). A sound prover on a lossy translation is only as good as the translation. On miniF2F-v2, statements were simplified or wrong in over half of problems.

Implementation: fail closed. If the formal form does not parse, route to the informal path, and count how often (cost of the route). Do not trust model-judged round-trip (97% LLM vs 66% human).

### 4.6 Stop and restart rule

Rognvaldsson et al.: a router sees the failed attempts and decides continue or restart with a new decomposition. Features that worked: proof similarity and error diversity (28.9% cost cut at parity) beat attempt count only (19.7%). Oracle with perfect knowledge of difficulty: 62.0%. Single workshop paper, 85 problems, 8B prover. Implementation: S6 fires on "same error twice" (already in the schema). The test is whether error diversity is a better trigger than a count.

### 4.7 Search over sampling

HTPS (AlphaZero-style), RMaxTS (intrinsic-reward MCTS) and best-first search with a value function. Evidence says the extra gain over plain retry is small once samples are matched: +3.3 points for V1.5 (60.2 to 63.5%), under 0.2% at 3200 samples in ProofAug. A learned value function added a few points in GPT-f (42.56 to 44.59/47.21). This links to the parallel subfields "Monte Carlo tree search" and "MCTS limits".

### 4.8 Classic saturation (for completeness)

Given-clause loop: pick a clause, resolve it with all processed clauses, add results, simplify (subsumption, demodulation), repeat until the empty clause appears. Strategy portfolios and clause-selection heuristics decide speed. In Vampire, neural clause selection gives +27.6% on TPTP (train only) and +101% on Mizar40 test, but only within the training family (d09). This links to the parallel subfields "Resolution and saturation" and "SAT solving, DPLL".

## 5. What holds up

### What replicated or has several sources
- Exact checker is the base of every result (K01, 4 sources).
- More samples raise the solve rate; returns diminish at high cost (K02, K03).
- Generator plus symbolic tool beats either alone (Thor, Magnushammer, Lean Copilot; K04, K17).
- Decomposition helps (DSP, DeepSeek-V2, Hilbert; K07). Three separate groups, different systems.
- Repair from real error text helps by a small, consistent amount (K06).
- Text-to-solver translation helps on shallow, synthetic logic and constraint tasks (K10).
- Benchmark saturation and cross-era incomparability (K09).

### Failures, nulls and boundary conditions
1. **Whole pipeline vs parts.** Informal-to-formal-to-proof gave about 36% where the parts reported 97% and 69-71% alone (d01). Reason: simplified or wrong formal statements in over half the problems.
2. **Tree search vs naive retry.** Under 0.2% difference at 3200 samples (d04). Sample-matched, not token-matched.
3. **LINC with GPT-4 on FOLIO.** 72.5% vs CoT 75.3%, p=0.58: no benefit at the top model (a22, b11). Gains were large for StarCoder+ (56.0 vs 41.8).
4. **Plain arithmetic (GSM).** Solver route 71.8 vs program-aided 72.7. No gain where the problem has no constraint structure (d15).
5. **Learned guidance off-distribution.** Vampire neural clause selection falls below default on other families (d09).
6. **Novel premises.** LeanDojo drops from 51.2% to 26.3%. Rango loses only about 5 points with in-project proof retrieval, so the loss depends on what is retrievable (d11).
7. **Formal behind informal on some items.** AIME 24-25: 6 formal vs 8 informal majority vote (15 problems, tiny) (a19). AG2: o1 and Gemini thinking 0 of 50 on geometry without a symbolic engine, but that setup lacked the engine.
8. **Weak reasoner.** Hilbert with gpt-oss-120b 13.3% vs 70.0% with Gemini 2.5 Pro (b18).
9. **Early general models.** GPT-4 wrote Lean 3 syntax when told Lean 4; PutnamBench 1/640 (c25).
10. **Informal drafts.** A bigger drafter was worse on test in one DSP table (8B 36.5, 62B 34.0, 540B 30.3 in b03) but better in another (a14/c04: 37.7 at 62B, 38.9 at 540B). The sources disagree, so treat drafter effect as unsettled. Test and valid also disagree on which drafter is best.
11. **LeanAgent** only compared to ReProver; several repositories at 0-7% (d12).
12. **Synthetic data.** GPT-f: adding synthetic proofs at 5% of data hurt (c01).

### Moderators
- Model strength (reasoner quality dominates in agents).
- Whether a symbolic engine is present (geometry).
- Problem type: constraint-structured vs forward arithmetic (SATLM); synthetic vs natural text (LINC ProofWriter 98.3% vs FOLIO).
- Sample budget definition (pass@1 vs pass@8192; not comparable without it).
- In-distribution vs novel premises.
- Subject: Seed combinatorics 7/14 vs algebra 72/85.

### Interventions that worked
Verifier-in-loop sampling; decomposition with a cheap exact filler; real-error repair (small); retrieval of solved proofs; tool call to a symbolic helper; solver abstain on UNSAT/ambiguous; stop/restart router (single source).

### Interventions that did not (or did not clearly) work
Tree search over matched samples; LLM-judged back-translation as a fidelity check; neural guidance across distributions; relying on a weak planner; model "looks right" judgments with no kernel (not directly tested here, but it is why the kernel is used).

### Corrections to earlier lines (from critique.md)
- Kimina-Preview 72B numbers (52.94 / 65.16 / 68.85 / 77.87 / 80.74) were mis-credited to DeepSeek-V2 7B in b12 and c12. They are Kimina's own (a18, b13). DeepSeek-V2's own confirmed numbers: 82.4% pass@32, 88.9% pass@8192, 217/244, 47/658, 761.8 vs 6751.9 tokens. The DeepSeek 7B figures need a clean re-read and are not used here.
- b03 says "DSP human proof 38.9%". Correct: human proof 42.6% valid, 39.3% test; Minerva 62B 43.9% valid / 37.7% test; Minerva 540B 42.6% / 38.9%.
- Hilbert is a 2025 paper (arXiv 2509), not 2026.
- A d03 row mapping and c24 row alignment came from jumbled PDF tables; read them as approximate.

## 6. Language models

This whole field is language-model research, so this section pulls out what changed the outcome and by how much.

### 6.1 Trajectory on one benchmark (miniF2F-test)
GPT-f Metamath pass@1 1.3% (2021) -> Thor 29.9% (2022) -> DSP 39.3% (2022/23) -> DeepSeek-V1.5 60.2% whole / 63.5% tree (2024) -> Kimina 80.74% pass@8192 and DeepSeek-V2 88.9% pass@8192 (2025) -> Goedel-V2-32B 90.4% with self-correction -> Hilbert 99.2%, Seed 99.6% (2025). Budgets differ at every step. The last part is saturated; use fresh items.

### 6.2 What changed things, in rough order of size
| Change | Size | Evidence |
|---|---|---|
| Scale of RL/data plus long reasoning | PutnamBench 1 (2024) to 47 (DeepSeek-V2) to 331 (Seed) | a25 |
| Strong general reasoner as planner in an agent | 70.0% vs 13.3% (reasoner swap); 99.2% vs 49.1% (reasoner alone) | b18 |
| Frontier general agent, no training | Aleph 637/672 at $54; Theo 32/32 | d05, d06 |
| Decomposition | 75% (prover only, pass@4) to 98.36% at depth 2 (not token-matched); 8B router paper 23 to 48 of 85 | d13, d07 |
| Informal sketch plus filler | 20.9% to 39.3% (older base) | a14 |
| Hybrid with symbolic tool | 39.0 to 57.0% (PISA) | a11 |
| More samples | +6.5 points for 256x samples at the top end | a19 |
| Tree search over sampling | +3.3 points or under 0.2% | a16, d04 |
| Repair from kernel error | +1.5 to +2.3 points | b07, c14 |
| Retrieval | +3.6 points (LeanDojo random split), +1.3 points and about 43% fewer tokens (Hilbert) | c07, d14 |
| Value function | +2 to +4.6 points (GPT-f) | c02 |

### 6.3 Behaviour of general chat models without a checker or tools
- GPT-4 zero-shot 29.0% on LeanDojo random split and 7.4% on novel premises. GPT-4 1/640 on early PutnamBench; wrote Lean 3 syntax.
- Few-shot GPT-4 on miniF2F 13.52%; the same model in an agent loop with execution and backtracking 26.63% (roughly double). Weaker models gain little (GPT-3.5 9.02%, CodeLlama 5.73%).
- o1 and Gemini thinking: 0 of 50 on IMO geometry where AG2 solved 42.
- On natural-language logic, translation errors and missing implicit facts are the main cause of loss. Syntax errors fall as model strength grows (38% to 24% to 13%).
- Informal drafts are wrong 42% of the time (21 of 50 in the hand check) and sketches still help.

### 6.4 Cost
$5-70 per proof for frontier general agents, $18-170 for trained provers (author estimates; subscription and API list prices differ about 6x; leaderboard cost cells not independently verified; d05, d06, d08). Hilbert uses 24.4M tokens per solved problem. Top DeepSeek numbers need pass@8192.

### 6.5 What this does not tell us
No study here runs a light, training-free scaffold at a fixed token budget against a single long reasoning pass on a small formal set with a frontier model. Aleph and Theo are the nearest, but they are not token-matched (critique GAPS 1).

## 7. What our agent should take

Tags: part = schema part (G guardrail, S state, O operator, memory). Status [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Exact verifier decides acceptance wherever one exists (S4, S8, G2, G3).** Program checks (kernel, unit tests, solver, calculator); model opinion is never the accept signal. [E] K01. Evidence a07, a10, a20, b18. Already in the schema as G2/G3/S8; this adds the strongest numbers for them: every top result in this field depends on a hard checker.
2. **Repair only from located, verbatim checker output, at most 2 rounds (S5, G2).** Gain is small (+1.5 to +2 points), so do not invest more rounds. [E] K06. Evidence a13, b07, b14, c14. Confirms the existing S5 rule.
3. **Pair the model with an exact symbolic or programmatic tool when the step is checkable (O tool call, S7).** [E] K04, K17. Evidence a11, b04, a12, b05, b17, c17. A tool slot for solver, calculator or test runner. Gains come from problems neither part solves alone (8.2%).
4. **Decompose at impasse into subgoals with exact leaf checks, depth at most 2 (O3, S6).** [E] K07. Evidence a14, b03, c04, b18, c19, d13. Confirms O3 and the depth-2 tree rule. Planner quality matters, so use the strongest available model for the decomposition slot (G, K08; b18).
5. **Fail closed at formalisation (S2, S1, G6).** If a text-to-formal translation does not parse or cannot be executed, route to the informal path and log it. Do not treat a translation as ground truth. [E] K10, K11. Evidence b10, c22, a22, c23. Executable rate can be as low as 32.6%.
6. **Budget by difficulty; stop when marginal gain per token falls (G7, G12, S6).** The last 6.5 points cost 256x samples; CoT cost 9x tokens. [E] K03. Evidence a19, b24, c12.
7. **Evaluation hygiene: fresh held-out items for any claim about scaffold gains; state the budget (G7).** [E] K09. Evidence a25, b21, d03.
8. **Memory: store solved subgoals as retrievable worked examples keyed by class; a retrieved hit is a hint, never proof (memory).** In-distribution value is established [E] K05 (a10, b06, c07, d10, d11). That proof retrieval beats lemma retrieval is [S] (d10); see Test first.

### Test first (single-source or contested; nothing here enters SCHEMA.md until its test passes)

1. **Sample-check-repair-decompose scaffold, training-free, vs one long reasoning pass at equal tokens [S].** Part S5/O3, G. K18. Evidence d05, d06 (not token-matched). Test T1.
2. **Error-diversity stop/restart trigger instead of attempt count [S].** Part S6, G12. K20. Evidence d07. Test T3.
3. **Whole-sample vs small tree with checker pruning at equal tokens [C].** Part O (search vs sample). K14. Evidence a13, a16, c27, d04. Test T1 arm D variant.
4. **Fidelity check for self-formalised statements [S].** Part S2/S8. K21. Evidence d01, d02. Prior: a self round-trip does not catch bad forms (97% vs 66%). Test cheaper replacements, such as running the formal form on 2-3 known-answer examples. Test T5.
5. **Formal route vs informal majority vote [C].** Part S8 (when to formalise). K12. Evidence a19, a21 (tiny samples). Test T7.
6. **Solved-example retrieval vs lemma-name retrieval, on held-out new lemmas [S].** Part memory. K05. Evidence d10, d11, c07. Test T6.
7. **Solver route when the task has constraint structure, CoT when it is forward arithmetic [E on shallow sets, untested on ours].** Part S0 gate/S2. K10. Evidence d15, b11. Test T4.
8. **Matched-token ablation of decomposition itself [S].** Part O3. K07/K08 gap. Evidence d13 is not token-matched. Test T9.

## 8. Concrete tests on our bench

All arms get the same total token budget per item, counted including setup (G7). Same items, same seeds, same model unless the test is about the model. Report accuracy, false-accept rate, tokens per accepted answer, and a bootstrap 95% interval. Use items from exact-check families (code with tests, arithmetic or constraint puzzles with a solver, small formal or semi-formal logic items, ARC-style items with held-out examples). Use fresh items not seen in prompts (K09).

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 30-60 exact-check items of mid difficulty (some with a Lean or Python-with-tests checker) | A: one long reasoning pass. B: N short independent attempts, checker picks. C: B plus 1-2 repair rounds with verbatim error. D: C plus decomposition at impasse | Accuracy at budget; false accepts; tokens per accepted | B > A (K02, G11). C adds +1 to +3 points over B. D adds most on hard items, little on easy |
| T2 | Same items | verify-then-accept (checker) vs self-judged accept | False accepts per 100; accuracy | Self-judged accept has several times more false accepts. Checker arm near zero |
| T3 | Hard-tail items where B and C fail often | Fixed N retries vs restart-with-new-decomposition after same error twice vs restart on error-diversity drop | Accuracy at fixed total tokens | Error-diversity trigger beats count (d07: 28.9% vs 19.7% cost cut). Accept only if >= +3 points or >= 15% fewer tokens |
| T4 | 40 items, half constraint-structured, half forward arithmetic | CoT vs text-to-solver (with fail-closed fallback to CoT) | Accuracy; executable rate; fallback rate | Solver wins on constraint items (+15 to +25 points, as in SATLM); tie on arithmetic; frontier model may tie on natural text (LINC FOLIO) |
| T5 | 20 items with a deliberately wrong formal statement (planted) plus 20 correct | Self round-trip check vs 2-3 known-answer examples run against the formal form | Wrong forms accepted | Round-trip misses a large share (human 66% vs LLM 97% faithful); known-answer examples catch more |
| T6 | Items needing a lemma not seen earlier vs seen earlier | No library vs lemma-name library vs solved-example library | Accuracy on seen vs novel; gap | Example library gains most on seen (d10 +47%) and shrinks on novel (c07 51.2 to 26.3). Check it does not hurt on novel items |
| T7 | Mixed set including items with a numeric answer | Majority vote over 5 informal samples vs formal/checked route | Accuracy; cost | Formal wins on items with exact structure; informal vote wins on short numeric answers (a19 6 vs 8) |
| T8 | Hard items | Tool slot (solver/calculator) vs no tool | Accuracy; tool-call rate | Some items solved only with the tool (Thor 8.2%). Gain concentrated in a small share of items |
| T9 | Multi-step items | Direct attempt vs sketch-then-fill vs extra independent samples to match tokens | Accuracy | Sketch beats extra samples only on multi-step items. If tie, the decomposition gain was only extra tokens |

## 9. What does not transfer, and why

- **Absolute numbers.** miniF2F and PutnamBench are saturated and public; budgets are pass@8192 and millions of tokens. Our bench has far smaller budgets.
- **Training-based gains.** Most gains in this field come from RL, expert iteration, online training (HTPS 1360 A100 days) and data. Our scaffold forbids training (K13: small provers win by data, not by scaffold).
- **The kernel.** A Lean kernel is a perfect, cheap checker. Most of our tasks have partial checkers (held-out examples, tests). Fitting the examples is not proof (G3). Weaker checkers leak false accepts; the Lean numbers are an upper bound.
- **Proprietary heavy compute.** Seed-Prover heavy, Hilbert at 24.4M tokens per solved problem, Aleph $54-68 per problem. Not reproducible at our budget.
- **Human-made statements.** Seed-Prover IMO 2025 statements were formalised by humans. Formalisation is the step our agent must do itself (S2), and it is the weak link.
- **Geometry and classic provers.** AG2 and Vampire depend on a closed domain with a dedicated symbolic engine.
- **Tree search.** Marginal over sampling at matched samples; not worth building before T1 arm D shows a need.
- **Lifelong retraining (LeanAgent, HTPS online training).** Updates weights. Only the memory idea transfers.
- **Neural clause selection.** Not a language-model result and does not transfer across families.
- **Informal-only tasks.** Where there is no formal check, none of the verifier gains apply; fall back to agreement and the no-check mode (G4).

## 10. Open questions

1. At equal total tokens, does a training-free scaffold match trained provers or a single long reasoning pass? (K18; Aleph and Theo are the only hints.)
2. How much of Hilbert's and DSP's gain is decomposition itself versus the specialised prover or extra tokens? (d13 prover-only baseline is a weak pass@4.)
3. How often does self-formalisation silently change the statement in our own tasks, and what cheap check catches it?
4. Does the exact-check route help on code-with-tests and arithmetic as much as on Lean? (Not studied here.)
5. Does a solved-example library transfer to new premises? LeanDojo 51.2 to 26.3; Rango partial fix; no direct rerun.
6. Token-matched whole-proof vs tree search (Baldur vs HTPS vs RMaxTS).
7. Classic ATP: CASC solve counts, and whether LLM-guided premise selection helps saturation provers (not found).
8. Whether Lean version changes or contamination alter the saturated numbers (no non-replication found; not searched systematically).
9. Is error diversity a better stop/restart trigger than attempt count outside an 85-item workshop study?
10. Does the drafter's size matter for sketches? DSP tables disagree (see section 5, item 10).

## 11. Sources

[V] opened as full text or page this session (per evidence file); [M] snippet or secondary page only. [V*] marks the 10 papers the critique re-opened as full-text PDFs.

**Classic era**
- [M] Newell, Shaw, Simon (1956) Logic Theory Machine, via https://en.wikipedia.org/wiki/Logic_Theorist (a01)
- [M] Davis (1954) Presburger program, via https://en.wikipedia.org/wiki/Automated_theorem_proving (a02, a04)
- [M] Robinson (1965) resolution, via https://en.wikipedia.org/wiki/Resolution_(logic) (a03, b19)
- [V, secondary page] McCune (1997) Robbins problem, via https://en.wikipedia.org/wiki/Robbins_algebra (a05); Wikipedia ATP/CASC/TPTP https://en.wikipedia.org/wiki/Automated_theorem_proving (a06)
- [M] CASC-J12 results https://tptp.org/CASC/J12/WWWFiles/Results.html (b20)

**Neural ATP**
- [V*] Polu and Sutskever (2020) GPT-f https://arxiv.org/abs/2009.03393
- [V] Lample et al. (2022) HyperTree Proof Search https://arxiv.org/abs/2205.11491
- [V] Zheng, Han, Polu (2022) miniF2F https://arxiv.org/abs/2109.00110
- [V*] Yang et al. (2023) LeanDojo https://arxiv.org/abs/2306.15626
- [V] Jiang et al. (2022) Thor https://arxiv.org/abs/2205.10893
- [V] Mikula et al. (2023) Magnushammer https://arxiv.org/abs/2303.04488
- [V] First et al. (2023) Baldur https://arxiv.org/abs/2303.04910
- [V*] Jiang et al. (2023) Draft, Sketch, and Prove https://arxiv.org/abs/2210.12283
- [V*] Tsoukalas et al. (2024) PutnamBench https://arxiv.org/abs/2407.11214
- [V] Xin et al. (2024) DeepSeek-Prover-V1.5 https://arxiv.org/abs/2408.08152
- [V] Lin et al. (2025) Goedel-Prover https://arxiv.org/abs/2502.07640
- [V*] Lin et al. (2025) Goedel-Prover-V2 https://arxiv.org/abs/2508.03613
- [V*] Wang et al. (2025) Kimina-Prover Preview https://arxiv.org/abs/2504.11354
- [V*] Ren et al. (2025) DeepSeek-Prover-V2 https://arxiv.org/abs/2504.21801
- [V*] ByteDance Seed (2025) Seed-Prover https://arxiv.org/abs/2507.23726
- [V] Chervonyi et al. (2025) AlphaGeometry 2 https://arxiv.org/abs/2502.03544
- [V*] Hilbert (2025) https://arxiv.org/abs/2509.22819
- [V] Thakur et al. (2024) COPRA https://arxiv.org/abs/2310.04353
- [V] Lin et al. (2025) Lean-STaR https://arxiv.org/abs/2407.10040
- [V] Song, Yang, Anandkumar (2024/25) Lean Copilot https://arxiv.org/abs/2404.12534
- [V] Kumarappan et al. (2025) LeanAgent https://arxiv.org/abs/2410.06209
- [V] Wu et al. (2022) Autoformalization with LLMs https://arxiv.org/abs/2205.12615
- [V] Ospanov, Farnia, Yousefzadeh (2025) miniF2F-Lean Revisited https://arxiv.org/abs/2511.03108
- [V] Liu et al. (2025) ProofAug https://arxiv.org/abs/2501.18310
- [V] Soltani Moakhar et al. (2026) Theo https://arxiv.org/abs/2606.31134
- [V] Rognvaldsson, Sun, Dekoninck, Vechev (2026) cost-quality tradeoff of agentic proving https://arxiv.org/abs/2606.04883
- [V] Chvalovsky, Suda, Urban (2026) Teaching Vampire New Tricks https://arxiv.org/abs/2609.16228
- [V] Thompson et al. (2025) Rango https://arxiv.org/abs/2412.14063

**Neurosymbolic logic**
- [V*] Olausson et al. (2023) LINC https://arxiv.org/abs/2310.15164
- [V] Pan et al. (2023) Logic-LM https://arxiv.org/abs/2305.12295
- [V] Ye et al. (2023) SATLM https://arxiv.org/abs/2305.09656

**Secondary citations only:** costs of $50 and over $40 per problem (d08) are cited inside d07 and were not re-opened. Aleph and Seed-Prover 1.5 figures come from the Theo leaderboard table (d06) and were not independently verified.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 11 established claims: 7 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D03.03-K01** (reworded: the sources support less). Sources show proofs are checked by the proof assistant, but not that this verifier is 'exact' for every result or that every result is reportable only because of it: it checks validity against the formal statement only (Seed-Prover IMO statements were human-formalised; lean-gym wrongly rejected 21.1% of correct proofs; miniF2F statements have been found flawed). Corrected claim: A proof assistant kernel (Lean, Isabelle) gives an exact check that a proof is valid for the formal statement as written, which is why recent prover results can be reported with confidence; it does not check that the statement matches the intended problem, and benchmark tooling can still misjudge proofs.
- **D03.03-K04** (reworded: the sources support less). Thor numbers (57.0 vs 39.0 vs 25.7, 8.2% neither) are correct, but Magnushammer is a learned premise selector that replaces Sledgehammer's selection (59.5 vs 38.3, a different Sledgehammer baseline from Thor's 25.7), not a generator paired with a symbolic tool beating both. Corrected claim: Pairing a language model with a symbolic tool beats either alone: Thor 57.0% vs LM 39.0% vs Sledgehammer 25.7% on PISA, with 8.2% solved by neither alone. Separately, a learned premise selector (Magnushammer) beats Sledgehammer's own premise selection, 59.5% vs 38.3% on PISA.
- **D03.03-K05** (reworded: the sources support less). All numbers check out, but 'helps mostly in-distribution' is not supported by LeanDojo: retrieval adds +3.6 points on the random split and +3.1 on novel_premises (a larger relative gain on the harder split), so the gain is not concentrated in-distribution. Corrected claim: Retrieval of relevant facts helps in and out of distribution but absolute accuracy is much lower on new premises: LeanDojo ReProver 51.2% random split vs 47.6% without retrieval, and novel_premises 26.3% vs 23.2%; GPT-4 zero-shot 29.0% and 7.4%. Gap check: in-project step-wise retrieval (Rango) keeps unseen-project accuracy at 32.0% vs 36.8% file-wise; LeanAgent continual updating proved 155 sorry theorems; neural clause guidance in Vampire falls below default off-distribution.
- **D03.03-K09** (reworded: the sources support less). Numbers are right (Thor 29.9, Seed 99.6, GPT-4 1/640, Seed 331/657, Hilbert 462/660), but only miniF2F is saturated; PutnamBench at 50-70% solved is not, and problem counts differ by version (640, 657, 660). Corrected claim: miniF2F-test went from 29.9% (Thor, 2022) to 99.6% (Seed-Prover, 2025) and is now saturated; PutnamBench rose from 1/640 (GPT-4, 2024) to 331/657 (Seed-Prover) and 462/660 (Hilbert) in 2025, so it is far from saturated yet. Numbers from different eras and benchmark versions should not be compared directly.
- **D03.03-K03** (now single-source: only one opened source, code check).
- **D03.03-K17** (now single-source: only one opened source, code check).
