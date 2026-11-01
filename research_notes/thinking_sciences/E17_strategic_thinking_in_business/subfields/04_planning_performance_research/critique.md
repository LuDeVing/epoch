# Critique, E17.04 Planning-performance research

## Corrections made (sources re-opened this session)
1. b29 vs c05: Plan-and-Solve zero-shot average. Table 2 of arXiv 2305.04091 (full text): CoT 70.4, PS 72.9, PS+ 76.7, PoT 73.5. b29 said PS 73.5; that is PoT. c05 is right. Claims use 72.9.
2. Confirmed in full text: Vending-Bench table (Sonnet $2,217.93, min $476; o3-mini $906.86; Human $844.05; Gemini 1.5 Pro $594.02; GPT-4o mini $582.33; GPT-4o $335.46). b26 and c23 name different rows, no conflict.
3. Confirmed in full text: ToT Game of 24 (7.3 / 4.0 / 9.0 / 45 / 74%); PlanBench GPT-4 206/600, Instruct-GPT3 41/600, verification 191/600 and 4/600; o1-preview Mystery 317/600 (52.8%), randomized 37.3%, Fast Downward 0.265 s, Llama 3.1 405B 62.6%; Large Language Monkeys 15.9% to 56% at 250 samples vs SOTA 43%; CSQA 65.2 to 71.9, StrategyQA 63.8 to 65.4.
4. Confirmed from Crossref abstracts: George 2019 "positive, moderate, and significant", strongest for effectiveness and formal planning, holds in public and private sectors. Hamann 2022 (183 samples) says effects are stable over time and planning types, larger for manufacturing, larger firms, high uncertainty avoidance, and high environmental uncertainty. Camuffo 2020 RCT abstract confirmed (116 startups).
5. New fact not in the evidence files: Hamann 2022 finds planning pays more under uncertainty, against the "plans fail in turbulence" view. Added to K03.

## Contradictions
- Shea-Van Fossen 2006 (effect vanishes after trim-and-fill) vs Hamann 2022 and George 2019 (robust positive). Different corrections and samples. Unresolved.
- Goh 2026 (c21) reports o1 Mystery Blocksworld 74.3% baseline; Valmeekam 2024 reports o1-preview 52.8%. Different model versions or prompts; not reconciled.
- Plan-and-Act 57.58% (b34) vs TheAgentCompany 30% (b35): different benchmarks, not comparable.

## Weak spots
- No pooled r from any business meta-analysis was read. Everything is "positive, moderate" in words.
- The founding comprehensiveness studies (Fredrickson 1984, Dean and Sharfman 1996, Nutt 1993) and the McKinsey 2006 survey were never opened. The subfield's key claim (options before selection) has no read primary support.
- No study tests planning or option generation in an LLM on a firm-performance outcome. LLM evidence comes from proxy tasks (math, Blocksworld, code, simulations).
- opened:true on Wikipedia pages is not strong evidence.

## Only seen in snippets or abstracts
a07 to a19, b01 to b11, b13 to b19, b23 to b25, c03, c04, c25 to c27, critics of Illusion of Thinking.

## GAPS
1. What are the pooled correlations (r, CI, I2) in Boyd 1991, Miller and Cardinal 1994, George 2019, Hamann 2022, and do they survive publication-bias correction?
2. What do Fredrickson and Mitchell 1984 and Dean and Sharfman 1996 find on comprehensiveness (options considered) and performance, and under what instability conditions does it reverse?
3. Does any LLM study measure option-generation count against final decision quality in strategy tasks at equal tokens?
4. Doshi 2024 and Girotra 2023: actual correlations with expert rankings, idea-quality gains, and cost per idea.
5. Does a plan-first step beat direct answering for current (2025 to 2026) reasoning models at equal tokens on open-ended judgment tasks, not math?
6. Does planning help more under high uncertainty for LLM agents (difficulty-scaled planning budget), as Hamann 2022 suggests for firms?
7. Can model-based selection among strategic options be made reliable without a ground-truth checker; what verifier substitutes exist for business decisions?
8. What exactly did McKinsey 2006 report (sample size, percent of firms not using plans for key decisions)?
9. Brinckmann 2010 and Delmar and Shane 2003: effect sizes for planning in new ventures and the moderators.
10. Does the Camuffo 2020 RCT effect (performance, pivots) replicate in later RCTs of planning or hypothesis-testing training?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d21). Claims K05, K16 updated; K19 to K23 added. Web search quota was exhausted, and OpenAlex, Semantic Scholar and arXiv search were rate-limited, so work went through Crossref, direct arXiv PDFs, the Wharton PDF and the AEA registry. Wiley, SSRN and JSTOR returned 403, which blocks all the business meta-analyses.

Closed:
- Gap 8 (McKinsey 2006): CLOSED. N=796 executives, July/Aug 2006, firms of at least $500M revenue. Over 75% have a formal process, fewer than 25% say it is key to their most important decisions, 52% say a small senior group decides, 23% say the formal process does (d01, K19).
- Gap 4 (Girotra): CLOSED. Purchase intent 40.4% vs 46.8% vs 49.3%, 35 of top 40 ideas from GPT-4, about $0.63 per idea (d08). No expert-ranking correlation exists in that paper. Doshi stays abstract-only (d17).
- Gap 10 (Camuffo replication): CLOSED in direction. SMJ 2024 replication, 759 firms in four RCTs, shows more idea termination and a non-linear pivot effect; the abstract does not restate a revenue gain. Same research group. Independent Uruguay replication is registered, no results (d18, d19, d20, d21, K05).
- Gap 7 (verifier substitutes): PARTLY CLOSED. Aggregation (12-LLM crowd Brier 0.20 vs humans 0.19) and LLM judges (above 80% human agreement, with position, verbosity and self-enhancement bias) have numbers; none was tested on business-option selection except Doshi (abstract) (d15, d16, d17, K23).
- Gap 6 (difficulty-scaled budget): PARTLY CLOSED. Snell 2024 shows about 4x compute saving by difficulty on math; search hurts on easy items. Nothing tests it on firm-like decisions (d11, K22).
- Gap 5 (plan-first vs direct, 2025 to 2026, open-ended): PARTLY CLOSED. Only indirect evidence: chain-of-thought lowers accuracy on some judgment-type tasks (o1-preview -36.3 points vs GPT-4o on grammar learning) and longer reasoning can lower accuracy (Gema 2025). No equal-token plan-first test found (d12, d13, K21).
- Gap 3 (option count vs decision quality at equal tokens): PARTLY CLOSED. PlanSearch (code, with checker) shows diverse plans lift pass@200 from 55.6 to 77.0 (Claude 3.5 Sonnet) and diversity predicts the gain; Meincke 2024 measures diversity only. No strategy-task study found (d09, d10, K20).

Still open:
- Gap 1: no pooled r, CI or I2 for Boyd, Miller and Cardinal, George or Hamann. Only counts: Boyd 29 samples / 2,496 firms, "modest"; George 87 correlations / 31 studies, "moderate"; Hamann 183 samples. Publication-bias survival unresolved. The Shea-Van Fossen trim-and-fill result stays single-source.
- Gap 2: Fredrickson and Mitchell 1984 and Dean and Sharfman 1996 unreadable (JSTOR, no abstract). K17 stays single-source. The instability reversal is unverified.
- Gap 9: Delmar and Shane gives only an abstract (223 ventures); Brinckmann 2010 has no text at all.
- Goh 2026 vs Valmeekam 2024 on o1 Mystery Blocksworld: not reconciled.

Corrections and cautions found:
- George 2019 is in Public Administration Review, not a business journal.
- Camuffo 2024 replication abstract leads with termination and pivots, so "performs better" rests on the 2020 paper.
- Registry for the second Italian trial lists both 257 and 250 as the final count.
- PlanSearch's headline 77.0 is pass@200 (Claude 3.5 Sonnet), not pass@1 (40.3); it needs a test checker.
