# Critique, B05.04 Prioritised memory access (cross-check)

## Scope note
All four evidence files (a, b, c, d) were read in this pass. Many a and b lines are the same source read twice (Mattar and Daw, Ambrose, Liu 2021, Gillespie, Schaul, FreshPER). Counts in claims.jsonl count papers, not lines.

## Numbers re-opened (PMC full text, local arXiv text, eLife page)
Confirmed: Liu 2021 learning rates 0.79 vs 0.37 (gain) and 0.61 vs 0.54 (need); high vs low utility t(28)=3.30 p=0.003; 30 ms forward p=0.74; need levels 17/33/50%. Ambrose 2016: reverse z=3.57 p=3.6e-4; forward z=0.305 p=0.76; 581/738 classified (79%). Davidson 2009: 106/263 forward, 68/263 reverse, 89 mixed; 66/138 over 250 ms. Gillespie 2021: about two-fold previous-goal enrichment; R2 = 0.033/0.015/0.012/0.025; previous-goal vs later visits p = 0.49/0.32/0.18/0.08. Schaul 2016: 41 of 49 games; median 48% to 106%; 111% to 128%. FreshPER: +46/+367/+133/+18. Sun 2026: 23% to 62%. Yoo 2026: +0.61/+0.60/+1.66 pp. Momennejad p=0.0068 present on the eLife page; its other figures were not string-matched.

## Corrections
1. a16 (Davidson): forward more frequent is p<0.005 for all 263 events (binomial); for events over 250 ms the paper gives p<0.002. a16 merged the two.
2. b01 says the Mattar and Daw paper gives no numeric simulation results; a09 quotes event counts (about 2 to 0.8 per trial). Those are read off figures. Treat a09 as approximate.
3. b11 (Rainbow) is typed replication but is an ablation inside a new method. b13 and b14 are the real replication-style evidence.
4. a30 and b16 are the same paper (FreshPER). b22/b23 call three results independent, but a30 and b16 are one source. Claims count it once.
5. b05 "0.70 with 160 ms replay vs 0.61 without, p=0.023" is now CONFIRMED in the Liu 2020 preprint text (difference 0.09, p=0.023; forward 30 ms difference 0.01). Earlier note of 'unverified' is withdrawn.
6. K09 was set to established on two independent sources (Schaul, Rainbow ablation). Rainbow is not a clean replication, so this rests mostly on one family of results.

## Contradictions
- Gain x need is supported (Ambrose, Liu 2021), yet Gillespie 2021 finds replay tracks the previous goal, not the planned choice, and Carey 2019 (unopened) points the same way. Species, tasks and decoding differ.
- Direction: the model predicts forward before runs and reverse after; Davidson 2009 shows forward outnumbering reverse (40% vs 26%) in another design.
- Need alone: weak (p=0.16), from one human study.
- Priority helps in Atari (Schaul) but hurts or adds little elsewhere (Sujit, Fedus, FreshPER).

## Weak spots
- Founding studies (Foster and Wilson 2006, Diba and Buzsaki 2007, Pfeiffer and Foster 2013, Gupta 2010, Jadhav 2012, Widloski 2022, Moore and Atkeson 1993) were read as abstracts only. Diba numbers (841/887, 395/464) are second-hand.
- The model was not fitted; every match is qualitative.
- The human gain x need test has N=29 and one task; no replication found.
- All LLM evidence is replay of rollouts in RL fine-tuning. None tests a prompt-time scaffold or retrieval ordering. Chen 2025 and DyJR numbers are missing.
- Search was throttled (b24), so recall of 2024-2026 LLM-memory papers is probably incomplete.

## GAPS
1. Does any study order retrieval of stored items (agent memory, notes, subgoals) by an expected-value-of-update score and compare it with recency and random at equal tokens?
2. What cheap proxy for gain works in an LLM (self-rated chance the plan changes, logprob shift, critic score), and does it correlate with the true benefit of revisiting?
3. Has Liu 2021 (gain beats need in humans, N=29) been replicated or extended with a larger sample or another task?
4. What did Carey 2019 and later work find on replay of non-preferred outcomes, and how far does it limit the gain x need account (open the full text)?
5. What are the headline numbers in Chen 2025 (P2Value) and Li 2026 (DyJR), and do they separate ordering from filtering?
6. How much does stale priority hurt when the situation changes inside one reasoning episode (new evidence mid-problem), and how fast should priority decay?
7. Do later theory papers (2019-2026) fix the myopic and no-uncertainty limits (non-myopic or uncertainty-aware replay value; Jensen 2024 metalearned rollouts)?
8. Is backward (reverse) revisit better than forward revisit for credit assignment in LLM multi-step tasks, measured at equal tokens?
9. How do Dyna-style agents with learned models guard against compounding model error when prioritised backups run on simulated experience?

## Gap search results (evidence_d.jsonl, d01-d19)
Web search quota ran out early; the arXiv/OpenAlex/Semantic Scholar APIs returned 429, so work used Europe PMC, arXiv search pages, and direct PDF/HTML downloads. Closed means answered from opened text; partial means answered in part.

1. Order retrieval by expected value of update vs recency and random at equal tokens: PARTIAL. MemRL (d09) ranks stored episodes by a learned Q-value and beats similarity-only RAG (avg CSR 0.798 vs 0.699), but has no recency or random control at equal tokens and needs a reward critic. No gain x need test exists. Still open.
2. Cheap gain proxy: PARTIAL. Self-rated importance matched recency in a retention test (d10: F1 0.016 vs 0.017 at budget 32) and was never validated in Generative Agents (d11). Learned Q correlates with success (r=0.861, d09). A strength + similarity + inhibition-of-return rule nears Mattar and Daw in RL (d04, abstract only). No study correlates a logprob-shift or self-rated-gain proxy with true benefit of revisiting. Open.
3. Replication of Liu 2021: OPEN. Europe PMC scan of 128 citing records found no replication or larger-sample re-test (d18). Search is keyword-only.
4. Carey 2019: CLOSED (preprint full text, d01). 4 rats, 19 sessions; replay content biased away from the preferred arm (r(19)=-.75, p<.001), also before the task; does not predict trial-by-trial choice. Gagne and Dayan 2022 (d02) show gain x need with forgetting explains pessimal replay, so it limits need-only and recency rules, not gain x need. Journal version not opened.
5. Chen 2025 (P2Value) and Li 2026 (DyJR): CLOSED. P2Value large gains are distillation from GPT-4-turbo (GPT-Neo 5.73 to 42.12 pass); self-fine-tuning is small or negative; no ordering ablation (d06). DyJR separates admission from use: +2.5/+3.7 for confidence admission, +1.5 for JS over policy-gradient, 29.8 to 34.1 overall (d07). Neither separates ordering from filtering by rank; DyJR separates filtering. K14 downgraded.
6. Stale priority and decay: PARTIAL. FreshPER tau=500 vs 1000 by drift speed (d08); DyJR shortest window best (d07). Nothing inside a single reasoning episode. Open for that case.
7. Theory fixes: PARTIAL. Uncertainty addressed (d02); learned triggering (d03); myopic limit not addressed in any paper found (d19). Jensen 2024 sidesteps rather than fixes the myopic limit.
8. Reverse vs forward revisit in LLM tasks at equal tokens: OPEN. Only listing-level hits on step credit assignment (d17); none opened, none test direction.
9. Dyna and compounding model error: CLOSED for RL. MBPO short branched rollouts (d12); Panahi 2024 shows neural PER can still spike (d13). No LLM-specific study found.

Corrections to earlier notes: P2Value headline numbers were inflated by distillation (see d06). The b05 figure "0.70 vs 0.61, p=0.023" is still unverified. New claims K18-K23 added; K06, K10, K11, K14, K15, K16, K17 revised. Not opened: Eldar 2020, Wimmer 2023, Diekmann 2023, Panahi full text, SRPO, FOCUS, TTEL, journal version of Carey.

## Cross-check pass (second run, with evidence_c and evidence_d)
Re-opened this pass and CONFIRMED against full text: Schaul 2016 (48% to 106%, 111% to 128%, mean 418% to 551%); Fedus 2020 (+17.3% with 1M to 10M without prioritisation; -2.3% without n-step); Liu 2021 (gain 0.79 vs 0.37, need 0.61 vs 0.54, t(28)=3.30 p=0.003, forward t=-0.34 p=0.74, backward-replay learning rate 0.70 vs 0.61 p=0.023); Ambrose 2016 (reverse z=3.57 p=3.6e-4, forward z=0.305 p=0.76, 581/738 = 79%); Momennejad 2018 (rho 0.54 p=0.0068, t(23)=4.89, difference p=0.023); Jensen 2024 (r=0.186 string present); Eldar 2020 (11.1% string present); Park 2023 (29.89 present); MemRL (r=0.861 present); DyJR 34.1 present in the paper text.
No number was found wrong. Status fixes: K14, K17, K22, K23 changed to single-source (statuses must be one of four values; K17 and K22 rest on one opened source or an abstract). K24 added.
Not re-opened and still second-hand: Diba 2007 counts, Moore and Atkeson, Foster and Wilson, Pfeiffer and Foster, Wimmer 2023, Diekmann 2023, Panahi 2024, SRPO, FOCUS, TTEL.
Caution: c-file LLM-memory papers (MemRL, ReMe, APEX-EM, trajectory memory) report gains from outcome-weighted retrieval, but none has a recency or random control at equal tokens, so none supports gain x need directly.

## GAPS (final list, most decision-relevant first)
1. Does ordering stored subgoals or notes by an expected-value-of-update score (gain x need) beat recency and random at equal tokens in a prompt-time scaffold?
2. Which cheap gain proxy (self-rated chance the plan changes, logprob shift, critic score, dependency count) predicts the real benefit of revisiting an item?
3. After a changed fact, does backward revisit from the change point beat forward re-read at equal tokens in LLM multi-step tasks?
4. Has Liu 2021 (gain over need, N=29) been replicated with a larger sample or another task, and does need alone ever carry an effect?
5. How fast should priority decay inside one reasoning episode when new evidence arrives, and does event-driven reset beat time decay?
6. Does scoring a subgoal together with its dependants (non-myopic gain) beat single-item gain?
7. Does an ordering ablation (priority vs uniform at equal sample count) exist for P2Value, advantage replay or MemRL?
8. What are the exact counts in the founding rodent papers (Foster and Wilson 2006, Diba and Buzsaki 2007, Pfeiffer and Foster 2013) from the full text?
9. How do LLM agents with prioritised self-simulation limit compounding model error, with real feedback after each imagined step?

## Gap search results (final run, evidence_d.jsonl d01-d33; claims K25-K29 added)
Method: 6 of 8 allowed WebSearch calls, plus Europe PMC, arXiv full texts and PMC pages. OpenAlex had no budget left. Old lines d01-d19 were kept as they were; d20-d33 are new. Closed means answered from opened text.

1. Gain x need order vs recency and random at equal tokens, prompt time: OPEN (partial). Nearest: Yoo 2026 (d20), uniform vs |advantage| at equal replay count, +0.39 avg and +3.39 pass on Qwen3-1.7B, single seed, training time; Chen and Cheng 2026 (d21), learned value 0.770 vs recency 0.368 vs random 0.300 gold retention, retention not order; WMT (d24), +9.97 pp over linear history with 32.8% fewer tokens, no recency or random control.
2. Cheap gain proxy: PARTIAL. SRPO (d22) shows the model's own first-wrong-step judgement beats random reset (clean-prefix 28.7% vs 16.3% Pass@4), but half of its self-localisations overshoot. Chen and Cheng (d21): a relevance cue scored against the future question gets 0.979 but 0.286 blind. No study correlates a proxy with true benefit of revisiting.
3. Backward vs forward revisit at equal tokens: OPEN. SRPO and listed credit-assignment papers revisit the first error, but none compares directions.
4. Liu 2021 replication: PARTIAL. No same-task larger-sample replication found. A Neuron 2026 iEEG study (d29, N=34, abstract only) extends it: ripples carry which indirect experience is most valuable to update. Need alone: a 2026 rat preprint (d28) finds time and behavioural state, not reward, shape replay, which argues against utility-only accounts.
5. Priority decay inside one episode: PARTIAL. WMT (d24) decays by missed selection, not elapsed time, and invalidation suppresses directly; MemDecay (d25) measures half-lives 148 to 189 vs 14 to 16 steps by region. No ablation of decay vs event reset.
6. Non-myopic gain (subgoal plus dependants): OPEN. STALE (d23) shows propagated conflicts are harder (best plain model 55.2%; dependency search 68.0%); WMT branch priority scores a subtree. No ablation of single-item vs dependant-scored gain. Sagiv 2025 (d30) extends need to future goals.
7. Ordering ablation for P2Value, advantage replay or MemRL: PARTIAL. Closed for advantage replay (d20, equal-count uniform control). Still absent for P2Value and MemRL.
8. Founding rodent counts: CLOSED for Diba and Buzsaki 2007 (d26: 36% forward, 19% reverse; 841/887; 395/464) and Pfeiffer and Foster 2013 (d27: 2,028 events, none above P 0.02). Foster and Wilson 2006 and Gupta 2010 were not opened (no open full text found).
9. LLM prioritised self-simulation with real feedback: OPEN. Search found Imagine-then-Plan, GILP and others (d32), listings only, none opened.

Corrections: none of the earlier numbers was found wrong. The Diba counts are no longer second-hand. Still not opened: Foster and Wilson 2006, Gupta 2010, Jadhav 2012, Widloski 2022, the Neuron 2026 iEEG paper body, the journal Carey 2019, Imagine-then-Plan, GILP.
