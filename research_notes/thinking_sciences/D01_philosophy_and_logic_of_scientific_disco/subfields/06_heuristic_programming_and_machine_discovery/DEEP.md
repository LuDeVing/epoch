# Heuristic programming and machine discovery: deep document

*Subfield D01.06. Sources: evidence_a-d.jsonl (ids a01-d20), claims.jsonl (K01-K34), critique.md. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Numbers are as read in the papers; section 11 shows which sources were opened.*

## 1. What it is

This field asks one question. Can discovery be done by a program that searches with a short list of heuristics, tests each guess against data, and keeps what passes?

Herbert Simon and Pat Langley built programs in the 1970s and 1980s that did this for empirical laws (BACON) and for experiment strategy (KEKADA). In the 2000s, King's group built robot scientists (Adam, Eve) that ran the loop in a real lab. From 2020, symbolic regression (AI Feynman, PySR) and then language models (LLM-SR, LaSR, FunSearch, AlphaEvolve, AI Scientist) re-ran the same loop with a learned generator.

The shared shape is generate and test:
1. A generator proposes a candidate law, program or experiment.
2. A checker scores it on data.
3. The score steers the next proposal.

The field splits on where the knowledge sits: in a hand-written heuristic list (BACON), in a cost-staged search ladder (AI Feynman), or in a language model that proposes structure while code fits and scores (LLM-SR).

Why it matters for our agent. Our schema is a generate-and-test graph (S3 generate, S4 test, S5 revise, S6 impasse). Operators O1-O8 are heuristics fired at an impasse. This subfield is the oldest working model of that design. It also has the best modern measurements of what the checker is worth.

## 2. History and theories in depth

### 2.1 BACON (1977-1987)
- **BACON.1 (Langley 1977, IJCAI-77; a01, a02).** A two-page design note. A small set of production rules runs as parallel regularity detectors over attribute-object-value tuples. A constancy triggers a generalisation. A monotone trend triggers a new defined term: a ratio if two variables move together, a product if they move in opposite directions. The law is a higher-level term that turns out constant. Hypotheses are never rejected, only qualified with bounds. No quantitative results. Authors' own limits: no conditional laws, built-in choice of which dimensions to vary, no noise handling.
- **BACON.3 (Langley 1979; a03, a04).** Rediscovered the ideal gas law, Kepler's third law, Coulomb's law, Ohm's law and Galileo's laws. In the ideal gas run it built pV at level 1, pV/T at level 2 and pV/nT at level 3. Each level reuses the same few rules on the output of the level before (recursion over description levels). Two experiment orderings per task gave the same final laws at different cost.
- **BACON.4 and .5 (a05, b20).** Added intrinsic properties and conservation laws. In the BACON.5 ideal gas example (n=1, T=300), V falls as p rises, pV is tried and found constant at 2496.0 (R = 8.32, nRT = 2496). It also exploits symmetry or analogy: a relation found for one object is reused to cut the search for the next.
- **The 1987 book (c26, a28; snippet only).** Collects the programs and their later cases (Black's law, momentum, energy).
- **What was claimed.** Sufficiency: a short list of data-triggered heuristics can rebuild known laws. Not claimed: success rates, noise robustness, or discovery of anything new (K02).

### 2.2 KEKADA (Kulkarni and Simon 1988; a09, a27, d17)
KEKADA replays Hans Krebs's discovery of the urea cycle. Unlike BACON it reacts to surprise: when an outcome differs from expectation, it sets a new goal to explain the anomaly and picks experiments for that goal. Only the abstract was reached (d17). It says the heuristics are largely domain-general. The heuristic list, experiment counts and goal rules were not read. KEKADA is the ancestor of impasse-triggered subgoaling (K05).

### 2.3 Later program lines (a06, a07, a08, a10, b16)
- **Dzeroski, Langley, Todorovski (2007; a10).** Moves from rediscovery to equation discovery with noise, background knowledge and process models.
- **Kramer, Langley et al. (2023; a06, a07).** Review. Lists systems that did real science: Zytkow's FAHRENHEIT coupled to electrochemistry, and a robot that rediscovered Galileo's inclined-plane law.
- **Langley (2024, AAAI-24; a08, a09).** States two open challenges: integration of components, and on-line revision of an accepted model when new data contradict it. Most work is batch (K25).
- **AI-Descarte (Cornelio et al. 2023; b16).** Adds logical derivability from background theory to symbolic regression. Candidates that contradict the theory are pruned. Recovers Kepler's third law, time dilation and Langmuir from few points (K24, single source).

### 2.4 Cost-staged symbolic regression (a11, a12, b01, b02)
AI Feynman (Udrescu and Tegmark 2020) is BACON's descendant in spirit. It tries cheap structural tests first: dimensional analysis, polynomial fit, symmetry, separability, additive or multiplicative splitting. These cut one hard problem into small ones. Brute force comes last. AI Feynman 2.0 adds Pareto-optimal complexity-versus-error output. Own result: 100 of 100 Feynman equations vs 71 for Eureqa, and a rise from 15% to 90% on a harder set. Other labs got far lower numbers (section 5).

### 2.5 Robot scientists (King et al.)
- **King 2004, Nature (a26, d14).** Abstract only. Cost-aware experiment selection was competitive with human choice and cut cost 3-fold and 100-fold against cheapest-first and random selection. Which factor goes with which baseline is not confirmed.
- **Adam (King 2009, Science; a25, b18, c27: snippets).** A closed loop in yeast: knowledge base, abductive hypothesis, planned experiment, robot run, measured result, update. A 2010 review (d16) counts twelve genes assigned to locally orphan enzymes. An earlier note said six; unresolved.
- **Eve (Williams et al. 2015; a22, a23, d15).** Drug screening. Active screening is supported only by an economic replay on a real 14,400-compound screen: screening a third to a half of the library was cost-optimal. TNP-470 hit P. vivax DHFR (IC50 0.16 uM against over 165 uM for the human enzyme, about 1000-fold; b19).
- **2026 Eve study (a24, b17).** On YGR067C, effects were only partly significant.

### 2.6 Evolutionary program search (2023-2025)
FunSearch (Nature 2024; c12, d12), AlphaEvolve (2025; b09, c10, c11, d11), ShinkaEvolve (d10) and Eureka (c25, d09) keep a population of programs, ask an LLM to mutate good ones, and score each with an automatic evaluator. This is generate and test with a model as the mutation operator.

## 3. Core findings with exact numbers

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| BACON rebuilds known laws from small hand-prepared data with a few data-triggered heuristics | 5+ laws (ideal gas, Kepler 3, Coulomb, Ohm, Galileo); ideal gas built in 3 levels (pV, pV/T, pV/nT); no success rate reported | a01, a03, a05, a06, a10, c26 | [E] for sufficiency on known cases only |
| Early demos prove sufficiency, not discovery | programmer-chosen variables, no noise handling, no rates | a02, a03, a05, a10 | [E] |
| Experiment order changes cost, not the final law | 2 orderings per task, same laws | a04 | [S] |
| Cost-staged search beats one big search | AI Feynman 100/100 vs Eureqa 71 (own paper); 15% to 90% on harder set | a11, a12, b01, b02 | [E] on direction; headline [C] |
| AI Feynman headline fails to transfer | LaSR table 38/100 (PySR 59/100); SRBench exact recovery 53% at zero noise, behind others above noise 0.01 | b03, c07 | [C] |
| Numeric fit is not form recovery | 46-50% Acc0.1 but 5-13% symbolic (LaSR-class); PySR 0% symbolic outside physics | a15, b25, c05, c06 | [E] |
| LLMs partly recite known laws | best symbolic accuracy on disguised sets 31.5% (Transform), 28.1% (Synth); other splits 30.63% and 10.81%; direct prompt without data 7.21% | a13, a15, a16, b06, b21, c03-c05 | [E] |
| Role split: LLM proposes structure, code fits constants | LLM-SR about 2.5K iterations vs 2M+; E. coli OOD NMSE about 0.0037 vs above 1; no refine loop NMSE 1.01e-1 ID, 1.81e-1 OOD; no skeleton+optimizer 3.78e-1 | a13, a14, b05, c01, c02, c24 | [E] (authors' numbers, one family) |
| Very sparse LLM calls help a classic search | LaSR 72/100 vs PySR 59 +-3, LLM called on 1% of steps; Llama3-8B at 1-10% call rate 67-71; 41 synthetic equations test R2 0.913 vs 0.070 | c07, c08, c09 | [S] |
| Extra scaffolds do not beat plain code generation; only real feedback helps | DiscoveryBench best 25% (biology 0%); ReAct and self-critic planning not better than plain | a17, b07, c16, c17, c28 | [E] |
| Domain hints help modestly | DataVoyager 9.9% to 17.5% (+7.6 points, subset size not stated; labels in the sentence swapped, direction inferred) | a17, b07, d01 | [S] |
| More compute buys more at higher cost | ScienceAgentBench best 32.4% (34.3% with expert knowledge); 42.2% with o1-preview at over 10x cost | b08, b24 | [S] |
| Interactive discovery: agents lag humans | DiscoveryWorld best agent 38% easy, 18% challenge; humans 0.66 completion, 0.55 explanatory knowledge; brute force scores on completion but low on knowledge | c18, c19 | [S] |
| LLM experiment choice is weak | BoxingGym: all models struggle on information-gain choice; model+statistics scaffold not consistently better than plain GPT-4o, favours linear forms | c20, c21 | [S] |
| Frontier law discovery is real but fragile | NewtonBench, 324 counterfactual tasks, 11 LLMs: weak models under 10%, GPT-5 75.9%, Gemini-2.5-pro 65.4%; hardest setting 40.3% and 16.7%; code interpreter helps models below about 40%, slightly hurts stronger ones | d02, d03 | [S] |
| Noise breaks form recovery before fit | noise 0.0001 cut exact-form accuracy 12-16%, fit error flat | d03 | [S] |
| Without a strong checker, selection plateaus | MATH, Llama-3-8B: coverage 82.9% to 98.44%; majority/reward-model selection 40.50% to 41.41% beyond about 100 samples | d04 | [E] (with d03, d05) |
| Learned checkers get exploited by stronger search | stronger search against a process reward model hurts easy questions | d05, d06 | [E] |
| Evolutionary search with an evaluator finds real gains | AlphaEvolve matched best known on 75% and improved 20% of 50+ math problems; rank-48 for complex-valued 4x4 matrices (baseline 49, recursive Strassen); Eureka beat human rewards on 83% of 29 tasks, mean +52%, 16 samples x 5 iterations | b09, c10, c11, c25 | [E] |
| Depth beats breadth at equal sample count with rich feedback | Eureka 2 iterations x 16 beat 32 first-attempt; removing reward reflection cost 28.6% of normalised score; ShinkaEvolve weighted parent sampling beat hill climbing | d09, d10 | [E] |
| A hypothesis layer helps only when direct attempts are hard | ARC (100 tasks, GPT-4): direct 17%, programs 23%, summarised hypotheses 30%, human-selected 33%, Icecuber (no LLM) 43%; correct hypothesis on 49 tasks (33 of 49 solved); List Functions 31/59/69; SyGuS 94.3% both | a21, d07, d08 | [S] |
| LLM ideas look more novel before execution, worse after | novelty 5.64 vs 4.84, p<0.05, 49 ideas per condition, 79 reviewers, 298 reviews; after execution (N=43) AI ideas fell 1.05 (novelty), 1.76 (excitement), 1.88 (effectiveness) vs -0.010, +0.078, -0.052 for human; over-generation collapses to about 5% non-duplicates | b13, b14, b22, c22, c23 | [E] |
| Model judges are near chance at predicting outcomes | GPT-4.1 51.9%; fine-tuned 77% on published pairs, 63.6% on 33 new ideas; 25 human experts 48.9% on NLP | d13 | [S] |
| End-to-end science agents fail in documented ways | 5 of 12 experiments failed on coding errors; median 5 citations (5 of 34 from 2020+); first four benchmarks chosen in 82.4% of 945 runs; AI Scientist reviewer 70% accuracy vs 73% human, F1 0.57 vs 0.49, AUC 0.65; under $15 per paper | a18, a19, b10-b12, c13, c14 | [E] |
| AI Scientist-v2 | 1 of 3 papers reached workshop acceptance level (6.33/10); N=3 | b15, c15 | [S] |
| Robot scientists run the loop and validate findings | Adam twelve genes (2010 review); Eve TNP-470 about 1000-fold; King 2004 cost cuts 3-fold and 100-fold; Eve 2015 replay: screen a third to a half of the library | a07, a22-a24, b17-b19, c27, d14-d16 | [S] |
| On-line revision works with exact counterexamples, not by prompting alone | WorldCoder revises code world models (ReAct baseline 15% +-8% of Sokoban levels); LLMs improve little after round 1 in a 5-round belief task | d18, d19 | [S] |
| A generic heuristic library chosen per task beats CoT | Self-Discover: 39 modules, BBH +7 and +6 over CoT and Plan-and-Solve on PaLM 2-L (+6, +8 on GPT-4); 10-40x fewer calls than self-consistency | d20 | [S] |
| Small-model retention of evolutionary gains is unclear | FunSearch "not too sensitive" to code LLM (about 10^6 samples); AlphaEvolve says larger models help (no number); ShinkaEvolve record in 150 samples with frontier ensemble | c11, d10, d11, d12 | [C] |
| Co-scientist Elo rises with compute | Elo is the system's own judge; independent checks: few wet-lab results, 15 curated goals | a20, d13 | [S] |

## 4. Mechanisms and models

### 4.1 BACON as an engineer would build it
State: a table of terms. Each term is a variable or a derived term, with one value per row.

Loop, per level:
1. For each term, test if it is nearly constant across rows (tolerance test). If yes, report the law and stop.
2. Else, for each pair of terms, test if one rises while the other falls (sign of correlation over sorted rows).
3. If they move together, define a ratio. If in opposite directions, define a product.
4. Add the new term as a column and go to 1. Cap depth (3 levels in the ideal gas case).
5. With several independent variables: hold the others fixed, vary one, fit, treat the fitted parameters as new data, and repeat. This gives pV, then pV/T, then pV/nT.

Design choices:
- Constancy is a tolerance test. The originals had minimal noise handling.
- Hypotheses are qualified with bounds, not deleted.
- Reuse by symmetry: after solving one object, try the same form on the next (K04).

### 4.2 KEKADA's surprise trigger (abstract only; unverified)
1. Hold an expectation about an outcome.
2. Run the experiment and compare.
3. If the outcome differs, open the goal "explain this anomaly" and choose the next experiment by heuristics tied to that goal.
4. Else continue the planned line.

### 4.3 Cost-staged ladder (AI Feynman)
Order modules by cost. Run cheap ones first: unit analysis, low-degree polynomial fit, symmetry check, separability check. If a module splits the problem, recurse on the parts. Only then run brute force. Filter survivors by error versus complexity.

### 4.4 Propose, fit, feed back (LLM-SR, LaSR)
- **LLM-SR (a13, c01, c02).** The LLM writes an equation skeleton as code with free constants. A numeric optimiser fits the constants. The score and the best skeletons go into the next prompt. Removing the refine loop or the skeleton+optimiser each hurts.
- **LaSR (c07).** A classic evolutionary regression search. On about 1% of steps an LLM reads learned natural-language "concepts" and proposes edits. The concept library grows from good equations. The gain survives a leakage control (c08) and a 1-10% call rate (c09).
- **Equal-token note.** None of these compare against an LLM given the same tokens as pure reasoning. That is the gap behind K01.

### 4.5 Population search with an evaluator (FunSearch, AlphaEvolve, Eureka, ShinkaEvolve)
1. Keep a pool of programs with scores.
2. Sample parents, weighted by score, not always the best (d10).
3. Prompt the LLM with the parents plus evaluator feedback text.
4. Evaluate the children; insert the good ones.
5. Repeat. Eureka's reward reflection (a summary of what each reward component did) is the rich feedback. Removing it cost 28.6% of the score (d09).

### 4.6 Hypothesis-then-program (Hypothesis Search; a21, d07)
Ask the model for 64 candidate natural-language rules, summarise to 8, write a program per rule, run on the examples. Limit: only 49 of 100 ARC tasks had any correct hypothesis, so hypothesis quality caps the gain.

### 4.7 Active experiment choice (King 2004, Eve)
Score each possible experiment by expected information per cost. Run the best. Update. Reported gain: cost cut 3-fold and 100-fold against cheapest-first and random.

## 5. What holds up

**Holds up (several sources).**
- A hard automatic checker plus a population of candidates yields real gains (K17, K28). AlphaEvolve, Eureka, FunSearch, LLM-SR and LaSR all rely on one.
- Feedback from real output beats model self-critique (K12).
- Selection is the bottleneck, not generation. Coverage rises to 98.44% while selection stays near 41% (d04). Judges are near chance on outcomes (d13). Idea quality reverses after execution (b14).
- Fit is not form (K08). Disguised problems cut scores sharply (K09).
- Noise matters more than benchmarks show (d03).

**Replications and failed replications.**
- AI Feynman: 100/100 (own) vs 38/100 (LaSR table) vs 53% exact at zero noise (SRBench). A setup difference (tuned symbol sets, 1-2 extra hours on some equations, budgets), not a transcription error. Do not quote 100/100.
- BACON: no independent replication with success rates was found in what was read.
- Eve 2026 study on YGR067C: only partly significant effects (a24).
- DiscoveryBench hint effect: apparent direction conflict was a swapped label in the sentence; resolved to +7.6 points on an unstated subset (d01).

**Moderators.**
- Checker strength (K26): strong checker gives large gains; noisy or learned checker gives plateau or harm.
- Task difficulty: the hypothesis layer helps on ARC (17 to 30) but not on SyGuS (94.3% both) (K27).
- Model strength: a code interpreter helps models below about 40% and slightly hurts stronger ones (d03).
- Noise: 0.0001 is enough to break form recovery.
- Contamination: famous equations are easier than disguised ones.

**Interventions that worked.** Propose-fit-feedback split (K10). Sparse LLM calls inside a classic search (K11, single source). Revise-the-best with rich feedback at equal samples (K28). Exact counterexample feedback for revision (K31, single source). Cost-staged ladders in symbolic regression (K06). Weighted parent sampling (d10).

**Interventions that did not work.** Self-critique and ReAct-style scaffolds in DiscoveryBench (K12). Model-judge ranking (K18, K29). Over-generating ideas (about 5% non-duplicate). Scaling search against a learned checker (d05). BoxingGym's statistics scaffold for experiment design (c21). Prompting alone for belief update across rounds (d18).

## 6. Language models

**On law discovery.** Frontier models do real discovery on counterfactual tasks. NewtonBench: GPT-5 75.9%, Gemini-2.5-pro 65.4%, weak models under 10%, hardest setting 40.3% and 16.7% (d02, d03). On LLM-SRBench, direct prompting with no data gets 7.21% and the best data-driven method gets 31.5% on one split and 28.1% on another (a15, c05). The gap between those numbers is the value of the propose-fit-feedback loop. The gap between famous and disguised equations is recitation.

**What changed the numbers, and by how much.**
- Code fitting and feedback: LLM-SR about 2.5K iterations where classic search used 2M+; E. coli OOD NMSE about 0.0037 vs above 1.
- A sparse LLM added to a classic search: LaSR 72 vs 59 (13 more equations); R2 0.913 vs 0.070 on 41 synthetic equations.
- Hypotheses added: ARC 17 to 30 (GPT-4).
- Code interpreter added: helps weak models, slightly hurts strong ones that settle early (d03).
- Noise 0.0001: exact-form accuracy down 12-16%.
- A generic heuristic library: BBH +6 to +8 over CoT (d20).

**On data-driven discovery.** Best DiscoveryBench 25%, biology 0%. ScienceAgentBench best 32.4%; 42.2% with o1-preview at over 10x cost. DiscoveryWorld best 38% easy, 18% challenge, against human 0.66 completion.

**On ideas and papers.** Ideas look better than humans' before running (5.64 vs 4.84) and worse after (-1.05, -1.76, -1.88 vs about 0; N=43). AI Scientist costs under $15 per paper, but 5 of 12 experiments failed, and its reviewer is at 70% vs 73% human accuracy, AUC 0.65. AI Scientist-v2: 1 of 3 papers at acceptance level.

**On experiment design and revision.** Poor. BoxingGym: models struggle to choose informative experiments. Belief updating across rounds is weak without training. WorldCoder-style code revision on exact counterexamples works.

**Caveats on almost every number.** The strong numbers come from the authors, one model family each, on tasks with a hard numeric checker. Symbolic accuracy in LLM-SRBench is judged by GPT-4o. Samples are small: 100 ARC tasks on one model, 15 co-scientist goals, 3 papers, 41 synthetic equations.

## 7. What our agent should take

### Add now (established)

1. **Score the form, not only the fit.** Log form-correct and fit-correct separately; check held-out and out-of-domain points, and one noisy case. Schema: G3, S4. [E] K08, K26. Evidence a15, b25, c05, c06, d03.
2. **Revise from real output, not self-critique.** Tokens go to running code and reading its output. Schema: G2, S5. [E] K12. Evidence a17, b07, c16, c17, c28. Adds an independent source to what G2 already says.
3. **Do not trust a soft checker.** A learned or self-judge checker plateaus (about 41% selection while coverage is 98%) and stronger search exploits it. Keep checks hard; where none exists, mark the output unverified. Schema: G5, S0. [E] K26. Evidence d03, d04, d05.
4. **Model judges do not select ideas.** Confirms G8. Schema: G8. [E] K18, K29. Evidence b13, b14, b22, c22, c23, d13.
5. **Evaluate on disguised or transformed items with a no-data arm.** Schema: bench design, G7. [E] K09. Evidence a13, a15, a16, b06, b21, c03-c05.
6. **Final audit: re-check every reported number against logged tool output.** Schema: S8, G10. [E] K19. Evidence a18, a19, b10-b12, c13, c14.
7. **Spend model calls on proposals; let code fit, score and rank.** Schema: section 1 (program vs model), G5. [E] K10. Evidence a13, a14, b05, c01, c02, c24.
8. **With a hard checker, revise the best candidate with detailed feedback rather than drawing many fresh ones.** Schema: S5. [E] K28. Evidence d09, d10. Apply only where the class already has some success (G12).
9. **Do not read rediscovery as discovery.** Schema: bench, G7. [E] K02. Evidence a02, a03, a05, a10.
10. **Keep the BACON pattern (heuristics fired by data signals) as the design model for S6.** Schema: G1, S6, O library. [E] K01 for sufficiency only; the operator table itself is a Test-first item.

### Test first (single-source or contested)

| # | Idea | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Signal-to-operator table (constant: state law; monotone: ratio or product; irrelevant: stop varying) vs free reasoning at equal tokens | O library, S2 | [S] design from K01; no direct test | a01, a03, a05, d20 |
| T2 | Surprise trigger: open an explain-the-anomaly subgoal when a prediction fails, vs re-sample | S6 | [S] K05, abstract only | a09, a27, d17 |
| T3 | Force a revision on the exact failing cases | S5, S6 | [S] K31 | d18, d19 |
| T4 | Hypothesis-first only on retry | S3 | [S] K22, K27 | a21, d07, d08 |
| T5 | Cheap-first operator ladder vs random order | S6 order | [S] K06 (symbolic regression only) | a11, a12, b01, b02 |
| T6 | Early irrelevance probe (vary one variable at a time) | S2 | [S] K03 | a04 |
| T7 | Reuse a solved sibling's relation | O7, memory (subgoal library) | [S] K04 | a05 |
| T8 | Cost-aware choice of the next check | S4, S7 | [S] K30 | d14, d15, d16 |
| T9 | Minimum N distinct probes before the first fit | S4 guard | [S] K32 | d02, d03 |
| T10 | Reject candidates that contradict stated background facts | S4 | [S] K24 | b16 |
| T11 | Call the model only at stuck points | S6, G11 | [S] K11 | c07, c08, c09 |
| T12 | Score completion and explanation separately | bench metric | [S] K15 | c18, c19 |
| T13 | Mid-run contradicting observation: measure revision (open problem is [E]; the fix is [S]) | S5, S9, memory | [S] K25, K31 | a08, d18, d19 |
| T14 | Small-model retention of population-search gains | budget | [C] K33 | d10, d11, d12, c11 |

## 8. Concrete tests on our bench

All arms get the same token cap. Report accuracy per token. Use disguised or fresh items. Include a plain-model arm.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Freshly disguised law-finding tasks (NewtonBench-style), noise 0 and 0.0001 | A free reasoning; B signal-to-operator table; C table with randomised operators (control) | exact-form accuracy; held-out and OOD error | B above A by 3 to 8 points; C no better than A. If C equals B, any structure helps, the signals do not. |
| B2 (T2) | Tasks with a planted surprise (rule changes after the 3rd example) | A re-sample; B forced explain-the-anomaly subgoal | fraction revised correctly; tokens to correct | B above A by about 8 to 10 points; smaller than B3's gain. |
| B3 (T3, T13) | Accepted law, then a contradicting data point mid-run | A free; B exact failing cases fed back with forced revision; C same tokens as self-critique | revision rate; final accuracy | B above C by 10 points or more; C about equal to A. |
| B4 (T4) | Fresh ARC-like items | A direct; B programs only; C hypothesis-then-program always; D hypothesis only on retry | accuracy; tokens | D matches C at lower tokens; C and D beat B on hard items only. |
| B5 (T5) | Items with cost-labelled operators | A cheap-first; B random order; C costly-first | solved per token | A uses 10% or more fewer tokens than B at equal accuracy. |
| B6 (K28) | Items with a hard code checker | A 32 fresh samples; B 2 rounds x 16 revise-best with feedback text | accuracy | B above A, as in Eureka. |
| B7 (T8) | Items with unequal check cost | A cost-aware; B cheapest-first; C random | tokens to first failing case | A uses about half the tokens of C. |
| B8 (K26) | Same loop with strong checker, noisy checker, self-judge | three arms plus plain | gain over plain per arm | Gain shrinks under noise and vanishes under self-judge. Sets the G5 and S0 limit. |
| B9 (T9) | Interactive law tasks | A free tool use; B at least 5 distinct probes before first fit | accuracy by model strength | B above A for the strong model; no change for the weak. |
| B10 (T11) | Long symbolic tasks | A model on every step; B model at stuck points only | accuracy at equal tokens | B equal or above A. |

## 9. What does not transfer, and why

- **BACON on its own.** Needs numeric columns, programmer-chosen variables and hand-prepared data. Our items are mostly text and reasoning, so only the pattern "signal fires heuristic" carries over.
- **Hard numeric checkers.** LLM-SR, LaSR, AlphaEvolve and Eureka all have an exact score. Open reasoning tasks do not. Without one, selection plateaus (d04).
- **Robot scientists.** Their value is the physical experiment. Our agent cannot run a lab. Design analogy only (K23).
- **AI Scientist and co-scientist results.** Self-graded or model-judged. Not evidence of ability (K20, K21).
- **Population search at 10^6 samples.** FunSearch scale exceeds our token budget. Small-model retention is unmeasured (K33).
- **Famous-case rediscovery.** Shows recitation as much as discovery.
- **Self-reported benchmark tops.** AI Feynman 100/100 vs 38/100 (K07).
- **Idea novelty before execution.** Reverses after execution (b14).

## 10. Open questions

1. Does a short signal-to-operator table beat free reasoning at equal tokens on fresh disguised tasks? No direct test.
2. What does KEKADA's surprise rule do in detail? Heuristic list unread.
3. How much of the LLM-SR or LaSR gain survives a weak or absent checker? Only indirect evidence (d03-d05).
4. Best number of hypotheses per budget across styles (64 candidates, sparse calls, 16 x 5)? No equal-token comparison.
5. Do cheap-first ladders beat random order in an LLM agent? Only symbolic regression measured.
6. Active vs random experiment choice in robot scientists, with exact numbers? King 2004 pairing unconfirmed; Adam 2009 unread.
7. On-line revision of an accepted law after contradiction in LLM agents? Nearest: WorldCoder.
8. Do small open models keep population-search gains at equal tokens?
9. Does model-judge Elo predict external truth? Only partly answered.
10. Adam gene count: 6 or 12?

## 11. Sources

[V] opened, [M] snippet or secondary only.

- [V] Langley (1977) BACON, IJCAI-77. https://www.ijcai.org/Proceedings/77-1/Papers/057.pdf (a01, a02)
- [V] Langley (1979) Rediscovering physics with BACON.3. http://www.isle.org/~langley/papers/bacon.ijcai79.pdf (a03, a04)
- [V] Langley, Bradshaw, Simon (1981) BACON.5. https://www.ijcai.org/Proceedings/81-1/Papers/025.pdf (a05)
- [M] Langley (1981) BACON.4 (b20), no URL recorded
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery. https://mitpress.mit.edu/9780262620529/ (a28, c26)
- [V, abstract only] Kulkarni and Simon (1988) KEKADA. https://doi.org/10.1207/s15516709cog1202_1 (d17); [M] https://doi.org/10.1207/s15516709cog1202_4 (a27)
- [V] Dzeroski, Langley, Todorovski (2007) Computational discovery of scientific knowledge. http://www.isle.org/~langley/papers/discovery.comm07.pdf (a10)
- [V] Kramer, Langley et al. (2023) From equation discovery to autonomous discovery. https://arxiv.org/abs/2305.02251 (a06, a07)
- [V] Langley (2024) Integrated systems for computational scientific discovery. http://www.isle.org/~langley/papers/discovery.aaai24.pdf (a08, a09)
- [V] Udrescu and Tegmark (2020) AI Feynman. https://arxiv.org/abs/1905.11481 (a11, a12, b01)
- [V] Udrescu et al. (2020) AI Feynman 2.0. https://arxiv.org/abs/2006.10782 (b02)
- [V] La Cava et al. (2021) SRBench. https://arxiv.org/abs/2107.14351 (b03)
- [V] Cranmer (2023) PySR. https://arxiv.org/abs/2305.01582 (b04; garbled cells, not used in claims)
- [V] Cornelio et al. (2023) AI-Descarte (b16; no URL recorded)
- [V] Shojaee et al. (2025) LLM-SR. https://arxiv.org/abs/2404.18400 (a13, a14, b05, c01-c03)
- [V] Shojaee et al. (2025) LLM-SRBench. https://arxiv.org/abs/2504.10415 (a15, a16, b06, b21, c04-c06)
- [V] Grayeli et al. (2024) LaSR. https://arxiv.org/abs/2409.09359 (c07-c09)
- [V] Ma et al. (2024) LLM and simulation as bilevel optimizers. https://arxiv.org/abs/2405.09783 (c24)
- [V] Majumder et al. (2024) DiscoveryBench. https://arxiv.org/abs/2407.01725 (a17, b07, c16, c17, d01)
- [V] Chen et al. (2024) ScienceAgentBench. https://arxiv.org/abs/2410.05080 (b08, b24)
- [V] Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769 (c18, c19)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 (c20, c21)
- [V] Zheng et al. (2026) NewtonBench. https://arxiv.org/abs/2510.07172 (d02, d03)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660 (a21, d07, d08)
- [V] Tang, Key, Ellis (2024) WorldCoder. https://arxiv.org/abs/2402.12275 (d19)
- [V] Qiu et al. (2026) Bayesian teaching. https://arxiv.org/abs/2503.17523 (d18)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (d20)
- [V] Romera-Paredes et al. (2024) FunSearch. https://pmc.ncbi.nlm.nih.gov/articles/PMC10794145/ (d12); [M] https://www.nature.com/articles/s41586-023-06924-6 (c12)
- [V] Novikov et al. (2025) AlphaEvolve. https://arxiv.org/abs/2506.13131 (b09, c10, c11, d11)
- [V] Ma et al. (2024) Eureka. https://arxiv.org/abs/2310.12931 (c25, d09)
- [V] Lange, Imajuku, Cetin (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349 (d10)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d04)
- [V] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314 (d05)
- [V] Wu et al. (2025) Inference scaling laws. https://arxiv.org/abs/2408.00724 (d06)
- [V] Lu et al. (2024) The AI Scientist. https://arxiv.org/abs/2408.06292 (a18, a19, b10, c13, c14)
- [V] Yamada et al. (2025) AI Scientist-v2. https://arxiv.org/abs/2504.08066 (b15, c15)
- [V] Beel et al. (2025) Evaluating Sakana's AI Scientist. https://arxiv.org/abs/2502.14297 (b11)
- [V] Luo, Kasirzadeh, Shah (2025) Hidden pitfalls of AI scientist systems. https://arxiv.org/abs/2509.08713 (b12, b23)
- [V] Gottweis et al. (2025) AI co-scientist. https://arxiv.org/abs/2502.18864 (a20)
- [V] Si, Hashimoto, Yang (2024) Can LLMs generate novel research ideas. https://arxiv.org/abs/2409.04109 (b13, b22, c22, c23)
- [V] Si, Hashimoto, Yang (2025) Ideation-execution gap. https://arxiv.org/abs/2506.20803 (b14)
- [V] Wen et al. (2025) Predicting empirical AI research outcomes. https://arxiv.org/abs/2506.00794 (d13)
- [M] King et al. (2004) Nature. https://doi.org/10.1038/nature02236 (a26); [V, abstract] https://europepmc.org/article/MED/14724639 (d14)
- [M] King et al. (2009) The automation of science. https://doi.org/10.1126/science.1165620 (a25, b18, c27)
- [V] Sparkes et al. (2010) Towards robot scientists. https://pmc.ncbi.nlm.nih.gov/articles/PMC2813846/ (d16)
- [V] Williams et al. (2015) Eve drug repositioning. https://pmc.ncbi.nlm.nih.gov/articles/PMC4345494/ (a22, a23, d15); [M] b19
- [V] Bjurstrom et al. (2026) YGR067C with robot scientist. https://europepmc.org/article/PMC/PMC13043775 (a24, b17)
