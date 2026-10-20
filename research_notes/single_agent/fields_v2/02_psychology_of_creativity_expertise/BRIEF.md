# Psychology of creativity and expertise: what it offers one thinking agent

Evidence ids are short: a-03 means psychcreat-a-03, b-12 means psych-b-12, c-15 means 02-c-15, d-05 means 02-d-05. Where a CHECK line in evidence_d disagrees with claims.jsonl, the CHECK line wins. Our own measurements come from 00_PLAN.md and are cited as "our data". Credibility is stated in the references.

## 1. What the field studies

The field asks how people produce new and useful ideas, and how experts differ from novices. Creativity work looks at problem finding, fixation, incubation and group idea generation (a-01, a-03, a-15, c-01). Expertise work looks at chunking, problem representation and the role of practice (a-12, a-14, a-07). For one agent, the useful parts are the failure modes (fixation on a familiar answer, weak group process) and the conditions under which they appear (a-05, c-16).

## 2. Established findings

Status is "established" in claims.jsonl. I note where a CHECK line or the sources soften it.

**2.1 A familiar good solution blocks a better one, even in experts (Einstellung).** In chess, experts said they searched for a better move but kept looking at the features of the first one (a-03, b-16). Their performance dropped to that of players about three classes weaker (b-16, snippet). An independent eye-tracking study found that experts who chose the familiar move kept looking at it, while those who found the best move gradually looked away (a-04, b-17). Two labs agree, both in chess, so transfer to open tasks is by analogy. The Bilalic original is known from a snippet only (a-03, b-16).

**2.2 Deliberate practice explains a modest share of skill differences.** A meta-analysis of 88 studies and 11,135 people found practice explained 26% of variance in games, 21% in music, 18% in sports, 4% in education and under 1% in professions (a-07). One copy of the same paper reports about 12% overall (b-18). The claims file says "about 18% overall". That is wrong: 18% is the sport figure (a-07). Use 12% overall. A sport-only meta-analysis gave about 18% overall in sport and about 1% among elite performers (c-07). A double-blind replication with 39 violinists did not reproduce the original finding that practice matched skill level (a-10, c-11). Three of these sources share a lead author, so independence is partial (claims.jsonl note).

**2.3 Chess skill rests on large stores of chunks and templates.** Masters recalled real positions far better than novices, but were no better on random positions (a-12). Template theory adds long-term templates, with about 50,000 chunks estimated for masters, and says experts do better on random positions given time (a-13, b-21). All three are snippet level.

**2.4 Real interacting groups brainstorm worse than the same people working alone and pooled.** Nominal groups produced nearly twice as many different ideas (c-01). Of 22 earlier experiments, 18 favoured nominal groups and 4 (all two-person groups) showed no difference (c-02). Waiting for a turn (production blocking) explained most of the loss in direct manipulations (c-03). On quality, all six earlier studies that measured total quality favoured nominal groups (c-04). A meta-analysis agrees, with a larger gap for bigger groups, but I only have a secondary summary of it (c-05).

**2.5 Shown examples make designers copy example features.** This is the standard design fixation result, known from secondary pages (c-19). A direct experiment with 60 people found an AI image generator raised fixation on an initial example and led to fewer, less varied ideas (b-12). One review argues the mechanism may be a used-up pool of likely solutions, not conformity (c-20).

## 3. Single-source and contested findings

### 3.1 Single-source

- **Einstellung has a boundary.** When the familiar move was a clear blunder, all experts and most novices avoided it (a-05, c-16, b-17). When it was good but suboptimal, 8 of 17 experts and 8 of 17 novices chose it (a-05, c-15). One study, 34 players. Reading for design: a failure signal drives the switch, not a schedule (c-16).
- **Luchins water-jar.** A practiced long method persisted on a problem with a simple solution (a-06). Snippet only.
- **Experts sort by principle, novices by surface.** Four experiments, 8 experts and 8 novices in the first (a-14, d-03). The citation is confirmed, but no replication was found in this round (d-04).
- **Experts look at the target faster** (407 ms against 719 ms) (c-17).
- **Incubation is small and conditional.** The meta-analysis of 117 studies found a small positive effect, larger for divergent than for insight tasks (a-15, c-12). A demanding break task weakens it (c-13). Earlier studies conflicted (c-14). A later study with 90 analyzed people found an effect only in a mindfulness group and only on flexibility, not on fluency or originality (d-05). No preregistered replication was found (d-07). Stays "small and conditional".
- **Problem finding.** Art students who explored longer before drawing made work experts rated more original (a-01). Cohort study, snippet only. No test on LLM agents exists (b-22).
- **Intelligence and creativity correlate weakly** (r about .17) in a meta-analysis of about 21 studies (a-16). The venue of the citation was not verified. The art cohort also found no link to success (a-02).
- **Executed LLM ideas lose their novelty edge.** At ideation, LLM research ideas were judged more novel than expert ideas, and slightly weaker on feasibility (b-14, d-10). After 43 experts spent over 100 hours executing ideas, LLM ideas lost significantly more score than human ideas (b-15). One research group, two stages.
- **Chain-of-thought reduced fixation in LLMs but not in humans** (b-05). One preprint, abstract only.
- **Stronger reasoning models fall into Einstellung traps less** (b-02). The top 5 models answered 55% to 70% correctly, with high confidence, on questions physicians commonly miss (b-03). One medical preprint.
- **Self-revision without outside feedback does not help LLM reasoning and can hurt** (c-18). One preprint, abstract only.
- **Telling designers about fixation reduced it** (c-21). Snippet, credibility 40.
- **Chess hours to master vary from 3,016 to 23,608** (c-09). Secondary citation.

### 3.2 Contested

- **How big the practice effect is.** A music meta-analysis with a broader definition found a larger effect (a-08). Critics say a correlation of 0.61 should not be read as 36% of variance, and that the claim is about a third (a-09, c-10). The original claim rested on retrospective estimates from groups of musicians (a-11, c-11). A 2020 review asks whether the view is a testable theory (b-19). Both camps agree on direction: practice matters, but not all.
- **Electronic brainstorming removes the group penalty.** One search summary says yes (c-23). Writing ideas while waiting did not fix it (c-22, an encyclopedia summary). The check on this failed because the source could not be opened (d-12, d-13). Unsettled.
- **Persona prompts.** A large study found "genius" or demographic personas did not reliably raise creativity, while temperature helped up to a point (b-07). A preprint found ordinary personas improved diversity more than famous ones (b-06). The measures differ.
- **Weisberg's ordinary-thinking view.** Creative thinking is ordinary thinking (a-18, b-20). Theory from one author. Do not build a step on it.

## 4. Mechanisms an agent can run

All checks use the equal-token test: give the plain model the same total tokens (for example best-of-N or longer plain reasoning) and compare. Risk is judged against our data: forced divergence helped open tasks (NoveltyBench 3.18 to 9.63, architecture search 7% lower perplexity) and hurt single-answer tasks (ARC 4/10 plain against 2/8 scaffold, word puzzles about 92% against about 75%).

**M1. Doubt on a failure cue, not on a schedule.**
- Trigger: a check fails, or two independent samples disagree. Not run by default.
- Action: drop the current answer's frame and generate a fresh approach from the task statement only.
- Check: three arms on both task types: plain, always-doubt, doubt-on-cue, at equal tokens. Prediction: doubt-on-cue keeps the open-task gain and avoids most of the single-answer loss (critique.md).
- Evidence: a-05, c-16, b-17, a-03, a-04.
- Risk: single-answer tasks often show no visible cue. Samples from one model are correlated, so agreement is weak evidence (our data). Then the trigger never fires and the step gives nothing.

**M2. Task regularity gate (turn the schema off).**
- Trigger: start of every task.
- Action: classify the task as open-ended (many valid answers) or single-answer with a checkable result. On single-answer tasks, answer plainly and spend tokens on verification, not divergence.
- Check: compare gate on against always-on divergence at equal tokens, on ARC and word puzzles.
- Evidence: our data; Kahneman and Klein is only a record, with the claim unverified (d-01, d-02). The expert Einstellung boundary is the closest verified support (a-05).
- Risk: a wrong gate decision loses the open-task gain. This is the largest gap in the field, since no verified human work on when to trust a first answer was found (critique.md).

**M3. Independent draws, then merge (nominal group).**
- Trigger: open-ended task needing many ideas.
- Action: run N calls with no sight of each other's output, then merge and dedupe. Do not let calls take turns in one context.
- Check: N independent calls against one long chat of N turns, equal tokens.
- Evidence: c-01, c-02, c-03, c-04.
- Risk: samples from one model are correlated, so pooling gives less than with people (our data, b-11). The human effect comes from blocking, which a model does not have in the same form (section 6).

**M4. Fresh-context re-draw after exposure to an example.**
- Trigger: the agent has produced or been shown a first solution and must find alternatives.
- Action: ask for alternatives in a new context that does not contain the first solution.
- Check: alternatives generated in-context against in-fresh-context, measuring distinct answers at equal tokens.
- Evidence: b-12, c-19, c-20, b-05, b-13.
- Risk: the used-up-pool account (c-20) predicts the loss is partly just coverage, so a fresh draw may repeat the same mode. Little to lose on single-answer tasks if gated by M2.

**M5. Incubation as a context reset.**
- Trigger: stuck after the first attempt on an open or insight task.
- Action: set the problem aside, run a light unrelated step, then restart from the task statement.
- Check: reset against continued reasoning at equal tokens.
- Evidence: a-15, c-13, d-05, d-07.
- Risk: the human effect is small and conditional, and no LLM test exists. Cheap to try, but expect a null.

**M6. Problem-finding pass before solving.**
- Trigger: open-ended task with vague goals.
- Action: list ways to reframe the task and pick one before generating solutions.
- Check: pass on against off, on open tasks only, equal tokens.
- Evidence: a-01, a-02, b-22.
- Risk: single cohort, snippet level, and no LLM test. Treat as a hypothesis to measure. On single-answer tasks it adds tokens and drift.

**M7. Problem representation by principle.**
- Trigger: any technical task.
- Action: before solving, restate the problem by its underlying principle, not its surface wording, and retrieve methods from that principle.
- Check: restate-first against direct solving, equal tokens, on tasks with misleading surface cues.
- Evidence: a-14, d-03, d-04, b-01.
- Risk: single source, no replication found here (d-04). The models may already do this.

**M8. Selection with a weak judge.**
- Trigger: after generating many candidates.
- Action: select with a judge, but report judge uncertainty and keep a diverse shortlist, not only the top one.
- Check: judge-picked against random pick from the same pool, scored by an independent grader.
- Evidence: d-08, d-09, d-11, b-15, b-14.
- Risk: the CHECK line says LLM judges are weak evidence for picking the best idea, especially on feasibility (d-11). A bad judge turns a diversity gain into noise.

## 5. Evidence on LLMs and AI agents

- LLMs show fixation: early outputs constrain later ones, and ideas converge on familiar spaces (b-04, b-05). The Only Connect benchmark was built to test red-herring fixation (b-01). One hackathon study saw ChatGPT recommend the last item in a supplied list for every prototype (b-13, search snippet, credibility 40). Mostly 2026 preprints, abstract level.
- Open-ended LLM answers are homogeneous within and across models, shown on 26K queries with 31,250 human annotations (b-11). This matches our correlated-samples finding.
- People who use AI idea tools show more fixation and fewer, less varied ideas (b-12). A meta-analysis of 28 studies and 8,214 participants found GenAI and humans do not differ in creative performance (g = -0.05), and humans helped by GenAI beat unaided humans (g = 0.27), with a diversity cost in human-AI work (b-09). A second meta-analysis of 17 studies found a small non-significant effect favouring GenAI, driven by a few large effects (b-10). LLMs can beat the average human on the Divergent Association Task, but the best models are still surpassed by top humans (b-08).
- Persona and temperature: see section 3.2 (b-06, b-07).
- LLM judges of creativity track humans only moderately and use a narrower set of standards (d-08). In a benchmark of 11,012 pairwise human comparisons, models clustered tightly and three LLM-judge setups correlated weakly and inconsistently with humans (d-09). Both are preprints, abstract level.
- Novel ideas can fail later: the ideation-execution gap (b-15).
- Stronger reasoning models may fall into traps less (b-02). That could shrink our forced-doubt gain on newer models (critique.md). Re-run our measurements when the model changes.
- Self-revision without feedback can hurt (c-18). It matches our scaffold loss on single-answer tasks.

## 6. What does not transfer to a model

- **Production blocking** is a human limit from waiting for a turn and holding an idea in memory (c-03). A model has no turn. Only the independence of draws transfers (M3).
- **Years of practice** and the deliberate practice debate (a-07, a-10) describe how humans train. A model does not accumulate hours in the run. Only the point that fixed procedure gives a modest share of performance gap carries over, and that is an analogy.
- **Chunk counts** such as 50,000 chunks (a-13) are human memory estimates.
- **Eye movements** (a-04, c-17) have no model counterpart, though attention to the first answer's features is the same idea.
- **Incubation by unconscious processing** is a human claim. Only a context reset can be tested (M5).
- **Personality and intelligence correlates** (a-16, a-17) describe people, not agents. Feist 1998 (a-17) was never used in a claim.
- **Weisberg's theory** (a-18, b-20) is a position. No step built on it.
- **Evaluation apprehension and social effects** in groups (c-03) do not apply to one model.
- Unusable sources: 02-c-24 (no author, credibility 0), c-21 (weak), b-13 (search result only).

## 7. Open questions

1. When is the first answer right? Verified human evidence is missing, since Kahneman and Klein could not be opened (d-01, d-02). The largest gap.
2. How do judges pick good ideas, and what does weak selection cost? Only weak preprints found (d-08, d-09, d-11).
3. Does doubt-on-cue beat always-doubt and plain at equal tokens on both task types? Needs our own run (critique.md).
4. Does an LLM incubation analogue help? No test (d-05, d-07).
5. Does problem finding help LLM agents? No test (b-22).
6. Can structured disagreement or a devil's advocate beat nominal groups? Nothing found. The electronic-group claim is unresolved (c-23, d-13).
7. Is the practice effect near 12% or a third? Depends on the definition (a-07, a-09, b-18).
8. Do forced-doubt gains shrink as models improve? One preprint hints yes (b-02).
9. Does Einstellung in chess transfer to open design or writing? Unknown (critique.md).

## 8. References

Checked means: fetched = page opened; abstract = abstract read; snippet = search result or record only; memory = not opened.

1. Getzels, J.; Csikszentmihalyi, M. (1976). The Creative Vision: A Longitudinal Study of Problem Finding in Art. Wiley. https://libcat.library.tamu.edu/Record/in00000601483. Snippet. (a-01)
2. Review of The Creative Vision (2015). Project MUSE. https://muse.jhu.edu/article/599015/summary. Snippet. (a-02)
3. Bilalic, M.; McLeod, P.; Gobet, F. (2008). Why good thoughts block better ones. Cognition 108(3):652-661. https://pubmed.ncbi.nlm.nih.gov/18565505/. Snippet. (a-03)
4. Sheridan, H.; Reingold, E. (2013). The mechanisms and boundary conditions of the Einstellung effect in chess. PLoS ONE 8(10). https://pmc.ncbi.nlm.nih.gov/articles/PMC3790829/. Fetched. (a-04, a-05, b-17, c-15, c-16, c-17)
5. Luchins, A. (1942). Mechanization in problem solving. Psychological Monographs. Via https://www.futilitycloset.com/2022/01/20/the-einstellung-effect/. Snippet. (a-06)
6. Macnamara, B.; Hambrick, D.; Oswald, F. (2014). Deliberate practice and performance in music, games, sports, education, and professions: a meta-analysis. Psychological Science. https://stafforini.com/works/macnamara-2014-deliberate-practice-and/. Snippet. (a-07, b-18, c-06)
7. Platz, F.; Kopiez, R.; Lehmann, A. (2014). The influence of deliberate practice on musical achievement. Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2014.00646/pdf. Fetched. (a-08)
8. Hambrick, D.; Oswald, F.; Altmann, E.; et al. (2014). Facing facts about deliberate practice. Frontiers in Psychology. https://pmc.ncbi.nlm.nih.gov/articles/PMC4101876. Fetched. (a-09, c-10)
9. Macnamara, B.; Maitra, M. (2019). The role of deliberate practice in expert performance: revisiting Ericsson, Krampe and Tesch-Romer (1993). Royal Society Open Science. https://pmc.ncbi.nlm.nih.gov/articles/PMC6731745/. Fetched. (a-10, a-11)
10. Chase, W.; Simon, H. (1973). Perception in chess. Cognitive Psychology. https://andymatuschak.org/prompts/Chase1973.pdf. Snippet. (a-12)
11. Gobet, F.; Simon, H. (1996). Templates in chess memory. Cognitive Psychology. https://bura.brunel.ac.uk/handle/2438/1339. Snippet. (a-13)
12. Chi, M.; Feltovich, P.; Glaser, R. (1981). Categorization and representation of physics problems by experts and novices. Cognitive Science 5(2):121-152. https://doi.org/10.1207/s15516709cog0502_2. Snippet. (a-14, d-03, d-04)
13. Sio, U.; Ormerod, T. (2009). Does incubation enhance problem solving? A meta-analytic review. Psychological Bulletin. https://pubmed.ncbi.nlm.nih.gov/19210055/ and https://eprints.lancs.ac.uk/id/eprint/56211. Snippet and fetched. (a-15, c-12, c-13, c-14)
14. Kim, K. (2005). Meta-analysis of the relationship between creativity and intelligence. Citation not verified. https://www.mdpi.com/2079-3200/9/2/23. Snippet. (a-16)
15. Feist, G. (1998). A meta-analysis of personality in scientific and artistic creativity. Personality and Social Psychology Review. https://journals.sagepub.com/doi/10.1207/s15327957pspr0204_5. Snippet. (a-17)
16. Weisberg, R. (1993; 2006). Creativity: Beyond the Myth of Genius; Creativity: Understanding Innovation in Problem Solving. https://www.cambridge.org/core/books/rethinking-creativity/setting-the-stage/749A572F4DC658A70404FB23B3820D71. Snippet. (a-18, b-20)
17. Naeini et al. (2023). Large Language Models are Fixated by Red Herrings. NeurIPS 2023 datasets track. https://arxiv.org/abs/2306.11167. Abstract. (b-01)
18. Shidara, Prem, Kim, et al. (2026). Advances in LLM Reasoning Enable Flexibility in Clinical Problem-Solving. arXiv 2601.11866. https://arxiv.org/abs/2601.11866. Preprint, abstract. (b-02, b-03)
19. Carichon, Sharma, Gira, et al. (2026). IDEAFix. arXiv 2606.00875. https://arxiv.org/abs/2606.00875. Preprint, abstract. (b-04)
20. Deng, Brucks, Toubia (2026). Examining and Addressing Barriers to Diversity in LLM-Generated Ideas. arXiv 2602.20408. https://arxiv.org/abs/2602.20408. Preprint, abstract. (b-05, b-06)
21. Huang et al. (2025). Divergent Association Task, humans against LLMs. Nature Human Behaviour. https://doi.org/10.1038/s41562-025-02331-1. Snippet. (b-07)
22. Bellemare-Pepin, Lespinasse, et al. (2024). Divergent Creativity in Humans and Large Language Models. arXiv 2405.13012. https://arxiv.org/abs/2405.13012. Preprint, abstract. (b-08)
23. Holzner, Maier, Feuerriegel (2025). Generative AI and Creativity: A Systematic Literature Review and Meta-Analysis. arXiv 2505.17241. https://arxiv.org/abs/2505.17241. Meta-analysis, abstract. (b-09)
24. de Rooij, Biskjaer (2025). GenAI vs human creativity meta-analysis. ACM proceedings. https://pure.au.dk/ws/files/465399318/3746175.3746189.pdf. Snippet. (b-10)
25. Jiang, Choi, et al. (2025). Artificial Hivemind. NeurIPS 2025. https://arxiv.org/abs/2510.22954. Abstract. (b-11)
26. Wadinambiarachchi et al. (2024). The Effects of Generative AI on Design Fixation and Divergent Thinking. CHI 2024. https://arxiv.org/abs/2403.11164. Abstract. (b-12)
27. ChatGPT as an inventor (2024). arXiv 2404.18479. https://arxiv.org/abs/2404.18479. Search result only, authors not read. (b-13)
28. Si, C.; Yang, D.; Hashimoto, T. (2024). Can LLMs Generate Novel Research Ideas? arXiv 2409.04109. https://arxiv.org/abs/2409.04109. Preprint, abstract. (b-14, d-10)
29. Si, C.; Hashimoto, T.; Yang, D. (2025). The Ideation-Execution Gap. arXiv 2506.20803. https://arxiv.org/abs/2506.20803. Preprint, abstract. (b-15)
30. Bilalic, McLeod, Gobet (2008). Inflexibility of experts: reality or myth? Cognitive Psychology. https://cognition.aau.at/download/Publikationen/Bilalic/Bilalic_etal_2008b.pdf. Snippet. (b-16)
31. Hambrick, Macnamara, Oswald (2020). Is the Deliberate Practice View Defensible? Frontiers in Psychology. https://pmc.ncbi.nlm.nih.gov/articles/PMC7461852/. Snippet. (b-19)
32. Gobet, F. (1998). Expert memory: a comparison of four theories. Cognition 66:115-. https://bura.brunel.ac.uk/handle/2438/815. Snippet. (b-21)
33. CoQuest authors (2024). CoQuest. CHI 2024. https://arxiv.org/abs/2310.06155. Snippet. (b-22)
34. Diehl, M.; Stroebe, W. (1987). Productivity loss in brainstorming groups: toward the solution of a riddle. Journal of Personality and Social Psychology. https://homepages.se.edu/cvonbergen/files/2013/01/Productivity-Loss-In-Brainstorming_Toward-the-Solution-of-a-Riddle.pdf. Fetched. (c-01, c-02, c-03, c-04)
35. Mullen, B.; Johnson, C.; Salas, E. (1991). Productivity loss in brainstorming groups: a meta-analytic integration. Basic and Applied Social Psychology. https://scrapbox.io/nishio-en/Productivity_Loss_in_Brainstorming_Groups:_A_Meta-Analytic_Integration. Secondary summary only. (c-05)
36. Macnamara, B.; Moreau, D.; Hambrick, D. (2016). Deliberate practice and performance in sports: a meta-analysis. Perspectives on Psychological Science. https://hhs.purdue.edu/skill-learning-and-performance-lab/wp-content/uploads/sites/43/2024/08/macnamara-et-al-2016-the-relationship-between-deliberate-practice-and-performance-in-sports-a-meta-analysis.pdf. Fetched. (c-07, c-08, c-09, c-11)
37. Ericsson, K.; Krampe, R.; Tesch-Romer, C. (1993). The role of deliberate practice in the acquisition of expert performance. Psychological Review. Read via the Macnamara and Maitra replication. (c-11)
38. Huang, J.; Chen, X.; et al. (2023). Large Language Models Cannot Self-Correct Reasoning Yet. arXiv 2310.01798. https://arxiv.org/abs/2310.01798v2. Preprint, abstract. (c-18)
39. Jansson, D.; Smith, S. (1991). Design fixation. Design Studies 12. https://journals.sagepub.com/doi/ref/10.1068/b200333. Snippet. (c-19)
40. Exposure effects in design idea generation: unconscious conformity or a product of sampling probability. Design Society. https://www.designsociety.org/download-publication/24262/exposure_effects_in_design_idea_generation_unconscious_conformity_or_a_product_of_sampling_probability. Snippet. (c-20)
41. Overcoming design fixation through education and creativity methods. ICED 2013. https://asiachapter.designsociety.org/download-publication/34578/Overcoming+design+fixation+through+education+and+creativity+methods. Snippet. (c-21)
42. Production blocking. Wikipedia, citing Diehl and Stroebe 1991. https://en.wikipedia.org/wiki/Production_blocking. Fetched, encyclopedia. (c-22)
43. DeRosa, D.; Smith, C.; Hantula, D. (2007). Electronic brainstorming meta-analysis. Computers in Human Behavior. https://www.sciencedirect.com/. Search summary only, not opened. (c-23, d-12, d-13)
44. Jagiellonian University record, authors unknown. https://ruj.uj.edu.pl/entities/publication/867bf388-56b6-4cd7-ab59-e5de974d16e7. Snippet, unusable. (c-24)
45. Kahneman, D.; Klein, G. (2009). Conditions for intuitive expertise: a failure to disagree. American Psychologist. https://doi.org/10.1037/a0016755. Record only (snippet); the content claim is from memory. (d-01, d-02)
46. Teng, S.-C.; Lien, Y.-W. (2022). Propensity or diversity? Investigating how mindfulness and mind-wandering relate to incubation. PLOS ONE. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0267187. Fetched. (d-05, d-07)
47. Tan, T.; Zou, H.; et al. (2015). Mind wandering and the incubation effect in insight problem solving. Creativity Research Journal 27(4):375-382. https://doi.org/10.1080/10400419.2015.1088290. Record only. (d-06)
48. Lyu, P.; Kim, Y.J.; et al. (2026). Why Large Language Models and Humans Converge on creativity judgments. arXiv 2607.22218. https://arxiv.org/abs/2607.22218. Preprint, abstract. (d-08, d-11)
49. Bhat, N.; Browne, K.; et al. (2025). Creativity Benchmark. arXiv 2509.09702. https://arxiv.org/abs/2509.09702. Preprint, abstract. (d-09, d-11)
