# Category learning: clustering, explanation-based, Bayesian: deep document

*Subfield A11.08. Built from evidence_a-d.jsonl (a01-d18), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are in brackets. [V] = page or PDF text opened this session, [M] = snippet or second-hand only. Founding papers (Anderson 1991, Tenenbaum 1999, Pazzani 1991, Minton 1990) were NOT opened first-hand; their facts come through Sanborn et al. 2010, MacLellan et al. 2026, Murphy 2007 and recall. This is said again wherever it matters.*

## 1. What it is

This subfield asks how a learner turns a few examples into a general concept when the number of concepts is not fixed in advance. Four families sit here.

- **Clustering and multiple prototypes.** Anderson's Rational Model of Categorization (RMC, 1991) groups items into a flexible number of clusters. Items that look alike join one cluster. A new cluster opens when no old one fits. SUSTAIN (Love, Medin, Gureckis 2004) does the same in a network: it adds a cluster only when it makes a surprising error.
- **Explanation-based generalisation (EBG/EBL).** Mitchell, Keller and Kedar-Cabelli (1986) learn a general rule from one example by explaining it with a domain theory, then keeping only the features the explanation used.
- **Bayesian concept learning.** Tenenbaum (1999) scores every candidate concept by prior times likelihood. The size principle says a smaller consistent concept earns more likelihood per example: (1/size)^n.
- **LLM versions of all three (2023-2026).** A language model proposes rules in words, a program checks them, and a Bayesian or utility step re-weights them. This is the part that matters most for us.

Why it matters for our agent. The schema has two states that do this job. S2 REPRESENT must turn examples into rules. S7 SELECT must keep asking whether the rules still fit. The literature gives three levers: how many candidate rules to keep and how to keep them distinct, how to test them, and when to open a new rule or write an exception.

Links to subfields researched in parallel (not covered here): category learning by rule, prototype and exemplar (A11.07); comparison and relational language (A11.09); MDL and Bayes; inductive logic and ILP; hypothesis generation. Earlier deep documents are listed in 00_FIELDS.md.

## 2. History and theories in depth

### 2.1 Shepard, Hovland and Jenkins (1961) and the clusters-needed idea
Six types of binary categories over three binary dimensions. In people, difficulty runs type I < II < III-V < VI. Nosofsky et al. (1994, N=120) and Badham et al. (2017, N=96) replicated this order [a27, M; K03]. SUSTAIN explains it by the clusters needed: 2, 4, 6, 8 clusters for I, II, III-V, VI [a07, V]. Difficulty tracks how many separate rules a problem needs.

### 2.2 Anderson (1991): the rational model [a01, M; a02-a04, V via Sanborn]
Category learning is density estimation. Each item joins an existing cluster or starts a new one. The prior over partitions has a coupling parameter c. Low c gives many small clusters (exemplar-like). High c gives few large clusters (prototype-like). Sanborn, Griffiths and Navarro (2010) showed this is the same as a Dirichlet process mixture model with a Chinese-restaurant prior [a02, V; b19 Gershman and Blei 2012 tutorial, V].
Anderson's search, local MAP, assigns each item to its single best cluster as it arrives. This is order-dependent and brittle. In Nosofsky's Shepard data the second-best cluster for an item can sit at a 0.9997 posterior ratio to the best, so a tiny change in order or noise flips the choice [a04].

### 2.3 Sanborn et al. (2010): approximate inference and order effects [a02-a04, V]
They replaced local MAP with Gibbs sampling and with particle filters. A particle filter with one particle commits to one sampled partition and does not revise.
- Anderson and Matessa sorting task: 25 of 40 people (62.5%) sorted by the features that came first in training order. Single particle showed the order effect in 63% of runs, M=100 particles in 52%, local MAP in 100%.
- Medin and Schaffer 1978 Exp 1, one block: local MAP r=.87; M=100 particles r=.78; M=1 r=.77. Ten blocks: .95 / .93 / .90.
- Smith and Minda 1998 data: single particle had higher likelihood than local MAP in all 80 parameter settings.
- Shepard problems: single particle fit better in 58% of settings; best SSD 0.24 against 0.31 for local MAP.
Read with care. The fits are correlations on a handful of transfer items. The result shows that human order effects can come from a sampling approximation, not from a different theory.

### 2.4 SUSTAIN (Love, Medin, Gureckis 2004) [a07-a10, V]
A clustering network. It starts with one cluster and adds a cluster only when its prediction is wrong in a surprising way. Attention to each feature is tuned by learning. Results it reproduces (blocks to criterion, model values in brackets):
- Inference learning vs classification learning: linear structure 6.5 (7.5) vs 12.3 (11.2) blocks; non-linear 27.4 (28.6) for inference vs 10.4 (10.6) for classification.
- Learning a name for each item beats learning two category labels: 7.1 vs 9.7 blocks (first/last-name study).
- Unsupervised learning and the Shepard order.
Key lesson: what is learned depends on the question asked. The same examples give a different representation when you predict a label or predict a missing feature [K04; single-source because the original studies were read only through this paper].
Contrast with the RMC: SUSTAIN opens a cluster on error only; the RMC opens one on prior probability.

### 2.5 Prototype-to-exemplar shift [a06, a24, a26, b18; K05, K06]
Smith and Minda (1998), non-linearly separable task, 16 people, 10 segments: exceptions are missed in the first 3 segments and fixed from segment 4. Behaviour looks prototype-like early and exemplar-like late. MacLellan et al. (2026) reproduce this with Cobweb (a category-utility hierarchy) only with prior strength alpha about 2; below 0.6 the shift vanishes [a06, V]. A rival account is attention change (Nosofsky and Zaki 2002, not opened). The mechanism is contested.

### 2.6 Explanation-based generalisation (Mitchell, Keller, Kedar-Cabelli 1986) [a11, a12, V]
Four inputs: goal concept, one training example, domain theory, operationality criterion. Two steps: (1) explain why the example fits the goal, using the theory; (2) regress the goal through the proof to get sufficient conditions in operational terms. The explanation separates relevant features from irrelevant ones. Worked examples: SAFE-TO-STACK, CUP, a search-control problem.
Named failures when the theory is imperfect: incomplete (cannot prove the example), intractable (proof too costly), inconsistent (two rules give two weights). The authors call for combining explanation-based with similarity-based methods. Later came the utility problem (Minton 1990, not opened [d15]): learned rules that match often can slow search more than they help. This paper has no human data. Pazzani (1991) is the human-side study of prior knowledge in concept acquisition; it was not opened [d14, b29], so we have no numbers.

### 2.7 Tenenbaum (1999) and the size principle [d12 V via Murphy 2007; d13 and a13 abstract only]
Concept learning as Bayesian inference over hypotheses (intervals, rules, sets). Likelihood of n examples under a hypothesis of size |h| is (1/|h|)^n. Verified arithmetic for the number game: after seeing {16, 8, 2, 64}, "powers of two" beats "even numbers" by nearly 5000:1 (7.7e-4 vs 1.6e-7). "Powers of two except 32" is rejected only through the prior [K29, d12]. The human data in the thesis are not verified. Tenenbaum and Griffiths (2001) generalise this to similarity (abstract only).

### 2.8 The LLM turn (2023-2026)
Three moves follow the older ideas: (a) a language model proposes the hypothesis space, replacing hand-built grammars; (b) a program or Bayes rule tests and weights it; (c) a meta-trained network absorbs the priors. See Sections 5 and 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RMC equals a Dirichlet-process mixture; local MAP is order-dependent | second-best cluster at 0.9997 ratio to best | Sanborn 2010 [a02, a04] | Established (K01) |
| Single-particle filter matches human order effect | 25/40 people (62.5%); PF 63%, M=100 52%, local MAP 100% | Sanborn 2010 [a03] | Single-source (K02) |
| Same filter fits Medin-Schaffer and Smith-Minda data | one block r=.87 (MAP), .78 (M=100), .77 (M=1); ten blocks .95/.93/.90; PF better in 80/80 S&M settings and 58% Shepard settings (SSD .24 vs .31) | Sanborn 2010 [a02-a04] | Single-source (K02) |
| Difficulty tracks clusters needed | Shepard I < II < III-V < VI; SUSTAIN 2/4/6/8 clusters; Nosofsky N=120, Badham N=96 | Love 2004; Shepard 1961 [a07, a27] | Established (K03) |
| Inference vs classification learning | linear 6.5 vs 12.3 blocks; non-linear 10.4 (classification) vs 27.4 (inference) | Love 2004 [a08] | Single-source (K04) |
| Item names beat category labels | 7.1 vs 9.7 blocks | Love 2004 [a09] | Single-source (K04) |
| Prototype early, exemplar late | exceptions missed in segments 1-3, fixed from segment 4 (16 people, 10 segments) | Smith and Minda 1998 via MacLellan 2026 [a24, a06] | Established as phenomenon; mechanism contested (K05, K06) |
| Cobweb vs RMC on classic data | Spearman .95 vs .91 (M&S Exp 1); Hayes-Roth .95-.96; context model .96 on Exp 2 | MacLellan 2026 [a05, b17] | Single-source, weak (K20) |
| Generalisation gradient depends on test format | Exp 1 N=277, Exp 2 N=245; decisions steeper, BF>1000; absolute framing about 20% more Gaussian | Lee, Wills, Schlegelmilch 2026 [a14, b21] | Single-source (K16) |
| ARC, 100 tasks, GPT-4: direct vs propose-test | direct 17%; program 23%; summarised hypotheses 30%; human-selected 33%; human-written 45% | Wang 2024 [a17, c12] | Established (K08) |
| Hypothesis generation is the bottleneck | correct hypothesis for 49/100 ARC tasks; 33 (67%) of those gave correct programs | Wang 2024 [a17, b15] | Established (K09) |
| List Functions error sources (GPT-4o) | generator 46.4% correct; summarizer 34.5 (drops 26% of correct ones, 12.1-point loss); implementor 61.2; overall 62.0; up to 257 calls per task; refinement rescued 4.3% | Parab 2025 [c13] | Single-source (K09) |
| Refinement is not universal | ACRE 28% to 59%; MiniARC task accuracy 13.8 (plain) vs 14.6 best; raw 33.1 falls to 18.7 | Qiu 2024 [a18, b12] | Established (K08) |
| LLM applies rules worse than it proposes them | MiniSCAN above 80 to about 0; ACRE 59.0 to 47.0; List Functions 61.2 to 50.0; MiniARC 14.6 to 5.4 (last three mapped by inference) | Qiu 2024 [a18, b13, c09] | Single-source (K10) |
| Noisy examples break induction | 1-2 of 8 corrupted hurts; keeps falling at 12.5/25/50%. Second lab, list functions 10 to 30% noise: GPT-4o 39.9 to 26.1; GPT-4o-mini 31.3 to 19.7; DeepSeek-V3 43.1 to 30.5. Subset sampling + execution: 2.8-point drop vs 6.0 | Qiu 2024; Li 2025 [a19, d03] | Established (K11) |
| Reasoning model flips per instance under noise | R1 Atbash CoT 65.0 clean and noisy, consistency 70.0%; SRR 82.0 to 79.0, 93.0% | Li 2025 [d04] | Single-source |
| LLM-proposed hypotheses re-weighted by Bayes fit people | logical concepts R2=.81 with 100 proposals, within 3% of human accuracy; number game original model needed over 5000 hypotheses; English beats Python | Wong et al. 2023 [a16, b06, c05, c06] | Established (K12) |
| Online rule updating fits Zendo | fuzzy R2 .57, hard .10, batch .05, LLM-only .25; log-lik -1478.82 vs -1539 vs -5209.93; ActiveACRE online hard 0.35 vs 0.15 and 0.10 | Piriyakulkij 2024 [b09, b10] | Established (K12) |
| LLM generalises less like humans in number game | JSD human-Bayes .36, GPT-Bayes .56, best fit .49 (GPT) and .30 (human); rule bias humans .9, GPT 1.0 | Bazigaran and Sohn 2025 [c01-c04] | Established (K13) |
| Meta-learned prior network fits humans | BIC 38722.13 vs Claude direct 39816.90; 41207.20 vs 42401.42; posterior freq .43 vs RMC .41 (SE .05); OpenML 70.95 vs TabPFN 70.51; Shepard MSE .0287 vs .2627 | Jagadish 2024 [b01-b05] | Single-source (K14) |
| Claude-2 prompted directly is exemplar-based from block 2 | Badham error: Claude .18 vs ERMI .05 | Jagadish 2024 [c19] | Established (K05) |
| Induction and transduction combine | ensemble 26.50%; induction 18.78%; transduction 15.25% (ARC validation, 2 tries) | Li 2024 [c23, d09] | Established (K17) |
| Candidate pools plus execution on ARC | sampling 43% vs o1-preview 18% and Claude 3.5 Sonnet 14% single pass; about 9% of rules that fit all train pairs still fail test | ARC Prize 2024 [d08] | Single-source (K24) |
| IID samples are duplicates | unique programs among failed instances: K=2 1.40, 4 1.79, 8 2.92, 16 4.56, 32 7.89; Mixture of Concepts +4.5 (GPT-4o-mini), +5.0 (Llama-3.1-70B) | Lee 2025 [d10] | Established (K23) |
| Falsification is the first failure with current models | confirmation tests 66-82% instruction-tuned, 24-39% reasoning; success 33-41% vs 68-75% top reasoning; 92-98% of failed games had a surface-feature hypothesis | FalsifyBench 2026 [d01, d02] | Single-source (K25) |
| Rule library lifts weaker model | CLUTRR +11.1 to +16.4; GPT-3.5 using GPT-4 rules +27.2; random rules hurt | Zhu 2023 [a20, c14] | Established (K15) |
| Explanations in few-shot | 280B model, 40 tasks, untuned explanation gain about one third of example gain, twice the instruction gain | Lampinen 2022 [b16] | Established (K15) |
| ExpeL insights | HotpotQA 40% vs Reflexion 39%; ALFWorld 59 vs 54 | Zhao 2024 [c15] | Established (K15) |
| Executable rules beat prose | PAL +15 points absolute over CoT on GSM8K | Gao 2023 [d05] | Established (K26) |
| Example order matters in ICL | SST-2 permutation 88.7% to 51.6% on model change; voting +3.9 to +17.9 on reasoning sets | Lu 2022; Wang 2023 [d07, d06] | Contested for rule induction (K27) |
| Strict utility filter for memory | deleting by measured utility cut memory about 3x; helps with a strict evaluator, hurts with a noisy one | Xiong 2025 [d11] | Single-source (K28) |
| LLM gap to humans on concepts | ConceptARC humans 91%, GPT-4 25% (one-shot 33%), best ARC program 52%; minimal tasks humans .95 vs GPT-4 text .69 | Moskvichev 2023; Mitchell 2023 [c24, c25] | Single-source, 2023 models (K18) |
| Goal-driven clustering in words | human preference 80% vs LDA 56%, 71% vs Instructor; covers 66% of samples | Wang 2023 [c16] | Single-source (K21) |
| Abstract rules vs metamers | networks beat humans on metamers in 7 of 8 abstractions | Kumar 2022 [b22] | Single-source (K22) |

## 4. Mechanisms and models

### 4.1 RMC as a Dirichlet-process mixture
After n items, an existing cluster k with n_k items has prior c*n_k / ((1-c) + c*n). A new cluster has prior (1-c) / ((1-c) + c*n). Multiply each by the likelihood of the item's features under that cluster (product over features of smoothed frequency). Engineering reading:
- Keep a list of clusters, each with a count and a feature tally.
- A new item joins the cluster with the highest prior times likelihood, or opens a new one if the "new" score wins (local MAP). Or sample from the scores (particle filter).
- c is the one dial: low c, many clusters (memorise); high c, few clusters (generalise).
- One particle means one committed assignment path with no revision. Many particles keep several weighted paths. The order effect shrinks with more particles (63% to 52% in Sanborn).
The 0.9997 ratio is the warning: assignments are often near ties, so do not read a "best" cluster as strong evidence.

### 4.2 SUSTAIN (surprise-driven cluster recruitment)
Cluster activation is feature-wise similarity weighted by attention. The winner makes the prediction. If it is right, strengthen it and shift attention. If the error is surprising (above a threshold), recruit a new cluster centred on this item. Start with one cluster. At prompt level this reads: open a new rule only when no existing rule fits and the miss is clear. Because recruitment is on error, cluster count grows with difficulty (2/4/6/8 for Shepard types).

### 4.3 Cobweb and category utility (hierarchy)
A tree of groups. Each new item descends the tree. At each node choose among: add to the best child, create a new child, merge the two best children, or split the best child, by category utility (gain in predictability of features). Prior strength alpha controls how readily new nodes form; alpha about 2 gives the prototype-to-exemplar shift. Upper nodes are general, leaves are specific, so exceptions sit at the leaves [a05, a06, b17].

### 4.4 Size principle and the Bayesian rule score
Score(h) = prior(h) * (1/|h|)^n for every h consistent with all n examples, else 0 (or a small value for noise tolerance). Normalise in code. Prediction for a new item is the sum of scores of hypotheses that contain it. A broad rule is penalised exponentially with n. With few examples the prior dominates; with many the likelihood does. Wong et al. use an LLM to propose 50-100 hypotheses, then score them exactly this way [a16, b06].

### 4.5 LLM hypothesis search (propose, test, refine)
Wang et al. 2024 [a17]: (1) the LLM writes many natural-language hypotheses; (2) optionally a summarizer prunes them; (3) the LLM turns each into a program; (4) programs run on all given examples; (5) keep a hypothesis whose program fits all; (6) apply it to the test input. Parab et al. 2025 locate failures by stage: generator 46.4% correct, summarizer drops 26% of correct ones, implementor 61.2% [c13]. Qiu et al. add a refinement round with execution feedback; it helps only where the right answer lies inside the hypothesis space [a18].
Variants:
- bandit-style hypothesis bank with upper-confidence scoring and replacement of weak ones (HypoGeniC; +31.7 SHOE SALES, +13.9 DECEPTIVE REVIEWS, +3.3 HEADLINE, +24.9 TWEET over few-shot) [c17];
- online Bayesian updating of fuzzy rules (Piriyakulkij) [b09];
- subset-sampled rules with execution feedback for noise (SRR) [d03];
- diversity-first prompting: "list K distinct concepts, then one hypothesis per concept" [d10].

### 4.6 Online rule updating with experiments (Zendo, ActiveACRE)
Maintain weighted rules. After each observation multiply each weight by the likelihood under that rule (fuzzy: allow some chance the label is wrong). Choose the next experiment to split the rules. Fuzzy rules explain humans (R2 .57); hard rules score higher for the machine (Zendo, out of 8: online hard about 6.55, online fuzzy 5.35, humans 5.26; row alignment is probable, not certain) [b09, b10; critique correction 1].

### 4.7 Explanation-first step in prompt form
(1) State the domain theory in plain sentences. (2) Take one example and write a short proof from the theory that it has the label. (3) Keep only the features the proof used. (4) Write the generalised rule. (5) Test it on the other examples. If no proof can be built, the theory is incomplete: fall back to induction. The nearest LLM evidence is explanations attached to few-shot examples [b16]. No test of the full regression step with an LLM was found.

### 4.8 Meta-learned priors (ERMI)
Generate many category tasks with an LLM, meta-train a network on them, then use it on human tasks. This is not a scaffold technique; it is relevant only as a source of priors [b01-b05, c21].

## 5. What holds up

**Replicated or confirmed by more than one source**
- Cluster count tracks difficulty (Shepard order; Nosofsky 1994, Badham 2017) [K03].
- Prototype-like early, exemplar-like late, as a phenomenon in humans [K05].
- Propose-test-refine with an external checker beats direct prompting on rule induction: four sources (Wang, Qiu, Li, Zhou) [K08].
- Hypothesis generation is a bottleneck in 2023-24 models (Wang, Parab) [K09].
- Noise brittleness: Qiu 2024 and Li 2025, two labs [K11].
- Diversity of candidates matters: Lee 2025 and ARC Prize results [K23, K24].
- Induction plus direct answering combine (Li 2024, ARC Prize) [K17].
- Reusing verified rules in memory helps weaker models (Zhu, Zhao, Lampinen) [K15].

**Failures and boundary conditions**
- Refinement rescued only 4.3% of wrong hypotheses in List Functions [c13]. It cut MiniARC raw accuracy from 33.1 to 18.7 with no task-accuracy gain (13.8 to 14.6) [b12]. Net: refinement works only where the hypothesis space contains the answer.
- Summarising or pruning hypotheses throws away correct ones (26% in Parab) [c13].
- About 9% of rules that fit all train pairs still fail test [d08]. Fit is not proof (matches G3).
- Cobweb's edge over RMC (.95 vs .91) rests on about 6 items with no test; the context model itself scores .96 [critique correction 6].
- ERMI vs RMC on Badham is a tie (.43 vs .41, SE .05). It leads only on Devraj (.32 vs GCM .24) [critique correction 7].
- The prototype-to-exemplar shift needs alpha near 2; alpha below 0.6 removes it [a06].
- Lee et al. 2026: domain interactions did not replicate in the second test phase; most learning-mode differences came from test wording [a14, b21].
- Hard rules score higher than fuzzy rules, but fuzzy rules fit people. A human-like fit is not an accuracy-maximising design [b10].
- Few-shot prompting degraded DeepSeek-R1 on inductive tasks (introduction claim only; no table opened) [d17].

**Moderators**
- Model size: only the largest model gained from explanations in Lampinen [b16].
- Executable vs prose application: execution removes much of the application gap (PAL +15 points; SRR noise drop 2.8 vs 6.0) [d05, d03].
- Evaluator strictness for memory deletion [d11].
- Test format and framing (decision vs rating) [a14].

**Source-count honesty.** The 85 evidence lines come from about 25 papers. Qiu, Jagadish, Wong, MacLellan, Lee and Wang each count as one source [critique].

## 6. Language models

**Direct prompting looks exemplar-based and unlike humans.** Claude-2 prompted directly on category learning was fully exemplar-based after block 2; BIC 39816.90 vs ERMI 38722.13; Badham error .18 vs ERMI .05 [b01, c19]. GPT-4 ratings in the number game also differed from humans [b07].

**Number game.** o1-mini JSD to Bayes .56 vs humans .36; best-fit variant .49; fitted rule bias 1.0 for GPT vs .9 for humans; the ablation says it acts as a maximum-likelihood learner while humans match a prior-plus-averaging variant. GPT-4o, DeepSeek-V3 and LLaMA-3-8B were less structured [c01-c04]. A size-principle prompt has not been tested [K29].

**Rule induction (ARC, ACRE, MiniSCAN, List Functions).**
- ARC 100 tasks GPT-4: direct 17%, program 23%, hypotheses summarised 30%, human-selected 33%, human-written 45% [a17].
- ACRE 28% to 59% with the checked loop [a18].
- ConceptARC: GPT-4 25% zero-shot, 33% one-shot, humans 91%, best program 52% [c24, c25]. Models are 2023-era and both papers come from one group.
- ARC Prize 2024: sampling programs 43% vs single pass o1-preview 18% and Claude 3.5 Sonnet 14% [d08]. Induction 18.78% plus transduction 15.25% gives 26.50% [d09].
- List Functions (GPT-4o): generator 46.4% correct, overall 62.0, up to 257 calls [c13].

**Application is the weak point of in-model checking.** With the LM as interpreter: MiniSCAN above 80 to about 0; ACRE 59.0 to 47.0; List Functions 61.2 to 50.0; MiniARC 14.6 to 5.4 [a18, b13; mapping inferred]. A model trained to generate and follow rules (ReDis, 7-8B) gained +23.2% (1D-ARC), +2.8% (ACRE), +66.6% (MiniSCAN) relative to GPT-4o [d17]; that is training, not a scaffold.

**Noise.** Accuracy falls steadily with corrupted examples; GPT-4o list functions 39.9 to 26.1 at 10 to 30% noise. DeepSeek-R1 stays flat in accuracy on Atbash but flips which instances it solves (consistency 70.0%) [d03, d04].

**Falsification (2025-26 models).** FalsifyBench, 12 models including GPT-5.2: confirmation tests 66-82% for instruction-tuned models, 24-39% for reasoning models. Success tracks it (33-41% vs 68-75%). Failed games drift to surface-feature rules (92-98% for the top models) [d01, d02]. The first failure is the test step, not generation. Jin 2026 and Jhaveri 2026 were not read.

**Diversity.** IID sampling gives duplicates (1.40 unique programs in 2 samples, 7.89 in 32). Asking for distinct concepts first gives +4.5 / +5.0 points at equal sample count [d10].

**Bayes over LLM-proposed hypotheses.** 50-100 proposals with weighting: logical concepts R2=.81, within 3% of human accuracy [c06]. Online updating gains on Zendo and ActiveACRE [b09]. These use GPT-4-class models and are the strongest human-like results.

**Memory and experience.** Rule library +11.1 to +16.4 on CLUTRR; +27.2 for GPT-3.5 with GPT-4 rules; random rules hurt [c14]. ExpeL 40 vs 39 HotpotQA [c15]. Agents copy retrieved records; deleting by measured utility helps only with a strict evaluator [d11].

**What changed things, by how much.** External execution (PAL +15; noise drop 2.8 vs 6.0). Candidate pool (14-18% to 43% on ARC). Diversity prompts (+4.5/+5.0). Fallback to direct answering (18.78 to 26.50). A falsification step: confirmation share is 66-82% vs 24-39% across model types, but that is a model property, not a prompt effect we have measured. Pure refinement: small or negative outside narrow cases.

**Gap.** Nearly everything uses GPT-4/4o, Claude-2 or o1-mini. Almost nothing covers 2025-26 reasoning models on ARC-style induction, except Bazigaran (number game) and FalsifyBench.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **S2: write several candidate rules and keep them distinct, not one.** Prompt "list K different concepts that fit, then one rule per concept" before any sampling. [E] Claims K23, K24, K12, K08; evidence d10, d08, a17, b06. Supports G4 (samples from one model are not independent) and must still pass G7 (win at equal tokens).
2. **S2/S7: check every candidate rule against all given examples by code; write the rule as a function.** [E] K26, K08; evidence d05, d03, a18, b13. Matches G5 and G2.
3. **S7: a rule that fits the examples is not proven.** Hold out an example or a mutated input. About 9% of fitting ARC rules fail the test. [E for the principle; the 9% is single-source] d08. Matches G3.
4. **S7: when no candidate fits all examples, switch family (direct answer or new rule family); do not abstain.** [E] K17 (18.78 to 26.50); evidence c23, d09. Matches G6.
5. **S7: noise rule.** A rule need not fit every example when examples may be corrupted; allow named exceptions or outliers, scored by code. [E that brittleness exists, K11; the exception-list cure is untested, so list it also under Test first]. d03, d04, a19.
6. **S2: spend the budget on hypothesis generation; do not prune or summarise candidates before the code check.** [E] K09; a17, c13 (the summarizer lost 26% of correct hypotheses).
7. **Memory: store verified rules (code-checked) with a success/failure count.** Include a random-rule control. [E for rule-library gain, K15; the utility-filter part is [S], K28]. c14, c15, d11.
8. **S2: expect the number of rules to grow with problem structure (Shepard-like).** Use as a sanity check, not a control. [E] K03.

### Test first

1. **Weighted pool vs one rule at equal tokens (open a new rule only on a surprise).** [S/C] K01, K02, K12; a02, b06, b09. Not run with 2025-26 models.
2. **Forced falsifying test in S7:** choose one input inside a broader plausible rule but outside the current rule. [S] K25; d01, d02.
3. **Size-principle prompt:** list all consistent rules, prefer the one allowing the fewest other cases. [S] K29, K13; c01, d12.
4. **Shuffle example order, induce several times, vote.** [C] K27; d06, d07. G4: voting is a hint, so follow with a code check.
5. **Explanation-first generalisation when a domain theory is stated.** [S] K07; a11, a12, b16. Pazzani and Minton unread.
6. **Exception list instead of refit.** [S] K05, K11; a24, d03.
7. **Question framing:** same examples as "predict label" vs "predict missing feature". [S] K04; a08.
8. **Group by stated description, coverage and overlap scored by code.** [S] K21; c16.
9. **Budget split between induction and direct answer, picked by agreement with the examples.** Partly established (K17); untested at equal tokens with current models.
10. **Priors from the model's own generated example tasks.** [S] K14; b01-b05. May only work in a trained network.

## 8. Concrete tests on our bench

All arms at equal total tokens; setup cost counted (G7). Add list-function and number-game item types to the harness if missing.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and list-function items | A: 8 IID rule samples. B: "K distinct concepts first", then one rule each | held-out accuracy; count of unique rules | B +3 to +5 points (Lee 2025) |
| T2 | ARC-like grids | A: direct answer. B: N rules, code-checked on all examples. C: B with fallback to direct answer if none fits | accuracy; fallback rate | B > A; C > B by about 5-8 points if the ARC Prize pattern holds |
| T3 | List functions with 0/10/30% corrupted examples | A: rule must fit all. B: rule plus named exceptions, scored by code | accuracy; consistency of instances solved clean vs noisy | B cuts the noise drop (Li: 6.0 to 2.8) |
| T4 | Rule-apply step on ACRE and list functions | A: rule applied in prose. B: rule as code | accuracy; tokens | B recovers most of the 59.0 to 47.0 gap; report token cost |
| T5 | Number game (one- and four-example items) | A: plain. B: size-principle prompt; compare with a Bayes model | JSD to Bayes and to human data | JSD moves from .56 toward .36 |
| T6 | ARC-like, 5 shuffles of example order | A: single induction. B: vote over 5 orders, then code check | spread of final rule; accuracy | order spread exists; voting gain +3 to +10 if so (contested) |
| T7 | Zendo or Mastermind-style sequential tasks | A: confirm-only. B: forced falsifying test each round | success rate; share of confirming tests | B better, nearer reasoning-model rates |
| T8 | Task families with repeats | A: no memory. B: raw examples. C: verified rules with counts. D: random rules | accuracy; tokens | C > B > A; D < A |
| T9 | Items with a stated partial theory | A: induction from many examples. B: explain-one-then-generalise. C: both | accuracy as theory goes complete, incomplete, wrong | B wins when the theory is complete; loses when it is wrong |
| T10 | Same examples, two question framings | label vs missing-feature | rule structure; accuracy | different rules, as in Love 2004 |
| T11 | Regression check | ConceptARC minimal tasks | accuracy vs GPT-4 .69 | tracks S2 changes |

## 9. What does not transfer, and why

- **Human trial counts and blocks.** Love's 6.5 vs 12.3 blocks describe people learning over many trials. Our agent sees all examples at once.
- **Order effects of sequential learners (RMC particle filter).** Our agent can re-read all examples. Order sensitivity applies only to in-context order bias, which is unmeasured for 2025-26 models.
- **Fitting human choices as a goal.** ERMI, Centaur and fuzzy-rule fits aim at human likeness. We want accuracy, and hard rules beat fuzzy rules in accuracy [b10]. Centaur (fine-tuning on Psych-101) is out of scope for a scaffold [K19].
- **Meta-learned priors (ERMI).** Needs training; not a scaffold.
- **Classic EBL.** Needs a complete, correct, tractable domain theory. Most bench problems have none, and a wrong theory misleads [a12].
- **Cobweb vs RMC fit differences.** About 6 items, no test [critique].
- **Prototype-exemplar shift mechanism.** Contested; do not design S7 around it.
- **Generalisation gradients (Lee et al.).** A lab task with grey rectangles; useful mainly as a warning that answer format changes the result.
- **Heavy search budgets.** Up to 257 calls per task [c13] and thousands of sampled programs [d08] break G11 and G12 unless gated by difficulty.
- **Debate-like pools of rules.** G9 bans debate; pool by code, not by argument.

## 10. Open questions

1. Does a weighted pool that opens a new rule only on surprise beat one-rule-at-a-time at equal tokens with 2025-26 models? (Partly closed: breadth helps; Dirichlet-style weighting untested.)
2. Which stage fails first with current reasoning models: generation, pruning or application? FalsifyBench points to the test step; pruning and application were not isolated.
3. What does reliable rule application cost in tokens, against the 59.0 to 47.0 ACRE drop?
4. Does an explicit exception list restore accuracy under noise?
5. Is example-order sensitivity present in LLM rule induction, and does shuffling plus voting fix it?
6. Does a size-principle prompt move LLM generalisation toward humans?
7. Does explanation-first generalisation beat induction when the theory is partly wrong? (Pazzani 1991 and Minton 1990 unread.)
8. What is the utility cost of a growing rule library, and is there a safe filter?
9. Original Anderson 1991 and Tenenbaum 1999 numbers are not verified first-hand.
10. Do human-like priors help a scaffolded agent? The .43 vs .41 tie with RMC was not retested.
11. Do the GPT-4-era results (Qiu, Wang, Wong, Parab) still hold on current models?

## 11. Sources

[V] opened this session; [M] snippet or second-hand only.

- [M] Anderson (1991) The adaptive nature of human categorization. https://psycnet.apa.org/record/1991-20640-001 (facts via Sanborn 2010)
- [V] Sanborn, Griffiths, Navarro (2010) Rational approximations to rational models. https://osf.io/download/qj42m/
- [V] Love, Medin, Gureckis (2004) SUSTAIN. http://bradlove.org/papers/love_etal_2004.pdf
- [V] Mitchell, Keller, Kedar-Cabelli (1986) Explanation-based generalization. https://link.springer.com/content/pdf/10.1007/BF00116250.pdf
- [M] Tenenbaum (1999) thesis abstract. https://dspace.mit.edu/handle/1721.1/16714 ; [V] Murphy (2007) lecture summary. https://www.cs.ubc.ca/~murphyk/Teaching/CS340-Fall07/reading/joshConcepts.pdf
- [M] Tenenbaum and Griffiths (2001). https://doi.org/10.1017/S0140525X01000061
- [V] MacLellan et al. (2026) A rational account of categorization. https://arxiv.org/abs/2603.29895
- [V] Lee, Wills, Schlegelmilch (2026) Is generalization general? https://pmc.ncbi.nlm.nih.gov/articles/PMC13518074/
- [V] REFRESH (dimensional biases). https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8567459/fullTextXML
- [V] Wong, Grand, Lew, Goodman, Mansinghka, Andreas, Tenenbaum (2023) Human-like few-shot learning via Bayesian reasoning over natural language. https://arxiv.org/abs/2306.02797
- [V] Wang, Zelikman, Poesia, Pu, Haber, Goodman (2024) Hypothesis search. https://arxiv.org/abs/2309.05660
- [V] Qiu et al. (2024) Phenomenal yet puzzling. https://arxiv.org/abs/2310.08559
- [V] Zhu et al. (2023/24) Hypotheses-to-Theories. https://arxiv.org/abs/2310.07064
- [V] Han, Ransom, Perfors, Kemp (2023) Inductive reasoning in humans and LLMs. https://arxiv.org/abs/2306.06548
- [V] Binz et al. (2025) Centaur. https://arxiv.org/abs/2410.20268 ; Binz et al. (2023) Meta-learned models of cognition. https://arxiv.org/abs/2304.06729
- [V] Jagadish et al. (2024) ERMI. https://arxiv.org/abs/2402.01821
- [V] Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing experiments and revising rules. https://arxiv.org/abs/2402.06025
- [V] Lampinen et al. (2022) Can language models learn from explanations in context? https://arxiv.org/abs/2204.02329
- [V] Gershman and Blei (2012) Tutorial on Bayesian nonparametric models. https://gershmanlab.com/pubs/GershmanBlei12.pdf
- [V] Wikipedia: Explanation-based learning. https://en.wikipedia.org/wiki/Explanation-based_learning
- [V] Kumar et al. (2022) Disentangling abstraction from statistical pattern matching. https://arxiv.org/abs/2204.01437
- [V] Poth (2023) Probabilistic learning and psychological similarity. https://www.mdpi.com/1099-4300/25/10/1407
- [V] Bazigaran and Sohn (2025) Number game. https://arxiv.org/abs/2512.20162
- [V] Parab et al. (2025) Error sources in hypothesis search. https://arxiv.org/abs/2509.01016
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang, Shang, Zhong (2023) Goal-driven explainable clustering. https://arxiv.org/abs/2305.13749
- [V] Zhou et al. (2024) HypoGeniC. https://arxiv.org/abs/2404.04326
- [V] Yang et al. (2024) DEER. https://arxiv.org/abs/2212.10923
- [V] Li et al. (2024) Combining induction and transduction. https://arxiv.org/abs/2411.02272
- [V] Moskvichev, Odouard, Mitchell (2023) ConceptARC. https://arxiv.org/abs/2305.07141 ; Mitchell, Palmarini, Moskvichev (2023). https://arxiv.org/abs/2311.09247
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/abs/2606.04751
- [V] Li, Wang, Zheng, Song (2025) Patterns over principles. https://arxiv.org/abs/2502.16169
- [V] Gao et al. (2023) PAL. https://arxiv.org/abs/2211.10435
- [V] Wang et al. (2023) Self-consistency. https://arxiv.org/abs/2203.11171
- [V] Lu et al. (2022) Fantastically ordered prompts. https://arxiv.org/abs/2104.08786
- [V] Chollet et al. (2024) ARC Prize 2024 technical report. https://arxiv.org/abs/2412.04604
- [V] Lee, Koh, et al. (2025) Generating diverse hypotheses. https://arxiv.org/abs/2412.13422
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067
- [V] Sadeq et al. (2025) Reasoning distillation for ICL (ReDis). https://arxiv.org/abs/2504.10647
- [M] Medin and Schaffer (1978); Smith and Minda (1998); Hayes-Roth and Hayes-Roth (1977); Griffiths et al. (2007); Shepard, Hovland, Jenkins (1961): second-hand via Sanborn 2010, MacLellan 2026, Love 2004.
- [M] Pazzani (1991) https://escholarship.org/content/qt9wv5n75t/qt9wv5n75t.pdf ; Minton (1990) https://aitopics.org/doc/classics:AC09A14F ; Anderson, Love and Mitchell DOI pages (c26-c28) and Tenenbaum NIPS 1999 (c29, b28): not opened.
