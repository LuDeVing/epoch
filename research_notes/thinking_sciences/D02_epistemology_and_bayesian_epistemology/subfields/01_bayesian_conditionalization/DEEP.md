# Bayesian conditionalization: deep document

*Subfield D02.01. Built from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b10, d07 ...) point to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Conditionalization is the rule for updating belief when you learn something for sure. You have a credence function Cr over possibilities. You learn evidence E. Every possibility that conflicts with E goes to zero. The rest are divided by Cr(E) so they sum to 1 again.

Formula: Cr'(X) = Cr(X and E) / Cr(E). It is defined only when Cr(E) is not 0. (a01, b24)

The key property is ratio preservation. Two surviving possibilities keep the same odds as before. Only the eliminated ones change. (a01)

Two parts to keep apart:
- Elimination: set what E rules out to zero.
- Renormalisation: divide the survivors by their total so they sum to 1.

Odds form: posterior odds = prior odds x likelihood ratio. Hard elimination is the limit case where the likelihood of the evidence under a hypothesis is 0.

Why it matters for our agent: stage S7 (Select) and guardrail G5 (code selects, code normalises probabilities over exclusive answers). The agent has a set of candidate answers. Checks rule some out. Code, not the model, sets the ruled-out ones aside and rescales the rest.

What the literature gives us:
1. A long philosophical case for coherent, rule-governed updating (Dutch book, accuracy).
2. A large human literature on how people deviate (too little update, base-rate neglect, format effects).
3. A newer LLM literature (2021-2026) showing models do not update coherently in their heads, and that code-side arithmetic fixes much of it.
4. One human study (Mandel 2018) that directly supports the G5 normalisation step. No LLM replication exists.

## 2. History and theories in depth

**Origins.** Bayes (1763) gave the core results. Earman argues the view is "Bayesian" because the essay holds both probabilism (credences obey the probability axioms) and conditionalization, not because of the theorem alone. Ramsey (1926) and de Finetti (1937) tied degrees of belief to betting behaviour and showed incoherent bets lose for sure. Credit taken from SEP; the originals were not read. (a02, a31)

**Synchronic Dutch book (probabilism).** SEP example: credences .75 in A and .30 in not-A can be booked for a sure loss of $5. This is the basis for "make exclusive options sum to 1". (a02)

**Diachronic Dutch book (conditionalization).** Teller (1973) and Lewis (1999). If you plan to adopt Pr2(A) after learning E, and Pr2(A) differs from Pr1(A|E), a bookie sells four bets and wins a sure amount: [Pr1(A|E) - Pr2(A)] x Pr1(E), whether E is true or false. Skyrms (1987) proved the converse: a conditionalizer cannot be booked this way. (a03, a32)

Criticisms:
- Van Fraassen (1989): assumes the agent fixes the update rule in advance.
- Gallow (2019): fails if the possible evidence propositions overlap rather than partition.
- Briggs and Mahtani: shows tension, maybe not strict irrationality.
- Practical, not epistemic: a betting loss is not an error of belief. (a02, a03)

Rescorla (2019) extended the theorem and converse to Kolmogorov conditionalization, which handles evidence of prior probability zero. Levi and Kyburg complain the invariance condition asks for unreasonable rigidity. (a04)

**Accuracy arguments.** Credences are estimates of truth values. Non-probabilistic credences are accuracy-dominated (Joyce 1998). Briggs and Pettigrew (2020) show conditionalization as a plan avoids dominance. The SEP extract did not mention Greaves and Wallace (2006), who show conditionalization maximises expected accuracy; that is background knowledge, not read here. This gives a non-betting reason to normalise: coherent distributions score better on a proper scoring rule. It justifies the plan, not every later revision. (a05)

**Jeffrey conditionalization.** For uncertain evidence. Scale credences inside E and inside not-E by common factors so the new credence in E is what the experience fixed. Nothing is forced to zero. Ratios inside E and inside not-E are kept (rigidity). Defended by a Dutch book. Weisberg's Red Jelly Bean case says it is still too inflexible. It needs the shifted credence in E as input, which the evidence does not supply. Strict conditionalization is the limit case of a perfect check. (a06)

**Known limits (SEP).** (a07, a08)
- Priors: probabilism plus conditionalization do not fix induction. The verdict depends on the prior.
- Zero credence: conditioning on a zero-credence proposition is undefined by the ratio formula. A credence of 0 or 1 can never move. Regularity (no zero credence for possible events) conflicts with the coin case. Responses: infinitesimals, comparative probability, Kolmogorov limits. Unsettled.
- Old evidence: Mercury and general relativity (Glymour, Earman).
- New theory: credence drops with no new evidence.
- Memory loss: conditionalization preserves certainties.
- Self-locating belief: Sleeping Beauty (Lewis 1/2, Elga 1/3).

For us the new-theory problem is concrete: if the true answer was never in the candidate set, conditionalizing cannot add it. That is a generation (S3) problem.

**The psychology line (human updating).**
- Edwards (1968) conservatism, the bookbag task. Bags are 700 red/300 blue or 300 red/700 blue. Draw with replacement: 8 red, 4 blue. Typical answer about .70. Bayes: .967. (a09, b01) Primary not read; secondary sources only.
- Competing explanations: anchoring on the prior (Tversky and Kahneman), noisy memory retrieval (Hilbert 2012), cognitive ability (Oechssler 2009: bias shrinks with ability but does not vanish). (a10)
- Benjamin (2019) is the best opened synthesis. Stylised facts: underinference is the norm; it grows with sample size; base rates are also under-used; signals are not pooled as Bayes says, recent ones count more. (b01-b05, b25)
- Base-rate side: Kahneman and Tversky (1973) engineer-lawyer; Bar-Hillel (1980) cab problem; Casscells et al. (1978) Harvard staff test. The two errors do not conflict: people under-use both the prior and the evidence relative to Bayes. (b03, a12-a14)
- Format line: Gigerenzer and Hoffrage (1995) natural frequencies. Rivals say nested sets (Barbey and Sloman 2007), ecological rationality, or problem interpretation (Sirota 2015). (d03, b22)

**Bayesian models of LLM behaviour.** Xie et al. (2022): in-context learning as implicit inference over latent concepts. Arora et al. (2025): Bayesian scaling laws fit ICL curves. Zhu and Griffiths (2024): iterated learning can elicit an LLM's prior. Against: Falck et al. (2024) martingale violations. A good fit of a Bayesian model does not prove a Bayesian mechanism. (a21, a22, b15, b08)

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Conditionalization: zero what E excludes, divide by Cr(E); survivors keep ratios | Cr'(X)=Cr(X and E)/Cr(E), Cr(E) not 0 | SEP (a01, b24) | [S] definition, one source opened |
| Diachronic Dutch book sure loss | [Pr1(A\|E) - Pr2(A)] x Pr1(E) | SEP Dutch Book; Teller; Lewis (a03) | [C] argument disputed |
| Humans under-update on sample evidence | Pooled slope of subjective on Bayes log-odds c-hat = 0.20 (SE 0.063); 8 red/4 blue: ~.70 stated vs .967 Bayes | Benjamin 2019; Edwards 1968 (b01, a09) | [E] |
| Underinference depends on sample size | Mean slope for samples of 2-6: 0.73, 0.98, 0.52, 1.06, 0.67 (SE 0.07-0.10). So 0.20 is pooled and overstates small-sample conservatism | Benjamin 2019 (b01; critique) | [E] |
| Reported belief follows sample proportion, not count difference | Card deck, 2/3 proportion: median 70% for 8a/4b (Bayes 94%), 68% for 4a/2b (80%), 70% for 40a/20b (99.9999%) | Benjamin 2019 (b02) | [E] |
| Distance from Bayes depends on scale | .70 vs .97 from .50 is ~43% of the Bayes move in probability; in log-odds ~25% (0.85 vs 3.39) | critique (a09) | [E] arithmetic |
| Overinference is rare | Appears when signal rates are close (0.6 vs 0.5) | Benjamin 2019 (b01) | [S] |
| Base rates under-used, usually partly | Engineer-lawyer 30% vs 70% pool: mean answers 50% vs 55%; odds ratio ~1.2 vs Bayes 5.4 | K&T 1973 via Benjamin (b03) | [E] |
| Cab problem | Bayes 41% (.12/.29); modal answer 80% (36% of respondents); ~10% near correct | Bar-Hillel 1980 via Benjamin (b03) | [E] |
| Causal base rates are used more | e.g. "85% of accidents involve blue cabs" | Bar-Hillel 1980 (b03) | [S] |
| Feedback with correct posterior removes underinference | Donnell and DuCharme 1975: gone within 60 trials, mostly first 10; then overinference on a new problem. Martin and Gettys 1969: no learning over 200 trials | Benjamin 2019 (b04) | [S] small labs |
| Natural frequencies, primary study | Study 1 N=60, 15 problems: probability 16% (standard menu), 28% (short menu); frequency 46%, 50%. Study 2 N=15: 6.4%, 17.5% (probability formats) | Gigerenzer and Hoffrage 1995 (d03, d04) | [C] size and mechanism contested |
| Natural frequencies, later | Binder 2015: 42% vs 5% (no visuals 26% vs 2%; visuals 51% vs 6%). Garcia-Retamero and Hoffrage 2013: 51% vs 38%. Physicians 46% vs 10% | Cui et al. 2023 review (b21) | [C] mixed; publication bias noted |
| Natural frequencies plus training are additive | N=577 medical students: probability pretest 36%; NF pretest 68% (OR 11.55); probability after training 64%; NF after training 89%; interaction OR 0.98, p=.759 | Feufel 2023 (b20) | [S] no control group |
| Natural frequencies weak or reversed | N=329: single test 36.2% vs 21.6% (OR 2.41); two sequential tests 4.9% vs 10.6% (OR 2.73 for odds/LR); psychology students OR 1.45, p=.22 | Schulz 2025 (b19) | [C] |
| Coherentizing human forecasts | N=50 analysts, 4 exclusive hypotheses: MAE 0.23 raw, 0.15 coherentized (35%, d=0.96, t(49)=6.77), 0.09 after averaging all 50 (61%). Plain normalisation 0.13 | Mandel et al. 2018 (d01, d02) | [E] humans; untested in LLMs |
| Coherentizing helped ACH group more | d=0.69 control, d=1.37 ACH. ACH checklist did not improve accuracy (d=0.45 favouring control) | Mandel 2018 (d02) | [S] |
| LLMs plateau in multi-round preference updating | 5 rounds, 624 users, 3 flights per round; Bayesian Assistant final round 81%; off-the-shelf ~36-58% (read from figures); CoT, numeric encoding, 30 rounds did not help; humans improved p=.002 but short of Bayes | Qiu et al. 2025/26 (a16, c01, c02) | [S] |
| Bayesian teaching (fine-tuning) beats oracle teaching | Human users N=500, flights: baseline 37.0%, oracle-tuned +24.0, Bayesian-tuned +38.5 (CI 31.1-45.9). Hotel: 36.7%, +16.7, +29.4. Agreement with Bayesian Assistant ~80% | Qiu et al. (b06, a17) | [S] training, out of scope |
| LLMs violate the martingale property | Bernoulli n=50, m=n/2 and 2n; gpt-3.5 Gaussian sample variance 0.711, CI [0.680, 0.742], below 1; instruct models not closer than GPT-3 | Falck et al. 2024 (a19, b08) | [E] with b10, b11 |
| Coherence axioms broken across calls | ForecastBench, 30 scenarios: over 50% violation across separate conversations for almost all model-axiom pairs; within one dialogue ~10% (Gemini-2.5-Pro), 1 of 30 (Gemma-4-31B) | Filbry et al. 2026 (d09, b11) | [S] small |
| Step-by-step vs batch updating | GPT-5.1 near-optimal step-by-step vs its own likelihoods, often far in batch. But AUROC/ECE: batch equal or better on 3 of 4 datasets; forced Bayes worse on MediQ | Chen et al. 2026 (b10, d06, d07) | [C] |
| Likelihoods are the weak link | ~half of wrong-direction batch updates move toward a better (GPT-5.1) likelihood; ~15% more land closer to the oracle posterior | Chen et al. 2026 (d07) | [S] |
| Reasoning plus code closes the gap to an oracle posterior | No reasoning: final success cut by at least 30% vs oracle trajectory, some weak models near 0% on 20Q; reasoning fixes the simple case; code fixes the no-closed-form case (Gemini-2.5-Pro, ProteinWorld-hard; 40 runs per environment) | Filbry et al. 2026 (d08) | [S] mostly 26-35B models |
| Code arithmetic on Bayesian-network word problems | GPT-4 extract + ProbLog ~98% (96-100% every split) vs ~29% CoT (approximate, garbled table) | Nafar et al. 2024, BLInD (d15) | [S] |
| Word-valued premises are hard | GPT-4-Turbo 8.7% correct with word premises; 3.1% with no premises; GPT-4 writing ProbLog ~76% parse errors | QUITE (d16) | [S] |
| In-context evidence beats stated prior; error is in the prior | Base models ~60-80% heads regardless of stated bias; best-fit discount 0.31 (Gemma-2-2B-it) to 0.91 (Mistral-7B-it); attention correlation R=0.02, -0.03 | Gupta 2025 (b07, c06, c07, d18) | [E] small models, toy task |
| Discounted filter fits better than exact Bayes | gamma below 1 for all models; instruct-tuned discount more; update divergence under 13% of total error; rho = -0.85 for Llama-3.1-8B die | arXiv 2512.18489 (b12) | [S] |
| Option label bias | MMLU 0-shot: gold to D: gpt-3.5-turbo 67.2 to 60.9; gold to A: llama-30B 53.1 to 68.2; picks A/B/C/D 34.6/27.3/22.3/15.8% | Zheng et al. 2024 (a23, d13) | [E] 2023 models |
| Permutation averaging removes bias | llama-2-70B: 50.8 default (RStd 7.5), 54.7 cyclic x4 (RStd 4.5), 51.8 PriDe 5% (RStd 2.3); llama-30B 34.6 to 47.7 cyclic | Zheng et al. (d13) | [E] 2023 models |
| Example order swings accuracy | SST-2 4-shot, GPT-3 2.7B: 54.3% to 93.4%; contextual calibration up to +30.0 points | Zhao et al. 2021 (b16, c11) | [E] |
| Self-consistency over greedy CoT | GSM8K +17.9, SVAMP +11.0, AQuA +12.2. PaLM-540B GSM8K: greedy 56.5, vote 74.4, normalised weighted sum 74.1, unnormalised 59.9, weighted average 22.1 | Wang et al. 2023 (a24, d10) | [S] |
| Verbalised confidence calibration | Verbalised cut ECE by a relative ~50% vs token probabilities for ChatGPT, GPT-4, Claude 2 | Tian et al. 2023 (a25, c20) | [E] |
| Large models calibrated on MC when formatted right | "None of the above" hurts calibration; RLHF miscalibration fixed by temperature tuning | Kadavath et al. 2022 (a26) | [E] |
| LLM forecasts without retrieval near coin flip | Brier .208 best (GPT-4-1106) vs crowd .149, random .25; full system .179; accuracy 71.5% vs 77.0% | Halawi et al. 2024 (c18) | [S] |
| Naming the wrong option is harder than naming the right one | Elimination less accurate in every model and dataset; small models below 50/50. Iterative elimination ARC: LLaMA-2 70B ~.834, .812, .768 (4, 3, 2 choices); 7B .526, .322, .232 (read from layout; check before quoting) | Balepur et al. 2024 (d11, d12) | [S] 2023 models |
| Embers of autoregression | GPT-4 cipher decoding 51% for high-probability output vs 13% for low-probability | McCoy et al. 2023 (a27) | [S] |
| GPT-3 on the cab problem | Approximately correct, but fails on slight rewording (black cab gave 20%); correct on 6 of 12 vignettes, others correct or human-like errors | Binz and Schulz 2023 (c21; critique) | [C] |
| LLMs on the HIV problem | Facilitated natural-count version answered correctly more often by all models except Llama 2; 7 models x 12 tasks x 10 runs; per-model numbers only in a figure | Macmillan-Scott and Musolesi 2024 (d05) | [S] 2023 models |
| Scaffold with running differential | MAI-DxO (o3) 81.9% at $4,735 vs plain o3 78.6% at $7,850; 304 NEJM cases; Bayesian role not ablated | Nori et al. 2025 (d17) | [S] |
| BIRD: LLM proposes factors, Bayes net computes | Pairwise preference F1 59%, more than 30% above GPT-4; abductive factor generation +4.4 / +3.9 points | Feng et al. 2025 (b14, c14) | [S] |
| VLM evidence integration is additive log-odds | R^2 0.852, 0.800, 0.692, 0.860 across four 3-4B models; unit-weight naive Bayes 0.477-0.717; interaction adds at most 0.001 | arXiv 2610.19407 (b13) | [S] |

## 4. Mechanisms and models

Written so an engineer can build each piece.

### 4.1 The core update (the S7/G5 operation)

Input: K exclusive candidate answers, a prior vector p, a result from a check.

Hard version:
```
def condition(p, ruled_out):          # p: dict answer -> prior
    q = {a: (0.0 if a in ruled_out else v) for a, v in p.items()}
    z = sum(q.values())
    if z == 0: raise RevivalNeeded    # evidence contradicts every candidate
    return {a: v / z for a, v in q.items()}
```
Unit test: for any two survivors a, b, q[a]/q[b] equals p[a]/p[b].

Soft version (likelihood update, covers noisy checks):
```
def update(p, lik):                   # lik[a] = P(evidence | answer a)
    q = {a: p[a] * max(lik[a], FLOOR) for a in p}
    z = sum(q.values()); return {a: v / z for a, v in q.items()}
```
Hard elimination is lik[a] = 0. A floor (for example 0.02) keeps a wrongly ruled-out answer recoverable. Rationale: a credence of 0 cannot be moved by any later evidence (a04, a07). The floor is a design choice from the SEP argument. No LLM study has tested floor versus hard zero (d11, d12).

Jeffrey version (uncertain evidence): given the check's reliability r that E is true, set mass r on E and 1-r on not-E, scaling inside each part by a common factor (a06). A noisy check should shift, not zero, a candidate. Untested in LLMs (K27).

### 4.2 Pure normalisation (the Mandel step)

If the model gives raw scores s_a for exclusive options that do not sum to 1, divide each by the total: p_a = s_a / sum(s). In Mandel 2018 this was as good as the quadratic-programming "closest coherent vector" method (MAE 0.13 vs 0.15; d02). Expect a gain only when the sum is far from 1. Log the sum first. If it is near 1, normalising does nothing.

### 4.3 Where the model's numbers come from

1. Verbalised confidence. Better calibrated than token log-probs for RLHF models (a25). Elicit all options in one call. Separate calls break normalisation more than 50% of the time; one dialogue cuts that to about 10% (d09).
2. Sampled frequency (vote). A frequency estimate, not a calibrated posterior (a24).
3. Token log-probs. Carry label, position and common-token bias (a23, b16). Divide by a content-free baseline (contextual calibration, b16) or average over option permutations (cyclic permutation, PriDe; d13).

### 4.4 Removing prompt-injected priors

Option order and label are non-evidential priors. Shuffle option order across draws (cyclic where cheap), take the mean probability per content item, then normalise. Cyclic over 4 options costs 4x. PriDe estimates the label prior from about 5% of samples at 1.15 to 3.4x cost (d13). Contextual calibration: get label probabilities for a content-free input ("N/A"), then rescale so that prediction is uniform (b16).

### 4.5 Natural-frequency restatement

Rewrite "prevalence 0.1%, false positive rate 5%" as "of 10,000 people, 10 have it; of the 9,990 others, about 500 test positive". Then compute in code anyway. Accounts of why it helps compete: nested sets, ecological frequency format, problem interpretation, and (the original authors, d04) computational simplicity of the arithmetic (b22). The effect is not general (b19). It is a representation option for S2/O6 to test, not a rule.

### 4.6 Division of labour the evidence supports

Model: extract quantities, propose factors and levels, judge a likelihood label on a fixed scale. Code: multiply, normalise, threshold. Support: BLInD ~98% vs ~29% CoT (d15), BIRD F1 59% (b14), reasoning plus Python closed the no-closed-form case (d08). Weak link: the model's likelihood judgments (d07, d16). So log them and, where possible, take two independent samples.

### 4.7 Descriptive models of how LLMs update

- Discounted Bayesian filter: old evidence gets weight gamma below 1 (b12). Compare Benjamin, Bodoh-Creed, Rabin (2018) for humans: posterior odds = likelihood ratio x prior odds^d, 0<d<1, so older signals fade as d^k (b05). Both say old evidence fades.
- Additive log-odds with unequal modality weights plus a prior (b13).
- Latent concept inference (Xie 2022) and Bayesian scaling laws (Arora 2025): a prompt acts like evidence about which task is running. Post-training mostly shifts the prior over tasks (b15).
- Martingale test (Falck): a true Bayesian's prediction should not depend on the order of exchangeable data or on imputed missing data. LLMs fail this (b08).

## 5. What holds up

**Replicated or multi-source (strongest parts).**
1. Human underinference from sample evidence. Dozens of bookbag studies, synthesised by Benjamin 2019 (b01). Overinference is rare. Size depends on sample size, and the pooled slope 0.20 overstates small-sample conservatism.
2. Partial, not total, base-rate neglect (b03). Boundary: causal or specific base rates raise use (Bar-Hillel 1980).
3. LLMs break Bayes coherence without tools: Falck (martingale), Filbry (Dutch-book axioms), Chen (own-likelihood gap). Three independent papers (K09 [E]). Caveat: Chen and Filbry measure consistency against the model's own likelihoods, not truth. A consistent model can still be wrong.
4. Prompt-format priors (label, position, example order) distort answers: Zhao 2021 and Zheng 2024 agree (K12 [E]).
5. Verbalised confidence beats token log-probs for RLHF models: Tian and Kadavath (K14 [E]).

**Failed or contested.**
- Natural frequencies. Large in 1995 (46% vs 16%, strict criterion) and Binder 2015 (42% vs 5%); mild in Yamagishi 2003; null in psychology students (OR 1.45, p=.22); reversed for two sequential tests (4.9% vs 10.6%) (b19, b21, b22). Mechanism unsettled. The apparent clash 16/46 vs 22/48 is only standard-menu vs menu-average of one study (d03).
- One-at-a-time updating. Better internal consistency, but task performance (AUROC, ECE) was equal or better in batch mode on 3 of 4 datasets, and forced Bayes hurt on MediQ (d06, d07). Do not assume sequential updating raises accuracy.
- Whether GPT-3 shows the base-rate fallacy: passes the cab vignette, fails on rewording (c21).
- Failed interventions: CoT, numeric encodings, 30 rounds for LLM multi-round updating (c02). Explicit debiasing instructions helped little against option bias (a23). Stated prior in the prompt does not fix base-model priors (b07, d18). Longer reasoning chains had more doubt but no more accuracy (b23). Scale did not help in Pythia 70M-12B (c07).

**What worked.**
- Forcing exclusive hypotheses to sum to 1: MAE 0.23 to 0.15 (35%), 0.09 after averaging 50 (61%), in humans (d01). Plain normalisation 0.13 (d02).
- Permutation averaging and PriDe against label bias (d13).
- Contextual calibration: up to +30.0 points (b16).
- Offloading arithmetic to code (d15, d08).
- Feedback on the correct posterior removes human underinference in a few dozen trials but can overshoot (b04).
- Fine-tuning on Bayesian assistant guesses (b06) works but needs training.

**Moderators.**
- Humans: sample size; closeness of signal rates.
- LLMs: model size (negligible for updating in Pythia); instruction tuning (follows a stated bias better, discounts old evidence more); reasoning (helps simple cases) and code (helps no-closed-form cases); one dialogue vs separate calls (violations over 50% down to ~10%); task type.
- Tension: Chen and Filbry say reasoning gets near Bayes; Qiu says CoT did not help in the preference task. Probably task (given likelihoods vs hidden user preferences). Untested.

**Strength of evidence.** Only 2 of 19 early claims have three or more independent sources. Almost all LLM-updating studies are preprints, use 2B-70B open models and toy tasks. Frontier models appear only in Chen (GPT-5.1), Filbry (Gemini-2.5-Pro), Halawi and Nori (o3).

## 6. Language models

**Default behaviour.**
- They do not accumulate evidence like a Bayesian. In a 5-round preference task accuracy stalls after round 1 (Qiu: Gemma 2 9B/27B, Llama 3 8B/70B, Qwen 2.5 7B/32B, Gemini 1.5 Pro, GPT-4.1 Mini). 48 humans improved (p=.002) but also fell short (c05, a16).
- Predictions depend on order (martingale violation). Uncertainty does not shrink like a posterior; gpt-3.5 is overconfident with small samples (a19, a20, b08).
- Probabilities over exclusive options often fail to sum to 1 when asked in separate conversations (over 50% of 30 scenarios) (d09).
- Prompt format injects priors: example order moved GPT-3 2.7B from 54.3 to 93.4 on SST-2 (b16); gold at D vs A moved gpt-3.5-turbo and llama-30B by 6 to 15 points (a23).
- Output probability pulls on answers: cipher 51% vs 13% (a27).
- Own priors are wrong and slow to correct: coin tasks start at 60-80% heads (b07).

**What helped, and by how much.**

| Intervention | Effect | Source |
|---|---|---|
| Code does arithmetic, model extracts | ~98% vs ~29% CoT (GPT-4, BLInD) | d15 |
| Reasoning plus code execution | Gemini-2.5-Pro closes no-closed-form gap (40 runs) | d08 |
| Reasoning, no code | Fixes the simple case; otherwise final success down at least 30% vs oracle | d08 |
| Step-by-step with own likelihood | Near-optimal consistency for GPT-5.1 | d06, d07 |
| Staying within one dialogue | Violations from over 50% to ~10% | d09 |
| LLM proposes factors, Bayes net computes | F1 59%, more than 30% above GPT-4 | b14 |
| Contextual calibration | Up to +30.0 points | b16 |
| Cyclic permutation (x4) | llama-2-70B 50.8 to 54.7 | d13 |
| Self-consistency (vote) | +17.9 GSM8K, +11.0 SVAMP, +12.2 AQuA | a24 |
| Natural counts in HIV problem | Helped all 2023 models except Llama 2 | d05 |
| Verbalised vs token probabilities | ~50% relative ECE cut | a25 |
| Fine-tuning on Bayesian assistant | +38.5 points vs baseline 37.0 (human users, flights) | b06 |
| Retrieval plus aggregation (forecasting) | Brier .208 to .179 (crowd .149) | c18 |
| Probability-ranked differential in a scaffold | 81.9% vs 78.6% (not ablated) | d17 |

**What did not help.** CoT, numeric encodings, 30 rounds (c02). Forcing explicit Bayes from the model's own likelihoods (mixed; hurt on MediQ; d07). Explicit debiasing instructions (a23). Stating the bias in the prompt for base models (d18). Prompting for frequencies raised their use but not reliability (b23). Scale alone (c07).

**Where the weak link sits.** In a Bayes update the arithmetic is easy. The likelihood judgment is the problem: about half of wrong-direction batch updates follow a better likelihood than the model's own (d07); word premises are solved in 8.7% of QUITE cases (d16). The "ruled out" call is itself unreliable: asking for the wrong option is less accurate than asking for the right one in every model and dataset tested (d11). Wrong zeros compound over rounds (d12).

**Still unknown.** Whether code-side normalisation of a frontier model's option scores beats its own stated distribution at equal tokens (not tested anywhere). Position bias on 2025-26 frontier models. Hard zero vs soft down-weighting (no head-to-head). Jeffrey updating (no LLM study).

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | Keep probability arithmetic (normalising, multiplying, thresholding) in code, never in the model's head. Without tools LLMs break Bayes coherence | G5/S7 | [E] | K09: a19, a20, b08, b10, b11 |
| A2 | Do not read model-stated confidence as a posterior that sharpens with evidence; it does not | G5 | [E] | a20, b08 |
| A3 | Randomise option order across draws and average over permutations before normalising; do not trust one fixed order | S7 | [E] that bias is real; frontier size untested | K12: a23, b16, c11, d13 |
| A4 | Count independent evidence passes explicitly in code; humans under-weight many small pieces and LLMs fade old ones | G5/S7 | [E] humans; [S] LLM discounting | b01, b02, b12 |
| A5 | If a verbalised probability is used, prefer verbalised over token log-probs for RLHF models; check calibration per task class | S7 | [E] | a25, a26 |
| A6 | Elicit all option scores in one call as numbers and normalise in code; separate calls fail the sum-to-1 test over half the time | G5 | [S] for the one-call rule; [E] that coherence fixing helps (humans) | d09, d01, d02 |
| A7 | Fix the update rule before seeing the check result (design rationale from the Dutch book) | G5 | [S] rationale only | a03 |
| A8 | Log the raw sum of option scores per run, so normalisation gains can be attributed | memory/log | process, no claim | d01 |

### Test first (each is a row in UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Code normalisation of raw option scores vs the model's own stated distribution, Brier at equal tokens | G5/S7 | [S] human-only | K16: d01, d02 |
| T2 | Hard zero vs floor (soft down-weighting) with a revive rule | S7 | [S] | K20: d11, d12, a04, a07 |
| T3 | Code posterior from model likelihood labels vs model-stated posterior | S7 | [C] | K10, K18, K22: b10, d07, d08, b14, d15 |
| T4 | Per-evidence code posterior vs batch, scored on accuracy | S7 | [C] | K10: b10, d06, d07 |
| T5 | Permutation averaging on frontier models | S7 | [S] 2023 models | K23: d13, d14 |
| T6 | Natural-count restatement of probability problems | S2/O6 | [C] | K06: d03, b19, d05 |
| T7 | Prior in the prompt vs prior in code | G5 | [S] small models | K25: d18, b07 |
| T8 | Jeffrey-style update from the model's stated confidence in a check | G5/S7 | none found | K27: a06 |
| T9 | Elicit P(E\|H) twice and average, or flag disagreement | S7 | [S] | K21: d07, d16 |
| T10 | Vote over N samples vs normalised probability aggregation, equal tokens | S7 | [S] | K13: d10 |
| T11 | Reseed the option set when all candidates fail, instead of renormalising over a stale set | S3/S7 | [S] | K02: a08 |
| T12 | A probability-ranked running differential role, ablated | S7 | [S] | K26: d17 |

## 8. Concrete tests on our bench

All tests: both arms at equal tokens (count prompt plus completion for every call; give the cheaper arm extra samples). At least 3 seeds. Report Brier, accuracy, and the paired difference with a 95% bootstrap interval.

1. **Normalise vs raw (T1).** Items: exclusive-answer multiple-choice items with a gold label (ARC-style, BRAINTEASER, held-out set), 200 or more. Arm A: model states a probability per option, used as is. Arm B: same output, code divides by the sum. Log the sum. Metric: Brier and accuracy, split by items where |sum - 1| > 0.2. Expected: no change when the sum is near 1; a Brier gain on far-from-1 items.
2. **Hard zero vs floor (T2).** Items: tasks with a check that can rule options out (rule induction, ARC candidates with partial checks). Arm A: set ruled-out options to 0. Arm B: multiply by a floor of 0.02, revive if all else fails. Add 0%, 10%, 20% injected wrong "ruled out" calls. Metric: gold-zeroed rate, final accuracy. Expected: hard zero loses with noise; tie at 0%.
3. **Model posterior vs code posterior (T3).** Items: sequential-evidence tasks where each clue has a checkable likelihood (20 questions on animals, ForecastBench-style scenarios, Eleusis-like). Arm A: model states the final posterior. Arm B: model gives per-clue likelihood on a 5-level scale; code maps, multiplies, normalises. Arm C: B with oracle likelihoods (upper bound). Metric: accuracy and Brier against truth, not against the model's own consistency. Expected: B above A on hard sizes; the C minus B gap is the likelihood-quality loss.
4. **Sequential vs batch code posterior (T4).** Same items. Per-clue update with only the current clue shown vs all clues at once. Metric: accuracy, AUROC, ECE. Expected per Chen: no accuracy gain from sequential.
5. **Order bias on the target model (T5).** 200 MC items with gold evenly at A-D. Measure accuracy by gold position. Arm A: fixed order. Arm B: mean over 4 cyclic orders (4x cost). Arm C: single order with 4x more samples. Metric: accuracy, position gap.
6. **Natural-count restatement (T6).** 60 base-rate and test-accuracy problems (HIV, cab, mammography variants), 3 rewordings each. Arm A: probabilities. Arm B: counts out of N. Metric: exact correctness and stability across rewordings. Expected: some gain on single-test problems, none on two sequential tests.
7. **Stated prior vs code prior (T7).** Coin or die tasks with a stated bias and n flips. Arm A: prior in prompt, model answers. Arm B: prior in code, model only extracts counts. Metric: total variation distance to the Bayes posterior.
8. **Jeffrey vs hard condition (T8).** Checks with known reliability (a flaky tool at 80% accuracy). Arm A: result treated as certain. Arm B: Jeffrey shift with r = stated reliability. Metric: Brier, gold-zeroed rate.
9. **Elicit twice (T9).** Arm A: one likelihood sample. Arm B: mean of two. Arm C: mean of two plus flag when they differ by over one level. Metric: wrong-direction update rate, final accuracy.
10. **Vote vs normalised aggregation (T10).** 8 samples voted vs 8 verbalised distributions averaged vs one long chain. Metric: accuracy. Expected: tie within 1 point (PaLM-540B tied within 0.3).
11. **Reseeding (T11).** Items where the gold answer is missing from the initial candidates. Arm A: renormalise over the stale set. Arm B: reseed on total failure. Metric: gold-in-set rate, accuracy.
12. **Differential ablation (T12).** Scaffold with vs without a role that keeps a probability-ranked list. Metric: accuracy, cost per item.

## 9. What does not transfer, and why

- **Human conservatism numbers.** Slope 0.20 and the 43% and 25% figures come from bookbag tasks with people. LLMs need not share the bias; Gupta says the error is in the prior, not the update (b07). Use as a hypothesis for the direction of error only.
- **Natural frequencies as a general fix.** Mixed even in humans (b19, b22). The 1995 result used a strict process-plus-outcome criterion and students.
- **Bayesian teaching.** Needs fine-tuning (Qiu). Our agent does not train. Only the diagnosis transfers: the gap is in update behaviour, not knowledge (b06, c03).
- **Martingale and discounted-filter results.** Small open models and synthetic tasks (Bernoulli, Gaussian, die). Unknown for GPT-5-class models on real tasks.
- **Consistency scores (Chen, Filbry).** They measure agreement with the model's own likelihoods. Consistent is not correct (K10).
- **Dutch book and accuracy arguments.** They justify coherence for an ideal agent. They are not a performance claim; the practical-not-epistemic objection stands (a03).
- **Self-consistency weights.** In Wang et al. the weights are path probabilities, not verbalised option probabilities. The vote/normalised tie says nothing about verbalised probabilities (d10).
- **Open-ended problems.** No exclusive answer set, so conditionalization over candidates (S7) does not apply in open mode.
- **Calibration studies.** Tian and Kadavath test answer confidence, not likelihoods P(E|H). Likelihood quality is unmeasured (critique gap 6).
- **Forecasting and diagnosis scaffolds.** Halawi and Nori use retrieval and many other parts; no ablation isolates conditionalization.
- **Strict zero.** In philosophy, conditioning on zero is undefined. In an agent, a zero is a lost answer. The theory (a04, a07) and the elimination data (d11, d12) both point to a floor, but the data are 2023 models and no head-to-head exists.

## 10. Open questions

1. Does code-side normalisation of an LLM's raw option scores improve Brier or accuracy over its own stated distribution at equal tokens? (no LLM study)
2. Hard elimination vs soft down-weighting when evidence judgments are noisy. What is the error rate of an LLM's "ruled out" call and what does a wrong zero cost?
3. Does one-at-a-time evidence beat batch on accuracy in frontier models outside Chen's and Filbry's tasks? Neither paper has been independently replicated.
4. How large is option-position bias on 2025-26 frontier models, and does permutation averaging still help?
5. How good are elicited likelihoods P(E|H)? Answer-confidence calibration is a different thing.
6. What is the best handling of uncertain evidence in a scaffold (Jeffrey or likelihood ratios)? No LLM study.
7. Adversarial base-rate rewordings on frontier models, after Binz and Schulz 2022 and Macmillan-Scott 2024.
8. Does a stated numeric prior move a frontier model's answer as Bayes predicts?
9. Vote vs explicit normalised probability at equal tokens on current models.
10. Does a Bayesian-teaching-like effect appear with worked posteriors as in-context examples?
11. Is the error rate of "ruled out" calls lower when the check is code-run rather than model-judged?
12. When the true answer was never in the candidate set, how often does the agent notice and reseed?
13. Primary sources still unread: Ramsey, de Finetti, Lewis, Teller, Edwards 1968, Kahneman and Tversky 1973, Bar-Hillel 1980, Casscells 1978, Binz and Schulz body, Griffiths 2023.

## 11. Sources

[V] = opened and read. [M] = snippet, memory or secondary mention only.

- [V] SEP, Bayesian Epistemology. https://plato.stanford.edu/entries/epistemology-bayesian/ (b24 read to section 5.1 only)
- [V] SEP, Dutch Book Arguments. https://plato.stanford.edu/entries/dutch-book/
- [V] Benjamin (2019) Errors in probabilistic reasoning and judgment biases. https://www.nber.org/system/files/working_papers/w25200/w25200.pdf
- [M] Wikipedia, Conservatism (belief revision), on Edwards 1968, Hilbert 2012, Oechssler 2009. https://en.wikipedia.org/wiki/Conservatism_(belief_revision) (secondary page)
- [M] Wikipedia, Base rate fallacy. https://en.wikipedia.org/wiki/Base_rate_fallacy
- [M] Kahneman and Tversky (1973) On the psychology of prediction. https://doi.org/10.1037/h0034747
- [M] Bar-Hillel (1980) The base-rate fallacy in probability judgments. https://doi.org/10.1016/0001-6918(80)90046-3
- [M] Casscells, Schoenberger, Graboys (1978). https://doi.org/10.1056/NEJM197811022991804
- [M] Edwards (1968) Conservatism in human information processing (no URL; memory)
- [V] Gigerenzer and Hoffrage (1995) How to improve Bayesian reasoning without instruction. https://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf
- [V] Schulz, Wegwarth, Giese (2025) Risk expression using likelihood ratios and natural frequencies. https://pmc.ncbi.nlm.nih.gov/articles/PMC11980142
- [V] Feufel et al. (2023) Boosting for insight and/or for agency? https://pmc.ncbi.nlm.nih.gov/articles/PMC9903474
- [V] Cui, Lo, Liu (2023) Visualizations to improve Bayesian reasoning, review. https://pmc.ncbi.nlm.nih.gov/articles/PMC10059693 (Binder 2015, Yamagishi 2003, Sirota 2015, Brase 2021, Mellers and McGraw 1999 are secondary reports here)
- [V] Mandel, Karvetski, Dhami (2018) Boosting intelligence analysts' judgment accuracy. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/1530E9DAE8F42B2E8FC2B5FE374DB50F/S1930297500006628a.pdf/boosting-intelligence-analysts-judgment-accuracy-what-works-what-fails.pdf (journal page https://dlab.sauder.ubc.ca/sjdm/journal/18/18803/jdm18803.html)
- [V] Qiu et al. (2025/26) Bayesian Teaching Enables Probabilistic Reasoning in LLMs. https://arxiv.org/abs/2503.17523
- [V] Falck, Wang, Holmes (2024) Is In-Context Learning in LLMs Bayesian? https://arxiv.org/abs/2406.00793
- [V] Xie et al. (2022) In-context Learning as Implicit Bayesian Inference. https://arxiv.org/abs/2111.02080
- [V] Zhu and Griffiths (2024) Eliciting the Priors of LLMs. https://arxiv.org/abs/2406.01860
- [V] Zheng et al. (2024) LLMs are not robust multiple choice selectors. https://arxiv.org/abs/2309.03882
- [V] Wang et al. (2023) Self-Consistency. https://arxiv.org/abs/2203.11171
- [V] Tian et al. (2023) Just Ask for Calibration. https://arxiv.org/abs/2305.14975
- [V] Kadavath et al. (2022) Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
- [V] McCoy et al. (2023) Embers of Autoregression (abstract and contents only). https://arxiv.org/abs/2309.13638
- [V] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576 (c21 read; a29 was title page only)
- [M] Griffiths et al. (2023) Bayes in the Age of Intelligent Machines. https://arxiv.org/abs/2311.10206
- [M] Ramsey (1926); de Finetti (1937). https://doi.org/10.1017/CBO9780511641947 (via SEP)
- [M] Lewis (1999); Teller (1973). https://doi.org/10.1017/CBO9780511625343.024 (via SEP)
- [V] Gupta et al. (2025) Enough Coin Flips Can Make LLMs Act Bayesian. https://arxiv.org/abs/2503.04722
- [V] Chen et al. (2026) LLMs are not (consistently) Bayesian. https://arxiv.org/abs/2605.06915
- [V] Filbry, Melo, Gal (2026) From Prompts to Posteriors. https://arxiv.org/abs/2610.29331
- [V] Large Language Models as Discounted Bayesian Filters. https://arxiv.org/abs/2512.18489
- [V] Vision-Language Models Integrate Conflicting Evidence Like Biased Bayesian Observers. https://arxiv.org/abs/2610.19407
- [V] Feng, Zhou, Lin, Roth (2025) BIRD. https://arxiv.org/abs/2404.12494
- [V] Arora, Jurafsky, Potts, Goodman (2025) Bayesian scaling laws for in-context learning. https://arxiv.org/abs/2410.16531
- [V] Zhao, Wallace, Feng, Klein, Singh (2021) Calibrate Before Use. https://arxiv.org/abs/2102.09690
- [V] Paruchuri et al. (2024) What Are the Odds? https://arxiv.org/abs/2406.12830
- [V] Do Chains-of-Thoughts of LLMs Suffer from Hallucinations, Cognitive Biases, or Phobias in Bayesian Reasoning? https://arxiv.org/abs/2503.15268
- [V] Hagendorff et al. (2023) Thinking Fast and Slow in LLMs. https://arxiv.org/abs/2212.05206 (exact figures not captured)
- [V] Lew et al. (2023) Sequential Monte Carlo Steering of LLMs. https://arxiv.org/abs/2306.03081
- [V] Zhao et al. (2024) Twisted Sequential Monte Carlo. https://arxiv.org/abs/2404.17546
- [V] Halawi et al. (2024) Approaching Human-Level Forecasting. https://arxiv.org/abs/2402.18563
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and cognitive biases in LLMs. https://arxiv.org/abs/2402.09193
- [V] Balepur, Palta, Rudinger (2024) It's Not Easy Being Wrong. https://arxiv.org/abs/2311.07532
- [V] Guda et al. (2025) Quantifying and mitigating selection bias. https://arxiv.org/abs/2511.21709 (setups and abstracts mostly)
- [V] Nafar, Venable, Kordjamshidi (2024) BLInD. https://arxiv.org/abs/2402.09614
- [V] Schrader et al. (2024) QUITE. https://arxiv.org/abs/2410.10449
- [V] Nori et al. (2025) Sequential Diagnosis with Language Models. https://arxiv.org/abs/2506.22405
- [M] Pearl (1988) Probabilistic Reasoning in Intelligent Systems (memory)
- [M] Repo note on Mandel 2018, C:/Users/User/Desktop/AGI/research_notes/single_agent/fields_v2/08_intelligence_analysis/ (earlier claim file; superseded by the opened PDF)

Two numbers still need a PDF check before quoting: Balepur Table 17 accuracies (d12) and the BLInD CoT average (d15).
