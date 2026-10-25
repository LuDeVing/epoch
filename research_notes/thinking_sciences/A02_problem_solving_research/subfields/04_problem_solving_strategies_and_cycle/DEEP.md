# Problem-solving strategies and the problem-solving cycle: deep document

*Subfield A02.04. Built from evidence_a-d.jsonl (a01-a32, b01-b30, c01-c28, d01-d23), claims.jsonl (K01-K37) and critique.md in this folder. Evidence ids in brackets. Where critique.md corrected a number, the corrected number is used here. Parallel subfields (means-ends analysis, monitoring, representational change, progress monitoring, verification, adaptive stopping, Soar, diagnosis, Polya, Schoenfeld, debugging, anomaly handling) are only linked, not covered.*

---

## 1. What it is

This subfield asks four questions.

1. What strategies do solvers have? The usual list is decomposition, working backwards, analogy, abstraction, trial and error, and hypothesis testing.
2. How do solvers choose among them, and do they switch when one stops working?
3. What is the problem-solving cycle, and does it describe real behaviour?
4. How do problem type (well- or ill-defined, small or complex) and solver (novice, strong, weak model) change the answer?

Three research traditions meet here.

- **Gestalt and information-processing tradition.** Duncker (1945) and Luchins (1942) on how a solver narrows down a solution and gets stuck. Simon (1973) on well- and ill-structured problems. Gick and Holyoak on analogy.
- **Strategy choice tradition.** Siegler's overlapping waves, Lemaire and Siegler's four parameters of strategic competence, the formal selectors ACT-R (Lovett and Anderson), SSL (Rieskamp and Otto) and SCADS (Shrager and Siegler).
- **Complex problem solving (CPS) tradition.** Dorner's Lohhausen, Tailorshop, and the minimal systems of Funke and Greiff (MicroDYN), with the argument over whether CPS is one ability.

The LLM side is a fourth strand. It asks whether naming a strategy in a prompt helps, whether a model can pick its own strategy, and whether a router or switch rule beats the best fixed strategy at equal cost.

For our agent the practical question is narrow. Do we give the agent a repertoire of strategies, and if so, who chooses (the model, a code rule, a learned table), on what signal, and when does the agent switch? The evidence says: a repertoire exists in people, selection is learned from success counts, noticing a change is the weak point, and in LLMs prompted strategy labels add little by themselves. Gains come from measured switch signals and from cost savings.

---

## 2. History and theories in depth

### 2.1 Duncker, Luchins and the gestalt line

- **Duncker (1945).** Solving proceeds by successive narrowing: from a general solution, to a functional solution, to a specific one. His problems include the radiation (tumour) problem, the box (later candle) problem, gimlet, pliers, weight and paperclip. Box problem: when the boxes already held the tacks, matches and candles, solving was harder than when they were empty. He called the habitual function a narrowing of attention and named the fix recentering [a10, secondary; a11 not opened]. A fixedness effect can double solving time [a10].
- **Luchins (1942) Einstellung.** After six problems that one long method solves, most people used that method on critical problems with a shorter one. A direct instruction helped over half. Controls found the short way at once. The 77% figure in a garbled OCR snippet is unverified [a22, not opened].
- **Kotovsky, Hayes and Simon (1985).** Tower of Hanoi isomorphs with different rules differ greatly in difficulty, so representation drives difficulty, not space size alone [a32, citation only].

These are the human origin of two agent concerns: fixation on a habitual method, and the value of redescribing the problem.

### 2.2 Well- and ill-structured problems

- **Simon (1973).** The line is blurry. The same information-processing principles apply to both. Ill-structured problems are worked on by splitting off well-structured parts [a12, listing only; not opened].
- **Jonassen (1997, 2000).** Well-structured: convergent answer, limited rules, defined parameters. Ill-structured: several solutions and paths, uncertain rules, missing information [d21, summary only].
- **Dorner's five features of a complex problem** (as restated by Funke): complexity, interrelatedness (connectivity), dynamics, intransparency, polytely (conflicting goals) [a15, d22].

No validated operational test of "well- or ill-structured" was found. The only usable proxy is disagreement across repeated attempts [d20], which is an outcome signal, not a structure test.

### 2.3 Dorner, Lohhausen and the logic of failure

- **Lohhausen.** A simulated town with over 2,000 variables. Participants acted as mayor for 10 simulated years in about 10 hours. Success was not predicted by IQ. It was associated with staying calm and switching between analytic and holistic modes [a13, b11]. The raw N and coefficients come from Dorner et al. (1983), which was not opened [a31].
- **Failure list** (Jansson 1994, Dorner): acting on current feedback only, thematic vagabonding, selective information, no self-reflection, hasty action, global hypotheses, fewer tests [a13].
- **Emergency reaction under complexity.** Less self-reflection, fewer intentions, more stereotyping; hasty action with more risk and rule violations; degraded hypothesis work with more global hypotheses, fewer tests and entrenchment [a14]. Ramnarayan et al. (1997) generic errors: inadequate plans, learning blocked by stereotype knowledge, reactive instead of proactive action [a14].
- **Size ladder.** Tailorshop about 20 variables, Moro about 60, Lohhausen about 2,000 [b11]. In small systems, VOTAT analyses the whole system in about 3 minutes; in knowledge-rich systems people need assumed causal relations, global monitoring and heuristics [a16].

The evidence for Dorner's account is qualitative. It is a source of testable trace features, not a set of effect sizes.

### 2.4 The Funke and Greiff line: MicroDYN

- MicroDYN: 3 to 5 variables, about 3 minutes of exploration, a short control phase. A single strategy, vary one thing at a time (VOTAT), is enough [a13, a15, a16].
- Dorner and Funke (2017) now warn that minimal systems risk becoming "minimal valid systems" [a13].
- MicroDYN covers few of the five features: up to three inputs and outputs, mostly no side effects, no conflicting goals [a15]. It adds about 5% of variance in school grades beyond fluid intelligence (modal result) [a15].
- Meta-analysis: CPS and intelligence correlate, mean g = .433 (47 studies, 60 samples, N = 13,740). Newer MicroDYN-type measures correlate most [a17, b10; confirmed from the abstract in critique.md].
- Suss (1999) reports near-vanishing correlations among different complex problems after controlling for processing capacity and prior knowledge [a18, snippet only]. The 2018 editorial: little reason to posit a CPS ability beyond knowledge and reasoning [b15].

### 2.5 Siegler: overlapping waves and the four parameters

- **Overlapping waves** [a05, via Fazio, DeWolf and Siegler 2016]. At any time a person knows several strategies. The same person uses different ones on similar problems, and on the same problem twice. Choice is adaptive to speed and accuracy. Improvement comes from four changes: discovering new strategies, relying more on efficient ones, choosing more adaptively, and executing better.
- **Four parameters of strategic competence** (Lemaire and Siegler 1995): repertoire, frequency, efficiency, adaptivity [b17, b18]. The choice/no-choice method gives unbiased efficiency, because in free choice people pick strategies on the items that suit them [b18, secondary].
- **Formal weakness.** A methods paper that tried to make waves testable found that waves could arise from simple linear growth along one strategy dimension. Fit was below usual cutoffs (CFI .911, RMSEA .075, N = 75) and the author wrote "No substantive conclusions from this illustration can be drawn" [b16]. Waves are a useful description, with thin formal tests.
- **Strategy discovery.** SCADS builds strategies from simple operators using heuristics (such as dropping redundant steps) and filters them with metacognitive constraints. It matched children's addition data in at least eight ways [a20, abstract only]. A later multiplication study found SCADS could not build all children's strategies from recombined addition operators [a20].
- **Rebuilt as a small neural model** (Rahman and Shrager 2025): choice between recall and finger counting by output entropy (confidence), fallback when confidence is low, learning from the fallback. The wave pattern appears (counting rises, peaks, falls to zero). Only numbers 1 to 5; the authors say adaptive choice and discovery are not yet shown [c22].

### 2.6 Formal strategy selectors

| Model | Rule | Fit | Source |
|---|---|---|---|
| ACT-R (Lovett and Anderson) | each strategy is a production with a Bayesian success estimate from past successes and failures; the highest noisy estimate wins | R2 = .99 binned group data, .66 individuals (last 45 problems); one free parameter | a01, a02 |
| SSL (Rieskamp and Otto) | choice probability = expectancy / sum of expectancies; expectancy rises by payoff when the strategy was chosen | predicted choice probability .71 (N = 24) and .58 (N = 120) vs chance .33 | a19 |
| SCADS (Shrager and Siegler) | distribution over strategies plus discovery of new ones | matches at least 8 patterns in children's addition | a20 |
| RCCL (Lovett and Schunn 1999) | represent, construct, choose, learn; re-represent the task when all strategies do poorly | partly supported in 2025 test | a04 |

### 2.7 The analogy line

- Gick and Holyoak (1980, 1983): the main obstacle is noticing that an analog applies. With a hint most apply it. Comparing two analogs builds a schema [a08, a09, b19].
- Catrambone and Holyoak (1989): transfer collapses after a context shift or delay and returns only with three analogs, schema-focused questions and a reworded target [b20].
- Replication doubts: Seiter and Krabbe (2025) find no clear effect of the source's strategy on the target's strategy [b21].

### 2.8 The problem-solving cycle

The generic cycle (understand and represent, plan or choose a strategy, execute, check, learn) is not a single tested theory in the sources collected. What was found:

- RCCL is the closest empirical cycle: represent, construct, choose, learn [a04].
- Siegler's four changes describe how a repertoire develops [a05].
- Self-Discover (select, adapt, implement, then follow per instance) and Plan-and-Solve are the LLM versions [a23, a26].
- Meta-Reasoner (progress report, then choose continue, restart, backtrack or decompose) is an explicit cycle with a controller [a29].
- Polya, Schoenfeld and Soar versions of the cycle belong to parallel subfields.

No study in this set shows that following the cycle in order raises performance. Treat the cycle as a design frame, not as a proven mechanism [E: no evidence either way].

---

## 3. Core findings with exact numbers

Status: E established (two or more independent sources agree), S single-source, C contested. Numbers marked (c) were corrected in critique.md.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| People choose strategies near probability matching to learned success rates | Building Sticks, N = 67, 90 problems, 4 conditions; group fit to matching law R2 = .60 for individuals; extreme users (>=43 of last 45): 18%, 13%, 6% in three conditions | a01 | E |
| ACT-R Bayesian success estimate fits choice | R2 = .99 group, .66 individuals; alpha+beta = 255, noise variance .052 | a02 | E |
| SSL reinforcement fits cue-based strategy choice | predicted probability .71 (N = 24), .58 vs .33 chance (N = 120); after a switch only 27% moved to a compensatory strategy, 65% to take-the-best | a19 | E |
| Noticing a shift predicts adaptation, not working memory | N = 56; aware (18) .44 vs unaware (37) .17 shift; F(1,53) = 12.7; dual-task load no effect | a03 | S |
| Strategy use follows task cues and re-representation occurs under low success | N = 100; cue sensitivity b = 1.03; representation change .71 vs .58, F(1,98) = 8.09 | a04 | S |
| Strong solvers use many strategies; weak ones keep flawed ones | N = 19, 19 strategies coded, mean 11.21 per person, 96% correct; weaker group about 52% correct; kept own strategy on 57% of trials in Exp 3 (switches to correct alternative: t(25) = 5.23, d = 1.06) | a06, a07 | S |
| Recent strategy is chosen again (priming) | .45 vs .41, F(1,30) = 5.68, partial eta2 = .16 | a21 | S |
| Strategy feedback beats outcome feedback for adaptivity | posttest gap to optimal 2.87 vs 6.17; subtraction use 61 vs 45%; no effect in high-IQ children (N = 120 in Study 2) | b17 | S |
| Extra setup cost lowers use of the better strategy | subtraction 47% (pure) vs 38% (mixed) | b30 | S |
| Analogy: noticing is the bottleneck | Exp IV: hint 92% vs no hint 20%; Exp V baseline 10%; two analogs 45 vs 21% pre-hint; good schema 94 vs poor 53% | a09, b19 | E |
| Analogy transfer collapses after context shift or delay | total solutions 65% (30 min) vs 42% (1 week); recovered to 74% with three analogs plus schema questions | b20 | S |
| Replication of source-strategy transfer fails | N = 282, chi2(15) = 22.10, p = .105, V = .13; controls gave the splitting solution 51% | b21 | C |
| Productive failure: problem-first beats instruction-first | 53 studies, 166 comparisons; g 0.36 (CI 0.20-0.51); 0.37-0.58 high fidelity; 0.87 bias-corrected; young pupils and domain-general skills favour instruction first | d01 | S (one meta-analysis, abstract read) |
| MicroDYN: effective strategy (VOTAT) helps but is not necessary or sufficient | N = 4,371; effective use falls about 20% with more inputs; guessing common | b13 | E |
| CPS profile gaps | N = 1,343; profiles 84.3% / 6.2% / 3.1% / 6.5%; CPS means 61.37 / 35.39 / 27.03 / 22.75; F(3,1339) = 187.28 | b14 | S (profile means not re-found in text, critique.md) |
| Transfer MicroDYN to Dynamis2 | N = 165; d = 0.40; about 40% transfer; VOTAT-performance r = .28; PULSE carried transfer (exploratory) | b12 | S |
| Knowledge and control dissociate | r about .35 to .41 | b24 | S |
| CPS and intelligence | mean g = .433, 47 studies, N = 13,740 | a17, b10 | C (measurement dispute) |
| No prompt-named strategy beats no strategy | TruthQuest Phi-4 / R1-Distill: none 47.2 / 63.4; four strategies 45.1-49.0 / 61.4-63.0 | b01 | S |
| Oracle over strategies is far above best fixed | TruthQuest oracle 82.9 / 90.1 vs best 49.0 / 63.4; ZebraLogic oracle 37.7 / 36.4 vs 27.3 / 32.0 | b02 | E |
| Merging strategy outputs recovers a fraction | Phi-4 best single 49.0, majority 54.9, vote+prob 57.3, vote+verifier 55.8, verifier alone 46.9, oracle 82.9; ZebraLogic gains +0.6 to +1.0; R1-Distill verifier 74.1 | b03 | E |
| Per-paradigm routing: small accuracy gain, large cost gain | 18k runs, 761 tasks per pair, 4 models, 6 paradigms; oracle +17.1 over best fixed; router 53.1 vs best fixed 50.3 vs Direct 47.6; recovers 26% of gap; GPT-5 tokens about 7.0k routed vs 14.0k always-ReAct vs 3.5k always-Direct | d02 | E |
| Learned (model, strategy) router | 82.5% at 1091 tokens vs QwQ-32B 80.0 at 2745; OOD 94.2 at 394 vs 93.7 at 1387; Qwen3-4B thinking 82.4 at 3112.8 vs non-thinking 73.4 at 592.1 vs router 83.8 at 1321.1 | b08, c11, c12, d04 | E |
| Self-chosen strategy fails below the frontier | self-routing avg 48.4 vs Direct 47.6; GPT-5 67.1 vs 60.3; Qwen3-Max 42.4; Qwen3-30B 27.5 (both below Direct) | d18 | S |
| Escalate on low consistency cuts cost | cost cut 46-85% vs GPT-4 alone; GSM8K 92.49 vs 87.93 at equal cost; SVAMP 90.75 vs 88.75; GPT-4 vs GPT-3.5 gap 6-16 points at 7-13x cost (c) the "35.8-53.6%" saving is not in the paper | a28, b05, b29, c06 | E |
| Disagreement routing at equal sampling cap | Qwen3-8B across 7 math sets: base 61.3, majority 68.9, routed 75.8 (6 samplings); Qwen3-4B 60.4 / 68.0 / 73.2; DS-R1-Distill-Llama-8B 60.4 / 66.2 / 69.4; ablation AIME24 36.7 base, 56.7 rewrite only, 40.0 majority only, 66.7 full | d03, d20 | S (counted in samplings, not tokens) |
| Self-Discover: task-level composed structure | PaLM 2-L BBH 56 / CoT 60 / PS 61 / SD 67; T4D 30 / 40 / 42 / 69; MATH 45 / 42 / 49 / 50.5; GPT-4 BBH 58 / 75 / 73 / 81, T4D 51 / 52 / 53 / 85, MATH 70.5 / 71 / 70 / 73; 10-40x fewer calls than self-consistency | a23, b06, c09 | C |
| Free-text per-instance plans beat JSON on MATH | MATH 1-shot structured 63.50 / 67.50 vs unstructured 75.50 / 76.50 (LLaMA / Mistral); T4D task-level 100.00 / 96.63 | b07, b28 | C |
| Error source after a good plan: execution | 87.5% of 200 structures correct; 74.7% of 99 wrong answers computation; Hanoi algorithm given did not move the collapse point | b27, c10, c24 | E |
| Plan-and-Solve error classes (zero-shot CoT, GPT-3) | 46 wrong answers: misunderstanding 27%, missing step 12%, calculation 7% | a26 | S |
| Abstraction (step-back) | PaLM-2L Physics 66.4 plain / 65.0 CoT / 73.2; Chemistry 70.9 / 75.3 / 81.8; TimeQA 41.5 to 66; GSM8K 75.8 / 84.4 / 84.3; fixes 20.5% of errors, adds 11.9% | a27, c14, c15 | S |
| Decomposition (least-to-most) | SCAN length >= 99% vs 16% CoT; GSM8K 60.97 to 62.39; 5+ step problems 39.07 to 45.23 | a24 | S |
| Analogical prompting (c) | GPT-3.5: GSM8K 75.0 0-shot, 75.8 0-shot CoT, 76.7 5-shot CoT, 77.8 analogical (+1.1 vs 5-shot CoT); MATH 33.0, 33.9, 34.9, 37.3 (+2.4) | c13 (a25 row labels were shifted) | S |
| Search with evaluation (Tree of Thoughts) | Game of 24, GPT-4, 100 tasks: IO 7.3, CoT 4.0, CoT-SC k=100 9.0, ToT b=1 45, b=5 74, best-of-100 CoT 49; about 60% of CoT samples fail after step 1; GPT-3.5 both roles 19, GPT-4 gen + GPT-3.5 eval 64, reverse 31; about 5.5k tokens vs 6.7k for 100 CoT | c04, c05 | E |
| Progress-report controller (Meta-Reasoner) | Game of 24 GPT-4o-mini: CoT 4, ToT 65, MACM 80, Meta-Reasoner 89; no progress report 85; no bandit 82; TheoremQA 84.13 vs 39.46 without bandit | a29 | S |
| Learned strategy choice by training (SMART) | GSM8K Gemma 7B 40.4 to 55.4, Mistral 7B 56.9 to 67.9, Qwen2 7B 81.9 to 85.4 | c08 | S |
| Strategy as callable tool vs fixed script | Smolbenchmark: Llama3.3-70B 52.8 / 66.0 / 80.0 (baseline / fixed-order prompting / tools); Qwen2.5-32B 79.6 / 82.0 / 88.0; Qwen2.5-7B 75.8 / 74.0 / 80.0; Llama3.1-8B 48.9 / 47.1 / 60.0; GPT-4.1 AIME 2024 32.0 / 42.0 / 53.0 (o1-preview 44.6; 30 items) | d14 | S |
| CoT adds little for reasoning models | GPQA Diamond: o3-mini +2.9 (p = .024), o4-mini +3.1 (p = .003), Gemini Flash 2.5 -3.3 (p = .005); 20-80% longer | d13 | E (with d19) |
| CoT can hurt where deliberation hurts people | artificial grammar GPT-4o 87.5 to 64.4 with CoT; o1-preview 57.7 vs GPT-4o 94.0; Claude 3.5 Sonnet -1.8 (ns) | c23 | S |
| Overthinking on easy items | o1-like models used 1,953% more tokens on 2+3; token output cut 48.6% on MATH500 with no accuracy loss | c25 | S |
| Red herrings fixate LLMs | OnlyConnect: GPT-4 solved 6 of 494 walls (239 of 1976 groups); no red herrings (WordNet set) 471 / 1926; humans 285 / 1405 | c01, c03 | C |
| Classic-style Einstellung in LLMs | six items per cell; 3 steps in every cell with CoT; may be instruction following | d06 | C |
| Cue-triggered rigidity gone in strong reasoning models | mARC: 100 items; most models < 50% in 2025; Claude 4.1 Opus 0.751 vs physicians 0.66 (CI 0.55-0.75) | d07, d08 | C |
| MacGyver functional fixedness | majority-of-people 79.3% vs GPT-4 73.3%; self-reflection cuts infeasible solutions 9.7%, divergent-convergent 4.3% | c16, c17 | C |
| Agents fail to notice the best option changed | set-shifting gpt-5.5 0.14 to 0.86 with rule; deepseek-v4-pro 0.38 to 0.74; mimo-v2.5 and gemini-3.5-flash-lite little or negative | d05 | S |
| Hidden-rule exploration is poor and fixable | OR over AND bias; 16-96 sampled hypotheses remove the gap; typed scaffold alone 87.3 to 77.3, with monitor 89.1 (110 trials per arm, one-tailed) | c19, c20, c21 | E (bias) / S (fix) |
| Long-horizon derailments | Vending-Bench mean net worth Sonnet $2,217.93, o3-mini $906.86, human $844.05, GPT-4o $335.46; CoffeeBench Haiku 4.5 about 40 idle days, net +$454 vs GPT-5.5 +$3,109 | d11, d12 | E |
| Strong LLM in Tailorshop | gpt-5.5, no reasoning, 50 sessions: end value about 305k vs humans 138k | d10 | S |
| Persistent record read by an outside bandit | LIMBO up to 83% lower cost (53% average); MemCon +2.6 to +4.2 over G-Memory, 10.9-24.1% fewer tokens | d15, d16 | E |
| LLMs explore poorly in-context from raw history | only GPT-4 + CoT + external summary worked | d17 | S (abstract only) |

---

## 4. Mechanisms and models

Each mechanism is given in a form an engineer can build.

### 4.1 Success-count strategy selector (ACT-R / SSL style) [a01, a02, a19]

State: for each (task class c, strategy s) keep successes S[c,s] and failures F[c,s].

Rule, ACT-R style:
1. Estimate p[c,s] = (S + alpha) / (S + F + alpha + beta). Lovett and Anderson used alpha + beta = 255, a very strong prior, so estimates move slowly.
2. Add noise to each estimate (variance .052 in their fit).
3. Pick the strategy with the highest noisy estimate.
4. After the attempt, add one to S or F according to a code-run check, not the model's own opinion.

Rule, SSL style (alternative):
1. Expectancy e[c,s] starts at a prior.
2. P(choose s) = e[c,s] / sum over s' of e[c,s'].
3. After use, e[c,s] += payoff (a code-computed score).
4. Add a forgetting factor (Rieskamp's extension, phi = .07, preferred for 30 of 120 people by AIC) so old history decays [a19].

Known behaviours to expect and plan for:
- Entrenchment. Strong early preferences slow adaptation. SSL predicts it; people showed it (only 27% moved to a compensatory strategy after the environment changed) [a19].
- Probability matching rather than always taking the best. For an agent, prefer greedy plus a small explore rate, and explore on purpose when counts are low.
- Cold start: no history for a new class. Use a prior by task class set at the S0 gate, then update [a30, analyst reading].

### 4.2 Switch-noticing rule [a03, d05]

Humans: adaptation after a shift depends on noticing it. LLM agents: they keep calling the old option [d05].

Implementation:
1. Keep a rolling window of results per strategy (last k attempts).
2. If the strategy's recent success rate falls below its long-run rate by a set margin, or a hard failure occurs, raise an explicit "success changed" flag.
3. On the flag, force a strategy re-selection step. Do not leave this to the model's sense of progress.

Result so far: an explicit "reuse the last success, switch after a failure" rule lifted set-shifting accuracy from 0.14 to 0.86 (gpt-5.5) and 0.38 to 0.74 (deepseek-v4-pro), but did nothing for two weaker models [d05]. So the check should be a structural step in the scaffold, tested per model.

### 4.3 Escalation ladder on a measured signal [a28, b05, d03]

Adaptive-Solver ladder:
1. Solve cheaply (small model or simple prompt, 3 samples).
2. Check agreement. In Adaptive-Solver the thresholds by sample size are {1: 1.0, 3: 1.0, 5: 0.8, 10: 0.6} [c06].
3. If agreement is below the threshold, escalate one of: stronger model (cost x7-13 or x20-30), more samples, different prompt method (cost x1-2), finer decomposition [b05, b29].

Disagreement routing (Lin et al.) [d03]:
1. Draw two samples. If they agree, stop.
2. On mild disagreement, take a majority vote over more samples.
3. On persistent disagreement, rewrite (reformulate) the problem and solve again.
4. Cap total samplings (six).

Rewriting helps hard items and hurts easy ones; majority voting is the reverse [d20]. Combined they beat either. Stated blind spot: consistent but wrong answers (false agreement) [d03].

### 4.4 Progress-report controller [a29]

Meta-Reasoner: after each reasoning step the model writes a short progress report. A contextual bandit (LinUCB) reads it and picks continue, restart, backtrack or decompose. A dynamic version lets the model propose new arms. Ablation: no progress report 85, no bandit 82, fixed arms K = 3: 65, K = 5: 72, dynamic: 89 on Game of 24. Caveats from critique.md: single runs, bandit tuned on 30-50 queries, same model scores the reward, and the TheoremQA collapse to 39.46 without the bandit looks like an implementation failure of that arm.

### 4.5 Search with evaluation (decompose, propose, value, prune) [c04, c05]

Tree of Thoughts: propose several next steps, value each (sure / maybe / impossible), keep the best b, repeat. Idea generation is the bottleneck: a strong generator with a weak evaluator keeps most of the gain (64 vs 74 vs 31). Code can hold the state and the pruning.

### 4.6 Hypothesis sampling for hidden-rule tasks [c20]

1. Sample N distinct hypotheses (16 to 96 worked).
2. Weight them equally.
3. Choose the probe that eliminates the most hypotheses.
4. Drop the refuted ones, repeat.

This removed the OR-over-AND bias in the blicket environment. A monitor that detects a wrong hypothesis space was what made the typed scaffold pay off [c21].

### 4.7 Strategy as a callable operation [d14]

Offer four operations as tools the model can call: understand the question, recall related, examine the answer, backtrack. They beat the same steps given as a fixed-order prompt. Use rates: understand-question about 42%, backtrack about 20%. Instruct models, math only.

### 4.8 Task-level plan with compose-and-follow [a23]

Stage 1, once per task type: SELECT relevant modules from about 39 seeds, ADAPT them, IMPLEMENT a reasoning structure (3 calls). Stage 2, per instance: follow the structure (1 call). Competing result: free-text per-instance plans beat JSON [b07]. Rule of thumb from b28: for batches of similar items, share a plan; for mixed items, plan per item.

### 4.9 Confidence-gated fallback [c22]

Use the cheap strategy (recall) while output confidence is high; use the slow one (counting) when it is low; learn from the fallback. Needs calibrated confidence. LLM confidence is poorly calibrated in the sources [d07], so use sample disagreement instead.

### 4.10 Analogy retrieval gate [a09, b19, c13]

Humans fail to retrieve an analog unprompted. Gate: before solving, write an abstract restatement of the problem, list 2-3 earlier solved problems with the same structure, and map them. LLM version: analogical prompting, small gain (+1.1 to +2.4 over 5-shot CoT in GPT-3.5).

### 4.11 Productive failure order [d01]

Attempt first, then retrieve the method, then compare the attempt with the method. Human pooled g = 0.36. No LLM implementation is documented.

---

## 5. What holds up

### 5.1 Holds up

- **Success-based strategy choice in people.** Three independent model families (ACT-R, SSL, RCCL) fit choices from reinforcement of success. Probability matching at group level, overmatching in some individuals [a01, a02, a04, a19].
- **Repertoire plus variation.** Several studies show many strategies per person and use tailored to problem type [a05, a06, b17].
- **Noticing is the analogy bottleneck.** Direction replicated across Gick and Holyoak 1980, 1983 and Catrambone and Holyoak 1989 [a09, b19, b20].
- **No fixed strategy wins across tasks or sizes** for LLMs. Replicated in Zhang et al., Adaptive-Solver, Select-then-Solve [b01, b02, c07, d02].
- **Cost savings from routing and escalation.** Adaptive-Solver, Route to Reason, Select-then-Solve and disagreement routing all report fewer tokens or calls at equal or better accuracy [b05, c11, d02, d03].
- **Execution errors dominate after a good plan.** Self-Discover (74.7%), Step-back (over 90% of residual errors in the reasoning step), Hanoi with the algorithm given [b27, c15, c24]. Exception: Plan-and-Solve on zero-shot CoT found misunderstanding larger than calculation (27% vs 7%) [a26]. The error mix depends on method and model.
- **Strategy matters little for MicroDYN beyond reasoning ability.** VOTAT predicts success, is neither necessary nor sufficient, and is confounded with reasoning [b13, b14, b15, b12].
- **Thinking mode wastes tokens on easy items** [c12, c25, d13].

### 5.2 Failures, boundary conditions and contradictions

- **Analogy base rates.** Gick and Holyoak: controls about 8-10%. Seiter and Krabbe: 51% of controls gave the splitting solution. The source's strategy did not transfer (V = .13) [b21]. Earlier try in 2024 with 40 adults and 37 pupils also failed to confirm. Different coding and population; unresolved.
- **Gick and Holyoak numbers.** The 76% / 49% / 8% figures were seen only in a slide deck, a secondary source [a08, critique.md]. Direction agrees with b19, a09.
- **The Seiter result is a conference paper in German** with different materials [b21].
- **Self-Discover vs instance-level plans.** Gunasekara and Ratnayake's own Self-Discover baseline on BBH (86.59 / 82.04) is far above the original 67 / 81, so the setups are not comparable [critique.md]. Which format wins is task-dependent.
- **Does strategy matter in CPS?** Strategy use predicts MicroDYN success, but VOTAT does not mediate transfer (r = .28) [b12]. These fit as "weak and confounded".
- **CPS as one ability.** g = .433 against near-zero cross-problem correlations after control [a17, a18]. Contested.
- **Oracle gaps are inflated.** The oracle takes the best of four stochastic runs; no resample-only control exists in Zhang et al. [b02]. Select-then-Solve counts one lucky run per paradigm [d02]. The true complementarity is smaller than +17 or +33 points.
- **Merging by vote or verifier** recovers under a third of the oracle gap (Phi-4 TruthQuest 54.9 / 57.3 / 55.8 vs oracle 82.9) and ZebraLogic gains under 1 point [b03].
- **The verifier is unstable**: R1-Distill 74.1 on TruthQuest, Phi-4 46.9 [b03].
- **Meta-Reasoner** is single source with an implausible ablation [a29, critique.md]. SMART needs training [c08].
- **Scaffold alone can hurt.** The typed state machine lowered accuracy (87.3 to 77.3). The monitor restored it (89.1). Vendor preprint, one-tailed test [c21].
- **Einstellung in LLMs is contested.** Red herrings crush GPT-4 (6 of 494 walls) but the ablation also changes semantic difficulty [c03]. The classic-style test has six items per cell [d06]. Cue-based fixation was strong in 2024-25 (most models under 50%) and gone for strong reasoning models in 2026 (0.751 vs 0.66), on the same 100 public items, so contamination is possible [d07, d08].
- **Examples do not install a strategy.** More shots (1 to 10) did not help OnlyConnect grouping [c02].
- **Plain CoT.** Helps non-reasoning models on average, adds +2.9 to +3.1 or even -3.3 for reasoning models [d13]. CoT hurts where deliberation hurts people [c23]. GPT-5 with CoT lost 15 points on HumanEval (85 to 70) [d19].
- **Named strategy in prompt.** No gain over no strategy [b01]. Strategy as a tool call gains [d14]. Not yet reconciled: one tested logic tasks on small open models, the other math on instruct models.
- **Corrections from critique.md that matter.** (1) Analogical prompting gains are +1.1 (GSM8K) and +2.4 (MATH) over 5-shot CoT, not +2.8 and +4.3. (2) The by-size table in Zhang et al. (b04) mislabels models and is unreliable; the safe reading is that no strategy wins at every size, and hard ZebraLogic is 9.4-15.1%, not 8%. (3) Adaptive-Solver's "35.8-53.6% saved" is not in the paper; the headline is 46-85%.

### 5.3 Interventions that worked

- Strategy feedback (naming which method fits) over outcome feedback, in children [b17].
- A hint plus two analogs plus schema questions, in people [b19, b20].
- Explicit success-changed rule, in capable LLMs [d05].
- Disagreement-triggered vote or rewrite [d03].
- Cheap-first escalation [b05].
- Hypothesis sampling and probe selection [c20].
- Strategy operations as tools [d14].
- A monitor added to a typed scaffold [c21].

### 5.4 Interventions that did not work

- Naming a strategy in the prompt [b01].
- Adding more in-context examples [c02].
- Letting weaker models self-route [d18].
- Handing over the full Hanoi algorithm [c24].
- Showing weaker students a better strategy after they chose one (kept own on 57% of trials) [a07].
- Few-shot examples for Einstellung steps [d06].
- Raw history in the prompt for bandit-like exploration [d17].
- Productive failure for young pupils and domain-general skills [d01].

---

## 6. Language models

### 6.1 Prompted strategies

| Strategy | Best number | Condition | Source |
|---|---|---|---|
| Composed structure (Self-Discover) | T4D 30 to 69 (PaLM 2-L), 51 to 85 (GPT-4) | task-level, 3 extra calls | b06 |
| Same, math | MATH 45 to 50.5 (PaLM 2-L), 70.5 to 73 (GPT-4) | small gains | c09 |
| Abstraction | Physics 66.4 to 73.2; TimeQA 41.5 to 66 | knowledge-heavy; none on GSM8K | a27, c14 |
| Decomposition | SCAN >= 99% vs 16%; GSM8K +1.4 | length generalisation | a24 |
| Analogy | MATH 33.0 to 37.3 (GPT-3.5) | +2.4 vs 5-shot CoT | c13 |
| Search | Game of 24 4% to 74% | one task, similar token cost to 100 CoT samples | c04 |
| Plan-and-Solve | six arithmetic sets: CoT 70.4, PS+ 76.7 | text-davinci-003 | a26 |
| Cognitive tools | Llama3.3-70B 52.8 to 80.0 | instruct models | d14 |

### 6.2 What changed the picture

- **Model strength.** Stronger models gain less from structure. GPT-5 Direct 60.3 vs best fixed paradigm 61.8; Qwen3-30B 21.9 vs 31.7 [d19]. SMART: +15 for Gemma 7B, +4 for Qwen2 7B [c08]. Structure pays when it adds information (search, execution), not when it only restates reasoning [d19].
- **Reasoning models.** CoT adds +2.9 / +3.1 / -3.3 on GPQA Diamond and costs 20-80% more time [d13]. Thinking models cost up to 10 times more tokens, with small gain on easy tasks [c12]. Decomposition, abstraction and analogy prompts were not tested on RL reasoning models in any source found [K35].
- **Self-choice.** Only GPT-5 benefits from choosing its own paradigm [d18].
- **Routing.** Router accuracy gains are small (+2.8 points over the best fixed paradigm), cost gains large (about half the tokens of always-ReAct) [d02]. The router chose Direct for 47-73% of tasks [d18]. Disagreement routing gives a larger accuracy gain (+6.9 over majority vote on Qwen3-8B at six samplings) but is counted in samplings [d03].
- **Format.** JSON vs free text matters on MATH (63.5 vs 75.5) [b07].
- **Execution.** Models fail at long procedures even when given the algorithm [c24] (critique: others question the setup; not opened).

### 6.3 Human-like biases

- Red herrings: GPT-4 6 of 494 walls [c01].
- Content effects on Wason selection: realistic rules beat abstract in humans, Chinchilla, PaLM 2-L, GPT-3.5 (z > 2.2) [c18].
- OR-rule preference in hidden-rule tasks, persists under CoT, ReAct and Reflexion [c19].
- Inflexible clinical pattern use in 2025 models, mostly gone for strong reasoning models in 2026 [d07, d08].
- Proposing solutions to unsolvable problems (GPT-4, PaLM2) or calling solvable ones unsolvable (Llama2-7b, Claude2, GPT-3.5) [c16].

### 6.4 Long-horizon, Dorner-like behaviour

- Vending-Bench: all models derail on a mistaken belief about a delivery, then loop; not tied to context fill [d11].
- CoffeeBench: Claude Haiku 4.5 idle-drift, about 40 of 90 days idle (SD 22), onset on days 26, 66, 25 [d12].
- Tailorshop: gpt-5.5 (no reasoning) beat typical human trajectories (about 305k vs 138k) [d10]. Humans with an LLM advisor gained 94k in Phase A, but 13k remained after withdrawal [d09].
- Nobody mapped these failures to Dorner's list or tested a monitor.

---

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory. Status: [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| N1 | Hold a small repertoire of strategies and choose per item; do not assume one fixed strategy wins | O1-O8 repertoire | [E] | K03, K09; a05, a06, b02, c07, d02 |
| N2 | Switch strategy only on a measured signal (failed check, disagreement), never on a schedule or on the model's own say-so | G (switch), S monitor | [E] | K10, K11; b03, b05, d03, d18 |
| N3 | Cheap-first, escalate on disagreement or failed check. Count tokens, not calls | G stopping/escalation | [E] | K11, K30; a28, b05, c06, d02, d04 |
| N4 | Do not add a generic "think step by step" operator for thinking models; keep an easy-item shortcut | G adaptive stopping | [E] | K12, K35; c12, c25, d13, d19 |
| N5 | Keep strategy choice in code from counted checks (success counts per task class and strategy), not from the model's sense of success | memory / G5 | [E] (outside bandits), model use untested | K01, K36; a01, a02, a19, d15, d16 |
| N6 | When showing the model a strategy table, show a summary (tries and successes), not a raw log | memory format | [E] | K36; d17 |
| N7 | Verify steps after choosing a plan; execution errors outnumber plan errors | G verification | [E] | K15; b27, c10, c15, c24 |
| N8 | Run long procedures through code, not text reasoning | O execute | [E] | K15; c24 |
| N9 | Judge by a check on the outcome, not by whether the trace looks like the right method | G3 | [E] | K21; b13, b24 |
| N10 | Keep search with a code-held state for tasks with early dead ends, and spend on idea generation | O search/backtrack | [E] | K18; c04, c05 |
| N11 | Keep several rival hypotheses alive in hidden-rule tasks and pick probes that split them | O hypothesis test | [E] | K27; c19, c20 |
| N12 | Run an analogy step only with an explicit retrieval gate; do not trust the model to notice | memory / O analogy | [E] for the human bottleneck; gain in LLM [S] | K06; a09, b19, b20, c13 |
| N13 | Measure operators on the same items (choice/no-choice), never on self-picked items | bench design | [E] (method) | b18, K09 |
| N14 | Long-horizon runs: add a no-op counter, a repeated-action detector and a belief-versus-observation check | S monitor | [E] failures exist; monitor value untested | K33; d11, d12 |

N14 is established only for the failure modes. The value of the monitor is in "Test first" (U-rows in UNKNOWNS.md).

### 7.2 Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Estimate the oracle gap on our mix with 3+ repeats per strategy; build a router only if the repeat-corrected gap is large | O routing | [S] | K30, K09; d02, b02 |
| T2 | Disagreement-guided routing (two samples, vote, reformulate) at a token cap | G / O reformulate | [S] | K29; d03, d20 |
| T3 | Success-changed check after a strategy stops working | S monitor / G | [S] | K02, K32; a03, d05 |
| T4 | Persistent strategy-success table read by the model, vs none, vs outside bandit | memory | [S] | K36; d15, d16, d17 |
| T5 | Operators offered on demand vs fixed-order script | O unit of strategy | [S] | K37; d14 |
| T6 | Task-level vs per-instance free-text plan; shared plan across similar items | O select/adapt | [C] | K14; a23, b07, b28 |
| T7 | Abstraction (step-back) only for knowledge-heavy items; track fix and break rates | O abstraction | [S] | K16; a27, c14, c15 |
| T8 | Decomposition only when step count is high | O decomposition | [S] | K17; a24 |
| T9 | Analogical recall with self-written list of similar problems | O analogy | [S] | K06, K08; c13 |
| T10 | Attempt-first then retrieve a method vs retrieve first | order | [S] human only | K34; d01 |
| T11 | Fixation check: after a failed approach, force a different frame; includes "is the problem solvable under the constraints" | G / O | [C] | K26; c01, c16, c17, d07, d08 |
| T12 | Progress report plus strategy decision rule after each phase | S monitor / O | [S] | K19; a29 |
| T13 | Direct-answer option for implicit-pattern items | O applicability | [S] | K13; c23 |
| T14 | Strategy review: show the agent its plan next to a better alternative | G | [S] | K05; a07 |
| T15 | Backward verification of an answer | verification | [S] snippet only | K28; c26 |
| T16 | Strategy-fit feedback: failed check says which method class failed | G2 | [S] human only | b17 |

### 7.3 Specific design notes

- **Unit of strategy.** Prefer operators in O1-O8 the agent can call over named templates or fixed scripts [d14]. Keep menus short and in free text [b07].
- **Reset at problem boundaries.** Recent strategy biases choice [a21]; reset the repertoire state per problem and keep counts per class.
- **Make the better operator cheap to invoke.** Setup cost lowers use [b30].
- **Do not credit a strategy for what a better reasoner does anyway** [b14].
- **Use sample disagreement as the difficulty and structure proxy** until a validated well- versus ill-structured test exists [d20].

---

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (count output plus reasoning tokens; cap the more expensive arm to the cheaper one's budget, or compare accuracy per 1,000 tokens at a fixed cap). Use 3 or more repeats per item to separate luck from real differences. Report item counts and a paired test.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Oracle gap | mixed set: logic puzzles, math, knowledge questions, hidden-rule items, 150+ items | 5-7 strategies, 3 repeats each; same-strategy resample oracle as control | oracle minus best fixed, minus resample-only oracle | repeat-corrected gap well below +17; expect under 8 points. Router only if >= 8 |
| B2 Disagreement routing | same set, thinking model | (a) best single strategy; (b) 6-sample majority; (c) 2-sample, vote on mild, reformulate on persistent, cap at same tokens | accuracy at token cap; tokens per item | (c) beats (b) by 3 to 6 points; gain concentrated on hard items |
| B3 Cheap-first | same | always-deep vs cheap with 3-sample agreement escalation | accuracy; tokens | same accuracy, 30-60% fewer tokens |
| B4 Self-choice vs signal | same | model picks strategy; disagreement picks; fixed best | accuracy; self-choice entropy | self-choice at or below fixed on weaker models |
| B5 Success-changed check | stream of items where best strategy flips mid-stream | none; explicit rolling-rate check; outside bandit | items to recover after flip; accuracy after flip | recovery in under 5 items with the check, much slower without; no effect on weak models |
| B6 Strategy table | repeated task classes (30+ items per class) | no table; table shown as summary; raw log; outside bandit | accuracy per class over time; tokens | outside bandit best; summary table close; raw log no gain or worse |
| B7 Operators as tools vs fixed script | math and logic items | same four operations as tools vs fixed-order prompt vs plain | accuracy | tools beat script on instruct models; unknown on thinking model |
| B8 Plan format | batches of 10 similar items and mixed batches | task-level plan; per-instance free-text; per-instance JSON | accuracy; tokens | free text over JSON by several points on math; task-level wins on homogeneous batches |
| B9 Abstraction | knowledge-heavy vs arithmetic items | step-back vs plain | net fix and break rate per item type | gain on knowledge items (+5 to +8), none on arithmetic |
| B10 Decomposition | items of 2 to 10 steps | least-to-most vs plain, by step count | accuracy by step count | gain only at 5+ steps |
| B11 Analogy gate | items with known analogs in memory | agent lists similar solved problems first vs none | accuracy | small gain (+1 to +3); larger if the memory holds real solved cases |
| B12 Attempt first | transfer items (new variant of a taught method) | attempt then retrieve method vs retrieve then solve | transfer-item accuracy | small gain on transfer items, none on standard-procedure items |
| B13 Fixation check | items with a familiar pattern and a blocker; red-herring items | forced alternative frame vs none | accuracy | gain for non-reasoning or small models; none for a strong reasoning model |
| B14 Implicit pattern | artificial-grammar style items | CoT vs direct vs mixed | accuracy | direct beats CoT |
| B15 Long-run monitor | simulated business (vending or Tailorshop style), 3+ seeds | no monitor; no-op counter; belief-check; both | derailments per run; end value | fewer derailments with the monitors |
| B16 Hypothesis list | hidden-rule (blicket / MicroDYN style) with AND rules and 8 objects | free exploration; explicit list of 16-64 hypotheses with probe selection; with and without monitor | rule accuracy; probes used | list beats free exploration; scaffold alone may hurt |
| B17 Progress report | multi-phase items | one-line report plus decision rule vs none | accuracy; tokens | small gain; confirm with a code reward not a self-scored reward |

---

## 9. What does not transfer, and why

- **Probability matching.** People match; an agent should exploit. Matching is a human cost of exploring with limited memory [a01].
- **Working-memory capacity as moderator.** Schunn found no effect of working memory on adaptivity [a03]. LLM context is a different limit. Vending-Bench derailments were not tied to context fill [d11].
- **Stress and emergency reaction.** LLMs have no stress. The stereotyped, hasty, unreflective pattern may appear for other reasons (a mistaken belief, loops). Match by pattern only [a14, d11].
- **Overlapping waves as a developmental curve.** Rise and fall of strategies with age and practice is a learning curve in children. It has weak formal tests [b16] and no direct meaning for a scaffold without weight updates.
- **Child arithmetic and fraction strategies.** Findings from counting, fractions and Building Sticks are about strategy choice among known simple options [a01, a06, b17]. The structure carries over (repertoire, success estimate), the numbers do not.
- **Analogy effects from the radiation problem.** One target problem family, college students [b19, b20]. Replication doubts [b21]. LLMs have the opposite problem (too many near-matches; see red herrings [c01]) and a model's recall is a prompt step, not a memory failure of the same kind.
- **Lohhausen results.** Human, 1980s, small samples, qualitative, contested [b11]. A strong no-reasoning LLM beat people in Tailorshop [d10]. The failure list is a test list, not a prediction.
- **MicroDYN and VOTAT.** Small, well-defined, one strategy enough. Gains do not carry to open ill-defined problems [a13, a15, b10].
- **Productive failure.** Human learners gain from struggle, then instruction. An LLM does not learn from a failed attempt in weights; the analogue is only an in-context contrast [d01].
- **Lemaire's feedback result.** Strategy feedback helps children but not high-IQ children [b17]. No claim for strong models.
- **Intelligence correlations of CPS.** A measurement result about people, no agent use except as a caution [K23].
- **Training-based routing (SMART, learned routers).** Need weight updates or labelled data on every model-strategy pair [c08, c11]. Use as upper-bound references.
- **Prompt-only strategy results from 2023-2024 models** (PaLM 2, GPT-3.5, GPT-4). May not hold for thinking models [d13, d19].

---

## 10. Open questions

1. At equal tokens, does a routed strategy beat the best fixed strategy on our mix, and what is the repeat-corrected oracle gap? Partly closed: router +2.8 (d02), disagreement +6.9 over majority at a sampling cap (d03). No paper fixes tokens.
2. Which switch signal is best: answer disagreement, progress report, verifier, or sub-goal failure? No head-to-head under one budget.
3. Does an LLM read and use its own strategy-success table? Outside bandits work [d15, d16]; raw history in context does not [d17]; no test of a summary table.
4. Do decomposition, abstraction and analogy still help RL reasoning models? Only plain CoT tested [d13, d19].
5. Is Einstellung real in LLMs under the classic Luchins design? Nothing clean. The tests found are tiny [d06] or cue-based [d07, d08].
6. How to classify an item as well- or ill-structured at inference time? Simon (1973) not obtained; Jonassen and Funke seen as summaries only [a12, d21, d22]. Sample disagreement is the only proxy [d20].
7. Do Dorner-style failures occur in LLM agents, and which monitor catches them? Derailments, loops and idle-drift documented [d11, d12], no taxonomy mapping and no monitor test.
8. Does productive failure have an LLM analogue? No test [d01].
9. What is the right unit of a strategy: template, operator, plan structure? Operators as tools led fixed script in one source [d14]; free text led JSON in another [b07].
10. Does the analogy step add anything for a model whose memory holds real solved cases?
11. Is the set-shifting result (d05) about strategy, or only about tool choice? The setting is tool choice. WCST-style LLM paper not identified [d23].
12. What explains the Meta-Reasoner ablation (84.13 vs 39.46)? Likely an implementation artefact.
13. Which parts of Duncker's and Luchins's original data survive? Both monographs were not opened [a11, a22].
14. Why do control rates for the radiation problem differ so much (about 10% vs 51%) [b21]?

---

## 11. Sources

[V] = opened and read (full text, HTML or PDF) this run. [M] = snippet, abstract or secondary summary only. Marks follow the evidence files and critique.md.

**Strategy choice, human**
- [V] Lovett and Anderson (1995) CogSci, Building Sticks Task. https://www.andrew.cmu.edu/user/lovett/cogsci95.html (a01, a02)
- [V] Schunn, Lovett and Reder (2001) Awareness and working memory in strategy adaptivity. Memory and Cognition 29(2). https://www.cmu.edu/dietrich/psychology/memorylab/publications/01_cds_mcl_lmr.pdf (a03)
- [V] Frontiers in Psychology (2025) Task representation and individual differences in strategy selection (RCCL test). https://pmc.ncbi.nlm.nih.gov/articles/PMC11958946/ (a04)
- [V] Fazio, DeWolf and Siegler (2016) Strategy use and strategy choice in fraction magnitude comparison. https://aic-fe.bnu.edu.cn/docs/20160428171728955538.pdf (a05, a06, a07)
- [V] Rieskamp (2008) reanalysis of SSL, Judgment and Decision Making 3(3). https://dlab.sauder.ubc.ca/sjdm/journal/bn6/bn6.html (a19)
- [M] Shrager and Siegler (1998) SCADS. https://www.psychologicalscience.org/journals/psychological-science/1467-9280.00076/ (a20)
- [V] Luwel, Torbeyns, Schillemans and Verschaffel (2009) Priming effects in strategy choice. https://pedagogischestudien.nl/article/download/14426/15932/31398 (a21)
- [V] Luwel and Verschaffel (2008) four parameters of strategic competence. https://revistas.um.es/analesps/article/download/42741/41051/186521 (b17, b30)
- [M] Lemaire and Siegler (1995) Four aspects of strategic change. https://doi.org/10.1037/0096-3445.124.1.83 (b18)
- [V] Boom (2015) Overlapping waves as latent growth plus IRT. https://www.frontiersin.org/articles/10.3389/fpsyg.2015.00289/full (b16)
- [M] Analyst synthesis of three selectors (a30). https://pmc.ncbi.nlm.nih.gov/articles/PMC11958946/
- [V] Rahman and Shrager (2025) A Small Math Model. https://arxiv.org/abs/2509.24068 (c22)
- [M] Rahman and Mishra (2025) A Fragile Number Sense. https://arxiv.org/abs/2509.06332 (c28)

**Gestalt, analogy, fixation**
- [V] Behrens (2003) Thinking outside of the box (on Duncker). https://en.gestalttheory.net/uploads/pdf/GTH-Archive/2003BehrensThinkingOutsideOfTheBox.pdf (a10, secondary)
- [M] Duncker (1945) On problem-solving. https://nierlib.nier.go.jp/opac/opac_link/bibid/BB00521192 (a11)
- [M] Luchins (1942) Mechanization in problem solving. https://escholarship.mcgill.ca/downloads/t435gh114 (a22)
- [M] Kotovsky, Hayes and Simon (1985) Why are some problems hard? https://www.cmu.edu/dietrich/psychology/pdf/kotovsky_vita.pdf (a32)
- [V] (secondary slides) Gick and Holyoak (1980) Analogical problem solving. https://www.slideshare.net/slideshow/analogical-problem-solving/259643516 (a08, a09; numbers not seen in the original)
- [V] Gick and Holyoak (1983) Schema induction and analogical transfer. https://www.gwern.net/doc/psychology/1983-gick.pdf (b19)
- [V] Catrambone and Holyoak (1989) Overcoming contextual limitations. https://sites.lifesci.ucla.edu/psych-reasoninglab/wp-content/uploads/sites/273/2021/04/Catrambone_Holyoak1989.pdf (b20)
- [V] Seiter and Krabbe (2025) Analoges Problemloesen auf dem Pruefstand. https://ojs.dpg-physik.de/index.php/phydid-b/article/download/1477/1736/7964 (b21)
- [V] Sinha and Kapur (2021) productive failure meta-analysis, abstract via OpenAlex. https://doi.org/10.3102/00346543211019105 (b22, d01)

**Well- and ill-structured problems**
- [M] Simon (1973) The structure of ill-structured problems. https://ojs.unbc.ca/index.php/design/article/viewFile/1273/1090 (a12)
- [M] Jonassen (1997) Instructional design models for well- and ill-structured problem solving. https://doi.org/10.1007/BF02299613 (d21)

**Complex problem solving**
- [V] Dorner and Funke (2017) Complex problem solving: what it is and what it is not. https://www.frontiersin.org/articles/10.3389/fpsyg.2017.01153/full (a13, a14, b11)
- [V] Funke (2015) CPS: single ability or complex phenomenon? https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2015.01669/pdf (a15)
- [V] Funke (2014) minimal complex systems. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2014.00739/full (a16)
- [M] Stadler et al. (2015) CPS and intelligence meta-analysis. https://orbilu.uni.lu/handle/10993/22523 and https://doi.org/10.1016/j.intell.2015.09.005 (a17, b10; abstract confirmed in critique.md)
- [M] Suss (1999) critique. https://www.uni-bamberg.de/allgpsych/weitere-personen/dietrich-doerner/ (a18)
- [M] Dorner et al. (1983) Lohhausen and Dorner (1996) Logic of Failure, secondary. https://www.spektrum.de/lexikon/psychologie/lohhausen-untersuchung/8960 (a31)
- [V] Schoppek and Fischer (2017) Common process demands of two complex dynamic control tasks. https://doi.org/10.3389/fpsyg.2017.02145 (b12, b24)
- [V] Molnar and Csapo (2018) Problem-solving strategies, logfile analyses. https://doi.org/10.3389/fpsyg.2018.00302 (b13, b23, b25)
- [V] Wu and Molnar (2022) Logfile analyses of exploration strategies. https://pmc.ncbi.nlm.nih.gov/articles/PMC9332318 (b14, b26)
- [V] Editorial (2018) CPS beyond the psychometric approach. https://pmc.ncbi.nlm.nih.gov/articles/PMC6056815/ (b15)
- [M] Funke (2010) Complex problem solving: a case for complex cognition? https://doi.org/10.1007/s10339-009-0345-0 (d22)
- [V] Welsch (2026) When the AI leaves the Tailorshop. https://arxiv.org/abs/2610.00163 (d09, d10)

**LLM strategy methods**
- [V] Zhang et al. (2025) Reasoning strategies in LLMs. https://arxiv.org/abs/2507.11423 (b01-b04)
- [V] Zhou et al. (2024) Adaptive-Solver. https://arxiv.org/abs/2310.01446 and https://arxiv.org/html/2310.01446v1 (a28, b05, b29, c06, c07)
- [V] Zhou et al. (2024) Self-Discover. https://arxiv.org/abs/2402.03620 (a23, b06, b27, c09, c10)
- [V] Gunasekara and Ratnayake (2025) instance-level Self-Discover. https://arxiv.org/abs/2507.03347 (b07, b28)
- [V] Pan et al. (2025) Route to Reason. https://arxiv.org/abs/2505.19435 (b08, c11, c12, d04)
- [M] Suzgun and Kalai (2024) Meta-Prompting. https://arxiv.org/abs/2401.12954 (b09)
- [V] Zhou et al. (2023) Least-to-most prompting. https://arxiv.org/abs/2205.10625 (a24)
- [V] Yasunaga et al. (2024) Analogical reasoners. https://arxiv.org/abs/2310.01714 (a25, c13)
- [V] Wang et al. (2023) Plan-and-Solve. https://arxiv.org/abs/2305.04091 (a26)
- [V] Zheng et al. (2024) Step-back prompting. https://arxiv.org/abs/2310.06117 (a27, c14, c15)
- [V] Meta-Reasoner. https://arxiv.org/html/2502.19918v4 (a29)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c04, c05)
- [V] Liu et al. (2024) SMART. https://arxiv.org/abs/2410.16128 (c08)
- [V] Naeini et al. (2023) LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167 (c01-c03)
- [V] Tian et al. (2024) MacGyver. https://arxiv.org/abs/2311.09682 (c16, c17)
- [V] Lampinen et al. (2024) Content effects on reasoning. https://arxiv.org/abs/2207.07051 (c18)
- [V] GX-Chen et al. (2025) Language agents mirror human causal reasoning biases. https://arxiv.org/abs/2505.09614 (c19, c20)
- [V] Alderete et al. (2026) Separable pathways for causal reasoning. https://arxiv.org/abs/2604.20039 (c21)
- [V] Liu et al. (2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 (c23)
- [V] Shojaee et al. (2025) The illusion of thinking. https://arxiv.org/abs/2506.06941 (c24)
- [V] Chen et al. (2025) Do not think that much for 2+3. https://arxiv.org/abs/2412.21187 (c25; early sections only)
- [M] Chen et al. (2025) Reverse thinking. https://arxiv.org/abs/2411.19865 (c26)
- [M] Noise, adaptation and strategy (EMNLP 2025). https://aclanthology.org/2025.emnlp-main.391.pdf (c27)
- [V] Zhou et al. (2026) Select-then-Solve. https://arxiv.org/abs/2604.06753 (d02, d18, d19)
- [V] Lin et al. (2026) When to vote, when to rewrite. https://arxiv.org/abs/2604.26644 (d03, d20)
- [V] Ye (2026) Set-shifting behavioral test for harnessed agents. https://arxiv.org/abs/2607.13396 (d05)
- [V] Haq et al. (2025) Is your LLM trapped in a mental set? https://arxiv.org/abs/2501.11833 (d06)
- [V] Kim et al. (2025) Clinical problem-solving, inflexible reasoning. https://arxiv.org/abs/2502.04381 (d07)
- [V] Shidara et al. (2026) Advances in LLM reasoning enable flexibility. https://arxiv.org/abs/2601.11866 (d08)
- [V] Backlund and Petersson (2025) Vending-Bench. https://arxiv.org/abs/2502.15840 (d11)
- [V] Sugiura et al. (2026) CoffeeBench. https://arxiv.org/abs/2606.16613 (d12)
- [V] Meincke et al. (2025) Decreasing value of chain of thought. https://arxiv.org/abs/2506.07142 (d13)
- [V] Ebouky et al. (2025) Cognitive tools. https://arxiv.org/abs/2506.12115 (d14)
- [V] Sharma et al. (2026) LIMBO. https://arxiv.org/abs/2609.14138 (d15)
- [V] Jiang et al. (2026) MemCon. https://arxiv.org/abs/2607.13591 (d16)
- [M] Krishnamurthy et al. (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371 (d17; abstract only)
- [M] WCST-style LLM study, unidentified (d23). https://www.nature.com/articles/s41598-020-72407-7 (nearest human WCST paper; the LLM paper was not recovered)

**Cautions on sources.** All 2026 papers are preprints with no outside replication. Several downloads were truncated by a full disk in the gap pass; the disagreement-routing paper and the set-shifting paper were read as arXiv HTML. The EDRM paper (2605.22873) PDF was damaged and is not used.
