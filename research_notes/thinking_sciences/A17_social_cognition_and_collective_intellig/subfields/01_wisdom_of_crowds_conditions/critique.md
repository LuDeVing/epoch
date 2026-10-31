# A17.01 Wisdom of crowds: conditions - cross-check critique

## Corrections and confirmations (re-opened this session)
Confirmed from arXiv abstract pages: Wang 2023 self-consistency (+17.9 GSM8K, +11.0 SVAMP, +12.2 AQuA, +6.4 StrategyQA, +3.9 ARC-c); Kim 2025 (350+ LLMs, 60% agreement when both err); Schoenegger 2024 (12 LLMs, 31 questions, 925 humans, acquiescence, +17-28% in Study 2; the equivalence result is exploratory, not preregistered); Denisov-Blanch 2026 (five benchmarks, 25x cost, no consistent gain, correlated errors, confidence weighting no benefit); Li 2025 Self-MoA (+6.6 AlpacaEval, +3.8% average).
Corrections and flags:
- a15 Agent Forest: the abstract has no numbers; the +12 to +24 style figures come from the paper body and were not re-seen here. Treat as read-by-agent, unverified by me.
- a01/a02/a03 are one source (Wallis 2014); Galton 1907 itself was never read. Wallis gives median 1208 (draft) / 1207 (published), truth 1197 vs 1198. K01 is therefore marked single-source.
- a04 vs a02: Wikipedia summary gave Galton as 800 guessers; Wallis says 787 usable cards. Use 787.
- c23 vs MoA: 65.1% vs 65.8% both appear in one paper; use 65.1.
- b12/c01 duplicate the same Schoenegger figures; a13, b12, b13, c03 are one study, not four sources.
- a16/b19/c14 (and a17/b20/c15) are the same Kim et al. paper. Counting them as independent would inflate K03; independent support there is Goel 2025, Denisov-Blanch 2026 and Kohli 2026.
- b04 reports individual error -23% and mean error -10%: check these are different metrics before quoting either.
- Douven: a20 gives best single Brier 0.284 (Opus 4.6), c04 gives 0.273 (Sonnet 4.6) on the 208 set; different subsets, not a contradiction.

## Contradictions between sources
- Social influence: Lorenz 2011 (harm) vs Becker 2017 and Almaatouq 2021 (help in decentralised networks or with proper weights). Resolution is network structure and weighting, not a single sign.
- Diversity: Barrera-Lemarchand (heterogeneous groups beat clones) vs Li 2025 Self-MoA (same-model repeated beats mixed). Likely reconciled by member quality gaps and by task type (numeric estimation vs open generation), but not tested head to head.
- Debate: Du 2023 style gains vs Huang, Smit, Wang, Debate-or-Vote finding vote is as good or better. Weight goes to the latter, which controls compute.
- Verified vs unverified: math voting works (verifier or exact answer), truthfulness voting does not. These are consistent once framed as scatter-of-wrong-answers.

## Weak spots
- Many 2026 items are preprints (Denisov-Blanch, Kohli, Chetlapalli, Douven, Barrera-Lemarchand, hidden clones). Single studies; effects small.
- Condorcet correlated-vote theory (Ladha 1992) and Hong-Page/Thompson critiques were cited from memory or secondary reading (a26, b09, b10, b25). Page's book unopened.
- Human replications are few: the crowd-within replication is one lab; Frey and van de Rijt 2021 was seen only through summaries.
- Almost all LLM crowd tests use multiple choice, exact-answer math or short numeric answers. Open-ended reasoning traces are untested for independence.
- No study found that measures, for one model, how sampling temperature or prompt diversity changes error correlation versus a vote's realised gain, at equal tokens.

## Seen only in snippets or not opened
a01, a12, a26, a27, a28, b07, b10, b11, b24, b25, b26, c25 (opened:false). Their numbers are not used in claims except as hedged context (K12 uses b26 only as secondary).

## GAPS
1. Does resampling one model with prompt/frame diversity lower error correlation enough to restore the gain of voting, measured against Condorcet's independent prediction, at equal tokens?
2. On items with no verifier, what is the best use of extra tokens if voting only reinforces shared errors (verification, retrieval, critique by a different frame)? Any head-to-head at equal tokens?
3. Does vote gain track n_eff (Kish or participation ratio) quantitatively across tasks, so we can predict when k samples are worth it?
4. When is heterogeneity worth it: what quality gap makes mixing models lose (Self-MoA) versus win (clone test), and does this transfer to a single-model agent using different roles?
5. Does confidence or self-consistency fraction give any usable truth signal for stopping or escalating (Denisov-Blanch says confidence weighting fails; Surprisingly Popular needs expert minority)? Can "predict what others will say" be turned into a diagnostic of shared bias?
6. Within-agent crowd-within: how much gain from two spaced or reframed samples versus two same-prompt samples in LLMs, and what plays the role of delay?
7. How much does showing prior sample answers to later samples (anchoring, social influence) hurt or help in a revision step, versus blind independent revision?
8. What is the best aggregator for numeric and probability answers under LLM acquiescence and skew (median, geometric, extremized mean), tested on post-cutoff items?
9. Hong-Page search diversity: does a team of different search strategies beat the best strategy repeated on real agent search tasks?
10. Ladha-style correlated-vote bounds: what is the maximum achievable vote accuracy given measured pairwise error correlation of our samples?


## Gap search results (evidence_d.jsonl, d01-d16)

Search note: the WebSearch budget ran out after four queries, and arXiv, OpenAlex and Semantic Scholar all returned HTTP 429 afterwards. Finds came from the first four searches plus arXiv API results before the rate limit. Searches for Surprisingly Popular in LLMs, Kish n_eff versus vote gain, Hong-Page on agent search, and post-cutoff extremizing found nothing; this is a search failure, not proof that none exist. d14, d15 and d16 were read as abstract pages only.

**Closed or mostly closed**
- Gap 10 (Ladha-style bound): closed as a calculation (d10, d11). With per-vote accuracy 0.69, rho=0.1 caps majority vote at about 0.887 and rho=0.2 at 0.805; independence would reach 1.0. d04 adds that the true cap is the all-wrong rate (0.052 on MATH-500), which rho does not identify. New claims K21.
- Gap 7 (showing earlier answers): answered for small 7-8B models (d05): blind self-revision beat peer-visible debate, up to 27.6 pp. Single study, so K24 is single-source. Larger and reasoning models untested.
- Gap 2 (no-verifier token use): mostly answered. A separate selector or verifier beats more same-model votes (d07, d08), and voting plateaus without a checker (d16). But no study compares verification, retrieval and different-frame critique at equal tokens, and retrieval is untested. K22.
- Gap 5 (confidence as truth signal): partly answered (d13, d14, d02). Confidence is weak (52-62% pair discrimination) but saves samples. Nothing found on Surprisingly Popular or "predict what others say" as a shared-bias diagnostic. K25.

**Partly answered**
- Gap 1 (prompt diversity at equal tokens): contested (d01, d02, d03). Prompt diversity did not help when sampling already decorrelated errors (AIMO 3), helped pass@k and best-of-N but not majority vote (Wang), and persona frames lowered correlation without an equal-token baseline (d02). K20.
- Gap 4 (heterogeneity): d12 gives regression weights (quality coefficient larger than diversity on MMLU, CRUX, MATH); d04 gives one matched-quality win (+0.027 at k=3); d07 shows diversity needs a selector. No numeric quality-gap threshold was found, and transfer to one model in different roles is untested.
- Gap 8 (aggregator): d06 shows median of 30 samples beats mean, mode and greedy on numbers, including 15 post-cutoff FUTURE questions. Probability answers, extremizing and geometric mean were not tested. K26.
- Gap 6 (crowd within): d06 supports averaging same-prompt samples by median; reframed or delayed samples versus same-prompt were not found. Rephrased frames plus synthesis helped (d09), which is not the same test.

**Still open**
- Gap 3 (vote gain versus n_eff across tasks): only indirect evidence (d04 shows rho is not enough; d11 gives the prediction curve). No study ties measured n_eff to realised gain.
- Gap 9 (Hong-Page search diversity on agent search tasks): nothing found.

**Changes to claims.jsonl**
- K06 raised from single-source to established (d03, d08, d16 independent of earlier sources).
- K08, K10, K13, K07, K11 got extra evidence ids; K08 stays contested.
- New claims K20-K26 (K20 and K23 contested, K24 and K26 single-source).
- Note for K23: d07 and d09 disagree on synthesis; the difference could be model, task or aggregator.
