# C08.01 The 4R cycle: cross-check and critique

Method: ten sets of numbers were re-checked against the saved full-text of the papers (pdftotext files on D:/research_scratch/C08.01/), plus Reflexion re-downloaded and read. Claims are in claims.jsonl (25 claims, K01-K25).

## Re-checked and confirmed
1. Memento (arXiv 2508.16153) K table: K=0,1,2,4,8,16,32 gives average F1/PM 59.9/72.2, 63.6/77.9, 63.7/78.1, 64.5/78.5, 64.1/78.2, 63.9/78.1, 63.9/78.1. Peak at K=4 confirmed. Bamboogle PM 91.2 at K=1 vs 87.2 at K=32 confirmed.
2. Memento headline: 66.6 F1 / 80.4 PM on DeepResearcher; abstract says CBR adds 4.7 to 9.6 absolute points out of distribution. Confirmed. The ablation differences (+4.5, +3.7, +6.7 F1) are arithmetically consistent with the listed pairs.
3. Memento learning curve: gap at pass 5 of 0.38 and 0.97 follows from 84.47, 84.85, 85.44. Consistent.
4. Xiong 2025 (arXiv 2505.16067) main table: add-all, C1, C2, C3 and strict rows confirmed; fixed memory row (67.53, 16.75, 40.11, 71.50) is higher than add-all on all four agents. "After about 2000 executions" confirmed.
5. ReasoningBank (arXiv 2509.25140): Gemini-2.5-flash overall 40.5 / 42.1 / 44.1 / 48.8 / 51.8 with scaling; Shopping 49.7 (RB), 44.4 (AWM), 40.6 (Synapse); Gemini-2.5-pro 53.9; Claude 3.7 no memory 41.7. Confirmed.
6. ExpeL (arXiv 2308.10144): insights-only/retrieve-only 36/31 (HotpotQA), 50/55 (ALFWorld), 37/38 (WebShop) confirmed in text. Table 3 values (59.0, 48.5, 42.5, 40.0; 39.0, 32.0, 29.0, 28.0) confirmed as numbers; the mapping of row labels to numbers rests on a garbled extraction and the earlier agents' reading.
7. Aha, Kibler, Albert 1991: Hungarian IB1 58.7, IB2 55.9 (36.0% stored), IB3 80.5 (7.5% stored), C4 78.2; 20 of 76 noisy (26.3%), average 28.3%. Confirmed.
8. Gentner et al 1993 (2.36 / 1.48, 52%, 82%), Catrambone and Holyoak 1989 (71% vs 41%; 65% vs 42%), Kubricht 2015 (55%, 50%, 81%; chi-square 6.60, p=.01). Confirmed.
9. Dynamic Cheatsheet (arXiv 2504.07952) Table: Claude 3.5 Sonnet AIME 2024 23.3 / 36.7 / 43.3 / 50.0 / 46.7 (BL, DC-empty, DR, DC-Cu, DC-RS); GPT-4o Game of 24 10 / 19 / 6 / 93 / 99; GPT-4o MMLU-Pro Eng 53.2 to 44.0. Confirmed. A separate table has full-history 26.7 / 6.7 for Claude.
10. Reflexion: HumanEval 91.0 vs 80.1; MBPP-Python 77.1 vs 80.1 (worse); false-positive rate MBPP 16.3% vs HumanEval 1.4%; 130 of 134 AlfWorld. Confirmed.
11. Evo-Memory r = 0.717 and 0.563 confirmed.

## Corrections
- b04 (and the claim built on it): the "AgentDriver 85.40 vs 89.60 (904 vs 788)" pair belongs to CIC-IoT, not AgentDriver. AgentDriver strict is 51.00 (memory 1178) and history-based deletion gives 51.81 (846), a gain of 0.8, not 4.2. EHRAgent 38.67 to 42.06 is right. K08 uses the corrected labels.
- a30 and b23: the 30.2% figure is Llama-2-7B trained from scratch on base addition with a 441-sample held-out square (random split 92%). The 81.5% training share belongs to a different run (GPT-3.5 fine-tuned), whose held-out square accuracy was 97.5%, not far below 100%. a30 mixed the two. b23 names the first author "Zhang"; the first author is Yi Hu (Hu, Tang, Yang, Zhang).
- c18: "almost zero accuracy" on held-out squares was not found in the paper text I read; the paper reports 30.2% (Llama-2 from scratch) and shows holes for GPT-2. Treat c18's "almost zero" as unsupported.
- b22: the false-positive rates (16.3% vs 1.4%) are MBPP Python vs HumanEval Python, not "16.3% vs 1.4% on HumanEval".
- c14/a26 dates: ReasoningBank is arXiv Sept 2025 (ICLR 2026 submission); listed as 2025 and 2026 in different lines. Same paper.
- a20/a21/b15/c03 are all Memento; a25/b17/c06/c07 are all ExpeL; a26/b18/c14/c15 all ReasoningBank. Counting these as separate sources would inflate independence. Claims count each paper once.
- c21 is an agent-written comparison, not a source. It was used only as a cross-reference.

## Contradictions between sources
- Memory helps (K01, K11, K12) vs memory is a small part of the gain (K03, K04). Memento CBR adds a few points; the scaffold adds more; the no-CBR run also improves over passes.
- Transfer: Memento claims largest CBR gains out of distribution (+4.7 to +9.6); Evo-Memory finds gain rises with within-stream task similarity (r 0.56 to 0.72). Not necessarily conflicting (different definitions of similarity and different baselines) but it is the key open point (K18).
- Failures: ReasoningBank gains from them, AWM and Synapse do not (K11). One benchmark, one model family.
- Retain-selectively: Xiong shows a strict filter wins; Smyth and Keane show random deletion loses competence; but history-based deletion on RegAgent lost 4.4 points (K08). Oracle-quality filters are assumed in the best case.
- Dynamic Cheatsheet: GPT-4o Game of 24 10 to 99 is stored code for one task family; same paper shows harm on other tasks (K19, K25).

## Weak spots
- Almost all agent results are single runs. Sarukkai's own figure shows five trials differing by about 0.06 on InterCode-SQL. No confidence intervals in ExpeL's retrieval ablations beyond the stated standard errors (0.3 to 2.1).
- Gains are mostly measured without equalizing tokens. Retrieved cases add context; Memento reports about 26k, 48k, 121k tokens per task by level but not a no-memory token cost.
- Benchmarks are shared (ALFWorld, WebArena, HotpotQA), so agreement across papers is partly the same task family.
- Human-subject evidence (Gentner, Catrambone, Kubricht) concerns analogical retrieval of stories and puzzles, not retrieval of subgoals by an agent.
- Gentner's per-condition Ns and Catrambone's Ns were not re-read; only the percentages.
- Smyth and Keane 1995 numbers (86% and 80%) were not re-opened in this pass; Pan et al 2005 follow-up gives only direction. K09 is marked contested for that reason.
- Seen only in snippets or abstract pages: Lopez de Mantaras 2005 beyond what a13-a16 report (b09 abstract only); Voyager (c20, no numbers); CASCADE (arXiv 2605.06702) not covered by any evidence line here; Hatalis 2025 review has no numbers. Wilkerson and Leake "20 to 28 percent" remains a snippet only.
- No evidence line tests the revise-and-repair half of Aamodt and Plaza's cycle (CHEF-style explain-then-repair) in an LLM; only generic self-correction (Huang, Reflexion).

## GAPS (most decision-relevant first)
1. At equal total tokens (retrieved text counted), does a case library beat the same scaffold with an empty library, and by how much, on a task stream of the kind we run? No source equalizes tokens.
2. What is the break-even library size and k for LLM agents? Memento peaks at K=4; no one has plotted success against library size with distractors (the LLM version of the utility problem).
3. Which retain rule is best when the only judge is the same LLM: success-only, success plus distilled failure, or strict external check? Xiong's judge was tuned on 300 trajectories; what is the minimum judge precision at which add-selective beats add-nothing?
4. How often does a retrieved case hurt (harm rate), and can a cheap structural check at reuse (Gentner-style relational match) cut it? No paper reports harm counts per retrieved case.
5. Does the benefit of cases depend on similarity of the new problem to the nearest stored case, and what similarity threshold should trigger "do not reuse"? Evo-Memory and Memento disagree in direction.
6. Does an explicit revise step with an explanation of failure (CHEF style, A&P Revise) beat plain retry with feedback in an LLM at equal tokens? Not tested anywhere in the evidence.
7. Is distilling a strategy from a case better than storing the raw solved-subgoal record, once the distiller is the same model? ReasoningBank says yes (48.8 vs 42.1), but Synapse is a particular baseline and the distiller is tuned.
8. Do these results hold on reasoning tasks without environment feedback (math, ARC-like puzzles), or only for agentic tasks with a check? Dynamic Cheatsheet shows large variance by task family.
9. How much of case-memory gain is format priming (Min et al 2022) rather than solution reuse? A format-matched irrelevant-case control is missing in all agent papers.
10. Does the picture change with strong models that already solve the task (CBR-RAG: +1.94%, Haiku gains nothing)? What is the no-memory success rate above which retrieval should be skipped?

## Gap search results

Search note: WebSearch quota ran out and the arXiv, OpenAlex and Semantic Scholar APIs rate-limited during this pass, so sources were found by one search and then by known paper ids. Fifteen evidence lines (d01 to d15) were added; claims K26 to K33 are new and K02, K06, K07, K12, K16, K18, K19, K20, K22, K24 were updated.

| Gap | Result | Main evidence |
|---|---|---|
| 1 Equal tokens vs empty library | Still open as a direct test. Indirect: complex loops do not beat plain retry at counted cost (K26); a CBR agent paid +49% prompt tokens for a non-significant gain (K33). | d01, d04, d09, d11 |
| 2 Library size and k | Partly closed for k: saturation at about 5 (OBAM), retrieval benefit shrinks as examples grow (51.5 to 4.9 points), MATH ICL peaks near 125 then falls (K31). Library size with distractors still unplotted. | d02, d10, d13 |
| 3 Retain rule and judge precision | Partly closed. A same-model judge had about 17% precision on graph colouring (K06). The break-even precision is still unmeasured (K28). | d11, d12, d14 |
| 4 Harm per retrieved case | Harm is real and concentrated on hard items (K29): 10% of PopQA questions, -26.1 points on failed ALFWorld items, -9.2 on MMLU-Pro Eng. No paper gives a harm count per retrieved case for a case library. A cheap check (NLI filter) works but drops helpful passages (K30). | d03, d06, d08, d15 |
| 5 Similarity and a do-not-reuse threshold | Still open. Far-task reuse of raw cases hurts (Hu), near conflicting neighbours hurt (OBAM), topical overlap makes distractors worse (Shi). K18 stays contested. No threshold. | d02, d03, d07 |
| 6 Explain-the-failure revise vs retry | Mostly closed against same-model explanation (K27): no gain at equal tokens unless the explanation is accurate. A CHEF-style step with an external check is untested. | d09, d11, d12, d05 |
| 7 Distilled vs raw | Narrowed. Distilled is safer across tasks; raw is better within a task (80.5 vs 65.5). K12 moved to contested. | d03 |
| 8 Tasks with no environment check | Partly closed. Gains exist on AIME and GPQA without ground truth (Dynamic Cheatsheet) but are mixed (-9.2 on MMLU-Pro Eng for GPT-4o) and uncurated history is worst. Implicit reasoning QA is where retrieval hurt in Yoran. | d08, d15 |
| 9 Format priming | Still open for agents. Indirect support only: problems-only prompts matched ground-truth solutions on MATH500. | d13 |
| 10 When to skip retrieval | Partly closed by analogy: popularity-gated retrieval beat always retrieving by 5.3 points (K32). No agent threshold. | d06, d02 |

Caveats on this pass. d12 per-task rows come from a garbled table, only ranges were used. d02 store-all ablation magnitude was not read from a figure. Min et al. 2022 was not re-opened. Downloaded PDFs and text were kept on drive D only.
