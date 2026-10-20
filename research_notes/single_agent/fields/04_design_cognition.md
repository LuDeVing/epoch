# Design cognition: what it offers one thinking agent

*2026-10-20. Marks: [V] checked this session by search or fetch (often the abstract or a secondary summary, not the full paper); [M] from memory, re-check numbers. Where a [V] only covers the abstract, I say so.*

## 1. What the field studies

Design cognition studies how designers think on ill-defined problems: problems with no single right answer, where the goal itself is unclear at the start. Methods are mostly protocol studies. A designer thinks aloud while working, and researchers code the transcript into moves (gather information, frame the problem, propose a solution, evaluate). Schon described the designer as a reflective practitioner who "talks" with the situation and listens to its "back talk". Dorst and Cross showed that problem and solution are built together, each reshaping the other. Cross summarised designerly ways of knowing: solution-first conjecture, framing the problem to make it tractable, and sketching as a thinking tool.

For us the field is a source for the open-ended and under-specified side of the router (diverge mode, reframing), and a warning about when framing work is wasted on well-posed problems.

## 2. Core findings

**F1. Problem and solution co-evolve (moderate; nine-designer protocol study).**
Dorst and Cross 2001 analysed protocols of nine experienced industrial designers on one task, rated the designs, and found the co-evolution model generally holds. Creative moments were tied to a bridge: a partial idea that fits both a refined problem frame and a partial solution. They add "default" and "surprise" problem and solution spaces. [V] (abstract and summary pages). Small sample, one task. Later critics say the model is read too loosely and propose mapping the problem space before solutions (Kokotovich, IASDR 2015) [V].

**F2. Strategy differs by designer, and no strategy wins alone (moderate-weak).**
Kruger and Cross 2006 found four strategies in nine designers: problem-driven, solution-driven, information-driven, knowledge-driven. Strategy was not simply related to solution quality. Solution-driven did not lose. [V] (abstract). Lesson: "always analyse the problem first" is not supported.

**F3. Experts frame; novices rush to solutions (moderate, from reviews).**
Reviews report novices spend about half as long scoping the problem as experts and jump to solutions. Cross describes expert designers as actively imposing a frame and steering search, rather than analysing the whole problem exhaustively. [V] (secondary summaries only, original numbers not checked). Cross 2004 "Expertise in design: an overview" is the usual source [M].

**F4. Reflection and attention to back talk mark better student designers (moderate-weak).**
Adams, Turns and Atman 2003 coded verbal protocols of engineering students using Schon's theory. Measures were problem setting and listening to back talk, and seniors were more reflective than freshmen. [V] for the framework and measures; the effect sizes are not checked. Atman et al. 2007 (Journal of Engineering Education 96(4)) compare students and expert practitioners; I know the title and venue [V], the finding that experts spend more time on problem scoping and gather more information is [M]. Also: problem understanding and information gathering depend on each other, so neither can finish first [V].

**F5. Structuring recurs through the whole task (weak-moderate).**
A software-design paper citing Goel and Pirolli reports that "problem structuring" dominates early but returns periodically. [V] (secondary). This says reframing is a recurring event, not a phase.

**F6. Fixation is real and driven by examples (strong as a phenomenon, effect sizes unchecked).**
Jansson and Smith 1991: designers shown an example copy its flaws and narrow their search. [V] for the definition and source. Sio, Kotovsky and Cagan 2015 review it; this is a literature review, not a meta-analysis [V]. Mitigations are mixed: some analogy and example-handling "nonintuitive findings" exist [V title only]. A definitional debate says fixation is not one thing: unconscious adherence, conscious block, intentional resistance [V].

**F7. Primary generator (weak, mostly theory).**
Darke 1979 (Lawson reports it): architects pick an early simple idea, the primary generator, from a few known values, then test it against the problem and revise. [M]. Evidence is a small interview study. It gives a pattern, "conjecture early, then test", close to our "trust first answer until a check fails".

**F8. Reflection-in-action vs on-action (theory, no controlled evidence found).**
Schon's two modes are an essay-level framework. I found no controlled study of them. Treat as design inspiration. [M]

## 3. Mechanisms an agent can run

**M1. Frame-before-solve, only for open problems.**
- Trigger: router says "no objective check, open answer" (diverge route), or the probe shows attempts disagree on what the task even asks.
- Action: write 2 to 3 frames of the problem in one line each ("this is really about X"). Pick the one whose frame yields a concrete solution test. Keep the original wording (principle 4).
- Check: equal tokens vs plain on NoveltyBench and architecture search; count distinct answers and utility. Compare with diverge-only (no frames).
- Evidence: F2, F3; the CHI 2025 null result (section 4) warns this alone may not help.
- Risk: on single-answer tasks, framing cost matches our BrainTeaser loss. Never run it on converge routes.

**M2. Bridge step (co-evolution cycle) with a cap.**
- Trigger: diverge route, after the first set of candidate ideas; or at an escalate-ladder impasse (rung 3, re-read).
- Action: for each of the top 2 candidates write "what this solution assumes the problem is". If two candidates assume different problems, restate the problem so that the better parts of both are covered, then generate one new candidate for the new statement. Maximum 2 cycles.
- Check: does the restated problem produce a candidate that beats the earlier best on the evaluator or the training run? Log how often the cycle changed the winner. Arm: with vs without the cycle at equal tokens.
- Evidence: F1 (moderate, nine designers).
- Risk: extra calls; endless re-spec. The cap and "stop if the winner does not change" guard this.

**M3. Primary generator with test (the convergent form of F7).**
- Trigger: converge and revise routes.
- Action: write the single simplest guiding idea first, state what it predicts on the examples or tests, run the check, and only reframe if the check fails. This is what our step 4 already says.
- Check: reframe-on-failure vs reframe-on-schedule, equal tokens, on ARC and BrainTeaser. The gate is not losing to plain.
- Evidence: F7 (weak) plus our own data.
- Risk: weak external evidence. Mostly a name for what we already do.

**M4. Reframe trigger = back talk from the check, not a timer.**
- Trigger: a real check output exists (test fails, example mismatch, evaluator score low) and two revisions did not fix it.
- Action: the agent writes "what the failing output says about my frame" (one sentence about the frame, not the code), then picks one of three reframings: change representation, relax a constraint, swap which part is the goal. Then the escalation ladder continues.
- Check: pass rate after the reframe step against more plain resamples, equal tokens.
- Evidence: F4 (listening to back talk is the measured reflective behaviour); consistent with Xu et al. 2026 (section 4).
- Risk: the model may write plausible but empty reflections. Require the reflection to cite a concrete output line.

**M5. Anti-fixation: de-anchor from examples.**
- Trigger: diverge route, whenever the prompt or memory supplies an example answer or a lesson from earlier.
- Action: generate before reading examples or lessons; or list which features of the example are essential and which are accidental, then generate a candidate that drops one accidental feature.
- Check: distinct answers and share of candidates that copy a prior example's flaws; at equal tokens.
- Evidence: F6 (strong as a phenomenon in humans), plus LLM fixation reported by Xu et al. [V].
- Risk: it can conflict with the look-back memory (lessons are examples). Test lessons shown after first generation vs before.

**M6. External co-regulator call.**
- Trigger: diverge or long revise loops, every 2 to 3 steps.
- Action: a separate call, same model, reads the trace and answers only: "Is the agent stuck on one paradigm? Name an unexplored region." Its output feeds the next step.
- Check: design quality vs a self-monitoring prompt and vs plain loop, equal tokens.
- Evidence: Xu, Martelaro, McComb 2026: external agent beat self-monitoring, which beat the plain loop, at similar cost, on one battery-pack problem [V abstract].
- Risk: one task, preprint. Overlaps with our forced-doubt that hurt on puzzles. Run only on open routes.

**M7. Stop signal: "good enough" frame test.**
- Trigger: any route.
- Action: before reframing, ask whether the current frame already yields a passing or agreeing answer. If yes, stop. This guards against the F3 over-reading ("experts always reframe").
- Check: share of runs where reframing was skipped, and accuracy against always-reframe.
- Evidence: our data; F2.
- Risk: none beyond a small prompt cost.

## 4. Evidence on LLMs and AI agents

- **Shin et al., CHI 2025, "No Evidence for LLMs Being Useful in Problem Reframing" (arXiv 2503.01631).** 280 participants, three ways of using LLMs. LLM use did not improve problem frame quality, widened the gap between experienced and inexperienced designers, and lowered perceived agency for novices. [V] (search summary of abstract). This is the most direct and the most negative result. It is about humans using LLMs, not an LLM framing alone.
- **Xu, Martelaro, McComb 2026, arXiv 2603.24768.** LLM design agents fixate; self-regulation and external co-regulation loops beat a plain loop on a battery pack design problem without much more compute; co-regulation beat self-regulation. They note reflection that is poorly regulated can itself cause fixation. [V] (abstract). One problem, preprint.
- **Wang et al., arXiv 2511.15331.** 20 designers; curated reasoning improved design quality and creativity. [V] (search summary only; I did not read the paper, so what "curated" means is unchecked).
- **Zhang et al., AHFE 2025.** Zero-shot chain-of-thought prompting led an LLM to mimic problem-driven vs solution-driven styles. It matched human styles in broad terms but failed at nonlinear problem-solution switching. [V] (summary). Small, conference paper.
- **ICCC 2026 paper 78.** Seven students rated 27 LLM answers under three prompting strategies for reframing. A first step, not a test. [V] (summary).
- **Bruggeman et al. 2025 (Cambridge).** Proposes soundness and completeness for scoring design reasoning, human or LLM led. [V] (summary). Possibly useful as a scoring idea.
- **Giota et al. 2026.** Prompt-Reflection-Reframe loop for bias; validated by scenarios only. [V] (summary). Weak.

Reading: the only controlled gains for agents come from external regulation against fixation (M6). The only large controlled test of LLM reframing is null. No study I found tests Dorst-Cross co-evolution as a procedure inside an LLM at equal tokens.

## 5. What does not transfer, and where it could hurt

- **Embodied sketching.** Sketches "talk back" because the drawing shows unplanned relations. A model's text has no such surprise unless a tool executes it (code run, simulation, training run). Back talk must come from real outputs (consistent with plan principle 3).
- **Tacit expertise and years of practice.** Expert reframing rests on a store of past cases. The model's prior knowledge is not the same and cannot be "grown" in one call. The look-back memory is the nearest substitute, and it is untested.
- **Traits and motivation.** Tolerance of ambiguity, taste, commitment. Not transferable.
- **Human protocol quirks.** Think-aloud changes human thought; a model's written reasoning may not reflect what it does inside.
- **Could make the agent worse.** (a) Framing on a well-posed puzzle: our BrainTeaser and ARC results say any forced non-converging move costs accuracy. (b) Reflection with no external signal can degrade answers (Huang et al. 2023, plan principle 3). (c) CHI 2025 null result: LLM-generated frames did not improve frame quality. (d) Cycles eat budget; the 0% full-scaffold run shows the cost. (e) Reading designers' "problem-driven vs solution-driven" as a rule: Kruger and Cross found neither wins.

## 6. Open questions

- Does an explicit frame step beat plain diverge on NoveltyBench at equal tokens, or does the diverge cards already do the same work?
- Is the bridge cycle (M2) worth its calls, measured by how often it changes the winner?
- Does an external regulator call (M6) generalise past one engineering task, and does it help or hurt on puzzles?
- Do lessons from memory cause fixation (M5)? Show before or after first generation.
- Can a router detect "ill-defined vs well-posed" cheaply? Probe disagreement on the problem statement (not the answer) is a candidate signal.
- Protocol analysis of the agent's own traces: code moves (frame, solve, evaluate) and compare to expert coding. Cheap and could reveal novice-like rushing.

## 7. References

1. Dorst, K. and Cross, N. (2001). Creativity in the design process: co-evolution of problem-solution. Design Studies 22(5), 425-437. https://doi.org/10.1016/S0142-694X(01)00009-6 [V]
2. Kruger, C. and Cross, N. (2006). Solution driven versus problem driven design: strategies and outcomes. Design Studies 27(5), 527-548. https://oro.open.ac.uk/7423 [V]
3. Adams, R., Turns, J., Atman, C. (2003). Educating effective engineering designers: the role of reflective practice. Design Studies 24(3), 275-294. [V bibliographic; findings via a review at https://cpree.uw.edu/?p=1442]
4. Atman, C. et al. (2007). Engineering design processes: a comparison of students and expert practitioners. J. Engineering Education 96(4), 359-379. [V title only; findings M]
5. Jansson, D. and Smith, S. (1991). Design fixation. Design Studies 12(1), 3-11. [V]
6. Sio, U., Kotovsky, K., Cagan, J. (2015). Fixation or inspiration? A meta-analytic review of the role of examples on design processes. Design Studies 39. [V that it is a review of findings; "meta-analytic" in the title is M, and the search called it a review]
7. Kokotovich, V. (2015). IASDR paper on co-evolution interpretation. https://opus.lib.uts.edu.au/bitstream/10453/41435/1/IASDR2015%20Kokotovich%20Final%20Paper%20378%20.pdf [V]
8. Schon, D. (1983). The Reflective Practitioner. Basic Books. [M]
9. Cross, N. (2004). Expertise in design: an overview. Design Studies 25(5). [M]; Cross, N. (2006). Designerly Ways of Knowing. Springer. [M]
10. Darke, J. (1979). The primary generator and the design process. Design Studies 1(1). [M]; Lawson, B. (1980/2005). How Designers Think. [M]
11. Shin, J. et al. (2025). No Evidence for LLMs Being Useful in Problem Reframing. CHI 2025. https://arxiv.org/abs/2503.01631 [V] (author list not checked)
12. Xu, Z., Martelaro, N., McComb, C. (2026). Supervising Ralph Wiggum: Exploring a Metacognitive Co-Regulation Agentic AI Loop for Engineering Design. https://arxiv.org/abs/2603.24768 [V]
13. Wang et al. (2025). arXiv 2511.15331 (curated reasoning for designers). https://arxiv.org/pdf/2511.15331v2 [V summary only]
14. Zhang et al. (2025). Leveraging LLMs to emulate the design processes of different cognitive styles. AHFE 2025. https://openaccess.cms-conferences.org/publications/book/978-1-964867-39-7/article/978-1-964867-39-7_12 [V summary]
15. ICCC 2026 paper 78 (LLM reframing, 7 students). https://computationalcreativity.net/iccc26/papers/ICCC26_paper_78.pdf [V summary]
16. Bruggeman et al. (2025), Cambridge, probabilistic evaluation of design reasoning. https://www.cambridge.org/core/product/A4AEC038573F521DF5808BFFB6D9C67E/core-reader [V summary; author list as reported]
17. Huang et al. (2023). Large language models cannot self-correct reasoning yet. [M, cited in the plan]
