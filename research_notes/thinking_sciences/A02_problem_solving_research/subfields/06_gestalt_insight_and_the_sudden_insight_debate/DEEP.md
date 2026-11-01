# Gestalt insight and the "sudden insight" debate: deep document

*Subfield A02.06. Built from evidence_a-d.jsonl (a01-a28, b01-b25, c01-c26, d01-d24), claims.jsonl (K01-K41) and critique.md in this folder. Evidence ids are in brackets. Where a number comes from a review or a citing paper (not the primary), it is marked second-hand.*

## 1. What it is

Insight research asks one question. When a person is stuck on a problem and then suddenly sees the answer, is something special going on? Or is it ordinary search that only feels sudden?

Three terms matter.

- **Impasse.** The solver has tried the obvious moves and has no next move.
- **Restructuring.** The solver changes how the problem is represented. A constraint is dropped, a chunk is split, an object gets a new role. The old frame is replaced, not searched harder.
- **Aha.** The feeling that goes with the solution: pleasure, suddenness, certainty (a09).

The debate has two camps.

- **Special-process.** Gestalt psychology and Ohlsson's representational change theory (RCT). Restructuring is a distinct step. The full solution may arrive as a whole (a01, a05).
- **Nothing-special.** Kaplan and Simon (1990), MacGregor, Ormerod and Chronicle (2001). Insight problems are ordinary search in a huge or badly framed space. Better salience and a progress monitor are enough (a16, a17).

Most authors now favour a mix. Salmon-Mordekovich and Leikin say "unequally integrated" (b07). Nothing here settles it.

For our agent this is background. It gives us one operator (restructure), one state (impasse) and several rules about trust in a sudden, confident answer. It does not give a mechanism proven to beat plain sampling.

## 2. History and theories in depth

**Gestalt era (1910s to 1945).**
- Wertheimer (1925, 1945, "Productive Thinking") set the contrast between reproductive thinking (apply old habits) and productive thinking (restructure the whole). Second-hand via a01. No primary numbers were opened.
- Kohler (1925) described a chimpanzee that saw crates as building blocks. The animal looked, paused, then acted. Taken as the founding case of sudden "seeing" (a01).
- Duncker (1945) introduced functional fixedness. An object used in its usual role is hard to see in a new role. The candle problem is the best-known case. Duncker's original numbers were not obtained (critique, weak spots).
- Maier (1931) two-string problem and Scheerer (1963) belong to the same family. Not opened.

**Information-processing era (1960s to 1990s).**
- Metcalfe and Wiebe (1987) tried to measure suddenness. People rated "warmth" (closeness to the answer) at intervals. On algebra, warmth rose gradually. On classic insight problems, warmth stayed low and then jumped [d22, a02, b18]. The primary shows small effects (section 3).
- Kaplan and Simon (1990) argued insight is search over a problem space whose crucial features are not salient. Raising salience shrinks the space (a17).
- Ohlsson (1992) built RCT. A wrong initial representation causes an impasse. Three mechanisms break it: constraint relaxation, chunk decomposition, re-encoding. Activation spreads from working memory and retrieves new elements. Ohlsson also wrote that the sudden appearance of the complete solution may be an illusion of limited introspection (a05, b15). This is the quote in our SUBFIELDS row.
- Knoblich, Ohlsson, Haider and Rhenius (1999) tested RCT on matchstick arithmetic. Problems that need a stick taken from an operator are harder than ones that need a stick from a number. Breaking a tight perceptual chunk is harder than breaking a loose one (a06).
- MacGregor, Ormerod and Chronicle (2001) modelled the nine-dot problem as maximization plus progress monitoring. Each move should connect as many dots as possible. A look-ahead check of lines left versus dots left flags failure and pushes search outside the grid (a16).
- Sternberg and Davidson's three-process theory (selective encoding, combination, comparison) is in the SUBFIELDS row. It was not researched in this pass.

**Aha as a measured experience (2010s on).**
- Danek and Wiley (2017): the Aha has three core parts and occurs with wrong answers too (a09, b03).
- Webb, Little and Cropper (2016): insight is a solver state, not a task type (b04).
- Wiley and Miller (2026): Aha is a metacognitive judgment inferred from cues, not a readout of restructuring (a20).
- Becker, Wang and Cabeza (2024): Aha tracks a prediction error about solvability (b10).

**Dynamics and measurement (2018 on).**
- Bilalic et al. (2019) and Graf et al. (2023) argue that the verdict "sudden or gradual" depends on the statistic used (b01, b02).

**The LLM era (2025 on).**
- DeepSeek-R1 reported an "aha moment" as a rise in the word "wait" (a25). Later papers tested whether it does anything (section 6).

## 3. Core findings with exact numbers

Status: **E** established (two or more independent sources agree), **S** single source, **C** contested.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Warmth jumps late on insight problems (original claim) | Exp 1: 26 recruited, 19 usable; correlations .26 (t(18)=2.02) and .23 (t(18)=1.63, one-tailed). Exp 2: 73 students, 39 usable for warmth. Second-hand: 76% of correct and 52% of wrong solutions followed a sudden jump | Metcalfe and Wiebe 1987 [d22, b18, a02] | C. Small, partly one-tailed |
| Warmth pattern absent with self-reported insight | N=51, 971 trials, 29% reported as insight. Warmth no different; insight answers more accurate and more confident | Hedne et al. 2016 [d23] | C. Different task |
| Individual restructuring mostly incremental on matchsticks | Problem B, first 5 min, 26 solvers: 54% incremental, 27% sudden, 19% unclear | Bilalic et al. 2019 [b01] | C |
| Magic tricks: few solutions show a sudden change | 14% sudden, 10% incremental, rest flat or zigzag (second-hand) | Danek et al. 2018 [b12] | C |
| Triangle of Circles: more sudden | 68% sudden, 32% incremental (second-hand) | Cushen and Wiley 2012 [b11] | C |
| Change-point models find an abrupt gaze shift near the 90% bin; ANOVA smears it | 34% solved unaided, +11% after hint. The "sudden" figure is simulated; the real data are gradual | Graf et al. 2023 [b02, a08] | C. Methods paper |
| Late gaze shift to the crucial element in solvers | Shift in the last third of solving time (about 5 min per problem) | Knoblich et al. 2001; Bilalic 2019 [a07, b01] | E |
| Hidden gradual build-up before the answer | Relatedness ratings rise toward the solution; anagram solvability judged within 250 ms, better with more time | Durso 1994; Novick and Sherman 2003 [a03, a04, b13, b14] | C. Smith and Kounios 1996 did not replicate |
| Felt Aha is linked to correctness on average | Correct M=66.5 (SD 18.4) vs wrong M=52.3 (SD 18.8), t(69)=10.21; N=70, 35 tricks, 1778 solutions | Danek and Wiley 2017 [a09, b03] | E |
| Many wrong answers also feel like Aha | 37% (417 of 1124) of wrong solutions had Aha above the correct mean | Danek and Wiley 2017 [b03] | E |
| Self-labelled insight answers are more accurate | d=0.99 and 0.74 (Exp 1), 1.50 and 0.51 (Exp 2), 0.66 and 0.39, 1.85 and 1.24 | Salvi et al. 2016 [b05] | E |
| Aha-accuracy correlation by task | Exp 1: insight r=.50, CRA r=.41, non-insight r=.02. Exp 2 (feedback): .495, .39, .19 | Webb et al. 2016 [b04] | E |
| Aha follows cues, mainly a correct first move | 377 students, 1164 trials analysed; F(1,1091)=112.17; partial R2=.09 (CI .06 to .12) | Wiley and Miller 2026 [a20] | S |
| Relaxing a constraint is not enough (ten-penny) | Control 3/30 (10%), line hint 2/29 (7%), intersection hint 6/28 (21%), maximization hint 21/29 (72%); chi2(1,59)=23.80, phi=.64 | Oellinger et al. 2017 [a15] | E |
| Key hints on the nine-dot do not reliably help | No figures in the secondary source | Weisberg and Alba 1981; Kershaw 2013 [a18] | E |
| Re-depicting the problem helps; handling objects does not | Pencils 27.3% (12/44) vs 32.6% (14/43), p=.59. Matchstick picture 46.7% (14/30) vs 79.3% (23/29), p=.010, V=.337 | Macchi et al. 2026 [b09] | S |
| Verbalising hurts a reinterpretation problem, helps a procedural one | Insight 57% vs 13%; non-insight 30% vs 80% | Macchi et al. 2025 [b08] | C |
| No overshadowing on verbal CRAs | 0.42 (N=26 silent) vs 0.40 (N=27 aloud), p=.51 | Chein and Weisberg 2014 [d18] | C |
| Sleep or incubation does not help | N=77; incubation F(1,64)=0.008, sleep F(1,64)=0.047; initial solve rates matchstick 45.5%, nine-dot 6.0%, eight-coin 8.0% | Schoenauer et al. 2018 [b06] | C. Sio and Ormerod meta-analysis (not opened) reports a small positive effect |
| Insight problems are not that special | 88.5% of correct "insight" solves rated as insight, yet only 7.97% had an impasse | Salmon-Mordekovich and Leikin 2023 [b07] | C |
| Pre-use blocks new use (Duncker effect) in children | 6-7 year olds 18% box solution after pre-use vs 89% without; 5 year olds 64% vs 65%; 60 children | German and Defeyter 2000 [d24] | S |
| Sudden switches arise in plain networks | 46/99 networks vs 49/99 humans steeper than control; none at zero update noise | Loewe et al. 2024 [c24] (with a22) | E |
| Spontaneous "wait" shifts in LLMs are rare and go with lower accuracy | 6.31% of traces; 2.57% vs 16.44% correct, N=723,200; formal Aha 1.79% | d'Aliberti and Ribeiro 2026 [c01, c02] | E for direction |
| A forced reconsideration pass helps maths | MATH-500 32.2% to 40.6% (+8.41pp; 50,574 fixed vs 23,500 broken); crosswords +0.45pp; Rush Hour +0.01pp. Compute doubled | d'Aliberti and Ribeiro 2026 [c05] | S |
| R1-Zero "aha" is already in the base model | DeepSeek-V3-Base-685B emits "Aha"/"wait" on 500 MATH items; reflection not positively correlated with accuracy | Liu et al. 2025 [a26, c13] | S |
| VLM aha moments rarely help | 8.3% of responses; best-of-N with self-verification down to -16.7% | Wu et al. 2025/26 [b19, c15] | S |
| Insight-type riddles stay hard for LLMs | NazoNazo subset: human 52.9%; non-reasoning 7.6%, reasoning 17.6% | Mizumoto et al. 2025 [c07] | S |
| Right answer written, then rejected | 5.23% to 39.34% of wrong answers (four models, string match) | Mizumoto et al. 2025 [c08] | S |
| Lateral puzzles: models far below humans | BRAINTEASER 53% and 63% vs human 92%, random 25% | Jiang et al. 2023 [b23, c19] | E |
| Reworded twins expose memorisation | ChatGPT fails 45% of originals whose context twin it solves; over 80% of SemEval entries drop on twins, up to 0.28 and 0.34 | Jiang 2023, 2024 [c19, d21] | E |

## 4. Mechanisms and models

Each is written so an engineer could build it.

**4.1 RCT as an operator set (K01).**
- State: impasse detected, with a record of which problem elements the last k steps named.
- Operators, cheapest first: (a) relax a constraint (drop one condition, ask "what if not?", our O4); (b) decompose a chunk (O3); (c) re-encode in another form (O6).
- Order by tightness. Items that need a tight constraint or chunk loosened are the hard ones (a06). Try loose constraints first.
- Pair every operator with a search criterion (4.2).

**4.2 Maximization plus progress monitor (a16, a15).**
- Criterion: each move should cover as much of the goal as possible.
- Monitor: with look-ahead, compare moves left with goal parts left. If the count cannot close, mark the frame failed and fire the restructure operator.
- Look-ahead 2 flags failure earlier than look-ahead 1.
- Why it matters: in ten-penny, the relaxation hint alone gave 7% to 21%. Adding the criterion gave 72% (a15). An operator without a criterion is not enough.

**4.3 Stall detector from stuck focus (K03).**
- Keep a counter of how often each named problem element appears in the reasoning.
- If the same elements are named for N steps and no new candidate appears, call it a stall.
- Require some depth on the current line first. Too much thought-switching goes with wrong answers (d08: wrong responses had 418% more thought switches).
- Trigger candidates, untested head to head (K33): same-element stall, entropy spike (d10), sample disagreement, cheap solvability probe.

**4.4 Latent-progress probe (K35, d01, d04).**
- At fixed token checkpoints, stop the trace and force an answer. Record the answer distribution.
- Human analogue: Durso's relatedness ratings. LLM evidence: accuracy and commitment rise with trace depth (GPQA Diamond 30.8-42.3% at decile 0 to 49.0-73.1% at the end; d01). Hidden-state probes give ROC-AUC over 0.9 on AIME (d04).
- Use: a flat probe means no progress; a rising probe means keep going. Per-trace jump versus ramp is unmeasured (K34).

**4.5 Change-point test (K02).**
- Fit a one-jump model and a linear model to per-step progress. Compare. Do not average over runs; averaging turns a jump into a ramp (b02).

**4.6 Model reduction view (a22).**
- Impasse is a state of high uncertainty over rules. A model-reduction step prunes candidate frames and produces a jump in behaviour and confidence. In the simulation, the agent without reduction inferred the rule at trial 33 and was certain by trial 35.
- Engineering reading: keep a list of candidate frames with weights. Insight is the step where most are dropped at once.

**4.7 Silent-gate view (c24).**
- A hidden variable can be learned slowly and used only after a gate opens. Behaviour then looks sudden.
- Engineering reading: before a full restructure, run a cheap probe of the hidden hypothesis. The probe may open the gate.

**4.8 Verification gate (K06, K30, K36).**
- Any sudden, confident answer goes through a check against the original problem text. The check result must change the output. A verbal check that cannot change the answer is decorative (d07: over 30% of steps in Kimi-K2.6, nearly 60% in Qwen3.6-35B are decorative).
- Add an endorse-or-reject call for every candidate that appeared earlier in the trace (c08, d04, d08).

**4.9 Restart versus patch (K37).**
- Wrong prefixes anchor later steps (d12; d01: 13-32% less anchoring when the stronger model continues freely).
- Restart from a short summary of verified facts. The pilot (d16: 4 of 5 wins vs 2 of 5; 22.6 vs 28.6 questions) is too small to rely on.

## 5. What holds up

**Holds up.**
- Insight is a solver state, not a problem type (K12: b04, b07, a20).
- Felt insight is a partial signal. Insight answers are more often right (d up to 1.85), yet 37% of wrong answers feel the same (K06, K07).
- A restructure needs a search criterion. Hints to relax a constraint rarely work alone (K08).
- Changing the representation beats adding activity (K09).
- LLM "aha" text is cheap and common, and does not mark a gain (K15).
- Benchmarks need private reworded twins (K22, K41).

**Failed or weak replications.**
- Metcalfe's warmth jump did not appear with self-reported insight on magic tricks (d23).
- Gradual build-up (Durso; Novick and Sherman) was not found by Smith and Kounios 1996 in anagrams (b13).
- Verbal overshadowing: 57% vs 13% (b08) against nulls from Gilhooly, Fleck and Weisberg and Chein and Weisberg (d18). Kiyokawa and Dienes (2020, abstract only) say some nulls were inconclusive, not null (d19).
- Sleep and incubation gave nothing at N=77 (b06). The older meta-analysis was not opened.
- Pencil handling gave no help (b09).
- The R1-Zero claim that RL creates the aha moment failed: the base model already does it (a26). A 2B vision replication shows the surface behaviour appears from some starting points only (c14).

**Moderators.**
- Measure and statistic (b02). Individual versus group data (b01, b11, b12).
- Insight defined by problem type or by self-report (d22 vs d23).
- Task: verbal CRAs vs spatial problems (d18 vs b08).
- Age: functional fixedness is learned; 5-year-olds were immune (d24).
- Mindset: growth mindset strengthened the Aha-correctness link for first-move-correct solves (a20).
- Background: STEM students solved the pencil problem more often (46.7% vs 11.9%; b09).
- Temperature and entropy in LLMs: shifts help a little at low T and act as noise at high T; they were harmful even at high entropy on maths (-7.40pp) (c04).

**Interventions that worked.**
- Maximization hint plus relaxation (72%; a15).
- Picture showing operators can be split (79.3% vs 46.7%; b09).
- Opposite-reading prompt, more insight than a hint (a12, second-hand).
- Divergent-then-convergent prompting for GPT-4: efficient solutions 30.1% to 36.6% on 180 problems (d20, a reading of a figure).
- Question reformulation plus sampling: 83.0 vs 79.5 for plain self-consistency on GPT-3.5 (d15); RM-PoT 80.4/69.1/88.0 vs 77.3/64.9/87.6 (d14).
- Forced reconsideration on maths (+8.41pp, compute doubled; c05).

**Interventions that did not work.**
- Rest or sleep alone (b06).
- Key hints without a criterion (a15, a18).
- Handling real objects (b09).
- Intrinsic self-correction on 2023 models: GPT-3.5 GSM8K 75.9 to 74.7, GPT-4 95.5 to 89.0 (d11).
- Debate vs self-consistency at equal responses (d11).
- Self-verification in VLMs (b19).
- Two free-talking agents on situation puzzles (a24, preprint).

## 6. Language models

**What was measured.**
- *Spontaneous "aha" in traces.* d'Aliberti and Ribeiro (c01-c06): 1M+ traces, three domains. Shift in 6.31%. Accuracy 2.57% with a shift vs 16.44% without. DeepSeek-R1 shifts in 0.00-0.25% of traces. GPT-4o 0.88-2.21%, with accuracy below its no-shift accuracy at every temperature (c03). Pooled shift-entropy odds ratio 0.77 (CI 0.58-1.02, p=.070). Cue wording did not matter.
- *Forced reconsideration.* MATH-500 +8.41pp (32.2% to 40.6%), but compute doubles and 23,500 correct answers were broken (c05). Small GRPO-tuned Qwen2.5 and Llama models.
- *Is the aha moment real?* The base model already does it (a26). More reflection is not more accuracy. VLMs: 8.3% of responses (b19). Chen and Wang (c17): about 40% of R1 steps are analysis against about 15% framing for an expert; reflection helps only inside deduction. Long et al. (d06): only 5.4% of rechecks were corrective. Zhao et al. (d07): many steps decorative.
- *Pseudo-aha.* On evolved maths problems a flawed shortcut caused 77% to 100% of errors (c18). This is false insight in machine form. Adversarial set.
- *Fixation.* Only Connect: GPT-4 10-shot solved 6 of 494 original walls, 59 randomised, 471 with red herrings removed (b22). Chain of thought may lock in a long procedure on 6 Einstellung items (c11, n=6, weak). A wrong prefix lowers later accuracy (d12).
- *Insight benchmarks.* NazoNazo: 38 models, reasoning 17.6% vs non-reasoning 7.6% vs human 52.9% (c07). Release date predicted accuracy; parameter count did not. CresOWLve: creative questions lose 6.08 to 17.21 points against factual ones on the same knowledge; GPT-5.4 nearly doubles from no thinking to medium effort (c22, b24). Rebus: GPT-5 60.42%, gpt-4o 18.75% (c23). BRAINTEASER: 53% and 63% vs 92% human (b23). MacGyver: GPT-4 18.9% efficient, 37.5% infeasible (d20).
- *Knows but does not commit.* Right answer in the log for 5.23% to 39.34% of wrong answers (c08). Probes predict correctness, ROC-AUC over 0.9 (d04). Over 70% of wrong responses held a correct thought that was dropped (d08). Injected ground truth is often ignored (d05).
- *Where information arrives.* Population accuracy is a ramp (d01). Answer-relevant information comes in bursts at plan and reflection tokens (d02, d03). One worked case: a voiced check lowered expected accuracy; the method switch in the next sentence raised it (d02).
- *Early ChatGPT.* Jan 2023 version on 30 verbal insight problems: 7/15 practice, 5/15 transfer; humans 0.55 and 0.35. One run, with feedback after errors (a23).

**What changed it, by how much.**
- More reasoning effort: about doubled accuracy on CresOWLve; class average 7.6% to 17.6% on NazoNazo; GPT-5 vs gpt-4o on rebus 60.42% vs 18.75%. Does not reach human level.
- Forced second pass: +8.41pp maths, about 0 elsewhere.
- Reformulation before sampling: +3.5 average points (d15), +1.1 to +4.2 per set (d14). Older models, easy maths.
- Divergent step: +6.5 points for GPT-4 (d20).
- Early exit by probe: 24% fewer tokens, same accuracy (d04).
- Confidence filtering: 43-79% fewer tokens than majority vote (d09).
- Penalising thought switches: QwQ AIME2024 38.3 to 44.1 (d08).

**Contested.** The compute-matched comparison of a second look versus independent samples. Voting beat sequential thinking for a 1.5B model (41.0 vs 27.4 on AIME24; d12). Sequential chains beat parallel in 43 of 45 matched-token cells, but chains were capped at 4096 tokens and one headline cell is misprinted (d13). No study used an explicit restructure operator (K31).

**Gap.** No paper was found running Duncker's candle, nine-dot or matchstick problems on 2024-2026 LLMs with human norms (c26, K28). The search budget was limited. Treat classic results as unmeasured.

## 7. What our agent should take

Status: **[E]** established, **[S]** single-source, **[C]** contested. Parts: G guardrail, S state, O operator, M memory or logging.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| 1 | Keep restructuring as named operators (relax a constraint O4, decompose O3, re-encode O6), called only from an impasse state. Matches the schema; log which operator fired. | O, S | [E] (K01) | a01, a05, a06, b15, a07 |
| 2 | Never read a "wait", "aha" or "let me reconsider" in a trace as progress or as restructuring. Judge by what changed: a new frame, a new constraint, a new answer. | G (G10) | [E] (K15) | c01-c03, b20, b19, a26 |
| 3 | A sudden, confident answer goes through a check against the original problem text, and the check can change the output. Felt certainty is never a stop signal. | G (G2, G3) | [E] (K06, K36) | a09, b03, a20, d06, d07 |
| 4 | Pair every restructure with a search criterion and progress test (maximization; remaining versus needed count). A restructure alone is not enough. | O + G | [E] (K08) | a15, a16, a18, b25 |
| 5 | Route on observed impasse (repeated elements, no new candidates), not on task label. | S (S0, S6) | [E] (K12) | b04, b07, a20 |
| 6 | After a reframe, allow search time. Do not stop at the first revised framing. | S | [E] (b25) | b25, b02 |
| 7 | When re-encoding, change the form (table, layout, opposite reading), not the amount of activity. | O (O6) | [E] for direction (K09) | b09, a15 |
| 8 | Evaluate on private reworded twins and report group accuracy. | G (G7, test design) | [E] (K22, K41) | b23, c20, d21, c07 |
| 9 | Do not treat flat self-rated progress as "no progress". Use a probe at checkpoints, not a self-report. | G, S | [E] direction (K35) | a03, a04, d01, d04 |
| 10 | Keep an endorse-or-reject step for earlier candidates (scan the trace before the final answer). The phenomenon is established; the recovery rate is not. | S8 | [E] phenomenon (K30) | c08, d04, d05, d08 |
| 11 | Frame diversification beats plain re-sampling on decoy items: force different framings, not the same one k times. Direction established; size from older models. | O | [E] (K20, K32) | b22, d14, d15 |

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Restructure operator versus extra independent samples with weighted vote at equal tokens | O (O4, O6) | [C] (K31) | d11, d12, d13, d14, c05 |
| T2 | Trigger rule: same-element stall vs entropy vs disagreement vs probe vs none | S | [S] (K33) | d08, d09, d10, d16 |
| T3 | Endorse-or-reject recovery of dropped candidates | S8 | [S] (K18, K30) | c08, d04, d08 |
| T4 | Restart with a verified-facts summary vs patch vs fresh sample | O, M | [S] (K37) | d12, d16, d01 |
| T5 | Short answer-first vs forced long chain of thought on reframing items | G (G11) | [C] (K10) | b08, d17, d18, d19 |
| T6 | Divergent uses first (functional fixedness) | O (O6) | [S] (K40) | d20, d24 |
| T7 | Change-point vs linear shape of per-step progress | S, M | [C] (K02, K34) | b02, d01-d03 |
| T8 | Shortcut check after any confident shortcut | G | [S] (K19) | c18, d07, d23 |
| T9 | Abduction prompt at impasse | O (O8) | [S] (K29) | b21, c16 |
| T10 | Pause or incubation (no operator) | none | [C] (K11) | b06, a21 |
| T11 | Probe-the-gate before full restructure | S | [E] in networks, untested in prompts (K14) | c24, a22 |

Do not add: a "sudden insight" mode, an Aha detector based on wording, a rest step, or two free-talking agents (K23, a24).

## 8. Concrete tests on our bench

All arms get the same total tokens, setup cost included (G7). Use private reworded twins and report original and twin scores. Three or more seeds per item.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | BRAINTEASER-style and NazoNazo-style reframing items; ARC items with a planted decoy | (a) N samples + weighted vote; (b) same-chain extension; (c) impasse, then restructure (relax / decompose / re-encode), then solve | Accuracy per 1K tokens; regressions (right to wrong) | Small gain for (c) on decoy items only; break-even or loss elsewhere. The +8.41pp in c05 was not compute matched |
| B2 (T2) | Same items | Triggers: stall, entropy spike, sample disagreement, solvability probe, none | Accuracy at equal tokens; fire rate; false-fire rate | One trigger beats none by 2+ points; stall needs a minimum depth |
| B3 (T3) | Items whose traces contain a gold answer early | With vs without review call; judge-based match, not string | Wrong answers recovered minus right answers broken | Recover 3-10% of wrong answers if verification failure is 5-39% as reported |
| B4 (T4) | Items with an injected wrong prefix of 0, 200, 800, 1600 tokens | Patch in place; restart with summary; fresh sample | Recovery rate by prefix length | Patch decays with length; restart stays flat |
| B5 (T5) | Reframing items vs procedural items | Answer-first short vs forced step-by-step | Accuracy per arm per item class | Interaction like the human 57 vs 13 and 30 vs 80; may be null |
| B6 (T6) | Fixedness items: candle, two-string, MacGyver subset, with a pre-use mention | Pre-use vs none; divergent-first vs plain retry | Solve rate; infeasible rate | Pre-use lowers solve rate; the divergent step recovers a few points |
| B7 (T7) | 100+ reframing items with probe at checkpoints | Fit jump vs linear model per trace | Share of traces better fit by a jump; does the jump predict a correct answer | A mixed share, like humans (27% sudden vs 54% incremental) |
| B8 (T8) | Items that invite a shortcut (EvolMath-style) | No check; non-gating check; gating check | Wrong-but-confident rate | Gating check cuts it; non-gating check does nothing (d07) |
| B9 | Ten-penny and nine-dot as text puzzles with human norms | Hints: none, relax, maximize, both | Solve rate | Both beats either (human: 7-21% vs 72%) |
| B10 | Same item set at 3 token budgets | Plain vs scaffold | Accuracy curve | Shows where the scaffold beats raw budget (K21) |

## 9. What does not transfer, and why

- **Suddenness as a design target.** Human suddenness depends on introspection and on the statistic. An LLM trace is fully logged, so no hidden step can be "illusory". We can measure, not feel (b02, a05).
- **The Aha feeling.** It follows cues, mainly a correct first move, not restructuring (a20). The model's "Aha!" tokens are pretraining text (a26).
- **Incubation and sleep.** No weights change during a pause. A pause with no new input adds nothing. Only a fresh pass with a different frame is meaningful (K11).
- **Pupil, gaze, gamma.** These mark human attention and arousal (a11, a21, a07). The only analogue is which problem elements the trace names.
- **Verbal overshadowing.** The human effect is about a verbal system interfering with nonverbal processing. An LLM thinks in tokens. The closest analogue is chain-of-thought length, and no insight task has been tested (d17).
- **Physical manipulation.** Pencils did not help even humans (b09).
- **Warmth ratings.** Weak even in humans (d22, d23). Self-reported closeness from an LLM is likely worse; use a forced-answer probe.
- **Single-puzzle effect sizes.** Most human data use one or two puzzles and student samples. Do not copy a number into a threshold.
- **Public riddle scores.** Contamination makes them near useless without twins (b23, c07, c22).

## 10. Open questions

1. At equal tokens, does an explicit restructure operator beat independent samples plus voting on a current frontier model? (Gap 1; no study.)
2. Which trigger works best? Only entropy has been tested, on small models. (Gap 2)
3. What is the recovery rate of an endorse-or-reject step with a non-string judge? (Gap 3)
4. Do nine-dot, candle, matchstick and ten-penny with human norms show models falling for the same traps and gaining from the same hints? (Gap 4; no paper found.)
5. Does forced step-by-step reasoning hurt reframing items in LLMs? (Gap 5)
6. In single traces, is restructuring a jump or a ramp? (Gap 6)
7. Does a flat probe predict a failure that a restructure fixes? (Gap 7)
8. How much of the gain on riddle benchmarks survives private twins for 2025-26 reasoning models? (Gap 8)
9. Do the founding numbers (Duncker 1945, Maier 1931, Wertheimer, Kohler) replicate? Original numbers were not obtained. (Gap 9)
10. What is the false-insight rate with and without a gating check? (Gap 10)
11. Sternberg and Davidson's three-process theory was not researched here.
12. Sio and Ormerod's incubation meta-analysis and Schooler 1993 were cited from memory. Check the figures.

## 11. Sources

[V] = opened this session. [M] = snippet, second-hand or memory only.

**Human insight and Gestalt**
- [V] Vitello and Salvi (2023), Gestalt's perspective on insight. https://pmc.ncbi.nlm.nih.gov/articles/PMC10743969/ (a01)
- [V] Graf, Danek, Vaci, Bilalic (2023), GAMs and change point analysis. https://pmc.ncbi.nlm.nih.gov/articles/PMC10219327/ (a08, b02, b25)
- [V] Bilalic, Graf, Vaci, Danek (2019), temporal dynamics of insight. https://eprints.whiterose.ac.uk/195625/7/Bilalic_et_al_2019_the_temporal_dynamics_of_insight_problem_solving.pdf (b01)
- [V] Danek and Wiley (2017), false insights. https://pmc.ncbi.nlm.nih.gov/articles/PMC5247466/ (a09, b03)
- [V] Webb, Little, Cropper (2016). https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01424/pdf (b04)
- [V] Salvi et al. (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC5035115/ (b05)
- [V] Schoenauer et al. (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5834438/ (b06)
- [V] Salmon-Mordekovich and Leikin (2023). https://pmc.ncbi.nlm.nih.gov/articles/PMC10366031/ (b07)
- [V] Macchi, Poli, Caravona (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11942870/ (b08)
- [V] Macchi, Inglese, Caravona (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13208192/ (b09)
- [V] Becker, Wang, Cabeza (2024), no coefficients extracted. https://pmc.ncbi.nlm.nih.gov/articles/PMC11680657/ (b10)
- [V] Oellinger et al. (2017), ten-penny. https://pmc.ncbi.nlm.nih.gov/articles/PMC5533865/ (a15)
- [V] Oellinger, Szathmary, Fedor (2023), card sorting, tables not read. https://pmc.ncbi.nlm.nih.gov/articles/PMC10196050/ (a19)
- [V] Wiley and Miller (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13608503/ (a20)
- [V] Macchi, Turco, Inglese, Caravona (2026), pupil; abstract and preprocessing only. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608808/ (a21)
- [V] Doulfoukar, Pezzulo, Stuyck (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13585804/ (a22)
- [V] Metcalfe and Wiebe (1987). https://link.springer.com/content/pdf/10.3758/BF03197722.pdf (d22)
- [V] Hedne, Norman, Metcalfe (2016). https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5005374/ (d23)
- [V] German and Defeyter (2000). https://link.springer.com/content/pdf/10.3758/bf03213010.pdf (d24)
- [V] Chein and Weisberg (2014). https://link.springer.com/article/10.3758/s13421-013-0343-4 (d18)
- [V, abstract only] Kiyokawa and Dienes (2020). https://cognitivesciencesociety.org/cogsci20/papers/0192/index.html (d19)
- [V] Loewe et al. (2024). https://arxiv.org/abs/2302.11351 (c24)
- [M] Metcalfe (1986) warmth numbers (via a02, b18)
- [M] Durso, Rea, Dayton (1994) (via a03, b13)
- [M] Novick and Sherman (2003) (via a04, b14)
- [M] Knoblich et al. (1999, 2001) (via a06, a07)
- [M] Ohlsson (1992) (via a05, b15)
- [M] Kaplan and Simon (1990) (via a17)
- [M] MacGregor, Ormerod, Chronicle (2001) (via a16)
- [M] Weisberg and Alba 1981; Scheerer 1963; Lung and Dominowski 1985 (via a18)
- [M] Cushen and Wiley (2012); Danek, Williams, Wiley (2018) (via b11, b12)
- [M] Salvi 2020; Laukkonen and Tangen 2017; Bianchi 2020; Laukkonen 2021; Korovkin 2021 (via a11-a14)
- [M] Sio and Ormerod (2009), from memory. https://doi.org/10.1037/a0014212 (b16)
- [M] Schooler, Ohlsson, Brooks (1993), from memory. https://doi.org/10.1037/0096-3445.122.2.166 (b17)
- [M] Wertheimer, Duncker, Kohler, Maier, Adamson, Glucksberg: not opened; no primary numbers.

**Language models and AI**
- [V] d'Aliberti and Ribeiro (2026), Illusion of Insight. https://arxiv.org/abs/2601.00514 (c01-c06, c25, c26)
- [V] Mizumoto et al. (2025), NazoNazo. https://arxiv.org/abs/2509.14704 (c07-c10)
- [V] Haq et al. (2025), mental set. https://arxiv.org/abs/2501.11833 (c11)
- [V] Yang et al. (2025), Understanding Aha moments. https://arxiv.org/abs/2504.02956 (c12)
- [V] Liu et al. (2025), R1-Zero-like training. https://arxiv.org/abs/2503.20783 (a26, b20, c13)
- [V] Zhou et al. (2025), 2B aha. https://arxiv.org/abs/2503.05132 (a27, c14)
- [V] Wu et al. (2025/26), Aha Moment Revisited. https://arxiv.org/abs/2506.17417 (b19, c15)
- [V] DeepSeek-AI (2025), R1. https://arxiv.org/abs/2501.12948 (a25)
- [V] Hu et al. (2025), Beyond Aha. https://arxiv.org/abs/2505.10554 (b21, c16)
- [V] Chen and Wang (2026). https://arxiv.org/abs/2606.07410 (c17)
- [V] Chen et al. (2025), EvolMathEval. https://arxiv.org/abs/2508.13003 (c18)
- [V] Jiang et al. (2023), BRAINTEASER. https://arxiv.org/abs/2310.05057 (a28, b23, c19, c20)
- [V] Jiang, Ilievski, Ma (2024), SemEval Task 9. https://arxiv.org/abs/2404.16068 (d21)
- [V] Chen et al. (2024), SPLAT. https://arxiv.org/abs/2410.06733 (c21)
- [V] Ismayilzada et al. (2026), CresOWLve. https://arxiv.org/abs/2604.03374 (b24, c22)
- [V] Lee et al. (2025), Puzzled by Puzzles. https://arxiv.org/abs/2505.23759 (c23)
- [V] Naeini et al. (2023), Only Connect Wall. https://arxiv.org/pdf/2306.11167 (b22)
- [V] Orru et al. (2023), ChatGPT on insight problems. https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637/ (a23)
- [M] Qiu, Zhou, Schooler (2026), abstract only. https://doi.org/10.31234/osf.io/pzkvh_v1 (a24)
- [V] Ballon et al. (2026), reasoning trace trajectories. https://arxiv.org/abs/2601.23163 (d01)
- [V] Bogdan et al. (2025), Thought Anchors. https://arxiv.org/abs/2506.19143 (d02)
- [V] Qian et al. (2025), mutual information. https://arxiv.org/abs/2506.02867 (d03)
- [V] Zhang et al. (2025), models know when they are right. https://arxiv.org/abs/2504.05419 (d04)
- [V] Cuesta-Ramirez et al. (2025). https://arxiv.org/abs/2507.00711 (d05)
- [V] Long et al. (2026), self-verification dilemma. https://arxiv.org/abs/2602.03485 (d06)
- [V] Zhao et al. (2026), fake aha moments. https://arxiv.org/abs/2510.24941 (d07)
- [V] Wang et al. (2025), underthinking. https://arxiv.org/abs/2501.18585 (d08)
- [V] Fu et al. (2025), Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d09)
- [V] Wang et al. (2025), 80/20 high-entropy tokens. https://arxiv.org/abs/2506.01939 (d10)
- [V] Huang et al. (2024), LLMs cannot self-correct. https://arxiv.org/abs/2310.01798 (d11)
- [V] Wen et al. (2025), ParaThinker. https://arxiv.org/abs/2509.04475 (d12)
- [V] Anonymous (2025), Sequential Edge; text and table disagree. https://arxiv.org/abs/2511.02309 (d13)
- [V] Zhang et al. (2025), RM-PoT. https://arxiv.org/abs/2502.12589 (d14)
- [V] Wu et al. (2025), Is depth all you need. https://arxiv.org/abs/2502.10858 (d15)
- [V] Li et al. (2025), situation puzzles. https://arxiv.org/abs/2503.18394 (d16)
- [V] Liu et al. (2025), Mind Your Step. https://arxiv.org/abs/2410.21333 (d17)
- [V] Tian et al. (2025), MacGyver. https://arxiv.org/abs/2311.09682 (d20)

**Corrections carried over from critique.md.** Graf 2023's sudden figure is simulated. The "65.5 vs 49.5" pair in b19 was dropped. b19 and c15, a26/b20/c13, and c01-c06 are one paper each. b01's participant counts beyond "54% of 26" are unverified. a11's "60.5%" is second-hand and not quoted.

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 16 established claims: 9 confirmed as written, 7 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A02.06-K03** (reworded: the sources support less). The final-third shift is in Bilalic 2019 real data, but the change point near the 90% bin comes from Graf 2023 data that the paper states are simulated to represent a sudden shift; the original 2019 data show a gradual group-level shift (27% of solvers sudden-looking, 54% incremental). Also Graf 2023 re-analyses the same data from the same lab, so the two sources are not independent. Corrected claim: Solvers who later succeed shift attention from the values to the critical element (the plus sign/operators) only in the final third of the solving period, while non-solvers stay on the obvious parts (values); on the original eye-tracking data the group-level shift looks gradual (individually 27% of solvers sudden-looking, 54% incremental), so whether the shift is abrupt is unresolved.
- **A02.06-K07** (reworded: the sources support less). Effect sizes match (Salvi d 0.39 to 1.85), but Webb non-insight Aha-accuracy r was 0.02 only in Exp 1 (0.24, p=.04 in Exp 1a; 0.19 with BF10 about 40 in Exp 2), so near 0 is too strong; Salvi says analytic solutions had relatively more commission errors than timeouts compared with insight, not that insight errors are mostly omissions. Corrected claim: On average, self-labelled insight solutions are more accurate than analytic ones (d about 0.4 to 1.85 across four experiments), and analytic-labelled responses include relatively more errors of commission (wrong guesses) and insight responses relatively more omissions (timeouts). Aha and accuracy correlate r about 0.4 to 0.5 for classic insight problems and CRAs, and only weakly (r 0.02 to 0.24) for non-insight problems.
- **A02.06-K12** (reworded: the sources support less). Salmon-Mordekovich and Leikin found verbal insight problems differed from verbal non-insight (resembling only spatial non-insight), found impasse reports 37 to 41% on insight vs 1.7% on verbal non-insight, and conclude with mixed evidence for both business-as-usual and special-process; Wiley and Miller study 4 puzzles of one type, so solver state vs problem type is not shown as the claim states. Corrected claim: Insight is not a clean property of problem type: insight ratings vary within a problem type, Aha-accuracy links differ by task (strong for insight problems and CRAs, weak for non-insight), and insight and spatial non-insight problems resemble each other on dual-task and individual-difference tests (both unaffected by secondary tasks), though verbal insight problems differed from verbal non-insight problems and the authors find some evidence for a rarer special-process mode.
- **A02.06-K21** (reworded: the sources support less). Numbers match, but for NazoNazo GPT-5 falls inside the human 95% CI (46.6 to 59.2), so the gap is closed for the best model; the averages (7.6/17.6 vs 52.9) do not close it. Rebus GPT-5 60.42 vs gpt-4o 18.75 and CresOWLve doubling are correct. Corrected claim: More reasoning effort or a reasoning model helps on insight-type riddles and usually does not close the gap to humans: NazoNazo non-reasoning 7.6% vs reasoning 17.6% vs human mean 52.9% (120-item subset), though GPT-5 alone falls within the human 95% CI; rebus puzzles GPT-5 60.42% vs gpt-4o 18.75%; CresOWLve GPT-5.4 nearly doubles from no thinking to medium effort while non-thinking models stay under 30%.
- **A02.06-K22** (reworded: the sources support less). BRAINTEASER (45% fail, SemEval 80% drop) numbers are right, but BRAINTEASER only suggests memorisation, CresOWLve reports some contamination evidence and a risk, and Mizumoto argue memorisation does not explain NazoNazo scores; contaminated or memorised as established fact is too strong. Corrected claim: Riddle and lateral benchmarks carry contamination or memorisation risk: ChatGPT fails 45% of original or semantic puzzles whose context-reconstructed twin it solves (BRAINTEASER authors suggest memorisation), CresOWLve reports some contamination evidence for its public quiz sources, and in SemEval-2024 Task 9 over 80% of leaderboard models lost accuracy on grouped original+semantic puzzles even with 80% training data; the NazoNazo authors argue memorisation does not explain their low scores.
- **A02.06-K32** (reworded: the sources support less). Numbers match (GLM-4-9B in d14, GPT-3.5-turbo in d15), but RM-PoT also adds program-of-thought execution and 5 retrieved examples, and PoT alone (78.9/65.6/87.1) already beats SC, so the gain is not due to re-encoding alone. Corrected claim: RM-PoT (reformulation K=4 plus retrieved examples plus program-of-thought code, GLM-4-9B, N=16 paths) scored 80.4 / 69.1 / 88.0 vs self-consistency 77.3 / 64.9 / 87.6 on GSM8K / AQuA / SVAMP, but PoT alone scored 78.9 / 65.6 / 87.1, so part of the gain is not from reformulation (d14); question-reformulation plus sampling (QuestionC-SC) averaged 83.0 vs 79.5 for plain self-consistency on GPT-3.5-turbo across ten tasks (d15). This is rewording, not constraint relaxation, and token counts are not matched.
- **A02.06-K35** (reworded: the sources support less). ROC-AUC above 0.9 is reported only for R1-Distill-Qwen-32B on AIME (in-distribution generally above 0.7); the 24% saving at 88.2% is for R1-Distill-Llama-8B on MATH. Corrected claim: A latent-progress probe predicts later success in LLMs when you have access to the model or can truncate its trace: hidden-state probes give ROC-AUC above 0.7 in-distribution and above 0.9 for R1-Distill-Qwen-32B on AIME (d04), early exit at threshold 0.85 on R1-Distill-Llama-8B (MATH) saves about 24% tokens at 88.2% accuracy, equal to no early exit (d04), and truncated-trace answer distributions track final accuracy (d01). It does not yet show that a flat probe reliably precedes a restructure that works.
- **A02.06-K01** (now single-source: only one opened source, code check).
- **A02.06-K41** (now single-source: only one opened source, code check).
