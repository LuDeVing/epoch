# Critique: C09.07 Diagnosability (cross-check)

Evidence read: 85 lines (a 31, b 26, c 28). Claims written: 24 (C09.07-K01 to K24).

## 1. Numbers re-opened this session (PDF text)

Confirmed exactly:
- Marozzo and Lio (arXiv 2606.13220): SIA 79.2 [72.7,83.7], ReAct 69.0, ToT 61.5, potential 89.2 vs 84.0, 9.0 hypotheses and 5.2 questions, 21.0 hypotheses for ToT; backbones 75.4 vs 69.2 and 76.1 vs 68.4; exact diagnosis 6/10 vs 5/10.
- Luo et al. (arXiv 2603.21250): distributed-systems GoS Match 70.67 / Relevant 88.00 vs best baseline 34.00; error rates 22.22 / 41.32 / 63.89 vs 0 / 9.70 / 18.75; backtracking 30.90; ablations 18.12, 12.32, 19.57.
- Hu et al. UoT (arXiv 2402.03271): GPT-4 closed-set 71.2 / 37.5 / 97.0 / 88.0 / 67.3 vs direct 50.5 / 30.5 / 91.3 / 72.3 / 43.7; open set 55.3 and 28.0; 38.1% average; 5.9%; matched-cost table 9.2k tokens 54.4/92.5/66.0 vs 4.5k 33.8/85.1/60.3.
- Choudhury and Williamson BED-LLM: 37.4 points; GPT-4o Animals 45 / 83 / 93, in-context beliefs 25.
- MAI-DxO: 304 cases, 80% vs 20%, 85.5% max-accuracy, 20% and 70% cost cuts. Extra detail seen: o3 alone 78.6% at $7,850, MAI-DxO 79.9% at $2,397. So the "80% vs 20%" headline is physicians vs system; against plain o3 the accuracy gain is about 1 point and the gain is cost.
- Cloud-OpsBench: 33.1% and 29.4% (GPT-5) confirmed, 73% log-termination figure confirmed.
- Plank and Wotawa: hit rates 79.5 / 76.9 / 38.5, hallucination 20.5 / 15.4 / 7.7 / 94.9, W 1.846 / 1.832 / 1.526 / 0.314, Phi-2 1.05 vs 0.08-0.67.
- Cassez and Tripakis dynamic observers: Theorem 1, diagnosability with dynamic observer is in P (opened).

Corrections and warnings:
1. GoS medical diagnosis (a25, b09, b10): the evidence says human-judge Match 39.86 / Relevant 78.99 for GoS. In the table text, the GoS row is blank in extraction and the Single/CoT row prints exactly 39.86 / 78.99 under human judge. The prose also says GoS reaches 39.86. One of the two is a layout shift or a paper error. Do not quote 39.86 as GoS; the safe GoS number is the distributed-systems 70.67 (clean table). Ablation numbers (18.12, 12.32) are LLM-judge Match and are still valid for relative comparison.
2. a25 says baselines Match 34.00 is "best baseline" for distributed systems: confirmed (Multi/CoT), but b09 reports it as 34.00 in one place and the medical best baseline differently; keep the two datasets separate.
3. Token matching in UoT (c07): the matched-cost table compares UoT at 9.2k tokens with Adapted-ToT at 4.5k. That is 2x, not matched. K09 is therefore marked contested and the claim now says so.
4. MAI-DxO: corrected reading above (gain over o3 is cost, not accuracy).
5. Duplicates: a21-a24 and b01-b04, a27-a31 and b06-b08, a25-a26 and b09-b10, a18 and b14, a12/b12 and a19, a10 and b11 are the same sources. Independent-source counts in claims count papers, not evidence lines.
6. c15 (ORCA-bench) carries a note that a secondary summary said 884 tasks vs 1,079 in the abstract. Abstract value kept.

## 2. Contradictions between sources

- LLM test selection: ACTMED (c19) says LLMs pick the same global tests for every patient; UoT/BED-LLM show an LLM can improve when scaffolded with information-gain scoring. These agree rather than conflict (free choice is poor, scaffolded choice is good). The one contrary item is the search-summary claim that LLMs do not beat random experiments in sequential BED (c27, not opened).
- Cost: information-gain scaffolds look cheap (UoT, MAI-DxO, ACTMED) while coding-agent harnesses in Cloud-OpsBench cost 2 to 4x tokens (c13). Different task types, different baselines.
- Potential vs final (SIA): ToT has a larger pool (21.0 hypotheses) but worse final score; more hypotheses do not help without selection.

## 3. Weak spots

- No paper in the set tests diagnosability itself on an LLM: no study gives an LLM a model, computes whether faults are separable, and measures whether the LLM says "cannot tell". The link from formal diagnosability to LLM agents is by analogy (potential-final gap, ungrounded diagnosis, redundant probes).
- Most 2026 LLM numbers are single preprints from one group each (SIA, GoS, Cloud-OpsBench, PAVE, ORCA). SIA and GoS use LLM judges; GoS medical set is small (about 138 cases from the percentages; not verified).
- SIA stress test is 10 pairs; no significance.
- Plank and Wotawa scored by hand, 3 runs, 7 small systems, 13 models; the double-fault finding rests on one scenario.
- Sztyber-Betley cost ($30 per o1 iteration) meant o1 ran once.
- Founding-era evidence is theory (proofs), not empirical; "replications" do not apply. Complexity claims for weak diagnosability rest on the Miao et al. preprint.

## 4. Seen only in snippets or secondary text (not opened)

a02, a09, a14 (abstracts/DBLP), b17, b18, b19, b20, b21 (cited inside opened papers), c27 (search summary), c28 (GALA 42.22%, secondary). c24 and c25 numbers: only abstract-level. c26: abstract only.

## GAPS

1. Does an LLM, given a small system model and a probe set, correctly say "these two faults cannot be told apart by any allowed probe" (decide diagnosability)? No study found; it is the direct test for the agent.
2. When a probe is available that would separate the top two hypotheses, how often does the LLM choose it without a scaffold (redundant-probe rate, EIG=0 questions) across models 2025-2026?
3. Does the SIA result (ask the question that separates the top two) replicate on an independent benchmark and by a different group, at equal tokens against best-of-N?
4. How much of the potential-final gap in diagnosis tasks is true non-diagnosability (evidence cannot separate) versus selection error? Need cases with a known isolability matrix.
5. Do LLMs name multi-fault candidates when prompted for a minimal candidate set (hitting sets), beyond the one Plank scenario? Compare enumeration by LLM vs by code as faults rise past 150 diagnoses.
6. Does abstaining ("need another probe") when the evidence is provably non-diagnosable improve calibrated accuracy, and what do current benchmarks (Cloud-OpsBench Hard performance faults) reward?
7. Is the information-gain gain preserved at truly equal tokens and with open-set (no supplied candidates) in real fault tasks? UoT matched cost was 2x.
8. Do strong 2026 models (not GPT-4, GPT-4o) still show the UoT and BED-LLM gains, or has native reasoning closed the gap? UoT and BED-LLM used older models.
9. Does the choice of sensor/probe order (cost-aware, NP-hard in general) matter for LLM agents: does a cost-weighted probe operator beat cheapest-first at equal budget?
10. Does the explicit hypothesis ledger (GoS, BED-LLM) help because of state tracking or because of the information-gain step? Ablate each separately.

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d19). Search tools were limited (arXiv, OpenAlex and Semantic Scholar rate limits; WebSearch budget gone), so gaps 3, 5, 7 and 9 got no new sources.

1. Gap 1 (LLM decides diagnosability): STILL OPEN. No direct test found. Nearest: Gogleva et al. 2026 probe 1, where models given two near-identical predictions picked the closer one instead of saying "uninformative" (accuracy 0.30 to 0.53 on 43 items, d04); and NetFlow-DSR, where code makes the observability verdict and the LLM only labels roles (d15, d16). New claim K32 records the absence.
2. Gap 2 (redundant-probe rate): PARTLY CLOSED. Seven 2026 LLMs chose separating experiments 24.1% of the time vs 19.2% random over 6,596 experiments (d03). Cloud-OpsBench gives only a repeat-call proxy (RAR 0.45 for Qwen3-8B, near 0 for GPT-5; d14). K10 moved from contested to established.
3. Gap 3 (SIA replication by another group): OPEN. Nothing found. Only a different-domain EIG use (d19, abstract only).
4. Gap 4 (non-diagnosability vs selection error): PARTLY CLOSED, one domain. With a known isolability matrix only 7 of 60 cases were structurally non-diagnosable (diagnosis 0.12), against 0.30 for the 39 resolvable ones (d02). Selection and evidence use dominate. K14 is now "established" with two sources (SIA, Gogleva), but they are different tasks and Gogleva's structural class is small.
5. Gap 5 (multi-fault enumeration vs code): OPEN. No new source.
6. Gap 6 (abstention): PARTLY ANSWERED. Cloud-OpsBench has no abstain option, and 22% of audited weak-process cases ended ambiguous (d13). Benefit of abstaining is untested.
7. Gap 7 (equal tokens, open set): OPEN. New cost data: BED-LLM runs 61x slower per game than a trained policy (d08), still not a best-of-N match.
8. Gap 8 (2026 reasoning models): OPEN, leaning negative. Reasoning alone lowered solve rate in a small model (d08), ASIG gain faded from 7B to 14B (d10), BED-LLM used no reasoning questioner (d12). K30 is "contested".
9. Gap 9 (cost-weighted probe order): OPEN. No source.
10. Gap 10 (ledger vs information-gain step): PARTLY CLOSED. BED-LLM ablation: ICL beliefs 46, filtered set with LLM judging 61, even-split 87, full EIG 95 (Qwen2.5-72B, Animals) (d11). State alone is not enough; the scored split carries most of the gain. Gogleva adds that the weak step is deriving each hypothesis's predictions (0.88 to 1.00 when given vs 0.51 to 0.74 when derived; d05).

Caveats: d07 shares authors and simulator with d01 to d06 (not independent). d17, d18, d19 are abstract-only. Gogleva et al. is a single group and a synthetic task.
