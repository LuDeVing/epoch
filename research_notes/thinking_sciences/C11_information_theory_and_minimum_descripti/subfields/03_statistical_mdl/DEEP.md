# Statistical MDL: deep document

*Subfield C11.03. Writer pass over evidence_a-d.jsonl (a01-a26, b01-b28, c01-c25, d01-d17), claims.jsonl (K01-K30) and critique.md. Ids in square brackets are evidence ids or claim ids. Status: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Minimum description length (MDL) says: the best explanation of data is the one that gives the shortest total code. The total has two parts. Part one is the length of the hypothesis. Part two is the length of the data once the hypothesis is known. Write it as L(H) + L(D given H). A hypothesis that is too simple leaves a long residual. A hypothesis that is too complex costs a lot to state. The minimum sits between them.

The statistical branch makes this exact. It uses probability models, so code length is -log2 of a probability. Choosing a model is then the same as choosing a probability distribution that compresses the data best. [a01, a07]

Why it matters for our agent. Step S7 (SELECT) must choose among candidate rules, programs or answers that all fit the examples. The current order is symmetry, then group size, then shortest. "Shortest" is an MDL idea. This document asks: how far can that tie-break be trusted, how should length be computed, and when does it fail?

Short answer from the evidence:
- The theory is solid and old. Complexity penalties protect against overfitting. [K01, E]
- It is not free of failure. With few examples it needs care, and when the true rule is not among the candidates it can pick over-complex ones. [K02, E]
- No study yet tests a length tie-break inside an LLM agent loop against majority vote or model confidence at equal tokens. [critique, K25]
- The best-supported practical use is as a last tie-break after held-out fit and vote. The room left for it is small: about 9% of train-fitting ARC programs are false positives, and a vote removes about half of those problems. [K25, d04]

## 2. History and theories in depth

### 2.1 Founding (1960s to 1980s)

- Wallace and Boulton (1968) and Rissanen (1978) are the roots. Dates are given in Grunwald's tutorial. [a09]
- Rissanen 1978 ("Modeling by shortest data description") introduced the two-part code for parametric models. Per Grunwald and Roos, it worked on discretised countable parameter sets and treated the complexity term as zero. The primary paper was not opened here. [a01, d08, b26 (M), K30]
- Schwarz 1978 gave BIC at the same time. BIC is what you get from MDL if you keep only the (k/2) log n term. [a10, b27 (M)]
- Wallace and Freeman (1987) gave the MML variant. Rissanen (1996) tied stochastic complexity to Fisher information. [a09]

### 2.2 Crude versus refined MDL

Grunwald's tutorial separates two versions. [a08]
- **Crude MDL**: pick H minimising L(H) + L(D given H). Problem: L(H) depends on how you code hypotheses, so the result is arbitrary.
- **Refined MDL**: use one universal code per model, so complexity is a property of the model class, not of a coding trick. Stochastic complexity = L(D given best fit) + COMP(model).

Four ways to build a universal code, all with the same leading behaviour: [a01, a08]
1. Two-part code (oldest).
2. Bayes mixture (Jeffreys prior for exponential families matches NML up to o(1)). [a03]
3. Normalised maximum likelihood (NML, Shtarkov 1987). It is the minimax-regret code: it minimises the worst-case extra bits over the best-fitting member. [a02]
4. Prequential (predict-then-reveal) plug-in code, Rissanen 1984 and Dawid 1984.

Also named: the switch distribution and RIPr. [a01]

Tutorial example: fit a degree-k polynomial to a small sample. A line underfits, degree n-1 overfits, and the third degree wins on code length. [a08] Section 2.10 of the tutorial lists conceptual problems, so "MDL guards against overfitting" is not unconditional.

### 2.3 The penalty

For a regular model with k parameters and n data points: [a03, b06]

COMP(M) = (k/2) log(n / 2pi) + log of the integral of sqrt(det Fisher information) + o(1)

BIC drops the geometry term. For a Bernoulli model NML complexity is the log of a sum over counts, within a constant of (1/2) log n. [a02]

### 2.4 AIC versus BIC

MDL and Bayes factors act like BIC: consistent (they find the true model if it is in the set) but prediction-suboptimal by about a factor of order log n. Cross-validation and AIC act the other way. The switch distribution loses only log log n. [a04, c20, K01 E]

Practical reading: if the goal is "find the true rule", length penalties are right. If the goal is "best prediction on a new input", a held-out check is at least as good.

### 2.5 Misspecification

All of the above assumes the truth, or something near it, is in the model set. When every candidate is wrong:
- Gruenwald and Langford (2007) proved there is a countable classifier set and a distribution where the MDL and Bayes classifiers stay a fixed distance K above the best error in the class, for all large sample sizes. The case needs heavy-tailed priors and is artificial. [a19]
- Gruenwald and van Ommen (2017) showed it in ordinary regression: heteroskedastic noise, a homoskedastic model, polynomial models M0 to M50. With 100 points (about 50 at (0,0)) standard Bayes overfits. SafeBayes learns a learning rate eta, picked eta about 0.4, and matched the best predictor. Synthetic data only. [a20, d09]
- Fix: tilt the likelihood to p^eta with eta below 1, so the data part is damped. [a05, d08]
- Status: [E] for the theory and the constructed demonstrations (3 independent sources). No LLM-agent study measures it. [critique]

### 2.6 Neural networks

- Hinton and van Camp (1993) gave the first MDL view of neural nets: add noise to weights and trade squared error against the information in the weights (bits-back; cost equals KL between posterior and prior). Only small problems. [a11]
- Blier and Ollivier (2018) measured actual code lengths of deep nets. See section 3. Main lesson: prequential coding is tight; naive two-part coding with raw weights is hopelessly loose. [a12, b04, c10]
- Whitney et al. (2020): MDL and validation loss both depend on evaluation-set size, so representation rankings can flip as data grows. They propose surplus description length and epsilon sample complexity. [a26, c22, K22 E]

### 2.7 Probing and data analysis

- Hewitt and Liang (2019): add a "control task" with random labels per word type. A probe that does well on the control is memorising. [d07]
- Voita and Titov (2020) turned this into MDL probing: the code length of the probe labels, with the probe's own cost counted. [a15]
- Perez, Kiela and Cho (2021): Rissanen Data Analysis. A feature is useful if adding it shortens the online code length of the labels. [a21]

### 2.8 Language models as compressors

Next-token loss is code length: an LM plus arithmetic coding is a lossless compressor. [a17]
- Deletang et al. (2024) measured it. [b09]
- Huang et al. (2024) found benchmark score is near-linear in compression. [a23]
- Elmoznino et al. (2025) showed in-context learning is MDL in disguise: loss over a context equals its prequential code length. [a24]
- Mazor, Morgan and Pass (2026) prove next-token predictors equal monotone compressors up to an additive gap of 2. Pure theory. [b15]

### 2.9 MDL for program synthesis and ARC

- DreamCoder (Ellis et al. 2021) uses a Bayesian/MDL objective to grow a library of reusable primitives. Beats enumeration up to 400 million programs per task in 24 h. In LOGO and tower tasks no alternative solves over 60% of held-out tasks while DreamCoder nears 100%. Costs about a day on 20 to 100 CPUs. Compression gain is tangled with the neural recogniser. [c19]
- MADIL (Ferre 2025): MDL-guided MCTS over task models for ARC. [b21, d02]
- CompressARC (Liao and Gu 2025): a tiny network trained at test time to minimise the description length of one puzzle. [c15, d01]
- Hypothesis Search (Wang et al. 2024): LLM proposes hypotheses, code checks them. [c17, d05]

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MDL penalty is about (k/2) log n plus geometry term; acts like BIC | k parameters, n points; AIC/CV differ by log n factor in prediction rate | Grunwald and Roos 2019 [a03, a04] | [E] K01 |
| Two-part MDL and Bayes can be inconsistent under misspecification | Error stays at least K above best in class for all large n (constructed case) | Gruenwald and Langford 2007 [a19] | [E] K02 |
| SafeBayes fix in regression | 100 points, eta about 0.4, matches best predictor; standard Bayes overfits | Gruenwald and van Ommen 2017 [a20] | [E] K02 (synthetic only) |
| Raw float32 two-part code is terrible | MNIST uniform 199 kbits; two-part >8.6 Mbits (ratio >45). CIFAR10 >428 Mbits (ratio >2500) | Blier and Ollivier 2018 [a12, b04, critique] | [S] K03 |
| Prequential code is tight | MNIST 4.10 kbits, ratio 0.02, 99.5% acc. Variational 24.1 kbits, ratio 0.12, 95.5% acc. CIFAR10 prequential 45.3 kbits, ratio 0.27, 93% | Blier and Ollivier 2018 [c10] | [S] K03 |
| Random labels cannot be compressed | Code stays near log2(10) bits per label on MNIST; true labels go far below, about half the code in weights | Blier and Ollivier [a13, b05] | [E] K04 |
| Catch-up effect | CIFAR-10: per-label cost below uniform after about 1,000 samples; cumulative ratio above 1 until about 5,000 | Blier and Ollivier [a14] | [S] K05 |
| MDL probing beats accuracy | Accuracy wrong in 8 of 10 settings, MDL in none. POS layer 0 online code 96 vs 515 kbits (real vs control); layer 1 115 vs 717. Variational 85 vs 470 (layer 0). Accuracy 93.7 (real) vs 96.3 (control) | Voita and Titov 2020 [a15, b01, c08] | [S] K06 |
| Accuracy ranking flips with seed | Layer 1 vs 2: 97.48/97.31 (seed 1) vs 97.38/97.48 (seed 0) | Voita and Titov [b02] | [S] K06 |
| Real-task probes are small | 33-75 neurons vs about 260-480 for control tasks | Voita and Titov [a16, b03] | [S] K07 |
| Control tasks expose capacity | Linear 97.2 task / 71.2 control / 26.0 selectivity; MLP-1 97.3 / 92.8 / 4.5; MLP-2 97.3 / 93.2 / 4.2 | Hewitt and Liang 2019 [d07] | [S] K29 |
| LMs compress non-text | Chinchilla 70B: ImageNet patches 43.4% (PNG 58.5%); LibriSpeech 16.4% (FLAC 30.3%); enwik9 8.3% (gzip 32.3%) | Deletang et al. 2024 [a17, b09, c04] | [S] K08 |
| Counting model bytes reverses it | Adjusted rate on 1 GB: Chinchilla 1B about 211%, 7B about 1,400%, 70B about 14,000% (critique corrected earlier "1400-1500%") | Deletang [b10, c05, critique] | [S] K09 |
| Optimal model size per dataset size | Vanilla Transformers on enwik7/8/9: adjusted rate rises again beyond a critical size | Deletang [b11, a18] | [S] K09 |
| Tokenizer effect flips with model size | Raw rate on enwik9, 200K/6.4M/38M params, ASCII: 22.9/13.6/6.4%; last BPE row 19.3/16.4/9.0 | Deletang [d12] | [S] K28 |
| Score is near-linear in compression | Pearson about -0.95 per domain, -0.93 overall, RMSE 3.1%, 31 LLMs, 12 benchmarks. HellaSwag -0.881, TriviaQA -0.951, MMLU -0.890 | Huang et al. 2024 [a23, c06, d11] | [E] K10 |
| That law is weaker out of domain; base models only | Out-of-domain correlation "significantly weaker"; fine-tuned models not general compressors | Huang [c07, b13] | [E] K10 |
| MDL example selection for ICL | GPT2-XL, 8 datasets, 3 seeds: TopK+MDL 60.16, TopK 58.14 (+3.5% rel), TopK+LocalE 51.36, majority vote 50.43, random 42.78 or 43.06 | Wu et al. 2023 [a22, c11] | [S] K11 |
| That score is confidence | Minimising the label code length equals picking examples that make the model confident | Wu [c12] | [S] K11 |
| Word order and label compression | MNLI labels compress to 50% of prior with word order, 75% with shuffled words; CoLA incompressible without word order | Perez et al. 2021 [a21] | [S] K12 |
| ICL prefers simple explanations | Prequential ICL beats train-risk ICL at short contexts on all tasks, 5 seeds, 10,000 meta-train tasks of 1,000 points; advantage vanishes with data | Elmoznino et al. 2025 [a24, c01, c02] | [S] K13 |
| GPT-4 does not do this on Mastermind | Much higher cross-entropy than small meta-trained ICL models and than a marginal-label baseline; gpt-4o run was already one-example-at-a-time | Elmoznino [b17, c03, d15] | [S] K14 |
| MDL regulariser on formal languages | Dyck-1 MDL net size 139, test gap +0.1%; L1/L2 nets 460-600 units, gaps up to 11-13% | Abudy et al. 2025 [b19] | [C] K15 |
| Optimising MDL from random init fails | Hand-init 100% at about 3.4e2 bits; variational KL coef 1.0 gave 54% at 2.64e3 bits | Shaw et al. 2026 [b20] | [C] K15 |
| MADIL on ARC | 69 of 400 eval tasks fit, 57 correct (82% generalisation), 53 on first try, 180 s budget; 59 vs Icecuber 117 under stricter count; 80% of solutions in first 20 s | Ferre 2025 [b21, d02] | [E] K16 |
| CompressARC on ARC | 20.0% pass@2, 18.5% pass@1, 24.25% pass@5, 26.0% pass@10, 31.25% pass@100 on 400 eval; 34.75% pass@2 on train; 76K params; 138 h for 400 puzzles (about 20.7 min each, RTX 4070) | Liao and Gu 2025 [c15, d01] | [E] K16 |
| CompressARC steps | Eval pass@2 at 100/200/500/1000 steps: 1.25/6.0/15.0/19.25%; peak 21.5% at 1500; U-Net on target puzzle only 0.75% | Liao and Gu [d01, c16] | [E] K16 |
| Hypothesis Search | 100 ARC tasks: direct 17%, program-only 23%, summarised hypotheses 30%, human-selected 33%, human-written 45% | Wang et al. 2024 [c17, d05] | [S] K17 |
| Held-out validation selects programs | 200 examples at length 10: 100% test accuracy on parity, CAP, IsPrime where SGD stays near chance; IsPrime+47 reaches 80.6% at n=100; SHA-256 parity near chance | Singhal et al. 2026 [c18] | [S] K17 |
| False positives among fitting programs | About 9% of train-fitting programs are wrong on test; majority vote clears about half of problems that have one | Li et al. 2024 [d04] | [S] K25 |
| MDL-style aggregation of samples | KELM T-F1 47.4 vs greedy 46.9; WebNLG 29.3 vs 29.1; GenWiki 24.3 vs 23.7 (gpt-3.5) | Nair and Wang 2024 [b22] | [S] K18 |
| MDL pruning of stored rules | ToolHop test-rand 27.6 to 31.1 (72 rules); unseen 42.1 to 43.1. BFCL test-rand 54.8 to 56.6, unseen 47.6 to 48.5, rules 151 to 121. SD 1.2-1.6. Prompt merging 27.5 vs MDL 31.1 (ToolHop), 52.1 vs 56.6 (BFCL) | Gao et al. 2026 [b23, d14] | [S] K19 |
| Description-length difficulty | Discovery point matches identifiability bound in 89% of cases; r=+0.85 with structural size, r=-0.007 with growth | Ganeshan 2026 [b24] | [S] K20 |
| LLMs cannot write the shortest program | Length 128, GPT-4o accuracy 35.6/15.0/29.6/24.8/6.5/33.3% (Audio-16, Audio-8, MFCC, DNA, Text, Synthetic); Llama-3.1-405B 18.0/10.1/24.2/22.5/9.6/18.0; Llama-3.1-8B 5.9/3.9/8.8/3.7/1.4/8.5; programs longer than gzip (precision above 1) | Kolmogorov Test 2025 [c13, d13] | [S] K21 |
| Rankings depend on data size | MNIST and ELMo POS: MDL and validation choose different representations at different set sizes | Whitney et al. 2020 [a26] | [E] K22 |
| Non-vacuous bound for GPT-2 124M | SubLoRA 12.12 bits per dim; LoRA 13.09; subspace 14.59; original 70.76 (vacuous); random guess 15.62; 96.41% error | Lotfi et al. 2024 [a25] | [S] K23 |
| Spurious fits with few examples | 21 ARC training tasks have fits wrong on test; 21 of 62 search failures need non-compressive steps | Ferre [d03] | [S] K26 |
| Fit-only selection overfits | MiniSCAN: T=3 N=1 beat N=5; plain sampling plus vote does not reliably help rule induction | Qiu et al. 2024 [d06] | [S] K27 |

## 4. Mechanisms and models

Each mechanism is given in a form an engineer can build.

### 4.1 Two-part score (crude MDL)

score(H) = L(H) + L(D given H). L(D given H) = sum over examples of -log2 p(example under H). L(H) = bits to write H under a fixed coding scheme.

For an agent: H is a candidate rule or program. L(H) can be the token count of its text, or -log2 of its probability under a fixed LM. L(D given H) is 0 bits if H reproduces every example exactly and large if it fails. Crude MDL is arbitrary because L(H) depends on the scheme. [a08] So: fix the scheme once, use one model and one tokenizer, and compare only candidates against each other. [K28]

### 4.2 Prequential code (predict-then-reveal)

Procedure:
1. Order the examples x1..xn.
2. For i = 1..n, fit (or condition) on x1..x(i-1), assign probability p(xi given past), add -log2 of it.
3. Total = code length. No separate model cost is needed: the cost of the model is paid by the early mistakes.

Why it works: a model that is too flexible predicts badly early and pays for it. Random labels never get cheaper than uniform. [a13] Elmoznino et al. show an LM's next-token loss over a context is exactly this quantity. [a24]

For an LLM agent: for each candidate rule R, prompt "Rule R. Input x1 -> output" and read the log-prob of the true output; continue through the examples. A fixed program has L(D given H) of zero or infinity, so prequential scoring helps mainly when candidates are soft (probabilistic or natural-language rules).

### 4.3 NML

NML probability of data under model M: p(D given M) = p(D at its best fit) / sum over all D' of p(D' at its best fit). The denominator is the complexity. Its log is COMP(M). Computable exactly for small discrete models (Bernoulli: a sum over counts of C(n,n1) (n1/n)^n1 (n0/n)^n0). [a02] For a pool of candidate rules over a small discrete output space this gives a principled complexity charge. Usually approximate with (k/2) log n.

### 4.4 Damped likelihood (SafeBayes)

Replace the data likelihood by its eta-th power, so the data term is multiplied by eta. eta = 1 is standard; eta = 0 leaves the prior. Choose eta by prequential score: for each eta, predict each next example, pick the eta with the lowest sum of prediction losses. [a20, a05] In an agent: score(H) = L(H) + eta * L(D given H) with eta in {0.25, 0.5, 1}; choose eta on held-out examples or from the class record. Not tested on LLM hypotheses (K26).

### 4.5 MDL probing

Online code of labels given a representation: split the data into blocks, train the probe on block 1, code block 2 with it, train on blocks 1+2, code block 3, and so on. Sum the codes, plus the uniform code for the first block. Variational version: sum of the KL term (model cost) and the data code. [a15] Compare against a control task with random labels. Good representation = short code for real labels, long code for control. [b01]

### 4.6 Rissanen Data Analysis

Compute the online code length of the labels with and without a feature (word order, a sub-question). The drop in bits is the feature's value. Only compare estimates from the same learner and block layout. [a21] Use for scaffold ablation: bits saved on a fixed labelled set by adding a scaffold step.

### 4.7 Bits per character as a quality proxy

BPC of a base model on fresh in-domain text: -sum log2 p(token) / number of characters. Normalising by characters, not tokens, removes tokenizer effects. Across 31 base models the score is linear in it. [a23, d11] Only compare within one model. [K28]

### 4.8 Test-time compression (CompressARC)

For one puzzle, train a 76K-parameter network from scratch for 2000 steps to minimise reconstruction loss plus the KL cost of the latent code (a bits-back objective). The puzzle's own description length is minimised, and the output for the test grid comes out. 18.5% pass@1 at about 20.7 minutes each. [d01] No pretraining. This is a generator, not a ranker.

### 4.9 MDL-guided program search (MADIL)

MCTS over task models. A task model is a program in a small DSL. Value = compression of the training pairs (inputs and outputs) under the model. A fit is accepted if it encodes all training pairs. Generalisation of fits is 82%; recall is low (69 of 400 fit). The authors admit some expression lengths are badly designed and that the data/model weight needs revising. [d02, d03]

### 4.10 MDL rule consolidation (RIMRULE)

Have the LLM propose rules from failures. Then choose a subset of rules minimising L(rules) + L(errors given rules). Result: 7% to 20% fewer rules, higher accuracy on the random split. [b23, d14] Unseen gains are inside noise.

### 4.11 Propose-then-verify with a held-out set

LLM proposes many programs. Score each on held-out data. Keep the best. No gradients. [c18, c17] This is the practical form of the fit term. Length is optional.

## 5. What holds up

### Replications and consistency

- **Penalty theory**: same result from Rissanen, Schwarz, Wallace-Freeman and Grunwald's review; BIC-like behaviour is standard. [E, K01]
- **Random labels are incompressible**: shown in Blier and Ollivier, in Voita and Titov (control tasks), and from the other side by Hewitt and Liang. [E, K04]
- **Compression tracks capability**: Huang et al. found it across 31 models. Yuan et al. 2025 report a consistent "information capacity" within a series across 56 models, with a strong linguistic bias. Two groups on related ideas; Yuan's correlations were not extracted. [a23, b14] [E, K10]
- **Data-size dependence**: Whitney et al. and the catch-up effect in Blier and Ollivier point the same way. [E, K22]
- **ARC**: MADIL and CompressARC are different systems that both show pure compression is verified but weak and slow. [E, K16]

### Failures and limits

- **No replication of Wu et al.** Search tools were blocked, so absence of evidence is weak. The paper itself says TopK helps only on small-label NLU, not on QA, multi-choice or NLG; gains shrink with a smaller retrieval set. In the OPT scaling figures, SST-2 plateaus after 1.3B, and on SNLI a 30B OPT beats 175B. [d10]
- **MDL selection reduces to model confidence** in Wu et al. [c12]. The MDL label adds little over a confidence heuristic. Our schema already rejects verbal confidence as a stopping rule (4b); logit confidence is a different quantity.
- **Raw versus adjusted accounting**: Deletang's raw rates make LLMs look like great compressors; counting weights reverses it. Any "LLM compresses X%" claim needs the accounting stated. [critique, b10]
- **Huang's law has a boundary**: base models, in-domain text, short context only. Elmoznino shows GPT-4 does not act as a prequential Occam learner on a novel task. These do not strictly conflict (average benchmark skill versus one novel task), but they cap how far a length tie-break can be trusted. [critique]
- **Optimisation**: MDL objectives are hard to optimise from random init (Shaw et al.; Abudy et al.). The MDL optimum exists but search does not find it. [b19, b20] [C]
- **Misspecification**: proven or demonstrated only in constructed settings. Real-data demonstrations are few. [a05]
- **MDL consolidation** has no recency or usage baseline; unseen gains +1.0 and +0.9 sit below an SD of 1.2 to 1.6. [d14]
- **MDL probing evidence** is a single paper plus a control-task precursor. Probe widths were not rechecked. [critique]

### Moderators

| Moderator | Effect |
|---|---|
| Number of examples | Complexity penalty matters most when few; vanishes with enough data (Elmoznino, Blier catch-up) |
| Model class contains truth | If not, plain MDL can be inconsistent (K02) |
| Code scheme | Raw weights terrible, prequential tight (K03) |
| Tokenizer, model size | Compression rate direction flips (K28) |
| Domain | Linear law weaker out of domain (K10) |
| Label space | Wu et al. gains need small closed label sets |

### Interventions that worked

- Prequential coding instead of weights-plus-fit. [c10]
- Control tasks plus complexity cost for probes. [b01]
- Eta below 1 in the misspecified regression case. [a20]
- Held-out validation of LLM-proposed programs (100% at 200 examples where SGD fails). [c18]
- Summarising hypotheses before coding them (17 to 30% on ARC). [c17]
- Test-time compression with no pretraining (20% pass@2). [d01]

### Interventions that did not

- Asking an LLM directly for the shortest program. [c13]
- MDL aggregation of sampled outputs over greedy (gains of 0.0 to 0.6 T-F1). [b22]
- Plain sampling plus majority vote for rule induction (does not reliably help). [d06]
- Optimising an MDL net from random init. [b20]
- Fit-only selection with many hypotheses (overfits exemplars). [d06]

## 6. Language models

### How LMs behave on these tasks

1. **As compressors**: strong on raw rate, weak once weights are counted. Chinchilla 70B beats PNG, FLAC and gzip on raw rate (43.4 vs 58.5; 16.4 vs 30.3; 8.3 vs 32.3). Adjusted for 1 GB of data it is about 14,000% of raw. [b09, b10, critique]
2. **As a benchmark proxy**: BPC predicts average benchmark score linearly (r about -0.93 to -0.95, 31 base models). [a23]
3. **As rule-chooser** under prompts: the model-confidence version of MDL helped GPT2-XL by 2.02 points (58.14 to 60.16). [a22]
4. **As Occam learner**: meta-trained small transformers behave like prequential coders; GPT-4 / gpt-4o did not on Mastermind. Prompt format, meta-training and task difficulty were not separated. Scale is unlikely to be the cause. [a24, d15]
5. **As shortest-program writer**: poor. GPT-4o 6.5 to 35.6% accuracy at length 128 depending on modality; programs longer than gzip. A trained 1.5B SeqCoder gets 36 to 84%. [c13, d13]
6. **As hypothesis proposer**: good when code checks. Summarised hypotheses lift ARC from 17% to 30% (100 tasks). Fitting programs almost always generalise. [c17, d05]
7. **As an ARC solver paired with compression**: pure compression systems get 18.5 to 20% (CompressARC) and 57 correct of 400 (MADIL, about 14%; 69 of 400 fit). LLM program sampling with GPT-4o reached 42% on the public eval; the top private score rose from 33% to 55.5% in 2024. [d16]

### What changed it, by how much

| Change | Effect | Source |
|---|---|---|
| Prompt: direct to program to summarised hypotheses | 17% to 23% to 30% | [c17] |
| MDL-picked in-context examples | +2.02 points mean (58.14 to 60.16), GPT2-XL | [a22] |
| MDL consolidation of rules | +3.5 (ToolHop random split), +1.8 (BFCL random); unseen +1.0, +0.9 within noise | [d14] |
| MDL aggregation of samples | +0.0 to +0.6 T-F1 | [b22] |
| More test-time steps in CompressARC | pass@2 1.25% (100 steps) to 20.0% (2000) | [d01] |
| More samples in CompressARC | pass@1 18.5% to pass@100 31.25% | [d01] |

### Where the gap is

The false-positive rate among fitting programs is about 9%. A vote already removes about half of those problems. So the largest possible lift from a length tie-break is a few percent of problems, and only on fit-but-disagree cases. No study tested a shortest-fit rule there. [d04, K25]

## 7. What our agent should take

Format: item; schema part; status; evidence.

### Add now (established)

1. **Memorisation is not explanation. Reject a fit that costs as many bits to state as the data.** Part: G3 / S7. Status [E]. Evidence: K04; a13, b05, b03, c09. In practice this strengthens G3: a pass must be on something not fitted to. A rule whose statement is as long as the list of examples is a lookup table, not a rule.
2. **Length is the last tie-break, after held-out fit, symmetry and vote. It never replaces a held-out check.** Part: S7. Status [E] for the principle: MDL is BIC-like and not prediction-optimal against validation (K01), and a check beats a prior when a check exists. Evidence: K01, a04, c20. The size of the remaining room (K25) is [S].
3. **Do not read "shortest" as "true" when the true rule may be outside the proposal set.** If every candidate fails the held-out example, do not rank by length; go to S5/S6. Part: S7 / G3. Status [E]. Evidence: K02; a05, a19, a20, d08, d09.
4. **Compare lengths only within one model, one tokenizer, one example count.** Part: S7. Status [E] for example-count dependence (K22; a26, c22); [S] for tokenizer dependence (K28; d11, d12). Recheck the ranking at a lower example count before trusting it.
5. **Count the cost of the scaffold when comparing explanations.** Part: G7. Status [S] for the numbers (K09, K03) but G7 already requires it. No schema change beyond noting the MDL basis.

### Test first (not yet established; see UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Shortest-fit as tie-break on fit-but-disagree cases vs first-fit, vote, confidence at equal tokens | S7 | [S] | K25, K17; d04, d05, d06 |
| T2 | Which length: token count, LM log-prob, prequential code | S7 | [S] no comparison exists | K21, K26; d03, d13 |
| T3 | Damped complexity weight (eta below 1) with 2-5 examples | S7 | [S] | K02, K05, K26; a20, a14, d03 |
| T4 | Scrambled-label control on a candidate rule | S7 / G3 | [S] | K29, K04; d07, a13 |
| T5 | One hold-out example before any length rule | S4 / S7 | [S] | K27; d06 |
| T6 | Prequential (sequential) scoring of soft rules | S7 | [S] | K03, K13; c10, a24 |
| T7 | MDL-picked in-context examples (confidence) on a current model | O / S3 | [S] | K11; a22, c12, d10 |
| T8 | MDL pruning of stored lessons vs recency or usage | memory | [S] | K19; b23, d14 |
| T9 | Rissanen Data Analysis as scaffold-ablation metric | evaluation | [S] | K12; a21 |
| T10 | Per-token log-loss as cheap quality proxy for candidates | S7 | [S] | K10; a23, d11 |
| T11 | Compression score as ranker of LLM-proposed ARC programs | S7 | [S] none tested | K16, K17; b21, c15, d01 |
| T12 | Rule size as difficulty gauge for S0 | S0 | [S] | K20; b24 |

## 8. Concrete tests on our bench

All arms get the same token budget. Setup cost for any arm that scores lengths is counted.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC and rule-induction items where at least two LLM-proposed programs fit all given examples and disagree on the test input | (a) first-fit, (b) majority vote over test outputs, (c) model confidence (mean log-prob), (d) shortest-fit by token count | Accuracy on the fit-but-disagree subset; share of items where (d) changes the answer from (b) | Small: a few points at most, since about 9% of fits are false positives and a vote clears half [K25] |
| T2 | Same items | Length by (a) token count of code, (b) LM log-prob of code under a fixed prior, (c) prequential log-prob of examples under the rule text | AUC of length for predicting correctness on the test | Unknown. (b) or (c) likely beat (a); (a) is cheapest |
| T3 | Rule induction with 2, 3, 5 examples | score = L(H) + eta * L(D given H), eta in {0.25, 0.5, 1}, vs raw fit | Held-out accuracy by example count | eta below 1 helps at 2-3 examples; no gain at 5 |
| T4 | Rule items | Same selector with and without a scrambled-label pass (fit scrambled outputs; if equally good, discount the fit) | Rate of false-positive picks | Cuts false positives modestly; costs one extra pass |
| T5 | ARC-like items | Hold out 1 of k examples before any length rule vs fit on all k | Accuracy and tokens | Fewer spurious fits (MiniSCAN T=3, N=1 beat N=5) |
| T6 | Soft-rule items (natural-language rules) | Score by total fit vs prequential per-example log-prob | AUC for correctness | Prequential slightly better with few examples [K13 single] |
| T7 | Few-shot classification, small label sets | Random vs TopK vs TopK + lowest label code length vs TopK + confidence only | Accuracy | MDL close to confidence; gain over confidence near zero [c12] |
| T8 | Lesson memory, long runs | Prune lessons by (a) recency, (b) usage count, (c) minimum L(lessons) + L(errors given lessons) | Accuracy on unseen classes at equal prompt tokens | Roughly equal to usage; gains below 1 SD |
| T9 | Any scaffold step (e.g., S2 representation) | Online code length of gold labels with and without the step | Bits saved per item vs accuracy change | Same direction as accuracy; less noisy |
| T10 | Candidate answers | Rank by mean per-token log-prob of the candidate vs by vote | Rank correlation with correctness | Moderate within one model; weak across domains [c07] |
| T11 | ARC public eval | LLM proposes N programs; rank fitting ones by (a) vote, (b) MADIL-style compression of the training pairs under the program | Accuracy | Unknown; small if (b) only breaks ties |
| T12 | S0 gate data | Rule size vs plain pass rate | Correlation | Possibly useful; r=0.85 was on recurrences, not LLM items |

Log for each run (SCHEMA section 6): the selector's pick vs the best candidate available, the number of fit-but-disagree items, and tokens.

## 9. What does not transfer, and why

- **Asking the model to write the shortest program or rule.** It does poorly (GPT-4o 6.5 to 35.6%; programs longer than gzip). Compute length in code. [c13, K21]
- **Raw-compression claims.** Chinchilla beating gzip is a raw-rate statement. With weights counted it loses. Do not cite it as evidence that LLM judgement is parsimonious. [b10]
- **Weight-code results for deep nets (float32 two-part, variational bits-back).** The model of interest has no weights we can edit or count. Only the prequential idea transfers. [c10]
- **MDL regularisation and architecture results (Dyck nets, Kolmogorov-complexity objectives).** They act on training, not on a scaffold. Optimisation from random init fails. [b19, b20]
- **CompressARC as a component.** About 20.7 GPU-minutes per puzzle; G7 rules it out as a generator in an LLM scaffold. Its idea (compress the puzzle itself) is a different system. [d01]
- **Non-vacuous generalisation bounds, singular-learning links.** Background only. [a25, c25]
- **The linear compression-score law.** It ranks base models. It does not tell us which of two candidates inside one run is right. [a23, c07]
- **AIC/BIC debates for continuous parameter models.** Our candidates are discrete rules or programs; the (k/2) log n term has no clean meaning there.
- **Human simplicity preferences.** Covered in other documents in this series; this one is statistical MDL only.

## 10. Open questions

1. Does shortest-fit beat first-fit, vote and confidence at equal tokens on fit-but-disagree cases? Decides whether S7 uses length at all. [critique GAP 1]
2. Which length measure predicts correctness best for LLM hypotheses: tokens, LM log-prob, prequential? [GAP 2]
3. Does a damped weight help with few examples, and when the true rule is outside the proposal set? [GAP 3]
4. Does the Wu et al. gain replicate on a current model, and does it beat plain confidence? [GAP 4]
5. Are Huang and Deletang numbers stable across tokenizers and families? Yuan et al. report linguistic bias; correlation values were not extracted. [GAP 5]
6. Can a compression score rank LLM-proposed programs? No test found. [GAP 6]
7. Why did GPT-4 fail prequential Occam on Mastermind? Prompt format, meta-training and task difficulty are unseparated. Forced sequencing is not the fix because the run was already sequential. [GAP 7, d15]
8. Does MDL consolidation of lessons beat recency or usage pruning on unseen tasks? [GAP 8]
9. Rissanen 1978 was not opened; the founding derivation is taken from Grunwald and Roos. [GAP 9, K30]
10. Does the catch-up effect (code above uniform until about 5,000 samples) have an analogue for LLM context, where the model starts with a strong prior?
11. Does an explicit length rule in the prompt (as opposed to code) change what the model proposes?

## 11. Sources

[V] = opened and read this session. [M] = snippet or not opened.

| Source | Mark | URL |
|---|---|---|
| Grunwald and Roos (2019) Minimum description length revisited | [V] | https://arxiv.org/abs/1908.08484 |
| Grunwald (2004) A tutorial introduction to the minimum description length principle | [V] | https://arxiv.org/abs/math/0406077 |
| Hinton and van Camp (1993) Keeping neural networks simple by minimizing the description length of the weights | [V] | https://www.cs.toronto.edu/~hinton/absps/colt93.pdf |
| Blier and Ollivier (2018) The description length of deep learning models | [V] | https://arxiv.org/abs/1802.07044 |
| Voita and Titov (2020) Information-theoretic probing with minimum description length | [V] | https://arxiv.org/abs/2003.12298 |
| Hewitt and Liang (2019) Designing and interpreting probes with control tasks | [V] (PDF); arXiv entry b28 [M] | https://aclanthology.org/D19-1275.pdf ; https://arxiv.org/abs/1909.03368 |
| Deletang et al. (2024) Language modeling is compression | [V] | https://arxiv.org/abs/2309.10668 |
| Gruenwald and Langford (2007) Suboptimal behavior of Bayes and MDL in classification under misspecification | [V] | https://arxiv.org/abs/math/0406221 |
| Gruenwald and van Ommen (2017) Inconsistency of Bayesian inference for misspecified linear models | [V] | https://arxiv.org/abs/1412.3730 |
| Perez, Kiela and Cho (2021) Rissanen Data Analysis | [V] | https://arxiv.org/abs/2103.03872 |
| Wu, Wang, Ye and Kong (2023) Self-adaptive in-context learning | [V] | https://arxiv.org/abs/2212.10375 |
| Huang, Zhang, Shan and He (2024) Compression represents intelligence linearly | [V] | https://arxiv.org/abs/2404.09937 |
| Elmoznino et al. (2025) In-context learning and Occam's razor | [V] | https://arxiv.org/abs/2410.14086 |
| Lotfi et al. (2024) Non-vacuous generalization bounds for large language models | [V] | https://arxiv.org/abs/2312.17173 |
| Whitney et al. (2020) Evaluating representations by the complexity of learning low-loss predictors | [V] | https://arxiv.org/abs/2009.07368 |
| Yuan, Shao, Li (2025) Information capacity | [V] | https://arxiv.org/abs/2511.08066 |
| Mazor, Morgan, Pass (2026) Language modeling is monotone compression | [V] | https://arxiv.org/abs/2610.11031 |
| Abudy et al. (2025) A minimum description length approach to regularization in neural networks | [V] | https://arxiv.org/abs/2505.13398 |
| Shaw et al. (2026) Bridging Kolmogorov complexity and deep learning | [V] | https://arxiv.org/abs/2509.22445 |
| Ferre (2025) MADIL | [V] | https://arxiv.org/abs/2505.01081 |
| Nair and Wang (2024) MIDGARD | [V] | https://arxiv.org/abs/2405.05189 |
| Gao et al. (2026) RIMRULE | [V] | https://arxiv.org/abs/2601.00086 |
| Ganeshan (2026) Where induction runs out | [V] | https://arxiv.org/abs/2608.29411 |
| Kolmogorov Test authors (2025) The Kolmogorov Test | [V] | https://arxiv.org/abs/2503.13992 |
| Liao and Gu (2025) ARC-AGI without pretraining (CompressARC) | [V] | https://arxiv.org/abs/2512.06104 |
| Wang et al. (2024) Hypothesis search | [V] | https://arxiv.org/abs/2309.05660 |
| Singhal et al. (2026) LLM priors for ERM over programs | [V] | https://arxiv.org/abs/2510.14331 |
| Ellis et al. (2021) DreamCoder | [V] | https://arxiv.org/abs/2006.08381 |
| Kaushik et al. (2023) LLaMA-7B as predictor for entropy and compression | [V] preliminary | https://arxiv.org/abs/2306.04050 |
| Learning options via compression (2022) | [V] | https://arxiv.org/abs/2212.04590 |
| Compressibility measures complexity: MDL meets singular learning theory (2025) | [M] | https://arxiv.org/abs/2510.12077 |
| Li et al. (2024) Combining induction and transduction for abstract reasoning | [V] | https://arxiv.org/pdf/2411.02272 |
| Qiu et al. (2024) Phenomenal yet puzzling | [V] | https://arxiv.org/pdf/2310.08559 |
| Chollet et al. (2025) ARC Prize 2024 technical report | [V] | https://arxiv.org/pdf/2412.04604 |
| Rissanen (1978) Modeling by shortest data description | [M] | https://doi.org/10.1016/0005-1098(78)90005-5 |
| Schwarz (1978) Estimating the dimension of a model | [M] | https://doi.org/10.1214/aos/1176344136 |
