# Classical propositional and first-order logic: deep document

*Subfield D03.01. Built from evidence_a-d.jsonl (a01-a25, b01-b25, c01-c28, d01-d22), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids are cited in brackets. [V] = opened and read; [M] = snippet or memory only.*

## 1. What it is

Classical logic is the standard formal system for valid argument. It has three parts.

- **Syntax.** A formal language: propositional letters and connectives (not, and, or, if-then). First-order logic adds predicates, variables and the quantifiers "for all" and "there exists".
- **Deduction.** Rules that turn premises into conclusions by form alone (modus ponens, modus tollens, hypothetical syllogism, proof by cases). A proof is a finite list of steps, each licensed by a rule.
- **Semantics.** A model assigns truth values (propositional) or a domain plus interpretations (first order). A set of sentences entails a conclusion if the conclusion is true in every model of the premises. A set is consistent if some model makes all of it true.

Three properties tie these together.

- **Soundness:** whatever you can derive is entailed.
- **Completeness (Godel 1929/30):** whatever is entailed can be derived. Equivalently, every consistent set has a model [a01, a02].
- **Limits:** first-order validity is only semi-decidable (Church 1936, Turing 1936-37). A prover can confirm a valid claim if it runs long enough, but may never halt on an invalid one. Propositional satisfiability is decidable but NP-complete (Cook 1971, Levin 1973) [a03, a04, a25].

Why it matters for our agent. In S4 (test) and S8 (verify) the agent often has to check that stated rules do not contradict each other, and that a conclusion really follows. "Rules contradict" is a satisfiability question. "Conclusion follows" is an entailment question. This document covers what is known about doing both, with humans, with solvers and with language models, 2020 to 2026.

Scope note. Most LLM work here uses synthetic or semi-synthetic benchmarks (PrOntoQA, ProofWriter, FOLIO, ProverQA, LogicBench, Multi-LogiEval, JustLogic, ZebraLogic, SATBench). Almost all report accuracy only. No study tests a prompted scaffold that checks stated rules for contradiction at equal tokens. That is the main gap (section 10).

## 2. History and theories in depth

**Frege (1879).** The Begriffsschrift gave the first full formal language with quantifiers and a proof calculus. It made logic a matter of form. Russell's letter of 16 June 1902 showed the naive set-theoretic system built on it was inconsistent [a05]. Lesson: a rule system that looks fine can hide a contradiction, and finding it is a real skill.

**Hilbert-Ackermann (1928).** Posed the completeness question for first-order logic cleanly and asked for a decision procedure (the Entscheidungsproblem) [a25].

**Godel (1929 thesis, 1930 paper).** Proved completeness of first-order logic. Henkin (1949) gave the modern model-existence proof; Hasenjaeger (1953) simplified it [a02]. The proof is not effective: it shows a model exists, not how to build it. Compactness and the Lowenheim-Skolem theorems follow (SEP Theorems 25-26) [a01]. First-order languages cannot pin down the size of a model.

**Church (1936) and Turing (1936-37).** Showed no algorithm decides first-order validity [a03]. Valid claims are findable by search. Invalid ones may not be refutable by any halting procedure.

**Cook (1971), Levin (1973).** Propositional satisfiability is NP-complete [a04]. Detecting a contradiction in a rule set is hard in the worst case even before quantifiers. Modern SAT and SMT solvers handle many real instances, with no promise of speed.

**Psychology of logic.** Two rival accounts of how people reason: mental rules (inference schemas applied in the head) and mental models (build and inspect possible situations). Humans are not logic machines. The most solid finding is belief bias (Evans, Barston and Pollard 1983), in sections 3 and 5. The dual-process review (Evans 2008) and the rules-versus-models debate were not opened [b25, M].

**Neural and LLM era.** RuleTaker (Clark et al. 2020) showed a fine-tuned transformer answers rule-based questions over English with about 99% accuracy in distribution and 95%+ on deeper chains [a10, c01]. ProofWriter (Tafjord et al. 2021) generated step-by-step proofs, +9% absolute proof correctness [a11, c02]. FOLIO (Han et al. 2022) moved to expert-written first-order problems and showed the easy synthetic result did not carry over [a06]. From 2023 two lines grew: (1) prompted chain of thought with analysis of where it fails (Saparov and He 2023), and (2) neuro-symbolic pipelines that translate to formal language and call a solver (Logic-LM, LINC, SatLM, Faithful CoT). From 2025 reasoning models (o1, R1, o3-mini, o4-mini) changed the picture again.

## 3. Core findings with exact numbers

Status: E = established, S = single-source, C = contested. Source ids in brackets.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Soundness, completeness, compactness hold for first-order logic; validity is semi-decidable; SAT is NP-complete | Godel 1929/30; Church 1936; Turing 1936-37; Cook 1971 | SEP, Wikipedia [a01-a04, a25] | E (K01) |
| LLM single steps are mostly valid; planning is the weak point | text-davinci-002, 5-hop fictional ontology: 93.2% steps strictly valid, 2.4% broadly valid, 5.9% invalid (as printed, sums to 101.5); only the largest model beat chance | Saparov and He 2023 [a08, b17, c03] | E (K02) |
| Models struggle with longer proofs and do not produce hypothetical subproofs (proof by cases) | qualitative, 2023 | Saparov et al. 2023 [c04] | E |
| Accuracy falls with proof depth | Multi-LogiEval mean over models: propositional 85.42 (depth 1) to 42.96 (depth 5); first order 83.21 to 32.96; GPT-4 propositional 89.17 to 66.67; items per depth 410/442/310/280/110 | Patel et al. 2024 [a21, c20] | E (K03) |
| Same on ProverQA | GPT-4o CoT easy 94.2, medium 79.4, hard 50.0; Claude-3.5-Sonnet 95.2/83.6/56.4; Llama3.1-70B 90.4/73.2/46.8 | Qi et al. 2025 [a22, b01, c13] | E (K03) |
| CoT gain shrinks with difficulty | Mean gain over standard prompting, 7 models: easy +12.86, medium +8.43, hard +3.86; ProntoQA +16.57, ProofWriter +14.36, FOLIO +5.41 | Qi et al. 2025 [b02] | S (K07) |
| Premise order matters | Drop over 30 points; GPT-4-turbo and PaLM 2-L lose 20-30; Gemini 1.0 Pro and GPT-3.5-turbo fall from over 65 to under 25. GPT-4-turbo, 12 rules, no distractors: forward order 96.5 vs 76.0-84.5 other orders | Chen et al. 2024 [a18, a19, b15] | E (K04), old models only |
| Under bad order the commonest error is fact hallucination | GPT-4-turbo, tau 0.5: correct 76.0, wrong refutation 10.5, rule hallucination 2.0, fact hallucination 11.5 | Chen et al. 2024 [b16] | S (K05) |
| Distractors and order hurt hard first-order items | GPT-4o CoT hard 50.0 (default), 57.4 (no distractors), 62.4 (no distractors, proof order); medium 79.4, 82.2, 87.4; easy 94.2, 94.4, 95.6 | Qi et al. 2025 [b03, c14] | S (K06) |
| Translation to FOL: valid syntax far above correct meaning | FOLIO few-shot GPT-4 syntactic validity 93.9 vs execution accuracy 63.8; zero-shot 86.1 vs 51.7; GPT-3.5 few-shot 93.3 vs 56.0, zero-shot 68.4 vs 50.4 | Han et al. 2024 [a07, b06, c12] | E (K08) |
| Translate-then-solve beats CoT on search-like tasks | GPT-4 ProofWriter standard 52.67, CoT 68.11, Logic-LM 79.66; AR-LSAT 33.33/35.06/43.04; LogicalDeduction 71.33/75.25/87.63. SatLM (code-davinci-002) ProofWriter 99.7 vs CoT 80.1, CLUTRR 68.3 vs 40.8, LSAT 35.0 vs 23.5, BoardgameQA 79.4 vs 60.7, GSM-Sys 69.4 vs 46.5 | Pan et al. 2023; Ye et al. 2023 [a12, a16, b12, c07] | E (K09), old models |
| Solver route does not always win | FOLIO GPT-4: CoT 75.3 vs LINC 72.5, McNemar p=0.58 (182 items); PrOntoQA GPT-4 CoT 98.79 vs Logic-LM 83.20; StarCoder+ LINC 56.0 vs CoT 41.8 | Olausson et al. 2023; Pan et al. 2023 [a14, c09, a12] | E (K10) |
| Solver and CoT make different errors | LINC fault types L1-L3 vs CoT C2 (invalid deduction); LINC syntax errors StarCoder+ 38%, GPT-3.5 24%, GPT-4 13% | Olausson et al. 2023 [b10, c10] | S (K11) |
| Repair loops raise executability, not always correctness | Logic-LM executable FOLIO GPT-4 79.9 to 85.8, GPT-3.5 66.7 to 84.3. Logic-LM++ GPT-3.5 FOLIO 62.80 to 62.25; GPT-4 78.92 to 84.80 with pairwise semantic check. VeriCoT reflection: pass rate +8 to +15, accuracy -1.7 (ProofWriter), +0.6 (BioASQ), +1.4 (SARA) | [a13, b08, c06, c16, d10, d11] | E (K12) |
| Solver UNSAT/AMBIG signals allow abstention | GSM-Sys selective accuracy 77% (SatLM) vs 45% (ProgLM), lower coverage. VeriCoT: only 15-45% of chains verify at 84-94% precision (ProofWriter 45.2/94.1, BioASQ 25.3/84.3, SARA 15.2/87.0). SymbCoT verifier: correct-by-flawed-reasoning 6% (CoT), 2% (no verifier), 0% (verifier); about 30% more output tokens; no coverage reported | [c08, d09, d14] | S (K13) |
| Benchmarks leak world knowledge | JustLogic: no-context gaps above random on FOLIO and LogiQA 2.0 (exact values not copied). Removing universal rules from 60 ProverQA items: GPT-4o CoT 68.33 to 45.00, direct 58.33 to 43.33; Llama-3.1-70B CoT 65.00 to 53.33 | [a23, a24, b04] | E (K14) |
| Reasoning models reach or pass humans on deduction but collapse on big search | JustLogic: human 73.0, R1 80.9, o1 72.9, GPT-4o 65.6, o1-mini 62.0, Llama3-70B 53.1, Llama3-8B 49.8, random 33.3. ZebraLogic overall: o1-full 81.0, R1 78.7, o1-preview 71.4, o1-mini 59.7, GPT-4o 31.7; X-Large: o1-full 42.5, R1 28.5. R1 CoT on FOLIO 86.2 vs Logic-LM 78.92. Knights and Knaves: o3-mini-high 0.94, R1 0.81, o1 0.42, GPT-4o 0.37 | [a23, d16, d17, d22, c25] | E (K15) |
| Belief bias, people | Evans et al. 1983, percent accepting. Exp 1 N=24: valid-believable 92, valid-unbelievable 46, invalid-believable 92, invalid-unbelievable 8. Exp 2 N=64: 88/56/72/13. Exp 3 N=32: 91/53/67/6. Exp 2 correct 87% when logic agreed with belief, 48% when it conflicted | [d01, d02] | E (K16) |
| Belief bias, models | Chinchilla, PaLM 2, Flan-PaLM 2, GPT-3.5 show the same content effect as people on NLI, syllogisms, Wason | Lampinen et al. 2024 [b18, b19, c21] | E (K16) |
| Belief bias is mainly response bias | Trippas et al. 2018: 22 studies, N=993; group-level ROC slopes near 1; believability does not change discriminability on average; individual differences moderate it | [d04] | E (K22), narrow wording |
| Rule type matters | LogicBench Yes-label accuracy: ChatGPT 48.04, GPT-4 63.98; GPT-4 hypothetical syllogism about 85, modus tollens about 59. Binary QA average: ChatGPT 81.9, GPT-4 89.6, Gemini 88.8, Llama-2 57.9. Models do better on No-label than Yes-label | [a20, b13, c18, c19] | E (K17) |
| Consistency failures on simple facts | Large LLMs break negation and implication consistency; semantic-loss fine-tune helps; plain SFT does not | Calanzone and Teso 2024 [b22, c17] | S (K18), training result |
| Weakness-targeted examples | LogicAsker: failure rates 29% to 90% across six LLMs on 25 rules; GPT-4o 91.92 to 97.23 | [b14] | S (K19) |
| All-LLM pipeline with verifier | SymbCoT gains over Naive/CoT/Logic-LM: GPT-3.5 +21.56/+6.11/+3.53; GPT-4 +22.08/+9.31/+7.88. Exception: FOLIO GPT-3.5 below Logic-LM | Xu et al. 2024 [b20, c15] | S (K20) |
| Fine-tuning on solver traces | LoGiPT 13B about 81-90% on ProofWriter/PrOntoQA; parse success CodeLlama-13B-Base 0.33%, Instruct 71.3%; ProverQA finetune +21 to +44 | [c23, c14] | E (K21), training |
| Inconsistency detection in small rule sets | SATBench easy UNSAT o4-mini 98.2, R1 98.2; hard UNSAT o4-mini 65.0, R1 83.6, DeepSeek-V3 74.3, Claude-3.7 42.1, GPT-4o 18.9; hard SAT 66.7 vs hard UNSAT 39.3 over 20 models; overall o4-mini 89.3, R1 87.8, GPT-4o 58.0 (random 50) | Wei et al. 2025 [d05, d06] | S (K23) |
| Naming the conflicting subset is harder | SATQuest overall: o3-mini 0.56, R1 0.42, QwQ-32B 0.40, GPT-4.1 0.38; MUS and MCS tasks lowest | Zhao et al. 2025 [d08] | S (K24) |
| Right label, invalid trace | o4-mini SAT label 94.7 vs trace valid 74.6; Claude-3.7 83.2 vs 47.4. Errors: satisfiability bias (o4-mini 68.7%), context inconsistency (R1 44.7%), condition omission (about 13%) | [d06] | S (K25) |
| Back-translation checks: mixed | 97/100 clauses faithful after solver equivalence filter (SATBench); Logic-LM++ GPT-4 +5.9, GPT-3.5 -0.55; LLM-ARC 8-shot +6.6; VeriCoT reflection leaves meaning errors | [d07, d10, d11, d21] | C (K26) |
| Counter-model check vs LLM judge | NL2FOL SMT counter-model F1 0.78 (LOGIC), 0.80 (LogicClimate) vs GPT-4o judging same forms 0.66, 0.73; end-to-end GPT-4o 0.96/0.58, o1-preview 0.93 on LOGIC; 54% of pipeline errors were missing background knowledge | Lalwani et al. 2025 [d12, d13] | S (K27) |
| Selection is the bottleneck | ZebraLogic GPT-4o baseline 31.7; majority vote N=32 38.0 (N=128 37.6); reward model N=32 34.8; oracle best-of-32 60.3, of-128 69.1 | Lin et al. 2025 [d18] | S (K28) |
| Distractors hurt reasoning models | R1 error 1.5% to 4.5% (3x) on 225 math items; R1-distill-Qwen-32B 8.0% (2.83x); outputs 1.5x longer in 17-42% of cases | Rajeev et al. 2025 [d20] | S (K29), math not logic |
| Contraposition step | Logic-of-Thought FOLIO subset N=135: GPT-4 Direct 82.96, LoT 83.55 (+0.59); ablation without contraposition 76.00 to 72.22 (-3.8); model labels in the table are inconsistent | Liu et al. 2024 [d15] | S (K30) |
| Answer accuracy vs soundness | ProverQA Hard outcome-RL: answer correct 91.31, GPT-judged sound 21.97 (Extra: 86.96 vs 11.87); formal step verification raised soundness to 76.1 at accuracy 92.97 | Chen et al. 2026 [d19] | S (K31) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it.

**4.1 Satisfiability check on a rule set (the S4/S8 contradiction test).**
1. Parse each stated rule into a formula. For propositional rules: one symbol per atomic claim, one clause per rule.
2. Conjoin all formulas. Ask a SAT or SMT solver for a model.
3. SAT means consistent. UNSAT means a contradiction exists. A timeout means "undecided", never "consistent" (K01).
4. To locate the conflict, find a minimal unsatisfiable subset: drop rules one at a time and re-solve, or use the solver's core.
5. Entailment is the same call: add the negated conclusion. UNSAT means the conclusion follows. SAT gives a counter-model, a concrete witness the agent can show.

For first order, bounded model finding (small finite domains) catches many invalid claims but cannot prove validity. It can only confirm "no counter-model up to size n".

**4.2 Translate, solve, interpret (Logic-LM, LINC, SatLM).**
1. The LLM turns the problem text into formal language: first-order formulas, a constraint program, or declarative SAT-style code. SatLM writes the spec and does not compute the answer.
2. A solver (Prover9, Z3) returns True / False / Uncertain, or UNSAT / AMBIG for the spec.
3. Optional repair: feed solver error text back to the LLM for a fixed number of rounds (Logic-LM) [b08].
4. Failure points: meaning errors in translation (valid syntax, wrong content; K08), inconsistent predicate arity (LINC's most common syntax error), and information lost in translation (K11). A solver is only as right as the translation.
5. Gating idea (untested): call the solver only when CoT samples disagree or proof depth is high (K10, K28).

**4.3 Fully prompted symbolic chain (SymbCoT).** Four LLM roles in sequence: translate to symbols, plan, solve step by step, verify chain and translation. No external prover. The verifier costs about 30% extra output tokens [d14]. Gains +6.1 (GPT-3.5) and +9.3 (GPT-4) over CoT on average [b20].

**4.4 Step-level validity checking.** The model emits one inference per line, tagged with the rule used and the source lines. A checker (a second LLM pass or a formal verifier) rejects any step with no source line. This targets fact hallucination (K05) and the gap between right label and valid trace (K25, K31). VeriCoT does this with an SMT verifier: it verifies only 15-45% of chains but at 84-94% precision [d09]. Treat "unverified" as a third outcome, not as "wrong".

**4.5 Restate in dependency order.** Before reasoning, list premises in the order they will be used (forward-chaining order). Premise Order and ProverQA both find forward order best [a19, c14]. The step costs tokens and can add its own errors. Untested on reasoning models.

**4.6 Relevance filter.** Mark which premises can reach the question through shared predicates or entities, drop the rest. Removing distractors alone lifted GPT-4o hard accuracy 50.0 to 57.4 [c14].

**4.7 Contrapositive and negation expansion.** For each if-then rule, write the contrapositive and the explicit negation cases. Aimed at modus tollens, the weakest common rule (GPT-4 about 59 vs about 85 for hypothetical syllogism) [c19]. Evidence for the step alone is weak (K30).

**4.8 Belief separation.** Judge the argument form first with content replaced by neutral symbols, then compare with how believable the conclusion is. Log false-accept and false-reject separately by whether the conclusion sounds true (K22). This follows from the response-bias account [d04].

**4.9 Trace validity audit.** After the label, check every clause or step against an explicit assignment. SATBench error types give the checklist: satisfiability bias (defaulting to "satisfiable"), context inconsistency, condition omission [d06].

## 5. What holds up

**Holds up well (several groups, several models).**
- Accuracy falls with proof depth: Multi-LogiEval, ProverQA, PrOntoQA, ZebraLogic all agree [a21, a22, a08, d17].
- Syntactically valid translation is much more common than correct translation [a07, b06, b10].
- Premise order and irrelevant premises change answers [a18, c14, d20]. The order result is from four 2023-24 models. The distractor result on reasoning models is on math.
- Rule type matters: modus tollens and negation are harder than hypothetical syllogism [c19, d16].
- Content and belief effects exist in people and in models [d01, d02, b18]. Trippas et al. 2018 (22 studies, N=993) supports a response-bias account on average [d04]. Earlier notes b23 and b24 conflicted (reasoning flaw vs response bias); the opened papers settle only the group-level claim. Dube et al. 2010 and Heit and Rotello 2014 were not opened.
- Benchmarks leak world knowledge [a24, b04].

**Contested or mixed.**
- Solver versus CoT. Large wins on weaker models and search-like tasks (ProofWriter +11.5 for GPT-4; SatLM +19.6). No win or a loss on strong models and short deduction (LINC GPT-4 FOLIO p=0.58; PrOntoQA CoT 98.79 vs 83.20). R1 CoT alone scores 86.2 on FOLIO, above the GPT-4 solver pipelines [d16]. The solver advantage may shrink with reasoning models, but nobody compared at equal tokens.
- Repair loops raise executability reliably and accuracy unreliably. Logic-LM++ pairwise check: GPT-4 +5.9, GPT-3.5 -0.55. VeriCoT reflection moved accuracy -1.7 to +1.4 [d10].
- Back-translation: sources disagree (K26). No catch-rate study exists.

**Failed or weak.**
- Plain supervised fine-tuning did not fix consistency (model says false to everything) [c17].
- Majority vote and reward-model selection barely help on ZebraLogic (31.7 to 38.0 and 34.8) while the oracle reaches 60.3 [d18].
- More votes do not repair unsound chains [d19].
- Contraposition: only a bundled ablation; GPT-4 total gain +0.59 [d15].

**Moderators.**
- Model strength: solver gains concentrate in weaker models (StarCoder+ +14.2, GPT-3.5 +7.7) and vanish for GPT-4 on FOLIO.
- Task type: search-like (ProofWriter, LSAT, ZebraLogic) benefits; short deduction (PrOntoQA) does not.
- Size: SAT/UNSAT detection falls with clause count; hard UNSAT runs from 18.9 (GPT-4o) to 83.6 (R1).
- Knowledge: pipelines lose on familiar content where end-to-end models use background knowledge (54% of NL2FOL errors) [d13].
- Individual differences in people moderate belief bias [d04].

**Data quality notes (from the critique).**
- Many evidence lines are the same paper (ProverQA, FOLIO, Logic-LM, LINC, SatLM, Premise Order, LogicBench), not replications. Independent-source counts in claims.jsonl count papers.
- Metric names matter. LogicBench Yes-label (48.04, 63.98) differs from binary-QA average (81.9, 89.6). Multi-LogiEval table means (85.4 to 43.0) differ from the abstract (about 68 to about 43), which covers all logic types.
- The Saparov step split sums to 101.5 as printed. Treat as approximate.
- Not re-checked: a14 "Uncertain 57% vs 41%", JustLogic Table 4 values, b22 consistency metrics, c27/c28 numbers, LoGiPT ranges, LogicAsker figures.
- Evans 1983 numbers recalled earlier (89/56/71/10) were close; the opened Exp 2 values are 88/56/72/13 [d02].

## 6. Language models

**Behaviour in 2022-2024 models.**
- One-step inference is mostly valid. Failures lie in choosing which valid step to take and in long chains [a08, c03]. Only the largest model tested beat chance on 5-hop top-down proofs.
- Accuracy falls sharply with depth. GPT-4 on Multi-LogiEval propositional: 89.17 to 66.67 from depth 1 to 5 [a21].
- Premise order: GPT-4-turbo 96.5 forward vs 76.0 at the worst setting; Gemini 1.0 Pro and GPT-3.5 fall from over 65 to under 25 [a19, b15]. Fact hallucination (inventing an unproven fact) is the main error [b16].
- Rule gaps: GPT-4 modus tollens about 59 vs hypothetical syllogism about 85 on Yes-label items [c19]. Models do better on "No" than "Yes" [b13].
- Content effects mirror humans [b18].

**What changed it, and by how much.**
- Chain of thought: +12.9 easy, +8.4 medium, +3.9 hard on ProverQA (mean of 7 models); +16.6 on ProntoQA [b02].
- Solver pipelines (GPT-4, Logic-LM over CoT): ProofWriter +11.5, FOLIO +8.3 (78.92 vs 70.58), LogicalDeduction +12.4, AR-LSAT +8.0, PrOntoQA -15.6 [a12]. LINC on FOLIO GPT-4: -2.8, not significant [a14].
- Declarative prompting (SatLM, code-davinci-002) over CoT: ProofWriter +19.6, CLUTRR +27.5 [c07].
- Prompted symbolic chain (SymbCoT): +9.3 over CoT for GPT-4 [b20].
- Removing distractors and ordering premises: GPT-4o hard 50.0 to 62.4 (+12.4) [c14].
- Targeted examples (LogicAsker): GPT-4o 91.9 to 97.2 [b14].
- Training on prover-generated data: +21 to +44 on ProverQA [c14]. Out of scope for a prompted agent.

**2025-2026 reasoning models.**
- JustLogic: R1 80.9, o1 72.9 vs human average 73.0 [a23].
- FOLIO: R1 CoT 86.2, above the 2023 GPT-4 pipelines [d16].
- Knights and Knaves: o3-mini-high 0.94, R1 0.81, o1 0.42, GPT-4o 0.37 [d22]. "Reasoning model" is not one thing.
- ZebraLogic: o1-full 81.0, R1 78.7 overall; X-Large 42.5 and 28.5. They spend about 10x the hidden reasoning tokens [d17, c26].
- SATBench: o4-mini 89.3, R1 87.8 vs GPT-4o 58.0 (random 50). Hard UNSAT: o4-mini 65.0, R1 83.6 [d05]. Labels outrun traces by 10-30 points on SAT [d06].
- SATQuest: o3-mini shortens its reasoning and invents shortcuts at high complexity [d08].
- ProverQA Hard: outcome-RL 7B reaches 91.3% answers but 22.0% sound chains [d19].
- Distractors: R1 math error 1.5% to 4.5% [d20].

**Reading this honestly.** Reasoning models have closed much of the gap solver pipelines were built for, on small and medium problems. Large search and chain validity are still weak. Nobody has re-run the premise-order, back-translation or solver-gating tests on them. All numbers are benchmark accuracy, nearly all on synthetic or semi-synthetic data.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = stored claims. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Treat "consistent" as a claim that needs a witness, and "undecided" as a legal answer.** The verifier gets a step budget; a timeout reports "undecided". Part: G (verify) / S8. [E] K01. Evidence a01-a04, a25.
2. **Do not trust a correct-looking label; check the trace.** Each derived line cites which given lines it came from. Part: S8 / G (no unsupported claim). [E] that planning is the weak point (K02); sizes of the label-vs-trace gap are [S] (K25, K31). Evidence a08, c03, d06, d19.
3. **Separate form from content in verify.** Judge validity on neutral symbols first, then look at believability. Report false-accept and false-reject separately by whether the conclusion sounds true. Part: G (belief separation) / S8. [E] K16, K22. Evidence d01, d02, d04, b18.
4. **A formalisation that parses is not a correct formalisation.** Require the formal form to be read back in English and compared before use. Part: S8 / O-formalise. [E] for the problem (K08). The read-back fix is [C] (K26), so treat it as a flag, not a proof. Evidence a07, b06, c12.
5. **Expect accuracy to drop with chain length; plan for it.** Break long derivations into steps checked one at a time. Part: S4 / O-plan. [E] K02, K03. Evidence a21, a22, c03, c04, c02.
6. **Order premises by dependency and drop irrelevant ones as low-cost hygiene.** [E] that order and distractors matter (K04); the fix at equal tokens is untested (see U3). Part: S2 / O-restate, O-filter. Evidence a18, a19, c14.
7. **Flag known weak rule types: modus tollens, negation, implicit premises.** Write the contrapositive for these only. Part: S8 / O-contrapositive. [E] that they are weak (K17); [S] that the line fixes it (K30). Evidence c18, c19, d15, d16.
8. **Use a real solver when the task is search-like and the model is not a strong reasoner.** Part: S8 / tools. [E] K09, K10. Evidence a12, a14, a16, c07.
9. **Evaluate our scaffold on counterfactual or nonsense-content items and report by depth and rule type.** Part: eval hygiene. [E] K14, K03. Evidence a24, b04.
10. **Memory pre-use check.** Test stored claims pairwise for p vs not-p, and for p, p implies q, not-q. Part: memory. [S] (K18); cheap, plain consistency pass. Evidence b22, c17.

### Test first

- Required clause-by-clause assignment for contradiction detection (K23, K25). [S]
- Abstain outputs UNSAT / AMBIG / undecided and selective accuracy (K13). [S]
- Back-translate-and-compare step (K26). [C]
- Restate in dependency order on reasoning models (K04, K29). [E] on old models, unmeasured on new.
- Sample disagreement as solver trigger (K11, K28). [S]
- Standalone contrapositive line (K30). [S]
- Counter-model search in S8 for invalid conclusions (K27). [S]
- Minimal conflicting subset request (K24). [S]
- Soundness-judged comparison of scaffolds (K31). [S]
- Prompt-only verifier (SymbCoT style) ablation at equal tokens (K20). [S]

Training and example-library results (LogicAsker K19, LoGiPT and ProverQA finetune K21) are not taken.

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (hidden reasoning plus output). Report accuracy with a 95% interval, and trace soundness where noted. Use at least two models, one non-reasoning and one reasoning.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hidden-conflict rule sets: 10, 30, 50 plain-English rules, one seeded contradiction, plus matched consistent sets, 100 items per size | A: free CoT. B: required clause-by-clause assignment, stating the model or the conflicting pair | UNSAT detection, false-alarm rate on SAT, trace validity | B raises hard-size detection and lowers the "satisfiable" default; +10 points or more on weak models; small on R1-class |
| T2 | Same sets plus underdetermined cases and a budget cap | A: forced answer. B: consistent / contradictory / underdetermined / undecided | Selective accuracy at coverage; accuracy of answered items | B higher selective accuracy at some coverage cost; measure the cost |
| T3 | FOLIO and ProverQA hard items with shuffled premises and distractors, 200 items | A: raw order. B: restate in dependency order and drop irrelevant premises, then reason | Accuracy; fact-hallucination rate | B +5 or more on hard tier for non-reasoning models; unknown for reasoning |
| T4 | 100 formalisations with 20 planted meaning-changing errors (swapped quantifier, dropped negation, reversed implication) | A: no check. B: back-translate to English and compare to source | Catch rate, false-flag rate, tokens | B catches over half; cost within 30% extra tokens |
| T5 | Mixed FOLIO/ProverQA items, 5 CoT samples each | A: single CoT. B: solver or verifier called only on disagreement. C: solver always | Accuracy at equal tokens; AUC of disagreement as error predictor | B matches C at lower cost if disagreement predicts error |
| T6 | Modus tollens, negation, contrapositive items (LogicBench style), 150 items | A: plain. B: write contrapositive and negation of each rule first | Accuracy on modus tollens items | B +5 on non-reasoning models; near zero on reasoning |
| T7 | Invalid-conclusion items (fallacies, non-sequiturs) in plain English | A: attempt a proof. B: build a small counter-model, then judge | F1 for invalid detection | B better on invalid, equal or worse on valid |
| T8 | Syllogisms crossing validity and believability, 4 cells x 50 | A: plain. B: judge form on neutral symbols first | False-accept in invalid-believable cell; false-reject in valid-unbelievable | B halves invalid-believable acceptance |
| T9 | Stored-claim sets with planted p / not-p and p, p implies q, not-q contradictions | A: no check. B: pairwise consistency pass before use | Contradictions caught; cost | B catches nearly all direct ones; fewer indirect |
| T10 | Any of T1-T3, scored for chain soundness | A: free steps. B: step source tags with a source check | Soundness rate; accuracy minus soundness gap | B shrinks the gap |

## 9. What does not transfer, and why

- **Fine-tuning gains** (RuleTaker 99%, LoGiPT, ProverQA +21 to +44, Logic-RL, semantic-loss consistency). Our agent is a scaffold, not trained. These show the skill is learnable, not that a prompt gives it [c01, c23, c17].
- **Solver wins on 2023 models.** Logic-LM, LINC and SatLM used GPT-3.5, GPT-4, StarCoder+ and code-davinci-002. R1 CoT already beats those pipelines on FOLIO [d16]. The size of today's solver gain is unknown.
- **Random CNF puzzles (SATBench, SATQuest).** Clauses are arbitrary, not realistic rule sets. Detection rates may be too high or too low for real specs [d05, d08].
- **Human belief-bias experiments.** Four-problem syllogism tasks with undergraduates. They give the direction (check form apart from believability) and a measurement recipe, not the size for an LLM [d01, d02].
- **Synthetic fictional ontologies (PrOntoQA).** Rules are clean and complete. Real rule sets are vague, partly inconsistent and open to interpretation.
- **A full prover guarantee.** First-order validity is semi-decidable. No scaffold can promise to refute every invalid claim (K01). Bounded counter-model search gives only "no counter-model up to size n".
- **Distractor results from math** (R1 1.5% to 4.5%). Different task; a signal only [d20].
- **Benchmark scores as proof of logic.** World-knowledge leakage (K14), label-without-valid-trace (K25, K31) and missing background in pipelines mean accuracy overstates reasoning.
- **Foundations source quality.** Frege, Godel, Church, Turing and Cook rest on SEP and Wikipedia, not the original papers. Fine for dates, weak for detail.

## 10. Open questions

1. Does a solver or consistency step still help reasoning models on FOLIO and ProverQA hard at equal total tokens? (Partly answered: R1 CoT beats old pipelines; no equal-token comparison.)
2. How well can an LLM detect inconsistency in realistic natural-language rule sets, not random CNF? At what size does it break?
3. How often does back-translation catch a meaning error, and at what token cost? No catch-rate study exists.
4. Do premise-order effects persist in 2025-2026 reasoning models, and does restating in dependency order recover them?
5. Can disagreement among CoT samples predict when a solver call is worth making? ZebraLogic oracle headroom (60.3 vs 38.0) says selection is the bottleneck.
6. Does a standalone contrapositive step help, and for which models?
7. Does bounded counter-model search beat proof search in S8, and for which problem types?
8. Can a prompt-only verifier give usable abstain signals, and at what coverage? SymbCoT gave no coverage figure.
9. How much of belief bias in LLMs is response bias and how much lost discrimination? The human meta-analysis says response bias on average. No ROC-style study of models was found. Dube et al. 2010 and Heit and Rotello 2014 were not opened.
10. How big is the gap between answer accuracy and chain soundness for prompted (not RL-trained) reasoning models?
11. Does a "name the minimal conflict, then check pairwise" step work better than free-form conflict naming?

## 11. Sources

Opened [V] unless marked [M]. Many ids point to the same paper.

**Foundations**
- [V] SEP, Classical Logic (first 100,000 of 124,709 chars). https://plato.stanford.edu/entries/logic-classical/ (a01)
- [V] Wikipedia, Godel's completeness theorem. https://en.wikipedia.org/wiki/G%C3%B6del%27s_completeness_theorem (a02)
- [V] Wikipedia, Entscheidungsproblem (Church, Turing). https://en.wikipedia.org/wiki/Entscheidungsproblem (a03, a25)
- [V] Wikipedia, Cook-Levin theorem. https://en.wikipedia.org/wiki/Cook%E2%80%93Levin_theorem (a04)
- [V] SEP, Gottlob Frege (first 100,000 of 127,435 chars). https://plato.stanford.edu/entries/frege/ (a05)

**Benchmarks and LLM analysis**
- [V] Han et al. (2022/2024) FOLIO. https://arxiv.org/abs/2209.00840 (a06, a07, b05, b06, c11, c12)
- [V] Saparov and He (2023) Language Models are Greedy Reasoners. https://arxiv.org/abs/2210.01240 (a08, a09, b17, c03)
- [V] Saparov et al. (2023) Testing the General Deductive Reasoning Capacity of LLMs. https://arxiv.org/abs/2305.15269 (c04)
- [V] Clark, Tafjord, Richardson (2020) Transformers as Soft Reasoners. https://arxiv.org/abs/2002.05867 (a10, c01)
- [V] Tafjord et al. (2021) ProofWriter. https://arxiv.org/abs/2012.13048 (a11, c02)
- [V] Chen et al. (2024) Premise Order Matters in Reasoning with LLMs. https://arxiv.org/abs/2402.08939 (a18, a19, b15, b16)
- [V] Parmar et al. (2024) LogicBench. https://arxiv.org/abs/2404.15522 (a20, b13, c18, c19)
- [V] Patel et al. (2024) Multi-LogiEval. https://arxiv.org/abs/2406.17169 (a21, c20)
- [V] Qi et al. (2025) ProverGen / ProverQA. https://arxiv.org/abs/2502.06563 (a22, b01-b04, c13, c14)
- [V] Chen, Zhang and Tao (2025) JustLogic. https://arxiv.org/abs/2501.14851 (a23, a24, d16)
- [V] Wan et al. (2024) LogicAsker. https://arxiv.org/abs/2401.00757 (b14)
- [V] Lin et al. (2025) ZebraLogic. https://arxiv.org/abs/2502.01100 (c25, c26, d17, d18)
- [V] Wei et al. (2025) SATBench. https://arxiv.org/abs/2505.14615 (d05, d06, d07)
- [V] Zhao et al. (2025/2026) SATQuest. https://arxiv.org/abs/2509.00930 (d08)
- [V] Xie et al. (2025) Logic-RL (Knights and Knaves table). https://arxiv.org/abs/2502.14768 (d22)
- [V] Rajeev et al. (2025) Cats confuse reasoning LLM. https://arxiv.org/abs/2503.01781 (d20)

**Neuro-symbolic pipelines**
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (a12, a13, b07, b08, c05, c06)
- [V] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 (a14, a15, b09-b11, c09, c10)
- [V] Ye et al. (2023) SatLM. https://arxiv.org/abs/2305.09656 (a16, b12, c07, c08)
- [V] Lyu et al. (2023) Faithful Chain-of-Thought. https://arxiv.org/abs/2301.13379 (a17, b21, c22)
- [V] Kirtania et al. (2024) Logic-LM++. https://arxiv.org/abs/2407.02514 (c16, d11)
- [V] Xu et al. (2024) SymbCoT. https://arxiv.org/abs/2405.18357 (b20, c15, d14)
- [V] Feng et al. (2025) VeriCoT. https://arxiv.org/abs/2511.04662 (d09, d10)
- [V] Feng et al. (2023) LoGiPT. https://arxiv.org/abs/2311.06158 (c23)
- [V] Liu et al. (2024) Logic-of-Thought. https://arxiv.org/abs/2409.17539 (c24, d15)
- [V] Kalyanpur et al. (2024) LLM-ARC. https://arxiv.org/abs/2406.17663 (d21)
- [V] Lalwani et al. (2025) NL2FOL. https://arxiv.org/abs/2405.02318 (d12, d13)
- [V] Chen, Zhou and Zhang (2026) PRoSFI. https://arxiv.org/abs/2603.29500 (d19)
- [V] Jiang et al. (2023) Draft, Sketch, and Prove. https://arxiv.org/abs/2210.12283 (c27; numbers not re-checked)
- [V] Wu et al. (2022) Autoformalization with LLMs. https://arxiv.org/abs/2205.12615 (c28; numbers not re-checked)
- [V] Calanzone and Teso (2024) Logically Consistent LMs via Neuro-Symbolic Integration. https://arxiv.org/abs/2409.13724 (b22, c17; metric values not extracted)

**Psychology**
- [V] Evans, Barston and Pollard (1983). https://link.springer.com/content/pdf/10.3758/BF03196976.pdf (d01-d03); earlier snippet record [M] https://doi.org/10.3758/BF03196976 (b23)
- [V] Trippas et al. (2018) Characterizing belief bias in syllogistic reasoning (22 studies, N=993). https://osf.io/gafvu/download (d04)
- [V] Lampinen et al. (2024) Language models show human-like content effects on reasoning tasks. https://arxiv.org/abs/2207.07051 (b18, b19, c21)
- [M] Dube, Rotello and Heit (2010); Trippas, Handley and Verde (2013). https://doi.org/10.1037/a0020386 (b24)
- [M] Evans (2008) dual-process review; mental rules vs models. https://plato.stanford.edu/entries/logic-classical/ (b25)
