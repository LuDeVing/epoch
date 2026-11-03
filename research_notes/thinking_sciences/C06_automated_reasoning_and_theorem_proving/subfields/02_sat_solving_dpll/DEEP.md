# SAT solving, DPLL: deep document

*Subfield C06.02. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K28), critique.md in this folder. Evidence ids (a01, b11, c08, d02...) point to those files. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

SAT asks one question: given a Boolean formula in conjunctive normal form (CNF, an AND of OR-clauses), is there a true/false assignment that makes every clause true? It was the first problem proved NP-complete (Cook 1971, a24, not opened). No known algorithm is fast in the worst case.

DPLL is the classic complete search method for it. It does four things in a loop (a02):
1. Unit propagation: if a clause has one unassigned literal left and the rest are false, that literal is forced. Set it.
2. Pure literal elimination: if a variable appears with one sign only, set it that way.
3. Stop: no clauses left means SAT. An empty clause means this branch is UNSAT.
4. Decide: pick a variable, try one value, recurse; if that fails, back up and try the other value.

Wikipedia states this as five rules: Propagate, Pure, Decide, Backtrack, Fail (a02).

Modern solvers use CDCL (conflict-driven clause learning). CDCL is DPLL plus learned clauses, non-chronological backjumping, restarts and forgetting (a03). Industrial solvers solve instances with millions of variables this way.

Why it matters for our agent (S4 TEST): a SAT instance is the cleanest model of "test candidate answers against constraints". Three lessons carry over. First, apply all forced consequences by code before guessing (unit propagation). Second, when a branch fails, record why, so the same failure is not repeated (clause learning). Third, a verdict can come with a checkable certificate (an assignment for SAT, a proof for UNSAT). The other half of the field asks how language models do when handed SAT-like tasks, and whether they should do the search themselves or hand it to a solver.

This is a technical field. There are no human-subject studies. "Founding studies" here are algorithm and benchmark papers, and the evidence is runtimes, solved-instance counts and LLM accuracy.

## 2. History and theories in depth

**1960-1962: DP and DLL.** Davis and Putnam (1960) gave a resolution-based procedure. Davis, Logemann and Loveland (CACM, 1962) replaced the memory-hungry resolution step with backtracking search. This is what is called DPLL. Note: the Wikipedia intro says 1961; the paper is CACM 1962 (a01, critique).

**1971: Cook.** SAT is NP-complete (a24, not opened). So no polynomial algorithm is expected, and interest moves to typical-case behaviour.

**1992: hard and easy distributions.** Mitchell, Selman and Levesque (AAAI 1992, a23, not opened) showed random 3-SAT is easy when there are few or many clauses, and hardest near the clause/variable ratio alpha of about 4.27, where about half of formulas are satisfiable. Statistical physics (Monasson et al. 1999, a21) linked this to a phase transition. Ding, Sly and Sun (2022, a22) proved the threshold location for large k. Status [E] (K01, four sources). Practical meaning: difficulty is not set by size alone. Test sets must sweep alpha.

**1996-1999: GRASP and clause learning.** Marques-Silva and Sakallah (GRASP, ICCAD 1996; IEEE Trans. Computers 1999, a25, not opened) added conflict analysis: when a branch fails, derive a new clause that rules out that whole cause, and jump back to the relevant level, not just the last decision. Bayardo and Schrag (AAAI 1997) did related look-back work (a03).

**2001: Chaff.** Moskewicz, Madigan, Zhao, Zhang and Malik (DAC 2001, a05). Reported one to two orders of magnitude speed-up over GRASP and SATO on difficult benchmarks. The authors credit engineering, not stronger learning: two-watched-literal propagation (do not touch clauses that cannot yet become unit), the VSIDS decision heuristic (favour variables in recent conflicts, with decay), and restarts. Numbers: SSS-SAT.1.0, Chaff finished all 100 instances in under 1000 s (100 s cap each) while SATO aborted 32 of the first 41 it tried. VLIW-SAT.1.0, Chaff finished 100 in under 10000 s; SATO and GRASP aborted 19 of the first 20. On easy DIMACS sets all three tie. Caveat: authors' own runs and configs; they could not reproduce one GRASP result (a05).

**2003: MiniSat.** Een and Sorensson (a26, not opened): a small clean reference CDCL solver, the base for many later solvers.

**2009: Glucose and LBD.** Audemard and Simon (IJCAI 2009, a07). A learned clause is scored by its literal block distance (LBD): the number of distinct decision levels in it. Low-LBD clauses are reused much more. Use counts per clause: LBD 2 had 202 propagation uses and 1827 conflict uses; LBD 3, 50/295; LBD 4, 26/136; LBD 5, 19/80; length-2 clauses 209/2452. Keeping low-LBD clauses and deleting the rest helped: on SAT-Race 06 the original MiniSat solved 70, with LBD 79, with extra tweaks 82. Glucose solved 176 on its table (PicoSAT 153, RSAT 139, MiniSat 132, zChaff 2001 84), and was 1.7x faster than RSAT on commonly solved instances. Single source for the claim that a cheap score beats keep-all or length (K03, [S]). Benchmark sets and cut-offs differ between tables.

**2016: Pythagorean triples.** Heule, Kullmann and Marek (a08, a09, b20). Can {1..n} be 2-coloured with no monochromatic a^2+b^2=c^2? The answer is no for n=7825. Method: cube-and-conquer. Cost about 4 CPU years: 21,900 + 13,200 CPU hours. The formula F7825 was reduced to 3745 variables and 14,672 clauses. The proof is a DRAT certificate of almost 200 TB (68 GB compressed) checked by an independent verified checker. Lesson: a hard negative claim can be made trustworthy by a checkable certificate, so the solver need not be trusted (K04, [S]).

**2018-2024: neural SAT.** NeuroSAT (Selsam et al., a10-a12, b01-b03): a message-passing net trained on one bit (sat/unsat) reached 85% on SR(40), decoded a satisfying assignment in 70% of satisfiable cases, and scored 25% on SR(200) with more iterations; NeuroUNSAT and clustering variants scored 100% and 98% in the reported setups. It is far weaker than CDCL. NeuroCore (Selsam and Bjorner, b04-b06) put predictions inside Glucose: 205 vs 187 solved, but the authors later showed random logits (rand-glucose) matched it on SATCOMP-2018, so most of the gain was a refocusing effect. On scheduling, neuro-glucose solved 20% more and rand-glucose 2.5% fewer. Also Graph-Q-SAT (b07, b08), G4SATBench (b09, b10: weak transfer across distributions and sizes; GNNs behave like local search, not CDCL), QuerySAT (b21), and NeuroBack (b22: 193/197/203 and 198/190/204 solved, gains +5.2%, +3.0%, +7.4%, with a random-phase control).

**2022-2026: LLMs enter.** Two threads: (a) LLMs as direct reasoners on SAT-like tasks (Hazra 2024/2025, SATBench, Zhang 2026, ZebraLogic, SATQuest); (b) LLMs as translators into a solver (SatLM, Logic-LM, SAT-RL), and LLMs as designers of solver heuristics (AutoSAT, AutoModSAT, SATLUTION, DaSAThco, AESAT). Details in sections 3, 5 and 6.

**Competing readings of why LLMs fail.** (1) Shortcut view (Hazra): LLMs track statistics such as the share of satisfying assignments, not search. (2) Budget view (Verma 2026, d02): failure is partly the token cap. (3) Complexity-collapse view (Utsho 2026, c24; Zhang 2026): accuracy holds then collapses past a size threshold. (4) Bias view (SATBench): models over-say SAT and give invalid traces. These are not exclusive.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Random 3-SAT is hardest near alpha 4.27, about half satisfiable | threshold proven for large k | a21, a22, a23 | [E] K01 |
| Chaff is 1-2 orders of magnitude faster than GRASP/SATO, due to engineering | SSS-SAT.1.0: 100/100 in <1000 s; SATO aborted 32 of first 41 | a05 | [E] K02 (authors' runs) |
| LBD picks useful learned clauses | LBD 2: 202/1827 uses; MiniSat 70 vs 79 vs 82 solved; Glucose 176 vs MiniSat 132 | a07 | [S] K03 |
| SAT proof as checkable certificate | n=7825; ~4 CPU years; 200 TB DRAT (68 GB compressed); F7825 3745 vars, 14,672 clauses | a08, a09, b20 | [S] K04 |
| Non-reasoning LLMs drop to ~10% in the hard 3-SAT region | ~5000 formulas, n<=10, mean n 7.2; few-shot no help | a13, a14, c14, c15 | [C] K05 |
| Zhang 2026: most models say SAT almost always, no easy-hard-easy shape except GPT-5 | ADR: GPT-5 0.79 at 25 vars, 0.35 at 50 (~20% runs finish); others ~0.5 accuracy | a19, a20, c17 | [S] K13 |
| Verma 2026: density and solver hardness are confounded | matched-density pairs with 10x-50x conflict ratio: pooled gap +1.7 points, p=0.74 | d01 | [S] part of K05 |
| DeepSeek-R1 is the exception on small 3-SAT | R1 hard-region accuracy beats others' easy-region accuracy; flat in model-count ratio; more thinking tokens in hard region | a14, a15, b17, c16 | [S] K06 |
| Translate to CNF and call a solver beats direct LLM search | ~100% across alpha vs ~10% hard region (GPT-4, MiniSat) | a13, c14 | [C] K07 |
| On real text, translation costs accuracy | legal NLI: real Z3 pipeline beat plain LLM for 1 of 5 models (Claude 74.5 vs 63.1); scope laundering 15.3-52.5%; answer accuracy 91.2 vs formula equivalence 80.6 | d04, d05 | [C] K07/K25 |
| SatLM beats CoT on constraint tasks (code-davinci-002) | GSM-SYS 69.4 vs CoT 46.5 vs ProgLM 43.4; LSAT 35.0 vs 23.5; BoardgameQA 79.4 vs 60.7; ProofWriter 99.7; prior SoTA 37.4 and 80.7 | b14, c01, c02 | [C] K08 |
| With 2025 models the solver gain is small on near-ceiling sets | GPT-5 ProofWriter 98.60 vs 98.66; LogicalDeduction 100 vs 99.56; mean -0.13; DeepSeek-Reasoner ProofWriter 96.87 vs 98.61; at 14-17 steps solver keeps 76.7% vs CoT 62.2% | d08 | [C] K08 |
| Solver is not universally better | Logic-LM GPT-4: PrOntoQA 83.2 vs CoT 98.8; better on ProofWriter, FOLIO, LogicalDeduction, AR-LSAT | c05-c07 | [S] K09 |
| Solver signals enable abstention and repair | SatLM selective accuracy 77% vs 45% on GSM-SYS; Logic-LM FOLIO executable rate 66.7% to 84.3% (GPT-3.5), accuracy plateaus early | b15, c03, c06 | [E] K10 |
| UNSAT is much harder than SAT | SATBench hard: SAT 66.7 vs UNSAT 39.3 (average); o4-mini 91.1 vs 65.0; Claude 3.7 hard UNSAT 42.1; o4-mini overall 89.3; DeepSeek-R1 87.8; Claude 3.7 overall 74.8; hard average 53.0 | a17, b11, c08 | [E] K11 |
| SATQuest agrees: harder with solver complexity | o3-mini 0.56 and R1 0.42 overall; MUS tasks among hardest | d09 | [E] K11 |
| Satisfiability bias and invalid traces | o4-mini SAT label 94.7 vs trace 74.6; Claude 3.7 83.2 vs 47.4; bias = 68.7% of o4-mini errors (R1 40.5%) | a18, b12, c09 | [E] K12 |
| Naming failure patterns recovers failures | 60.4% of o4-mini and 73.2% of R1 failures corrected on re-evaluation; LoRA only 51.9 to 53.6 (Qwen2.5-14B) | b13 | [S] K14 |
| Token cap explains part of UNSAT failure | at 16k: all 28 non-abstained random-UNSAT rows hit cap, accuracy 0.036 vs 1.00 on SAT control; at 32k gap gone | d02 | [S] K23 |
| Surface form shortcuts | relabelling cut accuracy a mean 93 points for one model, none for another; satisfiable pigeonhole lookalikes raised false-UNSAT 2.1% to 18.8% (Llama 3.3) | d03 | [S] K24 |
| Narrative wrapper costs little for strong models | o4-mini puzzle 89.4 vs raw CNF 94.3; V3 84.0 vs 87.3 | c10 | [E] K22 |
| Search-heavy CSPs collapse with size | ZebraLogic o1-full 81.0, Llama-405B 32.6 (large 1.5, X-large 0.0); GPT-4o majority 38.0 (N=32), oracle best-of-N 60.3 | c19, c24 | [E] K21 |
| CoT transformers can in principle run DPLL | O(p^2) params, CoT 8p-20p steps; trained 99.8%+ in-distribution; no length generalisation; full trace correct down to 86.06% on skewed data | a16, c11, c12 | [S] K19 |
| Neural SAT classifiers generalise poorly | NeuroSAT 85% SR(40), 70% decoded, 25% SR(200) | a10, b01-b03, b09, b10 | [E] K17 |
| Neural guidance in CDCL: small, partly refocusing | NeuroCore 205 vs 187; rand-glucose equal on SATCOMP; NeuroBack +5.2%/+3.0%/+7.4% | b04-b06, b22 | [E] K18 |
| LLM-evolved solver heuristics: real but shrinking | AutoSAT beats MiniSat on 9 of 12 sets; SATLUTION 347/345/344 vs 334/331 (official 327/321); AESAT train gain 36.6% PAR2 vs held-out 1281-1291 solved vs 1269 (about 1-2%); only 46% of training winners kept edge | b23-b25, c20-c23, d06, d07 | [E] K20, K27 |
| Decisions agree across encodings | CNF vs Vertex Cover vs 3D packing agree on 75-80% | b19, c18 | [S] K15 |

## 4. Mechanisms and models

An engineer can implement each of these. The program does the search; the model fills slots.

**4.1 DPLL with unit propagation (the core loop).**
```
solve(F, assignment):
  loop:
    unit = clauses with exactly one unassigned literal and no true literal
    if an empty clause exists: return UNSAT(conflict clause)
    if no unit: break
    set each unit literal true; record "forced by clause C"
  if all clauses satisfied: return SAT(assignment)
  v = pick_variable(F)
  for value in [True, False]:
    r = solve(F with v=value, assignment + v)
    if r is SAT: return r
  return UNSAT
```
Pure literal elimination is optional. Cost control: keep two watched literals per clause so propagation does not scan every clause (a05).

**4.2 Clause learning and backjumping (CDCL).** Keep an implication graph: each forced literal points to the clause that forced it. On a conflict, walk back from the conflict clause, resolving with the reason clauses, until the learned clause has exactly one literal from the current decision level (first UIP). Add the clause. Jump back to the second-highest level in it, not the previous decision. Effect: the same cause of failure is never explored again (a03). First UIP and VSIDS details are in Chaff (a05, a06) and not on the Wikipedia page.

**4.3 VSIDS.** Each variable has a score. Bump the score of variables seen in conflict analysis. Periodically divide all scores (decay). Branch on the top score. Meaning: recent trouble is the best guide (a06).

**4.4 Restarts and forgetting.** Restart search often, keeping learned clauses. Delete learned clauses that look useless. LBD is the cheap usefulness score: count distinct decision levels in the clause; keep low values (a07). Agent analogue: score a memory note by a cheap proxy and keep the top few. Untested for LLMs.

**4.5 Certificate checking.** SAT: plug the assignment in and evaluate every clause; linear time. UNSAT: the solver emits a DRAT proof (lemma list) and an independent checker verifies each lemma (a08, a09). Agent analogue: any claim "no solution exists" should ship a checkable reason; a SAT claim must survive substitution.

**4.6 Cube-and-conquer.** Split the problem with a lookahead step into many small "cubes" (partial assignments) and solve each with CDCL in parallel (a08). Agent analogue: split by code, not by the model.

**4.7 Translate-then-solve (SatLM pattern).** The model writes declarative constraints (variables, constraints, query). Z3 or MiniSat decides. Solver output has hard states: SAT with model, UNSAT, AMBIGUOUS (several models), execution error. Use these for abstention and repair (b14, b15). Logic-LM adds a few self-refinement rounds on the solver's error text (c06).

**4.8 Matched-pair evaluation (ADR).** For each SAT formula build its one-edit UNSAT twin. Score a pair as correct only if both are right. Always-SAT guessing scores 0 on pairs (a19, a20, K13).

**4.9 Trace grading.** To grade an LLM's SAT trace: take the claimed assignment and evaluate it. For UNSAT take the claimed contradiction or core and check each clause exists and the derivation is sound. SATBench's finding (label right, trace wrong) is only visible this way (a18, b12).

**4.10 Self-improving solver loops.** AutoSAT, AutoModSAT, SATLUTION and AESAT use an LLM to propose code changes to solver heuristics, run them on a training set, and keep winners. Needed controls: a held-out set drawn differently, an equal-budget parameter-tuning baseline (missing in these papers), and instance families not in training (d06, d07).

## 5. What holds up

**Holds up well**
- The phase transition and its location (K01, four sources, one a proof).
- CDCL, VSIDS and watched literals as the engine of modern solvers (K02). Caveat: Chaff's numbers are the authors' own.
- UNSAT is harder than SAT for LLMs (K11): SATBench and SATQuest agree. Report them separately.
- Satisfiability bias and label-right/trace-wrong (K12): SATBench and Zhang agree on direction.
- Solver error signals support repair and abstention (K10).
- Search-heavy CSP accuracy falls with search space and conflicts (K21): ZebraLogic and Utsho.
- Neural guidance gives small gains once a random control is run (K18). The NeuroCore headline (+10 to 20%) did not survive the authors' own random-logits check on SATCOMP.
- LLM-evolved heuristics give some real gains (K20), but they shrink on held-out data (K27).

**Contested**
- Easy-hard-easy shape for LLMs (K05). Hazra 2024/2025 (same group) see it with n<=10 and mostly non-reasoning models. Zhang 2026 (25-75 variables) find most models label nearly everything SAT; only GPT-5 tracks the transition. Verma 2026 finds solver conflict ratio does not order accuracy at matched density. Possible causes: sizes, tasks (search vs decide), models.
- DeepSeek-R1 robustness (K06). Hazra: flat and strong at n<=10. SATBench: 44.7% of its errors are context inconsistency. Zhang: reasoning models fall apart past 25 variables.
- Solver gain (K07, K08). Old model (code-davinci-002): large gain on GSM-SYS, LSAT, BoardgameQA. Current models: under 1% on near-ceiling deduction sets, with a retained advantage at depth (76.7 vs 62.2 at 14-17 steps). Logic-LM loses on PrOntoQA (83.2 vs 98.8). In legal NLI the real Z3 pipeline was worse than the plain LLM for 4 of 5 models.

**Failures and null results**
- Few-shot examples did not lift the hard region (a14).
- Story wrapper did not help GPT-4 (a13); it costs a few points for strong models (c10).
- Light LoRA on 1,100 traces: 51.9 to 53.6 (b13).
- Density and conflict proxies do not order accuracy for three instruct models (d01).
- Majority vote adds almost nothing on large puzzles (GPT-4o 38.0 at N=32 vs oracle 60.3) (c19). Oracle best-of-N is not a usable arm.
- Self-refinement plateaued after early rounds (c06).
- Neural SAT classifiers do not transfer across distributions or sizes (b09, b10).

**Moderators**
- Formula size and variable count (collapse past about 25 variables for most models; GPT-5 0.79 to 0.35 from 25 to 50 variables).
- Token budget (d02: 16k vs 32k cap).
- Surface form (d03).
- Input format familiarity (R1 tied to familiar formats, a14; R1 and QwQ drift in raw DIMACS, d10).
- Whether the translation step is faithful (d05).
- SAT vs UNSAT side.

**Interventions that worked:** declarative formalisation plus solver (old model, clean tasks); solver-error repair loop (early rounds); explicit failure-pattern naming (re-evaluation only); matched-pair scoring (for measurement); certificates.
**That did not:** few-shot, story re-encoding, light fine-tuning, voting at scale, neural guidance without a random control.

**Evidence quality warnings** (critique.md). Nearly all LLM-SAT data are tiny random formulas. CDCL's strength is on structured industrial instances, which no LLM agent has been tested on. Many LLM claims rest on one paper repeated across files. Solver-evolution numbers are author-reported on own hardware (SATLUTION official baselines 327/321 vs authors' 334/331). Several 2026 papers are preprints with small model panels. SATQuest text and figure disagree on GPT-4.1 and V3; the figure was used.

## 6. Language models

**Direct reasoning.**
- Non-reasoning LLMs (GPT-4, GPT-4o, Gemini 2.0 Flash, Claude 3.7, V3): about 10% in the hard 3-SAT region at n<=10 (a14). They mostly fail to classify UNSAT. GPT-4 does greedy-like search and relies on solution-count shortcuts (a13, a14, c14).
- DeepSeek-R1 is the exception. Its traces show backtracking, unit propagation, heuristic choice and self-correction, but it often stops without exploring the whole tree, so it is sound on SAT and incomplete on UNSAT (a14, a15).
- SATBench (a17, b11, c08): o4-mini 89.3 overall (hard 78.0: SAT 91.1, UNSAT 65.0); R1 87.8 (hard UNSAT 83.6); Claude 3.7 74.8 (hard UNSAT 42.1). Average hard 53.0; hard SAT 66.7; hard UNSAT 39.3. Accuracy falls as clauses grow.
- Label vs trace: o4-mini 94.7 vs 74.6; Claude 3.7 83.2 vs 47.4 (a18). Satisfiability bias is 68.7% of o4-mini errors and 40.5% for R1.
- Zhang 2026: GPT-5 ADR 0.79 at 25 variables, 0.35 at 50 with about 20% completion at 50; other models near 0.5 past 25. A model with precision 0.78, recall 0.76, F1 0.77, accuracy 0.77 scored only 0.60 on ADR, so plain accuracy overstates skill (a19, a20, c17).
- Hazra 2025: accuracy rises with the satisfiable share (model count / 2^n) for non-reasoning models; R1 is flat; R1 uses more thinking tokens in the hard region (b16, b17).
- Budget: reasoning models hit the output cap on hard UNSAT. At 16k all 28 non-abstained random-UNSAT rows capped (accuracy 0.036) while the satisfiable control was 1.00. At 32k the gap went (d02).
- Giving up: o3-mini output gets shorter on MCS/MUS tasks at high complexity; models fabricate solver calls; R1 and QwQ drift in raw DIMACS (d09, d10).
- ZebraLogic (c19): o1-full 81.0 overall; Llama-405B 1.5 on large and 0.0 on X-large; adding samples helps little by vote.
- Utsho 2026 (c24, abstract and intro only): reasoning models hold up, then collapse past a task-specific threshold; drops often over 50%; failures are inconsistent traces and incomplete assignments.
- Surface sensitivity: relabelling cut one model by a mean 93 points; the pigeonhole lookalike changed false-UNSAT 2.1% to 18.8% for Llama 3.3 (d03).

**Solver delegation.**
- Hazra (a13): GPT-4 translates to CNF, MiniSat solves: about 100% at all alpha. This measures translation plus a trusted solver, not LLM reasoning (critique).
- SatLM (b14, c01-c04): old model, large gains (see table). Selective accuracy 77% vs 45% on GSM-SYS using solver status.
- Logic-LM (c05-c07): mixed; PrOntoQA worse.
- 2025/2026 models (d08): under 1% gain on near-ceiling sets; advantage at 14-17 steps (76.7 vs 62.2). Small R1 distills often fail to produce formalisations; Qwen3 14-32B match GPT-5 once they emit valid FOL.
- Faithfulness (d04, d05): scope laundering 15.3-52.5%; the real Z3 pipeline beat the plain LLM for 1 of 5 models in legal NLI. Without a faithfulness reward, answer accuracy was 91.2 but formula equivalence 80.6.

**What changed things, by how much.**
- Reasoning training (R1, o-series): from about 10% to above it in the hard region on small formulas.
- Solver delegation: large gains on an old model; near zero on easy sets for current models.
- Naming failures: 60.4% / 73.2% of failures corrected on re-evaluation (selection-biased).
- More tokens: removes the matched-density gap between 16k and 32k (one model family).
- Light fine-tuning: +1.7 points.

**LLMs as solver designers.** AutoSAT, AutoModSAT, SATLUTION, DaSAThco, AESAT: see sections 3 and 5. Training-set gains are large (36.6% PAR2) and held-out gains small (1-2% more solved). No equal-budget tuning baseline.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Report SAT-side and UNSAT-side accuracy separately on every constraint benchmark; add UNSAT-heavy hard items | S4 test design | [E] | a17, b11, c08, d09 (K11) |
| Check the reason, not only the label: substitute the claimed assignment by code; for "impossible" claims demand the conflicting constraints and check them | G3/G10, S4, S8 | [E] | a18, b12, c09, c17 (K12) |
| Use hard tool signals (UNSAT, ambiguous, execution error) for abstention and at most 2 repair rounds, with the real tool output shown | G2, S5 | [E] | b15, c03, c06 (K10) |
| Include a random-control arm for any feature that injects guidance (hint, retrieved note, ranking) | G7 | [E] | b04-b06, b22 (K18) |
| Evaluate any self-improvement loop on a held-out split drawn separately from the tuning set, and against equal-budget tuning | G7, outer loop | [E] | b23-b25, c20-c23, d06, d07 (K20, K27) |
| Do not rely on majority vote on large constraint puzzles; oracle best-of-N is a ceiling, not an arm | G4, G5 | [E] | c19, c24 (K21) |
| Do not assume narrative re-encoding helps; for strong models it costs a few points | none | [E] | c10, a13 (K22) |
| A small-formula success is no evidence about larger sizes; test beyond example size | S0/S4 | [E] | b09, b10 (K17), a19 |
| Sweep difficulty (alpha 3, 4.27, 6) when testing a search task | test design | [E] | a21-a23 (K01) |

Note: these checks fit G3, G10 and S8 already. What is new is the specific form: assignment substitution, core checking, UNSAT reported separately, random-control arm.

### Test first

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| Code does unit propagation before the model guesses (forced-move step), with explicit decide/propagate/backtrack trace and code-verified steps | S4 / O (new "propagate" step) | [S] | a02, a03, a16, K02, K19 | No LLM study at equal tokens (d15) |
| Translate-then-solve, routed only when the problem is formalisable | O (tool delegation) | [C] | b14, c05-c07, d04, d05, d08 (K07-K09) | Gain measured on old model; faithfulness loss on real text |
| Require executed tool output, not narrated solver output | G10 | [S] | d04 (K25) | scope laundering 15.3-52.5% |
| Forced check before answering "SAT/valid"; for "impossible" demand a checkable core | S8 | [S] | b13, a18 (K12, K14) | SATBench fix was on re-evaluation |
| Name known failure modes (satisfiability bias, early stop, narrated solver call) in a short note | G | [S] | b13 (K14) | selection effect |
| Stop-and-delegate rule before hitting the budget cap on hard UNSAT-like items | S6, G12 | [S] | d02 (K23) | one model family |
| Abandonment signal: shortened trace on hard items | S6 | [S] | d09, d10 (K26) | |
| LBD-like cheap score for which lessons to keep | memory | [S] | a07 (K03) | human solver only; no LLM test |
| Paired-twin items (same logic, new surface; one-edit SAT/UNSAT twins) as shortcut detector | S4 / test design | [S] | d03, a19 (K13, K24) | |
| Certificate for negative claims, checked by an independent checker | G3, S8 | [S] | a08, a09, b20 (K04) | |
| More thinking in hard cases | G12 | [S] | a15, b17 (K06) | R1 only |

## 8. Concrete tests on our bench

All arms get the same total token budget, including setup, repairs and solver-call tokens (G7). Report SAT and UNSAT sides separately.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Random 3-SAT, n 8-12 and 25-50, alpha 3, 4.27, 6; half SAT, half one-edit UNSAT twins | plain / CoT / best-of-N vote / scaffold with code unit propagation and verified decide-backtrack trace | ADR pair accuracy; label accuracy; trace accuracy | Scaffold above CoT at n 25-50, small at n<=10 |
| T2 | Same items | scaffold with forced assignment substitution and core check vs same without | trace validity; false-SAT rate | False-SAT rate falls; UNSAT label accuracy up |
| T3 | Our own formalisable constraint puzzles (logic grids, scheduling, SATBench-style hard) | direct reasoning / translate-then-solve always / routed | accuracy; translation executable rate; faithful-formalisation rate | Solver wins at depth, ties on easy; router best |
| T4 | T3 items plus 5 non-formalisable items | narrated-solver prompt vs executed-tool prompt | agreement of narrated vs executed answer | Narration disagrees on a sizable share (d04 range 15-52%) |
| T5 | Hard UNSAT items at budgets 8k, 16k, 32k | plain vs stop-and-delegate at 50% budget | accuracy by budget; cap-hit rate | Delegation recovers the 16k loss |
| T6 | Paired twins: original and relabelled/lookalike items | plain vs scaffold | accuracy gap | Scaffold shrinks the gap |
| T7 | SATBench hard (UNSAT heavy) | plain vs prompt with named failure modes | fresh-run accuracy, not re-evaluation | Gain smaller than the 60.4% correction figure; 3+ points counts |
| T8 | Lesson memory over 30 related problems | keep-all vs LBD-like score (lessons used in distinct sub-problems) vs random keep | accuracy; context tokens | Score beats random keep at equal context |
| T9 | Any scaffold feature that injects hints | feature vs random-hint control | accuracy difference | Feature must beat the random control |
| T10 | Evolved prompts or heuristics | tuned on split A, tested on split B from a different family | held-out gain vs training gain | Held-out gain far under training gain |

## 9. What does not transfer, and why

- **Raw CDCL speed numbers.** They come from compiled code on millions of clauses. A language model does not process clauses at that rate. Only the structure transfers (forced moves first; learn from conflicts; check certificates).
- **VSIDS and watched literals as such.** These are engineering for fast propagation. In an agent, code can do propagation exactly, so the model needs no analogue.
- **LBD as proven for LLM memory.** It was shown for clause deletion in a solver. Whether low decision-level spread predicts a useful lesson for an LLM is unknown.
- **Neural SAT results (NeuroSAT, GNNs).** They are trained networks; a prompt-only scaffold does not train. They also generalise poorly (K17). Value is as a warning and a baseline.
- **Pythagorean-triples scale.** 4 CPU years and 200 TB of proof are not agent scale; the lesson is the checker, not the cluster.
- **Small-formula LLM results (n<=10).** Real tasks have structure and larger size; errors could go either way.
- **SatLM gains from code-davinci-002.** Current models are near ceiling on the deduction sets (d08).
- **"About 100% with MiniSat".** This measures translation plus a trusted solver on clean CNF, not reasoning, and clean CNF is rare in real tasks.
- **Evolved solver gains.** Training-set gains do not carry to held-out sets (1-2%).
- **Phase transition for non-random problems.** The alpha 4.27 peak is a property of random k-SAT; our tasks are not random.

## 10. Open questions

1. Does a prompt-only scaffold (code unit propagation, explicit decide/backtrack trace, certificate check) beat plain CoT and best-of-N on random 3-SAT near 4.27 at equal tokens? No study (d15).
2. Do current models still gain from declarative formalisation plus solver on LSAT, BoardgameQA, GSM-SYS, and by how much per token? (d08 covers only near-ceiling sets.)
3. How often does NL-to-constraints translation fail on our own problems, and does that hide the "about 100%" figure?
4. At what size do R1, o4-mini and GPT-5 fail at a fixed generous budget: size or budget?
5. How much of satisfiability bias goes away with a forced substitution check in a fresh run?
6. Do current reasoning models act like DPLL (backtracking, propagation) or like greedy local search? Only qualitative remarks exist (d10).
7. Is there a cheap quality score for what the agent keeps in memory, as LBD is for clauses?
8. After equal-budget tuning and structured held-out instances, what is left of LLM-evolved heuristics?
9. Do checked proof-style UNSAT outputs (resolution or clause-learning traces with an external checker) improve UNSAT accuracy?
10. Does the solution-count shortcut appear in ZebraLogic or SATBench? A paired-twin test could say.
11. Does the contested easy-hard-easy shape come from formula size, task type (search vs decide) or model type?

## 11. Sources

[V] = opened this session, [M] = snippet or secondary only. Evidence ids in brackets.

- [V] Wikipedia, DPLL algorithm (a01, a02, a04). https://en.wikipedia.org/wiki/DPLL_algorithm
- [V] Wikipedia, Conflict-driven clause learning (a03). https://en.wikipedia.org/wiki/Conflict-driven_clause_learning
- [V] Moskewicz et al. (2001) Chaff (a05, a06). https://www.princeton.edu/~chaff/publication/DAC2001v56.pdf
- [V] Audemard and Simon (2009) Predicting learnt clauses quality (a07). https://www.ijcai.org/Proceedings/09/Papers/074.pdf (critique: only partly re-checked on MiniSat variant counts)
- [V] Heule, Kullmann, Marek (2016) Pythagorean triples (a08, a09, b20). https://arxiv.org/abs/1605.00723
- [V] Selsam et al. NeuroSAT (a10-a12, b01-b03, c13). https://arxiv.org/abs/1802.03685
- [V] Selsam and Bjorner (2019) NeuroCore (b04-b06). https://arxiv.org/abs/1903.04671
- [V] Kurin et al. Graph-Q-SAT (b07, b08). https://arxiv.org/abs/1909.11830
- [V] Li, Guo, Si, G4SATBench (b09, b10). https://arxiv.org/abs/2309.16941
- [V] QuerySAT (b21). https://arxiv.org/abs/2106.07162
- [V] NeuroBack (b22). https://arxiv.org/abs/2110.14053
- [V] Hazra et al. (2024) Can LLMs reason? 3-SAT (a13, c14, c25). https://arxiv.org/abs/2408.07215
- [V] Hazra et al. (2025) Have LLMs learned to reason? (a14, a15, b16, b17, c15, c16). https://arxiv.org/abs/2504.03930
- [V] Pan et al. (2025) Can transformers reason logically? (a16, c11, c12). https://arxiv.org/abs/2410.07432
- [V] Wei et al. (2025) SATBench (a17, a18, b11-b13, c08-c10). https://arxiv.org/abs/2505.14615
- [V] Zhang, Chen, Chen (2026) Matched-pair evaluation (a19, a20, b18, b19, c17, c18). https://arxiv.org/abs/2605.28602
- [V] Monasson et al. (1999) 2+p-SAT (a21). https://arxiv.org/abs/cond-mat/9910080
- [V] Ding, Sly, Sun (2022) satisfiability conjecture (a22). https://arxiv.org/abs/1411.0650
- [M] Mitchell, Selman, Levesque (1992) (a23). https://www.aaai.org/Papers/AAAI/1992/
- [M] Cook (1971) (a24). https://dl.acm.org/doi/10.1145/800157.805047
- [M] Marques-Silva and Sakallah GRASP (a25). https://doi.org/10.1109/12.769433
- [M] Een and Sorensson MiniSat (a26). http://minisat.se/Papers.html
- [V] Ye et al. (2023) SatLM (b14, b15, c01-c04). https://arxiv.org/abs/2305.09656
- [V] Pan et al. (2023) Logic-LM (c05-c07). https://arxiv.org/abs/2305.12295
- [V] SATLUTION (b23). https://arxiv.org/abs/2509.07367
- [V] AutoModSAT (b24, c21). https://arxiv.org/abs/2507.22876
- [V] DaSAThco (b25, c22). https://arxiv.org/abs/2509.12602
- [V] Lin et al. (2025) ZebraLogic (c19). https://arxiv.org/abs/2502.01100
- [V] Sun et al. (2024) AutoSAT (c20). https://arxiv.org/abs/2402.10705 (JAIR page d14 [M])
- [V] Schidler and Szeider (2025) (c23). https://arxiv.org/abs/2501.14630
- [V] Utsho et al. (2026) (c24; abstract and intro only). https://arxiv.org/abs/2604.13371
- [V] Verma (2026) Solver-hard is not model-hard (d01-d03). https://arxiv.org/abs/2607.17047
- [V] Wang et al. (2026) Know your limits (d04). https://arxiv.org/abs/2606.16118
- [V] Sun and Meel (2026) SAT-RL (d05). https://arxiv.org/abs/2610.14402
- [V] Luo et al. (2026) AESAT, IJCAI (d06, d07). https://www.ijcai.org/proceedings/2026/257
- [V] Wang, Seggoju, Paschke (2026) CoT vs solver-augmented (d08). https://www.neurosymbolic-ai-journal.com/system/files/nai-paper-952_0.pdf
- [V] Zhao et al. (2026) SATQuest (d09, d10). https://arxiv.org/abs/2509.00930
- [M] LLM-guided evolutionary search for constraint model reformulation (d13). https://arxiv.org/abs/2607.28268
- [M] FSTA 2026 trace-learning lead (d12): no title, do not cite.
- [M] Search status notes (d15, d16).

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 9 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C06.02-K17** (reworded: the sources support less). G4SATBench findings are accurate (b09 and b10 are the same paper), but the general claim ignores that the original NeuroSAT paper reports generalisation to larger problems (25% of satisfiable SR(200)) and new domains by running more iterations, and G4SATBench says SR-trained models generalise better. Corrected claim: G4SATBench finds that NeuroSAT and GGNN struggle to generalise across distributions in most cases and show limited generalisation to larger formulas (better when trained on SR), and that GNNs learn a heuristic akin to greedy local search and fail to learn the CDCL heuristic; the original NeuroSAT paper reported more favourable transfer to larger problems when run for more iterations.
