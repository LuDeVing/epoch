# Uncertain evidence: deep document

*Subfield D02.04. Sources: evidence_a-d.jsonl (ids a01-a25, b01-b30, c01-c18, d01-d16), claims.jsonl (K01-K23), critique.md. Ids below refer to those files. Where critique.md corrected an evidence line, the corrected number is used here.*

## 1. What it is

Uncertain evidence means evidence that does not arrive as a clean fact. You do not learn "the output passed". You learn "the output probably passed", or "a checker with a known hit rate said pass". The question is how a reasoner should change its credences when the input itself is soft.

Our agent meets this at S4 (TEST). A noisy check should shift credence in a candidate. It should not set it to 0 or 1. Three questions follow.

1. How is the shift stated: as a new posterior, or as the strength of the evidence?
2. How are several shifts combined, and does the order matter?
3. Do language models do this well on their own, or must code do it?

Two formal answers exist.

- **Jeffrey conditionalization** (Jeffrey 1965). You state the new probability of each cell of a partition. The new credence in any claim A is the sum over cells of P(A | cell) times the new cell probability. It needs rigidity: the conditionals P(A | cell) must not change.
- **Pearl virtual evidence** (Pearl 1988). You state a likelihood ratio (a Bayes factor) for the observation, as if a dummy child node had been observed. The shift then depends on the old prior.

They agree on hard evidence and differ in between. No study says which is better for an agent (K17, contested).

Facts that matter most for the agent:

- Jeffrey and Pearl give different numbers for the same words (12% vs 3% in one worked case).
- Successive Jeffrey updates do not commute. Bayes-factor updates do.
- LLMs updating in text are poor Bayesians on hard evidence already. No study tests true soft evidence on LLMs.
- LLMs both over-react (to pushback) and under-react (to logical undercutters). Updates must be graded and computed by code.
- Repeated checks from one model are not independent.

## 2. History and theories in depth

**Jeffrey (1965), The Logic of Decision.** Founding example: you see a cloth by candlelight and are unsure whether it is green, blue or violet. Experience shifts your credence over colour, but you cannot name a proposition that you learned for certain. Rule: P_new(A) = sum_i P(A | E_i) P_new(E_i). Ordinary conditioning is the case P_new(E_j) = 1. Condition: rigidity, the P(A | E_i) stay fixed. (a12, c15; both [M], outline confirmed through a01, a03, a06.)

**Diaconis and Zabell (1982).** Show Jeffrey updating is the minimum-distance update under the shifted-cell constraint, and that successive Jeffrey updates depend on order. (a13, b30, c18; all [M]; theorems not verified at source.) Munk et al. (a04) give the same KL-closest result and credit Peng et al. 2010.

**Field (1978) and Skyrms (1987).** Field restated the Jeffrey input as a Bayes factor to fix order dependence. Skyrms gave a diachronic Dutch-book argument for Jeffrey conditioning under rigidity. (a24, [M].) Field and Wagner define "same learning" as same Bayes factor, not same posterior (b01, [V] through the 2021 paper).

**Pearl (1988, 1990).** Virtual evidence: add a child node with a likelihood ratio to model an unreliable observation. Pearl argued the strength should be set by the reliability of the source, not by the final posterior. (c16, a25, [M].)

**Chan and Darwiche (2005).** Jeffrey fixes the posterior on the evidence; virtual evidence fixes the likelihood ratio. One can be converted into the other. (a14, c17, [M]; the quoted sentence comes from Jacobs, which was read.)

**Smets (1993) and Wagner (1992).** Generalise Jeffrey to belief functions and to lower probabilities. Jeffrey needs two things: new weights on a partition (R1) and unchanged ratios inside each cell (R2). Bayes is the limit where one cell gets probability 1. Different generalisations give different answers; no empirical test. (a06, a07, [V].)

**Hawthorne (2004), Trpin (2019).** Sequences of Jeffrey updates depend on order; Jeffrey sequences can reach confident false beliefs after uncertain but non-misleading observations. (b28, b29, [M], snippets only.)

**Huber (2008), reply to Crupi et al.** Under Jeffrey updating, whether E confirms H depends on the earlier prior. The same E can confirm, disconfirm or be neutral for H, for suitable priors. Crupi et al. show confirmation grows with Pr(E) when Pr0(H) < Pr0(H | E). (b04, [V]; 3-page reply.)

**Jacobs (2019), Jacobs and Stein (2023).** The clearest modern comparison. Jeffrey treats soft evidence as a new state of affairs (a convex mix of point updates). Pearl treats it as a likelihood. They agree at strength 0 and 1. Pearl raises expected validity; Jeffrey lowers KL divergence (a variational view). The authors say they cannot decide which is "right". (a01, a02, a05, [V].)

**Dziurosz-Serafinowicz and Dziurosz-Serafinowicz (2021).** Free uncertain evidence has non-negative expected value under stated conditions, extended to Pearl-style sets of likelihood ratios. They argue a ratio input is better than a Jeffrey input because a ratio does not depend on the prior; a Jeffrey shift bakes the old prior in. (b01-b03, [V].)

**Munk, Mead, Wood (2023).** Compare Jeffrey, Pearl and Tolpin's distributional evidence in simulation. The reading of the uncertainty is a modelling choice and the posteriors differ. (a03, [V].)

**Human data.** Phillips and Edwards (1966) and Edwards (1968): the bookbag-and-poker-chip task, where people update in the right direction but too little (conservatism). (a23, b27, [M].) Zhao and Osherson (2010) tested invariance with uncertain evidence and report rough conformity to Jeffrey's principle (b05, abstract page [V]; full paper closed, d14). Hadjichristidis, Sloman and Over (2014) and Over and Hadjichristidis (2009) say Jeffrey's rule does not fully describe induction from uncertain premises (a10, a11, d15, [M], title or snippet only). No N or effect size from any of these can be cited.

**Bayesian view of LLM in-context learning.** Xie et al. (2022): ICL as implicit inference over a latent concept, in a synthetic setting (b24, [V]). Arora et al. (2025): Bayesian scaling laws (c08, [V]). Falck et al. (2024) contradict the Bayesian claim with a martingale test (b11-b13, [V]). Section 6 covers these.

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. Status follows claims.jsonl.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Jeffrey and Pearl give different posteriors for the same stated uncertainty | Disease test: prior 1%, sensitivity 90%, false-positive rate 5%. Pr(d given pos) = 15%, Pr(d given neg) = 0.1%. With 80% certainty of a positive: Jeffrey about 12%, Pearl about 3% (148 of 4702 in the paper's count) | Jacobs 2019 (a01); Munk 2023 (a03) | E (K01) |
| Successive Jeffrey updates do not commute; Pearl updates do | Proposition 5.3 (Jeffrey), Proposition 4.3(3) (Pearl commutativity) | Jacobs 2019 (a02); Dziurosz-Serafinowicz 2021 (b01) | E (K02) |
| Repeated tests give wildly different results depending on how repeats are modelled | Prevalence 5%, sens 90%, spec 95%, results pos, pos, neg: 64%, 9%, 33% from three WebPPL programs. With 3000 tests (2000 pos, 1000 neg) program 1 goes to about 100%, the others stay put. The 64% was not re-checked this session | Jacobs and Stein 2023 (a05) | E (K04) |
| Jeffrey valid only under rigidity; readings differ in simulation | Ball drop: x = 1 m, timing error 0.03 s, observed 0.43 s vs ideal 0.45 s; Kepler-90: 7 transits, 20 min measurement error, 10 min model error | Munk 2023 (a03); Smets 1993 (a07); Wagner 1992 (a06) | E (K03) |
| Whether E confirms H depends on the prior | Same E can confirm, disconfirm or be neutral | Huber 2008 (b04) | S (K15) |
| Free uncertain evidence has non-negative expected value | Worked example: likelihood ratios 2 for B vs 1 for not-B | Dziurosz-Serafinowicz 2021 (b02) | S (K15) |
| Soft labels improve calibration in Jeffrey-style nets | CIFAR-10H, 10,000 images, accuracy about 46-47.5%; calibration gains "upwards of 20%" in some cases | Yu 2021 (a08) | E (K16), small image models |
| Non-reasoning LLM updating on evidence in context is far from the oracle | Final success cut by at least 30% vs oracle across models; near 0% for weaker models on 20 Questions. Gemma-4-31B-it with reasoning matches the oracle on ProteinWorld-simple; Gemini-2.5-Pro reasoning-only put 85% mass on a hypothesis with true posterior 0.261 (ProteinWorld-hard, no tools, uniform prior) | Filbry et al. 2026 (a16) | E (K05) |
| Probabilities elicited in separate chats are incoherent; inside one dialogue mostly coherent | Violations over 50% of 30 scenarios across chats for almost all model-constraint pairs; within a dialogue 10% for Gemini and 1 of 30 for Gemma | Filbry 2026 (a17) | S (K13) |
| Prompting tricks do not fix weak updating | CoT, numeric encodings, 30 rounds and base models all failed. 624 simulated users, 5 rounds; some original variants score about 37-41% in the final round vs Bayesian Assistant about 80% | Qiu et al. (b06, b07, c07) | E (K05) |
| Fine-tuning on a Bayesian Assistant works; teaching on imperfect Bayesian guesses beats teaching on a perfect oracle | Agreement with the assistant about 80%. A 40% random-noise control barely beat the original model. 48 human-annotated users (15 raters each, 720 participants); human round 1 to 5 gain p = 0.002 | Qiu et al. (b08-b10) | E (K16) |
| LLMs start with biased priors, then update roughly Bayesian | Zero-shot 60-80% on a favoured coin outcome; Llama3.1-8B plotted against posterior mean 0.88 | Gupta et al. 2025 (a20, c01) | E (K06) |
| A discounted filter fits LLM updating better than plain Bayes | Fitted gamma 0.88 (Llama-3.1-8B, biased die); T = 100 observations, changepoint at t = 51; update error typically under 13% of total error; correlation of attention to past evidence with fit about -0.85 | Zhang et al. 2025 (c02) | E (K06) |
| In-context learning violates the martingale property | Bernoulli n = 50, means 0.3/0.5/0.7, paths m = n/2 and 2n; short paths mostly fine, long paths deviate; GPT-4 deviates even on short paths for some means | Falck et al. 2024 (b11-b13) | E (K06) |
| Elicited probability revisions fit a tempered Bayes update with exponent alpha | log q_post = alpha(log q_pre + log b) + c. Alpha: baseline 1.03, verifier-conditioned 1.11, retrieval-augmented 1.18, aggressive evidence scaling 1.26. 4,975 problems, mean R2 about 0.76. Higher alpha went with higher ECE/Brier | Farmer et al. 2026 (c05) | S (K09) |
| Pushback flips correct answers | "Are you sure?": accuracy down by up to 27% (Claude 1.3). First answer changed 32% (GPT-4) to 86% (Claude 1.3); admit mistake 42% to 98%. A separate 27% case is LLaMA 2 when a user suggests a wrong answer | Sharma et al. 2024 (b21-b23) | E (K07) |
| Larger and reasoning models resist pushback | Debate Turn-of-Flip out of 5: Qwen2.5-72B 4.90, Llama-3.3-70B 4.85, DeepSeek-r1 4.85, DeepSeek-v3 4.16, Qwen2.5-7B 0.83. Third-person framing cuts sycophancy by up to 63.8% | Hong et al. 2026 (d09) | E (K22) |
| Framing of the challenge changes flips | Casual "Sure Rebuttal" persuades 84.5% vs 56.1% for a full formal rebuttal; Llama-3.3-70B 93.9% under "Are you sure". Neutral side-by-side judging: +24.6% net gain | Kim and Khashabi 2025 (d10) | E (K22) |
| Models under-update on logical undercutters | Belief-R (update/maintain/BREU): Llama-3 70B 10.99/92.09/51.54; GPT-4 Turbo 19.65/82.69/51.17; Mixtral 8x22B 35.38/36.57/35.98; Command R+ (PS) 44.04/53.13/48.59. 30 LMs; best about 50% BREU. CoT and PS did not help (PS about +1%) | Wilie et al. 2024 (b14-b16) | E (K08) |
| Bayesian error rises with sycophantic over-updating | Evidence quality check on 100 examples: 77% (FortuneDial), 92% (Moral Stories) high quality. Calibrating the prior alone raised Bayesian error; prior plus posterior scaling cut it | Atwell et al. 2026, BASIL (c03) | S |
| BayesBench: larger models can over-react to skewed coin evidence | Seven models 3B-70B (LLaMA 3B/8B/70B, Qwen 3B/7B/14B/32B). Scaling helps latent inference, not downstream prediction. Not a general result for all seven (critique correction) | Samanta et al. 2026 (a18) | S |
| Models do not treat evidence normatively | Contradictory evidence acts like golden; irrelevant evidence lowers confidence. Models accept coherent counter-evidence but show confirmation bias and herd on evidence count; order effects over 5% (over 30% for PaLM2, Llama2-7B); GPT-4 80% memorisation ratio | Kim et al. 2025 (c06); Xie et al. 2024 (c10); Wan et al. 2024 (c09) | E (K10) |
| Verbal confidence is a weak signal | GPT-4 AUROC 62.7%; weaker models ECE above 0.377; GSM8K AUROC 54.8% to 92.7% with 5-sample consistency; GPT-4 at 93.6% accuracy ECE 0.064; AUROC gap 0.522 vs 0.605. Verbalised beats token probabilities, relative ECE cut about 50% | Xiong et al. 2024 (b17-b19); Tian et al. 2023 (b20, c13) | E (K11) |
| Actions depart from stated confidence | Models bet against their own high confidence in a prediction-market task | Pal et al. 2026 (c04) | E (K11) |
| Hedge words map to numbers for strong LLMs, with a belief-dependent shift | 10 LLMs vs 94 humans, 14 hedges x 60 statements; 85% or better agreement with human mode for GPT-4, Llama3-70B, Gemini; 7 of 10 beat an individual human; mean 7.0 points lower for false statements, up to 49.5 for "possible" | Belem et al. 2024 (d01) | S (K18) |
| Old small models do not know hedges | Zero-shot RoBERTa about 50/50/46 (chance 50); humans 97.0/93.5/89.5 | Sileo and Moens 2023 (d02) | S |
| Written hedges are unfaithful to model uncertainty | Best faithfulness about 0.63 (GPT-4), 0.7 (Gemini Ultra) | Yona et al. 2024 (d03) | S |
| LLM supplies factors, code combines | BIRD: F1 59% for agreement with humans, over 30% above GPT-4; factor sampling +4.4%/+3.9% (Llama-2/Llama-3.1); human preference for BIRD questions 52.8% vs 32.8% (14.4% equal). BLInD: 100% at 2 variables falling to 73% at 9 in weaker setups; 900 test items | Feng et al. 2025 (b25, b26); Nafar et al. 2024 (a21) | E (K12) |
| Retrieval forecaster aggregating soft evidence nears the crowd | Brier: random 0.250, crowd 0.149, zero-shot GPT-4-1106 0.208 (SE 0.006); test set 914 questions (3,762 is the train set, 5,516 total) | Halawi et al. 2024 (c11) | E (K12) |
| Self-check reports are asymmetric | GPT-4 as own verifier: false negative rate 95.8% (113/118) and 97.09% (100/103) in two domains; 20.7% and 15.48% in the others; false positive 0.5% (2/397) to 18.55% (64/345) | Stechly et al. 2024 (d06) | E (K19) |
| Self-review without outside signal does not help | GPT-3.5 GSM8K keeps first answer 74.7%; changes are more often correct to incorrect. With oracle labels GPT-3.5 GSM8K 75.9 to 84.3. Sound-verifier backprompting 16% to about 40%; a bare "try again" nearly as good | Huang et al. 2024 (d08); Stechly et al. 2023 (d07) | E (K19, K22) |
| Errors are shared across models | When both wrong, same wrong answer 42.3% (HuggingFace, 12,032 questions) and 60% (HELM, 14,042); up to 0.97 within one provider; random would be about one third | Kim et al. 2025 (d04) | E (K20) |
| Weighted verifier combination beats equal weights | Supervised +11.2 points (about 50,000 labelled pairs); top-K +3.6, learned weights +7.8; Weaver (5-10 labelled queries) +17.1% vs unweighted, +13.5% vs majority | Saad-Falcon et al. 2025 (d05) | E (K20) |
| Same-source repeats hit a ceiling | MATH, Llama-3-8B-Instruct: coverage 82.9% at 100 samples to 98.44% at 10,000; majority vote or reward-model selection only 40.50% to 41.41% | Brown et al. 2024 (d13) | E (K20) |
| Reasoning models are still overconfident | Confidence above 85% on wrong answers; more depth: GPQA +10.8% accuracy and -5.5% ECE, but on items wrong at every depth ECE and MCE rise; reasoning training lowers "I don't know" rate | Mei et al. 2025 (d11); Zeng et al. 2025 (d12) | E (K21) |
| Human Jeffrey conformity is rough | Rough conformity; no N, no effect size | Zhao and Osherson 2010 (b05, d14) | C (K14) |

## 4. Mechanisms and models

### 4.1 Two ways to encode "this check is noisy"

Let H be the candidate (right or wrong). Let E be the check outcome.

**Pearl / Bayes factor (use this).** State the evidence as a likelihood ratio.

- Posterior odds = prior odds x BF.
- For a pass: BF_pass = P(pass | right) / P(pass | wrong).
- For a fail: BF_fail = P(fail | right) / P(fail | wrong).
- Log form: logit_post = logit_prior + log BF. Log-odds add, so any order gives the same result (commutes).
- A soft report ("80% sure it passed") is a virtual-evidence input: a mix of the pass and fail likelihoods, then one update.

**Jeffrey.** State q = new probability that the check passed.

- P_new(H) = q x P(H | pass) + (1 - q) x P(H | fail).
- It needs P(H | pass) and P(H | fail) to stay fixed (rigidity).
- Worked example: P(H | pass) = 15%, P(H | fail) = 0.1%, q = 0.8 gives 0.8 x 15 + 0.2 x 0.1 = 12.02%. The Pearl reading with the same 80% gives about 3% (a01).

The difference: Jeffrey treats the 80% as your all-things-considered credence that the test was positive. Pearl treats it as the reliability of a signal, which is then combined with the prior. If the 80% already includes the prior, use Jeffrey. If it describes the check alone, use Pearl. A check's hit rate describes the check alone. So the Bayes-factor form is the natural one for the agent. This is a design argument (b03), not an empirical result (K17).

Conversion (Chan and Darwiche, [M]): any Jeffrey shift can be rewritten as a Bayes factor given the prior. Log the factor, not the posterior.

### 4.2 Ledger algorithm for S4

1. Code holds a ledger per candidate: prior log-odds, then a list of entries (check id, source family, outcome, BF).
2. Each check type has a table: P(pass | right), P(pass | wrong), measured on a labelled set. Pass and fail get separate BFs (a self-check "fail" can be almost uninformative, d06).
3. The model only reports the typed outcome and counts (for example "3 of 4 held-out cases passed"). It does not write a probability.
4. Code computes log-odds = prior + sum(log BF x w_source), where w_source is the correlation discount.
5. Code maps log-odds to credence and normalises across mutually exclusive candidates (G5).
6. Credence never reaches 0 or 1 from a noisy check. Clip to [eps, 1 - eps].

### 4.3 Correlation discount

Same-family checks share errors (d04, d13). Simple rule: group checks by model family. Within a group, count the strongest entry fully and add a fraction of the others (start with 0, then test 0.25 and 0.5). This is a design proposal; the right discount is unmeasured. Weaver (d05) shows learned weights from 5-10 labelled queries work for selection, and notes its own independence assumption is violated.

### 4.4 Rigidity check

Jeffrey and virtual evidence both assume the check does not change how H relates to its consequences. Test: split the check outcome by sub-cases. If the check is informative only inside one sub-hypothesis (the Kepler case in a03, where only orbital period P differs), a single BF is wrong. Implementation: for each check, record outcome per sub-case of the test inputs; if pass rates differ across sub-cases by more than a threshold, split the BF per sub-case. No agent study exists (K23).

### 4.5 Tempered update (alpha)

Farmer et al. (c05) fit log q_post = alpha(log q_pre + log b) + c. Alpha above 1 means the model over-weights evidence. Use it as a diagnostic: fit alpha on the agent's own credence log. If credence is code-computed, alpha is 1 by design, and the open issue is whether the BFs themselves are calibrated. Capping or shrinking alpha toward 1 is a candidate test (K09, single source).

### 4.6 Discounted filter

Zhang et al. (c02): belief at time t is a filter that forgets old evidence by factor gamma (fitted 0.88). In an agent this means early checks in a long chain lose weight if the model holds the ledger. A code-held ledger avoids it.

### 4.7 Change-gate

A rule in code: credence may change only when a new tool result arrived this step. It blocks pushback flips (b21-b23) and self-review flips (d08). It may raise under-update (Belief-R, b14). Graded BF updates when new premises arrive give the middle path.

### 4.8 Hedge decoding

If the model must write a hedge, decode it with a fixed table in code or a fresh call that cannot see the candidate. The model's number shifts with its belief in the claim (d01), so asking in the same context as the candidate leaks belief into the weight.

## 5. What holds up

**Holds up (two or more independent sources):**

- Jeffrey and Pearl differ off the endpoints; Jeffrey sequences do not commute (a01, a02, a05, b01, a03; K01, K02).
- Jeffrey needs rigidity; readings of soft evidence give different posteriors (a03, a06, a07, b05; K03).
- LLMs without code update poorly even on hard evidence; prompting tricks do not fix it (a16, b06, b07, b16; K05).
- LLM updating is roughly Bayesian only in the simplest cases; priors and forgetting explain most gaps (a20, c02, b11-b13; K06).
- Both over-reaction to pushback and under-reaction to undercutters occur (b21, b14, a18, c03; K07, K08).
- Self-checks and self-review give little without an outside signal (d06, d07, d08).
- Errors and repeated checks are correlated (d04, d05, d13).
- Verbal confidence is weak; sample agreement is better but not independent (b17-b19, c04).
- An LLM-proposes, code-combines pipeline beats direct LLM probability (b25, a21, c11).

**Moderators:**

- Model size: large and reasoning models resist pushback much more (d09: 4.85-4.90 of 5 vs 0.83). Small models over-update (a18).
- Framing of the challenge: follow-up turn vs neutral side-by-side judging, casual vs formal rebuttal (d10).
- Source of the evidence: social pushback leads to over-reaction; a logical undercutter leads to under-reaction; evidence streams lead to alpha above 1 and discounting.
- Task: simple binary coin tasks look Bayesian (Gupta); structured tasks with likelihoods to build do not (Filbry, Qiu).
- Same dialogue vs separate chats for probability elicitation (a17).
- Evidence placement: evidence shown beside the claim is not discounted when contradictory (c06); evidence conflicting with memory is accepted when coherent (c10). Not a true conflict.

**Failures and weak spots:**

- Prompting: CoT, plan-and-solve, numeric encodings, more rounds, base models (b07, b16).
- Self-review (d08). Sound-verifier feedback content added little over "try again" (d07).
- Model-stated confidence as a stop signal (b17).
- No LLM study tests true soft (Jeffrey-style) evidence. Nearly all use hard observations.
- Human Jeffrey studies are unread beyond abstracts. "People roughly follow Jeffrey" is contested (K14).
- Several 2026 preprints (Filbry, Samanta, Farmer, Atwell) are single-source and not peer reviewed.
- Dynamics papers use small open models (2B-8B).

**Interventions that worked:** code-side combination (b25); fine-tuning on Bayesian Assistant outputs (b09, but we cannot train); weighted verifier ensembles (d05); neutral re-judging (d10, +24.6%); third-person framing in debate (d09, up to 63.8% less sycophancy); single-dialogue elicitation (a17); calibrating both prior and posterior scaling (c03).

**Did not work:** CoT/PS (b16), forced self-review (d08), the random-noise teacher control (b10), more samples from one source past about 100 (d13).

## 6. Language models

**On hard evidence, no code.** Final success falls at least 30% below the oracle across models; weak models reach near 0% on 20 Questions (a16). Off-the-shelf models plateau after round 1 in five-round preference tasks (b06). Humans also fall short, but improved from round 1 to 5 (p = 0.002, 48 users, b08). The errors are mostly numerical slips, not wrong likelihoods: models rebuild likelihoods and Bayes' rule correctly (a16). This points to code doing the arithmetic.

**With reasoning and code.** Gemma-4-31B-it matches the oracle on ProteinWorld-simple. A reasoning-only Gemini-2.5-Pro trace still put 85% mass on a hypothesis with true posterior 0.261 on the hard task (a16, critique correction). The line "with reasoning and code, close to oracle" is only partly checked.

**Are LLMs Bayesian?** Partly.

- For (simple binary data): evidence outweighs bias instructions; updates broadly Bayesian; deviations come from priors of 60-80% on a coin (a20, c01). Bayesian scaling laws fit ICL (c08).
- Against: martingale violated and order sensitive (b11-b13). A discounted filter fits better than plain Bayes, gamma 0.88 (c02).
- Resolution: it depends on the task. "LLMs are Bayesian" is supportable only for the simple case (critique).

**Over-reaction.** User pushback flips correct answers: accuracy down by up to 27% after "Are you sure?" (Claude 1.3); first answers changed 32-86% (b21, b22); swaying occurs even after high stated confidence (b23). Larger models can over-update on skewed coin evidence (a18). Alpha above 1 on verifier-style evidence, with higher calibration error (c05). The effect fades in newer, larger, reasoning-tuned models in debate (d09), but follow-up framing and detailed rebuttals still raise flips (d10).

**Under-reaction.** Belief-R: strong models update in only 10-20% of cases that need it while maintaining 82-92% when no update is needed. Models that update more fail to maintain (b14, b15). Direction depends on the source type.

**Evidence handling.** Contradictory evidence is treated like golden; irrelevant evidence lowers confidence (c06). Models herd on evidence count and show order effects over 5%, over 30% for some models (c10). Relevance to the query drives which document wins, not style cues (c09).

**Confidence and hedges.** Verbalised confidence is weak but better than token probabilities for RLHF models (b17, b20). Reasoning models state over 85% on wrong answers and grow more confident with depth on items they keep missing (d11). Hedge-to-number mapping is good in strong models and shifts by 7.0 points with the model's belief (d01).

**Coherence.** Separate chats: over 50% violation. One dialogue: 10% (Gemini) and 1 of 30 (Gemma) (a17).

**What changed it, by how much.**

| Change | Effect | Source |
|---|---|---|
| Code combines LLM-proposed factors | over 30% better than direct estimate | b25 |
| Fine-tune on Bayesian Assistant | about 80% agreement with assistant | b09 (not usable by us) |
| Weighted verifier ensemble | +11.2 points supervised; +13.5 to +17.1 Weaver | d05 |
| Neutral side-by-side judging | +24.6% net | d10 |
| Third-person framing | up to -63.8% sycophancy | d09 |
| Sample consistency for confidence | AUROC 54.8% to 92.7% on GSM8K | b18 |
| Prior and posterior calibration | significant Bayesian error cut | c03 |
| CoT, PS, more rounds | no help | b07, b16 |

**Gap.** No LLM study measures coded Bayes-factor multiplication against model-restated credence at equal tokens, rigidity checks in agent runs, or Jeffrey vs Pearl by final accuracy (K23). Search was blocked, so this is weak evidence of absence.

## 7. What our agent should take

Schema parts: G (guardrail), S (state), O (operator), memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Log every noisy check as a likelihood ratio, never as a stated posterior.** Code multiplies. S4, G5. [E] K01, K02. Ids a01, a02, a05, b01, b03, c17.
2. **Never let a noisy check set credence to 0 or 1.** Clip. Pass and fail shifts are graded. S4. [E] K01, K08. Ids a01, b14, b15.
3. **Set separate Bayes factors for pass and for fail,** measured as P(pass | right) and P(pass | wrong) on a labelled set per check type. S4. [E] K19. Ids d06, d07, d08.
4. **Count same-family checks as one source** (full discount to start). G4. [E] K04, K20. Ids a05, d04, d05, d13. Direction is established; the size of the discount is not.
5. **The model reports typed outcomes and counts; code computes credence.** Do not ask the model to compute a posterior in text. G5, S4. [E] K05, K12. Ids a16, b06, b07, b25, a21, c11.
6. **Do not use stated verbal confidence as a check weight or a stop signal.** G4, S4. [E] K11. Ids b17-b19, c04, d11. (Already in section 4b of SCHEMA.md.)
7. **Do not let the model review its own answer without an outside signal.** G2. [E] K22. Ids d07, d08. (Matches section 4b.)
8. **Keep the ledger and the normalisation over exclusive candidates in code, not in the model's context.** G5, memory. [E] K06. Ids b11-b13, c02, a20. (Early evidence is forgotten when the model holds the ledger.)
9. **Do not feed irrelevant or contradictory material into a check weight as if it were support.** S1/S4. [E] K10. Ids c06, c10, c09. The filter itself is untested; the danger is established.

### Test first

| Item | Part | Status | Ids |
|---|---|---|---|
| Code-multiplied BF vs model-restated credence at equal tokens | S4/G5 | [E] direction, no direct arm | K05, K23; a16, d16 |
| Jeffrey vs Pearl convention by final accuracy and Brier | S4 | [C] | K17, K01; a01, a03, a14 |
| Correlation discount size (0, 0.25, 0.5, full) for same-model checks | G4 | [E] direction, size unknown | K20, K04; d04, d13 |
| Cap or shrink alpha toward 1 on verifier evidence | S4/G5 | [S] | K09; c05 |
| Rigidity check on checks informative in only one sub-case | S4/G3 | [S] as an agent step (theory [E]) | K03; a03, a06 |
| Credence moves only on new tool output | G2/S4 | [S] gate; pushback half [E] | K22, K07, K08; d09, d10, b14 |
| Fixed hedge-to-number table in code | S4/G5 | [S] | K18; d01, d03 |
| One thread vs fresh calls for elicited likelihoods | G5/memory | [S] | K13; a17 |
| Graded check score vs pass/fail in the ledger | S4 | [S] for agents ([E] for image nets) | K16; a08, b09 |
| Priors set by code (base rate) vs model-stated priors | memory/S0 | [E] diagnosis, fix untested | K06; a20, c01 |
| Run cheap noisy checks vs skip, at equal tokens | S4 | [S] | K15; b02, b04 |
| Neutral re-judging in place of continuing the chat after a challenge | G5/G2 | [S] | K22; d10 |

## 8. Concrete tests on our bench

All arms use equal tokens, including setup cost (G7).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Code BF vs restated credence | Checkable items with known answers, 3-5 noisy checks per candidate | A: model writes new credence in text. B: model reports outcome, code multiplies BFs | Brier and credence error vs the oracle posterior; final accuracy | B lower Brier; Filbry shows at least 30% loss for A vs oracle |
| T2 Jeffrey vs Pearl | Same check logs on items with known answers | A: posterior-stated shifts (Jeffrey). B: BF-stated (Pearl) | Brier; final accuracy | B better or equal, with zero order variance |
| T3 Order invariance | Permute 3-5 checks on one candidate | A: posterior-stated. B: ratio-stated | Variance of final credence across permutations | B zero; A positive (a02) |
| T4 Correlation discount | k = 1, 3, 5 repeated checks from the same model on known-wrong candidates, plus one different-family check | Discount 0, 0.25, 0.5, full | False-confirmation rate; Brier | Discount lowers false confirmation (d04, d13) |
| T5 Pass/fail asymmetry | Labelled check outputs | A: one symmetric accuracy. B: separate BF_pass and BF_fail | Brier; log-loss | B better where fail is near-uninformative (d06) |
| T6 Alpha cap | Credence log from verifier checks | A: free update. B: alpha shrunk to 1 or capped | ECE and Brier | B lower ECE if alpha above 1 holds for our agent (c05) |
| T7 Change-gate | Correct answers followed by a no-information objection; plus mixed undercutting and irrelevant new premises | A: ungated. B: credence changes only on new tool output | Flip rate on correct items; wrong flips; under-update rate (Belief-R style) | B fewer wrong flips; watch that under-update does not rise |
| T8 Rigidity | Planted checks informative only under one sub-hypothesis | A: plain update. B: rigidity step splits the BF | Final accuracy; Brier on planted items | B catches planted violations; false-alarm rate on normal checks stays low |
| T9 Hedge table | Check reports written with hedges on true and false candidates | A: model's own number. B: fixed table in code or blind fresh call | True-vs-false shift in decoded number; Brier | B shift near 0 (d01 reports 7.0 points) |
| T10 One thread vs fresh | Elicited likelihoods for 30 scenarios | A: fresh calls. B: one thread | Dutch-book and sum-to-one violations | B much lower (a17: over 50% vs 10%) |
| T11 Graded vs binary ledger | Checks with a score from 0 to 1 | A: pass/fail. B: graded | Calibration (ECE) | B better (a08, b09) |
| T12 Cheap noisy check value | Items where a cheap check costs tokens | A: run the check. B: skip it, spend tokens on another attempt | Accuracy at equal tokens | A wins if the BF is above a threshold (b02) |

## 9. What does not transfer, and why

- **Fine-tuning on a Bayesian Assistant (b09, c07).** Works, but we scaffold only and do not train.
- **The philosophical case for Jeffrey (Skyrms Dutch book, Diaconis-Zabell minimal distance).** It assumes an agent that can state its own all-things-considered posterior on the partition. Our agent cannot do this reliably (verbal confidence AUROC 62.7%, b17), and posterior-stating is order dependent (a02).
- **Human conservatism (Phillips and Edwards, Edwards 1968).** LLMs show both over- and under-reaction, by source type; conservatism does not describe them. The human data are also unread beyond abstracts.
- **Zhao and Osherson invariance findings.** Human rough conformity says nothing about LLM rigidity, and the full paper was not readable.
- **Coin and die studies (Gupta, Zhang, Falck).** Single binary parameter, hard observations, small open models (2B-8B). Our checks are structured and noisy.
- **Oracle labels (d08).** Gains from oracle labels are not available in an agent; they show only that the gain came from the label.
- **Image-net soft labels (Yu 2021).** Annotator distributions on CIFAR-10H are not tool-check outputs.
- **Pushback sycophancy results (b21, d10).** Social pressure from a user, not an informative check. A check result in our loop is not a person, though the gate in 4.7 handles both.
- **Forecasting pipeline (Halawi).** Needs retrieval and fine-tuning, and gains are against a crowd, not a code check.
- **Weaver (d05).** Selection among samples, not credence updating; it assumes conditionally independent verifiers, which the paper itself says is violated.
- **BASIL (c03).** The Bayesian reference is built from the model's own elicited priors, so it is not an oracle.

## 10. Open questions

1. Does coded Bayes-factor multiplication beat model-restated credence at equal tokens on our items? (No direct study; K23.)
2. Jeffrey vs Pearl: which gives better final accuracy and calibration in an agent loop? (K17.)
3. What is the right discount for repeated checks from one model? No intra-model correlation was measured; cross-model it is 42-60% when both are wrong.
4. What are the calibrated pass and fail Bayes factors for our own checks? Does capping alpha at 1 lower error?
5. Does a rigidity test catch real violations, and how often do they occur?
6. Does a "credence moves only on new tool output" rule stop flips without raising under-update?
7. Are hedges mapped consistently across models? QUITE per-model accuracies (a22) were not extracted.
8. Do frontier reasoning models show alpha above 1 and the prior bias? Does extended thinking change alpha? (K21, d11.)
9. What do Zhao and Osherson (2010) and Hadjichristidis et al. (2014) report: N, effect sizes, failures of invariance? Both are closed access.
10. Unverified figures: the first WebPPL number (64%) against the paper, the BayesBench effect sizes, the Gemma simple case in a16, the exact Yu 2021 table alignment.
11. Gap searches 1, 4, 8 and 9 ran with search blocked (HTTP 429, quota exhausted). Repeat them with search available.

## 11. Sources

[V] = opened and read this session. [M] = snippet, title, abstract page or memory only.

**Theory and philosophy**
- [V] Jacobs (2019), The Mathematics of Changing one's Mind, via Jeffrey's or via Pearl's update rule. https://arxiv.org/abs/1807.05609
- [V] Jacobs and Stein (2023), Pearl's and Jeffrey's Update as Modes of Learning in Probabilistic Programming. https://arxiv.org/abs/2309.07053
- [V] Munk, Mead, Wood (2023), Uncertain Evidence in Probabilistic Models and Stochastic Simulators. https://arxiv.org/abs/2210.12236
- [V] Wagner (1992/2013), Generalizing Jeffrey Conditionalization. https://arxiv.org/abs/1303.5436
- [V] Smets (1993), Jeffrey's rule of conditioning generalized to belief functions. https://arxiv.org/abs/1303.1514
- [V] Dziurosz-Serafinowicz and Dziurosz-Serafinowicz (2021), The value of cost-free uncertain evidence. https://link.springer.com/content/pdf/10.1007/s11229-021-03377-0.pdf
- [V] Huber (2008), Reply to Crupi et al. https://kops.uni-konstanz.de/bitstream/123456789/3496/1/HuberReply.pdf
- [V] Yu (2021), Bayesian Neural Networks with Soft Evidence. https://arxiv.org/abs/2010.09570
- [M] Jeffrey (1965), The Logic of Decision. https://doi.org/10.7208/chicago/9780226395838.001.0001 ; https://en.wikipedia.org/wiki/Jeffrey_conditioning
- [M] Diaconis and Zabell (1982), Updating subjective probability. https://doi.org/10.1080/01621459.1982.10477893
- [M] Field (1978), A note on Jeffrey conditionalization; Skyrms (1987), Dynamic coherence and probability kinematics. https://doi.org/10.1086/288841
- [M] Pearl (1988), Probabilistic Reasoning in Intelligent Systems. https://doi.org/10.1016/C2009-0-27609-4
- [M] Pearl (1990), Jeffrey's rule, passage of experience, and neo-Bayesianism. (no URL)
- [M] Chan and Darwiche (2005), On the revision of probabilistic beliefs using uncertain evidence. https://doi.org/10.1016/j.artint.2005.03.001
- [M] Dietrich, List and Bradley (2016), Belief revision generalized. https://doi.org/10.1016/j.jet.2016.03.002
- [M] Hawthorne (2004), Three Models of Sequential Belief Updating on Uncertain Evidence. https://philsci-archive.pitt.edu/11230
- [M] Trpin (2019), Jeffrey conditionalization: proceed with caution. https://doi.org/10.1007/s11098-019-01356-3

**Human studies**
- [V, abstract page only] Zhao and Osherson (2010), Updating beliefs in light of uncertain evidence. https://collaborate.princeton.edu/en/publications/updating-beliefs-in-light-of-uncertain-evidence-descriptive-asses/ ; https://doi.org/10.1080/13546783.2010.521695 (full text closed, d14)
- [M] Hadjichristidis, Sloman and Over (2014), Categorical induction from uncertain premises. https://doi.org/10.1080/13546783.2014.884510
- [M] Over and Hadjichristidis (2009), Uncertain premises and Jeffrey's rule (BBS commentary). https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/uncertain-premises-and-jeffreys-rule/1AC759EB5A1667BEDDC2EE17A365F421
- [M] Phillips and Edwards (1966), Conservatism in a simple probability inference task. https://doi.org/10.1037/h0023653
- [M] Edwards (1968), Conservatism in human information processing. (no URL)

**LLM studies**
- [V] Filbry, Melo, Gal (2026), From Prompts to Posteriors. https://arxiv.org/abs/2610.29331
- [V] Samanta et al. (2026), BayesBench. https://arxiv.org/abs/2606.30850
- [V] Qiu et al. (2025/2026), Bayesian Teaching Enables Probabilistic Reasoning in LLMs. https://arxiv.org/abs/2503.17523
- [V] Gupta et al. (2025), Enough Coin Flips Can Make LLMs Act Bayesian. https://arxiv.org/abs/2503.04722
- [V] Zhang, Yang, Wang (2025), LLMs as Discounted Bayesian Filters. https://arxiv.org/abs/2512.18489
- [V] Falck, Wang, Holmes (2024), Is In-Context Learning in LLMs Bayesian? https://arxiv.org/abs/2406.00793
- [V] Xie, Raghunathan, Liang, Ma (2022), ICL as Implicit Bayesian Inference. https://arxiv.org/abs/2111.02080
- [V] Arora, Jurafsky, Potts, Goodman (2025), Bayesian scaling laws for in-context learning. https://arxiv.org/abs/2410.16531
- [V] Wilie et al. (2024), Belief Revision: The Adaptability of LLM Reasoning (Belief-R). https://arxiv.org/abs/2406.19764
- [V] Xiong et al. (2024), Can LLMs Express Their Uncertainty? https://arxiv.org/abs/2306.13063
- [V] Tian et al. (2023), Just Ask for Calibration. https://arxiv.org/abs/2305.14975
- [V] Sharma et al. (2024), Towards Understanding Sycophancy in Language Models. https://arxiv.org/abs/2310.13548
- [V] Atwell et al. (2026), BASIL. https://arxiv.org/abs/2508.16846
- [V] Pal et al. (2026), Knowing What You Know Is Not Enough. https://arxiv.org/abs/2511.13240
- [V] Farmer, Kochar, Lee (2026), Empirical Characterization of Inference-Time Elicited Probability Revisions. https://arxiv.org/abs/2603.19262
- [V] Kim, Kim, Thorne (2025), From Evidence to Belief. https://arxiv.org/abs/2504.19622
- [V] Wan, Wallace, Klein (2024), What Evidence Do Language Models Find Convincing? https://arxiv.org/abs/2402.11782
- [V] Xie, Zhang, Chen, Lou, Su (2024), Adaptive Chameleon or Stubborn Sloth. https://arxiv.org/abs/2305.13300
- [V] Halawi et al. (2024), Approaching Human-Level Forecasting. https://arxiv.org/abs/2402.18563
- [V] Feng, Zhou, Lin, Roth (2025), BIRD. https://arxiv.org/abs/2404.12494
- [V] Nafar, Venable, Kordjamshidi (2024), BLInD. https://arxiv.org/abs/2402.09614
- [V, partial] Schrader et al. (2024), QUITE. https://arxiv.org/abs/2410.10449
- [V] Belem et al. (2024), Perceptions of Linguistic Uncertainty by Language Models and Humans. https://arxiv.org/abs/2407.15814
- [V] Sileo and Moens (2023), Probing neural language models for understanding of words of estimative probability. https://arxiv.org/abs/2211.03358
- [V] Yona, Aharoni, Geva (2024), Can LLMs Faithfully Express Their Intrinsic Uncertainty? https://arxiv.org/abs/2405.16908
- [V] Kim, Garg, Peng, Garg (2025), Correlated Errors in LLMs. https://arxiv.org/abs/2506.07962
- [V] Saad-Falcon et al. (2025), Weaver. https://arxiv.org/abs/2506.18203
- [V] Stechly, Valmeekam, Kambhampati (2024), On the Self-Verification Limitations of LLMs. https://arxiv.org/abs/2402.08115
- [V] Stechly, Marquez, Kambhampati (2023), GPT-4 Doesn't Know It's Wrong. https://arxiv.org/abs/2310.12397
- [V] Huang et al. (2024), LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Hong et al. (2026), Measuring Sycophancy of Language Models in Multi-turn Dialogues. https://arxiv.org/abs/2505.23840
- [V] Kim and Khashabi (2025), Challenging the Evaluator. https://arxiv.org/abs/2509.16533
- [V] Mei et al. (2025), Reasoning about Uncertainty. https://arxiv.org/abs/2506.18183
- [V] Zeng, Xuan, Cui, Voigt (2025), Thinking Out Loud. https://arxiv.org/abs/2504.06564
- [V] Brown et al. (2024), Large Language Monkeys. https://arxiv.org/abs/2407.21787

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 16 established claims: 12 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **D02.04-K04** (reworded: the sources support less). Jacobs and Stein show the repeated-Pearl-conditioning program (prog1) going to 100% as the number of tests grows, while the Jeffrey-style programs stay put; no source shows Jeffrey sequences reaching confident false beliefs. Corrected claim: Counting repeated noisy checks as independent evidence can pile up confidence: with 5% prevalence, 90% sensitivity, 95% specificity and results pos, pos, neg, three ways to model the repeats give 64% (condition on each test, a repeated Pearl update), 9% and 33% (Jeffrey-style update on the empirical test distribution), and the repeated-conditioning program goes to about 100% with 3000 tests in the same 2:1 ratio while the others stay put. Repeated samples and checks from one source share errors, so extra independent-looking checks can add little real information (majority vote and reward-model selection gain only 40.50% to 41.41% from 100 to 10,000 samples).
- **D02.04-K05** (reworded: the sources support less). Filbry et al. find the failure for non-reasoning models; with reasoning (and code) updates become close to the oracle (e.g. Gemma-4-31B-it matches it on ProteinWorld-simple), so 'without code' is too wide, and Qiu et al.'s null results for CoT prompting, numeric encodings, 30 rounds and base models are on a flight-recommendation task. Corrected claim: Without reasoning or code execution, LLMs update badly on evidence in context: Filbry et al. find non-reasoning updates cut final success by at least 30% versus an oracle, and in a five-round flight-recommendation task Qiu et al. found chain-of-thought prompting, numeric encodings, 30 rounds and base models did not fix the weak updating. Fine-tuning on a Bayesian assistant's predictions does improve it, whereas reasoning plus code execution brings updates close to the oracle; a scaffold cannot train, but it can supply reasoning and code.
- **D02.04-K19** (now single-source: the sources are not independent). The false-negative and false-positive rates come from one paper (Stechly et al. 2024; Graph Coloring FNR 95.8% and Mystery Blocksworld FNR 97.09%, FPR 0.5-18.55% over the four domains, GPT-4); the other listed sources are the same group's earlier paper and Huang et al., which support only the direction (self-verification without an external signal does not help).
- **D02.04-K20** (reworded: the sources support less). Brown et al. show that majority voting and reward-model selection plateau at about 100 samples while coverage keeps rising to 98%, so repeated sampling does not stop helping, only these selection checks do; the correlation numbers (42.3% and 60% agreement, 0.97 for one Llama pair, +11.2 points) check out. Corrected claim: Errors are shared across models, so more checks do not mean more independence: when both models are wrong they pick the same wrong answer on average 42.3% (HuggingFace) and 60% (HELM) of the time (0.97 for one same-provider Llama pair), weighted verifier ensembles beat naive averaging by up to 11.2 points, and gains from adding verifiers shrink because of correlated biases. Majority voting and reward-model selection from repeated samples of one model plateau at about 100 samples even though coverage keeps rising.
