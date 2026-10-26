# Engineering design methods: subfields

Engineering design methods are taught procedures from need to working design. They divide into systematic design (Pahl and Beitz, VDI 2221), functional modelling and decomposition, TRIZ, morphological and creativity methods, axiomatic design, systems engineering, and design-space search. Teaching is common; controlled evidence is thin.

Opened facts. A Purdue paper reports two studies. Study 1: 25 novice teams compared top-down, energy-flow and enumeration decomposition; top-down and energy-flow gave similar results and enumeration did worse; diagramming helped teams reach consensus. Study 2: 78 reports from industry engineers; about half used decomposition, and use showed no correlation with final design quality. A survey (Van Eck, McAdams, Vermaas) finds no consensus view on functional reasoning across three models (Functional Basis, Function-Behavior-State, Functional Reasoning).

TRIZ evidence, stated plainly: the encyclopedia entry I opened offers only corporate and anecdotal claims (several tagged as needing sources) and no independent evaluation. A 2018 design-conference paper on integrating TRIZ with systematic design says case studies, interviews and surveys would be needed to study benefits. I could not run the extra search for controlled TRIZ studies (search budget refused it), so I cannot say none exists; I found none in what I opened.

## Subfields

| Subfield | What it studies | Key people or works | Useful for our agent | How |
|---|---|---|---|---|
| Systematic design | Staged process | Pahl and Beitz; VDI 2221 | Med | S1, S2 |
| Functional decomposition | Overall function into sub-functions | Stone and Wood; Van Eck et al. | High | O3; Purdue evidence |
| TRIZ | Contradiction matrix, 40 principles, ideal final result | Altshuller | Med | O4 and O8 as typed reframes; evidence anecdotal |
| Morphological analysis | Table of options, combine | Zwicky | Med | S3 open mode, code enumerates |
| TRIZ with systematic design | Fixing creativity gaps in FDM | Fiorineschi, Frillici, Rotini 2018 | Med | Notes FDM gives non-comprehensive creativity support |
| Axiomatic design | Independence axiom | Suh | Low | Selection idea |
| Bio-inspired and analogical design | Retrieval of analogues | Helms, Goel; Chakrabarti | High | O7 |
| Design-space exploration | Search, trade-offs | Papalambros; Deb | Med | S7 select |
| Empirical design research | Metrics of ideation | Shah et al. 2003 | High | What to measure |

## Deep research

One folder per subfield in `subfields/`. Read `DEEP.md` first; section 7 is what the agent should take, section 8 the tests. `UNKNOWNS.md` lists what we don't know and must test before adding.

| Subfield | Deep document | Status |
|---|---|---|
| Systematic design | | not started |
| Functional decomposition | [`subfields/02_functional_decomposition/DEEP.md`](subfields/02_functional_decomposition/DEEP.md) | done, batch 5 (2026-10-27) |
| TRIZ | | not started |
| Morphological analysis | | not started |
| TRIZ with systematic design | | not started |
| Axiomatic design | | not started |
| Bio-inspired and analogical design | | not started |
| Design-space exploration | | not started |
| Empirical design research | | not started |

## Dig into next

**1. Functional decomposition strategies.**
- Why did top-down tie with energy-flow and beat enumeration?
- Can an LLM produce a decomposition whose parts code can check (each part solvable alone, parts combine)?
- Evidence: the Purdue studies, our decomposition solve rate by class.

**2. TRIZ contradiction as a typed reframe.**
- Does stating a contradiction (improve A, B worsens) make an LLM produce more distinct candidates?
- Evidence: need a literature search for controlled TRIZ studies (the Spreafico and Russo 2016 survey of TRIZ industrial case studies, cited in the 2018 paper, is a lead), then an equal-token test by distinctness.

**3. Analogical retrieval.**
- Which retrieval and mapping steps get far analogues that help?
- Evidence: Helms and Goel work, F05 results on variance.

## Does not transfer

Prototyping, manufacturing, cost, standards, safety and customer processes are physical or institutional. Process models (V-model, stage gates) manage organisations; for a single answer they add setup cost, which G7 forbids unless they pay for themselves. Decomposition's measured benefit was team communication, a human matter.

## Sources

[V] = opened and read this session. [M] = search result only, or from memory. Opened: 4. The extra TRIZ search was refused by the budget.

1. Purdue, Empirical studies of functional decomposition in early design (abstract page). https://pure.psu.edu/en/publications/empirical-studies-of-functional-decomposition-in-early-design/ [V]
2. Van Eck et al., functional decomposition survey. https://scholarsmine.mst.edu/mec_aereng_facwork/5841 [V]
3. TRIZ (encyclopedia entry). https://en.wikipedia.org/wiki/TRIZ [V]
4. Fiorineschi, Frillici, Rotini 2018, Supporting systematic conceptual design with TRIZ (PDF text read). https://designsociety.org/download-publication/40519/SUPPORTING+SYSTEMATIC+CONCEPTUAL+DESIGN+WITH+TRIZ [V]
5. Springer 2024 metrics paper. https://link.springer.com/article/10.1007/s00163-024-00434-w [M]
6. Pahl, Beitz et al., Engineering Design. [M]
7. Spreafico and Russo 2016, TRIZ industrial case studies: a critical survey, Procedia CIRP 39 (cited in source 4; not opened). [M]
