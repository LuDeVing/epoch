# Logic programming and knowledge representation: deep document

*Subfield D03.08. Evidence: evidence_a to evidence_d.jsonl (a01-a25, b01-b27, c01-c27, d01-d20), claims K01-K33, critique.md. Schema parts refer to SCHEMA.md v0.2 (guardrails G1-G12, states S0-S9, operators O1-O8). Status marks: [E] established, [S] single source, [C] contested. Evidence ids are in brackets.*

## 1. What it is

Logic programming writes knowledge as rules and facts. A machine then runs them. The rule is the program. Prolog is the classic case: Horn clauses such as `grandparent(X,Z) :- parent(X,Y), parent(Y,Z).` plus a query. Answer set programming (ASP) is the modern cousin. It adds negation, defaults and constraints, and a solver (clingo) returns all consistent answer sets. SAT and SMT solvers (Z3) and first-order provers (Prover9) fill the same role: you state what must hold, the solver finds what follows.

Knowledge representation (KR) is the wider field. It asks how to write down what is known so a machine can reason over it. Description logics (DLs) are the decidable KR fragments behind OWL ontologies. Cyc is the giant hand-written knowledge base. Knowledge graphs are the lighter, fact-only form.

Why it matters for our agent. The schema state S2 (Represent) asks for "rules in a checkable form". This subfield is the best evidence on what happens when rules are written in a form a program can run and a model cannot fudge. The 2023-2026 work asks one question many times: should a language model write the rules and let a solver do the reasoning (translate-and-solve), or should it reason in text (chain of thought)? The answer depends on the task, and the details are the value here.

Scope notes. Training-based rule reasoners (RuleTaker, ProofWriter) are covered as upper references only, since our agent is not trained [K14]. Linked subfields researched in parallel and not covered here: Inductive logic and ILP; Formal argumentation frameworks (AI); Interactive theorem proving; Neural and LLM proof search; Automated planning (STRIPS, PDDL); Readings in model-based diagnosis; Software, spreadsheet, KB debugging; Knowledge networks; Argument evaluation criteria.

## 2. History and theories in depth

**Logic plus control (Kowalski 1974-1979).** Kowalski's thesis: an algorithm is logic plus control, `A = L + C`. Logic says what is true about the problem. Control says how the search runs. The two are separable. The same Horn clauses give the same meaning whether run top-down (backward chaining, Prolog) or bottom-up (forward chaining, Datalog). Control changes efficiency only. Worked examples in the paper: factorial, subset, grandparent, and sorting. A naive sort (permutation plus ordered test) and quicksort share the logic idea but differ in control [a01]. He credits Pat Hayes with "computation is controlled deduction" and Codd with the same split in databases [a02]. The 1988 history gives dates: 1971 is sometimes called the birth of Prolog, 1972 the first system, and the article covers up to December 1974. It is a personal account, biased to Edinburgh, and Hayes disputed the credit [a03]. Limits: conceptual paper with hand-worked examples, no benchmark. Kowalski says the split is not always clean. Horn fragment only at that point, no negation.

**Semantics (van Emden and Kowalski 1976).** Gave Horn clause programs a clean model-theoretic and fixpoint meaning. Not opened; cited by Kowalski's texts [a04].

**Negation as failure (Clark 1978).** "Not P" means "P cannot be proven". This makes programs non-monotonic: add a fact and a conclusion can disappear. Not opened [a05].

**Stable models and ASP (Gelfond and Lifschitz 1988).** Defined the stable-model semantics: a program can have zero, one or many answer sets. This is the base of ASP, which is declarative, handles defaults and exceptions, and can enumerate all consistent worlds. The file was downloaded as PostScript but not read [a06].

**Expressiveness versus tractability (Brachman and Levesque 1984; Baader et al. 2003).** The classic KR tradeoff: the more a language can say, the harder it is to reason in. Neither source was opened [a24, a25]. One opened result shows the price: SHIQ with unrestricted complex role inclusions is undecidable, and a related grammar-logic problem is ExpTime-complete. The motivation was medical terminology, such as propagating a property along a part-of relation [a07]. Practical DLs (OWL EL, DL-Lite) are deliberately restricted fragments.

**Cyc and hand-built knowledge.** Lenat and Marcus (2023) describe about four decades, a 50-person project, tens of millions of hand-written axioms in CycL (higher-order logic with contexts), default rules and specialised reasoners. They argue trustworthy AI needs an LLM plus explicit knowledge. It is a position paper by Cyc's founder with no controlled comparison. The cost of hand-building is the main limit [c21].

**Language-based rule reasoning (2020-2021).** RuleTaker trained a transformer on synthetic facts and rules in English with closed-world negation. About 99% on held-out synthetic data, 95%+ on deeper chains, 98% on paraphrased rules, 90%+ zero-shot on five of six variants of hand-written rule bases [a08, b08, c18]. ProofWriter generated implications and proofs step by step, with +9 absolute proof accuracy over earlier methods [a09, c19]. These are the founding evidence that rule reasoning can be done "in language", but with trained models on synthetic data.

**The LLM turn (2022-2026).** PrOntoQA (Saparov and He) parsed chains of thought into symbolic proofs and found that models take valid steps but plan poorly [a10, b09]. Then came the translate-and-solve family: Faithful CoT (Jan 2023), SatLM, Logic-LM, LINC, GPT-3 plus ASP, Prolog-writing models, ChatLogic, VERUS-LM, and in 2026 ASP agents and round-trip checks. Section 6 covers them.

## 3. Core findings with exact numbers

All accuracy numbers are percent. "GPT-4" means early-2023 GPT-4 unless noted.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Logic and control separate; same Horn clauses, two control orders, same meaning | Conceptual; worked examples only | Kowalski 1979 [a01, a02, a03] | [S] K01 |
| Translate-and-solve beats standard prompting on all five Logic-LM sets (GPT-3.5, GPT-4) | GPT-4 std/CoT/Logic-LM: ProntoQA 77.40/98.79/83.20; ProofWriter 52.67/68.11/79.66; FOLIO 69.11/70.58/78.92; LogicalDeduction 71.33/75.25/87.63; AR-LSAT 33.33/35.06/43.04. Avg gain GPT-3.5 +39.2 over std, +18.4 over CoT; GPT-4 +24.98, +10.44 | Pan 2023 [a11, b01, c01] | [E] K04 |
| Logic-LM does not beat CoT everywhere | PrOntoQA GPT-4 CoT 98.79 vs 83.20; ChatGPT CoT 67.80 vs 61.00; text-davinci-003 83.0 vs 85.0 | Pan 2023 [c02, b02] | [E] K05 |
| Gain grows with proof depth | Logic-LM minus CoT: +7.1, +5.0, +12.7, +20.0, +39.4 at ProofWriter depth 0, 1, 2, 4, 5 (300 per subset) | Pan 2023 [a12, b03, c04] | [E] K10 |
| Syntax is easy, real text is hard (executable rate, GPT-4, no refinement) | ProntoQA 100, ProofWriter 99.0, LogicalDeduction 100, FOLIO 79.9, AR-LSAT 32.6. GPT-3.5 FOLIO 66.7, AR-LSAT 11.3. Accuracy on executable items: FOLIO 80.4, AR-LSAT 60.0 | Pan 2023 [c03, b03] | [E] K06 |
| Solver error-message refinement fixes syntax, not meaning | Exec rate +5.01 pts avg; FOLIO GPT-4 79.9 to 85.8; accuracy on executable items 80.4 to 79.9; AR-LSAT 32.6 to 39.8 | Pan 2023 [c05, a12] | [E] K07 |
| Pairwise LLM check of each edit adds a little | Logic-LM++ GPT-4 FOLIO 84.80 vs 78.92; AR-LSAT 46.32 vs 43.04; ProofWriter 79.66 vs 79.66. Claimed +18.5 over std, +12.3 over CoT, +5 over Logic-LM. Exec accuracy +6 (GPT-4), +3 (GPT-3.5) | Kirtania 2024 [a20, b13, c06] | [E] K07 |
| FOLIO GPT-4: LINC does not beat CoT | CoT 75.3 vs LINC 72.5, McNemar p=0.58. StarCoder+ 56.0 vs 41.8; GPT-3.5 62.6 vs 54.9 | Olausson 2023 [a13, b04, c10] | [C] K24 |
| LINC gives high precision, low recall | Precision on True/False 93 vs CoT 81; recall 60 vs 75; says Uncertain 57% vs 41% | Olausson 2023 [a14, b05] | [E] K09 |
| FOL syntax errors scale with model size | 38% StarCoder+, 24% GPT-3.5, 13% GPT-4 (most common: one symbol, different arities) | Olausson 2023 [b05, c11] | [E] K06 |
| LINC and CoT make different mistakes | Mistake overlap 0.14-0.22 vs 0.52-0.56 among in-context methods. No ensemble tested | Olausson 2023 [b05, c11] | [S] K23 |
| Declarative spec plus solver beats imperative code on constraint tasks | SatLM, code-davinci-002 greedy: GSM-SYS 69.4 vs program-aided 43.4 (+23); with self-consistency 80.9. GSM 84.8 SC. LSAT SoTA 30.9 to 37.4. BoardgameQA 73.9 to 80.7. On plain GSM greedy 71.8 vs 72.7 | Ye 2023 [a15, b06, c07] | [E] K11 |
| The gain is the solver, not the formal spec | SatNoSolver 26.6/23.7/40.7 (GSM-SYS/GSM/CLUTRR) vs STANDARD 21.0/22.2/41.2 (5.6 pts above standard on GSM-SYS). SatCoTSolver 54.5/63.2/48.9. LINC scratchpad (formulae, no prover) did not beat naive | Ye 2023 [c09]; Olausson [b04] | [E] K08 |
| Solver gives UNSAT and AMBIG signals; abstaining lifts selective accuracy | GSM-SYS selective accuracy 77 vs 45. Table 5 GSM-SYS correct 43.3 vs 69.4, incorrect 52.5 vs 20.6. CLUTRR UNSAT 20.1 vs 3.5, AMBIG 15.5 | Ye 2023 [b07, c08] | [E] K09 |
| Proof planning, not single steps, is the LLM weakness | 5-hop fictional ontology: 93.2% steps strictly valid, 2.4% broadly valid, 5.9% invalid. SatLM CoT-solver error split: planning 72.5% (GSM-SYS), 42.5% (GSM), 47.5% (CLUTRR) | Saparov 2023 [b09]; Ye [c09] | [E] K12 |
| Prior world knowledge props up rule reasoning | True ontology clearly above fictional and false; exact values only in a figure | Saparov 2023 [b21, a10] | [S] K13 |
| Faithful chains: solver answer follows from the chain | Better than CoT on 9 of 10 sets (code-davinci-002). MWP +6.3, planning +3.4, multi-hop +5.5, CLUTRR +21.4 relative; none on StrategyQA, Sports | Lyu 2023 [b10, c12] | [S] K21 |
| GPT-3 plus ASP on logic puzzles | 100 test puzzles: zero-shot GPT-3 2, few-shot GPT-3 3, zero-shot GPT-4 21, few-shot GPT-4 7; GPT-3 ASP 81, GPT-4 ASP 92. Prior system 71. Few-shot GPT-4 worse than zero-shot | Ishay 2023 [a16, c13] | [E] K04 |
| Reusable ASP modules plus LLM fact parser | bAbI: few-shot 80.34, CoT 86.18, GPT-3+ASP 99.99. StepGame about 10.7% label errors (107 of 108 disagreements). CLUTRR: 363 of 400 correct, 16 label errors, 21 parse errors. curie-001 parser 44.7-62.4 vs davinci-002 88-93 on StepGame | Yang 2023 [b11, c14, b23] | [S] K20 |
| Prolog helps on interdependent-variable problems | 55-problem NLR set: constraint satisfaction 8 to 100; algorithmic games 8.3 to 66.7. Text-only GPT-4 100 to 0 as interdependence goes 1 to 4; Prolog stays at ceiling. Navigate over 98 with Prolog | Borazjanizadeh 2024 [a17, b12, c15] | [E] K10, K11 |
| ChatLogic on PARARULE-Plus | GPT-3.5 base 0.344, CoT 0.3875, ChatLogic 0.5275. GPT-4 base 0.555, CoT 0.69, ChatLogic 0.73. Llama 2-7B 0.0475, 0.105, 0.1825. N=100. On CONCEPTRULES GPT-4 CoT matched or beat it | Wang 2024 [c16] | [E] K04 |
| Older benchmarks overstate ability | ProverQA CoT easy/medium/hard: GPT-4o 94.2/79.4/50.0; Claude-3.5-Sonnet 95.2/83.6/56.4; Mistral-Large 92.6/75.8/52.2; Llama3.1-8B 75.6/46.6/33.6. ProntoQA CoT 100.0 and 99.2. Std to CoT GPT-4o: 87.2/68.6/46.2 to 94.2/79.4/50.0. Avg CoT gain 12.86/8.43/3.86 | Qi 2025 [b15, d17] | [E] K25 |
| Solver route loses on shallow and implicit items, wins on search-heavy ones (GPT-4o) | ZebraLogic avg CoT 28.2 (easy 77.9, hard 8.9) vs declarative Prolog 58.8 vs Python+constraint library 71.7. GSM8K CoT 94.6, GSM-Hard 69.1, EntailmentBank CoT 81.8 (Prolog far lower) | He and Wang 2025 [d01, d20] | [E] K26 |
| FOLIO with open models, CoT beats LINC for all five | Qwen2.5-32B naive/CoT/LINC/NSCoT 66.18/75.49/68.14/71.08; Gemma-3-12B 64.22/77.45/57.35/63.24; Llama-3.1-8B 33.33/70.59/58.33/68.14; Mistral-7B 53.43/56.37/52.94/53.92; Qwen2.5-7B 59.31/70.59/58.33/66.67. N=204. Naive beat LINC on 3 of 5 | Bansal 2025 [d03] | [E] K26 |
| Small-model solver collapse is mostly format | Ministral-8B ProntoQA CoT 86.60 vs Logic-LM* 2.20, LINC* 6.20; FOLIO 60.78 vs 0.00/1.96; exec rates 0-13.67% | Beiser 2025 [d16] | [S] |
| Retries are a real cost | GSM-Hard Prolog zero-shot GPT-4o at max 1/2/10 attempts 49/63/71; Prolog one-shot 73/77/78; Python zero-shot 75/76/76. ZebraLogic one-shot 83/83/83 vs 84/84/84. 80 of 1319 still not executable after 10 | He and Wang 2025 [d02] | [S] |
| Round-trip equivalence as a gold-free faithfulness test | 150 traffic rules, Claude Opus 4.6: 44.7% equivalent with no repair; random 66.7; regenerate 64.7; diagnosis-guided 85.3. Wildlife 62.3 to 85.7. Human check 25 rules: equivalent faithful 13/14 (93%), non-equivalent 8/11 (73%) | Amrollahi 2026 [d12, d13] | [S] K30 |
| LLM judge of its own solver loop accepts wrong outputs | Incorrect PASS: Gemini 2.5 Pro 5.06% (50/989), Flash 8.76%, o4-mini 12.42%, R1 13.86%, DeepSeek-V3 37.33% (249/667) | Ishay and Lee 2026 [d09] | [S] K29 |
| Reasoning models still gain from ASP on hard constraint tasks | Mean 51.3 to 78.0 (7 task columns). Gemini 2.5 Pro 62.9 to 93.9; Flash 43.3 to 86.9; o4-mini 63.4 to 82.3; R1 52.3 to 81.9; V3 34.3 to 45.0. ZL-XXL 24.2 to 71.3; SudokuBench 8.4 to 59.8. Without revisions 54.6, with 78.0 | Ishay and Lee 2026 [d07, d08] | [S] K27 |
| ASP beats SMT on defaults; SMT beats ASP on plain puzzles | ZL-XL SMT 84.0 vs ASP 75.2; ZL-XXL 72.2 vs 56.2. MultiLogicNMR skeptical ASP 92.9 vs SMT 35.8; credulous 84.3 vs 35.0 (chance 33.3). BoardgameQA ASP 82.1 vs SMT 60.1. Reference text none 61.4, standard 70.0, compact 73.1 | Ishay and Lee 2026 [d10] | [S] K31 |
| Frontier models do explicit defeasible rules without a solver | BoardgameQA ASP 82.4 vs baseline 84.7; reasoning models 92.0 vs 88.0; V3 71.3 to 44.0 | Ishay and Lee 2026 [d11] | [S] K32 |
| Target language matters on shallow sets | Pyke 44.55, ASP 56.40, NLTK 61.44, FOL 63.92 (6 LLMs, 8 prompts, n=80 each). Meaningful predicate names 58.42 vs enumerated 45.49 (n=200). FOL vs NLTK and NLTK vs ASP not significant after correction | Beiser 2025 [d15] | [S] K15, K31 |
| Agent loop with solver saturates ASP writing | Sonnet 4.5 solved 128 of 128 problems in every run. Hard mean 7.7 calls (3.7 to 26.0). Hard "killer" item about 622k input, 23k output tokens. Earlier best 58.5% on NL-ASP-200 | Szeider 2026 [c22, d19] | [C] K19 |
| One-shot ASP is often semantically wrong | Syntax scores mostly 0.6-1.0; semantic often 0-0.4 (8 LLMs, 10 graph problems, heatmap). 17 of 21 graph problems flawed with ChatGPT-3.5 | Borroto 2026 [c23, c24] | [C] K19 |
| Cost of translate-and-solve | Mean 2.18 revisions (Gemini 2.5 Pro 0.45, V3 5.43). 12x12 Zebra: Gemini 2.5 Pro+ASP 100% at about 25k tokens vs baseline similar tokens, 0% | Ishay and Lee 2026 [d08] | [E] K28 |
| Automated prover fixes semantic mistranslation (upper bound) | PrOntoQA steamroller, 100 problems, 3 trials, GPT-3/GPT-4/Gemini-Pro: CoT one-shot 0.65/0.94/0.74; logic program 0.66/0.94/0.57; +syntax fix 0.83/0.95/0.74; +partial semantic fix 0.87/0.983/0.77; +full fix 0.98/0.995/0.96. Partial fix removes 45-72% of errors | McGinness 2024 [d14] | [S] |
| Unified solver with generic prompts | VERUS-LM / Logic-LM GPT-4: PrOntoQA 95.8/83.20; ProofWriter 93.83/78.80; FOLIO 78.43/68.55; AR-LSAT 68.36/23.40. FOLIO refinement none 57.8, syntax 74.0, syntax+semantic 78.4; exec rate 71.6, 89.2, 100; exec accuracy 80.8, 80.6, 78.4 | Callewaert 2025 [d05] | [S] |
| Task-type routing signal | BERT classifier on question text, over 1000 labelled questions, 92.6% accuracy for inference type. Routes among solver modes, not solver vs CoT | Callewaert 2025 [d06] | [S] K33 |
| CoT helps mainly on math and symbolic | FOLIO zero-shot CoT vs direct (header order confirmed): GPT-4o 79.8/62.6; Claude 3.5 Sonnet 73.9/68.5; Gemini 1.5 Pro 73.9/74.4; Gemini 1.5 Flash 74.9/69.5; Llama-3.1-70B 70.9/69.0; Llama-3.1-8B 58.6/56.7; Llama 2 7B 36.5/33.0. ContextHub L2: GPT-4o 54.5 vs 45.6 | Sprague 2025 [b14, b19, d18] | [E] K18 |
| DL and ontology reasoning is hard | OntoURL (57,303 questions, 40 ontologies, 20 open LLMs): understanding 80-94; SWRL and DL reasoning 60-75; Qwen2.5-72B DL 68.4, 3B 51.1 (chance 50); learning tasks about 0-22. DL-Lite small ontologies near 100, above a size threshold near 0. GPT-4 ALCQ 9-shot 77-89, 0-shot 30-42 (chance 33.3); DeBERTa 97.5 | Meng 2025; Wang 2024; Poulis 2024 [a21, a23, b18, c25, c27] | [E] K16 |
| Noise and missing premises hurt OWL proofs | Up to 47% drop at 1:20 irrelevant axioms, up to 38% with missing premises; simplification accuracy 80.91 to 40.14, derivation 80.30 to 32.39. In-context aid lifted one score 3.82 to 61.95 | Yang 2026 [b17, c26] | [E] K17 |
| Formal wording cost is contested | DeBERTa 95.3 (meaningless names) vs 58.5 (DL terms); GPT-3.5 0-shot 57, 9-shot 61; GPT-4 0-shot 20, 9-shot 65 on HardSymbolic. OWL proofs: formal vs natural form under 8% | Poulis 2024 [a22]; Yang 2026 [c26] | [C] K15 |
| Training-based rule reasoners | RuleTaker about 99 in-distribution; D2 model 71.1 at depth 3; D3 model 97.6 at depth 5 (same experiment); 81% flip (16654/20549) after removing a critical sentence; critical sentence flagged F1 about 92; models trained only to depth 0-1 fall below chance past depth 2 | Clark 2020 [a08, b08, b22] | [E] K14 |
| Knowledge-graph agent | Think-on-Graph, GPT-4 vs ChatGPT IO: CWQ 67.6 vs 37.6, WebQSP 82.6 vs 63.3, GrailQA 81.4 vs 29.4, Simple Questions 66.7 vs 20.0. Fine-tuned best Simple Questions 85.8 | Sun 2024 [c20] | [S] K22 |

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it as plain code around a model.

**4.1 The translate-and-solve pipeline.**
1. Formalise: the model reads the natural language problem and writes a program (FOL for Prover9, clauses for Prolog, rules for clingo, constraints for Z3).
2. Execute: code runs the solver with a time limit (clingo runs were capped at 20 s) [c22].
3. Interpret: code maps the solver result to an answer. Result types matter: SAT with one model, SAT with several (AMBIG), UNSAT (rules conflict), timeout, error.
4. Repair: on error, feed the solver message back and retry, up to a cap.
5. Fallback: if still not executable, either use CoT (Logic-LM did, for 20.1% of FOLIO) or abstain.

Mixing a CoT fallback into the number hides which method won. Report arms with and without it [K24].

**4.2 Why the solver adds value.** The solver removes two failure sources: the model's planning errors (72.5% of CoT-solver errors on GSM-SYS) and its execution errors on interdependent variables [c09, b12]. It cannot remove translation errors. Evidence that the benefit is the solver itself: the same spec without the solver is at standard-prompt level [c09, b04]. So "write the spec, then reason in text" is not enough.

**4.3 Declarative versus imperative target.** Declarative targets say what must hold. Imperative ones say step by step what to compute. SatLM shows declarative wins when variables interlock (GSM-SYS +23) and ties when the problem is a plain sequence (GSM) [b06, c07]. Prolog variables are not mutable, so most Prolog failures were variable-name assignment errors [b12]. A one-shot declarative example removed most retries for Prolog [d02].

**4.4 Solver signals for abstention.** Treat UNSAT as "the rules I wrote conflict, my translation is probably wrong". Treat AMBIG as "underdetermined, I am missing a fact". Both go to a revise or abstain branch, not a guess. SatLM's selective accuracy 77 vs 45 shows the value, at lower coverage [b07, c08]. LINC's "Uncertain" works the same way: 93% precision, 60% recall [b05].

**4.5 Repair loops, and what they can and cannot fix.** Error text repairs syntax. Meaning errors pass silently. Evidence: accuracy on executable items flat (80.4 to 79.9) while the executable rate rose 79.9 to 85.8 [c05]; VERUS-LM execution accuracy 80.8 to 80.6 to 78.4 across refinement levels [d05]. Logic-LM++ adds a pairwise check of each edit by a model, for about +5% [b13]. But the judge is the same model, and in a solver loop it accepted wrong outputs 5 to 37% of the time [d09]. A better design uses an independent check, below.

**4.6 Round-trip faithfulness check.** Formalise the text (A). Translate A back to text. Formalise that text (B). Ask an SMT solver whether A and B are equivalent. If not, a diagnosis step names the stage to repair. Diagnosis-guided repair gave 85.3% equivalent vs 44.7% before, and 64.7% by plain regeneration [d12]. Cost: 3 translations per item plus repair rounds (6 to 26 LLM calls per repaired item). The check is a heuristic: two errors can cancel, and negation inversion and conditional thresholds were common misses [d13].

**4.7 Rule-fragment choice.** Choose by what the problem contains.
- Plain constraint puzzles: SMT (Z3) or a constraint library. More training data helps the model [d10, d01].
- Defaults, exceptions, "unless", several consistent worlds: ASP. Skeptical and credulous questions need answer-set enumeration [d10, d11]. Watch for models mixing strong negation (-) and default negation (not) [d15].
- Shallow deduction over short rule lists: CoT or plain FOL. The solver adds nothing [d01, d03].
- Large instance data: keep facts outside the prompt. DL-Lite accuracy fell toward 0 above an ABox size threshold [c25].
- Datalog, plain Horn and decidable DL were not compared at all.

**4.8 Reference text.** Add a short guide to the target language. Compact guide 73.1 vs standard 70.0 vs none 61.4, averaged over four puzzle sets. The full clingo manual costs 22k tokens vs 2.6k for the compact guide [d08, d10]. The guide is paid in every call.

**4.9 Gating.** The evidence supports one rule: search-heavy, interdependent, many-constraint items go to a solver. Shallow, short-chain, implicit-rule items go to CoT [d01, b12, c04]. Signals from the text: variable interdependence count, proof depth, number of constraints. A BERT classifier names the inference type at 92.6% [d06]. No router was tested against always-solver and always-CoT.

**4.10 Knowledge side.** Facts and rules are separate problems. When the hard part is retrieving knowledge (StrategyQA), the solver adds nothing [b10]. Reusable hand-written modules plus an LLM fact parser reach 99.99 on bAbI [b11], but need one module per domain and a strong enough parser (curie-001 vs davinci-002: 44.7 vs 92.6 on StepGame k=1) [b23]. Self-correcting loops may replace hand modules when given a compact guide [d10]. Unproven.

## 5. What holds up

**Replicated across independent papers.**
- The solver beats CoT on search-heavy and interdependent problems: Logic-LM, SatLM, Prolog-NLR, GPT-3+ASP, ChatLogic, He and Wang, Ishay and Lee 2026 [K04, K10, K26, K27].
- Gain grows with depth: Logic-LM +7.1 to +39.4; Prolog stable as interdependence goes 1 to 4 while text GPT-4 falls to 0 [c04, c15].
- Syntax is solvable, meaning is not: Logic-LM exec rates, LINC syntax errors, VERUS-LM flat accuracy under refinement, Logic-LM++ [K06, K07].
- The solver, not the spec, produces the gain: SatLM SatNoSolver, LINC scratchpad [K08].
- CoT holds up on easy synthetic items: GPT-4 PrOntoQA 98.79, ChatGPT 67.80 vs 61.00, ProverQA ProntoQA 100.0, FOLIO with open models [K05, K26].

**Failures and contradictions.**
- FOLIO GPT-4: Logic-LM 78.9 vs CoT 70.6, but LINC 72.5 vs CoT 75.3 (p=0.58). Probable causes: CoT fallback on 20.1% non-executable items, 10-vote majority, different subsets. Not resolved [K24]. VERUS-LM reports Logic-LM FOLIO at 68.55 and itself at 78.43, a third setting [d05].
- Open-weight models: CoT beat LINC for all five on FOLIO (N=204); naive prompting beat LINC for 3 of 5 [d03].
- Small models fail the solver route mostly on format: Ministral-8B Logic-LM* 0.00 on ProofWriter vs CoT 51.67, with markdown bold around predicates [d16]. This says more about output discipline than reasoning.
- LLM judge false-accepts: 5.06% to 37.33% [d09]. Self-checking breaks G5 for weaker models.
- The ASP agent saturates at 128 of 128 [c22], while one-shot ASP semantic scores are often 0-0.4 [c23]. The loop, the tuned prompt (tuned over five iterations), reference validators and the model all differ. Loop value and benchmark artefact are not separated [K19].
- Formal wording: DeBERTa fell to 58.5% with DL terms, but OWL proofs showed under 8% [K15]. Prompted models lost 13 points when predicate names were enumerated [d15].

**Moderators.**
- Model size and code ability (syntax error rate 38/24/13%).
- Problem depth and interdependence.
- Executable rate on the dataset (FOLIO 79.9 vs AR-LSAT 32.6).
- Rule fragment: SMT vs ASP flips between plain and default tasks (35.8 vs 92.9).
- Prior world knowledge (true vs fictional ontologies) [b21].
- Noise: 1:20 irrelevant axioms cut accuracy up to 47% [b17].
- Reasoning-model status: these models gain from ASP mostly on hard sets (ZL-XXL 24.2 to 71.3); the BoardgameQA gain is small or negative (84.7 baseline vs 82.4 ASP) [d07, d11].

**Interventions that worked.** Declarative prompting; solver feedback for syntax; reference guide (compact 73.1 vs none 61.4); diagnosis-guided repair (85.3% equivalent vs 44.7%); abstaining on UNSAT and AMBIG; theorem-prover fix with a reference formalisation (0.98 to 0.995, an upper bound only) [d14]; meaningful predicate names (+13).

**Did not work or did not add.** Writing a spec without the solver; error-message-only repair for meaning; the CoT-then-FOL hybrid (NSCoT trailed CoT); long reference manuals; Prolog zero-shot without examples; knowledge-retrieval tasks (StrategyQA, Sports). Hand-written modules in new domains were not tested.

**Source gaps that limit confidence.** Founding papers (van Emden-Kowalski, Clark, Gelfond-Lifschitz, Brachman-Levesque, DL Handbook) were not opened [a04, a05, a06, a24, a25]. No human study. No equal-token comparison in any paper. Almost all LLM evidence is from 2023 models. FOLIO has annotation noise. Cost is rarely reported.

## 6. Language models

**Early models (2023): the solver route wins on formal tasks.** GPT-3.5 gained +39.2 over standard and +18.4 over CoT with Logic-LM, averaged over five sets. GPT-4 gained +24.98 and +10.44 [c01]. With GPT-3 plus ASP, GPT-4 reached 92% on logic puzzles vs 21% zero-shot [c13]. Prolog took text-only GPT-4 from 8% to 100% on constraint satisfaction [c15]. Code-davinci-002 with SatLM added 23 points on GSM-SYS [c07]. These are the headline numbers. Later papers show they are task-specific.

**Where CoT wins.** GPT-4 on PrOntoQA: 98.79 CoT vs 83.20 Logic-LM [c02]. GPT-4 on FOLIO per LINC: 75.3 vs 72.5 [c10]. GPT-4o on EntailmentBank: CoT 81.8, Prolog far lower, because implicit rules are lost in translation [d01, d20]. Open models of 7B to 32B on FOLIO: CoT 56.37 to 77.45, above LINC for all five [d03]. ProverQA hard: CoT only +3.86 points over standard on average [d17].

**What changed with model strength.**
- Syntax: error rate falls with model size (38, 24, 13%).
- The gain from CoT itself is model-dependent: FOLIO GPT-4o 79.8 vs 62.6 direct, Gemini 1.5 Pro 73.9 vs 74.4 [d18].
- The 2025 reasoning models still gain a lot on hard constraint tasks (mean 51.3 to 78.0; o4-mini 63.4 to 82.3; R1 52.3 to 81.9; Gemini 2.5 Pro 62.9 to 93.9). The baseline is the model alone, not a token-matched CoT, so treat this as an upper bound [d07]. Weak models can lose: DeepSeek-V3 on BoardgameQA 71.3 to 44.0 [d11].
- ASP agent loops: Claude Sonnet 4.5 solved 128 of 128 in every run [c22]. This is a saturated, prompt-tuned benchmark.

**What changed the result most.**
1. Having a solver at all on interdependent items (large).
2. Retries and repair rounds: Prolog GPT-4o 49 to 71 over 10 attempts (zero-shot); one-shot example 73 to 78 [d02]. ASP without revisions 54.6 vs 78.0 with [d08].
3. Target language: SMT vs ASP flips by task type [d10]; FOL vs Pyke 63.92 vs 44.55 on shallow sets [d15].
4. Predicate naming: 58.42 vs 45.49 [d15].
5. Reference text: 61.4 to 73.1 [d10].
6. Independent semantic check: 44.7% to 85.3% equivalent [d12].

**Cost.** Mean 2.18 revisions; 7.7 tool calls on hard ASP items; up to 26; one item about 622k input tokens; Gemini 2.5 Pro 0.45 revisions vs DeepSeek-V3 5.43 [d08, d19]. 12x12 Zebra: solver arm 100% vs baseline 0% at about the same 25k tokens. No paper gives tokens per correct answer for solver vs CoT on FOLIO-type items. This matters for G7 (equal tokens).

**Knowledge-base and ontology reasoning.** Models read ontologies well and reason poorly: OntoURL understanding 80-94, SWRL and DL reasoning 60-75, construction 0-22 [a23, b18, c27]. DL-Lite performance collapses past an ABox size [c25]. Noise (1:20 distractors) cut OWL EL extraction by up to 47% [b17]. Think-on-Graph shows a no-training agent walking a knowledge graph and beating ChatGPT's IO prompt (CWQ 67.6 vs 37.6), but it needs a well-formed graph and many calls [c20].

## 7. What our agent should take

Schema mapping: S2 Represent, S4 Test, S5 Revise, S7 Select, O6 Change representation, O3 Decompose, O5 Work backwards. G2, G3, G5, G7, G10, G12 are the guardrails this subfield touches. The claim file labelled several items "O3"; here the schema's own operator names are used.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | For constraint-heavy, interdependent or multi-hop items with a checkable answer, allow "executable rules plus solver" as a route in S2 and S4. The solver, not the written spec, must produce the answer | S2, S4, O6 | [E] | K04, K08, K10, K11; b01, b06, b12, c09, c15 |
| A2 | Do not use the solver route on shallow, short-chain or implicit-rule items. Plain CoT or direct wins there and costs less | S0 gate | [E] | K05, K26; c02, d01, d03, d17 |
| A3 | Treat a solver result as a typed signal: SAT unique, AMBIG, UNSAT, timeout, error. UNSAT and AMBIG go to revise or abstain, not a guess | S4, S5 | [E] | K09; b07, c08, b05 |
| A4 | Use solver error text only to repair syntax. "It executes" does not mean "it is right". Log accuracy and executable rate separately | S5, G3 | [E] | K07; c05, d05, a20 |
| A5 | Never let the model that wrote the rules approve its own repair. Use a code-run check (execution plus the unfitted tests of G3). The false-accept range of 5 to 37% is [S] | G5, G2 | [E] rule; [S] rate | K07, K29; b13, d09 |
| A6 | Keep large fact lists out of the prompt. Store them outside and fetch the few relevant ones. Distractor axioms cut accuracy up to 47% | S1, S2, memory | [E] | K16, K17; c25, b17 |
| A7 | Planning, not single-step validity, is the weak link. Give the agent an explicit step that lists candidate inferences and backtracks, chosen by code | O3, O5, S6 | [E] | K12; b09, c09 |
| A8 | Do not assume CoT helps on logic items. The gain depends on the model. Measure per model | S0 gate, G7 | [E] | K18; b19, d18 |

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Reasoning-model solver arm vs CoT arm at equal tokens on FOLIO, ProverQA hard, AR-LSAT | S0, S2 | [S] | K27, K25; d07, d17 |
| T2 | Round-trip back-translation plus equivalence as the semantic check, vs test cases and a second independent translator | S4, S5, G5 | [S] | K30, K29; d12, d13 |
| T3 | Disagreement trigger: run solver and CoT, accept on agreement, escalate on disagreement | S4, S7, G4 | [S] | K23; b05, d03 |
| T4 | A cheap router on depth, interdependence, constraint count | S0 | [S] | K33; d01, d06 |
| T5 | ASP for rules with exceptions; SMT or constraint library for plain puzzles | S2 | [S] | K31; d10 |
| T6 | Short target-language guide (compact 73.1 vs none 61.4) | S2 | [S] | K31; d08, d10 |
| T7 | List implicit rules before translating, to catch lost word-meaning rules | S1, S2 | [S] | K32; d20 |
| T8 | Counterfactual noun swap to separate retrieval from deduction | G10, S8 | [S] | K13; b21, d04 |
| T9 | Verified rule-module library (time, space, kinship) | memory | [S] | K20; b11, c14 |
| T10 | Meaningful predicate names (+13 on shallow sets) | S2 | [S] | K15; d15 |
| T11 | Retry cap and escalation rule for repair rounds | S5, G7, G12 | [S] | K28; d02, d08 |
| T12 | Restrict S2 rules to a decidable fragment | S2 | [S] | K03; a07 |
| T13 | Edit-the-chain faithfulness check | G10 | [S] | K21; b10 |

## 8. Concrete tests on our bench

All tests: both arms at equal token budgets, including retries, setup and fallback. Report tokens per correct answer.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | FOLIO (clean subset, note noise), ProverQA hard, AR-LSAT, ProofWriter depth 5 | CoT (reasoning model) vs solver route (ASP or Z3, with repair, no CoT fallback) vs solver with CoT fallback | Accuracy; tokens per correct; executable rate | Solver wins on AR-LSAT and depth 5. CoT wins on FOLIO and depth 0-2. ProverQA hard unknown |
| B2 | Mixed pool of shallow and deep items | Always-CoT vs always-solver vs router (depth, interdependence, constraint count) | Accuracy at equal total tokens | Router matches the better arm per class and saves tokens, if the features predict the winner |
| B3 | FOLIO and AR-LSAT with seeded semantic translation errors | Self-approval vs round-trip equivalence vs test cases vs second independent translator | False-accept rate on wrong translations; tokens; final accuracy | Round trip and second translator below the 5 to 37% self-approval rate. Test cases cheapest |
| B4 | Same items as B1 | Solver arm and CoT arm; accept on agreement, escalate on disagreement | Accuracy and tokens vs either alone | Mistake overlap 0.14-0.22 suggests a gain. Agreement accuracy above 95% |
| B5 | Constraint puzzles (ZebraLogic mid and large), default and exception items (MultiLogicNMR style) | SMT vs ASP; with and without compact guide | Accuracy; time-outs | SMT wins plain, ASP wins defaults; guide +5 to +10 |
| B6 | Open-ended items with missing facts and implicit rules (EntailmentBank style) | Plain CoT vs CoT then solver vs solver with implicit-rule listing step | Accuracy; lost-rule rate | CoT wins unless the listing step closes the gap |
| B7 | Items with 1, 10, 50 irrelevant rules | All rules vs retrieved relevant rules | Accuracy; tokens | Retrieval holds accuracy. All rules lose up to 40% |
| B8 | Rule items with true, fictional and counterfactual nouns | Same agent, solver vs CoT | Accuracy gap by noun type | Gap shrinks when the solver executes the rules |
| B9 | Spec-without-solver ablation | Formal spec then CoT vs spec executed | Accuracy | Spec-then-CoT close to plain prompting |
| B10 | Repair rounds 0, 1, 2, 3 | Cap per item | Accuracy per token | Plateau after 1 to 2 rounds on semantic items |

## 9. What does not transfer, and why

- **Training-based reasoners (RuleTaker, ProofWriter, DeBERTa on ALCQ).** Our agent is not trained. Their 97-99% figures are in-distribution on synthetic data [K14].
- **Cyc-scale hand-built knowledge.** Decades and about 50 people. Not feasible. A small module library is the only version worth testing [c21].
- **Synthetic benchmarks.** PrOntoQA, ProofWriter, CLUTRR and bAbI are template-made. High numbers tell little about real text. FOLIO and AR-LSAT show the real gap (79.9 and 32.6 executable).
- **ASP-Bench saturation.** The 128-of-128 result used a tuned prompt, reference validators and temperature 0. In real use there is no gold validator.
- **DL and OWL tasks.** Ontology construction and DL entailment are not our task types. Take only the lessons about size and noise.
- **Non-monotonic theory (negation as failure, stable models).** No human study. It transfers as a design rule only: a new fact can retract a conclusion.
- **Faithful CoT numbers.** code-davinci-002 greedy, an old retired model [K21].
- **Think-on-Graph.** Needs a Freebase or Wikidata graph. Our items have no graph.
- **Solver gains over standard prompting.** The baseline matters. The Ishay and Lee 51.3 to 78.0 baseline is the model alone, not a token-matched CoT.

## 10. Open questions

1. Reasoning-model CoT vs solver arm on FOLIO, ProverQA hard and AR-LSAT with logged tokens. No such run exists.
2. Tokens per correct answer, solver vs CoT, across the whole range. Retries and repair dominate cost but are not summed.
3. What catches semantic mistranslation: round trip, test cases, or a second translator? Only round trip has numbers (85.3% vs 44.7%). It has not been compared with Logic-LM++'s +5%.
4. Does disagreement between solver and CoT arms flag errors? Overlap 0.14-0.22 says so. Nobody tested it.
5. Can depth, interdependence or constraint count be read from text well enough to gate?
6. Open-ended text with missing facts and implicit rules. Implicit rules get lost. No test on truly open text.
7. Which fragment: Datalog, Horn, ASP, decidable DL? No head-to-head for LLM translation and time-outs.
8. Do verified rule modules transfer across domains, and what do they cost to build?
9. Is the formal-wording penalty real for prompted frontier models? Contested.
10. Does CoT still help on FOLIO-type items for reasoning models?
11. Is the ProverQA hard split really near chance? The label mix is not stated. 50.0 to 56.4 is above 33.3 if balanced.
12. Does the ASP-loop success survive without the benchmark's tuned prompt and validators?

## 11. Sources

[V] = opened and read (full text, this run or the earlier run of this batch). [M] = snippet or memory only.

- [V] Kowalski (1979) Algorithm = Logic + Control. https://www.doc.ic.ac.uk/~rak/papers/algorithm%20=%20logic%20+%20control.pdf [a01, a02]
- [V] Kowalski (1988) The early years of logic programming. https://www.doc.ic.ac.uk/~rak/papers/the%20early%20years.pdf [a03]
- [M] Van Emden and Kowalski (1976) Semantics of predicate logic as a programming language. https://doi.org/10.1145/321978.321991 [a04]
- [M] Clark (1978) Negation as failure. https://doi.org/10.1007/978-1-4684-3384-5_11 [a05]
- [M] Gelfond and Lifschitz (1988) The stable model semantics. https://www.cs.utexas.edu/users/vl/papers/stable.ps [a06]
- [V] Horrocks and Sattler (2003) Decidability of SHIQ with complex role inclusion axioms. https://www.cs.ox.ac.uk/ian.horrocks/Publications/download/2003/HoSa03a.pdf [a07]
- [M] Brachman and Levesque (1984) Tradeoff between expressiveness and tractability. https://www.cs.toronto.edu/~hector/ [a24]
- [M] Baader et al. (2003) The Description Logic Handbook. https://doi.org/10.1017/CBO9780511711787 [a25]
- [V] Clark, Tafjord, Richardson (2020) RuleTaker. https://arxiv.org/abs/2002.05867 [a08, b08, b22, c18]
- [V] Tafjord, Dalvi, Clark (2021) ProofWriter. https://arxiv.org/abs/2012.13048 [a09, c19]
- [V] Saparov and He (2023) Language models are greedy reasoners. https://arxiv.org/abs/2210.01240 [a10, b09, b21, c17]
- [V] Pan et al. (2023) Logic-LM. https://arxiv.org/abs/2305.12295 [a11, a12, b01-b03, b20, b27, c01-c05]
- [V] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 [a13, a14, b04, b05, c10, c11]
- [V] Ye et al. (2023) SatLM. https://arxiv.org/abs/2305.09656 [a15, b06, b07, b26, c07-c09]
- [V] Ishay, Yang, Lee (2023) Leveraging LLMs to generate answer set programs. https://arxiv.org/abs/2307.07699 [a16, c13]
- [V] Yang, Ishay, Lee (2023) Coupling LLMs with logic programming. https://arxiv.org/abs/2307.07696 [b11, b23, c14]
- [V] Borazjanizadeh and Piantadosi (2024) Reliable reasoning beyond natural language. https://arxiv.org/abs/2407.11373 [a17, b12, b24, c15]
- [V] Lyu et al. (2023) Faithful chain-of-thought reasoning. https://arxiv.org/abs/2301.13379 [a18, b10, c12]
- [V] Fang et al. (2024) LLMs are neurosymbolic reasoners. https://arxiv.org/abs/2401.09334 [a19]
- [V] Kirtania et al. (2024) Logic-LM++. https://arxiv.org/abs/2407.02514 [a20, b13, c06]
- [V] Poulis, Tsalapati, Koubarakis (2024) Transformers in the service of DL-based reasoning. https://arxiv.org/abs/2311.08941 [a21, a22]
- [V] Meng et al. (2025) OntoURL. https://arxiv.org/abs/2505.11031 [a23, b18, c27]
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [b14, b19, d18]
- [V] Qi et al. (2025) ProverQA. https://arxiv.org/abs/2502.06563 [b15, d17]
- [V] Wang et al. (2024) Can LLMs understand DL-Lite ontologies? https://arxiv.org/abs/2406.17532 [b16, b25, c25]
- [V] Yang, Chen, Sattler (2026) LLM for OWL proofs. https://arxiv.org/abs/2601.12444 [b17, c26]
- [V] Wang et al. (2024) ChatLogic. https://arxiv.org/abs/2407.10162 [c16]
- [V] Sun et al. (2024) Think-on-Graph. https://arxiv.org/abs/2307.07697 [c20]
- [V] Lenat and Marcus (2023) Getting from generative AI to trustworthy AI. https://arxiv.org/abs/2308.04445 [c21]
- [V] Szeider (2026) ASP-Bench. https://arxiv.org/abs/2602.01171 [c22, d19]
- [V] Borroto Santana et al. (2026) BLAST. https://arxiv.org/abs/2604.22306 [c23]. Borroto, Kareem, Ricca (2024) read second-hand through ASP-Bench [c24]
- [V] He and Wang (2025) When do symbolic solvers enhance reasoning in LLMs? https://arxiv.org/abs/2512.03272 [d01, d02, d20]
- [V] Bansal, Kurniawan, Frermann (2025) Robustness of neurosymbolic reasoners on FOL. https://arxiv.org/abs/2509.17377 [d03, d04]
- [V] Callewaert, Vandevelde, Vennekens (2025) VERUS-LM. https://arxiv.org/abs/2501.14540 [d05, d06]
- [V] Ishay and Lee (2026) LLMs as ASP programmers. https://arxiv.org/abs/2604.27960 [d07-d11]
- [V] Amrollahi, Lopez, Barrett (2026) Faithful autoformalization via roundtrip verification. https://arxiv.org/abs/2604.25031 [d12, d13]
- [V] McGinness and Baumgartner (2024) Automated theorem provers help improve LLM reasoning. https://arxiv.org/abs/2408.03492 [d14]
- [V] Beiser, Penz, Musliu (2025) Intermediate languages matter. https://arxiv.org/abs/2502.17216 [d15, d16]

Not opened: a04, a05, a06, a24, a25 [M]. Figure-only values: PrOntoQA ontology effect (b21), DL-Lite F1 cells (b16, b25), BLAST heatmap (c23), ProofWriter table cells (a09, c19). Table text for He and Wang, VERUS-LM and Bansal was garbled by PDF extraction, so only rows readable by position are quoted.
