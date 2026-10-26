# Critique and cross-check: Wargaming (E12.02)

Cross-checker pass. Sources re-opened from local text of the PDFs (Green 2005, Armstrong 2002, Rivera 2024, Lamparth 2024, Elbaum and Panter 2025, WGSR-Bench, Matlin 2026, Riedl and Matlin 2026, Richelieu, COA-GPT, Shrivastava 2024). PDFs deleted afterwards.

## Numbers confirmed (re-read in source text)
- Green 2005: 101 forecasts by 23 game theorists 31%; 354 unaided student forecasts 31%; 105 simulated-interaction forecasts 62%; error cut 47%; permutation P=0.004; combining gave accurate forecasts in 7 of 8 (modal game-theorist forecast right in 3 of 8). (b01-b04)
- Armstrong 2002: 28% for chance, unaided judgement and game theory vs 61% for role playing once the non-interactive case is dropped; Wilcoxon P=0.03; over 1100 participants. (b06)
- Rivera 2024: GPT-3.5 neutral escalation 10.15 to 26.02 (+256%). (a09, b08, c01)
- Lamparth 2024: 214 experts, 48 teams, 21 actions; LLM frequency matches humans on 16 (GPT-3.5), 10 (GPT-4), 9 (GPT-4o). (a11, b14, c05)
- Elbaum and Panter 2025: 6.37 baseline, 3.96 at T=0.5, 3.33 at T=0.01, 4.61 planning prompt, 2.76 de-escalation prompt, final-day 11.1 vs 6.7 and 6.5. (a20, b11, b12)
- WGSR-Bench: 85.9% vs 37.5% complex situation analysis; 85.7 / 85.5 / 77.9 humans vs 49.1 R1 on opponent modelling; 92.3 / 80.7 vs 60.0 policy generation; 84.0 vs 83.3 and 45.2 vs 87.8 long vs short reward. (a21, a22, b23, b24, c22, c23)
- Matlin 2026: 223 studies, 20 (9%) both-creative, 4 of 63 core, 152 (68%) autonomous, 19 (8.5%) human in loop, single coder with LM help, no reliability. (a23, b20)
- Shrivastava 2024: GPT-4 most inconsistent; semantic-preserving ablations comparable to T=0.2 sampling for all models except GPT-4. (a18, b19, c12)
- COA-GPT: best variant 3.4% below the human expert mean; 112 thousand battles for the RL baseline. (a15)

## Corrections made
1. **c19 (Richelieu) mixed two tables.** Win 6.83% vs Cicero 6.03% is the Cicero table (Most SC 8.63 vs 6.90, Survived 39.95 vs 41.87, Defeated 44.60 vs 45.20). The figures Most SC 18.33 vs 4.10, Survived 38.27 vs 32.90, Defeated 34.30 vs 61.37 are from the AutoGPT table (win 9.10 vs 1.63). The edge over Cicero is small, with no significance test, and Richelieu survives slightly less often than Cicero. Claim K17 uses the corrected split. Evidence line c19 should be patched.
2. **b09 said "prompt sensitivity analyses reported no significant change" in Rivera.** The appendix says the GPT-3.5 No-Goals and Low-Stakes prompt variants did significantly reduce severe actions; most other variants did not. K06 uses this.
3. **b19 said prompt-rewrite inconsistency "exceeded" sampling inconsistency at T>=0.2.** The paper says meaning-preserving rewrites are comparable to T=0.2 sampling (GPT-4 lower). Claim K04 uses the corrected wording. c12 contains the same loose phrase ("any temperature above 0.2 gave more inconsistency than rewrites"), which is true only for T above 0.2.
4. **a11 and b14 say "no significant difference on 16/10/9 actions"; paper says the LLM "statistically matches" on these. b14 also says LLM teams were built from the first 107 players' backgrounds; not re-checked.** No numeric change.
5. **b06 (Armstrong 2002) audits Green's earlier 6-situation study, not the 8-conflict 2005 paper.** The 61% vs 28% and the 8-conflict 62% vs 31% are different datasets, not a replication of each other. In K01 they count as two reports from one research programme (partly independent only by the auditor). No outside lab replication of the role-play result was found.
6. **c02 per-scenario means (9.78/11.83/11.83 etc.)**: the PDF table row labels are offset (scenario names sit on the middle row of each block), so the neutral/invasion/cyberattack assignment of those means is uncertain. Do not cite per-scenario values from c02 without re-reading the table.
7. **a26-a28, c28-c30 stay unopened leads.** a26 (Green and Armstrong 2011) was not opened; Green 2005 is the opened evidence for the same claim.

## Contradictions between sources
- Rivera: the same-model simulation always escalates. Elbaum and Panter: with a 7B model, escalation depends strongly on temperature and prompt. Not a contradiction of the direction, but of how stable it is.
- Lamparth: newer models (GPT-4, GPT-4o) matched human action frequencies on fewer actions than GPT-3.5. WGSR-Bench and others imply stronger models are better. So "better model" does not mean "closer to human wargame behaviour."
- Hua (WarAgent) reports high fit to history; the same paper's authors note memory. Fit does not equal prediction.
- Dialogue: Lamparth says simulated dialogue is thin and agreeable; Richelieu-style systems use structured modules (opponent model, reflection) and gain. The difference is structure, not more voices.

## Weak spots
- Almost every LLM number comes from a handful of papers (Rivera, Lamparth, Shrivastava, Yin). Lamparth and Shrivastava share an author group. Independence is low across the board.
- Only Green/Armstrong tests accuracy against real outcomes. All LLM studies measure similarity to humans, escalation score, or consistency, not whether the wargame found a real weakness.
- Elbaum and Panter is a 7B model, one scenario, 10 runs per cell.
- WGSR-Bench scores policy generation with an LLM judge; human groups are college volunteers.
- Matlin counts are single-coder.
- No source tests the target use directly: a wargame step added to a single LLM agent's plan at equal tokens. Practice is ahead of evidence (b26).
- Founding historical material (Kriegsspiel, Naval War College 1894, Perla) rests on Wikipedia and one Schuurman article; Perla and Naval War College primary text was not opened. No numbers exist for outcome effects.

## Seen only in snippets or secondhand
- Emery 2021, Brewer and Blair 1979 (computer-run escalation): secondhand through two LLM papers.
- Davis and Stan 1984 RAND RSAS: secondhand through Snow Globe.
- Jensen et al. (actor identity effects): secondhand through Elbaum and Panter.
- Lin-Greenberg et al. 2022 and Lin-Greenberg 2022: abstract or Crossref only.
- Cicero, as cited in Richelieu.
- Sun et al. 2023 win rates: figures only, not extracted.
- WarAgent counterfactual trigger rates: tables garbled.

## GAPS
1. Does adding a separate-call adversary or wargame step to an LLM agent's plan improve plan quality at equal tokens? No study tests this. (Our own A/B with seeded flaws.)
2. Is there any outside-lab replication of Green's role-play advantage (62% vs 31%), and does it hold for LLM role-players or only humans? Also what does it do on non-interactive problems beyond Panalba?
3. How much do real military red-team and wargame evaluations report about whether they found actual plan flaws (Perla 1985, Naval War College 1894 records, RAND, Army red-team reports)? Primary historical outcome data are missing.
4. How accurate is LLM adjudication against rule-based or human adjudication on stated moves (agreement rate, invented consequences)? Matlin shows it is rarely tested; find any measured study (2025-2026).
5. Does using a different model, a code-search opponent, or a rule set for the adversary find more weaknesses than the same model with a different persona? Welfare Diplomacy hints yes; one run only.
6. How many repeated adversary runs are needed before a flagged weakness is stable (variance across runs and paraphrases), and does code clustering of runs help? Shrivastava measures spread but not plan-level agreement.
7. What do the original Emery 2021 and Brewer and Blair 1979 sources say about computer opponents escalating, and is the effect about missing human costs or about scripted rules?
8. Does opponent modelling by explicit goals (given, not inferred) close the WGSR-Bench gap with humans? Test with goals supplied in the prompt.
9. Hindsight leakage: how much of the accuracy in historical-scenario wargames (WarAgent, Taiwan crisis) disappears with anonymised or post-cutoff scenarios?
10. Post-2025 LLM wargame studies not yet found: any measured results from frontier models (2026) on escalation, consistency, or red-team findings versus human teams, and any replication of Lamparth with newer models.

## Gap search results (evidence_d.jsonl d01-d24; claims K22-K27 added)

Search limits: the web search quota ran out partway; OpenAlex, Semantic Scholar and the arXiv API were rate limited. Discovery used arXiv's search page and Crossref instead. Brewer and Blair 1979, the DTIC red-team report and Friedman's book could not be opened.

1. Separate-call adversary at equal tokens: STAYS OPEN. Nearest is IFPV (d04): 61.0% vs 49.3% mission success, but scored by the same adversary used in design, in a simulator, compute not matched, no flaw recall or false alarms. Equal-compute debate vs self-consistency exists only for reasoning QA (d07: +1.3 and +2.7 points). Our own seeded-flaw A/B is still needed.
2. Outside replication of Green: STAYS OPEN (not found). Crossref shows the role-play papers are Green and Armstrong; Bolton and Erev 2002 are commentaries (d23). No LLM role-player test on Green's conflicts found. K01 lowered to single-source programme.
3. Primary outcome data on real wargames and red teams: PARTLY CLOSED, still weak. Millennium Challenge 2002 (d21) is a documented case of a red team finding a weakness and being constrained until the end state was scripted (JFCOM report, via Zenko). Plan Orange 1933 (d22) is a pointer only. Perla 1985, NWC 1894 records, RAND and Army red-team reports were not opened.
4. LLM adjudication accuracy: PARTLY CLOSED. Only a self-consistency study exists (d01, d02): 3-6% of outcomes change on re-run under bounded adjustment, 14-16% under free judgement. No human baseline. A claimed kappa of about 0.89 vs three human adjudicators traced to a withdrawn paper (d03) and must not be used.
5. Different model, code opponent, or rule set: PARTLY CLOSED. IFPV (d05): a prompted LLM opponent exposed fewer flaws than a scripted one; a world-model opponent exposed the most. Greenland study (d14) shows model choice changes behaviour 3.8-fold. RevengeBench (d09) shows code-space opponent recovery is feasible. Still no test on seeded-flaw plans.
6. Run counts and clustering: PARTLY CLOSED. Synthetic COA-Bench (d06): most of the drop is in the first 2-4 samples. Strategic-game comparisons needed about 150 seeds (d08). No test of agreement on which weakness was flagged, and no code clustering test.
7. Emery 2021 and Brewer and Blair 1979: PARTLY CLOSED. Emery was opened (d10): it contrasts one abstract MAD game with one human-played game, not computers vs humans in general, and does not mention Brewer and Blair in the text read. Lamparth and Rivera overstate it (d11). K19 set to contested. Brewer and Blair still unread.
8. Giving the adversary explicit goals: STAYS OPEN. No study found. Related: Colonel Blotto (d17) shows LLM strategies are stereotyped; RevengeBench (d09) infers rather than being told.
9. Hindsight leakage in historical wargames: STAYS OPEN for wargames. General evidence supports the worry (d18, d19, d20); no anonymised or post-cutoff WarAgent or Taiwan test found.
10. 2026 frontier models: PARTLY CLOSED. Payne 2026 (d12): no de-escalating choice in 21 games. Solopova 2026 (d13): agreement with graduate students 0.25-0.54 round 1, falling in round 2. Touchent 2026 (d15) and Adl and Williams 2026 (d14): language and framing move behaviour strongly. No expert-team replication of Lamparth with newer models was found.

Corrections to earlier files: unchanged from the section above (c19 still unpatched in evidence_c.jsonl). A search summary attributed "Lamparth et al. 2024 AIES" findings correctly, but the Emery passage appears in both Lamparth (2403.03407) and Rivera (2401.03408).
