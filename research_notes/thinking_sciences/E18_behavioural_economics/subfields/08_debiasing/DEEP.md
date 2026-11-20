# Debiasing: deep document

*Subfield E18.08, behavioural economics. Built from evidence_a-d.jsonl (a01-a33, b01-b25, c01-c25, d01-d20), claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids in brackets. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Debiasing is the study of how to cut systematic judgement error. A bias here is a repeatable error with a known direction: anchoring, overconfidence, confirmation bias, framing, sunk cost, hindsight.

The field has two families of fix (Soll, Milkman and Payne 2015, a01):

- **Modify the person.** Teach rules, give strategies, give feedback, raise motivation.
- **Modify the environment.** Change the question format, the default, the incentive, the checklist, the decision model, or the group process.

A fix only works if it matches the source of the bias. Soll et al. say a System 2 correction needs three things: attention, the right normative rule, and the skill to apply it (a02). If the rule is unknown, more effort does not help. If the bias comes from low effort, a rule is not needed, effort is.

Why it matters for our agent. The agent is a scaffold over a language model. Our question is which "debias" steps are worth their tokens. SCHEMA 4b already says generic bias checklists and "be careful" prompts fail. This document tests that claim against the literature. It finds where the claim is right (reminders, awareness, reflection), where it is too broad (rule supply, input restructuring, format change, feedback), and what is still unknown.

Scope limits:

- Human evidence is mostly bias-test scores in labs, not real decisions. The one field-like test is Sellier 2019 (b03).
- Most human training evidence comes from one lab (Morewedge). One independent team (Martey 2014) agrees on the immediate effect (d16, d17).
- LLM evidence is 2022-2026, mostly small or older models, bias-score gaps rather than task accuracy, and almost never at equal tokens (critique.md).

Neighbouring subfields (not covered here): Heuristics and biases; Dual-process accounts of judgment; Prospect theory and risky choice; Verbal confidence; Retrieval and ensembles for LLM forecasts; Structured analytic techniques; Judicial bias and noise. Debate and reflection are also covered in the single-agent briefs F07, F08, F12.

## 2. History and theories in depth

**1980s: the rocky start.** Fischhoff (1982, a30, not opened) gave the first taxonomy. A bias can come from the task, the judge, or the match between them. His four strategies were warnings, telling the direction of bias, feedback, and extended training. Later authors call the early record rocky (a30, b09). Early tests found that training worked on the trained problem type but transfer failed unless training was extensive (statistics courses) or people knew they were being tested (b09, via Sellier 2019).

Lord, Lepper and Preston (1984, a33, not opened) gave the founding "consider the opposite" result: telling people to consider the opposite cut biased assimilation of evidence. Arkes (1981) called psychoeducation alone "absolutely worthless" (a10). Arkes, Dawes and Christensen (1986, a07, b08) found that paid judges did worse than unpaid ones when they tried to improve on a reliable formula.

**1990s-2000s: taxonomies and matching.** Arkes (1991, a31, not opened) split errors into strategy-based, association-based and psychophysical, and said each needs its own fix. Larrick (2004, a32, not opened) split fixes into motivational, cognitive (consider the opposite, rule training) and technological (linear models, group aggregation), and warned that more effort does not fix strategy-based errors. Fong and Nisbett (1991) showed statistical training transfers in the lab but fades over weeks (a03). Larrick, Morgan and Nisbett (1990) found economists apply sunk-cost logic more than humanities or biology professors (a03).

Lilienfeld, Ammirati and Landfield (2009, a09-a11) pointed out the imbalance: a 2008 PsycInfo search gave 1,211 hits for "cognitive bias" and 158 for "debias". Evidence on confirmation-bias debiasing was thin and mixed. They also noted backfire risks: listing many alternatives raised certainty that the outcome was inevitable (Sanna, Schwarz and Stocker 2002, a11), and the bias blind spot (Pronin 2004) makes people think debiasing is for others.

**Elicitation and aggregation line.** Soll and Klayman (2004) showed that asking for 10th, 50th and 90th percentiles raises interval hit rate about 20 points (a05). Haran, Moore and Morewedge (2010) built SPIES, a bin-probability format that removed overprecision at the 90% level (a17). Larrick, Mannes and Soll (2012) showed that averaging two answers from one person gives about half the gain of averaging two people (a06).

**2015: a user's guide and the first strong training result.** Soll, Milkman and Payne (2015, a01-a08) set six criteria for choosing a method: effectiveness, decision readiness, competence and benevolence of the decider, heterogeneity, decision frequency and decision complexity. Morewedge et al. (2015, a12-a14) reported that one 30-minute serious game with personalised feedback cut bias more than a video and lasted 2-3 months. Mellers et al. (2015, b10-b12) showed in a randomised forecasting tournament that a short probabilistic-reasoning module improved real forecasts. Aczel et al. (2015, b13, b14) tested "real-life" debiasing and found gains only for statistical-principle biases.

**2019-2025: transfer and replication.** Sellier, Scopelliti and Morewedge (2019, a15, a16, b03, b04) showed transfer to an unannounced business case. Heerma van Voss et al. (2025, b05, b06) replicated in national risk analysts. Martey et al. (2014, d16, d17) and Dunbar et al. (2017, d18) tested other games from other teams. O'Sullivan and Schofield (2019, b15) found a cognitive forcing checklist did not help doctors.

**2022-2026: LLMs enter.** Jones and Steinhardt (2022, a27) used human bias designs to find failures in code models. Suri et al. (2023, a26) found GPT-3.5 shows anchoring, framing and endowment effects. Echterhoff et al. (2024, a18-a20) made BiasBuster and tried awareness, few-shot and self-help debiasing. Lyu et al. (2025, a21-a23) proposed SACD, an iterative loop. Itzhak et al. (2024, a24) found instruction tuning raises some biases. Large benchmarks followed (Malberg a28, Knipper c14, CogBias c15). Anchoring-specific studies (Lou and Sun a25, Huang b20) found that generic prompts do not remove it. Sovrano et al. (2026, d05-d07) gave the first LLM support for the "supply the missing rule" view. Kraishan (2026, d01-d04) found extended thinking does not reduce bias.

**Competing theories of why biases persist** (b14):

1. **Missing mindware** (Stanovich and West 2008). People lack the rule. Fix: teach and supply the rule.
2. **Failure of monitoring or inhibition** (De Neys and Bonnefon 2013). People know the rule but do not stop the intuition. Fix: restructure input, force a pause at the right point, change the environment.
3. **Low effort.** Fix: money, accountability. Works only if effort is the limit (a07).
4. **Wrong model with more effort.** Incentives make people think harder but not smarter (a07).

The agent-relevant lesson from this history: the winning moves are rule supply, input and format change, aggregation, and feedback. The losing moves are warnings, instruction to be careful, and unstructured reflection.

## 3. Core findings with exact numbers

Human evidence first, then LLM evidence. "Status" uses the claims.jsonl marks.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| One-shot game cut bias more than video, Exp 1 (bias blind spot, confirmation bias, fundamental attribution error) | Game -46.25% immediately, -34.76% at 8 weeks; video -18.60% and -20.10%. N=278 recruited, 243 lab (game 160, video 83), 196 follow-up | Morewedge et al. 2015 (a12, b01) | [E] K03 |
| Same, Exp 2 (anchoring, projection, representativeness) | Game -31.94% then -23.57% at about 3 months; video -25.70% then -19.20%. N=269, 238 lab, 192 follow-up | Morewedge 2015 (a13) | [E] K03 |
| Training transfers to untrained facets | Trained facets d=.78 (post) and .24 (follow-up); untrained d=.79 and .65; trained vs untrained d=.20 at post, none at follow-up | Morewedge 2015 (a14) | [E] |
| Independent game test | Combined bias score 19.91 to 2.44 (game) vs 18.65 to 14.82 (video) post-test; at 8 weeks 6.70-11.42 (N 30-40 per cell) vs 17.36 (video, N=40). Game beats video on FAE; no advantage on bias blind spot; confirmation-bias advantage gone at retention | Martey et al. 2014 (d16, d17) | [E] K03 |
| Transfer to unannounced case | 58.8% vs 72.2% chose the inferior confirming race option; OR .549, CI [.33, .92], p=.022, N=290. Short-lag 56.8% vs long-lag 63.2%, ns (1 to 52 days) | Sellier et al. 2019 (a15, a16, b03) | [S] K04 |
| Mechanism is more disconfirming arguments, not lower confidence | Confirming statements 1.45 vs 2.07 (d=.39); disconfirming ns (d=.11); confidence beta .16, p=.053; training beta -.53, p=.047 | Sellier 2019 (a16, b04) | [S] K05 |
| Expert replication | 71 risk analysts (56 valid) and 118 students; intervention F(1,169)=20.74, eta2=.109; no group by intervention interaction; bias blind spot persisted and did not predict bias | Heerma van Voss et al. 2025 (b05, b06) | [E] K06 |
| Rule training works only for rule-type biases | N=154, 10 biases, 4-week follow-up. Gain mostly on statistical biases, most on insensitivity to sample size; no gain for others from analogical or awareness training | Aczel et al. 2015 (b13, b14) | [E] K02 |
| Statistical training transfer fades | Fades over weeks (no number in review) | Fong and Nisbett 1991 via a03 | [E] K02 |
| Forecast training in a randomised tournament | 743 forecasters, 150,000+ forecasts, 199 questions. Training r=.17 (t(741)=4.56); teaming r=.30; R=.43 (dispositions, training, teams), R=.64 once behaviour is added. Belief updating beta .45 | Mellers et al. 2015 (a29, b10-b12) | [E] K11 |
| Cognitive forcing checklist | 2.8 vs 3.1 cases correct, CI -0.94 to 0.45, p=.49. 76 analysed of 320 | O'Sullivan and Schofield 2019 (b15) | [C] K08 |
| Interval overprecision, plain 90% interval | 5/95 fractiles hit 73.79%, overprecision 16.21 points (d=.74). SPIES hit 88.35% | Haran et al. 2010 (a17) | [E] K09 |
| Percentile splitting | About +20 points hit rate. CFO 80% intervals held truth 33% of the time | Soll and Klayman 2004; Ben-David et al. 2013 (a05) | [E] K09 |
| Crowd within | One person averaged twice gives about half the gain of averaging two people; delay helps | Larrick et al. 2012; Vul and Pashler 2008 (a06) | [S] K10 |
| Incentives backfire when effort is not the limit | Paid judges did worse than unpaid against a formula | Arkes et al. 1986 (a07, b08) | [E] K01 |
| Planning prompt and defaults | Colonoscopy planning prompt 85% vs 63% (opt-out default); default enrolment +37 points | Narula 2013; Madrian and Shea 2001 (a08) | [S] |
| Debiasing evidence is thin | 1,211 PsycInfo hits "cognitive bias" vs 158 "debias" (June 2008) | Lilienfeld et al. 2009 (a09) | [E] |
| LLM biases are everywhere | 30 biases in some of 20 models (30,000 tests); bias-consistent in 17.8-57.3% of instances across 45 models | Malberg 2024; Knipper 2025 (a28, c14) | [E] K12 |
| GPT-4 framing | Admit 0.375 vs reject 0.780 (gap -0.405). Llama-2 7B: 32.1% fewer females judged good at math | Echterhoff 2024 (a18) | [E] K12 |
| GPT-3.5 anchoring | Mean estimate 20.83 (low anchor) vs 105.97 (high), t(58)=8.78; humans 22.50 vs 80.50 | Suri 2023 (a26) | [E] |
| Code models | Irrelevant functions cut accuracy 22.3-30.5 points; framing line copied 81% (Codex) vs 4.5% | Jones and Steinhardt 2022 (a27) | [S] |
| Instruction tuning raises some biases | GPT-4 belief bias 0.07 (valid) vs 0.49 (invalid); instruction-tuned models show more decoy, certainty, belief bias | Itzhak 2024 (a24, b22) | [S] K13 |
| Generic anchoring fixes fail | CoT, principles, ignore-hint, reflection: no significant gain. Llama-3.1-8B 34.7%: question-aware 36.8, self-improving 38.4, knowledge enhancement 50.5 (worse), adversarial finetune 33.3, Anti-DP 24.7 | Lou and Sun 2024; Huang 2026 (a25, c07, c10) | [E] K14 |
| Both-anchor strategy | GPT-4 near benchmark on 8 expert-hint questions; others stayed far off | Lou 2024 (c08) | [S] K16 |
| Awareness prompts break instruction following | Llama-2 7B contrastive admit 0.996, reject 1.000. GPT-4 awareness gap -0.470 vs -0.405 baseline (no gain). GPT-3.5 awareness 0.035 vs 0.165 | Echterhoff 2024 (a19, c02) | [E] K14 |
| Self-help rewrite | GPT-4 framing gap -0.405 to -0.010; GPT-3.5 0.165 to -0.080; GPT-3.5 group attribution got worse 0.085 to 0.150; GPT-4 left 2.7% biased framing cues | Echterhoff 2024 (a20, c03) | [S] K17 |
| SACD loop | FOMC llama3.1-8b: vanilla 0.3805, CoT 0.3425, self-help 0.2100, SACD 0.1570. Removing analysis: 0.2370 vs 0.1175 (gpt-3.5). Errors /500 finance: self-help 257 vs SACD 61 | Lyu 2025 (a21-a23, c04-c06) | [S] K18 |
| Debate and reflection raise bias | FOMC debate 0.5020 vs vanilla 0.3805; gpt-3.5 debate 0.5155; Reflexion PubMedQA 70B 0.5585. Few-shot 70B 0.3655 vs vanilla 0.1648 | Lyu 2025 (a22, b19) | [E] K19 |
| Rule elicitation before the decision | Bias sensitivity 12.9% (none) vs CoT 16.1% vs self-debias both 8.3% vs axiom steps 6.3% (p<.001); about 51% cut; open-ended 40 items: GPT-4o-mini 0.40 to 0.275, Llama-3.1-8B 0.40 to 0.30, CIs about 35 points wide | Sovrano et al. 2026 (d05-d07) | [S] K25 |
| Prompt debias by bias family | Response +40.5%, Social +5.9%, Info Processing -1.1%, Judgment -4.4% | Huang CogBias 2026 (c15) | [C] K20 |
| Activation steering | Bias cut 26-32%; Llama loses under 1 point on 25 benchmarks, Qwen up to 19.0 on Judgment biases | CogBias (c16) | [S] K21 |
| More prompt detail | Reduced most biases up to 14.9%; Overattribution worse by up to 8.8%; above 32B helped in 39.5% of cases | Knipper 2025 (c14) | [S] K22 |
| Distractor options | GPT-4o SimpleQA accuracy 35.14% to 65.40%, ECE 0.612 to 0.037; helped 91.97-95.86% of cases, harmed 4.14-8.03% | Chhikara 2025 (c17) | [S] K16 |
| Reasoning models anchored less | Anchored ratio GPT-4o 27.3%, R1 25.0%, Qwen3-235B thinking 22.0%, Mistral-7B 51.1%, Qwen2.5-0.5B 60.5% | Huang 2026 (b20, c09) | [C] K15 |
| Extra thinking does not help | 12,350 calls, 7 models. Reasoning vs sibling Delta=+0.031, p=.157. No significantly negative slope on realised tokens. GPT-5.1 used 116-118 tokens at any ceiling | Kraishan 2026 (d01-d03) | [C] K26 |
| Restating numbers lowers anchoring | Pooled change -0.015, CI [-0.026, -0.004]; item level p=.057; 5 of 5 items | Kraishan 2026 (d04) | [S] K16, K31 |
| LLM interval overprecision | GPT-4o-mini hit-average FinQA 18.29%, Medical 60.30%, MMLU 68.04% vs nominal 60-95%; CoT lifts MMLU to 80.49% for 4o-mini only; self-refinement mostly hurts | Bahaj et al. 2025 (d10, d11) | [S] K28 |
| Own memory can anchor | Qwen3-235B Hit@5 0.526 with insight memory vs 0.601 without | RealICU 2026 (d12, d13) | [S] K29 |
| Same-model debate raises judge bias | Position consistency with a debiased critic 0.817, 0.825, 0.831 (GPT-4o-mini, MTBench) | Ma et al. 2025 (d14, d15) | [S] K30 |
| Devil's advocate agents in clinical review | Initial diagnosis correct 0/80; top-2 differential 61/80 (76%) | Ke et al. 2024 (c21) | [S] K23 |
| Pre-mortem for LLMs | No effect size; InvThink safety analogue up to 32% less harm | Hills 2025; Kim et al. 2025 (d08, d09) | [S] K27 |
| Bias scores are fragile | 10 repeats of one prompt vary; small wording changes matter; 5 items per bias is too few | Suri 2023; Macmillan-Scott 2024; d20 (b24, c18, d20) | [E] K24, K31 |

## 4. Mechanisms and models

This section says how each mechanism works, in steps an engineer can build.

### 4.1 Match the fix to the error source (Soll, Milkman, Payne)

Decision table for the agent:

| Error source | Test | Fix |
|---|---|---|
| Missing rule (base rates, sample size, sunk cost, regression) | The right answer follows from a rule the agent can state when asked | Supply or elicit the rule before the decision (4.2) |
| Intuition or inhibition (anchoring, framing, order, authority cue) | The agent knows the rule when asked but ignores it when the cue is present | Remove or restructure the cue in the input (4.3) |
| Forgetting a step in a long task | Error is an omitted step, not a wrong judgement | A fixed checklist run by code (4.6) |
| Overprecision | Intervals too narrow | Change elicitation format (4.4) |
| Shared error across samples | Repeated samples agree and are wrong | Aggregation does not help; change the input or check against ground truth |

Human support: Aczel 2015 (b13, b14) found gains only for rule-type biases. LLM support: Sovrano 2026 (d05-d07) found rule elicitation cut sensitivity about half where reminders did not. No LLM study sorts biases by type as Aczel did (critique gap 4).

### 4.2 Rule-elicitation operator (single-source in LLMs)

Procedure from Sovrano et al. (d06):

1. Before the decision, ask the model to list the facts, the best-practice rules, and background axioms for this class of decision.
2. Then ask it to decide, with the list in context.
3. Measure sensitivity: the fraction of items whose answer flips between a matched biased and unbiased prompt.

Result: 12.9% to about 6.3% (p<.001 after Benjamini-Hochberg). CoT alone was worse, 16.1%. Cost: one extra call or a longer prompt. The open-ended version had smaller and uncertain gains (d07).

### 4.3 Input restructuring (neutralise, restate, add the other side)

Mechanisms that worked in LLM studies:

- **Neutral restatement** (SCHEMA S1 input hygiene). The agent or code rewrites the prompt, stripping the stated guess, the authority cue and the framing words, then answers the rewrite. This is self-help (a20) and the first step of SACD.
- **Both-anchor.** Give a low and a high anchor that straddle the truth (c08).
- **Distractor options.** Add three plausible wrong answers to a factual question (c17).
- **Restate every number** before answering (d04, directional only).

Why it should work: the bias is a surface-feature effect (Huang: anchoring is shallow, visible in early layers, c09). Removing the surface feature removes the cause. Instructions leave the cue in the context.

Capability gate: self-help works for GPT-4 and fails or over-edits for weak models (Llama changed 40-52% of decisions, b17).

### 4.4 Elicitation format

- **Fractiles.** Ask for 10th, 50th and 90th percentiles separately. Hit rate about +20 points in humans (a05).
- **SPIES.** Cut the range into bins, ask for probability in each bin, read intervals off the resulting distribution. Hit rate 88.35% vs 73.79% at the 90% level (a17).
- **Distribution before point.** Ask for the distribution, then the point.
- LLM side: a plain "give a 90% interval" does not calibrate GPT-3.5 or GPT-4o-mini and does not widen on request (d10). SPIES is untested on LLMs.

Implementation: the program builds the bins, the model fills probabilities, code normalises them to sum to 1 (consistent with G5) and computes the interval.

### 4.5 Aggregation and the crowd within

Sample twice with different framings and average (a06). Humans gain about half what two people would. For an LLM, two samples from one model are correlated (G4), so expect less. Averaging is a variance cut, not a bias cut. It does not remove a shared anchor.

### 4.6 Checklists

Soll et al. (a08): checklists help with forgetting errors in complex, stressful, repeated tasks. The cognitive forcing checklist for judgement (b15) did not. Split rule: a checklist item must name a concrete, checkable step (for example "was the base rate looked up?") that code can verify. A checklist item that says "consider whether you are biased" is a reminder and belongs under 4b.

### 4.7 Feedback and training

The game worked through personalised feedback and practice after each round (a12). Hypothesised pieces: define the bias, show examples, practice, get feedback on your own error, repeat across contexts. Transfer to untrained facets was as large as to trained ones (a14). An LLM analogue is a memory of past errors with their corrections, shown after the first attempt. This is untested. RealICU warns that remembering the agent's own conclusions causes anchoring (d12).

### 4.8 Iterative detect-analyse-rewrite (SACD)

Loop (c04): (1) determine whether the prompt contains a bias; (2) analyse which sentences and which bias; (3) rewrite only the biased sentences; repeat until step 1 says no bias. Ablation: removing the analysis step hurts most (0.2370 vs 0.1175 on FOMC with GPT-3.5, c06). Error types: self-help under-debiases (257 of 500 errors, finance); SACD fixes that but adds bias confusion (49, 108, 73 errors) (a23). Tokens were not matched to baselines. It is a detector plus a rewrite, so it fits SCHEMA S1 only if code (not the model) caps the rounds at 2-3.

### 4.9 Devil's advocate and pre-mortem

Prospective hindsight (imagine the plan failed, explain why) rests on Mitchell et al. 1989 (a04). Consider-the-opposite is helped by listing a few reasons, hurt by listing many (a11). For LLMs, "could you be wrong" (Hills, d08) and InvThink (d09) have no measured effect on judgement bias. This is a candidate, not a finding.

### 4.10 Measuring bias in an LLM

Bias score = difference in biased answers between a biased and a control prompt, over matched pairs (Lyu b18; Sovrano d05). Rules (K24, K31): at least 100 matched items per bias, paraphrase sets, 10 or more repeats, analyse per item (the item is the unit, not the call), report both bias and accuracy, log tokens per arm.

## 5. What holds up

### Replicated or established

- **Reminders and awareness alone do little.** Human: Arkes called psychoeducation worthless (a10); Aczel found awareness gave no gain at 4 weeks (b13). LLM: Lou and Sun, Huang, Echterhoff, Sovrano all show small or no effects (K14, K01). [E]
- **Incentives help only effort-limited errors** (a07, b08). [E]
- **Rule training works for rule-type biases, fades over weeks** (a03, b13, b14). Three sources. [E]
- **Game training with feedback.** Two teams agree on the immediate effect and an 8-week effect (d16, d17); Morewedge reported 2-3 months. Heerma van Voss 2025 replicated the Carter Racing training in experts (b05). [E]
- **Format change for overprecision.** Percentile splitting and SPIES, two sources (a05, a17). [E]
- **Debate and Reflexion raise LLM bias.** Three sources (a22, b19, d14). [E]
- **Probabilistic-reasoning training improved real forecasts.** Randomised; r=.17 (b10). [E]
- **LLMs show biases and are fragile to wording** (K12, K24). [E]

### Failures and weak points

- Morewedge's abstract quotes numbers mixing Exp 1 and Exp 2; use the body (critique.md).
- Martey: retention N is only 30-40 per cell and attrition was heavy (144 of 391 at 8 weeks, from critique). No game advantage on the bias blind spot. Confirmation-bias advantage was lost at retention.
- Sellier: the case-completion difference was not significant (73.1% vs 63.0%, p=.071), and the sample was graduate students in one school.
- O'Sullivan: 76 of 320 analysed, so low power. Doctors liked the tool but it did not help (b15).
- Trained-facet effect fell from d=.78 to .24 at follow-up (a14). Part of the effect decays.
- Bias blind spot did not shrink with expertise or training and did not predict actual bias (b06).
- Almost all outcomes are bias-test scores, not decisions with consequences.

### Moderators

- **Bias source** (rule vs intuition vs effort). The strongest moderator (b14).
- **Time lag.** Statistical training fades in weeks. Game effect fades partly in 2-3 months. Sellier's lag of 1 to 52 days showed no fade.
- **Domain closeness.** Best education is domain-specific and close in time to the decision (b07).
- **Model capability** (LLMs). Self-help works for GPT-4 but fails for Llama-2 7B (K17). Reasoning models are anchored less in one study (b20) and not in another (d01).
- **Bias family** (LLMs). Prompt debiasing helps Response biases, not Judgment ones (c15).
- **Expert hints.** Expert anchors were never overcome by any simple prompt (c07).

### Interventions that worked vs did not

| Worked | Did not work or backfired |
|---|---|
| Game with feedback (human) | Video alone: smaller (-18.60%) |
| Rule training for statistical biases | Awareness training for other biases |
| Percentile splitting, SPIES | Plain 90% interval |
| Probabilistic-reasoning module (forecasting) | Scenario module (dropped, b12) |
| Neutral rewrite by a strong model (GPT-4) | Few-shot debias examples (collapse to 0 or 1) |
| Rule elicitation before decision (LLM, single-source) | CoT (16.1% vs 12.9%, worse) |
| Both-anchor, distractors | "Ignore the hint", reflection |
| Single devil's advocate (clinical, single-source) | Same-model debate, Reflexion |
| Activation steering (weights; out of scope) | Knowledge enhancement (anchoring 50.5%, worse) |

## 6. Language models

### Baseline behaviour

- Biases are present across families and sizes. Malberg: all 30 biases in some of 20 models; framing mean about 0.41 and anchoring about 0.39 across models (b23). Knipper: 17.8-57.3% bias-consistent across 45 models (c14).
- GPT-3.5 anchoring shifted the mean from 20.83 to 105.97; GPT-4 from 22.0 to 94.33 on 5 trials per condition (a26).
- GPT-4's anchoring index was about 0.45 against 0.61 in the human source (c07). Stronger models were more consistently anchored; 9 of 11 non-significant exceptions came from GPT-3.5 (a25).
- Models say they are unbiased and then show the bias (Suri, a26).
- Many errors are not human-like (c18). Kraishan found framing, loss aversion, escalation and confirmation lean opposite to humans in all seven models. Only anchoring is human-like (+0.163, d=1.89, d03).
- Instruction tuning raises decoy, certainty and belief effects (a24).
- Code models: irrelevant preceding functions cut accuracy 22.3-30.5 points (a27).

### What changed it, by how much

| Intervention | Effect | Where |
|---|---|---|
| Awareness or "be careful" prompt | Often nothing; GPT-3.5 framing gap 0.165 to 0.035 helped; GPT-4 no gain (-0.405 to -0.470) | a19 |
| Awareness on judge biases | Helped order, compassion fade, egocentric, bandwagon on GPT-3.5; bandwagon and verbosity on GPT-4; order bias unchanged by any method | c12 |
| CoT | Anchoring none (Lou); FOMC 0.3805 to 0.3425 (small); Sovrano 12.9% to 16.1% (worse) | a25, c04, d05 |
| Reflection, ignore-hint, principles | No significant effect on anchoring | b21 |
| Few-shot debias examples | Often worse; collapse to 0 or 1 | a19, a22 |
| Self-help rewrite | GPT-4 framing -0.405 to -0.010. Weak models over-edit | a20 |
| SACD loop | FOMC 0.3805 to 0.1570 (llama3.1-8b) | a21 |
| Rule elicitation | 12.9% to 6.3% | d06 |
| Question-aware, self-improving prompts | Anchoring 34.7% to 36.8% and 38.4% (no gain) | c10 |
| Anti-DP | 34.7% to 24.7% | c10 |
| Detailed prompts | Up to 14.9% less for most biases, one bias worse | c14 |
| Distractor options | ECE 0.612 to 0.037 (GPT-4o, SimpleQA) | c17 |
| Reasoning-trained models | Anchored ratio 22-27% vs 51-61% for small models (Huang), but not less biased than siblings (Kraishan Delta +0.031) | b20, d01 |
| Extra thinking tokens | No negative slope; realised tokens often far below ceilings | d02 |
| Restate every number | -0.015 pooled, directional | d04 |
| Debate or Reflexion | Raises bias (0.3805 to 0.5020) | a22 |
| One debiased critic in debate | Small gain (0.817 to 0.831) | d15 |
| Devil's advocate multi-agent | 76% top-2 vs 0/80 initial (no equal-token control) | c21 |
| Activation steering | -26 to -32% bias; capability cost varies | c16 |
| Insight memory (agent's own conclusions) | Hit@5 0.526 vs 0.601 without; anchors | d12 |

### Reading the pattern

1. Changing the input beats adding an instruction (K16).
2. Supplying or eliciting the rule before the decision is the best-supported prompt-level fix so far, but it has one source (K25).
3. Generic reflection and debate do not fix and can worsen bias (K14, K19).
4. Effects depend on the model and the bias, so a one-size debias prompt is fragile (K20).
5. Reasoning models are probably not a debiasing tool in themselves (K15 contested, K26 contested).
6. Interval calibration is poor and asking for higher confidence does not help (d10).

### Measurement cautions

Bias scores differ by paper, so numbers cannot be pooled. Sample sizes are small (5 items per bias, 40 open-ended items). Models are old or small. Token costs are almost never equalised. SACD uses several calls per item. Hills (d08) is a demonstration with no control arm.

## 7. What our agent should take

Marks: schema part (G guardrail, S state, O operator, memory), status, evidence ids and claim ids.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| A1 | **Keep SCHEMA 4b "bias checklists and debiasing instructions" and sharpen it.** Do not add "be aware of bias X", "ignore the hint", "reflect" or "be careful" lines. Wording change: they fail as reminders; this does not rule out rule supply or input change (below). | 4b, G1 | [E] K01, K14 | a07, a10, b08, b13, a25, b21, c07, a19, d05 |
| A2 | **Do not add debate or Reflexion as a debiaser.** It raises measured bias. Already G9; add the bias-specific evidence as a second support. | G9 | [E] K19 | a22, b19, d14 |
| A3 | **Input hygiene as a debiasing step.** Code (or one rewrite call) removes stated guesses, authority cues, framing words and irrelevant numbers before attempts, and keeps the original beside it. This matches S1. The evidence says input change works more often than instruction. The rewrite should be done by code where the cue can be pattern-matched; by the model only on strong models. | S1, O6 | [E] that input change beats instruction (K16, 4 sources); [S] for the exact remedy | a20, c03, c08, c17, c22, d04 |
| A4 | **Elicit a distribution before a point for numeric or probability answers.** Bins or fractiles, normalised in code. Human evidence is established; LLM evidence is missing, so it goes in as a format default for human-style tasks only after the test U6. For now add only "normalise exclusive probabilities in code" (already in G5). | G5, S4 | [E] in humans K09; LLM untested | a05, a17, d10 |
| A5 | **Measurement protocol for any debias arm.** 100 or more matched items per bias, paraphrase sets, 10 or more repeats, per-item analysis, tokens logged, accuracy reported beside bias. Becomes a rule in section 6 (logging) of SCHEMA and in our bench. | log, G7 | [E] K24, K31 | b24, c18, d07, d20, d02 |
| A6 | **Do not carry forward the agent's own conclusions as memory before the first attempt.** Already SCHEMA section 5 (lessons shown after the first attempt). Add the RealICU result as support. | memory | [S] K29 (the rule itself is [S] in SCHEMA) | d12, d13 |
| A7 | **Rule-type vs intuition-type routing is the right frame for any debias step.** A debias step must name which error source it targets. A step that targets "bias in general" is rejected by G7. | G7, 4b | [E] human K02 | a02, b13, b14 |

### Test first (not yet established; see UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | **Rule-elicitation operator before the decide step** (list the facts, rules and axioms for this problem class, then decide). Best-supported LLM prompt-level fix; one source, small models, a sensitivity metric. | O (new operator, used at S1/S2 for judgement classes) | [S] K25 | d05, d06, d07 |
| T2 | **Neutral rewrite plus restate-the-numbers** vs instruction at equal tokens, per model capability. | S1, O6 | [S] K16, K17 | a20, c03, d04 |
| T3 | **Iterative detect-analyse-rewrite (SACD-style) capped at 2-3 rounds** against best-of-N at equal tokens. | O (loop at S1) | [S] K18 | a21, a23, c05, c06 |
| T4 | **Fractile or SPIES elicitation for LLM forecasts.** | O elicitation, S7 | [E] in humans, untested in LLMs (K09, K28) | a05, a17, d10, d11 |
| T5 | **Both-anchor and distractor options.** | O6 | [S] K16 | c08, c17 |
| T6 | **Past-error memory with corrections** vs conclusion memory vs none. Mimics game feedback. | memory | [S] K03 (human), K29 | a12, a14, d12 |
| T7 | **Pre-answer failure listing (pre-mortem) vs post-answer "could you be wrong"** vs none. | O (devil's-advocate, G1-gated) | [S] K27, [C] K07 | a04, a11, d08, d09 |
| T8 | **Single-agent devil's advocate** (one extra pass that argues the best alternative) vs multi-agent vs none. | O | [S] K23 | c21, d15 |
| T9 | **Checklist split: forgetting-type vs judgement-type tasks.** | G, S4 | [C] K08 | a08, b15 |
| T10 | **Thinking on vs off, 1k vs 4k thinking tokens vs one-line input restatement** at logged realised tokens. | S (extended reasoning), G11 | [C] K15, K26 | b20, d01, d02, d04 |
| T11 | **Per-family routing** (Response vs Judgment biases) vs one generic prompt. | G | [C] K20 | c15, c12 |

Notes on the add list:

- Nothing in the "Test first" list may be added to SCHEMA.md until its test passes (SCHEMA section 8, rule 2).
- Weights-level fixes (activation steering, Anti-DP, adversarial fine-tuning, instruction-tuning choice) are out of scope for a prompt scaffold (K21).
- The model choice item (K13, base vs instruction-tuned) is single-source and is not actionable for a scaffold over a fixed model.

## 8. Concrete tests on our bench

All arms use equal tokens: the plain arm gets the extra budget as additional independent samples with code selection (best-of-N or self-consistency), per G7. Log realised tokens per arm. Use 100 or more matched biased/control item pairs per bias, 3 or more paraphrases per item, 10 or more repeats, and analyse per item with a paired test. Report accuracy next to bias.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 Reminder control | Anchoring and framing pairs (numeric estimates; admit/reject style) | (a) plain; (b) plain plus "be aware of bias X, ignore the hint"; (c) plain with extra samples to match tokens | Bias gap (biased minus control answer) and accuracy | (b) within 3 points of (a). Confirms 4b. |
| B2 Rule elicitation | Matched biased/unbiased dilemmas, labelled rule-type (base rate, sample size, sunk cost, hindsight) vs intuition-type (anchor, framing, order) | (a) plain; (b) CoT; (c) rule-elicit then decide; (d) best-of-N at (c)'s tokens | Sensitivity (flip rate between matched pairs), split by rule-type and intuition-type | (c) cuts sensitivity by 30% or more on rule-type; little on intuition-type. Source d06 reports 12.9% to 6.3% on small models. |
| B3 Neutral rewrite | Anchoring items with stated guess, authority cue, irrelevant number; framing pairs | (a) plain; (b) instruction "ignore"; (c) code-stripped input; (d) model rewrite then answer; (e) restate-the-numbers line; run on a strong and a small model | Anchored ratio, bias gap, accuracy against truth | (c) or (d) cut anchoring more than (b); (d) fails on the small model (Echterhoff). Expect 5-15 points. |
| B4 SACD vs best-of-N | Same items, multi-bias prompts | (a) plain; (b) SACD capped at 3 rounds; (c) best-of-N at (b)'s tokens; (d) self-consistency | Bias score and accuracy | Open. Source gap: 0.3805 to 0.1570 without token match. Expect the gap to shrink at equal tokens. |
| B5 Elicitation format | Numeric forecast items with known outcomes | (a) point only; (b) single 90% interval; (c) 10/50/90 fractiles; (d) SPIES bins normalised in code | Hit rate of 80/90% intervals, mean interval width, Brier or CRPS | (c) and (d) lift hit rate toward nominal. Human +15 to +20 points. LLM unknown. |
| B6 Anchor structure | Anchoring items with expert and random anchors | (a) one anchor; (b) both anchors straddling truth; (c) no anchor; (d) distractor options on MCQ items | Anchor index and accuracy | (b) near benchmark on items where anchors straddle truth; no gain where they do not. |
| B7 Past-error memory | Stream of 200 mixed-bias items with feedback on earlier items; held-out items of untrained bias facets | (a) no memory; (b) memory of past conclusions; (c) memory of past errors plus correction, shown after first attempt; (d) best-of-N at equal tokens | Bias on held-out facets, accuracy | (c) transfers to untrained facets by at least 20% bias cut; (b) worse than (a) (RealICU). |
| B8 Failure listing | Planning and forecasting items (hindsight, optimism), plus the items from B1 | (a) plain; (b) pre-answer failure listing; (c) post-answer "could you be wrong"; (d) consider-the-opposite with 2 reasons; (e) best-of-N | Accuracy, flip rate right-to-wrong and wrong-to-right (G1 log) | (b) or (d) small gain; (c) breaks as many as it fixes. |
| B9 Devil's advocate | Diagnosis-type vignettes with a misleading first impression | (a) plain; (b) single-agent devil's advocate pass; (c) multi-agent roles; (d) best-of-N | Top-1 and top-2 accuracy | (b) matches (c) at lower cost; both beat plain only if the misleading cue is a bias, not a knowledge gap. |
| B10 Checklist split | Two task sets: forgetting-type (long task with 8 required steps, one often omitted) and judgement-type (bias vignettes) | (a) plain; (b) code-verified step checklist; (c) generic reminder checklist | Omission rate; judgement accuracy | (b) cuts omissions by 30% or more; (c) null on judgement. Matches Soll boundary. |
| B11 Reasoning budget | Anchoring, framing, loss aversion items | (a) thinking off; (b) thinking 1k; (c) thinking 4k; (d) off plus input restatement | Bias with realised tokens logged | No negative slope in (b) to (c) (Kraishan). (d) at least as good as (c) at lower cost. |
| B12 Power and stability pilot | One bias, 20 paraphrases, 20 repeats | plain only | Within-item and between-paraphrase variance | Sets the minimum item count for B1-B11. Run first. |

## 9. What does not transfer, and why

- **Human training time and decay.** The game worked over 30 minutes of practice with feedback and still lost part of its effect by 2-3 months. An LLM in a fresh context has no between-session decay but also no learning. Training transfer in humans does not map to a stateless prompt. The nearest analogue is memory (T6).
- **Bias blind spot.** It concerns self-knowledge. An LLM has no stable self-image to protect. Self-reports are unreliable anyway (Suri: the model says it is not biased and then is, a26).
- **Motivation, incentives, accountability.** They help effort-limited errors in people. An LLM does not have effort in that sense. More tokens are not more effort (K26). Telling a model "you will be rewarded" is a reminder.
- **Warnings and awareness.** Weak in humans (a10) and weak in LLMs (K14). They are not a transfer problem; they just fail twice. But awareness helped some LLM judge biases (c12), so do not drop the idea completely for position-type judge tasks. Use code-level fixes there (swap order, run both orders, average).
- **Group debiasing.** Human groups add independent information. Same-model agents share errors (K19, K30). Human group evidence (teaming r=.30, b10) does not transfer to same-model debate. Independent models or code-selected samples do not suffer from this, but the evidence for diverse-model groups is thin.
- **Human-direction of bias.** LLMs show some human-like biases (anchoring) and some reversed ones (framing, loss aversion in Kraishan, d03). A fix tuned to the human direction can go the wrong way. Always measure the direction on our model first.
- **Instruction tuning as a cause.** Itzhak (a24) says RLHF raises some biases. Not actionable in a scaffold over a fixed model.
- **Activation steering and fine-tuning.** Out of scope for a scaffold with no weight access (K21).
- **Field outcomes.** No human study shows a lasting effect on real consequential decisions beyond Sellier's single case. Bias-test score gains may not be decision-quality gains. Our bench should measure task accuracy, not only bias gap.
- **Domain-specific human knowledge.** Meteorologists calibrated in their field are poorly calibrated outside it (b07). For the agent, class-specific rule libraries are needed; a general rule list will not help.

## 10. Open questions

1. At equal tokens, does SACD beat best-of-N on anchoring and framing with frontier reasoning models? (gap 1, B4)
2. Do reasoning-trained frontier models (GPT-5-class, Claude thinking) still show anchoring and framing, and does budget above about 3,500 tokens help? Huang and Kraishan disagree. (gap 2)
3. Is there a non-Morewedge replication of one-shot game training beyond 8 weeks, and a replication with a non-video comparator? (gap 3)
4. Which LLM biases are missing-rule errors and which are intuition errors? No LLM study sorts them as Aczel did. (gap 4)
5. Does pre-mortem prompting have any measured LLM effect on judgement? (gap 5)
6. Does past-error memory transfer to untrained bias facets as the game did? Does storing conclusions anchor, as RealICU suggests? (gap 6)
7. Does SPIES or fractile elicitation calibrate LLM intervals? (gap 7)
8. Does role-diverse debate (DReaMAD, MoLaCE) beat single-agent debiasing at equal tokens? (gap 8)
9. When does a checklist help an LLM (forgetting-type errors) and when does it fail (judgement errors)? (gap 9)
10. How stable are LLM bias scores across paraphrases, and what item count detects a 5-point gain? (gap 10)
11. Why do the two reasoning studies disagree: the metric (anchored ratio vs signed score), item set, or model set?
12. Do the effects of rule elicitation persist on frontier models, or is it only a small-model repair?
13. Is the Echterhoff self-help result a capability threshold, and where is it for current models?
14. Human side: does the bias blind spot have any debiasing that works, since it persisted in experts (b06)?
15. Is there any LLM analogue of the Sanna backfire, where listing many alternatives raises certainty?

## 11. Sources

Marked [V] if the page or PDF text was opened this session (per the `opened` field in the evidence files, with the critique's re-opened list), [M] if known only from a snippet, abstract or citation.

- [V] Soll, Milkman, Payne (2015) A User's Guide to Debiasing (Wiley Blackwell Handbook of JDM, ch. 33) | https://static1.squarespace.com/static/5353b838e4b0e68461b517cf/t/59b966cd4c0dbf23b6b997b2/1505322703896/39-2016_Handbook_of_JDM.pdf | ids a01, a02, a03, a04, a05, a06, a07, a08
- [V] Lilienfeld, Ammirati, Landfield (2009) Giving debiasing away | https://pdf.stafforini.com/lilienfeld-2009-giving-debiasing-away.pdf | ids a09, a10, a11
- [V] Morewedge et al. (2015) Debiasing decisions: improved decision making with a single training intervention | https://openaccess.city.ac.uk/id/eprint/12324/1/Debiasing_Decisions_PIBBS.pdf | ids a12, a13, a14
- [V] Sellier, Scopelliti, Morewedge (2019) Debiasing training improves decision making in the field | https://openaccess.city.ac.uk/id/eprint/22233/1/DebiasingTrainingTransfers_InPress.pdf | ids a15, a16
- [V] Haran, Moore, Morewedge (2010) A simple remedy for overprecision in judgment (SPIES) | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/34DDFA0D8B602B6089A1B6BEEF22A486/S1930297500001637a.pdf/a-simple-remedy-for-overprecision-in-judgment.pdf | ids a17
- [V] Echterhoff et al. (2024) primacy and status-quo results | https://arxiv.org/abs/2403.00811 | ids a18, a19, a20, b16, b17, c01, c02, c03
- [V] Lyu et al. (2025) negative results for reflection and debate | https://arxiv.org/abs/2504.04141 | ids a21, a22, a23, b18, b19, c04, c05, c06
- [V] Itzhak, Stanovsky, Rosenfeld, Belinkov (2024) Instructed to bias | https://arxiv.org/abs/2308.00225 | ids a24, b22
- [V] Lou (2024) Anchoring Bias in Large Language Models: An Experimental Study | https://arxiv.org/abs/2412.06593 | ids a25, b21, c07, c08
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans? (GPT-3.5) | https://arxiv.org/abs/2305.04400 | ids a26, b24
- [V] Jones and Steinhardt (2022) Capturing failures of LLMs via human cognitive biases | https://arxiv.org/abs/2202.12299 | ids a27, b25
- [V] Malberg et al. (2024) A Comprehensive Evaluation of Cognitive Biases in LLMs | https://arxiv.org/abs/2410.15413 | ids a28, b23, c13
- [V] Mellers et al. (2015) The psychology of intelligence analysis: drivers of prediction accuracy | https://faculty.wharton.upenn.edu/wp-content/uploads/2015/07/2015---the-psychology-of-intelligence-analysis.pdf | ids a29
- [M] Fischhoff (1982) Debiasing (in Kahneman, Slovic, Tversky eds., Judgment under Uncertainty) | no URL (cited via secondary source) | ids a30
- [M] Arkes (1991) Costs and benefits of judgment errors: implications for debiasing | no URL (cited via secondary source) | ids a31
- [M] Larrick (2004) Debiasing (Blackwell Handbook of JDM, pp. 316-337) | no URL (cited via secondary source) | ids a32
- [M] Lord, Lepper, Preston (1984) Considering the opposite: a corrective strategy for social judgment | no URL (cited via secondary source) | ids a33
- [V] Morewedge, Yoon, Scopelliti, Symborski, Korris, Kassam (2015) Debiasing decisions: improved decision making with a single training intervent | https://doi.org/10.1177/2372732215601001 | ids b01, b02
- [V] Sellier et al. (2019) mechanism and Hawthorne control | https://doi.org/10.1177/0956797619861429 | ids b03, b04, b09
- [V] Heerma van Voss et al. (2025) bias blind spot and floor effect | https://doi.org/10.1038/s41598-025-28794-w | ids b05, b06
- [V] Soll, Milkman, Payne (2015) A user's guide to debiasing | https://doi.org/10.1002/9781118468333.ch33 | ids b07, b08
- [V] Mellers et al. (2015) individual differences | https://doi.org/10.1037/xap0000040 | ids b10, b11, b12
- [V] Aczel et al. (2015) rival accounts of why biases persist | https://pmc.ncbi.nlm.nih.gov/articles/PMC4523707/ | ids b13, b14
- [V] O'Sullivan and Schofield (2019) A cognitive forcing tool to mitigate cognitive bias: a randomised control trial | https://pmc.ncbi.nlm.nih.gov/articles/PMC6325867/ | ids b15
- [V] Huang et al. (2025/2026) Understanding the Anchoring Effect of LLM with Synthetic Data | https://arxiv.org/abs/2505.15392 | ids b20, c09, c10, c11
- [V] Sumita, Takeuchi, Kashima (2024) Cognitive Biases in LLMs: A Survey and Mitigation Experiments | https://arxiv.org/abs/2412.00323 | ids c12
- [V] Knipper et al. (2025) The Bias is in the Details: An Assessment of Cognitive Bias in LLMs | https://arxiv.org/abs/2509.22856 | ids c14
- [V] Huang et al. (2026) CogBias: Measuring and Mitigating Cognitive Bias in LLMs | https://arxiv.org/abs/2604.01366 | ids c15, c16
- [V] Chhikara (2025) Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in LLMs | https://arxiv.org/abs/2502.11028 | ids c17
- [V] Macmillan-Scott and Musolesi (2024) (Ir)rationality and Cognitive Biases in LLMs | https://arxiv.org/abs/2402.09193 | ids c18
- [V] Oh et al. (2026) From Belief Entrenchment to Robust Reasoning in LLM Agents (DReaMAD) | https://arxiv.org/abs/2503.16814 | ids c19
- [V] Kim and Torr (2025) Single LLM Debate, MoLaCE: Mixture of Latent Concept Experts Against Confirmation Bias | https://arxiv.org/abs/2512.23518 | ids c20
- [V] Ke et al. (2024) Mitigating Cognitive Biases in Clinical Decision-Making Through Multi-Agent Conversations Using LLMs (JMIR) | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11615553/ | ids c21
- [M] Synthesis across c01-c21 (our reading) | internal | ids c22
- [M] Soll, Milkman, Payne (2015) A user's guide to debiasing (human background, from memory only) | https://onlinelibrary.wiley.com/doi/book/10.1002/9781118468333 | ids c23
- [M] Hills (2025) could-you-be-wrong follow-up prompt (search result only) | https://arxiv.org/html/2507.10124v1 | ids c24
- [V] Ma et al. (2025) Bias-free agent in LLM judging debate (search result only) | https://arxiv.org/abs/2505.19477 | ids c25, d14, d15
- [V] Kraishan (2026) and Sovrano et al. (2026) read together: sample size and unit of analysis (our reading) | https://arxiv.org/abs/2610.10049 | ids d01, d02, d03, d04, d20
- [V] Sovrano, Dominici, Bacchelli (2026) Mitigating Prompt-Induced Cognitive Biases in General-Purpose AI for Software Engineering (PROBE-SWE) (R | https://arxiv.org/abs/2604.16756 | ids d05, d06, d07
- [V] Hills (2025) Could you be wrong: Debiasing LLMs using a metacognitive prompt for improving human decision making | https://arxiv.org/abs/2507.10124 | ids d08
- [V] Kim, Kim, Park, Park, Breazeal, McDuff, Park (2025) InvThink: Premortem Reasoning for Safer Language Models | https://arxiv.org/abs/2510.01569 | ids d09
- [V] Bahaj, Rahimi, Chetouani, Ghogho (2025) Gauging Overprecision in LLMs: An Empirical Study | https://arxiv.org/abs/2504.12098 | ids d10, d11
- [V] Shen et al. (2026) RealICU: Do LLM Agents Understand Long-Context ICU Data? | https://arxiv.org/abs/2605.13542 | ids d12, d13
- [V] Martey, Shaw, Stromer-Galley, Kenski, Clegg, Folkestad, Saulnier, Strzalkowski (2014) Testing the Power of Game Lessons: The Effects of Art  | https://dl.digra.org/index.php/dl/article/view/631 | ids d16, d17
- [M] Dunbar et al. (2017) Mitigation of Cognitive Bias with a Serious Game (Int. J. Game-Based Learning) | https://doi.org/10.4018/ijgbl.2017100105 | ids d18
- [M] Anon. (2026) Investigating Anchoring Bias and Prompt-Based Mitigation in Large Language Models (Oxford J. of Student Scholarship, vol 10 iss | https://www.oxfordjss.org/aug-2026-vol-10-issue-3/investigating-anchoring-bias-and-prompt-based-mitigation-in-large-language-models | ids d19

Internal sources: SCHEMA.md and 00_FIELDS.md in this repository [V]; critique.md (re-opened Morewedge 2015, Sellier 2019, Mellers 2015, O Sullivan 2019, Echterhoff 2024, Lyu 2025, Lou and Sun 2024, Huang et al., Chhikara 2025, Knipper 2025) [V].
