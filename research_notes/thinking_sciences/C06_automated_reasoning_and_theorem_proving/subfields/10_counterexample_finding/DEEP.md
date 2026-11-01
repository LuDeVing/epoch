# Counterexample finding: deep document

*Subfield C06.10. Models that refute a claim. Schema link: S7 discriminating test (and guardrails G2, G3, G10). Evidence ids (a01-d16) are in evidence_a-d.jsonl; claim ids (C06.10-K01 to K36) are in claims.jsonl; corrections are in critique.md. Where a paper appears under several ids, it is ONE source.*

## 1. What it is

A counterexample is one concrete case where a claim is false. Finding one is the cheapest and strongest way to kill a claim. One case settles what no number of confirming cases can.

Three kinds of work sit under this name.

1. **Model finders for logic.** Tools such as Mace4, Paradox, Nitpick, Kodkod and SMT-based finite model finders. You give them the denial of a conjecture. They search finite structures of growing size. A structure that satisfies the denial is a countermodel (a01, b23, a07).
2. **Test and bug finders for code.** QuickCheck-style random testing, LLM-written adversarial tests, "hack" inputs on competitive-programming solutions (REFUTE, TestCase-Eval, UTGen, ARBITER).
3. **Human and LLM hypothesis testing.** Wason's 2-4-6 task and its descendants. Does the tester pick a case that could break the current guess, or a case that fits it (b25-b29, b06, b10)?

A fourth strand uses learned search to build counterexamples to open mathematical conjectures (Wagner 2021, PatternBoost, AlphaEvolve) (a14, a17, a18).

Why it matters for our agent. In S7 two or more candidate rules still fit all examples. The schema says: run the one input where they differ. That is a counterexample search aimed at a pair of rules. If the agent is bad at this step, S7 does nothing. The main message of the newest work is that models are bad at it, and that outside checks and structure repair most of the problem.

Three terms used with care:
- **Falsify**: produce an input that makes the claim or the program fail.
- **Verdict**: the model says "true" or "false". Easier than producing the witness.
- **Witness**: the exhibited counterexample. Must be checked by code.

## 2. History and theories in depth

**Wason and the positive-test story (1960s to 1990s).** In the 2-4-6 task people see the triple 2-4-6, guess a rule, and test triples. Most test triples that fit their own guess. Many announce a wrong rule with confidence. Wason read this as confirmation bias. In the selection task fewer than 10 percent give the logically correct cards in the original; Evans, Newstead and Byrne replicated this in 1993, and Kaufman et al. (2011) tested 112 people on 70 items (b29). Framing the rule as a social contract or permission rule raises success (Cosmides and Tooby 1992, via b29). Nickerson's 1998 review treats the pattern as a wide family of biases (b25).

**Klayman and Ha (1987).** A positive test strategy (test cases the hypothesis says are positive) is not a bug in itself. When the true rule is narrower than the guess, positive tests reveal the error. When the true rule is broader, they never do. So the strategy is efficient in the common case and fails in a specific one (b26; second-hand through Nickerson; original not opened). Evans (1989) puts the cause elsewhere: people fail to think of falsifying cases at all (b27, second-hand). Mynatt, Doherty and Tweney (1978) found that in a simulated discovery world no participant found the rules in a ten-hour session (b28, secondary summary). The dispute is unresolved (K15, contested).

**Lakatos (1976).** In *Proofs and Refutations* a counterexample is not just a stop sign. It can lead to repair of the claim or of the definitions. Not opened this run (a13). It is still the best framing of what to do after a refutation, and no LLM study tests it (K28).

**Finite model finding in automated reasoning.**
- McCune's MACE (1994) turned first-order clauses into propositional logic at a fixed domain size and ran a Davis-Putnam solver. First use: small existence questions for quasigroups. Not opened (a04; second-hand through a06).
- Paradox (Claessen and Sorensson 2003) added symmetry breaking and clause splitting. Not opened (a05; second-hand through a06).
- Mace4 (McCune 2003) dropped the SAT flattening step that blew up in Mace2. It does its own search, starts at domain size 2, and grows the size (b23, c15). It is the model-finding twin of the prover Prover9 (a02).
- Kodkod (Torlak and Jackson 2007) is a relational model finder behind Alloy. Not opened (a11).
- Reynolds et al. (2013) built a finite model finder inside the SMT solver CVC4 (a06, a30).
- Nitpick (Blanchette and Nipkow 2010) targets higher-order logic in Isabelle/HOL. It encodes to relational logic and uses Kodkod and SAT (d01, a07).

**Random testing.** QuickCheck (Claessen and Hughes 2000) made random property testing a standard counterexample finder for programs. Not opened (a12). A 2026 test shows a plain random generator matches an adaptive LLM tester (d14).

**Learned search for conjectures (2021 on).** Wagner (2021) used deep cross-entropy reinforcement learning with no prior knowledge to find counterexamples to graph conjectures (a14). PatternBoost (2024) alternates local search and a transformer (a17). AlphaEvolve-style LLM-guided evolution (2025) tried 67 problems (a18). The pattern: search works when a counterexample is a finite object with a cheap score.

**Falsification as an LLM capability (2023 to 2026).** The question changed from "does the model reason well" to "can it break a plausible wrong answer". REFUTE, CounterMath, TestCase-Eval, WILT, Failing to Falsify and OpenConjecture are the main benchmarks. Training work (CounterMath SFT, Lean disproof, SymCE, ARBITER, INSPIRE) came in 2025 and 2026.

## 3. Core findings with exact numbers

Status: established = two or more independent sources agree; single-source; contested. Counts follow claims.jsonl with corrections from critique.md applied.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Solving a problem does not mean you can break a near-correct solution to it | REFUTE, 324 problems (rating 1200-3500, 34 topics). Best model (o3-mini high) with code execution: about 9 percent at best (Table 1 max cell 9.3). Its Codeforces rating (2130) implies about 48.7 percent solve rate. R1: rating 2029, 44.0 percent. Solve rates are estimated from ratings. | a20, b01, c01 (one paper) | Established with TestCase-Eval (K01) |
| Same gap in test writing | TestCase-Eval fault exposure: Qwen3-32B 43.8, R1-Distill-32B 41.6, Qwen3-8B 41.3, GPT-4.1 36.5, GPT-4.1-mini 33.6, GPT-4o 31.7. Humans 93.3 (20-problem sample). GPT-4.1 by fault type: wrong answer 42.0, runtime error 35.4, time limit 20.9, memory 25.1. | b14, c05 | Established (K01) |
| Coverage grows with many samples | Qwen3-32B cov@1 50.8, cov@20 95.7. GPT-4.1 cov@1 45.3, cov@20 80.0. | b14, c06 | Single-source |
| Correct solution or execution feedback does not close the gap | REFUTE cells stay between 0.9 and 9.3 percent across 5 models and 4 setups. Execution removed validation failures (R1 45 and V3 36 zero-shot, 0 with agent) but gains were small. | a21, b02, b03, c02 | Single-source (K02) |
| Forced random search plus brute force helps a little; many outputs are invalid | RandSearch: V3 4.0, Flash Thinking 3.7, R1 4.0, o3-mini high 8.3. With oracle: V3 15.1, Flash 7.7, R1 9.9. About 35 percent of runs end with an invalid counterexample; 86 percent of those from wrong brute-force code, 14 percent invalid test format. | a21, b04, c03 | Established (K03) |
| Different strategies win on different cases | o3-mini RandSearch refuted 6 percent of submissions other modes missed (3 percent with oracle). No clear trend of success with difficulty bucket for R1 and o3-mini. Median tests passed by the wrong code: 17. | b05, c04 | Single-source (K04) |
| Verdict is easier than witness | CounterMath, 1,216 items. F1: R1 80.7, Gemini 2.5 Pro 77.0, Claude 3.7 64.8, o1-preview 60.1, GPT-4o 59.0, Qwen-max 58.9; most open models near 30; Qwen2.5-Math-72B 41.8. Strict / loose rationale: R1 54.2/65.3, Gemini 65.1/75.7, Claude 45.0/52.5, o1-preview 39.8/40.9, GPT-4o 19.7/21.3. Row order read from a garbled table. | a22, b12, c07, c08 | Single-source (K08, K09) |
| Counterexample fine-tuning: in-domain small, out-of-domain unreliable | CounterMath SFT F1 38.3 to 41.1. OOD MATH 80.5 to 87.9; AIME 2024 20.0 to 30.0 (3 of 30 problems). INSPIRE: AIME unchanged for 2 of 3 models, +6.67 (2 problems) for one; MATH500 +0.6 to +1.8; GSM8K +0.5 to +1.1. Single runs, no confidence intervals. | a23, b13, c09, a28, d12 | Contested (K10, K31) |
| LLMs repeat the 2-4-6 error | Failing to Falsify: 11 models, success 6 to 78 percent in 45 turns. Share of incompatible tests rises with success. Qwen3-8B 6 percent non-thinking vs 21 thinking; 14B 23 vs about 35; 32B 33 vs 41. | b06, b08, c10 | Established with WILT (K11) |
| WILT: best model solves few hidden rules | 50 rules, up to 30 tests then a guess. Claude 3.5 Sonnet 14/50 (28 percent), o1-mini 13, o1-preview 12, chatgpt-4o-latest 11, Mistral Large 2 11, GPT-4o 9, Llama 3.1 405B 8, Gemma 2 9B 0. | b10, c13 | Established (K11) |
| Opposite-test instruction (Think-in-Opposites, TiO) | Average success 42 to 56 percent. Thinking models: TiO +0.123 success, +0.168 incompatible share (p < 2e-5); Dual-Goal +0.148. Non-thinking: TiO +0.063 (p = 0.0033), share +0.020 (n.s.); Dual-Goal -0.060 (p = 0.0065). Qwen3-32B thinking 41 to 61 percent; Gemini 2.5 Pro 0.73 to 0.78. | b07, c11 | Single-source (K12) |
| Thinking mode lifts success but not clearly test quality | Thinking uses 1,000 to 2,000 tokens per turn vs about 6 to 14 non-thinking. Success rises, incompatible share not consistently. | b08, c10 | Single-source (K13) |
| Test design and rule guessing are separate skills | o1-mini with GPT-4o tests: 19/50 vs 13/50 alone. | b11, c14 | Single-source (K14) |
| Positive testing is not itself an error | Klayman and Ha case analysis. Cause of failure disputed (Evans). | b25-b28 | Contested (K15) |
| Paradox beats Mace4 | TPTP 3.1.1, 1,251 satisfiable problems, 300 s: Paradox 1083, FM-Darwin 1074, Mace4 802. FM-Darwin solved 328 that Mace4 could not (169 timeouts, rest out of memory) and 82 that Paradox could not. | d04 | Established (K16, K32) |
| Newer finders: Paradox leads, SMT adds coverage | TPTP 5.4.0, 300 s: Paradox 1450, CVC4 fm 1277, CVC4 f 1190, CVC4 fmi 1165, Z3 941. CVC4 variants solved 52 satisfiable problems Paradox did not. Authors are the CVC4 team. | d03 | Established (K16, K18) |
| SMT finder vs MACE-style encoding | 793 random colouring problems, 60 s: best CVC4 variant 723; other variants 664, 617 and 309 (per critique.md). | a06, a30 | Single-source (K18) |
| Nitpick on Isabelle theories | 3,200 mutants (200 from each of 20 theories), 10 s limit. Genuine counterexamples on most theories. Example rows (Quickcheck vs Refute vs Nitpick): Map 43 vs 0 vs 157; Fun 5 vs 162 vs 163; Predicate 19 vs 103+45 potential vs 161; List 119 vs 1+17 vs 117+9. Weaker on real-arithmetic theories. | d01 | Established (K17) |
| Nitpick on TPTP higher-order | Disproved 293 of 2,729 formulas vs 214 for Refute (most formulas are theorems). Counterexamples to 5 formulas "proved" by TPS or LEO-II: 2 bugs in TPS, 1 in LEO-II. | d02 | Established (K17) |
| Search defaults | Nitpick: scopes 1 to 10 per type, 30 s timeout; four type variables mean 10,000 scopes without monotonicity pruning. Mace4: start size 2. Witnesses over infinite types are "potentially spurious". | a07-a10, b23, b24 | Established |
| Learned search refutes real conjectures | Wagner: n=19 tree, value 5.16 below bound 5.24; about 5,000 iterations on an ordinary PC; true up to n=18; a published disproof had n=600. PatternBoost: 6-cube subgraph with 81 edges and diameter 6, below the conjectured 82. No-isosceles n=64 grid: 110 points vs 96 from the best LLM program search. | a14, a15, a17, b30, b31, c19, c20 | Established (K19, K20) |
| LLM-guided evolution found nothing on many conjectures | 67 problems. No counterexample for a strengthening of Sendov, Duchi, a power-of-2 cycle conjecture (graphs to 40 vertices). Models cheated weak verifiers (float leaks, degenerate points). | a18, a19, c22, c23 | Established (K21) |
| LLM conjecture solving at scale | 200 random arXiv conjectures: 70 counterexamples, 55 proofs (by pass: 49/15/6 and 33/11/11). 84 percent held up under same-family LLM review. About 60 percent of early counterexamples were textbook; trivial group and single vertex appear. | a26, a27, d10 | Single-source (K22) |
| Formal disproof training | FOR-COUNTER 1,058 problems: pass@1 222 vs 127 strongest baseline; pass@4 274 vs 200; pass@9 302 vs 224. Rejected from ICLR 2026; counts reported because autoformalization is noisy. | a24, a25, d11 | Single-source (K23) |
| Exact checker as reward and filter | SymCE, 4,707 false conjectures, held-out n=201: Qwen3-4B base 0.30, SFT 0.35 (not significant), RL with verifier 0.50 (paired delta +0.199 [0.13, 0.27]). Verifier audit 97.7 percent of 177 decisions correct. | d05, d07 | Established (K30) |
| Imitation trap | Training to always emit a witness: true-theorem recognition 0.27 to 0.00. "Conclusion not negated" failure rose 1 to 31 percent. RL with sparse reward: 0.65; explicit true/false 0.84. | d06 | Established (K03, K30) |
| Models find errors worse than they fix them | Tyen et al. (BIG-Bench traces from PaLM 2): GPT-4 step-level mistake finding 52.87 percent overall; logical deduction step-level 67.67 (direct-trace 40.67). Backtracking with oracle location +18.04 to +43.92 points on wrong traces; small losses on right traces (about 0 to -11). | b18, c26 | Single-source (K24) |
| Self-review without feedback does not help | Huang et al.: GPT-3.5 GSM8K 75.9 to 74.7 (round 2); CommonSenseQA 75.8 to 41.8; GPT-4 GSM8K 95.5 to 89.0. Oracle label: GPT-3.5 GSM8K 75.9 to 84.3. | b19 | Single-source (K25); fits G2 |
| LLM critics find bugs and hallucinate | CriticGPT (McAleese et al.): critiques preferred over human ones in 63 percent of natural bug cases; over ChatGPT critiques more than 80 percent on tampered bugs. | b21, c27 | Established with d08 (K26) |
| Executed counterexamples beat verdict-only judging | ARBITER (Qwen3.6-35B-A3B): hack success 40.61 to 62.67; hard-split verdict accuracy 67.43 to 83.40 (UOJ), 65.34 to 84.50 (USACO-JUDGE). One tool-using sample beat eight plain samples. A failing input predicted a correct diagnosis 71.6 vs 10.3 percent (400 audited). | d08, d09 | Established (K26) |
| Models misjudge plausible wrong programs | About 60 percent accuracy vs 50 percent chance (Counterfeit Conundrum). GPT-4 execution prediction near 80 percent. | b20 | Single-source (K27) |
| Test generation tradeoff | Qwen2.5-7B prompted for failing tests: attack rate +13.53, output accuracy -16.47. UTGen: attack 42.0, output accuracy 58.0 vs prompted 39.8 and 40.8. UTDebug: +3.17 (HumanEvalFix), +12.35 (hard MBPP+). | b16, c24 | Single-source (K06) |
| Adversarial tests as selector | Best-of-10, Qwen2.5-7B: beats an 8B reward model by 4.43 on HumanEval+; random tests 3.73 worse; prompted tests 1.83 worse. Self-test selection 28.56 to 43.01; public tests 45.99; both 46.15. | c25, d15 | Single-source (K07, K35) |
| Random generator equals adaptive LLM tester | Adaptive minus random-property failure rate -0.024 [-0.097, +0.043]. Adaptive minus static LLM tests -0.131 [-0.228, -0.050]. Seeing the source added nothing: -0.005 [-0.044, +0.034]. | d14 | Single-source (K33) |
| LLM and numeric falsifiers win on different cases | 21 cyber-physical specs, 10 runs each. LLM first on 14 of 21. Six specs falsified in one simulation every run. AT51 and AT54: LLM 0 of 10, FReaK 10 of 10. | d13 | Single-source (K34) |
| Solver offload depends on clean translation | Logic-LM, GPT-4 (Standard / CoT / Logic-LM): PrOntoQA 77.40 / 98.79 / 83.20; ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04. Translation executable: FOLIO 79.9, AR-LSAT 32.6 percent. | d16 | Single-source (K29) |
| Statistical hypothesis falsification | POPPER (alpha 0.1), DiscoveryBench type I: ReAct 0.145, Self-Refine 0.248, POPPER 0.152. Power 66.5 percent above ReAct. Nine bioinformaticians: similar quality in about 10 times less time. | b17 | Single-source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 Finite model search (Mace4, Paradox, Nitpick).**
1. Input: the denied claim as clauses or a formula with free types.
2. For domain size n = 1, 2, 3, ... up to a limit (Mace4 starts at 2; Nitpick tries scopes 1 to 10 per type): build the constraint problem for that size.
3. Encode to SAT (MACE style), or hand to an SMT solver (CVC4 finite model finder) or a relational solver (Kodkod, for Nitpick).
4. Break symmetries (renamings of domain elements) so equivalent models are not searched twice. This is why Paradox beats plain MACE.
5. If SAT: decode the model and print it. If UNSAT at all sizes within the limit: say "none found". This is NOT a proof of truth.
6. Prune scopes by monotonicity: if the claim cannot fail at a small scope for a monotonic type, skip bigger scopes (Nitpick). Integers, rationals and lists of them are generally non-monotonic, so pruning fails and 10,000 scopes may be needed (a08).
7. Re-check the model in the original claim. Nitpick can return a spurious witness when the encoding is coarse (coinductive types; fixed with a bisimulation depth) (a09).

Limits. Finite models only. Memory runs out for large domains. Different finders solve different problems, so run a portfolio (d03, d04).

**4.2 Verifier-gated refutation loop (SymCE, ARBITER pattern).**
1. Model proposes a witness (often one line of code).
2. Code checks: (a) every hypothesis of the claim holds on the witness, (b) the NEGATED conclusion holds, (c) the input is legal.
3. Only a witness passing (a) to (c) counts. Reward and acceptance both use this.
4. "None found" is a first-class output. Without it the model invents witnesses for true claims (d06: true-theorem recognition 0.27 to 0.00 after witness-only SFT).
5. The checker must be exact. Use rational or integer arithmetic. AlphaEvolve search exploited float leaks and degenerate points (a19, c23). SymCE's checker was right in 97.7 percent of 177 audited cases (d07).

**4.3 Generator plus brute-force checker (REFUTE RandSearch).**
1. Model writes (a) an input generator and (b) a simple slow reference solution.
2. Code runs both on many small random inputs and compares.
3. Any input where the target and the reference disagree is a candidate.
4. Check the reference separately. 86 percent of invalid results came from a wrong brute force (a21).

**4.4 Rule-discovery test selection (Wason family).**
1. Keep a set of live hypotheses H.
2. Choose a test input x. Prefer an x that some hypothesis in H calls negative (an "incompatible" test) and that splits H.
3. Observe the oracle's answer.
4. Drop hypotheses that disagree.
5. Log the incompatible-to-compatible ratio (I:C). In Failing to Falsify, I:C tracks success (b06).
6. Option: use two calls. One designs the test, another updates the hypothesis. WILT shows the skills are separable (b11).
7. Prompt that worked: "make the next test opposite to your last one" (TiO) (b07).

**4.5 Counterexample-guided selection (S7).**
Given rules A and B that fit all examples: find inputs where A(x) differs from B(x) by running both on generated inputs (random plus boundary). Run the most informative x on the oracle. Keep the rule that agrees. This is differential testing, the setting where a random generator matched an LLM tester (d14).

**4.6 Search for constructive counterexamples (Wagner, PatternBoost).**
1. Define a score for a finite object (a graph, a point set) that crosses a bound when the conjecture fails.
2. Cross-entropy RL: sample many objects, keep the top fraction, retrain the sampler on them (a14). Wagner reports about 5,000 iterations and large run-to-run variation.
3. PatternBoost: build by local search from seeds, keep the best, train a transformer on them, sample, repeat (a17).
4. Exact check of the final object.

**4.7 Locate then fix (Tyen).**
Find the first wrong step by code or a trained checker. Regenerate from that step. Fixing works once the location is given (+18 to +44 points on wrong traces). Finding is the hard step: 52.87 percent step-level at best (b18).

## 5. What holds up

**Holds up (two or more independent sources).**
- Models that can solve a problem cannot reliably break a wrong solution (REFUTE, TestCase-Eval). K01.
- LLMs show the Wason pattern, and success tracks the share of tests that can contradict the guess (Failing to Falsify, WILT). K11.
- An exact external checker is needed. It removes most invalid counterexamples (35 percent invalid in REFUTE without one; 97.7 percent verifier accuracy in SymCE). K03, K30.
- Self-review without outside feedback fails (Huang), while located errors get fixed (Tyen). These agree: locating is the weak link. G2 stands.
- Model finders work on small structures and are tool-specific. Paradox 1083 and Mace4 802 of 1,251 at 300 s; solved sets only partly overlap. K16, K32.
- Nitpick finds real bugs, including in provers, and can return spurious witnesses. K17.
- Learned search can refute decades-old finite-object conjectures (Wagner, PatternBoost). K19, K20.
- Weak verifiers get exploited (AlphaEvolve). K21.

**Failed or doubtful.**
- Out-of-distribution gains from counterexample fine-tuning. CounterMath reports AIME 20 to 30 (3 problems). INSPIRE finds AIME unchanged for two of three models. Neither has confidence intervals. Treat as noise. K10, K31.
- Training a model to always output a witness. It fabricates witnesses for true claims (0.27 to 0.00). d06.
- Giving the correct solution to the falsifier. REFUTE stayed in the 1 to 10 percent band. K02, one paper.
- Execution feedback. It removed invalid-format failures, but success gains were small (only R1 showed a modest gain). b03.
- Thinking mode as a substitute for falsification intent. Success rises but the incompatible share does not consistently rise. K13.

**Moderators and boundary conditions.**
- Model type. TiO helps thinking models (+0.123) and only a little for non-thinking (+0.063); Dual-Goal hurt non-thinking models (-0.060, p = 0.0065) (c11).
- Fault type. Wrong-answer faults are easier to expose than time-limit and memory faults (42.0 vs 20.9 and 25.1 for GPT-4.1) (c05).
- Language. Python solutions are easier to break than C++ or Java (b15, single-source). 317 of 324 REFUTE items are C++.
- Task framing. Blicket hypotheses have no clean opposite, so TiO transfers less (c12).
- Translation quality for solver offload. Logic-LM helps when translation runs (FOLIO 79.9 percent executable) and hurts when it does not (PrOntoQA 83.20 vs CoT 98.79) (d16).
- Domain size. Finite finders find nothing when the smallest counterexample exceeds the limit. "None found" proves nothing (a07, b24).
- Solved-set overlap. Strategies and finders win on different cases (b05, d04, d13).

**Interventions that worked.**
- Exact-checker reward (SymCE +0.199 paired delta).
- Executed counterexample for judging (ARBITER 40.61 to 62.67 hack success).
- TiO prompt for thinking models.
- Splitting test design from rule guessing (19/50 vs 13/50, small N).
- Random generator plus brute force for weaker chat models.
- Adversarial tests as a selector (beats an 8B reward model by 4.43 on HumanEval+).

**Interventions that did not work.**
- Giving the oracle solution to the tester; prompt-only "write failing tests" (output accuracy falls 16.47 points for Qwen2.5-7B); unaided self-review; witness-only SFT; training for general reasoning gain.

**Cross-check corrections (critique.md).** Many claims rest on one paper counted three ways. REFUTE solve rates are estimated from ratings. CounterMath rows come from a garbled table. Tyen's 52.87 is the overall step-level figure; 40.67 is a direct-trace cell. Huang's oracle result is 75.9 to 84.3, not 95.5. The REFUTE abstract says "under 9 percent" but one cell reads 9.3. CriticGPT's first author is McAleese. No study compares tool-assisted refutation with unaided refutation.

## 6. Language models

**Unaided frontier models are poor falsifiers.** REFUTE: about 9 percent at best against an implied 49 percent solve rate (a20). TestCase-Eval: best 43.8 percent, humans 93.3 (b14). WILT: best 14 of 50 hidden rules (b10). Failing to Falsify: 6 to 78 percent over 11 models (b06).

**Verdict beats witness.** On CounterMath, R1 gets F1 80.7 but strict rationale 54.2 (c08). GPT-4o: F1 59.0, strict 19.7. The model often says "false" without a valid case.

**Models make invalid counterexamples.** About 35 percent of RandSearch runs in REFUTE ended with a wrong counterexample (a21). Witness-only SFT drove true-theorem recognition to 0.00 (d06). In OpenConjecture, trivial cases such as the trivial group appear and about 60 percent of early verified cases were textbook (d10), with same-family review only.

**What changed performance, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Thinking mode | Success: Qwen3-8B 6 to 21 percent; 14B 23 to about 35; 32B 33 to 41. Incompatible share not clearly higher. | b08, c10 |
| TiO prompt (thinking models) | success +0.123; incompatible share +0.168 | c11 |
| TiO or Dual-Goal (non-thinking) | TiO +0.063; Dual-Goal -0.060 | c11 |
| Distilled TiO traces | Qwen3-8B 21 to 35 percent; from 32B teacher 44 percent; Qwen3-32B 41 to 64 | c12 |
| Prompted random search (REFUTE) | 4.0 to 8.3 percent; oracle 7.7 to 15.1 | a21 |
| Execution feedback | validation failures 45 and 36 to 0; small success gain | b03 |
| Tests from another model | 13/50 to 19/50 | b11 |
| Chain-of-thought for tests | CoT above direct (figure only) | b15 |
| Verifier-reward RL (4B) | 0.30 to 0.50 | d05 |
| Tool-using judge with executed counterexample | 40.61 to 62.67 hack success | d08 |
| Logic solver offload | ProofWriter 68.11 (CoT) to 79.66; PrOntoQA 98.79 (CoT) to 83.20 | d16 |
| Fine-tuning on about 1,000 counterexamples | in-domain F1 +2.8; OOD uncertain | a23, d12 |

**Search with LLMs.** AlphaEvolve-style loops tried 67 problems and found no counterexamples on several famous ones (a18). They also cheated (float leaks). LLM search won on 14 of 21 cyber-physical specs but failed completely on some where a blind optimizer won 10 of 10 (d13). A plain random property generator matched an adaptive LLM tester (d14).

**Models with tools.** No study measures an LLM that calls Mace4, Nitpick or an SMT model finder against the same LLM unaided at equal tokens (K29). The nearest evidence is Logic-LM and ARBITER: execution helps when the model supplies a legal input.

**Locating beats reviewing.** Models find the faulty step 52.87 percent at best and fix it +18 to +44 when told where (b18). Whole-trace self-review can break right answers (CommonSenseQA 75.8 to 41.8) (b19).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Every counterexample is checked by code before it counts.** Check each hypothesis of the claim and the negated conclusion; use exact arithmetic. Part: G2, G3, S7, S8. [E] K30, K03, K21. Evidence d05, d07, a21, b04, a19. (This extends G2 and G3 to the agent's own S7 output. It needs a wording line, not a new guardrail.)
2. **"None found" is a legal result of S7.** Never force a witness. Part: S7, compatible with G6. [E] K30. Evidence d06, d05. Log the rate of "none found" in S9.
3. **S7 test inputs are executed, not argued.** Run both candidate rules rather than predict what they do. Part: S7, G10. [E] K26; K25 and K27 support. Evidence d08, d09, b19, b20.
4. **A finite-search witness is re-checked in the original claim, and "none found" is never read as "true".** Part: S7, S8. [E] K17. Evidence a07, a09, b24.
5. **Log the share of S7 tests that could contradict the current best rule (I:C).** Part: S9 log / memory. [E] K11. Evidence b06, c10, b10. Costs nothing.
6. **Locate, then fix.** At S5 show the located failing output (already G2). Do not ask the model to find the fault by reading its own reasoning. Part: G2. [E] as a guardrail; K24 and K25 are single-source each. Evidence b18, b19.

### Test first

7. **Opposite-test instruction in S7** ("choose the input that is positive under one rule and negative under the other"). Part: S7. [S] K12. Evidence b07, c11. Open Qwen3 models, toy rules; small effect for non-thinking models.
8. **Generator plus brute-force checker in S7** vs free-form test choice. Part: S7. [E] for direction, small gain, 35 percent invalid. K03. Evidence a21, b04.
9. **A random/property arm in the S7 portfolio**; measure the LLM arm's gain over it. Part: S7. [S] K33. Evidence d14.
10. **Portfolio of falsification strategies** (random, boundary, small-model search, opposite test). Part: S7/O. [S] K04, K34. Evidence b05, d13. Union gain at equal tokens unmeasured.
11. **Separate calls: design the test, then update the hypothesis.** Part: S7. [S] K14. Evidence b11.
12. **Offer a model-finder tool for small logic claims** (Mace4, Nitpick, SMT). Part: S7 tools. [S] K29; tool strength [E] K16, K32. Evidence d03, d04, d16. No LLM-plus-finder study exists.
13. **Check-intended-hypotheses step** to cut trivial counterexamples. Part: S7/G3. [S] K22, K36. Evidence d10.
14. **Claim-repair step after refutation (Lakatos).** Part: new operator candidate after S7. [S] K28. Evidence a13 (not opened), d09 (code only).
15. **Score verdict and witness separately** on our bench. Part: bench. [S] K08. Evidence c08.
16. **Critic role in S7 that must emit an executable counterexample, not prose.** Part: S7, G5. [E] direction (K26), false alarms uncounted. Evidence b21, d08, d09.
17. **Think-before-test step.** Part: S7. [S] K05. Evidence b15. G11 applies: thinking cost counts.
18. **Generated tests as a selector, trusted tests first.** Part: S4, S7. [S] K07, K35. Evidence c25, d15. Consistent with G4.

Guardrail fit. G1: S7 fires only when two rules still fit, which is a signal. G7: every "Test first" item must win at equal tokens. G9: a critic is not a debater; it must output an executable input or nothing.

## 8. Concrete tests on our bench

All arms get equal total tokens (setup and tool calls counted, G7). Use at least 3 seeds. Report paired differences with 95 percent intervals; samples are small in this field.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Falsification gap | ARC items with 2 to 4 programs that fit all train pairs; planted-bug code items | solve rate vs rate of producing a failing input for a planted bug, same model | Gap in points | Large gap, as in REFUTE (49 vs about 9) |
| T2 Discriminating test | ARC items where two fit programs differ on the test grid | free-form S7 vs opposite-test instruction vs code-run differential (run both programs on generated inputs) | Share of items where S7 picks the program that is right on the held-out grid | Code-run best; TiO small gain |
| T3 Executable counterexample | wrong-candidate-answer items with a checker | prose critique vs model must emit an input that code runs | Valid counterexample rate; false-alarm rate | Executable arm has fewer false alarms |
| T4 Invalid-witness rate | small algebra, graph, list claims, half true | free-form witness vs witness with code check of hypotheses and negated conclusion, "none found" allowed | Invalid witness rate; false refutation of true claims | Checker cuts invalid witnesses below 5 percent |
| T5 Model-finder tool | small first-order or Isabelle-style claims, half true | LLM alone vs LLM with a Nitpick or Mace4 call (30 s) | Valid refutations of false claims; wasted calls on true claims | Gain on clean formalisations; loss when translation fails |
| T6 Strategy portfolio | planted-bug code items; hidden-rule items | best single strategy vs union of random, boundary, opposite, small search | Union gain over best single | Positive if wins are disjoint |
| T7 Random arm | code items with property tests | LLM adaptive tester vs random property generator | Failure rate per N tests | No LLM advantage |
| T8 Split calls | WILT-style hidden rules (Python lambdas) | one call vs separate design and update calls | Rules found of 50 | +3 to +6 of 50 |
| T9 I:C logging | all S7 runs | observational | Correlation of I:C with success | Positive |
| T10 Hypothesis check | open conjectures or textbook claims | accept counterexample vs check intended hypotheses first | Share trivial or out-of-domain, judged by an independent model plus a human sample | Lower trivial share |
| T11 Claim repair | refuted claims with a known repair | discard and retry vs repair step | Downstream answer correct | Unknown |
| T12 Verdict vs witness | CounterMath-style items | verdict-only vs strict rationale scoring | Gap | 10+ points, as in c08 |

## 9. What does not transfer, and why

- **Training results (CounterMath SFT, Lean disproof, SymCE RL, ARBITER, INSPIRE, UTGen).** We do not train. Only the design lessons transfer: an exact verifier, allow "none found", execute inputs.
- **Competitive-programming falsification (REFUTE, TestCase-Eval).** The oracle is exact (run two programs). Many of our tasks have none. The gap still warns us not to assume S7 works.
- **Learned conjecture search (Wagner, PatternBoost).** Needs a cheap score, a finite object and hours of compute. Our items are single problems with small budgets.
- **Mace4/Nitpick numbers.** TPTP and Isabelle mutants at 10 to 300 s. Our items are not formalised, and translation to logic is the unmeasured step.
- **Wason-style rule games.** Integer triples, clean oracle, cheap tests. Real claims have costly tests and often no clean opposite.
- **Human confirmation-bias findings.** The cause (bias, rational positive test, or failure to think of falsifiers) is unresolved. Fixing an LLM need not mirror people.
- **Statistical hypothesis falsification (POPPER).** Needs datasets and sequential error control. Different object.
- **Numbers from garbled tables.** CounterMath rows, Tyen cells and REFUTE cells carry transcription risk (critique.md). Use ranges.

## 10. Open questions

1. Does giving an LLM a finite-model finder raise refutation over unaided reasoning at equal tokens? No study (K29).
2. How often does an unaided frontier model produce an invalid counterexample outside code, and does an exact checker remove them? REFUTE's 35 percent is the only data point.
3. Does Think-in-Opposites transfer from Wason rules to real claims at equal tokens?
4. Is test design or the update after the test the bottleneck? WILT's cross-model split suggests design; GTDD (source access adds nothing) is not a replication.
5. What is the equal-token union gain of several falsification strategies?
6. How did MACE, Paradox and Mace4 compare with provers in CASC model-finding tracks? Reports not obtained.
7. How well do models repair a claim after refutation, and does repair help?
8. Do trained critics transfer from code to natural-language reasoning?
9. Are CounterMath OOD gains real? INSPIRE says near zero; neither has confidence intervals.
10. What fraction of LLM-found conjecture counterexamples survive expert review as non-trivial?
11. What does a wasted S7 test cost? No data on false-alarm cost.
12. Does positive or negative testing find errors first on our task mix?

## 11. Sources

[V] opened (text read this session), [M] snippet only or not opened. Several ids point at the same paper.

- [V] McCune, Prover9 and Mace4 manual and home page. https://www.cs.unm.edu/~mccune/prover9/manual/2009-11A/mace4.html and https://www.cs.unm.edu/~mccune/mace4/ (a01, a02)
- [V] Wikipedia, Mace4 (stub, weak). https://en.wikipedia.org/wiki/Mace4 (a03)
- [V] McCune (2003) Mace4 Reference Manual and Guide. https://arxiv.org/abs/cs/0310055 (b23, c15, c16)
- [M] McCune (1994) A Davis-Putnam program and its application to finite first-order model search. https://www.mcs.anl.gov/~mccune/papers/ (a04)
- [M] Claessen and Sorensson (2003) New techniques that improve MACE-style finite model finding. https://www.cse.chalmers.se/~koen/pubs/entry-sat03-paradox.pdf (a05)
- [V] Reynolds, Tinelli, Goel, Krstic (2013) Finite model finding in SMT. https://homepage.divms.uiowa.edu/~ajreynol/cav13.pdf (a06, a30)
- [V] Reynolds et al. (2017) Constraint solving for finite model finding in SMT solvers. https://arxiv.org/pdf/1706.00096 (d03)
- [V] Baumgartner, Fuchs, de Nivelle, Tinelli (2009) Computing finite models by reduction to function-free clause logic. https://peba62.github.io/publications/ME-finite-models-JAL.pdf (d04)
- [V] Blanchette, Picking Nits (Nitpick user's guide, 2010, 2024, 2026 editions). https://isabelle.in.tum.de/doc/nitpick.pdf ; https://www21.in.tum.de/~blanchet/nitpick.pdf ; https://isabelle.in.tum.de/dist/Isabelle/doc/nitpick.pdf (a07-a10, a29, b24, c17)
- [V] Blanchette and Nipkow (2010) Nitpick: a counterexample generator for higher-order logic based on a relational model finder. https://www21.in.tum.de/~nipkow/pubs/itp10.pdf (d01, d02). Publisher DOI https://doi.org/10.1007/978-3-642-14052-5_11 (c18, [M])
- [M] Torlak and Jackson (2007) Kodkod. https://emina.github.io/papers/kodkod.tacas07.pdf (a11)
- [M] Claessen and Hughes (2000) QuickCheck. https://www.cs.tufts.edu/~nr/cs257/archive/john-hughes/quick.pdf (a12)
- [M] Lakatos (1976) Proofs and Refutations. https://doi.org/10.1017/CBO9781139171472 (a13)
- [V] Wagner (2021) Constructions in combinatorics via neural networks. https://arxiv.org/abs/2104.14516 (a14-a16, b30, c19)
- [V] Charton, Ellenberg, Wagner, Williamson (2024) PatternBoost. https://arxiv.org/abs/2411.00566 (a17, b31, c20)
- [V] Ellenberg et al. (2025) Generative modeling for mathematical discovery. https://arxiv.org/abs/2503.11061 (c21)
- [V] Georgiev, Gomez-Serrano, Tao, Wagner (2025) Mathematical exploration and discovery at scale. https://arxiv.org/abs/2511.02864 (a18, a19, c22, c23)
- [V] Sinha et al. (2025) Can language models falsify? REFUTE. https://arxiv.org/abs/2502.19414 (a20, a21, b01-b05, c01-c04)
- [V] Li et al. (2025) CounterMath. https://arxiv.org/abs/2502.10454 (a22, a23, b12, b13, c07-c09)
- [V] Li et al. (2026) Learning to disprove. https://arxiv.org/pdf/2603.19514 (a24, a25, d11)
- [V] Jenne et al. (2026) OpenConjecture. https://arxiv.org/pdf/2610.40382 (a26, a27, d10)
- [V] Wang et al. (2026) INSPIRE. https://arxiv.org/pdf/2608.27501 (a28, d12)
- [V] Jhaveri et al. (2026) Failing to falsify. https://arxiv.org/abs/2604.02485 (b06-b09, c10-c12)
- [V] Banatt et al. (2024) WILT. https://arxiv.org/abs/2410.10998 (b10, b11, c13, c14)
- [V] Yang et al. (2025) TestCase-Eval. https://arxiv.org/abs/2506.12278 (b14, b15, c05, c06)
- [V] Prasad et al. (2025) UTGen. https://arxiv.org/abs/2502.01619 (b16, c24, c25)
- [V] Huang et al. (2025) POPPER. https://arxiv.org/abs/2502.09858 (b17)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (b18, c26)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b19)
- [V, abstract and a few result lines] Gu et al. (2024) The Counterfeit Conundrum. https://arxiv.org/abs/2402.19475 (b20)
- [V] McAleese et al. (2024) LLM critics help catch LLM bugs. https://arxiv.org/abs/2407.00215 (b21, c27)
- [V, results not read in detail] Eisape et al. (2023) Syllogistic reasoning in humans and language models. https://arxiv.org/abs/2311.00445 (b22)
- [V] Nickerson (1998) Confirmation bias (reviews Wason, Klayman and Ha, Evans). https://pages.ucsd.edu/~mckenzie/nickersonConfirmationBias.pdf (b25-b27)
- [V, secondary] Wikipedia, Confirmation bias; Wason selection task. https://en.wikipedia.org/wiki/Confirmation_bias ; https://en.wikipedia.org/wiki/Wason_selection_task (b28, b29)
- [M] Klayman and Ha (1987), Evans (1989), Mynatt, Doherty and Tweney (1978), Wason (1960, 1966, 1968): read only through the reviews above.
- [V] Zouak et al. (2026) SymCE. https://arxiv.org/pdf/2610.02444 (d05-d07)
- [V] Deng et al. (2026) ARBITER, Beyond the Verdict. https://arxiv.org/pdf/2610.18760 (d08, d09)
- [V] Arjomandbigdeli, Zhou, Bak (2026) LLMs as falsifiers for cyber-physical systems. https://arxiv.org/pdf/2609.20752 (d13)
- [V] Kato (2026) GTDD. https://arxiv.org/pdf/2610.02952 (d14)
- [V] Xu et al. (2026) Two-stage RL for sound and adversarial test generation. https://arxiv.org/pdf/2609.03955 (d15)
- [V] Pan, Albalak, Wang, Wang (2023) Logic-LM. https://arxiv.org/pdf/2305.12295 (d16)
