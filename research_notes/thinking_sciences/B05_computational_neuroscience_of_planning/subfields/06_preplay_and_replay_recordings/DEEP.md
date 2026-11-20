# Preplay and replay recordings: deep document

*Subfield B05.06. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b25, c01-c26, d01-d20), claims.jsonl (K01-K29), critique.md. Status words follow claims.jsonl. Numbers are from pages opened in this run unless marked. Foster and Wilson 2006 and Foster 2017 have no figures here (paywalled).*

## 1. What it is

Place cells in rodent hippocampus fire at set places. Their spikes can also be recorded when the animal is still, in short bursts called sharp-wave ripples (SWRs, about 50 to 120 ms). In a burst, cells often fire in an order that matches a path through space. The path is "played" in a fraction of a second. Three timings matter.

- **Replay**: the order matches a path the animal already ran. Seen after a run (often reversed) or before a run (often forward).
- **Preplay**: the order matches a path the animal has not yet run, seen in sleep or rest before the first run on a new track. If real, the brain pre-builds a menu of sequences and new places get mapped onto them.
- **Pre-choice or "planning" replay**: during a pause before a choice, the sequence depicts a future path to a goal.

The subfield is a set of recordings plus a decoding method. A decoder uses place fields to turn spikes in a short event into a path. A shuffle test says whether the path is better than chance. Most disputes here are disputes about that decoder: templates, thresholds, shuffles and time windows (a21, b04, b07).

Why this matters for an LLM agent scaffold. Replay is a biological case of three operations an agent can run: (1) roll out candidate futures before acting, (2) walk backwards from an outcome to assign credit, (3) review stored experience in idle time. The recordings tell us when each occurs, how long it runs and what it depends on. They do not test any language model. No LLM study tests preplay or replay recordings directly (K17, c24, b25). All LLM-side links in this document are analogy.

## 2. History and theories in depth

**2006, reverse replay.** Foster and Wilson (a01) reported that rats replay recent paths in reversed order right after a run, at the end of a linear track. They linked it to evaluating event sequences as in reinforcement learning. Quote (a01): "recent episodes of spatial experience are replayed in a temporally reversed order". Only the abstract was opened. No spike counts, compression factor or rat number was obtained (d01, K20). Cite no figure from it.

**2007, forward and reverse.** Diba and Buzsaki (a02): on a linear track, ripple sequences ran in reverse at the end of a run and forward before the run. 3 rats, 1,256 neurons, 267 firing at least 5 Hz in both directions. 95% of significant forward events came before the run. 85% of significant reverse events came after. This gives the basic split: forward before action, reverse after outcome. Templates came from the same session on a known track, so this is anticipation, not preplay.

**2009, extension and remote content.** Davidson, Kloosterman, Wilson (a03, b05, a26): in 4 rats, 19% of stopped-time events were longer than 250 ms. Durations ran 40 to 1018 ms. Long replays chain across ripples. Karlsson and Frank (a04): replay of an environment that is not the current one. 288 of 612 candidate events (47%) in first exposure to a second environment replayed the first. Chance is 5%. In the rest box 256 of 580 (44.1%) did. After long stillness it fell: 373 of 1046 (35.7%), and 106 of 310 (34.2%) after more than 60 s of immobility.

**2011, preplay.** Dragoi and Tonegawa (a05-a07, a21). Mice ran a novel arm joined to a familiar track. 14.2% of events with at least 4 novel-arm cells were significant preplay (chance 3.2%, P<1e-32, binomial). 16.2% of familiar-track events were significant replay. 81.1% of preplay events were at the junction end. 91% of preplay cases correlated with the novel template in one direction only. Median 6 place cells per event. Later place-field stability was lower for de novo fields (r=0.42 vs 0.62 on the contiguous arm, P<0.016). The authors read this as: sequences are preconfigured, then selected by experience. The mouse count differs between records (3 in a05, 4 in a07). Check the paper before quoting.

**2013, preplay of many tracks.** Dragoi and Tonegawa (a08, a22). 3 naive rats on 1.5 m tracks. 9.8% of events were significant preplay. Preplay covered on average 82.6% of track length (n=1,388, P<1e-200). 85.3% were unidirectional. Track-specific preplay was found for several tracks, with capacity "at least 15" tracks. 93.7% of cells were active on more than one track, yet preplay specificity was over 90%. Threshold: the 97.5th percentile of 500 surrogate orderings. The 2014 review (a09) adds no new data.

**2013, plan-like replay.** Pfeiffer and Foster (a10, a11, a24). Rats foraged in an open arena with a remembered home well and random wells. 4 rats, 40 tetrodes, up to 250 CA1 neurons at once. 144 to 373 trajectory events per session (25.3% to 43.9% of candidates). Mean duration 103.6 ms, path length 40.0 to 199.1 cm. 0 of 2,028 events had P>0.02 under shuffle. Replay before leaving a place depicted the future path to the goal. It matched the future path whether that ended at home or elsewhere (P 4.96e-22 and 1.12e-13). Home was less represented before non-home trips (P=9.6e-3). A random well that was the previous goal was not over-represented. Rats did not face the goal during these events.

**2015, the failed replication.** Silva, Feng, Foster (a12, a13, b01-b04). Same lab as Pfeiffer and Foster. 4 rats, 40 tetrodes, about 61 place cells per epoch, 3 novel linear tracks per day. 9,803 Sleep-1 candidate events. Median absolute rank correlation 0.174 real vs 0.172 shuffled (rank-sum p=0.08, KS p=0.122, Levene p=0.44). With best-template choice: 0.245 vs 0.258 (p=1). 435 of 442 units (98%) were well clustered by L-ratio. In Sleep 1 vs Run 1 (9,818 vs 4,438 events): absolute weighted correlation 0.17 vs 0.40, max jump 0.75 vs 0.43 (all p<1e-10). Poisson-rate and time-swap controls reproduced the false preplay pattern that a single threshold gives. The NMDA blocker D-CPPene before Runs 2 and 3 removed trajectory events (saline runs significant, drug runs not). Adding matched noise to saline spikes did not remove them, so poorer decoding did not explain it. Conclusion: trajectory events need previous experience of the track.

**2015, a conditional preplay.** Olafsdottir et al. (a14, a25, b06): 4 rats, 212 place cells, T-track with a see-through barrier. Cued arm 7.37% preplay (p<0.001), uncued arm 4.41% (p=0.33); cued vs uncued p<0.001. Cued preplay was equal in both directions (7.34% vs 7.40%). Preplay appeared only when the goal was cued and visible. This is the one independent lab, with a positive but weak and conditional result.

**2016, rigid and plastic cells.** Grosmark and Buzsaki (a15): 4 rats, 491 place cells, 8 novel sessions. 216 neurons contributed strongly to pre-run or post-run sequences. 73% of pre-run contributors also contributed post-run (a rigid core). Rigid vs plastic split at the median change in contribution.

**2016, reward and reverse replay.** Ambrose, Pfeiffer, Foster (a16): reverse replay rate (not forward) tracked reward change. It exceeded forward at the increased-reward site (z about 4) and at the decreased-reward site (z about 3). Exact digits were truncated in extraction.

**2017 and 2021, plan versus memory.** Olafsdottir, Carpenter, Barry (d03): 8 rats, 6 m Z-track, 24 sessions, 1,415 engaged and 3,010 disengaged events. Engaged (just after arriving at or before leaving a reward corner): 62.26% direction-congruent (p<0.0001), 80.70% local-arm (p<0.0001). Disengaged: 52.19% (p=0.39), 71.42% (p=0.31). Engaged vs disengaged p<0.0001. A classifier on engaged events before turns reached 60.3% (p=0.02). Gillespie et al. 2021 (b18; critique corrected the task): eight-arm win-stay lose-switch maze with dynamic goals, 4 rats. Pre-choice replay related to reliably rewarded and less recently visited places, not to the upcoming choice, and not trial by trial to behaviour. Zheng et al. 2021 (b11): sequences differ on correct vs error trials; running speed did not differ (F(1,42)=1.2, p=0.3).

**2021, decoder artefacts.** Denovellis et al. (b10): 10 rats. 89% of SWRs (23,071 of 25,844) were classifiable at the 0.80 posterior threshold. Of these 96% (22,170) were spatially coherent and 14% (3,295) had some incoherent segment. Overall 86% of all SWRs were coherent. The most common class was slower than real time. Earlier "fast replay" claims partly reflect decoder choice.

**2019 to 2025, extensions.** Farooq and Dragoi 2019 (d06; same lab): no trajectory sequences at P15-P16 (stationary location frames instead, about 16% of awake-rest frames). Preplay-like sequences from about P17-18. Replay larger than preplay at P23-P24 (P<0.009). Farooq, Zhou, Sibille, Dragoi 2025 (a20, b09): adult rats. Theta sequences survived spike jitter of 35 to 55 ms that abolished phase precession (p=2.1e-11 at one jitter scale), after 1 to 2 laps. Author lists differ between two records; treat as one source. A human cortex backbone-sequence study (d07) is a looser test; numbers not extracted. Breffle et al. 2024 (a18, a19, b07): a network of 15 random clusters, mean participation 1.25, makes preplay-like sequences with no design. Capacity about 8.6 tracks vs about 15 in Dragoi and Tonegawa 2013. A permuted network gave a median correlation shift centred on zero. So preplay-like sequences can arise from random structure.

**Theories.**
1. *Preconfigured selection* (Dragoi and Tonegawa; a09): sequences exist before experience, learning picks among them.
2. *Experience required* (Silva et al.): sequences form only after the place graph is sampled (a23).
3. *Random clustered network* (Breffle): preplay is a side-effect of recurrent structure.
4. *Prioritised replay* (Mattar and Daw 2018; d05): replay order is Need times Gain.
5. *Rollout planning* (Jensen et al. 2024; c01): replay is policy-sampled imagined action sequences.
6. *Counterfactual pre-solving* (Carvalho et al. 2025, Multitask Preplay; d08): spare compute solves tasks that were reachable but not chosen.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Forward events before run, reverse after | 95% of significant forward events before; 85% of reverse after; 3 rats, 267 cells | Diba and Buzsaki 2007 (a02) | established (K01) |
| Awake reverse replay exists | no counts obtained | Foster and Wilson 2006 (a01, d01) | established, no figures |
| Reverse (not forward) rate tracks reward change | z about 4 and about 3 | Ambrose 2016 (a16) | single-source (K02) |
| Replay chains beyond one ripple | 19% of events over 250 ms; 40-1018 ms; 4 rats | Davidson 2009 (a03) | single-source (K10) |
| Replay of a remote environment | 47% of 612 events in first exposure; 34.2% after more than 60 s still | Karlsson and Frank 2009 (a04) | single-source (K11) |
| Most SWR content is coherent, often slower than real time | 96% of 23,071 classified coherent; 14% any incoherent; 10 rats | Denovellis 2021 (b10) | established (K09) |
| Pre-choice sequences depict path to remembered goal | 2,028 events, 0 with P>0.02; away events P 4.96e-22, 1.12e-13; 4 rats | Pfeiffer and Foster 2013 (a10, a11) | contested (K03) |
| Pre-choice replay encodes rewarded, stale places, not choice | 8-arm win-stay lose-switch; 4 rats | Gillespie 2021 (b18) | contested (K04) |
| Mode switches with engagement | 62.26% vs 52.19% direction-congruent; 60.3% turn classifier (p=0.02); 8 rats | Olafsdottir 2017 (d03) | single-source (K21) |
| Humans: on-task replay with replanning, off-task with preferred paths | N=40; r=0.32 (p=0.04); flexibility vs RT r=-0.61 | Eldar 2020 (d04) | single-source (K22) |
| Preplay of novel arm (mice) | 14.2% vs chance 3.2%, P<1e-32; 16.2% replay; 81.1% at junction | Dragoi and Tonegawa 2011 (a05) | contested (K05) |
| Preplay of many tracks (rats) | 9.8% of events; 82.6% coverage, n=1,388; capacity at least 15 | Dragoi and Tonegawa 2013 (a08) | contested (K05) |
| No preplay on linear tracks | 9,803 events; 0.174 vs 0.172, p=0.08; 4 rats | Silva 2015 (a12, b01) | contested (K06) |
| Trajectory events need NMDA-dependent experience | drug runs 2 and 3 not significant; decode-noise control passed | Silva 2015 (b03) | single-source |
| Preplay is cue-gated | cued 7.37% (p<0.001), uncued 4.41% (p=0.33); 4 rats | Olafsdottir 2015 (a14) | single-source (K08) |
| Random networks can make preplay | capacity about 8.6 vs about 15 tracks | Breffle 2024 (a18, b07) | single-source (K07) |
| Pre-existing sequences in pups | none at P15-16; preplay-like from P17-18; same lab | Farooq and Dragoi 2019 (d06) | contested (K28) |
| Rollout network reproduces replay | home-trial success 0.622 true goal vs 0.403 disjoint, 0.433 full control; 37 sessions, 3 rats | Jensen 2024 (c02) | single-source (K12) |
| Human think time vs rollouts | r=0.186, falls to 0.070 after distance control; 94 people; steps fall up to at least 15 rollouts | Jensen 2024 (c03) | single-source (K12) |
| Pre-solving beats relabelling in grid worlds | 97.74% success vs 5.56% (HER), 7.65% (landmark SF), 0% (UVF); human reuse 62.39%, N=100 | Carvalho 2025 (d08) | single-source (K29) |
| Sleep-time precompute | about 5x less test-time compute; +13% GSM-Symbolic; +18% AIME; 2.5x cost drop at 10 queries | Lin 2025 (c07, d09) | single-source (K14) |
| Memory modules vs equal tokens | Gemini 3 Flash WebArena: vanilla 44.78 vs AWM 39.34, ASI 41.02, ReasoningBank 39.33; 3 runs | Hajimiri 2026 (d12) | single-source (K24) |
| Backward credit in training | ALFWorld 77.6 to 91.4 (+13.8); WebShop 66.1 to 73.8 (+7.7); Qwen2.5-7B | Tan 2026 HCAPO (d13) | single-source (K27) |
| LLMs poor at naming the culprit step | best step-level 20.68% (Claude-Sonnet-4, Who&When handcraft) | Zhang 2025 AgenTracer (d14) | single-source (K27) |
| LLM cognitive-map planning weak (2023 models) | GPT-4 1-step 0.99, n-step 0.47, policy revaluation 0.21; 0 of 30 shortest path | Momennejad 2023 (d17) | single-source (K19) |

## 4. Mechanisms and models

Each model is written so an engineer can build a toy version.

**4.1 The decoder (needed to judge any claim).**
1. Bin spikes in an event (an SWR or population burst, at least 50 ms, at least 4 to 6 cells).
2. Compute each cell's place field on a track.
3. Score the event against a template: rank correlation of firing order with field position, or a Bayesian posterior over position per time bin, then weighted correlation and max jump distance.
4. Shuffle (cell identity, time bins or Poisson rate) 500 to 10,000 times. Call the event significant at the 97.5th percentile or P<0.02.

Warning from Silva (b02, b04) and Denovellis (b10): one fixed threshold, one template pick and one shuffle type can create or remove the effect. Best-template selection applied to both real and shuffled data gave 0.245 vs 0.258, so the pick itself creates structure. Agent analogue: a score is only evidence if the same selection step is applied to a null.

**4.2 Prioritised replay (Mattar and Daw, d05).** Keep a model of the world. For each stored transition (state, action, next state) compute Need (expected future visits to that state from the current one) and Gain (improvement in policy value from doing this backup). Priority is Need times Gain. Do the top backup, update, repeat. Predictions: forward replay where Need is high (near the current state, before acting), reverse replay where Gain is high (after a surprising reward, backing value up). Diekmann and Cheng (b12) found cheaper rules near that performance: reverse mode clearly beat no replay and random replay, and was "close to, even if slightly below" Mattar and Daw. Antonov and Dayan (b13) extend it to bandits. In LLM RL training plain priority fails and needs an age decay (FreshPER, d18).

**4.3 Rollout planning (Jensen et al., c01-c04, c26).** A recurrent policy network (100 GRUs) can choose "imagine" instead of "move". An imagined action sequence (up to 8 actions, 120 ms per rollout vs 400 ms per physical action) is sampled from its own policy and fed back as pseudo-input. Trained by meta-RL (8x10^6 episodes, 5 agents). Result: replays avoid walls and over-represent the goal. Steps to goal fall with the number of forced rollouts, up to at least 15. The first imagined action matched the next real action more often in successful than unsuccessful rollouts (P<0.001, home trials). The time cost is explicit, so the policy learns when to stop.

**4.4 Random clustered preplay (Breffle, a18).** Build a recurrent excitatory network where each neuron belongs to about 1.25 of 15 clusters. Run it with noise. Population bursts of at least 50 ms and 5 cells already carry sequences. Map a new track onto the clusters by random place-field assignment. Capacity about 8.6 tracks. Use it as a null: any claim of designed structure must beat this.

**4.5 Multitask Preplay (d08).** While acting for goal A, use spare compute to simulate in the learned model the paths to goals B and C that were reachable. Store the solutions. At test, if the goal is B or C, reuse. Results: 97.74% success vs 5.56% to 7.65% for relabelling or landmark successor features, and 0% for universal value functions. Humans reused 62.39% (N=100). It is the closest AI analogue of preplay. It has not been run on language tasks.

**4.6 Sleep-time compute (Lin et al., c07, d09).** Before the user query arrives, a model reads the stored context and writes inferences, summaries and likely-question answers to a cache. At query time it answers from the cache. About 5x less test-time compute at equal accuracy. Predictability of the query given the context was measured as log-probability under Llama2-70B base. The gap widens with predictability across five bins. No zero-gain point was measured. Five parallel sleep-time generations generally beat 10 (critique).

**4.7 Cross-attempt consolidation (Hippo, d10).** After several attempts at one task, compare the attempts, then merge lessons by rule (add or delete, with applicability conditions). Free rewriting hurt (54.57). Separate summaries plus append-only 61.30. Compare plus append-only 70.10. Compare plus add-and-delete 72.90. No-memory baseline 64.20. Caution: no-memory success in at least one of 8 attempts is 73.6%, near the per-attempt 72.9%, so retries explain much of the gain.

**4.8 Backward credit pass (HCAPO, d13).** After an episode, ask the model, given the outcome, to score each earlier step's credit. Rescale step-level advantages. One extra forward pass per trajectory, about 8.3% of latency. A training-time method, not an inference-time scaffold.

## 5. What holds up

**Holds up.**
- Awake replay exists, runs in both directions, and forward events cluster before runs and reverse events after (a02; K01 has 3 independent sources).
- Replay is mostly coherent and mostly slower than real time with a proper state-space decoder (b10). Fast-replay claims depend on the decoder.
- Replay content depends on task state. Plan-like near action points (62.26%), at chance in long pauses (52.19%) (d03). Humans show a similar split (d04). This may reconcile Pfeiffer and Foster with Gillespie: different tasks, different engagement.
- Replay carries content that is not about the current place (Karlsson and Frank), and it gets less likely after long stillness.

**Contested.**
- Preplay. Positive: Dragoi lab (mice 2011, rats 2013, pups 2019, adult theta 2025). Negative: Silva 2015 (9,803 events). Partial: Olafsdottir 2015 (cued only, 7.37%). Neither side is independent of its own lab. The dispute is thresholds, templates, silence windows (50 vs 100 ms) and cell counts (4 vs 6) (critique, a21). No independent hippocampal preplay replication with 2023-2026 data was found (d07 is human cortex and a looser test).
- Plan vs memory for pre-choice replay (K03 vs K04). Not settled.
- Capacity: 15 tracks vs 8.6 (model).

**Moderators.** Cue or goal visibility (Olafsdottir 2015). Engagement (Olafsdottir 2017). Time spent still (Karlsson and Frank). Reward change (Ambrose 2016). Age (Farooq and Dragoi 2019). Experience (Silva 2015, NMDA block).

**Interventions that worked.** NMDA blockade removed trajectory events (Silva). Prioritisation beat random replay in grid worlds (d05). Age decay rescued prioritised replay in LLM RL (d18). Rule-bound merging of multi-attempt lessons beat free rewriting (d10). Sleep-time precompute saved about 5x test-time compute (c07).

**Did not work.** Free rewriting of memory (54.57, d10). Plain accumulation of lessons falls below no memory over time (d10). Plain prioritised replay in LLM RL degraded results (d18). Memory modules lost to equal-token extra steps (d12). Foresight tools were invoked under 1% of the time by some agents, about 15% of rollouts were misused, and performance fell up to 5% (d15).

**Weak spots.** Foster and Wilson 2006 and Foster 2017 have no numbers (d01, d02). BrainMem steps are 2 points on about 50 tasks (c17). Several 2026 papers (Hippo, 2606.15017, FreshPER) were read once. Network failures limited cross-checks to 8 numbers from full text (critique).

## 6. Language models

No LLM study records or tests replay or preplay (K17). What exists falls into five groups.

1. **Formal link.** Whittington, Warren, Behrens (b22, c09): transformers relate formally to hippocampal models. No replay measurement.
2. **Planning on cognitive maps (CogEval, d17).** 8 models, 2023. GPT-4: 1-step 0.99, 2-step 0.82, 3-step 0.55, n-step 0.47, policy revaluation 0.21, reward revaluation 0.67, transition revaluation 0.60. GPT-3.5: 0.76, 0.73, 0.37, 0.31, 0.18, 0.57, 0.59. Shortest path one cluster away: 0 of 30 at temperature 0. Old models. Not re-run.
3. **Forward foresight (preplay analogue).** Qian 2026 (d15): agents rarely call a world-model simulator (some under 1%), misuse about 15% of rollouts, and do up to 5% worse when it is available or forced. WebATLAS (d16): 47.9 base to 63.0 full (memory plus look-ahead); look-ahead is not isolated. Dyna-Think (c11): 2x fewer tokens than R1; no success rates read. Jensen (c03): a small network gains steadily to about 15 rollouts, but it is a maze net, not an LLM.
4. **Backward credit (reverse-replay analogue).** HCAPO (d13): +13.8 ALFWorld, +7.7 WebShop, training time, Qwen2.5-7B, 3 seeds. AgenTracer (d14), Who&When handcraft subset, step-level accuracy: Claude-Sonnet-4 20.68, Gemini-2.5-Pro 17.24 (18.97 with ground truth), GPT-4.1 13.29 (6.90), DeepSeek-R1 9.72 (6.90). Acting on flagged errors gave 4.8 to 14.2% gains on two systems. Blame is hard even where the backward pass helps.
5. **Memory review and sleep.** Sleep-time compute (c07). Hippo (d10): WebArena 64.20 to 72.90, SWE-bench Verified 81.50 to 88.50; without the consolidated layer 66.50 and 83.80; without episodic reflection 68.70 and 85.63. CER (d11): WebArena 24.3 (ReAct) to 33.4 offline, 33.2 online, 36.7 hybrid (+51.0% relative), at 7.9K to 20.6K extra input tokens per task. BrainMem (c16, c17): EB-ALFRED GPT-4o 64.0 to 82.0 along the ablation ladder (working 68.0, episodic 70.0, semantic 76.0, feedback 82.0). HEMA (b23): recall after 150 turns 87%, +46 points over raw. FSFM (c19): +8.49% access efficiency. Reflexion (c14): 91% vs 80% on HumanEval. Voyager (c15): 3.3x unique items. AWM (c12): +24.6% relative on Mind2Web, +51.1% on WebArena.

**The control that matters.** Hajimiri 2026 (d12), matched tokens, 3 runs: vanilla with extra steps beats memory modules. Gemini 3 Flash WebArena: vanilla 44.78 vs AWM 39.34, ASI 41.02, ReasoningBank 39.33. GPT-5.4-mini: 32.67 vs 27.02, 29.00, 24.58. Qwen 3.6-27B: 42.14 vs 38.01, 40.15, 37.00. WorkArena-L1 Qwen: 55.56 vs 53.53, 48.49, 55.56. A critical review (snippet only) says the control was also strengthened. FreshPER (d18): +46% NQ Search, +367% Sokoban, +133% VLM FrozenLake over on-policy; plain PER degrades. Arnal 2026 (d19): up to 40% compute saved with replay in RL training.

**What changed behaviour, by how much.** Equal-token controls erase much of the memory gain. Rule-bound consolidation beats free rewriting by about 18 points on one benchmark (72.90 vs 54.57). Age decay flips prioritised replay from harmful to helpful. Forced simulation can hurt (up to 5%).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Parts: G guardrail, S state, O operator, M memory.

### Add now (established)

1. **Replay-style memory must be judged against an equal-token retry arm.** [E] M, G7. Trajectory reuse helps in many papers (K16: AWM, Reflexion, Voyager, ExpeL; c12, c13, c14, c15), but matched-token tests show extra steps can match it (d12). Every memory or review element runs against a retry arm at equal tokens.
2. **Two directions, two jobs.** [E] for the biology (a01, a02, a16), [S] for the transfer. Keep S3/S4 forward (candidates before commit) and S5 backward (from the failing output to the earlier step) as separate operators. The backward step stays inside G2 (cite the real output, code locates it), because LLM blame is poor (d14, best 20.68%).
3. **Require a null for any "pre-built structure" or selection-score claim.** [E] G3, G5. The Silva vs Dragoi dispute shows one template, one threshold and best-template choice can create or remove an effect (b02, b04, b07, b10). Any score used to pick a candidate is compared with the same score on a mutated or shuffled input, and more than one scoring rule is used (K09).
4. **Decoded or written traces are inference, not record.** [E] G10 (b10, d14). Do not accept reasoning text or a decoder output as proof.
5. **Keep rollouts conditional and checked.** [C] but safe as a rule consistent with G1: simulate on a trigger, and verify the output is used (d15: under 1% invocation, about 15% misuse, up to 5% loss).

### Test first (not yet established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Forward rollout of 2 to 4 candidate plans before acting; saturation near 15 rollouts | O (plan), S3 | [C] | a10, c03, d15, d16 |
| Backward pass from failed outcome to earlier step with replay-with-fix check | S5, G2 | [S] | a02, a16, d13, d14 |
| Plan pass at decision points, review pass in idle time (mode switch) | S, M | [S] | d03, d04, a10, b18 |
| Idle-time precompute on notes before the question | M | [S] | c07, d09, d08 |
| Counterfactual pre-solving of nearby variants | O | [S] | d08 |
| Value-and-recency ordered review vs random review | O (priority), M | [S] | d05, d18, b12 |
| Rule-bound cross-attempt merge vs append-only vs free rewrite | S5, M | [S] | d10 |
| Goal stated first raises branch quality only for goal-relevant branches | G | [S] | a14, a25 |
| Recall of an earlier similar problem during a new one | M | [S] | a04 |
| Hindsight relabelling of failed attempts to the sub-goal reached | O | [S] | c10 |
| Chained rollouts of fixed total tokens vs several short ones | O | [S] | a03, a26 |
| Entrenchment check: idle review that re-reads preferred answers raises confident error | G | [S] | d04 |

## 8. Concrete tests on our bench

Common rules. Both arms get equal total tokens including setup or idle-time compute (G7). At least 100 items, at least 5 seeds, report spread. An equal-token retry arm (plain model, several attempts, vote by code) is always included (d12).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 forward rollout | ARC-like and multi-step puzzles with a check | A: act then revise (S5). B: 3 candidate rollouts before commit, then act. C: retry arm | pass rate at equal tokens | B above A on items with mid-range plain pass rate; small or negative on easy items. Add if at least +3 points over C |
| T2 backward credit | tasks where a failed attempt exists | A: forward re-read of the failing attempt. B: backward walk from failing output to blamed step with replay-with-fix check. C: retry | correct fix rate in 2 rounds; error localisation accuracy | B above A on multi-step chains; blame without a check near 20% (d14) |
| T3 mode switch | long tasks with decision points and an idle budget | A: one mixed pass. B: plan pass at decision points, review pass in idle | pass rate; confident-error rate | B at least +2 points; watch confident error from idle review |
| T4 sleep-time precompute | question sets sharing a context, with varied predictability | A: all budget at query time. B: part of budget on context precompute | accuracy at equal total tokens, by predictability bin | gain grows with predictability; find the bin where it hits zero |
| T5 counterfactual pre-solving | families of near variants of one problem | A: solve the asked variant only. B: spend spare tokens on 2 neighbouring variants first, reuse | accuracy on asked variant; reuse rate | gain only when the later query is a neighbour |
| T6 prioritised review | memory of past solved items | A: random review. B: order by value and recency (age decay) | next-item accuracy | B above A; priority without decay should be worse |
| T7 cross-attempt merge | repeated tasks | A: append-only. B: compare then add-and-delete. C: free rewrite. D: retry | accuracy over successive rounds | B best, C worst, A decays over rounds |
| T8 goal-first framing | branching tasks with goal-relevant and irrelevant branches | A: goal after. B: goal first | rollout quality by branch type | gain only for goal-relevant branches |
| T9 shuffled-null scoring | candidate selection by a score | A: score alone. B: score compared with score on mutated input | selection precision | B reduces false picks |

## 9. What does not transfer, and why

- **Spike timing and compression.** A 100 ms ripple at high compression has no counterpart. Tokens are slow and cost the same per step.
- **Preplay itself.** Whether the brain pre-builds sequences is unsettled (K05, K06, K07). An LLM already has pretrained structure. The useful lesson is only the null-comparison discipline.
- **Place-cell templates.** Rats have a 2D space. Language tasks have no fixed decoder.
- **Capacity numbers (15 vs 8.6 tracks).** Network facts, not agent facts.
- **Reward signals.** Reverse replay tracks reward change. Our agent has a check pass or fail, which is coarser.
- **Small samples.** 3 to 10 rats per study, N=40 humans (d04), 94 humans in Jensen. Too weak to fix constants such as "15 rollouts".
- **Training-time evidence.** HCAPO, FreshPER and replay buffers change weights. Our agent does not train, so only inference-time analogues count.
- **Sleep and consolidation.** No weights change at night. Sleep-time compute is a cache, not consolidation.

## 10. Open questions

1. Does backward credit assignment after a failed LLM attempt beat forward re-reading at equal tokens? No inference-time test exists.
2. Does forward rollout before acting beat act-then-revise at equal tokens, and where does it saturate?
3. Where is the zero-gain point of sleep-time precompute when the query is unpredictable? Predictability is confounded with difficulty (d09).
4. Foster and Wilson 2006 and Foster 2017 numbers. Need library access (d01, d02).
5. Which task features flip replay between plan and memory? Engagement is one (d03). Is it the only one?
6. Independent hippocampal preplay replication with 2023-2026 data. Shin and Jadhav W-track data not opened.
7. Prioritised vs random replay in an LLM memory-review loop.
8. Replay ablated alone in agent memory stacks. Hippo's retry baseline (73.6% at least once in 8) suggests retries explain much.
9. CogEval with current models and an explicit edge list.
10. Does the Hajimiri token-matched result hold when the memory baselines are tuned?
11. Resolve the 2025 Dragoi paper's author list and title before citing.

## 11. Sources

[V] opened in this run. [M] snippet only.

- [V] Foster and Wilson 2006 (abstract only). https://pubmed.ncbi.nlm.nih.gov/16474382/ (a01, a27); https://www.nature.com/articles/nature04587 (d01)
- [V] Diba and Buzsaki 2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2039924/ (a02)
- [V] Davidson, Kloosterman, Wilson 2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC4364032/ (a03, a26, b05)
- [V] Karlsson and Frank 2009. https://pmc.ncbi.nlm.nih.gov/articles/PMC2750914/ (a04)
- [V] Dragoi and Tonegawa 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3104398/ (a05-a07, a21, b14)
- [V] Dragoi and Tonegawa 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3670374/ (a08, a22, b15)
- [V] Dragoi and Tonegawa 2014 review. https://pmc.ncbi.nlm.nih.gov/articles/PMC3866444/ (a09)
- [V] Pfeiffer and Foster 2013. https://pmc.ncbi.nlm.nih.gov/articles/PMC3990408/ (a10, a11, a24, b17)
- [V] Silva, Feng, Foster 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC6095134/ (a12, a13, a23, b01-b04)
- [V] Olafsdottir et al. 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4479790/ (a14, a25, b06)
- [V] Grosmark and Buzsaki 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4919122/ (a15)
- [V] Ambrose, Pfeiffer, Foster 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC6013068/ (a16)
- [V] Foster 2017 abstract. https://pubmed.ncbi.nlm.nih.gov/28772098/ (a17); [M] Annual Reviews page (d02)
- [V] Breffle et al. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11488848/ (a18, a19, b07, b08)
- [V] Farooq, Zhou, Sibille, Dragoi 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12391462/ (a20, b09)
- [V] Denovellis et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8476125/ (b10)
- [V] Zheng et al. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8185092/ (b11)
- [V] Diekmann and Cheng 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC10076035 (b12)
- [V] Antonov and Dayan 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC11829958 (b13)
- [M] Gillespie et al. 2021. https://doi.org/10.1016/j.neuron.2021.07.029 (b18); re-opened in critique as PMC8497431
- [V] Mattar and Daw 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6203620/ (d05); [M] https://www.biorxiv.org/content/10.1101/225664.full.pdf (c21, b19)
- [V] Olafsdottir, Carpenter, Barry 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC5697915/ (d03)
- [V] Eldar et al. 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7299337/ (d04)
- [V] Farooq and Dragoi 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6794005/ (d06); [M] https://doi.org/10.1126/science.aav0502 (b21)
- [V] Human cortex backbone sequence study. https://pmc.ncbi.nlm.nih.gov/articles/PMC10406814/ (d07)
- [M] Sagiv et al. 2025 (c22); Bakermans et al. 2025 (c23); Grosmark and Buzsaki DOI page (b20)
- [V] Jensen, Hennequin, Mattar 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11239510/ (c01-c04, c26)
- [V] Brain-Like Replay Naturally Emerges in RL Agents 2024. https://ar5iv.labs.arxiv.org/html/2402.01467 (c05, c06)
- [V] Carvalho et al. 2025, Multitask Preplay. https://arxiv.org/pdf/2507.05561 (d08)
- [V] Lin et al. 2025, Sleep-time Compute. https://arxiv.org/abs/2504.13171 ; https://arxiv.org/pdf/2504.13171 (c07, d09)
- [V] Momennejad et al. 2023, CogEval. https://arxiv.org/abs/2309.15129 ; https://arxiv.org/pdf/2309.15129 (c08, d17)
- [V] Whittington, Warren, Behrens 2022. https://arxiv.org/abs/2112.04035 (b22, c09)
- [V] Andrychowicz et al. 2017, HER. https://arxiv.org/abs/1707.01495 (c10)
- [V] Yu et al. 2025, Dyna-Think. https://arxiv.org/abs/2506.00320 (c11)
- [V] Wang et al. 2024, Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c12)
- [V] Zhao et al. 2024, ExpeL. https://arxiv.org/abs/2308.10144 (c13)
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366 (c14)
- [V] Wang et al. 2023, Voyager. https://arxiv.org/abs/2305.16291 (c15)
- [V] Ma et al. 2026, BrainMem. https://arxiv.org/html/2604.16331 (c16, c17)
- [V] Kim 2025, brain-inspired replay in continual learning (abstract only). https://arxiv.org/abs/2509.00047 (c18)
- [V] Gu et al. 2026, FSFM. https://arxiv.org/abs/2604.20300 (c19)
- [V] Bhardwaj 2026, SuperLocalMemory V3.3. https://arxiv.org/abs/2604.04514 (c20)
- [V] HEMA 2025. https://arxiv.org/pdf/2504.16754 (b23)
- [V] Auton Agentic AI Framework 2026 (no replay numbers). https://arxiv.org/pdf/2602.23720 (b24)
- [V] Song et al. 2026, Hippo. https://arxiv.org/pdf/2610.24453 (d10)
- [V] Liu et al. 2025, Contextual Experience Replay. https://aclanthology.org/2025.acl-long.694.pdf (d11)
- [V] Hajimiri et al. 2026. https://arxiv.org/pdf/2606.15017 (d12)
- [V] Tan et al. 2026, HCAPO. https://arxiv.org/pdf/2603.08754 (d13)
- [V] Zhang et al. 2025, AgenTracer. https://arxiv.org/pdf/2509.03312 (d14)
- [V] Qian et al. 2026, world model as tool. https://arxiv.org/pdf/2601.03905 (d15)
- [V] WebATLAS 2025. https://arxiv.org/pdf/2510.22732 (d16)
- [V] Ma et al. 2026, FreshPER. https://arxiv.org/pdf/2604.16918 (d18)
- [V] Arnal et al. 2026. https://arxiv.org/pdf/2604.08706 (d19)
- [V] Kim and Choi 2026 (abstract only). https://arxiv.org/pdf/2611.01952 (d20)
- [M] Search sweeps via arXiv API and Semantic Scholar (b25, c24, c25): no direct LLM replay test found.
