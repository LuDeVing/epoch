# D07.08 Critique: Integrated HPS and the method of case studies

## Numbers re-opened this session (cross-checker)
Confirmed against the paper text or abstract (arXiv/NBER, 2026-11-10):
1. Si, Yang, Hashimoto (2409.04109): novelty 4.84 human (119 reviews), 5.64 AI (109), 5.81 AI reranked (109); 49 writers, 79 reviewers, 298 reviews; reviewer agreement 56.1% vs 66.0% NeurIPS 2021; 4000 seeds, only 200 non-duplicates. Confirmed. Extra: ICLR 2024 agreement 71.9%. Abstract says p < 0.05 (b12 says p<0.01 for one test; both can hold, but cite p<0.05 for the headline).
2. Azoulay et al. (NBER w21788): 452 stars, 3,076 subfields, 31,142 control subfields (34,218 total), +8.6%. Confirmed. Added nuance: effect comes mostly from early deaths; older stars give a small, imprecise effect (Appendix E). The paper's text says earlier work covers collaborators only.
3. FIRE-Bench (2602.02905): F1 46.7 Claude Code (Sonnet-4), 41.9 Codex, 37.9 and 31.9 OpenHands, median CV 0.37, false positives 76.4-95.0% contradictory/unrelated, alternatives 4.5-10.9%, cutoff table. Confirmed. Note 31.9 appears twice (o4-mini average and o4-mini medium-task score): a coincidence, not an error.
4. ScienceAgentBench: 32.4%, 34.3%, 42.2% (o1-preview), 102 tasks, 44 papers, nine experts. Confirmed. The 42.2% is o1-preview, not an "o1 variant" (c08 wording), and costs over 10 times more.
5. LLM-SRBench: 239 problems, 31.5% best. Confirmed in abstract. The 28.1% LSR-Synth and direct prompting figures were not re-opened.
6. DiscoveryBench: 264 + 903 tasks, best 25%. Confirmed (abstract).
7. DiscoveryWorld: 120 tasks, 8 topics, 3 levels. Confirmed (abstract). The 38%/18%/66% figures not re-opened.
8. MOOSE-Chem: 51 papers after January 2024; no-contamination claim rests on model cutoff date. Confirmed. The 83.7% hit ratio not re-opened.
9. Memento (2508.16153): 87.88% GAIA val, 79.40% test, 66.6 F1 / 80.4 PM, +4.7 to 9.6 OOD, K=4 F1 64.5 PM 78.5. Confirmed. Detail: the 79.40% test score uses a case bank built from validation, so it is not independent of the validation run.
10. a01 (Pitt) remains unopened; only secondary quotes.

Corrections: no numeric errors found. Wording fixes: c08 o1 label; b12 p-value; a21 says all four agents about 34.2 or less on the bias task, not checked.

## Contradictions and tensions
- Planck's principle: earlier tests (Hull, Gorham, Levin) found little support; Azoulay finds an effect through outsiders. These are different outcomes (age of acceptance vs entry of outsiders), so they do not directly conflict. b04 (Hull 1978) was never opened.
- Contamination: FIRE-Bench says no consistent pre-cutoff advantage; LLM-SRBench says Feynman equations are memorised. Method differs (date split vs form change); form change is the stronger test. Medium gpt-5 44.5 to 23.1 shows small-n noise.
- Memento: case memory gains vs repeated-tries baseline (78.65 to 84.47) – gain over equal-attempt baseline is unclear.
- Si et al.: novelty up, feasibility not, and reviewers agree poorly; "better ideas" is not shown.

## Weak spots
- Core HPS evidence is philosophical argument (Pitt, Burian, Scholl, Herfeld, Chang). No measured test of the method of case studies exists in the opened sources.
- Many a-file LLM items are benchmarks, not tests of case use; the link to "treat cases as evidence" is by analogy.
- Several benchmark results come from one group per benchmark; "independent sources" counts for the discovery benchmarks (3) are three different groups but different tasks, so they agree in direction, not in measure.
- Memento, ExpeL and Sourati use "cases" as agent memory; this is related to, not the same as, HPS cases.
- Time-locked model papers are 2026 and report no rediscovery scores.

## Only seen in snippets or not opened
a01 Pitt, a08 VPI (Laudan et al. 1986), a09 Giere, a10 Hull, a11 Schickore, a14 Chang, a18 Kinzel, a19, a33, a34, b04, b09-b11, c19-c21 (Langley, Kolodner, Sauer and Scholl volume). The key book (Sauer and Scholl 2016) was not read.

## GAPS (most decision-relevant first)
1. Does a scaffold rule "tag every case as generative / refinement / justification, and flag justification claims resting on fewer than N cases" change an LLM's accuracy or calibration on claims backed by hand-picked cases, at equal tokens? No study found.
2. How strongly do LLMs favour confirming cases when asked to find supporting evidence (selection bias in case picking), and does a "seek the case that would refute" step fix it? Measure the rate.
3. What did the VPI programme (Laudan et al. 1986; Donovan, Laudan, Laudan 1988) actually find when it tested Kuhn, Lakatos and Laudan against many episodes: effect sizes, number of episodes, agreement between coders?
4. Does case memory (Memento-style) beat an equal-attempt repeat baseline when attempts and tokens are matched, and how many cases is best (Sourati says one, Memento says about four)?
5. Which contamination controls (form change, synthetic, date split, time-locked model) predict held-out scores best, and what is the memory share on FIRE-Bench-type tasks?
6. Do replication results exist for Planck's principle on other fields (physics, social science) and for Millikan/Mendel-type "too good" data claims that could serve as test cases for an agent's source check?
7. Do any LLM studies (2024-2026) measure whether models can reconstruct a historical discovery from period-only text (Kepler, Boyle, Darwin) and how closely they match the historians' accounts?
8. How reliable are LLM judges of historical case analyses; is there a rubric validated against historians (Zichert and Simons say there is no standard)?
9. Does Herfeld's network-analysis rule (explicit data, thresholds, repeatable case selection) improve an agent's case selection compared with free choice, measured by coverage of a known case population?
10. What is the actual size of Pitt's small-n problem in numbers: how many cases of how diverse a population are needed before a method claim stabilises (Burian says a few hundred are not enough, with no data)?

## Gap search results (gap searcher, 2026-11-10)
Evidence in evidence_d.jsonl (d01-d17); claims K04, K05, K07, K17, K20 revised; K21-K26 added. Search APIs (OpenAlex, arXiv) were rate-limited at times, so some items came from web search plus the paper PDFs.

- Gap 1 (scaffold rule tag/flag small-n, equal tokens): STILL OPEN. No direct study. Nearby: number-game papers (d13, d14) show LLM accuracy falls while confidence rises as examples accumulate, and LLMs under-generalise from one example. So hasty generalisation is not the default failure; growing overconfidence is.
- Gap 2 (confirming-case bias, refute step): MOSTLY CLOSED for hypothesis testing. Jhaveri et al. 2026: 11 LLMs confirm-first; prompts lift discovery 42% to 56% on average; works for thinking models, can hurt small non-thinking ones (d01, d02). Not yet tested on case picking from text.
- Gap 3 (VPI findings): PARTLY CLOSED. 250 hypotheses, 32 tested, 69-chemist example, five design flaws, limited impact (d03). Effect sizes and coder agreement not found; the 1986 and 1988 volumes were not opened.
- Gap 4 (case memory vs equal-attempt baseline; how many cases): PARTLY CLOSED. Empirical-MCTS beats repeated sampling (73.3 vs 70.0; 76.7 vs 56.7 plateau), Decocted Experience finds more items can hurt and distilled lessons beat raw cases, SpeedupLLM saves up to 56% compute only for similar questions (d09-d11). No strict token-matched case-bank study; Memento's gap to repeats unresolved.
- Gap 5 (contamination controls): STILL OPEN. Nothing new opened.
- Gap 6 (Planck replications, Millikan/Mendel): CLOSED for coverage. Hull et al. 67 scientists, 39.6 vs 48.1, under 10% variance (d04); Perrin 69 chemists, disconfirmed (d03); Cheng and Weinberg hump shape (d06); Millikan 58 of about 100-175 drops with little effect on result (d07); Mendel p about 0.99993, bias model (d08). Physics or social-science Planck replications not found.
- Gap 7 (period-only reconstruction): STILL OPEN. Only the GPT-1900 anecdote and a style study, both seen through summaries (d15, d16).
- Gap 8 (LLM judge reliability vs historians): PARTLY CLOSED. ProHist-Bench judge r = 0.77 on 50 items (d12); not for case-use analysis; no kappa.
- Gap 9 (Herfeld rule vs free selection): STILL OPEN. Only a press-reported caution (d17).
- Gap 10 (size of small-n problem): STILL OPEN. Critics give arguments, not thresholds; only the 10% Fahrbach figure (d05).

Opened with full text this session: d01-d02, d03-d05 (McAllister), d06 (front matter and abstract), d07, d08, d09, d10, d11, d12, d13, d14. Not opened: d15-d17 (summaries only).
