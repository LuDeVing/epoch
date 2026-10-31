# Critique: extraneous load and split attention (cross-check of evidence a, b, c)

Checked 2026-10-31. Claims are in `claims.jsonl` (A08.02-K01 to K23). Evidence file d was not part of this pass.

## 1. Numbers re-opened (arXiv full text read this session, PDFs deleted afterwards)

| # | Number | Source | Result |
|---|---|---|---|
| 1 | Shi 2023: at most 18 percent of solved base problems solved for all distractor types; fewer than 30 percent consistently solved | arXiv 2302.00093 | Confirmed |
| 2 | Shi 2023: chain-of-thought micro accuracy 72.4 to 77.8 with the ignore instruction | same, Table 3 | Confirmed |
| 3 | Shi 2023: macro accuracy "8.3 to 20.0" (evidence a21) | same, Table 3 | CORRECTED. 8.3 and 20.0 sit in the "Norm" macro column. Overall macro is 6.0 to 15.0 (as c02 says). Use c02. |
| 4 | Shi 2023: self-consistency +35.5 points on 0-COT | same, text | Confirmed (text: 35.5 percentage points, 0-COT) |
| 5 | Levy 2024: mean accuracy 0.92 to 0.68 at 3,000 tokens | arXiv 2402.14848 | Confirmed (abstract-level line in the intro) |
| 6 | Mirzadeh 2025: GSM-NoOp drops up to 65 percent | arXiv 2410.05229 | Confirmed |
| 7 | Weston 2023: 62.8 to 80.3 (oracle 82.0); GSM-IC 51.7 to 61.3 | arXiv 2311.11829 | Confirmed |
| 8 | Liu 2024: more than 20 points; closed-book 56.1; oracle 88.3 | arXiv 2307.03172 | Confirmed |
| 9 | Du 2025: 13.9 to 85 percent; at least 7.9 percent with masking; Mistral GSM8K 35.5 to 66.7 (up to 31.2) | arXiv 2510.05381 | Confirmed |
| 10 | Adapala 2025: Gemini 0.85, 0.82, 0.78, 0.72; slope -0.003 (p<0.001); GPT-4o 0.65 to 0.55, p=0.07, 32 percent of outputs lacking a final answer; Long Control p=0.45 | arXiv 2509.19517 | Confirmed. New detail: Llama and Mistral models scored 0.00 in all conditions (floor), so only two of five models carry the result. |
| 11 | Laban 2025: 39 percent average drop, 15 LLMs, 200,000+ simulations, visible in two-turn conversations | arXiv 2505.06120 | Confirmed |

Not re-checkable: Ginns 2006 (publisher abstract is withheld in Crossref and Semantic Scholar; OpenAlex rate-limited). The human-side numbers (Kalyuga 1999, Cammeraat 2020, Beege 2019, de Koning 2020, Cierniak 2012) were not re-opened here; they are taken from the a and b agents' "opened" flags.

Small internal oddity in Adapala: a slope of -0.003 per percent load predicts about -0.24 at 80 percent load, but the observed Gemini drop is 0.13 (0.85 to 0.72). The linear fit is rough; quote the cell means, not the slope.

## 2. Contradictions between sources

- Ginns 2006 effect size: 0.72 on 37 effects (Clearing House) vs d 0.85 on 50 studies, 2,375 novices (He and Loewen 2024) vs 0.89 (Frontiers). Likely the 50-study figure merges spatial and temporal contiguity. Unresolved (K02).
- Human meta-analyses say integration helps; Cammeraat 2020 (Exp 2) and Beege 2019 (Exp 1) found no effect. Meta-analytic means can hide a mix of strong and null studies, and publication bias is not discussed in any source we read.
- Load as the mechanism: theory says integration lowers extraneous load. Cierniak 2012 found no secondary-task difference and only 8 to 16 percent mediation; Wang 2016 found a small rated-load effect (d -0.24). The effect may be real while the stated mechanism is weak (K07).
- LLM length: Du 2025 and Levy 2024 say length alone hurts. Adapala 2025 says long control did not differ (p=0.45) and attributes the loss to distractor content. Du used whitespace on weaker open models; Adapala used a different task and mostly floor-level models. Not reconciled (K10).
- Random noise: Cuconasu 2024 found random unrelated documents helped (up to +35 percent), against the "all extraneous text hurts" reading. It was a retrieval-augmented setting with a specific model.
- Integration vs separation in machines: VMMU found separating text from image evidence helped (+7.97 mean), opposite to the human rule. The VMMU comparison is a rendering change (one page vs separate inputs), not a clean split-attention test.

## 3. Weak spots

- No direct LLM test of the classic contrast (integrated vs separated sources) was found. All LLM evidence is adjacent: distractors, length, position, compression. The agent_test column is therefore the main new evidence we can produce.
- Founding study (Chandler and Sweller 1992) never opened; second-hand only (K23). The human story rests on Kalyuga 1999 (N=34 and N=16 apprentices), Sweller 1994 (review, no figures) and three meta-analyses of which only one number (g 0.63) was read, and that through a German summary.
- LLM extraneous-load papers (Adapala, CogniLoad, ToolLoad) borrow CLT words but are not tests of the human effect. Adapala has 200 questions, two usable models and a truncation confound.
- Older models dominate the key distractor evidence: code-davinci-002 and text-davinci-003 (Shi), LLaMA-2 (Weston, Sclar). Mirzadeh 2025 reports o1-preview falling too, but strong 2025-2026 reasoning models are barely covered. Du 2025 shows only small drops for Claude and Gemini on GSM8K (-3.8 to -8.5).
- Mitigation numbers (S2A, recite, LongLLMLingua) are each from one lab, different models, and the cost of the extra call is mostly not counted against equal tokens (our guardrail G7).
- Single-study claims: audio and colour-coding (K06), imagination or mental-integration instruction (K08), multi-turn sharding (K16), format sensitivity (K17), VMMU (K18).

## 4. Seen only in snippets or abstracts (do not quote figures without opening)

Chandler and Sweller 1992 (a01); Pouw 2019 (a18, b05); Schmidt-Weigand 2010 (a19); Ayres and Sweller 2005 (a26); Cierniak, Scheiter, Gerjets 2009 (a27); Wang 2016 (b03, search snippet); Ginns 2006 (b01, via citing papers); ToolLoad-Bench abstract (b23); Cognitive Overload Attack (b24, c28); Ok and Lee 2026 prompt order (c06, 14 points CQO over QOC); Fu 2025 Exclusion of Thought (c27); the c21 "no direct LLM study" negative result is a first-pass search only.

## 5. Corrections made

1. Shi macro accuracy: use 6.0 to 15.0 (overall macro, COT), not 8.3 to 20.0 (that is the normalised column).
2. Adapala: added floor effect (three of five models at 0.00) to the claim that gets cited for "extraneous load slope".
3. Ginns effect size: demoted to "contested" rather than listing 0.72 or 0.85 as fact.
4. Evidence pairs a14/b06, a11/b02, a20/b16/c01, a22/b20/c04, a24/b17/c08, a23/c09 describe the same studies; counted as one independent source each in `claims.jsonl`.

## GAPS

1. Does the classic contrast (facts and referents integrated vs separated, same tokens) change accuracy in current LLMs at all? No direct study exists; this is the key test for S1/S2 and for the "integrate" half of the prompt rule.
2. Which of the filter-then-answer fixes (code-side removal, ignore instruction, S2A rewrite, recite-then-answer) wins at equal total tokens, counting the extra call, on strong 2025-2026 models?
3. Do strong reasoning models still lose accuracy to inert or near-miss clauses, and how much? Mirzadeh's o1-preview drop and Du's small Claude drops disagree on scale; no clean recent measure.
4. Is the Du 2025 length penalty real for clean, task-relevant context at agent lengths (5k to 30k tokens), given Adapala's null for long control?
5. What are the real numbers in Chandler and Sweller 1992 and Ginns 2006 (full text)? Resolve 0.72 vs 0.85 and confirm the founding experiments.
6. How much of the human pooled effect survives bias correction (publication bias, preregistered replications such as Cammeraat 2020)? Sets how strongly to trust the human analogy.
7. Does element interactivity (human d 0.78 vs 0.28) predict where restructuring helps LLMs, so the S0 gate can switch it on only for hard items?
8. Do near-miss (related but wrong) distractors hurt more than random ones in reasoning tasks (not only retrieval QA), and can code detect and drop them cheaply?
9. In multi-step agent runs, which history treatment (full, masked, summarised) is best at equal tokens on our own tasks, and does it interact with fresh-context attempts in S3?
10. How large is layout-noise (Sclar) for our own prompt format, so that any integrated-vs-separated difference smaller than that spread is ignored?

## Gap search results (2026-10-31, evidence_d.jsonl d01 to d37, claims K24 to K28 added)

Tool limits in this pass: web search quota spent, arXiv export and OpenAlex and Semantic Scholar rate-limited. Worked: ERIC API (abstracts), Crossref, Springer landing pages, direct arXiv PDFs. Publisher pages for Ginns 2006 and Chandler and Sweller 1992 returned 403.

| # | Gap | Status | What was found |
|---|---|---|---|
| 1 | Integrated vs separated in current LLMs | OPEN | Second search, still no direct study (d37). Nearest: premise order (d32): shuffled order costs 20 to 40 points, so any test must fix use-order (K25). |
| 2 | Which filter-then-answer fix wins at equal tokens on 2025-2026 models | OPEN (partly) | No equal-token comparison found. Masking vs summary in agents is measured in dollars: masking about equal to summary, half the raw cost, but a thinking model got worse with either (d27). |
| 3 | Strong reasoning models vs inert clauses | CLOSED (qualitatively) | Yes, they still lose. o1-preview -17.5 on GSM-NoOp (d14), Claude Opus 4 about 100% to 85-90% and R1 70% to 30% (d29), Cats 3 times error (d13), GSM-DC 2025 models 43% to 19% and 26% to 2% (d28). Size depends on task; no clean 2026 number (K24). |
| 4 | Length penalty for clean context at 5k to 30k | PARTLY CLOSED | RULER: GPT-4 loses about 3 points to 32K, Llama3.1 70B 1.7 points (d35); multi-hop loses much more than single-span (d12). Penalty is small at agent length for strong models and grows with reasoning depth (K27). Adapala vs Du conflict not reconciled. |
| 5 | Real numbers: Chandler and Sweller 1992, Ginns 2006 | PARTLY CLOSED | Ginns: 50 independent studies pooling spatial and temporal, d 0.85 (CI 0.68 to 1.02, second-hand), so the 0.72 vs 0.85 clash is a scope difference (K02 now established). Chandler and Sweller 1992 still not opened (K23). |
| 6 | Bias-corrected human size | OPEN | First-hand: g 0.63 on 58 comparisons (d21). No bias correction visible in abstracts. Recent human tests are mixed: Beege 2019 null, Florax 2010 retention only, Zhang 2022 and 2024 null, 2023 positive, Cammeraat 2020 null (d23 to d25, d01, d02). Schroeder 2020 finds load measures do not back the extraneous-load story (d22). |
| 7 | Element interactivity as a gate | PARTLY CLOSED | Human: d 0.78 high vs 0.28 low complexity (second-hand, d20). LLM: multi-hop vs single-span (d12) and step count in GSM-IC (d30) point the same way, but no direct LLM test (K27 gives the test). |
| 8 | Near-miss vs random distractors in reasoning | PARTLY CLOSED | Reasoning: same-topic, shared role names, in-range numbers hardest (d30). Retrieval: related-wrong -25% per distractor, random +35% (d31). Code detection of near-misses not tested. |
| 9 | History treatment at equal tokens, with S3 fresh context | OPEN (partly) | Masking is a cheap default for tool-heavy agents; summary lengthens runs; thinking models may need history (d27). Nothing on interaction with fresh-context attempts. |
| 10 | Layout noise for our format | PARTLY CLOSED | General size known: std up to 35% of mean across templates, chance-level worst cases (d36). Our own spread must be measured. |

Changes to claims: K02 contested to established (scope explained); K17 single-source to established (two sources); K15 narrowed with the thinking-model counterexample; K19 and K23 rewritten, still open; K03, K04, K07, K09, K10, K14 extended; K24 to K28 added.

Remaining open, in order of value: (1) run the integrated-vs-separated test on our harness with fixed use-order, several templates and seeds; (2) get the full texts of Chandler and Sweller 1992 and Ginns 2006 (library access); (3) equal-token comparison of filter fixes on the current model.
