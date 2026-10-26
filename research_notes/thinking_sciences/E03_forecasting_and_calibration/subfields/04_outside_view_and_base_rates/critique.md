# Critique: E03.04 Outside view and base rates (cross-check)

## Sources re-opened and checked this session (full text)
Chang et al. 2016 (JDM PDF), Schoenegger et al. 2025 prompt engineering (2506.01578), Pratt et al. 2024 (2406.04446), Halawi et al. 2024 (2402.18563), Flyvbjerg et al. 2024 uniqueness (2408.07710), Schoenegger and Park 2023 (2310.13014), Hsieh et al. 2024 (2408.12036).

## Confirmed
- Chang Table 5: comparison classes 0.17 (n=580), math/stat models 0.26 (453), select questions 0.26 (330), hunt for info 0.38, update 0.44, post-mortem 1.04, control 0.49. Year 1: -0.05 (n=119), -0.06 (n=113), +0.07 (n=152), F(2,381)=12.1.
- Schoenegger 2025: Base Rate First -0.016 (N=390, adj p=.036), mixed model -0.011 (adj p=.774); Frequency-Based -0.019; Step-Back -0.015; Multiple Reference Classes t-test -0.009 (adj p=.233), mixed -0.004; Base Rate First + CoT 0.000, adj p=.985; Base Rate First + Frequency -0.012, adj p=.162.
- Pratt: validation Brier Human .1334, Basic .1221, Base Rates .1562; weighted Base Rates .2540 (worst), Human .1746.
- Halawi: full system .179 vs crowd .149, 71.5% vs 77.0%; no fine-tuning .186 (+.007); no fine-tuning and no retrieval .206; 13,253 fine-tuning samples.
- Uniqueness paper: N=219, +5 points per uniqueness point, +45 at 10, 37% vs 1% extreme risk, tail 23 times the Gaussian (16% vs 0.7% extreme).
- Schoenegger and Park 2023: GPT-4 .20 (SD .18), crowd .07 (SD .08), t(22)=-1.23, p=.23 (23 questions).
- Hsieh: RTF .169 (median of 3), .170 (mean), crowd .172, sampled .180, GPT-4o .210.

## Corrections and cautions
1. The "0.17 vs 0.26" S0 line in SUBFIELDS.md is a standardized, self-tagged, correlational score, not a raw Brier. Two principles tie at 0.26. The AI Impacts page drops "standardized".
2. Oddity in Chang Table 5: all "standardized" means are positive (control 0.49, categorized 0.42). A deviation-from-question-mean score should average near zero, so the scale is not plain centering. The "SD" column (0.003 etc.) looks like a standard error. The unit is unclear, so use only the rank order.
3. a23 had a garbled .179; it is the confirmed test Brier of the full system. The base-rate line is one part of the prompt and was not ablated.
4. b19 and c01 list different author sets for the same paper (b19: Jones, Tetlock, Mellers; c01: Park, Karger, Trott, Tetlock). Not resolved here. Cite by first author and title.
5. c08 "without retrieval about .183" is the "no IR" row of Halawi's table; other rows are garbled in extraction and the row labels are uncertain.
6. c01 says "37 prompts"; b19 says 38. The paper's text should be checked for the count.
7. b02 says the tag analysis is year 4 only; the PDF confirms year-4 tagging.

## Contradictions between sources
- LLM prompt evidence: simple t-tests say Base Rate First helps (-0.016); the preregistered mixed model says no (-0.011, adj p=.774). Report the mixed model as the main result.
- Frequency format: Gigerenzer and Hoffrage 46-50% Bayesian; later replications 51% and 31% (Sloman), not significant gains. Both stand; effect size shrinks.
- Planning fallacy vs hiding hand: 22% of 327 projects show benefit overruns above cost overruns. The planning-fallacy side wrote both papers, so the sample is one group's.
- Politics vs psychology of optimism: not resolved.
- Pratt: the base-rate strategy is worst, yet Schoenegger finds it slightly positive. Differences: PaLM 2 with recalled base rates, mostly-No events vs frontier models and ForecastBench.

## Weak spots
- No source isolates the S0 step in a strong LLM scaffold. Every LLM result bundles it.
- No controlled test that RCF improves real project outcomes (a24).
- Human lab results are on students; project data are on large public projects (not random).
- LLM studies use 23 to 100 questions; effects of 0.01 to 0.02 Brier are inside noise.
- Dataset Yes-rate confounds base-rate prompts (Pratt, c11).
- Claims rated "established" mostly rest on cited or review sources for the human side; the founding Kahneman and Lovallo paper has no experiment.

## Seen only in snippets or second-hand (not opened)
Lovallo and Kahneman 2003 and Gilovich 2002 (student 84% / 20%), Buehler et al. 1994 and 1995 (Wikipedia figures), Koehler 1996, Brenner et al. 2005 and 2006, Cooper et al. 1988, Merrow 1981, PIMS, ForecastBench numbers beyond the abstract and tables (b17 "gap 0.054 vs 0.026" unverified), Lu 2025, AIA Forecaster, CogBias, Mu et al., Bench to the Future results, Schoenegger 2024 AI-augmented (b22 numbers odd and unverified).

## GAPS
1. Does a first-step class lookup (S0) beat a late base-rate check and no step, inside a retrieval-based scaffold, at equal tokens, on a balanced set of resolved questions with a mixed-model analysis?
2. Does a computed or retrieved class frequency (count by tool or search) beat a model-recalled one, and how big is the spread between runs (30% vs 8% in Hsieh)?
3. How should two or more disagreeing comparison classes be combined (pick, average, widen)? Multiple Reference Classes showed nothing; is there any tested rule?
4. Does the class lookup help more for weak models than for strong reasoning models that already do it unprompted (o3, o1)?
5. What is the real size of the Chang comparison-classes effect after controlling for question difficulty, and what is the unit of the standardized score? Is there a randomized test of the outside-view instruction alone (not CHAMP bundle)?
6. Does shrinking toward the class rate when the rate is extreme (below 10% or above 90%) improve Brier, as the Halawi crowd-confident result suggests?
7. Does the "this case is unique" signal predict LLM errors the way uniqueness predicts human overruns (a16), and should it trigger the class lookup?
8. Do natural-frequency counts versus percentages change LLM base-rate use, and does code-side arithmetic for chained updates beat in-text arithmetic?
9. Which tasks beyond forecasting (planning time, code effort estimates, ARC-style tasks) have usable classes, and what is the S0 fallback when no class exists?
10. What did Lovallo and Kahneman 2003 and Buehler 1994 actually report (N, design, effect), to anchor the order rule (class facts before case details)?


## Gap search results (evidence_d.jsonl, d01-d20)

Search limits: the shared WebSearch quota ran out, the arXiv API, OpenAlex and Semantic Scholar returned 429 or budget errors, so papers were found by direct arXiv PDF download and by re-reading earlier PDFs. No new paper was found that isolates an S0 step. Full texts opened: Buehler et al. 1994, Chang 2016, Halawi 2024, Hsieh 2024, Pratt 2024, Schoenegger 2024 and 2025, ForecastBench, Murphy 2026, Hindcast 2026, METR 2025, Araya 2025, REFER 2025, Paleka 2025, Flyvbjerg 2003 comment. Not opened: Lovallo, Clarke and Camerer 2012 (closed; abstract only), Lovallo and Kahneman 2003.

1. First-step lookup vs late check vs none, equal tokens: STAYS OPEN. Every system fixes one placement (Halawi last, ForecastBench step 2 of 8, Hindcast step 1 anchor bands). Only bundle contrast found: ForecastBench scratchpad vs zero-shot, GPT-4o .147 vs .168, Gemini-1.5-Pro .143 vs .147 (d16). Schoenegger Study 2 shows no base-rate prompt helps any of six models in a mixed model (d08).
2. Computed or retrieved class vs recalled: LARGELY CLOSED in direction. Code-counted priors are strong (Brier Index 58.3 vs agent 62.7; KNN counter 59.1 vs 50 baseline, d12, d13) and the recalled-base-rate pipeline was worst in Pratt (d11). Run spread: the "30% vs 8%" number was not found in Hsieh; the measured spread is ensemble SD 0.092 (ReAct) vs 0.150 (base LMs) (d10). No head-to-head recalled vs computed vs supplied on one question set.
3. Combining disagreeing classes: STAYS OPEN. Only rule in use is a plain average (d10); the field paper that says many similarity-weighted analogies beat few familiar ones was abstract-only (d05). Proposed test stays in K03.
4. Weak vs strong models: PARTLY INFORMED, no interaction test exists. o1 and o1-mini no better than non-reasoning models and no base-rate prompt helped any (d08); small reasoning model hurt by the scaffold (d15); small models skip a count-first step (d19). Still unresolved whether S0 helps weak models more.
5. Chang size and unit: PARTLY CLOSED. The score is standardized within question, so difficulty is controlled; unit still undefined (all means positive); the tag is self-reported; ANOVA F=12.28 for comparison classes; authors say it is too early to credit only that tag (d06). No randomized test of the outside-view instruction alone found anywhere. Also found: a base-rate-neglecting assistant helped humans nearly as much as a base-rate-first one (d07), which raises an anchoring confound.
6. Shrinking toward extreme class rates: STAYS OPEN with suggestive evidence. Halawi hedged and lost 0.04 Brier where the crowd was extreme (d09); Murphy's shrinkage was by run disagreement, not class rate, and chose none (d14); arithmetic floor from Paleka (d20). No direct test.
7. Uniqueness signal predicts LLM error: STAYS OPEN. Nothing found beyond the human data (a16).
8. Natural frequencies and code-side arithmetic: PARTLY CLOSED. LLMs do not spontaneously use natural frequencies and follow the instruction unevenly (one puzzle, three models, d18); code-side counting worked for seasonal class frequencies (d13). No forecasting test of text-frequency vs percent format.
9. Tasks beyond forecasting: PARTLY CLOSED. Software effort has a class (METR trial: 24% predicted speedup, 19% measured slowdown, experts 38 to 39% wrong, d17); no LLM test of an S0 step on effort or ARC-style tasks found. Fallback when no class exists is still undecided: widen the interval and say the class is unverified (design suggestion, not evidence).
10. Lovallo and Kahneman 2003 and Buehler 1994: PARTLY CLOSED. Buehler 1994 now read in full: Study 1 N=37, 33.9 vs 55.5 days, worst case 48.6; Study 4 N=123, linking recall to the task raised on-time finishes from 29.3% to 60.0% with no gain in absolute error; Study 5 N=123 observers (d01-d03). The 2003 Lovallo and Kahneman article could not be opened; only Flyvbjerg's reply (d04). Order rule (class facts before case details) has no direct primary test in what was read.

New cautions found
- Author sets: Schoenegger et al. 2025 prompt engineering is Schoenegger, Jones, Tetlock, Mellers (the b19 set). The Park, Karger, Trott, Tetlock set belongs to the AI-augmented paper (d07), so c01 may have attached the wrong author list (not verified against the c01 line itself).
- b22 oddity resolved: the AI-augmented study is N=991 humans, 6 questions; "24 to 28%" is accuracy gain over a weaker-assistant control.
- Pratt's Base Rates strategy is recalled from model memory with no search (d11), so its weakness does not speak to tool-computed classes.
- ForecastBench b17 numbers 0.054 vs 0.026 confirmed (d16).
