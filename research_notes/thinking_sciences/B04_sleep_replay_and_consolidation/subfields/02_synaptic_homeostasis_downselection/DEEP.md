# Synaptic homeostasis / downselection: deep document

*Subfield B04.02. Source files in this folder: evidence_a-d.jsonl (ids a01-a28, b01-b32, c01-c25, d01-d18), claims.jsonl (K01-K31), critique.md. Status tags: [E] established, [S] single-source, [C] contested. Schema parts: G = guardrail, S = state, O = operator, memory = SCHEMA.md section 5.*

## 1. What it is

The synaptic homeostasis hypothesis (SHY) says sleep is the price the brain pays for plasticity. During wake the brain learns mostly by making synapses stronger. Strong synapses cost energy, add noise, and use up room for new learning. Sleep brings total synaptic strength back down. It does this by activity-dependent down-selection: synapses that carry strong, repeated signal are spared or shrink little; weak or noisy ones shrink more. Signal-to-noise goes up and the brain can learn again the next day (a01).

Three core claims (a01): (i) learning in wake is mainly potentiation; (ii) there is little potentiation in sleep; (iii) sleep renormalises strength. The balance is claimed over the 24 h cycle, not at every moment. SHY does not rule out some depression in wake or some potentiation in sleep.

Why this matters for our agent. A lesson store that only grows is the same as a brain that only potentiates. The question for the schema is narrow: **should the lesson store get a scheduled, whole-store prune pass, and by what rule?** The neuroscience gives a design idea and a warning about when it fails. It does not give a number for an LLM. The LLM-agent literature gives numbers, but mostly from papers that are not sleep-branded (Xiong 2025, ACE, Dynamic Cheatsheet).

Out of scope here: replay and reactivation (other B04 subfields), incubation by "sleeping on it" (SCHEMA 4b already says it failed to replicate).

## 2. History and theories in depth

**2003 to 2006. The hypothesis.** Tononi and Cirelli proposed SHY in 2003 (Brain Res Bull) and 2006 (Sleep Med Rev). The 2003 paper was never opened here (a25); we rely on the 2014 review (a01). Starting evidence: slow-wave activity (SWA, 0.5-4.5 Hz) rises with time awake and decays in sleep. SWA is read as a marker of synaptic strength and sleep need (a06).

**2008. First molecular evidence.** Vyazovskiy 2008, rat cortex: GluA1-containing AMPA receptors 30-40% higher after wake than after sleep (a03, second-hand through the review; a24 not opened).

**2009 to 2013. Models.** Hill 2008, Olcese 2010, Nere 2013 built network models. Three rules: proportional downscaling with a floor; STDP-like rule where strong synapses depress less; protection from depression for synapses that fire together in sleep (a07). All give competitive down-selection and higher signal-to-noise. Nere 2013 (a10, a11, a12, a13) shows the same rules raise recall in toy networks.

**2011. Flies.** Bushey, Tononi, Cirelli 2011 (b03): synapse size and number rise after wake and fall only if the fly sleeps. Richer waking experience gave more growth and more sleep need.

**2012. Critique and reply.** Frank 2012 (b05, abstract only) argued that the cell mechanism is unclear and that temperature and glucocorticoids are alternative causes. Tononi and Cirelli replied (b04) that SHY is about function, not one mechanism, and that SWA is a good sensor. Critique note: this narrowing makes the theory harder to falsify (K22).

**2012. Contradicting cats.** Chauvette 2012: in head-restrained cats, evoked responses rose after sleep. Review authors call this sleep inertia (a05).

**2014. The review.** Tononi and Cirelli (a01, a02). Key conceptual move: why renormalise in sleep and not in wake? Wake input is a narrow, biased sample. Sleep spontaneous activity samples the whole store, so depression can be fair to old memories. Their example: weakening unused synapses during a day with a new acquaintance would keep the new person and lose old friends. This argument was never directly tested (K20).

**2014 to 2020. Rival results: sleep also adds.** Yang 2014 (b07): new spines form on specific branches after learning. Aton 2014 (b06, abstract only): V1 response potentiation after patterned experience needs sleep. Li 2017 (a19): REM prunes and also maintains new spines. Zhou 2020 (b08, abstract only): REM drives experience-specific spine elimination. These do not refute net renormalisation. They rule out "sleep only deletes" (K03).

**2016 to 2017. Structure and molecules.** de Vivo 2017 (a14, b01): serial-section EM in adolescent mouse cortex, synapses about 18% smaller after sleep. Diering 2017 (a17, b02): Homer1a drives scaling-down of synaptic AMPA receptors in sleep. Kuhn 2016 (b19): human TMS and plasticity data are consistent.

**2016. Firing-rate homeostasis.** Hengen 2016 (b10, abstract only) said firing-rate recovery needs wake. Watson 2016 (b12) found NREM homogenises rates. Torrado Pacheco 2021 (b09) found downward return happens in sleep. See section 5.

**2021 to 2022. Independent null and review.** Cary and Turrigiano 2021 (a18, b13): in juvenile rats, mEPSC amplitudes were stable across sleep and wake. Cirelli and Tononi 2022 (b21) reviewed the field and restated the position.

**2019 to 2026. Machine learning and LLM spin-offs.** Bazhenov group (c01-c05, c25): sleep-like phase in networks. Robinson 2022 (b24), Massey 2026 (b25, b26): dose-response. Then LLM memory work, 2025-2026: Xiong 2025 (d01-d05), ACE (c13, d06-d09), Dynamic Cheatsheet (c14, d10, d11), and sleep-branded papers SCM, SleepGate, ZenBrain, RSPM, FadeMem (b27-b32, d13-d16). The honest picture: the unbranded papers give the most usable evidence.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Adolescent mouse cortex synapses are smaller after sleep | Axon-spine interface (ASI) -18.9% vs spontaneous wake (p=0.001); -17.5% vs enforced wake (p=0.003); sleep vs enforced wake -1.7% (p=0.957); 6,920 synapses, 12 mice, one layer | de Vivo 2017 (a14, b01) | [E] for this population, one lab |
| Same effect in 2-week-old pups | ASI 33.9% smaller after sleep vs extended wake; two strains | de Vivo 2019 (b14) | [E], same lab |
| Which synapses shrink: small and medium shrink, largest spared | small/medium -11.9%, large +0.7%; about 80% of synapses scaled down | de Vivo 2017 (a15) | [C] |
| Local crowding matters | sparse dendrites -36.4% (sleep vs enforced wake -25.3%) vs dense +7.8% (-8.2%); interaction p=0.038; spine density unchanged p=0.761 | de Vivo 2017 (a16) | [S], modest p |
| Molecular scaling-down in sleep | over 4,500 PSD proteins, close to 10,000 phosphopeptides, about 20% regulated; Homer1a drives AMPAR removal | Diering 2017 (a17, b02) | [E] |
| AMPA receptors higher after wake | GluA1 30-40% higher after wake than sleep (rat) | Vyazovskiy 2008 via review (a03, a24) | [E] second-hand |
| Human indirect markers | Sleep deprivation, N=20 within-subject: Condition F(1,19)=7.5, p=0.013, partial eta2 0.283; Condition x Time F(3,57)=3.5, p=0.021, eta2 0.156. Frontal TMS slope rises over 18 h wake, returns after sleep | Kuhn 2016 (b19); Huber 2012 via review (a03) | [E], indirect |
| Juvenile rat cortex: no sleep/wake change | mEPSC stable in V1 and PFC; n=30 animals, P25-P31; authors note sleep at that age is fragmented with weak SWA homeostasis | Cary and Turrigiano 2021 (a18, b13) | [C] |
| Cat evoked responses rise after sleep | effect after 10 min of sleep, saturating after two short episodes | Chauvette 2012 via review (a05) | [C] |
| Flies: wake grows synapses, sleep shrinks them | VS1 spines rise after sleep deprivation, mostly stubby (mushroom p=0.29); Fmr1 overexpressors slept 9.6% less, recovered 39% vs 49% of lost sleep | Bushey 2011 (b03) | [E] |
| Firing-rate set point returns in sleep | +114% +/- 23% on ER2, +2% +/- 13% on ER4, controls 10% +/- 18%; 30 of 36 neurons (83.3%) | Torrado Pacheco 2021 (b09) | [C] vs Hengen 2016 |
| Sleep adds synapses on specific branches | new-spine formation 15.3 +/- 1.3% vs 6.4 +/- 0.8% and 4.4 +/- 0.9% untrained, p<0.0001; about 30% of branches respond | Yang 2014 (b07) | [E] |
| Active units protected | indirect units -32% task peak firing after sleep, direct units +7%; blocking ON/UP states stopped both | Gulati 2017 (a22) | [E] |
| UP states depress by default, paired synapses protected | mean depression 63-71% unprotected | Gonzalez-Rueda 2018 (a23, b18; abstract) | [S] |
| Model: procedural recall | 80% (S/N 4) to 90% (S/N 9) after sleep; 95% and S/N 19 later; extra wake or sleep potentiation drops recall to 20-25%, S/N 0 | Nere 2013 (a10, a13, a08) | [E] model |
| Model: declarative recall dips then recovers | 87% (S/N 6) to 75% (S/N 2) after one sleep; awake 53% (S/N 1); 94% (S/N 15) after 10 cycles; cued 95% vs non-cued 75% | Nere 2013 (a11) | [E] model |
| Model: gist protected, detail depressed | integrated memory depressed about 2%; misfit memory levels 1-2 28%, levels 2-3 11%; unrelated inactive old memories about 90% (artifact of equal rates) | Nere 2013 (a12) | [E] model |
| Sleep-like phase in networks | two-task: no sleep 5% / 95%; with sleep 63.2% / 45.4% (CUB-200). CIFAR-10 44% vs 19%. Incremental MNIST: sequential 19.49, EWC 20.37, SI 21.38, sleep (SRC) 48.47 +/- 5.03, OWM 77.04, rehearsal 0.75% 79.91, rehearsal+SRC 86.47 | Tadros 2022 (c01, c02, a26) | [E] |
| Sleep helps most with small buffers | iCaRL K=100: 65.5 to 78.1 with SRC | Tadros 2022 (c03) | [E] |
| Wake output layer only, sleep rest | ImageNet-1K top-5: offline 83.31, ER 63.92, REMIND 74.31, SIESTA 83.59; 1.9 h on one GPU | Harun and Kanan 2023 (c07) | [E] |
| Wake-sleep consolidated learning | CIFAR-10 buffer 200: ER 48.76 to 51.86; DER++ 57.35 to 63.97 | Sorrenti 2024 (c08) | [S] |
| Downscaling needs replay; inverted U in prune fraction | CIFAR-100 class-incremental, p = 0, .25, .5, .75, .9: best at p=0.75; p<=0.5 looked like 0; without replay collapse at every p | Robinson 2022 (b24) | [E] |
| Optimal sleep dose is small | STDP-SNN best at 10-20% sleep, 11 levels, 5 seeds, 4 datasets; gradient-trained SNN best at 0% | Massey 2026 (b25, b26) | [E] |
| Add-all memory is worse than a tiny fixed store | RegAgent 55.48 (4,100 records) vs 67.53 (100); AgentDriver 32.32 vs 40.11; CIC-IoT 59.90 vs 71.50 | Xiong 2025 (d01) | [E] |
| Utility-based deletion beats add-only | history-based: EHRAgent 38.5-38.7 to 42.06 (1,012 to 784 records); CIC-IoT 85.40 to 89.60 (904 to 788); AgentDriver 51.00 to 51.81 (1,178 to 846); combined deletion 188-323 records at 42.34 / 49.97 / 85.50 | Xiong 2025 (c11, d02, d03) | [E], one paper |
| Outcome-linked beats frequency deletion | history vs periodic: RegAgent 69.80 vs 67.65; EHRAgent 42.06 vs 38.59; AgentDriver 51.81 vs 50.94; CIC-IoT 89.60 vs 80.80 | Xiong 2025 (d02, d03) | [S] |
| Periodic deletion is not free | RegAgent 70.95 (2,938 records) to 67.65 (949): 68% fewer records, -3.3 points | Xiong 2025 (c12) | [S] |
| Full-history append can be below no memory | GPT-4o AIME 2024: baseline 20.0, full-history 6.7, curated DC-RS 40.0 | Suzgun 2025 (d10) | [E] |
| Whole-store rewrite collapses | ACE AppWorld: context 18,282 tokens to 122 tokens in one step; accuracy 66.7 to 57.1 (no-adaptation baseline 63.7). Ablation: rewrite-style 56.9 avg vs incremental 70.3 (ReAct 53.3) | Zhang 2026 ACE (c13, d06, d07) | [S] |
| Weak evaluators remove the gain | coarse evaluator harmful; judge fine-tuned on 300 labelled outcomes: AgentDriver 36.92 to 47.37 (add-all 32.32) | Xiong 2025 (d04) | [S] |
| ACE tolerance to bad updates | one bad update in five: 76.1 (base 70.7); all bad: 66.7, minus 4.0 | ACE (d08, d09) | [S] |
| Prune trigger size is a weak knob | FiNER, base 70.7: 10K / 50K / 100K tokens gave 78.6 / 78.4 / 78.3; dedup 50 / 70 / 90% gave 77.0 / 73.9 / 78.6; 10 reflection rounds 65.2 vs 5 rounds 67.6 | ACE (d07, d08) | [S] |
| Failure-triggered pruning can backfire | LoCoMo conversation, 35% error rate: 21 sleep cycles, 43% of store pruned, 19.5 points below baseline | RSPM (d13) | [S] |
| RSPM headline | solve rate 40.0% to 49.1% (+9.1, p=0.0003, simulated SWE-bench arm); 30.6% fewer entries; temporal consistency 92.5% vs RAG 80.6%; LLM conflict detector 92.5%, keyword 79.5% | Chauhan 2026 (b28, d14) | [S] simulation |
| Gist compression loses dates | temporal-expression preservation 3.05% to 62.39% with one prompt sentence; entities x1.02, x1.11; temporal accuracy +0.314 [0.254, 0.375]; 1,935 questions, 10 conversations | Kyrkewood 2026 (b31) | [S] |
| Toy supersession gate | 99.5% depth 5, 97.0% depth 10, 73.5% depth 15, 16.5% depth 30; baselines under 18%; decay-only 7.5% at depth 10; H2O 7.5% at 2 prior updates | SleepGate (b29, d16) | [S] toy |
| SCM toy suite | noise removed 50/55 (90.9%); 22/22 facts kept with 24 concepts vs 72 no-forget; FIFO 8/22 | Shinde 2026 (b27) | [S] toy |
| Mem0 | over 90% fewer tokens at near full-context accuracy | Chhikara 2025 (c17) | [S] |
| FadeMem | 45% less storage, about 1 F1 point over Mem0; removing fusion 29.43 to 13.63 multi-hop F1 (authors' chart) | Wei 2026 (b30, d15) | [S] |
| Sleep-time compute | about 5x less test-time compute at equal accuracy; up to +13% / +18%; 2.5x lower cost per query at 10 queries per context | Lin 2025 (c18, c19) | [S], replay side |
| Reflexion window | keeps last 1-3 reflections, FIFO, not ablated | Shinn 2023 (d18) | [S] |
| ExpeL vote and remove | HotpotQA insights-only 36% vs retrieve-only 31%; ALFWorld 50 vs 55; removal-at-zero rule not ablated | Zhao 2024 (c16, d12) | [S] |
| AWM offline vs online | Mind2Web step SR cross-task 45.1 vs 43.6; cross-domain 32.6 vs 35.5; MindAct 36.2 / 30.1 / 18.6 | Wang 2024 (d17) | [S], add-only |

## 4. Mechanisms and models

### 4.1 Biology in plain terms

- **Wake raises strength.** Learning uses potentiation. Neurons fire more, receptors move into synapses, spines grow. Total strength rises. Cost: energy (brain uses up to 25% of body glucose at 2% of body mass, a01), noise, saturation.
- **Slow-wave activity is both sensor and effector** (a06). Stronger synapses give more synchrony, which gives more SWA. SWA drives depression. Depression lowers synchrony, so SWA falls. Rate of depression is proportional to firing and synchrony, so SWA decays exponentially and the process stops itself (Olcese 2010). Suppressing SWA early in sleep prevents its decline (Dijk 1987).
- **Molecular route** (b02): Homer1a is induced in wake by activity and drives AMPA receptor removal at synapses during sleep. About 20% of the postsynaptic proteome shifts.
- **Local crowding** (a16): sparse dendrites scale down more than dense ones.
- **Protection** (a07, a22, a23): synapses on neurons that fire in sleep, especially those reactivated or paired pre-post, are spared. The default for the rest is depression.
- **Competition needs several sources** (a07): a neuron with all inputs from one source cannot compete, so down-selection cannot rank anything.

### 4.2 Three model rules (a07)

1. Proportional downscaling with a floor: every weight w becomes max(floor, a*w) with a<1. Cheap, ranks nothing, keeps order.
2. STDP-like depression where strong synapses lose less. Ranks by strength.
3. Protection from depression: synapses whose pre and post fired together in the offline phase are spared. Ranks by reuse.

Outcome in models (a10-a13): signal-to-noise rises, gist (high-level invariant links) survives, detail (low-level links) is depressed, misfitting new memories are depressed more, unrelated old memories fade if rates are equal.

### 4.3 Engineering recipe: whole-store prune pass for a lesson store

This is the implementable analogue, assembled from the evidence. Each step names its support.

```
WAKE (during tasks): only ADD lessons (one line each); log use + outcome per lesson.
SLEEP (offline pass, every N episodes, over the WHOLE store):
  1. Score each lesson by outcome-linked utility:
       u = (successes when lesson was in context) - (failures)   [per-item counters]
       protect if retrieved AND used in a passing step           [protection from depression]
  2. Cap: prune at most f of the store per cycle (start f = 10-30%).   [inverted U]
  3. Do not demote on failures of a task class that is simply hard;
     demote only if it failed where other runs succeeded.             [RSPM backfire]
  4. Supersession: if a newer lesson contradicts an older one, drop the older.  [SleepGate]
  5. Edit per item (ADD / EDIT / UPVOTE / DOWNVOTE / DELETE). Never rewrite the whole file.  [ACE collapse]
  6. If merging lessons into a rule, keep conditions (when, version, input range).  [Kyrkewood]
  7. Keep a retrieval path for survivors (prune alone does not protect old knowledge).  [Robinson, Golden]
```

Support: step 1 from Xiong (d02, d03) and Nere/Gulati (a07, a22); step 2 from Robinson (b24), Massey (b25); step 3 from RSPM (d13); step 4 from SleepGate (d16); step 5 from ACE (d06, d07); step 6 from Kyrkewood (b31); step 7 from b24, c04, c05.

Signal handling: the utility signal must come from verified outcomes (code check, held-out test). With weak self-judging, deletion helps nothing and errors spread through the store (d04, d08, d10).

## 5. What holds up

**Replications and agreement.**
- Smaller synapses after sleep: de Vivo 2017 (adolescent mouse, EM), de Vivo 2019 (pups), Diering 2017 (molecular), Bushey 2011 (flies), Kuhn 2016 (human, indirect). Different species and methods point the same way. But three of these are from the Tononi/Cirelli lab. Independent labs: Diering (supportive), Kuhn (supportive), Cary and Turrigiano (null), Torrado Pacheco (supportive on rates).
- Model support: Nere 2013 plus the Bazhenov group plus Capone 2019 (b23), where sleep-like slow oscillations help classification in toy networks.

**Failures and contradictions.**
- Cary and Turrigiano 2021: no mEPSC change in juvenile rat V1 and PFC (a18). Boundary: sleep at that age is fragmented, with weak SWA homeostasis (authors' own caveat).
- Cats: evoked responses rise after sleep (Chauvette 2012, a05).
- Adult mice: no sleep/wake spine change (a04). The structural effect is age dependent.
- Hippocampus: Spano 2019 (larger ASI after wake, b15, abstract) vs Havekes 2016 (fewer spines after sleep deprivation, b16, abstract). Spine number and synapse size are different variables.
- Which synapses: de Vivo says protect the largest; Diering as summarised by the 2020 review says large spines shrank most. The disagreement rests on second-hand reading.
- Firing rate: Hengen 2016 (recovery in wake) vs Torrado Pacheco 2021 (return in sleep). Torrado Pacheco reconciles them: upward in wake, downward in sleep. Watson 2016: homogenising, not uniform lowering.
- Inhibition rises in the sleep phase (Bridi 2020, b17): not only excitatory weakening.
- Sleep adds as well (b06, b07, a19, b08).
- Design weaknesses (critique.md): de Vivo 2017 has 12 mice, one layer, a snapshot design, and no tagging of individual synapses through a learning episode. No study ties downscaling to a specific learned content (a28).

**Moderators.** Age (adolescent yes, juvenile rat null, adult mouse no spine change), species, brain region, readout (mEPSC vs ASI vs spine count), local synapse density (a16), reactivation or pairing (protected).

**Interventions that worked.**
- Cueing during sleep saves cued items in the model: 95% vs 75% (a11).
- Slow-oscillation stimulation in a nap improved encoding in humans (Antonenko 2013, a09).
- A sleep phase in networks recovers old tasks (Tadros).
- Rehearsal plus sleep is best (86.47 vs 79.91 vs 48.47).

**Interventions that did not work or hurt.**
- Extra potentiation in wake or in sleep lowers S/N and recall in models (a08).
- Downscaling without replay: collapse at every p (b24). Freezing 1% of task-1 weights lets task 2 be learned but does not keep task 1 (a27).
- SRC alone loses to OWM and to rehearsal on incremental MNIST (c02).
- Too much sleep or pruning: inverted U (b24-b26). In gradient-trained SNNs the best sleep was 0% (b25).
- LLM memory: wholesale rewrite (d06), weak evaluator (d04), failure-triggered pruning on a hard task (d13), gist compression dropping dates (b31), toy gate failing past about 15 near-duplicates (b29).

**Independence.** The critique counts repeated readings of the same paper once (de Vivo 2017, Cary 2021, Tadros 2022). On the LLM side no sleep-branded paper has an independent replication (K18, K31).

## 6. Language models

No study in this folder tests SHY in a language model's weights. What exists is (a) sleep-like phases in small non-language networks, and (b) LLM-agent memory management that deletes, decays or merges. Everything below is by analogy.

**6.1 Non-language networks (not LLMs).** See section 3 rows for Tadros, Harun and Kanan, Sorrenti, Robinson, Massey. Take-away: sleep-like downscaling is a partial fix, beaten by a small rehearsal buffer, best combined, and needs a replay path. The best dose is small (10-20% sleep; p=0.75 of weights zeroed in one setup). With gradient-trained networks the benefit can vanish (b25).

**6.2 LLM agent memory on real benchmarks (the strongest evidence).**
- Xiong 2025 (d01-d05): four agents (EHRAgent, RegAgent, AgentDriver, CIC-IoT). Add-all can be worse than a fixed 100-record store. Utility-based deletion keeps or raises accuracy at 66-79% fewer records. Under a hard cap equal to the starting store it still beat the fixed store. History-based deletion beat an error-free memory on AgentDriver. This was with a strict, ground-truth-like evaluator. With weak evaluators the gain disappears and errors propagate ("experience following"). A judge tuned on 300 labelled outcomes fixed it: 36.92 to 47.37.
- ACE (c13, d06-d09): incremental delta edits with counters and dedupe: average 70.3 vs 56.9 for rewrite-style. Context collapse case: 18,282 to 122 tokens, 66.7 to 57.1. Gains survived one corrupted update in five, not all.
- Dynamic Cheatsheet (c14, d10, d11): curated memory beats full-history append; full-history can be below no memory. Small models fill memory with wrong strategies.
- ExpeL (c16, d12): vote and remove at 0, but the removal rule is not ablated.
- Mem0 (c17): ADD/UPDATE/DELETE/NOOP, over 90% fewer tokens at near full-context accuracy.
- Reflexion (d18), Generative Agents (c09), MemoryBank (c10): decay or FIFO caps are used; none ablated alone.
- AWM (d17): add-only; offline vs online similar in-domain.

**6.3 Sleep-branded LLM memory papers (self-benchmarked, single group).**
- RSPM (b28, d13, d14): +9.1 points, 30.6% fewer entries, but the SWE-bench arm is simulated. A 35% error-rate conversation drove 21 cycles, pruned 43%, and ended 19.5 points below baseline.
- SCM (b27): 22 facts, 50 noise items.
- SleepGate (b29, d16): 793K-parameter transformer on synthetic tokens.
- ZenBrain (b32): simulated corpora; headline 37% stability, 47.4% storage cut.
- FadeMem (b30, d15): 45% less storage; margin over Mem0 about 1 F1; judge-model scores.
- Kyrkewood (b31): gist summaries beat truncation on multi-hop but lose dates; one prompt sentence took temporal preservation from 3.05% to 62.39%.

**6.4 Replay side.** Sleep-time compute (c18, c19): work before the question cut test-time compute about 5x at equal accuracy; the gain tracks how predictable the query is; plain test-time compute wins at high budgets; 5 parallel sleep generations beat 10.

**6.5 What changed outcomes.** A verified utility signal (largest effect). Per-item edits instead of rewriting (about 13 points in ACE). A keep-dates instruction (3% to 62% date preservation). An LLM conflict detector over a keyword one (92.5% vs 79.5%). An outcome-linked rule over a frequency rule (up to 8.8 points on CIC-IoT). What did not change outcomes: prune trigger size from 10K to 100K tokens (78.6 vs 78.3).

## 7. What our agent should take

SCHEMA section 5 today: lessons are one line each, shown after the first attempt, trusted only after helping on two different problems [S]. Nothing prunes them yet. G7 requires every element to win at equal tokens.

### Add now (established)

Few items qualify. These are guards rather than new machinery.

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Do not keep an add-everything lesson store unbounded. Put a cap on store size. Add-all can be worse than a tiny fixed store and worse than no memory. | memory | [E] | d01, d09, K23 |
| A2 | Any pruning or demotion signal must come from a verified outcome (test result, held-out check), not from the model's opinion. Same spirit as G2 and G3. | G2/G3, memory | [E] | d04, d08, d10, K13 |
| A3 | Edit the lesson store item by item (add, edit, upvote, downvote, delete). Never ask a model to rewrite the whole store. | memory | [S] two papers, same direction; zero extra tokens | d06, d07, d11, K14 |
| A4 | When distilling lessons into rules, keep the conditions (when, which version, which input range). | memory | [S], low cost | b31, K15 |
| A5 | Protect lessons used in a passing step (protection from depression). | memory | [E] in biology and models; [S] for LLMs | a07, a22, K06 |

Only A1 and A2 are sturdy for LLMs. A3-A5 are listed because they cost nothing; they still pass G7 only when measured.

### Test first (not established for LLMs; see UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Scheduled whole-store prune pass vs add-only at equal tokens on a multi-episode stream | memory | [S] | d01-d03, c12, K12 |
| T2 | Outcome-linked deletion vs use-count vs age decay | memory | [S] | d02, d03, d16, K24, K19 |
| T3 | Prune fraction per cycle (inverted U) | memory | [S] analogy from networks | b24, b25, d07, K09, K27 |
| T4 | Prune only vs prune plus merge into rules | memory | [C] | d14, d15, K30 |
| T5 | Cap per-cycle prune share; demote only if the lesson failed where others succeeded | G, memory | [S] | d13, K25 |
| T6 | Supersession check in the prune pass | memory | [S] toy | d16, K28 |
| T7 | Offline whole-store pass vs per-episode (online) pruning | memory | [S] conceptual | a02, d17, K20, K29 |
| T8 | Prune plus small raw-episode buffer vs either alone | memory | [S] from networks | c02, c03, K10 |
| T9 | Utility-signal noise sweep (0, 10, 20, 50% wrong labels) | G, memory | [C] | d04, d08, K26 |
| T10 | Multi-cycle dip-then-gain pattern | memory | [S] model only | a11, K08 |
| T11 | Offline consolidation pass before questions (sleep-time compute) | S, memory | [S] | c18, K17 |
| T12 | Stage by store age: young vs mature | memory | [C] | a18, a14, K02 |

Do not add the sleep-branded LLM numbers to any claim. They are single-group and mostly synthetic (K18).

## 8. Concrete tests on our bench

All arms get the same total tokens, with setup and pass cost counted (G7). Items: a stream of at least 100 episodes in one problem class (for example ARC-like items and brainteasers), lessons written after each episode, evaluation on held-out items. Use plain pass rate with confidence intervals; 3 seeds minimum.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 add-only vs prune pass | 100-300 episode stream, held-out set every 25 episodes | add-only; prune every 20 episodes; frozen seed set of 20 lessons | held-out accuracy at final store, store size, tokens | Prune within 1 point of add-only or better at a 30-60% smaller store; add-only may fall below the frozen set (Xiong) |
| T2 rule comparison | same stream | outcome-linked; use-count; age decay; random prune (control) | held-out accuracy at equal store size | Outcome-linked beats use-count by 2-8 points when outcomes are verified; random is the floor |
| T3 prune fraction | stores of 20, 100, 500 lessons | drop 0, 10, 30, 60, 90% per cycle | accuracy vs fraction | Flat to slightly rising up to 30-60%, falls at 90%; optimum may move with store size |
| T4 prune vs merge | same stream | delete only; delete plus merge into rules; merge only | accuracy; fraction of rules that lose a condition (code check) | Merge adds little and drops conditions unless instructed |
| T5 safeguards | stream with a hard sub-class (low pass rate) | no cap; cap 20% per cycle; cap plus fail-where-others-succeeded rule | accuracy on the hard class and overall | Without a cap, pruning after hard-class failures loses points (RSPM -19.5); the cap removes the loss |
| T6 supersession | stream where facts change (version updates) | use-count only; use-count plus supersession check | accuracy on items needing the newest fact | Supersession check wins on stale-fact items |
| T7 online vs offline | same stream | prune after each episode; prune the whole store each 20 episodes | accuracy; which lessons survive (recency bias) | Offline slightly better, mainly when topics rotate |
| T8 buffer | same stream | lessons only; lessons plus 10 raw episodes; raw episodes only | accuracy at equal prompt tokens | Combination best at small budgets |
| T9 noisy labels | verified outcomes with injected flips | 0, 10, 20, 50% wrong | accuracy vs flip rate; crossing point vs add-only | Pruned store drops below add-only somewhere between 20% and 50% |
| T10 cycles | same stream | evaluate after 1, 3, 10 prune cycles | accuracy per cycle | Early dip then gain if the model result transfers (it may not) |
| T11 sleep-time | predictable question families | N tokens of offline consolidation vs N tokens at answer time | accuracy | Offline wins only if questions are predictable from the store |
| T12 age | young (<20) vs mature (>200) stores | prune vs add-only in each | accuracy difference by age | Benefit larger in mature stores (saturation argument), or null |

## 9. What does not transfer, and why

- **Weights vs text.** SHY acts on synaptic weights in a fixed network. Our lessons are text in a prompt. There is no multiplicative scaling of a text item. The analogue of "shrink" is lower retrieval rank or deletion, which is not the same as partial weakening.
- **Offline time is not free.** Sleep has no input and no output cost to the animal's goals. Our offline pass costs tokens counted by G7.
- **The energy argument.** The brain's glucose and area limits do not apply. Our limit is the context window and distraction, a different pressure (d01, d09 show the harm is real, but the cause is retrieval noise, not energy).
- **Net strength is not accuracy.** No biology study links downscaling to a specific piece of learned content (a28). The models (Nere) are toys.
- **Age and species dependence.** The effect is absent in juvenile rats and in adult mouse spines. We cannot map "age" onto a store without a test (T12).
- **"Sleep only deletes" is wrong in biology.** Sleep also adds and protects (b06, b07, a19). A prune-only pass is a poor analogy; the real pattern is prune plus selective strengthening plus replay (K03, K11).
- **Self-sampling in sleep.** Sleep samples the store by spontaneous activity. An LLM has none; code must point it at items. A whole-store pass by code, with scores, is the fair analogue (a02).
- **Sleep-branded LLM papers** borrow words, not mechanisms. Their tests are synthetic, simulated or single-group (K18).
- **Incubation.** SCHEMA 4b says "sleep on it" failed. Nothing here changes that; this subfield is about store maintenance.
- **Gradient-trained networks.** For gradient-trained SNNs the best sleep was 0% (b25). Downscaling may not help a trained transformer's weights, and we are not training anyway.

## 10. Open questions

1. Does a scheduled prune pass beat add-only at equal tokens on a real, independent, multi-episode stream? Only Xiong 2025 (four agents) and one simulation speak to it.
2. What fraction to prune per cycle? Robinson 2022 (best at 0.75 of weights), Massey 2026 (10-20% sleep), Xiong (66-91% record cuts for 0-4 points), ACE (no sensitivity to trigger from 10K to 100K). No sweep against store size.
3. Which rule? Outcome-linked beat frequency in one paper. Age decay alone: no ablation anywhere. Size-based protection (de Vivo analogue) and ExpeL votes alone: untested.
4. How reliable must the utility signal be? Bounded only by two points: 300 labelled outcomes was enough; ACE tolerated 1 in 5 bad updates.
5. Prune-only vs prune plus merge: not isolated. What do merged rules lose?
6. Does the early dip then gain pattern (87% to 75% to 94%) appear in LLM memory?
7. Online vs offline pruning: untested. Is the recency-bias argument true for an agent?
8. Do replay and downscaling add anything beyond a small raw-episode buffer at matched tokens? (Tadros: benefit at small buffers only.)
9. Is the benefit confined to young, saturating stores?
10. Independent replication of RSPM, SCM, SleepGate, ZenBrain: none found; the search tools were blocked.
11. Biology: which synapses shrink (small or large)? Is net downscaling real in adult cortex and hippocampus? No study tags a synapse through a learning episode.

## 11. Sources

[V] = full text or PDF opened this run (or by the checker). [M] = snippet or abstract only. Some b-line entries carry opened:true in the evidence files but were abstract-level (critique.md); they are marked [M] here.

Biology
- [V] Tononi and Cirelli (2014) Sleep and the price of plasticity. https://pmc.ncbi.nlm.nih.gov/articles/PMC3921176/ (a01-a03, a05-a09, a11, a12)
- [M] Tononi and Cirelli (2003) Sleep and synaptic homeostasis: a hypothesis. Never opened; via the 2014 review (a25).
- [V] Tononi and Cirelli (2012) Time to be SHY? https://pmc.ncbi.nlm.nih.gov/articles/PMC3350977/ (b04)
- [V] Tononi and Cirelli (2020) Sleep and synaptic down-selection. https://pmc.ncbi.nlm.nih.gov/articles/PMC6612535/ (a22, a23, b20)
- [V] Cirelli and Tononi (2022) The why and how of sleep-dependent synaptic down-selection. https://pmc.ncbi.nlm.nih.gov/articles/PMC8426406/ (b21)
- [M] Frank (2012) Erasing synapses in sleep: is it time to be SHY? https://pmc.ncbi.nlm.nih.gov/articles/PMC3317003/ (b05)
- [V] de Vivo et al. (2017) Ultrastructural evidence for synaptic scaling across the wake/sleep cycle. https://pmc.ncbi.nlm.nih.gov/articles/PMC5313037/ (a14-a16, b01)
- [V] de Vivo et al. (2019) Sleep-dependent synaptic renormalization in mouse pups. https://pmc.ncbi.nlm.nih.gov/articles/PMC6802737/ (b14)
- [V] Diering et al. (2017) Homer1a drives homeostatic scaling-down of excitatory synapses during sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC5382711/ (a17, b02)
- [V] Bushey, Tononi, Cirelli (2011) Sleep and synaptic homeostasis: structural evidence in Drosophila. https://pmc.ncbi.nlm.nih.gov/articles/PMC3128387/ (b03)
- [V] Cary and Turrigiano (2021) Stability of neocortical synapses across sleep and wake states during development. https://pmc.ncbi.nlm.nih.gov/articles/PMC8275129/ (a18, b13)
- [V] Torrado Pacheco et al. (2021) Sleep promotes downward firing rate homeostasis. https://pmc.ncbi.nlm.nih.gov/articles/PMC7864886/ (b09)
- [V] Kuhn et al. (2016) Sleep recalibrates homeostatic and associative synaptic plasticity in the human cortex. https://pmc.ncbi.nlm.nih.gov/articles/PMC4996971/ (b19)
- [V] Yang et al. (2014) Sleep promotes branch-specific formation of dendritic spines after learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC4447313/ (a20, b07)
- [V] Li et al. (2017) REM sleep selectively prunes and maintains new synapses. https://pmc.ncbi.nlm.nih.gov/articles/PMC5535798/ (a19; no numbers)
- [V] Puentes-Mestril and Aton (2017) Linking network activity to synaptic plasticity during sleep. https://pmc.ncbi.nlm.nih.gov/articles/PMC5592216/ (a21)
- [M] Aton et al. (2014) https://pmc.ncbi.nlm.nih.gov/articles/PMC4098801/ (b06)
- [M] Zhou et al. (2020) https://pmc.ncbi.nlm.nih.gov/articles/PMC7511313/ (b08)
- [M] Hengen et al. (2016) https://pmc.ncbi.nlm.nih.gov/articles/PMC4809041/ (b10)
- [M] Vyazovskiy et al. (2009) https://pmc.ncbi.nlm.nih.gov/articles/PMC2819325/ (b11); Vyazovskiy et al. (2008), second-hand via the 2014 review (a24)
- [M] Watson et al. (2016) https://pmc.ncbi.nlm.nih.gov/articles/PMC4873379/ (b12)
- [M] Spano et al. (2019) https://pmc.ncbi.nlm.nih.gov/articles/PMC6703893/ (b15)
- [M] Havekes et al. (2016) https://pmc.ncbi.nlm.nih.gov/articles/PMC4996653/ (b16)
- [M] Bridi et al. (2020) https://pmc.ncbi.nlm.nih.gov/articles/PMC9520672/ (b17)
- [M] Gonzalez-Rueda et al. (2018) https://pmc.ncbi.nlm.nih.gov/articles/PMC5873548/ (a23, b18)

Models and networks
- [V] Nere et al. (2013) Sleep-dependent synaptic down-selection (I) modeling. https://pmc.ncbi.nlm.nih.gov/articles/PMC3786405/ (a10)
- [V] Nere et al. (2013) (II) single-neuron level. https://pmc.ncbi.nlm.nih.gov/articles/PMC3790262/ (a13)
- [V] Capone et al. (2019) Sleep-like slow oscillations improve visual classification. https://pmc.ncbi.nlm.nih.gov/articles/PMC6586839/ (b23)
- [V] Tadros et al. (2022) Sleep-like unsupervised replay reduces catastrophic forgetting. https://www.nature.com/articles/s41467-022-34938-7 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC9755223/ (a26, b22, c01-c03, c25)
- [V] Golden et al. (2022) Sleep prevents catastrophic forgetting in spiking neural networks. https://pmc.ncbi.nlm.nih.gov/articles/PMC9674146/ (a27, c04)
- [V] Gonzalez et al. (2020) Can sleep protect memories from catastrophic forgetting? https://pmc.ncbi.nlm.nih.gov/articles/PMC7440920/ (c05)
- [V] Krishnan et al. (2019) Biologically inspired sleep algorithm. https://arxiv.org/abs/1908.02240 (c06)
- [V] Robinson et al. (2022) Continual learning benefits from multiple sleep mechanisms. https://arxiv.org/abs/2209.05245 (b24)
- [V] Massey et al. (2026) Sleep-based homeostatic regularization for STDP. https://arxiv.org/abs/2601.08447 (b25)
- [V] Massey, Nichele, Hubin (2026) Napping paradigm. https://arxiv.org/abs/2609.13927 (b26)
- [V] Harun and Kanan (2023) SIESTA. https://arxiv.org/abs/2303.10725 (c07)
- [V] Sorrenti et al. (2024) Wake-Sleep Consolidated Learning. https://arxiv.org/abs/2401.08623 (c08)

LLM and agent memory
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/abs/2505.16067 (c11, c12, d01-d05)
- [V] Zhang et al. (2026) Agentic Context Engineering (ACE). https://arxiv.org/abs/2510.04618 (c13, c20, d06-d09)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (c14, c21, d10, d11)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (c16, d12)
- [V] Chhikara et al. (2025) Mem0. https://arxiv.org/abs/2504.19413 (c17)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (c15, d17)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c09)
- [V] Zhong et al. (2023) MemoryBank. https://arxiv.org/abs/2305.10250 (c10)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (d18)
- [V] Lin et al. (2025) Sleep-time compute. https://arxiv.org/abs/2504.13171 (c18, c19)
- [V] Chauhan et al. (2026) Recursive Self-Pruning Memory (RSPM). https://arxiv.org/abs/2610.25561 (b28, d13, d14)
- [V] Shinde (2026) SCM. https://arxiv.org/abs/2604.20943 (b27)
- [V] Xie (2026) SleepGate. https://arxiv.org/abs/2603.14517 (b29, d16)
- [V] ZenBrain authors (2026). https://arxiv.org/abs/2604.23878 (b32)
- [V] Wei et al. (2026) FadeMem. https://arxiv.org/abs/2601.18642 (b30, d15)
- [V] Kyrkewood (2026) The Sleeping Agent. https://arxiv.org/abs/2608.11775 (b31)
- [M] Packer et al. (2023) MemGPT. https://arxiv.org/abs/2310.08560 (c24)
- [M] Xu et al. (2025) A-MEM. https://arxiv.org/abs/2502.12110 (c23; no pruning numbers)
- [M] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (c22; no pruning numbers)
