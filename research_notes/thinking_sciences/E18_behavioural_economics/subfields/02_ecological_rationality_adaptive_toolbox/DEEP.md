# Ecological rationality, adaptive toolbox: deep document

*Subfield E18.02. Built from evidence_a-d.jsonl (101 lines, ids a01-d19), claims.jsonl (K01-K26) and critique.md in this folder. Ids in brackets point to those files. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Corrections from critique.md are applied: the 2018 Cognitive Psychology paper is Parpart, Jones and Love (not the author list in b01-b03); the individual-level r = -0.03 in b10 is estimated versus actual recognition validity, not adherence versus validity; Claude 3.5 Sonnet showed no chain-of-thought harm on implicit learning (65.9 vs 67.7).*

## 1. What it is

Ecological rationality asks one question. In which environments does a given decision rule work well, and in which does it fail? It does not ask whether a rule is rational in general. The adaptive toolbox is the set of simple rules that a mind (or an agent) can pick from. Each rule is built from three parts: how to search for information, when to stop searching, and how to decide from what was found.

The core claims:

- Fast and frugal rules use few cues and little computation. Examples: take-the-best (TTB), tallying (count the cues for each option), the recognition heuristic, fast-and-frugal trees (FFTs), 1/N allocation, satisficing.
- A simple rule can match or beat a complex one out of sample. The reason is bias versus variance. With little or noisy data, a complex model fits noise. A simple rule is biased but stable.
- The match between rule and environment decides the result. A rule that wins in one environment loses in another. "Less is more" is a claim about specific environment features (few training cases, redundant cues, non-compensatory weights, high noise), not a law.
- Frugal does not mean fast in every sense. Counting cue look-ups is not counting seconds or tokens.

Why it matters for our agent. The schema has a direct mode (S0 chooses it when the class's plain pass rate is high) and a class record that S0 reads. This field says when a short, ordered, stop-early routine is enough, how many past cases are needed before a learned rule beats the full routine, and when deliberation backfires. It also supplies a vocabulary for cheap tests of an environment (redundancy, cue validity, compensatory or not).

What the field has not done: no study prompts an LLM with take-the-best, tallying or an FFT and measures accuracy at equal tokens [c25, d19, K18]. The LLM link is by analogy. Section 6 lists what is measured.

## 2. History and theories in depth

**Simon, Selten, satisficing.** Simon's bounded rationality said minds satisfice: take the first option that meets an aspiration level. Selten's aspiration adaptation theory supplies the formal base [a23, not opened]. The toolbox programme turned this into testable, computable rules.

**Take The Best and the ABC programme (1996-1999).** Gigerenzer and Goldstein (1996) defined TTB [a01]. Step 1: if only one option is recognised, choose it. Step 2: rank cues by validity (share of pairs where the cue points the right way). Step 3: look up cues in order and stop at the first one that discriminates. Step 4: choose the option it favours. Task: which of two of 83 German cities with more than 100,000 people is larger; 9 binary cues plus recognition. Competitors were Minimalist (random cue order), Take The Last (last discriminating cue first), tallying, weighted tallying, unit-weight and weighted linear models, and multiple regression. The book "Simple Heuristics That Make Us Smart" (1999) widened this to many heuristics [a23, not opened]. Czerlinski, Gigerenzer and Goldstein (1999) ran 20 data sets with cross-validation [a07, a27].

**Recognition heuristic (RH) and less-is-more (1996-2011).** Goldstein's serendipitous result: US students scored slightly higher on German cities (60% on Detroit vs Milwaukee for Americans, 90% for Germans, the other way round for German cities) [a12, b06]. This became the less-is-more effect: knowing less can give higher accuracy, if recognition validity beats knowledge validity. The BBC replication was informal (65% of New York listeners vs 82% of London listeners).

**The critique wave (2004-2014).** Newell and Shanks (2004) said people use more than recognition [b27, not opened]. Glockner and Broder (2011, 2014) used strategy classification with choices, times and confidence and found mostly compensatory use [b16, b17, d03, d04]. Pohl (2011) audited less-is-more and found it mostly a simulation result [b14]. The founders replied with boundary conditions: RH is for memory-based inference with high recognition validity, not for cues shown on screen [a13, a14].

**Statistical reframing (2006-2018).** Schmitt and Martignon proved that finding the best cue order is hard [a17]. Hogarth and Karelaia mapped the environments where TTB is exact and where hybrids win [b04, b05]. Simsek and Buckmann (2015) ran 63 data sets and found simple heuristics learn fast but do not beat regression on average [a18, c14]. Parpart, Jones and Love (2018) showed heuristics are the limit of an infinitely strong Bayesian prior; an intermediate prior beats both extremes [b01-b03]. Brighton and Gigerenzer (2015, "the bias bias") argue researchers overweight bias and underweight variance [b23, not opened].

**Trees and field cases.** Fast-and-frugal trees (Green and Mehr 1997; Martignon et al. 2008; Phillips et al. 2017) are one-cue-per-level decision trees with an exit at each level [b20, c15, c16]. Field cases: hiatus rule, bail decisions, stroke bedside exam [b21].

**LLM era (2022-2026).** LLM work uses the word "heuristic" in four other senses: Kahneman-Tversky bias tests [c07, c08, c10], game play [c06], search guides [b29], and mechanistic "bag of heuristics" [c24]. The relevant strand is different: when does extra deliberation hurt [c19, c20, c22, c23, a24], and cost-saving cascades that stop at the first sufficient answer [c17, d16-d18]. Bogdan (2026) is the only paper that links these to TTB, by theory [a25, c03].

**Competing views.** (1) Heuristics-and-biases: departures from logic are errors (separate subfield). (2) Compensatory process models (parallel constraint satisfaction, evidence accumulation) fit people better than the toolbox when cues are shown [b15, d03]. (3) The Bayesian view: heuristics are strong-prior limits, so the real driver is inductive bias, not simplicity [b03].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| TTB, weighted tallying, regression and tallying tie on German cities | Mean proportion correct: TTB .658, weighted tallying .658, regression .657, tallying .656, Minimalist .647, Take The Last .645, weighted linear .623, unit-weight linear .621. At 100% cue knowledge TTB .691, regression .694. 500 simulated individuals per cell. Regression was in-sample on full data | Gigerenzer & Goldstein 1996 Table 2 [a02, d01] | Established (parity, not victory) |
| TTB looks up few cues | TTB 5.91, Minimalist 5.64, Take The Last 5.29 values on average (range 2 to 20); integration rules look up all | GG96 [a03, d02] | Established |
| Linear models lose only because recognition is not built in | Imposing the recognition principle removed the gap (.62 vs .658) | GG96 [a05] | Established, one environment |
| Out-of-sample on the city task | Regression 71.9%, TTB 72.2%, unit-weight 71.4% over 10,000 random half-splits (fit: 74.3 / 74.2 / 74.1) | Wikipedia summary of Czerlinski 1999 [a27] | Secondary; "citation needed" tags |
| 20 data sets, cross-validated | TTB looks up 2.4 cues on average, regression and tallying 7.7; TTB at least as accurate as regression on average | Czerlinski et al. via Gigerenzer 2012 [a07] | Established, founders' sets |
| 63 data sets, 50% training | Logistic regression .747, CART .746, greedy lexicographic .743, TTB .743, single cue .734, tallying .725 | Simsek & Buckmann 2015 [a18, c14] | Established; TTB 0.4 behind regression |
| Cue ordering | Best .758, greedy .756, validity .742 (fitting); validity within 1.6 points of best; validity loses most with continuous cues | Simsek & Buckmann [a19]; Schmitt & Martignon [a17] | Established |
| Learning speed | One training pair gives at least 83% of the best reachable accuracy for a single-cue rule; tallying best at very small samples | Simsek & Buckmann [c14] | Established |
| Crossover with data size | House prices (231 pairs): TTB beats regression at 20 training pairs (about 9%), reverses at 100 (about 43%) | Parpart, Jones & Love 2018 [b01] | Established |
| Intermediate prior beats both extremes | Half-ridge best on all 20 data sets at 10, 20, 115 comparisons; with unknown cue direction TTB beats regression in 18 of 20 sets at 10-20 cases, tallying in 11 of 20 | Parpart et al. [b01, b02, b03] | Established (simulation) |
| TTB exact only when non-compensatory | 100% with non-compensatory weights and right order; equal weight 86-89% there; with error TTB beats a dominance baseline by only 3-4 points (baseline avg 68%; 84/77/71% for 3/4/5 cues) | Hogarth & Karelaia [b04, b05] | Established (theory + simulation) |
| Recognition adherence tracks validity | 11 environments: r = 0.64, p = 0.03. Examples: NHL validity .87, 96%; US cities .90, 95%; disease frequency .62/.60, 64%/71% | Pachur et al. 2011; GG 2011 [b07, b10] | Established for people |
| Recognition forecasts sports | Wimbledon 2004: recognition 72% vs ATP Entry 66%, Champions Race 68%, seedings 69% | GG 2011 [b08] | Single sport |
| Noncompensatory use of recognition is lab-dependent | 92% stayed with recognition (G&G 2002); median 97%, mean 82%, 17 of 28 (Richter & Spath); 64% aggregate, 23% always (Newell & Fernandez); 62-76% (Hilbig) | Pachur et al. [b11] | Contested |
| Strategy classification, cues shown | N = 80: PCS 62 (77.5%), TTB 12 (15%), RHe 4, RHe/TTB 2. TTB users time contrast significant for 25% | Glockner & Broder 2011 [b16, d03, d04] | Contested |
| Cues retrieved from memory | PCS 62%, RH or TTB 32% (up from 22.5%); PCS predicted 73% of choices, RH/TTB 71% | Glockner & Broder 2014 [b17] | Contested |
| Less-is-more from recognition | Predicted frequent but small (about .01-.02); max theoretical 26.3%; observed 0.3% and 3.5% in two studies | Katsikopoulos 2010; Pohl 2011 [a15, b14] | Contested |
| Frugal is not fast | Told to use TTB at a 2,000 ms deadline: slower and less compliant than tallying in Exp 1 (N=179); reversed in Exp 2 (N=173) | Bobadilla-Suarez & Love 2018 [b18] | Single source |
| Dawes: equal weights | Libby loan example: officers 74%, their models 72%, proper models about 78%, one ratio 80% (48 of 60) | Dawes 1979 [d05] | Established |
| 1/N portfolios | 14 optimising models vs 1/N on 7 data sets; mean-variance needs about 3,000 months (25 assets), 6,000 (50 assets) | DeMiguel et al. 2009 [a21, b24] | Single source, abstract-level |
| FFTs match standard learners | Held-out balanced accuracy SVM .86, FFT .83, logistic .83, random forest .83; about 2 cues; 10 author-chosen sets | Phillips et al. 2017 [c15] | Established (small sets) |
| FFT field cases | Chest pain: doctors sent about 90% to ICU, about 25% had infarction; tree nearly halved false alarms. Bail: tree 92%/85% vs weighted additive 86%/73%. Hiatus rule 83% vs Pareto/NBD 75%; stroke exam 100% sensitivity | Gigerenzer & Gaissmaier 2011 [b20, b21] | Single studies |
| CoT helps maths and symbols only | 110 papers, 1,218 comparisons, 264 datasets: symbolic +14.2, math +12.3, logic +6.9; 56.9 vs 45.5 in those three, 56.8 vs 56.1 elsewhere; 95% of MMLU gain on "=" questions | Sprague et al. 2024 [c19] | Established |
| CoT hurts where deliberation hurts people | Implicit learning: GPT-4o 87.5 vs 64.4, Claude 3 Opus 70.7 vs 62.7, Llama 3.1 70B 65.9 vs 57.1; o1-preview 57.7 vs GPT-4o 94.0 (36.3 gap). Face recognition 64.0 vs 51.2 and 44.0 vs 29.6. Claude 3.5 Sonnet 65.9 vs 67.7 (no harm) | Liu et al. 2024 [c20] | Established |
| Unanswerable (Knightian) items | 7,875 responses; direct 77.1%, longer reasoning 62.1-66.5%; drop 17.3 points (CI 7.7 to 25.5); controls -1.73 | Bogdan 2026 [c04, c05] | Single-author preprint |
| Direction replicated by two other labs | Abstention below answering: beta 0.96 [0.87, 1.06]; larger in reasoning models, beta 1.67; efficiency reward +14.7% abstention, 44% shorter chains | Tsvilodub 2026; Fan 2025 [d14, d15] | Established (direction) |
| Inverse scaling in test-time compute | Opus 4 near 100% to about 85-90% (Misleading Math); R1 about 70% to about 30% with five distractors | Gema et al. 2025 [c22] | Single paper, values read from plots |
| Overthinking | o1-like models use 1,953% more tokens; self-training cut tokens 35-49% at near-equal accuracy (MATH500 2407.9 to 1330.7 = -44.7%) | Chen et al. 2024 [c23] | Single source |
| Cascades | FrugalGPT up to 98% cheaper; 0.872 vs 0.857 at $6.5 vs $33.1; MoT cascade 0.929 vs 0.931 at 40% cost; UCCI -31% cost at F1 0.91; cascade routing +8% / +12% | Chen 2023; Yue 2024; Kotte 2026; Dekoninck 2025 [c17, d17, d18, d16] | Established |
| Routing between modes | MATH-500 free routing .78 at 2,811 tokens vs base .79 at 4,796; NoThink-only .66; MMLU-Pro router 58.57% vs 48.33% at -48.5% tokens | Kassenaar 2026; Wang 2025 [d13, d12] | Single-source each |
| Unit-weight LLM checklist | Founders F0.5 .102 vs elastic net .080 (not separable); gap shrinks with positives, rho -0.50 and -0.38, knee near 100 | Griffin et al. 2026 [d06, d07] | Single source |
| Popularity as LLM recognition cue | Accuracy correlation about 0.4 (davinci-003), about 0.1 (GPT-Neo 1.3B); popularity gate 46.5% (+5.3), davinci-003 retrieved for 40% | Mallen 2023 [d09] | Established for old models |
| LLM advisors act on one reason | Risk tolerance carries 57-88% of weight; GPT-4o equities FC .780 | Ross & Lo 2026 [c01, c02] | Single source, no ground truth |
| Equal-weight pooling | 12-LLM median Brier .20 vs human crowd .19; GPT-4 alone .15 | Schoenegger 2024 [d08] | Single source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 Take The Best.** Inputs: two options A and B, a list of binary cues with a stored validity v_i = (right calls) / (right calls + wrong calls) over past discriminating pairs, and a recognition flag.
```
if recognised(A) xor recognised(B): return the recognised one
for cue in sorted(cues, key=validity, reverse=True):
    a, b = value(A, cue), value(B, cue)
    if a != b: return the option with the positive value
return guess
```
Cost: one look-up per cue until the first difference (2 to 20 in the city task). Learning: count validity from training pairs. Plain validity ordering is within 1.6 points of the best order [a19]. Conditional-validity ordering (which accounts for cue dependence) is costlier and lost the TTB edge [a09].

**4.2 Tallying and unit-weight rules.** Score each option by the count of positive cues (all weights 1). Weighted tallying multiplies by validity. Dawes: with right signs and positively correlated predictors, equal weights lose little to fitted weights, and beat random weights on average, by mathematics [d05]. Engineer note: unit weights need standardised or binary inputs.

**4.3 Minimalist and Take The Last.** Random cue order, or last-successful cue first. They lose about one point to TTB [a04]. Why they work: in redundant environments cues point the same way. Redundancy (mean cue correlation) is a measurable class feature (mean 0.31 across the 20 sets [b01]).

**4.4 Recognition heuristic.** If exactly one option is recognised, pick it. Works when recognition validity alpha > 0.5. Less-is-more arises when alpha exceeds knowledge validity beta and recognition is partial. Non-compensatory means each weight exceeds the sum of all lower weights (1, 1/2, 1/4, ...) [a14]. Reliance rises with measured validity [b10] and falls when the recognition source is artificial or the criterion is known [b12].

**4.5 Fast-and-frugal tree.** An ordered list of cues; each has a binary question and an exit on one answer; the last cue has two exits.
```
for cue in tree: if cue.fires(): return cue.exit_decision
return default
```
Build from data: rank cues by a criterion (FFTrees "fan" uses about 1.85 cues on average; zig-zag 4.85; max 6.5) [c15]. Fan trees were slower to build (median 2.61 s and 15.93 s vs 0.59 s). Use balanced accuracy for rare outcomes.

**4.6 Why simple wins: bias and variance.** Error = bias squared + variance + noise. Few cases or high noise: variance dominates, so use a biased stable rule. More cases: bias dominates, so use the flexible rule. The crossover sits at tens to a hundred cases: 20 vs 100 pairs for house prices [b01]; about 100 positives for LLM-feature checklists [d07]. In the LLM pipeline the unit is positives, not total cases.

**4.7 Strong-prior view.** Treat a heuristic as a model with a prior of infinite strength (all weight on one cue, or on equal weights). Intermediate strength (shrink toward a default, let data move the weights) beat both extremes on all 20 sets [b01-b03]. Engineer note: partial pooling toward a class default, not a hard stop.

**4.8 Environment structure map (what decides the rule).** From Hogarth and Karelaia and Gigerenzer and Gaissmaier [b04, b05, b22]:
- Non-compensatory weights and a correct order: TTB is exact.
- Compensatory weights: equal-weight or hybrid rules win.
- Cue noise: all rules sink toward 50-70%; TTB barely beats dominance.
- High redundancy, moderate to high uncertainty: one-reason rules do best.
- Dependent cues: TTB tends to beat tallying but not always [a22, unopened].

**4.9 Cascade as a stop-at-sufficient tree.** A cascade queries a cheap model first and stops if a score passes a threshold. The learned rule in FrugalGPT: query GPT-J, stop at score 0.96 or above; else J1-Large, stop at 0.37 or above; else GPT-4 [c17]. The shape matches an FFT with models as cues. The reading is ours, not the authors'. Quality of the sufficiency signal decides the gain [d16]; calibration (ECE 0.12 to 0.03) lets thresholds be chosen from data [d18].

**4.10 Mode routing.** A classifier or RL-learned first token picks NoThink, Short or Long [d12, d13]. Gains depend on varied difficulty; with uniform difficulty a two-mode router collapsed to one mode on Countdown [d13].

**4.11 Free-energy view (theory only).** Bogdan: when the agent is unsure how precise its own evidence is (heavy-tailed precision prior), stopping after k cues is optimal; with descending dominance this equals TTB, with uniform validity it equals tallying; 26,696 numeric comparisons, 0 mismatches. Predicts that longer chain of thought hurts on items with no determinate answer [c03, a25]. Single author, unreviewed; do not build on it.

## 5. What holds up

**Holds.**
- Simple rules are about as good as regression out of sample, at a fraction of the look-ups. All four independent comparisons agree on the size: within about one point [a02, a07, a18, a27, d01].
- Small data favours simple. Crossover at 20 vs 100 pairs [b01]; knee near 100 positives in an LLM pipeline [d07]. The Chater et al. (2003) result that TTB loses to a neural net flipped when Brighton used cross-validation [a08].
- Equal weights are robust (Dawes; Gigerenzer tallying; RRF; model pooling) [d05, a02, d06, d08].
- Recognition adherence rises with recognition validity (r = .64 over 11 environments) [b10].
- CoT helps symbolic tasks and hurts some others (Sprague; Liu; Gema; Bogdan; Tsvilodub; Fan) [c19, c20, c22, a24, d14, d15].
- Cascades save cost: up to 98% in the best case, 30-60% outside it (FrugalGPT, MoT 40% of GPT-4 cost, UCCI -31%) [c17, d17, d18].

**Failures and corrections.**
- "TTB beats regression" is not stable. +0.3 on the city task out of sample, about 0 on the 20 sets, -0.4 on 63 sets at 50% training [a28]. In GG96 regression was in-sample and given more information than other rules [d01].
- Almost all positive TTB evidence is the founders' own simulations on the same 20 sets, many small [critique].
- Non-compensatory use of recognition is contested: 23% to 97% depending on lab and design [b11]; when cues are shown most people are best fit by a compensatory model (77.5%) [d03]; even classified TTB users do not show the predicted times (25% significant) [d04].
- Less-is-more from recognition: mostly simulation; predicted effect .01-.02; observed 0.3-3.5% in two studies; max theory 26.3% [a15, b14].
- The Parpart half-ridge model, which assumes known cue directions, shows no less-is-more; the effect appears only when direction is unknown [b01, b02].
- Frugal is not fast: TTB under time pressure was slower in one study and faster in another [b18].
- DeMiguel (1/N) and Dana and Dawes were not opened; Nelson 2018 found a partial replication that differs in size [b25, b24].

**Moderators.**
- Training size, noise, cue redundancy, compensatory structure, cue-order quality, cue type (binary vs continuous), whether cues are shown or retrieved, recognition validity, and whether the recognition source is real or induced.
- For LLMs: task class (symbolic vs not), item answerability, model strength (Bogdan: strong in mid-to-large, directional in two frontier models, absent or reversed in the weakest), and whether the model is a reasoning model.

**Interventions that worked.**
- Short-reasoning self-training: tokens down 35-49%, accuracy unchanged on one base model [c23].
- Efficiency reward: abstention +14.7%, chains 44% shorter on 4B and 8B models [d14].
- Few-shot examples largely removed the Gema regression effect [c22].
- Popularity gate for retrieval: +5.3 points over non-adaptive [d09].
- Learned mode routing: -41% to -76% tokens at near-equal accuracy where difficulty varies [d12, d13].

**Interventions that did not work or failed to carry.**
- Web search only partly reduced one-input collapse: cash -65%, tax-advantaged -45%, equities +16%; search used in 0% of profiles when merely available, 0.7% when encouraged, 99.9% when required [c02].
- Router gains vanished when difficulty was uniform and a misroute was costly (NoThink-only 12 points lower on MATH-500) [d13].
- Pooling 12 LLMs did not beat the best single model (GPT-4 .15 vs crowd .20) [d08].
- Suppressing CoT helped nothing in ChatGPT-3.5 (no change) and cost a little in GPT-4 (95% to 88%) [c09].

## 6. Language models

No study tests TTB, tallying, recognition or FFTs as prompts with equal-token arms (about 12 arXiv queries, one web search) [c25, d19]. The evidence is indirect, in six groups.

**6.1 When extra reasoning hurts (the "less is more" analogue).**
- Sprague et al. 2024 (110 papers, 264 datasets): gains only on symbolic (+14.2), math (+12.3), logic (+6.9). Elsewhere 56.8 vs 56.1. Up to 95% of the MMLU gain was on "=" questions. About 32% (59) of knowledge, soft-reasoning and commonsense sets showed a significant gain [c19].
- Liu et al. 2024: on implicit statistical learning, GPT-4o 87.5 vs 64.4; Claude 3 Opus 70.7 vs 62.7; Llama 3.1 70B 65.9 vs 57.1 (direct vs CoT); o1-preview 57.7 vs 94.0 for GPT-4o direct (440-problem subset). Face recognition 64.0 vs 51.2 and 44.0 vs 29.6. Rounds to learn exceptions: GPT-4o 2.9 vs 12.5; Claude 3.5 Sonnet 2.3 vs 6.4. Three of six tasks dropped significantly; Claude 3.5 Sonnet showed no harm on implicit learning (65.9 vs 67.7, p = .969). On weighted-feature choice CoT mostly helped strong models: Claude 3.5 Sonnet 81% vs 95% at the widest gap, Claude 3 Opus 72% vs 84%, GPT-4o 80% vs 87%; Llama 3.1 70B collapsed (42% vs 6%) [c20, c21].
- Gema et al. 2025: Opus 4 from near 100% to about 85-90% (Misleading Math, 2,500 questions); R1 from about 70% to about 30% with five distractors; Sonnet 4 safe answers about 60% to 47%. Five failure modes, family-specific. Few-shot examples removed the regression effect. Values read from plots [c22].
- Bogdan 2026 (pre-registered): 7 models, 7,875 responses, 45 items. High-uncertainty accuracy 77.1% direct, 62.1-66.5% with longer reasoning; drop 17.3 points (CI 7.7 to 25.5); controls -1.73; Qwen2.5-14B fell almost 40 points. Frontier models (claude-sonnet-4-5, gpt-4o) directional only. Regime was assigned by item category (disclosed deviation); scoring is abstention [a24, c04, c05].
- Independent direction replication: reasoning models write chains at least as long on unanswerable items and abstain worse (beta 0.96; 1.67 for reasoning vs instruct) [d14]; missing-premise questions produce much longer answers and rare abstention in reasoning models [d15]. QwQ-32B MiP-Formula: 453 tokens, 20% abstain.
- Hagendorff et al. 2023: CRT correct 5% (davinci-003), 59% (ChatGPT-3.5), 96% (GPT-4), humans 38%. Trap answers 80%, 15%, 0%, humans 55%. Step-by-step prompting lifted davinci-003 from 5% to 28%. These are old models; trap answers vanish in newer ones [c08, c09]. Owned by the heuristics-and-biases subfield.

**6.2 Overthinking and length.** o1-like models used 1,953% more tokens than conventional ones. QwQ on "2+3": 13 solutions, 901 tokens, first solution 39 tokens (4.3%). After self-training for short reasoning: ASDIV 96.9 to 96.8 (-48.6% tokens), GSM8K 94.8 to 96.0 (-46.1%), MATH500 93.0 to 92.8 (-44.7%; the paper's intro says 48.6%, its table gives 44.7%), GPQA 59.6 to 59.1 (-35.4%), AIME24 46.7 to 43.3 (-45.6%) [c23].

**6.3 Cascades and routing (stop-at-sufficient).**
- FrugalGPT: up to 98% cost cut at equal accuracy, or +4% at equal cost; HEADLINES 0.872 vs GPT-4 0.857, $6.5 vs $33.1; about 6% of cases the cheap model was right where GPT-4 was wrong [c17, c18].
- MoT cascade: 0.929 vs 0.931 at 40% of GPT-4 cost on six sets; CREPE 0.885 vs 0.871 at 47% [d17].
- UCCI: -31% cost (CI 27-35%) at micro-F1 0.91 on 75,000 queries, ECE 0.12 to 0.03 [d18].
- Cascade routing: up to +8% (cascading), +12% (routing) over prior methods; needs a good quality estimator [d16].
- Routers: vLLM semantic router 58.57% at 887.5 tokens vs 48.33% at 1,722.1 (baseline mode unclear); 1.5B learned router MATH-500 .78 at 2,811 tokens vs .79 at 4,796, GSM8K -76% tokens [d12, d13].
- All use 2023-2026 small or mid models. No 2026 frontier-price replication.

**6.4 Recognition-like signals in LLMs.** Popularity predicts accuracy (r about 0.4, davinci-003; about 0.1, GPT-Neo 1.3B) and gating retrieval on it beat always retrieving [d09]. Sparse-autoencoder directions mark known entities and causally steer refusal vs hallucination [d10]. Familiarity predicts belief stability across 21 LLMs [d11]. No study pits familiarity against contradicting cues.

**6.5 One-reason behaviour without being asked.** Frontier LLM advisors put 57-88% of weight on risk tolerance; 89-100% of allocations were multiples of 5 without search; the GPT-5.4 family collapsed less [c01, c02]. Nothing shows this is wrong, because there is no ground truth.

**6.6 Equal weights.** RRF vote: F0.5 .102 vs elastic net .080 on startup founders (positives < 2%, Npos = 158), not separable at founder level; Phase I trials F1 .655 vs .641; gap falls with positives (rho -0.50, p = 1.8e-6; -0.38, p = 1.1e-4), knee near 100 [d06, d07]. Silicon crowd: median of 12 LLMs Brier .20 vs human crowd .19 (t(60) = 0.19, p = .85); GPT-4 .15 [d08].

**6.7 LLM-generated priors.** Jagadish et al. used Claude-v2 to write thousands of tasks and meta-learned a small transformer. The model used one-reason rules when cue ranking was known (Gini of weights 0.3399), equal weights when only direction was known (0.0743), a weighted sum when neither (0.1794). Fit to human choices 0.7299 with two attributes, 0.6284 with four. Llama-3.1 70B matched Claude-v2 as generator; GPT-4 wrote only simple rules [c11, c12, c13].

**6.8 Other uses of "heuristic".** Suri 2024 (anchoring, conjunction 18/20 vs humans 10/20, endowment 92.5% vs 85%, GPT-3.5, 20-40 trials per cell) [c07]; Zheng 2025 (outcome-based play: 36 of 90 humans vs 63 of 126 model runs) [c06]; Binz and Schulz 2023 (GPT-3 gave the intuitive wrong answer on all three CRT items; no directed exploration) [c10]; Nikankin 2025 (arithmetic as a bag of heuristics) [c24]; Borro 2025 (+22 points task success, search guide sense) [b29]. These do not test our topic.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory = section 5 of SCHEMA.md. Note: claims.jsonl uses the tag "O1" loosely for "ordered checks"; it is not the schema's O1 Specialise. Here ordered checks go to S0 or S4.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | Make the class record carry, per check or per cue, its past hit rate, and order direct-mode checks by plain hit rate. Do not build a conditional ordering. | S0 / memory | [E] | K05; a17, a19, a09 |
| A2 | Combine candidate scores or checks by count (equal weights) in code until the class record holds enough labelled cases; keep weights fixed until about 100 labelled positives. | G5 / S7 / memory | [E] | K09, K02; a07, a18, b01, d05, d06, d07 |
| A3 | State the crossover rule in memory: trust a learned rule over the plain routine only after enough cases; below that use the simple one. Expect a crossover between 20 and 100 cases. | memory | [E] | K02; b01, a09, a28, d07 |
| A4 | Shrink toward the class default but let later checks override (partial pooling) rather than a hard stop on the first signal. | S0 / memory | [E] | K03; b01, b03, a18 |
| A5 | Let S0 read environment features (checks that are decisive vs many weak, redundancy, noise) and route accordingly. No fixed policy. | S0 | [E] | K04; b04, b05, a14, a22 |
| A6 | Gate deliberation by task class: use a cheap maths/symbolic yes-no test; chain of thought only for symbolic, math, logic items; direct for the rest. | S0 / G11 | [E] | K13; c19, c20, c08, c09 |
| A7 | Add an early answerability check before any long chain. Count tokens spent on unanswerable items. | G11 / S0 | [E] | K26, K12; d14, d15, a24, c20 |
| A8 | Report accuracy margins at one decimal and tokens used. Never write that a short rule beats regression or the full routine; write parity or the measured gap. | G7 / logging | [E] | K22, K01; d01, a28 |
| A9 | Cheap-first cascade: a direct answer with a code-computed sufficiency signal (agreement across short attempts, not verbal confidence) before escalating to the full scaffold. 4b forbids stopping on verbal confidence; keep it. | S0 / G12 | [E] | K15; c17, d16-d18, d17 |
| A10 | Measure the agent's own recognition validity per class (known vs unknown entity or problem) and log it in the class record. Use as a signal for retrieval or mode only; do not yet let it override other cues. | S0 / memory | [E] for validity | K24, K06; d09, d10, b10 |

A9 note: the cascade evidence is established for cost at near-equal accuracy; it depends on a calibrated signal. Our G4 says agreement among samples from one model is only a hint, so A9 must be tested on our bench before it governs S0 (see test T4). It is listed here because the direction is established, not the threshold.

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Take-the-best style prompt (ordered checks, stop at the first decisive one) vs weighted-sum prompt vs plain direct, at equal tokens on cue-based judgement items. | S0 direct mode | No LLM evidence | K18; c25, d19 |
| T2 | Fast-and-frugal tree built from the S0 class record (1 to 3 cues with exits) vs the full routine on held-out items. | S0 / S4 | [E] for humans and ML, none for agents | K11; c15, c16, b20, b21 |
| T3 | Hard-stop vs soft-weight use of familiarity (seen-before, known entity) when other cues contradict. | S0 | [C] | K07; b09, b11, b16, b17, d03, d04 |
| T4 | Cheap class router for direct vs deliberate mode: measure routing accuracy needed for a net token gain. | S0 / G12 | [S] | K25; d12, d13, d16 |
| T5 | Bogdan size of the CoT penalty on Knightian items with frontier models. | G11 | [S] direction [E] | K12; a24, c04, d14, d15 |
| T6 | Cap reasoning length on easy S0-class items. | G11 | [S] | K14; c23 |
| T7 | Learned weights vs count of checks as the class record grows (10, 30, 100). | memory | [S] | K23; d06, d07 |
| T8 | Single-input ablation: does the agent ignore later-listed inputs? | G | [S] | K16; c01, c02 |
| T9 | Equal split of token budget across sub-checks vs a fitted split. | G12 | [S], analogy | K10; a21, b24 |
| T10 | LLM-generated environment priors to set cue-order defaults. | memory | [S] | K21; c11-c13 |

Not to add: recognition-based less-is-more (K08, [C], small, mostly simulation); bias lists from the heuristics subfield (K17); the free-energy theory as design basis (K20); the claim that frugality is faster (K19, [S]).

## 8. Concrete tests on our bench

All arms at equal tokens per item (total tokens including setup, G7). Report per-item tokens, accuracy, and seeds. Use at least 3 seeds and a paired comparison.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Paired-comparison and cue-based judgement items where cues are given (city size, product choice, yes/no triage with 4 to 6 listed cues) | (a) plain direct, (b) TTB prompt with ordered checks and stop at first decisive, (c) weighted-sum prompt, (d) short CoT | Accuracy, tokens per item | Expect parity within 1 to 2 points between (b) and (c) on non-compensatory items; (b) cheaper in tokens; (c) better on compensatory items. Llama-class models may collapse on (c) as in c21 |
| T2 | S0-class items with a stored class record of 20, 50, 100 past cases | (a) full routine, (b) FFT (1 to 3 checks), (c) logistic or count of checks | Held-out balanced accuracy, tokens | FFT within 3 points of the routine at far fewer tokens at 20 cases; routine ahead at 100 (K02, c15) |
| T3 | Entity-comparison items where the model recognises one entity and a shown cue contradicts | (a) hard rule: pick the recognised, (b) soft weight, (c) plain | Accuracy, adherence rate | Hard rule wins when recognition validity is above about .8; soft wins when contradicting cues are reliable (K07) |
| T4 | Mixed pool: maths/symbolic items and non-symbolic ones (MMLU-Pro style) | (a) always CoT, (b) never CoT, (c) router by cheap class test, (d) oracle routing | Accuracy per token; routing accuracy; accuracy lost per misroute | (c) within 1 point of (a) at 40% or more fewer tokens if routing accuracy exceeds about 90% (misroute loss L = 12 points per item on MATH-500, d13). Break-even derived here: m x L must stay below the accuracy value of tokens saved |
| T5 | 45 or more matched pairs, unanswerable (underspecified, missing premise, Knightian) vs answerable | (a) direct, (b) short CoT, (c) long CoT, (d) answerability check first then CoT | Correct abstention rate, tokens | Direct and (d) above long CoT by about 10 points or more on unanswerable items, no drop on answerable ones |
| T6 | Easy items from our bench (plain pass rate above .9) | (a) uncapped reasoning, (b) cap at 100 to 300 tokens | Accuracy per token | Same accuracy at about half the tokens (c23) |
| T7 | Items with checkable features where an LLM writes yes/no checks | (a) unit-weight count, (b) fitted weights on 10, 30, 100 labelled cases | F0.5 or balanced accuracy | Count leads below about 100 positives, tie above (d07) |
| T8 | Multi-input judgement items (profile to allocation or triage) | (a) full input, (b) each input removed in turn | Share of output variance by input | Detect one-reason collapse; compare with the ground truth where it exists |
| T9 | Sub-check pipeline with 4 to 6 checks | (a) equal token split, (b) split by fitted check value | Accuracy at fixed total | Parity; equal split cheaper to build |
| T10 | Ordering of direct-mode checks | (a) plain hit-rate order, (b) greedy conditional order, (c) random | Accuracy and tokens | Within 1.6 points (a19); no gain from greedy once cost of learning is counted |

## 9. What does not transfer, and why

- Cue look-ups are not tokens. TTB's saving is memory look-ups [a03, d02]. An LLM reads the whole prompt at once; stopping early saves only generated tokens.
- The founders' evidence is simulation on 20 sets they chose. It says nothing about agent items.
- Recognition has a different meaning in an LLM. A person recognises a name from experience. A model has trained weights; popularity predicts accuracy (r about 0.4 davinci-003) but the model's own known-entity signal is internal [d09, d10]. No data on use against contradicting cues.
- Human-only process claims (time, confidence, non-compensatory use) do not apply: our agent has no response-time or confidence process to match [d04].
- Time pressure results (frugal is not fast) apply to people [b18].
- Old-model LLM results (CRT, GPT-3 anchoring) lose the intuitive trap answers in newer models [c08, c07, c10]. Do not cite them as current.
- CoT-harm studies use synthetic or narrow tasks, and 2024-2025 models [c20, c22, a24]. Claude 3.5 Sonnet showed no harm on implicit learning.
- Cascade savings use mid-2023 to 2026 small or mid models and prices. Best-case 98% is not a general number [c17, d16].
- Free-energy theory is single-author, unreviewed. The mapping to LLM internals is by behavioural proxy only [c03, a25].
- 1/N finance results are an analogy for an equal token split; sources are abstract-level [a21, b24].
- Human fast-and-frugal trees predict what magistrates do, not what is right [b21]. For our agent the check is the ground truth.
- "Heuristic" in LLM search papers (LLM-A*, hill climbing) is a different sense [b29].
- G1 and G4: doubt only on a signal, and agreement among samples from one model is not independent. Any rule that stops on agreement must be treated as a hint.

## 10. Open questions

1. Does a TTB-style prompt beat weighted-sum and plain direct at equal tokens? No study exists [K18].
2. Where is the crossover for an agent: how many past S0-class cases make a learned stop-early rule better than the full routine? Humans 20-100 cases [b01]; LLM-feature pipeline about 100 positives [d07].
3. How accurate must a cheap class test be to give a net gain from routing? [K25]
4. Does Bogdan's 17.3-point penalty replicate on frontier models with matched unanswerable and answerable items? [K12]
5. Is familiarity a valid cue in an LLM, and does it override other cues? [K24, K07]
6. Does an FFT from an S0 class record match the full routine on held-out items? [K11]
7. Do equal-weight combinations of sampled answers from one model match fitted weights? Pooling of different models did not beat the best one [d08].
8. Independent replication of 1/N (DeMiguel) and of FrugalGPT with 2026 prices. [K10, K15]
9. Dana and Dawes 2004, Brighton and Gigerenzer 2015, Katsikopoulos 2010, Newell and Shanks 2004, Martignon and Hoffrage 2002 are unopened.
10. How should S0 pick among tools? The selection mechanism of the toolbox is only partly specified ("mostly unconscious") [a11].
11. Can LLM-written environment priors (Jagadish) replace hand-set defaults in the class record? [c11-c13]

## 11. Sources

[V] = opened and read this session; [M] = snippet or abstract only (not opened).

Primary and review:
- [V] Gigerenzer & Goldstein (1996) Reasoning the fast and frugal way. https://pure.mpg.de/pubman/item/item_2543502_7/component/file_2561658/GG_Reasoning_1996.pdf ; doi https://doi.org/10.1037/0033-295X.103.4.650
- [V] Gigerenzer (2012) Homo heuristicus: less-is-more effects in adaptive cognition. https://utoronto.scholaris.ca/bitstreams/9765f507-f0fd-4d5f-8f6e-64e30981f2c5/download
- [V] Gigerenzer & Goldstein (2011) The recognition heuristic: a decade of research. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C72D7B4B4DFDB3D1EF7821AC1C0057DF/S1930297500002126a.pdf/the-recognition-heuristic-a-decade-of-research.pdf
- [V] Katsikopoulos (2010) The less-is-more effect: predictions and tests. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A1C8571FB975D397E6BB90EB5B9742C8/S1930297500003491a.pdf/the-less-is-more-effect-predictions-and-tests.pdf
- [V] Beaman, Smith, Frosch & McCloy (2010) Less-is-more effects without the recognition heuristic. https://dlab.sauder.ubc.ca/sjdm/journal/10/rh10/rh10.html
- [V] Schmitt & Martignon (2006) On the accuracy of bounded rationality. https://www.ruhr-uni-bochum.de/lmi/mschmitt/accuracyfrugal.pdf
- [V] Simsek & Buckmann (2015) Learning from small samples. https://proceedings.nips.cc/paper_files/paper/2015/file/94e4451ad23909020c28b26ca3a13cb8-Paper.pdf
- [V] Parpart, Jones & Love (2018) Heuristics as Bayesian inference under extreme priors. https://pmc.ncbi.nlm.nih.gov/articles/PMC5886040/
- [V] Hogarth & Karelaia (2003/2007) Take-the-best and other simple strategies. https://econ-papers.upf.edu/papers/709.pdf
- [V] Pachur, Todd, Gigerenzer, Schooler & Goldstein (2011) The recognition heuristic: a review of theory and tests. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2011.00147/full
- [V] Pohl (2011) On the use of recognition in inferential decision making. https://doi.org/10.1017/S1930297500001388
- [V] Glockner & Broder (2011) Processing of recognition information and additional cues. https://doi.org/10.1017/S1930297500002072
- [V] Glockner & Broder (2014) Cognitive integration of recognition information and additional cues. https://doi.org/10.1017/S1930297500004964
- [V] Bobadilla-Suarez & Love (2018) Fast or frugal, but not both. https://pmc.ncbi.nlm.nih.gov/articles/PMC5708146/
- [V] Gigerenzer & Gaissmaier (2011) Heuristic decision making. https://economics.northwestern.edu/docs/events/nemmers/2018/gigerenzer2.pdf
- [V] Dawes (1979) The robust beauty of improper linear models. https://www.cmu.edu/dietrich/sds/docs/dawes/the-robust-beauty-of-improper-linear-models-in-decision-making.pdf
- [V] Wikipedia: Take-the-best heuristic (secondary). https://en.wikipedia.org/wiki/Take-the-best_heuristic
- [V] Phillips, Neth, Woike & Gaissmaier (2017) FFTrees. https://doi.org/10.1017/S1930297500006239
- [V] Martignon, Erickson & Viale (2022) Transparent, simple and robust fast-and-frugal trees. https://doi.org/10.3389/fhumd.2022.790033
- [M] DeMiguel, Garlappi & Uppal (2009) Optimal versus naive diversification. https://ideas.repec.org/a/oup/rfinst/v22y2009i5p1915-1953.html
- [M] Martignon & Hoffrage (2002) Fast, frugal, and fit. https://refubium.fu-berlin.de/handle/fub188/3204
- [M] Gigerenzer, Todd & ABC group (1999) Simple heuristics that make us smart. https://dbpia.nl.go.kr/book/16560
- [M] Brighton & Gigerenzer (2015) The bias bias. https://doi.org/10.1016/j.jbusres.2015.01.061
- [M] Dana & Dawes (2004); Nelson (2018) thesis. https://ideas.repec.org/a/sae/jedbes/v29y2004i3p317-331.html
- [M] Katsikopoulos, Schooler & Hertwig (2010) The robust beauty of ordinary information. https://doi.org/10.1037/a0020418
- [M] Newell & Shanks (2004) On the role of recognition in decision making. https://doi.org/10.1037/0278-7393.30.4.923

LLM and AI studies:
- [V] Bogdan (2026) Free energy heuristics. https://arxiv.org/abs/2606.15877
- [V] Lin, Hou, Li & Yamada (2026) Why linear models can still work in a complex and changing world. https://arxiv.org/pdf/2610.13404
- [V] Borro et al. (2025) LLMs as common-sense heuristics. https://arxiv.org/abs/2501.18816
- [V] Ross & Lo (2026) One Size Fits None. https://arxiv.org/abs/2604.23837
- [V] Zheng, Zhou & Wang (2025) Beyond Nash Equilibrium. https://arxiv.org/abs/2506.09390
- [V] Suri et al. (2024) Do LLMs show decision heuristics similar to humans. https://arxiv.org/abs/2305.04400
- [V] Hagendorff, Fabi & Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206
- [V] Binz & Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576
- [V] Jagadish et al. (2025) Meta-learning ecological priors from LLMs. https://arxiv.org/abs/2509.00116
- [V] Chen, Zaharia & Zou (2023) FrugalGPT. https://arxiv.org/abs/2305.05176
- [V] Sprague et al. (2024) To CoT or not to CoT. https://arxiv.org/abs/2409.12183
- [V] Liu et al. (2024) Mind your step (by step). https://arxiv.org/abs/2410.21333
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417
- [V] Chen et al. (2024) Do not think that much for 2+3=? https://arxiv.org/abs/2412.21187
- [M] Nikankin et al. (2025) Arithmetic without algorithms. https://arxiv.org/abs/2410.21272
- [V] Griffin et al. (2026) Random Rule Forest. https://arxiv.org/abs/2505.24622
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Mallen et al. (2023) When not to trust language models. https://arxiv.org/abs/2212.10511
- [V] Ferrando et al. (2025) Do I know this entity? https://arxiv.org/abs/2411.14257
- [V] Dies et al. (2026) Epistemic familiarity and belief stability. https://arxiv.org/abs/2511.19166
- [V] Wang et al. (2025) When to reason: semantic router for vLLM. https://arxiv.org/abs/2510.08731
- [V] Kassenaar et al. (2026) Learning when to think. https://arxiv.org/abs/2608.20256
- [V] Tsvilodub et al. (2026) Rewarding efficient reasoning improves abstention. https://arxiv.org/abs/2609.20846
- [V] Fan et al. (2025) Missing premise exacerbates overthinking. https://arxiv.org/abs/2504.06514
- [V] Dekoninck, Baader & Vechev (2025) A unified approach to routing and cascading. https://arxiv.org/abs/2410.10347
- [V] Yue et al. (2024) LLM cascades with mixture of thought representations. https://arxiv.org/abs/2310.03094
- [V] Kotte (2026) UCCI. https://arxiv.org/abs/2605.18796
- [M] Search log (arXiv API and others), 2026-10-26 and 2026-10-27. https://export.arxiv.org/api/query

## Source audit (2026-10-27)

Fresh auditors re-opened the sources of 13 established claims: 6 confirmed as written, 7 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E18.02-K03** (reworded: the sources support less). The half-ridge result (intermediate prior best on all 20 data sets) is against directed tallying and sign-constrained regression, not TTB and unconstrained regression; TTB appears only in an appendix COR analysis (peak usually in the middle), and the two Parpart lines are one paper while Simsek tests no priors. Corrected claim: Parpart et al. (2018) show that tallying and TTB are limits of Bayesian inference under infinitely strong priors; in simulations on the 20 ABC data sets an intermediate-strength prior that uses all cues (half-ridge) beat directed tallying and sign-constrained regression at every training size, and the COR model with a TTB rule usually peaked at intermediate priors (appendix). Strong bias helps, not simplicity itself; this rests on one paper.
- **E18.02-K04** (now single-source: the sources are not independent). b04 and b05 are the same Hogarth and Karelaia paper (full text could not be opened, only abstracts via search confirm TTB effectiveness with 3-5 binary cues, hybrids better in compensatory worlds, and little advantage over a dominance rule under error); a14 only defines non-compensatory and does not test TTB; the only-with-perfect-order phrasing is not checked against the full text.
- **E18.02-K05** (reworded: the sources support less). The .758/.756/.742 (1.6-point) figures are from one earlier German-cities data set cited by Simsek and Buckmann, not 63 real data sets; across the 63 sets validity ordering is described only as very close to greedy except in a handful, and the paper says continuous cues placed first mask ordering differences (relative accuracy of the orderings drops more in the dichotomized versions), the opposite of validity losing most with continuous cues. Corrected claim: Finding the best cue order for a lexicographic rule is hard to approximate (no efficient algorithm within any constant factor unless P differs from NP; Schmitt and Martignon 2006), and a greedy ordering is proven to do better than take-the-best validity ordering. Empirically (Simsek and Buckmann 2015) greedy is identical or very close to the best order on 63 data sets and validity ordering is very close to greedy except in a handful; on the German cities set fitting accuracy was .758 best, .756 greedy, .742 validity (1.6 points).
- **E18.02-K06** (now single-source: the sources are not independent). r = 0.64 (p = .03, 11 environments), Pohl 89% to 75% and the 64%-96% table range check out, but b10 and b12 are the same Pachur et al. paper and Gigerenzer and Goldstein 2011 (b07/a13) share authors with it (the recognition-heuristic group) and report a different correlation (r = .57 across experiments).
- **E18.02-K09** (reworded: the sources support less). GG96 tallying .656 vs regression .657 is not an out-of-sample test (regression was given all Appendix information, more than any competitor), so it cannot support the out-of-sample wording; Schoenegger numbers (Brier .20 vs .19, p=.85; GPT-4 .15), RRF F0.5 .102 vs .080 and Dawes unit-weight robustness hold, though the ensemble aggregate is a median and Dawes full text could not be fully read. Corrected claim: Equal-weight or unit-weight rules predict nearly as well as fitted weights out of sample in social-science data (Dawes 1979: unit weighting is robust) and, per Czerlinski et al. as summarised by Gigerenzer 2012, on 20 ABC data sets under cross-validation; in the in-sample-favoured GG96 German-cities competition tallying (.656) was level with regression (.657), which had more information. An LLM yes/no checklist counted with unit weights matched or beat elastic-net weights when positives were scarce (RRF, F0.5 .102 vs .080, not separable at founder level). The median of 12 LLMs matched a human crowd (Brier .20 vs .19) but was worse than the best single model (GPT-4, .15).
- **E18.02-K12** (reworded: the sources support less). Numbers check out (36.3 points is the abstract maximum, an o1-preview vs GPT-4o comparison on one task; 17.3 points CI 7.7-25.5 from one pre-registered single-author study), but Tsvilodub et al. and Fan et al. are different experiments (chain length vs answerability, abstention rates only inferred from the abstract), not replications of the accuracy drop, and the effect is absent or reversed in the weakest models. Corrected claim: Longer or forced chain of thought lowers LLM accuracy on some tasks where deliberation also hurts people (Liu et al. 2024: up to 36.3 points lower for o1-preview vs GPT-4o on implicit statistical learning; lower CoT accuracy also on face recognition) and on unanswerable Knightian items (Bogdan 2026, single pre-registered study: 17.3 points, CI 7.7-25.5, strong in mid-to-large models, absent or reversed in the weakest); longer reasoning budgets also lowered accuracy on several task families (Gema et al. 2025). Two other labs report related but different findings: reasoning models write chains at least as long on unanswerable as on answerable items (Tsvilodub et al. 2026) and much longer responses on missing-premise questions (Fan et al. 2025); the 17.3-point size has not been replicated.
- **E18.02-K26** (number corrected). Betas are mislabelled: 0.96 is abstention below answering accuracy, 1.03 is the human comparison, and 1.67 is the question-type by model-type interaction (answer-abstain gap larger in reasoning than instruction models); Fan et al. report longer responses on missing-premise items but abstention rates only inferred from the abstract. Corrected claim: Independent labs see the cost of long reasoning on unanswerable items: reasoning models write chains at least as long on unanswerable as on answerable items (85% posterior probability that they are longer) and abstain credibly worse than they answer (beta 0.96) and worse than humans (beta 1.03), with the answer-abstain gap larger in reasoning than instruction-tuned models (beta 1.67) (Tsvilodub et al. 2026); an efficiency reward raised abstention 14.7% and cut chains 44% on average in fine-tuned 4B/8B models; Fan et al. 2025 independently report much longer responses by reasoning models on missing-premise questions.
- **E18.02-K22** (now single-source: only one opened source, code check).
