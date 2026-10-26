# Proofs and refutations (conjecture refinement): deep document

*Subfield D01.02. Evidence: evidence_a to evidence_d.jsonl (ids a01-a29, b01-b25, c01-c32, d01-d17), claims K01-K34 in claims.jsonl, cross-check in critique.md. Where critique.md corrected a number, the corrected number is used here. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested.*

**Headline.** Lakatos gave a menu of typed reactions to a counterexample. Pease (2007) made it runnable. Nobody has tested the typing against a plain "reflect and fix" loop or against resampling at equal tokens, with a language model or without. What is established is smaller and more useful: a repair loop pays only when the failing evidence comes from code, is located, and is shown to the model; repair is about break-even with fresh sampling, and in formal proving it loses; and repair loops silently weaken the claim.

---

## 1. What it is

Imre Lakatos, *Proofs and Refutations* (1976, from his 1963-64 papers), is a rational reconstruction of how the Euler formula for polyhedra (V - E + F = 2) was refined by counterexamples. Its subject is the loop **conjecture, proof, counterexample, repair, new proof**. It rejects the naive Popper reaction ("a refuted claim is dead") as the weakest of several moves.

Core terms:

- **Conjecture.** A claim, e.g. V - E + F = 2 for all polyhedra.
- **Proof (thought-experiment).** An informal argument split into steps (lemmas). Euler: remove one face, flatten, triangulate, remove triangles one by one.
- **Global counterexample.** A case that refutes the conclusion. The hollow cube has V - E + F = 4.
- **Local counterexample.** A case that refutes one lemma (proof step). The picture frame cannot be flattened in the way the step needs.
- A counterexample can be global only, local only, or both. The type says which repair to use.
- **Hidden lemma.** An unstated assumption in the proof. A global-only counterexample signals one.

Lakatos's reactions (named and ordered in Pease's thesis, a01, b06):

| Method | What it changes | Effect |
|---|---|---|
| Surrender | nothing; claim dropped | the naive Popper reaction |
| Monster-barring | the meaning of a term | the case is "not really a polyhedron" |
| Exception-barring | the claim | the case is excluded by name or by class |
| Monster-adjusting | the reading of the case | reinterpret the object so it fits (not implemented by Pease) |
| Lemma-incorporation | claim and proof | the failing step becomes a stated condition of the claim |
| Proofs-and-refutations (proof-generated concepts) | the concepts | a definition is chosen because the proof needs it |

Why this matters for our agent. SCHEMA.md has one reaction to a failed check: S5 REVISE (show the failing output, fix, at most 2 rounds), then S6 impasse. Lakatos suggests several typed reactions, and "Conjecture refinement" is an open slot in section 7 of the schema. This document asks whether any of that typing is worth adding, and what the evidence says about the surrounding loop.

Scope. Pease's computational model, LLM loops that refine a claim, rule, or proof from counterexamples, and the control question: does the refinement beat resampling at equal tokens? Neighbours covered elsewhere: lemma discovery and conjecturing, conflict-driven clause learning (no-goods), abduction, library learning, anytime search and restarts.

---

## 2. History and theories in depth

### 2.1 Lakatos and his critics

- Lakatos's book has essentially two case studies: the Euler formula and uniform convergence (a14). The method was reconstructed after the fact.
- Lakatos did not claim a single logic of discovery. The subtitle "the logic of mathematical discovery" was added by the editors (a15).
- Surrender takes about 1 of 120 pages in the book. Lakatos treats it as the first, weakest move (a01, a15).
- Feferman (1978) lists ten criticisms (a14, via the thesis): what happened before 1847; whether the method is only for transitional periods; relation to working experience; whether guessing has no end; what counts as improving a proof; where the first proof comes from; the form of conjectures; whether ordinary logic explains the same cases; whether there are no crystal-clear concepts; what is distinctive about mathematics. Hacking (1981) adds that the method is tied to hypothetico-deductive style.
- The one that bites our use: "where does the first proof come from" (vi). Lakatos describes repair of an existing attempt. He says nothing about producing the first attempt. That is our S3 GENERATE. Pease's program also needs a proof scheme given by hand.

### 2.2 Real practice: Martin and Pease (2013)

Martin and Pease checked Lakatos against online mathematical talk (a16, a17, a18, c08). Opened.

- MathOverflow sample: 34% of responses gave explicit examples or counterexamples to conjectures; 37% contained a corrected error; 56% cited literature; 90% of questions received a response flagged as an answer (78% reasonable, 12% partial). Sample size was not stated in the part read; coding was informal.
- Third mini-polymath, 174 comments: examples or counterexamples 33%, conjectures 20%, proofs 14%, concepts 10%, other 23%.
- A misleading word ("windmill", read as a pivoting half-line) produced counterexamples that exposed two readings of one concept. The authors call it monster-adjusting. One object was a supporting example for one person and a counterexample for another.
- Their own caveats: most examples fit Lakatos's categories only "with sufficient ingenuity"; little concept formation was seen on MathOverflow; Lakatos explains how a flawed assumption is repaired, not how it arises. They guess that naming causes misconceptions. This is untested.

Reading: counterexamples are a main currency of real mathematical progress, and a found error is routine. But the typing is not crisp in practice. A typed classifier needs a fixed reading of the terms first (S1).

### 2.3 Werndl: other ways to justify a definition

Werndl (2009; the arXiv copy is dated 2013 in one line, same paper; a19, c09) argues from ergodic theory that Lakatos's proof-generated definition is one of four justifications: proof-generated, natural-world, condition, and redundancy justification. Some definitions are justified two ways (Kolmogorov-Sinai entropy). One case study, philosophical argument. Meaning for us: "redefine the term until the proof works" must not be the only concept repair. A redefinition should also be checked against what the term was meant to describe.

### 2.4 Pease's model: HRL and the six methods (2007)

Pease's PhD thesis (Edinburgh) is the first full program of Lakatos's methods (a01-a15, b01-b06, c01-c07, d01-d04, d17). Opened.

**System.** HRL extends the HR theory-formation program. Each agent is a copy of HR with its own slice of the data. There are students and one teacher. Work alternates between independent phases and a discussion phase. Agents exchange conjectures, concepts, proof schemes and counterexamples, and keep what passes an interestingness threshold. Experiments: 3 students, 10 phases, 10 or 20 theory-formation steps per phase depending on the experiment (the surrender study used 20 steps x 10 phases). Interestingness is a weighted sum of surprisingness, comprehensibility, applicability and plausibility. Domains: group theory, animal taxonomy, number theory. Message order is non-deterministic.

**Why the data split matters.** With one agent holding all the data there is nothing to refute. Disagreement comes from different data, and counterexamples are found by checking, not by arguing. This is close to our G4 and G9 (no debate), but the engine is different: informed copies plus a code check, not persona voting.

**Decision procedure for lemma-incorporation (Algorithm 8, a03, c02).**

1. If the global counterexample also breaks a lemma: global-and-local incorporation. Add the failing lemma's concept to the premise (new claim: C implies Q).
2. Else, if some lemma has a local counterexample and a concept in the theory links the local and global counterexample and appears in a lemma: global-and-local incorporation.
3. Else: hidden-lemma incorporation.
4. No global but a local counterexample: local-only (the conclusion still holds but the reason is wrong; generalise or fix the step).
5. No counterexample: return claim and proof unchanged.

The linking-concept test exists to avoid confusing the hidden-lemma case with the global-and-local case.

**Hidden-lemma search (d04, a04).** The hardest method. Two surprise tests, both built on HR's record of how each concept was constructed (its ancestors):

- Type 1, unexpected behaviour: entity x is surprising for claim P implies Q if there is another claim C of the form P implies (Q and R) for which x is the only counterexample. HR walks the ancestor list of Q to find R. The missing condition is a property every other example has and x alone lacks.
- Type 2, non-meaningful terms: entity m is surprising for P(x) implies Q(x) if not P(m). The statement holds only vacuously (a circle counted as a polygon). Works for one-argument predicates only.

Both are shown on one worked example (Lakatos's cylinder), constructed to match Lakatos. No success rate is reported.

**Monster-barring (a05, a09, a10, b03, c03, d01).** Keep the claim, change what a term means. Hollow cube (V - E + F = 16 - 24 + 12 = 4) is barred by defining a polyhedron as a surface of polygons, not a solid. Two decision points: whether to propose barring an object, and how to answer a proposal. Vague-to-specific mode produced candidate definitions: in group theory they resembled the group axioms (associativity added to exclude groupoid GP2; an inverse condition to exclude semigroup SG1); in number theory a definition requiring a divides a excluded zero.

**Exception-barring (a06, a11, b04, c05).**

- Piecemeal exclusion: generalise a counterexample into a class and exclude it (hollow cube, then polyhedra with cavities, then claim for polyhedra without cavities).
- Counterexample-barring: exclude the named case (a*a*a = a repaired by "a is not 1").
- Strategic withdrawal: the only method that uses positive examples. Generalise from supporting cases (regular, then convex polyhedra) and restrict the claim to that class.

**Surrender (a08, b02, c04, d02, d17).** Five signals for when to give up on a claim: number of earlier modifications (0 to 3), interestingness threshold (0.5, 0.75, 1.0), interestingness compared with the theory average, plausibility threshold (0.7 to 0.9), domain-of-application threshold (0.4 to 0.8). Plausibility is (e - c)/e: e entities the claim talks about, c counterexamples. Example: "all primes are odd" over numbers 1-20 gives (8 - 1)/8 = 0.875.

**Theorem Modifier (Colton and Pease; thesis ch. 12; a12, b05, c06, d03).** The one automated exception-barring pipeline with a checker. Otter tries to prove the claim, then its negation. The model finder MACE builds supporting and falsifying models. HR invents specialisation concepts true of the supporting models. Each is added as a condition and re-proved by Otter. Only proved modifications are shown. A filter flags results as probably uninteresting if only the trivial algebra satisfies the condition or the condition restates the claim.

**What the thesis never did.** Evaluation is by parameter sweeps and by the program's own interestingness measure, plus a philosophical argument against criteria from Thagard, Sloman, Popper and Lakatos (consilience, simplicity). There is no baseline, no external judge, no statistics (a13, b01, b06). Lemma-incorporation has worked examples only. Monster-adjusting is unimplemented. The "problem of content" (over-narrowing) is named as future work (c07, d03).

### 2.5 The 2017 dialogue game

Pease, Lawrence, Budzynska, Corneli and Reed (2017, *Artificial Intelligence* 246) read Lakatos's informal logic as a dialogue game over structured arguments, then induce abstract argumentation frameworks and compute semantics to label what is acceptable (d05). Each formal step is implemented; a worked example on real collaborative mathematics is shown. Only the publisher record and abstract were read (PDF blocked). No quantitative evaluation is described. No LLM version exists.

### 2.6 Related machine lines (not Lakatos-labelled)

- **Conjecture generators with counterexample stores.** Graffiti-family systems; Davila's Optimist (c28) plans a counterexample-hunting "Pessimist"; AutoGraphForge (2026; c27, d16) loops generate, refute, add counterexample to the table, repeat until a round adds nothing.
- **Human-machine discovery.** Davies et al. (Nature 2021) via Davis's review (c10): humans conjectured a bound linking knot signature to slope and volume, built a dataset of about 36,000 knots to look for counterexamples, found some, and revised the bound by adding injectivity radius. The reviewer argues the neural net was used in only 2 of 11 steps.
- **Counterexamples to induction (CTIs).** CIll (c30): in invariant generation, a failed inductive step returns a CTI; the model must propose an invariant that excludes it. This is classic "strengthen the lemma until the proof goes through", i.e. hidden-lemma incorporation with an LLM as proposer.
- **Lemma-level verification.** Ke et al. (2026; a26, c26) on the Gilbert-Pollak Steiner ratio.

---

## 3. Core findings with exact numbers

Numbers are those verified in critique.md where it re-opened the paper; HRL and Theorem Modifier numbers were later checked against the thesis (gap pass, d01-d04, d17). Status: E, S, C as in SCHEMA.md.

### 3.1 Pease / HRL (all single source, one lab, self-scored)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Best reaction to a refuted claim, on average, was surrender at the first counterexample | modification limit 0 among best; limit 3 worst (-12 on the hierarchy score); 42 sessions = 14 per domain x 3 domains | Pease 2007 (a08, b02, d02) | S |
| Relative value beats absolute thresholds as a surrender signal | hierarchy score: interestingness vs theory average 14; compare-to-average 12; zero modifications 8; plausibility 0.7 scored 7 | Pease 2007 (d02) | S, circular outcome |
| Remaining scope ("domain of application") was not a useful surrender signal | no reported benefit across 0.4-0.8 | Pease 2007 (d02) | S |
| Monster proposal is accurate when scored by author's list | group theory 82-100%, animals 94-100% (platypus found), number theory 97% | Pease 2007 (a09) | S; the 97% is degenerate (nothing flagged; 0 and 1 missed) |
| Barring minimum is not one constant | single-agent runs up to 30-40% good; multi-agent 0-10% good, 10% hypothesised best; mixed runs best at 40-50% each (sum 120-150%); coded default 15% | Pease 2007 (d01) | S; do not carry any threshold |
| Reaction to monster proposals worse than proposing | 82-88% correct in sessions 69-75 (group theory) | Pease 2007 (a09) | S |
| Monster-barring yields useful definitions | group-axiom-like (associativity excludes GP2; inverse excludes SG1); a|a excludes zero | Pease 2007 (a10) | S |
| How a counterexample is generalised matters | number theory modification by counterexample-barring scored 0.508 (surprisingness 1/61, plausibility 1); another by piecemeal exclusion 0.016; group theory modifications 0 to 0.941 over 17 groups | Pease 2007 (a11) | S, preliminary |
| Theorem Modifier repairs invented non-theorems | 83% of 98 got a valid modification, 3.1 per item; 7 of 9 (78%) real TPTP non-theorems; HR 3000 steps, Otter and MACE 10 s | Pease 2007 ch. 12 (a12, d03) | S; no baseline; non-theorems made by deleting axioms, so repairs may undo the corruption |
| Hidden-lemma surprise tests | one worked example (cylinder); no rate | Pease 2007 (d04) | S |
| No baseline exists for any of the above | three hypotheses (tunable methods), 3 domains, no control arm | Pease 2007 (a13, b01) | E (two readings agree) |

### 3.2 Human practice

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Counterexamples are a main currency | MathOverflow: 34% of responses gave examples or counterexamples, 37% had corrected errors, 56% cited literature; mini-polymath: 33% of 174 comments | Martin and Pease 2013 (a16, a17) | S |
| Definitions are justified in more ways than proof-generation | 4 kinds from one case study | Werndl 2009 (a19) | S |
| Real counterexample refinement used a purpose-built search set | about 36,000 knots; net predicted signature at 78%, slope alone also 78% | Davis 2021 review (c10) | S |

### 3.3 Self-correction and repair in language models (the evidence that carries weight)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Without an external check, self-correction does not help and can hurt | GPT-3.5 GSM8K 75.9 / 75.1 / 74.7 (standard / round 1 / round 2); CommonSenseQA 75.8 / 38.1 / 41.8; GPT-4 GSM8K 95.5 / 91.5 / 89.0; with oracle labels 84.3, 89.7 (GPT-3.5), 97.5 (GPT-4 GSM8K); GPT-3.5 kept first GSM8K answer 74.7% | Huang et al. 2024 (b07, b08, c17); Kamoi et al. 2024 (b10, c19) | E |
| Locating the fault is the bottleneck, not fixing | best model GPT-4 finds the mistake 52.87% overall; 300 traces (255 wrong, 45 right); with true location, backtracking +23.53 on wrong traces and -11.11 on right ones (one task row, tracking shuffled objects); random location +11.76 fixed, 15.56 broken | Tyen et al. 2024 (b09, c18) | S (K08), consistent with ProcessBench |
| Executable or tool feedback gives gains that model-only feedback does not | CRITIC (EM, AmbigNQ / TriviaQA / HotpotQA): CoT 44.2 / 67.4 / 33.7; no tool 42.0 / 67.3 / 34.9; with tool 50.0 / 72.7 / 38.7; Self-Debug MBPP GPT-4 72.8 to 80.4 with unit tests, to 76.4 without execution; Reflexion HumanEval 91.0 vs 80.1 | Gou 2024; Chen 2024; Shinn 2023 (b13, b16, b11, c20, c21) | E |
| Repair is about break-even with fresh sampling in code | GPT-4 APPS: 10 drafts + 1 repair each = 1.05x pass@20; 2 drafts + 10 repairs each = 0.97x; human feedback 52.60% repaired vs GPT-4 feedback 33.30% | Olausson et al. 2024 (b14) | S (K10); cell labels uncertain per critique |
| In formal proving, repair loses to fresh restart at equal tokens | Lean MiniF2F sequential pass@64: Qwen 44.5% repair vs 62.8% retry; DeepSeek-Prover-7B 24.5% vs 75.3%; at 200k tokens repair trails by 25.9 and 73.5 points; repair prompt about 9.1k input tokens vs 115 | Repair, Retry preprint (d06) | S (preprint, 11 problems) |
| Self-correction ahead at small budgets, restarts ahead at large | PutnamBench: 57 (self-correcting prover) vs 48 at pass@32; 93 at pass@2048 vs 86 | Pythagoras-Prover (d08) | S, system-to-system |
| Repair pays when the error is local and mechanical | correct diagnostic +34.0 pp (Lean-3 syntax), +26.5 pp (unknown identifier); +4.3 and +4.0 elsewhere; repair 29 solved vs retry 35 | Repair, Retry (d07) | S; subgroups, reader-computed |
| A self-written check can pass wrong answers | Reflexion MBPP Python false-positive rate 16.3% vs 1.4% on HumanEval; MBPP 77.1 vs 80.1 baseline | Shinn 2023 (b11, b12) | S |
| Propose-test-refine of rules needs a symbolic interpreter | ACRE 64.0 direct, 65.0 self-consistency, 70.0 self-refine (LM interpreter), 78.2 (T=1,N=1), 82.5 (T=3,N=5); task accuracy 28.0 to 59.0; MiniSCAN task accuracy 0.0 to 70.0 (T=3,N=5); List Functions 65.1 to 62.4; MiniARC 33.1 to 18.7 | Qiu et al. 2024 (b18, b19, c22) | S |
| Refinement mostly adds an exception for the failing example | quote: "adding exceptions for a specific example, rather than starting from entirely new hypotheses" | Qiu et al. 2024 (b19) | S |
| Many explicit hypotheses tested as code beat direct prompting on ARC | GPT-4, 100 tasks: direct 17, program only 23, LLM-summarised hypotheses 30, human-selected 33, human-written 45; feedback rounds 0 to 3: 24, 28, 28, 30 | Wang et al. 2024 (b20, c23) | S |
| Self-feedback on math says "looks good" | ChatGPT feedback "everything looks good" in 94% of math cases; GPT-3.5 math 64.1 vs 64.1; repair introduces a new problem in 20% of sampled failures | Madaan et al. 2023 (b15) | S |
| Training can fix self-correction; prompting cannot | Gemini 1.5 Flash MATH: base 52.6 to 41.4 (-11.2); SCoRe 60.0 to 64.4 (+4.4); 15.8% of correct answers turned wrong at baseline | Kumar et al. 2024 (b17) | S, needs training |

### 3.4 Counterexample finding in language models

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Models solve problems they cannot falsify | REFUTE (324 samples, 304 authors): best RandSearch 8.3% (o3-mini high); 4.0 / 3.7 / 4.0 for other models; solve rates up to 44-48.7%; with the correct solution given 15.1% (DeepSeek-V3), 9.9% (R1); 35% of all RandSearch samples end in an invalid counterexample (86% of those from wrong brute-force code) | Sinha et al. 2025 (a22, c16, d14) | S |
| University counterexample use is weak below frontier reasoning models | COUNTERMATH (1,216 pairs; annotation agreement 95.4%): 7B models about 30 F1; Qwen2.5-Math-72B 41.8; GPT-4o 59.0; o1-preview 60.1; R1 80.7 | Li et al. 2025 (a20, b21, c15) | S |
| Small SFT gain | 1,025 samples: F1 38.3 to 41.1 (+2.8); strict 30.2 to 31.1; examples used 74.2 to 79.4%; hint prompt about +1.4 F1 | Li et al. 2025 (a21, c15) | S |
| Counterexample-only training breaks truth recognition | Qwen3-4B, n=201: Pass@1 base 0.30, SFT 0.35, RLVR 0.50 (paired delta +0.199 [0.13, 0.27]); true-theorem recognition 0.27 to 0.00 after SFT (4 seeds, also Gemma-3-4B); SFT asserted FALSE on 70% of true theorems | Zouak et al. 2026 (a23, a24, c14) | S, preprint |
| Dropping a hypothesis gives cheap false conjectures with known counterexamples | 575,039 candidates from 212,463 seeds; SymCE 4,707 items from 6,748 theorems, verifier 173/177 = 97.7% | Li et al. 2026; Zouak et al. 2026 (a23, a25, c13) | E (two groups) |
| LLM conjecture-then-prune is low yield | 757 outputs, 420 unique; 109 (25.95%) refuted by GAP code; 40 (9.52%) no counterexample; 271 (64.52%) code did not run | Chuharski et al. 2024 (a27, c12) | S |
| Locating the first wrong step by reading is weak; formal evidence is better but costly | ProcessBench GPT-4o F1 79.2 / 63.6 / 51.4 (GSM8K / MATH / OlympiadBench) vs o1-mini 93.2 / 88.9 / 87.2; FaithSieve (Qwen3.5-9B, 200 items): formal 61.0 exact vs direct 51.0, majority of 241 samples 51.0, reviewer panel 52.0, challenge-and-defence 55.5 at 124% tokens; about 152x tokens | ProcessBench (d09); FaithSieve (d10) | S (K25) |
| Planted wrong claims are corrected when labelled as outside work | adoption of a planted wrong claim about 83% from own thought vs at most 3.3% from an external role; correction +23 to 93 points; self-distrust prompts 0-23.3% | Self-Correction Illusion (d13) | S, 30 tasks per cell |

### 3.5 Silent change of the claim

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM-assisted proof work drifts | 16 of 100 original declarations changed, including a theorem weakened to assume three of its four requirements | Isabelle contract paper (d11) | E with the two lines below |
| Models alter the problem statement to make it easier | seven failure modes; "Problem modification" listed; fix: word-by-word statement-integrity check | QED (c32) | E (with d11, d12) |
| Repair loops keep 15-45% meaning drift | 150 traffic and 77 wildlife statute rules; equivalence 44.7% to 85.3% after up to 3 repair rounds; NLI drift 16.2% (equivalent) vs 28.7% (non-equivalent); 13/14 equivalent rules faithful on human check | Round-trip autoformalisation (d12) | E (K26) |

### 3.6 Lemma and invariant repair, counterexample stores

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Lemma-level iteration with code verification certified progress | Steiner ratio bound 0.824 to 0.8559 (conjectured 0.866); no improvement over 10 rounds with bottleneck reflection removed | Ke et al. 2026 (a26, c26) | S |
| A counterexample store pays in round 1, then collapses | store 2,860 graphs; round 1 +494 to 793 witnesses (20-28%); round 2 +39 to 164; round 3 +3 to 21; four partitions stopped at round 5, one at round 9; merge removed 1,413 refuted by other shards' witnesses | AutoGraphForge (c27, d16) | S |
| CTI-guided invariant generation | 222 RISC-V instances; baselines solved 146, 76 left; solved all remaining PicoRV32 and NERV cases except the M extension; not serv | CIll (c30) | S |
| Persistent false-positive control for many weak checks | Type-I error held at 0.1 in 6 domains; ReAct and CodeGen baselines did not control it | POPPER (c31) | S |

---

## 4. Mechanisms and models

Each mechanism is written so an engineer can code it. "Code" means the program in SCHEMA section 1; "model" means a slot-filling call.

### 4.1 The base loop

```
state: claim C, proof as numbered steps L1..Ln (if any), case base X (positive examples), counterexample store K
loop:
  find counterexamples to C and to each Li           # code: run, enumerate, mutate, search
  if none: stop, return (C, proof)                    # a search that fails leaves C standing (a24)
  type each counterexample                            # code (4.2)
  choose a repair by type                             # code (4.2)
  model writes the repair, shown the failing output   # G2
  re-check on: the new counterexample, the old store K, held-out cases
  accept only if all pass and the statement-fidelity check passes (4.6)
```

Three properties of this loop have measured support: the check is code (E), the failing output is shown (E), the old counterexamples are re-run (b15: repair introduces a new fault in about 20% of sampled failures).

### 4.2 Typing a counterexample (Pease, Algorithm 8)

Inputs: counterexample x, claim C (premises P, conclusion Q), lemma list L1..Ln each with a testable statement.

```
global = (P(x) and not Q(x))                 # x satisfies premises, breaks conclusion
local_i = (premise of Li holds on x and Li's result fails on x)   # x breaks step i
if global and any local_i:         type = BOTH
elif global and linked-concept:    type = BOTH   # a concept ties the local and global counterexample
elif global:                        type = GLOBAL_ONLY  (hidden lemma)
elif any local_i:                   type = LOCAL_ONLY
else:                               type = NONE
repair:
  BOTH        -> add the failing lemma's condition as a premise of C
  LOCAL_ONLY  -> fix step i (or generalise it); keep C
  GLOBAL_ONLY -> search for the hidden condition R (4.5); add R to proof and claim
  NONE        -> return unchanged
```

Precondition: the proof must be written as separately testable steps. This is the main practical cost for informal solutions (K02). Open point: in Martin and Pease's data one object was a counterexample to one reader and a support to another (a17), so the terms must be fixed first (S1 restatement).

### 4.3 Exception-barring and monster-barring as code

- **Counterexample-barring.** Claim C becomes "C and x is not the case". Cheap, can leave a claim with no content.
- **Piecemeal exclusion.** Find a predicate F true of x and of other failing cases and false of supporting cases (the Theorem Modifier idea: examples on both sides, name a class that separates them). New claim: "C for all cases not satisfying F". Check on held-out cases.
- **Strategic withdrawal.** Find a predicate G true of all supporting cases. New claim: "C for cases satisfying G". Also check on held-out cases.
- **Theorem Modifier pattern.** Counterexamples and supporters from a checker; the proposer names a restricting condition; a prover or executor re-checks the restricted claim; a filter drops conditions that are trivial or restate the claim.
- **Monster-barring.** Keep the claim, add a definition check: bar x only if x fails a stated definition of the concept, and write the new definition into the answer. Pease's cheap proposal score is the share of accepted claims the object breaks: an object that breaks many beliefs is probably outside the domain (a09). The thresholds differ by experiment (3.1) and do not transfer.

### 4.4 Surrender and the cost of content

Signals Pease tested, all cheap counts on a stored case base (d02, d17):

- plausibility = (e - c)/e, e = stored cases the claim covers, c = counterexamples among them;
- relative value = claim's score divided by the average over open claims;
- number of repairs already made (a cap, not a predictor);
- remaining scope = share of stored positive cases still covered. Pease listed this as the "domain of application" and it was not useful in his data, but his thesis separately proposes a coverage meter against the problem of content (c07). Untested.

Engineering reading: a repair cap (2 to 3 rounds), then restart from the original problem. The LLM evidence (d06, d08) supports "repair a few rounds, then restart" more than any Pease threshold.

### 4.5 Hidden-lemma probes (three candidate prompts)

- **Odd-one-out (Pease type 1).** Find a property R such that x is the only case violating "P implies Q and R". Code can test candidate R against the case base.
- **Vacuity (Pease type 2).** For each step, check whether the antecedent is false on x (the step holds only vacuously).
- **Plain question.** "What did the proof assume that the claim does not state?"

No study compares them (K30).

### 4.6 Statement-fidelity guard

After every repair, diff the claim and its assumptions against the original. Allowed outcomes: unchanged; or a strict restriction that is written out as an explicit condition. Reject anything else. Evidence: Isabelle audit, QED's word-by-word check, and the round-trip method (d11, d12, c32). It works in case studies; the cost to repair success is unmeasured.

### 4.7 Counterexample store

Keep every counterexample found for this problem class (and within a run). Re-run each revised claim against the store before spending a new search. Evidence is graph theory only: most new witnesses arrive in round 1, yield collapses, a round with no new witness is the stop signal; a shared store matters (1,413 refutations missed by separate shards). Whether this saves LLM tokens is unmeasured (K32).

### 4.8 Refute with a third-party framing

Present the draft in a fresh context as an outside submission and ask for a located failure. Planted-error evidence: adoption 83% (own) vs at most 3.3% (external), and "treat as ground truth" raised acceptance to 70% (d13), so the framing must say "unverified".

### 4.9 Locate before repair

Prefer an executor. Where none exists, a reasoning-mode critic with a challenge-and-defence structure is the best reading-only method found (+4.5 over direct at 124% tokens), still 5.5 below the formal pipeline at about 1/150 of its tokens (d10).

### 4.10 Stop rule for a repair loop

Candidates: a round that adds no new counterexample (fixed point; d16); repair cap; plausibility below a threshold; coverage below a threshold. Only the first has an independent dynamics study. None has been tested on an LLM.

---

## 5. What holds up

### 5.1 Replicated or multi-source

- **No gain from self-critique without an external check** (K07, E). Huang et al., Kamoi et al. (survey), CRITIC's no-tool ablation, Self-Refine (94% "looks good"), and Tyen et al. agree. Boundary: Huang's tasks are reasoning with simple prompts; fine-tuned models (SCoRe) can learn positive self-correction.
- **Executable feedback is the active ingredient** (K09, E). CRITIC ablation isolates the tool; Self-Debug and Reflexion add to it; Kamoi's survey agrees.
- **Models fix well once the location is shown, and find locations poorly** (Tyen; ProcessBench; FaithSieve). Reasoning-mode models read far better than chat models (GPT-4o 51.4 vs o1-mini 87.2 on OlympiadBench).
- **Repair drifts the claim** (K26, E). Three independent audits.
- **Hypothesis-dropping as a source of false claims** (K17, E). Two groups.
- **No Lakatos-labelled LLM loop has been compared with resampling** (K22, E as an absence): Pease's own evaluation has no baseline, and our searches found none.

### 5.2 Single-source or contested

- Typing by global/local (K01), surrender-at-zero (K03), restart beating repair in Lean (K24, two preprints from different groups but both formal), break-even in code (K10), FaithSieve costs (K25).
- Break-even versus loss: Olausson finds about break-even in code (1.05x and 0.97x); the Lean papers find repair clearly worse. The settings differ (informal and executable tests vs a formal verifier), so this is a moderator, not a contradiction. Do not generalise either one.
- Dense versus sparse reward in SymCE: equal on the counterexample benchmark, differing by 33 +/- 8 points on a truth probe under the training-style prompt (critique.md). Both statements are true.

### 5.3 Failures and limits

- **Self-written checks end the loop on wrong answers.** Reflexion MBPP false positives 16.3% vs 1.4% (K11).
- **Exception patching.** Refinement adds "unless" clauses instead of new rules (Qiu). It fails when the first rule was wholly wrong, and MiniARC fell from 33.1 to 18.7 with refinement.
- **Counterexample-only training over-refutes** (Zouak): true-theorem recognition 0.27 to 0.00; SFT model said FALSE on 70% of true theorems. A prompt-only analogue is expected but not measured.
- **Prompting alone does not install the habit.** A hint prompt gave about +1.4 F1 on COUNTERMATH (c15).
- **Check harness failures dominate.** 64.52% of generated GAP programs did not run (Chuharski); 35% of REFUTE random-search samples ended in an invalid counterexample. Fix the harness before judging ideas.
- **Conjecture generators repeat.** Mean cosine self-similarity 0.22 to 0.42; more trials did not raise diversity (c12). LeanConjecturer gave more varied output when all prior conjectures were in context (c24).
- **Lakatos fit is subtle.** Martin and Pease: most examples fit "with sufficient ingenuity".

### 5.4 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Feedback source (code vs model) | code helps, model does not | b07, b13, b16 |
| Located vs unlocated feedback | located helps | b09, d07 |
| Error type (local mechanical vs structural) | repair pays for local mechanical (+34.0, +26.5 pp vs +4.3, +4.0) | d07 |
| Budget size | repair ahead at small budgets, restart ahead at large | d08, d06 |
| Verifier cleanness | formal verifier made repair worse than restart | d06 |
| Role label | external role raises correction | d13 |
| Model type | reasoning models locate and falsify much better | d09, a20 |
| Domain | symbolic interpreter available (ACRE) vs pattern grids (MiniARC) | b18 |

### 5.5 What worked as an intervention and what did not

Worked: code feedback shown to the model; located faults; unit tests (Self-Debug +7.6 on MBPP GPT-4); a symbolic interpreter for rule refinement (ACRE 64.0 to 82.5); hypothesis list plus execution (ARC 17 to 30); structured failure reports (Steiner bound); statement-diff check (case study).

Did not work or not shown: self-critique without a check; prompted slow-down or self-distrust (0-23.3% correction); additional reading votes for localisation (majority of 241 samples = 51.0, same as direct); debate as a counterexample hunter (Huang: debate does not beat self-consistency at equal responses); SFT on counterexamples alone.

---

## 6. Language models

### 6.1 What models do on these tasks

1. **They propose rules and claims they cannot apply or falsify.** Models solve problems up to 44-48.7% on REFUTE yet find counterexamples for under 9%. Giving the correct solution raises this only to 15.1% or 9.9%.
2. **They keep wrong answers in a loop they cannot grade.** GPT-3.5 on CommonSenseQA fell 75.8 to 38.1; changes go more often right-to-wrong than wrong-to-right.
3. **They locate faults poorly and fix them well** (GPT-4 52.87% overall location accuracy; backtracking with the true location +23.53 on wrong traces).
4. **They patch with exceptions** (Qiu) which is exception-barring by default, and they change the claim quietly (Isabelle 16 of 100 declarations; 15-45% statute drift).
5. **They over-refute after counterexample training** (70% FALSE on true theorems).
6. **They take a claim as true when it sits in their own turn and test it when it is labelled as someone else's** (83% vs at most 3.3% adoption), but an "assume this is ground truth" label raised acceptance to 70%.

### 6.2 What changed performance, by how much

| Change | Effect | Source |
|---|---|---|
| External tool vs none in critique | +8.0 / +5.4 / +3.8 EM over the no-tool variant (50.0 vs 42.0 etc.) | CRITIC |
| Unit-test feedback vs none | GPT-4 MBPP 80.4 vs 76.4 (and 72.8 base) | Self-Debug |
| Symbolic interpreter vs LM interpreter | ACRE 82.5 vs 70.0; MiniSCAN task accuracy 70.0 vs near zero | Qiu |
| True location vs random location | +23.53 fixed vs +11.76 fixed (broken 11.11 vs 15.56) | Tyen |
| Human feedback vs GPT-4 feedback for repair | 52.60% vs 33.30% repaired | Olausson |
| Correct diagnostic vs shuffled (Qwen, Lean) | +18.2 pp [+8.2, +28.2]; DeepSeek about 0 | Repair, Retry |
| Retry vs repair (Lean, 200k tokens) | repair behind 25.9 and 73.5 pp | Repair, Retry |
| Formal evidence vs reading for first-error location | 61.0 vs 51.0 exact; +10 at 152x tokens | FaithSieve |
| External role vs own turn | correction +23 to 93 points | Self-Correction Illusion |
| RLVR with code verifier vs base on counterexamples | Pass@1 0.50 vs 0.30 | SymCE |
| Hypothesis list + code vs direct (ARC) | 30 vs 17 (100 tasks) | Hypothesis Search |
| Hint prompt "reason by example" | about +1.4 F1 | COUNTERMATH |

### 6.3 Cautions on the LLM evidence

- Many papers use different models, so cross-paper rankings are suggestive only (critique.md).
- 2026 preprints (SymCE, Learning to Disprove, Ke, Repair-Retry, FaithSieve, Self-Correction Illusion, Isabelle, round-trip, QED, CIll) are recent, unreviewed, mostly single groups. Learning to Disprove was rejected from ICLR 2026. Weight them low.
- The Lean restart finding is from a clean formal verifier and 11 sequential problems. Informal conjecture repair may differ.
- The evidence supports the pieces (executable feedback, location, calibration) but not the Lakatos typing itself. No test of global/local typing, lemma-incorporation or monster-barring with an LLM exists.

---

## 7. What our agent should take

Key to the schema parts: **G** guardrail, **S** state, **O** operator, **memory** = SCHEMA section 5. Ids refer to evidence lines and claims.

### 7.1 Add now (established [E])

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | A revision is driven by a failing output produced by code (a test, a run, an enumerated counterexample), never by the model's opinion. Already G2; the evidence for the repair loop specifically confirms it. | G2 (confirms) | [E] | b07, b08, b10, b16, c17, c19; K07, K09 |
| A2 | Repair prompts include the located failing output and the exact step or input that fails, not a bare "incorrect". | S5 | [E] for "executable and specific feedback beats generic"; location part [S] | b09, b13, b15, c11, c26; K09 |
| A3 | A found counterexample is added to a regression set and every later revision is re-run on it, plus on held-out cases. Repair introduced a new fault in about 20% of sampled failures. | S5, S8, G3 | [E] for held-out/regression; the 20% figure is single-source | b13, b15, G3 |
| A4 | Statement-fidelity check: compare the final claim with the original; allow only unchanged or an explicit written restriction; log every change. | new guardrail candidate G13 or part of S8 | [E] that drift happens (3 sources); [S] that the check preserves repair success | d11, d12, c32; K26 |
| A5 | A found-nothing search leaves the claim standing; never convert "no counterexample found" into "claim is false", and never treat it as proof either. Test sets for the refute step must contain true claims. | G3, S7, S4 | [E] by G3 plus K16 (single-source) and K11; mark the false-refutation evidence [S] | a24, b12, c14 |
| A6 | Do not use a self-written check as the stopping rule unless it was written independently of the answer and run on held-out cases. | G3 | [E] with K11 as [S] number | b12, b11 |
| A7 | Equal-token control: any repair or refute loop must be compared with best-of-N resampling and fresh restart at the same total tokens, counting input tokens. | G7 (applied) | [E] as practice; sizes are [S] | b14, d06, d08; K10, K24 |
| A8 | Present generic self-critique as not to add (already in 4b). No change. | 4b | [E] | b07, b10 |

### 7.2 Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Typed repair.** Force a type label (global-only / local-only / both) by running each written step on the failing case, then choose the repair by type. | O refute / S5 sub-routine | [S] design from Pease; [D] for LLMs | a02, a03, c02, d04; K01 |
| T2 | **Stepwise solution as state.** Require numbered, separately checkable steps so a counterexample can be located. | S2/S3 output format | [S] | a02, b09, c18; K02 |
| T3 | **Repair-then-restart.** Cap repair at 2 to 3 rounds, then restart fresh from the original task; decide by error type (repair local mechanical errors, restart structural ones). | S5, S6, G12 | [S] (two preprints, formal setting) | d06, d07, d08; K24, K33 |
| T4 | **Worth-saving gate.** Before any repair, compute plausibility and relative value on stored cases; drop or restart cheap low-value claims. | G12 / S5 | [S] circular outcome | a08, b02, d02, d17; K03, K29 |
| T5 | **Coverage meter.** Track the share of original positive cases still covered after each repair; reject repairs below a threshold. | S5, memory | [S] proposal only | c07, a06, d17; K04 |
| T6 | **Patch counter.** Count exception clauses added to a rule; at a set count force a fresh rule. | S5, S6 | [S] | b19, c22; K12 |
| T7 | **Third-party framing for the refute pass.** Fresh context, draft labelled as an unverified outside submission. | O refute, G4 | [S] | d13; K27 |
| T8 | **Code-run counterexample search** (enumerate small cases, random and mutated inputs, brute-force compare) instead of asking the model to "think of a counterexample". | O refute, S7 | [S] for LLM falsification being weak; the code-search gain itself unmeasured | a22, c16, a20; K14 |
| T9 | **Locate by executor where possible; otherwise a reasoning-mode critic with challenge-and-defence.** | S5 | [S] | b09, d09, d10; K08, K25 |
| T10 | **Hidden-lemma probes** (odd-one-out, vacuity) against "what did the proof assume?". | O refute | [S] one worked example | d04; K30 |
| T11 | **Persistent counterexample store** for the problem class. | memory | [S], no LLM test | c10, c27, d16; K19, K32 |
| T12 | **Monster-barring guard.** Allow redefinition of a term only with an explicit written definition and a definition check; log it. | S1, G3 | [S] | a05, a10, c32; K06 |
| T13 | **Hypothesis list plus execution on rule-induction items** (ARC-style), at most 3 feedback rounds. | S3/S4 | [S] | b18, b20, c23; K12, K13 |
| T14 | **Fixed-point stop**: stop repairing when a round produces no new counterexample. | S6 | [S] dynamics from graph theory | c27, d16; K32 |

Not recommended to carry over: any Pease threshold number (barring minimum, interestingness thresholds, HR step counts), the 97% number-theory score, and the label "Lakatos method" as a reason to add anything. Our measurements overrule the literature (SCHEMA 8.3).

---

## 8. Concrete tests on our bench

All arms get the same total tokens, including input tokens of repair prompts (FaithSieve and Repair-Retry show input tokens can dominate). Report per-item logs per SCHEMA section 6. Seeded item sets are built by hypothesis-dropping (K17): take a verified rule or theorem, drop a condition, and the broken case is a known counterexample.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 | **Seeded false rules and claims** (ARC-like rules, small number-theory or set claims, with a known counterexample and a known repaired version). Also include true claims. | (a) plain answer; (b) best-of-N resampling; (c) untyped reflect-and-fix with the failing output; (d) typed repair (T1) with code-computed type; (e) typed, with model-assigned type | final claim correct and fidelity-checked; false-refutation rate on true claims; repair success per round | (d) over (c) small, if any; (c) about equal to (b). Prediction: typing helps only on items where steps are separately checkable. Break-even is the default. |
| B2 | **Seeded flawed proofs / worked solutions** with one wrong step (word sorting, shuffled objects style traces; small algebra proofs) | (a) model locates then fixes; (b) executor locates then model fixes; (c) true location given (upper bound); (d) restart | step-location accuracy; fix rate; break rate on right traces | (b) well above (a); (c) +20 or more; restart competitive at equal tokens. |
| B3 | **Repair vs restart schedule** on items with a clean checker (code, unit tests; a small formal set if available) | (a) pure restart; (b) repair 2 rounds then restart; (c) repair 5 rounds; (d) repair by error type (local mechanical repair, structural restart) | pass at equal total tokens | (b) at or above (a) at small budgets, (a) ahead at large; (d) above (c). |
| B4 | **Surrender gate** on a stream of generated claims with a cost per claim | (a) always repair; (b) always drop and regenerate; (c) repair only if plausibility >= 0.7 and relative value >= 1 | useful true claims per token | (c) over (a) if the cheap signals predict repair success; if plausibility does not predict it, drop T4. |
| B5 | **Silent drift** on seeded claim sets with fixed original text | (a) repair loop with no check; (b) same plus statement diff check; (c) same plus a prompt "do not change the statement" | share of final claims whose statement differs from the original; repair success | (a) shows drift in a non-trivial share (expect 10 to 20%, per audits); (b) removes it with at most a small loss in success; (c) removes little. |
| B6 | **Exception pile-up** on rule-induction items where the first rule is wrong | (a) free refinement; (b) refinement with a patch counter forcing a fresh rule at 2 exceptions; (c) fresh sampling | accuracy | (b) over (a) where the first rule is wholly wrong (MiniARC-style items); no gain where it is nearly right. |
| B7 | **Refute pass framing** on planted-error drafts and on drafts that are correct | (a) same-turn reflect; (b) fresh context, draft labelled as an outside unverified submission; (c) fresh context, no label | detection of planted errors; false-refutation rate on correct drafts | (b) above (a) on detection; watch for more false refutations. |
| B8 | **Counterexample finding**: REFUTE-style items plus correct-solution negatives, COUNTERMATH True items | (a) prompt only; (b) prompt plus code execution; (c) code-run brute-force compare scaffold | find rate on false items; recall on true items (false-refutation rate); per-class report | (c) above (a) on find rate; check the false-refutation rate stays low. Cap from REFUTE: best prompt 8.3%. |
| B9 | **Hidden-lemma probes** on proofs with a known hidden assumption | (a) "what did the proof assume?"; (b) odd-one-out probe; (c) vacuity check per step | share of items where the probe names the hidden condition | open; small differences likely. |
| B10 | **Counterexample store** over a problem class with repeated claims | (a) rederive each time; (b) shared store re-run first | tokens spent on rederived refutations; rounds to fixed point | (b) saves most in round 1; expected positive if claims repeat across items. |
| B11 | **Hypothesis list plus execution** on ARC-like rule items | (a) direct; (b) one program; (c) 4 hypotheses, executed, up to 3 feedback rounds | accuracy | (c) above (a) by several points; most of the gain in the first feedback round (24 to 28 of 30 on Wang's curve). |

Baseline for all: the thinking-mode baseline from SCHEMA section 7 (does one extended-thinking attempt already beat this graph). Run it first on the same items.

---

## 9. What does not transfer, and why

- **Pease's numbers.** Barring minimum, interestingness thresholds, step counts and the 97% score come from three toy domains, a self-defined interestingness measure and the author's list of expected monsters. They do not transfer to LLM tasks.
- **Multi-agent HRL.** The disagreement came from agents holding different data. A single model with persona copies does not reproduce it (G4, G9). Huang et al. found debate no better than self-consistency at equal response count.
- **Lakatos as a source of first ideas.** The method repairs an existing attempt. It does not produce the first proof or the first conjecture (Feferman criticism vi). Our S3 and open mode need other sources (analogy, grounding).
- **Philosophical evaluation.** Consilience and simplicity arguments (thesis ch. 11) are not performance evidence.
- **Training results.** SymCE RLVR, SCoRe, Learning to Disprove and COUNTERMATH SFT change weights. We only scaffold. They matter as bounds: counterexample drill alone can break truth recognition.
- **Formal verifier dynamics.** The Lean restart-beats-repair result has a verifier that gives a clean diagnostic and a memoryless alternative. Informal repair may behave differently.
- **Graph-theory store dynamics.** Cheap witnesses over 348,207 test graphs and 1.22 CPU-years do not carry to language-model token costs.
- **Mathematical typing in open domains.** The global/local type needs a claim and steps that a program can run. For judgement tasks, advice and open writing there is no counterexample to compute. G8 governs those.
- **Interestingness as an outcome.** Pease's outcome was the agents' own interestingness (circular). We use external correctness.
- **Human mathematical talk.** Social proofs on MathOverflow involve experts, literature (56% cited) and long-running threads, none of which our single agent has.

---

## 10. Open questions

1. Does typing a counterexample (global/local/both) and repairing by type beat an untyped reflect loop and a best-of-N control at equal tokens? (No study; the main test, B1.)
2. What cheap signal says "surrender now"? Pease's signals are untested outside his self-scored runs. Plausibility, relative value, coverage and error type are the candidates (B3, B4).
3. How far can a claim be narrowed before the repair is empty? No measured threshold; coverage meter is a proposal.
4. Can an LLM locate the failing step without an executor at acceptable cost? Reading methods gain 0.5 to 4.5 points over plain judgement at equal tokens; formal pipelines about 10 at 152x tokens.
5. How often do repair loops silently change the claim on a seeded set, and does a diff check preserve repair success?
6. Do the Pease hidden-lemma surprise tests have an LLM equivalent that beats the plain question?
7. What did the 2017 dialogue-game paper find in its worked example, and did anyone evaluate challenge-and-response against a plain list? Only the abstract was read.
8. Do Theorem Modifier results replicate with a modern prover and an LLM proposing the restriction? No study.
9. Does a persistent counterexample store cut wasted refutation rounds for an LLM?
10. Is break-even (code repair) or loss (Lean repair) the general case for informal conjecture repair? The Lean result came from 11 sequential problems per model.
11. Are the 2026 preprints reproducible? All are single groups.
12. Does the external-role framing effect (d13) survive natural (non-planted) errors?
13. Is monster-barring ever the right move for an LLM agent, or should it always be treated as drift? No measure of when redefinition helps.
14. What is the real false-refutation rate of a prompt-only agent on true claims? COUNTERMATH can supply it; no direct rate is reported.

---

## 11. Sources

[V] = opened and read this session or the gap pass (critique.md re-opened 12 of them). [M] = snippet or abstract only, or cited second-hand.

**Lakatos and its formalisations**
- [V] Pease (2007) A Computational Model of Lakatos-style Reasoning, PhD thesis, Edinburgh. https://era.ed.ac.uk/handle/1842/2113 ; PDF copy https://www.exeter.ac.uk/research/groups/education/pmej/pome27/Pease%20%20A%20Computational%20Model%20of%20Lakatos-style%20Reasoning.pdf (chapters 9, 10, 12, 13 read in the gap pass; numbers in the first pass not all re-opened by critique)
- [M] Lakatos (1976) Proofs and Refutations. Cited only through the thesis.
- [M] Feferman (1978) criticisms of Lakatos; Hacking (1981); Larvor (1998). Cited only through the thesis (a14, a15).
- [V] Martin and Pease (2013) Mathematical practice, crowdsourcing, and social machines. https://arxiv.org/abs/1305.0900
- [V] Werndl (2009) Justifying Definitions in Mathematics, Going Beyond Lakatos. https://arxiv.org/abs/1310.1625 (dated 2013 on the arXiv listing; same paper)
- [M] Pease, Lawrence, Budzynska, Corneli, Reed (2017) Lakatos-style collaborative mathematics through dialectical, structured and abstract argumentation, AI 246. https://www.research.ed.ac.uk/en/publications/lakatos-style-collaborative-mathematics-through-dialectical-struc (abstract page only; PDF blocked)
- [M] Colton and Pease (2004) Theorem Modifier. Cited through the thesis chapter 12.
- [V] Davis (2021) review of Davies et al. https://arxiv.org/abs/2112.04324
- [V] Chen and Jiang (2026) Lectures on AI for Mathematics. https://arxiv.org/abs/2604.11504 (loop description only)

**Self-correction and repair**
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them given the error location. https://arxiv.org/abs/2311.08516
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297 (abstract, introduction and structure)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Chen et al. (2024) Teaching Large Language Models to Self-Debug. https://arxiv.org/abs/2304.05128
- [V] Olausson et al. (2024) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738
- [V] Kumar et al. (2024) SCoRe. https://arxiv.org/abs/2409.12917
- [V] Repair, Retry, and the Cost of Hindsight (2026). https://arxiv.org/html/2610.22698
- [V] Pythagoras-Prover (2026). https://arxiv.org/pdf/2606.12594
- [V] The Self-Correction Illusion (2026). https://arxiv.org/html/2606.05976v1
- [V] Chen et al. (2024) ProcessBench. https://arxiv.org/pdf/2412.06559
- [V] FaithSieve (2026). https://arxiv.org/html/2608.26310v2

**Rule induction and hypothesis search**
- [V] Qiu et al. (2024) Phenomenal yet puzzling: inductive reasoning with hypothesis refinement. https://arxiv.org/abs/2310.08559
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660

**Counterexample generation and conjecturing**
- [V] Li et al. (2025) COUNTERMATH. https://arxiv.org/abs/2502.10454
- [V] Sinha et al. (2025) Can Language Models Falsify? REFUTE. https://arxiv.org/abs/2502.19414
- [V] Zouak et al. (2026) Counterexample Generation via Per-Theorem Symbolic Verifiers (SymCE). https://arxiv.org/abs/2610.02444
- [V] Li et al. (2026) Learning to Disprove (rejected from ICLR 2026). https://arxiv.org/abs/2603.19514
- [V] Chuharski et al. (2024) Mining Math Conjectures from LLMs: A Pruning Approach. https://arxiv.org/abs/2412.16177
- [V] Onda et al. (2025) LeanConjecturer. https://arxiv.org/abs/2506.22005
- [V] Pastorek (2026) AutoGraphForge. https://arxiv.org/abs/2609.03478
- [V] Davila (2024) The Optimist. https://arxiv.org/abs/2411.09158
- [M] Dong and Ma (2025) STP self-play provers. https://arxiv.org/abs/2502.00212 (abstract numbers from a search summary)

**Lemma, invariant, proof-agent loops**
- [V] Ke et al. (2026) Gilbert-Pollak via LLMs. https://arxiv.org/abs/2601.22365
- [V] Zheng et al. (2023) Lyra. https://arxiv.org/abs/2309.15806
- [V] Su et al. (2026) CIll. https://arxiv.org/abs/2602.23389
- [V] Huang et al. (2025) POPPER automated hypothesis validation. https://arxiv.org/abs/2502.09858
- [V] An et al. (2026) QED. https://arxiv.org/abs/2604.24021
- [V] Woodcock et al. (2026) Contract-Aware Rescue of a Drifted Isabelle Development. https://arxiv.org/pdf/2608.18822
- [V] Faithful Autoformalization via Roundtrip Verification and Repair (2026). https://arxiv.org/html/2604.25031
