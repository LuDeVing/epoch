# F02.01 Distributed cognition theory: cross-check critique

## Sources re-opened this session (full text)
PAL (arXiv 2211.10435), Huang et al. (2310.01798), Cemri et al. (2503.13657), Kim et al. (2512.08296), Nye et al. (2112.00114), Du et al. (2305.14325), Kosmyna et al. (2506.08872), Hesselmann and Gollo 2020 (PMC7651475). Vallee-Tourangeau 2016 page was fetched but the results text could not be parsed, so its digits are not re-confirmed.

## Corrections and confirmations
1. PAL GSM8K: direct 19.7, CoT (Codex) 65.6, PAL 72.0, model-simulated runtime 23.2. Confirmed (Table 6).
2. PAL ablation text says 23.2 is "only 4.5 points higher than DIRECT", but 23.2 - 19.7 = 3.5. Paper's own inconsistency, confirmed. Use 3.5.
3. PAL GSM-HARD: the paper's text says direct 5.0, CoT 20.1, PAL 61.5; Table 1 (garbled in extraction) shows 23.1 and 61.2 for other rows (PaLM-540B CoT, PAL). Evidence lines a26 (20.1, 61.5) and b22/c01 (23.1, 61.2) are both from the paper but from different spots. Corrected claim: CoT about 20-23, PAL about 61. Also b22 labels 65.6 as CoT PaLM; the table and text make 65.6 the Codex CoT and 56.9 the PaLM-540B CoT (c01 is right on 56.9).
4. Huang et al.: Table 3 confirmed (GPT-3.5 75.9/75.1/74.7; CSQA 75.8/38.1/41.8; GPT-4 GSM8K 95.5/91.5/89.0). Oracle (Table 2) confirmed (95.5 -> 97.5; 82.0 -> 85.5; 49.0 -> 59.0). Table 7 has 76.7 at 1 response and 88.2 at 9 responses.
5. Cemri et al.: kappa 0.88, 150 traces, 41% to 86.7%, +9.4%, +15.6%, 11.8 / 15.7 / 12.4 / 13.2 / 6.2 / 8.2 / 9.1 percent, 94% LLM-annotator accuracy, group shares 41.8 / 36.9 / 21.3: all confirmed.
6. Kim et al.: 260 configurations, R2cv 0.373 / 0.413, 87%, beta -0.236 (p=.004), -0.096, SWE-bench figures, finance 0.631 vs 0.349, error amplification 17.2 independent vs 4.4 centralized (decentralized 7.8, hybrid 5.1): confirmed. New caveat: the paper reports the error-amplification main effect as non-significant (beta 0.014, p=.658) after controls, so "errors amplify" is descriptive, not a tested driver. a-b lines also call the 87% "best architecture predicted for held-out configurations"; the paper says held-out task domains, a restricted sense.
7. Nye et al.: 8.8 / 31.8 vs 20.1 / 50.7; 11 / 20 vs 26.5* / 41.5. Confirmed; the asterisk (relaxed scoring for few-shot) is real.
8. Du et al.: Table values confirmed with standard errors (67.0+-4.7, 72.1+-4.5, 81.8+-2.3; 77.0, 75.0, 85.0; chess 91.4, 102.1, 122.9; MMLU reflection 57.7). Evidence c10 says majority 69.0 and 81.0 for GSM8K: not re-checked.
9. Kosmyna: 15/18 vs 2/18 vs 2/18, p<.001, N=54, 18 in session 4. Confirmed. The 83.3% is the share failing to quote.
10. Hesselmann and Gollo: BF01 5.07 at N=89 analysed of 117 tested; RT 825 vs 821 ms; original N=46, Camerer N=104 (+130). Confirmed. Note a25 and b05 both cite Camerer 62% from the abstract or from memory; b05 is not opened. Camerer itself was not re-opened here.

## Contradictions between sources
- The "debate helps" headline (Du, c10/c11) vs "debate gain disappears at equal responses" (Huang c09, Smit b09/b10, Wang b11). Du used about 100-problem evaluation sets and the same model for every agent. The later papers are cost-matched, so they are better for our equal-token rule, but they used GPT-3.5/4-era models.
- Reflexion (c12) shows large gains with model-written tests, while Huang (c07) shows self-correction fails without an external signal. Compatible: Reflexion's gain relies on execution feedback, i.e. an external check.
- Kim (b15-b18) says multi-agent hurts on sequential tasks and saturated tasks; Li (b24) says more agents help on most tasks. Compatible if voting over independent samples is separated from interacting agents; not tested head to head.

## Weak spots
- No source tests the distributed-cognition theory itself on an LLM agent. c21 and c22 found no citation of Hutchins in the AI papers. Every AI claim here is analogy.
- Founding human studies (Hutchins 1995; Hollan et al. 2000) give no effect sizes. Tetris (a10-a12) has no extracted N or means. Zhang and Norman 1994 (a21) was not read at all.
- Many AI figures are from 2022-2024 models (Codex, GPT-3.5, GPT-4); transfer to current models is unknown, especially for self-correction (b21 survey suggests the answer depends on feedback quality).
- a32 (Cognitive Workspace) is very weak: GPT-3.5, 8 documents, d of 23-196. Do not use.
- Kim's regression explains under half the variance (R2cv 0.37) on correlational data.
- Cemri's labels are mostly LLM-annotated (94% agreement with experts on a subset).

## Only seen in snippets or not opened
a21 Zhang and Norman 1994; b05 Camerer (figures from memory, though matching the abstract); b06 Woolley 2010; b07 Riedl 2021; b08 Ren and Argote 2011; b11 Wang 2024 table values; b23 and Du numbers beyond Table 1; a24 Chuderski 2021; b25 Riedl 2026 table columns; a22 digits after parsing garble.

## GAPS
1. Does a real interpreter or unit test beat a model-simulated check at equal tokens on current models (2025-2026), on tasks other than grade-school math? PAL ablation is one benchmark and Codex-era.
2. Does intrinsic self-correction still fail on current reasoning models, and does a cheap cross-check (second sample, program) restore the gain? Huang is 2023-era.
3. At equal tokens, what is the break-even between self-consistency, debate and a single long chain for current models, per task type (sequential vs decomposable)?
4. Is Kim's 45% single-agent threshold stable under a token-matched design that does not penalise multi-agent, and does it hold on tasks outside the six benchmarks?
5. Which external-memory design (scratchpad, notes file, retrieval, paging) gives gain on long tasks, with an independent benchmark rather than the authors' own (MemGPT, Voyager are authors' own)?
6. Do the original human numbers hold? Open Zhang and Norman 1994 (representational effects, e.g. Tower of Hanoi isomorphs), Kirsh and Maglio 1994 (subjects, means) and the Vallee-Tourangeau results; any independent replications of interactivity effects?
7. Is verbalised reasoning (scratch notes) faithful enough to serve as an external trace we can audit, on current models? Turpin 2023 is older; look for 2025 faithfulness studies.
8. Which failure modes in Cemri's taxonomy (termination, verification) are cured by a fixed non-LLM harness rather than by more agents, and by how much?
9. Is there any paper that tests distributed-cognition or extended-mind predictions directly on LLM agents (for instance coupling, offloading threshold)? Searches found none; a dedicated search is still needed.

## Gap search results (evidence_d.jsonl, d01-d16; claims K22-K30 added)
Tool limits this round: WebSearch budget spent after one query, arXiv API and arXiv search pages returned 429, Semantic Scholar 429, OpenAlex daily budget used. Sources were opened by direct page fetch. Many are abstract-level only (marked in limits).

1. Real interpreter vs model-simulated check, current models: PARTLY CLOSED. ToRL (AIME24, 7B: 10.0 no tool, 26.7 TIR, 43.3 ToRL) and Chain of Code (BBH 84 vs CoT 72; Python-only fails non-algorithmic tasks) support real execution plus a model fallback. Still OPEN: no equal-token real-vs-simulated ablation on 2025 models.
2. Intrinsic self-correction on reasoning models: PARTLY CLOSED. Self-Correction Bench: 64.5% blind spot in 14 non-reasoning models, about zero in reasoning-trained ones, "Wait" cuts it 89.3%. But it tests detection of an injected error, not free-running self-repair. A cheap second-sample or program check restoring the gain was not measured here: OPEN.
3. Break-even self-consistency vs debate vs long chain: PARTLY CLOSED. Tran and Kiela 2026 (equal thinking tokens): single 0.418 vs debate 0.388 at 1000 tokens; parallel-vs-extended thinking paper reports up to 20% for parallel (abstract only). Per-task-type break-even table: OPEN.
4. Kim's 45% threshold: Kim is already token-matched (mean 4,800 tokens), so the worry that it penalises multi-agent unfairly is not supported. Stability outside the six benchmarks is NOT tested (94% match in-sample, CI about 20 points per cell): OPEN. Tran and Kiela on FRAMES and MuSiQue point the same way (single agent better).
5. External memory with independent benchmark: CLOSED for direction. MemoryAgentBench: long context 48.8-60.6 beats MemGPT 28.3, Mem0 21.1; RAG wins only exact retrieval. Second half of the paper not read.
6. Human numbers: PARTLY CLOSED. Kirsh and Maglio re-read: small descriptive data (mental rotation pilot with 3 subjects), no independent replication found. Magen 2025 supports the offloading cost (N=40, d=2.28). Zhang and Norman 1994 could not be opened (403, archive host unreachable): OPEN. Vallee-Tourangeau results: OPEN.
7. Faithfulness of traces on current models: CLOSED. Chen 2025: 25% (Claude 3.7) and 39% (R1); reward hacks verbalised under 2% in 5 of 6 environments. Treat traces as non-authoritative.
8. Cemri failure modes cured by a fixed harness: OPEN. No new source; only indirect support (Kim: budget fragmentation).
9. Direct tests of distributed-cognition predictions on LLM agents: OPEN (search not possible this round; absence weakly supported).
