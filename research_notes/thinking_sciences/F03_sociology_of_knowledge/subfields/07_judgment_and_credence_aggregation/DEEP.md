# Judgment and credence aggregation: deep document

*Subfield F03.07. Built from evidence_a-d.jsonl (a01-a27, b01-b29, c01-c26, d01-d24), claims.jsonl (K01-K36) and critique.md in this folder. Ids in brackets are evidence ids or claim ids. Numbers marked "unverified" were not re-opened and should not be cited.*

## 1. What it is

Judgment aggregation asks one question. Many voters hold opinions. How do we combine them into one group opinion that is rational and, if possible, true?

Three strands matter here.

1. **Logical aggregation (judgment aggregation).** Voters judge several linked propositions, for example premises p and q and a conclusion "p and q". Majority voting on each proposition can give a group view that contradicts itself. This is the doctrinal paradox or discursive dilemma.
2. **Truth-tracking (Condorcet).** If voters are independent and each is right with probability above 1/2, majority accuracy rises toward 1 with group size. If competence is below 1/2, it falls toward 0.
3. **Credence pooling.** Voters give probabilities. We combine them by linear pool (mean), log pool (geometric mean), trimmed mean, median, log-odds mean, or with extremizing.

Why it matters for our agent. Stage S7 (select) combines several attempts into one answer. Guardrail G4 says samples from one model are not independent. G5 says code selects. Every S7 rule is an aggregation rule. The theory tells us when each rule is safe. The data tells us how far LLM samples break the assumptions.

Vocabulary:
- Agenda: the set of propositions being judged.
- Premise-based procedure (PBP): vote on premises, derive the conclusion by logic.
- Conclusion-based procedure (CBP): vote only on the conclusion.
- Proposition-wise majority: majority on every proposition separately.
- Competence: probability a voter is right on a proposition. Independence: voters' errors are not correlated.
- Coverage: chance that at least one sample is right (pass@k). Not the same as vote accuracy.

## 2. History and theories in depth

### 2.1 Condorcet (1785)
Condorcet's jury theorem: n independent voters, each correct with probability p. If p > 1/2, majority accuracy rises toward 1 as n grows. If p < 1/2, it falls toward 0, and one voter is best [a09]. Worked case: n = 3, p = 0.8 gives majority accuracy 0.896 [a09]. Near p = 1/2 the gain grows about with sqrt((2n+1)/pi) times (p - 1/2) [a09].
Extensions: heterogeneous competences (Berend and Paroush 1998) [a09]. Correlated voters (Ladha 1992) and premises not justified at once (Dietrich 2008) are known only from memory here [a10], so no figures are taken from them. Both say mild positive correlation can be survived but strong correlation can leave a group worse than one voter.
List (2008) restates the theorem with explicit competence and independence conditions and compares rules: majority beats dictatorship and unanimity on both positive and negative reliability [a07].

### 2.2 The doctrinal paradox (Kornhauser and Sager 1986/1993)
Three judges vote on p (valid contract), q (breach) and r (liable iff p and q) [a01].
- J1: p=1, q=1, r=1. J2: p=1, q=0, r=0. J3: p=0, q=1, r=0.
- Majority: p=1, q=1, r=0.
- Premise-based gives "liable". Conclusion-based gives "not liable". The verdict depends on the procedure.
The tutorial notes there is no clear understanding of how a court should proceed [a01].

### 2.3 Discursive dilemma (Pettit 2001)
Pettit generalised the case beyond courts [a02]. Agenda {p, p->q, q}.
- J1 accepts p, p->q, q. J2 accepts p, not(p->q), not q. J3 accepts not p, p->q, not q.
- Majority accepts p, p->q and not q. That set is inconsistent although every member is consistent.
This is a fact about the agenda, not only about law.

### 2.4 List-Pettit impossibility (2002)
For agendas that are non-simple and evenly negatable (for example {p, q, p and q} with negations), any aggregation function that accepts every consistent profile (universal domain) and is systematic is dictatorial [a03]. Systematic means the same rule treats every proposition alike and the group view on a proposition depends only on the individual views on that proposition.
Escape routes:
- Restrict the domain. List (2003): if members can be ordered so that each proposition is accepted by an interval of them (unidimensional alignment, like single-peaked preferences), proposition-wise majority is consistent [a08].
- Drop systematicity: use a premise-based rule. Votes on premises decide, the conclusion is derived [a04, a06].
- Drop completeness: allow "no verdict" on some propositions (abstain).

### 2.5 Nehring's Paretian dilemma
Premise-based voting can overturn a unanimous verdict on the conclusion. Example: three judges, three premises (duty, negligence, causation). Each judge rejects a different premise, so all three reject liability. The premise-wise majorities accept all three premises, so the group finds liability against every member [a04]. Only dictatorial rules satisfy independence, monotonicity and unanimity preservation on such agendas [a04].

### 2.6 How often does the paradox occur? List (2005)
List computed the chance that proposition-wise majority is inconsistent on the conjunctive agenda (R iff P and Q) [a05, b25]. Table values (re-verified in the critique):

| Profile | n | P(inconsistent) |
|---|---|---|
| Impartial culture | 3 | 0.0938 |
| Impartial culture | 11 | 0.2157 |
| Impartial culture | 101 | 0.2500 (limit) |
| pTT=0.3, pTF=pFT=0.25, pFF=0.2 | 3 | 0.1125 |
| same | 11 | 0.3211 |
| same | 31 | 0.4979 |
| same | 101 | 0.7113 |
| same | 501 | 0.9754 |
| same | 1501 | 0.9999 |
| pTT=pTF=pFT=0.33, pFF=0.01 | 3 | 0.2156 |
| same | 51 | 0.9757 |

Reading: under a uniform profile the limit is 0.25. Under mild departures it goes to 1. The paradox is not rare in large groups. With premises true and competence low but above chance, the limit is 1. With high competence it is 0 [b25].

### 2.7 Truth-tracking of PBP versus CBP (List 2005)
With independent voters of competence p, q > 0.5 on the premises [a06]:
- PBP reaches the right conclusion with probability tending to 1.
- CBP reaches the right conclusion for the right reasons with probability tending to 0 unless p times q exceeds 0.5. Per-premise reliability must exceed the k-th root of 0.5: 0.71 for k=2 premises, 0.79 for k=3 [a07].
- If P and Q are not both true, CBP reaches the correct "no" faster, regardless of reasons [a06].
- If a voter is right on P exactly when right on Q, PBP and CBP always coincide and no inconsistency occurs [a06].
So premise-based aggregation beats conclusion-based when voters are good at the sub-claims. Conclusion-based is better mainly when the conclusion is false for easy reasons.

### 2.8 Probability pooling
Genest and Zidek (1986) [b26, a11; not opened, theory only]. The linear pool does not preserve independence and is not externally Bayesian. The log pool is externally Bayesian but lacks marginalisation. No pool meets all axioms. Dietrich and List (2016) extend pooling to linked propositions with the same impossibility structure [a12; memory only]. No figures from these two are used.
Extremizing: Satopaa, Pemantle and Ungar (2015) show optimal extremizing of an averaged forecast rises when forecasters share less information [b04]. Lichtendahl et al. (2018): extremize when forecasters use private information (each forecast double-counts the prior); when information is shared, anti-extremizing can be right [d21].

### 2.9 Surprisingly popular
Prelec, Seung and McCoy (2017): choose the answer that is more popular than people predicted. It is claimed to beat majority vote when the crowd is mostly wrong [b27, d08]. The paper is paywalled. The error-cut figure (21.3% in b27) is unverified; the same figure belongs to Lorenz 2011 [d07]. Only a simulation claim was seen: a 90% majority is right about 90% of the time; a 55% majority is not much better than chance [d08]. A learned human aggregator using confidence and meta-cognitive data raised success 20% to 35% over rule-based methods, including SP, on 2,490 human responses [d23].

### 2.10 Diversity
Hong and Page (2004) claimed diverse groups can beat high-ability groups. Later critique says the result rests on restrictive assumptions [b28; memory only]. Not used for numbers.

### 2.11 LLM era (2022 on)
Self-consistency [a13] is Condorcet voting over one model's samples. The literature since asks three things: how far independence fails (Section 6), whether debate adds anything beyond voting, and whether better rules (confidence weights, verifiers, trace readers) beat plain vote.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Doctrinal paradox: premise and conclusion votes disagree | 3 judges; p=1, q=1, r=0 by majority | a01, a02 | Established (theory) |
| Impossibility: universal domain + systematic means dictatorship | Theorem on non-simple, evenly negatable agendas | a03 | Established (theorem) |
| Unidimensional alignment restores consistency | List 2003 Theorem 2 | a08 | Established (theorem) |
| Paradox frequency, conjunctive agenda | IC n=3 0.0938, n=101 0.2500; skewed profile n=101 0.7113, n=1501 0.9999 | a05, b25 | Single source (table re-verified) |
| PBP tends to 1 when p,q>0.5; CBP needs pq>0.5 | thresholds 0.71 (2 premises), 0.79 (3) | a06, a07 | Established (theory) |
| Condorcet: majority beats a single voter only if p>1/2 and independent | n=3, p=0.8 gives 0.896 | a09, a07 | Established (theory) |
| Self-consistency gains over greedy CoT | GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-c +3.9 (PaLM-540B); plain majority GSM8K 74.4 | a13, c08 | Single source (widely reused) |
| Probability-weighting of paths is not better than plain vote | normalised 74.1 vs plain 74.4 on GSM8K; unnormalised 59.9 | c08 | Single source |
| More agents; small model passes large | Llama2-13B + vote 59% vs Llama2-70B single 54% (GSM8K); gains GSM8K +12 to +24, MATH +6 to +10, HumanEval +4 to +9 | a18, b11, c09 | Single source |
| Vote saturates, coverage does not | MATH Llama-3-8B coverage 82.9% (100) to 98.44% (10,000); vote 40.50% to 41.41%; SWE-bench Lite 15.9% to 56% at 250 samples with verifier | b13, c11 | Single source |
| Per-query competence can be below 1/2 | hard query: correct 34% vs wrong 56%; MMLU Physics 53% easy, 47% hard | b12 | Single source |
| LLM errors are correlated | 349 LLMs, 12,032 Qs: wrong-wrong agreement 0.423 vs chance 0.127; Helm about 0.60 vs 0.333; 100% and 97.5% of pairs above chance; one pair 0.9987 | a25, b23, c12 | Single source (re-verified) |
| Repeated samples carry little extra information | ICC 0.50 to 0.93; ten ratings = 1.07 to 1.81 independent; independence model overconfident in 42/42 settings | c14 | Single source |
| Same-model sample error correlation about 0.6; personas do not help | gpt-oss-120b N=5: GPQA 0.633 vs 0.603; LCB-Hard 0.571 vs 0.607 | d11 | Single source |
| Bagging correlated classifiers adds nothing | F1 -0.01; precision/recall +0.00 to +0.01 (about 65,000 headlines) | a26, b24 | Single source |
| Debate vs vote, Qwen2.5-7B, 7-benchmark mean | single 0.7205; debate T=2 0.7377, T=3 0.7112, T=5 0.7050; centralised 0.6551; vote 0.7691 | a15, b17, c15 | Established |
| Debate loses to CoT-SC at equal budget | GPT-3.5/4: debate 18 queries vs SC 20; debate plateaus or falls with budget | d13 | Single source (agrees with others) |
| 23 small models, 5,500+ runs | solo 80.4; debate 84.4; SC-9 84.8; persona debate 81.9; debate 3.4x tokens | d14 | Single source (agrees) |
| Debate gain depends on voiced dissent | gain nearly vanishes when withholding forced to 1 | d15 | Single source |
| Single strong prompt matches discussion | single agent with demonstration reaches the upper bound on FOLIO-wiki | a17, b20 | Contested (few numbers) |
| Du et al. debate gains | arithmetic 67.0 / maj 69.0 / debate 81.8; GSM8K 77.0 / 81.0 / 85.0; MMLU 63.9 to 71.1; chess 29.3 to 45.2 | a14, b21 | Contested (baseline-dependent) |
| Mixed vs repeated best model | Self-MoA +6.6 AlpacaEval, +3.8 avg (MMLU, CRUX, MATH); MoA 65.1% vs GPT-4o 57.5% | a23, a24, b15 | Contested |
| Mixed-model teams lose to roster majority | -1.04 points, 80 teams | d14 | Single source |
| Heterogeneous judge panel beats big judge | PoLL Pearson 0.917 vs 0.817; kappa NQ 0.763 vs 0.627; 7x cheaper | a19, b22, c17 | Established (model-family panels) |
| Same-family clones gain nothing from deliberating | clone d = 0.087 / 0.144 / 0.062, all n.s.; mixed groups squared error 0.164 vs 0.195, d 0.40 | c20 | Single source (preprint) |
| Forecasting crowd | 12 LLMs median Brier 0.20 vs 925 humans 0.19, t(60)=0.19, p=0.850 (31 Qs) | a20, b05, c01 | Single source |
| Averaging model and humans beats model updating | GPT-4 0.17 to 0.14 by updating; average 0.13; Claude 2 0.22 to 0.15; average 0.14 | a21, b06, c03 | Single source |
| Probability aggregators nearly tie | trimmed 0.1649, median 0.1651, geometric 0.1655, mean 0.1656, no ensemble 0.1676, USC 0.1691, crowd 0.1600 | a22, b08, c04 | Established |
| System + crowd average is best | test: system 0.179, crowd 0.149, average 0.146 | c04 | Established |
| Superforecasters beat LLMs | 0.096 vs best LLM 0.122 vs public 0.121 | b09, c06 | Established |
| Extremizing with diverse information | GJP Brier 0.132 mean, 0.128 log-odds, 0.123 model | b04 | Established (humans) |
| Leakage inflates LLM forecasts | cloud vs local Brier gap 35.8% full, 8.9% clean | c19 | Single source |
| Learned aggregation beats means | clean set: logistic 0.241, MLP 0.264, mean 0.313, median 0.343 (mean beat median) | c18 | Single source |
| Confidence-weighted vote (CISC) | cost cut 41% (budget 5) and 46% (budget 10) with P(True); verbal 22% / 30%; plain needs 18.6 samples to match CISC at 10; accuracy gain 1 to 2 points | d01 | Single source |
| Confidence signal can be useless | Qwen3-1.7B P(True) AUROC 0.47 | d05 | Single source |
| Adaptive stopping | math 73.2 to 73.1 accuracy, 40 to 13.8 samples (3.3x); ESC sample cuts 34% to 84% | d02, d03 | Established |
| Agreement share tracks accuracy | GSM8K "highly correlated" (no single number) | d04 | Single source |
| Method-prompt diversity | graph colouring GPT-4: CoT 15, SC-10 23, DIV-SE 97; Blocksworld 4/5: 40.0, 41.2, 69.6 | d09 | Contested (prompt-quality confound) |
| Trace-level LLM synthesis beats vote | SC-MoA vs SC (11 vs 10 calls): BBH-3 86.5 vs 80.4; AIME 91.1 vs 85.6; LCB-Hard 62.6 vs 57.3 | d10 | Single source |
| USC matches exact-match vote | GSM8K 90.2 vs 90.4; MATH 37.4 vs 37.9; code 45.5 vs 45.6 | d18 | Single source |
| Minority flipping is risky | 686 of 1,754 items 2:1; minority right in 175 (25.5%); blind trust -19.16; trained rule +1.71 of 10.0 margin, 39 right flips, 9 wrong | c22, d17 | Single source |
| Delegation on one small model | PPV 42.21% vs majority 40.71% (MMLU-Pro 12,032 Qs, Qwen3-1.7B, 16 voters) | d05 | Single source |
| Weak-verifier ensemble beats vote | Weaver avg 87.7 vs vote about 72.2; first sample 68.4; needs labelled dev set | d19 | Single source |
| False positives cap resampling | best K often under 10 | d20 | Single source |
| Humans: pooling vs best member | pooling beats best only when accuracy gap under 0.1; 101 radiologists / 16,813 diagnoses; 40 dermatologists / 4,320 | b01, d06 | Established (human case) |
| Humans: social influence | N=144; mean closer than individuals only 21.3% (77.1% in log space); decentralised network: SD fell 43%, median error 0.76 to 0.67 SD | b02, d07, b03 | Contested (Lorenz vs Becker) |
| Final-answer vote can be right for wrong reasons | MedQA SC-only wins 40% faithful | d22 | Single source |
| LLMs favour popular wrong options | 66% popular-wrong when all distractors more popular (22 LLMs) | d24 | Single source |
| Consistency checks track Brier; forcing them does not help | correlation 0.92 (conditional, arbitrage, scraped set) | c24 | Single source |

## 4. Mechanisms and models

### 4.1 Condorcet with correlation (implementable)
Majority accuracy for n independent voters of competence p (n odd):
`P_maj(n,p) = sum over k > n/2 of C(n,k) p^k (1-p)^(n-k)`.
For correlated voters use the design effect. If the mean pairwise error correlation is rho, the effective number is
`n_eff = n / (1 + (n-1) * rho)` (this formula is the critique's own arithmetic, not from a paper).
Check: rho = 0.6, n = 5 gives n_eff = 5 / (1 + 4*0.6) = 1.47. This matches the "about 1.5 of 5" from d11. With rho = 0.6 and n = 40, n_eff = 1.62. The ceiling is 1/rho = 1.67. More samples hardly help once rho is about 0.6.
Caution: LLM error correlation is mostly item-level. On easy items every sample is right; on hard items they share the same wrong mode. The better model is per-item competence (4.2).

### 4.2 Per-item competence and the rise-and-fall curve
For item i the samples give a correct-answer share c_i and a leading wrong-answer share w_i. If c_i > w_i, voting helps as n grows. If w_i > c_i (34% vs 56% in the example), more samples lock in the wrong answer [b12]. Overall accuracy is the mean over items. Easy items rise, hard items fall; the sum can rise then fall. The predicted optimum number of calls matched observed data on MMLU Physics, TruthfulQA, GPQA and AVeriTeC [b12].
Implementation: estimate the answer-share histogram from the first k samples; model the lead with a Dirichlet.

### 4.3 Adaptive stopping (Adaptive-Consistency, ESC)
Sample one at a time. After each sample, estimate the probability that the current leader stays the leader under a Dirichlet model of answer counts. Stop when it exceeds a threshold. Cap at max samples (40 in the paper) [d02]. Math 73.2 to 73.1 with 40 to 13.8 samples [d02]. ESC alternative: sample in windows, stop when a window is unanimous. Sample cuts: MATH -33.8%, GSM8K -80.1%, StrategyQA -76.8%, CSQA -78.5%, Coin Flip -84.2%, Last Letters -67.4% [d03]. The rule measures lead stability, not correctness (K27).

### 4.4 Confidence-weighted vote (CISC)
For each sample j with answer a_j and confidence s_j, within one question compute w_j = softmax(s_j / T) with T tuned, sum weights per distinct answer, pick the largest. The within-question normalisation is the key [d01]. Cost saving by signal: P(True) 41%/46%, response probability 22%/31%, verbal 0-100 22%/30% [d01]. Accuracy gain at equal samples only 1 to 2 points. The best-calibrated signal was not the best weight; what matters is ranking right above wrong within a question [d01]. Failure: P(True) AUROC 0.47 on Qwen3-1.7B [d05]. Raw unnormalised probability weighting hurts [c08].

### 4.5 Premise-wise (sub-claim) voting in code
Not tested on LLMs (K35). Design, from theory [a06, a07]:
1. Ask each of N samples for a structured answer: sub-claims s_1..s_k and a final answer.
2. For each sub-claim take the modal value across samples.
3. Derive the conclusion with a code function (for example AND).
4. Also compute the conclusion-wise modal answer.
5. Log disagreement. Count samples whose own sub-claims contradict their own conclusion.
Rule from theory: PBP is safe when sub-claim competence exceeds the k-th root of 0.5 (0.71 for two, 0.79 for three). Below that CBP can still be right, for wrong reasons. If premises are strongly dependent (right on P iff right on Q), the two coincide [a06].
Risk: Nehring's dilemma (PBP overturns a unanimous conclusion) [a04]. Treat "all samples agree on the conclusion but the premise vote differs" as an alarm, not an override.

### 4.6 Probability pooling in code
Inputs: probabilities p_1..p_n from samples (for example six, as in Halawi).
- Mean, median, geometric mean, trimmed mean: within 0.0007 Brier of each other [a22].
- Log-odds mean: `sigmoid(mean(logit(p_j)))`. Extremized: `sigmoid(a * mean(logit(p_j)))`; a > 1 extremizes, a < 1 pulls to 0.5.
- Use a > 1 only when forecasters hold private, differing information [b04, d21]. Samples from one model share nearly all information, so default a = 1 (K32; matches G4 "no extremizing"). No LLM test exists.
- For skewed positive numbers use median or geometric mean (Lorenz: arithmetic mean closer than individuals in 21.3% of cases; log space 77.1%) [d07]. Douven's clean set found the mean beat the median, so check skew [c18].

### 4.7 Surprisingly popular (to pilot)
Ask each sample for its answer and a predicted share of other samples picking each option. For each option compute actual share minus mean predicted share. Pick the largest positive gap. The premise (an informed minority that knows it is the minority) is probably absent when all voters are one model's samples (K36). Untested.

### 4.8 Why debate is a martingale
Choi et al.: when agents update beliefs by talking, the expected belief in the correct answer does not change from talk alone. Gains come from the final vote. A Dirichlet model gives a lower bound on vote accuracy that rises with n [a15, b17]. An oracle-biased update moved MMLU formal logic from 0.5000 to 0.6825, so what helps is a bias toward truth, not talk [b17]. Mansuri: discussion can overturn a wrong initial majority only if the rate of withheld dissent is below a critical rate [d15].

### 4.9 Minority flip gate
In a 2:1 split the minority is right 25.5% of the time (175 of 686) [d17]. A rule must flip only when expected gain exceeds expected loss. Always trusting the minority: -19.16 points. A trained classifier on debate features: 81.2% flip precision (39 right, 9 wrong), net +1.71, recovering 22.3% of the margin [d17]. For one small model, a label-free delegation rule using group answer entropy and reasoning-embedding similarity won 366 questions and lost 185 [K33; d05]. Count right-to-wrong flips as well as wrong-to-right.

## 5. What holds up

### 5.1 Replicated or multi-source
- **Debate adds little beyond vote at equal budget.** Choi (2025), Smit (2024), Zhang (2025), Wang (2024, two papers), Ferreira (2026), Mansuri (2026) agree [a15, a16, a17, b16, d13, d14, d15]. Equal-token tests: debate 18 queries lost to CoT-SC 20 [d13]; solo 80.4, debate 84.4, SC-9 84.8 at 3.4x tokens [d14].
- **Agreement-based stopping is safe.** Adaptive-Consistency and ESC show 2x to 8x savings with under 0.1 point mean loss [d02, d03].
- **LLM error correlation is high.** Kim et al. at scale; Zhang and Martinez on ratings; Lefort on classifier bagging; Fadnavis on samples [a25, c14, a26, d11]. Each number is still from one team.
- **Heterogeneous judge panels help.** PoLL [a19]; deliberating mixed-family groups help, clones do not [c20].
- **Probability aggregators are interchangeable.** Five rules within 0.0042 Brier on validation [a22]. The LLM merge step (USC) is no better [a22]. Averaging system and crowd is best [c04].
- **A real checker beats vote.** Brown (SWE-bench Lite 15.9% to 56%), Weaver, Stroebl [b13, d19, d20]. A weak verifier's false positives cap the gain.

### 5.2 Failures, contradictions and moderators
- **Du 2023 vs later work.** Du reports debate 81.8 vs majority 69.0 on arithmetic and 71.1 vs 63.9 on MMLU [a14]. Later papers find debate shrinks against voting or a strong single prompt [a17, b16]. Likely drivers: baseline strength, model size, tuning. Smit found Multi-Persona improved after hyperparameter tuning [a16].
- **Mixing models.** MoA says mixing helps (65.1% vs 57.5%) [a23]. Self-MoA says repeat the best (+6.6, +3.8) [a24]. Zhang says mixing two models helps debate (Heter-SoM +6.4%, Heter-EoT +8.2%) [b16]. Ferreira's mixed teams lost 1.04 points to roster majority [d14]. Moderator: quality-diversity trade-off [b15].
- **Humans: social influence.** Lorenz: seeing others' estimates narrowed diversity without improving accuracy [b02, d07]. Becker: accuracy improved in decentralised networks and worsened with a biased hub [b03]. Becker was not reopened.
- **Pooling humans.** Pooling beat the best doctor only when the accuracy gap was under 0.1 [d06]. Do not pool a strong solver with weak ones.
- **Confidence weights.** Help when the signal ranks right above wrong within a question (CISC) [d01]. Hurt or useless otherwise (AUROC 0.47 [d05]; unnormalised weighting 59.9 vs 74.1 [c08]). Han 2026: confidence-weighted pooling with some self-weight improved accuracy in LLM networks (star, GPT-3.5: 0.67 to 0.80) [c21].
- **LLM aggregator vs code.** Forecast probabilities: USC 0.1691 worse than trimmed mean 0.1649 [a22]. Reasoning tasks: SC-MoA beat vote by 5 to 6 points [d10]. Task decides (K16 contested).
- **Method-prompt diversity.** Large gain on planning (DIV-SE) [d09], but persona prompts did not lower error correlation [d11] and lowered accuracy in 23 small models [d14]. Part of the DIV-SE gain is prompt quality.
- **Consistency forcing.** Consistency scores correlate with Brier but forcing consistency did not improve forecasts [c24].
- **Voting vs consensus rule by task.** Voting +13.2% on reasoning, consensus +2.8% on knowledge; more rounds hurt [b18, c16]. One team.

### 5.3 Interventions that worked
Plain majority over samples; adaptive stopping; a real verifier or checker; heterogeneous model panels as judges; averaging model with crowd forecast; trace-reading aggregator on reasoning tasks (single team); label-free delegation on one small model (+1.5 to +2.2).

### 5.4 Interventions that did not work
Debate beyond vote; persona prompts for lower correlation; bagging correlated classifiers (F1 -0.01); forcing probabilistic consistency; blind minority trust (-19.16); calibration fixes on a naturally calibrated ensemble (binning, isotonic) [c05]; extra debate rounds (0.7377 at T=2 to 0.7050 at T=5) [b17].

### 5.5 Data quality flags (from critique)
- b27 (Prelec 21.3% error cut) unverified; the same figure belongs to Lorenz.
- a23: MoA 65.1% in abstract vs 65.8% in body. Cite 65.1 with a note.
- a16 / b19 (Smit): dataset mapping unverified; do not cite numbers.
- DCR Table 1 jumps of 30 to 40 points for weak models look too large; unconfirmed [d16].
- Weaver Table 1 and Table 3 disagree on GPQA majority (47.4 vs 44.9); cite averages only [d19].
- a10, a11, a12, b26 to b29 are from memory.

## 6. Language models

### 6.1 Independence is broken
- Across 349 LLMs: when both are wrong they agree 0.423 of the time versus 0.127 by chance. Helm: about 0.60 vs 0.333. 100% of HF pairs and 97.5% of Helm pairs are above chance. Llama 3.2-90B and 3.1-70B agree 0.97. More accurate models are more correlated, even across providers. Features explain 34% to 62% of variance [a25, b23, c12].
- Same-model samples: ICC 0.50 to 0.93 over 52,500 judgments (7 open models 1B to 32B, 3 prompts, 10 samples). Ten ratings = 1.07 to 1.81 independent ratings [c14]. Pairwise error correlation among 5 samples of gpt-oss-120b is 0.57 to 0.63 [d11]. n_eff about 1.5.
- Consequences: judges inflate weaker models [c13]; 20 firms each using a random LLM leave about 20% of applicants excluded vs near 0 for random [c13]; bagging three classifiers gave no gain [a26].
- What did not change it: persona prompts (0.633 vs 0.603) [d11]. What helped some: method prompts on planning [d09] (confounded with prompt quality), different model families [c20, a19].

### 6.2 Voting over samples (Condorcet-style)
- Self-consistency: gains in Section 3 [a13]. Gains saturate quickly within 40 samples [c08].
- Agent Forest: gains grow with difficulty and for weaker models. Relative gains on GSM8K 69% / 37% / 16% for Llama2-13B / Llama2-70B / GPT-3.5-Turbo; on MATH 200% / 120% / 34% [a18].
- On hard items, extra votes lock in the wrong mode [b12]. Majority vote plateaus (40.50% to 41.41% on MATH from 100 to 10,000 samples) while coverage keeps rising [b13].
- Arithmetic task in Choi: single 0.8140, debate 0.7600, vote 0.9900 [a15].

### 6.3 Debate and discussion
See 5.1 and 5.2. Debate adds +3 to +7 points over one answer, ties or loses to vote at matched budget, costs 3.4x tokens and 1.6x wall-clock [d14]. Answer diversity falls from round to round [d13]. Gains need voiced dissent [d15]. Centralised debate was worst (0.6551) [a15].

### 6.4 Confidence and agreement
- Agreement share is a safe stopping signal [d02, d03] and correlates with accuracy [d04].
- Confidence weights save 22% to 46% of samples depending on the signal [d01].
- Small models can have chance-level self-confidence [d05].
- LLMs favour popular wrong options 66% of the time under popularity pressure [d24]; a source of shared wrong modes.

### 6.5 Trace and verifier aggregation
- SC-MoA: an LLM reads all traces; +6.1 (BBH-3), +5.5 (AIME), +5.3 (LCB-Hard) at 11 vs 10 calls; GPQA-Diamond 73.2. Beneficial vs harmful flips at consensus: GPQA 12 vs 5 [d10]. Single team.
- USC: matches exact-match vote; does not scale to many samples [d18].
- Graph self-consistency: SC-only wins on MedQA are 40% faithful; GPQA SC-only wins entirely spurious [d22].
- Verifiers: Weaver 87.7 vs 72.2 with labelled data and 33 verifiers [d19]. Stroebl: false-positive cap, best K often under 10 [d20].

### 6.6 Forecasting
- 12 LLM median Brier 0.20 vs 925 humans 0.19 (31 questions) [c01]; best single GPT-4 0.15, worst Coral 0.38 [b05]. Acquiescence: mean forecast 57.35% (sd 20.93) though 14 of 31 resolved yes [a20].
- Human median shown to the LLM: GPT-4 0.17 to 0.14; simple average 0.13 (t(92)=2.58, p=.011). Claude 2: 0.22 to 0.15; average 0.14 (t(92)=3.53, p=.001) [c03]. Update size correlated with distance to the human median (r=0.88 / 0.87): models moved toward the number rather than weighing evidence [b06].
- Halawi: test Brier 0.179 vs crowd 0.149; accuracy 71.5% vs 77.0%; average of the two 0.146 [c04].
- ForecastBench: superforecasters 0.096 vs public 0.121 vs best LLM 0.122; best LLM without crowd access 0.136 [b09, c06].
- AI-assisted humans: N=991, accuracy up 24% to 28%; superforecasting assistant 41% vs noisy 29% without one outlier [b07].
- Learned aggregation of 15 LLMs on 254 questions (94 clean): logistic 0.241 vs mean 0.313 [c18]. Leakage gap 35.8% vs 8.9% [c19].

### 6.7 Networks and conformity
Han 2026: agents adjust toward the majority. Star topology hub accuracy 0.67 at self-weight 0 to 0.80 at 0.75. Ring m=2 to complete graph m=6 at self-weight 0.25: 0.70 to 0.75. Without confidence weighting accuracy fell in all topologies [c21]. Deliberation across families: individual error fell 0.230 to 0.159; group squared error 0.164 vs 0.195 [c20].

### 6.8 What nobody has measured
No measured doctrinal-paradox rate in LLM output. No premise-wise code vote versus answer vote at equal tokens. No Surprisingly Popular test on one model's samples. No extremizing test on LLM samples. See Section 10.

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Select in code by plain vote over independent samples. Do not use debate as a default. | S7, G5, G9 | [E] | K12, K30; a15, b17, d13, d14, d15 |
| A2 | State which aggregation rule is used and which condition it drops (premise-based drops systematicity). Log per task. | S7 | [E] (theory) | K01, K02; a01-a03, a08 |
| A3 | Treat low modal share as "hard item": escalate, do not vote harder. (Theory is established; the exact gate threshold is not, see T3.) | G4, G12, S7 | [E] theory | K05; a07, a09, b12 |
| A4 | Never read agreement as proof. A stable lead measures stability, not truth. | G4 | [E] | K27; d02, d03 |
| A5 | Use adaptive stopping on the vote (Dirichlet lead or unanimous window). | S7, G12 | [E] | K27; d02, d03 |
| A6 | Where a real checker exists (tests, tools, retrieval) select by checker. Treat same-model self-checks as weak verifiers and cap the sample count (K about 5 where false positives are high). | S4, S7, G3 | [E] | K29; b13, d19, d20 |
| A7 | For probability outputs use a simple code rule (mean, median, trimmed, geometric), no extremizing. | S7, G4, G5 | [E] | K17; a22, b08, c04 |
| A8 | For skewed positive numbers check skew first; prefer median or geometric mean over the arithmetic mean. | S7 | [C] on the choice | K34; d07, c18 |
| A9 | Flip to a minority answer only through a tested gate. Log wrong-to-right and right-to-wrong flips. | S7 | [E] | K33; d17, d05, d16 |
| A10 | If more than one model is ever allowed, use mixed-family panels for judge roles. With one model do not call samples independent. | G4 | [E] | K14; a19, c20, a25 |
| A11 | Use only post-cutoff questions when testing forecast aggregation. | memory/bench | [S] | K25; c19 |
| A12 | When an external anchor (human or crowd value) exists, average with it instead of letting the model update toward it. | S7, S8 | [S], direction replicated | K18; c03, c04 |

### Test first (not yet established; see UNKNOWNS.md)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Premise-wise (sub-claim) code vote versus answer vote on multi-step tasks. | S7, O3 | [S] indirect | K35, K04, K01; d10, d22, a06 |
| T2 | Effective sample size from error correlation; set N from n_eff. | G4, S7 | [S] | K06, K07, K26; a25, c14, d11 |
| T3 | Agreement-bin gating: abstain or escalate under a threshold. | S0, S7, G12 | [S] | K11; b12, d04 |
| T4 | Confidence-weighted vote with within-question softmax. | S7 | [C] | K21, K28; d01, d05, c08 |
| T5 | Trace-reading aggregator (LLM) after the code vote. | S7 | [C] | K16, K35; d10, d18 |
| T6 | Method-prompt diversity versus temperature at equal tokens. | S3, G4 | [C] | K31; d09, d11, d14 |
| T7 | Surprisingly popular on samples. | S7 | [S] | K36; d08, d24 |
| T8 | Log-odds aggregation with a free extremizing factor; expect a at or below 1. | S7 | [S] | K32; d21, b04 |
| T9 | Debate or discussion only with voiced dissent and equal tokens. | S7 | [C] | K13, K30; d15, a14 |
| T10 | Reading sub-steps (faithfulness) as a tie-breaker. | S7, G10 | [S] | K35; d22 |

Note on G4 (current text): "No persona or strategy voters on single-answer problems. No extremizing votes." This subfield supports the persona clause (d11, d14) and the no-extremizing default (theory only, K32). The "strategy" clause is in tension with DIV-SE (d09), which is why T6 is a test and not an addition.

## 8. Concrete tests on our bench

All tests compare arms at equal total tokens (count samples, sub-claim prompts and any aggregator call). Always include a plain single-call arm and a plain majority arm. Use post-cutoff items.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 Premise vs answer vote | Multi-step tasks with 2 to 3 checkable sub-claims (word problems, logic grids, ARC sub-rules, brain teasers) | (a) answer majority over N; (b) code premise-wise majority with derived conclusion over N; (c) hybrid: premise vote, flag when it overrides a unanimous conclusion | Accuracy; rate of samples with sub-claims inconsistent with their own conclusion; rate of premise/conclusion disagreement; who is right when they disagree | PBP at or above CBP if per-premise accuracy exceeds 0.71 (two premises); no gain if premises are strongly dependent |
| B2 n_eff measurement | Any bench with ground truth, 5 to 20 samples per item | temperature only; temperature + method prompts; temperature + persona; separate seeds across sessions | Mean pairwise error correlation rho; n_eff = n/(1+(n-1)rho); accuracy vs n | rho about 0.6 for temperature and persona; method prompts lower rho only if quality holds |
| B3 Agreement-bin accuracy and gate | Mixed-difficulty items | vote at k = 5, 10, 20; split by leader share (bins of 0.2) | Accuracy by bin; gain of k=20 over k=5 per bin; items where more samples hurt | Low-share bins flat or negative; high-share bins saturate; set the gate at the bin where gain turns non-positive |
| B4 Confidence-weighted vote | Math, MMLU-style, BBH | plain vote; verbal 0-100 weighted (softmax T tuned on a dev split); token-probability weighted; P(True) weighted | Accuracy at equal samples; samples needed to match plain vote at 10 | 1 to 2 points, or 22% to 46% fewer samples; none if AUROC near 0.5 |
| B5 Trace-reader vs code vote | Reasoning tasks with exact answers | code vote over N; code vote over N-1 plus one LLM reader over all traces (same total calls) | Accuracy; beneficial vs harmful flips | +5 to +6 if SC-MoA replicates; otherwise no better than vote |
| B6 Log-odds and extremizing | Probability outputs on resolved binary items (post cutoff) | mean; median; trimmed; log-odds mean; log-odds times a in {0.8, 1, 1.2, 1.5} | Brier, log loss, calibration slope | Differences under 0.002 among simple rules; best a at or below 1 |
| B7 Skew check | Numeric estimation tasks | arithmetic mean; median; geometric mean | Median absolute log error | Geometric mean or median wins if samples are right-skewed |
| B8 Minority flip gate | Items with 2:1 or 3:2 sample splits | keep majority; flip by gate (entropy + reasoning similarity); LLM reconciler | Net wins minus losses; minority-right rate | Minority right about 25%; a gate needs wins well above losses |
| B9 Surprisingly popular | Multiple-choice with a popular distractor | modal pick; SP pick (answer + predicted share) | Accuracy; items where they differ | Probably no gain for one model's samples; a gain would appear only on popular-trap items |
| B10 Debate with dissent | Reasoning tasks | N samples + vote; 3 agents x 3 rounds with forced dissent roles, tokens matched | Accuracy at equal tokens | Tie or loss to vote; keep out of the schema unless it wins |
| B11 Verifier cap | Code/math with unit tests, plus a non-code set with a same-model verifier | vote; vote + same-model verifier; vote + real checker | Accuracy; false-positive rate; best K | Real checker wins; same-model verifier gains cap early |

## 9. What does not transfer, and why

- **Human independence experiments.** Kurvers (doctors), Lorenz and Becker (students) used independent people with different information. One model's samples share weights, prompt and training data. Their pooling results do not carry over [b01, b02, b03].
- **Extremizing.** Works for forecasters with private information (GJP 0.132 to 0.123) [b04]. Samples from one model share everything, so the double-counting argument runs the other way [d21].
- **Surprisingly popular.** Needs an informed minority who know the crowd is wrong. One model's samples do not contain one (K36).
- **Hong and Page diversity.** Rests on assumptions that were criticised; diversity of weights is not diversity of prompts [b28].
- **Courts and committees.** Real judges give distinct reasons; our voters are samples. The paradox structure still applies, but its cost is a wrong answer, not a legitimacy problem.
- **Heterogeneous panels.** PoLL, MoA and deliberating mixed families need several model families. Our agent is one model. Prompt diversity is the proxy, and the proxy is weak [d11].
- **Huge-n results.** Brown's 10,000 samples and Agent Forest's 40 are beyond a practical budget. The relevant range is n = 3 to 10.
- **Forecasting benchmarks.** Small sets (31 questions) and training leakage (35.8% vs 8.9% gap) limit transfer [c19].
- **Voting where answers cannot be matched.** Free text needs USC or a reader, which has its own scaling limit [d18].

## 10. Open questions

1. Does premise-wise code voting beat answer voting on LLM samples at equal tokens? What is the doctrinal-paradox rate on multi-step agent output? (Gap 1)
2. What is the ICC across tasks, temperatures and prompts for one model, and can any prompt design lower it without lowering quality? (Gap 2)
3. Where does per-item competence fall below 1/2, and can agreement share predict it well enough to gate abstain or escalate? (Gap 3)
4. Does verbalised or token-level confidence help at equal samples on our models? (Gap 4)
5. What extremizing factor suits correlated LLM samples? Probably 1 or lower; untested. (Gap 5)
6. Does a verifier beat vote outside code and math without labelled data? (Gap 6)
7. Debate vs vote at equal tokens is mostly closed for older and small models. Newer reasoning models are not tested. (Gap 7)
8. Reopen: Genest-Zidek 1986, Dietrich-List 2016, Prelec 2017 (the 21.3% figure), Becker 2017 and Satopaa 2015 beyond recorded numbers, Karger 2025 details. (Gap 8)
9. Does Surprisingly Popular work on a single model's samples? (Gap 9)
10. In a single model's 2:1 splits, can any gate flip safely? He 2026 found 25.5% minority-right for three vendors; DCR harm counts are unreported. (Gap 10)
11. Do reasoning models with long chains show the same error correlation? Most data is from non-reasoning or small models.
12. Does Han 2026's self-weight benefit hold when one model re-reads its own earlier samples? Unknown.

## 11. Sources

[V] opened and read (per evidence file). [M] snippet or memory only.

**Judgment aggregation theory**
- [V] Grossi and Pigozzi (2012) Introduction to Judgment Aggregation (a01-a04): https://www.csc2.ncsu.edu/faculty/mpsingh/local/Social/f25/wrap/readings/Grossi+Pigozzi-Judgment-Aggregation-2012.pdf
- [V] List (2005) The probability of inconsistencies in complex collective decisions (a05, a06, b25): https://personal.lse.ac.uk/LIST/PDF-files/inconsistencies.pdf ; https://philpapers.org/rec/LISTPO-3
- [V] List (2008) Group knowledge and group rationality (a07): https://personal.lse.ac.uk/list/PDF-files/ListEPISTEME.pdf
- [V] List (2003) A possibility theorem on aggregation over multiple interconnected propositions (a08): https://personal.lse.ac.uk/list/PDF-files/PossibilityThm.pdf
- [V] Condorcet's jury theorem, Wikipedia (a09): https://en.wikipedia.org/wiki/Condorcet%27s_jury_theorem
- [M] Ladha (1992) / Dietrich (2008) (a10): https://doi.org/10.1111/j.1540-5907.1992.tb00041.x
- [M] Genest and Zidek (1986) (a11, b26): https://doi.org/10.1214/ss/1177013825
- [M] Dietrich and List (2016) Probabilistic opinion pooling (a12): https://philpapers.org/rec/DIEPOP-2
- [M] Hong and Page (2004) (b28): https://doi.org/10.1073/pnas.0403723101
- [M] Mellers et al. (2014, 2015) (b29): https://pubmed.ncbi.nlm.nih.gov/25987508/
- [M] Prelec, Seung, McCoy (2017) (b27, d08; abstract and preview only): https://www.nature.com/articles/nature21054

**Humans: pooling and influence**
- [V] Kurvers et al. (2016) (b01, d06): https://pmc.ncbi.nlm.nih.gov/articles/PMC4978286/
- [V] Lorenz et al. (2011) (b02, d07): https://pmc.ncbi.nlm.nih.gov/articles/PMC3107299/
- [V] Becker, Brackbill, Centola (2017) (b03; not reopened in critique): https://pmc.ncbi.nlm.nih.gov/articles/PMC5495222/
- [V] Satopaa, Pemantle, Ungar (2015) (b04; not reopened in critique): https://arxiv.org/abs/1406.2148
- [V] Lichtendahl et al. (2018) (d21): https://arxiv.org/abs/1705.02391
- [V] Shinitzky et al. (2022) (d23): https://arxiv.org/abs/2201.08247

**LLM voting, debate and mixing**
- [V] Wang et al. (2023) Self-consistency (a13, b10, c08, d04): https://arxiv.org/abs/2203.11171
- [V] Du et al. (2023) Multiagent debate (a14, b21): https://arxiv.org/abs/2305.14325
- [V] Choi, Zhu, Li (2025) Debate or Vote (a15, b17, c15): https://arxiv.org/abs/2508.17536
- [V] Smit et al. (2024) Should we be going MAD? (a16, b19; numbers not cited): https://arxiv.org/abs/2311.17371
- [V] Wang et al. (2024) Rethinking the bounds of LLM reasoning (a17, b20): https://arxiv.org/abs/2402.18272
- [V] Li et al. (2024) More agents is all you need (a18, b11, c09): https://arxiv.org/abs/2402.05120
- [V] Verga et al. (2024) PoLL (a19, b22, c17): https://arxiv.org/abs/2404.18796
- [V] Wang et al. (2024) Mixture-of-Agents (a23, b14): https://arxiv.org/abs/2406.04692
- [V] Li et al. (2025) Self-MoA (a24, b15): https://arxiv.org/abs/2502.00674
- [V] Zhang et al. (2025) Stop overvaluing multi-agent debate (b16): https://arxiv.org/abs/2502.08788
- [V] Kaesberg et al. (2025) Voting or consensus (b18, c16): https://arxiv.org/abs/2502.19130
- [V] Wang et al. (2024) Reasoning in token economies (d13): https://arxiv.org/abs/2406.06461
- [V] Ferreira, Liu, Zheng (2026) Beyond symmetric agents (d14): https://arxiv.org/abs/2609.35875
- [V] Mansuri et al. (2026) Multi-agent discussion gains less when dissent is withheld (d15): https://arxiv.org/abs/2609.38324
- [V] Han et al. (2026) Conformity dynamics (c21): https://arxiv.org/abs/2601.05606
- [V] The Wisdom of Artificial Deliberative Crowds (2026; authors not extracted) (c20): https://arxiv.org/abs/2609.22497
- [M] Confidence-credibility aware weighted ensembles (2025) (a27): https://arxiv.org/abs/2512.17630
- [M] Yuan et al. (2026) Probabilistic aggregation (c26): https://arxiv.org/abs/2506.14625

**Correlation and independence**
- [V] Kim, Garg, Peng, Garg (2025) Correlated errors in LLMs (a25, b23, c12, c13): https://arxiv.org/abs/2506.07962
- [V] Lefort et al. (2024) Independence in ensemble sentiment analysis (a26, b24): https://arxiv.org/abs/2409.00094
- [V] Zhang and Martinez (2026) Beta-binomial latent class (c14): https://arxiv.org/abs/2510.23874
- [V] Fadnavis et al. (2026) SC-MoA and appendix K (d10, d11): https://arxiv.org/abs/2605.29116
- [V] Hu and Collier (2024) Persona effect (d12): https://arxiv.org/abs/2402.10811
- [V] Naik et al. (2024) DIV-SE (d09): https://arxiv.org/abs/2310.07088
- [V] Abdallah et al. (2026) PopMCQ (d24): https://arxiv.org/abs/2608.29257

**Scaling, stopping, selection**
- [V] Chen et al. (2024) Are more LM calls all you need? (b12): https://arxiv.org/abs/2403.02419
- [V] Brown et al. (2024) Large language monkeys (b13, c11): https://arxiv.org/abs/2407.21787
- [V] Aggarwal et al. (2023) Adaptive-Consistency (d02): https://arxiv.org/abs/2305.11860
- [V] Li et al. (2024) ESC (d03): https://arxiv.org/abs/2401.10480
- [V] Taubenfeld et al. (2025) CISC (d01): https://arxiv.org/abs/2502.06233
- [V] Sakai, Song, Larson (2026) PPV (d05): https://arxiv.org/abs/2606.08098
- [V] He et al. (2026) Minority Sentinel (c22, d17): https://arxiv.org/abs/2606.29270
- [V] Wen et al. (2026) DCR (d16; numbers unconfirmed): https://arxiv.org/abs/2608.15303
- [V] Chen et al. (2023) Universal self-consistency (c10, d18): https://arxiv.org/abs/2311.17311
- [V] Saad-Falcon et al. (2026) Weaver (d19): https://arxiv.org/abs/2506.18203
- [V] Stroebl et al. (2026) Limits of inference scaling through resampling (d20): https://arxiv.org/abs/2411.17501
- [V] Revalor et al. (2026) Graph reasoning coherence (d22): https://arxiv.org/abs/2607.08017
- [V] Karge (2026) Jury theorem for confidence-calibrated agents (c23; abstract and intro only): https://arxiv.org/abs/2602.22413

**Forecasting**
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd (a20, a21, b05, b06, c01-c03): https://arxiv.org/abs/2402.19379
- [V] Schoenegger et al. (2024) AI-augmented predictions (b07): https://arxiv.org/abs/2402.07862
- [V] Halawi et al. (2024) Approaching human-level forecasting (a22, b08, c04, c05): https://arxiv.org/abs/2402.18563
- [V] Karger et al. (2025) ForecastBench (b09, c06, c07): https://arxiv.org/abs/2409.19839
- [V] Douven (2026) Wisdom of LLM crowds (c18, c19): https://arxiv.org/abs/2607.18269
- [V] Paleka et al. (2025) Consistency checks (c24): https://arxiv.org/abs/2412.18544
- [V] Reasoning and tools for human-level forecasting (2024) (c25; abstract only): https://arxiv.org/abs/2408.12036

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 11 established claims: 7 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F03.07-K05** (reworded: the sources support less). Condorcet theorem (Wikipedia, List 2008 for the >1/2 and independence conditions) is stated for equal-competence independent voters; 'only if' is too strong (heterogeneous competence, Berend-Paroush, and correlated cases are not covered), and List 2008 does not state the p<1/2 case. Corrected claim: For independent voters of equal competence p, majority accuracy rises toward 1 with group size if p>1/2; if p<1/2 it falls toward 0 and a single voter is best (Condorcet jury theorem).
- **F03.07-K27** (reworded: the sources support less). Adaptive-Consistency reports 3.3x average (up to 7.9x) with under 0.1% average accuracy drop, but ESC's -33.8% (MATH) is only about 1.5x and ESC reports only 'comparable' accuracy, so '2x to 8x with under 0.1 point loss' for both is wider than the sources. Corrected claim: Agreement-based early stopping cuts samples roughly 1.5x to 8x (Adaptive-Consistency: 3.3x on math on average, up to 7.9x, GPT-3.5 4.4x, with under 0.1% average accuracy drop; ESC: -34% to -84% samples with comparable accuracy). It measures lead stability, not correctness.
- **F03.07-K30** (reworded: the sources support less). Ferreira et al. and Wang et al. support the numbers (+3.3/+6.6/+5.7, 1.6x, 3.4x), but Mansuri et al. show discussion's gain shrinks as dissent withholding rises and can overturn a wrong majority only below a critical withholding rate, not that discussion helps 'only if' dissent is voiced. Corrected claim: Debate versus vote at matched budget: debate is a mild gain over one answer (+3 to +7 points) but ties or loses to independent-sample majority vote and costs 1.6x wall-clock and 3.4x tokens; discussion's gain shrinks as agents withhold dissent, and it can overturn a wrong majority only when withholding is below a critical rate.
- **F03.07-K33** (number corrected). Minority Sentinel's 22.3% is the recovery rate of minority-correct 2:1 cases (39 of 175), not 22% of the oracle margin (net +1.71 of a 10.0-point margin is about 17%); other numbers (-19.16, +1.5/+2.24, 366 vs 185) match. Corrected claim: Flipping to the minority is risky: always trusting the minority costs 19 points, a trained flip rule in a 3-vendor debate recovers 22% of the minority-correct cases (39 of 175) for a net gain of only +1.71 points (about 17% of the 10-point oracle margin), and on one small model a label-free delegation rule adds 1.5 to 2.2 points (366 wins vs 185 losses). An LLM reconciler recovers minority-correct answers on math but with unreported harm counts.
- **F03.07-K02** (now single-source: only one opened source, code check).
