# Critique and cross-check: A10.10 Naturalistic decision making

## Re-opened this session (checked against source text)
1. Kopka & Feufel 2026 (PMC13061108): overall 63.3 / 67.6 / 66.7%, OR 2.26 and 2.05, self-care 13.4 to 29.8 / 24.6%, GPT-4.1 self-care 0 to 43.8 / 39.2%, reasoning interaction OR 2.15. CONFIRMED. GPT-4.1 mini DF 49.8 to 62.4 confirmed (+12.6, "13" is rounded); its RP value is 60.7 (+10.9).
2. CORRECTION: c10 and b13 say "6 ChatGPT models" for the published version. The published paper used 10 models (GPT-4o, 4.1, 4.1 mini, o3, o4 mini, o4 mini high, 5.1 Instant, 5.1 Thinking, 5.2 Instant, 5.2 Thinking). Six was the preprint. Use 10.
3. Vidulich & Tsang 2026 Study 1 (PMC13100097): 0.20 to 0.27, d=1.39; blunder size 0.98 to 1.45, d=0.96; EBPM 0.20 to 0.38. CONFIRMED. Kasparov 2750 to 2646 confirmed.
4. Hagendorff et al. (arXiv 2212.05206): CRT correct GPT-4 96%, ChatGPT-3.5 59%; intuitive errors 80% davinci, 55% humans, 15% ChatGPT-3.5, 0% GPT-4; CoT davinci intuitive 80 to 29%; no-CoT GPT-4 95 to 88%, intuitive 0 to 10%. CONFIRMED. b14 says 95% for GPT-4 CRT; Study 1 gives 96%, 95% is the Study 2 baseline. Minor.
5. SwiftSage (arXiv 2305.17390): 84.7 vs 33.8 / 36.4 / 45.3, fast-only 49.22, 757.07 vs 2,983.46 tokens per action. CONFIRMED. ReAct 1,971 and SayCan 1,856 tokens not re-checked.
6. Chen et al. (arXiv 2412.21187): 1,953% more tokens, 48.6% token cut, "more than 92%" initial round correct. CONFIRMED. The 92% applies to QwQ-32B and R1 on ASDIV/MATH500 only.
7. NOT confirmed: Grove et al. 2000 (b20, from memory; abstract fetch failed). Treat "136 studies, mechanical about 10% better" as unverified.
8. NOT reachable: the founding fireground report (a24, b01). The 80-90%, under 12%, 156 points, 26 commanders figures stay second-hand.

## Contradictions and weak spots
- Fireground percentages vary by source (80%, 80-90%, 81.4%, "117 of 134"). Nobody read the report, so K01 is single-source despite many lines.
- RPD replications named by Klein & Wright (Schmitt & Klein 1999, Keren 2013, Skriver 1998) are listed by the model's founder, not described, not independent.
- Take-the-first (Johnson & Raab) was never opened; effect sizes unknown. The rival long-term-working-memory model predicts the opposite sign and was not tested head to head.
- Einstellung (Bilalic) pulls against RPD: the first recognised option can block a better one. Both hold; when first match is dangerous is not quantified.
- Only one study (Kopka & Feufel) tests NDM prompts on LLMs: 2 emergency cases, no chain-of-thought-only baseline in the parts read, no gain for GPT-5.2. All other "LLM" lines are dual-process analogues, not NDM tests.
- Pre-mortem, wargame and forecasting lines link to NDM only by analogy.
- Snippet-only or unopened: a24-a27, b01, b04, b05, b06, b13, b20, b27, b28, c10, c11, c27, c28.
- Samples are small (one goalkeeper, 44 players, 20 grandmasters); chess is not field work.

## GAPS
1. What exactly do the founding fireground report and its 2010 postscript say (N, definition of "comparison", the unaccounted ~8%)?
2. Do NDM-style frames beat plain chain-of-thought at equal tokens on tasks other than triage, and on frontier models where GPT-5.2 showed no gain?
3. What is the first-option vs later-option quality gap in Johnson & Raab and Raab & Johnson (N, effect sizes), and has it replicated outside sport?
4. Can an agent tell when its quick answer is in a regular, feedback-rich zone (Kahneman & Klein condition) better than its own confidence does?
5. How often is the first-round answer of reasoning models final-correct by task difficulty, and what early-exit rule keeps accuracy at lower tokens?
6. Which escalation triggers (SwiftSage-style) work best for a text-only agent, and what is the false-alarm cost?
7. How large is the Einstellung penalty for LLM agents when a familiar-but-worse solution is present, and does a forced re-look operator fix it?
8. Does the cap of about 3 variables and 6 transitions on mental simulation have an LLM analogue that improves the simulate branch?
9. Is the Grove et al. (2000) mechanical-vs-clinical result confirmed, and do LLM judges follow the same pattern against simple formulas?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d23). Claims K01-K03, K06, K08, K12, K14 were updated and K22-K28 added.

1. Fireground report: PARTLY CLOSED. The 2010 abstract and the 1986 abstract (Crossref) confirm 26 commanders (mean 23 years), 156 decision points, under 12% with simultaneous comparison of two or more options, and over 80% direct identification of typical situation and action. The "80-90%" figure is not in the primary abstract. "Comparison" means simultaneous relative evaluation, so testing one option at a time does not count. The full report (DTIC ADA199492) and the postscript returned HTTP 403; the share between 12% and 80% (up to about 8%) is still unexplained.
2. NDM frames vs plain chain of thought at equal tokens: OPEN. Re-reading Kopka & Feufel shows no chain-of-thought arm and no token comparison, and the authors say part of the gain may be extra reasoning. No other NDM-prompt study was found. Needs our own test.
3. First option vs later options: OPEN for effect sizes. Johnson & Raab (2003) and Raab & Johnson (2007) are closed access. Non-sport evidence leans against take-the-first: a 2025 knowledge-free task (44 healthy, 53 MDD) found later paths more unique (medians 122.7 vs 374.5, 155.7 vs 542.0), and the LTWM side cites nurses and soccer (Ward 2010, 2013), Missier 2015, Belling 2015 (time pressure restores TTF-like behaviour). That is a secondary summary.
4. Can an agent sense a regular, feedback-rich zone better than its confidence: PARTLY ANSWERED, negative for stated confidence. Inserted confidence sentences swing delegation (median 20.6 points; 53-70 on larger models) but well-targeted flips beat chance by only +2 points (Nudgeability, 9 open models). A 2026 judge study finds verbalized confidence useful on the newest proprietary models, so it may be model-dependent. Kahneman & Klein 2009 full text could not be opened. No test of regularity detection exists.
5. First-round correct by difficulty and early exit: MOSTLY CLOSED. Easy problems peak at about 1.5K thinking tokens and hard ones at about 8K (R1-32B); past about 7K tokens net flips are harmful (67.5% of 80 inspected negative flips were true overthinking). DEER's 0.95 confidence-threshold exit cut chains 19.1-80.1% with accuracy +0.3 to +5.0 over 11 models and 10 benchmarks; answer-repeat stopping cut over 40% of tokens on NQ but is unstable on MATH-500 and GPQA; a hidden-state probe saved 24% but needs weights. All on open reasoning models; frontier API models are untested.
6. Escalation triggers: PARTLY ANSWERED. SwiftSage's four triggers have no per-trigger ablation. ReflexGrad's stall rule tested m=3/5/7: 84.3% / 88.1% / 86.6% on GPT-5 ALFWorld; each false slow activation costs 5 calls and a 5-step cooldown; m=10 missed recoveries. One benchmark, author-built.
7. Einstellung penalty and re-look: OPEN. OnlyConnect shows large fixation-like loss (GPT-4 0-shot 6 solved walls with red herrings vs about 59 without; 2023 models; read from a jumbled table). A six-item mental-set test is noise. No forced re-look test exists.
8. Simulation cap analogue: OPEN for the exact cap. LLMs show load limits (PI-LLM log-linear drop with interference; N-back in 15 models; entity tracking depends on operations per box), but no 3-variable/6-transition measurement. Measure on our own model.
9. Grove et al. 2000: CONFIRMED at abstract level (about 10% more accurate; 33-47% and 6-16%). "136 studies" is unverified. LLM judges vs simple formulas: only one small 2026 comparison (logistic regression 84.1% vs prompted LLMs 60-80%, LLM test set about 30 cases); no real test.

Corrections carried forward: Kopka & Feufel published version used 10 models; Hagendorff CRT GPT-4 is 96% in Study 1 (95% is the Study 2 baseline); the Chen "over 92%" first-round figure applies to QwQ-32B and R1 on ASDIV and MATH500 only.
