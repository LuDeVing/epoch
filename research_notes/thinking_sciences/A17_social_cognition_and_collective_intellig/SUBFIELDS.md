# Social cognition and collective intelligence: subfields

This field studies how people think about others and how groups think together. It divides into aggregation (wisdom of crowds), social influence and conformity, group decision making, the collective intelligence factor, mass collaboration and deliberation, and theory of mind. We already have rules against debate (G9) and against treating samples as independent (G4). The useful parts are the conditions under which aggregation works and the ways it fails.

Marks: (V) = confirmed in a source opened this session; (M) = from memory.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Wisdom of crowds: conditions | Needs independence, diversity, a correct answer, random not shared error | Galton 1907; Condorcet 1785; Surowiecki; Page's diversity theorem (V via Wikipedia) | High | G4 and selection: when a vote is valid |
| Crowd within | Averaging repeated guesses by one person helps a little; anchoring limits it | Vul and Pashler 2008; Herzog and Hertwig 2009 dialectical bootstrapping; Ariely et al. 2000 found no gain (V via Wikipedia) | High | Single-model resampling is a "crowd within"; expect small, correlated gains |
| Surprisingly popular method | Picks the answer more common than predicted, cutting errors 21.3% against majority vote in the reported study | Prelec, Seung, McCoy 2017 (V via Wikipedia) | Med | Selection idea to test in code |
| Social influence on crowds | Mild influence reduces diversity without raising accuracy; individual incentives raise convergence on the group mean | Lorenz et al. 2011; Bazazi et al. 2019, PLoS ONE (V) | High | G4/G9: keep attempts isolated |
| Consensus and premature agreement | Groups seeking consensus can lose accuracy; contrarians sidelined | Wikipedia summary (V) | Med | G9 evidence |
| Conformity | Following the majority | Asch 1951/1955 (cited in Bazazi, V) | Med | G5: models conform to a stated answer |
| Collective intelligence factor c | Group general ability across tasks; 192 groups, first factor about 43 to 44%; linked to social sensitivity and turn-taking | Woolley et al. 2010; Engel et al. 2014 (V via Wikipedia) | Low | Background only |
| Disputes over c | Weak evidence claimed; a correction cut one reported variance figure from 44% to 19.6% | Credé and Howardson 2017; Riedl et al. 2021 correction (V via Wikipedia) | Low | Warns against leaning on c |
| Group ability and task type | Communication tasks depend on the least able member; selection tasks on the most able | Devine and Phillips 2001 (V via Wikipedia) | Low | Background only |
| Transactive memory and reasoning | Groups divide who remembers what | Wegner 1987 (M); Transaction Systems Model (S) | Med | Memory design |
| Mass collaboration, deliberation | Open collaboration; epistemic democracy | Tapscott and Williams; Landemore (V via Wikipedia) | Low | Background only |
| Theory of mind | Reasoning about others' beliefs | Premack and Woodruff (M) | Low | Background only |

Correction from the first draft: the Wikipedia collective intelligence page carries a notice that parts may be machine-written, so those figures need checking in the original papers before use.

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Wisdom of crowds: conditions | | not started |
| Crowd within | [`subfields/02_crowd_within/DEEP.md`](subfields/02_crowd_within/DEEP.md) | done, batch 5 (2026-10-27) |
| Surprisingly popular method | | not started |
| Social influence on crowds | | not started |
| Consensus and premature agreement | | not started |
| Conformity | | not started |
| Collective intelligence factor c | | not started |
| Disputes over c | | not started |
| Group ability and task type | | not started |
| Transactive memory and reasoning | | not started |
| Mass collaboration, deliberation | | not started |
| Theory of mind | | not started |

## Dig into next

**1. Conditions for aggregation to work.**
- Questions: How correlated are samples from one model, and how does error fall with N under that correlation? Which sources of variety (wording, order, tools) lower correlation without lowering accuracy?
- Evidence needed: Page's diversity theorem; Lorenz et al.; our agreement data (92% vs 75% test).

**2. Why influence harms.**
- Questions: At what point does showing one attempt to another bias it? Does a blind critic behave better than a debate turn?
- Evidence needed: Bazazi et al. 2019 (opened); our blind versus non-blind critic runs.

**3. Surprisingly popular selection.**
- Questions: Can a prediction of "what others will answer" be elicited from a model and used in code to pick a minority-correct answer?
- Evidence needed: Prelec et al. 2017 (to be opened); a test on our single-answer items.

## Does not transfer

Reputation, status, trust, group identity, leadership and the social cost of disagreement are about people. One model is not a group. The c factor, built on social sensitivity and turn-taking, cannot be applied to one agent. Hidden-profile findings need members with different private information.

## Sources

[V] = opened this session. [S] = seen in search results only. [M] = from memory. Opened count: 4. The extra searches could not be run (search budget used up).

1. [V] Bazazi, von Zimmermann, Bahrami, Richardson 2019, PLoS ONE: https://pmc.ncbi.nlm.nih.gov/articles/PMC6855459/
2. [V] Salminen 2012, Collective Intelligence in Humans: A Literature Review (PDF text read, short): https://arxiv.org/pdf/1204.3401
3. [V] Wikipedia, Wisdom of the crowd: https://en.wikipedia.org/wiki/Wisdom_of_the_crowd
4. [V] Wikipedia, Collective intelligence: https://en.wikipedia.org/wiki/Collective_intelligence
5. [S] Transaction Systems Model of Collective Intelligence: https://www.psychologicalscience.org/journals/perspectives/17456916231191534/
6. [M] Lorenz et al. 2011 PNAS; Wegner 1987
