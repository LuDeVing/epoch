# D05.05 Instruction effectiveness: cross-check and critique

## Numbers re-opened this session (source text read)
Confirmed against the paper text: Wei 2022 (GSM8K 17.9 to 56.9, other four tasks), Kojima 2022 (MultiArith 17.7 to 78.7, GSM8K 10.4 to 40.7), Du 2023 (arithmetic 81.8, GSM8K 85.0, chess 122.9, MMLU 63.9/57.7/71.1, validity 29.3/38.8/45.2, persona 71.1 to 74.2), Huang 2024 (Tables 2, 3, 7, 8: GSM8K 75.9/75.1/74.7, CSQA 75.8/38.1/41.8, GPT-4 95.5/91.5/89.0, oracle 84.3 and 97.5, 74.7% kept answer, CommonGen-Hard 44.0/67.0 and 81.8/75.1), Min 2022 (1.7 multi-choice, 2.6 classification), Sprague 2025 (1,218 comparisons, 110 papers, +14.2/+12.3/+6.9, 56.9 vs 45.5), Zheng 2024 (+7, +11, +27, +7), Yasunaga 2023 (GSM8K 76.7 vs 77.8; davinci-003 54.0 vs 61.0), Kestin 2025 (N=233 enrolled, 194 eligible, medians 4.5 vs 3.5, z=-5.6, effect 0.63).

## Corrections
1. Kestin (a15, c16): N=142 and N=174 are lesson-level observations (pre-test baseline N=316), not students. 194 students, two lessons each in a crossover. Do not read 142 as a student count.
2. Huang Table 7 (b10): the pdf table layout is garbled. Debate scores 83.2 and 83.0 are reported, but the response counts attached to them (b10 says "9 responses") cannot be pinned from the text layout. Safe reading: debate about 83 vs self-consistency 82.5 (3), 85.3 (6), 88.2 (9). The conclusion (debate not above matched voting) stands.
3. Abrami 2015 inclusion (a01 vs a07): a01 says gains were significant for interventions of 1 hour to 2 days; a07 (Stanford Encyclopedia) says inclusion required at least 3 hours. These disagree and neither was checked in the journal paper. Treat the duration claim as unverified.
4. a01 says "341 studies"; the count is 341 effect sizes (a07, b02). Effect sizes, not independent studies.
5. c11 duplicates a13/b11 with fewer numbers; a13 values are the verified ones. c09 and c03 are the same papers as b08 and b07 (not independent sources). Counted once in claims.
6. c18 (Reflexion 91% vs 80% HumanEval) and c19 (ExpeL 40% vs 39%) came from abstracts/tables not re-opened; b17 Self-Refine "about 20%" is an abstract claim that Huang (b09) undermines.

## Contradictions between sources
- Debate: Du reports debate above majority vote (GSM8K 85.0 vs 81.0), Huang finds matched-compute self-consistency equal or better. Du's majority vote and Huang's self-consistency differ in setup, so "contested", not refuted. Our G9 follows Huang.
- Reflection: helps arithmetic in Du (72.1 vs 67.0) but hurts GSM8K and MMLU; Huang shows it hurts without an oracle. Consistent: no reliable gain.
- Self-Refine (+20%) vs Huang: resolved by baseline strength (CommonGen-Hard 44.0 vs 81.8 standard prompt).
- Human CT instruction: Abrami 0.30 vs Huber and Kuncel (programs aimed at CT added nothing beyond normal college). Different designs (RCT/quasi-experiments vs longitudinal cohort); not reconciled.
- Inquiry learning g=1.34 vs Abrami 0.30: the 2026 meta-analysis has I2=92%, Egger p<.001, and effect depends on control group (1.53 vs 0.78). Likely inflated by bias and weak controls.

## Weak spots
- No Abrami 2015 full text (secondary summary only); exact moderator table, explicit-then-applied g, and mentoring-alone g missing.
- Founding worked-example studies (Sweller and Cooper 1985), Kirschner et al. 2006 and Alfieri 2011 were never opened; only the 2023 worked-examples meta-analysis is cited, and its title was confirmed while figures came from one source.
- Bastani PNAS numbers (+48%, +127%, -17%) were not re-opened here (publisher page blocked); rest on two earlier agent reads that agree.
- Kestin is one course at one university; the prompt design is credited but not ablated. AI-tutor evidence for the agent is indirect: our agent is the learner/solver, not the tutor.
- Almost all LLM "teaching" evidence is prompting on 2022-2023 models. Little tested on current reasoning models that already think step by step; the CoT gains may be much smaller there.
- b04/b05 are narrative reviews without effect sizes. CQoT (c23) is LLM-judged and small.
- Only seen in snippets/abstracts: Reflexion, ExpeL, Rubin 2021, Lampinen exact gains, Chang 2023 (no numbers at all).

## GAPS
1. Does stepwise reasoning instruction (CoT, step-back, least-to-most) still add anything on current reasoning models that already think by default? Needs a 2024-2026 measurement at equal tokens.
2. What are the exact Abrami 2015 moderator values (explicit-principles-then-applied, mentoring alone, dialogue types) and the inclusion rules (1 hour vs 3 hours)? Full journal text needed.
3. Which element of the Kestin tutor (expert-written solutions in the prompt, step sequencing, self-pacing) drives the gain? Any ablation or replication in 2025-2026?
4. Does matched-compute self-consistency beat debate on tasks beyond GSM8K and with current models (reasoning, code, factuality)? Du's factuality gain (biographies) was not tested against voting.
5. Does a lesson/memory store help when lessons are written from verified failures vs unverified ones, at equal tokens? Reflexion/ExpeL numbers were not re-opened and neither ablates gating.
6. Is the worked-example effect (g=0.48) reversed for expert-like models, the human expertise reversal effect? Is there an LLM analogue (exemplars hurting strong models)?
7. What do the founding studies (Sweller and Cooper 1985; Kirschner 2006; Alfieri 2011 assisted vs unassisted discovery) actually report, with numbers?
8. Do the Bastani guardrail results (hint prompt removes harm) replicate, and is there an agent analogue where giving the solution to memory harms later unaided runs?
9. Is explicit teaching of critical-thinking dispositions (g=0.23) transferable to an agent at all, or are dispositions only visible as skill gains?

## Gap search results
Sources opened this session: Meincke 2025, Zhang 2025 (debate), Xiong 2025, Reflexion, Wang 2025 (Harm to Help), DeepSeek-R1, Alfieri 2011 (full text), Bastani 2025 (PMC full text), Kestin 2025 (PMC full text). Evidence in evidence_d.jsonl (d01-d19). Search tools were rate limited (OpenAlex, Semantic Scholar, arXiv API returned errors or 429; WebSearch budget spent), so some gaps stay open.

1. Stepwise instruction on reasoning models: PARTLY CLOSED. Meincke 2025 (GPQA Diamond only) finds +3 points or less for o3-mini and o4-mini and -3.3 for Gemini Flash 2.5; non-reasoning gains are partly from a baseline told not to think. Step-back and least-to-most were not re-measured on reasoning models. Equal-token test still missing. New claim K30.
2. Abrami 2015 moderator values and 1 hour vs 3 hours inclusion: STILL OPEN. Journal text (SAGE) returned 403, no open copy found. The a01/a07 disagreement stands.
3. Which Kestin tutor element drives the gain: STILL OPEN. The paper has no ablation and lists its own limits (single course, first-exposure content). Found only that the platform had to enforce step order because the prompt alone failed (K36). No 2025-2026 replication found in the reachable sources.
4. Matched-compute self-consistency vs debate beyond GSM8K: CLOSED for non-reasoning models. Zhang 2025 covers 9 benchmarks, 4 models, 6 calls; debate wins over CoT in about 15% of configurations and loses to SC; SC scales with tokens, debate does not. K13 moved from contested to established. Still open: reasoning models, and Du's biography factuality task against voting.
5. Verified vs unverified lessons: CLOSED in direction. Xiong 2025 shows add-all memory falls below a fixed memory and oracle-gated memory is best (K32). Reflexion ablation shows reflection without tests hurts. Caveat: gating tested against an oracle or a fine-tuned judge, not token-matched against no memory.
6. Expertise reversal analogue for LLMs: CLOSED for the LLM side. Wang 2025 and DeepSeek-R1: demos hurt reasoning models (K31). The human expertise reversal numbers (Kalyuga) were not opened, so the "human version" is cited from memory of the field only.
7. Founding studies: PARTLY CLOSED. Alfieri 2011 read in full (K34). Sweller and Cooper 1985 and Kirschner 2006 could not be fetched (host unreachable); still only secondary.
8. Bastani: PARTLY CLOSED. Numbers now read from the paper (K35); the PNAS erratum is only an affiliation fix; no independent replication found. No agent analogue measured; Xiong's experience-following is the closest.
9. Dispositions (g=0.23) transfer to an agent: STILL OPEN. No source found; treat dispositions as not testable apart from skill outcomes.

Changes to claims.jsonl: K13 now established with d04-d06 added; K05, K06, K07, K12, K14, K21, K22, K25 got extra evidence ids; new claims K30-K36.
