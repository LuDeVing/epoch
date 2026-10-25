# Critique: mental models theory (cross-check)

Cross-checker pass. Inputs: evidence_a.jsonl (27 lines), evidence_b.jsonl (29 lines). evidence_c.jsonl did not exist when this pass ran, so nothing from a third agent was checked. Claims are in claims.jsonl (18 claims: 5 established, 8 single-source, 5 contested, 0 refuted).

## 1. Numbers re-opened (full text read in this session)

| # | Line | Source re-read | Result |
|---|---|---|---|
| 1 | a04, b01 | Johnson-Laird & Savary 1999 (PDF) | Confirmed: 16 Princeton students, 100% predicted invalid conclusions on illusions, confidence 4.4 vs 4.3, every participant better on controls (1 in 65,000). |
| 2 | b03 | same, Exp 2 | Confirmed: 15 of 20 gave the illusory answer, sign test under 1 in 30,000. |
| 3 | b04 | same, Exp 3 | N=40 confirmed, 33 drew an illusory conclusion and were right on the control, 7 ties (1 in 8 billion). Per-illusion percentages (85, 63, 68, 98) not re-checked in the table. |
| 4 | a07, b09, b10 | Yang & Johnson-Laird 2000 antidote (PDF) | Confirmed: one-case 33% to 65% illusions, 93% to 79% controls (z=3.27, 2.31); two-case 39% to 71% illusions, 87% to 72% controls (z=3.72); illusion-control difference z=0.44. Note: b10 says controls z=1.99, p<.05; the text shows a reliable decline but I read z only for Exp 1 (2.31). Minor. |
| 5 | a15, b15, a16 | Khemlani & Johnson-Laird 2012 meta-analysis (PDF) | Confirmed: hits 95%, correct rejections 74%, verbal models 63%/90%/84% with I2=52%, models vs heuristics 76% vs 66%, W=.86 and .64, entropy-accuracy r=-.52, hardest valid 1%, easiest valid 90%, easiest invalid 76%. Correction: W=.45 is for the rank order of entropy, as a16 says. The publication-bias regression (z=2.03) was for the mental-models theory's hits only, as a15 implies. Sample sizes 20x5 + 56 = 156 confirmed from Table 5. |
| 6 | a26, b25 | Eisape et al. 2024 (PDF, arXiv v-current) | Confirmed: 139 human participants (Ragni 2019), about 50% human accuracy, about 75% best LM, 1296 settings with 923 finished, PC1 77% of variance, control correlation 0.6 with SYSTM2. Temperature 0.5 confirmed. |
| 7 | b18 | Ragni et al. 2018 retest (PDF) | Confirmed: 58% to 68%, 19 of 20, 27.5 changes, 95.9% same polarity, fits 60% and 65%. |
| 8 | b19 | Dames, Klauer & Ragni 2021 | Only the abstract was reachable (OpenAlex): N=100, gains in session 1 only, valid items only, bias against "no valid conclusion". The finer numbers (50.1%, 2.6%, OR 1.96) were NOT re-checked: the publisher page returned a bot challenge. |
| 9 | a20 | Byrne 1989 (PDF) | Table confirmed: modus ponens 96 / 96 / 38 (simple / alternative / additional), modus tollens 92 / 96 / 33, denial of antecedent 46 / 4 / 63, affirmation of consequent 71 / 13 / 54. N=24 from Trinity College Dublin confirmed. The "8 per group" detail is plausible but I did not read it directly. |
| 10 | a21, b27 | Ragni & Johnson-Laird 2018 modality (PDF) | Exp 1 N=53, 80% vs 56%, z=6.1, r2 .99 vs .01, Yes 84%, No 81%: confirmed. CORRECTION: Exp 2 had N=51 (not 50), 83% vs 50%, r2 .98 vs .05. The "89% yes, 76% no" in a21 belong to Experiment 3 (N=50), not Exp 2. |
| 11 | b28 | Johnson-Laird 2024 (PDF) | The quote is accurate: 95% vs 63%, 15 s vs 24 s, 2 minutes. It is a recalled result of Victoria Bell's study, so still second-hand. |
| 12 | a24 | Khemlani, Lotstein & Johnson-Laird 2014 (PDF) | Confirmed: 92% vs 51%, z=3.21, Cliff's delta .56, b=3.31, SE .42, search .58, 9.5% qualified responses. |

Sources that could not be re-opened: Johnson-Laird & Savary 1996 (web archive returned a bot challenge, so a02 and a03 numbers are unchecked this pass; a01 and a02 were marked opened by agent A), Dames 2021 full text, Bertolazzi et al. 2024 (a27, b24 not re-opened; the human baseline 44.63/40.97 comes from the meta-analysis and was not rechecked), Khemlani & Johnson-Laird 2008/2009 (a08, b06, b07: not re-opened).

## 2. Contradictions and tensions between lines

- a08 vs b06/b07 (same paper, differently cited). a08 puts the instructed Exp 2 illusion accuracy at 50/38 in block 1 and "47%" overall; b06 gives 37% for illusions in Exp 2; b07 gives 38/38/63/56 vs 17/21/21/58 by problem type. These are not clearly the same quantities. Do not quote a single "instructed accuracy" number for this paper until re-read.
- Year labelling: the disjunctive illusions paper is 2008 in a08/a09 and 2009 in b06/b07 (the URL is 2008). Same paper.
- a21 vs b27: same paper, a21 mislabels experiments (fixed above).
- b18 vs b19: the small retest finds a gain on both valid and no-valid-conclusion items and attributes it to more counterexample search. The N=100 retest finds a smaller gain on valid items only and attributes it to response bias. They partly contradict (claim A01.01-K10: contested).
- a15 vs b15 describe the same meta-analysis, so they are one source, not two.
- Counting "independent sources": most lines trace to Johnson-Laird, Khemlani, Ragni or their students. Only Eisape et al., Bertolazzi et al., Singmann et al., Dames et al., Oberauer and Newstead are outside that network, and several of those were not opened.

## 3. Weak spots

- Illusions: the best-attested effect has no independent replication or meta-analysis in the set. b12 says no study failed, which is the authors' claim (b12 limits). The only outside number is a search snippet (b14: 80-85% acceptance), not opened.
- Illusions for LLMs: no line tests an LLM on illusory inferences. Everything about scaffold design (A01.01-K03, A01.01-K04) is extrapolated from humans.
- Instruction fixes lower control accuracy (93 to 79, 87 to 72). Any operator must be gated by a signal, otherwise it costs accuracy where not needed.
- mReasoner fits are in-sample with free parameters (a23, b17) and by the theory's authors. Model-size and search values vary by study, and group differences are interpreted without a test.
- Illusion "correct" answer is often "nothing follows" because the premises are self-contradictory (b04). Few participants noticed. This overlaps with the NVC difficulty (A01.01-K06) and may be partly the same effect.
- All human studies are student or small online samples, N 16 to 56 per experiment except the meta-analyses.
- b28 (95% vs 63%) is the cheapest looking fix and the least verified.

## 4. Seen only in snippets, abstracts or second-hand

- b14 (Koralus & Mascarenhas): fetch empty, snippet numbers only.
- b22 (Oberauer 2006): abstract in a search result.
- b29 (Newstead et al.): search summary, no numbers. Claim A01.01-K18 leans on it only for the mechanism.
- b11 (Goldvarg & Johnson-Laird 2000, 57%): second-hand via Yang & Johnson-Laird.
- b05 (Johnson-Laird & Goldvarg 1997): cited, not opened.
- a14 (Girotto & Gonzalez 53% vs 8%): cited from the naive probability paper.
- b19 details beyond the abstract (this pass).
- b28 original (Bell).

## GAPS

1. Do current frontier LLMs fall for illusory inferences (propositional, quantified, embedded disjunction) at human rates, and does the confidence/self-consistency signal fail to flag them? This decides whether an enumeration operator is needed at all (G1, G10).
2. Does a code-driven "premise A true and B false, then B true and A false" case table, with the model filling each row, beat plain and beat a prose warning at equal tokens on LLM illusion items, and what does it cost on controls (the human cost was 93 to 79 and 87 to 72)?
3. Is the "list the possibilities" model method (95% vs 63%, 15 s vs 24 s) real? Find Bell's original data (Johnson-Laird 2006 book, other reports) and any independent replication.
4. Is there any independent-lab replication of illusory inferences with real effect sizes (Rips, Tabossi, Koralus, Mascarenhas, Walsh)? How large are the effects with careful controls for pragmatics and for item order?
5. For LLMs, does accuracy fall with model count, and does an explicit "no valid conclusion" candidate plus counterexample search lift NVC accuracy without raising false rejections? (Test on 64 syllogisms with frontier models; the evidence is only PaLM 2 and open models up to 70B.)
6. What triggers counterexample search for a model? Is search on a code-detected signal (answer disagreement, unbelievable answer, multiple-model item) better than always-on at equal tokens, as the mReasoner search parameter suggests (.4 vs .8, .58)?
7. Is the practice gain in syllogisms a bias shift (Dames 2021) or deeper checking (Ragni 2018)? Re-read Dames 2021 in full and test whether in-context history shifts only the NVC rate in an LLM.
8. How much does content or belief bias affect current LLMs once forms are fixed, and does a counterexample search remove it? (Bertolazzi et al. used 2024 open models; newer models and reasoning models untested.)
9. Do the second-hand numbers (b11 57%, a14 53% vs 8%, a10 summary percentages) hold in their original papers? Re-open Goldvarg & Johnson-Laird 2000 and Girotto & Gonzalez.
10. Does code-expanded counting of models (full state table) fix LLM probability errors of the kind seen in naive-probability and unique-event studies, beyond what sum-to-one normalisation already gives?

## Gap search results (evidence_d.jsonl, d01 to d21; claims A01.01-K01 to A01.01-K04, A01.01-K06, A01.01-K07, A01.01-K09, A01.01-K10, A01.01-K15, A01.01-K18 updated; A01.01-K19 to A01.01-K24 added)

Search note: WebSearch hit its session quota after about 8 calls. The rest was done by direct downloads from modeltheory.org, arXiv and Springer, and by arXiv and OpenAlex API queries. An arXiv title/abstract query for "illusory inferences" returned one paper (Koralus & Wang-Mascianica 2023). OpenAlex 2023+ searches for illusions in LLMs, mReasoner with LLMs, and counterexample search for LLMs found nothing that tests those directly. Absence in these indexes is weak evidence, not proof.

Status by gap:

1. LLMs on illusions. PARTLY CLOSED. Two LLM studies exist, both from the Oxford erotetic-theory group (d01: 38 models, 383 fallacy items, mean correct 40.6%, no link to capability, wrong answers increasingly the predicted fallacy; d02: GPT-4 fallacy production 34%). They show LLMs fall for disjunction fallacies. Still open: a human-rate comparison on the same items, matched controls, and any confidence or self-consistency test. So the enumeration operator is justified as a test, not as an established fix (A01.01-K19).
2. Table vs plain vs prose warning at equal tokens. OPEN. The only prose-vs-control LLM data (d02) shows no gain for GPT-4 (8/19 vs 7/19). Human control cost confirmed in the original (d05: 93 to 79 and 87 to 72). The code-built table has never been tested on an LLM.
3. Model method 95% vs 63%. OPEN, and weaker than before. The source is an unpublished thesis; Johnson-Laird's own two reports disagree (65% vs 63%, 25 s vs 24 s) (d11). A01.01-K15 is now "contested".
4. Independent replication of illusions. PARTLY CLOSED. Espino, Orenes & Moreno-Rios 2024 (d08; N=80, Spanish) replicates the conditional illusion at large size: correct 83% on controls vs 6% on illusions, r=.87, confidence equal. They are only partly independent. Rips, Tabossi, Mascarenhas & Koralus (human data), Walsh originals were not obtained in full. The Mascarenhas & Koralus human figure (about 60% endorse the illusory "Mary has an ace") is second-hand through d01. Pragmatic and item-order controls are still not quantified. Boundary conditions found: framing (physical vs logical disjunction 84% vs 19%), response format (63% vs 19%), co-reference (d06, d07, d09; A01.01-K20).
5. Frontier LLMs on the 64 syllogisms, model count, NVC plus search. OPEN. No frontier or reasoning model study with a model-count curve was found. 2025 work (d14) judges validity, not conclusion generation. d15 warns that the answer key must fix existential import (A01.01-K23).
6. Trigger for counterexample search. OPEN. The mReasoner fit (d18) is in-sample and gives no trigger rule; individual parameters show no concordance (W=.28, p=.33). The trigger-by-code-signal idea remains a hypothesis.
7. Practice gain: bias shift or deeper checking. PARTLY CLOSED for humans. Full text of Dames 2021 read (d10): gains on valid items only (valid 55.5% to 60.3%, invalid 46.1% to 47.2%), with fewer NVC answers, and the authors themselves offer two explanations without separating them. The LLM test (history shifts only the NVC rate) is not in the literature I could find.
8. Content and belief effects in current LLMs. PARTLY CLOSED. 2024 open models show the effect (d13) and 14 models in 2025 show a mean +10.81 pp belief bias (d14), but top models under 2 pp. Whether counterexample search removes it has no test. Reasoning-tuned models were not separately tested for belief bias in anything I opened.
9. Second-hand figures. PARTLY CLOSED. Goldvarg & Johnson-Laird 57% is a table cell (possibility illusions after the check; overall 71% vs 30% for no help) (d04). The same-paper conflict for Khemlani & Johnson-Laird 2008/2009 is resolved toward the 2009 text (d07: controls 95%, illusions 19%; instructed gap 34 points vs 79). Girotto & Gonzalez 53% vs 8% could not be opened (d21).
10. Code-expanded counting for LLM probability errors. OPEN. LLM probability judgments are incoherent (d20) and the human JPD violation rate is 56% (d19), but nobody tested a counting table or compared it with sum-to-one normalisation (A01.01-K24).

Corrections to earlier lines found on re-reading:
- b11 "57% after the remedial check" is the possibility-illusion cell only; the overall figure is 71%.
- b28 / A01.01-K15 numbers differ between Johnson-Laird's 2012 and 2024 texts.
- a02/a03 (Johnson-Laird & Savary 1996) still not re-opened; a08/b06/b07 only reconciled for the 2009 journal text.

Status changes in claims.jsonl: A01.01-K01 and A01.01-K02 now "established" (human illusion and confidence results hold in a second lab, partly independent); A01.01-K15 "contested"; A01.01-K19 to A01.01-K24 new. A01.01-K05 to A01.01-K08, A01.01-K11 to A01.01-K14, A01.01-K16, A01.01-K17 unchanged.

What the gap search says about the schema: the enumeration operator (O3) and G10 (do not trust confidence on this class) are supported for humans and plausibly for LLMs, but the schema should keep the table as a gated, tested operator. The cost on controls (about 15 points in humans) and the lack of any LLM table test are the reasons.

## Addendum: cross-check of evidence_c.jsonl (32 lines, c01 to c32)

The first pass above did not see evidence_c. This addendum covers it. Claims A01.01-K04, A01.01-K06, A01.01-K07, A01.01-K19, A01.01-K22 were updated and A01.01-K25 to A01.01-K30 added (30 claims now).

Numbers re-opened from full text (arXiv PDFs, pdftotext, this session):
- c07/c08 Koralus & Wang-Masciantica 2023: confirmed 59/77/75% ETR-predicted, 18/33/34% human-like fallacies, 4/17 vs 14/17 (p=.0045) for GPT-3.5, 8/19 vs 7/19 for GPT-4. Note: c07/c08 and d02 are the SAME paper. They count as one source.
- c01 Eisape 2024: same paper as a26/b25 (already confirmed in the first pass). One source, not two.
- c06 Bertolazzi 2024: confirmed 58.89% valid, human 44.63%, correlation 0.80, atmosphere theory 92.31 / 82.97 / 62.79, SFT contradictory answers 0.31%.
- c09 Rulebreakers: confirmed +24.13 (gemma-2-27b), range 31.27 to 69.12, 0.0022 minimum.
- c19/c20 Sphere NN: confirmed 47.27 to 56.64 (121 to 145 of 256), 77.39 to 80.01, 51.67 and 95.83/89.17 chain figures, irrationality 48.05 to 40.23. Caveat: the gpt-3.5 "80% best at 3 terms" in c19 not separately checked.
- c22 CounterLogic: confirmed 11 LLMs, 14% drop, gap to 7%, +4% overall.
- c12 VoT: confirmed 23.5, 87.1 vs 57.4, 52.5 vs 49.5 (N=200). Correction to c12: the text says "23.5%", not clearly points; and "versus CoT only p < 0.16" is not a result I could place in the text. 87.1/57.4 is the overall tracking rate in the tiling task.
- c02 Holliday: the 89.50 maximum and a +21.50 gain figure appear in tables, but I could not tie "45% minimum" to a table cell in the extracted text (layout scrambled). Treat range as approximate.

Not re-opened: c03, c04 (not read by agent C), c05, c10, c11, c13 beyond abstract, c14, c15, c16, c17, c18, c21, c23 table, c25, c26, c27 (abstract only), c28 to c32 (abstract or no extraction).

New tensions:
- c08 vs a05/b02 (A01.01-K03, A01.01-K04): a procedural prompt can block a fallacy for GPT-3.5 (14/17 vs 4/17) but not GPT-4 (7/19 vs 8/19). The retest used only previously failed items, so regression to the mean is possible. A01.01-K04 downgraded to contested.
- c09 vs the assumption that explicit logic structure helps: chain of thought and symbolic translation raised ordinary accuracy but lowered rulebreaker accuracy. A truth-table operator might do the same (over-apply the formal rule). Needs a test on both item types.
- c12 vs c10: visualisation helps on some spatial tasks and not on ring navigation or on added views; no consistent rule for when.
- Counting independent sources: c01=a26=b25; c07=c08=d02. Several c lines are not about mental models theory itself (c13, c18, c21, c27 use "mental model" for world knowledge or are generic); they were used only for A01.01-K27 and not as support for the theory.

Additional weak spots: c-lines on LLMs are mostly 2023 to 2024 models; Koralus tested one sample per item through a chat interface; most new LLM numbers come from papers that do not use Johnson-Laird's illusion items.

## GAPS (final, most decision-relevant first)

1. Do current frontier and reasoning LLMs fall for Johnson-Laird's own illusory inferences (propositional, quantified, embedded disjunction) at human rates, with matched controls and a confidence or self-consistency test? Only 2023 chat models and a 38-model disjunction set were tested (G1, G10).
2. Does a code-built possibility table (premise A true and B false, then the reverse), filled in by the model, beat plain and beat a prose warning at equal tokens on illusion items, and what does it cost on controls (human cost 93 to 79 and 87 to 72)? Include rulebreaker and modal-fallacy items (A01.01-K25, A01.01-K26) since formal structure can hurt there.
3. What triggers counterexample search for a model? Is search on a code-detected signal (answer disagreement, premises conflict with knowledge, multiple-model item) better than always-on at equal tokens?
4. Do frontier and reasoning LLMs accept "nothing follows" when it is right, and does an explicit NVC option plus counterexample search lift NVC accuracy without raising false rejections (64 syllogisms, fixed existential-import key)?
5. Is the "list the possibilities" model method (95% vs 63%, 15 s vs 24 s) real? The source is an unpublished thesis recalled by Johnson-Laird, with his own two reports disagreeing. Find the original data or an independent replication.
6. Is there an independent-lab replication of illusions with careful pragmatic and item-order controls (Rips, Tabossi, Mascarenhas, Koralus, Walsh)? The one replication found (Espino et al. 2024, N=80) is only partly independent.
7. Is the practice gain a bias shift (Dames 2021: valid items only, fewer NVC answers) or deeper checking (Ragni 2018)? Does in-context history shift only the NVC rate in an LLM?
8. Does belief or content bias remain in frontier and reasoning models once forms are fixed (14 models in 2025 +10.81 pp mean, top models under 2 pp), and does a counterexample step remove it better than flag-and-reason (14% to 7%)?
9. Does a code-expanded counting table fix LLM probability incoherence beyond sum-to-one normalisation?
10. Do the 2023-24 premise-order drops (over 30%) and Rulebreaker failures persist for current frontier models, and does a code-reordered or code-checked premise restatement fix them at equal tokens?

## Gap search results (evidence_d.jsonl, d01 to d28; claims now 33)

New this pass: d22 to d28. d01 to d21 came from an earlier interrupted pass and were kept. Claims A01.01-K31 to A01.01-K33 added; A01.01-K01, A01.01-K09, A01.01-K18, A01.01-K19, A01.01-K27 got extra evidence ids and short notes. No status flipped. A01.01-K01 independent sources raised to 3.

Closed or half closed:
- Gap 5 (model method 95% vs 63%): closed as "unverifiable". d11 shows the source is an unpublished 1999 thesis and Johnson-Laird's two reports give different numbers (65 to 95%, 25 to 15 s; 95 vs 63%, 15 vs 24 s). No independent replication exists. A01.01-K15 stays contested. Do not quote 95%.
- Gap 7 (practice gain): half closed. Dames 2021 (d10) says the gain is inside session 1 and on valid items only, which favours a response-bias shift over deeper checking. No LLM test of in-context history was found.
- Gap 6 (independent illusion replication): half closed. Sable-Meyer & Mascarenhas 2021 (d24, N=64 and 70 analysed, controls 87/26 and 90/20) replicate the disjunction illusion in an independent lab, and show the trigger is knowledge links, not only word overlap. Ghasemi 2023 (d25) gives a matching-heuristic rival for related effects. Espino 2024 (d08) is still the only conditional-illusion replication. Still missing: item-order and pragmatics controls, quantified and modal illusions outside the Johnson-Laird lab.
- Gap 8 (belief bias): half closed. d14 (14 models, top under 2 points) and d22 (ten open models, content effect falls with chain of thought, most above 89% accuracy) say belief bias shrinks in strong models. Counterexample step vs flag-and-reason is not tested.
- Gap 3 (what triggers search): half closed. d23 shows disagreement-triggered verification beats always-on at lower tokens on math and commonsense tasks (82.1% at 0.592K vs 80.0% at 1.458K). It misses uniform errors, so it will not catch illusions. The code-signal trigger is untested. d18 (mReasoner) has the search probability as a free fit parameter, not a trigger test.
- Gap 9 (counting table): half closed. d19 and d20 confirm incoherence in humans and in 2023-24 LLMs. d21: the Girotto & Gonzalez 53% vs 8% figure stays second-hand. No counting-table test.

Still open (no outside evidence found, d28 is the search log):
- Gap 1: no test of current frontier or reasoning models on the classic illusions with controls and a confidence check. Only 2023 chat models (d02) and the 38-model disjunction set (d01, up to 91.7% correct for the best, so top models may now beat humans on that type).
- Gap 2: no test of a code-built possibility table. Human cost on controls (93 to 79, 87 to 72, d05) is the only number. Rulebreaker and modal sets (A01.01-K25, A01.01-K26) are tested only plain or with chain of thought.
- Gap 4: d12, d13, d14 show models rarely say "nothing follows" and fine-tuning fixes it where in-context examples do not. No frontier test of an explicit NVC option with counterexample search. A01.01-K23 (existential-import key) must be fixed before scoring.
- Gap 10: d26 is training-based on small models; d27 is moral reasoning. No premise-order or rulebreaker test on current frontier models; no code-reordering test.

What this means for the schema: the evidence for the possibility-table operator (O3) and for G10 is still from humans and 2023-24 models. The first harness tests, in order: (1) illusion items and controls on the current model, plain vs warning vs code table, all at equal tokens, with a control-cost readout; (2) NVC option with code counterexample search on the 64 syllogisms; (3) triggered vs always-on search with a code item signal. Keep the table gated until test 1 reports a control cost.

Limits of this pass: some PDFs were read only in part (d25 Experiments 3 and 4, d27 beyond the abstract and setup). arXiv keyword search was poor, so absence of a paper is not proof.
