# Expert-novice designers: deep document

*Subfield E05.09. Focus: the solution-first conjecture (Lawson; Cross). Built from evidence_a-d.jsonl (a01-a29, b01-b27, c01-c30, d01-d17), claims.jsonl (K01-K25) and critique.md in this folder. Evidence ids are cited in brackets. Status words follow the schema: established, single-source, contested. No new searching was done for this document.*

*Honest summary up front. The famous claim is old (1979), the human samples are tiny, and no direct failed replication exists. The best-supported parts are: (1) the style is learned, not innate; (2) early conjectures cost something (fixation) and help something (they probe the problem); (3) LLMs in hidden-rule loops mostly try to confirm their guess. The claim that solution-first makes better designs is contested. The claim that experts scope the problem more broadly is also contested.*

---

## 1. What it is

**The claim.** Skilled designers do not first analyse the whole problem and then synthesise a solution. They jump early to a candidate solution (a "conjecture") and use it to learn what the problem is. Cross calls this being solution-focused. The contrast is problem-focused: study the problem structure first, solve after.

**Where the term comes from.** Lawson (1979) gave final-year architecture students and postgraduate science students a block-arranging puzzle. Scientists hunted for the hidden rule. Architects went for a good-looking answer and tried the next best when one was refused. [a01, b01, a02]

**Why it matters for our agent.** Our schema has a state that restates the task (S1), a state that writes candidate rules (S2), a generate state (S3) with fresh contexts, a test state (S4), and an impasse state with operators including "reframe the goal" (O8). The question is where an early conjecture sits in that graph, when it should be allowed, and what stops it from becoming a trap. Memory matters too: the mechanism that makes expert conjecture work seems to be stored chunks of past solutions and abstract schemas. [a22, a23, b10]

**Scope of this document.** Expert-novice differences in general are covered by the parallel subfield "Expert-novice differences", fixation in depth by the design-fixation subfield, co-evolution by "Design-space exploration" and "Computational design", and designerly knowing by "Designerly ways of knowing". Here we only cover what bears on solution-first conjecture and on how experts and novices differ in doing it. We note links, not content.

**Four plain definitions.**
- Conjecture: a candidate solution written early, before the problem is fully known.
- Problem-driven: spend early effort on goals, constraints and criteria; solution later.
- Solution-driven: start from a candidate and let its failures teach the constraints.
- Co-evolution: problem and solution views are changed in turns until they fit (Dorst and Cross 2001, recalled, not opened [c28]).

---

## 2. History and theories in depth

### 2.1 Founding experiment: Lawson 1979
- Task: arrange coloured blocks in a 3 by 4 bay single-storey layout, red and blue faces, so the perimeter shows as much of a target colour as possible. Hidden rules about which blocks may touch change per problem. A computer answers allowed or not allowed. Over 6000 possible arrangements. [b01]
- Result as retold: scientists tried many mixes fast to discover the rule structure (problem-focused). Architects picked blocks for the colour target and swapped in the next best option when refused (solution-focused). [a01, b01]
- What we do not know: group sizes, scores, significance. The 1979 paper was paywalled and was not opened. Everything in the field about it is a textbook retelling. [a01, b01, d06, critique item 5]
- Task bias: the environment rewards solution-first search because a refusal is cheap and informative. The groups also differ in selection and education and were not randomly assigned. [b01]

### 2.2 Lawson's own control: first-years
- Lawson repeated it with school leavers and first-day architecture students. No consistent shared strategy, and overall problem solving was worse. He concluded the style comes from the degree. [b02, a02, d06]
- Cross (2001/2004) states the same: first-year science and architecture students did not show the difference. [a02]
- This is not a replication of the original effect. It is a different population. It supports "learned", not "true". The weakness: the first-years were also much less skilled at solving, so strategy contrast is muddy. [b02]

### 2.3 Three rival explanations for the style
Restrepo and Christiaans (2004) list them: [a03]
1. Education. Lawson; Thomas and Carroll (who say designers will design even if they could problem-solve).
2. Specific experience of the problem type. Lloyd and Scott (1994/95): designers with specific experience of the problem type approached it through solution conjectures; general seniority did not matter. [a04, b03]
3. Personal idiosyncrasy. Differences exist even in homogeneous groups (Christiaans, Dorst, Restrepo). Senior students with equal education wrote the brief in their own words either as abstract relations (problem-oriented) or as physical objects (solution-oriented), and this split was replicated in a later study with senior and intermediate students. [a05]

No longitudinal study separates the three. The authors say so. [a03] So the style may be a trait of the person or run, not only of expertise. For an agent this means: log which mode each attempt used.

### 2.4 Cross: solution-focus as a response to ill-defined problems
- Cross (2001/2004) argues solution-focus suits ill-defined problems that cannot become well-defined; designers satisfice rather than optimise. Cost: fixation on existing solutions. [a29]
- Standard expertise results (chess, physics) come from well-defined problems. Creative experts deliberately treat the task as ill-defined, treat it as harder than novices do, and solve similar tasks from first principles rather than recalling earlier solutions. [a13, b13]
- Ball and Christensen (2019) repeat that experts treat even well-defined problems as ill-defined and relax or redefine constraints. No experiment varied definedness directly. [d05]

### 2.5 Co-evolution
- Cross and Dorst (1998): experienced industrial designers explore the problem space, find a partial structure, use it to partly structure the solution space, check implications, feed back. Kolodner and Wills (1996): proposed solutions remind designers of issues. Solution conjectures are the tool for understanding the problem. [a08]
- Computational precedent: Maher and Tang (2003) model co-evolution (title seen only). [c29] Dorst and Cross 2001 recalled, not opened. [c28]
- A grounded-theory model (Zhang and Ma 2021, ten graduate students): a conjecture is triggered by analogising, inspiring, evaluating or questioning; it expands the problem space; the problem focus is then adjusted by small or radical steps. [b22]

### 2.6 Framing and primary generators
- Experienced architects have strong guiding themes (Lloyd and Scott 1995); outstanding engineers used a strong guiding theme (Cross and Clayburn Cross 1998); outstanding architects used primary generators to set problem boundaries and solution goals (Darke 1979). Goel and Pirolli: problem structuring dominates early but recurs throughout. [a09]
- Frame change tracks success in one case pair: the successful student team used five frames in sequence; the unsuccessful team used one frame and spent long naming problem features. N = 2 teams. [a10]
- Breaking a conventional frame needs procedural knowledge for the new frame: experienced architect vs non-architect, N = 2. [a14, b18]

### 2.7 Breadth-first versus depth-first, and opportunism
- Textbook: novices depth-first, experts top-down breadth-first. Cross says too simple. Depth-first lowers cognitive load; breadth-first lowers commitment. [a13, b13]
- Guindon (1990): designers interleave specification and solution; deviation from top-down is natural for ill-structured problems. Ball and Ormerod (1995), expert electronics engineers: very few deviations, only brief depth-first probes of a concept. [a11, b12] Rival accounts; no discriminating experiment in the reviews.
- Modal shifts: in a single experienced engineer 6 of 8 novel design decisions came while rapidly alternating drawing, examining and thinking. Student protocol studies link quality to rapid alternation. Correlational. [a12, b19]

### 2.8 The counterpoint: experts scope more
- Atman et al. (1999, via Cross): freshmen who spent a large share of time defining the problem did not produce quality designs; for seniors, more scoping (more and wider information) did. [a07, b05]
- Atman et al. (2007): 19 experts versus 26 freshmen and 24 seniors on a playground task; the main differences were problem scoping and information gathering. Counts seen only in an abstract snippet; not verified. [a17, d17]
- Christiaans and Dorst (1992): the more creative senior group asked less information, processed it at once and set priorities early. The other group collected data as a substitute for designing; need for information tracked inability to cope with uncertainty, not education. [a06, b04]
- So "solution-first" and "scope more" can both be true of experts. They refer to different things: early conjecture versus how much and what kind of problem information the designer takes in. See 5.2.

### 2.9 Fixation, attachment and restart
- Jansson and Smith (1991): senior students and professional mechanical engineers shown an example reproduced many more features than controls. Experienced people fixate too. Counts not in the source seen. [b14]
- Purcell and Gero (1991-96): mechanical engineers were more affected by an example than industrial designers; an innovative example made engineers fixate on its principle; industrial designers varied widely (fixated on being different). Authors point to educational program. [b15]
- Attachment: experienced mechanical engineers, senior electronics students and software designers pursued one proposal and patched it (Rowe, Ullman, Ball, Guindon). [b17]
- Smith and Tjandra (1998): in a game with nine groups of four, the top three groups were the three that scrapped their first design and restarted. [b16]

### 2.10 Computational account of why experts go solution-first
- Cited accounts: experts store larger organised chunks and many solution examples (Petre 2004; Cross 2004); novices start from problem structure if they cannot recognise a solution (Liikkanen and Perttula 2009); novices use trial and error (Ahmed et al. 2003). [a23]
- Perisic et al. (2019) agent model: teams with learned links needed fewer steps and made more new structures per step, hence more solution-side effort. This follows from design (experience = stored links), so it illustrates the theory and is not independent evidence. [a22]

---

## 3. Core findings with exact numbers

Status key: E established (two or more independent sources agree), S single-source, C contested. "Review" means the number is second-hand through a review and the original was not opened.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Architects solution-first, scientists rule-first on block task | 3x4 bays; over 6000 arrangements; hidden rules; group N not found | Lawson 1979 via How Designers Think [b01, a01] | E (direction); numbers unknown |
| Style is learned: not found in first-years | School leavers and first-year architecture students: no common strategy; lower skill overall; N not given | Lawson, Cross [b02, a02] | E |
| Specific experience with problem type tied to conjecture-led reasoning | More experienced: more generative; less experienced: more deductive; N not given | Lloyd and Scott 1994 via Cross [a04, b03] | S (review) |
| Same-education seniors split by early representation | Relational vs object-based brief restatements; replicated with senior plus intermediate students; N not given | Christiaans and Restrepo 2001/2003 [a05] | S |
| Problem-driven beat solution-driven on quality | N = 9 experienced designers; four strategies; effect sizes unknown; paper not opened | Kruger and Cross 2006 via Lemons [d01, b06] | C |
| Solution-driven scored higher on creativity | Abstract only; no effect size | Kruger and Cross 2006 [d02] | S |
| Students mostly problem-driven | 6 of 10 problem, 3 solution, 1 information, 0 knowledge | Lemons et al. 2011 [b07, d01] | S |
| Freshmen: big share on problem definition did not give quality | N not in review | Atman et al. 1999 via Cross [a07, b05] | S |
| Experts vs students: scoping and information gathering differ | 19 experts, 26 freshmen, 24 seniors (unverified) | Atman et al. 2007 [a17, d17] | S (unverified N) |
| Experts wrote more but not a different mix | 57 vs 11.5 statements; design detail 46% vs 48%; context 54% vs 52%; novices 30% natural frames vs 18%; 2 of 4 experts breadth-first; n = 4 vs 124; coder agreement 77% first pass, 72% across all four; different collection methods | Morozov et al. 2007 [a20, b08, b09] | S |
| Experts analogise more; experts schema-driven, novices case-driven | 32.2 vs 22.9 per hour; schema 53.1 vs 16.5; case 11.3 vs 29.4; F(1,14)=5.04 p=.041; form F=31.24; interaction F=111.33; N = 8 vs 8 | Ball, Ormerod, Morley 2004 [b10] | S |
| Process shape barely differs; persistence does | Phase order and time per phase: no difference; longest continuous design activity 976 s vs 446 s (significant); backward transitions 100% vs 74%, p=0.06; 4 vs 5 | Chen, Chen, Yang 2022 [b11] | C |
| Expert activity about 3 times novice, better organised | N = 2 (one expert, one novice) | Kavakli and Gero 2001/2002 [a15, a16] | S |
| Frame changes tracked success | 5 frames vs 1 frame; 1 team vs 1 team | Valkenburg and Dorst 1998 via Cross [a10] | S |
| Novel decisions in triple-mode periods | 6 of 8; one designer | Akin and Lin 1995 [a12] | S |
| Senior teams iterated scoping and alternatives | 48 iterations in one senior team; 4 minutes scoping vs immediate alternatives; 4 teams | Purzer et al. 2008 [a18] | S |
| Individual experts vary hugely | Scoping 10% to 30% of time; idea generation 5% to 66% | Atman et al. 2003 [a21] | S |
| Scrapping the first design went with winning | Top 3 of 9 groups scrapped and restarted | Smith and Tjandra 1998 [b16] | S |
| Example solutions induce fixation in professionals | Counts not given | Jansson and Smith 1991 [b14] | E (direction; with b15, b17) |
| Number of problem-exploration patterns vs placement | 252 problems; 32 patterns; r(102) = -0.18, p<0.05; all 19 finalists had 2+ patterns; 5 single-pattern solutions were not finalists | Studer et al. 2018 [d03, d04] | S |
| Agent model: experts fewer steps | Steps 290.7 vs 379.6; 310.6 vs 401.5; 316.2 vs 494.7; new links/step 1.07 vs 0.55, 1.19 vs 0.55, 1.32 vs 0.47; raw counts not significant on tasks 2 and 3 | Perisic et al. 2019 [a22] | S (model) |
| LLM rule-discovery: confirmation bias | Success 6% to 78%; counterexample prompts 42% to 56% mean discovery; 11 LLMs; 80 episodes per cell | Jhaveri et al. 2026 [d07, d08] | E (with d09) |
| Reasoning models do better on rule games | GPT-5.2-Chat 75%, GPT-OSS-120B 68%, best instruction-tuned DeepSeek-V3.1 41%, others 33-35%; confirmation ratios 27.3% and 39.0% vs 66-82% | Bertolazzi et al. 2026 [d09] | E (with d07) |
| LLM can be steered into either style | P-S index right in 20/20 problem-driven and 18/20 solution-driven runs; SS transitions 29.4% vs 9.9%, t=-8.949 | Zhang et al. 2025 [c01-c05] | S |
| LLM lacks problem-solution back-and-forth | PS transitions 6.7 vs 10.5, t=-3.83, p=.001; SP 6.4 vs 9.8, p=.003 | Zhang et al. 2025 [c03] | S |
| LLM fixation on text | Unique terms 67.4% vs 78.2%; structure keywords per 100: 142.71 vs 208.57; unique word items 180 vs 312, 86 shared | Chen et al. 2025 [b23, c15] | S |
| AI images raise fixation in humans | GenAI +.32 (89% CI .11 to .54, BF 124); image search +.27 (BF 42.48); fixation carried to next sketch rho = 0.56; N = 60, 277 sketches | Wadinambiarachchi et al. 2024 [b24, c11-c13] | S |
| GPT-4 team placed second of six | 14.8 m vs winner 37.66 m, mean 12.0 m; 16 prototypes of 116; pneumatic dropped after 1 iteration; 97 prompts | Ege et al. 2025 [c06-c09, b25] | S |
| LLM reframing gave no gain | 280 analysed of 456; 15 expert raters; four conditions | Shin et al. 2025 [a24] | C |
| LLM judge vs humans | Pearson expert-GPT-4 .556, novice-GPT-4 .547, expert-novice .602; Fleiss kappa .40-.49; r=0.50 over 1,103 ideas; context effect on humans b=0.18 (N=1,195), none for LLMs | Shaer 2024 [c19]; Lyu 2026 [d14] | S |
| Abstract memory transfers, cases win in-task | Forward transfer ALFWorld +6.5 vs -9.5, BabyAI +9.0 vs -7.5; task A 80.5 vs 65.5 | Hu et al. 2026 [d10] | S |
| Agents pivot at wrong rate | Pivot rate humans 25%, Codex 9%, MLEvolve 58%; post-pivot effect +0.089 vs -0.008; top humans return on 9% of versions, 78% of returns end higher | TraceML 2026 [d12] | S |
| Restart with carry-over beats cold restart | 71.8% vs 66.8% resolution (SWE-bench Verified) | Wang et al. 2026 [d11] | S |

---

## 4. Mechanisms and models

Each mechanism is written so an engineer can implement it. Status marks follow section 3.

### 4.1 Conjecture as a probe (Lawson)
- State: a candidate solution C and a feedback oracle F (a check, a refusal, a test run).
- Step: write C early, run F(C), read the failure, convert the failure into one new constraint, add it to the constraint list, write C' that satisfies all listed constraints.
- Why it works in Lawson's task: F is cheap and informative. Each refused arrangement names a rule. [b01]
- When it fails: when F is not informative or is slow, a guess is just a guess. Specific experience gates it; without a close precedent an early conjecture is noise. [a04, b03]
- Implementation hook: only enter this loop if the class has a cheap check (schema S0 asks this already). Otherwise lean problem-side.

### 4.2 The falsification rule (needed to make the loop work)
- The LLM failure in hidden-rule games is not "too slow to guess". It is guessing, then picking tests that fit the guess. [d07, d09]
- Rule: after writing C, the program asks for the test input most likely to break C, runs it, and counts a "break" attempt. Negative testing was the main driver of success in FalsifyBench. [d09]
- Counterexample prompts (Dual-Goal, Think-in-Opposites) raised discovery from 42% to 56% on average over 11 LLMs; gains were significant for thinking models and mixed for non-thinking ones. [d07]
- Fine-tuning on intervention traces cut the bias and carried to the Blicket test and math retries (two models trained; at most 2% degradation elsewhere). Not a scaffold result, but shows the habit transfers. [d08]

### 4.3 Co-evolution loop
- Cycle: problem view P, solution view S. Explore P to a partial structure; use it to shape S; check what S implies for P; update P; repeat until a matching pair. [a08]
- Conjecture triggers that open P (Zhang and Ma): analogising, inspiring, evaluating, questioning. Then adjust the focus by small or radical steps. [b22]
- Measurable proxies from FBS coding: P-S index (ratio of problem-space to solution-space statements, threshold 1.0), and transition counts PS, SP, SS. [c02, c05]
- LLM gap: single-pass chain-of-thought stays in one space and moves linearly; the unprompted LLM in a 36-person study never reshaped the problem space. [c03, d13] So forcing alternation must be done by the program. Forced alternation itself has not been tested.

### 4.4 Frame as a one-line anchor
- Experts hold a primary generator or guiding theme that sets problem boundaries and solution goals. [a09]
- Implementation: store one line per task, revisit on a signal only. The successful team in Valkenburg and Dorst changed frames five times; the failing one never. [a10] So the rule is revisit on a signal, not never and not on a timer.

### 4.5 Memory mechanism: chunks, schemas, cases
- Experts: abstract schema-driven analogies (53.1/h) versus novice case-driven (29.4/h). Case-driven analogies mostly used surface cues. [b10]
- Perisic et al. model: stored links make solution nodes reachable at once, which produces solution-first behaviour. [a22]
- LLM agent memory study: abstract insights transferred across tasks (+6.5, +9.0) while raw trajectories transferred negatively (-9.5, -7.5) but won within the same task (80.5 vs 65.5). [d10]
- Design: hybrid memory, with similarity-gated retrieval. Near match: raw case. Far: abstract schema.

### 4.6 Persist, abandon and return
- Human pattern: attachment to the first idea is common; the best groups scrapped and restarted; frame changers did better. [b17, b16, a10]
- LLM pattern: dropped the pneumatic concept after one failed iteration when the winner iterated it to 37.66 m; also clung to the last item in a list and added unneeded complexity. [c08, c09, b25]
- Agent traces: pivot rate 9% to 58% but no net gain; almost never return to parked approaches. [d12]
- Restart helps only with carry-over: 71.8% with the old diff as overlay vs 66.8% cold. [d11]
- Implementation: a pivot needs (a) a diagnosis line citing the failing output (G2), (b) a parked-idea note, (c) a return path. The "persist k tries" threshold k is untuned.

### 4.7 Mode alternation as a progress signal
- More successful students alternated rapidly between information, sketching and reflection. A single experienced designer's novel decisions mostly came in such periods. [a12, b19]
- Chen et al. found no difference in phase order or time per phase, only persistence (976 s vs 446 s). [b11]
- Implication: measure alternation or depth of persistence in agent traces, but do not hard-code a phase order. Weak evidence.

---

## 5. What holds up

### 5.1 Replications and what they did and did not replicate
- Lawson 1979: no replication of the strategy contrast with professionals found. A first-year control showed no consistent strategy. Different population. [b02, a02, critique]
- Restrepo and Christiaans: the problem-oriented vs object-oriented restatement split was replicated across two student studies. Same education level still split, so experience does not explain it fully. [a05]
- Kruger and Cross four strategies were reused by Lemons et al. on ten students: 6 problem, 3 solution, 1 information. A classification reuse, not a test of the quality effect. [b07]
- Fixation: Jansson and Smith effect extended by Purcell and Gero with a boundary condition (discipline and type of example). [b14, b15]
- Co-evolution findings: from several independent protocol groups (Cross and Dorst; Kolodner and Wills; Guindon). All small protocol studies. [a08, a11]

### 5.2 Failures, nulls and contradictions
- No difference in phase sequence or time per phase between 4 experts and 5 novices; only continuous design activity differed. [b11] N is too small to overturn older findings. [critique]
- Mix of problem context versus design detail was equal across groups (46/54 vs 48/52); the expert "broader scope" belief is not seen here. The a20 per-expert range (30 to 51% vs 49 to 70%) hides this. Only 2 of 4 experts were breadth-first. [b09, a20, critique correction 1]
- Cross and Lawson say experts are solution-focused. Kruger and Cross and Lemons find problem-driven designers do better on quality. Reconciliation: solution-first describes common expert habit, not the best strategy. Unresolved. [critique, K03]
- Atman: experts scope more than students. Conjecture-first and scoping can coexist. [a17]
- Delft workshop team produced alternatives earlier than individuals and then stepped back to clarify more often. [a19] Teams may shift timing.
- Training can flip the failure mode: engineers fixate on an example, industrial designers diverge too hard. [b15]
- Time on problem definition helped seniors, did not help freshmen. [a07, b05] Moderator is skill at scoping.

### 5.3 Moderators and boundary conditions
- Experience: first-years show no style difference. [a02]
- Specific experience of the problem type, not general seniority. [a04]
- Skill at scoping (freshmen vs seniors). [a07]
- Tolerance of uncertainty drives information gathering, not education. [a06]
- Problem definedness: argued (Cross) but never manipulated. [a29, d05]
- Discipline and example type (fixation). [b15]
- Feedback cost: Lawson's task rewards probing because refusal is cheap. [b01]
- Team versus individual. [a19, a18]
- Collection method (spoken vs written) blocks the Morozov comparison. [b08]

### 5.4 Interventions
Worked (weak evidence):
- Counterexample prompts in rule discovery: 42% to 56%. [d07]
- Style prompts on GPT-4o produced the intended P-S style and raised novelty and integrity over baseline (p<0.05, two raters r=0.77; N=10 per cell; scores read from a figure). [c01-c05]
- Restart with carry-over: 71.8% vs 66.8%. [d11]
- Role-play mentee persona (Feed-O-Meter): expert-rated specificity 4.64 vs 4.34 (p=0.0005), justification 4.73 vs 4.42 (p=0.0001), action 4.19 vs 3.93 (p=0.0025); overall helpfulness 4.47 vs 4.38 (n.s.); 24 students, 96 sessions, 12 raters. [c17]
- A short planning prompt distilled from human practice moved agent pivots toward the human profile and lifted scores (effect size not extracted). [d12]
- Abstract memory for cross-task transfer. [d10]

Did not work or unproven:
- LLM help in problem reframing: no gain in novelty or usefulness of frames; widened expert-novice gap (3 or more quiz items correct benefited). [a24]
- AI images to cut fixation: raised fixation and lowered fluency, variety and originality (small effects, wide intervals; fluency total effect about -.29, 76% posterior probability negative). [b24, c12]
- Unprompted LLM chat did not reshape the problem space. [d13]
- Multi-agent ideation loop (MIDAS, 13 agents): 50-80 raw ideas per session reduced to 11-24; no head-to-head quality numbers. [c22]

---

## 6. Language models

### 6.1 What LLMs do on solution-first versus problem-first
- GPT-4o can be prompted (zero-shot chain of thought) into either a problem-driven or solution-driven process on a bathroom-product task. Unconstrained: formulation 31.7% (problem) vs 16.3% (solution), t=8.489; structure 10.6 vs 29.3; function 18.9 vs 9.2 (all p<0.001). Coder agreement 79.5%. 10 runs per cell, human comparison from prior studies. [c01]
- Solution-driven runs iterated inside the solution space: SS 29.4% vs 9.9% (t=-8.949); with constraint 27.9 vs 13.1. [c02]
- P-S index correct in 20/20 and 18/20 runs. [c05]
- Both styles beat the plain GPT-4o baseline on novelty and integrity (p<0.05; solution-driven integrity higher than problem-driven). Problem-first with hard constraints cost feasibility (P2). Two expert raters, r=0.77. [c04]
- Missing: back-and-forth. PS 6.7 vs 10.5 (t=-3.83, p=.001); SP 6.4 vs 9.8 (p=.003). [c03]

### 6.2 Hypothesis-testing analogue of Lawson
- 11 LLMs in a 2-4-6-style loop: success 6% to 78% within 45 interactions. Confirmation bias is the main failure; thinking models do better. [d07]
- FalsifyBench, 12 LLMs: GPT-5.2-Chat 75%, GPT-OSS-120B 68%, DeepSeek-V3.1 41%, other instruction-tuned 33-35%, GPT-5-Nano 12%, Qwen3.5-9B 21%. Confirmation ratios 27.3% and 39.0% for the best versus 66-82%. Oracle agreement 85-95%. [d09]
- This is the nearest model-level analogue of Lawson. It does not compare "solution first" with "constraints first" at equal tokens. That comparison remains unrun. [d07, d09, critique gap 1]

### 6.3 Fixation in LLMs
- GPT-4o chair text: 67.4% unique terms vs 78.2% for Red Dot entries; 142.71 vs 208.57 structure keywords per 100 cases; seat 45.83 vs 66.67 and leg 10.42 vs 46.67; four fixation patterns named (descriptive statements, repetitive theme, limited context variation, high-frequency word susceptibility). Midjourney images clustered more (pairwise distance 16.0503 vs 16.2509, p=0.0238). Baselines differ (finished award entries vs participant-AI outputs). [b23, c14-c16]
- Hackathon: ChatGPT-4 listed five working principles but built the three common ones; dropped pneumatic after one setback; fixated on the last item in a prompt list; added unnecessary complexity; lost continuity. Ranked second of six. [c06-c09, b25, b26]
- Prompt hygiene: replacing the list with a general description removed the last-item effect (qualitative). [c09]

### 6.4 LLMs as design partners and judges
- Reframing: no benefit (N=280). [a24]
- Collaborative software design, 18 pairs: teams rarely accepted output as is; they treated it as a straw man. A second analysis found creativity in 13 of 18 documents, credited mostly to humans, and no case of the LLM reshaping the problem space (ChatGPT 3.5 Turbo). [a26, d13]
- Students using LLM agents moved to a prompt-evaluate-refine loop; cognitive load shifted to scoping and evaluation (40 students, 8 teams, qualitative). [a27]
- UX designers beat GPT-4o on reasoning soundness (about .42-.45 vs .298); GPT-4o coverage narrower; the summary itself flagged number inconsistencies. [c24, c25]
- LLM judges are generous (GPT-4 used 5 often), moderately aligned (Pearson .556 with experts), blind to context. [c19, d14, d15]

### 6.5 What changed it, by how much
- Style prompt: moves transition shares by about 20 percentage points (SS 29.4 vs 9.9). [c02]
- Counterexample prompt: +14 points average discovery (42 to 56). [d07]
- Reasoning mode: 68-75% vs 33-41% on FalsifyBench. [d09]
- Carry-over on restart: +5 points (71.8 vs 66.8). [d11]
- Showing a planted AI example: fixation +.32 (log-odds). [c11]

### 6.6 Limits of this LLM evidence
All design studies use GPT-4, GPT-4o, ChatGPT 3.5 or Midjourney (2024-25). No study of 2025-26 frontier reasoning models on design fixation or co-evolution was found. [d16, K24] Rule-game studies do include newer models but use number triples or word categories, not design.

---

## 7. What our agent should take

Schema part: G guardrail, S state, O operator, M memory. Status: [E], [S], [C]. Evidence ids in brackets.

### Add now (established)

1. **Treat the first conjecture as a probe and test it with something that tries to break it.** Part: S3/S4 plus G3 (a pass must be on something the answer was not fitted to), O (discriminating test). [E] Evidence: a01, b01, d07, d08, d09. Action: after an early candidate, code asks for the test input most likely to falsify it. This largely matches S7's "look for a counterexample" but moves it earlier, into the probe stage. Note: the effect size of doing this early versus late is not known; add as the rule that a conjecture is never accepted on confirming tests.
2. **Do not feed the agent's own first conjecture back as an example to later attempts.** Part: S3 (fresh contexts) and G4. [E] Evidence: b14, b15, b17, c11, c13. Fixation by examples is replicated in humans, including professionals. The schema already uses fresh contexts; keep it.
3. **Allow a second, independent design after a failed check instead of only patching the first.** Part: S5/S6. [E] on human cost of attachment: b14, b16, b17. The size of benefit on LLM tasks is not known; see test U3. Do not make restart the default.
4. **A style prompt is a scaffold, not a trait; log the mode of each attempt.** Part: S0/S9 (logging only). [E] that the style is learned (K02: b02, a02, a03); [S] that LLMs follow style prompts (c05). Logging costs nothing. A cheap per-run log: P-S index or a "restated brief is relational or object-based" tag (a05).

### Test first

| # | Item | Part | Status | Evidence |
|---|---|---|---|---|
| T1 | Candidate-first then derive constraints from failures vs constraints-first, on hidden-rule items | S2/S3 | [S] | K01, K20; a01, d07, d09 |
| T2 | Problem-first vs solution-first prompt by problem class, scored for quality and for diversity | S0/S1 | [C] | K03, K19; b06, d02, b07 |
| T3 | Forced alternation of problem and solution steps | S2/O8 | [S] | K12, K24; c03, d13 |
| T4 | Persist k tries then restart with carry-over, parked-idea note, return path | S6, M | [S] | K11, K22; c08, d11, d12 |
| T5 | Schema memory plus case memory, similarity-gated | M | [S] | K06, K21; b10, d10 |
| T6 | Prompt hygiene: no single salient last option in lists | G/S1 | [S] | K11; c09 |
| T7 | Sample diversity operator vs plain resampling | O | [S] | K10; b23, c15 |
| T8 | Calibrated judge as stop rule | G | [S] | K15, K23; c19, d14, d15 |
| T9 | Stored guiding-principle line per task class | M | [S] | K04; a09, a10 |
| T10 | Structured reframing vs free generation | O8 | [C] | K13; a24 |
| T11 | Reasoning-step scoring besides final answer | G | [S] | K16; c24, c25 |
| T12 | Cap on problem-information gathering with forced move to conjecture | S1 | [S] | a06, b04 |

Notes on a few:
- T1 is the direct replication of Lawson on a model. It is gap 1 in critique.md and has not been done.
- T2 reflects the contested result. Measure both correctness and diversity because solution-driven designers scored higher on creativity in Kruger and Cross. [d02]
- T4: note O8 in the schema is "Reframe the goal"; this test leaves O8 alone and targets the S6 pivot rule.
- Items we recommend against adding: a fixed phase order (K07, b11); "always scope breadth-first" (b09, d04); multi-agent ideation loops (G9, c22); and LLM reframing as a shipped operator before T10 (a24; already marked [S] in SCHEMA O8).

---

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens, same model, same items, fixed seeds; report with a paired test and a confidence interval, not point values. Setup cost is counted (G7).

| ID | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Hidden-rule puzzles (Lawson blocks style, 2-4-6 style, ARC-like rules) with a cheap oracle | A: write candidate first, then must propose one test aimed at breaking it; B: list constraints first, then candidate; C: plain | Success within 45 turns; confirming-test share | A over B by 5 to 15 points if the falsify rule is the driver; ties if tokens are spent mostly on setup |
| B2 (T2) | Open design briefs with rubrics, two sets: well-defined (spec with checks) and ill-defined | Problem-first, solution-first, plain | Blind rubric score for fit; unique-term share or embedding spread for diversity | Solution-first higher diversity, lower fit; direction reverses on well-defined briefs if Cross is right |
| B3 (T3) | Briefs where first-pass constraints are incomplete | Free CoT vs program-forced P-S-P-S turns (4 turns) | Design integrity rating; PS and SP transition counts | Higher integrity with forced alternation; if no gain, drop |
| B4 (T4) | Multi-try engineering or code tasks with a pass check | No pivot; free pivot; persist k=2 then restart cold; persist k=2 then restart with note | Final pass rate; return rate to parked ideas | Carry-over beats cold by about 3 to 5 points (a priori from d11); free pivot not better than no pivot |
| B5 (T5) | Near and far task pairs with memory | Case memory; schema memory; hybrid gated by similarity | Forward transfer (far), same-task success (near) | Schema wins far, cases win near; hybrid matches both |
| B6 (T6) | Prompts that list options | List with salient last item vs rotated order vs summary description | Share of outputs that copy the last item | Rotation or summary cuts the last-item copy |
| B7 (T7) | One prompt sampled N times | Plain resampling vs diversity operator | Unique-term share; mean pairwise embedding distance | Operator raises spread; check correctness not lost |
| B8 (T8) | Held-out expert-rated design briefs | Judge uncalibrated; judge calibrated on expert ratings; human | Stop-rule precision on held-out | Calibrated judge reaches agreement above r = 0.7 before use as stop rule |
| B9 (T9) | Task classes with repeated items | With stored one-line frame vs without | Pass rate and steps to pass | Fewer steps with frame on familiar classes; none on novel classes |
| B10 (T10) | Ill-defined briefs | Structured reframing vs free generation | Blind expert-rated frame novelty and usefulness | Null or small, based on a24 |
| B11 (T12) | Briefs with a large information pool | Open retrieval vs cap plus early priority list | Quality; tokens spent on retrieval | Cap helps weak models; null for strong ones |

All items: also run a "novice vs expert" cut, i.e. weaker vs stronger model, to see whether the effect depends on skill (as with freshmen vs seniors in Atman [a07]).

---

## 9. What does not transfer, and why

- **Years of experience.** Human expertise takes ten or more years and shapes reasoning through memory chunks. [b20] A prompt does not create that. The first-year result says style is learned. [b02]
- **Lawson's rewarded probing.** In the block task a refusal is cheap and exact. Where the check is expensive, absent or noisy, early guesses teach little. [b01]
- **Human fixation costs and training effects.** Engineers and industrial designers differ by education. [b15] An LLM's failure mode is set by the prompt and training, so human fixation rates cannot be copied. LLMs fixate in other ways (last-item effect). [c09]
- **Think-aloud protocols.** LLM reasoning text is not a record of how it decided (G10). Bruggeman argues for auditing reasoning traces; G10 argues we should not rely on them as evidence. These conflict and are settled in favour of G10 for decisions; trace scoring is a research test only (T11). [c25]
- **Small-N effects.** Many numbers come from N of 2 to 16. They are priors, not effects. [critique, K25]
- **Social and team effects.** Team timing (early alternatives then clarification) is a social process. [a19]
- **Sketching and visual fixation.** The AI-image study used sketches, an example avatar and students. [b24, c11]
- **Quiz-measured expertise.** The reframing study's "expert" is a short quiz, not years. [a24]
- **Human creativity ratings of finished products.** LLM judges miss context. [d14]
- **Hackathon with human hands.** The Ege team had humans executing and one run. [c06]

---

## 10. Open questions

1. Does candidate-first beat constraints-first for an LLM at equal tokens on hidden-rule tasks? Unrun. (K01, K20.)
2. What are the actual group sizes, scores and significance in Lawson (1979) and any later professional follow-up? Not found. (b01, d06.)
3. How large is the Kruger and Cross quality gap, and does it hold for ill-defined briefs? N = 9; effects not seen. (d01, d02.)
4. Do 2025-26 reasoning models fixate on examples, and do they reframe unprompted? No study. (K24.)
5. Does problem definedness moderate which order works? Never manipulated. (a29, d05.)
6. Does a persist-k-then-restart rule fix Ege's early abandonment? No replication of Ege et al. (K11, K22.)
7. Does forced alternation raise integrity? Untested. (K12.)
8. Are there human expert-novice samples of 30 or more per group? None found. Atman's counts unverified. (d17.)
9. Can a calibrated LLM judge serve as a stop rule? No study. (d15.)
10. Which of education, specific experience and idiosyncrasy sets the style? No longitudinal study. (a03.)
11. Does the style prompt effect (Zhang et al.) replicate on another model family and with real expert raters? (c01.)
12. Is the first-year "null" a true null or a floor effect from low skill? (b02.)

---

## 11. Sources

[V] = opened and read this session (full text or substantive page). [M] = snippet, abstract or second-hand only.

**Human studies and reviews**
- [V] Cross (2001/2004) Design cognition: results from protocol and other empirical studies of design activity. https://chunk.cc.gatech.edu/AY2013/cs7601_spring/papers/Cross-DesignCognition.pdf (a02, a04, a06-a14, a29, b03-b05, b12-b19, d06)
- [V] Lawson (1979), as retold in How Designers Think (Part 28 PDF). https://uop.edu.jo/PDF%20File/petra%20university%20%5BArchitecture_Ebook%5D_How_Designers_Think_-_The_Design_Process_Demystified-20603-Part28.pdf (b01, b02)
- [M] Lawson (1979) Cognitive strategies in architectural design, Ergonomics 22(1):59-68. Original not opened (a01 URL was a Wikipedia mirror).
- [V] Restrepo and Christiaans (2004) Problem structuring and information access in design. https://www.creativityandcognition.com/cc_conferences/cc03Design/papers/25RestrepoDTRS6.pdf (a03, a05)
- [V] Kavakli and Gero (2001) Strategic knowledge differences between an expert and a novice designer. https://researchoutput.csu.edu.au/en/publications/6d91e394-ebf1-419f-8bc0-7812d68a32d6 (abstract page; a15)
- [M] Kavakli and Gero (2002) The structure of concurrent cognitive actions. https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/The-structure-of-concurrent-cognitive-actions/991022156304504721 (a16)
- [M] Atman et al. (2007) Engineering design processes: students and expert practitioners. https://discovery.fiu.edu/display/pub199304 (a17, d17)
- [V] Purzer et al. (2008) Comparing design problem solving processes of product design and engineering student teams. https://peer.asee.org/4003.pdf (a18, a19)
- [V] Morozov, Kilgore, Atman (2007) Breadth in design problem scoping. https://peer.asee.org/2318.pdf (a20, b08, b09)
- [V] Atman, Turns, Cardella, Adams (2003) The design processes of engineering educators. https://www.creativityandcognition.com/cc_conferences/cc03Design/papers/32AtmanDTRS6.pdf (a21)
- [V] Ball, Ormerod, Morley (2004) Spontaneous analogising in engineering design. https://www.creativityandcognition.com/cc_conferences/cc03Design/papers/21BallDTRS6.pdf (b10)
- [V] Chen, Chen, Yang (2022) Behaviors of novice and expert designers. https://ijdesign.org/index.php/IJDesign/article/download/4194/998 (b11)
- [V] Lemons, Carberry, Swan (2011) Cognitive styles and design strategies of engineering students. https://peer.asee.org/50031.pdf (b07, d01; also second-hand for b21, b06)
- [M] Kruger and Cross (2006) Solution driven versus problem driven design. https://oro.open.ac.uk/7423 (b06, d02)
- [M] Mehalik and Schunn (2006) What constitutes good design? Via Lemons (b21)
- [V] Crismond and Adams (2012) The Informed Design Teaching and Learning Matrix. https://d-miller.github.io/DRK12/topic1/8857.pdf (b20)
- [V] Studer, Daly, McKilligan, Seifert (2018) Evidence of problem exploration in creative designs. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/89D7CE966A59A6690A7EEBD98A4F10C9/S0890060418000124a.pdf/div-class-title-evidence-of-problem-exploration-in-creative-designs-div.pdf (d03, d04)
- [V] Ball and Christensen (2019) Advancing an understanding of design cognition and design metacognition. https://clok.uclan.ac.uk/31276/1/31276%20Ball%20%20Christensen%20-%20Design%20Studies%202019.pdf (d05)
- [V] Perisic, Martinec, Storga, Gero (2019) A computational study of the effect of experience. https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9F4ECEF387AB15A15A6C83F76F546D34/S2220434219000040a.pdf/a-computational-study-of-the-effect-of-experience-on-problemsolution-space-exploration-in-teams.pdf (a22, a23)
- [V] Zhang and Ma (2021) Designing in complexity: how solution conjectures inform problem exploration. https://cambridge.org/core/services/aop-cambridge-core/content/view/EE9CDFC61D0A74662655502BF2C66DCF/S2732527X21001152a.pdf/designing-in-complexity-how-solution-conjectures-inform-problem-exploration.pdf (b22)
- [M] Dorst and Cross (2001) Creativity in the design process: co-evolution. https://doi.org/10.1016/S0142-694X(01)00009-6 (c28; recalled)
- [M] Maher and Tang (2003) Co-evolution as a computational and cognitive model of design. https://ir.lib.nycu.edu.tw/handle/11536/28133 (c29)
- [M] Jiang, Gero, Yen (2014) Exploring designers' cognitive style via FBS-coded protocols. https://doi.org/10.1007/978-94-017-9112-0_6 (c30)
- [M] Others known only through Cross: Lloyd and Scott 1994/95, Christiaans and Dorst 1992, Atman et al. 1999, Jansson and Smith 1991, Purcell and Gero, Smith and Tjandra 1998, Akin and Lin 1995, Akin and Akin 1996, Valkenburg and Dorst 1998, Guindon 1990, Ball and Ormerod 1995, Rowe, Ullman.

**LLM and AI studies**
- [V] Shin et al. (2025) No evidence for LLMs being useful in problem reframing. https://arxiv.org/pdf/2503.01631 (a24)
- [V] Guo, Yin, Sun, Chen (2024) Empirical study of problem-solution co-evolution in human-GAI collaboration, DRS2024. https://research.gold.ac.uk/37955/1/Empirical%20Study%20of%20Problem-solution%20Co-evolution%20in%20Human-GAI%20Col.pdf (a25, c26; critique corrects the author attribution)
- [V] Jackson, Cha, Prikladnicki, van der Hoek (2026) The role of LLMs in collaborative software design. https://arxiv.org/pdf/2604.09120 (a26)
- [V] Gong et al. (2026) How LLM-based agents shape engineering design thinking. https://nemo.asee.org/public/conferences/374/papers/51241/download (a27)
- [V] Lim, Choi, Hong (2024) Identify design problems through questioning. https://arxiv.org/pdf/2409.07178 (a28)
- [V] Chen et al. (2025) Understanding design fixation in generative AI. https://arxiv.org/html/2502.05870v1 and https://arxiv.org/pdf/2502.05870 (b23, c14-c16, d16)
- [V] Wadinambiarachchi et al. (2024) The effects of generative AI on design fixation and divergent thinking. https://arxiv.org/pdf/2403.11164 (b24, c11-c13)
- [V] Ege et al. (2025) ChatGPT as an inventor. https://arxiv.org/abs/2404.18479 (c06-c10, b25, b26)
- [V] Krajcer et al. (2026) ChatGPT in ideation for UX design students. https://repository.tudelft.nl/record/uuid:8407da06-3dfe-4e6f-a11e-cace8da53a6b (b27; abstract only)
- [V] Zhang et al. (2025) Leveraging LLMs to emulate the design processes of different cognitive styles. https://openaccess-api.cms-conferences.org/articles/download/978-1-964867-39-7_12 (c01-c05)
- [V] Lim et al. (2025) Feed-O-Meter. https://arxiv.org/abs/2509.07424 (c17, c18)
- [V] Shaer et al. (2024) AI-augmented brainwriting. https://arxiv.org/abs/2402.14978 (c19-c21)
- [V] Sankar et al. (2026) Progressive ideation using an agentic AI framework (MIDAS). https://arxiv.org/abs/2601.00475 (c22, c23)
- [V] Bruggeman et al. (2025) Probabilistic methods for evaluating human and LLMs during design problem-solving. https://doi.org/10.1017/pds.2025.10279 (c24, c25; read through a summary fetch, the summary flagged inconsistencies)
- [V] Panda (2025) A framework for LLM-powered design assistants. https://arxiv.org/abs/2502.07698 (c27)
- [V] Jhaveri, GX-Chen, Sucholutsky, Choi (2026) Failing to falsify. https://arxiv.org/pdf/2604.02485 (d07, d08)
- [V] Bertolazzi, Tentori, Bernardi (2026) FalsifyBench. https://arxiv.org/pdf/2606.04751 (d09)
- [V] Hu, Long, Wang (2026) When continual learning moves to memory. https://arxiv.org/pdf/2604.27003 (d10)
- [V] Wang et al. (2026) Fail-Fast, Restart-Smart. https://arxiv.org/pdf/2608.03222 (d11)
- [V] TraceML (2026) What auto-research agents miss in long-horizon ML development. https://arxiv.org/pdf/2608.26086 (d12)
- [V] Jackson, Liebel, Prikladnicki, van der Hoek (2026) Exploring creativity in human-human-LLM collaborative software design. https://arxiv.org/pdf/2604.24373 (d13)
- [V] Lyu, Kim, Xiao, Luan (2026) Why LLMs and humans converge and diverge in evaluating creativity. https://arxiv.org/pdf/2607.22218 (d14)
- [V] Creativity Benchmark (2025). https://arxiv.org/pdf/2509.09702 (d15)

**Reading notes.** The critique found two points to read alongside the evidence lines: a20 gives per-expert ranges, so use b09 for group mix; a24's "about 2 frames in 23.25 minutes" is for the manual condition only, and novices felt lower agency with LLMs even though overall agency did not drop. The Wadinambiarachchi fixation CI upper bound is .54 in one place and .55 in another in the paper; immaterial.
