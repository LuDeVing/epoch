# Choice architecture and nudging: deep document

*Subfield E18.05. Sources: evidence_a-d.jsonl (a01-a25, b01-b26, c01-c27, d01-d17), claims.jsonl (K01-K34), critique.md. Status marks: [E] established, [S] single-source, [C] contested. Evidence ids are in brackets. "V" means the page was opened; "M" means snippet, memory or second-hand only.*

## 1. What it is

Choice architecture is the design of the setting in which a choice is made. It covers which option comes first, which option is pre-selected, how the same facts are worded, which numbers are visible, and how many options are shown. A nudge is a change to this setting that moves behaviour without banning options or changing prices. Thaler and Sunstein (2008, *Nudge*) gave the term. The definition is broad: any layout is a nudge, because something has to be shown first [a01, V via Wikipedia].

Three families appear in the main meta-analysis [b02]:

- **Structure** (defaults, effort, option range and composition).
- **Information** (reminders, framing, social norms, translation).
- **Assistance** (commitment, planning tools).

Why it matters for our agent. A language model reads a prompt, and a prompt is a layout. The order of options, a pre-filled answer, a gain or loss wording, an irrelevant number, a "recommended" badge, and the position of a fact in a long context all act as nudges. The machine evidence shows that these layout effects are measured directly on models and are often large [b25, c26]. The human literature, in contrast, has shrunk under scrutiny. So the stance of this document is: **layout is a risk to control in the scaffold, not a lever to exploit.** The program should fix the layout, counterbalance it, and aggregate over it (guardrail G5: code selects).

Links to other subfields in this run (not covered here): Nudge evidence, Debiasing and cognitive forcing, Layout and presentation, Cognitive bias and premature closure, Dual-process theory, Aggregation and extremizing.

## 2. History and theories in depth

**Prospect theory and framing (1979-1981).** Kahneman and Tversky (1979) and Tversky and Kahneman (1992) model value as gains and losses from a reference point. From memory [a07, M]: loss aversion lambda about 2.25, curvature about 0.88, probability weight gamma about 0.61. The theory does not say what sets the reference point. The frame does. In the Asian disease problem (1981) the same outcomes are described as lives saved or lives lost. Gain frame: 72% chose the sure program. Loss frame: 78% chose the risky one. Original sample 152 students [a06, d09; second-hand, M].

**Status quo bias (1988).** Samuelson and Zeckhauser gave people a current option and measured switching. It is the template for later default work and for LLM tests [b20, M].

**Planner-doer and dual-process models (1981, 2011).** Thaler and Shefrin's planner-doer model and Kahneman's System 1 and 2 give the usual story: automatic choices follow the layout; deliberate choices should not [a08, M]. This dual-process split is contested (see the Dual-process theory subfield).

**Defaults in the field (2001-2004).** Madrian and Shea (2001) studied automatic 401(k) enrolment in one firm. Participation was 86% in the auto-enrolled cohort against 37% at 3-15 months tenure in the earlier cohort [a03, V]. Johnson and Goldstein (2003) compared opt-in and opt-out countries for organ donation and found consent gaps of about 60 percentage points [a02, b21, M, from memory]. Thaler and Benartzi (2004, Save More Tomorrow) used pre-commitment to future raises; saving rose from 3.5% to 13.6% in one firm, from memory [a05, M].

**Book and policy wave (2008-2015).** *Nudge* led to government "nudge units" (UK, US). They ran many randomized trials.

**Meta-analytic wave and correction (2019-2022).** Jachimowicz et al. (2019) pooled defaults: d = 0.68 [d07, V]. Mertens et al. (2022) pooled all choice architecture: d = 0.45 [b01]. Maier et al. (2022) re-analysed the same data for publication bias and found d near 0.04 to 0.11 [b03]. DellaVigna and Linos (2022) compared published papers with all trials from two nudge units: 8.7 pp against 1.4 pp [b05]. The field now agrees that heterogeneity is real and that the mean is smaller than first reported. It does not agree on how much smaller.

**Competing accounts of why defaults work** [b09, d07]:

1. *Effort*: changing the option costs work.
2. *Endorsement*: the default reads as advice.
3. *Status quo or reference point*: the default becomes what you already have (endowment, loss aversion).

In the only coded meta-analysis, endorsement (b = 0.32, p = .038) and endowment (b = 0.31, p = .044) were significant moderators; ease was not (b = -0.05) [d07]. These were coded by raters, not measured. For an LLM, endorsement is the closest analogue: text that marks an option is read as advice. Effort has no direct analogue.

**LLM wave (2021-2026).** Work on few-shot ordering (Zhao 2021, Lu 2022) found order swings accuracy from chance to near state of the art [c07, c09]. Jones and Steinhardt (2022) borrowed human-bias experiments to find model failures [b16]. Binz and Schulz (2023) ran cognitive tests on GPT-3 [a17]. Then came positional-bias studies (Liu, Zheng, Wang, Pezeshkpour, Sclar) and agent-behaviour studies (Cherep 2025/2026, Allouah 2025, Halimeh 2026). The newest results ask whether reasoning budget removes nudge sensitivity.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Auto-enrolment raised 401(k) participation | 86% in auto cohort vs 37% at matched 3-15 months tenure (non-participation gap 48.5 pp in the 0% category) | Madrian & Shea 2001 [a03] | [E] for direction; one firm, not randomized |
| Default carries its details | Among participants, 76% kept the default 3% rate; 80% of money in the money market fund; 61% of all NEW employees sat at 3% plus money market vs 1% in older cohorts. Different denominators: do not mix | Madrian & Shea [a04] | [S] |
| Organ donation defaults (registration, not donation) | Opt-in effective consent 4.25% (Denmark), 12% (Germany), 17.17% (UK), 27.5% (Netherlands); opt-out 98-99.98% (from memory) | Johnson & Goldstein 2003 [a02] | [M] unread, correlational |
| Welsh soft opt-out did not raise donors | Deceased donors 101 vs 104; consent 61.0% vs 45.8% dip; rest of UK rose 58.6% to 63.1% | Noyes 2019 [d08] | [S] before-after, short term |
| Default meta-analysis | d = 0.68 [0.53, 0.83], 58 studies, n = 73,675; binary studies 27.24 pp; trim-and-fill moves UP to d+ = 0.80 | Jachimowicz 2019 [d07] | [E] raw; correction [C] |
| Pooled nudge effect, raw | d = 0.45 [0.39, 0.52]; 455 effects, 214 publications, N = 2,149,683; I2 = 99.67%; prediction interval [-0.48, 1.39], about 15% backfire | Mertens 2022 [b01] | [E] raw; size [C] |
| By category and technique | Structure 0.55 (k = 227), information 0.38, assistance 0.31; default 0.62 (k = 132, N = 139,948), composition 0.55, reminder 0.30; food 0.72, health 0.34, finance 0.25 | Mertens [b02] | [S] not bias-corrected |
| Bias-corrected nudge effect | RoBMA d = 0.04 [0.00, 0.14]; most precise estimates 0.11 [0.00, 0.24]; BF01 0.95 and 0.31 (undecided); information BF01 33.8; finance 41; structure adjusted 0.12 [0.00, 0.43], BF01 1.1 (undecided) | Maier 2022 [b03] | [C] |
| Original authors' sensitivity | d = 0.31 moderate bias; 0.08 severe (paper text says 0.03; unresolved) | Mertens reply [b04] | [C] |
| At-scale vs published nudges | 126 RCTs, over 23 million people. Nudge units 1.4 pp (s.e. 0.3), 8.1% over control 17.2. Journals 8.7 pp (s.e. 2.5), 33.5% over 26.0. About six times. Bias-corrected academic 3.2 pp. Median arm 10,006 vs 484 people | DellaVigna & Linos [b05, b06] | [E] |
| Expert forecasts overshoot | Academics median 4 pp, practitioners 1.95 pp, actual 1.4 pp | [a13] | [S] |
| Choose vs reject framing beat a default (humans) | N = 1,072; framing OR 0.46 [0.29, 0.72]; default OR 0.49 in work scenario; no default effect in health | Framing the Default 2024 [b08] | [S] hypothetical |
| Human framing replicates | Many Labs: d = 0.60 (chi2 = 516.41; 31 of 36 sites); Kuhberger 1998 d about 0.31; Steiger & Kuhberger 0.52 corrected; ML2 discount scenario d = 0.40 | [d09, d10] | [S] second-hand, M |
| Gain/loss wording moves LLMs | ChatGPT 5 vs 4 on a 1-7 scale, all 11 trials each (humans 5.2 vs 4.6); Codex 50% to 17% (unary vs binary first); GPT-4 admits 40.5% more under reject framing; GPT-3 framing and certainty effects | [c02, b16, a15, a17] | [E] on 2022-24 models |
| Irrelevant anchor moves LLMs | ChatGPT 20.83 low vs 105.97 high anchor, t(58) = 8.78 (humans 22.5 vs 80.5); GPT-4 22.0 vs 94.33 (5 trials per cell); HumanEval 32.9 falls to 2.4-10.6 with distractors; framing line copied in 62-93% | [c01, c05] | [E] |
| Option slot shifts accuracy | 0-shot MMLU: gpt-3.5 67.2 to 60.9 (gold to D); llama-30B 53.1 to 68.2 (gold to A), 41.2 (to D); balanced picks 34.6/27.3/22.3/15.8% for A/B/C/D; reorder gap 13% to 75% | Zheng [b10, a21], Pezeshkpour [a22] | [E] older models |
| Few-shot order | Sentiment 54% to 93% across orderings; entropy selection +13% over 11 tasks; order quality does not transfer (correlations near 0 or -0.24) | Zhao, Lu [c07, a19] | [E] older models |
| Prompt format spread | Up to 76 points (LLaMA-2-13B); GPT-3.5, 320 formats: up to 56, median 6.4 | Sclar [a23, c16] | [S] |
| Lost in the middle | 20 docs: 75.8 first, 53.8 index 9, 63.2 last; closed-book 56.1. 30 docs 73.4 / 50.5 / 63.7. Claude-1.3 59.1 first, 54.8 mid, 59.9 last. Longer windows no fix (59.8 vs 59.9) | Liu [c10, b15, c11] | [E] 2023 models |
| U-shape depends on fill | Peaks near 0.25-0.38 of window; end bias beyond; present at initialization | Veseli 2025, Chowdhury 2026 [d05, d06] | [E] open models |
| Judge verdict flips on order swap | Conflict GPT-4 46.3% / 5.0%, ChatGPT 82.5% / 52.5%; Vicuna win 2.5% vs 82.5% by slot | Wang 2023 [b12] | [E] |
| Order balancing plus evidence first | ChatGPT scoring 44.4% / kappa 0.06 / conflict 82.5% to 58.7% / 0.31 / 35.0% (best k = 3) | Wang [b13] | [E] |
| Newer judges | Position bias 0.04 or less; style bias 0.10-0.76; swap plus merged CoT+rubric +7.5 to +11.5 pp on MT-Bench; plain swap -6.5 to -11.1 pp on LLMBar | Soumik 2026 [d04] | [S] |
| Agents accept defaults and suggestions | Default accept: human 0.51 to 0.88; GPT-3.5 0.33 to 0.99; Gemini 1.5 Flash 0.94; GPT-4o, Claude 3 Haiku, o3-Mini 1.0; Claude 3.5 Sonnet 0.89-0.91 | Cherep [b18, d03] | [E] |
| Shopping agents: position and badge | Top-row coefficient Sonnet 4 1.224, GPT-4.1 1.045, Gemini 2.5 Flash 0.344; Overall Pick badge +1.060 / +0.802 / +1.897; Sponsored tag negative; sign differs by model and flips across versions | Allouah 2025 [c17, c18] | [E] |
| Reasoning moves nudge pull, does not remove it | Six 2026 models, 21,600 runs: default OR 8.70, social OR 37.24; default share 92% (no reasoning) to 86% (high); social 96% to 98% | Halimeh 2026 [d01] | [C] preprint, ceilings |
| No-deliberation scorers take defaults | 97.5-99.9% on defaults; social 75-96%; control 47-49% | Kaltenpoth 2026 [d02] | [S] small models |
| Candidate text can be tuned to win | Seller edits: +3.66 to +14.89 pp market share (Gemini 3 Pro +0.32 n.s.); optimised string raised rank in about 40% of 200 runs; Bing 2.5x | [c18, d12, d13] | [S] |
| Capability removes plain errors faster than layout bias | Price-dominance failures 63% (Sonnet 3.5) to near zero; position effects persist | Allouah [c19] | [S] |
| Framing words cause directional error | Up to 94% for "equal" in non-CoT; DeFrame multi-framing cut BBQ framing disparity 92%, bias score 93% | [d15, d14] | [S] |
| Anchor hints | 162 distribution differences, 11 sign exceptions; "ignore" hints, CoT and reflection no significant gain on GPT-4/4o; expert-labelled anchors strongest | Lou & Sun [d11] | [S] weak source |

## 4. Mechanisms and models

Each mechanism is written so it can be coded.

**4.1 Default as prior plus copy.** For a model, a pre-filled or sample answer in the prompt raises the probability of that answer. Two sub-mechanisms:

- *Copy bias*: any value present in context is easy to emit. Test: unmarked sample.
- *Endorsement*: text that says "recommended", "suggested" or "default" is read as advice. Test: marked sample.

Implementation: keep the model-facing prompt free of any candidate answer. If a reference answer is needed (for example a prior attempt), the program decides when to show it (G2, G5) and labels it neutrally. Measure copy rate = share of final answers equal to the planted value when it is wrong.

**4.2 Token and position bias in multiple choice.** Zheng et al. show the bias lives mainly in the letter tokens: relabelling to a/b/c/d or 1/2/3/4 did not remove it [b11]. PriDe estimates the prior over option IDs on about 5% of items using permuted copies, then subtracts it. It needs output probabilities. Without logits, use cyclic permutation in code:

```
for k in range(n_options):
    order = rotate(options, k)
    ans[k] = model(prompt(order))   # map back to option content, not letter
final = majority(ans)               # code votes
```

Cost is n_options calls. Zheng et al. report the cheap prior estimate beats full permutation at lower cost [b11] (the 2%-20% stability claim is not re-verified, per critique).

**4.3 Position in long context (U-shape).** Accuracy is high for facts at the start or end and low in the middle, strongest at or below half of the window [d05]. Rule: put rules and key evidence first, the live question last, bulk material in the middle. A tested placement is better than a guess because the sign flips across model versions [c18].

**4.4 Order-balanced judging.** For any pairwise comparison, score both orders and combine. Evidence first, then score, with k = 3 evidence samples, helped most [b13]. Caveat from 2026 judges: if disagreement across orders is treated as a tie, clear-cut pairs lose accuracy (-6.5 to -11.1 pp on LLMBar) [d04]. So swap only when the two scores are close, or merge scores instead of declaring a tie.

**4.5 Neutral restatement (S1).** The program rewrites the task statement into plain, neutral wording before solving. Echterhoff's self-help method lets the model rewrite its own prompt to strip biasing parts; GPT-4 framing gap went -0.405 to -0.010, while awareness and contrastive instructions left it near baseline (-0.470, -0.410) [b17]. DeFrame uses several framings and checks agreement [d14]. Unsolved: no study audits that a rewrite keeps the meaning. Needed check: solve the original and the rewrite on items with ground truth, and compare accuracy as well as bias.

**4.6 Format randomization.** Meaning-preserving format changes move accuracy by a median of 6.4 points (GPT-3.5) and up to 76 (LLaMA-2-13B) [c16]. Mechanism: unknown; probably surface-token statistics. Remedy: evaluate every arm on 5-10 formats and report the range, or vote across formats.

**4.7 Selection pressure on candidate text.** Seller edits and optimised strings raise the chance of being picked [c18, d12, d13]. Treat retrieved or candidate text as adversarial in selection steps. Exaggerated claims work; plain praise did not [d13]. Code-side stripping of persuasion cues is an untested idea.

**4.8 Pre-commitment (code-side).** Save More Tomorrow works by deciding now what future-you must do [a05]. The analogue: lock checks and ordering before the model sees the problem (G2, G3).

## 5. What holds up

**Holds up.**

- Defaults raise take-up of the default option in humans. Direction is robust: 46 of 58 default observations significantly positive, 10 not, 2 negative [d07]. Size is disputed.
- Heterogeneity is real. I2 = 99.67%, prediction interval -0.48 to 1.39, about 15% backfire [b01]. All camps accept this [b04, b26]. Moderators matter more than the mean (K25).
- Published nudge effects exceed at-scale effects by about six times. Selective publication plus low power explains the whole gap: non-significant results were published with probability 0.1, and published studies have more than four times as many t values in 1.96-2.96 as just below [b06].
- Human framing replicates in large samples (d = 0.60 in Many Labs; about 0.3-0.5 after correction) [d09, d10]. Second-hand.
- Machine layout effects (option order, slot, long-context position, few-shot order, format) replicate across many labs and models [b10, a22, c07, c10, a23].

**Failures and corrections.**

- Mean nudge effect after correction: 0.04-0.11 (Maier) [b03]. Information and assistance nudges show evidence against an effect (BF01 33.8 and 9.1). Structure is undecided (BF01 1.1).
- The correction itself is contested. Jachimowicz's trim-and-fill moved the default effect up, 0.68 to 0.80, the opposite direction [d07]. Egger tests are weak under high heterogeneity. Szaszi et al. also find smaller or null effects [b26, second-hand].
- Welsh opt-out: stated consent moved slightly; actual deceased donors did not (101 vs 104), and the rest of the UK rose as much [d08]. A default can move the stated choice more than the real outcome (K32).
- Nudge units rarely changed defaults, so the six-times gap is partly a mix effect [b05].
- Human status quo and default effects do not carry over cleanly to models: most models chose the stated status-quo option less [a15], yet agents accept prompt defaults at 0.94-1.0 [b18]. Different tasks; nobody has run both on one model (K16 [C]).
- Seven LLMs were irrational mostly in non-human ways and inconsistent across repeats [c23]. Human bias lists predict LLM errors poorly.
- Instruction tuning can raise some biases: decoy effect rose in GPT-4 while certainty and belief bias fell [c22, S].

**Moderators.**

- Human: category (structure > information > assistance), domain (food 0.72 > health 0.34 > finance 0.25), endorsement (b = 0.32), consumer vs environmental contexts (b = 0.89 vs -0.60) [b02, d07]. Region and population did not matter in Mertens (p = .60, .26).
- LLM: model and version (position sign flips; Gemini preview to release inverted) [c18]; window fill (U-shape strongest at or below half) [d05]; quality gap between candidates (position bias bigger when answers are close) [b14]; task type (style bias 0.10-0.76 beats position bias 0.04 in 2025-era judges) [d04].

**Interventions that worked.**

- Evidence-first scoring plus balanced order (agreement 44.4% to 58.7%, conflict 82.5% to 35.0%) [b13].
- PriDe prior estimation on about 5% of items [b11].
- Self-help rewriting (framing gap -0.405 to -0.010) [b17].
- Multi-framing consistency (BBQ framing disparity -92%) [d14].
- Swap plus merged CoT and rubric (+7.5 to +11.5 pp) [d04].

**Interventions that did not work.**

- "Ignore the order" instructions: judge conflict unchanged [b12].
- Awareness and contrastive prompts: framing gap stays near baseline [b17].
- "Ignore the hint", chain of thought, reflection: no significant gain on anchoring in GPT-4/4o [d11].
- Zero-shot chain of thought shifts choices but does not remove nudge sensitivity [b19]. Few-shot human examples align behaviour but leave hypersensitivity [b19].
- Longer context windows: no fix for lost-in-the-middle [c11].
- Bigger models, more shots, instruction tuning: format spread persists [a23].
- Relabelling letters: token bias stays [b11].

## 6. Language models

**Direct evidence by effect type.**

*Framing.* GPT-3 reproduces certainty and framing effects (3 of 6 prospect-theory effects) [a17]. ChatGPT gave 5 vs 4 with zero variance [c02]. Codex fell from 50% to 17% when a task was described binary-first [b16]. GPT-4 admitted 40.5% more under reject wording [a15]. In 2025, framing words caused directional error of up to 94% on "equal" cases for non-CoT prompts [d15]. Negative framing gives about twice the bias of positive framing on BBQ (up to 4x) [d14].

*Anchoring.* ChatGPT 20.83 vs 105.97 for low and high anchors, close to humans [c01]. Wrong anchor code copied in 58-93% of outputs; accuracy dropped from 32.9 to 2.4-10.6 [c05]. Mitigation prompts did not help GPT-4 and GPT-4o [d11].

*Order and slot.* Gold moved to D costs gpt-3.5 6.3 points; moved to A lifts llama-30B 15.2 [b10]. Reorder gaps of 13-75% [a22]. Few-shot order swings 54% to 93% [c07]. Format changes: up to 76 points [a23].

*Long context.* 75.8 first, 53.8 middle, 63.2 last for GPT-3.5-Turbo at 20 documents; below closed-book at the middle [c10]. Later work: U-shape strongest below half fill, end bias above [d05]; present before training [d06]. Frontier 2026 reasoning models are untested.

*Judges.* Conflict on swap 46.3% (GPT-4) and 82.5% (ChatGPT) in 2023 [b12]. By 2026, five judges show position bias of 0.04 or less but style bias of 0.10-0.76 [d04]. Shi et al. (2025, 15 judges, over 150,000 evaluations) say position bias depends on judge, task and quality gap [b14].

*Defaults and suggestions in agents.* Cherep: GPT-3.5 0.99, Gemini 1.5 Flash 0.94, GPT-4o, Claude 3 Haiku and o3-Mini 1.0 on default nudges, against humans 0.88. Human score about 172 points; most models 134-159; only Gemini 1.5 Pro (166) and Claude 3.5 Sonnet (170) matched humans in late suggestion trials [b18, d03]. Halimeh (2026, six models): default OR 8.70 and social OR 37.24; Claude Sonnet 4.6 social 100% at both reasoning levels; Claude Haiku 4.5 default 100% and 99.3% [d01].

*Shopping agents.* Position and badge effects differ by model and version. Scarcity tags: only Gemini 2.5 Flash significant (-0.342) [c17]. Sellers can edit text to win (+3.66 to +14.89 pp) [c18].

**What changed the effects, and by how much.**

| Change | Effect | Source |
|---|---|---|
| Relabel option IDs | No removal | [b11] |
| "Ignore order" instruction | Judge conflict not fixed | [b12] |
| Awareness / contrastive instruction | Framing gap near baseline | [b17] |
| Self-help rewrite | Framing gap -0.405 to -0.010 | [b17] |
| Evidence first plus order balancing | Agreement 44.4 to 58.7; conflict 82.5 to 35.0 | [b13] |
| Swap plus merged CoT+rubric | +7.5 to +11.5 pp (MT-Bench) | [d04] |
| Plain swap, tie on disagreement | -6.5 to -11.1 pp on clear-cut pairs | [d04] |
| Zero-shot CoT | Shifts choices; pull remains | [b19] |
| High reasoning budget | Default share 92 to 86%; social share 96 to 98% | [d01] |
| o3-Mini (reasoning model) | Defaults 1.0 but resists late suggestion (0.15 vs human 0.34) | [d03] |
| Newer, stronger model | Plain errors near zero; position bias persists, sign flips | [c19, c18] |
| Multi-framing consistency | BBQ framing disparity -92% | [d14] |

**Reading.** Capability removes plain errors faster than layout bias (K21). Reasoning moves which nudge works rather than removing nudges (K28 [C]). Instruction-only guards are weak (K14). Code-side guards work (K15). Most older numbers are from 2022-2023 models; only Allouah, Cherep, Halimeh, Soumik and DeFrame use 2025-2026 models, and none uses a scaffolded agent. No study compares layout guards at equal tokens on one reasoning model (K34 open).

## 7. What our agent should take

Schema parts: G = guardrails G1-G12, S = states S0-S9, O = operators O1-O8, memory = section 5 of SCHEMA.md.

### Add now (established)

1. **Never let one fixed option order decide a multiple-choice or ranking answer.** Cyclic permutation in code, vote in code. G5. [E] K09, K14. Evidence: b10, b11, a21, a22, c12, c14, c04. Cost: up to n_options calls; count it under G7.
2. **Order-swap every pairwise judgment; combine scores in code.** G5, G8. [E] for swap (K13: b12, b13, c15, b14, d04); the swap-only-when-close refinement is [S] (K29, d04).
3. **Do not rely on instructions like "ignore order" or "be unbiased".** The guard is in code. G1, G5, G10. [E] K14. Evidence: b12, c15, c18, a16, b17, c21, d11, d01.
4. **Keep reference answers, sample values and anchors out of the model-facing working prompt unless the program shows them on a signal.** G2, G5, S1. [E] K08, K17. Evidence: c01, c05, c06, b16, b18, c17.
5. **Place rules and key evidence at the start of the prompt and the live question at the end; keep bulk text in the middle.** Prompt layout. [E] K12, K30. Evidence: a20, b15, c10, c11, d05, d06. Limit: 2023 and open models only.
6. **Do not hand-pick a few-shot order; shuffle per call and aggregate.** G5. [E] K10. Evidence: a19, c07, c09.
7. **Re-test every layout rule on each model version; do not port rules across models.** G7. [E] K19. Evidence: c17, c18, a19, b14.
8. **Treat the average nudge effect as small. Log task type, model and option count with every layout test; report every variant tried.** G7. [E] K04, K25. Evidence: b05, b06, b01, b26.
9. **Repeat each probe 5 or more times and test the model directly, not from a human bias list.** G7. [E] K22. Evidence: c23, a15, c20.

### Test first (single-source or contested)

1. **Neutral restatement (S1) of gain/loss or choose/reject wording, with a meaning check, versus multi-framing agreement.** S1. Framing moves models is [E] (K07: a17, a18, c02, c04, b16, a15, c20), but the remedy is [S] (K33: d14, d15, a16).
2. **Format spread across 5-10 prompt formats; vote across formats.** G5. [S] K11. Evidence: a23, c16.
3. **Endorsement vs copy bias: marked vs unmarked sample answer.** G5. [S] K23. Evidence: b09, d07, d11, d02.
4. **Marked default and social-proof line at low and high thinking.** G1, S1. [C] K28. Evidence: d01, d03.
5. **Swap-always versus swap-only-when-close for judges, with style cue stripping.** S6. [S] K29. Evidence: d04.
6. **Strip persuasion cues from candidate and retrieved text before selection.** G5, memory. [S] K26. Evidence: c18, d12, d13.
7. **Pre-commit checks and ordering in code before the model sees the problem.** G2. [S] K27. Evidence: a05 (numbers from memory).
8. **Choose vs reject wording flip rate.** S1. [S] K24. Evidence: b08, a06.
9. **Matched battery (default, order, framing, badge) on one model: does the human sign carry over?** G5. [C] K16, K34. Evidence: a15, c20, b18.
10. **Base-like versus tuned variants on decoy items.** No schema part. [S] K20. Evidence: c22.

Not carried into the schema: any claim about mean nudge size, organ donation as a model for prompt defaults, or Save More Tomorrow numbers.

## 8. Concrete tests on our bench

All arms use equal total tokens (G7). Where an arm makes k calls, the baseline gets k samples with fixed layout. Report accuracy, flip rate, and the range over layouts. Log model, version, option count.

| # | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Multiple-choice items with known gold (BrainTeaser, lettered ARC-like) | A: fixed order, k samples. B: cyclic permutation + code vote, k calls total | Accuracy; share of answers that move when the gold slot changes | B at least +2 pp where A shows a slot gap above 5 pp; no gain if the model is slot-robust |
| T2 | Same items, gold placed in each slot | A: plain. B: "ignore position" instruction. C: code permutation | Accuracy by gold slot; slot spread | B spread about equal to A; C spread shrinks |
| T3 | Wrong sample answer planted in prompt | A: no sample. B: unmarked wrong sample. C: sample marked "suggested" | Copy rate of the planted answer; accuracy | C > B > A in copy rate if endorsement matters; B = C if copy bias |
| T4 | Irrelevant number anchor, numeric items with truth | A: no anchor. B: low and high anchor. C: anchor stripped by code | Mean absolute error; low-high gap | B gap large (older models 20.83 vs 105.97); C closes it |
| T5 | Gain vs loss and choose vs reject paired items with ground truth | A: original wording. B: S1 neutral restatement. C: three framings and agreement vote | Answer flip rate across wordings; accuracy on original vs rewritten | B cuts flip rate; accuracy equal on original and rewritten |
| T6 | Pairwise comparisons, clear-cut and close pairs | A: one order. B: always swap, tie on disagreement. C: swap only when scores are close, merge scores | Agreement with truth, split by clear vs close | B hurts clear pairs (-6.5 to -11.1 pp on LLMBar); C best |
| T7 | Key rule or fact at start, middle, end at 25% and 80% fill | Placement arms | Accuracy by placement | U-shape on weak models; small on frontier reasoning models |
| T8 | Few-shot items | A: one fixed order. B: shuffled per call plus vote | Accuracy; order-to-order variance | B equals or beats the best fixed order, lower variance |
| T9 | Items with 5-10 prompt formats (separator, casing) | A: one format. B: vote across formats | Accuracy range over formats | Median spread of several points; B narrows it |
| T10 | Candidate list with one candidate edited to sound best | A: raw. B: code strips superlatives and badges | Share won by the edited candidate; correct pick preserved | B lowers the win rate |
| T11 | Default / social-proof line on two-option items | Low vs high thinking, with and without the line | Copy rate at each level | Default share falls slightly with thinking; social share may rise (d01) |

Write the expected effect before each test and compare after (K06: experts overpredict).

## 9. What does not transfer, and why

- **Effort.** A human default works partly because changing it costs effort. A model has no effort cost to change an answer, so the effort account does not apply. The agent's default effect is copy or endorsement.
- **Loss aversion and status quo.** Models are not shown to be loss-averse. Echterhoff found status-quo options chosen less by most models [a15]. Do not import prospect-theory parameters (lambda 2.25) into the schema.
- **Population effect sizes.** Mean d of 0.43-0.45 or 0.04-0.11 describes humans in online and field studies. It says nothing about a model. Layout effects must be measured per model and task.
- **Organ donation and 401(k) numbers.** Field data with consent or enrolment outcomes, not answer accuracy. The Welsh case shows a stated choice can move while the real outcome does not [d08]. Measure correctness, not copy rate.
- **Persistence and durability.** Habit and inertia over months have no analogue within one run.
- **Ethics and autonomy debates.** Relevant to people; not to a scaffold.
- **Sign.** Position bias flips sign across models and versions [c18]. Zheng's preference for letter A is not a law.
- **2022-2023 numbers.** Most quoted LLM swings come from GPT-3, GPT-3.5, Vicuna, Llama-2 and early GPT-4. Newer models fix plain errors [c19] and may fix more.
- **Nudge-unit evidence.** Letters and emails, take-up outcomes; no mapping to prompts.

## 10. Open questions

1. Do layout effects (option order, default marker, framing, anchor) survive on current reasoning models in one matched battery at equal tokens? (K34)
2. Does code-side permute-and-vote beat an instruction-only guard and a single canonical layout on our items?
3. Does S1 neutral restatement remove framing without changing meaning? No audit exists.
4. Is the LLM default effect endorsement or copy bias? No marked vs unmarked test found.
5. Safe prompt zones for 2026 frontier and reasoning models: lost-in-the-middle and format spread are tested only on 2023-2025 mid-size or older models.
6. How many order swaps before returns vanish? Existing designs use one swap.
7. Is the Maier correction right for defaults, given trim-and-fill moves up (0.68 to 0.80)? Unresolved, as is the 0.08 vs 0.03 sensitivity figure in b04.
8. Does the PNAS 2026 full text of Cherep say reasoning restores human-like sensitivity only inconsistently? Only the abstract was opened.
9. Do scaffolded agents (program plus model) show the same effects as raw prompts? No study.
10. Can code strip persuasion cues from candidate text without removing real information?
11. Unread sources: Hagendorff (2023, CRT biases vanish in ChatGPT); Horton (2023); the Szaszi letter; the Many Labs primary PDF; Johnson and Goldstein original; Save More Tomorrow original; PMC12478545 (decision time and defaults).

## 11. Sources

Marks: [V] opened, [M] snippet, memory or second-hand only.

**Human founding and replication**
- [M] Johnson & Goldstein (2003) Do defaults save lives? https://doi.org/10.1126/science.1091721 (a02, b21)
- [V] Madrian & Shea (2001) The power of suggestion. https://www.nber.org/papers/w7682 (a03, a04)
- [M] Thaler & Benartzi (2004) Save More Tomorrow. https://doi.org/10.1086/380085 (a05)
- [M] Tversky & Kahneman (1981) Framing of decisions, via https://en.wikipedia.org/wiki/Framing_effect_(psychology) (a06, b22)
- [M] Kahneman & Tversky (1979); Tversky & Kahneman (1992) https://doi.org/10.1007/BF00122574 (a07)
- [M] Thaler & Shefrin (1981); Kahneman (2011) https://doi.org/10.1086/260971 (a08)
- [V] Nudge theory page (definition, critiques) https://en.wikipedia.org/wiki/Nudge_theory (a01, a25)
- [V] Jachimowicz et al. (2019) default meta-analysis https://doi.org/10.1017/bpp.2018.43 (d07; a14 and b07 were second-hand)
- [V] Noyes et al. (2019) Welsh soft opt-out https://pmc.ncbi.nlm.nih.gov/articles/PMC6500329/ (d08)
- [V] Framing the Default (2024) https://pmc.ncbi.nlm.nih.gov/articles/PMC11612645/ (b08, b09)
- [M] Limits of Defaults, decision time https://pmc.ncbi.nlm.nih.gov/articles/PMC12478545/ (b23, download failed)
- [V, secondary] Many Labs 1 via FORRT page https://forrt.org/flora-replication-atlas/doi/10.1126/science.7455683/ (d09); PDF blocked
- [V, secondary] Kuhberger 1998, Steiger & Kuhberger 2018, Many Labs 2 summary https://atticusli.com/replication-crisis/framing-effect/ (d10)
- [M] JDM 2019 snippet https://dlab.sauder.ubc.ca/sjdm/journal/19/190426/jdm190426.html (d16)

**Meta-analyses and scale**
- [V] Mertens et al. (2022) https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589/ (a09, a10, b01, b02, b24)
- [V] Maier et al. (2022) https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501/ (a11, b03)
- [V] Mertens et al. reply https://pmc.ncbi.nlm.nih.gov/articles/PMC9351449/ (b04, b26; the Szaszi letter itself is [M])
- [V] DellaVigna & Linos (2022) https://www.nber.org/papers/w27594 (a12, a13, b05, b06)

**LLM and AI studies**
- [V] Jones & Steinhardt (2022) https://arxiv.org/abs/2202.12299 (b16, c05, c06)
- [V] Binz & Schulz (2023) https://arxiv.org/abs/2206.14576 (a17, c04)
- [V] Suri et al. (2023) https://arxiv.org/abs/2305.04400 (a18, c01-c03)
- [V] Zhao et al. (2021) https://arxiv.org/abs/2102.09690 (c07, c08)
- [V] Lu et al. (2022) https://arxiv.org/abs/2104.08786 (a19, c09)
- [V] Liu et al. (2024) Lost in the middle https://arxiv.org/abs/2307.03172 (a20, b15, c10, c11)
- [V] Zheng et al. (2024) https://arxiv.org/abs/2309.03882 (a21, b10, b11, c12, c13)
- [V] Pezeshkpour & Hruschka (2023) https://arxiv.org/abs/2308.11483 (a22, c14; abstract and figure 1 only)
- [V] Sclar et al. (2024) https://arxiv.org/abs/2310.11324 (a23, c16)
- [V] Wang et al. (2023) https://arxiv.org/abs/2305.17926 (a24, b12, b13, c15)
- [V] Shi et al. (2025) https://arxiv.org/abs/2406.07791 (b14)
- [V] Echterhoff et al. (2024) https://arxiv.org/abs/2403.00811 (a15, a16, b17, c20, c21)
- [V] Cherep, Maes, Singh (2025) https://arxiv.org/abs/2505.11584 (b18, b19); PNAS 2026 abstract https://www.media.mit.edu/publications/ai-agents-are-sensitive-to-nudges/ (d03)
- [V] Allouah et al. (2025) ACES https://arxiv.org/abs/2508.02630 (c17-c19)
- [V] Itzhak et al. (2024) https://arxiv.org/abs/2308.00225 (c22)
- [V partial] Macmillan-Scott & Musolesi (2024) https://arxiv.org/abs/2402.09193 (c23)
- [M] Hagendorff et al. (2023) https://arxiv.org/abs/2212.05206 (c24); Horton (2023) https://arxiv.org/abs/2301.07543 (c25)
- [V] Halimeh et al. (2026) https://arxiv.org/abs/2609.19843 (d01); Kaltenpoth et al. (2026) https://arxiv.org/abs/2611.09264 (d02)
- [V] Soumik (2026) https://arxiv.org/abs/2604.23178 (d04)
- [V] Veseli et al. (2025) https://arxiv.org/abs/2508.07479 (d05); Chowdhury (2026) https://arxiv.org/abs/2603.10123 (d06)
- [V] Lou & Sun (2024) https://arxiv.org/abs/2412.06593 (d11)
- [V] Kumar & Lakkaraju (2024) https://arxiv.org/abs/2404.07981 (d12); Nestaas et al. (2024) https://arxiv.org/abs/2406.18382 (d13)
- [V] Lim et al. (2026) DeFrame https://arxiv.org/abs/2602.04306 (d14); Shafiei et al. (2025) https://arxiv.org/abs/2506.03923 (d15)

Critique pass re-opened and confirmed numbers for Mertens, Maier, DellaVigna & Linos, Madrian & Shea, Liu, Zheng, Wang, Cherep, Echterhoff, Allouah, Sclar. Corrections adopted: the real at-scale effect is about one sixth of the published one; "66 of 80" equals the 82.5% win rate and is one number; 76% at 3% is a share of participants and 61% a share of all new employees; a16's 0%/1.4%/2.7% figures are unverified and not used.
