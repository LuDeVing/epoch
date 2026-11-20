# Critique: Limits of deliberate practice (A10.05)

## Numbers re-opened this session (full text via PMC)
Confirmed:
- Macnamara and Maitra (2019): best 8,224 h, good 9,844 h, less accomplished 4,558 h; best vs good t24=-0.93, p=.364, d=-0.38; good vs less accomplished t16.57=3.26, p=.005, d=1.33; group eta2=.26 (vs original 48%); teacher-designed 6,251 h, eta2=.23; weekly 22.69 vs 30.65 h, p=.024, d=-1.03. (a14, a15, b15, b16)
- Hambrick, Macnamara, Oswald (2020): corrigendum values 14 / 24 / 23 / 20 / 5 / 1; Ericsson rejected 87 of 88; r .54 to .78, 61% of reliable variance; sensitivity table 0.93 (87.1%) at .60/.60, 0.70 (49.0%) at .80/.80, 0.62 (38.7%) at .90/.90. (a10, a11, b21)
- Ericsson and Harwell (2019): r=.54, CI .44 to .63, 29%; objective .49, relative .65; quoted 14% for Macnamara 2014. (a18)
- Mosing et al. (2024): 6,471 twins, 1,302 complete pairs, mean age 40.7, practice-ability r=.36, d=.77 and .78; genetic component unaffected by practice, relative heritability rose with practice. (a20, b19)

## Corrections made
1. Publication-version mismatch. The subfield row (26/21/18/4/<1, overall 12%) and b01 to b05 are the ORIGINAL 2014 values. The 2018 corrigendum gives overall 14% (r=.38 in the 2020 table, 14.4%), games 24, music 23, sports 20, education 5, professions 1. Both sets are real; claims K01 quote both. Do not mix them in one table.
2. The same applies to Macnamara et al. (2016): the 2020 table lists sports at r=.45, 20.3% (original text r=.43, 18%). The elite 1% is quoted by the 2020 paper itself, so it stands.
3. Burgoyne et al. (2016) also has a 2018 corrigendum (Intelligence 71, 92-96). The chess intelligence numbers (r=.24, Gf .32 vs .11) were read from the original and not rechecked against the corrigendum. Treat as provisional.
4. a15 and b16 agree. a14 says "original r=.70"; b15 says original 48% of variance. Consistent (.70 squared is about 49%).
5. a20 wrote that genetic variance stayed flat; the paper also says relative heritability INCREASED with practice, which is the stronger statement against the theory. K11 uses this.
6. Hambrick 2014 chess: a05 gives pooled uncorrected r=.33 and corrected .39 while b09 gives average corrected r=.57 (weighted .49). These are different quantities (pooled vs study-average); not a conflict, but they must not be compared directly.

## Contradictions between sources
- Definition war: Ericsson and Harwell 29% (61% corrected) vs Macnamara 14%. Mostly about which of 88 studies count and how reliability is assumed. Unresolved (K07).
- Music: Platz corrected r=.61 (37%) vs Hambrick 29.9% average. Different study sets and correction rules (K08).
- Study counts differ: Platz 13 studies in the abstract vs 14 effects in the 2020 table.

## Weak spots
- Hours are retrospective self-reports in most studies; reliability is assumed, not measured. The sensitivity table shows the headline share can be 49% or 87%.
- The authors of the key papers (Macnamara, Hambrick, Oswald; Ericsson) are interested parties on both sides. Few independent re-analyses.
- Range restriction at the elite level lowers r; the 1% elite figure (6 effects, N=228) may partly be this. Including one excluded effect moves it to 8%, still not significant.
- Twin studies measure auditory discrimination, not performance.
- Almost all the LLM evidence (c01 to c27, a25, a26) was read at abstract level only. No LLM study tests deliberate-practice limits directly; all LLM claims are analogies and carry status single-source or contested.
- a24 (AI-assisted practice) has no objective logs.

## Only seen in snippets or abstracts
b18 (Mosing 2014 twins), b26 (Barth 2022 sports), b27, a13, a26, b24 (Campitelli and Gobet press release, journal 403), a09 original paper (corrigendum values seen through the 2020 paper), and nearly all c lines.

## GAPS
1. Does a scaffold loop that adds practice-like iterations (retry with a targeted check) show a dose-response curve at equal tokens, and where does it plateau? No direct study exists.
2. Which tasks fall in the high-predictability band (24%) vs low (4%) for an LLM, and does routing on predictability beat a fixed loop? Predictability was only coder-rated.
3. Does the elite-level 1% result survive range-restriction correction, and is there an analogue (best-of-N adds nothing on the hardest items)?
4. What exact numbers does the full Macnamara 2014 corrigendum report per moderator (practice method, performance method, predictability)? Only overall and domain values were verified.
5. What do the full texts of SCoRe, Self-Refine, Reflexion, Huang 2023 and Kamoi 2024 show at equal tokens, with baselines matched? Only abstracts were read.
6. Does transfer from practice on one task family to another hold against active controls for LLM scaffolds (far-transfer analogue of Sala and Gobet 0.03 SD)?
7. Are Burgoyne 2016 chess intelligence figures changed by the 2018 corrigendum?
8. Is Campitelli and Gobet 2011 sample and the "3,000 vs 30,000 h" spread reproducible from the journal text?
9. Do independent (not Macnamara/Ericsson) re-analyses exist for the 88-study set and the Ericsson-Harwell 14-study subset?
10. Does the junior-vs-senior pattern in sports (Barth 2022) have a counterpart in agent runs, i.e. do early-iteration gains mispredict final-budget quality?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d18). Claims K20 to K25 were added; K02, K07, K09, K10, K12 to K18 gained evidence ids.

Closed or mostly closed:
- Gap 5 (full texts). Closed. Huang 2023, Olausson 2023, Self-Refine, Reflexion, SCoRe and Kamoi 2024 were read in full text (d01 to d06). Intrinsic loops give flat or negative change (GSM8K 75.9 -> 74.7 over 5 calls; SCoRe base second attempt 41.4% vs first 52.6%). Self-Refine per-iteration gains shrink but are not budget-matched.
- Gap 1 (dose-response at equal tokens). Mostly closed as analogy. No direct study. Closest: self-repair is no better than resampling at equal budget (d02); sequential extra thinking flattens near 6x (d09); verified resampling keeps rising, 15.9% to 56% from 1 to 250 samples (d07). New claims K20, K21.
- Gap 2 (predictability routing). Partly closed. Snell 2024 shows difficulty routing beats a fixed best-of-N with about 4x less compute (d08), but the difficulty is model-estimated, not coder-rated. K22 is single-source.
- Gap 3 (elite tail analogue). Partly closed. Snell: no method progresses on the hardest bin; Yue 2025: base model matches RL model at large k (d10). The human range-restriction correction was not found; the 1% elite figure still has that doubt.
- Gap 6 (far transfer for LLMs). Partly closed. Huan 2025 (d11): math gains mostly do not transfer; RL transfers, SFT does not. This is weight training, not a scaffold, and no scaffold test with active control exists. K23.
- Gap 8 (Campitelli and Gobet). Partly closed. The spread is 3,016 to 23,608 h (N=104, 34% of variance, mean to master 11,053 h) from the 2007 data via a 2008 note (d12). The 2011 journal text was not available; the "3,000 vs 30,000" wording should be replaced by the exact figures.
- Gap 9 (independent re-analyses). Partly closed. Debatin et al. 2023 (N=178 chess) is an outside group with new data supporting the individualization reading (d14, K24). No neutral re-run of the 88-study set or the 14-study subset was found; the debate remains author versus author (d16).

Still open:
- Gap 4 (Macnamara 2014 corrigendum per moderator). The SAGE page is blocked (403); only domain values are verified (d17). Keep the 4/12/24 predictability split labelled as original 2014.
- Gap 7 (Burgoyne 2016 corrigendum). Elsevier page blocked (403) (d18). Keep r=.24 provisional.
- Gap 10 (early-iteration gains vs final-budget quality in agent runs). No source found. Indirect hint only: Self-Refine non-monotone tasks and Huang 2023 later rounds worse than round 1.

Caveats on this pass: most arXiv papers were read by section search with pdftotext, not line by line. Huan 2025 and Yue 2025 numbers beyond the abstract are from figures or key sections only. The Rubik's-cube paper coefficients were not extracted (d15).
