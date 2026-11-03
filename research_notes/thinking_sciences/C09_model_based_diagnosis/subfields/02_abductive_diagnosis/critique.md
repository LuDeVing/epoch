# Critique: C09.02 Abductive diagnosis (cross-check)

Checked 2026-11-03. Re-opened the full PDF text of 12 sources and compared the headline numbers to evidence_a/b/c.jsonl: Elenchos (2607.12733), Graph of States (2603.21250), ART (1908.05739), True Detective (2212.10114), DDx (2312.00164), rare-disease leakage audit (2610.33592), thinking effort (2609.01867), OpenRCA 2.0 (2606.27154), TempoBench (2510.27544), Kim et al. cloud RCA (2602.09937), LATS-RCA (2605.03505), Salimi et al. survey (2604.08016).

## Corrections made (or needed in the evidence files)
1. a04 (ART): the best BERT model is the Linear Chain variant at 68.9 on test; Fully Connected is 68.6. a04 said "fully connected" for 68.9. Other ART numbers confirmed (GPT-ft 63.1, majority 50.4, human 91.4, hypothesis-only 59.5, O1-only 63.5, O2-only 66.6).
2. a27 vs c19 (DDx): abstract says clinicians with LLM 51.7 and with search 44.4; the table says 51.8 and 44.5. Rounding difference in the paper itself. Top-10 59.1 vs 33.6 (p 0.04) and 36.1 unassisted confirmed.
3. a19 (Graph of States): 39.86 percent is the human-judge Match for GoS. The LLM-judge Match for GoS is 31.88. The ablation numbers (18.12 without causal graph, 12.32 without state machine) are LLM-judge, so compare them with 31.88, not 39.86. Best baseline human-judge Match is about 26.09 (Multi/FoT, $0.73/case). Error table confirmed: fabrication 22.22 vs 0, failed backtracking 52.78 vs 30.90.
4. a14 (Elenchos): the 0.90 at k=0 is null-case specificity (no fault present, model correctly says none), not fault-finding accuracy. The drop 0.90 to 0.32 to 0.15 mixes two different tasks. The honest fault-finding sequence is 0.32 (k=1), 0.15 (k=2+), 0.03 (interacting pair).
5. b21 (LATS-RCA): 91.3 percent is on one small benchmark (LO2); on 37 real production incidents it is 65.1 percent (24.1 of 37, range 62 to 70). Quote both.
6. Confirmed unchanged: Elenchos 0.65 vs 0.28 and 86.5 percent unused budget; OpenRCA 2.0 20.7/34.1/76.0/61.5/62.2/43.4; TempoBench 96.0 vs 32.1 and visibility drop 79.5 to 31.8 with at most 3.4 shift; Kim et al. 1,193 (71.2), 1,071 (63.9), 669 (39.9), 311 (18.6), best 12.5; Salimi DDXPlus 79.75/98.7 ranking and 63.0/28.1 generating, medians 79.96 vs 42.50 vs 28.8; leakage 54.3 to 40.3, g 0.94, classifiers 42.9 to 16.7, d 2.01; thinking effort r 0.552, 0.197, Fisher z 1.23 p .217; True Detective 0.38, 0.63, 0.83, human 47 percent.

## Duplicate entries (not independent sources)
- a13/a14/a15/a16 and c13/c14: one paper (Elenchos). a19/a20: one paper. b14 and c10: one paper (OpenRCA 2.0). b16/b17 and c01/c02/c03: one paper (Kim et al.). a21 and c25: one paper (HypoAgent). a23 and c16: one paper. a27 and c19: one study. b23 and c20: one paper. a25, a26, b09, b10: one survey. b11, b12, b13: one paper.
- Counts in claims.jsonl use distinct papers, not evidence lines.

## Contradictions and tensions
- Structure vs tools: explicit hypothesis state (GoS, LATS-RCA, HypoAgent) helps strongly, but richer tool sets did not (c12: free Python 85.4 vs full tools 82.8). Likely the gain comes from how hypotheses are tracked, not from more machinery.
- ReAct: c06 finds fewer hallucinations with ReAct (4 vs 12 vs 40 percent, 100 labelled predictions each), c04 finds agentic loops hurt small models. Different model sizes and tasks. Marked contested (K24).
- Procedure text: c11 says removing the five-step procedure did not hurt (and raised the score, none significant after correction), while Kim et al. say enriched protocol cut steps and pitfalls. The difference is prompt text (no help) versus enforced protocol (some help). Small effects both ways.
- Hypothesis breadth: LATS-RCA gain came from 18.9 vs 5.1 hypotheses with equal evidence (about 7.0 items), but cost rose from 41K to 156K tokens. At equal tokens the benefit is untested.

## Weak spots
- Most 2026 numbers are single-paper, single-run reports, many from arXiv preprints not peer reviewed. Several rely on LLM judges (GoS, OpenRCA 2.0 grading).
- Cloud RCA dominates the evidence. Little on non-software physical systems, which is where classic model-based diagnosis was built. The classic papers (Reiter 1987, de Kleer and Williams 1987, de Kleer-Mackworth-Reiter 1992, Console-Dupre-Torasso 1991, Bylander 1991, Peng-Reggia 1990) were not opened (a06 to a12 are from memory); only Dupre 2000, Poole 1994 and Roos were read.
- No study tests the Ab-predicate representation itself against free prose on an LLM. All LLM evidence is indirect.
- Pooled abduction vs deduction medians (b10) mix different models, methods and datasets.
- True Detective data (c18) is 2022, GPT-3.5/4 era.

## Seen only in snippets or listings
b24 (AUV recovery, 85 to 90 vs 60 to 78 top-3), b25 (PACS), b26 (A2P 47.46 vs 16.67), c08 (OpenRCA original, known via citing papers), c11 (partially), c17, c26 (clinical trial matching, up to 30 percent relative gain), c28/c29 (background knowledge). Do not cite these as verified.

## GAPS (most decision-relevant first)
1. Does forcing an explicit Ab-flag table (predicted vs observed per part) beat free-prose reasoning on an LLM at equal tokens? No direct study exists.
2. Does a forced rival-hypothesis step before stopping fix premature commitment, and what does it cost in tokens? Elenchos shows unused budget in 86.5 percent of failures, but no one tested a fix.
3. Can a hitting-set or minimal-conflict loop (code-side) rescue the multiple and interacting fault collapse (0.15 and 0.03 in Elenchos)?
4. Is the detect vs attribute gap closed by running the simulation in code (deterministic) rather than in the model? TempoBench suggests attribution copies visible guards.
5. At equal tokens, do tree/graph hypothesis methods (LATS-RCA, GoS) still beat plain best-of-N or self-consistency? Current comparisons are not token-matched.
6. Which discriminating-test (next probe) selection rule works for LLMs? Entropy-based probe choice from de Kleer and Williams (1987) was not opened and has no LLM test; Salimi lists it as an open gap.
7. Do prompt-text guardrails ever help abductive failure modes, or only enforced code checks? Needs a clean matched test.
8. Are abduction deficits stable on newest frontier models and non-software physical domains (circuits, mechanical, medical with leakage controls)? Evidence is mostly cloud RCA and 2024-2025 models.
9. Open the primary classic papers (Reiter 1987, de Kleer-Williams 1987, Console-Torasso 1991) to confirm formal claims K01-K03 in print.
10. How much of the reported gains in agentic diagnosis survives strict isolation against leakage (rare-disease audit shows leakage effect g 0.94 to 1.21 exceeded agent gain)?

## Gap search results (2026-11-03, evidence_d.jsonl d01-d17)

Limits of this pass: the shared WebSearch budget was used up and the arXiv, OpenAlex and Semantic Scholar APIs returned HTTP 429. No new papers could be discovered; work went to deeper reading of eight already-known PDFs (Elenchos, Graph of States, LATS-RCA, A2P, AUV/SPAR, How Far Can RCA Go, NeSy-CTM, PACS). Classic papers stayed behind paywalls (403).

Closed or partly closed
- Gap 4 (code-side simulation vs in-model): PARTLY CLOSED. Elenchos Simple Reflex Agent (code replay of fixed probes) scores V=1.0 at k=1 and additive sets; no LLM matched it (d01). Still open: a code simulator for interacting faults. NeSy-CTM (d12) adds a solver-verification pattern in another domain.
- Gap 7 (prompt text vs enforced checks): PARTLY CLOSED. Rules in prompt text did not rescue interacting faults (d02). Precomputed evidence plus knowledge rules gave 14.10 to 35.90; the procedure text did not help (d11). Still no matched test of enforced code checks vs the same rule as text.
- Gap 8 (physical domains, newer models): PARTLY CLOSED. AUV study (d09, d10, d16) shows top-3 85-90 percent vs rank-one 43-75 for gpt-5.5, weak local models far lower, and diagnosis decoupled from action. Detection-attribution gap holds for all 13 Elenchos models (d15). Still none on circuits or leakage-controlled medical sets.
- Gap 5 (token-matched tree vs best-of-N): NARROWED, NOT CLOSED. LATS-RCA used 2.1x to 3.8x the tokens and had no sampling baseline (d06); candidate breadth is its largest ablation (-7.0, d05); GoS beat larger topologies at lower cost (d07); PACS equal-sample comparison is in another domain (d13). K29 marked contested.
- Gap 2 (forced rival step): NOT CLOSED. Evidence is indirect: unused budget in 86.5 percent of failures (d04), breadth ablation (d05), AUV model that kept competing hypotheses did best (d10), more reasoning effort did not help (d03). No study forces a rival step and measures.

Still open
- Gap 1 (Ab-flag table vs prose): nothing found. A2P (d08) is the nearest: a three-step abduce, act, predict scaffold gave 2.4-2.9x step accuracy, with the predict step worth 7 to 12 points, but on log attribution and from an AI-written paper.
- Gap 3 (hitting-set loop for multiple faults): nothing found.
- Gap 6 (probe selection rule, entropy): nothing found; Elenchos prompt only says 'never repeat an uninformative probe' and 'discriminating probe' (d02).
- Gap 9 (classic papers in print): only Crossref metadata read (d14); K01-K03 remain secondary-source.
- Gap 10 (leakage-isolated gains): not re-examined beyond the earlier audit.

Corrections to a note above: Graph of States row labels. In the GoS table the first row (Match 31.88 LLM judge, 39.86 human judge) is GoS itself, not Single/CoT; baselines are all below 27 on human judge (d07).

Claims changed: K07, K08, K10, K11, K13, K25, K04 got extra evidence ids; new claims K26-K32 added (K29 contested, others single-source).
