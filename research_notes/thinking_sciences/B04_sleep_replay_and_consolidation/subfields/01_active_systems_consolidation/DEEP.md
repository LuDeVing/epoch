# Active systems consolidation: deep document

*Subfield B04.01. Source files in this folder: evidence_a-d.jsonl (ids a01-a25, b01-b25, c01-c25, d01-d21), claims.jsonl (K01-K35), critique.md. Evidence ids are cited in square brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Active systems consolidation (ASC) is a theory of what sleep does for memory. The claim: while you learn, the hippocampus stores a fast, detailed trace of the episode. During slow-wave sleep (SWS, deep NREM sleep) the hippocampus replays that trace again and again. Replay is paced by three nested rhythms: cortical slow oscillations, thalamo-cortical spindles, and hippocampal sharp-wave ripples. The replay trains the slow-learning neocortex. Over repeated nights the cortex holds a more stable, more integrated, more gist-like version of the memory, and the hippocampus is needed less. [a01, b01]

Key statement: Klinzing, Niethard and Born 2019 update Diekelmann and Born 2010. They say repeated replay "leads to a gradual transformation and integration" of the trace in cortex, embedded in global synaptic downscaling. [a01]

Three features of the modern version [a01]:
1. Replay of episodic aspects drives consolidation, for hippocampus-dependent and also independent memory.
2. SWS and REM oscillations regulate information flow and local plasticity.
3. Memories become abstracted and gist-like.

Why it matters for our agent: it is the closest biological template for an offline job that turns raw episodes into compact rules. Our agent has a fast store (episode log) and could have a slow store (rules, lessons). The theory says three things an engineer can use: replay many episodes while idle; transform them, do not just copy them; and keep the replay separate from the live task.

Two cautions up front. First, the human evidence is weaker than the theory's fame suggests (section 5). Second, no LLM study tests the human effects themselves. Every LLM paper borrows the metaphor and measures task benchmarks [c24, c25]. So LLM results below say "an offline consolidation step helped on this benchmark". They do not say "the biology is right".

## 2. History and theories in depth

**1994 to 2009: replay in rodents.**
- Wilson and McNaughton 1994: in 3 rats, hippocampal place cells that fired together during a spatial task fired together more in later SWS than in sleep before the task. Cells that were inactive or had non-overlapping fields showed no such effect. The effect decayed over the post-task sleep session. [a04]
- Ji and Wilson 2007: awake firing sequences were replayed in both visual cortex and hippocampus during SWS, and the two areas were coordinated for the same experience. Correlational. [a05]
- Girardeau et al. 2009: eliminating sharp-wave ripples after training impaired a hippocampus-dependent spatial task in rats. This is the key causal rodent test. [a06]
- All rodent items here were read at abstract level only.

**1995: complementary learning systems (CLS).** McClelland, McNaughton and O'Reilly: a fast hippocampal learner and a slow neocortical learner. Reinstating hippocampal memories interleaves new items with old ones, so the slow network learns structure without catastrophic interference. This is the computational parent of ASC and of most AI memory designs. [a08]
- 2016: Kumaran, Hassabis and McClelland carried CLS to AI. Not opened; treat as unverified. [a25]
- 2020: McClelland, McNaughton and Lampinen: in deep linear networks, the part of a new item that fits known dimensions can be learned fast without interleaving. Only the part needing a new dimension needs slow interleaved learning. This predicts fast integration of schema-consistent facts. [a09]

**2004: sleep and insight.** Wagner et al. "Sleep inspires insight": after training on a task with a hidden rule, more than twice as many people found the rule after 8 h of night sleep as after wake. [a07] Exact numbers (from Verleger 2013): 13 of 22 (59 percent) after sleep versus 5 of 22 (22.7 percent) or 5 of 20 (25 percent) in each of four control groups; chi2 = 10.2, df 4, p = .03. Base rate without sleep is about 20 to 25 percent. [d01]

**2006 and 2007: causal manipulation in humans.**
- Marshall et al. 2006: 0.75 Hz oscillating current in early NREM sleep raised slow oscillations and retention of declarative memory. 5 Hz lowered slow oscillations and left memory unchanged. Abstract only; no numbers read. [a02, b12]
- Rasch et al. 2007: an odor present at learning and re-presented in SWS improved declarative retention. It did not work in REM, in wake, or if the odor was absent at learning. fMRI showed hippocampal activation to the odor in SWS. This founded targeted memory reactivation (TMR). [a03, b13] Per-condition samples were small, about 7 to 17 as coded by Hu 2020. [b06, b13]

**2010 to 2013: the formal model.** Diekelmann and Born 2010 (not in our files) and Rasch and Born 2013 state the model: slow oscillations drive hippocampal ripples nested in spindles in the up phase, and this redistributes memory to cortex. REM is assumed to stabilise synaptically afterwards. The review contrasts this with passive accounts (sleep only cuts interference) and flags that what decides which memories get consolidated is poorly understood. It also concedes that the sequential hypothesis (SWS then REM) has rarely been tested directly, and that some procedural gains are recovery effects visible within hours of wake. [b01, b03, b25]
- 2013: Ngo et al. closed-loop audio: clicks in phase with slow-oscillation up states boosted slow oscillations, coupled spindles and memory. Out-of-phase clicks did not. [a10]

**Rival account: synaptic homeostasis.** Tononi and Cirelli 2014: wake strengthens synapses broadly; sleep renormalises net strength, and down-selection explains the memory benefit, not replay-driven strengthening. [a17] Norimoto et al. 2018 (mice): ripples triggered long-lasting synaptic depression; silencing ripples in slow-wave states prevented the downregulation and impaired learning of new memories. This fits both stories: ripples can both replay and downscale. [a18] Current theory merges the two (replay embedded in downscaling). [a01]

**Schema building by overlapping replay.** Lewis and Durrant 2011 (iOtA model): overlapping replay of related memories strengthens shared elements; repeated replay in new combinations builds schemas, gist, insight and also false memory. Theory only. [b17]

**2019 to 2026: the robustness turn.** Henin 2019 failed to replicate closed-loop memory gains. Cordi and Rasch 2021 (a proponent) reviewed replication failures and concluded effects are smaller, more task-dependent, less SWS-related and less lasting than assumed. Hu 2020 put TMR at g = 0.29 with a publication-bias-adjusted g = 0.18. A 2022 meta-analysis with g = 0.68 for acoustic stimulation was retracted in 2026. See section 5. [a11, b14, b04, b05, d10]

**2018 to 2026: the AI turn.** Sleep-like replay in small neural nets (Tadros 2022), then sleep-time compute (Lin 2025), then a wave of 2026 LLM memory papers (Auto-Dreamer, RecMem, All-Mem, Hippocam, REALM, SleepGate, others). See section 6.

## 3. Core findings with exact numbers

Status uses [E] established, [S] single-source, [C] contested. "Human" rows are not tests of an LLM.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| TMR in sleep gives a small memory gain | 91 experiments, 212 effect sizes, N = 2,004; g = 0.29 [0.21, 0.38]; Q(211) = 588, I2 = 71% | Hu 2020 [b04] | [E] small, heterogeneous |
| TMR works in NREM, not REM or wake | NREM2 g = 0.32 [0.04, 0.60]; SWS g = 0.27 [0.20, 0.35]; REM and wake ns | Hu 2020 [b04] | [E] |
| TMR is partly publication-biased | Egger Z = 8.489, p < .001; trim-and-fill g = 0.18 [0.06, 0.30]; unpublished k = 26 g = 0.18 [-0.06, 0.42] ns; published k = 186 g = 0.31 | Hu 2020 [b05] | [E] |
| Founding TMR skill result is near zero; declarative is larger | Rasch 2007 skill g = -0.08 [-0.52, 0.37]; spatial declarative g = 0.69 [0.19, 1.18]; associative in NREM g = 0.17 [0.03, 0.30] | Hu 2020 [b06] | [E] |
| 2025 nap TMR null | 80 homonyms, 40 primed, ~2 h nap; no TMR benefit though cue-evoked spindle/beta power rose | Ball 2025 [b15] | [S] abstract only |
| Slow-oscillation boosting by tES raised memory (original) | 0.75 Hz raised SO and declarative retention; 5 Hz did not; no numbers read | Marshall 2006 [a02, b12] | [C] |
| Closed-loop audio raised memory (original) | up-state clicks gave gains; out-of-phase no; no numbers read | Ngo 2013 [a10] | [C] |
| Closed-loop audio failed to replicate | Exp 1 n = 12 nap crossover, Exp 2 n = 19 double blind; Bayes factors for equality 0.302 and 0.299 (Exp 1), 0.249 (Exp 2) | Henin 2019 [a11] | [C] |
| Acoustic stimulation meta-analysis is borderline | 10 studies, 11 experiments, 177 people; g = 0.25, p = 0.07; phase-locked g = 0.36 (p = 0.047) | Wunderlin 2021 [d09] | [E] weak |
| A large acoustic meta-analysis was retracted | claimed g = 0.68 (under 35), 0.87 declarative; SE used for SD, wrong sample sizes; retracted 2026 | Stanyer 2022 [d10] | [E] do not cite |
| More acoustic nulls | insomnia N = 27 crossover, no effect; home study N = 34, one night, no effect | 2025/26 [d13] | [E] |
| tDCS plus CLAS, no overall gain | N = 20; null overall; lower retention only in high-Raven subgroup; compared with CLAS alone, not sham | Hausdorf 2025 [d11] | [S] |
| Mouse single-pulse CLAS did not beat sham | ripple suppression about 1 s after each pulse; up-state better than one other phase | Aksamaz 2024 [d12] | [S] |
| UP-state cueing cuts forgetting vs DOWN | forgetting 5% (UP) vs 15% (DOWN), t(23) = 2.28, p = .032; uncued 12%, not different from either; N = 24 | Ngo and Staresina 2022 [b10] | [S] |
| SO-spindle coupling relates to retention, weakly | 23 studies, 297 effect sizes; pooled r = 0.07 [0.01, 0.13], BF10 = 58.35; age slope -0.005 [-0.015, 0.008]; fast vs slow spindle r = -0.02, BF10 = 1.91 | Ng 2025 [b07, b08, a15] | [S] one meta-analysis, correlational |
| Spindles couple hippocampus and neocortex at ripples | 14 patients; 17,174 neocortical spindles, 14,748 hippocampal spindles, 3,748 ripples; stronger for long ripples | Ngo, Fell, Staresina 2020 [a16] | [S] |
| Rodent replay and ripple necessity | 3 rats co-firing; visual cortex-hippocampus coordination; ripple elimination impairs spatial task | Wilson 1994, Ji 2007, Girardeau 2009 [a04-a06] | [E] abstract level |
| Sleep has a capacity limit | n = 101 total; sleep benefit at 160 pairs (p < .01), none at 320; retention at 320 lower than 160 | Feld 2016 [a12] | [S] authors say near the detection limit |
| Hidden-rule insight after sleep | 13/22 (59%) vs 5/22 (22.7%) or 5/20 (25%) in four controls; chi2 = 10.2, p = .03 | Wagner 2004 via Verleger 2013 [d01] | [C] |
| Insight needs prior implicit knowledge | benefit specific to those who had acquired the rule implicitly; linked to SWS and 10-12 Hz; post hoc, exploratory EEG | Verleger 2013 [d02] | [S] own lab |
| Stage conflict: N1 | N = 103; rule found by 83% with at least 15 s N1 vs 30% awake; deeper sleep removed the effect | Lacaux 2021 [d04] | [C] |
| Stage conflict: N2 | preregistered, 90 enrolled, 68 analysed (28 N2, 22 N1, 18 awake); insight 85.7% (N2) vs 55.5% (wake); N1 63.6% ns | Lowe 2025 [d05] | [C] |
| No sleep help for classical insight problems | N = 77; magic tricks sleep effect F(1,64) = 0.047, p = .829 | Schonauer 2018 [d03] | [E] null |
| Sleep helps puzzle solving but cueing adds nothing | 62% sleep vs 24% wake (Exp 1); TMR 56% SWS cues, 58% REM cues, 57% wake cues (Exp 2) | Beijamini 2021 [d06] | [S] |
| Pink noise did not help insight | N = 72 analysed of 87; closer to wake; time in first N1 predicted insight | Vickrey 2023 [d07] | [S] |
| Gist and false memory: no overall sleep effect | DRM meta-analysis, null overall; larger for recall than recognition | Newbury 2019 [a14] | [E] |
| Own-lab gist replication failed | N = 16 within-subject; gist persisted to 1 year; sleep in first 12 h made no difference | Lutz 2026 [a13] | [S] small |
| Sleep favours well-connected nodes | 25 recruited, 19 analysed; sleep retention t(18) = 2.13, p = .048; centrality F(1,18) = 4.71, p = .044; slope F = 8.26, p = .015 | Feld 2022 [a21] | [S] weak |
| Item detail falls, category info kept, tied to REM | 35 analysed; REM theta and beta linked to transformation; SWS SO power (1-1.25 Hz) opposite | Liu 2025 [a22] | [S] challenges SWS-only |
| Sleep deprivation after learning hurts modestly | after learning g = 0.277 [0.177, 0.377]; before learning g = 0.621 [0.473, 0.769]; publication bias in both | 2022 meta-analysis [a23] | [S] |
| Sleep-like replay in small nets restores old tasks | CIFAR-10 sequential 19.01 vs SRC 44.55; incremental MNIST 19.49 vs 48.47; CUB-200 first/second task 63.2 and 45.4 (sequential 5.32, 95.41) | Tadros 2022 [a19, a20, c17] | [E] for nets; not LLM |

## 4. Mechanisms and models

This section is written so an engineer can map each part to a scaffold. The biology is the source of the pieces. The LLM evidence for each piece is in section 6.

### 4.1 The two-store loop (CLS)
- Fast store: write each episode as it happens, with little processing. High detail, high interference.
- Slow store: learns structure from many episodes. Must not be overwritten by one episode.
- Replay: the fast store re-presents episodes to the slow store, interleaved with old material. Interleaving is what prevents catastrophic interference. [a08]
- Schema shortcut (McClelland 2020): a new item that fits an existing rule can go straight into the slow store. Only the part that needs a new dimension needs slow interleaved learning. [a09]
- Engineer's version: episode log (fast) plus rule/lesson list (slow). An offline job reads a batch of episodes together with the existing rules, and edits the rules. A new episode that fits a rule just adds support to it. An episode that breaks a rule triggers a careful, interleaved review of that rule against old episodes.

### 4.2 The replay timing stack
- Slow oscillation (about 0.75 to 1 Hz) alternates up and down states. Up state is the window when the cortex is receptive.
- Spindles ride the up state. Ripples (hippocampal, very fast) nest inside spindles. The nesting is the hand-off of a replay event from hippocampus to cortex. [b01, a16]
- Evidence for the timing: one human study found up-state cueing cut forgetting more than down-state cueing (5 vs 15 percent, N = 24) [b10]. Across individuals, tighter SO-spindle coupling relates to retention, but only r = 0.07 [b07]. Causal boosting of the rhythm has mixed or failed replication [a11, d09, d13].
- Engineer's version: there is none that transfers. An LLM has no oscillation. The transferable idea is only "replay runs in a separate offline phase with its own budget", not "replay at phase X". See section 9.

### 4.3 Targeted memory reactivation (TMR)
- A cue present at learning is re-presented during sleep. The cue biases which memories get replayed. [a03]
- Conditions that mattered: cue must have been paired at learning; must be delivered in NREM (SWS and N2), not REM or wake. [b04]
- Engineer's version: at an idle step, re-insert a short cue plus key facts of chosen episodes into context, and let the model process them without a task. Compare with the same insertion mid-task. Prediction from Hu 2020: small gain, phase specific.

### 4.4 Selection: what gets replayed
- Review: what decides selection is poorly understood. [b01]
- Hubs: sleep favoured well-connected nodes in a learned graph, N = 19, p near .05. [a21]
- Capacity: gain at 160 pairs, none at 320. Authors suggest heavy load makes sleep favour forgetting. [a12]
- Engineer's version: a priority rule for the replay queue (connectivity, recurrence, surprise, reward) and a cap on batch size per pass.

### 4.5 Abstraction
- Overlapping replay of related episodes strengthens what they share. Repeated replay in new combinations yields gist and insight, and also false memory. [b17]
- Item detail falls while category information is kept; REM-related in one study. [a22]
- Engineer's version: the consolidator compares episodes and writes the shared part as a rule; the rule links back to its source episodes. Expect loss of dates, places and numbers unless the prompt protects them (section 6).

### 4.6 Downscaling (the rival mechanism)
- Net synaptic strength is reduced; weak traces drop out. [a17, a18]
- Engineer's version: pruning and dedup. Merge near-duplicates, drop entries never recalled, cap total store size. Safe pruning is dedup. Aggressive summarising of clusters is not (section 6).

### 4.7 Offline computation, not only storage
- Sleep-time compute: precompute inferences over the known context while idle. Later queries need fewer tokens. [b18]
- Offline recurrent passes over evicted context, on hybrid models, help most on deep reasoning items. [c01, c02]
- Engineer's version: an idle step that asks "what questions will come, what do I already know that answers them", and stores the answers.

### 4.8 Reconsolidation
- Retrieval reopens a memory so it can be updated. In agents this means: when a memory is used, check it against the new context and edit it. [c13, c11]

## 5. What holds up

### 5.1 Holds up reasonably
- TMR in NREM gives a small gain (g about 0.29, adjusted 0.18). Stage specificity (NREM yes, REM and wake no) is in the meta-analysis. [b04, b05] [E]
- Rodent replay exists, and ripples matter for spatial memory. [a04-a06] [E at abstract level]
- Sleep deprivation after learning hurts memory, but only g = 0.28. Before learning it hurts more (g = 0.62). [a23]
- The CLS design principle works in AI continual learning. [c18, a19]
- Sleep-like replay in small nets recovers old tasks with a cost to the newest task. [a20]

### 5.2 Does not hold up, or is weak
- **Boosting the rhythm to boost memory.** Original tES (2006) and closed-loop audio (2013) gains. Henin 2019 failed: Bayes factors 0.25 to 0.30 favour equality, even though slow oscillation and spindle activity rose. [a11] Meta-analysis g = 0.25, p = 0.07. [d09] The 2022 meta-analysis with g = 0.68 is retracted. [d10] Two more nulls (N = 27, N = 34). [d13] Mouse single pulses did not beat sham. [d12] The rhythm changed, memory did not. [K04, K34]
- **Founding TMR skill result.** g = -0.08. The founding paper was small. [b06]
- **TMR in a new task.** 2025 nap null despite a neural signature of reprocessing. [b15]
- **Gist and false memory.** DRM meta-analysis null overall. [a14] Own-lab 2026 gist replication failed (N = 16). [a13]
- **Insight.** Wagner 2004 had a modest global p (.03) and cells of 20-22. [d01] The same lab reports it did not reproduce the high solution rate later. [d01] An N = 77 study found no sleep help for classical insight problems and magic tricks. [d03] Pink noise did not help. [d07] Stage is unsettled: N1 helps in one study (83 vs 30 percent, N = 103) [d04], N2 in another (85.7 vs 55.5 percent, preregistered) [d05]. Lerner and Gluck 2019: many nulls; which task was used mattered more than the process. [d08] No large direct replication of Wagner 2004 was found. [K29, K30]
- **Targeted cueing beyond natural sleep.** Puzzle solving rose with sleep (62 vs 24 percent) but TMR added nothing (56 to 58 percent). [d06]
- **Mechanism strength.** SO-spindle coupling pooled r = 0.07, correlational. [b07]
- **Capacity limit** rests on one study that its authors say is near its detection limit. [a12]
- Cordi and Rasch 2021 summarise: effects are smaller, more task-dependent, less SWS-related and less lasting than assumed. [b14]

### 5.3 Moderators
- Memory type: declarative vs procedural. The SO-spindle link depends on it. [b08]
- Age: coupling-memory link weaker with age. [b08]
- Task: for rule discovery, which task was used mattered more than process or design; temporal rules were easier than non-temporal. [d08]
- Test type: DRM effects larger for recall than recognition. [a14]
- Prior knowledge: insight benefit only for those with implicit knowledge before sleep. [d02]
- Time of test: effects after recovery sleep are smaller than immediate effects. [a23]
- Cue pairing: the odor had to be present at learning. [a03]
- Publication status: published TMR g = 0.31, unpublished 0.18 (ns). [b05]

### 5.4 Interventions that worked and that did not
- Worked (small): cueing in NREM; up-state timed cueing in one study; sleep over wake for retention at moderate load.
- Did not work or unproven: closed-loop audio in replications; tDCS plus audio; pink noise for insight; TMR on puzzles and priming; REM or wake cueing.

### 5.5 Independence note
b07/b08/b09/a15 are one meta-analysis. b04/b05/b06/b11 are one meta-analysis. b18, c15 and b19 are one paper. Counting them separately overstates support. [critique.md]

## 6. Language models

Core point: no LLM study tests the human ASC effects (stage dependence, spindle coupling, timing, capacity). All of them borrow the idea of an offline step and measure benchmarks. [c24, c25, K27] Results below are what an offline step did. The controls are weak: most are single runs on the authors' own benchmark, gains of 1 to 3 points are within plausible noise, and the offline step's own tokens are mostly not charged. [critique.md]

### 6.1 Offline precomputation (sleep-time compute)
- Lin et al. 2025: about 5x less test-time compute at equal accuracy on Stateful GSM-Symbolic and Stateful AIME; up to +13 percent (GSM) and +18 percent (AIME) with more sleep-time compute; 2.5x lower average cost per query with 10 related queries per context (re-checked). [b18, c15]
- It dominates parallel pass@k at matched cost. [b19]
- Moderator: benefit tracks how predictable the question is from the context. At large test-time budgets the test-time-only baseline can win slightly. [b19, c15]
- Limits: authors' own benchmarks. Stateful AIME has 60 questions; Claude 3.7 averaged over 10 runs, others over 3; o1 showed limited gains. [critique.md]
- This is the only study framed in tokens. [K15, K16, K28]

### 6.2 Offline consolidation of agent memory
| Paper | What the offline step does | Result | Caveat |
|---|---|---|---|
| Auto-Dreamer (Ye 2026) [c09, c10, d14, d15] | learned consolidator rewrites a memory region into a smaller abstract set, linked to sources; GRPO-trained | ScienceWorld 41.1% vs 34.1% best baseline (UMEM), +10.2 vs ReasoningBank 30.9; ALFWorld 60.2; WebArena 52.3. Writer-only / untrained / trained: ALFWorld 48.0 / 59.2 / 60.2; ScienceWorld 29.6 / 31.4 / 41.1; WebArena 44.2 / 46.6 / 52.3. Bank tokens: ALFWorld 50,735 to 6,900; ScienceWorld 61,679 to 5,700. GRPO adds +9.7 / +5.7 / +1.0 pp | Point estimates; CIs are task-bootstrap only, no seeds; ALFWorld CI [54.65, 65.59] nearly touches Reflexion 49.17 [43.59, 54.73]; WebArena CI overlaps all baselines; consolidator tokens not reported. Abstraction lost location detail in the look_at_obj_in_light family |
| LightMem (2025) [b20] | offline "sleep-time" update reorganises, dedups, abstracts; online path only appends | QA accuracy up to +7.7% (LongMemEval) / +29.3% (LoCoMo); total tokens down up to 38x / 20.9x | Whole pipeline; offline step not isolated |
| RecMem (Dai 2026) [c12, d18] | consolidate only when similar interactions recur; three tiers | LoCoMo GPT-4.1-mini construction tokens 193.2K vs 1520.8K (Mem0) and 1459.9K (A-Mem), -87.3% and -86.8%; overall 86.92 vs Mem0 66.23, A-Mem 73.25; ablation: full 81.10, no raw tier 51.88, no semantic tier 70.58, no episodic tier 79.94, no recurrence gating 74.22 | Full context beat it on LoCoMo (90.84 vs 86.92); gating bundled with the tier design; scores averaged over three runs; best equal-cost view so far |
| All-Mem (Lv 2026) [d16, d17] | offline merge, split, update; raw units kept with recovery links | LoCoMo F1 52.18 full; without Merge 49.02 (-3.16); without recovery links 50.06; anchors only 49.27; LongMemEval-s +4.40 and +9.09 over Mem0. Audit of 190 edits: 94.2% valid, 3.7% harmful; 0% archived units unreachable, median 2 hops | Offline cost 74.1k tokens per event, 1,237 per turn amortised vs 539 online; not matched against a baseline that spends it elsewhere; single runs |
| Hippocam (Zeng 2026) [c11] | consolidates finished intents, recursive abstraction, re-consolidation on recall, raw kept | ScienceWorld transfer 78.9% (+30.1 pp over Plain, +16.2 over ACE); LoCoMo 77.6% (+10.1 over A-Mem); MemoryAgentBench 64k 41.0% with recall, 27.0% without | A-Mem wins ScienceWorld elsewhere (87.2%); interleaved tasks cost 23.1 pp on GoodAI; single runs |
| Microsoft human-inspired memory (Kerestecioglu 2026) [d19, d20] | deterministic dedup, optional cluster merge, reconsolidation; no LLM calls in consolidation | LongMemEval S: raw RAG 78.4 [74.8, 82.0]; dedup-only 76.8 [73.0, 80.4]; dedup + reconsolidation 75.8; aggressive cluster merge 48.4 [44.0, 52.8]; assistant-recall questions 94.6 to 39.3. M-tier: raw 71.2, pipeline at 200K tokens 70.1, 50K 49.2, 25K 38.8 | Dedup reaches parity, not gain; the value is a store-size trade-off; one run per configuration |
| REALM (Song 2026) [c13] | reconsolidation after retrieval | LoCoMo 73.96 to 75.97 (+2.01); LongMemEval 62.98 to 65.11 (+2.13); largest: single-session preference +6.66 | About 2 points, single runs; not reproduced in the Microsoft ablation (75.8 vs 76.8) |
| RPMem (Zhao 2026) [d21] | learned write gate for parametric (LoRA) memory | Qwen3-8B PERMA: learned gate 85.52%; best fixed rule 31.31 pp lower; keep-all rank concatenation 13.84% | Needs training; gate trained on the benchmark family |
| CodaRAG, Dual-Layer Agentic Memory [b24, b22] | consolidate entities before retrieval; filter writes then consolidate to weights | cascade prunes up to 68% of redundant memory, keeps over 98% of exhaustive-retention QA exact match | CodaRAG headline numbers not extracted; fine-tuning based |
| EVAF (Han 2026) [b21] | surprise-times-valence gated LoRA writes | goal persistence 0.812 to 0.904 with 2 to 3 writes per 200 events; retrieval still wins plain facts (0.956 to 0.973); stale-memory invalidation unresolved | GPT-2 and TinyLlama; synthetic; single author |

### 6.3 What the memory-agent results show, by operation
- **Dedup is safe; summarising clusters is not.** Dedup-only 76.8 vs raw RAG 78.4 (CIs overlap); cluster merge 48.4. [d19] Yet All-Mem's Merge is worth 3.16 F1 when raw stays recoverable. [d16] Contested (K32).
- **Keeping source-linked raw episodes protects against abstraction loss.** RecMem without raw tier 81.10 to 51.88; All-Mem without recovery links 52.18 to 50.06. [d18, d16] [E] (K33)
- **Abstraction drops specifics.** Gist compression preserved temporal expressions in only 3.05 percent of cases; a one-sentence prompt fix raised this to 62.39 percent and temporal accuracy by +0.314 [0.254, 0.375], n = 315 (LoCoMo, 1,501 questions, Claude Sonnet 4.6). SWC-Temporal 0.468, SWC-Full 0.379, sliding window 0.238, truncation 0.171, full context 0.706 (299 questions). [c14] Single author.
- **Rewriting does most of the compaction before any training.** 6x to 11x smaller banks untrained. [c10, d14]
- **Recurrence gating** cuts construction cost 71 to 87 percent. [c12, d18] Bundled with tiers, so single-source (K20).
- **Cadence is an inverted U.** Auto-Dreamer cadence k = 1 and k = 20 both worse than the main setting (k = 10) on ScienceWorld; ALFWorld varied about 5 pp. Authors blame a larger, noisier region at k = 20. Figure only, no seeds. [d14] This is the only LLM hint of a capacity limit (K31).
- **Rule-extraction baselines are close to no memory.** ExpeL 28.33 vs no memory 28.69 on ScienceWorld; 33.59 vs 30.83 on ALFWorld. [d15] The rule-edit idea (ADD, EDIT, UPVOTE, DOWNVOTE) works in ExpeL's own tests (HotpotQA 40% at R3; retrieve-only 40.3 to 54.4; ExpeL+Reflexion 54.5 to 60.4) but not generally. [c20, d15] Insights came from gpt-4 and can be hallucinated. [c20]
- **Reflection in Generative Agents** is one of three components; believability TrueSkill ablations 25.64 to 26.88 vs 21.21 with no memory, planning or reflection (100 raters). It measures believability, not accuracy, and agents embellish memories. [c19]
- **Offline step vs the same tokens elsewhere.** Mostly nobody checked. RecMem charges construction tokens, and full context still beat it. No paper has several seeds. [d14, d16, d18, K28]

### 6.4 Training-based "sleep" (weights, architecture)
- Behrouz 2026 "Sleep": Qwen3-8B AIME-24 base 73.8, GRPO 76.4, OPSD 76.6, Sleep 79.2; AIME-25 69.0 vs OPSD 67.4; HMMT-25 46.1 vs 45.1; Qwen3-1.7B AIME-24 51.6 vs 53.2. Removing dreaming collapses knowledge-incorporation scores (35.7 and 36.2 vs about 47-49). Few-shot ARC subset: Sleep 80% vs SEAL 72.5%, TTT 10%, ICL 0%, but only 8 held-out tasks. Sequential language learning: ICL drops near pretrained behaviour; more consolidation stages nearly recover. Margins of 1 to 3 points, no seed variance, average@16. [c06-c08]
- Lee 2026 "Do Language Models Need Sleep?": hybrid models with offline recurrent passes. GSM-Infinite: Jet 6 loops 6-op 0.742 to 0.812, 8-op 0.351 to 0.388; Ouro 4 loops 6-op 0.419 to 0.615, 8-op 0.210 to 0.272. Ouro 1.4B, window 512, 2-op: 0.596 to 0.905. Easy problems saturate. Needs fine-tuning. [c01-c03]
- SleepGate (Xie 2026): learned sleep cycle over the KV cache in a 793K-parameter toy model; retrieval under proactive interference 99.5 percent (depth 5), 97.0 (10), 73.5 (15), 16.5 (30); stale retrieval 62 percent at n = 30; baselines under 18 percent (the text names StreamingLLM at 18.0 at n = 2). Synthetic, preprint. [c04, c05] Proactive interference in LLMs falls log-linearly toward zero with stale updates; "ignore old values" prompts help only marginally (second-hand). [c21]
- Small nets: Tadros 2022 (numbers in section 3); Bazhenov 2026: after task 5 earlier tasks scored 0.00 without sleep and about 0.33 to 0.75 with it (read from a garbled table); recovery shrinks as tasks pile up. [a19, c16, b23]
- CLS-ER: two slow EMA models plus a buffer; Seq-Tiny-ImageNet with a 200-sample buffer, +176 percent over ER and +114 percent over DER++; gains largest at small memory. [c18]
- None of these can be run by a scaffold alone.

### 6.5 Products
- Anthropic "Dreams" for Claude Managed Agents (2026, secondary blog only): takes a memory store plus 1 to 100 past sessions and writes a new store with duplicates merged, stale entries replaced, insights added. No benchmark numbers. [c23] Not evidence of effect.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = SCHEMA.md section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Keep source-linked raw episodes beside any abstracted rule.** Rules carry pointers to the episodes they came from; the agent can open them on demand. Part: memory (lessons). [E] Evidence: d16, d17, d18, c10, c14 (K33, K18). Why: RecMem raw tier worth 29 points; All-Mem recovery links 2 to 3 F1; summarising dropped assistant-recall questions 94.6 to 39.3.
2. **If the offline job merges anything, merge near-duplicates and keep originals reachable; do not summarise clusters.** Part: memory. [E] that cluster summarising is destructive; dedup itself only reaches parity (K32 is [C] on merge). Evidence: d19, d16, c10.
3. **Protect time, place and number in every gist prompt.** One sentence ("preserve dates, places, numbers, names") in the consolidation prompt. Part: memory (S9 lesson line). The loss is repeated in three sources, so the instruction is cheap and safe; the size of the fix (3.05 to 62.39 percent) is [S]. Evidence: c14, d18, d19. Still logged per G7.
4. **A consolidated rule is trusted only after it has helped on two different problems.** This matches SCHEMA.md section 5. New evidence supports it: gist and DRM-like tasks show no reliable sleep gain, invented detail is a known cost of gist, and a hand audit still found 3.7 percent of consolidation edits harmful. Part: memory. [E] Evidence: a14, a13, b17, d17.
5. **Every consolidation test needs a no-replay arm and an equal-token arm.** Part: G7. [E] Evidence: b05, b14, d09, d10 (TMR and stimulation effects shrank or were retracted once controls and bias were handled).
6. **Do not claim biological validation for any consolidation design.** Part: G7. [E] Evidence: c24, c25, d10, d13.

### Test first (not yet in the schema)

7. **An offline pass that writes rules from a batch of episodes (S9 extension).** Part: memory. [C] Evidence: c09, c10, c12, d16, d19, d15 (K17, K26). Gains on several benchmarks but with mixed baselines, no seeds and uncharged offline tokens; one dedup-only design reaches only parity; ExpeL scored near no memory in Auto-Dreamer's CIs.
8. **Sleep-time precomputation over known context.** Part: memory / S1. [S] Evidence: b18, c15, b19. About 5x test-time saving on authors' own benchmarks; depends on query predictability.
9. **Recurrence-gated consolidation** (consolidate a topic only after it recurs). Part: memory. [S] Evidence: c12, d18. Saves 71 to 87 percent construction tokens; bundled with tiers.
10. **Batch-size cap per consolidation pass.** Part: memory. [S] Evidence: a12, d14 (K08, K31). The human 160 vs 320 result is near its detection limit; the LLM cadence sweep is figure-only.
11. **Prioritised replay** (hub, surprise, reward vs uniform). Part: memory. [S] Evidence: a21, c12, d21. No LLM paper tests it against uniform replay at equal tokens (K35).
12. **Reconsolidation at use time.** Part: memory (S9). [C] Evidence: c13, d19, d20. +2 points reported, not reproduced in one ablation.
13. **Separate pruning from abstraction.** Part: memory. [C] Evidence: a17, a18, d19, d14 (K14). Ablation needed.
14. **Replay in an idle step versus mid-task (TMR analogue).** Part: S9 / memory. [E] small in humans, [S] for LLMs. Evidence: b04 (K01, K02).
15. **Rules from episodes versus summaries only.** Part: memory. [C] Evidence: a07, d01-d08 (K09). Human insight evidence is inconsistent; test only for downstream use.

## 8. Concrete tests on our bench

All arms use equal total tokens, counting the offline pass. At least 3 seeds. Report total tokens per arm. Add a no-memory arm in each test.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multi-episode tasks where later items share a hidden rule (ARC-style families, BRAINTEASER families, ALFWorld-style) | A: offline pass of N tokens then answer; B: same N tokens as extra retrieval or extra reasoning at query time; C: no memory | accuracy on held-out items of the same family | A over B small positive on same-family items; none on unrelated items. If A is not above B, drop the offline job (K28) |
| T2 | Same items as T1 | A: offline pass writes rules; B: offline pass writes summaries only; C: raw append-only | accuracy on items needing the rule | A over B by 2 to 5 points if abstraction helps; contested (K09) |
| T3 | Questions on dates, places, numbers from consolidated memory | A: gist prompt as is; B: gist prompt plus "preserve time, place, numbers"; C: rules with source links opened on demand | accuracy on date/place/number questions; invented-detail rate | B and C large over A (c14: temporal preservation 3.05 to 62.39 percent) |
| T4 | Same memory with a planted false episode and a planted near-duplicate | A: consolidate then answer; B: raw only | planted-false-rule rate; harmful merge rate | A harmful rate near 3.7 percent (All-Mem audit); above 5 percent means keep new rules untrusted longer |
| T5 | Batch sizes 5, 10, 20, 40 episodes at the same total episodes | one arm per batch size | rule quality and downstream success per batch size | inverted U if the capacity analogue holds; flat if not (K31, K08) |
| T6 | Episodes with recurring and one-off topics | A: recurrence-gated; B: every-turn consolidation | accuracy, construction tokens | same accuracy at 70 percent or fewer tokens (K20) |
| T7 | Facts with hubs (many links) and leaves | A: replay hubs first; B: uniform; C: surprise-first | recall on hub and leaf questions | small gain for A on hub questions; Feld 2022 N = 19 is weak (K12) |
| T8 | Contradicting new facts after consolidation | A: update on retrieval; B: never update | accuracy on update questions; drift rate | about +2 points (K21); needs many seeds |
| T9 | Queries split into predictable and unpredictable from context | A: sleep-time precompute; B: test-time only | accuracy per half at equal tokens | A better on the predictable half; B wins at large budgets (K16) |
| T10 | Same memory | A: dedup only; B: dedup plus abstraction with raw kept; C: abstraction with raw deleted; D: forgetting only | accuracy, store size | B at least equal to A with smaller store; C worst (K32, K33) |
| T11 | Idle step vs mid-task replay of key facts | A: replay at task boundary; B: replay mid-task; C: none | later recall on held-out questions | A over B over C, small (K02, K05); lowest priority |
| T12 | Facts that fit an existing rule vs facts that break it | A: consolidate each; B: no consolidation | integration accuracy for new facts of each kind | schema-consistent facts integrate faster (McClelland 2020 prediction; no LLM test found) |

## 9. What does not transfer, and why

- **Oscillation phase, spindles, ripples.** An LLM has no slow oscillation. Phase-specific replay (UP vs DOWN) has no meaning in a prompt. The human evidence for timing is one study of 24 people. [b10]
- **Stage dependence (SWS vs N2 vs N1 vs REM).** Human stage results conflict even among themselves (N1 vs N2). Do not encode a stage rule. [d04, d05]
- **Rhythm boosting by stimulation.** Fails or is weak in humans and mice. Nothing to port. [a11, d09, d13]
- **Sleep deprivation effects.** Not applicable. Used only as a prior that the gain is small. [a23]
- **Weight-level methods** (SRC, SleepGate, Sleep, Auto-Dreamer GRPO training, RPMem, EVAF, CLS-ER). They need training or architecture change; our agent is scaffold-only. One trade-off does transfer: restoring old items costs newest-item accuracy. [a20]
- **Sleeping through a task.** The brain consolidates while offline for free. An agent's offline step costs tokens. That is why equal-token testing (G7) is the whole question.
- **"Gist" is not a free good.** Human gist (DRM) shows no reliable sleep effect, and LLM gist compression loses specifics. So "more schema-like" can hurt an agent. [a14, c14]
- **Rodent spatial replay** is a premise about biology, not something an agent can use directly. [a04-a06]

## 10. Open questions

1. Does an offline pass beat the same tokens spent at query time? Only sleep-time compute asks this. [K28]
2. Which operation carries the gain: dedup, abstraction, forgetting, or recurrence gating? No paper isolates all four at fixed tokens. [K32]
3. How much does abstraction lose, by type (dates, places, numbers, exceptions)? Only temporal expressions in LoCoMo and one Auto-Dreamer family are measured. [K19]
4. Is there a capacity limit in batch size per pass? One cadence sweep, figure only. [K31]
5. What are the exact numbers for Rasch 2007 and Marshall 2006? Not open access in this run.
6. Do the Henin follow-ups exist, and do they change the robustness picture? Not found.
7. Does prioritised replay (hub, surprise, reward) beat uniform replay in LLM agents? Not tested. [K35]
8. How often do consolidation passes invent rules (DRM-like false memory)? Not measured in any paper read. [K35]
9. Do LLMs integrate schema-consistent facts faster than inconsistent ones? No study. [K35]
10. Is reconsolidation worth more than about 2 points once variance is controlled, and does it cause drift? [K21]
11. Is there a large direct replication of Wagner 2004? None found; the largest related studies are N = 103, 90, 77 and 72. [K30]
12. Is the Anthropic "Dreams" feature better than plain dedup? No numbers.
13. Do the absences above hold? The search budget ran out, so absences are weak. [K27, K35]

## 11. Sources

Marks: [V] opened (as recorded in the evidence files; critique.md re-checked several numbers) or [M] snippet or abstract only.

**Human and animal sleep**
- [M] Klinzing, Niethard, Born 2019 (a01). https://pubmed.ncbi.nlm.nih.gov/31451802/
- [M] Marshall et al. 2006 (a02, b12). https://pubmed.ncbi.nlm.nih.gov/17086200/ and https://pubmed.ncbi.nlm.nih.gov/17108967/
- [M] Rasch et al. 2007 (a03, b13). https://pubmed.ncbi.nlm.nih.gov/17347444/ and https://pubmed.ncbi.nlm.nih.gov/17463252/
- [M] Wilson and McNaughton 1994 (a04). https://pubmed.ncbi.nlm.nih.gov/8036517/
- [M] Ji and Wilson 2007 (a05). https://pubmed.ncbi.nlm.nih.gov/17173043/
- [M] Girardeau et al. 2009 (a06). https://pubmed.ncbi.nlm.nih.gov/19749750/
- [M] Wagner et al. 2004 (a07). https://pubmed.ncbi.nlm.nih.gov/14737168/
- [M] McClelland, McNaughton, O'Reilly 1995 (a08). https://pubmed.ncbi.nlm.nih.gov/7624455/
- [M] McClelland, McNaughton, Lampinen 2020 (a09). https://pubmed.ncbi.nlm.nih.gov/32248773/
- [M] Ngo et al. 2013 (a10). https://pubmed.ncbi.nlm.nih.gov/23583623/
- [V] Henin et al. 2019 (a11). https://pmc.ncbi.nlm.nih.gov/articles/PMC6831893/
- [V] Feld, Weis, Born 2016 (a12). https://pmc.ncbi.nlm.nih.gov/articles/PMC5020097/
- [V] Lutz et al. 2026 (a13). https://pmc.ncbi.nlm.nih.gov/articles/PMC12856105/
- [V] Newbury and Monaghan 2019 (a14). https://pmc.ncbi.nlm.nih.gov/articles/PMC6488554/
- [V] Ng, Noh, Spencer 2025 (a15, b07-b09). https://pmc.ncbi.nlm.nih.gov/articles/PMC12507438/
- [V] Ngo, Fell, Staresina 2020 (a16). https://pmc.ncbi.nlm.nih.gov/articles/PMC7363445/
- [M] Tononi and Cirelli 2014 (a17). https://pubmed.ncbi.nlm.nih.gov/24411729/
- [M] Norimoto et al. 2018 (a18). https://pubmed.ncbi.nlm.nih.gov/29439023/
- [V] Feld et al. 2022 (a21). https://pmc.ncbi.nlm.nih.gov/articles/PMC9445065/
- [V] Liu et al. 2025 (a22). https://pmc.ncbi.nlm.nih.gov/articles/PMC12489065/
- [V] Sleep deprivation meta-analyses 2022 (a23). https://pmc.ncbi.nlm.nih.gov/articles/PMC8893218/
- [M] Rasch and Born 2013, PMC copy (a24), could not be opened. https://pmc.ncbi.nlm.nih.gov/articles/3768102
- [V] Rasch and Born 2013, Princeton copy (b01-b03, b25). https://princetonuniversity.github.io/NEU-PSY-502/_static/pdf/Class%2014/rasch-born-2013-about-sleep-s-role-in-memory.pdf
- [M] Kumaran, Hassabis, McClelland 2016 (a25), PMID unverified. https://pubmed.ncbi.nlm.nih.gov/27315762/
- [V] Hu et al. 2020 TMR meta-analysis (b04-b06, b11). https://pmc.ncbi.nlm.nih.gov/articles/PMC7144680/
- [V] Ngo and Staresina 2022 (b10). https://pmc.ncbi.nlm.nih.gov/articles/PMC9636934/
- [M] Cordi and Rasch 2021 (b14). https://pubmed.ncbi.nlm.nih.gov/33152570/
- [M] Ball et al. 2025 (b15). https://pubmed.ncbi.nlm.nih.gov/?term=No+evidence+for+a+targeted+memory+reactivation+effect+on+word-meaning+priming
- [M] Lowe et al. 2024 abstract (b16). https://pubmed.ncbi.nlm.nih.gov/?term=N2+sleep+inspires+insight
- [M] Lewis and Durrant 2011 (b17). https://pubmed.ncbi.nlm.nih.gov/21764357/
- [V] Verleger et al. 2013 (d01, d02). https://pmc.ncbi.nlm.nih.gov/articles/PMC3902672/
- [V] Schonauer et al. 2018 (d03). https://pmc.ncbi.nlm.nih.gov/articles/PMC5834438/
- [V] Lacaux et al. 2021 (d04). https://pmc.ncbi.nlm.nih.gov/articles/PMC8654287/
- [V] Lowe et al. 2025 (d05). https://pmc.ncbi.nlm.nih.gov/articles/PMC12200826/
- [V] Beijamini et al. 2021 (d06). https://pmc.ncbi.nlm.nih.gov/articles/PMC7965947/
- [V] Vickrey and Lerner 2023 (d07). https://pmc.ncbi.nlm.nih.gov/articles/PMC10722168/
- [V] Lerner and Gluck 2019, abstract level (d08). https://pmc.ncbi.nlm.nih.gov/articles/PMC6779511/
- [V] Wunderlin et al. 2021, abstract record (d09). https://doi.org/10.1093/sleep/zsaa296
- [V] Stanyer et al. 2022, retraction notice (d10). https://doi.org/10.1111/jsr.70111
- [V] Hausdorf et al. 2025 (d11). https://pmc.ncbi.nlm.nih.gov/articles/PMC12493016/
- [V] Aksamaz et al. 2024 (d12). https://pmc.ncbi.nlm.nih.gov/articles/PMC11214843/
- [V] Closed-loop stimulation nulls, insomnia and home, abstract records (d13). https://doi.org/10.1111/jsr.70247 ; medRxiv 10.1101/2025.03.04.25321710

**AI and LLM**
- [V] Tadros et al. 2022 (a19, a20, c17). https://pmc.ncbi.nlm.nih.gov/articles/PMC9755223/ ; https://doi.org/10.1038/s41467-022-34938-7
- [V] Lin et al. 2025 sleep-time compute (b18, b19, c15). https://arxiv.org/abs/2504.13171
- [V] LightMem (b20). https://arxiv.org/abs/2510.18866
- [V] Han 2026 EVAF (b21). https://arxiv.org/abs/2606.26806
- [V] Dual-Layer Agentic Memory 2026 (b22). https://arxiv.org/abs/2608.22215
- [V] Bazhenov et al. 2026 (b23, c16). https://arxiv.org/abs/2606.08447
- [V] CodaRAG 2026 (b24). https://arxiv.org/abs/2604.10426
- [V] Lee et al. 2026 (c01-c03, c24). https://arxiv.org/abs/2605.26099
- [V] Xie 2026 SleepGate (c04, c05). https://arxiv.org/abs/2603.14517
- [M] Wang and Sun 2025 PI-LLM, second-hand via Xie (c21). https://arxiv.org/abs/2603.14517
- [V] Behrouz et al. 2026 (c06-c08). https://arxiv.org/abs/2606.03979
- [V] Ye et al. 2026 Auto-Dreamer (c09, c10, c25, d14, d15). https://arxiv.org/abs/2605.20616 ; https://arxiv.org/pdf/2605.20616
- [V] Zeng et al. 2026 Hippocam (c11). https://arxiv.org/abs/2610.12124
- [V] Dai et al. 2026 RecMem (c12, d18). https://arxiv.org/abs/2605.16045 ; https://arxiv.org/pdf/2605.16045
- [V] Song et al. 2026 REALM (c13). https://arxiv.org/abs/2609.16053
- [V] Kyrkewood 2026 (c14). https://arxiv.org/abs/2608.11775
- [V] Arani et al. 2022 CLS-ER (c18). https://arxiv.org/abs/2201.12604
- [V] Park et al. 2023 Generative Agents (c19). https://arxiv.org/abs/2304.03442
- [V] Zhao et al. 2024 ExpeL (c20). https://arxiv.org/abs/2308.10144
- [M] Momennejad et al. 2018, second-hand via Lee (c22). https://arxiv.org/abs/2605.26099
- [M] Anthropic Dreams, secondary blog (c23). https://dev.to/czmilo/openclaw-dreaming-guide-2026-background-memory-consolidation-for-ai-agents-585e
- [V] Lv et al. 2026 All-Mem (d16, d17). https://arxiv.org/pdf/2603.19595
- [V] Kerestecioglu et al. 2026 (d19, d20). https://arxiv.org/pdf/2605.08538
- [V] Zhao, Cao et al. 2026 RPMem (d21). https://arxiv.org/pdf/2609.23466

Not in our files: Diekelmann and Born 2010 (the named founding review; Klinzing 2019 and Rasch and Born 2013 stand in for it).

**Links to other subfields run in parallel** (not covered here): Encoding specificity and cue-dependent retrieval (cue use in TMR); Expertise reversal and fading; Model-based versus model-free control; Sampling and voting (self-consistency); Language agents as architectures; Case representation; Knowledge organisation: illness scripts, categories; Bayesian conditionalization; Cognitive breakdowns; Human error and recovery. Earlier documents: see 00_FIELDS.md section "Deep research by subfield".

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 2 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B04.01-K11** (reworded: the sources support less). Newbury & Monaghan 2019 found no overall sleep effect but moderated effects (list length, recall>recognition); Lutz et al. (J Sleep Res 2026) is an adapted, not direct, replication of their 2017 protocol (N=16, 12 at one year, 2 excluded from sleep analyses) and tests visual gist, not word-list DRM. Corrected claim: The DRM meta-analysis (Newbury & Monaghan 2019) found no overall effect of sleep on accurate or false memory, with sleep effects only emerging with moderators such as shorter lists and recall rather than recognition tests; an adapted follow-up of the authors' own 2017 visual-gist protocol (Lutz et al. 2026, N=16) found no gist difference between sleep and wake, so these two sources do not show a reliable sleep effect on DRM gist.
- **B04.01-K22** (now single-source: the sources are not independent). Numbers match Tadros 2022 (CIFAR-10 19.01 to 44.55; CUB-200 new-task 95.41 to 45.4), but the 2026 follow-up (A. Bazhenov, Delanois, Krishnan) shares Krishnan with Tadros et al. and builds directly on that SRC method, so all evidence is one group's work; a22 a19 a20 c17 are the same paper.
- **B04.01-K34** (number corrected). Retraction notice of Stanyer et al. 2022 was first published online 16 June 2025 (it sits in the Feb 2026 issue, vol 35 no 1), not 'in 2026'; all other numbers (g=0.25 p=0.07 10 studies 177; g=0.68; N=27; N=34; N=20) match. Corrected claim: Acoustic slow-wave stimulation evidence is weaker than the original papers suggested: the 2021 meta-analysis found g = 0.25 (p = 0.07, 10 studies, 177 people); the 2022 meta-analysis that reported g = 0.68 in under-35s was retracted (notice online June 2025, in the February 2026 issue) for using SE as SD and wrong sample sizes; closed-loop stimulation was null for memory in chronic insomnia (N 27) and at home (N 34, authors flag low power); and a tDCS plus CLAS study (N 20) was null overall, with a memory decrement only in an exploratory high-fluid-intelligence subgroup.
- **B04.01-K01** (now single-source: only one opened source, code check).
- **B04.01-K02** (now single-source: only one opened source, code check).
- **B04.01-K03** (now single-source: only one opened source, code check).
- **B04.01-K07** (now single-source: only one opened source, code check).
- **B04.01-K24** (now single-source: only one opened source, code check).
- **B04.01-K29** (now single-source: only one opened source, code check).
