# E17.01 Scenario planning (Shell method): cross-check critique

Checked 2026-11-03 by the cross-checker. Evidence files a, b, c (26 + 25 + 26 lines) and claims.jsonl (18 claims, K01-K18).

## Numbers re-opened this session (10 checks)

1. Csaszar, Peterson, Wilde 2026 (arXiv 2602.01684), full PDF text: Gemini 2.5 Pro 0.74, GPT-5 family 0.67-0.71, best human (Expert 3) 0.45, other expert 0.04, Prolific crowd 0.19, 30 projects, 346 Prolific managers plus 3 MBA investors. CONFIRMED.
2. Same paper, gap Gemini minus Expert 3 = 0.29, p = 0.063. CONFIRMED, but the paper itself calls this significant only "at the 90% level". Evidence lines a18/b11 do not say that. CORRECTION: p = 0.063 is not significant at 5%.
3. Same paper, ensembles. a19 is right (best human + Gemini = 0.67; Gemini + GPT-5 Mini = 0.77, +0.03, not significant). b12 is WRONG where it says "Gemini + GPT-5 Mini (0.71) ... combining two strong models helped": 0.71 is GPT-5 Mini alone; the pair gives 0.77. CORRECTION made in claim K08.
4. Same paper, "Prolific captured 85% of oracle value". Confirmed, but it is measured for portfolios of about 5 picks (85% at K = 5 vs Expert 3 at 50%), not overall. b12 states it without this condition.
5. Same paper, replication: 26 projects after 3 removed, 30.8% raised under $100, model-rank correlation across samples about 0.54. CONFIRMED (a20). It is a replication by the same team on a second sample, not independent.
6. Elbaum and Panter 2025 (2508.01056): 6.37 / 3.96 (-38%) / 3.33 (-48%) / planning 4.61 (-28%) / de-escalation 2.76 (-57%). CONFIRMED against paper text.
7. Halawi et al. 2024 (2402.18563): test Brier 0.179 vs crowd 0.149, accuracy 71.5% vs 77.0%, GPT-4-1106 0.208. CONFIRMED. Note the crowd Brier changes with the ablation table (0.146 in Table 5, 0.149 in the main table). The "0.186 vs 0.162" in a/b was not re-checked.
8. Time-R1 (2505.13508): 48.90 vs 48.81 (DeepSeek-V3), 0.7780 vs 0.7503, +171.6%. CONFIRMED. The 0.09-point gap is far below any plausible noise; the paper's wording of "consistent gains" overreaches. Author attribution differs across lines (a21 "Liu et al.", c13 "Zhang et al."); unresolved.
9. XFinBench (2508.15861): scenario planning 246 test / 69 validation, 88.6% calculation, o1-preview 60.1, human 75.8. CONFIRMED in table text. The "88.6%" column alignment in the extraction is fuzzy.
10. Soru and Marshall 2025 (2501.04880): Brier 0.186 vs 0.236 vs 0.150 superforecasters, N=150. CONFIRMED. The paper itself says both "+26%" (abstract) and "+19%" (body) improvement over a baseline; treat percentages with care, use Brier.
11. Polyscene (2610.28102): abstract confirms five of 15 pairs at war, budget 5, three wars by 2026; Table 5 confirms 5/8/9/11 outcomes at budgets 4-7 and 8.4 s. The memory entry "350 GB" is printed in the paper but cannot be real on a 16 GB laptop; a12 correctly doubted it. Treat as a typo in the source.
12. Infinity-Chat / Artificial Hivemind (2510.22954): 26K queries, 31,250 annotations, >0.8 same-prompt similarity, 81% of pairs above 0.7 and 61.2% above 0.8 under min-p, cross-model 71-82%. CONFIRMED.
13. Phadnis 2015 and Schoemaker 1993 abstracts re-read via Crossref. Confirmed wording. No sample sizes or effect sizes exist in abstracts.

## Contradictions between sources

- Confidence: Schoemaker 1993 (lab) says scenarios counter overconfidence by exploiting the conjunction fallacy; Phadnis 2015 (field) says no aggregate effect. Both abstract-only. Not resolved. Healey and Hodgkinson say scenarios can also anchor.
- Aggregation: Halawi and Schoenegger find crowd-plus-model averaging helps; Csaszar finds averaging and human-AI teams never beat the best model. Different tasks (binary questions with a calibrated crowd vs 30-item ranking), so not a true conflict, but it blocks a general rule.
- LLM scenario value: pilots (Picavet, Ferrer i Pico 2025, architecture preprint) report gains; Ferrer i Pico 2026 (Girona) and the Delphi paper report narrow, technology-leaning output. No common measure.

## Weak spots

- The whole Shell-method base (Kahn, Wack, six steps, the 68% in 1983, the de Geus audit) rests on Wikipedia and HBR landing pages. No primary Wack text was read in full.
- No effect size exists anywhere for scenario planning on firm performance. Phelps 2001 (171 citations) and the 2020 "black box" paper were never read.
- Almost all LLM numbers are about forecasting or ranking, not about scenario construction. Only Time-R1 (plausibility by embedding similarity), Girona and Polyscene touch scenarios, and none compare to the Shell funnel.
- Csaszar: N = 30 (26 in replication), one platform, wide intervals; ranking Kickstarter projects is not strategic reframing.
- Elbaum: one 7B model, 10 runs, escalation score is a simulation metric.
- Park et al. (c16/c17) are only loosely related and give believability scores, not scenario quality.
- b-file lines duplicate a/c lines (b11=a18, b12=a19, b13=a10, b18=c08, b19=c11=c20); claim `independent_sources` counts them once.

## Seen only in snippets or abstracts (opened:false or abstract-level)

Schoemaker 1993, Phadnis 2015, Kuhn and Sniezek 1996, Healey and Hodgkinson 2009 and 2024, Meissner and Wulf 2013, Chermack 2006/2007, Phelps 2001, Cordova-Pozo and Rouwette 2023, the 2020 black-box paper, Goodwin and Wright 2001, Hodgkinson and Wright 2002, Ferrer i Pico 2025 and 2026, the architecture preprint, EcoGym, the Picavet pilot page, practitioner pieces (c26). Their numbers are second-hand.

## GAPS (most decision-relevant first)

1. Does giving an LLM the six-step funnel (7-9 mini-scenarios, cut to 2-3, draft, issues) beat a plain prompt and best-of-N at equal tokens on reasoning or planning items? No controlled test exists; this is our own experiment.
2. Which cut rule from 7-9 to 2-3 works for an LLM: the two most uncertain and most important drivers (Wack), maximum distance (diversity planning, Polyscene), or pairwise rank by the model itself? No head-to-head.
3. How many truly distinct mini-scenarios can an LLM produce when asked for 7-9, and which diversity forcing (named drivers, sampled personas, opposite-sign seeds) lifts it, measured by embedding clusters at equal tokens?
4. Do scenario-based prompts change LLM calibration (Brier) the way Schoemaker (overconfidence reduced) or Phadnis (no change) report for people? Needs resolved-question sets.
5. What is the real effect size of scenario planning on firm or decision outcomes in primary studies (Phelps 2001, Chermack, Meissner and Wulf 2013, Cordova-Pozo and Rouwette 2023 review)? Read the full texts.
6. What exactly did Wack and Shell do in 1972-73, per primary sources (Wack 1985 HBR full text, Wilkinson and Kupers 2013, Schoemaker 1993 full text), and which steps of the six-step recipe are original vs later tidy-up?
7. Does a separate robustness table (each action under each scenario) fix the "decision after scenarios" weakness (de Geus, Goodwin and Wright) when done by an LLM, or does the LLM just reproduce the narrative bias?
8. Can an LLM check scenario consistency (cross-impact, morphological cross-consistency) given the probe-versus-rating gap (de Langis 2025), and does an external symbolic check help at equal tokens?
9. Does the technology-optimism bias in LLM scenario drafts (Girona 80% and 61%) survive forced opposite-sign drivers, and does it appear in Claude-class models, not only GPT-4?
10. Does a targeted contrasting step ("think privately about the opposite future") beat generic balancing outside wargames, and at larger models than Mistral-7B?

## Gap search results (2026-11-03, gap searcher)

Evidence written to evidence_d.jsonl (d01-d16). Claims K01, K04, K18 got extra evidence ids; K19 and K20 added. Access was the main problem: arXiv, Semantic Scholar, OpenAlex and arxiv.org search all returned rate-limit errors, publisher pages returned 403 or paywall intros, and the WebSearch budget was used up. Only Crossref and a few landing pages worked.

- Gap 1 (funnel vs plain vs best-of-N): STAYED OPEN. No new paper reachable. Own experiment.
- Gap 2 (cut rule): STAYED OPEN. Design note d11 only; no measurement.
- Gap 3 (diversity forcing): STAYED OPEN.
- Gap 4 (calibration): STAYED OPEN. Human conflict still abstract-level.
- Gap 5 (effect size on firm outcomes): STAYED OPEN. Cordova-Pozo 2023 (173 citations) and Meissner and Wulf 2013 (124) confirmed to exist but not opened; Phelps 2001 not found.
- Gap 6 (what Wack did in 1972-73): PARTIAL. HBR 1985 and 2013 intros read: Wack and Newland built the system, Shell dropped its UPM forecast machine in the early 1970s. No primary method text; the 7-9 to 2-3 step is not traced to Wack (K19). Chermack 2017 is the next source.
- Gap 7 (robustness table): PARTIAL. Goodwin and Wright 2001 abstract confirms the weakness and proposes decision analysis. No LLM test.
- Gaps 8, 9, 10: STAYED OPEN.

Closed: none. Rerun when limits clear, starting with Cordova-Pozo 2023 full text, Chermack 2017, and an arXiv search for 2025-2026 LLM scenario papers.
