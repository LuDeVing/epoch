# Computational coherence models: deep document

*Subfield E11.04. Evidence ids (a01..d17) and claim ids (K01..K28) refer to evidence_a-d.jsonl and claims.jsonl in this folder. Marks: [V] source opened, [M] snippet, abstract or memory only. Status: [E] established, [S] single-source, [C] contested.*

## 1. What it is

A coherence model treats a decision as a network of claims. Some claims support each other. Some contradict each other. The model finds the set of claims to accept so that the most support is kept and the least conflict remains. The accepted set is the verdict, or the belief.

Three families matter here.

1. **Explanatory coherence (Thagard).** ECHO is a neural-style network. Each proposition is a unit. Explanation gives a symmetric excitatory link. Contradiction gives a symmetric inhibitory link. Activation settles. Units that end positive are accepted. (a01, a02)
2. **Constraint-satisfaction coherence.** The same idea stated as a combinatorial problem: split elements into accepted and rejected sets to maximise satisfied constraint weight. It is NP-hard but approximable, and it can be solved in code with MaxSAT, greedy flips or semidefinite programming. (a10, a11)
3. **Coherence as a human process.** People who read a legal case drift their ratings of the evidence toward the verdict they lean to. The shift is a "coherence shift". Network models predict it. (d01, d04, d05, d06)

A fourth family is new and is the one our agent can use. Since 2021, engineers have put a MaxSAT or factor-graph solver over a language model's own claims. BeliefBank, Maieutic prompting, ConCoRD, REFLEX and VERGE all do this. (b01, b03, b05, d10, d12)

Why it matters for the agent. The schema says "code selects" (G5). A coherence solver is one concrete way for code to select among claims or hypotheses. It is also a warning. Humans (and, in some studies, LLMs) distort evidence to fit the leaning answer. A scaffold must not let the model re-rate evidence after it has picked a side.

What this document finds. The solver part is real but proven only on 2021-22 small models and on formal-logic tasks. The human coherence-shift part is well replicated. The claim that ECHO "reaches human-like verdicts" on law is retrodiction by the author, not validation. No study tests an ECHO-style solver on an LLM-built legal evidence graph (K22, d17).

## 2. History and theories in depth

**1989, Thagard, "Explanatory coherence" (Behavioral and Brain Sciences 12(3)). [V a01-a09, d14, d15]**
- Seven principles: symmetry, explanation, analogy, data priority, contradiction, acceptability (competition), system coherence. Principle 2(c): the more propositions needed to explain something, the lower the coherence. This is a built-in simplicity penalty. (a01, c01)
- ECHO turns the principles into a network. A special evidence unit is clamped at activation 1 and feeds the data units (data priority). Default runs: excitation .05, inhibition -.2, data excitation .1, decay .05, activation range -1 to 1. Most networks settle in under 100 cycles. Copernicus v Ptolemy (over 150 units) took about 210. Lavoisier 107 cycles, Darwin 49. (a02, a03)
- Applications: Lavoisier, Darwin, Copernicus, and two legal cases. Chambers (the 1988 "preppy murder" case, input from press reports): ECHO clearly accepted guilt, but the real case ended in a plea, so there is no verdict to compare. Peyer (Cara Knott murder): the real jury hung 7 to 5, and ECHO found more coherence in guilt but did not strongly reject innocence. Thagard reads this as a match. It is a post-hoc reading of a mixed result. (a04, a05)
- Self-admitted limit: every proposition and link is typed in by the programmer. "More than a dozen" cases were analysed, "virtually no adjustment" in four main examples. Intercoder reliability was never tested. (a06)
- Peer commentary: Achinstein said the theory is empty if "explain" is undefined. Another commentator said "explains" could be replaced by "connected to" with no change. Chi said belief change hides the hard step of why people drop a hypothesis. (a08, a09)
- Author's reply (d14): he conceded to Klayman and Hogarth that ECHO analyses are not good tests of psychological validity and need controlled experiments. He answered Dawes's Simpson-paradox challenge by adding an alternative hypothesis to the toy network. He accepted probabilities where they exist and called himself a weak explanationist.
- The only human-data check in the paper is Ranney and Thagard (1988): two protocol cases of students learning naive physics. Thagard is co-author, so it is not independent. The report was blocked (403) and not read. (a07, d15)

**1992.** Thagard applied ECHO to an opponent's plans. The USS Vincennes network settled in 60 cycles. The F-14 attack hypothesis explained seven pieces of evidence, the airliner hypothesis two. ECHO rejected the airliner hypothesis, as the crew did. Another retrodiction from the official report. (a17)

**1998, Thagard and Verbeurgt, "Coherence as constraint satisfaction" (Cognitive Science). [V a10, a11]**
- Recasts coherence as partitioning elements into accepted (A) and rejected (R). A positive constraint is satisfied if both elements are in the same set. A negative constraint is satisfied if they are in different sets. Maximise total weight of satisfied constraints.
- Proof of NP-hardness by reduction (from MAX-CUT). Semidefinite programming (Goemans-Williamson) guarantees expected weight at least 0.878 of optimal (0.87856). The older incremental method guarantees 0.5. The connectionist method has no guarantee.
- The greedy flip method gave the same accepted set as ECHO on the authors' examples, except ties. Asynchronous Hopfield updates with symmetric weights converge to a local optimum. Synchronous ECHO updates have no general guarantee.

**1999-2004, the human side (Holyoak and Simon; Simon and colleagues).** See section 3. These are the real experiments. A constraint network predicts that ratings of evidence move toward the verdict, and they do. [V d01-d05]

**2003-2006, Thagard on legal inference.**
- 2003, "Why wasn't O.J. convicted?" Pure ECHO accepted that Simpson was the killer, and also that the LAPD tried to frame him. The jury acquitted. A JavaBayes network also said guilty: P(killed) .72, P(LAPD framed) .99, from about 60 hand-set conditional probabilities. Thagard added emotional coherence (HOTCO 2). A default valence link of .05 flipped the result to reject guilt. He also tried a presumption-of-innocence rule: guilt rejected if inhibition exceeds a threshold (.065 in the opened text). Valence values were tuned after the verdict. One case. (a14)
- 2004, von Bulow. ECHO accepts "Claus injected Sunny with insulin" for trial 1 (convicted) and rejects it for trial 2 (acquitted). Trial 1 took 188 cycles; greedy needed about 16 flips. Parameters differ from 1989 (excitation .04, inhibition -.06), so there are no stable "defaults". A Bayes network on trial 1 used guessed probabilities (.7 for witness-says-X-given-X, rest at .5). It agreed with ECHO. Thagard argued the comparison shows ECHO needs fewer numbers. It shows effort, not accuracy. No Bayes run for trial 2. (a12, a13)
- 2005, testimony: a two-path account. Default is automatic acceptance of a credible, consistent claim. Reflective path is explanatory coherence. No participant data. (a15)
- 2006 review and 2007 "Coherence, truth": coherence does not guarantee truth. Phlogiston was highly coherent. Only coherence that broadens (explains new facts) and deepens (explains why) tends toward truth. Self-review by the author. (a16, a18, c03)

**Rivals.**
- Bayesian and probabilistic coherence (Bovens and Hartmann; Olsson). They argue coherence is not truth-conducive in general. Not opened. [M b20]
- Predecisional distortion (Russo, Medvec and Meloy, 1996): people rate new information as favouring the current leader. A rival account of the same shift. [M b18]
- Araszkiewicz (2013) critiques the constraint-satisfaction theory as a theory of legal reasoning. Record only, content unread. [M b19]
- Parallel constraint satisfaction (PCS) as a general model of intuitive judgment (Glockner). Proponent-authored. (a21-a24)

**2020-2026, language models.** The idea returns as engineering: BeliefBank (2021), Maieutic prompting and Entailer (2022), ConCoRD (2022), REFLEX (2023), Logic-LM (2023), IBE-Eval (2024), VERGE (2026). Separately, psychologists ask whether LLMs show coherence shift (Lehr and Cummins 2025). See section 6.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Coherence shift in a legal case: ratings of six points of dispute move toward the final verdict | Holyoak and Simon 1999 Exp 1: N=54 (48 analysed), verdict x test F(1,44)=35.3, p<.001. Q-score pretest .37 (Quest) v -.20 (Smith), p=.06. Posttest 1.42 v -1.56, p<.001. No effect size reported. | d01 [V] | [E] |
| Shift survives a 1-week gap between pretest and case | Exp 2: N=19, pretest Q -.34 v -.30, posttest .94 v -1.03, F(1,17)=7.71, p=.01. Recalled pretest pulled toward verdict only marginally, r(16)=.43, p=.07. | d02 [V] | [S] (small N) |
| Character information spreads coherence to loosely linked points and a second case | Exp 3 N=80. Quest Q .93 (Bad Smith) v -.71 (Good Smith). Spread to second case F(1,78)=36.4. Two of four linked points significant. | d03 [V] | [S] |
| Shift appears at an interim test before the verdict, with or without stating a leaning | Simon et al 2001 Exp 1: N=50 (47 analysed). Verdict x test F(2,86)=35.3. Baseline gap .80 (p=.01), interim 2.23, post 2.55. Interim-to-post not significant (p>.30). | d04 [V] | [E] |
| Shift occurs with no decision task (memorise, comprehend) | Exp 2 N=125, F(2,236)=59.1. Exp 3 N=166, F(2,302)=78.6. Verdict groups defined by a later verdict. | d05 [V] | [S] |
| Independent online replication on agreement ratings | Qiao et al 2026 Study 1: N=130, Verdict x Test x Side F(1,128)=96.31, p<.001. Posttest prosecution agreement .80 v .53; defence .72 v .42. Pretest no difference. | d06 [V] | [S] (Holyoak co-author) |
| Shift is not reliable when strength is a likelihood ratio | Studies 2a (N=126) and 2b (N=83): three-way interaction p=.083 and p=.44. | d06 [V] | [S] |
| A constraint network fits group-mean shifts | 48 predicted values, r=.87, .79, .86; RMSE .080-.093. Bidirectional likelihood-agreement links fit worse. Fit to means, free parameters. | d07 [V] | [S] |
| Same effect in choice, not just law | Lee and Holyoak 2020, N=58 snack choice, beta -0.247, p<.001; also with a similarity task. | c10, c11 [V] | [S] |
| People mostly search for disconfirming evidence yet still shift | Four studies, three legal cases each. Sample sizes not read. | a22 [M] | [S] |
| PCS fits intuitive and deliberate inference best | Forst and Glockner 2026 N=128: 50-60% PCS, under 30% weighted additive, under 15% heuristics. Decision time 9241 v 5583 ms, d=0.85. Glockner and Jekel N=249, 250 inference tasks each. | a23, a24 [V] | [E] (proponent-authored) |
| Mock-juror emotion shapes evidence evaluation | N=713, 677, 651. Moral emotion predicts agreement with unrelated evidence, then votes and damages. A judicial instruction failed. | a26 [V] | [S] |
| ECHO accepts the known outcome on retrodicted cases | Chambers (plea), Peyer (hung 7-5, weak margin), von Bulow 1 and 2, Vincennes. Input author-coded, outcomes known. | a04, a05, a12, a17 [V] | [S] |
| Pure ECHO and a Bayes net both fail on Simpson | ECHO: guilty and framed. JavaBayes P(killed)=.72. Fix needed post-hoc valence .05 or presumption parameter. | a14 [V] | [S] |
| Coherence maximisation is NP-hard, approximable | SDP >= 0.878 of optimal; greedy flips match ECHO on authors' examples. | a10, a11 [V] | [E] |
| Solver over an LLM's beliefs raises consistency (BeliefBank) | Raw F1 about 69%. Constraints only 85.8. Relevant feedback + constraints 86.6. Relevant feedback only 79.5. Consistency about 95%. Solver alone about +16.5 F1. | b01, b02, c21 [V] | [E] (2021 model) |
| ConCoRD (NLI-detected links + MaxSAT) | BeliefBank F1 .831 to .914 (Macaw-Large), .855 to .931 (3B). ConVQA LXMERT .656 to .706; ViLT .784 to .804. NQ F1 +1.4 to +1.9 points. | b05, c22 [V] | [E] (small models) |
| Link source: estimated beat gold on BeliefBank, gold beat estimated on ConVQA and NQ | BeliefBank .914 (ConCoRD) v .862 (gold solver); 3B .931 v .905. ConVQA oracle .824 v .706. NQ T5-3B oracle .423 v .351. | b05, b22, c22 [V] | [C] |
| Entail + contradict links together beat either alone | BeliefBank F1 .914 both, .892 contradiction only, .827 entailment only. | b06 [V] | [S] |
| Maieutic prompting: explanation tree + NLI + MaxSAT | Com2Sense dev 72.5 v 58.1 standard, 61.6 CoT, 61.4 SC. CSQA 2.0 69.5 v 54.1/59.6/60.8. CREAK 85.2 v 60.3/64.8/70.5. Removing NLI -7; removing abduction -4. | b03, b04, c19, c20 [V] | [E] (GPT-3 era) |
| REFLEX rational layer: consistency up, accuracy flat | Consistency +8 to +11 (87.0 to 96.1; 88.2 to 95.9; 85.7 to 96.6). Accuracy 79.4 to 79.9, 74.0 to 75.0, 80.2 to 80.0. | d12 [V] | [E] |
| Solver can flip a true belief to a false one | Rat/cat example. No rate reported. | b24, d12 [V] | [E] (as a risk; rate unknown) |
| Entailer: own-belief chains, same accuracy, more faithful | OBQA 75.2 v 75.2; QuaRTz 75.4 v 74.1. Proofs clearly valid over 70% v 34%. Belief errors 33% of failures. 80 to 360 s per question. | b07, b25 [V] | [S] |
| IBE-Eval: features from coherence theory pick the right explanation | Up to 77% (+27 over random, +17 over GPT-3.5 judge). Spearman with humans 0.64 v 0.31 (n.s.). Hedging strongest. Logical consistency equal for right and wrong options. | a27, b08, b09, b26 [V] | [S] |
| Argument-graph solver (ArgLLM) matches CoT, no better | Accuracy comparable to CoT; gain is contestability. | b10 [V] | [S] |
| Logic-LM: solver over formalisation | GPT-4 FOLIO 69.11/70.58/78.92 (standard/CoT/Logic-LM); ProofWriter 52.67/68.11/79.66; AR-LSAT 33.33/35.06/43.04; ProntoQA 77.40/98.79/83.20 (CoT wins). | c24 [V] | [E] |
| VERGE (SMT, repair) Sonnet 3.7 | FOLIO CoT 70.4, SC 72.4, Logic-LM 71.6, VERGE 87.9. ProofWriter CoT 71.6, SC 86.6, PoT 98.2, VERGE 93.0. | d10 [V] | [S] (preprint) |
| Formalisation is the bottleneck | Unanimous formalisations faithful 76.7% v 56.0% (p=.002). 23.3% of unanimous still disagree with gold. Gold agrees with labels only 72.6%. 20B model about 30% valid SMT. | d11 [V] | [S] |
| LLM graph reconstruction from propositions | 76 synthetic graphs, 5-23 nodes. o1/3/4-mini perfect on about half of sparse graphs. One build per graph. | d08, d09 [V] | [S] |
| Deductive closure training | +3% to 26% supervised, +12% unsupervised on CREAK; incoherent rate 34.4 to 12. | c23 [V] | [S] (training, not usable) |
| GPT-4o coherence shift after writing an essay | Study 1 n=150: pro v control d=2.164, anti v control 1.795, pro v anti 3.775. Study 2 n=900: choice v no choice d=0.981 (pro), 0.252 (anti), P=.0298. | a28, c12, c13 [V] | [C] |
| Same shift with a user-written essay | Valence effect in all three Cummins studies. Ns not stated. | c14, d16 [V] | [C] |
| Adversarial roles omit unfavourable facts | 200 Swiss cases, o1 and Llama 3.3 70B. Role effect p<0.001. Human check: under 20% of prosecutor-view summaries favoured defence v 100% of defence-view; kappa 0.47. Balancing instructions did not remove it. | c15-c17 [V] | [S] |
| Coherence is not truth | Phlogiston; LLMs write consistent explanations for right and wrong options equally. | c03, b09 [V] | [E] |

## 4. Mechanisms and models

### 4.1 ECHO as an algorithm (implementable)

Inputs: a list of propositions P; a list of data (evidence) propositions D, a subset of P; explain links (hypothesis set H explains e); contradiction links (pairs that cannot both hold); optional analogy links.

Link weights by the principles:
- Symmetry: every link is two-way.
- Explanation: if hypotheses H1..Hn jointly explain e, add excitatory links between each Hi and e, and among the Hi. Weight scaled by 1/n (simplicity, principle 2c). So explaining with many hypotheses gives weak links.
- Contradiction: inhibitory link, weight set to the inhibition parameter.
- Data priority: a special unit with activation fixed at 1 is linked to each datum with the data-excitation weight.
- Acceptability: a hypothesis with more evidence support gets more weight. This falls out of the network.

Update rule per cycle, for unit j with net input net_j = sum_i w_ij * a_i:
- if net_j > 0: a_j(t+1) = a_j(t)(1 - decay) + net_j * (1 - a_j(t))
- else: a_j(t+1) = a_j(t)(1 - decay) + net_j * (a_j(t) + 1)
- Clip to [-1, 1]. Stop when no activation changes by more than a small threshold, or at a cycle cap (a few hundred).
- Accept a unit if final activation is above a small positive cutoff; reject if below its negative.

Parameters from the papers: excitation .04-.05, inhibition -.06 to -.2, data excitation .1, decay .05. They are not stable across the author's own studies (a12 v a02), so treat them as tunables and run a sensitivity sweep. Real failure modes: if excitation is too high relative to inhibition, inferior hypotheses are not rejected; far too high, the net oscillates (seen at excitation .17 on Chambers). (a03)

Caveat: the parameter values are confirmed in the opened text (a02, a03). The exact update-rule constants above are the standard activation rule of this model family, written from knowledge, and were not re-read line by line this session. Check against the 1989 text before relying on them.

### 4.2 Coherence as MaxSAT or MAX-CUT (more robust for an agent)

- Elements: claims c_1..c_n. Constraints: (i, j, w) with w > 0 for "go together" and w < 0 for "conflict" (magnitude = strength).
- Objective: choose the accepted set A to maximise the summed |w| over satisfied constraints.
- Exact: weighted partial MaxSAT with an off-the-shelf solver (RC2, as in BeliefBank, ConCoRD and REFLEX). For under about 50 claims this is fast.
- Approximate: greedy flip with random restarts (the 1998 paper; matches ECHO on tested cases). SDP gives the 0.878 guarantee but is heavy.
- Anchor: clamp evidence claims to accepted with a large weight (data priority). Without an anchor the solution is only defined up to a global flip.
- Output: the accepted set plus the "coherence gap" (weight lost). Report the margin between best and second-best solution. A small margin means "not decided" (compare Peyer, the hung jury).

### 4.3 The LLM-plus-solver pipeline (BeliefBank, ConCoRD, Maieutic, REFLEX)

1. The LLM proposes claims (answers, explanation statements, rules). Each gets a base weight from the LLM's probability or a fixed value.
2. Links: an LLM or NLI model judges pair relations (entail, contradict, none). Gold constraints if available.
3. Code runs MaxSAT. It flips or drops claims at minimum cost.
4. Optionally feed the chosen set back as context (BeliefBank "relevant feedback"). The solver alone gave more than feedback alone (85.8 v 79.5 F1 at batch 10). (b01, b02)

Where quality comes from: link quality (ConCoRD oracle gap), base-claim quality (Entailer: 33% of failures are wrong beliefs), and formalisation fidelity (VERGE: 23.3% of unanimous formalisations wrong). (b05, b25, d11)

### 4.4 Human-side model of coherence shift (Holyoak and Simon, Qiao)

A constraint network with nodes for verdicts (guilty, not guilty), evidence items and arguments. Evidence-argument links are positive for support. The two verdicts inhibit each other. Activation flows both ways. As the verdict node leans, activation flows back to evidence and raises the rated strength of items that support it. That backward flow is the "bidirectional reasoning" that makes ratings drift. Qiao 2026 found the flow goes from verdict to agreement ratings but not strongly back to likelihoods. (d07)

Engineering lesson: any pipeline where the model rates evidence after it has a leaning builds in this drift. The remedy is structural: rate before the verdict, rate in a fresh context, lock the ratings in code.

### 4.5 IBE-Eval features (code-computed scoring of competing explanations)

Four features, all computed by code: logical consistency (Prolog proof success), parsimony (proof depth, concept drift), coherence (mean NLI entailment of each If-Then step) and hedging (count of uncertainty words). A linear model over them picks the better of two explanations. Hedging was the strongest single predictor. Logical consistency was uninformative because LLMs rationalise equally well for wrong options. (a27, b08, b09)

## 5. What holds up

**Holds up well.**
- Human coherence shift. Several papers from one tradition (Holyoak and Simon 1999, Simon et al 2001, Glockner) plus a choice-task extension all find it. A new-sample 2026 replication (N=130, F=96.31) agrees, though a Holyoak co-author wrote it. It survives a one-week delay (N=19) and appears without a decision task (N=125, N=166). The shift is a comprehension process, not just post-decision dissonance. (d01-d06, c10)
- Solver over claims raises consistency. Three independent 2021-23 systems (BeliefBank, ConCoRD, REFLEX) agree: consistency up 8-25 points. (K11, K28; b21, d12)
- Coherence does not equal truth. Said by Thagard himself, and shown by IBE-Eval (consistent explanations for wrong answers), REFLEX (accuracy flat) and Entailer (33% of failures are wrong beliefs). (c03, b09, d12, b25)
- Solver on strict deduction beats plain CoT: Logic-LM +18.4 over CoT on average, VERGE +15 to +17 on FOLIO with Sonnet 3.7. (c24, d10)

**Failed, contested or weak.**
- ECHO as a predictor of verdicts. Every legal "success" is retrodiction with author-coded input. Simpson failed under pure ECHO and was fixed after the verdict. Peyer (7-5 hung jury) is a partial miss read as a hit. No blind coding, no intercoder reliability. Thagard conceded the analyses are not good psychological tests (1989). No independent replication of ECHO on human confidence was found (Schank and Ranney, Read and Marcus-Newhall not opened). (a04-a06, a14, d14, d15)
- ECHO v Bayes. The Bayes arm used guessed probabilities, so the comparison shows effort, not accuracy. (a13)
- Likelihood-ratio measure. In Qiao et al. the shift is not reliable when strength is a numeric likelihood ratio (p=.083, .44). The classic finding depends on how evidence strength is measured. (d06)
- Baselines were not clean. Simon 2001: the groups already differed by .80 at baseline (p=.01), 2.55 post. Holyoak and Simon Exp 1: pretest difference p=.06. Some of the "shift" is preexisting preference. Pre-ratings were taken in the same session except Exp 2. (d01, d04)
- No effect sizes in the founding papers (only F and p). Do not compute and quote d.
- Gold constraints are not always best. In ConCoRD, estimated links beat gold on BeliefBank; gold wins on ConVQA and NQ. Claim K12 is contested. (b05, c22)
- Argument-graph solvers (ArgLLM) are not more accurate than CoT. (b10)
- Solver helps less where CoT is already strong: ProntoQA CoT 98.79 > Logic-LM 83.20; ProofWriter PoT 98.2 > VERGE 93.0. (c24, d10)
- ECHO sensitivity: needs excitation and inhibition in a band and can oscillate. Tested only by the author on four cases. (a03)

**Moderators of the human effect.** Choice difficulty and attribute disparity raise the shift (Lee and Holyoak). Character information spreads it to loosely linked points (partly). Communicating the case (transmitting) increased the shift (Simon 2001 Exp 3). Emotion adds to it, and a judicial instruction did not remove the emotion effect (a26). Free information search does not prevent it: people searched mostly for disconfirming information and still shifted (a22, abstract only).

**Interventions that worked or did not.**
- Worked (LLM systems): MaxSAT solver over claims; both entail and contradict links; relevant-belief feedback given incrementally; cross-model agreement as an alarm for bad formalisation (catches 94.1% of bad formalisations at 28.8% precision); code-computed explanation features (IBE-Eval).
- Did not work: balancing instructions against role bias in LLM summaries (c16); a judicial instruction against emotion bias in mock jurors (a26); logical consistency as a truth signal (b09); feeding all raw answers at once instead of incrementally (74.5% accuracy, below incremental) (b02).
- Not tested: any debiasing of coherence shift in LLMs.

## 6. Language models

**Solvers over a model's own claims (2021-2023, small models).**
- BeliefBank (Macaw, T5-based): raw F1 about 69%, with solver about 86. Consistency about 72% to about 95%. (b01, c21; correction C1 in critique)
- ConCoRD: +8.3 F1 points (.831 to .914) and +7.6 (.855 to .931) on BeliefBank; +5.0 points on ConVQA LXMERT; +1.4 to +1.9 on NQ. Gains shrink on open-ended tasks. (b05, c22)
- Maieutic prompting (GPT-3): 72.5 v 61.4 for self-consistency on Com2Sense, a gap of 11.1 points (the paper claims "up to 20%"). Tree depth 2 and width 3 saturate. (b03, c19, c20)
- REFLEX: consistency +8 to +11, accuracy -0.2 to +1.0. So the solver mostly makes the model agree with itself. (d12)
- Entailer: no accuracy change, more faithful proofs, 80 to 360 s per question. (b07)

**Formal-logic solvers on current models.**
- Logic-LM (GPT-4): +9.8 on FOLIO, +11.5 on ProofWriter, +8.0 on AR-LSAT over CoT, but -15.6 on ProntoQA. (c24)
- VERGE (Sonnet 3.7, GPT-OSS): FOLIO 87.9 v 70.4 CoT and 72.4 SC (k=3). Token cost not equalised in the text read. A specialised PoT baseline wins ProofWriter (98.2 v 93.0). (d10)
- Formalisation is the weak joint. 76.7% fidelity when models agree, 56.0% when not. Gold labels agree with gold formulas only 72.6%. A 20B model gave about 30% valid syntax. Legal text is vaguer than FOLIO and is untested. (d11)

**Building the graph.** Reasoning models (o1/o3/o4-mini) rebuild a known signed graph exactly about half the time on sparse graphs. Non-reasoning models do worse, and dense graphs are harder. One build per graph; no repeat variance. (d08, d09)

**Explanation scoring.** IBE-Eval on GPT-3.5 and LLaMA 2: up to 77%. Current models and real legal tasks untested. (a27, b08)

**Do LLMs show coherence shift?**
- Lehr et al. 2025: GPT-4o rated Putin far more favourably after writing a pro-Putin essay (d=2.164, n=150). Choice framing moderated it (d=0.981 pro, 0.252 anti, n=900). (a28, c12, c13)
- Cummins, Elson and Hussey 2025: the valence shift also appears when the user wrote the essay, in chat, API and single-monologue versions. So it may be context-window sensitivity. Sample sizes not stated. Lehr's reply says the choice-versus-no-choice contrast is what matters and ran a new 900-response study; its numbers were not extracted. (c14, d16, a29)
- Either way, for an agent the practical fact is the same: what is in the context window moves the model's rating. That is a coherence shift in effect, whatever the cause.
- Abduction In Silico (2026): 16 models from 7 developers replicate human abduction patterns (sensitivity to explanation quality, suppression by alternatives). Abstract only. (a30 [M])

**Law-specific.** o1 and Llama 3.3 70B omit unfavourable facts when told to act as defense or prosecutor. Balancing instructions did not remove it. Humans confirmed (under 20% v 100%). The authors flag "stakeholder drift bias" as untested speculation. (c15-c18)

**No study found** that (a) runs ECHO or a similar network on an LLM-built legal evidence graph, (b) measures an LLM's evidence re-rating after a verdict in the same versus a fresh context, (c) compares LLM-judged, NLI and gold links on a frontier model, or (d) gives a flip-to-wrong rate for a solver. (K22, d17). The absence is search-limited (about 8 searches, rate-limited APIs), not proven.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5 of SCHEMA.md. No operator (O1-O8) fits this subfield; it acts on selection (S7) and on the rating step.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Consistency is not truth.** Never treat "the claims agree" as a pass. Report solver consistency and accuracy separately. A pass still needs an external check (G3). | G3, G10 | [E] | K15, K28; c03, b09, d12 |
| A2 | **Do not let the model re-rate evidence after it has a leaning.** Evidence ratings and link weights are fixed in code before the answer is chosen and not edited afterward. | G (rule under G2/G10) | [E] for humans; for LLMs the effect is real in practice but its cause is contested | K07, K23; d01-d06; c12, c14 |
| A3 | **Selection among claims is done by code**, not by asking the model which story is more coherent. Rate each claim or link separately, then select in code. | G5, S7 | [E] for the principle (consistency gains in three systems) | K01, K02, K11; a10, b01, b05, d12 |
| A4 | **Weak links must not outvote a strong supported claim.** If a solver flips a claim that has direct test evidence, keep the claim and flag the conflict. | G2, S7 | [E] as a risk (rat/cat; REFLEX net-zero accuracy) | K14; b24, d12 |
| A5 | **Route by task type.** A solver for strict deduction. CoT or program-of-thought where they win (ProntoQA, ProofWriter). | S0 | [E] | K18; c24, d10 |
| A6 | **Do not cite ECHO as validated.** No schema text should rest on ECHO verdict matches. | none (rule for research notes) | [E] | K03, K27; a06, d14 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Fresh-context re-rating.** Evidence ratings after a verdict are made in a fresh context holding only the pre-rating. Measure drift against same-context re-rating. | G, S1/S9 | [C] | K20, K23; c12-c14, d02 |
| T2 | **Claims-plus-links solver over an LLM-built graph (MaxSAT or greedy)** for items with competing hypotheses, against majority vote and CoT at equal tokens. | S7 | [S]; old models only | K11, K22; b01, b05, b03 |
| T3 | **Link source:** LLM-judged v NLI v oracle. | S2 link step | [C] | K12; b05, c22 |
| T4 | **Cross-model formalisation agreement as a gate.** Disagreement means fall back to CoT. | S0/S7 | [S] | K26; d11 |
| T5 | **Repeat-build stability check.** Build the graph three times. If the verdict differs, mark the item uncertain and spend more budget (G12). | S2, G12 | [S] | K06, K25; d08 |
| T6 | **IBE-Eval-style features** (hedging, proof depth, concept drift) as a code score for choosing among candidate explanations. | S7 | [S]; old models | K16; a27, b08 |
| T7 | **Numeric likelihood-style ratings** instead of free-text agreement when rating evidence. | S1 rating step | [S] | K24; d06 |
| T8 | **Margin threshold** (accept only if the margin over the rival exceeds a set value; else best-so-far per G6). | S7, G6 | [S] | K04, K10; a14 |
| T9 | **Role-neutral evidence summaries:** summarise each side in separate fresh contexts, merge by code. | S1 | [S] | K21; c15-c17 |

## 8. Concrete tests on our bench

All arms get equal tokens (G7). Count setup tokens. At least 3 seeds per arm. Report a paired difference with a 95% interval.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Short legal-style cases (about 12 evidence points, 2 verdicts), each point pre-rated 1-7 | (a) rate, give verdict, re-rate in the same context; (b) re-rate in a fresh context with only case and pre-ratings; (c) rate once, no re-rate | Mean signed shift of ratings toward the verdict; share of items with verdict-aligned shift above 1 point | (a) shows a clear shift. (b) cuts it by half or more if context drives it. If (a) equals (b), the fix does nothing. |
| B2 (T2) | ARC-style or BrainTeaser items with 3-6 candidate hypotheses and an external check | (a) plain model, one answer; (b) majority vote of k short attempts; (c) model writes claims and links, MaxSAT in code over candidates | Accuracy; consistency; flip-to-wrong rate (correct before, wrong after) | Consistency up; accuracy gain near zero or small (REFLEX pattern). Keep only if (c) beats (b). |
| B3 (T3) | 60 hand-labelled claim pairs (entail, contradict, none) from our bench | LLM-judged links; NLI links; hand labels | Link F1, then downstream accuracy | Oracle best on open QA; no clear winner on closed fact sets (ConCoRD pattern). |
| B4 (T4) | Strict-deduction items (FOLIO-style) and a legal-rule set | (a) CoT; (b) one-model formalisation + solver; (c) two-model formalisation, solver only on agreement, else CoT | Accuracy; coverage; silent-error rate | (c) at least equals (a) on deduction, fewer silent errors than (b). |
| B5 (T5) | 20 real or synthetic cases with at least two rival hypotheses | Build the graph 3 times independently, solve each | Edge overlap (Jaccard); verdict agreement across builds | Agreement under 80% means graph building is too noisy to select by. |
| B6 (T6) | Two-option causal or diagnostic items with a model-written explanation per option | (a) LLM judge picks; (b) code score from hedging, proof depth, concept drift, NLI | Accuracy at picking the correct-answer explanation | IBE-Eval reported +17 over a GPT-3.5 judge. Expect a smaller gap against a current judge. |
| B7 (T7) | Same cases as B1 | Free-text agreement v numeric probability of each point given each verdict | Drift size | Qiao: likelihood-style ratings drift less reliably. Expect smaller drift under numbers. |
| B8 (T8) | Constructed cases where the coherent story and the standard of proof diverge | Solver with margin threshold 0, 0.1, 0.2 | Accuracy against the designated outcome; share of low-margin items | Unknown size. Needs a threshold for "not proved". |
| B9 (T9) | Cases with a one-sided framing | Neutral, advocate-A and advocate-B summaries in separate contexts, merged by code | Share of key facts included | Balancing instructions failed in the paper; separate contexts may work. |

## 9. What does not transfer, and why

- **ECHO's verdict record.** Retrodiction with author-coded input and known outcomes. It says nothing about performance without hindsight. Do not use it as justification.
- **Hand-set parameters.** Excitation, inhibition and decay were hand-tuned per paper (a12 v a02). We have no principled values for LLM-built graphs.
- **Human-participant numbers.** The shift effects come from undergraduates and online samples in one lab tradition, on short vignettes. F values (no d) say nothing about size for an LLM.
- **Dissonance and motive.** Humans shift partly to feel consistent. An LLM has no stake in a verdict. If it shifts, the cause is context content, and the remedy differs (Cummins).
- **PCS as a decision rule.** That humans use PCS (50-60%) says what humans do, not what the agent should do.
- **Training-time coherence (deductive closure training).** Needs fine-tuning. Not usable in a frozen scaffold, though the contradiction-detection step can run at inference. (c23)
- **Emotional coherence (HOTCO) and the Simpson fix.** Valence values were set after the verdict. An agent needs no hot-cognition layer, and the tuning does not transfer. (a14)
- **Law-specific standards.** Burden of proof and admissibility are rules, not weights. A network can only mimic them with a designer-chosen threshold.
- **Small-model gains.** All MaxSAT-over-claims gains are on 2021-22 models (Macaw, GPT-3, T5). They shrink on open tasks (ConCoRD NQ: +1.4 to +1.9). Do not assume they hold on frontier models.
- **ECHO's typed inputs.** ECHO inputs were typed with care by experts. LLM-built propositions bring graph noise as a new failure source.
- **Argument-graph semantics (ArgLLM).** Equal to CoT in accuracy. Its gain is contestability, which our bench does not score.

## 10. Open questions

1. Does a frontier LLM show a coherence shift on legal evidence when it rates, decides and re-rates in the same context versus a fresh one? No study. Cheapest gap to run. (K22)
2. Does a solver over an LLM-built evidence graph beat majority vote or CoT at equal tokens on current models? Only small-model and formal-logic evidence.
3. How much does the verdict change across independent builds of the same real case? Only synthetic graphs, one build each. (K06, K25)
4. What is the flip-to-wrong rate of a solver? Only net effects (REFLEX).
5. Which link source is best on current models: LLM-judged, NLI, gold? ConCoRD is mixed. (K12)
6. Did any independent group replicate ECHO on human confidence data (Schank and Ranney; Read and Marcus-Newhall)? Not opened.
7. Does probabilistic coherence (Bovens and Hartmann; Olsson) beat ECHO on multiple-testimony tasks? Not opened.
8. Does the Lehr and Cummins dispute resolve? Cummins gave no sample sizes. Lehr's three-condition reading study numbers were not extracted.
9. What are the effect sizes of the human coherence shift? Founding papers give F and p only. Is there a meta-analysis?
10. Does routing by task type hold on legal text, where formalisation is vaguer than FOLIO?
11. Do IBE-Eval features still beat an LLM judge on a current model? Only a GPT-3.5 baseline exists.
12. Can predecisional distortion (Russo) be told apart from network coherence shift on verdict data? Not opened.

## 11. Sources

Founding and theory
- [V] Thagard (1989) Explanatory coherence, BBS 12(3):435-50, with author's response. https://www.gwern.net/doc/philosophy/epistemology/1989-thagard.pdf (a01-a09, d14, d15)
- [M] Thagard (1989), scan copy, no text layer. http://cogsci.uwaterloo.ca/Articles/1989.explanatory.pdf (c06)
- [V] Thagard and Verbeurgt (1998) Coherence as constraint satisfaction. https://arts.uwaterloo.ca/~pthagard/Articles/coherence.1998.pdf (a10, a11). Record only [M]: https://doi.org/10.1207/s15516709cog2201_1 (c05)
- [V] Thagard (2004) Causal inference in legal decision making. https://arts.uwaterloo.ca/~pthagard/Articles/causal-inference.pdf (a12, a13). Record [M]: https://doi.org/10.1080/08839510490279861 (c07)
- [V] Thagard (2003) Why wasn't O.J. convicted? https://arts.uwaterloo.ca/~pthagard/Articles/Coherence/OJ.pdf (a14). Record [M]: https://doi.org/10.1080/0269993024400002 (c08)
- [V] Thagard (2005) Testimony, credibility, and explanatory coherence. https://arts.uwaterloo.ca/~pthagard/Articles/testimony.pdf (a15)
- [V] Thagard (2006) Evaluating explanations in law, science, and everyday life. https://arts.uwaterloo.ca/~pthagard/Articles/evaluating.pdf (a16)
- [V] Thagard (1992) Adversarial problem solving. https://arts.uwaterloo.ca/~pthagard/Articles/adversarial.pdf (a17)
- [V] Thagard (2007) Coherence, truth, and the development of scientific knowledge. https://arts.uwaterloo.ca/~pthagard/Articles/coherence-truth.pdf and http://cogsci.uwaterloo.ca/Articles/coherence.truth.pos.2007.pdf (a18, c01-c03)
- [V] Wikipedia, Explanatory coherence. https://en.wikipedia.org/wiki/Explanatory_coherence (c04)
- [M] Araszkiewicz (2013) Limits of constraint satisfaction theory of coherence. https://doi.org/10.1007/978-94-007-6110-0_12 (b19, c09; record only)
- [M] Bovens and Hartmann (2003); Olsson, probabilistic coherence. https://doi.org/10.1093/0199269750.001.0001 (b20; from memory)

Human experiments
- [V] Holyoak and Simon (1999) Bidirectional reasoning in decision making by constraint satisfaction, JEP:General 128(1). Opened via the UCLA reasoning lab copy, https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/ (d01-d03). DOI https://doi.org/10.1037/0096-3445.128.1.3 (a19, b13 [M] earlier records)
- [V] Simon, Pham, Le and Holyoak (2001) The emergence of coherence over the course of decision making, JEP:LMC 27(5). Same UCLA lab folder (d04, d05). DOI https://doi.org/10.1037/0278-7393.27.5.1250 (b14 [M])
- [M] Simon, Krawczyk and Holyoak (2004) Construction of preferences by constraint satisfaction, Psych Science. https://doi.org/10.1111/j.0956-7976.2004.00678.x (a20)
- [M] Simon, Snow, Read (2004) The redux of cognitive consistency theories. https://doi.org/10.1037/0022-3514.86.6.814 (b15)
- [M] Simon (2004) A third view of the black box, U Chicago Law Review 71. https://chicagounbound.uchicago.edu/uclrev/vol71/iss2/3 (b11, abstract)
- [M] Simon, Stenstrom, Read (2015) The coherence effect. https://doi.org/10.1037/pspa0000029 (b16)
- [M] Simon and Read (2025) Toward a general framework of biased reasoning. https://doi.org/10.1177/17456916231204579 (a25)
- [M] Glockner (2010) Coherence shifts in probabilistic inference tasks. https://doi.org/10.1002/bdm.668 (a21)
- [M] Glockner and colleagues (2016) Information search, coherence shifts. https://doi.org/10.2139/ssrn.2816609 (a22)
- [M] Glockner and Engel (2013), PCS in legal cases. https://doi.org/10.1111/jels.12012 (b17)
- [M] Russo, Medvec and Meloy (1996) Distortion of information during decisions. https://doi.org/10.1006/obhd.1996.0038 (b18)
- [V] Forst and Glockner (2026) Intuitive and deliberate decisions. https://pmc.ncbi.nlm.nih.gov/articles/PMC12916998/ (a23)
- [V] Glockner and Jekel (2026) Cognitive reflection enhances rationality. https://pmc.ncbi.nlm.nih.gov/articles/PMC13295265/ (a24)
- [V] Mock-juror emotion and evidence evaluation (2025), Behavioral Sciences 15(7):965. https://pmc.ncbi.nlm.nih.gov/articles/PMC12292101/ (a26)
- [V] Lee and Holyoak (2020) Coherence shifts in attribute evaluations (bioRxiv). https://www.biorxiv.org/content/10.1101/2020.08.19.258046 (c10, c11)
- [V] Qiao, Kamper, Lagnado and Holyoak (2026) Coherence and Bayesian reasoning in legal judgment, CogSci 48. https://escholarship.org/uc/item/7q6407kv (d06, d07)

Language-model work
- [V] Kassner et al. (2021) BeliefBank. https://arxiv.org/abs/2109.14723 and https://aclanthology.org/2021.emnlp-main.697.pdf (b01, b02, b24, c21)
- [V] Jung et al. (2022) Maieutic prompting. https://arxiv.org/abs/2205.11822 and https://aclanthology.org/2022.emnlp-main.82.pdf (b03, b04, c19, c20)
- [V] Mitchell et al. (2022) ConCoRD. https://arxiv.org/abs/2211.11875 and https://aclanthology.org/2022.emnlp-main.115.pdf (b05, b06, c22)
- [V] Tafjord, Dalvi Mishra, Clark (2022) Entailer. https://arxiv.org/abs/2210.12217 (b07, b25)
- [V] Dalal et al. (2024) IBE-Eval. https://arxiv.org/abs/2402.10767 and https://aclanthology.org/2024.acl-long.14.pdf (a27, b08, b09, b26)
- [V] Freedman et al. (2025) Argumentative LLMs. https://arxiv.org/abs/2405.02079 (b10)
- [V] Kassner et al. (2023) REFLEX, language models with rationality. https://arxiv.org/pdf/2305.14250 (d12)
- [V] Akyurek et al. (2024) Deductive closure training. https://aclanthology.org/2024.findings-acl.584.pdf (c23)
- [V] Pan et al. (2023) Logic-LM. https://aclanthology.org/2023.findings-emnlp.248.pdf (c24)
- [V] Singh et al. (2026) VERGE. https://arxiv.org/pdf/2601.20055v3 (d10, d11)
- [V] Huntsman and Thomas (2025) Benchmarking graph construction by LLMs for coherence-driven inference. https://arxiv.org/pdf/2502.13953 (d08, d09). Same title [M]: https://doi.org/10.1109/icdmw69685.2025.00116 (a31)
- [V] Ambati (2026) Certified coherent reasoning via weighted MaxSAT (workshop abstract page). https://iclr.cc/virtual/2026/10017421 (d13)
- [V] Lehr et al. (2025) Kernels of selfhood. https://osf.io/preprints/osf/zewbr_v1 and https://pmc.ncbi.nlm.nih.gov/articles/PMC12107184/ (a28, c12, c13)
- [V] Lehr et al. (2025) Reply to Cummins et al. https://pmc.ncbi.nlm.nih.gov/articles/PMC12415207/ (a29)
- [V] Cummins, Elson and Hussey (2025) Cognitive dissonance in LLMs. https://osf.io/preprints/psyarxiv/3ny67_v1 (c14, c26, d16)
- [V] Cho, Hoyle and Hermstruewer (2025) Modeling motivated reasoning in law. https://aclanthology.org/2025.nllp-1.7.pdf (c15-c18)
- [M] Abduction In Silico (2026). https://link.springer.com/article/10.1007/s11023-026-09803-x (a30, abstract)
- [M] Search records on absence of studies: c25, d17, b23 (no source URL of substance)

Note on checks: the critique re-opened 7 sources and corrected the BeliefBank base F1 (about 69%, not 72%), the claim that gold constraints always win (false for BeliefBank), and the unstable ECHO parameters. These corrections are applied above.
