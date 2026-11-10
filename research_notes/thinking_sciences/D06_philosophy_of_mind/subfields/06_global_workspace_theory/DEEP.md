# Global workspace theory: deep document

*Subfield D06.06. Sources: evidence_a-d.jsonl (ids a01 to d21), claims.jsonl (K01 to K23), critique.md in this folder. Numbers were checked against the full text where the evidence line says opened:true. Items not re-opened are marked in section 11.*

## 1. What it is

Global workspace theory (GWT) says the mind has many parallel specialist processors that work without awareness. They compete for access to one small, shared workspace. The winner is made available ("broadcast") to all the specialists at once. Conscious content is what is in the workspace. Routine, well-practised tasks run in the specialists alone. Novel, effortful, error-prone tasks need the workspace (a01, a02, K01).

There are two main versions.
- **Cognitive version (Baars 1988).** A theatre or blackboard metaphor. A limited-capacity stage, a spotlight of attention, and an audience of unconscious experts (a12, b16; book not opened, no numbers).
- **Neuronal version (Dehaene, Changeux, and colleagues; "GNW" or GNWT).** The workspace is a network of long-range neurons, mostly in prefrontal and parietal cortex. Access is "ignition": a sudden, self-sustaining, all-or-none activation of that network at about 250 to 300 ms after a stimulus (a05, b07).

Why it matters for our agent. The theory is an architecture analogue for what our schema already does in code: many candidate thoughts, one chosen item, one item broadcast to the next step. Our code is the workspace. The model fills slots; code selects (G5) and decides transitions. GWT supports the design as a metaphor. It does not, by itself, show that the design pays off in tokens. The key finding of this review (K16) is that no study tests a small k-item bottleneck with one broadcast item on LLM reasoning at equal tokens. That test is ours to run.

Plain warnings for the reader:
- The human evidence is about consciousness (what is seen, what is reported). Our agent has no need for consciousness. Only the information-flow architecture matters.
- Almost every "established" claim here is human neuroscience. Most LLM and AI numbers are single-source.

## 2. History and theories in depth

**1988, Baars.** A Cognitive Theory of Consciousness. Proposes the global workspace as a functional architecture: specialist processors, a limited-capacity broadcast, contexts that shape what wins. We did not open the book (a12, b16). Its claims reach us only through Mashour et al. (2020) and Butlin et al. (2023).

**1998, Dehaene, Kerszberg, Changeux (a01 to a04).** The founding neural model. Two spaces. Space one: many specialist processors of five classes (perceptual, motor, long-term memory, evaluation, attention). Space two: one workspace of long-range neurons. Only one "workspace representation" can be active at a time. Global modulation by vigilance signals: awake means workspace on, slow-wave sleep means off. A simulated Stroop task ran 200 trials, with the new task introduced after trial 20. Routine tasks (colour naming, word naming) needed no workspace. The effortful task (colour naming with word interference) did need it. An error trial triggered intense workspace reactivation. The vigilance rule: after a correct answer V falls by 0.1 V; after an error V rises by 0.5(1-V). Weights are bounded 0 to 7. A stable pattern was found after about 5 to 50 trials. It is a toy network on one task. The authors call it partial and incomplete. It made predictions but did not fit human data.

**2001 to 2011, Dehaene and Changeux.** Experimental and theoretical approaches to conscious processing (a22, not opened). The key empirical idea: a nonlinear threshold. Below it, activity stays local. Above it, activity ignites and spreads (a21 Sergent 2005, not opened).

**2007 to 2009, the ignition evidence.** Masking studies in humans (a13, a14, a15). Details in section 3.

**2014, Pitts.** The first strong challenge. The P3b (a late wave) may reflect report and task demands, not access (a16, b12).

**2020, Mashour, Roelfsema, Changeux, Dehaene (a05 to a11, b07, b08).** The consolidated review. Divergence of seen from unseen trials at about 200 to 300 ms; the first 200 ms can be fully preserved on unseen trials. Working memory is the attended item in the workspace; focus capacity is one item, with a few more outside the focus. Dual task can delay access by more than 300 ms. Retro-cues work up to 900 ms. Disorders of consciousness, anaesthesia and sleep are explained as loss of broadcast.

**2021, VanRullen and Kanai (a24, b20, c07).** "Deep learning and the global workspace theory." A roadmap for building a workspace into deep nets via a shared latent space. No experiments.

**2022, Goyal et al. (a23, b17, c01 to c04).** The first deep-learning implementation: a shared workspace of a few memory slots, written by competition among specialist modules, read by broadcast. Details in sections 3 and 4.

**2023, Butlin, Long, Elmoznino et al. (a26 to a28, b23, c09 to c12).** Turn GWT into four indicators for AI: GWT-1 parallel specialised modules; GWT-2 a limited-capacity workspace that forms a bottleneck; GWT-3 global broadcast to all modules; GWT-4 state-dependent attention (the workspace can query modules in sequence for complex tasks). They find plain Transformers fail (the residual stream has the same width as the input, so it is not clearly a bottleneck). The Perceiver arguably meets GWT-1, GWT-2 and the first part of GWT-4. No current system meets all four. They suggest a leaky integrator with a slow timescale to mimic sustained broadcast.

**2023 to 2025, the Cogitate adversarial collaboration (a18 to a20, b01 to b05, d04, d05).** The biggest preregistered test of GNWT against integrated information theory. Details in section 5.

**2024, Goldstein and Kirk-Giannini (b24, c13, c26).** Argue that language agents (LLMs with memory, planning, perception modules) may satisfy GWT, because a central workspace could be added with small changes. This is philosophy, not measurement.

**2026, Anthropic "J-space" (c15 to c19, d01 to d03).** A vendor interpretability study claiming Claude models carry a small, capacity-limited workspace-like subspace. Details in section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Seen rate is nonlinear in masking delay; objective and subjective thresholds match | N=12; SOAs 16-100 ms; seen vs SOA F(5,55)=154.17; objective threshold mean 40.8 ms (SD 12.4); subjective vs objective r^2=0.747, slope 1.03 | Del Cul et al. 2007 (a13) | Established (small N, one paradigm) |
| Seen and unseen trials diverge late; early activity preserved | At SOA 50 ms divergence from about 270 ms; review: divergence at about 200-300 ms | a13, Mashour 2020 (a05) | Established |
| Masked words drive short local activity; unmasked drive long, late activity | N=10 patients; masked d'=0.02; effect duration 60 vs 378 ms; onset 366 vs 522 ms; beta synchrony 300-500 ms, t(1,282)=7.12 | Gaillard et al. 2009 (a14) | Established (patients, exploratory band) |
| Global effect needs attention | Exp 1 N=11 counting: global effect 260-700 ms; Exp 2 N=11 mind-wandering: gone beyond 400 ms; Exp 3 N=10 visual task: none; minimally conscious 3 of 4 showed it, vegetative 0 of 4 | Bekinschtein et al. 2009 (a15) | Established for tested paradigms; later work reports some effects without attention (not read) |
| Audibility ratings are bimodal near threshold; reports predicted from 250 ms | N=20 analysed; single-trial AUC above 0.75 from 250 to 700 ms | Sergent et al. 2021 (b11) | Established (auditory, small N) |
| Late P3b is not necessary for awareness | Masking, 18 analysed; only CIN, SEC and VAN present in aware and absent in unaware, regardless of task; P3b at about 380-480 ms only when task-relevant | Pitts et al. 2014 (a16, b12) | Established |
| Meta-analysis: VAN and P3b track awareness, P3b vanishes when task-irrelevant | 117 studies, 547 seen effect sizes; VAN SMD 0.37 [0.32, 0.43]; P3b 0.49 [0.41, 0.57]; P3b task-irrelevant -0.12 [-0.47, 0.23] | Hutchinson et al. 2026 (d20, b14) | Single-source (abstract only) |
| No-report masking: awareness around 250-300 ms | Mask delays 17, 33, 50, 67, 83 ms: never seen at two shortest, always at two longest, 50% at 50 ms | Stillman et al. 2024 (b13) | Single-source |
| Working memory without awareness possible | N=17 MEG; seen trials 69.1% correct (SD 17.4), chance 5%; seen vs unseen F(1,16)=198.5; 13 of 17 above-chance on unseen | Trubutschek et al. 2017 (a17) | Single-source; fits activity-silent storage |
| Cogitate: no PFC offset ignition | N=256 (fMRI 120, MEG 102, iEEG 34); 0 of 655 PFC electrodes with onset plus offset; 194/657 posterior and 123/655 PFC responsive; 25/657 posterior tracked duration | Cogitate 2023 preprint and 2025 Nature (a18, a19, d05) | Contested |
| Cogitate: PFC adds nothing to category decoding | Adding PFC: iEEG BF01 1.94e4 and 1.91e5; MEG 3.05 and 4.70; orientation absent in PFC iEEG (BF01 5.11-8.65); iEEG face vs object PFC about 70% vs posterior over 95% | Cogitate 2025 (b02, d04) | Established (published text re-read); the theory verdict is contested |
| Cogitate: connectivity prediction | Preregistered: supported neither theory (iEEG BF01 2.62-5.32); exploratory connectivity consistent with GNWT | Cogitate 2025 (d04, a20) | Contested |
| Shared workspace in a transformer: tiny gain | CATER Top-1/Top-5: Transformer 70.83/87.8; hard workspace 71.07/88.6; soft 71.33/88.3; ISAB 65.3/83.6 (SD about 0.44) | Goyal et al. 2022 (a23, b17, c02) | Single-source; within noise |
| Workspace size is nonmonotone (bouncing balls) | SCOFF baseline ARI 0.276. With workspace: 2 slots 0.154; 4: 0.487; 5: 0.915; 8: 0.891; 10: 0.351 | Goyal 2022 (c03) | Single-source, one task |
| Atari transfer | 36 game pairs; median ratio vs RIMs 1.13 and 1.11 (means 1.16, 1.15) | Goyal 2022 (c04) | Single-source |
| Workspace router chains operations | One-hot addition 100%; MNIST-image version 90.0%; toy | Chateau-Laurent and VanRullen 2025 (c05) | Single-source, toy |
| GW agent beats GRU in audiovisual navigation | About 80% vs just over 60% (from plots); sizes 32-512 all similar; random 0%; original SAVi RL agent 25%; 5 seeds | Dossa et al. 2024 (b21, c08, d15) | Single-source |
| Semi-supervised GW translation | 6x less paired data (N=5,000 vs 30,000); 4.5x on captions; ImageNet probe 55.7 +/- 0.2 vs 50.3 +/- 0.2 | Devillers et al. 2024 (a25, d16) | Single-source (same group) |
| Generative agents ablation | TrueSkill: full 29.89 (sd 0.72); no reflection 26.88; no reflection or planning 25.64; crowdworkers 22.95; none 21.21; 100 raters | Park et al. 2023 (c21) | Single-source; believability, not accuracy |
| Claude "J-space" capacity | At most 25 J-lens vectors; never above 10% of activation variance (median 6-7%) | Anthropic 2026 (c15, d01) | Single-source, vendor |
| J-space causal swaps | Top-5 hit 59% (J component) vs 88% (pure lens) vs 5% (non-J); multi-hop swaps 54/70/70% (Haiku, Sonnet, Opus 4.5; 50 prompts) | c16, d02 | Single-source |
| J-space broadcast heads | Ablate top 1%: recall@25 0.86 to 0.67; injected-thought report 0.54 to 0.09 | c18, d03 | Single-source |
| Reflection fine-tuning | Fabrication 0.25 to 0.07 (27 transcripts); deception 0.38 to 0.05 (100 scenarios) | c19 | Single-source; fine-tuning, not scaffold |
| Context length alone hurts | 13.9% to 85% accuracy drop within limit, 5 LLMs, persists with masked tokens; recitation up to 4% on RULER | Du et al. 2025 (d10) | Single-source (abstract) |
| Fixed-size overwrite memory in LLMs | 1,024-token memory, 8K window, under 5% loss out to 3.5M tokens; over 95% on 512K RULER; memory 256-4,096 robust | MemAgent (d11) | Single-source; RL-trained |
| Selection saves tokens, not accuracy (blackboard) | Control unit: MMLU 85.17 at 5.07M tokens vs 85.52 at 18.83M without; marking not deleting stale messages 84.38 | LbMAS (d07) | Single-source |
| Keep-few-and-prune search | Game of 24: ToT b=5 74% vs CoT best-of-100 49% at 5.5k vs 6.7k tokens; b=1 45% | Tree of Thoughts (d09) | Single-source here |
| Context curation | WebArena 36.4 to 41.2% with 8.8% fewer tokens; DeepSearch 57.1 vs 53.9 with about 8x fewer tokens | Li et al. 2026 (d12) | Single-source, preprint |
| GWT-labelled LLM agent | BIGMAS on DeepSeek-V3.2, N=100: Game 24 25.0/26.0/30.0/36.0 (base/ReAct/ToT/BIGMAS); Six Fives 12/18/25/30; Tower of London 6/10/18/20 | Hao et al. 2026 (d13) | Single-source; no token match |

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it.

### 4.1 Classic GWT loop (Baars, Dehaene 1998)
1. A pool of specialists runs in parallel on the input. Each emits a candidate with a salience score.
2. A competition picks one winner. In the 1998 model this is gated activation among workspace neurons; only one workspace representation is active.
3. The winner is written into the workspace and broadcast to all specialists. Each specialist may update.
4. Vigilance: a scalar V controls whether the workspace opens. After a correct answer V falls by 0.1 V. After an error V rises by 0.5 (1 - V). This opens the workspace after errors and lets routine tasks run without it (a01).
5. Routine tasks never open the workspace. Effortful ones do. Implementation: the gate in S0 and the doubt rule G1 already match this.

### 4.2 Ignition as a threshold (a13, b11, b13)
Model access as a bifurcation. Evidence accumulates; above a threshold the state flips to a self-sustaining "accessed" state and below it decays. Visibility ratings are bimodal, not graded. Implementation: a hard accept or reject step. A candidate is either committed or not. No weighted blending.

### 4.3 Shared workspace with slot attention (Goyal 2022, a23, c01)
- Workspace is a small memory of nm slots (say 2 to 10).
- Write: specialists compete by attention for write access to slots. Two versions: hard competition (top-k) and soft.
- Read: every specialist attends to the slots (broadcast).
- Cost is near constant in the number of specialists, not quadratic as in pairwise attention.
- Trade-off: too few slots lose information, too many dissolve the bottleneck (bouncing balls: ARI 0.154 at 2 slots, peak 0.915 at 5, 0.351 at 10).

Engineering reading for an LLM agent: a fixed-size, code-managed "state" block of k items. Write by code-ranked competition among candidates. Read by pasting the state into each next prompt.

### 4.4 Global latent space with translation (VanRullen and Kanai; Devillers 2024)
A shared latent space links modality-specific encoders. Training uses a small paired set plus cycle-consistency on unpaired data (a25, d16). This is representation learning. It does not map to our scaffold (section 9).

### 4.5 Router that chains specialists (Chateau-Laurent and VanRullen 2025, c05)
A learned router picks which module reads and writes the workspace next. Loss over T=20 steps rewards answering early. Maps to S6 operator choice, but it is a toy.

### 4.6 Butlin indicators as a spec (c09, c11, c12)
- GWT-1: parallel specialist modules. In our agent: independent attempts in S3.
- GWT-2: limited-capacity workspace. In our agent: a carried state block (does not yet exist as a fixed-size block).
- GWT-3: global broadcast. In our agent: the selected item is pasted into every later call.
- GWT-4: state-dependent attention, so the workspace can query modules in sequence. In our agent: code routing between states.

A leaky integrator with slow timescale can imitate sustained broadcast: keep the selected item for several steps with a decay unless refreshed.

### 4.7 Cognitive tick proposal (Theater of Mind, c14)
Per tick: generators propose, a critic scores each from -5 to +5, one winner is broadcast, generator temperature rises when thought diversity H(W) is low: Tgen = Tbase + alpha*exp(-beta*H(W)). Parameters unspecified; no experiments. Treat as a design sketch only.

### 4.8 J-space in a transformer (c15 to c19)
Authors project activations onto a "J-lens" (token-vocabulary directions). The verbalizable part is a sparse subspace: at most 25 vectors, at most 10% of variance. Broadcast heads (top 1%) copy this content into later layers. Ablating them hurts. The mechanism is inside one forward pass and not recurrent. For us it is a measurement of what a model carries, not a recipe.

## 5. What holds up

**Holds up (human).**
- A late, nonlinear divergence between seen and unseen at about 200 to 300 ms, with preserved early processing. Several lines agree: Del Cul 2007, Bekinschtein 2009, Sergent 2021, Stillman 2024, plus the review (K02).
- The late global effect needs attention in the tested paradigms (Bekinschtein 2009, a15).
- Task-irrelevant stimuli lose the P3b (Pitts 2014; meta-analysis -0.12 [-0.47, 0.23]); the earlier VAN or N2 persists. So late sustained activity may reflect report, not experience (K03). This is partly a loss for the ignition claim.

**Failed or contested.**
- Cogitate (N=256, preregistered). Two GNWT predictions failed: no sustained or offset ignition in PFC (0 of 655 electrodes with onset-and-offset profile) and PFC does not carry fine detail (orientation not decodable; adding PFC to category decoding gives no gain). Prediction 3 (connectivity) supported neither theory (BF01 2.62 to 5.32). The preprint reading that category decoding supports GNWT was superseded by the published text (d04, K05). Caveat: the iEEG N is 34 in text, 29 for decoding, and Figure 1f lists 32 in the preprint (critique).
- The GNWT camp (Naccache et al. 2025, b05, b06) replies: the ignition window is 200 to 800 ms; stimuli lasted 500 to 1500 ms; no visible versus invisible contrast was run, so the core contrast was not tested; PFC coding is mixed and hard to decode; decoding also works for non-conscious stimuli. No consensus verdict (K04, K06). Status: contested.
- Working memory without awareness (Trubutschek 2017): 13 of 17 above chance on unseen trials, so the workspace may not be the only store. Fits activity-silent storage.

**Moderators.** Task relevance, attention, report requirement, modality, mask timing, number of patients.

**AI side.** Nothing replicated.
- Goyal CATER gains (71.07 vs 70.83, SD 0.44) are within noise. Only the bouncing-balls task shows a large effect, and the slot count was tuned.
- Dossa: the GW agent beat a GRU, but larger workspaces did not help, and the authors say SAVi is not a good working-memory benchmark. No replication.
- Devillers: only extensions by the same group.
- Park: believability, several components removed at once.
- BIGMAS and CogniPair carry a GWT label but have no matched no-workspace control. A practitioner memory runtime says its benchmarks prove no reasoning gains (d18).

**Interventions that worked (in adjacent systems).**
- Keep-few-and-prune search at about equal tokens: ToT b=5 74% vs best-of-100 49%.
- Selection of who acts in a blackboard system: about 3x fewer tokens, same accuracy.
- Context curation: 3 to 5 points with fewer tokens on one frontier model.

**Did not work or no effect shown.**
- Larger workspaces (Dossa flat from 32 to 512).
- Marking stale messages instead of deleting them (84.38 vs 85.17 MMLU).
- Length alone: hurts (Du 2025).
- Interior optimum of workspace size for LLM agents: not found (K21). Blackboard rounds are noisy (GPQA 52.0, 54.0, 53.0, 51.0 at 2/4/6/8 rounds).

## 6. Language models

**What exists.**
1. **Anthropic J-space (2026; vendor only).** Sonnet 4.5 main, Haiku 4.5 and Opus 4.5 corroborate. Occupancy plateaus near 25 items (median). Unrelated word lists: about six words present at a comma, 1 to 2 at a single layer. Arithmetic (4 + 17) * 2 + 7: 21, 42, 49 surface in order. Category switches clear the old category within a few words. Causal swaps work 54%, 70%, 70% (Haiku, Sonnet, Opus) over 50 prompts. Ablating the top 1% of broadcast heads cuts recall@25 from 0.86 to 0.67 (random heads keep 0.86) and the injected-thought report rate from 0.54 to 0.09. Reflection fine-tuning on 10,000 prompts: fabrication 0.25 to 0.07, deception 0.38 to 0.05; ablating the implanted vectors brings them back (0.22 and 0.23). Limits: single-token lens, one vendor, not replicated, fine-tuning not scaffolding, about 200k of 336k characters read. The authors do not claim the full GWT architecture.
2. **Context length hurts (Du 2025).** Accuracy falls 13.9% to 85% with longer input even when irrelevant tokens are masked. Recitation helps up to 4% on RULER.
3. **Fixed memory (MemAgent).** 1,024-token memory, rewritten each chunk, RL-trained. Under 5% loss at 3.5M tokens. Memory size 256 to 4,096 robust. Retrieval QA, not reasoning.
4. **Blackboard systems (LbMAS, Salemi).** Selection and deletion cut tokens about 3x with accuracy within noise (MMLU 85.17 vs 85.52). Salemi beat RAG and master-slave at about 2.3x and 1.8x cost on KramaBench-type tasks. The blackboard is open to all agents, so there is no one-item bottleneck.
5. **Search (Tree of Thoughts).** Keep 5, prune: 74% at 5.5k tokens vs CoT best-of-100 49% at 6.7k. b=1 gave 45%. Crossword without pruning was worse; without backtracking 20% word-level. This favours hard selection of a few, but has no soft-mixing arm.
6. **Context curation (Li 2026).** WebArena 36.4 to 41.2% with 8.8% fewer tokens; DeepSearch 57.1 vs 53.9 with about 8x fewer tokens. The curator is RL-trained.
7. **GWT-labelled agents.** BIGMAS gains of 2 to 6 points over ToT with N=100, full visibility to all agents, no token match. CogniPair: 72% correlation, 77.8% match accuracy, no GWT ablation. Theater of Mind: no experiments.
8. **Philosophy.** Butlin: the residual stream is not a workspace. Goldstein and Kirk-Giannini: language agents may be close.

**What changed behaviour, and by how much.** The robust levers are all about curation: keep few items, prune, delete stale text. Token cost falls 3x to 8x. Accuracy changes are zero to 5 points. A "workspace" label itself is not shown to add anything.

**Missing.** No direct test of hard commit vs soft context mixing. No LLM replication of the slot-sweep optimum. No token-matched workspace ablation on reasoning accuracy.

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. "Schema part" refers to SCHEMA.md v0.2 (G guardrails, S states, O operators, memory). Evidence ids are from evidence_a-d.jsonl; K ids from claims.jsonl.

### Add now (established)
Honest summary: GWT adds almost no new behaviour that is established. The established items support what the schema already does, plus one audit tool.

1. **Code selects one item and passes only it forward; candidates are not all pasted into the next prompt.** Schema part: G5, S7. Already in the schema; GWT adds a second line of support (architecture analogue). [E] for the concept (K01; a01, a02, a03, b16), but the accuracy benefit at equal tokens is untested (see Test first). Do not cite GWT as proof of benefit.
2. **Use Butlin's four indicators (GWT-1 to GWT-4) as a design checklist for the scaffold.** Schema part: documentation only, no behaviour change. [E] (K11; a26, b23, c09 to c12). Our scaffold: GWT-1 independent attempts (S3); GWT-2 no fixed-size state block yet; GWT-3 selected item broadcast through code; GWT-4 code-routed states.
3. **Reading rule: do not treat late sustained activity, or any "workspace" label on a paper, as proof of benefit.** Schema part: G7. [E] (K03; a16, b12, b14, d20; K22; d13, d18, d19).
4. **Log the selector's pick versus the best available candidate, and tokens per state** (already in section 6 of SCHEMA.md). This is the measurement the tests below need. [D].

### Test first
5. **Explicit running state of goal and interim conclusions as one short block, instead of raw history.** Schema part: S-state, memory. K13 [E] that the workspace holds goal and interim conclusions (a28, a02, a10, c22); the accuracy benefit is untested, so it is a candidate until T3 passes.
6. **Hard single-item commit vs keep-k vs full context.** Schema part: S7, G5. [S]. Evidence: K20 (d09), K19 (d07), K17 (d10), K16. T1.
7. **Fixed-size carried state, rewritten every step, vs uncapped log.** Schema part: memory, S9. [S]. K18 (d11), K17 (d10), K07 (c01). T2.
8. **Workspace size sweep, k = 1, 3, 5, 8, 12.** Schema part: memory. [S] with no LLM support for a peak (K08, K21; c03, d15, d11). T4.
9. **Vigilance rule: open the full pipeline only after errors; run routine items without it.** Schema part: S0, G1. [S]. a01 (toy); our G1 data (92% plain vs 75% with forced doubt) is consistent. T5.
10. **Threshold commit: a candidate must pass the check before it enters the state; no soft weighting.** Schema part: S4, S7, G3. Analogy to ignition; [C] because human data (Cogitate, Pitts) disputes ignition as a theory. K02 [E] for the bimodality finding, no direct transfer. T1 arm A.
11. **Leaky state: items decay unless refreshed.** Schema part: memory. [S]. c12 (a design suggestion, no data). T6.
12. **Diversity-driven temperature in S3** (Theater of Mind). [S], no data (c14). Low priority; overlaps the S3 history rule.
13. **Reflection lesson lines (Park).** Schema part: S9, memory. [S] (c21: 29.89 vs 26.88). Believability only. Similar to S9; test as ablation (T8).

## 8. Concrete tests on our bench

All tests: all arms get the same total token budget, counted including setup (G7). Report accuracy with 95% intervals over at least 100 items per arm and 3 seeds. Log selector pick vs best candidate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with a check (ARC-style, Game-of-24-style, BrainTeaser); S3 gives 6 candidate attempts | A: code picks 1, only it goes to S5/S8. B: top 3 pasted. C: all 6 pasted (soft mix). Fixed total tokens | Final accuracy; flips right to wrong and wrong to right; tokens | A within 2 points of B; both beat C by 2 to 5 points (from ToT 74 vs 49 and the Du length drop). If A loses to B by more than 3 points, keep k=3 |
| T2 | Multi-step items needing more than 10 steps (long arithmetic chains, multi-constraint puzzles) | A: carried state capped at 300 tokens, rewritten each step. B: full growing log. C: capped at 1,000 tokens | Accuracy at equal total tokens; step where first failure occurs | A or C at least equal to B above 10 steps; about 3x fewer tokens (LbMAS-like) |
| T3 | Same as T2 | A: state = goal plus interim conclusions as one block. B: raw prior attempts and outputs | Accuracy; error-propagation rate | A better by 2 or more points, or equal at lower tokens |
| T4 | One fixed set of 100 items | k = 1, 3, 5, 8, 12 carried items | Accuracy vs k | Do not assume a peak. Report whether the curve is flat (Dossa), threshold (Phua) or interior optimum (Goyal). Expected: flat above 3 |
| T5 | Mixed easy and hard items with known per-class pass rates | A: gated (full pipeline only after a fail or low class pass rate). B: full pipeline on all | Accuracy and tokens | A same accuracy with 30 to 50% fewer tokens; no loss on hard items |
| T6 | Multi-turn items where early information matters | A: state items persist until replaced. B: items decay unless re-cited within 3 steps | Accuracy; stale-item errors | Within 2 points; if B better, stale items hurt |
| T7 | Long-input items (above 20k tokens) | A: recite evidence, then solve with one short state. B: full context | Accuracy at equal tokens | A at least +2 points (Du: up to +4% on RULER) |
| T8 | Repeated problem classes | With vs without S9 lesson lines | Accuracy on classes seen before | 0 to +3 points; run only after T1 to T3 |

## 9. What does not transfer, and why

- **Consciousness findings (ignition, P3b, VAN, seen/unseen).** They are about report and experience. Our agent has no experience to measure. At most they inspire a hard threshold. The ignition claim itself is contested (Cogitate, K04).
- **Neuronal anatomy (PFC, parietal, long-range neurons).** An LLM has no such split. Butlin says the residual stream is not a bottleneck, so a transformer has no built-in workspace (c10).
- **Representation-learning gains (Devillers 6x less paired data, Maytie).** These align modalities with few pairs. Our agent does not train.
- **Goyal's slot sweep.** It depends on a trained network with tuned slots on synthetic video. A prompt-only scaffold has no such knob in the same sense.
- **J-space numbers.** They describe internal activations in Claude. They do not tell us how to prompt. Reflection fine-tuning (fabrication 0.25 to 0.07) is training, which is out of scope.
- **MemAgent and context curation.** The memory and curator are RL-trained and the tasks are retrieval QA. Only the idea "fixed-size overwrite" transfers.
- **Believability (Park) and attraction prediction (CogniPair).** These are not correctness tasks.
- **Blackboard "selection".** It means which agent acts; all agents see the board. It is a cost lever, not a bottleneck. Multi-agent structure should not be imported (G9).
- **GWT-labelled agents.** BIGMAS gives every agent full visibility, the opposite of a small workspace.
- **Time scales.** Brain: 250 to 300 ms ignition and 0.3 to 0.5 s windows. Agent: steps and tokens. No mapping exists.

## 10. Open questions

1. Does a k-item bottleneck with one broadcast item beat a full-context scaffold on LLM reasoning at equal tokens? (K16; the core question.)
2. Is there an interior optimum for carried-item count in LLM agents, or is it flat or a threshold? (K21.)
3. Does hard commit beat soft mixing, with other things equal? (K20 has no soft arm.)
4. Is J-space replicable outside one vendor, and with multi-token concepts? Does its 25-item cap predict where scaffolds should cap state?
5. How large is the failed-replication record for ignition markers? The meta-analysis full text (moderators, unseen VAN SMD) was not read.
6. What does Cogitate's full published text say beyond the first 100k of about 240k characters read?
7. Does LLM reasoning accuracy fall when state items exceed some count, as in human working memory? (Sibling subfield: Working memory.)
8. Do the Dossa and Devillers findings replicate outside their groups?
9. Does a GWT-labelled agent with a matched control exist? (Tait 2026 returned 403.)
10. How strongly should GWT be cited as a design reason given the contested human side? Currently: weakly.

Links to sibling subfields run in parallel (not covered here): Working memory; Metacognition and higher-order representation; Dual-process theory; Search over thoughts; Tree of Thoughts; Compression at inference time; Cognitive artifacts; Logic programming and knowledge representation; Epistemic diversity.

## 11. Sources

[V] opened this session; [M] snippet or secondary description only.

- [M] Baars (1988) A Cognitive Theory of Consciousness. https://doi.org/10.1017/CBO9780511818059 (a12, b16)
- [V] Dehaene, Kerszberg, Changeux (1998) A neuronal model of a global workspace in effortful cognitive tasks. https://pmc.ncbi.nlm.nih.gov/articles/PMC24407/ (a01 to a04)
- [V] Mashour, Roelfsema, Changeux, Dehaene (2020) Conscious processing and the global neuronal workspace hypothesis. https://pmc.ncbi.nlm.nih.gov/articles/PMC8770991/ (a05 to a11, b07, b08)
- [M] Sergent, Baillet, Dehaene (2005) Timing of the brain events underlying access to consciousness. https://doi.org/10.1038/nn1549 (a21)
- [M] Dehaene and Changeux (2011) Experimental and theoretical approaches to conscious processing. https://doi.org/10.1016/j.neuron.2011.03.018 (a22)
- [M] Sergent and Dehaene (2004) Is consciousness a gradual phenomenon? https://doi.org/10.1111/j.0956-7976.2004.00748.x (b09)
- [V] Del Cul, Baillet, Dehaene (2007) Brain dynamics underlying the nonlinear threshold for access to consciousness. https://pmc.ncbi.nlm.nih.gov/articles/PMC1988856/ (a13; b10 is the DOI form, marked not opened)
- [V] Gaillard et al. (2009) Converging intracranial markers of conscious access. https://pmc.ncbi.nlm.nih.gov/articles/PMC2656551/ (a14)
- [V] Bekinschtein et al. (2009) Neural signature of the conscious processing of auditory regularities. https://pmc.ncbi.nlm.nih.gov/articles/PMC2635770/ (a15)
- [V] Pitts, Metzler, Hillyard (2014) Isolating neural correlates of conscious perception from neural correlates of reporting. https://pmc.ncbi.nlm.nih.gov/articles/PMC4189413/ (a16, b12)
- [V] Trubutschek et al. (2017) A theory of working memory without consciousness. https://pmc.ncbi.nlm.nih.gov/articles/PMC5589417/ (a17)
- [V] Sergent et al. (2021) Bifurcation in brain dynamics reveals a signature of conscious processing. https://pmc.ncbi.nlm.nih.gov/articles/PMC7895979/ (b11)
- [V] Stillman, Drake and colleagues (2024) Neural signatures of visual awareness. https://pmc.ncbi.nlm.nih.gov/articles/PMC11558846/ (b13)
- [V] Hutchinson et al. (2026) Meta-analysis of visual awareness negativity and P3b, Psychological Bulletin. https://doi.org/10.1037/bul0000521 (d20; b14 abstract via Europe PMC; full text not read)
- [M] Aru, Bachmann, Singer, Melloni (2012) Distilling the neural correlates of consciousness. https://doi.org/10.1016/j.neubiorev.2011.12.003 (b15)
- [V] Cogitate Consortium (2023) preprint. https://www.biorxiv.org/content/10.1101/2023.06.23.546249v1.full (a18 to a20)
- [V] Cogitate Consortium (2025) Nature 642. https://www.nature.com/articles/s41586-025-08888-1; full text https://pmc.ncbi.nlm.nih.gov/articles/PMC12137136/ (b01 to b04, d04, d05; first 100k of about 240k characters read)
- [V] Naccache, Sergent, Dehaene, Wang, Farisco, Changeux (2025) GNW theoretical response. https://pmc.ncbi.nlm.nih.gov/articles/PMC12510449/ (b05, b06)
- [M] Press and commentary on Cogitate. https://comdig.cssociety.org/2025/05/05/adversarial-testing-of-global- (d06; URL truncated in the evidence file)
- [M] Doerig, Schurger, Herzog (2021) Hard criteria for empirical theories of consciousness. https://doi.org/10.1080/17588928.2020.1772214 (b26)
- [V] Goyal et al. (2022) Coordination among neural modules through a shared global workspace. https://arxiv.org/abs/2103.01197 (a23, b17, b18, c01 to c04)
- [V] VanRullen and Kanai (2021) Deep learning and the global workspace theory. https://arxiv.org/abs/2012.10390 (a24, b20, c07)
- [V] Devillers, Maytie, VanRullen (2024) Semi-supervised multimodal representation learning through a global workspace. https://arxiv.org/abs/2306.15711 (a25, b19, c06, d16)
- [V] Maytie, Devillers, Arnold, VanRullen (2024) Zero-shot cross-modal transfer of RL policies through a global workspace. https://arxiv.org/abs/2403.04588 (d17; abstract only)
- [V] Dossa et al. (2024) Design and evaluation of a global workspace agent embodied in a realistic multimodal environment. https://pmc.ncbi.nlm.nih.gov/articles/PMC11211627/ (b21, b22, c08, c24, d15)
- [V] Chateau-Laurent and VanRullen (2025) Learning to chain operations by routing information through a global workspace. https://arxiv.org/abs/2503.01906 (c05)
- [V] Butlin, Long, Elmoznino et al. (2023) Consciousness in artificial intelligence. https://arxiv.org/abs/2308.08708 (a26 to a28, b23, c09 to c12, c23)
- [V] Goldstein and Kirk-Giannini (2024) A case for AI consciousness: language agents and global workspace theory. https://arxiv.org/abs/2410.11407 (b24, c13, c26)
- [V] Juliani, Arulkumaran, Sasai, Kanai (2022) On the link between conscious function and general intelligence in humans and machines. https://arxiv.org/abs/2204.05133 (b25, c20; abstract only)
- [V] Anonymous (2026) Theater of Mind for LLMs. https://arxiv.org/abs/2604.08206 (c14)
- [V] Gurnee, Sofroniew, Pearce et al. / Anthropic interpretability team (2026) Verbalizable representations (J-space). https://transformer-circuits.pub/2026/workspace/ (c15 to c19, d01 to d03; about 200k of 336k characters read)
- [V] Park et al. (2023) Generative agents. https://arxiv.org/abs/2304.03442 (c21, c25)
- [V] Sumers, Yao, Narasimhan, Griffiths (2023) Cognitive architectures for language agents. https://arxiv.org/abs/2309.02427 (c22)
- [V] Han and Zhang (2025) LbMAS blackboard multi-agent. https://arxiv.org/abs/2507.01701 (d07)
- [V] Salemi et al. (2025) LLM-based multi-agent blackboard system. https://arxiv.org/abs/2510.01285 (d08; Qwen table rows garbled)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (d09)
- [V] Du et al. (2025) Context length alone hurts LLM performance. https://arxiv.org/abs/2510.05381 (d10; abstract only)
- [V] Yu et al. (2025) MemAgent. https://arxiv.org/abs/2507.02259 (d11; tables garbled)
- [V] Li et al. (2026) Active context curation. https://arxiv.org/abs/2604.11462 (d12)
- [V] Hao, Dai, Qin, Yu (2026) BIGMAS. https://arxiv.org/abs/2603.15371 (d13)
- [V] Phua (2025) Can we test consciousness theories on AI? https://arxiv.org/abs/2512.19155 (d14)
- [V] netsky-lab (2026) gwt-context honest report. https://netsky-lab.github.io/gwt-context/honest-gwt-report.html (d18)
- [V] Ye et al. (2025) CogniPair. https://arxiv.org/abs/2506.03543 (d19; abstract only)
- [M] Tait et al. (2026) Evaluating global workspace markers in contemporary LLMs. https://www.preprints.org/manuscript/202601.1683/v1 (d21; 403, not read)
