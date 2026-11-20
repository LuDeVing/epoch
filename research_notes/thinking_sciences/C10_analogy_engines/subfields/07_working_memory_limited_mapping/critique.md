# Critique: Working-memory-limited mapping (C10.07)

## Re-opened this session (numbers confirmed)
Waltz 2000 (springer PDF): .60 vs .39 F(1,41)=6.64; .35 vs .64 F(1,41)=12.48; Exp 2 F(1,103)=23.70. Confirmed.
Webb, Holyoak, Lu 2023 (arXiv 2212.09196): N=40, OR 1.88 [1.21,2.91], r(30)=0.39, OR 1.76/0.0007 zero-generalisation, story OR 0.37. Confirmed.
Webb, Holyoak, Lu 2024/2025 (arXiv 2404.13070, PNAS Nexus 2025): P=8.9e-13, P=0.496, P=0.066, 46% (23/50) vs 39%, N=99/97. Confirmed.
Lewis and Mitchell 2024 (arXiv 2402.08955): 136 Prolific recruited, 2 rejected on attention checks; accuracy table .753 / .488 / .350 / (.452 not re-read; the layout text was scrambled but order matches b09). Confirmed.
Hodel and West 2023 (arXiv 2308.16118): synthetic-alphabet GPT-3 accuracy <0.1; comprehension check at least 30% of original. Confirmed.
Gong et al. (arXiv 2305.03731 v4): capacity about 3, d' about 1 at n=3, noise lowers it. Confirmed.
Yasunaga 2024 (arXiv 2310.01714): GSM8K 75.0 vs 75.8-77.8 (GPT-3.5), 14.8 vs 50.3-61.0 (davinci), MATH 33.0 vs 33.9-37.3. Confirmed. Table 7 Codeforces ablation (14/27 and 15/29) does not match c25 (16 to 19, 30 to 37 for GPT-4); c25 left unverified.
Zhang 2024 (EMNLP): BBH category (ii) GPT-3.5 44.4 to 67.6 confirmed. Note GPT-4 answer-only is 72.8, so the gain vanishes at GPT-4.

## Corrections
1. c09 says human N=46; wrong. Lewis and Mitchell recruited 136 (134 kept). b09 is right. a18/c24 "N=46" claims also should read 134. (c24 carries the error.)
2. c10 names authors "Webb, Mondal, Cohen"; correct authors are Webb, Holyoak, Lu (a16 and b11 right). Venue PNAS Nexus 2025.
3. a20 says GPT-3 keeps "at least 30%" of accuracy; that is the counterfactual comprehension check, not the task. Task accuracy was below 0.1 on four of six types (c08).
4. Gong et al. dated 2023 (a10, c11) and 2024 (b13); same paper (arXiv v4, Feb 2024). Count it once.
5. b04/b05 Richey 2014 and a06/a07 Tohill and Holyoak were not re-opened; numbers stand on the first agent's reading.

## Contradictions
- Webb 2023 says GPT-3 beats humans on letter strings; Lewis and Mitchell find humans .753 vs GPT-4 .452. Cause is partly the human sample (their humans scored higher), partly the prompt (alphabet listed), partly counting failures (fixed by code).
- Webb 2024 says no alphabet effect on original vs new synthetic alphabets; Hodel/West and Lewis/Mitchell see collapse. Conditions differ (code tool, interval size).
- Count-limit (Halford, LISA) vs binding-quality (Chuderski) vs inhibition (Richland, DORA): unresolved.
- Working-memory training does not improve analogy (Richey), while correlational work shows strong links (Kyllonen and Christal r about .3 to .4 on digit span).

## Weak spots
- The subfield's named key work (Keane and Brayshaw 1988 IAM) and Keane 1994, Halford 1998, Hummel and Holyoak 1997 were never opened. All serial-mapping claims rest on memory. This is the biggest hole.
- No LLM study tests serial-vs-parallel mapping or a mapping-size cap directly. The n-back and counterfactual studies are indirect proxies.
- Most LLM data is GPT-3 to GPT-4 era; Musker 2025 is the newest and few 2025-2026 frontier-model results exist here.
- Waltz Exp 1/2 are between-subjects with small cells; no independent replication was found.
- c14, c15, c17 to c21 are peripheral (latent state, cognitive-load multi-agent, Raven encoding, slot models); only seen as abstracts or partial text. c21 saw a title page only.
- Snippet-only or not opened: a23-a30, c01-c04, c21, b22.

## GAPS
1. What do Keane and Brayshaw 1988 and Keane, Ledgeway, Duff 1994 actually report (order effects, numbers) for serial incremental mapping?
2. Has anyone tested an LLM with a cap on mapping size (3 to 4 relations per step) vs unrestricted at equal tokens?
3. Do 2025-2026 frontier and reasoning models still fail counterfactual letter-string and symbol-binding tasks, with and without tools?
4. Does asking a model for a joint (multi-object) mapping raise relational answers as it does in humans (Markman and Gentner; Waltz)?
5. Is there an independent replication of Waltz 2000 or of the anxiety effect (Tohill and Holyoak) with larger N?
6. Does context length or distractor load degrade LLM relational mapping the way a digit load degrades humans (attribute-match shift)?
7. Does an explicit role-filler binding table (Chuderski-style) beat relation-count limiting for LLM analogy accuracy?
8. Which structured-prompt gains (Zhang 2024, Yasunaga 2024) survive when token cost is held equal?
9. Is the Webb 2024 code-execution fix general to non-counting analogy tasks?


## Gap search results
Evidence is in evidence_d.jsonl (d01 to d17). Web search was unavailable (shared budget used up), so work used the Keane technical report, arXiv PDFs and the Semantic Scholar API.

1. CLOSED (partly). Keane, Ledgeway, Duff 1994 was read from the TCD technical report (1993 preprint of the journal paper). IAM order effect in people: Singleton-First 178.0 s vs Singleton-Last 363.1 s, Mann-Whitney U=7, p<.005, N=20. Similarity effect: 210.9, 164.9, 69.7 s, F(2,12)=12.02, N=21. IAM model runs: 1 vs 2.9 mappings, t(18)=-4.67. Cells are very small and nothing replicated them. Keane and Brayshaw 1988 itself still not opened. IAM has no fixed relation-count cap. (d01 to d05; claim K17 updated.)
2. OPEN. No LLM study with a mapping-size cap at equal tokens found. Nearest: operand count in I-RAVEN-X (d08).
3. PARTLY CLOSED. o3-mini and R1 fall to 17.0% and 23.2% on noisy long Raven-style items (d07, d08). Frontier late-2025 models (GPT 5.2, Gemini 3 Pro, Claude Opus 4.5) stay below humans on far-analogy grids without code (d14). No 2025-26 rerun of the counterfactual letter-string task was found, so that part stays open.
4. OPEN. No LLM test of joint vs single-pair mapping prompts found.
5. OPEN. No independent replication of Waltz 2000 or the anxiety effect found. Related load and distraction work (d15, d16) seen as abstracts only.
6. PARTLY CLOSED. Distractors and length hurt LLM reasoning (d09, d10, d07). Not yet shown on analogy mapping with relational vs attribute scoring.
7. OPEN. Models have an internal binding mechanism (d12). No explicit-table vs count-cap comparison found.
8. OPEN. Yasunaga 2024 admits more output tokens and gives no equal-token run (d17). Zhang 2024 was not re-checked for cost.
9. OPEN. Only counting was fixed by code execution (Webb 2024). No non-counting test found.

Still unverified: Yasunaga Table 7 Codeforces numbers (c25). The Lewis and Mitchell digit-matrix row assignment in d06 is inferred from scrambled table text.
