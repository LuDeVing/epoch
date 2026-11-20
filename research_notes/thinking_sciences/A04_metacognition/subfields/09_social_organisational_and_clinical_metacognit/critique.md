# A04.09 Social, organisational and clinical metacognition: cross-check critique

Files checked: evidence_a.jsonl (28 lines), evidence_b.jsonl (25), evidence_c.jsonl (28). Claims: claims.jsonl (19 claims, K01-K19).

## Numbers re-opened this session (10)
Confirmed against full text (arXiv PDFs and Europe PMC XML):
1. Kosinski 2023/2024: ChatGPT-4 75% (CI 66-84), ChatGPT-3.5 and davinci-003 20% (CI 11-29), davinci-002 5% (CI 0-10); 178-study child meta-analysis anchor. Confirmed.
2. Shapira et al. 2023: GPT-4 97% on original false-belief items; adversarial drops 93.8 to 68.8, 71.4 to 0, 66.7 to 0 confirmed.
3. Huang et al. 2023: GPT-3.5 CSQA 75.8 to 38.1 (3 calls) to 41.8 (5 calls); GPT-4 GSM8K 95.5 to 89.0 (5 calls); oracle GPT-4 GSM8K 97.5, HotpotQA 59.0. Confirmed.
4. SimpleToM (Gu et al. 2026): GPT-3.5 behaviour 7.6%, o1-preview 84.1%, judgment 10 to 24.9%, reminder results GPT-4o 82.8 / Llama 89.5 / Claude 96.9. Confirmed.
5. SimToM (Wilf et al. 2023): GPT-3.5 BigToM false belief 70.5 (+29.5 over 0-shot, +14.2 over CoT); ToMI false belief +47 over CoT for GPT-3.5; SC-CoT 33.5 vs SimToM 81.0; oracle 96. Confirmed.
6. FANToM (Kim et al. 2023): human ALL 87.5; GPT-4 0613 + CoT 26.6 (Jun) and 14.8 (Oct). Confirmed.
7. Hi-ToM (Wu et al. 2023): GPT-4-32k 60.42 / 55.81 vanilla, CoT 64.04 / 55.72. Confirmed.
8. Normann and Morina 2018: g=2.06 vs waitlist, 0.69 and 0.37 vs CBT, 1.72 / 1.57 overall, trim-and-fill 0.53, 13 trials co-authored by Wells. Confirmed.
9. Hi-ToM first author and Kosinski dates: see corrections.
10. Bahrami 2010 and Strachan 2024 numbers: NOT re-opened (Science paywall; Nature paper not fetched). They remain as recorded.

## Corrections
- a10 attributes Hi-ToM to "He et al."; first author is Wu (He is a co-author). c12 is correct. Treat a10 and c12 as the same paper.
- c15: "GPT-4 ToMI false belief +13.4" is wrong in scope. The paper text says GPT-4 gains 13.4 points on ToMI overall over 0-shot CoT, not specifically false belief.
- c21: "GPT-3.5 kept its GSM8K answer 74.7%" is actually the accuracy after round 2 (5 calls), not a retention rate. Round 1 = 3 calls, round 2 = 5 calls in the paper's table.
- a12/a11: the value 84.1 appears twice in SimpleToM (o1-preview behaviour prediction; Claude-3.5 judgment with reminder). They are different cells, not a duplication error.
- a17 is marked opened:true but the Science paper is paywalled; the numbers may come from a secondary text. Treated as unverified.
- Same-paper triple counting: Strachan (a14, a15, b13, c06-c08), Kosinski (a01-a04, c01, c02), Ullman (a05, b14, c03, c04), Normann (a19, a20, b01-b03, c25), Wang and Zhao (a13, b16, c19, c20), Kim (a08, a09, c09-c11) are single sources. Claims count them once (independent_sources).

## Contradictions and tensions
- Kosinski reads 75% as child-like theory of mind; Ullman and Shapira show the same models fail small alterations. Both hold: high on standard items, brittle on altered items. Strachan's human data adds that humans also fail some perturbation items (757 humans failed half), so the altered items are not clean either.
- CoT: helps in Kim/Wilf/Gandhi in some cells, hurts or is flat in Hi-ToM deception and in Huang self-correction. No single rule.
- Wang and Zhao metacognitive prompting gains vs Huang's finding that self-correction hurts: different tasks (NLU classification vs reasoning), different baseline (CoT vs standard); not directly comparable.
- MCT clinical effect sizes (g about 2) are against waitlist; against active treatment the effect is 0.37 at follow-up. Wells-group g 1.98 vs independent 1.49 (p=0.09) suggests allegiance inflation.

## Weak spots
- The subfield focus ("beliefs about others' minds; metacognitive therapy; Wells; Demetriou") barely transfers to the agent. Evidence on Wells' own model (S-REF, MCQ-3) was never opened (a26, a27 opened:false). Demetriou has a single line (a24) and no developmental numbers.
- No paper tests MCT techniques (detached mindfulness, attention training, worry postponement) on an LLM. The "agent_relevance" for the clinical block is mostly none.
- Multi-agent items (b17-b19) are 2026 preprints seen mainly at abstract or partial level; b18 and b19 have no numbers.
- b08 is a 2015 review of 10 RCTs, partly superseded by b07.
- b20-b25 and a26-a27, c27, c28 were not opened; c28 is our own analysis, not a source.
- SimpleToM is one source; claim K04 stays single-source.

## Seen only in snippets or not opened
a26, a27, b20-b25, c27, c28 (not opened). a07, a05, b18, b19 have no exact numbers. b12 abstract-level only.

## GAPS (most decision-relevant first)
1. Does an explicit "what does this party know" filter (SimToM-style) improve our agent at equal tokens on tasks where another party's knowledge matters (negotiation, user modelling), and does it still help for a strong reasoning model (SimpleToM suggests the gap closes with reasoning tokens)?
2. Is the knowing-doing gap (mental state right, behaviour prediction wrong) present in our agent, and does a reminder-in-system-prompt fix it as in SimpleToM (82.8 to 96.9%)?
3. For two-run ensembles of unequal quality, does confidence-weighted merging beat the stronger run alone at equal total tokens (Bahrami rule: ratio near 1 helps, low ratio hurts)? Need a direct LLM replication.
4. Where exactly does intrinsic revision help versus hurt a modern reasoning model (Huang 2023 used GPT-3.5/4)? Need a 2025-2026 replication with reasoning models and an external-signal control.
5. Do any peer-reviewed tests use Wells' MCT mechanisms (detached mindfulness, worry postponement, metacognitive beliefs) as agent control, for example against rumination loops in long reasoning chains? One targeted search found none.
6. What are the exact Bahrami 2010 and Strachan 2024 numbers from the open full text, and do Mahmoodi 2015 (equality bias) replicate in LLM groups?
7. How much of the clinical MCT advantage over CBT survives removing allegiance and low-quality trials (Normann 2018 gives 0.37 at follow-up, 0.53 trim-and-fill; any 2023-2026 independent RCTs)?
8. Does Demetriou's developmental ordering (executive, inferential, self-awareness) predict the order in which LLM capabilities appear with scale or reasoning training?
9. How do the nested-belief (Hi-ToM order 3+) failures change with reasoning models in 2025-2026?

## Gap search results (evidence_d.jsonl, d01-d16; claims K20-K23 added)
Constraints this run: WebSearch budget was exhausted, and the arXiv, Semantic Scholar and OpenAlex APIs returned 429. Evidence came from arXiv PDFs and Europe PMC full text. Absence of a result below means "not found here", not "does not exist".

1. PARTLY CLOSED. Thought-tracing (Kim 2025, d01-d03) is a second explicit mental-state routine. It beats CoT and most reasoning models at fewer tokens (ToMi 76.0 vs o1-medium 70.8, R1 68.3, o3-mini-medium 64.0). Reasoning tokens alone do not fix it. Still open: a test of this on our own agent at equal tokens, and negotiation or user-modelling tasks.
2. OPEN. No new knowing-doing gap data. Kim 2025 shows the related false-belief vs true-belief trade-off.
3. OPEN. No LLM replication of Bahrami-style confidence-weighted merging found (d15).
4. PARTLY CLOSED. Tyen 2024 and Kamoi 2024 (d04, d05) give a mechanism and a survey verdict: finding the error is the bottleneck, and prompt-only feedback does not work. K09 upgraded to established (three sources). No 2025-2026 reasoning-model test with an external-signal control was found.
5. OPEN. Detached mindfulness has only human trials (d13: g -1.80, k=3). No LLM test.
6. HALF CLOSED. Strachan 2024 numbers verified from full text (d07). Bahrami 2010 full text not available from Europe PMC; Mahmoodi 2015 LLM replication not found.
7. PARTLY CLOSED. 2025-2026 trials (d08-d12): independent OCD RCT vs TAU, g -1.12 to -1.54, but mechanism not supported; Exner non-inferiority vs ERP not confirmed at 6 months (second-hand); independent tMCT vs CBT trial only a protocol. Waitlist-based effects remain; the CBT advantage is still weak.
8. OPEN. Nothing found linking Demetriou's order to LLM capability order.
9. OPEN. No Hi-ToM order 3+ result for reasoning models found; thought-tracing covers first-order tasks only.

Evidence opened this session: 12 of 16 lines. Not opened: d06 (SCoRe abstract only), d11 (second-hand), d15, d16 (search records).
