# Critique: Dynamic memory, early CBR (C08.02)

## Corrections made (numbers re-checked against saved paper text in D:/research_scratch/C08.02)
Confirmed as written: Xiong RegAgent fixed 67.53 / add-all 55.48 / strict 70.95 / C1 63.18, EHRAgent 16.75 and 38.50; Memento K sweep (59.9/72.2, 63.6/77.9, 64.5/78.5, 64.1/78.2, 63.9/78.1), no-CBR 59.9/72.2, GAIA 87.88 and 79.40 with level splits; ReasoningBank WebArena no memory 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8, Shopping 39.0/40.6/44.4/49.7; Generative agents 29.89/26.88/25.64/22.95/21.21, chi2(4)=150.29, d=8.16; Mem0 full-context 72.90, Mem0g 68.44, Mem0 66.88, A-Mem 48.38; AWM 35.5 vs 23.5 (+12.0, +51.1% relative); CBR-RAG 0.8967 / 0.9141 / +1.94%, 2,084 cases, 32 test; Sourati 27.7% label overlap and +2.5-6 F1; Dynamic Cheatsheet AIME24 23.3 to 50.0; Evo-Memory r=0.717 / 0.563.

Corrections:
1. ExpeL ablation (a26 vs b20/c07): a26 said random sampled = 40.0 and left reasoning-similarity uncertain. The garbled table, read row by row, gives ReAct 40.0, reasoning-similarity 48.5, random 42.5, ExpeL 59.0. Use b20/c07. a26 is wrong on random.
2. c22 names the authors "Hua et al." The paper (arXiv 2402.17709) is by Yi Hu et al. a32 is right. Numbers: 30.2% leave-square-out vs 92% random split for Llama-2-7B base-9 addition (lk=20 square); c22's "441 held-out samples" is from the paper (about 10,000 samples total).
3. a21/b11 attribute Memento to "Wang et al." and c03 to "Zhou et al."; the arXiv paper is Zhou et al. Use Zhou. Similarly c09 "Zhao et al." for ReasoningBank vs a28 "Ouyang et al."; first author was not re-checked, treat as unresolved.
4. b29/a31: the "A-Mem lags by more than 25 J points" line is in the Mem0 paper text but refers to a category-level comparison; at overall level A-Mem 48.38 vs Mem0g 68.44 is 20 points. Claim scoped accordingly (K21).
5. c12 shows "26.1" for EHRAgent coarse; the paper has 26.19 (C1) / 25.91 in a second table. Minor, rounding.
6. a07 vs a09: number of Muskie stories in CyFr is about 30 (thesis) vs about 10 (Dec 1980 report). Different dates; both may be right.
7. a20: CYRUS date 1984 on a course slide vs 1980 thesis vs 1983 journal. Use 1980 (thesis) and 1983 (Cognitive Science 7).

## Contradictions between sources
- Insights vs retrieval: ExpeL says insights-only beats retrieval-only on HotpotQA (36 vs 31) but loses on ALFWorld (50 vs 55). So no universal winner.
- Failure storage: ReasoningBank gains from failures (+3.2 Shopping) but the same table shows AWM losing (44.4 to 42.2). Evo-Memory also shows degradation without filtering.
- A-Mem claims gains over MemGPT on LoCoMo; Mem0 re-run puts it far behind. Not resolved.
- Memory vs full context: Mem0 and MemoryAgentBench say long context wins when it fits; Dynamic Cheatsheet and Memento say distilled memory adds a lot. They differ in task (conversation recall vs recurring problem solving).

## Weak spots
- Early CBR (CYRUS, IPP, Dehn) has no quantitative evaluation anywhere; every "finding" is design description. Established status for K01 means agreement on that absence.
- Human-data foundations (Bower-Black-Turner 1979, Reiser et al. 1985, Williams & Hollan 1981) were NOT opened (a13, b09, b10). No numbers may be cited.
- Kolodner 1983 and Lebowitz 1983 journal papers were behind HTTP 403; only abstracts (b05, b06). Schank 1982 Dynamic Memory book not opened.
- Most LLM results are single-run, single-benchmark, often with no confidence intervals (ReasoningBank, AWM, Memento iterations). CBR-RAG test set is only 32 questions.
- Memento "CBR adds" figures mix tool use, planner-executor split and cases; only K23 isolates cases.
- Independence: ReasoningBank, AWM, Synapse comparisons share one benchmark (WebArena), so "independent sources" counts papers, not independent testbeds.

## Seen only in snippets or secondary
- Wikipedia (a19, b07, b08, c01, c02) and a course slide (a20): dates only.
- b09, b10: written from memory, flagged unverified.

## GAPS (most decision-relevant first)
1. At equal tokens and equal number of attempts, how much of case-memory gain remains over a best-of-N no-memory arm, for a strong frontier model on reasoning (not web/tool) tasks?
2. Does generalising two episodes into a norm (E-MOP rule) produce wrong lessons often enough to need the "revise or demote" step, and what is the measured wrong-lesson rate for LLM-written lessons?
3. What is the best index: situation features (CYRUS-style), task embedding, or reasoning trace, when tasks are diverse and not recurring? ExpeL only tests recurring benchmarks.
4. Which write gate (verifier success, LLM judge, human) keeps add-all degradation away at low cost, and how does a coarse judge compare with the strict oracle in Xiong et al.?
5. Does cue elaboration (infer missing index features before retrieval) raise hit rate for LLM agents? No LLM study tests Kolodner's elaboration strategies directly.
6. What do the primary human studies (Bower-Black-Turner 1979, Reiser et al. 1985, Williams & Hollan 1981, Schank 1982) actually report in numbers?
7. Is the retrieval size plateau near 3-4 cases robust across model strength and case length, or only an artefact of the Memento/DS-Agent setups?
8. Do the Lebowitz IPP follow-ups (UNIMEM, generalisation-based memory) give any measured accuracy figures that the 1983 papers lacked?
9. Can an independent replication confirm A-Mem and AWM gains outside their own benchmarks?
10. How should case memory behave for weak backbones, where it gave zero or negative gains (starchat, GPT-4o-mini)? Is a capability threshold measurable?

## Gap search results (2026-11-03)
Tool limits: arXiv API, Semantic Scholar, OpenAlex and arXiv search were all rate-limited, and the shared WebSearch budget ran out after one query. Evidence is in evidence_d.jsonl (d01-d19). Papers opened: ReasoningBank (2509.25140), Memp (2508.06433), UNIMEM (Lebowitz 1987), HyDE, EvolMem, FORGETEVAL.

- Gap 1 (memory vs best-of-N): PARTLY CLOSED. ReasoningBank Shopping, Gemini-2.5-flash, k=5: no-memory best-of-5 39.0 to 42.2; memory MaTTS 49.7 to 55.1 (d01, d02). Web task only; no frontier reasoning-task test. K07 moved to contested (Memento said gain shrinks with iterations; ReasoningBank says it persists). New claim K27.
- Gap 2 (wrong-lesson rate): STAYS OPEN. UNIMEM paper shows the mechanism (spurious two-instance generalisations, repaired by feature removal) but gives no rate (d12). New claim K30.
- Gap 3 (best index, non-recurring tasks): PARTLY CLOSED. Memp: LLM-extracted keywords 76.02 vs raw query 73.38 vs random 74.59 vs none 71.93 (GPT-4o) (d06). Still only recurring benchmarks; no reasoning-trace key. K29.
- Gap 4 (write gate): PARTLY CLOSED. ReasoningBank judge 72.7 percent accurate; success rate barely changes down to about 70 percent simulated accuracy (d03). Simulated flips only. K28. Memp update-policy numbers are only in plots (d09).
- Gap 5 (cue elaboration for agents): STAYS OPEN. Only indirect evidence (HyDE, +16.8 and +15.8 nDCG@10 over Contriever on DL19/20) (d14).
- Gap 6 (human primary studies): STAYS OPEN. Not accessible; no numbers (d18).
- Gap 7 (plateau): PARTLY CLOSED. Memp ALFWorld shows rise, plateau, decline (d08); optimum k not given numerically. K08 gets a second setup.
- Gap 8 (UNIMEM numbers): CLOSED (negative). Lebowitz 1987 has parameter sweeps (9-14 top-level generalisations, 3 x 100 universities) but no accuracy (d10, d11).
- Gap 9 (replications): STAYS OPEN. No AWM reproduction found. A-MEM third-party results: EvolMem 44.54 vs base 52.18; FORGETEVAL 56.9 to 70.6 percent (d15, d16, d17). K22 extended.
- Gap 10 (weak backbones): PARTLY CLOSED. Gemma-3-12B gains 17.1 to 24.1 with distilled memory, while raw-trajectory Synapse falls to 16.0 (d04). Threshold depends on memory form, not just model size. K15 extended.

Corrections: first author of ReasoningBank is Ouyang (d05); c09's "Zhao" is wrong.
