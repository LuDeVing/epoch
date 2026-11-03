# Critique: D04.01 Argument standardisation and diagramming

Cross-check of evidence_a, evidence_b, evidence_c (79 lines). Claims are in claims.jsonl (K01-K26).

## 1. Numbers re-opened this session (from arXiv PDF text)

| Source | Numbers checked | Result |
|---|---|---|
| Stab & Gurevych 2017 (1604.07370) | 402 essays, 6,089 components, kappa .877/.635/.833, alpha .810/.524/.824, support .708, attack .737, human F1 .868, 95.2/87.9/80.5% | Confirmed |
| Niven & Kao 2019 (1907.07355) | 77% peak, 71% warrants only, "not" 61%, adversarial 53% (mean/median 50%), 5 of 20 seeds failed | Confirmed |
| Habernal et al. 2018 (1708.01425) | 1,970 instances, 173 AMT workers, 79.8% mean, 90.9% trained | Confirmed |
| Pirozelli et al. 2026 (2605.13793) | conclusion 92.50, span P/R/F1 80.31/72.87/75.70, relation 80.57, AbstRCT full span 59.65 / link 20.82 vs Morio 70.93 / 39.74, gold link 51.51, AAEC full link 0.41 vs 55.72 | Confirmed |
| Feng & Hunter 2026 (2608.18821) | Microtext: .426 with none, .512 with one, .555 at 4 steps | Confirmed (the ANLI/ARCT table is in a different paper and was not re-opened) |
| Castagna et al. 2024 (2412.15177) | Llama 3.1-70B reasoning 8.05 / 7.5 / 8.4, math 8.95 / 9.25 / 9.55; Nemotron-51B reasoning 6.75 / 7.7 / 7.3 | Confirmed |

### Corrections made
1. **b20 mislabels the human ratings.** The paper's Table 1 is column-shifted in the PDF text. The running text says implicit premises M=2.86 (agreement .95), undercuts 2.90 (.88), convergent/linked 2.85 (.80). b20 assigned 2.86 to "span", 2.90 to "conclusion", 2.85 to "relation", 2.96 to "structure" and 2.92 to "implicit premises". Use c03's reading (completeness 2.96, faithfulness 2.92). The span F1 / conclusion accuracy / relation accuracy values (75.70 / 92.50 / 80.57) are fine. These ratings are not accuracy against gold, only two annotators on 42 arguments.
2. **a15 and c12 are the same paper under two author lists** (Gampel et al. vs Pietron et al., same numbers). Counted as one source. Author names need a check.
3. **b19-b21 and c01-c04 are the same Pirozelli paper**, a16/a17/c20/c21 the same Feng & Hunter work, a12/b16/c10 the same Chen et al., a14/b14/b15 the same Gorur et al., a02/b01 etc. the same Stab & Gurevych. Independence counts in claims.jsonl treat each as ONE source. Most "established" claims therefore rest on only two or three real papers.
4. a12 dates Chen et al. 2023 and b16/c10 2024: arXiv versus venue year; same work.
5. Argument-mapping effect: a08 says about 0.8 SD, b27 says about 0.70 SD (Alvarez 2007 thesis), a08 snippet gives 0.34 for a typical course. These are not reconciled and no primary was opened (K24 marked contested).

## 2. Contradictions and tensions between sources
- Linked vs convergent: Stab & Gurevych say do not bother for structure identification; Pirozelli's pipeline has an explicit step for it and humans rate it 2.85/3. Both sides measure different things (parsing F1 vs plausibility ratings). No study measures whether the label helps a downstream answer.
- Pirozelli: strong on a small textbook set (42 arguments, mean 332 characters), near-zero link F1 on AAEC with exact spans. Even with gold components AAEC link F1 is 22.88, below the prior 55.72, so "bottleneck is span finding" (c04) is only half true.
- Feng & Hunter: more premise steps help up to 3 or 4, then drop at 5 on Microtext; ANLI keeps rising to 3. Different tasks, so no common optimum.
- Ku et al.: stance chosen freely helps, stance assigned hurts. Not seen elsewhere.
- CQoT: best in 18 of 20 comparisons, but CoT beat CQoT on Nemotron reasoning; judge is an LLM; steps cost tokens.
- Human ARCT 79.8% vs single zero-shot LLM 79.28% (Ku): the LLM already equals the human average. Niven & Kao show the benchmark has cues, so the LLM result may also be cue-driven; nobody ran the adversarial set on LLMs in the opened evidence.

## 3. Weak spots
- Almost all LLM studies measure extraction (F1, accuracy) or LLM-judged quality. None measures whether standardising an argument improves the agent's own downstream reasoning at equal tokens (K26). This is the key gap for S1/S2.
- Most key numbers sit in 2026 preprints and workshop papers, several by single author groups and not replicated (Pirozelli, Feng & Hunter, Ryu, Wang et al.).
- Gupta et al. (Toulmin prompting) success metric counted that the words claim/grounds/warrant appear, not that they were correct. Gold-warrant acceptability only 45.7%, kappa .18 to .31.
- Cabessa et al. compare with prior systems on the same corpus but with kNN examples chosen from training data of that corpus.
- Prompt format effects (de Wynter) mean a single reported number is fragile.
- Training-effect literature (argument mapping courses) is secondhand.
- Founding theory (Toulmin 1958, Freeman 2011, Johnson & Blair) was not opened (a19-a25 opened:false). Claims about them rest on citations in other papers.

## 4. Seen only in snippets or not opened
a19 Sviridova et al. 2025; a20 Toulmin 1958; a21 Freeman 2011; a22 Johnson & Blair; a23 Peldszus & Stede 2013; a24 Peldszus & Stede 2016 (counts via Feng & Hunter); a25 Twardy 2004 (403). The 0.34 SD figure and Alvarez 2007. Also not re-opened this session: Gupta et al., Ku et al., Ryu et al., Gorur et al., Chen et al., Glockner et al. (MISSCI), ArgBench, Cabessa, Wang et al. (Graphionale), de Wynter, Abkenar, Habernal & Gurevych 2017. Their figures are taken from the evidence files as written.

## GAPS (most decision-relevant first)
1. Does restating a claim with its grounds (S1/S2) improve downstream answer accuracy for an LLM agent at equal tokens, compared with plain CoT? No opened study tests this.
2. Do hidden-premise generation steps (1 to 5) help on non-benchmark reasoning tasks (math, planning, code), and is the peak at 3 to 4 steps stable across engines and authors?
3. Does a linked/convergent label change any downstream result, or only the diagram? Is the drop-one-premise test reliable when run by an LLM?
4. How do strong current LLMs score on adversarial ARCT (warrants swapped, claim negated), and how much of the 79% is cue use?
5. How much of the Toulmin critical-question loop's gain (CQoT) survives against a token-matched baseline such as sample-and-vote, and with a non-LLM judge?
6. Why is attack-link recall so low for LLMs, and does a dedicated counter-argument pass raise it without more false attacks?
7. Is the gold-span versus full-pipeline gap (Pirozelli) caused by span definition mismatch in the annotation or by genuine model errors; does it transfer to free-form agent text where there is no gold span?
8. What do the primary sources say on argument-mapping effects (Twardy 2004, Alvarez 2007, van Gelder 2015) and what is the replication record outside the Melbourne group?
9. Does restating a long argument (over 290 words, 9+ premises) hurt, and does chunking restore performance?
10. Do Toulmin-name prompts still get correct (not only present) claim/grounds/warrant with current models, and is naming Toulmin still better than naming Walton schemes?

## Gap search results

Evidence in evidence_d.jsonl (d01-d16, all opened this session). Search conditions: WebSearch budget was already used up, and the arXiv API, Semantic Scholar and OpenAlex returned 429. Work was done through arXiv listing pages, direct PDFs and Europe PMC full text. Claims K04, K05, K11, K22, K24, K26 were updated; K27-K33 added.

| Gap | Status | What was found |
|---|---|---|
| 1 Restating improves downstream accuracy at equal tokens | Open, narrowed | No direct test. Nearest: Toulmin-form training gave no accuracy gain over SFT-CoT (32.67 vs 32.14, d04); structure given to zero-shot LLMs gave F1 +0.012 to +0.030 (d05); argument-computed verdicts did not beat direct prediction (d11). Only TRACE ties Toulmin-shaped traces to accuracy (r=.741 across models; one RL run 77.86 to 84.69 on GSM8K, d03). Lean: structure buys inspectability, accuracy is unproven. |
| 2 Hidden-premise steps on math, planning, code; stability of 3 to 4 peak | Open | d10 re-read: only ANLI and ARCT, 1 to 3 steps, one engine, fixed candidates, AMR+SAT checker. Nothing on non-benchmark tasks. |
| 3 Does the linked/convergent label change downstream results; LLM drop-one test | Open, narrowed | Nothing tests the label. d05 shows extracted structure barely helps an LLM; d07 shows an LLM reviewer is unstable (6.2% verdict flips) so code checks should do structural tests. Drop-one-premise by LLM not measured. |
| 4 Adversarial ARCT with current LLMs | Open | arXiv search finds only 4 ARCT papers, none with an LLM on the adversarial set (d15). |
| 5 CQoT vs token-matched baseline, non-LLM judge | Open | d08: no sample-and-vote baseline, GPT-4o judge, 8192 vs 2000 token settings. d09: critical-question generation itself under 57% useful. |
| 6 Low attack recall; counter-argument pass | Partly closed | d06: gated second pass raises attack F1 .383 to .427 at 14% of calls; blanket debate no net gain; RoBERTa attack F1 .071/.167 from class imbalance. Caveats: 42 attack test items, no significance test, no false-attack rate. |
| 7 Gold-span vs full-pipeline gap; free-form text | Open | Nothing new. d12 shows relation scoring lacks gold in a shared task. |
| 8 Argument-mapping primaries | Partly closed | Cullen et al. 2018 opened (d01): d=0.71 [0.37, 1.04] LSAT, essays d=0.87, N=105 vs 56, quasi-experiment, feedback confounded. d02: earlier CCTST effects about 3x larger than LSAT. Twardy 2004, Alvarez 2007 and van Gelder 2015 still not opened; 0.8 vs 0.34 SD unreconciled. K24 stays contested. |
| 9 Long argument degradation; chunking | Open, one clue | d13: long papers handled by sentence-level anchored extraction. No length-cliff measurement. |
| 10 Toulmin-name prompts correct, not just present; Toulmin vs Walton | Open | No correctness study found (d15). d04 shows Toulmin-form output is better rated by LLM rubric but not more accurate; d14 shows scheme in justification differs from scheme in reasoning for about 20% of dilemmas. |

New cautions: TRACE correlation is across models (size confound); several 2026 numbers are single-group preprints; ITA Table 1 values were not extracted (column-scrambled).
