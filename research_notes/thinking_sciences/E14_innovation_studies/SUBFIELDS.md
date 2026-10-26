# Innovation studies: subfields

Innovation studies examines how new products, methods and technologies arise. It divides into recombinant search (new things as new combinations of parts), exploration versus exploitation, organisational ambidexterity, breakthrough and novelty measurement, user and open innovation, and design-based processes. The branch most useful to us is search: how far to look from what is known, and how to tell a promising novelty from noise.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Recombinant search | New combinations have lower mean usefulness but higher variance; familiar components raise usefulness; refining a combination helps; reusing one too often hurts | Fleming 2001, using patent citations [V via AcaWiki] | High | Operator O7; analogue distance |
| Exploration versus exploitation | Experiment and risk versus refinement and efficiency; over-focus on either fails | March 1991 [V via Wikipedia] | High | S0 gate; G12 |
| Organisational ambidexterity | Structural (separate units) or contextual (same unit); mixed evidence that balance helps, depends on environment | Gibson and Birkinshaw 2004 (41 firms); He and Wong 2004; Jansen et al. 2006 [V via Wikipedia] | Low | Background only |
| Bandit-style exploration | Epsilon-greedy, Thompson sampling, UCB, intrinsic rewards; difficulties with sparse rewards and noisy-TV traps | Machine learning literature [V] | High | Tree search; per-class widen rule |
| Atypicality versus disruption | Atypical (distant) combinations extend topics; disruption replaces a dominant idea inside a topic; the two metrics differ. 41 million papers, 1965 to 2024 | arXiv 2506.15959 [V, abstract only] | Med | Selection; open mode |
| Breakthrough innovation | What marks rare high-impact work | Kaplan and Vakili 2015 [M] | Med | Selection |
| Novelty measurement | Atypical combinations in papers and patents | Uzzi et al. 2013 [M] | Med | Selection (open mode) |
| Design thinking, stage-gate, open and user innovation | Teachable processes; outside sources | Cooper, Brown, von Hippel, Chesbrough [M] | Low | Background only |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Recombinant search | [`subfields/01_recombinant_search/DEEP.md`](subfields/01_recombinant_search/DEEP.md) | done, batch 5 (2026-10-27) |
| Exploration versus exploitation | | not started |
| Organisational ambidexterity | | not started |
| Bandit-style exploration | | not started |
| Atypicality versus disruption | | not started |
| Breakthrough innovation | | not started |
| Novelty measurement | | not started |
| Design thinking, stage-gate, open and user innovation | | not started |

## Dig into next

1. **Recombinant search and distance.** Questions: Does Fleming's pattern (lower mean, higher spread for new combinations) match SCHEMA O7? Can distance between components be computed in code? What mix of familiar and new parts did best? Evidence needed: the 2001 paper itself (I read only a summary page), Kaplan and Vakili, Uzzi et al.
2. **Exploration versus exploitation.** Questions: Is there a usable rule for when a stuck search should widen? Do bandit methods give a cost-aware rule? Do ambidexterity results, which depend on environment, translate to per-class settings in S0? Evidence needed: March's simulation, bandit theory, our per-class pass rates.
3. **Atypicality versus disruption.** Question: Which kind of attempt (distant combination, or replacing the leading rule) should open mode favour? Evidence needed: the full 2025 paper.

## Does not transfer

Firm strategy, patents, R&D budgets, clusters and diffusion are organisational or market matters. Citation-based novelty needs a population of outputs and years to mature. Ambidexterity results rest on small firm surveys (41 firms in the lead study) and depend on organisational structure. Diversity-of-knowledge effects depend on team members.

## Sources

[V] means opened this session with WebFetch. [M] means memory or search snippet only.

1. [V] AcaWiki, Fleming on recombinant uncertainty: https://acawiki.org/Recombinant_uncertainty_in_technological_search
2. [V] arXiv abstract, Can Recombination Displace Dominant Scientific Ideas: https://arxiv.org/abs/2506.15959
3. [V] Wikipedia, Exploration-exploitation dilemma: https://en.wikipedia.org/wiki/Exploration-exploitation_dilemma
4. [V] Wikipedia, Organizational ambidexterity: https://en.wikipedia.org/wiki/Organizational_ambidexterity
5. [M] March (1991), Exploration and exploitation in organizational learning.
6. [M] Kaplan and Vakili (2015), The double-edged sword of recombination in breakthrough innovation, SMJ.
7. [M] Uzzi, Mukherjee, Stringer, Jones (2013), Science.

Opened sources: 4.
