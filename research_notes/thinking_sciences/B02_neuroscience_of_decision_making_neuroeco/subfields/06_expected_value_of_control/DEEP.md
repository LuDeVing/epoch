# Expected value of control: deep document

*Subfield B02.06. Sources: evidence_a-d.jsonl (ids a01-a28, b01-b25, c01-c26, d01-d21), claims.jsonl (K01-K26), critique.md. All numbers below were re-checked in the critique pass unless marked otherwise. Cost-matched comparisons only; nominal-budget gains are upper bounds.*

## 1. What it is

Expected value of control (EVC) is a theory of how a mind decides how much effortful thinking to apply. Shenhav, Botvinick and Cohen (2013) wrote it down in three equations (a01, a02, b01).

- A **control signal** has an identity (which task, which parameter, which attention target) and an intensity (how hard).
- Each candidate signal is scored: EVC(signal, state) = sum over outcomes of Pr(outcome | signal, state) x Value(outcome), minus Cost(signal).
- The system picks the signal with the highest score: signal* = argmax EVC.
- Value is recursive: Value(outcome) = immediate reward + gamma x max EVC at the next state. Today's control choice accounts for later control choices.
- Cost is a monotonic function of intensity. It rises faster at high intensity, so the best intensity sits in the middle.

Three jobs are kept apart: **monitor** (read conflict, errors, delays), **specify** (choose identity and intensity), **regulate** (carry it out). In the original paper the dACC monitors and specifies, and lateral PFC regulates.

The same idea has other names in other fields: value of computation (VOC), rational metareasoning, resource-rational analysis, cost-benefit arbitration. In machine learning it appears as "learn how hard to think" and as a token price on reasoning. All say: think more only when the expected gain beats the cost.

Why it matters for our agent. Schema S0 (gate) and guardrails G11 (think briefly by default) and G12 (spend by difficulty, search only with a foothold) are EVC rules in plain clothes. This document asks which parts of EVC are established enough to put in the schema, and which are only attractive theory.

Scope note. EVC has three layers that have very different evidence:

1. The normative rule (payoff minus cost, choose the best intensity). It is a definition, not a finding.
2. Human behaviour that fits the rule (demand avoidance, effort discounting, reward and efficacy effects). Moderate evidence, small samples.
3. The brain claim (dACC computes EVC). Contested. We do not need it.

For the agent, only layers 1 and 2 matter, and layer 1 is tested through LLM token-budget work (section 6).

## 2. History and theories in depth

**Before 2010: effort assumed aversive, never tested.** Hull's (1943) law of less work held that organisms avoid effort. Kool et al. (2010) note this "appears never to have been subjected to a direct experimental test" for mental effort (a23). Decision research had precursors: Payne, Bettman and Johnson (1993) effort-accuracy trade-off in strategy choice, and Smith and Walker (1993) decision-cost theory.

**Conflict monitoring (Botvinick, Cohen and colleagues, 2001).** In the Stroop network model, response conflict (co-activation of rival response units) signals that control is too weak and should rise (a04). EVC generalises this. Conflict is one input to monitoring; reward, delays, errors, negative feedback and pain are others. The review concedes dACC may track time on task instead (Grinband 2011) (a04, b02).

**Demand avoidance (Kool et al. 2010, 2013).** Given equal pay, people pick the option with fewer task switches. This is the founding behavioural evidence for an intrinsic cost of control (a07, a08, b06). Kool's group also argued the cost is hard to tell from opportunity cost.

**Effort discounting (Westbrook, Kester and Braver 2013).** The COG-ED task prices effort in dollars. It gave the first quantitative cost curve: cost rises with load, is higher in older adults, tracks Need for Cognition, and discounting is not simply subtractive (a09, a10).

**EVC (2013).** Shenhav et al. unified dACC findings under one rule (a01-a04). The review is conceptual. It lists its own weak points: the outcome-relevance prediction is untested, fMRI and single-unit data suggest different dACC functions, and a time-on-task account is a rival (b02).

**Rival views on cost.**
- *Resource account* (ego depletion): control burns a limited fuel. Two large preregistered replications found near zero effect (d01, d02), so this account lost.
- *Opportunity-cost account* (Kurzban et al. 2013): effort is the felt output of a computation about the best alternative use of the same limited machinery. It predicts no fuel tank (a17). Not directly separable from intrinsic cost with current tasks (b06).
- *Effort paradox* (Inzlicht, Shenhav and Olivola 2018): effort is also valued, which a pure cost-minimiser misses (b15, not opened).

**Challenge to the dACC story (Shenhav et al. 2014).** The foraging-value reading of dACC (Kolling et al. 2012) was confounded with choice difficulty. Once de-confounded, dACC tracked difficulty with a quadratic, not linear, relation to forage value (a11). This refutes a rival, but EVC predicts the same thing (harder choices need more control), so it does not prove EVC.

**Learning the value of control.** Lieder, Shenhav, Musslick and Griffiths (2018) made EVC learnable. People use reinforcement learning to predict the value of each control signal from stimulus features (Learned Value of Control, LVOC). This reproduced five earlier experiments (a05, a06). Bustamante et al. (2021) showed a prediction of LVOC: feature-based learning produces over-exertion of control on new stimuli (d14).

**Extensions.**
- Reward changes the *form* of control, not only its amount (Leng et al. 2021, a14). Ritz et al. (2022) frame control as multivariate optimisation with an effort cost that regularises many equal-reward settings (a19).
- Reward and efficacy both matter (Fromer et al. 2021, a12, a13). Efficacy is "how much does effort change the outcome".
- Model-based planning is a control choice too. Kool, Gershman and Cushman (2016) showed the standard two-step task gives planning no payoff, so there was no trade-off to arbitrate; a redesigned task made people plan more (a16).

**Trait and measurement crisis.** The original link between demand avoidance and self-control (r = -.38, N = 50) did not replicate cleanly (b05, b07). The three popular effort tasks do not agree with each other (b07). This weakened trait claims, not the cost-benefit core.

**Machine learning (2020-2026).** Without naming EVC, the LLM literature rebuilt it:
- Rational metareasoning for LLMs (RaM, De Sabbata et al. 2024-2025): reward = correctness minus token cost (c01, a24).
- Compute-optimal test-time scaling (Snell et al. 2024): choose strategy by difficulty bin (c09).
- Learned input-adaptive allocation (Damani et al. 2024), shadow-price allocation (Zhai et al. 2026) (b20, c08).
- Overthinking and underthinking work (Chen 2025; Wang 2025; Zhou 2026) shows the cost of misallocation (b18, c06, d21).
- Formal EVOC for LLM agents (Oh and Gobet 2025, MGV), theory only (c05).

Nobody has run the classic human effort paradigms on an LLM (c25, d19, d20).

## 3. Core findings with exact numbers

Status key: established = replicated or large and consistent; single = one source or one lab; contested = sources disagree; human-only = no LLM test.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Given equal pay, people avoid the higher-demand option | Exp 1, N=43, 500 trials: low-demand choice 0.68 (SD 0.24); 36 of 43 (84%) chose it more, p<0.0001. Errors 1.73% vs 2.58%. 14 subjects who erred more on the low-demand deck still chose it 0.80. 12 unaware subjects 0.71, p=0.02 | Kool 2010 (a07) | established (generalises across demand types) |
| The bias generalises and shrinks with a speed incentive | Exp 4, N=16, subtraction with/without carry: low-demand rate 0.73; RT 1,207 vs 2,026 ms; alpha 0.93. Exp 6B N=51: payment reduced switch avoidance (p<0.01) | Kool 2010 (a08) | established, small N |
| Effort has a dollar price that rises with load | N=25 young, 25 older. Value of $2.00 offer at 4-back: 0.49 (=$0.98) young, 0.20 (=$0.40) old. Load effect young F(1,122)=103, eta2=0.46; old F(1,72)=14, eta2=0.17 | Westbrook 2013 (a09) | established (retest r=.80, b08) |
| Discounting is not a fixed subtraction | $5 offer at 3-back worth $3.07 (decrement $1.93); $1 offer worth $0.60 (decrement $0.40) | Westbrook 2013 (a09) | single |
| Effort discounting tracks delay discounting; bigger offers discounted less | n=33: B=0.30, SE=0.13, P=0.03, R2=0.14 | Westbrook 2013 Exp 2 (a10) | single, modest |
| Effort AUC predicts Need for Cognition | R2=0.10, P=0.02; beat NASA-TLX (P=0.03 vs 0.16) | Westbrook 2013 (a09) | weak replication: r=.168, N=663 (b07) |
| Reward speeds control without losing accuracy | Study 1 N=21: reward b=-9.81 ms (p=.002). Study 2 N=44: -5.03 (p=.004). Study 3 N=35: -7.02 (p<.001) | Fromer 2021 (a12) | single lab, three studies |
| Efficacy speeds control | Study 1 efficacy b=-14.9 ms (p<.001). Study 2 -5.89 (p=.016). Study 3 -3.85 (p=.001) | Fromer 2021 (a12) | single lab |
| Reward x efficacy interaction | Study 1 p=.116 (null). Study 2 b=-9.23 (p=.009). Study 3 b=-2.27 (p=.027). CNV interaction -0.35, p=.046 | Fromer 2021 (a12, a13) | contested (unstable) |
| Reward and penalty move different control parameters | N=32 free-pace Stroop. Reward: faster, accuracy unchanged (p=.612). Penalty: slower, more accurate (Chisq=26.73, p<.001) | Leng 2021 (a14) | single |
| Effort cues overlap with reward cues in ACC/striatum | N=22; RT gap 760 ms; accuracy 98% vs 96% (p=.045) | Vassena 2014 (a15) | single, anatomical overlap only |
| dACC foraging-value reading is confounded with difficulty | Exp 1 N=15 replicated original; Exp 2 dACC quadratic, not linear, in forage value | Shenhav 2014 (a11) | contested (about the brain) |
| LVOC (learned value) fits learning and conflict adaptation | BIC visual search: LVOC 1817.8 vs Rescorla-Wagner 9763.2 vs WSLS 3449.9. Reward-Stroop: LVOC 45.3 vs 1333.9 vs 2454.8. Reward conflict-adaptation 0.6 to 8.0 ms | Lieder 2018 (a05, a06) | single (model fits to published means) |
| Humans over-exert control after feature-based reward learning | N=30. EITHER-frequency lowered reward rate beta=-0.03 (t=-7.30); BOTH-trial errors beta=0.03 (Z=4.38); persisted over 40 BOTH trials | Bustamante 2021 (d14) | single |
| Trait demand avoidance links to self-control | Original N=50: r(48)=-.38; with delay choices -.49. Replication N=217: no link; trait variance 59% | Kool 2013 (b06); Strobel 2020 (b05) | contested |
| Effort tasks do not agree | N=663, six studies, cross-task r<.1. NFC: discounting .168, reasoning .176, demand avoidance .085 (ns). Retest: DST .537, COG-ED .804 | Maekela 2023 (b07, b08) | established |
| Ego depletion (fuel) fails | Hagger: 23 labs, N=2,141, d=0.04 [-0.07, 0.15]. Vohs: 36 labs, 3,531 tested, d=0.06 [-0.02, 0.14], BF about 4.4 for null | d01, d02 | established (null) |
| Willpower-mindset ego-depletion replication fails | Original N=60; replication N=187: no main effect, no moderation | b11 | established (null) |
| Trained token-cost reward shortens chains | 23-45% fewer tokens vs few-shot CoT and STaR. Llama-3.1-8B: STaR 47.4% / 222.7 tokens vs RaM 50.1% / 170.8. Instruct: 61.9% / 215.1 vs 63.5% / 146.2 | De Sabbata (c01, a24) | single paper (3 files) |
| RaM length follows difficulty; plain CoT does not | Easy-vs-hard length gap: RaM 50.3% (3B) and 36.0% (8B); STaR 34.4%, 35.9%; few-shot CoT 19.0%, 23.5%; instruct CoT 0.5%, 0.9% | De Sabbata (a25) | single; hindsight split |
| Cost term can hurt out of distribution | MMLU-CF 8B: 40.2 to 36.4 (-3.8). 3B: 27.0 to 29.5 | De Sabbata (c03) | established across papers (c26) |
| Length-penalty RL loses accuracy | 7B: AIME -16% tokens / -3.3 pts; MATH500 -37% / -2.2; GSM8K -65% / -1.7 | Arora and Zanette (c13) | established (K10) |
| Reasoning models overspend on easy items | '2+3': 1,953% more tokens; 13 solutions; first round correct in over 92% overall (per set about 89-97%); first solution under 60% of tokens; self-training -48.6% tokens on MATH500 | Chen 2025 (b18, c10) | established |
| Basic-math overthinking across 53 models | Reasoning models 6,780 tokens vs 378; accuracy 72% to 44% at 1,024-token limit | LLMThinkBench (c16) | established |
| Extra thinking has a peak then declines | R1-32B AIME: 37.8 (2K), 46.5 (4K), 53.8 (8K), 55.8 (12K), 54.9 (16K); 12K to 16K -0.9 [-1.4, -0.4]. Easy MATH peak 1.5K; Level 5 about 8K; GPQA about 10K. Flip ratio first >1 at 7K (1.09, p=.038) | Zhou 2026 (c06, c07) | established, 60 problems |
| Knee at the smallest budget on easy and medium maths | 7B distilled: 95% of uncapped accuracy at 256 tokens on GSM8K and MATH-500. AIME: 56.5% converge (96.5% accuracy), 43.5% never close (11.5%) | Oladri 2026 (d12) | single, possible extraction artefacts |
| Adaptive allocation beats uniform at equal average cost | Damani: 25-50% less compute (budgets B>=8, oracle verifier); chat 0-10% (25-40% on high-variance subset). Snell: about 4x less than best-of-N (gross, low budgets) | b20, d08, c09, d09 | established with caveats |
| Training-free sample allocation | Adaptive-consistency up to 7.9x fewer samples, <0.1% accuracy drop. ESC saves 33.8% (MATH) to 84.2% (Coin Flip). DEER: -19.1% to -80.1% length, +0.3 to +5.0% accuracy | c18, c19, c20 | established |
| Shadow-price allocation, cost-matched | DeepSeek-V3 MATH: learned 0.575 at cost 2.73; fixed 0.517 at cost 2.00; random 0.534 at cost 2.98. Equal-cost gain about 4.1 pts | Zhai 2026 (c08, critique) | single |
| Predicted allocation fails at generous budgets | GSM8K, 1.5B: adaptive beats uniform at 16-96 tokens (up to +7.9 pts); worse than uniform from about 96-128 | Brown 2026 (d07) | single |
| Difficulty is predictable only moderately | Question-only AUROC 0.83-0.88 (Bulut); two-class accuracy 72-84% (Damani); 3-class 66.3% vs 58.7% majority (Brown); non-convergence vs difficulty r2 about 0.19 (Oladri) | d06, d07, d08, d12 | established as "moderate" |
| Prompt-stated budget moves length by difficulty | TALE-EP GPT-4o-mini: arithmetic 313.5 to 39.6 tokens; College 675.8 to 259.9 (accuracy 78.00% to 70.00%); overall 461.25 to 148.72 tokens, accuracy 83.75% to 81.03% | Han (b19, d17) | single/established for "length can be set"; no price/reward test |
| Too-small stated budget is overrun ("token elasticity") | 157 tokens vs 86 for a reasonable budget | Han (d17) | single |
| Learned length control by prompt | L1: beats S1 by up to 20 pts absolute; 100-150% relative at 512 and 1,024 tokens. SelfBudgeter: -61% length; 1.5B GSM8K +11.01 pts at 43% length. L1 weak on AIME2025 | b21, c11, c12 | single each |
| Learning when to think | AdaptThink 1.5B: length -53%, accuracy +2.4%. Kassenaar 1.5B: MATH500 0.782 vs 0.796, length -41% | c17, d13 | single each |
| CoT helps mostly on maths and symbolic logic | 100+ papers, 20 datasets, 14 models | Sprague 2024 (c14) | established |
| Deliberation can hurt where humans deliberate badly | o1-preview vs GPT-4o implicit learning -36.3 pts; CoT hurt all 6 VLMs on face recognition; only 3 of 6 predicted effects held | Liu 2025 (c15) | established (partial) |
| Forced self-inspection loses to sampling at equal tokens | Qwen2.5 1.5B/3B/7B: all 18 comparisons negative; Self-Refine -3.6 to -6.3; forced Reflexion -5.5 to -10.1 (7B MATH-500 CI [-15.0, -5.7]) | Mirzaei 2026 (d16) | single preprint |
| Token counts track human time | 1 SD more tokens ~ 1 s more human decision time; N=27,071 posts, 1,854 raters | Davidson 2025 (d18) | single |
| Models spend less on the hardest items | o3-mini token peak near size 100 then falls; no model solved sizes above 100 | Estermann 2025 (d15) | single, one model |
| Underthinking: early thought switching | Wrong answers 225% more tokens, 418% more switches (search summary only) | Wang 2025 (d21) | single, unverified |

## 4. Mechanisms and models

All forms below can be written as short code that lives outside the model. The decider should be program code, not the model (a01).

### 4.1 The base rule

```
for each candidate mode m (direct, short, step-by-step, checked, open) and depth d:
    gain(m, d)  = P_correct(m, d | problem class) * value_of_correct
    cost(m, d)  = price_per_token * expected_tokens(m, d)  (+ latency, + risk)
    EVC(m, d)   = gain - cost
choose argmax EVC
```

Properties from the human data:
- Payoff curve rises with intensity but flattens. Cost curve rises faster at high intensity. The optimum is interior (a03).
- Harder task: lower payoff per unit intensity, so the optimum moves. If effort cannot help, the optimum is zero ("intensity can fall again when a task is too hard", a03).
- Cost is not a flat subtraction. The Westbrook data show larger offers are discounted less (a09). A model with cost as a fraction of value fits better than a fixed price.

### 4.2 Reward and efficacy

Fromer's design separates two arguments of the payoff term (a12):
- reward: how much the outcome is worth;
- efficacy: how much intensity changes the probability of the outcome.

In the rule, efficacy is dP/dd. Zero efficacy gives zero marginal gain, so intensity should drop to the floor whatever the reward. Human data confirm this direction (faster responses with higher efficacy, b values -3.85 to -14.9 ms), but the interaction is unstable (p=.116 / .009 / .027).

### 4.3 Value is recursive

Value(outcome) = reward + gamma x max EVC(next). A deep first step is worth more if it saves effort later (a02). For an agent: spend on S1/S2 (understanding, representation) when it removes cost in S3-S8. No study measured this; it is theory.

### 4.4 Form of control

Control has several knobs, many giving the same reward rate (a19). In a drift-diffusion model: threshold (caution), drift rate (quality of evidence use), non-decision time. Reward raised drift (speed with kept accuracy). Penalty raised threshold (slower, more accurate) (a14). For an agent the knobs are: reasoning length, number of independent samples, verify pass, mode choice. Treat them as separate levers priced separately, with a small regulariser (a19) so the choice is well-posed.

### 4.5 Learned Value of Control (LVOC)

```
features f(problem)              # task type, length, surface cues
w[m]  = running estimate of net value per mode, per feature
choose m = argmax_m  w[m] . f(problem) - cost(m)
after outcome: w[m] += lr * (observed_net_value - w[m] . f) * f      # delta rule
cost(m, c) = omega * t + exp(a * ||c|| + b)     # time cost + convex intensity cost
```
LVOC fits human learning and transfer (a05, a06) but also predicts a failure: if the feature "this looks like past paying problems" is shared by problems where effort does not pay, the agent over-exerts (Bustamante, d14). Guard: log per problem class whether extra thinking changed the answer, and learn from that, not from reward alone.

### 4.6 Shadow-price allocation (Zhai)

```
for each input x, budget grid B = {b1..bk}
choose b(x) = argmax_b  Acc_hat(x, b) - lambda * cost(b)
```
Average cost is monotone in lambda, so one scalar lambda hits any total budget (c08). Acc_hat comes from a small classifier on cheap text features (over 91% imitation of the oracle). Practical point: tune lambda to hit a **realised** mean cost, then compare with a random allocator at the same realised mean (critique correction 1).

### 4.7 Difficulty-routed strategy (Snell, Damani)

```
bin = predicted_difficulty(question)         # from pass rate history or a cheap predictor
policy[bin] = {samples N, search type, max tokens}
```
Beam/search helps hard bins and hurts easy ones; sequential revision helps easy-to-medium (c09). Include the predictor's cost (Snell leaves it out, d09). A predictor with AUROC about 0.85 is the realistic input (d06). Brown shows the crossover: when budgets are generous, a noisy predictor does worse than uniform (d07). Rule: use a fixed default when predicted-difficulty confidence is low.

### 4.8 Stopping rules

- **Agreement stop** (adaptive-consistency, ESC): sample until the majority is stable or a window is unanimous (c18, c19). Training-free.
- **Confidence exit** (DEER): at a transition word, force a trial answer; stop if confident (c20).
- **Knee stop**: per difficulty bin, stop at the budget where marginal accuracy per token falls below lambda (c06, d12).
- **Cap and discard**: on hard sets, chains that do not close by the cap are almost always wrong (11.5% vs 96.5%), so a cap loses little (d12).

### 4.9 Self-priced budget

TALE and SelfBudgeter have the model state a budget first, then reason within it (b19, c12). TALE-EP gave 67% fewer output tokens with under 3% average accuracy loss. Risks: too-small budgets are overrun (token elasticity), and the budget is the model's own estimate (self-pricing, not an external price).

### 4.10 Monitor-Generate-Verify (MGV)

Oh and Gobet write EVOC(b,c) = Q*(b,c) = E[r(b,c) + V*(B_t+1) | b,c] for an LLM agent, adding a Monitor step before generation (c05). It is a design, with no experiments.

## 5. What holds up

**Holds up**
- Demand avoidance with equal pay, in several demand types (Kool 2010; generalisation across experiments, a07, a08). Replicated in the sense that follow-up work uses the paradigm, though Strobel's null was about traits, not the effect.
- Cost rises with load and tracks delay discounting (Westbrook; COG-ED retest r=.80, b08).
- No fuel tank. Hagger (N=2,141, d=0.04) and Vohs (3,531 tested, d=0.06, BF about 4.4 for null) agree; Job-replication also null (b11, d01, d02). Model cost as price or opportunity cost.
- Overthinking on easy items in reasoning models (Chen; LLMThinkBench; Zhou).
- Per-item adaptive allocation beats uniform at equal average cost in several independent papers (K13, six sources), with cost caveats.
- Prompt-level length control exists and is cheap (L1, TALE, SelfBudgeter).
- CoT helps mainly on maths and symbolic logic (Sprague, 100+ papers).

**Failures and contested results**
- Trait link: r=-.38 (N=50) did not replicate at N=217; Juvina also failed (b05, b06). Three effort tasks correlate under .1; DST retest .54 (b07, b08).
- Efficacy x reward interaction: null in Study 1, present in Studies 2 and 3, p=.046 at the EEG level (a12, a13).
- dACC as the seat of EVC: foraging reading refuted by difficulty confound; EVC predicts the same data (a11, b02).
- Ego depletion main effect: null. Small exploratory signals (persistence d=0.15 on the E-task protocol, felt fatigue as only moderator) leave a felt-effort route open (d02). Dang (2016) argued Hagger's task was weak (d03); Vohs used two procedures and found d=0.06, weakening the objection.
- Standard planning task gave no payoff to planning (Kool 2016): a design flaw, not an EVC flaw (a16).

**Moderators seen in opened sources (b24)**
reward size, efficacy, task type, load, age (older adults discount more), depression status (b10: n=31 vs 36, group x efficacy and group x reward interactions on accuracy, small), working memory (r=.185 with discounting, b07), Need for Cognition (weak). Time pressure and training were not covered.

**What worked on LLMs**
- Trained cost reward (RaM): -23 to -45% tokens, accuracy kept (c01).
- Training-free stop rules: ESC, adaptive-consistency, DEER.
- Difficulty-routed policies at low budgets (Damani, Brown, Snell).
- Prompt-stated budgets (TALE).

**What did not work**
- Cost terms that cut accuracy: RaM 8B out of distribution -3.8; Arora 7B AIME -3.3; L1 weak on AIME2025; hard truncation (E1) hurts (c26).
- Format reward alone collapses accuracy (GSM8K 1.64%, c12).
- Adaptive allocation at generous budgets with a noisy predictor (Brown, d07).
- Forced self-critique/reflection at equal tokens (Mirzaei, 18/18 negative, d16).
- Early trace signals add nothing beyond question difficulty (Bulut, d06). The "prefix dominance trap" (~20%) is a forced-prefix result on 10 failed AIME questions per model, not a measured cost of a wrong strategy (d04, d05).

**Cost-matching caveats (apply to all gains)**
- Zhai: "+5.8 points at average budget 3.0" compares learned at realised cost 2.73 with fixed at cost 2.00. Against a random allocator at cost 2.98 (0.534) the gain is about 4.1 points (critique).
- Damani: matched to uniform best-of-k at equal average budget, but needs an oracle verifier, and the chat "tranches" figure (25-40%) is a high-variance subset (d08).
- Snell: "about 4x" ignores difficulty-estimation cost (2,048 samples per problem for oracle bins) and holds at low budgets (d09).
- HAB: MATH500 test set is 78 questions (two questions separate HAB from CoT); a fixed setting reached 95.02% on GSM8K at 172.6 tokens vs HAB 95.24% at 211.1 (d10).
- TALE: abstract and Table 3 disagree (80.22% vs 81.03%) (d17).

## 6. Language models

### 6.1 Has anyone run the human EVC paradigms on LLMs?
No. Zero of about 20 opened sources, plus seven targeted searches (c25, d19, d20). No LLM effort-discounting task (COG-ED style), no demand selection task, no prompt that varies stated reward and stated efficacy and measures allocation by difficulty. LLM work tests the normative rule only through token budgets.

### 6.2 Trained cost-benefit (the machine EVC)
| Method | Result | Source |
|---|---|---|
| RaM (reward = correctness - lambda x length, expert iteration) | 23-45% fewer tokens; Llama-3.1-8B 50.1% at 170.8 tokens vs STaR 47.4% at 222.7; MMLU-CF 8B -3.8 pts | c01, c03 |
| Arora and Zanette (length-penalty RL) | 7B: AIME -16% tokens (-3.3), MATH500 -37% (-2.2), GSM8K -65% (-1.7) | c13 |
| SelfBudgeter | -61% length; 1.5B GSM8K +11.01 at 43% length; MATH500 +3.54 at 44% | c12 |
| L1 | beats S1 by up to 20 pts at 512/1,024 tokens; collapses on AIME2025 | c11 |
| AdaptThink | 1.5B: -53% length, +2.4% accuracy | c17 |
| Kassenaar | 1.5B: MATH500 0.782 vs 0.796, -41% length | d13 |
| Chen self-training | QwQ-32B-Preview -48.6% tokens on MATH500 at same accuracy | b18 |
| TAB (per-turn budgets) | 40% fewer tokens at equal accuracy vs static; agentic up to 20% solver-token savings | d11 |

Pattern: savings are large on easy sets (GSM8K -65% to -83%) and small on hard ones (AIME -16% to -27%), with accuracy loss of 1-4 points typical. All these need training; none is available as a plain scaffold lever.

### 6.3 Training-free allocation
- Adaptive-consistency: up to 7.9x fewer samples, under 0.1% accuracy drop across 17 datasets and 3 LLMs (c18).
- ESC: saved 33.8% of samples on MATH, 80.1% GSM8K, 84.2% Coin Flip (c19).
- DEER: -19.1% to -80.1% length, +0.3 to +5.0% accuracy across 10 benchmarks and 11 models (c20).
- TALE-EP prompt budget: 67% fewer output tokens, accuracy 83.75% to 81.03% (d17).
- Difficulty-routed policies: Snell about 4x gross; Damani up to 50% on code/math (b20, c09).

### 6.4 Overthinking, underthinking, and the shape of the returns curve
- Overthinking on trivial items: 1,953% more tokens on '2+3'; 6,780 vs 378 tokens on basic math; accuracy under a 1,024 cap falls from 72% to 44% (b18, c16).
- Marginal utility of tokens falls, then turns negative: R1-32B AIME peak 55.8% at 12K tokens, 54.9% at 16K; 67.5% of 80 hand-checked negative flips were genuine overthinking (c06).
- Optimum depends on difficulty: easy 1.5K, Level 5 about 8K, GPQA about 10K (c07). Combined indicators predict negative flips at 76.3% precision, 80% recall.
- Bimodal on hard sets: finished chains 96.5% right, unfinished 11.5% (d12).
- Underthinking: more thought switches in wrong answers (summary only, d21). Reduced effort on the hardest puzzles: o3-mini token peak near size 100 (d15). So LLMs misjudge effort payoff in both directions, as humans do (Bustamante, d14).
- Where CoT does not help: non-symbolic tasks (Sprague), implicit learning, face recognition, exceptions (Liu; -36.3 pts for o1-preview vs GPT-4o on implicit learning).

### 6.5 Difficulty estimation (the input every EVC rule needs)
AUROC 0.83-0.88 question-only; 72-84% two-class accuracy; 3-class 66.3% vs 58.7% majority; early signals add nothing beyond difficulty; adaptive worse than uniform above about 96-128 tokens per query with a noisy predictor (d06-d08). The LLM's own first-pass reasoning length correlates with human difficulty (1 SD of tokens ~ 1 s of human time, d18), which suggests a cheap signal, not yet tested for AUROC.

### 6.6 Self-inspection
Forced self-critique does not repay its token cost. Qwen2.5 1.5B-7B, GSM8K and MATH-500, 150 questions each: 18/18 self-inspection comparisons negative; Self-Refine -3.6 to -6.3 points; forced Reflexion -5.5 to -10.1 (d16). Caveat: single author, small models, maths only. This lowers the plausibility of the "effort paradox" for scaffolds (effort having value of its own); K18 stays single-source.

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Evidence ids in parentheses. Schema part: G (guardrail), S (state), O (operator), memory.

### Add now (established)

1. **Allocate thinking by difficulty, not uniformly.** G12 / S0. [E] K13, K20 (c09, b20, c18, c19, c20, d08, d09). Already in G12. Refine the wording: gains are at equal average cost against uniform; nominal-budget gains are upper bounds; difficulty prediction is moderate (AUROC about 0.85), so fall back to a fixed default when confidence is low (K20; d06, d07).
2. **Do not model cost of thinking as a depleting fuel.** G11. [E] K07 (d01, d02, b11). Add no "tokens left" counter that changes behaviour beyond a hard budget, and do not blame accuracy loss on "fatigue" after long context unless length explains it.
3. **Cap re-checks on easy items; first answer is usually right.** G11 / S0. [E] K11 (b18, c10, c16, c22). Log first-answer-equals-final-answer rate per class; stop after the first stable answer on classes where it is high.
4. **Keep an accuracy floor when tightening the token price.** G11. [E] K10 (c03, c13, c26, c12). Always run a hard-bin holdout; cost penalties lost 1.7-3.8 points in several papers and L1 collapsed on AIME2025.
5. **Extra thinking has a knee, then negative returns; locate it per difficulty bin.** G11 stop rule. [E] K12 (c06, c07, c15, d12). Set a stop budget per bin from our own sweep. The value comes from our bench, not from other models' numbers.
6. **Stop-when-agree sampling beats fixed N at equal tokens.** S0 / G11. [E] K13, K17 (c18, c19, c20). Use an agreement stop for sampled attempts; a stated budget in the prompt works as a cheap length dial (b19, b21).
7. **Skip deliberation on non-symbolic tasks.** S0 gate. [E] K15 (c14, c15). Run direct vs short-reason per task class; drop the long path where the gap is near zero.
8. **Put a floor as well as a ceiling.** G11 / G12. [S for the floor, E for the ceiling] K23 (d14, d15, d21, c10). Ceiling on easy items is established; the floor on hard-but-unsolved items is single-source (see "Test first").

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence | Why not yet |
|---|---|---|---|---|
| Prompt-stated token price / reward / efficacy shifts thinking by difficulty at equal tokens | G11/S0 | [S] K03, K25 | d17, d20, a12 | No study tests a price or efficacy frame against a random-length control |
| "Thinking will not help" cue lowers effort without hurting accuracy (efficacy term) | G12 | [S] K03 | a12, a13 | Human only; interaction unstable |
| Cached per-class value of deep vs shallow thinking (LVOC memory) | S0 / memory | [S] K08 | a05, a06, d14 | Fits to published means; over-exertion risk |
| Shadow-price allocation with realised-cost control | S0 | [S] K14 | c08, d07, d08 | Only Zhai has random-allocator control |
| Per-step (within-chain) budget | S0 / O-choice | [S] K21 | d10, d11 | No ablation; HAB test set 78 items |
| Knee-stop vs fixed depth on our agent | G11 | [S] K22 | d12, c06 | Other models only; possible extraction artefacts |
| Cost of a wrong allocation | G11/S0 | [C] K19 | d04, d05, d06 | Not measured anywhere |
| Replace forced self-check with one more independent attempt | G12 / O-verify | [S] K24 | d16 | Small models, maths only |
| Reasoning-length first pass as a difficulty signal | S0 | [S] K26 | d18 | Correlation with human time only |
| Revealed effort-cost curve of the agent (COG-ED style) | G11 | [S] K16 | c25, d19 | Never done on any LLM |
| Reward vs penalty framing changes the lever used | G12/O-choice | [S] K04 | a14 | Human only |
| Human trait scales as agent personality parameters | none | [C] K05 | b05-b09 | Do not use |

## 8. Concrete tests on our bench

Rules for all tests: both arms at equal measured total tokens (report realised mean tokens per arm, not nominal); pre-register item split by difficulty bin (from past pass rate); at least 3 seeds; paired bootstrap CIs; report hardest-bin accuracy separately.

| ID | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Mixed-difficulty items, bins easy/medium/hard (e.g. BrainTeaser plus ARC subsets) | (a) no frame; (b) stated token price; (c) stated reward for correctness; (d) "extra thinking will not change the result"; (e) random-length control matched to (b)'s realised mean | Thinking tokens per bin; slope tokens vs difficulty; accuracy per bin | (b)/(c) raise slope vs (e); (d) lowers tokens on hard bin and loses accuracy; if (b) = (e), the price is just noise |
| T2 | Same items | Knee sweep: budgets x per bin; then knee-stop rule vs fixed depth | Accuracy-vs-tokens per bin, knee with bootstrap CI; accuracy at equal total tokens | Knee near smallest budget on easy; higher on hard; stop rule beats fixed by a few points at equal tokens |
| T3 | Items with a verifier | Difficulty-routed depth vs uniform vs random allocation at the same realised mean | Accuracy at equal realised cost; cost of predictor included | Routed > uniform by 2-5 points at low budgets; vanishes at generous budgets (Brown) |
| T4 | Items where first answer can be compared with final | Cap re-checks after a stable first answer vs always re-check | First=final rate; accuracy; tokens | Same accuracy, fewer tokens on easy classes |
| T5 | Hard-but-unsolved items | Floor on thinking (minimum deep attempt) vs no floor | Accuracy on hardest bin | Floor helps where the agent under-thinks; null means drop the floor |
| T6 | Easy items needing depth vs hard items given shallow budget | Forced wrong allocation (shallow on needs-depth; deep on easy) vs right allocation | Accuracy loss, token waste | Measures cost of a wrong call (K19); expect asymmetric loss |
| T7 | Items with checks | Forced self-verify pass vs one more independent attempt (equal tokens) | Accuracy | Independent attempt >= verify (Mirzaei); if verify wins, keep it |
| T8 | Choice task: offer the agent a depth menu with priced payoffs (COG-ED style) | Fit discount curve across loads and offer sizes; compare 3 prompt wordings | Monotone in load? Amount effect? Retest agreement | Tells whether a cost curve exists at all; no reference result exists |
| T9 | Per-turn tasks with unlike steps | Per-turn budgets vs uniform vs per-problem | Accuracy at equal tokens | Gain only if turns differ clearly in difficulty |
| T10 | Mixed items | First-pass token length as difficulty predictor | AUROC for "needs deep" | Compare with question-only AUROC about 0.85 |

## 9. What does not transfer, and why

- **Brain localisation (dACC, lateral PFC).** Contested and irrelevant to a scaffold (K06). Use EVC as a normative rule only.
- **Trait scales (Need for Cognition, self-control).** Weak and non-replicating links; tasks disagree (K05). Do not give the agent personality parameters. Measure its own revealed preference instead.
- **Ego depletion / fuel.** Null in large replications (K07). The agent has no fuel; its limit is context and a token budget.
- **Millisecond effects.** Reward and efficacy effects of 3-15 ms are not an agent-scale quantity; only the direction transfers.
- **Intrinsic effort cost felt by the agent.** An LLM has no metabolic or opportunity cost. The price is a design choice we set (tokens, latency, money). Opportunity cost exists for the system (the other uses of those tokens), not for the model.
- **Effort paradox (effort valued).** No evidence that extra effort has intrinsic value for LLMs; forced reflection lost to sampling (K18, K24).
- **Learned human cost curves.** Westbrook's dollar prices depend on n-back load and age. No mapping to token cost.
- **Training-based results (RaM, L1, SelfBudgeter, AdaptThink).** Cannot be used by a scaffold directly. Only the direction (short on easy, long on hard) and the failure modes (accuracy floor) carry over.
- **Small-model maths results.** Most LLM numbers are 1.5B-32B open models on GSM8K/MATH/AIME, with 60-462 test items in several cases. Not shown for agentic or open-ended tasks.
- **Standard two-step task.** Planning does not pay there (a16); a lesson for design, not a source of effects.

## 10. Open questions

1. Does a stated price, reward or efficacy in the prompt change allocation by difficulty at equal tokens, against a random-length control? (K03, K25; no study.)
2. Do LLMs show an efficacy effect: does "your thinking will not matter" lower effort and accuracy? (No study; a "learned helplessness" analogy paper only, d20.)
3. What is the knee per difficulty bin for our agent, and does a knee stop beat fixed depth? (Other models: knee at 256 tokens on easy/medium maths, d12.)
4. What is the cost of a wrong allocation or wrong difficulty call? (Not measured; Brown's crossover is the only indirect evidence.)
5. Do effort-discounting choice tasks reveal a cost curve in an LLM? (Never run.)
6. Does within-chain budgeting beat per-problem budgeting at equal tokens? (HAB lacks an ablation; TAB did not compare.)
7. Does a pre-generation activation probe predict difficulty better than text features (AUROC above 0.85)? (Bulut says it might.)
8. Is the reward x efficacy interaction real? (p=.116, .009, .027, .046 in one lab.)
9. Is the effort cost an intrinsic, opportunity or computed cost? Human tasks cannot separate them (b06).
10. Can underthinking numbers (225% more tokens, 418% more switches) be verified in the paper text? (d21 is summary only.)
11. Do results hold outside maths: agentic, open-ended, planning tasks? (TAB gives agentic savings of up to 20% solver tokens, but no EVC-style comparison.)
12. Hagger full text and the last third of Vohs were not read; Inzlicht 2018, Kurzban 2013, Lieder and Griffiths 2017, Musslick 2015, Callaway 2022, Kouneiher 2009, Kolling 2012 were not opened.

## 11. Sources

[V] = opened and read this run; [M] = snippet, summary or recalled only. Evidence ids in brackets.

**Theory and human studies**
- [V] Shenhav, Botvinick, Cohen (2013) The expected value of control. https://pmc.ncbi.nlm.nih.gov/articles/PMC3767969 [a01-a04, b01, b02]. Read to about 100k of 300k characters (b01 note).
- [V] Lieder, Shenhav, Musslick, Griffiths (2018) Rational metareasoning and the plasticity of cognitive control. https://pmc.ncbi.nlm.nih.gov/articles/PMC5937797 [a05, a06]
- [V] Kool, McGuire, Rosen, Botvinick (2010) Decision making and the avoidance of cognitive demand. https://pmc.ncbi.nlm.nih.gov/articles/PMC2970648 [a07, a08, a23]
- [V] Kool, McGuire, Wang, Botvinick (2013) Neural and behavioral evidence for an intrinsic cost of self-control. https://pmc.ncbi.nlm.nih.gov/articles/PMC3754929/ [b06]
- [V] Westbrook, Kester, Braver (2013) What is the subjective cost of cognitive effort? https://pmc.ncbi.nlm.nih.gov/articles/PMC3718823 [a09, a10]; DOI link https://doi.org/10.1371/journal.pone.0068210 [M, b22]
- [V] Shenhav, Straccia, Cohen, Botvinick (2014) Anterior cingulate engagement in a foraging context reflects choice difficulty, not foraging value. https://pmc.ncbi.nlm.nih.gov/articles/PMC4156480 [a11]
- [V] Fromer, Lin, Dean Wolf, Inzlicht, Shenhav (2021) Expectations of reward and efficacy guide cognitive control allocation. https://pmc.ncbi.nlm.nih.gov/articles/PMC7884731 [a12, a13, b03, b04]
- [V] Leng, Yee, Ritz, Shenhav (2021) Dissociable influences of reward and punishment on adaptive cognitive control. https://pmc.ncbi.nlm.nih.gov/articles/PMC8746743 [a14] (Study 1 only)
- [V] Vassena et al. (2014) Overlapping neural systems represent cognitive effort and reward anticipation. https://pmc.ncbi.nlm.nih.gov/articles/PMC3946624 [a15]
- [V] Kool, Gershman, Cushman (2016) When does model-based control pay off? https://pmc.ncbi.nlm.nih.gov/articles/PMC5001643 [a16]
- [V] Kurzban et al. (2013) An opportunity cost model of subjective effort. https://pmc.ncbi.nlm.nih.gov/articles/PMC3856320 [a17]; the b14 record says the page was blocked, so treat as [M].
- [V] Westbrook and Braver (2015) Cognitive effort: a neuroeconomic approach. https://pmc.ncbi.nlm.nih.gov/articles/PMC4445645 [a18]
- [V] Ritz, Leng, Shenhav (2022) Cognitive control as a multivariate optimization problem. https://pmc.ncbi.nlm.nih.gov/articles/PMC8939373 [a19]
- [V] Bustamante et al. (2021) Learning to overexert cognitive control in a Stroop task. https://pmc.ncbi.nlm.nih.gov/articles/PMC8208940/ [d14] (earlier a20 was [M])
- [V] Strobel et al. (2020) Dispositional cognitive effort investment and its relation to demand avoidance. https://pmc.ncbi.nlm.nih.gov/articles/PMC7556472/ [b05]
- [V] Maekela et al. (2023) Is it cognitive effort you measure? https://pmc.ncbi.nlm.nih.gov/articles/PMC10434945/ [b07, b08]
- [V] Dispositional individual differences in cognitive effort investment. https://pmc.ncbi.nlm.nih.gov/articles/PMC7821547/ [b09]
- [V] Depression and EVC (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12010535/ [b10]
- [V] Replication of Job, Dweck, Walton (2010), PLoS One (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10310002/ [b11]
- [V, abstract level] Hagger et al. (2016) multilab ego-depletion replication. https://doi.org/10.1177/1745691616652873 [d01]; b12 was recalled.
- [V, first two thirds] Vohs et al. (2021) multisite ego-depletion test. https://pmc.ncbi.nlm.nih.gov/articles/PMC12422598/ [d02]; b13 was recalled.
- [V] Dang (2016) Commentary on Hagger. https://pmc.ncbi.nlm.nih.gov/articles/PMC4971805/ [d03]
- [M] Inzlicht, Shenhav, Olivola (2018) The effort paradox. https://pmc.ncbi.nlm.nih.gov/articles/PMC6172040/ [b15]
- [M] Kouneiher, Charron, Koechlin (2009). https://doi.org/10.1038/nn.2321 [a21]
- [M] Kolling, Behrens, Mars, Rushworth (2012) Neural mechanisms of foraging. https://doi.org/10.1126/science.1216930 [a22]
- [M] Kolling et al. (2014) record. https://doi.org/10.1038/nn.3771 [b23] (title only; the opened paper on this question is Shenhav 2014, a11)
- [M] Lieder and Griffiths (2017) Strategy selection as rational metareasoning. https://doi.org/10.1037/rev0000075 [a26]
- [M] Musslick, Shenhav, Botvinick, Cohen (2015) [a27] (page not located)
- [M] Callaway et al. (2022) Rational use of cognitive resources in human planning. https://doi.org/10.1038/s41562-022-01332-8 [a28]

**LLM and AI studies**
- [V] De Sabbata et al. (2025) Rational metareasoning for LLMs (RaM). https://arxiv.org/abs/2410.05563 [c01-c04, a24, a25, b16, b17]
- [V] Oh and Gobet (2025) Monitor-Generate-Verify. https://arxiv.org/abs/2511.04341 [c05, d05]. (c24 points to this URL by mistake for Lieder 2018: [M].)
- [V] Zhou et al. (2026) When More Thinking Hurts. https://arxiv.org/abs/2604.10739 [c06, c07]
- [V] Zhai et al. (2026) Adaptive test-time compute allocation. https://arxiv.org/abs/2604.14853 [c08]
- [V] Snell et al. (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314 [c09, d09]
- [V] Chen et al. (2025) Do NOT think that much for 2+3=? https://arxiv.org/abs/2412.21187 [b18, c10]
- [V] Aggarwal and Welleck (2025) L1. https://arxiv.org/abs/2503.04697 [b21, c11]
- [V] Li et al. (2025) SelfBudgeter. https://arxiv.org/abs/2505.11274 [c12, c26]
- [V] Arora and Zanette (2025) Training language models to reason efficiently. https://arxiv.org/abs/2502.04463 [c13]
- [V] Sprague et al. (2024) To CoT or not to CoT. https://arxiv.org/abs/2409.12183 [c14]
- [V] Liu et al. (2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 [c15]
- [V] Srivastava et al. (2025) LLMThinkBench. https://arxiv.org/abs/2507.04023 [c16]
- [V] Zhang et al. (2025) AdaptThink. https://arxiv.org/abs/2505.13417 [c17]
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 [c18]
- [V] Li et al. (2024) Early-stopping self-consistency. https://arxiv.org/abs/2401.10480 [c19]
- [V] Yang et al. (2025) DEER. https://arxiv.org/abs/2504.15895 [c20]
- [V] Zhou et al. (2026) Thinking Economically: HAB. https://arxiv.org/abs/2606.01168 [c21, d10]
- [V] Survey (2025) Reasoning on a Budget. https://arxiv.org/abs/2507.02076 [c22]
- [M] de Varda, Fedorenko et al. (2025) The cost of thinking is similar between large reasoning models and humans. https://news.mit.edu/2025/cost-of-thinking-1119 [c23] (news piece; PNAS doi 10.1073/pnas.2520077122 returned 403)
- [V] Han et al. (2025) TALE. https://arxiv.org/abs/2412.18547 [b19, d17]
- [V] Damani et al. (2024) Learning how hard to think. https://arxiv.org/abs/2410.04707 [b20, d08]
- [V] Luo et al. (2025) Learning from Peers in Reasoning Models (LeaP). https://arxiv.org/abs/2505.07787 [d04]
- [V] Bulut (2026) It's the problem, not the path. https://arxiv.org/abs/2609.03436 [d06]
- [V] Brown, Muppidi, Shahout (2026) Predictive scheduling. https://arxiv.org/abs/2602.01237 [d07]
- [V] Jali, Nayak, Joshi (2026) Not all turns are equally hard (TAB). https://arxiv.org/abs/2604.05164 [d11]
- [V] Oladri, Jawahar, Mohamed (2026) Token budget saturation. https://arxiv.org/abs/2607.21433 [d12]
- [V, abstract and first page] Kassenaar, Yang, Francois-Lavet (2026) Learning when to think. https://arxiv.org/abs/2608.20256 [d13]
- [V] Estermann and Wattenhofer (2025) Reasoning effort and problem complexity. https://arxiv.org/abs/2503.15113 [d15]
- [V] Mirzaei (2026) Sample more, reflect less. https://arxiv.org/abs/2607.28576 [d16]
- [V] Davidson (2025) AI reasoning effort predicts human decision time. https://arxiv.org/abs/2508.20262 [d18]
- [M] Wang et al. (2025) Thoughts are all over the place. https://arxiv.org/abs/2501.18585 [d21] (search summary only)
- Search records, not sources: d19 (https://www.semanticscholar.org/), d20 (https://arxiv.org/).

Caveat on newer preprints: Mirzaei, Bulut, Oladri, Jali, Kassenaar are 2026 preprints from small teams, not peer reviewed.

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 10 established claims: 8 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **B02.06-K02** (reworded: the sources support less). Payoff-minus-cost (EVC) is Shenhav et al.'s theoretical proposal, not a rule shown by the data; Westbrook's results are consistent with it, and the delay-discounting link is modest (R2=0.14, n=33). Corrected claim: Effort-based choice is consistent with a payoff-minus-cost account (EVC theory): in Westbrook et al. 2013 people trade money against n-back load, discounting rises with load, larger offers are discounted less, and effort discounting correlates modestly with delay discounting (B=0.30, P=0.03, R2=0.14, n=33).
- **B02.06-K12** (now single-source: the sources are not independent). The R1-32B AIME numbers (55.8 at 12K, 54.9 at 16K; difficulty optima 1.5K and 8K) all come from one arXiv preprint (Zhou 2026, 60 AIME problems, v1) listed twice (c06, c07); the other listed papers (Liu, Sprague) concern chain-of-thought hurting, not token-budget curves.
