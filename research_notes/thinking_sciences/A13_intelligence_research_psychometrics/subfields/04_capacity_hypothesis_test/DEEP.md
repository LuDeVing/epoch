# Capacity hypothesis test: deep document

*Subfield A13.04. Built from evidence_a.jsonl (27 lines), evidence_b (28), evidence_c (28), evidence_d (18), claims.jsonl (K01-K25) and critique.md (cross-check, with its corrections applied). Ids such as a02, b06, c14, d06 point to evidence lines; K-ids point to claims. Sources read only as abstracts or second-hand are flagged in section 11. Do not quote a study count for the Dokic 2025 review: it is unknown.*

## 1. What it is

The capacity hypothesis says: working memory capacity (WMC) limits how well people reason about new problems (fluid intelligence, Gf). Raven's matrices are the standard test.

The testable step: if capacity is the cause, harder items load memory more. So the correlation between one item and a WMC score should rise with item difficulty, or with the number of rules per item (rule tokens).

The finding of this subfield: that prediction mostly fails. Most studies see a flat or humped curve. The newest, Dokic et al. 2025 (Intelligence 108, 101874; N=543; operation, reading and symmetry span against Raven APM), found no support using item difficulty, rule tokens, SEM or latent growth curves (a16, b17, d01).

Two readings of the failure, both partly right:
1. Capacity is not the cause. Rivals: attention control, process overlap, relational binding.
2. The test is bad. Formal capacity models let the item-wise correlation rise, fall or stay flat (Frischkorn and Oberauer 2021). Floor and ceiling alone make an inverted U (Smolen and Chuderski 2015). So a null does not refute capacity, and a positive result would not prove it.

Lesson for our agent: do not assume rule count (or any structure count) drives difficulty. Measure difficulty empirically per item and per agent variant, and measure load by controlled manipulation. This corrects our first draft, which used rule count as the load variable.

Links only (covered elsewhere): Extraneous load and split attention; Generalisability and transfer; Monitoring and control framework; Sampling and voting; the A08 cognitive load documents.

## 2. History and theories in depth

**Founding claims (1990).**
- Kyllonen and Christal 1990: reasoning is "little more than" working-memory capacity. Latent correlations of .80 to .88 are cited from memory and never verified (d05, a17). Later work puts the link lower: Ackerman et al. 2005 meta-analysis range .312 to .641; Kane et al. 2005 about 50% shared variance (a18).
- Carpenter, Just and Shell 1990: two production-system models of Raven (FAIRAVEN, BETTERAVEN). Rules come from a taxonomy: constant, pairwise progression, figure addition/subtraction, distribution of 3, distribution of 2. Difficulty rises with the number of rule tokens and with goal management. Second-hand (via Little 2014): rule tokens explained 57% of item-accuracy variance, across items, not people (d04, a26). Original never opened.

**The item-wise test.** Capacity theory implies the WM-item correlation grows with demand. Early tests:
- Salthouse 1993: no rise even at overall r=.59 (second-hand; Little argues age pooling inflated r; a06, a27).
- Unsworth and Engle 2005: N=160, no rise (a02-a04).
- Wiley et al. 2011: claimed items needing a NEW rule combination carry the WM link (a05).
- Salthouse and Pink 2008: latent Gf-WM link just as strong at the smallest set sizes (a13).
- Embretson 1995: early model-based test, never opened (a14).

**The statistical turn.**
- Little, Lewandowsky and Craig 2014: the flat curve is an artifact of a low overall correlation. With a four-task WM composite the slope rises (a07-a09).
- Smolen and Chuderski 2015: the curve is an inverted U because of ceiling and floor (a10, a11, b03, b04).
- Frischkorn and Oberauer 2021: the whole design is non-diagnostic. Correlation peaks where sample mean capacity matches item demand (b01, b02, c01, c02).

**Moderator and rival lines.**
- Time pressure (Chuderski 2013, 2015; Colom 2015): b08-b13.
- Training as intervention (Melby-Lervag 2016): b14-b16.
- Attention control (Burgoyne and Engle 2020; Unsworth, Miller and Strayer 2024) and process overlap (Kovacs and Conway 2016): b21-b24.

**Recent human tests.** Burgoyne, Hambrick and Altmann 2019: complex span and Visual Arrays k; neither showed the predicted rise (d02, abstract only). Dokic 2025 (above).

**LLM turn (2023-2026).** LLM studies mostly swap "rule count" for other load axes: relational complexity (REL), parallel branches (Patil), unique rules (Webb), n-back depth, binding count. None runs the item-wise correlation design on its own terms (d18, K21).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Ospan-Raven link flat across items | N=160; r=.335 overall; item 1 r=.26, item 24 r=.26; larger sample r(1042)=.349 | Unsworth and Engle 2005 (a02) | Established |
| Hardest quartile has no link | Quartile accuracy .83, .69, .44, .18; r with Ospan .324, .294, .331, .079 (ns) | a03 | Floor and non-attempt confound (47% finished) |
| More rule tokens, weaker link | Tokens 1-4: accuracy .72, .66, .32, .25; r=.342, .276, .245, .113 | a04 | Established (K04) |
| Wiley token-wise r | .25, .24, .33, .21 for 1-4 tokens | a05 via Little | Second-hand |
| Only positive item-wise result | 130 recruited, 126 analysed; composite r=.56; slope .004, t(34)=2.87, p<.01, r2=.20 | Little 2014 (a07, b06) | Contested (K02) |
| Same data, Ospan alone | r=.36; slope t(34)=1.39 ns; r2=.05 | Little 2014 | Shows dependence on WM measure |
| Slope depends on overall r | Simulated slope .0002 (rho .1) to .0016 (rho .9) | Little 2014 (a08) | Simulation |
| Small token interaction | Tokens beta -0.10 (SE .005); WMC x tokens beta .02 (SE .007), p<.01 | a09, b07 | Single-source, tiny |
| Inverted U over difficulty | N=347: linear F(1,34)=0.4, p=.53; segmented adj R2=.17; breakpoint error .44; r=.46 below, -.52 above; quadratic term -0.43 | Smolen and Chuderski 2015 (a11, b03) | Established |
| Same, bigger sample | N=939: segmented adj R2=.22; breakpoint .42; r=.53 / -.50. Quadratic adj R2 .14 (N=347), .23 (N=939) | b03, c04 | Samples overlap; the 939 WM score is not complex span |
| Floor/ceiling math | Half of scores at floor/ceiling cuts r from 1.0 to .86; base r .5 falls to .45 with ~25% on floor | b04, a10 | Math, established |
| New-rule claim fails | Harrison: n=208 complete; novel r=.36 vs repeated r=.50, z(205)=-2.29, p=.02. Smolen: .223 vs .197, z(34)=1.41, p=.17 | a12, b05 | Refuted (K05) |
| Capacity theory allows any pattern | Sim N=100/250/500; 17 items, 1-4 tokens; 12,000 runs per model; peak where mean WMC = demand; Pearson r .33-.41 vs point-biserial .23-.29; ordinal agreement .91-.98 | Frischkorn and Oberauer 2021 (b01, b02) | Established (K03) |
| Dokic 2025 null | N=543; three analysis routes all null; review: mixed evidence, majority null; Little named as positive | a16, b17, d01 | Abstract only; no coefficients |
| Time pressure, study 1 | N=890; latent r=1.0 speeded, .83 moderate, .62 unspeeded | Chuderski 2013 (b08) | Contested (K06) |
| Time pressure, review | 26 studies: <=30 min r=.395 (55 r, N=2253); 40 min .316 (41, N=1847); >=45 min .263 (11, N=553) | b09 | Between-study confound |
| Late items lose most under time cap | First half -3.7%, second half -17.6% | b10 | Single-source |
| Time replication, better battery | N=264; broad WM shares 83.4% of timed Gf; untimed reanalysis 58.2% | Chuderski 2015 (b11) | Same lab |
| Time failed replication | N=302 (93/99/110); latent r .89, .74, .96; score effect d=.39, .58, 1.01 | Colom 2015 (b12, b13) | Non-monotone |
| Latent link not load dependent | ~1000 adults; latent .86 (.78 age-partialled), .74 (.66) | Salthouse and Pink 2008 (a13) | Established (K09) |
| WM training does not lift Gf | 87 pubs, 145 comparisons; nonverbal g=0.05 [-0.02, 0.13] (treated controls, k=67); 0.20 with untreated; WM gain vs Gf gain beta -.01 | Melby-Lervag 2016 (b14-b16) | Single meta-analysis (K07) |
| Attention-control rival | 90 samples, 84.4% show a factor (snippet); difference scores <10% construct variance | b21-b23 | Snippet for the 90 samples |
| Webb 2023 unique rules | Humans N=40; GPT-3 vs human OR=1.88 generative, 6.27 multiple choice; unique rules OR=.61 humans, .25 GPT-3; profile r(30)=.39 | a20, c06 | Single-source (K11) |
| I-RAVEN-X load | Arithmetic: reasoning models 80.5% to 63.0%; plain LLMs 59.3% to 4.4% | a23 | Single-source |
| Perception beats load | o3-mini 86.6% to 17.0%; R1 80.6% to 23.2%; longer rules cost o3-mini 5.6%, R1 +2.2% | b28 | Symbolic input, two models |
| REL relational complexity | 45% drop RC 3 to 9; RC explains 24/32/44% of explainable variance (next factor 7/17/6%); homoplasy 35% at 4 taxa to 1% at 25 | REL 2604.12176 (b25, b26, c14) | 2026 preprint (K10) |
| REL: size alone is not difficulty | Fixed-RC larger inputs improve: REL-A5 56-64% to 77-87%; REL-A7 (RC 6) ~12% at any size | b27, c16 | Same study |
| REL: compute does not fix it | Token cap 4096 to 16384: ~2-3% on A4/A5, 0.4% on REL-C; ICL +3.4 to +6.6 points | c15, d10 | Contested (K13) |
| Parallel-branch collapse | 7 models 8B-235B; 100% to 12 branches; collapse at 20-30; same for all sizes | Patil 2026 (c17, d06) | Single-source (K19) |
| Binding capacity scales with size, partly | K50 = c * N^0.82, 12 models up to 3B, R2=.73; Pythia flat at k 3-6 from 410M to 12B | Ravulapalli 2026 (d07) | Single-source (K20) |
| Interference vs capacity | Spearman -0.473 p=.142; +0.20 p=.56; n=11 | d08 | Inconclusive |
| n-back misread | Strong model 90.08, 90.08, 84.75% at 8, 9, 10-back; weak models 1.00 at 1-back, ~.09-.20 at 2-3 back | Hu and Lewis 2025 (c11) | Contested (K14) |
| Budget by difficulty | MATH-500 best budget 1.0K (L1) to 7.5K (L5); AIME R1-32B 41.4% at 2K, 55.6% at 10K, 53.1% at 16K; 67.5% of 80 negative flips true overthinking | Zhou 2026 (d13) | Single-source (K23) |
| Fitted vs structure difficulty | LLM-judged features AUC .74-.84 vs oracle IRT .92-.95, baseline .66-.73 | Ge 2026 (d17) | Single-source (K24) |
| Fitted vs human difficulty judgment | IRT vs human pairwise 94.2% GSM8K, 73.7% ARC, 73.4% Winogrande; GPT-4 judge Spearman .61, .22, .16 | Easy2Hard-Bench (d16) | Single-source |

## 4. Mechanisms and models

**4.1 Floor and ceiling (what makes the curve a hump).** A binary item score is a thresholded noisy function of ability. Items near ceiling have almost no variance, so any correlation with WM is near zero. Items near floor are the same. Middle items show the biggest correlations. Implementation: simulate theta ~ N(0,1), WM = rho*theta + noise, item pass = (theta + noise > difficulty), then compute the point-biserial r per item by difficulty. You get an inverted U with no theory of capacity at all (a10, b04).

**4.2 Frischkorn and Oberauer capacity models (b01).** Three response models: Generic, Slot and Resource. Each item has demand d (rule tokens 1-4). Each person has capacity c. Pass probability rises with c minus d. The item-WM correlation then depends on two things: the share of ability variance that comes from WMC, and how close the sample mean capacity is to d. Low-capacity sample: correlation falls as demand rises. High-capacity sample: it rises. Mean matched to demand: peak. To implement a diagnostic test: sweep mean capacity over several levels and check that the correlation peak moves with it. A single sample cannot test the hypothesis.

**4.3 Little's slope artifact (a08, a09).** The item-wise slope is proportional to overall r. Bootstrapping the observed matrix down to r of about .23 reproduces the flat curve. A null at low overall r is weak evidence. Use a composite of several WM tasks to raise r before testing slopes.

**4.4 Carpenter production-system model (d04).** Solver loop: perceive attributes, induce a rule from the taxonomy, hold sub-goals, apply, check. Failures come from losing a goal or a rule token. BETTERAVEN adds abstraction and goal management, so it solves items FAIRAVEN cannot (a04). Engineer's reading: the load variable is the count of rule tokens held at once plus pending sub-goals. It is hand-coded, and the data show it is a weak predictor of WM dependence.

**4.5 Time and learning account (Chuderski).** Under a time cap, mostly easy items get attempted, so the WM link comes from easy items only (b11). The explanation (a hypothesis): with more time people learn relations during the test, which draws on other abilities.

**4.6 Rival mechanisms.** Attention control (keeping the goal against distraction), process overlap (tests share many processes), relational integration (binding items jointly). The LLM analogue of the third is relational complexity: operands bound at once (REL). The LLM analogue of the first is a distractor-count dial (Ghaffari 2026: the evidence margin needed grows with the log of the effective distractor count; same-format distractors hurt most; d09).

**4.7 Empirical difficulty by IRT (K17, K24).** 1PL model: P(pass) = sigmoid(ability_j - difficulty_i). Fit over many agent variants on a task bank. Agent ability can split additively into an LLM part and a scaffold part (d17). Difficulty is then a fitted number, not a count. Caveat: pooled difficulty measures the average model (d16).

**4.8 Budget by difficulty (d13).** Accuracy against reasoning-token budget is concave. The peak budget rises with item difficulty. Tight caps lose hard items first. Large caps hurt easy items by overthinking.

## 5. What holds up

**Holds.**
- The item-wise null in humans: five or more partly independent sources (K01). The pattern is flat or inverted U.
- The null is non-diagnostic (K03): formal models and floor/ceiling math agree, from two independent groups.
- Rule-token count weakly predicts the WM link (K04). It does lower accuracy (beta -0.10) but does not drive the WM link.
- The high latent WM-Gf correlation is not load dependent (K09).

**Failed or refuted.**
- Wiley's "new rule drives the link": reversed in Harrison (n=208), null in Smolen (K05).
- Little 2014 outside its lab: Burgoyne 2019 and Dokic 2025 null. A same-lab second study (RSPM) reported a reduced effect; its supplement is unread. Verdict: contested (K02).
- Colom 2015 did not replicate the monotone time effect (latent .89, .74, .96).
- WM training: Melby-Lervag g=0.05 with treated controls. The 0.20 with untreated controls is a control-group artifact. Studies with 20 or more per group g=0.01 (k=34) vs smaller 0.26 (k=25).

**Moderators.** Overall WM-Raven r (Little), sample mean capacity (Frischkorn), floor and ceiling (Smolen), WM measure (Ospan alone vs composite), time limit (Chuderski, contested), control group type (Melby-Lervag).

**Independence warning.** Most human data are Raven APM from two lab groups (Unsworth/Engle; Chuderski/Smolen). Chuderski 2013, 2015 and Smolen 2015 reuse overlapping datasets. Frischkorn and Oberauer are the only fully separate theory source.

**Interventions.**
- Worked in LLMs: code for exact indexing or counting (GPT-4 + code reached human level on shuffled-alphabet analogies, P=.496 vs humans; Lua function for Hanoi N=15 under 5,000 tokens; K22). Demonstrations for n-back comprehension (Hu and Lewis). Disabling reasoning on text multiple-choice RAPM for some models (p=.021).
- Did not work: more test-time tokens at high relational complexity (0.4% average); pattern hints (10 models, all ns); an RDKit tool when the model still held the whole set (recall .109, .094, .079); WM training in humans.
- Mixed: in-context examples (+3.4 to +6.6 points, task ordering kept); notes slot (WCST image-hard p=.052).

## 6. Language models

**What the tests look like.** No LLM study runs the item-wise correlation design. They test demand axes directly (accuracy against manipulated load). That is easier and more informative than the human design.

**Load axes and results.**
- Relational complexity (REL; Opus 4.5, Gemini 3 Pro, GPT-5.2): RC 1-2 near solved (91% on 30x30). Accuracy falls 45% from RC 3 to 9 with entity count fixed. Entity count is a noisy proxy. RC beat prompt length in regression (24/32/44% vs 7/17/6%). Extra tokens gave 0.4%. Three models, synthetic tasks, no human control. The 93% drop is on REL-B1 (a history task), not a Raven task.
- Parallel branches (Patil, 7 models, 8B-235B): sharp collapse at 20-30 branches, the same for every size. The threshold did not move with parameter count. That differs from the human prediction that the peak shifts with capacity. Instruction-tuned models, probably without long reasoning.
- Operands and range (I-RAVEN-X): reasoning models 80.5% to 63.0%, plain 59.3% to 4.4%. With perceptual uncertainty the load effect is small next to the perception effect (o3-mini 86.6% to 17.0%).
- Unique rules (Webb 2023, GPT-3): rule diversity, not total count, matters (OR .25 for GPT-3). Not tested on reasoning models or images. Lewis and Mitchell 2024: GPT accuracy drops on counterfactual alphabets. Webb 2024 reply: code closes most of the gap (counting was the weak step).
- Attribute count (MaRs-VQA, GPT-4o + CoT): 57.78% at Level 1 to 21.74% at Level 5, non-monotone in the middle (only endpoints are safe).
- n-back: Gong 2024 says capacity about 3 for gpt-3.5-turbo. Hu and Lewis 2025 say task misunderstanding; a strong model reached 84.75-90.08% at 8 to 10-back.
- Binding capacity (Ravulapalli): K50 grows with parameters (exponent 0.82) up to 3B, but Pythia stays at 3-6 from 410M to 12B. Recall only.
- Raven-like text and images (NeuroCognition, 10 LLMs vs 11 humans): difficulty lowers scores (p<.001). Text beats image for LLMs. Humans fail to remember, LLMs fail to manipulate. One general factor holds 75% of variance over 156 models. The human RAPM text figures 0.430/0.444 come from a pilot of N=9; the 0.814 image figure is borrowed from another study. Disabling reasoning raised text MC for some models (p=.021). Two models had reasoning disabled because overthinking exhausted output limits.
- Collapse at high complexity (Shojaee 2025) vs output-limit artefact (Lawsen 2025, preliminary).

**What changed performance, by how much.**
- Code for indexing and counting: GPT-4 to human level (P=.496) on shuffled alphabets.
- Demonstrations: strong n-back results; gpt-4v gained up to 100% with symmetric CoT demos on one set (c23).
- More tokens: 0.4% to 3% at high RC. The best budget rises with item difficulty (1.0K to 7.5K), and AIME peaks near 10K.
- Model size: does not move the branch collapse; moves binding recall slowly.

**Caveats.** Many LLM results are 2026 preprints with 1 to 3 models. Output-length limits confound difficulty results. Perception confounds image items. Backward digit span against text Raven in 15 LLMs is snippet-only (a25).

## 7. What our agent should take

Status key: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Do not use rule count, or any structure count, as the budget rule or the difficulty measure.** Treat it as one weak feature. Schema part: G12. [E]. Evidence: a04, a09, b07 (K01, K04, K05).
2. **Never read one correlation or one load curve as proof of a capacity mechanism.** Any pattern fits. Require a sweep over capacity levels before claiming one. Schema part: G7 and G12. [E]. Evidence: b01, b02, a10 (K03).
3. **Check floor and ceiling before reading any difficulty slope.** Drop items with pass rate near 0 or 1 from per-difficulty analysis. Schema part: memory (S9 class record). [E]. Evidence: b04, a11, a03.
4. **Check by code that an apparent capacity failure is not a task misunderstanding or an output cut-off.** Log truncations; test whether answers fit a different task. Schema part: S1 and S4. [E] for the confound (Hu and Lewis; Lawsen); the capacity reading itself is [C]. Evidence: c11, c12, d12 (K14).
5. **Send exact indexing, counting and enumeration to code.** Schema part: O3 and G5. [E] in direction (three sources); [C] when the model must still hold a joint set. Evidence: d11, d12, d10 (K22).

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Per-item fitted (1PL) difficulty from several agent variants sets the budget, instead of rule count | G12 | [S] | c26, d16, d17 (K17, K24) |
| Token cap set by difficulty class (cap-by-difficulty grid) | G11/G12 | [S] | d13, b10 (K23) |
| Relational-complexity estimate (jointly bound items) triggers decomposition | S2/O3 | [S] (two preprints) | b25, b26, d06 (K10) |
| Decompose by joint-binding count, not by length | O3 | [S] | b27, c16 |
| Fixed notes slot holding the current rule | S5 | [S] | c21, c20 (K18) |
| Unique-rule diversity as a difficulty feature | S2 | [S] | a20 (K11) |
| Separate perception from rule errors (symbolic input) | S1/S2 | [S] | b28, a23 (K12) |
| Distractor-count dial separate from load | G1 | [C] | d08, d09 (K08) |
| Several short attempts vs one long at high RC | G11 | [C] | c15, d10, d13 (K13) |
| Reasoning off for text multiple-choice matrix-like items | G11 | [S] | c20 (K15) |
| Capacity sweep (model size, context, notes) against item demand | G12 | open | d18 (K21) |

## 8. Concrete tests on our bench

All arms get equal total tokens. Report setup cost (G7).

1. **Rule-count budget vs fitted-difficulty budget.** Items: our task bank, coded for rule count and fitted by 1PL from at least 4 agent variants. Arms: A tokens by rule count; B tokens by fitted difficulty; C both. Metric: pass rate at equal total tokens. Expected: B at least C, both above A; A near a uniform budget (K01, K24).
2. **Cap-by-difficulty grid.** Items in 4-5 difficulty bands. Caps of 1x, 2x, 4x, 8x a base. Metric: pass rate by band and cap, plus overthinking flips. Expected: optimal cap rises with band; one global cap loses to per-band caps (K23, K06).
3. **Capacity sweep (the Frischkorn design).** Three capacity levels: plain; plus notes slot; plus notes and code decomposition (or two model sizes). Items graded by fitted difficulty. Metric: where the item-demand curve breaks, and whether the break moves with capacity. Expected: if capacity matters, the break moves right. Patil predicts no move without a structural change (K19, K21).
4. **Relational-complexity decomposition.** Items with RC fixed while entity count varies, and the reverse. Arms: decompose when RC is over threshold; decompose by length; no decomposition. Metric: pass rate at high RC. Expected: the RC trigger beats the length trigger (K10).
5. **Novelty vs repetition.** Items with novel vs repeated rule combinations at the same difficulty. Metric: failure-rate difference. Expected: none (K05).
6. **Unique rules at fixed total.** Hold total rules fixed, vary unique rules. Metric: accuracy. Expected: more unique rules, lower accuracy (K11).
7. **Distractor-length sweep.** Add irrelevant text at fixed reasoning load. Metric: accuracy slope against distractor count and against load. Expected: separate dials (K08).
8. **Notes slot for the current rule.** With and without a fixed rule note, on rule-switching items. Metric: perseveration errors and pass rate. Expected: fewer set-maintenance errors (K18).
9. **Truncation audit.** On every test above, log output cut-offs and answers that fit a different task. Exclude or flag affected runs.

## 9. What does not transfer, and why

- **The correlational design.** It needs many people with varied capacity. We have one agent or a few variants. Use accuracy against manipulated demand instead.
- **Human working-memory span.** An LLM context holds the full text, so maintenance load is largely removed (NeuroCognition gave full history). LLM failure is in manipulation and binding, not storage (c19).
- **Rule-token counts from Carpenter.** Hand-coded for one test, confounded with item position, and a weak predictor of the WM link even in humans.
- **Time-pressure findings.** Contested in humans (Colom). A token cap is only an analogy.
- **WM training result.** No direct agent analogue; training is outside our scheme (K07).
- **Parameter count as capacity.** Binding capacity and the branch threshold do not scale cleanly with size (K19, K20).
- **Raven image items.** They add a perception confound (b28, c19).

## 10. Open questions

1. What are the Dokic 2025 review's study count, inclusion rule and coding? Full text is paywalled.
2. Has Little 2014 been replicated outside its lab with a multi-task composite? Its own second study's supplement is unread.
3. Does any LLM study cross several capacity levels with item demand on reasoning items?
4. Does relational complexity beat fitted IRT difficulty for LLMs? Does fitted difficulty rank items the same across models?
5. Does the Webb unique-rule effect hold for reasoning models and image items?
6. How much of REL's collapse is an output-limit effect (Lawsen)? What happens when the agent decomposes by code at fixed tokens?
7. Does a token cap shift LLM failures to hard items on Raven-type items? The direction is known on MATH (K23).
8. What do Carpenter 1990 and Kyllonen and Christal 1990 actually report? Never opened.
9. Is attention control (distractors) a better model of LLM failure than capacity?
10. Is an LLM capacity score (binding count) linked to reasoning item demand at all?

## 11. Sources

[V] opened, [M] snippet or second-hand only.

- [M] Carpenter, Just and Shell 1990, Psych Review 97, 404. https://doi.org/10.1037/0033-295X.97.3.404 (via Little 2014 and Frischkorn)
- [M] Kyllonen and Christal 1990. https://doi.org/10.1016/S0160-2896(05)80012-1
- [V] Unsworth and Engle 2005. https://www.gwern.net/doc/dual-n-back/2005-unsworth.pdf
- [M] Wiley, Jarosz, Cushen and Colflesh 2011. https://doi.org/10.1037/a0021613
- [M] Salthouse 1993. https://doi.org/10.1016/0160-2896(93)90019-8
- [V] Salthouse and Pink 2008. https://uva.theopenscholar.com/files/vcap/files/why_is_working_8.pdf
- [M] Embretson 1995. https://doi.org/10.1016/0160-2896(95)90031-4
- [V] Little, Lewandowsky and Craig 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC3968765/ (supplement not read)
- [V] Smolen and Chuderski 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4547002/
- [V] Harrison, Shipstead and Engle 2015. https://englelab.gatech.edu/articles/2015/ (n=208 complete; the N=99 in b19 is wrong)
- [V] Frischkorn and Oberauer 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8367890/
- [V] Dokic, Koso-Drljevic and Bilalic 2025, Intelligence 108, 101874. https://doi.org/10.1016/j.intell.2024.101874 ; https://idiprints.knjiznica.idi.hr/1181/ (abstract pages only)
- [V] Burgoyne, Hambrick and Altmann 2019. https://doi.org/10.3758/s13423-019-01606-9 (abstract only)
- [V] Chuderski 2013. https://www.gwern.net/doc/dual-n-back/2013-chuderski.pdf
- [V] Chuderski 2015. https://www.gwern.net/doc/dual-n-back/2015-chuderski.pdf
- [V] Colom et al. 2015. https://www.gwern.net/doc/dual-n-back/2015-colom.pdf
- [V] Melby-Lervag, Redick and Hulme 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC4968033/
- [V] Burgoyne and Engle 2020. https://englelab.gatech.edu/articles/2020/Burgoyne_Engle_2020_CD.pdf
- [M] Unsworth, Miller and Strayer 2024. https://pubmed.ncbi.nlm.nih.gov/38769271/
- [M] Kovacs and Conway 2016. https://www.gwern.net/doc/iq/2016-kovacs.pdf
- [V] Webb, Holyoak and Lu 2023. https://arxiv.org/abs/2212.09196
- [V] Webb, Holyoak and Lu 2024. https://arxiv.org/abs/2404.13070
- [V] Lewis and Mitchell 2024. https://arxiv.org/abs/2402.08955
- [V] Haznitrama, Ardi and Oh 2026 (NeuroCognition). https://arxiv.org/abs/2603.02540
- [V] Li 2025, rule omission. https://arxiv.org/abs/2510.03127
- [V] Camposampiero et al. 2025, I-RAVEN-X. https://arxiv.org/abs/2510.17496
- [V] Camposampiero et al. 2025, reasoning models on I-RAVEN. https://arxiv.org/abs/2503.11207
- [V] Gong, Wan and Wang 2024. https://arxiv.org/abs/2305.03731
- [V] Hu and Lewis 2025. https://arxiv.org/abs/2412.18120
- [V] Gong and Zhang 2024. https://arxiv.org/abs/2409.10715
- [M] Backward digit span in 15 LLMs. https://escholarship.org/content/qt28m3k4g4/qt28m3k4g4.pdf
- [V] Fesser et al. 2026 (REL). https://arxiv.org/abs/2604.12176
- [V] Patil et al. 2026. https://arxiv.org/abs/2604.06799
- [V] Ravulapalli and Chadha 2026. https://arxiv.org/abs/2609.30634
- [V] Ghaffari et al. 2026. https://arxiv.org/abs/2609.22101
- [V] Shojaee et al. 2025. https://arxiv.org/abs/2506.06941
- [V] Lawsen 2025. https://arxiv.org/abs/2506.09250
- [V] Zhou et al. 2026. https://arxiv.org/abs/2604.10739
- [V] Jiang et al. 2024. https://arxiv.org/abs/2401.12117
- [V] Li et al. 2026 (RIDE). https://arxiv.org/abs/2511.04120
- [V] Ding et al. (Easy2Hard-Bench). https://arxiv.org/abs/2409.18433
- [V] Ge et al. 2026 (Agent Psychometrics). https://arxiv.org/abs/2604.00594
- [V] MaRs-VQA authors 2025. https://arxiv.org/abs/2406.10424
- [V] Galanti and Baron 2024. https://arxiv.org/abs/2407.18968

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 3 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A13.04-K01** (reworded: the sources support less). Salthouse and Pink (2008, nearly 1,000 adults) varied WM-task set size, not Raven item difficulty (and found Gf effects slightly larger at higher set sizes); it does not test the item-wise WM-Raven curve. Unsworth and Engle show a slight decrease, Little 2014 a moderate increase. Corrected claim: Across studies the WM-Raven item correlation does not reliably rise with item difficulty; flat, slightly falling or inverted-U curves are the usual result (Unsworth and Engle 2005 N=160; Smolen and Chuderski 2015 N=347 and 939, overlapping data; Burgoyne 2019; Dokic 2025 N=543 by item difficulty, rule tokens and latent growth models), though Little 2014 found a moderate increase. Salthouse and Pink 2008 (nearly 1,000) varied WM-task set size, not Raven item difficulty, and found Gf effects only slightly larger at higher set sizes. The Dokic review calls the evidence mixed with most studies null; its study count is not stated.
- **A13.04-K09** (reworded: the sources support less). Salthouse and Pink supports the set-size and trial-order point (latent r .74 and .86, but Gf effects were slightly larger at higher set sizes); Colom 2015 tested RAPM administration time (latent r .74 and .96 by time group, weighted .86), not set size or trials. Corrected claim: The latent WM-Gf correlation is high (.74 to .96 across latent models) and was not reduced by larger set size or later trials in the WM tasks (Salthouse and Pink 2008, nearly 1,000 adults; Gf effects were if anything slightly larger at higher set sizes) or by longer Raven administration time (Colom 2015, weighted r = .86), so strong WM-Gf overlap does not by itself show a load-driven mechanism.
