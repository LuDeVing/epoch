# Bayesian models of cognition: deep document

*Subfield C03.01. Built from evidence_a-d.jsonl (a01-a27, b01-b25, c01-c28, d01-d18), claims.jsonl (K01-K26) and critique.md in this folder. Evidence ids are in brackets. "Figure-read" means the number came from figure labels, not prose.*

## 1. What it is

Bayesian models of cognition say that a mind treats thinking as inference. It holds a space of hypotheses. Each hypothesis has a prior (how likely before the data) and a likelihood (how well it explains the data). The belief after the data (the posterior) is prior times likelihood, normalised.

The programme asks "what would an ideal learner do here?" and then checks whether people behave that way. This is Marr's computational level: it says what problem is solved, not which steps solve it.

Three uses of the word "Bayesian" must be kept apart [b09, a08]:
- Normative: Bayes is the yardstick for a good update.
- Descriptive: a fitted Bayesian model summarises behaviour.
- Mechanistic: the brain or a network literally computes posteriors. The programme's own authors say the brain may only approximate Bayes [b06, b22].

Key people: Tenenbaum, Griffiths, Kemp, Goodman, Xu, Perfors. The strands:
1. Everyday prediction from one data point (Griffiths & Tenenbaum 2006).
2. Concept and word learning (size principle, hierarchical priors).
3. Resource-rational and sampling accounts (Vul et al. 2014, Sanborn & Chater 2016).
4. Language-model-era work: eliciting an LLM's prior, testing whether in-context learning is Bayesian, and hybrid systems where an LLM proposes or scores and code does the Bayes.

Why it matters for our agent. The schema selects by prior and fit (G3, S7). This field gives (a) a standard for a correct update, (b) a way to read an LLM's hidden priors, (c) evidence that the LLM should supply likelihoods or hypotheses while code holds the posterior (G5, S4/S7), and (d) a warning that "fits well" can be a post-hoc claim (G3).

## 2. History and theories in depth

### 2.1 The formal core

From the Perfors, Tenenbaum, Griffiths & Xu (2011) tutorial [a06, a24]:
- Posterior is proportional to likelihood times prior.
- A hypothesis is defined by the data it allows.
- Size principle. If examples are drawn from the concept ("strong sampling"), a hypothesis h consistent with n examples has likelihood (1/|h|)^n. Marble example: bag A holds 2 marbles, bag B holds 3. After one red marble A is favoured 1.5 times. After red, green, red, green, A scores (1/2)^4 = 0.0625 against (1/3)^4, about 5 times as likely. Smaller consistent hypotheses win exponentially fast ("suspicious coincidence").
- Hierarchical models learn second-order knowledge (overhypotheses), for example that regions tend to be long thin rectangles, so one example informs the next.

Word learning (Xu & Tenenbaum 2007, as described in the tutorial) [a07]: adults and 3-4 year olds saw 1 or 3 labelled examples of a new word and picked other members from 45 objects in 3 superordinate categories. With one example, generalisation was graded. With three, it sharpened to the narrowest level, as the size principle predicts. Per-condition numbers were not in the text read; this is second-hand.

### 2.2 The 2006 prediction study

Griffiths & Tenenbaum (2006), "Optimal predictions in everyday cognition" [a01-a04, b01, b02, c15]. People saw one value t (a movie has grossed $10M) and guessed the total. Median guesses were compared with Bayesian posterior medians computed from public data tables used as priors.

Design: 350 undergraduates in two groups (208 and 142). Each person answered one item per class, with t drawn from 5 values per class. Group 1: movie grosses, poem lengths, life spans, pharaoh reigns, marriage lengths. Group 2: movie run times, US House terms, cake baking times, waiting times, marriage lengths. Analysed responses: 174 grosses, 197 poems, 197 life spans, 191 pharaohs, 136 run times, 130 House terms, 126 cakes, 158 waiting times.

Three prior shapes gave three prediction shapes [a02]:
- Gaussian prior (life spans, run times): guess pulled toward the mean.
- Power-law prior (grosses, poems): guess is a constant multiple of t (about 1.5 times for grosses).
- Erlang prior (House terms, pharaoh reigns): guess is t plus a constant.

The single uninformative rule p(total) proportional to 1/total (Gott 1993) was rejected as a rule for all domains. Cake baking times have an irregular prior, and people still tracked it [a04].

Misses and corrections (critique item 9):
- Marriage was dropped: 52% answered "forever".
- Six domains use empirical priors with no tuning (grosses, poems, life spans, run times, House terms, cakes).
- Pharaohs needed a subjective scale: 35 students gave a median typical reign of 30 years, giving Erlang b = 17.9 against a true value near 9.34 [a03, b02].
- Waiting times had no known prior. A power law with exponent 2.43 was fitted to the human medians. That part is circular.
- Some evidence lines said "5 of 8 domains". The paper states no such count. Use the wording above.

Fit was judged by eye against bootstrap bars; the main text gives no fit statistic [a01, b01].

### 2.3 The rich-prior versus few-samples dispute

- Mozer, Pashler & Homaei (2008) [b03, b04, c16]: a model where each person has only k=2 stored examples (Min2: take the smaller relevant example, else guess) fits group medians about as well as full Bayes in 8 domains. It has one free parameter (guess factor g = 0.30; 0.03 for life spans). Their discriminating test is between-person variance: small-sample models predict large spread. Humans were more variable than every sample model with k>1 (variance ratio V(d) > 0 over 5 query points). Humans were also more variable than the k=1 and k=2 models in some domains.
- Lewandowsky, Griffiths & Kalish (2009) [c17]: iterated-learning chains converged to the real-world priors, which contradicts Min2 and supports rich individual knowledge. The text read was qualitative.
- Vul, Goodman, Griffiths & Tenenbaum (2014), "One and done?" [a05, b05, b24]: re-plotting the 2006 data shows the spread of individual answers matches the posterior, as if each person drew one sample. Then a theory: if thinking costs time, one sample per decision maximises reward rate.
  - Sample cost equal to action cost: zero samples (guess) is best.
  - Action/sample time ratio below about 10 with symmetric reward: one sample is best. With no punishment for errors the ratio must be 2 or more before a second sample helps.
  - Sequential policies: 0 or 1 samples below a ratio of about 25.
  - Optimal count rises slowly; up to 75 samples only at the cheapest tested costs.
  - Fixed-k, sequential probability ratio test and accumulator rules gave nearly the same reward rate; none won at every ratio.
  - 100 samples often suffice for reasonable inference; 2,500 or more may be needed for close approximation.
- Bowers & Davis (2012) [c18]: the life-span result could come from knowing life expectancy is about 75 and ignoring current age; the 2-instance model fits as well.

Verdict: contested (K03). Group fit alone cannot prove each person holds the full prior.

### 2.4 Critiques and replies

Mostly abstract-level [b07-b12, a19, a20]; c18 is text-level.
- Jones & Love (2011): hypothesis sets, priors and environment assumptions are rarely measured; competing Bayesian models are rarely compared. They propose "Bayesian Enlightenment": tie Bayes to mechanism.
- Bowers & Davis (2012): "just-so stories". Priors, likelihoods and utilities can be tuned afterwards so almost anything fits.
- Marcus & Davis (2013): post hoc practices (choice of task, response measure, prior, likelihood). Probabilistic does not mean optimal. They re-analyse several published models, including the 2006 study; those details were not read.
- Tauber, Navarro, Perfors & Steyvers (2017): separate the normative use from the descriptive use; three case studies show they lead to different conclusions.
- Sanborn & Chater (2016): the brain as a Bayesian sampler. With few samples it produces base-rate neglect, the conjunction fallacy and unpacking effects, so these errors do not refute Bayes. Critics say different sampling assumptions can make nearly any error Bayesian, which is the unfalsifiability complaint.
- 2025 "The myth of the Bayesian brain" and a 2026 heuristic-anchored sampler (heuristic first estimate, samples refine it; fits medical belief updating best in most conditions; N=200 plus re-analysis of Stengard et al. 2022) [b11, b12]: abstract only.
- Griffiths, Chater, Norris & Pouget (2012) reply that showing optimality is rarely the aim. Not opened.

Authors' self-assessment [a08, b06, b22, b23]: "optimal" may not mean best behaviour; the hypothesis space is chosen by the modeller; neural plausibility is unclear. The bridge is resource-rational and sampling process models. Griffiths (2020) [a09, b22]: human intelligence is the best use of limited time, compute and communication; departures from Bayes become predictions, not failures. Caution: cost parameters must themselves be measured or they add freedom.

### 2.5 Other human work (not opened)

Ernst & Banks (2002) [a18]: vision and touch are weighted by reliability, as maximum likelihood predicts (memory only; later suboptimality reviews such as Rahnev & Denison 2018 not opened). Kemp & Tenenbaum (2008) [a22] structural form discovery, Tenenbaum et al. (2011) [a21] "How to grow a mind", Chater et al. (2006) [a23]: memory only. Lake et al. (2017) [b21]: human-like learning needs models, causality and compositionality. Lesson: hypothesis-space design matters more than the update rule.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Median everyday predictions match Bayes with real-world priors | 350 students (208 + 142); 6 of 8 analysed domains with no fitted parameter; fit judged by eye | Griffiths & Tenenbaum 2006 [a01, b01, c15] | single-source (K01) |
| Prior shape sets prediction shape | Gaussian: pull to mean. Power law: about 1.5 x t for grosses. Erlang: t + constant | G&T 2006 [a02] | single-source |
| Pharaoh scale wrong | Erlang b = 17.9 (35 students, median 30 yrs) vs true about 9.34 | G&T 2006 [a03, b02] | single-source (K02) |
| Waiting-time prior was fitted | power-law exponent 2.43, least squares to human medians | G&T 2006 [b02] | single-source; circular |
| Marriage dropped | 52% answered "forever" | G&T 2006 [a01] | n/a |
| Two-sample memory fits group medians | Min2, g = 0.30 (0.03 life spans); 10,000 simulated people; 100 replications | Mozer et al. 2008 [b03] | contested (K03) |
| Humans more variable than all k>1 sample models | V(d) > 0 over 5 query points | Mozer et al. 2008 [b04] | contested |
| Iterated-learning chains converge to real priors | stationary distributions match, qualitative | Lewandowsky et al. 2009 [c17] | contested |
| One sample per decision can be reward-optimal | ratio < ~10: 1 sample; sequential: 0 or 1 below ~25 | Vul et al. 2014 [a05, b05] | single-source (K04) |
| Size principle | (1/2)^4 vs (1/3)^4: ratio about 5 after 4 examples | Perfors et al. 2011 [a06] | single-source (K21) |
| Few-sample samplers reproduce base-rate neglect and conjunction error | model results, no single figure | Sanborn & Chater 2016 [b10] | single-source (K06) |
| Off-the-shelf LLMs update beliefs poorly (flights, 5 rounds, 624 simulated users) | Bayesian Assistant 58% after round 1, 81% final; random 37%; Gemma 2 9B 37%, Llama 3 70B 45%, Gemini 1.5 Pro 51% | Qiu et al. [a13, c01, critique 1] | single-source (K07) |
| Prompt fixes do not close the gap | CoT, numeric options, 30 rounds, base models, verbalised posterior: no meaningful gain | Qiu et al. [a14, b25, c02] | single-source (K08) |
| Fine-tuning on Bayesian predictions works | about 75-76% final (figure-read), about 80% agreement with Assistant; beats oracle teaching; p<0.001; transfers to hotels, web shopping, real users | Qiu et al. [c03, c04, d17] | single-source |
| Humans as the recommender improve over rounds | p = 0.002; 48 users; below Assistant | Qiu et al. [c05] | single-source |
| Training-free code-held posterior | AdaptFuse 76.2% (legacy; 74.0% revised) vs Bayesian Teaching 73.4% vs self-consistency 44.7% vs Oracle 59.1% (Gemma 2 9B); margin over teaching 2.8 -> 0.6 without EMA; N=3 samples 72.8-73.3% | Lin et al. 2026 [c06, d09, d10] | single-source (K09) |
| Accuracy depends on prior typicality | Gemma Original 37% -> about 60% with human-like preferences; regression on L2 distance p<0.001 | Qiu et al. appendix [b15, d16] | single-source (K10) |
| ICL as implicit Bayes (synthetic) | 12 to 16 layers: 81% -> 85% at equal loss 1.33; single concept gives flat curves; order matters | Xie et al. 2022 [a10, b17, c12] | contested (K11) |
| ICL violates the martingale property | GPT-3, 3.5, 4, Llama-2-7B, Mistral-7B; Bernoulli n=50, Gaussian n=100 | Falck et al. 2024 [a11, b16, c13] | contested |
| Belief entrenchment persists | positive Martingale Score in 51 of 54 CoT setups, 7 models; only DeepSeek R1 clearly lower; debate helps, CoT does not | He et al. 2025 [d01, d02] | single-source (K25) |
| LLM prior can be elicited | iterated in-context learning; GPT-4 modes match human priors in 6 everyday tasks; pharaoh differs; visual comparison | Zhu & Griffiths 2024 [a12, a26, b18, c14] | single-source (K12) |
| Output probability steers deterministic tasks | GPT-4 shift cipher 51% vs 13%; reversal 97% vs 53%; rot-13 21% vs 11% | McCoy et al. 2023 [b20] | established (K13) |
| o1 keeps the pull | better on rare variants, still better on high-probability output | McCoy et al. 2024 [d18] | single-source |
| GPT-3 mixed on classic judgments | 12 vignettes, human-like on 12, correct on 6; cab answer 20%; all 3 CRT items intuitive-wrong | Binz & Schulz 2023 [b19, c19] | single-source (K14); old model |
| Bandit regret GPT-3 vs humans | 2.72 (SD 5.98) vs 3.24 (SD 10.26) | Binz & Schulz [a15] | single-source |
| Sycophancy acts as confirming evidence | N=557; discovery 5.9% default GPT, 29.5% random feedback, 14.1% disconfirming, 11.8% agreeable, 8.4% confirming | Batista & Griffiths 2026 [c07] | established with d03 (K15) |
| Agents confirm their own tests; counterexample prompt helps | 11 LLMs; success 6-78%; mean 42% -> 56%; Blicket Qwen3-32B 0.57 -> 0.86; Qwen3-8B 0.32 -> 0.40 | Jhaveri et al. 2026 [d03, d04] | single-source (K24) |
| LLMs assume people are too rational | GPT-4o Spearman 0.94 with max EV, humans 0.48; fit to human choice 0.28-0.41 | Liu et al. 2025 [c20] | single-source (K16) |
| Propose-then-weight fits humans | number game R2 = 0.95 (tuned prior, 100 samples); logical concepts R2 = .81; Zendo online fuzzy .57 vs hard .10 vs ReAct .25 | Ellis 2023; Piriyakulkij 2024 [c21, c22] | established (K17) |
| Bayesian inverse planning beats direct LLMs | MMToM-QA 75.3 / 76.7 vs GPT-4V 44.0, human 93.0; BToM r = 0.93 | Jin et al. 2024; Ying et al. 2024 [c23, c24] | established (K18) |
| EIG question choice at equal tokens | Pruned UoT 48.1 / 88.4 / 63.2 vs CoT-SC 32.6 / 37.6 / 42.5 (20Q / diagnosis / troubleshooting, GPT-4, about 4.6k tokens) | Hu et al. 2024 [d05] | established with c25-c27 (K19) |
| Diversity constraint alone | Llama 3.3 70B 39.4% -> 80.0% (no-repeat question type), 97.4% forced open-ended | Hutson et al. 2025 [d08] | single-source |
| Battleship questions | human mean EIG 1.27 vs raw LLM 0.65-0.66; k=10 samples close the gap | Grand et al. 2024 [c25] | single-source |
| LLM samples are correlated | 60% agreement when both wrong (71 LLMs, 14,042 questions) vs 33% by chance; vote 40.5-41.4% from 100 to 10,000 samples while coverage 82.9 -> 98.4% (MATH, Llama-3-8B) | Kim et al. 2025; Brown et al. 2024 [d11, d12] | established (K23) |
| Self-consistency gains saturate | GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9 | Wang et al. 2022 [d14] | established |
| Prior distilled into weights | standard net needs about 10x more examples; English perplexity 19.67 vs 19.75 (p<1e-20); 5-gram 24.4 | McCoy & Griffiths 2023 [a16, c10] | established (K20) |
| LLM-made tasks give a human-like prior | ERMI beats classical models in 15 experiments; category learning beats 7 rival models in 2 experiments | Jagadish et al. 2024, 2025 [c08, c09] | established with c10 (K20) |

## 4. Mechanisms and models

### 4.1 The basic update (implementable)

State: a list of hypotheses H, each with prior p(h). For each data item d:
1. Compute likelihood p(d|h) for every h.
2. Multiply by the current weight, then divide by the sum so weights add to 1.
3. Repeat. Yesterday's posterior is today's prior [a25].

Use log weights to avoid underflow. Keep the table in code, not in the model's text. This is what the Bayesian Assistant in the flight task does exactly [c01].

Size principle in code: for hypotheses that are sets, likelihood of n examples is (1/|h|)^n if all are in h, else 0 (or a small noise term). Rank consistent hypotheses by prior x (1/|h|)^n. Valid only if examples were sampled from the concept; if they were chosen for another reason the inference changes [a06].

Everyday estimation in code: pick a reference-class prior (Gaussian, power law or Erlang, from data). For observed t, the posterior over total T is proportional to p(T)/T for T >= t. Report the median. Rule of thumb from [a02]: power law gives a constant multiple, Erlang a constant add, Gaussian a pull to the mean.

### 4.2 LLM proposes, code weights (K17)

Ellis (2023) [c21]: the LLM writes 50-100 natural-language hypotheses. Code scores prior times likelihood (does the hypothesis explain each example, judged by the LLM or by running it). Normalise and read off predictions. Ablating the LLM proposer, or using Python hypotheses, fit worse. GPT-4 direct judgments differed clearly from humans. Piriyakulkij et al. [c22] add sequential Monte Carlo belief updating and expected-information-gain experiment design. Fuzzy (soft) rules fit humans; hard rules score higher but fit humans worse.

### 4.3 LLM supplies likelihoods, code holds the posterior (K09, K18)

AdaptFuse [c06, d09, d10]: a symbolic module holds a posterior over a discrete hypothesis set. A frozen LLM gives likelihood-like signals through multiple samples (Dirichlet aggregation). The two are fused by entropy, with a positional EMA. Hypothesis count M = 24, 48, 96, 192 gave 71.8, 74.6, 76.2, 76.0%. Severe misspecification still gave about 69-70%. N = 3 samples gave 72.8-73.3% at 2.63 s; N = 5 passed the Bayesian Teaching point estimate. Cost per round: direct 0.52 s, CoT 2.15, self-consistency 3.67, AdaptFuse 4.35 s. Limits: hypothesis set, parser and likelihood were hand-built per domain; comparison is system-level; no symbolic-only baseline.

BIP-ALM [c24] and BToM [c23]: Bayesian inverse planning with the LM scoring action likelihoods under each goal or belief. Small open models inside the wrapper beat GPT-4V used directly (task is two-choice, chance 50%).

Wong et al. [a17, c28]: the LLM translates language into probabilistic programs; a probabilistic engine reasons. Mostly demonstration, no aggregate score.

### 4.4 Eliciting an LLM's prior by iterated learning (K12)

Zhu & Griffiths [a12, a26]: show the model data d, ask for a hypothesis h, draw new data d' from p(d|h), feed d' back. If the learner samples from its posterior, the chain's stationary distribution equals its prior. This needs sampling, not a modal answer. Settings: tmax = 150 years for male lifespan, 100 for pharaohs, 120 min for cakes. Qiu appendix [d15] gives a cheaper way: ask for verbalised beliefs before any evidence (Gemma 2 9B put most weight on "no preference"; Gemini 1.5 Pro favoured cheaper, shorter, earlier flights). The authors warn these may differ from the prior the model uses when acting.

### 4.5 Information-gain question selection (K19)

Expected information gain (EIG) of a question = expected drop in entropy of the posterior over hypotheses after hearing the answer. Procedure: the LLM samples candidate questions; a program turns each into a partition of the hypothesis set; code ranks by EIG; ask the top one.
- LIPS (Battleship) [c25]: 18 boards; best human EIG 3.61; 97% of human questions had EIG > 0.
- OPEN [c26]: Bayesian optimal experimental design chooses what to ask; an LLM verbalises. Removing verbalisation hurts users.
- UoT [d05, d06]: simulate answer branches, score by information gain. Ablation (figure-read): on 20Q, ToT 33.8 vs ToT with uncertainty reward 45.3; UoT without reward 48.5 vs UoT 54.4. Search gives much of the gain; the reward adds about 6-12 points.
- DPO on 55,000 EIG-ranked pairs [d07]: Success@1 rose INLG 56.7 -> 68.9, Things 51.1 -> 61.1. Training, not scaffold.
- GuessingGame [d08]: one SD more Bayesian IG cut expected game length by 43% (p = 1.77e-7). Simple diversity constraints did almost as well as computing EIG.

### 4.6 Martingale and entrenchment tests (K11, K25)

Martingale test [a11]: a Bayesian's current prediction should equal the expected prediction after more exchangeable data. Generate imagined continuations from the model and compare. Data order should not matter. Uncertainty should shrink at a known rate.

Martingale Score [d01]: per reasoning step, regress the belief change on the prior belief. Positive means updates just track the prior (entrenchment). Beliefs are LLM-judge probabilities, not token probabilities. For CoT forecasting a score of 0.0 gave Brier under 0.25; a score of 0.04 gave worse than chance.

### 4.7 Sample budget logic (K04, K23)

Vul et al.: sampling pays only if samples are independent draws from the posterior and costly in time. For LLMs neither holds [d11-d14]. Pairs of models agree on 60% of questions when both are wrong, so extra samples add coverage but not vote accuracy. A verifier turns coverage into accuracy: SWE-bench Lite with tests went from 15.9% (1 sample) to 56% (250 samples) [d11]. Chen et al. [d13]: majority vote first improves, then can decline as hard queries lose; numbers not extracted.

### 4.8 Resource rationality as design rule (K22)

Use the Bayesian answer as the target. Ask how few samples or steps get near it. Where compute is cheap and parallel, draw several and aggregate in code; where it is costly, stop early [b05, b24].

## 5. What holds up

### 5.1 Held up

- Prior-sensitive prediction in people (group level): every later paper re-uses the same 2006 data (Mozer, Vul, Lewandowsky re-analyse or extend it), mostly from the same labs. No independent replication with new participants was found. Status single-source (K01).
- Resource-rational sampling accounts are accepted even by critics as a better framing than "optimal" (K05, K22, established).
- LLM proposer plus explicit Bayesian weighting fits human concept learning (number game, Zendo, logical concepts; K17, established). All from the Ellis/Tenenbaum orbit, so independence is lower than the count.
- LLM as likelihood inside a Bayesian wrapper beats direct prompting on theory of mind (K18, established; two papers, one task style).
- EIG-based question selection beats unaided LLM questioning (K19, established; four papers) and beat CoT-SC at equal tokens in one paper [d05].
- Confirmation bias in self-chosen tests and the counterexample fix (K15; K24 single-source).
- LLM output follows prior probability of the text (K13, established; two papers, same group).
- LLM samples are correlated, so voting plateaus (K23, established; four sources).

### 5.2 Failures, contested and weak

- Individual-level Bayes: Min2 versus rich priors is unresolved (K03). Vul et al. partly reconcile: each person acts on one sample from a rich posterior.
- Post-hoc fitting: pharaohs and waiting times in the founding paper itself; critics say priors and likelihoods are tuned after the data (K05).
- In-context learning as Bayes: theory holds only in small synthetic models; martingale tests reject exact Bayes in GPT-3/3.5/4, Llama-2, Mistral (K11). Compatible only with "approximately Bayesian". Ranking of which model is closest is inconsistent: a11 says GPT-4 is the Bernoulli exception, c13 says all but GPT-3.5 deviate in the Gaussian task (unresolved, critique item 10).
- No pre-registered Bayesian-versus-rival comparison on LLM behaviour was found.
- Flight-task findings (K07-K10) rest on one preprint family. AdaptFuse's headline moved between versions and the revised comparison is system-level.
- Zhu & Griffiths compare priors by eye with no fit statistic.
- Binz & Schulz: the a15 wording that GPT-3 treated the base rate as irrelevant is wrong; b19 and c19 say it answered the cab problem near-correctly (20%). Use the latter. The model is old and may have seen the vignettes.
- Transfer of stored priors across problems for an agent: no study (K26).

### 5.3 Moderators

- Typicality of the case: the model's prior helps typical cases and hurts atypical ones (37% vs about 60%) [d16].
- Real users add noise: all models, including the Bayesian Assistant, stay well below the 80% seen with simulated users [c04, b14]. Original LLMs did well at round 1 with humans because human preferences are predictable.
- Misspecified hypothesis grids cost a few points (about 69-70% vs 76%) [d10].
- Output probability: GPT-4 shift-13 cipher is over 100 times more common online than shift-12; accuracy follows [b20].
- Prompt wording: small rewording or reordering broke GPT-3 results (Wason A,K,4,7 vs 4,7,A,K) [b19].
- Domain: entrenchment worst in value-laden and paper-review domains, mildest in forecasting [d01]. GATE gains appeared in content recommendation and email verification, not moral reasoning [c27].
- Cost ratio: the optimal number of samples depends on the action/sample time ratio [b05].

### 5.4 Interventions that worked or did not

| Intervention | Result | Evidence |
|---|---|---|
| Chain of thought for belief updating | no gain | a14, c02 |
| Numeric options, 30 rounds, base models | no gain | b25 |
| Verbalised posterior prompt | improves belief-derived prediction in some settings, not direct prediction | a14, c02 |
| Fine-tune on exact Bayesian predictions | about 75-76% vs 81% ceiling; beats oracle labels | c03 |
| Code-held posterior (training-free) | 76.2% vs 44.7% self-consistency; 0.6-point margin over teaching without EMA | d09 |
| Counterexample / Think-in-Opposites prompt | success 42 -> 56 (mean); Blicket 0.57 -> 0.86 | d03 |
| Distilling that behaviour into weights | smaller gain than the prompt | d04 |
| Debate | lowered entrenchment; CoT did not | d02 |
| Critical-thinking prompt | lowered entrenchment only in forecasting; prior-conforming prompt raised it | d02 |
| Diversity constraint on questions | 39.4 -> 80.0% (Llama 3.3 70B) | d08 |
| More samples with vote | plateau 40.5-41.4% | d11 |
| More samples with verifier | 15.9 -> 56% on SWE-bench Lite | d11 |

Note: debate lowering entrenchment sits oddly with G9 (no debate for accuracy at matched cost). The He et al. result concerns a belief-drift metric, with a link to accuracy shown for forecasting only. Treat it as a test item, not a reversal of G9.

## 6. Language models

### 6.1 Do LLMs update like Bayesians?

Off-the-shelf, no. Flight task [c01, a13, critique 1]: after 5 rounds Gemma 2 9B 37%, Llama 3 70B 45%, Gemini 1.5 Pro 51%, random 37%, exact Bayes 81% (58% after round 1). Models are nearly flat from round 1 (figure-read). Humans acting as recommender improved from round 1 to 5 (p = 0.002) and beat small LLMs [c05]. Prompts did not repair this.

What changed it:
- Fine-tuning on the Bayesian Assistant: about 75-76%, about 80% agreement; oracle fine-tuning is worse; the skill transferred to hotels, web shopping and real users [c03, c04].
- External posterior with LLM likelihoods: 76.2% (Gemma 2 9B, legacy), Llama 74.3 vs 76.3, Qwen 65.2 vs 67.3 (teaching vs fusion) [d09].
- Restricting to typical users: 37% to about 60% with no method change [d16]. Part of the "deficit" is prior mismatch.

### 6.2 Is in-context learning Bayesian?

- Theory in a synthetic setting: yes, implicit inference of a latent concept [a10, c12]. Flat curves with a single concept; failure with random pretraining data or unseen concepts.
- Real models: martingale violations and uncertainty not shrinking at the Bayesian rate [c13]. The authors state this falsifies exact Bayes.
- 2025 reasoning models: belief entrenchment in 51 of 54 CoT setups; DeepSeek R1 the one clear exception; GPT-4o forecasting score +0.0018 with no prompt and +0.0156 with a critical-thinking prompt; OpenReview about +0.07 to +0.10 [d01, d02].
- o1 reduces but does not remove the prior-probability effect [d18].

### 6.3 What is the LLM's prior?

GPT-4's elicited priors match human modes in six everyday quantities and differ on pharaohs (closer to the truth than people). Median years for speculative events: 2042 (superhuman AI), 2045 (zero carbon), 2050 (Mars colony) [a12]. LLMs assume people act more rationally than they do (0.94 vs 0.48) [c20]. Priors can also come from LLM-simulated worlds: ERMI [c08, c09].

### 6.4 Famous-task behaviour (old models)

GPT-3 on 12 vignettes [b19, c19, a15]: human-like on all 12, correct on 6. It fell for Linda, answered the cab problem at 20%, gave intuitive-wrong CRT answers, and showed 3 of 6 Kahneman-Tversky choice biases. Bandit regret was lower than humans (2.72 vs 3.24). Fresh, perturbed items are needed because the vignettes are probably in training data. No current-model re-run was found.

### 6.5 Task-prior pull

GPT-4 accuracy follows the probability of the output text: shift cipher 51% vs 13%, reversal 97% vs 53%, rot-13 encoding 21% vs 11%, rare Pig Latin variant 23% [b20]. o1 narrows the gap on rare variants but keeps the sign [d18].

### 6.6 Hybrid systems

Zendo average predictive accuracy (out of 8): human 5.26, direct ReAct 4.60, batch fuzzy 5.35, online fuzzy 6.01, batch hard 6.55 [c22]. ActiveACRE task solving: 0.00 for direct up to 0.35 for the best hard-rule variant. MMToM-QA overall 75.3 / 76.7 vs 44.0 [c24]; text only: human 82.5, GPT-4 48.0, SymbolicToM 63.0, BIP-ALM 71.7 / 70.5. BToM correlation 0.93 [0.91, 0.94] for goals and 0.92 for belief statements; non-mentalising baselines 0.04-0.19 on belief statements [c23].

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Counterexample test when two candidate rules fit.** Code asks the model for an input where they disagree and runs it. Part: S7, G3. Status [E] for the principle (human sycophancy study N=557 plus an 11-LLM agent study). Ids: c07, d03, d04, K15. The schema already lists this; this evidence supports it but the code-run version is still untested. The agent-side numbers are single-source (K24).
2. **Keep counting and normalising in code (G5).** Never let the model carry a running posterior in text. Part: G5. Status [E] for "do not trust running credence" (martingale violations in several model families, CoT no help on belief updating). Ids: a14, b25, c02, a11, c13, d01, K08, K11. The code-held posterior win itself is [S] (Test first).
3. **Propose-then-weight for rule discovery.** The model proposes 50-100 hypotheses in separate draws; code scores prior times likelihood; selection is by weight. Part: S3 to S7. Status [E] (three tasks). Ids: c21, c22, a17, K17. Boundary: the evidence is fit to humans; hard rules score higher on accuracy but fit humans worse.
4. **LLM parses or scores likelihoods, code does inference, on social and inference items.** Part: S7 / code-held inference. Status [E]. Ids: c23, c24, K18. Boundary: two-choice items, simulator data.
5. **Do not count on sample voting to fix shared bias.** G4 already says this; add the numbers (60% shared errors; vote plateau 40.5-41.4% from 100 to 10,000 samples). Use a verifier when many samples are drawn. Status [E]. Ids: d11, d12, d13, d14, K23.
6. **Prior-audit rule.** Any prior or likelihood used in a step is set and logged before the outcome is scored; count steps where it was set afterwards. Part: G3. Status [E] as a critique. Ids: b02, b07, b08, a19, a20, c18, K05, K02.
7. **Low-probability answers get code verification at S8.** When the answer is an unlikely string (rare cipher, reversal, odd format), do not let the model judge it. Part: G3, S8. Status [E]. Ids: b20, d18, K13.
8. **Design rule.** The Bayesian module is a normative check, not a claim about how the model computes. Ids: a09, b22, b23, c11, b09, K22.

### Test first

| Item | Schema part | Status | Ids |
|---|---|---|---|
| Code-held posterior over a hypothesis set with LLM likelihoods vs CoT and self-consistency at equal tokens beyond flights | S4/S7 operator | [S] | c06, d09, d10, K09 |
| EIG ranking of candidate probes vs unranked and vs plain diverse sampling | S6 operator / probe choice | [E] vs unaided, [S] vs diversity | c25-c27, d05-d08, K19 |
| Name the reference-class distribution first for quantity estimates | S1 / G3 | [S] | a01-a04, K01, K02 |
| Elicit the agent's own prior before the task; flag low-probability correct answers | S0 / G3 audit | [S] | a12, d15, b20, K12, K13 |
| Flag atypical cases and shift weight to evidence | S0 / G3 | [S] | b15, d16, K10 |
| Entrenchment check: log belief before and after each evidence item; flag updates that only track the prior | S5 / G10 | [S] | d01, d02, K25 |
| Disconfirming-test operator at impasses | new operator / S7 | [S] | d03, d04, K24 |
| Size-principle tie-break among consistent hypotheses | S7 | [S] | a06, a07, K21 |
| Store solved-problem priors in memory and test transfer | memory | [S] | a24, d17, K21, K26 |
| Few cheap samples plus verifier vs one long deliberation | G11 / G12 | [E] direction, [S] size | d11, d12, b05, K04, K23 |
| Correct the over-rational model of other agents | none (user or adversary prediction) | [S] | c20, K16 |

## 8. Concrete tests on our bench

All arms get equal total tokens (the plain arm gets extra samples to match). Setup cost counts (G7).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Hidden-rule discovery items with a checker (number game, Zendo-style, ARC-like rule families) | (a) CoT + self-consistency; (b) LLM proposes 50 hypotheses, code holds posterior, LLM scores likelihood; (c) as (b) with symbolic likelihood where possible | Accuracy on held-out probes; log-likelihood of true rule | (b) beats (a) by 5 or more points. (c) isolates the LLM likelihood contribution. |
| T2 | Multi-round hidden-preference task (flights, 5 rounds), then a diagnosis task | Plain, CoT, code-held posterior | Accuracy per round | Plain flat near 40-50%; code-held posterior 70%+ on flights; smaller gain off-task. |
| T3 | Rule discovery where the agent picks its own tests | (a) plain; (b) counterexample-required operator; (c) EIG-ranked tests; (d) diverse-question constraint | Success rate; turns to solve | (b) +10 to +14 points over (a). (c) vs (d) tests whether EIG adds anything beyond diversity (d08: diversity alone gave +40 points on 20Q). |
| T4 | Quantity estimation from one value, with known reference distributions | (a) plain; (b) name reference class and shape first; (c) code applies a prior to a model-given distribution | Log error to Bayes median | (b) small gain if model priors are human-like; larger gain from (c) where the model's scale is wrong (pharaoh-like items). |
| T5 | Items whose correct answer is low-probability text | (a) plain; (b) code verification; (c) prior-audit flag then code verification | Accuracy by output-probability bin | Gap high vs low probability (51 vs 13 for GPT-4) shrinks with (b) on checkable items. |
| T6 | Belief-update stream with known posteriors (Bernoulli, Gaussian) | (a) model states probability after each item; (b) code counts; (c) model plus entrenchment flag | Error to exact posterior; martingale score | (a) violates martingale; (b) exact by construction; (c) between. |
| T7 | Typical vs atypical cases of one task | plain vs prior-flag step | Accuracy by typicality bin | Plain about 37% atypical vs 60% typical; flag step closes at most half the gap. |
| T8 | Samples at equal tokens: k = 1, 3, 5, 10 short vs one long, with and without a checker | vote vs checker | Accuracy; error overlap among samples | With checker, accuracy rises with k; with vote, it plateaus by k = 5-10. |
| T9 | Sequence of related problems | stored class prior vs none | Accuracy on later problems | Unknown; no prior evidence. |
| T10 | Predicting a simulated user's or adversary's choice | plain vs plain plus "people are noisy" correction vs data-fitted model | Spearman to human choice | Plain over-rational (0.94 vs 0.48); correction should lower it. |

## 9. What does not transfer, and why

- Human group-level fit does not tell us what any agent does inside. A Bayesian-looking aggregate can come from a cheap rule (Min2) [b03, c18].
- Vul et al.'s one-sample result assumes independent draws from the posterior and costly sampling. LLM samples are strongly correlated and cheap in parallel [d11-d14]. Do not copy "one sample is enough".
- Fine-tuning on Bayesian traces (Bayesian teaching, DPO on EIG pairs): our agent does not train. Only the target behaviour carries over [c03, d07].
- The flight task has a small, exactly computable hypothesis space. Many real tasks do not. Building a grid per domain is real work [d09, d10].
- The 2006 study used public data tables as priors. Our agent has no such tables unless the reference class is supplied.
- The synthetic ICL theory (Xie) covers small models and in-distribution concepts [a10, c12]. It says little about a frontier model.
- Cue-combination optimality (Ernst & Banks) is perceptual and was not opened.
- Neural-implementation claims of the programme: no schema use.
- Famous-vignette results (GPT-3): likely recall from an old model [b19].
- Debate lowers entrenchment (d02) but G9 rests on accuracy at matched cost; the two address different outcomes.

## 10. Open questions

1. Does a code-held posterior beat CoT and self-consistency at equal tokens beyond flights and hotels, for example diagnosis or rule discovery? Only AdaptFuse (one preprint family) and the related UoT work cover this.
2. Is EIG question choice better than plain diverse sampling at equal tokens? No matched-token head-to-head exists.
3. Can an agent's own prior be audited cheaply, and does correcting it raise accuracy where the correct answer is unlikely? Elicitation works; correction is untested.
4. Does naming the reference class first improve estimation in the 2006 paradigm for current models? No direct study.
5. Has any pre-registered Bayesian-versus-rival comparison been run on LLM behaviour? None found.
6. Do stored priors or overhypotheses transfer across problems for an LLM agent? Only weight-level skill transfer is shown.
7. Does flagging atypical cases help? Typicality is measured; no intervention tested.
8. How correlated are samples of the same model (not across models)? Not measured directly; likely higher than the 60% cross-model figure.
9. Is there a decisive test of Min2 versus rich priors? No independent replication of the 2006 study with new participants was found.
10. Are the Martingale Score results robust with token-probability beliefs and with 2026 reasoning models?
11. Critique papers (Jones & Love, Marcus & Davis, Tauber, Sanborn & Chater, the 2025 myth paper) and perceptual suboptimality reviews were seen as abstracts only; their detail needs reading.
12. Xu & Tenenbaum 2007 numbers are second-hand.

## 11. Sources

[V] = opened this session. [M] = snippet or memory only.

- [V] Griffiths & Tenenbaum (2006), Optimal predictions in everyday cognition. https://cocosci.princeton.edu/tom/papers/predictions.pdf ; https://doi.org/10.1111/j.1467-9280.2006.01780.x ; https://sites.socsci.uci.edu/~lpearl/courses/readings/GriffithsTenenbaum2006_OptimalPredictions.pdf
- [V] Vul, Goodman, Griffiths & Tenenbaum (2014), One and done? https://web.stanford.edu/~ngoodman/papers/VulGoodmanGriffithsTenenbaum-COGS-2014.pdf ; https://doi.org/10.1111/cogs.12101
- [V] Perfors, Tenenbaum, Griffiths & Xu (2011), A tutorial introduction to Bayesian models of cognitive development. https://cocosci.princeton.edu/tom/papers/LabPublications/BayesCogDev.pdf ; https://doi.org/10.1016/j.cognition.2010.11.001
- [V, second-hand via the tutorial] Xu & Tenenbaum (2007), Word learning as Bayesian inference.
- [V] Griffiths (2020), Understanding human intelligence through human limitations. https://arxiv.org/abs/2009.14050
- [V] Mozer, Pashler & Homaei (2008). https://www.cs.colorado.edu/~mozer/Research/Selected%20Publications/reprints/MozerPashlerHomaei2008.pdf
- [V] Lewandowsky, Griffiths & Kalish (2009). https://cogsci.syr.edu/wp-content/uploads/2021/03/LewandowkskyGK2009.pdf
- [V] Bowers & Davis (2012). https://pages.ucsd.edu/~mckenzie/Bowers&Davis2012PsychBull.pdf
- [V] Xie, Raghunathan, Liang & Ma (2022). https://arxiv.org/abs/2111.02080
- [V] Falck, Wang & Holmes (2024). https://arxiv.org/abs/2406.00793
- [V] Zhu & Griffiths (2024). https://arxiv.org/abs/2406.01860
- [V] Qiu et al. (2025/2026), Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523
- [V] Lin, Dai et al. (2026), AdaptFuse. https://arxiv.org/abs/2604.03925
- [V] Binz & Schulz (2023), Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] McCoy & Griffiths (2023). https://arxiv.org/abs/2305.14701
- [V] McCoy et al. (2023), Embers of autoregression. https://arxiv.org/abs/2309.13638
- [V] McCoy et al. (2024), o1 and embers. https://arxiv.org/abs/2410.01792
- [V] Wong et al. (2023), From word models to world models. https://arxiv.org/abs/2306.12672
- [V] Griffiths, Zhu, Grant & McCoy (2023), Bayes in the age of intelligent machines. https://arxiv.org/abs/2311.10206
- [V] Lake, Ullman, Tenenbaum & Gershman (2017). https://arxiv.org/abs/1604.00289
- [V] Batista & Griffiths (2026), sycophantic AI. https://arxiv.org/abs/2602.14270
- [V] Jagadish et al. (2025), ERMI. https://arxiv.org/abs/2509.00116 ; Jagadish et al. (2024) https://arxiv.org/abs/2402.01821
- [V] Liu et al. (2025), LLMs assume people are more rational. https://arxiv.org/abs/2406.17055
- [V] Ellis (2023). https://arxiv.org/abs/2306.02797
- [V] Piriyakulkij et al. (2024). https://arxiv.org/abs/2402.06025
- [V] Ying et al. (2024), BToM. https://arxiv.org/abs/2402.10416
- [V] Jin et al. (2024), MMToM-QA. https://arxiv.org/abs/2401.08743
- [V] Grand et al. (2024), LIPS. https://arxiv.org/abs/2402.19471
- [V] Handa et al. (2024), OPEN. https://arxiv.org/abs/2403.05534
- [V] Li et al. (2023), GATE. https://arxiv.org/abs/2310.11589
- [V] He et al. (2025), Martingale Score. https://arxiv.org/abs/2512.02914
- [V] Jhaveri et al. (2026), Failing to Falsify. https://arxiv.org/abs/2604.02485
- [V] Hu et al. (2024), Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271
- [V] Mazzaccara et al. (2024). https://arxiv.org/abs/2406.17453
- [V] Hutson et al. (2025), GuessingGame. https://arxiv.org/abs/2509.19593
- [V] Brown et al. (2024), Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [V] Kim et al. (2025), Correlated errors. https://arxiv.org/abs/2506.07962
- [V] Chen et al. (2024), Are more LM calls all you need? https://arxiv.org/abs/2403.02419 (abstract and intro; numbers not extracted)
- [V] Wang et al. (2022), Self-consistency. https://arxiv.org/abs/2203.11171
- [M] Ernst & Banks (2002). https://doi.org/10.1038/415429a
- [M] Jones & Love (2011). https://doi.org/10.1017/S0140525X10003134
- [M] Tenenbaum, Kemp, Griffiths & Goodman (2011). https://doi.org/10.1126/science.1192788
- [M] Kemp & Tenenbaum (2008). https://doi.org/10.1073/pnas.0802631105
- [M] Chater, Tenenbaum & Yuille (2006). https://doi.org/10.1016/j.tics.2006.05.007
- [M] Marcus & Davis (2013). https://doi.org/10.1177/0956797613495418
- [M] Tauber et al. (2017). https://doi.org/10.1037/rev0000052
- [M] Sanborn & Chater (2016). https://doi.org/10.1016/j.tics.2016.10.003
- [M] Heuristic-anchored Bayesian sampler (2026) and The myth of the Bayesian brain (2025), via europepmc search pages.
