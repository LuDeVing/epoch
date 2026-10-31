# Program induction, language of thought: deep document

*Subfield C03.02. Focus: concepts as short programs (Piantadosi, Goodman). Schema parts: S2 REPRESENT, S3 GENERATE. Built from evidence_a-d.jsonl, claims.jsonl (K01-K28) and critique.md in this folder. Evidence ids (a01, b12, c05, d08 ...) point to those files. Files a, b and c re-read the same ten or so papers, so repeated ids are not independent sources: claims count papers, not lines. Almost no study here uses a 2025-2026 frontier model; read every LLM number as "model of its year".*

---

## 1. What it is

The language of thought (LoT) idea says that thinking uses a compositional code. A small set of primitive symbols is combined by rules into longer expressions. Fodor (1975) and Boole (1854) are the founders (a30, not opened).

The modern version is **program induction**. A concept is a short program. The learner holds a grammar of primitives (and, or, not, count, next, set operations, loops). It scores each possible program by two things:

- **Prior**: shorter programs are more likely (a simplicity bias).
- **Fit**: how well the program explains the examples seen.

Posterior = prior x fit. This is Bayesian inference over programs, or minimum description length. Key works: Goodman, Tenenbaum, Feldman and Griffiths 2008 (Rational Rules, a07/a08); Piantadosi, Tenenbaum and Goodman 2012 (number words, a01-a06) and 2016 (logical primitives, a09-a12); Lake, Salakhutdinov and Tenenbaum 2015 (Bayesian Program Learning, a13/a14); Ellis et al. 2021 (DreamCoder, a17/a18); Rule, Tenenbaum and Piantadosi 2020 and 2024 (a29, c19).

The idea that matters for an agent has three parts:

1. **Represent a concept as an executable rule**, not as a vague description.
2. **Generate many candidate rules** (proposal), then **test them by running** on the examples (likelihood).
3. **Prefer the short rule** when several fit.

Since 2023 an LLM can play the proposer (Ellis 2023 a19; Wang et al. 2024 a20; Qiu et al. 2024 a22). Execution on the examples plays the likelihood. This is the shape of the schema's S2 (write 1 to 4 candidate rules), S3 (generate attempts), S4 (test) and S7 (select).

Scope: what the human work found, what the LLM and AI work measured (with numbers), what holds up, and which parts to test in our schema. Overlaps with other subfields are noted only as links: library learning (sibling folder 03_library_learning), Statistical MDL, Systematicity, Heuristic search, Sampling and voting, Scientific discovery as reasoning, Structure mapping.

---

## 2. History and theories in depth

### 2.1 Roots (1950s to 2000)

- **Bruner, Goodnow and Austin (1956)** and **Shepard, Hovland and Jenkins (1961)** ran classic rule-learning studies on logically defined categories. Some Boolean concepts are much harder than others. Not opened (a32).
- **Fodor (1975)**: thought is a compositional symbolic code. No numbers (a30).
- **Feldman (2000)**, Nature 407:630-3: the first strong quantitative law. Across **41 mathematically distinct Boolean concept types in six families**, subjective difficulty was proportional to Boolean complexity, the length of the shortest equivalent propositional formula (d17, abstract only; N and correlation not read, full text paywalled).
- **Lafond, Lacouture and Mineau (2007)** re-tested this and reportedly found shortest-formula length does not fully predict difficulty (b09, snippet only, unverified).

### 2.2 Rational Rules (Goodman et al. 2008)

A concept is a formula in disjunctive normal form from a grammar. The prior falls with formula length. The likelihood has an outlier parameter b. One free parameter overall. Fit to the Medin and Schaffer (1978) category structure, with human data from the Nosofsky et al. 1994 replication: **R2 = 0.98** for Rational Rules (one free parameter), 0.98 for RULEX (nine free parameters), 0.96 for the context (exemplar) model (a07). Individual patterns: if each person holds **one formula sampled from the posterior**, the model explains **36 individual generalisation patterns at R2 = 0.83** (Nosofsky et al. 1994 Experiment 1, a08). The prototype item (T3 = 0000) is the most likely transfer item classed as category A, with no prototype mechanism. The authors call strictly deterministic single-rule use troubling given graded typicality within individuals (a08). Caveats: the conference version was read, not the journal paper; DNF is assumed in advance; fits are on group averages.

### 2.3 Number words as bootstrapping (Piantadosi, Tenenbaum, Goodman 2012)

The question: children are 1-knowers, 2-knowers, 3-knowers (maybe 4), then abruptly learn all counting words around age 3;6. Carey (2009) explains the jump by analogy (a31, second-hand). The model gives a program-learning account (a01-a06, b01-b03):

- The hypothesis is a lambda-calculus program over primitives: singleton?, doubleton?, tripleton?, set operations, logic (and, or, not, if), next/prev on the count list, and a recursive call L. The space is infinite.
- Search is MCMC over 1 to 1000 data points. Data are number-word frequencies from CHILDES (children aged 20 to 40 months), power-law frequency, counted including non-numerical uses such as "give me one".
- Prior: rational-rules style, rewarding reuse, penalising length, plus an extra penalty (parameter c) on recursive lexicons. Noise a = 0.75 in the reported run.
- Result: the learner goes through 1-, 2-, 3-, (4-) knower stages and then jumps to the recursive CP rule. The jump happens when enough data finally pays for the longer recursive program (a04).
- **Mod-5 control**: relabel the data with a mod-5 number system and the same model learns Mod-5, after the same subset stages. Natural number is not hard-wired (a05). Mod-N was deliberately left out of the language and special MCMC proposals were needed.
- **Free parameter problem**: with no recursion penalty the jump comes roughly after the 1-knower stage (too early). With log c = -100 the model stays a 4-knower for a long time (a02). Timing is not predicted.
- Removing doubleton and tripleton primitives makes the jump earlier; adding quadrupleton and quintupleton delays it (b02). Informal manipulations, no systematic sweep.
- Untested prediction: a child who hears only the first three number words would never make the jump (a06).
- Critics: Rips, Asmuth and Bloomfield (a modular number system fits the same data); Asmuth and Rey (the model recombines existing primitives and creates nothing new). Not opened (a06, b03).

Status: an existence proof, qualitative fit, no fit statistic. No new child data have tested it. Contested.

### 2.4 Logical primitives of thought (Piantadosi, Tenenbaum, Goodman 2016)

Which logical connectives are primitive in the mental language? Design logic: if "red OR square" is easier than "red XOR square", XOR is not primitive; difficulty tracks description length in the mental language (a12). The experiment: 108 concepts, **1,596 participants** (Mechanical Turk), about 20 per concept and list, two lists per concept, 25 labelled sets each; alien word "wudsy" (a09). Overall accuracy **78% vs chance 56%**. Cross-list reliability R2 = 0.81. 3.9% of data removed on average (SD 2.6%).

Model comparison (a10, a11, b04, b05):

- Best grammar FULLBOOLEAN explains about **88% of variance** in held-out response patterns. The EXEMPLAR model explains only about **half**.
- FULLBOOLEAN beat IMPLIES, HORNCLAUSE, NAND, NOR significantly (Wilcoxon, Bonferroni, p<.05), but **not** BICONDITIONAL, CNF, DNF or SIMPLEBOOLEAN. The top grammars cannot be separated. Held-out likelihood gap to the nearest competitor: about 8 points.
- Adding iff (biconditional) helped; XOR-type concepts such as "red XOR circle" account for most of the iff advantage. Horn-clause form, common in AI, did several hundred log-likelihood points worse.
- A uniform prior with no simplicity bias is the next worst model.
- Quantifier concepts fit worse: about 66% of response variance, 78% of concept-mean difficulty (b04).
- Written descriptions at sets 5, 10, 25 were too ambiguous to analyse; the authors take that as mild evidence people do not hold the concept as an English sentence (a09).
- Individual people switch sharply between rules while the group average looks graded (b06; visual evidence only). Early rules are simplified approximations of the target.
- One run took about 50 processor days.

### 2.5 Programs for perception and generation (Lake et al. 2015)

Bayesian Program Learning: a handwritten character is a generative program of strokes, parts and relations. One example is parsed into a program, then used to classify and generate (a13, a14). One-shot classification among 20 characters: people 4.5% error (N = 40), BPL 3.3%, deep convnet 13.5%, deep Siamese convnet 8.0%, Hausdorff 38.8%. Lesions: no learning-to-learn 11.0%, no compositionality 14.0%. Visual Turing test: 147 judges identified the machine at 52% (t(47) = 2.03, P = 0.048; only 3 of 48 judges reliably above chance). Lesion without learning-to-learn: 80% identified; without compositionality: 65%; dynamic version (N = 143): 59%. Limit: hand-built stroke grammar for one domain.

### 2.6 Machine program induction (DreamCoder, 2020-2021)

Wake-sleep program learning (a17, a18, b10, b11, c11):

- Wake: search for programs that solve tasks, guided by a neural recogniser.
- Abstraction sleep: compress solutions into new library functions.
- Dreaming sleep: train the recogniser on programs sampled from the library.
- Text editing: 128 training tasks, 108 SyGuS 2017 test problems. **3.7% solved before learning, 79.6% after** (mean solve time 235 s to 40 s). CVC4 82.4% (1 hour, 8 CPUs); DreamCoder 84.3% at that budget.
- List processing: 218 problems, about 20 new routines; it rediscovered filter, then max, nth largest, sort. Physics: 93% of 60 laws after 8 cycles. LOGO and towers: nearly 100% held-out vs no ablation above 60%.
- Costs: about a day on 20-100 CPUs; needs 100+ training tasks per domain and a hand-set starting primitive set; no natural language.
- Ablations (five runs, 20 wake-sleep cycles): no recogniser or no abstraction solves fewer; memorising solved programs without compression is worse.

### 2.7 Hacking, not just shortest-program (Rule, Tenenbaum, Piantadosi 2020)

The dominant LoT proposal is "balance simplicity and fit by Bayes or MDL while stochastically sampling programs". The "child as hacker" paper argues learners also **revise** code for many values (speed, clarity, reuse, memory) with many operations (add function, debug, refactor, memoise). Worked example: sum-to-min strategy in early addition; children keep several strategies at once (a29). Opinion piece, no new data. Rule et al. 2024 turned it into a model (section 4.6).

### 2.8 The LLM turn (2023 on)

- **Wong et al. 2023 "From word models to world models"** (a26, b26): an LLM translates sentences into probabilistic programs (Church) and the program engine reasons. Four domains shown qualitatively; no benchmark numbers (one worked case: a 23.90% chance drops to 0% after a contradiction).
- **Ellis 2023** (a19, b18, c09): the LLM is the proposal distribution over English concepts, a tuned prior reweights, Bayes picks.
- **Hypothesis Search** (Wang et al. 2024) and **Phenomenal yet Puzzling** (Qiu et al. 2024): the LLM proposes rules, code checks them (section 6).
- **ARC**: Chollet's Abstraction and Reasoning Corpus is the main bench. Humans solve it by inferring a hidden program (Johnson et al. 2021, a15). Machine entries mostly sample programs (Greenblatt) or predict grids (transduction).

---

## 3. Core findings with exact numbers

Status: established = two or more independent papers agree; single = one paper; contested; open = no evidence found. Cells give the condition. Claim ids in brackets.

### 3.1 Human studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Rule-based concept learning is well fit by Bayesian inference over short formulas | R2 = 0.98 (Rational Rules, 1 free parameter) vs 0.98 RULEX (9 parameters), 0.96 context model | Goodman et al. 2008 (a07) | established [K01] |
| One sampled rule per person explains individual patterns | R2 = 0.83 on 36 individual patterns | Goodman 2008 (a08); Piantadosi 2016 (b06, visual only) | established [K02] |
| Structured logic grammars beat exemplar models | 88% of held-out variance (FULLBOOLEAN) vs about 50% (exemplar); N = 1,596, 108 concepts; accuracy 78% vs chance 56% | Piantadosi 2016 (a09, a10, b04) | established [K01] |
| Richer connectives than and/or/not fit better (iff) | FULLBOOLEAN beats Horn clause, NAND, NOR, IMPLIES (p<.05); not BICONDITIONAL, CNF, DNF, SIMPLEBOOLEAN | Piantadosi 2016 (a10, a11) | single (resolution limit) |
| Quantifier concepts fit worse | about 66% of response variance, 78% of concept-mean difficulty | Piantadosi 2016 (b04) | single |
| Difficulty of Boolean concepts is proportional to shortest-formula length | 41 concept types, 6 families (N, r not read) | Feldman 2000 (d17) | single (abstract only); Lafond 2007 disputes (snippet) [K04, K28] |
| Staged number-word learning arises from data volume alone | stages 1-, 2-, 3-, (4-)knower, then jump; Mod-5 data learned Mod-5; timing set by log c | Piantadosi 2012 (a01-a05) | single [K03]; contested [K04] |
| One-shot stroke-program learning matches people | error 3.3% (BPL) vs 4.5% (people, N = 40) vs 13.5% (convnet); judges 52% identification (N = 147) | Lake 2015 (a13, a14) | single (one domain) |
| People infer ARC programs quickly | 83.8% per task (SD 16.7), 95 people, 40 tasks, 3 attempts; hardest task 38.1%; longer description, b = -0.17, CI [-0.315, -0.020], p = 0.03 | Johnson et al. 2021 (a15) | single |
| Humans on ConceptARC | humans about 91% vs GPT-4 25% vs best program 52%; per concept humans 0.83-0.97, GPT-4 0.13-0.63; 16 concepts, 480 test inputs | Moskvichev 2023 (b23); Mitchell 2023 (c18) | established [K13] |
| 88% of ARC tasks can be passed on by language alone | best synthesiser given descriptions: 22 of 183 test tasks (12%); language alone at most 1 task | Acquaviva et al. 2022 (a16) | single |
| Human list-function learning | 392 people, 100 functions; mean accuracy 0.521 (CI 0.479-0.559), range 0.042-0.868; 54% of functions acquired by half of learners within 8 trials; 50% of functions acquired by someone after one trial, 99% within eight; only 2% by all | Rule et al. 2024 (c19, c25) | single (second sample replicated; supplement not read) |
| Children find the blicket in 2 trials | 3-4 year olds, ACRE | Gopnik 2001; Sobel 2004 as cited by Qiu (a23) | second-hand |

### 3.2 Program induction by machines before LLMs

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Library learning in a closed domain | text editing 3.7% to 79.6% (108 tasks); CVC4 82.4%; physics 93% of 60 laws; LOGO/towers near 100% vs below 60% for ablations | DreamCoder (a17, b10, b11, c11) | single paper [K12] |
| ARC program-synthesis ceiling before LLMs | Icecuber DSL 20% private (2020); 43% on the 100-task Hypothesis Search sample; 49% for an ensemble of 2020 entries | ARC Prize 2024 (c16); a20 | established |
| Synthesisers on human language descriptions | at best 12% of 183 test tasks | Acquaviva 2022 (a16) | single |
| Kaggle program winner vs humans | 57.5% on the 40 human tasks (21% hidden test set); Spearman with humans 0.35 | Johnson 2021 (a15) | single |

### 3.3 LLM and AI studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hypothesis then program beats direct answering (ARC, 100 tasks, GPT-4) | direct 17%; program only 23%; summarised hypotheses 30%; human-selected 33%; human-written LARC hypotheses 45%; Icecuber 43%; language-only hypotheses 19% | Wang 2024 (a20, b12, b13, c01) | established with Qiu [K05] |
| Same pipeline on easier sets | 1D-ARC (108): direct 39.6, program 61.1, full 73.1. List Functions (100): 31, 59, 69. SyGuS (89): CrossBeam 74.8, GPT-4 program 94.3, full 94.3 | Wang 2024 (c03) | single [K06, K07] |
| Hypothesis generation is the bottleneck | GPT-4 correct hypothesis on 49 of 100 ARC tasks; 33 of 49 (67%) correct program; 28 of 30 summarised-hypothesis wins had a correct hypothesis | Wang 2024 (c02, b12) | single [K08] |
| Propose-test-refine with a symbolic interpreter | task acc IO vs best refinement (T=3, N=5): ACRE 28.0 vs 59.0; MiniSCAN 0.0 vs 70.0; List Functions 39.6 vs 52.4; MiniARC 13.8 vs 14.6 (raw 33.1 vs 18.7) | Qiu 2024 (c05, a22, d14) | established [K05] |
| LMs cannot apply their own rules | MiniSCAN about 85-93 task acc with symbolic interpreter vs 0.0 with LM interpreter; MiniARC 14.6 vs 5.4; self-refine (LM interpreter) ACRE 32.0, MiniSCAN 0.0 | Qiu 2024 (c06, a22) | established with Ellis [K09] |
| Raw vs task gap | IO raw/task: ACRE 64.0/28.0; MiniSCAN 61.7/0.0; List 65.1/39.6; MiniARC 33.1/13.8. Refinement T=1,N=1: ACRE 78.2/45.0; MiniSCAN 46.3/0.0; List 67.4/52.0; MiniARC 5.9/3.8 | Qiu 2024 (d14) | single |
| Refinement fails on MiniARC | raw IO 33.1, SC(N=5) 31.3, SR 15.1, refinement 5.9 (T1N1), 12.8 (T1N5), 10.1 (T3N1) | Qiu 2024 (d15) | single [K06] |
| Noise and unfamiliar symbols hurt LMs | 12.5, 25, 50% of 8 outputs perturbed: accuracy falls steadily; one noisy example already hurts | Qiu 2024 (c07, a23) | single [K15] |
| Fit to examples only can overfit | MiniSCAN T=3,N=1 beat T=3,N=5 | Qiu 2024 (c08) | single observation |
| Induction and transduction complement | ensemble 56.75% on ARC validation (2 tries) vs average human 60.2%, best human 97.8%; later 61.9% (Akyurek); induction 18.78% vs transduction 15.25% in one setting, 11.07% vs 13.50% in another; ensembles 26.50%, 19.50%; ARC-Heavy: transduction+TTT 43.25, induction 19.25 | Li et al. 2024 (a24, b16, c14, c15) | established [K06] |
| Program samples that pass examples can be wrong | about 9% false positives (fine-tuned 8B); about half of affected problems still have the right majority answer | Li 2024 (a25, b17, d13) | established with Qiu overfitting [K11] |
| Models beat humans on the hardest 20% of ARC problems, trail on the easiest 20% | five difficulty tiers | Li 2024 (a25) | single |
| More samples help, log-like | Greenblatt GPT-4o: 1024 samples 25% (V0), V2 30%, V2 at 2048 34%, ensemble of 4 before revision 37%, with revision 50% (SE about 5); about 3 points per doubling; ARC Prize report 42% public | Greenblatt blog (d05); ARC Prize (c16) | established [K10] |
| K and diversity curve | GPT-4o-mini avg accuracy baseline/concept-first: K=4 36.1/39.7; 8 39.2/43.7; 16 42.7/47.1; 32 45.4/47.8; 64 49.0/53.6; 128 54.4/54.7; 256 55.0/59.8. 16 concepts x 2 at K=32: 52.0 | Lee 2025 (d11, c22, d12) | single [K17, K22] |
| One-shot code writing is weak; search carries the gain | ARC-test one-shot: Qwen-Coder 7B 1.0, 14B 1.0, 32B 1.5; GPT-4.1 8.0; Claude-4-Sonnet 20.75; o3-mini 38.25. Sample-6k / Sample&Refine-6k / SOAR-6k: 14B 5.63/14.25/36.25; 32B 12.63/19.87/42.75; GPT-4.1 19.75/26.25/45.50 | Pourcel 2025 SOAR (d06) | established with Greenblatt [K24] |
| Reasoning model with propose-code-run loop | ARC-AGI-1 100-puzzle val, official 2 attempts: o4-mini 55.17 (SD 3.18), Claude Sonnet 4 thinking-16k 54.17, DeepSeek R1 26.33, Qwen3-235B 16.67, Gemini 2.5 Flash thinking-16k 13.83; Oracle@1 46.33 (SD 1.04) | ArcMemo (d08) | single harness [K05, K21] |
| Direct-grid reasoning models on ARC-AGI-1 semi-private | o3 (high) 60.8% at $0.50; o3-pro 59.3% at $4.16; o4-mini (high) 58.7% at $0.406; Claude Sonnet 4 thinking-16k 40% at $0.366; Opus 4 thinking 35.7% at $1.25; Gemini 2.5 Pro 33.0%; DeepSeek R1 21.2%; GPT-4.1-nano 0% | ARC Prize leaderboard (d04), via summarising fetch | single, no tokens [K21] |
| Single-pass frontier baselines 2024 | public/semi-private pass@1: o1-preview 18/21, Claude 3.5 Sonnet 14/21, Gemini 1.5 5/9; Greenblatt 43/42; Berman 53.6/58.5; ARChitects 53.5% private; MindsAI 55.5% (not eligible) | ARC Prize 2024 (c16, c17) | established |
| Cost lever is parallel samples | o3: 1,024 samples, 5.7B tokens/100 tasks, 87.5% ARC-AGI-1; 6 samples, 33.5M tokens, 75.7%. ARC-AGI-2: Berman 79.6 to 29.4, Pang 77.1 to 26.0 (2.5-3x drop) | Vahdati 2026 survey (d02, d03, d18) | single, secondary [K25] |
| Spread inside a paradigm exceeds gap between paradigms | induction 2% to 79.3% (SD 27.4) vs about 15 points between paradigms; systems run on all 100 tasks average 38.8% vs 65.6% for subsets under 100 (inflation) | Vahdati 2026 (d01) | single, secondary |
| Library learning with an LLM | LILO over DreamCoder: +33.14 REGEX, +20.42 LOGO, +2.26 CLEVR (DreamCoder 94.50). LLM solver alone vs DreamCoder: +32.20, +3.60, -5.83 CLEVR. Unnamed abstractions: -30.60 REGEX, -2.91 CLEVR, -11.11 LOGO; AutoDoc recovers +9.73, +2.27, 0.00. LLM as compressor: 19.01% (998 of 5250) valid. One LLM round about 48 CPU-hours of DreamCoder search | Grand 2024 (a27, b20, b21, c12, c13) | contested [K12] |
| Library reuse is rare in LLM systems | LEGO-Prover: over 20,000 lemmas, 1,233 (6%) in prompts, one reused once. TroVE: 15 functions, 3 reuses in 3,201 questions | Berlot-Attwell 2024 (a28, d10) | contested [K12, K26] |
| Concept memory on ARC | ArcMemo: +4.2 points official; PS 59.33 vs 55.17 no memory; OE 56.67; cheatsheet 57.67; benefit shrinks with compute; tokens equal or higher | Ho 2025 (d08, d09) | single [K26] |
| Rule library from training | +10-30% over CoT; CLUTRR +11.1 to +16.4; GPT-3.5 CoT +27.2 with GPT-4 rules; wrong rules cause 65% and 81% of baseline errors | Zhu 2024 HtT (c21) | single [K20] |
| LLM as concept proposer fits human learning | Number game R2 = 0.95 (8 humans, tuned prior); shape/logic concepts (112 concepts, 1,596 humans) R2 = 0.81 with 100 proposals, within 3% of human accuracy; GPT-4 alone fits worse | Ellis 2023 (a19, b18, c09) | single |
| Ellis held-out new concepts | majority-colour: model 2 batches, humans fast; minority-colour: model 4, humans 3; N = 16 | Ellis 2023 (c10) | single, tiny |
| Input representation | GPT-4 13/50 text grids to 23/50 object-based on easiest ARC; 81/400 best representation; text-davinci-003 85 solved of 800 vs 44-46 with random alphabets | Xu 2024 (b24, d16); Mirchandani 2023 (b22) | established, old models [K14] |
| Code plus simulated lines | BIG-Bench Hard: text-davinci-003 Direct 55, CoT 72, CoC 84; PaLM 2-S 49, 61, 78; GPT-4 CoC 91 | Chain of Code (c23) | single [K18] |
| Metaprogram revision for list functions | MPL at 5K steps reaches 84% of its 500K rate; closer to human than Fleet (V = 874, p<.001, effect 0.39); Codex one function per trial matched 25th-percentile humans | Rule 2024 (c19, c20) | single [K16] |
| Language into probabilistic programs | qualitative only | Wong 2023 (a26, b26) | single, no numbers [K19] |
| Co-training to instill human bias | language-grounded meta-RL agent beat baseline on human-like boards, worse on control boards (p<.0001) | Kumar 2023 (b25) | single (small neural agents) |
| Concept-first diversity | +3.3 to +5.0 average accuracy (GPT-4o-mini +4.5, Llama-3.1-70B +5.0); unique hypotheses of 8 rise +0.37 to +1.00 | Lee 2025 (c22) | single [K17] |

Note on c01 versus a20: a20 and b12 list human-selected hypotheses at 33%; c01 gives human-written LARC hypotheses at 45%; critique.md confirms 45 for human-written.

---

## 4. Mechanisms and models

Each model is written so an engineer could build it.

### 4.1 The generic program-induction learner

Inputs: examples E (input-output pairs or labelled items); a grammar G of primitives.

1. **Hypothesis space** H: all programs derivable from G.
2. **Prior** P(h): product of production probabilities in G. Longer programs get lower prior (each extra symbol multiplies by a number below 1). This is the simplicity bias. Kolmogorov complexity fixes simplicity only up to a constant, so the choice of primitives matters (a12).
3. **Likelihood** P(E | h): a noisy-match term. If h(x) = y the probability is high; otherwise low (noise a, or outlier b in Rational Rules). In the number model an incorrect prediction has likelihood (1-a)/N.
4. **Posterior** P(h | E) proportional to P(h) P(E | h).
5. **Search**: MCMC (propose subtree edits, accept by posterior ratio); enumeration; or an LLM that proposes h.
6. **Predict**: use the single best h (MAP), sample one h per learner (the human-like "one rule at a time"), or average predictions over many h.

### 4.2 Rational Rules (Goodman et al. 2008)

Concept = DNF formula built by a grammar (a disjunction of conjunctions of feature tests). Prior falls with length. One parameter b for outliers. Predict a new item by the posterior probability that it satisfies the concept. For individual simulation: sample one formula per simulated person. R2 = 0.98 group, 0.83 individual (a07, a08). Build hint: restrict the grammar to feature-equality tests; use MCMC with subtree regeneration.

### 4.3 Bootstrapping number model

Same learner, with a recursive primitive L and a count list. The stage structure falls out of description length vs fit: a subset-knower rule is short but fits only some data; the recursive rule is longer but fits all. With enough data the posterior flips. The flip point is set by the recursion penalty c: moving it between 0 and log c = -100 moves the jump from "after 1-knower" to "after 4-knower" (a02). Treat the flip timing as a tunable, not a prediction.

### 4.4 Logic-primitive comparison (Piantadosi 2016)

Run the same learner under different grammars. Score each grammar by held-out likelihood of human response patterns. The learner is memory-limited (it forgets examples). Result: FULLBOOLEAN (and/or/not/iff plus normal forms) fits best with a simplicity prior; no-simplicity prior is worse (a10).

### 4.5 DreamCoder wake-sleep

Loop per cycle: (1) wake: for each task, enumerate programs in order of prior x recogniser score until time-out; keep solutions. (2) abstraction sleep: refactor solved programs to find shared fragments, add the best fragment as a new named primitive if it shortens the whole set. (3) dream sleep: sample programs from the library, run them to make synthetic tasks, train the recogniser to map task to likely program. Needs a task set and a runnable DSL (a17, a18). LILO replaces enumeration with an LLM, uses Stitch for compression and an LLM auto-documentation step that gives names and docstrings (a27, c13).

### 4.6 Metaprogram search (Rule et al. 2024)

A metaprogram is a program that edits a program (add, delete, replace a subtree, wrap in a conditional). Search moves through program space by applying metaprograms to the current best hypothesis rather than sampling anew. At 5K steps MPL reaches 84% of its 500K-step acquisition rate and fits human trial-by-trial learning better than Fleet (V = 874, p<.001) (c19). 82.8% of metaprograms are at least as simple as their programs. Weakness: recursive problems solved with recursion in only 34.4% of MPL runs vs 97.0% for non-recursive. For an LLM agent this is S5 REVISE: edit the failing hypothesis using the failing output instead of resampling.

### 4.7 LLM-as-proposer pipeline (Hypothesis Search / Qiu / Ellis)

1. Show the examples. Ask for K distinct natural-language hypotheses (Wang: 64, summarised to 8; Qiu: T = 1 to 3 iterations with N = 1 to 5 rules).
2. For each, ask for a program implementing it.
3. **Run the program on every example** with an interpreter. Do not let the model apply its rule in prose (c06, d14).
4. Keep programs that pass all examples. If none, feed failing cases back and revise (Wang: 3 rounds of execution feedback; Greenblatt: about 3,040 revision samples per problem, only where fewer than 32 programs pass).
5. Select: majority output over passing programs; or prior x fit as in Ellis with a learned prior over English hypotheses.

Ellis (2023) uses about 50-100 proposals and a learned prior. The pretrained prior alone is syntax-sensitive; the tuned prior mattered most for complex logic concepts (a19, c09).

### 4.8 Induction-vs-transduction router

The induction model writes a program; the transduction model outputs the grid. Run induction first. If a program passes all training pairs, use it. Otherwise fall back to transduction. Li et al. 2024 describe this exact rule and note the split is stable across seeds (d13, c14).

### 4.9 Diversity-first proposing (Mixture of Concepts)

Step A: ask for a list of K distinct high-level concepts. Step B: for each concept, ask for one hypothesis. This beats IID repeated sampling at small K (K = 4 to 16: +3.6 to +4.5); the gain vanishes at K = 128 (d11). Concept-stage tokens were not charged to K.

---

## 5. What holds up

### 5.1 Held up

- **Short executable rules fit human rule learning.** Two independent papers (Goodman 2008, Piantadosi 2016) and Feldman's law agree (K01). Boundary: group averages, labelled shape and Boolean tasks, mostly Mechanical Turk.
- **A simplicity bias matters.** The no-simplicity prior is worse (a10); human ARC difficulty rises with description length (a15, b = -0.17, p = 0.03).
- **Propose, execute, check beats direct answering on 2023-era LLMs.** Hypothesis Search (a20) and Qiu et al. (a22) agree in direction on ARC, 1D-ARC, List Functions, ACRE and MiniSCAN (K05). Different teams, different datasets.
- **Execution beats simulation.** MiniSCAN task accuracy 0.0 with the LM as interpreter vs 46-70+ with a symbolic one. LM-as-interpreter variants never helped (self-refine ACRE 32.0 vs IO 28.0; MiniSCAN 0.0) (c05, c06).
- **Search is what makes program writing work.** One-shot program writing is low even for strong models (GPT-4.1 8.0, Claude-4-Sonnet 20.75, o3-mini 38.25). Sample plus refine adds a lot (GPT-4.1 19.75 sampling, 26.25 with half-refinement, 45.50 with SOAR) (d06). Greenblatt: about 3 points per doubling (d05) (K10, K24).
- **Induction and transduction complement each other.** Stable per-problem split across seeds (K06).
- **Humans were ahead on ARC-like induction through 2024.** 83.8% per task (a15); ConceptARC 91% vs GPT-4 25% (K13). The 2026 survey reports much higher machine scores (Opus 4.6 93.0% on ARC-AGI-1, 68.8% on ARC-AGI-2, d03), reached with heavy test-time compute.

### 5.2 Failures, contests and moderators

- **Number-word bootstrapping.** Free recursion-cost parameter, hand-picked primitives, no new child data, rivals (Carey analogy, Rips modular number) stand (K03, K04). Do not build on it.
- **Shortest-formula law.** Lafond et al. 2007 reportedly find length does not fully predict difficulty (b09, snippet). Rival complexity measures claim better fit. Unverified. Feldman's own N and r not read.
- **Grammar identification.** The 2016 study cannot separate the top grammars (a10). "Which primitives" is answered only to that resolution.
- **Rule-per-person vs graded averages.** The individual-switch evidence is visual (b06). A rule model can mimic gradients by averaging over rules; hybrid rule + exemplar models (Nosofsky) are not ruled out (b05). Goodman et al. call deterministic rule use troubling given within-person typicality (a08).
- **Refinement hurts on MiniARC.** IO raw 33.1 vs refinement 5.9-18.7. The explanation (pattern matching suits direct prompting, grids read poorly, a multimodal model did worse) is a guess (d15). Hypothesis Search says the language step matters only when the concept is hard to state as code (SyGuS 94.3% either way; language-only 19% below programs 23%) (K07). Both say "task-dependent"; neither explains why.
- **Hypothesis-step gain varies by set.** ARC +7 (23 to 30), 1D-ARC +12 (61.1 to 73.1), List Functions +10 (59 to 69), SyGuS 0.
- **Language hypotheses without code.** 19% on ARC, below programs alone (23%) (b13).
- **False accepts.** About 9% of passing samples are wrong (fine-tuned 8B); majority vote fixes about half of affected problems (K11, K23). In MiniSCAN T=3,N=1 beat N=5 (overfitting to exemplars). No 2025-2026 rate exists.
- **Noise brittleness.** One perturbed example in eight already hurts LMs; a warning in the prompt only partly fixes it (a22, c07).
- **Library learning is contested.** DreamCoder and LILO show big gains in closed domains. LILO's own re-run of DreamCoder (28.53) fell below the LAPS-reported 42.64 (b20), so the baseline is soft. An LLM as compressor produced only 19.01% valid abstractions; unnamed abstractions hurt (-30.60 REGEX) until documented. Berlot-Attwell finds near-zero literal reuse (1 reuse in LEGO-Prover; 3 in 3,201 TroVE questions) and gains better explained by self-correction and self-consistency. Part of the conflict is what counts as reuse: function calls (near zero) vs idea-level hints (ArcMemo +4.2 official, shrinking with compute, tokens not reduced) (K12, K26). Berlot-Attwell used weak models and a 12-problem ablation.
- **Diversity prompting.** Gain +3.6 to +4.5 at K = 4-16, +0.3 at K = 128. Greedy decoding shows no significant gain. Authors read the gain as more diverse hypotheses, not better reasoning (d11, d12). Temperature above 1.33 gave no extra diversity (c22).
- **Refinement vs sampling.** With GPT-4o-mini iterative refinement did not beat plain sampling; with GPT-4o it did (d12). In SOAR half sampling plus half refinement beat all sampling at every size (d06). Weak models may not benefit.
- **Search plateaus.** The gain is logarithmic and bounded by the base model; SOAR plateaus with budget and size when the model is not updated (d07). No true knee found.
- **Difficulty collapse.** All paradigms drop 2.5-3x from ARC-AGI-1 to ARC-AGI-2 (d03, d18).
- **Benchmark inflation and noise.** Systems run on all 100 tasks average 38.8% vs 65.6% for under-100-task subsets (d01). Hypothesis Search used 100 random tasks; Greenblatt SE about 5; ArcMemo SD up to 3-5 points.
- **Contamination.** Mirchandani note possible ARC contamination in training data (b22).

**Interventions that worked.** An executable check. Hypotheses in words when code is hard (ARC, 1D-ARC, List Functions). Object-structured input for GPT-4 (13 to 23 of 50). Diversity prompts at small K. Routing induction then transduction. Naming and documenting abstractions (LILO). Targeted revision (Rule 2024). Verified rule libraries (HtT +10-30%).

**Interventions that did not.** LM as its own interpreter. Plain majority vote (helped less than hypothesis selection, a22). Language hypotheses without code (b13). Refinement on MiniARC. LLM-written abstractions without checks (19.01% valid). Unnamed abstractions. Parsel decomposition with model hypotheses (hurt; 47.5% only with human hypotheses, b13).

---

## 6. Language models

### 6.1 What models do on their own

- GPT-4 alone judges the number game "decidedly different from human averages" and scores below the Bayesian wrapper on shape concepts (b19, a19). Different is not wrong there (no ground truth).
- Text LLMs complete abstract token patterns in context even with arbitrary token alphabets (Mirchandani 2023): text-davinci-003 solved 85 of 800 ARC problems, but only 44-46 with random alphabets; text-davinci-002 64; GPT-4-0613 77; PaLM 42; hand-built DSL search 130 (b22). Numbers are not matched across models.
- GPT-4 reads flat text grids poorly: 13/50 simplest tasks; 23/50 with object description; 81/400 on the training set with the best representation (b24, d16).
- Frontier models in 2024 score low without search: o1-preview 18%/21% (public/semi-private pass@1), Claude 3.5 Sonnet 14%/21%, Gemini 1.5 5%/9% (c17).
- ConceptARC: GPT-4 per concept 0.13-0.63 vs humans 0.83-0.97; Count 0.13 vs 0.86; Order 0.60 vs 0.95. Minimal tasks (48): humans 0.95, GPT-4 0.69 (T = 0) and 0.65 (T = 0.5), GPT-4V 0.25 zero-shot and 0.23 one-shot (c18).
- 2025 direct reasoning models: o3 (high) 60.8% at $0.50 per task; o4-mini (high) 58.7%; Claude Sonnet 4 thinking-16k 40%; Gemini 2.5 Pro 33.0% (d04). The 2026 survey lists higher numbers: Opus 4.5 37.6% on ARC-AGI-2 at $2.20, GPT-5.2 Pro 54.2% at $15.72, Poetiq Gemini 3 Pro refinement 54% at $30.57; GPT-5.2 Pro 90.5% and Gemini 3 Flash 84.7% on ARC-AGI-1 (d02). These are relayed by a secondary survey, and it does not say whether the models induce programs internally.

### 6.2 What changed the results, and by how much

| Change | Effect | Source |
|---|---|---|
| Write a program instead of the grid (GPT-4) | ARC 17 to 23; 1D-ARC 39.6 to 61.1; List Functions 31 to 59 | c04, a20 |
| Add a hypothesis step | ARC 23 to 30 (summarised), 33 (human-picked), 45 (human-written); 1D-ARC to 73.1; List Functions to 69; SyGuS 0 | a20, c01, c03 |
| Run code instead of letting the LM simulate | MiniSCAN 0.0 to 46-77 | c06, d14 |
| Propose-test-refine loop (GPT-4-era) | ACRE 28.0 to 59.0 task acc; MiniSCAN 0.0 to 70.0; List Functions 39.6 to 52.4 | c05 |
| More samples (GPT-4o) | about +3 per doubling to 2,048; 50% with about 8,000 samples plus revision (100-task test subset) | d05 |
| More hypotheses K (GPT-4o-mini) | 36.1 (K = 4) to 55.0 (K = 256); +0.6 from 128 to 256 | d11 |
| Concept-first diversity | +3.6 to +4.5 at K = 4-16; +0.3 at K = 128; +4.8 at K = 256; +6.6 for 16x2 at K = 32 | d11, d12 |
| Search plus refinement for a small open model | Qwen 32B one-shot 1.5 to 42.75 (SOAR-6k) | d06 |
| Reasoning-model base with code loop | o4-mini 55.17, Sonnet 4 thinking-16k 54.17, vs Gemini 2.5 Flash thinking-16k 13.83 in the same harness | d08 |
| Memory of abstract concepts | +4.2 official at standard compute; shrinks with compute; tokens equal or higher | d08, d09 |
| Object-structured input (GPT-4) | 13/50 to 23/50 | b24 |
| Induction plus transduction ensemble | 56.75% vs average human 60.2%, beyond either alone | a24 |
| Hybrid code plus simulation (Chain of Code) | text-davinci-003 CoT 72 to CoC 84; GPT-4 CoC 91 | c23 |
| Rule library (HtT) | CLUTRR +11.1 to +16.4; GPT-3.5 +27.2 with GPT-4 rules | c21 |
| LILO abstractions with documentation | +33.14 REGEX over DreamCoder; unnamed -30.60 | a27, c13 |

### 6.3 What is still missing

- **No equal-token comparison** of "propose K plus execute" vs plain extended reasoning on a current frontier model. ArcMemo gives same-harness propose-and-run numbers (o4-mini 55.17, Sonnet 4 thinking-16k 54.17; 100-puzzle validation subset). The leaderboard gives direct-grid numbers (o3-high 60.8%, Sonnet 4 thinking-16k 40%) on a different split and harness. Token counts exist only for o3 (5.7B vs 33.5M tokens per 100 tasks). The Sonnet 4 pair (54.17 in a loop vs 40 direct) hints that code loops help, but sets and harnesses differ (K21).
- ArcMemo reports token use "similar to the baseline" and memory runs raised output tokens (d09).
- Token costs of verification and of the concept stage are not reported (Lee, Hypothesis Search).
- Faithfulness: with direct prediction, correct raw answers often arrive without the intended rule (task accuracy far below raw). An interpreter removes the LM-as-interpreter failure; what is left (ACRE 78.2 raw vs 45.0 task at T1N1) is wrong rules plus a strict metric, not unfaithfulness (d14, K09).
- No LLM study uses the human one-rule-at-a-time result (K27). No LLM study ties shortest-formula length to model difficulty (K28).

---

## 7. What our agent should take

Marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Execute, do not simulate, the induced rule.** At S4 TEST, a candidate rule written as code is run by the harness on every example. The model never applies its own rule in prose. Part: S4, G2, G3. [E]. Evidence: c05, c06, a22, d14, K09 (MiniSCAN 0.0 with LM interpreter vs 46.0-70.0 symbolic).
2. **Propose several rules, then test, instead of answering directly**, on items that have a check (ARC-like, list functions, rule puzzles). Part: S2 (1 to 4 candidate rules, already in the schema), S3, S4. [E]. Evidence: a20, a22, c01, c05, d08, K05. Gain size depends on model and set (see Test first, T1).
3. **Pair every code proposal with a run-and-check step**; never rely on one greedy program. Part: S3, S4, G7. [E]. Evidence: d06, d02, d03, d05, K24.
4. **Do not trust a rule because it fits the given examples.** Keep the unfitted check of G3. When several passing programs disagree on a fresh input, vote or run the discriminating input. Part: G3, S7. [E]. Evidence: a25, b17, c08, d13, K11. The 9% false-accept rate is from fine-tuned 8B models: a reason for care, not a prediction for ours.
5. **Spend by difficulty and stop at the first pass.** Returns are logarithmic with no sharp knee up to K = 256. Part: G12, S3. [E]. Evidence: d05, d11, a25, K10, K22.
6. **Select by execution in code, not by a model judge.** Already G5; this subfield supports it (plain majority vote helped less than hypothesis selection, a22). Part: G5, S7. [E]. Evidence: a22, d09.
7. **Report headroom against the human mean** when judging items of this kind (83.8% per task on ARC-style tasks; 60.2% average human on ARC validation). Part: bench reporting. [E]. Evidence: a15, b23, a24, K13.

### Test first

8. **Induction first, transduction fallback router.** Run the program route; if no program passes the demonstrations, answer directly. Part: S0 and S3 (mode choice). [E for complementarity in fine-tuned models; untested on prompted frontier models]. Evidence: a24, b16, c14, c15, d13, K06.
9. **Add the hypothesis-in-words step only where code fails or the concept is perceptual.** Part: S2, S5. [S]. Evidence: a21, b13, c03, K07.
10. **Diversity-first proposals** (list K distinct concepts, then one hypothesis per concept). Part: S3 in checked mode. [S]. Evidence: c22, d11, d12, K17. Weak models only; concept-stage tokens uncounted.
11. **Object-structured S2 representation** (objects, counts, regions, symmetry parsed by code). Part: S2, O6. [S]. Evidence: b24, d16, K14. GPT-4-era only.
12. **Targeted revision of the failing hypothesis from a named failing output** vs blind resampling. Part: S5, G2. [S]. Evidence: c19, a29, d06, d12, K16.
13. **Noise-tolerant fit** (accept a rule that fits all but k examples, flag as approximate). Part: G3, S4. [S]. Evidence: a22, c07, K15.
14. **Commit to the best-passing program vs blend answers by vote.** Part: S3, S7. [S for humans; open for LLMs]. Evidence: a08, b06, d13, K02, K27. No LLM study.
15. **Memory of named, documented concepts** offered by similarity on a later batch, with a no-memory control and a reuse counter. Part: memory (subgoal library). [C]. Evidence: a27, c13, a28, d10, d08, d09, c21, K12, K20, K26. Best-supported form: idea-level hints and documented abstractions, not literal function reuse (near zero).
16. **Hybrid execution** (run code, let the model simulate only the unrunnable lines). Part: S4. [S]. Evidence: c23, K18. Old models.
17. **Rule length as a difficulty gate** (length of the model's shortest rule feeds S0 and G12 spend). Part: S0, G12. [S, human only]. Evidence: a15, d17, K28. No LLM test.

Not to take: number-word bootstrapping (K03, K04); word-to-probabilistic-program translation as a reasoning tool (K19, no numbers); debate (G9).

---

## 8. Concrete tests on our bench

Rules for all: both arms get the same total tokens (setup, proposals, feedback and every extra stage counted); at least 50 items (100 for effects under 5 points); 3 seeds; paired on the same items; report tokens per arm.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 50 ARC-style grid items plus 50 list-function items | A: plain extended reasoning, direct answer. B: propose K = 4 hypotheses in words, code each, run on demonstrations, pick survivor, same token cap | Exact-match solve rate; tokens; false-accept rate on a held-out pair | B above A by 5-15 points on list functions; sign on ARC unknown for a current model |
| T2 | Same items split by type (exact computation vs fuzzy perceptual: count, shape, symmetry) | A: program route only. B: direct only. C: program first, direct fallback if no program passes | Solve rate by type; fallback rate | C at least equal to the better arm on both types; gain over best single arm 3-8 points |
| T3 | Items with a check; K sweep | K = 1, 2, 4, 8, 16, stop on first pass, with and without concept-first diversity | Solve rate vs tokens; knee; diversity gain | Log-like curve; diversity +3 to +5 at K = 4-16, near zero by K = 64 |
| T4 | 50 items where a program fits all demonstrations | A: accept first passing program. B: hold out one demonstration and require a pass. C: vote across up to 5 passing programs | False-accept rate; solve rate; tokens | B or C cuts false accepts by about half from a baseline near 9%; if the baseline is already low, headroom is small |
| T5 | Items answerable in two forms | A: model applies its rule in prose. B: harness executes the rule | Rule-application error rate | B well below A (MiniSCAN-size gap on complex rules; small on simple lists) |
| T6 | Sequential 100 items | A: no memory. B: named, documented abstractions from earlier solves, offered by similarity after the first attempt. C: idea-level hints only | Solve rate on later items; verbatim reuse count; idea-level reuse count; tokens | B or C +2 to +5 at low compute, shrinking at high; verbatim reuse near zero |
| T7 | 50 ARC-style items | A: raw text grids. B: code-made object parse fed into S2 | Solve rate; tokens | 0 to +10 on strong models; large only for weak text-grid readers |
| T8 | Generated Boolean-concept items scored by minimal formula length | No arms; one model | Correlation of accuracy with formula length | Negative correlation, r about -0.3 or stronger, if the human law carries over |
| T9 | Items where the first code attempt fails | A: revise by editing the failing hypothesis with the failing output named. B: resample fresh hypotheses | Solve rate | A at or above B by 2-6 points |
| T10 | Items with 12.5-25% noisy examples | A: exact fit required. B: allow k exceptions | Solve rate on noisy vs clean | B higher on noisy, equal on clean |
| T11 | 50 items where several passing hypotheses differ | A: commit to the highest-ranked passing program. B: majority output across passing programs | Solve rate | B at least A (first LLM test of the one-rule vs blend question) |

---

## 9. What does not transfer, and why

- **Number-word bootstrapping.** A developmental claim; its timing comes from a free parameter. No agent decision depends on it (K03, K04).
- **MCMC timescales.** Human-style search over thousands of data points. The agent has a few examples and a token budget. Take only the idea: sample a rule, test it, revise.
- **DreamCoder training.** Needs 100+ tasks per domain, about a day on 20-100 CPUs, a hand-set DSL. The agent is a scaffold and does not train. LILO-style libraries can partly transfer through prompts; the training loop cannot (a17, b10).
- **Human-fitted priors.** Ellis's prior was tuned on human data. The agent has no labelled data per domain, and the pretrained prior alone is syntax-sensitive (a19).
- **Group-average fits (R2 0.98).** They do not show the agent's reasoning matches the rule model; tasks were small labelled shape and Boolean sets.
- **Verbal descriptions as concepts.** People's written descriptions were too ambiguous (a09). For an agent, a stated rule is not evidence of the rule used (G10), which is why execution matters.
- **Handwritten-character BPL.** A hand-built stroke grammar for one domain; no scaling shown.
- **Greedy single-attempt program writing.** Weak (GPT-4.1 8.0), so "write a program" alone is not a method (d06).
- **Pure-induction claims.** Transduction wins on fuzzy perceptual tasks (Li). "Concepts as programs" is not universal even on ARC.
- **Relayed leaderboard and survey scores.** Not matched in set, harness or tokens. Use as headroom, not proof of method (d01, d04).
- **2025 cost gains.** Mostly fewer parallel samples (o3: 1,024 vs 6), not cheaper reasoning (d02).
- **Probabilistic-program translation (Wong 2023).** No measured gain; skip until a benchmark exists (K19).

---

## 10. Open questions

1. At equal tokens, does propose-K-plus-execute beat plain extended reasoning on a current frontier model? Which K? (K21; still open.)
2. Where is the knee in accuracy vs proposals once verification tokens are counted? Is diversity prompting worth its extra stage? (Lee: no sharp knee to K = 256; token cost not reported.)
3. What is the false-accept rate for prompted 2025-2026 models, and does holding out a demonstration cut it? Nobody has tested a held-out demonstration.
4. Do reasoning models induce programs inside their thinking, and does forcing explicit program induction help or hurt them?
5. Do LLMs show the human one-rule-at-a-time pattern, and does committing to one sampled rule beat blending? (K27, open.)
6. Does shortest-formula length predict LLM difficulty on Boolean concepts? What did Feldman 2000 (N, r) and Lafond 2007 report? (K28, half closed.)
7. Why does refinement hurt on MiniARC and perceptual tasks? Can cheap signals route per item? (Guess only.)
8. Is library reuse real at the idea level, and does it survive higher compute? (ArcMemo gain shrinks; literal reuse near zero.)
9. Does object-structured input help strong models, or only weak text-grid readers? Only GPT-4-era tests exist.
10. Do LLM-written rules prefer the same connectives as people (iff, XOR)? Can the Piantadosi grammar comparison be run on model rules?
11. Do all paradigms face the same 2.5-3x drop on harder items, and does that cap induction-based scaffolds on hard items?

---

## 11. Sources

[V] opened (full text or page read this session by the research agents); [M] snippet only or second-hand.

**Human and cognitive-model studies**
- [V] Piantadosi, Tenenbaum, Goodman (2012) Bootstrapping in a language of thought. https://web.stanford.edu/~ngoodman/papers/COGNIT2374.pdf
- [V] Goodman, Tenenbaum, Feldman, Griffiths (2008) A rational analysis of rule-based concept learning (CogSci 2007 conference version read). https://escholarship.org/uc/item/37n016f5 ; journal copy https://web.stanford.edu/~ngoodman/papers/RRfinal.pdf [M] (download failed)
- [V] Piantadosi, Tenenbaum, Goodman (2016) The logical primitives of thought. https://colala.berkeley.edu/papers/piantadosi2016logical.pdf ; https://gwern.net/doc/psychology/linguistics/2016-piantadosi.pdf
- [V] Piantadosi and Jacobs (2016) Four problems solved by the probabilistic language of thought. https://colala.berkeley.edu/papers/piantadosi2016four.pdf
- [V] Lake, Salakhutdinov, Tenenbaum (2015) Human-level concept learning through probabilistic program induction. https://www.cs.cmu.edu/~rsalakhu/papers/LakeEtAl2015Science.pdf
- [V] Johnson, Vong, Lake, Gureckis (2021) Fast and flexible: human program induction in abstract reasoning tasks. https://arxiv.org/abs/2103.05823
- [V] Acquaviva, Pu, Kryven et al. (2022) Communicating natural programs to humans and machines. https://arxiv.org/abs/2106.07824
- [V] Rule, Tenenbaum, Piantadosi (2020) The child as hacker. https://colala.berkeley.edu/papers/rule2020child.pdf
- [V] Rule et al. (2024) Symbolic metaprogram search improves learning efficiency and explains rule learning in humans. https://doi.org/10.1038/s41467-024-50966-x
- [V] Feldman (2000) Minimization of Boolean complexity in human concept learning, Nature 407:630-3 (abstract only). https://pubmed.ncbi.nlm.nih.gov/11034211/ ; full text [M] https://www.nature.com/articles/35011045
- [M] Lafond, Lacouture, Mineau (2007) Complexity minimization in rule-based category learning. https://doi.org/10.1016/j.jmp.2006.12.002
- [M] Fodor (1975) The language of thought; Boole (1854) (books, not opened)
- [M] Carey (2009) The origin of concepts; Wynn (1990, 1992); Lee and Sarnecka (2010) (via Piantadosi 2012)
- [M] Shepard, Hovland, Jenkins (1961); Bruner, Goodnow, Austin (1956) (cited by other papers)
- [M] Rips, Asmuth, Bloomfield; Asmuth; Rey (critiques of bootstrapping, as discussed in a06, b03)
- [M] Medin and Schaffer (1978); Nosofsky et al. (1994); Gopnik (2001); Sobel (2004) (data sources cited inside the papers above)

**Machine and LLM studies**
- [V] Ellis et al. (2021) DreamCoder. https://arxiv.org/abs/2006.08381 ; https://arxiv.org/pdf/2006.08381
- [V] Ellis (2023) Human-like few-shot learning via Bayesian reasoning over natural language. https://arxiv.org/abs/2306.02797
- [V] Wang, Zelikman, Poesia, Pu, Haber, Goodman (2024) Hypothesis search: inductive reasoning with language models. https://arxiv.org/abs/2309.05660
- [V] Qiu et al. (2024) Phenomenal yet puzzling: testing inductive reasoning capabilities of language models with hypothesis refinement. https://arxiv.org/abs/2310.08559
- [V] Li, Hu, Larsen, Ellis et al. (2024) Combining induction and transduction for abstract reasoning. https://arxiv.org/abs/2411.02272
- [V] Wong et al. (2023) From word models to world models. https://arxiv.org/abs/2306.12672
- [V] Grand, Wong et al. (2024) LILO. https://arxiv.org/abs/2310.19791
- [V] Berlot-Attwell, Rudzicz, Si (2024) Library learning doesn't: the curious case of the single-use library. https://arxiv.org/abs/2410.20274
- [V] Chollet et al. (2025) ARC Prize 2024 technical report. https://arxiv.org/abs/2412.04604
- [V] Mirchandani et al. (2023) Large language models as general pattern machines. https://arxiv.org/pdf/2307.04721
- [V] Moskvichev, Odouard, Mitchell (2023) ConceptARC. https://arxiv.org/pdf/2305.07141
- [V] Mitchell, Palmarini, Moskvichev (2023) Comparing humans, GPT-4 and GPT-4V on abstraction and reasoning tasks. https://arxiv.org/abs/2311.09247
- [V] Xu, Li, Sanner, Khalil (2024) LLMs and the ARC: object-based representations. https://arxiv.org/pdf/2305.18354
- [V] Kumar, Correa, Dasgupta et al. (2023) Using natural language and program abstractions to instill human inductive biases. https://arxiv.org/pdf/2205.11558
- [V] Zhu et al. (2024) Large language models can learn rules (Hypotheses-to-Theories). https://arxiv.org/abs/2310.07064
- [V] Lee et al. (2025) Generating diverse hypotheses for inductive reasoning (Mixture of Concepts). https://arxiv.org/abs/2412.13422
- [V] Li et al. (2024) Chain of Code. https://arxiv.org/abs/2312.04474
- [V] Pourcel, Colas, Oudeyer (2025) SOAR. https://arxiv.org/pdf/2507.14172
- [V] Ho et al. (2025) ArcMemo. https://arxiv.org/pdf/2509.04439
- [V, via summarising fetch tool; numbers as relayed] Greenblatt (2024) Getting 50% (SOTA) on ARC-AGI with GPT-4o. https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt
- [V, via summarising fetch tool; numbers as relayed] ARC Prize (2025) Which AI reasoning model is best? https://arcprize.org/blog/which-ai-reasoning-model-is-best
- [V, secondary survey] Vahdati et al. (2026) The ARC of progress towards AGI: a living survey of abstraction and reasoning. https://arxiv.org/pdf/2603.13372
- [M] Akyurek et al. (2025) test-time training on ARC (via Li and the survey)
- [M] Berman and Pang ARC-AGI-2 systems (second-hand via the survey, d18)
- [M] Fleet, Metagol, Enumerate baselines (named in Rule 2024)
