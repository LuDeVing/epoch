# Methods and measurement: deep document

*Subfield A12.10 of the psychology of insight. Built from evidence_a-d.jsonl (a01-a25, b01-b28, c01-c28, d01-d22), claims.jsonl (K01-K29) and critique.md in this folder. Evidence ids are cited in square brackets. Status marks: [E] established, [S] single-source, [C] contested.*

## 1. What it is

This subfield asks a plain question: how do we know that a person, or a model, had an insight? And which tasks may we call "insight tasks" at all?

Three parts matter.

1. **Task choice.** Labs use classic insight problems (nine-dot, matchsticks, Deer, Ansburg and Dominowski verbal problems), compound remote associates (CRA, RAT), rebus puzzles, magic-trick videos, riddles, and "non-insight" control problems such as cryptarithmetic. The label comes from the experimenter, not from the solver.
2. **Measures.** Insight is mostly measured by report: a yes/no "Aha", a rating on several dimensions (pleasure, certainty, suddenness, surprise), or "feeling of warmth" ratings taken every 10 to 15 seconds. Other measures are objective: pupil size, blackboard unpredictability, solution jump, and (for models) entropy and hidden-state probes.
3. **Ecological validity.** Lab puzzles may not match real insight. The field evidence is thin and was mostly read at abstract level. The "real insight is often gradual" claim is not yet quantified [K21, d16, d17].

Why this matters for our agent: S6 (impasse) needs a test set. If the set is built from items we only *call* insight items, results mean little. If we trust "Aha" words in traces as a signal, we may act on a feeling that does not track truth.

Main finding in one line: insight lives in the solver's experience of a solution, not in the problem [a04, b17]. Aha reports are cue-based judgments, not a truth label [a10, b06].

## 2. History and theories in depth

**Restructuring and its three assumptions.** Gestalt-descended theories say a solver starts with a wrong representation, then changes it, then the solution comes in a jump. Ash, Cushen and Wiley (2009, Journal of Problem Solving 2(2), 6-41) argue that these are three separate assumptions: representational difficulty, representational change and discontinuity. Few studies test all three, so "insight problem" is under-defined [a01, b15]. Only the abstract page was read; the PDF was blocked (403). Their list of method obstacles is therefore not recorded here.

**Individual differences.** Ash and Wiley (2006) separated problems that allow a large faulty search space from problems that isolate restructuring. Working-memory span predicted success on the first kind, not the second. They read this as support for automatic redistribution of activation in restructuring, not controlled search. Insight is not one process [a03, b14].

**Warmth era.** Metcalfe and Wiebe (1987) reported that warmth rose suddenly for insight problems and gradually for non-insight problems, which was taken as the signature of insight. Webb's commentary notes that Metcalfe and Wiebe lost 34 of 73 subjects to data loss, and that Metcalfe (1986) found high warmth on wrong answers [a23, b05, b11; snippet level only].

**Aha experience era.** Bowden, Jung-Beeman and colleagues used the self-reported Aha as the marker. Danek et al. (2014) argued that "insight problems per se do not exist, only solutions with insight": the same problem is solved with or without Aha [b17, d12]. Webb, Little and Cropper (2016) made this the title: "Insight is not in the problem" [a04, b01].

**Aha as a metacognitive judgment.** Danek and Wiley (2017) asked about false insights: wrong solutions that carry strong Aha. Wiley and Danek (2026) then argued Aha ratings are "Judgments of Aha" inferred from cues such as fluency, speed and correctness [a08, a10]. A 2024 preregistered CRA study found that only surprise tracks a metacognitive prediction error; suddenness moved the other way [d19]. So Aha is a bundle with unstable parts.

**Non-report markers.** Pupil dilation during incubation (Macchi et al. 2026) and information-theoretic unpredictability of mathematicians' blackboard writing (Tabatabaeian et al. 2025, PNAS) give measures that do not rely on report [d18, d16].

**Competing views on whether insight is special.** Macchi et al. (2025): verbalisation hurts insight and helps non-insight, so there is a process split. Salmon-Mordekovich and Leikin (2023): insight problems are mostly solved by analytic routes, so insight is "not that special". Weisberg (2015): business-as-usual cognition inside an integrated theory [a14, a16, b16 snippet]. This is [C].

**LLM-era methods work (2023-2026).** Benchmarks were built to need a representation shift (NazoNazo riddles, Only Connect walls, BRAINTEASER, BrainBench). In parallel, researchers asked whether "Aha"-like words in reasoning traces mean anything [a17, b21, c21, c23, a20, b25].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Aha tracks accuracy for insight problems and CRA, not for non-insight problems | Exp 1 (N=193): r=.50 insight, .41 CRA, .02 non-insight. Exp 1a (ESL-filtered subset): r about .40 for insight; task-by-Aha effect F(2,158)=33.98, eta2=.30 | Webb et al. 2016 [a04, b01, a07] | [E] (K01) |
| Same task label, very different insight rate | 51.9% of correct classic-problem trials reported as insight (Salvi, quoted by Webb); 29% of magic-trick trials (Hedne, 971 trials); 76% of generated CRA solutions (Kizilirmak); 41% of solved magic tricks (Danek 2014, 34 tricks, 48 people) | [b03, b09, b27, d12] | [E] (K07) |
| Wrong answers also carry Aha | Magic tricks, N=70: 2450 trials, 1778 solutions, 36.8% (654) correct, 63.2% (1124) wrong. Aha 66.50 (SD 18.42) correct vs 52.34 (SD 18.78) wrong, t(69)=10.21. 417 of 1124 wrong answers (37%) rated above the correct-answer mean | Danek and Wiley 2017 [a08, b06] | [E] (K02) |
| Aha rises with speed | Solve time 35.81 s correct vs 42.46 s wrong, t(1776)=6.26. The time-by-accuracy interaction in the mixed model was not significant (t=1.58, p<.12); claim main effects only | [a09, b08, critique] | [E] (K03) |
| Aha is a cue-based judgment (matchsticks) | N=377, 1164 analysed trials of 1508. Aha-correctness F(1,1091)=112.17, partial R2=.09 [.06,.12]. Three-level index (wrong / correct after wrong first move / correct after correct first move) F(2,1079)=71.48, partial R2=.11. Highest Aha after a correct first move, not after a representation change | Wiley and Danek 2026 [a10, a11] | [E] (K03); lab-dependent (absent in Strickland 2022 for matchsticks) |
| Insight-labelled answers more accurate | Hedne: accuracy .57 vs .37 (d=.51), confidence 78.32 vs 68.95 (d=.50). Salvi 2016: CRA 93.7% vs 78.3%; visual Aha 78.4% vs 41.5% | [b09, d13, b12] | [C] (K08) |
| Warmth difference not found | Hedne: differential warmth 12.93 vs 11.65, t(239.38)=0.72, p=.47, d=.07 (971 trials, magic tricks). Laukkonen and Tangen: per-person r=.61 (n=51) but per-problem r=.08 (n=182, p=.235) | [b09, b04] | [E] that measures disagree (K05); [C] for the signature (K06) |
| Warmth and self-report barely agree | Of 631 correct trials, 180 had 2+ warmth ratings. 75.6% of warmth-insights vs 50.8% of non-warmth items were self-reported insight (contingency 75.6/24.4/50.8/49.2) | Laukkonen and Tangen 2018 [b04, b05] | [E] (K05) |
| Warmth found for CRA | Last-two-rating rise 2.59 with Aha vs 1.43 without | Kizilirmak 2018 [b10] | [C] (K06) |
| Aha components | Pleasure, certainty and suddenness carry most of the overall rating. Surprise r=.07 in one study, .29-.48 in another. Only surprise tracks prediction error; suddenness negative | [b07, a05, d19] | [C] (K04) |
| Aha does not separate solving from generation | N=77 (8 excluded, 5 excluded for all-Aha). No Aha-strength difference between CRA/polysemy solutions and category generation | Smith et al. 2026 [a13] | [S] (K20) |
| WM predicts large-search insight only | N=203; WMSPAN beta=.27, p<.01, R2=.08; interaction R2 change .046, F(1,111)=5.81 (another reading gives df 112; analysis subsample unverified); solve time beta=-.22 | Ash and Wiley 2006 [a03] | [S] (K09) |
| Verbalising hurts insight, helps non-insight | Deer: 13% aloud vs 57% silent. Cryptarithmetic: 80% aloud vs 30% silent. Salmon-Mordekovich (N=115): insight solved mostly by analytic routes unaffected by secondary tasks | Macchi 2025 [a14]; [a16] | [C] (K11) |
| Item-level human base rates are partial | CRA norms (Romanian, 111 items, n=63): accuracy mean .54, SD .43; RT correct 15.37 s; alpha .93 for accuracy | [d14] | [E] that item difficulty varies (K26) |
| Pupil marker | 82 analysed; 11 of 40 incubation participants solved (27.5%); constant high pupil size only in later solvers | Macchi et al. 2026 [d18] | [S] (K27) |
| Mathematicians' blackboard foreshadowing | 6 mathematicians, 12 proof sessions (plus a pilot), 4,653 blackboard interactions, 27 sudden insights in 13 of 14 sessions, each with measurable lead-up | Tabatabaeian et al. 2025 [d16] | [S] (K27, K21) |
| Field coding | 120 incidents, 14 features, three pathways (contradiction, impasse, connection). Share gradual vs sudden not in the abstract | Klein and Jarosz 2011 [d17] | [C] (K21); abstract only |
| NazoNazo riddles | 38 models; non-reasoning 7.60% (n=16), reasoning 17.59% (n=19), human 52.9% (CI 46.6-59.2%, pilot n=126, 120 items). All 201 items: 9.42% vs 19.25%, OR 2.29 [1.99, 2.64], Welch t(24.093)=2.976, d=0.946. Size vs accuracy r=-0.017; release date rho=.402 | Mizumoto et al. 2025 [a17, c01, d21] | [S] (K12) |
| Verification failure | Gold answer written in the thought log yet not committed in 5.23% to 39.34% of wrong answers, by model | [a18, b19, d21] | [S] (K13) |
| Mid-trace shifts | 6.31% of traces; 2.57% vs 16.44% accuracy; formal detector 1.79%; forced reconsideration MATH-500 0.322 to 0.406 (+8.41 pp). Llama 3.1-8B lost 4.19 pp in a small slice | d'Aliberti and Ribeiro 2026 [a20, c05-c08, d20] | [S] (K14, K22) |
| Red-herring fixation | GPT-4 0-shot: 6/494 walls (humans 285/494), 239/1976 groups (humans 1405/1976). Best few-shot: 7 walls (5-shot), 272 groups (3-shot). OCW-Randomized 59/595; OCW-WordNet 471/1926 (pairing with GPT-4 0-shot likely, not certain). GPT-3.5 0-shot 0/114 walls | Alavi Naeini et al. 2023 [b21, c16, c17] | [S] (K15) |
| Lateral-thinking benchmarks | BRAINTEASER human 91.98%; ChatGPT 62.68% sentence, 53.46% word; group accuracy across rewrites 50.72% and 39.71%. BrainBench: Opus 4.6 extended thinking 80.3% (consistency 74.0%), GPT-4o 39.7%; extended thinking +3.3 / +3.0 pp average, naive physics -26.7 pp | [c21, c23, c24] | [E] brittleness (K17) |
| Recast and false corrections | o3 56.7% to 73.3% when puzzles recast as math (p=.023). Models accepted a false correction of a correct solution over 60% of the time | Han et al. 2025 [c25, c26] | [S] (K18) |
| Oracle-free self-correction lowers accuracy | GPT-3.5 CommonSenseQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 91.5 to 89.0 | Huang et al. 2024 [d08] | [E] (K18, K22) |
| RAT is nearly saturated | 57 items: GPT-4o 54.96, DeepSeek-V3 51.00, Gemini 2.0 44.93 vs 19.13 for 46 students | [d15] | [E] (K25, K16) |
| Written reasoning unfaithful | Hint mentioned in 25% (Claude 3.7 Sonnet) and 39% (DeepSeek R1) of cases; hidden-state probes ROC-AUC above 0.7, ECE below 0.1, 24% fewer tokens with early exit | [d06, d07] | [E] (K24) |
| Aha words not tied to accuracy | Aha/wait words occur in base models before RL; sit on high-entropy tokens | [d04, d05] | [E] (K23) |
| Inverse scaling | R1 70% to 30% with five distractors; Opus 4 near 100% to 85-90% | Gema 2025 [d02] | [S] (K29) |

## 4. Mechanisms and models

### 4.1 Aha as a judgment from cues (implementable as a logging rule)
The best-supported model is that the Aha rating is inferred from cues, not read from a special process. Cues: speed, fluency, a correct first move, confidence, surprise. When a solution comes fast and feels easy, people report more Aha, right or wrong [a09, a10, b08].

For an agent, the analogue is a stated "I see it" or a high confidence at the end of a short trace. Implementation: log (a) token count to the final answer, (b) whether the first working frame was kept, (c) stated confidence, (d) the external check result. Then fit accuracy against (a)-(c). If confidence tracks token count more than correctness, it is a cue, not a signal. Do not use it as a stopping rule (SCHEMA 4b already says verbal confidence is a weak stop).

### 4.2 Three-criteria restructuring audit (to tag items and traces)
From Ash et al. (2009) [a01]: for each item, require evidence for
1. wrong first representation: a first frame that many solvers adopt and that cannot reach the answer;
2. representation change: the working frame in the trace changes in content, not only in wording;
3. discontinuity: progress is flat, then the answer appears, rather than a steady approach.

Engineering form: from a trace, code extracts the stated frame at each step (a one-line "current frame" slot, filled by the model, compared by code with an embedding distance plus a string check). A change is a frame whose distance from the previous one exceeds a threshold calibrated on hand-labelled traces. Discontinuity is a flat candidate-quality curve (scored by a verifier on partial answers) followed by one step up. This scoring method is our proposal; no source gives an automatic method (gap 2 stayed open). Marker words ("wait", "Aha") must not be the detector [d04, d05, d20].

### 4.3 Multi-indicator agreement
Because warmth and report disagree (per-problem r=.08) [b04], an item or trace is tagged "insight-like" only when at least two independent indicators agree: (i) frame change, (ii) stall then jump, (iii) entropy spike at the switch, (iv) a probe on hidden states if available [d05, d07]. Report the agreement between indicators as a number.

### 4.4 Shift detector from d'Aliberti and Ribeiro
A cue word (such as "wait") plus a change in the answer or approach. Fires in 6.31% of traces (formal detector 1.79%). Forced reconsideration under high entropy: pass 2 conditioned on pass 1, MATH-500 0.322 to 0.406 [a20, c05-c08]. Re-read note: no cue-free control found, tokens roughly doubled, and the cue hurt Llama 3.1-8B (-4.19 pp, small slice) [d20]. Raw shift effects of about -22.5 pp are domain-specific and entropy-bucketed; do not mix them with the pooled gap of 16.44 minus 2.57 = -13.9 pp (critique). Treat as a design to test, not a result.

### 4.5 Gold-in-trace detector (verification failure)
Code scans the full thought log for the gold answer. In production there is no gold, so use the SCHEMA S4 harvest: extract every distinct candidate string the attempt raised and test all of them. NazoNazo shows reasoning models name the right answer and then do not commit in 5% to 39% of wrong answers [a18, d21]. Caveat: the measure is literal mention, so a rejection counts as a mention. Hidden states encode correctness better than the text says [d07], and text traces are often unfaithful [d06], so the fix is a code check on the candidate, not a written "double-check".

### 4.6 Contamination guard
Public puzzles are exposed [d03, d10, d11, d15, d22]. Pipeline: (1) guided-completion test per item (give the first part of the item and see whether the model completes it verbatim; agreement with experts 92-100% in Golchin and Surdeanu [d11]); (2) alter surface and answer; (3) match answer probability, since GPT-4 cipher accuracy moves 51% vs 13% with answer probability [d10]; (4) keep open, blind and post-cutoff sets as NazoNazo does (42 open, 159 blind, plus a new set) [d21].

## 5. What holds up

**Holds up (two or more sources).**
- Insight is not a property of the task. Aha-accuracy correlations depend on task (r .50 / .41 / .02) [a04, b01]; Danek et al. reach the same view from magic tricks [d12]; the Webb quote of earlier work agrees [b17]. [E]
- Aha is not a truth label. 37% of wrong answers rated above the correct mean [a08]; Metcalfe 1986 found the same pattern with warmth [b03]. [E]
- Aha depends on cues (speed, first move) [a09, a10, b08]. [E]
- Self-report, warmth and objective markers disagree [b04, b09, b10]. [E]
- Aha/wait words in models are not reliable markers of insight [d04, d05, d20]. [E]
- Written reasoning is a weak guide [d06, d07]. [E]
- Popular puzzles are contaminated or saturated [d15, d11, d10]. [E]

**Failed or contested.**
- Sudden warmth as a signature: lost in Hedne (d=.07) and Laukkonen and Tangen (per-problem r=.08), kept in Kizilirmak (2.59 vs 1.43) [b09, b04, b10]. Metcalfe and Wiebe lost 34 of 73 subjects [b05].
- Aha-correctness: present in Kizilirmak 2021, absent for matchsticks in Strickland 2022 [a11].
- Component structure: surprise r=.07 vs .29-.48 [b07, a05].
- Verbalisation harm: Macchi (13% vs 57%) and Fleck and Weisberg 2013 against Salmon-Mordekovich and Leikin 2023 [a14, a16].
- Incubation by distraction does not replicate in the wider record (SCHEMA 4b). The pupil result [d18] is single-source.

**Moderators.** Task type; who generated the answer; rating interval; number of usable warmth ratings (only 180 of 631 trials had 2+) [b04]; first move correct or not [a10]; item familiarity (223 of 1508 matchstick trials dropped as seen before) [a10]; for models, scoring (answer only vs justified) and model generation [c14, c18].

**Interventions that worked (models).**
- Recasting narrative puzzles as math: o3 56.7% to 73.3%; deepseek-reasoner 50.0% to 63.3% [c26].
- Hint plus math prompt for strong models: o3 68.4 to 74.4 on logic; R1 44.6 to 50.6 [c25]. A 1.5B distill was flat or worse.
- Removing red herrings: GPT-4 solved 59 of 595 groups with diluted herrings (OCW-Randomized) and 471 of 1926 on OCW-WordNet, where herrings were removed (pairing likely, not certain) [c16, c17].
- Oracle labels for self-correction (not available at test time) [d08].

**Interventions that did not work.**
- Oracle-free self-correction [d08].
- Extended thinking on trick questions: +3 pp average, naive physics -26.7 pp [c24].
- Chain-of-thought where verbal thinking hurts humans: hurt 3 of 6 tasks, none an insight task [d01].
- Longer reasoning: inverse scaling on distractor and zebra tasks [d02].
- Few-shot on Only Connect: GPT-4 walls 6 to at most 7 [b21].

## 6. Language models

**Overall picture.** "LLMs are bad at insight" and "LLMs are good at insight" are both false as single statements [critique]. Item sets, scoring and model generation differ.

| Study | Task | Result | Note |
|---|---|---|---|
| Speed 2023 [b22, c11-c13] | RAT, 5 insight problems | GPT-3.5 poor on RAT; GPT-4 good on 5 insight problems | early models; small |
| Orru 2023 [c14, c15] | 30 Ansburg and Dominowski problems | ChatGPT 12/30 (7/15 practice, 5/15 transfer); human median .55 practice, .35 transfer (n=20) | Jan 2023 version |
| Zhang 2025 [c18-c20] | RAT (61 humans), character puzzle, stumpers, rebus (60 humans) | Models beat humans on RAT (estimates .19, .26, .35). GPT-4o beat humans on all three insight tasks (character -.21, stumpers -.06, rebus -.39 gap); GPT-3.5 lost | newer models better |
| Generative AI vs students [d15] | 57-item RAT | 54.96 / 51.00 / 44.93 vs 19.13 | RAT saturated |
| NazoNazo [a17, c01] | children's riddles needing a representation shift | non-reasoning 7.60%, reasoning 17.59%, human 52.9% | one lab, one language; GPT-5 inside human CI; search-augmented near human |
| Only Connect [b21, c16] | grouping with red herrings | GPT-4 0-shot 6/494 walls, humans 285/494 | contamination admitted [d22] |
| BRAINTEASER [b23, c21, c22] | lateral multiple choice | ChatGPT 53-63%, human 92% | group accuracy across rewrites lower |
| BrainBench [c23, c24] | 100 trick questions, 8 models | best 80.3% (Opus 4.6 thinking); GPT-4o 39.7% | extended thinking +3 pp |
| Han 2025 [c25-c27] | Braingle brainteasers | creative vs brute-force route scored; hints help strong models; false corrections accepted over 60% | |
| CREATE [c28] | associative paths | thinking models not always better | abstract only |

(Latif 2024 [a22] is not an insight study and is not used as evidence.)

**What changed the results.**
- Model generation: GPT-3.5 to GPT-4o flips RAT and some insight tasks from below human to above [c18]. Release date predicts NazoNazo score (rho=.402) but size does not (r=-0.017) [a17].
- Reasoning mode: +9.99 pp on NazoNazo (7.60 to 17.59) [a17], but only +3 pp on BrainBench with extended thinking and losses in some categories [c24]. The cause (length or verification) is untested; length alone is not reliably helpful [d02].
- Problem form: narrative to math, +16.6 pp for o3 [c26]; red herrings removed [c16].
- Retrieval: search-augmented models are near human on NazoNazo, which hints that some riddles are lookup [a17].

**Failure modes specific to this subfield.**
- Verification failure: right answer in the log, wrong answer submitted (5.23-39.34%) [a18, d21].
- "Oh!" markers before wrong answers [b19].
- Spontaneous mid-trace shifts are rare (6.31%) and linked to lower accuracy (2.57% vs 16.44%) and do not grow with RL [a20]. This is confounded: hard items may cause both shifts and failure.
- Sycophantic flips under challenge [c26, d08].
- Familiar-framing misapplication [d03, d10].

**Do models have Aha?** No measurement of model self-reports of Aha was found. Aha-like words are present in base models and not tied to accuracy [d04]; they sit on high-entropy forking tokens [d05]. Yang et al. 2025 claim an effect for Aha-trained models; only the abstract was read [b25, c09]. [C]

## 7. What our agent should take

### Add now (established)

1. **Do not label S6 test items "insight" by name.** Tag each item by trace evidence (wrong first frame, frame change, jump) and report by item type. Part: S6 (test set). [E] K01 (the three-criteria tagging itself, K10, is [S]). Evidence: a04, b01, b17, a07, a01.
2. **Never treat an "I see it" or "Oh!" marker as evidence of a correct answer.** Decisions come from external checks (existing G2, G10). Part: G. [E] K02, K23, K24. Evidence: a08, b06, d04, d05, d06, d07.
3. **Use two or more independent indicators for any insight or restructuring flag** and log their agreement. Part: S6 logging (SCHEMA section 6). [E] K05. Evidence: b04, b05, b09, b10.
4. **Report base rates and difficulty per task family; do not pool.** Part: S6 test design; class record in memory. [E] K07, K26. Evidence: b03, b09, b10, d12, d14.
5. **Report consistency across rewrites, not only item accuracy.** Part: S6 test design. [E] K17. Evidence: b23, c21, c22, c23.
6. **Do not use famous public puzzles as the held-out set**; use renewable, post-cutoff or blind items plus a completion contamination test. Part: bench. [E] K25. Evidence: d03, d10, d11, d15, d22, d21.
7. **A written check step is not a check.** Test any verification by whether the answer changes when the check fails. Part: G10 / S8. [E] K24. Evidence: d06, d07.
8. **Score justification separately from the answer, and run several sessions per model.** Part: bench. [E] K16. Evidence: c14, c18, d15.
9. **Do not build the progress monitor on a suddenness signature.** Part: S6 trigger stays code-fired (no pass, no change, repeated error). [E] that measures disagree; the signature itself is [C]. K05, K06. Evidence: b04, b09, b10.

### Test first

| Item | Part | Status | Evidence |
|---|---|---|---|
| Entropy-gated or signal-gated forced reconsideration vs always-on vs never, with cue-free resample control | O / G1 | [S] | K14, K22; a20, c05-c08, d20 |
| Gold-in-trace harvest plus "check every candidate you wrote" step | S4 / G | [S] | K13; a18, b19, d21 |
| "Drop your first grouping" operator on Only Connect style items | O4 / O6 | [S] | K15; b21, c16 |
| Recast narrative puzzles in formal terms (O6 change representation) | O6 | [S] | K18; c25, c26 |
| Does a challenge ("this is wrong") flip correct more than wrong answers? | G | [S] | K18; c26, d08 |
| Does forced step-by-step help or hurt insight items vs matched non-insight at equal tokens? | O / S0 mode | [C] | K11; a14, a16, d01 |
| Large-search vs restructure-only items under varied context budget | memory | [S] | K09; a03 |
| Real-world case set scoring lead-up before the frame switch | S6 test set | [C] | K21; d16, d17 |
| Does agent confidence track speed more than correctness? | G | [S] | K03; a09, a10 |
| Elicit surprise, certainty and suddenness separately from the agent | logging | [S] | K28; d19 |

## 8. Concrete tests on our bench

All arms run at equal total tokens (setup counted, G7). Use at least 3 seeds. Report accuracy, flips of correct answers (correct to wrong), and tokens.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Renewable riddle set (NazoNazo-style open, blind and new items; BRAINTEASER-style multiple choice with rewrites) | plain; best-of-N; scaffold with gated reconsideration; scaffold with always-on reconsideration; cue-free resample | accuracy; correct-to-wrong flips; consistency across rewrites | Gated at least equal to plain; always-on lower (our word puzzles: 92% plain vs 75% forced doubt). Gain over the cue-free resample would be the real effect. |
| T2 | Riddles with known gold answers | plain vs plain plus harvest of every candidate in the trace plus a code test (no extra judge) | share of wrong answers whose trace contains the gold; accuracy | Harvest recovers a share of the 5-39% verification failures. Add if gain holds at equal tokens. |
| T3 | Only Connect walls (original vs WordNet variant) | plain; "drop your first grouping" operator always; operator only after a code-detected stall | walls and groups solved | Operator helps on the original, no change on the variant. Small sample; expect noise. |
| T4 | Same insight items and matched non-insight items (cryptarithmetic-style) | direct answer; forced step-by-step; short reason | accuracy by item class | If human verbal harm transfers: step-by-step lower on insight items, higher on non-insight. d01 suggests it may not transfer. |
| T5 | Narrative brainteasers vs formal recasts (O6) | plain; recast first then solve | accuracy (code check or a judge with agreement verified) | +10 to +17 pp for strong models as in c26; none for small ones. |
| T6 | Mixed set with items where the first move is right and where it is wrong | any arm; log final confidence and tokens to answer | correlation of confidence with tokens vs with correctness | If cue-like, confidence tracks tokens; then confidence stays out of stopping rules. |
| T7 | Answers already correct and already wrong | no challenge vs "this is wrong" prompt | flip rate by correctness | Correct answers flipped more often than wrong ones repaired (c26: over 60% accepted false corrections). |
| T8 | S6 item audit | three-criteria tagging on 100 items plus two indicators (frame change, stall-jump) | indicator agreement (kappa); share passing all 3 | Low agreement expected (humans: per-problem r=.08). Defines the strict subset. |
| T9 | Contamination check | guided completion on every S6 item | share of items completed verbatim | Drop those items; compare accuracy before and after. |

## 9. What does not transfer, and why

- **Warmth ratings.** They need a person pausing every 10-15 s. An agent has no comparable feeling, and the human signature is itself contested [b09, b10]. Use entropy, frame change and checks.
- **Aha as reward or proof.** Aha is a metacognitive judgment from speed and fluency [a10]. A model's "Oh!" is a token on a forking point [d05], present before RL [d04].
- **Verbalisation harm.** Humans lose on Deer when talking aloud (13% vs 57%), but chain-of-thought hurt models on tasks that are not insight tasks, and the human mechanism has no clear model analogue [a14, d01].
- **Working-memory span.** Human span limits do not map to context length; the large-search vs restructure-only split is only a design idea [a03].
- **Pupil size and gesture.** No analogue except internal signals (entropy, probes) [d16, d18].
- **Famous insight problems.** Humans meet them once; models have seen them in training [d03, d11, d22]. Human base rates cannot be copied to models.
- **Magic-trick and visual items.** Text agents do not see them without a vision step.
- **Field insight.** Klein and Jarosz routes (contradiction, connection) cover cases the puzzle literature ignores, but no numbers exist yet [d17].

## 10. Open questions

1. Does an uncertainty-gated forced reconsideration beat always-on and never at equal tokens on insight items? (K22; no test exists.)
2. What do Ash et al.'s three criteria look like in a model trace, and can they be scored automatically?
3. How often is real insight gradual? No number found (K21). Full text of Klein and Jarosz 2011 and Weisberg's work unread.
4. Does the NazoNazo gap replicate in other labs and languages, and is the reasoning-model gain due to length or to verification? (K12, K29)
5. Is the 5-39% verification failure rate reproducible on another puzzle set, and does it survive a measure that excludes rejections? (K13)
6. Do Aha-like markers carry any signal after conditioning on entropy and trace position, in closed models? (K19, K23)
7. Does verbalisation hurt LLMs on insight items at equal tokens? (K11)
8. Do model self-reports of Aha exist and do they track speed as in humans? (K03)
9. What is the contamination rate of classic insight sets (nine-dot, Ansburg and Dominowski, Only Connect)? Nobody has measured it.
10. Per-item insight rate across CRA, matchsticks and riddles together is not available (K26).
11. Is the matchstick Aha-correctness link lab-dependent or task-dependent? (a11)

## 11. Sources

[V] opened (full text or page read in this series), [M] snippet or secondary citation only.

- [V] Ash, Cushen, Wiley (2009) Obstacles in investigating the role of restructuring (abstract page only; PDF blocked). https://docs.lib.purdue.edu/jps/vol2/iss2/3 (a01; b15 is marked [M] in the b file)
- [V] Webb, Little, Cropper (2016) Insight is not in the problem. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035735/ and https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01424/pdf (a02, a04-a07, b01-b03)
- [V] Ash and Wiley (2006) The nature of restructuring in insight. https://link.springer.com/article/10.3758/BF03193814 (a03, b14)
- [V] Danek and Wiley (2017) What about false insights? https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5247466/ (a08, a09, b06-b08)
- [V] Wiley and Danek (2026) Aha! ratings as metacognitive judgments. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13608503/ (a10-a12, a25)
- [V] Smith et al. (2026) Comparing Aha! moments in problem solving and generative ideation. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC13514830/ (a13)
- [V] Macchi, Poli, Caravona (2025) Dissociable effects of verbalization. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11942870/ (a14, a15)
- [V] Salmon-Mordekovich and Leikin (2023) Insight problem solving is not that special. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10366031/ (a16)
- [V] Mizumoto et al. (2025) NazoNazo benchmark. https://arxiv.org/abs/2509.14704 (a17-a19, b18-b20, c01-c04, d21)
- [V] d'Aliberti and Horta Ribeiro (2026) The illusion of insight in reasoning models. https://arxiv.org/abs/2601.00514 (a20, a21, b24, c05-c08, c10, d20)
- [V] Latif et al. (2024) Can OpenAI o1 outperform humans. https://arxiv.org/abs/2412.05753 (a22; not insight evidence); [M] its RAT result as cited in NazoNazo (b26)
- [M] Metcalfe and Wiebe (1987) Intuition in insight and noninsight problem solving. https://link.springer.com/article/10.3758/BF03197722 (a23, b11)
- [M] Bowden et al. (2005) New approaches to demystifying insight, via Webb 2016. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5035735/ (a24)
- [V] Laukkonen and Tangen (2018) How to detect insight moments. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.00282/pdf (b04, b05)
- [V] Hedne, Norman, Metcalfe (2016) Intuitive feelings of warmth and confidence. https://www.frontiersin.org/articles/10.3389/fpsyg.2016.01314/pdf (b09)
- [V] Kizilirmak et al. (2018) Feelings-of-warmth increase more abruptly for verbal riddles. https://www.frontiersin.org/articles/10.3389/fpsyg.2018.01404/pdf (b10, b27)
- [M] Salvi et al. (2016) Insight solutions are correct more often. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035115 (b12; d13 later read it through a page summary, not PDF text)
- [V] Webb et al. (2018) Commentary: Moment of (perceived) truth. https://minerva-access.unimelb.edu.au/server/api/core/bitstreams/955a0d31-bb2c-5eee-9796-21ab686218c0/content (b13)
- [M] Weisberg (2015) Toward an integrated theory of insight. https://doi.org/10.1080/13546783.2014.886625 (b16)
- [M] Danek et al. 2014 / Klein and Jarosz 2011 / Fleck and Weisberg 2013 as cited by Laukkonen and Tangen (b17)
- [V] Alavi Naeini et al. (2023) LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167 (b21, c16, c17, d22)
- [V] Speed (2023) Assessing the nature of large language models. https://arxiv.org/abs/2309.07683 (b22, c11-c13)
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057 (b23, c21); SemEval-2024 Task 9 https://arxiv.org/abs/2404.16068 (c22)
- [V, abstract level] Yang et al. (2025) Understanding aha moments. https://arxiv.org/abs/2504.02956 (b25, c09)
- [M] Wikipedia Insight / field record. https://en.wikipedia.org/wiki/Insight (b28)
- [V] Orru et al. (2023) Human-like problem-solving in ChatGPT. https://pmc.ncbi.nlm.nih.gov/articles/PMC10244637 (c14, c15)
- [V] Zhang et al. (2025) AI delivers creative output but struggles with thinking processes. https://arxiv.org/abs/2503.23327 (c18-c20)
- [V] Tang (2026) BrainBench. https://arxiv.org/abs/2603.14761 (c23, c24)
- [V] Han et al. (2025) Creativity or brute force? https://arxiv.org/abs/2505.10844 (c25-c27)
- [V, abstract page only] Wadhwa et al. (2026) CREATE. https://arxiv.org/abs/2603.09970 (c28)
- [V] Liu et al. (2025) Mind your step (by step). https://arxiv.org/abs/2410.21333 (d01)
- [V] Gema et al. (2025) Inverse scaling in test-time compute. https://arxiv.org/abs/2507.14417 (d02, d03)
- [V] Liu et al. (2025) Understanding R1-Zero-like training. https://arxiv.org/abs/2503.20783 (d04)
- [V] Wang et al. (2025) Beyond the 80/20 rule. https://arxiv.org/abs/2506.01939 (d05)
- [V] Chen et al. (2025) Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (d06)
- [V] Zhang et al. (2025) Reasoning models know when they're right. https://arxiv.org/abs/2504.05419 (d07)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d08)
- [V, no effect sizes] Kadavath et al. (2022) Language models (mostly) know what they know. https://arxiv.org/abs/2207.05221 (d09)
- [V] McCoy et al. (2023) Embers of autoregression. https://arxiv.org/abs/2309.13638 (d10)
- [V] Golchin and Surdeanu (2024) Time travel in LLMs. https://arxiv.org/abs/2308.08493 (d11)
- [V] Danek et al. (2014) It's a kind of magic. https://pmc.ncbi.nlm.nih.gov/articles/PMC4258999/ (d12)
- [V] Normative data for 111 CRA problems in Romanian (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6737282/ (d14)
- [V] Generative AI models outperform students (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12546817/ (d15)
- [V] Tabatabaeian et al. (2025) PNAS, mathematicians' foreshadowing. https://pmc.ncbi.nlm.nih.gov/articles/PMC12415256/ (d16)
- [V, abstract only] Klein and Jarosz (2011) A naturalistic study of insight. https://doi.org/10.1177/1555343411427013 (d17)
- [V] Macchi et al. (2026) Pupil dilation and unconscious analytic thought. https://pmc.ncbi.nlm.nih.gov/articles/PMC13608808/ (d18)
- [V] Surprise! Clarifying the link between insight and prediction error (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11680657/ (d19)
