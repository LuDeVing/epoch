# A06.05 Schemas: cross-check critique

## Re-opened sources (numbers confirmed)
1. Anderson and Pichert (1977), ERIC ED142974 PDF: shifters +7.1%, no-shift -2.9% less, F(1,35)=9.57, p<.01. Confirmed (a11).
2. Sweegers et al. (2015), PMC4659923: congruent face-home matches 34.65 (SD 1.44) vs incongruent 28.21 (SD 6.8x). Confirmed (b08). d-prime figures not re-checked.
3. Wang et al. (2026), arXiv 2610.27406 full text: anti-persistence best in all nine settings, joint memory in eight, abstraction/joint below trajectory in seven of nine, Reflexion 52.9%. Confirmed (a29). Paper itself warns the nine settings are not independent observations.
4. Lee et al. (2024) ReadAgent, arXiv 2402.09727 full text: gist compression 85.53%, ReadAgent-P 86.91%, ReadAgent-S 87.17%, MemWalker re-implementation 66.73%, raw text 85.83%. Confirmed (c09). Note: the appendix also quotes ReadAgent-P (1-5 pages) at 86.63%, so the headline 86.91% is the best of several look-up limits.
5. Kwon (2026), arXiv 2606.25449 full text: 27% to 59% (8B) and 0% to 49% (Opus) wrong-time emission confirmed (c11). The same text shows frontier models at 0.00 wrong emission in some soft/hard conditions, so the effect depends on prompt design.
6. Abstract pages re-opened for Kumar (a28/c16), Perez (b01), Xie (c04), ExpeL (c20): titles and the qualitative direction match. Per-table numbers not re-checked.

## Corrections and cautions
- a28 and c16 are the same paper (Kumar et al. 2024); counted once in independence. The reported GPT-4 t(198)=-7.01 sign is odd (text says velocity is higher in multimodal chains for GPT-4 too); keep "as reported".
- a29 and c13 are not independent measures of the same effect, so K09 is single-source.
- c17 was never opened; K07 uses it only as a pointer.
- Bartlett counts (a03, a04, a06): the archive.org item could not be re-opened this pass (item not found), so they stay as first recorded.

## Contradictions
- Congruent items are learned faster (b08 learning phase) but incongruent items have higher recognition d-prime (b08), while others (a31, a33, b14) find congruent advantages for associative memory. Outcome depends on test type and delay.
- Cockcroft et al (b09) found weak or absent schema clustering memory effects; most other lab studies report clear effects.
- Abstraction memory helps in AWM, ExpeL, BoT (c18-c20) but hurts in Wang et al. (a29). Seeded wrong rules, not the abstraction itself, are likely the difference; untested.
- c04: LLMs are both receptive (coherent counter-evidence) and stubborn (substitution evidence).

## Weak spots
- Founding studies (Bartlett replications, Brewer and Treyens) have no verified numbers (a17, b25 unopened). This is the largest hole in the "founding studies with exact numbers" requirement.
- Alba and Hasher (1983), Rumelhart (1980), Roediger and McDermott, Hintzman are unopened.
- Many 2026 sources are preprints (PsyArXiv, arXiv) not yet peer reviewed.
- No LLM study tests Bartlett's design directly (serial recall of a culturally foreign story with and without a schema prompt).
- Agent benchmarks reported without equal-token controls.

## Only seen in snippets or metadata
a17, a19-a24, a26, a34, a35, b22-b33 (except abstracts), c17.

## GAPS
1. What are the exact N and intrusion rates in Brewer and Treyens (1981) (recall and recognition of the office objects), and has it been replicated with LLM agents?
2. Does a seeded wrong schema/rule in agent memory persist longer than a seeded wrong raw fact at equal tokens (tests Wang et al. against AWM/ExpeL)?
3. Does a "source-first" note policy (keep derivation, not only conclusion) beat summary-only notes on correction recovery across more than one task family?
4. Do LLMs reproduce Bartlett-style distortion (rationalisation, omission of culturally foreign details) in single-step recall of unfamiliar stories, and how does it scale with delay or context length?
5. What do Gauld and Stephenson (1967), Wynn and Logie (1998), and Bergman and Roediger (1999) report in numbers, and how large is the instruction effect on distortion?
6. Does an explicit "list the assumed defaults" or "state what the text did not say" operator reduce gap-filling errors in counterfactual and stereotype tasks at equal tokens?
7. Which schema-violation items does LLM summarisation drop or over-keep (surprise vs congruence), and does that match the human mixed results?
8. Is there a human-and-LLM meta-analysis of schema-congruency effects on memory (Rojahn and Pettigrew 1992 numbers, newer work)?
9. Does repeated self-summarisation drift (attractor strength) matter at the agent context lengths we use, and does tagged provenance slow it?
10. Can LLM-estimated semantic centrality (b20) be used as a cheap flag for notes likely to be distorted?

## Gap search results
Search conditions: WebSearch quota was used up; arXiv and Semantic Scholar search APIs returned 429 and OpenAlex had no budget. Discovery went through DataCite, Europe PMC and Crossref; papers were opened on arxiv.org and PMC. Evidence is in evidence_d.jsonl (d01 to d17); claims K22 to K29 added; K02, K06 to K10, K17, K18, K21 got new evidence ids.

1. Brewer and Treyens numbers: OPEN. Paper is closed access; only secondary pages read (N reported as 86 in one place, 30 in others; no intrusion or recognition rates). No LLM replication found. (d01)
2. Wrong rule vs wrong raw fact at equal tokens: OPEN, partial. ACE shows seeded harmful bullets in an abstraction playbook cost 4.0 points only when injected every step (d10); Xiong and MINJA show wrong raw records are replayed (d12, d13). No study has both arms. Wang et al. versus AWM/ExpeL remains unresolved.
3. Source-first notes across task families: PARTLY CLOSED as evidence of direction. Nakayashiki (16 models, three runs) and PlanFence (30 workflows) show derivation links help only if checked (d11, d15); neither compares source-first with summary-only notes directly. Kwon's single setting still stands alone for that comparison.
4. Bartlett-style single-step LLM recall and scaling with delay: OPEN. No direct study found. Nearest are Perez (50-step chains, d05) and Kumar (grids, d06); "Who Remembers What" (700 five-step chains) was abstract only (d16).
5. Gauld and Stephenson, Wynn and Logie, Bergman and Roediger numbers: OPEN. Bergman and Roediger abstract read (replicated; 15 min, 1 week, 6 months, no N; d02). The other two were not reachable (d17). Instruction effect size unknown.
6. "List the assumed defaults" operator: OPEN. Wu et al. shows the default-world gap survives comprehension checks, CoT and 16 examples (d08), but nobody tested the operator.
7. Which schema-violating items LLM summarisation drops: PARTLY CLOSED. Acerbi and Stubbersfield, full text read: stereotype-consistent over inconsistent (beta 0.058), negative, social and threat kept, ambiguity resolved negatively (d04). Direction matches the "congruent kept" side of the human results; surprise-driven keeping was not tested.
8. Meta-analysis of congruency: CLOSED for the old one. Rojahn and Pettigrew (1992): 60 studies, 165 tests, slight inconsistent advantage, direction set by test type (d03). Stangor and McMillan 1992 and any newer meta-analysis not found or opened. Abstract only.
9. Self-summarisation drift at agent context lengths: PARTLY CLOSED. ACE saw a 18,282 to 122 token collapse in one rewrite (d09); Perez shows drift over 50 steps (d05). No provenance-tagging condition tested.
10. LLM-estimated semantic centrality as a distortion flag: OPEN. Nothing new found; b20 remains the only source.

New caveats: d11 and d15 are single-author or small preprints; Wang/Kwon-type claims remain uncontrolled for tokens. Statuses changed: K17 text notes numbers still unverified; K29 added with status "open" (no direct LLM Bartlett or office-study test found).
