# Critique: Organisational ambidexterity (E14.03)

Cross-check run 2026-11-19. Search tools: arXiv and Semantic Scholar APIs returned HTTP 429, so checks used OpenAlex and Crossref abstracts (new lines in evidence_x.jsonl, x01-x06). No WebSearch used. No PDFs downloaded.

## Corrections made
1. He and Wong 2004 citation count: a11 says 777 (IDEAS). Crossref gives 2934 and OpenAlex 4489. Use the larger counts; 777 is a single-database figure.
2. He and Wong 2004 abstract now read: N=206, interaction positive, imbalance negative for sales growth. Confirms a10/a11/b09. Coefficients still unread.
3. Mathias 2014 (b05 had no finding): the abstract says exploration and exploitation each have strong performance effects, and ambidexterity has WEAKER effects than either focus. This contradicts the founding story and is the most important missing number. Added as x01.
4. Cao, Gedajlovic and Zhang 2009 (a22/b13 had no substance): balance dimension vs combined dimension; synergy; balance helps resource-constrained firms, combined magnitude helps resource-rich firms. Added as x03.
5. Jansen 2006 abstract agrees in direction with all betas in a14/a15 (x05). Betas themselves not rechecked.
6. Gibson and Birkinshaw: a03 gives alignment-adaptability r=.50, b03 gives r=.54 for the same pair. Unresolved; treat as about .5. The 4234 vs 4195 respondent count stays flagged (working paper vs published).
7. Kula 2023: Crossref abstract confirms 19 studies/30 effects/11,246 and 22 studies/49 effects/98,630, and the direction (positive, significant). The g=0.771 figure was not in the abstract I could reach; keep it as b08 only.
8. Krishnamurthy 2024 and Binz and Schulz: abstracts agree with b17/c06/c12. The "over 60%" suffix-failure number and the t-values were not rechecked.
9. b21 and c04 report the same GPT-5 294 of 297 count; they are one source, counted once.
10. Ten checks attempted: Gibson and Birkinshaw (published abstract via Crossref had none), He and Wong, Mathias, Cao, Jansen, Kula, Krishnamurthy, Binz and Schulz, MACE abstract, Harris and Slivkins abstract. Abstract-level agreement for 8; MACE and Harris-Slivkins abstracts agree with c08 and c02 in direction. Full-text numbers (tables) could NOT be re-opened this run.

## Contradictions between sources
- Gibson-Birkinshaw (balance rises with performance) vs Mathias 2014 (ambidexterity weaker than focus) vs Clauss 2020 (ambidextrous strategy negative, N=150) vs Ebben-Johnson (N=300, balance worse). He and Wong (positive) and Kula g=0.77 point the other way.
- Likely reasons: different ambidexterity measures (product vs sum vs balance, per Cao 2009), same-source survey bias, resource level, environment.
- Kula g=0.77 vs Mathias: not reconcilable without moderator data; Kula used one author and limited databases.
- Structural vs contextual: only the Fourne et al. 2019 meta-analysis (European Management Journal) tests this directly. I saw its title only, no numbers. O'Reilly and Tushman (proponents of structural) and Gibson-Birkinshaw (proponents of contextual) both reviewed here are self-interested.

## Weak spots
- The founding study is 41 units, cross-sectional, perceptual performance; top-group advantage disappears with separate raters (4.11 vs 4.13).
- Junni 2013 and Fourne 2019 effect sizes never seen. Mathias 2014 and Wenke 2020 effect sizes never seen.
- No LLM or AI study tests structural vs contextual ambidexterity. LLM evidence is about exploration in bandits and evolutionary search, an analogy only.
- LLM evidence is toy tasks (two-armed delegation, bandits), small N, single papers. MACE, ShinkaEvolve and LoongFlow are vendor or preprint results; LoongFlow used 3 runs per arm.
- AI-in-firms surveys (a27, a28, c22) are about human firms using AI and are low-quality, self-report.

## Only seen in snippets or abstracts
He and Wong, Mathias, Junni, Cao, Jansen (partly), Raisch-Birkinshaw, Gupta et al., Fourne, Wenke et al., Chandrasekaran 2012 (via Wikipedia only), Tang et al. 2026 (c25 snippet), Harris and Slivkins full text beyond what c08-c11 recorded.

## GAPS
1. What are the pooled effect sizes (k, N, r) in Junni 2013, Mathias 2014, Fourne 2019 and Wenke 2020, and how do balance and product measures differ?
2. Fourne 2019: does the meta-analysis favour structural or contextual ambidexterity, and under which contingencies (size, dynamism, resources)?
3. Does a scaffold that forces an explore:exploit split beat explore-only and exploit-only at equal tokens on reasoning benchmarks? (No study found.)
4. Is there any LLM study that compares separate explorer and exploiter agents with one alternating agent (structural vs contextual analogue)?
5. Do the He and Wong coefficients (interaction, imbalance) replicate in non-manufacturing samples, and what is the effect size?
6. Does the 50.0% to 0.0% lock-in drop with external UCB (MACE) replicate on other model families and non-toy tasks?
7. How much of Gibson-Birkinshaw's stepwise gain survives objective performance data, e.g. the firm-level financials (r=.75 only at firm level)?
8. Does token or compute budget act like resource level (Cao 2009): does balance help at small budgets and doing both at high levels help at large budgets?
9. Which candidate-diversity controls (novelty rejection, island count) in evolutionary LLM search matter most? ShinkaEvolve had no island ablation.

## Gap search results

Run 2026-11-19. WebSearch budget was exhausted, arXiv API, OpenAlex and Semantic Scholar search were rate limited, and publisher pages (AOM, ScienceDirect, the Erasmus repository PDF) returned 403 or a bot challenge, which was not bypassed. Work used Semantic Scholar by-DOI abstracts, Crossref, arXiv HTML pages and arXiv listing pages. 20 new lines in evidence_d.jsonl (d01 to d20); claims.jsonl now has 23 claims (K18 to K23 new; K01, K05, K06, K09 to K14, K17 updated).

1. Pooled effect sizes (Junni, Mathias, Fourne, Wenke): STAYED OPEN. No r values obtained. Gained: Fourne 114 studies and 33,492 organisations; Mathias 117 studies and more than 21,000 firms; Wenke 2021 SME meta-analysis 34 studies and 5,488 SMEs (d01, d03, d05). Junni numbers still missing (d04). Balance vs product measures: not resolved.
2. Fourne: PARTLY CLOSED. Abstract says structural separation helps balance at all sizes, more in high-tech, and avoiding separation benefits service firms (d01, d02). Resource and dynamism contingencies, and coefficients, not seen. Note the outcome is balance, not performance.
3. Forced explore:exploit scaffold at equal tokens: STAYED OPEN. No study found (d20). Closest: depth-breadth allocation (d10, d11) and equal-token single vs multi-agent (d14).
4. Separate explorer and exploiter vs one alternating agent: PARTLY CLOSED as "closest analogues". d08 (strategy agent plus generation agent, one model, no numbers) favours the split on stability. d14 and d15 (role splits at equal tokens) favour the single agent: above 500 thinking tokens single beat every split on average; centralised multi-agent lost 28 points (CI -44 to -12) at 2.8 to 6.1 times the tokens. No direct explorer vs exploiter test.
5. He and Wong coefficients in non-manufacturing samples: STAYED OPEN. Only indirect hints: Fourne (service firms gain from avoiding separation) and Junni (b04, stronger link in non-manufacturing). Coefficients unreachable.
6. MACE replication: PARTLY. Same paper covers five named models (Qwen2.5-7B, GPT-4, GPT-5, Llama3.1-8B, Mistral-7B) and four QA benchmarks (d16). Independent work on frontier models and non-toy tasks (d09, 5 frontier LLMs, 7 chemistry datasets) shows a different but related failure: stated exploration intent about 92% of traces with near-zero realised novelty. The 50.0% to 0.0% lock-in figure was NOT found in the text read; treat as unverified (claim K12 annotated). No independent replication of MACE itself.
7. Objective performance data: PARTLY CLOSED. Uotila 2009 (S&P 500, archival financials) finds an inverted-U in exploration share with optimum moving with R&D intensity (d06). Lubatkin 2006 (139 SMEs, multisource) keeps a positive link (d07). The stepwise Gibson-Birkinshaw gain has not been re-tested on objective data. Both abstracts only; no coefficients.
8. Budget as resource level: PARTLY. Best allocation depends on task and model capability (d10), best search width rises with budget (d13), a weak model gains nothing from depth (d10). Not a clean Cao-style balance-small, both-large result; budgets here are call counts, not tokens.
9. Diversity controls: PARTLY. Diverse init and island selection give small gains within one SD on one task; island count not ablated in any paper found (d12, d17, d18). Which control matters most remains unknown.

New cautions: d08 reports no numbers and one model; d14 covers multi-hop QA only; d15 had a flawed write-execution rate in the multi-agent build; all new numeric finding for human firms (d01 to d07) are abstract-level only.
