# E13.09 Work and domain analysis: cross-check critique

Scope: evidence_a (28 lines), evidence_b (24), evidence_c (27). Claims: claims.jsonl (K01 to K20).

## Headline

The founding evidence (Rasmussen, Vicente, DURESS studies) was never opened by any agent. Everything on the human side rests on Wikipedia pages, secondary applications and one meta-review. On the LLM side, no study tests work domain analysis (WDA) or the abstraction hierarchy as an agent method. The nearest evidence is expert decision models (Wang 2024, Kopka 2026), one cognitive-work-analysis prompt recipe (Figueiredo 2025), layered memory (STRATA), and O*NET-based work benchmarks.

## Re-opened sources (numbers checked against the paper text this session)

1. Wright et al. 2019 (PMC6696941): 14/14 vs 13/22 (p<0.01), 17/20 vs 10/16 (p=0.15), 9/17 clinical vs 27/36 simulated. CONFIRMED. Extra: the EID comparison (making functional relationships visible) was tested and was not among the significant ones. The paper's figure says n=35 while the counts sum to 36; a one-case inconsistency in the source.
2. Wang et al. 2024 (arXiv 2310.10648): 700 conversations; entropy 6.00 / 3.37 / 3.42 / 3.37; +76% prefer, +80% useful on GPT-4; p<0.05 two-tailed t-test. CONFIRMED. Correction: expert decisions did not improve the "care" score for llama-2 and gpt-3.5-turbo.
3. Figueiredo 2025 (arXiv 2508.21209): d=0.225, CI [0.150, 0.300], t(2980)=6.16, F=37.90 partial eta2 0.012, IRR 0.004, z=-22.71, 1,200 simulated exchanges. CONFIRMED. Effect on gold similarity is small; the large effect is question count (a behaviour count the recipe asks for directly).
4. Kopka and Feufel 2026 (JMIR, abstract): 63.3 / 67.6 / 66.7; self-care 13.4 to 29.8 and 24.6; 45 vignettes. CONFIRMED. Added: only 2 emergency and 30 non-emergency cases; so 13 self-care vignettes.
5. STRATA (arXiv 2610.19386): Hermes 30.4/35.8 vs memoryless 62.8/66.9 on AppWorld Test-Normal; 48.3/55.8 vs 75.7/80.6 on ScienceWorld; 269 vs 201 nodes; 48.7 vs 23.3 injected lines; ablation row 70.6/50.8/41.0. CONFIRMED. Correction of emphasis: the authors state that on Test-Normal A-Mem leads STRATA by +0.4/+3.4 on Flash; STRATA's lead is on Test-Challenge, which they flag as confounded (scale, difficulty, application mix). Three seeds only; differences under one SD are not claimed.
6. GDPval (arXiv 2510.04374): 44 occupations, 9 sectors, 14-year average expert experience, 220 gold tasks, 47.6% win-or-tie for Claude Opus 4.1, +5 points from the prompt, 86% to 64% PowerPoint errors. CONFIRMED. The 47.6% counts ties.
7. TheAgentCompany (arXiv 2412.14161): 175 tasks; 30.3% completion / 39.3% partial credit for the best agent; Claude 3.7 26.3%, 3.5 24.0%. CONFIRMED with a version caveat: the paper table lists the 39.3% / $4.2 / 27.2 steps row under OpenHands 0.28.1 and the 30.3% / 34.4% / $6.3 row under OpenHands 0.14.2, so partial credit 39.3% and completion 30.3% may come from different harness versions. Treat them as separate results.
8. WORKBank (arXiv 2506.06576): 1,500 workers, 844 tasks, 104 occupations, 52 AI experts, 46.1%, 41.0%, 47.5%. CONFIRMED. Correction: 45.2% is the share of OCCUPATIONS with H3 dominant, not of tasks. The evidence line c17 phrased this correctly; the percentages H3 45.2 / H2 35.6 / H4 16.3 / H1 1.9 / H5 1.0 were not re-checked beyond the 45.2.
9. Zhang 2024 AR-HUD (b05): the text says "3 of 5 scenarios" while the numbers listed name S1 and S4 as not significant. Not re-opened; the number split (S2, S3 significant; S1, S4 not) leaves S5 as the third. Claim K03 uses "3 of 5".
10. Not re-opened (no time or no open source found): Morice 2021 (b04, F values), Chang Lee 2026 quantum chemistry (c11; arXiv search returned a different paper), Handa 2025 (c18, c19). K06 labels the c11 figures as not re-verified.

## Contradictions and tensions

- Wright 2019 finds EID-style relationship display NOT a significant predictor; Zhang 2024 and Morice 2021 report benefits. Both can be true (simulator, novice, small n), but then the design framework is confounded with other design choices (b05 limits say so).
- Wang 2024 says a self-chosen decision path helps strong models; Kopka and Figueiredo give fixed expert recipes. No study compares given vs self-generated analysis at equal tokens.
- STRATA: layered memory beats flat, but on Test-Normal A-Mem (linked flat memory) is as good or better on Flash. The "abstraction helps" claim is partly benchmark-dependent.
- Prompt-level work scaffolds: GDPval shows +5 points from a generic verify prompt; Kopka shows +4.3 points from reasoning-strategy prompts. Neither isolates WDA content from "more reasoning text".

## Weak spots

- Founding studies (a04, a05, a24, a25, b18 to b22, c27) were not opened. Their numbers are missing. Several snippet-only lines (b18, b19) were not turned into claims, except K16 and K17, flagged single-source.
- Three of five LLM-side positive results use human or LLM raters in one domain each; none controls for prompt length.
- Evidence lines a01 to a03, b10 are Wikipedia only (opened, but a secondary source).
- Application papers (a10 to a13, b11 to b15) report constraints coverage but no outcome measure; they show WDA is usable, not useful.
- K02 (absence of LLM tests) rests on the same few search engines; absence in 2026 literature search is not proof.
- Independent_sources counts treat a paper and its citation of the same study as one.

## GAPS (most decision-relevant first)

1. Does an abstraction-hierarchy S0 prompt (purpose, abstract function, general function, physical function, physical form, with why/how links) beat a plain or goals-and-constraints-only S0 gate at equal tokens, on mixed problem classes? Nobody has measured this.
2. What did Pawlak and Vicente (1996) and Christoffersen et al. (1996/1997) measure on DURESS II: N, conditions, effect sizes, especially for novel faults, and did anyone replicate or fail to?
3. Is the benefit of expert decision scaffolds a content effect or a length effect? Need a length-matched generic-advice control (Wang 2024 has none; Kopka has none).
4. How much harm comes from a wrong problem-class label at the gate (Wang's random decisions gave -97%), and how often do LLMs mislabel classes when self-generating the analysis?
5. Do analysts (or LLM samples) agree when assigning facts to abstraction levels? No inter-rater figure was found for human WDA either.
6. Does the Wright 2019 pattern (simulated gains larger than clinical-trial gains: 75% vs 53%) have a counterpart for scaffolds, i.e. benchmark-to-deployment shrinkage?
7. Which later reviews (McIlroy and Stanton 2015 is the one named, unopened) summarise EID effect sizes across domains, and what is the pooled effect?
8. Chang Lee and Rondinelli 2026 (decision-ladder agent, 24.9% to 44.1% coverage): confirm the numbers and the baseline fairness; the arXiv listing was not found.
9. In work-task benchmarks (TheAgentCompany, GDPval), do failures cluster on problem-class misreading or on execution? A failure taxonomy keyed to the work-domain levels does not yet exist.
10. When should the agent ask the human rather than act (WORKBank 47.5% mismatch)? No agent-side test of a desire-versus-capability gate exists.

## Gap search results

Evidence in evidence_d.jsonl (d01 to d18); claims K17, K02, K05, K07, K14 updated; K21 to K26 added. Web search was limited (Semantic Scholar, OpenAlex and arXiv APIs returned 429 much of the time; publisher and core.ac.uk PDFs returned 403), so the founding DURESS papers were read at abstract level only.

- Gap 1 (AH prompt vs plain/goals-only at equal tokens): STAYS OPEN. No such test. Nearest are Step-Back (one abstraction level, MMLU chem +11, TimeQA +27, d13) and Self-Discover (T4D 69% vs 40% CoT on PaLM 2-L, d14); neither is a five-level hierarchy or length-matched.
- Gap 2 (Pawlak/Vicente, Christoffersen): PARTLY CLOSED. Direction found, numbers not. Christoffersen 1996: little difference in average, but P-only group up to 2x slower at times even after 5.5 months (d01); 1995 report: faster detection, more accurate diagnosis (d02); Pawlak 1996 found a P+F deficiency (history information) (d04); a critique was printed (d05). No replication found. K17 now "contested". N and effect sizes still unobtained.
- Gap 3 (content vs length): STAYS OPEN for scaffolds. Length alone hurts (0.92 to 0.68 at 3000 tokens, d09); filler gives commercial LLMs nothing (d10); so a content effect is plausible, but no length-matched scaffold control exists. Self-Discover is the nearest self-vs-given case.
- Gap 4 (wrong class label harm): PARTLY CLOSED. Models label ambiguity near chance (50 to 54% accuracy, d15). Harm from a wrong label is still only Wang's -97% (random decisions).
- Gap 5 (inter-rater agreement for WDA): STAYS OPEN. None found for humans (d18); Reising and Sanderson call display mapping open-ended artistry (d08). MAST's human kappa 0.88 (d11) is a model for the test.
- Gap 6 (benchmark-to-deployment shrinkage): PARTLY CLOSED by analogy. METR trial: forecast 24% faster, measured 19% slower (d16). No scaffold-specific counterpart.
- Gap 7 (pooled EID effect): STAYS OPEN. McIlroy and Stanton 2015 reviews applications, not effects; 40% omit SRK (d07). No pooled estimate found beyond Wright 2019.
- Gap 8 (Chang Lee and Rondinelli): STAYS OPEN. Paper not found (d17); K06 figures remain unverified.
- Gap 9 (failure clustering): PARTLY CLOSED. MAST: spec/design 41.8%, coordination 36.9%, verification 21.3%; role-spec fix +9.4% (d11, d12). Step-Back and Self-Discover residual errors are mostly in execution (over 90%; 74.7%). No taxonomy keyed to work-domain levels. Nothing for TheAgentCompany or GDPval specifically.
- Gap 10 (ask vs act gate): PARTLY CLOSED. CLAMBER shows weak ambiguity detection and low-quality clarifying questions (d15); MAST FM-2.2 (proceeding without asking) is 6.8%. No agent-side desire-versus-capability gate test.

Unconfirmed in this pass: all DURESS N and effect sizes; Pawlak and Maddox texts (opened=false); Zhang 2024 AR-HUD "3 of 5".
