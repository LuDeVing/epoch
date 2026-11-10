# Critique: E09.06 Tools and questions (why/why-not, slicing)

## Corrections made (10 number groups re-opened from source PDFs)
Confirmed exactly: Whyline 2004 (F(1,5)=12.64, factor 7.8, M=3.20 vs 2.25, t(7)=3.0, 19 of 24, 68%/85%/50%; N=4 without, 5 with); Java Whyline 2008 (median 4 min range 1-12 vs 10 min range 3-38, 18 self-described experts, Wilcoxon p<.05, 35,597 events, 90% wrong guesses); Whyline 2009 (chi2=10.6 and 5, t=22.6, t=4.6, "three times as often"); Ko-DeLine-Venolia 2007 (61/44/41/36%, 17 developers); ChatDBG (57/67/85, 36/55, ten runs, gpt-4-1106); Olausson (33.30 -> 52.60 with human feedback, 42.64/19.33/3.67 -> 62.21/45.67/14.67); Shahandashti (60.84, 7.33, 59.69, 4%, 3.9%).
Corrections:
- c06 names the authors "Ko, Aung, Myers (2007)". The 2007 information-needs paper is Ko, DeLine, Venolia (a10/b09 are right). Ignore the c06 author line.
- a05/b05/c03: the 10-minute control group is NOT a concurrent control. It is 18 experts from a different earlier study, so the "2x faster" is a cross-study comparison with N=9 novices. The 2009 CHI paper (N=20, concurrent control) is the sturdier result.
- a04: the "7.8x" is an average of per-scenario ratios across six scenarios, on a repeated-measures test with only 4 and 5 people; do not quote it as a general speed-up. c05 says "factor of 8", a rounding of the same number, not a second study.
- a09 (2005) and b10 (2006) both give 35% navigation time; likely the same dataset, so not two independent sources. Counted once in K05 via the 2007 paper as the second source.
- Not re-opened (second-hand): Weiser 1982/1981 (PDF 403), Parnin and Orso 2011, Ko 2025 retrospective details, SliceMate, CausalRepair, BluesFL, SWE-Doctor, REval, debug-gym, mutation robustness. Their numbers rest on the evidence agents' reading and were not re-checked here.

## Contradictions
- Trace/runtime info helps (LDB +9.8%, SWE-Doctor, CausalRepair) vs does not (Adnan-Kuhn: resampling beats trace repair on LiveCodeBench, BPD no gain; debug-gym: o3-mini and Aider show no or unstable effect). Likely boundary: benchmark difficulty, model strength, and whether the trace is a focused slice or the whole trace. Not resolved.
- Slice quality: GPT-4o exact match 7.33% (Shahandashti) vs SliceMate large gains; different benchmarks and metrics (Accuracy-D partial credit vs EM). Not comparable.
- Human feedback beats model feedback (Olausson), yet model-made slices/estimators (RecovSlicing) beat baselines. Suggests the model is a weak self-critic but a decent dependency estimator.
- Human studies say answering why-not questions is the big win; the Java Whyline users rarely asked why-didn't questions because of delay.

## Weak spots
- No independent replication of Whyline anywhere. Same lab, builder-run studies, tiny N, students, tools built by the evaluators.
- Weiser 1982 is the founding claim but its stats were never read; Ko 2025 itself calls it weakly supported.
- Parnin and Orso 2011 (the well-known challenge to automated debugging tools) was only seen as a citation.
- LLM work mostly compares a tool-supplied slice to no slice; few test "model asks why-questions itself" vs "tool computes slice" at equal tokens.
- ChatDBG success is run-level on student programs, GPT-4 era, no variance reported beyond ten runs.
- Mixed benchmark contamination risk (Defects4J, HumanEval) is untested in most 2024-2026 studies.

## Only seen in snippets / abstracts
Weiser 1982, Weiser 1981, Parnin and Orso 2011 (all opened:false). ChatDBG per-component ablation numbers are in a figure that was not extracted.

## GAPS
1. At equal tokens, does a code-computed backward slice of the failing output beat the model's own free exploration for bug localisation in an agent (SWE-bench-style), and by how much?
2. What are the exact Parnin and Orso 2011 results (N, tasks, rank vs success) and did anyone replicate Whyline-style claims independently?
3. Does a plain "why did X not happen / why did Y happen" prompt step help an LLM agent versus a hypothesis list, and which question types (why-not vs why-did) matter?
4. At what dependence-chain length or slice size should the agent switch from free reasoning to a tool-computed slice (the 20 upstream sources / 600 lines / 100 steps thresholds from Li et al.)?
5. What did Weiser 1982 actually measure (N, test statistics), and is there any later human study that validates slices as a cognitive unit?
6. Why do trace-guided repair results disagree (LDB, Adnan-Kuhn, debug-gym)? Is it focused-slice vs whole-trace, model strength, or benchmark?
7. Can model confidence gate extra backward-search steps (AutoFL Spearman 0.52-0.57) without raising token cost?
8. Do dynamic slices work when no failing test or reproduction exists, and how often does the agent need to build the reproduction first (SWE-Doctor: fail-to-fail tests mislead)?
9. How robust is slice-guided localisation to semantic-preserving rewrites (78% flips in the mutation study) when a tool, not the model, computes the slice?

## Gap search results
Evidence is in evidence_d.jsonl (d01-d24). Claims K02, K07, K10, K12, K13, K14 were extended; K15-K18 added.
1. Slice vs free exploration at equal tokens: STAYS OPEN. No head-to-head found. Indirect: capable agents fail mostly after reaching the right functions (d21, 60-69% of failures), and runtime diagnosis costs more tokens (d02). K15.
2. Parnin and Orso: CLOSED for numbers (d18, author PDF read: 24 students, high performers 8:51 vs 14:28, p<0.05, no effect of rank changes, 61% of time spent after seeing the fault). Independent Whyline replication: still none found.
3. Why-not vs why-did prompt vs hypothesis list: STAYS OPEN. Partial support: per-candidate explanations (d22 RGFL), bounded runtime questions (d23 Debug2Fix), hypothesis bottleneck (d24). No question-type ablation exists in what was found.
4. Switch thresholds: CLOSED as a negative. The 20/600/100 numbers are read from plots on a value-prediction task and never tested as tool switch points (d15).
5. Weiser: PARTLY CLOSED. Second-hand via Parnin and Orso (d19): 21 programmers, 3 programs, recognition test; later tool tests null or mixed. The discrepancy with the earlier "two programs" remains. Original statistics still unopened.
6. Trace disagreement: PARTLY CLOSED. Likely cause is focused answer vs raw dump plus token cost and model strength (d06, d07, d08, d23); no controlled test separates them.
7. Confidence gating: STAYS OPEN. Spearman 0.57/0.52 needs five runs per bug (d09); call cap of 10 vs 20 matters (d10); no equal-token test.
8. No reproduction: PARTLY CLOSED. Non-witnessing tests hurt (d01, d24); how often the agent must build the reproduction first is not measured.
9. Robustness of tool-computed slices: PARTLY CLOSED. CausalRepair fell 7.7% vs 15% for a baseline under rewrites (d05); one benchmark, one model.
Not opened: Weiser 1982 original, the "Do Coding Agents Still Need a Debugger" paper (d20, titles only).
