# Critique: F01.03 Blend network types (cross-check)

## Numbers re-opened this session (PDF text, D:/research_scratch/F01.03)
Confirmed exactly: Kombine (2509.21043): 43.4/53.4/59.0%, 97.1% given valid generic space, 22.1/32.9/12.8% humans, 2,070 concepts, 7,868 properties, 0.674, 1 in 5 (412/2,070 = 19.9%), human-judge agreement 75% (n=96); gpt-5.6-sol blending 64.8 vs analogy 55.4 (composite, Table 7; model name is as printed). PopBlends (2111.04920): 56.0/55.3/58.7, 90.0/96.6/93.3, 89.1/75.9, 98.3, 2.03 vs 0.87, mental demand 2.85 vs 5.80 (p=0.004), effort p=0.006. Peng 2025 (2504.13120): 78.3/73.5/62.9/51.0, 0.26 to 0.35, 85.1/81.6% agreement. Xu 2026 (2602.01335): ablation rows and 64.44/67.11/72.89/76.22%. Matsuhira (2411.03595): BCD 0.621, MCD 0.862, aggregate 0.389/0.471. Misty (2409.13900): 103 operations, 36/35/19/9/4 split, 3.2 (median 3, SD 1.3), 5 of 14 (35%) agreeing. Olearo (2506.23630): 100 participants, 51%. Coulson and Van Petten 2002: F(2,34)=3.90, 6.86, 98%, 40%, 2.03, 2.18. Coulson and Matlock 2001: 0.84/0.81/0.78, F(2,68)=5.48, t=3.26.

## Corrections and flags
1. Peng 2025 fusion vs replacement (b15 vs c07): the text says fusion is more precise in 9 models; the Figure 5 caption says replacement is higher. c07 repeated the text claim, also "humans show the same pattern", without noting the contradiction. Status set to contested (K10).
2. Xu 2026: the "16.8% increase" is on the "AA" metric (the paper's own label); b23 left it as AA, c09 called it analogy appropriateness. Not verified which. Do not quote as "analogy appropriateness" without opening the metric definition.
3. Xu 2026: Task 1 table shows Metaphor Ingenuity 4.61 while the user-study ablation shows 4.56 for the full system. Different evaluations; do not mix.
4. Misty (a21 gave no N, c17 and b20 gave 14): N=14 confirmed. a21 and b20 both cite 103 operations.
5. Kombine's single-scope/double-scope scale (a14) is a new metric, not the 2002 typology; Kombine counts single-scope as both inputs contributing. Keep this out of any claim that LLMs were tested on the typology.
6. Ge and Parikh (2021) precision table is garbled; model-to-number mapping unrecoverable (a18, b11, c04). "ConceptNet 37.33" in c04 is wrong: 37.33 is the BERT-large row. Do not use ConceptNet numbers. Not re-opened.
7. Coulson-Van Petten: "metaphor vs literal F=6.86" and "linear trend F=6.86" are the same number in the paper; not a copy error.

## Contradictions and weak spots
- The typology definitions come only from Wikipedia and Turner's pages. Fauconnier and Turner 1998 and 2002 were never read (a02, b09, b10, a23 all opened:false). Every "established" statement about types is therefore secondary.
- Rival theories explain the N400 gradient equally (b07), so ERP support for blending is non-discriminating.
- Image-domain evidence (Peng, Xu, Olearo, Matsuhira) is the strongest on scaffold effect, but authors designed the metrics and baselines got a plain prompt (scaffold plus extra calls confounded).
- No text-only, reasoning-task test exists for any blend scaffold.
- LLM judges: Kombine (3-LLM panel), Peng (GPT-4o judging GPT-4o), Hernandez (GPT-4). Self-preference risk.
- Only seen in snippets or abstract: Cappa/Lippolis 2025 (no results), Cho 2025 IT-Blender (qualitative only), Hernandez 2024 (85% figure unverified), Olearo 2024, Jonczyk 2020 and Miller 2025 (via PMC, sample sizes not extracted). Not opened: Gibbs, Ritchie, Eppe 2018, Veale 2000, Lieto, Cunha 2020, Sun 2025, Hicke 2024, Dreyfus 2014, ACL 2026 Xi et al. poster.
- Search coverage: WebSearch budget exhausted; Semantic Scholar and OpenAlex returned 429. "No study varies network type" rests on arXiv and Europe PMC keyword search only.

## GAPS
1. Does any ACL/EMNLP/CogSci 2025-2026 paper (e.g. Xi, Cheng, Soni, Turner, "Evaluating Creative Generative AI with Conceptual Blending") label LLM outputs by network type and report scores? Open the PDF.
2. What do Fauconnier and Turner (2002, ch. on network types; Turner 1998 "Figure") say exactly about simplex, mirror, single-scope and double-scope, with their worked examples and any claims about which suits novelty?
3. Does a text-only reasoning or creativity benchmark show gain from forcing "how the inputs combine" before the answer (the IEI result outside images)? E.g. analogical prompting, divergent-thinking tasks at equal tokens.
4. In Peng et al. 2025, which direction is correct for fusion vs replacement (check the figure data and appendix)?
5. Does a code-side check of the generic space (the Kombine bottleneck) raise valid-blend rate, and has anyone tested a verify-shared-slot gate for LLMs?
6. Is there any human study that classifies real creative products or inventions by network type and measures novelty or quality (Turner 2014, Dreyfus 2014, physics education work)?
7. What are the exact Kombine results by blend quality Q (1/2/3), i.e. what share of LLM blends reach double-scope-emergent, and how does that vary with temperature and model size?
8. Do the Lieto et al. and Eppe et al. (COINVENT) computational systems report evaluation numbers that could serve as a code-side blend-ranking baseline?
9. How does Hernandez et al. (2024) measure novelty gain from "alien" pairs, and is there a text-domain equivalent?

## Gap search results (evidence_d.jsonl, d01-d16)
Closed:
- Gap 1 (Xi et al. ACL 2026): closed, negative. Opened the poster. It proposes a FrameNet-based rubric (completeness, clarity, relevance, understanding depth, coherence, execution time) and reports no scores. It does not label outputs by network type (d01).
- Gap 2 (primary F&T text): closed for definitions. Fauconnier and Turner 2003 gives the four types and calls them prototypes on a continuum (d04, d05). The 1998 paper has none of the four names; it uses frame, one-sided and two-sided networks (d02, d03). The 2002 book chapter itself was not opened. On novelty: two-sided/double-scope gives more chance of non-optimal blends and also the opportunity for creativity; complex numbers is the worked case. No test.
- Gap 4 (Peng fusion vs replacement): closed. Rendered Figure 5 and read the bars: fusion higher in 9 of 11 models and for average people; the caption is the error (d06). K10 is no longer contested.
- Gap 5 (code-side shared-slot gate): closed, negative. No paper tests one. Kombine's judge prompt already separates shared-slot (uv) from concatenation, so the gate is easy to build (d09).
- Gap 8 (Lieto, Eppe): closed. Eppe 2018 says it has no empirical evaluation and gives a score formula; Lieto and Pozzato give worked examples only (d14, d15). No baseline numbers exist.
- Gap 9 (Hernandez 2024): closed. Method and numbers extracted (d07). A text-domain equivalent is plausible but untested.

Partly closed:
- Gap 3 (text-only gain from forcing "how the inputs combine"): no direct test found. Closest: Dish COVER, where code does the blend and novelty rose at about equal value (d10, d11); analogical prompting, +4% average (d12); Synectics distance types (d13). None varies a blend-combination field in a reasoning task. Searches were limited (arXiv API returned 429; two WebSearch calls).
- Gap 7 (Kombine Q split): the Q=1/2/3 shares are not published. Per-model integration scores (76.7 top, 3.3 phi-4, humans 1.3 percent of max), one temperature (0.9), N=75 humans (d08). Temperature and size effects cannot be read from the paper.

Still open:
- Gap 6 (human study coding real products by network type): none found. Birdsell 2019 is qualitative (d16). Turner 2014, Dreyfus 2014 and physics-education work were not opened.

New flags:
- Kombine's scale differs from the 2003 typology (single-scope there means both inputs contribute). Do not cite it as a test of F&T types (already flag 5; now confirmed against the primary text).
- Peng Figure 5 values were read by eye; no significance test reported.
- Model names in Kombine are as printed in the paper.
