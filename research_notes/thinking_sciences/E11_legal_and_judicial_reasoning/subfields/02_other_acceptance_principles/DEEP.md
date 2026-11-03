# Other acceptance principles: deep document

*Subfield E11.02. Written 2026-11-03 from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01 to d17) point to lines in the evidence files. Claim ids (K01 to K26) point to claims.jsonl. Status marks: [E] established (two or more independent sources), [S] single source, [C] contested.*

**Honest summary first.** The founding experiments for this subfield (Pennington and Hastie 1986, 1988, 1992) could not be opened in any run (a27, a28, a29, b27, d03). So the claim that coverage and uniqueness drive human verdicts and confidence rests on the authors' own later restatements (a01 to a04, b14, b15, d01, d02), which contain no numbers. What we do have with exact numbers is (1) the coherence-shift experiments of Holyoak and Simon, Simon et al., and Engel and Gloeckner, (2) Thagard's explanatory-coherence network, (3) a handful of LLM studies that compute coherence-like scores in code or measure LLM coherence effects, and (4) general results on agreement, self-correction and judge bias that bear on how an agent should compute "coverage, coherence, uniqueness" in code. No study found tests whether an LLM's choice and confidence follow planted differences in story coverage, coherence and uniqueness (K19, c23, d17). That test is ours to run.

## 1. What it is

Pennington and Hastie's story model says a juror builds a story from the trial evidence plus world knowledge, learns the verdict categories, and then matches the story to a category. Part of the model is a set of **certainty principles** that say when a story is accepted and how confident the juror is. In the 1996 restatement (a01 to a04, b14) there are three:

| Principle | What it says | Role |
|---|---|---|
| **Coverage** | How much of the trial evidence the story accounts for. More coverage, more acceptable. Poor coverage lowers confidence in the story and in the verdict. | Acceptance |
| **Coherence** | Three parts: consistency (no contradiction with believed evidence or with other parts of the story), plausibility (fits what usually happens), completeness (the expected story structure has "all its parts", with motives, plans and intentions linking episodes). The three combine into one coherence level, with no stated rule. | Acceptance |
| **Uniqueness** | If more than one story is judged coherent, none is unique and belief in any one of them is diminished. If one coherent story exists, it is accepted. | Confidence only |

The 1994 restatement for judges (d01) lists five things that set global confidence: coverage, completeness, internal consistency, plausibility and uniqueness. There, uniqueness is defined by how far the juror is entertaining alternative stories, not by how many alternatives exist.

This subfield is "other acceptance principles": coherence and uniqueness as the certainty principles beyond coverage (coverage is treated in subfield 01, story model of juror decisions). Three bodies of work grew around them:

1. **Coherence as a process** (psychology of constraint satisfaction): Holyoak and Simon 1999, Simon et al. 2001, Simon and Holyoak 2002, Engel and Gloeckner 2013. Coherence is not only a property of a finished story. It is built while the person reads, and it bends the person's ratings of single pieces of evidence.
2. **Coherence as computation** (Thagard 1989, 2003; Huntsman 2025; the MaxSAT line of Kassner, Jung, Mitchell). Coherence can be written as a constraint problem and solved by a program.
3. **Coherence and uniqueness in language models** (Dalal 2024, de Langis 2025, Lehr 2025, and the agreement literature). Whether a model's own judgements of coherence are good, whether code can do better, and whether agreement across samples works as a uniqueness signal.

Why it matters for our agent: the schema's S7 SELECT picks among candidates by code. The certainty principles are a ready-made menu of code-computable scores: coverage (share of evidence items explained), consistency (contradiction count), completeness (empty slots in a template), uniqueness (gap between the best and the runner-up). The key warnings from the research are that the principles have no validated combining rule (K02), that human coherence is itself a bias source (K03, K07), and that a model's self-rated coherence is weak (K14).

## 2. History and theories in depth

### 2.1 The story model and its certainty principles (1986 to 1996)

Pennington and Hastie ran mock-juror studies in the 1980s and early 1990s (1986 JPSP 51:242; 1988 JEP:LMC 14:521; 1992 JPSP 62:189; 1993 Cognition 49:123). The designs named in later papers: presenting evidence in story order versus issue order (witness by witness) and checking verdicts and confidence; checking whether jurors' free recall is organised as a story. We could not open any of them (a27, a28, a29, b27, d03). A peer commentary printed with Thagard 1989 says the finding that evidence order changes verdicts conflicts with Bayesian updating, which is order-free (a08, c09). Subfield 01 cites order cells of about 78% and 31% guilty verdicts, but this is second-hand and unverified (a27, K20). Do not quote it.

What we can read are the authors' own restatements. The 1996 law review article (a01 to a04, b14, b15) states the three principles in the table above. It gives no weights, no formula, no per-story confidence drop. It says rival models (Bayesian "meter" models that add up evidence, and prejudice-trigger models) fit mock-juror data less well, in the authors' words: "For the most part, empirical studies of mock-jurors' decisions do not support this model" (b15). That is a claim by proponents citing their own studies, not a fresh test.

A commentator in the Thagard 1989 issue says Pennington and Hastie give no theory of what makes a good story (a08). We rate that as established (K02): any scoring formula we build is our own design.

### 2.2 Thagard's explanatory coherence (1989) and emotional coherence (2003)

Thagard (a05 to a08, c06 to c10) built on Pennington and Hastie and wrote seven principles of explanatory coherence. The opened text names symmetry, explanation, analogy, data priority, contradiction, acceptability and system coherence (a05; c10 also lists competition). "Explanation" is the most important: a hypothesis coheres with what it explains, and co-hypotheses that jointly explain cohere with each other. The program ECHO is a localist connectionist network (a06, c06). Propositions are units. Explanation and analogy give excitatory links. Contradiction and competition give inhibitory links. Evidence units receive "data excitation". Activation spreads until the network settles. Positive final activation means accept, negative means reject. Defaults: data excitation .1, decay .05, inhibition -.2, simplicity impact 1 (c06 lists excitation .05).

ECHO was run on Lavoisier's chemistry and on two real murder trials, Chambers (the "preppy murder") and Peyer (a07, b17, c07). In Chambers it gave a clear win to the guilt hypotheses. In Peyer the real jury hung 7 to 5 for conviction. ECHO found more coherence in guilt but rejected innocence much less strongly than in Chambers (Table 11). The author says results hold when decay, excitation, inhibition and data excitation are halved or doubled (c08). Limits: fitted after the fact to newspaper accounts, not a prospective prediction; links are hand-coded; commentators note many free parameters (c06, c09).

Thagard 2003 (a09 to a11, b16) asked why Simpson was acquitted. ECHO accepted that Simpson was the killer and that the police tried to frame him, even without the inadmissible evidence. A hand-built Bayesian network in JavaBayes agreed: P(killed) = .72, P(drug killings) = .29, P(police framed) = .99 (which the author calls too high). Both models predicted guilt, the jury acquitted. Thagard added emotional valences (HOTCO): each unit has an activation and a valence, and valence feeds back to activation. A valence link of .05 to "O.J. is good" and 7.05 to "LAPD is good" reproduced the acquittal. Update rule: a_j(t+1) = a_j(t)(1-d) + net_j(max - a_j(t)) if net_j > 0, else net_j(a_j(t) - min), with d about .05. This is a fit after the verdict, with parameters set by hand (b16). The "60 conditional probabilities" claim was not re-found in the text (critique.md), so treat it as unverified (K11).

Lesson: a pure coherence model with plausible inputs can reach the wrong answer when the inputs omit a prior or a valence. For us this is a reason to keep priors (class pass rates, S0) as a separate input to selection.

### 2.3 Coherence shift (1999 to 2013)

The key human result: the act of reading an ambiguous case shifts the person's ratings of single disputed arguments toward whichever side the person will end up favouring, and this happens before any decision is stated.

**Holyoak and Simon 1999** (a12 to a15, b04 to b07). Students judged Quest v. Smith (an internet libel case) built from six paired arguments. They rated each argument before the case, then again after reading and after a verdict.
- Exp 1: 54 students, 48 analysed after dropping 6 switchers; verdicts 26 Quest, 22 Smith; 75% confident (4 or 5 of 5). Verdict x test interaction F(1,44) = 35.3, p < .001.
- Exp 2: about 19 analysed, one-week delay; F(1,17) = 7.71, p = .01. Memory for one's own earlier ratings drifted toward the final verdict: recalled Smith-supporter pretest score -1.32 against actual -0.30, F(1,16) = 3.66, p = .07; verdict predicted recall, r(16) = .43, p = .07 (critique.md corrected the a14 numbers; b06 is right).
- Exp 3: 80 recruited, 64 analysed. A "Bad Smith" character cue gave 78% Quest verdicts against 28% for "Good Smith", chi2(1, N=64) = 16.1, p < .001. Motive rating 1.83 against -2.75, t(62) = 8.98. A single manipulated fact spread to neighbouring points and, through one shared analogy, to a second case.
- Switchers: 6 of 30 (20%) in the three-phase group changed verdict between interim and posttest and did not show the pattern (b05).

**Simon, Pham, Le and Holyoak 2001** (a16 to a19, b01 to b03):
- Exp 1: N = 47 analysed of 50; verdicts 49% / 51%; 93% at least moderately confident; interaction F(2,86) = 35.3, p < .0001. Gap between eventual Quest and Smith supporters: .80 at baseline, 2.23 at interim, 2.55 after decision. Cronbach alpha across the six ratings: -0.25, .74, .80.
- Exp 2: memorise-only instruction; N = 120 of 125; F(2,236) = 59.1. Alpha .08, .70, .80. Significant positive correlations among 21 pairs: 2 at baseline, all at postdecision.
- Exp 3: N = 157 of 166; decision, reception and communication sets did not differ (condition x shift F(4,302) < 1); main F(2,302) = 78.6. Alpha .12, .77, .80. Gap .32, 2.03, 2.50.
- Reading: most of the shift happens before commitment (interim to post was not significant, p > .30). Coherence is generated while the case is processed; decisions follow from it.

**Simon and Holyoak 2002** (a30, b08) review this as constraint satisfaction with bidirectional links, against dissonance accounts, and say the shift has replicated many times. Those replications are the authors' own lab and mostly the same case (b08).

**Engel and Gloeckner 2013** (a20, a21, b09 to b13, d04, d05) is an independent lab (Bonn, Germany; different stimulus; German students). Students played prosecutor or defence, then predicted the court ruling.
- Exp 1: 149 students. Predicted conviction 64% (prosecution, n = 73) against 50% (defence, n = 76). Subjective p(guilty) 66% against 50%. Coherence shifts fully mediated the role effect: indirect effect .31, 95% CI [.19, .44]. Information search did not mediate (.020, CI [-.04, .10]).
- Exp 2: 92 students, an incentive of 100 euro paid in 1 of 10 cases. 56% (n = 50) against 40% (n = 42). Logit coefficient .73, z = 1.47, p = .07 one-sided (p = .028 after excluding 7 whose prediction differed from their own verdict). A large accuracy payment did not remove the bias.
- Exp 3: 29 students (13 and 16). Plea offers 70.0 (prosecution) against 18.4 (defence), t(27) = 5.00, p < .001. Predicted guilty 46% against 37%.
- Direction of the shift: mainly devaluing conflicting evidence. Prosecution: contra-guilty evidence -125.1 (SE 16.3), pro-guilty +9.7 (SE 10.2). Defence: pro-guilty -54.5 (SE 16.6), contra-guilty -15.7 (SE 14.4).
- Time: the paper states coherence effects are "transient", citing Simon et al. 2008 (not opened). Role effect on verdict prediction: 14% in their data against 17% in Simon et al. 2008. Quick deciders were biased, slow ones not. In one study the time x role interaction was z = -3.06, p = .002 (short p = .003, long p = .66). In Exp 2 the interaction was only p = .24 (quick half p = .003, slow half p = .23), so "slow means unbiased" is weak (K09).

### 2.4 Explanation selection by code in language models (2021 to 2026)

- **BeliefBank** (c16): a weighted MaxSAT solver over a store of model answers and hand-written constraints revises clashing beliefs. Consistency about 95%, +17% F1 over the raw model (T5-large era).
- **Maieutic prompting** (c15, c24): GPT-3 writes abductive explanation trees ("X is true because..."), a verifier scores belief and consistency, a weighted MaxSAT picks the most coherent truth assignment.
- **ConCoRD** (d09): MaxSAT over the model's own candidates with NLI-estimated edge weights.
- **IBE-Eval** (a22, a23, b23, c01 to c05, c25): code-computed explanation features pick the better of two LLM explanations.
- **Huntsman and Thomas 2025** (c11 to c14): coherence maximisation as MAX-CUT over LLM-built proposition graphs.

Numbers for all are in sections 3 and 6.

## 3. Core findings with exact numbers

Status: [E] established, [S] single source, [C] contested. H = human study, L = LLM study.

| Finding | Numbers | Source (evidence ids) | Status |
|---|---|---|---|
| Three certainty principles: coverage and coherence govern acceptance; uniqueness governs confidence | No numbers, no weights, no formula | Hastie and Pennington 1996 (a01 to a04, b14, d01, d02) | [S] H, verbal theory; founding data unopened |
| No theory of what makes a good story; no combining rule | Commentary and the authors' own text | a08, b14, c09 | [E] (2 sources) |
| Order of evidence changes verdicts (story order versus issue order) | "About 78% vs 31%" is second-hand | Pennington and Hastie 1986/88/92 (a27, a28, b27) | Unverified; do not use |
| Coherence shift in a split-verdict case | Exp 1 F(1,44) = 35.3 (N = 48); F(2,86) = 35.3 (N = 47); F(2,236) = 59.1 (N = 120); F(2,302) = 78.6 (N = 157) | Holyoak and Simon 1999; Simon et al. 2001 (a12, a16 to a18, b01 to b04) | [E] H (2 papers, same lab) |
| Shift appears before commitment and without a decision task | Interim-to-post change p > .30; memorise and comprehend sets equal to decision set, F(4,302) < 1 | a16 to a19, b03 | [S] H |
| Rating consistency jumps with reading | Alpha -.25 to .08 baseline, .70 to .77 interim, .80 post; correlations significant 2/21 at baseline, all at post | a17, a18, b02, b03 | [S] H |
| Confidence is high on an ambiguous case | 75% to 93% moderately confident or higher with a near 50/50 split | a12, a13, a16, a17 | [S] H |
| One manipulated fact spreads to neighbouring points | Verdict 78% vs 28%, chi2(1, 64) = 16.1; motive rating 1.83 vs -2.75, t(62) = 8.98 | Holyoak and Simon 1999 Exp 3 (a15, b07) | [S] H |
| Memory of own earlier ratings drifts toward the verdict | Recalled -1.32 vs actual -0.30, p = .07, N about 19 | a14, b06 | [S] H, marginal |
| Role-induced bias via coherence shift, independent lab | 64% vs 50% (N = 149); 56% vs 40% (N = 92); indirect .31 [.19, .44]; plea 70.0 vs 18.4 | Engel and Gloeckner 2013 (a20, b09 to b11) | [S] H (different design); Exp 2 borderline |
| Large accuracy incentive does not remove it | 100 euro in 1 of 10; same-size effect | b10, d05 | [S] H |
| Shift works by devaluing conflicting evidence | Prosecution contra-guilty -125.1 vs pro-guilty +9.7 | a21, b12 | [S] H |
| Boundary: shift is transient; slow deciders less biased; about 20% switch verdict | Time x role z = -3.06, p = .002 (one study); p = .24 in Exp 2; switchers 6 of 30 | b05, b13, d04, d05 | [E] H that a boundary exists (2 sources); duration unknown |
| ECHO reproduces trial outcomes in direction | Peyer hung 7-5; Chambers clear guilt; stable under halving/doubling parameters | Thagard 1989 (a07, b17, c07, c08) | [S] model, post-hoc |
| Coherence alone and Bayes both predict O.J. guilty; acquittal needs emotion | ECHO guilt; P(killed) = .72, P(framed) = .99 | Thagard 2003 (a09 to a11, b16) | [S] model, post-hoc |
| IBE-Eval: code features pick the better explanation | Up to 77% (COPA, GPT-3.5), 27 points over chance, +17.5 over GPT-3.5 judge; Spearman with humans .64 vs .31 | Dalal et al. 2024 (a22, c01, c05) | [S] L, no replication found (d17) |
| Logical consistency alone does not discriminate | Accuracy .51 to .55 | c02, c03 | [S] L |
| Hedging and short proofs are best single predictors | Uncertainty-only up to .70; parsimony +14% over consistency | a23, c04 | [S] L |
| Human raters agree with IBE-Eval picks | 96% COPA, 91% E-CARE; kappa .68; 100 pairs, 2 raters | c05 | [S] L |
| Self-evident explanations rarely game parsimony | 2% generated; under 0.1% of errors | c25 | [S] L |
| LLM hidden states separate coherent from incoherent stories; own ratings do not | Probe at target .80 to .96; at end .60 to .82; coherence response .59 to .77; quality-rating gap under 1 point; r = .33 | de Langis et al. 2025 (a24, b18, b19) | [S] L |
| LLMs more sensitive to setting violations than character violations; humans not | Human contrast 54.29, CI [-117.39, 225.97], n.s. | a25 | [S] L |
| LLM coherence shift after writing an essay | d = 2.16 (pro), 1.80 (anti) vs control, n = 50 per cell; choice framing d = .98 pro, .25 anti (n = 150 per cell); Claude 3.5 third-person smaller (d = .23 to .68) | Lehr et al. 2025 (b20 to b22, d15) | [S] L |
| LLM stance revision depends on source and evidence; model-dependent | Trust elasticity on clearly false claims .024 (Qwen), .169 (Grok), .264 (Llama), .113 (GPT-4o) | Qi and Lerman 2026 (d16) | [S] L, health claims |
| Coherence maximisation as MAX-CUT is feasible; depends on density and model | 76 graphs; density F = 369.50; o-series perfect reconstruction about half the time on sparse graphs | Huntsman and Thomas 2025 (c11, c12) | [S] L, synthetic |
| Solver over model beliefs raises accuracy | BeliefBank +17% F1, consistency about 95%; Maieutic 72.5 vs 61.6 (CoT) on Com2Sense; ConCoRD +8.1 F1; self-consistency +17.9 on GSM8K | c15, c16, c18, d09 | [E] L (4 sources; small/old models; only SC compared to a plain vote) |
| Cross-model agreement beats same-model vote and self-verifier | AIME-24 56.7 vs 36.7 vs 30.0; MATH-500 96.6 vs 95.2 vs 93.2; GPQA 35.9 vs 33.3 vs 26.3 (gain not significant) | Liu 2026 (d06) | [S] L preprint |
| Agreement predicts correctness better than stated confidence | GPT-4 verbalized AUROC 62.7% average; GSM8K 54.8% vs 92.7% with 5 samples; unanimous 4-model panel 99.5% on MATH-500 at 85% coverage | Xiong 2024; Liu 2026; Wang 2022 (d10, d07, d11) | [E] L (3 sources) |
| Free-form selection by an LLM works when voting cannot | TruthfulQA 62.1 to 67.7 (PaLM 2-L); 79.8 to 82.5 (gpt-3.5); GSM8K 90.2 vs 90.4 | Chen et al. 2023, USC (d08) | [S] L |
| Self-correction without an outside signal hurts | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0; with oracle 97.5 | Huang et al. 2024 (d14) | [E] L (also schema 4b) |
| LLM judges are gameable by form | Swap consistency 23.8% Claude-v1, 46.2% GPT-3.5, 65.0% GPT-4; padded answer wins 91.3% (weak judges) vs 8.7% (GPT-4), 23 cases | Zheng et al. 2023 (d12, d13) | [S] L, 2023 models |
| Multi-agent LLM juries rarely converge | 17 of 18 hung (N = 3 per cell); 20 LLM jurors, 432K decisions, non-reversal 70 to 80%; persona moved severity more than statement | Ersoz 2026; Wu 2026 (a26, c20, b24, b25) | [E] L (2 preprints, exploratory) |

## 4. Mechanisms and models

Each model below is described so an engineer can write it. None is validated as a combined rule (K02), so treat every formula as an experiment, not a fact.

### 4.1 Constraint-satisfaction coherence (Holyoak and Simon; ECHO)

State: a set of units, one per proposition (evidence items, hypotheses, sub-claims). Links: symmetric weights. Positive for "explains" or "supports", negative for "contradicts" or "competes with". Evidence units are clamped with a small positive input from a special "evidence" unit.

Update loop (ECHO defaults, a06):
```
for each unit j:
  net_j = sum_i w_ij * a_i            # w from explanation (+0.05..0.1), contradiction (-0.2)
  if net_j > 0: a_j = a_j*(1-d) + net_j*(max - a_j)
  else:         a_j = a_j*(1-d) + net_j*(a_j - min)
repeat until the largest change is under a threshold; accept units with a > 0.
```
d is about .05, max = 1, min = -1. Properties that matter: bidirectional influence (the hypothesis lifts its evidence and the evidence lifts the hypothesis), winner-take-all between rival sets (this explains the high confidence in a split case, a13), and spread (one clamped fact moves distant units, a15). The bidirectional link is why human ratings drift: "evidence" is not fixed, it is re-valued by what the network leans toward.

Implementation note: the dangerous part is the bidirectional edge. In code we can build the same network but clamp the evidence ratings made earlier (see 4.4). We do not need the dynamics for anything except a settle step over claims.

### 4.2 Coherence as MAX-CUT or MAX-SAT (Thagard; Huntsman; BeliefBank; ConCoRD)

Write the problem as: propositions P1..Pn with signed weights w_ij (positive = cohere, negative = contradict). Find the accept/reject split that maximises the sum of satisfied weights. This is MAX-CUT on the negated weight matrix (c11). For n up to about 25 this is brute-forceable or solvable with a small solver.

Pipeline (c13, d09):
1. Extract atomic claims from k sampled answers (LLM call, fixed template).
2. Weight each pair (LLM or NLI call: entails, contradicts, unrelated). Take the median weight over repeated runs because LLM edge weights vary run to run (c14).
3. Solve the split in code.
4. Accept the answer whose claims land in the accept set; the margin between the best and runner-up partitions is the uniqueness signal.

Known weaknesses: reconstruction fidelity falls with graph density and depends on the model (density F = 369.5, c12); near-optimal alternative partitions exist (c14), which is itself a uniqueness measure; ConCoRD showed noisy NLI weights still help small models and even beat gold constraints on BeliefBank (d09), but no study compares it with plain voting or runs it on a frontier model (K24).

### 4.3 The certainty principles as code scores

A concrete, testable design (our own; nothing in the literature validates it):

| Principle | Code score | Needs |
|---|---|---|
| Coverage | covered / total, where total is a fixed list of evidence items extracted from the task once, and covered is the count of items an entailment check says the candidate's account uses or explains | A fixed list, built before candidates are seen |
| Consistency | number of contradiction pairs among the candidate's own claims and against the fixed evidence list (NLI or LLM edge call, median of 3) | Pair checks |
| Completeness | empty slots in a fixed template for the task class (cause, mechanism, conditions, consequence) | A template per class |
| Plausibility | the class prior from S0 or a retrieved-fact check | Prior data; no validated source |
| Uniqueness | gap between best and runner-up total score; or vote margin across independent samples | k fresh samples |

Combine by a lexicographic or weighted rule and ablate each term (K02). Use uniqueness only to decide what to do next (abstain, escalate to S6, spend more samples), not to choose between candidates: this is how the story model itself uses it (a03, a04).

### 4.4 Remedies that follow from the coherence shift

The shift implies three mechanical rules for an agent:
1. **Freeze first ratings.** Rate each evidence item (or sub-claim) before any hypothesis exists, store the rating in code, and never show the model its own earlier rating as editable. Human memory of earlier ratings drifts toward the final verdict (b06), and an LLM shows a shift of d = 1.8 to 2.2 after writing text for one side (b20). External storage as a fix is untested (d15, K26).
2. **Do not re-rate after choosing.** Ratings made after the model has leaned or written an answer are contaminated. If a re-rating is needed, use a fresh context that shows no draft answer (fits S3's fresh-context rule).
3. **Re-read the conflicting evidence.** In humans the shift is mostly devaluing the evidence that disagrees with the leaning side (-125.1 vs +9.7, a21). A forced restatement of the strongest counter-evidence is a candidate remedy; untested (K08).

### 4.5 IBE-Eval (code-computed explanation features)

Steps (a22, c01): 1. For each answer option, have the LLM write an explanation. 2. Convert the explanation to a proof graph and check logical consistency with a Prolog solver. 3. Parsimony: proof depth and concept drift (new concepts not in the question). 4. Coherence: mean step-wise entailment score. 5. Uncertainty: count of epistemic hedges. 6. A linear model over the features picks the option. In the data, consistency alone was at chance (.51 to .55) because models write consistent explanations for wrong answers (c03). Depth .67, drift .67, coherence .66 and hedges .70 were each above chance; composed .77 (c02). Hedges were the strongest single cue (c04). The risk: hedge counts are a surface cue that prompting could change. Models and tasks were GPT-3.5 and Llama 2, on two-option causal QA only.

### 4.6 Uniqueness as agreement

If uniqueness means "the best story stands alone," the nearest validated code signal is agreement across independent samples. Verbalized confidence is weak (GPT-4 average AUROC 62.7%, GSM8K 54.8%); five-sample consistency lifts GSM8K to 92.7% (d10). A unanimous panel of four independent models was 99.5% correct on MATH-500 at 85% coverage, and three-quarters agreement gave 98.5% at 94% coverage (d07). Two limits: single-model samples are correlated (G4), and on science and knowledge sets unanimity saturated at 0.769 because of shared errors (d07). A runner-up gap over generated stories was not itself tested.

## 5. What holds up

**Holds up (human).**
- The coherence shift itself replicated across Holyoak and Simon 1999 and three experiments in Simon et al. 2001, with a large effect (F values 35 to 79 at N = 47 to 157), and the idea was conceptually replicated by an independent lab with a different stimulus and country (Engel and Gloeckner, b09). It appears without a decision task (b03).
- Gap: nearly all the support is vignette studies with students, one case (Quest v. Smith) from one lab, switchers dropped (about 5% of participants in Simon 2001, 20% of the three-phase group in 1999), and no preregistered independent replication of the original paradigm (b08).

**Failed, weak or contested.**
- Founding story-model numbers: unverified in this run (K20, K26).
- Engel and Gloeckner Exp 2 is borderline (p = .07 one-sided; p = .028 after excluding 7). Exp 3 has N = 29.
- Memory drift for earlier ratings: p = .07, N about 19 (b06).
- Pure coherence models predicted conviction for O.J. while the jury acquitted (a09 to a11); the fix was fitted after the fact.
- The coherence-shift evidence concerns coherence. It says nothing separately about coverage or uniqueness, and no opened experiment shows uniqueness changing confidence by an amount.

**Moderators.**
- Time: slow deciders show less bias (d04, d05), but the interaction was significant in one study and not in Exp 2 (p = .24). Duration of the shift is unknown (Simon et al. 2008 unopened).
- Incentive: money did not remove the role bias (b10, d05).
- Direction: the shift is asymmetric; devaluing conflicting evidence dominates (a21).
- Task ambiguity: the shift was measured in a deliberately balanced case.

**Interventions that worked.**
- Sample agreement as a confidence signal beats stated confidence by a wide margin (d10, d07).
- Solvers over model beliefs improved consistency and accuracy on small models (c15, c16, d09).
- Cross-model agreement beat same-model voting and a self-verifier on seven closed-answer benchmarks (d06), though with extra compute and a floor on science sets.
- External signals help where self-asking does not: oracle labels lifted GPT-4 GSM8K to 97.5, while self-critique lowered it to 89.0 (d14).

**Interventions that did not work.**
- Intrinsic self-correction without an outside signal: GPT-3.5 CommonSenseQA 75.8 to 38.1 (d14).
- LLM-written logical-consistency checks alone: accuracy .51 to .55 (c03).
- Asking the model to rate coherence or quality: gap under 1 point on the rating scale between coherent and incoherent stories (b19). Reasoning mode did not fix it (rating accuracy .517 and .737 for two reasoning models).
- Multi-agent deliberation as a way to reach a coherent accepted story: 17 of 18 hung (a26).
- A large accuracy incentive on the human role bias (b10).

## 6. Language models

**How models behave on coherence tasks.**
1. **Models know more than they say.** Hidden-state probes separate coherent from incoherent stories at 0.80 to 0.96 at the incoherent sentence, falling toward chance by the end of the story for small models (0.60 to 0.82). Prompted coherence responses reach only 0.59 to 0.77 and quality ratings differ by under 1 point (Llama3.1-70B: probe .942 at target, .817 at end, response .765, quality .672; Qwen2.5-72B .958, .817, .707, .621; Llama3.1-8B .850, .667, .594, .595; a24). Models notice setting violations (rain in the desert) more than character violations (a vegetarian orders a cheeseburger), while humans show no such gap (a25). Open-weight 2024-25 models only. We cannot read hidden states from an API model, so the practical reading is: do not use a model's coherence rating as a selector (K14).
2. **Models are strong rationalisers.** They write logically consistent explanations for the wrong option as often as for the right one (consistency alone .51 to .55, c03). About 41% of sampled wrong GPT-3 cases involved explanations that did not support the model's own answer, and models could justify a statement and its negation (c24).
3. **Models show a human-like coherence shift.** GPT-4o's rating of Putin moved toward the essay it had just written: pro vs control d = 2.164, t(98) = 10.82; anti vs control d = 1.795; pro vs anti d = 3.775 (n = 50 per cell, b20). A preregistered second study (n = 150 per cell) found a larger shift when the model was given an illusion of free choice: d = 0.981 pro, 0.252 anti (b21). Claude 3.5, rating what the essay's author would think, showed smaller effects (d = .23 pro, .678 anti on leadership; b22). Caveats: one topic, one main model; the controls are other chats, not the model's own earlier rating (d15). Whether storing the first rating externally removes the shift is untested.
4. **Models revise stance according to source and evidence, differently by model.** Trust elasticity on clearly false claims .024 (Qwen), .169 (Grok), .264 (Llama), .113 (GPT-4o), health claims (d16).
5. **Models sit in early impressions and personas.** Twenty frontier LLM jurors, 12 juror profiles, 500 cases, 432K decisions: only 3 of 500 cases unanimous, mean mode-share .645, non-reversal rate about 70 to 80% after a defendant's statement; persona moved severity more than the statement; model severity-bias scores ranged from +0.55 to -0.59 (b24, b25, c19). Twelve LLM juror agents in a 12 Angry Men setting: 17 of 18 runs hung, GPT-4o 9 of 9 hung with a mean of 1.0 vote change per run, Llama-4-Scout 1 acquittal in 64 turns (a26, c20). Exploratory, N = 3 per cell, no significance tests.

**What code-computed selection did.**

| Method | Model, task | Result | Id |
|---|---|---|---|
| IBE-Eval (consistency, parsimony, coherence, hedges) | GPT-3.5, COPA | 77% vs about 59% for GPT-3.5 judge; +17.5 average | a22, c01, c02 |
| IBE-Eval vs humans | 100 pairs | Spearman .64 vs .31 | c05 |
| Maieutic prompting + MaxSAT | GPT-3, Com2Sense | 72.5 vs 61.6 CoT, 61.4 SC | c15 |
| Maieutic | CSQA 2.0; CREAK | 69.5 vs 59.6 and 60.8; 85.2 vs 64.8 and 70.5 | c15 |
| BeliefBank MaxSAT | T5-large | +17% F1, consistency about 95% | c16 |
| ConCoRD | Macaw, LXMERT | F1 +8.1, accuracy +5.0 | d09 |
| Self-consistency | PaLM-540B | GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4 | c18 |
| Cross-model consensus (12 candidates) | Qwen3-235B pool, 7 sets | AIME-24 56.7 vs 36.7 SC vs 30.0 own verifier; MATH-500 96.6 / 95.2 / 93.2; OlympiadBench 72.6 / 65.4 / 62.2 | d06 |
| USC (LLM picks most consistent) | PaLM 2-L, gpt-3.5 | TruthfulQA 62.1 to 67.7; 79.8 to 82.5; math ties vote | d08 |
| MAX-CUT reconstruction | o1/o3/o4-mini, Claude 3.5 | perfect reconstruction about half the time on sparse graphs; fidelity falls with density | c11 |

**What did not work or worked less.**
- Self-grading with no outside signal: negative (d14).
- LLM judge picks flip with order: swap consistency 23.8% Claude-v1, 46.2% GPT-3.5, 65.0% GPT-4; padding wins 91.3% for weak judges, 8.7% for GPT-4 (d12, d13). A coverage score read by an LLM may be inflated by padding with restated evidence. Code that counts items against a fixed list is safer. Current frontier judges are untested.
- Reasoning mode did not fix coherence ratings (b19).

**Not tested anywhere we found.** Whether an LLM's choice and confidence follow planted differences in story coverage, coherence and uniqueness (K19); whether IBE-Eval generalises to frontier models or open-ended tasks (d17); whether a MaxSAT/MAX-CUT acceptance step beats self-consistency voting with noisy edges on a frontier model (K24); whether stored first ratings remove the LLM coherence shift (d15). Two possibly relevant 2025 items (LLM story-model coding with ChatGPT precision 72.7%; a mock-jury replication with GPT-4o, Claude 3.5 Sonnet and o1) were seen only in snippets and could not be opened (c21, c22).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, M memory. Status: [E], [S], [C].

### Add now (established)

| # | Item | Part | Status and evidence | Ids |
|---|---|---|---|---|
| A1 | **Treat agreement margin as the uniqueness signal and use it only to decide what to do next** (abstain, escalate to S6, draw more samples), not as a justification. Do not use the model's stated confidence for this. Log vote margin per item (S9). | S7, S8, S0 | [E] agreement beats stated confidence (3 sources: GPT-4 AUROC 62.7% average; GSM8K 54.8% vs 92.7%; unanimous panel 99.5%) | d10, d11, d07; K22 |
| A2 | **No self-rated coherence, quality or confidence as a selector.** Selection scores come from code, or from a judge that sees no authorship and no stated answer. | G5 (already present); reinforce | [E] | d14, b19, a24; K14, K21 |
| A3 | **Do not use a consensus or debate stage to settle the answer.** LLM jurors hang or hold their starting vote. | G9 (already present) | [E] | a26, c20, b24; K18 |
| A4 | **Where code can compute a selection signal from independent runs, prefer it to model self-verification** (cross-model agreement, test results). Note the shared-error floor: when models share errors, a code score cannot recover. | G5, S7 | [E] (d06 and d14 here; test-based verifiers in other subfields) | d06, d14; K21 |
| A5 | **Coherence shift as a hazard: do not let the model re-rate the evidence after it has drafted or leaned.** Rate evidence items before hypotheses exist, in a separate context, and keep the rating in code. | G (sub-rule to G2/G3); S2 | [E] for the human effect (K03: two papers plus an independent lab); the LLM effect is [S] | a12, a16 to a18, b04, b09, b20; K03 |

A5 is the one new item for the schema text. Its human basis is established, its LLM remedy is not. As written it only restricts and adds no model call (ratings are made once). Schema section 8 requires an equal-token test before it enters SCHEMA.md; see U4 in UNKNOWNS.md.

### Test first (single source, contested, or unvalidated)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Coverage, consistency and uniqueness scores computed in code against a fixed evidence list, as a tie-break or selector in S7 | S7, O | [S] (formula is ours, K02) | a01 to a04, K01, K02 |
| T2 | IBE-style surface features (hedge density, step count, concept drift) as tie-breakers among candidate explanations | S7 | [S] (one paper, 2 models, 2-option tasks) | a22, a23, c04, K12, K13 |
| T3 | MaxSAT / MAX-CUT over claims extracted from k samples, with median-of-3 LLM edge weights, as an acceptance step | S7 | [S] vs vote; [E] that solvers help small models | c11 to c16, d09, K16, K17, K24 |
| T4 | Frozen first ratings plus a fresh-context re-rating, measuring drift | G, S2 | [S] LLM | b20, b21, d15, K15, K26 |
| T5 | Role reset: after an advocate role (S3 attempt), a neutral re-read of the original task before S7 | S3, S7 | [S] (human only) | b09, b10, K07 |
| T6 | Restate the strongest counter-evidence before the final answer | S8 | [S] (mechanism from human data only) | a21, b12, K08 |
| T7 | Runner-up gap over generated stories as an escalation trigger at S6 | S6, S7 | [S] (agreement works; gap over stories untested) | d07, d10, K22 |
| T8 | Padding attack on the coverage score: does restated evidence inflate the LLM-read score but not the code count | G5 | [S] 2023 models | d12, d13, K25 |
| T9 | Planted-story test: vary coverage, coherence and uniqueness in stories shown to the model; do choice and confidence move as the model predicts | none yet | open | K19 |
| T10 | Premise-flip spread: change one fact and count how many neighbouring sub-judgments the model shifts | O (propagate consequences) | [S] human | a15, b07, K06 |
| T11 | Slow versus fast deliberation at equal tokens | S3, S5 | [C] human, interaction not always significant | d04, d05, K09 |
| T12 | Cross-model second opinion in S7 where several models are available | S7 | [S] preprint | d06, K21 |

## 8. Concrete tests on our bench

All arms at equal tokens (setup cost counted, G7). Expected effects are guesses informed by the numbers above, not predictions from the literature.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 | Closed-answer items with a check (math, ARC-style, BrainTeaser), 200 items | (a) plain model, (b) majority vote of k, (c) vote plus code uniqueness margin used to abstain or escalate | AUROC of margin vs stated confidence for correctness; accuracy at 85% coverage | Margin AUROC far above stated confidence (literature 92.7% vs 54.8%); accuracy at 85% coverage above full-coverage accuracy |
| B2 | Open-ended explanation items with blind grading | (a) plain, (b) USC-style LLM pick, (c) code score = coverage minus contradictions against a fixed evidence list, (d) c plus hedge/step features | Blind-graded quality; pick vs best available | (c) or (d) match USC at lower cost; +3 to +8 points if code features carry signal; none if not |
| B3 | Two-option causal items (COPA/E-CARE style) | (a) plain, (b) LLM judge, (c) IBE features in code | Accuracy | A frontier model may leave little headroom; look for any gain over vote |
| B4 | Items with extracted claims, k = 5 samples | (a) majority vote, (b) MaxSAT over claims with median-of-3 NLI weights, (c) LLM judge | Accuracy at equal tokens | Gain over vote only where answers are long and partly overlapping; none on single-token answers |
| B5 | Evidence-rating items (rate 6 disputed arguments, then choose) | (a) rate after drafting an answer, (b) rate first in a fresh context, frozen in code | Drift (post minus pre rating, toward chosen answer); accuracy of final choice | (a) shows drift in the d = 1 to 2 range (Lehr); (b) near zero by construction; accuracy gain small unless drift flips answers |
| B6 | Role items (advocate then neutral prediction) | (a) no reset, (b) neutral fresh re-read, (c) two-sided briefing | Bias gap between roles (analogue of 64% vs 50%) | Gap drops in (b) and (c) if the LLM has human-like role bias |
| B7 | Items with planted counter-evidence | (a) plain, (b) forced restatement of strongest counter-evidence, same total tokens | Weight kept on counter-evidence; final accuracy | Better retained counter-evidence; accuracy effect uncertain |
| B8 | Padding attack | Candidate story with restated evidence vs original | Change of LLM-read score vs code count | LLM score inflates on weaker judges; code count unchanged |
| B9 | Planted-story items (coverage 40/70/100%, contradictions 0/2/4, rival strength weak/equal) | Plain model; model with S7 code score | Choice and stated confidence vs plan | Choice follows coverage and contradiction counts; confidence drops with equal rivals if the model mimics uniqueness |
| B10 | Items with two near-equal stories | Vote margin vs runner-up score gap as escalation trigger at S6 | AUROC for correctness; tokens saved | Margin and gap correlate; gap adds little over margin |

## 9. What does not transfer, and why

- **Juror psychology and social effects** (group pressure, legitimacy, burden of proof, persuasion) are institutional. The Engel and Gloeckner role manipulation is a human motivated-reasoning effect; an LLM has no stake, so an LLM role bias, if present, comes from persona text, not incentive (Wu: persona moved severity more than the statement, b25).
- **Student vignette data** (one case, one lab, rating scales, switchers dropped) gives effect sizes that will not carry to API models. Treat F values as proof that the process exists, not as sizes for our agent.
- **Thagard's networks** need hand-coded links and hand-set valences and were fitted after the verdict (a09, b16). The method transfers; the numbers do not.
- **IBE-Eval numbers** come from GPT-3.5 and Llama 2 on two-option causal QA. A frontier model may produce fewer hedged wrong explanations; the hedge cue may vanish or flip (K13).
- **Story coverage as defined for juries** means an account of trial facts. For problems with a verifiable answer, a check beats any coverage score. Coverage, coherence and uniqueness belong to open or no-check problems (G6 and the no-check route in the schema).
- **Hidden-state probes** (de Langis) need white-box access; with an API model only the output-level result transfers.
- **The "transient" boundary** may not apply to an LLM: the context is rebuilt each call, so a shift persists only as long as the context carries the drafted text.
- **Uniqueness in the human sense** (entertaining alternatives) has no analogue in a single sample; our analogue is the sample-agreement margin, which is a different quantity and is correlated across samples from one model (G4).

## 10. Open questions

1. What exactly do Pennington and Hastie 1986, 1988 and 1992 report: order effects, confidence by uniqueness, verdict shares? (a27, a28, b27, K20)
2. Does an LLM's choice and confidence follow planted differences in coverage, coherence and uniqueness? (K19)
3. Does a code score (coverage minus contradictions, uniqueness gap) beat vote and an LLM picker at equal tokens on a frontier model and on open-ended tasks? (K21, K23)
4. Does IBE-Eval generalise past COPA and E-CARE, past GPT-3.5 and Llama 2? Is the hedging cue stable on current models? (d17, K12)
5. How large is the coherence shift in current frontier models on case-evidence ratings, and does external storage of the first rating remove it? (d15, K15)
6. Does MAX-SAT acceptance over extracted claims beat voting given noisy edges and a frontier model? (K24)
7. How long does the human shift last, and is slowness a real moderator? Simon et al. 2008 is unopened. (K09)
8. What do the story-model LLM-coding study (precision 72.7%) and the GPT-4o/Claude mock-jury replication report? (c21, c22)
9. Can adversarial or self-evident stories game coverage or parsimony scores in current pipelines? (K25, c25)
10. Should the combining rule for coverage, coherence and uniqueness be lexicographic, additive, or learned from our logs? No source says. (K02)
11. Do coverage and coherence matter separately? No opened experiment separates them.

## 11. Sources

[V] opened and read in this run (pdftotext or HTML). [M] snippet or abstract only, not read.

1. [V] Hastie and Pennington (1996), The O.J. Simpson stories: behavioral scientists' reflections, U Colorado Law Review 67. https://lawreview.colorado.edu/wp-content/uploads/2026/02/Hastie-Pennington.pdf (a01 to a04, b14, b15, d02)
2. [V] Hastie and Pennington (c.1993-94), Implications of the Story Model for the trial judge. https://ciaj-icaj.ca/wp-content/uploads/documents/import/1993/HASTIE.ED.pdf?id=1503 (d01)
3. [V] Thagard (1989), Explanatory coherence, Behavioral and Brain Sciences 12:435. https://doi.org/10.1017/S0140525X00057046 and https://www.gwern.net/doc/philosophy/epistemology/1989-thagard.pdf (a05 to a08, b17, c06 to c10)
4. [V] Thagard (2003), Why wasn't O.J. convicted? Emotional coherence in legal inference. https://arts.uwaterloo.ca/~pthagard/Articles/OJ.pdf (a09 to a11, b16)
5. [V] Holyoak and Simon (1999), Bidirectional reasoning in decision making by constraint satisfaction, JEP:General 128:3. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/HolyoakSimon.99.pdf (a12 to a15, b04 to b07)
6. [V] Simon, Pham, Le and Holyoak (2001), The emergence of coherence over the course of decision making. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/Simon_etal.2004.pdf (a16 to a19, b01 to b03)
7. [V] Simon and Holyoak (2002), Structural dynamics of cognition. https://reasoninglab.psych.ucla.edu/wp-content/uploads/sites/273/2021/04/SimonHolyoak_2002.pdf (a30, b08; legal section only)
8. [V] Engel and Gloeckner (2013), Role-induced bias in court, J Behav Decis Making 26:272. https://doi.org/10.1002/bdm.1761 and https://ius.uzh.ch/dam/jcr:63d46323-c34c-4fee-a24e-a06e858a3de5/Engel_and_Glockner_2014__Role_Induced_Bias_in_Court.pdf (a20, a21, b09 to b13, d04, d05)
9. [V] Dalal, Valentino, Freitas and Buitelaar (2024), Inference to the Best Explanation in Large Language Models (IBE-Eval), ACL 2024. https://arxiv.org/abs/2402.10767 and https://aclanthology.org/2024.acl-long.14.pdf (a22, a23, b23, c01 to c05, c25, d17)
10. [V] de Langis et al. (2025), Mary, the Cheeseburger-Eating Vegetarian. https://arxiv.org/abs/2512.07777 (a24, a25, b18, b19)
11. [V] Lehr, Saichandran, Harmon-Jones et al. (2025), Kernels of selfhood. https://arxiv.org/abs/2502.07088 (b20 to b22, d15)
12. [V] Qi and Lerman (2026), Confident but Conflicted. https://arxiv.org/abs/2606.22633 (d16)
13. [V] Ersoz (2026), 12 Angry AI Agents. https://arxiv.org/abs/2605.01986 (a26, c20)
14. [V] Wu (2026), When does defendant statement matter? (JuryBench). https://arxiv.org/abs/2609.09887 (b24, b25, c19)
15. [V] Huntsman and Thomas (2025), Benchmarking graph construction by LLMs for coherence-driven inference. https://arxiv.org/abs/2502.13953 (c11, c12)
16. [V] Huntsman (2025), Automatic coherence-driven inference on arguments. https://arxiv.org/abs/2509.18523 (c13, c14)
17. [V] Jung et al. (2022), Maieutic Prompting. https://arxiv.org/abs/2205.11822 (c15, c24)
18. [V] Kassner et al. (2021), BeliefBank. https://arxiv.org/abs/2109.14723 (c16)
19. [V] Tafjord et al. (2022), Entailer. https://arxiv.org/abs/2210.12217 (c17)
20. [V] Wang et al. (2022), Self-Consistency Improves Chain of Thought Reasoning. https://arxiv.org/abs/2203.11171 (c18, d11)
21. [V] Mitchell et al. (2022), ConCoRD. https://arxiv.org/abs/2211.11875 (d09)
22. [V] Liu (2026), LLMs as a Jury: cross-model consensus. https://arxiv.org/abs/2607.10139 (d06, d07)
23. [V] Chen et al. (2023), Universal Self-Consistency. https://arxiv.org/abs/2311.17311 (d08)
24. [V] Xiong et al. (2024), Can LLMs express their uncertainty? https://arxiv.org/abs/2306.13063 (d10)
25. [V] Zheng et al. (2023), Judging LLM-as-a-Judge with MT-Bench. https://arxiv.org/abs/2306.05685 (d12, d13)
26. [V] Huang et al. (2024), Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (d14)
27. [M] Pennington and Hastie (1992), Explaining the evidence: tests of the story model, JPSP 62:189. https://doi.org/10.1037/0022-3514.62.2.189 (a27, b27)
28. [M] Pennington and Hastie (1988), Explanation-based decision making, JEP:LMC 14:521. https://doi.org/10.1037/0278-7393.14.3.521 (a28)
29. [M] Pennington and Hastie (1986) JPSP 51:242 and (1993) Cognition 49:123. https://doi.org/10.1016/0010-0277(93)90038-W (a29, d03)
30. [M] Simon (2004), A third view of the black box, U Chicago Law Review 71. https://chicagounbound.uchicago.edu/uclrev/vol71/iss2/3 (b26; abstract only)
31. [M] Simon, Krawczyk et al. (2008), transience of coherence shifts (cited in Engel and Gloeckner; not opened). (b13, d04)
32. [M] LLM story-model coding study (Univ. Turku repository). https://www.utupub.fi/bitstreams/41dd9017-bbc2-4c89-9bd2-de03c4803325/download (c21)
33. [M] Mock jury replication with GPT-4o, Claude 3.5 Sonnet and o1, Law and Human Behavior 2025 (c22; no URL)
