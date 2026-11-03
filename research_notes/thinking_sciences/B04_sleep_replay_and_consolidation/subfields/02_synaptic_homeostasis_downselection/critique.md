# B04.02 Synaptic homeostasis / down-selection: cross-check critique

Checker run 2026-11-03. Evidence files read: evidence_a (28 lines), evidence_b (32), evidence_c (25). Claims: claims.jsonl (22 claims, K01-K22).

## Numbers re-opened and confirmed (source text read this session)

1. de Vivo 2017 (PMC5313037): ASI -18.9% vs spontaneous wake (p=0.001), -17.5% vs enforced wake (p=0.003), SW vs EW -1.7% (p=0.957); 6,920 synapses. Confirmed (full text).
2. Diering 2017 (PMC5382711): more than 4500 PSD proteins, close to 10,000 phosphopeptides, about 20% regulated. Confirmed (full text).
3. Cary and Turrigiano 2021 (PMC8275129): rats P25-P31, n=30 animals for state behaviour, mEPSC stable in V1 and PFC. Confirmed (abstract and methods). The authors themselves note sleep at this age is fragmented with weak SWA homeostasis, a boundary condition for the null.
4. Torrado Pacheco 2021 (PMC7864886): +114% +/- 23% on ER2, +2% +/- 13% on ER4, controls 10% +/- 18%, 30/36 neurons (83.3%). Confirmed.
5. Kuhn 2016 (PMC4996971): Condition F(1,19)=7.5, p=0.013, partial eta2 0.283; Condition x Time F(3,57)=3.5, p=0.021, 0.156. Confirmed.
6. Nere 2013 (PMC3786405): procedural 80% (S/N 4) to 90% (S/N 9); declarative 87% to 75% vs 53% without sleep; misfit memory depressed 28% and 11%. Confirmed.
7. Tadros 2022 (Nat Commun / PMC9755223): Table 1 values 19.49, 48.47 +/- 5.03, 77.04, 79.91, 86.47; CUB-200 sleep 63.2 / 45.4; CIFAR-10 44% vs 19%. Confirmed.
8. Xiong 2025 (arXiv 2505.16067): strict-evaluator no-deletion 70.95/2938, 51.00/1178, 85.40/904; history-based 42.06/784, 51.81/846, 89.60/788; combined 42.34/248, 49.97/323, 85.50/188; periodic deletion 67.65/949 and 69.80/2286. Confirmed from PDF text.
9. Chauhan 2026 RSPM (arXiv 2610.25561): 40.0% to 49.1%, +9.1, p=0.0003; 30.6% fewer entries; 92.5% temporal consistency vs RAG 80.6%. Confirmed. The abstract also gives the other two gains (+11.9 temporal, +7.6 LoCoMo) and about 93% fewer retry loops.
10. Massey 2026 (arXiv 2601.08447): STDP-SNN best at about 10-20% sleep, SG-SNN best at 0% sleep. Confirmed in text. SCM (2604.20943) and SleepGate (2603.14517) abstracts also confirmed (90.9% noise reduction; 99.5% depth 5, 97.0% depth 10, baselines under 18%).

## Corrections

- a26 error: "after a second sleep period overall accuracy on both tasks 90%" was attached to the CUB-200 baseline (5% / 95%). In the paper the 90% belongs to the reduced class-incremental MNIST task (digits 0,1 then 2,3), not CUB-200. The CUB-200 sleep result is 63.2% / 45.4% (c01). Treat a26's 90% as the MNIST 0/1 then 2/3 task only.
- c11 / c12 vs the paper: Xiong 2025 prints EHRAgent no-deletion as 38.50 in one table (strict row in the evaluator table) and 38.67 in Figure 5. The paper is internally inconsistent by 0.17. Gains of history-based deletion (+3.4 to +3.6) hold either way. Use 38.5-38.7.
- c12: RegAgent row 67.65 with 949 records is now confirmed (not "about"). Periodic deletion cut records by 68% at a cost of 3.3 points, so "small loss" is not free.
- a14 vs b01, a18 vs b13, and a26 / b22 / c01-c03 are repeated readings of the same papers (de Vivo 2017, Cary 2021, Tadros 2022). Counted once in independent_sources.
- a15 vs a17: the "small vs large" disagreement between de Vivo and Diering rests on Tononi and Cirelli's summary of Diering; the Diering abstract does not state it. Marked contested, one side second-hand.

## Contradictions between sources

- Juvenile rat cortex shows no sleep downscaling (Cary 2021, a18/b13) while adolescent mouse EM shows -18% (de Vivo 2017) and 2-week-old pups -33.9% (de Vivo 2019, b14). Species, age and readout (mEPSC vs ASI size) all differ; no one study varies them.
- Hippocampus: Spano 2019 (larger ASI after wake, abstract only) vs Havekes 2016 (fewer spines after 5 h of sleep deprivation, abstract only). Spine number and synapse size are different variables.
- Firing-rate homeostasis: Hengen 2016 (recovery in wake) vs Torrado Pacheco 2021 (downward return in sleep). Torrado Pacheco reconciles them as upward-in-wake, downward-in-sleep. Watson 2016 shows homogenising, not uniform lowering.
- Sleep as potentiation: Aton 2014, Yang 2014, Li 2017, Zhou 2020 show sleep adds or keeps synapses. Not a refutation of net renormalisation, but it rules out "sleep only deletes".
- AI studies: SRC alone loses to rehearsal and OWM on most sets (Tadros) while the sleep-inspired LLM-memory papers report large wins over add-only. The sleep benefit in AI is mostly shown when combined with a replay path.

## Weak spots

- Most of the experimental support is from one lab (Tononi/Cirelli: Nere, de Vivo 2017 and 2019, Spano 2019, Bushey 2011, the 2012-2022 reviews). Independent labs (Cary, Diering, Torrado Pacheco, Kuhn) give mixed to supportive results.
- de Vivo 2017: 12 mice, one layer, snapshot design; structural proxy, no tagging of individual synapses through a learning episode (admitted in a28).
- No study connects downscaling to a specific piece of learned content. All AI mappings are by analogy.
- Every LLM "sleep" memory paper is single-group and self-benchmarked (K18). RSPM's SWE-bench part is a simulation. SleepGate is a 793K-parameter toy with synthetic tokens, so nothing here shows transfer to a real LLM.
- Xiong 2025 is the best agent-memory study but covers four agents, its strict evaluator effectively gives ground truth, and the effect shrinks or vanishes with weak evaluators.
- Mem0, FadeMem and MemoryBank claims are partly judge-model scores; FadeMem margin over Mem0 is about 1 F1 point.

## Seen only in abstract or snippets (full text not opened)

Aton 2014 (b06), Zhou 2020 (b08), Hengen 2016 (b10), Vyazovskiy 2009 (b11), Watson 2016 (b12), Spano 2019 (b15), Havekes 2016 (b16), Bridi 2020 (b17), Gonzalez-Rueda 2018 (a23 second-hand, b18 abstract), Frank 2012 (b05), Vyazovskiy 2008 (a24, second-hand), Tononi and Cirelli 2003 (a25, never opened), MemGPT (c24), A-MEM and Voyager (no pruning numbers). Li 2017 (a19) has no numbers. Claims that depend on these are tagged contested or single-source or hedged in the claim text. Note: several lines above are marked opened:true in the evidence files while the numbers were taken only from abstracts; treat opened flags on b-lines as abstract-level unless listed in the confirmed section.

## GAPS (most decision-relevant first)

1. Does a scheduled prune pass over a lesson store beat add-only at equal total tokens on a real, multi-episode agent stream (not synthetic)? Only Xiong 2025 (four agents) and a simulation (RSPM) speak to this.
2. What fraction to prune? Robinson 2022 (best at p=0.75 of weights), Massey 2026 (10-20% sleep) and Xiong (66-91% record cuts with small loss) give different scales. Is there an interior optimum for lesson counts, and does it depend on store size?
3. Which pruning rule: age decay, use-count (ExpeL votes), outcome-linked reinforcement (protection-from-depression analogue), or size-based protection (de Vivo large-synapse spare)? No study compares these head to head in LLM memory.
4. How reliable must the utility signal be before pruning stops helping? Xiong shows weak evaluators remove the gain; find the threshold for a self-judging agent without ground truth.
5. Prune-only vs prune plus merge: does distilling surviving lessons into rules (RSPM, SCM) add benefit over deletion alone, and what does it lose (dates, conditions, per Kyrkewood)?
6. Is the early dip then gain pattern (Nere declarative: 87% to 75% to 94% over 10 cycles) visible in LLM memory, i.e. does one prune cycle hurt and several help?
7. Does pruning during the task (online, wake-like) differ from a separate offline pass over the whole store (recency-bias argument, a02)? Not tested anywhere.
8. Do sleep-inspired replay and downscaling add anything beyond a small raw-episode buffer once tokens are matched? Tadros shows the combination wins at small buffers (K=100: 65.5 to 78.1) and little at large ones.
9. Age dependence: does the benefit of pruning appear mainly in young stores that are saturating and vanish in mature, stable ones (Cary vs de Vivo, adult mice)? Any analogue for stores of lessons after hundreds of episodes?
10. Independent replication of any 2026 LLM sleep-memory paper (RSPM, SCM, SleepGate, ZenBrain) on a public benchmark with real model calls and equal tokens.


## Gap search results

Run 2026-11-03. Search tools were mostly blocked: WebSearch budget used up, arXiv API/search, Semantic Scholar and OpenAlex returned 429 or no credit. Work was done by opening full PDF text of papers already named in the evidence (Xiong 2025, ACE, Dynamic Cheatsheet, ExpeL, RSPM, SleepGate, FadeMem, AWM, Reflexion) and reading the parts that bear on the gaps. New evidence: evidence_d.jsonl (d01-d18, all opened). New claims K23-K31; K12-K14, K16, K18, K19 extended.

1. Prune pass vs add-only on a real multi-episode stream: PARTLY CLOSED. Xiong 2025 (four agents) shows add-all is worse than a 100-record fixed store (RegAgent 55.48 at 4100 records vs 67.53 at 100) and that utility-based deletion keeps or raises accuracy at 66-79% fewer records. Dynamic Cheatsheet shows full-history append can fall below no memory (GPT-4o AIME 2024 20.0 to 6.7). Still no public, independent, equal-token comparison on a new stream.
2. What fraction to prune: STILL OPEN. ACE finds no sensitivity to prune trigger from 10K to 100K tokens (78.6 to 78.3). Xiong shows 66-91% record cuts with 0-4 points lost. No sweep of prune fraction against store size exists. Interior optimum unproven.
3. Which rule: PARTLY CLOSED for one comparison. Xiong strict evaluator: outcome-linked (history) deletion beat frequency (periodic) on all four agents (e.g. CIC-IoT 89.60 vs 80.80). SleepGate toy: use-count style retention (H2O) kept stale items. Age decay alone: no ablation anywhere; protection by size (de Vivo analogue) untested; ExpeL vote rule untested alone.
4. Utility-signal reliability threshold: PARTLY CLOSED, no threshold number. A judge fine-tuned on 300 labelled outcomes helped; ACE survived 1 bad update in 5 and lost 4.0 points at all-bad; RSPM shows a failure-attribution rule can cost 19.5 points on a hard task. Self-judging with no outcome signal: degrades, not measured by level.
5. Prune-only vs prune plus merge: STILL OPEN. Indirect only (ACE incremental edits, FadeMem fusion ablation by its own authors, RSPM has no prune-only arm). Loss from distilling (dates, conditions) rests on Kyrkewood alone.
6. Early dip then gain: STILL OPEN. No LLM-memory paper reports per-cycle accuracy through repeated prune cycles. Closest: ACE shows 10 reflection rounds worse than 5; RSPM reports baselines decay while RSPM does not as conversation length grows, no cycle-by-cycle numbers.
7. Online vs offline prune pass: STILL OPEN. AWM offline vs online is an indirect, add-only comparison (similar in-domain; online better under mismatch). Recency-bias argument stays untested.
8. Replay and downscaling beyond a small buffer: NOT RESEARCHED in this pass (no new source); remains as in Tadros (benefit at small buffers).
9. Age dependence (young vs mature stores): STILL OPEN. SleepGate fails past about 15 near-duplicates (toy). No LLM study stratifies by store age.
10. Independent replication of 2026 sleep-memory papers: STILL OPEN. None found; search was blocked. RSPM turned out to be a short paper with a simulated SWE-bench arm.

Net: the strongest usable guidance for the agent is (a) prefer outcome-linked deletion to frequency or age deletion, (b) make edits per item, never rewrite the whole store, (c) cap prune fraction per cycle and guard against pruning after hard-task failures, (d) calibrate the utility signal on a small labelled set. All of it rests on Xiong 2025 and ACE, authors' own benchmarks, not independent replication.
