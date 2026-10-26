# Lemma discovery and conjecturing: deep document

*Subfield C06.07. Written 2026-10-26 from evidence_a-d.jsonl (about 140 evidence lines), claims.jsonl (K01-K21) and critique.md in this folder. Numbers follow the critique's corrections. Where the critique says a figure is version-specific or from a snippet, it is marked. Links to other subfields are notes only: Library learning (DreamCoder, LILO), Proofs and refutations (conjecture refinement), Abduction, Conflict-driven clause learning, Geneplore, Quality-diversity.*

---

## 1. What it is

A lemma is a small true statement that helps prove a bigger one. A conjecture is a statement offered as possibly true. This subfield asks four questions.

1. Can a machine propose statements worth proving? (conjecturing)
2. Can it find the missing step in a stuck proof? (lemma discovery)
3. How many of its proposals are true, new and used? (yield)
4. Do kept lemmas help later problems? (transfer)

There are two purposes, and the literature mixes them.

- **Top-down, goal-directed.** A proof is stuck. Find the lemma that bridges the gap. TBC, Hipster proof mode, Kaliszyk and Urban chained conjecturing, LEGO-Prover requests, Hilbert subgoals.
- **Bottom-up, exploratory.** Explore a theory with no target. Find its laws. AM, Graffiti, HR, QuickSpec, MathlibLemma, STP conjecturer.

For our agent the question is narrower. Our agent works inside one session, with a checker where one exists, and no training. Almost all the evidence is for formal provers (Lean, Isabelle, HOL Light) with a proof checker. So the question "does asking for lemmas help a scaffold on plain-text hard problems, at equal tokens" has no direct answer in the literature (critique gaps 1 and 2). This document says what the formal evidence implies, and what we must test.

Where lemma-making sits in our schema:

- **O3 Decompose** (sub-problems whose answers combine) is the closest operator. A lemma is a decomposition whose parts are reusable statements.
- **O1 Specialise / O2 Generalise** are the two ways a lemma is made from a goal (QuickSpec tests special cases; LEGO-Prover's evolver generalises).
- **S4 TEST / S7 SELECT** hold the filters (counterexample search, discriminating tests).
- **Memory: subgoal library** (planned, [D]) is the place where kept lemmas live.
- **G4, G5, G8, G10** govern who may judge a lemma: code and checkers, not the proposing model.

---

## 2. History and theories in depth

### 2.1 AM and Eurisko (Lenat, 1976-1984)

AM represented a math concept as a small Lisp predicate. New concepts came from small syntactic mutations of that code, steered by empirical findings and heuristics. In the June 1976 worked example, LIST-EQUAL was true on about 2% of random list pairs (about 50 example lists). That rarity fired "generalize" and gave L-E-1 (same length), L-E-2 (same first element) and L-E-3. From same-length AM derived length, natural numbers, addition, and elementary number theory (a01).

Lenat and Brown's own retrospective (AAAI-83, a01, a02, a25, c27) gives the key lesson. Much of AM's success came from the density of worthwhile math concepts when written as Lisp, not from the heuristics alone. Mutations of short predicates had a high hit rate. The same scheme aimed at heuristics (two-page Lisp bodies) almost always gave junk. Eurisko only improved after heuristics were split into many small slots, so one slot edit expanded into many coordinated code edits. Heuristic bodies often shrank by an order of magnitude. AM stalled because it could not find new domain-specific heuristics for the fields it opened. They also argue that structure-level mutation says nothing about meaning: a minimal structural generalisation need not be a minimal meaning generalisation.

Critique and replication: Ritchie and Hanna (1984) said the published description did not match the program. Heuristics were mixed into control code, some rules were vague (Rule 218, "structurally similar"), and user hints steered it. Ritchie (1991) noted that seven years on almost nothing had built on AM and there were no reported replications (a03, a23/b21, b23; mostly abstract or secondary text, see section 11). No hit-rate count exists. Treat AM as a design lesson, not as measured evidence. [K12]

### 2.2 Graffiti and the graph-theory line (Fajtlowicz, 1988 onward)

Graffiti generated graph inequalities of fixed shapes and tested them against a stored example set. The "Dalmatian" rule keeps a conjecture only if it holds on all stored examples and is sharper on at least one than earlier ones (b24). This keeps counts low. The weakness is the fixed example set: false conjectures survive if the counterexample graph is missing. Graffiti used a few hundred graphs. Graffiti.pc used up to millions, yet a bigger set did not always help, because small special counterexample graphs were still missing (b24). Johansson and Smallbone note that systems that generate test data on demand avoid this (a23).

Many Graffiti conjectures led to published papers. The numbers "about 80 papers, at least 60 proved" come from a history page and a blog (b27) and are unverified. Papers inspired is not the same as conjectures proved. Modern descendants: the Optimist (Davila, 2024; about 60 broad conjectures from a tiny knowledge base), TxGraffiti (table-true linear-program inequalities, ranked by touch and sharpness; true only on the table), AutoGraphForge (2026: refutation against about 348,000 graphs left 6,522 conjectures; LLMs used only for proving; no proved count in the abstract) (b24, b25, c28).

### 2.3 HR (Colton, Bundy, Walsh, 1999-2002)

HR represents a concept as a data table, with 10 production rules that turn old concepts into new ones. A conjecture appears when a new concept's table equals an old one. Conjectures go to the prover Otter and the model finder Mace (which adds counterexamples to the data). Interestingness is scored by parsimony, complexity, discrimination, proof difficulty and surprisingness (a04). Best result: refactorable numbers (the divisor count divides the number), missing from the OEIS and added. HR conjectured they are 0, 1, 2 or 4 mod 8 and that odd refactorables are squares; later proved. The publisher blurb claims 20 new number types accepted by the OEIS (b26, snippet only). No junk-rate counts.

### 2.4 Theory exploration: QuickSpec, Hipster, IsaCoSy, TheSy, TBC

**QuickSpec** (Claessen, Smallbone, Hughes, 2010; a05, a06, b14). Generate terms from a signature, test on random data, group terms into equivalence classes, read equations off the classes, prune what follows from earlier ones by congruence closure. Raw step: 5,000 to 50,000 equations. The target is tens. After pruning, the heap library gave a short complete set, and adding list operations found `toList (fromList xs) == sort xs` (heapsort). Its only interestingness test is "not reducible by what is known". It rarely produces false or duplicate conjectures, because testing is built in, but testing is unsound and needs executable generators. It scales to about 30 functions or term size about 9.

**Hipster** (2014; a08). QuickSpec inside Isabelle/HOL. Default 200 random tests, stop if classes were stable over the last 100, else double. Drops any lemma that routine reasoning (no induction) proves. Proved lemmas are tagged and reused. Has an exploratory mode and a proof mode (find the lemma missing from the current goal). The Isabelle kernel checks every proof.

**Johansson and Smallbone survey (2021)** (a06, a07, a27). Three families of conjecture generator: heuristic rule-based (AM, HR, MATHsAiD), term generation plus testing (QuickSpec, Graffiti, IsaCoSy, IsaScheme, Speculate), neural. Also the top-down / bottom-up split. Vampire solved 7 of 50 TIP inductive problems alone; with a 90-line script that adds QuickSpec conjectures as lemmas it solved 25 (7 plus 18; 3 problems timed out in QuickSpec). HipSpec 44, CLAM 41 (partly interactive), Zeno 21.

**TheSy** (2020; b15, c25). Symbolic exploration with abstraction. On CVC4's 311-problem suite, 5 min: TheSy plus simple induction proves 187; Z3 75; CVC4 without conjecturing 70; CVC4 with its own conjecturing 260. So the built-in generator beat TheSy. On 85 IsaPlanner problems TheSy was 380 times faster than Hipster at the 25th percentile (0.48 s vs 182.47 s), 57 times at the median, 6 times at the 75th, but overall slower (51.6K s vs 47.1K s) because of its case splitting (critique correction 1). [K16]

**Template-Based Conjecturing, TBC** (Nagashima et al., 2022; a09, b13, c22). 16 fixed templates (identity, commutativity, associativity and similar) replace random term generation. On failure: generate, refute with Quickcheck and Nitpick, prove with Sledgehammer (5 s per conjecture), retry the goal with proved ones as lemmas. TIP benchmark, 462 problems (85 IsaPlanner, 50 Prod, 327 TIP15). Largest gain: 40 points on Prod. IsaPlanner: 60% solved with no conjecture, so little to gain. Weak on TIP15 (15 min limit). In the running example 10 conjectures were proved and only 2 used (8 of 10 unused). Caveat: templates were added after solving some benchmark problems by hand.

**Counterexample plus exploration for missing hypotheses** (Gamboa et al., 2023; b20, ACL2). When a conjecture is false, restricted exploration over non-redundant terms can suggest the missing hypothesis: `(consp x)` for `(< 0 (len x))`. It fails when the needed predicate is not in the vocabulary, and a subsumption heuristic chose too-weak hypotheses in a real-number case (counterexample x = 1/2). Case studies only.

### 2.5 Lemma mining from existing proofs (Kaliszyk and Urban, 2014)

Only a tiny fraction of lemmas in HOL Light and Flyspeck are named and reused. They mined the inference graph for all intermediate lemmas (about 20 million stored; 25% more time, 6 GB), scored them (dependency count U, savings D, size, conjunction test, PageRank variants), de-duplicated, and added the best to the premise pool (a11, a24, b16, b17, c26).

- Core HOL Light, 1,954 theorems. Old best of 14 methods 63.1%; union 65.4%.
- Fully honest evaluation: 61.7% to 64.8% (about 5% relative).
- Cheating scenario (a nearby lemma from the target's own proof is available): 76.5%.
- Chained conjecturing of mid-proof lemmas: Q2 54.5% to 61.4% (chain 1) and 63.8% (chains 1-3), that is +12.6% and +17.0% relative.
- Housekeeping: about 33% of clauses from 200,000 core lemmas are subsumed; 2,076,682 partly de-duplicated lemmas fell to 1,076,995 after alpha-normalisation. Doubled size often means a mere conjunction. PageRank PR1 and PR2 pick overlapping lemmas (79%), reverse PageRank PR3 and PR4 overlap only 11%.

The lesson is about evaluation: leaking the lemma from the answer inflates gain from 5% to about 24% relative.

### 2.6 Neural conjecturing (2020 onward)

- **Urban and Jakubuv (2020)** (b19). GPT-2 on Mizar. 381,432 predictions, 193,320 unique. Statements look right but are mostly not useful. Language-model loss does not measure logical usefulness. Early small experiment.
- **Rabe et al. (2020)** skip-tree (a10). Details in section 3.
- **Gauthier and Urban (2025)** (b18, c20, c21). Learning conjecturing from scratch on 16,197 OEIS-derived problems. Brute-force start (1,000 candidates per problem) solved 2,506. Four self-learning runs reached 5,565, against 2,265 for CVC5, Vampire or Z3 at 60 s. The loop took about three months. Gains came in jumps when one reusable predicate appeared (iteration 41 of run 1). Predicates are trained on own solved problems, so memorisation rises.
- **Minimo** (Poesia et al., 2024; c16, c17). Conjecturer and prover trained by self-play on an 8.45M-parameter model; conjectures picked by hardness; hindsight relabeling learns from failed attempts. Without relabeling the conjecturer collapses to trivial statements (such as `0 = 0` in arithmetic). Exact rates only in figures (not seen).
- **STP** (Dong and Ma, 2025; a16, a17, a26, b10, b11, c14, c15). One model is conjecturer and prover. Details in sections 3 and 4.

### 2.7 LLM conjecture-and-prove loops (2023 onward)

- **LEGO-Prover** (Wang et al., 2024; a12-a14, b08, b09, c01-c03, d06, d07). Prover plus evolver share a growing library of verified lemmas ("skills") in vector stores. Details in section 4.
- **Conjecturing-Proving Loop, CPL** (Kasaura et al., 2025; a14, a15, c04-c06). Separate conjecturer call (GPT-4o, library as context) and prover call (o3, Lean feedback, up to 16 tries). Verified pairs join the library.
- **MathlibLemma** (2026; a20-a22, b01-b04, c10-c13). Four stages: Discovery, Judge, Formalizer, Prover, seeded by one Mathlib file at a time.
- **Lemmanaid** (Alhessi et al., 2025/2026; b05-b07, c07-c09). A small tuned model predicts lemma templates; a symbolic engine fills the holes.
- **Johansson and Smallbone (2023)** (c23, c24). GPT-4 as lemma proposer in Isabelle. A case study.
- **Seed-Prover** (ByteDance, 2025; b12, c18, d05) and **Hilbert** (2025; c19, d01-d04, d15). Industrial decomposition systems.
- **DeepSeek-Prover-V2** (d09). Subgoal-style chain of thought, about 10 times more output tokens.

Sections 3 to 6 give the numbers.

### 2.8 Theory of why conjecturing should help

Three arguments recur in the sources.

1. **Dense feedback.** Real targets give almost no signal when the prover is weak. Conjectures near the edge of ability give some. STP: at an 11.4% checkpoint, only 131 of 2.5M proofs for 79K unproved statements were correct, yet at least 47% of generated conjectures were proved (a17). Earlier work cited there: 98.5% of sampling compute produced no proof.
2. **Reuse.** A proved lemma is paid for once and used many times. Gauthier and Urban's jumps came from single reusable predicates (c21).
3. **Compositional search.** Splitting a long proof into lemma-sized steps lets a weaker prover solve each step. Hilbert's 7B DeepSeek prover goes from 61.3% (pass@4) to 96.7% or 98.4% inside the decomposition (d02).

The counter-arguments are also in the sources. Most proposals are not used (section 3). Lemma yield depends on the representation (AM). Gains shrink when the base prover is already strong (TBC on IsaPlanner). Leakage inflates results (Kaliszyk and Urban).

---

## 3. Core findings with exact numbers

"Useful" has a different meaning in each row. Do not put the rates on one scale (critique, weak spots).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Neural skip-tree conjectures: provable vs provable and new | Assumptions task 32.19% / 26.20%; equalities 19.61% / 12.28%; free-form 82.32% / 12.70% (uniform data), 97.75% / 0.59% (weighted sampling). Prover proves only about 58% of validation theorems, so these are lower bounds | Rabe et al. 2020 (a10) | single paper, checked against survey (a07) |
| Used at least once in over 200,000 proofs | 3,445 of 3,857 assumption theorems (89%); 979 of 3,440 equalities (28%); 49 of 130 free-form (38%) | Rabe 2020 (a10) | low bar: use as premise survives a pruning step |
| Survey figure for neural conjectures | 13-30% both provable and new; rest copies, alpha-renamings or false | Johansson and Smallbone 2021 (a07, b14) | second-hand |
| Lemmanaid census of 7,628 generated conjectures (HOL-test) | Gold 1,721 (22.6%); other true 1,356 (17.8%); false 1,802 (23.6%); unresolved 2,749 (36.0%) | Alhessi et al. (b06, c08) | single group |
| QuickSpec precision | Several thousand lemmas; precision under 1% on Octonions | Lemmanaid (b07) | single group |
| MathlibLemma funnel (GPT-5.1, 109 seed files) | Proposed 3,427 / 2,591 / 3,130 (total 9,148). Judge-accepted 71.4 / 66.6 / 63.2%. Compilable of accepted 77.1 / 70.6 / 61.3%. Trivial 4.1 / 6.6 / 10.8%. Final 4,028 (about 44% of proposals) | Liu et al. 2026 (a20, b01, c10) | established that filters remove most (K02) |
| LLM judge false rejections | Audit of 53 judge-rejected: 54% truly false, 46% valid | MathlibLemma (a20, b02, c11) | single source, n=53 (K03) |
| Proving the discovered lemmas, Success@2 | GPT-Reasoning 19.39%, Goedel 17.70%, GPT 15.69%, Kimina 10.70%, DeepSeek-32B 6.98%, DeepSeek-70B 6.68%, Qwen 2.46%. Union 37.39% (foundational 47.48, applied 27.48, abstract 30.93). Goedel-8B pass@16 only 0.32% (13/4,028) | MathlibLemma (a21, b03, c12) | single source |
| Expert audit of unsolved lemmas | 107 of 138 (78%) provable; of 31 unproven: 25 (81%) missing hypotheses, 5 (16%) false, 1 formalisation gap | MathlibLemma (b03) | residual sample, not random |
| Real-world uptake | 6 hand-cleaned lemmas submitted to Mathlib: 3 merged, 1 redundant, 2 not pursued. 1,506 released proofs; about 200 USD for statements, 500 USD proving; 0.46 USD per proof all-in (about 0.33 proving only) | MathlibLemma (a22, c13) + critique 4 | pilot, n=6 |
| QuickSpec as lemma front end | Vampire on 50 TIP: 7 alone, 25 with QuickSpec lemmas; HipSpec 44, CLAM 41, Zeno 21 | Johansson and Smallbone 2021 (a06) | authors' survey (K04) |
| Template conjecturing | +40 points on Prod; IsaPlanner 60% unaided, small gain; 2 of 10 proved conjectures used in the running example; TIP15 weak | Nagashima et al. 2022 (a09, b13, c22) | tuned templates |
| Lemma mining, honest evaluation | 61.7% to 64.8% (about 5% relative); cheating 76.5%; chained conjecturing 54.5% to 61.4% to 63.8% | Kaliszyk and Urban 2014 (a11, b16) | single group (K13) |
| LEGO-Prover headline | 100 attempts, ChatGPT: miniF2F-valid 57.0% (prior 52.4), test 50.0% (prior 45.5); 257 of 488 problems solved overall | Wang et al. (a12, c01) | version-dependent figures |
| LEGO-Prover library ablation | Valid split, 50 attempts: 50.4% vs 47.1% (+3.3). Gap near zero early, widens. Library 22,532 skills: 10.8% from prover, 38.2% from request solver, 51.1% from directional transformation. 24% of 135 proved problems used retrieved skills (51% copied, 49% imitated) | (a13, b08, b09, d07) + critique 6 | single run; no-library arm also drops the evolver (K05, K06) |
| CPL discovery | Target theorem found 5 of 20 runs (avg 106 theorems) vs 0 of 20 for simple loop (avg 328); Fisher p=0.024; 14M tokens per run; o3 | Kasaura et al. (c04) | single source, one target (K07) |
| CPL library in context | Re-proving 2,123 theorems: 99% (2,106) with earlier library vs 91% (1,935) with definitions only; McNemar p=4e-35. First-loop runs: 309 theorems vs 941; loop proofs longer (KS p=1e-13) | (c05) | partly measures memory of own proofs |
| Version-specific CPL numbers (do not cite) | "30 loops, 269 theorems vs 400 loops, 359"; "267 of 269"; "128 tries" | earlier arXiv version (a14, a15) | dropped, per critique 5 |
| Models judge a true new theorem false | GPT-4o said false 10 times, wrong proof 6 times; GPT-o3 gave no wrong proof but always judged it false | CPL (c06) | one theorem |
| STP self-play | LeanWorkbook 28.5% vs 13.2% for best expert iteration (training set). miniF2F-test 65.0% (pass@3200), ProofNet-test 23.9%, PutnamBench 8/644. 48 iterations, 3.6M conjectures, 241M proofs, 51.3B tokens | Dong and Ma (a16, b10, c14) | training method |
| STP transfer | Only 2-3 points higher pass@128 on miniF2F-test and ProofNet-test from retraining with conjectures | (b11, c15) | appendix, single run (K08) |
| Seed-Prover | Heavy: 5,000 conjectures by default, days of thinking; past IMO 121/155 (78.1%): easy 47/55, medium 47/56, hard 27/44. Medium (not heavy): miniF2F 99.6%, PutnamBench 331/657 (light 201/657) | Chen et al. (b12, c18, d05) + critique 2 | no lemma-pool ablation (K09) |
| Hilbert depth ablation | miniF2F: D=0 75% (Goedel-32B pass@4), D=2 98.36%, D=3 98.7%; final 99.2%; PutnamBench 462/660 vs Seed-Prover 331/657 | Wang et al. 2025 (c19, d01) | confounded by strong reasoner (K09) |
| Hilbert baselines | Goedel-32B alone 90.8% pass@8192, 94.7% with self-correction pass@1024; Gemini 2.5 Pro alone 49.1% (quoted); DeepSeek-7B 61.3% to 96.7%/98.4% inside Hilbert; 671B at pass@8192 88.9%; 2.3M reasoner + 1.3M prover tokens per sample | (d02) | no equal-token arm |
| Retrieval of known theorems | Goedel 99.2% vs 97.9%; reasoner calls 548 vs 862; reasoner tokens 2.3M vs 4.0M. DeepSeek 98.4% vs 97.1% | Hilbert (d03) | near ceiling, single run (K20) |
| Compute scaling in Hilbert | PutnamBench 13.3% at smallest budget to 55.9% at 328K reasoner calls, 424K total calls, 1,880M tokens | (d04) | read from plot text |
| Decomposition costs tokens | DeepSeek-Prover-V2 miniF2F-test 671B: non-CoT 52.94% at 1 sample; CoT 82.4% pass@32, 88.9% pass@8192. Output tokens 442.6 vs 4,488.5 (7B), 761.8 vs 6,751.9 (671B) | Ren et al. (d09) | not equal tokens |
| Verifier needed to convert samples | MATH, Llama-3-8B: coverage 82.9% (100 samples) to 98.44% (10,000); majority vote / reward model only 40.50% to 41.41%. SWE-bench Lite 15.9% to 56% with 250 samples | Brown et al. (d08) | the equal-token baseline for gap 1 (K19) |
| Counterexample reasoning is weak | CounterMath: GPT-4o judgement F1 about 59.0, strict rationale about 19.7%; o1-preview F1 60.1, strict about 39.8% (row alignment uncertain; pattern only) | Li et al. (d13) | scrambled table |
| GPT-4 as plain-text conjecturer | Insertion sort: all lemmas correct and useful. Functional geometry: about 50% of runs gave useful drawing-specific lemmas; most generic ones (associativity, commutativity) false. Renaming Drawing to Monkey removed all drawing-specific lemmas. Temperature above 1 gave non-existent symbols | Johansson and Smallbone 2023 (c23) | case study, contamination admitted (K11) |
| Template vs direct on commercial LLMs | AFP-2026 (leakage-free): Lemmanaid 6.7B 41.7%, neural 6.7B 38.1%; Claude Opus 4.5 19.4% template / 34.5% direct; GPT-5.2 15.8% / 25.2%. Octonions: Lemmanaid 76.6-78.9%, neural 61.7-62.3%, QuickSpec 22.8%, ensemble 84.9%; Opus 47.1/46.3%, GPT-5.2 50.0/45.4%. Prompts about 1,700 vs 325 tokens | Alhessi et al. (b05, b07, c07, c09) + critique 3 | single group; compute not matched (K10) |
| Lemmanaid held-out recall | Best backend: 50.2% HOL-test, 28.6% AFP-test, 41% AFP-2026; ensemble 58.6% / 42.7% | (b05) | gold-match proxy |
| Learning conjecturing from scratch | 16,197 OEIS problems: 5,565 solved vs 2,265 for CVC5/Vampire/Z3 at 60 s; about three months | Gauthier and Urban (b18, c20) | narrow domain, needs training (K14) |
| Names vs constants perturbation | GSM-Symbolic: names-only change small effect, values larger, extra clause up to 65% drop. Putnam-AXIOM: o1-preview 41.9% original, minus 19.6 points (46.8% relative) on 100 variants; 19 models | (d11, d12) | variants may be harder (K21) |
| LLM judges of ideas | Human-human agreement 56.1%; best LLM judge 53.3%; accept/reject papers: Claude-3.5-Sonnet 71.4%, GPT-4o 61.1%, Opus-3 63.5% | Si et al. (d10) | different task |
| Least-to-most prompting | SCAN length split at least 99% with 14 exemplars vs 16% chain of thought | Zhou et al. (d14) | synthetic; decomposition, not lemmas |

---

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it. The agent is a program that fills model slots; the checker is code.

### 4.1 Test-then-prove pipeline (QuickSpec, Hipster, TBC, MathlibLemma)

```
propose(candidates)
  -> dedupe (normalise names; reject if equal to or an instance of a known statement)
  -> triviality filter (provable by routine reasoning, or reducible by known facts)
  -> falsify (run on random or small-case inputs; keep survivors)
  -> [optional] judge (blind; see 4.6)
  -> prove (budgeted)
  -> store (verified lemma + how it was used)
```

Details to copy:

- Hipster test schedule: start with 200 random tests, stop if equivalence classes were stable over the last 100, else double (a08).
- QuickSpec pruning: equations that follow from earlier ones by congruence closure are dropped. Without it the output is 100 times too long (5,000-50,000 vs tens) (a05).
- MathlibLemma funnel: 9,148 proposed to 4,028 kept (44%). The cheap steps (judge, compile, triviality) are run before proving (a20).
- Proof-bypass screen: reject any proof that uses `sorry`, new axioms, constants or opaque definitions (a22).
- In plain text there is no kernel. Replace "compile" by "state the lemma in a form code can run": a Python predicate over small cases. Replace "prove" by "derive inside the main attempt, with the lemma flagged as unverified if no check exists".

### 4.2 Goal-directed lemma proposal at a stuck point (TBC, Hipster proof mode, Kaliszyk-Urban chaining)

1. Run the base attempt. If it passes the check, stop (G1).
2. On a located failure, show the stuck sub-goal.
3. Propose a small set of lemmas (templates or free-form) that would close the gap.
4. Filter (4.1). Prove survivors. Retry the goal with proved lemmas in context.
5. Log which lemmas were used in the final success.

Evidence: the gain is large when the base prover is mid-strength (Prod +40 points; Vampire 7 to 25 of 50) and small when it is already strong (IsaPlanner 60% unaided) or too weak (TIP15). [K04]

### 4.3 Request-and-retrieve library with an evolver (LEGO-Prover)

- Two stores (lemmas and problem-solving skills), embeddings for retrieval.
- Prover loop: split an informal proof into steps. Write the lemma statements it wishes it had ("requests"). Use requests as queries into the store (c03). Write the modular formal proof with the retrieved skills.
- Evolver loop: (a) request solver proves open requests; (b) directional transformation generalises stored lemmas (for example scale a constant to a variable, parameterise, extract key concepts). Added to the library only if SequenceMatcher similarity to existing skills is under 0.85 (d06).
- Observed origin of skills: 10.8% prover, 38.2% request solver, 51.1% directional transformation. Directly reused skills mostly came from request solving (71%), then key concepts 12%, scaling 12%, parameterisation 6% (d07).
- Use: 24% of 135 verified problems used retrieved skills; half copied, half wrote a new lemma imitating one.
- Scaffold lesson: request-style retrieval (ask for the lemma you wish you had, then look it up) is what produced direct reuse. Mass generalisation filled the library (51%) but is not shown to be used.

### 4.4 Separate conjecture and prove calls with the library in context (CPL)

```
library = []
loop:
  statement = conjecturer(context = library + definitions)      # no proof written here
  proof     = prover(statement, feedback = checker, tries <= 16)
  if checked(proof): library.append((statement, proof))
```

The conjecturer never writes proofs. The prover never chooses the statement. The library goes back into the context of both. In the one hard discovery task, this found the target in 5 of 20 runs vs 0 of 20 for the joint call. Cost: 14M tokens per run (c04). Different models in the two arms (GPT-4o and o3 vs o3 alone), so the separation is confounded with a model mix (a14). [K07]

### 4.5 Self-play conjecturer at the edge of ability (STP, Minimo)

Selection rule for training the conjecturer (STP, a16, a26):

- seed theorem with proof, plus a lemma used in it, goes to the conjecturer;
- keep conjectures whose prover pass rate is in (0, 1/4]: barely provable;
- drop the lowest 20% by ratio of minimal proof length to statement length (elegance filter: stops artificially long goals);
- re-weight by Wasserstein distance to the unproved real targets, so topics stay varied (a per-item reward collapses to one mode);
- the lemma in the seed must be used in the conjecture's proof.

Minimo adds hindsight relabeling: a failed attempt that proved some other statement is stored as a success for that other statement (c16, c17). Without it the conjecturer drifts to trivial statements.

Scaffold reading: the "not too easy, not unprovable" band is a usable rule. A scaffold cannot train, but it can discard sub-statements the model solves instantly (trivial) and those it never solves (waste), and keep the middle.

### 4.6 Judge as filter

MathlibLemma's judge drops 30-37% of raw candidates. In an audit of 53 rejections, 46% were valid (b02). The generator and the judge are the same model family, so the set reflects its taste. In a scaffold this is G5 and G8: a judge may rank, it may not kill. Use judge scores to order work, and use tools to reject.

### 4.7 Recursive decomposition (Hilbert, Seed-Prover heavy)

Hilbert: a reasoner writes a proof sketch with `sorry` steps. Each step becomes a lemma. A prover tries each. An unsolved lemma is decomposed again, to depth 5. A retrieval step first looks for an existing library theorem (d03). Disabling the informal shallow solve forces more depth for the same result (d15).

Seed-Prover heavy: propose thousands of conjectures (default 5,000), prove what can be proved into a lemma pool, rank, give hundreds of the best to the main prover. Used only on problems that medium mode failed. Light, medium and heavy differ in compute and in lemma use together, so lemma use is not isolated (d05). [K09]

### 4.8 Lemma value scoring from use (Kaliszyk-Urban)

Score a stored lemma by how many later statements depend on it, how much it saves, its size, and whether it is only a conjunction of two others. Merge alpha-variants first. For a scaffold: keep a per-lemma counter of distinct later problems in which it appears in an accepted answer. This is the metric the literature lacks (critique gap 4; K15).

### 4.9 Representation rule (AM, Eurisko)

Edit small, named units. Mutations of short predicates had a high hit rate. Mutations of two-page bodies were junk until the bodies were split into slots (a01, a02). In lemma terms: keep lemmas short, one claim each, in the problem's own vocabulary. Do not mutate or "improve" a long plan.

---

## 5. What holds up

### 5.1 Established (two or more independent sources)

- **Most proposals are not useful (K01).** Lemmanaid 22.6% gold and 23.6% false; Rabe 12.7% provable-and-new under uniform data and 49 of 130 free-form theorems used; TBC 2 of 10 used; QuickSpec precision under 1%; LEGO-Prover 22,532 skills for a 3.3-point ablation gain. Direction agrees across five systems. Rates are not comparable.
- **Cheap filters remove most raw candidates before costly proving (K02).** MathlibLemma, Hipster, QuickSpec, Lemmanaid, Gamboa et al. all test or refute first.
- **Gains are strongest as goal-directed bridges for a mid-strength base (K04).** Three independent systems (QuickSpec/Vampire, TBC, Kaliszyk-Urban chaining). Small when the base solves most, or when the problem is too hard.
- **A verified-lemma store in context helps modestly (K05).** LEGO-Prover +3.3 points; CPL 99% vs 91%.
- **Self-play conjecturing helps training when expert iteration stalls (K08).** STP and Minimo; transfer is small (2-3 points).
- **Machine checking controls bad lemmas (K17).** Hipster, MathlibLemma and CPL keep only checked proofs. Models in plain language judged a true new theorem false (GPT-4o 10 times, GPT-o3 always).
- **Transfer is weakly measured (K15).** Only Rabe has per-lemma reuse, and only in-run.
- **AM's lesson on representation (K12).** Three sources: the author's retrospective, a critic, a later survey.

### 5.2 Replications, failures and boundary conditions

- **No replication of AM exists** (Ritchie 1991, abstract only). Critics said published descriptions did not match behaviour. Treat AM as inspiration.
- **Leakage inflates results.** Kaliszyk and Urban: 76.5% (cheating) vs 64.8% (honest). TBC templates were added after solving some benchmark problems by hand. GPT-4 had seen the authors' tool repositories and the Isabelle libraries. Lemmanaid's AFP-2026 split is the only leakage-controlled test and is single-group.
- **The headline gains confound lemma use with a stronger system.** Hilbert's D=0 arm is a pass@4 prover with no informal reasoner and far fewer tokens. Gemini 2.5 Pro alone is 49.1% (quoted), the same Goedel-32B prover alone reaches 90.8% at pass@8192 and 94.7% with self-correction at pass@1024. No arm gives the prover the same total tokens. Seed-Prover has no lemma-pool ablation. The 99.6% miniF2F and 331/657 Putnam results are medium mode, not heavy, so they must not be credited to conjecture pools (critique 2).
- **The LEGO-Prover library gain is small and confounded.** Single run, valid split only, 50 attempts. The no-library arm also removes the evolver (more tokens spent on the library arm). Trivial and duplicate lemmas are admitted by the authors. No held-out split. (K06)
- **STP's headline is a training-set number.** 28.5% vs 13.2% is on LeanWorkbook, which the model sees. Of 20 unproved statements, 7 were provable, so the best possible rate is 38.7%-68.5%. Real held-out gain: 2-3 points.
- **Provable is a trap metric (Rabe, Lemmanaid).** Weighted sampling pushed "provable" to 97.75% while "provable and new" fell to 0.59%. Lemmanaid: 36% of outputs are unresolved. Trivial truths (predicting False, `x = x`) appeared on inspection. Minimo drifted to `0 = 0`.
- **Templates are not free help for strong general models.** Opus 4.5 got 19.4% with templates vs 34.5% direct on AFP-2026; GPT-5.2 15.8% vs 25.2%. The small tuned model gains from templates. Possible reasons: longer prompt (about 1,700 vs 325 tokens), format, capability. Untested (K10; critique gap 8).
- **Tool comparisons depend on setting.** TheSy 380 times faster at the 25th percentile but slower overall because of case splitting; CVC4's own conjecturing (260) beat TheSy (187) on a different suite (K16).
- **Fixed example sets fail** (Graffiti). Bigger sets did not always help because small special counterexamples were missing.
- **Gains vanish when the base is strong.** TBC on IsaPlanner (60% unaided); the honest HOL Light lemma-mining gain of about 5%.
- **Sample counts alone do not convert to accuracy.** Coverage 82.9% to 98.44% but majority vote 40.50% to 41.41% (d08).
- **Models do not know when they are wrong about counterexamples.** CounterMath: judging true/false is better than giving a valid rationale (d13).

### 5.3 Interventions that worked

- Test-first filtering (QuickSpec, Hipster, MathlibLemma).
- Goal-directed bridging lemmas for a mid-strength base (K04).
- Separate conjecture and prove calls with library in context in one discovery task (K07).
- Retrieving known theorems before proposing new ones (Hilbert: 99.2% vs 97.9%, 2.3M vs 4.0M reasoner tokens; K20).
- Hindsight relabeling and a difficulty band in self-play (Minimo, STP).
- Union of several provers (MathlibLemma: 19.39% best single vs 37.39% union). Different provers solve different lemmas.
- Missing-hypothesis suggestion from counterexamples in ACL2 (case studies).

### 5.4 Interventions that did not work, or were not shown to

- Judge-only gating (46% false rejections in one audit).
- Free-form neural sampling tuned for provability (Rabe weighted: 0.59% new).
- Mass generalisation to fill a library (LEGO: half of 22,532 skills from directional transformation; no usage count).
- Language-model loss as a proxy for usefulness (Urban and Jakubuv).
- Bigger fixed example sets (Graffiti.pc).
- Mutating long heuristics (Eurisko, before slotting).
- Temperature above 1 (non-existent symbols; Johansson and Smallbone). Temperature 0 gave no visible change.

---

## 6. Language models

### 6.1 How LLMs behave as conjecturers

- **Many proposals, few used.** MathlibLemma funnel keeps 44% of proposals as non-trivial type-checked statements, but only 37.39% of those get proved by any model in the union, and the best single model proves 19.39%. Lemmanaid: about a quarter of outputs match a human lemma.
- **Judges are lossy.** 46% of judge-rejected lemmas were valid (n=53). On research ideas, LLM judges agree with humans 53.3% vs human-human 56.1%.
- **Recall, not derivation, may carry much of the apparent skill.** GPT-4 produced drawing-specific lemmas about half the time, and renaming the symbols removed all of them (c23). The authors found their repositories in the model's memory. On Putnam-AXIOM, o1-preview falls 19.6 points on variants (41.9% original). On word problems, names-only changes barely move accuracy (GSM-Symbolic), so the renaming test only works where names carry meaning.
- **Generic algebraic laws are often false.** Associativity and commutativity were proposed for operations that lack them.
- **Strong models already know what is true.** In AFP-2026 prompting, Opus 4.5 reaches 34.5% when writing lemmas directly; a 6.7B tuned model reaches 41.7% with templates.
- **Wrong about true new theorems.** GPT-o3 always judged the target theorem false; GPT-4o said false 10 times.
- **Counterexample reasoning is weak.** CounterMath strict-rationale rates about 20-40%.

### 6.2 What changed the outcome, and by how much

| Intervention | Change | Source |
|---|---|---|
| Add a checker and keep only checked statements | turns coverage into accuracy (coverage 98.44% vs vote 41.41%) | d08, K17 |
| Goal-directed lemmas at a stuck point | Vampire 7 to 25 of 50; Prod +40 points | a06, a09 |
| Separate conjecture call and prove call | 5/20 vs 0/20 on one target (p=0.024) | c04 |
| Verified earlier lemmas in context | 91% to 99% (re-proving), +3.3 points (LEGO ablation) | c05, a13 |
| Recursive decomposition with a strong informal reasoner | miniF2F 75% (D=0) to 98.36% (D=2); confounded | d01 |
| Retrieve existing theorems | 97.9% to 99.2%; reasoner tokens 4.0M to 2.3M | d03 |
| Templates for a small tuned model | 38.1% to 41.7% (AFP-2026) | b07 |
| Templates for a frontier model | 34.5% to 19.4% (worse) | b07 |
| Self-play conjecturing (training) | LeanWorkbook 13.2% to 28.5%; held-out only 2-3 points | a16, b11 |
| Chained conjecturing | 54.5% to 63.8% relative +17.0% | b16 |
| Decomposition-style chain of thought | 52.94% (1 sample, non-CoT) to 82.4% (pass@32), at about 10 times the output tokens | d09 |
| Union of provers | 19.39% to 37.39% | c12 |

### 6.3 What is not known

There is no equal-token comparison of "lemma-first" against "longer direct attempt" (K18, gap 1). There is no calibrated plain-text lemma truth rate (gap 2). There is no curve of success against the number of conjectures (gap 6; Seed-Prover uses 5,000, CPL ran about 106 theorems per run, LEGO thousands). There is no paired test of goal-directed against undirected conjecturing (gap 7).

---

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Evidence ids are from the evidence files; K-ids are in claims.jsonl.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Falsify before proving.** Any lemma the agent proposes is run on small cases or a computed check (or a counterexample search) before it is proved or relied on. No check possible: flag it "unverified" and do not let it carry the final answer alone. | S4 TEST (before S5/S6 use of a lemma); G3, G10 | [E] K02, K17 | a05, a08, a20, b01, b05, b20, d08 |
| A2 | **Checker output, not model opinion, decides whether a lemma is kept.** The generating model never rejects its own lemma by judgment (a judge may only reorder work). Extends G5 and G8 to lemmas. | G5, G8 | [E] (G5/G8 already [E]; lemma-specific audit n=53 is single-source) | a20, b02, c06, c11 |
| A3 | **Propose lemmas only at an impasse, goal-directed.** Lemma proposing is an S6 operator step (a form of O3, with O1 and O2 as the generators), never run on routine problems. Fits G1 and G12: gains are largest for a mid-strength base and small when the unaided rate is high. | S6, O3, G1, G12 | [E] K04 | a06, a09, a11, b13, b16 |
| A4 | **Within-run verified-lemma store, shown after the first attempt.** Keep checked lemmas, de-duplicated by normalised statement, and place them in context for later steps of the same run. Gain is real but modest, so keep it small. | Memory, subgoal library (within-run only) | [E] K05 (two sources; effect +3.3 points and 91% to 99%) | a13, b08, c02, c05 |
| A5 | **Log the lemma funnel.** For every lemma: proposed, deduplicated, failed falsification, checked, proved, used in the accepted answer, cost in tokens. Report "used fraction" and "tokens per used lemma". | Section 6 logging; G7 | [E] K01, K15 | a10, a09, a13, c08, c30 |
| A6 | **Do not trust "provable" or "plausible" as the quality metric.** Quality is true AND not trivial AND used. | G7, bench design | [E] K01 | a10, b06, b19 |
| A7 | **Keep lemmas short, one claim, in the problem's vocabulary.** Do not mutate or "improve" a long plan as one unit. | O3, O1/O2 output format | [E] K12 (three sources, qualitative) | a01, a02, a25, b21 |
| A8 | **Evaluate lemma value only on cases where the lemma was not derived from the answer.** Treat any leaked run as an upper bound. | Bench design (G3) | [S] K13 (single group) but cheap | a11, a24, b16 |

A8 is single-source and is listed here only because it costs nothing; it is a rule for the bench, not a change to the agent.

### Test first (not yet established for our setting)

| # | Item | Schema part | Status | Evidence | Why not now |
|---|---|---|---|---|---|
| T1 | Lemma-first (propose, check, then solve) vs one longer direct attempt, equal tokens, plain-text hard problems | O3, S6 | [S] gap, K18 | d08, d09, d14 | No paper tests this; formal gains confounded with compute |
| T2 | Computed small-case test on each proposed lemma in plain text | S4, G3 | [S] K19 | d08, d13 | Only formal evidence; counterexample judging by models is weak |
| T3 | Separate "conjecture" call from "prove" call vs joint | S3, S6 | [S] K07 | c04, c05, c06 | One topic, one model mix, 5/20 hits |
| T4 | Retrieve known results first (before inventing a lemma) | Memory, S2 | [S] K20 | d03 | One system near ceiling |
| T5 | Edge-of-ability sub-goals (solved sometimes, not always) | O3, S6 | [S] K08 (training) | a16, a17, a26, c16 | STP is a training result; held-out gain 2-3 points |
| T6 | Recall check: perturb constants or domain names of a lemma; large drop flags memory | G9-like, S4 | [S] K11, K21 | c23, d11, d12 | One case study; Putnam variants may be harder |
| T7 | Cross-problem transfer of stored lemmas (held-out split, per-lemma reuse count) | Memory, subgoal library | [S] K15 gap | a10, a13, c30, d07 | Nobody has measured it |
| T8 | Request-then-retrieve (ask for the lemma you wish you had, then look it up in the store) vs free generation | Memory, S3 | [S] K05/K06 | c03, d07 | 71% of directly reused LEGO skills came from requests, single system |
| T9 | Template/analogue lemma prompts vs cold lemma writing for a strong LLM | O7, O3 | [C] K10 | b07, c09 | Strong LLMs did worse with templates |
| T10 | Number of lemmas to propose at fixed budget (breadth vs depth) | S6, G12 | [S] gap 6 | b12, c04 | Seed-Prover 5,000 vs CPL 106 |
| T11 | Recursive decomposition depth 0, 1, 2 on hard items | O3 | [C] K09 | c19, d01, d15 | Confounded by strong reasoner |
| T12 | Union of lemma proposers from different prompts or models | S3 (G4 caution) | [S] | c12 | Union helps for proving; our samples come from one model and are correlated (G4) |
| T13 | Blind judge for ordering (never killing) lemma candidates | G5 | [S] K03 | a20, b02, d10 | Judge quality on lemmas unmeasured |
| T14 | Compact-rule mutation for O3/O6 prompts | O3, O6 | [S] K12 | a01, a02 | Qualitative |

---

## 8. Concrete tests on our bench

Every test uses two arms at equal total tokens (setup cost counted, G7), the same checker, and the same items. Items must be hard enough that the plain pass rate is neither near 0 nor near 100 (G12; section 5.2: gains vanish at both ends). Report with a paired test (McNemar for pass/fail; bootstrap CI for rates). Use at least 3 seeds. If an item type has no checker, use a computed small-case test (T2).

| Test | Item type | Arm A | Arm B | Metric | Expected effect |
|---|---|---|---|---|---|
| B1 (T1) | Hard exact-answer items needing an auxiliary fact (number theory, inequalities, combinatorial identities); plain pass rate 20-70% | Lemma-first: propose 3-6 lemmas, falsify, solve with survivors | One direct attempt with the same total tokens as one long reasoning, or best-of-N with a check | pass rate per token; pass rate at fixed tokens | Small positive on mid-difficulty items (+3 to +8 points, by the LEGO analogy); zero or negative on easy items |
| B2 (T2, A1) | Same items | Falsification (compute small cases) before relying on a lemma | No falsification | fraction of relied-on lemmas that are false; final accuracy; tokens saved per used lemma | Lemma error rate falls strongly (the filter removes 56% of MathlibLemma proposals); accuracy gain modest |
| B3 (A2, T13) | Lemma candidates with known truth (generate 100 per item type, label by tool) | Blind judge accept/reject | Tool-based accept/reject | judge false-negative rate; judge false-positive rate | Judge false-negative rate near 30-45% (MathlibLemma audit 46%); if lower than 15%, a judge may be used to order work |
| B4 (A3) | Mixed set: 50% easy (plain pass rate over 85%), 50% hard | Lemma step on every problem | Lemma step only at S6 impasse | tokens per solved item; accuracy | Same accuracy on hard, lower cost on easy (G1/G12 pattern); on easy items always-on may lose accuracy |
| B5 (T3) | Open conjecture task: find and prove a non-obvious identity or property in a small domain | Separate conjecturer call then prover call | Joint call | hit rate of the target over 20 runs; theorems per run | Like CPL: 5/20 vs 0/20 is the reference; accept a smaller gap as support |
| B6 (T4) | Items solvable from known theorems | Retrieve known theorems first, then conjecture | Conjecture directly | accuracy; tokens | Small gain and fewer tokens (Hilbert: 2.3M vs 4.0M reasoner tokens) |
| B7 (T5) | Chains of 3-5 dependent sub-statements | Keep only sub-goals the model solves in some but not all of 3 tries | Keep all sub-goals | main-goal pass rate at equal tokens | Positive if the band rule works (STP reading) |
| B8 (T6) | Proposed lemmas from B1 | Perturb constants and domain names | Original statement | accuracy of the lemma's use; true/false stability | A large drop on perturbed variants marks recall, not derivation |
| B9 (T7, A4) | A stream of 40+ related problems in order, plus a held-out set from a different class | Lemma store carried across problems | No store (store reset each problem) | accuracy gap vs stream position; per-lemma reuse count on held-out | Gap grows with stream length (LEGO); near zero on held-out class if transfer is weak |
| B10 (T8) | Same stream | Request-then-retrieve | Free generation into the store | direct-reuse rate; accuracy | Request-based higher direct reuse |
| B11 (T9) | Lemma writing against held-out gold lemmas | 3 analogous lemmas as templates | Cold lemma writing | match to gold lemma; falsification pass rate | For a frontier model, templates may be worse (Opus 19.4% vs 34.5%); also test token-matched short templates |
| B12 (T10) | Hard items | N = 2, 5, 10, 25 conjectures at fixed total tokens | n/a | accuracy against N | Inverted-U expected; find the peak |
| B13 (T11) | Hard multi-step items | Decomposition depth 0, 1, 2 at equal tokens | n/a | accuracy | Gain at depth 1 and possibly 2; zero on easy |
| B14 (A5) | All runs | n/a | n/a | the lemma funnel (proposed, deduplicated, falsified, checked, used) | Used fraction in the 10-40% range (Rabe 28-89%, TBC 20%, Lemmanaid 22.6%) |

Rules for all lemma tests:
- Blind scoring: whoever scores lemmas does not see which arm produced them.
- Count the cost of proposing, filtering and proving (setup cost).
- Report the leak-allowed run (lemma derived from the known answer) separately as an upper bound (K13).
- Do not feed the lemma-proposing arm the model's earlier answer as a hint (G4, G10).

---

## 9. What does not transfer, and why

- **Training-based gains (STP, Minimo, Gauthier and Urban, Rabe).** They update weights. A scaffold cannot. Only the design lessons transfer: difficulty band, hindsight, diversity re-weighting. STP's own held-out gain is 2-3 points.
- **Days-of-compute systems (Seed-Prover heavy, Hilbert).** 5,000 conjectures and up to 22.8M tokens per hard item (Hilbert); 1,880M tokens on PutnamBench. A bounded agent cannot afford this. G11 says prefer several short attempts. The result also depends on a strong closed reasoner.
- **Kernel-checked proofs.** Lean, Isabelle and HOL Light give a perfect check. In plain text there is no kernel, only small-case computation or code. The formal yields (compile rate, Sledgehammer proof) do not carry over, and models judge counterexamples poorly (CounterMath).
- **Equational conjectures (QuickSpec, TheSy).** They need executable generators and a signature. Plain-text problems rarely have one. The idea transfers (test on random or small inputs, prune what follows from known facts), not the tool.
- **AM and Graffiti heuristics.** Qualitative, no replication, hand-tuned to specific domains.
- **Library size as a goal.** 22,532 LEGO skills for a 3.3-point gain. Our context is limited, and the agent works on single problems or short streams, so a large library cannot be shown.
- **Gold-lemma recall as the metric.** It rewards re-finding human lemmas, and undercounts valid new ones. We care about use in a correct answer.
- **Lemma libraries as a cure for all items.** Gains are largest for mid-strength baselines; they shrink for strong ones and for hopeless ones (TIP15).
- **Mathlib and AFP content.** Contamination: LLMs have seen these libraries, so claimed derivation can be recall.
- **Debate-like multi-agent conjecture voting.** G9 already excludes it.

---

## 10. Open questions

1. At equal tokens, does asking for lemmas inside one reasoning session beat a longer direct attempt? (critique gap 1; no paper)
2. What share of LLM lemmas in plain text are true and used, and how much does a small-case check raise it? (gap 2)
3. How much of the library gain survives de-duplication, a triviality filter and a held-out split? (gap 3; LEGO +3.3 has one split)
4. Does a lemma proposed for one problem help different problems, per-lemma? (gap 4; only same-run reuse is measured)
5. Are Seed-Prover and Hilbert gains due to lemma pools or to stronger models and compute? (gap 5; confound documented)
6. What is the best number of conjectures at fixed budget? (gap 6)
7. Do goal-directed conjectures beat undirected ones? (gap 7)
8. Why do commercial LLMs do worse with templates than with direct writing: prompt length, format or capability? (gap 8)
9. How good is a judge model at deciding whether a conjecture is interesting, new, or trivial? (gap 9; 46% false rejections in one audit)
10. Does symbol renaming expose recall in domains other than drawing? (gap 10; Putnam-AXIOM variants may simply be harder)
11. Is the CPL proof-length increase (KS p=1e-13) harder lemmas or just verbose proofs? (critique)
12. How do TheSy, Hipster and CVC4's built-in conjecturing compare on one shared benchmark with the same time rules? (K16)
13. Do small-case computations predict truth for lemmas that are not about numbers (geometry, combinatorics, logic)?
14. What was the actual hit rate of Graffiti and HR? The numbers we have are second-hand.

---

## 11. Sources

Marker: [V] opened this session (full text or pdftotext of the paper); [M] snippet, abstract, or secondary page only.

| Source | Mark | URL |
|---|---|---|
| Lenat and Brown (1983/84) Why AM and Eurisko Appear to Work (a01, a02, a25, c27) | [V] OCR, noisy; local copy | https://www.aaai.org/Papers/AAAI/1983/AAAI83-059.pdf ; https://www.aaai.org/Papers/AAAI/1983/AAAI83-062.pdf |
| Lenat and Brown (1984) AI journal version (b22) | [M] | https://interlisp.org/history/bibliography/7g8qmm8l/ |
| Ritchie and Hanna (1984) AM: a case study in AI methodology (a03) | [M] abstract | https://researchportal.hw.ac.uk/en/publications/am-a-case-study-in-ai-methodology/ |
| Same, via Wikipedia (b21) | [M] secondary | https://en.wikipedia.org/wiki/Automated_Mathematician |
| Ritchie (1991) Learning from AM (b23) | [M] abstract | https://www.dai.ed.ac.uk/papers/documents/rp522.html |
| Colton, Bundy, Walsh (1999) Automated discovery in pure mathematics (a04) | [V] | https://cgi.cse.unsw.edu.au/~tw/ARW99.pdf |
| Colton (2002) HR thesis/book blurb (b26) | [M] | https://era.ed.ac.uk/items/907e65a9-0410-4e9f-9923-58e572aec62d |
| Graffiti history (DeLaVina) and blog (b27) | [M] | https://www.uhd.edu/documents/academics/sciences/history.pdf |
| Claessen, Smallbone, Hughes (2010) QuickSpec (a05) | [V] | https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quickspec.pdf |
| Johansson and Smallbone (2021) Conjectures, Tests and Proofs (a06, a07, a23, a27, a28, b14) | [V] | https://arxiv.org/pdf/2109.03721 |
| Johansson, Rosen, Smallbone, Claessen (2014) Hipster (a08) | [V] | https://arxiv.org/pdf/1405.3426 |
| Nagashima et al. (2022) Template-Based Conjecturing, TBC (a09, b13, c22) | [V] | https://arxiv.org/pdf/2212.11151 |
| Singher and Itzhaky (2020/21) TheSy (b15, c25) | [V] | https://arxiv.org/pdf/2009.04826 |
| Gamboa, Manolios, Smith, Thompson (2023) Counterexample generation and theory exploration, ACL2 (b20) | [V] | https://arxiv.org/pdf/2311.08857 |
| Davila (2024) The Optimist (b24) | [V] | https://arxiv.org/pdf/2411.09158 |
| Davila (2026) TxGraffiti (b25) | [M] abstract | https://arxiv.org/pdf/2409.19379 |
| Pastorek (2026) AutoGraphForge (c28) | [M] abstract | https://arxiv.org/abs/2609.03478 |
| Kaliszyk and Urban (2014) Learning-assisted theorem proving with millions of lemmas (a11, a24, b16, b17, c26) | [V] | https://arxiv.org/abs/1402.3578 |
| Rabe, Lee, Bansal, Szegedy (2020) Skip-tree training (a10) | [V] | https://arxiv.org/abs/2006.04757 |
| Urban and Jakubuv (2020) First neural conjecturing datasets (b19) | [V] | https://arxiv.org/pdf/2005.14664 |
| Gauthier and Urban (2025) Learning conjecturing from scratch (b18, c20, c21) | [V] | https://arxiv.org/pdf/2503.01389 |
| Poesia, Broman, Haber, Goodman (2024) Minimo (c16, c17) | [M] page summary; figures not seen | https://arxiv.org/abs/2407.00695 |
| Dong and Ma (2025) STP (a16, a17, a26, b10, b11, c14, c15) | [V] | https://arxiv.org/abs/2502.00212 |
| Wang et al. (2024) LEGO-Prover (a12, a13, b08, b09, c01-c03, d06, d07) | [V] pdftotext | https://arxiv.org/abs/2310.00656 |
| Zhao et al. (2023) Subgoal-based demonstration learning; Jiang et al. (2022) Thor (a18) | [M] via LEGO-Prover table | https://arxiv.org/abs/2310.00656 |
| Kasaura et al. (2025) Conjecturing-Proving Loop, v4 (a14, a15, c04-c06) | [V] | https://arxiv.org/abs/2509.14274 |
| Liu et al. (2026) MathlibLemma (a20-a22, b01-b04, c10-c13) | [V] | https://arxiv.org/abs/2602.02561 |
| Alhessi et al. (2025/26) Lemmanaid (b05-b07, c07-c09) | [V] | https://arxiv.org/abs/2504.04942 |
| Johansson and Smallbone (2023) Exploring mathematical conjecturing with LLMs (c23, c24) | [V] | https://ceur-ws.org/Vol-3432/paper5.pdf |
| ByteDance Seed (2025) Seed-Prover (b12, c18, d05) | [V] | https://arxiv.org/abs/2507.23726 |
| Wang et al. (2025) Hilbert (c19, d01-d04, d15) | [V] | https://arxiv.org/abs/2509.22819 |
| Ren et al. (2025) DeepSeek-Prover-V2 (d09) | [V] | https://arxiv.org/abs/2504.21801 |
| Brown et al. (2024) Large Language Monkeys (d08) | [V] | https://arxiv.org/abs/2407.21787 |
| Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? (d10) | [V] | https://arxiv.org/abs/2409.04109 |
| Mirzadeh et al. (2025) GSM-Symbolic (d11) | [V] | https://arxiv.org/abs/2410.05229 |
| Gulati et al. (2025) Putnam-AXIOM (d12) | [V] | https://arxiv.org/abs/2508.08292 |
| Li et al. (2025) CounterMath (d13) | [V] table scrambled | https://arxiv.org/abs/2502.10454 |
| Zhou et al. (2023) Least-to-most prompting (d14) | [V] | https://arxiv.org/abs/2205.10625 |
| Synthesis lines c29, c30, d16 | not sources | n/a |
