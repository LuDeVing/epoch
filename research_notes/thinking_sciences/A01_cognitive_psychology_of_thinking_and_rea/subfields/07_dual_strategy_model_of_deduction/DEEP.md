# Dual-strategy model of deduction: deep document

Scope: the claim that people judge deductive validity in one of two ways. One way searches for a counterexample (mental-model style). The other estimates how likely the conclusion is (probability-heuristic style). This file covers the human evidence, the formal models, the language-model evidence, and what our single-agent scaffold (SCHEMA 0.2) should take from it.

Evidence ids (a01 to d23) point to the lines in evidence_a.jsonl to evidence_d.jsonl in this folder. Claim ids (A01.07-K01 to A01.07-K26) point to claims.jsonl. Overlap with the earlier deep documents (mental models, Wason, content effects, belief bias, dual process) is referred to, not repeated.

Honest framing up front. Almost all human evidence comes from one research network (Markovits and collaborators) and one instrument. No independent replication of the diagnostic was found (d23, A01.07-K26). Treat effect sizes as upper bounds. No study has run the diagnostic on a language model (c30, A01.07-K17).

---

## 1. What it is

**The idea.** Two ways to answer "does this conclusion follow?"

- **Counterexample strategy.** Look for a case where the premises are true and the conclusion is false. If one is found, reject. This is the mental-models route. It is slow and costs working memory.
- **Statistical strategy.** Judge how probable the conclusion is, using stored knowledge and stated odds. Accept if it is likely enough. This is the probability-heuristics route. It is fast and cheap.

**Where it started.** Verschueren, Schaeken and d'Ydewalle (2005) asked people to think aloud on everyday if-then problems. Both kinds of reasoning appeared in the same people. People with more working memory used more counterexamples (a01, a24). Markovits and colleagues then built a short test that sorts people by their response pattern (a02, b04).

**The diagnostic.** Abstract "affirmation of the consequent" (AC) items on an invented planet. Form: If P then Q. Q is true. Is P true? Each item states how often Q occurred without P in 1,000 observations (a02, b04, a26).

- 13 items in the original: 5 with about 10% alternative antecedents (the "90%" items, 90% P-and-Q), 5 with about 50%, 3 at 0%.
- The newer 10-item scoring uses R90 and R50, the count of rejections out of 5 in each set.
- Counterexample type: rejects everything (R90 + R50 = 10).
- Statistical type: rejects the 50% items more than the 90% items (R50 > R90 + 1).
- Intermediate: rejects four of the five 90% items.
- Other: anything else. Probably people who switch or misread the task (a06, b19).

A counterexample reasoner ignores the stated odds, because any exception kills validity. A statistical reasoner follows the odds. That is the whole logic of the test.

**The shares.** Roughly a third each of counterexample and statistical, about a quarter unclassifiable. They vary by sample: statistical 28% (n=107 students, 2015), 45% (n=139 adults, 2020), 37% (n=2,122 Prolific, 2021) (b04, b06, b19, A01.07-K01).

**Formal specifications.** Beeson, Stupple, Schofield and Staples (2019) is a theory review, not a data paper. It proposes Mental Models Theory as the counterexample strategy and the Probability Heuristics Model (PHM, Chater and Oaksford 1999) as the statistical one (a14, b22). It adds no new experiments. Its proposals are untested.

**Why it matters for us.** SCHEMA part S2 asks "which strategy for which item class". This subfield answers: the choice is set by the question wording, the time or token budget, and the reasoner's habit. It is not set by logic alone. A scaffold must choose on purpose.

---

## 2. History and theories in depth

### 2.1 Roots, 1999 to 2007

- **Chater and Oaksford (1999), PHM** (a16, a17, a18). Quantified statements are ordered by informativeness (All > Most > Few > Some > None-type). Three generation heuristics and one test heuristic produce an answer fast without computing validity.
- **Geiger and Oberauer (2007)** (a13). The probabilistic side of conditional reasoning. Belief in an if-then rule and willingness to infer from it track how often exceptions occur, not how many kinds of disabling condition exist. Disabler count matters only when no frequency is given.
- **Verschueren, Schaeken and d'Ydewalle (2005)** (a01, a24). Think-aloud study. Both strategies appear. Working memory predicts which.

### 2.2 The diagnostic era, 2010 to 2017

- **Markovits, Lortie Forgues and Brunet (2010)** (a12, b17). Response format matters. A scaled certainty rating tracks exception frequency. A yes/no "follows logically" answer shows a different profile: any exception rejects. This is the first hint that format selects the mode.
- **Markovits, Lortie Forgues and Brunet (2012)** (d06, a26, b29). The original diagnostic paper. Individual response patterns across a block show two distinct strategies. The counterexample pattern goes with higher abstract-reasoning scores. A block and a pattern rule are needed. One answer is not diagnostic.
- **Markovits, Brunet, Thompson and Brisson (2013)** (d01, a25, b05). Direct evidence that the strategies are open to the same person. Time pressure pushes toward statistical. Free time pushes toward counterexample. Confidence in the fast strategy predicts switching. Only the abstract was opened. Samples, time limits and percentages are unknown.
- **Markovits, Brisson and de Chantal (2015)** (a10, b01 to b04). Same stated odds, two questions. On validity, strategy changes how people react to new evidence. On probability, groups answer alike.
- **Markovits, Brisson, de Chantal and Thompson (2017), belief bias** (a07, b09, b10). Statistical reasoners show a larger belief effect.
- **Markovits, Brisson and de Chantal (2017), logic versus information processing** (d05). Tests whether counterexample reasoners are just "more logical". They are not. On modus ponens with explicit premise strength, statistical reasoners accept more. With many disabling conditions, the pattern reverses. So the strategies are processing styles.

### 2.3 Consolidation, 2018 to 2024

- **Brisson and Markovits (2020)** (a11, b14 to b16). Both groups retrieve the same stored alternatives. They differ in how they turn them into a yes/no.
- **de Chantal, Newman, Thompson and Markovits (2020)** (a08, b06 to b08). Strategy beats working memory as a predictor of belief resistance. Eye tracking adds a process signature.
- **Markovits et al. (2021)** (a09, b11 to b13). Strategy predicts accuracy under 3.5 to 5 s deadlines. Working memory does not.
- **Thompson and Markovits (2021)** (d04, a27). Four studies, about 200 each. Strategy predicts belief bias, base-rate neglect and denominator neglect beyond IQ, reflection and numeracy. Not the conjunction fallacy.
- **Gagnon-St-Pierre, Doucerain and Markovits (2021)** (d12). Strategy predicts social bias.
- **Gratton and Markovits (2021)** (a20, b18, b19). N=2,122. A disconfirming statement lowers belief more for counterexample reasoners.
- **Beghin and Markovits (2022)** (a19, b20). Contingency learning. Small effects.
- **Markovits and Thompson (2023)** (d02, a05, a28). Instruction to reason by counterexample or by probability. N=885 over two studies. Only the abstract and the review account were opened.
- **Markovits (2024) review, "Are There Two Kinds of Reasoners?"** (a02 to a06, d03). The main secondary source. Written by the model's author, so it may present the model favourably.

### 2.4 Challenges, 2019 to 2026

- **Knauff and Gazzo Castaneda (2025)** (a21, b25, b26). Free-text answers show counterexample-based uncertainty more often than probability words. They call the scale effect "probabilistic masking".
- **Kosourikhina and Handley (2025)** (a22). Under speed, invalid AC and DA syllogisms are endorsed nearly as often as valid ones. Fast mode is not counterexample search.
- **Newman, Gibb and Thompson (2017)** (d07). Fast answers already carry rule and probability information. Slow answers add belief. A near-independent deadline study (Thompson overlaps).
- **Markovits, Thompson and Bergeron (2026); Markovits, Bergeron and Gagnon-St-Pierre (2026); Mekik, Vivier and Markovits (2026)** (d09, d13). Fast judgments follow semantic availability: how many alternatives come to mind. This competes with De Neys (2023, a formal-validity intuition) and Ghasemi et al. (2022, a matching account). Not opened beyond abstracts.
- **Markovits (2025)** (d10). About 15% of people respond logically at 5 s on semi-abstract items.
- **Markovits, Bergeron and Gagnon-St-Pierre (2026)** (d08). More time is not simply more logic.

### 2.5 The theory split in one paragraph

Beeson et al. (2019) say the pair "MMT plus PHM" explains more than either alone. PHM has trouble with "no valid conclusion" answers (Hattori 2016, cited in a14, a15). A counterexample strategy predicts them. Beeson et al. also point out that PHM may describe "a possible strategy rather than a fundamental reasoning mechanism" (a15), which is the same move the dual-strategy model makes. Selection between the two is proposed to be a meta-reasoning decision that picks the least demanding strategy (Beilock and DeCaro 2007; Roberts 2000 argued people switch between tasks or trials) (b21). None of this is tested.

---

## 3. Core findings with exact numbers

Status key: replicated-in-lab means several studies from the Markovits network; single means one paper; second-hand means only a review or citing paper was read; contested means evidence points both ways.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Both strategies appear in think-aloud answers; counterexample is most common | N=54 (18 per span group, from pool of 292). 1,728 answers: counterexample 52.6%, bare acceptance 25.8%, likelihood 9.8% (F(2,50)=167.33). Counterexample share low/medium/high span .472/.543/.563 (linear F(1,51)=4.60). Likelihood .143/.084/.067 (F(1,51)=8.01). Span-by-type interaction only p=.055 | a01 (Verschueren 2005) | single; small N |
| Sample shares of types | 53 CE/30 stat/24 other of 107 (2015). 43 CE/62 stat/34 other of 139 (45% stat, 2020). 768 CE (36.2%) / 794 stat (37.4%) / 560 other (26.4%) of 2,122 (2021) | b04, b06, b19 | replicated-in-lab; share is sample dependent |
| Strategy shows on validity questions, not probability questions | Validity: after evidence update CE 1.51 to 0.13, stat 1.50 to 0.97 (of 2); interaction F(1,74)=15.29, eta2p=.171, N=107. Probability: CE .789 to .775, stat .763 to .762, no strategy effect, N=86 | a10, b01, b02 (Markovits 2015) | replicated (Brisson 2020 Study 3, N=157) |
| Strategy only matters on uncertain forms | Invalid conclusions endorsed (of 3): CE 0.99, stat 1.55; validity x strategy F(1,77)=10.5, eta2p=.118; alternatives effect F(1,77)=16.42, eta2p=.176; N=104. No effect on MP/MT | a11, b14 (Brisson 2020) | replicated in Study 2 (N=212) |
| Under probability instructions the gap vanishes | N=157. Likelihood AC 61.2 vs 58.0, DA 69.9 vs 64.5. Valid 83.5 vs invalid 61.8. Validity x strategy F(1,115)=1.45, p=.23 | a11, b16 | single (earlier studies had shown an interaction) |
| Response format alone changes processing | Categorical n=70 vs scaled n=68. Accept MP+MT with 0 exceptions 87.1%, with 10% exceptions 38.6% and 34.3%, with 50% exceptions 32.1% and 28.6%. Scaled ratings: frequency effect F(1,66)=23.63 | a12, b17 (Markovits 2010) | replicated by Geiger and Oberauer (a13) on the scaled side |
| Exception frequency, not disabler count, drives scaled ratings | Exp 1 N=27: frequency on conditional F(1,26)=23.1, eta2p=.47; on MP F(1,26)=34.0, eta2p=.50; disabler number no effect. Exp 3, no frequency: disablers F(1,19)=35.2, eta2p=.63 | a13 (Geiger and Oberauer 2007) | single paper; one effect did not replicate between Exp 1 and 2 |
| Task order primes strategy | N=92. Updated acceptance 0.96 after probability items vs 0.53 after validity items first. Order x inference F(1,89)=4.45, eta2p=.048. Probability ratings unchanged | b03 | single; small effect |
| Belief bias is larger for statistical reasoners | Study 1 invalid forms, 170 classified (87 CE, 83 stat; plus 61 other). Belief effect (of 4): stat 2.47 (d=1.66), CE 1.47 (d=1.04). Interaction F(1,168)=19.92, eta2p=.106. Study 2 valid MT N=189: stat 1.38 (d=.80), CE 0.25 (ns); CE slower 24.81 s vs 19.92 s. Study 3 "Most" N=121: stat 1.96, CE 1.21; F(1,99)=7.23, eta2p=.068 | a07, b09, b10 (Markovits 2017) | replicated across 3 studies, one lab |
| Strategy beats working memory for belief resistance | Study 1 N=139 (66 analysed): conflict correct CE .76 vs stat .32; strategy x type F(1,64)=19.90, eta2p=.237. Strategy beta -.42 (p<.001); WM beta -.21 (p=.07); total 27.7% of variance; WM alone 10.9%, strategy alone 23.7%. Statistical faster 6.36 s vs 8.84 s. Study 2 N=196 (113 classified): conflict d=1.0, premise fixation d=.57 | a08, b07, b08 (de Chantal 2020) | single; only 47.5% of sample analysed in Study 1 |
| Strategy predicts fast logic at 3.5 to 5 s | N=206. Non-sequitur rejection: stat .60 vs CE .84 (F(1,143)=21.67, eta2p=.132). At 3.5 s stat .503 (chance), CE .76. At 5 s CE .92, stat .66. AC correct rejection CE .59 vs stat .31 | a09, b11 (Markovits 2021 Study 1) | single; online |
| Under 4 s limit, WM stops predicting; strategy does not | N=291 (149 at 4 s, 142 unlimited; 15.2% of 4 s trials unanswered). 4 s: strategy predicts AC (b=.32, p<.001), non-sequiturs (b=.07, p=.046); WM t<1. Unlimited: both predict. R2 33.6% and 42.6% | a09, b12 | single; null WM effect |
| Strategy predicts fast belief-conflict beyond IQ | N=150 (43 CE, 56 stat, 51 other). Conflict correct .27 (vs .51 unlimited); strategy-Raven r(99)=.33. R2=18.8%; only strategy significant (b=.23, p<.0001) | b13 | single |
| Time pressure shifts toward statistical; free time shifts back | Direction confirmed in the 2013 abstract; Ns, limits and percentages unopened | d01, a04, a25, b05, d03 | second-hand (abstract and review); [S] |
| Strategy steerable by instruction | N=885 over two studies. Following limited by spontaneous strategy. Statistical reasoners changed most; CE changed little. Effect carried to next task (belief bias; base rates) | d02, a05, d03 (Markovits and Thompson 2023) | second-hand; no per-study numbers |
| Strategy adds to IQ, reflection, numeracy in 3 of 4 tasks | 4 studies, about 200 each. Belief bias, base rate, denominator neglect yes. Conjunction fallacy no | d04 (Thompson and Markovits 2021) | single; abstract only |
| Single disconfirmation hits CE reasoners harder | N=2,122. After one disconfirming statement belief CE 0.14 vs stat 1.75 (scale -7 to +7). Repetition: CE 3.81 vs stat 4.25, ns. Interaction F(1,1290)=5.57, eta2p=.004 | a20, b18 | single; tiny interaction |
| Causal strength ratings differ by strategy, small | Study 1 N=200: F(1,124)=4.61, eta2p=.036 (stat 48.2 vs CE 40.8). Study 2 N=452: F(1,298)=11.84, eta2p=.038, Bayes factor 20.37 | a19, b20 | single; small |
| Free text shows counterexample-based doubt | Exp 1 N=20: certain 29.6%, counterexample 41.9%, probability 28.5%. Exp 2 N=37: certain 30.7%, counterexample 45.9%, probability 23.5% (z=2.94, p=.003). Over 1,300 written responses | a21, b25, b26 | contested against the scale-based split; small N |
| Speeded invalid AC/DA look valid | N=248, two experiments. Valid 73% vs invalid 66% endorsed (p=.06). Exp 2 63% vs 62% (p=.7) | a22 | single; not a strategy study |
| Fast answers follow alternative count | Four studies; under severe limits "many alternatives" gives more "invalid" than "few". About 15% respond logically at 5 s | d09, d10, d13 | contested interpretation; abstract only |
| More time can add association | Two studies, N=200 each. Time raised coherence and alternative-generation responses; on conflict base rates it raised stereotype weight | d08 | single; abstract only |
| Feeling of rightness predicts later change | N=289. Low-feeling mixed responders shift to validity-based; high-feeling shift to belief-based | d11 | single; abstract only |
| PHM fits human syllogism data | 5 studies, 320 points, r(318)=.90, rms .30. Logically correct 51.8% overall, 64.9% on valid. Min-heuristic predicts 95.17% of conclusions on invalid syllogisms. Matches p-valid conclusions in 22 of 31 (32 of 38 with Most and Few) | a16, a17 | single model paper; about 6 fitted parameters |
| PHM extends to Most and Few | Exp 1 (AMFO) pmin 67.03%, fit r(102)=.92. Exp 2 (MFIE) r(254)=.65 (42% of variance), pmin 37.03%. Rips (1994) r(254)=.74 with ten parameters | a18 | single; weaker with MFIE |
| Mood and strategy cross-check: other contexts | Brisson Study 2 deny-first endorsements (of 4): CE 1.27 vs stat 2.11 | b15 | single; N not captured |

Numbers I did not confirm: the 2013 time-pressure numbers, the 2023 training numbers, the F=5.57 value for Gratton 2021 (could not be extracted from the PDF text), and the study-by-study assignment of the F values in b10.

---

## 4. Mechanisms and models

This section is written so an engineer can turn each model into code.

### 4.1 The shared retrieval, different threshold model

Evidence: a11, b14, b16, d05.

1. Read the premises. Retrieve alternatives (cases that give Q without P). Both strategies retrieve the same alternatives (Brisson 2020).
2. Decision step, which is where the strategies split:
   - **Counterexample rule:** if any credible alternative exists, reject. Accept only if none is found.
   - **Statistical rule:** estimate P(P | Q) from the frequency of alternatives. Accept if above a threshold. Under a stated odds of 90% accept, under 50% reject.
3. The response format is applied last. A scaled answer outputs the estimate directly. A yes/no answer applies the rule above.

In code:

```
alts = retrieve_alternatives(premises)        # model slot
if mode == "counterexample":
    verdict = "reject" if any(valid(a) for a in alts) else "accept"   # valid() in code
else:
    p = share_of_cases_supporting(alts)        # in code from stated counts
    verdict = "accept" if p >= theta else "reject"
```

The threshold theta is the free parameter that separates the types. Counterexample is the special case theta = 1.0. This is an interpretation by the authors (Brisson: strategy shifts the threshold, not the retrieval). It is not a tested mechanism.

### 4.2 Diagnostic scoring (implementable now)

Evidence: a02, b04, b06.

```
R50 = number of rejections among the 5 items with ~50% alternatives
R90 = number of rejections among the 5 items with ~10% alternatives
if R90 + R50 == 10:       type = "counterexample"
elif R50 > R90 + 1:       type = "statistical"
elif R90 == 4:            type = "intermediate"    # counterexample who sometimes defaults
else:                     type = "other"
```

A continuous score (10% acceptances minus 50% acceptances) correlated r=.97 with the dichotomy in b06. The classification is one session of one item type. No reliability is published (d22, A01.07-K25).

### 4.3 The PHM statistical strategy

Evidence: a16, a17, a18, a23.

Informativeness order: All > Most > Few > Some > No-type (the paper orders by information theory with a rarity assumption).

- **Min heuristic:** the conclusion quantifier is that of the least informative premise.
- **P-entailment:** the next preferred conclusion is the one probabilistically implied by the min-conclusion.
- **Attachment:** the subject of the conclusion follows the min-premise's end term.
- **Max test heuristic:** confidence in a conclusion depends on how informative the most informative premise is.

Fit: r=.90 over 320 points; min-heuristic share of choices by max-premise: A 70.14%, I 31.11%, E 18.78%, O 18.04%; p-entailment about 10.76%; error 1.22% (a17).

Code form: given two quantified premises, `min_conclusion(p1, p2)` returns the heuristic answer. Compare with the logically valid answer from a solver. Where they disagree, the heuristic is wrong and a search is worth paying for (a16 agent_relevance). PHM covers no "nothing follows" answers: it predicts 60.42% of correct conclusions on valid syllogisms and 0% on invalid (a23).

### 4.4 The mReasoner counterexample search

Evidence: c03, c04.

mReasoner is a mental-model simulator with four knobs: LEN, BROAD, SYSTM2 (the probability of searching for a counterexample), WEAKEN. If the search is not triggered, the reasoner accepts its first conclusion. Search uses three moves:

1. Add an entity.
2. Move a property between entities.
3. Split one entity in two.

For a code-run search on quantified premises, each move is a small mutation of a finite model. Check the premises still hold and the conclusion fails. If so, the counterexample is certified.

In Eisape et al., 1,296 parameter settings (923 finished). PC1 captured 77% of behavioural variance. With correct answers zeroed out, PC1 still correlated 0.6 with SYSTM2. Larger models behave like high-SYSTM2, high-WEAKEN reasoners (c03). This is a behaviour fit, not proof of an inner search.

### 4.5 Strategy selection

Proposed, not tested (a14, b21):

- Selection is a meta-reasoning decision. People tend to pick the least demanding strategy.
- Signals available in humans: time available, response format, order of tasks, confidence in the fast strategy (d01, d11), alternative count (d09), working memory (a01, with limits).

A rule-based selector that uses these signals is our design hypothesis [D], not a finding.

### 4.6 The two-process timing picture

- Fast answers (3.5 to 5 s) are cue driven: semantic availability of alternatives, matching, and for a minority (about 15%) form (d09, d10).
- Slow answers add belief information (d07), and may also add alternative-generation (d08).
- Conflict detection is common to both strategies. Reaction time and feeling of rightness patterns match (b10). The divide is in resolving the conflict (b10, a07).

---

## 5. What holds up

### 5.1 Strong inside the lab

- The two response patterns exist and are stable within a session (b04, b06, d03).
- The gap shows on validity questions about uncertain forms (AC, DA, invalid syllogisms) and vanishes on probability questions (b02, b16, a11, A01.07-K02). This was shown in three papers.
- Belief-bias interaction replicated across three studies within the same paper and again in de Chantal (2020) and Markovits (2021) (a07, a08, a09).
- Strategy predicts performance beyond IQ in three of four tasks (d04).

### 5.2 Moderators

- **Question wording:** validity vs probability (a10, b02, b16).
- **Response scale:** categorical vs scaled (a12, b17). Free text gives a third picture (a21).
- **Time:** short limits push toward statistical (d01).
- **Premise type:** on MP with stated strength, statistical reasoners accept more. With many disabling conditions, counterexample reasoners accept more (d05).
- **Sample:** the share of statistical types ranges 28% to 45% (b04, b06, b19).
- **Task order:** probability items first move later validity judgments toward statistical (b03).

### 5.3 Failures, null results, tensions

- **Working memory story.** Verschueren: more working memory, more counterexample use, but the shift was about 9 points and the interaction was p=.055 (a01). de Chantal (2020): WM beta -.21, p=.07 (b07). Markovits (2021): WM and strategy correlate r=.12 (a09), and under 4 s WM has no effect while strategy does (b12). Raven correlates r=.33 with strategy (b13). So WM matters mostly with unlimited time (A01.07-K05, contested).
- **Probability instructions.** Brisson Study 3 found no validity-by-strategy interaction under probability instructions, unlike earlier studies (a11).
- **Disconfirmation interaction** is tiny (eta2p .004, a20/b18). Treat as marginal.
- **Conjunction fallacy:** strategy does not predict it (d04).
- **Causal tasks:** eta2p .036 to .038 (a19). Small.
- **Free-text challenge.** About 42% to 46% of answers explain uncertainty by a counterexample, and only about 23% to 29% by probability (a21, b25, b26). The authors suspect hedge words were coded as probabilistic, so the real counterexample share may be higher. This does not fit a clean two-type split built on rating scales (A01.07-K15, contested).
- **Speed paradox.** Kosourikhina and Handley (2025): under speed, invalid forms feel valid to most people (a22). This conflicts with "counterexample reasoners reject quickly" unless counterexample reasoners are the minority (about 15% logical at 5 s, d10).
- **Fast-answer interpretation.** Semantic availability (Markovits) vs formal-validity intuition (De Neys 2023) vs matching (Ghasemi 2022) (d13). Unresolved.
- **A transcription slip.** The 2024 review once says counterexample responding was "significantly faster" in 2013. Every other source says slower. Treated as a slip (a04).

### 5.4 Replication status

- No independent-lab replication of the 50/90 diagnostic. About 20 papers, all with Markovits or a close collaborator as author (d23, A01.07-K26).
- Near-independent work tests neighbouring questions: Newman, Gibb and Thompson (2017, deadlines, d07), Kosourikhina and Handley (2025, a22), Knauff and Gazzo Castaneda (2025, a21).
- No test-retest. Stability is documented only inside a session (d22, A01.07-K25).

### 5.5 Interventions

- **Worked:** short instruction to reason by counterexample or by probability, N=885, effect carried to the next task. Statistical reasoners changed most (d02, d03). Details unopened.
- **Worked:** changing the question from "how likely" to "is it logically valid" exposes strategy differences (a10, b02).
- **Did not work well:** counterexample reasoners hardly changed under instruction (d03). The follow-up task effects differed in direction between belief bias and base rates.
- **Unknown:** durability. A 2025 OSF registration for counterexample-based training exists, with no results seen (b31).
- **Boundary:** counterexample reasoning is not always better. It does not remove belief bias (d=1.04 remains, b09), and on MP with stated premise strength it can reject too much (d05).

### 5.6 Individual differences

- Counterexample types score higher on composite IQ, cognitive reflection and open-mindedness: M=0.438 vs -0.099 (a03). Intermediate lies between. Other is lowest.
- Strategy still predicts over and above these (d04, a03).
- Statistical reasoners answer faster (6.36 s vs 8.84 s, b07).
- Children as young as 6 show both kinds of reasoning (a06). Developmental claims are second-hand.

---

## 6. Language models

### 6.1 Headline

No study runs the diagnostic on a language model or tests a counterexample-versus-statistical prompt switch (c30, A01.07-K17). Everything below is indirect.

### 6.2 The estimate signature (form heuristic, rare "nothing follows")

- Eisape et al. (2024), PaLM 2: LMs almost never say "nothing follows". "Nothing follows" is correct for 37 of 64 syllogisms. LM accuracy on those is close to 0%. On the 27 syllogisms with a valid conclusion, human accuracy is about 50%, best LM about 75% (c01, c02). Method: zero-shot chain of thought, 30 samples at temperature 0.5.
- Bertolazzi, Gatt and Bernardi (2024), LLaMA-3 8B zero-shot CoT: atmosphere theory predicts 92% of its correct valid conclusions, 82.97% of its errors on invalid schemas, 62.79% on valid schemas. Humans 44.63% on valid, 40.97% on invalid. Best invalid-schema accuracy 32.50 (LLaMA-3 70B instruct) (a23, c06). PHM predicts 60.42% of correct conclusions on valid and 0% on invalid because it has no "nothing follows".
- NeuBAROCO (Ando et al. 2023), atmosphere items where the right answer is neutral (104 items): RoBERTa 0%, BART 0.96%, GPT-3.5 39.42% (d16). Old models.
- Holliday, Mandelkern and Zhang (2024): 29 LLMs make basic mistakes with conditionals. No model passes 90% on uncontroversial patterns. Best Llama 3.1 405B 89.50%, GPT-4 Turbo 87.17, Claude 3.5 Sonnet 85.33, Claude 3 Haiku 65.50. AC and DA fallacies are within these patterns (c08).
- Hasan, Greff and Grissom (2026): 29 models, 14,320 prompts. Only 9 beat the 0.5 competence floor (Gemma4:31B 0.675, Sonnet 4.6 0.642, Opus 4.7 0.570). Eleven below 0.30. Most had a fixed Yes or No preference. Gaps up to 64 points between negated and non-negated versions. Direct answers only (d15).
- Wang and Shi (2025): modus tollens is the hardest form for most open models. Possibility is easier than necessity. Soft accuracy ranges from llama-2-7b 0.335 to mistral-8x7b 0.724 (human 0.595, o1 0.926) (c25).

Reading: the default model behaviour is a cheap form heuristic, analogous in role to the statistical strategy. Eisape et al. fit larger models to a high-SYSTM2 profile (c03). Both can hold: bigger models search more but still fail on invalid items.

### 6.3 Alternatives and probability

- Kamath et al. (2026), ProbCOPA: 210 items, 25 to 30 raters per item, eight reasoning LLMs. Models match humans only at the extremes and avoid mid-scale answers. Human split-half Spearman 0.98 and 0.97. 90 of 100 sampled chains explicitly weigh alternative scenarios. Chain length correlates with human disagreement: Spearman 0.50 for GLM-4.6, 0.30 to 0.36 for GPT-5 and Kimi-K2. Higher temperature, persona prompts and reasoning effort did not restore human variation (c11, c12, c13). The strategies blend inside the chain.
- Orth, Mondorf and Plank (2026): Llama and Qwen models are sensitive to P(B|A) and relevance, slope up to 0.65. Less consistent than humans. Larger is not closer to humans (c14).
- Kirkpatrick and Sterken (2025): on 20 defeasible patterns with generics, CoT often hurts. For models above 75% zero-shot, mean CoT drop 11.14 points (SD 15.74), 28 LLMs (c17).
- Belief-R (Wilie et al. 2024), suppression-task style: 30 LMs mostly fail to revise. Most open models near 0% on belief update accuracy. CoT no significant gain. Plan-and-Solve about +1 point (c15, c16). Models do not spontaneously consider disabling conditions.

### 6.4 Does prompting or reasoning effort change strategy

- Holliday: zero-shot CoT cuts mistakes. Gains: Claude 3 Haiku +21.5, GPT-4o mini +15.83, GPT-4o +13.5, Claude 3 Opus +13.5, Llama 3.1 405B about +4.3, Mistral Large 2 about +0.2. Few-shot is not significantly different from zero-shot. Weak models gain most (c09).
- Poddar et al. (2025): 14 LLMs, 160 syllogisms. Twelve of 14 more accurate on belief-congruent items. Mean belief bias +10.81 points (SD 16.32, p=.0280, d=0.66). Top models under 2 points, weak ones up to 46.9. No systematic CoT gain. Few-shot mean -3.57 points (p=.0165) (d14).
- Nguyen et al. (BIS, 2026): all items valid and belief-inconsistent, so "always yes" scores perfectly. GPT-5-nano minimum effort 69.22, medium 98.84. GPT-5-mini medium 99.72. GPT-4o 79.54. Qwen3-32B 99.58 without thinking, 99.12 with. Effort levels are vendor settings, not equal tokens (d17).
- Bertolazzi: in-context examples and instruction tuning help valid inferences but not invalid ones. Only fine-tuning removed most biases. Accuracy falls as premises grow (c07).
- Li et al. (CounterMATH, 2025): a hint prompt to reason by example helped little; 1,025 training examples gave a small gain (Qwen2.5-Math-7B F1 38.3 to 41.1) and transferred (MATH 80.5 to 87.9, AIME 2024 20.0 to 30.0) (c23, c24).
- Dettki et al. (2026): on collider causal judgments, models use more rule-like strategies than humans. CoT improves alignment up to a ceiling (c26).

Reading: simple prompt changes give limited strategy control. The gains from "reason step by step" are model specific and largest in weak models.

### 6.5 Can models find falsifying cases

- REFUTE (Sinha et al. 2025): best agent falsifies under 9% of wrong submissions (o3-mini high with code feedback), though ratings suggest it can solve up to 48% of such problems. After all initial tests pass, success is 4% (+-1%). Prompting a random-plus-brute-force search: DeepSeek-V3 4.0, Gemini Flash 2.0 Thinking 3.7, DeepSeek-R1 4.0, o3-mini (high) 8.3. Handing over the correct solution (Oracle) gave 15.1, 7.7, 9.9. 35% of RandSearch samples ended in an incorrect counterexample; 86% of those came from wrong brute-force code (c18, c19).
- Counterexample Game (Drucker and Mahowald 2026): counterexample validity falls over iterations: 69% at position 0, 42 to 50% at positions 1 and 2, 17 to 30% by positions 5 to 9. Full history did not help (35.0% vs 36.0%). An Opus 4.5 judge accepted 60% of counterexamples, five humans 32%. Cohen kappa between human consensus and Opus 0.42 (95% CI 0.25 to 0.59) (c20, c21).
- CounterMATH: 1,216 statements, 87.8% true; DeepSeek-R1 F1 80.7; Qwen2.5-Math-72B-Instruct 41.8; most 7B open models around 30 (c23).
- Zouak et al. (2026): 4,707 false conjectures with Python verifiers. SFT on counterexamples alone destroyed true-theorem recognition (0.27 to 0.00 for Qwen3-4B). Reinforcement learning with the verifier as reward repaired it to 0.66. Verifier audit 97.7% of 177 decisions (d20). Training study, not a prompt scaffold.
- FVA-RAG (Ravishankara 2025): a falsification loop in retrieval; 79.80 to 80.05% vs 71.11 to 72.22% (Self-RAG); falsification triggered on 24.5% of queries (c22). Single author preprint, unreplicated.

Reading: asking the model to find a counterexample is weak. Code that checks it is cheap and reliable.

### 6.6 Code-run solvers

- Logic-LM (Pan et al. 2023): LLM translates, a solver infers. Average +18.4 points over CoT, +39.2 over standard prompting. GPT-4 (standard / CoT / Logic-LM): PrOntoQA 77.40 / 98.79 / 83.20; ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04. CoT wins on PrOntoQA. Not matched on tokens. Not counterexample search on invalid AC/DA (d18).
- Jha et al. (2023): a Z3 solver returns counterexamples to LLM plans in blocks world; 20 random problems; no matched baseline (d19).
- Guo et al. (2026): a router before generation beat random, self-select and always-think. Qwen3-4B on MovieLens: +6.3% NDCG@10 at 49.5% of tokens. A model asking itself did poorly (d21). Analogue only.

### 6.7 Summary of LLM picture

- Default is a form heuristic with a strong accept bias and few "nothing follows" answers.
- Chains list alternatives but the verdict stays compressed and often wrong on invalid items.
- CoT helps weak models most and can hurt on defeasible and belief-conflict items.
- Model-run counterexample search is weak and its judge is lenient.
- Code-run checks are the reliable part.

---

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. "Part" = SCHEMA part (G guardrail, S state, O operator, memory). The evidence ids are to this folder.

### Add now (established)

1. **Treat the verdict question as a design variable. Set it in code, not by default.** Ask "does it necessarily follow" for necessity items. Ask "how likely" for likelihood items. Never mix them in one request. **Part:** S1/S4. **[E]** a10, b02, b16, a11, a12, A01.07-K02, A01.07-K09.
2. **Do not assume one reasoner type. Do not use a model's graded output as proof it reasoned probabilistically.** The scale can create the pattern. **Part:** G10. **[E]** A01.07-K01, A01.07-K09; **[C]** a21 on how much.
3. **Put the counterexample check in code, not in the model's judgment.** Models falsify under 9% in REFUTE, validity decays over iterations, and the LLM judge accepts about twice as many counterexamples as humans. Code verifiers were 97.7% accurate on 177 audited decisions. **Part:** G2/G3/G8, S4. **[E]** c18, c19, c20, c21, d20, A01.07-K12 (the 60% vs 32% judge figure is single-source, A01.07-K13).
4. **Add a code-triggered "nothing follows" probe on invalid-looking forms.** Models almost never answer it, and weaker models follow atmosphere/min heuristics. Trigger on form (AC/DA, invalid-looking quantified premises), not on a schedule. **Part:** S4, O4 (drop a constraint, as the checking move). **[E]** a23, c02, c06, d16, A01.07-K10. The probe itself is untested.
5. **Do not rely on a step-by-step prompt to produce counterexample behaviour.** CoT gives no systematic gain across 14 models on belief conflict, hurts on generics, and gives about +1 on belief revision. **Part:** G11 ("think briefly by default"), SCHEMA 4b. **[E]** d14, c17, c16, A01.07-K23 (the overall status is contested because Holliday shows large CoT gains for weak models, c09).
6. **Do not claim a counterexample step removes belief effects.** In humans the belief effect shrank (d from 1.66 to 1.04) but did not vanish. **Part:** S8. **[E]** b09, a07, A01.07-K03.
7. **Do not map "search" to "more correct".** Strategy is an information-processing style (MP flips with premise strength and disabler count). Gate the search by item class. **Part:** G1, S4. **[S]** d05, A01.07-K18. Reasoning is sound, but the effect is one paper.
8. **Fast answers are cue driven, not guesses, and not logic.** On a capped path, assume the invalid-but-plausible forms are wrong about half the time (66% vs 73% endorsement in Kosourikhina). Verify those specifically. **Part:** G11/S0. **[E]** a22, d10, d09, d07, A01.07-K04, A01.07-K16 (A01.07-K16 is single-source; the rest are two sources).

### Test first

1. **Run the diagnostic on the agent.** 13 items, 90% vs 50% alternatives, under "valid?" and "how likely?" framings, at several token caps. Expect statistical-like at low cap and "valid?" framing. **Part:** S0/G11. **[S]** A01.07-K17, c30.
2. **Cheap-by-default, search-on-signal routing.** Use a quick estimate. Switch to code-run counterexample search when the signal fires. Candidate signals: low agreement across short samples (analogue of low feeling of rightness, d11), many available alternatives (d09), form flag (AC/DA). Compare with always-search at equal tokens. **Part:** G1/G12/S0. **[S]** A01.07-K06, A01.07-K21, A01.07-K24. Router evidence is from ranking (d21) and the human signals are from one lab.
3. **Instruction steering.** "Reason by counterexample" vs "reason by likelihood" per item class. Expect larger effect on weaker models (human analogue: statistical reasoners changed most, d02). **Part:** S0. **[S]** A01.07-K07.
4. **Order effect.** Likelihood questions before validity questions in one context vs fresh contexts. Supports fresh context per attempt (S3). **Part:** S1/S3. **[S]** b03, A01.07-K08. Effect size small in humans (eta2p .048).
5. **Alternative-count gate.** Count generated alternatives in code and see whether the answer tracks the count more than the form in capped mode. **Part:** G11/S0. **[C]** A01.07-K19.
6. **Disconfirmation weight.** Have code decide how much one failing case counts. In humans it differs by mode (CE 0.14 vs stat 1.75). **Part:** G2. **[S]** a20, but the interaction was tiny (b18).
7. **Syllogism figure as a load probe.** Non-contiguous middle terms should hurt a premise-reordering counterexample search but not a heuristic. **Part:** S4. Untested even in humans (a14, b22).
8. **mReasoner moves as operators.** Add / move / split as code-checked model-building moves on quantified items. **Part:** O4/O6 with code check. **[S]** c04.
9. **Extra time can hurt on conflict items.** Compare short and long budgets on belief-conflict items with a code check. **Part:** G11. **[S]** d08. Related to the "think briefly" guardrail.

### Memory

- Class record: log per item class whether the estimate or the search won. This is the memory form of the "which strategy wins on which item class" question. **Part:** memory. **[D]**.
- Treat any measured "strategy label" for the agent as a within-run measurement (A01.07-K25).

---

## 8. Concrete tests on our bench

All arms at equal tokens. Counting setup cost (G7).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | 13-item Markovits diagnostic (5 at 90%, 5 at 50%, 3 at 0%), framed "valid?" and "how likely?" | Plain model, under token caps (low, medium, high) | R90, R50, type label per cap and framing; agreement across 5 samples | Statistical-like pattern at low cap and "likely" framing; counterexample-like at high cap and "valid" framing. If the model rejects all ten at every cap, it is search-like by default. If it accepts all, it is accept-everything (the BIS confound). |
| T2 | Invalid AC and DA conditionals and quantified syllogisms (including pseudo-words and believable content) | (a) plain CoT, (b) CoT plus code-triggered "nothing follows" probe, (c) code-run counterexample search (add/move/split on a finite model) | Error on invalid schemas; false rejection rate on valid schemas; per class | (c) and (b) cut error on invalid; watch false rejection on valid and on strong-premise MP. Logic-LM suggests solvers can lose where the model already solves the class (PrOntoQA 83.20 vs 98.79). |
| T3 | Belief-conflict syllogisms (valid-unbelievable, invalid-believable) plus neutral | Plain; forced search step; content-swap in S1 (replace content with symbols); code check | Accuracy on conflict items reported separately by validity; belief effect | Search/swap lowers belief effect. Expect it not to reach zero. Report invalid-believable separately, because an all-valid set hides always-accept. |
| T4 | Same stems as T1 and T3, asked as "valid?" vs "how likely?" vs both in one request vs separate fresh contexts | 4 arms | Verdict consistency; answer shift after probability-first | Probability first lowers validity rejections; fresh contexts fix it. |
| T5 | Mixed item set (necessity items and likelihood items) | (a) always search, (b) always estimate, (c) rule router on form + alternative count + prior conflict, (d) router on sample agreement | Accuracy per class; tokens | (c)/(d) match always-search at fewer tokens. The test fails the router idea if always-search wins at equal tokens. |
| T6 | Modus ponens with stated high premise strength, and with many disabling conditions | Plain; search step | Rejection of strong-premise MP | A forced search step wrongly rejects strong-premise MP. This tests the "search is not more correct" claim (d05). |
| T7 | Belief-conflict and base-rate items at two token budgets | Short vs long reasoning with a code check | Accuracy by item; items that get worse with more tokens | Some conflict items worsen with longer thinking (d08). |
| T8 | Instruction arms: "reason by counterexample" vs "reason by likelihood" | Per item class | Gain per class; weak vs strong model | Larger shift on the weaker model; per-class pattern differs (human analogue d02). |
| T9 | Mixed set with defeasible generics ("birds fly") | Plain; CoT; search | Accuracy; CoT effect | CoT can lower accuracy (11.14 points in c17). |
| T10 | Re-run of T1 on another day and with fresh content sets | Same agent | Type agreement | Fills the missing test-retest gap (A01.07-K25). |

Report per item class and per model, not averages. Report false rejections next to correct rejections.

---

## 9. What does not transfer, and why

- **Working memory.** The founding trade-off ties strategy to working memory. A model has no span. Context length and token budget are only loose analogues. Even in humans the WM link is modest (9 points; beta -.21, p=.07).
- **Time pressure in seconds.** Deadlines of 3.5 to 5 s are human processing limits. A token cap is a weak analogue. Reasoning effort settings are vendor-defined, not equal tokens (d17).
- **Think-aloud and eye tracking.** Process evidence in humans (premise fixation d=.57) does not map to model text. Chain text is not evidence of the process (G10, c13).
- **Fixed types.** Human types are partly stable within a session. A model is a function of its prompt. A "type" label for a model is a measurement of one prompt condition, not a trait (A01.07-K25). The single-run diagnostic is a short test with no reliability data.
- **Soft normativism.** Humans may read "does it follow" as "is it probable" and be reasonable (a14, b23). A model task has a stated norm. The scaffold should state the norm, so this ambiguity should not exist for us.
- **Content and sample effects.** Students on an invented planet, French-speaking, paper or online (b01, b04). Small samples. The 50/90 stated-odds items may not reflect everyday inference.
- **The "Other" group.** About a quarter of people are dropped. Removing them can inflate the apparent separation (b19).
- **Counterexample ability itself.** In humans counterexample search is a mental act. In models it is weak (under 9% in REFUTE). The scaffold must therefore put it in code, which is a different mechanism from the human one.
- **Training results.** Counterexample training (CounterMATH, Zouak) needs weight updates. Our agent has no training, so only the code-checked scaffold parts apply (c24, d20).
- **PHM fit.** PHM was fitted to human syllogism data with about six parameters. Its min/atmosphere predictions fit LLaMA-3 8B well (82.97% of errors on invalid schemas) but that is a pattern match, not proof of the same mechanism (a23, c06).
- **Social, causal and contingency generalisations.** Small effects (eta2p .004 to .038), mostly relevant to people. Low priority for the agent (A01.07-K14).

---

## 10. Open questions

1. What does an LLM do on the 13-item diagnostic, and does it flip with "valid?" vs "how likely?" and with token budget? (c30, A01.07-K17.)
2. Does a code-run counterexample search beat plain CoT at equal tokens on invalid AC/DA and belief-conflict items? On which item classes does it lose, and what is its false-rejection rate? (A01.07-K22.)
3. Test-retest reliability of the diagnostic, across days and content sets. None found. (d22, A01.07-K25.)
4. How much of the time-pressure switch (Markovits 2013) is a true strategy change vs guessing? The 2013 numbers were never opened. Fast answers are cue driven (d07, d09), but the share is not quantified. (d01.)
5. Can strategy be chosen on purpose? The 2023 instruction study (N=885) needs full text: per-study N, effect sizes, durability. (d02.)
6. Which item classes does each strategy win on outside belief-bias syllogisms: quantified, planning, causal? Human data show tiny effects in causal tasks. (A01.07-K14.)
7. Does a "nothing follows" probe fix min/atmosphere errors without raising false rejections? (A01.07-K10, d16.)
8. Does an independent lab replicate the diagnostic effects? None found. (d23, A01.07-K26.)
9. Can a cheap router pick search vs estimate better than always-search? Analogue is only a ranking router. (d21, A01.07-K24.)
10. Is the two-type split real, or is it two modes of one person made visible by scales? (a21, b25, b26, A01.07-K15.)
11. What is the semantic-cue vs formal-intuition vs matching explanation for fast answers? (d13.)
12. Do mid-sized reasoners show a strategy effect at all? Every LLM paper here uses its own framing; none uses the diagnostic. (c30.)
13. Beeson's untested proposals: syllogism figure should hurt only counterexample reasoners; strategy selection is meta-reasoning. (a14.)

---

## 11. Sources

[V] = opened and read this session (full text, or abstract where marked "abstract" below). [M] = snippet or second-hand only.

**Founding and human dual-strategy work**

- [V] Verschueren, Schaeken and d'Ydewalle (2005). Everyday conditional reasoning: a working memory-dependent tradeoff between counterexample and likelihood use. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/BF03195301.pdf (a01)
- [M] Verschueren, Schaeken and d'Ydewalle (2005). A dual-process specification of causal conditional reasoning. Thinking and Reasoning 11, 239-278. https://doi.org/10.1080/13546780442000178 (a24, b28)
- [V] Markovits (2024). Are There Two Kinds of Reasoners? J. Intelligence 12(3):25. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10971091/ (a02 to a06, d03, d22)
- [V] Markovits, Brisson and de Chantal (2015). Additional evidence for a dual-strategy model of reasoning. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-015-0535-1.pdf (a10, b01 to b05)
- [V] Markovits, Brisson, de Chantal and Thompson (2017). Interactions between inferential strategies and belief bias. Memory and Cognition. https://link.springer.com/10.3758/s13421-017-0723-2 (a07, b09, b10)
- [V, abstract] Markovits, Brisson and de Chantal (2017). Logical reasoning versus information processing in the dual-strategy model. JEP:LMC. https://doi.org/10.1037/xlm0000291 (d05)
- [V] de Chantal, Newman, Thompson and Markovits (2020). Who resists belief-biased inferences? Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-019-00998-2.pdf (a08, b06 to b08)
- [V] Brisson and Markovits (2020). Reasoning strategies and semantic memory effects in deductive reasoning. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-020-01027-3.pdf (a11, b14 to b16)
- [V] Markovits, de Chantal, Brisson, Dube, Thompson and Newman (2021). Reasoning strategies predict use of very fast logical reasoning. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-020-01108-3.pdf (a09, b11 to b13)
- [V] Gratton and Markovits (2021). Reasoning strategies determine the effect of disconfirmation on belief in false claims. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-021-01190-1.pdf (a20, b18, b19)
- [V] Beghin and Markovits (2022). Reasoning strategies and prior knowledge effects in contingency learning. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/s13421-022-01319-w.pdf (a19, b20). Listed as "Begin" in one earlier line; the correct spelling is Beghin.
- [V] Markovits, Lortie Forgues and Brunet (2010). Conditional reasoning, frequency of counterexamples, and the effect of response modality. Memory and Cognition. https://link.springer.com/content/pdf/10.3758/MC.38.4.485.pdf (a12, b17)
- [V, abstract] Markovits, Lortie Forgues and Brunet (2012). More evidence for a dual-process model of conditional reasoning. Memory and Cognition 40:736-747. https://doi.org/10.3758/s13421-012-0186-4 (d06; a26 and b29 [M])
- [V, abstract] Markovits, Brunet, Thompson and Brisson (2013). Direct evidence for a dual process model of deductive inference. JEP:LMC 39(4). https://doi.org/10.1037/a0030906 (d01; a25, b05 [M])
- [V, abstract] Markovits and Thompson (2023). Can we change how people reason? JEP:LMC 49, 1773-1785. https://doi.org/10.1037/xlm0001293 (d02; a28 [M])
- [V, abstract] Thompson and Markovits (2021). Reasoning strategy vs cognitive capacity as predictors of individual differences in reasoning performance. Cognition 216:104866. https://doi.org/10.1016/j.cognition.2021.104866 (d04; a27, b30 [M])
- [V, abstract] Gagnon-St-Pierre, Doucerain and Markovits (2021). Reasoning strategies explain individual differences in social reasoning. JEP:General. https://doi.org/10.1037/xge0000852 (d12)
- [V] Markovits et al. (2019). The development of fast and slow inferential responding. https://link.springer.com/content/pdf/10.3758/s13421-019-00927-3.pdf (b27; abstract and introduction only)
- [V, abstract] Markovits, Bergeron and Gagnon-St-Pierre (2026). Thinking longer versus thinking better. Memory and Cognition. https://doi.org/10.3758/s13421-026-01905-2 (d08)
- [V, abstract] Markovits, Thompson and Bergeron (2026). Fast reasoning uses semantic activation as an intuitive cue. Memory and Cognition. https://doi.org/10.3758/s13421-026-01859-5 (d09)
- [V, abstract] Markovits (2025). Evidence for some form of abstract logical intuition. Psychonomic Bulletin and Review. https://doi.org/10.3758/s13423-025-02713-6 (d10)
- [V, abstract] Thompson and Markovits (2025). Fast reasoning and metacognition. Psychonomic Bulletin and Review. https://doi.org/10.3758/s13423-025-02662-0 (d11)
- [V, abstract] Markovits, Bergeron and Gagnon-St-Pierre (2026), with Mekik, Vivier and Markovits (2026). Rethinking logical intuitions about deductive reasoning. JEP:LMC. https://doi.org/10.1037/xlm0001667 (d13)
- [M] Markovits et al. (2018), Markovits et al. (2016, reported in the 2024 review) as cited in a03 and b24; and Markovits et al. (2025) OSF registration of counterexample training. https://doi.org/10.17605/osf.io/mh83s (b31)

**Theory and independent work**

- [V] Chater and Oaksford (1999). The Probability Heuristics Model of Syllogistic Reasoning. https://www.dectech.co.uk/publications/LinksNick/ReasoningAndDecisionMaking/The%20Probability%20Heuristics%20Model%20of%20Syllogistic%20Reasoning.pdf (a16 to a18)
- [V] Beeson, Stupple, Schofield and Staples (2019). Mental Models or Probabilistic Reasoning or Both. Psychological Topics 28(1). https://pt.ffri.hr/pt/article/download/517/276 (a14, a15, b21 to b24)
- [V] Geiger and Oberauer (2007). Reasoning with conditionals: Does every counterexample count? https://link.springer.com/content/pdf/10.3758/BF03192938.pdf (a13)
- [V] Knauff and Gazzo Castaneda (2025). Reasoning beyond clicks. https://link.springer.com/content/pdf/10.3758/s13421-025-01796-9.pdf (a21, b25, b26)
- [V] Kosourikhina and Handley (2025). Conflict detection with invalid inferences: All heuristics, no logic. https://link.springer.com/content/pdf/10.3758/s13421-025-01709-w.pdf (a22)
- [V, abstract] Newman, Gibb and Thompson (2017). Rule-based reasoning is fast and belief-based reasoning can be slow. JEP:LMC. https://doi.org/10.1037/xlm0000372 (d07)
- [M] Hattori (2016); Elflein and Ragni (2018); Roberts (2000); Beilock and DeCaro (2007); Stupple and Ball (2007); De Neys (2023); Ghasemi et al. (2022). Cited inside a14, a15, b21, b22, d13, not opened.

**Language-model studies**

- [V] Eisape, Tessler, Dasgupta, Sha, van Steenkiste and Linzen (2024). A Systematic Comparison of Syllogistic Reasoning in Humans and Language Models. https://arxiv.org/abs/2311.00445 (c01 to c05)
- [V] Bertolazzi, Gatt and Bernardi (2024). A Systematic Analysis of LLMs as Soft Reasoners: Syllogistic Inferences. https://arxiv.org/pdf/2406.11341 (a23, c06, c07)
- [V] Holliday, Mandelkern and Zhang (2024). Conditional and Modal Reasoning in LLMs. https://aclanthology.org/2024.emnlp-main.222.pdf (c08 to c10)
- [V] Kamath, Madathil, Schuster, de Marneffe and Reddy (2026). Humans and LLMs Diverge on Probabilistic Inferences. https://aclanthology.org/2026.tacl-1.93/ (c11 to c13)
- [V] Orth, Mondorf and Plank (2026). If Probable, Then Acceptable? https://aclanthology.org/2026.eacl-long.18/ (c14)
- [V] Wilie, Cahyawijaya, Ishii, He and Fung (2024). Belief-R. https://aclanthology.org/2024.emnlp-main.586.pdf (c15, c16)
- [V] Kirkpatrick and Sterken (2025). Generics and Default Reasoning in LLMs. https://arxiv.org/abs/2508.13718 (c17)
- [V] Sinha et al. (2025). Can Language Models Falsify? (REFUTE). https://arxiv.org/abs/2502.19414 (c18, c19)
- [V] Drucker and Mahowald (2026). The Counterexample Game. https://arxiv.org/abs/2605.03936 (c20, c21)
- [V] Ravishankara (2025). FVA-RAG. https://arxiv.org/abs/2512.07015 (c22)
- [V] Li et al. (2025). CounterMATH. https://arxiv.org/abs/2502.10454 (c23, c24)
- [V] Wang and Shi (2025). Logical forms complement probability. https://arxiv.org/abs/2502.09589 (c25)
- [V] Dettki, Wu and Rehder (2026). Do LLMs Share Human-Like Biases? https://arxiv.org/abs/2602.02983 (c26)
- [V] Azin, Yu, Singh and Jouravlev (2026). Presupposition and Reasoning in Conditionals. https://arxiv.org/abs/2605.18352 (c27)
- [V] Poddar, Sahoo and Ghosh (2025). Understanding Syllogistic Reasoning in LLMs. https://arxiv.org/abs/2512.12620 (d14)
- [V] Hasan, Greff and Grissom (2026). Benchmarking LLM Competence on Logical Inference over Probability Operators. https://arxiv.org/abs/2607.27405 (d15)
- [V] Ando, Morishita, Abe, Mineshima and Okada (2023). NeuBAROCO. https://arxiv.org/abs/2306.12567 (d16)
- [V] Nguyen et al. (2026). BIS Reasoning 1.0. https://arxiv.org/abs/2506.06955 (d17)
- [V] Pan, Albalak, Wang and Wang (2023). Logic-LM. https://arxiv.org/abs/2305.12295 (d18)
- [V] Jha et al. (2023). Counterexample Guided Inductive Synthesis using LLMs and SAT solving. https://arxiv.org/abs/2309.16436 (d19)
- [V] Zouak et al. (2026). Counterexample Generation via Per-Theorem Symbolic Verifiers. https://arxiv.org/abs/2610.02444 (d20)
- [V] Guo et al. (2026). Think When Needed: Model-Aware Reasoning Routing. https://arxiv.org/abs/2601.18146 (d21)
- [M] Gomez-Sanchez et al. (2021). Conditional content, explicit information and generating cases. https://digibug.ugr.es/handle/10481/66918 (c28; snippet only)
- [M] Lean Disprove (ICML 2026 listing). https://icml.cc/virtual/2026/82610 (c29; listing only)
- [M] Search record: no LLM test of the diagnostic (c30); no test-retest (d22); no independent replication (d23). Europe PMC https://www.ebi.ac.uk/europepmc/ and PMC review above.

Cross-check notes (critique.md): the earlier line a07 gave N=170 analysed; the paper classifies 170 plus 61 "other" (about 231). The Gratton interaction F=5.57 could not be extracted from the PDF text. Several d-lines are abstract-level. The 2013 and 2023 papers need full text to close gaps 4 and 5.
