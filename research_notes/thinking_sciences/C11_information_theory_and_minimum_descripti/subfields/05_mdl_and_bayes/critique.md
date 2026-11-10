# Critique: MDL and Bayes (C11.05)

Cross-check of evidence_a, evidence_b, evidence_c (81 lines). Ten source PDFs were re-opened this session and checked against the recorded numbers. Claims are in claims.jsonl (K01-K23).

## Numbers re-checked

Confirmed exactly: Blier and Ollivier (MNIST 4.10 vs 24.1 kbits, CIFAR 45.3 vs 89.0 kbits, accuracies 99.5/95.5 and 93.3/61.6); Deletang (ImageNet 43.4 vs PNG 58.5, LibriSpeech 16.4 vs FLAC 30.3, Chinchilla enwik9 raw 8.3, gzip 32.3, LZMA2 23.0); Huang (-0.95 per domain, -0.93 overall, RMSE 3.1%); Voita and Titov (accuracy wrong in 8 of 10 settings, MDL always right); Lotfi PAC-Bayes (MNIST 11.55/11.20, CIFAR-10 74.68, 6.23 KB to 0.38 KB, 358 KB to 46.3 KB); Lotfi LLM bounds (GPT-2 small 12.12 BPD, 96.41/77.90/58.34, 70.76, 15.62); Chlon (0.020/0.011 and 0.039/0.022 bits, candidate mass above 0.999); Falck (Gaussian n=100 m=50; Bernoulli m=n/2 mostly inside the Bayes interval except GPT-4 at means 0.3 and 0.5); Qiu (about 80% agreement with the Bayesian Assistant); the Grunwald and Langford gap (0.5 H(0.2) - 0.2 = 0.1610 by my arithmetic; the paper text reads 0.1609, a rounding difference; the PDF text could not be grepped, so this one rests on arithmetic).

## Corrections made (claims use the corrected values)

1. Arora et al. Bayesian scaling laws (b15, c05). Table 1/3 was misread. Correct values (NRMSE, GINC pretrain): bounded 0.0274 interp / 0.0621 extrap; logistic 0.0272 / 0.1138; Bayesian 3M+1 parameters (scoring-wise) 0.0268 / 0.0814; Bayesian original (M^2+M+1 parameters) 0.0279 / 0.0493. So (a) c05 is wrong that logistic has the lowest interpolation error: the 3M+1 Bayesian law does (0.0268). (b) b15 is wrong that the Bayesian law with 3M+1 parameters extrapolates at 0.0493: that is the larger original law; the matched-size law extrapolates at 0.0814, worse than the bounded law (0.0621). The "Bayesian wins extrapolation" story only holds for the law with more parameters. Claim K15 is therefore marked contested.
2. Lotfi et al. LLM bounds (c14, b23). "Larger models have tighter bounds" is overstated. The table: 124M 12.12, 354M 11.96, 458M 11.95, 773M 12.10, 849M 12.01 BPD; Top-1 bound 96.41, 95.99, 96.69, 96.17, 96.51. All larger models beat 124M in BPD by 0.02 to 0.17, but not monotonically, and Top-100 error is slightly worse for larger models (58.34 to 59.25). Also the c14 claim of "849M 12.01" being tighter than 354M's 11.96 is false.
3. Qiu et al. (c07, b24). Gemma "37%" is the aggregate over simulated users. Appendix F.2 says that when users are filtered to human-stated preferences that match the LLM prior, original Gemma gets about 60%. This weakens the "LLMs cannot do Bayesian updating" headline. Added to K17.
4. c21 and c22 were not re-opened by their authors and only cite subfield 03; they carry little independent weight and are counted as the same source as a13/a10.
5. Duplicate lines: b04-b06 and c16 are the same paper as a07; b17/b18/c01/c02 and a20 are one paper; b21/c10/a21 are one paper. Independent source counts in claims.jsonl count papers, not lines.

## Contradictions between sources

- Wikipedia (b01) says NML "has no Bayesian equivalent". Grunwald and Roos (a04, c15) say NML matches Bayes-Jeffreys asymptotically for regular models and exactly in some luckiness cases. The review is the better source; the subfield claim should read "no general Bayes equivalent; equal only asymptotically or in special cases".
- Falck (b12) says LLM ICL violates the Bayes martingale property; Chlon (c12) says the violation is small in bits and order-averaging recovers it. These are compatible but not tested on the same models, so the size of the violation for current frontier models is unknown.
- Xie (a20) presents ICL as Bayesian; Elmoznino (a14) and Zhang (c11) offer a compression view and a model-averaging view that agree on the same predictions. They are not competing on any measured result I found.
- Lotfi marginal likelihood (b09-b11) vs MDL practice: marginal likelihood is the Bayes code length, and it can anti-correlate with generalisation. This conflicts with the folk idea that shorter total code length always means better generalisation. Boundary: it is misleading for trained-model accuracy; fine for prior fit.

## Weak spots

- Most agent-relevant results (Falck, Chlon, Arora, Qiu) are each a single paper on small synthetic tasks (Bernoulli coins, GINC HMMs, flight choices). No replication on frontier reasoning models.
- Every Bayes-vs-MDL inconsistency result (a07, a08) is from one group (Grunwald) and is theory or simulation.
- No study tests an MDL or Bayes selection rule inside an agent scaffold at equal tokens. All "agent_test" lines are proposals.
- The strongest claim for our use (select by code length with a prior) has only indirect support: Huang correlation across models, Elmoznino theory, Voita and Titov probing.

## Seen only in snippets or secondhand

a01, a02, a23, a24, a25 (Rissanen 1978, Shtarkov 1987, MacKay, Hinton and van Camp, Barron-Rissanen-Yu) were not opened; they are cited via Grunwald and Roos. a21/b21/c10 (Grau-Moya) tables were not extracted. b09-b10 exact Spearman values were not recovered. c24 (no NML in LLM work) rests on rate-limited searches.

## GAPS

1. Does a code-length selection rule (pick the answer or hypothesis with the highest sequence log-probability, with and without a prior term) beat majority vote or self-consistency at equal tokens on reasoning benchmarks? No direct study found.
2. How large is the martingale/order violation for current frontier reasoning models (not just GPT-4, Llama-2, Qwen2.5), and does shuffle-averaging of context give an accuracy gain at equal tokens?
3. Is there any LLM or agent work using NML, luckiness, or minimax-regret selection (the subfield's unique claim)? The search was rate-limited; redo with Semantic Scholar and OpenAlex.
4. Does chain-of-thought length act as a description length that predicts correctness (shorter correct derivation preferred)? Look for studies relating reasoning-trace length or likelihood to accuracy.
5. Do tempered or learning-rate-adjusted combination rules (SafeBayes-style, down-weighting evidence) help when an LLM aggregates noisy samples or tool outputs under model misspecification?
6. How should the prior be set for an agent's hypothesis set: does stating an explicit prior help or hurt (BoxingGym says often neither), and does prior strength interact with the number of observations?
7. Do conditional (hold-out) marginal-likelihood scores, as in Lotfi, outperform total scores for choosing between candidate programs or explanations in LLM program synthesis?
8. Does the prequential gain of a stored memory note (change in later-token loss) predict whether the note helps downstream accuracy better than relevance or recency?
9. Can Bayesian Assistant-style explicit posterior tables, kept in the scaffold rather than trained in, close the plateau after round 1 seen by Qiu et al. at equal tokens?
10. Is post-training's shift of the task prior (Arora) reproducible with independent fits on real LLMs, and does it predict many-shot jailbreak success?

## Gap search results (2026-11-10, evidence_d.jsonl d01-d19, claims K24-K30)

Search tools: Semantic Scholar, OpenAlex and the arXiv API returned 429; WebSearch budget ran out after 2 calls. I used arXiv HTML/abs pages and a paper-search index instead. Negative findings below are therefore weak.

Closed or mostly closed
- Gap 1 (code-length selection vs voting at equal samples): mostly closed. Raw sequence probability alone loses to voting (PaLM-540B GSM8K 59.9 vs 74.4, d01; self-certainty 52.71 vs SC 56.15 on Llama-3.1-8B, d02). A joint reasoning-plus-answer log-prob (PiCSAR) beats self-consistency in 37 of 40 comparisons and at k=6 beats 16 of 20 baselines run at k=16 or 32 (d03). Entropy-weighted voting adds only +0.5 to +3.4 (d07) and nothing in a small AIMO test (d09). No test with an explicit prior term. K24 marked contested.
- Gap 4 (chain length as description length): closed for reasoning models. Shortest chain beats random and longest on 4 models (d05), the same direction in 10 other models (d16) and in a verifier-free comparison (d08); accuracy falls past a peak (d06). No stable effect for non-reasoning models (d08). Failed-step fraction predicts better than length (d16). K25 established.

Partly closed
- Gap 5 (SafeBayes-style down-weighting) and Gap 7 (hold-out scores for candidate programs): partial. BMA over LLM-written programs puts 0.998 to 1.000 weight on one model; stacking by held-out predictive score matches ELPD with spread weights (d10). Tempering was not tested, and nothing compares conditional marginal likelihood with total on program synthesis. K27.
- Gap 6 (prior strength vs observations): partial. Only d15 (toy transformers, loss-complexity tradeoff, abstract only). No LLM study of explicit prior strength vs number of observations beyond BoxingGym (K22).
- Gap 9 (explicit posterior table in the scaffold): partial. BeliefTrack shows prompting fixes belief tracking inconsistently in 7-9B models (update failure 60.0 to 69.0 with a prompt) and RL fixes it (d18). No scaffold-table test at equal tokens.

Stayed open
- Gap 2 (martingale violation for frontier reasoning models; shuffle-averaging at equal tokens): open. Only 7-9B models measured (d13), with loss gains but no accuracy gain reported, and m extra passes per item.
- Gap 3 (NML, luckiness, minimax regret in LLM work): open. Nothing found; two-part MDL agents exist (RIMRULE +4.5/+4.6 over prompt consolidation, d11; MIDGARD, d12). K29 and K26.
- Gap 8 (prequential gain of memory notes): open. Memory Tax (d17) shows memory systems below RAG but does not score notes by loss change. K30.
- Gap 10 (independent fits of prior shift; link to jailbreak): open. Only the original authors fit it, and non-Bayesian laws fit about as well (d14).

Notes on integrity
- I accidentally re-ran an older generator (C11.05_mk.py) from the folder; it rewrote evidence_b.jsonl with the same size (19031 bytes) and ids b01-b26. No content difference was detected, but I could not diff because the folder is untracked.
- Author names were not available for several 2025-2026 preprints (d06-d09, d13, d16-d18); sources are named by title and arXiv id.
- The cross-checker's corrections of Arora et al. (b15, c05) are kept; my fetch of that paper gave table values that disagreed, so they were not used.
