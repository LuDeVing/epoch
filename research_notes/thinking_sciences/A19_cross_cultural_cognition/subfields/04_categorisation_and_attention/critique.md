# A19.04 Categorisation and attention: cross-check critique

Checked 2026-11-19. Sources re-opened this session (text extracted from PDF or XML): Hu et al. 2026 (arXiv 2601.17096), Jin et al. 2023 (2308.14242), Sun and Wang 2025 (2510.05869), Sabir et al. 2025 (2507.00700), Many Labs 2 (Klein 2018), Norenzayan et al. 2002, Masuda and Nisbett 2006, Chua et al. 2005, Klein et al. 2009, Lacko et al. eye-movement paper (PMC12326012).

## Numbers confirmed (10 checked)
1. Hu Task 4 triads: US model 8.10 (SD 1.44) vs Chinese 6.04 (SD 1.54), t=-13.81, d=1.38. Confirmed. Language 7.10 vs 7.04 confirmed in earlier read.
2. Hu Task 1 images: DALL-E 3 11.53 objects (SD 4.39) vs iRAG 8.10 (SD 1.91), d=1.01. Confirmed.
3. Jin 2023: AHS GPT-3.5 5.35 (0.11), GPT-4 5.01 (0.10) vs norm 4.87 (0.49, N=702); TCT 0.87 and 0.85; SCS-Ind 6.98 vs 4.73. Confirmed.
4. Sun and Wang: overall language d=0.045, p=.1501; 3 of 8 models significant in Exp 2 (ernie d=-0.171, qwen 0.540, gpt -0.190). Confirmed (but see corrections).
5. Sabir: 26.10% (COCO 1K) and 73.37% (1K Japanese) for GPT4o-JP 6-shot balanced; 13.21% translation shift. Confirmed.
6. Many Labs 2: N=7,396, 64% vs 44%, t=37.05, d=0.86 [0.81, 0.91]. Confirmed. Original d: European Americans 0.00, East Asians 0.67. Confirmed.
7. Norenzayan 2002 Study 2: belong-to 67% vs 33%, F(1,100)=44.40; similar-to East Asians 41% vs 59%, European Americans 69% vs 31%. Confirmed.
8. Masuda and Nisbett 2006: F(1,64)=3.96; F(1,35)=9.44; F(1,58)=22.72; F(1,58)=128.62. Confirmed.
9. Chua 2005: 118 ms sooner, t(43)=2.41; F(1,43)=4.43 and 9.50. Confirmed.
10. Klein 2009: F(3,181)=2.01 ns; t(89)=4.71; F(3,375)=16.92 and 18.26. Confirmed. Seven-sample eye-tracking study: F(6,401)=12.77, Ghana 1895 ms, Taiwan 1528 ms, Germany 1533 ms, Ghana g=1.95, Taiwan g=0.44. Confirmed.

## Corrections made
- c09 (Hu image probe) mixed two tasks. English 10.91 vs Chinese 10.07 objects is Task 2 (scene interpretation or description), not image generation. Task 1 generation: Chinese prompts 10.71 vs English 8.91 objects. The paper itself prints 10.90 and 10.06 in the results and 10.91 and 10.07 in the discussion (rounding). Claim K15 uses the results-section values.
- c09 left out that the US image model also placed horizons higher (533.47 vs 519.79, d=0.34).
- c04 joined two experiments. The overall language result (mean diff 0.0053, p=.1501, d=0.045) is Experiment 1. The "3 of 8 models" result (ernie, qwen, gpt) is Experiment 2. In Experiment 1 the significant models were deepseek and qwen (both preferred Chinese). Fixed in K13.
- a22 and c05 say framing had a "small" effect (copied from the summary table). The appendix reports change-framed vs neutral d=-2.095 and eta-squared 0.54, the largest effect by far. The paper contradicts itself; the appendix numbers are the data. See K14.
- b06 put "median d 0.60 originals vs 0.15 replications in WEIRD samples" under the Norenzayan effect. That median is across all 28 ML2 effects, not this effect.
- c10 and a25: the 26.10% and 73.37% are on different datasets with the same model, so they are a content effect plus a model effect. In the same table plain GPT-4o gets 57.6 to 59.1% on the Japanese set, so a Japanese-tuned model adds about 14 points; most of the gap is image content.

## Contradictions between sources
- Rule vs resemblance by culture: Norenzayan 2002 reports a culture gap in the similar-to condition (n=18 per cell); Many Labs 2 reproduces only the instruction effect and finds the culture moderation inverted; Klein 2009 finds no culture effect in rule choices and only a response-time difference.
- Eye tracking: Chua 2005 supports earlier object fixation for Americans; Rayner and colleagues (snippet only) do not; the 2025 seven-sample study shows Taiwan has the smallest focal-background gap (g=0.44) but Germany (1.32) sits next to it, so the East-West order is only partly there.
- LLM triads: Jin calls a high relational share "holistic"; Hu finds the US model more relational than the Chinese one. Different items and scoring.
- Language effect in LLMs: Lu et al. (Nature Human Behaviour 2025) say Chinese prompts make GPT and ERNIE more holistic; Sun and Wang and Hu find none or reversed. Lu et al. was never opened, so its numbers are second-hand.

## Weak spots
- The founding numbers (Chiu 1972, Ji and Nisbett 2000, Norenzayan 2002 Study 2 groups of 18) come from small student samples, and several were read only through the 2001 review (no counts: a02, a04, a05, a06, a07, a08).
- a17 (Rayner), b07 (Many Labs 2 reanalysis), c15 (Atari et al.), b22 and c06 (Lu et al.) were seen only in snippets or secondary summaries. b10 and the Jin and Hu human benchmarks were not independently checked.
- Many LLM results rest on two models per side (GPT-4o vs ERNIE) with temperature 1 (Hu), temperature 0 (Sun and Wang) or 10 runs (Jin). Temperature 0 removes variance. A "Chinese model" that is also RLHF-tuned confounds culture with alignment.
- Items in Jin are 20 triads from human work, likely seen in training. Contamination is untested.
- Nothing here measures whether a holistic or analytic style helps an agent solve problems. Relevance to the schema is background only; the one transferable result is that wording and framing move outputs more than culture or language cues do.

## Not seen in full text
Rayner et al. 2007 and 2009; Schimmelpfennig et al. 2024; Lacko et al. 2025 (abstract level); Lu et al. 2025; Atari et al. 2023; Tao et al. 2024 and Ananthram et al. 2024 beyond abstracts and cached text.

## GAPS
1. Does re-wording the same task ("belongs to" vs "similar to", change-framed vs neutral) shift our agent's answers more than any scaffold step at equal tokens? (Decides whether a wording control belongs in G7 tests.)
2. Is the high relational triad share in LLMs stable across scoring rules and fresh (unseen) triads, or an artefact of memorised items?
3. Does an LLM prompted with "attend to context first" vs "focus on the main object" change accuracy on change-detection or distractor-heavy reasoning problems at equal tokens?
4. Do persona or language prompts change anything on a fixed set at temperature 0 and 1 for the models we actually use (replicate Sun and Wang on our model)?
5. What did Rayner et al. 2007 and 2009 find numerically, and how large is the Chua effect once corrected for sample size?
6. Do LLMs show the child-style thematic-to-taxonomic shift when given age-labelled triads (no study found)?
7. Is the Lu et al. 2025 language effect real for any model (needs the full text and items)?
8. Does categorisation by relation (thematic cue) vs by taxonomy help analogue retrieval (O7) on our tasks?
9. How much of the Sabir VLM caption gap is image content vs output language (needs a crossed design)?

## Gap search results (2026-11-20)
Sources opened this session: Rayner et al. 2007 and 2009 (PMC full text), Goh et al. 2009, Kelly 2011, Gingras 2023, Sabir et al. Tables 2 to 6, Jin 2023 and Hu 2026 (methods), Sun and Wang appendix, Sclar 2023, Cao 2024, Shi 2023 (GSM-IC), Gentner, Rattermann and Forbus 1993. Evidence is in evidence_d.jsonl (d01 to d19).

- Gap 1 (wording vs scaffold at equal tokens): PARTLY CLOSED from literature. Wording and format noise is large (median 7.5 points, up to 76; Sclar) so a wording control with paraphrase spread belongs in G7 tests. No run on our agent; that needs an experiment. See K22.
- Gap 2 (triad stability, unseen items): OPEN. Found that Jin's 20-item test had only 10 real items and Hu uses the textbook Seagull-Sky-Dog example; no fresh-item study exists. Scoring differs between the two studies (relational share vs R-C score).
- Gap 3 (context-first vs focus-first on distractor tasks): PARTLY CLOSED. Closest data: GSM-IC, "ignore irrelevant information" gives +5.4 (CoT) and +3.1 (least-to-most) points on a 2023 model. The context-first direction was never tested. Needs our own run. See K23.
- Gap 4 (replicate Sun and Wang on our model): OPEN. Needs an experiment on our models; not answerable from literature. Sun and Wang's temperature-0 design removes variance; run temperature 0 and 1.
- Gap 5 (Rayner and Chua effect size): CLOSED. Rayner 2007: N=74, no group effect over all scenes (background 2489 vs 2565 ms, F<1), partial effect only on 6 Chua-like scenes (foreground 4299 vs 4813 ms, p=.04). Rayner 2009: N=24, all F<1. Chua's effect is about g=0.72 (95% CI 0.12 to 1.33); Goh 2009 finds large effects in dwell and dispersion (N=31). Verdict: small to moderate, scene-dependent. See K05.
- Gap 6 (child-style triads on LLMs): OPEN, no study found after another search. Weak evidence of absence.
- Gap 7 (Lu et al. 2025 full text): OPEN. Full text paywalled; abstract only. Critique details (4 to 12 items, 2 models, unreleased items) recorded in K25.
- Gap 8 (thematic cue vs taxonomy for analogue retrieval): PARTLY CLOSED. Human data (Gentner 1993) show surface similarity drives retrieval and relations drive soundness; LLM evidence is secondhand snippets only. Needs a test on O7. See K24.
- Gap 9 (Sabir image content vs output language): CLOSED enough. Content is the larger factor (+47 points COCO to Japanese images) and language the smaller (+11 to +15 points on the same COCO images); the judge also inflates holistic share vs humans (29.00 vs 17.75). See K16.

Corrections to earlier claims: K05 now cites four eye-tracking studies and an effect size; K16 now states the content-vs-language split (single paper, stays single-source).
