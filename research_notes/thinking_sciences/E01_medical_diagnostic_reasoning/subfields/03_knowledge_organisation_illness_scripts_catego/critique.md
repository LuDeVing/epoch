# Critique and cross-check: E01.03 Knowledge organisation, illness scripts, categories

## Sources re-opened this pass (numbers checked)
Confirmed exactly: Goh 2024 JAMA Netw Open (76 vs 74, +2, CI -4 to 8, P=.60; 519 vs 565 s; LLM alone +16, CI 2-30, P=.03); Healy 2026 UK replication (74.3 vs 65.7, p=.001; -21.3 vs LLM alone; 30% of questions; SD 12.8); Kanjee 2023 JAMA (45/70 = 64%, 27/70 = 39%, mean differential 9.0, mean rank 2.5, 66% agreement, kappa .57); Moghadami 2021 (15.74 vs 14.38, P=.009; SCT 6.12 vs 4.54, P=.0001; n=50 per arm); Nori 2025 (physicians 20% at $2,963; GPT-4o 49.3% at $2,745; o3 78.6% at $7,850; MAI-DxO 79.9%, 81.9% no budget, 85.5% at $7,184); Brodeur 2024 (78.3% CI 70.7-84.8; 52%; 88.6% vs 72.9%, p=.015; R-IDEA 78/80 vs 47/80 vs 28/80); Savage 2023 preprint (GPT-3.5 46/48/analytic -6 P=.001/differential -8; GPT-4 76/77/78/78); Schmidgall 2024 preprint (1,273 questions; 72.7, 51.8, 49.7, 33.4; GPT-4 -14.0 false consensus, -0.2 confirmation; false consensus -24.9, frequency -18.2 averaged).

## Corrections and discrepancies
1. Savage GPT-4 test size: evidence a23/b20 says 498 usable (20 errors); the preprint says 497 (21 errors). Use "about 497-498"; the published version may differ. The 38% vs 34% hard-NEJM result and the 65% vs 18% false-logic result are not in the preprint v1, so were not re-verified.
2. Schmidgall: c04 says GPT-3.5 "average drop 37.4%" (preprint wording); b23 says -17.8% (published figures). With unbiased GPT-3.5 at 49.7%, a 37.4-point drop is implausible, so 37.4% looks like a score, not a drop. Use the published -17.8 (GPT-4 -5.1) and treat 37.4 as unreliable.
3. c03 gives MAI-DxO cost $2,397; the paper text says $2,396 in one place and $2,397 in another. Trivial.
4. Evidence a15 and b12 are the same paper (Coderre 2003); Savage appears in a22-a24, b20, c01; Goh in a25, b22, c06; Yanagita in b19, c18; Hudon in a30, b28, c16; Coskun in a31, b32, c17; Lilamand in a29, b30, c12. Independent source counts in claims.jsonl were set accordingly. Listed counts are far fewer than 91 lines suggest.
5. Healy 2026 is labelled a replication, but its result is split: it replicates "LLM alone beats physician plus LLM" and does NOT replicate "no benefit from LLM access" (+8.6 points, p=.001 vs +2, p=.60). Different design (within-subject, 22 people, 4 vignettes).
6. The derived effect size "d about 2.0 pre to post" for Moghadami (b17) was computed by the agent, not reported by the paper. d=0.54 also appears derived. Treat as approximate.

## Contradictions between sources
- Intermediate effect: robust (Schmidt and Rikers review) vs vanishes when experts must comment on each finding (Norman, Wimmers). Not resolved.
- Biomedical knowledge: encapsulation says it is packed away; Rikers 2005, Woods and van de Wiel say it is still active and used on hard cases. Both are supported; the real question is when it is used.
- Prototype scripts vs exemplars (Brooks, Norman) vs causal models: Ark 2006 (additive effect) suggests they are not exclusive.
- LLM diagnosis: very high on NEJM cases (o1 78%) but meta-analysis pooled 52% across 83 mostly biased studies and only matching non-experts. Differences come from case difficulty, model generation and scoring.

## Weak spots
- Founding human studies (a01, a02, a04, a06, a08, a09) were seen as abstracts only. Their numbers are mostly absent. The 1980s-2000s sample sizes are small (a7: 18 and 17; a16: final 15/11/8).
- Almost all human studies are from a few groups (Maastricht, McMaster, Montreal).
- No direct test exists of "illness scripts help an LLM". The LLM evidence is indirect: script-style prompts (no benefit), scripts written by LLMs (partly wrong), SCT scores (rise with generation).
- Many LLM results are on exam-style vignettes (MedQA, NEJM) where the case text is clean; real-case results (Hager, MIMIC-IV) are worse.
- Vendor and preprint sources (Nori, Brodeur, McDuff) have no independent replication.
- Snippet-only or unopened: a01, a02, a04, a06, a08-a15, a18, a29-a31, b06-b16, b18, b29-b32, c07, c09-c14, c16-c17, c19-c20, c24, c26-c28. Takita 2025 meta-analysis (a26) and Woods 2007 (a13, a14, b07) were not re-opened here (PubMed lookups failed); their numbers rest on the first agent's reading.

## GAPS
1. Does giving an LLM an explicit stored class library of illness scripts (enabling conditions, key features, mimics) beat the same tokens spent on free chain of thought, on held-out NEJM-style cases? No study tests this directly.
2. Does a retrieved similar solved case (exemplar) help an LLM more than a prototype script, as Brooks and Norman found for humans, and does the combination (Ark 2006: 56% vs 42%) carry over?
3. Why did clinician-style prompts (Savage 2024) not help GPT-4? Does this still hold for newer reasoning models, and does it depend on the case being hard?
4. How good are LLM-authored scripts as a class library when checked by experts? Yanagita found 15.8% deficient; does retrieval from a verified source fix the errors, and which fields (cardiology, psychiatry) fail most?
5. Do enabling conditions (age, risk context, prevalence) actually shift LLM hypothesis ranking? Safranek shows base-rate cues swing sensitivity from 79% to 30%; what graded prior gives balance?
6. Is the intermediate effect (more detail, worse ranking) visible in LLMs, for example more findings listed but a worse differential when forced to elaborate?
7. What are the sample sizes, effect sizes and replications behind the founding Schmidt/Boshuizen, Custers and Brooks studies, which remain abstract-only here?
8. Do SCT-style updating tests predict real diagnostic accuracy of an agent, given that human SCT scores correlate poorly with factual knowledge and LLM SCT scores lag MCQ scores?
9. Does a challenger or devil's-advocate step (Schmidgall, Nori) recover accuracy lost to bias cues at equal tokens, or does it only add cost?
10. Are the claimed gains of structured role scaffolds (MAI-DxO) independent of the model and the benchmark, when run by someone other than the vendor?

## Gap search results

Evidence is in evidence_d.jsonl (d01-d25). claims.jsonl now has 33 claims (K25-K33 new; K02, K05, K07, K14, K17, K19, K20, K21, K24 revised). New status values used: "preliminary" (several independent preprints, none at equal tokens) and "open" (untested).
Search tools: WebSearch quota ran out after two calls; I used arXiv search pages, Europe PMC and direct PDFs. Semantic Scholar, OpenAlex and the arXiv API were rate limited. About 25 sources opened; the 1990s-2000s human studies are abstracts only (paywalled).

1. Class library vs same tokens of free CoT (gap 1): STAYS OPEN, but closer. Feng 2026 (d13) shows a verified, contrast-organised wiki beats no knowledge, random pages and BM25 pages (Qwen3.8-27B 63.0, 64.0, 67.0, 72.0, 75.5) and that removing it costs 9-14.5 points. It never compares with free CoT at equal tokens, and it is bundled with a review module. MedEinst (d14) is also positive.
2. Exemplar vs script vs both (gap 2): OPEN. No LLM study separates them. Ark 2006 detail now known: N=48, 12 per group, 42/41% vs 56/53% (d01). MedEinst combines exemplars and graphs. Fixed few-shot examples are unstable (d18).
3. Clinician-style prompts (gap 3): PARTLY CLOSED as explanation, OPEN as a test. A human parallel exists (Sibbald 2013, dual-processing instruction no effect, d09). ER-Reason (d16) shows reasoning models do not beat non-reasoning ones at belief updating. Noever (d24) shows difficulty splits matter (81% easy vs 43% hard). No study reran Savage's prompts on current reasoning models.
4. LLM-written script quality (gap 4): PARTLY CLOSED. Yanagita table: cardiovascular 6/14 and psychiatric 5/11 rated deficient; dermatology and respiratory none (d11). Scripts omitted frequency and sensitivity. Retrieval fix: only MamaBench (d15) tested verified retrieval, cutting failure rate by 4.0-5.5 points with about 20% still failing; no script-specific test.
5. Priors and enabling conditions (gap 5): PARTLY CLOSED. LLMs are weaker on numeric than semantic medical knowledge (Avnat, d12). No study tests a graded prior; the 79% to 30% swing (Safranek) stands alone. Open.
6. Intermediate effect in LLMs (gap 6): OPEN. No direct test. Indirect: trace quality only loosely tracks accuracy (R=0.56, d17), MedEinst names overthinking (d14), early commitment dominates (d23). Human side: effect depends on elaboration instruction (d05).
7. Founding human studies (gap 7): PARTLY CLOSED. Abstract facts recovered: Schmidt and Boshuizen 1993 (effect vanishes with restricted time, induced by priming), van de Wiel 1998 failed replication by the same group (linear rise, 4 cases, three study times), Rikers 2000, Wimmers 2005, Eberhard 2009 (61 students, 20 dentists, effect present), Norman and Brooks 1997 (30% specific similarity), Ark 2006. Original sample sizes for 1993 and Custers 1996 are not in abstracts and stay unknown. K02 stays contested.
8. SCT predicts real accuracy (gap 8): OPEN. ER-Reason (d16) gives SCT-style scores and final-diagnosis accuracy but does not report how one predicts the other. Keemink 2018 (d10): script richness did not correlate with exam score (r=-0.006), a caution for proxy metrics.
9. Challenger at equal tokens (gap 9): OPEN, with a lean. DMoA (d19): most of the gain comes from several proposers; the rebuttal adds about 1-1.5 points. The Duke-NUS 71.3% result has no control (d20). Counterfactual multi-agent (d18) beats other agent methods but not at stated equal tokens. Schmidgall mitigation was prompt education, not a challenger (d21). MedEinst debate agents did worse (d14).
10. MAI-DxO independent replication (gap 10): OPEN. I found no third-party rerun. MedAgentBoard (d22) and the leakage audit (d25) are indirect cautions only.

New caveats found while checking: (a) the arXiv ids 2606+ papers are all preprints, most by single labs; (b) Feng 2026 and Chen 2026 build their own benchmarks and fixes; (c) Table text in the Schmidgall and MedEinst PDFs extracted poorly, so some per-cell values are marked uncertain; (d) Europe PMC abstracts were treated as "opened" for the human studies, but full texts were not read.
