# Critique: C02.04 Soar other memories and RL (cross-check)

## Numbers re-checked against source text (arXiv PDFs opened this session)
1. Reflexion: ALFWorld +22% absolute in 12 iterations, +8% absolute from reflection over episodic-only (100 HotPotQA questions, ground-truth context), ReAct hallucination plateau 22%. Confirmed (a24, b11, c13, c14).
2. Reflexion Table 3 (HumanEval Rust, 50 hardest). Clarification: base model 0.60; test generation omitted 0.52; self-reflection omitted 0.60; full Reflexion 0.68. So omitting reflection equals the base rate. b12 is right; a24's "52 vs 60" alone is incomplete.
3. Generative Agents TrueSkill 29.89 / 26.88 / 25.64 / 22.95 / 21.21 and effect size 8.16. Confirmed (a23, b13, c15). Caveat: raters scored believability, not task success.
4. Mem0 LoCoMo overall J: Mem0 66.88, Mem0g 68.44, Zep 65.99, LangMem 58.10, OpenAI 52.90, A-Mem 48.38, full context 72.90 at 26,031 tokens (p95 17.1 s). Confirmed (b18, a26). Best plain RAG in the paper's sweep is 60.97.
5. Hu et al. overall: GPT-4o-mini 42.3, BM25 41.5, HippoRAG-v2 41.6, Mem0 21.1, Cognee 20.6, Zep 24.0, GPT-5-mini 60.6. Confirmed (b19).
6. LongMemEval: GPT-4o 0.870 vs 0.606 (30.3%), ChatGPT 0.5773, offline reading 0.9184, +9.4% recall, +5.4% accuracy, +11.3%. Confirmed (b14, b15). Minor: c20 says Coze GPT-3.5 0.2474 and b14 says Coze GPT-4o 0.3299; these are probably two table rows, not rechecked.
7. MemGPT deep memory retrieval 38.7 to 66.9, 32.1 to 92.5, 35.3 to 93.4. Confirmed (b17, c16).
8. NOT re-verified: Gorski and Laird Table 1 (a08, garbled text, do not cite), Derbinsky 2012 scaling numbers (a10, b05), STARS percentages (c08, c09; guessed arXiv id did not match), Memory-R1, ExpeL, Voyager, A-Mem figures.

## Contradictions between sources
- Mem0 paper (extracted memory close to full context at far lower cost) vs Hu et al. (Mem0 21.1 vs backbone 42.3). Different benchmarks and backbones, vendor vs independent authors. Treat vendor numbers as upper bounds.
- Xiong (deletion helps only with a strict evaluator) and Reflexion test omission (52% below base) both say memory value depends on verifier quality.
- a08 cannot be reconciled with anything else; its table was unparseable.

## Weak spots
- Soar primary evidence is old (2004-2013), toy domains (Eaters, TankSoar, Well World), mostly graph-only results, small n.
- Nason and Laird 2005 and the 2012 book were never opened (a17, a18, c05, c06, c26); RL claims rest on the manual and Laird 2022.
- No study compares Soar memories with LLM-agent memories; links are analogies (CoALA, Pink 2025 position paper, Wray 2025 table).
- Snippet-only: b25 (Derbinsky and Laird 2009), a19.
- Reflexion, Generative Agents and Voyager used GPT-4-era models; not retested on current models.

## GAPS
1. At equal tokens, does a distilled-lesson class record beat putting raw earlier solutions or the full history in context, on current models?
2. Does write-gating by a verifier prevent error propagation on our benchmarks, and what minimum verifier quality makes memory help rather than hurt?
3. Does cue design (state features plus proposed operator, recency bias, fact-key expansion) change the hit rate of the useful record, and by how much? Soar shows bias matters; no LLM measurement matches.
4. When the full history fits in context, is any retrieval store worth it (Mem0 paper vs Hu et al.)? Where is the length crossover?
5. Can Soar-RL-style operator preference learning be approximated in context from outcome counts, with no weight updates, and does it beat fixed operator order?
6. Does a short recent-history cue fix hidden-state failures in LLM agents as it does for ZigguSoar (b07)?
7. What do forgetting and deletion policies do beyond the few agents Xiong et al. tested?
8. What are the true numbers in Gorski and Laird Table 1 and Nason and Laird 2005 (primary PDFs needed)?
9. Do memory benefits persist for strong reasoning models with extended thinking, or do they make episodic notes redundant?

## Gap search results (evidence_d.jsonl, d01-d19)
Web search budget was exhausted, so sources were arXiv PDFs opened by direct fetch (ReasoningBank, ExpeL, Dynamic Cheatsheet, ACE, Krishnamurthy et al., AWM, RMM, RULER, Memory-R1, MemoryBank).

1. CLOSED (partly): distilled lessons vs raw history. ReasoningBank 48.8 vs raw-trajectory 42.1 vs none 40.5; Dynamic Cheatsheet shows full history can fall below no memory (GPT-4o 6.7 vs 20.0). Still open: no study is token-matched. New claims K18, K19.
2. CLOSED (partly): write gating. A 72.7%-accurate judge was enough in ReasoningBank; ACE says memory can degrade with no reliable signal; best signal is a programmatic check. Minimum accuracy below 70% not measured. K20.
3. CLOSED (partly): cue design. ExpeL 59.0 vs random 42.5; RMM 70.4 vs RAG 63.6 vs oracle 90.2. State plus proposed-operator cue still unmeasured. K21.
4. OPEN-ish: crossover. RULER gives effective lengths (GPT-4 64K), Dynamic Cheatsheet shows raw history hurts. No direct Mem0-vs-Hu reconciliation; no token-length crossover curve for agent memory.
5. PARTLY OPEN: Krishnamurthy et al. show externally computed outcome summaries are required; no test against fixed operator order. K22.
6. OPEN: no LLM study found on short recent-history cues for hidden-state failures.
7. OPEN: Memory-R1 and MemoryBank have no isolated deletion or forgetting ablation; Xiong remains the only deletion evidence.
8. OPEN: Gorski and Laird and Nason and Laird primary PDFs not reachable (404, 403, no search budget).
9. PARTLY CLOSED: ACE with GPT-5.1 gains 11.6; Dynamic Cheatsheet found R1/o1 gains minimal. No test with extended thinking on and off. K23, K24.
