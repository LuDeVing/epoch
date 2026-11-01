# B04.08 Complementary learning systems: cross-check critique

## Numbers re-opened this session (10 checked)
1. McClelland 1995 Table 1 (a08): Dh 0.250 / 0.050 / 0.035 / 0.001 per day for Winocur, Kim and Fanselow, Zola-Morgan and Squire, Squire and Cohen; monkey D 0.025/day. CONFIRMED from the PDF text.
2. van de Ven and Tolias (a13, c08): Split MNIST Class-IL EWC 20.01, DGR 90.79, DGR+distill 91.79, iCaRL 94.57; domain-IL DGR 95.72, +distill 96.83; permuted Class-IL EWC 25.04, Online EWC 33.88, DGR 92.19, +distill 96.38. CONFIRMED against the paper table. Note: a13 prints DGR permuted columns fine; the "Permuted MNIST Class-IL: None 17.26" in c08 was not re-checked.
3. Scialom 2022 (a18, b13, c03): rehearsal 0 / 0.25 / 1%; CT0 keeps 99.8% (T0pp) and 98.0% (T0 3B) of upper bound over 8 tasks. CONFIRMED in text.
4. Ibrahim et al. 2024 (a21, b14, c04): 5% replay weak shift, 25% German; replay grid 0.5/1/5/10/50% and 25%. CONFIRMED. CORRECTION: c04 lists Gupta as first author; the paper's author order is Ibrahim, Therien, Gupta... It is the same paper as a21 and b14.
5. CLS-ER (a16, b10, c10): +176% over ER and +114% over DER++ on S-Tiny-ImageNet, buffer 200. CONFIRMED in text (relative percentages; a16's absolute MNIST-360 numbers rest on garbled tables and were not re-read).
6. Sparse memory finetuning (a23): NQ F1 drop 89% full, 71% LoRA, 11% sparse. CONFIRMED from arXiv abstract.
7. HippoRAG (a24 vs b19, c13): a24 says "10-20 times cheaper"; abstract says 10-30 times cheaper and 6-13 times faster. CORRECTION: a24 should read 10-30x. b19/c13 are right.
8. Sleep-time compute (c19): about 5x less test-time compute, +13% GSM-Symbolic, +18% AIME, 2.5x lower cost. CONFIRMED in abstract and body.
9. Lampinen latent learning (c01, c23): oracle retrieval without ICL sequences about 12% (reversal) and about 6% (codebooks). CONFIRMED in text.
10. Arani/Buzzega DER baselines: arXiv IDs for DER (2004.07211) and CLS-ER (2201.12604) resolve to the right titles; the DER table values (a14, c12) were not re-read from the table because extraction was garbled. Left as reported, flagged below.

## Duplicate entries, not independent sources
Three agents wrote about the same papers, so apparent triple support is one source:
- Scialom 2022: a18, b13, c03 (plus b26 and c21 which reuse it).
- Ibrahim 2024: a21, b14, c04.
- Luo 2023/2025: a19, b12, c05.
- CLS-ER: a16, b10, c10. DER: a14, c12. van de Ven: a13, c08. Kemker FearNet: a15, c09. Biderman: a22, b15. Huang SSR: a20, b18. EWC: a12, b07, c20. Gutierrez HippoRAG: a24, b19, c13. Rolnick: b08, b25, c06. Chaudhry: b09, c07.
- b21 / b22 / b23 / a05-a07 / a10 are primary studies read only via the 1995 or 2016 text.
The claims file counts independent_sources by distinct papers, not by evidence lines.

## Contradictions and tensions
- 1995 theory says new learning must be slow and interleaved to avoid damage; Tse 2007/2011 (via Kumaran 2016) say schema-consistent learning can be fast and still safe. Both are in the record; the new claim K17 is marked contested.
- Generative replay: works on MNIST (Shin 2017, van de Ven: DGR 90.79) but diverges for LLMs (LAMOL vs rehearsal). Different scales and domains, so not truly contradictory, but it limits transfer.
- Scale and forgetting: Luo finds worse forgetting up to 7B; Ibrahim shows replay fixes it at 405M and 10B. Different setups.
- Spurious forgetting (Zheng) and task-inference skew (Kotha) both say forgetting is partly not real loss, but disagree on mechanism and on whether replay helps (Zheng: 20% replay does not remove the alignment drop).
- Kemker 2018 (b11) finds all tested mechanisms fail on real data, while FearNet by the same first author reports 0.923. The self-reported gains of dual-memory methods are not yet confirmed by an outside group.

## Weak spots
- No direct LLM-agent test of the CLS claim (interleave old problems when writing a new lesson). All LLM evidence is weight-level fine-tuning; agent-level work (Reflexion, Generative Agents, MemGPT) is only CLS-adjacent.
- Many percentages are lab-reported, one paper each (sleep-time compute, sparse memory finetuning, Larimar, HippoRAG).
- Biology numbers come from a single theory paper's reading of four experiments; group sizes mostly missing.
- Table-derived numbers (DER, Rolnick, Chaudhry, Huang SSR) came through garbled PDF extraction in several lines; column mapping was inferred.

## Seen only in snippets or secondary reading
a05, a06, a07, a10 (read via McClelland 1995), a26, b21, b22, b23 (via Kumaran 2016 or 1995 text), a20/b18 partial table, c20 (opened:false). Merzenich dystonia is a personal communication.

## GAPS
1. Does interleaving old problems into a new-lesson update reduce regression in a frozen-weights LLM agent at equal tokens, and what regression-set size per lesson is enough? (Nobody has run this; K01, K04.)
2. Does a schema-consistency gate (write fast if the lesson fits an existing rule, replay-verify if novel) beat uniform replay, as Tse 2007 and Kumaran 2016 suggest? Needs a test with measured conflict rates.
3. Is real stored replay better than model-generated replay for prompt-level memory, given LAMOL's failure vs DGR's success? (K07.)
4. What is the dose-response of replay in an agent lesson store (0.25%, 1%, 5%, 25% of context or update tokens), compared with Scialom's weight-level curve?
5. Does an offline consolidation pass (sleep-time compute) improve a lesson store enough to pay for its tokens, beyond the reported 5x on predictable queries?
6. Is "forgetting" in LLM continual learning mostly recoverable by re-cueing (spurious forgetting)? If so, a verify-by-recueing step may replace replay.
7. Can an independent group reproduce dual-memory gains (CLS-ER, FearNet, DualNet) against well-tuned ER/DER++ at equal compute? Kemker 2018 suggests caution.
8. Do in-context or retrieval memories of old lessons beat distilled summary rules on derived/reversed questions only when the agent has practised using context (Lampinen)? What practice is needed?
9. Primary data behind graded retrograde amnesia (Kim and Fanselow N per group, Zola-Morgan and Squire effect sizes) were never opened; are the decay rates in Table 1 robust to modern replications (systems consolidation vs multiple-trace/transformation theories)?
10. Prioritised or salience-weighted replay (Kumaran 2016) for rare, hard lessons: does it help an agent's regression set more than uniform sampling?

## Gap search results (evidence_d.jsonl d01-d18; claims K20-K24 added)
Tool limits: WebSearch quota ran out after one query; arXiv API, Semantic Scholar and OpenAlex were rate-limited. Sources were opened by direct PDF/PMC fetch. Only the sources below were read; results are not exhaustive.

1. Interleaved old problems in a frozen-agent lesson update: OPEN. No study found (d18, K22). Closest: Zhang 2026 (d02) shows the damage is large (GPT-5.4 100% to 54% on a 19-problem slice; 58.5 to 38.5 mean accuracy over ten runs) and Tablan 2026 (d03) offers a hold-rate metric. Neither has a replay arm. Regression-set size per lesson: no data.
2. Schema-consistency gate vs uniform replay: OPEN. Indirect support only: gated Retain/Delete/Consolidate doubled accuracy over forced consolidation (d02); verified rules locked from edits (d03). K17 stays contested. Tse 2007 primary still unread.
3. Real vs generated replay: PARTLY CLOSED for weights. Fewer than 20% of 24,000 LAMOL pseudo samples were valid (d06). Raw stored episodes beat model-written abstractions in d02 and d03, which is the prompt-level analogue. Direct agent test still missing.
4. Dose-response of replay in a lesson store: OPEN. Nothing beyond Scialom (weight-level).
5. Does an offline pass pay: PARTLY CLOSED. Boundary found: about 1.5x not 5x on SWE-Features, and worse at high test-time budgets (d09). Gain tied to query predictability (d08). Still one paper.
6. Is forgetting recoverable by re-cueing: PARTLY CLOSED. Weight-level recovery is near 100% (d05) but needs training on old data or ten irrelevant instances. Prompt-only recovery by translation is partial (d07: 1.0% vs 56.75% drop). A prompt re-cue step for agent lessons is untested. Mechanisms still differ.
7. Independent reproduction of CLS-ER, FearNet, DualNet: OPEN. Soutif-Cormerais 2023 (d11) did not include them, found no clear winner, and called tuned ER very strong; Buzzega 2020 (d12) got +51.2 and +26.9 points just from tricks on ER. K06 stays single-source.
8. In-context vs distilled rules on derived questions, practice needed: OPEN for retrieval. Lampinen 2025 (d10) shows fine-tuning on in-context inference traces closes the gap; the 12% and 6% oracle-retrieval figures are not in that paper (they belong to c02), so the practice question is not answered.
9. Animal decay rates: CLOSED as a negative. Primary studies opened (d15, d17, d16). Gradient exists (1 vs 50 days, F(1,24)=16 in Anagnostaras 1999) but Table 1's per-day rates are model fits; several labs report flat gradients (Lehmann 2007, Sutherland 2008, Sparks 2011, Broadbent and Clark 2013). K02 moved to contested. Kim and Fanselow 1992 and Zola-Morgan and Squire 1990 were read only via the 2015 review.
10. Prioritised replay of rare hard lessons: OPEN, leaning small. MIR +2.8% accuracy and -2.5% forgetting on MNIST Split; PER wins 41 of 49 Atari games (RL); independent benchmark shows no clear winner (d11, d13, d14). No test on rare-lesson regression.

New tension: Hu 2026 (abstract insights reduce forgetting, +3.5 vs -4.0 BWT) vs Zhang 2026 (forced abstraction regresses solved problems). Different tasks and memory modules; unresolved.
Fetch-summary caveat: d15, d16, d17 were read through a fetch tool that summarises the page, so exact table values may be ambiguous.
