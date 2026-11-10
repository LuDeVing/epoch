# Critique: E08.07 Training and tutors (cross-check)

## Re-opened this session (full text)
Sherlock 2 report (ERIC ED382817), Memento (arXiv 2508.16153), ReasoningBank (2509.25140), ExpeL (2308.10144), AWM (2409.07429), Tutor CoPilot (2410.03017), CBR-RAG (2404.04302).
Could not re-open (rate limits): Cloud-OpsBench, Ma 2014, Bastani 2025, Goh 2024, Kestin 2025. Their numbers stay as the agents recorded them.

## Confirmed
- Sherlock Table 7: VTT3 59/95/85, VTT4 58/91/86, NIT 75/87/86 (control/tutored/masters; N 23/18/13). t = -4.04, -3.72, -2.77. Frankenstation t=-2.93, p=.006. Fault solved in time 63.6/70.6/83.3%.
- Memento: GAIA 87.88 val / 79.40 test; DeepResearcher 66.6 F1 / 80.4 PM; without CBR 59.9/72.2; K sweep (K=4: 64.5/78.5).
- ReasoningBank WebArena table: Flash none 40.5, Synapse 42.1, AWM 44.1, RB 48.8, MaTTS 51.8; Pro 46.7/53.9/56.3; parallel 49.7 to 55.1.
- AWM: 35.5 vs 23.5, +12.0 points, +51.1% relative.
- Tutor CoPilot: +4 points mastery (p<.01), +9 for lower-rated tutors, about $20 per tutor.
- CBR-RAG: 0.8967 no-RAG vs 0.9141 hybrid AnglEBERT k=3, 32 test cases.

## Corrections
1. c18 (ExpeL ablation labels) is wrong. The paper's Table 3 rows are ReAct 40.0, reasoning-similarity 48.5, random 42.5, ExpeL 59.0. b16 has it right. c18 listed "random 40.0, reasoning similarity 42.5, task similarity 59.0".
2. a02/Sherlock effect sizes (1.27, 1.17, .96 SD) do not follow from the table: (95-59)/37 = 0.97, (91-58)/37 = 0.89, (82-55)/31 = 0.87. The NIT value .87 does match (12/14). The big VTT effect sizes use some other SD. Use "about 1 SD", and say the control SD of 37 against a tutored SD of 5 is the real story: the tutor removed the weak tail.
3. a20/b19 "out-of-distribution gains 4.7 to 9.6": from Table in Memento, F1 gains are MuSiQue +5.0, Bamboogle +8.7, PopQA +6.1; PM gains +9.5, +9.6, +8.6. The quoted 4.7 low end did not appear; treat range as about +5 to +10.
4. a24: the Flash "RB 46.5 to 49.7" pairing mixes a Pro-table cell (46.5 is Pro Synapse in the shopping column). Direction (failures help RB) is consistent with 49.7 in the main table, but the baseline 46.5 is unverified.
5. a01 lists masters VTT3 as 85, which matches Table 7. The OCR gives VTT4 masters 86.

## Contradictions and tensions
- Human case-library results (Tawfik) say forced retrieval/reuse prompts can hurt; Memento and ExpeL show retrieval helps agents. Different populations and tasks; not a true conflict, but we cannot assume prompting a model to "use cases" is safe.
- Cloud-OpsBench case reuse hurts on TrainTicket and for some models, while OM-RAG and RCACopilot show big gains. Likely cause: retrieval quality and system complexity. No paper tests this directly.
- Bastani (AI tutor hurts) versus Kestin (AI tutor helps): the difference is guardrails and design, not the model.
- ReasoningBank says AWM loses with failure cases; AWM paper is only about successful workflows. Not a contradiction, but baselines in one paper are re-implemented, so their AWM number differs from the AWM paper's own.

## Weak spots
- Almost all agent-side memory numbers are from one paper each, on different benchmarks, by the groups that built the method. No third-party replication of Memento, ReasoningBank, or AWM was found.
- None of the LLM studies compare memory against the same extra tokens spent on plain sampling, except ReasoningBank's MaTTS (memory-free scaling is flat there).
- Sherlock: one field test, 3 bases, small N; the VTT is a scored verbal protocol, rated by the study team; no delayed test beyond Parker's six-month check (c01, snippet-level).
- Human case-library literature (Jonassen, Tawfik) was read at abstract level only for most entries (a14, a16, a18, b04, b05, b08, b09 have no numbers).
- Tutor/RCT studies (Kestin, Bastani, Tutor CoPilot) are about teaching humans; they say little about an agent using a case library.

## Seen only in snippets or not opened
b27 (gap note), c03 (scanned PDF), c27 (press release), c26 (scores not extracted). a11 and a12 are Wikipedia.

## GAPS
1. Does a case library help at equal tokens against the same tokens spent on self-consistency or longer reasoning, for fault diagnosis specifically (not web or QA)?
2. What is the rate of harm when the nearest case is wrong (negative transfer), and does an abstain-on-poor-match rule remove it? Cloud-OpsBench hints at it but does not test it.
3. Is there any third-party replication of Memento, ReasoningBank, AWM or ExpeL numbers on a diagnosis benchmark?
4. Which case indexing (symptom, cause, device family, strategy) works best, and does indexing by strategy transfer better than by surface similarity?
5. Do failed cases with a diagnosis line help more than success cases in troubleshooting, as in ReasoningBank, and what is the effect of wrong or noisy stored cases?
6. How big is the effect of the "strategic knowledge" hint (Hydrive) on a language model, and does a case library add anything once the strategy is stated in the prompt?
7. How many cases and what mix of novel versus familiar faults are needed before gains appear (the human Sherlock set was 34 problems)?
8. What do the Jonassen and Hernandez-Serrano case-library papers actually report in numbers, and were they replicated by anyone other than Tawfik's group?
9. How does a case bank interact with a fixed scaffold (guardrails and states) rather than a bare agent: additive, redundant, or conflicting?

## Gap search results (evidence_d.jsonl, d01-d18; claims K27-K38 added)

Limits of this pass: WebSearch budget was exhausted; arXiv, OpenAlex and Semantic Scholar APIs returned 429. Sources were found through ERIC, CrossRef and the Hugging Face paper index, then read as arXiv HTML through a summarising fetch (first 100k characters only). Numbers are as the summariser extracted them.

1. Equal tokens, case library vs self-consistency, diagnosis: OPEN. No study found. Indirect: memory methods cost up to 3.6x tokens and often lose to a stronger base model (d08); Cloud-OpsBench gives no token cost for ICL (d02). Self-consistency in RCA was recommended but not measured (d15).
2. Harm from wrong nearest case: PARTLY CLOSED for general agents. Conflicting memory costs 10 to 26 points and is followed about two thirds of the time (d03); wrong lesson 40 vs 55 percent success when removed (d06); Cloud-OpsBench TrainTicket ICL fell (d02). Abstain rule: only a fine-tuning analogue (harmful reuse 100 to 25 percent, d04); relevance gating gave no gain in d03. Not tested on diagnosis. OPEN for diagnosis.
3. Third-party replication: PARTLY CLOSED. EvoMemBench (AWM, ReasoningBank, AgentKB) and the EDV paper (ReasoningBank, +2.6 on tau2) are independent and show smaller or uneven gains (d06, d08). Evo-Memory is from Google, not independent. No replication of Memento or ExpeL, and none on a diagnosis benchmark. OPEN for diagnosis.
4. Indexing: PARTLY. Insight-level beats raw for harder targets (d13); shape similarity is a weak proxy in fault retrieval (d14); explanation and difference indexing prompts help humans (d12). No head-to-head of symptom vs cause vs strategy indexing. OPEN.
5. Failed cases and noisy cases: CLOSED enough for the agent. Distilled failures help (+3.2) and raw ones hurt (-2.2) (d17); add-all noisy memory loses 5 to 12 points and strict admission wins (d01); wrong lessons cost 15 to 25 points (d06). The a24 baseline worry is resolved: 46.5 is the success-only value. Not tested on troubleshooting.
6. Hydrive strategic-hint effect on an LLM, and whether a bank adds beyond it: OPEN. No LLM study found.
7. How many cases and what mix: PARTLY. Gain rises with similarity (r 0.56 to 0.72) and with episodes under raw retrieval (d07, d05); K saturates at 4 (K09). No threshold for a diagnosis bank. OPEN.
8. Jonassen and Hernandez-Serrano numbers: PARTLY CLOSED. The 2003 paper reports a win on multiple-choice process questions only and no short-answer difference; no N or effect size obtained (abstract only) (d10). Replications: only the Tawfik lab (N=22 to 91) and Park 2020 (N=105, indexing prompts) (d11, d12), from ERIC records, not full text. No outside replication on fault diagnosis.
9. Bank with a fixed scaffold: OPEN, with one hint. Planner x memory was super-additive on SWE-bench Verified (d16, p=0.011), and plain agent structure is not reliably additive (d15). Nothing tests guardrails and states plus a case bank.

Design hints that follow: gate admission with a verifier (K27, K28), consult the bank after the first failed hypothesis (K38), store abstract cause and difference notes (K33, K34), and treat published gains as upper bounds (K31).
