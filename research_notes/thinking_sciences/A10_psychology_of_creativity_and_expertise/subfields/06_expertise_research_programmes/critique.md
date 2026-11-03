# Critique, A10.06 Expertise research programmes (cross-check)

## Numbers re-opened this session (full text or abstract)
Confirmed against the source text:
1. Huan et al. 2025 (arXiv 2507.00432), Table: Qwen3-14B non-reasoning average 45.7 base, 29.0 SFT no-think (TI -104.1), 53.2 RL. Confirmed. SFT think is 21.1. Confirmed.
2. Zheng et al. 2024 (2311.10054): 162 personas, 2,410 questions, in-domain coefficient 0.004 (p<0.01), classifier 78.1%. Confirmed.
3. Wu et al. 2024 (2307.02477) Table 32: GPT-4 chess legality 100.0 default vs 21.0 counterfactual, 100.0 vs 61.0 with CoT; CCC 89 vs 74 and 100 vs 96; GPT-3.5 73 vs 4. Confirmed.
4. Betley et al. 2025 (2502.17424): 6,000 insecure examples, 19.8% misaligned on GPT-4o. Confirmed (the +-7.1 interval was not re-verified).
5. Ruoss et al. 2024 (2402.04494): Elo 2895 vs humans, 2299 vs bots, GPT-3.5-turbo-instruct 1755 and 66.5 puzzles. Confirmed.
6. SPIRAL (2506.24119) Table 1: Qwen3-4B 34.0 to 44.5 (+10.5); Qwen3-8B 39.5 to 49.6; Octothinker 25.8 to 33.8 (+8.0). Confirmed.
7. Bediou et al. (OpenAlex abstract): g=0.55 cross-sectional, 0.34 intervention, 30% publication-bias inflation. Confirmed.
8. Macnamara et al. 2014 (abstract): 26/21/18/4/<1 percent. Confirmed. Note the 2018 corrigendum changed some values slightly.
9. Sala & Gobet 2017 (abstract): small to moderate effects, inversely related to design quality. Qualitative claim confirmed; the g values (0.34/0.16/0.12) in a05 come from the earlier searcher's reading and were not re-checked here.

## Corrections and clarifications
- a22 reports only SPIRAL vs base. SPIRAL Table 1 also has SFT game baselines (Qwen3-4B SFT-Multi 39.7; Qwen3-8B SFT-Multi 46.1, i.e. +6.6 over base). So part of the "game transfer" gain comes from game data under SFT too. Claim K13 carries this.
- c08/c25: the chess legality task is a balanced yes/no problem (chance 50%). GPT-4 at 21% is far BELOW chance, meaning it systematically applies the standard rule, not that it guesses. This makes the gap stronger than "weak."
- c07 says RL shift is 0.98 token-rank positions; b20 reports other measures (KL 0.084 vs 0.372). Different metrics, not a conflict.
- Ruoss: "tournament Elo 2299" in b27 is the Elo against bots, not a human-tournament Elo. Human blitz Elo 2895 is on Lichess against self-selected humans.
- a23 and b21 are the same paper (Xie, ViGaL); a24/b25/c10 are the same paper (Aryabumi); a21/b19/c05-c07 the same paper (Huan); a28/c16 the same (Schut). Counting them as independent sources was avoided in claims.
- a05/b01 and a06/b05/a08 are overlapping work by one research group (Sala, Gobet). "Established" for far-transfer-null therefore rests on one group plus Melby-Lervag (independent) and Simons review.
- Duplicate ids for the same paper in files a, b and c are not extra evidence.

## Contradictions between sources
- Chess instruction: Sala & Gobet 2016 meta-analysis found d 0.34-0.38, but the Jerrim 2016 randomised trial (about 1,900 per arm) found nothing. The meta-analysis included almost no active controls. Jerrim arm sizes are from a single reading and were not re-opened.
- Video games: Bediou (g 0.34 intervention) vs Sala et al. 2018 (null) and Unsworth 2015 (near zero at latent level). Differences come from control choice, inclusion rules and extreme-group designs. Unresolved.
- Persona prompts: Zheng (no gain on MMLU) vs Xu ExpertPrompting (48.5% vs 23% preference). Different task and judge; Xu uses GPT-4 as judge, which may favour longer answers.
- Human far-transfer null vs LLM transfer (code to NL reasoning, game RL to maths). Machines transfer when trained by RL or mixed pretraining, and not under narrow SFT. The human null is not a prediction for LLMs.

## Weak spots
- Most claims about the scaffold are by analogy. No study here ran a thinking scaffold; only Zheng and Wu test prompts.
- Persona claim (K09) is single-source and used only four open model families; large closed models were not covered.
- Several 2025-2026 LLM papers are preprints (Huan, Xie, SPIRAL ICLR 2026 version is peer-reviewed).
- Deliberate-practice variance figures depend on reliability corrections (Hambrick 2020); uncorrected vs corrected differ by a factor of about two.

## Seen only in snippets or abstracts (opened:false in files)
a09, a10, a12, a13, a14, a23, a24, a25, a26, a27, a28, b01, b04, b05, b06, b07, b08, b09, b25. Their numbers are as the abstract states. Sample sizes for van Ravenzwaaij 2014 and Unsworth 2015 were not read. b04 was not read at all.

## GAPS
1. Does a thinking scaffold (our schema) improve held-out domains at equal tokens against a length-matched placebo scaffold, or only in the domain it was tuned on?
2. Do expert-persona instructions help our agent on verifiable benchmarks with larger closed models, given Zheng tested only open models?
3. Is the counterfactual-twin gap (Wu: 100 to 21 in chess) reduced by a rule-restating or verification guardrail, and at what token cost?
4. What is the exact mechanism that makes RL transfer and SFT forget, and does prompt-level scaffolding behave like RL (little latent shift) or SFT?
5. Is the SPIRAL game-transfer gain mostly format and reasoning-style learning (SFT baseline also gains) or game-specific skill? What does a non-game synthetic-task control give?
6. How do chunk-based expert memories (Gobet template theory) translate to retrieval stores for an LLM: does retrieving solved patterns help on structured but hurt on novel problems, as in random-position chess?
7. Are early-fixation expert triage effects (Sheridan and Reingold) reproducible as an early relevance-filter step that saves tokens without losing accuracy?
8. What are the exact sample sizes, controls and effect sizes of Jerrim 2016, van Ravenzwaaij 2014 and Unsworth 2015 (not opened here)?
9. Does cross-domain contamination (Betley emergent misalignment) occur with prompt-level domain modules, or only with weight updates?
10. Is the human far-transfer null stable under newer preregistered, large-N replications from groups outside Sala and Gobet?

## Gap search results
Search note: WebSearch budget was exhausted and the OpenAlex, Semantic Scholar and arXiv query APIs were rate limited, so sources were found by known ids, Crossref, Europe PMC and direct arXiv PDFs. Evidence is in evidence_d.jsonl (d01 to d16).

1. Scaffold vs length-matched placebo on held-out domains: STAYED OPEN. No study found that tests it. d16 (filler tokens, 3SUM: CoT 95.1, filler 93.6, none 78.7) shows a placebo can carry much of the gain in trained small models, which supports the need for the control. Must be run by us.
2. Expert personas with larger closed models: PARTLY CLOSED. d09: GPT-4 persona average 91.06 to 92.28 (arithmetic) and 61.37 to 77.08 (other tasks, driven by Letter 19.8 to 92.8), with some datasets down; Llama3-8B worse on 7 of 12. No Claude or Gemini data. K09 changed to contested.
3. Rule-restating or verification guardrail on counterfactual twins: STAYED OPEN. d15 shows generic self-verification lowers accuracy (GPT-4 GSM8K 95.5 to 89.0); only information-adding checks can help. Not measured on Wu's twins.
4. Mechanism of RL transfer vs SFT forgetting: MOSTLY CLOSED. d11: forgetting tracks forward KL from the base policy (R2 0.96 toy, 0.71 LLM); d10: SFT collapses on rule variants (V-IRL-L 80.8 to 1.3), RL rises. Prompt scaffolds change no weights, so they avoid this route; behavioural drift from prompts untested. Claim K20 added.
5. SPIRAL game vs generic gain: MOSTLY CLOSED. d12: SFT on the same games gives 5.7 of 10.5 points (4B) and 6.6 of 10.1 (8B); weak-opponent RL falls below base. No non-game synthetic control exists in the paper. K19 added.
6. Chunk memories as retrieval stores: PARTLY OPEN. d13 (ExpeL) shows retrieval and insights help and carry over HotpotQA to FEVER (ReAct 58 to about 63-70). No evidence on harm for novel problems.
7. Early-fixation triage as token-saving relevance filter: STAYED OPEN. No LLM study found in the time available.
8. Sample sizes for Jerrim, van Ravenzwaaij, Unsworth: PARTLY CLOSED. van Ravenzwaaij opened (d01: N=20 in Exp 1, 10 per group; N=45 in Exp 2, 15 per group). Unsworth only abstract (d02); full text blocked (403). Jerrim/EEF report blocked (403); arm sizes remain from the earlier reading, unverified.
9. Cross-domain contamination at prompt level: CLOSED (yes it occurs). d14: 1 to 24% EM with 16 narrow examples, from 2 examples, across Gemini, Kimi-K2, Grok, Qwen. K21 added.
10. Human far-transfer null stable in large-N work outside Sala and Gobet: PARTLY CLOSED. d03 Owen 2010 (N=11,430, no transfer), d04 Simons 2016 review, d07 and d08 on placebo effects (mixed). No newly preregistered large replication found. K01 notes group dominance.
