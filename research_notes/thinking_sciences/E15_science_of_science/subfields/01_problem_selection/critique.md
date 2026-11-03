# E15.01 Problem selection: cross-check critique

## Corrections made (sources re-opened this session)

Re-opened full text of: Si et al. 2024 (arXiv 2409.04109), Si et al. 2025 (2506.20803), Wen et al. 2025 (2506.00794), Gupta and Pruthi 2025 (2502.16487), Gu and Krenn (2405.17044), Foster et al. 2015 (arXiv 1302.6906), Hill et al. 2025 (PMC12222024), Wang et al. 2017 (Lirias PDF), Tong et al. 2026 (2603.14473), Gong et al. 2026 (2603.16659).

Confirmed with no change: a01/b01 (Test 1 per-review novelty 4.84/5.64/5.81, N=119/109/109); a05-b07 (Table 4, gap table, correlation table); a07/a08/c05 (1,585 and 6,000 pairs, 51.9%, 48.9%, 64.4%, 63.6%, 75.1%, 38.8 to 53.0); a10/a11 (24.0%/36.0%, 88.8/89.0, 1.3/32.7, 51.3/68.5, Turnitin and OpenScholar 0); b08-b11 (181,078 nodes, 84,709,977 links, 85.8/14.2, 12.4/1.8, R=0.983, R2=0.2916, 2.26, 24%/35%, 137 prizes, 7594 awardees, 241,176 articles); b13-b16 (89%, +18% dispersion, +57%, 19%/11% subject categories, 10%/17% JIF); b19-b21 (7.4%, 2.2%, 93%, 88%, 2.1%, 1.8%, 43%, 35%, 29%, 61%/59%); c15/c27 (59.2, 41.6, 31.1, 38.8, 55.0 to 85.5, 87%, 0.145, 36.2).

Corrections:
1. c01 mislabels the per-idea (Test 2) figures. Per-idea NOVELTY is 4.86 / 5.62 / 5.78 (Human / AI / AI+rerank, N=49 each, p 0.03 and 0.00). The 4.56 / 5.18 / 5.45 and p=0.08 in c01 are the EXCITEMENT scores. Claims use the corrected novelty values. Also c01 calls the AI-alone novelty gap non-significant per idea; it is significant (p=0.03) for novelty, not for excitement (p=0.08).
2. a16 and c10 say high-citation-predicted pairs were rated 1.94 (lower than random). The paper's 1.94 is a test statistic ("weak statistical evidence (1.94)"), not a mean rating. The means are 2.350 (high-citation), 2.446 (random), 2.414 (titles-only). The difference is about 0.1 point.
3. a24: "24.9% rated 4 or 5" is 1,107 of 4,451 ideas; 394 rated 5. The a24 text is fine; b23 gives 1,632 (36.7%) rated 1. Confirmed.
4. a03 gives Claude-3.5-Sonnet 71.4% ranker accuracy; this is on ICLR review pairs (a different task). The ranking of the idea pool by the same LLM judges was 43-53% (c03/b03). These are not contradictory but must not be mixed.
5. c14: the 64.7 to 80.9 (Qwen3-4B) and 71.7 to 83.1 (30B) gains are in-domain table values (Table 3); the paper's text at Section 4.3 describes the same numbers as 2025 temporal results. The paper is internally ambiguous; we use "in-domain" and flag it. Thinker win rates 81.5% and 76.5%, and 54.2% against three strong LLM judges: confirmed.
6. a05 phrasing "AI ideas dropped much more after execution than human ideas" is right for the within-idea gap (p 0.001-0.025). It must be paired with c22: direct per-idea post-execution comparison (N=43) is not significant on any metric (FDR 0.175-0.586). The per-review result (N=181, one-sided) is significant on 4 of 5. The paper itself says it lacks power to confirm its pre-registered hypothesis.
7. b10: 24% and 35% are not "needed odds"; the paper derives p(new)=0.76 p(repeat) and p(jump)=0.65 p(repeat) from equal expected citations (mean citations 8.38 repeat, 11.00 new, 12.90 jump) and calls it unlikely. Same content, wording fixed in claim K12.

## Contradictions between sources

- Prompted judges vs trained judges: Si and Wen show prompted LLMs at chance; Tong, Gong, Wen-fine-tuned show 59-83%. Not a conflict; different supervision. But the trained ones are fine-tuned weights, so it is unclear what transfers to a pure scaffold.
- Gu and Krenn: citation-impact prediction (Krenn and Zeilinger AUC 0.85; Krenn 2022 AUC 93-99%) does not translate to expert-rated interest. Predicting what will be studied is not predicting what is interesting.
- Hill 2025 (pivoting is penalised) vs Foster 2015 (rare strategies earn more citations on average but not enough for the risk) vs Wang 2017 (novelty wins long run, loses short run): all point to short-run penalties for novelty, but they use different novelty measures (journal combinations, chemical links, distance from own work).
- Si 2024 (AI ideas more novel) vs Gupta and Pruthi (24% plagiarised, partly from the same pool) vs Si 2025 (novelty advantage vanishes after execution): blind novelty ratings do not survive retrieval or execution checks.

## Weak spots

- Almost all LLM evidence is NLP/AI research ideas (Si, Wen, Gupta). Gu and Krenn covers wider fields but only with one LLM family.
- Most N are small (N=19 and 24 ideas in Si 2025; 45 pairs for experts in Wen; 50 proposals in Gupta).
- Many "AI scientist" systems (a12, a13, b31, b33, c12) are judged by LLMs; independence of the judge is weak. Status "contested" for K20.
- No test at equal tokens of a scaffold (rather than fine-tuning) for question selection. Every trained-judge result is weights.
- Citation counts as a proxy for question value are a strong assumption (Foster, Hill, Tong, Wang).

## Only seen in snippets or abstracts (not opened in full)

- a18/b08 Foster: b08 opened the arXiv version; a18 only the Crossref abstract. Treat the published ASR version as unread.
- a19/b12 Rzhetsky et al. 2015 PNAS: abstract only; no simulation numbers.
- a20 Fortunato 2018: abstract only.
- a22 Kuhn 1959, Kitcher 1990: from memory, no numbers.
- c16 BoLeBench: conference listing abstract only; the 70.8%, 67.1% and 36.0% figures are unverified.
- c17-c19 Swanson 1986, Tshitoyan 2019, Krenn 2020 (c19 duplicates a15, which was opened): not opened.
- b34 SciMON and a13 ResearchAgent: exact human-eval tables not extracted.
- c13 AI Idea Bench 2025: benchmark description only; no model results recorded.
- b29, b30, b31, c11, c12, c21: not re-opened in this cross-check.

## GAPS

1. Does a prompting-only scaffold (retrieval of past question-outcome pairs plus a cheap probe run) match the fine-tuned judges of Wen, Tong and Gong at equal tokens? No study tests this.
2. How large is the S0 probe-run effect: how much does a cheap pilot (not 100 hours of execution) recover of the ideation-execution gap, and at what token cost?
3. What novelty-check design (retrieval depth, full text vs abstract, separate judge model) is cheapest and still catches the 24% rewrite rate? Wen found full papers beat abstracts (53.0% vs 38.8%); is there a cost curve?
4. Do the results (Si, Gupta) hold outside NLP and for questions that are not paper ideas (debugging, business, engineering problems)? Which evidence exists for open-ended question choice in tasks an agent actually receives?
5. What portfolio rule (fraction of risky vs repeat questions) is optimal when the agent has a fixed token budget? Foster and Rzhetsky say the human mix is too conservative; is there a model with numbers the agent could use?
6. Is the pivot penalty (Hill 2025) a cost of lost expertise, which the agent has little of, or a social/reputation cost, which it lacks? This decides whether switching questions is cheap for an agent.
7. What do BoLeBench and the "pick the bolder attempt" rule actually measure? Need the full paper and a replication on other corpora.
8. Does self-consistency or tournament selection (Co-Scientist Elo) beat single-pass question choice under an independent outcome measure, at equal tokens, not LLM-judged?
9. How do expert rater disagreement (56.1% in Si) and the 3-5 reviewer panels needed affect the cost of building a trustworthy gold label for our own agent tests?
10. Are there published replications or failures of the Wen et al. result on newer cutoff dates or different fields (the test set was built after one base-model cutoff)?

## Gap search results

Searches: WebSearch used 3 calls (the shared budget then ran out); arXiv and OpenAlex and Semantic Scholar APIs were rate limited (429), so the rest came from direct arXiv PDFs, PMC pages and Europe PMC. New evidence is in evidence_d.jsonl (d01 to d18); claims K23 to K29 added; K04, K06, K07, K11, K12, K14, K20 got extra evidence ids and short claim additions.

Closed or mostly closed
- Gap 2 (probe-run effect): closed for ML tasks. d02: pairwise selection accuracy goes from about 65% (reasoning only) to 78.5% with a 5-minute pilot, 82.8% at 30 min, 84.0% at 4 h. Not tested on open research questions with a cheap pilot against the 100-hour execution gap (K24).
- Gap 6 (pivot penalty): answered. d10: reputation and audience explain only about 26% of the penalty. The rest looks like lost local knowledge; an agent has cheaper switching but not free (K28).
- Gap 9 (gold-label cost): answered. d08, d15, d13: pairwise expert agreement 56.8% and 56.1%; rubric rho 0.745; executed labels cost 100+ hours per idea (K29).

Partly closed
- Gap 1 (scaffold vs fine-tuned judges): d01 gives the first prompt-only (frozen) selector with a measured gain (0.684 to 0.711 and 0.729). Still no equal-token comparison with fine-tuned judges such as Wen or Tong (K23). Stays open on the comparison.
- Gap 3 (novelty-check cost curve): d04 shows given related works do not rescue scalar scores (F1 17.2), d06 shows retrieval adds about +0.03 on a trained judge. OpenNovelty (d05) has no ablation. No cost curve exists. Open.
- Gap 4 (outside NLP): d07 adds product ideas with purchase intent. Nothing found for debugging, engineering, or business problem selection. Partly open (K26).
- Gap 5 (portfolio rule): d11, d12, d18 give qualitative and break-even rules, no budgeted optimum. Partly open (K27).
- Gap 8 (tournament vs single pass): d09 shows Elo tracks GPQA accuracy (top-Elo 78.4%), but Elo is LLM-judged and there is no equal-token best-of-N baseline in the text read; d08 shows frameworks vary from +177 Elo to nothing. Open on equal tokens.

Stayed open
- Gap 7 (BoLeBench): not opened; no budget left for the search. Figures 70.8%, 67.1%, 36.0% remain unverified.
- Gap 10 (replication of Wen): no replication found. Tong et al. is a related but different test (d03, d16). WebSearch ran out before a targeted search, so the absence is weak evidence.

New cautions found
- d03 Tong et al. out-of-domain table is garbled in text extraction; only prose numbers were used.
- d06 the 0.73 vs 0.76 metric label was not confirmed.
- d12, d13, d14 are carried-over or summary-only lines (opened:false).
- Some 2026 sources use model names (GPT-5.1, Claude 4.5, Opus 4.8) not in the earlier evidence; the cutoff dates differ from the 2024-era studies, so results across d01 to d09 and a01 to c27 are not on the same model generation.
