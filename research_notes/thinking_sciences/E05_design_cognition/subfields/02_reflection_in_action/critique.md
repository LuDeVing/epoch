# E05.02 Reflection-in-action: cross-check and critique

Checked by re-opening sources this session: arXiv full text via pdftotext (Huang, Reflexion, Tyen, Stechly, Self-Refine, Renze, Tsui, SCoRe), the Suwa 2001 PDF, and the UTS record for Kokotovich. 19 claims in claims.jsonl.

## Corrections made (numbers re-checked against source)
1. b01 is WRONG. It gives GPT-3.5 oracle numbers as GSM8K 95.5, CSQA 82.0, HotpotQA 49.0. Those are the GPT-4 no-oracle baselines. Huang Table 2: GPT-3.5 standard 75.9/75.8/26.0, oracle 84.3/89.7/29.0; GPT-4 standard 95.5/82.0/49.0, oracle 97.5/85.5/59.0. a18, c05, c06 are right. Ignore b01's numbers.
2. b08 is WRONG on Leetcode. Reflexion Table 1: MBPP Python is 80.1 (GPT-4) vs 77.1 (Reflexion); Leetcode Hard Python is 7.5 vs 15.0 (Reflexion wins). a14 is right. The "below GPT-4 alone" result belongs to MBPP only.
3. a31 and c26 say Kokotovich (2015) could not be found. b24 found it (UTS record, IASDR 2015, pp. 1115-1128). Re-opened: the abstract says the designer draws on prior pattern and knowledge "in a spontaneous tacit way", that this "has some limitations", and that designers "may limit the field of issues". The task brief is confirmed. Abstract only, conceptual, no data.
4. a21 labels the +23.53 gain as word sorting. In Tyen Table 6 the text extraction scrambles the task labels; the row with -11.11/+23.53 sits beside "Tracking shuffled objects". Numbers per row are right (true location: +23.53, +43.92, +36.86, +18.04, +18.06; random: +11.76, +20.39, +21.57, +10.59, +5.16). Task-to-row labels in a21, b10, c16 are unreliable.
5. b10 says random-location loss on correct traces is "-8.89 to -15.91". Actual range is -6.67 to -15.91 (c16 is right).
6. Confirmed with no change: Huang Tables 3, 4 and 7 (CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5/91.5/89.0; GPT-4-Turbo 91.5/88.0/90.0; 74.7% retention; debate 83.2/83.0 vs vote 85.3/88.2); Reflexion 130 of 134, 16.3% vs 1.4% false positives, Rust-50 0.60/0.52/0.60/0.68; Tyen 2186 traces, 52.87, 85%/15% split; Stechly 16% baseline, 1 of 100, about 40% at n=15; Renze GPT-4 0.786/0.827/0.876/0.925/0.932/0.971; Tsui 64.5%, 89.3%, 156%, 5,306 traces, 76.0%; Suwa 2001 340 segments (136/182/22), 606 and 171, group means 27.2/44.6/49.6 and F values; Self-Refine math 64.1 to 64.1 and 94% "looks good"; SCoRe -11.2, +4.4, 15.6 (HumanEval 9.1 headline, +12.2 second-try delta).
7. Self-Refine constrained generation appears as 28.0 to 37.0 (b05, GPT-3.5 column) and 29.0 to 49.7 (a23, c04, GPT-4 over 3 iterations). Both are real but different models. Do not compare them.

## Contradictions between sources
- Huang (self-correction hurts) vs Liu 2024 (fair prompts, temperature 0, small gains; a28 has only p-values): prompt wording matters. K09 is marked contested.
- Self-Refine (about 20 points gain) vs Huang: Self-Refine tasks are stylistic or checkable; Huang's are single-answer reasoning. A boundary condition, not a true conflict. Huang also notes some earlier gains came from a better initial prompt or more calls.
- Reflexion ablations: dropping the written reflection left Rust-50 at 0.60 (full 0.68), but on HotPotQA reflection added 8 points over episodic memory only (100 questions). Value of the reflection text is mixed.
- Renze: big gains, but only on items already known to be wrong. Same mechanism as Huang (the signal does the work), opposite-looking headline.
- Tyen: even a correct locator costs up to 11 points on traces that were already right.

## Weak spots
- The human foundation (Schon 1983, Schon and Wiggins 1992, Goldschmidt 1991, Valkenburg and Dorst 1998, Suwa 1998, Dorst and Dijkhuis 1995) is from memory or abstract only (a03, a04, a05, a07, a08, a09 opened:false). No numbers for Quist and Petra.
- The human numbers rest on one expert (Suwa 2001, one coder for the main analysis) and one novice experiment with self-selected groups. Mejia 2018 found 2 vs 3 unexpected discoveries in two protocols, no clear link to creativity, coder agreement 62% and 71%. Mangano 2015 is observational.
- Machine results mostly use GPT-3.5, GPT-4 (2023) and Llama-2. No 2025-2026 frontier retest of Huang's setting was found. Tsui 2026 tests open non-reasoning models only.
- Reflexion's ALFWorld win uses a hand-made hallucination detector plus an environment signal, so it is not reflection alone.
- No study tests Schon's predictions against an LLM (a30, c28). Search limits (rate-limited OpenAlex and Semantic Scholar) make this absence weak.
- The 2025-2026 design-with-LLM papers (c21 n=18, c22 n=25, c23, c24) are qualitative or conceptual, with no effect sizes.
- "independent_sources" counts overstate independence: many results share benchmarks (GSM8K, CSQA) and prompts, and Kamoi is a review of the same papers. K01 and K02 were set to the number of truly separate groups.

## Only seen in snippets or abstract
Schon 1983 (Wikipedia summary), Eklund 2023 (abstract; full text 403), Kokotovich 2015 (abstract), Suwa 2000 (search summary), Suwa and Tversky 1997 (abstract), Liu 2024 (partial), Eraut timing critique (memory).

## GAPS
1. At equal tokens, does an S5 revise pass triggered only by a code-side check beat best-of-N plus a code selector on our benchmarks? No paper compares them with a matched budget.
2. Does Huang's result (self-correction hurts) hold for 2025-2026 reasoning and frontier models, with thinking tokens on? Only Tsui 2026 (open non-reasoning models) was found.
3. How much of Reflexion's gain comes from the written lesson versus retrying with a failure flag? Ablations disagree (Rust-50 no change, HotPotQA +8, Renze Retry 0.827 vs Explanation 0.876).
4. Does a program-made error locator (failing test, stack trace, constraint violation) reach Tyen's true-location gains (+18 to +44 points), and what does it cost on traces that were already right (up to -11)?
5. Does Kokotovich's narrowing claim have a measurable form: do revise loops anchor on the first frame, and does a problem-space map step before revising reduce it? No empirical test found.
6. Does a neutral continuation marker ("Wait") or attributing the output to someone else raise revise quality at no extra calls on frontier models? Tsui covers only 14 open models.
7. What do Schon's original cases (Quist and Petra, Schon and Wiggins 1992) actually count? Needed to know whether back-talk has any measured human rate beyond Suwa 2001's 28% (one architect).
8. Has Suwa, Gero and Purcell's unexpected-discovery rate been replicated with more than one designer, and does it predict outcome quality (Mejia 2018 says unclear)?
9. For open design-like tasks with no checker, which feedback source works (human, rubric program, a second model with a different prompt)? Self-Refine says specific feedback helps; Huang says self-feedback fails on reasoning; the middle is unmeasured.

## Gap search results

Search tools were limited in this pass (WebSearch budget used up; arXiv, OpenAlex and Semantic Scholar rate-limited). Sources were fetched by known arXiv id and read as PDF text. Evidence is in evidence_d.jsonl (d01 to d18). Claims K01, K03, K05, K06, K09, K11, K12, K13, K16, K17, K19 were extended and K20 to K26 were added.

Correction to the gap wording: Reflexion's Rust-50 ablation does not show "no change" from the lesson. The tests-only arm (no written reflection) scored 0.60, equal to the base, and full Reflexion scored 0.68. So the lesson added 8 points there and 8 on HotPotQA (d08, d09). The small-N caveat stands (50 and 100 items).

- Gap 1 (S5 revise vs best-of-N at equal tokens): PARTLY CLOSED. Olausson 2024 compares repair with resampling at matched budget in code: modest, uneven gains, 1.05x and 0.97x of baseline in the cells quoted, up to +8% (GPT-4, APPS) and +34% (GPT-3.5, competition problems) (d01). Snell 2024: trained revisions narrowly beat parallel sampling on MATH (d03). No test with a prompt-only revise pass, a code selector and a frontier model. Stays open for our benchmarks.
- Gap 2 (Huang on 2025-2026 frontier models): PARTLY CLOSED. Zhang 2025 finds accuracy falls in all four tasks including o1-family models and R1 in a blind pass (d12). Tsui v3 (Aug 2026) adds reasoning models and finds a small or negative blind spot (d10). Nobody was found who reran the Huang setup on GPT-5-class or Claude thinking models with thinking budgets varied. Open.
- Gap 3 (lesson vs retry flag): PARTLY CLOSED. Self-Debug: bare flag gives most of the gain, MBPP GPT-4 72.8 to 78.8, with tests 80.6 (d06). Reflexion: lesson adds 8 points in two small tests (d08, d09). Renze: 0.827 vs 0.876. Net: the flag is the larger part, the lesson a few points. Claim K22 is marked contested. No clean three-arm test at equal calls.
- Gap 4 (program locator reaching Tyen gains, cost on right traces): STILL OPEN. Indirect: Olausson shows feedback quality is the bottleneck even with execution results (d02); Snell shows 38% of correct answers flipped by a naive revision (d04); ProcessBench shows model locators are weak (d13). No paper gives the gain of a stack trace or constraint violation as locator, with the cost on correct traces.
- Gap 5 (Kokotovich narrowing measurable): STILL OPEN. No test of anchoring on the first frame or of a problem-space map step. Only looping and over-thinking counts exist (d12). Claim K24 says so.
- Gap 6 (neutral "Wait" or other-author framing at no extra calls on frontier models): PARTLY CLOSED. Tsui v3 gives Claude 3.5 Haiku 52.5% and Sonnet 4 41.4% blind spot, and "Wait" brings non-reasoning models close to their reasoning siblings (d10). s1 ablation: "Wait" 53.3 vs "Hmm" 50.0 vs none 50.0 on AIME24, 30 questions (d11). The prefill trick is not available on most closed APIs, and no test through instruction text only was found.
- Gap 7 (Schon's case counts): STILL OPEN. Only Crossref records were reached; the sister abstract confirms a narrated workshop example. No tally found (d17).
- Gap 8 (replication of unexpected-discovery rate): STILL OPEN. Full texts unreachable; no multi-designer replication found; absence is weak because search was limited (d18).
- Gap 9 (feedback source on open tasks): STILL OPEN, with side evidence. For code a stronger model or a human critic beats same-model feedback (33.3% vs 52.6% repaired, d02); same-model judges favor their own text (d15); Kamoi says the open-text middle is unexplored (d05, d16). Claim K26 is contested.

Weak spots of this pass: Tsui v3 read only to character 100000 of 134709; the Self-Debug and Zhang tables were scrambled by text extraction, so per-cell values are marked approximate; abstract-only for ProcessBench, Gandhi and Panickssery.
