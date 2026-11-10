# Critique: ACT-R production compilation (C02.07)

Cross-checker pass. Sources re-opened this session: Taatgen et al. 2008 (FMS PDF), Memp, SkVM, LATM, ReasoningBank, AWM, ASI.

## Corrections made
- a02: medium-difficulty p=.031 is wrong. Published: t(18.9)=1.99, p=.062 ("approached significance"). Main effect p is .014 (b01 right), not .013.
- c13 mislabels LATM columns ("shuffled/sorting 20.4->92.2; Dyck 59.2->98.3"). Table 2: Dyck 20.4->92.2, Word Sorting 59.2->98.3. b20 is correct.
- Confirmed unchanged: Memp ALFWorld/TravelPlanner numbers, ReasoningBank 40.5/44.1/48.8/51.8, AWM 35.5 vs 23.5 (+12.0), ASI 32.7/36.3/40.4, SkVM 15% / 7% / 25% / 39 of 49, Taatgen 2008 Exp1 77.0 vs 91.1, hard 70.4 vs 89.9.
- AWM relative gain over SteP is 7.9% in the abstract and 7.6% in the results text; both appear in the paper.
- a03 (Exp 2 R2 .74/.76) vs b02 (R2 .66-.75): different fits reported; not re-opened in full. Treat as about .7.
- Not re-opened (second-hand): Heathcote 2000 numbers, Voyager table, Schumacher timings, Gianferrara 2021, Yu 2024 distillation.

## Contradictions and weak spots
- Taatgen 2008: effect of context instructions shrinks from Exp1 to Exp3 (accuracy model fit R2 .82 to .44; interaction with difficulty vanishes). All three experiments from one lab.
- Most compilation evidence is model fitting by Taatgen and colleagues with fitted parameters. Almost no test ablates compilation. Ji 2025 sets it aside; Gianferrara 2021 never switches it off.
- Exponential vs power law (Heathcote 2000) undermines the classic "power law" claim that compilation was built to explain.
- LLM analogues (Voyager, AWM, ASI, Memp, LATM) are not compilation. They commit after one verified success, not after repeated co-firing, and use much larger units. The analogy is loose.
- Mixed LLM results: Memp hurts hard constraints on TravelPlanner; ExpeL worse on heat tasks; SkVM shows skills in context hurt 15% of tasks; Distilling S2 into S1 fails on GSM8k CoT.
- Voyager: 3 runs per method. Different benchmarks, models and baselines across LLM papers; no equal-token comparisons anywhere.
- "No LLM implementation of ACT-R compilation exists" rests on one web search and citation tracing; absence claim only.
- Several lines were only seen via second-hand description (a21, a22, a23, a24, a25, b10, b24-b26).

## GAPS
1. Does a routine/lesson store with ACT-R-style promotion (low start utility, promote after repeated co-firing) beat verify-once-then-commit at equal tokens? Nobody has tested this.
2. Ablation: does turning routine storage off hurt early vs late items in a long sequence, controlling for tokens (Voyager showed late-only gains with 3 runs)?
3. What is the wrong-reuse rate of routines committed from one example vs several, on near-miss tasks (over-specialisation, DC-10 case)?
4. Does context-style (pre/post-condition) lesson wording beat plain step lists in an LLM, as in Taatgen 2008? Has anyone run it, and does it shrink as in Exp 3?
5. When does a stored routine hurt a model (SkVM 15%): which model sizes and task types, and can a cheap gate predict it?
6. Which granularity (script vs trajectory vs both) is best under hard constraints, given Memp TravelPlanner results contradict ALFWorld?
7. Is writing a wrong routine into procedural memory worse than a wrong episodic note, as Sumers 2024 claims? No measurement found.
8. Do 2020-2026 papers beyond those found (e.g. Soar chunking in LLM agents, Zhu and Reid productions from LLM reasoning) report measured results on compiling reasoning into rules?
9. Does the cost of the write step (LLM call to induce skill) pay back at equal tokens? Most papers report steps, not total tokens.
10. Re-open Heathcote 2000, Gianferrara 2021 and Taatgen 2013 PRIMs transfer numbers to confirm primary values.

## Gap search results (gap round, 2026-11-10)
New evidence: evidence_d.jsonl (d01-d15, all opened). Claims updated (K03, K08, K10, K11, K12, K15, K16, K20, K21) and K22-K28 added.

- Gap 1 (ACT-R-style promotion vs verify-once at equal tokens): STAYS OPEN. No study sweeps a co-firing count. Closest: GRASP (d10) shows the gate on commits is the main driver (no gate 63.5% / 40.1% vs 88.8%); MSCE (d14) promotes on estimated gain. Neither compares verify-once with repeated confirmation.
- Gap 2 (routine store off, early vs late): PARTLY ANSWERED, mixed. MSCE gains grow p0 to p100 (+13.84 to +17.00 Pass@1); Zhang 2026 (d11) finds ungated consolidation peaks near step 20 then falls below no-memory. No token-controlled, multi-seed position split. Open.
- Gap 3 (wrong-reuse rate, one example vs several): PARTLY ANSWERED. Zhang 2026 reports over-generalised and garbage entries (5x and 20x rates under cumulative consolidation, from the project page only); GRASP regression budget removal costs 7.0 points. No one-vs-several-example comparison. Open.
- Gap 4 (context-style wording in LLMs): PARTLY ANSWERED. EffectMem (d13) with applicability and postcondition contracts gives SR 15% to 65% on ScienceWorld/Qwen3-8B, but there is no plain-step arm with the same checks. Xu & Wu (d06): abstraction level effects small, CIs cross zero. No shrink-with-practice test. Open.
- Gap 5 (when routines hurt, which models, cheap gate): PARTLY CLOSED. SkillsBench (d03, d04): 13 of 87 tasks negative, self-written skills -8.1 to -11.5 pp; Liu 2026 (d05): weak models fall below no-skill when only general skills are retrievable (Kimi 19.8 vs 21.8, Qwen 19.7 vs 20.5), rewriting recovers part but hurt Kimi. Causes found: no applicability boundary, heavy pipelines, loading failures. A validated cheap predictor not found.
- Gap 6 (script vs trajectory under hard constraints): STAYS OPEN. Nothing new beyond Memp. Xu & Wu (d06) test abstraction on SkillsBench only.
- Gap 7 (wrong procedural vs wrong episodic note): STAYS OPEN as a direct test. Indirect: episodic-only matches consolidators (d11, d12); ungated skill writing equals no skills (d10).
- Gap 8 (Soar chunking, other 2020-2026 compile-reasoning work): CLOSED with finds. CogRec (d08, Soar chunking from LLM answers at impasse, LLM call rate falls, chunking off hurts), NeSyPr (d09, trained proceduralisation: latency and token cuts), 2026 review (d15). Zhu and Reid not located. None implements repeated co-firing promotion.
- Gap 9 (write cost at equal tokens): STAYS OPEN. SkillReducer (d07) counts injection tokens; GRASP counts probe calls only.
- Gap 10 (re-open Heathcote, Gianferrara, PRIMs): PARTLY CLOSED. Heathcote 2000 (d01) and Gianferrara 2021 (d02) opened and confirmed. Taatgen 2013 PRIMs transfer numbers still second-hand (not retrievable open-access this round).

Caveats: Zhang 2026 per-model numbers and the 5x/20x rates were taken from a project-page summary; abstract and WebShop/ScienceWorld numbers were checked in the PDF. CogRec Table 2 text extraction was misaligned. Two tools (Semantic Scholar, arXiv API) rate-limited; 2 WebSearch calls plus 2 follow-ups used (4 of 8).
