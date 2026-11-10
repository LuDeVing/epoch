# Critique: ACT-R declarative memory (cross-check)

## Numbers re-opened (this session, text extracted from source PDFs)
1. Anderson & Schooler 1991: Ebbinghaus fit log P = 3.862 - 0.126 log delay, R2 .978; practice 4.08 - 1.44 log days R2 .996 vs exponential R2 .949. CONFIRMED. Environment exponents .73 / .77 / .83 CONFIRMED.
2. Park et al. 2023: decay 0.995, min-max scaling, all alpha = 1 CONFIRMED (a19 had said "from memory"; now read). TrueSkill 29.89 / 26.88 / 25.64 / 22.95 / 21.21, d = 8.16, H(4) = 150.29 CONFIRMED.
3. MemoryBank Table 2: English ChatGLM .809/.438, BELLE .814/.479, ChatGPT .763/.716; Chinese .84/.418, .856/.603, .711/.655 CONFIRMED. Note: c03 gave English correctness only; Chinese correctness is .418/.603/.655. 194 questions and "exploratory and highly simplified" CONFIRMED.
4. Settles & Meeder 2016: MAE HLR .128, no-half-life .350, Leitner .235, Pimsleur .445, LR .211, constant .175; 12.9M instances; 3.3M students CONFIRMED. CORRECTION: AUC of Leitner (.542) is slightly higher than HLR (.538). The line in b23 saying AUC "near .51-.54" is right, but HLR does not win on AUC. Calibration, not ranking, is what improved.
5. Murre & Dros 2015: 31-day 0.041 (Ebbinghaus .211), power R2 .974 AIC -16.6, summed exponential AIC -24.5 CONFIRMED. NEW CAVEAT: the paper says a corrected savings measure gives 0.137 at 31 days, so the "no retention at 31 days" reading is partly a measure artefact.
6. Kerestecioglu 2026: S-tier raw RAG 78.4 [74.8, 82.0], aggressive consolidation 48.4 [44.0, 52.8], VSCode 97.2% / 58% / +21.8 pp CONFIRMED. CORRECTION to a25: the paper names deduplication, not importance decay, the dominant mechanism on VSCode. The +21.8 pp should not be credited to forgetting.
7. Hou 2024: t = -5.687, CI [-0.27, -0.12], threshold 0.86 CONFIRMED.
Not re-confirmed: SYNAPSE (F1 40.5, ablations), Pavlik & Anderson fit numbers, Rivera-Lares, Cohen-Dallal, Pirolli, FadeMem, OBLIVION, CAMeR. SYNAPSE could not be fetched (arXiv title search returned nothing), so K09 stays single-source and unverified by me. The local file named syn.txt is actually SynapticRAG, not SYNAPSE; do not trust the filename.

## Contradictions between sources
- Pavlik & Anderson (practice slows decay) vs Rivera-Lares 2022 and Cohen-Dallal 2018 (rate of forgetting independent of strength). Rivera-Lares has floor effects at 1 week in Exp 1 and about 20 per cell. Unresolved.
- Power vs exponential: Murre & Dros AIC favours summed exponentials slightly; Anderson-Schooler favours power. Averell & Heathcote 2011 and Murre & Chessa 2011 were never opened.
- Alqithami 2025 abstract (Hybrid best, .911) vs its Table 2 (Random Drop best, .635). The paper is internally inconsistent; excluded from claims.
- LLM-agent forgetting results disagree by benchmark: helps on VSCode (via dedup) and temporal LoCoMo, hurts on LongMemEval.

## Weak spots
- No LLM study isolates a recency, frequency or activation term against a plain cosine baseline at equal tokens. Park ablations are whole-module.
- Almost every LLM-memory paper is 2026 preprint, single benchmark, own ablation, LLM-judge scoring.
- Hou 2024 tasks are authors' own; ACT-R human fits are small N (20 per group, 5 per cell).
- Claims marked established are mostly "established that the gap exists", not "established that ACT-R scoring helps an LLM".

## Seen only in snippets or not opened
a07 (Anderson & Milson), a10 and a14 (secondhand), a26, a27/c22 (pensyve), b11-b13, b22, c14 (Honda 2025), c23, c24. No claim relies on them alone except K02 (contested, partly) and K21.

## GAPS
1. Does adding a use-count / base-level term to Park-style recency+importance+relevance raise retrieval accuracy at equal tokens on a task with repeated use over time?
2. Is the decay clock better as wall time, turns, or number of intervening memory events for an LLM agent (slowed-clock question)?
3. Does a power-law decay beat exponential at ranking (AUC/NDCG) in an agent memory, given that form is contested in human data?
4. Which benchmark can actually test use-history effects? LoCoMo and LongMemEval cannot. What minimal multi-session benchmark would?
5. Does activation-based ranking help on exceptions (one-off event on a habitual slot, Hou Task 0), or does frequency hurt?
6. Does SYNAPSE's node-decay and fan gain replicate on another backbone and a non-temporal-bias benchmark?
7. Does ranking by activation without deletion beat delete-on-decay at equal tokens (OBLIVION vs Kerestecioglu)?
8. Does practice-dependent decay (Pavlik-Anderson) survive the Slamecka-McElree replications, and is it needed for an agent at all?
9. Honda 2025 (ACT-R + cosine for agents): does it exist, and what did it measure?
10. How sensitive are results to d (0.3 to 0.7) and noise, given weak identifiability?

## Gap search results

Search was limited this session: Semantic Scholar, OpenAlex search and export.arxiv.org returned 429, and WebSearch had no budget left. Sources were reached by direct arXiv HTML, Crossref and single-record OpenAlex lookups. Evidence is in evidence_d.jsonl (d01-d15). New claims are K23-K30.

1. Use-count term on top of Park at equal tokens: OPEN. No paper isolates it. FadeMem has a frequency term but ablates modules only (d08). Rocchi 2026 (abstract only) warns that counting retrieval as use mostly credits passengers (d13, K27).
2. Best clock: OPEN. Five papers use five clocks and none compares (d15, K23).
3. Power vs exponential at ranking: OPEN. No LLM study; Averell & Heathcote 2011 abstract shows human data split by analysis (d10, K24).
4. Smallest benchmark: PARTLY CLOSED. CAMeR-Bench exists (76 memories, 100 rounds) but scores weights, not answers; MemoryAgentBench tests overwrite (d09, d11, K29). A design is sketched in K29.
5. Exceptions: PARTLY CLOSED. Hou Task 0 re-read: frequency picks the habit, recency picks the one-off, both wrong (d06, K25). One item only.
6. SYNAPSE: PARTLY CLOSED. Paper fetched and re-verified (40.5 vs Zep 39.7; ablations match). Holds on GPT-4o and Qwen-3b, same authors (d01, d02). New correction: its node decay is a per-step leak, not base-level decay, so K10 no longer supports ACT-R decay (d04). Other-benchmark test still open.
7. Rank vs delete: OPEN. OBLIVION has no decay on/off ablation; CAMeR shows time-only decay collapses (d07, d09, K26).
8. Pavlik-Anderson vs Slamecka-McElree: OPEN, not re-searched. The ACT-R site was unreachable. Practice-dependent decay is probably unnecessary for an agent, but that is inference.
9. Honda 2025: CLOSED on existence, OPEN on results. It is ACM HAI '25, DOI 10.1145/3765766.3765803; abstract only, no numbers, a simulation (d05).
10. Sensitivity to d and noise: PARTLY CLOSED. SYNAPSE delta sweep costs up to 2.4 avg F1; OBLIVION temperature table is non-monotone and contradicts its text (d03, d07, K28). No noise-parameter sweep found.

Weak spots of this pass: d05, d10, d12, d13, d14 are abstract-only (opened true for the abstract record, not full text). Nothing here changes the earlier verdict that no evidence yet shows ACT-R scoring helps an LLM agent.
