# Premortem and prospective hindsight: deep document

*Subfield E12.05. Written from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01, b16, d10 ...) point to those files. The short version: the premortem is a popular method with a thin evidence base. It reliably makes people less confident and makes them list more failure reasons. It has not been shown to improve plan outcomes. No prompt-only LLM test on reasoning accuracy exists.*

## 1. What it is

A premortem asks a team to assume that a plan has already failed, and then to explain why. Gary Klein popularised it in 2007 (HBR). The idea comes from "prospective hindsight": explaining an event as if it had already happened. Mitchell, Russo and Pennington named and studied this in 1989.

The procedure (Klein 2021, a06):
- Brief the plan.
- Say: a crystal ball shows the plan failed.
- Two minutes of silent individual writing.
- Round-robin: one reason each, leader first.
- Later additions: a short step to propose actions against the top reasons.
- A session takes 20 to 30 minutes.

Klein's stated aim is social: make it safe for knowledgeable people to voice doubts (a05, a08). The cognitive claim is different: certainty of failure makes people retrieve more concrete, episodic causes.

Three things are often mixed up in the literature. We keep them apart:
1. **Failure frame**: the assumed outcome is failure, not success.
2. **Certainty frame**: the outcome is stated as having happened, not as possible.
3. **Safe dissent**: the group procedure lets people speak up.

Only the first two can apply to a single LLM agent. The third has no meaning for one agent (see section 9).

Why we care: our schema fires doubt only on a signal (G1) and revises only from real output (G2). A premortem is a doubt-generating step. The question is whether it is a useful operator at an impasse (S6), a way to find test cases for S4/S8, or a thing we should not add (section 4b of SCHEMA already rejects unstructured self-reflection and bias checklists).

## 2. History and theories in depth

**Fischhoff 1975, hindsight bias (a09, a15, a16).** Give people a story with four possible outcomes and tell them one is true. They rate the told outcome as more likely than people who judge in foresight. Over 150 articles and two meta-analyses followed. Guilbault et al. 2004 (secondary snippet, a18): 95 studies, 252 effect sizes, mean d = 0.39 (95% CI .36 to .42); debiasing manipulations had no significant effect. The premortem turns this bias into a tool: a known outcome makes causes feel easy to find.

**Koriat, Lichtenstein, Fischhoff 1980 (a19, a20).** The key precursor. Subjects answered general-knowledge questions with confidence. Writing reasons for and against improved calibration (Exp 1, 68 analysed, within subject, control always first). In Exp 2 (200 volunteers, 66 per group) only a contradicting reason improved calibration; supporting reasons did nothing. Writers found one contradicting reason hardest to produce (18.3 reasons for vs 13.4 against, t(61) = 7.99). Fischhoff and Macgregor (1982) reportedly failed to replicate (a22, no numbers).

**Mitchell, Russo, Pennington 1989 (a01, a13, d03).** Two experiments crossed time direction (future vs past) with outcome certainty (sure vs uncertain). The abstract says time direction had little effect in Exp 1. Outcome certainty drove longer, more episodic, past-tense explanations. Exp 2: uncertainty changes the kind of explanation. The paper tested no plan and no premortem. The famous "+30% more reasons" is not in the abstract. It is quoted second-hand by Veinott 2010 (a12) and a review page (a02, b07). The same page says reason quality was not assessed and that Klein 2007 restated "30% more reasons" as "30% better identification of correct reasons" (K02). A 2025 review repeats that restatement (b08). We never saw N or the test statistic. Treat the 30% as unverified.

**Klein 2007 (a05).** Practitioner article. No outcome data on the open summary page.

**Arkes, Faust, Guilmette, Hart 1988 (a21).** Neuropsychologists (194 of 480 returned). Hindsight bias in 42 of 72 (58%) vs 28 of 68 (41%) when asked to write a reason each alternative could be right; chi2(1, N=140) = 4.12, p < .05. This is the "consider the alternative" debiaser. Fischhoff's earlier warnings had little effect (a17).

**Veinott, Klein, Wiggins 2010 (a10, a11, a12).** The only controlled test of the premortem as Klein defined it. Numbers in section 3.

**Sanna and Schwarz 2004 (a23); Schwarz et al. 2007 (a24).** Metacognitive ease. Listing 3 failure thoughts (easy) pushed judgments the failure way. Listing 12 failure thoughts (hard) acted like success thoughts, because generating them felt difficult. "Consider the opposite" backfires when it feels hard. This is the main published boundary condition: more failure causes can make people less pessimistic, not more.

**Sieck, Merkle, Van Zandt 2007 (a25, a26).** The ASC model: people use the favoured option as a retrieval cue and build a supporting explanation, which causes overconfidence. Assuming each option true and explaining why ("explain, independent") cut overconfidence further, and drifted into underconfidence for hard foils (d for foil plausibility 0.031, 0.126, 0.404 across conditions). Retrieving reasons against the favourite is hard, so plain listing can fail.

**Hill 2012 (d04, d05).** Often cited as premortem evidence. It is not. It tests support-theory unpacking with 32 search planners: listing the scenarios in which a lost person left the area raised that probability (F(1,28) = 4.753, p = .038). Only 11 of 32 showed the effect. It is a rival mechanism: listing any scenario set inflates its probability.

**Applied work, 2016 to 2026.** Gallop and Bischoff 2016 (b06, d19); Peabody 2017 thesis (a14, b01-b03, d09); Gilmartin 2019 (b09); Beidas 2022 (b10); Roose, Lehman, Veinott 2023 (d07); Wippold 2024 (b11); Kannan 2026 (b04). All small, mostly qualitative, few with controls.

**Backward planning (Park, Lu, Hedgcock 2017, d06).** A relative: planning backward from the goal beat forward planning on motivation and performance, mainly for complex goals. No numbers read; a corrigendum exists.

**LLM era.** InvThink 2025-26 (a27, d10-d12) calls itself premortem reasoning but lists harms before answering. AUGUR (d13) is a trained pre-mortem method. Veinott and Lehman 2024 (d01) compare students and ChatGPT-4. See section 6.

## 3. Core findings with exact numbers

Status: **established** (two or more independent sources), **single-source**, **contested**, **second-hand** (number not checked in the primary).

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Failure-imagined premortem cut plan confidence about twice as much as pros/cons or cons-only | N=178 students, 5 conditions. Change in confidence: premortem -25.0 points, pro-con -14.0, cons-only -12.4, critique and baseline about 0. Condition F(5,173)=30.88, p<.0001. Premortem vs pro-con t(74)=-7.08; vs cons-only t(67)=-8.42. Pilot plan confidence 67%. | Veinott 2010 (a10, a11) | single-source (only controlled test); confidence is not plan quality |
| After fixes, premortem confidence recovered most | Time2 to Time3 F=72.54 (as printed), p<.0001; premortem vs pro-con t(74)=-4.42. Recovery may be regression from the lowest point. | Veinott 2010 (a11) | single-source |
| Subjective understanding of the plan rose | Omnibus F(5,173)=1.92 n.s.; premortem t(74)=1.97, p<.05 only vs baseline, not vs critique | Veinott 2010 (a11) | single-source, weak |
| Certain outcome gives longer, more episodic explanations; time direction matters little | Abstract only; no N or statistics read | Mitchell 1989 (a01, d03) | single-source (abstract) |
| "About 30% more reasons" | Not in the abstract. N and test unknown. | Mitchell 1989 via Veinott 2010 (a02, a12, b07) | contested, second-hand |
| "30% better identification of correct reasons" | A restatement error of the above; repeated in a 2025 review | Klein 2007; review (b07, b08) | established as an error (K02) |
| Premortem beat brainstorming on risk quality, plan changes and black-swan finds | N=101, teams of 4-6, 45 min, blind panel, quality = score above 70 on two scales. No effect sizes seen. | Gallop and Bischoff 2016 (b06, d19) | single-source, second-hand |
| Cadet field test: fewer fouls, less fixation vs standard check | N=52 cadets, 6 exercises (3 premortem, 3 standard); no change in planning or execution time; no statistics seen | Peabody (a14, b01, d09) | single-source, thesis, abstract only |
| Premortem vs worst-case: equal counts for familiar plans, more reasons for complex unfamiliar plans | Exp 2 N=72 no difference in counts, categories differed. Exp 3 N=82 premortem more reasons; groups more solutions than individuals | Peabody (b02, b03) | single-source |
| Game teams found many causes but few revised plans | 10 teams, n=68; mean 17.8 failure reasons and 16.7 mitigations per team; no control | Roose 2023 (d07) | single-source |
| Brainwriting premortem is quick | 116 staff, 10 sessions, 364 ideas, 217 unique, 93 agreed; brainwriting about 10 min; no control | Gilmartin 2019 (b09) | single-source, uncontrolled |
| No formal outcome evidence for the premortem | Reviews say never evaluated or no evidence found | b09, b13, b10, a07, a08 | established |
| Hill 2012 is not premortem evidence | N=32, F(1,28)=4.753, p=.038, 11 of 32 showed effect | d04, d05 | established (as a correction) |
| Listing 3 failure thoughts shifts judgment; 12 does not | N=227; 12-condition mean 9.9 thoughts vs 3.0; planning fallacy contrast t(207)=8.38; hindsight t(207)=4.83 | Sanna and Schwarz 2004 (a23) | single-source, human |
| Contradicting reasons improve calibration, supporting ones do not | Exp 2: 200 volunteers, 66 per group | Koriat 1980 (a20) | contested (Fischhoff and Macgregor 1982 failed to replicate; no numbers) |
| Hindsight bias is real; debiasing mostly fails | d=0.39 (95% CI .36-.42), 95 studies, 252 effects; debiasing no significant effect | Guilbault 2004 (a18, snippet) | established |
| Considering how the other outcome could be true cuts hindsight bias | 58% vs 41% biased, N=140, chi2=4.12 | Arkes 1988 (a21) | established (a09, a17, a21, b14) |
| Intrinsic self-correction hurts reasoning | GPT-3.5 CommonsenseQA 75.8 to 38.1 (round 1), 41.8 (round 2); GSM8K 75.9/75.1/74.7; GPT-4 GSM8K 95.5 to 91.5 (round-2 value 89.0 unconfirmed) | Huang 2024 (b16, c01, c02) | established |
| With oracle labels the same loop looks good | GPT-3.5 GSM8K/CSQA/HotpotQA 75.9/75.8/26.0 to 84.3/89.7/29.0; GPT-4 95.5/82.0/49.0 to 97.5/85.5/59.0 | c01 | established |
| LLMs find reasoning errors poorly but fix them well | BIG-Bench Mistake, 2186 chains, 5 tasks; GPT-4 52.87% overall; gold location +18 to +44 points on wrong traces, 0 to -11 on right ones (the +18 to +44 not re-opened) | Tyen 2024 (b17, c04, c05) | established |
| Reflection helps when told the answer failed | Reflexion HumanEval 91% vs 80%; Renze GPT-4 re-asked accuracy: baseline 0.786, Retry 0.827, Explanation 0.876, Solution 0.925, Composite 0.932 | b18, b19, c09, c10 | established |
| Tool-verified critique beats own-opinion critique | CRITIC +7.7 F1 on QA, +7.0 points on math; without the interpreter, -1.8 on one math task; about 12% of GPT-4 plans executable alone | c07, c16, b20 | established |
| Draft-hidden verification works best | CoVe FACTSCORE 55.9 (few-shot), 60.8 joint, 63.7 factored, 71.4 factor+revise | Dhuliawala 2023 (c11) | single-source (plus Weng +2.33% backward check, c12) |
| Failure attribution after the fact is hard for LLMs | Who&When: best 53.5% agent, 14.2% step (127 systems); MAST kappa 0.88 humans, 1600+ traces, 14 modes | c17, c18, b22, b23 | established |
| Machine red teaming scales but loses diversity | 0.5M zero-shot cases, 3.7% offensive replies; RL red LM over 40% but 78% of its cases contained one word | Perez 2022 (c20) | single-source |
| Structured failure-first prompt beat plain safety prompt | TRIDENT harmfulness 3.22 zero-shot, 2.62 safety prompt, 2.19 InvThink (1-5, lower is better, LLM judges) | InvThink (d10, a27) | single-source, safety task |
| Failure vs success direction made no difference | Qwen-2.5-7B SFT, 23,063 targets; safety rate 1.000 both; harmfulness 1.23 vs 1.01 | InvThink B.2 (d11) | contested (both arms at ceiling) |
| Trained pre-mortem methods raise math accuracy | AUGUR +5.01, +4.28, +5.66 over GRPO; InvThink Qwen3-8B average 0.61 base to 0.63 SFT+RL, single seed | d12, d13 | single-source, training not prompting |
| Self-labelled "verified" gives no benefit; audited gives a gain | 1,330 runs, nine models; audited gate +0.114 [0.019, 0.208], n=55 paired | d17 | single-source, indirect |
| What-if failure prompts feel helpful but do not measure better | N=214 main study | Ghosh 2026 (d15) | single-source |
| Forward world-model simulation helps agents | VisualWebArena +34.1% relative; Online-Mind2Web +42.3%; Mind2Web-Live +23.8% | Gu 2025 (c19) | single-source |

## 4. Mechanisms and models

Seven candidate mechanisms. Each is written so it can be turned into a prompt or a program step.

**M1. Certainty frame raises retrieval of concrete causes (Mitchell 1989).**
Mechanism: when an outcome is stated as fact, the person builds a causal story from episodic memory, not a probability judgment.
Implementation: put the failure into the prompt as a stated fact ("the final answer was checked and is wrong") and ask for causes. Compare against "list risks".
Evidence: a01, d03. Count effect only; no quality measure.

**M2. Failure focus lowers confidence (Veinott 2010).**
Mechanism: attending to failure reasons lowers stated confidence. Veinott read the half-sized drops of pro-con and cons-only as showing that both failure focus and certainty contribute (a12).
Implementation: elicit confidence before and after the failure list. For an LLM, use sampled agreement or P(True) (c21), not stated words (SCHEMA 4b: verbal confidence is not a stop rule).
Caveat: confidence is the outcome, not accuracy. A drop is useful only if it tracks real error.

**M3. Counter-evidence retrieval (Koriat 1980, Sieck 2007).**
Mechanism: confidence follows the amount and strength of evidence for the chosen answer. Forcing reasons against the choice removes one-sided retrieval. The ASC model says the favoured option acts as a retrieval cue, so it must stop being the cue.
Implementation: for each candidate answer, in a fresh context, assume it is the true one and explain why ("explain, independent"), then do the same for each rival. Compare strength. Same shape as Sieck's best arm.

**M4. Metacognitive ease reversal (Sanna and Schwarz 2004).**
Mechanism: the felt ease of generation, not the content, sets the effect. 3 failure thoughts shift judgment; 12 reverse it.
Implementation: cap the number of failure causes requested (3 to 5). Do not ask for 12. An LLM has no clear analogue of felt ease; test the cap anyway.

**M5. Unpacking (Hill 2012, support theory).**
Mechanism: listing any scenario set raises its judged probability, so a long failure list can inflate the probability of failure without new information.
Implementation: do not read the model's probability of failure after a long list as evidence. Use a code check.

**M6. Safe dissent (Klein).**
A social mechanism. Not tested separately (b12 poster: forward "promortem" differed in Exp 1, not in Exp 2). Not implementable for one agent.

**M7. Acting on causes (Roose 2023).**
Finding causes is cheap; revising the plan is the weak link. Implementation: after listing, force a revision step and score whether the plan changed.

**Engineer's recipe for an agent premortem step.** A candidate, not part of the schema.
1. Input: current best attempt A and the task.
2. Fresh context, state: "A was run on a fresh input and gave a wrong result." Ask for 3 to 5 distinct causes, each as a testable claim ("fails when X").
3. Code turns each claim into a test input or mutated input. Run A. To follow CoVe (c11), turn each cause into a check question answered without A in view where possible.
4. Keep only causes confirmed by a run (K13, K28). Discard the rest before the reviser sees them.
5. Show confirmed failing outputs to the reviser (S5), per G2.
Control arms: plain "list risks" (no failure assumption), Retry ("your answer was wrong"), forward success scenario, and extra independent attempts at equal tokens.

## 5. What holds up

**Holds up (established):**
- Confidence drops after a failure frame in humans (Veinott N=178; one study, but a large gap: -25 vs -14 vs -12.4).
- Hindsight bias exists; most debiasing fails; "how could the other outcome be true" is the one reliable exception (a09, a17, a18, a21, b14).
- Nobody has measured plan outcomes at scale (K07).
- LLM intrinsic self-correction does not help reasoning and often hurts (K10).
- LLMs locate errors poorly and fix them well once told where (K11).
- External or tool verification is what makes critique work (K13).

**Failures and corrections:**
- Fischhoff and Macgregor 1982 failed to replicate Koriat 1980 (a22; no numbers).
- The 30% claim is not in the Mitchell abstract; Klein's restatement as quality is wrong (K01, K02).
- Hill 2012 is not a premortem study (K22). Reviews citing it for reduced overconfidence are wrong.
- Zhang 2023 (N=622) is not a premortem study (d08).
- Student poster: forward vs backward framing differed in Exp 1 but not Exp 2 (b12; no N seen).
- The only LLM direction control (InvThink inverse vs forward SFT) was a null at ceiling (d11).
- Self-Refine's +20% is for style tasks (sentiment 3.8 to 36.2; readability 15.0 to 45.0); math 0 gain, code optimisation +0.2 (c08). Huang and Kamoi found no gain on verifiable reasoning (K15).

**Moderators and boundary conditions:**
- Number of causes requested: 3 helps, 12 reverses (a23).
- Plan complexity and familiarity: Peabody Exp 3 (complex, unfamiliar) saw more reasons than worst-case; Exp 2 (familiar) did not (b02, b03). Park 2017: backward planning helps mostly for complex goals (d06).
- Individual vs group: all arms wrote individually first in Veinott, which inflates rivals (a10).
- Rival method: worst-case is close; the premortem's edge over it is about content category, not count (a14).
- Retrieval difficulty: reasons against the favourite are hardest to produce (a20, a26).

**Interventions that worked (human):**
- Contradicting-reason writing (Koriat Exp 2, contested).
- Assume-each-option-true explanation (Sieck 2007).
- Failure frame for confidence (Veinott).
- Brainwriting for speed (Gilmartin 2019, uncontrolled).

**Interventions that did not work or were not shown:**
- Warnings against hindsight bias (a17).
- Pros/cons and cons-only as confidence reducers (about half the effect, a10).
- Forcing many (12) failure thoughts (a23).
- Combining a what-if prompt with an assumptions check: may hurt (d15, single-source).
- Acting on premortem output in game teams (d07).

## 6. Language models

**No prompt-only LLM test of a true premortem on reasoning accuracy was found** (b25, c23, d18). Searches covered Crossref, arXiv, Semantic Scholar and OpenAlex as available. Some sources were blocked (Springer, Sage, preprints.org; arXiv API 429). Treat this as "not found", not "does not exist".

**Direct premortem studies of LLMs:**
- *Veinott and Lehman 2024* (d01, d02): ChatGPT-4 failure reasons compared qualitatively with student reasons for the same plan. HCII 2024 Late Breaking Papers, pp. 256-268, 38 references. Abstract read; no results; Springer behind a login wall. Unknown whether LLM causes matched human ones.
- *InvThink* (a27, d10-d12): list harms, analyse consequences, answer under constraints. Safety task, LLM-judged.
  - TRIDENT harmfulness (1-5, lower better): zero-shot 3.22, safety prompt 2.62, InvThink 2.19. That is 32% below zero-shot and 16% below the safety prompt. SafetyBench gain about 5 to 13%; Illegal Activities +15.8% (N=1,767).
  - Agentic scenarios: blackmail rates down 90%, murder attempts down 44%.
  - Frontier Claude and GPT models sat at 70 to 75% whatever the method (a27).
  - It lists harms before answering. It does not assume failure happened, so it is not Klein's certainty frame. There is no baseline that asks for risks without a failure assumption.
  - Direction control (d11): inverse vs forward SFT, same tokens. Safety rate 1.000 both. Harmfulness 1.23 vs 1.01. Both collapsed to refusal (XSTest false-refusal 0.980 both). Low power.
  - Reasoning (d12), Qwen3-8B average over GPQA, MATH500, ARC-C, MMLU: base 0.61, general SFT 0.56, InvThink SFT 0.61, RL 0.60, SFT+RL 0.63. MATH500 0.50 to 0.55; GPQA 0.46 to 0.51. Single seed. Trained, not prompted.
- *AUGUR* (d13, preprint): pre-mortem reasoning trained with failure-aware SFT plus GRPO. Average accuracy over GRPO: +5.01 (Qwen2.5-7B-Instruct), +4.28 (Llama-3.1-8B-Instruct), +5.66 (Qwen3-4B-Base). Abstract only.
- *Scott 2025* (a29): AI-assisted prospective reflection tool, 18 participants. A probe study; no accuracy result.
- *Ghosh 2026* (d15): humans reviewing GPT-4o plans with seeded errors. N=214 main study (groups of 60, 45, 50, 59). An "Assumptions" check cut overreliance without raising load. A "WhatIf" failure prompt was rated more helpful but did not measure better; combining both may hurt.
- *Name collision*: "Prospective Hindsight", arXiv 2610.02740 (a30, b15, d14), is an RL training signal (prediction before feedback vs evaluation after). Not a premortem.

**Close relatives with measured results:**
- Self-correction without feedback hurts: GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5. Right answers were flipped to wrong more often than the reverse (c02: GPT-3.5 kept its first GSM8K answer 74.7% of the time).
- With an oracle label, gains: GPT-4 HotpotQA 49.0 to 59.0 (c01). The oracle is the leak.
- Error finding: GPT-4 52.87% (c04). A random location helped wrong traces but cost right ones (c05).
- Reflection with a failure signal: Renze GPT-4 0.786 to 0.827 with Retry alone, 0.932 with a composite reflection (c10). So "Retry" is the baseline any premortem must beat. Part of any premortem gain may be only "you were wrong, try again".
- Tools: CRITIC +7.7 F1 (c07). About 12% of GPT-4 plans executable alone (c16).
- Draft-hidden verification: CoVe 55.9 to 71.4 FACTSCORE (c11). Backward answer check +2.33% (c12).
- Forward simulation: +34.1% relative on VisualWebArena (c19). Reverse-thinking training +13.53% (c13).
- Critic help: humans found about 50% more flaws (c14); CriticGPT preferred 63% and 80% of the time but hallucinated and nitpicked (c15).
- Failure attribution after the fact: 53.5% agent, 14.2% step (c17). Prospective causal generation is probably harder (an inference).
- Machine-generated test cases lose diversity (c20).
- Models can estimate P(True) for their own answers (c21), so confidence shift is measurable. No premortem study measured it (d18).

**Summary:** a failure-frame prompt has one positive safety result, one null direction control at ceiling, trained-method gains of about 4 to 6 points on math, and a large body of evidence that unaided self-critique does not help. Our agent should expect a gain only through code-verified causes (section 7).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested.

### Add now (established)

Nothing in this subfield justifies adding a new state or operator. The established findings support existing rules and one narrowing:

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Do not add an unaided premortem or self-critique step; it falls under 4b "unstructured self-reflection" | 4b | [E] | b16, c01, c02, b20, c06 (K10) |
| Any failure cause the agent lists must be confirmed by a run before it reaches S5; unconfirmed causes are dropped | G2, G10 | [E] | c07, c16, b20 (K13); d17 (K28, [S]) |
| Do not use "+30% more reasons" or "30% better" as a prior for anything | none | [E] | a02, b07, b08, d03 (K02) |
| Do not use Hill 2012 or Zhang 2023 as premortem support | none | [E] | d04, d05, d08 (K22) |
| Treat the premortem as a hypothesis generator only; no outcome evidence at scale | none | [E] | a07, a08, b09, b13, d07 (K07) |
| A Retry signal ("the check failed") is the baseline for any reflection; a premortem must be compared to Retry | S5, S6 | [E] | b18, b19, c09, c10 (K12) |
| Models find the fault poorly and fix it well: give code-found locations, not model-found ones | S5 | [E] | b17, c04, c05 (K11) |
| Considering how the alternative could be true is the one reliable human debiaser (test before use for LLMs) | G anti-anchoring | [E] | a09, a17, a21, b14 (K09) |

### Test first

| Item | Schema part | Status | Evidence | Why test |
|---|---|---|---|---|
| Failure-frame cause generation at S6, code-verified, then S5 revise | S6, new operator | [S] | a10, a27, d10 (K23) | Only positive evidence is safety and human confidence. Must beat plain "list risks", Retry, forward-success and extra attempts at equal tokens. |
| Failure-frame generator of test inputs for S4/S8 | S4, S8, G3 | [S] | c20, c16 (K13, K17) | G3 needs an unfitted check; causes may supply new inputs. Diversity cap needed. |
| Assume-each-candidate-true explanation before S7 selection | S7 | [S] | a25, a20, a21 | Human calibration evidence; close to the existing counterexample search [E]. |
| Backward-from-end-state step (O5) on hard items only | O5 | [S] | d06 (K26), b21, c12 | Park gains are for complex goals; numbers unread. |
| Cap of 3 to 5 failure causes | prompt parameter | [S] | a23 | Human reversal at 12; no LLM evidence. |
| Forced plan revision after listing | S5 | [S] | d07 (K27) | Weak link in human teams is acting on causes. |
| Confidence shift (P(True) or sample agreement) as a signal | S0, S6 | [S] | c21, a10 (K21) | No study; verbal confidence rejected in 4b. |
| Failure vs success direction | prompt | [C] | b12, d11 | Existing controls null or unseen. |
| Draft-hidden verification of each cause | S4 | [S] | c11, c12 (K14) | CoVe gain on facts; unknown for reasoning. |

## 8. Concrete tests on our bench

All arms get the same total token budget (G7). Setup tokens count. Items are those on our bench (ARC-style grid tasks, word puzzles and BRAINTEASER). Score by code, not by a model judge (G5, G8). Run at least 3 seeds; report paired differences with intervals.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1. Failure frame at impasse | ARC items where the first attempt fails the check | (a) Retry only; (b) list risks, no failure assumption; (c) failure-frame causes, unverified; (d) failure-frame causes, code-verified; (e) forward success scenario; (f) extra independent attempts | Items solved after S6; fraction of listed causes confirmed by a run | (d) above (a) and (f) by a few points; (c) at or below (a) per K10; (b) and (c) similar. If (d) = (a), the premortem adds nothing beyond Retry plus a check |
| T2. Cause yield | 30 items with logged failures | Failure-frame vs risk-list vs success-frame, 10 samples each | Confirmed causes per sample; distinct failure categories per 10 samples | Count higher under failure frame (human result); confirmed yield unknown. Expect diversity collapse (c20) |
| T3. Cause cap | Same items | 3, 5, 12 causes requested | Confirmed causes per 1k tokens; solved items | 12 not better than 3 to 5 per token |
| T4. Premortem as test-case generator | Items with an unfitted held-out check | Cause-derived mutated inputs vs random mutations vs held-out only | Wrong-answer detection rate at S8; false alarms | Targeted inputs catch more fitted-but-wrong programs; not shown in the literature |
| T5. Assume-each-candidate-true | Items with 2 to 4 candidate answers | Explain-each-true then code selects vs vote vs counterexample search (S7) | Selection accuracy vs the best candidate available | Small gain, maybe zero vs counterexample search |
| T6. Confidence shift | Items with known correctness | P(True) or agreement before and after the premortem | AUC for correctness before vs after | Unknown; if the shift does not track error, drop it |
| T7. Plan-revision forcing | Multi-step plan items | Premortem + forced revision vs premortem only | Plan changed; plan success | Forced revision raises the change rate (d07). Success unknown |
| T8. Easy vs hard | Items split by plain pass rate | Premortem step on easy vs hard items | Net gain and token cost per band | Gain only on hard items (Peabody Exp 3); loss on easy (G11) |
| T9. Draft-hidden cause check | Items with verifiable causes | Check each cause with the draft hidden vs visible | Confirmed-cause precision | Hidden better, as in CoVe (c11) |

## 9. What does not transfer, and why

- **Safe dissent.** The social purpose (let juniors voice doubts) has no meaning for one agent. The 20 to 30 minute group session with round-robin has no equivalent. Samples from one model are not independent voters (G4).
- **Felt certainty of failure.** The human effects (confidence drop, metacognitive ease, unpacking) are stated-confidence effects. An LLM's verbal confidence is not a stop rule (4b). Whether prompt framing moves LLM P(True) is untested (d18).
- **Hindsight bias as the engine.** Humans get a bias, then exploit it. A model has no stored memory of the outcome; the "certain" frame is only a prompt, and the model may simply play along and write plausible causes with no tie to the real failure. That is the G10 problem: reasoning text is not evidence.
- **Counts as success.** All human evidence is about more reasons or lower confidence. An LLM can produce any number of reasons cheaply, so counts carry no value; only confirmed causes count.
- **Group structure.** Brainwriting and round-robin resemble debate mechanics, which G9 excludes.
- **One-shot plans.** Real teams face one-shot plans; the agent can run a check. Where a check exists, running it beats imagining failure. The premortem matters most where no check exists, and that is where it is least verifiable. This is the central tension.
- **Model age.** Most LLM self-critique numbers come from GPT-3.5 and GPT-4-era models (critique.md). Reasoning models may differ.
- **Trained pre-mortem methods.** InvThink and AUGUR change weights. We use a scaffold only (a27, d13).

## 10. Open questions

1. What does Veinott and Lehman (2024) find: did ChatGPT-4 causes match human ones? (d01 abstract only.)
2. Does a failure frame beat "list risks" and Retry on current reasoning models at equal tokens, scored by confirmed flaws?
3. What is the true Mitchell 1989 effect: N, test, and was reason quality measured?
4. Do code-verified premortem causes improve the final answer over unverified ones? (d17 is indirect.)
5. Does a premortem shift LLM P(True), and which way does accuracy move?
6. Is the benefit due to certainty, failure focus or just extra generation? Promortem and equal-token controls are missing.
7. What are the numbers in Park, Lu, Hedgcock 2017 and the corrigendum?
8. How diverse are repeated premortem samples from one model; do several scenarios beat one?
9. Does the effect appear only on complex, unfamiliar plans (Peabody Exp 3)?
10. What is the Peabody cadet effect size (PDF 403, abstract only)?
11. Did Fischhoff and Macgregor 1982 really fail to replicate Koriat 1980, and by how much?
12. Do reasoning models change the intrinsic self-correction picture?
13. Does a failure frame hurt on easy items by raising false doubt? (Our own data: forced doubt cost 17 points on word puzzles, 92% vs 75%, SCHEMA G1.)

## 11. Sources

[V] = opened (page or PDF text read) per the evidence files. [M] = snippet only or not opened. Several [V] items were abstract or record pages only; this is stated in the notes after the list.

- [V] Mitchell, Russo, Pennington 1989, J Behav Decis Making 2(1), 25-38 (abstract only). https://doi.org/10.1002/bdm.3960020103 ; https://colab.ws/articles/10.1002%2Fbdm.3960020103 ; https://api.crossref.org/works/10.1002/bdm.3960020103
- [V] Veinott, Klein, Wiggins 2010, ISCRAM. https://idl.iscram.org/files/veinott/2010/1049_Veinott_etal2010.pdf
- [V] Klein 2007, HBR premortem (summary page). https://hbr.org/2007/09/performing-a-project-premortem
- [V] Klein 2021, Psychology Today. https://www.psychologytoday.com/ie/blog/seeing-what-others-dont/202101/the-pre-mortem-method
- [V] Gary Klein site. https://www.gary-klein.com/premortem
- [V] Wikipedia Pre-mortem. https://en.wikipedia.org/wiki/Pre-mortem
- [V] Wikipedia Hindsight bias. https://en.wikipedia.org/wiki/Hindsight_bias
- [V] Review page on premortem evidence (secondary for Mitchell, Veinott, Gallop). https://corporate.jcx.au/premortem
- [V] Blank, Musch, Pohl 2007 overview of hindsight bias. https://iphils.uj.edu.pl/~a.trybus/classes/logic/cs/20.Pohl.Hindsight.Bias.pdf
- [M] Guilbault et al. 2004 and Christensen-Szalanski 1991 meta-analyses (snippets). https://stafforini.com/works/christensen-szalanski-1991-hindsight-bias-metaanalysis
- [V] Koriat, Lichtenstein, Fischhoff 1980 (full URL is truncated in evidence_a.jsonl a19; host newiipdm.haifa.ac.il)
- [V] Arkes, Faust, Guilmette, Hart 1988. https://Www.Gwern.net/doc/psychology/cognitive-bias/sunk-cost/1988-arkes.pdf
- [V] Sanna and Schwarz 2004; Schwarz et al. 2007 (dornsife.usc.edu, Norbert Schwarz site; full URLs in a23, a24)
- [V] Sieck, Merkle, Van Zandt 2007. https://www.globalcognition.org/articles/sieck-obhdp07-fixation-cognitive-overco (path truncated in a25)
- [V] Meuer, Nestler, Oeberst 2022. https://doi.org/10.1037/xap0000445
- [V] Hill 2012, Judgment and Decision Making. https://jbaron.org/journal/11/111014/jdm111014.pdf
- [V] Park, Lu, Hedgcock 2017 (abstract). https://doi.org/10.1177/0956797617715510
- [V] Peabody thesis (abstract). https://digitalcommons.mtu.edu/etdr/374/
- [V] Kannan 2026 thesis (abstract). https://digitalcommons.mtu.edu/etdr/2053/
- [M] Gallop and Bischoff 2016 (record only). https://doi.org/10.1080/19488289.2016.1240118
- [V] Roose, Lehman, Veinott 2023 (abstract). https://doi.org/10.1177/21695067231193680
- [V] Zhang et al. 2023, J Personality. https://doi.org/10.1111/jopy.12879
- [V] Gilmartin et al. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6493673/
- [V] Beidas et al. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9375077/
- [V] Wippold et al. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11756269/
- [V] Implementation Science Communications 2025 review. https://pmc.ncbi.nlm.nih.gov/articles/PMC12330140/
- [V] Koellinger and Treffers 2015. https://pmc.ncbi.nlm.nih.gov/articles/PMC4683002/
- [M] Student poster SJDM 2020, dlab.sauder.ubc.ca (snippet; URL truncated in b12)
- [V] Veinott and Lehman 2024 (abstract). https://digitalcommons.mtu.edu/michigantech-p2/1606 ; https://api.crossref.org/works/10.1007/978-3-031-76827-9_15
- [V] InvThink, arXiv 2510.01569. https://arxiv.org/abs/2510.01569
- [V] AUGUR preprint (abstract). https://doi.org/10.20944/preprints202610.0494.v1
- [V] Prospective Hindsight (RL), arXiv 2610.02740. https://arxiv.org/abs/2610.02740
- [V] Bench to the Future 2, arXiv 2604.26106. https://arxiv.org/abs/2604.26106
- [V] Scott et al. 2025, arXiv 2505.14370. https://arxiv.org/abs/2505.14370
- [V] Ghosh et al. 2026, arXiv 2601.18033. https://arxiv.org/abs/2601.18033
- [V] Life-task planning interviews, arXiv 2512.11096. https://arxiv.org/abs/2512.11096
- [V] Audited action gates, SSRN 7348298. https://doi.org/10.2139/ssrn.7348298
- [V] Huang et al. 2024, arXiv 2310.01798. https://arxiv.org/abs/2310.01798
- [V] Tyen et al. 2024, arXiv 2311.08516. https://arxiv.org/abs/2311.08516
- [V] Kamoi et al. 2024, arXiv 2406.01297. https://arxiv.org/abs/2406.01297
- [V] Renze and Guven 2024, arXiv 2405.06682. https://arxiv.org/abs/2405.06682
- [V] Shinn et al. 2023 Reflexion, arXiv 2303.11366. https://arxiv.org/abs/2303.11366
- [V] Madaan et al. 2023 Self-Refine, arXiv 2303.17651. https://arxiv.org/abs/2303.17651
- [V] Gou et al. 2024 CRITIC, arXiv 2305.11738. https://arxiv.org/abs/2305.11738
- [V] Dhuliawala et al. 2023 CoVe, arXiv 2309.11495. https://arxiv.org/abs/2309.11495
- [V] Weng et al. 2023, arXiv 2212.09561. https://arxiv.org/abs/2212.09561
- [V] Chen et al. 2025 Reverse thinking, arXiv 2411.19865. https://arxiv.org/abs/2411.19865
- [V] Saunders et al. 2022, arXiv 2206.05802. https://arxiv.org/abs/2206.05802
- [V] McAleese et al. 2024 CriticGPT, arXiv 2407.00215. https://arxiv.org/abs/2407.00215
- [V] Kambhampati et al. 2024, arXiv 2402.01817. https://arxiv.org/abs/2402.01817
- [V] Zhang et al. 2025 Who&When, arXiv 2505.00212. https://arxiv.org/abs/2505.00212
- [V] Cemri et al. 2025 MAST, arXiv 2503.13657. https://arxiv.org/abs/2503.13657
- [V] Gu et al. 2025 world model, arXiv 2411.06559. https://arxiv.org/abs/2411.06559
- [V] Perez et al. 2022, arXiv 2202.03286. https://arxiv.org/abs/2202.03286
- [V] Kadavath et al. 2022, arXiv 2207.05221. https://arxiv.org/abs/2207.05221

Notes on source depth: Mitchell 1989, Veinott and Lehman 2024, Gallop and Bischoff 2016, Park 2017, Peabody, Kannan, Roose 2023 and AUGUR were abstract or record pages only. Veinott 2010, Koriat 1980, Arkes 1988, Sanna and Schwarz 2004, Sieck 2007 and Hill 2012 were read in text. Not re-opened (critique.md): Tyen's +18 to +44, Huang's 89.0 round-2 value, MAST kappa 0.77, Renze per-type values, Veinott 2010 secondary-page details, Gallop 2016, Peabody statistics.
