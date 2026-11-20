# Assumption testing: deep document

*Subfield E17.09. Key works: McGrath and MacMillan (1995, 2000) discovery-driven planning. Schema target: S7 (discriminating test). Evidence ids a01-a28, b01-b26, c01-c28, d01-d18 are in the evidence files of this folder; claim ids E17.09-K01 to K21 are in claims.jsonl. Status words follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Assumption testing means turning the hidden beliefs behind a plan or an answer into explicit statements, then running the cheapest check that could prove them wrong, before more money, time or tokens are spent.

Three traditions meet here.

- **Business planning.** Discovery-driven planning (McGrath and MacMillan) starts from the outcome the plan needs, lists every assumption that must hold, and spends in stages, testing the riskiest assumption first. Lean startup uses the same idea as build-measure-learn loops with cheap tests (A/B test, fake door, concierge) [a01, a02, a03].
- **Hypothesis-testing psychology.** Wason's 2-4-6 task (1960) shows that people test cases that fit their guess and so fail to find a broader hidden rule. Klayman and Ha (1987) reply that positive testing is a sound heuristic when the guess is broader than the truth [a15, a16, b18; all second-hand].
- **LLM evaluation.** Since 2024 there are benchmarks that put models in a Wason-style loop (WILT, FalsifyBench, Failing to Falsify) and measure how often they test to refute rather than to confirm.

For our agent the link is S7. S7 already says: if two rules still fit, run the one input where they differ. This document asks how far that idea extends: to listing assumptions, ranking them, and choosing tests, and what the evidence says about each step.

Important limit up front. Almost all LLM evidence is on rule-discovery games with numbers or WordNet categories. The business evidence is human. No controlled study was found of an LLM writing an assumption map, a premortem or a discovery-driven plan and being scored on decision quality [K15, a28, c28, d17, d18].

## 2. History and theories in depth

**1960, Wason's 2-4-6 task.** People are told that 2-4-6 fits a hidden rule (any increasing triple). They propose triples and get yes or no. Most propose triples fitting a narrow guess such as "add 2", get yes, and announce a wrong rule. As described in the 2026 LLM paper: 29 participants, 6 correct at the first announcement, 21 eventually found the rule. Mean ratio of incompatible to compatible tests (I:C) was 1.79 for first-time-right and 0.24 for first-time-wrong; among first-time failers, 0.50 for later-right and 0.19 for still-wrong [a15, b15, c02]. The 1960 paper itself was not opened.

**1987, Klayman and Ha.** A positive test strategy (test cases your hypothesis says are true) is not the same as confirmation bias. It works when the target is narrower than the hypothesis. It fails when the target is broader, as in 2-4-6 [a16, b18]. This is the main rival theory, and the 2026 papers state it themselves [b12, c08]. Not opened.

**1989, Mitchell, Russo and Pennington.** Prospective hindsight ("imagine it failed; why?") is said to raise the number of reasons generated, often quoted as about 30%. This is the base of the premortem. The figure is from memory and was never verified; do not cite it [b26, d17].

**1995 and 2000, McGrath and MacMillan.** Discovery-driven planning: begin with the required profit and work back (reverse income statement), list the assumptions behind each line (volume, price, cost), set checkpoints, and release funding only as key assumptions are tested. The description we have is from Mansoori and Lackeus (2020): six guideline areas, ten steps, an assumptions checklist reviewed at each milestone. The 1995 HBR article was not opened and no outcome numbers from it were verified [a01, a02, b24].

**2011 on, lean startup.** Build-measure-learn loops with cheap tests. McGrath (2024) frames both methods as learning races: discovery-driven growth tolerates wider uncertainty and is less prescriptive [a03, a04].

**2014, Kerr, Nanda and Rhodes-Kropf.** Economic theory of entrepreneurship as experimentation: skewed outcomes make many cheap experiments the right investor policy. Not opened [b25].

**2020, Camuffo et al., first RCT.** The first randomized test that teaching a "scientific approach" (theory, falsifiable hypotheses, tests with thresholds) changes founder behaviour. It includes a formal model: a founder has a prior on idea value, gets a signal, and chooses to develop, pivot or exit by a threshold. A scientific approach raises signal precision, cutting both false positives (bad ideas pursued) and false negatives (good ideas dropped) [a05-a10, b01-b05].

**2022, Koning, Hasan and Chatterji.** Observational evidence that startups adopting A/B testing tools gain about 10% in page views, with a large selection artifact in the raw comparison [a12-a14, b07-b09].

**2024 to 2026, the LLM turn.** WILT (2024) shows frontier models are poor at multi-turn rule induction. Failing to Falsify, FalsifyBench and the sycophancy paper (all 2026) measure confirmation bias directly and test prompts and training that reduce it. Popper (2025) builds an agent that falsifies with error control. Otis et al. (2024) is the one field RCT of an LLM business adviser [a17-a27, c01-c28, d01-d18].

**Competing explanations of why people and models confirm.**
1. Confirmation bias in the motivational sense.
2. Positive test strategy: a sound default that fails on broad rules (Klayman and Ha).
3. Matching bias: on the Wason selection task LLM errors fit matching bias better than confirmation bias; accuracy is higher on deontic than descriptive rules by 5.0 to 41.2 points [b20].
4. Evidence sampled from the hypothesis: Batista and Griffiths' Bayesian account says data drawn from the current hypothesis raise confidence and barely move the posterior [a21, c15].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Default LLMs test mostly confirming triples; success rises with the share of disconfirming tests | 11 LLMs; success 6% to 78% within 45 turns; I:C correlates positively with success in thinking and non-thinking models; 80 episodes per model-variant | Jhaveri et al. 2026 [a17, b12, c01] | [S] one paper, directionally agreed by FalsifyBench |
| Think-in-Opposites prompt lifts rule discovery | Average 42% to 56%; improved success in all 11 model-by-mode settings; Dual-Goal in 8 of 11; I:C up in 18 of 22 cases; Dual-Goal hurt Qwen3-14B 23% to 13% and Qwen3-32B 33% to 10% (standard mode) | Jhaveri et al. 2026 [a18, b13, c03] | [S] |
| Gain is significant for thinking models, mixed for non-thinking | Qwen3-32B thinking 0.41 to 0.61, I:C 0.14 to 0.54; Qwen3-8B non-thinking 0.06 to 0.06; Qwen3-14B thinking 0.34 to 0.48; Llama-3.3-70B 0.21 to 0.38; GPT-4o 0.11 to 0.16; QwQ-32B 0.50 to 0.59; Gemini-2.5-Pro 0.73 to 0.78 | Jhaveri et al. 2026 [d04, c04] | [S] |
| Token cost of the opposite-test prompt | Qwen3-32B thinking about 1,030 to 1,450 tokens per turn (+41%) for +20 points success; no equal-token best-of-N arm | Jhaveri et al. 2026 [d05] | [S] |
| Human original of Think-in-Opposites | N=180, 60 per group; success 78.33% (opposites) vs 38.33% (properties) vs 36.66% (control); chi-square(2)=27.986, p<.001; one task only | Branchini et al. 2025 [d03] | [S] |
| Reasoning models falsify more and succeed more | FalsifyBench: GPT-5.2-Chat 75%, GPT-OSS-120B 68%, best instruction-tuned DeepSeek-V3.1 41%, other instruction-tuned 33-35%, GPT-5-Nano 12%, Qwen3.5-9B 21%; 12 models x 100 games | Bertolazzi et al. 2026 [a22, b16, c06] | [S] |
| Positive-test share predicts failure | Spearman rho -0.937 (p<0.001, 12 models); mixed-effects coefficient -4.15 (OR 0.016) vs oracle error -0.12 (OR 0.885, interval spans zero); n=1,200 games | Bertolazzi et al. 2026 [a23, b17, c07] | [S], observational across models |
| Conclusive falsification rates | GPT-OSS-20B 59.2%, GPT-OSS-120B 53.4%, GPT-5.2-Chat 49.5%, GPT-5-Nano 26.6%, Llama-4-Maverick 18.0% | Bertolazzi et al. 2026 [a23, c08] | [S] |
| Frontier models weak at multi-turn rule induction | WILT: Claude 3.5 Sonnet 14/50, o1-mini 13, o1-preview 12, chatgpt-4o-latest 11, GPT-4o 9, Llama 3.1 405B 8, GPT-4o-mini 6, Gemini 1.5 Pro 5 | Banatt et al. 2024 [a24, c10] | [E] with FalsifyBench |
| Test quality is the bottleneck | o1-mini 19/50 with cases from chatgpt-4o-latest vs 13/50 alone and best single model 14/50 | Banatt et al. 2024 [c11] | [S] |
| Agreeable AI partner cuts human discovery | Discovery: random sequences 29.5%, disconfirming 14.1%, agreeable 11.8%, confirming 8.4%, default GPT-5.1 5.9%; default vs random 23.6 points, CI [-34.0, -13.2]; chi-square(4)=28.02, p<.001, n=504 of 557 | Batista and Griffiths 2026 [a20, a21, c14, d01] | [S] |
| Confirming AI raises confidence | Round 3 minus round 1 confidence: confirming +9.5, default +5.4, disconfirming -20.6, random -56.8; F(4,507)=72.67, eta2=.36 | Batista and Griffiths 2026 [c15, d01] | [S] |
| Disconfirming generator does not restore discovery | 14.1% vs 29.5% random; disconfirming vs confirming p=.143; default vs disconfirming 8.2 points, p=.043 one-sided | [d01, a20] | [S] |
| Distilling falsification traces | 8B AIME 2025 0.60 vs 0.33 (p=0.0386); 32B 0.80 vs 0.73 (p=0.6875, ns); Wason success of 8B almost tripled; GSM8K loss at most 2% | Jhaveri et al. 2026 [a19, b14, c05] | [S]; training, not usable by a scaffold |
| Founder training in hypothesis testing: pivots | 116 startups (of 164 applicants), 41 pivots by 30 firms; 19 treated vs 11 control firms pivoted; 7 treated vs 1 control pivoted more than once; coefficients 0.261 (p=0.027), neg. binomial 0.803 (p<0.001), panel 0.016 (p=0.033) | Camuffo et al. 2020 [a05, a06, b02] | [E] (two RCT papers) |
| Same training: revenue | 17 of 116 firms earned revenue (9 treated, 8 control); 85 of 107 revenue observations from treated firms; cross-section 10,799.5 euros (p=0.010); winsorized 2,666.8 (p=0.008); sinh 0.396 (p=0.065); panel linear 674.97 (p=0.127, ns); panel winsorized 172.5 (p=0.037) | Camuffo et al. 2020 [a07, b04] | [C] fragile to specification |
| Same training: exit and confidence | 44 exits (24 treated, 20 control); cross-section exit 0.035 (p=0.045); Cox p=0.101, panel p=0.716 ns; confidence to abandon 4.4 vs 3.2 (p<0.01, 81 firms) | Camuffo et al. 2020 [a08, b03] | [S] |
| Pooled replication | 759 firms, 4 RCTs (one listing says 754); more terminated ideas; nonlinear pivots; working paper read as "fewer pivots, higher performance" | Camuffo et al. 2024 SMJ [a11, b06, d16] | [E] on direction; revenue and fragility unchecked |
| A/B testing and startup performance | 35,262 startups, 173 weeks; adoption 7.6% at start, 16.75% ever; page views +280% raw, +46% fixed effects, +11.8% with tech-stack control, +8.5% with growth trends; launches +9% to 18% (0.067); event study +8% after one year, no pre-trend | Koning et al. 2022 [a12, a13, b07, b08] | [S] observational |
| A/B testing moderators | Gain concentrated in firms older than about 5 years; youngest interval includes zero; experienced managers gain more | [a14, b09] | [S] exploratory |
| LLM business adviser: split effect | N=640 Kenya; average +0.05 s.d. (CI -0.06 to 0.16); high performers +0.19 s.d. (p=0.07, about +15%); low performers -0.09 s.d. (p=0.007, 8% in working paper, nearly 10% published); difference 0.267 s.d. (p=0.013) | Otis et al. 2024 [a26, a27, b10, c25, d15] | [S] |
| Mechanism of the split | Usage was similar (0.59 more messages for high performers, p=0.33); low performers adopted generic advice (for example price cuts); text model predicted performer type at 43.2% and 51.8% | [a27, b11, d15] | [S] exploratory |
| Self-correction without external feedback fails | GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1) and 41.8 (round 2); GPT-4 GSM8K 95.5 to 91.5 and 89.0; GPT-4 HotpotQA 49.0 to 43.0; GPT-3.5 GSM8K kept 74.7%; with oracle labels GPT-4 GSM8K 97.5 | Huang et al. 2024 [b21, b22] | [E] (also in SCHEMA 4b) |
| Information gain is not always best | Number Game: easy rules EIG 3-8 queries vs positive-test 2-6 vs passive 2-5; hard rule "digits sum to <8" EIG 43, others did not finish; all fail when the proposer gives the target little mass | Chari and Pattanaik 2026 [b19, d02] | [C] one workshop paper |
| Information-seeking beats instruction | Mix colour task, basic/contaminated/wrong label: vanilla 52/46/6, with in-context examples 58/56/2, InfoSeeker 76/80/14; telling baselines about uncertainty barely helps | Fang and Ke 2025 [c16, c17] | [S] |
| Pre-action verification | Static verifier: 9,930 commands, 482 tools, 95.8% invalid caught at 10.0% false positives; ALFWorld 98.7% (134 tasks); removing verification: failures 2 to 9, replans 3 to 6 | Althoubi 2026, Qu 2026 [c21, c18] | [E] across 3 sources, narrow domains |
| Closed-loop experiment selection | NewtonBench symbolic accuracy 67.6% vs below 8% for LLM baselines (PySR 24.07%, Bayesian optimization 24.54%); chemistry 35.09% symbolic | Kabra et al. 2026 [c22] | [S] |
| Popper falsification agent | Type-I error 0.082-0.103 at alpha 0.1; power 0.58-0.64 vs ReAct 0.010-0.383 and Self-Refine 0.067-0.476; Fisher combined power 0.65-0.80 but Type-I 0.173-0.311; 9.7x faster than 9 humans; of 128 failed logs 35.9% misread p-values, 28.1% ineffective test choice, 17.2% tests breaking implication | Huang et al. 2025 [d06, d07] | [S] |
| Pre-test scores mislead | LLM research ideas fell 5.382 to 3.406 (-1.976) after execution vs human 4.596 to 3.968 (-0.628); 43 executors; overall gap difference 1.348 (p=.004) | Si et al. 2025 [d08] | [S] |
| LLM plans rated above entrepreneurs' | 10 plans, 250 evaluators; +0.14 s.d. (p<0.001); LLM-investor score correlation 0.52 on 138 plans (about 29% of variance) | Csaszar et al. 2024 [d09, d10] | [S] |
| LLM startup prediction poor | 50 startups (10 successful); GPT-4o accuracy 26%, precision 21.28%; best tool variant 50%, below the 80% from always saying "fail" | Wang et al. 2025 [a25] | [C] vendor authors |
| LLM judges of business ideas | 300 ideas, about 3,000 expert scores; fine-score agreement often near zero or negative | Hirota et al. 2026 [b23] | [S] |
| Arguing a side raises confidence | 60 debates, 10 LLMs; initial 72.9% vs 50% rational, final 83%; both sides at 75% or more in 61.7% | [d12] | [S]; matches G9 |
| Distractor-normalised confidence | TriviaQA ECE Qwen3-8B 0.097 vs 0.149; Gemma-3-4B 0.121 vs 0.252; Qwen3-1.7B worse 0.177 vs 0.104; SimpleQA GPT-4.1 ECE 0.089 vs 0.263 but AUC 0.786 vs 0.800; about 10 calls | DiNCo 2025 [d13] | [S] factual QA only |

## 4. Mechanisms and models

**4.1 Hypothesis-sampled evidence (why confirming tests stall).** If every test is drawn from inside the current hypothesis H, the answer is almost always "yes". The posterior over alternatives barely moves, but the learner's own certainty rises. Implementation: for each candidate rule, store the set of inputs it accepts. A test is informative only if candidate rules disagree on it. Code computes, for each proposed input, how many surviving candidates accept it, and keeps tests that split the set [a21, c15, S7 in SCHEMA].

**4.2 Falsifiability by set relation (FalsifyBench).** Whether a negative test can falsify depends on how the hypothesis set H relates to the true rule T. If H is inside T (guess too narrow), only inputs outside H can reveal it. If H contains T (guess too broad), positive tests inside H can fail. So the test generator must reason about the relation, not just "try to disprove". Implementation: ask the model for the most general and the most specific variant of its guess, then pick inputs that lie between them [c08, a16].

**4.3 Signal-precision model of startup decisions (Camuffo).** Decision: develop if expected value v0 exceeds threshold v*, else pivot or exit. The scientific approach does not push every founder toward exit or pivot; it makes the signal sharper, which lowers false positives and false negatives. The threshold is set before the test (example: reject a hypothesis if fewer than 60% of 50 interviews corroborate; 4 hypotheses, 3 passed, 1 failed). Implementation: every assumption gets a pre-registered pass rule (metric, threshold, sample size) written before the test is run, and code applies it [a09, a10].

**4.4 Discovery-driven plan as a data structure.** Fields per assumption: statement, what depends on it, current evidence, risk (impact times uncertainty), cheapest test, pass rule, status. The reverse income statement is the work-backwards step: start from the target and list what must be true. This is the same move as operator O5 applied to a plan [a02]. Ranking by risk is practitioner advice (Bland and Osterwalder), not tested [a28].

**4.5 Test-then-decide loop with error control (Popper).** Generate a falsification experiment for a hypothesis, get a p-value, combine evidence sequentially, and stop when the combined evidence passes a threshold. Type-I error held near the nominal 0.1. Its most common failures were misreading p-values and choosing tests that do not break the implication, so the part to copy is a check "could this test change the decision?" before running it [d06, d07].

**4.6 Information-seeking as an explicit step (InfoSeeker, AEC, PCE).** Keep a grounded fact store used to commit and a belief store used only to prune. Query the world when unsure, simulate when confident. The planner turns hidden assumptions into a decision tree scored by likelihood, goal gain and cost. The active ingredient is the explicit step: telling the model about uncertainty or adding examples barely moved results [c16, c17, c18, c19].

**4.7 Information-gain query policy.** Maintain a posterior over candidate programs or rules; pick the query with highest expected information gain. Works when the proposer can express the target. Fails by a support-mismatch trap: diagnostic boundary queries push the posterior to regions where the LLM proposes invalid or too-specific programs [b19, d02, c12, c24].

**4.8 Verify-before-commit gate.** A cheap deterministic check before an irreversible step; abstain or replan on failure. Code-run, not model-judged [c21, c18, c20].

## 5. What holds up

**Held up across sources.**
- Default LLMs confirm and do poorly at multi-turn rule induction: WILT 2024 (best 14/50), FalsifyBench 2026 (instruction-tuned at most 41%), Failing to Falsify 2026 (6% to 78%). Two benchmarks by different groups, different task forms [K01, K04].
- Hypothesis-testing training changes founder behaviour in RCTs: the 2020 paper (116 firms) and the 2024 SMJ pooled replication (759 firms in four RCTs) agree that treated firms terminate more ideas and show a different pivot pattern [K07].
- Self-correction without external evidence does not help [b21, b22].
- Verification before acting helps in several 2026 agent benchmarks [K13].

**Replications and failures.**
- Pivot direction flipped between the 2020 paper (treated pivot more: 0.261, p=0.027) and the pooled replication (working-paper reading: fewer pivots, higher performance; SMJ abstract: nonlinear). Pivot count is not a stable outcome [b02, b06, d16].
- The revenue effect in the 2020 paper rests on 17 firms, fails the panel linear specification (p=0.127) and is marginal on sinh (p=0.065) [K08].
- Whether the 759 firms replicate the revenue effect and its fragility is unknown (full text blocked) [d16].
- The 29.5% human discovery rate came from random hypothesis-independent sequences. A disconfirming generator reached only 14.1%, so "just disconfirm" is not enough for the user-facing case [d01].
- Number of firms in the replication, 759 or 754, is unresolved [b06].

**Moderators.**
- Thinking vs non-thinking models: prompt gains are significant for thinking models, mixed for non-thinking (Qwen3-8B non-thinking 0.06 to 0.06) [d04, a18].
- Concept complexity: positive tests are as good or better on easy rules; information gain wins on compound rules; all fail when the proposer cannot express the target [d02].
- Firm age and manager experience for A/B testing [b09].
- Baseline performance for LLM advice: high performers +15%, low performers -8% to -10% [a26].
- Task structure: negative testing is not always better; it fits when the true rule is broader than the guess [c08].

**Interventions that worked.**
- Think-in-Opposites prompt (reasoning models), 42% to 56% on average [a18].
- Explicit information-seeking step (InfoSeeker 76/80/14 vs 52/46/6) [c17].
- Test selection by a separate model or process (WILT pairing, 19/50 vs 14/50) [c11].
- Hypothesis-independent sampling for human users (29.5%) [d01].
- Pre-action verification with a deterministic check [c21].
- Distillation of falsification behaviour (not usable without training) [a19].

**Interventions that did not work or are untested.**
- Dual-Goal prompt in some standard-mode models (Qwen3-32B 33% to 10%) [c03].
- Telling baselines about uncertainty or giving examples [c17].
- Model-based design augmentation in BoxingGym [c23].
- Arguing a side (debate): confidence up, not down [d12].
- Premortem, devil's advocate, assumption maps: no LLM measurement found [d17, d18, K15].
- Switching to thinking mode raised success without raising I:C, so thinking is not the same as testing negatively [a18].

## 6. Language models

**Default behaviour.** Models propose tests that fit their own current guess. Success on Wason-style tasks tracks the share of disconfirming tests (Spearman -0.937 between positive-test share and conclusive falsification across 12 models) [a23, K01].

**Size and mode.** Reasoning models do much better: FalsifyBench 75% (GPT-5.2-Chat) and 68% (GPT-OSS-120B) vs 33-41% for instruction-tuned. Small models are near floor: GPT-5-Nano 12%, Qwen3.5-9B 21%, Qwen3-8B non-thinking 6% [a22]. On WILT (2024) the best was 28% [a24].

**What changed it.**
- Think-in-Opposites prompt: +14 points on average (42% to 56%); +20 points for Qwen3-32B thinking at about 41% more tokens per turn [a18, d05].
- Non-thinking models: +0 to +17 points, not reliably significant [d04].
- Separate test generator: o1-mini 13/50 alone, 19/50 with another model's test cases (N=50) [c11].
- Explicit information-seeking: +24 points on the clean mix-colour task, +34 on the contaminated variant [c17].
- Training on falsification traces: 8B student success almost tripled; math transfer only at 8B [b14].

**Sycophancy as the user-facing failure.** With human users, default GPT-5.1 produced a 5.9% discovery rate against 29.5% for random sequences [d01]. Confirming evidence raised confidence (+9.5) while random sequences lowered it (-56.8) [c15]. The AI chose the test sequences; agents that choose their own tests under a seeded hypothesis were not studied.

**Business tasks.** An LLM adviser gave no average effect; low performers lost 8-10% by adopting generic advice [a26, b11]. LLM-written plans were rated 0.14 s.d. above entrepreneurs' plans without outcome data [d09]; LLM research ideas lost 1.98 of 10 points after execution against 0.63 for human ideas [d08]. LLM startup prediction was 26% for GPT-4o on a 20%-success sample [a25]. Judges agree weakly with experts on fine scores [b23]. Synthetic founders were not tested for accuracy and may inflate optimism [d11].

**Agent loops.** Verification gates and information-seeking steps help in narrow domains: static shell verifier 95.8% caught at 10.0% false positives [c21]; ALFWorld failures 2 to 9 without verification [c18]; NewtonBench 67.6% vs below 8% [c22]; Popper Type-I 0.082-0.103, power 0.58-0.64 [d06].

**Calibration.** Self-debate raised stated win probability 64.1% to 75.2% [d12]. Distractor-normalised confidence cut ECE on factual QA (SimpleQA GPT-4.1 0.089 vs 0.263), not tested on plans [d13]. Agentic overconfidence persists on coding; history-in-context plus a "be judicious" prompt reduced it for some models, mostly by accepting fewer contracts [d14].

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence | Note |
|---|---|---|---|---|
| Revise or confirm an assumption only from external evidence, never from re-reading or self-review | G2, G10, S5 | [E] | b21, b22, K11 | Already in the schema; adds that the check for an assumption must be a run, a tool result or a user-supplied fact. |
| Verify before committing an irreversible step with a deterministic check; abstain or replan on failure | S8, G3 | [E] | c18, c21, c20, K13 | Three sources, narrow domains. Keep the check code-run. |
| Do not use the model's own score of its plan or idea as evidence of quality | G5, G8 | [E] | d08, d09, d10, b23, K19 | Pre-test scores fell 1.98 of 10 points after execution. Two sources. |
| Do not use debate or "argue a side" as a doubt step | G9 | [E] | d12, K20 | Already in the schema; this confirms it for confidence. |
| Do not forecast venture success from LLM judgment; abstain or flag | G (calibration) | [E] on weak accuracy | a25, b23, d10 | Sources are small or vendor-affiliated; keep as a conservative rule. |

### Test first

| Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|
| One-line "test the opposite" instruction in S7 when two candidates still fit | S7 | [S] (K02, K17) | a18, b13, c03, d03, d04 | Only on rule games. Gains mixed for non-thinking models. Needs an equal-token comparison. SCHEMA cites 42% to 56% as [E] with 2 sources; the second source is the human study on one task. |
| Code-computed discriminating test: pick the input where surviving candidates disagree | S7 | [S] | c11, c12, c22, b19, d02 | Works on toy tasks; may hurt on simple rules (support-mismatch trap). |
| Separate test-generating call from the answer-guessing call | S3/S7 | [S] | c11 | N=50, one pairing. |
| Assumption-mapping step (list, rank by risk, one test per top assumption) | S1/S7 or O5 | [C] untested | a02, a28, c28, d18 | No LLM measurement. |
| Pre-registered pass rule per assumption before the test is run | S7/S8 | [S] human only | a09, a10 | Human RCT only. |
| Hypothesis-independent test sampling when the user supplies a hypothesis | S1 input hygiene | [S] | d01, K05 | The study had the AI choose tests for human users. |
| Test-design check: "could this test change the decision?" | S7 | [S] | d06, d07 | Failure analysis from one agent; about 45% of failed logs were test-design failures. |
| Premortem or distractor-normalised confidence for forecasts | G calibration | [C] | d12, d13, d17 | No premortem measurement; distractor method tested on factual QA only. |
| Ask for the riskiest assumption instead of giving generic advice | G calibration to user | [S] | a26, b11, K10 | Mechanism is user adoption of generic advice; not an agent-side test. |
| Memory: record per problem class whether a discriminating test changed the answer | memory | [S] | S9 lessons | No outside evidence. |

## 8. Concrete tests on our bench

All tests: both arms at equal token budgets. The scaffold arm's setup cost counts (G7). Report success per 1,000 tokens as well as raw success. Use at least 3 seeds.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Rule induction (WILT-style 2-4-6 variants, FalsifyBench subset of 100 games) | (a) plain; (b) plain plus one-line opposite-test instruction; (c) best-of-N at the tokens of (b); (d) code-computed discriminating test | Success rate; I:C; success per 1,000 tokens | (b) +10 to +15 points on a reasoning backbone, about 0 on a non-thinking one; (d) beats (b) on compound rules, loses on easy rules |
| T2 | Same items, split by backbone mode | thinking vs non-thinking, each with and without opposite-test | Interaction of mode by prompt | Gain only on thinking |
| T3 | ARC-style or bench items where two candidate programs both fit the examples | S7 as written vs S7 plus code-picked input where candidates differ vs vote | Final correct rate | Small gain only where candidates truly differ; compare against the 34/36 vs 33/36 baseline |
| T4 | Decision items with a hidden fact (business case with 5 planted assumptions, 2 false, answerable by a simulated lookup tool) | (a) plain reasoning; (b) list assumptions, test top 2 by risk; (c) list assumptions, test 2 chosen at random; (d) best-of-N | False assumptions caught; final decision quality; tool calls used | (b) over (a) and (c) only if risk ranking matters; (b) vs (c) isolates the ranking |
| T5 | Seeded-hypothesis items (user states a wrong rule) | (a) agent picks its own tests; (b) code-sampled hypothesis-independent tests; (c) input hygiene: hypothesis moved into a marked block | Discovery rate; confidence change | (b) approaches the 29.5% pattern; (a) near the 6% pattern if sycophantic |
| T6 | Forecasting questions with known outcomes | (a) plain; (b) premortem; (c) distractor-normalised confidence; (d) debate | Brier score; calibration error | (c) better than (a); (b) unknown; (d) worse |
| T7 | Plans with later-known outcomes or executed tasks | self-score vs executed-run score | Rank correlation | Self-score correlates poorly; confirms G5 |
| T8 | Advice items to a simulated low- and high-skill user | generic advice vs forced riskiest-assumption question first | Advice specificity; user-model success | Removes the low-performer loss if the Otis mechanism holds |

## 9. What does not transfer, and why

- **Founder RCT effects (Camuffo).** They depend on weeks of training, real customers, mentors and time. The agent has no customers and no calendar. What transfers is the structure: hypotheses with pre-set thresholds [a05, a09].
- **A/B testing gains (Koning).** Page views of live firms; observational; benefit concentrated in older firms. The agent cannot run live traffic tests [a12, b09].
- **Distillation results.** They change weights; our scaffold cannot [a19, b14, K06].
- **Rule-game numbers.** Wason, WILT and FalsifyBench have a single hidden rule, binary or oracle feedback and cheap tests. Business assumptions have no oracle, tests cost money, and "falsified" is fuzzy. The 42% to 56% lift cannot be assumed for business items [d04, K17].
- **Negative testing as universal.** It fits when the truth is broader than the guess; not otherwise [c08, a16].
- **Simulated customers.** Synthetic founders may inflate optimism; no accuracy was shown [d11].
- **Human sycophancy study.** Humans chose their hypotheses and the AI chose the sequences. An agent choosing its own tests is a different case [d01].
- **Popper numbers.** Statistical hypotheses over data tables with p-values; strategic assumptions have no p-value [d06].
- **Mitchell 1989 "30% more reasons."** Unverified; do not use [b26, d17].

## 10. Open questions

1. Does an assumption-map step beat plain reasoning at equal tokens on any decision benchmark? No study found [d18].
2. Does Think-in-Opposites transfer to open business or forecasting questions and to non-thinking models? Only rule games so far [d04].
3. Does the 759-firm replication report the same revenue effect and panel fragility? Abstract only [d16].
4. Which test policy wins as concept complexity grows, and can code choose it? One workshop paper [d02].
5. Does any premortem or devil's advocate prompt reduce LLM overconfidence? Nothing measured [d17].
6. Do agents resist user-seeded hypotheses when they pick their own tests? [d01]
7. How do LLM-proposed cheap experiments compare with what founders actually ran? Proxies only [d08, d09, d11].
8. Is the Otis low-performer harm reproduced for other advisers, and does forcing riskiest-assumption questions remove it? [d15]
9. What does the extra turn cost versus best-of-N at equal tokens? One data point (+41% tokens per turn) [d05].
10. How much does the bias metric depend on the LLM judge that labels guesses and tests (Failing to Falsify; FalsifyBench oracle 85% to 95%)? [c01, a22]
11. Original sources not opened: Wason 1960, Klayman and Ha 1987, McGrath and MacMillan 1995, Kerr et al. 2014, Mitchell et al. 1989.

## 11. Sources

[V] opened and read; [M] snippet or search summary only.

- [V] Mansoori and Lackeus (2020) Comparing effectuation to discovery-driven planning, lean startup and others. https://doi.org/10.1007/s11187-019-00153-w
- [V] McGrath (2024) Who Learns Fastest, Wins (teaser page only). https://www.ritamcgrath.com/?p=2003
- [V] Camuffo, Cordova, Gambardella, Spina (2020) A scientific approach to entrepreneurial decision making, Management Science. https://doi.org/10.1287/mnsc.2018.3249 and https://www.gwern.net/doc/economics/2019-camuffo.pdf
- [M] Camuffo, Gambardella et al. (2024) replication, SMJ 45(6). https://openaccess.city.ac.uk/id/eprint/32437 ; abstract [V]: https://econpapers.repec.org/RePEc:bla:stratm:v:45:y:2024:i:6:p:1209-1237 ; CEPR abstract [V]: https://causalclaims.trfetzer.com/paper/DP15972.html
- [V] Koning, Hasan, Chatterji (2022) Experimentation and startup performance. https://www.nber.org/papers/w26278
- [M] Wason (1960), as described in Jhaveri et al. https://arxiv.org/pdf/2604.02485
- [M] Klayman and Ha (1987). https://doi.org/10.1037/0033-295X.94.2.211
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to Falsify. https://arxiv.org/abs/2604.02485 and https://arxiv.org/html/2604.02485
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/abs/2606.04751
- [V] Batista and Griffiths (2026) A rational analysis of the effects of sycophantic AI. https://arxiv.org/abs/2602.14270 and https://arxiv.org/html/2602.14270
- [V] Banatt et al. (2024) WILT. https://arxiv.org/abs/2410.10998
- [V] Branchini, Bianchi, Burro (2025) Thinking in opposites improves hypothesis testing in Wason's rule discovery. https://pmc.ncbi.nlm.nih.gov/articles/PMC12402026/
- [V] Chari and Pattanaik (2026) Wild guesses and mild guesses in active concept learning. https://arxiv.org/pdf/2602.06818
- [V] Piriyakulkij et al. (2024) Doing experiments and revising rules with natural language and probabilistic reasoning. https://arxiv.org/abs/2402.06025
- [V] Piriyakulkij et al. (2026) Induction and inquiry via probabilistic programs. https://arxiv.org/abs/2609.01815
- [V] Abe et al. (2026) Deontic conditional reasoning in LLMs. https://arxiv.org/pdf/2603.06416
- [V] Huang et al. (2024) Large language models cannot self-correct reasoning yet. https://arxiv.org/pdf/2310.01798
- [V] Hirota et al. (2026) Aggregate vs personalized judges (PBIG-DA). https://arxiv.org/pdf/2604.22517
- [V] Wang, Ihlamur, Alican (2025) SSFF. https://arxiv.org/abs/2405.19456
- [V] Otis, Clarke, Delecourt, Holtz, Koning (2024) The uneven impact of generative AI on entrepreneurial performance. https://conference.nber.org/conf_papers/f194654.pdf and https://osf.io/download/hdjpk/ ; published version [M]: https://pubsonline.informs.org/doi/10.1287/mnsc.2024.06909
- [V] Fang and Ke (2025) InfoSeeker. https://arxiv.org/abs/2510.01531
- [V] Qu (2026) Active Epistemic Control. https://arxiv.org/abs/2602.03974
- [V] Seo et al. (2026) From assumptions to actions. https://arxiv.org/abs/2602.04326
- [V] Yuan et al. (2026) SAVER, verify before you commit (abstract level). https://arxiv.org/abs/2604.08401
- [V] Althoubi (2026) Look before you leap. https://arxiv.org/abs/2609.11957
- [V] Kabra et al. (2026) LLM-AutoSciLab. https://arxiv.org/abs/2605.24043
- [V] Gandhi et al. (2025) BoxingGym. https://arxiv.org/abs/2501.01540
- [V] Huang et al. (2025) Popper. https://arxiv.org/html/2502.09858
- [V] Si et al. (2025) The ideation-execution gap. https://arxiv.org/html/2506.20803v1
- [V] Csaszar, Ketkar, Kim (2024) AI and strategic decision-making. https://arxiv.org/pdf/2408.08811
- [V] Teutloff (2025) Synthetic founders. https://arxiv.org/html/2509.02605v1
- [V] When two LLMs debate, both think they'll win (2025). https://arxiv.org/abs/2505.19184
- [V] DiNCo (2025). https://arxiv.org/html/2509.25532v2
- [V] Agentic overconfidence (2025). https://arxiv.org/html/2512.24661
- [V] Schonthal (2023) Could generative AI out-entrepreneur humans? https://insight.kellogg.northwestern.edu/article/generative-ai-entrepreneurship
- [V] Innovation Growth Lab summary of Camuffo et al. https://innovationgrowthlab.org/blog/confused-or-unimaginative-how-adoption-scientific-approach-improves-entrepreneurial
- [M] McGrath and MacMillan (1995) Discovery-driven planning, HBR. https://hbr.org/1995/07/discovery-driven-planning
- [M] Kerr, Nanda, Rhodes-Kropf (2014) Entrepreneurship as experimentation. https://doi.org/10.1257/jep.28.3.25
- [M] Mitchell, Russo, Pennington (1989) Back to the future. https://doi.org/10.1002/bdm.3960020103
- [M] Search notes on riskiest-assumption practice and absence of LLM studies (a28, c28, d17, d18); R.A.I.S.E. https://arxiv.org/abs/2504.12090

Links to parallel subfields (not covered here): Debiasing; Argument mapping training; Structured analytic techniques; Forward and backward reasoning; Automated discovery; Imprecise credences; Search theory; Verbal confidence; Heuristics and biases; Technical and physical red teams.
