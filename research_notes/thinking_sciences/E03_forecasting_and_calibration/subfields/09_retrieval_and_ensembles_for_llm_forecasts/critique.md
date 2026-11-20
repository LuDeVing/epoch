# Critique: E03.09 Retrieval and ensembles for LLM forecasts

## Checks made (re-opened this session)
Halawi et al. 2024 (arXiv 2402.18563 PDF text), ForecastBench (arXiv 2409.19839 PDF text), FRI Substack post of 2026-01-29.

Confirmed:
- Halawi Table 14 (validation): mean .1656, median .1651, geometric .1655, trimmed .1649, USC .1691, no ensemble .1676, crowd .1600.
- Halawi Table 5: rows .179, .182, .181, .183, .186, .206 (crowd .146 in that table). Weighted crowd mix uses 4x weight on the crowd.
- FRI post: xAI Grok 4.20 Preview and Cassi ensemble_2_crowdadj tied #2; gap to superforecasters 0.017; Cassi uses Tavily retrieval, o3 + GPT-5 ensemble, a review LLM, and a "crowd adjustment" for platform questions when forecast and price disagree. The "nearly 0.01" figure is only partly seen (sentence cut off in my extraction; the earlier agent read it in full).

Corrections:
1. c03 mislabels Table 5. Correct reading: .181 is fine-tuned GPT-3.5 alone, .183 is the same without retrieval, .186 is base GPT-4 with retrieval, .206 base GPT-4 without retrieval. So retrieval is worth about 0.02 for a base model but only about 0.002 for the fine-tuned setup. a02 and b02 are right; c03 ("base GPT-4 only 0.181", "no IR 0.186") is wrong. b02's "retrieval plus fine-tuning = 0.027" is a mix of two rows and is loose.
2. ForecastBench best-LLM number on the 200-item set: text says Claude 3.5 Sonnet 0.122; the table row for freeze values + scratchpad says 0.128 (news version 0.132). b10 uses 0.122 (text), a09 0.128 (table). The paper is internally inconsistent; use 0.128 from the table, and say so.
3. Halawi crowd Brier: .149 in the main test text, .146 in the Table 5 caption (different subset or rounding). Keep .149 as the headline.
4. a22 and b14 depend partly on snippets/summaries (see below).

## Contradictions between sources
- Does retrieval help? Halawi: yes for a base model (.02); Pratt et al.: News API best strategy but worse than the basic prompt; Lu and Zhang: RAG worsened Brier (.159 to .250) because of upward shift. Likely explanation: retrieval quality and base-rate handling, not retrieval itself.
- Does averaging help? Halawi .003; FutureSearch cuts SD by two thirds (variance, not Brier); Hsieh: ensembling hurt base GPT-4o. Variance reduction does not imply Brier gain when bias dominates.
- Crowd adjustment: Halawi gains .003 overall (4x crowd weight); Cassi nearly .01 but only on market questions and from a blog. Different setups, not a replication.
- Thinking models: FutureSearch found no significant gain; Metaculus found higher-reasoning twins win 8 of 8 pairs. Different metrics and question sets.

## Weak spots
- Most Halawi numbers (a01-a05, b01-b06, c01-c05) are one paper triple-counted by three agents. Independent sources for ensembling gain are really 1.
- Nobody has measured the averaging gain at equal total tokens. All evidence is at equal question, not equal compute.
- Cassi and xAI results come from a blog post with no per-entry scores and no ablation; xAI's 8-run average is not separated from its search tools.
- Metaculus winner statistics (28 vs 7 calls, 86% ensemble) are observational and confounded by effort.
- Question sets are small (31, 113, 202, 464) with wide CIs; many p-values uncorrected.
- Leakage (Paleka, El Lahib) means older retrieval-based results may be inflated; Halawi has at least 3.8% early-resolved questions.

## Seen only in snippets or secondary summaries
- a22, a23, a24 (Metaculus notebook and LessWrong synthesis, via page summaries), c24 (search snippet only, unverified).
- The "nearly 0.01" crowd-adjustment gain: single blog sentence; no table.
- a18 values not transcribed.

## GAPS
1. Does averaging N runs beat one longer run at equal tokens for a scaffolded agent (no study measures this)?
2. How much of the retrieval benefit survives leak-free search (what is Halawi's gain with leak-checked retrieval)?
3. What exactly is Cassi's crowd-adjustment rule and score, and is the near-0.01 gain real outside market questions?
4. Is diversity (different prompts or models) worth more than extra copies at equal calls, and how many distinct members before the gain flattens?
5. How to detect and reject poisoned or fabricated retrieved articles without discarding the 39% of genuine news that filters drop?
6. Why does retrieval raise mean forecasts (0.20 to 0.46)? Does a base-rate-first step or shrinkage to a reference class fix it?
7. Does xAI's 8-forecast average vs its search tools explain its #2 rank (needs ablation)?
8. Does a consistency check (arbitrage violations) work as a cheap filter to pick or weight ensemble members?
9. Does the small-ensemble gain hold for reasoning models whose own per-run variance is lower?

## Gap search results (evidence_d.jsonl, d01-d21)
Sources opened this pass (PDF text): Murphy 2026 BLF (2604.18576), AIA Forecaster (2511.07678), Aitchison et al. 2026 (2606.29661), Peng et al. 2026 (2609.33257), SoccerArena (2607.24573), CHAIN (2609.36689), Corroboration Illusion (2609.22246), Hindcast (2607.14051), Paleka et al. (2412.18544), Temporal leakage (2602.00758), FutureSearch blog.

1. Equal-token averaging vs one longer run: STAYED OPEN. Closest is CHAIN (d14): 5-sample average gained 0.004 Brier, a structured 5-call method 0.036, but the structured method used 4.9x the tokens. Aitchison (d11) fixes the number of samples, not tokens. Nobody has matched tokens.
2. Retrieval benefit under leak-free search: PARTLY CLOSED. Hindcast (d18) shows gains on 8 of 9 small models with immutable pre-cutoff archive (up to 23%); AIA (d09) shows about 0.009 Brier overall for agentic search with foreknowledge filtering; the leakage audit (d20) has no closed-book baseline. Halawi's own gain with leak-checked retrieval is still unmeasured.
3. Cassi crowd adjustment: PARTLY CLOSED. BLF (d01, d02) puts Cassi on common questions: market gain over the plain price is +0.6 Brier Index points, not significant; overall +1.0 over crowd+prior, not significant. AIA (d09) measures the price itself as worth 0.010-0.013. The exact rule is still unpublished. K11 moved to contested.
4. Diversity vs copies: CLOSED in direction, open in size. Aitchison (d11), Peng (d12), SoccerArena (d13): diversity pays only when members are decorrelated; gains flatten near 3 distinct members. All are small (N=113 to 1,000+) and one includes a fine-tuned model.
5. Poison detection without dropping real news: STAYED OPEN. Corroboration Illusion (d17) shows each tested defense has a cheap bypass; BLF (d05) leak filter drops 29.9% of clean results. No defense that keeps genuine news and rejects poison has been shown. Only tested on 7-8B models.
6. Why retrieval inflates means and fixes: MOSTLY CLOSED. Corroboration Illusion (d16): base-rate prompt .250 to .184; per-document median .250 to .222; still above base-rate-only .127. Platt/extremization (d10) fixes the opposite hedging bias. Frontier-agent test of a combined fix is missing.
7. xAI 8-run average vs search tools: STAYED OPEN. BLF (d01) reports Grok 4.20 only on one tranche and no ablation; Aitchison (d11) suggests Grok models add value by decorrelation. No ablation of the xAI entry exists.
8. Consistency as ensemble filter: CLOSED NEGATIVE/UNTESTED. Paleka (d19): correlations are across models, vary by check (Negation -0.36 on NewsAPI), and a consistency-patched forecaster did not improve accuracy. No study filters or weights ensemble members by consistency. K14 moved to contested.
9. Small ensembles for reasoning models: PARTLY CLOSED. FutureSearch (d15): 4 mixed frontier runs gained about 0.005; BLF (d04): reasoning model still has market cross-trial SD about 0.09-0.10, cut to 0.03 with a belief state. No clean reasoning vs non-reasoning matched comparison.

Caveats of this pass: Fig 2a K-curve in BLF read only as a range from a figure; BLF Table 2 rows matched to methods by arithmetic after PDF row jumbling; d21 is snippet-only (opened:false). Web search budget used: 8 of 8.
Most new sources are 2026 preprints, workshop papers or blogs not yet replicated.
