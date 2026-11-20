# Critique: Analogy and precedent in legal theory (E11.07)

## Numbers re-opened this session (all from full PDF text)
1. Spamann and Klohn (2016): 87% (13/15) vs 41% (7/17) affirmance, Boschloo p<.01; precedent cells 9/14 vs 11/18, 20/32 total; Bayes factor 8.7 for defendant vs precedent. Confirmed (b01, b02).
2. Liu, Klohn, Spamann (China): 86% and 82% vs 40%; p = 0.020, 0.015, 0.039; precedent 13% of time (2.93 min) vs statute 4% (0.81 min); 68% read precedent first; 29% cited it. Confirmed (b04, b05).
3. Zhang et al. 2026 (2510.08710): Task 1 100%, Task 2 64.82-92.09%, Task 3 11.46-33.99%, Qwen3 78.66% vs 30.04%, gpt-5 4,456 vs 3,081 tokens (+45%). Confirmed (a15, a17, b13, b14, c01-c03).
4. Webb et al. 2023: digit matrices OR 1.88 p=0.005; letter strings OR 1.76 p=6.3e-5; story analogies OR 0.37 p=0.0003 (15 of 54 students picked the analogous story on every trial). Confirmed. Correction: the p=6.3e-5 is the overall effect. The zero-generalisation effect has the same OR 1.76 but p=0.0007 (a22).
5. Lewis and Mitchell 2024: alternate-rule errors 38.59% GPT-3.5, 22% GPT-4, 5.81% GPT-3; 46 humans vs 57 in Webb. Confirmed (a23).
6. Zhang, Savelka, Ashley 2025 (2510.20941): 73.31% (173/236), 71.19% (168/236), GPT-5 75.42% verification, Gemini-Pro 42.37% with 131 unknowns, reversed control 97.46-100%. Confirmed (b15, c08, c09).
7. Zhang, Gray et al. 2025 (2506.00694): text confirms GPT-4o abstention 86.67%, Qwen-QWQ-32B 56.67%, Maverick 50.00%, Llama-3-8B, Scout, 4o-mini 0.00%; GPT-4o hallucination accuracy 99.64%. The values 3.33% (Llama-3-70B) and 23.33% (DeepSeek-R1-Distill) rest on a garbled table: the text extraction puts values one row off from labels. Treat these two as probable, not confirmed (c07).
8. Fan et al. 2025 (2505.14104): LoRA Llama-3.2-3B 19.21 to 70.96; Ministral-8B 73.18; Claude-3.7-Sonnet 66.67 and the 71.81 to 80.95 precision change are consistent with the table once the one-row label offset is applied. Row attribution is inferred, not read cleanly (c10, c11).
9. Zhang et al. token table: the same one-row label offset exists in the Zhang 2026 table (rows for gpt-5 and qwen3 appear swapped). The prose gives the right pairing: gpt-5 3,189 tokens at 92.09%, qwen3-thinking 9,596 tokens (3.0x) at 78.66%. a17 mixes the two: "487 to 3,189 to 7,025" are gpt-5 per task, not the non-thinking model. Correction applied in claim K05 (a17, c03).
10. Not re-opened: Blass and Forbus table, Demir and Canbaz, Zheng, CourtReasoner, Huang, Chen and Zhang. Their numbers rest on the first agents' reading (marked opened:true there).

## Contradictions between sources
- Spamann and Klohn (precedent null, US) vs Liu et al. (precedent effect, China). Different precedent strength (weak vs strongly favourable), different judges, N=32 vs 48; the authors themselves say a weak precedent is easy to dismiss (b25). No clean contradiction, but no common effect size either.
- Webb (emergent analogy) vs Lewis and Mitchell and Hodel and West. Same task, different stimuli; the dispute is about contamination and counterfactual tests, not data errors.
- Realist reading (outcome-driven similarity; Braman and Nelson, Spamann) vs Spellman and Schauer (knowledge and framing). Not tested head to head.
- Flat vs hierarchical result model (Prakken and van Woerkom vs Bench-Capon and Atkinson): formal dispute without empirical test.

## Weak spots
- Most LLM legal results come from one research group (Ashley, Savelka, Zhang) and from one benchmark family, so "independent_sources" is often 1. Only three claims (likeness relative to rule, retrieval needs reasoning, relation-between-cases weakness) rest on two or more independent groups.
- Zhang 2026 has 253 items per task and a temperature of 0.3 with one run; no confidence intervals. Task 3 may be partly a test of the CATO hierarchy convention, not of general analogy.
- Founding human studies are small (N=32, N=48, 19 informative cells). Spamann-Klohn's own p<0.11 on the key comparison.
- None of the AI studies compare a scaffold against plain prompting at equal tokens, which is our G7 test. Thinking vs non-thinking is the only close comparison, and it is not token matched.
- Chinese-law datasets (Fan) may not transfer to common-law precedent.

## Seen only in snippets or not opened
Levi (1949) book, Sunstein (1993) full text, Horty (2011), Rissland and Ashley, Aleven (abstract only), Marchant et al. (search summary only), Alexander (1996), Ashley (1990), Aleven and Ashley (1994). Their claims are tagged single-source or rely on secondary sources. Chen and Li (2018) had no sample sizes on the page opened.

## GAPS
1. Does an explicit "name the rule the analogue stands for, then check it on the target" step beat plain analogue retrieval at equal tokens on a non-legal task with exact labels (Levi's three steps as an operator)?
2. Can code-side hierarchy lookup (CATO-style relevance) close the Task 3 gap (11-34%) that model-side reasoning leaves, and at what token cost?
3. What do models do on "no valid analogue" cases when allowed a typed fallback instead of forced abstention (conflict with G6)? Is 0-87% abstention variance stable across prompts?
4. Is there any replication of Spamann and Klohn with LLMs as the judges: do they follow irrelevant sympathy cues over a weak precedent, and does blind outcome-hidden selection fix it?
5. What is the effect size and sample of Braman and Nelson (2007)? Do outcome-hidden analogue selections change which case is picked in LLMs?
6. Independent replication of Zhang et al. 2026 and of the SILVER rule-induction gain by a different group and on common-law data.
7. Do case-based memories (retrieved solved items) help LLMs more than written rules in non-legal reasoning, as Chen and Zhang (2025) report for moderation? Any equal-token comparison?
8. Is the era effect (older precedents recalled worse) a general memory-recency bias that would also hit our lesson memory (S9)?
9. What do Sunstein (1993) and Levi (1949) full texts add to the features of analogy beyond the secondary readings used here (needs a full-text pass)?
10. Do reasoning-trained models handle analogy under counterfactual stimuli (Lewis and Mitchell design) in 2025-2026, i.e. after the 2024 GPT-4 era?

## Gap search results
Budget note: the arXiv, Semantic Scholar and OpenAlex APIs all returned 429 or a daily-budget error, and the web search budget ran out after two searches. Gaps were worked from direct page fetches. Evidence is in evidence_d.jsonl (d01-d17); pages read through a summariser, not PDFs.

1. Rule-naming step vs plain retrieval at equal tokens: STILL OPEN. Closest are analogical prompting (d10, d11: +1 to 3 points on math, +4 on Codeforces Acc@1, no rule-naming arm, no token match) and rule-following (d12, fine-tuning). Added K24, K25.
2. Code-side hierarchy lookup for Task 3: OPEN. Zhang 2026 does not test it (d13).
3. Typed fallback and abstention stability: OPEN. The two garbled values are now confirmed (Llama-3-70B 3.33%, R1-Distill 23.33%, d14). One prompt, N=30; no prompt variants in either paper (d14, d15). Added K27.
4. LLM judges in Spamann-Klohn style: PARTLY CLOSED. GPT-4o follows precedent, ignores sympathy (d01); press reports over 90% vs students 85% and judges swayed 65% (d02); newer models 100% vs judges 52% on choice of law (d03). Whether blind outcome-hidden selection helps is untested. Two 2026 items (Katz and Zamir, a SAGE rerun) could not be opened (d16, d17). Added K23.
5. Braman and Nelson effect size: OPEN on numbers. Abstract confirms two experiments, bias strongest at moderate similarity, no training effect (d05). No N or effect size obtained (book chapter 403). No LLM test found.
6. Independent replication of Zhang 2026 and SILVER: OPEN. Nothing found by another group.
7. Case memory vs written rules, equal tokens: PARTLY. Hu et al. (d12) favour explicit rules out of distribution; Yasunaga (d10) favours self-made examples. Different methods, no equal-token comparison, Chen and Zhang not re-checked. OPEN.
8. Era effect as general recency bias: OPEN. Neither Zhang paper dates its cases or breaks results by age (d13, d14); K12 stays single-source.
9. Sunstein and Levi full texts: OPEN. Only Schauer's abstract was read (d06); it does not summarise Sunstein.
10. Reasoning models on counterfactual analogy: OPEN. Lewis and Mitchell tested only GPT-3 to GPT-4 and no reasoning models (d07). No 2025-2026 follow-up found.
Correction: d15 (Zhang, Savelka, Ashley) notes GPT-5 Task 2 is 75.42% (178/236); critique item 6 listed 73.31% (173/236) for a different cell, so check that cell before reuse.
