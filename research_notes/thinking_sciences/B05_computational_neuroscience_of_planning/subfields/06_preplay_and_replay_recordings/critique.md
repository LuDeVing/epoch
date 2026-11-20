# Critique: B05.06 Preplay and replay recordings (cross-check)

## Corrections and confirmations (sources re-opened this session, full text)
1. Silva, Feng, Foster 2015 (PMC6095134): CONFIRMED. 9803 Sleep-1 events; median abs correlation 0.174 vs 0.172 (rank-sum p=0.08); best-template 0.245 vs 0.258 (p=1); Levene p=0.44 and 0.77; L-ratio 435/442 (98%); 4 rats, 40 tetrodes, mean 61 cells.
2. Dragoi and Tonegawa 2011 (PMC3104398): CONFIRMED 14.2% preplay (P<1e-32 binomial), 16.2% familiar-track replay, 81.1% at the junction, 16.1% in the sleep-box sessions. (b14 was marked not opened; it now is.)
3. Dragoi and Tonegawa 2013 (PMC3670374): CONFIRMED 9.8% of events, 82.6% track coverage (n=1,388), forward:reverse 1.04, capacity "at least 15" tracks.
4. Pfeiffer and Foster 2013 (PMC3990408): CONFIRMED 144-373 trajectory events per session (25.3-43.9%), mean 103.6 ms, 40.0-199.1 cm, 0 of 2028 with P>0.02; Wilcoxon P 4.96e-22 and 1.12e-13. (b17 said page blocked; opened now.)
5. Denovellis 2021 (PMC8476125): CONFIRMED 10 rats; 96% (22,170/23,071) of classified and 86% of all 25,844 SWRs coherent; 14% (3295/23,071) had any incoherent segment. Added detail: 89% of SWRs (23,071/25,844) were classifiable at the 0.80 threshold.
6. Breffle 2024 (PMC11488848): CONFIRMED capacity about 8.6 tracks vs about 15 in Dragoi 2013.
7. Lin 2025 Sleep-time Compute (arXiv 2504.13171, full text): CONFIRMED about 5x less test-time compute, up to +13% and +18%; the 2.5x cost drop is for 10 queries per context. Added: 5 parallel sleep-time generations generally beat 10.
8. CORRECTION to b18 (Gillespie 2021, PMC8497431): the task was an eight-arm win-stay lose-switch maze with dynamic goals, four rats, NOT a W-track. Main result: pre-choice replay relates to reliably rewarded and less recently visited places, not to the upcoming choice, and not trial-by-trial to behaviour.
9. a05 to a08, a10, a12 numbers: no change needed.
10. Not re-opened (taken from earlier agents): Davidson 2009, Karlsson and Frank 2009, Olafsdottir 2015, Ambrose 2016 (z values missing), Jensen 2024, BrainMem, AWM, Reflexion, Voyager, CogEval.

## Contradictions between sources
- Preplay: Dragoi lab (mice contiguous arm, naive rats, 2011/2013/2025) vs Silva 2015 (no preplay on linear tracks in rats). The dispute is partly about templates, thresholds and shuffles (a21 notes 50 ms vs 100 ms silence and 4 vs 6 cells). Neither side is independent of its own lab. Olafsdottir 2015 (independent) finds weak, conditional preplay (7.37% cued, 4.41% uncued, p=0.33).
- Plan vs memory: Pfeiffer and Foster (future path to goal) vs Gillespie (past reward and recency, not choice). Task differs (open arena foraging vs eight-arm win-stay lose-switch), so both may hold.
- Capacity: 15 tracks (D&T 2013) vs 8.6 tracks (random-network model).
- Author lists for the 2025 Dragoi paper differ between a20 (Farooq, Zhou, Sibille, Dragoi) and b09 (Zhou, Sibille, Dragoi). Treat a20 and b09 as one source; the title also differs ("Generative emergence" vs "...in the hippocampus"); resolve before citing.

## Duplicates (do not count as independent)
a12 = b01; a03 = b05; a14 = b06; a18 = b07; a20 = b09. Claim K06, K09 and K10 counts reflect this.

## Weak spots
- Foster and Wilson 2006 and Foster 2017 (a01, a17) were abstract-only; no spike counts or compression factors recorded. This is the most-cited paper in the subfield and has no numbers here.
- Ambrose 2016 z values truncated.
- Most LLM entries (c08 to c20) are abstract-only. BrainMem noise is large (2-point steps, about 50 tasks).
- No LLM study directly tests preplay/replay. Everything LLM-side is analogy: memory, sleep-time compute, trajectory reuse.
- Model papers (Jensen, c05, Diekmann) are small tasks; c05 has no numbers.
- Network was unreliable this session (S2 429s, Europe PMC 503s); only 8 numbers cross-checked from full text.

## GAPS
1. Does a backward credit-assignment pass after a failed LLM attempt (outcome to earlier steps) beat forward re-reading at equal tokens? (No LLM study found.)
2. Does a pre-answer forward-rollout of candidate paths beat act-then-revise at equal tokens, and where does it saturate (Jensen: about 15 rollouts)?
3. Is sleep-time precompute (Lin 2025) beneficial when the query is NOT predictable from the context? Their gain correlates with predictability; the boundary is not measured for reasoning tasks.
4. Foster and Wilson 2006 and Foster 2017 full numbers (event counts, compression, rat counts) are missing.
5. Gillespie vs Pfeiffer: which task features decide whether replay encodes the future or the past? Directly relevant to whether the agent should plan or consolidate at a given state.
6. Do the 2023-2026 replication attempts of preplay (beyond Silva 2015, Olafsdottir 2015, Breffle 2024) exist, e.g. Farooq and Dragoi 2019 developing animals, Shin/Jadhav W-track data? Not opened.
7. Does prioritised replay (Mattar and Daw 2018; Sagiv 2025; Antonov and Dayan 2025) outperform random replay in an LLM memory-review loop? Only gridworld evidence.
8. Does any LLM-agent memory paper ablate replay of stored trajectories alone (BrainMem, AWM)? Needed for the isolated effect.
9. CogEval per-model numbers for planning on cognitive maps (c08) were not captured.

## Gap search results (evidence_d.jsonl, d01 to d20; claims K20 to K29 added, K03 to K05, K14, K15, K19 updated)

CLOSED
- Gap 9 (CogEval numbers): closed. GPT-4 1-step 0.99, n-step 0.47, policy revaluation 0.21; one-cluster shortest path 0 of 30 at temperature 0. 2023 models only (d17).
- Gap 5 (plan vs memory): closed in part, mostly resolved. Same rats switch mode with engagement: engaged replay 62.26% direction-congruent vs 52.19% disengaged, 8 rats (d03). Humans: on-task replay goes with replanning, off-task with preferred paths, N=40 (d04). Mattar and Daw predict forward replay where Need is high, reverse where Gain is high (d05). Rule for the agent: plan at decision points, consolidate in idle time.

PARTLY CLOSED
- Gap 1 (backward pass vs forward re-read at equal tokens): still no inference-time test. Training-time evidence: HCAPO +13.8 ALFWorld over GRPO (d13). Frontier LLMs name the wrong culprit step most of the time (best 20.68% step-level, d14).
- Gap 2 (forward rollout vs act-then-revise): no equal-token test. Foresight tools are underused (under 1% invocation) and rollouts misused about 15% (d15). WebATLAS look-ahead is not ablated alone (d16). Saturation near 15 rollouts (Jensen) not re-tested.
- Gap 3 (sleep-time when query unpredictable): authors say less effective, gap widens with predictability bins, but no measured zero point and predictability is confounded with difficulty (d09).
- Gap 6 (preplay replications): found Farooq and Dragoi 2019 (same lab, preplay-like sequences from P17-18 in pups, d06) and a human cortex backbone-sequence study (looser test, d07). No independent 2023-2026 hippocampal preplay replication found. Shin/Jadhav W-track data not opened.
- Gap 7 (prioritised vs random replay): only gridworld (d05) and RL-training evidence (FreshPER, d18; replay buffer, d19). No LLM memory-review comparison. Priority needs an age decay.
- Gap 8 (replay ablation in agent memory): Hippo isolates comparison and update rule (d10); CER separates dynamics and skills (d11); but the token-matched study shows memory modules often lose to extra steps (d12, vanilla 44.78 vs 39.34 to 41.02 on Gemini 3 Flash). A critical review of that study (seen as snippet only) says the control was also strengthened.

STAYED OPEN
- Gap 4 (Foster and Wilson 2006, Foster 2017 numbers): Nature page paywalled, Annual Reviews page blocked, PubMed has only the abstract. No counts, compression or rat numbers. Needs library access (d01, d02).

New caveats found
- Multitask Preplay (d08) is the closest AI analogue of preplay (counterfactual pre-solving): 97.5% vs 5.56-8.22% for goal relabelling in grid worlds. Not a language-task test.
- Hippo no-memory at-least-once over 8 attempts is 73.6%, near its per-attempt 72.9%: retries may explain much of the gain (d10).
- Search budget: OpenAlex free quota and arXiv API returned limits partway; 5 WebSearch calls used. Several LLM papers dated 2026 (Hippo, 2606.15017, FreshPER) were read once and are single-source.
