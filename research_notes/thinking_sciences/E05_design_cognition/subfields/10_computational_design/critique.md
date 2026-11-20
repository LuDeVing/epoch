# Critique: E05.10 Computational design (FBS)

## Re-checked numbers (local text of sources re-read this session)
Confirmed: Ma et al. 2023 (cosine 0.804, 0.746, hull 0.294, mean 0.748); Sahadevan 2024 (experts 54/93/87, ChatGPT about 78% then 100%); Song 2016 (15.13/15.22/22.38, d 2.55); Luo 2021 (level means .12/.14/.06 and .46/.48/.64, partial eta 0.336, agreement 80%, kappa 0.78); Ralph 2013 (1384 of 4410, 31%, 96.6%); Fujiu 2025 (165 nodes, 1176 records, recall@8 0.625); Elhambakhsh 2025 (681 samples; pretrained 0.04/0.27/0.20; 0.89 test).

Corrections and notes:
- Elhambakhsh: the first accuracy column in the table is TRAIN accuracy (0.93 at 10%). The 0.89 is a test figure. Test accuracy falls with more training data, unexplained in the paper; treat as a fine-tuning artefact. c06 rounds 0.89 to "about 90%".
- Sahadevan: the 100% ChatGPT figure is on the items used to tune the rules, so not held out. Only 71% (n=31; per-class n 7-13) is held out.
- Not re-opened: Wells 2016 p-values, Williams 2012 ranges, Bruggeman 2025, Ege 2025, Massoudi and Fuge 2025, Tanaka 2026 (taken from the evidence files as written).

## Contradictions and weak spots
- Expertise: Song 2016 and Luo 2021 find large differences; Wells 2016 finds none (all p>0.05). Tasks, age groups and measures differ (decomposition and system level vs raw FBS processes), so it may not be a true conflict. Status contested.
- Pahl-Beitz as predictive model fits only partly. The a12-a14 simulations are an unreviewed draft.
- Domain independence (a13): only function shared a slope, F(2,5)=5.2, p=0.06, not significant.
- Gero 1990 (a01) was never opened. No source was opened for Maher (case-based design) or Dorst and Cross. The focus named Maher; this is a real hole.
- All LLM-on-FBS studies are single, small-n, and none tests FBS as a prompt scaffold against a plain prompt at equal tokens. Tanaka 2026 is closest; its judge validity is poor (ICC -0.52 on one problem).
- Gero and Milovanovic (2020) reviews the authors' own group; citation counts are not validity evidence.
- Abstract-only or secondary: a01, a23, a26, a27, c21, c24, c25, c26, b17.

## GAPS
1. Does labelling agent reasoning with F/Be/Bs/S states (vs plain chain of thought) improve quality at equal tokens? No study found.
2. Is there held-out multi-coder reliability (kappa) for LLM FBS coding of design protocols, beyond Sahadevan's n=31?
3. What do Gero 1990 and Gero and Kannengiesser 2004 (situated FBS) report numerically; does any experiment test the eight processes causally?
4. Maher and Poon (1996) co-evolution and Maher's case-based design: numbers and replications.
5. Does the expert decomposition-recomposition advantage transfer to LLMs when forced by prompt?
6. Do FBS evaluation steps (expected vs derived behaviour) reduce errors in LLM design loops?
7. Do LLM design outputs show narrow variance across seeds (Bruggeman), and does an FBS reformulation step restore spread?
8. Is Elhambakhsh's falling test accuracy with more data reproduced elsewhere?
9. What are the results of Kannengiesser and Gero 2019 hypotheses H1/H2 (fast and slow design thinking)? Only a snippet was seen.

## Gap search results
Evidence is in evidence_d.jsonl (d01-d18). Search was limited: arXiv, Semantic Scholar and OpenAlex APIs returned rate-limit errors, the web search budget ran out after 6 calls, and par.nsf.gov, AAAI and Springer pages could not be fetched. Absence of a study below means "not found", not "does not exist".

1. FBS labels vs plain chain of thought at equal tokens: OPEN. Nothing found (d14). Nearest is Chen et al. 2024 (d01-d03), now read in full: FBS three-stage prompt chain 3.31 vs free ChatGPT prompting 2.90 vs no-AI 2.63 (80 people, 20 per group, 3 raters, kappa 0.66). Human picks words at each hop, no token control, and the t-tests look inflated (t 6.64 implies about 60 scores per group; my calculation). Professionals gained 0.02 over free prompting. Claims K17, K18.
2. Held-out multi-coder kappa for LLM FBS coding: OPEN for design. Analogue only (d09, d10, d16): GPT-4 kappa 0.68 per code with rationale, 0.59 without, 111 gold passages; weak on rare codes. Claim K23.
3. Gero 1990 and Gero and Kannengiesser 2004 numbers; causal test of the eight processes: OPEN. Sources blocked (d17). Indirect finding only: the processes are used as coding categories, not manipulated. Kannengiesser and Gero 2019 (Design Science) was read in full and is theory only.
4. Maher and Poon 1996 and Maher's case-based design: PARTLY CLOSED. The model is now described from a read secondary source (d07): two populations, fitness check, refocus. Gero, Kannengiesser and Crilly 2022 (d04-d06) give the first FBS-measured version: one 1-hour session, switch counts overstate co-evolution by about 50% and 100%. No original numbers, no replications, nothing for case-based design (d18). Claim K19.
5. Decomposition-recomposition forced on LLMs: OPEN (d15).
6. FBS evaluation step reducing LLM design errors: OPEN (d13, d15). The FMEA review asserts it with no measurement. Only measured analogue is Ma 2024's critique pass raising diversity (d11).
7. Narrow spread across seeds and FBS reformulation restoring it: OPEN, with detail. Ma 2024 (d11): no monotone effect of temperature or top-P; human recall by topic 0.25-0.80 in the embedding classifier, LLM 1.00. Bruggeman 2025 (c18, not re-read) shows variance 0.042 vs 0.102. No FBS reformulation test.
8. Elhambakhsh falling test accuracy reproduced elsewhere: OPEN, nothing found (d12).
9. Kannengiesser and Gero 2019 H1/H2: OPEN. The Design Science paper has no hypotheses or numbers (d08). The conference paper (Human Behavior in Design pp 89-100) holds them and could not be fetched. Claim K21 marked unverified.

New claims K17-K23 added; K01, K06, K08, K11, K14 gained evidence ids. No status of an existing claim changed.
