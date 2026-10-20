# Design cognition: what it offers one thinking agent

Evidence ids are in brackets. "Memory" means the line rests on recall or a search snippet, not an opened page. Where the CHECK lines (design-d-15 to d-21) disagree with the claims file, the CHECK lines are used.

## 1. What the field studies

Design cognition studies how designers think on ill-defined problems: how they frame the problem, how they move between problem and solution, how they get stuck on an example, and how experts differ from novices. Its classic work is protocol studies of a few designers [design-a-05, design-a-06, design-a-11]. Its newer work asks whether LLMs show the same traps and whether LLM help improves design thinking [design-a-03, design-a-04, design-b-04].

The field is thin on controlled tests. Most classic findings were not opened by any agent in this round. They rest on memory or snippets [design-a-05, design-a-06, design-a-07, design-a-10, design-a-11, design-a-12, design-d-01, design-d-05]. This brief therefore gives few "established" findings and many hypotheses.

Fit with our data: design tasks are open-ended. Our schema won on open tasks (NoveltyBench, architecture search) and lost on single-answer tasks (ARC, word puzzles). So most of what follows should run only on the open branch.

## 2. Established findings

Status "established" here means at least two sources agree and at least one was fetched. Several are only weakly established. The weakness is stated.

**E1. Intrinsic self-correction without an external signal often fails or hurts. It works when reliable external feedback exists.**
- Huang et al. 2023 tested self-correction on reasoning benchmarks and found it often fails and sometimes lowers performance [design-c-04].
- A critical survey found no prior work showing successful self-correction from feedback by a prompted LLM, except on tasks unusually suited to it. It found success when reliable external feedback exists [design-c-05].
- No pooled effect size was recorded.

**E2. More deliberation can lower accuracy on some tasks.**
- Chain of thought cut accuracy by up to 36.3 points absolute (o1-preview versus GPT-4o) in three of six tasks, and was mixed in the rest. This was a preprint [design-c-06].
- Making reasoning models think longer can lower accuracy. One failure mode is distraction by irrelevant information in Claude models [design-c-07].
- o1-like models spend large compute on simple problems for little gain. This was a preprint [design-c-08].
- The task families are not design tasks. They do match our puzzle losses.

**E3. AI idea access raises individual creativity but lowers diversity across people. Samples from one model resemble each other.**
- Writers with GenAI ideas wrote more creative individual stories, but the stories were more similar to each other [design-c-09].
- ChatGPT text for office chairs showed repetition, high-frequency words and lower novelty (67.4% versus 78.2% for human entries). This was a preprint with 10 designers and 96 GenAI solutions [design-b-04].
- GPT-4o outputs clustered mid-range while humans covered both obvious and highly latent needs. The authors call this exploratory and small [design-b-11].
- Together these support forced divergence on open tasks, which matches our NoveltyBench result.

**E4. LLMs and AI tools fixate on familiar solutions. Direction agrees, each source is weak.**
- An LLM design agent fixated on existing paradigms (preprint, one problem) [design-a-04, design-b-03, design-c-03].
- ChatGPT-4 in a 48-hour hackathon showed design fixation (preprint, one team) [design-b-07, design-d-14].
- A snippet-only report says an AI image generator raised human fixation on a first example and lowered originality and variety [design-b-12]. This concerns human users, not an agent.
- Treat E4 as a likely trend, not a measured effect.

**E5. Human design fixation from examples is real. Its size is not established.**
- A fetched review of 25 studies found wide differences in methods and results and called for more consistent methods [design-a-01, design-a-14]. No pooled effect size was found [design-a-14].
- The founding study (Jansson and Smith 1991) is memory only, credibility capped at 50 [design-a-07, design-d-17].
- Sio et al. 2015 is titled a meta-analytic review. The label is supported by the title. The effect sizes were not read [design-d-06, design-d-17, design-a-08].
- A short review concludes fixation risk can be limited by managing quantity, abstraction, proximity and method of examples. It was a snippet [design-d-07].
- Do not quote effect sizes from this field. Measure our own.

**E6. Less experienced users adopt AI output directly. Experienced designers assess it critically.**
- Chen 2025 (preprint, 10 people) found this [design-b-06]. Shin 2025 found LLM help widened the experienced-novice gap [design-a-03, design-b-02].
- Both concern human users. For an agent, the point is only that a model that takes its own first output has no critic unless a step supplies one [design-b-06].

## 3. Single-source and contested findings

### Single-source

**S1. LLM help did not improve problem-frame quality.**
- 280 participants, three LLM modes, CHI 2025, fetched [design-a-03, design-b-01, design-c-01]. It also widened the experienced-novice gap and lowered novices' agency [design-b-02, design-c-02].
- The three entries are one paper. It tests humans using an LLM, not an LLM framing alone. It is a reason to demand a test, not proof that an agent frame step fails [design-a-03].

**S2. External co-regulation of an LLM design agent beat self-regulation, which beat a plain loop, at similar compute.**
- One preprint, one battery-pack problem [design-a-04, design-b-03, design-c-03, design-d-13, design-d-21]. It is the only controlled LLM fixation-mitigation test found [design-d-13, design-d-21].

**S3. Analogy methods raised novelty. Novelty gain and fixation reduction are separate.**
- 97 experts: WordTree and SCAMPER raised novelty. WordTree reduced fixation, SCAMPER did not [design-a-02].

**S4. Problem and solution co-evolve (Dorst and Cross 2001).**
- Nine experienced designers, one task, protocol analysis. Creative moments came with a bridge that fits a refined frame and a partial solution [design-a-05, design-b-14, design-c-12, design-d-01].
- CHECK: the paper and abstract exist and the model is widely cited. Effect sizes, replications and any LLM test were not verified. It remains a hypothesis [design-d-15].
- A 2026 scoping review of 16 DRS papers says the model is widely used and also critiqued, but its abstract does not say how [design-d-03]. The critique by Kokotovich is unread [design-c-14].
- The review suggests keeping problem and solution records distinct and interdependent [design-d-04]. Dorst and Cross also propose default and surprise spaces [design-d-02].

**S5. No design strategy predicts better solutions (Kruger and Cross 2006).**
- CHECK: UNSETTLED. The citation is confirmed. The findings were not opened [design-d-05, design-d-16]. Earlier entries repeat the claim from memory [design-a-06, design-b-13, design-c-13].

**S6. Experts scope the problem longer and gather more information. Reflective attention to back talk rises with seniority.**
- Three memory-only papers from one research cluster, counted as one line [design-a-10, design-a-11, design-a-12]. Seniority is confounded with other skills.

**S7. Primary generator: designers adopt an early simple idea and test it.**
- Small 1979 interview study, memory only [design-a-13].

**S8. GPT-4o scored below human designer groups on latent-need elicitation.**
- About 0.30 versus 0.45 soundness; 5 designers per group; exploratory. Prompting with the human protocol's guidance raised explicit annotation use but gave the lowest variance and did not broaden ideas [design-b-10, design-b-11].

**S9. An LLM agent dropped promising ideas after minor difficulty.**
- One hackathon team, preprint [design-b-07, design-d-14].

**S10. Sycophancy can weaken a critic that reads the draft.**
- Sharma et al. 2023: assistants show sycophancy, and humans and preference models sometimes prefer sycophantic answers over correct ones. Preprint, not tested on design self-critique [design-c-11].

**S11. Written reasoning may not be what drives the answer.**
- Biasing features shift answers while the written reasoning omits them, and accuracy fell by up to 36 percent on BIG-Bench Hard [design-d-08].
- Models differ widely across tasks in how much they condition on written reasoning [design-d-09].
- CHECK: PARTLY. No direct test of problem-frame text was found [design-d-19].

**S12. LLM judges are unreliable for creativity.**
- Inconsistent verdicts under minor prompt changes and label bias [design-d-10]. Verbosity and leniency bias, with wide scales less stable; separating analysis from judging helps [design-d-11].
- CHECK: supported as a risk by two fetched preprints. No peer-reviewed meta-analysis was found [design-d-20]. A third paper, on translation, is a snippet [design-d-12].

### Contested

**C1. Prompting LLMs with problem-driven or solution-driven styles.**
- Zhang 2025 (conference paper, n not recorded) reports human-like static features and more novel, complete solutions than baselines, but not nonlinear problem-solution switching [design-b-08].
- The supporting items are weak. DesignerlyLoop is a human interface study where humans edited the reasoning [design-b-09, design-c-10]. The ICCC 2026 paper could not be read [design-b-15, design-c-16].
- Net: no solid evidence that a style prompt helps an agent. The one useful signal is that the model does not switch frames by itself in one pass [design-b-08].

**C2. Nominal-group effect (independent generation pooled beats interacting groups).**
- CHECK: UNSETTLED. No source was retrieved. Memory only [design-d-18].

## 4. Mechanisms an agent can run

All run only on the open branch (no objective check, open-ended answer) unless stated. Each must beat the plain model at equal tokens. No mechanism here has an LLM test at equal tokens on our tasks [design-a-15].

**M1. Reframe on failure, not on a timer.**
- Trigger: a real check fails (test, example mismatch, a run) or two attempts disagree on a checkable point.
- Action: write what the failure says about the problem, restate the frame in one or two sentences, retry once. Cap at two rounds.
- Check: with the same token budget, compare "revise from check output" against "retry plain" on items where the first attempt failed. Count items fixed.
- Evidence: [design-c-04, design-c-05, design-a-09, design-c-07].
- Risk: if the check is only the same model re-reading itself, E1 says it does not help [design-c-05]. On single-answer tasks, extra rounds can drop accuracy [design-c-06, design-c-07].

**M2. Gate by task type before any framing step.**
- Trigger: always, first, cheap.
- Action: a short router call (or the probe agreement) decides: single answer with a likely natural first answer, or open and ill-defined. Skip frame and divergence steps on the first kind.
- Check: run the gated schema and the ungated schema at equal tokens on a mixed set. Gating must recover the puzzle losses without losing the open-task gains.
- Evidence: [design-c-06, design-c-08, design-c-07].
- Risk: a wrong route on an open task loses the divergence gain. A wrong route on a puzzle repeats our ARC loss.

**M3. Forced divergence with a diversity metric.**
- Trigger: open branch.
- Action: several independent calls, each told to avoid the themes already listed; track repeated themes and high-frequency terms across candidates. Keep one call per candidate rather than one long interacting thread.
- Check: distinct answers and a non-LLM diversity measure at equal tokens against plain sampling. Our own result is 3.18 to 9.63 distinct.
- Evidence: [design-c-09, design-b-04, design-b-11, design-d-10]. The independent-call design is the testable form of the nominal-group claim [design-d-18].
- Risk: this is the schema that hurt on single-answer tasks, so it needs M2. Diverse is not good, so it needs an evaluator (M7). Copying expert steps into a prompt narrowed output in one study, so do not replace divergence with a fixed expert recipe [design-b-10].

**M4. Delayed exposure of examples and lessons.**
- Trigger: the agent has memory lessons or examples from earlier problems.
- Action: generate a first set of candidates without them, then show lessons. Vary abstraction and distance of the lessons.
- Check: lessons-before versus lessons-after the first generation, at equal tokens; measure copy-of-example rate and distinct answers.
- Evidence: [design-a-07, design-a-01, design-d-07, design-b-12]. All are weak for LLMs; the human effect is real but its size is unknown [design-a-14].
- Risk: on tasks where a lesson is the answer (a known trick), delaying it wastes tokens. This may clash with the lessons memory in the plan; no evidence either way.

**M5. Persistence rule.**
- Trigger: a candidate fails a check.
- Action: before dropping it, write the diagnosis of the failure. Drop only if the diagnosis says the idea itself is wrong, not the implementation.
- Check: compare final quality with and without the rule at equal tokens on build-and-test tasks (architecture search).
- Evidence: [design-b-07, design-d-14, design-a-13].
- Risk: one team, anecdotal. Persistence on a wrong idea burns tokens. Our ARC runs were fooled by a program that fit all examples, so persistence needs a verification step [design-d-14].

**M6. External stuck-check (separate-context co-regulator).**
- Trigger: every 2 to 3 steps on open routes, or when the last steps produce similar candidates.
- Action: a separate call sees the trace, not the author's framing, and answers one question: which region or paradigm is unexplored? It must name a specific gap.
- Check: against self-monitoring (same model, same context) and a plain loop, at equal tokens.
- Evidence: [design-a-04, design-b-03, design-c-03, design-d-13, design-d-21, design-c-11].
- Risk: single-source, one problem, preprint [design-d-21]. A critic reading the draft as the author's own tends to approve [design-c-11]. The monitor could add tokens with no gain on tasks without fixation.

**M7. Evaluator with bias controls.**
- Trigger: after divergence, to prune candidates.
- Action: write analysis of each candidate first, score on a narrow scale, compare in pairs with shuffled order, use several prompts, control for length, and add a non-LLM novelty measure such as embedding distance or count of distinct answers.
- Check: agreement of the evaluator with held-out outcomes (a training run, a test, human anchors). Compare a single LLM score against this procedure at equal tokens.
- Evidence: [design-d-10, design-d-11, design-d-12, design-d-20].
- Risk: all evidence is preprint. Without an objective pruner (as in architecture search), divergence adds noise [design-d-20].

**M8. Bridge cycle (experiment arm only).**
- Trigger: open branch, after M3, when two partial ideas each fit a different reading of the problem.
- Action: restate the problem so two partial ideas both fit, generate once more, cap at two cycles. Keep the frame record and the solution record separate [design-d-04].
- Check: with and without the bridge at equal tokens; report how often it changes the winner.
- Evidence: [design-a-05, design-d-01, design-d-02, design-d-15, design-b-08]. The model did not switch frames itself in one pass, so a program would supply the switch [design-b-08].
- Risk: one nine-person study, no LLM test [design-a-15, design-d-15]. Humans using an LLM did not frame better [design-a-03]. Do not build on this; test it.

**M9. Frame-swap control (diagnostic, not a step).**
- Trigger: during development only.
- Action: swap or corrupt the written frame and check whether the final answer moves.
- Check: if the answer does not move, the frame step is decoration, remove it.
- Evidence: [design-d-08, design-d-09, design-d-19].
- Risk: it costs extra calls, so use it on benchmarks, not in production runs.

## 5. Evidence on LLMs and AI agents

- Agents fixate. One preprint reports a design agent stuck on existing paradigms and helped by a separate monitor [design-a-04, design-d-13]. A hackathon LLM team showed fixation and dropped good ideas early [design-b-07, design-d-14]. Both are preprints with one case [design-d-21].
- Output is alike across samples and across people [design-c-09, design-b-04, design-b-11].
- Humans using an LLM did not frame problems better, and the gap between experienced and inexperienced widened [design-a-03, design-b-02].
- A style prompt gave more novel and complete outputs, but no nonlinear frame switching (conference paper, n not recorded) [design-b-08].
- Copying a human protocol's guidance into the prompt narrowed output and did not lift soundness above human groups [design-b-10].
- Self-critique with no external signal is unreliable [design-c-04, design-c-05]. Critics can be sycophantic [design-c-11].
- Longer thought can hurt [design-c-06, design-c-07, design-c-08]. Written reasoning may not drive the answer [design-d-08, design-d-09].
- LLM judges of creativity are biased toward length and leniency and are prompt-sensitive [design-d-10, design-d-11].
- No controlled test of a Dorst-Cross procedure inside an LLM at equal tokens was found. The search budget ran out, so this means not found [design-a-15].

## 6. What does not transfer to a model

- Years of practice. Expert-novice gaps are confounded by experience and tools [design-a-10, design-a-11, design-a-12]. A prompt cannot give a model decades of practice.
- Sketching and physical prototyping, where back talk comes from the drawing [design-a-09]. A model has no sketch. Its back talk must come from tests and runs [design-c-05].
- Sense of agency and trust. The agency finding is about human users [design-a-03, design-b-02].
- Human fixation size. Effect sizes are variable and may not apply to a model that fixates through its training distribution [design-a-14, design-b-04].
- Curated reasoning by a human. DesignerlyLoop's gain came from humans editing the reasoning, which a program-run schema lacks [design-c-10].
- "Analyse the problem first". The one study on strategies reported no simple link to quality, and it is unsettled [design-d-16, design-a-06].
- Reflection as a procedure. There is no controlled test, and it is an essay framework [design-a-09].

## 7. Open questions

1. Does an LLM frame step help at equal tokens on open tasks? The human study says no for humans [design-a-03]; the agent case is untested [design-a-15].
2. Does the model use its written frame? Run the frame-swap test [design-d-19].
3. How many options to generate and when to stop? No quantity-versus-quality evidence was collected.
4. How to score novelty and usefulness without a biased judge [design-d-20]?
5. Does independent pooled generation beat an interacting session for an LLM at equal tokens [design-d-18]?
6. Do lessons shown before versus after first generation change fixation [design-d-07]?
7. Do the memory-only classics (Dorst and Cross, Kruger and Cross, Jansson and Smith) hold up when opened? Kokotovich's critique is unread [design-c-14, design-d-15, design-d-16].
8. Can the co-regulation result replicate beyond one battery-pack problem [design-d-21]?
9. What do insight-problem studies of constraint relaxation say? Not searched; the critique ranks them closest to a reframing step.

## 8. References

1. Vasconcelos, L. A., Crilly, N. (2016). Inspiration and fixation: Questions, methods, findings, and challenges. Design Studies 42. https://www.repository.cam.ac.uk/handle/1810/252511. Checked: fetched. [design-a-01, design-a-14]
2. Moreno, D. P., Blessing, L. T., Yang, M. C., Hernandez, A. A., Wood, K. L. (2016). Overcoming design fixation: Design by analogy studies and nonintuitive findings. AI EDAM 30(2), 185-199. https://www.cambridge.org/core/journals/ai-edam/article/abs/overcoming-design-fixation-design-by-analogy-studies-and-nonintuitive-findings/038760839BBBEFC08F146457A77BBE51. Checked: fetched. [design-a-02]
3. Shin, J., Polyanskaya, A., Lucero, A., Oulasvirta, A. (2025). No Evidence for LLMs Being Useful in Problem Reframing. CHI 2025 (arXiv 2503.01631). https://arxiv.org/abs/2503.01631. Checked: fetched. [design-a-03, design-b-01, design-b-02, design-c-01, design-c-02]
4. Xu, Z., Martelaro, N., McComb, C. (2026). Supervising Ralph Wiggum: Exploring a Metacognitive Co-Regulation Agentic AI Loop for Engineering Design. arXiv 2603.24768 (preprint). https://arxiv.org/abs/2603.24768. Checked: fetched. [design-a-04, design-b-03, design-c-03, design-d-13, design-d-21]
5. Dorst, K., Cross, N. (2001). Creativity in the design process: co-evolution of problem-solution. Design Studies 22(5), 425-437. https://doi.org/10.1016/S0142-694X(01)00009-6 and https://oro.open.ac.uk/3278. Checked: memory and snippet (abstract via search summary; pages would not open). [design-a-05, design-b-14, design-c-12, design-d-01, design-d-02]
6. Kruger, C., Cross, N. (2006). Solution driven versus problem driven design: strategies and outcomes. Design Studies 27(5), 527-548. https://doi.org/10.1016/j.destud.2006.01.001. Checked: snippet (citation confirmed via Crossref; findings not opened). [design-a-06, design-b-13, design-c-13, design-d-05, design-d-16]
7. Jansson, D. G., Smith, S. M. (1991). Design fixation. Design Studies 12(1), 3-11. https://www.sciencedirect.com/science/article/pii/0142694X91900034. Checked: memory. [design-a-07, design-d-17]
8. Sio, U. N., Kotovsky, K., Cagan, J. (2015). Fixation or inspiration? A meta-analytic review of the role of examples on design processes. Design Studies 39. https://doi.org/10.1016/j.destud.2015.04.004. Checked: snippet (title and venue via Crossref; abstract not retrieved). [design-a-08, design-c-15, design-d-06, design-d-17]
9. Schon, D. A. (1983). The Reflective Practitioner. Basic Books. No URL. Checked: memory. [design-a-09]
10. Adams, R. S., Turns, J., Atman, C. J. (2003). Educating effective engineering designers: the role of reflective practice. Design Studies 24(3), 275-294. https://cpree.uw.edu/?p=1442. Checked: memory. [design-a-10]
11. Atman, C. J., Adams, R. S., Cardella, M. E., Turns, J., Mosborg, S., Saleem, J. (2007). Engineering design processes: a comparison of students and expert practitioners. Journal of Engineering Education 96(4), 359-379. No URL. Checked: memory. [design-a-11]
12. Cross, N. (2004). Expertise in design: an overview. Design Studies 25(5), 427-441. No URL. Checked: memory. [design-a-12]
13. Darke, J. (1979). The primary generator and the design process. Design Studies 1(1), 36-44. No URL. Checked: memory. [design-a-13]
14. Chen, L., Song, Y., Zheng, C., Jing, Q., Hansen, P., Sun, L. (2025). Understanding Design Fixation in Generative AI. arXiv 2502.05870 (preprint). https://arxiv.org/abs/2502.05870. Checked: fetched. [design-b-04, design-b-05, design-b-06]
15. Ege, D. N., Ovrebo, H., Stubberud, V., Berg, M., Elverum, C., Steinert, M., Vestad, H. (2024). ChatGPT as an inventor: Eliciting the strengths and weaknesses of current large language models against humans in engineering design. arXiv 2404.18479 (preprint). https://arxiv.org/abs/2404.18479. Checked: fetched (design-b-07), snippet (design-d-14). [design-b-07, design-d-14]
16. Zhang, X., Gu, J., Chen, H., Ding, S., Chai, C., Fan, H. (2025). Leveraging LLMs to emulate the design processes of different cognitive styles. AHFE 2025. https://openaccess.cms-conferences.org/publications/book/978-1-964867-39-7/article/978-1-964867-39-7_12. Checked: fetched. [design-b-08]
17. Wang, A., Li, Z., Tong, X., Hui, P. (2025). DesignerlyLoop: Forming Design Intent through Curated Reasoning for Human-LLM Alignment. arXiv 2511.15331 (preprint). https://arxiv.org/abs/2511.15331. Checked: fetched. [design-b-09, design-c-10]
18. Bruggeman, R., Ciliotta Chehade, E., Marion, T., Ciuccarelli, P. (2025). Probabilistic Methods for Evaluating Human and LLMs During Design Problem-Solving. Proceedings of the Design Society 5 (ICED25), 2651-2660. https://www.cambridge.org/core/product/A4AEC038573F521DF5808BFFB6D9C67E/core-reader. Checked: fetched. [design-b-10, design-b-11]
19. Wadinambiarachchi et al. (2024). The Effects of Generative AI on Design Fixation and Divergent Thinking. CHI 2024. https://dl.acm.org/doi/10.1145/3613904.3642919. Checked: snippet (page returned 403). [design-b-12]
20. ICCC 2026 paper 78 (authors and title not read). https://computationalcreativity.net/iccc26/papers/ICCC26_paper_78.pdf. Checked: memory (PDF unreadable). Not cited as support. [design-b-15, design-c-16]
21. Huang, J., Chen, X., Mishra, S., Zheng, H. S., Yu, A. W., Song, X., Zhou, D. (2023). Large Language Models Cannot Self-Correct Reasoning Yet. ICLR 2024 (arXiv 2310.01798). https://arxiv.org/abs/2310.01798. Checked: fetched. [design-c-04]
22. Kamoi, R., Zhang, Y., Zhang, N., Han, J., Zhang, R. (2024). When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs. TACL 12, 1417-1440 (arXiv 2406.01297). https://arxiv.org/abs/2406.01297. Checked: fetched. [design-c-05]
23. Liu, R., Geng, J., Wu, A. J., Sucholutsky, I., Lombrozo, T., Griffiths, T. L. (2024). Mind Your Step (by Step): Chain-of-Thought can Reduce Performance on Tasks where Thinking Makes Humans Worse. arXiv 2410.21333 (preprint). https://arxiv.org/abs/2410.21333. Checked: fetched. [design-c-06]
24. Gema, A. P., Hagele, A., Chen, R., Arditi, A., et al. (2025). Inverse Scaling in Test-Time Compute. TMLR (arXiv 2507.14417). https://arxiv.org/abs/2507.14417. Checked: fetched. [design-c-07]
25. Chen, X., Xu, J., Liang, T., He, Z., et al. (2024). Do NOT Think That Much for 2+3=? On the Overthinking of o1-Like LLMs. arXiv 2412.21187 (preprint). https://arxiv.org/abs/2412.21187. Checked: fetched. [design-c-08]
26. Doshi, A. R., Hauser, O. (2023). Generative artificial intelligence enhances creativity but reduces the diversity of novel content. arXiv 2312.00506 (journal version in Science Advances 2024 not opened). https://arxiv.org/abs/2312.00506. Checked: fetched. [design-c-09]
27. Sharma, M., Tong, M., Korbak, T., Duvenaud, D., Askell, A., et al. (2023). Towards Understanding Sycophancy in Language Models. arXiv 2310.13548 (preprint, ICLR 2024). https://arxiv.org/abs/2310.13548. Checked: fetched. [design-c-11]
28. Kokotovich (2015). IASDR 2015 paper on interpretation of the co-evolution model. https://opus.lib.uts.edu.au/bitstream/10453/41435/1/IASDR2015%20Kokotovich%20Final%20Paper%20378%20.pdf. Checked: memory (PDF unreadable). [design-c-14]
29. Biskjaer, M. M., Halskov, K., de Rooij, A. (2026). Problem-solution co-evolution research in the DRS conference community (2001-2025). DRS 2026. https://dl.designresearchsociety.org/drs-conference-papers/drs2026/researchpapers/240. Checked: fetched (abstract). [design-d-03, design-d-04, design-d-15]
30. Hatipoglu, S. C., Yildiz, D. (2018). Examples in Design Education: Inspiration or Fixation? SHS Web of Conferences. https://doi.org/10.1051/shsconf/20184801061. Checked: snippet. [design-d-07]
31. Turpin, M., Michael, J., Perez, E., Bowman, S. R. (2023). Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting. NeurIPS 2023 (arXiv 2305.04388). https://arxiv.org/abs/2305.04388. Checked: fetched. [design-d-08, design-d-19]
32. Lanham, T., et al. (2023). Measuring Faithfulness in Chain-of-Thought Reasoning. arXiv 2307.13702 (preprint). https://arxiv.org/abs/2307.13702. Checked: fetched (abstract wording to be checked against the paper). [design-d-09]
33. Lu, L.-C., Liu, M., Lu, P.-C., Tian, Y., Sun, S.-H., Peng, N. (2025). Rethinking Creativity Evaluation: A Critical Analysis of Existing Creativity Evaluations. arXiv 2508.05470 (preprint). https://arxiv.org/abs/2508.05470. Checked: fetched. [design-d-10, design-d-20]
34. Wang, X., Wu, J., Li, X., Zheng, C., Zhou, Y. (2026). Decoupled Analysis-Judging: An Automated Creativity Evaluator Using LLMs in Complex Multi-step Creativity Tasks. arXiv 2609.03432 (preprint). Checked: fetched. [design-d-11]
35. Gerrits, van Noord, Guerberof Arenas (2026). Creativity Bias: How Machine Evaluation Struggles with Creativity in Literary Translations. arXiv 2605.13596 (preprint). https://arxiv.org/abs/2605.13596. Checked: snippet. [design-d-12]
36. Mullen et al. (1991) and Diehl and Stroebe on production blocking (nominal groups). No source retrieved. Checked: memory. [design-d-18]

Bottom line for the agent design: supported rules are to gate by task type (M2), reframe on external check output (M1), keep divergence only on open tasks (M3), use a separate-context critic (M6) and an evaluator with bias controls (M7) [design-c-04, design-c-05, design-c-06, design-c-09, design-c-11, design-d-20]. The bridge cycle, frame step and lesson timing (M4, M8) are hypotheses for equal-token arms, not findings [design-a-15, design-d-15].
