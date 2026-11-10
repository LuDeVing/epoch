# A17.10 Transactive memory and reasoning: cross-check critique

Checker: re-opened PDF text of Kim et al. 2606.19911 (MATM), Li et al. 2505.11556 (HiddenBench), Shang et al. 2506.06843 (CoThinker), Babu et al. 2608.20564 (Consilience), and the PMC full text of the collaborative-inhibition meta-analysis (PMC11428894). Scratch PDFs deleted after extraction.

## Numbers re-checked (10 and more)

| # | Number | Source | Result |
|---|--------|--------|--------|
| 1 | CI meta-analysis d=0.54, CI 0.49-0.58, 140 studies, 185 ES, N=19,492 | PMC11428894 | Confirmed |
| 2 | Membership: strangers 0.75 (k=46), acquaintances 0.45 (21), friends 0.18 ns (8), couples -0.19 ns (9), QB=17.68 | Table 1 | Confirmed. Evidence file a12 right; b02 gave only p-values for couples/friends (fine) |
| 3 | Monitoring yes d=0.14 p=.20 (k=12) vs no 0.66 (k=173) | Table 1 | Confirmed |
| 4 | MATM ALFWorld 0.4708 / 0.5511 / 0.6431; steps 11.77 / 11.18 / 10.35 | text + table | Confirmed. The extracted table is shifted by one row, so read steps from the paper's prose |
| 5 | MATM scope: ALFWorld 0.646/0.631/0.599; WebArena 0.298/0.277/0.1915 | Table 2 | Confirmed. WebArena cross type is 0.1915 (a02 said 19.1, b17 and c03 said 19.2; both are rounding of the same value) |
| 6 | MATM oracle 20.07 to 38.69 and 16.58 to 40.38 | text | Confirmed |
| 7 | MATM 98.6% / 31.8% / effective producers 2.2 vs 10.5 | text | Confirmed |
| 8 | HiddenBench 30.1% vs 80.7%; humans 0.125/0.385/0.604; GPT-4.1 0.008/0.233/0.733 | abstract, text | Confirmed |
| 9 | HiddenBench N=3 +0.348 to N=7 +0.006; dissent GPT-4.1 0.233 to 0.492, Gemini 0.889 to 0.306; Reveal-All 0.926/0.982; secretary 0.241/0.713; structured 0.800/0.727/0.743 | tables | Confirmed |
| 10 | CoThinker TMS ablation 81.87/76.41, 55.97/62.36, 57.15/58.37; TMS-on styles-off 69.79/49.02/48.21; tokens Flash-8B 13,688 | table lines | Confirmed |
| 11 | Consilience 0.83 vs 0.26; 11 of 12 models; +0.13; 15-model means 0.083/0.285/0.731/0.843; 82.22% | text | Confirmed |

## Corrections and additions

1. Trim-and-fill: the CI meta-analysis authors report that correcting for 36 missing studies cuts d from 0.54 to 0.40 (CI 0.33-0.51), still significant. Angles A and B both gave only 0.54 and the fail-safe N 31,401. Put 0.40 beside 0.54 whenever cited.
2. CoThinker's "16 of 25 comparisons Holm-significant" is internally inconsistent in the appendix: 13 wins + 2 losses (single-agent) plus 3 wins + 1 loss (multi-agent) is 19, not 16. Three losses are all on instruction-following, which the authors call the low-load boundary. Treat the count as unreliable; the direction (wins on high-load items, losses on instruction-following) is stable.
3. In HiddenBench the dissent table row labels are split across lines in text extraction; the first row (0.233 to 0.492) matches the prose for GPT-4.1, so assignment is right.
4. Evidence a17 reports b=0.42 for curiosity to TMS; b23 reports r=.37 for the same link. These are different statistics (path coefficient vs correlation), not a conflict.
5. a02 and c03 say the oracle result is one consumer and one seed. Confirmed; do not generalise.
6. b02 says published-only friends are "24 vs 24"; Table 2 shows friends k=2, d=0.22 ns. Use k=2.

## Contradictions between sources

- Shared vs local memory: MATM finds a shared pool helps; LLMA-Mem finds local per-role memory beats shared and hybrid (3 points, no variance). The designs differ (trajectory reuse across consumers vs role-specific episodic memory), so this is unresolved, not refuted.
- CoThinker's TMS module helps one backbone and hurts two. Their cause (newer models refusing to show reasoning) is untested.
- Dissent: helps GPT-4.1, kills Gemini-2.5-Flash. No universal setting.
- Humans and LLMs: familiarity removes group recall loss in humans; LLM agents from one model are maximally "familiar" yet HiddenBench shows they still fail to pool. So familiarity alone does not make a directory.
- Reranker features helped ALFWorld a lot and WebArena little; LambdaMART fell to baseline on WebArena.

## Weak spots

- No study tests a Wegner-style who-knows-what directory in an LLM loop with an ablation. MATM and CoThinker borrow the name only. LLMA-Mem has a transactive module but no ablation. iAgents InfoNav and Consilience route are close analogues, evaluated on their own benchmarks by their authors.
- Almost every machine result is a preprint by one group, single benchmark family, and often designed on the same family it is tested on (Consilience, the structured exchange protocol).
- WebArena memory tests use 47 tasks; one task is about 2 points.
- Human TMS evidence is mostly self-report surveys (Lewis scale), cross-sectional, so the TMS-performance link is correlational. Collaborative inhibition studies use word lists, not reasoning.
- CoThinker's cost is about 19x IO tokens; no matched-compute single-agent baseline (e.g. best-of-N), so gains may be a token effect.
- Several 2026 arXiv numbers (ids 2606, 2608, 2610 etc.) come from preprints I could not cross-check with a second group.

## Only seen in snippets or abstracts (opened:false)

Wegner 1987, Wegner/Erber/Raymond 1991, Lewis 2003 (abstract), Liang/Moreland/Argote 1995, Hollingshead 2001 (abstract), Bachrach 2019 (abstract), Sparrow 2011 (abstract), Camerer 2018 (abstract; Sparrow's inclusion and per-study result unconfirmed), Lu/Yuan/McLeod 2012, Stasser & Titus 1985, ICU human-AI teaming 2023 (abstract). None of the founding human numbers (Liang 1995, Wegner 1991) were read; the file gives no founding-study figures.

## GAPS

1. Does a code-held who-knows-what directory (competence per tool, sub-skill or memory store, updated from measured success) beat a flat store at equal tokens in an LLM agent? No published ablation isolates this.
2. What are the actual numbers in the founding human studies (Liang, Moreland and Argote 1995; Wegner, Erber and Raymond 1991; Hollingshead 1998, 2001): recall counts, errors, effect sizes, and which replicated?
3. Did the Sparrow, Liu and Wegner 2011 effect replicate in Camerer 2018, with what effect size, and what does the Gong and Yang 2024 meta-analysis give as the pooled d for "remember where, not what"?
4. Does the exchange-then-decide protocol and the Consilience controller transfer to tasks not built from the HiddenBench family, and do they beat a single-context call with all facts at equal tokens?
5. How much of the MATM-style experience-store gain survives after near-duplicate removal, and does it replicate outside ALFWorld and WebArena (e.g. code, math, planning tasks) by an independent group?
6. Is CoThinker's gain a compression effect or a token effect? Needs a matched-compute baseline (best-of-N, self-consistency with the same tokens) and per-backbone ablation of the rolling summary.
7. Does source-credibility weighting (provenance, past success) in memory retrieval help at all, given MATM found producer strength irrelevant? Test with deliberately wrong sources.
8. Does forced dissent have a sign that can be predicted from the backbone (e.g. baseline pooling accuracy), or must it be tested per model?
9. Is the collaborative-inhibition loss reproduced in LLM sampling (pooling N recalls through shared context vs code-side union), and does a monitoring ledger remove it as the human d=0.14 suggests?
10. Does answer-first-then-consult (reflection first) cut anchoring on retrieved memory in LLMs, beyond the small human study (N=42)?

## Gap search results

New evidence is in evidence_d.jsonl (d01-d22). Claims K18, K11, K12, K17 were edited; K24-K31 are new.

| Gap | Status | What was found |
|-----|--------|----------------|
| 1 Code-held directory vs flat store at equal tokens | Partly closed, still open at matched tokens | Two independent preprints test a competence or reliability table updated from outcomes: MetaCogAgent (82.4 vs majority vote 77.1 vs single agent 65.3; static profile costs 3.2 points) and Sigma-Mem (46.22 to 71.10 under a reliability shift). Both on authors' own benchmarks, neither compares with a flat store at equal tokens. Delivery matters: agents made zero voluntary memory calls in 114 turns (d20). |
| 2 Founding human numbers | Open | Wegner 1991, Liang 1995 and Hollingshead 1998 are paywalled (403 from the author site). Only designs and the qualitative result (couples win only with their own division; strangers win when categories are assigned) are known, from a secondary source. No counts or effect sizes. |
| 3 Sparrow replication and meta-analysis | Closed for the priming step; partly open for where-versus-what | Camerer 2018 replication report: pooled N=234, 2.89 ms, t(233)=0.76, p=.449 against original t(45)=3.26. Hesselmann 2020: N=89, BF01=5.07. Gong and Yang 2024: 22 studies, memory-task subgroup d=0.56, CI -0.15 to 1.28; no clean pooled d for 'remember where, not what'. Experiments 3-4 of Sparrow were not replicated by anyone found. |
| 4 Transfer of exchange protocol and Consilience | Open | ICML 2026 HiddenBench version adds no outside task. A matched-cost debate study (2.1-3.4x tokens for equal or lower accuracy, homogeneous 7-8B teams) argues against open exchange when information is not split. |
| 5 MATM gain after near-duplicate removal; independent replication | Partly closed | Xiong 2026 (independent group): add-all storage below fixed memory on all four agents; strict-checked additions above it. Supports quality gating. No code, math or planning replication of MATM itself, and no direct near-duplicate-removal ablation. |
| 6 CoThinker compression vs token effect | Open | No matched-compute CoThinker rerun found. A theory paper (2601.17311) states the condition for synergy at equal budget, and the debate study shows exchange can cost 2-3x tokens for no gain. Still needs a best-of-N run with the same tokens. |
| 7 Source-credibility weighting | Partly closed, now contested | Sigma-Mem shows weighting by outcome history helps when peers truly differ and hurts when feedback misleads (CF@50). Showing confidence scores gave nothing significant in debate (+0.025, SE 0.015). Nobody tested deliberately wrong sources with provenance tags directly. |
| 8 Predicting the sign of dissent | Open | Debate study: outcome bounded by the strongest reasoner, majority pressure suppresses correction. No rule found linking baseline pooling accuracy to the sign of forced dissent. |
| 9 Collaborative inhibition in LLM sampling | Open | No LLM study found after OpenAlex and web searches. |
| 10 Answer-first before consulting memory | Partly closed on the harm side | MemTrapBench: every memory framework fell below no-memory (over 10 points; trap case 31.05% vs 94.39%); MERIT: agents ignore a correct retrieved fact 45-53% of the time. Answer-first ordering itself was not tested. |

Caveats on this search pass:
- Search budget used: 5 of 8 WebSearch calls; arXiv export API returned HTTP 429 (shared limit), so OpenAlex and Semantic Scholar were used for discovery.
- Sigma-Mem and Xiong tables were read from text extractions with garbled columns; margins over the baselines in Sigma-Mem were not read exactly.
- The Camerer 2018 article page was opened only at abstract level; the Sparrow-specific numbers come from the replication project's own report on OSF.
- Several 2026 items (MetaCogAgent, Sigma-Mem, MemTrapBench, MERIT, Epistemics of Agent Memory) are single-group preprints.
