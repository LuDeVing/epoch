# Critique: Pragma-dialectics (cross-check)

## Numbers re-opened this session (arXiv PDFs, pdftotext)
Confirmed exactly: Payandeh 2023 (GPT-3.5 37% vs 29%; GPT-4 67% vs 37%; "41% and 69% more likely"); MAFALDA (GPT-3.5 0.627/0.201/0.138; human 0.749/0.352/0.186); Jin 2022 (range 8.62 to 53.31; Electra-StructAware 58.77; +5.46); Khan 2024 (humans 88% vs naive 60%; LLM 76% vs 48%; consultancy 78% and 54%); Sharma 2024 (27%, 32% to 86%, 42% to 98%, Claude 1.3 98%); Zhang 2025 (about 15% of cases; +0.85% Claude-3.5-haiku; Heter-MAD 76.7 vs CoT 72.5); Smit 2024 (+15% Multi-Persona, +5% SoM on 376 USMLE; best about 61% MedQA); Du 2023 (arithmetic 67.0 vs 81.8; GSM8K 77.0 vs 85.0; chess 91.4 vs 122.9; MMLU 71.1 vs 73.8 in the biography table row, with personas 74.2).

## Corrections and notes
- LOGICCLIMATE size: a18 says 1,109, b20 says 1,079. Both are in the paper: 1,109 climate claims in the challenge set text, 1,079 in the dataset table. Not an error, but cite which.
- Zhang 2025 "gains vs CoT" (MATH +29.3%, AGIEval +12.3%, MMLU-Pro +11.4%) are relative percent changes of the table, not points (71.1 vs 55.0 on MATH). c24 said "gains"; read as relative.
- Sharma: "wrongly admit mistakes" range is 42% (GPT-4) to 98% (Claude 1.3); b25 wrote "42% to" truncated, c18 has it right.
- Khan 2024: same numbers in b26 and c12, counted as one source for independence.
- Du 2023 MMLU: c11 lists 63.9/57.7/71.1 (single/reflection/debate); b28 had no numbers. Consistent.

## Not re-opened (only trusted from earlier agents)
Zhou 2025 (a12-a15; arXiv title search failed), Singh 2026 (a23, a24), Chen 2026 (a25), Gajewska 2026, Mouchel 2025, Jeong 2025, Goffredo 2022, van Eemeren 2023 review numbers (b01-b05; Table 1 was an image), Voting or Consensus (c25). These stay marked by their own opened flags and are single-source in claims.
Never opened at all: a10, b10 (no result), b11, b12, b13, c26. Amsterdam experiment numbers (sample sizes, effect sizes) were never obtained anywhere.

## Contradictions
- Debate helps (Khan, Michael, Du) vs debate does not beat strong baselines (Smit, Zhang). Reconciled by setup: Khan/Michael use a weak judge with strong debaters holding information; Du compares to weak single-agent baselines. Not a contradiction about the same quantity; claim K12 marked contested.
- Zhou: the PD prompt helps (+2 acc) without context and not with context (49 vs 49): tiny test set, no noise estimate.

## Weak spots
- The theory itself has almost no independent empirical test; the evidence is one team's experiments covering 4 of 10 rules, clear-cut cases only.
- No LLM study applies pragma-dialectical rules as designed besides one student-level prompt paper. Most LLM evidence is about fallacy detection or debate, loosely linked.
- Several 2026 preprints (v1/v2) are unreviewed. Search coverage was limited (APIs rate-limited, WebSearch budget).
- Relevance to a single agent is low (multi-party theory).

## GAPS
1. Does a rule-based self-audit (burden of proof, relevance, starting point, closure rules) beat a generic critique at equal tokens on seeded flawed drafts, with CIs?
2. What are the sample sizes and effect sizes of the Amsterdam experiments (2000, 2009, 2012)? Need full text.
3. Has anyone replicated the lay-judgment findings independently (e.g. Hahn and Oaksford, Bayesian approach), and do they agree?
4. Do current frontier LLMs flag sound arguments that share a scheme with a fallacy (Singh 2026 foils), and does rule-based prompting reduce that?
5. Does demanding new evidence before revising (burden-of-proof rule) cut sycophantic flips in current models, versus Sharma 2024 numbers?
6. Does a fallacy-aware critique step lower fallacy rate in the agent's own final answers (FIPO-like effect) and at what token cost?
7. Is internal two-sided debate better than self-consistency at equal tokens for our task mix (Smit/Zhang say often not)?
8. Does strategic-maneuvering-style audience adaptation by an LLM produce derailments that detectors miss?
9. Are there 2025-2026 LLM studies using the Periodic Table of Arguments or PD rules beyond Zhou 2025 that the search missed?

## Gap search results (gap searcher, 19 Nov 2026)
Search limits: arXiv export API, Semantic Scholar and OpenAlex rate-limited (429) throughout; WebSearch budget ran out after two calls; arXiv listing pages and PDFs were used instead. Evidence is in evidence_d.jsonl (d01 to d21).

1. Rule-based self-audit vs generic critique at equal tokens: STAYED OPEN. No such study found. Closest: Zhou 2025 (PD prompt 53% vs base 51% on 120 items, one 8B model) and LoFa CoT defence (+7 to 13% for GPT-4, none for authority). New claim K21.
2. Amsterdam sample sizes and effect sizes: MOSTLY CLOSED. 2000 study N=92 pupils, fallacies 3.75 vs controls 5.29, F=539.31 (d01). 2002 series: effect sizes (within-subject variance share) .08 to .57, tu quoque weakest, one null (d02). Follow-ups n=24, n=75, Spanish n=47 and 29 (d03). Still missing: per-study n for the six studies, and numbers for the 2009 book and 2012 paper (d04, record page only).
3. Independent replication of lay judgments: PARTLY CLOSED, negatively. Spanish replication is by the same team (d03). Independent Cardiff Bayesian experiments (N=73, 72) show graded, content-driven judgments of a classic fallacy but are not a replication (d05). Nothing independent on PD rules. Status of K03 kept single-source.
4. Frontier LLMs flagging sound arguments that share a scheme with a fallacy: ANSWERED, rule prompting untested. Singh 2026 opened: Claude Sonnet 5 native-to-matched gap +13.5pp, Haiku 4.5 +12.6pp, Qwen +0.5pp; binary prompt reverses the sign (d08). Whether rule or critical-question prompting reduces it is open.
5. Evidence-demand rule vs sycophantic flips: PARTLY CLOSED. SycEval shows fabricated citations produce the most regressive flips (d10); SYCON-Bench shows frontier models hold under bare pressure (ToF near 5 of 5) but not on false presuppositions (about 3) (d11); evidence-first prompting cut flips from up to 72% to 12% in code smells (d17); CoPE-Bench says to score stubbornness too (d18). No direct test of a burden-of-proof rule on open argument. New claim K24.
6. Fallacy-aware critique lowering fallacy rate in own answers and token cost: STAYED OPEN. Only FIPO (a21, a22) and LoFa CoT analysis. K27.
7. Internal debate vs self-consistency at equal tokens: STAYED OPEN (arXiv queries returned nothing); K13/K14 remain best evidence.
8. Strategic-maneuvering audience adaptation producing undetected derailments: STAYED OPEN. Related: DeflectBench shows LLMs write deflection fallacies on request, mostly labelled (d16); debate judges are moved by manipulation (d14). No study of unprompted derailment.
9. Missed 2025-2026 PD or Periodic Table studies: CLOSED (negative). Only Zhou 2025, now opened (d07; PTA prompt 44% vs base 51%). Walton-scheme critical-question work exists (d20, unopened). Journal-only work may remain unseen.

Corrections to earlier notes: Zhou 2025 is now opened and its numbers (53% vs 51%, 120 test items) confirmed; a12 to a15 can be treated as verified. Singh 2026 numbers (85.9%, 16.6%, 58.9%) confirmed in the full text. Claims K02, K03, K04, K07, K10, K20 updated; K21 to K27 added.
