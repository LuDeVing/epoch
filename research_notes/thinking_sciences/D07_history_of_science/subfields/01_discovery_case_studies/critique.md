# D07.01 Discovery case studies: cross-check critique

## Corrections and confirmations (sources re-opened this session as arXiv PDF text)
Confirmed exactly: LLM-SRBench 31.5% (LSR-Transform, LLM-SR GPT-4o-mini 31.53) and 239 problems; NewtonBench 324 tasks, GPT-5 75.9, Gemini-2.5-pro 65.4, hardest 40.3 and 16.7, code effect 73.3/40.9/18.9/14.7; DiscoveryWorld 66% / 55% / 11 of 16 tasks, 38% and 18% (ReAct), 34% and 8% (Hypothesizer); Si et al. 4.84 / 5.64 / 5.81, N=49, 79 reviewers, 298 reviews, 56.1% vs 50.0%, 200 non-duplicates of 4000; AI Feynman (Eureqa 71% basic, 15% bonus vs AI Feynman 90% bonus); ScienceAgentBench 32.4 / 34.3 / 42.2 / 10.8% / 17x; DiscoveryBench 264 + 903, 25%; MOOSE-Chem 96.7/83.7/60.8 and 4.020 vs 2.882/2.686/2.549, without multi-step 3.765; AI Scientist F1 0.57 vs 0.49, AUC 0.65 both, balanced acc 65 vs 66, 70% accuracy, correlation 0.14 between humans, under $15 per paper; Kosmos 79.4%; Shi et al. (arXiv 2610.24131, 16 Oct 2026) +0.70 [0.41, 1.03], 86/11/3, Ring -0.33.

Corrections and notes:
1. LLM-SRBench "28.1% on LSR-Synth" (a23, b08): the abstract says this, but in the table 28.12 is a single domain cell (LaSR GPT-4o-mini, material science, symbolic). Read it as a best single-domain value, not an average over LSR-Synth. The LSR-Synth domain values for LLM-SR GPT-4o-mini (11.1, 16.7, 9.9, 20.2) are lower.
2. DiscoveryBench "no-data guess about 13-16%" (c17): table shows NoDataGuess 15.4 / 15.6 / 13.5 for GPT-4o / GPT-4p / Llama-3, while CodeGen is 15.4 / 13.9 / 11.5. The no-data guess equals the code agent in this (garbled, interleaved) table. This is stronger than c17 states. The 25% best is ReAct (24.5), row mapping uncertain.
3. a17 had no NoDataGuess number; now filled (above).
4. AI Scientist (a25, b21, c19) look different but are the same paper with different metrics (correlation, F1/AUC, balanced accuracy). Not a contradiction.
5. The Faraday diary count 16,041 (b05) could not be re-confirmed: escholarship page is script-rendered. Keep as single-source.

## Contradictions between sources
- Reasoning scaffolds: a16 says DataVoyager gained from domain knowledge; c17 says ReAct and DataVoyager did not beat CodeGen. Different conditions (knowledge vs no knowledge). Status contested.
- Code tool helps weak models, hurts strong ones (NewtonBench), while ScienceAgentBench and LLM-SR show code loops help. Different task type (interactive probe vs fixed data). Not resolved.
- Seeming conflict: LaSR best on numeric, worst on symbolic. A metric effect, not an error.

## Weak spots
- The subfield's core sources were never opened: Nickles (1980) case volume, Kulkarni & Simon (1988) KEKADA, Langley et al. (1987), Holmes on Krebs, Gruber on Darwin (a01, a05, a28, c22-c25). All KEKADA and BACON facts are second-hand (SEP, Darden, Downes). There is no heuristic list, no experiment count and no operator sequence from any real discovery. This is the biggest hole, since the subfield's stated value is "operator sequences".
- Nearly all numbers are LLM benchmark results on equation discovery (one sub-area). Biology, chemistry wet-lab and theory-building cases are covered only by Co-Scientist (one case) and Kosmos (self-reported).
- Judges are LLMs in LLM-SRBench (GPT-4o), DiscoveryWorld (GPT-4o), ResearchBench, MOOSE-Chem; agreement figures come from the authors.
- Seen only in snippets or garbled tables: ResearchBench per-model numbers, LLM-SRBench Figure 4 gap magnitude, DiscoveryBench table row mapping, DiscoveryWorld figures beyond headline.
- No study tests a thinking schema or operator sequence mined from a historical case against a plain agent at equal tokens. Claims on schema parts are therefore hypotheses.
- Dunbar, Nersessian and Thagard claims are from SEP, not the papers.

## GAPS
1. What are the actual operator sequences in KEKADA (Kulkarni & Simon 1988): the heuristic list, number of experiments, and how it handled the surprise? Fetch the paper (and Holmes).
2. Do mined operator sequences (surprise check, change one variable, near analogy, look-back) improve an LLM at equal tokens on obscured historical cases, versus plain sampling? Any published ablation?
3. How large is the memory effect: what are the exact numbers for original vs transformed forms in LLM-SRBench Figure 4, and the NoDataGuess vs code-agent scores in DiscoveryBench per model?
4. Does sampling many independent runs beat structured scaffolds on discovery tasks at equal tokens (beyond Shi et al., one preprint with symbolic regression)? Replications?
5. What do notebook-based reconstructions (Krebs, Faraday, Darwin, Kepler) show about how often scientists changed method after an impasse, and how long they stayed stuck? Any counts?
6. Is there evidence that an LLM can detect and act on a surprising result (anomaly) in a data set, with measured rates, e.g. on DiscoveryWorld or in a Co-Scientist style run?
7. Where do failures in discovery agents concentrate (hypothesis, experiment design, interpretation)? Kosmos shows interpretation at 57.9%; are there independent breakdowns?
8. Do LLM judges of discovery quality (GPT-4o graders in DiscoveryWorld, LLM-SRBench) match humans at the level needed, and what do code-only checks lose?
9. Are there replications of Co-Scientist's cf-PICI rediscovery or leak checks showing it was not in training or public data?
10. What do Lugg-type critiques show about how far rational reconstructions (Hanson on Kepler) differ from real traces, with a measured difference rather than argument?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d18). Web search quota was exhausted and the arXiv, Semantic Scholar and OpenAlex search endpoints returned 429, so gaps that need a literature search could not be searched. Direct PDFs (arXiv, archive.org), Crossref and Wikipedia worked.

Status by gap:
1. KEKADA operator sequences: CLOSED from the primary tech reports (d01 to d04; archive.org copies of DTIC ADA203323 and NASA NTRS 19920016497). 64 heuristics (31 general, 33 domain-specific); surprise rule PG1/PC8; fixed explanation order; scope threshold of 3; five strategies. Caveats: results are typed in by the user, fit to Krebs is stated not measured, Holmes's book still unopened. Also found that the DOI cog1202_4 in a05/c24 is a different paper (Sweller); the correct one is cog1202_1.
2. Ablation of mined operator sequences versus plain sampling at equal tokens: OPEN. None found; search was unavailable. KEKADA itself has no ablation. The closest outside items (d16, d17) compare architectures at equal compute on non-discovery tasks.
3. Memory effect in exact numbers: PARTLY CLOSED. DiscoveryBench is fixed (d07): NoDataGuess 0.0 / 4.7 / 11.5 against CodeGen 15.5 / 16.3 / 12.1 (GPT-4o / GPT-4p / Llama-3). The earlier critique item 2 was wrong; the 13.5-15.6 values were ReAct and DataVoyager rows. LLM-SRBench no-data versus with-data is exact (d08), and NewtonBench shows no-data LSR-Transform rising to 29-35% for 2025 models (d09). The Figure 4 original-versus-transformed gap in points is still OPEN (values are in the plot, not in the text).
4. Independent runs versus structured scaffolds: OPEN, weakened. No replication found. Re-reading Shi et al. (d15) shows it is call-matched not token-matched, a 7B model, five data rows, no seed replication, and compares independent runs with peer-communication topologies, not with tool scaffolds. K09 changed from established to contested.
5. Counts from notebook reconstructions: PARTLY CLOSED. Dated Krebs timeline (d05): about 16 weeks to the first surprise, about 5 method shifts in 8.5 months. Kepler: at least 70 repetitions of one routine (d06, tertiary). Faraday and Darwin have no counts; Faraday 16,041 still single-source.
6. LLM surprise detection with rates: OPEN. Only an anecdotal NewtonBench trace where a model flags 'Key Anomaly Identified'; no rate. DiscoveryWorld does not measure it.
7. Where failures concentrate: PARTLY CLOSED. Two systems agree on interpretation as the weak step (Kosmos 57.9% vs 85.5% and 82.1%, d13; DiscoveryWorld procedure high, completion low, Reactor Lab regression 0.00, d12). Kosmos evaluators are collaborators and DiscoveryWorld's location is inferred from scores.
8. LLM graders versus humans: PARTLY CLOSED. LLM-SRBench: 123 of 130 (94.6%) raw agreement with two authors, no kappa (d10). DiscoveryWorld: human notes graded by hand, agents by GPT-4o, no agreement reported (d11), so the human-versus-agent knowledge gap is not like for like. What code-only checks lose is not measured.
9. Co-Scientist cf-PICI replication or leak check: OPEN. The paper reports n = 1 with no leak control (d14). Kosmos did a pre-cutoff rerun (d13). Search for outside replications was impossible.
10. Rational reconstruction versus real traces, measured: OPEN. Nothing measured found.

Corrections to earlier items and claims:
- Critique item 2 (NoDataGuess equals CodeGen) is wrong. Raw text reading gives NoDataGuess 0.0 / 4.7 / 11.5. Only Llama-3 comes near CodeGen. K20 rewritten, K05 relabelled (the 25% best is Reflexion with an oracle; best normal agent 16.3).
- K06 downgraded: the DiscoveryWorld unit tests are generic skills (dialog, doors, pick-and-place), not discovery sub-skills, so the 'parts work, chaining fails' reading is not supported.
- K09 contested; K07 given exact numbers (ReAct and DataVoyager do not beat CodeGen; DataVoyager GPT-4o is 5.7 vs 14.1 on DB-SYNTH).
- New claims K21 to K27 added. K27 lists what stayed open.

Next pass should first rerun four searches: operator-sequence ablations, anomaly-detection rates for LLM agents, measured reconstruction-versus-trace comparisons, and outside checks of cf-PICI. Also open Holmes (1980/1991) and render LLM-SRBench Figure 4.
