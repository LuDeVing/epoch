# Inductive logic and ILP: deep document

*Subfield D03.09. Key works: Muggleton. Why it matters: represent and generate rule candidates (S2, S3). Built from evidence_a-d.jsonl, claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids (a01 ... d20) point to those files. No equal-token comparison exists anywhere in this literature; every LLM effect size below is an upper bound for a fixed budget.*

## 1. What it is

Inductive logic programming (ILP) learns a logic program (a set of rules) from examples plus background knowledge (BK). The input is positive examples, negative examples and BK. The output is a hypothesis that covers the positives and none of the negatives. The result is readable and can be run.

Inductive logic in the wider sense is the study of how a finite set of cases supports a general rule. For our agent the useful part is narrow and concrete:

- A rule is a small program that a computer can run on every example.
- A candidate rule is scored by counting: examples explained, examples violated, rule length.
- Search over rules is guided by what failed, not by retrying blind.

Claimed strengths of ILP (Cropper et al. 2021; a04, a07, c13): data efficiency (often one example), reuse of BK, recursion, predicate invention (naming new helper concepts), readable output. Claimed weak spots: noise, scale, raw perception, hand-made BK and language bias.

Why this matters for the schema. S2 (represent) asks the model to write 1 to 4 candidate rules. S3 (generate) produces attempts. S4 (test) runs them. ILP is the mature field that already solved "generate rules, test by counting, use the failures". The LLM literature of 2023 to 2026 redid this with a language model as generator and code as tester. That is the core of this document.

## 2. History and theories in depth

**Setting.** Muggleton (1991) named the field (a09, not opened; setting taken from the 2021 survey). Muggleton and De Raedt (1994) gave the formal frame (a10, not opened): search over clauses ordered by generality (theta-subsumption), with refinement and inverse resolution. Rule A is more general than B if A covers everything B covers. That order lets a search prune. If a rule is too general (covers a negative), all its generalisations are also bad. If it is too specific (misses a positive), all its specialisations are bad.

**Search families** (a05, b05):
1. Top-down: start general, specialise. Can learn recursion. Wasteful.
2. Bottom-up: start from examples, generalise (Golem, relative least-general generalisation). Fast. Long hypotheses. Hard for recursion and invention.
3. Progol / inverse entailment (Muggleton 1995, a11, not opened): build the most specific clause that entails one seed example (the bottom clause), then search between it and the empty clause with A*. A prompt analogue: write the most specific rule that explains this one case, then generalise.
4. Meta-level: encode learning as a solver problem (ASPAL, ILASP, Popper).

**FOIL (Quinlan 1990; a01-a03).** Greedy covering. Add one literal at a time, choose by an information-gain score, stop when a clause costs more bits than it explains. Needs negatives. Cannot invent predicates. Capped at 128 constants in the 1990 implementation.

**Meta-interpretive learning (Muggleton, Lin, Tamaddoni-Nezhad 2014/15; a23, not opened).** Higher-order templates (metarules), for example chain: P(A,B) :- Q(A,C), R(C,B). Learning means filling the template variables. This gives recursion and predicate invention. Metagol is the system. It is "almost useless" without good metarules (a06). It does not remember failed clauses (a24).

**Popper (Cropper and Morel 2021; a12-a13, b01-b04).** Generate, test, constrain. A solver proposes a hypothesis in a bounded space. It is run on the examples. Failure gives constraints: too general prunes all generalisations, too specific prunes all specialisations. Repeat. This is the template for our loop.

**Differentiable ILP (Evans and Grefenstette 2018; a14-a15, b07-b08).** Clauses get learned weights, trained by gradient descent over fuzzy truth values. Tolerant to label noise. Memory heavy. Arity at most 2. Not a model for our agent (b08).

**Noise handling (MaxSynth, Hocquette et al. 2023; b11-b12).** Replace "fit all examples" by a minimum description length trade-off: program size against training errors, solved as MaxSAT. The authors say that "ILP cannot do noise" is unfair. The hard case is noise plus recursion plus invention.

**Ultra-strong machine learning (Michie 1988; Muggleton et al. 2018; d16-d17).** A learner is ultra-strong if its output makes a human perform better than from the examples alone. That tests a rule as a communication object, not only as a predictor.

**Reuse and one-shot induction (Lin et al. 2014 MetagolDF; d18).** Learn earlier tasks, keep the invented predicates, and later programs get smaller and faster to find. This is the ILP ancestor of a rule store.

**2020s turn: LLMs as the generator.** From 2023 the generator is a language model and the tester is code (Hypothesis Search a16, Qiu a18, HtT c01; then ALBI c16, which replaces Popper's ASP generator with an LLM). Rule induction from words (DEER, a20) moved ILP-style tasks into natural language. 2025 to 2026 benchmarks (SLR-Bench b22, PBEBench d02, InductionBench d04) ask how far this goes.

**Competing views.**
- ILP developers: symbolic, exact, data efficient, brittle on noise and raw input (a07).
- LLM view: the model's priors make proposals cheap; verification does the rest (LLM-PV d14).
- Neighbour-based view (MIRAGE a22): LLMs often answer new cases by similarity to seen cases, not by the rule. A right answer is not proof of a right rule.

## 3. Core findings with exact numbers

Status key: E = established in claims.jsonl (2+ independent sources), S = single source, C = contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| FOIL learns relations from tuples with a counted score | Family relations: 78 of 80 test cases correct over 20 trials (neural net 7 of 8), 11 s per trial. Chess endgame, 100 training positions: FOIL 92.5% (sd 3.6, 1.5 s), CIGOL 77.2% (21.5 h), DUCE 33.7% (2 h). 1000 positions: FOIL 99.4% (sd 0.1, 20.8 s), DUCE 37.7% | a01, a02 | E (K01) |
| Learning from failures beats enumeration | Evens program: Enumerate 159 s vs Popper 4 s. Buttons task, 10 required buttons: Popper solves it; Enumerate manages 3 (p=20) and 1 (p=200) | a12, a13, b01 | E (K02) |
| ILP backends scale very differently | Metagol falls to 50% default accuracy near 10,000 examples; Popper fine at 20,000; ILASP failed to ground. List length 50 and 500: Popper under 1 s, Metagol 20 s and 54 s | a13, b02 | E (K03) |
| Classical ILP breaks under label noise; MDL helps | Popper and Aleph struggle from 10% noise. MaxSynth works to about 30%: beats Popper on 25 of 42 tasks, ties 13, loses 4 (p<0.01). iggp-rps with noise: Popper and Aleph under 55%, MaxSynth over 90%. dILP perfect on 5 of 6 tasks at 10% mislabelling | b11, b07, a15 | E (K04) |
| MML vs C-MDL scoring (no LLM) | No significant difference on 30 tasks or at 10-50% noise. MML better in all 12 few-example or one-sided conditions (20 and 50 examples), significant in 11 of 12. Can learn from positives only | d09, d10 | S (K24) |
| LLM hypothesis, then program, then test beats direct output (ARC, GPT-4, 100 tasks, top-1) | Direct 17%, program only 23%, LLM-summarised hypotheses 30%, human-selected 33%, human-written 45%, Icecuber DSL search (no LLM) 43%. 1D-ARC 39.6 / 61.1 / 73.1. List Functions (100) 31 / 59 / 69. SyGuS (89) 94.3 with or without hypotheses | a16, a17, b18, c07 | S (K05; all one paper) |
| Hypothesis quality is the bottleneck | GPT-4 had a correct hypothesis for 49 of 100 ARC tasks. With a human-selected hypothesis 33 of 49 (67%) gave a correct program. Parab 2025 (GPT-4o, 100 list tasks, 64 samples): generator correct 46.4%, summariser 34.5%, implementor 61.2%, overall 62.0%. Summariser keeps only 74% of correct hypotheses (12.1 point absolute loss). Implementor rescues 19.9% of trials where both earlier steps failed | a16, b19, c08, d06 | E (K06) |
| Mean test accuracy vs humans, same 100 list tasks | Humans 0.521 (sd 0.202); hypothesis search 0.487 (sd 0.326); direct GPT-4o 0.359 (sd 0.309) | d07 | S |
| Refinement with a symbolic interpreter (GPT-4) | Task accuracy: ACRE 28.0 (IO) to 59.0 (T=3, N=5); MiniSCAN 0.0 to 46.0 (T=3, N=1; raw 77.0; up to about 95 with a symbolic parser); List Functions 39.6 to 52.0. Self-refine with the LM as interpreter: ACRE 32.0. Majority vote 29.0 vs 28.0 | a18, b14, c04 | S (K07) |
| Refinement can hurt | MiniARC raw accuracy 33.1 direct vs 5.9-18.7 refined. SIRBench: Gemini-2.5-Flash 43.81 to 39.06, GPT-4.1 32.41 to 33.25, Claude-3.5-Haiku 31.53 to 31.63 | b14, c04, d11 | E (K08) |
| Induce/apply gap | MiniSCAN task accuracy above 80% with a symbolic interpreter, near 0 when the LM applies its own rules. Altered arithmetic at 512 shots: GPT-4o-mini deductive 71.4 vs inductive 47.8; GPT-5 inductive 87.2 vs deductive 83.7 | b15, c05, d12 | C (K09) |
| Writing the rule vs running it | GPT-4 reaches accuracy 1 in most SolverLearner cases when code runs the induced function; zero-shot GPT-3.5 about 0.03-0.12 in bases 8, 9, 11 | c11 | E (K17) |
| Noise fragility | Noise on 12.5%, 25%, 50% of 8 exemplars: drop even at one noisy example; telling the model reduces but does not remove it. DeepSeek-R1 at 10% noise: List Functions CoT 76.0 to 68.4 (-7.6), SRR 83.6 to 78.0 (-5.6); Atbash CoT 0.0 accuracy change but only 70.0 consistency | b16, c06, d08 | E (K10) |
| Rule library from verified rules | CLUTRR, GPT-4: CoT 50.6 to HtT 64.3. GPT-3.5: 21.2 to 37.6; with GPT-4 rules 48.4. Random rules: 9.9. Wrong rules cause 65% (CLUTRR) and 81% (base-16) of CoT errors. Base-16 library precision 98.5, recall 92.2. List Functions task accuracy 46.0 to 56.2 | c01, c02, c03 | S (K11) |
| LLM plus logic engine on relational chains | CLUTRR 8-10 hops terminal accuracy, CoT to Popper-ly: Qwen-3.5 4B 19.09 to 61.93; Gemma-4 E4B 14.39 to 62.74; LLaMA-3.2 3B 18.72 to 42.48; Claude Sonnet 4.6 56.92 to 71.38; GPT-5.4 59.91 to 75.09. GPT-4 on IsUncle 49.05% vs 60k-parameter DLM 100% | c18, b24, c23 | E (K12) |
| LLM + ILP loop iterations | ALBI, 30 Popper tasks, all 100% success: 1.4-1.7 iterations vs Popper 6.8. Wall time: Popper 81.8 s, Gemini 333.6 s, Claude 397.7 s, GPT 1631.9 s. Anonymising predicate names: iterations x1.36-1.67; zendo2 11-17 vs 1-7 | c16, c17 | S (K13) |
| Predicate invention needs a verifier | Nine poker concepts: ILP alone 0/9; unverified LLM 58%; self-critique 73%; Prolog verification 80%; without knowledge pool 67%. Pool gain up to +31 points, but -9 on flush | c19 | S (K14) |
| LLM vs classical ILP under noise | Large LLMs F1 about 0.25 higher than Popper on average, about 3 orders of magnitude faster. No LLM beat Popper on CHAIN. GPT-4o 21x Llama3-8B at noise 0.1. GPT-4o and GPT-3.5 errors 0% syntax / 100% logic; Gemma-7B 100% syntax. No gain beyond about 3 iterations | a21, b20, b21, c21 | S (K15) |
| CoT and reasoning models on induction | MIRAGE GPT-4o: CoT lowers accuracy by up to 18% and 22%. SLR-Bench: CoT adds about 5%; o3 basic/easy/medium/hard 99/93/74/45; GPT-4o to o3 doubles accuracy for +1777% tokens, +1034% cost. PBEBench-Lite: Qwen3-32B 1.8 without CoT vs 41.9 with CoT; GPT-5 72.4; gpt-oss-120b 62.5 | a22, b22, d02 | C (K16) |
| Equal calls: sampling vs repair (ARC-AGI public test) | 6,000 calls. Qwen2.5-Coder-14B 5.63 sample to 14.25 sample+refine; 32B 12.63 to 19.87; Qwen2.5-72B 12.88 to 25.25; Mistral-Large-2 18.50 to 25.62 | d01 | S (K21) |
| Longer thinking vs more samples | gpt-oss-120b on PBEBench: longer thinking beat more samples at matched compute | d02 | S (K22) |
| Candidate count scales as 1/p | k >= log(2/delta) / (-log(1-p)). Measured p about 0.46 (GPT-4o list functions). LLM-PV: IsPrime 100% test accuracy from 200 examples where SGD transformers fail with 100k. Sketch-and-Verify (code, 19 hard problems): diverse K=2,M=5 recovers 11/19 vs flat N=10 5/19; K=10,M=10 15/19 vs flat N=100 10/19 | d06, d14, d15 | E (K23) |
| Induction and transduction cover different ARC tasks | Ensemble 56.75% (2 tries) vs average human 60.2%; later 61.9% | c12 | E (K18) |
| Rule chain length is a wall | PBEBench hard set under 5% for GPT-5 and gpt-oss-120b. InductionBench: o3-mini compatibility 5.69% (log-weighted 33.93%), R1-Distill-70B 0.78%, Llama-3.3-70B 0.12%. More examples stop helping as window k grows; slightly lower accuracy with more examples in PBEBench | d02-d05 | E (K26) |
| ILP backend matters in hybrids | ILP-CoT on CLEVR-Hans (Qwen-7B): direct 51.60, custom CoT 35.85, ILP-CoT 81.85. Backend: Popper 46.74, Metagol 81.85, ILASP timeout. ARC-AGI-1 GPT-4o: 5.25 direct, 9.25 CoT, 10.25 ILP-CoT | b25, c24 | S |
| Human studies of ILP rules | Rule acquisition group n=22: 1 wrote the correct rule; mean score 1.76 to 5.24 after seeing Metagol rules, t(21)=7.63, p<0.001. Naming predicates: Grandfather 6.68 correct vs 5.15 incorrect. One-shot string induction about 61% vs humans 87% (cyphered) / 74% and FlashFill 76%. Complex theories hurt: win_3 fell, p=0.005 | d16-d18, b10 | E (K25, K19) |
| Rules from agent traces as guards | AutoSpec, 291 traces: F1 0.98 and 0.93, up to 94% fewer false positives, 4-5 iterations | c20 | S (K20) |

## 4. Mechanisms and models

Written so that an engineer can build them.

### 4.1 Counted coverage score (FOIL, Popper)
For a candidate rule r and example set E (positives P, negatives N):
- covered_pos = number of p in P with r(p) true. violated = number of n in N with r(n) true.
- score = covered_pos - violated (or F1). With noise, use score = covered_pos - violated - lambda * length(r). Length is tokens, literals or AST nodes (MDL style, b11).
- Run r as code. Never let a model judge whether r covers an example (b15: the proposer cannot apply its own rule).
- Held-out check: split examples into fit and hold-out. A rule that fits all fit examples but fails the hold-out is rejected (G3).

### 4.2 Generate, test, constrain (Popper) as an agent loop
```
constraints = []
repeat until budget:
    h = LLM.propose(examples, constraints_as_text)      # fresh context
    result = run(h, examples)                            # code
    if result.all_pass: return h
    for e in result.missed_positives: constraints += "must cover e (last rule too specific)"
    for e in result.covered_negatives: constraints += "must not cover e (last rule too general)"
    constraints += "do not repeat the shape of h"
```
Popper's real constraints prune whole families by generality. The cheap prompt equivalent is the exact failing example, the direction of the failure, and a forbidden rule shape. ALBI (c16) does this with Prolog: 1.4-1.7 iterations vs 6.8 for ASP-based Popper.

### 4.3 Hypothesis search (Wang et al.)
1. Ask for N natural-language hypotheses (they used 64).
2. Optionally summarise to M (8). Warning: the summariser lost 26% of correct hypotheses in Parab's test (d06). Prefer dedupe in code by behaviour on the examples.
3. Turn each hypothesis into a program. Run on the training examples with up to 3 rounds of execution feedback.
4. Keep programs that pass. Apply to the test input. Tie-break by shortest or by agreement on fresh inputs.

### 4.4 Induction versus transduction (c12)
Run two routes: write a program (induction) and predict the output directly (transduction). Choose by counted fit on the training pairs. Induction wins on exact computation and composition. Transduction wins on fuzzy perception.

### 4.5 Rule library (HtT, c01)
Phase 1: on labelled training items, the model writes rules. Run each. Count how often each rule is used and how often the answer is right. Keep rules above a usage and precision threshold. Phase 2: put the library in the prompt for new items. The library must be verified: random conclusions drop GPT-4 from 50.6 to 9.9 (c02).

### 4.6 Candidate-count rule (LLM-PV, d14)
If p is the chance that one proposal is a correct rule, you need k >= log(2/delta) / (-log(1-p)) proposals to find one with confidence 1-delta. With p = 0.46 and delta = 0.05: k >= 3.69 / 0.616 = 6. With p = 0.05: about 72. Estimate p on a few probe items before setting N. Dedupe by behaviour on the examples so that N counts distinct candidates (d15).

Caveat: the bound says nothing about selection. If many wrong rules also fit the examples, picking the right one is the next bottleneck.

### 4.7 Template constraint (metarules)
Give the model a rule-shape template (chain, identity, recursion, "for all x in list: f(x)") and ask it to fill the slots. ILP-CoT (c24) uses the LLM to propose structure and Metagol to fill it. This narrows the space. It is also the main ILP failure when the templates are wrong (a06).

### 4.8 Predicate invention with a verifier (ADVENT, c19)
The model proposes a named helper concept. Code runs it on the examples. Keep it only if it separates positives from negatives or shortens the final rule. Keep the number of helpers small. Forget unused ones (Forgetgol, a06: irrelevant BK hurts).

### 4.9 Noise handling
- Leave-one-out: drop each example in turn. If dropping one example lets a much shorter rule fit, flag that example as suspect.
- Diverse subsets (SRR, d08): induce from several subsets, keep the rule with the best execution score overall.
- MDL pick among candidates: score = errors + lambda * length.

## 5. What holds up

**Holds up (2 or more independent sources):**
- Counted scoring of rules by running them as code works. ILP (FOIL, Popper, Metagol) and LLM hybrids (Qiu, Wang, ALBI) agree (K01, K17).
- Failure-driven constraints beat blind retry (K02). The LLM-loop evidence for fewer iterations is single-source (K13).
- Hypothesis quality, not code writing, limits LLM induction. Wang and Parab agree (K06).
- Refinement without a code check is little or no help. On perceptual or fuzzy tasks it can hurt (K08: Qiu MiniARC, SIRBench).
- Noise hurts both ILP and LLM rule induction (K04, K10).
- Chain depth is a wall (K12, K26).
- Number of distinct candidates needed scales roughly as 1/p (K23).
- A rule library only helps if its rules are right (random rules: -40.7 points, c02; one source).

**Failures, boundary conditions and competing explanations:**
- SyGuS: hypotheses gave no gain over programs (94.3 both), because plain code search already worked (a17). The abstract-rule step pays only when the rule is hard to see.
- MiniARC: refinement worse than direct (33.1 vs 5.9-18.7). Perceptual task, text grids.
- SIRBench: refinement changed accuracy by -4.75 (Gemini), +0.84 (GPT-4.1), +0.10 (Haiku). Fuzzy scientific outputs make "fit the examples" a weak check. Non-reasoning models only.
- Parsel helped with human hypotheses (47.5%) and hurt with LLM hypotheses (b18).
- Overfitting by refinement: on MiniSCAN, T=3,N=1 beat T=3,N=5 (a18).
- Self-consistency alone did not help (ACRE 29.0 vs 28.0).
- CoT: MIRAGE says CoT lowers induction accuracy by up to 22%. SLR-Bench says about +5%. HtT uses CoT as baseline and still wins by adding rules. Probable moderator: inducing an unseen rule (CoT can hurt) vs applying stated rules (CoT helps). No paper tests both in one setup.
- More compute is not monotone: o4-mini-high vs o4-mini on SLR medium tier 40% vs 52% (b23). Gandarela: no gain beyond about 3 refinement iterations. PBEBench: more examples slightly lower accuracy.
- Reusing earlier predicates hurt on flush (-9, c19). Multi-task reuse in Metagol needs forgetting (a06).
- Neighbour-based reasoning (MIRAGE): right answer without right rule. Score the rule on cases far from the examples.
- Induce/apply gap is contested: strong for GPT-4 on MiniSCAN, absent for GPT-5 on altered arithmetic (but that test is implicit induction). Small models (Llama3 8B) revert to normal arithmetic and get worse after 128 shots (d13).
- ALBI's 100% is a ceiling on Popper's own noise-free benchmark, which the models may have seen. Anonymising predicate names costs iterations (x1.36-1.67), so part of the speed comes from word meaning.
- Cost: ALBI uses fewer iterations but is 4 to 20 times slower in wall time than Popper (per-iteration cost 10 to 100 times higher). Gandarela says LLMs are about 1000 times faster. Different tasks and baselines.

**Interventions that worked:** run the rule in code; propose several hypotheses in words first; execution feedback up to 3 rounds; verified rule library; Prolog verification of invented predicates; diverse (not flat) candidates; hybrid with a symbolic backend (ILP-CoT with Metagol); length-penalised scoring when examples are few.

**Interventions that did not:** self-refine with the LM as interpreter; majority vote alone; summarising many hypotheses into few; telling the model about noise (reduces the drop, does not remove it); unverified invention; refinement on perceptual or fuzzy tasks; more examples when the hypothesis space is large.

**Human evidence (small, not LLM).** Machine-learned rules help people when simple and fail when complex (win_3 p=0.005, b10; one study had 4 vs 9 students). LLM-written explanations of ILP strategies gave no advantage (c27: 150 recruited, subgroup effect only). Does not transfer to the agent.

## 6. Language models

**Direct behaviour.**
- GPT-4 era (2023): good at proposing rules, poor at applying them. ACRE task accuracy 28.0 with direct output; MiniSCAN 0.0.
- The pool contains the right rule in under half of tries for GPT-4 and GPT-4o (49 of 100 tasks; 46.4% of 64-sample trials).
- Brittle to noise: with 10% noise accuracy can stay level while individual answers flip (R1: 0.0 change, 70% consistency).
- Big models make logical errors, not syntax errors (GPT-4o 0% syntax). Small models make syntax errors (Llama3-8B 46%, Gemma-7B 100%).
- On CLUTRR chains, frontier models fail on a missing inverse relation (75-78%). Small models fail on a wrong rule (43-49%) (c18).
- Word meaning helps. Renaming predicates to p0, p1 raised iterations x1.36-1.67 but kept 100% success (c17).

**What changed it, by how much.**
- Run code on the rule: ACRE 28.0 to 59.0; MiniSCAN 0.0 to 46.0; SolverLearner near 1.0.
- Hypothesis then program: ARC 17 to 30 (33 with a human picking).
- Test and repair at equal calls: ARC-AGI 12.88 to 25.25 (72B).
- Reasoning models: PBEBench Qwen3-32B 1.8 to 41.9 with CoT; GPT-5 72.4. SLR hard level 45-46 for o3 and gpt-5 (do not quote a GPT-4o hard score; the cell is ambiguous). o3 costs +1777% tokens over GPT-4o.
- Verified rule library: CLUTRR 50.6 to 64.3.
- Symbolic step check on CoT: CLUTRR 8-10 hops, Claude Sonnet 4.6 56.92 to 71.38; GPT-5.4 59.91 to 75.09; small models +24 to +48.

**Walls for 2025-26 models.** PBEBench hard cascades under 5% for GPT-5. InductionBench best compatibility 5.69%. A 20-rule cascade is near zero for gpt-oss-120b even at 16,384 tokens and 32 samples. More examples do not move these walls.

**Caveats.** Most evidence uses GPT-4 or GPT-4o (2023-24). 2026 reasoning models appear only in SLR-Bench, PBEBench, InductionBench, ALBI, Popper-ly and MATHEMAGIC. No study compares hypothesis-plus-test, CoT and best-of-N at equal tokens.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Run candidate rules as code against every example. Never let the model judge coverage.** Part: S4, G2, G3. [E] Evidence: b14, b15, c04, c11, a13 (K01, K17).
2. **Score candidates by counted fit (covered minus violated), with a held-out part.** Part: S4, S7. [E] Evidence: a01, a02, b02, a18 (K01).
3. **Turn each failure into a located, directional message for the next attempt ("this example is not covered: too specific" or "this negative is covered: too general") and forbid the failed rule shape.** Part: S5, O. [E] Evidence: a12, a13, b01, c14, c16 (K02). The LLM-loop evidence is single-source (c16).
4. **Spend effort on hypothesis recall and selection, not on code writing.** Part: S2, S3. [E] Evidence: a16, b19, c08, d06 (K06).
5. **Do not refine blindly. Keep the best first-pass candidate and revert if refinement lowers held-out fit. Skip refinement when no code check exists.** Part: S5, G2. [E] Evidence: b14, d11, d05 (K08).
6. **Allow for noise: do not discard a rule on one failing example when labels may be wrong; flag suspect examples.** Part: G3, S4. [E] Evidence: b11, b07, b16, d08 (K04, K10).
7. **Set the number of candidates from an estimate of p, and dedupe by behaviour.** Part: S3. [E] Evidence: d06, d14, d15 (K23).
8. **On long chains of interacting steps, hand step checking to code (hop-count trigger). Do not trust the model to track long relation chains.** Part: S6, O3 (decompose). [E] Evidence: c18, a21, d02-d05 (K12, K26). The trigger threshold itself is untested.
9. **Run both routes (program and direct answer) and choose by counted fit.** Part: S3, S7. [E] Evidence: c12, a16 (K18).
10. **Keep a best-so-far candidate with partial fit; do not copy ILP's all-or-nothing exact fit.** Part: G6. [E] Evidence: b03.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Hypothesis-then-program at equal tokens vs plain CoT and best-of-N, current reasoning model | S2, S3 | [S] | a16, b18, d01, d07 (K05, K21) |
| Verified rule store across tasks (kinship and arithmetic only so far) | memory | [S] | c01-c03 (K11); wrong-rule propagation unknown |
| MDL-style fit-minus-length pick in an LLM loop under 10-30% noise | S7 | [S] | d09, d10, b11 (K24) |
| Predicate invention with code verification | S2 | [S] | c19 (K14) |
| Fresh-context application call vs code execution (induce/apply gap), current models | S3, S4 | [C] | b15, d12 (K09) |
| One long thought vs several short attempts for rule induction | G11, S3 | [C] | d02, a22, b22 (K16, K22) |
| Rule-shape template (metarule) in the prompt | S2 | [S] | c24, a06 |
| Cheap signal for when refinement will hurt | G, S5 | [S] | b14, d11, d05 |
| Anonymised concept names to test reliance on word meaning | S4 | [S] | c17, a22 |
| Failure-class constraints on the agent's own failed attempts (Popper style) | S5, S6 | [S] | a12, c16, d19 |
| Rules from agent traces compiled into guards | memory, G | [S] | c20 (K20) |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (prompts, outputs and any feedback). Items are types, not files.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-like grid and list-function items with a code check and a held-out example | A: plain CoT. B: best-of-N by consistency with training pairs. C: 3-4 hypotheses, then code, run, repair up to 2 rounds | Held-out exact match | C above B by at least 5 points on items with an executable check; no gain on easy items (cf. SyGuS) |
| T2 | Same items, 10% and 25% planted wrong labels | A: accept-if-all-fit. B: fit minus lambda*length. C: leave-one-out suspect flagging | Held-out accuracy | B or C recovers about half the noise loss (R1 lost 5.6-7.6 at 10%); a null result is plausible (d09) |
| T3 | Kinship or relation-composition items, 6-10 hops | A: CoT. B: CoT plus code step-checker over a small verified rule set. C: model writes the whole chain as a program | Final accuracy by hop count | B above A, gap grows with hops (Popper-ly +15 to +48) |
| T4 | Rule-induction items with a rule-application step (MiniSCAN style) | A: model applies own rule. B: fresh-context application call. C: code applies | Task accuracy | C above B above A for non-reasoning models; B close to C for current reasoning models (d12) |
| T5 | Mixed items: executable check vs fuzzy or perceptual-like | A: first pass only. B: always refine. C: refine only if held-out fit improves, else revert | Accuracy and token cost | C equals or beats A and B; B loses on fuzzy items (MiniARC, SIRBench) |
| T6 | Rule-induction items, N in {2, 4, 8, 16} candidates deduplicated by behaviour | Same token budget split into N candidates vs fewer longer attempts | Recall of a correct rule in the pool; top-1 selection accuracy | Recall rises as 1-(1-p)^N; selection becomes the bottleneck once recall passes about 80% |
| T7 | Items with an HtT-style rule store | A: no store. B: verified store. C: store with 20% wrong rules | Accuracy and tokens including store cost | B above A; C well below B (propagation) |
| T8 | Items where the agent's own attempts fail twice | A: plain resample. B: resample with located failing example and forbidden shape. C: B plus "too general / too specific" tag | Rounds to solution at equal tokens | B and C need fewer rounds than A (Popper 159 s vs 4 s; ALBI 1.4-1.7 vs 6.8) |
| T9 | Items that allow a helper concept (multi-condition rules) | A: direct rule. B: invented helpers, unverified. C: helpers run against examples before use | Accuracy; helpers used | C above B, at or above A (58 / 73 / 80 in ADVENT) |
| T10 | Rule items with anonymised concept names | A: original names. B: anonymised | Accuracy | Small loss expected (ALBI iterations x1.4-1.7). A large loss means reliance on word meaning |

## 9. What does not transfer, and why

- **Exact-fit search over a fixed language (Popper, Metagol, ILASP).** Needs a hand-made language bias and BK. Our agent works on open tasks. Use the loop, not the solver (a06, b08).
- **Differentiable ILP.** Memory use, arity at most 2, one task solved in only 30% of seeds (a14, b08).
- **Training results (SLR fine-tuning, MATHEMAGIC fine-tuning, induction finetuning).** The agent does not train (b23, d13).
- **Human cognitive-window studies (b10, c27, d16, d17).** Small samples, humans. Only useful if we show rules to a human.
- **ALBI 100% results.** Noise-free, Popper's own suite, possibly seen in training. A ceiling.
- **Wall-clock claims.** "LLMs 1000 times faster" (GPU vs CPU) and "ALBI 4-20 times slower" are not our metric. Our metric is tokens.
- **ARC-specific large-sampling gains (Icecuber, 20k-program ensembles).** Not available at equal tokens.
- **Clean-label deterministic benchmarks (SolverLearner, LLM-PV).** Our rules are often noisy or fuzzy.
- **Muggleton's founding numbers.** The 1991, 1995 and 2014/15 papers were never opened. One-example learning claims rest on surveys and one string-task paper (d18: about 61%, below humans).
- **HtT and Popper-ly.** Small closed rule sets (kinship, base arithmetic). Not shown for open rule spaces.

## 10. Open questions

1. At equal tokens, does hypothesis generation plus counted test beat plain CoT and best-of-N for rule induction with a current reasoning model?
2. What is the recall-vs-N curve for correct rules, and where does selection become the bottleneck? (The summariser loses 26% of correct hypotheses.)
3. Does MDL scoring help in an LLM loop when 10-30% of examples are wrong? No LLM-plus-MDL study exists.
4. Does the induce/apply gap persist for 2026 models on rule-writing tasks such as MiniSCAN? Does a fresh-context application call close it?
5. Is a verified rule store worth its tokens beyond kinship and arithmetic? How do wrong rules propagate?
6. What cheap signal predicts that refinement will hurt?
7. Is there a hop-count cutoff beyond which LLM rules should go to a solver? No threshold has been measured.
8. What do the primary Muggleton papers (inverse entailment, MIL) report on example efficiency? Not opened.
9. Does verified predicate invention transfer to open domains, and what does it cost in tokens?
10. Does feeding the agent's own failed attempts as forbidden-shape constraints cut rounds? No LLM-plus-Popper-constraints paper was found beyond ALBI and Popper-ly.
11. Are the 2026 results (ALBI, Popper-ly, ADVENT, AutoSpec, SLR) replicated by other labs? All are single-lab.
12. Is the CoT split explained by "induce an unseen rule" vs "apply stated rules"? Nobody tests both in one setup.

Links to parallel subfields: Search over thoughts, Tree of Thoughts, Logic programming and knowledge representation, MDL and Bayes, Interactive theorem proving, Neural and LLM proof search, Category learning (rule, prototype, exemplar), Matrix tests and task analysis, Strategy on matrices, Argument evaluation criteria, Dual-process theory.

## 11. Sources

[V] = opened and read (full text) in this series. [M] = snippet or secondhand description only.

- [V] Quinlan (1990) FOIL. https://link.springer.com/content/pdf/10.1007/BF00117105.pdf
- [V] Cropper, Dumancic, Evans, Muggleton (2021/22) ILP at 30. https://arxiv.org/abs/2102.10556
- [V] Cropper and Dumancic (2022) ILP at 30, JAIR. https://arxiv.org/abs/2008.07912
- [V] Cropper, Dumancic, Muggleton (2020) Turning 30. https://arxiv.org/abs/2002.11002
- [M] Muggleton (1991) Inductive logic programming. https://doi.org/10.1007/BF03037089
- [M] Muggleton and De Raedt (1994) ILP: theory and methods. https://doi.org/10.1016/0743-1066(94)90035-3
- [M] Muggleton (1995) Inverse entailment and Progol. https://doi.org/10.1007/BF03037227
- [M] Muggleton, Lin, Tamaddoni-Nezhad (2014/15) Meta-interpretive learning. https://doi.org/10.1007/s10994-014-5471-y
- [M] Cropper and Muggleton (2016) Metagol. https://github.com/metagol/metagol
- [M] Law, Russo, Broda, ILASP. https://www.ilasp.com
- [M] Rule (2020) List functions dataset. https://dspace.mit.edu/handle/1721.1/131296
- [V] Cropper and Morel (2021) Popper. https://arxiv.org/abs/2005.02259
- [V] Evans and Grefenstette (2018) dILP. https://arxiv.org/abs/1711.04574
- [V] Hocquette, Niskanen, Jarvisalo, Cropper (2023) MaxSynth. https://arxiv.org/abs/2308.09393
- [V] Sharma, Dumancic, King, Cropper (2026) MML for rule learning. https://arxiv.org/abs/2508.06230
- [V] Zhang, Xu, Yilmaz, Liu (2023) Critical review of ILP for XAI. https://arxiv.org/abs/2112.15319
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660
- [V] Qiu et al. (2024) Phenomenal yet puzzling. https://arxiv.org/abs/2310.08559
- [V] Zhu et al. (2023) Hypotheses-to-Theories. https://arxiv.org/abs/2310.07064
- [V] Yang et al. (2024) DEER. https://arxiv.org/abs/2212.10923
- [V] Gandarela, Carvalho, Freitas (2025) Expressivity-graded analysis. https://arxiv.org/abs/2408.16779
- [V] Li et al. (2025) MIRAGE. https://arxiv.org/abs/2410.09542
- [V] Helff et al. (2026) SLR-Bench. https://arxiv.org/abs/2506.15787
- [V] Li et al. (2024) LLMs for relational reasoning. https://arxiv.org/abs/2401.09042
- [V] Peng et al. (2025) ILP-CoT. https://arxiv.org/abs/2509.21874
- [V] Han et al. (2023) Inductive reasoning in humans and LLMs. https://arxiv.org/abs/2306.06548
- [V] Cheng et al. (2024) SolverLearner. https://arxiv.org/abs/2408.00114
- [V] Li et al. (2024) Induction and transduction. https://arxiv.org/abs/2411.02272
- [V] Benterki et al. (2026) ALBI. https://arxiv.org/abs/2611.05039
- [V] Chen and Ma (2026) Reason Popper-ly. https://arxiv.org/abs/2607.23019
- [V] Yu et al. (2026) ADVENT. https://arxiv.org/abs/2607.01585
- [V] Ma et al. (2026) AutoSpec. https://arxiv.org/abs/2606.24245
- [V] Borroto et al. (2025) LLM2LAS. https://arxiv.org/abs/2509.16590 (not re-opened in the cross-check)
- [V] Rocha et al. (2024) ILP for ARC. https://arxiv.org/abs/2405.06399 (not re-opened in the cross-check)
- [V] Ai, Muggleton et al. (2021) Beneficial and harmful explanatory ML. https://arxiv.org/abs/2009.06410
- [V] Ai, Langer, Schmid, Muggleton (2026) Ultra strong ML with LLM explanations. https://arxiv.org/abs/2509.00961
- [V] Pourcel, Colas, Oudeyer (2026) SOAR. https://arxiv.org/abs/2507.14172
- [V] Naik et al. (2026) PBEBench. https://arxiv.org/abs/2505.23126
- [V] Hua et al. (2025) InductionBench. https://arxiv.org/abs/2502.15823
- [V] Parab et al. (2025) Error sources in hypothesis search. https://arxiv.org/abs/2509.01016
- [V] Li, Wang, Zheng, Song (2025) Patterns over principles. https://arxiv.org/abs/2502.16169
- [V] Lin et al. (2025) SIRBench-V1. https://arxiv.org/abs/2509.16226
- [V] O'Brien et al. (2025) MATHEMAGIC. https://arxiv.org/abs/2510.05962
- [V] Singhal, Mishra, Malach, Galanti (2026) LLM-PV. https://arxiv.org/abs/2510.14331
- [V] Jiang, Yi, Zhu (2026) Sketch-and-Verify. https://arxiv.org/abs/2605.08658
- [V] Muggleton et al. (2018) Ultra-strong ML comprehensibility, Machine Learning 107. https://doi.org/10.1007/s10994-018-5707-3 (opened in the gap pass; the snippet-only entry b09 is superseded)
- [V] Lin, Dechter, Ellis, Tenenbaum, Muggleton (2014) MetagolDF. https://dspace.mit.edu/handle/1721.1/102524
- [M] Search logs d19, d20 (absence of evidence from one search each). https://arxiv.org/abs/2005.02259
