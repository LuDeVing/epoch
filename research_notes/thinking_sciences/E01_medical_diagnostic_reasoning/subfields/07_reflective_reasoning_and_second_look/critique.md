# E01.07 Reflective reasoning and second look: cross-check critique

Checked against evidence_a/b/c.jsonl (101 lines). 21 claims in claims.jsonl (K01-K21).

## 1. Numbers re-opened this session (PubMed abstracts via NCBI eutils, arXiv PDF text)

Confirmed exactly:
- Staal 2022 (BMJ Qual Saf): 29 studies, 2732 participants, g=0.20 (0.10-0.29), I2 70 to 38 percent after removing 3 training studies. Confirmed. NOT confirmed from the abstract: "17 of 29 were verification after initial diagnosis", "only 2 of 29 in real practice", "13 of 29 same cases". Those stay single-read from full text (a24 says opened).
- Prakash 2019: 44 studies of 10,114 screened, 4380 professionals, guided reflection ES 0.38 (0.23-0.52). Confirmed. Abstract says "deliberate reflection on a formulated diagnosis", which supports a second look after a hypothesis exists.
- Ilgen 2013: N=393, F(1,379)=2.44 P=.12, complexity F=965.2, experience F(2,379)=39.6. Confirmed. The abstract also says first impressions gave better assessment reliability (alpha>=0.75 more efficiently). Evidence lines omit this.
- Mamede 2020 Think Twice: N=167, initial 0.22 vs final 0.26 P<.001; group means as in a17/b07. Confirmed. The abstract's conclusion is that reflection helps "independently of the evidence searched", and it has no control arm without a second pass.
- Monteiro 2015: 12/19, 9/11, 8/17 revised at least one; 8 percent of diagnoses; 1.20 to 1.22 of 2, t=2.15 p=0.03. Confirmed. NOT in the abstract: "18 percent of incorrect diagnoses revised to correct", "60 of 745". Unverified here.
- Costa Filho 2019: N=61, 49.7+/-12.1 vs 38.4+/-14.6 p=0.002; confidence 64.3 vs 58.9 p=0.228; calibration 0.15 vs 0.20 p=0.197. Confirmed. Note a09 gives p=0.21 and 0.19 and b19 gives 0.228 and 0.197; the abstract matches b19. Use b19.
- Huang 2024 (arXiv 2310.01798, Tables 2 and 3): all GPT-3.5 and GPT-4 numbers in b29/c01/c02 confirmed (CSQA 75.8 to 38.1 to 41.8; GPT-4 GSM8K 95.5 to 91.5 to 89.0; oracle 84.3, 89.7, 29.0, 97.5, 85.5, 59.0). c03's Llama-2 and GPT-4-Turbo figures were not rechecked.
- Savage 2023 (arXiv 2308.06834): test set 518, GPT-4 set 497 after 21 API errors; GPT-3.5 analytic 40 (-6, P=.001), differential 38 (-8), Bayesian 42 (-4, P=.02); GPT-4 differential +2.2 (P=.24). Confirmed. The published npj paper's own abstract says GPT-4 can mimic reasoning "without sacrificing accuracy", which is the same finding framed as non-inferiority.
- Mamede 2010 availability bias (JAMA): N=36, 18+18; second-year 1.55 (CI 1.15-1.96). Confirmed in the opened part.
- Mamede 2010 conscious thought (Psych Res): abstract confirms the expert-by-complexity pattern, no N in abstract (N=34 residents and 50 students rests on the a04 full-text read).
- Case revisitation 2026 (Diagnosis): N=67, chi2(1)=7.68 p=0.006. CORRECTION: the abstract gives OR=1.77 with CI 0.76-2.78 and OR=0.56 with CI 0.24-0.89, both p=0.050. A CI of 0.76-2.78 includes 1 and does not match p=0.050 and the OR 0.56 cannot lie in a CI reported as an odds ratio for the favoured group. Treat both simple effects as not established; only the interaction is reported reliably.

Corrections made to the evidence set (not edited in place, recorded here):
- a09 p-values for confidence/calibration (0.21, 0.19) should read 0.228, 0.197.
- a30/b37 effects labelled "OR=1.77 (p=0.050) favouring no access" must carry the caveat above.
- a24 sub-counts and a36/b06 "18 percent" figure are not in abstracts; mark as full-text-only.

## 2. Duplicates (do not count as independent)

a03=b01; a04~b25; a05=b12; a06=b14 partial; a07=b13; a09=a10=b19 (one study); a11=b20; a12=b21; a15=b15; a16=b16; a17=b07; a18=b08; a19=b05; a20=b17; a23=b03; a35=lambe study (b04 reviews it); a36=b06; a37 separate; a30=b37; c01=c02=c03=b29 (one paper); c05=c06; c07=c08=c09; c10=c11. Independence counts in claims.jsonl are based on this.

## 3. Contradictions between sources

1. Reflection helps experts on complex cases (Mamede 2008, 2010) but Schmidt 2017 found a gain on simple and complex cases alike, Costa Filho found gains on easy cases (76.8 vs 60.1) and a weak one on hard (22.7 vs 16.7, p=.08), and Think Twice found a gain only on very hard cases with floor accuracy 22 percent. The difficulty rule is not stable. K02 is marked contested.
2. Structured DR beats first impression in Mamede lab trials, but Ilgen 2013 (N=393) and Lambe 2018 (N=186) show nothing. The DR lab's defence (bottom-up hypothesis order) is untested by anyone else.
3. Structure vs no structure: Think Twice shows plain return equals for/against; Monteiro shows free self-directed return gives almost nothing; Ibiapina shows guided beats free. Reading: some guidance matters in learning, but at diagnosis time the second look itself may be most of the effect. Unresolved.
4. b38 and a04: "more than 35 percent gain" vs initial 0.45 to final 0.58 (29 percent relative). Different measures; not reconciled.
5. LLM side: Huang and Kamoi say self-correction fails, MedAgents/MDAgents/DERA say critic loops help. The helpful studies add retrieval, roles, extra calls or physician judges, and none holds tokens equal.

## 4. Weak spots

- Nearly all human evidence is written vignettes with the full information given, one lab network (Mamede, Schmidt, Rotterdam and Brazil), small N (34 to 119), students or residents.
- No human study separates a structured second look from simply spending more time or seeing the case twice. Staal notes 13 of 29 shared this flaw.
- No real-practice DR trial. Staal found only 2 of 29 in practice.
- Mechanism claims (knowledge activation, reprocessing under each hypothesis) are not tested directly (a26).
- LLM studies: most are exam multiple choice or vignettes likely in training data. No LLM study tests the exact DR procedure (for, against, expected-but-missing, alternative) against a plain second pass at equal tokens.
- c-file evidence lines for 2025-2026 LLM studies were read as abstracts and partial text; effect sizes were not recomputed (for example the 2026 medical QA self-correction study differences of about one point at n=244 to 1273 are within noise).
- Chernikova 2019/2020 (a37, g 0.58 vs 0.26) not re-opened this session; it mixes teacher and medical education.

## 5. Only seen in snippets or abstracts

a03, a05, a06, a07, a08, a11 to a14, a17, a18, a19, a21, a22, a23, a29, a30, a31, a32, a35 partly, b09, b14, c10 results tables, c12 effect sizes, c16 last 10k characters, and the 2023 review used as source for a02, a25, a26 (self-description by the DR lab).

## GAPS (most decision-relevant first)

1. Does a structured for/against/missing/alternative second look beat a plain second pass (re-read and re-answer) at equal tokens for an LLM, and on which items (hard vs easy)? No study tests this.
2. Does an LLM second look with a code or tool-judged trigger (external check) beat one with a model-judged trigger, in diagnosis rather than math and commonsense?
3. What is the net flip rate (correct-to-wrong vs wrong-to-correct) of LLM diagnostic revision, and does it depend on first-pass confidence or sample agreement as a difficulty gate?
4. Is there any real-practice or non-vignette trial of deliberate reflection with patient outcomes, or only vignettes?
5. Does the bottom-up hypothesis order (hypotheses emerging one at a time from findings) matter, as the DR authors claim, versus listing a differential first? Any independent test?
6. Do LLMs trained on reasoning (o3, R1 class) already do the second look internally, so that an added scaffold step is redundant? Which published comparisons exist at equal thinking-token budgets?
7. Does retrieved look-alike contrast knowledge (discriminating features) outperform a process prompt for LLMs facing availability-style and anchoring cues?
8. Can an LLM's confidence be used to decide when to reflect, given that human confidence did not track accuracy and Huang shows self-judgement fails?
9. Do multi-agent critic gains (MedAgents, MDAgents, DERA) survive a matched-token single-agent baseline?
10. Are there independent replications (outside the Mamede/Brazil network) of the delayed-learning effect and of the cued-reflection advantage?

## Gap search results (evidence_d.jsonl d01-d27, claims K22-K30 added)

Search note: WebSearch quota was exhausted, arXiv/OpenAlex/Semantic Scholar APIs returned 429 or quota errors, so sources were found through PubMed eutils, known arXiv ids and PDF text. Search coverage is therefore narrower than usual; "stayed open" below means not found, not proven absent. PDFs were read as full text (d01-d16); PubMed items are abstracts only (d17-d27).

Closed or mostly closed:
- Gap 3 (net flip rate): mostly closed for diagnosis. An "Are you sure?" challenge to 10 LLMs on 120 vignettes gave 544 right-to-wrong vs 198 wrong-to-right flips, accuracy 51.8 to 42.2 (d17, abstract). Math flip table for an untreated model: 15.8 percent right-to-wrong vs 4.6 percent wrong-to-right (d13). Not closed: whether first-pass confidence or sample agreement separates the harmful flips from the helpful ones in diagnosis (no study). New claim K22.
- Gap 9 (do critic gains survive matched tokens): closed outside medicine, partly in medicine. Matched-budget studies find same-model debate and self-refinement lose to CoT-SC or a single reasoning pass (d01, d03, d05); mixing different models is the part that helps (d04). In medicine the margins over CoT-SC are small and unmatched (d06, d07, d02). K17 changed from single-source to contested. New claims K24, K25.
- Gap 8 (confidence as a reflect trigger): mostly closed. Verbalized confidence overestimates; sample consistency has AUC 0.66 to 0.79 in diagnosis (d18); probes work but need weights (d15). Not tested: sample-agreement gating of a second look inside a diagnosis pipeline. K27 single-source.
- Gap 2 (tool-judged vs model-judged trigger): partly closed outside diagnosis. Reflexion with an oracle stop beat SC; with a GPT-4 judge it did not (d03). Prompt wording is a major hidden factor (d14, d12). No diagnosis-domain test. K23 added; K13 updated.

Partly answered:
- Gap 6 (reasoning models already do the second look): not settled. Medical reasoning models gain from thinking tokens up to 256 to 512 (routine) or about 4K (hard), forced Wait re-thinking adds little and sometimes breaks correct answers (d08, d09); reflection words do not track accuracy (d11); R1 still anchors (d10). No published comparison of "budget B" vs "budget B/2 plus structured second look" in medicine was found. K26 contested.
- Gap 10 (independent replication): partly. Independent McMaster/Toronto work supports a structured verification pass in ECG reading (d19, d20) and fails the plain slow-down instruction (d27). The delayed-learning effect still has only Mamede/Schmidt-network replications (d25 includes co-authors). K28 added.
- Gap 5 (bottom-up order): one independent order test (late vs early alternatives, d21) shows no order difference for presence of the right diagnosis; it does not test the DR claim directly. K29 single-source.

Stayed open:
- Gap 1 (structured for/against/missing/alternative vs plain second pass at equal tokens, hard vs easy items): no study found. Closest are d14 (wording matters), d12 (framing as external) and d03/d05 (equal-budget losses of refinement). Highest-priority test for our agent.
- Gap 4 (real-practice trial with patient outcomes): none found; reviews confirm vignette and training-level evidence only (d22, d23). K30.
- Gap 7 (retrieved look-alike contrast knowledge vs process prompt for LLMs): no LLM study found; the human side still says knowledge, not process, resists anchoring (d24, same lab).

Corrections to earlier text: d19 and d20 are independent of the Mamede network; d25 and d24 are not. K17 status moved to contested. Two things not rechecked: the exact per-step curves in m1 Figure 3 (d08) and whether the Smit 2024 medical runs of Table 2 used GPT-3.5 throughout (taken from the paper's GPT-3.5 main setup).
