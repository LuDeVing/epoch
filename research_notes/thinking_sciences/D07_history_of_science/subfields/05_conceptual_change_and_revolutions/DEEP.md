# Conceptual change and revolutions: deep document

*Subfield D07.05. Sources: evidence_a-d.jsonl (ids a01-a30, b01-b28, c01-c25, d01-d20), claims.jsonl (K01-K33), critique.md. Checked 2026-11-10. Where a number was only seen second-hand, it is marked.*

## 1. What it is

This subfield studies how a framework of ideas is replaced by another. It has two sides.

- **History and philosophy of science.** Kuhn (1962) described normal science, anomalies, crisis and revolution. The oxygen versus phlogiston case is his main example.
- **Cognitive science and education.** How people (children, students, scientists) respond to data that does not fit their theory, and what it takes for them to change the theory.

It matters to our agent for one reason. The agent must decide **when to stop patching an approach and reframe the problem** (impasse trigger S6, operator O8 "reframe the goal"). Kuhn's picture gives the shape of the trigger: a single failure is normal and is explained away; failures that pile up and resist the current frame justify a change. Kuhn gives no number for "pile up". No human or LLM study found here varies that number (K29).

Core finding in one line: **reframing helps when an external check shows a failure, and it hurts or does nothing when the model only doubts itself** (K03, K04, K26). The best direct test of a Kuhn-style agent (Smith 2026) did not beat blind sampling (K19).

## 2. History and theories in depth

### 2.1 Kuhn's cycle (a01, a04, a05)

- Pre-paradigm science, then **normal science**: puzzle-solving inside a shared framework (the "disciplinary matrix"). Puzzle-solving is pp.35-42 of the 1962 text.
- **Anomalies** are first ignored or explained away. Only a build-up of anomalies that undermine the practice causes **crisis** (pp.66-76).
- **Revolution** revises the matrix. No rule compels the choice of the new framework. The new framework may lose some old explanations ("Kuhn-loss", pp.99-100).
- Book facts: 264 pages in 1962; second edition 1970; over 1 million copies; 16 languages.
- Kuhn compared a paradigm change to a Gestalt switch (duck-rabbit). The SEP entry notes he was unsure whether this was an analogy or a general fact about the mind (a02).
- Kuhn gives no quantitative threshold for when anomalies become crisis (a01).

### 2.2 Incommensurability (a03)

Kuhn (1962) said rival paradigms lack a common measure, so partisans only partly communicate. After 1987 he narrowed it to **taxonomic** incommensurability: kind terms cannot cross-classify unless one is a species of the other (the no-overlap principle). Kuhn (2000 [1991]) said it is "far from being the threat to rational evaluation of truth claims". For the agent: a new frame may need new terms, and old tests may not map onto it.

### 2.3 Critics (a05)

Popper and Lakatos (1965 Bedford College symposium, 1970 volume), Feyerabend, and Toulmin (change is more frequent and less dramatic than Kuhn says). Copernicus used about as many epicycles as Ptolemy (Koestler count 48 vs 40). Clairaut explained lunar precession in 1750 after about 60 years of failed attempts.

### 2.4 The oxygen case (a04, a06, a16)

- Becher's terra pinguis 1667; Stahl named phlogiston 1703. Stahl never explained mass gain when tin and lead burn.
- Defenders added **auxiliary patches**: Boyle's negative mass idea, Guyton de Morveau's "lighter than air" phlogiston. This is the "peripheral change" response (see 2.6).
- Oxygen identified about 1771, named 1777; nitrogen 1772. Cavendish and Priestley were phlogiston adherents who still found the key data.
- Air was thought an element; in the 1780s it was shown to be a mixture. Thagard calls this reclassification "branch jumping".
- The SEP entry itself calls the oxygen example "somewhat stretched" (a01). Butterfield called it the "postponed revolution". Treat it as narrative, not as a measured case (K23).

### 2.5 Theories of conceptual change in learners (a08-a14, a29, a30)

| Account | Claim |
|---|---|
| Posner, Strike, Hewson, Gertzog (1982) | Four conditions for giving up an old conception: dissatisfaction, the new one is intelligible, plausible, fruitful. Built on Kuhn and Piaget. Theory paper, no data (a11, b15). Not opened. |
| Chi (1992) | Naive concepts sit in the wrong ontological category (matter instead of process); change is a category shift. |
| Vosniadou | Framework theory with entrenched presuppositions. Children merge the taught round earth with the observed flat earth into synthetic models: "two earths" or a sphere with people inside (a10). |
| diSessa | Knowledge in pieces; change is reorganisation of many small resources. |
| Carey (1985) | Many 4-year-olds treat tables and clocks as alive because they move; by 10 most have the adult concept of living thing. Children under 7 often do not count people and insects as animals (a09). |
| Gopnik and Meltzoff (1997) | "Theory theory": infants' development resembles scientists' theory change. Ages 6, 9, 18 months are given for steps in object knowledge (a30). |
| Thagard (2002, 2014) | Conceptual change in science moves by reclassification; scientists compare explanatory coherence of two theories; children's change may be piecemeal (a08, a16, a29). |

Whether children's change equals scientists' change is not settled (K24).

### 2.6 What people do with an anomaly (a12, b27)

Chinn and Brewer (1993) sort responses into seven: **ignore, reject, exclude** as outside the theory's scope, **hold in abeyance, reinterpret, peripheral theory change, theory change**. Only the last is full conceptual change. The taxonomy comes from memory of the paper; the paper was not opened (publisher blocked, d15). Student think-aloud work (b24) fits: six students, about 16 hours in a physics lab, and what they did (keep, remove, recollect, mitigate) depended on the cause they gave for the anomaly.

Festinger, Riecken and Schachter (1956): after the predicted end of the world on 21 Dec 1954 failed, most believers kept their framework (a13). Participant counts not read.

Bruner and Postman (1949): playing cards with anomalous suits (red six of spades) needed longer exposure to be named; subjects first saw normal cards, then showed hesitation (a07). **Figures are from memory and unverified.** Do not use the numbers.

### 2.7 Scientists in the lab (b26, d16)

Dunbar (1997): in molecular biology labs, unexpected results were common, and groups usually first blamed method, later changed the model. Counts were not read (K22, contested). Kulkarni and Simon (1988) built KEKADA, which reacts to surprising results by focusing follow-up experiments on the surprise (c25; full text blocked).

## 3. Core findings with exact numbers

Status key: E = established (two or more independent sources, opened), S = single source, C = contested, O = open question.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Kuhn: anomalies are ignored first; crisis comes from accumulation. No threshold. | pp.35-42, 66-76 | a01, a04 | E (as theory) |
| Intrinsic self-correction hurts non-reasoning models | GPT-3.5 CSQA 75.8 -> 38.1 (one round) -> 41.8 (two); GPT-4 GSM8K 95.5 -> 91.5 -> 89.0; GPT-4 HotpotQA 49.0 -> 49.0 -> 43.0 | Huang 2024 (b07, c07) | E |
| With oracle labels revision helps | GPT-3.5 GSM8K 75.9 -> 84.3; GPT-4 GSM8K 95.5 -> 97.5; CSQA GPT-3.5 75.8 -> 89.7; GPT-4 HotpotQA 49.0 -> 59.0 | Huang 2024 Table 2 (critique correction) | E |
| Self-correction blind spot | 14 non-reasoning models, mean blind spot 64.5%; "Wait" cuts it 89.3%; DeepSeek-V3 0.567 -> 0.902 with Wait vs R1 0.908; datasets SCLI5 286, GSM8K-SC 1,313, PRM800K-SC 448 | Tsui 2025 (d01, d02) | S |
| Plain challenge flips answers | 67,640 runs, 10 models, 7 tasks: mean flip 46%, mean drop 17%; GPT-4 flips 10.4% of correct, 30.3% of wrong | Laban 2023 FlipFlop (d03) | S |
| Naive revision overturns correct answers | About 38% of correct MATH answers turned wrong (PaLM 2-S*) | Snell 2024 (d04) | S |
| Contrast of two frames cuts toxic reflection | Toxic reflections 52 -> 11; GSM8K GPT-3.5: CoT 76.6, self-reflection 75.8, SC-vote 83.5; Self-Contrast 84.4 vs best-of-5 81.8 | Zhang 2024 (d06) | S |
| Reflexion with external failure signal | +22% AlfWorld, +20% HotPotQA, +11% HumanEval; HumanEval 91% vs GPT-4 80%; reflection beats episodic memory alone by +8% on HotPotQA; Rust (50 hardest) 0.68 vs 0.60 without reflection, 0.52 without tests | Shinn 2023 (c11, d05) | E |
| Reflexion trigger is counted | Same action and response more than 3 cycles, or more than 30 actions; stop after 3 consecutive failures | d05 | O (never swept) |
| Refutation text helps humans | g=0.41, 95% CI [0.30, 0.51], 44 comparisons, 33 studies, n=3,869, I2 about 61%; trim-and-fill g=0.28 [0.16, 0.39] | Schroeder and Kucera 2022 (b01, b02) | E |
| Refutation moderators | Domain, images (k=9), medium, length, test timing all not moderating | b03 | E |
| Refutation by grade (older review) | Helped grades 3-10 (10 studies), not K-2 (1) or grade 11+ (11) | Tippett 2010 via b04 | C |
| Refutation text, large single effect | N=157, d=2.34, t(153)=7.32; 98.1% erred at pretest | p-value study 2026 (b23) | S |
| Old info stays active after correction | Persistence d=0.75 to 1.06 (52 samples, N=6,878); debunking d=1.14 to 1.33; no backfire | Chan 2017 (d10) | E |
| Illustrations do not remove old info | Exp 1 N=322; Exp 2 N=357 (with causal explanations) | b17 | S |
| Backfire does not replicate | N=1,156, three experiments; backfire only under induced skepticism, open responses only | d11 | E |
| Person-impression persistence inconsistent | 1 of 3 experiments shows continued influence | d12 | S |
| Transition states with two theories | 5-year-olds, N=102: transition theorists 34% (35/102) to 50% (51/102); mass theorists 13% to 27%; control 3/34 vs 12/34 per evidence arm | b21, b22 | S |
| Training does not remove misconceptions | N=953; adherence to correct rule fell with experience r=-.267, p<.001 | b19 | S |
| Counterfactual tasks | 11 task pairs; GPT-3.5 parseable drawing code 99% -> 62%, 71%, 75% on flipped and rotated settings; base-9 worse than base-8 and base-16; GPT-4 passes comprehension check but fails task | Wu 2024 (a18, b09, d09) | S |
| Memory vs evidence | ChatGPT keeps memory answer 3.7% (no support) vs 99.8% (all support); GPT-4 8.9% vs 99.8%; 80% memorisation on popular questions; order shifts over 5 points (over 30 for PaLM2, Llama2-7B) | Xie 2024 (b05, b06) | S |
| Belief revision weak | Belief-R, about 30 models: GPT-4-Turbo BU 19.65, BM 82.69, BREU 51.17; Llama-3 70B 10.99 / 92.09 / 51.54; best BREU about 50; CoT and plan-and-solve add about 1 point | Wilie 2024 (a19, a20, c19) | S |
| Discovery agents fail the full cycle | Best agent completes 38% easy, 18% challenge; Hypothesizer finds 34% / 8% of gold knowledge; humans 66% completion, 55% knowledge (16 tasks, up to 11 scientists); unit tasks about 60%+ | DiscoveryWorld (a21, a22, b12) | S |
| Parallel frames tested as code | ARC 100-task subset: direct 17%, program 23%, LLM summaries 30%, human pick 33%; 33 of 49 (67%) correct programs; SyGuS 94.3% | Wang 2024 (b11, c17) | E (with ACRE) |
| Propose-test-refine | ACRE: IO 28.0, SC N=5 29.0, self-refine 32.0, T=1 N=1 45.0, T=3 N=5 59.0; MiniSCAN 0.0 -> 46.0; MiniARC 13.8 -> 14.6 | Qiu 2024 (c15) | E |
| Noisy exemplars hurt rule induction | Accuracy fell at 12.5%, 25%, 50% corruption; noise warning reduced the drop only | c16 | S |
| Bayesian surprise as signal | 21 datasets; 5-29% more LLM-surprising discoveries at budget 500; human surprisal rating 0.67 (CI 0.63-0.71) vs 0.11 direct LLM, 1,620 hypotheses, 3 annotators each; 67% of surprising findings also surprise experts (500+) | AutoDiscovery (a23, a24, c18) | S |
| Kuhn agent did not beat blind sampling | Full scaffold B 0.8027; no scaffold 0.8612; floor prompt 0.8906 (+0.1159); one-shot best-of-15 0.8463; 7 of 10 arms fail nulls; 17 of 64 iterations improved (26.6%) | Smith 2026 (c01-c06, d08) | S |
| Scaffold cost is context | Cache re-reads 2.5x counted tokens; explicit reasoning 2.5% of spend; full scaffold 111.4M tokens per run vs 15M for fifteen pulls | c04 | S |
| Aha under RL | R1-Zero AIME 2024 15.6% -> 77.9%; "wait" frequency rises | DeepSeek-R1 (c12) | C |
| Overthinking and collapse | Near-zero accuracy past a model-specific complexity; easy puzzles overthought | Shojaee 2025 (c13) | C |
| Budget forcing with "Wait" | s1-32B AIME24 50.0% -> 57% | Muennighoff 2025 (d13) | S |
| Coherence net settles fast | ECHO: more than a dozen cases, some over 150 propositions, under 200 cycles; SDP at least 0.878 of optimum | Thagard and Verbeurgt 1998 (a15) | S (human-modelling only) |
| BoxingGym | 10 environments; explicit-model tool does not reliably beat plain LLM; hyperbolic discounting stays poor | Gandhi 2025 (a25, a26) | S |

## 4. Mechanisms and models

### 4.1 Kuhn trigger as a counted state machine

```
state: frame F, fail_count n, best_score
on each external check:
    if pass: n = 0
    else: n += 1
    if n >= N: fire IMPASSE (reframe)
```

- Smith 2026 fires after 5 or more consecutive non-crashing rejections (d08). Reflexion reflects after more than 3 repeated cycles and stops after 3 consecutive failures (d05).
- Neither paper swept N. Our design should sweep N = 1, 2, 3, 5 (K29).
- The signal must come from code (test, score, tool), not from the model's feeling of doubt (K04).

### 4.2 Reframe levels (K22, K02)

Order the response by cost and by Chinn and Brewer:
1. Re-check data and procedure (blame method first, as Dunbar reports).
2. Name the cause of the failure (students' choice depended on the stated cause, b24).
3. Peripheral change (patch).
4. Change the frame itself (O8).

### 4.3 Reframe step with a select guard (K26)

1. Keep first answer A1 and its check result.
2. Show the failing output (located by code, G2). Name the old frame and why it fails (refutation form, K09).
3. State the new frame in one sentence; solve under it in a fresh context.
4. **Select** with code (test, vote, verifier). The guard must be able to keep A1.

Reason: naive revision overturns about 38% of correct answers (d04); a challenge flips 10.4% of GPT-4's correct answers (d03). Contrast of two frames cut toxic reflections 52 -> 11 (d06).

### 4.4 Parallel frames (K15)

Sample K different frames (in words), implement each as a checkable program, run them on the examples, keep those that pass. This is Hypothesis Search: 17% -> 30% on ARC. The selector is external (programs on examples).

### 4.5 Two live frames and a coherence tally (K13, K11)

Humans hold old and new conceptions side by side (transition states 34% to 50%). ECHO-style tally: nodes for evidence and frames, excitatory links where a frame explains evidence, inhibitory links where frames contradict. Settle by iteration (under 200 cycles). A simple version for our agent: for each rival frame count explained items and contradicted items from the test log; choose by the tally. No LLM test exists (d20).

### 4.6 Bayesian surprise as impasse detector (K17, K32)

Sample the model's belief answer n times before evidence and n times after. Fit Beta(1+k, 1+n-k) to each. Surprise is a flip in leaning. Use five answer categories mapped to 0, .25, .5, .75, 1 plus "cannot comment", because boolean elicitation overestimated belief (d14). Cost: two sample sets plus the experiment. Not compared with a failed-test signal.

### 4.7 Retired-frame note (K10)

Old information stays active after correction (competition for activation, KReC, b16). Implementation: after a reframe, write "retired: <old claim>, reason" in working state, and run a leak check that scans later steps for the retired claim.

### 4.8 Cheap re-read baseline (K27)

Append "Wait" and let the model re-read. For non-reasoning models this cut the blind spot 89.3%. This is the null any heavier reframe operator must beat.

## 5. What holds up

**Replications and meta-analyses**
- Refutation text: meta-analysis g=0.41 shrinks to 0.28 after trim-and-fill, 10 studies imputed. Heterogeneity is moderate (I2 about 61%). No moderator worked. The older grade pattern (no help at grade 11+) is contested.
- Persistence of corrected misinformation: robust in a 52-sample meta-analysis (d=0.75 to 1.06). Backfire did not replicate (N=1,156). Person-impression persistence is inconsistent (1 of 3).
- Self-correction: Huang's negative result is confirmed by Kamoi's survey (no prompted-LLM success without external feedback) and by Self-Contrast (self-reflection -0.8% GSM8K, +0.7% SVAMP, not significant).

**Failures and limits**
- Smith 2026: the full loop scored below blind sampling; 7 of 10 arms failed the nulls. Single preprint, one domain (DNA motifs), n=10 runs per arm.
- Kuhn cycle: no quantitative test exists; oxygen case is stretched (K23).
- Bruner-Postman, Posner, Chinn and Brewer, Dunbar, Shtulman and Valcarcel, Vosniadou and Brewer: primary papers not opened, numbers unverified.
- Child studies: 5-year-olds (N=102) may not transfer to models.

**Moderators that matter**
- External signal present or absent (largest: Huang oracle vs none; Reflexion with tests 0.68 vs 0.52 without).
- Model type: reasoning-trained models show near-zero blind spot; prompted non-reasoning models do not (d01, d02).
- Task difficulty: easy items favour sequential revision, hard ones a balance with parallel sampling (d04); reasoning collapses past a complexity threshold (c13).
- Fact popularity: stickiness grows with popularity (b06).
- Error source: wrong answers flip more than right ones, but right ones still flip.

**Interventions that worked**
- Verbal lesson after an external failure (Reflexion).
- Contrast of two frames (Self-Contrast).
- Propose, test, refine with a symbolic interpreter (ACRE 28 -> 59).
- Several hypotheses tested as programs (ARC 17 -> 30).
- "Wait" re-read for non-reasoning models.
- Refutation text for humans.

**Interventions that did not work**
- Model-judged self-review without signal (Huang).
- "Your answer could be right or wrong" instruction (did not remove the drop).
- Chain of thought on Belief-R (about +1 point).
- Warning about noisy exemplars (reduced the drop only).
- Illustrations or causal explanation against old-fact activation (b17).
- Heavy scaffolding with forced worksheets (arm I 0.8179 vs floor 0.8906).
- Explicit model-fitting tool in BoxingGym.

## 6. Language models

**Self-correction.** Prompted non-reasoning models cannot tell when their own answer is wrong. Huang (2024): GPT-3.5 CommonSenseQA 75.8 -> 38.1 after one round because false options look relevant and the model changes too often. GPT-4 GSM8K 95.5 -> 89.0 after two. With oracle labels the same models gain (GPT-4 HotpotQA 49.0 -> 59.0). Kamoi (2024) generalises: success needs reliable external feedback or large-scale fine-tuning.

**Update of that result.** Tsui (2025) shows the failure is a blind spot specific to own output. The same error is caught far more often when framed as the user's. Average blind spot 64.5% over 14 models. Reasoning-trained models have near-zero blind spot. "Wait" lifts DeepSeek-V3 from 0.567 to 0.902, close to R1 at 0.908. Budget forcing with "Wait" gave s1-32B 50.0% -> 57% on AIME24.

**Challenge sensitivity.** FlipFlop: 46% mean flip, 17% mean accuracy drop. Fine-tuning cuts the drop by 60% (not to zero). Belief-R shows the same trade-off: models that update well fail to maintain correct beliefs. GPT-4-Turbo has BU 19.65 and BM 82.69; Llama-3 70B has BU 10.99 and BM 92.09. Both end near 51 combined.

**Stored frame.** Counterfactual tasks (Wu 2024) cut accuracy even when procedure is unchanged, and GPT-4 passes a comprehension check yet fails the task. Xie (2024): coherent counter-evidence is accepted (3.7% memory use for ChatGPT when no evidence supports memory), but mixed evidence leaves the model clinging (80% memorisation for GPT-4 on popular facts).

**Discovery.** DiscoveryWorld: best agent 38% easy, 18% challenge, humans 66%. Unit tasks are fine, so chaining and revising is the weak part. BoxingGym: experiment design and model proposal weak. AutoDiscovery: Bayesian surprise tracks human surprise (0.67 vs 0.11 rating).

**Frames as hypotheses.** Hypothesis Search (ARC 17 -> 30%) and Qiu (ACRE 28 -> 59) show that several frames tested by code help. Qiu also shows the model is a weak applier of its own rules.

**Reasoning models.** The "aha" signal appears under RL (AIME 15.6% -> 77.9%) but no controlled test shows that rethinking causes the gain. Reasoning collapses past a complexity threshold and overthinks easy items. Reconsideration is not free.

**Kuhn agent.** Smith (2026) is the only direct use of Kuhn in an agent. The Kuhn side-agent got the task text but not the history, was handed a random assumption to violate and a random domain to import, and made almost no web-search calls. The phase took 63 runs and 33.5M tokens of 229.0M total. The full scaffold (0.8027) lost to the floor prompt (0.8906) and to one-shot best-of-15 (0.8463). The Kuhn agent was not an ablation arm, so its own effect is unknown. Selection among independent draws, not the loop, paid.

**Refutation for LLMs.** Not tested. Nearest: Reflexion's explain-failure (+8% HotPotQA), Self-Contrast.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = lesson store (S9).

### Add now (established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Reframe or revise only on an external failure signal (test, tool, score), never on model doubt. Already G1 and G2; this adds the numbers. | G1, G2, S6 | [E] | b07, c07, c09, c10, d01, d05, d07, d19 (K03, K04) |
| Every reframe is paired with a select step that can keep the first answer. | O8 guard, G5 | [E] | d03, d04, d06 (K26) |
| After an external failure, write one verbal lesson and retry; do not retry blind. Keep the lesson in memory. | S5, S9 | [E] | c11, d05 (K05) |
| Generate several different frames and test each as a program on the examples; select by code. | S3, S4 | [E] | b11, c15, c17 (K15) |
| Anomalies are not all frame failures: first re-check data and procedure, then patch, then change the frame. Treat the oxygen case as narrative only. | S6 order | [E] for the response taxonomy (a12 unopened, b24 opened) | a01, a12, b24, b27 (K01, K02) |
| Do not add: model-fitting stage by default (BoxingGym), forced worksheets, debate. | 4b | [E]/[S] | a26, c05 |

### Test first (not yet established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| Consecutive-failure trigger with N tuned (1, 2, 3, 5) vs reframe at first failure vs best-of-N. | G1, S6 | [S]/open | d05, d08 (K29, K19) |
| Refutation-form reframe prompt (name old frame, why it fails, new frame) vs "try another approach". | O8 | [S] | b01, d05, d06 (K09, K28) |
| "Wait" re-read as the cheap baseline and as an O8 control. | O8 | [S] | d01, d02, d13 (K27) |
| Retired-frame note and leak check after reframe. | memory, S6 | [S] for humans only | b16, d10 (K10) |
| Two live frames with a coherence tally of explained vs contradicted items. | S5, S7 | [C] | a15, c23 (K13, K33) |
| Bayesian surprise as impasse detector on single-answer tasks. | S6 | [S] | c18, d14 (K17, K32) |
| Frame restatement before solving, on counterfactual tasks. | S1, O8 | open | d09, d18 (K31) |
| Difficulty routing: cheap parallel draws first, reframe only on unsolved items. | G12, S0 | [C] | d04, d08 (K30) |
| Counterfactual probe to flag stored-frame dependency. | S1 | [S] | a18, d09 (K06) |
| Outlier check step for a wrong exemplar. | S2, G3 | [S] | c16 (K16) |

## 8. Concrete tests on our bench

All arms get the same token cap, counting setup cost (G7). Include a best-of-N one-shot arm as the null (Smith 2026 showed it can beat a loop).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Trigger count | ARC items with an example-based check; multi-step puzzles | Reframe at N=1, 2, 3, 5 consecutive failed checks; best-of-N one-shot | Solved rate at equal tokens; reframes fired per item | Small N wastes tokens and flips good answers; large N wastes budget; expect a middle N to beat best-of-N by a few points, or no arm to beat it (then drop O8 trigger work) |
| T2 Refutation reframe | Items that reach S6 | Plain "try a different approach"; explain-failure line; named-old-frame refutation (old frame, why it fails, new frame) | Solved rate among items that reached S6 | Refutation at or above explain-failure; both above plain retry (Reflexion +8%) |
| T3 Wait baseline | Same items | "Wait" re-read; heavy reframe operator; no revision | Solved rate; correct-to-wrong rate | Wait matches or beats heavy reframe on non-reasoning models; no gap on reasoning models |
| T4 Flip guard | Items whose first answer was correct | Reframe without select; reframe with select that can keep A1 | Correct-to-wrong rate | Without select about 10-38% loss; with select under 5% |
| T5 Counted vs model-judged trigger | Mixed items | Model says "I doubt this"; failed-test count; consecutive non-improving iterations | Solved rate; false-trigger rate | Test-based triggers win; model doubt about equal to or below no trigger |
| T6 Parallel frames vs retry | ARC items | K different frames each run on examples; one frame retried K times | Solved rate at equal tokens | Frames beat retry, as 17 -> 30% in Hypothesis Search |
| T7 Retired-frame leak | Multi-turn items with a correction inserted in context | No note; retired-frame note | Rate the old claim reappears | Note lowers leakage; first measure baseline leak rate (no LLM data exists) |
| T8 Coherence tally | Items with two plausible frames and a log of evidence | Free choice; explained-minus-contradicted tally | Selection accuracy | Tally at or above free choice when the log is accurate |
| T9 Surprise signal | Single-answer tasks | Bayesian surprise (2 x k samples); one failed check; self-consistency disagreement | Precision and recall of "this item will fail"; tokens per signal | Failed check wins on cost; surprise adds only where no check exists |
| T10 Restatement | Counterfactual arithmetic and spatial tasks | Solve directly; restate under the new frame, then solve | Accuracy on counterfactual form | Unknown; Wu shows comprehension check alone does not fix it |

## 9. What does not transfer, and why

- **The Kuhn cycle as a quantity.** No threshold, no controlled test, and the oxygen case is stretched. Use as a shape, not a number.
- **Gestalt switch and incommensurability.** Describe human perception and communities. An LLM has no stable perceptual frame to switch; the frame is in the prompt and can be rewritten for free.
- **Child studies.** 5-year-olds' balance theories (N=102) and earth models measure learning over days. An agent's reframe is within one run.
- **Refutation text effect sizes.** They measure human readers with delayed tests. LLM transfer is untested; Huang shows "your answer may be wrong" does not help models.
- **Persistence of old information.** Shown in reading times and rating tasks. No LLM context-window test exists.
- **Social side** (community, authority, generational change). The single agent has no community. Treat in the social epistemology subfield.
- **Training-based gains** (RISE, fine-tuning for self-correction, RL "aha"). Our agent does not train.
- **Posner conditions.** A teaching model with no opened data. A checklist is cheap, but there is no evidence it helps a model.

## 10. Open questions

1. Does the count N matter, and is there a good default? (Gap 1; no study varies N.)
2. What does the Kuhn agent add inside Smith's loop? No on/off arm exists; v2 is the latest version.
3. Does name-the-old-frame refutation beat explain-failure for LLMs? (Gap 3.)
4. Does an ECHO-style tally help an LLM choose between frames? (Gap 4; no study found.)
5. What are the exact counts in Chinn and Brewer 1993 and Dunbar 1997? (Gap 5; not opened.)
6. Do retracted claims persist in LLM context windows? (Gap 6; none found.)
7. Do reasoning models with tools judge their own anomalies reliably on open-ended tasks? (Gap 7 partly closed.)
8. Is Bayesian surprise cheaper or better than a failed check as impasse signal? (Gap 8.)
9. Does restating the frame before solving recover counterfactual drops? (Gap 9.)
10. What fraction of correct first answers does our reframe operator overturn at equal tokens? (Gap 10: measured for other operators only.)
11. Is the failure of Smith's scaffold due to context cost (2.5x cache re-reads) or to the loop design?

Search note: arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429 during the gap search, so "not found" means not found, not absent.

## 11. Sources

[V] = opened and read this session; [M] = snippet or abstract page only; not opened.

- [V] SEP, Thomas Kuhn. https://plato.stanford.edu/entries/thomas-kuhn/ (a01, a02)
- [V] SEP, Incommensurability. https://plato.stanford.edu/entries/incommensurability/ (a03)
- [V] SEP, Scientific Revolutions (first 100k of 156k characters). https://plato.stanford.edu/entries/scientific-revolutions/ (a04)
- [V] Wikipedia, The Structure of Scientific Revolutions. https://en.wikipedia.org/wiki/The_Structure_of_Scientific_Revolutions (a05)
- [V] Wikipedia, Phlogiston theory. https://en.wikipedia.org/wiki/Phlogiston_theory (a06)
- [M] Bruner and Postman (1949). https://doi.org/10.1111/j.1467-6494.1949.tb01241.x (a07, figures unverified)
- [V] Thagard (2002) Conceptual change. https://www.arts.uwaterloo.ca/~pthagard/Articles/conc.change.pdf (a08-a10, a29, a30)
- [M] Posner et al. (1982). https://doi.org/10.1002/sce.3730660207 (a11, b15)
- [M] Chinn and Brewer (1993). https://doi.org/10.3102/00346543063001001 (a12, b27, d15)
- [V] Wikipedia, Conceptual change. https://en.wikipedia.org/wiki/Conceptual_change (a13, a14)
- [V] Thagard and Verbeurgt (1998). https://www.arts.uwaterloo.ca/~pthagard/Articles/coherence.1998.pdf (a15)
- [V] Thagard (2014). https://www.arts.uwaterloo.ca/~pthagard/Articles/thagard.explanatory.sci&ed.2014.pdf (a16)
- [V] Thagard (2006/2008). https://www.arts.uwaterloo.ca/~pthagard/Articles/conc.change.life.pdf (a17)
- [V] Wu et al. (2024) Reasoning or Reciting. https://arxiv.org/abs/2307.02477 (a18, b09, b10, c20, d09)
- [V] Wilie et al. (2024) Belief-R. https://arxiv.org/abs/2406.19764 (a19, a20, c19)
- [V] Jansen et al. (2024) DiscoveryWorld. https://arxiv.org/abs/2406.06769 (a21, a22, b12, b13, c14)
- [V] Agarwal et al. (2025) AutoDiscovery. https://arxiv.org/abs/2507.00310 (a23, a24, c18, d14)
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540 (a25, a26, c21)
- [M] Guzzetti et al. refutation research. https://doi.org/10.2307/747886 (a27)
- [M] Thagard (1989) Explanatory coherence. https://doi.org/10.1017/S0140525X00057046 (a28, c23)
- [V] Schroeder and Kucera (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8784251/ (b01-b04, b14, b16)
- [V] Xie et al. (2024) Adaptive Chameleon or Stubborn Sloth. https://arxiv.org/abs/2305.13300 (b05, b06)
- [V] Huang et al. (2024) LLMs cannot self-correct yet. https://arxiv.org/abs/2310.01798 (b07, b08, c07-c09)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/abs/2309.05660 (b11, c17)
- [V] Outdated-information activation (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13736437/ (b17, b18)
- [V] Falling-bodies prevalence study (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10249391/ (b19, b20)
- [V] Balance-theory study, 5-year-olds (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC7387500/ (b21, b22)
- [V] Extended refutation text and humor (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13198534/ (b23)
- [V] Student sensemaking with anomalous data (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11659860/ (b24)
- [V] Plausibility transition model (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10251660/ (b25)
- [M] Dunbar (1997). https://doi.org/10.1037/10226-003 (b26, d16)
- [M] Shtulman and Valcarcel (2012). https://doi.org/10.1016/j.cognition.2012.04.005 (b28)
- [V] Smith (2026) The Little Scientist. https://arxiv.org/abs/2608.16951 and https://github.com/travis42/little-scientist-dale (c01-c06, d08)
- [V/M] Kamoi et al. (2024) survey. https://arxiv.org/abs/2406.01297 (c10 opened; d07 abstract only)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c11, d05)
- [V] DeepSeek-AI (2025) R1. https://arxiv.org/abs/2501.12948 (c12)
- [V] Shojaee et al. (2025) Illusion of Thinking. https://arxiv.org/abs/2506.06941 (c13)
- [V] Qiu et al. (2024) Hypothesis refinement. https://arxiv.org/abs/2310.08559 (c15, c16)
- [V] Zhu and Rzeszotarski (2025). https://arxiv.org/abs/2407.01929 (c22)
- [V] Wikipedia, Explanatory coherence. https://en.wikipedia.org/wiki/Explanatory_coherence (c24)
- [M] Kulkarni and Simon (1988) KEKADA. https://doi.org/10.1207/s15516709cog1202_1 (c25)
- [V] Tsui (2025) Self-Correction Bench. https://arxiv.org/abs/2507.02778 (d01, d02)
- [V] Laban et al. (2023) FlipFlop. https://arxiv.org/pdf/2311.08596 (d03)
- [V] Snell et al. (2024). https://arxiv.org/pdf/2408.03314 (d04)
- [V] Zhang et al. (2024) Self-Contrast. https://arxiv.org/pdf/2401.02009 (d06)
- [M] Qu et al. (2024) RISE. https://arxiv.org/abs/2407.18219 (d17)
- [M] Deng et al. (2023) Rephrase and Respond. https://arxiv.org/abs/2311.04205 (d18)
- [M] Gou et al. (2024) CRITIC. https://arxiv.org/abs/2305.11738 (d19)
- [V] Chan et al. (2017) Debunking meta-analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC5673564/ (d10)
- [V] Backfire replication (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10317933/ (d11)
- [V] Continued influence on person impressions (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12058158/ (d12)
- [V] Muennighoff et al. (2025) s1. https://arxiv.org/pdf/2501.19393 (d13)
- [M] Negative search result (Crossref, Europe PMC). https://api.crossref.org/works (d20)
