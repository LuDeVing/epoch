# Relevance-based fate of memories: deep document

*Subfield B04.03. Evidence ids (a01 to d18) are in evidence_a-d.jsonl; claim ids (K01 to K26) are in claims.jsonl; the cross-check is in critique.md. Numbers were checked against opened text unless marked otherwise.*

## 1. What it is

The idea: whether a memory is kept, strengthened or erased depends on how useful it is expected to be later. Feld and Born (2019/2020) use this to join two sleep theories that seem to clash. Active systems consolidation says sleep replays memories and strengthens them. Synaptic homeostasis says sleep scales down weak synapses and so erases things. The join: relevant traces are strengthened, irrelevant ones fade or are erased (a04, a07, b12).

Honesty point: the Feld and Born text is a review. It adds no new data on relevance. The reconciliation is a framing, not a head-to-head test (critique.md).

Why it matters for our agent: our memory holds one-line lessons by problem class (SCHEMA section 5). The question is which lessons to keep, promote or drop, and by what signal. The human finding says "expected future use" decides. The honest reading of the human data is weaker than the headline: the instruction effect is real but is mostly an encoding or attention effect that also appears in wake. The sleep-specific part is small or absent (K02, K21, K22).

Three things must be kept apart:
1. A relevance tag set after learning that changes what an offline process does (the Wilhelm claim).
2. A relevance tag that changes how well an item is encoded (the replicated effect).
3. A proxy for relevance in LLM memory (recency, access count, LLM rating, query match). No LLM study tests whether such a proxy predicts real later use (K20).

## 2. History and theories in depth

**Active systems consolidation (Diekelmann and Born 2010, a24; abstract only).** In slow-wave sleep, slow oscillations, spindles and sharp-wave ripples coordinate reactivation of hippocampal memories and their move to cortex. REM supports synaptic consolidation. This is the "strengthen" half.

**Synaptic homeostasis (Tononi and Cirelli 2014, a23; abstract only).** Sleep renormalises net synaptic strength by down-selecting synapses. This is the "erase weak traces" half. Crick and Mitchison (1983) proposed REM as an unlearning process; Oudiette 2013 builds on this (a11).

**Reconciliation (Feld and Born 2019/2020; a04, a05, a06, a07, b12, c23).** Replay may strengthen relevant and weaken irrelevant traces. Ripple timing in hippocampal sub-regions may decide potentiation versus depression. Human evidence for homeostasis is mainly better new learning after sleep. They discuss two ways reward selects memories:
- Account 1: hippocampal replay drives striatal and VTA dopamine during sleep.
- Account 2: a dopamine tag is set at learning, and replay then runs with no extra dopamine. Drug data favour Account 2. Pramipexole (D2 agonist) before sleep removed the high-over-low reward advantage in recognition but left the encoding-duration benefit. Sulpiride (about 60 percent D2 block) did not change the reward advantage (a05, b11).

They also note that weakly encoded memories are replayed more and gain more from sleep, so relevance picks different items than strength does (a06).

**Memory triage (Stickgold and Walker 2013, a20, opened).** Step one: choose which memories get sleep processing, guided by emotion, reward and instructions around encoding. Step two: choose the form of processing (stabilise, integrate, abstract).

**Continuous reshaping (Rouast and Schoenauer 2023, a21; abstract only).** Memories stay malleable and are shaped repeatedly by anticipated demand, flexibly and reversibly.

**Schema building (Lewis and Durrant 2011, a22; abstract only).** Overlapping replay strengthens shared elements and builds schemas. Relevant to abstraction of lessons.

**Founding empirical line.** Fischer and Born 2009 (reward announced after training; a19, abstract only). Wilhelm et al. 2011 (test expectancy). Saletin et al. 2011 (directed forgetting). Van Dongen et al. 2012 (within-subject relevance). Oudiette et al. 2013 (value plus cued reactivation). Then replications and nulls: Wamsley 2016, Reverberi 2020, Ashton and Cairney 2021, Barner 2023, Kurdziel 2025. The systematic review (Davidson and Pace-Schott 2021; a16, b07) concluded most studies do not support sleep-selective strengthening, and effects are likely much smaller than often suggested.

**AI line.** MemoryBank (2023) and Generative Agents (2023) use forgetting curves and importance ratings. In 2025 and 2026 a cluster of "sleep-inspired" memory papers appeared (SleepGate, SCM, OBLIVION, FadeMem, RD-Forget, ConsolidationBench, Language Models Need Sleep). Almost all are 2026 preprints by the method authors.

## 3. Core findings with exact numbers

Status: Established = replicated or consistent across several sources. Contested = mixed results. Single = one source.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Expecting a test raised overnight retention after sleep (word pairs) | Sleep expected 117.29+-3.54 vs unexpected 105.23+-3.01 percent, p=0.014. Expectancy x sleep/wake interaction p=0.05. Wake groups 96.7 to 104.9, no expectancy effect (p>0.49). Exp 1: 142 tested, 104 in main analysis | Wilhelm 2011 (a01, b01) | Contested |
| Same, card locations and finger tapping | Cards 98.80+-4.92 vs 73.13+-9.08 percent (p=0.019). Tapping gain 131.13+-4.08 vs 116.95+-5.04 percent (p=0.037). Exp 2 N=49 (10 excluded). Novel sequence: no difference (p>0.93) | Wilhelm 2011 (a02) | Contested |
| Not rehearsal or priming; more deep sleep in expecting group | Stage 4 8.20 vs 4.07 percent (p=0.03); Exp 2 11.72 vs 5.11 (p=0.01). Slow oscillation power (first 20 min) vs retention r=0.71 expected, r=-0.25 unexpected. Surprise recall at 30 min kept the gap (p=0.03) | Wilhelm 2011 (a03) | Single |
| Within-subject relevance (picture locations): sleep kept relevant set | 3-way interaction F=13.19, p=0.001. Sleep: relevant loss -1.8 vs irrelevant -3.1 (diff 1.3+-0.6, p=0.045). Wake: relevant -5.0 vs -3.3 (diff -1.7, p=0.005). 60 tested, 50 analysed (10 excluded for doubting the instruction) | Van Dongen 2012 (a12, b03) | Contested |
| Maze and motor: expectancy helps equally after sleep and wake | Maze time: expectation F(1,71)=7.35, p=.008, partial eta2=0.09; interaction F=0.77, p=.38. Motor: expectation F(1,89)=4.18, p=.04; interaction F=0.96, p=.33. About 100 participants (task n=75 and 94). 70 percent of unexpected-test subjects suspected a test | Wamsley 2016 (b05) | Established (null interaction) |
| Direct online replications of Wilhelm: no interaction | Exp 1: 162 analysed, 12 h interaction F=0.07, p=.786, BF01=4.00; 7 d F=1.34, p=.249, BF01=2.47; delay F(1,158)=9.67, p=.002; expectancy p=.428. Exp 2: 124 analysed (82 excluded for expectancy mismatch), 100 pairs, delay F(1,120)=5.27, p=.023, interaction null | Ashton and Cairney 2021 (d01) | Established failure |
| Closer repeat of Van Dongen, sleep only: no relevance effect | N=38; no sleep variable correlated | Reverberi 2020 (b04, via review) | Single |
| Weak replication of Van Dongen | 28 sleep, 28 wake. Sleep F(1,54)=6.71 p=.012; relevance F(1,54)=8.78 p=.005; interaction p=0.12 (12 h p=.35; 1 week p=.096). Sleep relevant vs irrelevant at 1 week t(27)=2.75 p=.01; wake t(27)=0.47 p=.64. 12 h retention sleep 58.7 vs 44.5; wake 41.1 vs 34.5. Odor cueing in sleep added nothing selective (odor n=23, vehicle n=20) | Barner 2023 (a13, a14) | Contested |
| Rough pooled expectancy x sleep effect | Five tests, signs set positive: r=0.097, 95% CI [0.010, 0.183]. Own back-calculation. No published meta-analysis exists | d02, d18 | Contested |
| Remember instruction beats emotion; sleep did not change behaviour | Two studies (online; in-lab with EEG). Remember instruction raised recognition and recall; sleep condition had no effect | Kurdziel 2025 (a17) | Single |
| Directed forgetting: nap boosted Remember words only | N=46 (23/23). Group x cue F(2,43)=6.17, p=0.004; group main F(1,44)=6.44, p=0.015. Fast spindles at P3 vs remember-minus-forget r=0.66, p=0.0006 | Saletin 2011 (a08, a09) | Contested |
| Directed-forgetting replications | Scullin: young N=50 partly positive (free recall, not recognition), older N=45 null. Rauchs N=25 null. List-method: Abel and Baeuml N=128, N=112 positive; Blaskovich N=112 and Hupbach N=92 null | Davidson 2021 (b09) | Contested |
| Reward as relevance cue | Of 12 datasets with a sleep x reward test: 4 positive, 2 mixed, 6 absent (reviewer's count). Fischer and Born N=76 positive; Tamaki N=47 and 40 positive; Tucker N=75 and 77 null; Oudiette N=30 null | Davidson 2021 (b08) | Contested |
| Time-pressure reward reversed the effect | Sleep-only, N=65, reversed on 2 of 4 outcomes | Stamm 2014 (b06) | Single |
| Value tag plus cueing in sleep: reactivation rescues low-value items | 60 adults, 4 experiments, n=15 each. Pre-nap recall 30.5 vs 23.6 items (high vs low value). Exp I loss low minus high 1.05+-0.15 cm error, p=0.004. With sound cues 0.30+-0.09 cm, p=0.2; cue x experiment F(1,28)=5.0, p=0.03. Without cues, high-reward items better kept in sleep and wake alike | Oudiette 2013 (a10, a11, b08) | Single |
| Emotion not preferentially kept by sleep | Meta-analysis, 31 studies, 36 datasets, no overall effect. Moderators: free recall, initial-learning control, full-night design | Lipinska 2019 (b13) | Established |
| Review verdict | Most studies do not show sleep-selective effects; no sleep variable reliably predicts which memory is picked | Davidson and Pace-Schott 2021 (b07, b26) | Established |
| Test-expectancy tally | One count: 3 positive (one lacks wake control), 2 none, 1 opposite. Another: interaction in 2 of 4 papers | a16, b07 | Contested |
| Weak traces replayed more (rats) | 19 sessions, 4 rats. Sleep replay track 1 vs 2 p=0.0002 and p=0.002 (Wilcoxon). Replay rose with laps, fell with familiarity | Huelin Gorriz 2023 (b15) | Single |
| Weak-trace sleep benefit is partly a ceiling effect | 120 analysed. No interference: weak sleep>wake t=3.25, p=.003, d=1.19; strong t=1.11, p=.28, d=.41. With interference: weak d=.83, strong t=4.64, p<.001, d=1.70 | Petzka 2021 (d03) | Single |
| Sleep keeps weak and strong alike; wake loses mostly weak | N=90 (30 per group). No oscillation measure related to retention. Abstract only | Schabus 2025/26 (d04) | Single |
| Learning-time theta tags items for sleep | N=31 nap vs wake. Sleep advantage t(30)=2.49, p=.019, d=0.45. Associative change -12.33 (sleep) vs -19.88 (wake). Classifier cluster 0.87-1.13 s, p=.010, d=0.72; immediate test p=0.08. 16+-4 percent of spindles coupled to a slow oscillation; early theta vs classifier peak r=0.39 | PLOS Biology 2026 (a18, b16, d17) | Single |
| Boundary: huge load | 640 word pairs: wake -11.2 (SEM 1.73) vs sleep -8.5 (SEM 1.70), F(1,74)=1.25, p=.27; N=78; harm beyond d=-0.20 ruled out (p=0.02); BF01=8.26 against harm, 1.45 for benefit. Earlier benefit at 160 pairs, none at 320. Recall was tested after another normal night | Kolibius 2021 (c24, d14) | Single |

## 4. Mechanisms and models

**4.1 Tag at learning, replay at sleep (human mechanism).** At encoding, a signal marks an item (reward, expected test, theta activity). In sleep, tagged items are replayed more, and slow-oscillation and spindle coupling carries them to cortex. Implementable analogue: at write time, store a field `expected_use`. A consolidation step reads the field and decides promote, keep or demote. Evidence that the tag is set at learning, not in sleep: pramipexole data (a05) and theta at learning predicting post-sleep survival (a18). All single-source (K07, K11).

**4.2 Replay rate by experience (rats).** Sleep replay count rises with laps run and falls with familiarity (b15). Engineer reading: replay priority = novelty times effort, discounted by how often the item was already consolidated. This is a prioritisation rule, not a retention rule. See the parallel subfield on prioritised memory access.

**4.3 Strong versus weak.** Weak traces get replayed more (a06), but the sleep gain for weak items depends on test difficulty (d03), and another study found sleep protects both (d04). Rule: do not drop a lesson because it looks weak. Weak plus relevant is a promotion candidate.

**4.4 Cue-based reactivation (targeted memory reactivation, TMR).** Playing a cue linked to an item during slow-wave sleep strengthens it. Oudiette 2013 rescued all low-value items; Barner 2023 found no selective benefit for relevant items. Agent analogue: re-reading a lesson at a consolidation step. This is rehearsal, not deletion.

**4.5 Reconsolidation / malleability (Rouast and Schoenauer).** Memories are reshaped each time they are used. Agent analogue: update a lesson's score or text whenever it is retrieved, as in ExpeL's UPVOTE and DOWNVOTE.

**4.6 LLM memory scoring formulas (all implementable).**
- MemoryBank (c01): retention R = exp(-t/S). S starts at 1, adds 1 on each recall, and t resets to 0. Use protects a memory.
- Generative Agents (c02): retrieval score = recency (0.995 per game hour) + importance (LLM rating 1 to 10) + relevance (cosine), each min-max scaled to [0,1]. Nothing is deleted.
- Chen and Cheng (b17, b18, d08): multi-factor value, weighted sum of reliability (0.64), emotional intensity (0.55), self/user relevance (0.23), goal relevance (0.00). Weights fitted against gold-evidence retention on LongMemEval-S. Not a measure of later use.
- ExpeL (c17): insights with ADD, EDIT, UPVOTE, DOWNVOTE; importance count; removed at zero.
- Xiong 2025 (c05, d07): delete a record after at least n retrievals if the mean utility of those retrievals is low. Selective add: store only runs judged good.
- FadeMem (c08): two layers with different decay speeds; decay depends on semantic relevance, access frequency and age; important memories decay 3 to 5 times slower.
- SF-AMS (b24): survival score from usage, redundancy and time, plus entity signals.
- Graph pruning (c12): weights on recency, access frequency, degree centrality, age.
- OBLIVION (b21, c15, d11): forgetting as lowered accessibility. Read path: consult memory only when agent uncertainty and buffer utility call for it. Write path: reinforce only memories that contributed to the answer. Decayed items can be reactivated by cues.
- RD-Forget (c07, d10): keep a source archive; build a query-conditioned view; superseded facts are suppressed for current-state questions and eligible again for historical ones; a rate-distortion budget picks what to keep.
- ConsolidationBench policy (b19, d09): per cluster choose keep, summarise, extract skill, distil rule or forget, under a token budget. Adding hindsight-regret features raised forgetting precision to 0.93 but nearly switched the gate off (0.61 forgets per seed vs 30).
- SleepGate (b22, c09, d06): learned conflict tagger, forgetting gate that evicts or compresses stale KV entries, consolidation module, run in periodic sleep cycles. Toy model only.
- Sleep-time compute (b25, c03, c04, d13): between queries, the model reasons about the context and precomputes what a future query is likely to need.
- Memory-R1 (c16) and Mem0 (c19): ADD, UPDATE, DELETE, NOOP manager, prompted or RL-trained.
- Agent Workflow Memory (c18): keep only workflows induced from judged-correct runs.

## 5. What holds up

**Replicated and robust**
- Telling people an item matters raises memory for it (Wamsley F=7.35, p=.008; Barner relevance F=8.78, p=.005; Kurdziel remember beat emotion) (K03, K22). It happens in wake as well as sleep. It is an encoding or attention effect.
- Emotion is not preferentially kept by sleep (31-study meta-analysis) (K09).
- In LLM agents, hard forgetting at high load is risky (ZenBrain, ConsolidationBench) (K16).
- In-context "forget" instructions do not work on LLMs (K23).

**Failed or weak replications**
- Sleep x expectancy interaction. Wilhelm: p=0.05, with suspicious subjects dropped after the fact (10, 17 and 11 by cell; they looked like the expected group). Ashton and Cairney (N=162 and 124): BF01 2.5 to 4.0 for no interaction. Wamsley: no interaction. Reverberi: no effect. Barner: interaction p=.12. Rough pool r about 0.10, CI 0.01 to 0.18, with optimistic signs (K02, K21).
- Wake behaviour is inconsistent. Wilhelm: no change. Van Dongen: relevant items lost more (-5.0 vs -3.3). Wamsley: expectancy helped in wake (K05).
- Directed forgetting: Saletin positive; Scullin partial; Rauchs and Kurdziel null (K08).
- Reward: about half positive; Tucker null; Stamm reversed (K06).

**Moderators**
- Store load: 640 pairs gave no sleep effect and no harm (K12).
- Test difficulty: the weak-trace sleep benefit appears under easy tests (d03).
- Time: Barner's selective sleep effect appeared only at 1 week and only in a planned contrast.
- Design: one participant per night, small samples, winner's-curse inflation likely; the same paradigm gives contrasting results (Davidson; b26).
- Exclusion rules: positive studies drop subjects who doubted the instruction (Van Dongen 10 of 60; Ashton Exp 2 82 of 213 for expectancy mismatch).

**AI interventions that worked (author-reported)**
- Blind multi-factor value beat uniform, recency and single factors on LongMemEval-S, keeping 30 percent: 0.770+-0.011 vs 0.657 uniform, 0.368 recency, 0.286 goal-only, 0.300 random. Gaps +0.120 [0.091, 0.149] and +0.402 [0.350, 0.452]. With the future query visible, goal relevance reaches 0.979 (oracle). Retention is gold evidence kept, not answer accuracy (K13).
- History-based deletion, strict evaluator: EHRAgent 38.67 to 42.06, CIC-IoT 85.40 to 89.60, AgentDriver 51.00 to 51.81; hurt RegAgent 70.95 to 67.65 (memory 2938 to 949). Coarse evaluator: EHRAgent +7.6, CIC-IoT +4.1, AgentDriver -2.9, RegAgent -2.3. Rows were paired by memory size and the figures were not viewed (K14, d07).
- Selective add: a strict gate on what gets stored beats add-all, which piles up low-quality records and fades over time (c06).
- RD-Forget: removing FORGET cost 91.86 to 68.60, 93.59 to 60.26, 74.00 to 51.00; removing the rescue step cost 91.86 to 88.37, 93.59 to 91.03, 74.00 to 65.00 (d10).
- OBLIVION: LongMemEval-S, GPT-4.1-mini: single layer 86.40, M4 89.60, full 90.60, flat retrieval 89.00. Token cost down 68 percent at 32K and 73 percent at 120K.
- Soft forgetting: in ConsolidationBench, rollback to source experiences lifted success from 0.0 to 1.0 (5 of 5 seeds).

**Did not work, or cost something**
- At moderate load forgetting buys efficiency more than accuracy: ZenBrain NoDecay cost only P@5 0.002 (p=0.043, |d|=0.015). Under stress 9 of 15 ablations became critical, quality down up to 93.7 percent (c13, c14).
- Pruning a 27,021-node graph removed 9.8 percent of nodes with token F1 +0.001 (CI -0.015 to +0.016) and judged correctness -1.6 points (CI -3.8 to +0.6). Graph memory itself lost to flat vector search (0.417 vs 0.468) (c12).
- Learned forgetting policy: precision 0.319 vs junk base rate 0.333; 74 percent of load-bearing clusters destroyed at least once; transfer regression -15.0 pp, 75 percent traced to forget, re-promotion, poisoning (b19, d09).
- Prompted DELETE decisions fragment memory (Memory-R1, c16).
- ExpeL: insights taken only from the initial few-shot examples gave no gain over ReAct; adding reflections to insight extraction hurt (c17).
- OBLIVION at short spans used about 5x (isolated) and 2x (2K) the tokens of full context; with a strong backbone and large window full context stayed competitive (b21, d11).
- In humans, cue-based rescue during sleep did not selectively help relevant items (Barner).

## 6. Language models

No study tests the human claim directly: does an expected-future-use tag set after learning raise later retention or use in an LLM or agent (K20, K26)? What exists:

**Memory with forgetting or utility scores**
- MemoryBank 2023 (c01): 194 probing questions. ChatGPT retrieval accuracy 0.763 EN, 0.711 ZH; correctness 0.716 and 0.655. The forgetting curve was not ablated in the extracted text.
- Generative Agents 2023 (c02): TrueSkill full 29.89 vs no reflection 26.88 vs no reflection or planning 25.64 vs crowdworker 22.95 vs no memory, planning or reflection 21.21. Retrieval as a whole matters; forgetting is not isolated.
- FadeMem 2026 (c08, d12): own LTI-Bench, 30 days, critical facts 82.1 vs Mem0 78.4, MemGPT 75.6, LangChain 71.2, Fixed-16K 50.2, at 55 percent storage. LoCoMo multi-hop F1 29.43 vs Mem0 28.37, MemGPT 9.46. Ablation: no dual layer 19.45 (-33.9 percent); no fusion 13.63 (-53.7 percent).
- OBLIVION 2026 (b21, c15, d11): see section 5. Phi-4-mini at 120K: full context 1.15, memory 2.52, OBLIVION 3.37. Qwen3-30B-A3B at 120K: 4.25, 4.17, 5.30. GPT-4.1-mini: 6.29 to 8.41 at 2K and 6.05 to 6.79 at 32K over full context.
- SF-AMS 2026 (b24): LoCoMo, Qwen2.5-7B, multi-hop F1 37.59 (+9.65 over best baseline). Without strategic forgetting: single-hop 16.11 (full 26.70), multi-hop 18.78, open-domain 14.06 (full 32.76), temporal 15.16 (full 29.24). Author ablation.
- RD-Forget 2026 (c07, d10): three-suite means 66.59 (Qwen), 86.71 (Luna), 77.13 (MiniMax), 72.83 (Kimi). Fact-consolidation gains 11.00 to 26.00 points over the better of ACE and ReasoningBank. BEAM Qwen 50.21 vs ACE 32.84.
- Human-inspired architecture 2026 (c11): dedup consolidation 97.2 percent retention precision, 58 percent store reduction. LongMemEval M-tier 70.1 vs 71.2 percent raw retrieval (overlapping CIs). S-tier +13.3 points preference recall.
- SCM 2026 (b23, c10): eight author-built tests, 100 percent recall over ten turns, 90.9 percent noise reduction. Not strong evidence.
- FSFM 2026 (c21): access efficiency +8.49 percent, signal-to-noise +29.2 percent, 100 percent elimination of security risks (as stated by the authors).
- DREAM 2026 (c22): suppresses harmful memories; attack success cut by over 95 percent; 92.96 percent task success in poisoned multi-agent systems.
- ZenBrain 2026 (c13, c14): LongMemEval-500 reaches 91.3 percent of full-context oracle; routing +20.7 percent F1 on LoCoMo.
- Language Models Need Sleep 2026 (c20): distillation then RL "dreaming"; numbers not extracted.
- Mem0 (c19): 26 percent relative gain in LLM-as-judge over OpenAI memory; 91 percent lower p95 latency; over 90 percent token saving vs full context. Memory-R1 (c16): +28 percent F1 with GRPO from 152 training pairs. AWM (c18): +51.1 percent relative on WebArena; +24.6 percent step success on Mind2Web cross-task.
- Experience-following (Xiong; c05, c06, d07): agents copy the output of the most similar stored task. Two failure modes: error propagation and misaligned replay.

**What these show.** Several preprints show gains from pruning, but gains are small or zero at moderate load and the downside at high load is large. Soft forgetting (suppress, keep source) is the common safer design. No paper runs suppress versus delete head to head.

**Interference.** Wang and Sun 2025 (d05): an in-context "forget previous updates" instruction gave under 10 points at 100 updates, negative for gpt-4.1-mini, with errors clustered at the instruction. Only a fake Q&A reset helped, with declining benefit. SleepGate (d06): the full-cache baseline reaches only 8.0 percent even at one prior update. SleepGate scored 99.5 percent at depth 5, 97.0 at 10, 73.5 at 15, 16.5 at 30 (793K-parameter toy model, 200 episodes per depth, five baselines at or below 18 percent). Overhead 15.6 percent.

**Offline precomputation.** Sleep-time compute (b25, c03, c04, d13): about 5x less test-time compute for equal accuracy on Stateful GSM-Symbolic and Stateful AIME. Up to +13 percent and +18 percent with more sleep-time compute. Cost per query 2.5x lower at 10 queries per context. The gain grows with how predictable the question is (five quantiles; values only in a figure). On the real coding task SWE-Features the gain holds only at low test-time budgets. This is a compute-saving analogy, not a retention test.

**Cross-level transfer.** ConsolidationBench (b19, b20): oracle ceiling success 0.632, transfer 0.333. Mem0-style success 0.335, retention 0.531, transfer 0.000. SimpleMem-style 0.306, 0.485, 0.000. Fixed L2 0.303, 0.480, 0.233. Learned 0.368, 0.582, 0.167. No consolidation 0.003. Eight of ten policies scored zero transfer. Synthetic, single source.

**Proxy problem.** Relevance in LLM work is always a proxy. The strongest blind result (Chen and Cheng) fits weights to gold-evidence retention and gives goal relevance weight 0.00 when the future query is hidden. So without seeing the future, topic relevance did not help there. Whether that transfers to lessons is unknown.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA section 5.

### Add now (established)

1. **Do not rely on a sleep-style offline pass to select by expected relevance.** [E] as a negative. Memory. The human sleep-specific interaction is small or absent (K02, K21, K22; a01, b01, b05, d01, d02, d15).
2. **Use the relevance flag at write time to shape how the lesson is written, not as an offline selector.** [E] for the human attention effect, untested in LLMs, so add it as a field, not a rule. Memory (K03, K22; b05, a13, a17).
3. **Never delete lessons by default; demote and keep an archive with a rescue path.** [E] Memory, G7. Hard forgetting destroyed 74 percent of load-bearing clusters at least once at chance precision; ZenBrain had 9 of 15 ablations critical under stress (K16; b19, d09, c13, c14).
4. **Do not use emotion or salience tags as a retention signal.** [E] Memory. 31-study meta-analysis, no overall effect (K09; b13). Chen and Cheng's emotion weight 0.55 was fitted on gold-evidence retention in dialogue, not on agent lessons.
5. **Do not rely on a "drop this" note inside the same prompt.** [E] Memory, G10. Under 10 points, negative for one model (K23; d05, d06). To drop a lesson, remove it from context.
6. **Do not drop a lesson because it is weak.** [E] as caution. Memory. Weak and strong traces are both protected in the best controlled studies, and the weak advantage depends on test difficulty (K10; d03, d04). Combined with the SCHEMA trust rule (trusted only after it helps on two problems), keep weak lessons visible as "untrusted".
7. **Judge memory rules by answer accuracy at equal tokens and include a high-load condition.** [E] G7. Light-load tests make forgetting look free (K16; c14), and retention proxies are not use (d08).

### Test first

1. Write-time "expected reuse" field vs none (K01, K03). Memory. [C] sleep part, [E] attention part, LLM untested. a01, b05, a13.
2. LLM-rated future-use tag vs recency vs access count as predictors of real reuse (K20, K26). Memory. [S]. Most decision-relevant. c27, d16, d08.
3. Outcome-based value (did the lesson help later) vs LLM-rated value (K06, K07). Memory. [S]. a05, b11, c23.
4. Utility-gated deletion vs keep-all vs recency pruning at three store sizes (K14, K25). Memory. [C]. c05, c06, d07, d14.
5. Soft demotion with rescue vs hard deletion (K17, K24). Memory. [S]. c07, d09, d10, b21.
6. Blind multi-factor value vs uniform on our own lesson logs, held-out future tasks (K13). Memory. [S]. b17, b18, d08.
7. Idle-time pre-writing of reuse notes between tasks at equal total tokens (K18). O / memory. [S]. b25, c04, d13.
8. Explicit "forget" tags and interference (K08, K23). Memory. [C]. a08, b09, d05.
9. Write-time features (surprise, effort) as predictors of later use (K11, K26). Memory. [S]. a18, d17.
10. Abstraction level of stored lessons (K19). Memory. [S]. b20.

## 8. Concrete tests on our bench

All arms get the same total token budget, including offline or between-task calls. Report accuracy with a bootstrap CI over items. A gain counts only if it clears the CI (G7). Run on at least two models and report per model; Xiong showed sign flips by agent and evaluator.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Reuse tag | Task stream with repeated problem classes; lesson written after each task | A: lesson with a "needed for class X when Y" field. B: untagged. Same store size | Later reuse accuracy on new items of the same class | Small positive, about 0 to +3 pp. Human effect is a main effect, not sleep-specific |
| T2 Tag predicts reuse | Log per lesson: LLM future-use rating, recency, access count, surprise (failed first attempt), effort (tokens) | Fit a simple model for "used and helped later" | AUC per predictor | Recency and access count likely beat the rating; rating wins only if it adds 0.05 AUC |
| T3 Keep-by-value | Store caps 50, 200, 1000 lessons; held-out future stream | keep-all (truncate), recency, random, utility-gated (Xiong rule), blind multi-factor | End-task accuracy | Tie at small store, possible gain at medium (judge-dependent), possible loss at high load |
| T4 Outcome vs LLM tag | Same stream | Value from observed later success vs from LLM rating at write time | End-task accuracy; share of needed lessons kept | Outcome should win; it arrives later |
| T5 Soft vs hard | Stream where some dropped lessons become needed again | Hard delete vs demote to archive with rescue on retrieval miss | Loss rate of needed lessons; accuracy; tokens | Soft saves needed lessons at some extra tokens |
| T6 Drop instruction | Interference set: updated rules for the same class | In-prompt "ignore old lesson" vs lesson removed vs task-boundary reset | Accuracy on current rule | Removal beats the note; note near zero |
| T7 Idle precompute | Between-task windows | Pre-write likely-reuse notes vs same tokens as extra test-time samples | Accuracy by predictability of next task | Gain only on predictable tasks; null possible |
| T8 Weak-lesson keep | Lessons with low confidence | Keep-strong only vs keep-weak-relevant vs keep-all | End-task accuracy | Keep-weak-relevant at least ties |
| T9 Stress | T3 with fast decay | Moderate vs stress decay | Count of rules that become critical | Replicates ZenBrain if real |

## 9. What does not transfer, and why

- **Sleep itself.** The sleep mechanism (slow-oscillation and spindle coupling, REM erasing) has no LLM counterpart. The replicated part (a relevance flag helps encoding) does not need sleep.
- **A wake baseline.** Studies disagree on what wake does to relevant items (K05). Do not treat an arm without consolidation as neutral.
- **Item counts.** Human studies use 40 to 640 word pairs or picture locations. Lesson stores hold different content. The 640-pair boundary is a weak guide.
- **Passive vs chosen forgetting.** Human erasure has no archive. An agent can keep a perfect archive and change only the view. Soft forgetting is possible for us and is safer.
- **Instruction after learning.** In humans, "a test is coming" changes motivation. In an LLM a message acts on the next call only; it does not change a stored trace.
- **Emotion and reward.** Emotion: null in a meta-analysis. Reward: about half positive. For an agent the analogue of reward is outcome, which exists only after use.
- **Theta tag.** No analogue measured. Surprise and effort are candidates, untested (d17).
- **Chen and Cheng weights.** Fitted to gold-evidence retention in chat logs, where the future question is hidden. Our lessons are matched by class at use time. Do not copy the weights.
- **Toy models.** SleepGate (793K parameters) says little about frontier models.
- **Compute-saving analogy.** Sleep-time compute lowers cost. It does not show that expected-use tagging beats other retention rules.

## 10. Open questions

1. Is there a real pooled effect for expectancy x sleep? A meta-analysis with unpublished nulls and Barner 2023 is missing (K21).
2. Does an LLM-rated or outcome-based future-use tag at write time predict later reuse better than recency or access count?
3. At equal tokens, does keeping lessons by expected use beat keep-all, recency and uniform pruning, and at what store size does pruning pay (K25)?
4. Soft vs hard forgetting: what is the loss rate of needed lessons in long runs?
5. Does the instruction effect depend on encoding strength?
6. Which write-time signals predict reuse?
7. How much of the sleep-time compute gain survives when the future query is uncertain (K18)?
8. Are the 2026 forgetting gains (FadeMem, OBLIVION, SF-AMS, RD-Forget) reproducible by third parties on answer accuracy?
9. Xiong 2025 Table 2: rows paired by memory size; Figure 5 not viewed.
10. Do "drop" tags help when the dropped item is physically removed from context?
11. The gap search ran without web search quota; a fresh sweep of 2026 agent papers was not possible.

## 11. Sources

[V] = opened this session. [M] = snippet or abstract only.

- [V] Wilhelm et al. 2011, Sleep selectively enhances memory expected to be of future relevance. https://pmc.ncbi.nlm.nih.gov/articles/PMC6623736/
- [V] Feld and Born 2020 (online 2019), Neurochemical mechanisms for memory processing during sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC6879745/
- [V] Saletin, Goldstein and Walker 2011, Sleep in directed forgetting and remembering. https://pmc.ncbi.nlm.nih.gov/articles/PMC3183424/
- [V] Oudiette, Antony, Creery and Paller 2013, Memory reactivation during wakefulness and sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC3677604/
- [V] Van Dongen et al. 2012, Sleep supports selective retention based on relevance. https://pmc.ncbi.nlm.nih.gov/articles/PMC3420871/
- [V] Barner et al. 2023, sleep and targeted memory reactivation on relevant memories. https://pmc.ncbi.nlm.nih.gov/articles/PMC12713986/
- [V] Davidson and Pace-Schott 2021, Does sleep selectively strengthen certain memories over others? https://pmc.ncbi.nlm.nih.gov/articles/PMC8318217/
- [V] Kurdziel et al. 2025, Top-down instruction outweighs emotional salience. https://pmc.ncbi.nlm.nih.gov/articles/PMC12537657/
- [V] Theta oscillations tag episodic memories for sleep-dependent consolidation, PLOS Biology 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC13521381/
- [M] Fischer and Born 2009, Anticipated reward enhances offline learning during sleep. https://doi.org/10.1037/a0017256
- [V] Stickgold and Walker 2013, Sleep-dependent memory triage. https://pmc.ncbi.nlm.nih.gov/articles/PMC5826623/
- [M] Rouast and Schoenauer 2023, Continuously changing memories. https://doi.org/10.1016/j.tins.2022.10.013
- [M] Lewis and Durrant 2011, Overlapping memory replay builds cognitive schemata. https://doi.org/10.1016/j.tics.2011.06.004
- [M] Tononi and Cirelli 2014, Sleep and the price of plasticity. https://doi.org/10.1016/j.neuron.2013.12.025
- [M] Diekelmann and Born 2010, The memory function of sleep. https://doi.org/10.1038/nrn2762
- [M] Brokaw et al. 2016, Resting state EEG correlates of memory consolidation. https://doi.org/10.1016/j.nlm.2016.01.008
- [V] Antony and Schechtman 2023, Reap while you sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC10429120/
- [V] Reverberi et al. 2020 (via review tables). https://europepmc.org/article/PMC/PMC8318217
- [V] Wamsley et al. 2016, Test expectation enhances memory consolidation across sleep and wake. https://pmc.ncbi.nlm.nih.gov/articles/PMC5070851/
- [V] Stamm et al. 2014, Negative reinforcement impairs overnight memory consolidation. https://europepmc.org/article/PMC/PMC4201816
- [V] Lipinska et al. 2019, Preferential consolidation of emotional memory: meta-analysis. https://europepmc.org/article/PMC/PMC6524658
- [V] Huelin Gorriz, Takigawa and Bendor 2023, experience and hippocampal replay. https://europepmc.org/article/PMC/PMC10710481
- [V] Kolibius, Born and Feld 2021, Vast amounts of encoded items nullify but do not reverse the effect of sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC7821853/
- [V] Ashton and Cairney 2021, Future-relevant memories are not selectively strengthened during sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC8568116/
- [V] Petzka et al. 2021, Does sleep-dependent consolidation favour weak memories? https://pmc.ncbi.nlm.nih.gov/articles/PMC7805594/
- [M] Schabus, Ameen and Heib 2025/26, Sleep preserves, wake differentiates (Europe PMC record 42165620). https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42165620&resultType=core&format=json
- [M] Hu, Cheng, Chiu and Paller 2020, TMR meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC7144680/
- [V] Zhong et al. 2023, MemoryBank. https://arxiv.org/abs/2305.10250
- [V] Park et al. 2023, Generative Agents. https://arxiv.org/abs/2304.03442
- [V] Lin et al. 2025, Sleep-time Compute. https://arxiv.org/abs/2504.13171
- [V] Xiong et al. 2025, How Memory Management Impacts LLM Agents. https://arxiv.org/abs/2505.16067
- [V] Wang and Sun 2025, Unable to Forget. https://arxiv.org/abs/2506.08184
- [V] Chen and Cheng 2026, Learning What to Remember. https://arxiv.org/abs/2606.12945
- [V] Annapureddy and Thamatani 2026, Epistemics of Agent Memory (ConsolidationBench). https://arxiv.org/abs/2609.33013
- [V] Rana et al. 2026, OBLIVION. https://arxiv.org/abs/2604.00131
- [V] Xie 2026, SleepGate. https://arxiv.org/abs/2603.14517
- [V] Shinde 2026, SCM. https://arxiv.org/abs/2604.20943
- [V] Yang et al. 2026, SF-AMS. https://arxiv.org/abs/2607.22562
- [V] Li and Li 2026, RD-Forget. https://arxiv.org/abs/2609.10263
- [V] Wei et al. 2026, FadeMem. https://arxiv.org/abs/2601.18642
- [V] Kerestecioglu et al. 2026, Human-Inspired Memory Architecture. https://arxiv.org/abs/2605.08538
- [V] Rusu et al. 2026, Selective Forgetting: graph-based memory. https://arxiv.org/abs/2608.28978
- [V] Bering 2026, ZenBrain. https://arxiv.org/abs/2604.23878
- [V] Yan et al. 2026, Memory-R1. https://arxiv.org/abs/2508.19828
- [V] Zhao et al. 2024, ExpeL. https://arxiv.org/abs/2308.10144
- [V] Wang et al. 2024, Agent Workflow Memory. https://arxiv.org/abs/2409.07429
- [V] Chhikara et al. 2025, Mem0. https://arxiv.org/abs/2504.19413
- [V] Behrouz et al. 2026, Language Models Need Sleep. https://arxiv.org/abs/2606.03979
- [V] Gu et al. 2026, FSFM. https://arxiv.org/abs/2604.20300
- [V] Liu et al. 2026, DREAM. https://arxiv.org/abs/2610.13267
