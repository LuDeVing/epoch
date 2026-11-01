# Critique: Analogical retrieval (MAC/FAC), cross-check

## Sources re-opened this session (numbers checked)
1. Forbus, Gentner, Law (1995) PDF: Table 2 reads LS .56, SF .53, AN .12, FOR .09. CONFIRMED a04. ARCS activations (LS .67, FOR -.11, SF -.17, AN -.27), Sour Grapes timing (ARCS 81-123 s vs MAC/FAC 0.2-0.3 s), ARCS up to 614 s, Table 4/5 values, SME 1 to 11 s per pair: CONFIRMED.
2. Gentner et al. (2009): t(122)=2.65, 88% vs 17% linking, chi2 N=73 6.12, 30% vs 78%, N=227 24.71, Red Adair 41% vs 30% p=.08, table of 124 (63% vs 42%): CONFIRMED.
3. Raynal et al. (2026) PMC: 14.45/d .84; 12.06/d .82; 11.82/d .54 CONFIRMED as reported.
4. Sourati et al. ARN: 76.9/73.2/45.3/33.9/57.3, humans 98.6/97.2/96.8/91.4, near 75.0 vs far 39.6, 1096 triples from 548 pairs: CONFIRMED.
5. AnaloBench: humans 96.0/72.5/73.3; gap 6.9 and 28.8 points: CONFIRMED. P@3 table present (42.9 / 6.5 / 3.9).
6. Jung et al. (2026): 1,300 queries, 10,573 pairs, best retriever 0.26, chance 0.07, reranker 0.81, 0.17 to 0.69, 0.25 to 0.70: CONFIRMED.
7. Puranam et al. (2025): 6.3 vs 8.7 (4/46), 20.3 vs 37 (17/46), original 29% vs 50% (8/28, 14/28), n=199: CONFIRMED.
8. Larraz and Corma (2026) PMC: 2/20 vs 20/20, Stokes 0/20 vs 18/20: CONFIRMED. NOTE: the baseline's Houdry/heat items match; guidance was supplied by the experimenter, so it is not a retrieval test.
9. Hope et al. (2017): P@1% 0.739 purpose-only; 749 ideas; 46% (N=105) vs 37% (49) vs 30% (54): CONFIRMED (k=2 run).
10. Yasunaga et al. (2024): the Table 1 values exist (75.0/14.8/60.8, 77.8/61.0/81.7), but row labels are lost in text extraction. See corrections.

## Corrections
- b02 and c02 give FOR = .03. The paper says .09. Use .09 (a04 is right).
- c18 labels 75.0% as "5-shot CoT" and 75.8-77.8% as self-generated variants. In the PDF text four rows appear (0-shot, 0-shot CoT, 5-shot CoT, Ours) and which row is which cannot be fixed from text; a33 and c18 disagree. Treat only "ours beats the baselines by about 4 points on average" and "last row is best" as safe. Needs a layout-preserving read of the table.
- a34 states the davinci-003 self-generated value as "inferred from a garbled table". Keep marked as uncertain (57-61%).
- Raynal 2026: Cohen's d values (0.84, 0.82, 0.54) do not match t/sqrt(n) (about 1.25, 0.9, 1.2); the authors likely used another formula. Report t values, treat d as not comparable.
- a20 says "two weeks"; a22/b02 say "about a week". The 1995 paper says the retrieval study was a week; not rechecked for the 1991 paper.
- a12/c01 call the paper "1994"; the Cognitive Science volume is 1995. The 1994 label comes from the QRG file name.
- a10 time range (6-37 s vs 17-614 s) and b08 (0.2-0.3 s vs 81-123 s) are about different probe sets; both are consistent with the "two orders of magnitude" claim in the paper.

## Contradictions between sources
- Surface dominance (Rattermann and Gentner 1987; Gick and Holyoak) vs Raynal et al. 2025-2026, where structure-only analogues win when the structure is familiar. Not a refutation: different cue design, everyday memories, not a story set. Real boundary condition.
- Webb et al. 2023 (GPT-3 does analogy) vs Lewis and Mitchell 2024 and Stevenson et al. 2025 (breaks with unfamiliar alphabets). These tests are letter-string and story-choice, not memory retrieval.
- Yasunaga: self-generation beats retrieval for large models; Rubin, Levy, ExpeL, RA-RFT: trained or structure-aware retrieval beats naive similarity. Both can hold, but they were never compared in one set-up.
- Task-level experience retrieval (HippoSpark, ExpeL) helps or hurts depending on the paper. ExpeL is positive (59.0 vs 40.0); HippoSpark finds trajectory retrieval hurts (.255 vs .326). Key difference may be benchmark and retrieval key.

## Weak spots
- MAC/FAC evidence is almost entirely one lab, simulations on 18 to 125 hand-encoded stories. No test with realistic memory size or with an LLM as the encoder.
- The human study (32 stories, 5 probes per type) is from a 1987 cited result; nobody in our set re-ran it. Raynal 2025-2026 are the only modern replications and they change the story.
- Gentner 2009 experiments are about negotiation and the fortress problem; no AI/LLM replication of the compare-then-recall effect.
- Several LLM results (AnaloBench T2, ARN) use tests of recognition or selection, not retrieval from a self-built store.
- 2026 arXiv numbers (HippoSpark, RA-RFT, ADR, CPR) are single preprints, not peer reviewed.
- Larraz and Corma is a hint study, 20 runs, one task.

## Seen only in snippets or via other papers
- Rattermann and Gentner 1987, Gentner Rattermann and Forbus 1993, Gick and Holyoak 1980/1983 numbers are second-hand (via FGL 1995 and Puranam).
- Novick 1988, Faries and Reiser 1988, Blanchette and Dunbar 2001 are cited but not opened.
- c29 (Sultan and Shahaf) is marked opened:false; its numbers come through StoryAnalogy and b29.
- Not re-opened this session: HippoSpark, RA-RFT, ADR, ExpeL, Buffer of Thoughts, BRIGHT, Thought Propagation, StoryAnalogy, Sultan and Shahaf.

## GAPS
1. Does an LLM-based two-stage retrieval (cheap embedding/keyword filter, then LLM structural rerank) beat one-stage embedding top-k and long-context stuffing at equal tokens, on a store the agent builds itself? No source tests this head to head.
2. How much of the human "surface dominates" effect transfers to an LLM agent retrieving from its own notes: does memory written as abstract schemas (K07) raise structural retrieval vs raw traces?
3. Does the compare-two-cases-before-retrieving effect (Gentner 2009) hold for an LLM? No replication exists.
4. When should retrieval fire (at start vs at stuck point)? HippoSpark and RA-RFT suggest start-of-task retrieval can hurt; what trigger rule works?
5. What shortlist size is right for the cheap stage? MAC/FAC says 10-20 percent of a tiny memory; what is the equivalent at thousands of items?
6. How often does a true structural analogue exist in an agent's memory? (Analogies about 3 percent of a corpus.) Retrieval gains cap at that base rate.
7. How do we stop false analogies? GPT-4 flags the correct and the wrong story (precision about 0.5). Which verification step (mapping check, candidate-inference test) cuts false positives at low token cost?
8. Does familiarity of the structure (named patterns) lift structural retrieval in LLMs the way Raynal 2025-2026 suggests for people?
9. Self-generated analogues (Yasunaga) vs retrieved cases: where is the crossover in model strength, and does it hold for current frontier models?
10. Are Yasunaga Table 1 row labels as claimed? Re-read the table with layout to settle the a33/c18 conflict before using any figure.

## Gap search results (2026-11-01, evidence_d.jsonl d01-d24, claims K26-K35 added)

Search note: WebSearch quota was used up and arXiv API and OpenAlex returned 429, so sources were chosen from the local set and from direct arXiv PDF and ar5iv HTML downloads. Every d-line was read this session. No new human-subject sources were opened.

### Closed
- GAP 10 (Yasunaga Table 1 labels): CLOSED (d01). Rows are 0-shot, 0-shot CoT, 5-shot CoT, Ours. 75.0 is the 0-shot GPT-3.5 value. a33 was right; c18 was wrong and K17 is rewritten. 5-shot CoT there is fixed exemplars, not retrieval.
- GAP 9 (crossover): CLOSED for the old models, OPEN for frontier models (d02, d03, d04, d05, K35). Table 4: retrieved beats self-generated up to davinci-001 (11 vs 9), tie at davinci-002 (47 vs 48), self-generated wins at davinci-003 (61 vs 57). Indirect newer signals say the benefit of self-generation and of structural scaffolds shrinks with model strength, and R1 says few-shot hurts. No direct test on current models.
- GAP 4 (when to retrieve): PARTLY CLOSED (d12, d13, d15, d16, d17, d18, K30). A gated trigger beats always-retrieve in four independent papers. Working rule: fire when the solver reports no clear next move, query with situation plus local goal, cap at 3-5 calls, and re-frame instead of retrying when the cap is hit; tune the gate per model. Start-of-task retrieval is contested (K16): it hurt in HippoSpark and RA-RFT, helped in ExpeL, and the retrieval key is the likely cause. No paper compares start vs stuck-point with the same key on analogue tasks.
- GAP 5 (shortlist size): PARTLY CLOSED (d06, d07, d11, d20, K28). For the LLM rerank, 10 to 40 survivors is enough; widening from 10 to 100 added -0.4 to +1.1 nDCG points on BRIGHT; the first cut of 151 to 40 lost 8.3 percent of positives in CPR. For the injected set, 1 item was best in ReasoningBank. No test on an agent-built store with thousands of items.
- GAP 6 (base rate of true analogues): PARTLY CLOSED (d14, d22, K31). Small stores give weak best matches (top-1 0.676 with 20 items vs 0.751 with 112) and CPR's analogy judgment dropped 91 percent of cross-topic pairs. Together with the 3 percent figure, expect no true analogue for most items. Still no measured rate on an agent's own memory.
- GAP 2 (schemas vs raw traces): PARTLY CLOSED (d05, d09, d10, d11, d24, K26). Distilled or abstract entries beat raw retrieved cases on task success in three independent agent papers (AWM +4.0 step SR over Synapse; ReasoningBank 48.8 vs 42.1; Dynamic Cheatsheet). Nobody measured structural retrieval rate itself, so the specific MAC/FAC claim (K07) is still simulation-only.

### Still open
- GAP 1 (two-stage vs one-stage vs stuffing at equal tokens): OPEN. Best proxies: CPR reranker 0.81 vs 0.26 at 20.2 calls and $0.071 per query (d06), Self-Route 38-61 percent of tokens for near-stuffing accuracy (d08), stuffing worse than no memory for GPT-4o (d09), 20-30 stuffed documents below closed-book (d19). No head-to-head on analogue retrieval from a self-built store.
- GAP 3 (compare-before-retrieve in an LLM): OPEN, untested (K33). Only ExpeL builds insights from failed-vs-successful pairs and does not ablate the pair step.
- GAP 7 (cheap false-analogy filter): OPEN. Candidate designs only: independent narrow checks (CoVe precision 0.17 to 0.36) and a mapping-plus-reject-taxonomy second call (kappa 0.84, n=50). Neither is tested on analogues, and no token-cost figure is reported (d21, d22, K32).
- GAP 8 (familiar named structures): OPEN, untested (K34). Only indirect evidence that LLM analogy accuracy drops with unfamiliar symbols (d23).

### Other corrections and cautions
- K16 changed from established to contested. The old text said inference-time retrieval lowered RA-RFT to 37.7; the paper shows 37.6 for a random trace and 38.5 for an off-the-shelf embedding retriever under RA-RFT training, against 43.3 for GRPO. The HippoSpark gain of .326 to .483 mostly comes from state assessment plus verification (.409 before any experience is added); experience adds .074.
- The Self-Route text quotes GPT-4O 46.83 vs LC 47.04, but the table average reads 48.89 vs 48.67. Treat sub-point gaps as approximate.
- ReasoningBank retrieved-count curve appears to be one domain (39.0 equals the Shopping no-memory value), not the overall score.
- All new LLM numbers are single papers on knowledge QA, math, web tasks or papers. None is a test of retrieving structural analogues from an agent's own memory.
