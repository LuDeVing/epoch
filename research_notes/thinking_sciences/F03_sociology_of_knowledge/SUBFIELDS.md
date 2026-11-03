# Sociology of knowledge: subfields

This field asks how communities come to treat some claims as knowledge: who is trusted, which methods count, how disputes close. It began with Mannheim and Merton, grew into the sociology of scientific knowledge (SSK) and the Strong Programme, then laboratory studies, actor-network theory, and the philosophical social epistemology. Stanford's entry on social epistemology now lists twelve areas, several of them formal models of communities. Most of the field concerns institutions and power. A few formal results (network structure, aggregation, division of labour) bear on how a single system should spread and combine its attempts.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Sociology of science and Merton's norms | Communism, universalism, disinterestedness, organised scepticism (CUDOS); counter-norms found by Mitroff | Merton 1942; Mitroff 1974 [V] | Med | Guardrails: universalism (judge by impersonal criteria) resembles blind judges (G5); scepticism resembles G3 |
| Strong Programme and SSK | Social factors shape all beliefs, true or false; symmetry; Edinburgh and Bath schools | Bloor, Barnes, Collins [V] | Low | Background |
| Laboratory studies and ANT | Daily practice that produces facts; humans and objects as actors | Latour and Woolgar; Knorr Cetina; Latour [V] | Low | Background |
| Network epistemology | Communication structure of a community; more communication can hurt (Zollman effect) | Bala and Goyal; Zollman; Mayo-Wilson et al. [V] | High | G4 and S3: fresh, isolated attempts; limit cross-talk |
| Division of cognitive labour | Spreading effort over approaches; priority rule | Kitcher 1990; Strevens; Muldoon and Weisberg [V] | High | S3 open mode: code allocates untried directions |
| Epistemic diversity | Diversity versus ability; epistemic landscapes | Hong and Page; Weisberg and Muldoon [V] | Med | Diversity of attempts, but G4 limits benefit from one model |
| Judgment and credence aggregation | Doctrinal paradox, pooling, Condorcet Jury Theorem | List and Pettit; Genest and Zidek [V] | High | S7 select: aggregation rules in code; Condorcet needs independence (G4) |
| Testimony, trust and peer disagreement | When to trust others; equal weight view | Hardwig; Christensen; Kelly [V] | Low | Background |
| Peer review and replication | Biases; replication rare; contradicted results persist | Ioannidis; Lee et al. [V] | Med | G3: held-out checks as replication |
| Values and inductive risk | Weighing the cost of error when accepting claims | Rudner; Douglas [V] | Med | Decision thresholds by error cost |
| Group belief and justification | Group agents, joint commitment | Gilbert; Lackey; Goldman [V] | Low | Not relevant |
| Epistemic injustice and misinformation | Credibility deficits, echo chambers | Fricker; Nguyen [V] | Low | Not relevant |
| Kuhn and paradigm crisis | Anomalies accumulate until a framework is replaced | Kuhn 1962 (from memory; Wikipedia SSK page names him an influence) | Med | S6 trigger idea: switch frame after several independent failures |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Sociology of science and Merton's norms | [`subfields/01_sociology_of_science_and_merton_s_norms/DEEP.md`](subfields/01_sociology_of_science_and_merton_s_norms/DEEP.md) | done, batch 8 (2026-11-01) |
| Strong Programme and SSK | | not started |
| Laboratory studies and ANT | | not started |
| Network epistemology | [`subfields/04_network_epistemology/DEEP.md`](subfields/04_network_epistemology/DEEP.md) | done, batch 7 (2026-11-01) |
| Division of cognitive labour | [`subfields/05_division_of_cognitive_labour/DEEP.md`](subfields/05_division_of_cognitive_labour/DEEP.md) | done, batch 7 (2026-11-01) |
| Epistemic diversity | | not started |
| Judgment and credence aggregation | [`subfields/07_judgment_and_credence_aggregation/DEEP.md`](subfields/07_judgment_and_credence_aggregation/DEEP.md) | done, batch 7 (2026-11-01) |
| Testimony, trust and peer disagreement | | not started |
| Peer review and replication | | not started |
| Values and inductive risk | | not started |
| Group belief and justification | | not started |
| Epistemic injustice and misinformation | | not started |
| Kuhn and paradigm crisis | | not started |

## Dig into next

**1. Network epistemology and division of labour.**
- The Zollman effect says more communication can hurt a community's learning. Does it predict that cross-talk between attempts lowers accuracy of the final pick?
- Can code assign directions so effort is spread as Kitcher-style models suggest? Weisberg and Muldoon's work says those models are not robust, so test it.
- Evidence needed: Zollman and Bala and Goyal models, our open-mode logs.

**2. Aggregation.**
- Which pooling rules (linear, geometric) suit candidate scores, and when does Condorcet's independence assumption fail for samples from one model?
- Evidence needed: List and Pettit, Genest and Zidek, our agreement-versus-correct data.

**3. Norms as checks.**
- Which of universalism, scepticism and replication translate into checks code can run?
- Evidence needed: Merton's text, replication studies, our G3 results.

## Does not transfer

Power, status, funding, reputation, rhetoric, institutions, injustice and trust between people are human matters. The relativist claims of SSK are not a procedure; critics say SSK ignores objective reality and note the science wars. Models of scientific communities assume agents with careers and credit, which a model lacks. The SEP entries are broad surveys, and only their first 100,000 characters were read.

## Sources

[V] means the page was actually opened (fetched and read) this session. [M] means seen only in search results or from memory.

1. [V] Social epistemology, Stanford Encyclopedia https://plato.stanford.edu/entries/epistemology-social/
2. [V] Social dimensions of scientific knowledge, Stanford Encyclopedia https://plato.stanford.edu/entries/scientific-knowledge-social/
3. [V] Sociology of scientific knowledge, Wikipedia https://en.wikipedia.org/wiki/Sociology_of_scientific_knowledge
4. [V] Mertonian norms, Wikipedia https://en.wikipedia.org/wiki/Mertonian_norms
5. [M] Division of cognitive labor and its critics (search results) https://web.sas.upenn.edu/weisberg/?p=106
6. [M] Kuhn 1962; Merton 1942; Kitcher 1990 (no URL)
