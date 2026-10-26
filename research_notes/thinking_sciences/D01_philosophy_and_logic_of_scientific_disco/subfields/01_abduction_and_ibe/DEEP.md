# Abduction and inference to the best explanation: deep document

*Subfield D01.01. Folder: `research_notes/thinking_sciences/D01_philosophy_and_logic_of_scientific_disco/subfields/01_abduction_and_ibe`. Built from evidence_a to evidence_d (a01-a30, b01-b26, c01-c27, d01-d31), claims.jsonl (K01-K33) and critique.md. Evidence ids in brackets. Claim ids are written K01 etc. (full form D01.01-K01).*

*Reading note. Several evidence lines record the same paper two or three times (Lombrozo 2007, Dalal et al., Sun and Saparov, GEAR, Qiu et al.). The critique counted independence per paper, not per line. "Status" below follows claims.jsonl: established, single-source, contested, open.*

---

## 1. What it is

Abduction is inference from a surprising fact to an explanation that would make the fact unsurprising. Inference to the best explanation (IBE) is the later, stronger form: out of the candidate explanations, accept the one that explains best.

Two jobs are hidden inside the word. Keep them apart, because the evidence differs.

- **Generation** (creative abduction): produce candidate explanations. Hard for people and for models.
- **Selection** (selective abduction): choose among given candidates. Close to human level on short commonsense items. [a03, b16]

For our agent, abduction is the loop "see the examples, guess the rule, run the rule, keep or fix it". It is the core of ARC-style items, of rule discovery, of diagnosis and of debugging. It sits inside the schema at S2 (candidate rules), S3 (generate), S4 (test), S5 (revise), S7 (select), S8 (verify).

The field has four threads:

1. **Philosophy of the schema**: Peirce, Hanson, Harman, Lipton, Douven (what the inference is, whether it is valid, what "best" means).
2. **Explanatory virtues**: simplicity, scope, unification, fit with background, coherence. Do they track truth?
3. **Human psychology**: do people prefer simple explanations, and is that rational? (Lombrozo and others.)
4. **LLM studies**: benchmarks and methods for abductive reasoning, with measured numbers.

Main message from the numbers: the generate-then-test loop works when a program runs the test and the rule is short and symbolic. It fails when the model must apply its own rule, when the structure is perceptual, and when several causes interact. Models almost never say "none of these fits". The right answer is often in the pool and not picked.

---

## 2. History and theories in depth

### 2.1 Peirce: abduction as proposal, and the three-step cycle

Peirce's schema, c.1903, three lines [a01]:

1. The surprising fact C is observed.
2. If A were true, C would be a matter of course.
3. Hence there is reason to suspect A is true.

It is a rule for proposing a hypothesis worth testing. It is not a rule for accepting one. Peirce worked on abduction for over fifty years, so his texts are not one coherent view (SEP caution) [a01].

Peirce's cycle [a02]:

- **Abduction** forms explanatory hypotheses. Peirce called it the only logical operation that introduces a new idea.
- **Deduction** draws testable consequences from the hypothesis.
- **Induction** scores the hypothesis by how many of those consequences hold.

This is exactly "generate, derive predictions, test". Liu, Neubig and Andreas (2024) tested the cycle in four LMs and called it "an incomplete loop" [c14]. Our S3, S4, S7 already realise it.

Source caution: all Peirce and Hanson material in our files is secondhand through the Stanford Encyclopedia of Philosophy. No Peirce primary text was opened.

### 2.2 Hanson: retroduction

Hanson (1960) gave a retroductive schema [a03]: surprising phenomena p1, p2, p3 are met; they would not be surprising if a hypothesis of type H held; so there is good reason to elaborate a hypothesis of type H. The output is a TYPE of hypothesis to work out, not a finished theory. This matches our S2: write candidate rule families first, then refine.

SEP splits abduction in two [a03]:

- selective abduction: pick from known hypotheses;
- creative abduction: generate new ones.

### 2.3 The context distinction and the discovery-machine objection

The old view (Popper, tied to Reichenbach) separated conceiving an idea from testing it, and said only testing is open to logic. The discovery-machine objection (Curd 1980) says no rule can output good hypotheses mechanically. BACON-style programs exist, but Gillies (1996) argues they cannot decide which data are relevant [a04].

Lesson for us: do not expect a procedure that outputs the right hypothesis. Expect a procedure that proposes many and tests them. That is K01 (established, two sources, secondhand).

### 2.4 Harman, Lipton, and "loveliness versus likeliness"

Harman (1965) named "inference to the best explanation" and argued that much induction is IBE. Harman's own text was not opened; the account here comes from Douven's SEP entry and Dellsen [a05, a21].

Lipton (2004) made the key distinction [a21]:

- **Loveliness**: how good the explanation would be if true. The balance of virtues: simplicity or parsimony, explanatory scope, unificatory power, fit with background data.
- **Likeliness**: how probable it is that the explanation is true.

IBE says the lovelier explanation is the likelier one. Whether that is so is the whole dispute.

Douven's SEP entry lists three schemas [a05]:

- **ABD1** (textbook): infer the truth of the candidate that best explains E. Problem: "candidate" and "best" are undefined, and a comparative premise gives an absolute conclusion.
- **ABD2** (Musgrave, Lipton): the best must also be "good enough".
- **ABD3**: further conditions (for example no close competitor).

Lipton also proposed adding the negation of all considered hypotheses as a catch-all. The SEP entry calls this hardly informative [a05].

### 2.5 The bad lot

Van Fraassen's objection: the best of a bad lot is still bad. If the true explanation is not among the candidates, IBE picks a false one with confidence. No fix is agreed [a05, a06]. Dellsen (2020) argues for a three-stage model: generate, adopt the loveliest as a working hypothesis, then consolidate over time. "Good enough" is read relative to the rivals and over time, not as an absolute virtue level, because absolute virtue levels cannot be measured [a20, K18].

This is the philosophical root of our G6 and S8 tension: do not abstain on the first pass, yet do not treat the best candidate as proven. Practical answer from the literature: adopt as working hypothesis, then test on something not fitted (G3).

### 2.6 IBE against Bayes

- Van Fraassen: a more informative theory cannot be more probable; probabilistic abduction either equals Bayes' rule or is Dutch-bookable [a06].
- Replies: Maher and Skyrms (losses in one respect are offset by gains in another); Douven (1999) and later work argue speed can offset Dutch-book exposure [a06, b07].
- Douven's **EXPL rule**: posterior = prior times likelihood, plus a fixed bonus c split among the best explanations of the TOTAL evidence, then normalised. With c = 0 it is exactly Bayes [a15].
- Climenhaga (2017): non-Bayesian IBE yields incoherent credences. Cabrera (2017): many virtues lack confirmational import (snippets only) [b23, b24].
- Wojtowicz and DeDeo (2020): explanatory values can arise from one Bayesian framework (abstract only) [d27].

### 2.7 Explanatory virtues and what they might be

Common virtues: simplicity, generality, coherence with accepted theory (Thagard 1978, McMullin 1996). Giere says they lack content. SEP says formal work on simplicity (Forster and Sober 1994) and coherence (Bovens and Hartmann 2003) makes them more precise [a07]. Whether a virtue is a truth-tracker or only a pragmatic preference is the central open question; the human and simulation evidence is in sections 3 and 5.

---

## 3. Core findings with exact numbers

Status key: est = established (two or more independent sources), single = single source, contested, open = untested.

### 3.1 Human explanation preferences

| Finding | Numbers | Source | Status |
|---|---|---|---|
| With no base rates, people pick the one-cause explanation; with base rates, the more probable disease | 96% one-cause (Exp 1, N=48); 92% more probable disease. Of the 96%, justification: 17% simplicity, 39% sufficiency, 39% probability | Lombrozo 2007 Exp 1 [a08, b01] | single (one lab) |
| Bias to simple persists when probability is given | N=144; 71% simple overall; chi2(7)=25, p<.01; over a third still chose simple when the complex story was 10 times more likely; logistic slope .795 (SE .217, not different from 1), constant -1.306 (SE .248) | Lombrozo 2007 Exp 2 [a09, b02] | single |
| Replication with experienced frequencies: bias smaller but stays | N=108; 63% simple; 41% at 1:10 against simple (39% in Exp 2); implied prior 68% (CI 57 to 78%); slope .62, constant -.77 | Lombrozo 2007 Exp 3 [a10, b03] | single |
| Committing to the unlikely simple story makes people overestimate its cause | seen in Exp 3 (size not recorded in our files) | [b03] | single |
| Unambiguous probability removes most of the bias; wording matters | N=48; joint-probability form 17% simple vs 61% at same ratio in Exp 2, chi2(1)=8.85, p<.01; "most likely" 46% vs 17%, chi2(1)=4.75, p<.05 | Lombrozo 2007 Exp 4 [a11, b04] | single |
| Preference depends on causal structure | N=544; strongest for one cause with two independent effects, modest for jointly sufficient causes, reversed for independently sufficient causes (abstract only) | Liquin and Lombrozo 2018 [b05] | single |
| Explaining pushes people to simple, broad hypotheses | 5-year-olds prompted to explain chose the common-cause story more; 4-year-olds at chance; adults found the 100% rule more than every control group | Lombrozo 2016 review [a12, a13] | single |
| Outside labs: people prefer explanations about as complex as the event | four studies, n = 286, 201, 523, 253 | Lim and Oppenheimer 2020 [d21] | contested with Lombrozo (K33) |
| Simplicity did not predict rated quality of real explanations; complexity preferred | Reddit corpus; sample sizes not read | Zemla et al. 2017 [d22] | abstract only |
| Simplicity preference stronger for deterministic and physical systems than stochastic and social | five studies; sizes not read | Johnson, Valenti, Keil 2019 [d23] | abstract only |
| Preference tracks root simplicity (unexplained causes), not the count of all causes | four experiments | Pacer and Lombrozo 2017 [d24] | abstract only |
| Judged explanatory goodness adds to Bayes in predicting credence | N=26, 10 draws from one of two 40-ball urns; R2 0.90 (MOAB) vs 0.83 (MO); AIC -398.77 for MO; chi2(2)=124.87, p<0.0001 | Douven and Schupbach 2015 [a14, b06] | single (reanalysis of one study) |
| Three experiments support explanationist updating | numbers not read | Douven and Schupbach 2015, Cognition [d26] | abstract only |

### 3.2 IBE against Bayes in simulation

| Finding | Numbers | Source | Status |
|---|---|---|---|
| EXPL reaches credence above 0.9 in the truth sooner than Bayes | 10-ball urn, 500 draws per sequence, 1000 sequences per hypothesis | Douven 2013 via Pettigrew [a16] | contested (K17) |
| A trivial rule matches EXPL on that speed measure | rule waits 10 draws then jumps to the matching hypothesis; scores equal or better | Pettigrew 2021 [a16] | contested |
| IBE** (uncertain evidence) puts >0.95 on the truth far more often than Jeffrey updating | about 49 to 52% vs 11 to 16% of runs; 55,000 runs | Trpin and Pellert 2019 [a18, d19] | contested |
| But IBE** is falsely confident early | first assignment above 0.95 on a false coin: 47% (233,882 runs) vs 3% (15,401); above 0.99: 37% vs 1%. Bonus fixed at 0.1; never varied | Trpin and Pellert 2019 Table 7 [d19] | single |
| Best bonus size is small and setting-specific | ICU diagnosis simulation; bonus drawn from U(0, 0.25); surviving EXPL agents settle at c = 0.010 (CI 0.010 to 0.011); Good's rule 0.117; fitness 0.873 vs 0.871 and 0.872 | Douven 2020 [d20] | single |
| Result depends on task risk and difficulty | 5,460 settings, 1,000 rounds each | Dellsen and Trpin 2025 [a19] | single |

### 3.3 LLM benchmarks and methods

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Hypothesis search (propose, program, run on examples) beats direct prompting on ARC | GPT-4, 100 tasks: direct 17%; programs only 23%; LLM-summarised 30%; human-selected 33%; human-written (LARC) 45% | Wang et al. 2024 [a28, b18] | est (K02) |
| The loss is mostly implementation | correct hypothesis in pool for 49 of 100 tasks; 33 of 49 (67%) became correct programs; LLM reranker had the correct hypothesis in top 16 of 64 for only 10 of 21 tasks | Wang et al. [d01, d02] | single (K24) |
| Propose-test-refine with a code interpreter helps on rule tasks | GPT-4, ACRE raw IO 64.0, SC 65.0, self-refine 70.0, refinement 82.5; ACRE task 28 / 29 / 32 / 59; List Functions raw 65.1 to 71.2; task 39.6 to 61.2; MiniSCAN task 0.0 to 46.0 (T=3,N=1) and 70.0 (T=3,N=5) | Qiu et al. 2024 [a29, c07, d07] | est (K02) |
| ...and hurts on MiniARC | raw 33.1 (IO) vs 18.7 (T=3,N=5); T=1,N=1 5.9; self-refine 15.1; task accuracy 13.8 vs 14.6 | Qiu et al. [a29, d07] | est |
| Model as its own interpreter erases the gain | ACRE 70.0 raw / 32 task vs 82.5 / 59 with symbolic interpreter; MiniSCAN task from above 80% to near zero | Qiu et al. [c08, c09] | single (K03) |
| Induction and transduction solve different ARC items; a cheap gate joins them | induction 18.78, transduction 15.25, ensemble 26.50 (GPT-4 descriptions); second setting 11.07 / 13.50 / 19.50 | Li et al. 2024 [d05] | single |
| Passing shown examples is a weak gate | CodeARC, o3-mini first function: 67.6% pass 10 initial examples, 38.9% pass the oracle (28.7 points false accepts); BARC about 9% of fitting programs are false positives | Wei et al. 2025; Li et al. [d09, d05] | est (K25) |
| Right item in pool, not picked | MATH Llama-3-8B coverage 98.44% at 10,000 samples vs 41.41% by vote or reward model; PaLM 2-L oracle vs SC: GSM8K 96.2 vs 90.4, MATH 57.2 vs 37.9; AIMO 3 best vote 42/50 vs pass@20 45.5; 2% to 46% of correct-sampling trajectories lose the vote | Brown et al.; Chen et al.; Nitarach; Li and Li [d03, d10, d12, d13] | est (K23, 5 sources) |
| Strict code checks recover much of that gap | SWE-bench Lite 15.9% to 56% with unit tests; exact multiset filter 74.2% to 92.2%, no new errors; CodeT HumanEval 47.0 to 65.8 (+18.8), MBPP 58.1 to 67.7 | [d11, d13, d03] | est |
| Test suites err too | 11.3% of SWE-bench Lite problems have flaky tests; one gate 100% precision (161 fires), another 5% | [d04, d18] | est |
| Selection among given explanations is near human level when short | ART human 91.4 vs best 2019 model 68.9; GPT-5.4 ART 87.2, e-CARE 88.0 (humans 91.4, 92.0); DDXPlus top-1 79.75, hit@3 98.7 | Bhagavatula 2019; Salimi 2026 [a26, b16, c15] | est (K04) |
| ...but long or open items are not | True Detective best 42.9 vs human average 47.0; MuSR murder best 68.0 (GPT-4o), GPT-5.4 60.8, human 92.1 | [b16, c15] | est |
| Open generation is much weaker than selection | GPT-5.4 ProofWriter abductive accuracy 21.5 (F1 61.6); DDXPlus hit@3 63.0 when generating vs 98.7 ranking; Llama3.1 8B ProofWriter 1.5; AbductionRules 99.6; NeuLR 70.8 | Salimi 2026 [c16] | est |
| On long puzzles the missing piece is the reasoning chain | True Detective, 191 puzzles; random 0.24; humans 0.47; vanilla 0.28 / 0.26 / 0.27; CoT 0.26 / 0.29 / 0.38; golden CoT 0.46 / 0.63 / 0.83 (GPT-3.5 FeedME / PPO / GPT-4) | Del and Fishel 2023 [a27, b17] | single (K05) |
| Abduction is far weaker than deduction on the same content | GPT-4 41.67% vs 72.22% (n=216 per task); GPT-3.5 31.02; Llama3-8B 37.50; Llama3-70B 37.04. Pooled medians (rough ordering only): deduction 79.96, abduction 42.50, induction 28.8 | Abe et al. 2026; Salimi 2026 [b13, c17, c18] | est (K07) |
| Accuracy collapses with more hypotheses needed | InAbHyD: above 80% at tree height 1 to below 50% at height 2 for all models except GPT-4o, while true hypotheses rise only 3.0 to 3.5 | Sun and Saparov [a22, b11, c04] | est (K06) |
| Attribution of rule changes collapses with interaction | exact accuracy 0.90 (k=0), 0.32 (k=1), 0.15 (k=2+), 0.03 (interacting); detection 0.65 vs attribution 0.28 (13 LLMs); GPT-5.4 detection 0.86, attribution 0.37, 0.41 at low and 0.47 at medium reasoning | Steiglechner et al. 2026 [b14, d28] | single (K22, K30) |
| Most generated hypotheses are inconsistent | 50,340 hypotheses: 17,835 consistent (35%), 28,159 contradicted an observation, 4,346 format failures; 70B-class about 20% | He et al. GEAR [a24, b19] | single (K12) |
| Gold-answer scoring hides underdetermination | about 80% of equally plausible hypotheses labelled incorrect | GEAR [c12] | single |
| Code-computed virtues beat a model judge | up to 77% accuracy (27 points above random); +17.5 average over GPT-3.5 judge; Spearman with human choice 0.64 vs 0.31 (n.s.); parsimony beats consistency by 14 points on average; uncertainty features +13 points on COPA and +4 on E-CARE | Dalal et al. IBE-Eval [b09, b10, c01-c03] | single (K11) |
| Models almost never say "none fits" | GPT-4 "Neither" 0.00% zero-shot, 2.78% few-shot; AbstentionBench: reasoning fine-tuning lowers abstention recall by 24% on average (20 models, over 35,000 unanswerable questions); DNR Bench instruction rescue: GPT-4o 0.42 to 0.98, Claude-3.7-Thinking 0.12 to 0.82, DeepSeek-R1 0.00 to 0.20, o3-mini-high 0.00 to 0.02 | [b13, c18, d15, d16] | est (K08, 4 sources) |
| Explaining first slows learning of exceptions in LLMs | rounds to learn all labels, direct vs CoT: GPT-4o 2.9 vs 12.5 (+331%, p<0.0001), Claude 3.5 Sonnet 2.3 vs 6.4, Claude 3 Opus 2.4 vs 5.5 | Liu et al. 2025 [d14] | single (K27) |
| Few-shot is unstable | InAbHyD in-distribution demos help at heights 3 and 4; height-1-only demos no gain; syllogism abduction few-shot: GPT-4 41.7 to 28.7, Llama-3-70B to 75.5 with 63% "Neither" | [b12, c18] | est (K09) |
| State-machine abduction agent on diagnosis | Match 39.86% vs about 26% best baseline; $0.12 vs $0.73 per case; distributed-systems diagnosis Match 70.67% (+36.67) | Luo et al. 2026 Graph of States [c20, c21] | single (K19) |

---

## 4. Mechanisms and models

Each item is written so an engineer can build it.

### 4.1 Peirce cycle as a program loop

```
observations O
repeat:
  H  = model.propose(O, k candidates)          # abduction (S3), fresh context per candidate
  P  = code.derive_predictions(H, held_out)     # deduction (S4)
  s  = code.run(H, O + held_out)                # induction (S4, S7)
  keep H if it fits O; rank by held-out fit
  if none fit: S5 with the failing output, then S6
```

Facts that shape it:

- The test must be run by code. Model-as-interpreter loses most of the gain (ACRE 82.5 to 70.0 raw, 59 to 32 task) [c08].
- More hypotheses per round help because an external check filters them [c08].
- Voting without a check barely moves (64.0 to 65.0) [c08].
- Rules from the model are often verbose; the model is a good proposer and a poor applier [c09].

### 4.2 Hypothesis Search (Wang et al.)

1. Sample 64 natural-language hypotheses per task.
2. Optionally have an LLM summarise or cluster them.
3. Turn each into a Python program.
4. Run on training pairs; up to 3 rounds of execution feedback.
5. Apply survivors to the test input.

Measured: 17 direct, 23 programs only, 30 summarised, 33 human-picked [a28]. A correct hypothesis was in the pool for 49 tasks; 33 became programs [d01]. An LLM likelihood reranker was poor (10 of 21) [d02]. Implication: build the implementer and its feedback rounds before the selector.

### 4.3 Fit gate versus held-out gate

A candidate that fits the shown examples is weakly supported. Differential testing gives a stricter gate. CodeARC's oracle returns new counterexamples; 67.6% fit the 10 examples, only 38.9% pass the oracle [d09]. Implementation:

- Keep some examples out of the fit step.
- Ask the candidate to predict on inputs where two live candidates disagree (S7 discriminating test).
- Give the gate two groups: cases the new rule must cover and cases it must leave alone. This blocks trivial entity-specific fixes (DeFAb: simple symbolic repairs solve all 336 tasks when only the observed case is checked) [d17, K32].
- Audit each gate's own precision and false-reject rate. One gate had 5% precision [d18].

### 4.4 Induction-first with a fallback gate (Li et al.)

```
cands = model.write_functions(train_pairs, n)
fit   = [f for f in cands if all(f(x)==y for x,y in train_pairs)]
if fit: answer = vote_by_behaviour(fit, test_input)      # induction
else:   answer = model.predict_directly(train_pairs, test_input)   # transduction
```

Ensemble 26.50 vs 18.78 and 15.25 [d05]. The gate is a code fact: does any candidate fit.

### 4.5 IBE-Eval: code-computed virtue score

Dalal et al. compute four features on each model-written explanation [b09, b10, c01-c03]:

- **Consistency**: logical consistency by a solver. Near useless (about .50 to .55 on most pairs): models write consistent stories for wrong options.
- **Parsimony**: proof depth and concept drift. These were 6% and 10% higher on average for the wrong option. Parsimony beats consistency by 14 points.
- **Coherence**.
- **Linguistic uncertainty**: count of hedging words. Wrong-option explanations hedge more. Strongest single predictor.

Combine the features in a simple linear model fitted on a labelled set. Result up to 77% on COPA and E-CARE with GPT-3.5, Llama 2 7B and 13B. Untested on modern models and harder tasks.

### 4.6 GEAR set-level scoring

For a set of hypotheses H1..Hn, code computes [a24, c12]:

- **Consistency**: share that reproduces every observation.
- **Generalisability**: do they give determinate predictions on unseen inputs.
- **Diversity**: do they give distinct predictions across the set.

No labels needed. Used for evaluation and as a DPO training signal (839,522 preference pairs) [a25]. In simulation, the set with higher scores was more likely to pass hidden cases (odds ratio above 1 in most cells, drifting to 1 with more hidden cases) [c13]. Nobody used it at inference time [d31]. The nearest inference-time analogue is CodeT dual agreement (a solution passes many generated tests and agrees with many other solutions): 47.0 to 65.8 [d11].

### 4.7 Explanationist update (EXPL)

```
for each hypothesis h:  post[h] = prior[h] * lik(E|h)
best = argmax over h of explanatory_goodness(h, E_total)     # ties share
for h in best: post[h] += c / len(best)
normalise
```

With c = 0 this is Bayes. Reported: faster to a high credence in the truth, but early false confidence (47% vs 3% at c = 0.1) [d19]. Douven 2020 finds survivors drift to c about 0.010 [d20]. Use as a near-tie breaker only (see section 7).

### 4.8 Graph of States (Luo et al.)

A state machine keeps an explicit causal graph of hypotheses and evidence, and drills deeper only when the confidence gap between the top two hypotheses passes a threshold. It targets four failures of deduction-style scaffolds on open diagnosis: fabricated evidence, context drift, failed backtracking, early stopping [c20]. Cost fell to $0.12 per case from $0.73, and without the state machine the agent cost $0.17 [c21]. Moderate thresholds help; very high thresholds stop shallow.

### 4.9 Dellsen's three-stage model

Generate; adopt the loveliest as working hypothesis; consolidate over time [a20]. In code: S3, S7 pick, and then S8 plus S9 keep testing the working hypothesis against new cases and retire it if a counterexample appears.

---

## 5. What holds up

### 5.1 Holds up (two or more independent sources)

- **Code-run test beats model-run test** (K02, K03). Hypothesis Search, Qiu et al. and Li et al. agree that an executing check carries the gain. K03 itself is one paper but matches G1/G5.
- **Pool contains the answer more often than selection finds it** (K23): five independent sources, across math, code and ARC.
- **Fit to shown examples is a weak gate** (K25): CodeARC, BARC, SWE-bench test issues, agent-gate audit.
- **Abduction weaker than deduction on the same content** (K07), **generation weaker than selection** (K04).
- **Accuracy falls with the number of required hypotheses** (K06): InAbHyD, GEAR, Elenchos.
- **Models rarely say "none fits"** (K08): four sources, four methods.
- **Few-shot is unstable for abduction** (K09).
- **What predicts the sign of hypothesis-then-test** (K28, read across three papers): helps on short, symbolic, composable rules (ACRE, List Functions, ARC induction); fails on perceptual or wide-window rules (MiniARC, ConceptARC single-concept, InductionBench).

### 5.2 Failures, boundaries, moderators

- **MiniARC**: refinement is worse than plain (33.1 to 18.7). Rules are verbose and hard to read, humans use pragmatic concepts [d07].
- **InductionBench**: compatibility collapses to 0 for all but o3-mini at window size 4; o3-mini 5.69% overall [d08].
- **Overfitting to examples**: on MiniSCAN T=3,N=1 beat T=3,N=5, blamed on overfitting to shown examples [c08].
- **Reasoning effort**: more effort adds little for attribution of interacting changes (0.37 to 0.41 to 0.47) [d28]. o1 stayed flat on composed causal arithmetic, other models did not [d29] (different task).
- **Reasoning hurts abstention**: lowers recall by 24% on average; larger budget generally worsens it [d15].
- **Newest model not always best**: on MuSR GPT-5.4 scored 60.8 vs 68.0 for GPT-4o [b16].
- **Self-consistency**: no help on ACRE; but beat the multi-role Theorem-of-Thought on some cases [c08, c22]. Different tasks.
- **Prompt diversity among voters did not help** on AIMO 3 (code-first mean 37.7 vs baseline 39.3) [d12].
- **Prompt style swings success**: DeFAb one model 133/336 direct vs 336/336 with another style [d17].

### 5.3 Human results: what is weaker than it looks

- All human explanation-preference data in the core experiments come from one lab (Lombrozo) (K13, single).
- Outside labs report moderators, not replications: complexity matching (Lim and Oppenheimer), complexity preferred in the wild (Zemla), context dependence (Johnson et al.) [d21-d23]. No direct replication or failed replication of Lombrozo 2007 or Douven and Schupbach 2015 was found. Treat K13 as one lab's result and K33 as contested.
- Douven and Schupbach 2015 is a reanalysis of one study with N=26.

### 5.4 IBE against Bayes: no verdict

K17 is contested. Speed to the truth is faster for explanationist rules in simulation. But a trivial rule matches the speed (Pettigrew), the early false-high rate is 47% vs 3% (Trpin and Pellert), and the best bonus is about ten times smaller than the default (Douven 2020). All simulations on coins and urns; none on language-model hypothesis pools.

### 5.5 Interventions that worked and did not

Worked:

- Execution-based filtering of hypotheses (Hypothesis Search, Qiu, Li) [a28, a29, d05].
- Execution feedback rounds: accuracy rose over rounds 1 to 3 in Wang et al. (26, then 31, then the final figure; the last value was not recorded in our files) [d01].
- Handing a gold reasoning chain (True Detective, 27 to 83) [a27]. This is an upper bound, not a method.
- Code-computed hedging and parsimony features over a model judge [b10].
- An explicit instruction to flag unanswerable items, for some models (GPT-4o 0.42 to 0.98) [d16].
- Matched in-distribution demonstrations on InAbHyD [b12].
- State machine with confidence-gap gate on diagnosis [c20].
- Preference training on label-free GEAR scores: small gains on 7B models (Llama-3.1-8B top-1 0.000 to about 0.03) [a25, c13].

Did not work:

- Voting without a check (ACRE 64.0 to 65.0) [c08].
- Model as its own interpreter [c09].
- LLM likelihood reranker for hypotheses [d02].
- Consistency as a selection signal [c02].
- Fixed few-shot demos (GPT-4 41.7 to 28.7) [c18].
- Prompt diversity among voters [d12].
- Chain of thought when exceptions exist (12.5 rounds vs 2.9) [d14].
- Instruction rescue for reasoning models like o3-mini-high (0.00 to 0.02) [d16].

---

## 6. Language models

### 6.1 Overall picture

1. **Selecting** among given explanations is close to human on short items. GPT-5.4: ART 87.2 (human 91.4), e-CARE 88.0 (human 92.0). Qwen2.5 3B, 7B, 72B on ART: 65.8, 75.8, 83.6 [c15]. So size matters here.
2. **Generating** explanations is far weaker. ProofWriter abductive 21.5, DDXPlus hit@3 63.0 generated vs 98.7 ranked [c16].
3. **Abduction trails deduction on the same content**: GPT-4 41.67 vs 72.22 [b13]. Pooled medians 42.50 vs 79.96 are a rough ordering only; they pool different models, methods and datasets (critique C). The like-for-like gap is Abe et al.
4. **Long, open tasks**: True Detective 42.9 (human 47.0); MuSR 60.8 to 68.0 vs human 92.1.
5. **Number of causes** is the strongest difficulty axis (section 3.3).

### 6.2 What changed performance, and by how much

| Change | Effect | Source |
|---|---|---|
| Execution-checked hypothesis search (ARC, GPT-4) | 17 to 30 (33 with human pick) | [a28] |
| Same loop on ACRE | raw 64.0 to 82.5; task 28 to 59 | [c07] |
| Same loop on MiniARC | raw 33.1 to 18.7 (worse) | [d07] |
| Ensemble induction plus transduction with a fit gate | 18.78 / 15.25 to 26.50 | [d05] |
| Replace code interpreter with LM interpreter | ACRE 82.5 to 70.0 raw; MiniSCAN above 80% task to near 0 | [c08, c09] |
| Gold reasoning chain | GPT-4 27% to 83% | [a27] |
| Chain of thought | GPT-4 27% to 38% on True Detective; hurts exception learning (2.9 to 12.5 rounds) | [a27, d14] |
| Self-consistency vote | ACRE 64.0 to 65.0 | [c08] |
| Few-shot | GPT-4 41.7 to 28.7; Llama-3-70B to 75.5 | [c18] |
| More reasoning effort | attribution 0.37 to 0.41 to 0.47 | [d28] |
| Reasoning fine-tuning | abstention recall -24% | [d15] |
| Explicit "flag unanswerable" instruction | GPT-4o 0.42 to 0.98; o3-mini-high 0.00 to 0.02 | [d16] |
| Code virtues vs GPT-3.5 judge | +17.5 average | [b09] |
| Structural hints in system prompt | weaker models score at all only with strong hints | [b15] |
| SFT on synthetic InAbHyD (Qwen3-4B) | strong accuracy +11.0 at height 1 | [c05] |
| Larger model (Qwen2.5 on ART) | 65.8 to 75.8 to 83.6 | [c15] |

### 6.3 Failure types

InAbHyD error types [a23, c06]: wrong direction of a relation; unnecessary hypotheses that ignore the ontology; trivial hypotheses that restate the observation; hallucinated entities, often copied from demonstrations. Graph of States adds fabricated evidence, context drift, failed backtracking, early stopping [c20]. Models over-rationalise wrong options by adding premises; larger models do this more [b10]. Abe et al. find belief bias like humans and a pull to always choose an explanation [b13].

### 6.4 Do models "do abduction"

Floridi et al. say token-completion models do not (no measured results). Imran et al. found GPT-4o picked the right persona in one of three cases (84% vs prior 49%), not GPT-4o mini. Pareschi has anecdotes without a baseline [a30, c25, c26]. K21 contested. Not relevant to engineering: judge by checked output (G10).

### 6.5 Simplicity in models

Small open models learn simpler Boolean concepts better than complex ones (Pearson r with complexity from -0.854 to -0.961) [c24]. In theory in-context learning has a compression pressure [d30]. But on InAbHyD, models fail to give the simplest explanation set even when they explain [a22, c05]. Nobody tested whether adding an explicit simplicity score helps LLM selection, apart from parsimony features in IBE-Eval (older models).

---

## 7. What our agent should take

Mark key: [E] established, [S] single-source, [C] contested. Schema part G/S/O/memory.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| A1 | Abduction output is a proposal only. A candidate counts as accepted only after code has run it. Already in G3 and G5; make the rate of S3 candidates rejected at S4 a logged number. | G3, G5, S3/S4, logging | [E] K01 | a01-a04 |
| A2 | In S0, route by a cheap check: can some short program fit the examples. Use hypothesis-then-test only when the rule is short and symbolic. If no candidate fits after N tries, switch to direct answering and log it. | S0 | [E] K28, K02 | a28, a29, d05-d08 |
| A3 | S4 must run candidates by code, not by the model re-reading its own rule. Keep a code runner as the only test. | S4, G1, G5 | [E] K02 (K03 supports) | a28, c07-c09, d05 |
| A4 | The fit gate must include a part the candidate was not fitted to: held-out examples or a differential test where two live candidates disagree. Measure each gate's own precision. | G3, S4, S7 | [E] K25 | d09, d05, d04, d18 |
| A5 | Log pool coverage next to final accuracy: for each solved or failed item, was a correct candidate anywhere in the pool. Makes selection loss visible. | logging (section 6), S7 | [E] K23 | d03, d10, d12, d13, d02 |
| A6 | Log implementation loss separately: a correct hypothesis that failed to become a correct program. In the one measured case this was the larger loss. | logging, S4 | [S] K24 (logging is cheap, so add) | d01 |
| A7 | Put an abduction item class in our bench; never infer abduction skill from deduction scores. | bench, S0 class record | [E] K07 | b13, c17, c18 |
| A8 | Treat generation as the weak half. Spend tokens on S3 diversity and S7 code selection, not on a model judge. | S3, S7, G5, G8 | [E] K04 | a26, b16, c15, c16 |
| A9 | No fixed few-shot exemplars in S3 unless tested per class and model. Never copy exemplar entities into new tasks. | S3 | [E] K09 | b12, c05, c18 |
| A10 | Do not rely on the model to say "no candidate fits". Any bad-lot signal must come from code (for example no candidate passes the unfitted test). | G6, S7, S8 | [E] K08 | b13, c18, d15, d16 |
| A11 | Expect accuracy to fall as the number of required causes rises. Set S0 mode and budget with the cause count in mind (G12). | S0, S2, S6 | [E] K06 | a22, b11, b14, a24, d28 |
| A12 | Keep the honest framing: loveliness is not likeliness. Never accept on a virtue score alone; acceptance needs a passed unfitted check (G3). | G3, S7, S8 | [E] K18 (philosophical), K17 contested | a05, a20, a21 |

### 7.2 Test first (not established; goes to UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Code-computed virtue score (parsimony, hedging count, scope) for S7 against vote and a blind judge | S7, G5 | [S] K11 | b09, b10, c01-c03, d10, d11 |
| T2 | Code-checked good-enough gate that flags "no candidate passes" | S7, S8, G6 | [S/open] K18, K29 | a20, d05, d15-d17 |
| T3 | Three-selector comparison: vote, blind model judge, code consistency plus held-out fit | S7 | open K31 | d10-d12, d31 |
| T4 | Code-built "what changed" table in S2 and an impasse operator at S6 for interacting causes | S2, S6 | [S] K22, K30 | b14, b15, d28 |
| T5 | Keep an exceptions list; do not let self-explanation overwrite case memory | S2, memory | [S] K15, K27 | a13, d14, d25 |
| T6 | Explanatory bonus of about 0.01 for near-tie breaking in S7 | S7 | [C] K17, K26 | a15, a16, d19, d20 |
| T7 | Parsimony count (hypotheses not needed to cover observations) as an S7 tie-break | S7 | [S] K10 | a22, b12, c05 |
| T8 | Simplicity weight that depends on data complexity; count unexplained root assumptions | S7 | [C] K13, K33 | a08-a11, d21-d24 |
| T9 | Diversity-aware top-k instead of first-passing (GEAR diversity, behaviour groups) | S7 | [S] K12 | a24, c13, d31 |
| T10 | Extracted fact table in S2 as a substitute for a "golden chain" | S2 | [S] K05 | a27, b17 |
| T11 | State machine with confidence-gap gate for open diagnosis tasks | S6, G9 | [S] K19 | c20, c21 |
| T12 | Held-out gate (G3) at equal tokens on the Hypothesis Search setup | S4, S7 | [S] K24 | d01 |
| T13 | Contextual gate with "must cover" and "must leave alone" groups to block local fixes | G3, S7 | [S] K32 | d17 |

---

## 8. Concrete tests on our bench

All arms run at equal tokens, setup cost counted (G7). "Plain" means one model, direct or short reasoning.

| Test and item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|
| B1 (T12) ARC-style rule items with hidden test pairs, 100 items | (a) plain; (b) propose-code-test with fit gate only; (c) same plus held-out gate; (d) vote over programs | exact-match rate; pool coverage; false accepts | (c) beats (b) by 2 to 4 points (K24 says about 3 in 100 on selection); (b) beats (a) only on items where some short program fits |
| B2 (T1, T3) Candidate pools with known truth (from ARC and rule tasks, N = 8 to 16 candidates) | vote; blind model judge, length-normalised; code consistency plus held-out fit; code virtue score (parsimony, hedging, scope) | top-1 hit rate vs oracle; gap to oracle | code fit beats vote; judge ties vote (USC: 90.2 vs 90.4); virtue score adds little on hard items (IBE-Eval only tested easy sets) |
| B3 (T2) Pools with the true rule removed (distractors only) plus a transfer set | model's own "none fits"; code gate "no candidate passes unfitted test"; combined | detection of bad lot (recall); false alarm on pools with a truth | code gate flags most bad lots; model alone near 0 (GPT-4 0.00%) |
| B4 (T4) Hidden-cause ladder, 1, 2, 3 interacting causes (Elenchos-style) | plain; plain with extended thinking; code "what changed" table in S2; table plus S6 operator | exact attribution accuracy by k | table lifts k = 2 and k = 3 above plain; extended thinking adds under 10 points (0.37 to 0.47 seen) |
| B5 (T5) Rules with exceptions (80% rule plus listed exceptions) | direct; self-explanation first; self-explanation plus separate exceptions list | rounds to learn all labels; final accuracy | list closes most of the 2.9 vs 12.5 gap |
| B6 (T6) Rule-ranking task with sequential observations | bonus c in {0, 0.01, 0.03, 0.1} as near-tie breaker | rate of early wrong commitment; time to right rule | c = 0.01 ties or beats c = 0; c = 0.1 shows early false confidence |
| B7 (T8) Two item sets: simple truth and rule-with-exceptions | no simplicity term; fixed simplicity weight; data-dependent weight | accuracy on each set | fixed weight wins on simple set, loses on exception set; data-dependent weight is best on average |
| B8 (T3, T9) Pools from B2 | first-passing; top-k by behaviour group; top-k by group plus diversity | accuracy and held-out generalisation | diversity helps when truth is under-represented; otherwise equal |
| B9 (A2) Mixed items: symbolic rule items and perceptual items | always hypothesis-then-test; always direct; S0 route by "does any short program fit" | accuracy by class | route beats both fixed policies; MiniARC-like items return to direct |
| B10 (T10) True Detective-style long items | plain; CoT; code-extracted fact table; table plus CoT | choice accuracy | table closes part of the 38 to 83 gap |
| B11 (T13) Rule repair items | gate on observed case only; gate with "must cover" and "must leave alone" groups | accepted-but-wrong rate | two-group gate cuts trivial local fixes |
| B12 (A5, A6) Every run above | logging only | coverage minus accuracy; implementation loss | shows where the loss is before building any selector |

---

## 9. What does not transfer, and why

- **Human simplicity preference as a prior.** One lab, the effect depends on wording, causal structure and domain; outside labs find complexity matching or complexity preferred. An LLM's pool need not be simple. (K13, K33.)
- **Douven and Schupbach credence data.** Descriptive, N=26, one study reanalysed. A model's output is not a credence reported by a person.
- **IBE-versus-Bayes simulations.** Coins and urns with hand-set bonus. A language model's pool is not a probability space with known likelihoods. The early-overconfidence result transfers as a warning only.
- **IBE-Eval numbers.** GPT-3.5 and Llama 2 on COPA and E-CARE, two short easy sets. Do not assume the +17.5 holds with modern models.
- **Hypothesis Search and Qiu et al. numbers.** GPT-4 and 2023 to 2024 setups. Current reasoning models were not tested with these loops. The direction (code test helps) is robust; the size is not.
- **Synthetic benchmarks** (InAbHyD, GEAR, Elenchos). Show failure patterns, not real-world rates. Real-world abduction (diagnosis, debugging) rests on Graph of States, one paper.
- **Peirce, Hanson, Harman, Lipton.** Secondhand through SEP. They give the frame, not numbers. Their "creative leap" is not a mechanism; we have no way to code it, only to sample and test.
- **Training results** (GEAR DPO, UNcommonsense imitation, SFT on InAbHyD). We do not train. Only the scoring ideas transfer.
- **Multi-role frameworks** (Theorem-of-Thought with abductive, deductive, inductive agents). Conflicts with G9 and G4; gains were on 7B models in one study.
- **Retrieval abduction** (LAMP, abductive RAG). System-specific and weakly documented (K20); not a basis for an operator.
- **Whole-process claims** ("LLMs do not really abduct"). Does not change what the scaffold should do (G10).

---

## 10. Open questions

1. Do code-computed virtues (parsimony, scope, hedging, consistency) beat vote and a blind judge on modern models and hard tasks? Only Dalal et al. tested, on easy sets with old models.
2. Does a held-out gate at equal tokens recover the selection share of the loss on Hypothesis Search? Estimate about 3 tasks in 100; not measured.
3. Can a code gate detect a candidate pool with no true explanation? No distractor-only benchmark exists.
4. What predicts the sign of hypothesis-then-test by class (plain pass rate, rule length, model size)? Pattern read across three papers; no head-on test.
5. What bonus size avoids early false confidence for language-model hypothesis pools? Only simulations.
6. How does accuracy fall with the number of interacting causes for current reasoning models, and does a code-built diff table or an impasse step flatten it?
7. Is a simplicity weight a good prior for LLM selection? Needs a test with simple truths and truths with exceptions, and an outside lab replication of the human result.
8. Does set-level scoring (consistency, generalisation, diversity) help as an inference-time selector?
9. Does self-explanation in S2 hurt when the truth has exceptions in our scaffold, and with 2025 to 2026 reasoning models?
10. Are there external replications or failed replications of Lombrozo 2007 and Douven and Schupbach 2015? None found.
11. How much of the open-generation weakness (ProofWriter 21.5, hit@3 63.0) can be recovered by more draws plus code selection?
12. Do explanation preferences differ when the task says "most likely" versus "most satisfying"? (Human wording effect 46% vs 17%.) Does an equivalent wording effect exist in prompts?
13. Why does the newest model score lower than an older one on MuSR (60.8 vs 68.0)? Prompt format, verbosity, or reasoning mode?

---

## 11. Sources

[V] = opened this session by a researcher in the series (page or PDF text read). [M] = snippet or abstract only. Where an evidence line was marked opened but only an abstract page was available, it is marked [M].

### Philosophy
- [V] SEP Abduction: Peirce. https://plato.stanford.edu/entries/abduction/peirce.html (a01, a02)
- [V] SEP Scientific Discovery (Hanson, context distinction, discovery machines). https://plato.stanford.edu/entries/scientific-discovery/ (a03, a04)
- [V] Douven, SEP Abduction (ABD1-3, bad lot, Bayes vs IBE, virtues). https://plato.stanford.edu/entries/abduction/ (a05-a07)
- [V] Dellsen (2020) Explanatory Consolidation: From Best to Good Enough. https://philsci-archive.pitt.edu/id/eprint/17290/1/Consolidation%20PPR%20Accepted%20Web.pdf (a20, a21)
- [V] Pettigrew (2021) On the pragmatic and epistemic virtues of IBE, Synthese. https://pmc.ncbi.nlm.nih.gov/articles/PMC8403472/ (a15-a17)
- [V] Dellsen and Trpin (2025) Testing Abductions From Uncertain Evidence. https://philsci-archive.pitt.edu/27291/1/Testing%20Abductions%20Web.pdf (a19)
- [M] Climenhaga (2017) IBE made incoherent. https://philarchive.org/rec/CLIITT (b23)
- [M] Cabrera (2017) Can there be a Bayesian explanationism. https://philarchive.org/rec/CABCTB (b24)
- [M] Douven (2013); Douven and Wenmackers (2017). https://hal.sorbonne-universite.fr/hal-02869743/file/EcoRatExRe.pdf (b26; fetch blocked)
- [M] Schupbach simulation summary, metapsychology review. https://metapsychology.net/?p=8055 (b22)
- [M] Wojtowicz and DeDeo (2020) From probability to consilience. https://doi.org/10.1016/j.tics.2020.09.013 (d27)
- [M] Farmer (2026) Abduction Without a Body. https://arxiv.org/abs/2608.02505 (c27)
- [V] Floridi, Morley, Novelli, Watson (2025) What kind of reasoning is an LLM doing. https://arxiv.org/pdf/2512.10080 (a30)

### Human psychology
- [V] Lombrozo (2007) Simplicity and probability in causal explanation. https://cognition.princeton.edu/sites/default/files/cognition/files/simplicity_probability.pdf (a08-a11, b01-b04)
- [V] Lombrozo (2016) Explanatory preferences shape learning and inference. https://cognition.princeton.edu/sites/default/files/cognition/files/explanatory_prefs_tics.pdf (a12, a13)
- [M] Liquin and Lombrozo (2018) Causal structure and probability information. https://journalpub.escholarship.org/cognitivesciencesociety/article/29224/galley/19095/download (b05; abstract page only)
- [V] Douven and Schupbach (2015) Probabilistic alternatives to Bayesianism. https://pmc.ncbi.nlm.nih.gov/articles/PMC4410515/ (a14, b06, b07)
- [M] Douven and Schupbach (2015) The role of explanatory considerations in updating. https://doi.org/10.1016/j.cognition.2015.04.017 (d26)
- [V] Trpin and Pellert (2019) IBE in uncertain evidential situations. https://philsci-archive.pitt.edu/id/eprint/14236/1/IBE_in_uncertain_evidential_situations.pdf (a18, d19)
- [M] Trpin and Pellert catalogue page. https://madoc.bib.uni-mannheim.de/63332/ (b08)
- [V] Douven (2020) The ecological rationality of explanatory reasoning. https://hal.sorbonne-universite.fr/hal-02869743/file/EcoRatExRe.pdf (d20)
- [V] Lim and Oppenheimer (2020) Explanatory preferences for complexity matching. https://doi.org/10.1371/journal.pone.0230929 (d21)
- [M] Zemla et al. (2017) Evaluating everyday explanations. https://doi.org/10.3758/s13423-017-1258-z (d22)
- [M] Johnson, Valenti, Keil (2019) Simplicity and complexity preferences. https://doi.org/10.1016/j.cogpsych.2019.05.004 (d23)
- [M] Pacer and Lombrozo (2017) Ockham's razor cuts to the root. https://doi.org/10.1037/xge0000318 (d24)
- [M] Williams, Lombrozo, Rehder (2013) The hazards of explanation. https://doi.org/10.1037/a0030996 (d25)
- [M] Bonawitz and Lombrozo (2012) Occam's rattle. https://cognition.princeton.edu/document/149 (b25)

### Language models
- [V] Bhagavatula et al. (2019) ART. https://arxiv.org/abs/1908.05739 (a26)
- [V] Del and Fishel (2023) True Detective. https://arxiv.org/pdf/2212.10114 (a27, b17)
- [V] Wang et al. (2024) Hypothesis Search. https://arxiv.org/pdf/2309.05660 (a28, b18, d01, d02)
- [V] Qiu et al. (2024) Phenomenal Yet Puzzling. https://arxiv.org/html/2310.08559 (a29, c07-c09, d07)
- [V] Sun and Saparov (2025/2026) Do Language Models Follow Occam's Razor. https://arxiv.org/pdf/2509.03345 (a22, a23, b11, b12, c04-c06)
- [V] He et al. (2025) GEAR. https://arxiv.org/pdf/2509.24096 (a24, a25, b19, b20, c12, c13, d31)
- [V] Dalal et al. (2024) IBE-Eval. https://arxiv.org/pdf/2402.10767 (b09, b10, c01-c03)
- [V] Abe et al. (2026) Abductive reasoning with syllogistic forms. https://arxiv.org/pdf/2603.06428 (b13, c18)
- [V] Steiglechner, Mahler, Lohmann (2026) Elenchos. https://arxiv.org/pdf/2607.12733 (b14, b15, d28)
- [V] Salimi et al. (2026) Wiring the Why. https://arxiv.org/html/2604.08016v2 (b16, c15-c17)
- [V] Liu, Neubig, Andreas (2024) An Incomplete Loop. https://arxiv.org/abs/2404.03028 (c14)
- [V] Zhao et al. (2024) UNcommonsense Reasoning. https://arxiv.org/abs/2311.08469 (c10, c11)
- [V] Shi et al. (2023) LAMP. https://arxiv.org/abs/2305.16646 (c19)
- [V] Luo et al. (2026) Graph of States. https://arxiv.org/abs/2603.21250 (c20, c21)
- [V] Abdaljalil et al. (2025) Theorem-of-Thought. https://arxiv.org/abs/2506.07106 (c22)
- [V] Lin (2025) Abductive inference in RAG. https://arxiv.org/abs/2511.04020 (c23)
- [V] Wang, McCoy, Steinert-Threlkeld (2024) Boolean complexity in in-context learning. https://arxiv.org/abs/2412.02823 (c24)
- [V] Imran, Lamb, Atkinson (2025) Out-of-context abduction. https://arxiv.org/abs/2508.00741 (c25)
- [V] Pareschi (2023) Abductive reasoning with GPT-4. https://arxiv.org/abs/2307.10250 (c26)
- [V] Kim (2022) Can language models perform abductive commonsense reasoning. https://arxiv.org/pdf/2207.05155 (b21; course report, table not cleanly read)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/pdf/2407.21787 (d03, d04)
- [V] Li et al. (2024) Combining induction and transduction. https://arxiv.org/pdf/2411.02272 (d05, d06)
- [V] Hua et al. (2025) InductionBench. https://arxiv.org/pdf/2502.15823 (d08)
- [V] Wei et al. (2025) CodeARC. https://arxiv.org/pdf/2503.23145 (d09)
- [V] Chen et al. (2023) Universal Self-Consistency. https://arxiv.org/pdf/2311.17311 (d10)
- [V] Chen et al. (2022) CodeT. https://arxiv.org/pdf/2207.10397 (d11)
- [V] Nitarach (2026) AIMO 3 lessons. https://arxiv.org/pdf/2603.27844 (d12)
- [V] Li and Li (2026) From discovery to decision. https://arxiv.org/pdf/2610.01014 (d13)
- [V] Liu et al. (2025) Mind Your Step (by Step). https://arxiv.org/pdf/2410.21333 (d14)
- [V] Kirichenko et al. (2025) AbstentionBench. https://arxiv.org/pdf/2506.09038 (d15)
- [V] Hashemi et al. (2025) DNR Bench. https://arxiv.org/pdf/2503.15793 (d16)
- [V] Cooper, Sadhu, Velasquez (2026) DeFAb. https://arxiv.org/pdf/2606.18557 (d17)
- [V] Reddy, Challaram, Basu (2026) Reason Less, Verify More. https://arxiv.org/pdf/2607.07405 (d18)
- [V] Maasch et al. (2025) Compositional causal reasoning. https://arxiv.org/pdf/2503.04556 (d29)
- [V] Elmoznino et al. (2025) In-context learning and Occam's razor. https://arxiv.org/pdf/2410.14086 (d30)
