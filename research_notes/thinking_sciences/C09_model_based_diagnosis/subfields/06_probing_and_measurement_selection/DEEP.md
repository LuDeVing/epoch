# Probing and measurement selection: deep document

*Subfield C09.06. Written from evidence_a-d.jsonl (a01-a28, b01-b35, c01-c30, d01-d22), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

The question: when several explanations (hypotheses, faults, rules, candidate answers) still fit the facts, which single test or question should the agent run next?

A good probe splits the surviving hypotheses so that each outcome rules out many of them. A bad probe has the same outcome under all of them. It tells the agent nothing.

Four related framings cover the same idea:

- **Model-based diagnosis (GDE).** Keep a set of candidate fault sets with probabilities. Pick the measurement that leaves the lowest expected entropy over candidates after it is read. de Kleer and Williams, 1987 [a01, b32, c29].
- **Sequential diagnosis and troubleshooting.** Pick the next test or repair to minimise expected total cost, not only entropy. Heckerman, Breese and Rommelse 1995; Breese and Heckerman 1996 [a07, a08, d19].
- **Active learning and generalised binary search.** Pick the query that splits the version space most evenly. Half-split is the equal-probability, equal-cost special case [a10, b19, b35].
- **Bayesian experimental design (BED).** Pick the design with the highest expected information gain (EIG), which equals the mutual information between the unknown and the outcome [a12, b21].

For our agent this is schema state S7 (SELECT). SCHEMA.md already says: "If two rules still fit, look for a counterexample: run the one input where they differ (discriminating test)." This subfield says how to choose that input, when to probe at all, how to price it, and what to do when the hypothesis set is open.

The headline finding for LLMs: **a model asked to "pick the most informative question" does this badly. Sampling candidate questions and hypotheses from the model, then scoring the candidates in code, does much better.** The gain is large for weak or mid-size non-reasoning models on closed hypothesis sets. It is small or unproven for reasoning models, soft answers and open hypothesis spaces.

## 2. History and theories in depth

### 2.1 GDE and minimum-entropy measurement (1987 to 1991)

de Kleer and Williams (1987), "Diagnosing multiple faults", introduced the General Diagnostic Engine. It does two jobs. First, it computes candidates: sets of components that, if faulty, explain the observations. Second, it chooses the next measurement.

The choice rule is minimum expected entropy. For each candidate probe point, take the possible values it could show. For each value, work out which candidates survive and what the probability distribution over them becomes. Weigh by the chance of each value. Pick the probe with the lowest expected entropy afterwards. Prior fault probabilities are assumed independent per component [a01, a02, a27, b32]. The primary paper was not opened by us. All formulas are second-hand from Siddiqi and Huang and later papers.

The entropy is taken over the diagnosis distribution. This is hard when diagnoses are many. de Kleer (1991) "Focusing on probable diagnoses" explains the practical fix [d18]:

- Keep only about 5 leading diagnoses. For an n-bit adder there are 3n-1 minimal diagnoses.
- With a handful of diagnoses, full multi-step lookahead is affordable. With very many, GDE uses one step only.
- Focused ATMS: unfocused implementation exceeds 60 s at about 50 components. The focused one is roughly linear to about 1500 components.
- Tie-break: choose the probe nearest a possibly faulty component.
- Warning: focusing can propose probes far from the true fault.

The 1992 paper "One step lookahead is pretty good" (de Kleer, Raiman, Shirley) is reported by Siddiqi and Huang: focusing on fewer probable diagnoses is cheaper but raises average measurement cost. More diagnoses help the entropy estimate [a26, a25]. We did not open it, so we have no numbers.

### 2.2 Decision-theoretic troubleshooting (1976 to 1996)

Three older results frame the cost side:

- **Hyafil and Rivest (1976):** building the minimum expected-depth decision tree is NP-complete. That is why practice uses greedy rules [a28, b34]. Not opened.
- **Kadane and Simon (1977):** for series-system testing with independent costs, test in order of probability over cost. With equal cost and equal probability this is halving [b35]. Not opened.
- **Heckerman, Breese, Rommelse (1995) and Breese and Heckerman (1996):** under single fault, independent components and fixed observation costs, the minimum expected cost sequence orders components by decreasing p_i / C_io. It needs no decision tree. The system replans after every step. Their printer example: pure repair sequence 13.62 min expected; best single observation then repair 13.71 min; best configuration-then-observe plan 12.98 min [d19, a07]. So observation helped only a little in that model, because repairs were cheap.

The authors flag that the single-fault assumption can compromise cost when there are several faults [a08, a25].

### 2.3 Sequential diagnosis at scale (2010 to 2011)

Siddiqi and Huang (AAAI 2010; JAIR 2011) rebuilt GDE-style probing on compiled d-DNNF representations [a02-a06, a27]:

- Compiled approach matched GDE in measurements on small circuits and ran thousands of times faster. Size 17 double fault: GDE 4.6 measurements, 4103 s; compiled 4.2, 0.01 s [a04].
- Entropy over wires alone was weak. Many unlikely diagnoses distort the estimate. The fix was to combine failure probability with entropy and to prune diagnoses [a03].
- c432 (160 gates), single fault: random order 92.3 measurements, entropy of wires only 42.0, failure probability plus entropy 6.7. Five faults: random 117.8, combined 9.4. c880 five faults: random 306.4, combined 15.8 [a03].
- They state that an optimal sequential diagnosis is a policy (a plan conditioned on earlier outcomes), that it is intractable, and that practice uses a heuristic [a05].

Boundary: noise-free gate-level circuits, faults injected at random, cost = count of measurements [a03, a05].

### 2.4 Active learning theory (2009 to 2017)

Golovin and Krause (2011, final 2017) defined adaptive submodularity [a09-a11, b19, b20, d20]:

- Greedy non-adaptive selection under submodularity gets at least (1 - 1/e) of the best fixed-size set.
- Generalised binary search (GBS), the Bayesian half-split on probability mass, is a special case. Known bounds: O(log |H|) worst case; O(log 1/min p) expected.
- For a uniform prior GBS makes at most (ln(|H|-1)+1)^2 times the optimal expected number of queries.
- For adaptive stochastic minimum-cost coverage: (ln(Q/delta)+1)^2 in general and (ln Q + 1)^2 for self-certifying instances. An earlier single-log claim was found flawed (Nan and Saligrama 2017) and is listed as open [d20].
- With non-uniform costs the greedy rule must use gain per unit cost. A log factor is kept [b20].
- Feige hardness: nothing better than ln Q unless NP is in quasi-polynomial time [d20].

Read this as: greedy is a sound default with a worst-case logarithmic guarantee. It is not a percentage claim. All results need noise-free answers and an exactly known prior. Robustness to a wrong prior is open [a09].

Beck et al. (2021) is a caution from deep active learning for images. Active learning gives 2x to 4x label savings over random with augmentation, but with augmentation sophisticated selection (BADGE) had no consistent gain over plain uncertainty sampling [b29, b30]. Fancy scoring tends to add little over a simple rule once the baseline is strong.

### 2.5 Bayesian experimental design (1956 to 2023)

EIG traces to Lindley (1956). Rainforth et al. (2023/2024), "Modern Bayesian Experimental Design" [a12, b21-b23]:

- EIG is doubly intractable in general. Nested Monte Carlo cannot beat an error rate of O(C^-2/3) in cost C, against O(C^-1/2) for plain Monte Carlo.
- In small discrete hypothesis sets the sum is exact and cheap. This is our case.
- Greedy design ignores effects on later steps. Learned design policies beat greedy in cited studies, partly through non-myopic planning [b22].
- Failure under misspecification: the same wrong model chooses and interprets data. EIG can get stuck querying similar designs [b23].

### 2.6 The LLM wave (2023 to 2026)

Order of events:

1. Zhang et al. 2023 showed raw LLMs are poor at 20 Questions [b05, c23].
2. GATE (Li et al. 2023) showed LM-asked questions beat user-written prompts in elicitation [a13, b27].
3. Piriyakulkij et al. (2023/2024) built the sample-then-score pattern: LLM proposes, code scores by information gain [b12, a14-a16].
4. Uncertainty of Thoughts (Hu et al. 2024) added simulated future answer branches [a17-a19, b01-b04, c20-c22, d01-d03].
5. Grand et al. 2024 (Battleship), Kobalczyk et al. 2025 (task disambiguation), BED-LLM (Choudhury et al. 2025/2026) refined it [a20-a22, b08-b11, b16-b18, c01-c07, d16].
6. MAI-DxO (Nori et al. 2025) applied a scaffold to expensive real diagnosis cases [b24-b26, d04, d05].
7. 2026: critical and boundary work. Kriz et al. found small gains on reasoning models [c12]. Pedrozo et al. found thinking models pick their best candidate in 19-36% of turns [d09]. Chari and Pattanaik found a trap with open hypothesis spaces [d13]. MoBayes moved the whole Bayes loop into code [c17-c19].

## 3. Core findings with exact numbers

"Status" uses [E], [S], [C] as in SCHEMA.md. All LLM-answerer studies use a simulated answerer unless stated.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Code-scored EIG beats prompt-only on 20 Questions | Paper claim +37.4 points avg over Prompt-Only, 5 LLMs (main figure), 3 sets of 100 targets; never decreased. Our mean of 18 Table 1 cells (6 LLMs x 3 sets): Prompt-Only 30.3, CoT 39.5, Split 55.4, Entropy 57.6, EIG 70.7 (gain 40.4; the gap to 37.4 is unexplained). Cells: Animals GPT-4o-mini 44 to 88; Celebrities Mistral-Large 19 to 91; Things GPT-4o 34 to 64; Llama-3.1-8B Animals 8 to 63 | BED-LLM [c01, c07, a20] | [E] (4 sources across K01) |
| Half-split recovers most of the gain | Split gains 25.1 of 40.4 points (about 62%). Animals Qwen2.5-72B: 45 / 87 / 95 (Prompt-Only / Split / EIG). Celebrities GPT-4o: 45 / 63 / 86. Things Llama-3.3-70B: 34 / 46 / 55 | BED-LLM [c02] | [S] |
| Asking the model to pick the best of the same candidates is much worse | Animals Mistral-Large Implicit 53 vs 95; GPT-4o 70 vs 93; Things GPT-4o-mini 25 vs 49 | BED-LLM [c03] | [E] with c04, b05, d10 |
| CoT about the best question does not close the gap | Animals GPT-4o: 45 / CoT 62 / EIG 93. Things Mistral-Large 26 / 29 / 58. Llama-3.3-70B Animals CoT 40 = Prompt-Only 40. CoT beats Split in some cells (Things GPT-4o 49 vs 40) | BED-LLM [c04] | [E] |
| Belief handling is critical | Raw in-context beliefs: Animals GPT-4o-mini 18 vs 88; Celebrities GPT-4o 52 vs 86. Data-Estimation pairing worse than prior-likelihood: Animals Llama-3.3-70B 40 vs 79 | BED-LLM [c05] | [E] with b10 |
| Gain shrinks on soft tasks | Film preference (200 profiles, 5 questions): gain "most clear" only with mismatched questioner/answerer; Prompt-Only stronger there; numbers only in plots | BED-LLM [c06, d16] | [E] direction |
| UoT: relative gain over direct prompting | "38.1%" is a mean of per-cell relative gains. Llama3-70B +46.6% relative = +10.1 points. Others +9.2 to +12.8 points. Open set +9.8 points, closed +10.9; UoT at or below DP in 0 of 40 cells | UoT [d01, d02, a18] | [S] (no independent replication) |
| UoT headline cells (GPT-4) | Common 49.0 to 70.9; Things 30.8 to 36.8; DX 89.4 to 97.0; MedDG 74.9 to 87.9; FloDial 43.7 to 67.3 (appendix 42.5 to 67.8). Llama3-70B open set: DX 26.0 to 35.6; MedDG 25.7 to 50.6; FloDial 11.1 to 26.1 | UoT [c20, b01] | [S] |
| Equal-token test, GPT-4 | 4.5-4.7k tokens (20Q / Dx / troubleshooting): CoT-SC k=33 32.6/37.6/42.5; Original-ToT 23.7/65.3/40.4; Adapted-ToT 33.8/85.1/60.3; Pruned UoT 48.1/88.4/63.2. 9.2-9.3k: Adapted-ToT D=4 40.9/86.7/63.7; UoT D=3 54.4/92.5/66.0 | UoT Table 2 [d02, b03] | [S] |
| Reward choice inside lookahead barely matters | GPT-3.5 (20Q-BIG-bench / Common / DX / MedDG / FloDial): IG 51.7/41.4/90.4/81.1/67.9; UR 51.7/44.2/92.1/81.3/67.1; PFS 37.9/36.9/89.4/81.3/67.1. Swapping ToT self-reward for uncertainty reward: +5.9% | UoT Table 3 [b04, c21] | [S] |
| One-step lookahead gets most of depth 3 | Medical Dx 82.6 to 86.7 to 92.5 at depth 1/2/3; troubleshooting 66.1 to 67 to 67.3; 20Q 63.5 to 64.7 to 75.2. Depth 1 is about 89%, 98%, 84% of depth 3 (series assignment inferred from interleaved text) | UoT App. E [d03] | [S] |
| Un-scaffolded LLMs are poor at 20Q | Success (30 items x 5 runs): GPT-4 0.31 Things, 0.50 Celebrities; GPT-3.5 0.28/0.27; Claude-2 0.21/0.31; Vicuna 7B 0.09/0.06. Human row 0.24 / 0.31. Failure modes: early enumeration, repeated questions | Zhang et al. [b05, c23, c24] | [E] |
| Weak-model gain, strong-model boundary | HumanEval, 4 questions: GPT-3.5 binary 70.8 to 85.6, open 75.9 to 85.0; Llama3-8B binary 53.0 to 65.8. GPT-4o-mini binary 79.6 vs 81.5, open 83.5 vs 83.8. Zero-question accuracy 71.0 (GPT-4o-mini) vs 44.1 (GPT-3.5) | Kobalczyk et al. [b08, b09] | [E] direction |
| Probability source matters | 20Q rank score at 10 questions: Llama3-70B EIG-uniform 6.3, EIG-logprobs 3.9, implicit 5.9, implicit-ToT 5.1. GPT-3.5 6.2 / 4.1 / 4.9 | Kobalczyk et al. [b10] | [S] |
| Open questions beat yes/no | APPS GPT-4o-mini, 4 questions: base binary 62.9, EIG binary 75.3, base open 75.1, EIG open 87.2. Llama3-8B EIG binary 26.9 vs open 50.7 | Kobalczyk et al. [b11] | [S] |
| Selection rule matters more than proposer | Zendo, hard rules, 1/5/10 candidates: random proposer 5.84/6.23/6.55; LLM proposer 5.73/6.19/6.55. Table 3 fuzzy/hard: LLM-chosen 4.52/4.72; random 5.03/5.84; InfoGain 5.35/6.55; humans 5.26. 5 seeds | Piriyakulkij et al. [a14, a15] | [E] (3 sources, K18) |
| Online hypothesis tracking | ActiveACRE (20 tasks): online hard rules 0.35 +/- 0.11 vs batch 0.15 +/- 0.08 vs batch+refine 0.10 +/- 0.07 (alignment inferred) | Piriyakulkij et al. [a16] | [S], tiny n |
| Sampling k questions then scoring (Battleship) | Human mean EIG 1.27 bits, best 3.61 (40 people, 605 pairs). LLM k=1 about 0.65. k=5 near human mean; k=10 above it (p<0.001 CodeLlama, p=0.01 GPT-4). 40% (CodeLlama) / 33% (GPT-4) of valid questions had EIG 0. Only 40-88% translate to valid programs | Grand et al. [b16, b17, c10, c11] | [S] |
| Text-to-SQL clarification ranking | Spider ambiguous subset N=290: execution accuracy EIG 76.6, uniform info gain 73.4, max-probability 72.1, random 70.1. Exact match 38.3 vs 21.0 | Qiu et al. [d15] | [S] |
| Code owns the Bayes loop | DDxPlus n=50/cell: MoBayes + GPT-5.4-nano top-1 78%, selective accuracy 81.2, DHS 88.0; best standalone Gemini 3.1 Pro 60%, 62.5, 75.7. Llama-4-Scout sensor 56% vs GPT-OSS-120B 40%. CI for 78% is 66 to 90 | MoBayes [c17, c18] | [S] |
| Stopping threshold trades coverage for accuracy | Threshold 0: selective accuracy 70, coverage 100; threshold 0.7: 100, 40. Focused top-3 EIG +12 pp top-1 (or up to +7 pp DHS; text inconsistent). k=5 slightly worse than k=3 | MoBayes [c19] | [S] |
| Reasoning models: inference-time BED gains modest, slow | BED-LLM 2376 s per game vs trained AR-BED 38.9 s (61.1x). Worse than non-reasoning base on some domains | Kriz et al. [c12] | [C] |
| Thinking raises per-turn gain, selection stays poor | Guess My City, 120 games per model: Qwen3-30B Instruct win 0.10, 0.14 bits/turn; Thinking win 0.93, 0.42 bits. Max-IG candidate chosen 0.19 to 0.36 of turns | Pedrozo et al. [d09] | [S], checkpoints confounded |
| Reasoning models fail to pick the right single question | QuestBench: over 80% on GSM-Q/GSME-Q; 40-50% on Logic-Q/Planning-Q. BFS on Logic-Q: depth 3 39.0%, depth 5 80.6%, depth 10 99.8% | QuestBench [a23, b13, d10] | [E] |
| Asking by default can hurt | MediQ: ask-allowed is 11.3% relative drop vs no questions; most samples get zero questions. Best abstention (confidence 1-5 + rationale + 3 samples): +22.3% over ask-always, +12.1% over no-ask, closes 51.2% of gap to full info. Rationale: ECE 0.286 to 0.211. Plain self-consistency without rationale degrades. Models above 70B beat no-ask; smaller did not. Threshold tuned on eval data | MediQ [b31, d06] | [E] direction (2 sources); threshold [S] |
| Separate gate in coding agents | Underspecified SWE-bench Verified, 500 tasks, Claude Sonnet 4.5: full spec 70.8; hidden 54.8; interactive baseline 70.4; single-agent self-detect 61.2; two-agent with binary checker 69.4 (p<0.001 vs single; p=0.621 vs interactive) | Edwards and Schuster [d07] | [S] |
| Models know but do not ask | Clarifying-question rate at most about 5% on ambiguous questions; falls with retrieved context | Su and Cardie [d12] | [S] (K24 [E] with MediQ, coding) |
| Reasoning training lowers abstention | AbstentionBench: 20 datasets, 20 LLMs, average drop 24% (abstract only) | Kirichenko et al. [d11] | [S], snippet only |
| Value-of-information gate | Gemini Mixed 20Q, VoI minus best of baselines: c=0.01 +0.34; 0.02 +0.84; 0.05 +1.36; 0.10 -0.90; 0.20 -0.96. GPT-4 Mixed 20Q c=0.01: 14.14 vs 11.49 | Dong et al. [d08] | [S] |
| Sequential diagnosis with a scaffold | 304 NEJM cases (56 held out): o3 78.6% at $7,850; MAI-DxO no budget 81.9% at $4,735 (-39.7% cost, +3.3 pts); budgeted 79.9% at $2,396; ensemble 85.5% at $7,184; GPT-4o 49.3% at $2,745; physicians 19.9% at $2,963 (56 cases, 764 diagnoses). On o3 and o4-mini the accuracy gain was not significant, the cost cut was | Nori et al. [b24, b25, d05] | [S] |
| No ablation of MAI-DxO roles | Variants differ in budget and ensembling only. Panel alone: -39.7% cost, +3.3 pts. Budget tracker: further -$2,339 for -2.0 pts. Ensemble: +3.6 pts at baseline cost | Nori et al. [d04, d05] | [S] |
| Ablation in non-medical troubleshooting | 100 cases, Gemini: Baseline 67.3; Thinking, no questions 67.5; Thinking + interaction 72.8; Ask-5 72.3; ReAct 69.0; ToT 61.5; full SIA 79.2 (CI 72.7-83.7). Remove counterfactual critique 74.0; remove follow-up questions 75.0; remove hypothesis expansion 76.5. Misleading-user stress test 10 pairs: 80.0 vs 76.0 | SIA, Marozzo and Lio [d14] | [S] |
| Priors in classic circuits | See c432 row in section 2.3: 92.3 / 42.0 / 6.7 | Siddiqi and Huang [a03] | [S], not re-checked |
| Cost-ordering proof | Order by p/cost under single fault, independent components. Printer model 13.62 / 13.71 / 12.98 min | Breese and Heckerman [a07, d19] | [E] as theory; LLM test none |
| Open hypothesis space can stall max-information probing | Number Game, queries to converge (EIG / positive-test / random): squares 3/2/2; odd 7/4/2; even <30 17/31/17; digits sum <8 43/DNF/DNF; remainder 5 mod 9 31/DNF/41 | Chari and Pattanaik [d13] | [S] |
| Free prompt rules on probe form | GuessingGame, 858 games: LLaMA-3.3 70B 39.4% standard, 80.0% with repeat-constraint, 97.4% with forced open questions; GPT-4o 64.1% to 98.5%; Gemini Flash-Lite 74.1% to 87.3%. One SD more Bayesian IG cuts game length 43% | Hutson et al. [d17] | [S] |
| Prior ablation (low trust) | Synthetic resumes: empirical prior 176 misclassifications vs uniform 387 | Amin [d21] | [S], low trust |
| Thinking alone without questions adds nothing | SIA: 67.3 vs 67.5. Best-of-35 on static differential: recall 0.537 vs 0.531 baseline, precision 0.403 vs 0.472 | [d14, d22] | [S] |
| Fine-tuning transfer is uneven | DPO on EIG pairs: INLG 56.7 to 68.9; Things 51.1 to 61.1; Celebrities 71.1 to 72.2; BigBench 17.2 to 31.0. ASIG (RL) 7B: MediQ +0.9 points; Kriz: dermatology 90.5 to 94.7 | [c08, c13, c16, c15] | [C], training-based |

## 4. Mechanisms and models

This section is written so an engineer can build it. The common pattern is **propose with the model, score with code, update with code.**

### 4.1 The core loop

State kept by code, not by the model:

- `H`: a list of hypotheses (candidate rules, suspect faults, candidate answers). Each has a weight `w_h`.
- `Q`: a list of candidate probes (questions, tests, inputs).
- `history`: every probe run and its observed answer.

One round:

1. **Sample hypotheses.** Ask the model for N hypotheses given the task and history (N about 10 to 100; BED-LLM found the ranking of 5 candidate questions at 10 sampled hypotheses already matched that at 85 [d16]). Filter each hypothesis against the full history. Drop any that contradict an observed answer. Raw in-context beliefs collapse (18 vs 88) [c05].
2. **Weight them.** Use uniform weights over the sampled, history-consistent hypotheses. Do not use the model's own log-probs: 3.9 vs 6.3 rank score [b10]. If a real prior exists (failure rates, past bug history), multiply it in (section 4.5).
3. **Propose probes.** Ask the model for K candidate probes (K = 5 to 10; more helps: 5.84, 6.23, 6.55 for 1, 5, 10 in Zendo [a15]). A cheap hand-made generator works as well when one exists [a15].
4. **Score each probe in code.** For each probe q and each hypothesis h, get the predicted outcome o(h, q). This is the step that needs a predictor: run the code (ARC, debugging), look up a table, or ask the model "what would h predict for q?" Then compute the score below.
5. **Pick the best probe** (subject to cost, gate and form rules). Run it for real. Record the answer.
6. **Update.** Drop hypotheses that contradict the answer, renormalise. Stop when one hypothesis has posterior above threshold, or the budget is spent.

### 4.2 Scores

Let `p(o | q)` be the weight of hypotheses predicting outcome `o`, and `H(.)` the Shannon entropy [a27]: `H(X) = -sum p log p`.

- **Half-split.** Choose q whose outcome classes are closest to equal weight. For binary outcomes: minimise `|weight(o=yes) - 0.5|`. UoT's reward for a yes/no question is `IG = -pA log pA - pN log pN` [a17]. For deterministic answers this equals maximising the marginal entropy of the answer.
- **Entropy of the answer.** `H(O | q) = -sum_o p(o|q) log p(o|q)`. Equal to EIG when answers are deterministic given the hypothesis.
- **Full EIG.** `EIG(q) = H(O | q) - sum_h w_h * H(O | h, q)`. The second term is the expected answer noise. It matters only when answers are noisy. BED-LLM showed Entropy-only fails on questions with noisy answers [a21]. If answers are deterministic, drop the second term and use entropy (or split).
- **Cost-weighted.** Score `EIG(q) / cost(q)`. Golovin and Krause require gain per unit cost for non-uniform costs [b20]. For single-fault ordering of component checks, use `p_i / C_i` descending [a07].
- **Expected entropy after probe (GDE form).** `E[H(post) | q] = sum_o p(o|q) H(w | o)`. Choose the smallest. Equivalent to maximal EIG.

Three tie-breaks from the literature: prefer the probe nearest a suspect component (de Kleer) [d18]; prefer an open question to yes/no when the answerer can handle it (it carries more information: +12 points on APPS GPT-4o-mini [b11]); prefer a probe type not yet used (section 4.7).

### 4.3 Lookahead

- One step is the default. de Kleer used one step when diagnoses are many [d18]. In UoT, one step reached about 84 to 98% of the depth-3 result [d03].
- Two steps matter only when a test is useless alone but enables a later one (Kriz Cube-NM style task, appendix numbers unread) [c14].
- UoT's simulated tree: for each candidate question, simulate each answer branch, then the next question, to depth 3. Score by summed probability-weighted information gain. Costly in tokens (4.5k to 9.3k per game with GPT-4) [d02].

### 4.4 The gate: when to probe at all

Evidence says self-initiated asking is poor in both directions. Models rarely ask when they should (about 5% at best [d12]; zero questions in most MediQ samples [d06]). They ask badly when they do (MediQ -11.3% relative [d06]). Reasoning fine-tuning lowers abstention [d11].

Two gates have been measured:

- **Confidence gate (MediQ).** Before each turn, the model rates confidence 1-5 and writes a rationale; repeat 3 times; ask only if the (aggregated) confidence is below a threshold. Threshold grid-searched [d06]. Without the rationale, self-consistency alone degrades.
- **Separate binary check (coding).** An independent call answers only "is this underspecified?" and, if yes, forces the next action to be a question. 61.2 to 69.4 resolve rate [d07].

A third, untested-in-agents, rule is **value of information**: probe if `expected utility gain > cost of the probe`. Matched or beat tuned thresholds at low cost, lost at high cost [d08].

For our agent, the cleanest gate is computed from the hypothesis set: probe when the leading hypothesis has a posterior share below a set value, or when two or more surviving hypotheses disagree on a fresh input. This is a code check, consistent with SCHEMA G1 (doubt only on a signal). No paper tests exactly this gate.

### 4.5 Priors and cost

Where priors come from:

- GDE: a device model gives per-component failure rates [a01, d19].
- Siddiqi and Huang: failure probability plus entropy cut measurements from 42.0 to 6.7 [a03].
- LLM agents: nothing tested except a synthetic study [d21]. A plausible source for debugging is repository history (which files change, which tests fail often). That is a test, not a fact (UNKNOWNS U5).

Cost model for a probe: tokens, wall-clock, dollars, irreversibility. Order checks by `p / cost` when one fault is likely and checks are independent. Otherwise use `EIG / cost`.

### 4.6 Putting Bayes in code (MoBayes pattern)

The LLM is a "sensor" only. It turns free-text answers into structured observations (symptom present / absent / unknown). Code holds a table of likelihoods `P(symptom | disease)`, updates the posterior, chooses the next question by EIG, and stops at a threshold [c17-c19]. Focus EIG on the top 3 suspects; focusing on 5 was slightly worse and too strong a focus hurt [c19]. Needs a knowledge base of likelihoods. In MoBayes the KB itself came from an LLM, and the gain held at about 10x lower cost [c18].

### 4.7 Cheap form rules

GuessingGame found that rules on question form alone moved success from 39.4% to 80.0% (no repeated question types) and 97.4% (forced open questions) on LLaMA-3.3 70B [d17]. The base model was falling into enumeration (guessing items one by one), the same failure Zhang et al. saw [b05]. So a rule set costs nothing in tokens: forbid repeating a question type; forbid naming a specific final answer before the hypothesis set is small; forbid asking an already answered question. These belong in the baseline arm of any test.

### 4.8 Falsification probes (a separate idea)

Max-entropy probes split the hypotheses. Falsification probes aim at the leader: "what test would break our current best?" MAI-DxO's Dr. Challenger does this by LLM judgment [d04]. SIA's counterfactual role costs 5.2 points when removed [d14]. The Number Game shows that probing the top hypothesis (positive test) is fast on easy rules and fails to falsify on compound rules (digits sum <8: EIG 43, positive-test did not finish) [d13]. A switch rule (safe positive probes first, falsifying probes when stalled) was proposed and not tested [d13]. This links to the fixation subfield.

## 5. What holds up

### 5.1 Replications and independent confirmations

- **Code-side scoring beats model-picked questions.** Seen in BED-LLM (20Q), UoT (20Q, diagnosis, troubleshooting), Kobalczyk (code tasks), Qiu (SQL), Grand (Battleship), MoBayes (diagnosis) [c01, c20, b08, d15, b16, c17]. Different authors, tasks and formats. Rating [E] for the direction.
- **Un-scaffolded LLMs choose probes poorly.** Zhang (2023), QuestBench (2025), Pedrozo (2026), Grand (2024) [b05, d10, d09, c11]. [E].
- **Selection rule over proposer.** Zendo, Battleship and task disambiguation all show candidates matter less than scoring [a15, b16, b08]. [E].
- **Weak-model benefit, strong-model boundary.** Kobalczyk, BED-LLM Table 1 (Llama-3.1-8B 8 to 63), Kriz, MediQ model-size split (above 70B only) [b09, c07, c12, d06]. [E] direction.
- **Self-initiated asking is poor.** MediQ, Su and Cardie, coding agents, AbstentionBench [d06, d12, d07, d11]. [E] for non-reasoning models.

### 5.2 Single-source or unreplicated

- UoT: no independent replication found [d01]. The 38.1% was misread easily as points; real figure about +10 points.
- BED-LLM's 37.4 average does not reproduce from our recount of Table 1 (40.4) [critique].
- Half-split at 62% of full gain: one paper [c02].
- MoBayes: n=50 per cell, wide CIs [c17].
- MAI-DxO: no ablation; accuracy gain not significant for o3 and o4-mini [d05, d04].

### 5.3 Failures, boundaries and competing explanations

- **Reasoning models.** Kriz: BED-LLM gives modest gains over a reasoning base and sometimes loses, at 61.1x the time (2376 s vs 38.9 s) [c12]. Authors reimplemented BED-LLM themselves. Hartmann et al.: BED-LLM's top score is partly hard-coded guessing when fewer than 3 candidates remain; RL gains on 14B only +4.2 and +1.8 points [c15]. Pedrozo: Instruct to Thinking is a checkpoint change, so thinking is confounded [d09]. [C].
- **Soft answers and open candidate sets.** UoT: "I don't have a fever" does not eliminate cleanly [a17, c22]. Things set GPT-4 30.8 to 36.8 only [c22]. DPO abstract targets 7.7 to 23.1% on 13 targets [c09].
- **Open LLM-proposed hypothesis space.** Max-information probes wipe out the particles; the proposer then returns invalid or over-specific hypotheses; learning stalls (odd numbers: EIG 7 vs positive-test 4 vs random 2) [d13]. But UoT's open set kept its gain (+9.8 vs +10.9 points) [d02]. The difference is probably the proposer: UoT re-lists possibilities from the model each time; the Number Game needs a valid generator over numbers. Unresolved.
- **Model misspecification.** Same wrong model chooses and reads data [b23].
- **Which UoT part works?** Rewards within 1-3 points of each other (GPT-3.5) [b04]. But swapping ToT self-reward for uncertainty reward gave +5.9% [c21]. The lookahead tree may do the work, or the scoring. Not separated.
- **Compute.** BED-LLM wall-clock on one setup: Prompt-Only about 26 min, CoT about 35, Implicit about 45, BED-LLM about 2.5 h, Data-Estimation 1 d 17 h (row order inferred) [d16]. Only UoT was matched on tokens (GPT-4 only) [d02]. Nobody gave a reasoning model the same tokens.
- **Thinking without questions.** SIA: 67.3 to 67.5 [d14]. Best-of-35 sampling on static differential: recall 0.537 vs 0.531 and precision down [d22]. Extra samples are no substitute for a good probe, but these are different tasks from probe choice.
- **Active learning in general.** Fancy selection adds little over simple uncertainty once the baseline is strong [b29].
- **Noise.** Nobody injected wrong answers into EIG probing. Text-to-SQL lists it as future work [d15]. SIA's stress test (10 paired cases) is the only trace: wrong suggested cause selected in 2 of 10 [d14].
- **Greedy theory.** Bound is worst-case log-squared; single-log claim withdrawn [d20]. EIG can be suboptimal because it ignores later steps [b22].

### 5.4 Interventions that worked

- Code-side EIG or split over sampled hypotheses [c01, c02].
- Filtering hypotheses against history [c05].
- Uniform weights over samples [b10].
- Sampling more candidate probes (up to 10) [a15, b16].
- Open questions where the answerer can answer them [b11].
- A separate gate that forces a probe [d07].
- Confidence-with-rationale gate with 3 samples [d06].
- Putting Bayes in code [c17].
- Rules against repeated question types [d17].
- Cleaning repeated and unanswerable questions plus paragraph format: +5.7 pp over MediQ BASIC [d06].

### 5.5 Interventions that did not work

- CoT about question quality [c04].
- Letting the model choose among the sampled candidates ("works much less well" than computed EIG) [d16].
- Model log-probs as weights [b10].
- Plain self-consistency for the ask gate (degrades) [d06].
- Giving GPT-4V a board image: no better than no board [b17, c11].
- Extra thinking with no questions [d14].
- Max-information probes alone on an open hypothesis space [d13].
- Transfer of RL-learned probing to MediQ (+0.9) [c16].

## 6. Language models

### 6.1 Baseline behaviour

- GPT-4 wins 0.31 (Things) and 0.50 (Celebrities) of 20Q games; Claude-2 0.21 / 0.31; Vicuna 7B 0.09 / 0.06. Humans 0.24 / 0.31 [b05, c24].
- Failure modes: guessing specific items early, repeating questions [b05]. 40% of CodeLlama and 33% of GPT-4 valid Battleship questions had zero EIG [c11].
- Reasoners are not exempt. Qwen3-30B thinking picks its own best candidate in 25-26% of turns [d09]. QuestBench: 40-50% on logic and planning for o1-preview and Gemini thinking models while BFS depth 10 gets 99.8% [d10].
- Models do not bring up missing information on their own [d12, d06, d07].

### 6.2 What changed behaviour, and by how much

| Change | Effect | Source |
|---|---|---|
| Code EIG over sampled hypotheses (non-reasoning, 20Q) | +37.4 points avg (paper) or +40.4 (our recount) | [c01] |
| Same, UoT with simulated branches | about +10 points avg (46.6% relative for Llama3-70B) | [d01] |
| Half-split only | about 62% of EIG gain | [c02] |
| Same-model weak (Llama-3.1-8B) | Animals 8 to 63, Celebrities 10 to 58, Things 10 to 26 | [c07] |
| Task disambiguation, GPT-3.5 | 70.8 to 85.6 (binary) | [b08] |
| Same, GPT-4o-mini | 79.6 to 81.5 | [b09] |
| Reasoning base + BED-LLM | modest, sometimes worse, 61x slower than trained | [c12] |
| Thinking checkpoint (Qwen3-30B) | win 0.10 to 0.93; 0.14 to 0.42 bits/turn | [d09] |
| Separate ask gate (coding) | 61.2 to 69.4 | [d07] |
| MediQ gate | +22.3% over ask-always | [d06] |
| Form rules (GuessingGame) | 39.4 to 80.0 to 97.4 | [d17] |
| Scaffold (MAI-DxO on o3) | cost -39.7%; accuracy +3.3 (n.s. for o3) | [d05] |
| Whole Bayes loop in code (MoBayes) | top-1 60 to 78 | [c17] |

### 6.3 Reading the pattern

The size of the gain tracks three things:

1. **How weak the base model is.** Largest for 8B models; near zero for GPT-4o-mini on HumanEval [b09, c07].
2. **Whether hypotheses are enumerable and answers are clean.** Closed sets and deterministic answers do best [a17, c22, c09].
3. **Whether the base model enumerates early.** Form rules fix this for free [d17].

For reasoning models the question is open. Evidence leans "smaller gain, high cost" [c12, d09, d10, d05, d11], but it is made from a handful of small, partly confounded sets.

### 6.4 Gaps in the LLM literature

- Almost every result uses an LLM-simulated answerer and a closed list of animals, celebrities or diseases [critique].
- No paper isolates probing inside an agent that also repairs or reasons [critique].
- Samples are small: Zendo 5 seeds, ActiveACRE 20 tasks, MoBayes n=50, DPO test sets about 45 games.
- Key GDE and lookahead originals not opened.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory. Status per SCHEMA.md marks.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Code, not the model, scores probes.** In S7, when two or more surviving candidates disagree, sample several candidate probes, compute each probe's outcome under each surviving candidate (by running code), and pick the probe whose outcomes split candidates most evenly. Never ask the model "which probe is best" and never trust CoT about it. | S7 + G5 | [E] direction (the half-split vs full EIG choice stays [S]) | c01, c03, c04, d16, b08, d15, c17; K01, K03 |
| A2 | **Keep an explicit hypothesis list in code and filter it by every observation.** No implicit memory of what has been ruled out. | S6/S7 + memory | [E] | c05, b10; K04 |
| A3 | **Use uniform weight over history-consistent samples** unless a real prior exists. Never weight by the model's own stated probabilities. | S7 | [S] for the log-prob comparison (b10) but safe default | b10, a21; K05 |
| A4 | **Generate several candidate probes (about 5 to 10), then select.** The scoring rule matters more than who proposes. | O / S7 | [E] | a15, a14, b16, c10; K18 |
| A5 | **Probes need a clean elimination.** Enumerate candidates first (S6/S2). Use probes that give clear, checkable outcomes. | S2/S7 | [E] | a17, c22, c09; K07 |
| A6 | **Do not self-trigger probing from the model's feeling.** The gate is computed (leading hypothesis share below a set value, or two surviving candidates disagree). Where a model-side check is needed, use a separate call, not the same agent. | S7 gate + G1 | [E] direction | b31, d06, d07, d12; K19, K24 |
| A7 | **Log repeated and already-answered probes and early specific commitments** (a trace check, not a rule). | G6 / logging | [E] | b05, c23, b07; K10 |
| A8 | **One-step greedy is the default lookahead.** | S7 | [E] for the theory, [S] for the LLM numbers | a09, a10, d18, d03, d20; K13, K31 |
| A9 | **Report tokens and wall-clock next to accuracy for any probing variant.** BED-LLM is about 6x Prompt-Only wall-clock. | G7 | [E] (design rule) | d16, c12; K17 |
| A10 | **Cost-weighted order for checks**: when one fault is likely and checks are independent, order by prior over cost; with equal cost and prior this is halving. Use as a documented rule only; no LLM test. | O probe order | [E] as theory only | a07, b35, d19; K12 |

### Test first (single-source, contested, or untested)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Computed scoring vs a thinking model at equal tokens.** The central question. | S7, G7 | [C] | c12, d09, d10, d02; K17, K22, K23 |
| T2 | **Half-split as the default score**, full EIG only if answers are noisy. | S7 | [S] | c02; K02 |
| T3 | **No-repeat-type and no-early-guess rules** in the baseline. | G (probe diversity) | [S] | d17; K28 |
| T4 | **Noise tolerance**: flip 10-20% of probe answers and measure the drop. | S7 evidence handling | [S] | d15, d16, d14; K29 |
| T5 | **Falsifying probe vs max-entropy probe vs positive-test** on fixation-prone items; switch rule. | S7 + fixation | [S] | d13, d14, d04; K15, K26 |
| T6 | **Computed gate** (leading share below threshold) vs ask-always vs no-ask. | S7 gate | [S] | d06, d07, d08; K19, K25 |
| T7 | **VoI gate with probe cost in tokens.** | S7 gate | [S] | d08; K25 |
| T8 | **Priors from repository history** for suspect ranking by p / cost. | S7 priors, memory | [S] | a03, d19, d21; K16, K30 |
| T9 | **Cost steward / challenger roles** ablated separately. | O | [S] | d04, d05, d14; K11, K27 |
| T10 | **Two-step lookahead** only for costly or enabling probes. | S7 | [S] | d03, c14; K14 |
| T11 | **Code-side posterior and stopping**, LLM as parser only. | S7 + code | [S] | c17-c19; K09 |
| T12 | **Soft hypothesis weights for open hypothesis spaces** or a safe-probe-first switch. | S6/S7 | [S] | d13; K26 |

## 8. Concrete tests on our bench

Rules for all tests: both arms get the same total tokens (prompt + completion + thinking, counted). Setup cost counts (G7). Report accuracy, tokens, wall-clock, number of probes. Use at least 100 items per arm where the item pool allows; report 95% CIs. Fix seeds and repeat 3 times. Use a different model as the answerer where an LLM answerer is used.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1, K22) equal-token head-to-head | Diagnosis items with a hidden fault and a finite candidate list (20Q-style set, debugging items with known buggy line, ARC two-rule ambiguity items) | (a) thinking model with N thinking tokens picks probes itself; (b) same or non-thinking model samples K=8 candidate probes and 20 hypotheses, code scores by EIG; (c) same with half-split; (d) plain baseline with no-repeat-type rule | success rate at budget; probes to solve; tokens | (b),(c) beat (d) by 10+ points for a non-thinking model; vs (a) unknown, expected within 5 points for strong thinking model |
| E2 (K02) half-split vs full EIG | Same as E1 plus a noisy-answer subset | split vs entropy vs full EIG, same K and N | success; probes; tokens | split within 5 points of EIG on deterministic items; EIG better on noisy items |
| E3 (K29) answer flip | E1 items with 0%, 10%, 20% of answers flipped | scored probing vs unscored probing vs scored probing with re-ask on contradiction | success drop per flip rate | scored probing drops more than unscored at 20% unless contradictions trigger a repeat; the re-ask arm recovers |
| E4 (K26) falsification | Fixation-prone debugging items where the obvious suspect is wrong | (a) max-entropy; (b) leader-falsifying probe; (c) positive-test; (d) switch rule | fixation rate (still on wrong leader after 3 probes); probes to correct fault | (b)/(d) lower fixation rate than (c); (a) vs (b) unknown |
| E5 (K19, K24) gate | Under-specified and fully specified items mixed 50/50 | no-probe; ask-always; self-initiated; computed-share gate; separate binary check call | accuracy; probes per item; false probes on fully specified items | gate beats ask-always on fully specified items; beats no-probe on under-specified |
| E6 (K25) VoI vs threshold | E5 items with probe price = tokens or minutes (3 price levels) | VoI gate vs best tuned threshold vs no probe | utility = reward minus price x probes | VoI wins at low and mid price, may lose at high price (as in Dong et al.) |
| E7 (K30) priors | Debugging items with repository history | uniform vs prior-weighted vs prior/cost-weighted suspect ranking | probes to find the fault | prior/cost beats uniform by 20%+ if history predicts bugs |
| E8 (K28) form rules | 20Q-style and debugging dialogues | baseline vs baseline + no-repeat-type vs + forced open question | success at equal tokens | big gain on weak models; small on strong ones |
| E9 (K14) lookahead | Items with enabling tests (test useless alone, useful later) | K=1 vs K=2 lookahead | success; tokens | K=2 wins only on enabling-test items |
| E10 (K11, K27) role ablation | Cost-bearing diagnosis items | full panel; minus challenger; minus cost steward; minus ensemble; plain | accuracy; spend | steward cuts spend; challenger lifts accuracy on anchored items |
| E11 (K09) code posterior | Closed-set diagnosis with a likelihood table | LLM tracks posterior vs code holds posterior, LLM parses | top-1; tokens | code arm wins on weak and mid models |
| E12 (K15) open hypothesis space | Number-Game-like rule discovery with LLM-proposed hypotheses | EIG vs safe-first switch vs random | queries to converge; stalls | switch rule avoids the stall |

Order guidance is in UNKNOWNS.md.

## 9. What does not transfer, and why

- **Training-based gains.** DPO, behaviour cloning, RL (Mazzaccara, Zhang, Kriz, Hartmann, Tajwar) [c08, b06, c12, c15, c25] teach a policy. We do not train. Use only as an upper bound. Transfer was uneven anyway (ASIG MediQ +0.9) [c16].
- **GDE circuit numbers (42.0 vs 6.7).** Noise-free gate-level circuits with known failure rates and a formal device model [a03]. Our tasks have no formal model. The rule "combine prior and entropy" transfers; the numbers do not.
- **p/C ordering.** Needs single fault, independent components, fixed observation costs [a07, d19]. Real bugs are often multiple, and probes interact.
- **Greedy guarantees.** Noise-free answers, exact prior, submodular objective [a09, b20]. LLM-sampled hypotheses are not an exact prior.
- **MoBayes.** Needs a likelihood table (symptoms by disease) [c17]. Few of our tasks have one.
- **UoT's full tree.** Costs 4.5k to 9.3k GPT-4 tokens per game [d02], and only GPT-4 was matched. Too costly for a short-think default (G11).
- **BED-LLM's own cost.** 2376 s per game against a trained 38.9 s; 6x Prompt-Only wall-clock [c12, d16]. Use only when probes are expensive and the item is hard (G12).
- **MAI-DxO.** The setting is real money per test, a deep differential and a gatekeeper that is an LLM inventing findings [d05]. The bundled design hides which role matters. Roles may not move our tasks.
- **20Q results.** Closed lists of entities, an LLM answerer and binary questions. Real debugging has noisy, rich answers and the hypothesis space is open.
- **Human results.** GATE humans and the Battleship data show people's questions are less informative than computed ones but humans use different question types [a13, b18]. We do not model human answerers.
- **Debate roles.** MAI-DxO's panel is multiple personas of one model. SCHEMA G9 and G4 forbid debate and persona voters on single-answer problems. Only the challenger role is compatible, as a code-triggered probe type (section 4.8), not a vote.

## 10. Open questions

1. At equal total tokens, does computed half-split (or EIG) beat a thinking model that gets more thinking tokens? Every paper gave the scored method more compute [critique gap 1].
2. How much of the gain survives soft, noisy or free-text answers with an open hypothesis set (real debugging)?
3. Does the gain hold for reasoning models on any task other than 20Q? Kriz says small; Pedrozo and QuestBench say headroom remains [c12, d09, d10].
4. Which MAI-DxO role saves money? Not measured.
5. What is the best trigger for probing? Self-initiated is poor; thresholds are tuned on test data [d06].
6. Does a probability-over-cost ordering work for LLM agents outside medicine? No study.
7. Do failure-rate priors help an LLM agent? One low-trust synthetic study.
8. Does a leader-falsifying probe lower fixation compared with a max-entropy probe? Only indirect evidence.
9. Original GDE and de Kleer 1992 and 2006 lookahead numbers: not obtained.
10. Why does UoT keep its gain on open sets while Number Game open sets stall? The proposer type may decide it.
11. Is UoT's gain from information-gain scoring or from lookahead structure? Rewards differ by 1-3 points, but ToT self-reward vs uncertainty reward differs by 5.9%.
12. BED-LLM's reported 37.4 vs our recount 40.4 from Table 1: unexplained.
13. Half-split's 62% share holds on one paper only. Does it hold with noisy answers?
14. Do wrong or inconsistent answers cripple EIG-driven probing? Nobody injected errors.

## 11. Sources

[V] = full text or page opened this session (by a research agent; critique re-opened the starred ones). [M] = snippet, abstract only, or citation only.

**Classic diagnosis and decision theory**
- [M] de Kleer and Williams (1987) Diagnosing multiple faults. Artificial Intelligence 32(1):97-130. https://www.fs.isy.liu.se/Edu/Courses/DocDiagnos/CourseMaterial/deKleer_Williams_1987.pdf and https://doi.org/10.1016/0004-3702(87)90063-4 (a01, b32, c29)
- [V] de Kleer (1991) Focusing on probable diagnoses, AAAI-91. https://cdn.aaai.org/AAAI/1991/AAAI91-131.pdf (d18)
- [M] de Kleer, Raiman, Shirley (1992) One step lookahead is pretty good, in Readings in Model-Based Diagnosis. No URL (a26, a25)
- [V] Siddiqi and Huang (2010) New Advances in Sequential Diagnosis, AAAI/KR. https://users.cecs.anu.edu.au/~jinbo/10-kr.pdf (a02-a04, a25)
- [V] Siddiqi and Huang (2011) Sequential Diagnosis by Abstraction, JAIR 41:329-365. https://arxiv.org/pdf/1401.3892 (a05, a06, a27)
- [V] Breese and Heckerman (1996) Decision-Theoretic Troubleshooting: A Framework for Repair and Experiment, UAI. https://arxiv.org/pdf/1302.3563 (a07, d19)
- [M] Heckerman, Breese, Rommelse (1995) Decision-theoretic troubleshooting, CACM 38(3):49-57. https://www.microsoft.com/en-us/research/publication/decision-theoretic-troubleshooting/ and https://doi.org/10.1145/203330.203341 (a08, b33)
- [M] Hyafil and Rivest (1976) Constructing optimal binary decision trees is NP-complete. https://doi.org/10.1016/0020-0190(76)90095-8 (a28, b34)
- [M] Kadane and Simon (1977) Optimal strategies for a class of constrained sequential problems, Annals of Statistics. https://doi.org/10.1214/aos/1176343854 (b35)

**Active learning and experimental design**
- [V] Golovin and Krause (2011/2017) Adaptive Submodularity. https://arxiv.org/pdf/1003.3967 (a09-a11, b19, b20, d20)
- [V] Rainforth, Foster, Ivanova, Bickford Smith (2023/2024) Modern Bayesian Experimental Design. https://arxiv.org/pdf/2302.14545 (a12, b21-b23)
- [V] Beck et al. (2021) Effective Evaluation of Deep Active Learning on Image Classification Tasks. https://arxiv.org/abs/2106.15324 (b29, b30)

**LLM probing and question asking**
- [V] Zhang, Lu, Jaitly (2023) Probing the Multi-turn Planning Capabilities of LLMs via 20 Question Games. https://arxiv.org/abs/2310.01468 (b05-b07, c23, c24; table re-checked*)
- [V] Li, Tamkin, Goodman, Andreas (2023) Eliciting Human Preferences with Language Models (GATE). https://arxiv.org/pdf/2310.11589 (a13, b27, b28)
- [V] Piriyakulkij, Kuleshov, Ellis (2023/2024) Active Preference Inference using Language Models and Probabilistic Reasoning. https://arxiv.org/abs/2312.12009 (b12; c28 [M])
- [V*] Piriyakulkij, Langenfeld, Le, Ellis (2024) Doing Experiments and Revising Rules with Natural Language and Probabilistic Reasoning. https://arxiv.org/pdf/2402.06025 (a14-a16)
- [V*] Hu et al. (2024) Uncertainty of Thoughts. https://arxiv.org/abs/2402.03271 (a17-a19, b01-b04, c20-c22, d01-d03)
- [V] Grand, Pepe, Andreas, Tenenbaum (2024) Loose LIPS Sink Ships. https://arxiv.org/abs/2402.19471 (b16-b18, c10, c11)
- [V] Mazzaccara, Testoni, Bernardi (2024) Learning to Ask Informative Questions. https://arxiv.org/abs/2406.17453 (c08, c09)
- [V*] Kobalczyk, Astorga, Liu, van der Schaar (2025) Active Task Disambiguation with LLMs. https://arxiv.org/abs/2502.04485 (b08-b11; c27 [M])
- [V*] Choudhury et al. (2025/2026) BED-LLM. https://arxiv.org/abs/2508.21184 (a20-a22, c01-c07, d16)
- [V] Li, Kim, Wang (2025) QuestBench. https://arxiv.org/abs/2503.22674 (a23, a24, b13-b15, d10)
- [V] Tajwar et al. (2025) Training a Generally Curious Agent (PAPRIKA). https://arxiv.org/abs/2502.17543 (c25; part read)
- [V*] Kriz, Berthon, Astorga, van der Schaar (2026) Amortizing Sequential Experimental Design in Reasoning LLMs. https://arxiv.org/abs/2610.20832 (c12-c14)
- [V] Hartmann et al. (2026) Amortising Bayesian Experimental Design for Sequential Information Gathering in LLMs (ASIG). https://arxiv.org/abs/2607.03426 (c15, c16)
- [V*] Kesmen et al. (2026) MoBayes. https://arxiv.org/abs/2604.20022 (c17-c19)
- [V] Ding et al. (2026) Whom to Query for What: Adaptive Group Elicitation. https://arxiv.org/abs/2602.14279 (c26)
- [V] Pedrozo, Soares, de Oliveira (2026) Do Reasoning Models Ask Better Questions? https://arxiv.org/abs/2601.17716 (d09)
- [V] Chari and Pattanaik (2026) Wild Guesses and Mild Guesses in Active Concept Learning. https://arxiv.org/abs/2602.06818 (d13)
- [V] Hutson et al. (2025) GuessingGame. https://arxiv.org/abs/2509.19593 (d17)
- [V] Qiu, Li, Su, Chen (2025) Interactive Text-to-SQL via Expected Information Gain. https://arxiv.org/abs/2507.06467 (d15)
- [V] Amin (2026) Bayesian Orchestration of Multi-LLM Agents for Cost-Aware Sequential Decision-Making. https://arxiv.org/abs/2601.01522 (d21; low trust)

**Diagnosis, clarification and gating**
- [V*] Nori, Horvitz et al. (2025) Sequential Diagnosis with Language Models (SDBench, MAI-DxO). https://arxiv.org/abs/2506.22405 (b24-b26, d04, d05)
- [V] Li et al. (2024) MediQ. https://arxiv.org/abs/2406.00922 (b31, d06; abstract-level in b31, full text in d06)
- [V] Edwards and Schuster (2026) Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents. https://arxiv.org/abs/2603.26233 (d07)
- [V] Dong et al. (2026) Value of Information: A Framework for Human-Agent Communication. https://arxiv.org/abs/2601.06407 (d08)
- [V] Su and Cardie (2026) Knowing but Not Showing. https://arxiv.org/abs/2605.25284 (d12)
- [M] Kirichenko et al. (2025) AbstentionBench. https://arxiv.org/abs/2506.09038 (d11; abstract only)
- [M] Laban et al. (2025) LLMs Get Lost in Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (c30; citation only)
- [V] Marozzo and Lio (2026) LLM-as-an-Investigator (SIA). https://arxiv.org/abs/2606.13220 (d14)
- [V] Coburn, Sanner, Silver (2026) Social Chain of Thought. https://arxiv.org/abs/2608.11420 (d22)

Evidence-file caveat: for several items the agent that wrote the line and the critique disagree on "opened" depth (for example b31 vs d06 for MediQ). The critique re-opened the starred ones and checked their numbers. The remaining items stay as the first agent reported them; Siddiqi and Huang tables were not re-checked.

Related subfields (parallel run, not covered here): Consistency-based diagnosis and conflict generation; Troubleshooting search strategies; Hypothesis limits in troubleshooting; Adaptive stopping and metareasoning; Verification design; Anomaly handling and fixation; Accuracy and dissociation of monitoring; LLM debugging.
