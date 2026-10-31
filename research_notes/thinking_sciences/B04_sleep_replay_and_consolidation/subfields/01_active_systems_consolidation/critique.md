# B04.01 Active systems consolidation: cross-check critique

## Numbers re-opened (10 checks)
Confirmed against full text or abstract this session:
1. Hu 2020 TMR meta-analysis (b04): 91 experiments, 212 effect sizes, N=2,004, g=0.29 [0.21,0.38]; NREM2 0.32; SWS 0.27; REM and wake ns. Confirmed (Europe PMC abstract).
2. Henin 2019 (a11): Bayes factors 0.302 and 0.299 (Exp 1), Exp 2 listed in Table 4. Confirmed (full text). Not re-checked: n=12 and n=19.
3. Feld 2016 (a12): n=101 total (Exp 1: 22 sleep + 26 wake; Exp 2: 27 + 26). Benefit at 160 pairs, not 320. Confirmed. Authors themselves say the effect is not large enough to be found reliably at n=101.
4. Ngo and Staresina 2022 (b10): 5 vs 15 percent, t(23)=2.28, p=0.032. Confirmed (full text).
5. Tadros 2022 (a19, c17): sequential vs SRC 19.49 vs 48.47 (MNIST), 19.67 vs 41.68, 47.18 vs 61.33, 19.01 vs 44.55 (CIFAR-10); CUB-200 63.2 and 45.4. Confirmed (full text table). Note OWM (77.04) beats SRC on incremental MNIST.
6. Lin 2025 sleep-time compute (b18, c15): about 5x, up to +13 and +18 percent, 2.5x per-query cost at 10 queries per context. Confirmed (full text). Stateful AIME has only 60 questions; Claude 3.7 averaged over 10 runs, others 3; o1 showed limited gains.
7. SleepGate (c04, c05): 99.5/97.0/73.5/16.5 and 62 percent stale at n=30. Confirmed. Small inconsistency inside the paper: abstract says baselines are "below 18%" while text names StreamingLLM at 18.0 percent at n=2.
8. Auto-Dreamer (c09, c10): 41.1 vs 34.1 (UMEM), +10.2 vs ReasoningBank 30.9, ALFWorld 60.2, controlled 72.7 vs 70.1 and 44.3 vs 42.0, GRPO +9.7/+5.7/+1.0. Confirmed (full text). Added: WebArena 52.3, memory 12x smaller on ScienceWorld and 6x on ALFWorld than the strongest baseline. Confidence intervals exist in an appendix (e.g. ScienceWorld 41.07 [37.5,44.7]) and overlap other baselines in places; c09 said "no variance", which is partly wrong.
9. Behrouz 2026 "Sleep" (c07): AIME-24 base 73.8, GRPO 76.4, OPSD 76.6, Sleep 79.2 on Qwen3-8B; 1.7B 51.6 vs 53.2. Confirmed.
10. Wagner 2004 (a07), Rasch 2007 (a03), Marshall 2006 (a02): abstracts confirm qualitative claims ("more than twice as many"). Exact percentages still not opened. Lutz 2026 (a13): N=16 within-subject confirmed; the paper also reports replicating high early prototype recognition, which a13 should say.

## Corrections and flags
- b18 and c15 are the same paper; b07 and a15 (plus b08, b09) are one meta-analysis; b04/b05/b06/b11 are one meta-analysis. Counting them as separate lines overstates independence. Claims use independent source counts.
- c24 and c25 are bookkeeping notes, not evidence; they were used only for the "no LLM tests human-style effects" claim.
- a25 (Kumaran 2016) was not opened and its PMID was from memory; treat as unverified.
- c21 and c22 are second-hand.
- Two snippet-only items surfaced during checking and should be followed up: a 2025 report that frontocortical tDCS plus closed-loop acoustic stimulation impaired memory in high-ability subjects (PMC12493016), and a 2024 mouse study where a single closed-loop acoustic stimulation suppressed hippocampal ripples and thalamo-cortical spindles (PMC11214843). Both cut against a simple "boost the rhythm, boost memory" story.

## Contradictions between sources
- Slow-oscillation boosting: Marshall 2006 and Ngo 2013 report gains; Henin 2019 finds equal memory with Bayes factors favouring the null; Cordi and Rasch 2021 say effects are smaller and task-dependent.
- Abstraction: Wagner 2004 and Lowe 2024 (N2, not SWS) support sleep-driven insight; the 2020 ill-defined-problem nap study (N=40) and the DRM meta-analysis show nothing; Liu 2025 ties abstraction to REM power, not SWS.
- LLM side: LightMem, Auto-Dreamer, RecMem all report gains but with different baselines; Hippocam wins ScienceWorld transfer while A-Mem wins ScienceWorld elsewhere (87.2).

## Weak spots
- Most founding studies were verified from abstracts only; no exact effect sizes for Marshall, Rasch, Wagner, Wilson, Ji, Girardeau.
- Almost every LLM result is a single run on authors' own benchmark or a small model; seed variance is mostly absent. Gains of 1 to 3 points (Sleep, reconsolidation) are within plausible noise.
- LLM gains rarely isolate the offline step from the whole memory pipeline (LightMem) or hold token budgets equal.
- No LLM study replicates a human boundary condition (stage dependence, capacity limit, timing).

## GAPS
1. Does an offline consolidation pass (episodes into rules) beat spending the same tokens at query time or on more retrieval, with seeds and equal total tokens? Which published memory-agent results already include that control?
2. Which consolidation operations carry the gain: merge/dedupe, abstraction into rules, forgetting/pruning, or recurrence gating? Any ablation that isolates each at fixed tokens?
3. How much does abstraction lose (dates, locations, numbers, exceptions), and does keeping source-linked raw episodes fix it without cost? Evidence beyond LoCoMo temporal and Auto-Dreamer look_at_obj_in_light.
4. Capacity limit: does rule extraction quality saturate or fall as the number of episodes per offline pass grows (analogue of 160 vs 320 pairs)? Any LLM study varying batch size of consolidation?
5. Exact effect sizes and sample sizes for Wagner 2004 insight (percent per group), Rasch 2007 and Marshall 2006, and the largest independent replications of sleep-dependent rule or insight discovery (2015 to 2026).
6. Do the 2025 to 2026 closed-loop and tES null or negative results (Henin follow-ups, PMC12493016, mouse ripple suppression) change the Cordi and Rasch 2021 verdict on robustness?
7. Selection for replay: do prioritised-replay rules (hub items, surprise, recurrence, reward) beat uniform replay in LLM agents, matching human findings on hub nodes (Feld 2022, N=19)?
8. Do LLM consolidation passes introduce false memories (DRM-like), and how is it measured? Any study of hallucinated rules from ExpeL-style insight extraction?
9. Are there any LLM studies that measure schema-consistent versus schema-inconsistent integration (McClelland 2020 prediction) by testing fast integration of new facts that fit existing rules?
10. Reconsolidation: is updating memory at retrieval worth more than +2 points when variance is controlled, and does it risk drift?


## Gap search results

Evidence is in `evidence_d.jsonl` (d01-d21). Claims K04, K09, K17-K21, K26 changed; K28-K35 added. Web search quota ran out early; arXiv, Semantic Scholar and OpenAlex APIs were rate limited, so I worked from Europe PMC full texts and the five LLM-memory PDFs I could already download (Auto-Dreamer, All-Mem, RecMem, Microsoft human-inspired memory, RPMem). Absences below are weak for that reason.

Status per gap: CLOSED (answered), PARTIAL, OPEN.

1. Offline pass vs same tokens at query time (PARTIAL, answer is mostly "nobody checked"). None of the five papers compares an offline pass against the same tokens spent on more retrieval or reasoning. Auto-Dreamer caps retrieval (top-K 3) but does not report consolidator tokens. All-Mem matches query-time tokens with Mem0, yet its offline pass costs 1,237 tokens/turn against 539 online. RecMem is the only one that charges construction tokens (193.2K vs 1,520.8K), and full context beat it on LoCoMo (90.84 vs 86.92). No paper has several seeds. New claim K28. The earlier sleep-time compute result (c15) remains the only token-framed test.

2. Which operation carries the gain (PARTIAL). Dedup: safe at moderate budget (76.8 vs 78.4 raw RAG, CIs overlap) and All-Mem Merge is worth 3.16 F1. Summarizing clusters: destructive (48.4). Abstraction/region rewriting: Auto-Dreamer's untrained rewrite alone gave most of the bank shrinkage and +11.2 pp on ALFWorld over writer-only. Recurrence gating: about 7 points in RecMem, but bundled with its tiers. Forgetting: too-hard budgets are harmful (57.0 at 10K). No paper isolates all four at fixed tokens. K32, K20.

3. Abstraction loss and source-linked raw episodes (CLOSED enough to act). Evidence beyond the two named cases: RecMem raw tier worth 29 points (81.10 to 51.88), All-Mem recovery links 2-3 F1, Microsoft summarising drops assistant-recall questions from 94.6 to 39.3. Source-linked raw storage mitigates it, with a link-hop cost. All-Mem audit: 94.2 percent of 190 edits valid, 3.7 percent harmful. Not tested: dates, places and numbers broken out by operation. K33.

4. Capacity limit for rule extraction (PARTIAL). One LLM data point: Auto-Dreamer cadence sweep, inverted U (k=1 and k=20 both worse on ScienceWorld). It is a cadence sweep, not a controlled batch-size sweep, figure-only, no seeds. No study varies batch size at fixed total episodes. K31. The human 160 vs 320 result (K08) stays single-source.

5. Exact human numbers (PARTIAL). CLOSED for Wagner 2004: 13/22 (59 percent) vs 5/22 (22.7 percent) or 5/20 (25 percent) in four control groups, chi2 10.2, p .03 (from Verleger 2013, which prints Experiment 1). STILL OPEN for Rasch 2007 and Marshall 2006: neither is open access, and the sites that could give the numbers were not reachable. Replications 2015-2026: no large direct replication of Wagner found. Largest related: Lacaux 2021 N 103 (83 vs 30 percent, N1), Lowe 2025 N 90 preregistered (85.7 vs 55.5 percent, N2), Schonauer 2018 N 77 null, Vickrey 2023 N 72 (pink noise, no gain), Beijamini 2021 (62 vs 24 percent; no TMR gain). Stage conflict N1 vs N2. K29, K30.

6. 2024-26 nulls vs Cordi and Rasch 2021 (PARTIAL). The robustness reading is not overturned, and is a little weaker: 2021 meta-analysis g 0.25 (p .07); the 2022 g 0.68 meta-analysis was retracted in 2026; two more closed-loop nulls (N 27, N 34). Correction to the earlier note: PMC12493016 is a tDCS plus CLAS study (N 20) with no overall memory effect and a decrease only in a high-Raven subgroup, and it compares to CLAS alone, not sham. PMC11214843 (mice) did not beat sham and shows about 1 s of ripple suppression after each pulse. The Henin follow-ups themselves were not found. K34, K04.

7. Does choosing what to replay help (OPEN, weak). Only recurrence gating (RecMem, about 7 points) and RPMem's learned write gate (parametric) were found. No LLM paper compares hub, surprise or reward priority with uniform replay. Human side: Beijamini 2021 shows targeted cueing added nothing beyond natural sleep. K35.

8. False or hallucinated rules from consolidation (OPEN). Not measured in any paper read. Nearest: All-Mem human audit (3.7 percent harmful edits, mainly over-merging entities), and ExpeL scoring about equal to no memory on ScienceWorld (28.33 vs 28.69) and ALFWorld (33.59 vs 30.83). K35, K26.

9. Schema-consistent vs inconsistent integration (OPEN). No LLM study found. K35.

10. Reconsolidation worth more than about +2 (PARTIAL, leaning no). Microsoft ablation: dedup + reconsolidation 75.8 vs dedup 76.8 (CIs overlap fully) on S-tier; authors say there were few contradictions to detect at 50 sessions; reconsolidation was on in M-tier but never switched off there. Drift risk: not measured except All-Mem noting harmful merges. K21 now contested.

Corrections to earlier lines: Auto-Dreamer's CIs are task-bootstrap only (no seeds); Wagner's wake figure is 22.7 percent for the 22-person groups and 25 percent for the 20-person ones (the 22 or 23 figure is explained); the "stimulation impaired memory" snippet is a subgroup result.

Still needed (in order): equal-total-token A/B/C test with seeds (K28); an operation-isolation ablation at fixed tokens; a false-rule rate measurement; Rasch 2007 and Marshall 2006 numbers from the PDFs; Henin follow-ups.
