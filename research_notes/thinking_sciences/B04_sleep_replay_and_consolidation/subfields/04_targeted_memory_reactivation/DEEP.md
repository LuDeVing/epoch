# Targeted memory reactivation: deep document

*Subfield B04.04. Sources: evidence_a-d.jsonl (ids a01-a27, b01-b27, c01-c25, d01-d26), claims.jsonl (K01-K32), critique.md in this folder. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Targeted memory reactivation (TMR) is a method from sleep science. A person learns something while a cue is present. The cue is a sound or a smell tied to the item. Later, while the person sleeps, the lab replays some of those cues. Memory for the cued items is then compared with memory for items that were not cued.

The idea is simple. During deep sleep the brain replays recent memories on its own. A cue is thought to push the brain to replay one chosen memory more often. If the chosen item is remembered better afterwards, replay is a cause of consolidation, not just a side effect.

What the field measures:
- Within-person contrast: cued items against uncued items in the same sleeper.
- Between-group contrast: cue during sleep against cue while awake, or against no cue.
- Memory tests the next day or after a nap: free recall, location error, finger-tapping speed, recognition.
- Sleep physiology: slow oscillations, spindles, and EEG responses to the cue.

The pooled result is a small, reliable benefit (Hedges g = 0.29, 91 experiments, N = 2004; a01). The benefit appears in NREM sleep, not in REM or wake (a02). Publication-bias correction shrinks it to about 0.13 to 0.18 (a06). Several 2022 to 2026 studies find no overall cued benefit (b07-b11, d06-d09).

Why this matters for our agent. The agent is a scaffold around a language model. It has no sleep. What can transfer is a design idea: a separate offline pass that re-presents chosen stored items, chosen by a cue, with no new input arriving. No study has tested that on a language model (K20, c20, d26). The evidence for the agent therefore comes from three sources: the human boundary conditions (when does re-presentation help or hurt), nearby LLM work on offline or idle-time computation (sleep-time compute and kin), and replay models in neural networks. Mapping to our agent is by analogy and each mapping needs its own test.

## 2. History and theories in depth

**Active systems consolidation (the main theory).** New memories are first held in the hippocampus. During NREM sleep they are replayed spontaneously. Replay is coordinated by slow oscillations, thalamo-cortical spindles and hippocampal ripples. Over repeated replays the memory is moved to cortex and becomes more stable (a26, b13). TMR adds one claim: a cue biases which memories get replayed. Cairney et al. (2018, a14) showed that a verbal cue in a nap evoked fast spindles, that the object or scene category of the cued item could be decoded in that window, and that decoding fidelity predicted later benefit. Schreiner et al. (2021, b13) found decodable reactivation without any external cue, and stronger reactivation predicted better consolidation across people.

**Rasch, Buchel, Gais and Born (2007), the founding study (a07, b02, c16).** A rose odour was present while people learned card-pair locations (a hippocampus-dependent task). The odour was presented again in slow-wave sleep. Recall rose. The same odour in REM did not help, odour during waking did not help, and a procedural finger-tapping task did not gain. An odour absent at learning did not work. fMRI showed hippocampal activation. Effect sizes come from Hu's table, because the primary text was never opened here: Exp 1 spatial g = 0.69 [0.19, 1.18], N = 18; finger tapping g = -0.08; Exp 3 REM g = -0.05, N = 17; Exp 5 SWS g = 0.64 [0.05, 1.22], N = 12. Three boundary conditions that still frame the field were already there: sleep state, memory type, and the link between cue and learning.

**Rudoy, Voss, Westerberg and Paller (2009) made it item-specific (a08, a09).** Each of 50 object-location pairs had its own sound. In a nap, half the sounds were replayed. People were at chance in guessing which sounds had been played. Location error was 1.07 cm (SE 0.08) for cued objects and 1.23 cm (SE 0.10) for uncued, t(11) = 2.6, p < .05, N = 12, with benefit in 10 of 12 people. An awake control (N = 12) showed 1.15 vs 1.32 cm, t(11) = 1.4, p = .18. The brain response to the sound tracked forgetting: EEG 600-1000 ms after onset was 15.3 microvolts larger on items that were forgotten less, t(11) = 3.2, p < .01. Hu's meta-analysis converts the same study to g = 0.48 [-0.08, 1.04], p = .095. The conversion is more conservative; do not call Rudoy strong.

**Extensions in the 2010s.**
- Skill learning (a10, a11). Cousins et al. (2014), N = 32: tones tied to one of two 12-item finger sequences, replayed in SWS. The cued sequence gave better explicit knowledge (p = .005) and faster skill (p = .04). Fast spindles at motor regions predicted skill gain, r = 0.71, p = .01. The control group, cued before sleep, showed no cue effect.
- Emotional memory (a12). Cairney et al. (2014), N = 15, 72 picture-location pairs. The cue helped negative pictures more than neutral, but only in response time, not accuracy, and only as a function of SWS and spindles.
- Weak memories (a13, b15). Cairney et al. (2016), N = 30: low-accuracy items benefited, strongly learned items did not. Overall TMR x time was only marginal, F(1,29) = 4.00, p = .055. Picture-word pairs, linked to the cue only indirectly, did not benefit. Creery et al. (2015, N = 20) found benefit only when pre-sleep accuracy was not near ceiling.
- Social bias (a15). Hu et al. (2015), N = 40 with a built-in replication: a sound paired with counter-stereotype training, replayed in SWS, reduced the cued implicit bias (F(1,39) = 14.61, p < .001; cued bias fell, t(39) = 2.70; uncued unchanged). At one week the cued/uncued difference held, F(1,37) = 4.67, p = .037, but cued against baseline was not significant (F = 0.47).

**The state question.** Four lines say the sleep state decides the outcome. Rasch 2007: SWS works, REM and wake do not. Cordi et al. (2014, a18): odour reactivation in REM did not protect memory from later interference (54.16 vs 52.86 percent, p = .87). Cairney 2018 (a14): the wake group showed no cue effect (t(18) = 0.09, p = .93) while the nap group did (t(26) = 3.83, p = .001). Hu et al. (b12): NREM P = .032, REM P = .982, wake P = .692, N = 62. Hoffman et al. (2024, b04, b05) show that awake TMR is mostly null (section 5).

**Fear and conditioning.** Fear is where the field is not settled.
- Humans, pooled: conditioning g = -0.03 [-0.35, 0.29], 4 experiments, N = 91; skin-conductance outcome g = -0.08 (a03, a20).
- Mouse: NREM cueing of the tone weakened later fear; REM cueing did not (Purple et al. 2017, a19).
- Mouse, substage matters (Zheng et al. 2024, d01): cueing during non-slow-wave NREM weakened fear, cueing during slow-wave sleep strengthened it. The sign depends on substage.
- Human odour-context extinction (Hauner et al. 2013, b17) was positive.
- Human PTSD, closed-loop TMR with the EMDR click (van der Heijden 2024, d02): TMR n = 17, sham n = 16, reduced avoidance in script-driven imagery. Small, and from a team that holds a device patent.
- Human weakening of an aversive memory by cueing a competing positive one (Xia et al. 2024, d03).
- Mouse causal test (b18): inhibiting cue-responsive V1 neurons during post-conditioning sleep disrupted fear consolidation.

**Models.** Lu, Foldes and Lewis (2024, c01-c03) built a small complementary-learning-systems network to simulate TMR (section 4). Barry and Love (2022, c04) showed in a VGG-style network that generative replay helped generalisation, and that a learned chooser replaying categories by their contribution mimicked selective consolidation of weak memories.

**The shift of the 2020s.** The first meta-analysis (Hu et al. 2020) stopped at about 2019. Since then single studies mostly report no overall cued benefit, benefit only for weak traces, or harm in unexpected states. The 2024 npj Science of Learning review (a21) says some declarative effects did not replicate, most studies are small, and calls for large preregistered multi-lab studies. In the same years engineers began to build "sleep" and "idle-time" methods for language models. They borrow the idea of an offline pass, not the cue.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pooled TMR effect, small but reliable | g = 0.29 [0.21, 0.38]; 91 experiments, 212 effect sizes, N = 2004 | Hu 2020 (a01) | [E] |
| Bias-corrected effect is about half | 3-parameter selection model g = 0.13 [0.06, 0.21]; trim-and-fill g = 0.18 [0.06, 0.30] (17 imputed); severe one-tailed g = -0.05. Published 0.31 vs unpublished 0.18, difference not significant (Q(1) = 1.005, p = .316) | Hu 2020 (a06) | [S] (one meta-analysis, none since) |
| Works in NREM only | SWS g = 0.27 [0.20, 0.35] (k = 174); N2 g = 0.32 [0.04, 0.60] (k = 13); REM g = -0.06 [-0.31, 0.18] (7 exp, k = 15); wake g = 0.07 [-0.09, 0.23] (18 exp, k = 30); unspecified g = 0.26; Q(4) = 10.74, p = .030 | Hu 2020 (a02) | [E] |
| N2 vs SWS not decisive | N = 34, no overall cued benefit, no N2/SWS difference; N = 20, F(1,18) = 4.05, p = .059, BF01 = 11.06 for equal effect | Wick and Rasch 2023 (b07); Sci Rep 2024 (b08) | [E] |
| Learning type | declarative g = 0.23 [0.15, 0.31]; skill g = 0.44 [0.25, 0.64]; conditioning g = -0.03 (4 exp, N = 91); others 0.38; Q(3) = 8.06, p = .045 | Hu 2020 (a03) | [E] skill > declarative; conditioning [C] |
| Outcome type | recall g = 0.24; performance 0.40; recognition 0.18 [-0.04, 0.40]; SCR -0.08; subjective 0.11 | Hu 2020 (a04) | [S] |
| Cue modality does not matter | auditory verbal 0.26; non-verbal 0.23; olfactory 0.32; Q(2) = 0.69, p = .709 | Hu 2020 (a05) | [S] |
| Design does not matter | within-subject 0.25 vs between-subject 0.28, p = .81 | Hu 2020 (a04) | [S] |
| Founding odour result | Exp 1 spatial g = 0.69 [0.19, 1.18], N = 18; REM g = -0.05, N = 17; finger tapping -0.08 | Rasch 2007 via Hu (a07) | [E] |
| Item-specific sound cueing | 1.07 vs 1.23 cm, t(11) = 2.6, N = 12; Hu g = 0.48 [-0.08, 1.04], p = .095 | Rudoy 2009 (a08) | [E], weak per study |
| Skill memory | N = 32, explicit knowledge p = .005, skill p = .04, spindle r = 0.71 | Cousins 2014 (a10) | [E] |
| Weak items gain, strong items do not | N = 30, overall F(1,29) = 4.00, p = .055; N = 20 (Creery) | Cairney 2016; Creery 2015 (a13, b15) | [E], 2026 support (d06, d07) |
| Very hard items may not gain | N = 22, easy words gain, difficult words no effect | Klaassen and Rasch 2024 (d05) | [S] |
| Cue count does not buy gain | rho = 0.02 (Cairney 2018); r = 0.23, p = .22 (2016); once vs five times N = 31 null | a27, d09 | [E] |
| Sleep physiology predicts gain | cue effect vs N3 duration p = .02, relative N3 p < .001, N = 24 (face-name); spindle r = 0.71 | b11, a10 | [E] |
| Awake cueing null or harmful | Hoffman N = 40, 40, 41: disruption in Exp 1, no effect in Exps 2 and 3 even with 6 study repeats; 14-result table mostly null | Hoffman 2024 (b04, b05) | [E] |
| Wake vs nap in one study | nap cued > uncued t(26) = 3.83, p = .001; wake t(18) = 0.09, p = .93; N = 46 | Cairney 2018 (a14) | [E] |
| Recent nulls | home TMR N = 61 no overall effect; face-name N = 24 delta 0.75 vs 0.21, p = .36; theta-tACS N = 37 (94.10 vs 98.35 percent, p = .31); once vs five N = 31; odour set N = 32; word-meaning priming; dogs N = 16 | b10, b11, b09, d09, d06, d08, b19 | [E] |
| Closed-loop stimulation without item cue | oscillations up, memory not up, N = 12 and N = 19 (95 percent power for a moderate effect) | Henin 2019 (a16) | [S] |
| Up-state timing | N = 16, up-state words theta t(15) = 2.69, p = .008; behavioural up vs down contrast not robust | a17 | [S] |
| Home closed-loop vocabulary | cued +8.6 percent vs uncued -4.6 percent, N = 24, no separate control | b14, d15 | [S] |
| Closed-loop spindle motor | N = 26, cued sequence gains larger when cues land in spindle trains | d16 | [S] |
| Cueing is not holistic | distinguishing features improved, shared features worsened, N = 34 | b23 | [C] |
| Competing memory weakens | positive-image cues weakened aversive recall; 48 word-image pairs | Xia 2024 (d03) | [S] |
| Stacked odour cues cancel | sound benefit only for weakly encoded items; odours tied to remember/forget instructions removed it | d07 | [S] |
| Suppress tone | replaying the "suppress" tone increased suppression-induced forgetting | d04 | [S] |
| Week-old memories resist harm | disrupting cues did not weaken 1-week-old memories, unlike fresh ones | d10 | [S] |
| Emotion | NREM only, emotional > neutral, N = 62, interaction F(1,59) = 3.17, P = .049; REM cueing impaired emotional memory (2025); RT-only effects N = 15 | b12, d13, a12 | [C] |
| Adaptive dose by difficulty | hardest items: group x time F(2,66) = 8.91, p < .001; personalized t(11) = -5.68; overall interaction F(2,66) = 0.74, p = .479; N = 12 per group | Shin 2025 (c13, a24, d14) | [S] |
| Implicit bias reduction | cued bias fell t(39) = 2.70, p = .010; N = 40 | Hu 2015 (a15) | [S] |
| PTSD closed-loop TMR | n = 17 TMR vs n = 16 sham, lower avoidance | d02 | [S] |
| Imagery rescripting plus TMR | N = 80, preregistered, rescripting d = 0.76-1.66, TMR added gains | d17 | [S] |
| LLM: sleep-time compute | about 5x less test-time compute at equal accuracy; +13 percent (GSM-Symbolic), +18 percent (AIME) when scaled | Lin 2025 (c08) | [S] |
| LLM: at uncertain observations it fades | Qwen3.5-4B 33.2 to 29.4; Gemini-2.5-Flash 50.5 to 50.1 (row mapping from a garbled table) | IdleSpec (d19) | [S] |
| LLM weight-level sleep | Qwen3-8B AIME-24: Sleep 79.2, OPSD 76.6, GRPO 76.4, SFT 75.5 | Behrouz 2026 (a22) | [S] |
| LLM agent nightly rewrite | cross-session recall 71 +/- 7 vs 0 with no rewrite; 40 percent wrong detail 76 to 60 | Zou 2026 (d22) | [S] |

## 4. Mechanisms and models

### 4.1 The biological mechanism, in steps

1. Learning links an item to a cue (sound, odour, instruction tone) in the same episode.
2. The memory is held first in a fast-learning store (hippocampus).
3. In NREM sleep, slow oscillations (about 1 Hz) group activity into up-states. Spindles (12-16 Hz) and ripples ride on the up-states. This is the window in which replay happens.
4. A cue played into that window re-activates the linked memory. Evidence: the cue evokes fast spindles and the content category can be decoded in the window (a14).
5. The replayed memory is strengthened and shifted toward the slow-learning store (cortex).
6. The size of the benefit tracks how much good sleep the person had (SWS time, spindles), not how many cues were played (a27).

Things that break the chain: the person is awake (new input competes), the person is in REM (different dynamics, g = -0.06), cues arouse the sleeper (face-name study, b11), or the memory is at ceiling (nothing to gain).

### 4.2 The CLS model (Lu, Foldes, Lewis 2024; c01-c03), as an engineer would build it

- Two stores. A fast store (hippocampus) and a slow store (cortex). Both are small networks.
- Training: the fast store learns the pairs quickly. The slow store learns only from replay of the fast store.
- Replay modes: spontaneous (the fast store reactivates items by itself), noise-driven (random input drives it), cue-driven (a cue input selects the item).
- A cue switches the fast store from spontaneous or noise-driven replay to cue-driven replay for the targeted pairs.
- Four variants: hippocampus plastic or stable, times replay spontaneous or noise-driven. 100 simulated repetitions per model.
- Results (Table 1, qualitative signs): the cued pair beats non-cued pairs only in the TMR condition. The two stable-hippocampus models show a positive targeted effect and zero non-targeted effect. The plastic and noise-driven model shows a negative effect on non-targeted memories. The TMR gain lasts or grows only if the hippocampal store consolidates its own replay; with a stable store it decays.
- Limits. Replay is perfect in the model, so effects are far larger than in humans. Signs are not fitted to data.
- Predictions to carry over: (a) a replay pass can cost neighbouring items when the store is plastic; (b) a gain from replay lasts only if the replayed material is written back into the store; (c) the mix of benefit, null and cost in human data can come from one mechanism with different store plasticity.

### 4.3 Replay chosen by contribution (Barry and Love 2022; c04)

A reinforcement-learning chooser decided which categories to replay, rewarded by their contribution to performance. It replayed newly acquired and weak categories more. That reproduces the human pattern that weak memories gain and strong ones do not. Implementation: score each stored item by expected gain, replay the top scorers, keep the rest.

### 4.4 Sleep-time compute (Lin et al. 2025; c08-c10), as an engineer would build it

- Input: a context (a document, a repository, a conversation) that will be queried later.
- Offline step: while idle, the model writes inferences about the context, such as likely questions and derived answers. The output is a stored annotation of the context.
- Online step: at question time the model reads context plus annotation and answers with a smaller test-time budget.
- Measured: about 5x less test-time compute for equal accuracy on Stateful GSM-Symbolic and Stateful AIME. Scaling sleep compute added up to 13 percent and 18 percent. 5 parallel generations beat 10 in the stated setting. The gain widens with how predictable the question is from the context (c09, five quantile bins, GPT-4o-mini). On SWE-Features the idle exploration won at small test budgets and lost at large ones (F1 axis about 0.30 to 0.55 over 3000 to 10000 test tokens; read from a plot).
- Limits: the authors built the stateful variants; o1 showed limited gains.

### 4.5 Related offline methods, each with its mechanism

- **IdleSpec (d19).** Plans conditional branches during idle time instead of guessing the next question. In tool agents the sleep-time baseline fell to or below vanilla. IdleSpec gained 5 to 7 points over vanilla.
- **ProAct (d23).** Predicts the user's next need chain and gathers evidence. Cut required turns 14.8 percent and user effort 11.7 percent on 200 predictable scenarios.
- **Studying Without a Syllabus (d20).** An agent studies an environment before the tasks are known. Beat no-study on 5 of 6 benchmarks. Budgets from $1 to $50 were flat or non-monotonic on two benchmarks; one rose 0.271 to 0.348. Studied artifacts cut the test-time rollouts needed (no-study needed 2 to 8 rollouts to match).
- **Auto-Dreamer (d21).** A learned consolidator rewrites a region of the memory bank offline. ScienceWorld +7 points over the best baseline with a 12x smaller active bank. Best at pass frequency k = 10, worse at k = 1 and k = 20. Point estimates only.
- **Nightly rewrite (Zou 2026; d22).** A Claude agent rewrites its text memory each night from the day's transcript. 10 days, about 130,000 tokens per day, 30 runs. Clean rewrite 71 +/- 7 multi-session recall; no rewrite 0. Overnight loss 8 +/- 2 clean vs 21 +/- 2 with detail corruption. Random text paired difference 0 +/- 2.
- **Librarian Agents (d24).** Builds a file workspace before queries. +33 points over the strongest baseline on BrowseComp-Plus. RL-trained, not a prompt scaffold.
- **SleepGate (c11, c22).** A learned micro-cycle on the KV cache evicts or merges superseded entries. 4-layer, 793K-parameter transformer. 99.5 percent at interference depth 5 and 97.0 at depth 10, then 73.5, 30.5 and 16.5 at depths 15, 20, 30. Decay-only was no better than baselines (12.5 percent at depth 2). Sleep overhead 15.6 percent.
- **SCM (c12, c23).** Memory with a working-memory limit, importance tags, NREM-like consolidation. 22/22 with 24 stored items vs FIFO 8/22. Removing the value tagger drops it to 18/22, removing NREM consolidation to 20/22. Only 22 questions.
- **Weight-level methods.** Language Models Need Sleep (a22, c07): knowledge incorporation 31.9 base, 33.4 fine-tune without dreaming, 46.7 SEAL, 48.1 Sleep, 48.9 four-level; removing Dreaming 48.1 to 35.7. Offline recurrent passes (a23): cellular-automata exact accuracy from about 10 percent to above 30 percent with 3 to 4 loops. WSCL (c05, c24): ablation 4.70 wake only to 35.68 with REM and NREM, 2 to 17 percent fewer updates. SRC (c06, c25): ECE 0.0622 to 0.0130 on ResNet-152 CIFAR-100 versus 0.0169 for temperature scaling. These need weight updates. They are not scaffold methods.

### 4.6 A TMR-like procedure for a scaffold (our design, untested)

This is a design for a test, not a finding.
1. During work, each lesson or fact is stored with a short cue tag (a key phrase) and the problem class.
2. After the run (no new input), a replay pass starts. Code selects the items to replay by a rule (for example: items the agent got wrong or was unsure of, from logged outcomes).
3. For each selected item, the cue is presented and the model re-derives or restates the item in a fresh context. The output is written back to memory only if it passes a check (for example it agrees with a stored ground-truth outcome).
4. Neighbouring items that were not replayed are tested afterwards to measure cost.
5. The pass has a token cap equal to the tokens the control arm spends on extra attempts.

## 5. What holds up

### 5.1 Holds up (replicated or pooled)

- **A small NREM cueing benefit exists on average.** Hu 2020, g = 0.29, and still about 0.13 to 0.18 after bias correction (K01, K02).
- **State gating.** NREM works, REM and wake do not pool to an effect. Four independent lines agree (K03). Within NREM the stage is not decisive: SWS vs N2 shows no difference (b07, b08).
- **Awake cueing mostly fails.** Hoffman three experiments and a 14-result table (K13). Raising study repeats from 3 to 6 did not rescue it.
- **Weak, not-yet-saturated items gain most.** Cairney 2016, Creery 2015, two 2026 studies (K10).
- **Dose is not the lever.** Cue count correlates with nothing (rho = 0.02; once vs five times null) (K12). The lever is the sleep state.
- **Recall and performance show it; recognition and ratings do not** (K07, single meta-analysis).
- **Skill tasks gain at least as much as declarative.** g = 0.44 vs 0.23 (K05).

### 5.2 Failures and nulls

- Wick and Rasch 2023 (N = 34): no overall cued benefit.
- SleepStim home TMR (N = 61): no overall effect. Low-intensity sound helped, high-intensity did not.
- Face-name TMR (N = 24): overall null. The cue effect depended on N3 time and arousals.
- Theta-tACS with TMR (N = 37): null; both tACS protocols blocked the usual benefit.
- Cued once vs five times (N = 31): null; an interference task raised error rates a lot and may have masked the effect.
- Odour-cued set (2026, N = 32): no overall benefit for the cued set; benefit only through encoding strength.
- Word-meaning priming (2025): priming happened, TMR added nothing, though cues raised spindle and beta power.
- Dogs (N = 16): no choice benefit, higher fast-spindle density on TMR nights.
- Henin 2019: closed-loop stimulation raised oscillations without a memory gain, in two experiments (N = 12 and N = 19). It is a failed replication of the Ngo 2013 design, not of item-cued TMR.
- Pattern: a physiological response to the cue (spindle, beta power) appears without a behavioural gain. A physiological proxy is not proof of a better memory (K15).

### 5.3 Moderators

| Moderator | Direction | Evidence |
|---|---|---|
| Sleep state | NREM yes; REM and wake no; REM can impair emotional items | a02, d13, b24 |
| Mouse sleep substage | non-slow-wave NREM cueing weakens fear; SWS cueing strengthens it | d01 |
| Encoding strength | weak items gain; ceiling items do not; the weakest (difficult words) may not | a13, b15, d05, d06, d07 |
| Cue-memory link | direct link needed; indirect picture-word pairs did not gain | a13, a07 |
| Sleep quality | N3 time, spindles, few arousals predict gain | b11, a14, a27 |
| Memory age | week-old memories resisted harm from disrupting cues | d10 |
| Interference | a competing memory or extra odour cues cancel or reverse the effect | d03, d07, b23 |
| Task type | skill > declarative > conditioning (null) | a03 |
| Measure | recall and performance show it; recognition and ratings do not | a04 |
| Sample size | nearly all studies N 12 to 40; mean about 22 | critique |

### 5.4 Interventions that worked

- Adaptive dose by difficulty (Shin 2025): worked on the hardest items only; overall interaction not significant; one lab, N = 12 per group.
- Closed-loop timing to slow-oscillation up-states (N = 16, N = 24, N = 26): positive, small, single lab.
- Pairing the cue with an instruction: a suppress tone increased forgetting (d04); a competing positive memory weakened an aversive one (d03).
- Clinical use: EMDR click in PTSD (n = 17 vs 16); imagery rescripting plus TMR (N = 80, preregistered). Both come from groups with device interests.

### 5.5 Interventions that did not work

- More cues (five vs one).
- Boosting encoding to rescue awake TMR (6 study repeats).
- Theta-tACS during cueing.
- High-intensity sound at home.
- Odour tied to multiple episodes (cancelled the sound benefit).
- Cueing in REM for declarative memory.

### 5.6 Contradictions in the literature

- Hu's pooled effect is positive, yet most 2022 to 2026 single studies find no overall benefit. Both can be true if the true effect is 0.13 to 0.2 and studies are underpowered. The meta-analysis needs updating; PubMed shows none after 2020 (d18).
- Hoffman says awake cueing is null or harmful. Hu's wake g = 0.07 agrees on null, not on harm. Harm appeared in 1 experiment of 3.
- Fear: human pooled null, mouse sign flips by substage. Not settled.
- Emotion: some studies say emotional items gain more, some find only RT effects, one finds REM cueing impairs them.
- Item specificity: the 2026 odour study suggests the benefit spread across the whole learning context, against the item-specific picture from Rudoy.

## 6. Language models

**No LLM study tests TMR.** Nothing gives a model an external cue tied to a stored item, re-presents it in an isolated pass, and measures item-specific recall (K20, b27, c20). A title screen of the 49 papers citing Sleep-time Compute found none (d26). This is title-level and the search tools were rate-limited, so treat it as likely true, not proven.

**What exists is nearby.** Grouped by how close it is to TMR.

| Group | Study | Result | Closeness to TMR |
|---|---|---|---|
| Idle pre-computation in context | Sleep-time Compute (Lin 2025) | 5x less test compute at equal accuracy; +13 and +18 percent when scaled; gain tracks predictability; baseline wins at high test budget | selective rehearsal chosen by prediction, no external cue |
| | IdleSpec (2026) | Sleep-time baseline fell to or below vanilla in tool agents; conditional plans +5 to +7 points | boundary condition: unpredictable observations |
| | ProAct (2026) | turns -14.8 percent, effort -11.7 percent, predictable chains only | same |
| | Studying Without a Syllabus (2026) | 5 of 6 benchmarks; budget flat; fewer test rollouts needed | same |
| | Librarian Agents (2026) | +33 points on BrowseComp-Plus; RL-trained | same, trained |
| Offline memory rewrite | Zou 2026 | clean nightly rewrite 71 vs 0; corrupted replay hurts | closest to a replay step on an LLM agent |
| | Auto-Dreamer (2026) | +7 points ScienceWorld; best at k = 10 | learned consolidator |
| | SCM, SleepGate | 22/22 vs FIFO 8/22; 99.5 percent at depth 5 | tiny models, tiny test sets |
| Weight-level sleep | Behrouz 2026; Lee 2026 | AIME-24 79.2 vs 76.6; CA accuracy 10 to over 30 percent | needs weight updates |
| Non-LLM networks | WSCL, SRC, Tadros 2022, Barry and Love 2022 | replay helps continual learning and calibration | replay in networks, not LLMs |

**How they behave and what changed it.**
- An idle pass helps when the future question is predictable and the result is reused. It fades when observations are uncertain (Qwen3.5-4B 33.2 to 29.4, Gemini-2.5-Flash 50.5 to 50.1), and the baseline can win at high test-time budgets.
- More idle budget did not reliably help (flat from $1 to $50 on two of three benchmarks).
- Pass frequency has an optimum (k = 10 best, k = 1 and 20 worse; no variance reported).
- Replay must be faithful. A wrong-detail distortion at 40 percent cut multi-session recall from 76 to 60. Random text changed recall by 0 +/- 2. Distortion did not improve transfer.
- Decay alone is not enough (SleepGate decay-only no better than baselines).
- Offline rewriting kept recall across sessions where no rewrite gave 0.

**Caveats for all of the above.** Authors build or modify the benchmarks to be stateful. Point estimates without seed variance are common (Behrouz, Auto-Dreamer). SleepGate and SCM use tiny models and 22 questions, where one question is 4.5 points. The IdleSpec row mapping comes from a garbled table. None of it is TMR; the analogy is that an offline pass re-presents selected material with no new input.

## 7. What our agent should take

Rule from SCHEMA.md section 8: a new element enters as [S] or [D] with an equal-token test. Established human findings do not become established agent findings, because the mapping to a language model is untested. So "Add now" is limited to guardrail-level and measurement practice that follows from established human boundary conditions and adds no new state.

### Add now (established)

| Item | Schema part | Status | Evidence | What it says |
|---|---|---|---|---|
| Never run a rehearsal or consolidation step in the middle of active problem solving. If one is run, run it in an isolated pass with no new input. | G (extends G1/G10 logic; state gating) | [E] human; agent mapping by analogy | K03, K13; a02, b04, b05, a14, b12 | Wake-state cueing was null or harmful in 3 experiments plus a 14-result table; NREM works. |
| Judge any replay step by outcome checks, never by an internal proxy and never by the agent's own confidence. | G (G10 already), log | [E] | K15, K07; a16, a04, b09 | Oscillations rose without memory gain in two replications; recognition and ratings do not show the effect. Score on free recall of the item. |
| Do not make replay depend on count. Do not repeat a rehearsal many times to buy gain. | G (G7, G12) | [E] | K12; a27, d09 | Cue number correlated with nothing (rho = 0.02; once = five times). Gate on state and need, not volume. |
| Plan for small effects. Use many items, paired designs, and report nulls. | bench practice | [E] | K01, K02, K14, K31; a01, a06, b07-b11 | True effect about 0.13 to 0.29; mean N about 22; many 2022-2026 studies are null. |
| Keep memory writes faithful. Never inject noise or distortion as "regularisation". | memory | [S] (one agent study), cheap to follow | K30; d22 | Wrong-detail replay hurt (76 to 60). |

### Test first

| Item | Schema part | Status | Evidence | Test sketch |
|---|---|---|---|---|
| Cue-tied replay pass: a stored lesson with a cue tag is re-presented in an isolated pass; compare against no replay at equal tokens. | memory, S9 look-back | [S] (no LLM test exists) | K01, K20, K21 | U1 and section 8 T1, T2. |
| Replay only items the agent got wrong or is unsure of, vs replay all. | O / memory (selection by code) | [E] human; untested in LLM | K10; a13, b15, d06, d07; c04 | U2. The very weakest items may not gain (d05). |
| Isolated replay vs the same re-presentation during task work. | G/S | [E] human; untested in LLM | K03, K13 | U3. |
| Cost to non-replayed neighbours. | memory | [C] | K17, K32; c03, b23, d03, d07 | U4. |
| Dose by difficulty rather than fixed count. | O | [S] | K11; c13, a24, d14, d05 | U5. |
| Idle pre-computation of notes for the predicted next step vs conditional plans. | S/O | [S] | K21, K27; c08, d19, d23 | U6. Only where follow-ups are predictable. |
| Cap idle passes and sweep pass frequency. | S | [S] | K28, K29; d20, d21 | U7. |
| Replay with a tag (keep or drop) and a rival item. | operators (replay with tags) | [S] | K32; d03, d04, d07 | U8. |
| Procedure-like items gain more than facts. | memory | [E] human pooled | K05; a03 | U9. |

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, with setup and replay tokens counted (G7). Use at least 100 items, a paired design, 3 seeds, and report null results with confidence intervals. Expect effects near the human range (standardised effect 0.1 to 0.3); size the item count for that.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Cue-tied replay vs none | Multi-session problem classes: a lesson learned in session 1 (rule or fact), tested in session 2 on a variant | A: isolated replay pass on cued lessons. B: the same tokens spent on extra independent attempts | Free-recall accuracy of the lesson-dependent answer on session-2 items; paired difference | Small positive, about 0.1 to 0.3. If it beats no replay but loses to extra attempts, drop it. |
| T2 Within-run item-level contrast | One run, 50 lessons, half cued in the replay pass, half not | Cued vs uncued items in one run (the Rudoy design) | Recall on cued vs uncued items | Small positive on weak items; null on items already correct |
| T3 Weak-only vs all | Items with logged first-attempt outcome | A: replay only failed or low-consistency items. B: replay a random equal number. C: replay all, same total tokens by shortening each | Gain per replay token; recall on previously failed items | A > B on failed items. Not expected to help the very hardest items. |
| T4 Isolated vs in-task | Same items | A: replay in a separate pass with no new problem. B: the same re-presentation inserted into the next task's context | Accuracy on the next task and on recall | A >= B; B may hurt (wake result) |
| T5 Neighbour cost | Lessons with near neighbours (shared surface features) | After replay of one lesson, test its non-replayed neighbours | Accuracy on neighbours vs a control run with no replay | Neutral or small negative; a drop above 2 points is a stop |
| T6 Dose by difficulty | Items with graded difficulty (plain pass rate) | A: replay count 1, 2, 4 by difficulty. B: fixed count with the same total | Accuracy on the hardest tercile | Helps only the hardest tercile |
| T7 Predictable vs unpredictable follow-up | Same context; follow-ups from a predicted set vs a surprise set | A: pre-computed notes. B: conditional plans. C: none | Accuracy at equal idle plus test tokens | Notes win on predictable; conditional plans win or tie on unpredictable (IdleSpec pattern) |
| T8 Faithful vs distorted replay | Same items | A: faithful replay. B: replay with injected wrong detail at 20 percent | Recall | A > B; no gain from noise |
| T9 Procedure vs fact | Multi-step procedures vs single facts | Replay both | Gain per class | Procedures at least as large as facts |
| T10 Replay with tag | Items with a keep or drop tag and a rival | Replay with the tag vs without | Retention of the tagged item and of the rival | The tag changes the item's fate in the expected direction |

## 9. What does not transfer, and why

- **The sleep state itself.** A model has no sleep stages, slow oscillations, spindles or arousals. State gating transfers only as the rule "isolate replay from active work", and that rule is by analogy.
- **Odour and sound as channels.** Hu found modality does not matter (g 0.26, 0.23, 0.32). For a model a "cue" is a token string. Whether a token cue does anything beyond the content it points to is unknown.
- **Spontaneous replay.** Humans replay spontaneously and the cue biases it. A model replays nothing unless we make it. So we pick the items by code; the "bias" step is our selection rule, not a nudge on a hidden process.
- **Fear and conditioning.** Human pooled null (4 experiments, N = 91), mouse results flip with substage, no LLM analogue. Skip it.
- **Emotion and valence.** Mixed in humans and not testable on a model (K18).
- **Physiological readouts.** Spindle, theta and beta responses had no necessary link to behaviour (b07, b09, d08). Nothing like them exists to check in a model, and we should not invent a proxy.
- **Consolidation into cortex.** The CLS model says gains last only if replayed material is written back (c02). For a prompted agent the write-back is a memory edit. Whether that behaves like a plastic hippocampus (costs to neighbours) is open.
- **Weight-level sleep methods** (Behrouz, Lee, WSCL, SRC, SleepGate). They update weights or caches. They are out of scope for a scaffold-only agent and serve as motivation only.
- **Incubation or "sleep on it" as a thinking aid.** SCHEMA 4b already lists distraction-based incubation as not working. TMR does not revive it. TMR needs a stored item and a cue; it does not say a rest between attempts helps.
- **Clinical findings** (PTSD, imagery rescripting). Positive but small, from groups with device interests, and no agent analogue.
- **Effect sizes.** Human g is about 0.13 to 0.29. LLM idle-compute gains (5x compute saving, +13 to +18 percent) come from benchmarks built to favour pre-computation and are not comparable.

## 10. Open questions

1. Does cueing a stored item with an external token, in an isolated pass, raise item-specific recall in an LLM agent at equal tokens? (No test found; K20.)
2. Isolated replay vs in-task replay at equal tokens: does the wake/NREM contrast show up? Nearest evidence: Zou 2026 (separate nightly rewrite 71 vs 0, no in-task arm) and the study-budget plateau (d20).
3. Replay only low-confidence items: partly closed in humans (weak items gain; the weakest may not, d05), open for LLMs.
4. Cost to neighbours: appears in the CLS model and in human interference studies. Not tested in an LLM.
5. What is the updated pooled TMR effect after 2020? No meta-analysis is newer than Hu 2020. A title scan shows at least five 2024 to 2026 nulls or encoding-strength-only results against about six positives, mostly N 16 to 80.
6. Does Shin 2025 (dose by difficulty) replicate outside one lab? Is there an equal-compute version for LLMs?
7. At what predictability and test budget does sleep-time compute stop paying? No single paper sweeps both.
8. Is the human conditioning null real or underpowered? Does the mouse substage flip replicate in humans?
9. Do sleep-inspired weight methods keep their gains against strong rehearsal baselines with variance reported? Behrouz and Auto-Dreamer report none.
10. Are the 2026 nulls (odour set, benefit spread over the learning context) a sign that benefit is not item-specific? If it spreads, a replay step in an LLM may help the whole context, not the chosen item.

## 11. Sources

[V] opened and read in this run (full text, or abstract page where noted). [M] snippet only or not opened. Status follows evidence_*.jsonl and critique.md.

**Human TMR**
- [V] Hu, Cheng, Chiu, Paller (2020) meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC7144680/ (a01-a06, a20, a26, a27; full text re-checked in critique)
- [M] Rasch, Buchel, Gais, Born (2007). https://pubmed.ncbi.nlm.nih.gov/17347444/ ; https://europepmc.org/article/MED/17347444 ; https://doi.org/10.1126/science.1138581 (primary text not opened; numbers via Hu's table)
- [V] Rudoy, Voss, Westerberg, Paller (2009). https://pmc.ncbi.nlm.nih.gov/articles/PMC2990343/ ([M] copy: https://europepmc.org/article/MED/19965421)
- [V] Cousins et al. (2014). https://pmc.ncbi.nlm.nih.gov/articles/PMC4244461/
- [V] Cousins et al. (2016), abstract-level. https://pmc.ncbi.nlm.nih.gov/articles/PMC4854410/
- [V] Cairney et al. (2014) emotional memory. https://pmc.ncbi.nlm.nih.gov/articles/PMC3954173/
- [V] Cairney et al. (2016) contingent on memory accuracy. https://pmc.ncbi.nlm.nih.gov/articles/PMC4835313/
- [V] Cairney et al. (2018) fast spindles and decoding. https://pmc.ncbi.nlm.nih.gov/articles/PMC5863764/
- [V] Hu et al. (2015) implicit social bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC4467959/
- [V] Henin et al. (2019) closed-loop acoustic stimulation. https://pmc.ncbi.nlm.nih.gov/articles/PMC6831893/
- [V] Closed-loop TMR at SO up vs down states (Sci Rep 2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6389952/
- [V] Cordi et al. (2014) REM odour. https://pmc.ncbi.nlm.nih.gov/articles/PMC4150443/
- [V] Purple, Sakurai, Sakaguchi (2017) mouse. https://pmc.ncbi.nlm.nih.gov/articles/PMC5388892/
- [V] Update on recent advances in TMR (npj Sci Learn 2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11018807/
- [V] Hoffman et al. (2024) awake TMR. https://pmc.ncbi.nlm.nih.gov/articles/PMC11868201/
- [V] Wick and Rasch (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10547374/
- [V] N2 vs SWS sound-word (Sci Rep 2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11032354/
- [V] Theta-tACS with TMR (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11036246/
- [V] SleepStim (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9649863/
- [V] Face-name TMR (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8755782/
- [V] Emotional arousal and TMR (Sci Rep 2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5159847/
- [V] Schreiner et al. (2021) endogenous reactivation. https://pmc.ncbi.nlm.nih.gov/articles/PMC8149676/
- [V] Closed-loop vocabulary at home, Dreem 2 (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12592824/
- [M] Creery et al. (2015). https://europepmc.org/article/MED/25845695
- [M] Oudiette et al. (2013) review. https://europepmc.org/article/MED/23433937
- [M] Hauner et al. (2013) fear extinction. https://europepmc.org/article/MED/24056700
- [M] Mouse V1 engram (2021). https://europepmc.org/article/MED/33619256
- [M] Dog TMR (2025). https://europepmc.org/article/MED/39933919
- [M] Odour-cued TMR (2026), europepmc copy. https://europepmc.org/article/MED/41656173
- [M] Cued once or five times (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12490198/
- [M] Difficulty in word learning (2024), europepmc copy. https://europepmc.org/article/MED/39495109
- [M] Memory reactivation not holistic (2024). https://europepmc.org/article/MED/38604779
- [M] Emotional memory in SWS and REM (2025), europepmc copy. https://europepmc.org/article/MED/40123003
- [M] Imagery rescripting plus closed-loop TMR (2024), europepmc copy. https://europepmc.org/article/MED/39695124
- [V] Zheng et al. (2024) mouse substage, abstract. https://pubmed.ncbi.nlm.nih.gov/39382074/
- [V] van der Heijden et al. (2024) PTSD, abstract. https://pubmed.ncbi.nlm.nih.gov/39116885/
- [V] Xia et al. (2024) aversive memory, abstract. https://pubmed.ncbi.nlm.nih.gov/39052838/
- [V] Suppress-tone TMR (Biol Psychol 2026), abstract. https://pubmed.ncbi.nlm.nih.gov/43000081/
- [V] Klaassen and Rasch (2024), abstract. https://pubmed.ncbi.nlm.nih.gov/39495109/
- [V] Odour-cued TMR (JSR 2026), abstract. https://pubmed.ncbi.nlm.nih.gov/41656173/
- [V] Odours plus sounds nullified (JSR 2026), abstract. https://pubmed.ncbi.nlm.nih.gov/41702567/
- [V] Word-meaning priming (Neuropsychologia 2025), abstract. https://pubmed.ncbi.nlm.nih.gov/40885484/
- [V] Once vs five times (Neuropsychologia 2025), abstract. https://pubmed.ncbi.nlm.nih.gov/40983248/
- [V] Week-old memories (NPJ Sci Learn 2024), abstract. https://pubmed.ncbi.nlm.nih.gov/39500927/
- [V] REM TMR disarming emotion (2025), abstract. https://pubmed.ncbi.nlm.nih.gov/41089190/
- [V] REM TMR late positive potential (2025), abstract. https://pubmed.ncbi.nlm.nih.gov/40575621/
- [V] Yuksel et al. (2025), abstract. https://pubmed.ncbi.nlm.nih.gov/40123003/
- [V] Shin et al. (2025) personalized TMR. https://arxiv.org/abs/2511.15013 ; https://arxiv.org/pdf/2511.15013 ; https://pubmed.ncbi.nlm.nih.gov/40691439/
- [V] Home closed-loop vocabulary (JSR 2025), abstract. https://pubmed.ncbi.nlm.nih.gov/39925332/
- [V] Closed-loop spindle TMR, motor (JSR 2026), abstract. https://pubmed.ncbi.nlm.nih.gov/42919667/
- [V] TMR and emotional memory modulation (Transl Psychiatry 2024), abstract. https://pubmed.ncbi.nlm.nih.gov/39695124/
- [V] PubMed TMR listing (title scan). https://pubmed.ncbi.nlm.nih.gov/?term=targeted+memory+reactivation
- [V] Dreamento toolbox (2023). https://arxiv.org/pdf/2207.03977

**Models and neural networks**
- [V] Lu, Foldes, Lewis (2024) CLS model of TMR. https://www.biorxiv.org/content/10.1101/2024.10.28.620229
- [V] Barry and Love (2022). https://discovery.ucl.ac.uk/10145147/1/bhac054.pdf
- [V] Sorrenti et al. (2023) WSCL. https://arxiv.org/pdf/2401.08623
- [V] Delanois et al. (2026) SRC. https://arxiv.org/pdf/2603.07867
- [M] Tadros et al. (2022). https://europepmc.org/article/MED/36522325

**Language models**
- [V] Lin et al. (2025) Sleep-time Compute. https://arxiv.org/pdf/2504.13171
- [M] Emergent Mind summary. https://www.emergentmind.com/papers/2504.13171
- [V] Behrouz et al. (2026) Language Models Need Sleep. https://arxiv.org/pdf/2606.03979
- [V] Lee et al. (2026) Do Language Models Need Sleep? https://arxiv.org/pdf/2605.26099
- [V] Xie (2026) SleepGate. https://arxiv.org/pdf/2603.14517
- [V] Shinde (2026) SCM. https://arxiv.org/pdf/2604.20943
- [V] Choi et al. (2026) IdleSpec. https://arxiv.org/pdf/2605.22154
- [V] Samuel et al. (2026) Studying Without a Syllabus. https://arxiv.org/pdf/2609.10824
- [V] Ye et al. (2026) Auto-Dreamer. https://arxiv.org/pdf/2605.20616
- [V] Zou (2026) Can an LLM dream? https://arxiv.org/pdf/2611.21648
- [V] Hu et al. (2026) ProAct. https://arxiv.org/pdf/2605.25971
- [V] Singh et al. (2026) Librarian Agents. https://arxiv.org/pdf/2610.22273
- [V] Semantic Scholar citations of Sleep-time Compute (title screen). https://api.semanticscholar.org/graph/v1/paper/arXiv:2504.13171/citations
- [V] arXiv exact-phrase search for TMR (gap note c20). https://export.arxiv.org/api/query?search_query=all:%22targeted+memory+reactivation%22
- [M] Wang and Sun (2025) PI-LLM, described second-hand through Xie 2026. https://arxiv.org/pdf/2603.14517
- [M] Hu et al. (2020) DOI. https://doi.org/10.1037/bul0000223

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 11 established claims: 10 confirmed as written, 1 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B04.04-K14** (reworded: the sources support less). All individual nulls check out (Wick and Rasch N=21+13, SleepStim Exp 1 N=61, face-name N=24, theta-tACS N=37, once vs five cues, odor 2026 N=32), but 'replicates poorly' is an unquantified summary of a hand-picked list: SleepStim Exp 2 (N=24) did find a benefit with limited sound intensity, Klaassen 2024 and the JSR 2026 studies found encoding-strength-dependent benefits, and Hu 2020 pools to a reliable g=0.29. Corrected claim: Several recent TMR studies report no overall cued benefit: SWS vs N2 cueing (N=34), SleepStim home TMR Exp 1 (N=61, though low-intensity cues helped and Exp 2, N=24, found a benefit), face-name (N=24, overall null but tracking N3 duration), theta-tACS plus TMR (N=37), cueing once vs five times (N=31), word-meaning priming, and odour-cued TMR 2026 (N=32), which suggests effects are fragile, but this is a selected list, not a replication rate (Hu 2020 pools to g=0.29).
