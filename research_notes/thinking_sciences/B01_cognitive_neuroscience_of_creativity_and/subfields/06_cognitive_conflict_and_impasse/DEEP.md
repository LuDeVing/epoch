# Cognitive conflict and impasse: deep document

*Subfield B01.06. Sources: evidence_a-d.jsonl (a01-a28, b01-b25, c01-c27, d01-d16), claims.jsonl (K01-K34), critique.md. Status marks follow SCHEMA.md: [E] established (two or more independent sources), [S] single source, [C] contested. Evidence ids are cited in brackets.*

## 1. What it is

Cognitive conflict is the moment a solver detects that new information does not fit the mental picture of the problem they hold now. It is not response conflict (Stroop, flanker). It is a clash between a representation and a fact [a01]. If the clash cannot be resolved, the solver is at an impasse: no move looks useful. Resolving it needs restructuring, which means a new view of the problem [a01, a08].

The Danek and Flanagin (2019) review frames two parts: conflict (detect the mismatch) and restructuring (build a new representation). Our schema uses this as the S6 trigger: conflict between output and expected result. S6 is fired by code, not by the model's own feeling of being stuck.

Three things matter for an engineer.
- The human evidence for conflict as its own step is thin: one fMRI study (N=30), one small ERP study (N=14), no independent replication [critique].
- The human evidence for impasse and restructuring as behaviour is stronger and older (Knoblich 1999, Knoblich 2001, Fedor 2015).
- Every LLM paper that touches this tests a neighbouring construct (knowledge conflict in QA, self-correction, fixation, wrong-frame repetition). None tests a conflict trigger inside a solver stuck under a wrong frame, except as benchmarks.

Boundary with other subfields (not covered here): productive failure, calibration, search over thoughts, anomalies and paradigm change, creative problem solving, reflection-in-action, priming of orientation. Only links are noted in section 10.

## 2. History and theories in depth

**Gestalt background.** Insight problems are hard because the first representation is wrong. This is the root of all later accounts.

**Kaplan and Simon (1990), incomplete encoding.** Search happens in a space of problem representations. Failure comes from an encoding that leaves out what is needed, and the solver must search for a better encoding. Seen only via secondary text [a12, M].

**Ohlsson (1992), representational change theory (RCT).** The initial representation is misleading, built by prior knowledge. Impasse happens when no operator in that representation leads on. Escape needs one of: constraint relaxation (drop an assumed rule), chunk decomposition (split a familiar unit), or re-encoding (add or change elements). Seen only via secondary text [a28, M] and through Knoblich 1999, which tests it.

**Knoblich, Ohlsson, Haider and Rhenius (1999), the founding test [a08-a11].** Matchstick arithmetic (move one stick to fix a false equation). Type A changes the result value (narrow constraint). Type B changes an operator (wider). Type C needs a tautology (widest). Type D needs a tight chunk broken (XI as one unit). Predictions: harder with wider constraint and tighter chunk. Both were confirmed (section 3). They also showed transfer: solving a hard type once makes the same type easy, which supports relaxation of the constraint itself.

**Knoblich, Ohlsson and Raney (2001), eye movements [a13].** Fixation times lengthen over time on hard problems (impasse). Attention is biased to numerals before the operator constraint is relaxed. This supports a misleading initial representation as the cause of impasse.

**Cognitive conflict as a neural step.** Luo, Niki and Phillips (2004) found an N380 at Cz with an ACC dipole when a riddle solution broke the first reading [b05, b25]. Luo and Knoblich (2007) argued conflict is needed before restructuring (only seen relayed [a06, M]). Qin et al. (2009) argued ACC marks subgoal handling after a candidate is retrieved, not the stuck state [b06]. Danek and Flanagin (2019) tested conflict directly with fMRI and found posterior visual, thalamic and hippocampal activity, not mainly ACC [a03, b01].

**Process accounts of the whole episode.** Fedor, Szathmary and Ollinger (2015) showed the classic stage order (search, impasse, insight, search) fits only about half of solvers [a14]. Ollinger et al. (2017) showed relaxing the right constraint is necessary but not sufficient [a18]. Wiley and Danek (2023/2024) is a review of restructuring and Aha, not opened [a27, d15, M].

**Competing explanations to hold in mind.**
- Incomplete vs misleading encoding (Kaplan-Simon vs Ohlsson): not separable with the Knoblich data [a11].
- Impasse as a distinct stage vs as a recurring event [a14].
- Conflict in ACC vs in posterior and subcortical regions [K09].
- Incubation as help vs null [a16].

**LLM-era neighbours.** Knowledge conflict (Xie 2024, Xu 2024) [a20, a21, a23]. Intrinsic self-correction (Huang 2024, Kamoi 2024, Tyen 2024, Kumar 2024) [b11-b17]. Fixation and Einstellung (Naeini 2023, Kim 2025/2026, Chen 2026) [c04-c08]. Machine insight (Mizumoto 2025, d'Aliberti and Ribeiro 2026, Tsui 2026) [a24, b18-b22].

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| A cue that contradicts the false view raises solving; an agreeing cue does not | Magic tricks, fMRI. Solve rate 0.59 vs 0.26, F(1,570)=58.81, d=0.64. Helpfulness 0.72 vs 0.26, F=107.33, d=0.87. 572 valid trials, N=30. Cue conditions 42.3 / 28.7 / 29.0% | Danek and Flanagin 2019 [a02, b01, b02] | Single-source |
| Conflict maps to posterior visual areas, thalamus, hippocampus, temporal lobes, frontal eye fields; reverse contrast empty | p<.001 voxel, p<.05 FWE cluster | Danek and Flanagin 2019 [a03] | Contested (vs ACC accounts) |
| Fast mismatch signal when a solution breaks the first reading | N380 peak 380 ms at Cz, ACC dipole, 14 subjects, 120 riddles | Luo, Niki, Phillips 2004 [b05, b25] | Single-source |
| ACC engaged after a candidate is retrieved, not while stuck | 20 adults, 30 s remote-associate items | Qin et al. 2009 [b06] | Contested |
| Wider constraint = harder | Median time A 40 s, B 155 s, C 300 s (cap), D 140 s; N=20; type effect F(3,57)=7.11, p<.001 | Knoblich 1999 Exp 1A [a08] | Established (two papers) |
| Eye-tracked solve rates by problem | A 23/24, C 18/24, B 9/24; B vs A chi2=18.38, p<.001; N=24 | Knoblich 2001 [a13] | Established with Knoblich 1999 |
| Constraint scope and chunk tightness are separate difficulty sources | Type D vs A T=10, p<.001; A vs B T=12; B vs C T=41, p<.05; N=20 | Knoblich 1999 [a11, b09] | Established |
| One solved hard item makes the same type easy in-session | Type x block F(3,57)=3.24, p<.05; transfer B p<.05, C p<.001, A p=.80 | Knoblich 1999 [a09, b08] | Single-source (one session, one format) |
| Telling solvers a forbidden form is allowed removes the difficulty | Exp 3, N=34. Regular-first group solved 61% of Type C in Block 1; tautology-first solved all; Block 2 92% vs 94%; chi2(1)=12.59 | Knoblich 1999 Exp 3 [a10] | Single-source |
| Classic stage order is followed by half of solvers | 19/39 solvers (49%) vs 8/62 non-solvers (13%); chi2(1,N=101)=41.42, phi=.64. 129 recruited, 101 analysed | Fedor 2015 [a14] | Single-source |
| People cannot report impasse reliably | Insight reported by 74% of solvers (29/39) vs 10% of non-solvers (6/62); impasse reports did not rise during behaviourally defined impasse | Fedor 2015 [a15] | Established (with Hedne) |
| Warmth ratings do not separate insight from non-insight solutions; wrong insight answers repeat later | N=51, 32 videos; 971 trials analysed (661 excluded); 29% insight; alpha=.911 | Hedne 2016 [a17] | Single-source |
| Relaxing constraints needs a search criterion | N=120 (4 x 30). Maximization OR 2.18 (CI 1.04-4.57); variation OR 3.99; Nagelkerke R2=.61; 28% of maximization group still failed | Ollinger 2017 [a18] | Single-source |
| Sleep or incubation does not help restructuring | N=77; incubation F(1,64)=0.008, p=.930; sleep p=.829; REM 20.6% vs 19.8% | Schonauer 2018 [a16] | Contested (Cai 2009 REM not opened) |
| Physical handling of sticks does not reliably help | Three series, Bayesian regression, ROPE +/-0.2 log-odds; movements low; null | Spiridonov 2025 [b10] | Contested (original not opened) |
| Intrinsic self-review lowers accuracy | GPT-3.5 CSQA 75.8 / 38.1 / 41.8 (calls 1/3/5); GSM8K 75.9 / 75.1 / 74.7; GPT-4 GSM8K 95.5 / 91.5 / 89.0 | Huang 2024 [a22, b11, c11] | Established |
| Neutral review wording does not remove the loss | GPT-4-Turbo GSM8K 91.5 to 88.0 / 90.0 (neutral), 90.0, 91.0; Llama-2 CSQA 64.0 to 37.5 / 36.5 (neutral); wording moves GPT-4-Turbo CSQA round 1 by up to 7 points (81.5, 74.5, 81.5) | Huang 2024 tables 5-6 [d08] | Established |
| Locating the mistake is the bottleneck | GPT-4 found the mistake in 52.87% overall; given the location, backtracking added +18.04 to +43.92 points on wrong traces; oracle labels lifted GPT-4 HotpotQA 49 to 59 | Tyen 2024, Huang 2024 [b14, c13, c26, c12] | Established |
| RL-trained self-correction cuts right-to-wrong flips | Gemini Flash right-to-wrong 15.8% before SCoRe vs 1.4% after; MATH500 52.6 to 41.4 prompt-only | Kumar 2024 [b15] | Established (with Kamoi) |
| Self-correction works with reliable external signals | Survey: gains in realistic settings need external feedback or fine-tuning | Kamoi 2024 [b16, b17, c14, c25] | Established |
| Self-correction blind spot | 64.5% blind spot across 14 non-reasoning models (62.8% in another cut); "Wait" cut it 89.3%, mean accuracy +156%; Haiku 52.5%, Sonnet 4 41.4%; 5,306-trace fine-tune cut it 76.0%, think traces stripped only 38.1% | Tsui 2026 [b21, b22] | Single-source |
| Blind spot is mostly non-reasoning mode | Qwen3-14B non-thinking 0.117 to 0.868 with "Wait" (thinking mode 0.843); DeepSeek-V3 0.567 to 0.902 vs R1 0.908 | Tsui v3 [d04] | Established (with Kim 2026) |
| Spontaneous "Aha" shifts are rare and not helpful in small RL models | 6.31% of traces; Qwen2.5-1.5B 2.57% vs 16.44% (N=723,200); formal detector 1.79%; AME -0.0311 and -0.0615 | d'Aliberti and Ribeiro 2026 [b18, b20, c17] | Single-source |
| Aha-word self-reflection is not tied to accuracy | Present in base models; R1-Zero responses with reflection not more accurate | Liu 2025 [d12] | Single-source |
| A cue added by code under high entropy lifts accuracy | MATH-500 Pass1 0.3221 to Pass2 0.4062 (+8.41 pp); crosswords +0.45 pp (0.0970 to 0.1015); Rush Hour +0.01 pp; high-entropy raw -7.40 pp, low-entropy -22.88 pp; 50,574 vs 23,500 | d'Aliberti and Ribeiro 2026 [b19, c18] | Contested (Pass 2 is a second sample) |
| Blind extension with "Wait" loses to parallel samples at equal tokens | Small distilled models: GSM8K 1.5B -11.8% vs +10.1% for parallel; accuracy 87.3% at 1100 tokens falling to 70.3% at 15980; parallel about 22% higher at 16K | Ghosal 2025 [d01] | Contested |
| Sequential "Wait" gains in s1 (different-model comparison) | AIME24 50.0 to 56.7 at 4x | Muennighoff 2025 [d02] | Single-source |
| Confidence-based trace filtering saves tokens | Up to 84.7% fewer tokens; GPT-OSS-120B AIME25 99.9 vs 97.0 majority; HMMT25 92.9 to 88.9 when filtered hard | Fu 2025 DeepConf [d03] | Single-source |
| Models accept a coherent counter-answer, favour memory-matching evidence | 8 LLMs, 500-1,356 conflict examples each; evidence order changes answers over 5% for most, over 30% for PaLM2 and Llama2-7B; StrategyQA integration failed in 38.2% | Xie 2024 [a20, a21, c09, c23] | Single-source (survey a23 agrees) |
| Red-herring fixation in LLMs | Only Connect: GPT-4 0-shot 6 walls solved with herrings, 68 on randomised set, 471 on no-herring set; humans 285/494 walls | Naeini 2023 [c04, c20] | Established |
| Clinical fixation | M-ARC best models about 50% vs physicians 66%; MedEinst 5,383 paired cases, 49 diseases, 17 LLMs, trap rate 43-61%, robust accuracy 11-12% | Kim 2025, Chen 2026 [c05, c07, c22] | Established |
| Newer reasoning models close the gap on M-ARC | Best reasoning model 0.751 vs physicians 0.66 | Kim 2026 [c06] | Contested |
| Riddle insight gap | NazoNazo 201 riddles: humans 52.9% (n=126); non-reasoning 7.6%; reasoning 17.6%; verification failures 5.23% to 39.34% of wrong answers (Opus 4 25.00%) | Mizumoto 2025 [a24, c01, c02, c21] | Single-source |
| Debate does not fix a dominant wrong prior | MedEinst Qwen3-32B: base robust 11.86%; MDAgent, DyLAN about 8-10%; evidence-audit scaffold 24.21% (accuracy 69.49%, trap 33.75%) | Chen 2026 [c08] | Single-source (authors' own method) |
| Irrelevant context drops math accuracy | No more than 18% of baseline-solved problems stayed solved across all distractor types; self-consistency (20 samples) recall 99.7% | Shi 2023 [c15, c27] | Single-source (old models) |
| Failure-triggered reflection works with a reliable signal | ALFWorld 130/134, HumanEval pass@1 91%; +22% ALFWorld, +20% HotPotQA, +11% HumanEval | Shinn 2023 [c16] | Established (with Kamoi) |
| Wrong frames repeat in coding agents | 1,750 trajectories, 50 tasks, 4 models, 5 runs. Silent failure (5/5 submit, 0/5 resolve) 80% of Llama 4 failing runs, 68% GPT-5 (19/50 tasks), 16% Gemini. Patch cosine 0.80-0.91 vs 0.48-0.57. Pre-edit guards: Claude 65.2 to 64.8; GPT-5 44.4 to 46.0 / 44.0 | Mehta 2026 [d06, d07] | Single-source |
| 3-gram repeat detector flags stalls | 100% of one model's no-submit tasks, no false positives on two others; harness rule: window 20, pause at 3 repeats, no measured gain | Mehta 2026, terminal-agent paper [d07, c19] | Single-source |
| Adding missing information beats a wrong-frame fix | MathSticks: text equation input raised o3 38.50 to 60.00, Gemini-2.5-Pro 22.50 to 45.25; humans (3 adults) 91.72% | Ji 2025 [d13] | Single-source |
| Hints change behaviour but are rarely reported | CoT verbalised the used hint in 25% (Claude 3.7 Sonnet) and 39% (R1) | Chen 2025 [d14] | Single-source |
| Stored failure lessons transfer modestly and can harm | SWE-Bench-Verified flash 34.2 to 38.8; pro 54.0 to 57.4; WebArena Multi +4.6 over best baseline (AWM below no-memory; AWM 44.4 to 42.2 with failures); Trace2Skill best cell +57.65 pp with cells at -7.70, -6.36, -5.83; EDV tau2 Pass@1 85.1 vs 76.4 | Ouyang, Ni, Zhu 2026 [d09-d11] | Established (three sources, modest) |
| Self-written lessons can store the agent's own error | Self-Confirmation Trap Rate 11.0% under reflection memory, 5.0% with third-party distillation | Zhu 2026 [d11] | Single-source |
| Mental set in LLMs | Llama-3.1-8B shortcut problems exact match 0.16 (few-shot); 12 problems only | Haq 2025 [a26] | Single-source (tiny) |

## 4. Mechanisms and models

### 4.1 The human model, as a program

Representational change theory can be written as a loop. An engineer can implement the skeleton.

1. State: a representation R0 (objects, assumed rules, chunks treated as units). Operators are those legal under R0.
2. Search under R0 until no operator raises a progress score. This is the impasse. In code it is a measured condition, not a feeling (see 4.3).
3. Conflict detection: a new fact F (a failing test, an output that differs from expected) contradicts something R0 predicts. Record the pair (prediction, fact).
4. Restructure. Pick one of three moves:
   - Relax a constraint: remove one assumed rule from R0 and re-enter search. Wider constraints cost more (Type A < B < C).
   - Decompose a chunk: re-tokenise a unit into parts. Tighter chunks cost more (Type D).
   - Re-encode: add missing information (see K33).
5. Re-search under R1. Add a score so search is guided (Ollinger: relaxation alone is not enough [a18]).
6. If R1 fails, the impasse recurs. Allow more than one pass: only about half of solvers follow one clean cycle [a14].
7. Store the relaxed constraint as a lesson with its problem type. In the human data, transfer follows the constraint, not surface form [a09].

### 4.2 Two sources of difficulty

Keep two fields in the S6 state line: `scope` (how wide a rule must be relaxed) and `tightness` (how strongly the problem is chunked into units). Different repairs apply. Scope is helped by naming candidate constraints that may be dropped (Knoblich Exp 3 [a10]). Tightness is helped by re-tokenising: split numbers, words, objects. This maps to O4 (drop constraint) and O6 (change representation).

### 4.3 Conflict triggers an engineer can compute

None is established against the others (K25-K28). All fire in code.

| Trigger | What it sees | Evidence |
|---|---|---|
| Failing check or output differs from expected result | A real mismatch, the S4 fail | Strongest basis: external signals make self-correction work [b14, c16, b16] |
| Same error twice or no change after two rounds | Stall | Already in S6 |
| Repeated tool call (md5 of name and args, window 20, 3 repeats) | Loop only, not confident wrong fixes | [c19, d07] |
| Repeated 3-gram in output | Stall in text | [d07], 100% of one model's no-submit tasks |
| Token entropy or low-confidence window | Model uncertainty | [b19, d03], mixed: helps on math, can mislead when confidently wrong |
| Sample disagreement | Conflict among attempts | Fails on wrong frames: samples agree and are wrong [d06] |
| Model says "I am stuck" | Self-report | Unreliable in people [a15] and in models (r = .17, per SCHEMA S6) |

### 4.4 How to present a clash to the model

From the knowledge-conflict work [a20, a21, a23, c23]:
- A single coherent contradiction is accepted. A noisy or incoherent one is resisted.
- Evidence order changes answers, over 5% for most models.
- Show the failing output, located by code (G2), and name the step [b14].
- Attribute the draft to another author when checking it; models catch the user's error and miss their own [b21]. Single source, non-reasoning models.
- Keep the review prompt neutral and let code adopt the revision only if the check improves; a review prompt alone flips right answers to wrong [b13, c24, d08].

### 4.5 Hint injection

A relaxation hint ("this rule may be dropped") worked for humans [a10]. It is untested for LLMs (K34). Models use hints and rarely say so [d14], so log hint injection in code, not from the model's report.

## 5. What holds up

**Replicated or supported by two or more sources.**
- Wider constraint and tighter chunk make insight problems harder, shown in 1999 and again with eye tracking in 2001 [a08, a11, a13]. Same lab group, so independence is partial.
- Intrinsic self-correction without an external signal does not help and often hurts (Huang, Kamoi, Kumar, plus Tsui for the blind spot) [K11].
- The bottleneck is locating the error, not fixing it [K12].
- Failure-triggered, signal-backed reflection works [K21].
- LLM fixation on familiar-but-wrong cues exists across Only Connect, M-ARC, MedEinst [K17].
- People cannot report their own impasse or progress [K06].
- Stored lessons give small average gains and some harm [K31].

**Failed, null or contested.**
- Incubation and sleep: null in Schonauer 2018 [a16]; Cai 2009 REM benefit not tested there.
- Physical interaction helping matchstick solving: null in Spiridonov 2025 [b10].
- Blind "Wait" at equal tokens: loses to parallel sampling in small models [d01]; wins in s1 only against different models [d02].
- Pre-edit "check your reading" prompts did not move resolve rate [d07].
- Debate does not fix a dominant wrong prior [c08].
- Spontaneous Aha shifts do not become useful with training [b20].
- Brain-region claims for conflict: ACC (Luo 2004, Dietrich and Kanso) vs posterior and subcortical (Danek 2019) vs subgoal handling (Qin 2009).

**Moderators.**
- Reasoning mode: the blind spot and the "Wait" effect belong mostly to non-reasoning mode in open models [d04]. Frontier closed models were not retested.
- Source of the cue: code-added cues help; model-initiated shifts do not [b19, b20].
- Task: math +8.41 pp, crosswords +0.45, Rush Hour +0.01 [c18]. Gains depend on whether the task has a foothold (consistent with G12).
- Model age: Huang, Tyen, Shi, Naeini used 2023-era models. Kim 2026 shows reasoning models close the M-ARC gap (0.751) [c06] but riddles still show a gap (17.6%) [c21].
- Attribution: user vs self [b21].

**Interventions that worked.**
- A contradicting cue, with humans (59% vs 26%) [b01].
- An explicit relaxation hint, with humans [a10].
- Hint plus search criterion, with humans [a18].
- Naming the error location, for LLMs [b14].
- External feedback and test-run signals [c16, b16].
- Adding missing information (text for image) [d13].
- Token-confidence filtering [d03].
- Code-added "Wait" for non-reasoning mode [d04, b21].

**Interventions that did not work.**
- Self-review with no feedback, in any of three wordings [d08].
- Sleep or distraction [a16].
- Agreeing hints (humans) [b02].
- Majority voting against a shared wrong frame [d06, c08].
- More in-context examples against red herrings [c20].

## 6. Language models

**Self-correction.** Without an external signal, models lose accuracy. GPT-3.5 CSQA fell 75.8 to 38.1 in one round. GPT-4 GSM8K fell 95.5 to 91.5 to 89.0 [b11]. Most of the loss is right answers changed to wrong because the review prompt implies an error [b13, c24]. Neutral wording did not remove it [d08]. Oracle labels in earlier papers inflated gains (GPT-4 HotpotQA 49 to 59) [c12].

**Locating the mistake.** GPT-4 found the mistake in 52.87% of cases, but given the location, backtracking added +18.04 to +43.92 points [b14, c13]. People also fail to find their own impasse by introspection [a15], so the fix is the same: a code-located signal.

**Blind spot.** Models fix an error attributed to the user and miss the same error attributed to themselves: 64.5% blind spot across 14 non-reasoning models. Appending "Wait" cut it 89.3% [b21]. In reasoning mode it is small or negative [d04]. The author says the cause is training data (few self-correction demos), not capability [b22]. A spectral explanation (Petrova and Vejsiu) was read as abstract only [d05, M].

**Machine insight.** Spontaneous mid-trace Aha shifts in small RL models were 6.31% of traces and tied to lower accuracy (2.57% vs 16.44% for Qwen2.5-1.5B) [b18]. A code-added reconsideration cue under high entropy gave +8.41 pp on MATH-500 [b19], but Pass 2 is an extra sample, so compute is confounded. Ghosal found blind extension loses to parallel samples at equal tokens [d01].

**Fixation.** GPT-4 on Only Connect walls solved 6 with red herrings, 68 on a reduced-herring set, 471 on a no-herring set [c04]. On M-ARC the best models reached about 50% vs 66% for physicians [c05]; reasoning models reached 0.751 [c06]. MedEinst trap rates of 43-61% hold even for top-accuracy models [c07]. NazoNazo riddles: non-reasoning 7.6%, reasoning 17.6%, humans 52.9% [c01]; verification failure means the right answer appeared in the trace and was not kept [c02]. Mental-set tests on three LLMs show chain of thought raises accuracy but uses more steps [a26].

**Wrong frames repeat.** In coding agents 68 to 80% of failing runs for two models were identical failures across 5 runs [d06]. Agreement between samples is therefore not a conflict signal (G4). Pre-edit "check your reading" prompts did not help [d07].

**Context clash.** One irrelevant sentence cut math accuracy; only 18% of solved problems stayed solved under all distractors [c15]. Models take a coherent counter-answer and prefer memory-matching evidence [a20, a21].

**Memory.** Lessons from failures give modest gains (+4.6 pp on WebArena Multi; 34.2 to 38.8 on SWE-Bench-Verified) and some harm [d09, d10]. Self-written lessons can store the model's own mistake [d11].

**Hints.** Models use hints and verbalise them in only 25% (Claude 3.7 Sonnet) to 39% (R1) of cases [d14]. No LLM test of a relaxation hint exists.

**Net.** What changes outcomes is a signal from outside the model: tests, error location, a code-added cue, added missing input. What does not: asking the model to reflect, debate, agreement, a generic instruction.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| S6 trigger stays code-driven (failing check, repeated error, no change in two rounds). Do not use the model's self-report of being stuck. | G1, S6 | [E] | K06, K11, a15, b11, c16 |
| Name the failing step in S5 and S6 prompts. The repair prompt shows the located failing output, not "something is wrong". | G2, S5 | [E] | K12, b14, c13 |
| Adopt a revision only when a code check improves. Count flips of right answers. | G2, S5 | [E] | K22, K30, b13, d08 |
| Write O6 as two moves: relax a stated rule (scope) and split or re-tokenise a unit (tightness). Different problems need different moves. | O4, O6 | [E] | K02, a08, a11, a13 |
| Fixation is real. A retry after a failed reading must be fresh (S3 already does this); do not show the prior failed frame in the repeat attempt. | S3 | [E] | K17, c04, c07, c20 |
| Test the scaffold on a reasoning-model baseline, not only a non-reasoning one. | G7 | [E] | K29, d04, c06 |
| Do not use debate or majority agreement as a conflict signal. | G4, G9 | [E] | K20, K28, c08, d06 |
| Memory: store each lesson with an applicability condition and problem class; trust it only after it helps on two problems (already in SCHEMA section 5). | memory | [E] | K31, d09-d11 |
| Do not add incubation, sleep, forced pause, or physical-interaction analogues. | 4b | [E]/[C] | K08, K23, a16, b10 |

### Test first

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Code-inserted reconsideration cue (the located contradiction, or "Wait") gated on a failing check, vs a second plain sample at equal tokens | S6 | [C] | K15, K26, b19, d01, d02 |
| Conflict signal ranking: failing check vs repeated call vs entropy vs disagreement | S6 | [S] | K25, K27, K28, c19, d03, d07 |
| Tag a stall as missing information or wrong frame; add information first | S6 | [S] | K33, d13 |
| Relaxation hint list ("these rules may be dropped") at impasse | O4 | [S] (human only) | K03, K34, a10 |
| Reframe plus a search score and an "attempts must differ" rule | O6, S3 | [S] | K07, a18 |
| Allow the impasse trigger more than once per task, with a cap | S6 | [S] | K05, a14 |
| Present the draft as another author's work at check time | G5, S5 | [S] | K13, b21 |
| Store "assumption X was wrong" lessons, offered after the first attempt; test same-type and different-type | memory | [S] | K04, K31, K32, a09 |
| Admit lessons only after a code check or a different model confirms | memory, S9 | [S] | K32, d11 |
| Order and phrasing of a clash (one coherent contradiction, fixed order) | S5 | [S] | K19, a20, a21 |
| Counterfactual pair test against a dominant wrong prior | S7 | [S] | K20, c08 |

## 8. Concrete tests on our bench

All arms use equal total tokens. Report solve rate, tokens per state, flips right-to-wrong and wrong-to-right, and the trigger that fired.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Items with a runnable check where plain first attempts fail (ARC-like, code, our word and brainteaser sets) | (a) cue gated on failing check, code inserts the located failing output; (b) generic "try again"; (c) second plain sample | Solve rate at equal tokens | (a) beats (b) by several points; (a) vs (c) unknown; keep only if (a) is at least 3 pp above (c) |
| T2 | Same items, stalls marked by humans or by final failure | Trigger = failing check / repeated 3-gram or tool call / token entropy / sample disagreement / model "are you stuck?" | Precision and recall against marked stalls | Failing check highest precision; repeat count high recall on loops; disagreement low on wrong frames |
| T3 | BrainTeaser and lateral riddles with one hidden constraint | Relaxation hint list vs no list vs a same-length distractor list | Solve rate; hint use logged in code | Hint list helps where the blocked constraint is on it; distractor list gives no gain |
| T4 | Our own matchstick-style equation items with Type A to D structure | O6 as one move vs split into scope and tightness moves | Solve rate by type | Split helps types B and D more than A |
| T5 | Stuck items after a located failure | Repair prompt naming the failing step vs "something is wrong" vs no repair | Fix rate | Named step far higher (Tyen: +18 to +44 points) |
| T6 | Items with a right first attempt | Neutral review with code adopting a revision only if the check improves vs adopt-always | Right-to-wrong flips | Gated adoption removes flips; ungated loses several points |
| T7 | Items with a dominant wrong prior or red herring (Only Connect style, M-ARC-like) | Retry shown the prior failed frame vs fresh retry vs fresh retry plus "distractor" tag | Solve rate | Fresh retry beats shown-frame retry |
| T8 | Same items in reasoning and non-reasoning mode | Draft framed as user's vs as model's own | Error catch rate | Gap in non-reasoning mode, small in reasoning mode |
| T9 | 20 same-type impasse tasks then 20 different-type tasks | Lesson "assumption X was wrong" with applicability condition vs no lesson vs generic lesson | Solve rate on same-type; harm on different-type | Same-type gain; harm under 2 pp on different-type |
| T10 | Stalls with possibly missing input | Add-information first vs change-frame first, tagged by code | Repair rate | Add-information first wins on missing-input stalls |
| T11 | Tasks with several failure episodes | One-shot reframe vs up to 3 reframes (cap) | Solve rate and tokens | Multi-fire helps on hard items, costs tokens on easy items |

## 9. What does not transfer, and why

- **Neural region claims (ACC, thalamus, visual cortex).** No agent mechanism. Contested even in humans [K09]. Use behavioural triggers.
- **The N380 and brain timing.** It informs only the idea of a cheap check right after output [K10].
- **Aha feeling and warmth.** Humans use it as a marker. LLMs have no measured counterpart; Aha words in traces are not tied to accuracy [d12]. Warmth ratings do not even track insight in people [a17].
- **Incubation and sleep.** Null result, and no LLM analogue except a context reset [K08].
- **Physical interaction.** Null in humans and no counterpart [K23].
- **Self-report of impasse.** Unreliable in humans [a15]; the schema already avoids it.
- **One-session transfer of a relaxed constraint.** Human transfer is shown only within one session [a09]. For LLMs memory is a text lesson, with harm risk [d09-d11].
- **Matchstick arithmetic results as general.** Narrow, well-structured; N=20 to 34 [a08, a13].
- **Knowledge-conflict QA results as impasse results.** A prompt-vs-memory clash is not a solver stuck under a wrong frame [critique].
- **Magic-trick fMRI cue design.** The cue is applied after viewing, so it is a contradicting hint, not a clash the solver detects alone [critique].

## 10. Open questions

1. Does a code-fired conflict cue beat a plain second sample at equal tokens on frontier reasoning models? Not tested cleanly [K15, K26].
2. Which code signal best predicts a wrong frame? No head-to-head [K25-K28].
3. Does a relaxation hint help LLMs on matchstick or lateral items? Never tested [K34].
4. Do current frontier reasoning models still show red-herring fixation and verification failure? Mixed [K18, K29].
5. Does a stored "assumption X was wrong" lesson transfer to later same-type tasks and harm different-type tasks? [K31]
6. Is conflict a separate step from restructuring in an independent human replication? Candidates not opened: Wiley and Danek 2023, a 2026 pupil-dilation study [d15, d16].
7. How often is a confident new frame wrong (false insight) in LLM traces? [c03, a17]
8. What phrasing, order and attribution of a clash works inside an agent loop? [K19]
9. Does a neutral review prompt help current reasoning models? Closed only for weaker models [K30].
10. Does incomplete encoding (Kaplan and Simon) or misleading encoding (Ohlsson) better describe LLM failures, and do they need different repairs? [K33]
11. Links to parallel subfields, not covered here: productive failure (what to learn from the failed attempt), calibration (when to trust the signal), search over thoughts and Tree of Thoughts (how to expand after the impasse), anomalies and paradigm change (conflict at scale), reflection-in-action, priming of orientation, premature closure.

## 11. Sources

[V] opened; [M] snippet only or relayed.

- [V] Danek and Flanagin (2019), Cognitive conflict and restructuring. https://aimspress.com/aimspress-data/aimsn/2019/2/PDF/neurosci-06-02-060.pdf (a01-a05, a07, b01-b04, b23, b24)
- [V] Knoblich, Ohlsson, Haider and Rhenius (1999), Constraint relaxation and chunk decomposition. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (a08-a11, b07-b09)
- [V] Knoblich, Ohlsson and Raney (2001), An eye movement study of insight problem solving. https://link.springer.com/content/pdf/10.3758/BF03195762.pdf (a13)
- [V] Fedor, Szathmary and Ollinger (2015), Five square problem. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4523725/fullTextXML (a14, a15)
- [V] Schonauer et al. (2018), Sleep does not promote solving insight problems. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5834438/fullTextXML (a16)
- [V] Hedne, Norman and Metcalfe (2016), Warmth and confidence. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5005374/fullTextXML (a17)
- [V] Ollinger, Fedor, Brodt and Szathmary (2017), Ten-penny problem. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5533865/fullTextXML (a18)
- [V] Tik et al. (2018), Ultra-high-field fMRI insights on insight. https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6055807/fullTextXML (a19)
- [V] Luo, Niki and Phillips (2004), Aha effects in a guessing riddle task. https://pmc.ncbi.nlm.nih.gov/articles/PMC6871977 (b05, b25)
- [V] Qin, Anderson et al. (2009), Lateral inferior prefrontal cortex and ACC. https://pmc.ncbi.nlm.nih.gov/articles/PMC2705531 (b06)
- [V] Spiridonov et al. (2025), Sources of difficulty in interactivity. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2025.1691864/full (b10)
- [V] Xie et al. (2024), Adaptive chameleon or stubborn sloth. https://arxiv.org/abs/2305.13300 (a20, a21, c09, c23)
- [V] Xu et al. (2024), Knowledge conflicts for LLMs: a survey. https://arxiv.org/abs/2403.08319 (a23, c10)
- [V] Huang et al. (2024), LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (a22, b11-b13, c11, c12, c24, d08)
- [V] Tyen et al. (2024), LLMs cannot find reasoning errors. https://arxiv.org/abs/2311.08516 (b14, c13, c26)
- [V] Kumar et al. (2024), SCoRe. https://arxiv.org/abs/2409.12917 (b15)
- [V] Kamoi et al. (2024), When can LLMs actually correct their own mistakes. https://arxiv.org/abs/2406.01297 (b16, b17, c14, c25)
- [V] d'Aliberti and Ribeiro (2026), The Illusion of Insight in Reasoning Models. https://arxiv.org/abs/2601.00514 (b18-b20, c17, c18)
- [V] Tsui (2026), Self-Correction Bench. https://arxiv.org/abs/2507.02778 (b21, b22, d04)
- [V] Mizumoto et al. (2025), The Metacognitive Bottleneck (NazoNazo). https://arxiv.org/abs/2509.14704 (a24, a25, c01-c03, c21)
- [V] Haq et al. (2025), Is your LLM trapped in a mental set? https://arxiv.org/pdf/2501.11833 (a26)
- [V] Naeini et al. (2023), LLMs are fixated by red herrings. https://arxiv.org/abs/2306.11167 (c04, c20)
- [V] Kim et al. (2025), M-ARC. https://arxiv.org/abs/2502.04381 (c05, c22)
- [V] Kim et al. (2026), Advances in LLM reasoning enable flexibility. https://arxiv.org/abs/2601.11866 (c06)
- [V] Chen et al. (2026), MedEinst. https://arxiv.org/abs/2601.06636 (c07, c08)
- [V] Shi et al. (2023), GSM-IC. https://arxiv.org/abs/2302.00093 (c15, c27)
- [V] Shinn et al. (2023), Reflexion. https://arxiv.org/abs/2303.11366 (c16)
- [V] Building Effective AI Coding Agents for the Terminal (2026). https://arxiv.org/abs/2603.05344 (c19)
- [V] Ghosal et al. (2025), Does thinking more always help? https://arxiv.org/abs/2506.04210 (d01)
- [V] Muennighoff et al. (2025), s1. https://arxiv.org/abs/2501.19393 (d02)
- [V] Fu et al. (2025), DeepConf. https://arxiv.org/abs/2508.15260 (d03)
- [M] Petrova and Vejsiu (2026), Spectral origins of the self-correction blind spot. https://arxiv.org/abs/2607.09803 (d05)
- [V] Mehta (2026), Confident and wrong. https://arxiv.org/abs/2603.25764 (d06, d07)
- [V] Ouyang et al. (2026), ReasoningBank. https://arxiv.org/abs/2509.25140 (d09)
- [V] Ni et al. (2026), Trace2Skill. https://arxiv.org/abs/2603.25158 (d10)
- [V] Zhu et al. (2026), Execute-Distill-Verify. https://arxiv.org/abs/2606.24428 (d11)
- [V] Liu et al. (2025), Understanding R1-Zero-like training. https://arxiv.org/abs/2503.20783 (d12)
- [V] Ji et al. (2025), MathSticks. https://arxiv.org/abs/2510.00483 (d13)
- [V] Chen et al. (2025), Reasoning models don't always say what they think. https://arxiv.org/abs/2505.05410 (d14)
- [M] Luo and Knoblich (2007), as cited in Danek and Flanagin. https://aimspress.com/aimspress-data/aimsn/2019/2/PDF/neurosci-06-02-060.pdf (a06)
- [M] Kaplan and Simon (1990), via Knoblich 2001. https://link.springer.com/content/pdf/10.3758/BF03195762.pdf (a12)
- [M] Ohlsson (1992), via Knoblich 1999. https://www.kognition.uni-koeln.de/literature/Knoblich_etal_1999.pdf (a28)
- [M] Wiley and Danek (2023/2024). https://doi.org/10.1038/s44159-023-00257-x (a27, d15)
- [M] Pupil dilation and unconscious analytic thought in insight (2026). https://doi.org/10.3390/jintelligence14090211 (d16)
- [M] Cai et al. (2009), Metcalfe and Wiebe (1987), Dietrich and Kanso, Sprugnoli meta-analyses: relayed through Danek 2019 and Schonauer 2018, not opened.
