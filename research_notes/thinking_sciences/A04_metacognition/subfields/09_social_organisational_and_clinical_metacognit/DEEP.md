# Social, organisational and clinical metacognition: deep document

*Subfield A04.09. Evidence ids (a01-a28, b01-b25, c01-c28, d01-d16) refer to evidence_a-d.jsonl in this folder. Claim ids K01-K23 refer to claims.jsonl. Status marks follow SCHEMA.md: [E] established, [S] single source, [C] contested. Same-paper lines are counted once (see critique.md). Search budget in the last gap run was limited (APIs rate-limited), so "not found" means "not found here".*

**Verdict in one line.** The clinical half (Wells' metacognitive therapy, Demetriou's development theory) is human evidence and does not transfer to our agent. The social half (theory of mind in LLMs, dyad and group confidence, debate, self-correction) gives real guidance: tracking what another party knows needs an explicit step, standard ToM scores overstate skill, and self-revision without an outside signal does not help.

## 1. What it is

The subfield covers metacognition when other minds, groups or clinical symptoms are involved. It has four blocks.

1. **Beliefs about others' minds.** Theory of mind (ToM): tracking what another party believes, knows, intends or feels. Metacognition applied to other people. Tests: false belief (Sally-Anne style), faux pas, irony, strange stories, nested belief ("A thinks B thinks X"), and behaviour prediction from belief.
2. **Social metacognition in groups.** Two or more minds share confidence to decide together. Founding work: Bahrami et al. 2010 (dyads), Frith 2012 (review). The LLM analogue: multi-agent debate and conformity.
3. **Clinical metacognition.** Wells' metacognitive therapy (MCT): treat disorder by changing beliefs about thinking (worry is uncontrollable, rumination is useful) and by training detached mindfulness. Related: metacognitive training for psychosis. Wells and Matthews' S-REF model is the theory (a26, not opened; see section 11).
4. **Developmental metacognition.** Demetriou's theory: general intelligence g shifts from executive to inferential to self-awareness processes with age (a24).

Why it is in our study: the agent is one model with a scaffold. Block 1 matters when the task involves a user, a counterpart or a witness. Block 2 matters for ensembles of runs. Blocks 3 and 4 matter only as analogies. The index row says "does not transfer", and the evidence agrees for blocks 3 and 4.

## 2. History and theories in depth

**Theory of mind in humans.** The false-belief task asks where a person who missed a change will look. Children pass around age 4 to 6. Kosinski uses a meta-analysis of 178 child studies as a rough anchor (a01). Later batteries add higher-order belief, faux pas and irony (Strachan 2024, a14).

**First LLM tests (2022).** Sap, Le Bras, Fried and Choi tested GPT-3 (davinci): SocialIQa 55%, ToMi 60%, more than 30 points below humans on SocialIQa. Going from 10 to 35 shots added about 1 point (a06). Their reading: models learn from text, not from interaction, so pragmatics is missing (a07, no exact numbers).

**The scale story (2023).** Kosinski reported that ToM "emerged" with scale: 0% for GPT-1/2 and early GPT-3, 5% davinci-002, 20% for davinci-003 and ChatGPT-3.5, 75% for ChatGPT-4 on 40 strict tasks (a01, c01). He added controls and noted word-order cues in older models (a03, a04), and says he does not aim to settle whether this is true ToM.

**The robustness backlash (2023).** Ullman showed that small changes break GPT-3.5: a transparent bag, a sighted or informed protagonist (a05, b14, c03). Shapira et al. ran "Clever Hans" stress tests and found large drops (c05). Strachan et al. added human data and showed that humans also fail some perturbation items (c08). The agreed reading: high score on standard items, brittle on altered items.

**Interactive and nested ToM (2023).** FANToM (Kim et al.) tests belief tracking in conversation where parties join and leave; Hi-ToM (Wu et al.) tests belief orders 0 to 4. Both show a large gap to humans (a08, a10, c09, c12).

**Knowing versus doing (2024-2026).** SimpleToM (Gu et al., ICLR 2026) separates "what does X know" from "what will X do" and "was X reasonable" (a11, a12).

**Fixes via prompts (2023-2025).** SimToM (Wilf et al.): filter the story to what the character knows, then answer (c15-c18). Thought-tracing (Kim et al. 2025): write a running hypothesis about mental state while reading (d01-d03).

**Group metacognition.** Bahrami et al. 2010 found that two people with similar sensitivity decide better together than the better person alone, when they share confidence in words (a17, a18). Bahrami 2012 and Pescetelli 2016 refined this (b10, b11). Frith 2012 reviewed the line (a16, a28). In LLMs the nearest line is multi-agent debate, which Zhu et al. 2026 model as a martingale (b17).

**Self-correction (2023-2024).** Huang et al. showed intrinsic self-correction lowers accuracy (c21). Tyen et al. showed that the bottleneck is finding the mistake, not fixing it (d04). Kamoi et al. surveyed: prompt-only feedback fails (d05).

**Metacognitive therapy.** Wells built MCT on the S-REF model (a26, not opened). Meta-analyses: Normann et al. 2014 (g 0.97 vs CBT, b20, quoted) then Normann and Morina 2018 (b01-b03, c25). Later single trials span depression, OCD, work return and PTSD (b04-b06, a22). Independent trials from 2025-2026 keep the symptom benefit but question the mechanism (b06, d10).

**Metacognitive prompting (2023).** Wang and Zhao borrowed the word "metacognitive" for a five-step self-evaluation prompt (a13, b16, c19). It is not MCT. The overlap is only the name.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| LLM false-belief score rises with scale | 40 strict tasks: GPT-1/2 and early GPT-3 0%; davinci-002 5% (CI 0-10); davinci-003 and ChatGPT-3.5 20% (CI 11-29); ChatGPT-4 75% (CI 66-84) | Kosinski 2024 (a01, c01) | [E] as a score; reading as ToM [C] |
| Task split for GPT-4 | Unexpected Contents 90%, Unexpected Transfer 60% (20 tasks each, chi2=8.07, P=0.01) | Kosinski (a02) | [S] |
| Controls lower older models | davinci-003: 90% before item updates, 60% after, 20% after true-belief controls. GPT-4: 95% then 75% | Kosinski (a03) | [E] |
| Trivial alterations break models | GPT-3.5 still says Sam believes the bag holds chocolate, P about 87-98%, when Sam can see inside | Ullman 2023 (a05, b14, c03) | [E] |
| Stress test drops | GPT-4 97% on original ToM-k; adversarial: other-person 93.8 (davinci-002) to 68.8 (GPT-4); inon 71.4 to 0; transparent access 66.7 to 0 | Shapira 2023 (c05) | [E] |
| Humans fail perturbations too | 757 humans failed half of the perturbation items | Strachan 2024 (c08) | [S] |
| 2022 baseline | GPT-3 SocialIQa 55%, ToMi 60%; 10 to 35 shots adds about 1 point | Sap 2022 (a06) | [S], old model |
| Interactive ToM gap | FANToM ALL: humans 87.5; GPT-4 0613 + CoT 26.6 (June), 14.8 (Oct); ChatGPT + CoT 3.7; Llama-2 chat + CoT 0.4; fine-tuned Flan-T5-XL 53.7 | Kim 2023 (a08, c09-c11) | [E] |
| Nested belief | Hi-ToM: all 4 models under 60%. GPT-4-32k vanilla 60.42 / 55.81 (no deception / deception); CoT 64.04 / 55.72 (+3.60 / -0.09). Joint accuracy at order 3+ about 0.05-0.35 | Wu 2023 (a10, c12) | [E] |
| Backward belief inference | Humans 82% true-belief, 72% false-belief; most models far below chance there. GPT-4 0.858/0.861 vs Claude-2 0.675/0.708 | Gandhi 2023 (c13) | [S] |
| Knowing-doing gap | Mental state over 95% for frontier models; behaviour prediction 30+ points lower; GPT-3.5 7.6%; o1-preview 84.1%; judgment 10-24.9% (below chance) for GPT-4o, Llama-405B, Claude-3.5 | Gu 2026 SimpleToM (a11) | [S] |
| Reminder fix | Behaviour prediction above 80% for all; judgment still 42.2% (GPT-4o), 25.8% (Llama-405B). One GPT-4o item 49.5 plain, 62.8 generic CoT, 87.4 custom CoT. Claude-3.5 97.1% with reminder plus custom CoT | Gu 2026 (a12) | [S] |
| SimToM perspective filter | GPT-3.5: ToMI false belief +47 over 0-shot CoT; BigToM false belief 70.5 (+29.5 over 0-shot, +14.2 over CoT); SC-CoT 33.5 vs SimToM 81.0. Oracle perspective 96. GPT-4: ToMI overall +13.4 over 0-shot CoT, slight drop on BigToM. Single-prompt variant BigToM total 58.25 (17.63 below 0-shot CoT) | Wilf 2023 (c15-c18) | [E] for gain on weak models; effect on GPT-4 small |
| Reasoning models fail true-belief twins | ParaphrasedToMi false/true: o1-low 98.5/37.0; o1-high 97.0/49.0; R1 77.0/59.5; GPT-4o 38.5/80.5; GPT-4o+CoT 76.0/58.0 | Kim 2025 (d02) | [S] |
| Thought-tracing beats reasoning models | ParaphrasedToMi: GPT-4o 59.5, +CoT 67.0, +TT 76.0, +TT+CoT 74.3; o1-medium 70.8; o3-mini-medium 64.0; R1 68.3. FANToM All: GPT-4o 11.1, +TT 41.5, +TT+CoT 54.7; o1-medium 30.2; R1 37.9. MMToM-QA: GPT-4o+TT+CoT 69.0, o1-medium 76.0 (o1 wins), R1 49.0 | Kim 2025 (d01, d03) | [S] |
| Human vs GPT-4 by test | Irony: GPT-4 above humans (P=0.040, r=0.32). Faux pas: below (P=5.4e-5, r=0.55); GPT-3.5 near floor; LLaMA2-70B above (P=0.002, r=0.44) but illusory. Human N=1,907 total, about 48-51 per test | Strachan 2024 (a14, b13, c06) | [S] |
| Faux pas failure is caution | Only 2 of 349 GPT answers said the speaker knew. Likelihood wording: GPT-4 100%; GPT-3.5 about 3% needed a prompt, about 9% failed | Strachan (a15, c07, d07) | [S] |
| Dyad benefit | Exp 1: 15 dyads, dyad above better member t(14)=5.24 p<0.001. Exp 2: equal noise t(10)=2.50 p=0.03; unequal noise t(21)=0.68 p=0.54 (no benefit). Rule: R2=0.51, slope 0.6, intercept 0.74 | Bahrami 2010 (a17, a18) | [E] for similar partners; numbers unverified (paywall) |
| Non-verbal confidence tool hurts | Verbal talk near optimal for similar partners; adding a non-verbal confidence tool lowered performance; with noise on one partner, dyad worse than better observer | Bahrami 2012 (b10) | [S] |
| Dyad metacognition additive | Sensory and social contributions to wagers linearly additive; mean member metacognitive sensitivity predicts dyad benefit | Pescetelli 2016 (b11) | [S] |
| Hetero-metacognition | Reading another's confidence matched self-evaluation (auditory task, abstract-level) | Vuillaume 2020 (b12) | [S] |
| Homogeneous debate has no gain | Qwen-7B: debate 5x5 vs majority vote GSM8K 0.847 vs 0.908; CSQA 0.727 vs 0.808. Diversity + confidence: GSM8K 0.932, CSQA 0.828, MMLU-FL 0.619 vs 0.548, GPQA 0.361 vs 0.335 | Zhu 2026 (b17) | [E] with F08/F10 |
| Intrinsic self-correction hurts | GPT-3.5 CSQA 75.8 to 38.1 (round 1) to 41.8 (round 2); GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0; HotpotQA 49 to 43; with oracle label GPT-4 GSM8K 97.5, HotpotQA 59.0 | Huang 2023 (c21) | [E] |
| Mistake finding is the bottleneck | BIG-Bench Mistake, 300 traces per task; GPT-4 step-level finding 52.87; with oracle location, backtracking changes originally correct traces by -6.7 to -11.4 and incorrect by +23.5 to +43.9 | Tyen 2024 (d04) | [E] |
| RL for self-correction | +15.6% MATH, +9.1% HumanEval over base (abstract only) | Kumar 2024 (d06) | [S], not opened |
| Metacognitive prompting | Avg over 4 models zero-shot: BoolQ 89.0 vs CoT 86.3; DDI 73.4 vs 69.4; MedNLI 70.9 vs 67.1; QNLI 92.6 vs 91.2; EUR-LEX +15.0 to +26.9 over CoT. Errors: 68.3% overthinking, 31.7% overcorrection | Wang and Zhao (a13, b16, c19, c20) | [S] |
| Token self-knowledge | P(True)>0.5 filter improves accuracy; AUROC about 0.6-0.85, models 800M-52B | Kadavath 2022 (b15) | [S] |
| MCT vs waitlist | g=2.06 (CI 1.52-2.60, k=9); 25 studies, 15 RCTs, 780 adults; pre-post 1.72, follow-up 1.57 | Normann and Morina 2018 (a19, b01, c25) | [S] clinical |
| MCT vs CBT | g=0.69 post (k=8), 0.37 follow-up (k=7, CI 0.07-0.66); trim-and-fill 0.53; earlier 0.97 (5 trials). 5 of 15 trials described allocation concealment | (b02, c25, b20) | [S] clinical |
| Allegiance | Wells-group g=1.98 vs independent 1.49, p=0.09; without Dammen outlier 1.84, k=12, p=0.19 | (a20, b03) | [S] |
| MCT by condition | GAD recovery 67.36% vs 42.86% CBT (RR 1.59, 3 studies); depression RCT N=39 d=2.51; work return 39% vs 20% (N=236, OR 2.39); PTSD g=2.878 (7 uncontrolled studies); 2026 depression meta g -1.28 vs control | (a21, b04, b05, d09, a22, d08) | [C] |
| OCD mechanism not supported | Independent RCT N=76: Y-BOCS diff -4.00 post (g -1.12), -6.92 at 6 months (g -1.54); belief-mediated indirect effect beta=-0.01 | Anwar 2026 (b06, d10) | [S] |
| Detached mindfulness alone | Primary outcomes g -1.80 (CI -2.84 to -0.76), k=3; depression g -1.15 | (d13) | [S] |
| Metacognitive training for psychosis | 43 studies, N=1816: positive symptoms g=0.50, delusions 0.69, hallucinations 0.26, cognitive biases 0.16, negative 0.23, functioning 0.41. Benefit depends on baseline insight (614 participants, 13 studies) | Penney 2022, Goncalves 2026 (b07, b09) | [E] human only |
| LLM CBT tools | 2,067 participants; higher-empathy reframes preferred 39.7% vs 25.5%. CBT-Bench Level III scores -0.01 to -0.32 on a -2 to 2 scale. Chatbot treated "maybe" as agreement | Sharma 2023, CBT-Bench, CRBot (c22-c24) | [S] |

## 4. Mechanisms and models

Each model below is written so it can be coded. Only 4.1 to 4.7 have LLM evidence.

**4.1 Perspective filter (SimToM) [E for weak models].** Two calls. Call 1: given the story and character X, write only the events X witnessed or was told. Call 2: answer the question using only that filtered text. Code step: the filtered text replaces the story in call 2 (the original is not shown). The single-prompt version (both steps in one prompt) lost to plain CoT on BigToM (58.25, 17.63 below 0-shot CoT), so keep the calls separate (c16). An oracle filter gives 96, so filter quality is the limit.

**4.2 Thought-tracing (Kim 2025) [S].** While reading a story or a dialogue turn by turn, the model keeps a running hypothesis about each party's goals and beliefs, updates after each new event, and weights hypotheses by plausibility. The final answer uses the latest hypothesis. Result: better than CoT and than most reasoning models at fewer tokens (d01, d03). One counter-example: o1-medium beats it on MMToM-QA (76.0 vs 69.0).

**4.3 Knowing-doing split (SimpleToM) [S].** Ask three questions for each social case: (1) what does X know, (2) what will X do, (3) was X's action reasonable. Compare. If (1) is right and (2) or (3) disagrees with it, the model has the state but does not use it. Fix tested: a short reminder in the system prompt that the other party's knowledge decides their action, plus a custom CoT (a12).

**4.4 Paired controls [E].** For each false-belief item, build a true-belief twin and an altered twin (transparent container, informed protagonist). Score an item as passed only if all variants pass. This is Kosinski's all-or-nothing rule plus Ullman's variants. It catches the over-correction seen in reasoning models (true-belief 37 to 59.5 while false-belief 77 to 98.5, d02).

**4.5 External-signal revision [E].** Revise only when code supplies an external fault location or a failed check. Huang: without an external signal accuracy falls (c21). Tyen: finding the faulty step is the bottleneck (about 53% for GPT-4); given the location, backtracking helps wrong traces by +23 to +44 points but harms correct traces by 7 to 11 points (d04). Rule: use backtracking only on traces already flagged wrong by an outside check.

**4.6 Confidence-weighted merge of two judges (Bahrami) [E for humans, not tested on LLMs].** Each judge gives a choice and a confidence. Pick the answer from the judge whose confidence is higher. Collective sensitivity beats the better member only if the sensitivity ratio is near 1 (regression slope 0.6, intercept 0.74, R2=0.51; low-ratio pairs fell below break-even) (a18). Implementation for runs: code computes a calibrated confidence per run (for example agreement rate or token probability, see Kadavath b15), then picks the higher one. Do not use a free-form non-verbal confidence tool: it crowded out benefit in humans (b10).

**4.7 Debate as martingale (Zhu 2026) [E with F08/F10].** If agents are copies of one model and update toward each other, the expected group answer does not change over rounds. Gain needs diversity (different models or prompts) and confidence-aware updating. This supports SCHEMA G9. The new piece is the boundary: heterogeneous plus confidence gave GSM8K 0.932 vs majority 0.908 (b17), a hint to test a diverse, confidence-weighted merge in code (not a debate).

**4.8 MCT in outline (human, not coded) [S].** S-REF (not opened): a person's self-regulatory loop runs on metacognitive beliefs (positive: worry helps; negative: worry is uncontrollable). MCT tries to (a) show these beliefs are wrong, (b) teach detached mindfulness, meaning noticing a thought without engaging with it, (c) postpone worry and rumination, (d) retrain attention. Outcome claims are strong against waitlist; the mechanism claim is weaker (belief change did not mediate in b06). An engineer could map "noticing a loop without engaging" onto a loop detector, but our schema already has code-run impasse detection (S6), and no LLM test exists (d15, K23).

**4.9 Demetriou developmental model [S].** g loads on attention and memory, reasoning and cognizance; with age the weight moves from executive to inferential to self-awareness processes (a24). Implementable only as an ordering hypothesis (test U9 in UNKNOWNS.md).

## 5. What holds up

**Holds (multiple sources).**
- Standard ToM scores overstate competence in LLMs. Ullman, Shapira and Kosinski's own controls agree (K02, [E]). Humans also fail some perturbed items (757 humans failed half, c08), so altered items must be validated with human data before being treated as clean.
- Nested belief and interactive tracking are far weaker than first-order (FANToM, Hi-ToM; K07 [E]).
- Generic CoT is unreliable on social tasks (K06 [E]): +3.60 and -0.09 on Hi-ToM; the FANToM gap to humans stays above 60 points.
- Explicit perspective tracking helps weak models a lot (+47 ToMI false belief GPT-3.5) and strong models a little (c15, K05 [E]).
- Intrinsic self-correction does not help (K09 [E]: Huang, Tyen, Kamoi).
- Homogeneous debate has no expected gain (K15 [E]).
- Group benefit depends on similar partners and verbal confidence (K14 [E], human only).

**Failures and contested points.**
- Kosinski's 75% is read two ways (K03 [C]). Older models partly used word-order cues; GPT-4 handled most controls (a03, a04). GPT-4 still failed at least one prompt in 25% of tasks (a01).
- Shapira reports 0% on some adversarial categories for GPT-4, while Strachan shows humans also fail perturbations. Both "models are brittle" and "the perturbations are not clean" hold.
- Social reasoning versus caution: GPT-4's faux pas failure is mostly refusal to commit (2 of 349 said the speaker knew; likelihood wording gives 100%, d07). LLaMA2's faux pas edge is a bias, not skill (b13).
- Model generation matters: 2022 GPT-3 numbers (a06) and 2023 GPT-3.5 variants (Ullman) are old models. Reasoning-model checks exist only in Kim 2025 and SimpleToM (o1-preview 84.1%).
- Metacognitive prompting: modest gains over CoT on NLU, but 31.7% of its errors are overcorrection and 68.3% overthinking (c20). It conflicts with Huang only at first glance: different tasks (NLU classification vs reasoning), different baselines.
- MCT: the effect shrinks as trials accumulate (0.97 to 0.69 post; 0.37 at follow-up), allegiance may inflate (1.98 vs 1.49), only 5 of 15 trials reported allocation concealment, and the independent OCD trial did not support the mechanism (b06). Exner non-inferiority vs ERP was not confirmed at 6 months (second-hand, d11). The independent transdiagnostic trial is only a protocol (a25, d12).
- Detached mindfulness alone: g -1.80 but k=3 (d13).
- Metacognitive training for psychosis is small (g=0.16 to 0.50) and depends on baseline insight (b07, b09).

**Interventions that worked (on LLMs).** Perspective filter on weak models; thought-tracing; a system-prompt reminder for behaviour prediction; custom CoT for judgment (49.5 to 87.4 on one item); P(True) filtering; diversity plus confidence in group runs; oracle-located backtracking on wrong traces.

**Interventions that did not.** Generic CoT on deception and nested belief; more shots (about +1); single-prompt SimToM; homogeneous debate; intrinsic self-correction; reasoning effort alone on true-belief twins (o1 and R1 stay under 60 on true-belief); non-verbal confidence tools for human dyads.

## 6. Language models

**Behaviour on first-order false belief.** Near ceiling for frontier models: GPT-4 97% on ToM-k (c05), 96-99 on BigToM for all Kim 2025 models (d02), 75% on Kosinski's strict tasks (a01). This tells us little because the items are standard.

**Where they fail.**
1. Altered items: GPT-4 drops to 68.8, 0 and 0 on three adversarial categories (c05).
2. True-belief twins in reasoning models: o1-low true-belief 37.0 vs false-belief 98.5 (d02). The model over-applies "someone is mistaken".
3. Interactive tracking: FANToM ALL for GPT-4 + CoT 14.8-26.6 vs humans 87.5 (c09).
4. Nested belief: Hi-ToM joint accuracy at order 3+ about 0.05-0.35 (c12). No reasoning-model result found (K23).
5. Applying knowledge: GPT-3.5 behaviour prediction 7.6%, judgment 10-24.9% for strong non-reasoning models, with mental-state questions above 95% (a11).
6. Over-caution: faux pas answered with "not enough information" (d07).

**What changed it, by how much.**
- Perspective filter: +47 (ToMI false belief, GPT-3.5 over 0-shot CoT), +29.5 over 0-shot and +14.2 over CoT (BigToM). GPT-4 less (+13.4 ToMI overall, slight loss on BigToM).
- Reminder in system prompt: behaviour prediction above 80% for all (from 7.6% for GPT-3.5 base). Judgment only to 25.8% and 42.2% for Llama-405B and GPT-4o without custom CoT (a12).
- Thought-tracing on GPT-4o: ParaphrasedToMi 59.5 to 76.0; FANToM All 11.1 to 41.5 (54.7 with CoT).
- Reasoning models: help on SimpleToM (o1-preview 84.1% behaviour) and on MMToM-QA (o1-medium 76.0), but not on true-belief twins.
- Fine-tuning: FANToM Flan-T5-XL 53.7 vs humans 87.5 (c11).
- Self-correction prompts: lower accuracy (GPT-4 GSM8K 95.5 to 89.0). RL training for self-correction: +15.6% MATH (abstract only, d06).

**Social metacognition in LLM groups.** Homogeneous debate: no gain, sometimes below majority vote (0.847 vs 0.908). Diversity plus confidence: GSM8K 0.932, MMLU-FL 0.619 vs 0.548. Conformity dynamics (b19) and a human-grounded study of multi-agent traces (b18) are qualitative only. A hidden-profile paper (b24) was not opened.

**Clinical.** No peer-reviewed test applies Wells' MCT to an LLM's own thinking (c27, K18, K23). Therapy-chatbot work is about helping humans: 2,067 participants rated reframes (c22), CBT-Bench shows low Level II/III scores (c23), and CRBot dialogs show shallow reframing (c24).

## 7. What our agent should take

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Score any social or other-party probe as passed only if the base item, a true-belief twin and an altered twin all pass. Use the same rule on our own benches that involve another party's knowledge. | G4 (eval rule) | [E] | a01, a03, a05, b14, c03, c05, d02; K01, K02 |
| A2 | Never treat generic CoT as the social-reasoning step. Where another party's knowledge matters, run a separate explicit step (A3). | G11 note, S1 | [E] | a08, c09, c10, c12, c14; K06 |
| A3 | Add a perspective filter to S1 for tasks about another party: call 1 writes only what that party saw or was told; call 2 answers from the filtered text only. Two calls, not one prompt. Large gain for small models, small for strong ones, so gate it on the equal-token test B1 before it becomes a default. | S1 (frame step, not a new operator) | [E] for weak models; strong models [S] | c15-c18, a12, d01, d03; K05 |
| A4 | No revision on the model's own opinion. Reaffirms G2: revise only from a located failing output or an external check. Backtrack only traces already flagged wrong. | G2 (already present), S5 | [E] | c21, d04, d05; K09 |
| A5 | No debate between identical copies; confirms G9. | G9 (already present) | [E] | b17; K15 |

A4 and A5 are confirmations, not new rules. A1 to A3 are the only new items.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Knowing-doing check: ask "what does X know", "what will X do", "was X reasonable" and flag disagreement; add the reminder text to the system prompt. | S1, G4 | [S] | a11, a12; K04 |
| T2 | Thought-tracing as a running hypothesis per party for dialogue or multi-turn user modelling. | S1/S2 | [S] | d01-d03; K20 |
| T3 | Phrase social probes as "which is more likely" instead of yes/no knowledge questions, to remove over-caution. | S1 | [S] | d07, a15; K21 |
| T4 | Confidence-weighted merge of two unequal runs (code picks higher calibrated confidence), compared to the strong run alone. | S7, G4, G5 | [S] humans only | a17, a18, b10, b11; K14, K23 |
| T5 | Diverse (different prompts or models), confidence-weighted code merge versus majority vote; never debate. | S7, G9 boundary | [S] | b17; K15 |
| T6 | P(True)-style own-probability gate as a cheap abstain or retry signal. | G2, S4 | [S] | b15; K17 |
| T7 | Bounded self-check step (metacognitive prompting) versus CoT, with overcorrection rate measured. | G1, S8 | [S], likely negative | b16, c20; K10 |
| T8 | Detach-from-draft prompt (read own draft as another person's, judge only against the check). Idea only; no LLM test exists. Borrowed from detached mindfulness. | S5/S6 | untested | d13, d15; K23 |
| T9 | Nested-belief depth probe, order 1-4; log where accuracy collapses with and without T2. | S1 | [S] | c12, a08; K07 |

Do not add: MCT mechanisms, Demetriou ordering, therapy-chatbot techniques (section 9).

## 8. Concrete tests on our bench

All arms get the same total token budget (setup calls counted, G7). Report pass rate with a 95% interval; use at least 100 paired items per cell unless stated.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | False-belief, true-belief twin and altered twin (transparent bag, informed protagonist) built from ToMi and BigToM templates | plain; plain + CoT; scaffold with A3 filter | all-variants-pass rate | Plain high on base, much lower on all-variants; filter closes part of the gap (GPT-3.5 effect +30 to +47 points; for a strong bench model expect +0 to +15) |
| B2 | SimpleToM-style stories with three questions (state, behaviour, judgment) | plain; reminder in system prompt; reminder + custom CoT | behaviour accuracy; judgment accuracy; knowing-doing gap | behaviour above 80% with reminder; judgment 25-42% without custom CoT, higher with it (49.5 to 87.4 on one item) |
| B3 | Thought-tracing on FANToM or ParaphrasedToMi items | plain; CoT; thought-tracing; reasoning-effort increase | accuracy at fixed tokens | thought-tracing beats CoT by about 10 points at equal tokens (59.5 to 76.0 on GPT-4o) |
| B4 | Faux pas items, two phrasings (yes/no knowledge vs most-likely) | plain, both phrasings | accuracy; "not enough information" rate | likelihood phrasing near 100%, yes/no depressed by over-caution |
| B5 | Hi-ToM-style nested belief, orders 1-4 | plain; CoT; thought-tracing | accuracy by order | collapse at order 3+ (joint about 0.05-0.35 in 2023 models); scaffold lifts it less than at order 1 |
| B6 | Reasoning items with a check (GSM8K-like) | one run; one run + intrinsic revise; one run + revise with failed-check output | accuracy; harm rate on originally correct items | intrinsic revise lowers (GPT-4 95.5 to 89.0); revise on check output helps |
| B7 | Two runs of unequal quality (strong vs weak setting), exact-answer items, calibrated confidence | strong alone; majority of both; confidence-weighted pick; equal total tokens | accuracy | helps only if the confidence ratio is near 1; below the strong run if the weak run is much worse (Bahrami rule) |
| B8 | Same items as B7 with 3 runs | majority; diverse + confidence merge; 2-round debate | accuracy at equal tokens | debate between copies below majority; diverse + confidence about +2 to +9 points over majority (GSM8K 0.932 vs 0.908; MMLU-FL 0.619 vs 0.548) |
| B9 | Long reasoning chains with detected loops (repeat-text detector) | plain; hard stop; detach-from-draft prompt | accuracy; tokens | no published number; pass if accuracy up 3 points at equal tokens |
| B10 | Items with a held-out check where the model self-rates confidence | P(True) gate at 0.5; no gate | accuracy of kept answers; coverage | accuracy rises on kept answers; AUROC about 0.6-0.85 |

## 9. What does not transfer, and why

- **Metacognitive therapy.** It changes a patient's beliefs about their own worry and rumination. The agent has no emotional distress loop and no beliefs it holds across sessions. Strong clinical effects are against waitlist (g=2.06) and shrink against active therapy (0.37 at follow-up). Allegiance and low-quality trials may inflate them. The OCD mechanism test failed (beta=-0.01). No LLM test exists. Verdict: do not import (K11, K12, K22).
- **Detached mindfulness and worry postponement.** Human attentional skills. The nearest agent version is a code-run loop detector (already S6). The "detach" prompt is a guess (T8).
- **Metacognitive training for psychosis.** Targets delusion-related cognitive biases in people; effects small (0.16-0.50) (K13).
- **Wells' scale (MCQ) and S-REF.** Self-report scale and a theory of human emotion regulation; not opened (a26, a27). No agent equivalent.
- **Demetriou's developmental ordering.** Age-based change in humans. LLM capabilities do not develop by age, and nothing links the order to scale or reasoning training (K19, K23).
- **Human dyad confidence sharing.** Needs similar sensitivity, spoken confidence and feedback. Copies of one model are not independent (G4), so "similar partners" holds in the wrong way: similar but correlated.
- **Therapy-chatbot results.** They measure what helps a person feel better (empathy ratings, BLEU), not whether the agent thinks better (K18).
- **Kosinski's "emergent ToM" claim.** The score is real but its meaning is contested. We use the items as probes, not as a claim about the agent's mind.

## 10. Open questions

1. Does the perspective filter still help a strong reasoning model at equal tokens? SimpleToM shows reasoning closes much of the gap (o1-preview 84.1%), and Kim 2025 shows o1-medium wins on MMToM-QA, so the gain may shrink.
2. Does the knowing-doing gap exist in our agent, and does the reminder fix it?
3. Does confidence-weighted merging of unequal runs work for LLMs? No replication found (d15). Bahrami 2010 exact numbers could not be re-opened (paywall); Mahmoodi 2015 (equality bias) has no LLM replication found.
4. Where does intrinsic revision help or hurt a modern reasoning model with an external-signal control? All strong evidence uses GPT-3.5 or GPT-4 (c21, d04). Kumar 2024 reports gains from RL training, not prompting (d06, abstract only).
5. Do reasoning models do better at Hi-ToM order 3+? Not found.
6. How much of MCT's advantage over CBT survives independent, low-bias trials? An independent tMCT-vs-CBT trial is only a protocol (a25, d12).
7. Does the Demetriou order predict the order in which LLM abilities appear? Nothing found.
8. Does any peer-reviewed work use MCT mechanisms as agent control against rumination loops? One targeted search found none (c27). Search was limited.
9. How clean are altered ToM items? Humans fail half of the perturbed items (c08), so how to build twins that humans pass is open.
10. The 2026 multi-agent studies (b18, b19) are qualitative in what we read, and the hidden-profile paper (b24) was not opened.

## 11. Sources

[V] = opened this run (full text, PDF or page). [M] = snippet or abstract only, or second-hand.

- [V] Kosinski (2024) Evaluating large language models in theory of mind tasks (PNAS). https://arxiv.org/abs/2302.02083 (a01-a04, c01, c02)
- [V] Ullman (2023) Large language models fail on trivial alterations to theory-of-mind tasks. https://arxiv.org/abs/2302.08399 (a05, b14, c03, c04)
- [V] Sap, Le Bras, Fried, Choi (2022) Neural theory-of-mind? https://arxiv.org/abs/2210.13312 (a06, a07; a07 has no exact numbers)
- [V] Shapira et al. (2023) Clever Hans or Neural Theory of Mind? https://arxiv.org/abs/2305.14763 (c05)
- [V] Kim et al. (2023) FANToM. https://arxiv.org/abs/2310.15421 (a08, a09, c09-c11)
- [V] Wu et al. (2023) Hi-ToM (a10 lists "He et al."; same paper as c12, first author Wu). https://arxiv.org/abs/2310.16755
- [V] Gu et al. (2026) SimpleToM, ICLR 2026. https://arxiv.org/abs/2410.13648 (a11, a12)
- [V] Gandhi et al. (2023) Understanding social reasoning in language models with language models (BigToM). https://arxiv.org/abs/2306.15448 (c13, c14)
- [V] Wilf et al. (2023) Think Twice: perspective-taking (SimToM). https://arxiv.org/abs/2311.10227 (c15-c18)
- [V] Kim et al. (2025, COLM) Hypothesis-driven theory-of-mind reasoning (thought-tracing). https://arxiv.org/abs/2502.11881 (d01-d03)
- [V] Strachan et al. (2024) Testing theory of mind in large language models and humans, Nature Human Behaviour. https://www.nature.com/articles/s41562-024-01882-z and https://pmc.ncbi.nlm.nih.gov/articles/PMC11272575/ (a13-a15, b13, c06-c08, d07)
- [V] Frith (2012) The role of metacognition in human social interactions. https://pmc.ncbi.nlm.nih.gov/articles/PMC3385688/ (a16, a28)
- [V, numbers unverified] Bahrami et al. (2010) Optimally interacting minds, Science. https://www.science.org/doi/10.1126/science.1185718 (a17, a18; paywalled, numbers may come from a secondary text; b22 not extracted)
- [V] Bahrami et al. (2012) What failure in collective decision-making tells us about metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC3318766/ (b10)
- [V] Pescetelli, Rees, Bahrami (2016) Perceptual and social components of metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC4961070/ (b11)
- [V, abstract level] Vuillaume et al. (2020) Comparing self- and hetero-metacognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC7188279/ (b12)
- [M] Mahmoodi et al. (2015) Equality bias impairs collective decision-making. https://doi.org/10.1073/pnas.1421692112 (b23)
- [V] Zhu et al. (2026) Demystifying multi-agent debate. https://arxiv.org/abs/2601.19921 (b17, b25)
- [M] From process loss to assembly bonus (2026). https://arxiv.org/abs/2609.13261 (b18)
- [M] Conformity dynamics in LLM multi-agent systems (2026). https://arxiv.org/abs/2601.05606 (b19)
- [M] Hidden profile paradigm for LLM collective reasoning. https://arxiv.org/abs/2505.11556 (b24)
- [V] Huang et al. (2023) Large language models cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (c21)
- [V] Tyen et al. (2024) LLMs cannot find reasoning errors, but can correct them. https://arxiv.org/abs/2311.08516 (d04)
- [V] Kamoi et al. (2024) When can LLMs actually correct their own mistakes? https://arxiv.org/abs/2406.01297 (d05)
- [M] Kumar et al. (2024) Training language models to self-correct via RL. https://arxiv.org/abs/2409.12917 (d06)
- [V] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (b15)
- [V] Wang and Zhao (2023/2024) Metacognitive prompting. https://arxiv.org/abs/2308.05342 (a13, b16, c19, c20)
- [V] Normann and Morina (2018) The efficacy of metacognitive therapy. https://pmc.ncbi.nlm.nih.gov/articles/PMC6246690/ (a19, a20, b01-b03, c25; b20, b21 cited within, [M])
- [V] Meta-analysis (2023) MCT vs CBT for GAD. https://pmc.ncbi.nlm.nih.gov/articles/PMC10277900/ (a21)
- [V] Meta-analysis (2024) MCT in PTSD. https://pmc.ncbi.nlm.nih.gov/articles/PMC13294017/ (a22)
- [V] Nordahl and Wells (2018) MCT for social anxiety, A-B replication. https://pmc.ncbi.nlm.nih.gov/articles/PMC5906593/ (a23)
- [V] Hagen et al. (2017) MCT for depression, waitlist RCT. https://pmc.ncbi.nlm.nih.gov/articles/PMC5258745/ (b04)
- [V] Gjengedal et al. (2025) MCT and work focus. https://pmc.ncbi.nlm.nih.gov/articles/PMC12675033/ (b05, d09)
- [V] Anwar et al. (2026) MCT for OCD. https://pmc.ncbi.nlm.nih.gov/articles/PMC13670996/ (b06, d10)
- [M] Exner et al. MCT vs ERP, as cited in Anwar 2026 (d11, second-hand)
- [V] Torabi et al. (2026) MCT and depression meta-analysis. https://europepmc.org/article/PMC/PMC13383551 (d08)
- [V] Trial protocol (2026) transdiagnostic MCT vs CBT. https://pmc.ncbi.nlm.nih.gov/articles/PMC13721498/ (a25, d12)
- [V] Detached mindfulness meta-analysis (2026). https://europepmc.org/article/PMC/PMC13125881 (d13)
- [V] Penney et al. (2022) Metacognitive training for psychosis. https://pmc.ncbi.nlm.nih.gov/articles/PMC8943641/ (b07)
- [M] Metacognitive training for schizophrenia review (2015), 10 RCTs. https://pmc.ncbi.nlm.nih.gov/articles/PMC4526827/ (b08; partly superseded by b07)
- [V] Goncalves et al. (2026) Baseline cognitive insight moderates MCT efficacy. https://pmc.ncbi.nlm.nih.gov/articles/PMC13748317/ (b09)
- [V] Demetriou et al. (2020) Mapping mind-brain development. https://pmc.ncbi.nlm.nih.gov/articles/PMC7713015/ (a24)
- [M] Wells and Matthews (1994, 1996) S-REF model. https://doi.org/10.1016/0005-7967(95)00050-X (a26, not opened)
- [M] Wells and Cartwright-Hatton (2004) Short form of the Metacognitions Questionnaire (a27, not opened)
- [V] Sharma et al. (2023) Cognitive reframing of negative thoughts. https://arxiv.org/abs/2305.02466 (c22)
- [V] CBT-Bench (2024). https://arxiv.org/html/2410.13218v2 (c23)
- [V] CRBot (2025). https://arxiv.org/html/2501.15599v1 (c24)
- [V, no figures] Liu et al. (2026) Metacognition in LLMs. https://arxiv.org/abs/2607.11881 (c26, c27)
- [V, abstract level] Interpersonal alignment of neural evidence accumulation (2023). https://europepmc.org/article/PMC/PMC10746141 (d14)
- Search records, not sources: d15, d16, c28 (our own analysis).

*Links to parallel subfields (not covered here): Verbal confidence; Debiasing; Coordination and common ground; Collective intelligence factor c; Team science; Simulation vs theory accounts; Beliefs and affect; Argumentation and defeasible rules; Social cognition in animals.*
