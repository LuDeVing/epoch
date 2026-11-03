# Falsificationism: deep document

*Subfield D01.04. Bold conjecture, severe test, refutation. Key work: Popper. Evidence files: evidence_a-d.jsonl (ids a01-a26, b01-b26, c01-c28, d01-d16). Claims: claims.jsonl (D01.04-K01 to K26). Cross-check: critique.md. Links only (not covered here): Lakatos and refutation by proof (02_proofs_and_refutations), research programmes (03), abduction (01), theory comparison, hypothetico-deductive model, problem of the priors, experimental practice, Bayesian models of cognition.*

## 1. What it is

Falsificationism is Karl Popper's answer to two questions. How do we tell science from non-science? How should a scientist treat a theory? His answer: a claim is scientific only if some possible observation could contradict it. Make bold guesses (conjectures). Then try hard to break them (severe tests). Drop what breaks. Never call a theory proven; call it corroborated if it survived a risky test (a01, a02, a06).

The logic is plain. "All swans are white" cannot be proven by any number of white swans. One black swan refutes it. Confirming instances commit the fallacy of affirming the consequent. Refutation is deductive (a06).

Three ideas matter for our agent.
1. **Bold conjecture.** A claim that says more forbids more, so it is easier to refute and more informative. Content and probability vary inversely (a02).
2. **Severe test.** A pass counts only if the test would probably have failed had the claim been wrong. Mayo's later rule: if little has been done to rule out flaws, the claim has not passed a severe test (a07).
3. **Refutation as the move.** Search for the case that breaks the claim, not for cases that fit it.

Why it matters here. Our schema state S4 (TEST) and guardrail G3 (a pass must be on something the answer was not fitted to) already encode the core. S7 already has a counterexample search for rivals. This document asks: what does the evidence say about how well people and language models actually do this, what makes them do it better, and what is still unproven.

The short answer from the evidence:
- Humans prefer tests that fit their guess. This is a strong, replicated pattern, but it is a "positive test strategy", not simple irrationality (a09, b01).
- Language models show the same pattern on rule-discovery games, and models that test outside their guess win more often (a16, a19, a20).
- LLMs that can solve a problem are far worse at refuting a wrong solution (REFUTE: under 9% vs about 48.7% solve rate) (b19, d03).
- Prompts that force an "opposite" test help thinking models, and do not reliably help non-thinking ones (a17, b26, d08).
- Nobody has measured a forced falsification step inside a full agent at equal tokens against best-of-N. The link to G3 and S4 is by analogy (K26).

## 2. History and theories in depth

### 2.1 Popper's programme

- **Logik der Forschung (1935; English 1959)** and **Conjectures and Refutations (1963)** set out the programme. The target was the claim of psychoanalysis and Marxism to be confirmed by everything (a01).
- **Demarcation.** A theory that no possible observation could contradict is not scientific. This is a boundary rule, not a description of how scientists actually behave (a01).
- **Corroboration.** A theory is corroborated when it survives a risky prediction. Corroboration is not a probability and is not truth (a02, a06).
- **Basic statements.** Falsification needs singular statements that can be tested, but testing stops at statements we decide to accept. Popper compares this to a jury verdict that can be revised. So falsification is never fully mechanical (a03). This is the first crack.
- **Ad hoc rescue.** Popper first banned rescue moves, then allowed some, for example the Uranus anomaly that led to Neptune. Later he spoke of degrees of testability and accepted "immunizations" (a05, a06).
- **Verisimilitude.** Popper tried to rank false theories by closeness to truth. In 1974 David Miller and Pavel Tichy each showed the definition fails for any two false theories. Popper conceded in 1979 (a04).

### 2.2 Standard objections

- **Duhem-Quine.** A failed prediction does not say which assumption failed: the theory or an auxiliary (Putnam 1974). Lakatos: a core theory sits inside a protective belt of auxiliaries (a05). For an agent: when a test fails, the fault may lie in the candidate, the test, or the setup.
- **Strict falsificationism rejected.** Philosophers judged it unfaithful to the history of science (Kuhn, Lakatos) and unworkable (Duhem, Quine, Putnam, Churchland) (a13). The modern view is Bayesian optimal data selection or error statistics.
- **Mayo's severity.** Mayo (2019) keeps Popper's insight and says he fell short on corroboration, Duhem's problem and demarcation. Severity is defined in error-statistics terms, which Bayesians contest. Only abstracts were read (a07).

### 2.3 The psychology branch: Wason and what followed

- **Wason (1960), the 2-4-6 task.** The participant sees 2-4-6, is told it fits a hidden rule, proposes triples, gets yes or no, and announces the rule. The rule is "any increasing sequence". Most tested triples that fit their own guess (for example "even numbers rising by 2") and became confident in a wrong rule. Wason read this as a failure to eliminate hypotheses (d01).
- **Klayman and Ha (1987).** The "confirmation bias" is better described as a **positive test strategy**: test cases you expect to have the target property. It is a good general heuristic. It fails exactly when the true rule is broader than the hypothesis (hypothesis nested inside the target). Then only negative tests (outside the hypothesis) can reveal the error. When the target is rare, positive tests often are the more informative choice (a09, a11, b01).
- **Oaksford and Chater (1994).** On the abstract selection task the usual "wrong" choice is predicted by expected information gain under a rarity assumption. The "falsification" answer was judged against an outdated philosophy of science (a12, a13).
- **Dual-Goal (DAX/MED).** Tweney et al. (1980) told people that the rule is DAX and everything else is MED. Solvers treated these as two hypotheses and tested each with positive tests, which tests the complement. Success rose greatly. The mechanism is two complementary hypotheses, not more negative tests (b02, b24).
- **Gale and Ball (2002).** A 2x2 design separated the number of goals from the labels. The advantage came with goal count, not labels (b03).
- **Wason selection task.** Fewer than 10% choose p and not-q on the abstract version (b23). Content, deontic rules and matching bias change this (a14, c21, c22, b08, d02).

### 2.4 The AI and machine-discovery branch

- **Early systems.** BACON-style systems drop laws that fail on new data; Robot Scientist Adam and Eve discard hypotheses that experiments contradict (c27, c28; not opened).
- **2024-2026.** Wason-style benchmarks for LLMs (WILT, Failing to Falsify, FalsifyBench, Numberwang); counterexample benchmarks (REFUTE); falsification-built agents (POPPER, Baby-AIGS, co-scientist). See section 6.

## 3. Core findings with exact numbers

Status: E established (two or more independent sources), S single source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People test what fits their guess on 2-4-6 | N=29: 6 right at first announcement, 13 one wrong, 9 two or more, 1 none; 21 eventually right. Disconfirming:confirming index 1.79 (n=6) vs 0.24 (n=22), p=0.0002; 8.0 instances before announcing for correct vs 3.68 | Wason 1960 (d01, original opened) | E (K01) |
| Positive testing is a general strategy, not bare irrationality | Fails only when H is nested in the target; Doherty and Falgout: 32 of 40 data-saving patterns were positive-test patterns | Klayman and Ha 1987 (a09, b01) | E (K02) |
| Dual-Goal / DAX-MED raises human success | Standard task about 20%; Dual-Goal at least double, about 60% (secondary) | Gale and Ball 2002 (b03); Tweney 1980 via b24 (not opened) | E (K03), exact rates second-hand |
| Disconfirmatory instruction helps when no guess-by-guess feedback | Gorman and Gorman: disconfirm group beat confirm and control; N and rates not read | b04 (abstract) | S |
| Think-in-opposites training, humans | 36.66% to 78.33%; N=120; chi2(1)=22.067, p<.001; 47 vs 22 correct; slower to solve F(1,67)=10.63 | Branchini 2023 (b05) | S (K04) |
| Opposites step is the active part | N=180: opposites 78.33%, properties-only 38.33%, control 36.66%; chi2(2)=27.986. Same lab; opposites and control rates identical to 2023 (47/60, 22/60) | Branchini 2025 (b06) | S, may share data |
| Abstract selection task: few choose p and not-q | Under 10% (some studies 4%); 46% p and q, 33% p alone, 7% p, q, not-q | b23, a12 | E (K05) |
| Selection task: content and matching explain much | LLM deontic gain 5.0 to 41.2 points; Chinchilla, PaLM 2-L, GPT-3.5 realistic-rule advantage z>2.2; 7B models about 30% vs humans about 70% on social rules | a14, c21, c22 | E |
| Executive learning raises logical choices a little | 3/42 logical pre; 26.6% post vs 0%; Fisher p=.02 | b08 | S, small |
| Selection task meta-analysis | 228 experiments; 99 with redundant selections vs 10,000 simulations; feedback shifts to counterexamples | Ragni et al 2018 (d02, abstract only) | S, contested (Kellen and Klauer) |
| One general confirmation factor in humans | N=200; confirming 69.1% vs disconfirming 48.2%, F(1,198)=158.12, d=0.89; search d=1.18, weighing 0.31, memory 0.59 | Berthet 2024 (b07) | S (K06) |
| Excess of positive results in published science | 44% (71 Registered Reports) vs 96% (152 standard papers); 50% vs 96% without direct replications | Scheel et al 2021 (b10) | E in effect (K19); observational |
| LLMs poor at 2-4-6 type games, 2024 | WILT 50 tasks per model: Claude 3.5 Sonnet 14/50 (28%), o1-mini 13, o1-preview 12, 4o-latest 11, Mistral Large 2 11, GPT-4o 9, Llama 405B 8, Haiku 3 1, Gemma 2 9B 0. Numberwang pilot: mean 11% of 10 rules, 4 of 11 models got 0 | a15, b16, c18, c20 | E (K07) |
| LLMs, 2026 numeric game | 11 models, 45 turns, 80 episodes per cell: success 6% to 78%. Average discovery 42% to 56% with prompts | Jhaveri et al 2026 (a16, b11) | E with FalsifyBench (K07) |
| LLMs, 2026 semantic game | 12 models x 100 games; GPT-5.2-Chat 75%, GPT-OSS-120B 68%, GLM-5 58%, DeepSeek-V3.1 41%, MiniMax-M2.5 35%, others instruction-tuned 33-35%, Qwen3.5-9B 21%, GPT-5-Nano 12% | FalsifyBench (a19, d09) | S per paper; fits K07 |
| Positive-test share predicts LLM failure | rho=-0.779 (p=0.003) with success; rho=-0.937 (p<0.001) with conclusive falsification; mixed-effects coefficient -4.148 (OR 0.016), n=1,200 games; oracle error -0.123 (OR 0.885, spans zero) | a20, b14, c09, c10 | E (K08, observational) |
| Positive-test share by model | 24.2% to 39.0% (GPT-OSS-20B, GPT-5.2-Chat, GPT-5-Mini) vs 66-82% instruction-tuned. Within model, won vs lost: GPT-5.2-Chat 20% vs 50%; GPT-OSS-20B 17% vs 53% | a20, a21 | S |
| Conclusive falsification rate | GPT-OSS-20B 59.2%, GPT-OSS-120B 53.4%, GPT-5.2-Chat 49.5%, GPT-5-Nano 26.6%, Llama-4-Maverick 18.0% | c10 | S |
| Failure is not only confirmation | Failed games have more partly overlapping or disjoint hypotheses (+27.0 pp GPT-5.2-Chat; +22.3 GPT-OSS-120B; +21.4 GLM-5); Llama-4-Maverick 8.5 guesses per failed vs 3.8 per won game | c11 | E (K12) |
| Thinking mode and I:C | Qwen3-8B 6% to 21% success; Qwen3-32B thinking 0.41 success but I:C 0.14; Gemini-2.5-Pro 0.73, I:C 0.66 | c04 | C (K09) |
| Think-in-Opposites, LLMs | Success up in 11 of 11 cells; Qwen3-32B thinking 0.41 to 0.61 (I:C 0.14 to 0.54); Qwen3-8B 0.21 to 0.36; QwQ-32B 0.50 to 0.59; Qwen3-14B thinking 0.34 to 0.48; Gemini 0.73 to 0.78; Llama-3.3-70B 0.21 to 0.38; GPT-4o 0.11 to 0.16 (I:C down 0.25 to 0.17) | Jhaveri 2026 (a17, d08, b26) | S (K10) |
| Dual-Goal, LLMs | Helps 8 of 11; non-thinking Qwen3-32B 0.33 to 0.10; Qwen3-14B 0.23 to 0.13 | b26 | S |
| Blicket transfer | Qwen3-32B thinking 0.57 to 0.86 with TiO (I:C 0.54 to 1.31); non-thinking 0.64 to 0.56; R1-distill 0.41 to 0.43; QwQ 0.80 to 0.82 | c07 | S |
| Distillation of the habit | 72,000 examples; 8B 0.21 to 0.35; 32B 0.41 to 0.64; 8B from 32B teacher 0.59; Blicket 32B 0.57 to 0.77 | c06, a18 | S, training (K11) |
| Solve vs refute | REFUTE 324 problems: o3-mini breaks under 9% (8.9% zero-shot, 9.3% few-shot, 6.8% ReAct, 8.6% ReAct with demo) vs 48.7% rating-implied solve; R1 44.0% solve, 5.2/4.6/8.6/6.5% | Sinha et al 2025 (b19, d03) | E (K13) |
| Refute with the correct solution in hand | o3-mini breaks 3% new submissions; 6% with randomized search; 35% of RandSearch samples end with a wrong counterexample, 86% of those from wrong brute-force code, 14% test-validation failures | c16, d03 | S |
| LLM experiment proposer vs random | Zendo: human 5.26/8; ReAct LLM 4.60/8; best model 6.55/8; LLM proposer about equal to random proposer | Piriyakulkij et al 2024 (c17) | S |
| Agentic sequential falsification | Type-I error near 0.1 vs baselines 0.117-0.311 (Self-Refine 0.248, ReAct 0.145 on DiscoveryBench); 66.5% more power than ReAct; 3.17x Self-Refine on TargetVal-IL2; 9 experts: no difference, 9.7x faster; failures: misread p-values 35.9%, weak design 28.1%, test breaks implication 17.2%, wrong code 8.6%, hallucination 0.8% | POPPER (a22, a23, b21, c12-c14) | S (K14) |
| Self-critique does not falsify | GPT-4 GSM8K 95.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 41.8; GPT-3.5 GSM8K 75.9 to 74.7 | Huang et al 2024 (c23) | S (K17); same direction as schema 4b [E] |
| Tests inherit code faults | Fault detection about 14% (code first, same session) vs about 25% (fresh session, task text only); exposing code costs 9.1-18.2 points. 5 LLMs, HumanEval+ 164, MBPP 974, BigCodeBench 1,140. Earlier: bug detection 47% worse on real-world incorrect code | Konstantinou 2026 (d06); Huang 2025 (d05) | E (K21), two sources |
| LLM tests catch few planted flaws | SWE-Mutation: 2,636 mutants, 7 LLMs, detection 25-72%, agentic mutants 71.04% to 39.81%; Hamidi 2026: over 6,000 faulty programs, detection often near zero | d11, d10 | E (K23), d11 is a leaderboard page |
| Blame assignment | 7 LLMs, 3,192 instances; doc faults found 67-94%; code-only faults 21-43 points lower; source ranking tau_b <= 0.10 for code faults | Ulfat et al 2026 (d04) | S (K22) |
| Sycophantic examples block discovery | N=557 (504 analysed): discovery random 29.5%, disconfirming 14.1%, agreeable 11.8%, confirming 8.4%, default GPT-5.1 5.9% (diff 23.6 pp); confidence change +5.4 default vs -56.8 random; F(4,507)=72.67 | Batista and Griffiths 2026 (a25, d07) | S (K16) |

## 4. Mechanisms and models

### 4.1 Set-relation model (Klayman and Ha)

Let H be the set of cases the current hypothesis says are positive. Let R be the true target set.
- **H inside R (H narrower, the 2-4-6 case).** Every positive test (a case in H) also lies in R, so the answer is always "yes". Nothing is learned. Only a negative test (a case outside H) can return "yes" and show R is wider.
- **H contains R (H broader).** A positive test can return "no" and falsify.
- **Partial overlap or disjoint.** Both kinds can falsify.
- **Base rate.** If the target is rare and H is about as large as R, false positives outnumber false negatives, so positive tests find more errors (a09).

Implementation: tag every test with the believed relation between H and R, and the expected answer under H and under the rival. Pick the test where the answers differ. If you cannot tell the relation, include both a case inside H and a case just outside H. FalsifyBench does exactly this tagging per turn (c10); its tagging used GPT-5-Mini and was not human-checked at scale.

### 4.2 Incompatible-to-compatible ratio (I:C)

Count tests that the current hypothesis says should fail (incompatible) over tests it says should pass (compatible). Wason's 1.79 vs 0.24 is the human version (d01). Jhaveri used the same ratio for LLMs (a16). It is a cheap diagnostic that code can compute once the hypothesis is written as a predicate. It is a proxy, not the mechanism (see 4.5).

### 4.3 Think-in-Opposites and Dual-Goal as prompts

- **Think-in-Opposites (TiO).** After a test, name one feature of it. Next test an instance that is the opposite on that feature. Humans: 36.66% to 78.33% (b05). LLMs: success up in 11 of 11 cells (d08).
- **Dual-Goal.** Hold two hypotheses: the rule and its complement. Each test then is a positive test for one of them. Needs a rule with a well-defined complement (c05). Humans roughly double; LLMs mixed, and it hurt some non-thinking models (b26).
- Implementation: a code-controlled turn that inserts the instruction before the next test, only when reasoning is on (see section 7).

### 4.4 Sequential falsification with e-values (POPPER)

1. Turn a free-text hypothesis into measurable sub-hypotheses, each a null test.
2. A relevance checker confirms each sub-hypothesis is truly implied by the main one. Removing it inflated Type-I error (a23, c14). Checker vs 3 human raters: Spearman 0.55 on 90 proposals.
3. Run the test on data; get a p-value; convert to an e-value.
4. Multiply e-values across tests. Stop and call the hypothesis supported when the product passes 1/alpha. Optional stopping is safe because the combined e-value is a valid test (a22).
5. Alpha 0.1; Type-I near 0.1, baselines up to 0.311.

Boundary: needs data, valid p-values, and a strong coding model; Haiku 3.5 had high Type-I error (b21). Applies where numeric tests exist.

### 4.5 Why prompts help: not only I:C

Within a fixed reasoning mode, TiO raised success in all 11 cells, but I:C fell in 4 of 22 interventions (GPT-4o I:C 0.25 to 0.17 while success went 0.11 to 0.16) (d08). Thinking mode raised success without consistently raising I:C (c04). Failed FalsifyBench games show partly overlapping hypotheses, not just positive tests (c11). So the likely mechanism is broader: more distinct, better-aimed tests, less repetition (Branchini 2025 also found less repetition of the same hypothesis, b06). Length confounds are not ruled out (d08).

### 4.6 Severity as measurable detection rate

Mayo's idea can be turned into a number: plant known flaws and measure the share the check catches. SWE-Mutation and Hamidi et al. do this for test suites (d10, d11). Implementation for our agent: take solved items, insert a known error into the answer, run the S4 check, log detection. A check with low detection is not severe, and a pass on it means little.

### 4.7 Independence of the tester

A test written after seeing the candidate inherits its flaw (d05, d06). A random-input generator that never sees the bad code gives validity but weak power (d03). Sycophantic examples drawn from the user's own hypothesis block discovery (d07). So test generation should be isolated from the candidate's reasoning. This matches schema S3 (fresh contexts) and G3.

### 4.8 Blame assignment (Duhem-Quine) as a procedure

After a failed test, list the three suspects: candidate, test, setup or assumption. Check the test against a second source (a held-out checker, a second independent test) before discarding the candidate. No LLM study measures this directly (K22). Closest: LLMs rank which source to distrust near chance for code faults (d04).

## 5. What holds up

**Holds (two or more sources, or replicated many times)**
- Humans choose tests that fit their hypothesis on 2-4-6. Replicated across many labs (Mynatt, Mahoney, Tweney, Wason and Johnson-Laird, Klayman and Ha) (a10). Original figures confirmed: 6 of 29 right first time (d01).
- Positive testing is a strategy that depends on the set relation. Three sources agree (K02).
- Complementary-goal framing helps humans. Gale and Ball plus Tweney (K03). Exact rates second-hand.
- LLMs do poorly on rule discovery: four independent benchmark families (WILT 28% best, Numberwang 11%, Failing-to-Falsify 6-78%, FalsifyBench 12-75%).
- Models and episodes that test more outside their hypothesis succeed more. Two papers, observational (K08).
- Solving does not imply refuting (REFUTE; Zendo; tests inheriting code faults; tests catching few planted flaws).
- Self-critique with no external signal does not falsify (c23; also in schema 4b).
- Pre-committing the test changes the pass rate (Registered Reports 44% vs 96%, observational).

**Failures, caveats and contested points**
- The Branchini 2025 paper is not an independent replication. Same lab, identical rates (78.33% and 36.66%, 47/60 and 22/60). Treat 78% as one study (critique.md).
- Gorman and Gorman found a gain for disconfirmatory instruction only when subjects got no feedback on guesses until the end; earlier studies with immediate feedback found none (b04, abstract only). A boundary condition.
- Reasoning models and incompatible testing: FalsifyBench says reasoning models test much more outside their hypothesis (24-39% positive vs 66-82%); Failing-to-Falsify says thinking mode does not consistently raise I:C. Tasks differ (WordNet, 20 turns vs integers, 45 turns). Contested (K09).
- Human debiasing tricks do not transfer cleanly: Dual-Goal doubles human success but cut non-thinking Qwen3-32B from 0.33 to 0.10 (b26).
- Small reasoning models did worse than instruction-tuned ones on FalsifyBench (GPT-5-Nano 12%, Qwen3.5-9B 21% vs 33-35%) (b13). Extended thinking alone does not help at small scale.
- Oracle quality does not explain LLM failure (OR 0.885, interval spans zero) (b14). But the oracle is itself an LLM (kappa 0.34-0.98).
- WILT: reasoning models guessed early and gathered too little evidence; o1-preview used 9 tests, 5 confirming, and left most budget unused (b17, c19). Test quality and deduction are separable skills; o1-mini deduced better from other models' tests than from its own (c19).
- Wason selection task: low scores are not simply a failure to falsify. Matching bias and rarity-based information gain explain much (a12, a14, c21). The meta-analysis is disputed (d02).
- Execution feedback barely helps counterexample finding (6.8-8.6% vs 8.9-9.3%); it mostly removes invalid counterexamples (d03).
- A snippet reading of HumanEval test accuracy "80% to 57%" conflicts with the abstract (+57%); not used (critique.md).
- Jhaveri's secondary mention of WILT "26%" is wrong; use 28% (14/50).

**Interventions that worked**
- Humans: think-in-opposites (36.66 to 78.33%, one lab); Dual-Goal (about 20% to 60%); disconfirmatory instruction with delayed feedback; feedback on one's own tests in repeated tasks (d02); executive learning, a little (26.6% logical).
- LLMs: TiO prompt for thinking models (0.41 to 0.61, 0.21 to 0.36, 0.34 to 0.48); distillation (training, not for us); random unbiased examples (humans with AI: 5.9% to 29.5%); fresh-session test writing (14% to 25% detection); code-based randomized counterexample search (adds distinct cases, small).

**Interventions that did not work**
- Dual-Goal on non-thinking LLMs (cut success).
- Telling the model in the prompt to falsify: Numberwang models stayed confirmatory (c20). Also in schema 4b.
- Self-critique, bias checklists (schema 4b).
- Giving the correct solution to a refuter (3%).
- Letting an LLM propose experiments (no better than random, Zendo).
- Using the LLM's own test after its own code (14% detection).

## 6. Language models

**Rule-discovery games**

| Benchmark | Setup | Result |
|---|---|---|
| WILT (2024) | Hidden 3-number Boolean rule, 30 tests, 50 tasks | Best 14/50 (28%) Claude 3.5 Sonnet; Gemma 2 9B 0/50 |
| Numberwang pilot (2024-25, blog) | 11 LLMs, 10 integer-list rules | Mean 11%, median 10%; 4 of 11 got 0; confirmation bias even when told to falsify; epicycles instead of dropping hypotheses |
| Failing to Falsify (2026) | 11 LLMs, 45 turns, 4 rule sets x 4 rules, 80 episodes per cell | Success 6% to 78%; I:C correlates positively with success; average discovery 42% to 56% with prompts |
| FalsifyBench (2026) | 12 LLMs, 100 WordNet games each, 20 turns, H nested in R | 12% to 75%; rho -0.779 positive-test share vs success |

How they behave:
- They propose triples that fit their own guess, then keep going with false confidence.
- Reasoning models test outside their hypothesis more (FalsifyBench), though the Jhaveri data do not show this consistently.
- Stronger models try to falsify more (WILT). Repeated tests per game ranged from 9.78 down to 0.06 across models (b16, c19; the two entries pair models differently, so use only as a direction).
- Reasoning models may stop too early (WILT) or exhaust the turn limit (FalsifyBench). Llama-4-Maverick 8.5 guesses per failed game vs 3.8.

What changed it, and by how much:
- Thinking mode: Qwen3-8B 6% to 21%.
- TiO prompt: +0.05 to +0.20 absolute for thinking models; Qwen3-32B 0.41 to 0.61; Gemini-2.5-Pro ceiling-bound (0.73 to 0.78).
- Distillation: 8B 0.21 to 0.35; 8B from 32B teacher 0.59.
- Non-thinking models: TiO +0.03 to +0.17; Dual-Goal -0.23 to about 0.
- Newest 2026 models did not close the gap on FalsifyBench (top 75%). No Claude or Gemini frontier model was listed (d09). Our own model is untested.

**Counterexample finding**
- REFUTE: best 8.9% / 9.3% vs 48.7% solve (o3-mini high). DeepSeek-R1 44.0% solve. Execution did not lift it. Cases were kept because random tests fail on them, so a random baseline is near zero by design (d03).
- Zendo: LLM proposer about equals a hand-coded random proposer (c17).
- Test writing: 25% to 72% detection of planted flaws by test suite (d11); near zero in another 6,000-instance study (d10).

**Agents that use falsification**
- POPPER: calibrated Type-I error, 66.5% more power than ReAct, human parity at 9.7x speed. Failures are statistical misreads (35.9%) and weak design (28.1%), not hallucination (0.8%).
- Baby-AIGS FalsificationAgent: near 100% executability, but experts rated its falsification below conference level (a24). The numbers for the falsification part are weak.
- AI co-scientist: reflection and deep verification as steps, plus Elo tournament of debate (c24). The debate part conflicts with guardrail G9. Falsification step not ablated in the numbers read.
- He et al 2026 (position paper, simulated physics): protect validation data, track intermediate evidence; abstract and intro only (c25).
- Mossel 2026: claims that LLMs reason do not meet Popper's refutability test because transcripts and training data are hidden; opinion (a26).

**Related LLM findings that bear on severity**
- Self-correction without feedback: GPT-4 GSM8K 95.5 to 89.0 (c23).
- Tests written after faulty code: about 14% detection vs about 25% (d06).
- Sycophancy: default GPT examples gave 5.9% discovery vs 29.5% random (d07). Humans formed the hypotheses; this is not an agent testing itself.

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep G3 as is: pass only on something the answer was not fitted to. Add that the test must be written without sight of the candidate's reasoning (task text and the held-out data only), by code where possible. | G3, S4 | [E] | K21 (d05, d06), K13, K19 |
| A2 | After a failed test, name the suspect before discarding: candidate, test, or setup. Check the test against a second source. Cheap, one line. | S5, G2 | [E] for the problem (K18: a03, a05, a13); the procedure itself is untested (see U4) | a03, a05, a13 |
| A3 | Do not rely on self-critique or verbal "try to falsify" instructions as the test. Already in schema 4b. Add the falsification evidence (c20, c23) to that row. | 4b | [E] | K17, K07 |
| A4 | Log the share of tests that fit the current hypothesis, and the planted-flaw detection rate of the S4 check, as diagnostics (not controls). | Section 6 logging | [E] as diagnostic value (K08, K23) | a20, c09, d10, d11 |
| A5 | S7 counterexample search: when two rules fit, run the input where they differ. Prefer generated tests that sit outside the winner's set. Already present; add the set-relation note: if the guess is narrower than the target, only outside cases test it. | S7, S4 | [E] (K02, K08) | a09, b01, a20 |
| A6 | Do not sample test inputs from the candidate's own hypothesis (the sycophancy loop). Use code-made mutated or random inputs. | S4, G3 | [S] single source, but consistent with K21 and K02; adopt as a design rule | a25, d07 |

### Test first (not yet established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Forced "opposite test" turn (TiO) in S4 for rule-induction items, reasoning mode on only. | S4, O4 | [S] | K10 (a17, b26, d08) |
| T2 | Two-complementary-hypotheses step (Dual-Goal) in S2/S4. | S2, S4 | [C] human yes, LLM mixed | K03, K10 (b26) |
| T3 | Estimate the H-to-target relation before choosing test type. | S4 | [C] no LLM test | K02, gap 10 |
| T4 | Aim for distinct, non-repeated tests and spend the test budget; stop early only after a discriminating test. | S4, S6 | [S] | K12 (b17, c11, b16) |
| T5 | Isolate the refuter from the candidate's code and compare with random-input generation. | S4 | [S] | K13, K21 |
| T6 | Show the result of the last test before choosing the next. | S4 | [S] human meta-analysis | K24 (d02) |
| T7 | Statistical sequential stop with e-values where numeric tests exist. | G3, G5 | [S] | K14 |
| T8 | Pre-commit the test before the candidate is seen (compare to post-hoc). | G3, S3 | [S] human only | K19 |

## 8. Concrete tests on our bench

All arms at equal tokens (setup cost counted, G7). Use the same items across arms; at least 3 seeds. IDs match UNKNOWNS.md.

1. **Opposite-test step vs plain vs best-of-N (U1).** Item type: 2-4-6 style rule-discovery games (numeric and WordNet-category), plus Blicket. Arms: plain agent; plain with a code-inserted TiO turn; best-of-N at the same tokens. Metric: rule found within the turn limit; also I:C and number of distinct tests. Expected: +0.10 to +0.20 absolute in thinking mode (from d08); no gain or a loss in non-thinking mode.
2. **Refuter on answer-checking items (U2).** Item type: wrong candidate solutions to coding or exact-answer problems with a held-out checker. Arms: random-input generator; LLM refuter that sees the code; LLM refuter that sees only the task; each at equal tokens. Metric: share of wrong candidates broken (valid counterexample). Expected: the blind refuter at least matches the sighted one; all well under the solve rate (REFUTE 9%).
3. **Planted-flaw detection of S4 (U3).** Item type: solved items with a known inserted error. Arms: S4 as is; S4 with isolated test writer; S4 with a TiO-style outside-case test. Metric: detection rate of the planted error and false-alarm rate on correct answers. Expected: isolated writer about +10 points (d06: 14% to 25%).
4. **Blame assignment (U4).** Item type: a failing test where we inject the fault into the test or into the candidate. Arms: discard-on-fail; suspect-naming step plus second check. Metric: share of correct blame; final accuracy. Expected: unknown; measure.
5. **Complement-hypothesis step (U5).** Item type: rule-discovery games with a clean complement. Arms: plain; Dual-Goal; TiO. Metric: success. Expected: help in thinking mode, hurt in non-thinking.
6. **Set-relation pre-estimate (U6).** Item type: games where H is broader than R, and games where H is narrower. Arms: plain; plain plus a relation-estimate step. Metric: success; rate of wasted positive tests. Expected: gain only in narrower-than-target cases; possible harm when H is broader.
7. **Budget use (U7).** Item type: games and items with a test budget. Arms: plain; rule "spend the budget on distinct tests before guessing". Metric: success; unused budget. Expected: gain on reasoning models that stop early (WILT).
8. **Sampling source of test inputs (U8).** Item type: candidate-check items. Arms: tests sampled by the model from its own hypothesis; code-mutated or random inputs. Metric: detection of planted flaws. Expected: random or mutated higher; magnitude unknown (5.9% to 29.5% in a human setting).
9. **Feedback visibility (U9).** Item type: multi-turn games. Arms: model sees all prior results; model sees only the last. Metric: success.

## 9. What does not transfer, and why

- **Human selection-task results.** The low p-and-not-q rate reflects matching bias and rarity assumptions more than failure to falsify (a12, a14). Our agent has no card task.
- **Human training effects (Branchini).** One lab, one task, and no check that the 2025 data are new (b05, b06). Humans learn a habit; our agent has no learning across runs except through memory lines.
- **Distillation and fine-tuning (K11).** We do not train.
- **POPPER's e-value machinery.** Needs data and valid p-values; most of our items are exact-answer puzzles with a checker (K14).
- **Registered Reports.** A community-level effect on publishing (44% vs 96%). The analogue for a single agent is pre-committing the test, but there is no evidence on that at agent level (K19).
- **Strict Popperian rules.** Falsification is never mechanical (basic statements are decisions, Duhem-Quine). A rule "drop on first failure" is wrong; G2 plus A2 already handle this.
- **Philosophical demarcation and verisimilitude.** Not needed for an agent; verisimilitude was refuted in 1974 (a04).
- **Autonomous-science falsification agents.** Baby-AIGS and co-scientist report weak numbers on falsification itself (K20); co-scientist uses debate (G9 forbids it).
- **P-Bench.** Measures validity of a hypothesis test run, not choice of a falsifying test; read from a summary page (b22).
- **Games built so negatives are needed.** In FalsifyBench H is narrower than R by design (c08). If H is broader than the target, forced negatives add little and may cost tests.

## 10. Open questions

1. Does a forced opposite-test step raise accuracy of a tool-using agent on answer-checking tasks, at equal tokens, against best-of-N? No paper measures it (K26, gap 1).
2. Is incompatible testing causal for LLM success? Gains also appear when I:C falls (d08). No mediation or token-matched test.
3. Can an independent lab reproduce Branchini's 36.66% to 78.33%? Unknown whether the 2025 sample is new.
4. Does the gap between solving and refuting close for current frontier models, including Claude? FalsifyBench lists none; REFUTE used early-2025 models.
5. How well do LLMs assign blame among candidate, test and assumption (Duhem-Quine)? Only code-fault proxies exist (d04, d05).
6. Does severity, measured by planted flaws, predict final accuracy of an agent?
7. Is hypothesis-sampling bias (sycophancy loop) present when an agent writes its own tests? Only human-hypothesis data (d07).
8. What are the original Tweney (1980), Gorman (1984) and Ragni (2018) numbers? Only abstract-level or second-hand.
9. Do the 2-4-6 effects hold in open-ended reasoning, math and code answer checking?
10. When H is broader than the target, does forcing negative tests hurt? Klayman and Ha predict a loss; no LLM test.
11. Who is right on reasoning models and incompatible testing, FalsifyBench or Failing to Falsify? Needs both designs on one model set.

## 11. Sources

[V] opened (full text, or abstract/page where noted); [M] snippet or second-hand only.

Philosophy and theory
- [V] Thornton, Stanford Encyclopedia of Philosophy: Karl Popper. https://plato.stanford.edu/entries/popper/ (a01-a05)
- [V] SEP: Scientific Method. https://plato.stanford.edu/entries/scientific-method/ (a06)
- [V, abstracts only] Mayo (2019) Statistical Inference as Severe Testing. https://errorstatistics.com/wp-content/uploads/2023/01/abstracts-and-keywords-sist-1.pdf (a07)
- [V] Klayman and Ha (1987). https://pages.ucsd.edu/~mckenzie/KlaymanHaPsychReview1987.pdf (a09-a11, b01, b02)
- [V] Oaksford and Chater (1994). https://pages.ucsd.edu/~mckenzie/OaksfordChaterPsychReview1994.pdf (a12, a13)
- [M] Klayman and Ha DOI listing. https://doi.org/10.1037/0033-295X.94.2.211 (c26)
- [M] Popper, Logik der Forschung and Conjectures and Refutations; Lakatos 1978; Putnam 1974 (cited through SEP, never opened)

Human experiments
- [V] Wason (1960) QJEP 12:129-140. https://bear.warrington.ufl.edu/brenner/mar7588/Papers/wason-qjep1960.pdf (d01)
- [M] Wason (1960) as restated in arXiv 2604.02485 (a08, b25, c02)
- [V, abstract] Gale and Ball (2002). https://eprints.lancs.ac.uk/id/eprint/11136/ (b03)
- [M] Tweney et al. (1980), via b03 (b24)
- [V, abstract] Gorman and Gorman (1984). https://digitalcommons.mtu.edu/michigantech-p/9453 (b04, d12)
- [V] Branchini, Burro, Bianchi (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10219317/ (b05)
- [V] Branchini et al. (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12402026/ (b06)
- [V] Berthet et al. (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11561113/ (b07)
- [V] Executive learning and the Wason selection task, PLoS One (2015). https://pmc.ncbi.nlm.nih.gov/articles/PMC4388638/ (b08)
- [V, abstract] Ragni, Kola, Johnson-Laird (2018). https://www.modeltheory.org/?p=954 (b09, d02)
- [V, abstract via Crossref] Scheel, Schijen, Lakens (2021). https://journals.sagepub.com/doi/10.1177/25152459211007467 (b10)
- [V] Wikipedia, Wason selection task. https://en.wikipedia.org/wiki/Wason_selection_task (b23)

LLM studies
- [V] Banatt et al. (2024) WILT. https://arxiv.org/abs/2410.10998 (a15, b16, b17, c18, c19)
- [V] Numberwang pilot (Alignment Forum). https://www.alignmentforum.org/posts/RSqfcyAW9ZkveGQ5u (c20)
- [V] Jhaveri et al. (2026) Failing to Falsify. https://arxiv.org/abs/2604.02485 and https://arxiv.org/html/2604.02485 (a16-a18, b11, b12, b26, c01-c07, d08)
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/abs/2606.04751 and https://arxiv.org/html/2606.04751 (a19-a21, b13-b15, c08-c11, d09)
- [V] Sinha et al. (2025) REFUTE. https://arxiv.org/abs/2502.19414 (b19, c15, c16, d03)
- [V] Piriyakulkij et al. (2024) Zendo and ActiveACRE. https://arxiv.org/abs/2402.06025 (c17)
- [V] Huang et al. (2025) POPPER. https://arxiv.org/abs/2502.09858 (a22, a23, b20, b21, c12-c14)
- [V, summary page] P-Bench and Fisher-R1. https://huggingface.co/papers/2608.07437 (b22)
- [V] Batista and Griffiths (2026). https://arxiv.org/abs/2602.14270 and https://arxiv.org/html/2602.14270 (a25, b18, d07)
- [V] Abe et al. (2026) deontic Wason. https://arxiv.org/pdf/2603.06416 (a14)
- [V] Lampinen et al. (2024) content effects. https://arxiv.org/abs/2207.07051 (c21)
- [V] Seals and Shalin (2024). https://arxiv.org/abs/2309.05452 (c22)
- [V] Huang et al. (2024) LLMs cannot self-correct. https://arxiv.org/abs/2310.01798 (c23)
- [V] Liu et al. (2024) Baby-AIGS. https://arxiv.org/abs/2411.11910 (a24)
- [V, partly] Gottweis et al. (2025) AI co-scientist. https://arxiv.org/abs/2502.18864 (c24)
- [V, abstract and intro] He et al. (2026) Auto-research. https://arxiv.org/abs/2608.09855 (c25)
- [V] Mossel (2026) refutability gap. https://arxiv.org/pdf/2601.02380 (a26)
- [V] Ulfat et al. (2026) trust allocation. https://arxiv.org/html/2604.03447v1 (d04)
- [V, abstract] Huang et al. (2025) incorrect code and tests. https://arxiv.org/abs/2409.09464 (d05)
- [V] Konstantinou et al. (2026) coding before testing. https://arxiv.org/html/2607.05139 (d06)
- [V, abstract] Hamidi et al. (2026). https://arxiv.org/abs/2609.09315 (d10)
- [V, leaderboard page] SWE-Mutation. https://benchmarklist.com/benchmarks/swe_mutation_can_llms_generate_reliable_test_suites_in_software_engineering/ (d11)
- [M] Multi-agent test generation for Java JSON libraries. https://arxiv.org/pdf/2410.09414 (d14)
- [M] LLMs as falsifiers for CPS, listed as 2609.20752. https://papers.cool/arxiv/2609.20752 (d15)
- [M] Tian et al. 2024 LLMs for mutation testing. https://arxiv.org/html/2406.09843v5 (d16)
- [M] King et al. Robot Scientist. https://doi.org/10.1038/nature02236 (c27)
- [M] Langley et al. (1987) Scientific Discovery. https://mitpress.mit.edu/9780262620529/ (c28)

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 12 established claims: 9 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D01.04-K02** (reworded: the sources support less). Klayman and Ha show positive tests can also falsify when the hypothesized set merely overlaps or is disjoint from the true rule, not only when it is broader; positive tests fail only when the hypothesis is a strict subset of the rule. Corrected claim: Positive testing is a general heuristic, not irrational by itself: a positive test can falsify a hypothesis when the hypothesis is broader than, overlaps, or is disjoint from the true rule, but it can never falsify when the hypothesis is a strict subset (narrower) of the true rule, where only negative tests can. Whether a test is informative depends on that set relation.
- **D01.04-K18** (reworded: the sources support less). SEP says Miller and Tichy showed in 1974 that Popper's verisimilitude definition is formally defective for false theories and Popper conceded the mistake but kept the concept as heuristic; Duhem-Quine is not named (Putnam and Lakatos are); the 'philosophers judged unworkable' line is not in the SEP pages; a03-a06 are all one SEP entry. Corrected claim: Philosophically, falsification is never fully mechanical: Popper says acceptance of basic statements rests on a decision or agreement (like a jury verdict); a failed prediction does not show which assumption is at fault (Putnam; Lakatos's protective belt); and Miller and Tichy showed in 1974 that Popper's definition of verisimilitude is formally defective for false theories, which Popper partly conceded. Oaksford and Chater (1994) state that philosophers regarded strict falsificationism as unworkable.
- **D01.04-K19** (now contested: a source does not say this). Neither listed source (Mayo abstracts, SEP Popper) contains the 44% vs 96% Registered Reports figures; they come from Scheel et al. (2021), which I confirmed (71 vs 152) but which is not in the evidence; Mayo PDF text was unreadable; 'change outcomes' is a causal reading of a between-paper-type comparison.
