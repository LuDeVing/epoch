# Minimum message length: deep document

*Subfield C11.04. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K27), critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Priority for the agent: background only, with a few cheap hooks. Important limit up front: the founding paper (Wallace and Boulton 1968) was never opened in full (only its abstract, d15), and no LLM paper found uses MML by name. Everything about LLMs here is about MDL, prequential or Kolmogorov codes, which are cousins of MML, not MML itself.*

## 1. What it is

Minimum message length (MML) is a way to pick the best hypothesis for some data. You imagine sending the data to a receiver. The message has two parts.

- Part 1 states the hypothesis H (the model and its parameters).
- Part 2 states the data D, given H.

The best hypothesis is the one with the shortest total message. Length is counted in bits. An event of probability p costs -log2 p bits. So total length = -log2 Pr(H) - log2 Pr(D|H). Minimising it is the same as maximising Pr(H) x Pr(D|H), the posterior (a04, a28). Three views of one object (a04):

1. The best two-part compression of the data.
2. The most probable hypothesis after seeing the data.
3. The best trade-off between structure (part 1) and noise (part 2).

Three features separate MML from plain "fit the data":

- **Parameters cost bits.** A parameter must be stated to a finite precision. Too coarse and the data part grows. Too fine and part 1 grows. The optimum is a stated interval of width s with s^2 = 12 / Fisher information (b03). A precise value that the data cannot support is over-fitting, in bit terms (b04).
- **It needs a prior.** MML is fully Bayesian (a22, b02). MDL, its relative, tries to avoid priors by using universal codes (c02).
- **It outputs one theory.** MML does inference (one best hypothesis). Solomonoff-style methods do prediction (a mixture of many) (a24).

Counting bits needs no judge. That is the one reason it might matter for an agent: it is a score computed by code, not an opinion. Priority for our agent stays low. The useful part is the idea "charge for the claim and for what the claim leaves unexplained", not the formulas.

## 2. History and theories in depth

**1968, Wallace and Boulton, Computer Journal 11(2):185-194 (a01, d15).** First paper on MML. It introduced the Snob program for unsupervised classification (clustering) on a Sydney KDF 9 computer. The best classification gives the shortest two-part message: classes first, then each item given its class. The abstract says early tests agreed well with conventional taxonomy. The full text is paywalled; no data, class counts or bit thresholds were read here. Only the abstract page (d15) was opened. Facts on this paper are second-hand [M].

**Origin of the idea (a02).** David Boulton, an engineer, saw a theory as a concise way to represent data. Chris Wallace was a Bayesian. They found the two views were the same. Boulton's example was the periodic table: about 70 known elements, 92 later, arranged so that row and column show similarities. Knowing the table saves describing each element. This history is retold from Wallace's 2003 talk by his close colleague Dowe, so it is partisan.

**1969 onwards, early use.** Depression classification by numerical taxonomy (Pilowsky, Levine, Boulton 1969, a19, M) and later autistic-spectrum subgroups. Snob work in 1994 listed depression, cancer-family clusters, word classes and several thousand protein angle sets (a18).

**1975, Strict MML (Wallace and Boulton).** Defined an exact but heavy version. It builds a code-book over the data space: data is partitioned into groups, each with one estimate, so the expected two-part length is smallest (a05). Wallace said referees rejected the work; one found it "repugnant" (a03). Exposure in the statistics literature was delayed.

**1987, Wallace and Freeman, JRSS B 49(3).** A practical approximation. Length = -log prior + negative log-likelihood + 0.5 log Fisher information + (d/2)(1 + log kappa_d) (a07). This is "MML87". With the Fisher term crudely replaced by k log N it collapses to BIC and Rissanen's 1978 MDL. Dowe argues the Fisher term should not be dropped (a07).

**Rissanen's MDL (1978).** MML came about 10 years and about 6 journal papers earlier (a21), a priority claim from the MML camp. Neutral view: MDL grew from a different motive. MML always uses two-part codes and picks model family and parameters together. Refined MDL codes minimise worst-case regret; MML two-part codes minimise expected length under a subjective prior (c02). In practice the two often give similar answers (c02, c04). No head-to-head performance numbers exist in the neutral reviews (K08).

**1990s, theory work.** Snob models each class with Normal, multi-state, Poisson and von Mises attributes (a16, a32). Wallace and Dowe 1994 showed that giving each item wholly to one class makes estimates inconsistent. Partial (probabilistic) assignment gives shorter messages: cost is -log P(x) with P(x) summed over classes (a17). With total assignment, two Normal classes less than about 2.5 true SDs apart are not recovered (a17). Dowe and Wallace (1996, 1997) proved ML inconsistent on Neyman-Scott (a08). Wallace and Dowe 1999 tied MML to Kolmogorov complexity: part 1 makes a universal Turing machine act as if the data came from H; part 2 makes it write the data; the choice of machine is a prior (a33, M).

**2000s, applications and philosophy.** Decision trees (Needham and Dowe 2001), Bayesian networks (Comley and Dowe 2003, 2005) (b07). Dowe, Gardner and Oppy 2007 (Brit J Phil Sci) argued Bayesians have no simplicity problem, and answered Forster and Sober (a06, a15). Dowe 2010 (Handbook of Philosophy of Science chapter) is the main reference read here (a04-a08, a21, a23-a25). Wallace's book *Statistical and Inductive Inference by MML* appeared in 2005; Wallace died in 2004 (a31). Allison's 2018 book and web notes explain implementations (b02-b05, b22).

**2020-2026, applied revival.** MML87 for ARMA and ARMA-LSTM (c19), Granger causality (a29, c21), species distribution (c20), chemistry functional groups (c22, 2026), a Strict-MML information-geometry paper (c23, 2026), a tutorial (d03, 2022), and logic-program learning (d01, 2025-26). The last two are among the few not from Monash-linked authors (d01 is Cambridge, Delft and Helsinki).

**Competing views.**

- Dowe (a23): conjecture that only MML and very close Bayesian methods are in general both consistent and invariant under re-parametrisation; any non-Bayesian method with both properties would be far less efficient. Dowe says he has seen no counter-example. Unproven; Wallace doubted it.
- Grunwald (c02-c04): MDL is less assumption-bound; with large n refined MDL and Bayes factors choose the same model in nested cases.
- Compression-only view (a25): Dowe says plain one-part compression can give wrong models (Neyman-Scott, gap problem), and intelligence also includes memory and deduction, which compression does not cover.

## 3. Core findings with exact numbers

Status uses claims.jsonl. "Dev" means reported by MML's own developers.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MML score = two-part code length = maximise Pr(H) Pr(D given H) | Each extra bit halves probability. Optimal stated interval s^2 = 12 / Fisher | a04, a28, b03 | [E] K01, K03 |
| Wallace and Boulton introduced MML for clustering (Snob) | 1968; abstract only read | a01, d15 | [E] K02 (history), founding data unverified |
| Strict MML on binomial, N=100, uniform prior | 10 groups; 33 to 49 successes all give 0.41; P(41 at 0.41)=0.0809, P(33)=0.0218, P(49)=0.0216 | a06 | [E] worked example |
| Strict MML binomial n=10 | Partition {0},{1..4},{5..9},{10}; estimates 0.00, 0.25, 0.70, 1.00; naive partition costs about 9.84 bits, worse | d03 | [E] |
| Strict MML is NP-hard in general | Exact polynomial algorithms only for binomial (Farr and Wallace) and 1-D exponential families (Dowty); k-nomial k>2 exponential time | b05, d03 | [C] K20 |
| ML is inconsistent on Neyman-Scott; MML is not | ML sigma^2 tends to (J-1)/J x truth; J=2 gives half. MML code uses N/(N-1)-type factor | a08, b22, b06 | [E] K04 |
| Lancaster panel problem: MML gives correct df N(T-1) | One worked example; no simulation | a09 | [E] K04 |
| Polynomial order selection, N=10, noise SD 0.61, 1000 cases | ESPE: MML 0.1857 (SD 0.2633); AIC 15.8055 (SD 63.8077). 95th percentile 0.6075 vs 306.5. MML chose degree 0 or 1 255 times; AIC never | a10 | [S] K05, dev |
| AR order, cyclone, von Mises estimation | MML best in all AR cases; AIC overfits cyclone data; ML worst or equal-worst on every von Mises error measure, gaps largest at small samples. No tables reproduced | a11-a13 | [S] K05, dev |
| Gap/no-gap test | MML accepts a gap near (2 log N)/N; AIC wrongly prefers a gap of size (log N)/N | a14 | [S] dev, invented test |
| Granger on Hawkes cascades, p=7, T=200, F1 | MMLH 0.948 (SD 0.089), BIC 0.943, AIC 0.850, ADM4 0.773, MLE-ms 0.572, MDLH 0.566, thresh ML 0.410, random 0.130 | a29, critique | [E] K06 (small margin) |
| Same, p=20, T=200 | MMLH 0.933, BIC 0.927, AIC 0.719, ADM4 0.694, MDLH 0.398 | a29 | [E] K06 |
| MML boundary: dense graphs and long series | Mid-dense: MDLH best. T>=1000: MMLH about 0.9, MDLH about 0.95, AIC about 0.92. Priors were very flat so MML acts like BIC | a30, a29 | [S] K07 |
| MML87 ARMA orders | 10 parameter sets, 100 runs, N=50 to 500. ARIMA at T=3: RMSE AIC 2.987, BIC 3.027, HQ 2.914, MML87 3.075 (MML87 worst). Hybrid ARMA-LSTM best overall | c19 | [E] K06 |
| Cross-family selection in species models | MML fully correct on 10 of 11 artificial tests; each rival failed some; all methods failed one | c20 | [E] K06 |
| MML vs MDL on logic programs (independent) | MML ahead in 12/12 size-proportion cells (p<0.05 in 11) at train size 20 and 50; size 1: +6.8 +/- 2.4%; positive-only +9.2%; negative-only +25.9%; balanced or noisy data: no significant difference | d01, d02 | [S] K21 |
| Why MDL fails on positive-only data | The all-true program has zero errors and is short; MML charges log(all atoms / seen atoms) for it | d02 | [S] mechanism, no ablation |
| Two-part and variational codes weak for neural nets | 1M float32 params = 32 Mbits, about 200x the CIFAR10 uniform code. MNIST variational 24.1 kbits (ratio 0.12, 95.5% acc) vs prequential 4.10 kbits (0.021, 99.5%). CIFAR10 variational 89.0 kbits (0.54, 61.6%) vs prequential 45.3 kbits (0.27, 93.3%) | b09, b10, c10 | [E] K09 |
| Best variational code picks a worse model | Same figures: shortest code is not the most accurate model | b10, c10 | [S] K10 |
| LLM + arithmetic coding compress other modalities | Chinchilla 70B: ImageNet patches 43.4% vs PNG 58.5%; LibriSpeech 16.4% vs FLAC 30.3%; enwik9 8.3% vs gzip 32.3%, LZMA2 23.0%, Llama 2 7B 8.9% | b11, c05 | [E] K11 |
| LLaMA-7B on text | text8 0.7101 bpc vs ZPAQ 1.4, paq8h 1.2; 100KB Gutenberg 0.8426 bpc. Likely optimistic (training overlap) | c14 | [E] K11 |
| Charging model size (two-part) removes big-model edge | Chinchilla 70B adjusted: enwik9 21.9%, ImageNet 185.3%, LibriSpeech 228.9%. Transformers 200K/800K/3.2M raw enwik9 30.9/21.7/17.0%. Prequential would charge less | b11, b12, c06 | [E] K12 |
| Pre-trained small transformers beat gzip even with size counted | Best OOD audio ratio 0.49 vs FLAC 0.54; weak transfer to unseen modalities | c18 | [S] |
| Bits per character predicts benchmark score | 31 LLMs, 12 benchmarks; Pearson -0.93 (knowledge, RMSE 3.1%), about -0.95 per domain; saturates near 3M characters | b18, c08, c09 | [S] K13 |
| MDL probing separates real structure from memorised control | ELMo, POS: layer 0 control acc 96.3 vs 93.7 linguistic, codelength about 2x; accuracy wrong in 8 of 10 settings, MDL 0 of 10 | b16, c11 | [S] K14 |
| ICL loss = prequential code length | Prequential ICL generalises better than train-risk ICL at all dimensionalities; gap largest in low-data regimes. GPT-4 on Mastermind: code length above naive label-frequency baseline (from figure, qualitative) | b14, b15 | [S] K16 |
| Shortest-code example selection (MDL rank) | GPT2-XL, 8 datasets, mean acc: TopK+MDL 60.16; TopK 58.14; TopK+LocalE 51.36; Majority 50.43; GlobalE 49.75; Random 42.78 | c12, c13 | [S] K15 |
| CompressARC (code-length objective, no pretraining) | ARC-AGI-1 pass@2: train 34.75, eval 20 (peak 21.5 at 1500 iterations); pass@1 18.5 eval; about 20 min per puzzle | c25, d04 | [E] K17, K24 (blog) |
| MADIL (MDL program learner, no LLM) | About 7% at ArcPrize 2024; table 32.1% train, 6.0% private | d05 | [E] K24 |
| Kolmogorov Test: shortest program generation | Llama-3.1-405B and GPT-4o wrong 78% and 40% on natural length-128 sequences; GPT-4o accuracy audio 35.6, DNA 24.8, text 6.5; prompted programs longer than gzip | c15, c16 | [E] K17 |
| LLM-compressed text not learnable by another LLM | Equal-Info Windows make it learnable; SentencePiece still best at equal size | c17 | [S] K18 |
| MIDGARD (MDL merge of sampled reasoning graphs) | gpt-3.5 component F1 68.5 to 70.4, R100 23.7 to 25.7, R50 34.7 to 37.2. Code-Llama F1 54.1 to 55.6, R100 11.5 to 16.5. Equal add/delete cost variant 57.9, below greedy | d06 | [C] K22, K23 |
| RIMRULE (MDL-consolidated rules) | Rule count cut 7% (ToolHop), 20% (BFCL). Accuracy ToolHop 27.5 to 31.1; BFCL 52.1 to 56.6. Low-resource BFCL test-rand 55.2 to 62.1, test-unseen 46.0 to 60.0 | d07 | [C] K22 |
| ReuseRL: raw length penalty backfires | Pure length penalty -10.94 vs vanilla GRPO on TextWorld-Cooking; segmentation cost +17.70 over pure length (+0.71/+1.49 ALFWorld IID/OOD, +3.35 Countdown) | d08 | [C] K23 |
| Excess description length (prequential) | EDL near 0 for random labels; one example can remove up to log m bits; threshold about 1+ bit per parameter separates teaching from elicitation | d09 | [S] |
| No independent MML vs AIC/BIC replication found; no LLM paper uses MML | 0 MML hits in Elmoznino, Voita, Grau-Moya, Pan, Huang 2026; 0 of 13 arXiv MDL+LLM listings name MML | b25, b26, d10, d11, d13, d14, d17 | [E] K19 (negative result, search incomplete) |

## 4. Mechanisms and models

Each is written so an engineer could code it.

### 4.1 Two-part score (the core)

```
score(H) = L(H) + L(D | H)        # bits; lower is better
L(H)     = -log2 prior(H) + cost of stating parameters to useful precision
L(D | H) = -log2 P(D | H)
choose   = argmin score(H)
```

Accept a more complex hypothesis only if total length falls. Snob-style significance: a gap of more than 5 to 6 bits (Wallace and Freeman 1987) or 10 bits (Wallace and Boulton 1968, per a18) was called significant. No false-positive rate is given, so these are rules of thumb, not tests (a18).

### 4.2 Wallace-Freeman (MML87) for a model with d parameters

```
L = -log h(theta) + (-log f(x | theta)) + 0.5 * log det F(theta) + (d/2) * (1 + log kappa_d)
```

- h is the prior, F is the Fisher information matrix, kappa_d is the lattice constant (1/12 for d=1, 5/(36 sqrt 3) for d=2) (a07, b03).
- Assumes the prior is flat across the stated interval and F is close to constant over it. These simplifications can fail (b03).
- Normal example: MML sigma uses N/(N-1) scaling, like the unbiased estimate, not divide-by-N ML (b22).
- Replace 0.5 log det F by (d/2) log N and you get a BIC-like score (a07). Setting very flat priors also makes MML act like BIC (a29 limits).

### 4.3 Strict MML (reference, rarely implemented)

Partition the data space into groups j with prior mass q_j. Pick one estimate per group. Minimise sum_j (-q_j log q_j) + sum_j q_j x (expected cost of data given the group estimate) (a05). Exact algorithms exist only for 1-D cases (d03). Use Wallace-Freeman in practice.

### 4.4 Snob-style mixture clustering (a16, a17)

1. Hypothesis part states: number of classes, relative abundance of each class (label cost = -log2 abundance), class parameters to precision about their estimation error, and the class of each item.
2. Use partial assignment: item cost is -log of the sum over classes of p(j, x), not -log of the max.
3. Larger classes get more precise parameters than small classes.
4. The program only computes the length; no message is built.
5. Search: try adding, splitting, merging classes and keep a move if total length falls.

### 4.5 MML logic-rule learning (d01, d02)

The MML cost for a program charges for the program size plus the data given the program. The key term is the cost of positive examples under the program: an over-general program (e.g. "everything is true") pays log(all possible atoms / seen atoms) per example. A program covering only seen examples pays log(1) = 0. This makes MML prefer tight rules when only positives are given and when n is tiny. Both parts together: MDL with a plain error count picks the all-true rule at 100% positives, and MML does not.

### 4.6 Prequential code (the practical alternative, used in the LLM papers)

```
L_preq(D) = sum_t  -log2 P(x_t | x_1..x_{t-1}, model trained on x_1..x_{t-1})
```

No parameter description is needed. It charges the learning procedure, not the weights (c06, b09). In-context learning loss is exactly this sum (b14). EDL (d09) subtracts the bits under the final model to isolate how much was learned. Prequential code depends on data order, which is a flaw for reasoning traces.

### 4.7 MDL rank for choosing among candidates (Wu et al., c12)

For each candidate in-context example (or answer), compute the code length of the model's predicted label distribution; choose the shortest, i.e. most confident. This equals entropy minimisation (c13), the opposite of an earlier max-entropy method. Weakness: it uses model confidence as the code, so a confidently wrong choice wins. In schema terms this is a model-confidence selector and falls under G4/G5 cautions.

### 4.8 MDL merge of sampled structures (MIDGARD, d06)

Sample several reasoning graphs. Choose the merged graph minimising (cost of adding edges missing from a sample) + (cost of deleting edges present in samples), with unequal add and delete costs. Equal costs gave 57.9 F1, below greedy 68.5. So the asymmetry is the active ingredient.

### 4.9 MDL rule consolidation (RIMRULE, d07)

The model proposes rules from failure traces. Code scores each rule set by (rule text length) + (errors the rules fail to fix on a training set). Prune and merge until the score stops falling. Inject the small library in the prompt.

### 4.10 Per-puzzle code-length training (CompressARC, c25, d04)

Train a small network at test time for one puzzle to minimise reconstruction cross-entropy plus a KL cost on a latent (the KL weight on reconstruction is 10x). No weight regulariser. Sample outputs during training and pick the most frequent grid. 2000 iterations, about 20 min per puzzle on an RTX 4070.

## 5. What holds up

**Holds up (mathematics and logic).**
- The identity "minimise length = maximise posterior" is exact, not an empirical claim (a04, a28).
- Over-precise parameters are over-fitting. Ten-point 9th-degree polynomial is "almost certainly ridiculous" (b04). The Strict MML binomial example shows wide groups matching estimation error (a06, d03).
- ML inconsistency on Neyman-Scott is proved (a08). Textbook, not in dispute.

**Holds up with caveats (empirical).**
- MML beats AIC at small-sample order selection in several settings. Almost every table is from MML's developers or close collaborators (a10-a14, c19-c21, a29). The polynomial table (N=10, 1000 cases, ESPE 0.1857 vs 15.8) is from a draft chapter (Wallace 1997 results quoted in a 2007 draft); no independent lab repeated it (K05, K27, critique). Search for replication was cut short by rate limits, so this is a gap in our search, not proof of absence.
- Margins over BIC are tiny (0.005 F1, within one SD, a29). When priors are very flat MML is close to BIC.

**Moderators and boundary conditions.**
- Sample size: gaps are largest at small N and shrink with low noise and big samples (a10 limits, a13). At T>=1000, MMLH falls below AIC and MDLH (a30).
- Graph density: in mid-dense graphs MDLH wins (a30).
- Very short horizon: MML87 was the worst ARIMA method at T=3 (c19).
- Data balance: MML beats MDL on tiny and lopsided data, ties on balanced and noisy data. The authors suspect the MML prior is too optimistic on noisy data (d01).
- Model class: float32 two-part codes (MML style) lose to the uniform code for neural nets. Variational codes are weak. Prequential wins (b09, b10).
- Modality: LLM compressors do not beat domain tools once model size is charged on small data (b11, b12).

**Failed or null results.**
- Variational (MML-lineage) code selection chose models with worse accuracy: 95.5 vs 99.5 (MNIST), 61.6 vs about 93 (CIFAR10) (b10).
- GPT-4 failed to cut prequential code length on a novel task, worse than a naive baseline (b15).
- Pure brevity as a reward: -10.94 vs vanilla on TextWorld-Cooking (d08). Equal add and delete cost in MIDGARD was below greedy (d06).
- Frontier LLMs are poor at shortest-program generation (c15). Trained models do not transfer synthetic gains to natural data (c15).
- Pure compression solvers on ARC: 20% eval (CompressARC) and about 6 to 7% (MADIL), far below LLM methods (d04, d05). CompressARC cannot do counting, rotation, reflection or long-range tasks, and has posterior collapse in some runs (c25).
- Contested theory: Dowe's conjectures on invariance and consistency are unproven (a23). MML-vs-MDL framing differs by camp with no numbers (K08).

**Interventions that worked and did not (for agents).**
- Worked: structural compression that keeps explicit parts (rule consolidation, merged graphs with asymmetric costs, dictionary cost), all small gains, older or small models (d06, d07, d08).
- Did not: raw length pressure (d08), compressing memory so hard another model cannot learn it (c17).
- Worked at tiny scale: shortest-code in-context example choice on GPT2-XL (c12). Not tested on frontier models.

**Measurement warnings.**
- Wallace and Boulton 1968, Wallace and Freeman 1987, Baxter and Oliver 1995 never opened (critique). 
- Wikipedia sources (a22, a27, a28, a31, b06, b07, c01) are secondary.
- Numbers re-checked in the critique pass against PDFs: Deletang, Huang, Blier and Ollivier, Voita and Titov, Wu et al., Hlavackova-Schindler. Not re-checked: ESPE numbers (a10), CompressARC blog (re-opened in d04 and confirmed), Lester, Yoran.

## 6. Language models

No paper read applies MML to an LLM. What exists is nearby.

**Compression and prediction are one object.**
- LLM plus arithmetic coding: Chinchilla 70B reaches 43.4% on ImageNet patches and 16.4% on LibriSpeech, beating PNG (58.5%) and FLAC (30.3%) (b11, c05). gzip can even be run as a generative model (c07).
- LLaMA-7B reaches 0.71 bpc on text8, likely optimistic (c14).
- Counting model size as a two-part code reverses the picture for big models on small data: adjusted rates 185.3% (ImageNet) and 228.9% (LibriSpeech) for Chinchilla 70B (b11). Prequential coding would charge less (c06). This is MML's own lesson restated: parameter cost matters.

**Better compression, better ability.** Across 31 base LLMs, bits per character on fresh text correlates -0.93 to -0.95 with average benchmark score (b18, c08). Saturation near 3M characters (c09). It is a cross-model correlation, base models only. It does not say a given model's solutions get better when it compresses more.

**In-context learning as prequential coding (b14).** The ICL loss is a prequential code length, so ICL is pushed toward simple explanations. But GPT-4 did worse than a naive baseline on novel Mastermind (b15). The in-context Occam pressure is not guaranteed on a frontier model.

**MDL probing (b16).** Description length tells real linguistic structure from memorised noise where accuracy fails (8 of 10 settings wrong for accuracy, 0 for MDL). ELMo era.

**Selecting among candidates by code length.**
- Wu et al.: TopK+MDL 60.16 vs random 42.78 and TopK 58.14 on GPT2-XL (c12). Majority vote 50.43 and GlobalE 49.75 were lower. Uses model confidence as code length (c13). Not tested on a frontier model.
- MIDGARD: +1.9 component F1 on gpt-3.5 (68.5 to 70.4), +5.0 R100 on Code-Llama (11.5 to 16.5). Baseline is greedy, not majority vote at equal tokens (d06).

**Memory and rule libraries.** RIMRULE: +3.6 ToolHop, +4.5 BFCL over prompt-based consolidation; low-resource BFCL test-unseen 46.0 to 60.0 (d07). Rules from Llama3.2 and GPT-4o transfer to other models. Only tool-use tasks.

**Test-time search and shortest programs.** CompressARC: 20% eval pass@2 with no pretraining (d04). Kolmogorov Test: frontier models write programs longer than gzip and are wrong 40% (GPT-4o) to 78% (Llama-405B) on natural sequences (c15). So an LLM asked directly for "the shortest rule" is unreliable; code-side length counting is safer.

**Training-time pressure.** ReuseRL: raw length penalty -10.94, dictionary cost +17.70 over it (d08). Structure-Residual pretraining: 1.44% NLL gain at GPT-2 Medium 300M tokens, persisting to 20B (d11). Pan et al. frame LLM training as two-part coding (d10). These are training-side, not scaffold.

**Compressed text.** Text compressed by one LLM is not learnable by another without Equal-Info Windows (c17).

**Excess description length.** EDL (d09) separates teaching from elicitation in fine-tuning. No reasoning-trace use yet.

**Summary of "what changed it, by how much".** Shortest-code choice: +17.4 points mean accuracy over random on GPT2-XL, +2.0 over TopK (c12). Structural MDL merge: +1.9 F1 (d06). Rule consolidation: +3.6 and +4.5 (d07). Pure length: -10.94 (d08). All small or older models. No frontier-model measurement exists.

## 7. What our agent should take

Marks: G guardrail, S state, O operator, memory. Evidence ids from the evidence files.

### Add now (established)

Almost nothing here is both established and agent-specific. MML is background (SUBFIELDS priority Low). Two cautions can be recorded now, and both agree with existing schema rules.

1. **Never rank by shortness alone.** Pure brevity backfired by -10.94 (d08), equal-cost merging fell below greedy (d06), and the shortest code picked worse models (b10). Any length-based tie-break must sit beside fit and recurrence. Part: G5/S7 note. Status [E]-leaning: three papers (K23 is marked contested because they are different settings), so treat as a caution, not a rule change. Evidence d06, d08, b10, c10.
2. **A shortest-description score is a code-computed score.** It needs no model judge. This is consistent with G5 (code selects). Part: G5. Status [E] for the principle that code-computed scores avoid judge noise (SCHEMA already holds it); no new MML-specific evidence needed. Evidence a04, a28.

Nothing else from this subfield meets the two-independent-source bar for a schema change.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Rank sampled candidate answers by model-assigned code length (MDL rank) versus majority vote and plain self-rating, at equal tokens | S7 | [S] small model only | c12, c13, d14 |
| T2 | Shortest-rule tie-break among ARC candidates after frequency and symmetry, versus frequency only | S7 | [S]; solver-level evidence [E] that pure compression is weak | c25, d04, d05, K24 |
| T3 | Prequential scoring of a reasoning trace (how well earlier steps predict later steps) versus a two-part "explanation length plus residual" score as a correctness predictor | S4/S7 | [S] untested | b09, b14, d09, d18 |
| T4 | Charge over-general rules for what they fail to rule out when learning from 1 to 20 cases | S2/S7 | [S] logic programs only | d01, d02 |
| T5 | MDL-style consolidation of the lesson/rule memory: score = rule text length + errors on held-out problems | memory (S9) | [C] small models, tool use | d07, d08, c17 |
| T6 | Penalise over-precise claims (a stated number or exact detail the evidence does not support) in verbal confidence | G (calibration) | [S] idea from K03; no LLM study | a07, b04 |
| T7 | Report solution length alongside accuracy when comparing agent configurations | logging (section 6) | [S] | b16, c11 |
| T8 | Add-versus-delete asymmetric cost when merging sampled reasoning structures | S7 | [C] | d06 |
| T9 | Snob-style stop rule: accept a more complex hypothesis only if total length falls by more than a threshold of bits | S5/S6 | [S]; thresholds of 5 to 10 bits are human-statistics rules of thumb | a18, K26 |

## 8. Concrete tests on our bench

All arms use equal total tokens (setup cost counted, G7). Report per-item flips right-to-wrong and wrong-to-right.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Short-answer items with exact answers (math, ARC-like grids), N sampled candidates each | A majority vote; B shortest model-assigned code length (mean token log-prob of answer given prompt, answer-only); C B with majority vote as tie-break; D self-rating | accuracy, and how often the pick equals the best available candidate | B alone near or below A (confidence rewards confident errors, c13); C slightly above A (0 to 2 points) at best |
| T2 | ARC items with 2+ surviving rules after S4 | A frequency vote; B frequency then shortest rule (token count of the rule program) as tie-break | pass@2 on held-out outputs | Small gain only when ties are common; no change otherwise. Pure shortest rule worse than frequency |
| T3 | Reasoning traces with known correct/incorrect final answers | A two-part score (trace length + residual errors); B prequential score (sum of -log p of later steps given earlier steps); C trace length alone | AUC for predicting final correctness; calibration | B above A above C is the hypothesis; likely near chance for all; a null is useful |
| T4 | Rule induction from 1, 5, 20 examples (synthetic functions), positive-only and mixed | A fit-only; B fit plus penalty on rule generality (count of inputs it would accept beyond seen ones, sampled by code) | held-out accuracy by n | +5 points at n=1 to 5 on one-sided data, zero at balanced data (d01) |
| T5 | Sequence of problem classes with lessons | A prompt-based lesson list; B pruned list by (length + errors on a held-out set); C no lessons | accuracy on later problems of the same class; lesson count | B above A by 2 to 4 points with fewer rules (d07); no gain if lessons already help little |
| T6 | Items needing numeric estimates or exact details | A plain; B code flags claims with precision beyond a source-supported level and asks to round or hedge | Brier or ECE; accuracy | Small calibration gain; accuracy flat; risk: models hedge everything |
| T7 | Existing bench runs | Add tokens-per-correct-solution and answer length to summaries | rank changes among arms | Diagnostic only |
| T8 | Argument or structure-extraction items | A greedy single graph; B merged graph with add cost lower than delete cost; C equal costs | component F1 | B > A by about 2 points; C below A (d06) |
| T9 | Clustering or grouping of candidate answers (S7) | A fixed threshold; B accept a split only if description length drops by more than X bits | group purity | Marginal; mostly for engineering convenience |

## 9. What does not transfer, and why

- **The theory-of-statistics results.** Neyman-Scott, Lancaster, polynomial order selection with N=10: the agent does not estimate parameters of a fixed distribution. No transfer (K04, K05).
- **Strict MML.** NP-hard except 1-D cases (d03). No use at agent scale.
- **Fisher information precision.** An LLM has no tractable Fisher matrix over its claims. Only the principle (stated precision should match evidence) survives, as a heuristic, untested (T6).
- **Model-size charging.** Our agent is a fixed frozen model. The two-part cost of its weights is a constant and cancels. Adjusted compression rates (b11) do not matter for choosing among its outputs.
- **Compression-benchmark correlation (b18).** It compares models; we use one model. Not decision-relevant (K13).
- **Training-time length rewards (d08, d11).** We do not train.
- **MML-beats-AIC tables.** Developer-reported, tiny samples, statistical models. Not evidence about a thinking scaffold.
- **Code length from the model's own confidence (c12).** Conflicts with G4 and G5: samples from one model are not independent and models favour their own text. Confidence can pick a confidently wrong answer. This needs a code-computed, not model-judged, measure.
- **Direct "shortest program" prompts.** Frontier models are poor at it (c15), and CompressARC needs 20 minutes per puzzle on a GPU (c25), far over a token budget.
- **Wallace and Boulton 1968 thresholds.** Never seen; 10 bits (a18) is second-hand (K26).

## 10. Open questions

1. Does ranking sampled final answers by model code length beat majority vote or self-rating on a frontier LLM at equal tokens? No study found (K25, d14).
2. Does prequential scoring of reasoning steps track correctness better than a two-part score? Tools exist (d09), no test on traces (d18).
3. Is there any independent (non-Monash) MML versus AIC/BIC replication, and at what N does the gap vanish? Search incomplete (K27, d17).
4. Does a shortest-rule tie-break help on ARC beyond frequency voting? Not tested (K24).
5. What does the 1968 paper report (data, class counts, bit thresholds)? Paywalled (K26).
6. Does LLM-stated claim precision correlate with calibration? Zero hits (d18).
7. Where do MML and MDL differ in practice outside logic programs, with numbers? One study (d01).
8. How far can the agent compress its own memory before later steps cannot reuse it? RIMRULE and ReuseRL partly answer (d07, d08, c17).
9. Do 2020-2026 LLM papers use MML under another name (Wallace-Freeman, MML87, MMLD, two-part code)? Mostly closed: none found, listing recall imperfect (d10, d11, d13).
10. Are Dowe's invariance and consistency conjectures true? Unproven (a23).
11. Is the MML advantage on small and one-sided data (d01) due to the prior term, or to some other difference? No ablation (d02).

## 11. Sources

[V] = opened and read this session or in the research pass. [M] = snippet, listing or reference entry only.

- [M] Wallace and Boulton (1968) An information measure for classification. http://www3.oup.co.uk/computer_journal/hdb/Volume_11/Issue_02/110185.sgm.abs.html (a01); abstract page only [V for abstract]: https://academic.oup.com/comjnl/article/11/2/185/406485 (d15)
- [V] Dowe (2008) Foreword re C. S. Wallace, Computer Journal 51(5). http://www.csse.monash.edu.au/~dld/Publications/2008/DLDowe_ForewordReCSWallace_CompJVol51Num5Sept2008pp523-560.pdf (a02, a03, a20, a26)
- [V] Dowe (2010) MML, hybrid Bayesian network graphical models, consistency, invariance and uniqueness, Handbook of Philosophy of Science. http://www.csse.monash.edu.au/~dld/Publications/2010/Dowe2010_MML_HandbookPhilSci (a04, a05, a07, a08, a09, a21, a23, a24, a25)
- [V] Dowe, Gardner and Oppy (2007) Bayes not bust! (draft). http://www.csse.monash.edu.au/~dld/Publications/2007/DoweGardnerOppy_draftBayesNotBust (a06, a10-a15)
- [V] Wallace and Dowe (1994) Intrinsic classification by MML, the Snob program. http://www.csse.monash.edu.au/~dld/Publications/1994/Wallace+Dowe1994_IntrinsicClassificationByMML (a16, a17, a18)
- [M] Pilowsky, Levine and Boulton (1969) Classification of depression by numerical taxonomy (a19; reference entry in the Foreword URL above)
- [V] Monash Snob page. http://www.csse.monash.edu.au/~dld/Snob.html (a32)
- [M] Wallace and Dowe (1999) MML and Kolmogorov complexity, Computer Journal 42(4). http://comjnl.oxfordjournals.org/cgi/reprint/42/4/270 (a33)
- [M] Leads not opened: Learning logical rules using MML (2025); Entropic strict MML. Semantic Scholar listing (a34)
- [V] Wikipedia: Minimum description length. https://en.wikipedia.org/wiki/Minimum_description_length (a22)
- [V] Wikipedia: Minimum message length. https://en.wikipedia.org/wiki/Minimum_message_length (a27, b01, b06, b07, c01)
- [V] Wikipedia: Inductive probability. https://en.wikipedia.org/wiki/Inductive_probability (a28)
- [V] Wikipedia: Chris Wallace (computer scientist). https://en.wikipedia.org/wiki/Chris_Wallace_(computer_scientist) (a31)
- [V] Allison MML pages: https://www.allisons.org/ll/MML/ ; /Notes/Fisher/ ; /Notes/Inference/ ; /SMML/ ; /Continuous/Normal/ ; /KL/ (b02-b05, b22-b24, b27)
- [V] Hlavackova-Schindler, Melnykova and Tubikanec (2024) Granger causal inference in multivariate Hawkes processes by MML. https://arxiv.org/pdf/2309.02027 (a29, a30)
- [V] Grunwald and Roos (2019) MDL revisited. https://arxiv.org/abs/1908.08484 (b08)
- [V] Gruenwald (2004) Tutorial introduction to MDL. https://arxiv.org/abs/math/0406077 (c02, c03, c04)
- [V] Blier and Ollivier (2018) The description length of deep learning models. https://arxiv.org/abs/1802.07044 (b09, b10, c10)
- [V] Deletang et al. (2024) Language modeling is compression. https://arxiv.org/abs/2309.10668 (b11-b13, c05-c07)
- [V] Elmoznino et al. (2025) In-context learning and Occam's razor. https://arxiv.org/abs/2410.14086 (b14, b15, b26)
- [V] Voita and Titov (2020) Information-theoretic probing with MDL. https://arxiv.org/abs/2003.12298 (b16, b17, c11)
- [V] Huang et al. (2024) Compression represents intelligence linearly. https://arxiv.org/abs/2404.09937 (b18, b19, c08, c09)
- [V] Bornschein, Li and Hutter (2022) Sequential learning of neural networks for prequential MDL. https://arxiv.org/abs/2210.07931 (b20)
- [V] Grau-Moya et al. (2024) Learning universal predictors. https://arxiv.org/abs/2401.14953 (b21)
- [V] Wu et al. (2023) Self-adaptive in-context learning: an information compression perspective. https://arxiv.org/abs/2212.10375 (c12, c13)
- [V] Valmeekam et al. (2023) LLMZip. https://arxiv.org/abs/2306.04050 (c14)
- [V] Yoran et al. (2025) The Kolmogorov Test. https://arxiv.org/abs/2503.13992 (c15, c16)
- [V] Lester et al. (2024) Training LLMs over neurally compressed text. https://arxiv.org/abs/2404.03626 (c17)
- [V] Heurtel-Depeiges et al. (2025) Compression via pre-trained transformers. https://arxiv.org/abs/2410.05078 (c18)
- [V] Zheng, Dowe, Peiris and Rosadi (2021) MML in hybrid ARMA and LSTM forecasting. https://doi.org/10.3390/e23121601 (c19)
- [V] Fang et al. (2025) Model selection from multiple families in species distribution modelling using MML. https://doi.org/10.3390/e27010006 (c20)
- [V] Heterogeneous graphical Granger causality by MML (2020). https://doi.org/10.3390/e22121400 (c21)
- [V] Sharma and King (2026) Compressing chemistry reveals functional groups. https://doi.org/10.1021/acs.jcim.5c02917 (c22)
- [V] Makalic and Schmidt (2026) Information geometry and asymptotic theory for SMML. https://doi.org/10.3390/e28060713 (c23)
- [V] From More Is Different to Algorithmic Emergence (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13702946/ (c24)
- [V] Liao and Gu (2025) ARC-AGI without pretraining (blog). https://iliao2345.github.io/blog_posts/arc_agi_without_pretraining/arc_agi_without_pretraining.html (c25, d04)
- [V] Crossref listing for "minimum message length" since 2020. https://api.crossref.org/works?query=minimum+message+length (c26, c27; titles only)
- [V] Sharma, Dumancic, King, Cropper (2025/26) Learning logical rules using MML. https://arxiv.org/abs/2508.06230 (d01, d02)
- [V] Makalic and Schmidt (2022) Introduction to MML inference. https://arxiv.org/abs/2209.14571 (d03)
- [V] MADIL (2025). https://arxiv.org/abs/2505.01081 (d05)
- [V] Nair, Wang et al. (2024) MIDGARD. https://arxiv.org/abs/2405.05189 (d06)
- [V] Gao, Das et al. (2026) RIMRULE. https://arxiv.org/abs/2601.00086 (d07)
- [V] Xu et al. (2026) ReuseRL. https://arxiv.org/abs/2605.31509 (d08)
- [V] Donoway, Joren, Roger, Leike (2026) Excess description length. https://arxiv.org/abs/2601.04728 (d09)
- [V] Pan, Wang, Liao, Li (2025) Understanding LLM behaviours via compression. https://arxiv.org/abs/2504.09597 (d10)
- [V] Huang, Zuk et al. (2026) Structure-residual inductive biases for LM pretraining. https://arxiv.org/abs/2611.23197 (d11)
- [V] Spangher et al. (2026) Articulation upper bounds for language models. https://arxiv.org/abs/2610.19721 (d12; near-name hit, not MML)
- [V] arXiv listing searches (d13, d14, d17, d18): https://arxiv.org/search/?query=%22minimum+message+length%22+language+model&searchtype=all ; https://arxiv.org/search/?query=minimum+description+length+large+language+model&searchtype=all ; https://arxiv.org/search/?query=prequential+coding+language+model&searchtype=all
- [V] Bartlett, Desmond, Ferreira (2023) Priors for symbolic regression. https://arxiv.org/abs/2304.06333 (d16; partial read)

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 11 established claims: 10 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C11.04-K19** (reworded: the sources support less). Zero 'message length' hits in Pan et al. and Huang et al. and the 3-result arXiv search are verified, but 'the only 2025-26 AI paper using MML is a logic-program learner (d01)' has no listed evidence (d01 is not among the claim's sources; the arXiv search shows only 2012/2013/1997 papers) and is contradicted by Wen and Dowe (Entropy 2025, MML species-distribution model selection) which other claims here cite; the Allison page cited supports nothing about replication, and Elmoznino/Voita/Grau-Moya greps were not re-run. Corrected claim: No independent large replication or failed replication of MML itself was located in a limited search (arXiv, Crossref and web search were partly rate-limited); none of the LLM papers checked names MML (0 hits for 'message length' in Pan et al. 2025 and Huang et al. 2026, and an arXiv title search for 'minimum message length' language model returns only three non-LLM papers from 1997-2013). MML-in-LLM work is unestablished, while recent MML applications (e.g. Granger causality, ARMA-LSTM, species distribution models) exist outside LLMs.
- **C11.04-K09** (now single-source: only one opened source, code check).
