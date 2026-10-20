# Cognitive architectures: subfields

A cognitive architecture is a fixed program that models how a mind works: memories, a decision cycle and learning rules. The main families are Soar, ACT-R, EPIC, CLARION, Sigma, LIDA and global workspace models. The field divides by unit of control (operators or productions), by learning mechanism, and by theory of memory. Soar is the closest match to our schema: control is driven by impasses, and learning turns solved subgoals into rules. Marks: [V] = page opened this session; [M] = from memory or seen only in a search result.

## Subfields

| Subfield | What it studies | Key people or works | Useful (H/M/L) | How |
|---|---|---|---|---|
| Soar: operator selection and impasses | When preferences are insufficient, an impasse opens a substate | Soar tutorial [V]; Laird, Newell, Rosenbloom 1987 [M] | High | control: S6 IMPASSE |
| Soar: impasse types | Tie, no-change; the tutorial says others exist; search summaries list conflict and rejection (and later versions constraint-failure) | Soar tutorial [V]; manual not opened (URL gave 404) | High | S6: typed triggers |
| Soar: chunking | The trace behind a substate result is compiled into a new rule | Soar tutorial [V] | High | memory: subgoal library, S9 |
| Soar: other memories and RL | Episodic, semantic memory, operator preference learning | Laird 2012 [M] | Med | memory, S0 class record |
| ACT-R: production selection | One production fires; chosen by utility (payoff against cost) | ACT-R site [V] | Med | operator choice by success rate |
| ACT-R: declarative memory | Retrieval depends on context and history of use | ACT-R site, Wikipedia [V] | Med | memory ranking |
| ACT-R: production compilation | Merging steps into faster rules | Taatgen, Anderson [M]; not covered by the pages opened | Med | memory: lesson to routine |
| Hybrid and connectionist (CLARION, Sigma) | Explicit plus implicit knowledge | Sun; Rosenbloom [M] | Low | background only |
| Global workspace, LIDA | Broadcast and attention cycles | Baars; Franklin [M] | Low | background only |
| Language agents as architectures | Mapping Soar and ACT-R parts to LLM agents | arXiv 2607.23942 [M] | High | design check |

## Dig into next

1. **Soar impasse types and substates.** Which impasse types map to our S6 triggers (no change = no pass in two rounds; tie = two candidates equal)? What is returned from a substate (only results) and should our subgoal return only its result? Evidence: Soar manual impasse chapter (not yet opened), a trace of Soar on the Water Jug task, our logs of which trigger fired.
2. **Chunking as a subgoal library.** What is the condition part of a chunk, and how does Soar avoid over-specific chunks (the tutorial says chunks are only as general as the substate reasoning)? What is the LLM equivalent (a helper with a stated precondition)? Evidence: Soar chunking papers; a test that a stored rule helps on a second, different problem.
3. **ACT-R utility.** Can operator choice at S6 use a running success-minus-cost score per class? Evidence: operator logs with enough runs per class.

## Combined with LLMs

Opened, abstract level only:
- CogRec (arXiv 2512.24113): Soar plus an LLM for explainable recommendation. On an impasse the agent queries the LLM and chunking turns the answer into a rule. Reports "significant advantages" in accuracy, explainability and long-tail performance on three unnamed public datasets. No numbers and no LLM name on the abstract page; the PDF was unreadable by the fetch tool [V].
- NL2GenSym (arXiv 2510.09355): LLM generator plus critic that checks rules by running them in Soar. Task: Water Jug problem. Models: Gemini and Qwen series. Result: over 86 percent success writing rules; rules cut decision cycles to 1.98 times optimal; smaller models sometimes beat larger ones [V].
Both are narrow, unreplicated preprints. A 2026 review (arXiv 2607.23942) states robust experimental validation is largely absent [M]. No study compares an impasse-driven LLM agent with a plain one at equal tokens.

## Sources

1. https://soar.eecs.umich.edu/tutorials/soar_tutorial/05 [V] Soar tutorial: impasses and chunking
2. https://act-r.psy.cmu.edu/about/ [V] ACT-R overview
3. https://en.wikipedia.org/wiki/ACT-R [V] ACT-R article
4. https://arxiv.org/abs/2512.24113 [V] CogRec
5. https://arxiv.org/abs/2510.09355 [V] NL2GenSym
6. https://soar.eecs.umich.edu/soar_manual/04_ProceduralKnowledgeAndSoar/ [M] Soar manual, returned 404, not read
7. https://www.jimdavies.org/summaries/laird1987.html [M] summary of Laird et al. 1987
8. https://arxiv.org/pdf/2607.23942 [M] review of cognitive architectures and language agents
