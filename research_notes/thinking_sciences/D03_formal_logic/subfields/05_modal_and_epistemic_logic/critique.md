# Critique: Modal and epistemic logic (D03.05)

Cross-check date 2026-11-19. Method: re-opened arXiv PDFs (pdftotext) for KaBLE, Holliday et al., Kosinski, FANToM, ToMBench, Logic-LM, SymbolicToM, Hi-ToM, Ullman, MindGames, Shapira. Total 11 sources, about 25 numbers checked.

## Corrections made
1. Hi-ToM (b14): "joint accuracy near zero at order 4" is too strong. The paper's Figure 3 shows about 0.05 to 0.16 at order 4 (order 0 about 0.95). Claim K16 uses the corrected range.
2. KaBLE (a24, a25, b09): the paper uses 92.1% twice, once for true-belief confirmation and once for "I know" markers, and 85.7% both for factual average and for the no-marker case. Text in the paper itself is this way, so the "I know" vs no-marker contrast (92.1 vs 85.7) may be a reuse of other aggregates. Treat that contrast as unreliable. K13 drops it.
3. KaBLE table (a24, b08): the numbers 98.2/64.4 (GPT-4o) and 93.4/22.0 (GPT-4) and the averages 54.4 and 92.1 are confirmed in the table. But pdftotext misaligns row labels, so the exact task name behind the 64.4 and 22.0 row (recursive awareness vs first-person belief) is not certain. The 54.4 average is confirmed as first-person belief confirmation by the paper text.
4. KaBLE comparison "54.4 vs 80.7" (a24): first-person and third-person figures are aggregates over different task sets; not a clean contrast. Flagged in K13.
5. Holliday et al. (b01, b02): zero-shot and CoT deltas confirmed exactly (Llama 405B 89.50 / +1.00; GPT-4 Turbo Apr 87.17 / +4.33; Sonnet 85.33 / +2.33; mini 75.33 / +13.50; lowest 45.33). Correlations 0.81, 0.85, 0.75 confirmed. a22 has the same figures as a rounded range; same source, not independent.
6. Confirmed unchanged: Kosinski 75%, CI 66-84, 178-study child meta-analysis; FANToM 87.5 / 26.6 / 14.8 / 53.7; ToMBench 85.4 vs 75.3 and 13.6 human coherent drop; Logic-LM +39.2 / +18.4; SymbolicToM +38 to 92% on ToMi, +62, +78; Hi-ToM 60.42 / 55.81 / 58.11; Ullman P=95% and 98%, 94%; MindGames 94%, agreement 0.89, 400 cases; Shapira 97.5 / 83.3 / 27%.

## Contradictions between sources
- Kosinski (GPT-4 75%, on par with 6-year-olds) vs Ullman, Shapira, Hi-ToM, FANToM, ToMBench. The first measures one narrow template set; the rest use perturbed or harder items and find large drops. Not a data conflict, a difference in item difficulty. Models differ (2023 vintage).
- MindGames (b18) says no clear scaling trend in the GPT-3 family; Kosinski reports gradual improvement across the same family. Different tasks and prompts.
- Holliday et al. says modal skill tracks general benchmarks (r about 0.8); KaBLE shows large unexplained gaps between true and false belief within strong models (GPT-4 22%). These are different capabilities, so both can hold.
- CoT: Holliday finds small gains for strong models; KaBLE finds slight losses; Hi-ToM finds none under deception. Consistent only in saying CoT is not reliable for epistemic tasks.

## Weak spots
- Almost all LLM evidence is from 2023 to mid-2024 models (GPT-4 class). Nothing here measures current reasoning models. All claims on LLM results are single-paper, so none is "established" except when two benchmark families agree (K20).
- a-, b- and c-files overlap heavily: Suzgun, Holliday, Sileo, Kosinski each appear 2 to 3 times. Independent source counts in claims.jsonl count papers, not lines.
- No test of an epistemic-logic scaffold (explicit Kripke model, DEL update) against plain prompting at equal tokens exists in what we found, except SymbolicToM (2023, tracker for ToMi) and Logic-LM (general logic).
- Gettier and knowledge-luck cross-cultural sources (b23-b27) were never opened. Numbers unknown. The Machery and Seyedsayamdost replication story is therefore unverified here.

## Only seen in snippets or abstracts
b23, b24, b25, b26, b27 (abstract or metadata only); c03 (leaderboard, not opened); c20 OpenToM (abstract level, no numbers); c24, c25 (cited only); c26 (alphaxiv snippet, 2026 probability-operator benchmark, 14,320 prompts, unverified and should not be used); b20 Gandhi numbers (82/72 human) were not re-opened here; b22 Arslan numbers not re-opened; Strachan (b16, b17, c18) not re-opened, and b17 mixes two sets of percentages (71.11/87.78 for GPT-3.5 vs 19.27/30.10) that need checking.

## GAPS (most decision-relevant first)
1. How do current reasoning models (2025-2026, thinking-mode) score on KaBLE false-belief and first-person belief tasks? The 54.4% and 22% figures may be obsolete.
2. Does a "record the user's belief without endorsing it" step in a scaffold close the first-person false-belief gap at equal tokens?
3. Does an explicit per-agent belief table (SymbolicToM style) still help current models on Hi-ToM order 3 and 4, FANToM and nested-belief items, once token cost is matched?
4. Is the CoT penalty on belief tasks (KaBLE -4 to -6%) reproduced on current models, and what causes it?
5. Do LLMs show the McGee/modus ponens overacceptance and triad inconsistency in current models, and does a consistency-check step fix it?
6. Do muddy-children and public-announcement puzzles (MindGames-style) get solved by current models, and does a DEL-style update table beat free reasoning at depth k=4 or more?
7. What are the actual numbers and replication status in Gettier and knowledge-luck folk epistemology (Machery vs Seyedsayamdost, Nagel, Turri)? Matters only if the agent must model what lay users mean by "know".
8. Are there 2025-2026 papers using epistemic logic or DEL as a verifier or planning layer for LLM agents (multi-agent information asymmetry, epistemic planning), with measured gains?
9. Do response-bias controls (balanced true/false, always-answer-no baselines) change the ranking of current models on ToM benchmarks (Strachan's faux pas finding)?

## Gap search results (2026-11-19)
Search tools were rate limited (WebSearch budget used up, arXiv/Semantic Scholar/OpenAlex APIs returned 429). Papers were found through a Hugging Face papers search endpoint and direct arXiv PDF fetches. 21 lines in evidence_d.jsonl (d01 to d21; d21 not opened). Claims K13, K14, K17, K18, K21, K23 updated; K26 to K33 added.

1. Current reasoning models on KaBLE: STAYS OPEN. The arXiv text is v1 only and has no reasoning models (d20); the Nature MI version could not be fetched. Partial closure from neighbours: SimpleToM (d01) shows o1, o3-mini, GPT-5, R1 at 95-99% on "does X know" but 32-66% on behaviour judgment. So the gap persists in reasoning models for applied belief, narrower than for GPT-4o (15.3).
2. "Record the belief" step: PARTLY CLOSED on an adjacent task. SimpleToM mental-state reminder: behaviour prediction +30 points (GPT-4o 49.5 to 82.8), generic CoT less (d02). Not tested on KaBLE first-person belief, and not at equal tokens.
3. Belief tables on current models and orders 3-4: PARTLY CLOSED. ThoughtTracing beats o1/o3-mini/R1 on ParaphrasedToMi with fewer tokens (d03, d05). DEL-ToM gives gpt-4o-mini 75.0 to 93.5 on Hi-ToM (d06). Both need extra machinery (hypothesis sampling, trained verifier). Strict equal-token comparison still missing. EnigmaToM (d14) has no reasoning models.
4. CoT penalty on current models: PARTLY CLOSED, mixed. Reproduced as a false-belief bias in reasoning models (true-belief accuracy 28-49% for o1-preview, o3-mini; d04) and in Feb 2026 on older open models (d17). Opposite sign for stipulated modal semantics, where reasoning mode gives +84 points (d08). Cause suggested by authors (over-reasoning on no-asymmetry items), not proven.
5. McGee / modus ponens overacceptance and triad inconsistency: STAYS OPEN. No paper found.
6. Muddy children and public announcement at depth 4+: PARTLY CLOSED. DEL-ToM tests orders 0-4 on Hi-ToM only (order 4: Qwen3-4B 46.0 to 65.0). No muddy-children test of current models found. MindGames not rerun on current models.
7. Gettier and knowledge-luck numbers: STAYS OPEN. Only Crossref abstract for Machery et al. (Noûs 51(3), 2017, correcting b23's 2015). Wiley, PhilArchive and SSRN blocked (403).
8. Epistemic logic or DEL as verifier or planner for agents: PARTLY CLOSED. DEL-ToM (d06, d07) is the one direct case, with measured gains. Peng et al. 2026 (d19) uses an environment verifier under information asymmetry, not DEL, numbers not read. No epistemic planning paper with LLMs found.
9. Response-bias controls: PARTLY CLOSED. Hu, Sosa and Ullman (d16) and Lu et al. (d10: ExploreToM 22% yes vs 4% no) support bias controls; no re-ranking of current models by balanced scoring found. Strachan faux-pas rows (b16, b17, c18) still not re-opened.

New weak spots: DEL-ToM test sets are about 40 items per order; Hi-ToM format is in-distribution for the verifier. Andrieu and Sileo (d08) is a single August 2026 preprint. Several PDF tables (EnigmaToM, ThoughtTracing effort rows, ToM-RL) were misaligned in extraction, so only text-verified numbers were recorded.
