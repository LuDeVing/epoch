# Complementary learning systems: deep document

*Subfield B04.08. Written from evidence_a-d.jsonl (a01-a26, b01-b27, c01-c23, d01-d18), claims.jsonl (K01-K24) and critique.md. Evidence ids are in brackets. Many lines are the same paper read by different agents; independent counts are in claims.jsonl.*

## 1. What it is

Complementary learning systems (CLS) is a theory about why a learner needs two memory systems.

- A **fast** system stores single episodes with little overlap between them. In the brain this is the hippocampus.
- A **slow** system learns shared structure with small weight changes. In the brain this is the neocortex.
- The fast system **replays** stored traces to the slow system, mixed with other material. This interleaving lets the slow system learn without wiping out what it knows.

The core claim: if a shared-weight learner is trained on new material alone, it overwrites old knowledge. If new material is interleaved with old, it does not. [a01, a02, a03, b01, b02]

The key paper is McClelland, McNaughton and O'Reilly (1995) [a01]. The update is Kumaran, Hassabis and McClelland (2016) [b04-b06, b24].

Why it matters for our agent: our agent has frozen weights. It learns only by writing lessons (S9 LOOK BACK) into a store. The CLS question becomes: when a new lesson is written, how do we know it does not break old problems? The CLS answer is to test the new lesson against old problems before it is committed. This is a memory and guardrail question, not a training question.

State of the evidence in one paragraph. The weight-level result (replay prevents forgetting) is strong and well replicated in images, RL and LLM fine-tuning. The biology is real but the exact timing is contested. The explicit dual-memory networks (CLS-ER, FearNet, DualNet) have only self-reported gains. At the agent level (frozen weights, lessons in text), nobody has run the interleaved-replay test [d18, K22]. But 2026 papers show the damage it would prevent is large [d02, d03].

## 2. History and theories in depth

### 2.1 The problem: catastrophic interference

McCloskey and Cohen (1989) trained a back-propagation net on list AB, then list AC. After AC training the AB list was nearly wiped out, before AC even rose above 0% correct. Humans in Barnes and Underwood data still recall over 50% of AB after learning AC. [a02, b01, b21] McClelland et al. re-ran this simulation in 1995. McCloskey and Cohen's original was not opened by us; it is known only through the 1995 paper. [b21]

### 2.2 The 1995 theory

McClelland et al. asked why brains have both a hippocampus and a neocortex. Their answer has four parts. [a01, a04]

1. Cortical learning follows the gradient of error over all experiences. Small steps average over many cases. A large update from one case distorts what the net knows about others. [a04]
2. Reducing overlap between representations (sparser codes, French 1991) avoids interference. But it costs the ability to exploit shared structure. So the brain uses two systems instead. [b03]
3. The hippocampus binds single episodes quickly with sparse, non-overlapping codes.
4. Off-line reinstatement (sleep, rest) replays hippocampal traces to cortex, interleaved with other items. Cortex then learns slowly and safely.

The key simulation used Rumelhart's semantic net (500 epochs of base training on plant and animal facts) taught that penguins are birds that swim but cannot fly. [a03, b02]

- Focused learning (penguin facts only) learned the new fact fastest but damaged other animals. Birds got worse most. Fish improved slightly.
- Interleaved learning (penguin facts mixed with the base corpus) was slower but caused little damage.
- Same learning rate in both. Interference was the mean absolute error on 15 "can" items. Values are only in Fig 11, so there is no exact table.

Weak spot: the new facts were schema-inconsistent (penguins break the bird rule). This turned out to matter (see 2.4). [b02]

### 2.3 Graded retrograde amnesia and the decay model

If the hippocampus teaches the cortex over time, damaging it should hurt recent memories more than old ones. McClelland et al. fitted a two-compartment model to four studies. [a05-a09]

- Hippocampal trace decays at rate D_h per day. Replay happens at rate r times remaining strength. Cortex learns at rate C and decays at D_c.
- Table 1 (re-opened and confirmed in critique.md): D_h per day = 0.250 (Winocur, rats, social food preference), 0.050 (Kim and Fanselow, rats, fear), 0.035 (Zola-Morgan and Squire, monkeys, object discrimination), 0.001 (Squire and Cohen, human ECT patients, TV shows). [a08]
- Monkey net: learning rate 0.03, hippocampal decay 0.025 per day, reinstatement 0.1 per trial. A 16-16-16 net with 100 pairs reproduced the small monkey effect. Probability of retrieving at least one trace was 0.6 at the end of training and 0.47 for items learned just before. [a08, a09]
- Monkey study: 11 lesioned, 7 sham, 100 object pairs in 5 sets of 20, tested two weeks after surgery. The authors call this evidence weak and noisy (the 11-week point is anomalous). [a06]
- Five free parameters per study and four data sets. These are fits, not measured curves. [a08]

The decay rates differ by a factor of 250 across studies. So the time scale of consolidation is not a fixed constant.

Merzenich's focal dystonia report (repetitive practice narrowed cortical responses; interleaved practice corrected it) is a personal communication, not peer reviewed. [a10, b03]

### 2.4 Challenges and the 2016 update

Kumaran, Hassabis and McClelland (2016) took on two challenges and one extension. [b04-b06]

- **Fast inference within a session.** People infer across items never seen together (paired-associate inference, transitive inference) within one session. This looks like hippocampal generalisation, not slow cortical learning. The REMERGE model explains it by recurrent hippocampal activation. Both mechanisms may operate, depending on paradigm, amount of training and delay. [b05]
- **Schema-consistent learning can be fast.** Tse et al. (2007): rats with a learned flavour-place schema (six pairs, learned over weeks) learned two new pairs from a single exposure. A hippocampal lesion at 48 h spared the new memory; lesions at 3 h impaired it. In a novel arena, no fast learning. Tse 2011: plasticity gene expression in neocortex was higher 80 min after new pairs in the familiar arena. [b06, b22, b23, d16] The primary Tse papers were not opened.
- **Prioritised replay.** The hippocampus preferentially replays rare, salient events, so unusual lessons are not swamped by typical ones. Replay may be interleaved with cortex-consistent activity rather than faithful. Runaway reactivation may explain PTSD. [b04]
- The review maps DQN experience replay onto this account: interleaved past episodes feed a slow learner, prioritised by reward and surprise. This is an analogy, not a test. [b24]

Implication: the 1995 claim that integration must be slow and interleaved holds for schema-inconsistent material. For material that fits an existing schema, fast writing may be safe. This is claim K17 and it is contested. [K17]

### 2.5 The biology after 1995: how firm is the gradient?

Primary animal studies were opened in the gap search. [d15-d17]

- Anagnostaras, Maren and Fanselow (1999): rats with dorsal hippocampal lesions. Remote (50 day) context fear was spared; recent (1 day) was not. Exp 1: 29 rats (DH 14, sham 15; DH final n=11). Lesion x time F(1,24)=16, p<0.001. Peak freezing remote: sham 95.8, DH 96.6. Recent: sham 95.8, DH 71.6. Tone fear spared at both times. Only two delays, so the shape of the curve is unknown. [d15]
- Wiltgen et al. (2006): rats lesioned before training still learn context fear with enough trials. Five-delay design, sham n=17 to 26 per group, lesion n=17 to 26. Overall lesion effect F(1,185)=16.15. A slower non-hippocampal route exists. [d17]
- Squire et al. (2015) review: graded amnesia in monkeys, rats, mice, with gradients from days to months. But several labs report flat gradients (Lehmann 2007, Sutherland 2008, Sparks 2011, Broadbent and Clark 2013). Multiple-trace and transformation theories predict no sparing of detailed episodic memory. [d16]
- Result: the gradient is real in some paradigms, absent in others, and Table 1 rates are model fits. K02 is contested. [K02]

### 2.6 From theory to AI

- **Shin et al. (2017), deep generative replay.** First explicit CLS-inspired deep net. A generator (hippocampus-like) makes pseudo-samples of old tasks. A solver trains on new data mixed with them. No old data stored. MNIST solver chain, 5 generations, each trained only from the previous: 98.81, 98.64, 98.58, 98.53, 98.56%. Replaying random noise with old labels did not help. [a11]
- **Kirkpatrick et al. (2017), EWC.** A synaptic-consolidation analogue: slow weights that mattered for old tasks. Works on permuted MNIST and Atari (10 games in sequence), but fails in class-incremental settings. [a12, b07]
- **Kemker and Kanan (2018), FearNet.** Explicit fast store (kept exemplars), slow mPFC network trained during simulated sleep by pseudo-rehearsal, plus an amygdala-like gate. [a15, c09]
- **Arani et al. (2022), CLS-ER.** Working model plus fast and slow EMA copies. [a16, b10, c10]
- **Pham et al. (2021), DualNet.** Slow self-supervised learner plus fast supervised learner. [c11]
- **Hayes et al. (2021).** Review: AI mostly realises CLS as generative replay of past inputs. Few models have two-way hippocampus-cortex feedback. No explicit wake and sleep states. Procedural memories can consolidate without the hippocampus, so CLS is probably not the only model. [a17, b24, K18]
- **LLM era.** Rehearsal in instruction tuning (Scialom 2022), replay in continued pretraining (Ibrahim 2024), spurious forgetting (Zheng 2025), latent learning and episodic retrieval (Lampinen 2025), and agent-memory regressions (Zhang 2026, Hu 2026). See section 6.

## 3. Core findings with exact numbers

Status: established = several independent sources; single = one paper; contested = sources disagree. Ids refer to evidence lines; K ids to claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Sequential AB-AC training wipes AB in a back-prop net | AB near 0% before AC rises above 0%; humans keep above 50% | McClelland 1995 sim of McCloskey and Cohen 1989 [a02, b01] | single-source (K01) |
| Focused learning of penguin facts damages old knowledge; interleaved does not | Same learning rate; error averaged over 15 "can" items; values only in a figure | McClelland 1995 [a03, b02] | single-source (K01) |
| Graded retrograde amnesia exists | Context fear: 1 day lesion DH 71.6 vs sham 95.8; 50 days DH 96.6 vs sham 95.8; F(1,24)=16 | Anagnostaras 1999 [d15] | contested (K02): flat gradients in other labs |
| Table 1 hippocampal decay per day | 0.250, 0.050, 0.035, 0.001 (rats Winocur, Kim and Fanselow, monkeys, humans) | McClelland 1995 [a08] | model fits; design prior only |
| Schema-consistent pairs consolidate in 48 h | 6 learned pairs (weeks), 2 new pairs one trial; lesion at 3 h impairs, at 2 days spares | Tse 2007 via Kumaran 2016 [b06, b22] | contested (K17); primary not opened |
| Regularisation fails in class-incremental; replay works | Split MNIST Class-IL: none 19.90, EWC 20.01, SI 19.99, LwF 23.85, DGR 90.79, DGR+distill 91.79, iCaRL 94.57, offline 97.94 (20 seeds) | van de Ven and Tolias 2019 [a13, c08] | established (K03) |
| Same on permuted MNIST, Class-IL | EWC 25.04, Online EWC 33.88, DGR 92.19, DGR+distill 96.38, offline 97.59 | same [a13, c08] | established |
| Plain ER beats many specialised methods | Seq-CIFAR-10 Class-IL buffer 200: SGD 19.62, oEWC 19.49, SI 19.48, GEM 25.54, A-GEM 20.04, FDR 30.91, ER 44.79, iCaRL 49.02, joint 92.20 | Buzzega 2020 (DER) [a14] | established (K04) |
| Tiny memory is enough | One example per class gives 7 to 17% gains; ER over EWC/finetune about 15% at 1 per class, about 28% at 13 per class | Chaudhry 2019 [b09, c07] | established (K04) |
| Tuning explains much of the gap between replay methods | +51.2 points (CIFAR-10) and +26.9 (CIFAR-100) over plain ER, buffer 1000, from five fixes | Buzzega 2020b [d12] | single paper, same lab |
| Independent test: no clear winner | Split-CIFAR100 mem 2000: MIR 30.4, DER++ 29.9, ER-ACE 29.4; TinyImagenet mem 4000: MIR 22.7, DER++ 23.6, ER-ACE 21.3 | Soutif-Cormerais 2023 [d11] | replication; supports K04 |
| Logit matching on replay adds a little | MNIST-360 buffer 200: ER 49.27, DER 55.22, DER++ 54.16; buffer 1000: ER 75.18, DER 75.97 | Buzzega 2020 [a14, c12] | single-source (K05) |
| Dual-memory nets beat single-store replay (self-reported) | MNIST-360 buffer 200: CLS-ER 66.37 vs DER++ 54.16; buffer 500 75.70 vs 69.62; buffer 1000 79.54 vs 76.03; S-Tiny-ImageNet buffer 200 +176% over ER, +114% over DER++ | Arani 2022 [a16, b10] | single-source (K06); gap closes at large buffers (about 95.7 at buffer 5120) |
| FearNet vs iCaRL | Mean 0.923 vs 0.782; CIFAR-100 0.947 vs 0.749; CUB-200 0.891 vs 0.864; AudioSet 0.932 vs 0.733; oracle gate 1.002, 0.936, 0.972 | Kemker and Kanan 2018 [a15, c09] | single-source (K06) |
| Independent benchmark: all five mechanisms fall short | Dual-memory (GeppNet+STM) kept the base set but failed on new sessions | Kemker 2018 [b11] | replication, older nets |
| RL replay share | 50-50 near joint training; 75-25 and 100% replay also work; ablating behavioural cloning brings forgetting back. DMLab first-task column: separate 29.24, simultaneous 32.35, sequential 17.99, CLEAR 50-50 31.40, no BC 28.66 | Rolnick 2019 [b08, b25] | single-source (K19); column map inferred |
| Rehearsal in instruction-tuned LLM | 0% rehearsal: catastrophic loss; 0.25%: almost perfect stability; 1% (1,000 of 100,000 per task): zero-shot stationary; CT0 keeps 99.8% (T0pp) and 98.0% (T0 3B) of upper bound over 8 tasks, 70 datasets | Scialom 2022 [a18, b13, c03] | single-source (K08) |
| Generative replay diverges for LLM generation | LAMOL diverged from upper bound; fewer than 20% of 24,000 pseudo samples valid | Scialom 2022; Zheng 2025 [b26, d06] | contested (K07) |
| Self-synthesised rehearsal | Llama-2-7b, 10 SuperNI tasks, average result: no rehearsal 17.33, 1% random 60.64, 10% random 61.49, SSR 63.23, multitask 64.69 | Huang 2024 [a20] | single-source |
| Continual pretraining replay | 5% replay (weak shift), 25% (strong shift) plus LR re-warm and re-decay matches retraining at 405M and 10B; 50% replay saw 150B (SlimPajama) or 100B (German) fewer new tokens yet matched | Ibrahim 2024 [a21, b14] | single-source (K09); weights only |
| Forgetting rises with scale 1b to 7b in instruction tuning | BLOOMZ-7.1b 65.82 initial vs 60.61 after (7.15 drop); BLOOMZ-3b 63.90 vs 62.14 | Luo 2023 [a19, b12, c05] | contested (K11) |
| LoRA learns less, forgets less | Code CPT: best LoRA (rank 256) HumanEval 0.224 at 20B tokens; full finetune 0.218 at 4B, peak 0.263 | Biderman 2024 [a22, b15] | single paper |
| Sparse memory finetuning | NaturalQuestions F1 drop 89% full, 71% LoRA, 11% sparse | Lin 2025 [a23] | single preprint (K12) |
| Spurious forgetting | Old-task accuracy near 100% to about 10% in 150 steps; recovery to 96% by fine-tuning on half the old data or ten irrelevant instances; 20% replay and LAMOL do not remove the alignment drop | Zheng 2025 [b17, d05] | contested (K10) |
| Task inference skew | Alpaca ICL input drop: Leetspeak 1.0%, French 29.00%, English 56.75% | Kotha 2024 [b16, d07] | contested (K10) |
| Latent learning gap | Reversal curse: fine-tuning near zero, in-context near ceiling; oracle retrieval without ICL-supporting sequences about 12% (reversal) and about 6% (codebooks) | Lampinen 2025 [c01, c02, c23] | established (K13), but one group |
| Sleep-time compute | About 5x less test-time compute at equal accuracy; +13% (GSM-Symbolic), +18% (AIME); 2.5x lower per-query cost; SWE-Features only about 1.5x and worse at high budget | Lin 2025 [c19, d08, d09] | single-source (K16, K24) |
| Agent memory regresses solved problems | GPT-5.4 on a 19-problem ARC slice: 100% to 54%; 33 tasks: 58.5 (no memory), 55.1 (epoch 1), 38.5 (epoch 10) | Zhang 2026 [d02] | with d03 counts as established (K21) |
| Distilled rules hold less than stored experience | tau-bench banking: hold rate 0.65 distilled vs 0.88 stored experience; Mistral Large pass^1 0.103 none, 0.170 experience | Tablan 2026 [d03] | single paper (K21) |
| Memory-level interference in frozen agents | BabyAI: fine-grained per-step memory +15.0% forward, -10.0% backward; insight memory +3.5 BWT vs raw -4.0 | Hu 2026 [d01] | single-source (K20); conflicts with Zhang |
| Interference-based replay | MIR +2.8% accuracy and -2.5% forgetting on MNIST Split; MinImagenet ER 24.7 acc / 23.5 forgetting vs ER-MIR 25.2 / 18.0 | Aljundi 2019 [d13] | small effect; contested (K23) |
| Prioritised replay in RL | Beats uniform on 41 of 49 Atari games | Schaul 2016 [d14] | RL only |
| Reflection memory | Reflexion: 130 of 134 AlfWorld, +22% AlfWorld, +20% HotPotQA, +11% HumanEval, 91% pass@1 HumanEval vs 80% GPT-4 | Shinn 2023 [c17] | single-source (K15); loosely CLS |
| Eviction by net value | Memory 2.7x smaller, injection success 0.75 to zero | Wu 2026 [d04] | single preprint |

## 4. Mechanisms and models

Explained so an engineer can implement them. Weight-level first, then the agent-level translation.

### 4.1 Experience replay (ER), the workhorse

1. Keep a buffer of M stored examples from old tasks. Fill it by reservoir sampling or class-balanced selection. (Reservoir sampling evicts early classes when memory is tiny; it was 3.5% worse than K-Means selection in Chaudhry [b09].)
2. At each step, sample a batch of new data and a batch from the buffer.
3. Train on the union. Loss = loss(new) + loss(replay).
4. Replay share can vary widely. In RL, 50-50 works; 75-25 and 100% also work [b08]. In LLM instruction tuning, 0.25% to 1% of old data was enough [a18]. In continued pretraining the share depends on the size of the shift: 5% weak, 25% strong [a21].
5. Repeated passes over a tiny buffer do not overfit it; they can improve generalisation [b09].

### 4.2 Dark experience replay (DER / DER++)

Store the network's logits at the time each sample was seen. On replay, add a loss that matches current logits to stored logits (distilling the past model). DER++ adds a normal label loss on replayed samples. Gain over ER is small and shrinks with larger buffers. [a14, c12]

### 4.3 Generative replay (DGR, LAMOL, SSR)

1. Train a generator on each task. Train the solver on new data plus generator samples labelled by the old solver. [a11]
2. For LLMs: the model generates its own pseudo-inputs from few-shot demos (SSR), the latest model refines outputs, and diverse instances are kept. SSR matched real 1% rehearsal on Llama-2-7b [a20].
3. Failure mode: pseudo-sample quality. Fewer than 20% of 24,000 LAMOL samples were valid after filtering [d06]. Replaying random noise with old labels does nothing [a11].

### 4.4 Dual-memory networks

- **FearNet:** a fast store keeps recent exemplars. A slow network is trained during a "sleep" phase (every 10 study sessions) by pseudo-rehearsal from a generative autoencoder. A gate network decides which store to ask. Gate errors cost about 5 points on CIFAR-100. Uses ResNet-50 embeddings, not pixels. [a15, c09]
- **CLS-ER:** keep a working model W, a plastic model P and a stable model S. P and S are exponential moving averages of W; P is updated often, S rarely. On each step, sample the buffer, take logits from P and S for the replayed items, and add a consistency loss to W. Use S for inference. Gains vanish at large buffers. [a16, c10] Appendix, stable vs working vs plastic on P-MNIST: 75.22 / 63.09 / 71.32. [c10]
- **DualNet:** slow self-supervised representation learner plus fast supervised adapter. [c11]

### 4.5 Regularisation (the contrast)

EWC adds a penalty on weights, weighted by an estimate (diagonal Fisher) of their importance to old tasks. It works when task identity is given and fails in class-incremental settings (20.01%). [a12, a13]

### 4.6 Selecting what to replay

- **MIR:** pick buffer items whose loss would rise most after the proposed update (needs a gradient look-ahead). [d13]
- **Prioritised ER:** sample by TD error; needs bias correction. [d14]
- Both give small gains. An independent test found no clear winner. [d11]

### 4.7 Sparse and low-rank updates

LoRA limits the update to low rank; it learns less and forgets less. Sparse memory finetuning updates only the memory slots most activated by new facts relative to pretraining usage (TF-IDF ranking). [a22, a23] These do not apply to a frozen agent.

### 4.8 Agent-level translation (nothing here is tested)

| CLS part | Agent equivalent |
|---|---|
| Fast hippocampal store | Raw episodes: full solved problems with answers and reasoning, stored verbatim |
| Slow cortical learner | Distilled rules or lessons in the system prompt or skill store |
| Interleaved replay | Before committing a new lesson, re-run k stored old problems with the lesson in context and check they still pass |
| Sleep phase | An idle-time pass that re-derives and re-checks the lesson store (sleep-time compute) |
| Prioritised replay | Pick regression items most similar to, or most likely to conflict with, the new lesson |
| Schema gate | Write directly if the lesson fits an existing rule; replay-verify if it is novel |

Pseudocode for the proposed regression gate:

```
on new_lesson L:
    R = pick_regression_set(L, k)        # random or most similar solved problems
    base = pass_rate(R, store)           # cached from earlier runs
    new  = pass_rate(R, store + L)       # run in code, tokens counted
    if new >= base: commit L
    else: quarantine L (keep as raw episode, not as a rule)
```

Cost is k extra solves per lesson. This is what to measure at equal tokens.

## 5. What holds up

### 5.1 Holds up (replicated or checked by independent groups)

- **Replay beats regularisation in class-incremental learning.** van de Ven (20 seeds) agrees with Buzzega (SGD 19.62, oEWC 19.49, ER 44.79) and Kemker 2018. Regularisation fails without task identity. [a13, a14, b11] Established.
- **Small replay buffers are strong.** Chaudhry 2019, Buzzega 2020b (+51.2 and +26.9 points from tuning plain ER) and Soutif-Cormerais 2023 (no clear winner, tuned ER very competitive) agree. [b09, d11, d12] Established.
- **Tiny rehearsal works in instruction-tuned LLMs** (0.25% to 1%). Ibrahim cites Scialom: replay as small as 1% mitigates forgetting. [a18, c04] One paper for the main curve, so single-source.
- **Without replay or protection, LLMs and agents forget.** Luo (1b-7b), Scialom (0%), Zheng. [a18, a19, b17]
- **Stored raw episodes beat model-written abstractions** in two 2026 agent papers: Zhang (consolidated rules broke solved problems) and Tablan (hold rate 0.65 vs 0.88). [d02, d03]

### 5.2 Failures, contradictions and moderators

- **Dual-memory gains not reproduced.** Kemker 2018 (same first author as FearNet) found all five mechanisms fall short of offline training, and dual memory did not beat simpler ones. Soutif-Cormerais 2023 did not test CLS-ER, FearNet or DualNet. Buzzega 2020b shows baselines are often under-tuned. CLS-ER gains vanish at buffer 5120. [b11, d11, d12, a16]
- **Generative replay works on MNIST, fails on LLM generation.** DGR 90.79 on Split MNIST; LAMOL diverged on T0, and fewer than 20% of pseudo samples were valid. Different scale and domain. [a13, b26, d06]
- **Scale and forgetting.** Luo: forgetting rises from 1.1b to 7.1b; the authors suspect larger models simply start higher. Ibrahim: replay plus LR schedule matches retraining at 405M and 10B. Different setups. [a19, a21]
- **What forgetting is.** Zheng says it is lost task alignment, recoverable by training on half the old data or ten irrelevant instances. Kotha says it is task-inference skew, recoverable by changing the prompt. Zheng finds 20% replay does not remove the alignment drop. The mechanisms differ and no study compares them. [b16, b17, d05, d07]
- **Animal gradient.** Real in several paradigms (1 vs 50 days in Anagnostaras), flat in others (Lehmann 2007, Sutherland 2008, Sparks 2011, Broadbent and Clark 2013). Multiple-trace and transformation theories compete. [d15, d16]
- **Fast schema learning** (Tse 2007) contradicts the strictly slow 1995 account for schema-consistent items. [b06]
- **Abstraction: safe or harmful?** Hu 2026 finds abstract insights forget less (+3.5 vs -4.0 BWT, BabyAI). Zhang 2026 finds forced abstraction regresses solved problems. Different tasks and memory modules. Unresolved. [d01, d02]
- **Offline compute.** Sleep-time compute gave about 5x savings on rebuilt benchmarks but about 1.5x on SWE-Features, and was worse than test-time compute at high budgets. It depends on query predictability. [d08, d09]
- **Prioritised replay** helps a little in some settings; an independent benchmark found no clear winner. [d11, d13]

### 5.3 Interventions that worked

Replay of 0.25% to 1% of old data (LLM fine-tuning); 5% to 25% replay with LR re-warming (continued pretraining); tiny episodic memory (images); 50-50 replay with behavioural cloning (RL); gating consolidation with Retain/Delete/Consolidate (doubled accuracy over forced consolidation, Zhang [d02]); locking verified rules from edits (Tablan [d03]); pruning by net value (Wu [d04]).

### 5.4 Interventions that did not work

EWC/SI in class-incremental settings; replaying noise with old labels [a11]; 20% real replay for the alignment drop in Zheng [b17]; LAMOL pseudo-replay on T0 [b26]; 50% replay in pretraining (hurt adaptation to new data) [a21]; forced consolidation of lessons [d02].

## 6. Language models

### 6.1 Weight-level LLM results

- **Instruction tuning, T0.** 0% rehearsal: catastrophic loss of zero-shot ability. 0.25%: almost perfect stability. 1%: stationary. New tasks were learned equally well. CT0 reaches 99.8% (T0pp) and 98.0% (T0 3B) of upper bound after 8 tasks over 70 datasets, and the result is task-order invariant. [a18, b13] The authors argue stability comes from self-supervised pretraining. One paper.
- **Llama-2-7b on 10 SuperNI tasks.** Average result: no rehearsal 17.33; 1% random 60.64; 10% random 61.49; self-synthesised rehearsal 63.23; multitask upper bound 64.69. [a20]
- **Continued pretraining.** 405M models, hundreds of billions of tokens. Weak shift (Pile to SlimPajama) needs 5% replay; strong shift (English to German) 25%; confirmed at 10B. English averages within a 1.19 range (judged noise). [a21, b14]
- **Forgetting by scale.** Luo: BLOOMZ 1.1b to 7.1b forgets more with scale; decoder-only BLOOMZ forgets less than encoder-decoder mT0; general instruction tuning first reduces later forgetting. [a19, b12]
- **LoRA and sparse updates.** LoRA learns less and forgets less; full fine-tuning learns perturbations of rank 10 to 100 times higher. Sparse memory finetuning limited NQ F1 loss to 11% vs 89% full. [a22, a23]
- **Spurious forgetting.** In Zheng's synthetic dataset plus four real scenarios, damage occurs in the first 150 steps and is largely alignment loss. Freeze (bottom layers fixed) raised sequential fine-tuning accuracy from 11% to 44%. Gradient directions that undo alignment have average cosine similarity of only 0.4 across 10 trials. Ten epochs on 10 harmful examples moved LLaMa-2-7B-Chat safety from 0% back to about 99%. [b17, b27]
- **Task inference.** Kotha: fine-tuning skews which task the model infers; conjugate prompting (translation) recovers capability partly. Mostly synthetic. [b16, d07]

### 6.2 Latent learning and episodic memory

- Lampinen et al. (2025, co-author McClelland) show gradient-trained models fail to use information latent in training data. Reversal curse: fine-tuning near zero; in-context near ceiling. Augmenting fine-tuning with in-context inferences closes much of the gap (t > 149, p < 1e-16). [c01, c02, d10]
- A model with oracle episodic retrieval does better than baseline, but only about 12% (reversal) and about 6% (codebooks) without training sequences that teach context use. [c01, c23] These two figures belong to the latent-learning paper, not the generalisation paper (corrected in the gap search).
- Limit: synthetic data, models trained from scratch for the retrieval results, oracle retrieval. [c01]

### 6.3 Episodic and retrieval-based memories for frozen LLMs

- **HippoRAG** (hippocampal indexing, not CLS replay): up to 20% better than prior RAG on multi-hop QA; R@2 +11 and R@5 +20 on 2WikiMultiHopQA; about +3 on MuSiQue; 10-30x cheaper and 6-13x faster than IRCoT (an earlier line said 10-20x; corrected). Weaker on HotpotQA. [b19, c13] HippoRAG 2: +7% on associative memory; +9.5% F1 on 2Wiki and +3.1% on LV-Eval vs NV-Embed-v2. [c14] Same lab; weights never change; no forgetting test.
- **Larimar:** episodic memory on a frozen LLM; edits 4-10x faster than ROME/GRACE; near 100% rewrite accuracy up to 512 edits, 82% at 1024; two rephrases lift generalisation from 70.4% to 82.2%. Capacity is a hard limit. [c15]
- **Interactive continual learning:** ViT as System 1 and multimodal LLM as System 2 for hard examples; over 3% gain on ImageNet-R. Authors' own claim. [a25]

### 6.4 Agent-level results (frozen weights)

- **Hu 2026 [d01].** ReAct agent with ReMe memory, ALFWorld and BabyAI, 200 training instances per phase, 100 test. Frozen-weights agents still show interference, now as competition for the context window. Fine-grained per-step memory: +15.0% forward, -10.0% backward. Abstract insight memory: +3.5 backward vs -4.0 for raw. No replay arm.
- **Zhang 2026 [d02].** LLM rewriting of lesson banks: utility first rises, then falls, sometimes below no-memory. Even with ground-truth solutions, consolidation broke solved problems. GPT-5.4 on ARC-AGI Stream: a 19-problem slice went from 100% to 54%. Ten runs on 33 tasks solvable without memory: 58.5, 55.1 (epoch 1), 38.5 (epoch 10). Gated Retain/Delete/Consolidate doubled accuracy over forced consolidation. Episodic-only memory is competitive on WebShop, ALFWorld, AppWorld.
- **Tablan 2026 [d03].** Frozen model plus rule store on tau-bench banking, 97 tasks, 4 trials. Mistral Large pass^1: 0.103 none, 0.170 experience (32/97). Learning from outcome verdicts gave 1.6x and from corrections 2.6x the static-RAG baseline; 22 of 84 never-solved tasks converted. Hold rate: stored experience 0.88, distilled rules 0.65. Verified rules locked. Memory-vendor authors.
- **Wu 2026 [d04].** Value-minus-harm eviction: memory 2.7x smaller, uplink 2.4x, injection success 0.75 to zero. Replay-by-success alone can keep over-specific or adversarial entries.
- **Reflexion** [c17], **Generative Agents** [c16] (100 raters; full architecture vs prior-work condition d = 8.16; Kruskal-Wallis H(4)=150.29) and **MemGPT** [c18] (eviction at 70% context, summarising about 50%) are weight-free fast learners. None tests harm to old items.
- **Sleep-time compute** [c19, d08, d09]: precomputing inferences offline. 5x on rebuilt tasks; 1.5x on SWE-Features; worse at high budgets.

### 6.5 What changed behaviour, by how much

| Change | Effect |
|---|---|
| 0% to 0.25% to 1% rehearsal (T0) | catastrophic loss, then almost perfect, then stationary |
| Rehearsal vs none, Llama-2-7b, 10 tasks | 17.33 to 60.64 (1%) |
| Real 1% vs LAMOL pseudo-replay | 98.0-99.8% of upper bound vs diverged |
| Forced consolidation vs gated | gated doubled accuracy [d02] |
| Raw episodes vs distilled rules, hold rate | 0.88 vs 0.65 [d03] |
| Consolidation epochs 0 to 10 | 58.5 to 38.5 mean accuracy [d02] |

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = the lesson store written at S9. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Keep raw solved episodes; do not replace them with distilled rules alone.** Part: memory. [E]. Evidence: d02, d03 (two sources, different tasks); ER strength K04 [b09, d11, d12]. Rules are an index and a hint, not a replacement.
2. **Run a regression check before a lesson is committed.** Part: G (new guardrail candidate: no lesson commits without an old-problem check) plus S9. [E] for the need (K21: consolidation regresses solved problems; Scialom and Luo at weight level). The exact check design is untested (see Test first). Evidence: d02, d03, a18.
3. **Keep a small regression set of solved problems per class (1 to 5 exemplars).** Part: memory. [E] at weight level (K04: one example per class gives 7-17% gain). Transfer to the agent is the assumption. Evidence: b09, c07, d11, d12.
4. **Track backward transfer.** After every lesson batch, measure old-set accuracy (hold rate). Part: S9 and G7 (the schema must pay for itself). [E] as a metric: d01 and d03 both use it.
5. **Do not rely on "do not touch" flags alone.** Part: memory. [E] (K03: EWC 20.01 vs replay 90.79 in class-incremental). The analogy to prompts is weak, so use as a prior only. Evidence: a13, a14.
6. **Judge lessons on held-out problems of the class, not the problem that produced them.** This is already G3; CLS adds support. Evidence: d02.

### Test first (not established; see UNKNOWNS.md)

1. **Interleave k old problems at lesson-write time** (k = 1, 3, 5, 10). Part: S9 plus memory. No direct evidence; K22 is the gap. This is the key experiment.
2. **Schema gate:** write directly when the lesson fits an existing rule; replay-verify when novel. Part: S9. [C] K17; indirect support d02, d03.
3. **Real stored vs model-generated regression items.** Part: memory. [C] K07; weight-level only.
4. **Dose-response:** 0.25%, 1%, 5%, 25% replay in the lesson-write step. Part: memory. [S] a18, weight-level only.
5. **Re-cue before concluding a lesson conflicts.** If old performance drops after a lesson, re-run old problems with a re-cued prompt before demoting the lesson. Part: G (verify before commit). [C] K10.
6. **Offline consolidation pass (sleep-time compute)** between tasks, tokens counted. Part: memory/O. [S] K16, K24.
7. **Two-tier memory** (raw episodes plus distilled rules) vs one tier. Part: memory. [S] K06; gains self-reported.
8. **Prioritised regression picks** (most similar or most likely to conflict) vs random. Part: memory. [C] K23; expect a small effect.
9. **Context vs distilled summary on derived or reversed questions.** Part: memory/O (retrieve). [E] in weights (K13), untested for retrieval in agents.
10. **Provisional status for new lessons.** A new lesson stays provisional for N problems before it may override a rule. Part: memory. Design prior from the graded-amnesia fits, which are contested [K02]. Cheap to try.

Rejected for the agent (section 9): weight-level fixes (EWC, LoRA, sparse updates, LR re-warming), generative replay as default.

## 8. Concrete tests on our bench

All arms get equal total tokens (lesson writing plus regression checks counted against the same budget as the plain arm). Items come from the ARC and BRAINTEASER sets the harness already uses. Report hold rate on the old set and gain on the new lesson's class.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Sequences of 20 to 40 lessons written after solving problems; old solved set of 30 to 60 problems | (a) lesson committed as written; (b) re-solve k old problems per lesson, commit only if no regression, k = 1, 3, 5, 10 | Hold rate on old set after the sequence; gain on held-out new-class problems | (b) recovers a large share of the regression seen in Zhang (58.5 to 38.5); diminishing returns past k = 3 to 5. Effect size unknown |
| T2 | Same, k fixed at best value | random old problems vs most-similar old problems (embedding) vs most-recently-failed | Hold rate; lessons rejected | Small gain for similar-first (K23 expects small) |
| T3 | Lessons labelled by whether they fit an existing rule | uniform replay on all lessons vs schema gate (replay only novel ones) | Hold rate; tokens spent | Same hold rate at lower tokens if K17 holds |
| T4 | Lesson store with 50 lessons | distilled rules only vs raw episodes only vs both (two tiers) | Hold rate; pass rate on new problems | Both >= raw > rules (from d03: 0.88 vs 0.65) |
| T5 | Replay budget sweep | 0%, 0.25%, 1%, 5%, 25% of update tokens given to regression | Hold rate vs tokens | Steep at the low end (as Scialom); saturation by 5% |
| T6 | Regression set from real stored problems vs model-written imagined problems | two arms | Hold rate; fraction of imagined items valid | Real wins (K07; under 20% valid in LAMOL) |
| T7 | After a lesson causes a drop | (a) demote the lesson at once; (b) re-cue old problems (restate task and class) and re-test, then demote if still failing | False demotions; final hold rate | (b) recovers some drops if forgetting is partly spurious. Unknown size |
| T8 | Idle-time pass: derive implied inferences, reversals and derived rules from the store | with vs without pass; pass tokens counted | Accuracy on derived or reversed questions; net tokens | Helps on predictable queries only; may be near zero on ARC |
| T9 | Derived and reversed questions on stored facts | old lessons in context vs distilled rule | Accuracy on derived questions | In-context wins (Lampinen); depends on practice |
| T10 | New lessons enter a provisional tier | provisional for N = 0, 3, 10 problems before they can override | Hold rate; speed of learning | Small hold-rate gain, slower learning |

Controls: a no-memory arm and a raw-episode-only arm (it stayed competitive in d02). Run at least 5 seeds per cell; the 19-problem slice in d02 is too small to bound error.

## 9. What does not transfer, and why

- **Weight updates.** Our agent is frozen. EWC, LoRA, sparse memory finetuning, LR re-warming, 5% to 25% pretraining replay and logit matching all act on parameters. There is no gradient. [K09, K11, K12]
- **Catastrophic interference as such.** A text store does not overwrite itself the way shared weights do. What does happen is competition for context and rewriting by the model. Zhang and Hu show the symptom exists, but the mechanism is different: the damage comes from the lesson-writing LLM and from context limits, not from gradient steps. [d01, d02]
- **Replay percentages.** The 0.25% and 1% figures are fractions of fine-tuning data. A prompt has no such fraction. The equivalent is a token or problem budget, to be measured. [a18]
- **Brain timing.** Table 1 decay rates (0.250 to 0.001 per day) are model fits and span 250x. They cannot set a lesson's probation length. [a08, d16]
- **Sleep.** Hayes notes ML lacks wake and sleep states. Our agent has idle time, but there is no evidence that offline replay does more than give extra compute. The benefit seen is compute, not neural reactivation. [a17, d08]
- **Generative replay.** Works on MNIST, fails for LLM generation. An agent should store real problems. [K07]
- **Dual-memory networks.** CLS-ER's EMA copies are weight averages with no agent analogue. Only the idea of fast and slow tiers carries over. [a16]
- **Retrieval-index work (HippoRAG, Larimar).** Uses hippocampal indexing, not CLS interleaving, and tests QA and editing, not regression of old lessons. [b19, c15]
- **Image benchmarks.** MNIST, CIFAR and Tiny-ImageNet buffers (200 to 5120) have no counterpart in a lesson store of tens of items.
- **Reflexion-style loops.** They cover only the fast-learner half, with no old-item check. [c17]

## 10. Open questions

1. Does interleaving old problems at lesson-write time reduce regression in a frozen-weights agent at equal tokens, and what regression-set size per lesson is enough? Nobody has run it. [K22, d18]
2. Does a schema-consistency gate beat uniform replay? K17 is contested; the Tse primary papers are unread.
3. Real vs model-written regression items at the prompt level.
4. Dose-response of replay in a lesson store (0.25% to 25%).
5. Does an offline consolidation pass pay for its tokens beyond predictable queries?
6. Is forgetting in agents recoverable by re-cueing? Weight-level recovery is near 100% but needs training data; prompt-only recovery is partial (Alpaca 1.0% vs 56.75% drop). [d05, d07]
7. Can an independent group reproduce CLS-ER, FearNet and DualNet gains against well-tuned ER at equal compute? [d11, d12]
8. What practice teaches an agent to use retrieved context, given the oracle-retrieval figures of 12% and 6%? [c23]
9. Is abstraction safe (Hu: +3.5 BWT) or harmful (Zhang: 100% to 54%)? Probably depends on task and memory module. [d01, d02]
10. Does prioritised replay help rare, hard lessons more than uniform replay? Gains so far are small. [d13, d14]
11. How robust is graded retrograde amnesia to modern replications? Kim and Fanselow 1992 and Zola-Morgan and Squire 1990 were read only through secondary text. [d16]
12. The McCloskey and Cohen 1989 and Tse 2007 primaries were not opened.

## 11. Sources

[V] = opened and read this run (some through a fetch summary, noted). [M] = snippet or secondary reading only.

- [V] McClelland, McNaughton, O'Reilly (1995) Why there are complementary learning systems. https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf (a01-a04, a08, a09, b01-b03)
- [M] Kim and Fanselow (1992), read through the 1995 paper. https://stanford.edu/~jlmcc/papers/McCMcNaughtonOReilly95.pdf (a05)
- [M] Winocur (1990) and Zola-Morgan and Squire (1990), read through the 1995 paper. Same URL (a06)
- [M] Squire and Cohen (1979), read through the 1995 paper. Same URL (a07)
- [M] Merzenich on focal dystonia, personal communication (a10)
- [M] McCloskey and Cohen (1989). https://doi.org/10.1016/S0079-7421(08)60536-8 (b21)
- [V] Kumaran, Hassabis, McClelland (2016) What learning systems do intelligent agents need? https://web.stanford.edu/~jlmcc/papers/KumaranHassabisMcClelland16Final.pdf (b04-b06, b24; a26 was a cite-only line)
- [M] Tse et al. (2007) Schemas and memory consolidation. https://doi.org/10.1126/science.1135935 (b22, b23)
- [V] Shin et al. (2017) Deep Generative Replay. https://arxiv.org/abs/1705.08690 (a11)
- [V] Kirkpatrick et al. (2017) EWC. https://arxiv.org/abs/1612.00796 (a12, b07; c20 was a partial read)
- [V] van de Ven and Tolias (2019) Three scenarios for continual learning. https://arxiv.org/abs/1904.07734 (a13, c08)
- [V] Buzzega et al. (2020) Dark Experience for General Continual Learning. https://arxiv.org/abs/2004.07211 (a14, c12; table columns partly inferred)
- [V] Buzzega et al. (2020) Rethinking Experience Replay: a Bag of Tricks. https://arxiv.org/abs/2010.05595 (d12)
- [V] Kemker and Kanan (2018) FearNet. https://arxiv.org/abs/1711.10563 (a15, c09)
- [V] Kemker et al. (2018) Measuring Catastrophic Forgetting in Neural Networks. https://arxiv.org/abs/1708.02072 (b11)
- [V] Arani, Sarfraz, Zonooz (2022) CLS-ER. https://arxiv.org/abs/2201.12604 (a16, b10, c10)
- [V] Pham, Liu, Hoi (2021) DualNet. https://arxiv.org/abs/2110.00175 (c11; DualNet rows not captured)
- [V] Hayes et al. (2021) Replay in Deep Learning. https://arxiv.org/abs/2104.04132 (a17)
- [V] Rolnick et al. (2019) Experience Replay for Continual Learning (CLEAR). https://arxiv.org/abs/1811.11682 (b08, b25, c06; table mapping inferred)
- [V] Chaudhry et al. (2019) On Tiny Episodic Memories. https://arxiv.org/abs/1902.10486 (b09, c07)
- [V] Aljundi et al. (2019) Maximally Interfered Retrieval. https://arxiv.org/abs/1908.04742 (d13)
- [V] Schaul et al. (2016) Prioritized Experience Replay. https://arxiv.org/abs/1511.05952 (d14)
- [V] Soutif-Cormerais et al. (2023) Comprehensive evaluation of online continual learning. https://arxiv.org/abs/2308.10328 (d11)
- [V] Scialom, Chakrabarty, Muresan (2022) Fine-tuned Language Models are Continual Learners. https://arxiv.org/abs/2205.12393 (a18, b13, b26, c03, c21)
- [V] Luo et al. (2023, v5 2025) Catastrophic forgetting in LLMs during continual fine-tuning. https://arxiv.org/abs/2308.08747 (a19, b12, c05, c22)
- [V] Huang et al. (2024) Self-Synthesized Rehearsal. https://arxiv.org/abs/2403.01244 (a20, b18; partial table)
- [V] Ibrahim et al. (2024) Simple and Scalable Strategies to Continually Pre-train LLMs. https://arxiv.org/abs/2403.08763 (a21, b14, c04)
- [V] Biderman et al. (2024) LoRA Learns Less and Forgets Less. https://arxiv.org/abs/2405.09673 (a22, b15)
- [V] Lin et al. (2025) Continual Learning via Sparse Memory Finetuning. https://arxiv.org/abs/2510.15103 (a23; abstract)
- [V] Zheng et al. (2025) Spurious Forgetting in Continual Learning of Language Models. https://arxiv.org/abs/2501.13453 (b17, b27, d05, d06)
- [V] Kotha, Springer, Raghunathan (2024) Understanding catastrophic forgetting via implicit inference. https://arxiv.org/abs/2309.10105 (b16, d07)
- [V] Gutierrez et al. (2024) HippoRAG. https://arxiv.org/abs/2405.14831 (a24, b19, c13)
- [V] Gutierrez et al. (2025) From RAG to Memory (HippoRAG 2). https://arxiv.org/abs/2502.14802 (c14)
- [V] Das et al. (2024) Larimar. https://arxiv.org/abs/2403.11901 (c15)
- [V] Qi et al. (2024) Interactive Continual Learning: Fast and Slow Thinking. https://arxiv.org/abs/2403.02628 (a25)
- [V] Lampinen et al. (2025) Latent learning: episodic memory complements parametric learning. https://arxiv.org/abs/2509.16189 (c01, c23)
- [V] Lampinen et al. (2025) On the generalization of language models from in-context learning and finetuning. https://arxiv.org/abs/2505.00661 (b20, c02, d10)
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442 (c16)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c17)
- [V] Packer et al. (2023) MemGPT. https://arxiv.org/abs/2310.08560 (c18)
- [V] Lin et al. (2025) Sleep-time Compute. https://arxiv.org/abs/2504.13171 (c19, d08, d09)
- [V] Hu, Long, Wang (2026) When Continual Learning Moves to Memory. https://arxiv.org/abs/2604.27003 (d01)
- [V] Zhang et al. (2026) Useful Memories Become Faulty When Continuously Updated by LLMs. https://arxiv.org/abs/2605.12978 (d02)
- [V] Tablan, Taylor, Bernhem (2026) Learning on the Job. https://arxiv.org/abs/2607.22157 (d03)
- [V] Wu et al. (2026) Forget to Improve. https://arxiv.org/abs/2606.25115 (d04)
- [V] Anagnostaras, Maren, Fanselow (1999) Temporally graded retrograde amnesia of contextual fear. https://pmc.ncbi.nlm.nih.gov/articles/PMC6782148/ (d15; fetch summary)
- [V] Squire, Genzel, Wixted, Morris (2015) Memory consolidation. https://pmc.ncbi.nlm.nih.gov/articles/PMC4526749/ (d16; fetch summary)
- [V] Wiltgen et al. (2006) Context fear learning in the absence of the hippocampus. https://pmc.ncbi.nlm.nih.gov/articles/PMC6675287/ (d17; fetch summary)
- [M] Gap search negative result on agent-level interleaved replay (d18; limited tools, not exhaustive)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 4 established claims: 4 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

