# B04.03 Relevance-based fate of memories: cross-check critique

## Sources re-opened (full text this session)
Wilhelm 2011 (PMC6623736), Wamsley 2016 (PMC5070851), Kolibius 2021 (PMC7821853), Van Dongen 2012 (PMC3420871), Davidson and Pace-Schott 2021 (PMC8318217 tables), Chen and Cheng 2026 (arXiv 2606.12945), Lin 2025 sleep-time compute (2504.13171), Annapureddy 2026 (2609.33013), Xiong 2025 (2505.16067).

## Confirmed
- Wilhelm 2011: 117.29+-3.54 vs 105.23+-3.01 (p=0.014); interaction p=0.05; card locations 98.80 vs 73.13 (p=0.019); tapping 131.13 vs 116.95 (p=0.037); stage 4 8.20 vs 4.07 and 11.72 vs 5.11. N=142 participated in Exp 1; Davidson counts 104 in the main dataset (the rest are wake or excluded subgroups).
- Wamsley 2016: expectation main effect F(1,71)=7.35 p=.008; interaction F=0.77 p=.38 (completion time), F=0.96 p=.33 (motor).
- Kolibius 2021: N=78, wake -11.2 vs sleep -8.5, F(1,74)=1.25 p=.27; BF01=8.26 against harm, 1.45 for benefit.
- Van Dongen: F=13.19 p=.001 (is the relevance x group interaction on change scores; also reported as the 3-way with session); 50 analysed, 10 excluded for doubting the instruction.
- Chen and Cheng: 0.770+-0.011, 0.657, 0.518, 0.368, 0.286, 0.979 (oracle), gaps +0.120/+0.402/+0.277 with CIs; weights 0.64/0.55/0.23/0.00. Bootstrap B=103.
- Lin 2025: 5x test-time compute reduction, +13 percent and +18 percent.
- Annapureddy: +22.7 percent, CI [+1.89,+11.34] pp, 7.17x compression, 0.319 vs 0.333, 74 percent, -15.0 pp.

## Corrections
1. Kolibius (b24/c24 limits): "short retention interval" is wrong. Recall was tested after another night of regular sleep; the manipulation was sleep vs staying awake during the night after a full day of learning 640 pairs.
2. Xiong 2025 (c05): the table was misread. Under the strict evaluator, no-deletion is RegAgent 70.95 (2938 records), EHRAgent 38.67 (1012), AgentDriver 51.00 (1178), CIC-IoT 85.40 (904). The 63.18 figure for RegAgent belongs to another row and should not be used. Periodic: 69.80/38.59/50.94/80.80. History-based (reading the two-column layout): EHRAgent 42.06, AgentDriver 51.81, CIC-IoT 89.60; combined 42.34/49.97/85.50. So the claim "history deletion hurt AgentDriver" is not supported by the strict table (51.00 to 51.81); it may apply to a different evaluator. The text extraction is two-column and interleaved, so exact cell pairing stays uncertain; check the figure before citing.
3. Wamsley N: b05 says N=100 (74+26); the Davidson table lists VMT n=75 and MST n=94 and the paper's cell sizes are 18/28/21/30 for the maze groups. Cite "about 100, task-specific n 75 and 94".
4. Wilhelm Exp 1 final cell sizes in a01 (sum 142) mix tested and analysed groups; use 104 for the main dataset when comparing with Davidson.

## Contradictions between sources
- a16 (test expectancy: 3 positive, 2 none, 1 opposite) vs b07 (4 papers, interaction in 2 of 4). Different counting of datasets; both agree the evidence is mixed. Davidson's table lists Wilhelm as the only clean positive with a wake control plus Van Dongen.
- Wake behaviour of Wilhelm, Van Dongen and Wamsley disagree (claim K05).
- Saletin 2011 positive vs Kurdziel 2025 and Rauchs null (K08).
- Several 2026 LLM memory papers report gains from forgetting (K15) while ZenBrain, RD-Forget framing and ConsolidationBench show heavy risk (K16). They use different loads and metrics, so they do not directly conflict.

## Weak spots
- Human core is small samples, one participant per night, between-subject designs, flexible exclusion of suspicious subjects. Davidson calls this a replication problem with winner's-curse inflation.
- No meta-analysis of the test-expectancy effect exists.
- Feld and Born 2019/2020 is a review with no new data on relevance; the reconciliation (strengthen relevant, erase weak) is a framing, not tested head to head.
- Almost all LLM results are 2026 preprints, many author-built benchmarks, some on toy models (SleepGate 793K parameters, SCM eight author tests). Most proxy for relevance by retrieval count, recency or LLM rating.
- No LLM study tests the human claim directly (expected future use raising retention).
- Sleep-time compute is a compute-saving analogy, not a retention-by-relevance test.

## Only seen in snippets or abstracts
Fischer and Born 2009 (abstract), Rouast and Schoenauer 2023, Lewis and Durrant 2011, Tononi and Cirelli 2014, Diekelmann and Born 2010, Brokaw 2016, Stickgold and Walker 2013 (not opened), Reverberi 2020 (via review table only), Stamm 2014 (via review), Tamaki 2020, Prehn-Kristensen 2018, Barner 2023 and several 2026 LLM papers (not re-opened by the cross-checker; numbers taken from the finding agents).

## GAPS
1. Does an LLM-rated or outcome-based "future use" tag at write time predict real later reuse of an agent lesson better than recency or access count? (No direct test found; most decision-relevant.)
2. At equal tokens, does keeping lessons by expected future use beat keep-all, recency and uniform pruning on a multi-task stream, and at what store size does pruning start to pay (Kolibius load boundary)?
3. Soft forgetting (suppress, keep source) vs hard deletion: what is the measured loss rate of needed lessons for each in long agent runs?
4. Is there a pooled effect size (meta-analysis) for test expectancy x sleep, including unpublished nulls and Barner 2023, and how large is it?
5. Does the relevance instruction effect depend on strength of encoding (weak traces gain more), and does that map onto keeping weak but relevant lessons?
6. Which write-time signals (surprise, effort, theta-like markers analog) predict later use in agents, as the 2026 theta-tagging study suggests for humans?
7. Does offline precomputation (sleep-time compute) transfer to lesson distillation: how much of the +13/+18 percent gain survives when the future query distribution is uncertain?
8. Are the 2026 forgetting gains (FadeMem, OBLIVION, SF-AMS, RD-Forget) reproducible on independent benchmarks and with answer accuracy rather than retention proxies?
9. Xiong 2025 table: does history-based deletion help or hurt each agent under each evaluator (needs the figure, not text extraction)?
10. Do directed-forgetting style explicit "drop" instructions help an LLM agent avoid interference, as in SleepGate, without a custom-trained gate?

## Gap search results
Evidence is in evidence_d.jsonl (d01 to d18); claims K01, K02, K10, K14, K15, K17, K18, K20 were updated and K21 to K26 added. Limits of this pass: the WebSearch quota ran out, and the arXiv, Semantic Scholar and OpenAlex search APIs were rate limited. Europe PMC search, direct PMC/arXiv full texts and pdftotext still worked. So human-side gaps were searched; a fresh sweep of 2026 agent papers was not.

Closed or mostly closed
- Gap 9 (Xiong 2025 table): closed with moderate confidence (d07). Rows were paired using the memory-size ordering, which matches the text. Strict evaluator, none to history: RegAgent 70.95 to 67.65 (hurts), EHRAgent 38.67 to 42.06, AgentDriver 51.00 to 51.81, CIC-IoT 85.40 to 89.60. Coarse evaluator: RegAgent 63.18 to 60.88, EHRAgent 25.91 to 33.55, AgentDriver 36.92 to 34.00, CIC-IoT 74.00 to 78.10. The Figure 5 panels were not viewed. The earlier note that history deletion does not hurt AgentDriver holds only for the strict evaluator.
- Gap 10 (drop instructions): closed for the in-context case (d05, d06). Wang and Sun 2025 tested a per-key "forget all previous updates" prompt in five LLMs: under 10 points gain, negative for gpt-4.1-mini, errors cluster at the instruction. Only a fake Q&A reset helps. SleepGate itself does not test a prompted frontier model.
- Gap 7 (sleep-time compute under uncertainty): partly closed (d13). Gain widens with query predictability (five quantiles, bin values only in a figure), and on SWE-Features it holds only at low test-time budgets. Transfer to lesson distillation is untested.

Partly closed
- Gap 4 (pooled effect): no meta-analysis exists (d18). A rough own pool of five interaction tests, signs set positive, gives r about 0.10, CI 0.01 to 0.18 (d02). Ashton and Cairney 2021 (d01, N=162 and 124, BF01 2.5 to 4.0) is a clean direct replication failure that earlier files lacked. A real meta-analysis with unpublished nulls is still needed.
- Gap 5 (encoding strength): Petzka 2021 (d03) shows the weak-trace sleep advantage is largely a ceiling effect under easy testing; Schabus 2025/26 (d04, N=90, abstract only) shows sleep protects weak and strong alike. Neither tests relevance. Implication: do not drop weak lessons by strength alone.
- Gap 3 (soft vs hard): RD-Forget (d10) measured the rescue path at 3.5 to 9 points; ConsolidationBench (d09) shows rollback restoring success from 0.0 to 1.0 and hard forgetting destroying 74 percent of load-bearing clusters. No paper runs suppress versus delete head to head with a loss rate for needed lessons.
- Gap 8 (independent benchmarks): RD-Forget and OBLIVION report answer accuracy on public benchmarks (LongMemEval, LoCoMo-style, MemoryAgentBench, BEAM, PersonaMem, GoodAI LTM) but all are by the method's authors. OBLIVION is near parity with flat retrieval (90.60 vs 89.00) and saves tokens; with a strong large-window model full context stays competitive. FadeMem's headline retention figure is on its own benchmark. No third-party reproduction found.

Still open
- Gap 1 and gap 6 (does a write-time tag predict real reuse; which signals): no direct test found (d16, d17). Search was truncated, so recheck when quota returns. Closest proxies are outcome-based (retrieval-utility history, hindsight regret precision 0.93), which exist only after use. Chen and Cheng weights are fitted to gold-evidence retention, not reuse (d08).
- Gap 2 (equal-token comparison and store-size threshold): not measured. Only the human 640-pair boundary (d14) and Xiong memory sizes (d07) exist. K25 records this.

Corrections to earlier files
- Ashton and Cairney 2021 should be added to K01/K02 as the main replication failure; it was missing from the earlier synthesis.
- Wamsley 2016 is described in Ashton and Cairney as "no impact of future-test knowledge", but Wamsley found an expectation main effect in both wake and sleep (consistent with K03); cite Wamsley's own result.
