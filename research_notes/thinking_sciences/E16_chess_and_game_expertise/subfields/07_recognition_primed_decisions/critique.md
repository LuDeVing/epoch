# E16.07 Recognition-primed decisions: cross-check critique

Checked 2026-11-01. Sources re-opened this pass: Klein et al. (2010) abstract via Crossref, Chassy et al. (2023) PMC, Kopka and Feufel (2026) PMC, Vidulich and Tsang (2026) PMC text, Ruoss et al. (2024) full text Table 1, Karvonen (2024) full text, McIlroy-Young et al. (2020) full text, Hagendorff et al. (2023) full text, plus arXiv abstracts for Monroe and Chalmers, Transcendence, SwiftSage.

## Numbers re-checked

Confirmed exactly: Klein 2010 (26 commanders, mean 23 years, 156 decision points, under 12%, over 80%); Chassy 2023 (F(3,59)=14.558, eta squared 0.425, r=0.664, 44% variance, means 1.58/1.52/1.39/1.17, complexity F=34.271); Kopka 2026 (63.3 / 67.6 / 66.7%, OR 2.26 and 2.05, 13,500 assessments, GPT-4.1 self-care 0% to 43.8%, 88% over-triage); Ruoss Table 1 (all Elo and puzzle rows in b13, b14, c02, c04); Karvonen (99.8%, 99.6%, 46% vs 64%, probes 99.6 / 90.5 / 74.7, 2.6 times); Hagendorff (5%, 38%, 59%, 96%, 80%, 55%, 15%, 0%; 5% to 28%; 80% to 29%); Maia (46% minimum, over 52% maximum, Stockfish maximum 46%); Vidulich t(19)=6.54 d=1.39, t(19)=4.23 d=0.96, Kasparov 2750 to 2646, Moxley 45%/22%/25%, Burns 64-81%.

## Corrections

1. c06 "board-edit intervention success up to 92%" is wrong in kind. Table 2 reports the legal-move rate on a modified board: 41% without the intervention, 92.0% (16-layer) and 90.4% (8-layer) with it. It is not an edit-success rate.
2. c08 "Maia accuracy around 50.8% to 52.9% across bands 1100 to 1900" is imprecise. The text says the lowest Maia accuracy is 46% (Maia trained on 1900 predicting 1100) and the highest is over 52%. The 50.8 and 52.9 are two table cells.
3. c20/c21 Hagendorff: ChatGPT-4 is 96% correct in the Study 1 text and 95% in the Study 2 baseline and discussion (95% on CRT, 88% on semantic illusions). Different task subsets. Use 95-96%, and say which. The block-chain-of-thought drop (95 to 88%, p<.05) is confirmed; ChatGPT-3.5 unchanged (p=.49).
4. a09/b01: the group means 0.20 vs 0.27, 0.98 vs 1.45, 0.20 vs 0.38 and the winner/loser figures 0.15 vs 0.39 could not be found in the PMC text (tables stripped). The t and d values were confirmed. Treat the means as unverified this pass. "Higher in blitz for 18 of 20" was also not found in the text.
5. c11 vs Ruoss: Monroe and Chalmers list the 270M Ruoss model at 93.5% puzzles; Ruoss reports 95.4%. Different puzzle set or protocol. Do not mix the two numbers.
6. b16: the evidence line says internal search added 68 Elo at 100 simulations; the figure caption in the paper says "+300 Elo points even with a fairly limited search". Not reconciled (different tables or conditions). Neither should be cited alone.
7. a13 and a27: the emergency result rests on 2 vignettes. The headline gain is mostly from the 13 self-care vignettes. Wording in K12 now says this.

## Contradictions and weak spots

- Many lines repeat one paper: a09, a10, a26, b01-b06, b24 are all Vidulich and Tsang (2026); b10-b12 are one paper (Sunde); b13-b15, c01-c04 are one paper (Ruoss); b20 and c06 are Karvonen. Independent-source counts in claims.jsonl are therefore low, and "established" is rare.
- The founding 80% figure has never been checked here against any independent replication. Klein (2021) says it was replicated "several times" without citing; the sport studies (a15, a16) use RPD's own coding scheme, so they cannot refute it.
- Wikipedia (a04, a05) is a single-citation page with a needs-more-citations tag. It is the only source for "chess players use RPD". It carries no weight.
- The chess evidence mostly shows that intuition matters and that time pressure hurts; it does not test RPD's specific claim (one option, mental simulation of it, accept if it works). Connors et al. (b09) and Klein 1995 (a12, not opened) are the closest and are thin.
- Engine/transformer results (Ruoss, Monroe, Karvonen, Jenner) show fast pattern policies are strong, but they are trained on engine labels, not recognition by experience. Analogy to an LLM scaffold is loose.
- Only one LLM study (Kopka 2026) uses RPD directly as a prompt, with a small gain, one task, and no equal-token check. No LLM study found that tests RPD's failure on unusual cases.

## Only seen in snippets or abstracts

Klein 2010 (abstract only), Moxley 2012, van Harreveld 2007, Connors 2011, Monroe and Chalmers (abstract; table numbers from the earlier agent), Transcendence (abstract), SwiftSage and System-1.x switching numbers (earlier agent; System-1.x task not confirmed), Thinkless, DiLu, Voyager, Reflexion, Sunde 2022. Not opened at all: a02, a11, a12, a22, a23, a24, b25, b26.

## GAPS

1. Does the first-option, take-the-first heuristic beat later options in expert samples (Johnson and Raab 2003; Hepler and Feltz 2012)? Open and extract N, effect sizes and any failed replication.
2. Is there any measured boundary for RPD failure in atypical situations (novice vs expert share of recognition, Klein's "less than half"), with N and a source?
3. At equal tokens, does a fast first attempt plus a code check match a full multi-attempt scaffold on easy items, and where is the break-even difficulty? No LLM study found measures this with RPD framing.
4. What is the cheapest reliable signal for switching from recognition to deliberation (first-answer survival rate, margin between top two, agreement of two short attempts, stuck counter), and which has been tested?
5. Are there independent replications of the Klein 1985 80% finding outside firefighting that do not use RPD's own coding (e.g. ICU, military, aviation) with counts?
6. Does asking an LLM to simulate its single chosen option mentally before acting (RPD's step 3) add anything beyond naming the typical case? Any ablation.
7. Chess option generation: Klein et al. (1995) and Calderwood et al. (1988) numbers (not opened) on how many moves strong players consider and move quality under time pressure.
8. Reconcile the +68 vs +300 Elo search gain in Schultz et al. (2025) and the 93.5% vs 95.4% puzzle discrepancy (Monroe vs Ruoss).
9. Do retrieval-based or memory-based LLM agents (DiLu style) fail on out-of-coverage cases, and how does accuracy decay with distance from stored cases?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d27). Web search quota ran out during this pass, so papers were reached through PubMed, Europe PMC, arXiv PDFs and Semantic Scholar record pages. Publisher pages (Elsevier, JSTOR) returned 403 or no abstract.

| Gap | Status | What was found |
|---|---|---|
| 1 Take-the-first | Partly closed | Hepler and Feltz 2012 (N=72, TTF on 70% of trials, earlier options better), Hepler and Kovacs 2017 (N=68, no change under stress), Musculus 2019 (N=73 children), Haeusser 2014 (N=47), Laborde and Raab 2013 (replication, same lab), scoping review (8 TTF studies). One boundary case contradicts TTF order when no knowledge is involved (Chen 2025, N=98). Johnson and Raab 2003 could not be opened (abstract blocked); no effect sizes for any of these. No independent failed replication in an expert sample. |
| 2 Boundary of RPD | Partly closed | Best measured split: soccer referees N=60, experts .851 intuitive vs .835 analytic (n.s.), novices .643 vs .690 (analytic better, p<.05), style x level F(1,58)=20.09 (d09). Qualitative: pharmacists (N=12) go analytic on atypical items, residents (N=11) show premature closure. Klein's "less than half" for novices still has no source with N. |
| 3 Fast first + code check vs scaffold at equal tokens | Open (indirect evidence) | No RPD-framed study. Indirect: Snell 2024 (difficulty bins, easy items want sequential checks), Olausson 2024 (repair vs resampling at equal budget 0.97x-1.05x in quoted cases), Chen 2024 (first round correct in over 92% of cases), Large Language Monkeys (verifier is what makes sampling pay). Break-even by difficulty is only shown for MATH with a reward model. |
| 4 Cheapest switch signal | Mostly closed | Tested: agreement of samples (Adaptive-Consistency, 3.3x fewer samples, under 0.1% loss; ESC window unanimity, 33.8%-84.2% fewer), confidence weighting (CISC, over 40% fewer), stuck counter (SwiftSage, K13). Not useful alone: first-answer survival (self-check without feedback lowers accuracy, Huang 2024). No head-to-head comparison of the four candidates was found. |
| 5 Independent 80% replication | Open | None found. Non-fire RPD studies are qualitative and use RPD coding; the military paper (N=225) measures beliefs. |
| 6 Ablation of RPD step 3 | Open (nearest case only) | Kopka's RPD vs data-frame prompt: 67.6% vs 66.7%, overlapping CIs. Chain of Code shows real execution beats LM-imagined execution. No arm that adds only the simulation step. |
| 7 Klein 1995 and Calderwood 1988 numbers | Open | Both blocked (403 / abstract withheld). Only a second-hand note: 3 class B vs 3 masters, blitz vs 40 moves in 90 min, masters "seemed immune"; the source review calls the sample too small. |
| 8 Discrepancies | Closed, with one inference | Monroe's 93.5% is their own re-run of the Ruoss model (they plot puzzles rated 1000-3000; Ruoss 399-2867, 95.4%). Schultz: +68 is at 100 simulations; about +300 is reached at 500-2000 simulations by Table 1 (row pairing inferred from garbled PDF text, check the figure). |
| 9 Memory agents off coverage | Partly closed | DiLu: 70% to 35% success when moved from the home setting to a denser, wider one (10 scenarios each); RL fell 85%. Three settings only, so no decay curve. |

Claims changed: K08, K07, K16, K05, K12 (wording and evidence added); K17 and K18 rewritten with the new numbers; new K19-K23. K23 has zero independent sources by design (it records the missing replication).

Still needed: the full text of Johnson and Raab 2003, Klein et al. 1995, Calderwood et al. 1988 (library access); an LLM test with three arms (typical case only, plus simulation, plus real check) at equal tokens; a sample-based count of recognition vs comparison decisions in a non-fire domain that does not use RPD's own coding.
