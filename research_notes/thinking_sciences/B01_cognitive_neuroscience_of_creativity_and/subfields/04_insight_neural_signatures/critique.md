# Critique, B01.04 Insight neural signatures (cross-check)

## Re-opened sources (full text, this session)
- Jung-Beeman 2004 (PMC387268): 0.25% / 0.30% peak, 531 mm3 with peak t=4.89, t(18)=3.47 p=.003, F(1,18)=8.11 p=.011, RT 9.94 vs 9.25 s, 10.25 vs 11.28 s. CONFIRMED.
- Kounios 2008 (PMC2293274): HI ratio 3.5 (SD 2.3), 70.0% solved, 56.1% insight, Beta-1 F(3,72)=7.011 p<.001, High-alpha F=4.811 p=.004. CONFIRMED.
- Sandkuhler 2008 (PMC2180197): 38.8% (SD 9.6), 302 vs 88 trials, gamma 38-44 Hz, rho=-0.39 t=-5.17. CONFIRMED.
- 2024 HBM EEG (PMC10789201): 57.4%, RT 8.4 s, Eureka 55.6% of correct, cluster -1.96 to -1.55 s, sum(t)=1174, p=.01. CONFIRMED.
- Chi and Snyder 2011 (PMC3032738): 60% vs 20%, p=.022, logrank p=.008. CONFIRMED.
- Illusion of Insight (arXiv 2601.00514): 6.31%, +8.41 pp (32.21 to 40.62; 50,574 vs 23,500), 2.57% vs 16.44% N=723,200, kappa 0.726 / 0.79, strict detector 1.79%. CONFIRMED.

## Corrections
1. c01 says "11M+ traces". The paper says "1M+". Use 1M+.
2. a05: the paper text says the alpha burst (9.8 Hz, right posterior parietal) began approximately 1.4 s before the solution. The a05 window labels (-1.31 to -0.56 s) come from stat windows; quote the paper wording if reused.
3. a16 omitted that Eureka was also reported on 22.7% (SD 16.4) of incorrect trials in the 2024 EEG study. The label is not tied to correctness.
4. Duplicate lines count as ONE source: a01/b01/b02, a21/b17 (N=38 from b17), a22/b18, a23/b23/c01-c04, a24/c10, a18/b16, b21/c14, b22/c18, b20/c16/c17, b24/c12.

## Contradictions
- Right vs left temporal: Jung-Beeman 2004 (right) vs Tik 2018 and the 2024 EEG (left). Alpha: increase over right posterior (Jung-Beeman) vs left central/temporal cluster (2024) vs a decrease in Kim 2026 (theory).
- Gamma: right temporal 0.3 s before response (Jung-Beeman) vs parieto-occipital at -1.5 to -1 s (Sandkuhler).
- tDCS: Chi and Snyder 2011 and the 2020 study positive; Aihara 2017 null (N=66).
- LLM Aha: R1-Zero reports (b24, c12) count reflection words and length as aha; 2601.00514 and Wu 2025 find real shifts rare and not helpful.

## Weak spots
- Founding numbers rest on N=13-26, self-report labels, and lenient or uncorrected thresholds (IFG p<.015; Kounios topographic t-maps).
- No independent replication of the right-T8 gamma burst was found.
- Several 2025-2026 LLM numbers are preprints, use LLM judges (kappa about 0.73), and test small open GRPO-tuned models.
- No LLM paper tests a neural signature. The bridge is analogy only (suddenness, fixation, verification).

## Seen only in snippets or abstracts (do not cite as numbers)
a25, a26, a27, a28, b11, b12, b13, b14, b15, c13, c23, c24, c25, c26. Figure values in c06 and c08 were not read; c19 table columns are partly unclear. a20, b13 and b14 are abstract-level.

## GAPS
1. Is there any independent replication (other lab, N>30, corrected statistics) of the right-temporal gamma burst before insight solutions?
2. Do LLM reasoning traces show a sharp confidence or entropy jump just before correct answers on RAT or riddle items, and does it predict correctness better than chance (an analog of the pre-solution gamma burst)?
3. In larger or closed models (not only GRPO-tuned Qwen/Llama), how rare are mid-trace shifts, and do triggered reconsiderations still help under high entropy at equal tokens?
4. Does a decoy-listing (fixation-break) step improve Only Connect or RAT scores at equal tokens, and by more than best-of-N?
5. Do the rare-shift and entropy findings of 2601.00514 transfer to insight-type problems (riddles, matchstick, RAT) rather than math, crosswords and Rush Hour?
6. What do Bowden and Jung-Beeman 2003, Kounios 2006 and Kounios and Beeman 2009 actually report (numbers)? They were never opened.
7. How much of the human insight-label rate (55-56%) reflects problem difficulty or solving style, given Eureka also appears on 22.7% of errors?
8. Do riddle verification failures come from checking or from generation, and does an independent checker model fix them (NazoNazo: 5-39% of wrong answers)?
9. Do the tDCS null results reflect real absence or low power, given task and montage differences?

## Gap search results
New evidence is in evidence_d.jsonl (d01-d17). Claims K17-K20 added; K01, K02, K06, K09, K10, K12 extended.

1. Independent replication of right-temporal gamma burst: STAYS OPEN. None found. Kounios 2006 said its gamma effects could not be separated from EMG artifact (d01). A 2023 perceptual EEG study (N=25, cluster-corrected) found no gamma difference (d09). Gamma tACS (Santarnecchi 2019, N=31) raised CRA accuracy but is a stimulation test, with some inconsistent p values (d07). The Sheth critique (post-solution gamma stronger) was seen only in a search snippet; its PDF could not be fetched.
2. Entropy or confidence jump before correct LLM answers: PARTLY CLOSED (negative). No RAT or riddle study found. Math evidence says correct traces are smooth and incorrect ones spike (d10). Untested on insight items.
3. Mid-trace shifts in larger or closed models: STAYS OPEN. 2601.00514 re-read: Qwen2.5 and Llama only; reconsideration gain flips sign by model (+5.97 vs -4.19 pp) (d11). The arXiv API was rate-limited, so no further paper was found.
4. Decoy-listing step vs best-of-N at equal tokens: STAYS OPEN. No test found. A boundary result: over-inventive reasoning causes 90.8% of LLM errors on literal riddles (d12).
5. Transfer of 2601.00514 to insight tasks: STAYS OPEN (d11 states math, crosswords, Rush Hour only).
6. Founding-paper numbers: MOSTLY CLOSED. Bowden and Jung-Beeman 2003 (N=44, 33 ms RH priming advantage, p=.04) (d03), Jung-Beeman and Bowden 2000 (d04) and Kounios 2006 (N=19 EEG, N=25 fMRI) (d01, d02) were opened. Kounios and Beeman 2009 could not be retrieved (d17, opened false); it is a review of the same primaries.
7. Aha label vs difficulty or style: PARTLY CLOSED. Aha tracks correct first moves and mindset (N=377) (d15) and late, slow, novel responses (d16); labels vary 8-14 SD points between people (d14). No quantitative split of difficulty vs style.
8. Riddle verification: STAYS OPEN. NazoNazo only proposes structured verification (d13); no independent-checker test found.
9. tDCS nulls, power vs absence: INCONCLUSIVE. Aihara g=-0.19 (CI -0.69 to 0.30) so small effects are not excluded; hard matchstick had 3 solvers (d05). Salvi 2020 positive but one-site, one-task, between-group sham (d06).

Notes: a source error found in this pass. The "Kizilirmak" attribution in a search summary is wrong; the gamma tACS paper is Santarnecchi et al. 2019.
