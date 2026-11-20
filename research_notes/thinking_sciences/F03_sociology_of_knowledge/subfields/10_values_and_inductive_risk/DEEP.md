# Values and inductive risk: deep document

*Subfield F03.10 of sociology of knowledge. Key works: Rudner (1953), Douglas (2000). Evidence ids a01-a25, b01-b27, c01-c28, d01-d16 and claim ids F03.10-K01 to K26 refer to the jsonl files in this folder. Counting note: RiskEval (b10, b11, b25, c01-c05), BAS (b12, c15, c16) and Kalai et al. (b09, b18, c17) are each ONE paper spread over several lines. "Independent sources" below counts papers.*

## 1. What it is

Inductive risk is the risk of being wrong when you accept or reject a claim on evidence that does not prove it.

No evidence ever fully verifies a hypothesis. So someone must decide "this is strong enough". Rudner (1953) said how strong is enough depends on how bad a mistake would be. A toxic drug ingredient needs far more confidence than a batch of belt buckles. Hence the scientist, as scientist, makes value judgments (a01).

The idea has a plain decision-theory form. Two errors exist: accept a false claim (false positive) and reject a true one (false negative). Each has a cost. The threshold on confidence falls where expected costs are equal. With a miss-to-false-alarm cost ratio lambda, act when confidence exceeds lambda/(1+lambda). At a penalty of 100 that is about 0.99 (K04, c01).

Why it matters for our agent: a thinking agent often has to commit, abstain, escalate or flag. The right confidence bar differs by task. If the bar is fixed by habit, the agent is either reckless on costly errors or timid on cheap ones. Recent LLM studies (2025-2026) show that models mostly do not move the bar when told the cost. This makes the subfield one of the few in F03 with direct, measured LLM results.

Scope limits the philosophers stress (b19, b20): the argument bites for applied decisions with foreseeable practical consequences, where withholding judgment is not an option. It is about binary acceptance acts. Whether it refutes the value-free ideal of science is still contested (K03).

## 2. History and theories in depth

**Rudner 1953 (a01-a04, a25).** Six pages, no experiment, written at the Naval Research Laboratory. Three moves.
1. Science accepts or rejects hypotheses. None is fully verified.
2. So the scientist decides the evidence is enough, and the needed degree depends on the seriousness of a mistake.
3. Choosing a significance level is choosing how often you will accept a false hypothesis. Common levels are 1%, 5% and 0.3%. At 5%, a false hypothesis is accepted about one time in twenty in the long run. He cites Rosander (1951) and Neyman (1950) that these levels have no rigid justification and that which error matters more is subjective.
He raised the Manhattan Project: what probability did the scientists demand for "no uncontrollable chain reaction", and was the question even asked consciously? He pre-empted the "just report probabilities" reply (a03): saying "the probability is p" is itself accepting that claim, so the value decision is only moved one level up (a regress). His remedy (a04): objectivity means being explicit about which value judgments are made. Making them unconsciously leaves part of method uncontrolled. Rudner called it a rational reconstruction, not a description of what scientists do. Describing practice would need sociology and psychology.

**Replies, 1956-1965 (a05, a12, a13, b08; [M] secondary only).**
- Jeffrey (1956): general theories have no single use, so scientists cannot tailor acceptance to consequences. They should assign probabilities and not accept.
- Levi (1960/1962): community standards (for example 5%) fix when a claim counts as established. Also, deciding what to believe is not deciding what to do. Only action needs values.
- Hempel (1965) coined "inductive risk" and separated confirmation from acceptance. Four outcomes: true accepted, false rejected, false accepted, true rejected. The two error cells are the inductive risk. Values do not act as evidence but enter the acceptance rule.

**Douglas 2000 (a06-a10).** *Philosophy of Science* 67(4):559-579. She extends inductive risk beyond the final accept/reject. Non-epistemic values matter at three internal stages: choice of method, characterisation of data (borderline evidence), and interpretation of results. Values act indirectly, as weights on the consequences of error, never as evidence. Three accepted external roles remain: choice of problem, use of technology, limits on methods (for example human subjects).

Her case study is the dioxin rat-liver slides (a07). Kociba's 1978 female rat study had 50 animals per dose group. The same slides were read three times: 1978 original, 1980 for the EPA (Squire), 1990 by seven pathologists commissioned by an industry contractor. Only the classification was redone, not the experiment.

| Dose (ng/kg/day) | 1978 tumour livers | 1980 | 1990 |
|---|---|---|---|
| 1 | 3/50 | 8/50 | 1/50 |
| 10 | 20/50 | (benign 27/50) | 9/50 |
| 100 | 34/50 | (benign 33/47) | 18/50 |

The 1990 consensus was a simple majority, 4 of 7 pathologists. Table text came from garbled PDF extraction, so the control row and the 1980 totals are uncertain (a07 limits). Calling every borderline lesion benign gives fewer false positives, more false negatives, risk underestimated and regulation relaxed (Maine did this after 1990). Calling every borderline lesion malignant does the reverse (a08). Statistical power matters too (a09): a 1% excess cancer rate cannot be detected with 50 rats per group, and a two-year study with 200 rats cost about $3 million (Graham and Rhomberg 1996, in Douglas). More animals lower both errors but cost money, so a balance needs an ethical judgment. Blinding pathologists to dose (a10) stops values acting directly but does not remove the need to weigh error consequences, and only helps if borderline calls are spread evenly.

Douglas gives no loss numbers and did not test whether values changed outcomes. It is a normative argument with a real regulatory case.

**The map of the debate (a11, SEP).** Rudner 1953; Hempel 1965; Jeffrey 1956 and Levi 1960 replies; Douglas 2000 extension; Douglas 2009 direct versus indirect roles; Steele and Winsberg 2012 on value-laden uncertainty; Betz 2013 on hedged statements; Neyman-Pearson framing.

**Recent philosophy (2019-2026).**
- Henschen (2021) argues confidence in the argument is overrated: defenders have not beaten Jeffrey's and Levi's replies (a14; abstract page only).
- Dressel (2022, a15, b05, b19). An idealised Bayesian agent performs action D iff p exceeds t, where t is the probability at which expected utility of acting equals that of not acting. Outcomes split into first-order (truth, error, missed truth, averted error) and second-order (consequences for science and society). A trade-off parameter T in [0,1] weights scientific against extra-scientific utility. Result: descriptively the perfect scientist need not use non-epistemic values, so value-freedom is not refuted. Normatively, some applied cases call for such values, and this avoids wishful thinking. Limits: binary choices, single decisions, no sequences.
- Hatchwell (2024, b06, b23) defends Jeffrey: report credences. She concedes the policy communication step may still fall under the argument and that priors may smuggle in values. Frank (2017) and Steele (2012) say IPCC-style probability statements still involve inductive-risk judgments (b22).
- Uygun Tunc (2025 preprint, a16, b02-b04, b20) rebuilds the argument as two premises (epistemic insufficiency; legitimate value-encroachment) and attacks both. Thresholds are not arbitrary in practice: they vary with sample size and base rate of true hypotheses (5-sigma in particle physics versus 1.96-sigma elsewhere), which is evidence of error-rate calculation. She lists costs of value-set thresholds: who picks the weighting rule (meta-criterion), wishful thinking, belief/action category mistakes, premature closure of debate, Mannheim-style paradoxes. Dressel's Bayesian version avoids wishful thinking (b04). Preprint, authors defend the value-free ideal.
- MacGillivray (2019, b07) argues the whole argument rests on null hypothesis testing, a poor model of risk assessment. He proposes value-neutral inference plus structured decision analysis. Regulators already use cost-benefit reasoning. The Delaney Clause was an absolutist threshold that became untenable. Benchmark of US agencies: upper-bound lifetime incremental cancer risk 1e-6.
- Manski (2026, a17-a19, d10). The usual 5% Type I and 10-20% Type II is arbitrary and ignores loss size. In Wald's decision theory, regret = P(error) x loss when wrong, treating both errors symmetrically and using loss size. He argues this answers Douglas. When evidence fits several theories, the decision maker need not accept one: minimax regret can choose a policy under partial identification. With outcome bounds [LA,UA], [LB,UB], minimax regret picks A if UB-LA < UA-LB. If treatment can be split, it gives B the fraction (UB-LA)/[(UB-LA)+(UA-LB)]. Maximin only looks at the worst outcome.

**Philosophy of ML (c22-c24, c28).** Karaca (2021): classifier construction is underdetermined by data, so error costs (a cost matrix) come from social values. Cost-insensitive training maximises accuracy and hides this. Birch (2023): in disorders-of-consciousness imaging, 16 of 104 patients (15%) were classed as cognitive-motor dissociation, of whom about 5 were likely flukes, so expected false discovery is about 5/16 = 0.31, not 0.05. Bonferroni controls per-patient misattribution but raises false negatives; Benjamini-Hochberg controls FDR but per-patient risk grows with recordings. Biddle (2020) and Sullivan (2022) [M]: values enter ML at framing, data and design.

**Clinical forerunner (d16).** Pauker and Kassirer (1980): treat above a test-treatment threshold, withhold below a testing threshold, test in between. Thresholds come from test reliability and treatment benefit and risk. A derivation, not behavioural data.

**Statistics side (a20-a24, d01-d03).** Conformal prediction and conformal risk control turn the value choice into a parameter (alpha, or a chosen loss). The value judgment is moved to the user, not removed. Section 4 gives the mechanics.

## 3. Core findings with exact numbers

Status key: E = established (more than one independent paper or math), S = single paper, C = contested, N = normative argument only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Acceptance threshold must depend on error cost | Toxic drug vs belt buckles; 5% level = false hypothesis accepted 1 in 20 | Rudner 1953 (a01, a25) | N, widely cited; contested in scope (K01, K03) |
| Optimal threshold from costs | t = lambda/(1+lambda); about 0.99 at penalty 100; Kalai t=0.5/0.75/0.9 for penalties 1/2/9 | b05, b09, c01, c17 | E (K04) |
| Interpretation of the same evidence moved tumour counts | 10 ng: 20/50 (1978) vs 9/50 (1990); 100 ng: 34/50 vs 18/50; $3M for 200 rats | Douglas 2000 (a07, a09) | S, partly garbled table (K02) |
| LLMs ignore stated penalty at high stakes | Policy consistency high at penalty <=5, collapses at >=10 (HLE, GPQA); HLE penalty>=10 consistency 0.119 (DeepSeek-V3.2-Think) to 0.492 (Qwen3-Next-Think), range may be wider (two Gemini rows blank); accuracy and stated confidence flat across penalty 0.1 to 100 | RiskEval, Wang et al. 2026 (b10, b25, c01, c02, c05) | S (K05) |
| Model own-policy utility on HLE is negative | Normalised utility about -0.517 (GPT-5-mini) to -0.862 (Qwen3-Next-Think) at penalty >=10 | RiskEval (b10, b11) | S |
| Code-enforced threshold on the model's own confidence recovers utility | GPT-4.1-mini -0.537 to -0.087; Llama-4-Maverick -0.688 to -0.004; DeepSeek-V3.2 -0.853 to -0.169; Qwen3-Next-Think -0.862 to -0.295; GPT-5-mini -0.517 to -0.169; GPT-5-nano gain +0.313; range of gains +0.313 to +0.685 | RiskEval (b11, c03) | S (K06). Gain is under the model's stated belief; HLE ECE 0.47-0.85, so real gain is smaller |
| A prompt telling the model to use its confidence does nothing | Abstention and regret curves match baseline; consistency shift near zero | RiskEval (c04) | S (K07) |
| Implicit escalation thresholds vary by model | p* about 53% (GPT-5-mini, low) to 91-92% (GPT-5-nano 91%, Llama 4 Maverick 92%); Qwen3.5-9B 56% vs Qwen3.5-397B 81%. Text of the paper says "53% to over 100%" in one place (flag) | Act or Escalate, DosSantos DiSorbo et al. 2026 (c06) | S (K08) |
| Models overconfident about own accuracy | 201 of 304 model-condition pairs (66%); self-estimates 76% (Llama 3.3 70B) to 97% (Mixtral 8x7B) vs actual 75-80%; GPT-5-mini condition gaps -38 to +27 points | c07 | S |
| Cost framing plus reasoning helps; either alone helps little | Qwen3.5-9B at R=4 (threshold 75%): 62.0% base, 63.9% cost, 61.9% thinking, 78.8% both. GPT-5-mini: 64.7%, 75.8%, 73.2%, 87.1% | c08 | S (K09) |
| SFT on expected-cost chain of thought | 100% at ratios 2-50, 100% on held-out MovieLens, about 84% with signal removed | c08 | S, train/test same template |
| Triage: ranking good, operating point poor | AUROC 0.95-0.99; default GPT-5-mini false alarms about 10%, catches about 48% of emergencies; other families 94-100% caught, false alarms 12-28%; 576 variants (64 emergencies) | Yamin et al. 2026 (c09) | S (K10) |
| Stated cost ratio 5 or 10 moves operating point | GPT-5-mini routes about 50% more true emergencies up with no rise in unneeded referrals (original endpoint), about 30% (extended, 1,248 variants); Claude Fable 5 and Sonnet 5 shift the right way but recovered ratios span a narrower range, mainly at 0.1x or 100x; GPT-5.4 follows even at minimal reasoning; GPT-5-mini and DeepSeek with reasoning off barely move | c10, c11 | S |
| External fixed threshold on elicited probabilities is robust | Agreement with prompted regimes 80-100%; needs reviewed cases to set it | c12 | S |
| Mirror test mostly fails in small open models | 2 of 12 model-phrasings pass; 70B FN delta +0.713 (99.9% moved right), FP -0.244 (78.6%); 32B +0.459/-0.672; risk probe AUC about 0.83; shared cost-magnitude component 68-94% | Liu et al. 2026 (c13) | S (K11) |
| Symmetric 1:1 tradeoff wording pushes to low-risk answer | Median log-odds shift -0.375 (Qwen-7B), -0.250 (Llama-8B), -0.375 (Qwen-32B), -1.125 (Llama-70B) | c14 | S |
| Benchmarks reward guessing | 10 leaderboards audited; only WildBench gives minimal IDK credit; HELM Capabilities 4 of 5 scenarios none; pretraining bound: 20% singleton facts gives at least 20% hallucination | Kalai et al. 2025 (b09, b18, c17) | S (K12) |
| Calibration metrics mislead for decisions | AIME GPT-4o 11.7% acc BAS -5.06; GPT-oss 75.0% BAS 0.57; SimpleQA all negative BAS, ECE 49.0-84.2%; isotonic: Llama-3.3-70B BAS -2.97 to 0.02, GPT-4o-mini -3.86 to 0.001; top-k (k=3) elicitation highest BAS | BAS, Wu et al. 2026 (b12, c15, c16) | E with d05, d07 (K13) |
| ECE equal, resolution not | ECE verbal 0.0356, behavioural 0.0427, internal 0.0368; resolution 0.0316, 0.0637, 0.0515; Brier 0.1713/0.1465/0.1524 (verbal/behavioural/internal) | Ghosh et al. 2026 (d05) | S |
| Conformal factuality filter | FActScore 30% to 80% (frequency scoring 25% to 80% keeping about half of claims); NQ 78% to 93% (removes about a quarter); MATH 75% to 95% (removes 10%, +15%); targets 80-90%; most FActScore examples lose 50% of claims at alpha 0.2 | Mohri and Hashimoto 2024 (a22, c18) | E (K14) |
| Conformal risk control | Tumour segmentation FNR target 0.1, achieved 0.0987, sd 0.0114 over 1000 splits (n=1000 cal, 781 val) | Angelopoulos et al. (a20) | S, tight to O(1/n) |
| Conformal coverage spread by calibration size | alpha 0.1: n=20 sd 0.063; 50: 0.041; 100: 0.030; 200: 0.021; 500: 0.013; 1000: 0.009 (p5 0.785, 0.827, 0.849, 0.864, 0.877, 0.884). alpha 0.01 vacuous below n=99. n=10 gives sd 0.083, matching earlier sd 0.09 | d01-d03 (own computation from Beta law) | E on maths (K15) |
| Compositional conformal cascades | Budget 0.45; error risk -1.33 to -2.00 points; accuracy +0.67 to +2.00; weighted cost -30.37% on HellaSwag; calibration 1,275-1,500 items; test only 300 | Sun et al. 2026 (d12) | S |
| Test-time compute raises selective accuracy at a fixed bar | Jeopardy Odds threshold 0.95 (not claimed optimal); R1-32B scales better than s1-32B; models tied at Exam Odds differ at Jeopardy Odds | Jurayj et al. 2025 (b13, b26) | S (K16) |
| Conformal stopping for reasoning | Upper threshold risk = wrong answer; lower threshold risk = giving up on solvable item; confidence and probe signals hold under math-to-science shift, token-count signal does not; 4 models, AIME 1,011, DeepScaleR 1,189, GPQA-D 198 | Wang et al. 2026 (b15, b27) | S |
| Prompt Risk Control | Best-mean prompt broke the toxicity limit (0.925 quantile loss <= 0.05, delta 0.05); PRC prompt kept below; 20 prompts, 3,500 validation points | Zollo et al. 2024 (b14) | S |
| Cost-asymmetric probes | Type-I under 10%, average Type-I reduction 34% | Chaudhary et al. 2025 (c25) | S, needs white-box (K17) |
| Decision risk for NLI | ChatGPT answers an extra 20.1% of low-risk items it had called high-risk, skips a further 19.8% of high-risk errors; RoBERTa decision risk cut 28.3% in-domain, 18.9% out-of-domain; ChatGPT composite risk cut a further 17.9% | Shen and Kejriwal 2023 (b17) | S, old models |
| Decision scaffold | Up to 40% accuracy gain over zero-shot, CoT, self-consistency; two domains | DeLLMa (c21) | S |
| Verbalised confidence unstable across phrasing | 4.0-9.1% of decisions flip at 0.8 (Claude Sonnet and DeepSeek, 99 TriviaQA items); scores move 0.043-0.084; yet AUROC 0.937 (Sonnet), 0.956 (DeepSeek) vs three-sample agreement 0.790, 0.765 | Meyer et al. 2026 (d08) | C (K21) |
| Small Qwen models: no agreement across confidence formats | Spearman -0.069 to 0.086 (gate was >=0.60, falsified); 5 models 0.5B-7B | Ghosh et al. 2026 (d04) | C (K21) |
| Constant confidence gives all-defer | Break-even 0.80 (costs 0/1/5): 7 of 8 prompted LLM conditions defer every ticket; one setting AUROC 0.500; classical model threshold 0.60 cut cost 38.1% (CI 35.7-40.4), wrong routes 15.3% to 3.5%, wins 14 of 16 cost settings; 47,837 tickets | Gupta 2026 (d06, d07) | S (K22) |
| Probabilities incoherent | P(X)+P(not X) misses 1 by 0.064 (typed model), 0.293 first-token or 0.122 verbalised (27B); both statement and negation rejected in 196 of 480 pairs | Li et al. 2026 (d09) | S (K23) |
| Pending state is a move along the frontier | Premature retirement 39.2% to 15.5% at 15.3-point detection cost; 500 pairs; zero retirements in 141 same-conversation non-changes; tuned cascade equals raising threshold (26.8% vs 6.5% dev) | Chen and Le 2026 (d11) | S (K24) |
| Compute converts abstentions into answers | 19,200 traces, 120 problems; advisory 4k beats strict 8k in low config; in high, 0.42 points below strict 32k at 59% of tokens; authors disclaim equal-compute claim | Zhang et al. 2026 (d13) | S (K25) |
| Human baseline: stakes do not change BRD reading | 118 jury-eligible adults; seriousness lowered judged probability of guilt but did not significantly shift BRD interpretation or verdict | Lundrigan et al. 2018 (d14) | S, abstract only (K19) |
| Disclosing values does not raise trust | MTurk N=494 and 482; never more trusted; economic-growth values F(1,483)=5.95, p=0.015 | Elliott et al. 2017 (d15) | S (K26) |

## 4. Mechanisms and models

An engineer can build all of these. They share one shape: a model produces a confidence, code compares it to a cost-derived bar, and a value choice sits in one visible parameter.

**4.1 Break-even threshold.**
- Payoffs: correct = +1, wrong = -P, abstain = 0. Answer iff p*1 - (1-p)*P > 0, so p > P/(1+P).
- Table: P=1 gives 0.50; P=2 gives 0.667; P=3 gives 0.75; P=9 gives 0.90; P=100 gives 0.99. Flag: our evidence lines record Kalai's examples as t=0.75 with penalty 2, but t/(1-t) at 0.75 is 3. Either the line or the paper's example is off. Check the paper before copying numbers (open question 12).
- General cost form: act iff p > cFP/(cFP+cFN) when acting on a claim. For escalation: escalate iff accuracy p < 1 - c/cw (c06: Act or Escalate).
- Code must compute it from the cost numbers. Never hand it to the model (K05, K07).

**4.2 Three levels of control, from weakest to strongest (all measured).**
1. Directive in prompt ("use your confidence"): no effect (c04).
2. Cost framing in prompt plus reasoning: moves behaviour for some models, partial (c08, c10, c11). Prompted ratio is not the realised threshold (critique).
3. External gate: code applies a fixed threshold to elicited probability or confidence. Robust, 80-100% agreement with prompted regimes, and fixes miscalibration by learning a per-model mapping from target ratio to threshold (c12, b11).

**4.3 Recover the threshold map.** Run a sweep of stated cost ratios on reviewed cases. For each ratio, find the confidence cut that maximises utility on those cases. Store the map per model and per reasoning level (c12). Check it is monotone. Non-monotone means the confidence has no usable signal.

**4.4 Conformal claim filter (Mohri and Hashimoto; a22).**
1. Split the answer into sub-claims.
2. Score each sub-claim (frequency of the claim across samples, or self-confidence).
3. On a calibration set with human-checked claims, find the cutoff q such that the proportion of outputs containing a false claim is at most alpha.
4. At run time drop all sub-claims scoring below q.
5. The user sets alpha. That is the value judgment, made visible.
Cost: a calibration set. Use the Beta table in section 3 (n=100 gives sd 0.03 at alpha 0.1; n=200 gives 0.021; alpha 0.01 needs n>=99 just to be non-vacuous). The guarantee is marginal, not per topic, and an imperfect scorer drops true claims (half of FActScore claims at alpha 0.2).

**4.5 Conformal risk control (a20, a21).** Choose any monotone loss and tolerance alpha. The method picks the threshold so expected loss <= alpha with finite-sample guarantee, tight up to O(1/n). Learn-then-Test (a21) does the same as multiple testing. Both need exchangeable calibration data.

**4.6 Conformal stopping for reasoning (b15).** Two thresholds on a signal such as confidence: upper stops when confident (risk is a wrong answer); lower stops unsolvable items early (risk is giving up on a solvable one). Each is calibrated to a user-stated error rate. Tokens are saved where many items are unsolvable.

**4.7 Decision-theoretic scaffold (DeLLMa, c21).** The model lists unknown states and gives probabilities. Utility is elicited by pairwise preference and fitted with Bradley-Terry. Code picks the action with highest expected utility. Caveat: the utility comes from the model's guess, not the stakeholder.

**4.8 Evaluation by decision utility (BAS, c15).** Score answer-or-abstain utility averaged across a range of risk thresholds. It punishes confident errors more than log loss. Report it next to accuracy and ECE. Use isotonic recalibration on held-out data and top-k elicitation (k=3) to raise it.

**4.9 Preconditions before gating on verbal confidence.**
- Spread check: the confidence should take more than 3 distinct values (d07). Constant confidence gives AUROC 0.5 and all-defer.
- Phrasing check: elicit with three equivalent phrasings. Flip rates of 4-9% at 0.8 are normal for strong models (d08). Gate only if rank agreement is high and AUROC above 0.8 on own data.
- Coherence check: ask the claim and its negation; flag if probabilities sum outside 1 +/- 0.1 (d09).
- Mirror test: raise FN cost, then FP cost; shifts must be opposite (c13).

**4.10 Three-way decisions (d11).** Adding "pending" reduces the costly error but only moves along the same frontier. Report its price in the other error.

**4.11 Regret rules when losses are unknown (d10).** Maximin: pick the option with the best worst case. Minimax regret: pick the option minimising the maximum shortfall against the best option in each state. With bounds, rule from section 2. No LLM test exists.

**4.12 Douglas's three internal decision points as logging points.** At method choice, evidence characterisation (borderline calls) and interpretation, log which borderline calls were made and in which direction. Blinding to the hypothesis helps but does not remove the weighting of error consequences (a10).

## 5. What holds up

**Holds up.**
- The decision-theory threshold is maths (K04). It holds.
- Calibration metrics alone mislead for decisions. BAS (b12), ECE-vs-resolution (d05) and the constant-confidence case (d07) agree (K13).
- Conformal guarantees hold marginally with a large enough calibration set, and the spread shrinks like 1/sqrt(n) (K14, K15).
- Test-time compute and abstention interact (b13, d13), though no equal-token penalty test exists.

**Single-study and unreplicated.** All LLM threshold results (RiskEval, Act or Escalate, Yamin et al., Liu et al.) are 2026 preprints, one study each, none replicated. Two have arXiv ids 2608.* and 2609.* and are very recent.

**Conflicts and how they reconcile.**
- RiskEval says models ignore penalties at high stakes. Act or Escalate and Yamin say cost framing plus reasoning helps (GPT-5-mini +22.4 points; ratios 5/10 shift 30-50% of emergencies). Reconciliation: model, reasoning level and penalty size matter (<=5 fine, >=10 breaks). Not a true conflict, but not settled for our agent.
- Yamin reports Claude Sonnet 5 and Fable 5 shift correctly, but recovered ratios differ from stated ones. A prompted ratio is not a realised threshold.
- Verbalised confidence: strong on easy QA (AUROC 0.937-0.956, d08), near zero agreement for small Qwen models (d04). Model scale and task matter.

**Moderators.**
- Penalty size: consistency collapses at >=10 (b25).
- Reasoning: cost framing alone gives +1.9 points on Qwen3.5-9B; with thinking +16.8 (c08).
- Capability: stronger models follow prompted utilities (c11).
- Phrasing: a symmetric 1:1 tradeoff statement alone moves every model toward the low-risk answer (c14).
- Task: easy tasks (GSM8K) test little (b25). Hard tasks (HLE) have ECE 0.47-0.85.
- Domain shift: token-count signals fail across math to science; confidence and probes hold (b27).

**Interventions that worked.** External threshold gate (b11, c12). Cost framing plus reasoning (c08). Fine-tuning on an explicit expected-cost template (c08, same template train and test). Isotonic recalibration and top-k elicitation for BAS (c16). Conformal filtering (a22). Neyman-Pearson probes (c25, white-box only). Classical model with calibration-selected threshold (d06).

**Interventions that did not.** Prompt directive to use confidence (c04). Isotonic recalibration of a constant confidence (d07, AUROC stays 0.500). Pending state beyond a raised threshold (d11). Disclosing values to raise trust (d15). A pre-registered rank agreement of verbal confidence across formats (d04, falsified).

**Philosophical dispute is not resolved.** Jeffrey/Levi/Hatchwell (credences, belief vs action) against Rudner/Douglas. Henschen (2021) says defenders have not answered. Dressel (2022) shows value-freedom is not refuted descriptively, while normatively values may be needed. Tunc (2025) attacks both premises. Manski (2026) offers regret as a decision-theoretic way out. The ML papers assume the decision-theory form without engaging this. Rudner's argument is conditional on acceptance being a binary act.

**Human data.** No study found that scientists or analysts raise acceptance thresholds with stated error cost (K19). The one behavioural experiment opened (d14, N=118) found stakes did not change the reading of "beyond reasonable doubt". Earlier acquittal-bias studies (Simon and Mahan 1971) were not opened. The human baseline is missing, so we cannot say LLMs fall short of people.

## 6. Language models

**Do LLMs move their bar with stated cost?** By default, mostly no, at high stakes.
- RiskEval (c01, c02, c05): 13 penalties from 0 to 100, HLE, GPQA Diamond and GSM8K; 10+ models. Consistency with the optimal rule for own stated confidence is high at P<=5, then drops abruptly at P>=10. Accuracy and stated confidence do not change with penalty. Utility with own policy on HLE: -0.517 to -0.862.
- The failure is in the decision step, not the uncertainty estimate: applying the optimal threshold to the model's own confidence lifts HLE utility by +0.313 to +0.685 (b11). Upper bound only, since HLE calibration is poor.
- A prompt directive does nothing (c04).

**What changed it, by how much.**
- Cost framing plus reasoning: +16.8 points (Qwen3.5-9B, 62.0 to 78.8) and +22.4 points (GPT-5-mini, 64.7 to 87.1) at R=4 (c08).
- Cost ratio 5 or 10 on triage: 30-50% more true emergencies routed up for GPT-5-mini with reasoning (c10). Models with reasoning off barely moved (c11).
- Fine-tuning on expected-cost chain of thought: 100% decision accuracy in-template (c08).
- External threshold: robust, 80-100% agreement with prompted regimes (c12).
- Code gate in RiskEval: see above.

**Claude family.** Evidence is thin. Yamin et al. (c11): Claude Fable 5 and Sonnet 5 shift in the right direction at all reasoning levels, dampened at 0.1x and 100x. Meyer et al. (d08): Claude Sonnet AUROC 0.937 on easy TriviaQA (99 items), phrasing flips 4-9% of decisions at 0.8. Gupta (d07): a Haiku few-shot setting routed 19 of 1,000 tickets at break-even 0.80. No Claude result on open-ended claims. No mirror test on Claude.

**Where do models put the bar on their own?** Escalation thresholds from about 53% to 91-92% by model, not set by size or family (c06). 66% of model-condition pairs are overconfident (c07). In triage, default GPT-5-mini catches 48% of emergencies at 10% false alarms while other families catch 94-100% at 12-28% false alarms (c09). Ranking is good (AUROC 0.95-0.99), so the weakness is the operating point.

**Direction errors.** Small open models respond to the magnitude of a cost statement more than its direction (shared component 68-94%), and a symmetric statement pushes to the low-risk answer. Only 2 of 12 model-phrasings passed the mirror test (c13, c14).

**Benchmarks and training.** Binary grading rewards guessing (Kalai; 9 of 10 audited evaluations give no IDK credit). A model that always guesses beats one that abstains (b18). This is an upstream cause of over-acceptance.

**Confidence signal quality.** Strong models rank correctness well on easy QA (d08) but flip 4-9% of decisions at a threshold on rephrasing. Small models have unstable formats (d04). Sampling agreement has more than double the resolution of verbal confidence in small Qwen models (0.0637 vs 0.0316; d05) but beat by verbal in Claude/DeepSeek easy QA (d08). A constant confidence setting gives AUROC 0.500 and all-defer (d07). Probabilities may be incoherent (d09).

**Calibration size.** For a conformal filter, see the Beta table. LLM cascades used 1,275-1,500 calibration items per dataset (d12).

**Decision scaffolds.** DeLLMa (c21): up to 40% accuracy gain on two domains. Conformal factuality filters (a22): 30% to 80% and similar. Probes (c25): average Type-I reduction 34%.

**Test-time compute.** More reasoning raises confidence in correct answers so a fixed 0.95 bar answers more correctly (b13). Replay of 19,200 traces: most gains at a 4k cap replace abstention with a correct answer (d13). Nobody has tested this under a wrong-answer penalty at equal total tokens.

**Not LLM-tested.** Douglas's internal points (does reframing stakes flip borderline evidence calls?). Disclosure of the error trade-off and who bears it. Minimax regret. Open-ended scientific claims (Rudner's real setting). "Value-laden" in the LLM papers means a stated numeric penalty, not contested social values, so whose values and legitimacy have no LLM test.

## 7. What our agent should take

Schema parts: G = guardrails, S = states, O = operators and code tools, memory = section 5 of the schema.

Important tension: G6 says never abstain on the first pass; submit the best attempt. A threshold gate must not violate that. It applies only at the final commit step (S8), only on tasks that define an abstain or flag option with an explicit cost, and the default output remains the best attempt with a flag.

### Add now (established)

1. **[E] Compute the commit bar in code from stated costs; do not ask the model to apply it.** Bar = P/(1+P) or cFP/(cFP+cFN). Schema part: O at S8 (and S0 reads the cost). Evidence: b05, b09, c01, c17, a18 (K04). Note RiskEval (c04) shows prompting fails; the code route is the only measured one, though from a single paper (K05-K07 are Test first). The formula itself is established. Apply only when the task states an abstain option with a cost.
2. **[E] Report cost-weighted utility beside accuracy and ECE; recalibrate on held-out own-run data.** Schema part: memory (class record, section 5) and logging (section 6). Evidence: b12, c15, c16, d05, d07 (K13). Do not trust ECE alone (equal ECE, 2x resolution gap).
3. **[E] If any conformal filter or calibrated bar is used, report the calibration size and refresh it.** Schema part: G7 (pay for itself) and memory. Evidence: d01-d03, a22, c18, d12 (K14, K15). At alpha 0.1 want n>=200 (sd 0.021); do not use alpha 0.01 below n=99; sd 0.063 at n=20.
4. **[E] Name the error being traded.** When a decision depends on an error trade-off, log which error (false accept or false reject) and the cost ratio used. This is the weakest-claim [E]: Rudner's remedy (a04, Dressel b05). Schema part: logging (section 6). Whether showing it to users helps is untested (see U9), so it is a log field, not a user-facing disclosure.

### Test first (not yet established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Code-enforced threshold beats model self-applied at equal tokens, penalty 1-100 | O at S8 | [S] | b10, b11, c03, c04; K05-K07 |
| Find the penalty where our agent's consistency collapses, and see if S3-S5 reasoning moves it | G / S8 | [S] | b25, c02, c08 |
| Cost framing plus an explicit expected-cost step (compare R x p to 1) | O | [S] | c08 (K09) |
| Per-model threshold map from a ratio sweep | memory | [S] | c12, c09-c11 (K08, K10) |
| Verbal confidence precondition checks (spread, 3 phrasings, negation) before any gate | G | [C] | d04, d07, d08, d09 (K21-K23) |
| Mirror test (raise FN cost, then FP cost) as a regression check | G | [S] | c13, c14 (K11) |
| Abstain as a scored option in our evals | G | [S] | b09, b18, c17 (K12) |
| Conformal claim filter on open-ended outputs | O | [E] on QA, untested on open claims | a22, c18 (K14) |
| Pending state (three-way) versus a raised threshold | S | [S] | d11 (K24) |
| Spend more tokens when stakes are high, then gate | S / G12 | [S] | b13, d13 (K16, K25) |
| Minimax regret across rival hypotheses when losses unknown | O | [S] theory only | d10, a17-a19 (K20) |
| Disclosure of the error trade-off | G | [C] | c22, d15 (K18, K26) |
| Re-grade borderline evidence under high vs low stakes framing (Douglas) | S1/S4 logging | [S] | a07, a08 (K02) |

Not for the schema: probes (needs white-box, K17), fine-tuning on a cost template (we do not train).

## 8. Concrete tests on our bench

All arms at equal total tokens (setup counted, G7). Metric is mean utility = (+1 correct, -P wrong, 0 abstain) with P in {1, 2, 5, 10, 20, 50, 100}, plus accuracy and abstention rate.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Code gate vs prompt | Held-out items with a checkable answer and a confidence field (HLE/GPQA-type; our own hard QA) | A: plain with cost in prompt. B: cost in prompt plus "use your confidence" directive. C: plain answer, confidence elicited, code threshold P/(1+P) | Utility at each P; policy consistency | C beats A and B at P>=10; A and B match each other; gain smaller than RiskEval's +0.3 to +0.7 because of ECE |
| T2 Collapse point | Same items, P grid | Our agent with and without the S3-S5 reasoning stage | P at which consistency falls below 0.7 | Collapse at P about 10 without reasoning; later with it |
| T3 Cost framing x reasoning | Binary act/escalate items with a known R | 2x2: framing off/on x expected-cost step off/on | Decision accuracy vs optimal action | Both gives +15 to +20 points over base; either alone under +4 |
| T4 Confidence precondition | 100 own-run items | Verbal confidence under 3 equivalent phrasings; negation pair | Spearman across phrasings, AUROC, distinct values, P(X)+P(not X) | Pass if rank agreement high (>=0.6) and AUROC >0.8; flips 4-9% at 0.8 expected |
| T5 Mirror test | Vignettes with a tunable FN:FP ratio | Raise FN cost x 11 ratios; then raise FP cost; 3 phrasings | Fraction with opposite signed shifts | Claude should pass more often than the 2 of 12 for small open models |
| T6 Conformal filter size | Multi-claim outputs with human-checked claims | Calibration n = 20, 50, 100, 200 | Coverage sd, retained claims | sd matches 0.063, 0.041, 0.030, 0.021; retain about half of claims at alpha 0.2 |
| T7 Compute x penalty | Items with answers | 2x2: low/high reasoning x P=1/P=20, tokens matched by fewer vs more samples | Utility | Extra compute pays at P=20 by turning abstentions into correct answers; not at P=1 |
| T8 Pending state | Items with a ground truth where "needs confirmation" is allowed | Binary at raised threshold vs three-way at equal detection | Costly-error rate at matched detection | No gain beyond a raised threshold (d11) |
| T9 Disclosure | 50 high-stakes answers | With vs without one-line error-trade disclosure; blind raters | Rater preference, decision loss | Unknown; null possible (d15) |
| T10 Borderline stakes flip (Douglas) | Ambiguous evidence items (image or text) | Same evidence under low vs high stakes framing | Rate of flipped classifications; accuracy | Some flips; if accuracy drops, framing is leaking into evidence characterisation |
| T11 Regret rule | Items with two hypotheses and loss bounds | Maximin vs minimax regret vs plain best guess | Realised regret | Regret rule wins when bounds are wide |

## 9. What does not transfer, and why

- **Human values and legitimacy.** In the LLM papers "value-laden" means a numeric penalty in a prompt. Whose values, public legitimacy and democratic input have no LLM test and no schema slot.
- **Rudner's setting (open scientific claims).** Almost all LLM evidence is multiple-choice or classification QA with verbalised confidence. Open claims are untested.
- **Weights-based methods.** Neyman-Pearson probes (c25), probe-based steering (b16), SFT on cost templates (c08) need white-box access or training. Our agent is a scaffold over an API.
- **The DeLLMa utility function.** Elicited from the model, so values are the model's guess, not the stakeholder's (c21).
- **Penalty as a real cost.** RiskEval penalties are stated in a prompt, not experienced. Behaviour with real consequences may differ.
- **Simple abstention.** G6 forbids abstaining on the first pass. Gate only the final commit and keep the best attempt flagged.
- **Marginal conformal guarantees.** They do not hold per topic or after distribution shift, and they need exchangeable data (a20, a22, c19). Cascade guarantees used a loose 0.45 budget and 300 test items (d12).
- **Human behaviour claims.** No data that scientists actually shift thresholds with cost (K19). The founding philosophy is normative. We cannot claim LLMs "should be like scientists".
- **Philosophy of acceptance.** If acceptance is not binary (credences, Jeffrey), the argument weakens. A scaffold that outputs credence plus a code-applied rule sidesteps the dispute, but the final commit to the user is still a decision.
- **Pending state as a free win.** It sits on the threshold frontier (d11).
- **Value disclosure as trust builder.** Human survey says no (d15).

## 10. Open questions

1. Does a code-enforced threshold beat model-applied thresholds on our agent at equal tokens, for P from 1 to 100 (replicate RiskEval)?
2. At which penalty does our agent's policy consistency collapse, and does the schema's reasoning stage move it?
3. Does our agent's verbal confidence carry enough signal (AUROC) and survive rephrasing? Does isotonic recalibration on its own runs hold across domains?
4. Does our agent pass the mirror test, and how does it vary with phrasing?
5. How many calibration items does a conformal claim filter need for our agent, in practice? (Maths done: n=200 gives sd 0.021 at alpha 0.1.)
6. Do humans (scientists, analysts) shift acceptance thresholds with stated error cost? A human baseline would let us judge LLMs fairly.
7. Does disclosure of which error was traded and who bears it improve user decisions, rated blind?
8. Does cost framing plus reasoning replicate for Claude-family models and for open-ended claims?
9. How should thresholds be chosen when losses are unknown or contested (Manski minimax regret vs maximin), and can an LLM apply the rule reliably?
10. Does test-time compute at a high threshold pay for itself in abstentions at equal total tokens?
11. Reconcile prompted ratio versus realised threshold (Yamin): how large is the gap for our agent?
12. Does the Kalai convention for t and penalty (t/(1-t)) match P/(1+P)? Check the paper's scoring before copying numbers (see 4.1).

## 11. Sources

[V] = opened and read this session (full text or substantial text). [M] = snippet or secondary only.

Founding and philosophy
- [V] Rudner (1953) The Scientist Qua Scientist Makes Value Judgments. https://www.inters.org/files/scientist-qua-scientist.pdf (a01-a04, a25)
- [M] Hempel (1965) Science and Human Values, via Douglas (a05). https://mail.joelvelasco.net/teaching/120/douglas00-inductiveriskvalues.pdf
- [M] Jeffrey (1956); Levi (1960/62) via SEP and Hatchwell (a12, a13, b08). https://plato.stanford.edu/entries/scientific-objectivity/
- [V] Douglas (2000) Inductive Risk and Values in Science. https://mail.joelvelasco.net/teaching/120/douglas00-inductiveriskvalues.pdf (a06-a10)
- [V] Stanford Encyclopedia of Philosophy, Scientific Objectivity (summary read). https://plato.stanford.edu/entries/scientific-objectivity/ (a11)
- [M] Henschen (2021) How strong is the argument from inductive risk? Abstract page only. https://kops.uni-konstanz.de/entities/publication/0b4a0644-1dcc-44f1-8430-ac40762ffaf1/full (a14)
- [V] Dressel (2022) Inductive risk: does it really refute value-freedom? https://philsci-archive.pitt.edu/20990/1/def_22795_Dressel_Theoria37-2.pdf ; https://doi.org/10.1387/theoria.22795 (a15, b05, b19)
- [V] Hatchwell (2024) Individual values and inductive risk. https://link.springer.com/article/10.1007/s11229-024-04674-0 (b06, b23)
- [V] Uygun Tunc (2025 preprint) Is the value-free ideal untenable? Part I. https://philsci-archive.pitt.edu/25196/ (a16, b02-b04, b20)
- [M] Elliott (2022) via Tunc (b21); Steele (2012), Betz (2013), Frank (2017) via Hatchwell (b22).
- [V] MacGillivray (2019) Null hypothesis testing is not scientific inference. https://pmc.ncbi.nlm.nih.gov/articles/PMC6850348 (b07; last 17,627 characters unread)
- [V] Manski (2026) Coping with inductive risk when theories are underdetermined. https://arxiv.org/abs/2602.00355 (a17-a19, d10)
- [V] Birch (2023) Medical AI, inductive risk and communication of uncertainty. http://philsci-archive.pitt.edu/22305/1/Birchrisk.pdf (c22)
- [V] Karaca (2021) Values and inductive risk in ML modelling. https://link.springer.com/article/10.1007/s13194-021-00405-1 (c23)
- [M] Biddle (2020) On predicting recidivism. https://www.cambridge.org/core/journals/canadian-journal-of-philosophy (c24)
- [M] Sullivan (2022) Inductive risk, understanding, and opaque ML. https://philarchive.org/archive/SULIRU (c28)
- [V] Rathkopf (2025) From hallucination to reliability. https://arxiv.org/abs/2504.08526 (c26; no inductive-risk content)
- [V] Li, Yi, Chen (2025) Beyond accuracy: hallucination and regulation. https://arxiv.org/abs/2509.13345 (c27; no inductive-risk content)
- [V] Pauker and Kassirer (1980) Threshold approach to clinical decision making (abstract). https://pubmed.ncbi.nlm.nih.gov/7366635/ (d16)

Human behaviour
- [V] Lundrigan, Dhami, Mueller-Johnson (2018) Acquittal biasing effect of offence seriousness (abstract). https://doi.org/10.1080/13218719.2018.1478334 (d14)
- [V] Elliott, McCright, Allen, Dietz (2017) Values in environmental research. https://doi.org/10.1371/journal.pone.0186049 (d15)

Statistics and conformal methods
- [V] Angelopoulos, Bates, Fisch, Lei, Schuster (2025) Conformal risk control. https://arxiv.org/abs/2208.02814 (a20)
- [V] Angelopoulos et al. (2022) Learn then Test. https://arxiv.org/abs/2110.01052 (a21)
- [V] Angelopoulos and Bates (2021) Gentle introduction to conformal prediction. https://arxiv.org/abs/2107.07511 (d01-d03; derived table is our own computation)
- [V] Quach et al. (2024) Conformal language modeling. https://arxiv.org/abs/2306.10193 (a23)
- [V] Mohri and Hashimoto (2024) LMs with conformal factuality guarantees. https://arxiv.org/abs/2402.10978 (a22, c18)
- [M] Candes et al. (2024) LLM validity via enhanced conformal prediction. https://arxiv.org/abs/2406.09714 (c19)
- [M] Rubin-Toles et al. (2025) Conformal LM reasoning with coherent factuality. https://arxiv.org/abs/2505.17126 (c20)
- [V] BlackRock authors (2024) How to choose a threshold for an evaluation metric for LLMs. https://arxiv.org/abs/2412.12148 (a24; tables garbled)
- [V] Zollo et al. (2024) Prompt risk control. https://arxiv.org/pdf/2311.13628 (b14)
- [V] Wang et al. (2026) Conformal thinking. https://arxiv.org/pdf/2602.03814 (b15, b27)
- [V] Sun et al. (2026) Compositional conformal risk control for cascades. https://arxiv.org/abs/2611.11114 (d12)
- [V] Einbinder et al. (2026) Selective safety steering. https://arxiv.org/pdf/2605.14746 (b16)
- [V] Shen and Kejriwal (2023) Risk-aware robustness of LLMs. https://arxiv.org/pdf/2310.03283 (b17)
- [V] Chaudhary et al. (2025) LLM representations for asymmetric error classification. https://ggndpsngh.github.io/files/asymmetric.pdf (c25)

LLM threshold and decision studies
- [V] Wang, Zhou, Devic, Fu (2026) Are LLM decisions faithful to verbal confidence? (RiskEval). https://arxiv.org/abs/2601.07767 (b10, b11, b25, c01-c05)
- [V] DosSantos DiSorbo et al. (2026) Act or escalate? https://arxiv.org/abs/2604.08588 (c06-c08)
- [V] Yamin, Kelly, Wilder, Horvitz (2026) High-stakes decisions with LMs: emergency triage. https://arxiv.org/abs/2608.01361 (c09-c12)
- [V] Liu, Ding, Barrett et al. (2026) Misaligned clinical risk classification and cost asymmetry. https://arxiv.org/abs/2609.23999 (c13, c14)
- [V] Wu et al. (2026) BAS. https://arxiv.org/abs/2604.03216 (b12, c15, c16)
- [V] Kalai, Nachum, Vempala, Zhang (2025) Why language models hallucinate. https://arxiv.org/abs/2509.04664 (b09, b18, c17)
- [V] Liu, Fu, Yogatama, Neiswanger (2025) DeLLMa. https://arxiv.org/abs/2402.02392 (c21)
- [V] Jurayj, Cheng, Van Durme (2025) Is that your final answer? https://arxiv.org/pdf/2502.13962 (b13, b26)
- [V] Ghosh, Kumar, Garg (2026) Measurement validity of confidence signals. https://arxiv.org/abs/2610.25846 (d04, d05)
- [V] Gupta (2026) Cost-aware abstention for ticket classification. https://arxiv.org/abs/2610.31657 (d06, d07)
- [V] Meyer et al. (2026) Training-free self-reported confidence. https://arxiv.org/abs/2609.20541 (d08)
- [V] Li, He, Li (2026) Do a typed-decision model's probabilities obey the probability axioms? https://arxiv.org/abs/2609.33209 (d09)
- [V] Chen and Le (2026) Suggested is not superseded. https://arxiv.org/abs/2610.15710 (d11)
- [V] Zhang et al. (2026) Budget boundary effects in test-time reasoning. https://arxiv.org/abs/2609.38699 (d13)

Not opened: Simon and Mahan (1971) and earlier acquittal-bias studies (blocked); Pauker and Kassirer full text (403).

Parallel subfields, links only: Debiasing; Verbal confidence; Imprecise credences; Prospect theory and risky choice; Valuation and common currency; Social epistemology of discovery; Judicial bias and noise.
