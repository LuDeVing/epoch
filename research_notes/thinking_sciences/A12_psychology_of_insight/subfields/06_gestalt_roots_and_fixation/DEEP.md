# Gestalt roots and fixation: deep document

*Subfield A12.06 of the psychology of insight. Written from evidence_a-d.jsonl, claims.jsonl (K01-K33) and critique.md in this folder. Evidence ids (a01, b10, c01, d05 ...) point to the jsonl lines. Status marks: [E] established, [S] single-source, [C] contested.*

**Reading warning.** The classic human half of this subfield (Duncker, Luchins, Maier, Glucksberg, Adamson, Frank and Ramscar, Kohler) was read through Wikipedia and review texts, not the primary papers. No primary N is known for any of them. The modern human studies (chess, anagrams, chunk decomposition, chimpanzees, eye tracking) and the LLM studies were read in full text. Treat the classic numbers as "direction and rough size", not as exact.

---

## 1. What it is

Fixation is the failure to see a problem in a new way because past experience pulls the solver to an old way. The old way is usually good. It is wrong only for this problem.

Four forms matter here.

1. **Functional fixedness.** An object seen in its usual role is hard to see in an unusual role. Duncker's candle problem: fix a candle to a wall using a candle, matches, and a box of tacks. The box has to become a shelf. People who see the box as a tack container fail.
2. **Einstellung (mechanised set).** A method that worked on earlier problems keeps being used, even when a simpler method exists. Luchins' water-jar problems are the model case.
3. **Red-herring fixation.** A plausible but wrong grouping or answer, strongly cued, blocks the right one (chess "familiar move", Only Connect decoys).
4. **Representational lock-in.** The solver holds an implicit and wrong constraint (nine-dot: "stay inside the square"). The problem is not hard in itself. The frame is wrong.

Why it matters for our agent. A language model has very strong priors from training. A prompt can cue one of those priors. The model then commits early, and later text builds on the commitment. The schema parts that touch this are:

- **S1 UNDERSTAND**: restate the task and name what is being assumed. Fixation is "the failure to name": the blocking assumption was never said out loud.
- **O6 Change representation** (and O8 Reframe the goal): the operators used at an impasse to get out of a fixed frame.
- **G1** (doubt only on a signal), **G4** (samples from one model are not independent), **G9** (no debate), **4b** (no unstructured self-reflection): constraints on how any anti-fixation step may be built.

Main finding of this document in one line: fixation is real and large in humans, it appears in LLMs on decoy-rich tasks, but **no study has tested a naming scaffold against an equal-token plain baseline on classic fixation items** (K33). Everything we would add is therefore a hypothesis to test, except a few design constraints.

---

## 2. History and theories in depth

### 2.1 Gestalt origins
- **Kohler (1917), The Mentality of Apes.** Work done on Tenerife; most observations in the first six months of 1914, six years at the station (a10). Apes stacked boxes and joined sticks to reach fruit. Kohler called the sudden restructuring "insight" (Einsicht). The Wikipedia page gives no counts of apes, trials or latencies. Birch (1945) later showed that prior experience with sticks mattered for ape tool use, which weakens the "pure sudden insight" reading (b34, not opened).
- **Wertheimer (1945), Productive Thinking.** Contrast of *productive* thinking (seeing the structure) and *reproductive* thinking (applying a learned procedure) (a12). The Gestalt terms (Pragnanz, restructuring) were criticised as vague, with little quantitative work.
- **Maier (1930/31)** two-string problem and pendulum. **Duncker (1935 German; 1945 English)**, "On problem solving": the candle problem and the radiation problem. Duncker died at 37 (a13). The Wikipedia page gives no results for the radiation problem.
- **Luchins (1942)**, "Mechanization in problem solving": the water-jar task, which gave the name Einstellung (a08, b13, d01).

### 2.2 The core Gestalt claim
Problem solving is a restructuring of how the elements are seen. A solver is blocked when the elements are locked into the wrong structure. Insight is the structure changing. The key idea for us: **the block is in the representation, not in a lack of knowledge or effort.**

### 2.3 What was built on it
- **Functional fixedness** studies: pre-use of an object (Adamson 1952; Birch and Rabinowitz 1951; Glucksberg 1962), wording (Higgins and Chaires; Frank and Ramscar 2003), training against it (McCaffrey 2012 "generic parts").
- **Einstellung** studies: Luchins and Luchins (1959), age and stress variants, stuttering (a09), chess (Bilalic et al. 2008; Sheridan and Reingold 2013), anagrams (Ellis and Reingold 2014), chunk decomposition (Huang et al. 2018).
- **Nine-dot problem** (printed 1907; the n x n generalisation needs 2n-2 segments, Klamkin 1955, Selfridge 1956: a14, d16). Later work (Weisberg and Alba 1981; MacGregor, Ormerod and Chronicle 2001) moved the explanation from "lock-in" to lookahead and progress monitoring (d14).
- **Incubation**: stepping away from a stuck problem (Segal 2004; Sio and Ormerod 2009; Strick 2011).

### 2.4 Competing explanations of fixation
| Account | Claim | What supports it | What against |
|---|---|---|---|
| Gestalt restructuring | The structure is wrong; insight rebuilds it | Candle, nine-dot, pre-use effects | Vague; weak on mechanism (a12) |
| Memory / retrieval (Smith, Beda) | A strong wrong associate blocks the right one; strength sets the size of fixation | Human dose result (N=30, d12); Beda and Smith 2018 as cited (a25) | Primary not opened; only one small dose study |
| Habit / learned set | Repeated success makes the old method default | Luchins, chess, chunk decomposition (b13, b15-b18) | Habit tendency did not predict candle success (N=69, p=0.169, d11) |
| Search / progress monitoring | Solvers do hill-climbing and drop a path when progress stalls; difficulty = lookahead limits | Nine-dot variants 80-93% vs 0% (d14, secondary) | Primary not opened |
| Failure to try, not to see | People see the alternative and still do not use it | 29.4% (10 of 34) did not use a shortcut after a video of it (d10) | One lab, students, 91% female |
| Attentional (eye movements) | Fixation steers where the eyes go, so evidence is not sampled | Chess experts first fixated target region at 407 ms vs 719 ms for novices; optimal-move experts had more dwells (b16) | Process, not cause |

### 2.5 Reading of the history for an agent
Two lessons recur. First, **the same task changes difficulty with how it is presented** (underlining nouns, tacks beside the box). Fixation is partly a property of the prompt, which an agent can edit. Second, **showing the alternative is not enough** (d10, d13). The solver must act on it.

---

## 3. Core findings with exact numbers

Status: [E] established, [S] single-source, [C] contested. "Secondary" means seen only in Wikipedia or a review.

### 3.1 Human classics (secondary sources)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Empty box makes candle task easier than filled box | about 2:1 solvers, empty vs filled; no N | Adamson 1952 via Wikipedia (a03, b03) | [E] direction, secondary |
| Same direction, plus incentive effect | Prize $5 (top 25%) or $20 (best). Filled-box: high drive did worse than low. Empty box: more solvers, faster. No N, no means | Glucksberg 1962 via Wikipedia (a01, b01, b02, d02) | [S] |
| Wording changes written candle solving | Plain 23%; noun phrases underlined 55%; only "box" underlined 47%. (The Candle page says 25% to 50%.) Prefer 23/55 | Frank and Ramscar 2003 via Wikipedia (a02, a04, b04, d02, d03) | [E] direction; numbers disputed |
| "box and tacks" beats "box of tacks"; tacks beside box gives near-universal solving | no numbers | Higgins and Chaires, via Wikipedia (a02) | [S] |
| Direction of pre-use matters | After relay pretest people used the switch almost exclusively as pendulum weight; most after switch pretest used the relay; controls used both about equally | Maier 1930/31; Birch and Rabinowitz 1951 (a05) | [S] |
| Generic-parts training helps | 67% more fixedness-affected problems solved than controls (relative); Psych Science 23(3) | McCaffrey 2012 (a07, b05) | [S] |
| Water-jar rigidity | Test-problem rigidity 70% (no stress) vs 98% (stress); extinction problem failed by 58% vs 97%. 483 children aged 9-12 in the gender analysis; speed test N=98, 3 of 98 solved the extinction problem | Luchins 1942 via Wikipedia (a08, b13, d01) | [E] direction; counts unverified |
| Einstellung by age | Failure 29% middle-aged vs 65% older adults (Ross 1952). Extinction task 56% young adults, 68% children, 69% older adults. IQ link not significant | Luchins and Luchins 1959 via Wikipedia (b14) | [S] |
| Einstellung in stutterers | 58% of stutterers vs 4% of fluent speakers used the Einstellung solution on first two critical problems | Wikipedia (a09) | [S] |
| Nine-dot: simplified variants vs full | 80-93% solved on simplified variants with stronger hints; 0 solved on the nine-dot (Exp 1) | MacGregor, Ormerod, Chronicle 2001 via a 2019 report (d14) | [S] |
| Shuar adults show fixedness | Box task: slower selection, same total time. Spoon task: slower in both. Called preliminary | German and Barrett 2005 via Wikipedia (a06, b08) | [C] |

### 3.2 Modern human studies read in full text

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Chess Einstellung is not just for novices | 34 players (17 experts, mean rating 2223; 17 novices). Problem 1: 8 of 17 experts and 8 of 17 novices chose the familiar move; 9 experts found the optimal move | Sheridan and Reingold 2013 (b15) | [E] |
| Experts who escape look at more | Optimal-move experts (n=9) more dwells than familiar-move experts, F(1,15)=12.34, p<.01, and than novices, F(1,15)=13.46. First fixation on target region: experts 407 ms vs novices 719 ms | b16 | [S] |
| Anagram Einstellung costs time, not accuracy | 60 students, 72 trials. Accuracy 51.7% vs 53.8% (n.s.). Correct RT 15.3 s vs 13.4 s, t(59)=3.25, p<.01 | Ellis and Reingold 2014 (b17) | [E] |
| Chunk decomposition set | Exp 1 (N=32): accuracy interaction F(1,31)=11.00, p=.002, eta2=.26. Exp 2 (N=28): RT only, F(1,27)=29.50, eta2=.52, accuracy unaffected | Huang, Tang, Hu 2018 (b18) | [E] |
| Chimpanzees | 16 apes: time to success chi2(1)=7.33, p=.007; task success 5/8 vs 8/8, Fisher p=.200. Study 2 (14 apes): finding the strategy chi2=5.23, p=.022; tool selection 2/7 vs 3/7, p=.576 | PMC11130300 (b10, b11) | [C] |
| Seeing the shortcut is not enough | N=67. 89.6% did not adopt the shortcut in block 1. After video: informed group used it in 65.25% of correct trials (SD 42.88) vs control 9.12% (SD 25.13). 24 of 34 (70.6%) adopted it; 10 of 34 (29.4%) did not | Sci Rep 2022, PMC8828898 (d10) | [S] |
| Habit tendency does not predict candle success | N=69 (16 of 85 excluded for knowing the task); binomial F(1,66)=1.895, p=.169. Past use of an object raised fluency and lowered flexibility of alternative uses | Front Psychol 2021 (d11) | [S] |
| Accessibility x induction | N=30, 2x2 within-subject, interaction significant: strong induction hurt mainly when the answer was weakly associated | 2026, PMC13117359 (d12) | [S] |
| Format change without representation change does not help | Exp 1: 87 analysed, paper vs physical format, no difference. Exp 2: matchstick picture raised solutions | 2026, PMC13208192 (d13) | [S] |
| Insight vs non-insight is in the solver | Aha-accuracy r for insight tasks 0.50/0.40/0.495; non-insight 0.02/0.24/0.19. N=193, 82, 129. Accuracy: insight 0.51/0.49/0.45 vs non-insight 0.54/0.64/0.56 | Webb et al. 2016 (b22) | [S] |
| Incubation small positive | Sio and Ormerod 2009: 117 studies, mean d=0.29. Strick 2011: 92 studies, g=0.224. 4 min break as good as 12 min | b19 | [E] |
| Interactivity during a break | Exp 1 N=63: time-1 solving 43% (12/28) vs 6% (2/35), chi2=12.42. Exp 2 N=61: low-to-high switch 61% (14/23) of earlier non-solvers vs high-to-low 5% (1/20) | PMC6994426 (b21) | [S] |
| GenAI output raises fixation in designers | N=60: fluency about -0.21; originality negative with about 97% probability. 10-designer ChatGPT case: novel-term share 67.4% vs 78.2% | c21, c22 | [E] small effects |

### 3.3 LLM studies

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Red herrings block LLMs on Only Connect | 494 test walls / 1976 groups. Humans 285 walls (57.7%), 1405 groups (71.1%). GPT-4 0-shot 6 walls, 239 groups (12.1%). GPT-3.5 0 walls, 114 groups | Naeini et al. 2023 (c01, a16) | [S] |
| Removing decoys | GPT-4 0-shot walls: 6 (original) -> 59 (Randomized, 595 groups) -> 471 (WordNet, 1926/1976 groups = 97.5%). GPT-3.5: 0 -> 5 -> 337 | c02, a17 | [S] (WordNet confounded with easier categories) |
| Few-shot does not help | GPT-4 walls at 0/1/3/5/10 shot: 6, 4, 5, 7, 3. Groups: 239, 262, 272, 269, 249 | c03, a17 | [S] |
| Naming the connection is far worse than grouping | Human about 80% correct; GPT-4 10-shot F1 41-45%, exact match under 15%; 8.2% of connections wrongly include the clues | a18, c03 | [S] |
| MacGyver: unconventional tool use | 1,683 problems; 1,306 solvable (77.6%), 377 unsolvable (22.4%); of solvable, 1,073 (82.2%) need unconventional tool use. Seven LLMs 35-42% single-attempt vs humans 65.1%. Majority of humans 79.3% vs GPT-4 73.3%. Scale alone no clear gain (Llama2 7B/13B/70B) | Tian et al. 2023/2025 (a19, a20, c05; corrected in critique) | [S] |
| MacGyver GPT-4 error shares | wrong tool usage 42.4%; not achieving goal 17.7%; unavailable tools 16.9% + unfaithful to constraints 9.5% = 26.4% | a21, d09 | [S] (table rows garbled in PDF; paper text used) |
| Prompting on MacGyver | 180 problems, GPT-4: self-reflect -9.7 points infeasible, divergent-convergent -4.3; div-conv +6.5 efficient, self-reflect +2.2. Self-reflect did not help Claude2 or Llama2-13b | a22, b25 | [S] |
| Clinical Einstellung, 2025 | M-ARC 100 items: best Gemini-1.5-Pro 50%, o1 48%, DeepSeek-R1 52%; physicians 66% (5 physicians, SE 5.3) | Kim et al. 2025 (c10, d04) | [C] |
| Clinical Einstellung, 2026 follow-up | Claude 4.1 Opus 0.751 (CI 0.738-0.763, 15 runs) vs physicians 0.66 (CI 0.55-0.75); three other models not different from humans at highest reasoning effort. Human-miss set (20 of 100): physicians 36% vs 73% for top models | Shidara et al. 2026 (b28, c11) | [C] |
| MedEinst | 5,383 paired cases, 49 diseases, 17 LLMs. Trap rate: Gemini-2.5-Pro 60.90%, Claude-Sonnet-4.5 42.98%, GPT-5 51.87% (table). No size-robustness link. GPT-5 failures: blindness over 35%; of the noticed cases 43% underthinking, 22% overthinking | Chen et al. 2026 (c07, c08, d07) | [C] (paper contradicts itself on accuracy; use trap rates) |
| MedEinst structured scaffold | ECR-Agent on Qwen3-32B: base accuracy 40.25 -> 69.49; robust 24.21; trap rate 33.75 (from 43.46) | c09, d07 | [S] authors' own method |
| Creative vs factual | CresOWLve, 2,061 examples: accuracy drop of 6.08% (Gemini-3.1-Pro high) to 17.21% (Mistral-Large-3-675B). More reasoning effort raised scores monotonically | Ismayilzada et al. 2026 (c14) | [S] |
| Vision-language | CREATE: 155 problems, humans (N=25, 80 items) 16.5% first attempt. One model 32.5%, next best 12.5%. Text cues raised every model by 30.0-66.3 points. Wrong model answers literal in 22.8% vs 8.9% humans | Yang et al. 2026 (c15) | [S] |
| Rebus and character puzzles | Humans below GPT-4-turbo by 0.32 and GPT-4o by 0.39 on rebus (p<.001); above GPT-4 on Chinese character puzzles | Zhang et al. 2025 (c16, c17) | [S] |
| Spontaneous reframing | Shifts in 6.31% of 1M+ traces; no rise during GRPO. Entropy-gated external reconsideration +8.41 pp on MATH-500 (0.3221 -> 0.4062). DeepSeek-R1 and GPT-4o shifts only 1-7%, no accuracy benefit | d'Aliberti and Horta Ribeiro 2026 (c18, c19, d08) | [S] |
| Chain of thought removes perseveration | WCST categories 0.3-0.5 standard vs 4.6-5.0 with CoT (human 4.73, SD 0.45); perseverative errors not uniformly reduced | Hao et al. 2025 (c26) | [S] |
| Forced-opposition debate | Counter-intuitive arithmetic (200 items) GPT-3.5: base 26.0, CoT 28.0, SC 29.5, Self-Reflect 27.5, MAD 37.0; GPT-4 51.0. Tokens vs CoT: self-reflect 1.83x, MAD 2.46x | Liang et al. 2023/2024 (c20, d05, d06) | [C] (not token-matched) |
| Multi-turn early commitment | 39% average drop single to multi-turn, 200,000+ simulations; restating context recovers only 15-20% | Laban et al. 2025 (c28) | [S] |
| Lateral-thinking puzzles | BRAINTEASER: ChatGPT about 53% and 63% vs human 92%; sentence puzzles 60.77 original, 59.33 semantic rewrite, 67.94 context rewrite | Jiang et al. 2023 (c12) | [S] |
| Metacognitive co-regulation loop | 141.17 vs 106.08 Ah, d=1.846, 30 runs each; numbers for the self-regulation arm inconsistent | Xu et al. 2026 (c23) | [S] lead only |

---

## 4. Mechanisms and models

Each model below is written so an engineer can turn it into a test or a program step. None is yet shown to work in an agent.

### 4.1 Fixation as a dominant association (memory-strength model)
- State: each object or concept has a set of associates with weights. A cue (the prompt wording, a recent use) raises the weight of one associate.
- Rule: the chance of finding an alternative role falls as the cued associate's weight rises. The cost is larger when the right answer has a weak association (d12).
- Implementation view for an LLM: the "weight" is how strongly the prompt primes a pattern. A dose test varies priming strength (zero, one cue, three cues, a worked example) and measures the failure rate. Predicted: monotone rise.
- The prediction can fail: fixation may not grow with priming strength in the LLM.

### 4.2 Einstellung as a learned default with a switch cost
- State: a library of methods ranked by past success. A new problem is solved by the top method that applies.
- Rule: if the top method succeeds, it stays at the top. A shorter method is found only when the top method fails or when search is forced.
- Observable: the *speed* cost (tokens-to-solution; anagram RT 15.3 vs 13.4 s) is larger and more reliable than the *accuracy* cost (K08). An agent test must log tokens, not only accuracy.
- Implementation: build a sequence of N problems solvable by method A, then critical problems solvable by A or by a shorter B. Measure the share of critical problems where the agent uses A, and the token count.

### 4.3 Attention steering (what the solver looks at)
- Chess eye tracking: the familiar move captures first fixations. Experts who found the better move scanned more (b16).
- Agent analogue: when a trap is avoided, the trace contains more distinct candidate answers. A cheap proxy is the number of distinct candidates the trace raises. S4 "harvest" already collects dropped candidates, which fits.

### 4.4 Representation lock-in (restructuring)
- State: a problem model = objects, allowed roles for each object, constraints (stated and implicit).
- Fixation = an implicit constraint treated as stated ("lines stay inside the square"; "the box is a container").
- Repair = write the model explicitly, with each object's parts listed separately and each constraint marked *given* or *assumed*; then drop or flip one *assumed* constraint (this is O4 and O6 in the schema).
- Evidence on how: generic parts (McCaffrey: +67% relative, single study); underlining the nouns (Frank and Ramscar, 23% to 55%); "box and tacks" (Higgins and Chaires). All three work by splitting an object into a bare part, so the representation changes. Format changes that leave the representation alone do not help (d13).

### 4.5 Failure to try
- Observation: people who saw the better strategy still did not use it (29.4% of the informed group, d10).
- Model: seeing is a read; using requires a committed trial. The operator must therefore force a trial, not only list alternatives.
- Implementation: O6 outputs a *list* of alternative roles or representations; code then picks the top 1-2 and runs a *separate* attempt on each, in fresh context (S3 rule), scored by the check.

### 4.6 Progress monitoring and lookahead (nine-dot)
- Model: solvers pick moves that reduce distance to the goal. If no visible move does, they stop or restart in the same frame.
- Agent analogue: the impasse detector (S6). It already fires on "two rounds with no change". The open issue is what the operator does *after* it fires. Hints about the *kind* of move needed mattered more than naming in the human nine-dot data (80-93% with simplified variants and hints, 0 without; secondary).

### 4.7 Gated reconsideration
- Rule from Illusion of Insight: spontaneous reframing in traces is rare (6.31%) and does not help; reconsideration inserted when token entropy is high helped (+8.41 pp on MATH-500, small open models).
- Implementation: use an uncertainty signal available from sampling (disagreement among 3-5 independent short attempts, or token entropy where available) to trigger O6. This fits G1: a signal, not a schedule.

### 4.8 Anchoring by prior output (multi-turn and multi-agent)
- Early output constrains later output (Laban 2025: 39% drop; GenAI designs raise human fixation).
- Implementation: S3 already uses fresh contexts. The risk is in S5 REVISE and in lessons memory: both show earlier output. That is why lessons are shown after the first attempt only.

---

## 5. What holds up

### 5.1 Replications and consistent findings
- **Pre-use hurts (candle).** Duncker 1945 -> Adamson 1952 (about 2:1) -> Glucksberg 1962 (same direction). Consistent direction across 3 secondary reports. No large modern replication found. **[E] for direction.**
- **Wording matters.** Frank and Ramscar 2003 and Higgins and Chaires agree in direction. Percentages differ between sources (23->55 vs 25->50). **[E] for direction.**
- **Einstellung is real, in several tasks and in experts.** Luchins water jars; chess (Sheridan and Reingold, N=34; experts as vulnerable as novices on problem 1: 8/17 each); anagrams (N=60); chunk decomposition (N=32 and N=28). Four task families. **[E].**
- **It costs speed more reliably than accuracy.** Anagram accuracy unchanged; chunk Exp 2 changed RT only; chess problems with a blunder as the familiar move showed little effect. Luchins and chunk Exp 1 show accuracy costs. **[C] on the accuracy part.**
- **Incubation gives a small gain.** d=0.29 (117 studies), g=0.224 (92 studies). The mean effect is small and moderators are mixed. The schema lists "incubation by distraction" under 4b because unconscious-thought effects failed to replicate. The two do not conflict: a small positive break effect in humans is mostly *beneficial forgetting* of the wrong frame, which an LLM gets for free from a fresh context (S3). **[E] small.**

### 5.2 Failures, boundary conditions, caveats
- **Incentive effect.** Glucksberg's finding is often stretched to "incentives hurt creativity". One study, no N opened. The Wikipedia page notes no main effect of drive. **[S].**
- **Habit tendency did not predict candle success** (N=69, p=.169). The candle item is a low-power probe: few solvers (d11).
- **Developmental and cross-species.** Fixedness is not clearly universal. 4-5 year olds mixed, 6-7 year olds show it. Chimpanzees: success rate 5/8 vs 8/8 (p=.200) but time measures significant. The Shuar result is called preliminary. **[C].**
- **Format alone does not help.** Physical vs paper, N=87, no gain on the pencil problem (d13).
- **Seeing is not using.** 29.4% did not adopt a shortcut they had been shown (d10).
- **Stress/anxiety** raised Luchins rigidity from 70% to 98% (secondary). The nearest analogue in an agent is urgency wording or budget pressure; untested.
- **Dose.** Strong induction hurt only when the answer was weakly associated (N=30). The effect is not uniform.
- **Individual differences.** The politics-rigidity link is small and measure-dependent (a15).
- **Luchins numbers.** The 483 children and 3-of-98 figures are on the current Wikipedia page, but the 1942 monograph was not opened. The "established" mark for K07 rests on the four modern families.

### 5.3 Interventions that worked (human)
| Intervention | Effect | Strength |
|---|---|---|
| Underline object nouns / name parts | 23% -> 55% (candle, written) | secondary, direction [E] |
| Tacks outside box | near-universal solving | secondary |
| Generic-parts training | +67% relative | single study |
| Break, 4 min (as good as 12) | d about 0.2-0.3 | meta-analyses [E] |
| Low-to-high interactivity switch after an impasse | 61% (14/23) of non-solvers vs 5% | single study (b21) |
| Matchstick picture exposing the structure | more solutions | single study |

### 5.4 Interventions that did not work
- Physical vs paper format (no representation change).
- Few-shot examples on Only Connect (GPT-4: 6, 4, 5, 7, 3 walls).
- Scale alone (MacGyver Llama2 7B/13B/70B; MedEinst no size link).
- Spontaneous reframing in traces.
- Unstructured self-reflection: failed for Claude2 and Llama2-13b on MacGyver; helped GPT-4 by 9.7 points on infeasibility only.
- Consensus-style multi-agent systems on MedEinst (MDAgent and DyLAN baseline accuracy 14.93% and 6.51%; table reading). Forced-opposition debate with a judge did help (26.0 -> 37.0) but at 2.46x tokens, not matched.
- Restating the whole context after early commitment recovers only 15-20% of the multi-turn drop.

### 5.5 Moderators to log in any test
Memory strength of the decoy; whether the familiar move is a blunder; time pressure; expertise (experts as vulnerable); item familiarity (humans better on household problems, GPT-4 better on domain-specific ones: d09); reasoning effort.

---

## 6. Language models

### 6.1 Direct tests of fixation
| Study | Task | Result | Caveat |
|---|---|---|---|
| Naeini 2023 | Only Connect walls, decoys | GPT-4 0-shot 6 of 494 walls vs humans 285; decoys removed (Randomized) 59; WordNet 471 | Easier categories in WordNet; one paper; no CoT; no CI; 2023 models |
| Tian 2023 | MacGyver | 35-42% vs 65.1% humans | Wrong tool use (42.4% of GPT-4 errors) is physical infeasibility, not clearly fixation; about 6 human responses per problem, one used |
| Kim 2025 / Shidara 2026 | Medical Einstellung (M-ARC) | 2025: best 52% vs physicians 66%. 2026: Claude 4.1 Opus 0.751 vs 0.66, three others level | M-ARC public, possible contamination |
| Chen 2026 MedEinst | Clinical decoys | Trap rates 42.98% (Claude-Sonnet-4.5) to 60.90% (Gemini-2.5-Pro); GPT-5 51.87% | Paper text and table disagree; trap rate preferred; only zero-shot CoT, effort never varied |
| Liu 2025 | Chat search | Expectations from past systems shape prompts (N=450) | Human-side fixation in using LLMs, not model fixation |
| Gu and Shi 2025 | Continual learning | Methods reach accuracy thresholds earlier but end slightly lower on patched classes | Vision net; Einstellung as shortcut rigidity |

No study found that runs the classic Luchins water-jar, candle, nine-dot or matchstick items on 2025-2026 LLMs (d15, K33). The search tools were rate-limited, so this is weak evidence of absence.

### 6.2 What changed performance, and by how much
| Lever | Change | Where |
|---|---|---|
| Remove the decoys | GPT-4 6 -> 59 walls (clean), 471 (easier categories) | Only Connect |
| Reasoning effort | Monotone rise; GPT-5.4 nearly doubles (CresOWLve). Top models reach physician level on M-ARC at highest effort | CresOWLve, Shidara |
| Chain of thought | WCST 0.3-0.5 -> 4.6-5.0 categories | Hao 2025 |
| Text cue for images | +30.0 to +66.3 points | CREATE |
| Divergent-convergent prompt | +6.5 points efficient | MacGyver, GPT-4 |
| Self-reflect | -9.7 points infeasible for GPT-4; nothing for two other models | MacGyver |
| Forced-opposition debate | +11 points (26.0 -> 37.0), 2.46x tokens | Counter-intuitive arithmetic |
| Entropy-gated reconsideration | +8.41 pp | MATH-500, small open models |
| Structured causal scaffold (authors') | trap rate 43.46 -> 33.75 | MedEinst, Qwen3-32B |
| Few-shot | none | Only Connect |
| Scale | none clear | MacGyver, MedEinst |
| Context rewrite of puzzle | BRAINTEASER sentence puzzles 60.77 -> 67.94 | Jiang 2023 |

### 6.3 Reading
1. **Fixation in LLMs is task dependent.** Decoy-rich grouping and physical tool tasks show big gaps; rebus puzzles show models above humans (humans below GPT-4o by 0.39). A blanket "LLMs are fixated" claim is not supported (K22).
2. **Reasoning effort matters; scale and few-shot do not.** But MedEinst still shows trap rates above 50% for frontier models, so effort alone is not a cure (K19, contested).
3. **Generic reflection is unreliable.** This agrees with SCHEMA 4b. Gated and structured steps do better.
4. **Models name connections worse than they group** (human 80% vs F1 41-45%). A test should score the named reframing separately from the answer.
5. **The model is a strong prior engine.** GenAI output fixes human designers on its own output (c21, c22). This is a risk for any scaffold in which one pass's output is shown to the next.
6. **Contamination.** M-ARC became public in 2025. The 2026 rise may be partly leakage.
7. **Spontaneous insight in traces is rare** (1-7%), so the schema should not wait for the model to reframe by itself.
8. **Several 2026 papers use model names that could not be independently checked** (CREATE, MedEinst, Shidara), and some data are LLM-generated and LLM-filtered.

---

## 7. What our agent should take

Format: item | schema part | status | evidence ids. Anything marked [S] or [C] is a hypothesis and belongs in UNKNOWNS.md, not in SCHEMA.md.

### Add now (established)
These are design constraints and logging rules supported by several sources. None needs a new component.

1. **Log tokens-to-solution next to accuracy on any set-effect test.** | log (schema section 6), S9 | [E] | b15, b17, b18 (K08). Set costs speed more often than accuracy, so accuracy alone can hide a real fixation cost.
2. **Do not rely on the model to reframe by itself.** Any operator that changes representation must be triggered by code on a signal. | G1, S6 | [E] | c18, d08 (reframing in 1-7% of traces, no benefit). Consistent with existing G1.
3. **Keep generic reflection out ("reconsider your answer").** Result is model dependent (-9.7 points for GPT-4, nothing for two others). | 4b | [E] | a22, b25. Already in 4b.
4. **Do not use few-shot examples or a bigger model as a fixation fix.** | S0 | [E] | c03, a20, c07.
5. **Keep lessons shown after the first attempt, and attempts in fresh contexts.** Output from one pass anchors the next (humans and models). | S3, memory | [E] | c21, c22, c28. Already in schema.
6. **If an S1 or O6 step is added, it must change the representation (expose parts and assumed constraints), not only rephrase.** Format-only changes do nothing. | S1, O6 | [E] on the design rule, [S] on any gain | d13, a04, a07.
7. **Log the named reframing separately from the final answer.** Costs no tokens. | log | [S] but free | a18, c03.

### Test first (single-source or contested)
| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | S1 "name the fixation": list each object/concept as bare parts, mark each constraint *given* or *assumed* | S1 | [S] | a02, a04, a07, b05 (K02, K06) |
| T2 | O6 as list-then-try: alternative roles listed, then top 1-2 run as separate fresh attempts | O6 | [S] | d10 (K29) |
| T3 | Trigger O6 on an uncertainty signal (disagreement of 3-5 short attempts), not at fixed points | G1, S6 | [S] | c19, d08 (K23) |
| T4 | Decoy question in S1: "which clue/option fits two groups or answers?" | S1, S4 | [S] | c01, c02 (K13) |
| T5 | S4 harvest of dropped candidates as the anti-fixation mechanism | S4 | [S] | b16 (K09) |
| T6 | Generic-parts step in O6 | O6 | [S] | a07 (K06) |
| T7 | Break = fresh-context restart at an impasse vs continuing the trace | S6, S9 | [E] in humans (d about 0.2-0.3); agent effect unknown | b19, b21 (K10) |
| T8 | Hints on the kind of move (nine-dot style) vs naming | O6 | [S] | d14 (K32) |
| T9 | Dose test of decoy priming strength | G2 | [S] | a25, d12 (K12) |
| T10 | Debate with forced opposition vs single-agent O6 at equal tokens | G4/G9 | [C] | c20, d05, b29 (K27). G9 says no, so the burden is on the test |
| T11 | Urgency/pressure wording as stressor | S0 | [S] | b13, a01 (K03) |
| T12 | Score the model's reframing (name of the hidden category) as its own metric, and test whether it predicts success | log | [S] | a18 (K14) |

---

## 8. Concrete tests on our bench

All arms get the same token budget (counted for the whole pipeline including S1 and any setup, per G7). At least 3 seeds per arm per item. Report 95% bootstrap CIs. Use one current model and, if cost allows, a second family.

**Test A. Classic-item pilot (the gap in K33).**
- Items: Duncker candle isomorphs (candle, nail and mirror, rope and weight, tacks and box), nine-dot with and without hints, matchstick arithmetic, a 6-problem water-jar sequence, plus 10-20 new isomorphs written fresh to limit contamination.
- Arms: (1) plain; (2) plain plus a generic "reconsider" prompt; (3) S1 name-and-mark plus O6 list-only; (4) S1 plus O6 list-then-try; (5) best-of-N plain; (6) forced-opposition debate.
- Metric: solve rate (code-checked or rubric), tokens-to-solution, share of critical water-jar items solved by the habitual path.
- Expected effect: strong models already know the candle problem (contamination). Expect differences only on fresh isomorphs. Predicted order: arm 4 > arm 3 > arm 2 about equal to arm 1. A 10-point gain would be worth keeping.

**Test B. Decoy-present vs decoy-clean.**
- Items: our own wall set (16 items, 4 groups) in pairs, one with decoys and one with the decoys swapped for neutral items, matched on category difficulty (fixes the Naeini WordNet confound). Also a misleading-prior diagnostic set written fresh (not M-ARC).
- Arms: plain; plain with CoT; T4 decoy question; T3 gated O6; effort sweep (low, medium, high thinking) at matched total tokens.
- Metric: group accuracy, walls solved, trap rate (share of errors equal to the planted decoy), named-connection score.
- Expected: a decoy-minus-clean gap exists for plain; it shrinks with the T4 step; the effort sweep shows whether the scaffold beats raw thinking.

**Test C. Dose of priming.**
- Items: the same 20 problems with 0, 1, 3 primed wrong cues (a prior example using the wrong method, repeated).
- Arms: plain vs T1/T2 scaffold.
- Metric: failure rate and tokens-to-solution by dose.
- Expected: failure rises with dose for plain; the scaffold flattens the curve. If plain shows no dose effect, fixation is not the main LLM failure here and S1 naming is not worth its tokens.

**Test D. Water-jar Einstellung.**
- Items: 8 sequences of 5 training problems (method A), 3 critical problems (A works, shorter B exists), 1 extinction problem (only B works).
- Arms: plain in one running context; S1; O6 list-then-try; fresh context per problem (no carry-over).
- Metric: share of critical problems solved by A; extinction failure rate; tokens.
- Expected: the fresh-context arm removes most Einstellung at no token cost. If a modern model shows none in the running context, record it and drop the item.

**Test E. Gated vs always-on O6.**
- Items: Tests A and B pooled.
- Arms: O6 always; O6 on disagreement among 3 short attempts; no O6.
- Metric: solve rate at equal tokens.
- Expected: gated at least as good as always-on, at lower cost. If always-on wins, G1 needs a footnote.

**Test F. Break/restart.**
- Items: items where plain fails after the first attempt.
- Arms: continue the same trace; clean re-read in fresh context (original wording); fresh context with a different operator.
- Metric: solve rate at equal tokens.
- Expected: fresh restart at least as good as continuing (human d about 0.2-0.3).

**Test G. Debate vs O6.**
- Arms: forced-opposition debate with judge (about 2.46x tokens) vs single-agent O6 with matched total tokens vs best-of-N.
- Metric: solve rate on misleading-prior items. If debate does not beat best-of-N at equal tokens, G9 stands.

**Common control:** rename all surface nouns and rerun. If plain solves a classic item at 100% but fails its fresh isomorph, record contamination.

---

## 9. What does not transfer, and why

- **Incentive and anxiety effects** (Glucksberg, Luchins stress): human motivation effects. A model has no drive. Urgency wording may or may not act as a cue. Not a schema item.
- **Developmental, cross-cultural and chimpanzee data**: background only. They suggest fixation is learned, not a species limit. No agent test follows.
- **Eye movements and dwell counts**: there is no gaze. Only a behavioural proxy (distinct candidates raised) exists.
- **Sleep and long incubation**: no unconscious processing. A fresh context is the nearest equivalent, and it is cheap.
- **Aha ratings**: a human experience (r=0.40-0.50 with accuracy for insight tasks only). Model "aha" text is not evidence (G10); only 6.31% of traces show a shift and it does not predict success.
- **Physical interaction with the task** (paper vs real objects): no effect even in humans (d13).
- **Candle problem as a measure of individual fixation**: low power even in humans (N=69, p=.169). In an agent the classic item is contaminated by training. Use fresh isomorphs.
- **"Productive thinking" as genuine novelty**: judged by running (G8), not by a model's view of whether it saw anew.
- **Missing physical grounding**: part of the MacGyver gap is physical feasibility (42.4% wrong tool use), not fixation. A text scaffold cannot fix missing grounding.
- **GenAI fixation in human designers**: a human-side effect. It becomes relevant only if the agent's output is shown to a human or another agent (G4).

---

## 10. Open questions

1. Does an S1 naming step plus O6 list-then-try beat plain and generic reconsider at equal tokens on classic and fresh Duncker-type items? No study exists (K33).
2. How large is LLM Einstellung on water-jar sequences for 2025-2026 models, and does a bigger thinking budget remove it?
3. Is the Naeini decoy effect still present in current reasoning models when decoy-clean walls are matched on category difficulty?
4. Do MedEinst's baseline accuracies hold (paper text and table disagree)? Does varying reasoning effort lower trap rate? The paper only ran zero-shot CoT.
5. Does gated reconsideration scale beyond small Qwen/Llama models?
6. Primary human data are missing: Duncker 1945, Glucksberg 1962 (N, means), Adamson 1952, Frank and Ramscar 2003 (23/55 vs 25/50), Luchins 1942 group sizes. Is there a large-sample replication of the prior-use or incentive effect?
7. What do Weisberg and Alba 1981 and MacGregor et al. 2001 show for the nine-dot hint effect? Does an LLM follow the same pattern?
8. Does LLM fixation scale with the memory strength of the decoy (dose)?
9. Does debate reduce or amplify fixation at matched tokens? MAD +11 points vs MDAgent/DyLAN collapse.
10. Is the MacGyver gap fixation or missing grounding? No newer models were tested.
11. Is fixation in LLMs a problem of *seeing* (representation) or of *trying* (as in d10)? An experiment that supplies the alternative explicitly and measures use would separate them.
12. Does the 2026 rise on M-ARC reflect reasoning or contamination?

---

## 11. Sources

[V] = opened and read this session (see the limits in the evidence lines for what each page contained). [M] = snippet, citation, or recalled only.

**Human, secondary**
- [V] Wikipedia, Candle problem. https://en.wikipedia.org/wiki/Candle_problem (a01, a02, b01, b02, d02)
- [V] Wikipedia, Functional fixedness. https://en.wikipedia.org/wiki/Functional_fixedness (a03-a07, b03-b05, b08, d03)
- [V] Wikipedia, Einstellung effect. https://en.wikipedia.org/wiki/Einstellung_effect (a08, a09, b13, b14, d01)
- [V] Wikipedia, Wolfgang Kohler. https://en.wikipedia.org/wiki/Wolfgang_K%C3%B6hler (a10)
- [V] Wikipedia, Insight. https://en.wikipedia.org/wiki/Insight (a11, b31)
- [V] Wikipedia, Gestalt psychology. https://en.wikipedia.org/wiki/Gestalt_psychology (a12)
- [V] Wikipedia, Karl Duncker. https://en.wikipedia.org/wiki/Karl_Duncker (a13)
- [V] Wikipedia, Nine-dot problem / Nine dots puzzle. https://en.wikipedia.org/wiki/Nine-dot_problem ; https://en.wikipedia.org/wiki/Nine_dots_puzzle (a14, d16)
- [V] Wikipedia, Mental set. https://en.wikipedia.org/wiki/Mental_set (a15)
- [V] Tran, Esseily, Bovet, Kiraly (2021) review. https://pmc.ncbi.nlm.nih.gov/articles/PMC8649634/ (b06, b07, b09)
- [V] Detour paradigm in animal cognition (2018). https://pmc.ncbi.nlm.nih.gov/articles/PMC5756264/ (b12)
- [V] Incubation review (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4956660/ (b19, b20)
- [V] Role of motor activity in the nine-dot problem (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6352738/ (d14)

**Human, primary full text**
- [V] Sheridan and Reingold (2013) Einstellung in chess. https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/
- [V] Ellis and Reingold (2014) anagrams. https://pmc.ncbi.nlm.nih.gov/articles/PMC4079068/
- [V] Huang, Tang, Hu (2018) chunk decomposition. https://pmc.ncbi.nlm.nih.gov/articles/PMC6297678/
- [V] Chimpanzee functional fixedness (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11130300/
- [V] Incubation and interactivity (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC6994426/
- [V] Webb, Little, Cropper (2016) Insight is not in the problem. https://pmc.ncbi.nlm.nih.gov/articles/PMC5035735/
- [V] Overcoming cognitive set bias requires more than seeing an alternative (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC8828898/
- [V] Can habits impede creativity by inducing fixation? (2021). https://pmc.ncbi.nlm.nih.gov/articles/PMC8548374/
- [V] Semantic accessibility and heuristic fixation (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13117359/
- [V] Physical interaction with insight problems (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13208192/
- [V] Crossref / Europe PMC searches, 2026-11-03. https://www.ebi.ac.uk/europepmc/webservices/rest/search (d15)

**LLM and AI**
- [V] Naeini et al. (2023) Only Connect Wall. https://arxiv.org/abs/2306.11167
- [V] Tian et al. (2023/2025) MacGyver. https://arxiv.org/abs/2311.09682
- [V] Kim et al. (2025) M-ARC. https://arxiv.org/abs/2502.04381 ; peer-reviewed version https://pmc.ncbi.nlm.nih.gov/articles/PMC12606185/
- [V] Shidara et al. (2026). https://arxiv.org/abs/2601.11866
- [V] Chen et al. (2026) MedEinst. https://arxiv.org/abs/2601.06636
- [V] Ismayilzada et al. (2026) CresOWLve. https://arxiv.org/abs/2604.03374
- [V] Yang, Jangra, Muresan (2026) CREATE. https://arxiv.org/abs/2610.18569
- [V] Zhang et al. (2025) rebus. https://arxiv.org/abs/2503.23327
- [V] d'Aliberti and Horta Ribeiro (2026) Illusion of Insight. https://arxiv.org/abs/2601.00514
- [V] Liang et al. (2023/2024) MAD. https://arxiv.org/abs/2305.19118
- [V] Jiang et al. (2023) BRAINTEASER. https://arxiv.org/abs/2310.05057
- [V] Chen et al. (2024) Weak-eval-Strong. https://arxiv.org/abs/2410.06733
- [V] Liu, Karimnazarov, White (2025) Trapped by Expectations. https://arxiv.org/abs/2504.02074
- [V] Hao, Alexandre, Yu (2025) WCST. https://arxiv.org/abs/2505.22112
- [V] de Langis et al. (2025). https://arxiv.org/abs/2504.02789
- [V] Laban et al. (2025) Lost in multi-turn. https://arxiv.org/abs/2505.06120
- [V] Chen et al. (2025) design fixation in GenAI. https://arxiv.org/abs/2502.05870
- [V] Wadinambiarachchi et al. (2024). https://arxiv.org/abs/2403.11164
- [V] Xu, Martelaro, McComb (2026) CRDAL. https://arxiv.org/abs/2603.24768
- [V] Jeon, Cho, Shu (2025) PPoGA. https://arxiv.org/abs/2602.00007
- [V] Gu and Shi (2025) shortcut rigidity. https://arxiv.org/abs/2510.00475
- [V] Friston et al. (2025) active inference. https://arxiv.org/abs/2512.21129
- [V] Yang et al. (2025) Aha moments. https://arxiv.org/abs/2504.02956

**Cited or recalled, not opened**
- [M] Duncker (1945) On problem solving. https://doi.org/10.1037/h0093599
- [M] Luchins (1942) Mechanization in problem solving. https://doi.org/10.1037/h0093502
- [M] Bilalic, McLeod, Gobet (2008). https://doi.org/10.1016/j.cognition.2008.05.005 (abstract only; evidence b32 gives a different DOI)
- [M] Weisberg and Alba (1981). https://doi.org/10.1037/0096-3445.110.2.169
- [M] Vul and Pashler (2007). https://doi.org/10.1016/j.cognition.2006.01.003
- [M] Birch (1945). https://doi.org/10.1037/h0063625
- [M] Beda and Smith (2018) Chasing red herrings (via Naeini et al.)
- [M] Glucksberg (1962), Adamson (1952), Frank and Ramscar (2003), Higgins and Chaires, Maier (1930/31), Birch and Rabinowitz (1951), McCaffrey (2012), German and Barrett (2005), MacGregor, Ormerod and Chronicle (2001): seen only through the Wikipedia pages and reviews above.
- [M] Kohler (1917) The Mentality of Apes; Wertheimer (1945) Productive Thinking: not opened.

**Corrections applied from critique.md:** MacGyver counts (1,306 solvable, 377 unsolvable, 1,683 total); MedEinst: use trap rates, not text accuracy; Frank and Ramscar: prefer 23/55; Luchins 483 and 3-of-98 traced to Wikipedia only.

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 4 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **A12.06-K07** (reworded: the sources support less). Wikipedia attributes the 70/98/58/97 figures to a stress-vs-non-stress speed test of 98 students (Luchins and Luchins), not to Luchins 1942 (483 children); chess N=34, anagrams N=60, chunk N=32/28 are correct. Corrected claim: Einstellung (mechanised set) is real in humans: in a Luchins and Luchins water-jar speed test (98 students, as reported on Wikipedia) rigidity was 70% without stress and 98% under anxiety, extinction-problem failure 58% and 97%; also seen with experts in chess (Sheridan and Reingold 2013, N=34), anagrams (N=60) and chunk decomposition (N=32 and 28). Luchins figures come from Wikipedia only; primary Luchins 1942 and 1959 unopened.
- **A12.06-K26** (reworded: the sources support less). The 67.4% vs 78.2% novel-term figures compare ChatGPT output vocabulary with Red Dot award designs (AI-output fixation), not designers' fixation after exposure; originality effect is -0.03 (negligible), fluency -0.21 has only 76% probability negative. Corrected claim: A 60-person sketching study found that seeing AI-generated example images was linked to more fixation on the example and fewer, less varied ideas (GenAI fluency about -0.21, 89% interval about -0.66 to 0.26, 76% probability negative; originality -0.03, 97% probability negative but negligible). Separately, a 10-designer ChatGPT case study found ChatGPT's own chair descriptions had a lower novel-term share (67.4%) than Red Dot award designs (78.2%), which shows fixation in the AI output, not in the designers. Effects are small with wide intervals.
