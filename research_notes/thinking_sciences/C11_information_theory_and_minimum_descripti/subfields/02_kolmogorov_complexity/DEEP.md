# Kolmogorov complexity: deep document

Subfield C11.02. Sources: evidence_a-d.jsonl (ids a01-a29, b01-b27, c01-c26, d01-d16), claims.jsonl (K01-K27), critique.md. Status tags: [E] established, [S] single-source, [C] contested. Evidence marks: [V] opened, [M] snippet only.

## 1. What it is

Kolmogorov complexity K(x) is the length of the shortest program that prints x and halts, on a fixed universal machine (a01). A string of a trillion zeros has a tiny program. An irregular random string has no program much shorter than itself (a05). A counting argument shows most n-bit strings are incompressible, since fewer than 2^n programs are shorter than n bits (a26 [M]).

Three facts shape every use of the idea.

1. **K depends on the language.** The invariance theorem says changing the language changes K(x) by at most an additive constant, the size of a compiler (a01). For short objects this constant can dominate. "Shortest" only means something inside one fixed description language (K01 [E]).
2. **K cannot be computed.** It is upper semicomputable. You can find better and better upper bounds but never know when you have the best one (a02). "You know, but you do not know you know." In practice K is replaced by the length of a real code: a compressor output, a model's log-loss, or a count of operators in a small grammar (K02 [E]).
3. **K applies to one object; entropy applies to a distribution.** The string 110011011111 has entropy 0.811 but a higher K5 (33.36) than the alternating string 010101010101 (K5 26.99) (b11). Token entropy is not a substitute for rule simplicity (K21 [E]).

The link to reasoning is Occam's razor in code form. The best theory minimises the length of the theory plus the length of the data given the theory. This is the two-part code of MDL (Rissanen 1978), the practical form of the ideal K-based idea (a03, K03 [E]). The ideal route is Solomonoff induction: weight every program that could produce the data by 2^-length and predict with the mixture (a06 [M], a22).

For our agent the use is narrow. At S7 SELECT, two candidate rules that both fit the examples can be compared by a concrete length. Nothing here proves a rule is "the shortest". It only says "shorter than the alternatives found".

## 2. History and theories in depth

**Founders (1964-1966).** Solomonoff 1964 (algorithmic probability and induction), Kolmogorov 1965 (program-length definition of information) and Chaitin 1966 (length of programs for finite binary sequences) arrived independently. Chaitin also proved limits on what a formal system can prove about complexity (a06, a07 [M]; dates confirmed in a01 [V]). Levin 1973 added the universal distribution and the coding theorem. The founding texts were not opened. The standard textbook is Li and Vitanyi (a26, b25 [M]).

**Coding theorem.** |-log2 m(s) - K(s)| < c, where m is the universal distribution (d11 [V], via the BDM paper; K27 [E]). Frequent outputs of random programs have low K. This is the basis for estimating K of short strings by counting outputs.

**Solomonoff induction.** Put uniform random bits on the input tape of a monotone universal machine. The output distribution is the universal prior M(x) = sum of 2^-l(p) over programs p whose output starts with x. Prediction is the mixture. Total prediction error is bounded by a constant set by the length of the true source's program (a22, a06 [M]). It is incomputable without a time bound. Sterkenburg 2026 [M, d13] discusses the tension between computability and reference-machine dependence.

**Universal intelligence.** Legg and Hutter 2007 define the intelligence of an agent as expected reward over all computable environments, each weighted by 2^-K(environment). Simple environments count most (a04). It is a definition with no experiments. The survey mentions the C-Test, a computable proxy (a04, c26 [M]).

**MDL.** Rissanen 1978. Practical MDL swaps K for computable probability codes. Ideal MDL and practical MDL differ (a03).

**Similarity by compression.** Normalised information distance (NID) built from K is a universal metric, optimal in a class of computable distances up to additive terms. It is not computable, so NCD uses a compressor: NCD(x,y) = (C(xy) - min(C(x),C(y))) / max(C(x),C(y)) (a08). Cilibrasi and Vitanyi 2005 clustered 24 mammal mtDNA genomes and 36 music pieces with it (a09, a10).

**Short-string K.** Standard compressors are unusable for strings of about 50 symbols or fewer (a15). Soler-Toscano and colleagues built the Coding Theorem Method (CTM): run all small Turing machines and turn output frequency into complexity (a13). The Block Decomposition Method (BDM) sums CTM values of blocks plus log multiplicity, and tends to Shannon entropy when it loses accuracy (b19, d11). Zenil 2020 argues compression is an entropy-rate estimator no closer to K than Shannon entropy. He developed CTM/BDM, so this is not a neutral source (b18).

**Psychology.** Gauvrit et al. 2014 use CTM to score human randomness production (a14). Feldman 2000 found human concept difficulty proportional to Boolean complexity, the length of the shortest equivalent formula (d06). Rival accounts exist: Vigo 2013 GIST (d07), Pape et al. 2015 (b17), and Griffiths and Tenenbaum on subjective randomness as inference (b14 [M]).

**Neural networks and compression.** Goldblum et al. 2024 argue no-free-lunch is misleading because real data are low complexity, and show LMs prefer low-complexity sequences (a16). Deletang et al. 2024 show that prediction plus arithmetic coding is lossless compression (a18). Grau-Moya et al. 2024 train networks on universal-machine data (a21). Elmoznino et al. 2025 show in-context loss equals prequential code length (a17).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Invariance: language choice shifts K by a compiler-size constant | K_LISP(x) <= K_Java(x) + O(1) | a01 | [E] |
| K is only upper semicomputable | No program outputs K(x) for arbitrary x | a02 | [E] |
| Standard compressors fail on short strings | gzip rate 0.966 at 16 bytes, 0.846 (32), 0.736 (64), 0.622 (128), 0.398 (1M) on Audio-8bit; unusable at <= 50 symbols | b07, a15 | [E] |
| CTM correlates with machine size and depth | Km vs instruction count r = 0.83 (partial 0.81); Km vs Bennett logical depth r = 0.41 | a13 | [S] |
| Children's random strings only slightly above random in K5 | N=68, age 8.7; 21.74 (SD .52) vs 21.46; t(67)=4.35 (this t line was not re-found in the critique); grade F(2,65)=0.68, eta2=0.11 | a14, b12 | [S] |
| Subjective randomness tracks natural statistics more than K | Hsu data 100 arrays, 77 raters: complexity r=.52, natural stats r=.75; coefficients .19 vs .66; new N=100: r=.36 vs .56 | b13 | [C] |
| NCD clustering works | 24 species, S(T)=0.996 (fit of tree to distance matrix, not correctness); music 6 errors in 36 pieces | a09, a10 | [E] |
| gzip+kNN result inflated | Reported AG News .937, R8 .954, Yahoo .638; fair tie-breaking cuts accuracy up to 9 points; bag-of-words +1.4 (K=2), +1.1 (K=1), wins 6 of 7 sets | a11, a12 | [E] |
| LMs as compressors beat codecs (raw) | Chinchilla 70B: ImageNet 43.4% (PNG 58.5%), LibriSpeech 16.4% (FLAC 30.3%), enwik9 8.3% (Llama 2 7B 8.9%, gzip 32.3%, LZMA2 23.0%) | a18, c01 | [E] |
| Same, parameter-adjusted | Chinchilla 70B enwik9 21.9%; ImageNet about 185%, LibriSpeech about 229%, random about 225% | b02 | [E] (table garbled in extraction; critique confirms 21.9%) |
| Compression predicts benchmark score | 31 LLMs, 12 benchmarks; Pearson -0.93 overall, about -0.95 per domain; RMSE 3.1% | a20, b03 | [E] |
| Code: relation is log, not linear | Pearson -0.956, RMSE 5.7% (open) and 9% (closed) | b04 | [E] |
| LMs fail to write short programs | 128-byte sequences; GPT-4o accuracy audio16 35.6, audio8 15.0, MFCC 29.6, DNA 24.8, text 6.5, synthetic 33.3; Llama-405B 18.0/10.1/24.2/22.5/9.6/18.0; Llama-8B 5.9/3.9/8.8/3.7/1.4/8.5 | b05 | [S] |
| Failure rates on natural data | GPT-4o 40%, Llama-405B 78% (synthetic quoted 66/45 in intro, 65/55 in Sec 5.1) | a23, c04 | [S] |
| Prompted programs longer than gzip | Precision above 1.5 in every cell | b05 | [S] |
| Length hurts accuracy | Llama-405B at lengths 16/32/64/128: 47.1/29.9/20.9/14.2% | b07 | [S] |
| Correct programs mostly copy | Repetition > 95% of correct natural-data programs, about 20% synthetic (25 per modality) | a25, b07 | [S] |
| Trained SeqCoder: in-distribution only | Synthetic 84.5-92.5%, precision 0.57/0.56; natural <= 0.1%; > 99% of errors in first 16 chars (10K training); 93.5% (100K), 88.7% (1M) | a24, b06, c07 | [S] |
| CoT on program finding | -1.3 (Llama 8B), -5.1 (70B), +2.1 (405B); execution feedback 6.5 to 8.7% on MFCC | c06, b06 | [S] |
| LMs do not track a Solomonoff bound | 26 checkpoints, 0.8-35B, 177,591 programs; none within 3.32 bits of KT mixture; at 24 symbols best 4.5, median 36.5, worst 128 bits behind | c19 | [C] |
| Wan and Mei Solomonoff claim has a weak test | Only test is low- vs high-confidence few-shot selection: SMS Qwen 3B 90.07 vs 76.62, Qwen 7B 94.60 vs 92.73, Llama 3.2 3B 73.22 vs 64.94, Llama 3.1 8B 85.56 vs 85.22 | d01 | [S] |
| LMs prefer low-complexity sequences | Exponentially higher probability; stronger after pre-training; GPT-3 Ada to Davinci, strongest Davinci | a16, b10 | [S] |
| Prequential ICL generalises better at low data | Advantage vanishes at long context; GPT-4 on novel Mastermind much worse than meta-trained small models | a17, b08, c10 | [S] |
| UTM-trained nets approach optimal predictors | Regret rises with generating program length; match CTW on variable-order Markov | a21, c08, c09 | [S] |
| MDL search solves part of ARC | CompressARC 76K params: 20% of 400 eval, 34.75% train (2 guesses), pass@1 30.25%, pass@1000 52.75%, about 20 min/puzzle; steps: 500 = 23%, 1000 = 28%, 2000 = 30.25% | b20, c16, c17 | [E] |
| MADIL | 7% ArcPrize 2024 private; 69 of 400 eval tasks fit train, 57 correct on test (82%), 53 first attempt; 80% of solutions in first 20 s | b21, c18 | [E] |
| LMs miss the simplest hypothesis | Accuracy > 80% at height 1 to < 50% at height 2 (except GPT-4o); height 4 strong accuracy very low; SFT Qwen3-4B +11.0/+8.5/+4.0/+1.5 | b22, d02 | [S] |
| Shorter reasoning chains are more often correct | Shortest/random/longest: LN-Super-49B 63.4/47.7/28.9; R1-32B 60.0/55.5/37.8; QwQ-32B 71.1/68.9/56.7; R1-670B 83.3/78.2/58.9; shortest uses 31-48% fewer tokens | d03 | [S] |
| short-m@k | short-1@k up to 40% fewer thinking tokens than majority at similar or better accuracy; short-3@k beats majority at measured budgets; QwQ-32B small decline for short-1@k at large k | d04 | [S] |
| In-context accuracy falls with rule length | Operator count 1-5, 18 concepts/class; r = -0.961 (Gemma-2-9B, p=.009), -0.898, -0.884, -0.854 (Qwen2-72B, p=.065); Qwen2-72B 90% to 74% | d05 | [S] |
| Hypothesis-then-program on ARC | GPT-4, 100 problems: direct 17%, program 23%, summarised 30%, human-selected 33%; 1D-ARC 39.6 vs 61.1 | d08 | [S] |
| Held-out error as selector | 100% test accuracy from 200 examples on 10-parity, CAP, IsPrime; SGD near 50% even with 100k | d09 | [S] |
| Human concept difficulty vs Boolean complexity | 41 concept types; difficulty proportional to complexity; rivals claim better fit | d06, d07 | [C] |

## 4. Mechanisms and models

**4.1 Code length as a two-part score.** Score(rule) = L(rule) + L(exceptions | rule). L(rule) is the token count of the rule written in one fixed small DSL. L(exceptions) is the cost to list the example cells the rule gets wrong. A rule with zero exceptions reduces to rule length. Implementation: code parses the DSL, counts operators or tokens, runs the rule on every example and counts mismatches (K03, a03).

**4.2 Fixed description language.** Pick one small grammar (operators, primitives) and force every candidate rule into it. Count operators, as in d05 (classes 1-5). If free natural language is allowed, rank may change with phrasing. No study measured how much (d15, gap 6). Run the same candidates through two phrasings and check rank correlation (K01 test).

**4.3 Model log-loss as length (prequential code).** Feed examples to the model in order. The sum of negative log-probabilities of each next item is a code length and upper-bounds K(D) (a17). It needs token log-probs. Count the model itself or the comparison is unfair (Deletang two-part adjustment, b02).

**4.4 Compressor proxies.** gzip/NCD give a model-free distance for long texts only. Do not use them on short rules (K04). A trivial baseline is required, since bag-of-words beat gzip (a12). Use for clustering long traces, not for ranking short rules.

**4.5 CTM/BDM for short strings.** A CTM table lookup gives K estimates for short strings (and for blocks of that size). BDM(X) = sum of CTM(block) + log(multiplicity). Example: two repeated blocks of 26.99 bits each give 57.566 bits (d11). It depends on the reference machine (5-state, 2-symbol, 500-step cap) (a13). Useful only for binary-like data in tests.

**4.6 Selection by shortest chain (short-m@k).** Launch k samples. Stop when the first m finish. Take the majority among those m. Cost is counted in total thinking tokens (d04). This is length as a correctness signal, not rule simplicity.

**4.7 Filter, then rank.** Sample many programs, execute on all given examples, keep those that pass. Then rank survivors. Baseline: majority vote on outputs of survivors (Greenblatt style, d10 [M]). Candidate rankers: held-out error (d09), then length (untested). Hypothesis Search adds an LLM summary of 64 hypotheses to 8 (d08).

**4.8 MDL as the search objective (CompressARC).** A tiny network is trained at test time for each puzzle to minimise the description length of the puzzle. No pretraining. More steps help: 500 steps 23.00%, 2000 steps 30.25% on training (c17). Cost: about 20 min per puzzle on one GPU (c16). MADIL does MDL-scored pattern-based models with MCTS search. Correct model sizes were 3 to 46, mean 15.2 (c18).

**4.9 Parsimony quality metric.** Sun and Saparov define q(H) as the ratio of how often a hypothesis appears in valid proofs to how often it appears in the shortest proof (d02). This is a proof-length proxy for parsimony. Human agreement with the metric was 79%, against 33.3% chance and 51% for a length heuristic (b22).

## 5. What holds up

**Holds up.**
- The theory: invariance, incomputability, MDL link, coding theorem (K01, K02, K03, K27 [E]). Founding papers were read only through secondary text.
- Short strings break standard compressors (K04 [E]). Three sources.
- NCD clustering of genomes and music works across compressors (K08 [E]). The S(T)=0.996 value says the tree fits the distance matrix, not that the phylogeny is true.
- LMs as arithmetic coders compress many modalities better than specialised codecs, raw (K10 [E]).
- Compression tracks benchmark score across models (K11 [E]). Three sources, but correlational across models and it cannot rank scaffolds.
- MDL search solves part of ARC without pretraining (K19 [E]). Two systems (CompressARC, MADIL).

**Failed or weakened.**
- gzip+kNN (Jiang 2023) partly failed to replicate. Tie-breaking inflated it by up to 9 points, DengueFilipino train and test are identical, and bag-of-words beats gzip on 6 of 7 sets (a12). The idea is not dead, but not special.
- Linear compression-intelligence: for code the relation is log (Pearson -0.956). A preliminary run showed no clear correlation until a fresh validation set and Format Annealing were used (b04). Per-language differences exist (SQL worse than Python).
- Raw rates look strong, adjusted rates do not: with model size counted, Chinchilla 70B is 185-229% on non-text (b02).
- LLM-as-Solomonoff-approximator (Wan and Mei) is unsupported. Its only test is few-shot selection with no random baseline, gain 0.1-0.4 at 7-8B and large only at 3B (d01). Zenil 2026 finds none of 26 checkpoints within the bound (c19). Contested; only c19 has verified bound numbers.
- Humans: simplicity preference is not cleanly algorithmic. Subjective randomness r=.52 with complexity but r=.75 with natural statistics (b13). Feldman 2000 is challenged by Vigo 2013, Pape 2015 and Lafond 2007 (title only) (K24 [C]). Kurtz et al. 2013 (cited in b17): instructions to look for rules produced the rule-based advantage, neutral instructions did not.
- The children's randomness effect is tiny and unreplicated (K06 [S]).

**Moderators.**
- Sequence length: Llama-405B accuracy falls from 47.1 to 14.2% from length 16 to 128 (b07).
- Modality: text hardest for GPT-4o (6.5%), audio easiest (35.6%) (b05).
- Data size: prequential ICL helps only at low data; at long context the gap vanishes (c10).
- Model size: Llama 8B to 405B about tripled program accuracy (b27).
- Source program length: regret rises with generating program length (c08).
- Compressor choice and sample size (gzip vs PPMZ; short strings).
- Shortest-chain benefit excludes unfinished chains (d03).

**Interventions that worked.**
- Scale (b27). Hypothesis-then-program prompting on ARC (17 to 23 to 30%; compute unequal, d08). SFT on parsimony data (+1.5 to +11.0, b22). Meta-training for prequential code (low data, c10). Short-chain selection (d03, d04). Held-out validation selection (d09). More test-time steps for CompressARC (c17).
- Training on synthetic program data worked only in distribution (b06).

**Interventions that did not help.**
- Chain of thought on program finding: -1.3, -5.1, +2.1 (c06). CoT, buffer-of-thought and 8 demos did not close the weak/strong gap in ontology induction; buffer-of-thought beat CoT but accuracy stayed below 50% from height 2 (d02). Regularised SGD did not match prequential ICL at low data (b08). Execution feedback gave small gains (b06). A uniform prior over the DSL gave modest gains (a25).

**Not done.** No study tests "pick the shortest rule" as a scaffold step at equal tokens (critique). No equal-token MDL vs majority-vote comparison on LLM-sampled ARC programs (d14). No description-language invariance study (d15).

## 6. Language models

**As compressors.** A language model plus arithmetic coding is a lossless compressor, so log-loss is a code length (c01). On enwik9, raw: Chinchilla 70B 8.3%, Llama 2 7B 8.9%, LZMA2 23.0%, gzip 32.3% (c01). Domain-tuned Llama3-8B improved the ratio by 8.5% (MeDAL) and 38.4% (Pile of Law) (c11). Larger models help only up to a critical size on a fixed dataset, then the adjusted rate worsens (a19). Transformers trained from scratch on enwik8 overfit text (a18). In-context compression rate improves with sequence length, which is evidence of in-context learning (a19). Offline adjusted rates of gzip and LZMA2 on a 38M Transformer are 92.2% and 89.1% (c02).

**As predictors of ability.** Bits per character on fresh text predicts the average of 12 benchmarks across 31 LLMs: -0.93 overall (a20). The relation is weaker out of domain, and holds for base models trained to convergence (b03). For code it is logarithmic (b04).

**As program writers.** Weak. GPT-4o: 6.5% (text) to 35.6% (16-bit audio). Llama-3.1-8B: 1.4 to 8.8%. Correct programs are mostly copies (> 95%), and prompted programs are always longer than gzip output (precision > 1.5) (b05, b07). Models compress well by probability code but not by program (c25). Do not merge these two results.

**Trained program models.** SeqCoder gets 84.5-92.5% on the authors' DSL and about zero on natural data. Over 99% of failures occur in the first 16 characters (b06, c07).

**Simplicity bias.** Pretrained GPT-2 and GPT-3 give exponentially higher probability to low-complexity sequences, stronger after pretraining (a16, b10). Complexity was measured with a restricted expression-tree language, not true K. If the bias is already in the model, a "be simplest" instruction may add little (K15 test).

**Rule length and accuracy.** In-context accuracy falls as rule length rises: Gemma-2-9B r=-0.961, Qwen2-72B 90% to 74% over classes 1 to 5 (d05). These are class means (n=5), so the correlation is weak evidence.

**Occam failure.** On synthetic first-order-logic induction, models reach correct but not simplest hypotheses. Accuracy falls from above 80% to below 50% from height 1 to 2, except GPT-4o. SFT on Qwen3-4B added +1.5 to +11.0 strong accuracy (d02). No plain parsimony-prompt arm and no replication.

**Solomonoff behaviour.** Trained on universal-machine data, small Transformers and LSTMs approach optimal predictors (a21). Pretrained LLMs do not stay within the KT bound (c19). Wan and Mei's positive claim has no verified numbers beyond few-shot selection (d01).

**In-context Occam.** The prequential view says in-context learners trade fit against complexity (a17). GPT-4 on novel Mastermind did far worse than small meta-trained learners and a naive baseline (b08, 5 seeds). Large pretrained models can fail to minimise prequential code length on new tasks.

**ARC.** LLM systems score far above MDL systems: o3 high 87.5% on the semi-private evaluation against CompressARC 20% (c16). Greenblatt reached about 50% on a subset with GPT-4o by sampling about 8,000 programs per problem, filtering, then voting (d10 [M], from a search summary). Length was not the criterion.

**Length as a signal.** Within a question, the shortest chain beats the longest by up to 34.5 points (d03). This is reasoning-model math and GPQA only, correlational, with unfinished chains excluded.

**Newer illustrations.** Pass 2026 defines prompt value under an LLM-relative Levin complexity, illustrated on 12 GSM8K problems with 64 rollouts each (c21). Shportko 2026 uses perplexity as a proxy for K in steganography detection (paired t=5.11, 300 samples) (c22). Both are small and not turned into claims. Xu et al. 2025 gives a theory of conditional K and scaling; no numbers were read (b24).

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Never call a rule "shortest"; only "shorter than the alternatives found". Shorter length is a tie-breaker, never proof. | G10, S7 | [E] | a02, a27, K02 |
| Compare rule lengths only inside one fixed description language (small DSL). Do not compare lengths across phrasings. | S2, S7 | [E] | a01, b26, K01 |
| Do not use gzip or token entropy to compare short rule texts. Use exception count or operator count. | S7 | [E] | a15, b07, b11, K04, K21 |
| Any compression-based claim about the agent needs a trivial baseline and a count of the scaffold's own tokens. | G7 | [E] | a12, b02, K09, K10 |
| Use a two-part score (rule length plus exceptions) when a rule is not exact, as a tie-breaker after the held-out check (G3 comes first). | S4, S7 | [E] for the principle; implementation [S] | a03, K03 |
| Code, not the model, computes length and ranks. | G5 | [E] (guardrail already in schema) | a03, d09 |
| Compression ratio across models is not a scaffold metric. Do not use it to compare arms. | G7 | [E] | a20, c25, K11 |

Nothing in this list needs a new schema element. These are notes attached to S7 and G10.

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Explicit "state the shortest consistent rule, then check on all examples" step vs plain CoT at equal tokens | S7 | [S] | d08, d02, K20, K25 |
| Rank candidate rules by held-out error first, then length; test whether length adds anything | S7 | [S] | d09, d03, K26 |
| Among k sampled solutions that pass all examples, prefer the shortest (short-m@k analogue) vs majority vote at equal tokens | S7, G4, G11 | [S] | d03, d04, K22 |
| Cheap length proxy comparison: operator count, token count, exceptions, model log-loss | S7 | [S] | d02, d03, d05, d09, K23 |
| MDL ranking of LLM-sampled ARC programs vs filter-then-vote | S7 | [E] for MDL search itself; the comparison is untested | b20, b21, d10, K19 |
| Parsimony prompt closes the Occam failure | S3, S7 | [S] | b22, d02, K20 |
| Execute-and-check loop vs CoT for rule finding | S4 | [S] | c06, K14 |
| Rank stability across natural language / Python / DSL | S2, S7 | no study | d15, K01 |
| Rule length as a difficulty signal for the S0 gate | S0, G12 | [S] | d05, K23 |

Held-out validation error (d09) is the baseline any length rule must beat. Keep it ahead of length in the order.

## 8. Concrete tests on our bench

Both arms use the same total tokens, setup cost included (G7). Use the bench harness. Report paired differences with a bootstrap interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC subset (100 items) and List Functions rule-induction items | A: plain CoT. B: one "shortest consistent rule, verify on all examples" step in a fixed DSL, same total tokens | Exact-match accuracy, paired | 0 to +3 points; Yoran's CoT results suggest a null is likely (c06) |
| T2 | Same items, k=8 sampled programs | A: filter by examples, then majority vote on outputs. B: filter, then shortest program. C: filter, then lowest held-out error. D: C with B as tie-break | Accuracy at equal total tokens | C >= A; D >= C by 0-2 points if length adds anything |
| T3 | Rule-induction items with a known simplest rule | A: standard prompt. B: parsimony prompt in plain words | Rate of choosing the simplest consistent hypothesis (q(H) style) and accuracy | +5 to +15 points on strong accuracy if the failure is prompt-fixable; null if it needs SFT |
| T4 | Same candidate rules written in natural language, Python, DSL | Rank by length in each language | Spearman rank correlation of rankings; top-1 flips | rho > 0.8 for Python vs DSL; lower for natural language |
| T5 | 500 rule-induction items, generated rule length 1-5 operators | One arm; record accuracy per class | Correlation of rule length and accuracy; use as S0 gate | r about -0.85 to -0.96 on class means (d05) |
| T6 | Reasoning-trace length | Within item, k=4 samples run to completion | Accuracy of shortest vs random vs longest, same tokens | Shortest above random by 3-15 points on math (d03); smaller on rule induction |
| T7 | Rule-finding items | A: CoT. B: execute-and-check loop (run rule, see mismatches, revise once) | Accuracy at equal tokens | +2 to +8 points; G2 is already in the schema |
| T8 | Length proxy ranking | Tokens, operator count, exceptions, model log-loss | Spearman with held-out correctness per item | Held-out error beats any length proxy; log-loss best of the length proxies |
| T9 | ARC items, MDL-ranked vs vote | A: filter-then-vote. B: filter, rank by DSL length | Pass@2 at equal tokens | 0 to +3 points |

Pre-register the DSL and the stop rule before T1-T3. The expected effects are guesses from the nearest studies, not measured results.

## 9. What does not transfer, and why

- **Raw compression ratio.** It ignores the cost of the model. Adjusted for parameters, Chinchilla 70B is 185-229% on non-text (b02). A scaffold has no analogue of this table.
- **Compression predicts intelligence (Huang).** It holds across models, not across prompts or scaffolds (a20, b03). Weaker out of domain; for code it is log (b04).
- **SeqCoder and other learned program compressors.** In-distribution only; zero on natural data (b06). The agent is not trained.
- **NCD/gzip classifiers.** Inflated by tie-breaking and beaten by bag-of-words (a12).
- **CTM/BDM.** Binary strings, 5-state machines, 500-step cap. Not usable for rule text (a13, d11).
- **CompressARC.** Per-puzzle network training for 20 minutes on a GPU. Not a prompt scaffold (c16).
- **Prequential meta-training and UTM pre-training.** Training methods; the advantage vanishes at large data (c10, a21).
- **Solomonoff induction and Legg-Hutter intelligence.** Incomputable and reference-machine dependent; no experiments (a04, a22, d13 [M]).
- **Human simplicity findings.** Feldman 2000 is contested, the children's strings are a single sample, and natural statistics explain more variance (b13). A human preference for short rules does not show shorter rules are right.
- **Shortest-chain selection.** Reasoning-trace length is not rule length. It was shown on reasoning models with unfinished chains excluded (d03). It may not apply to rule induction.
- **Steganography and prompt-value papers.** Tiny illustrations (c21, c22).

## 10. Open questions

1. Does an explicit shortest-rule step beat plain CoT at equal tokens on rule induction? Nearest: Hypothesis Search, with unequal compute (d08).
2. Which cheap length proxy best ranks rules against held-out correctness? Each works only in its own setting (d16).
3. Does MDL ranking of sampled programs beat majority vote on ARC at equal tokens? No paper found (d10, d14).
4. Does a plain parsimony prompt close the Occam failure, and does it replicate beyond Sun and Saparov (d02)?
5. How much does rule rank change between natural language, Python and a DSL (d15)?
6. Do pretrained LLMs satisfy any Solomonoff-like prediction (c19 vs b23, d01)? Wan and Mei's figures were not extracted.
7. Does the length of a reasoning trace predict correctness on rule-induction items rather than math (d03 limits)?
8. Exact Feldman 2000 effect sizes, Lafond 2007 content, and failed replications (d06, d07; full text unread).
9. Founding sources (Solomonoff 1964, Kolmogorov 1965, Chaitin 1966, Levin 1973) and any 2020-2026 critique of the coding-theorem method (d11-d13).
10. Does short-chain preference survive control for item difficulty (easy items yield short chains)? Not addressed in d03.

## 11. Sources

[V] opened, [M] snippet only.

- [V] Gruenwald and Vitanyi (2008) Algorithmic Information Theory. https://arxiv.org/abs/0809.2754 (a01-a03, a27, a29)
- [V] Legg and Hutter (2007) Universal Intelligence. https://arxiv.org/abs/0712.3329 (a04, a05; c26 header only)
- [M] Solomonoff (1964) A formal theory of inductive inference. https://doi.org/10.1016/S0019-9958(64)90223-2 (a06)
- [M] Kolmogorov (1965); Chaitin (1966). https://en.wikipedia.org/wiki/Kolmogorov_complexity (a07)
- [V] Li, Chen, Li, Ma, Vitanyi (2004) The similarity metric. https://arxiv.org/abs/cs/0111054 (a08)
- [V] Cilibrasi and Vitanyi (2005) Clustering by Compression. https://arxiv.org/abs/cs/0312044 (a09, a10, c24)
- [V] Jiang et al. (2023) Low-resource text classification with compressors. https://aclanthology.org/2023.findings-acl.426.pdf (a11, c12)
- [V] Opitz (2023) Gzip versus bag-of-words. https://arxiv.org/abs/2307.15002 (a12, c13)
- [V] Soler-Toscano et al. (2013) Correspondence and independence. https://arxiv.org/abs/1211.4891 (a13)
- [V] Gauvrit et al. (2014) Algorithmic complexity for short binary strings applied to psychology. https://arxiv.org/abs/1106.3059 (a14, a15, a28, b11, b12, b26, c23)
- [V] Goldblum et al. (2024) No Free Lunch, Kolmogorov Complexity. https://arxiv.org/abs/2304.05366 (a16, b10, c14, c15)
- [V] Elmoznino et al. (2025) In-Context Learning and Occam's Razor. https://arxiv.org/abs/2410.14086 (a17, b08, c10)
- [V] Deletang et al. (2024) Language Modeling Is Compression. https://arxiv.org/abs/2309.10668 (a18, a19, b01, b02, c01, c02)
- [V] Huang et al. (2024) Compression Represents Intelligence Linearly. https://arxiv.org/abs/2404.09937 (a20, b03, c03)
- [V] Grau-Moya et al. (2024) Learning Universal Predictors. https://arxiv.org/abs/2401.14953 (a21, a22, b09, c08, c09)
- [V] Yoran et al. (2025) The Kolmogorov Test. https://arxiv.org/abs/2503.13992 (a23-a25, b05-b07, b27, c04-c07)
- [M] Li and Vitanyi (1997/2008) An Introduction to Kolmogorov Complexity. https://doi.org/10.1007/978-0-387-49820-1 ; https://www.springer.com/gp/book/9780387339986 (a26, b25)
- [V] Xuyang et al. (2025) Is Compression Really Linear with Code Intelligence? https://arxiv.org/abs/2505.11441 (b04)
- [V] Gauvrit, Soler-Toscano, Zenil (2015) Natural scene statistics. https://arxiv.org/abs/1509.03970 (b13)
- [M] Griffiths and Tenenbaum (2003) From algorithmic to subjective randomness. https://proceedings.neurips.cc/paper/2003/hash/b06b5541a62ed438f956b662b4e1ec28-Abstract.html (b14)
- [M] Feldman (2000) Nature. https://ideas.repec.org/a/nat/nature/v407y2000i6804d10.1038_35036586.html (b15). Abstract opened via PubMed in d06: [V] https://pubmed.ncbi.nlm.nih.gov/11034211/
- [M] Lafond, Lacouture, Mineau (2007). https://web-archive.southampton.ac.uk/cogprints.org/7132/index.html (b16)
- [V] Pape, Kurtz, Sayama (2015) Complexity Measures and Concept Learning. https://arxiv.org/abs/1406.7424 (b17)
- [V] Zenil (2020) Review of methods for estimating algorithmic complexity. https://arxiv.org/abs/2003.11044 (b18)
- [V] Zenil et al. (2018) Decomposition method (BDM). https://arxiv.org/abs/1609.00110 (b19, d11)
- [V] Liao and Gu (2025) ARC-AGI Without Pretraining. https://arxiv.org/abs/2512.06104 (b20, c16, c17)
- [V] Ferre (2025) MADIL. https://arxiv.org/abs/2505.01081 (b21, c18)
- [V] Sun and Saparov (2025) Do Language Models Follow Occam's Razor? https://arxiv.org/abs/2509.03345 (b22, d02)
- [V] Wan and Mei (2025) LLMs as Computable Approximations to Solomonoff Induction. https://arxiv.org/abs/2505.15784 (b23, d01)
- [V] Xu et al. (2025) Unifying Two Types of Scaling Laws from Conditional Kolmogorov Complexity. https://arxiv.org/abs/2501.06802 (b24)
- [V] Li et al. (2025) Understanding is Compression. https://arxiv.org/abs/2407.07723 (c11)
- [V] Zenil et al. (2026) LLMs are Shannon Lossy Compressors, Not Solomonoff Induction Estimators. https://arxiv.org/abs/2601.05280 (c19, c20; d12 snippet [M])
- [V] Pass (2026) The Value of a Prompt. https://arxiv.org/abs/2608.16438 (c21)
- [V] Shportko (2026) Kolmogorov Complexity Bounds for LLM Steganography. https://arxiv.org/abs/2603.21567 (c22)
- [V] Hassid et al. (2025/2026) Don't Overthink it. https://arxiv.org/abs/2505.17813 (d03, d04)
- [V] Wang, McCoy, Steinert-Threlkeld (2024) Minimization of Boolean Complexity in In-Context Concept Learning. https://arxiv.org/abs/2412.02823 (d05)
- [V] Vigo (2013) The GIST of concepts (abstract). https://pubmed.ncbi.nlm.nih.gov/23891825/ (d07)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660 (d08)
- [V] Singhal et al. (2026) LLM Priors for ERM over Programs. https://arxiv.org/abs/2510.14331 (d09)
- [M] Greenblatt (2024) Getting 50% on ARC-AGI with GPT-4o. https://blog.redwoodresearch.org/p/getting-50-sota-on-arc-agi-with-gpt (d10)
- [M] Sterkenburg (2026) Solomonoff induction. https://arxiv.org/abs/2603.20274 (d13)
- [M] Negative search results d14, d15, d16 (syntheses over the sources above).
