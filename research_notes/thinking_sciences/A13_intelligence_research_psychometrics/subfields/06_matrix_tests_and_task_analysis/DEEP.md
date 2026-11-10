# Matrix tests and task analysis: deep document

*Subfield A13.06. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K26), critique.md in this folder. Evidence ids (a01, b12, d04 ...) point to lines in the evidence files. Several ids hold the same paper (for example a13, b01, c01 are all Webb et al. 2023). Marks: [V] opened in a session, [M] snippet or secondary only.*

*Honest scope note. The assigned focus has two halves. The Raven half is covered with opened sources, except the founding 1990 paper, which was never opened (its numbers come from Little et al. 2014). The Woodcock-Johnson half is thin: task descriptions, one small factor analysis and one norm-sample analysis. No LLM study on either WJ test was found.*

## 1. What it is

A matrix test shows a grid of cells (usually 3x3) with the last cell missing. The solver must find the rule that links the cells and pick or produce the missing one. Raven's Progressive Matrices (Standard, Coloured, Advanced) is the classic. The rules are hidden. No words are needed.

Why psychologists use it: it is a short test that correlates with general fluid reasoning. Why it matters to us: it is the cleanest small task where one can see how rule induction, working memory and answer search combine. A matrix item has a hidden rule, a few examples (the complete rows), one query (the blank) and a check (does the answer fit every row and column). That is the same shape as many of our bench items (ARC-style grids, number rules, brainteasers with a pattern).

Task analysis is the second half of the name. It means breaking an item into the processing steps and features that make it hard, then predicting difficulty from them. The main result is that a small rule taxonomy plus a count of rule tokens predicts human item difficulty well (57% of variance, a01, second-hand).

The two Woodcock-Johnson (WJ) subtests in the focus are related but different tasks:
- **Concept Formation**: the child sees instances and non-instances of a concept and must state the rule. It is inductive rule discovery with feedback, with frequent rule switching (d09).
- **Analysis-Synthesis**: the child works through an incomplete logic puzzle of coloured squares using a key, to find a missing colour. It is sequential, deductive rule application. Harder items need more steps (d09).

Where it touches our schema: S0 (classify the problem before solving: rule type, number of rules, perception load), S2 (write candidate rules), S4 and S8 (check an answer against every row and column), G3 (a pass must be on something not fitted), G7 (equal tokens), G10 (reasoning text is not evidence), G11 and G12 (budget by difficulty).

Neighbouring subfields in this run (links only, not covered here): Working memory; Strategy on matrices; Category learning; Analogy and distant sources; Vector-space relational similarity; Compression at inference time; Methods and measurement; Calibration and overconfidence.

## 2. History and theories in depth

### 2.1 Raven and the matrix format
Raven's matrices were designed to measure the ability to see relations and to reason about them without language. Easy items are solved by more than 90% of people. The last items of the Advanced test are solved by fewer than 10% (a07, Little et al. 2014 quoting population figures). Accuracy falls with item position by design.

### 2.2 Carpenter, Just and Shell 1990 (the founding account) [M]
The paper was not opened (403 on DTIC and CMU, paywall at APA; d16). What we have comes from Little, Lewandowsky and Craig 2014 [V] and from search-abstract text.

- Solvers compare adjacent cells pairwise, find correspondences between features, and then apply a rule.
- The rule taxonomy: constant in a row; pairwise progression (increment or decrement); figure addition or subtraction; distribution of three; distribution of two (an XOR-like rule) (a01).
- The number of rule tokens in an item explained 57% of the variance in item accuracy (a01, via Little et al. 2014). Distribution-of-two items occur only late in the test, where accuracy is lowest.
- Two production-system simulations. FAIRAVEN had no strategic memory organisation and no distribution-of-two rule, and matched median college students. BETTERAVEN had better goal management and all rules, and matched the best performers (a02, b29).
- Four processing steps: find correspondences between cells; move them to a working-memory buffer where matching rules fire; use the rules to generate the missing cell; search the answer options for the best match (a03). This is **constructive matching**: build the answer first, look at the options second.
- Two abilities separate high from low scorers: inducing abstract relations and managing many goals in working memory (b29, abstract only).

Not read: sample sizes, fixation statistics, FAIRAVEN and BETTERAVEN fit numbers (critique gap 5, still open).

### 2.3 Competing and later accounts
- **Working memory account**: difficulty rises with the number of rules and goals held at once. Early studies found the working-memory (WM) link did not rise with item difficulty, which looked like a refutation. Little et al. 2014 showed this is a statistical artefact of low overall correlation (a04-a06; section 5).
- **Bayesian rule induction** (Little, Lewandowsky, Griffiths 2012): a posterior over candidate rules given the cell features. Only the abstract was seen [M] (a28).
- **Analogy construction** (Lovett, Forbus, Usher 2010) and **visual-imagery models** (ASTI, a pixel-based model using affine and set transformations) (a27, a25).
- **Strategy theory**: constructive matching (study the matrix, predict, then look at options) versus response elimination (look at options, rule them out). Higher ability goes with more constructive matching (b24, b25; section 5).
- **Low-level visual account**: part of difficulty is cell visual complexity, not abstraction (b27).
- **Critiques**: Raven is a good indicator of g with no special status (Gignac 2015 [M], b31); verbal overshadowing can interfere with visual items (DeShon et al. 1995 [M], b30).

### 2.4 Error-pattern literature
Kunda, Soulieres, Rozga, Goel 2016 [V] built a two-stage classification of every wrong answer on the Standard Matrices (coder agreement 82% before and 95% and 98% after negotiation; a25). They review older work (Halstead 1943, Bromley 1953, Vodegel Matzen 1994, Babcock 2002). Low scorers make mostly **repetition** errors (copy a neighbour; above 75% of errors in some low samples). Average and above-average scorers make mostly **incomplete-correlate** errors (the answer fits part of the rule; above 50% of errors) (a26). The primary papers by Vodegel Matzen were not read.

### 2.5 Machine versions of Raven
- **PGM** (Barrett et al. 2018 [V]): procedural matrices with generalisation splits (a11, a12, b07, b08).
- **RAVEN** (Zhang et al. 2019 [V]): grammar-generated, 7 layouts, rules after Carpenter (Constant, Progression, Arithmetic, Distribute Three), with structure and rule annotations (a08).
- **I-RAVEN** (Hu et al. 2021 [V]): fixes a leak in the RAVEN answer set (b09). **RAVEN-FAIR** is a later fix and is still slightly biased (b10).
- **I-RAVEN-X** (Camposampiero et al. 2025 [V]): larger grid (3x10), wider value range (up to 1000), confounder attributes and smoothed (uncertain) values (b18, b19, d03, d04).
- **Digit Matrices** (Webb et al. 2023 [V]): a text-only task built on the SPM rule structure (a13).
- **MARVEL, IQ50, RAVEN-S, MM-IQ, MaRs-VQA, NeuroCognition RAPM**: visual or text benchmarks for multimodal and reasoning models (a20, a22, b15, b16, a24).

### 2.6 Woodcock-Johnson
WJ is a battery. Concept Formation and Analysis-Synthesis are Gf (fluid reasoning) subtests in the Cattell-Horn-Carroll frame. Evidence we have: a one-factor model for Matrix Reasoning, Analysis-Synthesis and Concept Formation with all standardised loadings above .65 (N=69, ages 6-21, WJ-R; d09), and a WJ IV norm-data analysis in which both subtests are modest g measures (d10). Nothing on LLMs (d12).

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources, or replicated), **S** single source, **C** contested, **H** human-only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Rule-token count predicts human item accuracy | 57% of variance | Carpenter et al. 1990 via Little 2014 (a01, M) | E (second-hand) |
| Easy Raven items near ceiling, last Advanced items near floor | over 90% solved vs under 10% | a07 | E, H |
| WM-Raven link rises with difficulty only when overall correlation is high | composite WM r=0.56, N=126; slope 0.004, t(34)=2.87, p<.01, r2=0.20; operation span alone r=0.36, no slope | Little et al. 2014 (a05) | S |
| Rule novelty adds no WM effect | p=0.39 | a06 | S |
| Humans beat deep nets on RAVEN | humans 84.41%; ResNet+DRT 59.56%; ResNet 53.43%; CNN 36.97%; WReN 14.69%; LSTM 13.07% (chance 12.5%); symbolic solver 100% | Zhang 2019 (a08, b06) | E |
| Original RAVEN answer set leaks the answer | context-blind ResNet 71.9% (RAVEN) vs 12.2% (I-RAVEN); context-blind CoPINet 94.2% vs 14.2%; CoPINet 91.4% to 46.1%; PGM context-blind 22.4% | Hu 2021 (b09, c21), Barrett 2018 (a11) | E |
| RAVEN-FAIR still slightly biased | context-blind ResNet 17.2% vs 12.5% chance | b10 | S |
| Perceive-abduce-execute beats monolithic nets | PrAE 65.03 / 77.02 (RAVEN / I-RAVEN) vs CoPINet 52.96 / 22.84; NVSA 87.7 / 88.1 | Zhang 2021 (a18), Hersche 2023 (b11) | E |
| Auxiliary rule supervision is dataset-dependent | PGM +13.9 points (62.6 to 76.5-76.9); RAVEN ResNet+DRT 59.56 to 20.71 with rule loss | Barrett 2018 (a11, b08); Zhang 2019 (a09, d08) | C |
| Distractor attributes hurt trained nets | 79.3 / 78.3% without vs 63.0 / 62.6% with (WReN) | b08 | S |
| Trained nets do not transfer to new combinations | WReN: interpolation 64.4, held-out pairs 27.2 (51.7 with meta-target), held-out triples 19.0, extrapolation 17.2 | b07 | E |
| Benchmark scores overstate concept grasp | RAVEN MRNet 73% to 49% (Sameness variants, 210 items) and 44% (Progression, 80 items); SCL 89% to 62% and 68% | Odouard and Mitchell 2022 (b23) | E |
| Trained transformers fail on left-out rules | 92.6-93.4% same-rule vs 47.0% (one rule removed) and 31.5% (two); centre token accuracy 96.88% but answer accuracy 45.31% | Li 2025 (d15) | S |
| GPT-3 beats students on text Digit Matrices | N=40; generative OR 1.88 (CI 1.21-2.91, p=.005); multiple choice OR 6.27 (p=2.3e-8); best human 100% | Webb 2023 (a13) | C |
| GPT-3 difficulty profile resembles humans but is more fragile | item-type correlation r(30)=.39, p=.027; progression OR human .41 vs GPT-3 .07; unique rules .61 vs .25; permuted logic .52 vs .06 | a14 | S |
| Raven-text LLM scores, 2023 | open-ended text / symbolic: GPT-4 .410 / .330; davinci-003 .343 / .234; GPT-3.5 .226 / .161. Multiple choice: GPT-4 .697 / .535; davinci-003 .461 / .452; GPT-3.5 .276 / .315; chance .125 | Gendron 2023 (a16, c07) | S |
| Generic CoT does not help | GPT-4 MC .697 to .596 (text), .535 to .517 (symbolic); open .410 to .385 (text), .330 to .354 (symbolic); GPT-3.5 open .226 to .302 | c08, b05 | C |
| Fine-tuning gives in-distribution gain only | LLaMA2-7B .977 / .965; OOD splits roughly .44-.77 and .06-.09 | c09, a17 | E |
| Visual matrices near chance for multimodal models (2023-24) | IQ50, RAVEN-S, CCSE within -8.7 to +7.3 of random; MARVEL closed 25.7%, open 24.0%, humans 68.86%, best consistency 5.97%; MM-IQ o3 33.17% vs human 51.27%, chance 25%; MaRs-VQA open 16.9-24.3%, adults 81% | a20, a22, b15, b16 | E |
| Text-attribute input is far easier | GPT-3 3x3Grid 86.4% (naming) to 93.2% (naming plus decomposition); GPT-4 per-attribute 91.4%, with self-consistency n=7 93.2%; Llama-3 70B 83.2% and 85.0% (84.8% in d01) | Hu 2023 (b12), Hersche 2024 (c16) | E |
| Per-attribute decomposition helps arithmetic most | GPT-4 arithmetic rule 27.1% to 73.6%; progression 98.0 to 100; distribute-three 91.6 to 99.5; OPT 1.3B 20-30% to over 70% | c17, b12 | E |
| Predict-then-match beats options-visible (leak-free set) | GPT-4 74.8% vs 56.0 / 60.0; Llama-3 70B 79.0% vs 22.8 / 22.4. Not token matched | Hersche 2024 (d01) | S |
| Arithmetic fails at large range without tools | overall at range 50 / 100 / 1000: GPT-4 82.2 / 79.6 / 76.6; Llama-3 76.8 / 73.0 / 74.2; arithmetic rule at 1000: GPT-4 8.4%, Llama-3 0.4%; programmed ARLC 99.5% | c18 | S |
| Part of arithmetic failure is rule induction | 32 of 68 GPT-4 arithmetic errors fit a rule from the last row only | d02 | S |
| Reasoning models on clean text I-RAVEN | range 10: o3-mini medium 86.6 (arithmetic 74.4, 5,445 tokens); high 92.6 (86.1, 9,867); R1 80.6 (74.8, 4,486). Range 1000: o3-mini 81.0 (60.8, 7,209); R1 82.8 (65.8, 5,505) | Camposampiero 2025 (d03) | S |
| Reasoning models collapse under combined stress | o3-mini 81.0 clean, 69.8 (10 confounders), 75.6 (smoothing pL=0.51), 17.0 (both, 18,482 tokens); R1 82.8, 77.0, 63.0, 23.2; high-effort o3-mini 31.0% at 53,596 tokens; neuro-symbolic 98.6 to 88.0 | d04, b18 | S |
| Rule-program execution feedback | I-RAVEN-X Prolog direct 34.0, execution repair 39.6, ABPR 88.6; Python direct 64.0, repair 81.6. A-I-RAVEN Prolog 28.2 / 34.0, ABPR 93.6; Python 74.0 / 88.6 | Qiu 2026 (c23) | S (supplementary experiment) |
| Multi-round elimination beats single CoT | GPT-4o MaRs-VQA: CoT 33.96; +1/3/5 shots 35.22 / 36.10 / 36.03; multi-round 41.96; multi-round +1-shot 42.08 (3-seed averages) | Cao 2025 (b17) | S |
| Hypothesis-then-execute helps MC, hurts free generation | +31.86% relative (MC symbolic RAVEN); -40.93% relative (free generation); gain by difficulty +15.92 / +18.68 / +37.20% | LogiDynamics (c22) | S |
| Only corrective, interactive hints help | corrective hints and CoT demos up to +100% relative for GPT-4V; general and sample-specific hints hurt; refusals 4% to 18% with one-shot | Ahrabian 2024 (a21, c12) | S |
| Reasoning text unfaithful | faithfulness GPT-4V 50%, Gemini Pro Vision 25%; joint answer and reasoning correct GPT-4V 26%, best open 4% | a21, c13 | S |
| Pattern hints null; reasoning off helped text MC | hints p=.177 / .45 / .666; reasoning-off gain text MC p=.021, text gen p=.83, image MC p=.173 (4 models) | NeuroCognition (b21, d07) | S |
| Format swings, one run per model | MC to generative: GPT-5 .540 to .605; Claude Sonnet 4 .560 to .385; Grok 4 Fast .690 to .555 | a24, d07 | S |
| Models do better on text than image; humans (pilot) not | human text MC .430 +/- .167, gen .444 +/- .183 (N=9, same people both formats); image .814 borrowed from RAVEN paper | b20, d07 | S (weak) |
| Counterfactual letter strings: models drop, humans do not | human accuracy about .75 pooled; GPT models .35-.49; alternative-rule share of errors: humans 38.6%, GPT-4 22%, GPT-3 5.8% | Lewis and Mitchell 2024 (c05, c06) | C |
| Code execution closes part of that gap | GPT-4 plus code matches humans (P=.496) on permuted-alphabet letter strings; 46% of GPT-4 errors valid alternative rule vs 39% human | Webb 2024 (b02) | C (authors' own reply) |
| Correct answers often rest on wrong rules | about 27% of o3 correct ConceptARC text answers on unintended or wrong rules (humans about 7%); rule labels agree across repeats 66.0-70.9% pairwise; Python tools: text 77.1 to 75.6, images 5.6 to 29.2 (o3) | Beger 2026 (d13) | S |
| High ability goes with constructive matching | N=210; ability vs time on matrix r=.593; strategy shift vs item position r=.190 ns (r=.529, p=.004 first 27 items); eye-tracking predicts correctness above .8 from first 60% of time | b24, b26 | E, H |
| Visual complexity of cells adds to difficulty | N=159, 12-item APM; edge density and perceived complexity predict time and fixations | b27 | S, H |
| Dual n-back training does not raise matrix scores | N=58 (20 / 19 / 19), 20 sessions; no transfer | Thompson 2013 (b28) | S |
| WJ Concept Formation and Analysis-Synthesis load on Gf with matrices | all standardised loadings above .65, N=69, ages 6-21 | Green 2017 (d09) | S, H |
| WJ IV subtests are modest g measures | Schmid-Leiman g: Concept Formation .54 (ages 9-13), .56 (14-19); Analysis-Synthesis .50, .52; Number Matrices .61; Number Series .67; norm N=7,416 | Dombrowski 2018 (d10) | S, H |
| WJ III descriptives | Analysis-Synthesis n=87 mean 102.91 SD 17.19; Concept Formation n=89 mean 98.37 SD 16.16 | d11 | descriptive |

## 4. Mechanisms and models

Each model below is described so it could be coded. They are human or trained-model mechanisms. Section 7 says what we take.

### 4.1 Rule taxonomy and difficulty predictor (Carpenter)
Representation: each cell is a set of attribute values (shape, size, colour, number, position). A rule is a triple (attribute, rule type, row or column scope).
Rule types: constant; progression (+k or -k per step); arithmetic (cell3 = cell1 plus or minus cell2); distribute-three (the same three values appear once per row, order may differ); distribute-two (XOR-like: a feature present in exactly one of two cells).
Difficulty predictor: count rule tokens (one per attribute-rule pair) and add rule-type weights. Fit a logistic model on item accuracy. Warning: our only number for this (57%) is second-hand from 1990 data. Refit on our own items.

### 4.2 Constructive matching pipeline (Carpenter steps, Hersche d01)
1. Parse each cell into attributes (code or model).
2. For each attribute and each row, test each rule type against rows 1 and 2.
3. Keep rules that fit all complete rows. Apply them to row 3 to generate the missing cell.
4. Only then show or compare options. Pick the nearest by attribute match.

Key property: options stay hidden until step 4. On the I-RAVEN centre set this "predictive" route gave GPT-4 74.8% against 56.0-60.0% and Llama-3 70B 79.0% against about 22.6% (d01). Not token-matched, no options-only control, 2024 models.

### 4.3 Decomposed prompting (Hu 2023, Hersche 2024)
Convert panels to text attributes. Issue one query per attribute: "what is the rule for attribute X across these rows, what is the value in the blank". Combine the per-attribute answers in code. Optionally sample n=7 and vote (self-consistency). This took GPT-4 arithmetic from 27.1% to 73.6% and overall to 91.4% (93.2% with n=7) (c16, c17).

### 4.4 Abduce, execute, check (PrAE, NVSA, ABPR)
Perception gives per-attribute distributions. The abduction engine scores every rule template against the context. The execution engine applies the best-scoring rule to produce the answer distribution. ABPR (Qiu 2026) has the LLM write the rule as a Prolog or Python program. A meta-interpreter runs it on the given cells and returns which step failed. The model repairs only that step (c23). Execution feedback that names the failing step lifted I-RAVEN-X from 34.0% (direct Prolog) to 88.6%.

### 4.5 Soft rule selection (ARLC)
Score every candidate rule with a confidence. Combine all predictions weighted by confidence, instead of committing to one rule. ARLC reached 92.4-92.6% on I-RAVEN and 98.6-100% on unseen rule-attribute pairs (d06). The ablations do not isolate the soft-selection part, so its contribution is unknown.

### 4.6 Strategy model (eye-tracking)
Two observable strategies. Constructive matching: long time on the matrix, late first look at options, few toggles between matrix and options. Response elimination: early and frequent option inspection. High-ability people use constructive matching and raise it as items get harder. Low-ability people lower it (b24, b25 citing Liu 2023). A gaze model using nine metrics from the first 60% of response time predicts correctness above .8 (b26).

### 4.7 Working-memory model
Difficulty depends on how many rules and goals must be held at once. Little et al. 2014 show the item-wise correlation slope grows with overall correlation (simulation slopes 0.0002 to 0.0016 for overall rho 0.1 to 0.9; a04). For an LLM the analogue is the number of rule tokens per prompt and the length of the context, not human WM.

### 4.8 Error taxonomy
Repetition (copy a neighbour), incomplete correlate (fits part of the rule), other. For an LLM agent these map onto: copied an adjacent cell; satisfied one row or column rule but not all (b22, K18). A code check that tests the answer against every row and column catches the second class.

## 5. What holds up

**Holds up (two or more sources, or replicated)**
- Original RAVEN has an answer-set shortcut. Found by Hu 2021 and Barrett 2018 (context-blind 22.4% on PGM), confirmed by Malkinski and Mandziuk 2022 (b10). Always run a context-blind control.
- Explicit rule-then-execute pipelines beat monolithic nets and generalise better (PrAE, NVSA, ARLC, ABPR).
- Perception is the main bottleneck for multimodal models. Six benchmarks agree (IQ50, RAVEN-S, CCSE, MARVEL, MM-IQ, MaRs-VQA).
- Per-attribute decomposition helps text LLMs, with two independent teams (Hu 2023, Hersche 2024).
- Execution checks of a stated rule beat prompting for rewrites (Qiu 2026, supported by the corrective-hint result of Ahrabian 2024).
- Trained models do not transfer: PGM splits, Gendron fine-tuning, Odouard and Mitchell variants, VCog OOD (29-32%), rule omission (Li).
- High-ability humans use constructive matching, replicated in several eye-tracking samples.

**Failures to replicate and contested results**
- WM and difficulty: the early "no link" results (Wiley 2011, Salthouse 1993, Unsworth and Engle 2005) were an artefact of low overall correlation. Little 2014 found the slope with a stronger composite (r=0.56). Their novelty test was null (p=0.39). One sample only.
- Auxiliary rule loss: helps on PGM (+13.9), hurts on RAVEN (59.56 to 20.71). Zhang gives no cause. Our guess (rule loss disturbs a learned answer-set shortcut) is untested.
- WReN: strong on PGM, near chance on RAVEN (14.69%) (a10).
- GPT-3 analogical reasoning: Webb 2023 positive; Lewis and Mitchell 2024 and Hodel and West 2024 negative on counterfactual letter strings; the Webb 2024 reply says code execution fixes counting errors. Unresolved, and all on GPT-3 to GPT-4.
- Chain of thought: hurts GPT-4 on RAVEN-T multiple choice (Gendron), helps GPT-4V with demonstrations (Ahrabian), helps GPT-3.5 open-ended. Task format and model set the sign.
- Reasoning on or off: turning reasoning off helped text MC for 4 models (p=.021), no effect on generative or image. Reasoning had to be disabled for two models because overthinking used up the output limit.
- Hints: general and sample-specific hints hurt (Ahrabian); pattern hints null (NeuroCognition); corrective interactive hints helped.
- Stress headline: "o3-mini 86.6% to 17.0%" compares different settings. The matched baseline is 81.0% (d04).
- CoPINet on I-RAVEN: 22.84 (trained on 2x2Grid only, Zhang 2021) vs 46.1 (full training, Hu 2021). Both agree on a large drop.

**Moderators**
- Input form: text attributes versus images (a large gap for models, reverse for humans in a weak pilot).
- Answer format: multiple choice versus free generation (large, model-specific swings, single run).
- Rule type: arithmetic worst; progression and distribute-three nearly solved under decomposition.
- Value range and grid length: arithmetic falls below 10% at range 1000 for non-reasoning models without tools.
- Confounders plus fuzzy values: the combination breaks reasoning models; either alone does not.
- Layout: WReN does better on grid layouts than on independent components.

**Interventions that worked**: per-attribute decomposition; predict-before-options; execution-checked rule programs; multi-round elimination with self-check; corrective hints; self-consistency; reasoning models for large-range arithmetic.
**Interventions that did not work or were mixed**: generic CoT; extra shots for GPT-4 (worse); general hints; pattern hints; more reasoning effort at the hardest setting (31.0% at 53,596 tokens); dual n-back training for humans; auxiliary rule loss on RAVEN; Python tools on text ConceptARC.

## 6. Language models

### 6.1 Text matrices, 2023-24 era
- GPT-3 on Digit Matrices beat the human mean (OR 1.88 generative, 6.27 MC) (a13). GPT-3 on RAVEN 3x3Grid with attribute naming reached 86.4%, and 93.2% with decomposition (b12).
- RAVEN-T (Gendron): GPT-4 41.0% open-ended and 69.7% multiple choice on text; lower on the symbolic format (33.0%, 53.5%). Weaker models were near zero or near chance. Raven is likely in the training data (suspected, not proven) (b04).
- On I-RAVEN centre with oracle perception: GPT-4 56.0-60.0% when picking from options, 74.8% predict-then-match, 91.4% with per-attribute queries, 93.2% with n=7 votes. Llama-3 70B: 22.4-22.8%, 79.0%, 83.2%, 84.8-85.0%. GPT-4o was worse than GPT-4, and GPT-4 got worse with in-context examples in this setup (c16).
- Rule breakdown: constant, progression and distribute-three nearly solved after decomposition; arithmetic is the weak rule (c17).

### 6.2 Visual matrices
Near chance for every 2023-24 multimodal model. Within about 9 points of random on IQ50, RAVEN-S, CCSE (a20). On MARVEL, 25.7% closed and 24.0% open against 68.86% humans, with only 5.97% perception-plus-answer consistency (a22). o3 33.17% on MM-IQ against 51.27% humans and 25% chance (b15). Open models 16.9-24.3% on MaRs-VQA; GPT-4o 33.96% with CoT and 41.96% with multi-round elimination; o1 52.29%; adults 81% (b16, b17, c14). Fine-tuning a 7B model on reasoning annotations gave about 70% in distribution and 29-32% on RAVEN OOD (c15). Faithfulness of the stated reasoning was 50% for GPT-4V and 25% for Gemini Pro Vision (a21).

### 6.3 2025-26 reasoning models
- I-RAVEN range 10 (symbolic text): o3-mini medium 86.6% at 5,445 output tokens; high 92.6% at 9,867; R1 80.6% at 4,486. A prompted GPT-4 needed about 21 tokens per item against these thousands, so a rise of a few points costs two to three orders of magnitude more output (b19, d03).
- Range 1000: o3-mini medium 81.0% (arithmetic 60.8%), R1 82.8% (65.8%). Non-reasoning arithmetic collapses (GPT-4 8.4%) (d03, c18).
- Combined confounders and smoothing: 17.0% (o3-mini) and 23.2% (R1), with 18,482 tokens for o3-mini. High effort gave 31.0% at 53,596 tokens (d04). The neuro-symbolic model scored 88.0% under the same stress.
- The authors read this as reasoning models being unable to keep several probabilistic outcomes alive. Two causes (longer prompts; a general limit) were not separated (d05).
- NeuroCognition (10 recent models, single runs): models do better on text than image (p=.010); format flips scores by up to 0.175; hints null (b20-b22).
- Beger 2026 (ConceptARC, not Raven): o3 text 77.1% at medium effort; visual 5.6%, 29.2% with tools; about 27% of correct text answers rested on unintended rules (d13).
- ABPR 2026: LLM-written Prolog with an execution meta-interpreter reached 88.6% on I-RAVEN-X against 34.0% direct (c23).

### 6.4 Behaviour patterns
Invented visual features; over-clever rules that skip simple local rules (XOR, concatenation); answers that satisfy the stated rule on paper but break the real logic (b22). Reasoning text is often unfaithful (a21). Rule labels are unstable across repeats (about two thirds agreement, d13).

### 6.5 What changed it, by how much
| Change | Effect | Token cost reported? |
|---|---|---|
| Per-attribute decomposition (GPT-4) | arithmetic 27.1 to 73.6; overall to 91.4 | no |
| Predict first, then match (GPT-4 / Llama-3) | 56-60 to 74.8; 22.4-22.8 to 79.0 | no |
| Self-consistency n=7 on top of decomposition | +1.8 (GPT-4), +1.8 to +1.6 (Llama-3) | 7x calls |
| Reasoning model vs prompted LLM, range 1000 arithmetic | 8.4 to 60.8-65.8 | thousands of tokens vs tens |
| High vs medium effort, hardest stress | 17.0 to 31.0 | 18,482 to 53,596 |
| Execution feedback (Prolog) | 34.0 to 88.6 | not reported |
| Multi-round elimination (GPT-4o, images) | 33.96 to 41.96 | not reported |
| Generic CoT | about -10 to +8 points depending on model and format | not reported |
| Python tool on text ConceptARC | 77.1 to 75.6 | not reported |

Almost every study here used 2023-24 models. Only b15, b18-b22, c23, d03-d05 and d13 touch 2025-26 reasoning models.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Context-blind control before trusting any rule-induction item set** (G3, S0). Run the item with the question hidden or the examples removed. Drop items where the blind run beats chance. [E] Evidence: b09, c21, a11, b10, a19 (K02).
2. **Check the chosen answer against every row and column, and score partial matches as failures** (S4, S8, G3). A code check that applies the stated rule to all given cells. Human error types (incomplete correlate) and LLM failure traces (answers that fit part of the evidence) agree. [E] Evidence: a26, b22, a21, K18, K10.
3. **Use rule type and rule count as S0 difficulty features** (S0, G12). Tag problems by rule type (constant, progression, arithmetic, distribute, XOR) and count of distinct rules. Treat progression, arithmetic and multi-rule binding as the hard classes. [E] for the direction (human 57% second-hand; GPT-3 OR .07 for progression; arithmetic worst for GPT-4). Evidence: a01, a14, c17, c02 (K01).
4. **Separate input description from rule induction** (S1, S2). Perception is the bottleneck for images. When a problem has a visual form, give a text description of cells first and judge the two steps apart. [E] Evidence: a20, a22, b15, b16, a23, b12 (K04).
5. **Decompose by attribute when several attributes change** (O3). One sub-question per attribute, combine in code (G5). [E] Evidence: b12, c17, c16 (K05, K06). Needs the equal-token check from G7 before it becomes a default.
6. **When a rule is stated, execute it on the given cells and feed back the failing step** (G2, S5). Real execution output beats self-critique or general hints. [E] Evidence: c23, a21, c12 (K10). Already matches G2.
7. **Do not trust training-style gains or benchmark gains without shifted items** (G7, memory). Judge scaffold changes on re-labelled or re-laid-out items, not only the original set. [E] Evidence: a09, c09, c15, b23, b07, d15 (K11).
8. **Do not add a generic "think step by step" suffix to rule-pattern items** (G11). Effect has both signs. [C] Evidence: c08, b05, a21, b17. Keep as a test, not a rule.

### Test first (single-source or contested)

| Candidate | Part | Status | Evidence ids |
|---|---|---|---|
| Predict the missing cell before seeing options, then match by code | S0 / S2 / O | [S] | d01, a03, K13, K20 |
| Keep top-3 candidate rules alive with weights under noisy or confounded input | O (hypothesis set), S2 | [S] | d05, d06, d04, K23 |
| Run candidate rule as code (Python or Prolog) for arithmetic rules at large ranges | O, G2 | [S] | c18, d02, d03, c23, K21 |
| Score the stated rule as well as the answer, and require stable rule across 3 repeats | G10, S8 | [S] | d13, K25 |
| Abduce-then-execute prompting only when options are shown | O | [S] | c22, K09 |
| Multi-round elimination with a self-check | O | [S] | b17, c14 |
| Token cap plus verification instead of more effort | G11, G12 | [S] | d03, d04, K22 |
| Turn reasoning off or short for 8-choice text matrices | G11 | [C] | b21, d07 |
| Name the rule type in the prompt | S0 | [C] | d08, b21, K24 |
| Counterfactual relabelling of symbols as a generalisation check | G3, S8 | [C] | c05, b02, d14, K26, K12 |
| Corrective-hint loop: show a located failure, not a general hint | S5 | [S] | a21, c12 |

Not an item: working-memory training (b28) and Woodcock-Johnson loadings (d09, d10) have no direct agent counterpart yet.

## 8. Concrete tests on our bench

All arms run at the same token cap. Report tokens per item. Use at least 3 seeds. Use I-RAVEN style text items (attribute lists) and our ARC and brainteaser sets with rule tags.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | I-RAVEN centre, text attributes, range 10 and 100 | A: options visible. B: options hidden, predict cell, match by code. C: options only (control) | accuracy; C must stay near 12.5% | B beats A by 10+ points (d01 gap was 15-55 on 2024 models; expect less on current ones) |
| T2 | Same items, tagged by rule type | joint query vs per-attribute query, combined in code | accuracy by rule type, tokens | arithmetic gain largest (GPT-4 27.1 to 73.6 earlier); small for constant and progression |
| T3 | Arithmetic items at range 10, 100, 1000 | no tool; code execution of stated rule on first two rows; force-use-first-two-rows step | arithmetic-rule accuracy | tool arm holds near the range-10 level; no-tool falls (GPT-4 8.4% at 1000) |
| T4 | Items with 10 confounder attributes and smoothed values | single committed rule; top-3 weighted rules; plain reasoning at higher effort | accuracy drop vs clean | top-3 arm drops less than single-rule arm; high effort gains small (d04 pattern) |
| T5 | Our rule-induction items with stated rule | answer only; answer plus stated rule scored by code against all rows and columns | accuracy and share of correct answers with wrong rule | 10-25% of correct answers fail the rule check (d13 had 27% for o3) |
| T6 | Same items, 3 seeds each | MC vs generative; reasoning on vs short | SD across seeds, accuracy | format swing up to 0.1-0.2; fill the variance gap in NeuroCognition |
| T7 | Items with relabelled symbols and shuffled order | original vs counterfactual, with and without code | accuracy gap | gap shrinks with code (Webb 2024 claim); unknown for current models |
| T8 | Mixed-difficulty set | uniform budget vs budget by S0 rule count | accuracy per token | spend-by-difficulty wins (G12); check that rule count is a usable predictor first |
| T9 | Items with wrong first attempts | general hint vs corrective hint with located failing row | accuracy after revision | corrective hint wins; general hint no better than none |

## 9. What does not transfer, and why

- **Human working-memory capacity limits.** An LLM does not hold goals in a 4-item buffer. The analogue is context length and rule-token count. Little et al. 2014 is about people (K14).
- **Eye-tracking strategy measures.** No gaze for an agent. The usable idea is only the order of operations (matrix first, options later).
- **Item position as difficulty.** Raven items run from easy to hard by position. Our items are shuffled, so position gives no signal.
- **Working-memory training and g loadings.** Dual n-back transfer failure (N=58) and WJ factor loadings say nothing about a prompt scaffold.
- **Error types as ability markers.** Repetition versus incomplete-correlate errors separate human ability groups. For an LLM the same type tags are still useful as a diagnosis, but the ability meaning does not carry over.
- **Trained-network results** (PGM, RAVEN nets, rule loss, ARLC). They need training. Only their lessons carry: shortcuts exist, explicit rule structure generalises, execution helps.
- **Visual perception results.** Only relevant if our bench passes images. Our text items avoid the main bottleneck, so image findings set an upper bound on how much text results will hold.
- **Memorised content.** Raven and RAVEN are public; contamination is suspected for GPT-4 and not measured for current models, so scores on public matrix items should not be read as general ability.
- **Perfect oracle perception** (text attributes given by the benchmark). Real tasks need the agent to build this description, which is where it fails.

## 10. Open questions

1. What are the original Carpenter, Just and Shell 1990 numbers (sample sizes, fixation statistics, FAIRAVEN and BETTERAVEN fit)? Not read.
2. Do the Woodcock-Johnson Concept Formation and Analysis-Synthesis tasks yield a useful rule-discovery-from-feedback benchmark, and how do current LLMs score? No LLM study found; search was limited.
3. Does predict-before-options win at equal tokens on current reasoning models, with a context-blind control?
4. Does a code tool fix arithmetic at range 1000, or is the failure rule induction (32 of 68 errors fit a last-row rule)?
5. Does keeping several candidate rules alive reduce the collapse under confounders and smoothing?
6. How much of Raven-style performance on 2025-26 models is memorisation? No counterfactual matrix test exists for them.
7. How large is run-to-run variance for format and reasoning on/off on matrix items? NeuroCognition ran once per model.
8. Why does auxiliary rule labelling help on PGM and hurt on RAVEN?
9. Is the human text-versus-image result real? The pilot had 9 people and borrowed an image figure from another sample.
10. Does token count matter more than reasoning effort on the hardest stress? Only o3-mini was tried at high effort.

## 11. Sources

[V] = opened this session (or a prior session of this run, per the evidence file). [M] = snippet or secondary only.

- [M] Carpenter, Just, Shell (1990) What one intelligence test measures. https://doi.org/10.1037/0033-295X.97.3.404 ; https://apps.dtic.mil/sti/pdfs/ADA221448.pdf ; https://psycnet.apa.org/record/1990-23033-001
- [V] Little, Lewandowsky, Craig (2014) Working memory capacity and fluid abilities. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00239/pdf
- [M] Little, Lewandowsky, Griffiths (2012) A Bayesian model of rule induction in Raven's progressive matrices. https://escholarship.org/uc/item/9x09p399
- [V] Zhang, Gao, Jia, Zhu, Zhu (2019) RAVEN. https://arxiv.org/abs/1903.02741
- [V] Barrett, Hill, Santoro, Morcos, Lillicrap (2018) Measuring abstract reasoning in neural networks (PGM). https://arxiv.org/abs/1807.04225
- [V] Hu, Ma, Liu, Wei, Bai (2021) Stratified rule-aware network (I-RAVEN). https://arxiv.org/abs/2002.06838
- [V] Malkinski and Mandziuk (2022/2023) Deep learning methods for abstract visual reasoning (survey). https://arxiv.org/abs/2201.12382
- [V] Zhang, Jia, Zhu, Zhu (2021) Abstract spatial-temporal reasoning via probabilistic abduction and execution (PrAE). https://arxiv.org/abs/2103.14230
- [V] Hersche et al. (2023) A neuro-vector-symbolic architecture for Raven's matrices (NVSA). https://arxiv.org/abs/2203.04571
- [V] Camposampiero et al. (2024) Towards learning abductive reasoning using VSA distributed representations (ARLC). https://arxiv.org/abs/2406.19121
- [V] Webb, Holyoak, Lu (2023) Emergent analogical reasoning in large language models. https://arxiv.org/abs/2212.09196
- [V] Webb, Holyoak, Lu (2024) Evidence from counterfactual tasks supports emergent analogical reasoning. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell (2024) Using counterfactual tasks to evaluate the generality of analogical reasoning. https://arxiv.org/abs/2402.08955
- [V] Hodel and West (2023/2024) Response: Emergent analogical reasoning in large language models. https://arxiv.org/abs/2308.16118
- [V] Gendron, Bao, Witbrock, Dobbie (2023) Large language models are not strong abstract reasoners. https://arxiv.org/abs/2305.19555
- [V] Hu et al. (2023) In-context analogical reasoning with pre-trained language models. https://arxiv.org/abs/2305.17626
- [V] Hersche, Camposampiero et al. (2024/2025) Towards learning to reason: comparing LLMs with neuro-symbolic on arithmetic relations in abstract reasoning. https://arxiv.org/abs/2412.05586
- [V] Camposampiero, Hersche, Wattenhofer, Sebastian, Rahimi (2025) Can large reasoning models do analogical reasoning under perceptual uncertainty? https://arxiv.org/abs/2503.11207
- [V] Camposampiero et al. (2025) I-RAVEN-X. https://arxiv.org/abs/2510.17496
- [V] Ahrabian et al. (2024) The curious case of nonverbal abstract reasoning with multi-modal LLMs. https://arxiv.org/abs/2401.12117
- [V] Jiang et al. (2024) MARVEL. https://arxiv.org/abs/2404.13591
- [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4, and GPT-4V on abstraction and reasoning tasks (ConceptARC). https://arxiv.org/abs/2311.09247
- [V] Xu et al. (2024) LLMs and the Abstraction and Reasoning Corpus. https://arxiv.org/abs/2305.18354
- [V] Cai, Yang, Hu (2025) MM-IQ. https://arxiv.org/abs/2502.00698
- [V] Cao et al. (2025) What is the visual cognition gap between humans and multimodal LLMs (VCog-Bench, MaRs-VQA). https://arxiv.org/abs/2406.10424
- [V] Haznitrama, Ardi, Oh (2026) NeuroCognition. https://arxiv.org/abs/2603.02540
- [V] Zheng et al. (2025) LogiDynamics. https://arxiv.org/abs/2502.11176
- [V] Qiu et al. (2026) ABPR: LLM-driven algorithmic debugging. https://arxiv.org/abs/2603.20334
- [V] Beger et al. (2026) Distinguishing concept understanding from shortcuts on ConceptARC. https://arxiv.org/abs/2510.02125
- [V] Odouard and Mitchell (2022) Evaluating understanding on conceptual abstraction benchmarks. https://arxiv.org/abs/2206.14187
- [V] Li (2025) A study of rule omission in Raven's Progressive Matrices. https://arxiv.org/abs/2510.03127
- [V] Kunda, Soulieres, Rozga, Goel (2016) Error patterns on the Raven's Standard Progressive Matrices. https://doi.org/10.1016/j.intell.2016.09.004
- [V] von Gugelberg and Troche (2025) Individual differences in strategy and the item-position effect. https://pmc.ncbi.nlm.nih.gov/articles/PMC12295732/
- [V] Individual differences in problem-solving behaviour in reasoning tests (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13608805/
- [V] Eye-tracking plus machine learning on Raven's Progressive Matrices (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11595889/
- [V] Eisma and de Winter (2023) Responses to Raven matrices. https://pmc.ncbi.nlm.nih.gov/articles/PMC10469510/
- [V] Thompson et al. (2013) Failure of working memory training to enhance cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC3661602/
- [V] Green, Bunge, Briones Chiongbian, Barrow, Ferrer (2017) Fluid reasoning predicts future mathematical performance. https://escholarship.org/uc/item/3fp4r6mc
- [V] Dombrowski, McGill, Canivez (2018) Hierarchical exploratory factor analyses of the WJ IV. https://doi.org/10.1037/spq0000221
- [V] Caemmerer, Keith, Reynolds (2020) Beyond individual intelligence tests. https://doi.org/10.1016/j.intell.2019.101433
- [M] DeShon, Chan, Weissbein (1995) Verbal overshadowing effects on Raven's APM (cited in PMC10469510).
- [M] Gignac (2015) Raven's is not a pure measure of general intelligence (cited in PMC10469510).
- [M] Malkinski and Mandziuk (2025) A-I-RAVEN and I-RAVEN-Mesh (named in the ABPR paper).
