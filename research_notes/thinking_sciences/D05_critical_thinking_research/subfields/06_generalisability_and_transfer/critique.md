# Critique: D05.06 Generalisability and transfer

## Sources re-opened (this session, full text via arXiv PDF)
1. Mirzadeh et al. GSM-Symbolic (2410.05229): GSM-NoOp "up to 65%" and Phi-3-mini -65.7 confirmed; o1-preview -17.5 and o1-mini -29.1 confirmed; gap over 12 points for Gemma2-9B confirmed.
2. Wu et al. Reasoning or Reciting (2307.02477): GPT-4 base-9 addition 23.4% (no CoT) and 38.6% (0-shot CoT), GPT-3.5 6.6%, base-10 100% confirmed; "99% to 62%" for drawing confirmed in text. Column reading in b08 now checked against the table header (bases 8 9 10 11 16): correct.
3. Zhao et al. CoT mirage (2508.01191): 100% in distribution, 0.01% composition, 0% POOD/OOD confirmed. Correction: for LLaMA3-8B composition is 8.52%, near zero (0.01%) is Qwen3-14B. Evidence a24 should not be read as covering LLaMA.
4. Huan et al. (2507.00432): non-reasoning average base 45.7, SFT-think 21.1, SFT-no-think 29.0, RL 53.2, RL minus SFT +24.0; IFEval 69.2 to 42.3; +1.8 GPQA and +17.1 LiveCodeBench2 confirmed. Correction: 55.9 in the table row is the Qwen3-14B-Base GPQA score, not the SFT-think score as a25 and b17 say. The table dump is garbled, so which row 55.9 belongs to is uncertain.
5. Suzgun et al. Dynamic Cheatsheet (2504.07952): AIME 2024 23.3 to 50.0, AIME 2025 6.7 to 36.7 (DC-Cu), GPQA-Diamond 59.6 to 68.7 (DC-RS), full-history 26.7 confirmed. b22 and c12 are not in conflict: 6.7 to 40.6 is AIME 2020-2024 (a different set) under DC-RS. Note: GPT-4o AIME 2025 fell from 20.0 to 6.7 under full history (one run), a harm case.
6. Wang et al. Agent Workflow Memory (2409.07429): 36.2/45.1/43.6, 30.1/33.7/33.9, 18.6/32.6/35.5 and 24.6%/51.1% confirmed. Note: 24.6% is the overall Mind2Web relative gain, not cross-task only (a31 wording wrong). Task success rates are tiny (1.0, 0.7, 1.7 cross-domain), so step success gains hide near-zero whole-task success.
7. Huang et al. self-correction (2310.01798): GPT-3.5 CommonSenseQA 75.8 to 38.1 after one correction round (3 calls); GPT-4 GSM8K 95.5/91.5/89.0; oracle 97.5 and HotpotQA 29.0 to 59.0 confirmed.
Not re-opened: Sala & Gobet 2017 and Gobet & Sala 2023 (two evidence files agree with each other but both read the same papers), Abrami 2015 (read via summary only), Sprague, Dziri, Shojaee, Webb et al., McCoy, Chu, ExpeL. Treat these as seen once.

## Contradictions and tensions
- RL generalises, SFT does not (Huan, Chu) versus math-only data costs about 2 points on other tasks (General-Reasoner). Claim K14 and K15 contested.
- Strong subject-specificity (McPeck, Abrami 0.30 vs 0.57) versus inquiry meta-analysis finding subject domain not a moderator. The latter has I2 = 92% and funnel asymmetry, so weak.
- Humans: Gick & Holyoak numbers are recalled only (b25), while a06 has just "nearly 100 per cent with hint". Do not cite 20-30% as verified.
- Illusion of Thinking was read, but critiques (output-length limits, impossible River Crossing instances) were not searched; K22 left contested.

## Weak spots
- Many "independent" sources are one paper reported in three evidence files (AWM, Zhao, Wu, Huan, DC). Claims were recounted by paper, which demoted K01, K07, K16, K18 to single-source.
- Education evidence is mostly via secondary summaries (Willingham 2019, SEP, a Swiss summary of Abrami). Thorndike & Woodworth numbers missing (table lost).
- a10 "g = .47 2018 meta-analysis" has no clear source in the evidence line; unverified.
- No direct LLM test of McPeck's thesis: does a general scaffold beat class-specific scaffolds at equal tokens? All LLM memory studies compare memory vs none, not keyed vs shared.
- Mind2Web and WebArena gains are step-level; whole-task success remains small.
- a19 (Gabriel & Mushtaq): 73 completed, 56 analysed after 17 exclusions; low power for a null.

## GAPS
1. Does lesson memory keyed by problem class beat one shared lesson pool at equal retrieved tokens (the McPeck question for agents)? No paper tests this directly.
2. How does memory gain decay with distance (same class, sibling class, other domain) on reasoning, not web tasks? AWM cross-website gain is small; is that general?
3. Do scaffolds help on counterfactual or perturbed variants (Wu, GSM-NoOp, premise order), or only on the familiar form? Need scaffold-on vs scaffold-off results on those benchmarks.
4. What is the right control for scaffold transfer claims: which active-control prompt of equal length removes the expectation effect (Sala & Gobet lesson)?
5. When does curated memory hurt (Dynamic Cheatsheet full-history harm, AWM degrading on WebArena Multi)? What pruning rules fix it?
6. Did anyone replicate Gick & Holyoak analogical transfer with current LLMs (2024-2026) with counts, and does a hint-style cue raise reuse of a stored lesson?
7. Are the Illusion of Thinking collapses real or artefacts of output limits and ill-posed instances? Search for rebuttals.
8. Does Abrami's content-specific advantage (0.57 vs 0.30) hold once control type and study quality are modelled? Read the primary paper.
9. Does composition failure (Zhao 0.01%) persist for frontier reasoning models with tools, and does explicit decomposition into known sub-steps rescue it?

## Gap search results (evidence_d.jsonl d01-d20, claims K26-K34)
Search note: WebSearch quota ran out after four queries; arXiv, Semantic Scholar and OpenAlex APIs returned 429. Work used direct PDF fetches of known arXiv IDs. Gaps needing discovery of unknown papers (1, 2 on reasoning, 9 frontier) are therefore under-searched, not proven empty.

1. Keyed vs shared memory at equal tokens: STAYS OPEN. Dynamic Cheatsheet names topic-keyed memory as future work (d12). No test found. Reasoning models (R1, o1) gained little from DC.
2. Distance decay: PARTLY CLOSED, and K17 corrected. On Mind2Web the ReasoningBank gain does not shrink with distance (SSR +4.6/+2.2/+4.7 flash; +1.2/+2.1/+3.1 pro); AWM is what falls below no-memory cross-domain (d13, d14). Still web tasks with whole-task success of 1-5%. No reasoning-task curve.
3. Scaffolds on perturbed variants: PARTLY CLOSED. GSM-IC shows scaffold-on gains but not full rescue (macro 6.0 to 45.0, d03); GSM-Plus compositional prompt +4.7 over LTM (d06). Premise order was zero-shot only (d05), and K10 was too strong for math (9-15 points on R-GSM). Counterfactual (Wu) and GSM-NoOp scaffold arms still not found.
4. Active control: CLOSED as a design rule. Same-form generic instruction did not help (d04); invalid-but-relevant demonstrations keep 80-90% of gain, off-topic ones do not (d07); random labels barely matter (d08); filler tokens only in small trained models (d09). Use three arms: valid, invalid-but-relevant, off-topic of equal length. No paper applies this to a scaffold-transfer claim.
5. When memory hurts: CLOSED enough to act. Add-all lowered success in 4 of 4 agents (d10); history-based deletion by downstream utility helps with a reliable judge and can hurt with a weak one (d11). Strict filter used an oracle.
6. Gick-Holyoak with LLMs: PARTLY CLOSED. An adapted matching study (60 GPT-4 runs) shows no-hint failure and hint recall 1.00 with precision ~0.5 (d15). Human 1983 Exp 2 is 29% vs 50% (d16, second-hand), so the 20-30% vs 90% figure is still unverified and probably mixes two studies (K05 reworded).
7. Illusion of Thinking: MOSTLY CLOSED. Rebuttal finds token-cap and unsolvable River Crossing artefacts (d01); tools restore Hanoi to N=13 (d02). Both are preliminary (no counts; 5 trials per cell). K23 stays contested.
8. Abrami: CLOSED by correction, not by modelling. The 0.57 is an outcome-type split, not content-specific teaching (d18); explicit vs infused and STEM vs non-STEM did not differ. K01 reworded and set contested. Primary PDF blocked (403, d20), so control-type and quality moderators remain unseen.
9. Composition for frontier models with tools: STAYS OPEN. Only older evidence: decomposition plus search lifts 2Wiki EM 25.4 to 40.1 (d17). Zhao 0.01% vs 8.52% correction stands.

New weak spots: several tables extracted from PDFs are garbled (d06, d07, d11, Bamboogle in d17); column readings are marked as uncertain in the lines. d16 is second-hand. The SEP four-way split (d19) was read through a summariser.
