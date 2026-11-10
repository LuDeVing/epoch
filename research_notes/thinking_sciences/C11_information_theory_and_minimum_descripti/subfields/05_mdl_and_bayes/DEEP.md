# MDL and Bayes: deep document

*Subfield C11.05. Scope: code length matches probability; some MDL codes (normalised maximum likelihood, NML) have no general Bayes counterpart. Why it matters for our agent: selection with priors. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K30), critique.md in this folder. Corrected values from critique.md are used where the first extraction was wrong. Evidence ids (a01..d19) point to the jsonl lines. Status: [E] established, [S] single source, [C] contested.*

## 1. What it is

Minimum description length (MDL) says: the best explanation of data is the one that gives the shortest total code for the explanation plus the data given the explanation. Bayes says: the best explanation has the highest posterior, prior times likelihood.

The bridge is one line. Any code length L(x) in bits defines a probability 2^-L(x). Any probability p(x) defines a code of length -log2 p(x). So at the level of coding, MDL and Bayes are the same language (a03, K01). A language model that gives next-token probabilities is a compressor through arithmetic coding, and its summed negative log-probability over a text is the code length of that text (a10).

The two views part ways in three places.

1. **Which universal code.** To code data without knowing the best parameters you need a "universal" code. Four are in use: the Bayes mixture, the two-part code (describe the model, then the data), the prequential (predict-then-update, "online") code, and the NML code. They are different distributions. Bayes is one choice among four (a03, c15).
2. **NML.** The NML code (Shtarkov 1987) is the minimax-regret code: it makes the worst-case extra cost over the best-fitting model as small as possible, for every data sequence. It is not a Bayes mixture in general. For regular models it agrees with Bayes under the Jeffreys prior to leading order, (k/2) log n bits for k parameters. For Bernoulli it is within a constant. They differ at small n and for models with unbounded outcome spaces, where the plain NML normaliser is infinite and "luckiness" functions (prior-like weights that need not be normalised) are needed (a04, a06, c15, c25).
3. **Misspecification.** When the model class does not contain the truth, Bayes and two-part MDL can both fail to converge to the best member of the class, at any sample size (a07, a08).

What the subfield claim "NML has no Bayes counterpart" should say, after the critique: no general Bayes counterpart; equal only asymptotically or in special cases. Wikipedia (b01) states it more strongly than the review does.

For our agent the practical meaning is narrower than the theory. An agent holds several candidate answers or hypotheses and must pick one. Code length gives a score for each: how many bits the candidate needs to explain the evidence, plus how many bits the candidate itself costs. The prior is the cost of the candidate. The questions are whether such a score beats voting, whether it needs a prior, and where it misleads.

## 2. History and theories in depth

**Founding (1960s-1980s).**
- Solomonoff (1964) and Kolmogorov: the shortest program that outputs the data. The universal prior is 2^-K(h), where K is program length. Incomputable and tied to the choice of reference machine (b07, c18, a22). The Solomonoff bound: summed squared prediction error for any computable source mu is at most about K(mu) ln 2 (a21, a22).
- Rissanen (1978), "Modeling by shortest data description" [M, a01]. Two-part code. Cost of k parameters is about (k/2) log2 n bits, which is the BIC penalty. This identity holds for large samples only (b02).
- Shtarkov (1987), "Universal sequential coding of single messages" [M, a02]. Defines NML. Regret equals the log of the normaliser for every data sequence.
- Hinton and van Camp (1993) [M, a24]: description length as a regulariser for neural nets. MacKay (2003) [M, a23]: Bayes, evidence and Occam factors in one book.

**Consolidation (1990s-2000s).**
- Barron, Rissanen and Yu (1998) [M, a25] review of MDL.
- Vitanyi and Li (2000) (b07, b08, c18): "ideal MDL" equals Bayes with the algorithmic universal prior. Valid up to additive constants. For finite-set models it reduces to Kolmogorov's minimal sufficient statistic.
- Grunwald and Langford (2004/2007) (a07, c16): a constructed counterexample where Bayes and two-part MDL classifiers stay bounded away from the best-in-class error at every sample size. Largest gap about 0.161 at best error 0.2 (the paper text reads 0.1609; rounding). Upper bound on the Bayes classifier error is H(mu), the binary entropy of the best error. A randomised consistent alternative exists. The authors warn it covers only some versions of Bayes and MDL.
- Grunwald and van Ommen (2017) (a08, c17): in regression with heteroskedastic data and a homoskedastic model, the Bayes posterior moves onto ever higher-dimensional models. Squared-error risk stays poor over a very large range of n. SafeBayes (learning rate below 1, i.e. tempered likelihood) repairs it in simulation. It tends to pick a small rate when the posterior is not cumulatively concentrated.

**Modern review (2019).** Grunwald and Roos, "Minimum Description Length Revisited" (a03-a06, a26, a27, c15, c25). Main points: every code is a probability; the four universal codes; NML as minimax regret; the horizon problem (Bayes codes are horizon-independent but lack NML's worst-case meaning; horizon-independent non-Bayesian codes are rare); luckiness functions; lasso as an MDL estimator whose luckiness is not a normalised prior (sparsity favoured because log C(n,k) grows about linearly in k).

**Deep learning era (2017-2024).**
- Blier and Ollivier (2018) (a09): prequential code length as a measure of deep model compression, far tighter than variational or two-part codes.
- Voita and Titov (2020) (a16): MDL probing.
- Dziugaite and Roy (2017) (a18) and Lotfi et al. (2022, 2024) (a19, c14): PAC-Bayes and compression-based generalisation bounds that are non-vacuous for large nets and then LLMs.
- Lotfi et al. (2023) (b09-b11, c13): the marginal likelihood (the Bayes code length) can anti-correlate with generalisation.
- Deletang et al. (2024) (a10, a11): language models are compressors.
- Huang et al. (2024) (a17): compression of external text predicts benchmark score across models.

**In-context learning as Bayes or compression (2022-2026).**
- Xie et al. (2022) (a20, b17, b18): ICL as implicit Bayesian inference over latent concepts.
- Zhang et al. (2023) (b19, c11): ICL as Bayesian model averaging with O(1/T) regret (theory).
- Elmoznino et al. (2025) (a13-a15, c21): ICL loss summed over a sequence is a prequential code length; training on it rewards low error and low complexity together. This is the compression view. It makes the same predictions as the Bayes view; no measured result separates them (critique).
- Falck et al. (2024) (b12-b14, c03, c04, c28): martingale test of Bayesian behaviour in LLMs.
- Chlon et al. (2026) (c12): LLMs are Bayesian in expectation, not in each realisation.
- Arora et al. (2025) (b15, b16, c05, c06, c26, d14): Bayesian scaling laws.
- Muller et al. (2022) (b20, c09) and Grau-Moya et al. (2024) (a21, b21, c10): meta-training toward Bayes posteriors and toward Solomonoff induction.
- Qiu et al. (2026) (b24, b25, c07, c08, c27): Bayesian teaching.

**LLM selection and agent use (2022-2026).** Self-consistency tables (d01), self-certainty (d02), PiCSAR joint log-probability (d03, d04), shortest-chain results (d05, d06, d08, d16), BoxingGym (c19, c20), RIMRULE and MIDGARD two-part objectives (d11, d12), stacking against model averaging (d10), Memory Tax (d17), belief tracking (d18).

## 3. Core findings with exact numbers

Status column: E established, S single source, C contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Code length and probability are interchangeable; Bayes, two-part, prequential and NML are different universal codes | Regret order (k/2) log n for k parameters in regular models | Grunwald and Roos 2019 (a03, c15, c25) [V] | E |
| NML is minimax regret; matches Bayes-Jeffreys only asymptotically or in special cases; plain NML diverges for unbounded spaces | Bernoulli: (1/2) log n + constant | a04, a06, c15 [V] | E |
| Bayes and two-part MDL can be inconsistent under misspecification | Max gap to best error about 0.161 at best error 0.2; bound H(mu) | Grunwald and Langford (a07) [V] | S (one group, theory) |
| Bayes regression inconsistent under misspecification; tempering (learning rate below 1) repairs it | Simulated polynomial regression; risk poor over a very large range of n | Grunwald and van Ommen (a08, c17) [V] | S |
| Prequential code is much tighter than variational or two-part for deep nets | MNIST 4.10 vs 24.1 kbits (accuracy 99.5 vs 95.5); CIFAR-10 45.3 vs 89.0 kbits (93.3 vs 61.6); float32 two-part about 32 Mbits | Blier and Ollivier 2018 (a09) [V] | S |
| MDL probing separates real from control tasks; accuracy does not | Accuracy ranked wrongly in 8 of 10 settings; MDL right in 10 of 10 | Voita and Titov 2020 (a16) [V] | S |
| LMs compress many modalities | Chinchilla 70B: ImageNet patches 43.4% (PNG 58.5%); LibriSpeech 16.4% (FLAC 30.3%); enwik9 raw 8.3% (gzip 32.3%, LZMA2 23.0%), 2048-byte chunks. Counting parameters erases the gain on 1 GB | Deletang et al. 2024 (a10, a11) [V] | S |
| Benchmark score is near-linear in compression across models | Pearson about -0.95 per domain, -0.93 overall; 31 LLMs; RMSE 3.1% | Huang et al. 2024 (a17) [V] | S (cross-model) |
| Non-vacuous bounds for LLMs, still loose | GPT-2 small: 12.12 BPD vs 15.62 random, 96.41% Top-1 error bound, 58.34% Top-100; larger models 11.95-12.12 BPD, not monotone; Top-100 slightly worse for larger (to 59.25) | Lotfi et al. 2024 (b22, b23, c14) [V] | E (2 papers) |
| Non-vacuous bounds for small nets | MNIST LeNet5 11.55% (SGD), 11.20% (full batch); bound size 6.23 KB to 0.38 KB (-94%); ImageNet 358 KB to 46.3 KB (-87%); CIFAR-10 ResNet-18 74.68% | Lotfi et al. 2022 (a19) [V] | E |
| Marginal likelihood can anti-correlate with generalisation; conditional version stays positive | CIFAR Laplace BMA, precision 1e2, 1e-1, 1e-3: sign depends on precision; exact rho not recovered | Lotfi et al. 2023 (b09-b11, c13) [V] | S |
| ICL as implicit Bayes; depth helps at equal loss; order matters | 12 vs 16 layers, same validation loss 1.33, accuracy 81% vs 85% | Xie et al. 2022 (a20, b17) [V] | E (with Zhang b19, Elmoznino a13) |
| ICL prequential code length = complexity plus error; training on it generalises better | 10,000 tasks x 2,000 points (80/20); prequential ICL beat a train-error-only learner on held-out tasks | Elmoznino et al. 2025 (a13) [V] | S |
| LLMs violate the Bayes martingale property, mostly at long horizon and in Gaussian tasks | n=50; Bernoulli m=n/2: mostly inside the 95% Bayes interval except GPT-4 at means 0.3, 0.5; m=2n more deviations; Gaussian n=100, m=50: all but GPT-3.5 deviate | Falck et al. 2024 (b12, b13, c03) [V] | S |
| The violation is small in bits | Excess code length 0.020/0.011 bits (Bernoulli) and 0.039/0.022 bits (4-way) for Qwen2.5 7B/14B; candidate mass above 0.999 | Chlon et al. 2026 (c12) [V] | S |
| Order sensitivity grows like log n; shuffle mixing gains log-loss | Qwen2-7B Jensen gap 0.1041 nats/token, slope 0.377 (CI 0.319-0.435); Llama-3.1-8B 0.00982, slope 0.147; 3,059 items; 16 permutations; positive gap for 54 of 58 n values | d13 (arXiv 2509.11208) [V] | S |
| Bayesian scaling law (GINC, NRMSE interp / extrap) | Bounded 0.0274 / 0.0621; logistic 0.0272 / 0.1138; Bayes 3M+1 params 0.0268 / 0.0814; original Bayes 0.0279 / 0.0493. Real LLMs mean NRMSE: logistic 0.1599, Bayes 0.1628, bounded 0.1637, power 0.1675 | Arora et al. 2025 (b15, c05, c26, d14), corrected by critique [V] | C |
| Post-training moves the fitted task prior | Llama 3.1 8B; 50 many-shot prompts per dataset; no numeric jailbreak rates in text | Arora et al. (b16, c06) [V] | S |
| Off-the-shelf LLMs plateau after round 1 in a Bayesian preference task; Bayesian teaching fixes it | Gemma original 37% aggregate (about 60% when human preferences match its prior); tuned models about 80% agreement with the Bayesian Assistant; p<0.001, 3 seeds; transfers to hotels and web shopping; verbal beliefs under 50% aligned | Qiu et al. 2026 (b24, b25, c07, c08, c27) [V] | S |
| PFNs approximate Bayes posteriors in one pass | Near-perfect GP mimicry; over 200-fold speedup | Muller et al. 2022 (b20, c09) [V] | E (with c10) |
| Meta-trained nets approach Solomonoff / CTW | Regret near CTW on variable-order Markov sources (256 steps, depth up to 24, 6k test sequences, 3 seeds) | Grau-Moya et al. 2024 (a21, b21, c10) [V] | E |
| Unnormalised sequence probability loses to majority vote | PaLM-540B GSM8K: greedy 56.5, weighted sum unnormalised 59.9, normalised 74.1, vote 74.4. AQuA 38.2 / 48.0 / 48.3 | Wang et al. 2023 (d01) [V] | E (with d02) |
| Self-certainty and perplexity trail voting | Llama-3.1-8B, 4-set average: SC 56.15, self-certainty 52.71, perplexity 51.08, Borda 56.51; MATH N=64: SC 63.40 vs 56.70 vs 51.96 | Kang et al. 2025 (d02) [V] | E (with d01) |
| Joint reasoning-plus-answer log-prob beats voting | Beats SC in 37 of 40 comparisons; at k=6 beats 16 of 20 baselines run at k=16 or 32; Llama-3.1-8B GPQA-D self-certainty 26.54 to 29.80; R1-Distill-Qwen-7B at k=6 +12.33 (AIME24), +12.78 (AIME25) over SC; shrinks or vanishes for Qwen3 non-thinking | Leang et al. 2025 PiCSAR (d03, d04) [V] | C |
| Highest-score chains are shorter and more accurate | Llama-3.1-8B: 16.43 sentences and 53.33% vs 64.72 sentences and 44.20% | d04 [V] | S |
| Shortest chain is most often correct for reasoning models | LN-Super-49B math avg: random 47.7, longest 28.9, shortest 63.4; R1-670B 78.2 / 58.9 / 83.3; short-1@k uses up to 40% fewer thinking tokens than majority; GPQA-D R1-670B shortest 75.8 vs random 76.2 | Hassid et al. 2025 (d05) [V] | E (d05, d08, d16, d06) |
| Accuracy rises then falls with thinking length | R1-Distill-Qwen-1.5B GSM8K: 82.2% at about 385 tokens, 87.3% at about 1,100, 70.3% at about 15,980; MATH-500 83.2 to 78.3 at about 16k | d06 (arXiv 2506.04210) [V] | S |
| Failed-step fraction predicts better than length | 10 reasoning models; HARP, GPQA-D, AIME25; 16 traces per question | d16 (arXiv 2509.19284) [V] | S |
| Entropy-weighted voting gives small or no gain | +0.5 to +3.4 in d07; sequential beats parallel in 43 of 45 configs (30 problems per set); tied plain vote in a 10-problem local test | d07, d09 [V] | C |
| BMA over LLM-written programs collapses onto one program | Weight 1.000 (hurricane, inland flood), 0.998 (wildfire); 250 programs per task; stacking has the same held-out ELPD with spread weights | Bhide et al. 2026 (d10) [V] | S |
| Two-part MDL inside agents | RIMRULE: ToolHop 31.1 vs 27.5 (prompt consolidation), BFCL 56.6 vs 52.1; rules 72 to 67 and 151 to 121. MIDGARD: ExplaGraph StCA 30.3 vs 23.7 greedy (gpt-3.5, T=10) | d11, d12 [V] | S each; K26 two sources |
| Explicit prior and Bayesian program writing did not reliably help LLM scientists | BoxingGym: 10 environments, 5 trials, 6 LLMs | Gandhi et al. 2025 (c19, c20) [V] | S |
| Prompt choice by mutual information | On average 90% of the way from average to best template | Sorensen et al. 2022 (b26) [V] | S |
| Most agent memory systems lose to chunked RAG | LongMemEval-s RAG 72.2 / 81.4 / 90.0 across three backbones; all memory systems lower | Memory Tax (d17) [V] | S |
| Prompting for belief updates is inconsistent; RL helps | Qwen3.5-9B update failure 60.0 to 69.0 with a prompt; RL cuts failures 70.9% on average | d18 [V] | S |

## 4. Mechanisms and models

Each item is written so an engineer can code it.

**4.1 Code length of a candidate (the base score).** Given token log-probabilities, the code length of text y given prompt x is L(y|x) = -sum_t log2 p(y_t | x, y_<t). Probability is 2^-L. Sum, never average, if you want a code length. Averaging (length-normalised) is bits per token, a different quantity. The raw sum favours short text; PaLM's unnormalised weighting gave 59.9 vs 74.1 normalised on GSM8K (d01).

**4.2 Two-part score.** Score(h) = L(h) + L(data | h). L(h) is the cost to state the hypothesis (a prior in bits). L(data|h) is the misfit. In an agent: L(h) = tokens or symbols of the rule; L(data|h) = number of failures left uncorrected, times a weight. RIMRULE uses exactly this: rule symbol length plus uncorrected failures, weight alpha tuned on end-to-end accuracy (d11). The weight is a free knob; MIDGARD shows alpha=0.5 can drop every edge on some data (d12). Calibrate alpha on held-out items.

**4.3 Bayes mixture and posterior table.** Keep a list of hypotheses h_i with prior w_i. After each observation multiply w_i by p(obs | h_i) and renormalise. Prediction is the weighted mix. Code does the arithmetic; the model only supplies p(obs | h_i) or a hard 0/1 consistency. This is the Bayesian Assistant of Qiu et al. (uniform prior, max-expected-option, update after each choice; c27). Off-the-shelf LLMs do not do this internally after round 1 (c07), so the table must live in code.

**4.4 Prequential score.** L_preq = -sum_t log p(x_t | x_<t, h): score in order, predict then update. Blier and Ollivier show it is the tight measure for deep models (a09). For an agent: the value of a stored note is the drop in later-token loss with the note versus without. Not tested for agent memory (K30).

**4.5 Conditional marginal likelihood (hold-out score).** Split the evidence. Condition on the first part, score the second. The total marginal likelihood can flip sign against generalisation as prior precision changes; the conditional version stayed positively correlated (c13). Implementation: for each candidate program, run it on examples 1..k as context, score on k+1..n. This matches our G3.

**4.6 NML and luckiness.** NML(x) = max_theta p(x|theta) / sum_x' max_theta p(x'|theta). The normaliser is the model complexity. It is computable for small discrete models by enumeration (Bernoulli: sum over k of C(n,k) (k/n)^k (1-k/n)^(n-k)). For unbounded models the sum diverges, so a luckiness function restricts or weights the region (a06, c15). No LLM work uses it (K03, K29; the negative is weak because search APIs were rate limited).

**4.7 Tempered Bayes (SafeBayes).** Replace p(obs|h) by p(obs|h)^eta with eta below 1. Pick eta by which value gives the best sequential prediction (a08). In an agent, this down-weights evidence from a correlated or misspecified source (our G4). Untested in LLM aggregation (K27).

**4.8 Averaging versus selection.** Marginal-likelihood weighting over LLM-written programs gave weight 0.998 to 1.000 to one program (d10). Stacking (weights chosen by held-out predictive score) matched ELPD with spread weights. Rule: do not weight by raw marginal likelihood; weight by held-out score.

**4.9 Joint reasoning-plus-answer score (PiCSAR).** Score = log p(r|x) + log p(y|a,r,x), the log-probability of the chain plus the answer given the chain. Choose the argmax over k samples (d03). One extra forward pass for the answer term. It is a MAP rule with the model's own implicit prior.

**4.10 Short-m@k.** Launch k chains in parallel, stop when the first m finish, vote among those m (d05). Up to 40% fewer thinking tokens than majority vote. Only for reasoning models, only within one question.

**4.11 Order averaging.** Shuffle the order of evidence m times, query each, average the predictive distributions. Exact Bayes on exchangeable data is order-invariant, so variance across orders is a violation (c03). Mixing over permutations has a positive Jensen gain in log-loss (d13). Accuracy gain at equal tokens is unmeasured.

**4.12 Bayesian scaling law.** P(correct | n shots) = sum_i w_i p_i(shot)^(K n), normalised, with prior w_i over tasks, per-example likelihood p_i and efficiency K (c26). 3M+1 parameters for M tasks. A diagnostic of whether context moves the task prior. It fits about as well as a logistic curve on real LLMs (d14).

**4.13 Meta-trained predictors.** Train on tasks sampled from a prior (PFN, c09) or on random universal-machine programs (a21, c10). Needs training. Not a scaffold item.

## 5. What holds up

**Holds up well (two or more independent sources).**
- Code length equals negative log-probability; the four universal codes differ (a03, c15, c25; Vitanyi and Li c18, a22). [E]
- Non-vacuous but loose compression bounds for large nets and LLMs (a19, c14, a18). [E]
- Shorter finished chains are more often correct for reasoning models within a question (d05, d08, d16, d06). [E] Boundaries: reasoning models only; no stable effect for non-reasoning models (d08); GPQA-D R1-670B shortest 75.8 is below random 76.2 (d05); Qwen results anomalous, contamination suspected (d16); failed-step fraction beats length (d16).
- Raw sequence probability as a selection rule loses to majority vote (d01 PaLM-540B; d02 Llama-3.1-8B). [E]
- ICL is approximately Bayesian and order-sensitive, and depends on depth beyond loss (a20, b17, c03, d13, c12). [E] The size of the order violation for current frontier models is unknown.
- PFN and meta-trained approximations of Bayes and Solomonoff (c09, c10). [E]

**Single source, small tasks.** Martingale violations (Falck); excess code length in bits (Chlon, two Qwen sizes); Bayesian teaching (Qiu); prior shift in post-training (Arora); BoxingGym; RIMRULE; Memory Tax; stacking vs BMA (three tasks); MDL probing; prequential deep-net lengths; benchmark-compression correlation (31 models, cross-model only).

**Contested or weakened.**
- Bayesian scaling law "wins extrapolation": true only for the larger original law (0.0493); the matched-size law extrapolates at 0.0814, worse than bounded power (0.0621). Real-LLM differences are mostly not significant (b15, c05, d14). C.
- Qiu's "LLMs cannot update": Gemma original gets about 60% when users are filtered to those whose preferences match the model's prior, against 37% aggregate (critique correction 3).
- Larger models give tighter LLM bounds: only roughly. 124M 12.12, 354M 11.96, 458M 11.95, 773M 12.10, 849M 12.01 BPD; Top-100 error slightly worse for larger ones (critique correction 2).
- Joint-score selection (PiCSAR) beats voting in 37 of 40 comparisons, yet self-certainty trails voting (d02) and entropy weighting ties it (d09). The difference is the answer-conditioned joint term. One paper, so C.
- Marginal likelihood as a selection score conflicts with the folk belief that shorter total code means better generalisation. Fine for testing whether a prior fits, misleading for choosing a trained model (c13).

**Failed or null results.**
- Entropy-weighted voting added +0.5 to +3.4 (d07) and nothing in a 10-problem local test (d09).
- Explicit domain prior and PyMC model writing did not reliably help LLM scientists (c19, c20); the simplicity bias may reflect prompting, not a Bayes flaw.
- A belief-tracking prompt moved Qwen3.5-9B update failure from 60.0 to 69.0 (worse); RL fixed it (d18).
- Memory systems do not beat RAG (d17).
- A big pretrained LLM can fail to compress a new task: GPT-4 on Mastermind did worse than a small trained model (a13, K08).
- Sequential refinement beat parallel self-consistency at matched tokens in d07 (43 of 45 configs), against G11's "parallel beats extended thinking". Small sets, preprint, unresolved.

**Moderators.** Model type (reasoning vs non-reasoning); within-question vs across-question comparison; single exact answer vs open task; sample size n (NML and Bayes differ at small n, the usual agent regime); prior precision (marginal likelihood sign flips); chain length (peak then decline, d06); well-specified vs misspecified model class (Grunwald).

**Interventions that worked.** Length-normalising before weighting (d01); joint chain-plus-answer score (d03); shortest-first with voting (d05); MDL consolidation of rules over prompt consolidation (d11: +3.6 ToolHop, +4.5 BFCL); stacking instead of BMA (d10); Bayesian teaching by fine-tuning (c07); conditional rather than total marginal likelihood (c13); MI prompt selection (b26).
**Did not work.** Raw probability alone; self-certainty and perplexity versus voting; entropy weighting (small); explicit prior text (c19); belief-tracking prompts in 7-9B models (d18); memory systems versus RAG (d17).

## 6. Language models

**As compressors.** Chinchilla 70B reaches 8.3% of raw size on enwik9 against 32.3% for gzip and 23.0% for LZMA2, and 43.4% on ImageNet patches and 16.4% on LibriSpeech though trained on text (a10). Counting model parameters as part of the code (two-part) removes the advantage on a 1 GB corpus (a10, a11). Across 31 LLMs, compression of external text correlates with mean benchmark score at about -0.95 per domain, -0.93 overall (a17). This is across models; it does not show that within one model a lower code length of an answer means a correct answer.

**As approximate Bayesian learners.** Synthetic ICL follows a Bayesian pattern (a20). In real LLMs the martingale property fails: GPT-4 deviates at short horizon, all but GPT-3.5 deviate in the Gaussian task, and Llama-2-7B and GPT-3.5 shrink epistemic uncertainty more slowly than Bayes (b12, c03, c04). Instruction tuning did not help over GPT-3 base (c03). In bits the cost is small: 0.020/0.011 (Bernoulli) and 0.039/0.022 (categorical) extra bits for Qwen2.5 7B/14B, lower for the larger model (c12). Order sensitivity grows like log n for 7-8B models, with Jensen gain 0.1041 nats/token for Qwen2-7B and 0.00982 for Llama-3.1-8B (d13). No study measures this on frontier reasoning models.

**Priors in post-training.** SFT and DPO mostly shift the fitted task prior, not task knowledge (c06). Larger models shift slowly in SFT. The reading depends on the Bayesian fit being a real mechanism, and non-Bayesian laws fit about as well (d14).

**Updating from evidence.** Off-the-shelf 7-9B models plateau after round 1 of a 5-round preference task (c07). Fine-tuning on the Bayesian Assistant's guesses beat fine-tuning on oracle answers (all p<0.001) and transferred to hotels and web shopping (c08). Verbalised beliefs matched implied beliefs under 50% (c08). Prompting alone is not reliable (d18). Training changed behaviour; a scaffold with an explicit table was not tested.

**Selection by likelihood.** Unnormalised log-probability loses to voting (d01, d02). Joint chain-plus-answer log-probability wins in 37 of 40 comparisons (d03): +3.26 over self-certainty on Llama-3.1-8B GPQA-D, +7.07 on Llama-3.1-70B, +12.33/+12.78 on AIME24/25 for R1-Distill-Qwen-7B at k=6 against SC. Gains shrink for non-thinking Qwen3. Entropy weighting adds +0.5 to +3.4 only in sequential chains (d07). Short chains win within a question for reasoning models: 63.4 vs 47.7 random on LN-Super-49B math (d05), up to +34.5 points shortest vs longest in the best case (K25).

**Scientist agents.** BoxingGym: domain context and explicit probabilistic programs did not reliably help; agents wrote overly simple models; larger and instruction-tuned models beat reasoning-tuned OpenThinker (c19, c20).

**Two-part objectives inside pipelines.** RIMRULE (Llama3.2): ToolHop test-rand 26.5 zero-shot, 29.9 few-shot, 31.1 RIMRULE; unseen 35.1 / 37.9 / 43.1; BFCL 50.1 / 54.5 / 56.6 (d11). MIDGARD (gpt-3.5, T=10): ExplaGraph StCA 30.3 vs 23.7 greedy (d12). Neither compares with a Bayes aggregator or reports token parity.

**Candidate programs.** BMA over 250 LLM-written programs per task gives all weight to one (d10).

**What is missing.** No LLM work uses NML or luckiness (K03, K29). No study of an explicit prior term in selection (K24). No equal-token test of a code-length rule inside a scaffold.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = S9 and the memory store.

### Add now (established)

1. **Do not select by raw summed log-probability alone; if a score is used, it is length-normalised or joint, and code computes it.** Part G5/S7. [E] d01, d02, d03. Consistent with G5 as written.
2. **For reasoning-model attempts, prefer the shorter finished chain among attempts to the same question as a tie-breaker, then vote; drop chains with failed steps before extending.** Part S7 (the SELECT order "symmetry, group size, shortest" already uses shortest) and G11. [E] d05, d08, d16, d06. Boundary: not for non-reasoning models, not across questions.
3. **Cap thinking length per mode.** Part G11. [E] d06 adds a second line (accuracy peaks then falls).
4. **Treat the context as order-sensitive: vary the order of examples and evidence across independent attempts.** Part S3. [E] that order matters (a20 order test, c03, d13, c12). The equal-token accuracy gain of shuffle-averaging is not established, so only the diversity use is "add now"; the averaging rule is under Test first.
5. **A fit to the given examples is not proof; prefer a hold-out (conditional) score to a total score.** Part G3/S4. [E] by G3; extended by one source on marginal likelihood (c13, [S]). Keep G3 as is.
6. **Do not add a stated prior or an LLM-written Bayesian model as a booster.** Part S1/S5. [S] c19, c20, consistent with G7. Treat as "do not add" until tested.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Joint score (chain + answer log-prob) as selector vs majority vote, when log-probs are available | S7 / G5 | [C] | d03, d04, d02, d01 |
| T2 | Same plus an explicit prior term (hypothesis length in tokens) as a fourth arm | S7 | [S] | d11, a13 |
| T3 | Short-m@k early stop and vote for reasoning-mode items | S3/S7/G11 | [E] effect, [S] on our bench | d05, d16 |
| T4 | Order averaging: m shuffles of evidence vs m independent samples | S3 | [S] | c12, d13, c03 |
| T5 | Two-part MDL pruning of the rule store vs LLM summary | S9 memory | [S] (2 sources) | d11, d12 |
| T6 | Scoring a stored note by prequential gain rather than relevance or recency | S9 memory | [S] | a16, a09, d17 |
| T7 | Conditional (hold-out) score vs total score for choosing among candidate programs or rules | S4/S7 | [S] | c13, d10 |
| T8 | Weight candidates by held-out score (stacking) rather than raw marginal likelihood | S7 | [S] | d10 |
| T9 | Explicit posterior table in code, model supplies likelihoods only, small hypothesis set | S5/S7 | [S] | c07, c27, d18 |
| T10 | Tempered evidence weights when combining correlated samples | S7/G4 | [S] | a08, c17 |
| T11 | Mutual-information prompt selection with no labels | O/S1 | [S] | b26 |
| T12 | Prior strength vs number of observations (state a prior or not) | S1 | [S] | c19 |

Not to add: NML, luckiness functions, PAC-Bayes bounds, Kolmogorov-style priors, PFN or meta-training, Bayesian scaling laws as a control rule (K02, K03, K11, K15, K18, K19, K23). They are theory or need training, and none helps selection at equal tokens.

## 8. Concrete tests on our bench

All arms use equal total tokens (generation plus scoring passes). Report per-item pass rate with 95% bootstrap interval, paired by item.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 selection rule (T1, T2) | Word and reasoning items with exact answers; ARC-style with a check | (a) majority vote of k; (b) argmax joint log-prob; (c) vote weighted by joint log-prob; (d) (b) plus prior term = -lambda x chain tokens; same k samples | Accuracy; items flipped | (b), (c) +1 to +3 points over (a) in reasoning mode (PiCSAR); (d) unknown; zero or negative in direct mode |
| B2 shortest chain (T3) | Reasoning-mode items | (a) majority of k; (b) short-m@k with m = k/2; (c) random chain | Accuracy; thinking tokens | (b) matches (a) with 20-40% fewer tokens, so a few points at equal tokens; none for a non-reasoning model |
| B3 order averaging (T4) | Evidence-heavy items (several examples or facts) | (a) one pass; (b) m=3 shuffles then vote; (c) 3 independent samples at fixed order | Accuracy; variance across orders | (b) within 2 points of (c); positive only if order variance is high |
| B4 rule-store pruning (T5) | Repeated problem classes with failure lessons | (a) no pruning; (b) LLM summary; (c) MDL score (length + failures, alpha tuned on a dev split) | Held-out accuracy; store size | (c) +2 to +4 over (b), store 10-20% smaller (RIMRULE 72 to 67, 151 to 121 rules) |
| B5 note value (T6) | Items where a note exists | (a) retrieve by relevance; (b) by recency; (c) by loss drop of the note | Accuracy; notes used | Unknown; keep only if (c) beats (a) by 3 points |
| B6 hold-out score (T7, T8) | Rule-induction items with 4+ examples | (a) pick by fit on all examples; (b) fit on k-1, score on the held-out one; (c) stacking weights | Accuracy on the unseen case; fit-but-wrong rate | (b) cuts the fit-but-wrong rate; (a) reproduces the two-ARC-programs failure |
| B7 posterior table (T9) | Multi-round preference or hypothesis-elimination items | (a) plain multi-turn; (b) table in code, model gives a likelihood per observation | Accuracy at round 5; agreement with exact Bayes | (b) lifts the round-1 plateau; size unknown (Qiu's +40 points came from fine-tuning) |
| B8 prior text (T12) | Estimation items with a known base rate | (a) no prior; (b) base rate stated; (c) base rate plus 3 observations | Error; calibration | BoxingGym predicts no reliable gain; add only if (b) or (c) beats (a) by 3 points |
| B9 tempering (T10) | Items with several sample answers from one model | (a) plain vote; (b) weight w^eta, eta in {0.5, 1} picked on dev | Accuracy | Small; samples are correlated |

## 9. What does not transfer, and why

- **NML and luckiness.** The normaliser needs a sum over all datasets and does not exist for unbounded models. An LLM's output space is unbounded. No LLM study uses it (K03, K29).
- **Kolmogorov complexity and the universal prior.** Incomputable and reference-machine dependent (c18). A bridge only: shorter hypothesis, more prior weight.
- **PAC-Bayes and compression bounds.** Loose in absolute terms (96.41% Top-1 error bound for GPT-2 small); they do not rank answers (a19, c14).
- **Deep-net description lengths (MNIST, CIFAR).** Prequential 4.10 vs 24.1 kbits is image classification trained from scratch (a09). We do not train.
- **Meta-training toward Bayes (PFN, Solomonoff nets, Bayesian teaching).** Needs training (c09, c10, c07). Only the idea of a code-held posterior table survives.
- **Cross-model compression-score correlation.** 31 models (a17). It does not give a within-model selection rule.
- **Inconsistency theorems.** Constructed counterexamples or simulation by one group (a07, a08). They warn against trusting one prior when the hypothesis set is wrong; they are not a measured effect on LLMs.
- **Shortest-chain results.** Reasoning models only and within one question. They do not carry to non-reasoning models (d08) or to comparing different questions.
- **Synthetic Bayesian tests** (Bernoulli coins, GINC, flight choices): small, exactly enumerable hypothesis spaces. Real agent hypothesis sets are open.
- **Human literature.** This subfield's evidence has no human behavioural study, so there are no human effect sizes to transfer.

## 10. Open questions

1. Does a code-length rule with an explicit prior term beat vote at equal tokens? No direct test (gap 1; PiCSAR has no prior term).
2. How big is the order violation for frontier reasoning models, and does shuffle-averaging give an accuracy gain at equal tokens? Only 7-9B models, loss not accuracy (gap 2, d13).
3. Is there any LLM use of NML, luckiness or minimax-regret selection? Search was rate limited; the negative is weak (gap 3).
4. Does the prequential gain of a note predict downstream help better than relevance or recency (gap 8)?
5. Does an explicit posterior table in the scaffold close Qiu's plateau (gap 9)?
6. Do independent fits reproduce "post-training shifts the prior" on real LLMs, and does it predict many-shot jailbreak success (gap 10)? Non-Bayesian laws fit about as well (d14).
7. Do tempered rules help when aggregating correlated samples or tool outputs (gap 5)? Only BMA collapse is shown (d10).
8. Does prior strength interact with the number of observations in LLM reasoning (gap 6)? Only a toy-transformer abstract (d15).
9. Is the conditional marginal likelihood better than the total score for choosing among LLM-written programs (gap 7)?
10. Why does sequential refinement beat parallel voting at matched tokens in d07, against our G11? Small preprint, 30 problems per set.
11. Within one model, does the code length of a candidate answer predict correctness beyond the chain-level joint score? No study isolates it.

## 11. Sources

[V] = opened by the research agents (full text or HTML read); [M] = snippet or cited only.

- [M] Rissanen (1978), Modeling by shortest data description. https://doi.org/10.1016/0005-1098(78)90005-5 (a01)
- [M] Shtarkov (1987), Universal sequential coding of single messages. https://www.mathnet.ru/eng/ppi635 (a02)
- [V] Grunwald and Roos (2019), Minimum Description Length Revisited. https://arxiv.org/abs/1908.08484 (a03-a06, a26, a27, c15, c25)
- [V] Grunwald and Langford (2004/2007), Suboptimal behavior of Bayes and MDL in classification under misspecification. https://arxiv.org/abs/math/0406221 (a07, b04-b06, c16)
- [V] Grunwald and van Ommen (2017), Inconsistency of Bayesian inference for misspecified linear models. https://arxiv.org/abs/1412.3730 (a08, c17)
- [V] Blier and Ollivier (2018), The description length of deep learning models. https://arxiv.org/abs/1802.07044 (a09, c23)
- [V] Deletang et al. (2024), Language modeling is compression. https://arxiv.org/abs/2309.10668 (a10-a12, c22)
- [V] Elmoznino et al. (2025), In-context learning and Occam's razor. https://arxiv.org/abs/2410.14086 (a13-a15, c21)
- [V] Voita and Titov (2020), Information-theoretic probing with MDL. https://arxiv.org/abs/2003.12298 (a16)
- [V] Huang et al. (2024), Compression represents intelligence linearly. https://arxiv.org/abs/2404.09937 (a17)
- [V] Dziugaite and Roy (2017), Nonvacuous generalization bounds via PAC-Bayes. https://arxiv.org/abs/1703.11008 (a18)
- [V] Lotfi et al. (2022), PAC-Bayes compression bounds so tight. https://arxiv.org/abs/2211.13609 (a19)
- [V] Xie, Raghunathan, Liang, Ma (2022), In-context learning as implicit Bayesian inference. https://arxiv.org/abs/2111.02080 (a20, b17, b18)
- [V] Grau-Moya et al. (2024), Learning universal predictors. https://arxiv.org/abs/2401.14953 (a21, b21, c10)
- [V] Rathmanner and Hutter (2011), A philosophical treatise of universal induction. https://arxiv.org/abs/1105.5721 (a22)
- [M] MacKay (2003), Information Theory, Inference and Learning Algorithms. http://www.inference.org.uk/itprnn/book.html (a23)
- [M] Hinton and van Camp (1993), Keeping neural networks simple. https://doi.org/10.1145/168304.168306 (a24)
- [M] Barron, Rissanen, Yu (1998), The MDL principle in modeling and coding. https://doi.org/10.1109/18.720554 (a25)
- [V] Wikipedia (2026), Minimum description length. https://en.wikipedia.org/wiki/Minimum_description_length (b01-b03)
- [V] Vitanyi and Li (2000), MDL induction, Bayesianism and Kolmogorov complexity. https://arxiv.org/abs/cs/9901014 (b07, b08, c18)
- [V] Lotfi et al. (2023), Bayesian model selection, the marginal likelihood, and generalization. https://arxiv.org/abs/2202.11678 (b09-b11, c13)
- [V] Falck, Wang, Holmes (2024), Is in-context learning in LLMs Bayesian? A martingale perspective. https://arxiv.org/abs/2406.00793 (b12-b14, c03, c04, c28)
- [V] Arora, Jurafsky, Potts, Goodman (2025), Bayesian scaling laws for in-context learning. https://arxiv.org/abs/2410.16531 (b15, b16, c05, c06, c26, d14)
- [V] Zhang, Zhang, Yang, Wang (2023), What and how does in-context learning learn? https://arxiv.org/abs/2305.19420 (b19, c11)
- [V] Muller et al. (2022), Transformers can do Bayesian inference. https://arxiv.org/abs/2112.10510 (b20, c09)
- [V] Lotfi et al. (2024), Non-vacuous generalization bounds for large language models. https://arxiv.org/abs/2312.17173 (b22, b23, c14)
- [V] Qiu et al. (2026), Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (b24, b25, c07, c08, c27)
- [V] Sorensen et al. (2022), An information-theoretic approach to prompt engineering. https://arxiv.org/abs/2203.11364 (b26)
- [V] Chlon et al. (2026), LLMs are Bayesian in expectation, not in realization. https://arxiv.org/abs/2507.11768 (c12)
- [V] Gandhi et al. (2025), BoxingGym. https://arxiv.org/abs/2501.01540 (c19, c20)
- [V] Wang et al. (2023), Self-consistency improves chain of thought reasoning. https://arxiv.org/abs/2203.11171 (d01)
- [V] Kang, Zhao, Song (2025), Scalable best-of-N selection via self-certainty. https://arxiv.org/html/2502.18581v3 (d02)
- [V] Leang et al. (2025), PiCSAR. https://arxiv.org/abs/2508.21787 (d03, d04)
- [V] Hassid et al. (2025), Don't overthink it: preferring shorter thinking chains. https://arxiv.org/abs/2505.17813 (d05)
- [V] Does thinking more always help? (2025). https://arxiv.org/abs/2506.04210 (d06; authors not read)
- [V] The sequential edge: inverse-entropy weighted voting (2025). https://arxiv.org/abs/2511.02309 (d07)
- [V] Think deep, think fast: verifier-free inference-time scaling (2025). https://arxiv.org/abs/2504.14047 (d08)
- [V] Model capability dominates: inference-time optimization (2026). https://arxiv.org/abs/2603.27844 (d09)
- [V] Bhide, Gupta, Cunningham, Domke (2026), Stacking-based weighting for LLM-written programs. https://arxiv.org/abs/2611.03966 (d10)
- [V] RIMRULE (2026). https://arxiv.org/abs/2601.00086 (d11)
- [V] Nair and Wang (2024), MIDGARD. https://arxiv.org/abs/2405.05189 (d12)
- [V] Predictable compression failures: order sensitivity (2025). https://arxiv.org/abs/2509.11208 (d13)
- [V] In-context learning strategies emerge rationally (2025), abstract only. https://arxiv.org/abs/2506.17859 (d15)
- [V] What characterizes effective reasoning? Revisiting length (2025). https://arxiv.org/abs/2509.19284 (d16)
- [V] Memory Tax (2026). https://arxiv.org/abs/2610.34073 (d17)
- [V] When should models change their minds? Contextual belief (2026). https://arxiv.org/abs/2605.30219 (d18)
- [M] Gap-search log (2026-11-10), NML in LLM work. https://huggingface.co/api/papers/search (c24, d19; weak negative, no source)

Links to other subfields in this run (not covered here): Calibration and overconfidence; Compression at inference time; Aggregation and extremizing; Belief updating; Language Agent Tree Search; Search over thoughts; Epistemic value and curiosity.
