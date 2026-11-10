# Scientific discovery systems: deep document

*Subfield C04.10. Focus: automated hypothesis generation, from BACON (Langley, 1979 to 1987) to LLM research agents (2024 to 2026). Evidence ids (a01 to d22) point to evidence_a to evidence_d.jsonl in this folder. Claim ids (C04.10-Kxx) point to claims.jsonl. "Opened" means the page or PDF text was read in this run; BACON-era sources were mostly not opened and are marked so. Why it matters for our agent: open mode needs a generator and a running check, and this field is the longest record of what happens when the two are joined.*

## 1. What it is

Scientific discovery systems are programs that propose hypotheses, laws, equations or research ideas, test them against data or a scorer, and keep what survives. Three generations exist.

1. **Rule-based law finders (1979 to 1990s).** BACON and its relatives search a small space of terms (ratios, products, constants) in numeric tables. A fixed test, "is this term constant within error", decides. No model opinion is involved. (a01, a02, c01, c03, d01, d02)
2. **Symbolic and neural search for equations (2009 to 2024).** AI Feynman, PySR, genetic programming. Search plus structure tests (symmetry, separability, dimensions). (a04, a05, b05, b06)
3. **LLM-in-the-loop discovery (2023 to 2026).** An LLM proposes (equation skeletons, hypotheses, research ideas, program edits). Code fits, runs or scores. The best results are propose-then-check loops (LLM-SR, LaSR, AlphaEvolve, HypoGeniC). The worst results are LLMs asked to judge their own ideas, or end-to-end paper pipelines with no hard check. (a06, c05, c20, b08, b11, b18)

The shared shape is the same as our open mode: **generate widely, check by running, keep what passes**. The field's main lesson is where that shape breaks: when the check is a model's opinion, when the check can be gamed, or when the generator remembers the answer.

Task types that must be kept apart, because results do not carry between them:

| Task type | Example | Check available |
|---|---|---|
| Law or equation recovery from numbers | Feynman equations, LSR-Synth | fit error, exact structure match |
| Hypothesis from labelled data | HypoGeniC, HypoBench | accuracy on held-out examples |
| Research idea generation | Si et al., ResearchAgent | none until executed |
| Idea execution and paper writing | AI Scientist, Agent Laboratory | code runs, but results can be wrong silently |
| Open-ended discovery in an environment | DiscoveryWorld, Kosmos | rubric, expert audit |
| Search for constructions with a scorer | AlphaEvolve | programmatic score |

## 2. History and theories in depth

**Theoretical frame (Simon, Langley and colleagues).** Discovery is ordinary problem solving: heuristic search through a space of hypotheses (or of experiments), with a test and pruning rules. This is the claim of the 1987 book *Scientific Discovery* (Langley, Simon, Bradshaw, Zytkow). A later encyclopedia review restates it: most discovery programs are recursive search over expressions, a test of fit, and heuristics to prune. (a02, c03; the book itself not opened)

**BACON.** BACON.1 to BACON.3 (Langley 1979, 1981) look for constants and for linear, ratio and product relations. If two terms rise together, test their ratio. If one rises while the other falls, test their product. The new term becomes a variable and the loop repeats. BACON.3 is credited with rediscovering the ideal gas law, Kepler's third law, Coulomb's law, Ohm's law and Galileo's pendulum and constant-acceleration laws (6 laws; from search abstracts only). (a01, b02, c01, c02) The encyclopedia text gives the Kepler example: an INCREASING operator is applied to P/D and P^2/D, and P^2/D^3 comes out constant. (c03, opened)

**BACON.6 and noise (1984 technical report, opened).** The data are used only to test hypotheses, never to generate them. Each candidate parameter set is scored by correlation between observed and predicted values. Search starts from parameter values 1, 0, -1, keeps a beam of N best states, and stops when no state improves. Search effort is the same at any noise level, which is why it is robust to noise by design. The report gives no law counts or noise percentages, and the OCR text is partly garbled. (b01, d02)

**What BACON achieved, by an author's own account.** Simon (1995) says BACON re-created "a dozen or more" significant discoveries, from Kepler to Cannizzaro, from the same data the original scientist had. (d01, opened) The exact list is not verified.

**Human comparison.** Qin and Simon (1990): 14 subjects tried to find a law for planetary distance and period data. Their search heuristics resembled BACON's. Per Simon (1995), 4 of 14 found Kepler's third law. The abstract snippet seen in search words this differently, so the count rests on one secondary statement. (b03, d03, d01)

**Critiques of the BACON era.**
- The data were pre-selected and cleaned, so the hardest step (choosing which variables matter) was done by the human. (c01, a02)
- One paper argues the data BACON used does not match what Kepler and contemporaries had. (b04, snippet only)
- A philosophy-of-science critique says the evaluation rests on two case studies (sine law of refraction, Kepler III) and cannot show a general model of discovery. (c28, snippet only)
- Falkenhainer and Michalski's ABACUS (1986) extended BACON with applicability conditions for laws. Not opened. (a03)
- Later systems (GLAUBER, STAHL, DALTON) were built because BACON could not handle qualitative or structural discovery. (b01)

**Second generation: symbolic regression.** AI Feynman (Udrescu and Tegmark 2020) solved all 100 Feynman equations versus 71 for the best earlier public software, using neural-network tests for symmetry and separability to split the problem before search. (a04, a05, c04) AI Feynman 2.0 added noise robustness: 73 of 100 solved at noise level 10^-1, typically 1 to 3 orders of magnitude more robust than version 1. (b05)

**Third generation: LLMs.**
- 2023 to 2024: LLMs as hypothesis proposers from literature (Qi et al.; MOOSE; SciMON; ResearchAgent; Chain of Ideas). Mostly rated by model judges. (a21, a18, c15, c23, c24)
- 2024: LLM-SR puts the LLM inside an evolutionary equation search. The AI Scientist automates the whole paper pipeline. Si et al. run the first large blind expert study of LLM ideas. (a06, a09, a16)
- 2025: ideation-execution gap, plagiarism audits, independent tests of the AI Scientist, benchmarks built to block memorisation (LLM-SRBench), AlphaEvolve, co-scientist, Kosmos, PaperBench. (b10, b18, b22, a08, c20, b21, b24, b23)
- 2026: execution-grounded automated research and agentic equation discovery (SR-Scientist). (d07, d18)

**Competing theories of why discovery systems succeed.**
1. *Search power.* More search finds more laws. Contradicted by AI Feynman, where structure tests (not bigger search) gave the gain, and by LLM-SR, which beat baselines running 2M+ iterations with about 2.5K. (a05, a06)
2. *Prior knowledge.* The LLM already knows the equation. Supported by LLM-SRBench: scores drop sharply when equations are rewritten or invented. (a08, b13)
3. *Feedback loop.* A fit check shown back to the proposer is what matters. Supported by LLM-SR ablations and SR-Scientist ablations. (a07, d18)

All three are partly true. The loop carries most of the gain once memory is removed. Exact structure recovery stays low either way. (d19, d20)

## 3. Core findings with exact numbers

Status key: established = two or more independent sources (claims.jsonl); single = one study; contested = sources disagree.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| BACON re-created many historical laws from clean tables | "a dozen or more" (Simon 1995); 6 laws named for BACON.3 | Simon 1995 (d01); Langley 1979 (c01, M) | contested (original not opened; clean data) |
| Humans on Kepler task | 4 of 14 college students found the law | Qin and Simon 1990 via d01 (d03, M) | single, secondary |
| AI Feynman beats prior software on Feynman set | 100/100 vs 71/100 | Udrescu and Tegmark 2020 (a04, c04) | single (same group in both papers) |
| AI Feynman 2.0 under noise | 73/100 at noise 10^-1 | b05 | single |
| AI Feynman is brittle in an independent test | exact recovery 53% at noise 0 (next, GP-GOMEA, 27%); above noise 0.01 DSR, gplearn and AFP recover more | La Cava et al. 2021, 14 methods, 252 problems, 10 trials (b06) | contested |
| LLM inside the evolutionary loop beats search alone | LLM-SR about 2.5K iterations beat baselines with 2M+; LaSR exact solves 66 to 72 of 100 vs PySR 59 (abstract 66; table 67 / 69 / 71 / 72 by LLM-operation rate and model) | a06, c05, c06, a07 | established |
| LLM-SR OOD advantage on one system | OOD NMSE 0.0037 vs above 1 for others (E. coli growth) | a06, c06 | single |
| Loop ablation | no iterative refinement: NMSE 0.101 in-domain, 0.181 OOD; no skeleton plus optimizer: 0.378 / 0.375 | a07 | single |
| Memorisation inflates scores | best symbolic accuracy 31.5% (LSR-Transform), 28.1% (LSR-Synth); 239 problems | LLM-SRBench (a08, b13, c07) | single |
| Loop beats bare prompting even off memory | LLM-SR SA 31.53 vs direct prompt 7.21 on LSR-Transform; chemistry LSR-Synth 11.11 vs 0.0 | b13, d19 | single |
| LaSR on 41 synthetic equations | held-out R2 0.913 vs PySR 0.070; no true forms recovered | d20 | single |
| Data tool matters most in agentic regression | Acc0.01 63.57 full vs 35.66 without data tool; 57.36 without experience buffer | SR-Scientist (d18) | single |
| Fit is not law | R2 above 0.9999 on orbits but inconsistent implied force laws | Vafa et al. 2025 (c26) | single |
| Novelty at ideation: AI above human | human 4.84, AI 5.64, AI+human rerank 5.81; 49 ideas per arm; 79 reviewers; 298 reviews; feasibility 6.53 / 6.30 / 6.41 (ns) | Si et al. 2024 (a16, b09, c13) | single (three lines, one study) |
| Gap flips after execution | overall human 4.596 to 3.968 (-0.628), AI 5.382 to 3.406 (-1.976); novelty human 4.912 to 4.903, AI 5.778 to 4.729; 43 experts, over 100 hours each | Si et al. 2025 (b10, c14, c27) | single |
| Idea diversity wall | about 200 non-duplicates of 4000 seeds (cosine above 0.8) | a17, b12 | single |
| LLM judges near chance on ideas | direct 50.0 / 51.7, pairwise 45.0 / 53.3, AI Scientist reviewer 43.3; human agreement 56.1% | a17, b11 | single |
| Off-the-shelf judges near chance on outcomes | GPT-4.1 51.9%; o3 no better than random; expert majority 48.9%; best annotator 60.0%; fine-tuned GPT-4.1 plus retrieval 77%; 1,585 test pairs | Wen et al. 2025 (d09, d10) | single |
| Validation shown to judge lifts ranking | Claude 69.0 to 78.9; Gemini 56.9 to 62.3; human test: feasibility p=0.03, effectiveness p=0.02, overall p=0.29 | Liu et al. 2025 (d04 to d06) | single (social science, 8 papers) |
| Execution feedback in the loop | execution rate 42 to 78%; best-of-50 60.4% vs 48.0%; evolution 69.4%; RL collapsed to few simple ideas | Si et al. 2026 (d07, d08) | single |
| End-to-end pipelines are fragile | 5 of 12 experiments failed (42%); 4 of 7 papers missing figures; 4 of 7 wrong or invented numbers; 5 of 34 citations from 2020+; $6 to 15 per paper | Beel et al. 2025 (b18, c11), plus Lu et al. (a12) and Luo et al. (d14) | established |
| Silent process failures | 82.4% of 945 benchmark picks were among first four listed; auditor with paper only 55% vs 82% with logs and code | Luo et al. 2025 (d14, d15) | single |
| Automated novelty checks are too generous | 49 of 51 ideas flagged novel (Sonnet 3.5); 24% of 50 documents plagiarised; detectors Turnitin 0%, OpenScholar 0%, parametric-only 1.3%, oracle retrieval 88.8 / 89.0% | a13, b22, c19 | established |
| Staged retrieval novelty check | 89.66% on known not-novel ideas; keyword only 5.17%; snippet only 8.62%; embedding only 10.34%; without facet rerank 13.79%; 58 ideas. Co-scientist reflection with search 2.38 vs 6.14 without | d11, d12 | single (two systems) |
| Open-ended discovery agents lag humans | DiscoveryWorld best agent 38% easy, 18% challenge vs humans 66%; DiscoveryBench 25%; ScienceAgentBench 32.4% (42.2% with o1 at over 10x cost) | a22, b15, a24 | established |
| Hypothesis bank from data | +31.7 / +13.9 / +3.3 / +24.9% over few-shot on four datasets; beat supervised by 12.1 and 11.6% on two hard sets; bank updates add 0.7 / 5.8 / 8.1 / 7% | HypoGeniC (b08, c16) | single |
| Hypothesis recovery collapses with difficulty | best discovery rate 93.8% base, 38.8% harder; 194 datasets | HypoBench (d22) | single |
| Interpretation is the weak step | Kosmos: 79.4% overall of 102 statements; 85.5% data analysis; 82.1% literature; 57.9% synthesis | b24, c21 | single |
| Closed-loop evolution with evaluator | AlphaEvolve matched best known on 75% and surpassed on 20% of 50+ problems; kissing number in 11 dimensions to 593; tensor targets 38 matched, 14 surpassed, 2 behind of 54 | c20 | single |
| Evaluators get gamed | loopholes in leaky verifiers; evolved program coaxed a cheap LLM oracle into leaking the hidden function; mixed cheap and strong models sometimes beat strong-only | Georgiev et al. 2025 (d16, d17) | single |
| Retrieval of inspirations degrades at fine selection | hit ratio 96.4% at top 20% falls to 46.7 to 52.0% at top 0.016%; screening rounds 98.0% to 56.5% | MOOSE-Chem (a19) | single |
| Paper replication from scratch | best agent 21.0% (SE 0.8); human PhDs 41.4% vs o1 26.6% on 3 papers | PaperBench (b23, c25) | single |
| AI reviewer vs human | balanced accuracy 0.65 vs 0.66; false positive 0.31 vs 0.17; false negative 0.39 vs 0.52 | AI Scientist (a10, b19) | single |
| Few-shot examples lower novelty | GPT-3.5 novelty 1.42 zero-shot vs 1.02 five-shot similar examples | Qi et al. 2023 (a21) | single |
| Iteratively rewriting for novelty | gain on 56% of updated ideas (round 1), 57.8% (round 2); real paper idea still judged better 85% of the time | SciMON (c15) | single |

## 4. Mechanisms and models

### 4.1 BACON term search (implementable in about 50 lines)

```
state = table of variables (columns)
loop:
  for each pair/group of columns where one varies and another is held fixed:
    if column is constant within tolerance: record law "col = c"; stop
    if two columns rise together:   add column  a/b
    if one rises while other falls: add column  a*b
    (rule from c02; INCREASING / DECREASING operators from c03)
  new columns become variables; repeat to depth limit
```

Key property: the data only test. The test (constant within tolerance, or correlation between observed and predicted) is code. A noisy table raises the tolerance, not the search effort. (b01, d02) Limit: the variable list is supplied. The agent equivalent is the human step of choosing what to measure, which BACON never did.

### 4.2 Structure tests before search (AI Feynman)

Before searching, test cheap structure: low-order polynomial fit, translational and rotational symmetry, separability (f(a,b) = g(a)+h(b) or g(a)h(b)), dimensional analysis. When a test passes, split the problem into smaller ones. The gain came from these tests, not from larger search. (a05) Agent form: O3 decompose and O6 change representation, with a code test for each structure.

### 4.3 Propose, fit, feed back (LLM-SR, LaSR, SR-Scientist)

```
buffer = []                       # best programs so far, with scores
repeat K times:
  prompt = problem text + top-k programs from buffer (+ their scores)
  skeleton = LLM(prompt)          # code with free constants, no numbers
  params = optimizer.fit(skeleton, data)     # code, not the LLM
  score = error(skeleton, params, data)      # code
  buffer.add(skeleton, score)
return best of buffer, tested on held-out/OOD slice
```

Three parts do the work: the problem description in words (dropping it hurt), the constants fitted by an optimizer rather than written by the LLM (letting the LLM write constants hurt), and the iterative feedback (dropping it hurt most). (a07) SR-Scientist adds a data-analysis tool and an experience buffer; removing the tool cost the most (63.57 to 35.66 Acc0.01). (d18) LaSR adds a library of natural-language concepts that the LLM proposes and evolves; p is the share of LLM-driven operations, and 1% already gave 67 solves. (c05)

### 4.4 Hypothesis bank with reward (HypoGeniC)

Generate hypotheses from a few examples. Score each by how often it predicts new examples correctly. Use an upper-confidence-bound reward so rarely tried hypotheses still get tested. Keep a bank. Replace the weak with new ones generated from the examples the bank gets wrong. Classification then uses the bank. (b08, c16) The update step is the part that is "a running check": it adds a few points on average.

### 4.5 Retrieve inspirations, compose, rank (MOOSE-Chem, SciMON)

Split discovery into: retrieve inspirations from a literature pool, compose a hypothesis from background plus inspiration, rank. Retrieval works at coarse selection (96% hit at top 20%) and degrades at fine selection. (a19, a20) SciMON retrieves inspirations and rewrites an idea until it is not too similar to related work. (c15)

### 4.6 Evolve with a hard evaluator (AlphaEvolve)

LLM proposes program edits. Automatic evaluators score them. A database keeps the best and samples parents. Works when the score is smooth and machine-checkable. Needs the evaluator sealed from the generator. (c20, d16, d17)

### 4.7 Execution-grounded ranking

Run a cheap data-based test per idea, then show the result to the judge (Liu et al.), or run the full code (Si et al. 2026). Ranking accuracy rises where the test measures the thing in question (feasibility rose most: Claude 20.1 to 46.9). It does not move novelty much. (d05, d07)

### 4.8 Staged novelty check

Retrieve with a query built from the idea's facets, rerank by facet, then compare. The single-stage variants found 5 to 14% of known non-novel ideas. The staged pipeline found 89.66%. (d12) Self-consistency was the best prompting baseline for novelty ranking on 15,000 arXiv pairs; retrieval-augmented novelty was best overall; multi-LLM discussion fell below zero-shot. (d13, numbers not extracted)

### 4.9 Trace audit

An auditor that reads the run log and code finds 82% of process failures; reading only the final paper finds 55%. (d15) Implementation: log every dataset choice, subsample, seed and deviation; let the verify state read the log.

## 5. What holds up

**Holds up (two or more independent sources).**
- Proposing with an LLM and fitting or scoring with code works better than either alone (LLM-SR, LaSR, SR-Scientist; AlphaEvolve; HypoGeniC). Different teams, different tasks. (a06, c05, d18, c20, b08) Also: replacing the symbolic interpreter with the LM itself cut MiniSCAN accuracy from over 80% to almost zero. (b07)
- End-to-end paper pipelines without hard checks produce plausible but unreliable output. Beel et al. (independent) found 42% failed experiments and invented numbers; Luo et al. (independent of both) found silent choices. (b18, d14)
- Automated novelty checks are too generous. AI Scientist flagged 49 of 51 ideas novel; experts found 24% plagiarism; staged retrieval fixes most of it in one test. (a13, b22, d12)
- Open-ended discovery agents are far below humans: DiscoveryWorld, DiscoveryBench, ScienceAgentBench. (a22, b15, a24)

**Failures and contradictions.**
- AI Feynman wins its own papers (100/100) but gets 53% exact recovery at zero noise in an independent benchmark and is beaten above noise 0.01. Benchmark and noise level decide the winner. (b06)
- LLM-SR looks strong on famous equations; LLM-SRBench shows under 32% symbolic accuracy once memory is blocked. (a26)
- Si et al. 2024 (AI ideas better) and 2025 (AI ideas worse after execution) come from the same group. The flip is the result. No independent replication of either was found. (b10, critique.md)
- LaSR reports 66 in the abstract and up to 72 in the table; use "66 to 72 vs 59" and name the setting. (critique.md)
- BACON's record rests on author accounts, pre-selected data and two case studies. (c28, b04)

**Moderators.**
- *Evaluator type.* Hard computed check (fit, score, tests) works. Model opinion does not (judge accuracy 43 to 53%). (b11, d09)
- *Evaluator quality.* Leaky or noisy evaluators are gamed. (d16)
- *Memory.* On known equations part of the gain is recall. (a08)
- *Noise.* Exact-recovery winners change with noise level. (b06)
- *Domain.* DiscoveryBench: economics 25%, sociology 23%, engineering 7%, biology 0%. (b15)
- *Model.* A verify-then-continue scaffold raised o1 on PaperBench (to 43.4% on one variant) but hurt Claude 3.5 Sonnet. (b23)
- *Statement type.* Kosmos computed statements 85.5% accurate vs 57.9% for interpretation. (b24)

**Interventions that worked.** Fit-and-feed-back loop; data-analysis tool; experience buffer; validation shown to judge (feasibility and effectiveness only); staged retrieval for novelty; logs for auditing; evolutionary search with execution reward (69.4% vs 48.0% baseline); extra Elo tournament compute in co-scientist (self-scored). (a07, d18, d05, d12, d15, d07, b21)

**Interventions that did not work.**
- Few-shot examples for novelty (1.42 to 1.02). (a21)
- Ensembling the AI reviewer (no accuracy gain, lower variance); Reflexion and one-shot added about 2 points. (a10)
- Majority vote over more samples for induction; iterative refinement can overfit. (b07)
- Reasoning prompts (ReAct, planner plus critic) did not beat plain code generation in DiscoveryBench; oracle feedback did help. (b15)
- RL on execution reward collapsed onto a few simple ideas; longer thinking correlated with lower execution rate. (d08)
- Sampling more ideas: 4000 seeds gave about 200 distinct. (b12)
- Self-augmented chain of thought for outcome prediction: no gain. (d09)
- Multi-LLM discussion for novelty: below zero-shot. (d13)
- Extra screening rounds in inspiration retrieval: recall 98.0% to 56.5%. (a19)

## 6. Language models

**Generation is easy and cheap.** LLM ideas beat expert ideas on blind novelty at ideation (5.64 vs 4.84; rerank 5.81), with feasibility not significantly lower. (a16) A model cannot be made more novel by examples: five similar examples lowered novelty. (a21)

**But the ideas repeat.** About 5% of 4000 seeds were distinct. Ideas are similar across runs and models in the AI Scientist too. (b12, a12)

**Judging is near chance.** Judge accuracy 43.3 to 53.3% against human 56.1% (a17); outcome prediction 51.9% for GPT-4.1, o3 no better than random even with retrieval, experts 48.9% by majority. Moves above 60% needed training on 6,000 outcome pairs (77%) or a computed validation (Claude 69.0 to 78.9). (d09, d10, d05) The AI Scientist reviewer on accept/reject (0.65) is a different task and is over-optimistic (FPR 0.31 vs 0.17). (a10)

**Execution erases the advantage.** After human execution, AI overall dropped 1.976 vs 0.628 for human ideas, and novelty fell 1.049 vs 0.010. (b10) Execution by an automated executor works on code-checkable tasks (42 to 78% of ideas run). (d07)

**Recall masquerades as discovery.** Scores on Feynman equations fall when the form is changed or invented. Llama-3.1-8B error on plain Feynman problems dropped sharply, read as memorisation. (a08) Fitting is not understanding: R2 above 0.9999 with inconsistent force laws. (c26)

**Self-report is not checked.** Papers hid benchmark choices (82.4% by list position), subsampled data and invented numbers; paper-only audits catch 55%. (d14, d15) Kosmos interpretation 57.9% accurate. (b24)

**Novelty claims are inflated.** 49 of 51 flagged novel; 24% of documents plagiarised; with retrieval grounding the oracle detector reaches about 89%, without it 1.3%. (a13, b22)

**Scaffold effects depend on the model.** An iterative scaffold helped o1 and hurt Claude 3.5 Sonnet on PaperBench. (b23) Model mixing: cheap plus strong sometimes beat strong alone in AlphaEvolve. (d17) Claude 3.5 Sonnet with self-debug beat OpenHands on ScienceAgentBench by 10.8% at 17 times lower cost. (a24)

**Open-ended environment tasks.** Best agent 38% easy and 18% challenge on DiscoveryWorld; the Hypothesizer (keeps a list of hypotheses and tests them) had the best knowledge scores on easy tasks (0.34 vs ReAct 0.25) and not on challenge (0.08 vs 0.10). (a22, a23) Agents score 60%+ on unit-test sub-skills, so the failure is in the long loop. (c09)

**Caveats.** Many LLM-system claims (co-scientist, ResearchAgent, Chain of Ideas, Robin, AlphaEvolve) are self-scored. Most models tested are 2023 to 2025; Si et al. 2026 and Georgiev et al. use newer models but come from the same or related groups. (critique.md)

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md. Many of the established items confirm guardrails that are already in the schema (G3, G8, G10); that is a result too, because this field is an independent source for them.

### Add now (established)

| # | Take | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | In open mode, keep the model as proposer only. Fitting, scoring and selecting are done by code. Do not let the model replace the checker: swapping a symbolic interpreter for the LM itself cut accuracy from over 80% to almost zero. Constants in a proposed form are fitted by a tool, not written by the model. | S3 to S4, G5, G8 | [E] | a06, c05, d18, c20, b08, b07; K07 |
| A2 | Verify before claim. Every number in a final report must trace to a logged run, with the run's data and seed. Count unsupported numbers. Independent tests found 42% failed experiments, 4 of 7 papers with wrong or invented numbers, and silent choices. | S8 VERIFY, G10 | [E] for the need; the exact trace format is [S] | b18, c11, a12, d14; K10 |
| A3 | Novelty is checked against external sources by retrieval, never by the generating model. Self-checks flagged 49 of 51 ideas novel while 24% of documents were plagiarised; retrieval-less detectors score 0 to 1.3%. When retrieval is used it must be staged (query by facets, then rerank); single-stage retrieval finds only 5 to 14% of known non-novel ideas. | G8, S7 | [E] for retrieval; staged form [S] (one study, 58 ideas) | a13, b22, c19, d11, d12; K12 |
| A4 | Treat open-ended discovery as the weakest mode. Plan on far-below-human success and do not report an open-mode idea as "discovered" without a computed check. Agents reach 18 to 38% on DiscoveryWorld against humans' 66%. | S0 gate, S7 | [E] | a22, b15, a24; K13 |
| A5 | Keep a running check inside the loop and feed its output back to the proposer. Dropping iterative refinement is the largest single loss in LLM-SR ablations. (The ablation is single-source; the pattern of check-then-revise from real output is already G2.) | S5, G2 | [E] as pattern (G2); size [S] | a07, d18, b07 |

### Test first

| # | Take | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Run a cheap executed check on each candidate idea before ranking, and show the result to the selector. The ideation-execution gap (AI overall -1.976 vs human -0.628) suggests idea-stage scores mislead; a data-based validation raised ranking accuracy (Claude 69.0 to 78.9) but only on feasibility and effectiveness, not overall (p=0.29). | S4 before S7, G8 | [S] | b10, d05, d06, d07; K02, K23, K24 |
| T2 | Never let the model rank its own ideas alone. Judges are near 50% (43.3 to 53.3). Test whether a vote or a computed validation lifts ranking above 60%. | G5, G8 | [S] (two studies; ranking is near chance in both) | a17, b11, d09, d10, d05; K03 |
| T3 | Structure tests before search: split by symmetry, separability, dimensions or an invariance, with a code test for each. | O3, O6 | [S] (one group, clean data; contested under noise) | a04, a05, b05, b06; K05, K06 |
| T4 | Altered-variant control: test the agent on rewritten or synthetic versions of known problems, to separate recall from reasoning. | G (recall is not discovery) | [S] | a08, b13, d19, d20; K08 |
| T5 | Check a proposed law or rule on a shifted slice, not on the fit set. | G3 | [S] | c26, a07, d20; K09 |
| T6 | Tag each final statement as observed, computed or interpreted, and send interpreted ones to a second check. Kosmos: 85.5 / 82.1 / 57.9%. | S8, G10 | [S] | b24, c21; K11 |
| T7 | Hypothesis bank with a reward update on failures, for open tasks that have a labelled or checkable stream. | memory, O (new) | [S] | b08, c16, d22; K14 |
| T8 | Forced diversity: code keeps a history of directions and assigns untried ones; measure the duplicate rate against plain resampling at equal tokens. Sampling alone gives about 5% distinct ideas. | S3, O diverge | [S] | b12, a17, a25; K04 |
| T9 | Pair a check with a diversity term so only distinct ideas that pass count. RL on a pass reward collapsed to a few simple ideas. | S3, S7 | [S] | d08, d07; K24 |
| T10 | Judge sealed from the generator: the generator never sees the judge prompt or raw output; restrict judge output to a verdict. | G8 (extension) | [S] | d16, d17; K26 |
| T11 | Trace log read by the verify step: dataset choice, subsampling, seeds, stated deviations. Paper-only audit 55% vs 82% with logs and code. | S8, section 6 logs | [S] | d14, d15; K27 |
| T12 | Staged filtering for retrieval of analogues or literature: coarse top-k, then rerank, not repeated screening. | O7, memory | [S] | a19, d12; K16, K25 |
| T13 | Scaffold effect check per model: a verify-then-continue loop helped one model and hurt another. Test per model. | G7 | [S] | b23; K18 |
| T14 | Evolve-with-evaluator loop in place of best-of-n on tasks with a programmatic scorer. | S3 to S5 | [S] | c20, d07; K22 |
| T15 | Calibrate the self-review accept threshold on known outcomes; LLM reviewers are over-optimistic (FPR 0.31 vs 0.17). | G (calibrated self-review) | [S] | a10, b19; K20 |

**What not to add (matches SCHEMA.md 4b).** Debate or multi-LLM discussion for novelty (below zero-shot, d13). Few-shot examples to raise novelty (a21). Reasoning prompts without a check (b15). Ensembling a model reviewer for accuracy (a10).

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup and judge calls counted). Report per-axis, not only overall. Run at least 3 seeds and report the spread. Item sets are built from our own bench types plus small discovery-style tasks.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| 1 | Open-mode idea items (NoveltyBench style, 50 prompts) plus a small executable check (code or data test per idea) | (a) rank by model judge; (b) run cheap executed check, then rank; (c) check plus model judge | rate at which top-5 picks pass a held-out executed test; and human-blind feasibility and effectiveness win rate | (b) beats (a) by about 10 points on pass rate; no gain on blind novelty (d05, d06) |
| 2 | Same items | self-judge ranking vs random vs vote of 5 isolated judgments vs computed validation | ranking accuracy against executed outcome | self-judge and vote within 5 points of chance (50%); computed validation 60% or more (d09, d05) |
| 3 | Equation or rule recovery tasks (synthetic equations with fresh forms, 30 items, noise 0 and 5%) | (a) one-shot proposals; (b) propose, fit by tool, feed error back; (c) (b) minus feedback | exact-structure rate and held-out R2 on a shifted slice | (b) greater than (a) on R2 by a wide margin; exact structure stays low (under 35%); (c) between (a) and (b) (a07, d19) |
| 4 | Famous vs altered versions of the same 30 laws (original, rewritten form, invented) | one scaffold, same budget | drop in exact-solve rate original to altered | a drop of at least 20 points shows recall; scaffold should shrink the drop (a08) |
| 5 | Same 30 laws | structure tests (separability, symmetry, dimensions) before search vs search only | exact solve rate at noise 0 and 5% | gain at noise 0; may vanish at 5% (b06) |
| 6 | Novelty claims: 50 agent ideas with known prior work seeded in (10 known) | self-judge vs one-query retrieval vs staged retrieval | false "novel" rate on seeded known ideas; tokens | self-judge over 90% false novel; one-query under 20% caught; staged over 70% caught (d12) |
| 7 | Report tasks (agent runs analyses and writes a result) | verify step reads paper only vs reads trace log and code | unsupported or invented numbers caught of seeded faults | log arm catches about 25 points more (d15) |
| 8 | Report statements from item 7 | no tagging vs tag observed / computed / interpreted with second check on interpreted | accuracy per tag; final report error rate | interpreted statements the weakest (about 20 points under computed); second check lifts them (b24) |
| 9 | Diversity: 20 open prompts, n parallel drafts each | plain resampling vs history-forced untried directions | embedding-distinct fraction (cosine 0.8) and share passing check | distinct fraction well above 5%; pass share not lower (b12) |
| 10 | Evolve loop on 10 tasks with a programmatic scorer | best-of-n vs evolve with sealed scorer vs evolve with leaky scorer | best score; rate of scorer exploitation | evolve above best-of-n; leaky scorer shows exploitation (c20, d16) |
| 11 | Labelled hypothesis tasks (10 small classification or rule tasks) | few-shot vs bank with reward updates | held-out accuracy | bank gains 3 to 30 points depending on task (b08) |
| 12 | Model dependence | each of items 1, 3 and 7 on 2 or more models | sign of the scaffold effect per model | sign may differ by model (b23) |

## 9. What does not transfer, and why

- **BACON and AI Feynman need numeric tables with named variables.** Our items usually have no table and no variable list. The human step (choose what to measure) is the hard part and BACON never did it. (c01, a02)
- **LLM-SR and LaSR need a numeric fit score.** Most of our open items have no numeric score. Where there is none, A1 degrades to "code-run test" only if a test can be written.
- **AlphaEvolve needs a smooth, machine-checkable, sealed score.** On tasks without one the system fails or is gamed. (d16)
- **Novelty by blind human rating (Si et al.) cost 79 reviewers.** We cannot run that on our bench; we substitute embedding distance and retrieval, which measure something narrower.
- **Execution of ideas by experts (100+ hours each)** cannot be matched. The cheap executed check is only a stand-in, and no study has shown that it recovers the gap. (b10)
- **Self-scored results (co-scientist, ResearchAgent, Chain of Ideas, Robin, AlphaEvolve) do not transfer as effect sizes.** Use direction only. (critique.md)
- **Social-science validation (Liu et al.) used 8 papers.** Small domain and sample. (d05)
- **Pipelines that write whole papers** are not our task; their failure modes (list-position benchmark choice, invented numbers) matter only for tasks where the agent reports analysis.
- **Hypothesis banks (HypoGeniC) need labelled streams.** Open-ended items have none. (d22)
- **Models in these studies are mostly 2023 to 2025.** Newer models may move every number.

## 10. Open questions

1. Does a cheap executed check before ranking close the ideation-execution gap, at equal tokens? No study compares arms at equal tokens. (critique.md, gap 1)
2. Has anyone outside the Si et al. group replicated the ideation or execution study, with 2025 to 2026 models? Not found.
3. What exactly did BACON-era systems achieve (law list, noise tolerance, the 4 of 14 human count), from the original papers? The 1987 book and the Qin and Simon paper were not opened.
4. How much of the LLM-SR and LaSR gain is the loop and how much is memory on non-famous problems? Partly answered: the loop carries most of it, exact structure stays low. Still no clean decomposition at equal tokens.
5. Can any ranker exceed 60% on idea quality without outcome training or a computed validation? Voting on idea quality was not tested.
6. Does retrieval-grounded novelty checking cut the 24% plagiarism rate, and at what token cost? Not measured.
7. Do evolve-with-evaluator loops work when the evaluator is noisy or not code? Direction known (gamed), rate unknown.
8. Which error types dominate in 2025 to 2026 discovery agents, and which guardrail removes the most? No cross-system tally.
9. Is the Kosmos gap (85.5% computed vs 57.9% interpreted) reproduced elsewhere? Not found.
10. Does a hypothesis bank transfer to open-ended unlabelled tasks? HypoBench uses labelled tasks only.
11. Does the finding that few-shot examples lower novelty (one GPT-3.5 test) hold for current models?
12. Do structure tests (AI Feynman) help LLM agents, and at what noise level do they stop helping?

## 11. Sources

[V] = opened and read this run; [M] = snippet or recall only. One line per URL; ids list the evidence lines that use it. Cross-reading lines (a25, a26, b25, c27, d21) are syntheses of the sources listed.

- [M] Langley (1981) Data-driven discovery of physical laws (BACON.1-BACON.3) (1981). https://doi.org/10.1207/s15516709cog0503_2 (ids: a01)
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery: Computational Explorations of the Creative Processes (1987). https://mitpress.mit.edu/9780262620529/ (ids: a02)
- [M] Falkenhainer and Michalski (1986) Integrating quantitative and qualitative discovery: the ABACUS system (1986). https://doi.org/10.1007/BF00116895 (ids: a03)
- [V] Udrescu and Tegmark (2020) AI Feynman: a physics-inspired method for symbolic regression (2020). https://arxiv.org/abs/1905.11481 (ids: a04, a05, c04)
- [V] Shojaee et al. (2024) LLM-SR: scientific equation discovery via programming with LLMs (2024). https://arxiv.org/abs/2404.18400 (ids: a06, a07, b14, c06)
- [V] Shojaee et al. (2025) LLM-SRBench (2025). https://arxiv.org/abs/2504.10415 (ids: a08, a26, b13, b25, c07, d19)
- [V] Lu et al. (2024) The AI Scientist (2024). https://arxiv.org/abs/2408.06292 (ids: a09, a10, a11, a12, a13, b19, c10)
- [V] Yamada et al. (2025) The AI Scientist-v2 (2025). https://arxiv.org/abs/2504.08066 (ids: a14, a15, b20, c12)
- [V] Si, Yang, Hashimoto (2024) Can LLMs generate novel research ideas? A large-scale human study (2024). https://arxiv.org/abs/2409.04109 (ids: a16, a17, a25, b09, b11, b12, c13)
- [V] Yang et al. (2024) Large language models for automated open-domain scientific hypotheses discovery (MOOSE) (2024). https://arxiv.org/abs/2309.02726 (ids: a18, c17)
- [V] Yang et al. (2025) MOOSE-Chem: rediscovering unseen chemistry hypotheses (2025). https://arxiv.org/abs/2410.07076 (ids: a19, a20)
- [V] Qi et al. (2023) Large language models are zero shot hypothesis proposers (2023). https://arxiv.org/abs/2311.05965 (ids: a21)
- [V] Jansen et al. (2024) DiscoveryWorld (2024). https://arxiv.org/abs/2406.06769 (ids: a22, a23, b17, c09)
- [V] Chen et al. (2024) ScienceAgentBench (2024). https://arxiv.org/abs/2410.05080 (ids: a24, b16)
- [V] Langley, Zytkow, Simon, Bradshaw (1984) The Search for Regularity: Four Aspects of Scientific Discovery (CMU-RI-TR-84-20) (1984). https://www.ri.cmu.edu/pub_files/pub3/langley_pat_1984_3/langley_pat_1984_3.pdf (ids: b01, d02)
- [M] Langley (1979/1981) BACON.3 rediscovery of physical laws; summary via search results (mlanthology, philpapers) (1981). https://mlanthology.org/ijcai/1979/langley1979ijcai-rediscovering (ids: b02, c01)
- [M] Search snippet: lab study of human subjects on Kepler data (philpapers 'Laboratory Replication of Scientific Discovery Processes') (1990). https://api.philpapers.org/rec/QINLRO (ids: b03, d03)
- [M] Critique of historical fidelity of BACON data (search snippet, core.ac.uk) (1990). https://core.ac.uk/download/55868657.pdf (ids: b04)
- [V] Udrescu, Tan, Feng, Neto, Wu, Tegmark (2020) AI Feynman 2.0 (2020). https://arxiv.org/abs/2006.10782 (ids: b05)
- [V] La Cava, Orzechowski, Burlacu, de Franca, Virgolin, Jin, Kommenda, Moore (2021) Contemporary Symbolic Regression Methods and their Relative Performance (SRBench) (2021). https://arxiv.org/abs/2107.14351 (ids: b06)
- [V] Qiu, Jiang, Lu, Sclar, Pyatkin, Bhagavatula, Wang, Kim, Choi, Dziri, Ren (2024) Phenomenal Yet Puzzling: Testing Inductive Reasoning with Hypothesis Refinement (ICLR) (2024). https://arxiv.org/abs/2310.08559 (ids: b07)
- [V] Zhou, Liu, Shah, Tan, Tan (2024) Hypothesis Generation with Large Language Models (HypoGeniC) (2024). https://arxiv.org/abs/2404.04326 (ids: b08, c16)
- [V] Si, Hashimoto, Yang (2025) The Ideation-Execution Gap (2025). https://arxiv.org/abs/2506.20803 (ids: b10, c14, c27)
- [V] Majumder et al. (2024) DiscoveryBench: Towards Data-Driven Discovery with LLMs (2024). https://arxiv.org/abs/2407.01725 (ids: b15, c08)
- [V] Beel, Kan, Baumgart (2025) Evaluating Sakana's AI Scientist (2025). https://arxiv.org/abs/2502.14297 (ids: b18, c11, d21)
- [V] Gottweis et al. (2025) Towards an AI co-scientist (2025). https://arxiv.org/abs/2502.18864 (ids: b21, c18, d11)
- [V] Gupta and Pruthi (2025) All That Glitters is Not Novel: Plagiarism in AI Generated Research (2025). https://arxiv.org/abs/2502.16487 (ids: b22, c19)
- [V] Starace et al. (2025) PaperBench (2025). https://arxiv.org/abs/2504.01848 (ids: b23, c25)
- [V] Mitchener et al. (2025) Kosmos: An AI Scientist for Autonomous Discovery (2025). https://arxiv.org/abs/2511.02824 (ids: b24, c21)
- [M] Langley, Simon, Bradshaw, Zytkow (1987) Scientific Discovery: Computational Explorations of the Creative Processes (MIT Press); review text via search result only (1987). https://www.abebooks.fr/Scientific-Discovery-Computational-Explorations-Creative-Processes/94002290/bd (ids: c02)
- [V] Encyclopedia entry: Scientific Discovery, Computational Models of (Int. Encyclopedia of Social and Behavioral Sciences) (2001). https://users.sussex.ac.uk/~peterch/papers/isb202128.pdf (ids: c03)
- [V] Grayeli, Sehgal, Costilla-Reyes, Cranmer, Chaudhuri (2024) Symbolic regression with a learned concept library (LaSR) (2024). https://arxiv.org/abs/2409.09359 (ids: c05, d20)
- [V] Wang et al. (2024) SciMON: scientific inspiration machines optimized for novelty (2024). https://arxiv.org/abs/2305.14259 (ids: c15)
- [V] Novikov et al. (2025) AlphaEvolve: a coding agent for scientific and algorithmic discovery (2025). https://arxiv.org/abs/2506.13131 (ids: c20)
- [V] Ghareeb et al. (2025) Robin: a multi-agent system for automating scientific discovery (2025). https://arxiv.org/abs/2505.13400 (ids: c22)
- [V] Baek et al. (2024) ResearchAgent: iterative research idea generation over scientific literature with LLMs (2024). https://arxiv.org/abs/2404.07738 (ids: c23)
- [V] Li et al. (2024) Chain of Ideas: revolutionizing research via novel idea development with LLM agents (2024). https://arxiv.org/abs/2410.13185 (ids: c24)
- [V] Vafa, Chang, Rambachan, Mullainathan (2025) What has a foundation model found? Using inductive bias to probe for world models (2025). https://arxiv.org/abs/2507.06952 (ids: c26)
- [M] Philosophy-of-science critique of BACON (Springer chapter; author unverified) (1990). https://link.springer.com/chapter/10.1007/978-3-662-12405-5_10 (ids: c28)
- [V] Simon (1995) What is a systematic method of scientific discovery? (AAAI Spring Symposium) (1995). https://cdn.aaai.org/Symposia/Spring/1995/SS-95-03/SS95-03-001.pdf (ids: d01)
- [V] Liu, Dong, Gao, Feng, Pang (2025) Augmenting research ideation with data: an empirical investigation in social science (2025). https://arxiv.org/abs/2505.21396 (ids: d04, d05, d06)
- [V] Si et al. (2026) Towards execution-grounded automated AI research (2026). https://arxiv.org/abs/2601.14525 (ids: d07, d08)
- [V] Wen, Si, Yueh-Han, He, Feng (2025) Predicting empirical AI research outcomes with language models (2025). https://arxiv.org/abs/2506.00794 (ids: d09, d10)
- [V] Shahid, Radensky, Fok, Siangliulue, Weld, Hope (2025) Literature-grounded novelty assessment of scientific ideas (2025). https://arxiv.org/abs/2506.22026 (ids: d12)
- [V] Lin, Peng, Fang (2024) Evaluating and enhancing LLMs for novelty assessment in scholarly publications (SchNovel, RAG-Novelty) (2024). https://arxiv.org/abs/2409.16605 (ids: d13)
- [V] Luo, Kasirzadeh, Shah (2025) The more you automate, the less you see: hidden pitfalls of AI scientist systems (2025). https://arxiv.org/abs/2509.08713 (ids: d14, d15)
- [V] Georgiev, Gomez-Serrano, Tao, Wagner (2025) Mathematical exploration and discovery at scale (AlphaEvolve) (2025). https://arxiv.org/abs/2511.02864 (ids: d16, d17)
- [V] Xia, Sun, Liu (2026) SR-Scientist: scientific equation discovery with agentic AI (ICLR 2026) (2026). https://arxiv.org/abs/2510.11661 (ids: d18)
- [V] Liu et al. (2025) HypoBench: systematic benchmarking for hypothesis generation (2025). https://arxiv.org/abs/2504.11524 (ids: d22)
