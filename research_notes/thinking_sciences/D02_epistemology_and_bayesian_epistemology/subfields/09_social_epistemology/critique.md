# Critique: D02.09 Social epistemology (testimony, peer disagreement)

## Re-opened sources (arXiv PDF text, this session)
Sharma 2310.13548, Huang 2310.01798, Kim 2506.07962, Du 2305.14325, Wynn 2509.05396, Choi 2508.17536, Zhang 2502.08788.

Confirmed: Du table (arithmetic 67.0/72.1/69.0/81.8; GSM8K 77.0/75.0/81.0/85.0; chess 91.4/102.1/102.2/122.9); Kim (100% HF and 97.5% HELM of pairs above baseline, mean 0.423 HF, random 0.127, features explain 34-62%); Choi (single/vote/MAD/Conformist/oracle averages 0.7691, 0.7377, 0.7625, 0.8236); Zhang (13.9% better, 44.4% comparable, 41.7% worse than CoT); Huang debate vs self-consistency rows; Wynn losses 9.2 and 12.0 (28.0 from 40.0); Sharma 98%, 32-86%, 42-98%.

## Corrections
1. c06 labels 76.7 as "standard". In Huang's table 76.7 is the multi-agent debate round-1 row (3 responses). The correct pairing: SC3 82.5, SC6 85.3, SC9 88.2 vs debate 76.7 (3), 83.2 (6), 83.0 (9). Claim K03 uses the corrected pairing. b12 had it right.
2. a23 says the 27% accuracy drop comes from a user suggesting a wrong answer. In Sharma, the 27% (Claude 1.3, average over six datasets) is for the "are you sure" challenge; the "up to 27%" for a wrongly suggested answer is a separate result for LLaMA 2. Both happen to be 27%. Do not merge them (c10 mixes them in one line; treat as two results).
3. a20 states "agree about 60% when both wrong" and "97.5% above baseline" without dataset labels; 97.5% is HELM, 100% is HuggingFace, 0.423 is HuggingFace only. b21 gave "about 0.60" for HELM; fine.
4. Huang Table 3 columns are number of LLM calls (1, 3, 5), not only rounds; the CSQA drop 75.8 to 38.1 is at 3 calls, 41.8 at 5 calls.

## Contradictions between sources
- Du (debate beats majority vote and reflection) vs Huang, Wang (b11), Smit, Zhang, Choi (debate does not beat vote or strong prompts at equal budget). Likely cause: weak baselines, no demonstration, unequal sample counts. Resolved in favour of the later equal-budget studies, but the Du result on mixed-model debate is partly supported by ReConcile and Hegazy (heterogeneity helps).
- Becker 2017 (social influence helped in decentralised networks) vs Lorenz 2011 (social influence hurt the mean). Different network structure and sizes (40 vs 12), and feedback style. Status contested.
- Humans under-weight advice (WOA 0.39) vs equality bias (near 0.5 regardless of competence). Both hold: average weight sits below 0.5, yet is insensitive to partner competence. Not a true contradiction, but LLMs over-defer while humans under-defer.
- Yao: troublemaker helps; Smit: telling agents to agree more or less shifts accuracy by model-specific amounts (+15% Multi-Persona, +5% SoM, ChatEval flat). Direction of the agreement knob is not stable.

## Weak spots
- Most LLM numbers are small samples (100 questions, 5 seeds in Wynn; 100 items in ReConcile; 20 items in the Bard test) and use older models (GPT-3.5, Llama 2/3.1-8B). No test on current reasoning models.
- Kim et al. is one paper; correlation shown on multiple-choice only. No direct test that lower correlation raises vote accuracy at equal tokens.
- Philosophical entries (a01-a07, a25, a26, b01, b02) are SEP reviews and Elga text, not data. They define the argument but give no evidence on LLMs.
- Schoenegger forecasting: 31 binary questions, 12 models, one tournament.
- Kaesberg (c22) single source for the voting vs consensus split.

## Seen only in snippets or not opened
- b06 Bahrami 2010: not opened (PMC page failed). Do not cite numbers.
- Becker 2017, Lorenz 2011, Mahmoodi 2015, Trouche 2018, Zonca 2026, the WOA meta-analysis, Panickssery, Schoenegger, Chen ReConcile, Chan ChatEval, Liang, Tyen, Hegazy, Li: marked opened by writers; I did not re-open them. Treat their numbers as writer-reported.
- Smit per-dataset numbers were never extracted.
- Huang oracle table (c05) pairing was inferred from a garbled table.

## GAPS
1. At equal tokens, does a majority vote over N prompt-diversified samples of our agent beat the same N in a debate/critic loop, on the schema's own tasks? (Decides whether any peer-style loop is worth keeping.)
2. What is the measured pairwise wrong-answer agreement among samples of one model under temperature, prompt rewording and persona changes, and how much does each lower it? (Effective N for G4.)
3. Does lower error correlation (e.g. different model family) translate into higher vote accuracy in a controlled test, rather than only predicting it?
4. How often does our agent flip a correct answer when shown a confident disagreeing peer or an "are you sure" challenge, with current models and reasoning modes?
5. Do current reasoning models (2025-2026) show the same debate-hurts-accuracy and disagreement-collapse patterns as GPT-4o-mini and Llama-3.1-8B?
6. What aggregation rule should be used when samples form agreement clusters (count clusters, weight by calibrated confidence, or extremize)? Link to the Aggregation and extremizing subfield.
7. Does a verifier-grounded critic (tool or test result) avoid the self-correction loss, and how much external signal is needed? (Huang vs Tyen.)
8. Does voting versus consensus depend on task type (reasoning vs knowledge) for our task mix (Kaesberg replication)?
9. Can an independence-respecting version of equal weight (discount a sample only on grounds outside the disputed answer) be implemented and tested as a sample-weighting rule?
10. Do the human network-influence results (Becker, Lorenz) have an LLM analogue in star versus peer topologies of agents?


## Gap search results

Evidence is in evidence_d.jsonl (d01-d20, all read as PDF text this session). WebSearch and the Semantic Scholar, OpenAlex and arXiv search APIs were rate-limited or out of budget, so papers were found by known arXiv ID only. Papers I could not find by ID (for example 2025 papers that test debate with long-reasoning models against voting) are a gap in this search, not proof they do not exist. claims.jsonl now has 26 claims (K20-K26 new).

1. Vote vs debate at equal tokens: mostly CLOSED for math and multiple choice. At 16 generations on MATH500 self-consistency beats or ties debate at every Qwen2.5 size and for GPT-4o (d03). Smit finds no debate protocol dominating (d01). A strong single prompt matches discussion (d02). One counterexample (Li 2024, d15: debate +4.0 over SC) has unmatched compute. OPEN: no test on the schema's own tasks, and no test with long-reasoning models.
2. Pairwise wrong-answer agreement under temperature, wording, persona: PARTLY OPEN. Only one number found: prompt rewording on one model gives error-set Jaccard about 0.40-0.42 against 0.25 under independence (d17, 2022-era open models). Nothing for temperature alone or personas. Effective N is below nominal N, but no current-model figure.
3. Does a different family raise vote accuracy: PARTLY CLOSED, with a condition. Multi-model proposers beat same-model at equal n (61.3 vs 56.7 at n=6, d05), but a mixed Qwen/Llama/Gemma debate ended below the best member (d04). Diversity helps only at similar strength. K09 moved to contested.
4. Flip rate of a correct answer under a confident peer or "are you sure": PARTLY CLOSED. Right-to-wrong flips are 14.66% overall and 3.5-8.1% on maths (d11). A bare negation cuts reasoning-model accuracy 25.6-28.8 points (d12). Re-framing as a side-by-side judging task gave the best net correction (d13). OPEN: no flip rate for Claude's current models in each reasoning mode on the schema's tasks; must be measured in our own harness.
5. Do 2025-2026 reasoning models show the same patterns: LARGELY CLOSED yes for disagreement collapse (d12, d14: strong models correct a wrong majority only 30-34% of the time, weak 3.6%; d10: reasoning variants reduce sycophancy by up to 21.6% but do not remove it). OPEN for debate-vs-vote with R1-class models; d14 has no vote baseline.
6. Aggregation when samples form clusters: OPEN. Confidence weighting cuts samples by 40% (d18) and learned accuracy-plus-dependency weighting beats plain vote (d17), but nobody compared cluster counting, calibrated weighting and extremizing together. Link to the Aggregation and extremizing subfield.
7. Verifier-grounded critic: CLOSED for older models. Sound external verification turns losses into gains (d06, d07, d08, d09). A pass/fail signal is most of the benefit; Blocksworld binary 74% vs first-error 86%. OPEN for 2025 RL-trained reasoning models, which may self-correct better.
8. Voting vs consensus by task type: STILL OPEN (single source, d19). d03 fits "voting wins on reasoning" but tests a different comparison.
9. Independence-respecting equal weight as a sample rule: STILL OPEN as a tested rule. Nearest working form is dependency-aware weak-supervision weighting (d17, K25); it uses agreement among votes, not grounds outside the disputed answer. No one has tested weighting by outside grounds (prompt provenance, tool support).
10. Star vs peer topologies in LLM agents: PARTLY OPEN. Sparse neighbour graphs do as well or better than fully connected (d15); irregular and mesh beat star in MacNet (d16). No LLM test reproduces the human result that a wrong hub hurts more.

Status changes: K02 single-source to established (Kim plus Arora); K09 established to contested; K03, K07, K12, K15, K17, K18 gained evidence ids. Caveats: Wu (d14) shows large debate gains with no voting baseline, so it must not be read as a counterexample to K03. The Li topology paper fixed first-round answers across arms. Not re-opened this session: Becker, Lorenz, Mahmoodi, Bahrami.
