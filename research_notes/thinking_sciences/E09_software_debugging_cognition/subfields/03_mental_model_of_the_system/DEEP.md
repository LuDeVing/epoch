# Mental model of the system: deep document

*Subfield E09.03 of software debugging cognition. Focus: evidence gathering to build the model. Key work: Li and Coblenz 2026. Schema parts touched: S2 (running model), S6 (impasse), G2, G10. Evidence ids (a01-a27, b01-b24, c03-c26, d01-d23) refer to the evidence_*.jsonl files in this folder. Claim ids (K01-K21) refer to claims.jsonl. Written 2026-11-01 from files already collected; no new search.*

## 1. What it is

A "mental model of the system" is the picture a developer holds of the program while debugging. It says what the parts are, how they connect, what runs when, what data flows where, and what the developer does not yet know. Debugging is mostly the work of building and repairing that picture. The fix itself is usually small once the picture is right.

Three layers show up in the literature:

- **Static structure.** Objects, files, call and import relations, goals of components. (Littman 1986 "static knowledge"; Pennington's "program model" is control flow; Burkhardt's "static information".)
- **Dynamic behaviour.** What happens at run time: data flow, order of calls, state values. (Littman's "causal knowledge"; Burkhardt's "dynamic information".)
- **Situation / goal level.** What the program is for, and what the failure means in those terms. (Pennington's "situation model".)

The subfield question for our agent: how does a skilled debugger gather evidence to build and update this model, how much of the effort goes there, what works, and what is the machine equivalent? In our schema this is S2 REPRESENT used as a running note, with S5/S6 sending the agent back to it after a failed fix.

Scope notes. Hypothesis testing, fault localisation algorithms, and stopping rules have their own subfields in this series ("Fault localisation and repair", "Debugging as scientific method", "Gugerty and Olson findings", "Model-based diagnosis", "Progress monitoring"). This document covers them only where they bear on building the model.

## 2. History and theories in depth

Most of the theory below reaches us second-hand through the review by Wyrich et al. 2023 (a14-a18, opened). The original 1978-1995 papers were mostly not open. Where I give numbers from them I say so.

**Brooks (1978, 1983): top-down hypothesis refinement.** Understanding a program means refining hypotheses about what it does, from the top goal downward. Hypotheses are checked against "beacons" such as names and comments. Wiedenbeck (two experiments, cited in a14) found beacons help experienced developers, not novices. This is the earliest statement that the model is a set of guesses that are tested, not a copy of the code.

**Soloway and Ehrlich (1984): plans and discourse rules.** Experienced developers carry stock programming plans and expect code to follow rules of discourse. Adelson found experts recall larger semantic chunks (a14).

**Letovsky (1987): the opportunistic understander.** From think-aloud protocols of six professionals adding a feature. The understander has a knowledge base, an evolving mental model, and an assimilation process. It mixes top-down and bottom-up cues. It asks questions and makes conjectures with levels of certainty (a15). This is the closest ancestor of the "uncertainty list" in Li and Coblenz.

**Pennington (1987): program model versus situation model.** Borrowed from text comprehension. The program model (control flow, operations) comes first in procedural code. The situation model (data flow, goal hierarchy) comes later. Study 1 reportedly tested 80 professionals (web record, not opened). The original paper returned HTTP 403 (a16). All numbers here are second-hand.

**Littman et al. (1986): static versus causal knowledge.** A strong model needs both what components do and how they interact during execution. Developers who traced data flow between routines systematically did better than those who read "as needed". Sample sizes were not in the text read (a17).

**Von Mayrhauser and Vans (1995): integrated metamodel.** Joins Brooks, Pennington, Letovsky and Shneiderman. Developers switch between top-down, program and situation models around a shared knowledge base. It is descriptive, not predictive (a18).

**Gilmore: debugging contains comprehension.** Debugging is a loop with comprehension inside it. Bugs deeper in program structure were found more easily, which suggests detection happens during ongoing comprehension (a18). This matches the 2026 grounded theory.

**Burkhardt, Detienne, Wiedenbeck (1997): object-oriented code.** 30 OO experts and 21 novices read a library program. Boundary condition on Pennington: in OO code the situation model was better developed than the program model even early (a19, a20). The order of model building depends on the paradigm.

**Interrogative debugging (Ko and Myers 2004, 2008).** Programmers ask "why did" and "why did not" questions. In the authors' earlier Alice studies, 50 percent of errors came from false assumptions made while debugging, and 68 percent of questions were why-did-not (a11). The Whyline answers those questions from a recorded execution (a12, a13).

**Information foraging (Ko, Myers, Coblenz, Aung 2006).** Developers working in unfamiliar code forage for information of perceived relevance. Success depends on clear cues in the environment and on a way to keep what was found (a08-a10). Navigation cost is large. Misleading cues (a suggestive class name) send people to the wrong place.

**Field studies of professionals.** Roehm et al. 2012 (28 developers, 7 companies) found professionals avoid comprehension: they run the program, use the debugger to elicit runtime information, clone to avoid reading, and pick a start point from experience. Establishing and testing hypotheses was a minority strategy (9 of 28) (d11). Xia et al. 2018 logged 78 professionals over 3,148 hours and found comprehension about 58 percent of working time (d09). Layman et al. 2013 interviewed 15 Microsoft engineers: debugging is iterative hypothesis building, with instrumentation and logs the pain points (d10).

**Li and Coblenz 2026 (the key work).** A constructivist grounded theory from 12 people (7 professionals, 5 live-streamers) on 17 tasks, about 10.9 hours (a01, b01, c01). The loop has four steps: reproduce, build and update a mental model, work on a fix, validate. Mean time split: 12, 57, 13, 18 percent. 1.65 fix-validate cycles per task. After a failed first fix, people returned to model update in 9 of 17 tasks. Four sessions ended unfinished, all inside model update. The model has two parts: an **uncertainty** list (what I know I do not know) and **speculations** (loose guesses). Developers updated uncertainty with factual evidence first, then speculated on that base (a02). They almost never stated formal hypotheses (a03). They practised **knowledge avoidance**: a breadth-first, good-enough model, skipping tactics that need deep learning (a04, c03). Evidence came from two tracing modes (forward and backward) and from non-code sources: version history, colleagues, web, AI (a05, a06). Simple bugs were fixed by reading alone. Complex ones needed execution (a07).

**Machine-side lineage.** Self-debug and rubber-duck explanation (c25), Reflexion's memory of failures (c26), LDB's block-level runtime values (c24), SWE-agent's agent-computer interface (c12-c14), Agentless's fixed pipeline (b12, d21), graph-based repo models (LocAgent a21, OrcaLoca a23), hypothesis-and-investigation agents (CogniGent a24, AutoSD d16), debugger access (debug-gym b10, Debug2Fix d03), and trajectory studies (d01, d05, d06, d07, b15). None of these tests "model quality" as a manipulated variable. They test pieces.

## 3. Core findings with exact numbers

Status key: **E** established (two or more independent sources), **S** single source, **C** contested, **H** human-only, **M** older models only.

| Finding | Numbers | Source (evidence id) | Status |
|---|---|---|---|
| Professionals spend most debugging time updating the model | 12% reproduce / 57% model / 13% fix / 18% validate; 12 people, 17 tasks, 10.9 h; 1.65 fix-validate cycles | Li and Coblenz 2026 (a01, b01, c01) | S for the exact split, H; E for "comprehension is the biggest share" |
| Other field figures for comprehension share | Ko 2006 about 35% (10 analysed); Xia 2018 about 58% (78 pros, 3,148 h); Minelli up to 70% (cited) | d09, a09 | E, H; methods differ so not comparable |
| A failed first fix sends people back to model update | 9 of 17 tasks | Li and Coblenz (b01) | S, H |
| Unfinished sessions end in model update | 4 of 4 | a01 | S, H |
| Time does not track number of techniques | Spearman rho 0.10, p=0.68; avg 5.5 techniques per task; line-by-line reading in 16 of 17 tasks | b02, b03 | S, H, low power |
| Streamers make more transitions than other participants | median 9 vs 4, Mann-Whitney p=0.014 | b03 | S; group difference, not a technique effect |
| Developers do not state formal hypotheses unprompted | none articulated formal hypotheses; a cited performance-bug study counted hypothesis testing in 79 fifteen-second instances vs 832 inspecting source; Roehm 9 of 28 | a02, a03, d11 | E, H |
| Navigation is a large cost; most searches fail | Ko 2006: 35% of non-interrupted time (19 min) navigating; 88% (SD 11) of debugging searches led to nothing useful; about 25 min (36%) on irrelevant code; interruptions 22% excluded | a08, a09 | S, H, small Java program |
| Time split in maintenance tasks | about 20% reading, 20% editing, 25% search and dependency navigation, 10% testing, 5% tool switching, 6% API docs | a10 | S, H |
| Debugging share of a session is large and uneven | 13-95% of session time, mean 48% (sd 24); 80% of episode time from 25 episodes; 92% of searches were API explanation, 8% defect behaviour | b07 | S, H |
| Explicit hypotheses matter when prompted | Correct hypothesis at stage 2 gave 5x odds of fixing (p=0.01); correct hypotheses 11% (3/27), 25% (9/35), 39% (15/38) over stages 1-3; N=20 control | Alaboudi and LaToza 2020 (b05) | S, H |
| Supplied hypotheses help, supplied locations do not | Hypotheses: about 6x odds (p=0.039). Locations: no gain (p=0.67) | b06 | S, H |
| Asking "why did / why not" speeds diagnosis | Whyline: 7.8x faster in 6 scenarios (F(1,5)=12.64, p<.02); 3.20 vs 2.25 tasks in 90 min (+40%, t(7)=3.0, p<.02); N=9 | Ko and Myers 2004 (a12) | S, H, tiny |
| Java Whyline: novices with it beat experts without | median 4 min (n=9) vs 10 min (n=18), p<.05; initial guesses wrong almost 90% of the time (cited) | a13 | S, H |
| Dynamic knowledge is harder than static | Static 4.74 vs dynamic 3.62 (of 6), F(1,45)=106.2, p<.0001; experts lead only on static (5.00 vs 4.36) | Burkhardt 1997 (a19, a20) | S, H; questionnaire, not live debugging |
| Situation model beat program model in OO code | 4.36 vs 3.55, F(1,43)=110.94, p<.0001; N=51 | a19 | S, H; paradigm-bound |
| Models fail at runtime-behaviour prediction | REval 44.4% average, incremental consistency 10.3; CRUXEval GPT-4 63-67% (75-81% with CoT); CodeSense: Python no model above 50% | b19, b21, d12, d13 | E, M for the first three |
| Newer reasoning models simulate short snippets well | 85-98% on 427 snippets, 4 models; tool use fixed 58% of the computation-error category | Abdollahi 2025 (b20) | S, short snippets |
| Own-feedback repair is weak next to human diagnosis | GPT-4 own feedback 33.30% vs human 52.60%; intro 42.64/62.21, interview 19.33/45.67, competition 3.67/14.67; 16 humans, 40 programs | Olausson 2024 (b08, c22) | E (with Huang c23, Chen c25) |
| Repair barely beats resampling at equal compute | 10 samples + 1 repair each = 1.05x pass@20; 2 samples + 10 repairs = 0.97x pass@22 | c22 | S, M |
| Debugger access: strong models gain, weak do not | Claude 3.7 SWE-bench Lite 37.2 rewrite / 48.4 debug / 52.1 debug(5); Llama-3.3-70B 2.4/4.0/4.8; Aider GPT-4o 69.7/72.9, o3-mini 95.2/94.2 | debug-gym (b10, c06, c07) | E with d03, d16 |
| Forced debug call before editing | Debug2Fix GitBug-Java: GPT-5 60.2 to 73.1, Haiku 4.5 71.0 to 82.3, Sonnet 4.5 75.7 to 85.5; optional tools: GPT-5 60.8, Sonnet 64.5 (-14.8%); agent used a tool in 17 instances (9%) | Garg and Huang 2026 (d03) | S, vendor authors, 2 benchmarks |
| Real execution output matters; imagined output hurts | AutoSD: plausible patch 73% (real) vs 63% (no debugger); imagined debugger 11 pp less likely plausible; DONE-token runs 89% correct vs 82% | Kang et al. (d16) | S |
| Hypothesis loop for LLMs equals plain LLM on repair rate | AutoSD repair level with baseline; value is confidence and explanation; developers (N=20) judged patches better with explanations in 5 of 6 bugs | d16 | S |
| Hypothesis-and-investigation agent raises bug-report localisation | CogniGent: MAP +23.33 to +38.57%, MRR +25.14 to +53.74%; 591 reports, 15 systems; best document MAP 0.407; ablation: hypotheses carry up to 19% | Samir and Rahman 2026 (a24, a25) | S; open models, localisation only |
| Structural graph improves localisation | LocAgent Loc-Bench file Acc@5 83.39 vs Agentless 67.50, OpenHands 79.82, SWE-agent 77.68; SWE-bench Lite Acc@5 73.36 vs 58.39; Pass@1 27.92 vs 26.31; Pass@10 37.59 vs 33.58 | a21, a22 | E for localisation (with a23, c16); S for repair |
| Localisation gain gives small repair gain | +15 pp Acc@5 gave +1.6 pp Pass@1 | a22 | S |
| Interface design shifts results at fixed model | SWE-agent Lite, GPT-4 Turbo: summarised search 18.0 vs iterative 12.0 vs none 15.7; viewer 100 lines 18.0, 30 lines 14.3, full file 12.7; edit with lint 18.0, without 15.0, no edit command 10.3; last-5 observations 18.0 vs full 15.0 | c12-c14 | E (with Agentless skeleton c16); error bars +-3.0 to +-7.7 |
| Skeleton view beats full file for related-element search | 58.33% vs 53.67% (698 vs 778 lines) | c16 | S |
| Fixed pipeline matched agents | Agentless 32.00% (96/300), $0.70 | b12, c15, d21 | S, 2024, Lite |
| Generated reproduction tests are weak judges | 213 reproduced the issue; only 94 also passed on the true patch | d21 | S |
| Agents usually find the right file, even when failing | Right file in 72-81% of failed runs | Majgaonkar 2025 (b14, d07) | E with b18 |
| Many failures edit the right functions | 60-69% for GPT-5, GPT-5-mini, Qwen3 variants (range probable, see critique); agents inspect 8-12x more files and 17-25x more functions than needed; 16,758 trajectories | Kim 2026 (b18, d05) | S |
| Agents destroy correct patches | 5 cases of gold-identical patch lost; edit-commit checkpoint recovered 5/5; consensus +3.0 pp, p=0.08 | b18, d05 | S |
| Run length and failure | Failed runs longer: SWE-agent +12.6/+18.5%, OpenHands +31.0/+82.5%, Prometheus +56.6/+50.7%. But within 416 contested tasks resolved runs longer: 44.0 vs 39.6 steps, 263/416, p=1.9e-9 | Majgaonkar (d07) vs Mehtiyev (b15) | C |
| Gathering context before editing and validation separate success | Reported to hold after difficulty control; 12 never-solved tasks failed on architectural reasoning gaps | b16 | S |
| Model matters more than scaffold, and the gap shrinks | LLM switch moves resolution 51.5 pp (SWE-agent) and 31.5 pp (OpenHands); framework gap 19.4, 3.8, 0.9 pp over three model generations | b17 | S |
| Process anti-patterns | Repair raised resolution on problematic instances +23.5 pp (R1, n=17), +13.0 (V3, n=23), +6.9 (n=46); oscillation cut over 90%; steps cut 11.5-59.9% | Liu 2026 (d01, d02) | S, selected instances |
| Agents allocate fewer actions to exploration than humans spend time | Explore + search about 29% of actions pooled; generate fix 23%, run tests 19%, search 15%, explore 14%; 120 trajectories, 2,822 calls | Bouzenia and Pradel (d04) | S; actions, not time |
| Model families follow different phase schedules at similar pass@1 | 154k trajectories; GPT-5 collapses explore and localise into implement and verify | Gupta 2026 (d06) | S; LLM-judge labels |
| Long context hurts | Claude 3.5 Sonnet LongSWE-Bench 29% to 3% (32K to 256K); Claude 2 falls with context on SWE-bench | d14, c19 | E, M |
| Benchmarks overstate | SWE-bench+: 32.67% leakage, 31.08% weak tests, 12.47% to 3.97%; Live 19.25% vs Verified 43.20% same pair; Pro public best 43.6%, commercial 17.8%; PatchDiff 7.8% false passes (6.4 pp); issue-text-only file naming 76% vs 53% | b13, d17-d20 | E |
| First guesses are often wrong | Developers' initial guesses wrong almost 90% of the time (cited, Ko 2008); only 11% of stage-1 hypotheses correct | a13, b05 | E, H |

## 4. Mechanisms and models

Each mechanism ends with what is measured and what is a guess.

### 4.1 The four-step loop (Li and Coblenz)

```
REPRODUCE -> MODEL UPDATE <-> FIX -> VALIDATE
                  ^                       |
                  +---- on failed check --+
```

Implementation sketch. The program keeps a phase label. The agent works in MODEL UPDATE until a code-checked exit holds (see 4.6). FIX and VALIDATE are short. A failed VALIDATE returns to MODEL UPDATE with the failing output attached, not straight to FIX. Measured in humans: 57% of time in the model step and 9 of 17 tasks returning. Not measured: whether an agent does better with this shape at equal tokens.

### 4.2 The two-list model note (uncertainty and speculation)

Data structure for S2 as a running note:

- `known`: facts with a source (file:line, command output, log line). Only observed facts go here (G10).
- `unknown`: questions the agent cannot yet answer, each with the cheapest probe that would answer it.
- `guesses`: loose speculations about the cause. Each has a status: untested, supported, contradicted. A guess may point where to look. It is never evidence.

Update rules, from a02: add to `known` first; derive new `unknown` entries from `known`; only then add `guesses`. Code enforces that a guess cannot be promoted to `known` without a cited observation. Human basis: all developers tracked uncertainty on all tasks, and none wrote formal hypotheses (a02, a03). Contrast: prompting for explicit hypotheses raised human fix odds about 5-6x (b05, b06). The two fit together: let the note stay loose, but require a test for any guess that will drive a patch.

### 4.3 Evidence-gathering operators

From the human data the repertoire is: line-by-line reading (16 of 17 tasks), running with prints or breakpoints, forward tracing from a known state, backward tracing from the failure (including version history and bisect), asking an expert or the web or an AI, and temporary edits to probe (a05-a07, b02, d11).

Machine mapping:

| Human tactic | Agent operator | Measured on machines? |
|---|---|---|
| Reproduce | Run the failing test or script; keep the output | Yes: reproduction scripts in Agentless, but only 94 of 213 discriminate (d21) |
| Search for the symptom text | Summarised search listing files | Yes: 18.0 vs 12.0 (c13) |
| Read a bounded region | 100-line viewer | Yes: 18.0 vs 12.7 full file (c13) |
| Breakpoint and print | pdb tool | Yes, strong models only; must be forced (b10, d03) |
| Why-did-not question | Probe: run once, report whether and why a line did not execute | Not tested on LLMs |
| Backward trace through history | git log, blame, bisect tool | Not tested |
| Structure map | Call and import graph query | Yes for localisation (a21, a23) |
| Ask expert or web | Retrieval step, treated as untrusted | Not tested for debugging |

### 4.4 Probe before patch (the forced-probe rule)

Rule in code: no edit command is accepted until the run log has at least one executed probe whose output is stored in `known`. Debug2Fix reached a call rate near 99% this way and lifted GPT-5 from 60.2 to 73.1 on GitBug-Java (d03). The optional-tool arm fell below baseline because the agent called the tool in only 9% of cases. Open: whether the gain comes from the probe content or from the enforced delay (critique, gap 3). AutoSD's result that imagined output lowers the plausible-patch rate from 73% to 63% favours the probe reading (d16).

### 4.5 Structural map as an external model

Build once per repository, query on demand. Nodes are files, classes, functions. Edges are imports, invocations, inheritance (LocAgent a21). OrcaLoca adds priority scheduling of actions and distance-aware context pruning (a23). A cheaper variant is Agentless's skeleton: signatures and class outlines without bodies (c16). Rule: give the agent the map, not the files. Open bodies only for nodes the note marks relevant. Measured effect is on localisation (Acc@5 +16 pp on Loc-Bench, +15 on Lite) and a small effect on repair (+1.6 pp Pass@1).

### 4.6 Exit rule for the model step (a design gap)

No validated stop signal exists (critique gap 6). Candidate code-checked signals, none validated:

- the `unknown` list has no entry that blocks the planned patch;
- at least one executed probe discriminates between the top two guesses;
- the failing output is explained by a stated causal chain that names a line;
- a fixed budget share is spent (the Agentless answer: fix the schedule in advance, d21).

Step count alone is a bad stop rule. Failed runs are longer in some studies and shorter in others (C).

### 4.7 Revision after a failed fix

Human behaviour: return to model update, 9 of 17 tasks (b01). Agent failure modes: oscillation and RepeatedView loops (d01), thrashing that destroys a correct patch (d05), and a wrong first cause that persists while symptoms are patched (Majgaonkar case sympy-12236, d07). Mechanism: on a failed validate, code appends the new failing output to `known`, marks the guess that drove the patch as contradicted if the output differs from its prediction, and forces the next patch to name which `unknown` it addresses. Keep a checkpoint of the best verified state (d05: 5 of 5 recovered). Not tested as a bundle.

### 4.8 Static versus dynamic facts

Burkhardt's data say dynamic knowledge is the hard part for humans (3.62 vs 4.74) and does not separate experts from novices (a20). LLM data say the same from another side: models trace runtime behaviour poorly without running it (b19, d12, d13). Implementation: tag each `known` entry `static` (read from code) or `dynamic` (observed from a run). Report the dynamic share. A note whose entries are all static is a reading-only model and is suspect.

## 5. What holds up

**Replicated or corroborated (E).**

- Comprehension is a large share of professional effort. Three field methods agree on direction (Li and Coblenz 57%, Xia 58%, Ko 35%). The range across studies is 35-70%. The exact 57% is not a constant; methods differ (think-aloud, logs, rules).
- Own-feedback repair is weak and diagnosis is the bottleneck: Olausson (human 52.60 vs GPT-4 33.30), Huang (no gain without oracle), Chen (no-test MBPP +3.6% for GPT-4, others about 1%; most value needs test feedback).
- Executed evidence beats imagined evidence: Debug2Fix, AutoSD, debug-gym, LDB agree in direction.
- Compact, structured views beat raw reading: SWE-agent ablations, Agentless skeleton, LocAgent graph, long-context collapse.
- Localisation is no longer the main failure for capable models: Majgaonkar, Kim, Mehtiyev agree.
- Benchmark numbers are inflated by leakage and weak tests: six independent measurements.

**Failed or reversed.**

- The "failed runs are longer" claim reverses when task difficulty is controlled (Mehtiyev: resolved 44.0 vs failed 39.6 steps within contested tasks). Raw length comparisons mislead.
- Supplying fault locations to humans did not help (p=0.67), against the common assumption that finding the location is the bottleneck.
- Optional debugger tools lowered scores (Debug2Fix) and gave null or negative results on easy tasks (Aider: o3-mini 95.2 to 94.2).
- AutoSD's hypothesis loop did not beat a plain LLM on repair rate.
- The consensus variant against coherence collapse gave +3.0 pp, p=0.08, not significant.
- Execution-trace mid-training raised CRUXEval but not SWE-bench trajectory fit (CWM, a27).
- CodeMind: bug-repair success was not correlated with code-reasoning scores for most models (c20).

**Moderators and boundary conditions.**

- *Model strength.* Debugger tools help strong models only (debug-gym). Scaffold gain shrinks as models improve: framework gap 19.4, 3.8, 0.9 pp (b17). Effects found on 2024 models may shrink at the 2026 frontier. No frontier test of graph or debugger tools was found.
- *Familiarity.* Less familiar developers lean on backward tracing and version history. More familiar ones lean on forward tracing (a05, b02, c04). Based on about 5 people.
- *Bug complexity.* Simple bugs are fixed by reading. Complex ones need execution (a07).
- *Paradigm.* Which model is built first depends on object-oriented versus procedural code (a19).
- *Task type.* Human-feedback gains differ across intro, interview and competition problems (Olausson).
- *Codebase freshness.* Same pair 19.25% on SWE-bench-Live vs 43.20% on Verified.

**Interventions that worked.** Prompted hypotheses for humans (5-6x odds). Whyline-style why-not questions (7.8x faster, N=9). Forced probe before edit (+12.9 pp GPT-5). Debugger access for strong models (+11 to +15 pp Claude 3.7). Summarised search and bounded viewers. Lint on edit (+3.0). Graph map for localisation. Phase-aware stuck prompts on selected hard instances (+6.9 to +23.5 pp). Checkpoint of best state (5 of 5 recovered).

**Interventions that did not.** Supplying locations. Optional tools. Self-feedback without a check. Consensus on top of coherence collapse (not significant). Hypothesis loop for repair rate alone. Chain of thought, principle prompts and reflection against anchoring (Lou and Sun, d08: none removed the effect).

**Weak spots (from the critique).** Human samples are tiny (Li and Coblenz N=12 with 5 streamers; Ko N=10 analysed; Whyline N=9; Alaboudi N=20 control). Trajectory studies are correlational with heuristic phase labels. Liu's gains were measured on stubborn instances, so regression to the mean inflates them. Several debug-gym table columns were garbled in extraction; only the Claude and Llama rows were read cleanly. The Kim 60-69% range was not re-found in the abstract. Gugerty and Olson 1986, Parnin and Orso 2011, and Beller 2018 were not opened and carry no numbers here (b22-b24). Note on a05/b02: backward tracing was a dominant strategy at coarse levels (version history, files, calls) per the paper text; c04 is closer than a05/b02.

## 6. Language models

**How they behave on these tasks.**

- *Reading-only models are unreliable on run-time behaviour.* REval average 44.4% with incremental consistency 10.3 (b19, d12). CRUXEval GPT-4 63% output, 67% input; with CoT 81% and 75% (b21). CodeSense on real repository code: Python no model above 50%; 3-statement blocks about 20% for Claude 3.5; C under 10% (d13). Reasoning models of 2025 do much better on short snippets (85-98%, b20), and a calculator tool fixed 58% of computation errors. The gap is short synthetic snippets versus real code.
- *Localisation is mostly solved at file level.* Right file in 72-81% of failures (b14). Function-level edits are right in 60-69% of failures for capable models (d05). The weak point is keeping a coherent model across edits.
- *Over-exploration.* Agents inspect 8-12x more files and 17-25x more functions than needed (d05). Context overflow (35.6%) and endless file reading (17.0%) are leading failure modes of Sonnet 4 on SWE-Bench Pro (d17).
- *Phase mix.* Explore plus search is about 29% of actions pooled across three 2024 agents (d04), far below the 57% human time share, though actions are not time. OpenHands starts with about 50% explore and search in the first fifth of the run. Model families differ: GPT-5 collapses exploring into implementing; Qwen3-coder and Gemini spread effort (d06).
- *Weak models repeat themselves.* GPT-4o and Llama-3.3-70B rewrote the same parsing code again and again. Claude 3.7 and R1-distill read the error and found a line-number range bug (b11, c08). Claude 3.7 used pdb to test a Python 2 vs 3 rounding belief and corrected it (c09).
- *Reasoning models overthink in loops.* R1-distill models produced many more response tokens per episode (c10; no count extracted).
- *Self-correction.* Without an external signal it mostly does not help and may hurt (c23). With human diagnosis GPT-4 repair success was 52.60% vs 33.30% on its own.
- *Anchoring.* LLM answers move toward misleading hints. CoT, reflection and ignore-the-anchor prompts did not remove it. Collecting hints from several angles helped (d08, general question answering). In debugging, a wrong first cause persisted in one case study (d07). The rate is unmeasured.
- *Long context.* Claude 3.5 Sonnet LongSWE-Bench 29% to 3% from 32K to 256K (d14). SWE-bench: Claude 2 declines with context (c19). BM25 retrieval with Claude 2 gave 1.96% and retrieved none of the oracle files in almost half of instances (c18).

**What changed performance, by how much.**

| Change | Effect | Model, benchmark |
|---|---|---|
| Debugger from step 1 / after 5 rewrites | 37.2 to 48.4 / 52.1 | Claude 3.7, SWE-bench Lite (b10) |
| Same, weak model | 2.4 to 4.0 / 4.8 | Llama-3.3-70B (c06) |
| Forced debug call before edit | 60.2 to 73.1 | GPT-5, GitBug-Java (d03) |
| Debugger tools optional | 60.8 (flat); Sonnet 64.5 (-14.8%) | same (d03) |
| Real vs imagined debugger output | plausible 73% vs 63% | AutoSD (d16) |
| Block-level runtime values (LDB) | up to +9.8% | HumanEval, MBPP, TransCoder; early models (c24) |
| Summarised search vs iterative | 18.0 vs 12.0 | GPT-4 Turbo, Lite (c13) |
| 100-line viewer vs full file | 18.0 vs 12.7 | same |
| Lint on edit | 18.0 vs 15.0 | same (c14) |
| Last-5 observations vs full history | 18.0 vs 15.0 | same |
| Graph map | Acc@5 73.36 vs 58.39; Pass@1 27.92 vs 26.31 | Claude 3.5, Lite (a22) |
| Hypothesis + investigation agent | MAP +23 to +39% | open models, Bench4BL (a24) |
| Phase-aware stuck hint, rollback | +6.9 to +23.5 pp on problematic instances | DeepSeek, SWE-agent and OpenHands (d02) |
| Checkpoint of best state | 5 of 5 lost patches recovered | GPT-5 and others (d05) |
| Model switch | up to 51.5 pp | SWE-agent, 6 LLMs (b17) |

No study varies the presence or quality of a written running system model while holding tokens fixed. That is the central gap (K21).

## 7. What our agent should take

Status marks: [E] established, [S] single-source, [C] contested. Schema parts: G guardrail, S state, O operator, memory = notes and logs. Claim ids point to claims.jsonl. Every item still passes G7: keep only if it wins at equal tokens.

### Add now (established)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| A1 | After a failed check, return to S2 with the failing output appended. Do not go straight to a new patch. | S5/S6 to S2 | [E] for the human loop; G2 already holds the same rule | K01, a01, b01, c01 |
| A2 | Every claim entered in the model note cites an observation (file:line, command output). Guesses are labelled and never count as evidence. | G2, G10, S2 | [E] | K06, K13, b08, c22, c23, d16 |
| A3 | Where a runnable environment exists, make a probe (run, print, breakpoint) mandatory before the first edit. Do not make it optional. Strong models only; weak models gain nothing. | O (probe) | [E] | K05, b10, c06, d03, d16 |
| A4 | No self-feedback as diagnosis. A repair uses real failing output or a stronger external signal. | G2, S5 | [E] | K06, b08, b09, c22, c23, c25 |
| A5 | Verify run-time claims by running. Do not trust a predicted trace. | G10, S4 | [E] | K13, b19-b21, d12, d13 |
| A6 | Feed the model compact views: skeleton or graph map, bounded file windows (100 lines), summarised search results, last few observations rather than full history. | S2, memory | [E] | K11, K12, c13, c14, c16, a21, a22 |
| A7 | Keep context small by moving settled facts into the S2 note and dropping raw reads. | S2, memory | [E] | K17, K19, d14, c19, d17 |
| A8 | Make the note record the causal reason for the failure, not only its location. | S2 | [E] | K07, b14, b18, b16, d05, d07 |
| A9 | Never use "steps exceeded X" as a stall or stop rule. | G (stall rules) | [E] as a negative; the length effect itself is [C] | K08, b15, d07 |
| A10 | Evaluate any debugging test on post-cutoff or differential-tested tasks. | measurement | [E] | K16, K19, b13, d17-d20 |

### Test first (single-source, contested, or unverified for agents)

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Written three-list note (known / unknown / guesses) versus unstructured reading, at equal tokens | S2 | [S] human-derived; no LLM test | K21, a02, d22 |
| T2 | Ranked hypothesis list, each with one discriminating test, execution required | S2, O | [S]; humans benefit, LLM repair neutral | K04, K18, b05, b06, d16 |
| T3 | Forced probe versus delay-matched no-op | O, G | [S] | K05, d03, d16 |
| T4 | Why-did-not question before patching | O | [S] | K03, a12, a13 |
| T5 | Forward versus backward tracing chosen by a familiarity proxy | O | [S] | K15, a05, c04 |
| T6 | Static / dynamic tags and a minimum dynamic share | S2 | [S] | K14, a20 |
| T7 | Exit rule for the model step: fixed budget share versus signal-based | S2, S6 | [S] | K20, d21, K21 |
| T8 | Checkpoint of the best verified state with a stated reason to overwrite | G | [S] | K09, d05 |
| T9 | Loop and oscillation detector with a phase-aware hint | G | [S] selected instances | K10, d01, d02 |
| T10 | Structural graph map at the 2026 frontier | S2 | [S] older models | K11, a21-a23 |
| T11 | Guard against anchoring on a first cause (second independent diagnosis from a fresh context) | S3, G4 | [S] indirect | d07, d08, K21 |
| T12 | Agentless-style fixed schedule versus free exploration | S0/S2 | [S] | K20, b12, d21 |

## 8. Concrete tests on our bench

All tests need a code-debugging item pool. Our existing bench (ARC and BRAINTEASER) has no repository bugs, so this needs new items. Use three pools: (a) debug-gym Mini-nightmare style hand-built bugs (10 tasks as seed, extend to 40); (b) a post-cutoff subset of SWE-bench-Live or SWE-Bench Pro public (50-100 tasks, differential tests where possible, per d18, d19); (c) small synthetic bugs with hidden tests that we write and keep private. Both arms always get the same total token budget (input plus output, counted by the harness), same model, same temperature, 3 seeds. Report resolved rate with a paired test and a bootstrap interval. Always log tokens by phase.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 S2 note | Pools b and c | A: free reading and patching. B: same plus a code-enforced note with known / unknown / guesses, rewritten each cycle; note tokens count against the budget | Resolved rate; wasted file opens; repeated reads | +3 to +8 pp if context overflow is a main failure (d17); no gain would mean the note is a cost |
| T2 Hypothesis list | Pools a, b | A: free. B: ranked list, one test each, executed. C: list without execution | Resolved rate; correct-first-hypothesis rate; confidence calibration | B equal to A on resolved rate (AutoSD); B better on calibration; C worse than B by about 5-10 pp if d16 holds |
| T3 Forced probe | Pools a, c | A: probe optional. B: probe forced before edit. C: forced no-op wait of the same token cost | Resolved rate; probe-call rate | B > A by 5-12 pp on strong models; B approximately C means the gain is delay, not information |
| T4 Why-not question | Pool c | A: free. B: must write "why did X not happen" and answer with one run | Resolved rate; first-cause correctness | +2 to +6 pp, small and uncertain |
| T5 Tracing mode | Pool b split by repo size | A: forward only. B: backward only (version history first). C: mode chosen by a familiarity proxy | Resolved rate by band | C >= max(A, B); effect only in unfamiliar repos |
| T6 Static/dynamic | Pool c | A: free. B: at least 2 dynamic facts before edit | Resolved rate; dynamic-fact share | +2 to +5 pp |
| T7 Exit rule | Pools a, b | A: fixed 40% budget to model step. B: free. C: signal-based exit (4.6) | Resolved rate; tokens to first correct hypothesis | A approximately C > B at low budgets |
| T8 Checkpoint | Pool b | A: none. B: snapshot on test pass, reason required to overwrite | Lost-fix count; resolved rate | Recovers most lost patches; +1 to +3 pp |
| T9 Loop detector | Random (not selected) instances of pool b | A: none. B: RepeatedView / oscillation rule with hint | Resolved rate; steps | Much smaller than +6.9 to +23.5 pp (regression to the mean); +1 to +4 pp |
| T10 Graph map | Pool b | A: raw search and read. B: graph query tool | Localisation Acc@5; resolved rate | +10 pp localisation; +1 to +3 pp repair |
| T11 Anchoring | Pool c with a planted misleading symptom | A: one chain. B: second diagnosis in a fresh context that does not see the first | Resolved rate on planted-trap items | B +5 pp if anchoring is real |
| T12 Schedule | Pools a, b | A: Agentless-style fixed localize / repair / select. B: free loop | Resolved rate; cost | A approximately B at lower variance |

Also log, for every run, the token share on read / trace / note vs patch. This allows comparison with the 57 / 13 human split, with the caution that action counts and token shares are not time shares.

## 9. What does not transfer, and why

- **The 57% figure.** It is a mean time share of 12 people on web-app-heavy tasks, coded from think-aloud. An agent's tokens are not minutes. Reading is cheap for a model; thinking is the cost. Do not use 57% as a target. Use it only as a hint that early evidence gathering is where effort belongs.
- **Knowledge avoidance.** Humans skip deep learning because it is slow and memory is short. A model can read a graph map in one pass. Avoidance may still be right for context-cost reasons (long-context collapse), but the human motive differs.
- **No formal hypotheses.** Professionals succeed without them (Li and Coblenz), yet prompted humans do better (Alaboudi). For an LLM, written reasoning is not evidence of its decision process (G10). Our agent has no implicit store, so externalising is cheap.
- **Asking colleagues.** Not available to a single agent. The nearest equivalent is retrieval, untested for debugging.
- **Streamers.** Narration for an audience changes behaviour (more transitions, median 9 vs 4). Do not model that.
- **Whyline.** Needs a recorded execution and a UI of question menus. Only the idea (ask why-not, answer from a run) transfers. Evidence is N=9.
- **Foraging cost shape.** Humans pay for each file switch. Agents pay in tokens. Over-exploration (8-12x more files than needed) is the machine version, with different remedies.
- **Familiarity self-report.** An agent has no "I know this code" feeling. Any familiarity-based rule needs a proxy such as repo size or training-set overlap. Both are untested and may be confounded with memorisation (d20).
- **Debugger tools as used by humans.** Beller 2018 reports many developers avoid the IDE debugger and use prints (not opened). For an LLM the debugger helps only strong models and only when forced.
- **Benchmark transfer.** Our measurements must not inherit leaked SWE-bench numbers. Effects measured on contaminated sets (d18-d20) may be partly recall.

## 10. Open questions

1. Does a written running system model raise fix rate at equal tokens over unstructured reading, on a clean post-cutoff set? No LLM test found (K21, d22).
2. What share of tokens does the model-update phase take in agent traces, and is a human-like share a good target? Only action counts exist (d04).
3. Is the forced-probe gain due to the probe content or the enforced delay? (d03 vs d16)
4. Which part of a model matters: static, dynamic or causal? No agent study separates them (d23).
5. Do hypothesis lists help LLM agents as they help humans (5-6x odds), and do they anchor the agent on the first guess?
6. What signal tells the agent the model is good enough to patch? Generated reproduction tests are weak (94 of 213).
7. Do graph maps and debugger tools still help the 2026 frontier? Framework gaps shrank to 0.9 pp in one study.
8. How should a model be revised after a failed fix, beyond counting oscillation?
9. Does a compact S2 note beat full context at 100K+ tokens on real repositories, with retrieval controlled?
10. How much of reported agent success survives contamination-filtered tasks, for each effect above?
11. Is the human 57% stable? Li and Coblenz is one group and one sample, including five streamers. No replication yet.
12. Gugerty and Olson 1986 (skilled vs novice debuggers), Parnin and Orso 2011 (automated debugging aids), and Beller 2018 (print vs debugger) were not opened. Their numbers could change the human baseline.

## 11. Sources

[V] opened and read this session. [M] snippet or metadata only, or cited second-hand.

**Human studies and theory**
- [V] Li and Coblenz 2026, A Grounded Theory of Debugging in Professional Software Engineering Practice. https://arxiv.org/abs/2602.11435
- [V] Ko, Myers, Coblenz, Aung 2006, How Developers Seek, Relate, and Collect Information. https://faculty.washington.edu/ajko/papers/Ko2006SeekRelateCollect.pdf
- [V] Ko and Myers 2004, Designing the Whyline. https://faculty.washington.edu/ajko/papers/Ko2004Whyline.pdf
- [V] Ko and Myers 2008, Debugging Reinvented. https://faculty.washington.edu/ajko/papers/Ko2008JavaWhyline.pdf
- [V] Wyrich et al. 2023, Source Code Comprehension: A Contemporary Definition and Conceptual Model (review of Brooks, Soloway, Letovsky, Pennington, Littman, von Mayrhauser, Gilmore). https://arxiv.org/abs/2310.11301
- [M] Brooks 1978, 1983; Soloway and Ehrlich 1984; Letovsky 1987; Pennington 1987 (Cognitive Psychology 19(3):295-341, HTTP 403); Littman et al. 1986; von Mayrhauser and Vans 1995; Gilmore; Adelson; Wiedenbeck; Minelli. Known only through a14-a18 and d09.
- [V] Burkhardt, Detienne, Wiedenbeck 1997, Mental Representations Constructed by Experts and Novices in Object-Oriented Program Comprehension. https://arxiv.org/abs/cs/0612018
- [V] Alaboudi and LaToza 2020, Using Hypotheses as a Debugging Aid. https://arxiv.org/abs/2005.13652
- [V] Alaboudi and LaToza 2021, An Exploratory Study of Debugging Episodes. https://arxiv.org/abs/2105.02162
- [V] Xia et al. 2018, Measuring Program Comprehension. https://xin-xia.github.io/publication/TSE17.pdf
- [V] Layman et al. 2013, Debugging Revisited. https://www.swag.uwaterloo.ca/www/assets/other/papers/layman-esem-2013.pdf
- [V] Roehm et al. 2012, How Do Professional Developers Comprehend Software? https://memphis-cs.github.io/comp-7085-8085-2012-fall/papers/Roehm2012ICSE.pdf
- [M] Gugerty and Olson 1986, Debugging by skilled and novice programmers. https://dl.acm.org/doi/10.1145/22339.22367
- [M] Parnin and Orso 2011, Are automated debugging techniques actually helping programmers? https://doi.org/10.1145/2001420.2001445
- [M] Beller et al. 2018, On the dichotomy of debugging behavior among programmers. http://resolver.tudelft.nl/uuid:82fbe2e2-0dd6-4c17-9c13-49b320eb480c

**LLM and agent studies**
- [V] Chen et al. 2025, LocAgent. https://arxiv.org/abs/2503.09089
- [V] Yu et al. 2025, OrcaLoca (abstract and introduction only). https://arxiv.org/abs/2502.00350
- [V] Samir and Rahman 2026, Improved Bug Localization with AI Agents (CogniGent). https://arxiv.org/abs/2601.12522
- [V] Meta FAIR CodeGen Team 2025, CWM. https://arxiv.org/abs/2510.02387
- [V] Olausson et al. 2024, Is Self-Repair a Silver Bullet? https://arxiv.org/abs/2306.09896
- [V] Yuan et al. 2025, debug-gym. https://arxiv.org/abs/2503.21557
- [V] Xia et al. 2024, Agentless. https://arxiv.org/abs/2407.01489
- [V] Aleithan et al. 2024, SWE-Bench+. https://arxiv.org/abs/2410.06992
- [V] Majgaonkar et al. 2025, Understanding Code Agent Behaviour. https://arxiv.org/abs/2511.00197
- [V] Mehtiyev and Assuncao 2026, Beyond Resolution Rates. https://arxiv.org/abs/2604.02547
- [V] Kim et al. 2026, Coherence Collapse. https://arxiv.org/abs/2603.24631
- [V] Chen et al. 2024, Reasoning Runtime Behavior of a Program with LLM (REval). https://arxiv.org/abs/2403.16437
- [V] Abdollahi et al. 2025, Demystifying Errors in LLM Reasoning Traces. https://arxiv.org/abs/2512.00215
- [V] Gu et al. 2024, CRUXEval. https://arxiv.org/abs/2401.03065
- [V] Yang et al. 2024, SWE-agent. https://arxiv.org/abs/2405.15793
- [V] Zhang et al. 2024, AutoCodeRover. https://arxiv.org/abs/2404.05427
- [V] Jimenez et al. 2024, SWE-bench. https://arxiv.org/abs/2310.06770
- [V] Liu et al. 2024, CodeMind. https://arxiv.org/abs/2402.09664
- [V] Huang et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798
- [V] Zhong et al. 2024, LDB: Debug like a Human. https://arxiv.org/abs/2402.16906
- [V] Chen et al. 2024, Teaching Large Language Models to Self-Debug. https://arxiv.org/abs/2304.05128
- [V] Shinn et al. 2023, Reflexion. https://arxiv.org/abs/2303.11366
- [V] Liu et al. 2026, Process-Centric Analysis of Agentic Software Systems. https://arxiv.org/abs/2512.02393
- [V] Garg and Huang 2026, Debug2Fix. https://arxiv.org/abs/2602.18571
- [V] Bouzenia and Pradel 2025, Understanding Software Engineering Agents. https://arxiv.org/abs/2506.18824
- [V] Gupta et al. 2026, Dissecting model behavior through agent trajectories. https://arxiv.org/abs/2606.17454
- [V] Lou and Sun 2024, Anchoring Bias in Large Language Models. https://arxiv.org/abs/2412.06593
- [V] Roy et al. 2026, CodeSense. https://arxiv.org/abs/2506.00750
- [V] Rando et al. 2025, LongCodeBench. https://arxiv.org/abs/2505.07897
- [V] Kang, Chen, Yoo, Lou, Explainable Automated Debugging via LLM-driven Scientific Debugging (AutoSD). https://arxiv.org/abs/2304.02195
- [V] Scale AI (Deng et al.) 2025, SWE-Bench Pro. https://arxiv.org/abs/2509.16941
- [V] Zhang et al. 2025, SWE-bench Goes Live. https://arxiv.org/abs/2505.23419
- [V] Wang, Pradel, Liu 2026, Are Solved Issues in SWE-bench Really Solved Correctly? https://arxiv.org/abs/2503.15223
- [V] Liang, Garg, Moghaddam 2025, The SWE-Bench Illusion. https://arxiv.org/abs/2506.12286

**Negative searches (no source):** d15, d22, d23 record that no direct controlled test of a written running system model, of forced backward tracing, or of a stop signal was found. The search quota was exhausted and the three academic APIs returned 429, so absence is weak evidence.
