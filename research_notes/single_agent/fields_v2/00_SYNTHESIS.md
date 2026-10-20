# Synthesis: what twelve fields say about making one agent think better

*2026-10-20. Built from briefs 01 to 12 in this folder, after reading 00_PLAN.md and the earlier round (`../fields/00_SYNTHESIS.md`, eight fields, called "round 1"). 00_PLAN.md is not edited here.*

Ids: "F07 a-02" means evidence id a-02 in field 07's files (diag-a-02). F10 ids may be expdec-, expert- or plain letters. Marks: **[ours]** our measurement in 00_PLAN.md; **[V]** source opened, often only the abstract; **[M]** memory or snippet; **[pre]** preprint. Where a brief says its CHECK line overrides its claims file, I use the CHECK line. Round 1 had a "gap brief 08"; field 08 is now intelligence analysis, so I call the old one "the round-1 gap brief".

Source quality: across the twelve claims files, 84 claims are "established", 30 "contested" and 163 "single-source". Most LLM evidence is preprint, abstract level, on models larger or older than ours. Most human evidence is small lab samples. Read every mechanism below as a hypothesis to measure at equal tokens.

---

## 1. What changed since round 1

### Confirmed with more independent support

1. **Doubt must be triggered, never scheduled.** New: "be reflective" scored 44.5% against 45.0% for "be fast" in residents, and no instruction effect in 393 clinicians (F07 E1: a-02, a-14); only 8% of 745 diagnoses revised under unstructured reflection, corrections about equal to backfires (F07 E2); correct logic answers already in the first fast response (F03 E1); Einstellung bites only when the first move is good but not best (F10 2.1, F02 3.1). In LLMs, intrinsic self-critique collapses accuracy (F12 2.3, F10 2.2, F11 E1). Our BrainTeaser drop is the same shape [ours].
2. **A real outside signal makes revision work.** Three sources in F10 2.2, five in F12 2.3, plus F11 E1, F04 E9, F05 E7, F08 E5.
3. **Samples from one model are too alike.** 4000 generated ideas left about 200 unique (F05 b-02); two wrong models give the same wrong answer about 60% of the time across 350+ models (F10 b-10, F09 d-15). Within one model it is surely higher, but unmeasured (F09 d-17).
4. **Spend by difficulty.** F12 2.6 (over 4x efficiency, math with a trained verifier); F11 E2 (eight groups on overthinking). The one Claude metacognitive harness gained +19.6 on LiveCodeBench Hard and lost 0.7 on Easy (F11 d-04).
5. **Full ACH has no gain**: five human experiments and a review of 7 articles and 6 experiments; error 0.26 for ACH against 0.21 for control, n = 50 (F08 E1).

### New or sharpened

6. **All twelve fields want a mode gate and none can supply one.** F01 d-27, F05 d-09, F11 d-13, F03 Q7: no study predicts, before solving, whether a task is open or single-answer. The gate rests on our data alone.
7. **Judged novelty does not survive execution.** LLM ideas beat humans on blind novelty (5.64 against 4.84), then lost the edge when 43 experts ran them (F05 b-01, b-04, b-05; F01 b-09). LLM-judged novelty correlates negatively with later citations, rho -0.29 (F05 b-12). For our diverge route: the NoveltyBench win counts distinctness plus our utility score; the architecture win used a training run as judge. Only the second is selection the evidence supports.
8. **Model strength moves the right doubt rate.** CRT trap answers: 80% (davinci-003), 15% (ChatGPT-3.5), 0% (ChatGPT-4) (F10 d-01). Prompting the weak model to use algebra cut traps 80% to 29% but raised atypical errors 15% to 43% (F10 d-02). Doubt helps weak models and costs strong ones. Trap rate is a per-model number to measure.
9. **Forecasting scaffolds did not help an LLM**: Brier Basic 0.1062, Base Rates 0.1233, Breakdown 0.1815 on PaLM 2, 692 questions, partly a label artefact (F09 d-01, d-02 [pre]). Retrieval moved the score, templates did not (F09 d-21).
10. **Models fail at locating their own errors, not fixing them** (F12 2.5, F11 c-04, F08 c-13). A revise step must be handed the failing example by code.
11. **Counterexamples need code.** Valid counterexamples for under 9% of wrong solutions without it (F03 b-05 [pre]). With test feedback, counterexample prompting raised rule discovery 42% to 56% on 11 models (F08 E4 [pre]).
12. **Models write the right candidate and drop it** (F03 E4), and **written reasoning is not an audit trail** (F06 S11, F10, F11 E3, F12 2.8).

### Overturned, downgraded or corrected

- **The "36.3 points" CoT drop** repeated in four briefs is o1-preview against GPT-4o. Same-model drops: 23.1 (GPT-4o), 8.0 (Claude 3 Opus), 6.05 (Gemini 1.5 Pro), about 2 for small Llamas (F03 d-11).
- **Incubation** is d = 0.29, CI 0.21 to 0.39, not 0.41 (F04 d-01). Baird 2012 leans not replicated; unconscious thought g fell from 0.15 to 0.018 after bias correction (F03 E7, F04 E8). No incubation step.
- **Insight as sudden restructuring** rests on self-report; impasse may be about 8% of problems (F04 S3, one study); warmth did not separate insight (F11 a-10). This weakens plan principle 2's Metcalfe and Wiebe citation [M] and says the impasse trigger will rarely fire.
- **The Claude metacognitive harness**: cost $0.78 against $0.29 for pass@1 and $1.42 for a 4-attempt aggregator; 56.9 against 53.7 for the aggregator; matched random retry 45.7 against harness 47.0 with overlapping intervals, n = 100 (F11 d-02 to d-06). Still a hypothesis, one model, no replication.
- **Dorst and Cross, Kruger and Cross, Jansson and Smith** were not opened by anyone (F06 d-15 to d-17). Design cognition gives hypotheses.
- **Dropped citations:** Ghasemi 2022 for first-response correctness (F03 d-17); MedEinst "60.9%" (F10 b-02); AgentCDM and BASIN as ACH evidence (F08); Satopaa 1501.06943 withdrawn, cite 1406.2148 (F09 a-06); deliberate practice is about 12% overall, not 18% (F02 2.2).

---

## 2. Where the twelve fields converge

**C1. Gate first, then choose how much to think.** F01 M1, F02 M2, F03 M1, F05 M1, F06 M2, F07 M4, F10 M3, F11 M6, F12 M3. CoT helps on math and symbolic items only (F12 2.1: 100+ papers, 14 models); it hurts where thinking hurts people (F03 d-10 to d-12); longer thinking lowers accuracy on built tasks, with Claude models distracted (F12 a-18). Direction is strong. The router is untested (point 6).

**C2. A first answer stays unless a check overturns it.** F07 M4, F12 M2, F11 M1, F10 M2, F02 M1, F03 M3. Six lines of work, human and LLM.

**C3. Revision runs only from real output, and the output must be localised.** F12 M1 and 2.5, F11 M2, F03 d-08 (CRITIC: HotpotQA F1 42.8 to 52.9 with tools), F10 d-07 (execution feedback matched baselines using over 10x more samples [V abstract]), F06 M1 ("back talk" from the work).

**C4. The signal must be trustworthy.** Our ARC program that fit every example and was wrong [ours]; Reflexion's self-written tests passed wrong code (round-1 gap brief: 16.3% false passes); F12 M1 keeps held-out cases; F06 M5 ties persistence to a verification.

**C5. Alternatives help only if the right one is on the list, and the rival test must read something real.** F07 S1 (checklist with the true diagnosis 0.49 to 0.75, without it 0.43; one RCT, 90 students), F07 S4 (right diagnosis in the list 64%, ranked first 39%), F08 E4, F03 M7, F10 M2. The shared move: pick the input where two rivals disagree.

**C6. Code counts; the model proposes.** F08 E2 (forcing probabilities to sum to 1 cut error 35%), F08 M3 (drop clues consistent with all rivals), F05 M5 (all tested LLMs lost to linear regression on bandits, so the program keeps the books), F09 M5 and M6, our symmetry-first selector (34/36 against 33/36 for the vote) [ours].

**C7. Generate independently, then pool and select.** F01 E2, F02 2.4 (nominal groups won 18 of 22 experiments), F06 M3, F12 M7. Caution: the human cause is production blocking, which a model lacks. LLM support is one preprint (F01 b-05) plus our NoveltyBench result [ours].

**C8. Open-task selection needs something outside the generator.** F01 E4, F05 E3 and E4, F06 S12, F02 d-08, F10 3.1 (judges favour their own text). Only execution-based checks have support (F01 d-23).

**C9. Examples and hints fixate, so show them late.** F01 E1, F02 2.5, F06 E4 and E5, F07 E6 (BiasMedQA: GPT-4 lost about 5%, Llama 2 70B about 20%), F10 2.1. Bias warnings alone recovered little for weak models (F07 b-11).

**C10. One agent, not a team.** F08 E6, F10 2.3, F12 2.7; debate lost to self-consistency at matched cost (F03 d-06: 83.2 against 85.3 at 6 responses).

**C11. Stated confidence and written reasons are weak monitors.** F07 E4, F10 b-12 (AUROC 0.52 to 0.61), F11 E3, F11 metacog-b-02 (monitoring and control correlate r = .17), F09 M4.

---

## 3. Contradictions and how I resolve them

| Conflict | Resolution |
|---|---|
| **Agreement as the hardness signal.** F03 M2, F09 M3, F10 M4, F11 M3, F12 M4 route on it; F09 d-15, F10 b-10 say shared errors make it overconfident; semantic entropy costs 5 to 10x (F09 d-08). | Agreement is a prior. Early stop needs agreement plus a check the candidate was not fitted to, or a measured class table. Probe with 3, test 3 against 5. Measure AUROC first. |
| **No reasoning-field backing for divergence, strong backing for homogeneity.** F03 Q7 against F01 E3, F05 E2, F12 d-04. | Both hold. Evidence supports diversity on open tasks, not doubt on closed ones. Divergence stays on the open route. |
| **Isolated draws or an "avoid the previous" list.** F01 M2 against F06 M3, F12 M7; F12 d-05: in-context regeneration helps, not enough. | Three arms at equal tokens: isolated, isolated plus code dedupe, sequential avoid-list. |
| **Reflection helps on complex cases (F07 C1, snippets), not otherwise (F07 E2).** | Conditional trigger fits both: real failure, split, or flagged complexity. Require corrections to exceed backfires. |
| **Reframing.** Praised in F06, F03 M8; null in 280 people (F06 S1); helped on one task (F06 S2 [pre]). | After two failed revisions only, citing an output line, counted against equal fresh resamples. |
| **Reset or incubation.** F01 M9, F02 M5 propose; F04 M6 says add none. | Drop. If tested, test as a resampling control. |
| **Lessons early or late.** F06 M4 late; F11 M7, F10 M9 retrieve for same class. | Show after the first attempt, only if confirmed by an outside signal. Test before against after. |
| **Cap thinking or not.** F12 M5 caps; F09 b-18: removing backtracking hurt calibration (ECE 0.042 to 0.161); F12 d-12: hard-item collapse contested. | Cap only on gated easy items. Test accuracy against cap. |
| **Parallel against one extended thought.** F11 c-06, F12 d-08: parallel won by up to 20%; the round-1 gap brief cites the reverse. | A single extended-thinking attempt is the first comparison arm. |
| **Outside view and base rates.** F09 M1, F10 M7 propose; F09 d-01 no gain. | Off the default path. Retrieve facts when facts are the gap. |
| **Persona and strategy voters.** Ordinary personas restore diversity [pre] (F01 3b); strategy diversity failed on AIMO 3; our 92% to 75% [ours]. | Open route only, ordinary personas, measured. Never voters on single-answer tasks. |
| **Pre-mortem.** F10 M8 keeps it; F10 3.2: raises count of reasons, no decision evidence. | Only before a long or no-retry run, one short call. |
| **Harness gain against self-correction null.** F11 d-01 against E1. | No conflict: it uses a fitted controller and external checks. Hypothesis for hard items. |
| **Kahneman and Klein status.** F02 could not open it; F10 read the abstract. | Use F10: intuition is trustworthy in regular settings with feedback. |

---

## 4. Ranked mechanisms for one agent

Ranked by evidence, our data and cost together. "Equal-token test" means against plain best-of-N with the same checker and the same total tokens, counting the mechanism's own calls. Cost is relative to one plain attempt. Status: E established, S single-source, C contested, H hypothesis, O ours.

| # | Mechanism | Plan step | Trigger | Evidence and status | Cost | Equal-token test |
|---|---|---|---|---|---|---|
| 1 | **Mode gate** with per-class plain pass rate and per-model trap rate; sets direct, short rationale, full CoT, checked or open. | mode gate (new) | every problem | Direction strong (F12 2.1, F03 d-11, F10 d-01; E). Router untested (H). | saves | Gate on, gate off, best fixed arm per class, plus a single extended-thinking arm. Must not lose to plain by more than 1 point on BrainTeaser. |
| 2 | **Check-gated stop.** Stop only on a check the candidate was not fitted to (held-out, mutation, symmetry). | converge | checker exists | Strong: F12 M1, F10 M1, F06 M5, ARC failure [ours]. E | small | Wrong stops per 100 and tokens saved, against stop on first pass. |
| 3 | **Revise from real output**, failing example named by code, keep best-so-far, 1 to 2 rounds. | revise | check failed | Strong: F12 2.4 and 2.5, F11 c-04, F03 d-08, F10 d-07. E | small to medium | Pass rate after rounds 1 and 2 against fresh samples; with against without the localising line. |
| 4 | **Select by behaviour.** Run all candidates on rule-made inputs, group, discount trivial clusters, symmetry, then size, then shortest; anchored tie-break. | select | several candidates, runnable | Strong on replay [ours]; F10 M5, F08 E2. O, S | near zero | Offline replay against oracle best and the vote; extend to coding. |
| 5 | **Keep the first natural answer** when no checker exists: one probe, no critique. | route | single answer, no check | Strong, six lines (C2). E | saves | Plain against plain plus one critique round, on ARC and word puzzles. |
| 6 | **Probe, agreement as a prior.** 3 attempts (1 direct, 2 short rationale); log P(correct given k agree) per class. | probe | not gated to direct | Moderate to weak (F10 d-06; shared errors F10 b-10). C | 3x | AUROC of agreement against correctness; router against fixed thresholds. |
| 7 | **Diverge on open tasks.** Isolated calls from the bare task, typical answer first, optional ordinary-persona seeds, conventional core plus one or two distant slots, code dedupe, then prune. | diverge | open, no check | Strong on our data (3.18 to 9.63) [ours]; homogeneity E (F01 E3). Quality leg weak. O | +13% | At least 9 of 10 distinct; ablate typical-first, dedupe, persona seeds; add a non-LLM quality measure. |
| 8 | **Execution-based selection on open tasks**; judge only as controlled tie-break. | select | a run or test exists | Strong in direction: F05 b-04, F01 b-09, d-23; architecture win [ours]. E | medium | Pick by run against LLM judge against random, same candidates. |
| 9 | **Rule-based impasse detector.** Fires on no pass, two unchanged rounds, same error twice, or budget fraction; one state line, one rung, no repeats. | impasse detector | impasse only | Moderate: F03 M8, F11 E2; self-reports unreliable (F11 b-02). H | small | Wasted rounds and solved per 100k tokens against a plain retry loop. |
| 10 | **Discriminating test.** For the top two rivals, derive expected outputs, run the input where they differ. | discriminate | two or more rules fit | Moderate: F08 E4, F07 S4, F03 M7. S | small to medium | Accuracy on probe-split items against vote; how often the test changed the pick. |
| 11 | **Counterexample hunt by code**: rotate, mirror, empty, boundary; expected output derived first. | check | rule fits all examples, no checker | Moderate: F03 b-05, a-18. S | small | Replay against symmetry-first alone. |
| 12 | **Independent usual-suspects list** from a call that does not see probe answers. | ladder (resample) | split or no pass | Weak to moderate: one RCT (F07 S1); a wrong list hurt, small models anchor (F07 E6). S | one call | Gold-in-list rate, then accuracy; wrong-list harm control. |
| 13 | **Input hygiene.** Code isolates a supplied hint or consensus claim and runs a blind pass; marks distractor clauses without rewriting names. | intake (new) | hint or distractor in input | Moderate: F07 E6, F07 c-20, F12 c-15 (clause cut accuracy up to 65%). S | one pass | With against without injected hints; confirm no loss from keeping original words. |
| 14 | **Blind critic.** Strip authorship and order; judge derives expected answer before seeing outputs. | select | any model judging | Moderate: F10 M5, F11 a-05. S | near zero | Judge accuracy with and without hidden authorship. |
| 15 | **Coherence repair and recalibration in code**; no extremizing. | converge (output) | probabilities or confidence emitted | Moderate in humans (F08 E2). H for LLMs | none | Brier or log score against raw output. |
| 16 | **Reframe from back talk.** After two failed revisions, one sentence citing an output line, then a change of representation. | ladder (re-read) | impasse | Weak to moderate: F06 M1, F03 M8; null in F06 S1. C | small | Pass rate against equal fresh resamples. |
| 17 | **Look back, confirmed and late.** Store a lesson only if an outside check supports it; supported after helping twice; shown after the first attempt. | look back | end of problem; same class | Weak: F11 a-09 (with test feedback); staleness unsettled (F11 d-14). H | small | Held-out stream, memory on against off, before against after. |
| 18 | **Program-kept exploration ledger.** | diverge (long runs) | search across calls | Weak: bandit evidence only (F05 E6). S | prompt tokens | Ledger against none on architecture search. |
| 19 | **Pre-mortem** before a costly or no-retry run. | revise | before long run | Weak: counts reasons only (F10 3.2). H | one call | Share of crashed or regressed runs avoided per token. |
| 20 | **Separate-context stuck-check** every 2 to 3 steps. | diverge (long runs) | long open run | Weak: one problem, preprint (F06 S2). S | medium | Against self-monitoring and a plain loop. |

Arms to test, not defaults: choice shuffle on multiple-choice (F07 M6); Self-Discover and step-back per class (F12); frame-swap as a development diagnostic (F06 M9: corrupt the written frame, and if the answer does not move, delete the frame step); trajectory-level confidence (F09 M7).

---

## 5. Proposed single-agent design

```
 problem
   |
 A. INTAKE (code)                             mech 13; F07 M7, F12 M6
    isolate any supplied hint or consensus claim; mark distractor clauses; keep original words
   |
 B. MODE GATE (cheap call + class table)      mech 1; F01 M1, F03 M1, F05 M1, F10 M3, F11 M6
    -> DIRECT (class pass rate high: one natural answer, stop)
    -> CHECKED (a runnable check exists)
    -> NO-CHECK single answer
    -> OPEN
   |
 C. PROBE (3 attempts: 1 direct, 2 short)     mech 6; F03 M2, F09 M3, F10 M4, F12 M4
   |
 D. ROUTE
    CHECKED:  pass a non-fitted check -> SELECT (E), stop                 mech 2, 4
              fail -> REVISE from real output, failing example named       mech 3
              impasse detector fires -> LADDER (G)                         mech 9
    NO-CHECK: agree -> return plurality (trust the first answer)           mech 5
              split -> independent usual-suspects list, discriminating
                       test on the top two, blind anchored pick            mech 12, 10, 14
    OPEN:     DIVERGE (F), then execute or prune                           mech 7, 8
   |
 E. SELECT (code first, model last)           mech 4, 11, 14, 15
    behaviour groups -> symmetry/mutation -> group size -> shortest; counterexample hunt;
    coherence repair on any probabilities
   |
 F. DIVERGE (open only)                       F01 M2 M3, F05 M2 M6, F06 M3, F12 M7
    N isolated calls from the bare task; typical first; code removes near-duplicates;
    one or two medium-distance analogy slots with written mapping; execute where possible;
    long runs: ledger (mech 18) and stuck-check (mech 20)
   |
 G. LADDER (impasse only; one rung per state line; no repeats)   F03 M8, F06 M1, F07 M1
    re-check -> resample (usual suspects) -> re-read citing an output line (mech 16)
    -> helper problems -> diverge hard
   |
 H. FINISH
    always submit plurality or best-so-far; state confidence once, recalibrated in code;
    pre-mortem (mech 19) only before a no-retry run
   |
 I. LOOK BACK (mech 17)                       F11 M7, F06 M4, F10 M9
    lesson only if an outside check supports it; shown after the first attempt
```

Why this shape. Every call added on a single-answer task sits behind a failed check or a split, which is what the doubt evidence supports (C1, C2). Variety sits on the open route, where homogeneity evidence and our two wins support it. The model proposes; code counts, mutates, dedupes and recalibrates (C6). Each mechanism has a switch for ablation at equal tokens.

First comparison before building the rest: one extended-thinking attempt, plain best-of-3, and the full flow, at equal tokens, on the four suites in 00_PLAN.md section 5. If native thinking matches the flow on single-answer suites, keep the flow for open tasks and checked revision only.

Log per problem: route, mode, tokens, ladder rung, selector pick against best candidate, wrong stops per 100, error correlation between probe attempts, gold-in-list rate, and direction of every revision (right to wrong, wrong to right).

---

## 6. What to drop or keep off the default path

| Item | Reason |
|---|---|
| **Fixed-schedule doubt** (always-doubt, devil's advocate on a unanimous answer, closure gate) | Never won on single-answer tasks (F07 E1, E2; F12 2.3; our 92% to 75% and ARC) [ours]. Open route or before a costly step only. |
| **Self-critique with no outside signal** | Collapses accuracy (F12, F10 2.2, F11 E1); models cannot locate errors (F12 2.5). |
| **Full ACH matrix, key assumptions check** | Null in five human experiments (F08 E1); no trial of KAC. ACH-lite counted by code is a split-only experiment with a kill rule (F08 M6). |
| **Extremizing; persona or strategy voters on single-answer tasks** | One model's samples are not independent (F09 M6); failed on AIMO 3; matches our loss [ours]. |
| **Debate and multi-agent panels** | No better than self-consistency at matched cost (F10 2.3, F03 d-06); conformity (F08 E7). |
| **Incubation, reset, "sleep on it" calls** | d = 0.29 in humans, no mechanism in a model, not replicated (F04 M6, F03 E7). |
| **Written chain or stated confidence as evidence or gate** | Unfaithful (F06 S11, F11 E3); AUROC 0.52 to 0.61 (F10 b-12). |
| **Judge-only novelty ranking** | Near chance, negative with later citations (F05 E3, b-12; F01 E4). |
| **Forecasting scaffolds by default** | Worse than plain in the one LLM test (F09 d-01). |
| **Felt-aha, warmth or self-rated feeling-of-knowing as a load-bearing gate** | Warmth did not separate insight (F11 a-10); aha can be induced falsely (F04 C6); no gain on easy items (F11 d-04). |
| **Training-dependent methods** (process reward models, budget forcing, AdaptThink, RL self-correction) | Need labels, fine-tuning or RL (F12 section 6). |
| **Tree of Thoughts by default** | One cheap-scoring task, no equal-compute control (F12 3a). Allow where partial states score cheaply. |
| **Hard-item thinking caps** | Collapse contested (F12 d-12); removing backtracking hurt calibration (F09 b-18). |
| **Lessons or examples before the first attempt** | Fixation (C9). |
| **Rewriting names into codes** | Made the small model worse [ours]. |
| **Semantic entropy at full cost** | 5 to 10x samples, blind to consistent errors (F09 S4); reuse the probe samples. |
| **Human-training results** (creativity training, debiasing workshops, illness scripts, deliberate practice) | Change people, not a fixed model; debiasing checklists also failed in humans (F07 E3). |

---

## 7. What is still a guess

1. **The router.** No study predicts open against single-answer before solving (F01 d-27, F11 d-13). Probe size, thresholds and the class table are [design].
2. **Whether the flow beats one extended-thinking attempt at equal tokens.** Evidence points both ways (F11 c-06, F12 d-08 against the round-1 gap brief).
3. **How correlated Haiku samples are.** Unmeasured; it decides what agreement and early stop are worth.
4. **Whether a small model follows the procedure.** Most LLM evidence is from larger or older models (F12 critique, F10 section 5, F09 d-14). Each step is a hypothesis for ours.
5. **Divergence quality.** We have distinct counts and utility, not executed quality. No top-k test of verbalized sampling or any diversity method exists (F01 d-22). Typical-first alone is untested (F01 d-24).
6. **Discriminating tests, code counterexamples and the usual-suspects list for LLMs.** One paradigm each (Jhaveri; Kämmer), no equal-token test (F10 d-11, F07 d-05).
7. **Impasse rarity.** If impasse is about 8% of problems (F04 S3), the ladder fires seldom and its value is small. Our logs will show it.
8. **Lessons.** Whether they help or go stale is unsettled (F11 d-14). Human learning effects (testing g about 0.50, self-explanation about 0.55, productive failure g = 0.36) are [M] or secondary and do not transfer by default.
9. **Design-cognition procedures** (bridge cycle, frame steps) have no LLM test (F06 a-15). Run the frame-swap check before keeping any frame step.
10. **Token costs** in the table are estimates, not measurements.
11. **Source depth.** Most 2026 audits are single-author or workshop preprints at abstract level. Human nulls (ACH, debiasing) may come partly from skipped steps (F08 intel-a-10); code never skips steps, so the null does not settle it.
