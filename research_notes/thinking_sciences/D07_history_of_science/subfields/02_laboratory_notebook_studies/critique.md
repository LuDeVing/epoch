# D07.02 Laboratory notebook studies: cross-check critique

## What was re-opened (full text in D:/research_scratch/D07.02)
Confirmed against the paper text: DiscoveryWorld (66% completion, 55% knowledge, 38%/18%/34% agent figures, Table 4 rows), DiscoveryBench (peak 25%, biology 0%, economics 25%, sociology 23%), ScienceAgentBench (32.4/34.3, 16.7/20.6, 42.2, OpenHands 21.6 vs 10.8 points), Huang et al. self-correction tables, Si et al. (4.84/5.64/5.81, N=49 ideas, 79 reviewers, 56.1 vs 53.3, 4000 to 200 non-duplicates), Beel et al. (42%, +8%, 57%), FIRE-Bench (46.7, 31.9 to 37.9, +6.1 F1), Safdar and Saadeldin (+21.41 = 79.5%, 69.67 to 96.59, 2/42 vs 16/21, 36% Phase 1), Geng et al. (17/20, 16/20, yoked design).

## Corrections made
1. b13 labels the DiscoveryWorld columns as completion/process/knowledge and says completion barely falls with difficulty. The paper's columns are Procedure/Completion/Knowledge (a07 is right). ReAct completion falls 0.38 to 0.18 and knowledge 0.25 to 0.10, so both fall. b13 should not be used.
2. c08 (DiscoveryBench domain knowledge): the paper sentence reads "jumps from 9.9% (w/ domain knowledge) to 17.5% (w/o domain knowledge)". "Jumps" and the order contradict. Direction cannot be settled from the text; no claim was built on it.
3. c11: the 57% (4 of 7) figure appears twice in Beel et al.: structural errors and incorrect or hallucinated numbers. Both are stated in claim K10.
4. c19/K14: the 20 failures per box were sampled from the observation-only condition only, not all conditions.
5. b20: "4000 seed ideas, 200 non-duplicate" is per topic in the paper, not overall.
6. Huang et al. (b21): the 75.8 to 38.1 CommonSenseQA drop is the round-1 result with 3 calls (table row labelling is confusing), not round 2; round 2 is 41.8.

## Contradictions between sources
- Agent Laboratory (a14) and AI Scientist reviewer: automated reviewers score higher than humans in one, match them in another (65% vs 66% balanced accuracy). These are different reviewer designs; no true conflict, but the AI-reviewer match is on a narrow task.
- Si et al.: AI ideas more novel, but diversity collapses (b19 vs b20). Both hold: novelty per idea is high, number of distinct ideas is low.
- NewtonBench (c16): code helps weak models, hurts strong ones. ScienceAgentBench (c09): execution feedback nearly doubles success. Different tasks (symbolic law vs code workflow); the net effect of tools depends on the task and on model strength.

## Weak spots
- The core of this subfield (Holmes on Krebs, Gruber on Darwin, Kulkarni and Simon KEKADA, Grasshoff and May, Tweney, Dunbar) was NOT opened. Rows a16-a27, b05-b11, c02, c03 are memory or snippets (opened:false). No founding-study number (number of notebook steps, count of surprises, KEKADA match rate) is verified. Dunbar's "about half unexpected" is unconfirmed memory.
- The LLM evidence is about discovery agents in general, not about reconstructing step order from a notebook. Nothing measures operator order against a human record.
- Several claims rest on a single paper (Safdar, Geng, NewtonBench, Auto-Discovery-Bench, FIRE-Bench). Safdar is a one-agent behavioural case study.
- Blog and practitioner sources (c04, c28) were seen only in snippets.
- Wikipedia pages are the only opened sources for the historiography.
- The Huang et al. results are on GPT-3.5/GPT-4 (2023-24), possibly weaker than current reasoning models.

## Seen only in snippets
c02, c03, c04, c28, c29, a05, and all memory-based rows.

## GAPS
1. What exactly did Holmes's reconstruction of Krebs's 1931-32 notebooks find about operator order (number of experiments, where the surprise came, how long before the cycle idea)? Read Holmes 1980 and Grasshoff and May 2003 and extract the step sequence.
2. What did Kulkarni and Simon KEKADA reproduce, and what fraction of Krebs steps matched? Are there failed or partial reproductions?
3. Does any 2020-2026 LLM study test a surprise-driven rule (focus on the unexpected result, explain before moving on) at equal tokens? Search specifically for KEKADA-style prompts.
4. Is there a replay-of-historical-notebook test (Kepler, Krebs, Faraday, Darwin) with a LLM that scores order against the record? One blog (Panchekha) exists; read it and look for papers.
5. Gruber on Darwin: what do the 1837-39 notebooks show about parallel streams and impasses, with quantified counts (notebook entries per topic, time between Malthus reading and selection)? Also failed or critical readings (Kohn, Schweber, Ospovat).
6. Dunbar 1997 and Dunbar and Fugelsang: exact rates of unexpected findings and how labs responded (method check first, then model change). Open and record numbers.
7. Does a structured hypothesis-before, outcome-after notebook measurably help an LLM agent at equal tokens? Look for ablations (not just proposals).
8. Do impasse rules (ban the same operator family after N rejections) beat greedy accept/reject loops? Safdar suggests greedy anchoring; find controlled tests.
9. How reliable are historian reconstructions? Any measured agreement between independent reconstructions of one notebook (Nickelsen and Grasshoff 2009 on error)?
10. Newer reasoning models (2025-26): does the Huang et al. result that intrinsic self-correction does not help still hold, with numbers?

## Gap search results (2026-11-01)
Tools: WebSearch quota was exhausted; OpenAlex and arXiv search were rate limited; Semantic Scholar worked slowly. Founding studies were mostly paywalled. Evidence is in evidence_d.jsonl (d01-d16); claims K21-K28 added, K01, K03, K08, K16, K20 revised.

1. Holmes on Krebs, step order: PARTLY CLOSED. Full text of Kulkarni and Simon (CMU copy) was read; it paraphrases Holmes with dates (surprise 15 Nov 1931, about 3.5 months in; scope check to mid Jan; ammonia source by 23 Jan; catalyst; 13 Apr 24.5 urea per ornithine; citrulline 25 Apr). Holmes 1980 and Grasshoff and May 2003 were not readable; no experiment count.
2. KEKADA match: CLOSED as "no number exists". Three scenarios, about 10 user-decided steps, no fraction matched, no independent replication found. Authors list divergences from history.
3. LLM test of a surprise rule at equal tokens: PARTLY CLOSED. AutoDiscovery uses Bayesian surprise as search reward at equal evaluation budget (5-29% more surprising findings). No test of "explain the surprise before moving on" at equal tokens found.
4. Replay of a historical notebook with scoring: OPEN. Only the Panchekha blog (n=1, no scoring) was read.
5. Gruber on Darwin counts and critics: OPEN. Only a secondary timeline (about 14 months from notebook B to Malthus, 28 Sep 1838). Kohn, Schweber, Ospovat not reached.
6. Dunbar rates: OPEN. Text not obtained; the "about half unexpected" figure stays memory only.
7. Hypothesis-before, outcome-after notebook ablation: PARTLY CLOSED. Reflexion ablations (explanation step carries the gain, needs external tests); AIDE memory ablation shows no gain. Neither is equal tokens or a structured pre-registration notebook.
8. Impasse rule vs greedy: PARTLY CLOSED. AutoDiscovery (greedy loses efficiency with GPT-4o, ties with o4-mini) and MLE-bench (policy changes marginal, operators matter). No test of "ban an operator family after N rejections".
9. Reliability of reconstructions: OPEN. No inter-rater statistic found.
10. Huang et al. on newer models: PARTLY CLOSED. Tsui 2026 (reasoning models show small or negative blind spot; Wait lifts base models near reasoning models). No exact replication of Huang's protocol located.
