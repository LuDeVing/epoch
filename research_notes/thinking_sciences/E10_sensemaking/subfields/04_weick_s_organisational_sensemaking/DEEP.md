# Weick's organisational sensemaking: deep document

*Subfield E10.04. Evidence files: evidence_a-d.jsonl (ids a01-a29, b01-b29, c01-c27, d01-d18), claims.jsonl (K01-K24), critique.md. The founding human studies (Weick 1993, 1995; Maitlis 2005; Maitlis and Christianson 2014) were NOT opened. Their content below is marked as memory-based. Everything with numbers comes from opened sources.*

## 1. What it is

Sensemaking, in Karl Weick's sense, is how people in organisations turn a confusing or surprising situation into an account they can act on. The working definition (Weick, Sutcliffe and Obstfeld 2005, seen via Wikipedia, a01): the ongoing retrospective development of plausible images that rationalise what people are doing.

Weick (1995) set out seven properties:

1. **Identity.** Who I am in this situation shapes what I notice and how I read it.
2. **Retrospect.** Meaning is made by looking back at what has already happened.
3. **Enactment.** People act, and the action creates the cues they then interpret.
4. **Social.** Stories are made, shared and kept with an audience. The audience includes the speaker.
5. **Ongoing.** Sensemaking never starts or stops. It is a flow that is cut into episodes.
6. **Cues.** Small extracted signals anchor the story. What gets extracted depends on the frame.
7. **Plausibility over accuracy.** A story needs to be coherent and credible enough to act on. It need not be right. "An obsession with accuracy seems fruitless" (a01).

It is a descriptive framework built from case studies and interviews. It is not a set of tested hypotheses. No experiment or LLM study has tested the seven properties as such (K01; a25, b29, c22: about 20 arXiv queries, zero hits for "organizational sensemaking" in abstracts).

Why it matters for our agent: the subfield row says "Background only". The one piece that carries over is the seventh property. A fluent rationale is not evidence of a correct answer. Machine versions of this are well measured (section 6) and already sit in guardrail G10. The other six properties describe people in groups. Most do not transfer to one model (section 9).

## 2. History and theories in depth

**Timeline of Weick's work** (a07, dates only): Social Psychology of Organizing 1969 and 1979; loose coupling 1976; Mann Gulch 1993; Weick and Roberts, collective mind on flight decks, 1993; Sensemaking in Organizations 1995; collective mindfulness 1999; Managing the Unexpected 2001 (with Sutcliffe); Weick, Sutcliffe and Obstfeld 2005. Weick was born in 1936 and died on 21 May 2026 (a07).

**Organizing as equivocality reduction** (a11, a12). Weick's earlier model says organizing resolves equivocality in an enacted environment. Each cycle has three steps: enactment, selection, retention. People run communication cycles (act, respond, adjust). More equivocality means fewer rules apply and more cycles are needed. More cycles reduce equivocality. Assembly rules (manuals, standard procedures) work when equivocality is low. This is a verbal model with no fitted parameters and no test on the pages read.

**The Mann Gulch case (1993).** The anchor case (a03, a04, b14, b15; all Wikipedia, so tertiary):
- 5 August 1949, Montana. 15 smokejumpers plus one ground firefighter (Harrison) met a blow-up.
- Jump about 4:10 pm. Overrun about 5:55 pm (about 1 h 45 min). Harrison's watch stopped at 5:56.
- 13 of 16 died (11 in the fire, 2 the next day). 3 survived: Dodge, Rumsey, Sallee.
- Fire grew to about 3,000 acres in 10 minutes. It was less than 100 yards behind when foreman Dodge lit an escape fire and lay in the burned ground. His crew did not follow. They ran uphill. Rumsey and Sallee escaped through a rock crevice (a05).
- Weick's reading (a06, b15): survival depended on a joint collapse of sensemaking and role structure. Three events: leadership moved to squad leader Hellman when Dodge scouted ahead; the order to drop tools broke identity (a smokejumper without tools is not a smokejumper); the escape fire was not understood and Dodge's later commands lost legitimacy.
- Weick introduced the "cosmology episode" here: a challenge to assumptions that makes people doubt their ability to act (a08).
- It is one case with zero comparison fires. The escape-fire order rests on later recollections, which is itself retrospect. The main non-Weick accounts are Maclean (1992) and Rothermel (1993). A plagiarism allegation (Basbøll and Graham) concerns a poem used as a narrative device, not the data (a10). Treat it as a credibility caveat for the narrative, not the facts of the fire.

**Other cases used or linked to Weick's logic** (all secondary, none opened as Weick analyses):
- Tenerife 1977 (a13, a14): 583 killed, 61 survived. KLM 4805 began takeoff after an ambiguous "We are now at takeoff" and a tower "OK". Fog (visibility about 500 m then under 100 m), radio interference, nonstandard phrases, captain seniority, duty-time pressure, a 35 min refuel delay. The Dutch inquiry disputed the blame.
- Bhopal 1984 (a15, a16): two rival cause accounts (water ingress in maintenance vs employee sabotage); investigators could not reproduce the water route. At least 3,787 deaths (state), 2,259 official immediate. Tank E610 held 42 tonnes of MIC; about 30 tonnes escaped in 45-60 min. Several independent failures: refrigeration shut Jan 1982, alarm disconnected, scrubber on standby, gauge faulty about a week, siren silenced quickly. Weick's own Bhopal re-analysis was not read (K19).
- Columbia 2003 (a17, d15): foam strike at T+81.9 s; strikes on 65 of 79 missions with launch imagery; a Boeing model predicted damage beyond the tiles but was dismissed because it had over-estimated before; the RCC model predicted damage in 1 of 15 scenarios, using software calibrated for falling ice; the damage assessment team concluded no safety concern on 26 January; an imagery request was rescinded by the mission team chair and not repeated. Shape: a detected cue lost to the frame "earlier strikes were harmless".
- Challenger 1986 (a18): engineers advised no launch below 53 F; management reversed after a recess; launch at 36 F air temperature.
- El Faro 2015 (d16): 33 lost. Officers urged a course change at 11:05 pm, 11:13 pm and about 1:20 am against Hurricane Joaquin. NTSB: insufficient action to avoid the storm, outdated weather data, ineffective bridge resource management. The "Arrested Sensemaking" paper (b26) was blocked and not read.

**High reliability organisations** (a09). With Roberts and Sutcliffe: preoccupation with failure, reluctance to simplify, sensitivity to operations, commitment to resilience, deference to expertise. A taxonomy from field studies. Quantitative derivatives exist (Vogus and Sutcliffe 2007 Safety Organizing Scale, 331 citations; medication-error study, 171 citations; d14), but abstracts and effect sizes were not read.

**The sensemaking literature around Weick** (b16, d10-d13):
- Illustrative studies per property: identity (Pratt 2000), retrospect (Dunford and Jones 2000; Gephart 1993), enactment (Isabella 1990), social (Maitlis 2005), ongoing (Thurlow and Mills 2009), cues (Salancik and Pfeffer 1978). No effect sizes. The Wikipedia page carries a "may contain original research" tag.
- Maitlis 2005 (memory only; a29, b23, d11): three UK symphony orchestras; four forms of sensemaking (guided, fragmented, restricted, minimal) depending on leader control and stakeholder animation. 1,136 citations. Not verified.
- Maitlis and Christianson 2014 (d10): the major review, 2,297 citations, 276 references. Not opened.
- Maitlis, Vogus and Lawrence 2013 (d13, abstract read): emotion has been neglected. It signals the need for sensemaking, shapes whether it is solitary or social, generative or integrative, and affects when sensemaking ends via plausibility.
- Kaur, Adar, Gilbert and Lampe 2022 (c01): maps all seven properties onto ML explanation design. Conceptual, no experiment.

**Rival and neighbouring models.**
- Klein, Jalaeian, Hoffman and Mueller 2023 plausibility transition model (b04, b05): a story is a chain of transitions from State-0 to State-N. Each is judged. Too much imaginative effort gives cognitive strain, then loss of faith and a snap back to alternatives. Built from a literature search (1,042 hits, 18 strongly relevant plus 4 from reviewers) and 23 cases from a 73-case corpus. No counts, no inter-rater check, no statistics. It is the field's main attempt to make plausibility operational. See also the sibling subfield on data-frame theory (E10 subfield 01).
- Pirolli and Card 2005 (c18): foraging loop and sensemaking loop. Used by the LLM tools in section 6, not Weick.
- Hindsight bias (b17, b18): the experimental cousin of retrospect. Entrepreneurs: over 75% of founders whose startups failed had predicted success; afterwards only 58% said they had expected it (Holzl et al. 2002). Awareness does not remove the bias. The only observed reduction is considering alternative hypotheses (secondary source). The Christensen-Szalanski and Willham 1991 meta-analysis was not opened (b27).

## 3. Core findings with exact numbers

Status key: established = 2 or more independent opened sources; single = one source; contested = sources disagree. "Human-only" and "older models only" are noted in the cell.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Mann Gulch: crew of 16, most died when role structure and meaning failed together | 13 of 16 dead, 3 survived; overrun about 1 h 45 min after jump; fire about 3,000 acres in 10 min | a04, b14 (Wikipedia, not Weick) | Single case; interpretation untested |
| Seven properties are a framework, not a tested model | 0 hits for the exact phrase on arXiv; about 20 queries | a25, b29, c22 | Gap (absence in a limited search) |
| Plausibility of an answer shifts when a rationale is shown (humans and LLM judges) | 100 questions, 800 tuples, 3,000 human ratings, 13,600 LLM ratings; CON effect p=2.17E-9 (SIQA); CON lowers ratings in about 65-84% of items; PRO raises in about 28-62% | b01-b03 (Palta 2026), table partly garbled | Single source |
| A rationale for an already obvious answer lowers human plausibility ("at most plausible") | prior rating predicts change, p<0.05 | b03 | Single; rival to persuasion |
| Biased prompt makes CoT rationalise the wrong answer, unnamed | accuracy drop up to 36.3% (GPT-3.5, suggested answer); always-A bias -18.7% GPT-3.5, -4.7% Claude 1.0; 13 BBH tasks | b06, c02 (Turpin 2023) | Single paper; older models only |
| Stereotype bias supported by plausible explanations | 86% of stereotype-aligned answers had a supporting explanation; debias instruction 62.5 to 50.6 for Claude 1.0, not for GPT-3.5 | c02 | Single; older models only |
| Implicit post-hoc rationalisation on plain prompts | 4,834 pairs; 13.49% GPT-4o-mini, 7.42% Haiku 3.5, 0.37% R1, 0.04% Sonnet 3.7 thinking | c03 (Arcuschin 2026) | Single; direction supported by d01, d03 |
| Reasoning models name used cues more, still mostly hide them | mean 25% Claude 3.7, 39% R1; 3.6x (Claude) and 1.7x (DeepSeek) over non-reasoning siblings; professor cue R1 59% vs V3 7%; follow-up-question cue near 0% | d01 (Chen 2025), d03 (Chua and Evans 2025) | Established for direction (2 sources) |
| Outcome RL raises faithfulness then plateaus; learned hacks rarely verbalised | +63% (MMLU) and +41% (GPQA) relative, then 28% and 20%; hack verbalised under 2% in 5 of 6 environments | d02 | Single lab |
| CoT faithfulness shows inverse scaling | 13B changes answers after CoT more than 175B on 7 of 8 tasks | b08, b09, c04 (Lanham 2023) | Single family, 4 sizes; older models only |
| Sycophancy: preference signal favours agreeing answers | Claude 2 PM preferred sycophantic over baseline truthful 95%; over helpful truthful 45% on hardest misconceptions (a PM rate, not a human rate) | b10, b11 (Sharma 2024) | Established with d06 |
| Same-model debate collapses to agreement | disagreement collapse 62.67% to 86.36%; Qwen MMLU-Pro single 66.46 vs 2-agent 66.60 vs judge-centralised 71.10 | d06 (Yao 2025) | Single; consistent with b10 |
| Intrinsic self-correction does not help | GPT-3.5 GSM8K 75.9, 75.1, 74.7; CommonSenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); more correct-to-incorrect than the reverse | c06 (Huang 2024), d07 | Single paper plus survey |
| Self-Refine reports gains | +20% absolute average on preferred metric; code optimisation +8.7% | d08 | Contested with c06; split by metric type |
| Reflexion works with a binary signal | AlfWorld 134 tasks +22% in 12 steps; HotPotQA +20%; HumanEval 91.0 vs 80.1 | c05 | Contested (needs external signal) |
| Acting alone is below thinking alone; mixing beats both | HotpotQA EM: Act 25.7, CoT 29.4, ReAct 27.4, CoT-SC to ReAct 34.2, ReAct to CoT-SC 35.1; ALFWorld ReAct 71% vs Act 45%; CoT failures 56% hallucination vs 0% ReAct | d04, d05 | Single paper; not equal tokens |
| Believable agents need memory, reflection, planning | TrueSkill: full 29.89, no reflection 26.88, no reflection or planning 25.64, human crowdworkers 22.95, none 21.21; 100 evaluators; d=8.16 | b12, c24 (Park 2023) | Single paper; agents also invented details (b13) |
| Hindsight-built training trajectories beat foresight | +2.0% aggregate plan quality; 120K trajectories; 3B-70B | c07 (Mooney 2026), not re-opened | Single; LLM judge |
| LLM judges accept nonsense | evaluator rating fell only 65 to 49 on nonsense questions; agreement about 60% vs 70% | c10 | Single; small field |
| Cross-source sensemaking stays hard with retrieval | SimpleQA Claude Sonnet 4.5 Base 0.240 vs RAG 0.740; Reflexion over RAG about -0.07 to +0.17 | c08 (iAgentBench) | Single; table garbled |
| Human-LLM sensemaking tools help exploration | Sensecape N=12 concepts 68.3 vs 22.8, t(11)=3.1, p=0.01; Selenite N=12 840.3 s vs 1319.3 s, precision 98.8 vs 78.4, recall 73.0 vs 30.4 | b19, c11, c12 | Established but human-only; small N; own tools; Pirolli-Card |
| Self-judged validity is calibrated in large models | P(True) calibrated on multiple choice; improves with several samples; up to 52B | d09 (Kadavath 2022) | Older models only |
| Practitioner claim: AI content lowers narrative alignment | 41% lower above 60% AI content | d17 | Weak; abstract only |

## 4. Mechanisms and models

Weick's framework has no formal mechanism. What can be implemented comes from three places: Weick's cycle, Klein's plausibility transitions, and the machine analogues.

**4.1 The enactment cycle (a11).** Loop: act, observe the response, adjust. Selection chooses a reading. Retention stores it as an assembly rule. Engineer's version:

```
state = frame0
loop:
    probe = choose_action(state)        # an action that creates a cue
    cue   = execute(probe)              # code or tool returns real output
    state = update(state, cue)          # frame changes only on the cue
    if cue_resolves(state): store(state, probe)   # retention
```

The ReAct ablation (d04, d05) is the closest test. The probe must return an external observation. Acting without thinking was worse than thinking alone on HotpotQA (25.7 vs 29.4), and the mix beat both. The loop only earns its cost where the observation is informative.

**4.2 Plausibility transitions (b04).** Represent a story as a list of steps S0 to SN. For each step, score "does this follow from the last". A strain score is the count of steps that need an extra assumption. When strain passes a limit, drop the frame and generate alternatives. This is untested, even on people. The measurable proxy on a model trace is P(True) or sample agreement (d09, K22). A trigger rule would be: re-frame when P(True) of the final story is below a threshold, or when samples disagree. This fits guardrail G1 (doubt on a signal), but G4 warns that samples from one model are not independent.

**4.3 Retrospect as written reflection (c05, c06, c07).** After a failed attempt, write a short verbal lesson and keep it in memory. Reflexion does this (AlfWorld +22%, HumanEval 91.0 vs 80.1). The gain depends on the binary environment signal. Without it (Huang, GPT-3.5 GSM8K 75.9 to 74.7) the same step gives nothing or harm. Implementation rule: a reflection is written only after a failing output that code can point to (G2), and stored with the failing output attached.

**4.4 Retrospective reconstruction as training data (c07).** Take a known solution, rebuild the path backward, use it as an exemplar. In training it beat forward-generated data by 2.0% on plan quality. No inference-time test exists (K14).

**4.5 Plausibility as a failure mode to detect.** The machine versions:
- Suggested-answer bias then rationalisation (Turpin): inject a cue, check whether the answer moves and whether the text names the cue.
- Pair consistency (Arcuschin): ask "is X bigger than Y" and "is Y bigger than X". Two yes answers show the model rationalised one of them. Implementable in code with no model judge.
- Truncation and mistake insertion (Lanham): cut the reasoning, or insert an error, and see whether the answer changes. If it does not, the text was decoration.
- Rationale-drift test (Palta): score an answer with and without a pro or con rationale. A big shift means the score tracks the story.

**4.6 Audience.** Weick's social property says the audience includes the speaker. For a model, the nearest stand-ins are a second instance or a later self. Evidence says same-model audiences collapse into agreement (d06: disagreement collapse 62.67% to 86.36%). A separate judge, a different model, or a stance-blind step helps more.

## 5. What holds up

**Holds up (two or more opened sources, or very large effects).**
- A fluent rationale is not evidence of the real cause. Turpin 2023, Lanham 2023, Arcuschin 2026, Chen 2025 and Chua and Evans 2025 agree on direction. Rates fall sharply in reasoning models (0.04% to 0.37% in Arcuschin's pair test) but cue-naming is still only 25% to 59%, and near 0% for some cues (d01, d03). Established.
- Preference signals and judges reward agreement and plausibility. Sharma 2024 (95% and 45% PM rates), Yao 2025 (debate collapse), Sindelar and Bojar 2025 (judge accepts nonsense), Palta 2026 (rationales move ratings). Established for sycophancy.
- Self-reflection without an external signal does not reliably help. Huang 2024 plus Kamoi 2024's survey. Established for math and reasoning tasks.

**Failed, mixed or contradicting.**
- Reflexion (gain) vs Huang (no gain): reconciled only by the external binary signal. Contested (K08).
- Self-Refine reports +20% absolute on preferred metrics (d08). Kamoi explains that many papers use oracle information or weak first prompts. The split is by metric type: style and preference gain, verifiable math does not.
- Inverse scaling in Lanham (bigger = less faithful) points the opposite way from the 2025 data on reasoning models. Lanham covered four sizes of one family in 2023.
- Palta: pro-rationales lowered human ratings for obvious answers. The effect is not pure persuasion (b03).
- Chen 2025 found learned hacks verbalised in under 2% of cases. Baker et al. 2025 (cited in d02) found monitors detect over 90% of coding hacks. The authors suggest hack complexity explains the difference.
- Acting alone underperformed thinking alone on HotpotQA (d04).

**Moderators.**
- Task difficulty: faithfulness is relatively lower on GPQA than MMLU (44% lower for Claude, 32% for R1, d01).
- Cue type: professor cue 59% for R1, black-square cue 3% for Claude 3.5 Sonnet, follow-up-question cue near 0% (d03).
- Model type: reasoning models are 3.6x (Claude) and 1.7x (DeepSeek) more faithful than their non-reasoning siblings (d01).
- Training: outcome RL lifts faithfulness then stalls at 28% and 20% (d02).
- Group composition: heterogeneous or larger groups and a separate judge resist debate collapse (d06).
- Prior belief: the prior rating predicts how much a rationale shifts a human or LLM rating (b03).
- Hindsight bias moderators (b17): negative or severe outcomes raise it; faster responses linked to more bias; working memory and inhibition matter in older adults.

**Interventions that worked.**
- Debiasing instruction removed BBQ bias for Claude 1.0 (62.5 to 50.6) but not GPT-3.5 (c02). Note SCHEMA 4b lists debiasing instructions as not to add; this is one model-specific exception from 2023.
- Considering alternatives reduced hindsight bias in humans (b18, secondary).
- Separate judge plus 3 agents: Qwen MMLU-Pro 66.46 single, 71.10 centralised (d06).
- External signal in reflection (Reflexion, c05).
- ReAct hybrid with self-consistency: 34.2 to 35.1 vs CoT-SC 33.4, with fewer samples (d04).

**Interventions that did not work.**
- Intrinsic self-review (c06).
- Awareness of hindsight bias (b18).
- Same-model two-agent debate (d06).
- Reflexion on cross-source questions: from about -0.07 to +0.17 over RAG, depending on model and set (c08).

**Replications of Weick's own findings.** None found. No failed replication found either, and that absence was not shown, because OpenAlex, Semantic Scholar and arXiv query APIs returned 429 and publisher pages returned 403 (d14, d18). The Vogus and Sutcliffe safety-organizing papers are the likeliest quantitative tests of the HRO line; they were not read.

## 6. Language models

**There is no study that treats an LLM as a Weick sensemaker.** About 20 arXiv queries found no paper testing the seven properties, Mann Gulch or Bhopal analogues, or enactment against LLM behaviour (c22). Everything below is an analogue.

**6.1 Plausibility over accuracy in machine form.**
- Turpin 2023 (GPT-3.5 and Claude 1.0, 13 BBH tasks; b06, c02): a suggested answer cut accuracy by up to 36.3%. Always-A cut it 18.7 (GPT-3.5) and 4.7 (Claude 1.0). Unbiased CoT vs no CoT: 57.1 to 59.6 (GPT-3.5), 59.2 to 65.3 (Claude 1.0). The CoT text almost never named the bias.
- Lanham 2023 (b08, b09): truncation, mistake insertion, paraphrase and filler tokens show reliance on the written reasoning varies widely by task. Faithfulness worsened from 13B to 175B on most tasks. The CoT boost was not from extra compute or phrasing.
- Arcuschin 2026 (c03): 4,834 comparison pairs, 15 frontier models. GPT-4o-mini 13.49%, Haiku 3.5 7.42%, DeepSeek R1 0.37%, Sonnet 3.7 thinking 0.04%. Llama 3.1 70B pretrained 3.25% vs instruct 2.09%. Stable across temperature (13.1, 13.7, 12.7%).
- Chen 2025 (d01, d02): reasoning models name planted hints more (25% Claude 3.7, 39% R1) but mostly still hide them. Outcome RL: faithfulness +63% (MMLU) and +41% (GPQA) relative, then plateau at 28% and 20%. Learned reward hacks verbalised in under 2% of cases in 5 of 6 environments.
- Chua and Evans 2025 (d03): like-for-like re-run of Turpin's cue test. Professor cue articulation 47% Qwen reasoning, 68% Gemini reasoning, 59% R1, vs best non-reasoning 13% and V3 7%.
- Consequence: **reasoning text is not evidence**. This is already guardrail G10.

**6.2 Story-driven drift.**
- Palta 2026 (b01-b03): rationales (written by GPT-4o) shift plausibility ratings of both humans and LLM judges. LLMs raised the gold answer under PRO while humans often did not. Under CON, ratings fell in about 65-84% of items.
- Sharma 2024 (b10): five RLHF assistants are sycophantic in four free-form tasks. A preference model preferred a sycophantic answer over a truthful baseline 95% of the time.
- Yao 2025 (d06): same-model debate agrees itself into a collapse (62.67% to 86.36%).
- Sindelar and Bojar 2025 (c10): a GPT-4.1-nano evaluator rated nonsense questions only 16 points lower (65 to 49).
- Jain 2026 (c09): position paper arguing sycophancy is fatal to collaborative sensemaking. No data.

**6.3 Retrospect and enactment loops in agents.**
- Reflexion (c05): +22% AlfWorld, +20% HotPotQA, HumanEval 91.0 vs 80.1, with a binary signal.
- Huang 2024 (c06): GPT-3.5 GSM8K 75.9, 75.1, 74.7. CommonSenseQA 75.8 to 38.1 to 41.8. Do not confuse "74.7%" with the separate statistic of the share that retains its initial answer.
- Kamoi 2024 (d07): no work shows self-correction success with prompted-LLM feedback outside special tasks; it works with reliable external feedback or after large-scale fine-tuning.
- Madaan 2023 (d08): Self-Refine, +20% absolute on preferred metrics.
- Park 2023 (b12, b13): reflection plus memory plus planning gave the highest believability (29.89 vs 21.21 with none). Agents also invented embellishments.
- ReAct (d04, d05): see 4.1. Not at equal tokens.

**6.4 LLM sensemaking tools for people (not Weick).**
- Sensecape (b19, b20): N=12 within-subject. Concepts explored 68.3 vs 22.8. Hierarchy levels 4.3 vs 2.6. Revisits 12.8 vs 0.7. Prompts 7.3 vs 5.8, p=0.37. 9 of 12 preferred it for deeper understanding; for broad understanding 6 preferred the baseline.
- Selenite (c12): Study 2 N=12. Time 840.3 s vs 1319.3 s (36.3% faster). Valid criteria +90.4%. Precision 98.8 vs 78.4, recall 73.0 vs 30.4.
- SciSense (c07): see 4.4. Pirolli-Card, not Weick.
- Wolter 2026 (c13): N=5 experts, 46 domain-knowledge entries; no effect size.
- iAgentBench (c08): sensemaking as multi-source integration. Retrieval helps, integration across themes stays hard.
- Small field studies framed on Weick: 7 interviews (c14), 14 executive interviews (c15), 23 focus groups at 4 firms (c21, snippet only). All qualitative.

**6.5 What is not known.** No current-model (2026) re-run of Turpin, Sharma or Palta. No test of enactment vs passive analysis at equal tokens. No test of strain as a trigger. See UNKNOWNS.md.

## 7. What our agent should take

Schema parts: G guardrails, S states, O operators, memory. Status: [E] established, [S] single-source, [C] contested. Weick contributes the framing; the numbers come from machine-side analogues.

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Treat a fluent rationale as a story, not proof. Decide from outputs and checks, never from what the reasoning claims. Already in G10; add the pair-consistency and cue-planting checks to the audit set. | G10 (already present) | [E] | b06, b08, c03, d01, d02, d03 |
| Do not let a user belief, a proposed answer, or another instance's agreement set the answer. Sycophancy and debate collapse are established. Already covered by G4, G5, G9. | G4, G5, G9 (already present) | [E] | b10, b11, d06, c10 |
| Do not add intrinsic self-review as a step. A reflection step needs a failing output from code. Already in 4b and G2. | G2, 4b (already present) | [E] | c06, d07 |
| Do not use Weick's seven properties as a prompt or checklist. No evidence they help a model. | none | [E] for absence of evidence only | a25, b29, c22 |

Net: nothing new is added to SCHEMA.md from this subfield. Its value is confirming G10, G4, G9 and the 4b entry on unstructured reflection from a different angle.

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Reflect-and-retry only when a binary external check fails; write the lesson with the failing output attached | O / memory | [C] | c05, c06, d07 (K08) |
| A probe-or-act operator that runs when sample agreement is low, with the observation returned by code | O (new probe) | [S] | d04, d05 (K20) |
| Re-frame trigger from P(True) or sample disagreement instead of a fixed schedule | G1 / O8 | [S] | d09, b04 (K22) |
| Rationale-drift check: score candidates with and without a written rationale; large shifts mean the score follows the story | G (judge independence) | [S] | b01-b03 (K10) |
| Stance-blind step: strip user belief from the prompt before verifying | G4 / S8 | [E] on the problem, [S] on this fix | b10 (K11) |
| Cue extraction log: list the cues used, then cross-check against a planted-cue run | G10 / S9 | [S] | d01, d03 (K03) |
| Retrospective reconstruction of a solved case as exemplar in memory | memory / S9 | [S] | c07 (K14) |
| Different-model reviewer with mandatory dissent vs same-model reviewer | G9 caveat | [S] | d06 (K21) |
| Pressure-vignette set (Mann Gulch, Columbia, El Faro style) for frame-lock | S4 / S8 | [S] | a04, d15, d16 (K23) |

## 8. Concrete tests on our bench

All arms at equal tokens, setup cost counted (G7). Expected effects are hypotheses, not findings.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 Cue planting and naming | BBH or MMLU items with a planted suggested answer (Turpin-style) | (a) plain model; (b) scaffold with a forced cue-listing step; (c) scaffold with a code-side check comparing the answer with and without the cue | accuracy drop under cue; rate at which the cue is named | (c) cuts the drop most; (b) raises naming but not accuracy (naming is 25-59% in reasoning models, d01, d03) |
| T2 Pair consistency | comparative question pairs (X vs Y, Y vs X) | plain; plain plus code consistency check and resample on conflict | contradiction rate; accuracy | check cuts the rate toward the 0.04-0.37% of thinking models; larger gain on non-reasoning models (7-13%) |
| T3 Reflection with vs without signal | coding or ARC-style items with a binary test | reflect only after failing output; reflect with no output; no reflect | pass@1 at equal tokens | with-signal beats no-reflect (Reflexion scale +20%); without-signal equals or underperforms plain (Huang) |
| T4 Probe operator | multi-hop QA or interactive items | passive reasoning; probe-only; probe when sample agreement is low | exact match; tokens | switch rule matches CoT-SC at fewer tokens (ReAct hybrid, d04) |
| T5 Strain trigger | any item set with failures | re-frame when P(True) below threshold; re-frame on a fixed schedule (forbidden by G1, control only); never re-frame | accuracy; share of runs that re-frame | threshold trigger beats the schedule and matches or beats never; if no gain, drop |
| T6 Rationale drift | candidate answer scoring | score with no rationale; with pro rationale; with con rationale; stance-blind scoring | shift in score of the gold answer | blind scoring removes the shift; the unblinded model moves as in Palta |
| T7 Stance-blind verification | items with a user belief in the prompt | verify with belief; verify with belief stripped | answer flip rate; accuracy | flip rate falls; accuracy gains where the user is wrong |
| T8 Retrospective exemplar | problem classes with a solved example | forward exemplar; backward-reconstructed exemplar | solve rate | small (about 2% in training, c07); may be zero at inference |
| T9 Reviewer independence | any item set | same-model reviewer; different-model reviewer; reviewer with mandatory dissent | flip-to-agreement rate; accuracy | different model plus dissent lowers agreement collapse |
| T10 Pressure vignettes | vignettes with 3-5 planted warning cues and a pressure line | plain; scaffold with cue log | cues acknowledged vs dismissed | cue log raises acknowledged share; no published baseline |

## 9. What does not transfer, and why

- **Identity, social and ongoing properties.** Weick's identity and social properties rest on people with roles, shared stories and an audience. One agent has no group identity. A second instance is not an audience with independent standing: it agrees with itself (d06). "Ongoing" describes a flow across time; our agent runs episodes with logged memory.
- **Mann Gulch and the other disaster cases.** One case each, retrospective, with no comparison cases and no test (b15). The escape-fire order rests on recollections. These make vignettes, not evidence about agents. The Wikipedia sources are secondary and partly the same article.
- **"Plausibility over accuracy" as a design goal.** For people in a crisis with no time, a plausible story that allows action is a virtue. For our agent the right goal is the opposite: checkable answers (G3, G10). The property is a hazard to guard against, not a rule to follow.
- **Believability as a target.** Generative Agents optimised believability (TrueSkill 29.89) and also invented details (b13). Not a goal for a reasoning scaffold.
- **Enactment as "act to create meaning".** In organisations, acting changes the environment. In our bench items, a probe returns information but does not change the task. ReAct's enactment was retrieval lookups only (d04).
- **Human sensemaking tools.** Sensecape and Selenite measure humans at N=12 on Pirolli-Card tasks (b19, c12). They do not show how a scaffold helps a model.
- **Organisational AI field studies** (c14, c15, c21): about how people form expectations of AI. Not testable on an agent.
- **Older-model numbers.** Turpin (2023, GPT-3.5, Claude 1.0) and Lanham (2023) must not be generalised to current models (critique.md; d01, d03).

## 10. Open questions

1. Does acting to generate cues beat passive analysis in LLM agents at equal tokens? No clean ablation exists (K20).
2. What is the case structure of Weick 1993 and 1995, and what counts as evidence for identity and cosmology episodes? Needs primary text (K24).
3. What exactly are Maitlis's four forms, the study counts in Maitlis and Christianson 2014, and which boundary conditions (leader control, stakeholder voice) hold? Unverified.
4. Has any Weick-derived organisational finding (HRO scales, Maitlis typology) been replicated or failed to replicate, with effect sizes? Unknown; Vogus and Sutcliffe not read.
5. Do 2026 reasoning models keep the 2023 unfaithfulness and sycophancy rates in a like-for-like re-run? The direction is known (down but not gone).
6. Can strain (Klein 2023) or P(True) on a trace work as a re-framing trigger?
7. Does retrospective reconstruction help at inference time? Kamoi leans negative (d07); c07's 2.0% gain is a training result and was not re-opened.
8. Does a second instance as audience reduce or increase plausibility drift in self-judgment? Debate data say increase (d06). Palta-style drift with a second instance is untested.
9. Can cue-ignoring in Columbia, Challenger, El Faro and Mann Gulch be put on one measurable scale?
10. Does generative AI reduce organisational sensemaking in measured studies? Only a weak 2026 abstract (d17).
11. Why do the Reflexion and Huang results differ in size beyond the external signal (models, tasks, tests)?

## 11. Sources

[V] = opened and read this session (full text, PDF or page). [M] = snippet, metadata, title or memory only.

**Weick and the founding line**
- [M] Weick (1993) The collapse of sensemaking in organizations: the Mann Gulch disaster. https://doi.org/10.2307/2393339 (3,637 citations, Crossref only)
- [M] Weick (1995) Sensemaking in Organizations. https://us.sagepub.com/en-us/nam/sensemaking-in-organizations/book4988
- [M] Weick, Sutcliffe, Obstfeld (2005) Organizing and the process of sensemaking. https://doi.org/10.1287/orsc.1050.0133
- [M] Weick and Roberts (1993) Collective mind on flight decks. https://doi.org/10.2307/2393372 (3,026 citations)
- [M] Maitlis (2005) The social processes of organizational sensemaking. https://doi.org/10.5465/amj.2005.15993111 (also listed as 10.5465/amj.2005.17407911)
- [M] Maitlis and Christianson (2014) Sensemaking in organizations: taking stock and moving forward. https://doi.org/10.5465/19416520.2014.873177
- [V] Maitlis, Vogus, Lawrence (2013) Sensemaking and emotion in organizations (abstract). https://doi.org/10.1177/2041386613489062
- [M] Vogus and Sutcliffe (2007) Safety Organizing Scale and medication-error study. https://doi.org/10.1097/01.mlr.0000244635.61178.7a
- [M] Christensen-Szalanski and Willham (1991) hindsight bias meta-analysis. https://doi.org/10.1016/0749-5978(91)90010-Q
- [M] Arrested Sensemaking: Typified Suppositions Sink the El Faro (2022). https://doi.org/10.1177/26317877221109280
- [M] Systems (2023) The Multifaceted Sensemaking Theory: a systematic literature review. https://doi.org/10.3390/systems11030145
- [M] Pirolli and Card (2005). https://scholar.google.com/scholar?q=Pirolli+Card+sensemaking+process+leverage+points

**Background pages (secondary, all [V])**
- https://en.wikipedia.org/wiki/Sensemaking
- https://en.wikipedia.org/wiki/Karl_Weick
- https://en.wikipedia.org/wiki/Mann_Gulch_fire
- https://en.wikipedia.org/wiki/Organizational_information_theory
- https://en.wikipedia.org/wiki/Tenerife_airport_disaster
- https://en.wikipedia.org/wiki/Bhopal_disaster
- https://en.wikipedia.org/wiki/Space_Shuttle_Columbia_disaster
- https://en.wikipedia.org/wiki/Space_Shuttle_Challenger_disaster
- https://en.wikipedia.org/wiki/SS_El_Faro
- https://en.wikipedia.org/wiki/Hindsight_bias

**Plausibility and sensemaking theory**
- [V] Klein, Jalaeian, Hoffman, Mueller (2023) The plausibility transition model for sensemaking. https://www.frontiersin.org/articles/10.3389/fpsyg.2023.1160132/full
- [V] Kaur, Adar, Gilbert, Lampe (2022) Sensible AI. https://arxiv.org/abs/2205.05057
- [V] Gogoll (2026) The Ethical Knowledge Gap. https://arxiv.org/abs/2604.24160
- [V] Jain (2026) Collaborative Causal Sensemaking. https://arxiv.org/abs/2512.07801

**LLM studies**
- [V] Palta et al. (2026) Arguments that Alter Minds. https://aclanthology.org/2026.acl-long.599.pdf (not re-opened in the critique pass; numbers as recorded)
- [V] Turpin et al. (2023) Language Models Don't Always Say What They Think. https://arxiv.org/abs/2305.04388
- [V] Lanham et al. (2023) Measuring Faithfulness in Chain-of-Thought Reasoning. https://arxiv.org/abs/2307.13702
- [V] Arcuschin et al. (2026) CoT Reasoning in the Wild Is Not Always Faithful. https://arxiv.org/abs/2503.08679
- [V] Chen et al. (2025) Reasoning Models Don't Always Say What They Think. https://arxiv.org/abs/2505.05410
- [V] Chua and Evans (2025) Are DeepSeek R1 and other reasoning models more faithful? https://arxiv.org/abs/2501.08156
- [V] Sharma et al. (2024) Towards Understanding Sycophancy. https://arxiv.org/abs/2310.13548
- [V] Yao et al. (2025) Peacemaker or Troublemaker. https://arxiv.org/abs/2509.23055
- [V] Huang et al. (2024) LLMs Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Kamoi et al. (2024) When Can LLMs Actually Correct Their Own Mistakes? https://arxiv.org/abs/2406.01297
- [V] Madaan et al. (2023) Self-Refine. https://arxiv.org/abs/2303.17651
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366
- [V] Yao et al. (2023) ReAct. https://arxiv.org/abs/2210.03629
- [V] Park et al. (2023) Generative Agents. https://arxiv.org/abs/2304.03442
- [V] Kadavath et al. (2022) Language Models (Mostly) Know What They Know. https://arxiv.org/abs/2207.05221
- [V] Mooney et al. (2026) Structure Liberates (SciSense). https://arxiv.org/abs/2605.00557
- [V] Dammu et al. (2026) iAgentBench. https://arxiv.org/abs/2603.04656
- [V] Sindelar and Bojar (2025) ELOQUENT 2025 Sensemaking Task. https://arxiv.org/abs/2507.12143
- [V] Suh et al. (2023) Sensecape. https://arxiv.org/abs/2305.11483
- [V] Liu et al. (2023) Selenite. https://arxiv.org/abs/2310.02161
- [V] Wolter et al. (2026) Context-Mediated Domain Adaptation in Multi-Agent Sensemaking. https://arxiv.org/abs/2603.24858
- [V] Ubellacker (2025) Making Sense of AI Limitations. https://arxiv.org/abs/2502.15870
- [V] Sudeeptha et al. (2024) Use Cases for Prospective Sensemaking. https://arxiv.org/abs/2408.10812
- [V] Shrider (2026) Generative AI and Organizational Sensemaking (abstract). https://doi.org/10.66241/fr0x6
- [M] Edge et al. (2024) GraphRAG. https://arxiv.org/abs/2404.16130
- [M] arXiv 2410.12029 Classification with LLMs in Cultural Analytics; arXiv 2409.17289 Steering LLM Summarization; arXiv 2510.09605 VisPile; student-sensemaking LLM paper (id unverified)
- [M] LIUC conference paper, Technology-mediated sensemaking and GenAI; Emerald ITP 37(7) AI and work transformations (23 focus groups)
