# A20.08 Cognitive biases in software work: cross-check critique

Cross-checker pass. Re-opened (PDF text, this session): Mohanani 2020, Calikli/Arslan/Bener 2010, Shepperd 2018, Zhou 2026, Sovrano 2026 (PROBE-SWE mitigation), Failing to Falsify 2026, Zhao 2026, Kraishan 2026, Malberg 2025, Jones and Steinhardt 2022. Scratch PDFs and text deleted.

## Confirmed (no change)
- Mohanani: 826 retrieved, 308 removed, 65 primary studies, 37 biases, anchoring 26, confirmation 23.
- Shepperd: 410 developers, robust d=1.19, trimmed gap 60.5, about 350%, variance down threefold, 272 after dropping UK/Nepal/Vietnam, 102 with the workshop.
- Zhou: 2,013 actions, 808 LLM, 25% (505/2013) vs 52.9% (1104/2084) reversal, p=0.058, 257/949 biased reversed, Fixation 33 reversed = 43.4%.
- PROBE-SWE 2026: 12.9% control, 16.1% CoT, 10.2% / 10.3% / 8.3% for the debias prompts, 51% axiomatic reduction, tiers 8.1%->3.5% and 17.0%->12.2%.
- Failing to Falsify: 42% to 56%, 6% to 78%, I:C 1.79 human, TiO success in all, Dual-Goal in 8 of 11, I:C up in 18 of 22; QwQ baseline 0.500 / 0.362.
- Zhao: 137.69 / 104.15 vs 16.46 / 304.08; docstring 113.00 / 186.77; advanced 87.38 / 230.23; r=0.90; 318 methods, 233 defects.
- Kraishan: 12,350 calls, dz 0.27, p=.157, anchoring d=1.89, 79% of R1 calls over ceiling.
- Malberg: anchoring mean 0.39 (range -0.05 to 0.67), confirmation 0.15 (range -0.18 to 0.72), 30,000 tests, 20 models.
- Jones and Steinhardt: 22.3 to 30.5 points, 81% and 70.7% vs 4.5% and 0.0%, 32.9 / 25.6 baselines, 50% to 17%, 100% to 4.4%.

## Corrections made
1. a05 title is wrong. The PPIG 2010 PDF is Calikli, Arslan, Bener, "Confirmation Bias in Software Development and Testing: An Analysis of the Effects of Company Size, Experience and Reasoning Skills". Mohanani's P4 cites Calikli and Bener, which may be a related PROMISE 2010 paper; the link between the two was not opened.
2. a08 vs b05 conflict (students vs staff). Both are true but about different comparisons. Whole-group: students beat all staff on abstract questions (chi2(1)=8.114, p<.005) and software-themed ones (7.085, p<.01); 27 of 28 students found the rule vs 29 of 34 at the large firm. Experience-matched (43 employees vs 13 students): only test duration differed. So "students are better" is supported only when experience is not controlled. Students were also tested in a different setting.
3. a08 reports z=-1.39 as p<.05. A z of 1.39 is about p=.16 two-sided. The paper's own statement is unreliable; treat the duration difference as not significant.
4. b07 wrote "with workshop d=0.72" as if it were the anchor effect. In Shepperd, 0.72 is the standardised effect of the workshop on estimates (trimmed mean difference of 26 LOC/h), not the anchor effect inside the workshop group. The anchor effect (d=1.19) is from the no-workshop series. The median for the high anchor fell from 100 to 30 LOC/h.
5. Zhou is internally inconsistent: 949 (47.14%) vs 983 (48.8%) biased actions; 434/808 (53.71%) vs 456/808 (56.4%) biased LLM actions; chi-square 22.94 in the PDF vs 30.72 in the HTML v1 seen by c09. Use ranges (47-49%, 54-56%). a16 compares against the 2020 paper's 45.72%, which was not opened.
6. a22 and c22 are one paper (Lampinen et al., arXiv 2207.07051, earlier author list Dasgupta). Count it once.
7. a11-a13 (PROBE-SWE 2025) and b17-b18 (PROBE-SWE 2026) are the same group and benchmark. They are not independent. Also the 2025 paper rates anchoring the weakest bias (5.9%) while Malberg 2025 rates it among the strongest (0.39). Different measure (decision flip rate on SE vignettes vs signed score on managerial scenarios).
8. Independence: Jones and Steinhardt appear as a17-a20, b12, c01-c03; Zhou as a14-a16, b19-b20, c09-c10; Calikli as a05-a10, b05-b06. Counted once each in claims.

## Contradictions between sources
- Do reasoning models bias less? SynAnchors says yes (22-25% anchored vs 60% for a small model); Kraishan says no (+0.031, n.s.); PROBE-SWE says CoT makes it worse. Metrics and vignettes differ. Marked contested (K10, K11).
- Is confirmation bias even present in LLMs? Failing to Falsify, FalsifyBench and Zhao show confirm-seeking test selection. Malberg shows weak mean scores; Kraishan finds the opposite direction in all 7 models. Likely two constructs: bias in choosing tests (strong) vs bias in judging a vignette (weak). Do not merge them.
- Anchoring: strong with numeric and in-context code anchors, weakest in PROBE-SWE.
- Human debiasing: workshop helps partly (Shepperd) but Mohanani says no strong evidence and Gren and Svensson show instruction to ignore fails.

## Weak spots
- The core human claim (logic training lowers confirmation bias) is one 2010 correlational study with N=88, Mann-Whitney on small groups and group differences in setting and stress.
- Defect link is 5 developers and 12 testers.
- No human replications of Calikli were found; no randomised training trial exists in the evidence set.
- Almost all LLM work is on vignettes, abstract rule games, or old models (Codex, GPT-3.5, Llama 2). Frontier models are mostly untested. PROBE-SWE 2026 says so itself.
- Failing to Falsify, FalsifyBench and Zhao are 2026 preprints with large effects and no independent replication.
- Zhao's misguided-test metric correlates r=0.90 with effective tests, so it partly tracks volume.

## Only seen in snippets or second hand
- a24 Itzhak et al. (abstract only), a29 Fischhoff (via Mohanani), a30 Chattopadhyay 2020 (numbers via Zhou), b24 Wason 1960 and Klayman and Ha (from memory), b25 Leventhal 1994, b26 Aranda and Easterbrook 2005, c18 BlindSpotEval (abstract), c21 Sharma sycophancy (abstract), c22, c23 LLM-as-judge (abstract).
- Several c-lines note unread tails of pages (Zhao, Failing to Falsify, SynAnchors, Zhou HTML).
- Mohanani P-numbers (P4, P6, P31, P32) were taken from the review, and the underlying studies were not opened.

## GAPS
1. Does a forced falsification step (Think-in-Opposites or Dual-Goal) raise fix correctness on real code tasks (not 2-4-6 games), at equal tokens, on a frontier model?
2. Does writing tests from a spec in a clean context (without the candidate code) beat tests written with the code visible on non-Java, non-Defects4J tasks, and what share of generated specs inherit the bug?
3. How much does leaving a failed attempt in context hurt a modern instruction-tuned or reasoning model's next attempt, versus a clean-context retry? (Only Codex and CodeGen were tested directly.)
4. Is there any randomised trial in humans where logic or hypothesis-testing training reduces positive test bias in software testing? Did anyone replicate Calikli et al. 2010, and what is the Calikli and Bener PROMISE 2010 study (Mohanani P4) actually reporting?
5. Do reasoning models anchor and confirm less on code tasks, and does the SynAnchors vs Kraishan disagreement hold on a single common probe set?
6. Do the Leventhal et al. 1994 positive test bias numbers (spec completeness, domain knowledge as moderators) hold up, and does a more complete spec reduce positive tests in LLM test writers too?
7. Does asking the agent for a reference-class base rate before it estimates success reduce optimism in its own confidence, given that optimism and planning fallacy scores are near zero in Malberg?
8. Is stated confidence anchored by framing words ("this is easy") in LLMs the way self-rated comprehensibility is in people (Wyrich), while accuracy stays unchanged?
9. What is the cost-benefit of axiomatic cues (write the rules a correct answer must satisfy) on frontier models and on code tasks, given wide CIs on the open-ended test?
10. Does instruction tuning raise positive-test rates within a model family (base vs instruct) on the same falsification probe?

## Gap search results

Run 2026-11-10. 22 evidence lines in evidence_d.jsonl (18 opened). Semantic Scholar and the arXiv API were rate-limited; OpenAlex and 8 web searches were used, so coverage is partial.

1. Forced falsification step on real code at equal tokens: STAYS OPEN. Human RCT (Branchini 2025, N=180, 78.3% vs 36.7%) and LLM rule games exist (K02 now established for 2-4-6 tasks). Failing to Falsify transfers to AIME self-correction for Qwen3-8B (0.33 to 0.60, p=0.039; 32B n.s.) and says debugging is untested. No code-fix test found.
2. Tests from spec in clean context, non-Java: PARTLY CLOSED. Haeri 2026 (Python, Claude Haiku/Sonnet/Opus, GPT-5.3-codex, Gemini 3.5 Flash): rule-grounded tests 62% to 100% final correctness (+38 pp), false alarms 0% vs 33%. But all arms already hide the code, so code-visible vs code-hidden is still not compared. Spec inheriting the bug: injected, not measured as a rate; wrong rule lowered test accuracy to 82.8%, detection stayed 30/30. Ma and Eisty 2026 Java pilot (10 bugs) agrees. K04 now established (2 sources).
3. Failed attempt in context: PARTLY CLOSED, contested. Verma 2026 (1.5B-7B): -6.1 and -6.9 points vs blind resample, near-copies 33-68%. Jha 2026 (24-32B) same direction for localized edits. Arimbur 2026 (8B-70B+, Gemini): self-repair matches or beats resampling for stronger models. No frontier reasoning model tested. Yang 2026 contamination model is theory with a two-number fit and has a heterogeneity rival explanation. New claim K23.
4. Randomised human trial / Calikli replication / PROMISE 2010: MOSTLY OPEN. No software trial, no external replication. Salman 2019 (N=42) replicates the positive-test tendency (86.5% confirmatory), not the logic link. PROMISE 2010 is the companion of the PPIG paper by the same group (abstract only; full texts blocked). Non-software: Branchini RCT, Sellier quasi-experiment (58.8% vs 72.2%, N=290). K14, K24.
5. Reasoning models and bias on a common probe: PARTLY CLOSED, still contested. AnchorBench CoT: lower plausible-anchor influence in 11 of 15 cells (mean -0.06), above zero in 13 of 15, higher in 4. Matches Kraishan null more than SynAnchors. No native reasoning toggle on a bias probe; Huang 2026 toggles reasoning on code correctness only. Takenami 2025 seen second-hand.
6. Leventhal 1994 and spec completeness: OPEN on numbers. Abstract only (bias in every condition, reduced by expertise and complete spec); Salman 2019 notes a different test labelling. LLM analogue from Haeri: incomplete spec cuts detection 30/30 to 6/30. K25.
7. Reference-class base rate vs optimism: OPEN. No study. Jhang 2026 shows direct base-rate use near ceiling on frontier models. K28.
8. Framing words vs stated confidence: OPEN. Only effort-estimate request-format study (abstract). K27.
9. Axiomatic cues cost-benefit: PARTLY CLOSED. AnchorBench +Rule index 0.33 to 0.06 (vague judgment instruction 0.26); CogBias shows generic prompt debiasing backfires on judgment biases (-4.4%). Second source for K12 (now established). Still no cost or frontier-model code data.
10. Base vs instruct on falsification probe: OPEN. Nothing found; Failing to Falsify tests only post-trained models.

Counts: closed 0, partly closed 4 (2, 3, 5, 9), open 6 (1, 4, 6, 7, 8, 10). Claims: 22 to 28 (K23-K28 new); K02, K04, K12 raised to established; K10 reworded with AnchorBench numbers.

Caveats: Verma, Jha, Haeri, Ma, AnchorBench, Jhang are 2026 preprints or single-team results. d10, d11, d14, d21 and the Takenami figure are abstract-level or second-hand.
