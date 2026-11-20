# Imprecise credences: deep document

*Subfield D02.05 of epistemology and Bayesian epistemology. Evidence ids (a01-a28, b01-b26, c01-c27, d01-d17) point to the evidence_*.jsonl files in this folder. Claim ids (D02.05-K01 to K21) point to claims.jsonl. Research done 2026-11-17 to 2026-11-19.*

**Honest summary first.** This subfield is mostly philosophy and decision theory. The human data is about Ellsberg-type ambiguity aversion. The LLM data is almost all about calibration, not about imprecise credences as a reasoning step. No paper tests whether a low/high "unknown" flag raises answer accuracy at equal tokens (K17, K20). So the schema value is background plus one cheap candidate to test.

## 1. What it is

A normal Bayesian agent holds one probability per claim: P(H) = 0.6. An imprecise-credence agent holds a set of probability functions (a "representor" or "credal set"). For each claim X it reports a lower probability (smallest value in the set) and an upper probability (largest). Upper(X) = 1 - Lower(not X) (a01).

Why people want this:
- **Keynes (1921)** asked about "weight of argument": two urns can both give 50% but rest on very different evidence. Not opened by us; content via SEP (a10, b02, b21).
- **Ellsberg (1961)** showed people prefer a bet on a known 50/50 urn to a bet on an urn of unknown mix. No single probability explains the usual pattern (a02, b01).
- **Levi (1974, 1980)** and **Walley (1991)** built the theory: indeterminate credence, E-admissibility, lower and upper previsions (a17, a18, b23, b24; all second-hand).

One-line idea for an agent: store an "unknown" claim as an interval [low, high], not a point, and act differently when the interval is wide.

**Status of evidence.** The founding works (Keynes, Levi, Walley, Ellsberg 1961, Seidenfeld and Wasserman 1993, Camerer and Weber 1992, Chow and Sarin, Dolan and Jones) were NOT opened. Their content comes from the Stanford Encyclopedia of Philosophy (Bradley 2019, opened: a01-a07, b01-b07) and Elga (2010, opened: a08, b08).

## 2. History and theories in depth

### 2.1 The Ellsberg setup
A 90-ball urn has 30 red and 60 blue-or-yellow in unknown mix. Bets: I = red, II = blue, III = red or yellow, IV = blue or yellow. Most people prefer I to II and IV to III. One probability would need r > b and r + y < b + y, which cannot both hold (a02). The usual reading: people dislike the unknown mix. Steele notes the fit only works if the belief is truly indeterminate, not just badly introspected (b01).

### 2.2 The formal model
- A set P of probability functions. Lower P(X) = inf over P; upper = sup over P.
- **Precise** if lower = upper for all events. **Vacuous** if lower = 0 and upper = 1 for all non-trivial events (a11).
- **Update** member by member: P(X|E) = {p(X|E) : p in P, p(E) > 0} (a01).
- The interval alone is not the full picture: different sets can share the same bounds. SEP warns of this (a01, K01).

### 2.3 Rival traditions
- **Levi:** suspend judgement among members; choose by E-admissibility (an act is allowed if some member ranks it best) (a17, K06).
- **Walley:** lower and upper previsions; interval width measures weight of evidence. This fails when evidence conflicts (b02).
- **Gilboa and Schmeidler (1989) maxmin; Schmeidler (1989) Choquet:** second-hand only (a16).
- **Huber's measure** of suspension of judgement. Elga's toothpaste case: max-entropy answers depend on how options are described (b03).
- **Sharp-credence defenders:** Elga (2010). Rinard, Skyrms (resilience), Leitgeb (stability) say the useful part of "weight" fits inside precise probability (b02, b05).

### 2.4 The three classic problems
1. **Dilation** (Seidenfeld and Wasserman 1993; White's coin). Prior P(H) = 1/2 exactly. After learning which side of a painted coin is up, the posterior is [0,1]. Evidence that looks irrelevant widens the interval (a03, b04, b25). Bradley and Steele reply that the credal set changes, so Reflection is not broken (b04). Established as a known cost (K04).
2. **Belief inertia.** A vacuous prior stays vacuous for any evidence, so the agent never learns. Levi raised it; Walley accepted it as harmless; Rinard bans vacuous priors; Wilson 2001 and Cattaneo 2008, 2014 cut away extreme priors (a04, b05). Formula: p(H1|E) = p1 p(H1) / (p2 + (p1 - p2) p(H1)), continuous in the prior, so the whole [0,1] range is reached (a04). Established (K05).
3. **Decision paralysis and sure loss.** Elga's two bets: A loses 10 on heads and wins 15 on tails; B is the mirror. Taking both gains 5 for sure. An agent with credence [10%, 80%] may refuse each alone and then lose a sure 5 (a05, a08, b08). Chandler (2014) and Sahlin and Weirich (2014) showed some decision rules forbid refusing both, which weakens Elga's argument; Elga issued an erratum (a08). A midpoint rule would price a $100 ticket on H at exactly $45 and make the interval pointless (b08). Contested (K06).

### 2.5 Regress
If the interval is itself uncertain, why stop there? Sets of sets or second-order probabilities follow (a06, b06). SEP's answer is pragmatic: climb the "uncertainty escalator" only as far as needed (a06).

### 2.6 Comparative ignorance
Fox and Tversky (1995): ambiguity aversion appears when clear and vague bets are judged side by side and shrinks when each is judged alone (d01). Arlo-Costa and Helzner (2005) ran a close copy of the alone condition and did not reproduce the disappearance (d02). Chow and Sarin (2001) also found preference for known odds persisting in non-comparative conditions (d03, abstract-level only). This is the main boundary condition for human ambiguity aversion.

### 2.7 Link to machine learning
Hullermeier and Waegeman (2021) argue epistemic uncertainty needs set-valued representation; credal inference replaces one prior with a set of priors and returns a set of posteriors (b16, c01, K18). Credal methods are costly and rarely used on large models (c01). Sale et al.: credal-set volume works for 2 classes but loses continuity above 2 (b17, K16).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Interval model, member-wise updating, vacuous and precise definitions | Upper(X) = 1 - Lower(not X) | Bradley 2019 SEP (a01, a11) | Established (K01) |
| No single probability fits the Ellsberg pattern | Needs r > b and r + y < b + y | SEP (a02) | Established |
| About half of humans show Ellsberg aversion | "Slightly more than half" across 39 experiments (second-hand) | Oechssler and Roomets 2015 via Kuzmics (b10) | Established, second-hand (K02) |
| Two-ball Ellsberg paradox, risky urn preferred to a dominating ambiguous one | N=708 US representative sample; 54.9% show paradox; certainty equivalent 118.13 vs 101.03 cents, gap 17.1, t=11.7 | Jabarian and Lazarus 2022 (a14) | Single source; abstract confirmed, t-value not rechecked |
| Choice rules inconsistent with all classical ambiguity models | 18 of 27 (66.7%), 95% CI 46.0% to 83.5%; most common rule GWWY 13 (48.1%). A share of rules, not a plain preference rate | Kuzmics, Rogers and Zhang 2023 (b09, d04) | Single source, tiny N |
| Consistency under uncertainty about as good as under risk | 154 subjects; 20 (13.0%) perfectly rationalizable; 0 perfectly EU-rationalizable; share with consistency above 0.9: 28.6% (subjective EU), 50.0% (best kinked or sophisticated), 68.2% (multiple priors) | Dembo et al. 2026 (b11, d05) | Contested (K03) |
| Comparative ignorance, human | N=141; alone: clear $17.94 vs vague $18.42; together: clear $24.34 vs vague $14.85 (bet pays $100 or $0) | Fox and Tversky 1995, via Arlo-Costa and Helzner (d01) | Contested (K19) |
| Failed partial copy | N=97; alone: clear 15.33 (sd 9.34) vs vague 5.42 (sd 9.23); 13.65 vs 6.4; 44.80 vs 15.29; 38.47 vs 14; 13.83 vs 6.24 after dropping incoherent answers | Arlo-Costa and Helzner 2005 (d02) | Contested; one small classroom study |
| Dilation | Point 1/2 becomes [0,1] after seeing a cell of a partition | SEP; Seidenfeld and Wasserman (a03, b04) | Established (K04) |
| Belief inertia | Vacuous prior gives vacuous posterior for all evidence | SEP (a04, b05) | Established (K05) |
| Elga sure-loss pair | Bets -10/+15; taking both gives +5 sure | Elga 2010 (a05, a08) | Contested (K06) |
| Verbalized LLM confidence is a weak error predictor | GPT-4 average AUROC 62.7%; GSM8K vanilla 54.8%; ECE above 0.377 for GPT-3, GPT-3.5, Vicuna; abstract range 0.522 to 0.605 | Xiong et al. 2024 (c09, b20) | Established (K07) |
| Sample consistency helps on arithmetic | GSM8K AUROC 54.8% to 92.7% with 5 samples (text figure); GPT-4 consistency 84.4 on GSM8K | Xiong 2024 (c09, d12) | Established for arithmetic |
| Sample consistency elsewhere is middling | GPT-4 AUROC: Law 66.2, Date 68.9, Sport 60.3, Strategy 65.4, Ethics 56.3 | Xiong 2024 Table 4 (d12) | Contested (K08) |
| Ask for alternatives with probabilities, then confidence | ECE cut by a relative 50% often; over 50% with temperature scaling; ChatGPT, GPT-4, Claude 2 | Tian et al. 2023 (c10, d13) | Single source (K09) |
| LLMs do not express their own uncertainty faithfully | Faithfulness 0.52-0.57 vanilla; best 0.63 (GPT-4), 0.70 (Gemini Ultra); judge-human correlation 0.97 | Yona et al. 2024 (c12) | Established (K10) |
| LLMs handle ambiguity badly | GPT-4 disambiguations correct 32% vs 90% for dataset (1,645 items); detection 57% vs 50% chance; humans find 53% of follow-ups helpful | Liu et al. 2023 (c15); Kirchhof 2025 (c08, c25) | Established (K15) |
| Verbalized interval contains its own point estimate | 72.33% on AmbigQA; constraint gives 100%; AUROC 0.7862 to 0.7554 | Yang et al. 2026 (a19, d08) | Single source (K12) |
| Interval vs plain verbalized confidence, GPT-5 (MMLU-Pro / Non-MAQA / Non-AmbigQA AUROC) | Vanilla 0.8587 / 0.7577 / 0.7756; ProbInt 0.8617 / 0.7753 / 0.7713; Label prob. (5 samples) 0.7649 / 0.6430 / 0.5876; Credal 0.8798 / 0.7230 / 0.7932; N=200 per dataset, 5 repeats | Yang et al. 2026 Table 1 (d09) | Single source (K21) |
| Same, gemini-2.5-pro | Vanilla 0.7326 / 0.6889 / 0.6688; ProbInt 0.7466 / 0.7303 / 0.7128; Label prob. 0.6377 / 0.6483 / 0.5582 | Yang et al. 2026 (d09) | Single source |
| Small deterministic model (79% accuracy) | Label prob. AUROC 0.5; Vanilla 0.5698; ProbInt 0.6027 | Yang et al. 2026 App. D.2.3 (d10) | Single source |
| Credal LLM selective prediction at 80% coverage | OpenBookQA CLLM+SCC 99.0 (always-answer 93.2) vs semantic entropy 98.0; CoQA 71.5 (59.6) vs 70.5; TriviaQA 43.5 (32.4) vs 44.0 | Manchingal et al. 2026 (d06) | Contested (K11); authors' own, needs LoRA ensemble |
| Earlier "73-91% commit at 89-98% accuracy" | Not found in full text | d06 | Withdrawn |
| LLM Ellsberg aversion | Near-ceiling known-urn choice (AAI = P(choose known)) in reasoning LLMs; GPT and Llama 100% ambiguity averse (0% rational) in one battery | Tak et al. 2026 (b12, d14); Bini et al. 2026 (b14, d15) | Contested (K13) |
| Temperature sensitivity of SEU following | GPT-4o slope -24.6 (insurance), -38.4 (Ellsberg-style); Claude 3.5 -2.9 and -15.0, intervals include 0 | Helzner 2026 (a25, d07) | Single source; not an ambiguity claim |
| Credal volume | Sound for 2 classes, discontinuous above 2 | Sale et al. 2023 (b17) | Single source (K16) |
| Higher accuracy is not lower uncertainty | Conformal set size, 9 LLMs, 5 tasks | Ye et al. 2024 (c14) | Single source |

## 4. Mechanisms and models

### 4.1 Credal set from samples (implementable)
1. Draw k answers (say 5), each in a fresh context.
2. Group them by meaning (code; exact match or normalised).
3. For each distinct answer, lower = its share minus slack; upper = share plus slack. Or use per-label min and max over several models or prompts.
4. Store low and high per claim, never only the midpoint.
Caveat: samples from one model are not independent (G4), so the set is narrower than the truth. Sample frequency lost to verbalized confidence for GPT-5 and gemini-2.5-pro on QA (d09).

### 4.2 Verbalized interval (ProbInt, Yang et al. 2026)
Prompt for a first-order probability p and an interval [l, u]. Add the containment instruction l <= p <= u; without it the point lies inside only about 70% of the time (72.33% on AmbigQA). The constraint costs about 0.03 AUROC (d08). One call, no ensemble. Result: ties plain verbalized confidence on AUROC (d09).

### 4.3 Commit rule (interval dominance)
Commit to answer a if lower(a) > upper(b) for every rival b. Otherwise return the set of answers not ruled out, abstain, or ask. Used in credal LLMs with a trained LoRA ensemble (a21, d06). A black-box version uses 5 samples and per-label intervals.

### 4.4 Decision rules when the interval straddles the threshold
- **Maximin:** act on the lower probability. Pessimistic.
- **Maximax:** act on the upper. Optimistic.
- **E-admissibility (Levi):** allowed if best for some member; choose among allowed ones by a second rule.
- **Maximality:** drop acts that another act beats in every member.
- **Midpoint:** collapses to a sharp credence (Elga's point, b08).
Only maximin/maximax alignment with the model's own answers was measured, and rates were unreadable (d11, a27). No rule was compared by accuracy (K20).

### 4.5 Guards against known failures
- **Dilation guard:** if new evidence is judged irrelevant, do not let the interval widen; compare stated interval before and after. No LLM measurement exists (d16).
- **Inertia guard:** never start at [0,1]; start with a weak prior such as [0.05, 0.95] (K05, a04). Untested on LLMs.
- **Containment guard:** point inside interval (K12).

### 4.6 Ambiguity pre-check (a different sense of "ambiguity")
Hou et al. (2024) split uncertainty into input ambiguity and model ignorance by rewriting the question into clarified versions and comparing answers (c06). Total-uncertainty AUROC is about equal to semantic entropy and deep ensembles; ambiguity-detection AUROC for baseline ensembles on AmbigQA is about 55 (c06, c26). This is linguistic ambiguity, not Ellsberg-type (c15 limit).

## 5. What holds up

**Holds up**
- Dilation, inertia and "the interval loses information" are mathematical facts (K01, K04, K05).
- Humans often avoid unknown-odds bets: about half across 39 experiments (second-hand), 54.9% in N=708 (b10, a14).
- Verbalized LLM confidence is poorly calibrated and unfaithful (K07, K10).
- LLMs detect and enumerate ambiguity badly (K15).

**Failed, weakened or contested**
- Fox and Tversky's disappearance of aversion when judged alone: the partial copy (N=97) did not reproduce it (d01, d02). SEP also says Ellsberg patterns are rarer than usually said in some experiments (Binmore et al. 2012; Voorhoeve), with no numbers (a02).
- Kuzmics 18 of 27 was first read as a preference rate. It is not (d04).
- Dembo: 0 of 154 perfectly EU-rationalizable, but consistency under uncertainty matches risk, so the data do not prove imprecise credences (d05).
- Elga's argument was weakened by Chandler and by Sahlin and Weirich (a08).
- The credal LLM "73-91% commit at 89-98% accuracy" figure was not found (d06). At 80% coverage credal scores roughly tie semantic entropy on open QA (43.5 vs 44.0 on TriviaQA).
- Sample consistency's big gain is arithmetic; elsewhere AUROC is 56 to 69 (d12).
- No outside replication of credal-set gains was found (K20, d17).

**Moderators**
- Judged alone vs side by side (humans).
- Task type: arithmetic vs QA (LLMs).
- Model: a deterministic small model gives sample AUROC 0.5 but interval 0.6027 (d10).
- Training: the credal LLM needs LoRA tuning; benefit is largest on letter-answer tasks (d17).
- Distribution shift: calibration is lost out of distribution (c11, c27).

**Interventions that worked** (on calibration, not accuracy)
- Alternatives and probabilities first (Tian, relative ECE drop about 50%).
- Five samples plus consistency on GSM8K (AUROC 54.8 to 92.7).
- Containment instruction (100% containment).

**Did not work, or no evidence**
- Interval vs plain confidence: a tie within about one SD in several cells (d09).
- Accuracy gain at equal tokens from any interval flag: untested.

## 6. Language models

1. **Calibration.** Vanilla verbalized confidence: ECE above 0.377 (GPT-3, GPT-3.5, Vicuna); GPT-4 average AUROC 62.7% (c09). Calibration improves with scale up to 52B (c11) but is lost out of distribution (c27). Faithfulness to own sampling split is near chance (0.52-0.57; best 0.70) (c12).
2. **Fixes.** Alternatives first: relative ECE cut about 50% (c10). Samples plus consistency: GSM8K AUROC 92.7 (c09). Non-arithmetic: 56 to 69 (d12). With frontier models on QA, sample frequency (AUROC 0.5876, GPT-5, Non-AmbigQA) loses to verbalized confidence (0.7756) (d09).
3. **Interval prompting.** GPT-5: ProbInt 0.7753 vs Vanilla 0.7577 (Non-MAQA), 0.7713 vs 0.7756 (Non-AmbigQA): a tie. gemini-2.5-pro: 0.7303 vs 0.6889 and 0.7128 vs 0.6688 (ProbInt ahead by about 0.04). Point-in-interval only 72.33% (d09, d08). Plain verbalized confidence stays too uncertain as in-context examples increase; interval methods track error (a19).
4. **Credal LLMs.** Trained LoRA ensembles, white-box, small open models: 80%-coverage selective accuracy 99.0 / 71.5 / 43.5 (d06). Corrupted context cuts commitment from 87-92% to 65-71% (a21, author-reported). Standard-LLM proxy ECE 26-81% (d17). Random-set LLMs (a22) and Credal Transformer (a24) need training; tables unreadable.
5. **Creative text.** Credal sets over 100,000 stories; best model-human calibration 0.434; decoding explains 39.4-72.0% of epistemic uncertainty (a23, first page only).
6. **Ambiguity detection.** GPT-4 disambiguations 32% vs 90% (c15). Detection 57% vs 50% (c08). Tamkin: scale plus human-feedback training lets models match humans, either alone is not enough; models near 50% where humans are near 100% on negation (c16). Conformal set size on 9 LLMs: higher accuracy does not mean lower uncertainty (c14).
7. **Ellsberg behaviour.** Reasoning LLMs show near-ceiling ambiguity aversion (b12, d14). GPT and Llama 100% human-like in one battery (b14). One model looked neutral only by following option order. Claude 3.5 gave nulls in Helzner (a25). Both urns were always shown side by side, so comparative ignorance is untested. No link to answer quality.
8. **Economic rationality.** Chen et al. (c18) and Ross et al. (c19) test risk, not ambiguity. Binz and Schulz (c17): small vignette changes sent GPT-3 "vastly astray"; no Ellsberg test found. Tak et al.: thinking tokens may make choices more expected-utility consistent (b13, K14, contested).
9. **Decision rules.** Worst-case rules over a conformal set can hurt by favouring generic outputs; Bayesian rules do better when ambiguity is high, in tutoring and peer review (a26, direction only).

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)
1. **Store uncertain claims as low/high, not a point, in memory and S0 gate records. Keep both bounds; never collapse to the midpoint.** Part: S0 / memory. [E] (K01; a01, a11, b02, a17, a24). This is bookkeeping only. Its benefit is untested, so do not make it a decision input until U1 passes.
2. **Never initialise an interval at [0,1]; use a weak prior.** Part: O. [E] (K05; a04, b05, a18, b24). Theory only, no LLM test.
3. **Do not read a model's stated confidence as proof.** Part: G (extends G4, G10). [E] (K07, K10; c09, c12, b20). Already consistent with the schema.
4. **Do not widen a stored interval on evidence judged irrelevant (dilation guard).** Part: G. [E] as theory (K04; a03, b04, b25). The guard itself is untested.
5. **At S0, flag underspecified tasks: list readings or ask.** Part: S0. [E] that models do this badly (K15; c15, c08, c25, c16). The remedy is untested (U7).

### Test first
- **Interval flag vs point confidence** (K17, K21). S0/O. [S]. Closest: ProbInt ties Vanilla on AUROC (d09).
- **Sample-then-interval vs one verbalized interval** (K08). O. [C]; d09, d12.
- **List alternatives first, then low/high** (K09). O. [S]; c10.
- **Commit if lower beats rival upper** with 5 samples (K11). O. [C]; a21, d06.
- **Containment rule** (K12). G. [S]; a19, d08.
- **Tie-break at threshold** (abstain, maximin, ask, E-admissibility) (K06, K20). S/O. [C]; a05, a08, d11.
- **One claim at a time** to cut contrast penalty on vague claims (K19). S0. [C]; d01, d02. Weak support.
- **Vacuous-flag rule** (K05, K20). G. Theory only.

Do NOT add: Ellsberg-style behaviour steering (K13, no link to quality); credal volume (K16); any trained credal ensemble (white-box, needs LoRA, d06).

## 8. Concrete tests on our bench

All arms at equal total tokens; setup and extra calls are charged to the arm that uses them. Items are held-out, with known answers.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Held-out QA with exact answers, mixed difficulty | A: answer + point confidence. B: answer + [low, high] with containment; flag used to re-sample or abstain | Final accuracy; AUROC of flag for correctness | AUROC within 0.02 of A (d09 suggests a tie); gain only if the flag routes tokens better |
| T2 | Same, 5 samples | A: majority of 5. B: 5 samples + per-label interval, commit by dominance, else extra sample | Accuracy at 80% and 100% coverage | Small gain; none expected vs semantic entropy (d06) |
| T3 | Non-arithmetic open QA | A: verbalized interval. B: sample-spread interval | AUROC of correctness | B <= A on frontier models (d09, d12) |
| T4 | Items with interval straddling threshold (about 0.5) | Four rules: abstain, maximin, ask, E-admissible then maximin; include Elga-style sure-loss pairs | Accuracy and cost | Unknown; ask may win where a check exists |
| T5 | Sequential evidence with distractors | A: start [0,1]. B: start [0.05,0.95]. C: point prior | Final error; width after each piece | A stuck at [0,1]; B and C learn |
| T6 | Irrelevant-evidence probe | Same claim before and after an irrelevant fact | Share of cases where stated interval widens | Unknown; guard should push it to 0 |
| T7 | Underspecified tasks (AmbigQA-like) | A: answer directly. B: ambiguity check, then ask or list readings | Accuracy, extra tokens | Detection near 57% means a small gain; measure |
| T8 | Two-urn item alone vs beside a precise rival | One claim at a time vs paired | Stated confidence gap | Behaviour only; tests comparative ignorance in LLMs |
| T9 | Hedging words vs sample split | Compare verbal hedge to sample agreement | Agreement score | Near 0.52-0.57 baseline |

## 9. What does not transfer, and why

- **Ellsberg aversion as a preference.** It is a taste about unknown odds. Our agent's job is accuracy. LLM aversion is near ceiling (b12) with no shown link to answer quality (K13).
- **The Elga vs Levi debate.** No empirical test settles it (critique).
- **Credal LLMs** (LoRA ensembles, random-set, credal transformers). White-box and need training; our approach is scaffold only (a21, a22, a24, d06).
- **Credal volume.** Breaks above 2 classes (b17).
- **Image-classifier credal wrappers** (c04). Vision, and need several trained members.
- **Human lab numbers** (N=27, 97, 141 undergraduates). Small, and do not describe LLM behaviour.
- **Sample frequency as the interval.** One model's samples are correlated (G4); outside arithmetic the signal is weak (d12, d09).
- **Calibration gains.** Better ECE does not imply better answers (c14). Most metrics here are calibration, not task accuracy.

## 10. Open questions

1. Does a low/high flag change final accuracy or abstention quality at equal tokens vs a point confidence? (No paper; gap 1.)
2. How often do stated intervals exclude the point estimate for models other than GPT-5-mini? (About 70% in a19; 72.33% pooled; gap 3.)
3. Does LLM updating show dilation? (Gap 4; d16 found nothing.)
4. Which tie-break rule works best when the interval straddles the threshold? (Gap 5.)
5. Does showing one claim at a time lower LLM ambiguity aversion? (Gap 6.)
6. Do LLM Ellsberg results predict answer quality? (Gap 7.)
7. Do credal-set gains replicate outside the authors' own papers? (Gap 9.)
8. Is a vacuous flag ever useful, or should the rule be "never output [0,1]"? (Gap 10.)
9. Founding texts were never opened; their claims here are second-hand.
10. Several credal-LLM tables were unreadable in text extraction (a20, a22, a24, a26, a27).
11. Links to parallel subfields, not covered here: Verbal confidence; Retrieval and ensembles for LLM forecasts; Values and inductive risk; Evidence and probability reasoning; Prospect theory and risky choice; Debiasing; Dual-process accounts of judgment.

## 11. Sources

**Opened [V]**
- [V] Bradley (2019) Imprecise Probabilities, SEP. https://plato.stanford.edu/entries/imprecise-probabilities/ (a01-a07, b01-b07)
- [V] Elga (2010) Subjective Probabilities Should Be Sharp. https://www.princeton.edu/~adame/papers/sharp/elga-subjective-probabilities-should-be-sharp.pdf ; https://www.philosophersimprint.org/010005/ (a08, a09, b08)
- [V] Wikipedia, Imprecise probability; Ellsberg paradox. https://en.wikipedia.org/wiki/Imprecise_probability ; https://en.wikipedia.org/wiki/Ellsberg_paradox (a11, a12)
- [V] Jabarian and Lazarus (2022) https://arxiv.org/abs/2206.04605 (a14)
- [V] Kuzmics, Rogers and Zhang (2023) https://arxiv.org/abs/2212.03603 (a15, b09, d04)
- [V] Dembo, Kariv, Polisson and Quah (2026) https://arxiv.org/abs/2607.09355 (b11, d05)
- [V] Arlo-Costa and Helzner (2005), account of Fox and Tversky (1995). https://isipta05.sipta.org/proceedings/papers/s043.pdf (d01, d02)
- [V] Yang, Muandet, Caprio, Chau and Adachi (2026) https://arxiv.org/abs/2603.10396 (a19, a20, a27, d08-d11)
- [V] Manchingal, Nikolenko and Cuzzolin (2026) https://arxiv.org/abs/2608.23244 (a21, d06, d17)
- [V] Mubashar et al. (2025) https://arxiv.org/abs/2504.18085 (a22)
- [V] Garces Arias et al. (2025) https://arxiv.org/abs/2509.23088 (a23; first page only)
- [V] Ji, Song and Huang (2025) https://arxiv.org/abs/2510.12137 (a24)
- [V] Helzner (2026) https://arxiv.org/abs/2607.11920 (a25, d07)
- [V] Daheim and Gurevych (2026) https://arxiv.org/abs/2606.30578 (a26)
- [V] Tak et al. (2026) Sparks of Rationality https://arxiv.org/abs/2601.22329 (b12, b13, d14)
- [V] Bini, Cong, Huang and Jin (2026) https://arxiv.org/abs/2602.09362 (b14, b15, d15)
- [V] Hullermeier and Waegeman (2021) https://arxiv.org/abs/1910.09457 (b16, c01)
- [V] Sale, Caprio and Hullermeier (2023) https://arxiv.org/abs/2306.09586 (b17); Sale et al. (2024) https://arxiv.org/abs/2401.00276 ; https://arxiv.org/abs/2406.02354 (c02, c03)
- [V] Zucchet, Lee and Linderman (2026) https://arxiv.org/abs/2608.15448 (b18)
- [V] Kadavath et al. (2022) https://arxiv.org/abs/2207.05221 (b19, c11, c27)
- [V] Xiong et al. (2024) https://arxiv.org/abs/2306.13063 (b20, c09, c24, d12)
- [V] Wang et al. (2024) credal wrapper https://arxiv.org/abs/2405.15047 (c04)
- [V] Kuhn, Gal and Farquhar (2023) https://arxiv.org/abs/2302.09664 (c05)
- [V] Hou et al. (2024) https://arxiv.org/abs/2311.08718 (c06, c26)
- [V] Ling et al. (2024) https://arxiv.org/abs/2402.10189 (c07)
- [V] Kirchhof, Kasneci and Kasneci (2025) https://arxiv.org/abs/2505.22655 (c08, c25)
- [V] Tian et al. (2023) https://arxiv.org/abs/2305.14975 (c10, d13)
- [V] Yona, Aharoni and Geva (2024) https://arxiv.org/abs/2405.16908 (c12)
- [V] Quach et al. (2024) https://arxiv.org/abs/2306.10193 (c13)
- [V] Ye et al. (2024) https://arxiv.org/abs/2401.12794 (c14)
- [V] Liu et al. (2023) AmbiEnt https://arxiv.org/abs/2304.14399 (c15)
- [V] Tamkin et al. (2022) https://arxiv.org/abs/2212.10711 (c16)
- [V] Binz and Schulz (2022) https://arxiv.org/abs/2206.14576 (c17)
- [V] Chen et al. (2023) https://arxiv.org/abs/2305.12763 (c18)
- [V] Ross, Kim and Lo (2024) https://arxiv.org/abs/2408.02784 (c19)
- [V] Jia et al. (2024) https://arxiv.org/abs/2406.05972 (c20)

**Snippet or second-hand only [M]**
- [M] Keynes (1921) A Treatise on Probability (a10, b21; via SEP, Elga, Wikipedia). https://en.wikipedia.org/wiki/Imprecise_probability
- [M] Ellsberg (1961) Risk, ambiguity, and the Savage axioms, QJE 75 (b22; no URL kept)
- [M] Levi (1974, 1980, 1986, 1990) (a17, b23; via SEP) https://plato.stanford.edu/entries/imprecise-probabilities/
- [M] Walley (1991) (a18, b24, c22; via SEP)
- [M] Seidenfeld and Wasserman (1993) (b25; via SEP)
- [M] Camerer and Weber (1992) (b26; via SEP)
- [M] Gilboa and Schmeidler (1989), Schmeidler (1989), Klibanoff et al. (a16)
- [M] Oechssler and Roomets (2015), quoted via Kuzmics (b10) https://arxiv.org/abs/2212.03603
- [M] Fox and Tversky (1995), QJE original (a13; d01 via ISIPTA account)
- [M] Chow and Sarin (2001) https://econpapers.repec.org/RePEc:kap:jrisku:v:22:y:2001:i:2:p:129-39 (d03)
- [M] Dolan and Jones (search summary only)
- [M] Search notes (a28, c21, d16): zero hits for direct LLM Ellsberg or dilation tests; absence is weak evidence. https://export.arxiv.org/api/query
