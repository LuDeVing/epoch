# A06.03 Interference: cross-check critique

## Sources re-opened this session (numbers checked)
Wang & Sun 2025 (PI-LLM), Chattaraj & Raj 2026, SleepGate 2026, Xiong et al. 2025, Ding et al. 2026 (CMI), MINTEval 2026, Kerestecioglu et al. 2026, Shahrabi-Farahani & Rahmati 2026 (abstract), Arjmandi 2026 (abstract), Baeuml & Kliegl 2013.

## Confirmed
- Wang & Sun: size-class t=3.03, p=0.005; context length t=-0.144, p=0.886; R2=0.261; N=30. At 400 updates the M tier drops to 0% (one exception), L stays relatively high. Value length 10 words under 40%, 40 words under 5%. Per-key forget prompt under 10 points.
- Chattaraj & Raj: 93.9/96.0/72.9/45.5/24.6% RI at N=3/50/100/200/300; gap 69.5, t(38)=10.71, d=1.73; R2=0.491; reasoning 178.0 vs 150.3, d=1.76; error shares.
- SleepGate table, Xiong table (RegAgent 67.53/55.48/70.95, EHR 13.05/38.50, CIC 59.90/85.40), CMI (0.84/0.92 baselines; -0.34, -0.50), Kerestecioglu (70.1 vs 71.2; 78.4 vs 48.4; thresholds 0.542, 0.559), Baeuml & Kliegl (14.58%, t(23)=4.263, d=1.342; 11.27%, t(23)=3.491).

## Corrections
1. Wang & Sun Spearman: the paper writes rho squared = 0.673 (p=0.0016), not rho=0.673. Evidence a03 had it right; b02, c03 dropped the square. Also the text says the 128k-131k set is "two-thirds of non-CoT models"; N=19 is not stated in the text I read.
2. MINTEval: average accuracy is 27.7% in Section 3.2 but 27.9% in another passage of the same paper. Internal inconsistency; use "about 28%".
3. CMI: Dense same-slot conflict stability goes 0.92 to 0.54 (c16 truncated this). Paired contrasts against unrelated at count 8: -0.32 [-0.46,-0.20] and -0.48 [-0.62,-0.34].
4. Dense retrieval repeated-history plasticity is -0.46 (not smaller than same-slot -0.44), so "same-slot is worse" holds for lexical retrieval only.
5. Kerestecioglu: the garbled M-tier lower-budget figures (65.6/49.2/38.8) were not re-checked and stay uncertain.

## Contradictions between sources
- Scale and interference: Wang & Sun (R2=0.26, size matters) vs Chattaraj & Raj (RI R2=0.49 but PI R2=0.06 ns). They use different metrics (IES vs RIES/PIES), model sets (30 open vs 39 mixed), and Chattaraj includes closed models. Not a clean contradiction, but PI scale effect is unresolved.
- Wang & Sun report that the update-count task is mostly same-key old values; Chattaraj report PI errors 56.1% intrusion but 42.5% retrieval failure, with bimodal runs (>85% or <5%) at N>=200. Bimodality suggests sampling or format effects.
- Human literature says RI usually exceeds PI in strength for paired associates, while Chattaraj finds PI harder for LLMs. One paper only.
- Keppel & Underwood 1962 vs Peterson & Peterson 1959 own data: PI explanation for STM forgetting was imposed later; the original data show improvement over blocks.
- Weak mitigation results: Sculptor (trained) strongly helps, prompt-only barely (+5.9 or 0), consistent with Wang & Sun, not contradicting.

## Weak spots
- Almost all LLM evidence is synthetic key-value or QA benchmarks; none uses an agent doing real multi-step work with interfering memories.
- Several 2026 items are single-paper, arXiv-only, some preprints with garbled tables.
- Mitigation numbers (Wang & Sun mock reset, MINTEval timestamps) exist only in figures.
- No test of "cap similar entries per class" directly. Closest are Xiong (selective add), Kerestecioglu (dedup), CMI (relationship).
- No human release-from-PI effect sizes beyond Baeuml & Kliegl; Wickens 1963/70 numbers never opened.

## Only seen in snippets or secondary (opened:false)
a19 Underwood abstract figures, a27 and b24 Keppel & Underwood 1962, a29 Greenberg & Underwood, a30 Briggs/Barnes & Underwood, a33 and b27 Anderson & Neely, b21 Hubbard et al. 2018, b23 Wickens, b25 Underwood 1957 original, b26 Feredoes 2006, c25 Chroma secondary. Claims leaning on these (K16, K17) are marked contested or rely on opened reviews.

## GAPS
1. Does capping the number of similar entries per class (e.g. 3 to 5) improve agent task performance at equal tokens in a real multi-step agent, versus add-all and selective-add?
2. Does a category change (release from PI) work for an LLM: does rotating or labelling entries by category and retrieving from a different class restore accuracy?
3. Is the Chattaraj PI-harder-than-RI result reproducible, and does it hold for current frontier models and with retrieval-style instead of in-context memory?
4. What is the real size of timestamp/version-tag and supersession-link benefit (Mint-Eval Fig 8, STALE), and does tagging beat deletion?
5. What is the dose-response curve of near-duplicate count versus accuracy in a RAG memory with realistic (not synthetic) entries, and where is the knee?
6. Which structural resets (mock QA turn, summarize-and-restart, fresh context) work best against PI at equal tokens, and what is the exact gain of the mock QA reset?
7. Do reasoning tokens help finding the latest version, given o1 has RI 186 but PI 22?
8. What are the actual numbers for human release-from-PI (Wickens 1963/1970; Keppel & Underwood 1962) and the spacing boundary (Underwood & Ekstrand), to calibrate the human analogy?
9. Does item length (verbose entries) cause the interference, and does compressing memory entries to short normalized forms reduce it?
10. Does the PI effect depend on semantic similarity (word-type vs numeric distractors, as in the quantization paper) and can a similarity threshold decide which entries to merge or cap?

## Gap search results (evidence_d.jsonl, d01-d19; claims K26-K30 added)
Search limits: the web search quota ran out early and the arXiv, OpenAlex and Semantic Scholar APIs returned 429 or no budget. Papers already known were opened directly. The sweep for newer papers is incomplete.

1. Cap similar entries (OPEN). No paper tests a per-class cap at equal tokens. Nearest: Xiong (add-all 13.05 vs strict 38.50 on EHRAgent, record counts not tokens), Decocted Experience (sweet spot at intermediate memory size, no numbers), AIM (ICLR 2026, per-item interference ledger best under load, no numbers read). CMI gives the dose-response that a cap would target (gap 5).
2. Release from PI for LLMs (OPEN). Nothing found. Chattaraj lists category shift only as background. Cheap in-house test.
3. Chattaraj PI > RI (PARTLY CLOSED). Frontier models are in the 39: GPT-5 186.4 vs 99.2, o3 185.8 vs 76.0, Gemini-2.5-pro 162.5 vs 123.6, Claude-4.5-opus 178.4 vs 170.3 (gap nearly gone). No independent replication, and no retrieval-memory version. Same lab only.
4. Timestamp and supersession (MOSTLY CLOSED). MINTEval text has the numbers: drop 13.22 to 5.48 (Full), 31.43 to 10.45 (RAG). Li and Li: hiding superseded revisions beats keeping them active by 23.3 / 33.3 / 23.0 points. Nakshatri: a bare date hint gives no gain. Still no head-to-head of tag-and-keep vs delete. STALE has no ablation.
5. Dose-response (PARTLY CLOSED, synthetic). CMI: lexical drop is complete by 2 entries then flat; dense keeps falling to 8 (same-slot stability .92 to .54). Counts 0,2,4,8 only. No real-entry knee for 3 to 5.
6. Structural resets (OPEN). Wang and Sun anchor: with the mock QA reset, Gemini Flash 2.0 at 150 updates matches its no-reset score at 30-45 updates. No comparison to summarize-and-restart or fresh context.
7. Reasoning tokens (CLOSED for this paradigm). Reasoning models score 0 on PI at N>=50 (6 models); o1 PIES 22.0. Reasoning does not help.
8. Human numbers (PARTLY CLOSED, second-hand). Keppel and Underwood 1962: .99 on Trial 1, .58 on Trial 3 (via Loftus and Patterson). Release 91 percent for content shift, 74 percent for time shift (via a thesis). Release grows with category distance. Primary Wickens 1963/1970 and Underwood-Ekstrand tables were not opened. A 2018 study found no release in its paradigm (snippet only).
9. Item length (OPEN). Only Wang and Sun (length as driver). No test of compression as a fix.
10. Semantic similarity threshold (OPEN). Arjmandi has no similarity measure; the fan-effect paper (Roberts) is weak and model-dependent; Kerestecioglu thresholds 0.542 and 0.559 not reconfirmed. MINTEval: out-of-domain distractors hurt RAG most, which cuts against pure similarity.

Extra finding: Arjmandi shows distractor removal helps small models (Haiku 4.5 +0.083, Sonnet 4.6 +0.104) but barely helps Opus 4.7 (+0.008) or GPT-5.5 (+0.017). Caps may matter less for the strongest models.
