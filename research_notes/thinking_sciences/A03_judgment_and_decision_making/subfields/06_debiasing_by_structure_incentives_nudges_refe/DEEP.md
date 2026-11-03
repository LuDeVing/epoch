# Debiasing by structure: incentives, nudges, reference class forecasting: deep document

*Folder: A03.06. Built from evidence_a-d.jsonl (ids a01-a30, b01-b25, c01-c26, d01-d17), claims.jsonl (K01-K29) and critique.md. Corrections from critique.md are applied: Egger b = 2.10 and severe-bias d = 0.08 (not 2.28 / 0.03); DellaVigna and Linos nudge units = 8.1% over control mean; the "70% of the gap" figure is not quoted. Evidence marked "not opened" is flagged.*

## 1. What it is

Debiasing by structure means changing the situation in which a judgment is made, so the bias has less room to act. It does not try to fix the thinker. Three families sit under this heading.

- **Incentives.** Pay or penalties tied to accuracy, or accountability to an audience. The goal is more effort and more careful processing.
- **Nudges (choice architecture).** Change defaults, order, framing, effort and information display, without banning options. Thaler and Sunstein (2008) call this libertarian paternalism. The decision structure is changed, not the person.
- **The outside view / reference class forecasting (RCF).** Do not estimate from the story of this case (inside view). Pick a class of similar past cases, get the distribution of their outcomes, place this case in it, and adjust (Kahneman and Tversky; Flyvbjerg).

Why it matters for our agent. The agent is a scaffold around a language model. The scaffold is choice architecture for the model: it sets order, defaults, what is shown first, and which numbers are supplied. The outside view maps directly to S0 (gate: look up the problem class) and S7 (select: use the class record before the inside-view story). The class record in schema section 5 is a reference class store.

Core claim of the field, in one line: change the structure, supply the data, and the bias shrinks more than when you tell people to be careful. The evidence says this is true but smaller than first published, and for LLMs it needs per-model testing.

## 2. History and theories in depth

**Founding ideas (1970s-1990s).** Kahneman and Tversky separated the inside view (build a scenario from case details) from the outside view (use the statistics of similar cases). The planning fallacy is the best-known result: people predict finishing times that are too early even when they know past similar tasks ran late. Buehler, Griffin and Ross (1994) is the founding work; we only have secondary numbers (thesis students predicted 33.9 days, took 55.5; about 30% finished by their own estimate; d14, secondary source, primary not opened).

**Accountability (1980s-1999).** Tetlock and Lerner studied people who must justify judgments to an audience. Lerner and Tetlock (1999, Psychological Bulletin) is the review. The full text was not opened by any agent (d06 abstract only). The 266-experiment systematic review by Aleksovska et al. (2019, d05, opened) gives the direction by vote counts, not effect sizes: accountability mostly raises information search, processing depth, time and effort; mostly weakens bias; lowers confidence and overconfidence; raises caution; makes the dilution effect worse; works better when announced before the task; process accountability gives more calibrated and consistent decisions. Known-preference audiences cause conformity (older literature; not verified at effect-size level here).

**Financial incentives (1999).** Camerer and Hogarth (1999) reviewed incentive experiments. Recalled only (a18, b24, not opened): incentives help where extra effort pays, and rarely remove systematic anomalies like anchoring and framing. Do not cite until opened.

**Defaults and nudges (2001-2008).**
- Madrian and Shea (2001, d01-d02, opened): automatic 401(k) enrolment. Participation 37% before vs 86% after (3-15 months tenure). 76% of auto-enrolled stayed at the default 3% rate. 61% sat at the full default. The default set the amount as well as the choice.
- Johnson and Goldstein (2003, a01-a03, opened): organ donation. Opt-in 42%, opt-out 82%, forced choice 79% (N=161).
- Thaler and Sunstein (2008) *Nudge* (a20, not opened) popularised the idea and launched nudge units.

**Reference class forecasting in practice (2003-2013).** Lovallo and Kahneman (2003) brought the outside view to business. Flyvbjerg (2006, a12-a16; 2013, b08-b11) built it into method for transport infrastructure, and the UK Department for Transport adopted uplifts. Leleur et al. (2015, d15) name class choice as the weak point.

**The reckoning (2020-2022).** Large nudge meta-analyses gave d near 0.45 (Mertens et al. 2022). Reanalyses with publication-bias correction cut it to 0.04-0.11 (Maier et al. 2022) or 0.08-0.31 (Szaszi et al.; Mertens reply). DellaVigna and Linos (2022) found nudge-unit trials gave 1.4 percentage points against 8.7 in academic papers. The field now treats single published nudge effects as upper bounds.

**LLM era (2022-2026).** Studies measured human-like anchoring, framing and base-rate neglect in LLMs (Jones and Steinhardt 2022; Suri et al. 2023; Echterhoff et al. 2024; Malberg et al. 2024; Zhong et al. 2025). Forecasting work (Halawi et al. 2024; Schoenegger et al. 2024; Karger et al. 2025) uses retrieval and base-rate steps. Incentive-like prompts (EmotionPrompt, tipping) were tested for accuracy, not bias.

**Competing theories of why defaults work (Johnson and Goldstein 2003, a03).** (1) Default as advice from the policy-maker (endorsement). (2) Effort: accepting is free. (3) Status quo and loss aversion. A one-click change largely removed the effort route yet the effect stayed (82% vs 42%). Madrian and Shea cannot separate inertia from advice. Jachimowicz et al. (2019, d04) find defaults stronger when read as endorsement or status quo. White et al. (2021, d03) add time: defaults work mainly when people decide fast.

**Competing views on nudge effectiveness.** (a) Real, small to medium (Mertens). (b) No evidence after bias correction (Maier). (c) Huge heterogeneity, so the average is the wrong target (Szaszi). The field has not settled this (K04).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Opt-out vs opt-in organ donation (stated consent) | Opt-in 42%, opt-out 82%, forced choice 79%; N=161; opt-out not different from forced choice | Johnson and Goldstein 2003 (a01) | Established (original; replication not found) |
| Country donation registries | Explicit: Denmark 4.25%, Netherlands 27.5%, UK 17.17%, Germany 12%. Presumed: Austria 99.98%, France 99.91%, Hungary 99.97%, Poland 99.5%, Portugal 99.64%, Belgium 98%, Sweden 85.9%. 16.3% increase in donation rate (P<0.02) | a02 | Correlational, 11 countries |
| 401(k) auto-enrolment | Participation 37% vs 86% at 3-15 months; 76% at default 3%; 61% at full default vs 1% before; non-default share 7% to 37% in 15 months | Madrian and Shea 2001 (d01, d02) | Established, observational, one firm |
| Default effect shrinks with decision time | Exp 4 (N=637, preregistered): short 86% vs 66%, long 66% vs 64% (p=.506). Mini meta-analysis N=2,359, interaction d=1.19 [1.06, 1.32] | White et al. 2021 (d03) | Single source |
| Defaults meta-analysis | 58 studies, n=73,675, d=0.68 [0.53, 0.83]; two negative studies | Jachimowicz et al. 2019 (d04, abstract only) | Single source; probably inflated |
| Nudge meta-analysis overall | d=0.45 [0.39, 0.52]; 214 papers, 455 effect sizes, N=2,149,683; without outliers 0.42 [0.37, 0.46] | Mertens et al. 2022 (a04) | Contested |
| By category (Mertens coding) | Structure k=227 d=0.55; information k=130 d=0.38; assistance k=98 d=0.31 | a05 | Structure larger than others |
| By domain | Food d=0.72; prosocial 0.44; environment 0.43; health 0.34; other 0.29; finance 0.25 | a06 | Single source |
| Heterogeneity | I2=99.67%, tau2=0.23, prediction interval [-0.48, 1.39]; about 15% could backfire; Egger b=2.10 | a07 (corrected), b03 | Established |
| Bias-corrected nudge effect (Maier) | Unadjusted 0.43 [0.38, 0.48]; RoBMA-PSMA 0.04 [0.00, 0.14], BF01=0.95; precise studies 0.11 [0.00, 0.24], BF01=0.31 | Maier et al. 2022 (a08, b01) | Contested |
| By category after correction (Maier coding) | Information 0.00, BF01 33.84/10.57; assistance 0.01; structure 0.12 [0.00, 0.43], BF01 1.12/0.33. Maier's own raw categories: information 0.25, structure 0.58, assistance 0.22 | b02; critique | Contested |
| Bias-corrected (Szaszi; Mertens reply) | Severe 0.08, moderate 0.31; Andrews-Kasy -0.01 (SE 0.02); WAAP 0.07 (SE 0.03); trim and fill 0.08 (SE 0.03) | b03, b04 | Contested |
| Nudge units vs academic papers | 126 RCTs, 243 nudges, 23.5 million people. Units 1.38 pp (SE 0.30), 8.1% over control; academic 8.7 pp, 33.4%. Nudge units excluded defaults | DellaVigna and Linos 2022 (a10; b06 duplicate) | Single source |
| Infrastructure cost overrun | Rail 44.7%, bridges/tunnels 33.8%, roads 20.4% (constant prices); no improvement in 70 years | Flyvbjerg 2006 (a12) | Single author group |
| Demand forecast error | Rail -51.4% (SD 28.1), 84% off by more than 20%; road +9.5% (SD 44.3), 50% off by more than 20%; 27 rail projects actual/forecast 0.61, SD 0.52 | a12, b09 | Single author group |
| UK DfT uplifts | Roads 15% at 50% risk, 45% at 10%; rail 40% and 68%; at 80% certainty rail 57%, roads 32% (local roads table; UK practice) | a14 | Single source |
| RCF benchmark (conditional, no control) | 61 rail forecasts: SD of accuracy 33% vs 9.1%; chance of 15%+ shortfall 80% vs 5% | Flyvbjerg 2013 (b08) | Descriptive only |
| Outside-view prompt for students | Expected to beat 84% of peers; prior prompt cut rating by about 20%; still too high | Lovallo and Kahneman 2003 via a16, b10 | Single, secondary |
| Planning fallacy | 33.9 predicted vs 55.5 actual days; 30% on time; 13%/19%/45% finished by 50/75/99% estimates | Buehler et al. via d14 | Secondary source only |
| Accountability (review) | 266 experiments, 211 articles, 1970-2016; vote counts: more effort and processing, lower overconfidence, worse dilution; pre-task announcement better | Aleksovska et al. 2019 (d05) | Direction only |
| Forcing before AI advice | N=199, 75% accurate AI; incorrect-AI trials N=663; carb-source chi2(2)=44.35; no net team accuracy gain | Bucinca et al. 2021 (d07) | Single, humans |
| Bonus lowers over-reliance | $0.50 vs $0.01, N=114, difference 0.93 [0.41, 1.46] | Vasconcelos et al. 2023 (d09) | Single, humans |
| LLM anchoring | ChatGPT low 20.83 vs high 105.97 (humans 22.5 vs 80.50), t(58)=8.78; Codex equals anchor 67%; irrelevant context cuts Codex 22.3-30.5 points | a22-a24, c12, c14 | Established |
| LLM anchoring, 20 models | Mean anchoring 0.39, framing 0.41, status quo -0.42 (models prefer change) | Malberg et al. 2024 (d12) | Single |
| LLM mitigations | GPT-4 anchoring distance baseline 0.250, awareness 0.105, contrastive 0.300, counterfactual 0.383, self-help 0.283; GPT-4 framing -0.405 to -0.470 with awareness | Echterhoff et al. 2024 (b15) | Established, model-specific |
| Self-help rewrite | GPT-4 biased prompts left: 0% group attribution, 2.7% framing; GPT-3.5 17.2% framing, 8.5% status quo | b16, c09 | Established for strong models |
| Bandwagon | GPT-3.5 0.524 baseline, AwaRe 0.260, SoPro 0.955 (worse); order bias no clear change | Sumita et al. 2024 (b17, d11) | Established |
| Base-rate neglect in LLMs | 40 items: GPT-4 15% correct, Gemini 15%, LLaMA3-70B 10%; sunk cost 0%, overconfidence 10%; abstain + bias inspection reached 93.5% on BRU 205 items | Zhong et al. 2025 (b18, b19) | Single source |
| LLM uses a supplied class rate | Planning-fallacy update score: GPT-4o -0.16, Gemini 1.5 Pro -0.14, GPT-4o mini -0.06, average about -0.02; small Llamas +0.19/+0.20 | Malberg et al. (d13) | Single, parsed table |
| LLM forecasting | Brier: random 0.250, best plain GPT-4 0.208, no retrieval/no fine-tune 0.206, system 0.179, crowd 0.149; accuracy 71.5% vs 77.0%; 48,754 questions | Halawi et al. 2024 (a29, c01, c02) | Established (one paper) |
| Where LLM beats crowd | Crowd .3-.7: system .199 vs crowd .246; worse near 0 or 1 | b13, c03 | Established |
| Ensembling | Trimmed mean 0.1649 vs none 0.1676 vs USC 0.1691; crowd + system 0.149 to 0.146 | c04 | Small gain |
| LLM crowd | 12 LLMs 0.20 (SD .12) vs 925 humans 0.19 (SD .19), t(60)=0.19, p=.850; mean 57.35% (acquiescence); human median seen: GPT-4 .17 to .14, Claude 2 .22 to .15 | Schoenegger et al. 2024 (c05, c06) | Single source |
| ForecastBench | Superforecasters 0.096, public 0.121, Claude 3.5 Sonnet 0.122 (200 questions); best without crowd data 0.136 | Karger et al. 2025 (c07) | Single source |
| Cognitive reflection | 150 CRT items: GPT-3 5% correct, humans 38%, GPT-3.5 59%, GPT-4 96% | Hagendorff et al. 2023 (c15) | Single source |
| Incentive-like prompts | EmotionPrompt relative gain Vicuna 9.58, Llama 2 6.00, ChatGPT 4.32, GPT-4 0.85, Bloom 0.51, Flan-T5-L 0.28; tip helped Llama-7B, not ChatGPT; $1000 tip lowered accuracy | a25, c16, c18 | Established as uneven |

## 4. Mechanisms and models

Each mechanism below is written so an engineer can build it.

**4.1 Default as hidden anchor.** Any option, draft answer, number or prior output placed in the prompt before the model decides acts as a default and an anchor. Three routes: advice (the model reads it as a recommendation), effort (copying is cheap), status quo. Implementation: in code, treat everything shown before the answer as a possible anchor. Log, per item, whether the answer equals or moves toward the anchor. Test with three arms: default first, default second, no default (forced choice). Johnson and Goldstein show the no-default arm is needed to see direction (opt-out 82% vs forced 79%: the harm was in opt-in).

**4.2 Time and deliberation reduce default pull.** White et al. (d03): default advantage 86% vs 66% at short time, 66% vs 64% at long time. Engineering reading: more reasoning before the answer may reduce anchor pull. This conflicts with G11 (think briefly) unless the extra step is a structured second look, not longer thinking. Untested on LLMs.

**4.3 Reference class forecast, algorithm.**
1. Classify the case (S0). Key the class by features, not by the story.
2. Retrieve N past cases of that class from the class record, with outcomes.
3. Build the distribution of outcomes: mean, SD, quantiles. Compute in code.
4. Place this case: does it differ from the class in a way that is measured, not felt?
5. Choose an acceptable risk level and read the quantile (the UK DfT uplift method: 50% risk gives a lower uplift, 10% risk a higher one).
6. Commit the estimate. Adjust only on named, checked differences.

The weak step is 1-2 (class choice), per Leleur et al. (d15) and d13. Applying a supplied rate is easy for current LLMs (d13).

**4.4 Commit-first, then compare (forcing function).** Bucinca et al. (d07): make the person commit before seeing advice. For the agent: write own estimate, then reveal the class record, then combine in code. Reduces copying a wrong record. Human evidence shows no net accuracy gain and low liking, so expect modest gain.

**4.5 Averaging with an outside estimate.** Halawi (c04, c06): weighting the crowd 4x with the system beat either alone; Schoenegger: averaging model and human beat either. Implementation: final = w*agent + (1-w)*class rate, fit w on held-out items.

**4.6 Self-help rewrite.** Echterhoff (b16): a separate call rewrites the task to strip bias cues (framing words, anchors, group labels), then the model decides on the clean text. Works for GPT-4-class models; breaks on weak ones (Llama changed 40-52% of anchored decisions).

**4.7 Accountability as process audit.** Aleksovska (d05): announce before the task that the reasoning will be checked; audience unknown; process not outcome. For the agent this is a prompt line, not a payoff. No LLM test exists (K24).

**4.8 Incentives for an LLM.** There are no payoffs. A tip or penalty is text. Its effect is a prompt-sensitivity effect, not a motivation effect. Bucinca and Vasconcelos effects (humans) do not transfer by default.

**4.9 Option order.** Shuffle option order in code and vote over orders (Echterhoff primacy, a28). Prompts did not fix order bias (b17, d11).

## 5. What holds up

**Replicated or confirmed.**
- Defaults move binary choices by large amounts in the original studies. The 401(k) and donation results are consistent with each other. Szaszi et al. note defaults as an exception to inconsistent effects (b04, b07).
- Reference class forecasting bias is real in infrastructure: overruns and demand errors persist (Flyvbjerg). All from one author group.
- Human-like anchoring and framing in LLMs: four or more independent sources (K13).
- Base-rate neglect in LLMs at 10-15% correct on a standard prompt (one source).
- Retrieval matters more than prompt wording for LLM forecasting (c01, b25).

**Failed, shrunk or contested.**
- Nudge average: 0.43-0.45 raw, 0.04-0.11 (Maier), 0.08 severe and 0.31 moderate (Szaszi/Mertens). Maier finds strong evidence of no effect for information (BF01 33.84) and assistance nudges, and ambiguity for structure.
- Nudge units: 1.4 pp vs 8.7 pp in papers. Defaults were excluded from the units, so the default claim is untested at scale there.
- Defaults fade with decision time and with experience (non-default share 7% to 37% in 15 months).
- Outside-view prompting cut but did not remove optimism (about 20% drop in ratings, still too high).
- Forcing functions reduce following wrong AI advice but add no net accuracy (d07).

**Moderators.**
- Domain: food 0.72 down to finance 0.25 (raw).
- Endorsement and status quo readings strengthen defaults (d04).
- Decision time (d03).
- Task difficulty and checking cost for over-reliance (d08).
- Whether accountability is announced before the task; whether the audience view is known.
- LLM capacity: self-help works on GPT-4, not on small Llamas; EmotionPrompt gain falls from 9.58 to 0.85 as models get stronger.

**Interventions that worked for LLMs.** Self-help rewrite (strong models); awareness for anchoring in GPT-4 (0.250 to 0.105) and bandwagon in GPT-3.5; abstention plus bias inspection (93.5% on BRU); retrieval of data; trimmed-mean ensembling (small); blending with an outside estimate; chain of thought for CRT (GPT-3 5% to 28% with an algebra suffix; GPT-4 96%).

**Interventions that did not work or backfired.** Ignore-the-anchor and CoT on anchoring (Lou and Sun, c11); few-shot and counterfactual prompts (anchoring distance 0.300-0.383 vs baseline 0.250; broke decisions); awareness on GPT-4 framing (-0.405 to -0.470); social projection ("answer as most people would") raised GPT-3.5 bandwagon from 0.524 to 0.955; a $1000 tip lowered accuracy. This agrees with schema section 4b (bias checklists and instructions do not reliably work).

## 6. Language models

**Biases present.** ChatGPT shows human-like anchoring (high anchor 105.97 vs low 20.83; t(58)=8.78), conjunction (18/20 chose it vs humans 10/20), framing (5 in all 11 positive trials, 4 in all 11 negative), endowment (kept owned coin 85%) (a24, c14). Codex equals the anchor 67% of the time (c12). A 20-model test finds average anchoring 0.39 and framing 0.41; status quo goes the other way at -0.42 (d12). Instruction tuning and RLHF increase decoy, certainty and belief-bias effects (c13): more aligned does not mean less biased. Anchoring shifts whole output distributions in small open models (b20). Lou and Sun: GPT-4 anchoring index about 0.45 vs 0.61 in a human-style study, and time questions not significant; Suri found ChatGPT's high anchor stronger than humans'. Designs differ.

**Base rates.** Standard prompt: GPT-4 15%, Gemini 1.0 Pro 15%, LLaMA3-70B 10% correct on 40 base-rate items; GPT-4 total 36.1% on the 205-item BRU set (b18, b19). Yet when told the class overrun rate, most models update (d13). So the failure is not applying a rate but having or finding the right one.

**Forecasting.** Plain models are near the 0.250 coin-flip Brier; best plain GPT-4 is 0.208. Retrieval plus fine-tuning plus a scratchpad that includes "consider historical base rates" gives 0.179 against crowd 0.149 (Halawi). Removing both retrieval and fine-tuning gives 0.206. The base-rate step is never ablated alone. The system beats the crowd where the crowd is unsure (.199 vs .246 for crowd forecasts .3-.7) and loses near 0 or 1. ForecastBench: top LLM runs all had crowd forecasts or a freeze value; the best LLM without crowd data on market questions is 0.136, superforecasters 0.096. LLMs lean yes (mean 57.35%).

**What changed bias, by how much.**
- Self-help rewrite: GPT-4 residual biased prompts 0% to 2.7%. Weak models 8-17% residual.
- Awareness: GPT-4 anchoring 0.250 to 0.105; no help or harm for GPT-4 framing; bandwagon GPT-3.5 0.524 to 0.260.
- Abstain plus bias inspection: up to 93.5% accuracy.
- Seeing the human median: GPT-4 Brier .17 to .14, Claude 2 .22 to .15.
- Collecting hints from several perspectives helped anchoring where ignore-the-anchor failed (c11).
- Incentive text: EmotionPrompt gain 0.85 on GPT-4; tip no gain on ChatGPT.

**Human-in-the-loop.** Not an LLM-bias test but relevant: forcing functions reduce following wrong advice; a larger bonus ($0.50 vs $0.01) lowers over-reliance.

**Caveats.** Most bias studies used 2022-2024 models (Codex, GPT-3.5, GPT-4, Llama 2). Effects on 2025-2026 models are unknown. No study tests an agent that retrieves a reference class and computes its outcome rate (K24, K29). No study tests accountability or stakes prompts with calibration measured. Incentive-prompt studies measure accuracy, not bias.

## 7. What our agent should take

Status marks follow the schema: [E] established (two or more independent sources), [S] single-source, [C] contested.

### Add now (established)

1. **Treat anything shown before the answer as an anchor; place it deliberately.** Schema: G (anchor-placement wording) and S1 input hygiene. [E] K13, K14. Evidence a22, a23, a24, c11, c12, c14, b20, b15. Rule in code: the draft answer, prior attempt or retrieved number goes after the model forms its own estimate, never before. (Caution: this placement rule itself is untested; the established part is that pre-answer content anchors.)
2. **Do not rely on a generic warning or on few-shot/contrastive examples as the debias step.** Schema: confirms section 4b; add the LLM evidence to the "bias checklists" row. [E] K14, K16, K27. Evidence b15, c10, b17, d10, d11, c11.
3. **Do not add incentive, tip, emotional-stakes or "answer as most people would" lines.** Schema: section 4b new row. [E] K23, K27. Evidence a25, b21, c16, c17, c18, c26, a26, d11. The claim is "no reliable gain on strong models", not "proven harmful".
4. **Supply data, do not ask the model to recall it.** Where a base rate matters, give the class record from code. Schema: S0 gate, S7, memory (class record). [E] K19, K20. Evidence a29, c01, c02, b25, c07, c08, c25. Retrieval, not prompt wording, carried the forecasting gain.
5. **Order effects are fixed in code.** Shuffle option order and vote over orders; prompts did not fix order bias. Schema: G5 (code selects), S7. [E] K14. Evidence a28, b17, d11.
6. **Plan for shrinkage.** Any imported human debiasing effect is an upper bound; require our own held-out measure before keeping a step (already G7 and section 8 rule 3). Status: [C] for the size (K04), [E] for the pattern of shrinkage. Evidence b01-b04, a10.

### Test first (single-source or contested)

1. **Reference class record as S0/S7 input (new operator or S0 step).** Retrieve N similar past tasks with outcomes, compute rate and quantile in code, place the estimate in that distribution. Schema: S0, S7, memory class record. [S] K06, K07, K09, K28; K24 and K29 record that no LLM study exists. Evidence a12-a14, b08, b09, d13, d15, c24. Biggest headroom: base-rate items 10-15% correct (b18).
2. **Commit first, then reveal the class record, then combine in code.** Schema: S7. [S] K26. Evidence d07, d08.
3. **Blend agent estimate with the class rate by a fitted weight; trimmed mean over samples.** Schema: S7, G5. [E] that blending helps in forecasting (K20), [S] for our tasks. Evidence c04, c06, b14.
4. **Self-help rewrite of the problem at S1 (strip framing, anchors, labels).** Schema: S1 input hygiene. [E] on GPT-4-class (K15); not tested on current models. Evidence b16, c09, d10.
5. **A structured second look to shrink default pull.** Schema: S7 with the G11 limit. [S] K25. Evidence d03.
6. **Pre-task process-accountability line ("each step will be audited by an unseen checker").** Schema: S0 prompt. [S] K10, K24. Evidence d05, d06. Watch for dilution (irrelevant facts get used).
7. **Abstain/inspect-for-named-bias for multiple-choice items.** Schema: conflicts with G6 on first pass; only for a flagged choice item. [S] K15. Evidence b18.
8. **Percentile output instead of a point estimate.** Schema: S7. [S] K07. Evidence a14.
9. **Extreme class rate rule: when the class record is near 0 or 1, move toward it.** Schema: S7. [S] c03 (hedging is a hypothesis). Evidence c03, b13.

## 8. Concrete tests on our bench

All arms use equal total tokens (setup cost counted, G7). Report effect with a confidence interval and the per-task-type spread.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Estimation tasks with a true answer from our own history (plan length, pass rate, run time) | A: plain; B: base-rate prompt (no data); C: retrieved class record with rate and quantile computed in code | Error vs truth; interval calibration | C beats B beats A; the gap C minus B is the unknown. Expect small gain on easy items, larger on hard (b13) |
| T2 | Same, with a correct vs a wrong-but-plausible class | C-correct vs C-wrong | Error difference | Shows cost of class choice (d13, d15); wrong class should hurt more than no class |
| T3 | Numeric items with random anchors | plain; warning line; anchor removed and re-asked (structure); anchor placed after own estimate | Anchoring index | Structure beats warning for GPT-4-class (b15, b16); warning may help anchoring but not framing |
| T4 | Default/option-first items | default first; default second; no default | Rate of following the default | Sign may be negative (status quo -0.42, d12); no-default arm decides |
| T5 | Short vs long reasoning budget on T3/T4 | short; long; structured second look | Anchor/default pull; accuracy | Pull falls with deliberation (d03); long thinking may hurt easy items (G11) |
| T6 | Base-rate items (BRU style, 40 items) | standard; supplied class rate; abstain + bias inspection | Accuracy | From 10-15% toward 90%+ with supplied rate; abstain arm up to 93.5% (b18) |
| T7 | Forecast-style binary questions | plain; retrieval; retrieval + base-rate step; step alone | Brier | Retrieval carries most; isolates the base-rate step Halawi never ablated |
| T8 | Same | agent only; class rate only; weighted blend; commit-first then blend | Brier | Blend beats both (c04, c06); commit-first lowers copying of a wrong record |
| T9 | Framing pairs | plain; awareness; self-help rewrite | Framing delta | Awareness may be worse on framing (b15); rewrite best on strong model |
| T10 | Any judgment set | neutral; accountability line (pre-task, unseen auditor); stakes/tip line | Accuracy and calibration (verbalised confidence, d17) | Accountability: lower overconfidence; stakes line: no gain on strong models |
| T11 | Option order | fixed; shuffled and voted | Position bias | Shuffle fixes order bias that prompts do not |
| T12 | Majority-opinion step | none; "answer as most people would" | Bandwagon, yes-bias | Expect worse (b17); confirm on current models |

## 9. What does not transfer, and why

- **Real payoffs.** Humans feel a $0.50 bonus; a model does not. A prompt tip is text. Human incentive and accountability effects (Lerner and Tetlock, Camerer and Hogarth, Vasconcelos) cannot be assumed for LLMs.
- **Inertia and effort.** Part of the default effect is that accepting is free. A model with full context rewrites as cheaply as it copies. The effort route is smaller; the advice (endorsement) and anchor routes remain.
- **Status quo bias.** Humans stick; the 20-model test shows status quo bias goes the other way (-0.42). A default in the prompt may be under-followed on that bias type.
- **Social audience.** Accountability works through social motives (pleasing, defending). A model has none, but it shows sycophancy and conformity (majority-style prompts worsened bandwagon). A known-audience framing could raise conformity.
- **Long-term habit change.** Most nudge studies measure single short-term behaviours. Our agent decides per item.
- **Aggregate nudge effects.** The pooled d spans food, finance and health, unrelated to reasoning steps. The corrected values (0.04-0.31) are priors, not forecasts for our steps.
- **Infrastructure reference classes.** Flyvbjerg's classes are large, curated and stable (rail, roads). Our task classes may be small, noisy and shifting. The 33% to 9.1% benchmark is descriptive, one project, author-built.
- **Human base-rate neglect.** Humans neglect base rates because of vivid cases. An LLM applies a supplied rate readily (d13); its problem is finding the class.
- **Older models.** Codex, GPT-3.5 and Llama-2 results may not describe current models.

## 10. Open questions

1. Does a retrieved reference class beat a base-rate prompt at equal tokens for an LLM agent? No study found (K29).
2. How large is the planning-fallacy correction from an outside-view prompt in preregistered studies? Only secondary figures (d14).
3. Has the outside view failed in a replication outside infrastructure? Lovallo, Clarke and Camerer (2012, d16) not opened.
4. What do Lerner and Tetlock (1999) show at effect-size level? Full text not opened.
5. What does Camerer and Hogarth (1999) show? Not opened.
6. What is the default effect alone after publication-bias correction? Not computed; Maier's structure category is 0.12 [0.00, 0.43].
7. Do active-choice (forced choice) designs help an LLM? No study.
8. Do awareness, self-help and majority prompts still behave the same on 2025-2026 models? Newest tests found are from 2024.
9. Does an accountability or stakes line change calibration in current models? No study.
10. Does showing a base rate reduce over-reliance on AI advice? Not found.
11. Do default effects shrink with reasoning budget in LLMs? Untested.
12. Is the order-bias result in Sumita et al. positive or null? The paper disagrees internally (d11).
13. Egger b=2.10 vs 2.28 and severe d 0.08 vs 0.03: possibly different supplement versions; unresolved (critique.md).

## 11. Sources

[V] = opened and read. [M] = snippet, recall or citation only.

- [V] Johnson and Goldstein (2003) Do defaults save lives? Science. https://www.dangoldstein.com/papers/DefaultsScience.pdf
- [V] Madrian and Shea (2001) The power of suggestion. NBER w7682. https://www.nber.org/system/files/working_papers/w7682/w7682.pdf
- [M] Madrian and Shea (2001) QJE 116. https://doi.org/10.1162/003355301753265543
- [V] White, Jiang and Albarracin (2021) The limits of defaults. Social Cognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC12478545
- [M] Jachimowicz, Duncan, Weber, Johnson (2019) Defaults meta-analysis (abstract only). https://ideas.repec.org/a/cup/bpubpo/v3y2019i02p159-186_00.html
- [V] Mertens, Herberz, Hahnel, Brosch (2022) The effectiveness of nudging. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC8740589/
- [V] Maier et al. (2022) No evidence for nudging after adjusting for publication bias. PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC9351501/
- [V] Mertens et al. (2022) Reply to Maier et al., Szaszi et al., Bakdash and Marusich. https://pmc.ncbi.nlm.nih.gov/articles/PMC9351449/
- [V] Szaszi et al. (2022) No reason to expect large and consistent effects of nudge interventions. https://pmc.ncbi.nlm.nih.gov/articles/PMC9351519/
- [V] DellaVigna and Linos (2022) RCTs to scale. Econometrica. https://www.econometricsociety.org/publications/econometrica/2022/01/01/rcts-scale-comprehensive-evidence-two-nudge-units (critique re-opened NBER w27594)
- [V] Flyvbjerg (2006) From Nobel Prize to project management. https://arxiv.org/abs/1302.3642
- [V] Flyvbjerg (2013) Quality control and due diligence in project management: taking the outside view. https://arxiv.org/abs/1302.2544
- [V] Leleur et al. (2015) Combining RCF with overconfidence theory (abstract). https://journals.open.tudelft.nl/ejtir/article/view/3083
- [M] Lovallo, Clarke and Camerer (2012) Robust analogizing and the outside view. https://doi.org/10.1002/smj.962
- [M] Lovallo and Kahneman (2003) Delusions of success (cited via Flyvbjerg)
- [M] Buehler, Griffin and Ross (1994) Exploring the planning fallacy. https://doi.org/10.1037/0022-3514.67.3.366
- [V] Planning fallacy summary (secondary). https://en.wikipedia.org/wiki/Planning_fallacy
- [M] Lerner and Tetlock (1999) Accounting for the effects of accountability. https://doi.org/10.1037/0033-2909.125.2.255 (abstract only)
- [V] Aleksovska, Schillemans and Grimmelikhuijsen (2019) Five decades of accountability research. https://www.journal-bpa.org/index.php/jbpa/article/download/66/49
- [M] Camerer and Hogarth (1999) Effects of financial incentives. https://doi.org/10.1023/A:1007850605129
- [M] Thaler and Sunstein (2008) Nudge. https://yalebooks.yale.edu/book/9780300262285/nudge/
- [M] Tetlock and Gardner (2015) Superforecasting (cited in Halawi)
- [V] Bucinca, Malaya and Gajos (2021) To trust or to think. https://arxiv.org/abs/2102.09692
- [V] Vasconcelos et al. (2023) Explanations can reduce overreliance on AI. https://arxiv.org/abs/2212.06823
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases. https://arxiv.org/abs/2202.12299
- [V] Suri, Slater, Ziaee, Nguyen (2023) Do LLMs show decision heuristics similar to humans? https://arxiv.org/abs/2305.04400
- [V] Li et al. (2023) EmotionPrompt. https://arxiv.org/abs/2307.11760
- [V] Bsharat, Myrzakhan, Shen (2023) Principled instructions. https://arxiv.org/abs/2312.16171
- [V] Salinas and Morstatter (2024) The butterfly effect of altering prompts. https://arxiv.org/abs/2401.03729
- [V] Echterhoff et al. (2024) Cognitive bias in decision-making with LLMs (BiasBuster). https://arxiv.org/abs/2403.00811
- [V] Sumita, Takeuchi, Kashima (2024) Cognitive biases in LLMs: a survey and mitigation experiments. https://arxiv.org/abs/2412.00323
- [V] Zhong, Wang, Cao, Sun (2025) Balancing rigor and utility. https://arxiv.org/abs/2406.10999
- [V] Valencia-Clavijo (2025) Anchors in the machine. https://arxiv.org/abs/2511.05766
- [V] Lou and Sun (2024) Anchoring bias in LLMs. https://arxiv.org/abs/2412.06593
- [V] Malberg, Poletukhin, Schuster, Groh (2024) A comprehensive evaluation of cognitive biases in LLMs. https://arxiv.org/abs/2410.15413
- [V] Itzhak et al. (2024) Instructed to bias. https://arxiv.org/abs/2308.00225
- [V] Hagendorff, Fabi, Kosinski (2023) Thinking fast and slow in LLMs. https://arxiv.org/abs/2212.05206
- [V] Halawi et al. (2024) Approaching human-level forecasting with language models. https://arxiv.org/abs/2402.18563
- [V] Schoenegger et al. (2024) Wisdom of the silicon crowd. https://arxiv.org/abs/2402.19379
- [V] Karger et al. (2025) ForecastBench. https://arxiv.org/abs/2409.19839
- [V] Tian et al. (2023) Just ask for calibration (abstract). https://arxiv.org/abs/2305.14975
- [M] Zou et al. (2022) Autocast. https://arxiv.org/abs/2206.15474
- [M] Binz and Schulz (2023) Using cognitive psychology to understand GPT-3. https://arxiv.org/abs/2206.14576

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 10 established claims: 4 confirmed as written, 6 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A03.06-K13** (number corrected). The 67% exact-match-to-anchor figure comes from the GPT-3 estimation replication in Jones & Steinhardt, not from Codex; the Codex result is the 22.3-30.5 point accuracy drop. Corrected claim: LLMs show human-like anchoring: low and high anchors move estimates (ChatGPT high anchor 105.97 vs low 20.83); GPT-3 updated estimates equal the anchor exactly 67% of the time; irrelevant context cuts Codex accuracy by 22-31 points. One study (Lou and Sun) found GPT-4 anchoring index 0.45 vs 0.61 in a human study (anchoring weaker than in humans), and anchoring on time questions not significant.
- **A03.06-K15** (number corrected). The 17.2% (framing) and 8.5% (status quo) residual biased prompts for GPT-3.5 are from the awareness (plain warning) prompt, not self-help; for GPT-3.5 self-help only cut biased group-attribution prompts by 8.9%. Corrected claim: Structural debiasing of LLM inputs and procedure (self-help re-asking, abstention plus bias inspection) works well for strong models: self-help left GPT-4 with 0% biased group-attribution and 2.7% biased framing prompts, while GPT-3.5 reduced biased group-attribution prompts by only 8.9% with self-help; abstention plus specific-bias inspection reached a best accuracy of 93.5% (Gemini 1.0 Pro) on the 205-item BRU set, and the plain awareness prompt left GPT-3.5 at 17.2% (framing) and 8.5% (status quo) biased prompts.
- **A03.06-K16** (now single-source: the sources are not independent). The few-shot/contrastive/counterfactual worsening (GPT-4 anchoring 0.250 to 0.300/0.383, numbers verified) rests on one paper (Echterhoff et al.) listed twice; the other source (2412.00323) tests awareness and social projection, not few-shot or contrastive prompts.
- **A03.06-K23** (reworded: the sources support less). Emotion-stimulus (9.58 to 0.85) and tipping (Llama-7B helped, ChatGPT minimal, $1000 lowered accuracy) numbers check out, but no source shows an uneven effect of politeness or penalty prompts (Bsharat et al. only lists them among 26 principles with pooled results). Corrected claim: Incentive-like prompts (emotion stimuli, tips) have uneven effects: EmotionPrompt relative gain 9.58 (Vicuna) down to 0.85 (GPT-4); tipping $1, $10 or $100 helped Llama-7B and made minimal difference for ChatGPT; a $1000 tip lowered accuracy compared with smaller tips. Politeness and penalty lines appear among 26 prompt principles but no per-principle effect is reported. Incentives for LLMs are prompt text, not payoffs.
- **A03.06-K26** (reworded: the sources support less). Bucinca et al.'s chi2(2)=44.35 (N=663 incorrect-AI trials, carb-source) and the least-favorable ratings are for the pooled cognitive-forcing-function category (update, wait, on-demand) vs simple explanations, not specifically a 'commit before seeing AI advice' design. Corrected claim: Cognitive forcing functions (making people decide before seeing the AI answer, wait for it, or request it on demand) reduced following wrong AI advice on carb-source detection compared with simple explanations (chi2(2)=44.35, N=663 incorrect-AI trials; not significantly overall) but did not raise team accuracy, and people gave these designs the least favorable ratings; overreliance is a cost-benefit choice that falls when checking is cheap on a hard task and when the bonus is higher ($0.50 vs $0.01 per maze).
- **A03.06-K27** (reworded: the sources support less). Self-help did work best for prompt-induced bias, but Echterhoff et al. report it also worked well for Llama 2 on framing (0% and 1.4% biased prompts left) and status quo (0-6%) and failed for Llama only on group attribution, so 'weak on Llama' is too broad. Corrected claim: Mitigations are model-dependent in LLMs: self-help rewriting performed best for prompt-induced bias in 2023 models (GPT-4 left 0% biased group-attribution and 2.7% framing prompts; GPT-3.5 reduced group-attribution prompts by only 8.9%; Llama 2 did well on framing and status quo but failed on group attribution) while awareness, few-shot and counterfactual prompts gave small or inconsistent gains; awareness helped some evaluator biases but order bias did not clearly change; asking the model to answer as most people would (SoPro) made the bandwagon effect much worse for GPT-3.5 (0.524 to 0.955).
- **A03.06-K01** (now single-source: only one opened source, code check).
- **A03.06-K19** (now single-source: only one opened source, code check).
