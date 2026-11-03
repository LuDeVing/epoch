# Critique: A03.06 Debiasing by structure (incentives, nudges, reference class forecasting)

Cross-check by re-opening sources (PDF or full text, 2026-11-03). Semantic Scholar returned 429; no WebSearch used.

## Numbers re-opened and confirmed
1. Johnson and Goldstein (2003): N=161, opt-in 42%, opt-out 82%, neutral 79%; country rates (4.25, 27.5, 99.98, 99.91, 99.97, 99.5, 99.64) and the 16.3% (P<0.02) increase. a01-a03 correct. Source: dangoldstein.com PDF.
2. Mertens et al. (2022): d=0.45 [0.39, 0.52], n=2,149,683, "more than 200 studies... over 450 effect sizes". a04 correct (abstract, Europe PMC).
3. Maier et al. (2022) PNAS table: unadjusted 0.43 [0.38, 0.48]; RoBMA-PSMA 0.04 [0.00, 0.14] BF01=0.95; precise 0.11 [0.00, 0.24] BF01=0.31; Information 0.00, BF01 33.84 / 10.57; Structure 0.12 [0.00, 0.43], BF01 1.12 / 0.33; Egger b=2.10. a08, b01, b02 correct.
4. Szaszi et al. (2022): severe 0.08, moderate 0.31, Andrews-Kasy -0.01 (SE 0.02), WAAP 0.07 (SE 0.03), trim and fill 0.08 (SE 0.03). b04 correct.
5. DellaVigna and Linos (NBER w27594 working paper): 126 trials, 243 nudges, 23.5 million people; 1.38 pp (SE 0.30); academic 8.7 pp. a10 correct.
6. Flyvbjerg (2006): overrun 44.7 / 33.8 / 20.4%; rail demand error -51.4% (sd 28.1), road 9.5% (sd 44.3); 84% vs 50% off by more than 20%; students 84% of peers; uplifts 15/45 road, 40/68 rail, 32 and 57 at 80% certainty. a12, a14, a16 correct.
7. Halawi et al. (2024): 48,754 questions, 7,174,607 forecasts, 33,664 binary; Brier .179 vs crowd .149, accuracy 71.5% vs 77.0%, best plain GPT-4 .208, random .250. a29, b12 correct.
8. Schoenegger et al. (2024): 925 humans, 31 questions, LLM 0.20 (SD .12) vs human 0.19 (SD .19), t(60)=0.19, p=.850; mean 57.35%, t(1006)=86.20; 17-28% gain; GPT-4 .17->.14, Claude 2 .22->.15. c05, c06 correct.

## Corrections
- a07 says Egger b = 2.28 and severe-bias d = 0.03. Maier, Szaszi and the Mertens reply (b01, b03, b04) all give b = 2.10 and severe d = 0.08. Treat a07 as wrong; use 2.10 and 0.08. The 0.03 may come from an earlier version of the supplement; not resolved.
- a10 says nudge units were 8.0% over control mean; the working paper gives 8.1%. Minor. a11 "about 70% of the gap" was only seen in an abstract page; the paper text says that well-powered academic nudges, controlling for power with an Egger-type test, explain "the entire difference". Do not quote 70% without checking the published version.
- a14 "roads 32%" is a UK DfT table value for local roads/the road category (50% and 80% percentiles), not a general road figure. It is UK Department for Transport practice.
- Maier's own category effects (information 0.25, structure 0.58, assistance 0.22) differ from Mertens' (0.38, 0.55, 0.31); a05 uses Mertens only. Both codings are valid; the gap is a coding difference, not an error.
- b06 and a10 duplicate each other; counted as one independent source.
- a08 and b01 are the same paper; a04/a07 and b03 are the same author group. The independent_sources counts in claims.jsonl reflect this.
- Crowd Brier is .149 on all test questions but .146 in the table rows where the system has retrieval (subset). Quote .149 for the overall comparison.

## Contradictions between sources
- Nudges overall: d=0.43-0.45 (unadjusted) vs 0.04-0.11 (RoBMA) vs 0.08-0.31 (Mertens/Szaszi). Maier and Szaszi say no evidence; Mertens say modest evidence under moderate bias. Contested (claim K04).
- Nudge units (1.4 pp) vs academic papers (8.7 pp): DellaVigna and Linos attribute most of the gap to selective publication, but also note nudge units exclude defaults, which are larger (Jachimowicz). So the "defaults work" result is not refuted by the nudge-unit finding; it is simply untested there.
- Awareness prompt: helps anchoring in GPT-4 (0.250 -> 0.105) but not framing (b15) and hurts bandwagon in GPT-3.5 (b17). Different benchmarks, different bias definitions.
- LLM anchoring strength: Lou and Sun report a weaker anchoring index for GPT-4 (0.45) than a human-style study (0.61); Suri et al. report ChatGPT's high anchor stronger than humans' (105.97 vs 80.50). Different designs.

## Weak spots
- The core human literature is thin: accountability (Lerner and Tetlock), financial incentives (Camerer and Hogarth), the 401(k) default (Madrian and Shea), the planning fallacy (Buehler et al.), and the defaults meta-analysis (Jachimowicz) were never opened. Claims K10-K12 are placeholders.
- Reference class forecasting evidence is almost all Flyvbjerg's own datasets (infrastructure). Single author group, and the 2013 benchmark (33% -> 9.1%) is a descriptive comparison rather than a test with a control. Kahneman and Lovallo's original contexts and any failed replication of outside-view prompting were not found.
- No LLM study tests reference class forecasting as a bias remedy (the agent retrieves a class record and uses its rate). Halawi et al. is the closest, using retrieval and base-rate prompting, but the ablation does not isolate the base-rate step.
- Many LLM results are on 2022-2023 models (Codex, GPT-3.5, Llama-2); effects on current models are unknown. One summary claim (b17, arXiv 2412) has no author list recorded.
- Incentive-prompt studies (EmotionPrompt, tipping, Principled Instructions) measure task accuracy, not bias reduction, so they bear on "incentives" only by analogy.
- Only seen in snippets or recalled: a17-a21, b06, b07, b23, b24, c20-c22.

## GAPS
1. Does giving an LLM agent a retrieved reference class (past similar tasks with outcomes) improve calibrated estimates over a base-rate prompt alone, at equal tokens? (No study found; decisive for S0 gate / S7 selection.)
2. What do Lerner and Tetlock (1999) actually show: which kinds of accountability reduce which biases, with effect sizes, and has any LLM study tested an accuracy-demanding audience prompt?
3. What is the pooled effect of defaults (Jachimowicz et al. 2019) and how well does it survive the publication-bias corrections used by Maier and Szaszi?
4. Does the outside-view prompt for humans (Kahneman and Lovallo; Buehler et al.) replicate, and by how much does it cut planning-fallacy error in preregistered studies?
5. Madrian and Shea (2001) and later default-with-active-choice studies: what happens when the default is removed or when people must actively choose, and does a forced-choice step help an LLM?
6. Which of the LLM mitigations (awareness, self-help re-asking, abstention) still work on 2025-2026 models, and are any worse than no mitigation on framing or order bias?
7. Does a structural change (reordering options, removing the anchor, re-asking) beat a warning line on LLM anchoring at equal tokens?
8. How big are nudge effects in domains where the "default" is a model output (human-in-the-loop AI advice), and does showing a base rate reduce over-reliance?
9. Is there any failed replication of reference class forecasting outside infrastructure (software projects, startups, medical trials)?
10. Do incentive-style prompts (tips, penalties, accountability statements) change calibration, not just accuracy, in current models?


## Gap search results (2026-11-03)
Limits: arXiv API, Semantic Scholar, OpenAlex and dblp all returned 429 (shared quota); WebSearch was refused after one call (budget used). Sources were reached by direct URL, arXiv abs/pdf pages, NBER, Europe PMC, Crossref and a journal site. New evidence is in evidence_d.jsonl (d01-d17). Claims K10-K12 and K24 updated; K25-K29 added.

1. Retrieved reference class vs base-rate prompt at equal tokens: STAYED OPEN. No study found. Partial help (d13): in a 20-model benchmark, models handed the class overrun rate update on it (planning-fallacy score about -0.02 on average, GPT-4o -0.16), so the weak step is picking and retrieving the class (d15 also names class choice as RCF's weak point). Needs our own ablation (K28, K29).
2. Lerner and Tetlock: PARTLY CLOSED. Full text blocked (d06, abstract only). A 266-experiment systematic review (d05) gives the direction: accountability raises effort and information use, usually weakens bias, works better when announced before the task, lowers overconfidence, worsens the dilution effect; process accountability gives calibrated and consistent decisions. No effect sizes. No LLM accountability-prompt study found.
3. Defaults pooled effect: PARTLY CLOSED. Jachimowicz: 58 studies, n=73,675, d=0.68 [0.53, 0.83], two negative (d04, abstract only). Survival under bias correction was not tested by anyone found; Maier's corrected structure category is 0.12 [0.00, 0.43], so treat 0.68 as an upper bound. New: defaults fade with decision time (d03, interaction d=1.19; preregistered N=637 shows 66% vs 64% at long times).
4. Outside-view prompt replication (Buehler, Kahneman and Lovallo): STAYED OPEN. Only secondary figures for the bias itself (d14: 33.9 predicted vs 55.5 actual days, 30% on time; 13%/19%/45% finishing by the 50/75/99% estimates). No preregistered outside-view test found.
5. Madrian and Shea and active choice: PARTLY CLOSED. Opened primary (d01, d02): 37% vs 86% participation; 76% at default 3%; non-default share 7% to 37% in 15 months, so inertia decays. Active-choice studies not found. Forcing functions in human-AI work (d07): commit-first cut following wrong advice but gave no net accuracy gain. No LLM forced-choice test.
6. Mitigations on 2025-2026 models: STAYED OPEN. Newest tests found use 2024 models (d10, d11, d12). Pattern: self-help rewrite works on stronger models, awareness is uneven, majority-style prompts worsen bandwagon.
7. Structure vs warning at equal tokens: PARTLY CLOSED for 2023 models (d10: self-help rewrite beat awareness, few-shot, counterfactual); not equal-token and not current models.
8. Human-in-the-loop AI advice: PARTLY CLOSED (d07, d08, d09): overreliance is strategic, falls with cheaper checking on hard tasks, a larger bonus ($0.50 vs $0.01, N=114) and forcing functions. Showing a base rate to curb over-reliance was not found.
9. Failed RCF replication outside infrastructure: STAYED OPEN. Lovallo, Clarke and Camerer 2012 located (d16) but not opened (403).
10. Incentive prompts and calibration: STAYED OPEN. No study changes stakes or audience and measures calibration in current models. d17 supplies a calibration metric (verbalised confidence) only.

Corrections: d11 resolves the missing author list for the arXiv 2412 paper in b17 (Sumita, Takeuchi, Kashima). That paper disagrees internally on whether awareness helped order bias in GPT-3.5 (results text says no significant change, discussion says it did); quote neither without checking tables.
Caveats: d14 is a secondary source; d04, d06, d15, d17 are abstract-level; d13 cell values were parsed from a flattened PDF table.
