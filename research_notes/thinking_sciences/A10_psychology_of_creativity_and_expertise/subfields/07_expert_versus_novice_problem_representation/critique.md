# Critique, A10.07 Expert versus novice problem representation

## Corrections and confirmations (sources reopened as PDF text this session)
- Step-Back (arXiv 2310.06117), table read: PaLM-2L physics 66.4 / CoT 65 / Step-Back 73.2; chemistry 70.9 / 75.3 / 81.8. GPT-4 physics 69.4 / CoT 82.9 / Step-Back 84.5; chemistry 80.9 / 85.3 / 85.6. 20.5% fixed, 11.9% introduced, over 90% of residual errors in reasoning. CONFIRMED. Note: file a12 omits GPT-4 Step-Back (84.5), and the headline "+7%" hides that the GPT-4 gain over CoT is only +1.6 (physics) and +0.3 (chemistry). Recorded in claim K09.
- GSM-IC (2302.00093): CoT micro 72.4, macro 6.0; LTM micro 77.5, macro 18.0. CONFIRMED. CORRECTION: c02 says least-to-most "roughly doubled" macro; the paper text says about double, but its table shows 6.0 to 18.0 (tripled). Use table values.
- GSM-Symbolic (2410.05229): up to 65% drop (Phi-3-mini), o1-preview -17.5, Gemma-7b-it -20.6, Mistral-7b-v0.3 -24.0, best-to-worst gap over 12%. CONFIRMED.
- Kortemeyer (2508.08842): 60 items, 24/26 (92.3%), 27/30 and 25/30. CONFIRMED.
- Wolf et al. (1201.6601): 18 professors, 23 novices, 50 problems, same average category count (no significant difference), PCA first components about 87% of variance. CONFIRMED in outline; the exact means 10.8 and 11.4 were not located in the text extract, so they stay as reported by agent b.
- Mason and Singh (1602.08775, 1602.08781): classes 109/114/180; 18% Newton 2, 31% energy, 44% linear kinematics (version II); 34.4% vs 18.7%; p=0.90. CONFIRMED. The percentages come from version II, Chi problems.
- NOT reopened: Hardiman et al. 1989 numbers (agent b marked opened; I could not retrieve the paper), Chi 1981 percentages (b01 unopened, from secondary accounts). Treat as likely but unverified.

## Contradictions between sources
- Chi: novices surface-based vs Mason and Singh: many intro students choose expert categories; Hardiman: novices 59% deep choice. Likely reasons: item set, free vs forced choice, course level. Wolf: standard metrics do not separate groups at all.
- Chi's experts were grad students; Mason and Singh show faculty are far better, so the founding contrast is weaker than cited.
- Webb et al. (GPT-3 above humans on letter strings) vs Lewis and Mitchell (GPT below humans even on the standard alphabet): different samples, prompts, models.
- GSM-Symbolic's "pattern matching, not reasoning" reading is contested; o1-style models lose far less.
- Kortemeyer (strong LLM sorts by method) and Shi/Mirzadeh (distractor capture) can both hold: naming the method is easy, applying it under noise is not.

## Weak spots
- Agent a is mostly unopened memory (a01-a09, a21-a25): Gick-Holyoak (about 10% / 75%), Ross, Adelson, Weiser-Shertz, Gentner numbers unverified.
- Only one LLM card-sort study, one run, author-coded.
- Step-Back, Buffer of Thoughts, GSM-IC results are on older models; little on 2025-2026 reasoning models.
- Many claims are single-source (K03, K04, K06, K09-K11, K16, K17).
- No equal-token comparison in any LLM study; scaffold gains may partly be extra compute.
- Only seen in snippets or secondary: Veldhuis, Singh 2009, Lin and Singh 2010, Schoenfeld and Herrmann, Larkin 1980, Bhaskar and Simon, MAC/FAC.

## GAPS
1. Does an explicit S2 typing or principle step help a current reasoning model at equal tokens, or only weak models (Step-Back GPT-4 gain over CoT was +0.3 to +1.6)?
2. Do several current LLMs (not only GPT-5 Thinking) reproduce method-based sorting on a principle-by-surface crossed item set, over repeated runs with fixed coding rules?
3. Does the distractor and NoOp drop persist for 2025-2026 reasoning models, and does restate-and-strip beat plain CoT at equal tokens?
4. Is representation quality causal for solving in LLMs (forced wrong type labels), not just correlated as in Hardiman Experiment 2?
5. What are the actual Chi 1981, Gick-Holyoak, Ross and Schoenfeld-Herrmann numbers (open originals)?
6. How well do self-generated type labels agree with human structural labels on code tasks (Adelson, Weiser-Shertz analogues)?
7. When structure and surface agree (Ross), does forcing S2 add cost without benefit? Where is the break-even?
8. Does structure-labelled exemplar retrieval beat surface-embedding retrieval for agent memory at equal context size?
9. Is expert-like categorisation in LLMs robust to prompt-format changes (Sclar-style swings of up to 76 points)?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d18). Limits of this pass: the WebSearch budget was used up, and the arXiv, OpenAlex and Semantic Scholar search endpoints returned 429. Only papers fetched by known id could be opened. So "stayed open" often means "not found", not "shown absent".

1. S2 step at equal tokens on a current reasoning model: STAYED OPEN, leaning negative. No direct test found. Indirect: CoT helps mainly on math and symbolic items (d06), Self-Discover on GPT-4 gains only +2 on MATH (d08), skill exemplars +1.3 on GPT-4 GSM8K (d09), R1 authors say few-shot prompts hurt (d07). Claim K18 added as contested.
2. Several LLMs sorting by method: STAYED OPEN. Nothing beyond Kortemeyer found (d18).
3. Distractor drop in 2025-2026 reasoning models: PARTLY CLOSED. It persists but is smaller in absolute terms: R1 error 1.5% to 4.5% (d03), IMOAnswerBench drops 9-15% under long irrelevant context with reasoning cut up to 74% (d02), Qwen3-8B loses 14-20 points on Bangla distractor math (d04). Restate-and-strip versus plain CoT at equal tokens was not tested with a prompt; DAGGER's typed graph with distractor nodes (fine-tuned) is the nearest, with 89% fewer tokens (d04). K07 and K08 updated.
4. Causality of representation quality: STAYED OPEN. No forced-wrong-label study. Indirect work shows stated reasoning and hints often do not drive answers (d12, d13). Claim K21 added.
5. True original numbers: PARTLY CLOSED. Chi 1981 percentages obtained from a reproduced table (d01, claim K20); the original is paywalled and unopened. Gick-Holyoak percentages, Ross, Schoenfeld-Herrmann and Hardiman remain unverified; Webb et al. gives only the qualitative GPT-3 replication of Gick-Holyoak (d17).
6. Self-generated type labels vs human labels on code: STAYED OPEN. Only a hint that label quality depends on the annotator model (d10).
7. Break-even when surface and structure agree: PARTLY CLOSED as direction only. Overthinking costs on easy items (d05), verbalisation can hurt on pattern tasks (d15), similarity retrieval is enough on i.i.d. items (d11). No break-even point measured. Claim K19 added.
8. Structure-labelled vs surface-embedding retrieval: PARTLY CLOSED. Skill labels beat embedding retrieval by 5.2 points on GSM8K with GPT-3.5 at 8 shots, but only +1.3 on GPT-4 (d09); structure-coverage selection gains up to 23 points where similar examples are insufficient (d11). Not tested on agent memory.
9. Robustness to prompt format: PARTLY CLOSED. Paraphrases change scores and rankings with only moderate rank agreement (d14); no sorting-specific test.

Correction carried forward: the least-to-most GSM-IC change was a tripling (6.0 to 18.0), now written into K08.
Retry when quota refills: gaps 2, 4, 6 and a reasoning-model Step-Back or typing test.
