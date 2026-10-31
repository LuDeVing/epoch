# A06.01 Encoding specificity and cue-dependent retrieval: cross-check critique

## Corrections and confirmations (sources re-opened this session)
Checked against text in D:/research_scratch/A06.01 (pdftotext copies):
1. Murre (2021) PMC8568063: F=1.999 p=.163, F=16.2, F=.601 p=.440, original F=22.0 -> eta2 .647, d>=2.708, land-learned p=.47, underwater-learned better on land p<.01. All confirmed. Addition: the paper says it had results-blind in-principle acceptance, but its Stage 1 preregistration "was performed after data analysis", so call it "in-principle-accepted replication", not a clean preregistration (a10 says preregistered).
2. Thomson and Tulving (1970) Exp I: 15.7 (W-W), 20.2 (S-S), 19.0 (O-S), 11.1 (O-W), 9.2 (S-W), 13.9 (W-S) confirmed in text.
3. Higham (2002): free-report .24 / .29 vs no cue, confidence 3.41 (weak) vs 1.84 (strong), and Santa and Lamwers 5.33 / 5.40 / 10.07 confirmed.
4. Smith and Vela (2001): QT 242.47, QB 18.60, chi2 6.67, d .28 (CI +-.05), .68 interference reduction, .45 multiple contexts, .62 different experimenter (n=18), 1 day-1 week .63 (CI +-.21, n=6) confirmed.
5. Goh and Lu (2012): Exp 1 .37/.24 (F 17.14), .28/.28, interaction F=13.89; Exp 2 .31/.20, interaction F=5.23; Exp 3 overload F=90.24, cue types .32 > .25 > .09 confirmed.
6. Stern and Nadel (2026): 73.7 vs 53.5, +20.2, CI [12.1, 29.3], single-session 75 vs 75 p=.657 confirmed from the paper text.
7. Guo, Wu, Yiu (2026): human 91.2/82.4/71.8, DPR 94.1/76.3/58.2/44.7, slopes .41/.67/.53 confirmed in text.
8. Berglund et al. (2024): NameToDescription 50.0 same, 0.0 reverse; DescriptionToName 96.7; GPT-4 79% vs 33% confirmed (the 33% and 0.1% not re-seen).
9. Dinh et al. (2026): 50% to 90% counterfactual on V swap, 100% hallucination on K+V swap confirmed. Note a26 and b24 say "hallucination" while c01 says "100% counterfactual"; use the paper's word, hallucination.
10. Not re-opened: Poirier 2012 numbers, Smith and Manzano d values (b12), HippoRAG, HyDE, LongMemEval, A-MEM numbers. They come from earlier opened:true reads and match across a/b/c where duplicated (HyDE, Dinh, Smith and Vela, Thomson and Tulving agree across files).

Minor flags: a12 line "20% of effects exceeded d=.80" is a reading, not verified. a14 DOI was from memory. a16 and a18 contain no effect sizes. a25 "C5 to C7 +5 pp" versus c05 "C4 to C7 +6 pp" are the same step counted from different starting rows (48.5 vs 47.5).

## Contradictions between sources
- Global context: Godden and Baddeley (original d>=2.7) versus Murre (no effect) versus Smith and Vela (d .28) versus Saufley (null in 21 classroom tests). Best reading: real but small, very condition-bound; the diver study was an outlier.
- Match principle: Tulving's strict match (a01, a03) versus Nairne/Goh and Lu diagnostic value (b17, b18). Both predict the weak-studied-cue win; they differ on what happens at high overload, where match did not help. Poirier (a15) also supports discrimination over match.
- Strong cues: original "strong cues fail without encoding" versus Higham (forced report removes much of it). The effect is partly report criterion.
- Test type: Wikipedia (a28) says recall effects exceed recognition; Smith and Vela says no difference (.29 vs .27). Trust the meta-analysis.
- Context effect and associative processing: Smith and Vela find associative encoding removes the room effect, while Smith et al. video work finds large effects with one target per context. Cue overload is the common variable.

## Weak spots
- Founding papers Tulving and Osler (1968), Tulving and Thomson (1973), Tulving and Wiseman (1975), Godden and Baddeley (1975), Morris et al. (1977), Raaijmakers and Shiffrin (1981) were not opened; their content is secondhand.
- Almost all LLM evidence is one-run preprints: Stern and Nadel (n=20 per category, one benchmark, no scene-at-retrieval ablation), Guo et al., Chauvet (one 7B model), Dinh et al. (memorised book text). Only the retrieval-engineering papers (doc2query, HyDE, LongMemEval, A-MEM) have several benchmarks.
- No LLM study isolates encoding-retrieval match (same cue string at write and read) from enrichment in general. All "write-time enrichment helps" results confound extra information with extra cues.
- Human cue results use word lists; transfer to long agent notes is untested.
- Claim K04 is single-source (one replication) and K16 depends on an outcome not extracted.

## Seen only in snippets or abstracts
b21, b22, b23 (Eich, Nairne 2002, Tulving-Wiseman via other papers), b29 and b30 (abstracts), c24 to c27 (Jiang 2020 abstract; Eldan and Russinovich as cited; Ryu and Lewis; MemoCue and CDMem), a07, a08, a21, a23.

## Environment note
The C: drive was full (0 bytes free) when this cross-check ran, so claims.jsonl and critique.md could not be written into the research folder; they are in D:/research_scratch/A06.01/out/ and need copying.

## GAPS
1. Does a note written with scene or context plus the later retrieval cue beat the same note written without a scene at equal tokens, when the scene is NOT available at retrieval (the missing scene-at-retrieval ablation of Stern and Nadel)?
2. Is the benefit of write-time enrichment (keywords, likely questions) due to matching the later query's form, or only to extra tokens? A control with random extra tokens and one with same-length irrelevant keys is needed.
3. How large is the cost of a mismatched but semantically strong cue for a frontier LLM using retrieval (human: 9.2 vs 12.2 words)? No direct LLM replication of Thomson and Tulving with a frontier model exists; Chauvet used a 7B model.
4. What fan (items per cue) does an agent memory tolerate before accuracy falls, with entity/graph indexing versus dense retrieval, at equal context length (Guo et al. is a single preprint)?
5. Does forced-answer-then-score retrieval (Higham) beat free-report on mismatched cues for LLM agents, and does a "cues are associates" warning (Santa and Lamwers) change the model's use of retrieved items?
6. Does query rewriting into the stored form (HyDE) beat storing multiple forms at write time, and which costs fewer tokens on agent memory tasks rather than document search?
7. Do varied retrieval conditions during note use make notes cue-independent (Smith and Handy outcome not extracted; Saufley classroom null)? Needs the real numbers and an agent version.
8. What did Tulving and Osler (1968), Tulving and Thomson (1973) and Godden and Baddeley (1975) actually report (exact N, means)? Needed to settle the exact founding numbers.
9. Is the reversal-curse style cue-direction failure present for retrieved text in context (long-context models) or only in parametric memory?
10. Does the middle-of-context placement penalty interact with cue match (a matched lesson placed mid-prompt vs a mismatched one at the edge)?


## Gap search results

Evidence is in evidence_d.jsonl (d01 to d16). Web search quota ran out after the first few queries, arXiv and OpenAlex APIs were rate-limited, and the C: drive stayed full, so most sources came from direct PDF downloads by known arXiv id and the earlier D: scratch copies. Founding papers were not reachable.

Status by gap:

1. Scene written with the note, absent at retrieval: STILL OPEN. No paper runs this ablation. Nearest evidence is index-time context prefixes (d12: failure 5.7% to 3.7%/2.9%/1.9%), but the prefix is part of the stored text and there is no random-prefix control.
2. Form-match versus extra tokens: PARTLY CLOSED, negative side only. Expansion helps weak retrievers and hurts strong ones (d01), raw text beat LLM rewrites on LoCoMo (d05), random padding in the prompt can even raise accuracy (d02, prompt not note). No study separates matched keys from same-length random keys at write time. The test is still needed.
3. Cost of a mismatched strong cue for an LLM: CLOSED enough to plan with. Hard distractors cost 6-11 points for up to 70B models (d03), 0.5642 to 0.3626 for Llama2-7b (d02), and over 50 points when all retrieved passages are wrong for Claude 3.5 Sonnet and Gemini 1.5 Pro (d11). Not a Thomson-Tulving design replication with a frontier model.
4. Fan limits with graph versus dense indexing: STILL OPEN. Nothing new beyond the Guo et al. preprint (K08).
5. Forced answer or "cues are associates" warning: PARTLY CLOSED. Post-hoc fit checks work in small models (d09 NLI, d10 Chain-of-Note) and consolidation works for Claude and Gemini (d11); all cost some useful items. The exact Higham or Santa and Lamwers manipulations have no LLM test.
6. HyDE versus storing several forms: PARTLY CLOSED. HyDE gains depend on the model already knowing the stored text (d13: 40.0 vs 23.4 Recall@5, baseline 26.8); no head-to-head with multi-form storage on agent memory, no token costing.
7. Varied conditions making notes cue-independent: CLOSED for humans (d06): final recall .61 vs .43 with retrieval practice (Exp 1, N=45), no benefit with restudy (Exp 4, N=36, .36 vs .51 ns). Agent version untested. d15 adds that input processing decides whether context binds.
8. Founding numbers (Tulving and Osler 1968, Tulving and Thomson 1973, Godden and Baddeley 1975): STILL OPEN. Only secondhand: Godden and Baddeley Exp 1 had N=16, F=22.0 (d07); citation history in d14. Paywalled; search quota gone.
9. Reversal curse in context: PARTLY CLOSED. Short-context three-shot GPT-3 reverses at 96.7-100% (d08). Long-context retrieved text and recent models untested (leads in d16, not opened).
10. Middle penalty versus cue match: PARTLY CLOSED. Hard distractors hurt more at prompt edges (36-44% vs 28-34%) and reordering equals shuffle in real retrieval (d04). Matched-lesson-in-the-middle versus mismatched-at-the-edge was not run directly.

Corrections to earlier lines: K04 now states the replication was not cleanly preregistered. K10 changed to contested (enrichment gains depend on retriever strength and on keeping raw text). K17 now has the Smith and Handy numbers. New claims K20 to K27.

Remaining design-relevant unknowns: items 1, 2 (matched versus random keys at write time), 4 and 8.
