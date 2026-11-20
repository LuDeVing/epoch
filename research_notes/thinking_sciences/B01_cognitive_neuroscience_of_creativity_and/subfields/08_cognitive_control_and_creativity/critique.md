# Critique: B01.08 Cognitive control and creativity

## Corrections made (cross-check, this session)
- Peeperkorn et al. 2024 (arXiv 2405.00492): a16 says "5 per temperature, 31 stories"; c17 says "100 stories each, 36 raters". Both are right but for different parts. 100 stories per temperature were generated for the diversity analysis. For human rating, 5 stories per temperature (31 in total, since t = .001 gave only one extra unique story) were rated by 36 participants, 5 stories each. Use "31 rated stories, 36 raters" for novelty and coherence slopes. c17 should not be read as 100 rated stories per temperature.
- Gong et al. 2023 (OpenAlex abstract): r = .083, 95% CI .050-.115, n = 3104, k = 28 confirmed. b08 (525 correlations, 79 studies) is a different, larger meta-analysis seen only in a snippet; do not mix the two.
- Schapiro et al. 2026 (arXiv 2607.01433 abstract): "up to 14 human percentile points" and "N=720" confirmed. Detailed mode-collapse numbers (a21/c21) were not re-opened.
- Rosen 2016 interaction p: a11 gives p = .043 (chi2(4) = 9.84, model comparison) and b03 gives p = .002 (estimate -0.24). These are two different tests in the same paper (omnibus vs fitted interaction coefficient), not a conflict, but cite which one.
- Duplicate lines: a20/c20 and a21/c21 (Schapiro), a18/c14 (Bellemare-Pepin), a05/c26 (Beaty 2015), a22/c25 (Mondal/Webb planner), a01/b01/c27 (matched filter). Counted as one source each in claims.
- Top-10 numbers not re-opened (prior agents marked opened:true): Beaty 2015 r = .44, Benedek 2012 N = 104, Zhang 2016, Pena 2022, de Langis 2025, Ismayilzada 2026 r = .55, the WCST-vision paper. Treat as agent-read, not cross-verified, except where listed above.
- Semantic Scholar rate-limited (429); arXiv title search for de Langis, Ismayilzada and Patel returned nothing, so those could not be re-opened.

## Contradictions between sources
- Control helps vs control hurts: Benedek 2012 and the 2026 flanker study link inhibition to flexibility and originality; the matched-filter and tDCS studies say reduced left-PFC control helps. The Rosen expertise interaction suggests both can be true by skill level.
- tDCS direction: Khalil 2020 (cathodal left + anodal right helps originality); Rosen 2016 (anodal right DLPFC helps novices); Pena 2022 (tRNS helped picture completion, tDCS did not help unusual uses, had more side effects). The 2024 tDCS meta-analysis (snippet) says left DLPFC anodal helps, which sits uneasily with the inhibitory-left idea.
- WCST in LLMs: de Langis 2025 says reasoning models did not beat baselines on WCST; the vision-WCST paper says CoT text gets near 1.0. Differences are prompt format and rule exclusivity.
- "Trade-off" vs "co-operation": Beaty 2015 and the ALE meta-analysis show DMN plus executive coupling, so a simple see-saw is not supported.

## Weak spots
- The core theory (Chrysikou matched filter, Dietrich 2003) is read only as review or abstract (a01, a03 opened:false). No primary exact numbers for Chrysikou 2011 (N = 24 only).
- Most human numbers come from small samples (N = 17 to 104); p-values near .04 to .06 are common. tDCS results lack pre-registration in most cases.
- LLM "executive function" tasks are not shown to predict creative output in LLMs. No study found that manipulates a control-like variable in an LLM and measures creativity at equal tokens.
- Brain-alignment results (Ismayilzada) are correlational and across model size, so size confounds.
- Mode-collapse and DAT results use open 3B-14B models and one weight-steering method (single source).

## Only seen in snippets
b08 (WM meta, 79 studies), b09 (tDCS meta, 32 studies), a01/a03/a04/a09 abstracts only, c16 (Chen & Ding 2023, abstract), c11 and c12 not read.

## GAPS
1. Is there any LLM study that varies constraint tightness (strict versus relaxed instructions, or a separate generate-then-evaluate stage) and measures creativity and correctness at equal tokens? This is the direct test of O4.
2. What are the exact effect sizes in the 2023 WM-creativity meta-analysis (79 studies) and the 2024 tDCS meta-analysis (32 studies), and do they survive publication-bias correction?
3. Does the Rosen expertise interaction (novices gain, experts lose) replicate in any other domain or sample? If so, should relaxation depend on agent familiarity with the task?
4. Does the matched-filter hypothesis have a preregistered replication of Chrysikou 2011 or the 2013 tDCS study?
5. Do LLM scores on executive-function tasks (WCST, Flanker, Stroop) correlate with their DAT/AUT originality across models?
6. Does chain-of-thought or reasoning-mode training reduce LLM originality (more control, less diversity)? Any measured results 2025-2026?
7. Do evaluation-after-generation splits (Zhang 2016 view: generation bottom-up, evaluation top-down) improve LLM creative output compared with single-pass at equal tokens?
8. What do the CreativityNeuro and activation-steering results replicate on larger or closed models, and what is the cost on correctness tasks beyond MMLU?
9. Is there evidence that distractibility or "leaky attention" (Zabelina) gives better creativity in LLMs when context contains irrelevant material?

## Gap search results (gap searcher, 2026-11-20)
Evidence is in evidence_d.jsonl (d01 to d18). Claims K01, K02, K05, K06, K09, K11 updated; K15 to K19 added.

1. Gap 1 (constraint tightness at equal tokens): PARTLY CLOSED. No equal-token study exists. Two close tests: ReDNA (d02), where a goal-free diverge call then a constrained select call lifted AUT originality 2.91 to 3.77 and path success 48.2% to 67.9% on GPT-5.4; and Recipes for Creativity (d01), where more search iterations gave no creativity gain and the selector design mattered. Both use extra calls. Open: an equal-token rerun.
2. Gap 2 (meta-analysis numbers, publication bias): MOSTLY CLOSED. The 79-study meta-analysis is Gerver 2023 on memory in general (d03): r = .19, working memory r = .17, Egger p = .76, unchanged without unpublished data. It is not a pure WM-creativity paper; the Gong 2023 r = .083 stays the WM-specific figure. The 32-study tDCS paper (Chen 2024, d04) was only seen as an abstract: no g values or bias test. The 2025 preprint (d05) gives d = .54 and .40 for left frontal anodal with only a visual funnel check. Open: Chen 2024 effect sizes and bias tests.
3. Gap 3 (Rosen expertise interaction): STAYS OPEN. No replication in two searches (d07). Khalil 2023 (d08) shows trait moderation, not expertise. Do not make relaxation depend on agent familiarity yet.
4. Gap 4 (preregistered matched-filter replication): STAYS OPEN. Only the same lab's 2021 extension (d06, 246 participants) reproduced the fluency gain, not originality (d18).
5. Gap 5 (EF scores versus originality across LLMs): STAYS OPEN. No such study found (d16); CreativityPrism (d15) shows creativity skills do not transfer across dimensions.
6. Gap 6 (reasoning mode and originality): MOSTLY CLOSED, direction negative for trained reasoning. Thinking variants widen the uncertainty gap in 28 LLMs (d11). Think-SFT loses 62% of base diversity; no-CoT at inference does not restore it (d10). But prompted CoT reduced fixation (d12). Mechanism paper d09 is theory.
7. Gap 7 (evaluation-after-generation versus single pass at equal tokens): PARTLY CLOSED. Same evidence as gap 1; no equal-token test.
8. Gap 8 (CreativityNeuro on larger or closed models; correctness cost): STAYS OPEN. Still six open models, 3B to 14B; MMLU -3.13 pp, and MMLU-protected masks lost a further 0.71 pp (d17).
9. Gap 9 (distractibility in LLMs): PARTLY CLOSED. Random context raised judged novelty and unrelated context raised category spread (d13); metric-specific, LLM-judged, no correctness check. No test of leaky attention itself.

Caveats: OpenAlex and Semantic Scholar were rate-limited; Chen 2024 and Rosen 2016 were not read in full. 6 or 7 web searches used.
