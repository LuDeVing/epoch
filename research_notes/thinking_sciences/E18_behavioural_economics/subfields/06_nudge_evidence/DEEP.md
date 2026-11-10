# Nudge evidence: deep document

*Subfield E18.06 of behavioural economics. Evidence ids (a01..d16) point to evidence_a-d.jsonl; claim ids (K01..K25) point to claims.jsonl; critique.md holds the cross-check. Status marks: [E] established, [S] single-source, [C] contested. All numbers are from sources opened this run unless marked abstract-only.*

## 1. What it is

A nudge is a change in how a choice is presented that moves behaviour without banning options or changing prices. Thaler and Sunstein named it. The change is called choice architecture. Examples: a default option, a reminder text, a reordered menu, a social-norm label.

"Nudge evidence" is the question: how big are these effects, really? It matters to us because it is the best-studied case of an intervention literature whose headline numbers shrank when people measured them again at scale. Our agent is a scaffold (guardrails, states, operators) wrapped around a model. Each scaffold element is a small intervention on a model. Guardrail G7 says an element stays only if it wins at equal tokens against the plain model. The nudge literature shows how such wins turn out inflated: small samples, selective publication, winner's curse, expert over-prediction, and effects that do not carry over to new settings.

There is a second link. Language models are themselves nudgeable. They follow irrelevant defaults, suggestions, badges and social labels more than humans do (K11, K12). So this subfield gives two things: a method lesson for how we measure our own scaffold (G7), and a robustness test for the agent (G1, G3).

Scope notes. Productive failure, calibration, debiasing, dual-process theory, choice architecture and belief updating are other parallel subfields. Only links are noted here.

## 2. History and theories in depth

**Founding field studies.**
- Madrian and Shea (2001, a16, a17) studied one large US firm that switched to automatic 401(k) enrolment. Participation of employees hired under auto-enrolment was about 86%. The cohort hired just before it was about half. Firm-wide participation before the change was 61%, so the implied rise is about 25 points. The default was 3% of pay into a money market fund. Side effect: 65.1% of the auto-enrolled cohort contributed exactly 3%, 12.2 points above what would be expected if all new participants chose 3% freely. 61% of the new cohort followed the full default pattern (participate, 3%, money market) against 1% of other cohorts. About 80% of their money went to the money market fund. Limits: one firm, cohort comparison, not randomised, 78% female workforce.
- Choi, Laibson, Madrian, Metrick (2001, d15; abstract only) found the same in three firms. Participation went above 85%. After three years half still sat at the default rate and fund. The wealth gain was offset on average, though the lowest savers gained. This is the "anchor" side effect (K10).
- Johnson and Goldstein (2003, a18, a19) ran an online experiment (161 respondents, values read from a figure): consent 42% opt-in, 82% opt-out, 79% neutral. Cross-country effective consent: Denmark 4.25%, Germany 12%, Netherlands 17.17%, UK 27.5%; presumed-consent countries mostly 85.9% to 99.98%. A panel check found donation up 16.3% (p<0.02) after countries adopted presumed consent. Limits: registration is not donation; countries differ in law and culture; not randomised. These founding papers were not re-opened in the cross-check (critique).

**Theory.** Thaler and Sunstein's libertarian paternalism says designers can steer choices while keeping freedom. The behavioural basis is inertia, loss aversion, limited attention and status-quo bias. Jachimowicz et al. (2019, b14) name three channels for defaults: they signal endorsement, they set the status quo, and they save effort. Defaults work better when seen as endorsed by the architect or as the status quo.

**Taxonomy used in the meta-analysis.** Mertens et al. (2022, a04) sort nudges into three groups. Decision structure (defaults, option layout, effort, consequences). Decision information (framing, social norms, labels). Decision assistance (reminders, commitment). Beshears and Kosowsky (2020, b15) separately find that nudges that automate part of the decision are bigger, by Cohen's d 0.193, over 174 articles.

**The scale-up turn.** From 2020 the field's own data began to disagree with the first meta-analyses.
- 2020-2022: DellaVigna and Linos find nudge-unit trials at one sixth of published effects (a12-a14).
- 2021-2025: Milkman's megastudies test many ideas on one population with preregistration and find small gains and a winner's curse (a20-a22, b10-b12).
- 2022: the Mertens meta-analysis (a01-a06) and three published replies (a07-a11, b04-b08) fight over bias correction.
- 2021: Bryan, Tipton and Yeager (a23, b17) argue that failures to replicate reflect real context dependence. A single average is the wrong target.
- 2025-2026: LLM studies begin to treat models as the decision-maker being nudged (a24-a27, c01-c10).

**Competing explanations for the shrinkage.** (1) Publication bias and low power (DellaVigna and Linos, Maier). (2) Real heterogeneity, so averages mislead (Bryan, Szaszi). (3) Nudge-unit nudges differ in kind: mostly mail and message nudges on take-up, with few defaults. Features of the nudge explain about two thirds of the gap when power is not controlled (a14). These explanations are not exclusive. The data cannot separate them cleanly.

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Pooled nudge effect, published literature | d=0.45 (95% CI 0.39-0.52), 455 effects, 214 publications, N=2,149,683; d=0.42 after outlier removal; leave-one-out 0.43-0.46 | Mertens 2022 (a01, b01) | [E] as an unadjusted number |
| Extreme heterogeneity | I2=99.67%, tau2=0.23; 95% prediction interval -0.48 to 1.39; about 15% of interventions expected to backfire; moderators only cut I2 to 99.5% | Mertens (a02, b02) | [E] |
| Publication bias present | Egger b=2.28 (t(339)=4.61) in original; b=2.10 (t(332)=5.22) on corrected data (different datasets, not a conflict); moderate bias cuts d 0.42 to 0.31 (-26.79%); severe bias 0.03 original / 0.08 reply | Mertens (a03, a11); Maier (a07) | [E] |
| 63% of effects lie below the pooled mean (left cliff at zero) | overall 62.64%; health 72.62%, prosocial 67.39%, food 60.36% | Bakdash and Marusich (b07) | [E] descriptive |
| Bias-corrected overall effect near zero | RoBMA d=0.04 [0.00,0.14], BF01=0.95 (undecided); most precise estimates d=0.11 [0.00,0.24], BF01=0.31; Andrews-Kasy -0.01 (SE 0.02); WAAP 0.07 (SE 0.03); trim-and-fill 0.08 (SE 0.03) | Maier (a07); Szaszi (a10) | [C] |
| Structure beats information and assistance (raw) | Structure d=0.55 (0.45-0.64), k=227; Information 0.38, k=130; Assistance 0.31, k=98; structure vs information b=0.17, vs assistance b=0.24 | Mertens (a04, b02) | [C] |
| After correction, by category | Information raw 0.25 to 0.00 (BF01=33.84); assistance 0.22 to 0.01 (BF01=9.05); structure 0.58 to 0.12 [0.00,0.43] (BF01=1.12) | Maier (a08) | [C] |
| Domain | Food d=0.72 (0.49-0.95), finance 0.25 (0.12-0.37); after correction finance 0.00 (BF01=41.23), food 0.02 (BF01=5.16; precise 0.27, BF01=0.55 undecided) | Mertens (a05); Maier (a09) | [C] |
| Setting, country, age do not moderate; newer papers show smaller effects | only publication year predicted size | Mertens (a06) | [S] |
| Nudge units at scale vs academic papers | 126 RCTs, 243 nudges, 23.5M people: 1.4 pp (SE 0.3), 8.1% over control 17.2%. Academic: 26 papers, 74 nudges, 8.7 pp (SE 2.5), 33.5% over control 26.0% | DellaVigna and Linos (a12) | [E] |
| Power plus selection explain the gap | median arm n 484 vs 10,006; minimum detectable effect 6.3 pp vs 0.8 pp; academic sample has over 4x more studies with t in 1.96-2.96 than 0.96-1.96; selection-corrected academic mean 3.2 pp (SE 1.9) vs 8.6 uncorrected; publication probability of a non-significant trial 0.1 | DellaVigna and Linos (a13) | [E] |
| Academics are not the cause | BIT NA (no academics) 1.7 pp; OES 1.0 pp; OES with academics 1.0 pp | a14 | [E] |
| Experts over-predict | nudge-unit forecast median 4 pp (mean 5.8) vs true 1.4; academic-sample forecast median 6 pp (a15, not re-verified) | a15 | [E] |
| Vaccine megastudy (texts) | N=47,306, 19 messages, control 42%; average +2.1 pp (5%), 6 of 19 significant; best +4.6 pp, shrunk +2.8 pp (6.7%); equal true effects not rejected (chi2=21.277, df=18, p=0.266) | Milkman 2021 (a20) | [E] |
| Flu text megastudy | N=689,693, 22 messages, average +2.0 pp (6.8%); abstract only | Milkman 2022 (b11) | [E] |
| COVID booster megastudy | reminders +21% (1.05 pp) for boosters, +8% (0.34 pp) for flu; free rides added nothing; best-worst gap 0.26 pp; cells about 492,573 | Milkman 2024 (b12) | [E] |
| Gym megastudy | N=61,293, 54 programmes; 45% raised visits by 9-27%; only 8% still significant after the programme; judges could not predict winners (abstract only) | Milkman 2021 (a21, b10) | [E] |
| Savings email megastudy | 1,925,785 people, 7 campaigns; +0.05 pp (0.51%); best +0.13 pp (1.32%) | Milkman 2025 (a22) | [E] |
| Transfer failure in the field | 3 preregistered RCTs, N=314,824; reminders and ownership wording replicated; bundling and misconception messages gave no gain over a reminder | UCLA (b13) | [E] |
| Defaults are strongest but vary | d=0.68 (0.53-0.83), 58 studies, n=73,675; some null, two negative | Jachimowicz (b14) | [E] |
| Automation nudges larger | +0.193 d over other nudges, 174 articles (abstract only) | Beshears and Kosowsky (b15) | [S] |
| Default anchoring side effect | 65.1% at exactly 3% contribution; 3 firms: half still at default after 3 years | a17, d15 | [E] |
| LLMs over-follow defaults (basket task) | humans 51% (no nudge) to 88% (default); GPT-3.5 Turbo and GPT-5 Mini 99%; GPT-4o, GPT-4o Mini, Claude 3 Haiku, o3 Mini 100%; Gemini 2.5 Flash/Pro, Claude 4.5 Sonnet, o3, GPT-5 not different from humans | Cherep PNAS (a24, c01) | [E] (3 groups) |
| LLMs over-follow suggestions and highlights | late suggestion accepted: humans 25%, models 42-77%; wrong highlight first-reveal: humans 57%, Gemini 1.5 Pro 100% | a25, c02, c03 | [S] one group |
| LLM shopping agents | 3,600 agents, 21,600 choices: default OR 8.70 (7.54-9.97), social OR 37.24 (31.04-44.20) | Halimeh (c06, d08) | [E] |
| Reasoning effect | default 92% to 86% (OR 0.51, 0.41-0.62); social 96% to 98% (OR 1.71, 1.26-2.20); reasoning alone with no nudge beta -0.05 | Halimeh (c07, d09) | [S] |
| Wording flips default following | CPR game, indefensible default: gpt 5.4 0.27 to 0.88 under rewording; net pull 0.25 (agreement) vs 0.58 (conflict) | Montero-Porras (c09-c10, d11) | [S] |
| Format sensitivity | up to 76 accuracy points between equivalent formats (LLaMA-2-13B); median spread 7.5; weak cross-model correlation | Sclar (d04, d05) | [E] older models |
| "Think step by step" on an older model | text-davinci-002: MultiArith 17.7% to 78.7%; GSM8K 10.4% to 40.7% | Kojima (b27) | [E] historical |
| Same advice on 2024-25 models | vs direct control: Gemini Flash 2.0 +0.135, Sonnet 3.5 +0.117; vs default: Flash 2.0 +0.062, Sonnet 3.5 -0.019 ns; reasoning models marginal (o3-mini +0.029, o4-mini +0.031, Gemini Flash 2.5 -0.033) | Meincke (d06, d07) | [S] industry report |
| Mid-run guidance in coding agents | 10,554 trajectories: 90.93% judged recovered after one intervention, 79.07% after several; live A/B tool failures 5.07% vs 5.29% (-4.2%), tokens -5.3%; accuracy not measured | Wink (d01-d03) | [S] |

## 4. Mechanisms and models

This section is written so an engineer can turn the ideas into tests.

**4.1 Winner's curse and shrinkage.** If you test K variants and keep the best, the best observed gain is biased upward. Selection picks the luckiest noise. Milkman's vaccine study shows it: best message +4.6 pp observed, +2.8 pp after shrinkage (a20). To implement: (a) estimate the noise level per variant (standard error from the bench); (b) fit a random-effects model of true gains across variants; (c) shrink each variant toward the group mean by the weight tau2/(tau2+se2); (d) report the shrunk gain of the winner; (e) confirm on a fresh item set the selection never touched. If the equal-effects test cannot be rejected (as in a20, p=0.266), treat the variants as the same.

**4.2 Power and the file drawer.** The academic nudge sample had a median arm of 484 and a minimum detectable effect of 6.3 pp. With such low power, only inflated estimates cross the significance bar. Selection on significance gave 8.6 pp uncorrected against 3.2 pp corrected (a13). Rule: for each kept scaffold gain, compute the minimum detectable effect at our item count. If the observed gain is near that number, it is probably inflated. The signature of selection is a jump in the density of t values just above 1.96 (a13); a bench log that only records "wins" will show the same jump.

**4.3 Publication-bias correction methods.** Three families appear in the debate. Selection models weight the likelihood of a result by its p-value region. PET-PEESE regresses effect on its standard error; the intercept is the effect at infinite precision. Andrews-Kasy estimates publication probability from the t distribution. RoBMA averages across these with Bayesian weights and returns a Bayes factor BF01 (above 3 is evidence for no effect; below 1/3 for an effect; in between undecided). All are unstable when heterogeneity is high (a10 limits). For our use: we control selection, so we do not need these methods. A held-out set is cleaner.

**4.4 Heterogeneity as the main result.** The prediction interval -0.48 to 1.39 tells you what a new nudge will do far better than the mean. For a scaffold: report the spread across task families and models, not the pooled gain. If the interval for a new family spans zero, treat the scaffold as unproven there.

**4.5 How a default works (as a model).** A default adds three things: it lowers the cost of acting (effort), it signals endorsement, and it sets the reference point (a16, b14). For a human the cost term often dominates. For an LLM there is no effort cost, so the pull must come from endorsement and reference signals in the prompt text and from training. That fits the data: permission wording lowers the pull, instructive wording raises it (d11). Implementation probe: put an irrelevant pre-filled answer in the prompt, put the correct answer elsewhere, and measure acceptance rate.

**4.6 Resource-rational optimal nudge.** Cherep et al. (a26, c05) choose which information to pre-reveal using a cost-benefit model of how a person should search (Callaway, Hardy, Griffiths). Pre-revealing the most informative cells raised points for humans (163 to 175) and for several models (GPT-5 172 to 180). The mechanism is value of information: reveal what has the highest expected change in decision per unit cost. A scaffold analogue: before the model solves, show it the cheapest high-value fact (for example, run code on the examples and show the failing output). That already is G2. The finding is single-source and models differ: GPT-4o Mini stayed near 130-138 (a26).

**4.7 Two-route model of LLM susceptibility.** Halimeh et al. (c06-c08) use a dual-process frame. The default pull behaves like a fast route that deliberation can cut (92% to 86%). The social-proof pull behaves like content the model treats as evidence, and more deliberation raises it (96% to 98%). The frame is the authors' reading, not a tested mechanism. Practical meaning: a thinking step is not a general debiaser. It shifts which cue wins. Always measure both cue types.

**4.8 Wording as the main control variable.** Montero-Porras (d11) label a model "fixator" or "rejector" per wording. The label belongs to the pair model x wording. Sclar (d04) measure the same for formats and recommend FormatSpread: sample many plausible formats, estimate min and max accuracy, report the interval. Cost under 10 USD per task for GPT-3.5 (d05). Implementation: for every scaffold test, run at least 3 paraphrases of the task wording and report the spread.

**4.9 Forecast calibration.** Experts and judges predict poorly. DellaVigna and Pope (d14): the average forecast beat 96% of individual forecasters; experts did not beat non-experts at ranking. Hewitt et al. (d13): GPT-4 simulated responses correlated r=0.85 with 70 survey experiments but overestimated size, and dropped on megastudies to expert level. Implementation: log the predicted winner before running, then score rank correlation against measured results. Use forecasts only as a cheap prior.

## 5. What holds up

**Holds up well [E].**
- The raw pooled number is about 0.43-0.45, with near-total heterogeneity (a01, a02).
- Publication bias exists. The original authors concede it (a11, b08).
- At-scale trials produce effects about one sixth of academic ones, and power plus selection explain most of it (a12, a13).
- Megastudies find small positive gains, many nulls, winner's curse, and no ability of experts to pick winners (a20, a21, b10-b12, a22).
- Experts over-predict (a15, b13).
- Defaults give the biggest and most consistent human effect (b14, a16, a18), with side effects on dimensions the user did not choose (a17, d15).
- Reminder texts help a little: +21% relative for boosters in one chain, +2 pp in flu texts (b11, b12).

**Contested [C].**
- True average after correction: -0.01 to 0.31 depending on method (a07, a10, a03). Mertens give 0.08 to 0.31 as the sensitivity range.
- Whether structure nudges survive correction: RoBMA 0.12 with BF01=1.12, undecided (a08). Szaszi and Jachimowicz keep defaults as the exception (b06, b14).
- Whether heterogeneity means "nudges fail" or "nudges are context dependent" (a23 vs Maier). Maier find heterogeneity in all groups except finance (b05).
- Whether the food effect is real. Raw d=0.72; corrected 0.02 with a wide interval; with only precise estimates 0.27 (undecided).

**Failed or null interventions.**
- Free rides for booster shots added nothing beyond reminders (b12).
- Bundling flu and COVID shots and misconception messages gave nothing over a simple reminder in 3 RCTs (b13).
- Savings emails: +0.05 pp across 1.9 million people (a22).
- Gym programmes: only 8% showed any effect after the programme ended (a21).
- Image-enhanced energy feedback: 0.07 kWh/room-day vs control (p=0.793) (c15).
- ChatGPT-rewritten vaccine messages: overall mean 0.107 on a -5 to 5 scale (p=0.46); order effect larger than message effect (c16).
- LLM-picked decoys worked in the US, partly in Germany, not in China, India or Singapore (c13).

**Moderators seen.** Technique (structure beats others, raw). Domain (food, finance). Publication year (smaller recently). Medium (in-person vs letter, confounded with sample size). Power (the main one). For LLMs: model size class (small models follow defaults more, flagships follow social cues more; exploratory, d10), wording (d11), format (d04), reasoning setting (c07).

**What did not moderate.** Lab versus field, country (US vs other) and age group in the Mertens data (a06). Academic involvement in nudge units (a14).

**Interventions that worked at scale.** Text reminders with "waiting for you" phrasing (b11); a plan-making message (+23.65% relative, 1.20 pp, b12); micro-rewards for returning after a missed gym visit (b10); automatic enrolment for participation (a16). All modest except defaults.

## 6. Language models

**Biases reproduce, size is unreliable.** GPT-3.5 shows anchoring (low-anchor mean 20.83, high 105.97; human 22.5 and 80.50), framing, endowment and the conjunction error (18 of 20) (b19). Horton's "homo silicus" work replicates status-quo, fairness and other classics qualitatively across GPT-4, GPT-4o, Claude 3.5 and 3.7, DeepSeek; GPT-4o shows the least status-quo bias (b18, c11, c12). GPT-3 acts like fast human intuition on the CRT; ChatGPT and GPT-4 act hyper-rationally (b20, abstract). Digital twins correlate only r=0.20 with human answers across 164 outcomes (a30, abstract only) [K17, C]. LLM economic choices are more consistent with utility maximisation than humans but depend on wording (b24, c17).

**Defaults, suggestions, highlights (the direct nudge tests).**
- Basket task (Cherep, a24-a26, c01-c05). Humans take the default 51% without a nudge and 88% with. Many LLMs: 94-100%. Frontier reasoning models (o3, GPT-5, Claude 4.5 Sonnet, Gemini 2.5) are close to humans. Late bad suggestions: humans 25%, models 42-77%, but Gemini 2.5 Flash 13% and o3 Mini 7% fell below humans. Wrong highlight: humans 57%, Gemini 1.5 Pro 100%. Chain of thought and few-shot human data changed choices but did not remove hypersensitivity (c04). About a billion tokens were used. The preprint and PNAS human baselines differ (preprint early 0.37, late 0.34; PNAS 35%, 25%); use PNAS.
- Shopping, 17 models (a27): a higher rating raises selection by 30-80 pp in 14 of 17 models. Best-seller or Buy-1-Get-1 text shifts choice 10-60 pp in 14 of 17. Position: GPT-4.1 Nano +90 pp for the first item; Claude 3.5 Haiku -35.4 pp. Stated user preferences dominate once declared.
- Shopping, randomised (b23): top-row coefficient 1.224 (Claude Sonnet 4), 1.045 (GPT-4.1), 0.344 (Gemini 2.5 Flash). "Overall Pick" tag lifts a 10% baseline to 24.3%, 19.9%, 42.6%; "Sponsored" lowers it to 8.9%, 8.0%, 7.9%. Telling the agent to ignore position did not significantly cut position effects. GPT-4.1 and GPT-5.1 had nearly opposite position biases.
- 2026 shopping agents (c06-c08, d08-d10): default OR 8.70, social OR 37.24. High reasoning: default 92% to 86%, social 96% to 98%. Gemini 3.5 Flash default following 84% to 48%. GPT-5.4-mini social following 91% to 99%; GPT-5.4 no rise. Baseline about 50% in both reasoning settings. The authors did not test a prompt-level reflection step.
- Social dilemmas (c09-c10, d11-d12): the same model flips from rejecting an indefensible default to fixating on it with rewording (0.27 to 0.88 for gpt 5.4). Permission wording drops the pull to near 0 for several models; instruction wording raises it everywhere. Conflict defaults pull more than agreement defaults (0.58 vs 0.25). The authors name their limits: seven models, no Claude or Gemini, one shot, reasoning off.

**What changes the pull, and by how much.**

| Lever | Effect | Source |
|---|---|---|
| Stronger model family (reasoning built in) | frontier reasoning models near human default rate; older ones 94-100% | a24 |
| High reasoning setting | default 92% to 86% (OR 0.51); social 96% to 98% (OR 1.71) | c07 |
| Chain of thought, few-shot human examples | shifts choice, does not remove sensitivity | c04 |
| Wording (permission vs instruction) | 0.27 to 0.88 flips; permission near 0 | d11 |
| "Ignore position" instruction | no significant cut | b23 |
| Self-help debiasing (admissions task) | GPT-4 group attribution to 0%, framing to 2.7%; GPT-3.5 left framing at 17.2% | b22 |
| Model size | default OR 15.94 small vs 4.64 flagship; social 17.59 small vs 107.57 flagship | d10 |
| RLHF and instruction tuning | amplify decoy, certainty, belief biases; base models show less | b21, a28 |

**Training causes.** Instruction tuning and RLHF raise decoy bias (0.00 base to 0.38 tuned in one table, b21; mixed in a larger Flan-T5). Cheung et al. (a28) link omission bias to chatbot fine-tuning. Sharma et al. (b28) show five assistants lean toward the user's stated view; preference data sometimes rewards agreeable answers over correct ones. Cherep guess sycophancy is a cause but did not test it (c01).

**Prompt format and wording sensitivity.** Up to 76 accuracy points from equivalent formats; median spread 7.5; GPT-3.5 up to 56 (d04). The best format barely transfers between models (d05). Lampinen: content matching real-world belief changes logic performance (b30, abstract). Anchors shift the whole output distribution in small open models (c20, abstract).

**LLM-written nudges for humans.** Personalised weekly energy nudges in a dorm trial (233 residents; analysed n=169): -0.56 kWh/room-day vs control (p=0.014); hot water -3.6 L (p=0.087) not significant (c15). Rewritten vaccine messages: no gain (c16). GPT-2 bots to promote news: small effects (a29, abstract). LLM-picked decoys: country-dependent (c13). An LLM prior in a choice model cut the human data needed by 57-74% at 2% human data (c14).

**Nudges inside agent loops.** Wink (c21, d01-d03): about 30% of coding trajectories misbehave (12,499 of 42,807 = 29.2%). Guidance after one intervention was judged to recover 90.93%; after several 79.07%. Hand-coded: 37% of non-recoveries ignored the guidance. Live A/B: tool-call failure 5.07% vs 5.29% (-4.2%), tokens per session -5.3%, engineer interventions -4.2%, execution time -4.3% (p=0.073). Shadow mode: misbehaviour 15.14% vs 18.61%. Recovery was judged by an LLM judge (precision 85.71% on a small check). No task accuracy was reported. Agrawal (c22, abstract) show system-prompt moral nudges raise whistleblowing, with rates varying by family. Borah (c23, abstract) report accuracy nudges cut misinformation spread by up to 37% in a simulation.

**Advice-style prompt additions on current models.** Meincke et al. (d06, d07): on 198 GPQA Diamond questions x 25 trials, "think step by step" beat a direct-answer control for non-reasoning models (Gemini Flash 2.0 +0.135, Sonnet 3.5 +0.117), but against the model's own default the gain was +0.062 and -0.019 (ns). On the strict 25-of-25 metric it hurt Gemini Flash 2.0 (-0.131) and Gemini Pro 1.5 (-0.172). Reasoning models: marginal. Four wordings made negligible difference. Time cost 35-600%. The famous 2022 gain (b27) belongs to older models. Single benchmark; industry report.

**Not nudge tests.** The sycophancy, bias and CRT papers (b20, b21, b28, a28) show susceptibility but not nudge-style interventions.

**Coverage check.** An arXiv keyword search on "choice architecture" with LLM returned 5 papers, 3 relevant (c25). Few groups work on this, so each LLM finding rests on one to three groups.

## 7. What our agent should take

Format: item | schema part | status | evidence ids.

### Add now (established)

1. **Report per-family effects with intervals, never one pooled scaffold gain.** G7 | [E] | a01, a02, b01 (K01). The nudge mean hides a prediction interval of -0.48 to 1.39. Make per-family tables mandatory in every keep/drop decision.
2. **Count a scaffold gain only if measured on fresh, held-out items the selection never saw; shrink the winner.** G7, G3 | [E] | a03, a13, a20, b07 (K02, K06, K08). Winner's curse is large (4.6 to 2.8 pp). Add an exploratory/fresh split to the bench and report both.
3. **Treat every kept gain as probably inflated; re-run on a larger fresh sample.** G7 | [E] | a12, a13 (K06). The one-sixth ratio is the benchmark to compare ours against.
4. **Never let the agent or an LLM judge pick its own scaffold ideas; measure.** G7, G8 | [E] | a15, a21, b10, b13 (K07, K09). Experts and judges did not pick winners. LLM judges rank well on surveys but overestimate (d13, [S]), so use only as a cheap prior.
5. **Run many scaffold variants in one shared benchmark.** G7 | [E] | a20, a21, b12 (K08). The same-population megastudy design removes between-study publication bias.
6. **Validate transfer across model and task before keeping an element.** G7 | [E] | b13, a23, d05 (K09, K13). Format wins barely transfer between models.
7. **Run each scaffold test under 3 paraphrases and report the spread.** G7 | [E] | d04, d05, d11, d12 (K13). Two groups; spread up to 76 points on older models.
8. **Probe the agent with irrelevant defaults, wrong suggestions and social labels; record acceptance rate.** G1, G3 | [E] that models over-follow, [S] on exact rates | a24, c06, d11 (K11, K12). Three independent groups. This is a pre-flight check on the target model, not a scaffold feature.
9. **Check side effects on unchosen dimensions when a default is placed in the prompt (format, effort, plan).** S0, G7 | [E] in humans; none yet for agents | a17, d15 (K10). Madrian and Shea's 3% anchor is the model case.
10. **Compare against the model default, not a direct-answer control.** G7 | [S] | d06, d07 (K22). The advice gain shrinks to about zero against the default. Make it explicit in the bench spec.
11. **Run bias probes on the target model before relying on its intuition.** G1 | [E] | b21, a28, b22, b28 (K16). Instruction tuning amplifies decoy, framing and omission biases.
12. **Do not use the agent as a simulated user to size effects.** G7 | [C] | a30, b19, c11 (K17). r=0.20 against humans.

### Test first (not yet established; see UNKNOWNS.md)

- **Structural scaffold change vs advice at equal tokens** (forced output format, default plan, effort cap vs "be careful" text). O#/G7 | [C] | a04, a08, d06, d07 (K04, K24). Human data say structure beats advice raw, undecided after correction. Nobody tested it for LLMs. Priority high.
- **Reflection step that cuts default and suggestion pull without raising social or authority pull.** G1, G3 | [S] | c07, d09 (K12). API-level reasoning cut one and raised the other. A prompt-level step is untested.
- **Chain of thought at equal tokens on nudge following.** G7 | [S] | c04 (K14).
- **Information-presentation scaffold chosen by a cost-benefit rule** (pre-reveal highest-value facts). O#/G2 | [S] | a26, c05 (K15). Worked for about four of eight models.
- **Mid-run guidance injection scored on held-out accuracy, not on loops avoided.** S-state control | [S] | d01-d03 (K20). Recovery 91% in the table but about 4-5% in the live A/B.
- **Debiasing-instruction step at equal tokens on framing items.** G6/O# | [C] | b22, c18, c19 (K18). Self-help debiasing worked in GPT-4 but not GPT-3.5; biases persisted even with the formula supplied.
- **Agent forecasting its own scaffold winners.** G8 | [S] | d13, d14 (K23, K24).
- **How much of our measured scaffold gain disappears on a larger fresh sample** (is the one-sixth ratio visible?). G7 | open | d02 (K24).
- **Side effect of scaffold defaults on dimensions the model was not asked to choose.** G7 | open | (K10).
- **Stability of default sensitivity across model versions.** G7 | open | d10, d11 (K13). One comparison only (gpt 5.1 vs 5.4).

## 8. Concrete tests on our bench

All arms at equal total tokens (count setup, thinking and output). Report the winner's shrunk estimate and a fresh-set estimate.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | ARC-style and BrainTeaser items, split 50/50 into exploratory and fresh | plain model vs each kept scaffold element | accuracy gain exploratory vs fresh | fresh gain well below exploratory if selected on small n; if fresh gain is under 1/3 of exploratory, the DellaVigna pattern holds |
| T2 | Same items, 8-12 scaffold variants in one run | variants vs plain; winner shrunk by random effects | shrunk winner gain; chi2 test for equal true effects | shrunk gain about 60% of observed (Milkman 2.8 vs 4.6); may not reject equality |
| T3 | Items with a planted wrong default ("a previous attempt suggests X"), a wrong suggestion, a social label ("most solvers answered X"), a wrong highlight | target model plain; acceptance of the planted wrong cue per cue type | acceptance rate; accuracy | high acceptance (50%+) on small models; lower on strong reasoning models; cue types differ |
| T4 | T3 items | plain vs prompt-level reflection step ("check the cue against the evidence") vs equal-length neutral filler | acceptance per cue type | default pull down; watch social pull for a rise (Halimeh OR 1.71) |
| T5 | Same task, 3 paraphrases of the instruction and 3 output formats | each scaffold under each | accuracy range (max-min) across paraphrases; rank agreement across models | spread of several points; ranking differs across models (weak correlation, d05) |
| T6 | Mixed items | structural variant (forced answer format, default plan template, effort cap) vs advice variant ("be careful, double check") vs model default | accuracy vs default | structure larger than advice (human raw d 0.55 vs 0.31-0.38); advice near zero vs default (d06) |
| T7 | Agent-loop tasks with injected misbehaviour (loop, spec drift) | no guidance vs mid-run guidance vs guidance only at a failed check | final task accuracy; tokens; recovery | recovery up but accuracy gain small; compare with Wink's 91% table vs 4-5% live |
| T8 | Framing pairs (gain vs loss wording) and decoy items | plain vs self-help debiasing step vs equal filler | answer flip rate between frames | flip rate falls in strong models, not small ones (b22) |
| T9 | Forecast test | before T2, ask the agent and a judge to rank variants; compare with measured | Spearman rank correlation | modest and overestimating sizes (d13) |
| T10 | Default side effect | prompt default for effort cap or format | accuracy on dimensions the default did not target | anchoring on the default value, as with the 3% contribution rate |

## 9. What does not transfer, and why

- **Human effort costs.** A default saves a person effort. A model has no effort cost. The pull in models comes from wording and training (sycophancy, d11, c01). Human d values (0.45, 0.68) must not be used as expected LLM effect sizes.
- **Field outcomes.** Take-up of vaccines or savings is real-world behaviour over time. Our metric is accuracy on a fixed item. Persistence results (gym 8%) have no counterpart.
- **Pooled effect and its correction.** The Mertens-Maier fight is about a literature with unobserved selection. We control selection ourselves. Use the lesson (hold-out, shrink), not the statistics (RoBMA).
- **Nudges as non-coercive.** Libertarian paternalism assumes a choosing human. A scaffold is a design choice about the machine. The word "nudge" in Fei et al. (b29) means guided decoding, a different thing.
- **LLM as simulated human.** Simulated subjects are hyper-rational and stereotyped (r=0.20, a30), and Maksimenko's LLM decoys failed outside the US (c13).
- **Old-model results.** The 2022 "think step by step" gain (b27), GPT-3.5 bias replications (b19), GPT-2 news bots (a29) and Codex framing (b25) are on models that no longer match. Re-measure.
- **Process metrics as proof.** Wink's recovery and loop numbers are not accuracy (d01-d02). Nothing here shows guidance improves correctness.
- **Dollar cost-effectiveness.** Benartzi (b16) argues nudges compare well per dollar. Our cost is tokens and our test is G7, which counts that already.

## 10. Open questions

1. Is there a true small effect of structure nudges in human field data after correction? Needs large preregistered trials (K25; not searched).
2. Does a structural scaffold change beat advice-style additions at equal tokens on fresh items (K24)?
3. How much of our scaffold gain vanishes on a larger fresh sample?
4. Can an agent or LLM judge predict which scaffold variant wins better than chance, including on megastudy-like sets (d13)?
5. Does a deliberate reflection prompt reduce default and suggestion pull without raising social or authority pull?
6. Is default hypersensitivity stable across paraphrases and model versions (only gpt 5.1 vs 5.4 seen)?
7. Do RLHF-amplified biases (decoy, framing, omission) reach our task families, and does debiasing help at equal tokens? (K25; not searched.)
8. Do mid-run guidance injections raise accuracy or only visible good behaviour (Wink)?
9. Do prompt defaults in a scaffold have side effects like the 3% anchor?
10. Which moderators predict a scaffold effect across models: size, reasoning setting, wording, task type?
11. Why do LLMs over-follow cues: sycophancy, training data, or position priors? No causal test exists (c01 is a guess).
12. Are the 2026 single-group results (Halimeh, Montero-Porras) reproduced by anyone else? Halimeh's Claude cells hit 100% ceilings.

## 11. Sources

[V] = page or PDF text opened this run. [V-abs] = opened, abstract page only. [M] = snippet or listing only.

- [V] Mertens et al. 2022, The effectiveness of nudging (PNAS) https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589/ (a01-a06, b01-b03)
- [V] Maier et al. 2022, No evidence for nudging after adjusting for publication bias https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501/ (a07-a09, b04, b05)
- [V] Szaszi et al. 2022, No reason to expect large and consistent effects of nudging https://pmc.ncbi.nlm.nih.gov/articles/PMC9351519/ (a10, b06)
- [V] Bakdash and Marusich 2022, Left-truncated effects and overestimated meta-analytic effects https://pmc.ncbi.nlm.nih.gov/articles/PMC9351476/ (b07)
- [V] Mertens et al. 2022, Reply to Maier, Szaszi, and Bakdash and Marusich https://pmc.ncbi.nlm.nih.gov/articles/PMC9351449/ (a11, b08)
- [V] DellaVigna and Linos, RCTs to Scale (NBER w27594; Econometrica 2022) https://www.nber.org/papers/w27594 ; https://doi.org/10.3982/ecta18709 (a12-a15, b09)
- [V] Madrian and Shea 2001, The Power of Suggestion https://www.nber.org/papers/w7682 (a16, a17)
- [V] Johnson and Goldstein 2003, Do Defaults Save Lives? https://www.dangoldstein.com/papers/DefaultsScience.pdf (a18, a19)
- [V] Milkman et al. 2021, megastudy of text-based nudges for flu vaccination https://pmc.ncbi.nlm.nih.gov/articles/PMC8157982/ (a20)
- [M] Milkman et al. 2021, Megastudies improve the impact of applied behavioural science (gym) https://pmc.ncbi.nlm.nih.gov/articles/PMC8822539/ (a21, b10; abstract only)
- [V] Milkman et al. 2025, Can reminder emails compel Americans to save? https://pmc.ncbi.nlm.nih.gov/articles/PMC12477529/ (a22; full text per critique)
- [V-abs] Milkman et al. 2022, 680,000-person megastudy https://doi.org/10.1073/pnas.2115126119 (b11)
- [V] Milkman et al. 2024, booster megastudy https://pmc.ncbi.nlm.nih.gov/articles/PMC11222156/ (b12)
- [V] Field testing transferability of behavioural science knowledge (UCLA Health RCTs) https://pmc.ncbi.nlm.nih.gov/articles/PMC11132983/ (b13)
- [V-abs] Jachimowicz et al. 2019, When and why defaults influence decisions https://doi.org/10.1017/bpp.2018.43 (b14)
- [V-abs] Beshears and Kosowsky 2020, Nudging: progress to date https://pmc.ncbi.nlm.nih.gov/articles/PMC7946162/ (b15)
- [V-abs] Benartzi et al. 2017, Should governments invest more in nudging? https://pmc.ncbi.nlm.nih.gov/articles/PMC5549818/ (b16)
- [M] Bryan, Tipton, Yeager 2021, Behavioural science is unlikely to change the world https://pmc.ncbi.nlm.nih.gov/articles/PMC8928154/ (a23, b17; abstract only)
- [M] Choi, Laibson, Madrian, Metrick 2001, For better or for worse https://www.nber.org/papers/w8651 (d15)
- [M] DellaVigna and Pope 2018, Predicting experimental results https://www.nber.org/papers/w22566 (d14)
- [M] Hewitt et al., LLMs can predict results of social science experiments https://www.gsb.stanford.edu/faculty-research/publications/large-language-models-can-predict-results-social-science-experiments (d13)
- [V] Cherep, Maes, Singh 2026, AI agents are sensitive to nudges (PNAS) https://pmc.ncbi.nlm.nih.gov/articles/PMC13291645/ (a24-a26)
- [V] Cherep, Maes, Singh 2025, LLM Agents Are Hypersensitive to Nudges (preprint) https://arxiv.org/pdf/2505.11584 (c01-c05)
- [V] Cherep et al. 2026, A framework for studying AI agent behavior https://arxiv.org/abs/2509.25609 (a27)
- [V] Halimeh et al. 2026, A Dual-Process Perspective on Nudge Susceptibility in LLM agents https://arxiv.org/pdf/2609.19843 (c06-c08, d08-d10)
- [V] Montero-Porras, Abels, Lenaerts 2026, Prompt framing governs LLM default following https://arxiv.org/pdf/2610.03253 (c09, c10, d11, d12)
- [V] Allouah et al. 2025, What Is Your AI Agent Buying? https://arxiv.org/abs/2508.02630 (b23)
- [V] Horton et al., LLMs as Simulated Economic Agents https://arxiv.org/abs/2301.07543 (b18, c11, c12)
- [V] Suri et al. 2023, Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400 (b19)
- [V-abs] Hagendorff et al. 2023, Human-like intuitive behavior and reasoning biases in LLMs https://arxiv.org/abs/2306.07622 (b20)
- [V] Itzhak et al. 2024, Instructed to Bias https://arxiv.org/abs/2308.00225 (b21)
- [V] Echterhoff et al. 2024, Cognitive Bias in Decision-Making with LLMs https://arxiv.org/abs/2403.00811 (b22)
- [V-abs] Chen et al. 2023, Emergence of Economic Rationality of GPT https://arxiv.org/abs/2305.12763 (b24)
- [V-abs] Jones and Steinhardt 2022, Capturing failures of LLMs via human cognitive biases https://arxiv.org/abs/2202.12299 (b25)
- [V-abs] Binz and Schulz 2023, Using cognitive psychology to understand GPT-3 https://arxiv.org/abs/2206.14576 (b26)
- [V] Kojima et al. 2022, LLMs are zero-shot reasoners https://arxiv.org/abs/2205.11916 (b27)
- [V-abs] Sharma et al. 2023, Towards understanding sycophancy https://arxiv.org/abs/2310.13548 (b28)
- [V-abs] Fei et al. 2024, Nudging: inference-time alignment via guided decoding https://arxiv.org/abs/2410.09300 (b29)
- [V-abs] Lampinen et al., Language models show content effects on reasoning https://arxiv.org/abs/2207.07051 (b30)
- [V-abs] Jia et al. 2024, Decision-making behavior evaluation framework for LLMs https://arxiv.org/abs/2406.05972 (b31)
- [M] Cheung, Maier, Lieder 2025, LLMs show amplified cognitive biases in moral decision-making https://pmc.ncbi.nlm.nih.gov/articles/PMC12207438/ (a28)
- [M] Askari et al. 2024, Incentivizing news consumption (GPT-2 bots) https://pmc.ncbi.nlm.nih.gov/articles/PMC11404517/ (a29)
- [M] Peng et al. 2026, Digital twins are funhouse mirrors https://pmc.ncbi.nlm.nih.gov/articles/PMC13537255/ (a30)
- [M] Hegde et al. 2024, Infusing behavior science into LLMs https://pmc.ncbi.nlm.nih.gov/articles/PMC10986996/ (a31)
- [V] Maksimenko, Lee, Bansal 2025, Integrating LLMs with human data for decoy design https://arxiv.org/pdf/2508.12045 (c13, c14)
- [V] Li et al. 2026, LLM-generated personalized nudges for energy saving https://arxiv.org/pdf/2604.03881 (c15)
- [V] Working with LLMs to enhance messaging effectiveness for vaccine confidence https://arxiv.org/html/2504.09857v1 (c16)
- [V] Ross, Kim, Lo 2024, LLM economicus? https://arxiv.org/html/2408.02784v1 (c17, c18)
- [V-abs] Liu, Chen, Zhong 2025, Large Language Newsvendor https://arxiv.org/abs/2512.12552 (c19)
- [V-abs] Valencia-Clavijo 2025, Anchors in the Machine https://arxiv.org/abs/2511.05766 (c20)
- [V] Nanda et al. 2026, Wink: recovering from misbehaviors in coding agents https://arxiv.org/abs/2602.17037 (c21, d01-d03)
- [V-abs] Agrawal et al. 2025, Why do language model agents whistleblow? https://arxiv.org/abs/2511.17085 (c22)
- [V-abs] Borah et al. 2025, Mind the (Belief) Gap https://arxiv.org/abs/2503.02016 (c23)
- [V-abs] Patkar et al. 2026, From Perception to Action (UI interventions) https://arxiv.org/abs/2606.10861 (c24)
- [V] arXiv keyword listing check, "choice architecture" LLM https://arxiv.org/search/?query=%22choice+architecture%22+LLM&searchtype=all (c25)
- [V] Sclar et al. 2024, Quantifying language models' sensitivity to spurious features in prompt design https://arxiv.org/abs/2310.11324 (d04, d05)
- [V] Meincke, Mollick, Mollick, Shapiro 2025, Prompting Science Report 2 (Wharton GAIL) https://gail.wharton.upenn.edu/ (d06, d07; exact URL not recorded)
- [M] Wikipedia, Nudge theory https://en.wikipedia.org/wiki/Nudge_theory (background only)
