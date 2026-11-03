# Metacognitive knowledge: declarative, procedural, conditional: deep document

*Subfield A04.04. Folder evidence: evidence_a-d.jsonl (ids a01-a29, b01-b26, c01-c31, d01-d17), claims.jsonl (K01-K31), critique.md. All LLM results below are from this folder; most are single-run preprints. Human founding studies are known only through Flavell's 1979 essay, so exact N and recall rates are missing (K31).*

## 1. What it is

Metacognitive knowledge is what a thinker stores about thinking. It is ordinary long-term knowledge, not a special store (b01). Flavell (1979) split it into three variable types: person (me and others as thinkers), task (what the information and the goal demand), and strategy (what works for which goal) (a01-a04). He said most of it is an interaction: "you, unlike your brother, should use Strategy A, not B, in Task X, not Y" (a02).

Later work, mainly Paris, Lipson and Wixson (1983) and Schraw and Moshman (1995), cut strategy knowledge into three kinds (a27, a28; both snippet only):

- Declarative: knowing that. Facts about myself, the task and which strategies exist.
- Procedural: knowing how. How to run a strategy.
- Conditional: knowing when and why. Which strategy fits which situation.

Conditional knowledge was argued to be the part most often missing (a28, secondary report).

For our agent, this maps to a class record: for each task class, which operator (O1-O8) works, measured on our own bench, plus how to run it and when to stop. The record is declarative (class X has pass rate p under operator Y), procedural (the operator recipe) and conditional (pick Y when class is X and baseline is below some level).

Scope notes. Not covered here: confidence calibration in depth (see Confidence and metacognition and Metacognition models, run in parallel), regulation (planning, monitoring), and strategy-learning theories. Only links are noted.

## 2. History and theories in depth

**Flavell 1979 (a01-a05, b01).** A four-part model of cognitive monitoring: metacognitive knowledge, metacognitive experiences (feelings such as "this is hard"), goals, and actions. Knowledge is stored beliefs; experiences are live. The paper has no data. It lists four ways knowledge fails (a05): it can be wrong, not activated when needed, activated but without effect on behaviour, or acted on but unhelpful. Person knowledge has three sub-parts: within-person, between-person, and universals (a04). A useful insight: how well I know something now may not predict later (a04). Task knowledge has two sub-parts: the information available (abundant, familiar, organised, trustworthy) and the demands (recalling gist is easier than exact wording) (a03).

**Founding experiments, as reported in the 1979 essay only.**
- Flavell, Friedrichs and Hoyt (1970): children studied items until sure they could recall them perfectly. Older children said ready and usually were. Younger children said ready and usually were not (a06). No N or rates are in the essay.
- Markman (1977): children judged instructions riddled with omissions. Younger children missed the gaps and thought they understood (a07).
- Lesson: a feeling of being ready needs an outside check (K04).

**Paris, Lipson, Wixson 1983 (a28, snippet).** Origin of declarative, procedural, conditional in reading instruction. Not opened.

**Schraw and Dennison 1994 (a08, snippet).** A 52-item self-report inventory (MAI) with eight subscales under two heads: knowledge of cognition (declarative, procedural, conditional) and regulation (planning, information management, monitoring, debugging, evaluation). Two experiments, 307 undergraduates in total, reported as supporting two factors (database summary only).

**Later structure tests (a09, a10, b02-b06).** The two-head structure holds; the three-way split under knowledge does not (see section 5).

**Computational translations.** Oh and Gobet (2025) turn Flavell into Monitor-Generate-Verify: monitoring (difficulty, confidence, strategy retrieval) before generation, and verification feedback updates the monitoring knowledge. No experiments (a26). MIRROR, MUSE, MC2 and Think2 build on the same idea (a20-a23, c15-c16, b17).

**Other human lines.** School interventions that teach metacognitive strategies have lasting effects (b07-b09; snippet-only numbers). Veenman et al. (2006) argue metacognitive skill is general, teachable, best measured on-line, and best trained when embedded in the subject (b26, snippet). Hartwig and Dunlosky (2012): students often prefer weak strategies such as rereading and know little about self-testing (b25, snippet).

## 3. Core findings with exact numbers

Status: E established (two or more independent sources), S single-source, C contested. Opened status per source is in section 11.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Knowledge is mostly person x task x strategy interaction | 3 variable types, 4 failure modes | Flavell 1979 (a01-a05, b01) | S (theory essay) |
| Young children feel ready without being ready | no N or rates available | Flavell et al. 1970; Markman 1977 via Flavell 1979 (a06, a07) | S |
| MAI two factors fit; 3-way split under knowledge does not | N=528: two-factor CFI .96, RMSEA .05; higher-order CFI .84, RMSEA .11 | Gutierrez de Blume and Montoya 2021 (b02) | E (a09, b02, b03, b05, b06) |
| MAI replication, 18 items, two dimensions | N=462; r between dimensions .497; CFI .92, RMSEA .077 | Parpala 2022 (a09) | E |
| Full 52-item MAI has poor fit; 19-item subset fits | N=622 | Harrison and Vallin 2018 (b03) | E |
| LLMs follow a named strategy; free choice no better than fixed | Phi-4 TruthQuest free 47.2 vs forced 45.1-49.0; adherence 99/88/81/64 | Zhang 2025 (b13, c12, c14) | E (with b12, d04) |
| MRP strategy selection helps GPT-4, not GPT-3.5 | GPT-4 MRP .772 vs ToT .725; GPT-3.5 MRP .433 vs SPP .469 | Gao 2024 (b12) | S |
| Self-route does not beat Direct except tie at frontier | mean 46.7 vs Direct 47.6; GPT-5 60.3 = 60.3; Qwen3-Max 42.4 vs 49.8 | Select-then-Solve 2026 (d04) | S (text and table disagree) |
| Per-item oracle headroom is large on some tasks | Phi-4 TruthQuest 82.9 vs 47.2; R1-Distill 90.1 vs 63.4; ZebraLogic 37.7 vs 27.3 and 36.4 vs 32.0 | Zhang 2025 (b13, c12) | E |
| Same headroom across 10 benchmarks | oracle over best fixed: +12.4, +19.1, +21.6, +24.1 (4 models) | Select-then-Solve (d01) | E (K06) |
| Code combination beats single, far below oracle | TruthQuest Phi-4: vote 54.9, vote+prob 57.3, oracle 82.9 | Zhang 2025 (c13) | S |
| Learned router recovers a quarter of the gap | 53.1 vs best fixed 50.3 vs oracle 68.9; ~26% gap; 229 test tasks | d02 | S |
| Router vs random vs best model | RTR 82.5 at 1091 tokens; best model 80.0 at 2745; random 69.5 | Route to Reason (d06) | S |
| Skill-matched exemplars beat topic, random, complex-CoT | MATH GPT-4: CoT 42.2, Complex 50.30, topic 50.31, skill 53.88; GSM8K random 92.87, skill 94.31 | Didolkar 2024 (a12, a13) | S |
| Skill catalogue from strong model transfers | Mixtral MATH skill 28.44 vs topic 26.14; skill best in 4 of 6 other sets | a14 | S |
| Per-task structure beats CoT on structure-heavy tasks | GPT-4 BBH 81 vs 75; T4D 85 vs 52; MATH 73 vs 71 | Self-Discover (a15, b11) | S |
| Self-Discover saves calls | 10-40x fewer than self-consistency; structures right 87.5% | a16 | S |
| Gains shrink as baseline rises | SMART +15.2, +11.0, +3.5; GSM8K GPT-4 93.0 to 94.3 | b14, a13 | E (K10) |
| Fixed metacognitive prompt: small gain, overthinking | MP beats CoT by 4.8-6.4 zero-shot; overthinking 68.3% of MP errors | Wang and Zhao (a17, b18, c06) | E (with b17) |
| Forced plan-monitor-evaluate hurts non-reasoning model | Llama-3-8B GSM8K 69.55 vs plain 80.71 vs CoT 77.98 | Think2 (b17) | S, contested vs MP |
| Told own calibration, models do not change | confident failure 0.600 / 0.605 (told) / 0.514 (normative) / 0.143 (external control); 16 models, ~250k instances | MIRROR (a21) | E with a23, d09 |
| Self-knowledge does not transfer or compose | transfer index 0.019-0.175; compositional error 0.43-0.94 | MIRROR (a22) | S |
| Confidence control helps low-confidence items only | low 0.16 to 0.42; high 0.67 to 0.64; full 47.0 [37,57] vs random retry 45.7 | Cao 2026 (a23) | S |
| Knows tool is unneeded, uses it anyway | Kc/Aw 1.76-45.48% over 18 models; GPT-5 know 94.22 vs act 58.54 | KAPRO (d09, d10) | S |
| Learned think/no-think selector | length -53%, accuracy +2.4 (always-NoThinking -12.7 points, -79.9% length) | AdaptThink (b15) | E |
| Meta-controller | 87.0 vs 84.0 at 3941 vs 5691 tokens | Meta-R1 (b16) | S |
| Own-trace behaviours cut tokens | up to -46% tokens; MC2 MATH-500 78.93 to 85.13, Game-of-24 41.33 to 88.67, 1631 tokens vs CoT-SC 3200 | a19, a20 | E (K18) |
| Competence self-assessment in agents | ALFWorld novel: MUSE 84/90, random 68/69, lowest 59/61, Reflexion 45/51, ReAct 35/35 | MUSE (c16) | S |
| Models show less self-awareness than humans | 19% of model traces vs 49% human; NPMI with success -0.141 | Kargupta (c24) | S |
| School metacognitive instruction lasts | g about 0.50 post, similar follow-up | b09 (snippet) | S |

## 4. Mechanisms and models

### 4.1 The class record as data

An engineer can implement the Flavell triple as a table.

```
record[class][operator] = {n_runs, n_pass, tokens_mean, last_updated}
class key    = label from a fixed list (S0 gate), made once by the strongest model
person var   = the model id (record is per model; transfer is weak, see 4.6)
```

Declarative part: the table. Procedural part: the operator recipe text (O1-O8 definitions). Conditional part: the rule that reads the table and picks. Keep the three apart in code so they can be ablated (K22).

### 4.2 Building the class list (Didolkar 2024; a11, a12, c01, c02)

1. Strong model labels each training question with a fine-grained skill name (about 500 raw names on 7,000 GSM8K items; about 5,000 on 7,500 MATH items).
2. The same model clusters names into a small catalogue (22 for GSM8K, 117 for MATH).
3. At test time the model picks one label from the catalogue; exemplars tagged with that label are shown.

Weak points: Llama-2 70B and Mixtral cannot cluster (Mixtral puts everything in one cluster) (a14). Labels are topic-like skills, not strategies (c04). Label quality limits the gain.

### 4.3 Choosing the operator

Three ways, in order of evidence strength:
1. Code picks from measured pass rates (learned router). Select-then-Solve: logistic router on prompt features, labels from 300-400 items per model (d02, d03). RTR: about 1,470 training cases (derived) (d06, d07).
2. Model picks from a list of descriptions (Self-Discover, MRP). Works for GPT-4 class, fails for GPT-3.5 and Phi-4 (b12, b13).
3. Model is told its own scores in the prompt. MIRROR shows no effect (a21).

Rule from the evidence: choice should be made by code from measured data wherever possible (K13, K26), with the model used to execute the chosen operator, which it does well (K05).

### 4.4 Amortise per class (Self-Discover, a15, a16)

Select and adapt modules once per task class, write a fixed structure (JSON plan), then reuse it for every instance. Cost is a few extra calls per class, not per item. Gains: BBH 81 vs 75, T4D 85 vs 52 on GPT-4; only 1-7 points on MATH where 74.7% of failures are arithmetic (c10, c11).

### 4.5 Learn the record from own traces (a19, a20)

- Metacognitive Reuse: model reads its own solved traces, writes "behaviors" (name plus instruction), stores a handbook, retrieves by topic. Handbook built from 1k MATH questions. Up to 46% fewer reasoning tokens at equal or better accuracy (a19).
- MC2: reasoner, monitor and controller roles; lessons are consolidated across instances. Ablation on MATH-500: reasoner only 72.67, full 85.13 (a20). Larger gain for weaker backbones. Order effect noted.

### 4.6 Scope and decay

Self-knowledge is domain-bound. MIRROR transfer index 0.019-0.175 (a22). Trained confidence that tracks consistency transfers further than confidence that tracks accuracy (r = 0.49 with distance) (d11). Implication: key the record on class, and treat mixed-class or new-model cases as unknown until measured.

### 4.7 Cold start

Bandit recipe (d12): serve each of 10 baseline arms once; let the active set grow as sqrt(t). Regret bound O(T^0.75) at beta 0.5. No study gives items per class at which a measured record beats a prior (K29).

### 4.8 Gate by baseline

Gain shrinks as baseline accuracy rises (K10). Learned selectors save most on easy items: AdaptThink -50.9% length on GSM8K with +4.1 points (b15). Gate the record step by baseline pass rate (G7, G12).

## 5. What holds up

**Held up**
- Two-head structure (knowledge, regulation) of the human inventory: at least four replications (a09, a10, b02, b03).
- LLMs follow a named strategy on request; adherence varies by strategy (99% vs 61% for Phi-4 variants; other models 88, 81, 64 and 61, 12, 53, 11) (b13, c14).
- No fixed strategy wins across items; the oracle gap is large (b13, c12, d01). Oracle numbers are optimistic because the oracle takes a maximum over noisy runs (d01).
- Model-side self-choice does not beat the best fixed choice except at frontier strength, and even there it ties (b13, b12, d04).
- Externally controlled use of self-knowledge works where telling the model does not (a21: 0.605 told, 0.143 external).
- Gain shrinks with baseline (b14, a13, a20).
- Own-trace procedural memory saves tokens (a19, a20).

**Failed or weak**
- The three-way declarative/procedural/conditional split under knowledge: CFI .84, RMSEA .11, N=528 (b02). The 52-item eight-subscale model has poor fit (b03). Russian (N=527) and Latvian adaptations did not reproduce it (b06). An Arabic short form found three dimensions by network analysis against two by CFA (b05).
- No opened study tests conditional knowledge as separate from procedural knowledge, in humans or LLMs (K22, b24).
- Forced metacognitive prompts: Think2 Llama-3-8B GSM8K 69.55 vs plain 80.71 (b17). MP has overthinking in 68.3% of its errors, overcorrection 31.7% (c06). The contradiction with MP's own gains is unresolved (model, task, prompt design).
- Cao 2026: full confidence harness 47.0 [37,57] is inside the interval of random retry 45.7 on 100 items. The +8.6 headline is against a single attempt (critique section 2).
- Router gains over the best fixed choice are small and noisy (0.5-3 points) (d02, d06). Select-then-Solve, RTR and PRISM have internal contradictions between text and tables (critique; d04, d06, d13).

**Moderators**
- Model strength: Self-Discover and MRP help GPT-4/PaLM 2-L, not GPT-3.5 (a15, b12).
- Baseline accuracy (above).
- Task type: structure-heavy tasks gain; arithmetic-limited do not (c10, c11). Kargupta: scaffolding up to +66.7 on ill-structured tasks, down to -72 on others (c25).
- Label quality: GPT-4 labels beat GPT-3.5 and Mixtral labels (c02).
- Reasoning-trained vs not: forced cycles help the first, hurt the second (b17). The KAPRO table shows reasoning variants overuse tools more than instruct (Sonnet 4.5 think 41.96 vs instruct 23.12), against the paper's abstract (d10).

**Interventions that worked**: code-side routing from measured labels (d02, d06, d08); skill-matched exemplars (a12); once-per-task structure (a15); own-trace behaviour handbook (a19, a20); learned think/no-think (b15); external control of confident failure (a21). Weight-training methods (SMART, AdaptThink, MaR, Meta-R1) need training, which our scaffold cannot do; only the selection logic transfers.

**Interventions that did not**: telling the model its own calibration (a21); self-route from a prompt (d04); weak model as selector (b12); forced plan-monitor-evaluate on non-reasoning models (b17); prompted "could you be wrong?" has no accuracy numbers (c28).

## 6. Language models

**Procedural: easy.** Given a named strategy, models mostly follow it. Phi-4 adherence: supposition following 99%, and across models 88, 81, 64; chain construction 61, 12, 53, 11 (c14). But following a strategy does not improve accuracy: no single strategy beat the no-strategy prompt on Phi-4 TruthQuest (47.2 free, best single 49.0) (c12).

**Conditional: weak.** Model-side selection:
- MRP, 7 tasks, GPT-4 macro average MRP .772 vs ToT .725, SPP .688, Self-Refine .677, CoT .654. GPT-3.5: SPP .469, Step-back .452, MRP .433, CoT .416 (b12). On Game of 24 GPT-4 MRP is .31 vs ToT .41.
- Select-then-Solve zero-shot self-route, mean of 4 models 46.7 vs Direct 47.6; GPT-5 picks Direct 65.1% of the time and never Reflection (d04, d16).
- Oracle headroom: +12.4 to +24.1 points over the best fixed paradigm (d01); 35.7 points on TruthQuest Phi-4 (b23).

**Learned routers.** Select-then-Solve 53.1 vs 50.3 (d02). RTR 82.5 vs QwQ-32B 80.0, tokens 1091 vs 2745, random 69.5 (d06). On unseen sets RTR gets 93.1 to 95.3 (d07). Semantic Router: MMLU-Pro 58.57 vs 48.33 (+10.24 pp), tokens -48.5%, better in 11 of 14 domains (d08). PRISM +3.8 to +9.1 on math, with conflicting stated gains (d13).

**Self-knowledge.** Kadavath (2022): P(True) is well calibrated and improves with scale; P(IK) rises with source text and hints (c07, c08). Binder (2024): after fine-tuning GPT-4o self-prediction rose 32.6 to 49.4, a +17 advantage over a model trained on its behaviour (b20). MIRROR: above-chance domain-level self-knowledge, not used when told (a21). Meta-d' work: all three tested LLMs have substantial meta-d' but always suboptimal M-ratio (c19). MetaMedQA: GPT-4o identified its limits 3.7% of the time (c18, snippet).

**Knowing is not acting.** KAPRO: GPT-5 internal subspace Acc_know 94.22 vs Acc_act 58.54; Kc/Aw 1.76-45.48% (d09). This matches Flavell's "activated but ignored" failure.

**Self-awareness in traces.** 19% of model traces vs 49% human; negative NPMI -0.141 with success (c24). Direction of cause unknown.

**Making knowledge explicit.** Skill labels from GPT-4 gave +11.6 over CoT on MATH (a12). Metacognitive Reuse up to 46% fewer tokens (a19). MC2 gains largest for weaker backbones (Llama-3.1-8B MATH-500 65.47 to 76.80) (a20). MUSE: small LLMs gain much more from the loop (OpenELM-3B ReAct 4%, MUSE 55%) (c17). Of the 49 points MUSE gains over ReAct, random self-assessment keeps 33 (68 vs 35); assessment explains about 16 (critique section 2).

**Explicit metacognitive prompting.** MP +4.8 to +6.4 zero-shot over CoT but overthinks simple sets (c05, c06). Metacognition-as-Reward (training): Qwen3.5-9B 66.7 to 67.6, best gain +7.7 over base, +11.0 over DAPO (a18).

**Users.** Default explanations lead users to overestimate LLM accuracy; matching explanation length to confidence narrows the gap (N=301) (b21, c29).

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Choose the operator in code from measured pass rates, not by asking the model.** Part: S6 control / O1-O8 routing, G5. [E] a21, d02, d04, d06, d08, b12, b13 (K05, K13, K26 partly).
2. **Do not put the record in the prompt and expect compliance.** If the record is shown, enforce it by code (route, cap, retry). Part: G5, G10. [E] a21 (told 0.605 vs external 0.143), d09.
3. **Gate record use by baseline difficulty.** Skip the record step on classes where the plain model already passes; gain shrinks with baseline. Part: G7, G12. [E] b14, a13, a20 (K10).
4. **Measure the per-class oracle gap before building routing.** Skip classes where best-of-operators barely beats best fixed (ZebraLogic: 37.7 vs 27.3). Part: G7. [E] b13, c12, c13, d01 (K06).
5. **Always include random-operator and best-fixed-operator controls.** Random loses to best fixed by about 10 points; a gain over random is not a gain over best fixed. Part: G7, bench design. [E for the principle; the 10-point figure is single-source] d06, d07 (K25).
6. **Log the four Flavell failures separately.** Wrong record, record not retrieved, retrieved but ignored, used but unhelpful. Part: section 6 logging. [E] a05, a21, a23, c18, d09 (K02).
7. **Do not force a fixed plan-monitor-evaluate scaffold on every item.** Part: section 4b not-to-add, G1, G11. [E] b17, c06 (K12).
8. **Write the record from the agent's own solved items, per class, and measure on held-out items of that class.** Part: memory (section 5). [E] a19, a20, b19 (K18).
9. **Treat mixed-class items and new models as unknown until measured.** Part: S0 gate. [S] a22, d11. A safety rule, not a feature.
10. **Use the human vocabulary as vocabulary only.** The three-way split is not recovered empirically, so do not build three modules because the theory has three words. [E] a09, b02, b03 (K03).

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Per-class record routing vs best fixed vs random, equal tokens | O1-O8, S6 | [S] | d02, d06 |
| Per-class fixed structure written once vs per-instance choice | S0/S6, O3 | [S] | a15, a16 |
| Record in prompt vs record in code (same content) | G5 | [C] confounded | a21, d05 |
| Skill-matched hints vs topic-matched vs random hints | S0 gate, memory | [S] | a12, a13 |
| Strong model builds class list once, cheap model uses it | S0 gate | [S] | a14, c03 |
| Random or inverted record entries keep most of the gain? | G7 | [S] | c16 |
| Cold start: items per class needed (5, 10, 20, 40) | memory update rule | open | d12 |
| Self-route threshold for our model | S6 | [S] | d04, b12 |
| Escalate on impasse vs always-long | G12 | [E] for learned, [S] for ours | b15, b16, a24 |
| Procedural vs conditional ablation | all | open | K22 |

## 8. Concrete tests on our bench

All arms use equal total tokens including setup, three or more repeats, report mean and interval.

1. **T1 Record routing.** Items: 4-6 task classes from our bench (ARC-like, BrainTeaser, plus others), 40+ items per class. Arms: (a) random operator, (b) best fixed operator, (c) code router from measured per-class pass rates, (d) per-item oracle (reference only). Metric: pass rate at equal tokens; share of oracle gap closed. Expected: (c) above (b) by 1-5 points; (a) about 10 below (b) (d06, d02).
2. **T2 Prompt vs code.** Same record content. Arms: record in prompt and model picks; record in code and code picks; no record. Metric: pass rate, rate of "record ignored" (K27 log). Expected: code beats prompt by several points; prompt close to no-record (a21).
3. **T3 Oracle gap first.** Items: each class. Run all O1-O8 on a 30-item sample per class. Metric: oracle minus best fixed per class. Expected: some classes under 3 points; those are skipped (b13).
4. **T4 Per-class structure once.** Arms: structure chosen once per class and reused vs per-instance choice vs plain. Metric: pass rate and calls. Expected: gain on structure-heavy classes, none on arithmetic-limited (a15).
5. **T5 Hint matching.** Arms: hints by skill label, by topic, random hints, none. Metric: pass rate. Expected: skill > topic by about 3 on math-like classes, near zero on easy classes (a12).
6. **T6 Ablated record.** Arms: true record, random-entry record, inverted-entry record, no record, all code-routed. Metric: pass rate. Expected: random keeps much of the gain (c16); inverted loses it. Tells how much is the selection and how much is extra structure.
7. **T7 Cold start.** Build the record from 5, 10, 20, 40 items per class; test on 100 held-out items. Metric: accuracy of choice vs items seen. Expected: break-even at 10-20; unknown (K29).
8. **T8 Mixed-class and transfer.** Items that combine two classes; record built on a strong model applied to a cheaper model. Metric: pass rate vs best fixed. Expected: little or no gain (a22).
9. **T9 Self-route threshold.** Model picks operator from a list vs Direct vs best fixed on 3 classes. Metric: pass rate. Expected: tie or loss (d04).
10. **T10 Failure log.** Run the T2 prompt arm and tag each failure as wrong, not retrieved, ignored, unhelpful. Metric: counts. Expected: "ignored" is large (d09).

## 9. What does not transfer, and why

- **Inventory data (MAI).** Self-report scales in students. Our agent has no reliable self-report; only measured pass rates. The three-way split fails even in humans (b02).
- **Child development findings (Flavell 1970, Markman 1977).** Age-related monitoring gaps do not map to model size. Lesson kept: feelings of readiness need external checks.
- **School intervention effects (g about 0.50).** Teaching a person a strategy over weeks has no counterpart in a scaffold; numbers are snippet-only (b07-b09).
- **Weight-training methods** (SMART, AdaptThink, MaR, Meta-R1, trained confidence). We cannot train; only the choice logic transfers (critique section 4).
- **Fixed metacognitive prompts** (MP, Think2). They gain modestly or hurt, mainly because of overthinking; they conflict with G11 and 4b.
- **Oracle numbers.** Optimistic by construction (maximum over noisy runs); use only to decide where routing could pay (d01).
- **Router accuracy numbers.** Text and table disagree in Select-then-Solve, RTR and PRISM; use direction only (critique).
- **Human conditional knowledge as an extra store.** No evidence of a separable store (K22); an LLM has no separate memory for it either.
- **Mismatched cost measures.** Several studies report time or calls, not tokens; few are token matched (MC2 and Self-Discover are).

## 10. Open questions

1. At equal tokens, does a per-class operator record beat the best fixed operator and a random operator on our own classes? (Partly closed in the literature, not for our tasks.)
2. How large is our per-class oracle gap? A small gap kills the record for that class.
3. Is a record better enforced by code than shown in the prompt for operator choice (MIRROR says so for confidence only)?
4. How many items per class before a measured record beats a prior?
5. Does the record transfer to mixed-class items and to cheaper models?
6. Is conditional knowledge separable from procedural knowledge in an LLM? Planned ablation: arm A model is told the operator (procedural); arm B model picks from a list (conditional); arm C code picks from the record. B-A and C-B measure each part.
7. Do random or inverted record entries keep most of the gain?
8. At what model strength does self-selection stop losing? We have one data point (GPT-5 ties) and no number for our model.
9. What are the actual numbers in Flavell et al. 1970, Markman 1977, Schraw and Dennison 1994, Schraw and Moshman 1995 and Paris et al. 1983? Not reachable (d17).
10. What is the rate of the four Flavell failures when an LLM uses a written record (d16)?
11. Does self-awareness in traces cause lower success (Kargupta NPMI -0.141) or follow from harder items?
12. Why do forced metacognitive prompts help in MP and hurt in Think2?

## 11. Sources

[V] opened in this series, [M] snippet or summary only. URLs as recorded in the evidence files.

- [V] Flavell (1979) Metacognition and cognitive monitoring. https://jwilson.coe.uga.edu/emat7050/Students/Wilson/Flavell%20(1979).pdf ; https://doi.org/10.1037/0003-066X.34.10.906 (a01-a05, b01)
- [V, as reported in Flavell 1979 only] Flavell, Friedrichs and Hoyt (1970); Markman (1977) (a06, a07)
- [M] Schraw and Dennison (1994) MAI. https://doi.org/10.1006/ceps.1994.1033 (a08)
- [M] Schraw and Moshman (1995) Metacognitive theories. https://doi.org/10.1007/BF02212307 (a27)
- [M] Paris, Lipson and Wixson (1983) Becoming a strategic reader. https://doi.org/10.1016/0361-476X(83)90018-8 (a28)
- [V] Parpala (2022) https://doi.org/10.1007/s11409-022-09314-x (a09)
- [M] Harrison and Vallin (2018) https://doi.org/10.1007/s11409-017-9176-z (a10, b03)
- [V] Gutierrez de Blume and Montoya (2021) https://www.redalyc.org/journal/4975/497570255004/497570255004.pdf (b02, b24)
- [M] Junior MAI 18-item study (ERIC 2017) https://eric.ed.gov (b04); Arabic MAI short version (ERIC 2024) https://eric.ed.gov (b05); Latvian and Russian MAI adaptations https://dspace.rsu.lv/items/d4f7d161-6e90-4244-a1c1-08bd53b02e97 (b06)
- [M] Dignath and Buttner (2008) https://doi.org/10.1007/s11409-008-9029-x (b07); Donker et al. (2014) https://doi.org/10.1016/j.edurev.2013.11.002 (b08); de Boer et al. (2018) https://doi.org/10.1016/j.edurev.2018.03.002 (b09)
- [M] Hartwig and Dunlosky (2012) https://doi.org/10.3758/s13423-011-0181-y (b25); Veenman et al. (2006) https://doi.org/10.1007/s11409-006-6893-0 (b26)
- [V] Didolkar et al. (2024) Metacognitive capabilities of LLMs in math. https://arxiv.org/abs/2405.12205 (a11-a14, b10, c01-c04)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (a15, a16, b11, c10, c11)
- [V] Wang and Zhao (2024) Metacognitive Prompting. https://arxiv.org/abs/2308.05342 (a17, b18, c05, c06)
- [V] Gao et al. (2024) Meta-Reasoning Prompting. https://arxiv.org/abs/2406.11698 (b12)
- [V] Zhang et al. (2025) Reasoning strategies: follow, prefer, optimize. https://arxiv.org/abs/2507.11423 (b13, c12-c14)
- [V] Liu et al. (2024) SMART. https://arxiv.org/abs/2410.16128 (b14, c23)
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 (b15, c22)
- [V] Dong et al. (2025) Meta-R1. https://arxiv.org/abs/2508.17291 (b16)
- [V] Elenjical et al. (2026) Think2. https://arxiv.org/abs/2602.18806 (b17, c26, c27)
- [V] Didolkar et al. (2025) Metacognitive Reuse. https://arxiv.org/abs/2509.13237 (a19, b19, c21)
- [V] Zhuang et al. (2026) MC2. https://arxiv.org/abs/2604.17399 (a20)
- [V] Wang (2026) MIRROR. https://arxiv.org/abs/2604.19809 (a21, a22)
- [V] Cao et al. (2026) LLMs know when they know. https://arxiv.org/abs/2605.14186 (a23)
- [V] Khandelwal et al. (2025) SOFAI-LM. https://arxiv.org/abs/2508.17959 (a24)
- [V] Luo et al. (2025) Learning from peers. https://arxiv.org/abs/2505.07787 (a25; motivation only)
- [V] Oh and Gobet (2025) Monitor-Generate-Verify. https://arxiv.org/abs/2511.04341 (a26)
- [V] Chen et al. (2026) Metacognition-as-Reward. https://arxiv.org/abs/2605.23384 (a18, b22)
- [V] Binder et al. (2024) Looking Inward. https://arxiv.org/abs/2410.13787 (b20, c09)
- [V] Steyvers et al. (2025) What LLMs know and what people think they know. https://arxiv.org/abs/2401.13835 (b21, c29)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (c07, c08)
- [V] Valiente and Pilly (2025) MUSE competence-aware agents. https://arxiv.org/abs/2411.13537 (c15-c17)
- [V] Servajean and Servajean (2026) meta-d' for AI. https://arxiv.org/abs/2603.29693 (c19, c20)
- [V] Kargupta et al. (2025) Cognitive foundations. https://arxiv.org/abs/2511.16660 (c24, c25)
- [V] Hills (2025) Could you be wrong. https://arxiv.org/abs/2507.10124 (c28)
- [M] Griot et al. (2025) MetaMedQA. https://doi.org/10.1038/s41467-024-55628-6 (c18); MetaMedQA reanalysis https://arxiv.org/pdf/2608.14552 (c30); benchmark cognitive depth https://papers.cool/venue/2025.findings-emnlp.724@ACL (c31)
- [V] Select-then-Solve (2026) https://arxiv.org/abs/2604.06753 (d01-d05)
- [V] Route to Reason (2025) https://arxiv.org/abs/2505.19435 (d06, d07)
- [V] Semantic Router for vLLM (2025) https://arxiv.org/abs/2510.08731 (d08)
- [V] KAPRO, From Knowing to Acting (2026) https://arxiv.org/abs/2606.20661 (d09, d10, d16)
- [V] Metacognition when trained to predict own accuracy (2026) https://arxiv.org/abs/2609.33886 (d11)
- [V] Bandits in Prod (2026) https://arxiv.org/abs/2609.01335 (d12)
- [V] PRISM (2025) https://arxiv.org/abs/2509.24377 (d13)
- [M] Reasoning Router (Vadlapati 2025) https://www.academia.edu/144702030/Reasoning_Router_Dynamic_Multi_Strategy_Reasoning_for_Robust_Multi_Step_Problem_Solving (d14)
- [V] Metacognition framework for self-awareness in ensembles (2026) https://arxiv.org/abs/2608.15400 (d15)
- [M] Primary-source access attempt (d17) https://www.sciencedirect.com/science/article/pii/S0361476X84710333
