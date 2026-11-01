# C08.05 Retrieval and similarity: cross-check critique

## Corrections made (sources re-opened this session, arXiv PDFs via pdftotext)
Re-checked against the papers: KATE (a13/b01/c01), EPR (a15/a16/b04/c03), CEIL (a17), UDR (a19), Min et al. (b12/c07), Lost in the Middle (a29/b18/b19), Memento K (a26/c10), ReasoningBank k (c12), ExpeL ablation (c13), Levy et al. (c06).

Confirmed unchanged: KATE closest-10 46.0 vs farthest-10 31.0, IMDB 87.95 +-2.74, kNN-roberta 50.20; EPR dev table and the 84.5% copy rate; CEIL 30.68/45.84/53.37/56.76 (extracted row labels are shifted one row, mapping is right); UDR numbers; Min mean drops 2.6 (classification) and 1.7 (multi-choice); Memento K table; ExpeL 40.0/48.5/42.5/59.0 (label column also shifted, mapping right); Lost in the Middle closed-book 56.1 and oracle 88.3.

Corrections and additions:
1. c12 flagged k=2 = 46.0 as "my reading". Confirmed in text: "46.0 with 2, 45.5 with 3, 44.4 with 4"; k=0 is 39.0, k=1 is 49.7. c12 is now solid.
2. b19 describes 56.1 vs 56.0 (4K vs 16K) and 48.3 vs 48.2 as a "closed-book/oracle comparison". Those are the closed-book column only; oracle is 88.3/88.6 and 76.1/76.4. The point (longer context does not change closed-book score) is a trivial result, and it is not evidence that long-context models read the middle no better. Do not use b19 for that.
3. c06/a24 "50.3 to 73.5" is Top-K vs Cover-LS on the SMCalFlow-CS 32-C split (32 cross-domain training examples), Codex, a 100-example random test subset. Table rows are shifted in extraction. New boundaries read from the table: on the 0-C (zero-shot) split Cover-LS scored 0.3 while Top-K scored 17.0 and Cover-Utt 35.3; on COVR-10 random (69.4) beat Top-K (61.8). So "diversity wins" is split-dependent and one method collapses at zero cross-domain data.
4. b12 vs c07 on Min et al.: not a conflict. b12 gives the paper's text means (2.6, 1.7); c07 gives per-model figure ranges (0.8-1.6 for k sweeps). Both stand.
5. a14 left the 50.20 row unidentified; b02 and c02 (and the paper) identify it as plain kNN label voting. Settled.
6. a22 says exact deltas not recorded; now recorded (K11).

## Contradictions and tensions between sources
- Similarity vs diversity: pure top-k wins on easy tasks (b09 SST-2) and loses on compositional ones (c06, b09 SQuAD). The tension is real and depends on task difficulty and on whether any stored case is truly close. Not resolved by any paper that varies case-base coverage directly.
- Labels do not matter (Min) vs near-duplicates get copied (EPR copy rate, KATE). Min used random fixed demos; EPR/KATE retrieve near-duplicates. Nobody tested corrupted labels on retrieved near-duplicates.
- Power of Noise (c20) says random documents can help while Lost in the Middle and GSM-IC say irrelevant text hurts. Different models, tasks and placement; mechanism unknown.
- Memento says best K=4 and ReasoningBank says best k=1; case type differs (plans vs strategies) and neither reports variance.
- BM25 beats SBERT in EPR (structured outputs) but learned dense wins in RAG (a23). Task-dependent; BM25 won only on FEVER-like entity-heavy tasks in RAG.

## Weak spots
- The three evidence files heavily overlap: KATE, EPR, CEIL, Memento, Min, Lost in the Middle were each read two or three times. "Independent sources" in claims.jsonl counts distinct papers, not agents. Real independent source count is about 25 papers.
- Most ICL-retrieval results use GPT-Neo 2.7B, GPT-J, GPT-3 or Codex. Almost none use 2025-26 frontier models; Memento and ReasoningBank are the exceptions, with no variance reported and single runs.
- No paper isolates retrieval quality in agent loops at equal tokens; most compare against no memory, not against random memory. Memento, ReasoningBank, Sarukkai and CASCADE lack random-case controls.
- Many gains are on tiny test sets (KATE NQ 100 questions, CBR-RAG 32 cases, Levy 100 examples).
- Cited effect sizes are accuracy deltas with no confidence intervals in most tables.
- CASCADE (preprint, 2026) and the Huawei test-script paper (a28, not opened) are the least solid.

## Seen only in snippets or not opened
a06 Tversky 1977, a07 Aamodt and Plaza, a08 Richter, a09 Bergmann, a10 Smyth and Keane, a11 Lenz and Burkhard, a12 MAC/FAC, a28 Huawei CBR, a30 Wilkerson and Leake. The Weber and Richter classic theory (the subfield's named key works) is entirely unread; this is the largest hole against the brief. Cover and Hart, Aha et al., and all LLM-era numbers were opened. I did not re-open Aha et al. (a02-a04), Das et al. (a24), Dr.ICL (a21, no numbers) or DS-Agent this pass.

## GAPS (most decision-relevant first)
1. At equal tokens, does retrieving k=1 similar solved case beat a random solved case and a no-case baseline for a 2025-26 frontier model on multi-step reasoning tasks (not parsing or QA)? No paper has the random-case control there.
2. Do retrieved near-duplicate cases get copied, and does a wrong stored solution then hurt? (Min et al. tested only random fixed demos.) Corrupted-label test on retrieved cases.
3. Does adaptation-guided retrieval (rank by cost to adapt, Smyth and Keane) beat similarity-ranked retrieval with an LLM adapter? Unread classic; no LLM-era test found.
4. What keys work best for indexing cases: raw problem text, LLM-written abstract of structure, plan text, or outcome? BRIGHT suggests reasoning-rewritten queries help; no case-memory paper compares keys.
5. When should the agent skip retrieval? Need a similarity-threshold or confidence gate: Levy's zero-shot collapse, Memento's in-distribution +0.4, and distractor harm all point to a harm region, but no measured gate exists.
6. How does utility-weighted retrieval (EPR-style outcome re-ranking) behave with a tiny online case bank (tens, not thousands of cases)? EPR trained on thousands of labelled items.
7. What do Weber, Richter and Bergmann local-global similarity weights buy over a single embedding in an LLM era? Read the classic works and look for any ablation of per-attribute weights.
8. Is the 20-28% LLM-vs-kNN case-choice agreement (Wilkerson and Leake) real, and does LLM-chosen retrieval beat embedding retrieval downstream?
9. Do Lost-in-the-Middle position effects persist for 2025-26 models when 1-4 retrieved cases are placed in a prompt (short context)? Probably small, untested.
10. How does case-bank size affect retrieval quality and noise (Memento saturates at about 3k; Sarukkai marginal value falls)? Need a growth curve with forgetting, linked to the Case-base maintenance subfield.

## Gap search results

Second pass by the gap searcher. New evidence is in evidence_d.jsonl (d01 to d19); new claims K24 to K31; K02, K11, K12, K18, K21, K22 updated. Search was limited: WebSearch quota was used up early and the arXiv, Semantic Scholar and OpenAlex APIs returned HTTP 429, so I worked from papers I could open directly (PDF by arXiv id or CEUR/TCD links). Absence of a result below is weak evidence.

Closed or mostly closed
- Gap 2 (copying and wrong stored solutions): mostly closed. Xiong et al. 2025 show experience-following (output similarity rises with input similarity) and error propagation. Add-all memory lowered success 8 to 12 points vs a fixed memory; a strict filter raised it (d05, d06). Yoo et al. 2022 keep the Min et al. label result contested (d18). Still missing: a controlled corrupted-label test on retrieved cases with a frontier model.
- Gap 3 (classic AGR paper): the classic paper is now read (d01, d02): 100% vs 70% and 12% case choice, 3x faster. The LLM-era test is still missing (d03, d19).
- Gap 5 (when to skip retrieval): partly closed. Measured gates exist for QA: popularity gate +5.3 points, 10% of questions harmed by retrieval, confidence gate plateau, complexity router (d08 to d11). None is for case reuse and none uses a similarity threshold.
- Gap 4 (case keys): partly closed. LLM-written skill descriptions beat raw text on Spider (78.3 vs 74.6) and keep above random under perturbation (d12); Buffer of Thoughts supports distilled keys (d14). No paper compares plan text or outcome as keys.
- Gap 9 (position): partly closed for old models. Order swings accuracy from about 50% to over 85% at 4 examples (d16); permutation variance is lower with TopK but not zero (d17). No 2025-26 test.

Still open
- Gap 1: no random-case plus no-case control at k=1 for a 2025-26 frontier model on multi-step tasks. Closest: Yin and Leake PRIM at k=1 (gains 0 to 1 point for 70B and 32B models, no random arm, d04); Yasunaga fixed vs retrieved vs self-generated at k=5 (57 vs 54 vs 61, d13); Peng random vs TopK on GPT2-XL (d17).
- Gap 6 (tiny online bank): only indirect. History-based deletion needs at least 5 retrievals per case (d07), a floor that tens of cases rarely meet. No EPR-style test at that size.
- Gap 7 (local-global weights): classic Weber, Richter and Bergmann papers still not opened. CBR-RAG is the only weighted use found: +1.94% cosine over no retrieval with hand-set weights, 32 test cases (d15). No ablation of weights with correctness.
- Gap 8 (20-28% agreement): the Wilkerson and Leake figure was again not located; the survey cites that work only for trust (d03).
- Gap 10 (bank growth and forgetting): partly addressed by Xiong et al. (add-all hurts, periodic deletion cuts memory about 3x with 1 to 4 point loss on RegAgent, d06, d07). No growth curve for a case-reasoning bank of tens to hundreds of cases.

Practical lesson for the agent: store verified solutions only, gate retrieval on similarity or confidence, test per backbone, and always run a random-case arm.
