# Polya heuristics: deep document

*Subfield E06.01. Built from evidence_a-d.jsonl (ids a01-a30, b01-b28, c01-c25, d01-d16), claims.jsonl (E06.01-K01 to K30) and critique.md in this folder. Numbers marked "re-verified" were re-opened in the paper text during the critique pass. Links to parallel subfields are notes only: means-ends analysis, problem-solving strategies and cycle, Schoenfeld episodes, verification design, adaptive stopping, Soar impasses, probing, LLM debugging.*

---

## 1. What it is

George Polya's *How to Solve It* (1945) is a list of questions a solver can ask. The core ones:

- **Understand the problem.** What is unknown? What is given? Draw a figure.
- **Devise a plan.** Have you seen it before? Is there a related or auxiliary problem? Can you specialise, generalise, work backwards, decompose, drop a condition?
- **Carry out the plan.** Check each step.
- **Look back.** Check the result. Can you derive it differently? Can you use the result or method elsewhere?

Polya called these heuristics: rules of thumb that often help but never guarantee. They are the oldest list of "thinking operators" for problem solving. Our schema operators O1 to O8 (specialise, generalise, decompose, drop a constraint, work backwards, change representation, map an analogue, reframe) and the states S1 (understand), S9 (look back) come from this tradition.

The subfield asks four things:

1. Do the heuristics work, and for whom? (human teaching studies)
2. Why did they often fail in the classroom? (the Schoenfeld critique: descriptive not prescriptive, and no control)
3. What happens when we give a language model a heuristic menu or a Polya-style plan?
4. Which parts should our agent take, and which must be tested first?

The short answer from the evidence: a bare list of heuristic names is weak. Fine-grained procedures with triggers, plus a control mechanism that checks progress, are what worked in humans. In models, gains from Polya-style prompts are real but small, shrink with model strength, and are largely untested at equal tokens on current reasoning models.

---

## 2. History and theories in depth

### 2.1 Polya (1945) and the AI reception

Polya's list was written as advice to teachers. It names moves but gives no rule for choosing between them. In AI, Newell is quoted as saying "Polya revered and Polya ignored" (a04, b22). Hunt (1975) and Minsky (1961) found his work ad hoc: examples, no general rules. AI built means-ends analysis and search instead (link: Means-ends analysis subfield). Newell's original paper was not reachable, so this is second-hand.

### 2.2 The 1960s-70s classroom studies: little support

Schoenfeld's 1992 review (a03, b01, b02) summarises the pre-1980 teaching studies:

- Wilson (1967), Smith (1973): taught heuristics did not transfer to new domains.
- Kantowski, Kilpatrick, Lucas: heuristic use correlated only weakly with test performance.
- Harvey and Romberg (1980): "promising" but unproven.
- Begle (1979): strategies are "both problem- and student-specific", so teaching one or few strategies to everyone is "far too simplistic".

No pooled numbers are given. The studies were mostly unpublished dissertations. Lucas (1974) found a slight edge for explicit over implicit teaching (30 students; 8 or 13 weeks depending on the source, unresolved) (a13).

### 2.3 The Schoenfeld critique (1985, 1992)

Schoenfeld's four-part framework: resources, heuristics, control, beliefs. His critique of Polya has three parts.

**(a) Descriptive, not prescriptive (a01, a02, b03).** A Polya label lets you recognise a strategy in use. It does not tell an unfamiliar person how to carry it out. His worked example: "examine special cases" hides three different procedures.

| Problem | Right special-case procedure |
|---|---|
| Closed form of a sum with integer n | Try n = 1, 2, 3, find a pattern, prove by induction |
| Roots of a polynomial and its reversed-coefficient twin | Try easy-to-factor polynomials. Trying n = 1, 2, 3 is a wild goose chase |
| Recursive sequence a_n = mean of previous two | Choose starting values 0 and 1, draw the picture |

He says one could list a dozen more for specialising alone, and the same holds for nearly every Polya strategy. Fix: specify strategies at a finer grain, each with a precondition. Evidence "turned in Polya's favor" in the 1980s once this was done (Silver 1979/1981, Heller and Hungate 1985) (a08, b21). These grain-level studies were read only through his summary.

**(b) Control (a05, a06, b05).** In more than 100 videotaped attempts by college and high-school students on unfamiliar problems, about 60% were "read, decide quickly, pursue that direction come hell or high water". After his problem-solving course, under 20% were of that type, with a reported rise in success. The intervention was three questions asked by the instructor at any time: What exactly are you doing? Why are you doing it? How does it help you? Students first could not answer, then pre-empted the questions. It took "the better part of a semester". A mathematician solving a hard problem spent more than half his time making sense of the problem and commented on progress several times. **Limit:** one chapter, no N, no test, no control group. It is a single source (claims K03).

**(c) Drilling turns heuristics into algorithms (a08, b04).** When textbooks show a strategy, practise it, and test it, it "is no longer a heuristic in Polya's sense; it is a mere algorithm". Teaching is hard because the teacher must judge whether a student approach is fruitful.

### 2.4 Schemas versus strategies (a30)

Competing account: expert success rests on stored problem schemas (recognise features, run a procedure), not general heuristics. Schoenfeld agrees experts use schemas on familiar problems and strategies beyond the routine, but warns that crude schemas ("these features, use this procedure") are error-prone. The machine analogue is Buffer of Thoughts (c19): a library of thought templates retrieved by similarity (+11% Game of 24, +20% Geometric Shapes, +51% Checkmate-in-One at about 12% of the cost of multi-query methods; baselines chosen by the authors).

### 2.5 Heuristic vocabulary and the 1980s-2010s human work

- Koichu, Berman and Moore (2007): five-month field study, two grade-8 classes in Israel. Heuristic use correlated with learning gain. No control group (a13, a27; not opened).
- Collet (2009, grades 7-8): more heuristics used after training; medium correlation with success.
- Brockmann-Behnsen (2012, 2014): first results in four grade-8 classes favour explicit over implicit training (a13).
- Lester, Garofalo and Kroll (1989): teacher as external monitor, 16.1 hours over 12 weeks, 35.7% of class time, two grade-7 classes. Control and concept understanding grow together. Gains need many varied problems over a long time. Hard to sustain when basics are weak (a07, b06). No effect sizes in the summary.
- Hembree (1992): meta-analysis of 487 reports. Abstract only: no method clearly better in K-5, heuristics mildly better in grades 6-8, distinctly better in high school. Training in drawing diagrams or sketches gave the largest gain. Teachers trained in heuristics raised performance (a28, d15). Second-hand (Bruun 2013, b07, b26): explicit training was essential, practice without direction did not help, strict step-by-step procedures did worse than flexible approaches, rereading or restating the problem and pure trial and error gave no benefit. Effect sizes were never obtained.
- Trinchero and Sala (2016): 931 pupils, grades 3-5, 53 classes, 20 schools. Chess lessons by chess instructors who taught heuristics: maths gain d 0.50. Same lessons by school teachers without heuristics: d 0.20. Control: d 0.13. Not randomised at pupil level, and instructor and heuristics are confounded (b08, b25).

### 2.6 The two controlled tests of explicit heuristic training

- **Schoenfeld (1979):** 7 students (4 experimental, 3 control). Both groups saw the same worked solutions. The experimental group also got a list of five heuristics (draw a diagram; induction if there is an integer parameter; contradiction; a similar problem with fewer variables; subgoals) and solutions overlaid with notes saying which heuristic was used and how. Control did not improve. The experimental group solved about 2 more problems than at pretest. No statistics, no test-only group (a09, a10).
- **Rott and Gawlick (2014):** improved replication (d01, a11, a12). 28 German maths teacher students: explicit n = 9, practice-only n = 10, test-only n = 9. Heuristics: draw a figure, special cases, work backwards, drop a condition, fewer variables. ANCOVA F = 6.593, p = 0.005. Bonferroni explicit vs practice p = 0.043. Corrected d: explicit vs practice 0.79, explicit vs test-only 1.44, practice vs test-only 0.64. Explicit pre-post d = 0.88. The test-only group fell from 16 to 12 points, so the posttest was harder than the pretest. The authors call their own sample "very small" and ask for a larger study. No larger replication was found (the search was cut short).

### 2.7 Summary of the theory

The surviving theory: heuristics help when (1) they are specified finely, tied to problem features, (2) the solver is competent enough to execute them, (3) they are named explicitly during or after solving, and (4) something monitors progress and forces a switch. Weak support remains for general transfer.

---

## 3. Core findings with exact numbers

Status key: **E** established (two independent sources), **S** single source, **C** contested. "Human" = human studies; "LLM" = model studies. Claim ids in brackets.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pre-1980 teaching studies found little support, no transfer | No pooled numbers; weak correlations | Schoenfeld 1992 review (a03, b01) | E [K02] |
| Heuristics help older students more; diagrams strongest | 487 reports; K-5 none, 6-8 mild, high school distinct; effect sizes not obtained | Hembree 1992 abstract (a28, d15) | E [K02], numbers missing |
| Explicit heuristic training beats practice-only and no training | n = 9/10/9; F = 6.593, p = .005; d 0.79 and 1.44 | Rott and Gawlick 2014 (d01, a11) | E [K04], tiny samples |
| Original explicit-training test | N = 7 (4 vs 3); experimental +2 problems, control no gain | Schoenfeld 1979 via Rott and Gawlick (a09) | S, second-hand |
| Taught heuristics plus control questions cut uncontrolled attempts | About 60% to under 20%; over 100 tapes; no N, no test | Schoenfeld 1992 (a05, b05) | S [K03] |
| Chess transfer to maths only when heuristics taught | 931 pupils; d 0.50 vs 0.20 vs 0.13 | Trinchero and Sala 2016 (b08) | S [K05], confounded |
| Rigid step-by-step procedures did worse than flexible approaches; restating gave no benefit | Effect sizes not seen | Hembree via Bruun (b07, b26) | S, second-hand |
| One heuristic label hides several procedures | 3 problems, 3 procedures | Schoenfeld 1992 (a02) | S, argument [K01] |
| Teachers pick strategies by ease, not evidence | 70 teachers, 42 schools; none taught all NCTM strategies | Bruun 2013 (b24) | S |

### 3.2 Language-model studies: plan, abstract, decompose, analogy, menu

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Plan-first prompt vs zero-shot CoT (text-davinci-003), six math sets average | CoT 70.4, PS 72.9, PS+ 76.7, 8-shot manual CoT 77.6 (re-verified) | Plan-and-Solve (a15, c03) | S [K08] |
| Same, GSM8K | 56.4 / 58.2 / 59.3 (manual CoT 58.4) | a15, c03 | S |
| Same, other sets | MultiArith 83.8 / 87.2 / 91.8; AQuA 38.9 / 42.5 / 46.0; Last Letter 64.8 / 75.2 (PS+) | a15, critique | S |
| Planning cuts calculation and missing-step errors, not misunderstanding | 100 GSM8K items: semantic 27% CoT, 26% PS, 27% PS+; wrong answers 46 / 43 / 39 | a16, b10 | S [K09] |
| Step-back (generalise), MMLU physics / chemistry | PaLM-2L CoT 65.0 / 75.3 to 73.2 / 81.8; GPT-4 CoT 82.9 / 85.3 to 84.5 / 85.6; Llama2-70B CoT 59.3 / 64.1 to 64.8 / 66.7 (re-verified) | Zheng 2024 (a17, b12) | S [K10] |
| Step-back on GSM8K | CoT 84.4 vs Step-Back 84.3 | c04 | S |
| Step-back fixes and breaks answers | Fixes 20.5%, introduces 11.9% (physics); TimeQA+RAG fixes 39.9%, breaks 5.6%; StrategyQA 15.4% fixed vs 6.1% broken | a18, c22 | S [K11] |
| Over 90% of residual step-back errors are in the reasoning step | MMLU physics, PaLM-2L | a18, b27 | S |
| Least-to-most (decompose), SCAN length split | Standard 16.7, CoT 16.2, L2M 99.7 (code-davinci-002; re-verified) | Zhou 2023 (a19) | S [K12] |
| Least-to-most, GSM8K overall and by step count | 60.87 vs 62.39; 2 steps 76.68 vs 74.53 (worse); 3: 67.29 vs 68.91; 4: 59.39 vs 59.73; 5+: 39.07 vs 45.23 | a20, b11 | S |
| Hand-made decompositions fix nearly all GSM8K failures | Qualitative; choosing the decomposition is the bottleneck | b23 | S |
| Self-Discover (39-module menu, once per task) | PaLM 2-L BBH 60 to 67, T4D 40 to 69, MATH 42 to 50.5; GPT-4 BBH 75 to 81, T4D 52 to 85, MATH 71 to 73. Beats direct on 23/25, CoT on 21/25 (re-verified) | Zhou 2024 (a21, b14, c07) | S [K13] |
| Most MATH failures are computation | 74.7% of 99 wrong MATH answers computation errors; 87.5% of structures correct | a21, c23 | S |
| Analogical prompting (self-generated related problems) | GPT-3.5 GSM8K 75.8 (0-shot CoT) / 76.7 (5-shot) / 77.8; MATH 33.9 / 34.9 / 37.3; PaLM2 MATH 29.8 / 34.3 / 34.8; davinci MATH 50.3 / 54.0 / 61.0 | Yasunaga 2024 (c05, c24) | S [K14] |
| Problem elaboration (restate first) | GPT-3.5 GSM8K +9.93 greedy; open small models: Llama2-7B +0.33, Llama2-13B +0.68, Mistral-7B -1.04 | Zhu 2024 (b18) | S |
| Correct hints help, wrong hints hurt | 11 models, 17 prompts, MATH; wrong or random hints below CoT; numbers not captured | Agrawal 2024 (c09) | S [K16] |
| Plan in prose beats plan in JSON | MATH 200: LLaMA-3.1-405B 75.5 vs 63.5; Mistral-Large 76.5 vs 67.5 | Gunasekara 2025 (d13) | S [K30] |
| Per-problem plan beats task plan on mixed set, loses on uniform set | T4D task-level 100.0 vs instance-level 73.2 to 78.9 | d13 | S |

### 3.3 Language-model studies: diversity, routing, backward, control

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Spreading attempts over named approaches beats equal sampling of one prompt | GPT-4.1-mini AIME24 Acc@32 SC 60.0 to 73.3; GPT-4o-mini AIME25 3.3 to 23.3 (30 problems, 1 problem = 3.3 points) | TTS-Uniform (d03) | E [K28] |
| Same, DIV-SE | GPT-4 Graph Colouring CoT 15, SC-10 23, DIV-SE 97; MATH counting and probability CoT 62.24 to 79.11; GPT-3.5 AQuA +14 to +16.5; GPT-3.5 Blocksworld and LLaMA-2 zero-shot: no gain | Naik 2024 (d04) | E [K28] |
| No single strategy wins across slices; routing helps modestly | PRISM gain over best single +0.9 / +2.9 / +7.6 (Qwen / DeepSeek / Llama-3-8B); MATH 53.2, +3.1; router lost on AQuA; one strategy ranged 13.5 to 95.3 across datasets | Qi 2025 (d12, c12) | S [K23], C [K17] |
| Wrong class label loses most of the routing gain | Predicted-category routing 29% below true-category routing | c13 | S |
| Frontier models find fewer strategies than people | 80 AMC/AIME problems; 217 reference strategies; Gemini 184, DeepSeek 152, GPT 151, Claude Opus 4.6 110 | Yang 2026 (c11) | S [K22] |
| Working backwards is much harder than forward | GSM8K GPT-4 92.8 vs 38.6; PaLM-2 58.4 vs 10.8; LLaMA-2-70B 60.5 vs 15.2 (re-verified); MultiArith LLaMA-2-70B 95.7 vs 6.3 | c08 | S [K15] |
| Rewriting to forward form recovers 10 to 20 points | As above | c08 | S |
| Backward check adds 1 to 2 points over self-consistency, with extra chains | davinci 81.4 to 83.5; ComplexCoT 83.2 to 85.0; GPT-3.5-Turbo 85.5 to 86.6 | FOBAR (d11) | S [K29] |
| Self-check with no outside signal lowers accuracy (2023 models) | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 75.9 to 74.7; oracle label inflates to 84.3 / 97.5 | Huang 2024 (d07) | E [K25] |
| Locating the first error is the bottleneck | Best 52.87% (GPT-4); fewer false alarms with fewer calls | Tyen 2024 (d09) | E [K25] |
| A mis-aimed fix costs correct traces | True location: wrong-to-right +18.04 to +43.92, right-to-wrong 0 to -11.43; random location: +5.16 to +21.57, -6.67 to -15.91 | d16 | E [K25] |
| Reasoning models detect errors in others' work much better | ProcessBench avg F1: GPT-4o 61.9, QwQ-32B-Preview 71.5, o1-mini 87.9; GPT-4o OlympiadBench 51.4 | Zheng 2024 (d08) | S [K26] |
| Generic CoT on reasoning models is marginal or mixed | GPQA Diamond, 198 q x 25 trials: o3-mini +0.029, o4-mini +0.031, Flash 2.5 -0.033; 20-80% more time | Meincke 2025 (d02) | C [K27] |
| Opposite on distilled R1 (direct baseline suppresses thinking) | CoT helped in 72% of cases; R1-32B reflections 414.2 to 2.56 while accuracy 10% to 43.3% | Ge 2025 (d14) | C [K27] |
| Combining methods with different solved sets | IMO-AG-30: AlphaGeometry 25, Wu+DD+AR 21, Wu+AG 27, HAGeo 28 | c14, c15, c25 | E [K21] |

### 3.4 Training and diagnosis studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Naming a heuristic before each step in RL rollouts | 14 of 15 comparisons improved; mean +1.1 to +7.0 Avg@16; DeepSeek-Distill-Llama-8B 42.8 to 49.8 | SHAPE (a26) | S [K18], training only |
| Polya-like behaviours in the base model predict RL gain | Qwen-3B about 60% vs Llama-3B about 30% on Countdown; filler tokens give no gain (30 to 35%); wrong-solution priming worked as well | Gandhi 2025 (b15, b16) | S [K19] |
| Hard perturbations cut accuracy; heuristic mix shifts | Qwen3-32B 92.0 / 90.0 / 76.0 (original / simple / hard) | SHAPE (a24) | S |
| RL concentrates on strategies already in the base model | Density 1.2 to 1.5 vs 0.5 to 0.6 cross-model | a25 | S |
| Polya-stage tuning balances stage use, no accuracy measure | Instruct plan share 7.8% vs 18.9% tuned; 6 raters | Llama-Polya (a22, c02) | S [K20] |
| Polya-step benchmark: failures not uniform | Understanding above 90% for most; Reasoning 9.05 to 93.61%; o3 final 91.44% but all-pass 64.87% | SMART (a29) | S |
| Retrieved Polya text changes answer form, not content quality | 2880 solutions; persona about sevenfold odds of process quality, RAG not significant | b19 | S [K24] |
| Per-type effects of single-heuristic system prompts | Prealgebra most help; number theory almost none; auxiliary elements in geometry -25% (GPT) vs +14% (Claude); GPT-5.4-nano mostly hurt; n not stated | Anand blog (c01) | C [K17] |

---

## 4. Mechanisms and models

This section gives implementable designs. Each is a mechanism the evidence supports, with the evidence level beside it.

### 4.1 Operator as a typed record (fixes "descriptive not prescriptive")

Evidence: a01, a02, b03, b21. Status S.

Each operator is a record, not a label:

```
operator: {
  id, name,
  precondition: <features code can compute or the model can answer yes/no>,
  procedure: <numbered steps, plain prose, 3-6 lines>,
  worked_example: <one annotated solution, see 4.5>,
  success_check: <what code runs to say it helped>,
  failure_signature: <what output means this operator is the wrong choice>
}
```

Split coarse Polya operators into sub-variants keyed by problem class. Schoenfeld's specialise example gives three: (i) integer parameter, small values then pattern then induction; (ii) roots or polynomial, easy-to-factor instances; (iii) recursion, starting values 0 and 1 plus a picture. Do not apply sub-variant (i) to (ii): it wastes the budget.

The class key is the weak link. Class labels from a model lose about 29% of the routing benefit relative to true labels (c13). So the precondition should use cheap code-readable features first (does the text contain an integer parameter n, a recurrence, a polynomial, a figure, a numeric target?) and a model yes/no only as a fallback.

### 4.2 Control loop (the Schoenfeld monitor)

Evidence: a05, a06, a07, d07, d09, d16. Human control result S; model self-check hazards E.

Human version: an external monitor asks three questions at any time: what exactly are you doing, why, how does it help. Machine version for the schema, with the hazards from the LLM evidence built in:

1. Trigger from code, not from a clock: no new verified sub-result for K steps, same error twice, or budget fraction spent (this is S6).
2. Ask the three questions in a form that ends in a test: "State what you are computing. State what result you expect. Name a check that would show it is wrong." Code then runs the check (recompute, substitute, special case, bound).
3. If the check fails or cannot be run, abandon the direction and pick a different operator (one not yet used).
4. Never act on the model's opinion alone that the path is bad. Generic "are you sure" self-review lowered GSM8K accuracy for GPT-4 from 95.5 to 89.0 over two rounds (d07). A random error location broke 7 to 16 points of correct traces (d16).

Why not just copy the human result: the human result has no N and no control group. And reasoning models may already monitor themselves (K26 shows they judge others' errors well; live self-monitoring is untested).

### 4.3 Operator selection and diversity

Evidence: d03, d04, d12, c13, c11. Diversity E; routing S/C.

Three ways to use a menu:

- **Task-level menu (Self-Discover).** Once per task class, the model selects, adapts and writes a plan from 39 modules (3 extra calls). Fits S0 in our schema. Write the plan in prose, not JSON (d13: +9 to +12 points on MATH).
- **Diversity split (TTS-Uniform, DIV-SE).** Ask for k distinct approaches. Run one attempt per approach (or equal samples per approach). Vote or verify. At equal sample counts this beat plain self-consistency (E, two sources). Entropy per approach is a cheap signal for dropping unstable approaches (d03). The gain disappears if the model cannot follow the approach (GPT-3.5 on planning, LLaMA-2 zero-shot: d04).
- **Router (PRISM).** A trained classifier picks a strategy per problem. Gain over best single strategy +0.9 to +7.6, shrinking with model strength (d12). A hand-written precondition rule is untested.

Our schema (G1, G4) uses operators only at S6 or in open mode, and rules out strategy-persona voters on single-answer problems. The diversity evidence (d03, d04) is a tension with G4: those studies used different approach prompts, not personas, and voted by majority. Either read can be right. This must be tested (see U1 and U2 in UNKNOWNS.md).

### 4.4 Reformulations that work better than the Polya literal

- **Work backwards as reformulation (c08, d10, d11).** Models do backward reasoning badly (GSM8K GPT-4 38.6 vs 92.8 forward). Write instead: "Write the forward question whose answer is the given target quantity." Or use it as a check: substitute the candidate answer into the problem and test it. FOBAR (mask a number, supply the candidate answer, ask for the masked number) added 1 to 2 points over self-consistency, but with extra chains.
- **Generalise as principle retrieval (a17).** "What principle governs this?" helps on knowledge-heavy physics and chemistry for weaker models. Not on GSM8K. Over 90% of the remaining errors are in the reasoning step after the principle is named (a18).
- **Decompose gated by length (a20).** Hurts at 2 steps (74.53 vs 76.68), helps at 5 or more (45.23 vs 39.07). Gate by estimated step count or on a failed first attempt.
- **Auxiliary construction by enumerate-and-test (c14, c15).** Random auxiliary points already reach silver level in geometry with a symbolic checker; hand-written placement heuristics reached 28/30. The pattern: cheap proposal plus strong code check.

### 4.5 Worked examples annotated with the heuristic

Evidence: a09, a11, d01. Status E for humans.

The one intervention that has a controlled replication: show worked solutions with an overlay naming which heuristic was used and how. Explicit overlay beat identical unannotated worked solutions (d 0.79). In our schema this is S9: the look-back line records the operator and a short note on how it was applied, and a later prompt shows these annotated solutions as examples (after the first attempt, per section 5 of SCHEMA.md). Whether this transfers to models is untested (K04 test).

### 4.6 Understanding as its own check

Evidence: a16, b10, a29, b18. Status S.

Planning prompts cut calculation and missing-step errors but left semantic misunderstanding at 26 to 27% of 100 GSM8K items (a16). SMART finds Understanding mostly solved by recent models (above 90%) while Reasoning and Reflection vary (a29). Restating helped GPT-3.5 (+9.93 on GSM8K, b18) and was null or negative on small open models. So S1 restate-and-check has model-dependent value. Check it by code where possible: extract the numbers from the text and confirm each appears in the restatement.

### 4.7 Log schema for Polya moves

SHAPE's taxonomy (a23): 11 families (change of representation, cognitive reinterpretation, symbolic formalisation and auxiliary elements, classification/rephrase, wishful thinking/simplify, case analysis/decompose, contradiction, analogy/related theorems, experimental and pattern exploration, working backward, verification/looking back), labelled on content units. Best automated annotator: Grok-4.1-Fast F1 77.16, Gwet AC1 0.909; open Qwen3.5-27B F1 70.44. About $100 for 445 trajectories. Noisy but usable for counting which moves our agent emits. Link: Schoenfeld episodes subfield.

---

## 5. What holds up

### 5.1 Replications and independent agreement

| Result | Replicated by | Verdict |
|---|---|---|
| Explicit heuristic training with annotated worked solutions beats unannotated practice | Schoenfeld 1979 (N = 7); Rott and Gawlick 2014 (n about 10 per cell, d 0.79) | Direction replicated, size uncertain. Samples tiny. Both with strong-maths adults. |
| Explicit labelling gives a modest edge over implicit | Lucas 1974; Brockmann-Behnsen 2012/14 (first results) | Consistent, thin |
| Heuristic use correlates with success (medium) | Koichu 2007; Collet 2009 | Correlational only |
| Diagrams or representations: biggest human lever | Hembree 1992 abstract; teachers' practice (Bruun) | One meta-analysis, no numbers |
| Diverse approach prompts beat repeated single-prompt sampling (non-reasoning models) | TTS-Uniform (d03); DIV-SE (d04) | Two independent sources. Majority vote only. |
| Complementary methods union beats either alone | AlphaGeometry vs Wu (c14, c25); HAGeo (c15) | Geometry only |
| Self-check with no new info does not help | Huang 2024 (d07); Tyen 2024 (d09, d16) | Two sources, 2023-24 models |

### 5.2 Failures, nulls and contradictions

- **Early classroom studies:** no transfer, weak correlations (a03). Never overturned by numbers; reversed in direction only by fine-grained work that is second-hand.
- **No larger replication** of Schoenfeld 1979 exists in what we found. The search was cut short, so absence is weak.
- **Schoenfeld's 60% to under 20% control result** has no N or test. Counted once (a05 and b05 are the same source).
- **Step-back on a strong model:** GPT-4 CoT 82.9 / 85.3 vs Step-Back 84.5 / 85.6, inside run noise of about 1.2 (a17, b12). GSM8K: none.
- **Plan-and-Solve:** plain PS adds only +1.8 on GSM8K. PS+ does not beat 8-shot manual CoT on average (76.7 vs 77.6) and loses on MultiArith (91.8 vs 93.6) and SVAMP (75.7 vs 80.3) (b28). The critique pass corrected one earlier row mix-up (b09 "PS 73.5" is the zero-shot PoT row).
- **Least-to-most on short GSM8K problems:** worse at 2 steps. Authors say the decomposition prompts do not transfer across domains (a19).
- **Analogical prompting on strong models:** 1 to 3 points (c05); the 10.7 on davinci needed a demonstration.
- **Self-Discover on MATH:** +1 to +3 over baselines, within noise for 200 problems (b14).
- **Problem elaboration:** negative on Mistral-7B (-1.04) (b18).
- **Heuristic menus can hurt small models:** the blog (c01) found GPT-5.4-nano mostly hurt. Informal, no n.
- **Retrieved Polya text:** no significant gain in content quality (b19).
- **Generic CoT on reasoning models:** contested. d02 says marginal (+2.9, +3.1, -3.3 points); d14 says helpful on distilled R1 but its direct baseline suppresses thinking. d05 (39 problems, one sample) is within noise.
- **Fine-tuning on Polya dialogues:** no accuracy measured; stacking with MetaMath interfered (a22, c02).

### 5.3 Moderators (what changes the size of the effect)

| Moderator | Direction | Evidence |
|---|---|---|
| Solver strength | Gains shrink as the base gets stronger | Step-back (GPT-4 vs PaLM-2L), analogical (davinci 10.7 vs chat 1-3), PRISM (+7.6 to +0.9), TTS-Uniform |
| Human grade level | None in K-5, mild in 6-8, distinct in high school | Hembree abstract |
| Grain of specification | Fine-grained, trigger-linked beat label-only | Schoenfeld review (second-hand) |
| Problem length | Decomposition helps at 5+ steps, hurts at 2 | a20 |
| Task type | Large on world-knowledge and agent reasoning, small on maths | a21 |
| Error type | Helps calculation and missing-step; not misunderstanding or computation | a16, a21 |
| Task uniformity | One reusable plan beats fresh plans on uniform sets | d13 |
| Plan format | Prose beat JSON by 9 to 12 points | d13 |
| Ability to follow the approach | No gain if the model cannot execute it | d04 |
| Correctness of the hint | Wrong hints fall below CoT | c09 |
| Thinking mode | Prompt effect tiny on reasoning models, unless the baseline suppresses thinking | d02, d14 |

### 5.4 Interventions that worked and did not

**Worked (with caveats):** annotated worked solutions in humans; forward/backward combined check (+1 to 2); approach-diversity splits on non-reasoning models; category-aware routing (modest); correct hints; prose plans; stage-gated decomposition on long problems; complementary methods with a strong checker.

**Did not work or unproven:** drilling one heuristic per problem type; rigid step-by-step; restating (humans); generic self-review with no outside signal; random backtracking; Polya text injected as context for correctness; fine-tuning for stage balance (no accuracy measured); priming with filler tokens (b16).

### 5.5 What is missing from the evidence base

- Almost all LLM results are from 2023-era models (text-davinci-003, PaLM-2, GPT-3.5, GPT-4). Almost nothing on current reasoning models except 2025-26 preprints.
- Equal-token controls are missing in most studies. PS+, analogical prompting and Self-Discover use longer outputs or extra calls. Some of each gain may be extra compute.
- Work backwards, draw a figure and look back are almost untested as LLM operators.
- No hand-written precondition rule has been tested.
- The Hembree effect sizes were never read.

---

## 6. Language models

### 6.1 How models behave on these tasks

1. **Models skip planning by default.** Llama-3.1-8B Instruct spent only 7.8% of dialogue on planning against 18.9% after Polya tuning (c02). Polya-tuned models follow the stage order but the look-back stage stays shallow (d06).
2. **Understanding is mostly fine on recent models; reasoning and reflection vary.** On SMART, most of 22 models score above 90% on Understanding; Reasoning ranges 9.05% to 93.61%; Reflection best is 78.62%, about nine times the weakest (a29). o3: final answer 91.44% but all four stages pass only 64.87%.
3. **They are narrow in strategy.** Frontier models found 110 to 184 of 217 reference strategies on 80 AMC/AIME problems, despite accuracy near ceiling (c11). One dominant strategy often outweighs all others combined; in 500 samples on 3 AIME problems, the dominant strategy was often more than twice the rest together (d03).
4. **Failure on novel variants is partly a control failure.** Hard perturbations cut MATH accuracy by 10 to 30 points (Qwen3-32B 92 to 76); the heuristic mix shifts, but not enough (a24).
5. **Backward reasoning is a real weakness.** GSM8K GPT-4 92.8 forward vs 38.6 backward (c08).
6. **Self-assessment fails without outside signals.** See 5.2 and d07, d09. Reasoning models are much better at judging others' steps (o1-mini 87.9 vs GPT-4o 61.9 F1 on ProcessBench), but live self-monitoring has not been measured.
7. **Heuristic behaviour is not something a prompt adds.** RL solutions overlap strongly with strategies already in the base model (a25). Gandhi et al. (b15, b16) show base models with verification, backtracking, subgoals and backward chaining learn faster; backtracking mattered most. A prompt cannot create a skill the model lacks (G12).

### 6.2 What changed performance, and by how much

| Intervention | Model class | Change | Equal tokens? |
|---|---|---|---|
| Plan-first prompt (PS+) | davinci-003 | +6.3 avg (70.4 to 76.7); +2.9 GSM8K | No (longer outputs) |
| Step-back | PaLM-2L | +7.8 / +10.9 physics / chemistry vs CoT | Not stated |
| Step-back | GPT-4 | +1.6 / +0.3 vs CoT, inside noise | Not stated |
| Least-to-most | code-davinci-002 | SCAN length +83.5 vs CoT; GSM8K +1.5 | No (two prompts) |
| Self-Discover | PaLM 2-L | BBH +7, T4D +29, MATH +8.5 vs CoT | 3 extra calls, 10-40x fewer calls than self-consistency baselines |
| Self-Discover | GPT-4 | BBH +6, T4D +33, MATH +2 vs CoT | Same |
| Analogical prompting | GPT-3.5 | +2.0 GSM8K, +3.4 MATH vs 0-shot CoT | No |
| Approach diversity (TTS-Uniform) | GPT-4.1-mini | +13.3 AIME24 Acc@32 | Equal samples |
| Approach diversity (DIV-SE) | GPT-4 | Graph Colouring 23 to 97 vs SC-10; MATH C&P +16.9 | Lower cost reported |
| Router (PRISM) | 7-8B | +0.9 to +7.6 vs best single | Roughly equal |
| Backward check (FOBAR) | davinci / GPT-3.5 | +1.1 to +2.1 vs SC | No (extra chains) |
| Prose vs JSON plan | 405B, Large | +12 / +9 on MATH | Same content |
| Self-review, no signal | GPT-4 | -6.5 over two rounds (95.5 to 89.0) | n/a |
| Step-by-step prompt | o3-mini / o4-mini / Flash 2.5 | +0.029 / +0.031 / -0.033 (rating) | +20-80% time |

### 6.3 What this means in one paragraph

Polya-style prompting works best on weaker or older models, on tasks where the bottleneck is naming a principle or filling a skipped step, and when the prompt is concrete and matched to the problem. Gains shrink or vanish on strong models and on reasoning models. The diversity result (spreading attempts across named approaches) is the best-supported use of a menu, but it was measured on non-reasoning models with majority vote. The open question that decides everything for us is whether any of this survives at equal tokens on a current reasoning model.

---

## 7. What our agent should take

Format: item, schema part, status, evidence ids.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep operators out of the default path; use them only on a failure signal.** Heuristics need preconditions; a fixed menu for every problem has weak support. | G1, S6 (already in schema) | [E] | a03, b02, K02; Hembree abstract (a28, d15); c01 (informal) |
| A2 | **No vague self-review.** Any check must be concrete (recompute, substitute, special case, bound), run by code, and show the real output. | G2, G10 (already in schema) | [E] | d07, d09, d16 (K25) |
| A3 | **Treat a revision or intervention as costly.** Record fixed and broken rates for every operator, and keep best-so-far. | S5, G6, S9 log (section 6 of SCHEMA.md) | [E] | d16, a18 (20.5% fixed / 11.9% broken), c22 |
| A4 | **Add a diversity rule to open and no-check modes where sampling is used:** make attempts differ by named approach instead of repeating one prompt, and stop weak approaches by answer entropy. Only where majority vote is the aggregator and the model is not a reasoning model. This is a narrowing of S3, tested already on non-reasoning models in two independent sources. | S3, S7 | [E] for non-reasoning models only; do not extend to reasoning models until U1 passes | d03, d04 (K28) |
| A5 | **Gate execution-heavy operators by model ability.** If the model cannot follow an approach, a menu gives nothing. | S0 gate | [E] | d04 (GPT-3.5 Blocksworld, LLaMA-2 zero-shot), a25 |
| A6 | **Pair structural operators with code for computation.** Most maths failures are execution. | G3, S4 | [S] on number (74.7%), [E] on direction (also b17, a29) | a21, c23, b17, a29 |

A4 is the one place where the evidence sits in tension with G4's "no persona or strategy voters on single-answer problems". G4 is justified by our own measurement (92% plain vs 75% voters on word puzzles). A4 is therefore restricted to non-reasoning models in the evidence, and has not been added to the schema as a rule; it enters UNKNOWNS.md as a test. Treat A4 as "add after U1 passes" in practice.

### Test first

| # | Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|---|
| T1 | Operator records with precondition, procedure and worked example, not bare labels | O1-O8 | [S] | a01, a02, b03, b21 (K01) | Argument, not experiment |
| T2 | Concrete three-question control step, code-triggered | S6, G1 | [S] | a05, a06, b05 (K03); K25, K26 | 60% to 20% has no N; reasoning models untested |
| T3 | Annotated worked solutions (operator tag + how) shown after first attempt | S9, memory | [E] human, [S] model | a09, d01 (K04) | Human d 0.79, n about 10 per cell |
| T4 | Decompose gated by estimated step count (4+ steps) | O3 | [S] | a20, b11 (K12) | One model, one set |
| T5 | Work backwards as reformulate-to-forward and as substitution check | O5, S8 | [S] | c08, d10, d11 (K15, K29) | No equal-token test |
| T6 | Change representation first (diagram/table) as the first operator at impasse | O6 | [S] | a28, d15; nothing on LLMs | Biggest human lever, zero LLM data |
| T7 | Step-back as principle retrieval at impasse on knowledge-heavy classes | O2 | [S] | a17, a18, c22 (K10, K11) | Gain near noise on strong models |
| T8 | Prose plans, not rigid structured fields | rendering of S2, O menu | [S] | d13 (K30) | One paper, no repeats |
| T9 | Task-level plan reuse on uniform classes; fresh plan on mixed | S0, memory | [S] | d13, c19 (K07, K30) | T4D result on a rebuilt set |
| T10 | Self-generated related problem at impasse | O7 | [S] | c05, c24 (K14) | 1-3 points on strong models |
| T11 | Restate-and-check understanding, number extraction checked by code | S1 | [S] | a16, b10, b18 (K09) | Model-dependent; null for humans |
| T12 | Hand-written precondition router for O1-O5 vs plain, by problem class | S6 | [S]/[C] | d12, c13, c01 (K17, K23) | Never tested; classifier accuracy caps the gain |
| T13 | Approach diversity on a reasoning model, verifier instead of majority vote | S3, S7 | [S] | d03, d04, K21 | Measured on non-reasoning models only |
| T14 | Keep a heuristic-use log with the SHAPE taxonomy | section 6 (log) | [S] | a23 | Labeller F1 70-77, noisy |
| T15 | Do not add Polya text as context to improve correctness | n/a | [S] | b19 | Content quality not improved |

---

## 8. Concrete tests on our bench

All arms at equal tokens. "Equal" means the total tokens (thinking plus visible, setup and extra calls included) are matched to the largest arm, by either capping the larger arm or giving the smaller arm more plain samples. Report accuracy per token, not only accuracy. Use at least 25 samples per problem on reasoning models and a paired test (d02, d05 show 5-point differences on 39 problems are noise). Log thinking tokens.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| U1 Menu vs bare on a reasoning model | Maths problems with a numeric answer, mixed difficulty (GSM8K-hard, MATH levels 3-5, competition); also ARC and BRAINTEASER items | (a) bare problem; (b) O1-O5 menu with precondition and procedure given once; (c) k attempts each with a different O1-O5 operator, vote; (d) k plain samples, vote | Accuracy at equal total tokens; paired difference | Near zero for (b) on easy items; small positive for (c) on hard items; negative if the menu lengthens thinking |
| U2 Diversity with verifier | Items with a code check (ARC with held-out example, numeric answers with substitution) | k named-approach attempts + verifier vs k plain samples + verifier vs k named-approach + majority vote | Accuracy; share of items where approach arm covers a solution plain misses | Approach-diversity gain bigger with a verifier than with vote if solved sets differ (K21); shrinks on strong models |
| U3 Control step concrete vs generic vs none | Hard items where the first attempt often fails | (a) no control; (b) generic "review your answer" every K steps; (c) three-question control with a code-run check, triggered on impasse; (d) same, but on a fixed schedule | Final accuracy; false-alarm rate (right answers changed to wrong); dead-end persistence (steps after the first failed path) | (c) > (a) at hard items; (b) <= (a); (d) <= (c), because G1 says doubt only on a signal |
| U4 Operator label vs record | Items from three classes (integer-parameter sums, polynomial roots, recursions) | (a) label only; (b) label + procedure; (c) label + procedure + trigger + worked example | Accuracy on impasse subgoals; fixed-vs-broken rates | (c) > (b) > (a) on class-matched items; (c) not worse on unmatched items |
| U5 Annotated vs plain worked examples | Held-out problems with a class shared with the examples | In-context worked solutions: (a) none; (b) plain; (c) with operator tag and how it was used (shown after first attempt) | Accuracy on second attempt | Human d about 0.8; for models expect small, if any |
| U6 Decompose gated | Math word problems by step count (2, 3, 4, 5+) | Always decompose; never decompose; decompose only when estimated steps is 4+ or first attempt failed | Accuracy per step-count bin; tokens | Gated >= both; always-on loses at 2 steps (a20) |
| U7 Work backwards | Problems with a numeric target | (a) direct backward prompt; (b) reformulate-to-forward; (c) substitution check on forward answer; (d) none | Accuracy; right-to-wrong flips | (b) and (c) > (a); (c) gains 1-2 points (K29) |
| U8 Change representation first | Geometry-flavoured, grid and counting items | Draw/table first at impasse vs other operators first vs none | Accuracy; operator that solved the subgoal | Largest per-operator effect if Hembree transfers |
| U9 Plan format | Same plan content, any reasoning model | Prose vs JSON fields | Accuracy | Prose +9 to +12 on MATH (d13) |
| U10 Router accuracy ceiling | Items labelled by problem class | Code features vs model yes/no vs oracle label, routing O1-O5 | Routing accuracy; accuracy with predicted vs true class | Predicted about 29% below oracle (c13) |
| U11 Hint damage | Items with an injected wrong, vague, or correct hint | Correct, vague, wrong, none | Accuracy drop from wrong hint | Wrong < none (c09); checks whether S1 input hygiene catches it |
| U12 Understanding check | Word problems with distractors | Restate + extraction check by code vs none | Semantic-error share | Small cut in the 26-27% class on weaker models |

Every test logs: operator tried, whether it solved a subgoal, items fixed vs broken, thinking tokens, wall time.

---

## 9. What does not transfer, and why

| Human result | Why it may not transfer to our agent |
|---|---|
| Months needed to build the control habit (a06) | A model can be prompted at every trigger. But the human result does not tell us whether the check is any good. |
| Heuristic benefit grows with grade (Hembree) | For models, the parallel is base ability, but our direction (stronger model, smaller gain) is the opposite of "more competent, more benefit". Both can be true: a floor of competence, then diminishing returns. |
| Drilling turns heuristics into algorithms (a08) | Our operators are code-triggered and model-executed. Drilling is not a risk in zero-shot prompts, but fixed templates (rigid order) risk the same loss of flexibility (b26). |
| Explicit teaching beats practice (d01) | A model does not learn between prompts. The closest analogue is in-context examples (T3), whose effect is untested. |
| The monitor questions "what are you doing, why, how does it help" | Written reasoning is not a faithful record of what a model did (G10). Use the answer only to pick an abandon-or-continue decision, backed by code checks. |
| Schemas in experts (a30) | Our schema bank is built from our own runs, not decades of practice. Retrieval by similarity (Buffer of Thoughts) is the machine version and carries its own risk of crude schemas. |
| Polya's "look back" (derive the result differently, use it elsewhere) | In a model with no new information, look-back hurts (d07). Only look-back with a concrete new test (substitute, special case, independent method) is defensible. |
| Polya training studies on adults with strong maths (Rott and Gawlick) | Selected maths-teacher students; the model has no such selection. Effect size d 0.79 should not be taken as a prior for models. |
| SHAPE and Gandhi training results | Training-time. A frozen model with a prompt cannot gain a behaviour it lacks (a25). |
| Llama-Polya stage balance (a22) | Tutoring dialogue, not problem solving. No accuracy evidence. |
| Chess-to-maths transfer (b08) | Domain-shared structure required; confounded design. |

---

## 10. Open questions

1. Does an O1-O5 menu beat the bare problem on a current reasoning model at equal tokens? (U1) Everything else depends on this.
2. Which problem features predict when each operator helps or hurts? Only a blog (c01) gives per-type data. No precondition rule is tested.
3. Is the bottleneck selection or execution? L2M says the decomposition choice is the bottleneck; Self-Discover says 74.7% of failures are computation. A direct split on one model is missing.
4. Does the concrete control step help reasoning models in a live self-check? ProcessBench says they judge others' steps well (87.9 F1 for o1-mini); live self-check is unmeasured.
5. Does diversity help with a verifier, and does it help reasoning models? All diversity evidence is vote-based and on non-reasoning models.
6. What are the Hembree effect sizes by grade and method? Abstract only.
7. How large is the human effect of explicit heuristic training? Larger replication of Schoenfeld 1979 and Rott and Gawlick 2014.
8. How much damage does a mis-selected heuristic do on a current model, and can a concrete check catch it? Wrong hints hurt (c09); random backtracking broke 7 to 16 points (d16); nothing for operator misselection.
9. Do "draw a figure" and "look back" have any equal-token LLM evidence? None found.
10. Do reasoning models already do Polya moves implicitly? (Link: Schoenfeld episodes subfield; ThinkARM, SHAPE.) If yes, a prompted menu may only add tokens.
11. Does prose beat JSON on reasoning models, and for the operator menu itself?
12. Does the Polya-annotated worked-example effect (d 0.79 in humans) appear when examples are in context?
13. Does heuristic diversity gain shrink to zero as base ability rises? Evidence says it shrinks (d03, d12, c05, a17); the zero point is unknown.

---

## 11. Sources

Key: [V] opened and read this session (full text or the cited section); [M] snippet, abstract only, second-hand, or from memory.

### Human studies and reviews

- [V] Schoenfeld (1992) Learning to think mathematically (Handbook of Research on Mathematics Teaching and Learning). https://jwilson.coe.uga.edu/emat7050/Schoenfeld_MathThinking.pdf and https://faculty.tarleton.edu/brawner/wp-content/uploads/sites/11/2023/02/Schoenfeld_MathThinking.pdf (a01-a08, a30, b01-b06, b21, b22)
- [M] Schoenfeld (1985) Mathematical Problem Solving (book). https://digitalcommons.lib.uconn.edu/dissertations/AAI9006699 (a14; snippet only)
- [V via Rott and Gawlick] Schoenfeld (1979) Explicit heuristic training as a variable in problem-solving performance, JRME 10, 173-178 (a09). Original not opened; described by the replicators. Mark as [M] for the original.
- [V] Rott and Gawlick (2014) Explizites oder implizites Heurismentraining: was ist besser? Mathematica Didactica 37. https://journals.ub.uni-koeln.de/index.php/mathematica_didactica/article/download/1126/1080/3141 (a09-a13, d01)
- [M] Hembree (1992) Experiments and relational studies in problem solving: a meta-analysis, JRME 23(3), 242-273. https://doi.org/10.5951/jresematheduc.23.3.0242 (a28, d15; abstract only, effect sizes not obtained)
- [V] Bruun (2013) Elementary teachers' perspectives of mathematics problem solving strategies (quotes Hembree). https://files.eric.ed.gov/fulltext/EJ1020068.pdf (b07, b24, b26)
- [V] Trinchero and Sala (2016) Chess training and mathematical problem solving. https://www.ejmste.com/article/chess-training-and-mathematical-problem-solving-the-role-of-teaching-heuristics-in-transfer-of-4483 (b08, b25)
- [M] Koichu, Berman and Moore (2007) Heuristic literacy development, Instructional Science (a27; via Rott and Gawlick)
- [M] Lester, Garofalo and Kroll (1989) metacognition instruction (a07, b06; via Schoenfeld 1992)
- [M] Lucas (1974), Kantowski (1977), Collet (2009), Brockmann-Behnsen (2012, 2014), Wilson (1967), Smith (1973), Begle (1979), Harvey and Romberg (1980), Silver (1979, 1981), Heller and Hungate (1985): second-hand through Schoenfeld 1992 or Rott and Gawlick

### LLM studies: plan, abstract, decompose, analogy, menu

- [V] Wang et al. (2023) Plan-and-Solve Prompting. https://arxiv.org/abs/2305.04091 and https://arxiv.org/pdf/2305.04091v3 and https://ar5iv.labs.arxiv.org/html/2305.04091 (a15, a16, b09, b10, b20, b28, c03, c21)
- [V] Zheng et al. (2024) Take a Step Back. https://arxiv.org/abs/2310.06117 (a17, a18, b12, b27, c04, c22)
- [V] Zhou et al. (2023) Least-to-Most Prompting. https://arxiv.org/abs/2205.10625 (a19, a20, b11, b23; c06 is [M], from memory, later verified)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 and https://arxiv.org/html/2402.03620 (a21, b14, c07, c23)
- [V] Yasunaga et al. (2024) Large language models as analogical reasoners. https://arxiv.org/abs/2310.01714 (b13, c05, c24)
- [V] Zhu et al. (2024) Look Before You Leap (problem elaboration). https://arxiv.org/pdf/2402.15764 (b18)
- [V] Agrawal et al. (2024) Give me a hint. https://arxiv.org/html/2410.05915v2 (c09)
- [V] Gunasekara and Ratnayake (2025) Effects of structure on reasoning in instance-level Self-Discover. https://arxiv.org/abs/2507.03347 (d13)
- [V] Yang et al. (2024) Buffer of Thoughts. https://arxiv.org/html/2406.04271v2 (c19)

### LLM studies: diversity, routing, backward, control

- [V] Wu et al. (2025) Mitigating strategy-selection bias (TTS-Uniform). https://arxiv.org/abs/2509.17905 (d03)
- [V] Naik et al. (2024) Diversity of Thought (DIV-SE). https://arxiv.org/abs/2310.07088 (d04)
- [V] Qi et al. (2025) PRISM. https://arxiv.org/abs/2509.24377 and https://arxiv.org/html/2509.24377 (c12, d12)
- [V] Categorization and strategy tailoring (2024). https://arxiv.org/html/2411.00042v3 (c13)
- [V] Yang et al. (2026) Beyond Accuracy: strategy diversity. https://arxiv.org/html/2605.09292v1 (c11)
- [V] Fill in the Blank: backward reasoning (2023). https://arxiv.org/pdf/2310.01991 (c08)
- [V] Chen et al. (2025) RevThink. https://arxiv.org/abs/2411.19865 (d10)
- [V] Jiang et al. (2024) FOBAR. https://arxiv.org/abs/2308.07758 (d11)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d07)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors but can correct them. https://arxiv.org/abs/2311.08516 (d09, d16)
- [V] Zheng et al. (2024) ProcessBench. https://arxiv.org/abs/2412.06559 (d08)
- [V] Meincke et al. (2025) The Decreasing Value of Chain of Thought. https://arxiv.org/abs/2506.07142 (d02)
- [V] Ge et al. (2025) Innate Reasoning is Not Enough. https://arxiv.org/abs/2503.19602 (d14)
- [V] Salah and Muneer (2026) Temperature-dependent performance of prompting strategies. https://arxiv.org/abs/2604.08563 (d05)
- [V] Sprague et al. (2025) To CoT or not to CoT. https://arxiv.org/pdf/2409.12183 (b17; abstract, intro and findings only)
- [V] Sinha et al. (2024) Wu's Method can Boost Symbolic AI. https://arxiv.org/html/2404.06405v1 (c14, c25)
- [V] Duan et al. (2025) HAGeo. https://arxiv.org/abs/2512.00097 (c15; abstract page only)

### Polya-structured and heuristic-labelled LLM work

- [V] Lee et al. (2026) Llama-Polya. https://arxiv.org/abs/2602.10597 and https://arxiv.org/html/2602.10597v1 (a22, c02, d06)
- [V] Anonymous (2026) SHAPE of Thinking. https://arxiv.org/html/2608.28600 (a23-a26)
- [V] Anonymous (2025) SMART. https://arxiv.org/abs/2505.16646 (a29; c10 PDF was unparseable, [M])
- [V] Gandhi et al. (2025) Cognitive behaviors that enable self-improving reasoners. https://arxiv.org/pdf/2503.01307 (b15, b16)
- [V] Schorcht, Muller and Buchholtz (2026) No one-size-fits-all. https://link.springer.com/content/pdf/10.1007/s11858-026-01784-6.pdf (b19)
- [V, informal] Anand (2026) Testing Polya heuristics on AI math (blog). https://www.s-anand.net/blog/testing-polya-heuristics-on-ai-math/ (c01)
- [M] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c17)
- [M] Li et al. (2025) ThinkARM (Schoenfeld-style episodes). https://arxiv.org/html/2512.19995v1 (c16; link only, see the Schoenfeld episodes subfield)
- [M] TU Dresden (2025) Context injection, Polya knowledge base (c20; listing only, no results)
