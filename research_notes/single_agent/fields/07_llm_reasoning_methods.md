# LLM reasoning methods: what they offer one thinking agent

Marks: [V] = checked this session against a source page (mostly abstracts and search summaries, not full papers, so table numbers still need a re-read); [M] = from memory, re-check numbers. [ours] = measurement from 00_PLAN.md.

## 1. What the field studies

Since 2022, many papers have asked how to make one language model reason better at inference time, without retraining. The families are: written step-by-step reasoning (chain of thought, CoT), sampling many answers and voting (self-consistency), searching over partial thoughts (tree and graph search), revising an answer (self-refine, Reflexion), scoring steps with a verifier (process reward models, PRMs), choosing or composing a strategy per task (Self-Discover, plan-then-solve, step-back, analogical prompting), and wrapping the model in memory and control loops (CoALA, agent memory). The evidence is large but uneven. Most numbers come from big models on math, code and logic benchmarks. Few papers match tokens between arms. That is the filter we apply here, because our own data shows a method can win on accuracy and still lose at equal cost.

## 2. Core findings

**F1. CoT helps mainly on math and symbolic tasks, little elsewhere.** A meta-analysis of 100+ papers plus 20 datasets on 14 models found strong CoT gains mostly on math and logic. On MMLU, direct answers were almost identical to CoT unless the question or answer contained an equals sign (Sprague et al., ICLR 2025) [V]. Strength: strong (meta-analysis plus own tests). Implication: for multiple-choice and commonsense items, CoT costs tokens for nothing.

**F2. CoT can reduce accuracy when deliberation hurts humans too.** On implicit statistical learning, face-like visual recognition and classification with exceptions, o1-preview lost up to 36.3 points against GPT-4o zero-shot; on three other such tasks CoT did not hurt (Liu et al., ICML 2025) [V]. Strength: moderate, six tasks. This matches our BrainTeaser result [ours].

**F3. Small models gain less from CoT and from long chains.** Wei et al. 2022 reported that CoT gains appear only at roughly 100B parameters and below that chains are fluent but wrong [M]. Newer small models do better, but a 2025 study found models at or below 3B do not benefit consistently from long CoT or from distillation of strong-reasoner chains, and do better with short, simple chains (Li et al., "Small Model Learnability Gap") [V]. Strength: moderate. Note this is about fine-tuning on chains, so it is indirect for prompting Haiku class models, which are far above 3B.

**F4. More samples help a lot when a check exists, and plateau when it does not.** Repeated sampling raised SWE-bench Lite coverage (any sample solves it) from 15.9% to 56% with 250 samples on a DeepSeek coder model; five cheap samples beat one sample of GPT-4o or Claude 3.5 Sonnet at over 3x lower cost. Where no automatic verifier exists, majority vote and reward models plateau after a few hundred samples (Brown et al. 2024, Large Language Monkeys) [V]. Strength: strong. Coverage is not accuracy of the pick. Selection is the bottleneck.

**F5. Self-consistency (vote over CoT samples) is a reliable, if costly, gain on closed-answer tasks.** Wang et al. 2022 reported gains of several to 17 points on GSM8K-style math [M]. Adaptive stopping cuts the cost: Adaptive-Consistency used up to 7.9x fewer samples for under 0.1% loss (cited in 00_PLAN as [V]). Strength: strong for math, weak for open answers.

**F6. Test-time compute should be allocated per problem.** Snell et al. 2024: a compute-optimal policy (pick search against a PRM or sequential revision by estimated difficulty) improved efficiency by more than 4x over best-of-N; on problems where a smaller model has non-trivial success, test-time compute could beat a 14x larger model in a FLOPs-matched test; on the hardest prompts pretraining still wins [V, abstract-level; the last point is a third-party reading]. A follow-up reported 1B and 3B models beating a 405B model on MATH-500 with compute-optimal search, but the best strategy depends on policy model, PRM and difficulty [V]. Strength: strong on MATH, one family of tasks, with a trained PRM.

**F7. Longer thinking can make answers worse.** Anthropic-fellows work built tasks where longer reasoning lowers accuracy: counting with distractors, regression with spurious features, constraint-tracking deduction. Claude models became more distracted by irrelevant information as reasoning grew (Gema et al. 2025) [V]. Strength: moderate, synthetic tasks. It supports a cap on thinking length.

**F8. Tree and graph search over thoughts: huge gains on search puzzles, doubtful elsewhere.** Tree of Thoughts: Game of 24, GPT-4 CoT 4%, ToT (breadth 5) 74% (Yao et al. 2023) [V]. Cost is many times the tokens. Game of 24 is a task with cheap partial-state evaluation. Later work (e.g. Graph of Thoughts, LATS) reports more gains, numbers not checked [M]. Strength: strong where states can be scored, unknown otherwise. Needs a model good enough to judge partial states.

**F9. Self-correction with no outside signal does not work; with real feedback it does.** Huang et al. 2023: intrinsic self-correction in reasoning generally fails and sometimes lowers accuracy; earlier gains used oracle labels or weak first prompts; debate did not beat self-consistency at equal responses [V]. Kamoi et al. 2024 survey: no prior work shows success with feedback from prompted LLMs alone (except special tasks); it works with reliable external feedback (code runs, tools); fine-tuning can enable it [V]. Reflexion reports large gains with executable or environment feedback (about 91% pass@1 HumanEval, AlfWorld 130 of 134 tasks), but I did not confirm the base model or table [M, partly seen in secondary summary]. Greenblatt 2024 (ARC, 37% to 50% with revision on real outputs) is cited in 00_PLAN as [V]. Strength: strong and consistent. This is our most important rule.

**F10. Process verification helps, but it needs a trained verifier.** Lightman et al. 2023: process supervision beat outcome supervision for reranking on MATH, about 78% on a subset [V, abstract; exact 78.2 not seen]. Verifiers are costly to train and weaker out of domain [M]. For us the transferable form is not a PRM but a program-run check.

**F11. Strategy selection and composition: modest gains, some of it from the prompt format.** Self-Discover: model picks atomic modules (critical thinking, step by step), composes a structure once per task, then follows it. Up to 32% over CoT on BigBench-Hard, agent reasoning and MATH with GPT-4 and PaLM 2; beat CoT-self-consistency by over 20% at 10 to 40x less inference [V, abstract]. In zero-shot PaLM-2L it beat direct on 23 of 25 BBH tasks and CoT on 21 of 25 [V]. Strength: moderate, large models, one lab. Our four-strategy schema lost on BrainTeaser [ours], so the gain depends on task type.

**F12. Step-back and analogical prompting: small to moderate gains on large models.** Step-back (derive the principle first): PaLM-2L MMLU physics 66.4% to about 73%, chemistry 70.9% to about 82%, while zero-shot CoT barely moved [V]. Analogical prompting (the model writes its own related examples before solving): about +4% average over 0-shot and few-shot CoT across GPT-3.5, GPT-4, PaLM 2 on GSM8K, MATH, Codeforces, BBH [V]. Strength: moderate. Plan-and-Solve (Wang 2023): small gain over zero-shot CoT on math, a few points [M, not confirmed this session].

**F13. Agent architecture and memory: mostly frameworks, thin controlled evidence.** CoALA (Sumers, Yao, Narasimhan, Griffiths, TMLR) is a conceptual map: working and long-term memory, internal actions (reason, retrieve, learn), external actions, a decision loop [V]. It is a design vocabulary, not an effect size. LongMemEval (ICLR 2025): commercial assistants and long-context models drop about 30% when they must remember across long sessions; abilities tested are extraction, multi-session reasoning, temporal reasoning, updates, abstention [V]. Generative Agents reflection, MemGPT, Voyager skill library show benefits in their own settings [M]. Strength: weak to moderate; no equal-token comparison against plain long context in what I checked.

## 3. Mechanisms an agent can run

**M1. Probe, then spend by disagreement (adaptive allocation).**
- Trigger: any new problem.
- Action: draw 3 to 5 plain, short attempts. Compute agreement on the final answer (exact match, or program behavior on held-out inputs). If a check exists, run it. Stop at once if two attempts agree and pass. Spend more only when attempts split.
- Check: accuracy per token against fixed best-of-N, at the same total token budget, on ARC, coding, BrainTeaser. Log tokens saved on easy items.
- Evidence: F5, F6, Adaptive-Consistency [V]; Snell 4x [V].
- Risk: on small models, agreement can be confidently wrong. Early stop on easy items already ties plain in ARC-1 [ours], so gain there is cost, not accuracy.

**M2. Revise only from real check output, never from opinion.**
- Trigger: an attempt exists, a runnable check exists (tests, examples, program execution), and it failed.
- Action: feed the actual failing output and diff back; ask for a minimal fix; 1 to 2 rounds; keep best-so-far, never replace it with an unchecked revision.
- Check: pass rate after round 1 and 2 versus spending the same tokens on fresh samples.
- Evidence: F9 (Kamoi, Huang [V]; Greenblatt [V]; Reflexion [M]).
- Risk: with no check, this step must be OFF. A critique-only revision risks flipping right answers (Huang [V]).

**M3. Format gate: CoT only where it pays.**
- Trigger: before the first attempt, classify cheaply from the task text: does it need multi-step arithmetic, symbolic manipulation or search (CoT on) or recall, commonsense, multiple choice, perception-like pattern judging (short direct answer, or one short rationale)?
- Action: pick direct or CoT; cap reasoning length.
- Check: per task class, direct versus CoT at equal tokens; keep the gate only if it matches or beats the better fixed arm.
- Evidence: F1, F2, F7 [V].
- Risk: the classifier can be wrong; mitigate by letting the probe (M1) include one direct and one CoT attempt and comparing.

**M4. Verify by executing and select by behavior, not by judge.**
- Trigger: more than one candidate and a way to run them.
- Action: run all candidates on given and fresh inputs; group by behavior; tie-break by simplicity (our symmetry-first selector); for an unresolvable tie, derive the expected output from examples before seeing candidates.
- Check: selector pick rate versus oracle best candidate and versus majority vote, offline replay (34 of 36 versus 33 of 36 already [ours]).
- Evidence: F4 (selection is the bottleneck) [V]; F10 (verification helps; here by execution rather than a trained PRM).
- Risk: a program that fits all examples can still be wrong (ARC fooled twice [ours]).

**M5. Strategy choice once, per task class, with a cheap pick.**
- Trigger: task class is new or the probe split.
- Action: one call: from a short fixed menu (direct, decompose, step-back principle, work backwards, analogous solved problem), pick one or two and state why; then follow them in a single attempt. Do not run all in parallel and do not judge among them with a model.
- Check: versus plain at equal tokens, per class; record which strategy was picked and whether it matched the best fixed strategy.
- Evidence: F11, F12 [V], mostly large models.
- Risk: our four-strategy schema fell from 92% to 75% [ours]. Gate by the probe: only when attempts disagree.

**M6. Capped extra thinking, with a "stop when a check passes" rule.**
- Trigger: attempt still failing after M2.
- Action: allow one longer-reasoning attempt up to a token cap; stop at the first checked pass; no forced "wait" loops when a check already passed.
- Check: accuracy versus cap curve; if it declines past a cap on any suite, set the cap there.
- Evidence: F7 [V]; s1 budget forcing helps only on a fine-tuned model [V, abstract].
- Risk: budget forcing was trained for, not prompted; do not expect the same gain on a prompted Haiku.

**M7. Lesson memory, retrieved by class.**
- Trigger: after each solved or failed problem; and at the start of a problem of a known class.
- Action: write a one-line lesson (trick, trap) with its class and a verified-twice flag; retrieve at most 3 same-class lessons.
- Check: held-out problem set, with and without memory, equal tokens (lesson text counts).
- Evidence: F13 weak; Reflexion memory [M]; LongMemEval shows retrieval failure is common [V].
- Risk: noisy lessons add tokens and bias. Build last.

## 4. Evidence on LLMs and AI agents

All of Sections 2 and 3 are LLM studies. Points worth separating:

- Meta-level: Sprague et al. is the strongest single source on when CoT helps (F1) [V].
- Small models: Snell and the 1B-beats-405B paper show test-time search lets small models close gaps on math with a PRM (F6) [V]. The learnability-gap paper shows small models handle long chains poorly (F3) [V]. Both use open models far smaller than Haiku, so read them as direction only.
- Same-family warning: Gema et al. test Claude models directly and show distraction growing with reasoning length (F7) [V].
- Agents: Reflexion, LATS, Voyager, Generative Agents are agent-loop papers; effect sizes come from their own environments and mostly have external feedback [M].
- Gap: I found no study that tests a router across single-answer and open-ended tasks at equal tokens. That is the study 00_PLAN proposes.

## 5. What does not transfer, and where it could hurt

- Trained PRMs, budget-forcing fine-tunes, "long CoT" distillation: need training; prompting alone will not reproduce them.
- Tree search needs a reliable partial-state scorer; a small model judging its own partial thoughts is the exact intrinsic-feedback case that fails (F9).
- Reported gains from Self-Discover, step-back, analogical prompting were on PaLM-2L, GPT-4 and similar, mostly on benchmarks that are now likely saturated or contaminated. Expect smaller gains on Haiku.
- Forced structure on tasks where the first answer is usually right: Self-Discover-like multi-step setup and forced doubt cost accuracy in our data [ours] and match F1 and F2.
- Heavy setup: a scaffold that eats budget before the first answer scored 0% [ours]. Any mechanism above must be cheap at the start.
- Majority vote on open answers is meaningless; use diverge-then-prune there.
- Human traits (confidence, motivation) have no direct counterpart; agreement and check pass-rate are the proxies.

## 6. Open questions

1. Does a small model route its own problem class accurately enough to beat a fixed arm? Untested.
2. At Haiku scale and equal tokens, how much of Self-Discover, step-back and analogical prompting survives? Unknown; run them as arms M5.
3. Where is the reasoning-length cap per suite (F7)?
4. Does lesson memory help on held-out problems or only add noise?
5. How should near-miss candidates (fit all examples, still wrong) be filtered beyond symmetry checks?
6. Which published numbers hold when re-read: Reflexion base model, Plan-and-Solve gains, Self-Consistency deltas, Lightman 78.2. These are [M] or abstract-only.

## 7. References

1. Sprague et al. To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning. ICLR 2025. https://arxiv.org/abs/2409.12183
2. Liu, Geng, Wu, Sucholutsky, Lombrozo, Griffiths. Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. ICML 2025. https://arxiv.org/abs/2410.21333
3. Li et al. Small Models Struggle to Learn from Strong Reasoners. Findings of ACL 2025. https://arxiv.org/abs/2502.12143
4. Wei et al. Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. 2022. https://arxiv.org/abs/2201.11903 [M]
5. Brown et al. Large Language Monkeys: Scaling Inference Compute with Repeated Sampling. 2024. https://arxiv.org/abs/2407.21787
6. Wang et al. Self-Consistency Improves Chain of Thought Reasoning. 2022. https://arxiv.org/abs/2203.11171 [M]
7. Snell, Lee, Xu, Kumar. Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. ICLR 2025. https://arxiv.org/abs/2408.03314
8. Liu et al. Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling. 2025. https://arxiv.org/abs/2502.06703
9. Gema et al. Inverse Scaling in Test-Time Compute. TMLR 2025. https://arxiv.org/abs/2507.14417
10. Yao et al. Tree of Thoughts: Deliberate Problem Solving with Large Language Models. 2023. https://arxiv.org/abs/2305.10601
11. Huang et al. Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024. https://arxiv.org/abs/2310.01798
12. Kamoi et al. When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL 2024. https://arxiv.org/abs/2406.01297
13. Shinn et al. Reflexion: Language Agents with Verbal Reinforcement Learning. 2023. https://arxiv.org/abs/2303.11366 (numbers not verified from the paper)
14. Lightman et al. Let's Verify Step by Step. 2023. https://arxiv.org/abs/2305.20050
15. Muennighoff et al. s1: Simple test-time scaling. 2025. https://arxiv.org/abs/2501.19393
16. Zhou et al. Self-Discover: Large Language Models Self-Compose Reasoning Structures. 2024. https://arxiv.org/abs/2402.03620
17. Zheng et al. Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models. 2023. https://arxiv.org/abs/2310.06117
18. Yasunaga et al. Large Language Models as Analogical Reasoners. ICLR 2024. https://arxiv.org/abs/2310.01714
19. Wang et al. Plan-and-Solve Prompting. ACL 2023. https://arxiv.org/abs/2305.04091 [M]
20. Sumers, Yao, Narasimhan, Griffiths. Cognitive Architectures for Language Agents (CoALA). TMLR. https://arxiv.org/abs/2309.02427
21. Wu et al. LongMemEval: Benchmarking Chat Assistants on Long-Term Interactive Memory. ICLR 2025. https://arxiv.org/abs/2410.10813
22. Park et al. Generative Agents. 2023. https://arxiv.org/abs/2304.03442 [M]
