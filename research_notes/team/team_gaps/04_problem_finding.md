# 04. Problem finding and goal selection by automated systems

Date: 2026-10-17. Question: what does research say about choosing what to work on, and how can HTSA do it without drifting to trivial or unfalsifiable goals?

"Verified" = I read the claim on the cited page this session (abstract or HTML). "Memory" = recalled from training, not re-checked. Do not quote memory numbers without a check.

## 1. Evidence table

| # | Claim | Evidence | Numbers | Source URL | Status |
|---|---|---|---|---|---|
| 1 | Artists who spent longer finding their problem made more original work | Getzels and Csikszentmihalyi 1976, "The Creative Vision". Art students had 27 objects and one hour to draw. Problem-finders explored and rearranged longer. Outside judges rated their work higher | 27 objects; follow-up found 27 of 31 students (one account); 8 of the 11 lowest problem-finders had quit art. Sources disagree on follow-up timing (5 vs 7 and 11 years) | https://thereader.mitpress.mit.edu/the-1960s-art-school-experiment-that-redefined-creativity/ ; review https://muse.jhu.edu/article/599015/summary | Secondary sources via search; book not read. Treat numbers as soft |
| 2 | Problem construction is a distinct skill that feeds creative output (Mumford) | Mumford et al. on problem construction | none retained | none fetched | Memory |
| 3 | Posing problems is part of the work, not a warm-up (Polya, Silver) | Silver 1994, "On mathematical problem posing", For the Learning of Mathematics 14(1) 19-28. Posing = creating new problems and reformulating given ones. Credits Polya and Freudenthal | pp. 19-28 | https://link.springer.com/doi/10.1007/BF03217299 | Citation verified by search. Polya "looking back" is memory |
| 4 | Good problem choice needs an attack, not just importance | Hamming: "It's not the consequence that makes a problem important, it is that you have a reasonable attack." Keeps 10 to 20 important problems in mind. Spent 10% of time on big questions | 10 to 20 problems; 10% time | https://www.cs.virginia.edu/~robins/YouAndYourResearch.html | Verified on page |
| 5 | Choose on two axes: feasibility and interest. Spend time choosing before starting | Alon 2009, Molecular Cell 35(6) 726-728. Feasibility axis = difficulty. Interest axis = knowledge added. His lab asks new students to wait 3 months before committing | 3 months | https://li.me.jhu.edu/wp-content/uploads/Alon_2009.pdf | Verified via search summary |
| 6 | POET: generate problems and solve them together. Transfer of solutions between problems is essential | Wang et al. 2019. Solved challenges that direct optimization and a direct-path curriculum could not | no numbers on abstract | https://arxiv.org/abs/1901.01753 | Verified (abstract). "Minimal criterion" is NOT on this page. From memory: new environments must sit in a reward band, neither too easy nor too hard for current agents |
| 7 | Enhanced POET adds a domain-general novelty measure, a transfer heuristic, and a generic measure of open-ended progress | Authors say original POET was limited by a restricted problem space and no universal progress measure | four advances | https://arxiv.org/abs/2003.08536 | Verified (abstract) |
| 8 | "Learnable" alone is not "interesting". OMNI uses a foundation model as a model of interestingness | Zhang et al. 2023. Interesting = learnable and worthwhile (novel, not a minor variant of mastered tasks). Beats uniform sampling and learning-progress-only baselines | no numbers on abstract | https://arxiv.org/abs/2306.01711 | Verified (abstract) |
| 9 | OMNI-EPIC writes tasks as code (environment plus reward). Learnable = not too easy or hard for current skills | Faldor et al. 2024. Adjusts difficulty to the agent's progress | none on abstract | https://arxiv.org/abs/2405.15568 | Verified (abstract). Failure modes not on page |
| 10 | Teacher picks tasks by absolute learning progress. Handles many unlearnable tasks | Portelas et al. 2019, ALP-GMM, continuous bandit over environment parameters | none on abstract | https://arxiv.org/abs/1910.07224 | Verified (abstract) |
| 11 | CURIOUS: pick goals with highest absolute learning progress. Revisits goals it starts to forget. Robust to distractor goals | Colas et al., ICML 2019 | none on abstract | https://arxiv.org/abs/1810.06284 | Verified (abstract) |
| 12 | Compression progress as reward: interesting = data you start to predict or compress better | Schmidhuber 2010 | n/a | https://www.ece.uvic.ca/~bctill/papers/ememcog/Schmidhuber_2010.pdf | Verified via search summary. Oudeyer and Kaplan 2007: citation only; content is memory |
| 13 | Raw prediction error is fooled by noise (noisy TV). Progress, not error, is the safer signal | General curiosity literature | n/a | none fetched | Memory |
| 14 | LLM ideas beat human experts on novelty, not feasibility | Si, Yang, Hashimoto 2024. 49 idea writers, 79 reviewers (24 also wrote), 298 reviews, 1-10 scale | Novelty: human 4.84, AI 5.64, AI+human rerank 5.81. Excitement 4.55 / 5.19 / 5.46. Feasibility 6.61 / 6.34 / 6.44 (AI slightly lower, not significant). Overall 4.68 / 4.85 / 5.34 | https://arxiv.org/abs/2409.04109 ; https://arxiv.org/html/2409.04109v1 | Verified on page |
| 15 | LLM ideation lacks diversity | Of 4,000 generated seed ideas only about 200 were non-duplicates | about 5% unique | https://arxiv.org/html/2409.04109v1 | Verified on page |
| 16 | LLM judges are poor at ranking ideas | Balanced accuracy vs human consensus | Human inter-reviewer 56.1%; best LLM (Claude-3.5 pairwise) 53.3%; GPT-4o direct 50.0%; random 50.0%. NeurIPS'21 66.0%, ICLR'24 71.9% | https://arxiv.org/html/2409.04109v1 | Verified on page |
| 17 | AI co-scientist: generate, critique, evolve hypotheses in a tournament, conditioned on a researcher's goal. Quality rises with test-time compute. AML drug candidates validated in vitro | Gottweis et al. 2025, Gemini-based | no counts on abstract page | https://arxiv.org/abs/2502.18864 | Verified (abstract). Elo numbers are memory, unconfirmed |
| 18 | ResearchAgent: start from a paper, add graph and entity knowledge, define problems, iterate with reviewer agents whose criteria come from human judgments | Baek et al., NAACL 2025 | none on abstract | https://arxiv.org/abs/2404.07738 | Verified (abstract). Ranking method not on page |
| 19 | Agent Laboratory, AI Scientist, SciMON keep a human or fixed goal at the top | n/a | n/a | none fetched | Memory only. Do not cite numbers |
| 20 | Value of information (Howard 1966), Bayesian experimental design, knowledge gradient (Frazier, Powell): value of an experiment = expected improvement in the best decision minus cost | Standard decision theory | n/a | none fetched | Memory |

## 2. What the evidence says, in plain English

- People who spend more time on problem choice produce better work. This shows in artists and in advice from Hamming and Alon. Both add a limit: the problem must be attackable.
- Automated goal generators that worked used two filters. One is learnable (not too easy, not impossible). The other is interesting or novel. Learnable alone gives trivial tasks. OMNI says this directly.
- Learning progress picks productive tasks, but I only found evidence in simulated curricula (walkers, robot arms). I found none for open research questions. Treat it as a heuristic.
- LLMs propose ideas humans rate as more novel, but they repeat themselves (about 5% unique) and cannot rank them (53.3% vs 50% chance). So the ranker must not be a plain LLM opinion.
- Si et al. did not run the ideas. Novelty scores are not outcomes. They propose that as follow-up.
- No source I read describes a system that safely picks its own top-level goal. They keep the goal external or put a human on top (co-scientist takes a researcher goal). That supports a veto.

## 3. How HTSA should score and pick the next question

### Formula

score(q) = P(resolve) x Gain(q) x Novelty(q) / Cost(q), applied only to questions that pass the hard gates.

Inputs HTSA already has:
- Gain(q): tree priority of the node q sits under, times how many open siblings or parent goals the answer would unblock.
- Cost(q): the token or compute estimate already produced per question.
- P(resolve): past yield, the share of earlier questions of the same type (part, fact, weak spot, upward) that ended with a test verdict. Start at a prior of 0.5 and update with counts (Beta prior). With little data, stay near the prior.
- Novelty(q): 1 minus max similarity to questions already asked or answered. Counters the 5% unique finding.

Upward proposals: take Gain from the expected change to what the test reads, not from LLM enthusiasm. They have higher cost and lower P(resolve), so they rarely win on score. That is acceptable; they get a reserved slot (step 5).

### Ranked procedure

1. Hard gates first (drop, do not score): the question names a test that can fail, a pass/fail threshold, and a cost cap. No test, no entry.
2. Score survivors with the formula. Use test-result history, not LLM self-rating, for P(resolve) and Gain.
3. Learning-progress bonus per tree branch: absolute change in the test metric (or in count of closed questions) over the last 2 rounds. Flat for 2 rounds means down-weight. Moving means bonus. Use absolute change so a branch getting worse also gets attention.
4. Pick the top question. Show the top 3 with scores. The human can veto or swap before the round. Default is proceed.
5. Exploration slot: about 1 round in 5 (or 20% of budget) takes the best upward proposal or a random high-novelty question regardless of score. This echoes Hamming's 10% on big problems and stops the formula collapsing onto cheap questions.
6. After each round, log predicted vs actual cost, gain and resolved. Update P(resolve). If predicted and realised gain correlate poorly, fall back to tree priority only.

## 4. Guardrails to add

- Must-be-measurable rule. Every question and upward proposal carries a test, a metric, a threshold, and a "what counts as failure" line. Missing any one: reject.
- Minimal criterion (POET style). Reject questions the existing tree can already answer (too easy) and ones with no plausible attack (Hamming). Practical check: a short attack sketch or cheap pilot must exist.
- Budget cap per question and per round. Kill at the cap. Track unresolved spend per branch.
- Anti-triviality: a Novelty floor and a minimum Gain. Alarm if the cheapest option is picked in over half of rounds.
- Anti-unfalsifiability: no vague success words ("better understanding"). A reframe must change a number the test reads.
- Goal-drift check: every pick traces to a node of the externally given goal. A pick that does not trace up needs a human OK.
- Human veto at two points: the pick (default proceed) and any change to the success measure (default hold; a person must approve). The system must not rewrite its own test.
- Hold-out check: keep some test items unseen by the question chooser so the choice process cannot overfit the test.
- Dedupe proposals before ranking.

## 5. What to avoid

- Ranking by LLM score alone (best judge 53.3% vs 50% random).
- Treating novelty ratings as value. Si et al. never ran the ideas.
- Raw learning progress without absolute value and an unlearnable-task guard.
- Letting the system change the success measure or goal without a person. No source shows this is safe.
- Citing learning progress as proven for research questions.
- Relying on "interestingness" from a model of human taste (OMNI) alone; in research it may favour fashionable questions.
- Copying POET numbers or co-scientist Elo into design docs; not verified here.

## 6. Gaps

- Not read: Getzels book, Mumford papers, Polya, Oudeyer and Kaplan full text, Howard, Frazier knowledge gradient, goal-drift literature, SciMON, Agent Laboratory, co-scientist body (Elo, goal refinement stage). All memory-level.
- POET minimal criterion wording and OMNI-EPIC failure modes need the full papers.
- Only the first 100,000 characters of the Si et al. HTML were read.
