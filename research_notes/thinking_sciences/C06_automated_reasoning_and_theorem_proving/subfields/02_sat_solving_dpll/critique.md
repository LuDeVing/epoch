# Critique: SAT solving, DPLL (C06.02)

Cross-check by re-opening full PDF text this session (scratch on D:, deleted afterwards).

## Numbers re-opened and confirmed
1. SATBench (arXiv 2505.14615), Table: o4-mini 89.3 overall, hard SAT 91.1, hard UNSAT 65.0, hard 78.0; DeepSeek-R1 87.8; Claude 3.7 hard UNSAT 42.1, overall 74.8; average hard 53.0, hard SAT 66.7, hard UNSAT 39.3; error shares 68.7 / 40.5; 60.4% corrected for o4-mini. Confirmed.
2. Selsam and Bjorner NeuroCore (1903.04671): 205 vs 187 solved; rand-glucose solved the same as neuro-glucose on SATCOMP-2018; on scheduling rand-glucose 2.5% fewer, neuro-glucose 20% more. Confirmed.
3. Zhang et al. 2026 (2605.28602): GPT-5 ADR 0.79 at 25 variables, 0.35 at 50 with about 20% completion; precision 0.78 / recall 0.76 / F1 0.77 / accuracy 0.77 but ADR 0.60. Confirmed.
4. Hazra et al. 2025 (2504.03930): about 5000 formulas, D4 model counts, accuracy "drops to ~10%" in the hard region. Confirmed.
5. SATLUTION (2509.07367): 347/345/344 vs 334/331 on the authors' runs; official 327/321. Confirmed.
6. NeuroBack (2110.14053): 193/197/203 and 198/190/204; +5.2%, +3.0%, +7.4%. Confirmed.
7. Pythagorean triples (1605.00723): 4 CPU years, 21,900 + 13,200 CPU hours; F7825 reduced to 3745 vars and 14672 clauses. Confirmed.
8. SatLM (2305.09656): GSM-SYS 69.4 / CoT 46.5 / ProgLM 43.4, LSAT 35.0 / 23.5, BoardgameQA 79.4 / 60.7, ProofWriter 99.7, SoTA 37.4 and 80.7. Confirmed. Note the "SATLM 69.4" and "SATLM 71.8" columns are different datasets; no mixing found.
9. NeuroSAT (1802.03685): 85% classification, 70% decoded, 25% on SR(200), 100% NeuroUNSAT, 98% cluster. Confirmed.
10. Chaff (DAC 2001): one to two orders of magnitude; SATO aborted 32 of the first 41 on SSS-SAT 1.0. Confirmed. LBD (IJCAI 2009) only partly re-checked (the 1827 and 2452 usage counts appear; MiniSat variant solved counts were not re-read).

## Corrections
- a16: "full trace correct 99.1% to 100%" holds only for the Random-distribution rows. Marginal and skewed rows go down to 86.06% (Pan et al. table), as c12 says. Use c12 for the range. The 99.8% or higher SAT/UNSAT accuracy is the stated overall figure; the top row values read 99.81-99.99 for Marginal.
- a01/a02: the DLL year is 1962 (CACM); the Wikipedia intro saying 1961 is wrong or loosely worded.
- a13/c14 say GPT-4 "SAT Translate about 100%" is with MiniSat as the solver; this measures translation plus a trusted solver and is not LLM reasoning.
- b11 vs c08: both consistent (o4-mini hard is 78.0 combined, 91.1 SAT, 65.0 UNSAT). No error.
- a19 says "More than 2,700 formulas"; the claim of "all models except GPT-5 near 0.5 past 25 variables" is from c17 and was not re-verified line by line.

## Contradictions between sources
- Hazra 2024/2025 report an easy-hard-easy LLM curve (accuracy dips to about 10% at the threshold). Zhang et al. 2026 report that most models do NOT show this shape and instead label nearly everything SAT; only GPT-5 follows it. Causes are probably different formulas (n at most 10 vs 25-75 variables), different tasks (search for assignment vs decide), and different models. Claim K05 is therefore marked contested.
- Hazra says R1 is robust and flat; SATBench shows R1 83.6 on hard UNSAT yet 44.7% of its errors are context inconsistency, and Zhang says reasoning models collapse past 25 variables. Robustness depends on size.
- NeuroCore: the original abstract (+10 to 20%) versus the authors' own later correction (random logits do as well on SATCOMP). The headline is not safe.
- SatLM versus Logic-LM: SatLM wins on every set; Logic-LM loses on PrOntoQA with GPT-4 (83.2 vs 98.8). Solver gain is not universal.

## Weak spots
- Almost all LLM-SAT evidence is on tiny random formulas (n at most 10 in Hazra, up to 75 in Zhang). CDCL's strength is on structured industrial instances; nothing tests an LLM agent there.
- SatLM numbers are from code-davinci-002, an old model; the gain for current models is not measured here. No evidence file gives a current-model replication of SatLM at equal tokens.
- No study compares a scaffold with the same token budget on SAT tasks. All LLM studies report accuracy, not accuracy per token.
- Many claims count one paper repeated in files a, b and c (SATBench, Zhang, Hazra, NeuroSAT, SatLM). I counted distinct papers for independent_sources. Hazra 2024 and 2025 are one group; Zhang and SATBench are independent.
- AutoSAT / AutoModSAT / SATLUTION are author-reported on their own hardware; SATLUTION's official numbers differ (327/321 for the baselines vs 334/331).
- NeuroSAT/NeuroBack/QuerySAT relevance to a prompt-only scaffold is indirect.

## Seen only in snippets or secondary sources
- a01, a02, a03, a04: Wikipedia only. a23 (Mitchell, Selman, Levesque 1992), a24 (Cook 1971), a25 (GRASP), a26 (MiniSat paper) not opened. 
- b25 DaSAThco exact PAR-2 not extracted. c19 ZebraLogic, c20 AutoSAT, c23 Schidler and Szeider, c24 Utsho et al., b21 QuerySAT, b07/b08 Graph-Q-SAT, b09/b10 G4SATBench, and Logic-LM c05-c07 were not re-opened in this cross-check; they rely on the first-pass readings.
- Ding, Sly, Sun (a22): journal year from memory.

## GAPS
1. Does a prompt-only scaffold (unit propagation by code, explicit decide/backtrack trace, certificate check) beat plain CoT and best-of-N on random 3-SAT near alpha 4.27 at equal tokens? No study measures this.
2. Does a current frontier model (not code-davinci-002) still gain from SatLM-style declarative formalisation plus solver on LSAT, BoardgameQA and GSM-SYS, and how big is the gain per token?
3. How often does the translation step (NL to CNF/constraints) fail, and does the failure rate hide the "about 100%" translate-and-solve result on real tasks? Need the executable and faithful-formalisation rate on our own problems.
4. How large must a formula be before direct LLM reasoning fails for reasoning models (R1, o4-mini, GPT-5), and does it fail by size alone or by token budget? Zhang shows GPT-5 completes only about 20% of runs at 50 variables.
5. How much of the satisfiability-bias error can be removed by a forced check (substitute the claimed assignment, or demand a core for UNSAT)? SATBench shows 60.4 to 73.2% corrected by naming the failures; is that a fresh-run effect?
6. Do LLM agents behave like DPLL (backtracking, unit propagation) or like greedy local search? Hazra says GPT-4o does greedy search; G4SATBench says GNNs do. Needs trace-level audit of a current reasoning model.
7. Is there an LBD-like cheap quality score for what the agent keeps in memory (learned lemmas), tested against keeping everything at equal context?
8. For LLM-evolved solver heuristics (AutoSAT, AutoModSAT, SATLUTION), what remains after comparing with equal-budget parameter tuning and on structured instances held out from the evolution set?
9. Do the UNSAT-side failures (hard UNSAT 39.3% average, below chance) improve with proof-style outputs (resolution or clause-learning traces) that an external checker validates?
10. Does the Hazra "reliance on solution count" shortcut appear in other logic tasks (ZebraLogic, SATBench), and does a random-control or paired-twin test remove it?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d16). Opened in full text: Verma 2607.17047, Wang et al. 2606.16118, Sun and Meel 2610.14402, AESAT (IJCAI 2026), Wang/Seggoju/Paschke 2026, SATQuest 2509.00930. Others are search-snippet only and marked opened:false.

Closed or partly closed
- Gap 2 (current models and SatLM): partly closed. For GPT-5, Gemini 2.5 Pro, Claude Sonnet 4 and DeepSeek-Reasoner the solver gain is under 1% on near-ceiling deduction sets, but solver pipelines retain 76.7% vs 62.2% at 14-17 steps (d08). LSAT, BoardgameQA, GSM-SYS not re-run; accuracy per token not measured. K08 now contested.
- Gap 3 (translation failure): partly closed. In legal NLI the real Z3 pipeline beat plain LLM classification for only 1 of 5 models; scope laundering 15.3-52.5% (d04). Answer 91.2 vs formula equivalence 80.6 without a faithfulness reward (d05). Own-problem rate still unmeasured. K07 now contested.
- Gap 4 (size or budget): partly closed. Budget matters: all 28 non-abstained random-UNSAT rows hit a 16k cap (d02); density and conflict proxies do not order accuracy for three instruct models (d01). No R1/o4-mini/GPT-5 size sweep at a fixed generous budget.
- Gap 8 (LLM-evolved solvers): partly closed. AESAT held-out gain is about 1-2% vs 36.6% on training (d06); competition win claimed (d07). Still no equal-budget tuning baseline.
- Gap 10 (solution-count shortcut): partly closed for surface sensitivity (d03). ZebraLogic or SATBench twin tests not found.

Stayed open
- Gap 1 (scaffold vs CoT vs best-of-N at equal tokens): no study (d15).
- Gap 5 (forced check): no study; the SATBench grader checks only after the fact (d16).
- Gap 6 (DPLL vs local search trace audit): only qualitative remarks (d10) and a theory/training paper (d11); a 2026 trace-learning lead was not identified (d12).
- Gap 7 (LBD-like memory score): nothing found.
- Gap 9 (proof-style UNSAT outputs): SATQuest shows MUS tasks are hard (d09); no study of checked proof outputs improving accuracy.

Cautions
- SATQuest prose and figure disagree on GPT-4.1 and V3 scores; figure used.
- d12 is a lead without a title; do not cite.
- Several 2026 papers are preprints with small model panels.
