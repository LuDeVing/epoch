# Critique: Team science (E15.04), cross-check

## Re-opened sources (this session, full text via arXiv PDF)
1. Wu, Wang, Evans 2019 (arXiv 1709.02445): CONFIRMED 70% / 30% / 50% drop from 1 to 50 members; 72% more likely top-5% disruptive (solo vs 5-person); 10-person 50% more likely hit; Sleeping Beauty index 4x; two thirds within-person (beta -0.00018 vs -0.00027).
   CORRECTION: the arXiv abstract says "more than 50 million" works (a01 right); b02 says 65 million and 1954-2014 (likely the Nature version). Cite 50M for the arXiv text, 65M only for the published abstract, and do not mix.
2. Kim et al. 2025 (arXiv 2512.08296 v3): CONFIRMED +80.8% to -70.0%, 260 configs, SWE-bench degradation, ceiling threshold about 0.45 raw, beta -0.236, error amplification 4.4/7.8/17.2.
   CORRECTION: R2 0.373 is with the Intelligence Index and 0.413 with the Agentic Capability Index (ACI); evidence a22 words it as "0.413 with a capability metric" which is right only for ACI. Also the overall mean multi-agent change is -0.3% (95% CI -58.7 to +77.2), a useful headline not in the evidence.
3. Cemri et al. 2025 MAST (2503.13657): CONFIRMED 41% to 86.7%, 44.2/32.3/23.5, kappa 0.88, +9.4% for the final-say change. The text ties +9.4% to a workflow adjustment (CEO final say); c08 says role specification. Treat the +9.4% attribution as ambiguous.
4. Li et al. 2025 Self-MoA (2502.00674): CONFIRMED 6.6 points on AlpacaEval 2.0.
5. Li et al. 2024 Agent Forest (2402.05120): CONFIRMED GSM8K gains 12% to 24%.
6. Holst et al. 2024 (2402.14583): CONFIRMED 972,161 papers, 142,362 patents, 97% and 78% zero references, 98%/93% of 100 sampled actually had references in the PDF. The paper says the decline is "negated" for papers and "substantially reduced" for patents (a16 is slightly stronger than that for patents).
7. Hao et al. 2024/2025 AI and science (arXiv 2412.07727): NOT CONFIRMED. The arXiv text gives 27,405,011 papers with +98.70% annual citations and 41.3M target papers; the multipliers 3.02x, 4.84x, 1.37 years, F1 0.875 are from the Nature version (DOI 10.1038/s41586-025-09922-y) and were not seen. Keep as single-source.
8. Bertalanic and Fortuna 2026 (2606.02646): CONFIRMED functional form, ceiling 1/c, Qwen 32B c = 0.96/0.77/0.97 vs 7B 0.85/0.57/0.81.
9. Fortunato et al. 2018 / 17% per decade: NOT RE-OPENED. Rests on Wuchty 2007 (a24, b26), which no agent read. Mean 1.9 to 3.5 over about 45 years would give about 14-15% per decade compounded, so 17% needs checking.
10. Lin, Frey, Wu 2023: not re-opened (OpenAlex search only found it exists; Semantic Scholar rate-limited).

## Contradictions between sources
- Lin 2023 counts: a14 says 20M papers / 4M patents and 28% to 22%; b03 says 20,134,803 / 4,060,564 and D-score percentile 89 to 84. Different metrics (share with D>0 vs percentile), not necessarily conflict, but unreconciled.
- Debate: Du 2023 reports debate beating majority vote; Smit, Wang, Zhang 2024-25 find it does not at equal compute. Heterogeneous debate helps (Zhang) while mixing models hurts MoA (Li). Not truly contradictory: debate vs mixing differ, and quality gaps between models matter.
- Topology: MacNet says irregular graphs best; Kim says centralised contains errors and decentralised helps only on parallel search. Different tasks and metrics.
- Large teams: Lariviere says more authors, more citations; Wu says less disruption. Both consistent (impact vs disruption) but they use different outcomes.
- Super ties: Petersen says benefit; DBLP study (b09) says weak ties align with higher h-index.
- The 17% number appears twice with different meanings (team growth per decade vs Petersen citation boost 1.17). Do not conflate.

## Weak spots
- All human team-science evidence is observational and citation-based. Disruption (CD index) is shown fragile by Holst; Wu's team-size result was not itself tested by Holst, but it uses the same index and inherits the zero-reference risk. No independent replication of Wu 2019 found.
- Petersen (473 careers, two fields) is a small sample; super-tie effect on productivity is only 5.2%.
- Many LLM results are 2025-2026 preprints (Bertalanic, Mieczkowski, Riedl, Kim) without peer review; several use 7B-32B open models, so the ceiling may not carry to frontier models. Kim's own R2 is only 0.37 to 0.41.
- Exact scores for Smit 2024 (b17) and Wang 2024 (b18) were not extracted.
- Wuchty 2007, Guimera 2005, Jones 2009, Fortunato 2018 (a24-a27, b26) were recalled only, not opened.
- No LLM study maps directly onto the 17%-per-decade growth or complementary super-ties; the link is by analogy (team size, role complementarity, persistent partners).
- Only snippet-level: a15 Lin role numbers, b08 to b11 PMC items (abstract-level), c14 MARBLE agent-count numbers.

## GAPS
1. Does the Wu 2019 disruption-by-team-size result survive Holst-style zero-reference filtering? (Rerun on the same data with CD5=1 zero-reference entries removed; most decision-relevant for the human-side claim.)
2. Is 17% per decade in Wuchty 2007 / Fortunato 2018 exact, and over which fields and years?
3. At equal tokens, does one agent with diverse restarts plus a merge beat a single deep chain on novelty? (No LLM study measures disruption-like novelty against team size.)
4. At which single-agent accuracy does branching stop helping for frontier models (Kim's 0.45 ceiling), and does it hold above 32B open models?
5. Does persistent complementary role pairing (super-tie analogue) beat fresh roles per call in LLM teams? No study found.
6. Which MAST failure modes appear in a single-agent scaffold's own traces, and do role/stop rules cut them?
7. Are the Hao et al. Nature multipliers (3.02x papers, 4.84x citations) correct, and do they hold after controlling for selection of who adopts AI?
8. Is the Ringelmann ceiling (Bertalanic) reproduced by independent groups on frontier models?
9. Reconcile Lin 2023 counts and metrics, and test whether remote penalty is replicated outside Wu's group.
10. Why does heterogeneous debate help (Zhang 2025) while heterogeneous mixing hurts (Li 2025)? Is it a quality-gap effect?

## Gap search results (gap searcher, 2026-11-19)
Search note: WebSearch budget was exhausted and the arXiv, OpenAlex and Semantic Scholar APIs were rate-limited, so gaps 3 and 5 (which needed new literature search) could not be searched. Work used full-text PDFs and pages. Evidence in evidence_d.jsonl (d01-d16).

1. Wu 2019 vs Holst filtering: STILL OPEN. Holst cites Wu only in references and does not rerun team size (d15). Wu's SI has author fixed effects, topic, journal and review-exclusion checks and reference-based measures, but no stated zero-reference filter (d16). Nobody has rerun it; risk real but unmeasured.
2. 17% per decade: PARTLY CLOSED. Fortunato 2018 gives 17% citing Wuchty 2007 and Jones 2009, with no years or fields (d01). Wu SI: papers 2 to 5.5 over 1954-2014 (about 18% per decade by our arithmetic) and patents 1.7 to 2.7 (about 13%) (d02). Jones 2009: patents 1.73 to 2.33 over 1975-1999 (about 13%) (d03). Wuchty body paywalled; only the abstract was read (d04). So 13-18% is the safe range, 17% is a review average. The same review also uses 17% for a citation boost (K26).
3. Single agent with diverse restarts vs deep chain on novelty: STILL OPEN (no search possible). Indirect: Self-MoA says in-model sampling of the best model beats cross-model mixing (d11).
4. Does Kim's 0.45 ceiling hold for frontier models: PARTLY CLOSED. The fit includes GPT-5, Sonnet 4.5, Gemini 2.5 Pro and held-out frontier error is small on one benchmark, but the authors call it preliminary and no sweep varies one frontier model across accuracy (d08).
5. Persistent complementary roles vs fresh roles in LLM teams: STILL OPEN (no search possible).
6. MAST modes in single-agent traces: PARTLY CLOSED on the question of which modes apply. Modes 1.3, 1.5, 3.1, 3.2, 3.3 do not need a second agent; verification step +15.6%, role spec +9.4% (d12). No single-agent trace study found. Also note MAST category shares are inconsistent inside the paper.
7. Hao multipliers: CLOSED for existence. The arXiv v4 (Nature-accepted text) contains 3.02x, 4.84x, 1.37 years, 4.63% (d05). Selection control: matching on early trajectory leaves +24.45% citations and +9.61% productivity at year 10 (d06). So the earlier NOT CONFIRMED in item 7 above is superseded. Causal share still unproven.
8. Independent replication of Ringelmann ceiling: STILL OPEN. Single group; frontier part is a prediction with Gemini 3.1 Pro run at N=1 only (d13).
9. Lin 2023 counts: CLOSED. Raw 28% to 22% (papers), 67% to 55% (patents); controlled 20.4% to 19.5% and 58.2% to 56.5%; percentile 89 to 84 and 76 to 67 are three separate metrics (d14). Replication outside Wu's group: STILL OPEN.
10. Heterogeneous debate helps, mixing hurts: LARGELY CLOSED. Zhang's baseline is the average of two similar models; Li's is the best single model; quality outweighs diversity in Li's fits; Kim shows family-dependent effects (d09-d11). Not a contradiction, but a quality-gap plus baseline effect.

Corrections to earlier items: item 3 (+9.4% attribution) is settled, +9.4% is role spec and +15.6% is the verification step (d12). Item 7 multipliers now confirmed in arXiv v4.
