# Evidence and probability reasoning: deep document

*Subfield E11.09. Built from evidence_a to evidence_d.jsonl (a01-a30, b01-b31, c01-c28, d01-d19), claims.jsonl (K01-K30) and critique.md in this folder. Evidence ids in brackets. Where the critique corrected an earlier line, the corrected version is used here. Schema parts refer to SCHEMA.md v0.2 (guardrails G1-G12, states S0-S9, operators O1-O8, section 4b "not to add").*

## 1. What it is

This subfield is about how people, and now language models, read evidence that comes with numbers. The core task: a piece of evidence (a DNA match, a test result, a witness, a shoe print) has some probability under one story and some probability under a rival story. What should we believe afterwards?

Three ideas carry most of the field.

- **Bayes' rule in odds form.** Posterior odds = likelihood ratio (LR) x prior odds. The LR is how much more likely the evidence is if hypothesis H1 is true than if H2 is true. It is not the probability that either hypothesis is true.
- **The prosecutor's fallacy (flipping the conditional).** Treating P(evidence | innocent) as if it were P(innocent | evidence). A random-match probability of 1 in 1,000 gets read as "99.9% chance he is the source". The prior was dropped [a11, a12, b07].
- **The defence attorney's fallacy.** The mirror error: "many people share this profile, so the match is irrelevant". The match still raises the odds. Both names come from Thompson and Schumann (1987) [a16, not opened; numbers unverified].

The second strand is the study of **base-rate neglect and format**. The same Bayesian problem is solved by few people when stated in conditional probabilities, and by more when stated in natural frequencies ("8 of 1,000 women have the disease") [a01, a03].

The third strand is **how real fact-finders update**: jurors, judges, forensic scientists, lawyers. Findings: they under-update, ignore stated base rates, misread random-match probabilities, and cannot spot a flawed report [b04, b10, b12, b17].

The fourth strand is **the Bayesian-network (BN) programme** of Fenton, Neil and colleagues: model a whole case as a network of hypotheses and evidence, so that dependence, alternative explanations and explaining-away are explicit [a10, a25].

The fifth strand, new in 2023-2026, is **LLMs on these tasks**: how often they commit the fallacies, whether prompting helps, and whether offloading arithmetic to code or a solver fixes the rest (section 6).

Why it matters for our agent. The agent must weigh evidence in many tasks, not only legal ones. Any "given this test result, how likely is X" question has the same structure. The research gives us (a) a cheap representation change (counts), (b) a case for computing in code, and (c) a list of traps (dropped priors, dependent evidence, non-exclusive hypotheses, order effects) that a scaffold can check mechanically.

## 2. History and theories in depth

**1950s-1970s: conservatism.** Early work (Phillips and Edwards 1966; Peterson and Beach 1967, cited in b06) found people update in the right direction but too little. The gap grows with the amount of evidence (Schum 1966, cited in b06). Second-hand; originals not opened.

**1970s-1980s: base-rate neglect.** Kahneman and Tversky's lawyer-engineer problem and the cab problem (Tversky and Kahneman 1982; Bar-Hillel 1980). In the cab problem people answer near the witness accuracy (about 80%) while Bayes gives about 41% for the standard 85/15 version [a17, not opened; numbers from memory, do not quote as data]. Eddy (1982) reported that 95 of 100 physicians put the chance of cancer after a positive mammogram at 70-80% when the correct value is 7.8%. Casscells et al. (1978) found the same at Harvard [a02, second-hand via Gigerenzer and Hoffrage, who read the originals]. The mammography posterior: 0.8 x .01 / (0.8 x .01 + .096 x .99) = 0.078 (arithmetic checked in the critique).

**1987: legal fallacies named.** Thompson and Schumann gave the prosecutor's and defence attorney's fallacies their names [a16]. Their mock-juror data was never opened by us (paywall, d06). We cannot quote their percentages.

**1990s: the reconsideration.** Koehler (1996) argued that base rates are used much more than the neglect story claims: more when learned by experience or given as frequencies, when reliable, and when more diagnostic than the case information. He also argued that a mechanical "base-rate fallacy" label is normatively wrong when assumptions are unchecked [d05, abstract only]. This competes with the neglect narrative. Krynski and Tenenbaum (2007) found neglect shrinks when the problem is given as a causal structure (cited in b06).

**1995: the frequency-format account.** Gigerenzer and Hoffrage argued the mind is not Bayesian-blind; the probability format hides the algorithm. With natural frequencies (absolute counts from natural sampling) the computation is short [a01]. The evolutionary story (natural sampling) is an argument, not a tested result. The format effect is the tested part. Competing accounts: nested sets (Barbey and Sloman 2007, not in our evidence), and Fenwick, Campitelli and Thompson (2026), who say competence is a set of learned tools, not one privileged format [b22, abstract only].

**1990s-2010s: the legal debate.** Tribe (1971) and later critics: priors cannot be set, no number fits "beyond reasonable doubt", jurors cannot cope, Bayes conflicts with an open mind [a15]. Fenton, Neil and Berger (2016) answer each objection and argue for BNs [a10, a15]. Critics in 2025 argue LRs "have no place in criminal trials"; a reply says that confuses the expert's role with the jury's [b30, a27]. Practical obstacles (no software, data, training) may matter more than principle [b31]. This debate is unresolved [C].

**Case history: Sally Clark.** The expert squared 1 in 8,543 to get "1 in 73 million" for two cot deaths. The Royal Statistical Society called the squaring statistically invalid. Hill estimated that double SIDS was 4.5 to 9 times as likely as double murder; after one SIDS death the risk of a second is 6-10 times higher (Hill 2004, as cited). Conviction quashed 2003 [a28, b08]. Feeny and Stamboulid (2026) list three separate errors: assumed independence, treated a residual diagnosis as an explanation, and never compared with the rival explanation [b08]. Dawid: if background rates of double natural death are relevant, so are background rates of double murder [b09, second-hand]. Fenton (2014) adds that the Bayesian critique itself may have exaggerated the problem by not choosing exclusive and exhaustive hypotheses [a13, contested]. Other named cases: Lucia de Berk, Barry George, People v Puckett, Collins, OJ Simpson [a10].

**2000s-2020s: format and training for experts.** Hoffrage et al. (2000, Science) extended the frequency result to physicians and to legal professionals on DNA evidence [a07-a09]. Later work: training plus natural frequencies reached 89% in medical students; training effects fade; repeated exposure rivals lightweight training [b19-b21].

**2010s-2020s: forensic communication.** Experiments on how verbal, numeric and categorical conclusions move lay belief: belief change far smaller than the expert intended; a weak evidence effect; null results for conclusion format inside a full report [b10, b11, b14, b15].

**2023-2026: LLMs.** First wave: do models show human biases (Hagendorff et al. 2023 [b27]; Li and Rui 2024 [a19]). Second wave: prompting and fine-tuning (Qiu et al. [a23], Schoenegger et al. [c15]). Third wave: solver offloading and hybrid explanation (Nafar et al. [b24], Keppens [c01]), and legal-evidence order effects (Qiao et al., Bessis et al. [d07, d09]).

## 3. Core findings with exact numbers

Status: **E** established (2+ independent sources), **S** single source, **C** contested, **M** read second-hand or snippet only.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Physicians fail the mammography item in probability format | 95 of 100 gave 70-80%; correct 7.8% | Eddy 1982 via a02 | S, M |
| Casscells-type item: experts overstate | modal answer 95% (27 of 60); correct 2% | a09 | S |
| Natural frequencies raise Bayesian algorithm use (N=60 students, 15 problems) | probability standard 16%, short 28%; frequency standard 46%, short 50% | Gigerenzer and Hoffrage 1995 Study 1, a03 | E |
| Relative frequencies do NOT help; absolute counts do | relative frequency 60 vs probability 66 Bayesian algorithms (N=15, 24 problems) | a04 | S |
| Frequencies make strategies more consistent | consistency .32 to .49 (standard freq) vs .22 to .24 (standard prob) | a05 | S |
| Meta-analytic means across human studies | about 4% (probability) vs 24% (natural frequency), per problem | McDowell and Jacobs 2017, read via Weber et al. 2018, b01 | E, M (second-hand) |
| Legal professionals on DNA match, probability format | 13% of professionals and under 1% of 127 law students correct source inference | Hoffrage et al. 2000, a07 | S |
| Same, natural-frequency format | 68% professionals and 44% students | a07 | S |
| Guilty verdicts depend on format | probabilities: 55% of students (45% of professionals, figure not re-seen, OCR garbled); frequencies: 32% and 33% | a08 | S |
| People revert to probabilities even when given frequencies (N=180) | 49% still computed with probabilities; only 18% of probability-format participants switched to frequencies; frequencies used in 34% of 360 tasks | Weber et al. 2018, b02 | S |
| Context moves difficulty | frequencies: heroin 51% vs car accident 22%; probabilities 22% vs 19%; pooled 20% vs 36% | b03 | S |
| Medical students (N=577) | probabilities 34%; frequencies 68%; training then probabilities 64%; training plus frequencies 89% | Feufel et al. 2023, b19 | S, M (abstract) |
| Tree vs formula training (N=231) | post 87.1% vs 86.0% (p=.86); 1 month 72.4% vs 68.1% (p=.40); students with no prior training: 74.9% vs 58.7% (p=.02) | Kim et al. 2024, b20 | S, M |
| Repeated exposure (N=256 laypeople) | no training PPV 34.9 to 59.9 to 58.5%; textual 38.6 to 65.7 to 64.3; dynamic 48.8 to 70.8 to 65.5; held 8-10 days | b21 | S |
| Clinicians fail Bayesian items with high confidence (N=86) | 65.1% to 93.0% wrong by item; 74.4% negative confidence-weighted score on hardest item | Hefter et al. 2026, b18 | S |
| Prosecutor's fallacy, island example | prior 1/10,000, RMP 1/1,000 (LR 1,000): posterior source about 9%, not 99.9% | Fenton et al. 2016, a11, a12 | E |
| Sally Clark | 1/8,543 squared = 1 in 73 million; Hill odds 4.5:1 to 9:1 for double SIDS over double murder | a13, a28, b08 | E |
| Cohen's conjunction paradox | two witnesses at 70%: product 0.49; BN with reliability node resolves it | a14 | S |
| Jurors update the right way but not by the Bayesian amount (N=155) | stated base rates 0.01 and 0.001; subjective priors 0.534 abuse, 0.267 disorder; evidence stage F(2.545,315.587)=85.30, eta2=.408 | Shengelia and Lagnado 2021, b04 | S |
| Telling jurors causes may co-occur does not fix updating | abuse F(2,124)=1.20, p=.304; disorder F(2,124)=0.13, p=.881 | b05 | S |
| Belief change far smaller than experts intended | over 350,000 times smaller (Martire et al., as reported) | b10 | S, M |
| Weak evidence effect | weak inculpatory evidence lowers guilt belief, mostly verbal; Exp 1 N=494, Exp 2 N=411 | Martire et al. 2013, b14 | S, M |
| Conclusion format has no detectable effect | Exp 1 N=446 F(3,442)=0.102, p=.959; Exp 2 N=313 F(2,310)=0.255, p=.775; not-guilty 68.5% LR, 75.9% RMP, 72.3% verbal, 77.6% categorical | Martire et al. 2025, b15 | S (null) |
| Individual differences matter more than format | adj R2 = .257 (Exp 1), .343 (Exp 2) from comprehension, numeracy, need for cognition etc. | b16 | S |
| Professionals miss unsound reports (N=133) | reliability 3.3 vs 3.1, p=.094; 32% rated unsound report unreliable; fallacy noticed 7 times | de Roo et al. 2026, b17 | S |
| LLM: stereotype description kills base rates | correct odds ratio is 9; stereotype CS description: gpt-4o 1.25, gpt-4 1.18, claude-3-opus 1.68, gemini 2.58, mistral 1.62, llama 1.52, humans 2.02; bland description: 9, 9, 8.86, 6.36, 3, 9 | Li and Rui 2024, a19, d04 | E |
| LLM posterior tracks similarity | posterior-similarity Pearson 0.90-0.98; prior-posterior Spearman -0.84 to -0.90 | a20 | S |
| LLM prompt ladder | first three stronger instructions left correlations unchanged; "compute / posterior probability" wording forced step-by-step Bayes (GPT-4o only) | a21 | S |
| LLMs update poorly over 5 rounds | Gemma about 37% in round 1 and 5; CoT, numeric formats, 30 rounds gave no meaningful gain | Qiu et al. 2025, c07, c08 | E |
| Bayesian-teaching fine-tune | about 80% agreement with Bayesian assistant (simulated users; humans much lower); 3 models of 7-9B | c09 | S |
| CoT collapses with network size (BLInD, 100 items per split) | GPT-4 zero-shot V2..V10: 79,63,27,10,17,6,5,7,6; few-shot CoT: 78,64,36,25,22,16,7,7,7; basic QA 0-3 | Nafar et al. 2024, d01 | E |
| Solver offloading restores accuracy | GPT-4 ProbLog: 99,98,100,100,96,97,97,98,96; Monte Carlo 100 down to 88; plain Python (PAL) 99 down to 10; number extraction 100 | d02, c11 | E |
| Unconstrained LR from a BN fails silently | cross-transfer net: 390.4 vs correct 18.07 (about 21x); jury net: 4 of 100 runs 1.21 vs 0.662 | Keppens 2026, c01-c03 | S |
| Hybrid prompt (exact marginals and LR supplied, do not recompute) | 100% correct over 100 runs per network; fewer tokens | c04 | S |
| Bayesian-reasoning prompt hurts forecasts | Brier +0.03 vs control (t about 5.4); extremity 17.2-19.9 vs 11.9-13.4 points from 0.5 | Schoenegger et al. 2025, c15, c17 | S |
| Base-rate-first prompt helps slightly | Brier -0.011 to -0.016 | c16 | S |
| Belief entrenchment | Martingale Score positive in 51 of 54 CoT setups; 0.0 gives Brier below .25, 0.04 gives worse than random | He et al. 2025, c18, c19 | S |
| Forewarning GPT-4 about bias | 213 vs 138 words; correct bias named 5%; mean bias reduction 6.9%; framing 66% to 45% | Wang and Redelmeier 2025, b25 | C |
| o1 on clinical vignettes (1,800 responses) | base-rate neglect 0%; hindsight 100% vs 47.8%; Occam's razor 100% vs 0% | b26 | S |
| CRT | ChatGPT-3.5 59%, ChatGPT-4 96%; CoT lifted davinci-003 from 5% to 28% | Hagendorff et al. 2023, b27 | S |
| Evidence order, GPT-4o on Sally-Clark-style vignette (956 trials) | final guilt 0.66 (defence first) vs 0.40 (defence last); order F(1,994)=4645.65, partial eta2 .83; OR 0.002 for guilty when defence last; step-by-step OR 10.55 | Qiao et al. 2026, d07 | E (with d09) |
| Newer model, same effect, weaker | GPT-4o recency F(1,711)=424.76, means 4.24 vs 6.04; GPT-5.2 4.75 vs 5.35 | Bessis et al. 2026, d09 | E |
| Generic role/care prompts | limited, inconsistent effects (4 conditions x 720 trials per model) | d10 | C |
| GPT-5 joint probabilities | conjunction fallacy 18.8% vs 58.5% for humans (N=553 matched profiles) | Frontiers 2026, d11 | S |
| Probability words to numbers | abstention 93.5, 93.0, 76.1, 30.9%; "usual" humans 75.4% vs LLMs 15-52% | Jackson et al. 2025, d15 | S |
| Token bias in Linda-type items | answers drop when names change; n=500 and n=100 sets, ten models | Jiang et al. 2024, c23 | S |
| Online participants with LLM help | 57% scored 5 of 5 vs human ceiling about 24% (N=148) | b28, d12 | S, M |

## 4. Mechanisms and models

Each is written so that code can implement it.

**M1. Odds-form update (the core).**
Input: prior odds P(H1)/P(H2); for each evidence item e_i, LR_i = P(e_i|H1)/P(e_i|H2).
Output: posterior odds = prior odds x product of LR_i. Valid only if the items are conditionally independent given each hypothesis, and H1, H2 are exclusive and exhaustive. Convert to probability p = odds/(1+odds).
Check: island example. Prior 1:9,999, LR 1,000, posterior odds about 1:10, p about 9% [a11, a12]. A script does this in one line. The model's job is only to supply the numbers and state the hypotheses.

**M2. Natural-frequency rewrite (operator O6, change representation).**
Steps: pick N (1,000 or 10,000). Count cases with H: N x prior. Of those, count with E: x sensitivity. Of those without H, count with E: x false-positive rate. Answer = (cases with H and E) / (all cases with E). Mammography: 1,000 women; 10 with cancer; 8 of them test positive; of 990 without, about 95 test positive; answer 8/(8+95) = 7.8%.
Checker (code): counts are integers (or rounded and flagged), branches sum to N, answer equals M1.
Important: absolute counts from natural sampling help; relative frequencies do not [a04]. The step must produce absolute counts. Humans often do not self-translate (18% [b02]), and LLMs without a hint use symbolic algebra only [d03]. So the step must be forced by the program, not left to the model.

**M3. Likelihood-ratio ledger.**
Each evidence item gets a row: statement, P(e|H1), P(e|H2), source of each number, dependence on earlier items, reference class. Code multiplies the LRs. The ledger exposes two traps: (a) a missing P(e|H2) (the prosecutor's fallacy shows up as a ledger with one column); (b) items marked dependent get a joint likelihood, not a product.

**M4. Hypothesis-pair check (exclusive and exhaustive).**
Before any LR is used, list H1 and H2 and check: can both be false? can both be true? If yes, the LR does not give a posterior. Fenton's critique of the Clark reanalysis rests on this [a12, a13]. Shengelia and Lagnado found people count evidence for one cause as against the other (zero-sum thinking) even when told both can be true [b05]. Telling is not enough; the ledger must have a column "both possible?".

**M5. Dependence handling.**
Clark: independence assumed, wrongly. Rule: when two items share a cause (same family, same lab, same sample), do not multiply marginal rates. Either elicit P(e2|e1,H) or mark "dependent, joint rate needed". Keppens' jury observation network shows explaining-away: evidence for one cause lowers the other, LR 0.66 [c03, c05].

**M6. Bayesian network solver (offload).**
The LLM translates text into a ProbLog program or a BN spec; a solver computes. On BLInD, GPT-4 + ProbLog stayed 96-100% to 10 variables when all numbers and links were stated in text [d02]. Monte Carlo was 88% at the largest size. Plain-Python generation fell to 10% [d02]. So: a probabilistic-logic engine, not "write some Python". Structure can also be proposed by an LLM from variable names (PromptBN, SHD 0 on Asia) but only on textbook networks [c25]. Wong et al. use an LLM to translate sentences into conditions and queries for a probabilistic program [c24], illustrative only.

**M7. Hybrid explanation.**
Compute marginals and the LR symbolically; hand the numbers to the model; tell it not to recompute; let it write the explanation. Keppens: 100% numerically correct over 100 runs per network and fewer tokens. With marginals only the model missed the structural reason in the explaining-away case; adding partial belief-propagation messages fixed that [c04, c05].

**M8. Order-invariance check.**
Run the same evidence set in two or more orders, accumulate log-odds in code, flag if the verdict or posterior differs by more than a threshold. Rational updating is order-invariant for independent items. LLM order effect is huge (GPT-4o 0.66 vs 0.40) [d07]. The mechanism is recency plus conservative updating; the model's stated numbers move too little [d08]. Caveat: reversing order also changes the story, as Bessis et al. note [d09].

**M9. Martingale monitor.**
Under rational updating, the expected posterior equals the prior, so the revision should not be predictable from the prior. Fit posterior-minus-prior on prior across items. A positive slope means entrenchment [c18]. It needs a set of items; usable as an offline diagnostic, not per problem.

**M10. Verbal-to-numeric calibration.**
LLMs map words like "likely" inconsistently and often refuse to give a number [d15]. Calibrate per model: elicit numbers for each verbal term across many contexts, store the median and range, and keep numeric LRs, not words, as the working currency.

**M11. Two-elicitation consistency.**
Li and Rui: the same model gave a prior of 2-4% when asked alone and 10-30% inside a posterior judgment [a20]. Check by asking the prior in isolation and comparing it with the implied prior inside the full question; flag a mismatch above a threshold.

## 5. What holds up

**Replicated and robust.**
- Format effect: probability format gives low accuracy; natural frequencies raise it, in several samples and a meta-analysis [a03, b01, b03, b19, b21]. The direction is solid. The size varies widely: 46-50% (students, 1995), 24% (meta-analytic mean), 36% pooled and 51% vs 22% by item (Weber), 68% (medical students), up to 89% with training. Do not quote one figure (critique).
- Experts fail too: physicians and legal professionals [a02, a07, a09, b18].
- Dropping the prior is the root of the prosecutor's fallacy and is formally resolved by M1 [a11, a12].
- Jurors under-update and neglect stated priors [b04, b10].
- LLMs: stereotype-driven base-rate neglect [a19, d04]; collapse of unaided CoT with network size [d01]; solver offloading works [d02]; evidence-order sensitivity in GPT-4o and GPT-5.2 [d07, d09].

**Failures, nulls and conditional results.**
- Relative frequencies did not help [a04].
- Format of the forensic conclusion made no difference for mock jurors (null, N=446 and 313; low power for small effects) [b15].
- Tree training vs formula training: no overall difference; benefit only for students with no prior formula training [b20].
- Telling jurors that causes need not be exclusive did not change updating [b05].
- Generic forewarning barely helped GPT-4 [b25]; generic role or carefulness prompts gave limited, inconsistent effects on order bias [d10].
- Bayesian-reasoning prompts worsened forecasts [c15].
- Chain-of-thought, numeric formats and 30 rounds did not fix LLM belief updating in a preference task [c08].
- Told to use natural frequencies, reasoning LLMs used them partially or inconsistently [d03].

**Moderators.**
- Numeracy and comprehension (adj R2 .26-.34) [b16]; cognitive reflection and expertise [b18].
- Evidence type: DNA statistics gave belief changes near intended; shoeprint statistics were undervalued [b13].
- Expert experience and institutional authority sway lay and professional ratings more than method [b13, b17].
- Problem context (51% vs 22%) [b03].
- Prior formula training [b20].
- Whether the person calculates with frequencies, not how the task was shown [b02].
- Description type for LLMs: bland vs stereotype [d04]. Response mode and role framing in GPT-4o (mock juror OR 7.49, legal expert 2.20 vs advisor) [d07].
- Model era: o1 shows no base-rate neglect on clinical vignettes [b26]; GPT-5 is far more coherent than humans on explicit probabilities [d11]; GPT-5.2 order effect is weaker than GPT-4o [d09].

**Interventions that worked (humans).** Natural frequencies; training plus frequencies (89%); repeated exposure (about +25 points, held 8-10 days) [b19, b21]. Fading: 87% post-test to 72% at one month [b20].

**Interventions that did not.** Generic warnings, relative frequencies, format changes in forensic conclusions, exclusivity reminders.

**Competing explanations.** (1) Format and ecological rationality [a01]. (2) Nested sets and causal structure (Krynski and Tenenbaum, cited in b06). (3) Learned tools [b22]. (4) Base rates are used when reliable and relevant; "neglect" is overstated [d05]. (5) Expectation account of the weak evidence effect [b14]. (6) Zero-sum thinking for juror errors [b05]. For LLMs: RLHF or similarity-heuristic conjecture [a21, untested], metacognitive myopia [a24, theory], token bias [c23].

**Contested.** Whether BNs should enter court [a15, b30, b31]. Whether Fenton's exclusivity point means the Clark critique was exaggerated [a13]. Whether forewarning works [b25 vs d10].

**Source quality warnings (from critique).** Thompson and Schumann (1987), the cab problem and Koehler (1996) numbers were never opened. Several LLM items are 2026 preprints or workshop papers (Keppens, canary paper, b17, b18, b21) with no replication. Mock-juror data is MTurk. Many lines are reviews without numbers. Qiu et al. accuracy of about 80% was for simulated users; humans were much lower, and the Gemma baseline gap depends on the preference distribution (37% in the main figure, about 60% when filtered to human-like preferences).

## 6. Language models

**What the models do.**

| Task | Result | Source |
|---|---|---|
| Base rate, bland description | Bayes-correct (odds ratio 9) for gpt-4o, gpt-4, llama-3-70b; claude-3-opus 8.86; gemini 6.36; mistral 3 | d04 |
| Base rate, stereotype description | odds ratio 1.2-2.6 (correct 9); humans 2.02 | d04 |
| Recalled base rate | prior 2-4% alone but 10-30% inside posterior; posterior tracks similarity (r .90-.98) | a20 |
| Clinical base-rate vignette | o1 100% correct; GPT-4 no neglect in this task | b26, b25 |
| Textbook Bayes problems | far above human ceilings (inferred from online participants using LLMs: 57% perfect vs about 24%) | b28, d12 |
| Sequential preference updating | plateau after round 1; Gemma about 37% | c07 |
| BN question answering from text | CoT collapses: 79% (2 vars) to 6-7% (8-10 vars) | d01 |
| LR from a given BN | mostly right, silent failures: 390.4 vs 18.07; 4 of 100 wrong at 1.21 vs 0.66 | c01-c03 |
| Forecasting with Bayesian prompt | worse (Brier +0.03) | c15 |
| Belief revision | entrenched; Martingale positive in 51 of 54 CoT setups | c18 |
| Evidence order on legal vignette | GPT-4o 0.66 vs 0.40; GPT-5.2 4.75 vs 5.35 | d07, d09 |
| Conservatism | stated posterior moves the right way but too little vs Bayes on its own LRs | d08 |
| Joint probabilities | GPT-5 conjunction fallacy 18.8% (humans 58.5%) | d11 |
| Verbal probability words | inconsistent, often refused | d15 |

**What changed the behaviour, and by how much.**
- *Wording that forces computation.* One word ("compute", "posterior probability") reversed the representativeness bias in GPT-4o; softer instructions did nothing [a21]. No effect size reported; one model.
- *Offloading to a solver.* GPT-4 on 10-variable networks: CoT 7% to ProbLog 96% [d01, d02]. Plain generated Python: 10%. Monte Carlo: 88%.
- *Hybrid explanation.* Exact LRs supplied: errors dropped to zero across 100 runs per network [c04].
- *Fine-tuning on a Bayesian assistant.* About 80% agreement vs a poor baseline; needs training [c09]. Out of scope.
- *Examples in the prompt.* One-shot raised probability tasks by +70% and percentile tasks by +59% (Gemini 1.0 Ultra, GPT-4 Turbo, GPT-3.5) [c13].
- *Bayesian-reasoning prompt:* worse (+0.03 Brier) [c15]. Base-rate-first: slightly better (-0.011 to -0.016) [c16]. Gains not robust across models.
- *Generic warnings:* 6.9% mean bias reduction, correct bias named 5% [b25]. Legal-expert or meticulous prompts: limited [d10].
- *Prompting for natural frequencies:* partial and inconsistent in three reasoning models (qualitative) [d03].
- *Response mode.* Step-by-step judgment raised guilty-verdict odds 10.55-fold in GPT-4o; role framing mattered [d07].
- *Newer models.* Weaker order effects (GPT-5.2), far fewer conjunction errors (GPT-5), no base-rate neglect on easy vignettes (o1). Not eliminated.

**What we do not know about LLMs on this topic.**
- How often they commit the prosecutor's fallacy on realistic forensic prose (nothing measured) [d19].
- Whether the Hoffrage DNA result replicates with LLMs [d19].
- Claude-thinking and o3-class behaviour on legal order effects, conservatism and entrenchment.
- BLInD for 2025-2026 reasoning models.
- How well LLMs elicit structure, priors and independence from messy case text (BLInD states all numbers outright) [d02].
- The only evidence-law benchmark item (LegalBench hearsay) is rule application, not probability [c26].

## 7. What our agent should take

Schema mapping note. The claims file labels the convert-to-counts step "O2". In SCHEMA.md v0.2, O2 is "Generalise" and the matching operator is **O6 Change representation**. This document uses O6. A "hypothesis-pair check" overlaps with section 4b, which bans a full competing-hypotheses matrix (ACH) because it showed no gain. The check proposed here is two named hypotheses and one exclusivity test, not a matrix. It is a Test-first item, not an Add-now item.

### Add now (established)

1. **Compute posteriors, LRs and chained updates in code, not in the model's head.** Schema part: G5 (code selects, normalises) and S4 (test by running). Status **[E]**. Evidence: d01, d02, c04, c11, c01-c03. Rule: when a task contains probabilities, the model extracts numbers and hypotheses into a slot; code does the arithmetic and returns the result; the model explains. Rationale: CoT collapses with size (79% to 6%), solver offload holds (96-100%), an unconstrained LR fails silently and then gets rationalised (390.4 vs 18.07). Caveat: this tests translation of explicit text, not elicitation of structure.
2. **Do not trust a model's explanation of why a probability is right.** Schema part: G10, G2. Status **[E]**. Evidence: c02 (post hoc rationalisation), b25 (bias named correctly 5%). A checker must recompute, not re-read.
3. **No "reason like a Bayesian" prompt.** Schema part: section 4b (extends "debiasing instructions did not reliably reduce error"). Status **[E]** with new support: c15 (+0.03 Brier worse), b25, d10, a21 (soft instructions inert).
4. **Treat input wording as a source of error for base-rate items.** Schema part: S1 input hygiene. Status **[E]**. Evidence: a19, d04, a20, c23. A vivid description pushes LLM posteriors from odds ratio 9 to about 1.2-2.6. Code should move vivid but non-diagnostic description into a marked block and keep the numeric base rate in the slot used for computation.
5. **Order-invariance for evidence sequences.** Schema part: G4 (samples from one model are not independent) and S7 (select by behaviour on fresh inputs). Status **[E]** (two models, two papers). Evidence: d07, d09. Rule: when a task presents evidence in sequence, present it in at least two orders in fresh contexts; accumulate log-odds in code; if the conclusions differ, do not submit the model's stated posterior; report the code-accumulated one with an order-sensitivity flag.
6. **Ask for both conditionals explicitly.** Schema part: S1. Status **[E]** for the logic (a11, a12, b07, c28) and the arithmetic. Whether the restatement helps LLMs is untested, so only the script check "did the final answer use a prior?" is added now.
7. **Do not quote a single human success rate.** Memory and notes rule. The spread is 24-68% by sample. Status **[E]**.

### Test first

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Convert-to-counts operator (absolute counts out of N, code checker that counts sum to N and match M1), forced by the program | O6, S2 | **[S]** humans E, LLM untested | a01, a03, b01, b19, d03, K29 |
| T2 | Hypothesis-pair and exclusivity check (list H1, H2; "can both be false/true?"); dependence flag per evidence item | S2, G5 (see 4b ACH) | **[C]** | a12, a13, b05, K08, K26 |
| T3 | Two-elicitation consistency (prior alone vs implied prior) | G4, S1 | **[S]** | a20 |
| T4 | Martingale monitor on belief updates | G1, G10 | **[S]** | c18-c20 |
| T5 | Verbal-to-numeric calibration per model | G4 | **[S]** | d15 |
| T6 | Few-shot worked examples vs none for transfer to new base-rate problems | memory | **[S]** (humans for training; c13 for LLMs) | b19-b21, c13 |
| T7 | Base-rate-first ordering of the prompt | S1 | **[S]** | c16 |
| T8 | Automatic structure elicitation (hypotheses, priors, independence) from messy prose, then solver | S2, G5 | **[S]** | d02, c25, c24 |
| T9 | Check on weak inculpatory evidence: belief must not move the wrong way | G4 | **[S]** humans only | b11, b14 |
| T10 | Flagging a flawed forensic report (unsound method, transposed conditional) | G7, S8 | **[S]** humans only | b17 |

Each is expanded in section 8 and in UNKNOWNS.md.

## 8. Concrete tests on our bench

All arms get equal tokens. The plain arm spends its tokens on free reasoning; the scaffold arm spends them on the steps. Setup cost is counted (G7). Use at least 3 repeats per item and report the spread. Items must be perturbed versions (names, numbers, framing swapped) so that textbook memorisation does not hide the effect [b28, c23].

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Convert-to-counts | 60 base-rate items: 20 mammography-style, 20 DNA-match-style (prior, RMP, sensitivity, false-positive), 20 vivid-description items (Li and Rui style); numbers perturbed | (a) plain CoT; (b) CoT + forced counts step with checker; (c) tool-computed posterior | exact posterior within 1 percentage point | (c) near 100% on explicit text; (b) above (a) mainly on vivid-description items; (b) not above (c). If (b) is not above (a) by 5 points, drop O6 for explicit numbers. Frontier models may already be near ceiling on bland items [b26, d12]. |
| B2 Prosecutor's fallacy detection and commission | 30 forensic summaries in realistic prose: 10 with a seeded transposed conditional, 10 with a seeded defence-attorney fallacy, 10 clean; plus the task "state what the evidence shows about guilt" | (a) plain; (b) both-conditionals restatement; (c) ledger with P(e|H1), P(e|H2) columns | detection rate of seeded fallacies; commission rate (model's own output transposes); false-alarm rate on clean items | Fills gap 2 (nothing measured). Expect commission to fall with (c) because a one-column ledger is visibly incomplete. Baseline unknown. |
| B3 Hoffrage DNA replication | the two Hoffrage DNA cases (RMP 1 in 1,000,000, false-positive 0.003) in probability and natural-frequency format, with perturbations | plain, with and without hint | correct source inference; correct verdict | Human reference: 13% vs 68% (professionals), under 1% vs 44% (students) [a07]. LLMs probably near ceiling in both [d12]; the informative cell is the perturbed, longer-prose version. |
| B4 Dependent evidence (Sally Clark type) | 20 items: two or three evidence items that share a cause, with and without stated dependence; marginal rates supplied | (a) plain; (b) generic "be careful" warning; (c) hypothesis listing + dependence flag column | answer multiplies marginals when dependence applies (error); alternative hypothesis named | Tests gap 8 and K26. Expect (c) > (b) about equal to (a). Generic warning effect near 0 [d10, b25]. |
| B5 Order invariance | 40 sequences of 6-8 evidence items with known LRs, shown in two orders | (a) plain single pass; (b) two-order check with code log-odds; (c) code only | gap between final stated probability and Bayes; flip rate between orders | GPT-4o class: large order effect [d07]. (b) cuts flip rate to near 0 by construction; the question is accuracy against Bayes. |
| B6 Conservatism | same sequences, items with moderate LRs | model states per-item LR and posterior; compare with product of its own LRs and with ground truth | ratio of stated to Bayes log-odds | Expect ratio below 1 [d08]. If true, elicit LRs only and multiply in code. |
| B7 Solver offload at growing size | BN texts with 2-10 variables, 2025-2026 reasoning models | (a) CoT; (b) PAL code; (c) ProbLog translation | exact within tolerance, by size | Reproduces d01 and d02 on newer models; closes gap 4. Expect CoT better than 2024 but still falling with size. |
| B8 Structure elicitation | 20 case narratives in messy prose with a hand-built ground-truth BN | LLM proposes hypotheses, priors, dependence; solver runs | structure error rate; final posterior error | Gap 5. Expect much worse than BLInD's 96-100%. |
| B9 Martingale and consistency | 200 mixed items | compute Martingale slope and prior-alone vs implied-prior gap | slope, mean gap | Entrenchment predicted [c18]; diagnostic use. |
| B10 Weak evidence | 20 items of weak inculpatory evidence, verbal and numeric | plain | share where stated belief in guilt falls | Human effect mostly verbal [b14]; LLM unknown. |
| B11 Verbal scale | 20 verbal terms x 10 contexts | each model | median number, spread, abstain rate | [d15] predicts instability and abstention. |
| B12 Flawed report | 20 reports, sound vs unsound, incl. seeded transposed conditional | plain vs ledger | detection rate of unsound reports | Humans 32% [b17]; LLM unknown. |

Scoring is by code wherever possible. A model judge, if needed, sees no authorship or proposed answer (G5).

## 9. What does not transfer, and why

- **Natural-frequency training of humans.** The gain is partly a representation effect (transfers as a step) and partly learning (does not: we cannot train the model). Fine-tuning on Bayesian-assistant guesses (80% agreement) needs training [c09, K19].
- **The evolutionary argument** for natural sampling. It explains human minds; it says nothing about token predictors [a01].
- **Mock-juror findings about presenting LRs to laypeople** (format null, weak evidence effect). They concern human readers of a report. They matter only if our agent writes for lay readers [b15, b11]. LLM readers may be more format-sensitive (untested).
- **The legal-doctrine debate** (presumption of innocence, jury function) [a27, b30]. Not an agent decision.
- **Human conservatism numbers from the 1960s.** Different tasks, humans. LLM conservatism is measured separately [d08].
- **Debiasing by forewarning.** Weak even for GPT-4 [b25] and already in 4b.
- **BLInD offloading success as proof of structure elicitation.** BLInD gives all numbers and links; real cases do not [d02].
- **Preference-learning updating (flights)** [c07]. Small hypothesis space, latent user, simulated users. Not evidence weighing.
- **Election-probability coherence** (GPT-5, 18.8%) [d11]. Coherence on explicit numbers does not show good evidence weighing.
- **LegalBench hearsay** [c26]. Rule application, not probability.
- **Textbook networks** (Asia, Cancer, Insurance) used in structure discovery [c25] may be in training data; case graphs are contested.
- **Court-facing advice to experts** (report LRs, not posteriors [c28]). Relevant only to how the agent phrases output.

## 10. Open questions

1. Does a convert-to-counts operator improve a frontier LLM on perturbed base-rate and DNA-match problems at equal tokens, compared with plain CoT and a tool-computed posterior? (No controlled test found.)
2. How often do current LLMs commit the prosecutor's fallacy when summarising forensic evidence in realistic prose?
3. Does the Hoffrage DNA result (13% vs 68%) replicate with LLMs, and with legal professionals in 2020-2026?
4. Does the BLInD collapse with network size persist for 2025-2026 reasoning models?
5. Can structure (hypotheses, priors, independence) be elicited from messy case text, and how often is it wrong (Fenton's exclusivity and independence issues)?
6. Do reasoning models (o1/o3, Claude thinking) show conservatism, entrenchment, the weak-evidence effect and order effects on legal sequences?
7. What did Thompson and Schumann (1987) and Koehler (1996) find in numbers, and do they replicate?
8. Does explicit hypothesis listing beat generic warnings on dependent evidence?
9. How well do LLM-stated LRs and verbal strengths calibrate against ground truth across many networks?
10. Is the human null on forensic conclusion format (Martire 2025) also null for LLM readers?
11. Are the GPT-4o order effects driven by recency in token position, or by the story change when order is reversed [d09]?
12. Is LLM conservatism an artefact of eliciting self-reported LRs that are themselves incoherent [d08]?
13. Why does one prompt word reverse the representativeness bias in GPT-4o [a21]? RLHF, or only instruction following?

## 11. Sources

[V] opened this session (full text or substantial page text). [M] snippet, abstract only, press release or second-hand.

**Human studies and reviews**
- [V] Gigerenzer and Hoffrage (1995) How to improve Bayesian reasoning without instruction. https://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf (a01-a06; a29 content second-hand)
- [V] Hoffrage, Lindsey, Hertwig and Gigerenzer (2000) Communicating statistical information. https://library.mpib-berlin.mpg.de/ft/uh/UH_Communicating_2000.pdf (a07-a09; OCR garbled in places)
- [V] Gigerenzer and Edwards (2003) Simple tools for understanding risks. https://library.mpib-berlin.mpg.de/ft/gg/GG_Simple_2003.pdf (a30)
- [V] Fenton, Neil and Berger (2016) Bayes and the Law. https://pmc.ncbi.nlm.nih.gov/articles/PMC4934658/ (a10-a15; b29 was earlier marked unread)
- [V] Smit, Lagnado, Morgan and Fenton (2016) Using Bayesian networks to guide the assessment of new evidence. https://pmc.ncbi.nlm.nih.gov/articles/PMC4930139/ (a25)
- [V] Weber, Binder and Krauss (2018) Why can only 24% solve Bayesian reasoning problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC6194348/ (b01-b03; the 4% and 24% figures are McDowell and Jacobs 2017, read second-hand)
- [V] Shengelia and Lagnado (2021) Are jurors intuitive statisticians? https://pmc.ncbi.nlm.nih.gov/articles/PMC7892609/ (b04-b06)
- [V] Juror comprehension of forensic expert testimony: a literature review and gap analysis (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC7219164/ (b10-b13)
- [M] Martire, Kemp, Watkins, Sayle and Newell (2013) The expression and interpretation of uncertain forensic science evidence. https://pubmed.ncbi.nlm.nih.gov/23750600/ (b14)
- [V] Martire et al. (2025) Mock juror evaluations of forensic conclusion formats within a complete expert report. https://pmc.ncbi.nlm.nih.gov/articles/PMC12206337/ (a26, b15, b16)
- [V] Sidebotham (2025) Flipping the conditional. https://pmc.ncbi.nlm.nih.gov/articles/PMC12233044/ (b07)
- [V] Feeny and Stamboulid (2026) Sally Clark: trial and error by judge and jury. https://pmc.ncbi.nlm.nih.gov/articles/PMC13330532/ (b08, b09)
- [V] de Roo, Stevens and de Poot (2026) Institutional authority on forensic report evaluation. https://pmc.ncbi.nlm.nih.gov/articles/PMC12766657/ (b17)
- [V] Hefter, Hinkel and Hinkel (2026) Clinical expertise and cognitive reflection. https://pmc.ncbi.nlm.nih.gov/articles/PMC13744101/ (b18)
- [M] Feufel, Keller, Kendel and Spies (2023) Boosting for insight and/or agency. https://pmc.ncbi.nlm.nih.gov/articles/PMC9903474/ (b19)
- [M] Kim et al. (2024) Natural frequency tree vs formula training. https://pmc.ncbi.nlm.nih.gov/articles/PMC11515371/ (b20)
- [V] Repeated exposure rivals lightweight training in Bayesian inference (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13550133/ (b21)
- [M] Fenwick, Campitelli and Thompson (2026) Explaining success in Bayesian reasoning. https://pmc.ncbi.nlm.nih.gov/articles/PMC13481750/ (b22)
- [V] Algorithms on trial (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12221571/ (a27, b30; abstract and introduction)
- [V] First impressions matter: obstacles to probabilistic fingerprint reporting (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12460907/ (b31; abstract and introduction)
- [V] Sally Clark, Wikipedia (secondary). https://en.wikipedia.org/w/index.php?title=Sally_Clark&action=raw (a28)
- [M] Thompson and Schumann (1987) Interpretation of statistical evidence in criminal trials. https://doi.org/10.1007/BF01044641 (a16, d06; bibliographic record only)
- [M] Tversky and Kahneman (1982), Bar-Hillel (1980), the cab problem, via Gigerenzer and Hoffrage. https://library.mpib-berlin.mpg.de/ft/gg/GG_How_1995.pdf (a17)
- [V] Koehler (1996) The base rate fallacy reconsidered, abstract. https://doi.org/10.1017/S0140525X00041157 (d05; a18 second-hand)
- [V] Cuellar (2025) The Prosecutor's Fallacy and Expert Testimony. https://arxiv.org/abs/2502.03217 (c28, d17; abstract and introduction)
- [V] Analytic misjudgment of drug safety evidence (2026). https://doi.org/10.1007/s40264-026-01683-5 (d18; abstract)
- [M] An LLM canary in the online data coalmine (2026). https://doi.org/10.3758/s13428-026-03184-w and https://pubmed.ncbi.nlm.nih.gov/42786397/ (b28, d12; abstract only)
- [M] Pompedda, Santtila et al. (2025) Evaluating firearm examiner testimony using LLMs. https://doi.org/10.1080/29974100.2025.2503343 (d13; press releases only)
- [M] HelixCross (2026) AI-powered cross-examination simulator. https://doi.org/10.1016/j.fsisyn.2026.100725 (d14; abstract)
- [M] LLMs as jurors (2025), Law and Human Behavior. https://doi.org/10.1037/lhb0000620 (d16; database summary)

**LLM studies**
- [V] Li and Rui (2024) Dual traits in probabilistic reasoning of LLMs. https://arxiv.org/pdf/2412.11009 (a19-a21, d04)
- [V] Araya (2025) Do chains-of-thought of LLMs suffer from hallucinations, cognitive biases, or phobias in Bayesian reasoning? https://arxiv.org/pdf/2503.15268 (a22, c21, c22, d03)
- [V] Qiu et al. (2025) Bayesian teaching enables probabilistic reasoning in LLMs. https://arxiv.org/abs/2503.17523 (a23, b23, c07-c09)
- [V] Scholten, Rebholz and Huetter (2024-25) Metacognitive myopia in LLMs. https://arxiv.org/pdf/2408.05568 (a24; theory)
- [V] Nafar, Venable and Kordjamshidi (2024) Reasoning over uncertain text by generative LLMs (BLInD). https://arxiv.org/abs/2402.09614 (b24, c10-c12, d01, d02)
- [V] Wang and Redelmeier (2025) Forewarning AI about cognitive biases. https://pmc.ncbi.nlm.nih.gov/articles/PMC12413502/ (b25)
- [V] Evaluating the o1 reasoning LLM for cognitive bias (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12372181/ (b26)
- [V] Hagendorff, Fabi and Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206 (b27)
- [V] Keppens (2026) Hybrid explanation of Bayesian network derived likelihood ratios. https://ceur-ws.org/Vol-4253/paper5.pdf (c01-c06)
- [V] Paruchuri et al. (2024) What are the odds? https://arxiv.org/abs/2406.12830 (c13, c14)
- [V] Schoenegger, Jones, Tetlock and Mellers (2025) Prompt engineering LLMs for forecasting. https://arxiv.org/abs/2506.01578 (c15-c17)
- [V] He, Qiu, Sap and Shirado (2025) Martingale Score. https://arxiv.org/abs/2512.02914 (c18-c20)
- [V] Jiang et al. (2024) A peek into token bias. https://arxiv.org/abs/2406.11050 (c23)
- [V] Wong et al. (2023) From word models to world models. https://arxiv.org/abs/2306.12672 (c24)
- [V] Zhang, Zhang, Kordjamshidi and Cui (2026) Bayesian network structure discovery using LLMs. https://arxiv.org/abs/2511.00574 (c25)
- [V] Guha et al. (2023) LegalBench. https://arxiv.org/abs/2308.11462 (c26)
- [V] Leonelli (2026) Beyond post-hoc explanation: glassbox AI via probabilistic models. https://arxiv.org/abs/2606.07113 (c27; position paper)
- [V] Qiao, Cheung, Hampson and Lagnado (2026) Biased Judge: recency and order effects. https://doi.org/10.31234/osf.io/gcd6k_v1 (d07, d08; preprint)
- [V] Bessis, Wills, Wojciechowski, White and Pothos (2026) Legal decision biases in GPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC13024114/ (d09, d10)
- [V] Divergent patterns of probabilistic reasoning in humans and GPT-5 (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12992218/ (d11)
- [V] Jackson, Andreadis and Ancker (2025) LLMs and communication of medical probability words. https://pmc.ncbi.nlm.nih.gov/articles/PMC12712724/ (d15)
- Search log for gaps: https://www.ebi.ac.uk/europepmc/ (d19)

Not re-opened during the critique: Gigerenzer and Hoffrage 16/28/46/50 (matched memory and the first-agent PDF read), Li and Rui, Schoenegger et al., o1 vignette study, Wang and Redelmeier, Shengelia and Lagnado, Martire 2025.
