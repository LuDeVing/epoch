# Desirable difficulties: deep document

*Subfield A05.04 of the learning-science field. Written from evidence_a-d.jsonl (a01-a29, b01-b30, c01-c27, d01-d34), claims.jsonl (K01-K41) and critique.md in this folder. Evidence ids (a01, b22, ...) and claim ids (K01, ...) are cited inline. Status words: established (2+ independent sources), single-source, contested.*

**Reading warnings.** (1) Lines d01-d17 in evidence_d are reconstructed index lines: their text was copied from the claims, so re-open the source before reusing any number from them. (2) The 2026 LLM papers (arXiv ids 26xx) are preprints; none was seen peer reviewed. (3) No study found tests the central claim for an LLM agent (K34). All machine evidence here is by analogy.

---

## 1. What it is

A desirable difficulty is a learning condition that makes practice feel harder and often lowers performance during practice, but raises retention and transfer on a later test. The term and the framing come from Robert Bjork (a01, 1994). The standard list:

- **Spacing** (distributing practice over time instead of massing it).
- **Interleaving** (mixing problem or category types instead of blocking them).
- **Self-testing** (retrieval practice instead of restudy).
- **Generating or attempting before being shown** (including failed attempts followed by feedback).
- **Varying conditions** of practice, and **reducing feedback frequency**.

The second half of the idea matters as much as the first: **performance during learning misleads.** Conditions that help now often hurt later, and learners judge by what feels easy now. So both teachers and learners drift toward easy conditions (a01, a17, b16).

The label is defined by outcome: a difficulty is "desirable" if it helps later. That is partly circular (a01 limits, critique). It does not say all difficulty helps. Generation, extra task complexity and high cognitive load can all be undesirable (b05, a10, a22).

**Why it matters for our agent.** The schema judges changes (new lessons, new operators, new prompts) by pass rate. If the human pattern carries over, the quick gain seen when a lesson is written, or when a scaffold change is tried, can be the wrong signal. The practical caution: do not judge a lesson or a schema change by its immediate gain. Score it later, on fresh problems, with the helper removed.

What is known for LLM agents is thin. The nearest results are agent-memory studies that score held-out tasks (d18, d19, d21), weight-training studies that borrow spaced repetition (c01), and human studies of people using LLMs (c19). None varies "harder vs easier practice" and then tests after a delay (K34).

## 2. History and theories in depth

### 2.1 Early observations (before the name)

Bjork's 1994 chapter (a01) collects the early cases:

- **Bahrick (1979):** 50 Spanish words learned in sessions 0, 1 or 30 days apart. The 30-day gap was worst on in-session tests and best on a test 30 days after training.
- **Hogan and Kintsch (1971):** study trials won at the end of a session; test trials won after 48 hours.
- **Landauer and Bjork (1978, a18):** expanding retrieval practice. For test-type practice, rehearsals at increasing intervals gave the best name recall; for restudy-type practice, uniform spacing was slightly better. Later work found expanding vs equal gaps mixed, possibly depending on feedback (a07).
- **Mannes and Kintsch (1987):** an inconsistent outline hurt verbatim recall but helped inference questions.

### 2.2 The founding experiments

- **Shea and Morgan (1979, a02), contextual interference.** 72 subjects learned three arm-movement tasks, blocked or random. Blocked won in practice (errors 4.42 vs 9.13, F(1,68) = 23.75). Random won on retention (2.10 vs 4.33, F(1,68) = 12.85), at 10 minutes or 10 days. Blocked-trained subjects tested in random order did worst. At 10 days blocked-blocked was slightly faster than random-random, so the benefit depends on the test format.
- **Simon and Bjork (2001, a03), the keystroke study.** 48 students, 24 per group, learned three 5-key sequences, each with its own goal movement time. Practice error: blocked 5.68% vs random 8.85% (F(1,46) = 10.41). The 24-hour test reversed it: blocked 19.68% vs random 10.80% (F(1,46) = 22.29, p < .001). Blocked learners predicted they would do better (8.19% predicted vs 19.68% actual). Random learners predicted well (11.87% vs 10.80%). The authors conclude that people read current ease of access as a valid index of learning.
- **Roediger and Karpicke (2006, a05), test-enhanced learning.** Restudy won at 5 minutes (81% vs 75%, d = 0.52). Testing won at 2 days (68% vs 54%, d = 0.95) and 1 week (56% vs 42%, d = 0.83). Restudiers predicted they would remember more. In Exp 2 the group that read the passage 14.2 times recalled 40% at 1 week; the group that studied once and was tested three times recalled 61%.
- **Karpicke and Roediger (2008, a06).** 40 Swahili-English pairs. Dropping a pair from testing after one recall cost a lot (36% and 33% at 1 week vs about 80% when testing continued). About 80 extra study trials after first recall added almost nothing. Predicted recall was about 50% in all four conditions.
- **Kornell and Bjork (2008, a04), "spacing as the enemy of induction".** Paintings by 12 artists, massed or mixed, then identify the artist of new paintings. Exp 1a: 61% spaced vs 35% massed on the first test block (d = 0.99, N = 120). Exp 1b: 59% vs 36% (d = 1.28, N = 72). 78% did better with spacing, yet 78% said massing was as good or better. The authors expected massing to win. Interleaving won in every experiment.
- **Rohrer and Taylor (2007, a11).** Exp 2, geometry solid volumes: practice accuracy blockers 89% vs mixers 60% (d = 1.06); one-week test blockers 20% vs mixers 63% (d = 1.34). Small samples (about 16 analysed).

### 2.3 The theories

**New Theory of Disuse (Bjork and Bjork, 1992; a28, second-hand via Rowland a09).** Each memory has a storage strength (how well learned) and a retrieval strength (how accessible now). Performance during learning tracks retrieval strength. Durable learning is storage strength. A retrieval attempt adds more storage strength when retrieval strength is lower. So conditions that lower retrieval strength during practice can raise storage strength more. The primary chapter was not opened; no equations were seen.

**Retrieval effort / bifurcation accounts (a09).** Rowland's meta-analysis supports effortful processing: recall tests beat recognition tests. Limited support was found for semantic elaboration.

**Transfer-appropriate processing and elaborate encoding (a01).** Varied conditions force more elaborate encoding and more varied retrieval routes.

**Discriminative contrast (a21, Ge et al. 2021).** Interleaving puts different categories side by side, so differences stand out. Eye-tracking did not support the rival "attention attenuation" account (blocked learners attend less to later same-category items). Raising contrast raised learning. Sequential comparison and retrieval accounts are not ruled out.

**Metacognitive illusion accounts (a17, a29, b18).** Learners treat fluency as a sign of learning. Three causes were named by Yan, Bjork and Bjork (2016): fluency, prior beliefs, and belief that one is unique as a learner. Instruction alone had only modest effects in Exps 3-5; seeing the two schedules' test results separately plus theory moved a majority in Exp 6 (abstract only, b18).

**In-context vs in-weight learning (a24, b20, b21, c06, c07; one source).** A metalearning network that can learn both ways explains curriculum effects. If a rule can be read from a block, in-context learning solves it and blocked order wins. If there is no easy rule, errors flow into the weights, and interleaving wins because blocking causes forgetting of the earlier block. More errors give more in-weight learning and better retention, while limiting access to context examples hurts flexibility and helps retention.

**Cognitive load theory as the rival (a22).** Desirable difficulties says more effort improves retention. Load theory says extraneous load hurts. The 2025 review proposes a combined rule: raise difficulty for low-element-interactivity material, lower it for high-element-interactivity material. It is untested. It echoes Donovan and Radosevich (a10) on task complexity and the expertise-reversal subfield (A08.04).

**Learning vs performance (b16, Soderstrom and Bjork 2015, abstract only).** Performance during practice is an unreliable index of learning. Conditions that raise performance can lower retention, and the reverse.

### 2.4 Applied extensions

- **Self-regulated learning (a17, b09).** Learners choose desirable difficulties poorly. de Bruin (2023) describes the S2D2 framework (Start and Stick to Desirable Difficulties): explain the paradox and change how students judge effort.
- **Phase model (b08).** Hattie and Donoghue: surface acquisition, consolidation, deep learning; spaced investment pays at consolidation. Conceptual, not tested.
- **Spaced-repetition engineering (a20).** Half-life regression for Duolingo. See section 4.

## 3. Core findings with exact numbers

Status key: **established** = 2+ independent sources agree; **single-source**; **contested** = sources disagree or nulls exist. "Human" = human participants unless stated.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Practice performance runs opposite to later retention (motor) | Practice error blocked 5.68% vs random 8.85%; 24 h test blocked 19.68% vs random 10.80%; N = 48 | Simon and Bjork 2001 (a03) | established (K01) |
| Same, motor, retention and transfer | Practice errors 4.42 vs 9.13; retention 2.10 (random) vs 4.33 (blocked); N = 72 | Shea and Morgan 1979 (a02) | established (K01) |
| Same, prose | 5 min: restudy 81% vs test 75% (d = 0.52). 2 days: test 68% vs 54% (d = 0.95). 1 week: 56% vs 42% (d = 0.83); N = 120 | Roediger and Karpicke 2006 (a05) | established (K01) |
| Same, maths problems | Practice blockers 89% vs mixers 60%; test blockers 20% vs mixers 63% (d = 1.34) | Rohrer and Taylor 2007 (a11) | established (K01) |
| Learners misjudge: prefer the easy condition | 78% did better spaced yet 78% rated massing as good or better (N = 120); replication 71% (87 of 123) said massing taught most; 90% better spaced but 72% said massing better (second-hand) | Kornell and Bjork 2008 (a04); Verkoeijen 2014 (a13); Bjork et al. 2013 (a17) | established (K02) |
| Misjudgment persists in older adults | 75% of older adults (mean age 77) rated massing best for induction; 56% of young | Kornell et al. 2010 (a12) | established (K02) |
| Predictions flat while truth differs 2.4x | Predicted recall about 50% in all four conditions; actual 33-36% vs about 80% at 1 week; d = 4.03 for repeated retrieval | Karpicke and Roediger 2008 (a06) | established (K02) |
| Spacing helps at every retention interval (verbal recall) | 839 assessments, 317 experiments, 184 articles; best gap grows with the retention interval | Cepeda et al. 2006 (a07) | established (K03) |
| Optimal gap vs zero gap | Recall +64%, d = 1.1; recognition +26%, d = 1.5; N > 1,350. Best gap 1, 11, 21, 21 days for tests at 7, 35, 70, 350 days (about 43%, 23%, 17%, 8% of the interval, spline) | Cepeda et al. 2008 (a08) | established (K03) |
| Gap-ratio rule not firm | Online replication: spaced beats massed; best-gap effect mixed (162 analysed) | Rogers et al. 2025 (d12) | contested (K26) |
| Spacing shrinks with task complexity | Overall d = 0.46 (63 studies, 112 effects); simple tasks 0.97; average-complexity 0.42; complex 0.11 and 0.07; r = -.25; low-rigor studies gave larger effects | Donovan and Radosevich 1999 (a10) | single-source (K04) |
| Spacing, other meta-analytic size | d = 0.60 (4 metas, 360 studies) | Hattie and Donoghue 2016 (b07) | established (K03) |
| Testing beats restudy | g = 0.50 [0.42, 0.58], I-squared = 84.35%, tau-squared = 0.21; classroom g = 0.499 (222 studies, 48,478 students); g = 0.61-0.70 (Adesope, second-hand); d = 0.44 (10 metas, 674 studies) | Rowland 2014 (a09); Yang 2021 (b13); b04; b07 | contested (K05) |
| Testing effect failures | Higham 2023: restudy 0.74 vs retrieval 0.63-0.65 (n = 259) when a rating was required each trial; Zhao 2023: g = 0.10, BF10 = 0.19; Prolific: F = 0.13, p = 0.72 (67 of 120 returned) and U = 1773, p = 0.17 (129 of 426) | d10, d11, b03 | contested (K05, K07) |
| Testing transfers less | d = 0.40 [0.31, 0.50] to new items (122 experiments, N = 10,382); weakest to rearranged items and worked-example problems | Pan and Rickard 2018 (b14, abstract) | established (K06) |
| Unsuccessful retrieval then feedback beats read-only | Exp 1 .41 vs .31, d = 0.58 (N = 25); later experiments d = 0.38-1.49; omission vs commission errors equal (.64 vs .70, n.s.) | Kornell, Hays and Bjork 2009 (a15) | established (K08) |
| Interleaving, overall | g = 0.42 [0.34, 0.50]; paintings 0.67, photographs 0.35, maths 0.34, words -0.39, text n.s.; similarity between categories +0.22, similarity within -0.17; immediate follow g 0.73 vs spaced 0.22 | Brunmair and Richter 2019 (d03-d05; b11) | established (K09) |
| Interleaving, smaller older figure | d = 0.21 (1 meta, 12 studies) | Hattie and Donoghue (b07) | superseded by Brunmair |
| Interleaving replicates with forced choice | Identification: 0.29 vs 0.38, dz = 0.48 (N = 288); 2AFC: dz = 0.43 (N = 276); authors flag response-bias confound of identification | Donenfeld et al. 2026 (a14) | contested (K10) |
| Exact replication of painting recognition | Hit rate .75 vs .66, d = 0.37 (original .77 vs .67, d = 0.41); N = 123 | Verkoeijen and Bouwmeester 2014 (a13) | established (K02) |
| Classroom interleaving + retrieval | Month-later test: not quizzed 47%, blocked quiz 54%, interleaved quiz 63%; interleaved vs not quizzed d = 0.71; interleaved vs blocked d = 0.35; N = 155 | Sana and Yan 2022 (a19) | established (K09) |
| Physics course: harder homework, better surprise test | Homework 0.74 vs 0.69 and 0.76 vs 0.67 (blocked vs interleaved); surprise test d = 0.40 and 0.91 | Samani and Pan 2021 (b01) | established (K09) |
| Same course: high-stakes midterm hides it | Midterm 3 days later d = 0.20 (CI -0.04 to 0.43) and d = 0.02; students crammed | Samani and Pan 2021 (b02) | contested (K11) |
| Field RCT, year-long interleaving | +0.28 SD short term; no average effect on cumulative end-of-year test; gains in lower achievers | Kremer et al. (d28) | single-source (K40) |
| Counter-case to interleaving | Finding the one shared word in 6 clues favoured massing: .34 vs .22, d = 0.65 | Kornell and Bjork 2008 (a04) | single-source |
| Generation effect fragile | 0 of 7 recall experiments showed it; disadvantage in 4 of 7; N = 40 to 152 | Text generation replication 2025 (b05, b06) | single-source (K12) |
| Debiasing the illusion is hard | Instruction gave modest effects (Exps 3-5); separated results plus theory moved a majority (Exp 6) | Yan et al. 2016 (b18, abstract) | single-source (K13) |
| Learners choose testing only with feedback | Test chosen above 50% by list 4 with feedback (d = 1.10); not significant without | Kornell and Son 2009 (a16) | single-source |
| Half-life regression beats Leitner | MAE 0.128 vs 0.235; AUC 0.51-0.54 for all; 12.9M instances | Settles and Meeder 2016 (a20) | single-source (K19) |
| AI help raises practice, lowers later exam | GPT Base +0.137 practice (+48%), exam -0.054 (SE 0.022, -17% of control mean 0.321). GPT Tutor +0.361 (+127%), exam -0.004 (SE 0.013). 2,848 obs. | Bastani et al. 2025 (c19, b22) | established (K15) |
| Same direction, other study | ChatGPT essay score up (F = 4.549, eta2 = 0.108); knowledge gain F = 0.913; transfer F = 0.019 (N = 117) | Fan et al. 2024 (c21) | established (K15) |
| AI baseline: high perceived, low real learning | Guided hints vs baseline d = 1.14, about +45%; contrastive d = 0.74, p = 0.080; N = 85 | Eleftheriou et al. 2026 (c22) | established (K16) |
| Attempt first, then AI (humans) | Final test 91.85 vs 78.59, d = 1.54 (n = 60); AI-guided vs fixed pretest 85.71 vs 83.56 (p = .319); harder task 76.87 vs 69.65 (p = .018) | Struggle First (d29) | single-source (K41) |
| Machine: spaced scheduling vs uniform replay (weights) | TinyLlama old accuracy 49.0 vs 25.2 (base 54.3, naive 11.7); Llama-3.2-3B 51.6 vs 46.2; new accuracy about 20.0 vs 38.8 for difficulty-only | Atreya et al. 2026 (c01-c03) | single-source (K17, K28) |
| Machine: in-context distributed repeats | Sweet spot at 100-400 steps in a Markov-chain task | Kang et al. 2025 (d01, reconstructed) | established (K21) |
| Machine: order in fine-tuning inside noise | 761 runs, 12 base models; effects 0.010-0.021 vs 0.019 floor; largest contrast 0.0619 read +0.010 and -0.015 on reruns; interleaving +0.0483 when scored on both skills (6 of 6) | Chen et al. 2026 (c08, c09) | single-source (K29) |
| Machine: self-written skills hurt | -8.1 to -11.5 pp vs none; curated +18.2 to +24.8 pp (87 tasks, 3 harnesses) | SkillsBench (d08) | established (K22) |
| Machine: lessons overstate transfer | AppWorld GPT-4.1 held-out +3.6 pp vs dev +12.3 pp (task goal); +14.3 vs +26.3 (scenario goal) | Fang et al. 2026 (d21) | single-source (K36) |
| Machine: run noise | Single-run pass@1 spread 2.2-6.0 pp; SD above 1.5 pp at temperature 0; best strategy wins 77% of head-to-head runs over 30 trials | d25, d26 | established (K39) |

## 4. Mechanisms and models

Each model is written so an engineer can implement it. The first four are human-memory models; the rest are the machine analogues.

### 4.1 Storage strength vs retrieval strength (Bjork and Bjork, a28, a09; second-hand)

State per item: `S` (storage, only goes up) and `R` (retrieval, decays with time and rises on any access).

```
on study or retrieval at time t:
    gain_S = f(1 - R)          # lower R before the access -> bigger rise in S
    S = S + gain_S
    R = high                   # accessible right after
between accesses:
    R decays; the decay is slower when S is larger
performance_now ~ R
performance_later ~ S (and R after waiting)
```

The form of `f` is not in our sources; only the direction is ("difficult tests add more when retrieval strength is lower"). Prediction: any condition that keeps `R` high during practice (blocking, massing, restudy) gives good practice scores and little `S` gain.

### 4.2 Cepeda ridgeline (a08): choosing the review gap

Fitted model of final recall given gap `g` and retention interval `t`:

```
recall = A * (1 + b*t)^(-R)
A = p + (1 - p) * exp(-a * g)
R = 1 + c * (ln(g + 1) - d)^2
b = .011, p = .760, a = .017, c = .092, d = 3.453   (days)
```

Behaviour: recall rises then falls with `g` (inverted U). The best `g` grows with `t` but shrinks as a share of `t`: about 20-40% of a one-week delay, 5-10% of a one-year delay. The authors call this function "a reasonable" one, not unique. Rogers et al. 2025 (d12) found the best-gap result inconsistent online. Do not hard-code ratios; sweep the gap (K26).

### 4.3 Half-life regression (a20): when a stored item is due

```
p_recall = 2^(-lag / h)        # lag = time since last review, h = half-life
h = 2^(theta . x)              # x = history features (times seen, times correct, ...), learned by regression
review when p_recall falls below a threshold
```

On 12.9M Duolingo instances MAE was 0.128 vs Leitner 0.235. AUC was only 0.51-0.54 for every model, so ranking among items is weak. The A/B retention gains measure engagement, not learning (K19).

### 4.4 SuperMemo-2 state as used in SRT (c01, a25)

Per example: ease factor, review count, interval, due step. Per-example perplexity serves as the recall-quality score. At each step the examples that are due are replayed, within a fixed 20/80 old/new cap (same cap as uniform replay). Successful recall lengthens the interval; failure shortens it. Standard SM-2 (our background knowledge, not from the evidence lines): quality `q` from 0-5; if `q < 3` restart intervals at 1; else intervals 1, 6, then `interval * EF`; `EF' = EF + 0.1 - (5-q)(0.08 + (5-q)*0.02)`, floor 1.3. How perplexity was mapped to `q` was not recorded in our evidence; re-open c01 before copying. Overhead about +14.7% wall clock vs uniform replay.

Contrast baseline (c02): replay highest-perplexity old examples, no intervals ("difficulty-only"). It learns new facts best (38.8%) and keeps old knowledge poorly (27.4%). So "hardest first" is not "spaced".

### 4.5 Interleaving accounts as an implementable rule (d04, a21)

Interleaving helps when categories are similar to each other (so contrast is informative) and exemplars within a category differ (so each block does not already show the whole category). Meta-regression: similarity between +0.22, similarity within -0.17. Benefit was larger when items followed at once (g 0.73) than when spaced (0.22). Retention interval and retention-vs-transfer did not moderate. Rule for a lesson store: interleave lessons from classes that are easy to confuse; block lessons when one block shows a readable rule (a24).

### 4.6 In-context vs in-weight learning (a24, c07)

```
if the task has an easy rule:   in-context learning solves it from a block  -> blocked order wins
else:                           errors flow into weights                      -> interleaved order wins (blocking forgets block A)
```

In the small network, ablating attention to context raised errors and raised retention (b21). Two older LLMs (GPT-3.5, Llama 2 70B) showed the blocking advantage in context (c06); the supplement gives Llama 2 70B chi2 = 10.7, p = 0.001 and GPT-3.5 p = 0.1 (d06). In-context only; no weight updates.

### 4.7 Run-to-run floor and the selection effect (c08, d25, d26)

Chen et al. frame it as follows: an effect is real only if it exceeds the floor of the same recipe re-run. Floor in their setting: 0.019. A pair chosen by search resolves 0.144 vs 0.031 for a pair fixed in advance; 2 of 6 pairs reverse sign between independent runs. About 4 independent runs per endpoint buy resolution back. Implementation:

```
floor = SD over >= 5 reruns of the SAME schema at equal tokens
accept a change only if (mean delta over paired per-item tests) > k * floor, with k fixed in advance
never choose the comparison after seeing the results
```

### 4.8 Agent-memory analogues

- **MemoryBank (c18):** `R = exp(-t/S)`; `S` starts at 1 and rises with each recall. No ablation of the forgetting rule, so it supports nothing about forgetting schedules (critique).
- **TraceRetain (d18):** bounded in-context episode store; success-scored, age-scored, FIFO and unbounded policies. At 50 held-out tasks the policies are not separable (49/50, 48/50, 48/50, 47/50 vs 39/50 for no memory).
- **Faulty memory (d19, d20):** rewriting lessons incrementally is the worst consolidation schedule. Applicability conditions get stripped. Per-task fresh consolidation beat cumulative by 203 ScienceWorld points.
- **Tips (d21):** tips extracted from trajectories help held-out tasks less than the tasks they came from.

## 5. What holds up

### 5.1 Strong

1. **Practice-vs-delayed reversal** replicates across motor skills, prose, maths and categories (a02, a03, a05, a11, a04). The reversal is the key signature: the same condition wins at 5 minutes and loses at 2 days (a05).
2. **Learner misjudgment** replicates, including in a direct preplanned replication with web participants (a13: 71% of 123 chose massing; d = 0.37 vs 0.41 original) and in older adults (a12).
3. **Spacing for verbal recall** is the best supported single effect: 317 experiments (a07), d = 1.1 at the best gap in a 1,350-person study (a08), replicated online (d12).
4. **Interleaving for visual categories and maths:** g = 0.42 over 59 studies (d03); direct replications with N = 288 and N = 276 (a14); a classroom study d = 0.35 vs blocked (a19); a preregistered physics course d = 0.40 and 0.91 on surprise tests (b01).
5. **Seen vs held-out gap in agent lessons** matches the human lesson (d21, K36), though single-source.

### 5.2 Failures and nulls

- **Testing effect:** preregistered Higham 2023 (n = 259) found restudy beat retrieval (0.74 vs 0.63-0.65) when a memory rating was required each trial (d10). Zhao 2023: g = 0.10, BF10 = 0.19 (d11). Two Prolific studies found nothing (b03): F(1,66) = 0.13, p = 0.72 and U = 1773, p = 0.17, with 60-70% attrition and about 14 of 25 planned minutes spent. The authors blame the sample, not the effect. Meta-analytic I-squared is 84%, so the mean hides near-zero cases (a09).
- **Generation effect** was not found in 0 of 7 recall experiments and was a disadvantage in 4 (b05, b06). It appeared only under the old conditions: intentional learning, unlimited time, immediate test, between subjects. This shows difficulty is not one thing.
- **Interleaving on high-stakes exams:** null when students crammed (d = 0.20 and 0.02, b02). Year-long RCT: no average effect on the cumulative test (d28).
- **Interleaving for words and text:** g = -0.39 for words, n.s. for text (d03).
- **Cepeda gap ratios:** inconsistent in the online replication (d12).
- **Spacing in complex tasks:** d = 0.11 and 0.07 (a10).
- **Identification-test confound:** nearly all replications used identification tests, which mix memory and response bias; forced choice still gave dz = 0.43 (a14).
- **a14 data caution:** the paper prints swapped means in the Exp 2 text; use t and dz only (critique).

### 5.3 Moderators

| Moderator | Direction | Source |
|---|---|---|
| Category similarity between classes | more similar helps interleaving (+0.22) | d04 |
| Variation within a class | less variation helps interleaving (-0.17 when within-class similarity is high) | d04 |
| Material type | paintings 0.67 > photographs 0.35 ~ maths 0.34 > text n.s. > words -0.39 | d03 |
| Task complexity | spacing d 0.97 simple vs 0.07-0.11 complex | a10 |
| Rule available in a block | blocked wins | a24 |
| Test format | blocked learners fine if tested blocked | a02 |
| Task needing detection of commonality | massing won | a04 |
| Test delay | restudy wins at 5 min, testing at 2 days; interleaving g larger when items follow at once | a05, d05 |
| Cramming before test | hides interleaving | b02 |
| Feedback | needed for learners to choose testing and for unsuccessful retrieval to help | a15, a16 |
| Learner prior level | gains in lower achievers; high achievers little or none | d28 |
| Rating step each trial | removes testing effect | d10, d11 |

### 5.4 Interventions that worked and did not

**Worked:**
- Showing separated test results plus theory moved a majority away from the blocking belief (b18, abstract).
- Guided hints rather than answers: d = 1.14 (c22); GPT Tutor removed the exam loss (c19).
- Attempt before AI: d = 1.54 (d29).
- Interleaved retrieval quizzing in class: d = 0.71 vs not quizzed (a19).
- Self-testing is chosen by learners only after feedback (a16).

**Did not work:**
- Telling people the principle (b18, Exps 3-5; modest).
- Contrastive LLM design: highest mental demand, d = 0.74, p = 0.080 (c22).
- Unrestricted LLM help: exam -0.054 (c19).
- Fixed vs AI-guided pretesting made no difference (d29).

## 6. Language models

Everything here is by analogy to the human claim, except where noted.

### 6.1 Direct LLM versions of the human effects

**In-context order of examples.**
- Russin et al. (PNAS 2025; a24, b20, c06, d06). GPT-3.5 and Llama 2 70B showed the blocking advantage on a rule-governed task; on a rotated, ruleless task both failed (p < 10^-3). Human reference: blocking d = 0.47 for rule-like categories, interleaving d = 0.33 without a rule. Immediate generalisation, not a delayed test.
- Acta Psychologica 2025 (c26, abstract only): interleaving helped GPT-4o-mini and Llama 3.1, DeepSeek-V3 was less sensitive to sequence; spacing effects differed from humans; models showed metacognitive illusions (preferred the weaker schedule) or chose at random when asked which schedule is better. No numbers.
- Liu et al. 2024 (d07, reconstructed): easy-to-hard demonstration order beats random by about +9% on instruction-tuned models and hurts base models by -7.16%; immediate.

**Spacing in context.**
- Kang et al. 2025 (d01, reconstructed; K21): repeats placed at a distance beat massed or single exposure; sweet spot 100-400 steps (1-4 segment lengths) in a Markov-chain task; gradient-based continual learning showed no such spot.
- Janik 2024 (c04, c05; figures only): repeated facts separated by text are recalled better; permuted repeats slightly better than verbatim; related distractor lists hurt more than neutral filler. Models show primacy and recency (Pythia lacks recency).

**Weight training with spaced scheduling.**
- Atreya et al. 2026 (SRT; c01-c03). TinyLlama-1.1B Wikipedia: old accuracy base 54.3, naive continual pre-training 11.7, uniform replay 25.2, perplexity-prioritised 27.4, SRT 49.0; new accuracy 17.0 (naive), 38.8 (prioritised), 20.0 (SRT). Llama-3.2-3B-Instruct: old base 50.2, naive 43.0, uniform 46.2, SRT 51.6; new 42.4. Gap SRT over uniform: 23.8 points at 1.1B, 5.4 at 3B, so it shrinks with scale. Uniform replay hurt reasoning: BBH 8.4, GSM8K 6.8 (base GSM8K 77.6); SRT held MMLU 57.8, BBH 52.6, GSM8K 76.7, PIQA 74.3. Bootstrap SD about 2 points. Perplexity is the recall signal; this is not a delayed test of a harder condition.
- Prakriya et al. (LFR; a26): up-weights blocks that are being forgotten, claims 5-19% of tokens; the comparison to Pythia involves different data and does not separate spacing from hard-example selection.

**Order in fine-tuning.**
- Chen et al. 2026 (c08, c09): see 4.7. Most order effects fall inside the noise floor. Scoring only the last-trained skill hides the interleaving benefit; scoring both skills gives +0.0483 (6 of 6 pairs), 76% of it less forgetting of the first-trained skill. With conflicting answer conventions in the pool, arrangement matters a lot (-0.268, -0.443 vs -0.005 control; Qwen3-8B -0.0875 in 5 of 5 seeds), and writing the convention into the input switches it off (K30).
- Curricula: Zhang et al. (c10): 200+ models, baseline reached with 18-45% fewer steps, up to 3.5% sustained gain, depending on the metric. Elgaar and Amiri (c11): effects larger for small models and smaller at scale. Mordig et al. (c12): no robust easy-to-hard advantage for SFT or RL on synthetic deductive tasks. Campos 2021 (b28, abstract): no clear gain. Contested (K31).

**Repetition and variety in training.**
- Muennighoff et al. (c13): up to 4 repeated epochs cost almost nothing; the value of repeated tokens decays with a learned constant of about 15 repetitions (a decay constant, not a literal half-life). This is repetition, not spacing.
- Xu et al. 2026 (c14): masked-input regularisation worth about 1.3x unique data.
- Allen-Zhu and Li (c16): without augmentation, extraction accuracy goes to about 0% even when facts are seen. Lin et al. (c17): paraphrase, self-quiz and association before training: 66.25% vs 7.42% base on a Wikipedia SimpleQA subset (+313% relative over vanilla fine-tuning); FinanceBench 26% (+160%). Strategies are bundled; self-testing alone is not isolated. Zucchet et al. (c15): a plateau before knowledge emerges; imbalance shortens it but slows later acquisition.

### 6.2 Agent memory and skills (held-out scoring)

- **SkillsBench (d08):** self-authored skills -8.1, -11.3, -11.5 pp; curated +18.2 to +24.8 pp on three harnesses (87 tasks). The abstract reports +16.6 pp curated over 18 configurations (33.9 to 50.5), so the harness figures are not the global average. The authors say the deficit mixes content quality with creator-solver interference.
- **d09 (reconstructed line):** abstraction memory trails raw-trajectory memory on held-out tasks (49.0 vs 53.5 over nine settings, per K22). The "7 of 9 settings" detail was not found; do not use it.
- **TraceRetain (d18):** held-out ALFWorld, gpt-5-mini, 50 tasks: success-scored 49/50 and 48/50, FIFO 48/50, unbounded 47/50, none 39/50. Wilson intervals overlap for all memory policies. Single run per policy. Under 75% distractor writes, FIFO precision at 5 falls from 15.8% to 3.8% while the success-scored policy stays 16.9% to 16.6%.
- **Faulty memory (d19, d20):** GPT-5.4 failed 54% of ARC-AGI problems it solved without memory, after consolidating. Episodic-retaining agents had about 2x the accuracy of forced consolidation. ALFWorld Qwen3.5-27B: 19/48 none, 37/48 at stage 168, 24/48 at stage 169. WebShop AWM: 0.64 at 8 examples, 0.20 at 128 (equal to none). The cumulative store had about 5x over-generalised and 20x useless entries (LLM judge). Single seed; the author says the work may be incomplete.
- **IBM tips (d21):** AppWorld held-out: +3.6 pp task goal completion, +14.3 pp scenario goal; dev partition +12.3 / +26.3; train +4.4 / +10.0; hardest tasks +28.5 pp. GPT-4.1 only. No per-tip correlation.
- **Ferraz et al. (d22, abstract):** retrieval plus fine-tuning generalises to unseen tasks even when stored experience includes failed attempts.
- **SeqMem-Eval (d23) and Hu et al. (d24):** could not be read; they are the next sources for per-memory utility and backward transfer.

### 6.3 Humans using LLMs (the best-measured "performance misleads" case)

- Bastani et al. PNAS 2025 (c19, b22, b23): nearly 1,000 students; see section 3. Students did not perceive the harm. Randomised by class, one school, GPT-4, a few sessions; a PNAS correction notice and a design critique exist (not read).
- Fan et al. 2024 (c21): N = 117; essay up, knowledge and transfer flat; "metacognitive laziness" is the authors' reading.
- Kosmyna et al. 2025 (c23, b26): N = 54, 18 per group, 18 did session 4; LLM users under-engaged and could not quote their essays. EEG interpretation is debated.
- Eleftheriou et al. 2026 (c22): see section 3.
- Kestin et al. 2025 (b24): AI tutor median post-score 4.5 (N = 142) vs 3.5 in class (N = 174); immediate test only, so it cannot separate learning from performance.
- Struggle First (d29) and Akgun and Toker 2024 (d13: N = 61, reported d = 8.59 that does not match its own means; do not use that d).
- Clegg et al. 2024 (b30, abstract): richer VR training raised confidence, not recognition performance.

### 6.4 Can an LLM judge which condition will work later?

- Huff and Ulakci 2024 (c24): human JOL predicted later memory (B = 0.104, CI 0.005 to 0.202, N = 78); GPT-3.5, GPT-4-turbo and GPT-4o did not (all CIs include zero; B = 0.044, 0.016, 0.027). Scope: LLMs predicting human memory, not their own.
- Moran and Whiting 2026 (d16): verbalised confidence is a weak signal of capability once consensus items are removed (20 models, 6 benchmarks).
- Beyond Confidence 2026 (d32): verbalised confidence is overoptimistic across 12 LLMs and 38 tasks; effort appraisals match or beat it.
- Prompt predictability (d33, snippets): trained predictors do not transfer; hidden-state probe near chance.
- Cao et al. 2026 (c25): a metacognitive harness raised pooled accuracy 48.3 to 56.9 with Claude Sonnet-4.6 using a pre-solve feeling-of-knowing and post-solve judgment; the gain is a bundle of retry, aggregation and context management, not the signal alone. Not used as evidence for desirable difficulties.
- No study asks an LLM which of two schemas will do better later (K25).

### 6.5 Does the difficulty reverse for weaker models?

- Khan 2025 (d14): constrained prompts help gpt-4o (97 vs 93) but not gpt-5 (94.00 vs 96.36 on full GSM8K, one researcher). Harness Recession (d15, not opened): scaffolds help weak receivers and can turn negative (51 of 59 predicted signs, per K20).
- Li et al. 2024 (d30): self-reflection helps most when the model is unlikely to be right first; helps on TruthfulQA, hurts on HotpotQA without external feedback.
- Li et al. 2025 (d31): explicit chain of thought lowers instruction following across 15 models; selective reasoning recovers much of the loss.
- Nigerian RCT (d28): gains concentrated in lower achievers.
- Net: the "match difficulty to the learner" rule has indirect support; the S0 gate by baseline pass rate is a hypothesis (K20, contested).

### 6.6 Noise

Single-run pass@1 spreads 2.2-6.0 pp with SD above 1.5 pp at temperature 0 (60,000 SWE-Bench-Verified trajectories, 3 models, 2 scaffolds; d25). Trajectories diverge within the first few percent of tokens. The best strategy wins only 77% of head-to-head runs over 30 trials (d26). Practitioner floor: 3 seeds, 5 or more for strong claims (d27, snippet). A gain of 2-3 pp from one run can be noise. This matters because, with practice gain misleading, we need small delayed effects measured against a floor.

### 6.7 One more

PACIT (b27, abstract only): having the model judge whether an example is correct before answering, inspired by desirable difficulty, gave up to +9.16 ROUGE-L in-domain and +3.14 out-of-domain over in-context instruction tuning. ROUGE-L is an immediate surface metric; no check that difficulty drives the gain.

## 7. What our agent should take

Status: **[E]** established, **[S]** single-source, **[C]** contested. Schema parts: G guardrail, S state, O operator, memory = section 5 of the schema. Evidence ids in brackets; claim ids in parentheses.

### Add now (established)

1. **G3 / S9, score on delayed fresh problems with no helper.** When we judge a lesson, a prompt or a schema change, the quick pass rate on the problems it was written from is not the score. Use pass rate on held-out problems after a gap of other tasks, with the aid removed. Schema G3 already says "something the answer was not fitted to"; this extends it from single answers to the lessons and schema changes themselves. **[E]** human reversal (a02, a03, a05, a11, a04; K01); same direction for AI help (c19, c21; K15). Agent-side seen-vs-held-out evidence is **[S]** (d21; K36).
2. **S9 / memory, never admit a lesson on the run that wrote it.** A self-authored lesson is trusted only after held-out gain. Self-authored skills fell 8.1 to 11.5 pp while curated ones rose 18.2 to 24.8 pp. This is consistent with the schema's rule that a lesson becomes trusted only after it helps on two different problems. **[E]** (d08, d09, d19; K22).
3. **G7 / measurement protocol, rerun and use a floor.** Before any schema comparison, measure our own run-to-run SD over at least 5 reruns at equal tokens. Use paired per-item tests. Fix the comparison in advance; a pair picked after seeing results overstates (0.144 vs 0.031). **[E]** (d25, d26, d27; K39); selection effect **[S]** (c08; K35).
4. **G1 / S9, do not decide by the model's or the designer's feel for which variant is better.** Learners, old and young, prefer the easy condition (71-78%, a04, a13, a12); LLM verbalised confidence and judgments of learning are weak (c24, d16, d32). Decide by measurement. **[E]** (K02, K25).
5. **Logging, S9.** Record for every lesson both its pass rate on its source task and its gain on held-out tasks, so the per-lesson relation can be computed (needed for A05.04-U2 in UNKNOWNS.md). Cheap and needs no schema change. **[S]** rationale (d21; K36).
6. **Do not add "make it harder" as a free-standing element.** Generation (0 of 7), easy-to-hard ordering (contested) and extra difficulty in complex tasks (d = 0.07) can fail. Each candidate difficulty enters the schema only through its own test. **[E]** that "difficulty" is not one thing (b05, a10; K12, K04, K31).

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Lesson order in memory: interleaved vs blocked by problem class, scored on a delayed held-out set | S2 / memory | **[C]** for LLMs; **[E]** for humans | a04, d03, a24, c08, c09; K09, K14, K27, K29 |
| T2 | Attempt-first then lesson (or failing output) vs lesson-first | S5 | **[S]** (humans only) | a15, d29, d13; K08, K24, K41 |
| T3 | Revisit a stored lesson after 1, 2, 4, 8 intervening tasks vs back-to-back; SM-2-like state vs most-failed-first vs uniform | memory / S9 | **[S]** weights; **[E]** small in-context | c01, d01, d18; K21, K28, K38 |
| T4 | Elaborative storage: restate, self-quiz, link to two older lessons before storing, vs verbatim | memory / S9 | **[E]** for weights, untested in context | c16, c17; K32 |
| T5 | Keep raw episodes plus per-lesson trigger condition; consolidate on demand, not every time | memory / G7 | **[S]** | d19, d20, d18; K30, K37 |
| T6 | Hint-first from the agent's own memory vs answer-first | G3 / S5 | **[C]** | c19, c22; K33 |
| T7 | S0 gate: extra difficulty only on classes with a high plain pass rate | S0 | **[C]** | d14, d28, d30, d31; K20, K40 |
| T8 | Easy-to-hard vs random vs hard-first order of in-context examples | S2 | **[C]** | d07, c10-c12; K23, K31 |
| T9 | Model forecasts which of two schemas will do better, compared with measurement | G1 | **[E]** that LLM judgments are weak; the pair test is new | c24, d16, d32; K25 |
| T10 | Retrieval from memory (reconstruct the lesson closed-book) vs rereading it in context | S4 / memory | **[C]** | a09, d10, d11; K05, K06 |
| T11 | Cramming analogue: all lessons loaded at once vs distributed across the run | memory | **[C]** | b02, d28; K11, K40 |

Each T item maps to a row in UNKNOWNS.md. Nothing in "Test first" enters SCHEMA.md until its test passes.

## 8. Concrete tests on our bench

General design for all tests: two or more arms at **equal tokens** (setup, lesson-writing and retrieval counted, per G7); items drawn from ARC-like and BrainTeaser-like suites, split into a **learning stream** and a **held-out set** that no arm sees until the end; a **gap** of N unrelated tasks (N = 0, 5, 20) between learning and the held-out test; at least 5 reruns per arm; paired per-item analysis; the effect must exceed the measured floor (test T0).

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T0 floor | one fixed schema, held-out set of 100+ items | same arm, 5-10 reruns, new seeds | SD of pass rate; paired SD | SD around 1.5 pp or more (d25); sets the minimum detectable effect; Chen needed about 4 runs per endpoint |
| T1 order | ARC-like items grouped by transform type; BrainTeaser items grouped by trick type | (a) lessons stored and shown blocked by class, (b) interleaved across classes, (c) interleaved with class tags | held-out pass rate after gap N = 20; also the immediate pass rate on the learning stream, to count rank reversals | By the Brunmair moderators: interleaved better on ARC-like (similar classes, varied exemplars); blocked or null on word-like BrainTeaser; immediate rate favours blocked. Effect likely 1-5 pp, near the floor |
| T2 attempt-first | any item with a check | (a) agent attempts, sees its failing output, then the lesson; (b) lesson first | held-out pass rate; tokens | Human d up to 1.54 in simple tasks; expect small, larger on harder items (d29 Study 3) |
| T3 revisit | learning stream of 100+ tasks, lessons accrue | (a) back-to-back repeat, (b) revisit after 1, 2, 4, 8 tasks, (c) SM-2-like state, (d) most-failed-first, (e) uniform | old-task and new-task held-out pass rate (both, as SRT trades them) | In-context sweet spot might sit at several intervening tasks (d01). TraceRetain could not separate policies at 50 tasks (d18), so use 200 or more held-out tasks |
| T4 elaboration | lessons from the stream | (a) store verbatim, (b) restate + self-quiz + link two older lessons, equal total tokens | held-out transfer, split into near copies and far transfer | Weights: very large (66 vs 7 percent); in-context: unknown; expect help on far transfer, cost in tokens |
| T5 episodes | stream with conflicting conventions across classes | (a) consolidate every time, (b) raw episodes, (c) lesson + trigger condition, consolidate on demand | held-out pass rate; count of lessons flagged over-general by a fixed judge | Faulty-memory: consolidate-every-time worst; tagging should remove order sensitivity |
| T6 hint-first | items with a check | (a) answer-first, (b) hint from own memory only | held-out pass rate unassisted | Bastani: hints avoid the loss (-0.004 vs -0.054) |
| T7 gate | classes split by plain pass rate (high vs low) | difficulty on all, on high only, on none | held-out pass rate by class | Benefit on high-pass classes, loss on low-pass (expertise reversal) |
| T8 example order | in-context few-shot items | easy-to-hard, hard-first, random | accuracy on held-out items, immediate and after a gap | Liu: about +9% instruction-tuned; contested at scale; expect within floor |
| T9 forecast | pairs of schema variants | model ranks A vs B; then both measured | rate at which the model prefers the easier variant; rank agreement with measured delayed result | Human-like bias toward the easy variant; Huff: no reliable prediction |
| T10 closed-book | lessons | read lesson, vs reconstruct it from memory then check | held-out pass rate | Human g about 0.5 with high heterogeneity; far transfer weaker (d = 0.40) |
| T11 cramming | long runs | all lessons in context vs distributed across the run | held-out pass rate; tokens | Samani and Pan: cramming hides the benefit |

Reading rules: report the immediate pass rate and the delayed held-out pass rate side by side for every arm. Count **rank reversals** (arms whose order flips between the two). A reversal is the human signature (a05, a03). If immediate and delayed ranks agree on all tests, the caution adds little for our agent.

## 9. What does not transfer, and why

- **Time-based forgetting.** Human spacing works because memory decays and retrieval strengthens it. An in-context lesson does not decay; it is either in the prompt or not. Weight training does forget, but spaced replay trades plasticity for retention (new accuracy 20.0 vs 38.8, c02) and the gap shrinks with scale (23.8 to 5.4, c01). Muennighoff (c13): up to 4 repeated epochs cost almost nothing, so human-style massed vs spaced differences are not obvious in pretraining.
- **Effort and motivation.** Human difficulty works through effort, engagement and encoding depth, and through failing to persist (online nulls come with 40-70% attrition; b03). An LLM cannot be bored. Attrition and cramming explanations do not apply directly.
- **Metacognitive illusion.** The human bias toward easy conditions is a learner's fluency error. An LLM-based tuning loop has a different bias: it favours whatever scored best in its last run (c08: a pair picked by search resolves 0.144 vs 0.031 fixed). We should treat noise, not fluency, as the main trap.
- **Retrieval practice itself.** Retrieval from memory has no direct counterpart when the lesson sits in the prompt. "Reconstruct then check" is the nearest analogue, and it costs tokens (T10).
- **Generation and attempting.** Attempting before the answer helps humans partly through retrieval effort and error correction (a15). An LLM's attempt may be correlated and shallow (G4), and a rewrite of its own failed attempt is the self-reflection pattern the schema already rejects without real output (section 4b). The version that stays is "attempt, see real failing output, then fix".
- **Interleaving evidence base.** Most human tests use identification of paintings, maths formulas, college students. Our items are puzzles with possibly low category similarity. Brunmair's moderators predict where it helps but not by how much for LLMs (K27, unmeasured).
- **The reversal itself has never been shown for an LLM agent** (K34). Treat every machine result here as a proxy.
- **Human-with-LLM studies measure humans.** Bastani, Fan, Kosmyna, Eleftheriou: the learner is a person. What transfers is the evaluation lesson (do not judge by assisted performance), not the learning mechanism.
- **Weight-training results** (SRT, LFR, Chen) concern gradient updates. Our agent learns without training, so they inform memory design only by analogy.
- **Difficulty from the task vs difficulty added to the practice.** "Harder" in the human studies is a manipulation of practice conditions at equal content. Harder problems are a different thing (complex-task spacing d = 0.07, a10).

## 10. Open questions

1. Does any harder, interleaved or attempt-first condition for an LLM produce a delayed held-out gain at equal tokens (K34)? No study found.
2. Does the immediate pass rate of a stored lesson predict its delayed benefit per lesson? Only aggregate (d21); per-lesson rank correlation unmeasured (K36).
3. Is attempt-before-lesson better than lesson-first for an LLM? Humans only (d29, d13).
4. What revisit gap, in tasks or tokens, best resurfaces a lesson, and does an SM-2-like state beat most-failed-first and uniform retrieval for in-context memory? TraceRetain could not separate policies at 50 tasks (K38).
5. What is our own run-to-run floor, and how many reruns separate two schemas (K39)?
6. Do Brunmair's moderators predict LLM order effects on ARC-like vs brainteaser items (K27)?
7. Does an LLM show the human bias toward easy conditions when asked which schema will do better later (K25)? Indirect evidence only.
8. Does desirable difficulty reverse for weaker models or complex tasks (expertise reversal; A08.04), and can S0 choose by baseline pass rate (K20)?
9. Do conflicting conventions make order matter in an agent memory, and does tagging switch it off (K30)?
10. Are there large, preregistered multi-site replications of interleaving and testing after 2020? Only Higham, Zhao, Rogers, Donenfeld, Sigayret and a year-long field RCT found (d28).
11. How much of the SRT result (c01) is the interval schedule vs the borrowed perplexity signal? No ablation.
12. Is "hardest-first" ever a valid proxy for "desirable"? Evidence says no for replay (c02) but ordering results are mixed (K31).
13. SeqMem-Eval (d23) and Hu et al. (d24) were unreadable; they may give per-memory backward-transfer numbers.
14. Does the published critique of the Bastani design (c19 limits) change the size of the exam loss?

## 11. Sources

[V] = opened and read this run (full text or page text, including abstract pages where the whole point was in the abstract). [M] = snippet, abstract only or second-hand. (r) = reconstructed index line; re-open before reuse.

**Founding and theory**
- [V] Bjork (1994) Memory and metamemory considerations in the training of human beings. https://gwern.net/doc/psychology/spaced-repetition/1994-bjork.pdf (a01)
- [M] Bjork and Bjork (1992) A new theory of disuse; second-hand via Rowland 2014. https://gwern.net/doc/psychology/spaced-repetition/2014-rowland.pdf (a28)
- [V] Shea and Morgan (1979) Contextual interference effects. https://gwern.net/doc/psychology/spaced-repetition/1979-shea.pdf (a02)
- [V] Simon and Bjork (2001) Metacognition in motor learning. https://gwern.net/doc/psychology/spaced-repetition/2001-simon.pdf (a03)
- [V] Landauer and Bjork (1978) Optimum rehearsal patterns and name learning (exact figures not extracted). https://gwern.net/doc/psychology/spaced-repetition/1978-landauer.pdf (a18)
- [V] Bjork, Dunlosky and Kornell (2013) Self-regulated learning. https://gwern.net/doc/psychology/spaced-repetition/2013-bjork.pdf (a17)
- [M] Soderstrom and Bjork (2015) Learning versus performance. https://doi.org/10.1177/1745691615569000 (b16)
- [V] de Bruin (2023) Dealing with desirable difficulties. https://pmc.ncbi.nlm.nih.gov/articles/PMC10858853/ (b09)
- [V] Javadi group (2025) Does difficulty moderate learning? QJEP. https://pmc.ncbi.nlm.nih.gov/articles/PMC12432286/ (a22)
- [V] Hattie and Donoghue (2016) Learning strategies. https://pmc.ncbi.nlm.nih.gov/articles/PMC6380372/ (b07, b08)

**Spacing and testing**
- [V] Cepeda et al. (2006) Distributed practice in verbal recall tasks. https://gwern.net/doc/psychology/spaced-repetition/2006-cepeda.pdf (a07, b10)
- [V] Cepeda et al. (2008) Spacing effects in learning: a temporal ridgeline. https://gwern.net/doc/psychology/spaced-repetition/2008-cepeda.pdf (a08)
- [V] Donovan and Radosevich (1999) Distribution of practice meta-analysis. https://gwern.net/doc/psychology/spaced-repetition/1999-donovan.pdf (a10)
- [V] Rogers, Nakata and Chiu (2025) Optimizing distributed practice online (r). https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/optimizing-distributed-practice-online-a-conceptual-replication-of-cepeda-et-al-2009/C833408A4C3BAD939CA39EA734423BB7 (d12)
- [V] Roediger and Karpicke (2006) Test-enhanced learning. https://learninglab.psych.purdue.edu/downloads/2006/2006_Roediger_Karpicke_PsychSci.pdf (a05)
- [V] Karpicke and Roediger (2008) The critical importance of retrieval. https://learninglab.psych.purdue.edu/downloads/2008/2008_Karpicke_Roediger_Science.pdf (a06)
- [V] Rowland (2014) Testing vs restudy meta-analysis. https://gwern.net/doc/psychology/spaced-repetition/2014-rowland.pdf (a09, b12)
- [M] Yang et al. (2021) Testing boosts classroom learning. https://doi.org/10.1037/bul0000309 (b13)
- [M] Pan and Rickard (2018) Transfer of test-enhanced learning. https://doi.org/10.1037/bul0000151 (b14)
- [M] Chan, Meissner and Davis (2018) Retrieval potentiates new learning. https://doi.org/10.1037/bul0000166 (b15)
- [V] Sigayret et al. (2026) Testing the testing effect on Prolific. https://pmc.ncbi.nlm.nih.gov/articles/PMC12894256/ (b03, b04)
- [V] Higham et al. (2023) Spaced retrieval practice: can restudying trump retrieval? (r). https://doi.org/10.1007/s10648-023-09809-2 (d10)
- [V] Zhao et al. (2023) Judgments of learning following retrieval practice (r). https://pmc.ncbi.nlm.nih.gov/articles/PMC10607076/ (d11)
- [V] Kornell, Hays and Bjork (2009) Unsuccessful retrieval attempts. http://web.williams.edu/Psychology/Faculty/Kornell/Publications/Kornell.Hays.Bjork.2009.pdf (a15, b19)
- [V] Kornell and Son (2009) Learners' choices and beliefs about self-testing. http://web.williams.edu/Psychology/Faculty/Kornell/Publications/Kornell.Son.2009.pdf (a16)
- [V] Settles and Meeder (2016) Half-life regression. https://aclanthology.org/P16-1174.pdf (a20)
- [V] Text generation conceptual replication (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12185794/ (b05, b06)

**Interleaving**
- [V] Kornell and Bjork (2008) Is spacing the enemy of induction? http://web.williams.edu/Psychology/Faculty/Kornell/Publications/Kornell.Bjork.2008a.pdf (a04, b17)
- [V] Kornell, Castel, Eich and Bjork (2010) Spacing as the friend of both memory and induction. http://web.williams.edu/Psychology/Faculty/Kornell/Publications/Kornell.Castel.Eich.Bjork.2010.pdf (a12)
- [V] Verkoeijen and Bouwmeester (2014) Is spacing really the friend of induction? https://pmc.ncbi.nlm.nih.gov/articles/PMC3978334/ (a13)
- [V] Donenfeld, Kaldy and Blaser (2026) Interleaving without response bias. https://pmc.ncbi.nlm.nih.gov/articles/PMC13380076/ (a14; a27, a29 second-hand)
- [V] Brunmair and Richter (2019) Similarity matters (full text via the Wurzburg preprint; d03-d05 are (r) lines). https://www.psychologie.uni-wuerzburg.de/fileadmin/06020400/2019/Brunmair_Richter_in_press__2019_META-ANALYSIS_OF_INTERLEAVED_LEARNING.pdf (b11 abstract: https://doi.org/10.1037/bul0000209)
- [M] Yan, Bjork and Bjork (2016) On the difficulty of mending metacognitive illusions. https://doi.org/10.1037/xge0000177 (a29, b18)
- [V] Sana and Yan (2022) Interleaving retrieval practice promotes science learning. https://gwern.net/doc/psychology/spaced-repetition/2022-sana.pdf (a19)
- [V] Samani and Pan (2021) Interleaved practice in undergraduate physics. https://pmc.ncbi.nlm.nih.gov/articles/PMC8589969/ (b01, b02)
- [V] Rohrer and Taylor (2007) The shuffling of mathematics problems. https://gwern.net/doc/psychology/spaced-repetition/2007-rohrer.pdf (a11)
- [V] Ge et al. (2021) Interleaving effect, an eye-tracking study. https://pmc.ncbi.nlm.nih.gov/articles/PMC8718114/ (a21)
- [M] Kremer, Gray-Lobe, de Laat and van der Haar (2023, rev. 2026) Full-year interleaving math program in Nigeria, NBER w31853 (abstract level). https://nber.org/papers/w31853 (d28)

**Humans and AI help**
- [V] Bastani et al. (2025) Generative AI without guardrails can harm learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635/ (b22, b23, c19, c20)
- [V] Fan et al. (2024) Beware of metacognitive laziness. https://arxiv.org/abs/2412.09315 (c21; abstract-level F values)
- [V] Kosmyna et al. (2025) Your brain on ChatGPT. https://arxiv.org/abs/2506.08872 (c23; b26 abstract page)
- [V] Eleftheriou, Pallis and Constantinides (2026) Confidence without competence. https://arxiv.org/abs/2604.09444 (c22; abstract-level)
- [V] Kestin et al. (2025) AI tutoring outperforms in-class active learning. https://pmc.ncbi.nlm.nih.gov/articles/PMC12179260/ (b24)
- [V] Struggle First, Prompt Later (2025). https://arxiv.org/html/2504.10249v1 (d29)
- [V] Akgun and Toker (2024) Pretesting with conversational AI (r). https://arxiv.org/abs/2412.13487 (d13)
- [V] Critical-thinking paradox in generative-AI-integrated learning (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13521781/ (b25)
- [M] Clegg et al. (2024) Multimedia and immersive training. https://arxiv.org/abs/2407.05504 (b30)

**LLM and machine learning**
- [V] Russin, Pavlick and Frank (2025) In-context and in-weight learning. https://arxiv.org/abs/2402.08674 (a24, b20, b21, d06 (r)); CCN 2024 version https://2024.ccneuro.org/pdf/367_Paper_authored_CCN2024_authored.pdf (c06, c07). One source.
- [M] Interleaved and spaced practice in morphological learning, Acta Psychologica 2025. https://doi.org/10.1016/j.actpsy.2025.105518 (c26)
- [V] Liu et al. (2024) Let's learn step by step (r). https://arxiv.org/abs/2402.10738 (d07)
- [V] Kang et al. (2025) In-context learning can perform continual learning like humans (r). https://arxiv.org/abs/2509.22764 (d01)
- [V] Janik (2024) Aspects of human memory and LLMs. https://arxiv.org/abs/2311.03839 (c04, c05)
- [V] Atreya et al. (2026) When to review: spaced repetition for continual pre-training. https://arxiv.org/abs/2608.17530 (a25, c01-c03, d02 (r))
- [V] Prakriya et al. (2024/25) LFR pedagogy. https://arxiv.org/abs/2409.06131 (a26)
- [V] Chen et al. (2026) The Free-Recipe Limit. https://arxiv.org/abs/2609.26160 (c08, c09)
- [V] Zhang et al. (2026) Beyond random sampling. https://arxiv.org/abs/2506.11300 (c10)
- [V] Elgaar and Amiri (2026) Curriculum learning for LLM pretraining. https://arxiv.org/abs/2601.21698 (c11)
- [V] Mordig et al. (2026) Rethinking easy-to-hard. https://arxiv.org/abs/2603.27226 (c12)
- [M] Campos (2021) Curriculum learning for language modeling. https://arxiv.org/abs/2108.02170 (b28)
- [V] Muennighoff et al. (2023) Scaling data-constrained language models. https://arxiv.org/abs/2305.16264 (c13; b29 abstract)
- [V] Xu et al. (2026) Data-constrained pretraining regularization. https://arxiv.org/abs/2606.06888 (c14)
- [V] Zucchet et al. (2025) How do language models learn facts? https://arxiv.org/abs/2503.21676 (c15)
- [V] Allen-Zhu and Li (2023) Physics of language models 3.1. https://arxiv.org/abs/2309.14316 (c16)
- [V] Lin et al. (2025) Learning facts at scale with active reading. https://arxiv.org/abs/2508.09494 (c17)
- [V] Zhong et al. (2023) MemoryBank. https://arxiv.org/abs/2305.10250 (c18)
- [M] Xue et al. (2024) PACIT. https://arxiv.org/abs/2310.00901 (b27)
- [V] Song, Kim and Kim (2026) Minimal recurrent network for interleaved practice (quantitative tables not extracted). https://pmc.ncbi.nlm.nih.gov/articles/PMC13022130/ (a23)

**Agent memory and skills**
- [V] SkillsBench (2026). https://arxiv.org/abs/2602.12670 (d08 (r))
- [V] Wang, Panaganti and Zhou (2026) More memory, worse agents (r). https://arxiv.org/abs/2610.27406 (d09)
- [V] Reddy (2026) TraceRetain. https://arxiv.org/html/2606.29178v1 (d18)
- [V] Zhang et al. (2026) Useful memories become faulty. https://arxiv.org/abs/2605.12978 (d19); blog https://dylanzsz.github.io/faulty-memory/ (d20)
- [V] Fang et al. (2026) Trajectory-informed memory generation (IBM). https://arxiv.org/html/2603.10600 (d21)
- [M] Ferraz et al. (2026) Retrieval-augmented agents. https://arxiv.org/abs/2603.18272 (d22; abstract)
- [M] Dong et al. (2026) SeqMem-Eval. https://arxiv.org/abs/2605.15384 (d23; unreadable)
- [M] Hu, Long and Wang (2026) When continual learning moves to memory. https://arxiv.org/abs/2604.27003 (d24; unreadable)

**LLM metacognition, reflection and noise**
- [V] Huff and Ulakci (2024) Judgment of learning: a human ability beyond generative AI. https://arxiv.org/abs/2410.13392 (c24)
- [V] Moran and Whiting (2026) LLMs show no signs of individuated metacognition (r). https://arxiv.org/abs/2605.24299 (d16)
- [V] Beyond Confidence (2026) (abstract). https://arxiv.org/abs/2605.07806 (d32)
- [M] Prompt predictability studies. https://arxiv.org/pdf/2501.18883 (d33)
- [V] Cao et al. (2026) LLMs know when they know. https://arxiv.org/abs/2605.14186 (c25; not used as evidence)
- [V] Khan (2025) The prompting inversion (r). https://arxiv.org/abs/2510.22251 (d14)
- [M] Alim et al. (2026) Harness recession. https://neurips.cc/virtual/2026/171325 (d15)
- [V] Li, Yang and Ettinger (2024) When hindsight is not 20/20 (abstract). https://arxiv.org/abs/2404.09129 (d30)
- [V] Li et al. (2025) When thinking fails (abstract). https://arxiv.org/abs/2505.11423 (d31)
- [V] Bjarnason, Silva and Monperrus (2026) On randomness in agentic evals (abstract-level). https://arxiv.org/abs/2602.07150 (d25)
- [V] Potamitis et al. (2026) ReasonBENCH (abstract page). https://arxiv.org/abs/2512.07795 (d26)
- [M] MLflow practitioner guide on benchmarking agents. https://mlflow.org/articles/tags/how-to-benchmark-ai-agents/ (d27)
- [M] Winona State talk (2026), not used. https://openriver.winona.edu/rca/2026/AIsymposium2026/5 (c27)
