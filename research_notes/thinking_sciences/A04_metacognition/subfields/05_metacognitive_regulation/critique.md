# A04.05 Metacognitive regulation: cross-check critique

Checked by re-opening PDFs (arXiv, Southampton eprints) for 10 key numbers. Notes were patched in the `limits` field of the affected evidence lines.

## Numbers re-opened

| # | Number | Source opened | Result |
|---|--------|---------------|--------|
| 1 | Huang: GPT-3.5 CSQA 75.8 -> 38.1 -> 41.8; GPT-4 GSM8K 95.5 -> 91.5 -> 89.0 | arXiv 2310.01798 Table 3 | Confirmed (columns are 1, 3, 5 calls, not "rounds") |
| 2 | Huang oracle figures | Table 2 | Confirmed: GPT-3.5 GSM8K 75.9 -> 84.3, GPT-4 95.5 -> 97.5, HotpotQA GPT-4 49 -> 59 |
| 3 | Tyen: GPT-4 52.87, 2,186 traces | 2311.08516 | Confirmed |
| 4 | SCoRe: 52.6 -> 41.4, 15.8% vs 4.6%, +15.6 | 2409.12917 | Confirmed |
| 5 | Overthinking 1,953%, 48.6%, ">92% first round correct" | 2412.21187 | Confirmed |
| 6 | Self-Correction Bench 64.5%, 89.3%, 156%, 5,306 traces | 2507.02778 | Confirmed |
| 7 | Didolkar +11.6% CoT, +7.52% PAL | 2405.12205 | Confirmed (abstract-level text) |
| 8 | Muncer r=.37 [.29,.44]; online .54 vs offline .30 | Southampton PDF | Confirmed (b02 right) |
| 9 | Think2 Llama-3-8B GSM8K 80.71/77.98/69.55; funnel 51.2/27.9/16.3 | 2602.18806 | Confirmed, with omission fixed (below) |
| 10 | s1 AIME24 50 -> 57 | 2501.19393 | Confirmed as 50.0 -> 56.7; "57.6" was wrong |

## Corrections made

1. **c14 (s1):** "57.6 with budget forcing" is wrong. 57.6 is GPQA Diamond in an ablation row. AIME24 is 50.0 without budget forcing and 56.7 with it.
2. **a11 (Muncer):** "complex maths r = .54" is wrong. Complex alone is r = .48 (n=12, k=21); simple is r = .10 (n=4). The .54 figure is the online-measure x complex-task cell (n=13), and that omnibus test was only marginal (p = .058). b02 had the online .54 vs offline .30 split right.
3. **c22 and c24:** "95.5 oracle" for GPT-3.5 GSM8K is wrong. 95.5 is GPT-4's standard score. GPT-3.5 oracle is 84.3.
4. **c02 (Think2):** omitted that plain CoT on CorrectBench is 75.02, higher than Ann Brown at 68.14. So the structure beat only the Standard prompt (52.91). On CRUXEval-O, Standard is 5.25, so Ann Brown (5.12) equals Standard, and CoT (25.62) is the outlier.
5. **a15 vs b10:** Huang's columns are 1, 3, 5 model calls. a15 called them rounds 1 and 2. Numbers are the same.

## Contradictions between sources

- Muncer figures appear in a10 (Ohtani .53/.23 as cited), a11 and b02 with different labels; resolved above.
- Human metacognition training effects range from g = .37 (Theobald) to .69 (Dignath) to .50/.63 (de Boer). Different samples, outcomes and moderators. No source reconciles them.
- Reflexion's gains (+22% ALFWorld) look like they contradict Huang. They do not: Reflexion has an environment signal, Huang removes it. Self-Refine's "20% average" is mostly style tasks.
- Meta-R1 and MetaRAG show cheap monitoring helps; Huang, Tyen and Stechly show self-monitoring fails. These are compatible only if the monitor is a separate or externally grounded model. Marked contested (K22).
- Think2 says forced metacognition hurts a weak model but helps error diagnosis (50% vs 25% improved); the accuracy results and the funnel results disagree in direction.

## Weak spots

- Founding human studies (Flavell, Brown, Nelson and Narens, Swanson, Perkins and Salomon, Schraw and Dennison, Mevarech and Kramarski) were NOT opened. Swanson's compensation finding, the item this subfield was framed around, rests on abstract-level secondary reports. Treat as unverified (K05).
- Dignath, Donker, de Boer, Theobald and Higgins numbers come from a secondary summary page, not the papers.
- Human findings are mostly correlational (r) and not causal. The online-measure advantage might reflect that online measures sample the same effort that drives performance.
- Many LLM results use old models (text-davinci-003, GPT-3.5, 2023 GPT-4). No 2025-26 frontier model was tested with a clean intrinsic-review arm, except Self-Correction Bench (open non-reasoning models plus Claude 3.5 Haiku and Sonnet 4).
- Most prompting results (metacognitive prompting, Plan-and-Solve, Didolkar) lack token-matched baselines. Gains could equal what extra self-consistency samples would give.
- Think2 is a 2026 preprint with two 8B models, greedy decoding, and counts as small as 12 of 24.
- Meta-R1 and MetaRAG use the authors' own benchmarks and have no independent replication.

## Only seen in snippets or secondary pages

a01-a08, a10 (Ohtani via secondary page), b01, b04-b08, b09 (small prompt studies), b20 (Wang and Zhao metacognitive prompting, local file lost; numbers rest on c10), a25 (Nezhurina, title page only), c22-c26 (syntheses, not sources).

## GAPS

1. Does the human self-question "Is it getting me anywhere?" work as a stop-or-switch trigger for a current LLM, tested against a trace-feature trigger (repeats, no new facts) and a fixed budget at equal tokens? No study found.
2. For frontier 2025-26 models (reasoning and non-reasoning), does an intrinsic review step still lower accuracy, or has post-training removed the Huang effect? Need a clean token-matched arm.
3. What external signals can a general-purpose agent get cheaply (unit tests, re-derivation, tool check, independent second sample agreement) and which of them gate review well? Which tasks lack any?
4. Does the "your step vs colleague's step" framing (Self-Correction Bench blind spot) help in a scaffold, and does it hold for current frontier models and for long agent traces?
5. What is the best stop rule for overthinking (first answer checks, then stop) versus underthinking (abandoned paths), and can one trigger handle both without hurting hard items?
6. Is a separate cheap monitor (Meta-R1 style) better than the same model monitoring itself at equal total tokens, and does it replicate outside the authors' benchmarks?
7. Did Swanson (1990) compensation replicate (metacognition offsetting low aptitude) and do any studies show a prompt-only, untrained version of it? Open the original and later tests.
8. How much of the human online-vs-offline gap (r .54 vs .30) reflects the measure versus the task, given I2 up to 99.9%? Does it predict which agent signals (trace vs stated confidence) to trust?
9. Do token-matched controls erase the gains of metacognitive prompting, Plan-and-Solve and skill routing on current models?
10. Does forced Planning-Monitoring-Evaluation structure hurt only weak non-reasoning models, or also strong ones when the task is easy? Needs the Think2 ablation on a larger model set.

## Gap search results (2026-11-01)

New evidence is in evidence_d.jsonl (d01-d17; 16 opened, d15 not opened). WebSearch, OpenAlex and Semantic Scholar hit their budgets part way through, so papers were fetched by known arXiv id and read as PDF text. Gaps that depended on discovering unknown papers are the most likely to be incomplete.

Closed or mostly closed
- Gap 3 (cheap external signals): mostly closed for what exists. Unit tests and tools help only when the feedback is good (d03: GPT-4 self-repair 1.05x over pass@20; human feedback 33.3% -> 52.6%). CRITIC without its tool falls back to self-consistency level (d14). Kamoi's survey says the feedback is the bottleneck (d02). Tasks without any tool or test have no studied gate; that part is an open design question, not a missing paper.
- Gap 9 (token-matched controls): closed for code, math and QA on 2023-25 models (d03, d04, d09, d14, d17). Controls often erase the gain. Still open: no matched control found for metacognitive prompting or Plan-and-Solve on current models.

Partly answered
- Gap 5 (overthinking vs underthinking): both halves are documented with numbers (d06 above 92% first-round correct; d07 switching goes with error on hard items), and difficulty decides which fix helps (d04). No single two-sided trigger was found or tested.
- Gap 4 ('Wait' / colleague framing): 'Wait' removes 89.3% of the blind spot on non-reasoning open models (d05). Sonnet 4 still shows 41.4%. No test on reasoning models, long agent traces, or with a length-matched filler.
- Gap 8 (measure vs task): indirect only. Hidden-state and confidence signals predict correctness well (d11, d12), which agrees with online beating offline in humans. The human I2 split by measure vs task was not touched.

Still open
- Gap 1 (self-question vs trace trigger vs fixed budget): no head-to-head found. All six working triggers use trace or internal features (d16).
- Gap 2 (Huang effect on frontier models): only old-model numbers (d01) and the Sonnet 4 blind-spot row (d05). No clean token-matched arm for 2025-26 models.
- Gap 6 (separate monitor vs self-monitor): Meta-R1 (d13) has no self-monitor arm and no independent replication. MetaRAG not rechecked.
- Gap 7 (Swanson replication): original still unread (APA 403, Crossref no abstract). No replication or prompt-only version found (d15).
- Gap 10 (forced PME structure on strong models): nothing new; Think2 still rests on two 8B models.

New claims K26-K34 added; K25 evidence extended. Source-level cautions: d05 uses injected errors on simple tasks; d13 and d14 row/model labels were partly ambiguous in the PDF text and are flagged in their limits fields.
