# E07.07 Bio-inspired and analogical design: cross-check critique

Checked by re-opening the source text for 10 key numbers. Scratch texts are in D:/research_scratch/E07.07/.

## Numbers re-checked

| Evidence | Source re-opened | Result |
|---|---|---|
| a05/a06 | Goel & Hancock 2021 | Confirmed: 36/74 multifunctional (48.6%), 27/74 solution-based (36.5%), kappa 0.88 (94%), 22/27 (81.5%) vs 14/47 (29.8%), fixation 19/27 (70.4%) vs 31/47 (66%), 50 total. |
| a18/a19 | Dekel et al. 2021 | Confirmed: higher-order 5/42 (11.9%), chi2(1,N=64)=7.107, p=.008, phi=.33. |
| b11/b12 | Hope et al. 2017 (arXiv 1706.05585) | Confirmed: purpose-only 0.739 at top 1%; pr(Good)=0.71 vs 0.28 vs 0.27 (k=2), 749 ideas, 249 good; k=3 0.56 vs 0.16. |
| c13/c14 | Puranam et al. 2025 | Confirmed: factory 4/46 (8.7%) vs 6.3%; HR 17/46 (37%) vs 20.3%; GPT-4 radiation precision/recall 0.00. |
| c30 | AnaloBench (EMNLP 2024) | Table confirmed: GPT-4 89.1/66.5/60.7, human 96.0/72.5/73.3, Claude 68.2/30.2/25.9. CORRECTION below. |
| c28 | Kulikowski 2026 | Confirmed: AP 0.222 to 0.513, whole fingerprint 0.557, judges 8 of top 30 vs 0 of 30. |
| c29 | Cross-Pollination Retrieval | Confirmed: best of eleven 0.26 Recall@10; LLM reranker 0.81; row for fine-tuned 4B in table is garbled but abstract says 0.70. |
| c07 | Emuna et al. 2023 | Confirmed: 72% vs 36% at top 7, 69% vs 29% at top 15 (as in c07 text; p=2.26e-7, 2e-10). |
| c16/b23 | Yasunaga et al. 2024 | Table 1 confirmed GPT-3.5 75.0 vs 75.8-77.8 and MATH 33.0 vs 33.9-37.3. CORRECTION below. |
| b01-b05 | Chan et al. 2011 | NOT re-opened this pass (the local text file was not found); the d values stay as recorded by agent b. |

## Corrections

1. c30 / AnaloBench gap. The paper's abstract and intro say the human-GPT-4 gap is 28.8 points on 30-sentence stories. Its own Table 2 gives human 73.3 vs GPT-4 60.7, a gap of 12.6. 6.9 at one sentence is right (96.0-89.1). The 28.8 figure may refer to a different pair or setting. Use the table; do not quote 28.8. Human 30-sentence value rests on only 30 annotated items (1- and 10-sentence on 50).
2. The appendix table of AnaloBench has shifted rows (GPT3.5 row shows Tulu numbers 71.8/51.2/31.5). The main-text Table 2 is the trustworthy one.
3. b23 vs c16 (Yasunaga). b23 says text-davinci-003 fixed 5-shot is about 50% and retrieved 54%. Table 1 shows 5-shot CoT at 14.8% for text-davinci-003, with self-generated 50.3-61.0%. The 14.8% sits in a table whose row labels are partly missing in the text layer, so which baseline it is stays unclear. Either way the large gain is for an old weak model; for GPT-3.5-turbo the gain is 0.8 to 2.8 points on GSM8K. Treat "+4% average" as driven by weak models.
4. b21: human and model accuracy assignments were "inferred" from a shifted table. Do not cite 0.753 / 0.488 / 0.350 / 0.452 by model until re-read.
5. Hope et al. (b11) top-1% precision is the single best cell; at top 25% the gap shrinks (0.478 vs 0.399). Recall at top 1% is about 0.02. The headline overstates a narrow region of the curve.

## Contradictions between sources

- Fixation: Helms 2008 (a03) saw fixation concentrated in solution-driven teams; Goel and Hancock 2021 (a06) found no association over 74 cases. The earlier claim is not supported at scale. Coding of "fixation" is by two coders on written reports, a soft measure.
- Far analogies: Chan 2011 (b01) found no novelty gain for far alone; Goucher-Lambert 2020 (b07) found no novelty change from mid-session stimuli. Hope 2017 and later retrieval work push distant analogy as the goal. Human lab evidence for a far-analogy benefit is thin and conditional.
- LLM analogy ability: Webb 2023 (b20) says emergent; Lewis and Mitchell 2024 (b21) say brittle under counterfactuals; Webb 2024 (b22) says GPT-4 with code is on par. Both can be true: depends on tool use and task alteration.
- LLM retrieval: Webb-style tasks hand the model both items; AnaloBench T2 (c31) and StoryAnalogy (b17) show retrieval is near chance. Puranam (c14) shows the same: mapping fine after a hint, no spontaneous retrieval.

## Weak spots

- Founding human studies are classroom observational work from one institution (Georgia Tech, 2006-2013). No control group. Coding of "multifunctional" and "fixation" by two coders; kappa 0.88 is for the first assessment only.
- Most human design-by-analogy experiments (Chan, Goucher-Lambert) are single-lab, single-problem (energy harvesting), expert-rated novelty.
- LLM design studies (Zhu, Ma, Ding) use small rater panels (9 usable surveys in Zhu; 3 participants in Kang interview) and often LLM judges. Cross-Pollination, Idea-Catalyst, Kulikowski are 2026 preprints without peer review.
- Few studies measure tokens or cost. No study compared analogy retrieval to plain resampling at equal tokens. The best candidate to test on our agent.
- Companion structure-mapping, case-based and blending subfields are researched in parallel; links only.

## Only seen in snippets or abstracts

a14 (Vattam 2010), a20-a25 (Chan abstract only in a20; Fu 2013, Linsey 2012, Christensen and Schunn 2007, MAC/FAC, ARCS originals), a26, b10, c34. Sample sizes and effect sizes for Fu 2013 (near/far "sweet spot"), Linsey WordTree and Christensen and Schunn are missing. These are decision-relevant human baselines.

## GAPS

1. At equal tokens, does an explicit analogy-retrieval step (abstract the problem, retrieve, rerank, map) beat plain best-of-N resampling on reasoning and design tasks for a strong current model? No paper tests this directly.
2. Which representation should memory use for retrieval: domain-stripped function skeleton, purpose-only text, or full text with LLM rerank? Compare directly on one shared analogue bank with recall and cost (Hope 2017, Kulikowski 2026, Cross-Pollination 2026 used different data).
3. What are the numbers in Fu et al. 2013 (near/far sweet spot), Linsey et al. 2012 and Christensen and Schunn 2007? Open full texts and record N, effects, and the distance at which benefit peaks.
4. Does the human fixation finding in bio-inspired design (source-locked ideas) appear in LLM agents, and does a "second, different source" step reduce it? Measure same-source repeats.
5. How does retrieval quality in current frontier models (2026) compare on AnaloBench T2 and StoryAnalogy? Existing numbers use GPT-4, Claude-v2 and older models; the 28.8-point gap claim needs a clean rerun.
6. Does the Yasunaga self-generated-exemplar gain survive for current strong models (GSM8K already above 90%) and on non-math tasks? Reported gains are mostly for weaker models.
7. Is there a measured human benefit from domain experts (biologist on team) vs engineers alone beyond Farzaneh 2020 (N=20 pairs)? Replication needed; relevant to whether the agent needs a "domain-expert sub-role" (O7 plus roles).
8. How often do LLM-generated bio-inspired concepts survive feasibility checks when judged blind by experts (Zhu 2022 used 9 raters)? Need a larger blind rating with failure reasons.
9. Do compound analogies (several sources, 6/9 and 4/10 in human teams) help or hurt LLM design quality relative to a single best source at equal tokens?
10. What triggers spontaneous analogy use? Puranam found 1/15 unprompted use for GPT-4; test cheap trigger prompts versus a forced "list analogous problems" step and measure false-positive cost.

## Gap search results

Searches: WebSearch quota ran out early. Work continued with direct arXiv PDF/HTML fetches and Semantic Scholar forward-citation lists (AnaloBench, Yasunaga, Qin, Zhu). New evidence is in `evidence_d.jsonl` (d01 to d17, 16 opened). Claims K26 to K32 were added; K08, K09, K13, K14, K15, K18, K20, K21 were updated; K18 is now "contested".

**Closed or partly closed**
- Gap 5 (28.8 vs 12.6): CLOSED. Re-reading AnaloBench v2 shows the text says 28.8 but Tables 2 and 7 give 73.3 - 60.7 = 12.6 (d03). The T1 rows are now confirmed. Its Table 4 (true-positive subset) gives GPT-4 22.7 at 30 sentences, so do not quote that subset (d05). The 2026 frontier-model rerun is NOT closed: no paper found reports T2 or StoryAnalogy for 2025-2026 models (d04).
- Gap 6 (Yasunaga for strong models): PARTLY CLOSED, and the answer is mostly negative. Decoded tables show +1.1 over the best baseline for GPT-3.5 on GSM8K, and the 14.8% row is plain 0-shot (d06). Qin 2024: irrelevant examples beat relevant ones on math (71.5 vs 75.5) (d01). Gwak 2026: gain is a within-prompt process effect, about +5 to +9 without CoT on GPT-4.1/4o, about +1 with CoT (d07). Still unknown: reasoning models, and non-math tasks.
- Gap 2 (representation comparison): PARTLY CLOSED. Cross-Pollination shows a rerank over a wide pool beats all embeddings and HyDE (0.81 vs 0.26 vs 0.44), and RATIO shows first-stage recall in the top 100 caps the rerank (d08, d09). Not done: skeleton vs purpose-only vs full-text on one bank.
- Gap 1 (explicit analogy vs resampling): HALF CLOSED. Shen et al. 2026 compare analogy against a 1-call and a 2-call prompt on three frontier models with big diversity and novelty gains (d12). There is no best-of-N arm and no accuracy or feasibility score, so the question stays open for reasoning tasks.
- Gap 4 (LLM source-locking): PARTLY CLOSED. LLMs do show source-domain homogeneity (d11, d12) and design fixation in text (d15). The effect of a forced second, different source on same-source repeats is untested.
- Gap 8 (feasibility pass rate): STILL OPEN. Zhu 2022 had about 6 generated concepts rated by 9 people (d13). BioSpark gives a feasibility drop of 1.1 points on a 10-point scale next to the novelty gain (d14), not a pass rate.
- Chan 2011: effect sizes re-checked against the full text and confirmed (d02). One flag: Table 1 cell counts sum to 151, not the 153 used in K08.

**Still open**
- Gap 3: Fu 2013, Linsey 2012 and Christensen and Schunn 2007 full texts were not obtainable (Pitt PDF URL returns an error page, Springer paywalled). No sweet-spot distance can be cited (d16, d17).
- Gap 7 (mixed expertise beyond Farzaneh 2020), gap 9 (compound analogies for LLMs), gap 10 (trigger prompts and false-positive cost): no new study found; I could not search for them after the quota ran out. These need our own runs.

**What this means for the agent**
Treat explicit analogy as a diversity and novelty tool, not an accuracy tool. Add a feasibility critic, a source ledger that forces a second different source, and a wide first stage with an LLM rerank. Do not turn on "recall similar problems" by default for math; A/B test it.
