# Synthesis: what eight fields say about making one agent think better

*2026-10-20. Built from briefs 01 to 08 in this folder. Marks: [V] source checked (mostly abstract level), [M] from memory or a search snippet, [ours] our own measurement in 00_PLAN.md. Brief 08 (the gap brief) checked weak claims from the others; where it disagrees with an earlier brief, 08 wins. 00_PLAN.md is not edited here.*

---

## 1. Where the fields converge

**1. Doubt must be triggered by a failed check or a split, never run on a schedule.** Diagnosis: slow, careful residents were no more accurate than fast ones (Norman 2014 [V]), and generic reflection prompts gave no gain (Lambe 2018 [V]). Expert decisions: experts simulate one option and look elsewhere only when the simulation shows a flaw (Klein [M]); fast thinking is safe only in regular settings with feedback (Kahneman and Klein 2009 [V]). Metacognition: a weak feeling of rightness triggers rethinking (Thompson 2011 [V, secondary]). LLM methods: CoT can lower accuracy where deliberation hurts people (Liu 2025 [V]), and longer thinking can lower it on Claude models (Gema 2025 [V]). Our own BrainTeaser loss (92% to 75%) is the same result [ours]. Six sources, one rule.

**2. A real outside signal is what makes revision work.** Self-correction without one fails or hurts (Huang 2024, Kamoi 2024 [V]); models favour their own text when judging (Panickssery 2024 [V]); Greenblatt's ARC gain used real outputs [V]. Design cognition adds the human version: reflective designers listen to "back talk" from the work (Adams, Turns, Atman 2003 [V]). Brief 08 adds the limit: the signal must be trustworthy. Reflexion's self-written tests passed wrong code (16.3% false passes on MBPP, accuracy 80% to 77%) [V, full text].

**3. Alternatives help only if the right one is on the list, and the rival test must read something real.** Kämmer 2021: a checklist containing the true diagnosis lifted accuracy 0.49 to 0.75, one without it did not [V]. Jhaveri 2026: LLMs propose confirming tests, and a counterexample prompt raised rule discovery 42% to 56% on 11 models [V]. Platt and Klayman and Ha say the same in the plan [V]. Diagnosis, intelligence analysis and expert-decision briefs all land on "pick the observation where rivals disagree."

**4. Code should do the counting.** Analysts skipped ACH steps and let neutral facts leak into scores (Dhami 2019, Karvetski 2020 [V]); forcing probabilities to sum to 1 in code cut error 35% (Mandel 2018 [V]). Our symmetry-first selector (34 of 36 vs 33 of 36 for the vote) is the same lesson [ours]. Judged steps add noise; counted steps do not.

**5. Spend by difficulty, and keep setup cheap.** Snell 2024 (4x efficiency) and Adaptive-Consistency (up to 7.9x fewer samples) [V], plus the overthinking papers [V], agree. Every brief warns about our 0% full scaffold [ours].

**6. Fixation on a first wrong frame is real.** Einstellung in chess (Bilalic 2008 [V]), design fixation (Jansson and Smith 1991 [V]), MedEinst trap rates of 33.8% to 66.1% (08 [V]), Only Connect red herrings (08 [V]). The remedy that has any support is to generate before seeing examples, not to force doubt afterwards.

---

## 2. Where they contradict each other or our data, and how to resolve it

| Conflict | Resolution |
|---|---|
| **Agreement as confidence.** 03, 05, 06, 07 treat probe agreement as the machine "feeling of rightness". 08 finds rho 0.20 to 0.59 with correctness, and 48% of GPQA majority answers at agreement 0.8 or higher were wrong (arXiv 2607.08065 [V, single author]). Our ARC run was fooled twice. | Agreement is a prior. Stop on agreement only together with a check the candidate was not fitted to, or where a per-class table shows it pays. Measure AUROC first. |
| **Extremize the vote.** 03 M5 and 02 M4 say push or average votes. 08 says same-model samples share information, so extremizing amplifies bias (8 attempts act like about 2.6 votes [M]). | Drop extremizing for one model. Keep only code-side normalization to sum to 1. Use a measured calibration table if a probability is needed. |
| **Diverse voters.** 02 and 03 want varied prompts. 08: strategy and persona diversity failed on AIMO 3 and matches our 92% to 75% [V, ours]. | No persona or strategy voters on single-answer tasks. Diversity is for open tasks, where distinct answers is the goal (NoveltyBench 3.18 to 9.63 [ours]). |
| **Forced doubt moves.** 05 M4 (Einstellung break), 05 M5 (pre-mortem), 02 M5 (devil's advocate), 01 M4 (closure gate) all risk the BrainTeaser loss. Supporting evidence is on groups or counts of reasons: the "30%" pre-mortem figure counts reasons generated, not correct decisions (08 [V]). | Allowed only on open routes or before a costly irreversible step, never on a converge path. Each logs flips in both directions. |
| **Critic on another's proposal.** 05 M7 says people judge others' arguments well (Mercier and Sperber [V]). Huang says LLM critique alone hurts. | Allowed only when tied to a run or a difference input, authorship stripped. Otherwise off. |
| **Reframing.** Design cognition praises it, but the largest controlled test of LLM reframing is null (Shin, CHI 2025, 280 people [V]); Xu 2026 finds an external regulator helps on one problem [V]. | Reframe only after a failed check, citing a concrete output line; test on open routes only. |
| **Lessons shown early or late.** 04 warns examples cause fixation; 06 and 05 want lessons retrieved at the start. | Show lessons after the first attempt, and failure contrasts only after a failed attempt. Test before vs after. |
| **Router vs native thinking.** 08 M7: nothing shows a probe of K traces beats one extended-thinking attempt at equal tokens. Parallel beats sequential in one paper (2506.04210), the reverse in another (2511.02309 [M]). | Add the single-thinking arm as the first comparison. The router keeps single-answer duty only if it beats it. |
| **Weak claims corrected by 08.** Elstein "3 to 5 hypotheses" is not confirmed (downgrade to [M]). The "2025 GJP reanalysis" is a 2024 reanalysis, disputed. "Fast is not worse holds more for models" (01) is unsupported given MedEinst. The 2026 metacognitive harness (2605.14186, 48.3 to 56.9) has no equal-token comparison, so it is not support for the router. | Use the corrected labels. Do not cite the harness as evidence. |

---

## 3. Ranked mechanisms for one agent

Ranked by evidence strength, our data and cost together. "Equal-token test" always means against plain best-of-N with the same checker and same total tokens.

| # | Mechanism | Plan step | Trigger | Evidence | Token cost | Test at equal tokens |
|---|---|---|---|---|---|---|
| 1 | **Check-gated stop.** Stop only when candidates pass and the check includes something not fitted to (held-out example, symmetry, mutation). Agreement without a pass goes to revise or escalate. | converge | any task with a checker | Strong: Reflexion MBPP [V], our ARC fooling [ours] | small (extra check) | Wrong stops per 100 items and tokens saved, vs "stop on first pass" |
| 2 | **Revise from real output.** Feed the failing output, one-line explanation that cites an output line, keep best-so-far, 1 to 2 rounds, trusted checks only. | revise | check exists and failed | Strong: Greenblatt, Kamoi, Huang [V]; self-explanation g 0.55 [V, humans] | small to medium | Pass rate after round 1 and 2 vs fresh samples; with vs without the explanation line |
| 3 | **Select by behaviour.** Run all candidates on fresh rule-made inputs, group, discount constant or trivial clusters, symmetry first, then group size, then shortest; anchored tie-break. | select | more than one candidate and a way to run them | Strong: 34/36 vs 33/36 replay [ours]; CodeT clustering trap [M] | near zero | Offline replay against oracle best and the vote; extend to coding set |
| 4 | **Mode gate.** Decide direct short answer, one short rationale or full CoT, and cap thinking length. Probe includes one direct and one CoT attempt. | new step before probe | every problem | Strong: Sprague 2025, Liu 2025, Gema 2025 [V] | saves tokens | Per class, gate vs best fixed arm; accuracy against thinking cap |
| 5 | **Probe with a per-class calibration table.** Agreement is a prior; log P(correct given k of 5 agree) by class. | probe, route | every problem | Moderate: weak but positive signal (08 [V]) | small | AUROC of agreement vs correctness per suite; router vs fixed thresholds |
| 6 | **Diverge then prune** for open tasks, generating before reading examples or lessons. | diverge | no check, open answer | Strong on our data [ours]; fixation literature [V] | +13% [ours] | Keep at least 9 of 10 distinct; ablate de-anchoring |
| 7 | **Rule-based impasse detector.** Triggers: no pass, last two rounds changed nothing, same error twice, budget fraction. Write one state line, move one rung, never repeat a move. | escalate | impasse only | Moderate: Ohlsson [M]; effort misallocation papers [V] | small | Wasted rounds and solved per 100k tokens vs a plain retry loop |
| 8 | **Discriminating test.** For the top two rivals, derive expected outputs, run the one input where they differ, and update the ranking from real output only. | converge step 5, select | two or more rules fit | Moderate: Jhaveri 42% to 56% [V]; Platt [V] | small to medium | Accuracy on probe-split items vs majority vote; how often the test changed the pick |
| 9 | **Counterexample hunt** with rule-based mutations (rotate, mirror, empty case); expected output derived before seeing candidate output. | select | rule fits all examples, no checker for new inputs | Moderate: mental models [M]; our symmetry result [ours] | small | Replay: does it beat symmetry-first or only equal it |
| 10 | **Expertise-adaptive scaffold.** If the class plain pass rate is high, run bare; show worked examples only for weak classes; fade as skill rises. | route | per-class pass rate known | Moderate: expertise reversal [V]; explains our 92% [ours] | saves tokens | Three arms per class: bare, fixed scaffold, adaptive |
| 11 | **Independent candidate recall.** One call listing usual suspects that does not see probe answers; merge, dedupe. | escalate (resample rung) | probe split or no pass | Weak to moderate: Kämmer [V, one study]; 08 narrows the trigger | one call | Gold-in-candidates rate, then accuracy; wrong-candidate harm control |
| 12 | **Reframe from back talk.** After two failed revisions, one sentence on what the failing output says about the frame, citing an output line, then a change of representation. | escalate (re-read rung) | impasse | Weak to moderate: Adams 2003 [V]; Xu 2026 one task [V]; Shin null [V] | small | Pass rate vs equal fresh resamples |
| 13 | **Look back, shown late.** One-line lessons by class, supported after helping twice, shown after the first attempt; failure contrasts only after a failure. Calibration offset kept in code. | look back | end of problem; start of same class | Weak: Reflexion memory [M]; fixation risk | small per problem | Held-out stream, memory on vs off, before vs after first attempt |
| 14 | **Pre-mortem before costly runs.** Three failure reasons, run the cheapest test, one short call. | revise, diverge | before long architecture run or no-retry submission | Weak: quantity of reasons only [V]; PreFlect [V, listing] | small | Share of crashed or regressed runs avoided per token |
| 15 | **External co-regulator** every 2 to 3 steps on long open loops: "is the agent stuck on one paradigm?" | diverge | long open run | Weak: one task, preprint [V] | medium | vs self-monitoring and plain loop on architecture search |

Not ranked, and to keep out of the default path: key assumptions check (no trial), full ACH matrix (null in three human trials, [V]), devil's advocate on a unanimous answer, extremizing, persona voters, and a different-model tie-break (breaks the one-model rule; optional arm only).

---

## 4. Concrete changes to 00_PLAN.md

**Add**
1. **Step "mode gate" before the probe** (mechanism 4). Reason: CoT helps mainly on math and symbolic tasks and hurts where thinking hurts people [V]. It also protects BrainTeaser.
2. **A single extended-thinking arm** as the first comparison in section 5, plus an arm of 4 to 5 attempts with small thinking budgets. Reason: 08 M7. Without it the router's value is unproven. If thinking alone matches, restrict the router to diverge and revise.
3. **Per-class calibration table and wrong-stop log** in section 5 logging: P(correct given agreement), wrong stops per 100, pairwise error correlation between probe attempts, gold-in-candidates rate, and flip direction (right to wrong, wrong to right) for every doubt step. Reason: these decide which pieces pay.
4. **An abstain floor.** Never abstain on the first pass; always submit the plurality or best-so-far. Reason: the 0% scaffold and the 4 ARC abstentions [ours].
5. **Principle 10: samples from one model are not independent.** Reason: 08 F1 and F3.
6. **A rule-based impasse detector** in front of the ladder (mechanism 7). Reason: model-stated "I am stuck" is unreliable (monitoring and control correlate r = .17 [V]).

**Change**
7. Route "an attempt passes the check" must read: stop only if the check includes something not fitted to, else go to select. Reason: mechanism 1.
8. Principle 7 and Step 0: agreement sets a prior, early stop needs a check or a class table. Reason: Adaptive-Consistency was validated where errors are scattered, not on unanimous wrong answers (08 F5).
9. Converge step 5 (rival rule) fires only when two rules fit, not by default. Reason: our BrainTeaser result, and a small model may not follow eight steps; split the steps across calls if it fails.
10. Principle 3 text: cite the Reflexion MBPP result beside Reflexion, and say "trusted check." Reason: self-written tests misled the agent.
11. Look back (step 3): lessons shown after the first attempt; failure contrasts only after a failure; the calibration offset stays in code. Reason: fixation, and a verbal offset may not change behaviour.
12. Escalate rung 2 (resample) gets an independent "usual suspects" variant; rung 3 (re-read) must cite a concrete output line. Reason: mechanisms 11 and 12.
13. Section 4 build order: put mechanisms 1, 3 and 4 into pieces 3 to 5, and make the thinking-arm comparison part of piece 1.
14. Label fixes: GJP "2025 reanalysis" becomes "2024 reanalysis, disputed"; Elstein's hypothesis count becomes [M]; the metacognitive harness is not evidence for the router.

**Drop**
15. Extremizing, and any persona or strategy voters on single-answer tasks. Reason: 08 and our 92% to 75% loss.
16. Four-strategy parallel thinkers with a judge as a default. Self-Discover and step-back stay as per-class arms only (one lab, older large models [V]).
17. Fixed-schedule doubt of any kind (devil's advocate, closure gate) on converge routes.

---

## 5. What is still a guess

- **Everything LLM-side comes from larger models than Haiku.** Self-Discover, step-back, Tree of Thoughts, the harness and most calibration work. Each step is a hypothesis for our model.
- **Router accuracy.** No study tests a router across single-answer and open tasks at equal tokens. The probe size, thresholds, the 20% divergent slice and the extremizing factor (now dropped) are [design].
- **Correlation of Haiku samples.** Unmeasured. It decides whether agreement, early stop and any aggregation are worth anything.
- **Whether native thinking already does the probe's job.** Engineering inference only.
- **Counterexample and discriminating-test steps for LLMs.** Human mental-model evidence is moderate; the LLM evidence is one paradigm (Jhaveri) and no equal-token test.
- **Lessons and cards.** Productive failure, expertise reversal and testing effects are human learning results [V, secondary]; no equal-token LLM test exists. A wrong card may anchor a small model (BiasMedQA, MedEinst [V]).
- **Human nulls.** ACH failed in humans partly because steps were skipped; code may behave differently, so the null does not settle it either way.
- **Token costs in the table** are estimates, not measurements.
- **Many abstract-level sources.** Most 2026 audits in 08 are single-author or workshop preprints; treat each as one data point.
