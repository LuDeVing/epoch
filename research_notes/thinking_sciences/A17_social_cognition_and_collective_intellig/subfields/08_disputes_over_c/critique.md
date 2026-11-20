# A17.08 Disputes over c: cross-check critique

## Sources re-opened this session (full text) and result
1. Riedl 2021 correction (PMC9171794): AVE 44% -> 19.6%, loadings 0.27 to 0.52 unchanged. CONFIRMED.
2. Rowe, Hattie, Hester 2021 (PMC8019454): c to criterion r=.26 (CI .10 to .40), 8 samples, N=857, Q(8)=59.36, I2=86.5%, tau2=.05. CONFIRMED.
3. Rowe 2021: 163 of 171 inter-task correlations positive (95%); 59% between 0 and .30. CONFIRMED.
4. Rowe 2021: mean AVE 30.23% across 49 loadings; mean first factor 43.03%, mean c to criterion .253 (table row). CONFIRMED.
5. Rowe 2021: about 80% power statement; 84 to 782 groups needed for r=.30 to .10. CONFIRMED.
6. Zhou 2026 (ACL Findings PDF): r=0.55, first factor 66.3%, second 18.7%, CFI .967. CONFIRMED.
7. Zhou 2026: cost 75% higher, ACI 9.7% lower for the dearer group. CORRECTED (see below).
8. Zhou 2026: improvement up to 12.3% in table. CONFIRMED.
9. Riedl 2025/26 arXiv 2510.05174: OR 0.92 per agent, OR 1.50 per temperature unit, 7,150 runs, 200 runs x 3 conditions, no significant difference. CONFIRMED.
10. HiddenBench arXiv 2505.11556: GPT-4.1 pre 0.008, post 0.233, full 0.733; humans 0.385 vs 0.604; 65 tasks. CONFIRMED.
11. Ilic and Gignac 2024 (arXiv 2310.11616): 591 LLMs, 65.6%, chi2(44)=250.42, CFI .984, RMSEA .089. CONFIRMED.
12. Zhang 2025 (arXiv 2502.08788): CoT average 72.5, SoM-Heter 76.7. CONFIRMED.

Not re-opened (primary text not obtained): Woolley 2010 numbers (checked only through Rowe's table: 43.4% and 44.1%, consistent with a02/a03), Bates and Gupta, Engel 2014, Barlow and Dennis, Credé and Howardson, Smit 2024.

## Corrections made
- a24 says one group "cost 75% more but its ACI was only 9.7% higher". Zhou's text and Figure 6 say the dearer group (stronger LLMs) had the LOWER ACI; the cheaper group was 9.7% higher. b20 and c10 had it right. Claim K14 uses the correct direction.
- a02 says Study 1 first factor "over 43%"; Rowe gives 43.4%. Fine, same figure.
- b09 says all Bates and Gupta studies had groups of 3. a13 says Study 1 had 26 groups of 2 to 4. Use a13 (Study 1 is 72 people in groups of 2 to 4).
- a18 reports Barlow and Dennis mean inter-task r=-0.05 with no factor, while b12 (via Rowe's table) gives a first factor of 42% with 50% of correlations positive. These are different outputs of the same data (a plain eigenvalue share is high even with near-zero correlations in small samples). Treat "no factor" as the authors' reading, "42%" as Rowe's computation.
- Source labels: a09, b07 and c02 are the same correction note; they count as one source, not three.
- Year label on Riedl "emergent coordination": a26 says 2025, c12 says 2026 (ICLR). Same paper (arXiv 2510.05174).

## Key arithmetic point
A standardized loading of at most 0.52 means a squared loading of at most 0.27, so an AVE of 44% could never come from loadings in 0.27 to 0.52. The correction to 19.6% fits the loadings. Rowe's own AVE (30%) and the 43% first-factor share measure different things; papers mixing them overstate how much of group performance one factor explains.

## Contradictions between sources
- Member intelligence and c: Woolley r=.15; Rowe pooled .19 (independent .32, Woolley-affiliated .10); Bates and Gupta find group-IQ close to average IQ (beta .76). Older team meta-analyses (Bell, Devine, Stewart) pooled r=.28 for IQ and team performance, while Rowe finds .06 for the IQ-controlled subset against criterion tasks. No clean resolution.
- Social sensitivity: strong in Engel 2014 (r=.53/.55) and Woolley 2010 (female mediated by RME), absent in Bates and Gupta and weak in the 2025 dyad study.
- Credé and Howardson say no evidence for a factor in the six samples; Rowe's coding says 5 of 6 support one factor; the Woolley team's 2018 rebuttal was not read.
- Zhou finds LLM groups with first factor 66% vs human 43%; Ilic and Gignac find 65.6% across models. Both may mostly reflect shared underlying single-model ability, not group collaboration.

## Weak spots
- Almost all human c numbers come from one lab network (12 of 19 Rowe samples are Woolley-affiliated).
- Tasks are short lab tasks (typing, unscrambling, brainstorming) with small groups, student samples, and often low stakes.
- Riedl 2021's 8-task model fit is poor by usual standards (CFI .833) and the 3-task model is saturated.
- Every LLM c study found is one team (Zhou 2026), one framework (debate), under 10 agents. No independent replication.
- LLM multi-agent results are model-version specific (GPT-3.5, GPT-4o-mini, GPT-4.1); they age fast.
- Cost-controlled comparison (equal tokens) is mostly absent; Zhou notes cost only in one example.

## Seen only in snippets or metadata
- Woolley, Kim, Malone 2018 (a21, c07): metadata only, page returned 403.
- Credé and Howardson 2017 original paper (a19, c05): press accounts and Rowe's tables only.
- Burton et al. 2024 (c26): nothing obtained.
- Fan et al. 2026 (b24): abstract only.
- Kommol, Riedl, Woolley 2025 (b17): fit indices not on the page read.
- Woolley 2010, Engel 2014 and Barlow and Dennis figures are partly via Rowe's table.

## GAPS
1. Does a c-like factor survive in LLM groups when protocols other than debate are used, and with a cost-matched (equal token) baseline? Zhou 2026 used only the Du et al. debate setup.
2. How much of the LLM group factor is just shared single-model ability? Needs a factor analysis of the individual agents' scores on the same tasks versus the groups' scores.
3. What do Woolley, Kim, Malone 2018 and Credé and Howardson 2017 actually report (effort and nesting artifact tests), with exact first-factor values per sample?
4. Does ordinary multi-agent debate beat self-consistency at equal tokens on tasks where the c literature says process matters (information pooling like HiddenBench)? Results so far are mixed (Smit 2024, Zhang 2025).
5. Is there any randomised intervention that raised human c itself (not just a task), and did it transfer to held-out tasks?
6. Is a two-factor structure (for example speed/accuracy or convergent/divergent) better than one for LLM agent batteries, as Rowe 2024 and Graf 2019 found for humans?
7. Does the Kommol, Riedl, Woolley 2025 reanalysis report new fit indices that change the 19.6% AVE story?
8. Do the hidden-profile failures of LLM groups (0.233 vs 0.733) respond to a scaffold that forces private-fact disclosure, with a token budget fixed?
9. Do independent labs replicate c-to-IQ r=.32 versus Woolley-lab .10, and what task and sample features explain the difference?
10. Is the plug-in gain from ACI (average 4.6%, up to 12.3%) larger than the noise across seeds, and does it hold for other optimisers?

## Gap search results (evidence_d.jsonl, d01 to d19)

Closed or mostly closed
- Gap 4 (debate vs self-consistency at equal tokens): answered as "mixed, leaning against". Wang 2024, Tran and Kiela 2026, Hu 2026 and Bertalanic 2026 find no gain or a loss at matched budget; Wunderlich 2026 finds debate +1.3 and mixture-of-agents +2.7 points over SC at equal FLOPs on MMLU-Pro and BBH. K18 now "contested".
- Gap 8 (hidden profile and a disclosure scaffold): HiddenBench v3 shows Reveal-All 0.967 vs 0.233 baseline, a passive secretary 0.100, one dissenter 0.492. Token cost per arm is not reported and Reveal-All is an oracle, so "does it hold at fixed tokens" is still unmeasured. New claim K22.
- Gap 6 (two factors), human side: Graf 2019 (745 teams, one-factor CFI .73, first factor 17%), Rowe 2024 (N=85, two-factor), Kommol 2025 (three-factor). K11 updated. LLM-battery side not found.

Partly answered
- Gap 5 (intervention that raised c and transferred): randomised studies exist (Woolley 2022, 146 teams; McDonald 2026; Gupta 2024 nudges) but none shows a transferred rise in c. Feedback on effort hurt. K20 updated.
- Gap 10 (ACI gain vs noise): Table 1 is one run per cell, no CIs; cannot be judged. K15 notes this.
- Gap 3: only press coverage of Credé and Howardson (low effort and nesting arguments) and a summary of the 2018 reply were obtained; no per-sample first-factor values.

Still open
- Gap 1 (c-like factor with non-debate protocols and cost-matched baseline): no independent replication found; Zhou used debate only.
- Gap 2 (group factor vs shared single-model ability): the needed control is absent from Zhou's paper (K21).
- Gap 7 (Kommol reanalysis fit indices): only the abstract was read (22 studies, 5,279 individuals, 1,356 groups; three-factor best). Nothing on AVE.
- Gap 9 (independent labs on c-to-IQ): no new data.

Caveats on this pass
- d11, d17, d18, d19 are marked opened:false (search summaries or registry text only).
- d09 notes that the extracted G-Designer rows in Zhou's Table 1 are mislabelled; only the stated percentages were used.
- The earlier note that HiddenBench full-information accuracy was 0.733 and humans 0.604 stands; v3 headline of 30.1% vs 80.7% is across 15 LLMs.
