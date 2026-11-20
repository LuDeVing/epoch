# Stage model and incubation: deep document

*Subfield A12.08. Built from evidence_a-d.jsonl (a01-a26, b01-b30, c01-c27, d01-d16), claims.jsonl (K01-K26) and critique.md in this folder. Schema fit: our schema (SCHEMA.md section 4b) already lists "incubation by distraction" as not to add. Nothing here argues against that. This document is background, plus a short list of things worth testing at equal tokens.*

## 1. What it is

The stage model says creative problem solving runs in four stages: preparation (work on the problem consciously), incubation (leave it alone), illumination (the answer arrives, often as an "aha"), and verification (check the answer). Wallas named the stages in 1926, drawing on Poincare's self-reports (a01, a02).

Three things sit under this label, and they are different claims:

1. **A descriptive claim.** Solutions often seem to arrive after a break. This is introspection and anecdote.
2. **An empirical claim.** A break after an impasse raises later solving. This has been tested in about 117 studies. The average effect is small.
3. **A mechanism claim.** The break helps because of unconscious work, forgetting of wrong cues, a fresh look, or sleep. These accounts are not settled.

For our agent, the stage model is not a mechanism to implement. Its parts already exist in the schema as code-checked states: preparation is S1-S5, impasse is S6, verification is S8. The one stage with no counterpart is incubation, and the schema excludes it on purpose. The value of this document is to say why that exclusion is still right, what the closest LLM tests show, and which narrow variants are worth a cheap test.

## 2. History and theories in depth

**Poincare (1910).** He described mathematical discoveries after rest. His model: during preparation, ideas are set in motion like "hooked atoms". They then collide at random below awareness. A sense of mathematical beauty selects the good combination and passes it to consciousness (a02). He also said unconscious work cannot do long calculations that need held intermediate results. Limit: his examples were reported almost 30 years later (a01).

**Wallas (1926).** Four stages: Preparation, Incubation, Illumination, Verification. He added "associative chains" spreading in the break and an "Intimation" feeling just before the solution (a01). There was no experiment.

**Anecdote problems.** Weisberg (2006) showed that famous stories (Coleridge and Kubla Khan, Mozart, Kekule's benzene dream) are false or unreliable (a01, d11). The stage model therefore has weak anecdotal footing.

**Three accounts of why a break helps (Gilhooly 2016, a12, b10).**

| Account | Claim | Key support | Key problem |
|---|---|---|---|
| Unconscious work | Ideas keep recombining below awareness (Poincare; Dijksterhuis unconscious thought theory) | Immediate-incubation benefits; Gilhooly tests of conscious work found none (mean r = 0.11, 8 correlations, a18) | Unconscious thought effect on decisions did not replicate at scale (b17, K10). Gilhooly is an advocate. |
| Intermittent conscious work | The solver briefly returns to the problem during the break and does not notice | Cheap and plausible; fatigue relief alternative (Ellwood 2009) | Thought counts did not predict gain in Baird 2012 (b11), but they are self-reports |
| Beneficial forgetting / fresh look | The break lets misleading cues decay (Smith 1995), or any switch gives a fresh look (Segal 2004) | Smith: more solving when the misleading cue was forgotten (a14). Segal: break beat no break, length and demand did not matter (a13, b12) | Forgetting cannot explain immediate incubation. Segal is a single spatial problem, read second-hand. |

**Mind wandering variant.** Baird et al. (2012) found an undemanding break, which lets the mind wander, beat a demanding task, rest and no break, but only on problems seen before (b15). This fits assimilation of earlier-seen material more than free-floating unconscious work (K05).

**Sleep variant.** Wagner et al. (2004) found sleep doubled discovery of a hidden rule (a03). Later work split on stage and on task (section 5).

**Unified model.** Helie and Sun (2010) built CLARION with an explicit and an implicit module. Incubation is implicit processing while the explicit module is idle (a21, c19). The model's fits were not read here. Gilhooly notes it does not break through into awareness without an explicit return to the task (a21).

**Computational framing for ML.** Gizzi et al. (2022) and Nair, Gizzi and Sinapov (2024) map the four stages onto ML pipelines: preparation to problem formulation, incubation and illumination to knowledge representation and manipulation, verification to evaluation (a22, b24, c20). It is a design framework with no incubation test.

## 3. Core findings with exact numbers

Status key: established, contested, refuted, single-source (from claims.jsonl).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Break after impasse gives a small average benefit | 117 studies, 3,606 participants, median 25 per study. Weighted d = 0.29 (CI 0.21 to 0.39). Unweighted 0.41. 85 studies positive. Q = 173.99, df 113, between-study variance .0834 | Sio and Ormerod 2009 (b01) | established (K02) |
| Publication bias test found nothing | Regression beta = .08, p = .41 | b02 | contested; same test type missed bias elsewhere (K10) |
| Benefit differs by task | Linguistic k=65, visual k=35, creative k=14. Larger for divergent thinking than for linguistic or visual insight | b04, a11 | established |
| Low-demand filler beats high-demand filler | High-load k=76, d about 0.24. Low-load k=22, d about 0.52. Rest k=16, d about 0.46. Low load beat rest only on linguistic problems (beta .54, p < .05) | b03 | contested (K04) |
| Longer preparation gives bigger effect | Positive significant regression coefficient; moderators correlated | b04 | single-source (K03) |
| Sleep doubled discovery of a hidden rule | Sleep 13/22 (59.1%) vs 5/22 (22.7%) in each wake group. chi2 = 8.54, df 2, P = .014. No-training controls 5/20 (25%) each, chi2 = 7.07, P = .029 | Wagner 2004 (a03, a04) | contested (K06) |
| Sleep onset (N1) tripled insight | N = 103. N1 20/24 (83.3%), wake 15/49 (30.6%), N2 2/14 (14.3%). Fisher P < .001 | Lacaux 2021 (b06) | contested (K07) |
| N2 nap, not N1, helps in a perceptual rule task | 68 analysed of 90. N2 24/28 (85.7%), N1 14/22 (63.6%), wake 10/18 (55.5%). N2 vs wake p = .038. N1 vs wake p = .75. BF N2>wake 8.19, N2>N1 24.71. Baseline no nap 49/99 (49.5%), with nap 48/68 (70.6%), p = .007 | Lowe 2025 (a09) | contested (K07) |
| No sleep or incubation effect on classic insight problems and magic tricks | N = 77. Magic tricks: sleep F = 0.047, p = .829; incubation F = 0.008, p = .930; about 1.40 extra tricks solved regardless. Classic problems: sleep F(1,73) = 0.641, p = .426; incubation F(1,73) = 0.131, p = .719 | Schoenauer 2018 (a07, b08) | contested (K06) |
| Nap did not help a long ill-defined problem | N = 40 randomised; no effect on quality or creativity | Holda 2020 (a08, abstract only) | single-source |
| REM nap raised primed RAT items | N = 77 over two experiments. NREM n = 6 per experiment. Primed items P = .04 or .047. Repeated items P = .67; new items P = .261 | Cai 2009 (a06) | single-source (K08) |
| Cueing sleepers with puzzle sounds raised cued solving | N = 57. 31.7% vs 20.5%, t(56) = 3.22, p = .002, dz = 0.47 | Sanders 2019 (b09) | contested (K09, K26) |
| Sleep helps a video-game insight challenge; cueing adds nothing | Exp 1: 62% vs 24% (N = 42). Exp 2: 56% / 58% / 57% across cue types | Beijamini 2021 (d09) | contested |
| Incubation gain only for problems seen before | N = 145. Exposure x incubation F(1,141) = 4.98, p < .01. Undemanding beat demanding, rest and none (all p < .01). Rest vs none p = .30. New problems p = .39 | Baird 2012 (b15) | contested (K05) |
| Baird pattern partly replicated, partly not | Du 2025 (N = 85, no control): repeated > novel on UUT fluency (p = .006, d = 0.30) but not CRA (p = .72). Teng and Lien 2022 (N = 90): mind wandering vs control p = 1.000; only mindfulness improved flexibility (d = 0.70, p = .023) | d07, d08 | contested |
| Preregistered writing replication | N 200 recruited, about 125-135 analysed. No break type raised creative improvement overall. Mind wandering predicted gain only for repeated prompts, and only on automated ratings (GPT-4 beta 6.76, p = .036; human ratings beta -1.39, p = .793) | Sci Reports 2025 (a16) | contested (K11) |
| Interactivity during retest changes incubation gain | Cheap necklace problem. Exp 1 N = 63: time 1 high 12/28 vs low 2/35 solved. Time-2 gains: low-low +14%, low-high +52%, high-low +3%, high-high +25% | Henok 2018/2020 (a17) | single-source; no no-gap control |
| Unconscious thought advantage on decisions did not replicate | N = 399. Accuracy 50.8/61.7% deliberation vs 55.4/65.1% distraction, p = .30. Meta-analytic g 0.15 (CI .03 to .26) fell to 0.018 (CI -.10 to .14) after trim-and-fill | Nieuwenstein 2015 (b17) | refuted (K10) |
| Steindorf replication mixed | N = 822, three experiments. Effect in two, lost when thoughts were probed | d12 | single-source (K25) |
| Immediate incubation on decisions | 92 decision studies, g = 0.224 (Strick 2011), as reported by Gilhooly | a12, b19 | revised down by b17 |

## 4. Mechanisms and models

This section is written so an engineer could implement the candidates. None is in the schema.

**4.1 Fresh-look reset (the only break-like operator that maps to an agent).**
- Trigger: the S6 impasse detector fires (no pass, two rounds with no change, same error twice, or budget fraction spent).
- Action: start a new context containing the original task and the original wording only. Drop the failed attempt text. Optionally keep a one-line list of approaches already failed.
- Budget: the reset attempt must come out of the same total token budget as the plain arm.
- Why it might help: fixation on a misleading cue decays (Smith, a14); a switch gives a fresh look (Segal, b12). The LLM analogue of fixation is that early tokens condition later tokens, which S3 already handles by fresh contexts per attempt.
- Evidence it may not help: at matched total tokens, continuing the same prefix beat restarting 9 of 9 on MATH with two small models, and only 1 of 178 cells was prefix-limited (d01, K22).

**4.2 Failure-log return (assimilation account).**
- Baird's gain appeared only for previously seen problems (K05). Agent analogue: after a break, the agent returns to the problem with a stored log of failed attempts and their failing outputs (already in G2 and S5), rather than a blank start.
- Implementation: store failed attempt summaries as short lines keyed to the item. On return, show the log after the task statement. Lessons are shown after the first attempt already (schema section 5).

**4.3 Cue resurfacing (targeted memory reactivation analogue).**
- Sanders 2019 replayed a sound tied to each unsolved puzzle in sleep. Agent analogue: at a later turn, re-present only the cue (the short problem tag) of items still unsolved from a stored log, versus leaving them alone (b09).
- Evidence is thin: one positive lab, one null on a different task (d09, K26). Do not build it on this evidence.

**4.4 Offline pre-computation (sleep-time compute).**
- Lin and Snell (2025): the model thinks about a stored context before any question arrives, then answers with less test-time compute. About 5x less test-time compute for the same accuracy on Stateful GSM-Symbolic and Stateful AIME. Scaling sleep-time compute lifts accuracy by up to 13% and 18%. Cost per query is 2.5x lower when one context serves many queries (c15).
- The gain widens as the question becomes more predictable given the context. Predictability is the log-probability of the question given the context under Llama2-70B, binned in five quantiles. No threshold is given (d05).
- Implementation: needs a stable stored context and repeated queries about it. Otherwise no gain (K16).

**4.5 Entropy-gated reconsideration.**
- d'Aliberti and Horta Ribeiro (2026): after a first generation, if sequence entropy is in the top 20%, run a second pass with a cue such as "Wait, something is not right, we need to reconsider". Math accuracy went 0.322 to 0.406 (+8.41pp, N = 320,000 paired samples, Table 5). An appendix table gives 32.70% to 40.43% (+7.74pp, N = 464,000). The high-entropy bucket went 19.70% to 35.09% (+15.38pp) (b26, c12, d03). Critique note: Table 5's +8.41pp is the overall second-pass result; the entropy gate is a separate stratified analysis.
- Needs logit access. A second pass is a full extra generation, so it is not an equal-token result.
- Fits G1: doubt only on a signal. Entropy is a signal; a schedule is not.

**4.6 Spontaneous "aha" shifts are not insight.**
- Mid-trace shifts are rare (6.31% of traces overall) and mostly harmful. Shifted traces were 2.57% accurate vs 16.44% unshifted for Qwen2.5-1.5B in that analysis (N = 723,200). The formal detector fires on 1.79% of samples. Shifts did not grow with training (c11, b25).
- Rule: do not credit a trace for saying "wait". Judge change by the output (G10).

**4.7 Cognitive models of incubation.**
- CLARION (Helie and Sun): explicit rule module plus implicit associative module. During incubation only the implicit module runs, spreading activation. A solution surfaces when the implicit result passes a confidence threshold and is integrated with the explicit module (a21, c18). The model predicts that a distractor that loads the implicit module should hurt incubation. A human free-recall experiment (114 students, six groups of 19) found an incubation effect, F(5,108) = 10.65, p < .001 (c18). Fit statistics were not read.

## 5. What holds up

**Holds up (human).**
- A break after impasse gives a small average gain, d = 0.29, with large heterogeneity (b01). Dodds et al. 2003 counted 29 of 39 experiments with an effect (c18). The effect is not zero, and it is not large.
- Larger effect for divergent thinking than for linguistic or visual insight problems (b04).
- The break is more likely to help when preparation was longer (b04, single-source, correlated moderators).

**Does not hold up, or is contested.**
- Unconscious thought on decisions: the large replication found nothing (N = 399), and the bias-corrected meta-analytic g fell to 0.018 (b17). Steindorf (N = 822) found the effect in two of three experiments and lost it with thought probes (d12). Caveat: the paper's footnote says trim-and-fill does poorly under selective reporting, so 0.018 is a correction, not a final truth (critique).
- Sleep for insight: positive in Wagner 2004 and Lowe 2025, null in Schoenauer 2018 (classic problems and magic tricks), Holda 2020 (long problem), and a null on cueing (Beijamini 2021).
- Sleep stage: Lacaux says N1 only; Lowe says N2 and finds no N1 benefit (BF N1>wake 1.19). Stage groups are not randomised; cells are small (N2 n = 14 in Lacaux, N1 n = 22 in Lowe). Treat stage specificity as unresolved (K07). Lowe's wake group (55.5%) is close to its no-nap baseline (49.5%), so the result rests on a post hoc N2 subgroup.
- REM nap benefit (Cai 2009): NREM n = 6 per experiment. Schoenauer's naps had only 10-17 min REM and no effect (K08).
- Filler demand: Sio and Ormerod and Baird favour low demand; Segal found no demand effect (K04).
- Mind wandering as the mediator: weak or absent in Teng and Lien 2022 and in the 2025 preregistered study (K11).
- Retest gains are confounded with a second try (b21, a17, d07).

**Moderators that appear in the data.**
- Task type (association vs restructuring): Schoenauer argues incubation may help RAT-like tasks via spreading activation but not tasks needing a changed representation (b22).
- Repeat exposure (Baird; Du 2025 partly).
- Cue similarity: a break task in a different modality helped divergent thinking more than a similar one, against beneficial forgetting (b14).
- Interactivity of the retest context (Henok, a17).
- Fixating information in cueing studies (d10, unread, 403).

**Interventions that worked (small, single-lab, human).** Undemanding break (Baird); N2 nap (Lowe); sleep onset (Lacaux); sleep after training (Wagner).

**Interventions that did not work.** Demanding break; rest alone; sleep on classic insight problems; cueing in Beijamini 2021; unconscious thought for decisions at scale.

**Bias flag.** Sio and Ormerod's funnel test looked symmetric (beta .08, p = .41), but the same kind of test missed bias that trim-and-fill found in unconscious thought. Do not read d = 0.29 as bias-free (critique, contradiction 6).

## 6. Language models

**There is no direct test.** Three agents searched independently, plus a gap search. No study varies an incubation delay, break or distractor in an LLM and compares with humans (a26, b30, c24, K13). The APIs were rate-limited, so absence is probable but not proven.

**Nearest tests (all adjacent, none on incubation).**

| Study | What it tests | Numbers | Reads on incubation as |
|---|---|---|---|
| Bulut 2026 (d01, d16) | Continue prefix vs restart at matched tokens, MATH, two small 4-bit models (Gemma-4 E4B, Ministral-3 3B), 178 cells | Continue beat restart 9 of 9 at exact match. 1 of 178 cells prefix-limited. A larger restart budget reached the same threshold in 11/13. Ministral 3B: 0 to 79% of unsolved solved as restart budget grew; Gemma flat | No sign a reset helps. "Breakthroughs" are mostly compute compression |
| Bulut 2026 (d02) | Early-trace probes that predict success | Trace-blind difficulty proxy AUROC 0.873 on 192K R1 generations. Within-problem accuracy 0.496 (chance) | A stuck detector must be checked within problem, against a question-only baseline |
| d'Aliberti and Horta Ribeiro 2026 (c11, c12, d03) | Aha shifts and forced reconsideration | See 4.5 and 4.6. Crosswords +0.45pp, Rush Hour +0.01pp. Qwen2.5-7B +5.97pp, Llama 3.1-8B -4.19pp on a MATH subset. GPT-4o shifts 0.88-2.21%, R1 0.00-0.25% (math only) | Forced reconsideration helps on math when entropy is high; no equal-token baseline; small models |
| Yang 2025 (c14, d04) | Aha by linguistic markers | Reports reasoning-collapse rates over 200 samples per difficulty level; no accuracy effect size | Marker-based; conflicts with the d'Aliberti definition |
| Kang 2025 (c13) | Reflection after first answer | Eight reasoning models, five math sets. Truncating after the first candidate saved 24.5% of tokens for under a 2.9% accuracy drop | Reflection is mostly confirmatory |
| Lin and Snell 2025 (c15, d05) | Sleep-time compute | About 5x less test-time compute; up to +13% and +18% | Closest machine analogue, needs predictable questions |
| IdleSpec 2026 (c16, c17, d06) | Idle-time planning for agents | Vanilla / sleep-time / IdleSpec on GAIA+FRAMES: Gemma4-E4B 30.9 / 31.0 / 35.5; Qwen3.5-4B 33.2 / 29.4 / 40.0; Gemini-2.5-Flash 50.5 / 50.1 / 55.6. MLE-Bench Lite gold 18.2% vs 13.6% sleep-time | Sleep-time baseline did not carry to tool agents; authors' own baseline, may be under-tuned |

**Insight-style accuracy of LLMs depends on the benchmark.**

| Benchmark | Result | Source |
|---|---|---|
| Chinese RAT, 61 humans, 30 items | GPT-3.5 +0.19, GPT-4 +0.26, GPT-4o +0.35 over humans, all p < .001 | c01 |
| Chinese character puzzle, stumper | Humans above GPT-3.5 and GPT-4 on both; GPT-4o above humans (+0.21 on character puzzle, +0.06 on stumper, p = .011) | c02 |
| Rebus | GPT-4-turbo +0.32, GPT-4o +0.39 over humans | c02 |
| Representational-change choice task | Humans above GPT-4-turbo by 0.46 (CI .41-.51) and GPT-4o by 0.31 (CI .25-.36). Humans used transformation 72.41%; models used step-by-step reasoning 68.88% (GPT-4o), 71.26% (GPT-4-turbo) | c03 |
| 30 verbal insight problems, 20 humans | ChatGPT at about typical human rate | c05 |
| Psychometric battery, 5 insight problems | GPT-3.5 1.5 to 3.5 of 5 over four runs; GPT-4 4.5 of 5 on one run; humans 44-61% per item; analytic problems 0 correct. Large run-to-run variance | c06 |
| Stumpers | 81 humans 38.15%; GPT-3.5/4 57.8% (43.4% enhanced set); Davinci 29.6% | c07 |
| Stumper verification | Humans 100% when they had generated the right answer, 63.8% when not; models averaged 41%, below chance | c07 |
| NazoNazo Japanese riddles (201 items, 38 models) | Humans 52.9% (CI 46.6-59.2, n = 126, 120 items); non-reasoning 7.6%; reasoning 17.6%; odds ratio 2.29 (1.99-2.64); 9.42% vs 19.25% on all 201 items. GPT-5 inside the human CI (not formally tested). Verification failures 5 to 39% of wrong answers. Few-shot reasoning demos raised accuracy in all four tested models, significant in two | c08, c09, c10 |
| Only Connect walls (494) | Best GPT-4 10-shot connection F1 about 41-45% vs about 80% humans. Models solve far more when red herrings are removed | c21 |
| Riddle Riddle | Nine LLMs: 84.9% genuine riddles vs 50.7% riddle-like literal problems; humans 50.5% vs 80.5%. 90.8% of LLM errors were inventive overreach | d14 |

Take-away: older models trail on some insight tasks, newer ones lead on others. Contamination and language are open confounders (K18). Models that write the right candidate and then do not pick it are common (NazoNazo; the S4 harvest step in the schema covers the first half). Verification, not generation, is the weak step (K17).

**RAT is a weak proxy.** Across 55 instruction-tuned LLMs, RAT validity against creative-writing benchmarks was r = +0.62, +0.44, +0.51, but fell to +0.08 to +0.28 (not significant) after controlling for general capability. Combinatorial creativity r = +0.58 fell to +0.14 (c22). Do not use RAT alone as an insight proxy (K19).

**Humans using LLMs.** In two preregistered experiments (N = 1,100), LLM help raised performance while on but did not improve later unassisted creativity. On convergent RAT, guidance lowered accuracy by 10.6 points vs no LLM (95% CI -18.6 to -2.7, p = .005); answer-giving did not (p = .682) (a23). This is human-LLM interaction, not agent incubation (K20).

**Theory and proposals without data.** Polyak and Balkhyoor 2026 argue prompt use skips a pre-verbal associative phase (a24). Gwern's "LLM Daydreaming" proposes a background loop of random concept pairs with a critic; no experiments (c23). Dream-COP replays past search trajectories (listing only, c27).

## 7. What our agent should take

Status: [E] established, [S] single-source, [C] contested. Schema part in the second column.

### Add now (established)

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Keep "incubation by distraction" in 4b as not to add | 4b | [E] | b17, b02, K10 |
| Do not credit a trace for saying "wait" or "aha"; judge change by the output | G10 | [E] (already in schema) | b25, c11 |
| Verify with code or a held-out check, not the model's own endorsement | G2, G3 | [E] | c07, c08, c09, K17 |
| Doubt only on a signal; no scheduled break or reflection | G1 | [E] (already in schema) | c13, c12, K15 |
| Use fresh, post-cutoff items for any insight test; do not use RAT alone | S0 (bench design) | [E] | c22, c06, K18, K19 |

Nothing new needs to be added to SCHEMA.md from this subfield. The established findings reinforce existing rules.

### Test first

| Item | Schema part | Status | Evidence ids |
|---|---|---|---|
| Context reset at impasse that drops the failed text but keeps the problem, at equal tokens vs one long pass | S6, O6 | [S] | d01, d16, a14, b12, K12, K22 |
| Failure-log return vs blank restart after impasse | memory, S5 | [C] | b15, d07, d08, K05 |
| Entropy- or check-gated reconsideration cue at equal tokens | G1, G11 | [C] | b26, c12, d03, c13, K15 |
| Literal-reading check inside any reframe step | G3, O8 | [S] | d14, K24 |
| Stuck detector evaluated within problem against a question-only baseline | S6 | [S] | d02, K23 |
| Cue resurfacing of unsolved items from a log | memory | [C] | b09, d09, d10, K09, K26 |
| Offline pre-computation on a stored context with repeated queries | memory | [C] | c15, c17, d06, K16 |
| Code or independent-sample verification vs model self-verification on riddle items | G3, G4 | [S] | c08, c09, d14, K17 |

## 8. Concrete tests on our bench

All arms use equal total tokens, set by the plain arm. Score by code. Use post-cutoff or self-written insight items so contamination is low.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Riddle and insight items with a code-checkable answer (self-built from NazoNazo-style and matchstick-style items), where plain pass rate is 10-60% | A: one long pass. B: short pass, S6 fires, new context with task only, remaining tokens | Pass rate at final answer, paired by item | Near zero or negative (d01). Add only if B beats A by 5 points or more |
| T2 | Same items | A: reset with blank slate. B: reset plus one-line failure log | Pass rate | Small gain for B (Baird assimilation account), if any |
| T3 | Math or puzzle items with logit access | A: one pass at 2x length. B: pass, then reconsideration cue only when entropy is in the top 20% or a check fails, same total tokens | Pass rate; tokens per solved item | Unclear; d'Aliberti did not match tokens. Gain only if B wins at matched tokens |
| T4 | Riddle-like items with literal answers | A: reframe step without literal check. B: reframe plus literal-reading check by code | Pass rate on literal items; false-reframe rate | Fewer inventive-overreach errors (84.9% vs 50.7% gap, d14) |
| T5 | Items with a known difficulty label | Stuck detector scored within problem vs a question-only difficulty baseline | Within-problem AUROC | Chance (0.496 in d02) unless our detector is better |
| T6 | Multi-turn sessions with repeated items still unsolved | A: no resurfacing. B: resurface item tag from log at a later turn | Solve rate on cued vs uncued items | Small (dz 0.47 in humans, one lab); likely null |
| T7 | Repeated queries about one stored document | A: answer cold. B: sleep-time pre-computation of the context | Accuracy and total tokens per query | Gain only if questions are predictable (c15); skip otherwise |
| T8 | NazoNazo-style riddles | A: model picks among its own candidates. B: code-checked selection or independent sample | Verification-failure rate (right candidate written, wrong one chosen) | Lower failure rate (5 to 39% of wrong answers, c09) |

## 9. What does not transfer, and why

- **Sleep.** No agent analogue. Sleep-stage results are contradictory anyway (K07).
- **Time passing.** An LLM has no state that decays between turns. Forgetting of misleading cues (Smith) would have to be forced by dropping text. That is a context edit, not a break.
- **Mind wandering and filler tasks.** The mechanism is human attention. An agent has no idle attention to redirect. Filler tokens spend budget.
- **Unconscious thought for decisions.** Refuted at scale in humans (K10) and already in 4b.
- **Aha moments.** The feeling has no meaning in a token stream. Marker words do not track strategy change (c11).
- **Dreams and lucid dreaming.** No analogue (a10, abstract only).
- **Pupil dilation as an effort marker.** No analogue (a25).
- **Human-LLM interaction studies.** About human creativity after LLM exposure, not about an agent (a23, K20).
- **Press-level CLARION numbers (35.3%, 45.3%).** Unverified; not usable (c19).

## 10. Open questions

1. Does a break or context reset at equal tokens help on insight items (not MATH) for frontier reasoning models? No study exists (K13, gap 1).
2. Does d'Aliberti's +8.41pp survive a token-matched baseline, and does it hold for frontier models? Open (gap 2).
3. Does an output-change definition of aha give a different picture from marker-based definitions (Yang 2025 vs d'Aliberti)? Not tested (gap 3).
4. What predictability threshold makes sleep-time compute pay? No threshold given; tool-agent baseline gave none (gap 4).
5. Does Baird's repeat-exposure dependence replicate on true insight problems with a no-gap control? Open (gap 5).
6. Is Lacaux N1 or Lowe N2 right, or neither? No randomised or larger stage test (gap 6).
7. Segal 2004 sample sizes and effect sizes are unknown; only the verbal description via Gilhooly was seen (gap 7).
8. Is there any insight-task replication of unconscious thought, and what did Weisberg 2015 and Bowden 2005 report as null results? Not found (gap 8).
9. Does the Sanders cueing effect replicate outside one lab? One null (Beijamini) and one follow-up with a moderator (unread) (gap 9).
10. Does verification moved to code or an independent sample cut verification failures at equal tokens? No study (gap 10).

## 11. Sources

[V] opened and read this session. [M] snippet, abstract or second-hand only.

**Founding and reviews**
- [V] Gilhooly (2016) Incubation and creative problem solving, Frontiers in Psychology 7:1076. https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660 (a01, a02, a12, a14, a18, a20, b10-b14, b19, b20, d11)
- [M] Wallas (1926) The Art of Thought; Poincare (1910); via Gilhooly. Same URL.
- [V] Sio and Ormerod (2009) Does incubation enhance problem solving? A meta-analytic review. https://www.Gwern.net/doc/psychology/writing/2009-sio.pdf (b01-b04)
- [M] Segal (2004) Incubation in insight problem solving, Creativity Research Journal 16:141-148. Via Gilhooly, URL above.
- [M] Smith (1995), Smith and Blankenship (1991). Via Gilhooly.
- [M] Dijksterhuis and Nordgren (2006); Dijksterhuis and Meurs (2006); Strick et al. (2011); Hassin (2013). Via Gilhooly and Europe PMC. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22unconscious%20thought%22

**Sleep and insight**
- [V] Wagner et al. (2004) Sleep inspires insight, Nature 427:352-355. https://pages.ucsd.edu/~achiba/SleepInsightWagnerNature04.pdf
- [V] Cai et al. (2009) REM, not incubation, improves creativity. https://pmc.ncbi.nlm.nih.gov/articles/PMC2700890 ; abstract record [M] https://ui.adsabs.harvard.edu/abs/2009PNAS..10610130C
- [V] Schoenauer et al. (2018) Sleep does not promote solving classical insight problems and magic tricks. https://pmc.ncbi.nlm.nih.gov/articles/PMC5834438
- [M] Holda et al. (2020) Ill-defined problem solving does not benefit from daytime napping. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Ill-Defined%20Problem%20Solving%20Does%20Not%20Benefit%20From%20Daytime%20Napping%22
- [V] Lacaux et al. (2021) Sleep onset is a creative sweet spot. https://pmc.ncbi.nlm.nih.gov/articles/PMC8654287
- [V] Lowe, Petzka, Tzegka, Schuck (2025) N2 sleep promotes the occurrence of aha moments. https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3003185 ; conference version https://2024.ccneuro.org/pdf/29_Paper_authored_CCN_2024.pdf
- [M] News summary of Lowe 2025. https://www.news-medical.net/news/20250630/N2-deep-sleep-powers-your-next-aha-moment-study-reveals.aspx
- [V] Sanders, Osburn, Paller, Beeman (2019) TMR during sleep improves problem solving. https://faculty.wcas.northwestern.edu/paller/PsychSci2019.pdf
- [V] Beijamini et al. (2021) Sleep facilitates problem solving. https://pmc.ncbi.nlm.nih.gov/articles/PMC7965947
- [M] Sleep, TMR and fixating information follow-up (2021). https://informahealthcare.com/doi/full/10.1080/20445911.2021.1912050 (HTTP 403)
- [M] Konkoly et al. (2026) Creative problem-solving after provoking dreams. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Creative%20problem-solving%20after%20experimentally%20provoking%20dreams%22
- [M] Cordi and Rasch (2021), Brodt et al. (2018), as cited in Lowe 2024 (CCN URL above).

**Mind wandering, interactivity, unconscious thought**
- [V] Baird et al. (2012) Inspired by distraction. https://www.cmhp.ucsb.edu/sites/default/files/2018-12/Baird%20et%20al.%20%282012%29%20Inspired%20by%20distraction.pdf
- [V] Preregistered 2025 Scientific Reports writing study. https://pmc.ncbi.nlm.nih.gov/articles/PMC12241419/
- [V] Du, Gordon, Tolmie (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12190454/
- [V] Teng and Lien (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9053813/
- [V] Henok et al. (2020) Incubation and interactivity. https://pmc.ncbi.nlm.nih.gov/articles/PMC6994426
- [V] Nieuwenstein et al. (2015). https://journal.sjdm.org/15/15516/jdm15516.pdf
- [V] Steindorf, Rummel, Boywitt (2021). https://www.frontiersin.org/articles/10.3389/fpsyg.2021.545928/pdf
- [M] Macchi et al. (2026) pupil dilation. Europe PMC search link as above.

**Models**
- [M] Helie and Sun (2010) unified theory. https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=%22Incubation%2C%20insight%2C%20and%20creative%20problem%20solving%22%20AND%20Helie ; press https://www.sciencedaily.com/releases/2010/12/101201124345.htm
- [V] Helie, Sun, Xiong (2009) Mixed effects of distractor tasks. https://ccn.psych.purdue.edu/papers/pp772-helie.pdf

**Language models**
- [V] Nair, Gizzi, Sinapov (2024) Creative problem solving in large language and vision models. https://arxiv.org/pdf/2405.01453 (Gizzi 2022 [M] via this)
- [V] Zhang et al. (2025) AI delivers creative output but struggles with thinking processes. https://arxiv.org/pdf/2503.23327 (Raz 2024 [M] via this)
- [V] Kumar et al. (2025) Human creativity in the age of LLMs. https://arxiv.org/html/2410.03703v2
- [V] Polyak and Balkhyoor (2026) Before the Prompt. https://computationalcreativity.net/iccc26/papers/ICCC26_paper_134.pdf
- [V] d'Aliberti and Horta Ribeiro (2026) The illusion of insight in reasoning models. https://arxiv.org/pdf/2601.00514
- [V] Mizumoto et al. (2025) NazoNazo. https://arxiv.org/pdf/2509.14704v2 ; summary page [M] in d15
- [V] Kang et al. (2025) First Try Matters. https://arxiv.org/pdf/2510.08308
- [V] Yang et al. (2025) Understanding aha moments. https://arxiv.org/pdf/2504.02956
- [V] Lin, Snell et al. (2025) Sleep-time compute. https://arxiv.org/pdf/2504.13171
- [V] Choi et al. (2026) IdleSpec. https://arxiv.org/pdf/2605.22154
- [V] Bulut (2026) It's the problem, not the path. https://arxiv.org/pdf/2609.03436
- [V] Orru et al. (2023) Human-like problem solving in LLMs using ChatGPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637/
- [V] Speed (2023) caution against anthropocentric benchmarks. https://arxiv.org/pdf/2309.07683
- [V] Goldstein et al. (2023) Decoding Stumpers. https://aclanthology.org/2023.findings-emnlp.779.pdf
- [V] Alavi Naeini et al. (2023) LLMs are fixated by red herrings. https://arxiv.org/pdf/2306.11167
- [V] Schapiro et al. (2026) Do semantic distance tests predict creativity? https://arxiv.org/pdf/2605.13450
- [V] Fascendini et al. (2026) The Riddle Riddle. https://arxiv.org/pdf/2606.27103
- [V] Gwern (2025) LLM Daydreaming. https://gwern.net/ai-daydreaming
- [M] Dream-COP (2026) listing only. https://arxiv.org/search/?query=insight+problem+solving+LLM&searchtype=abstract

**Links to other subfields in this run (not covered here).** Insight neural signatures; Constraint satisfaction; Process stage models and incubation (A09); Dual-process and three-process accounts; Targeted memory reactivation; Retrieval as consolidation; Cognitive control and creativity.

## Source audit (2026-11-20)

Fresh auditors re-opened the sources of 3 established claims: 3 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

