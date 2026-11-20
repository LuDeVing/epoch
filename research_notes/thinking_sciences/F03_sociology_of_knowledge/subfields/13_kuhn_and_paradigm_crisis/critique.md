# Critique: Kuhn and paradigm crisis (F03.13)

Cross-check done 2026-11-19. Sources re-opened this pass: arXiv PDFs of Smith 2026 (2608.16951), Huang 2024 (2310.01798), Wang 2025 (2501.18585), Jhaveri 2026 (2604.02485), Bertolazzi 2026 (2606.04751), Alderete 2026 (2604.20039); the Bruner and Postman page (psychclassics); Chu and Evans (PMC8522281); the Science News page for c14. Abstract pages for 2610.37649 and 2609.01526 exist with matching titles.

## Corrections and confirmations (top 10 numbers)
1. Bruner and Postman (a08, a10): 28 ms vs 114 ms, t=3.76, 100% of normal cards by 350 ms, 89.7% of incongruous at 1000 ms, thresholds 360 / 420 / 84 ms. Confirmed. Note the 230 ms figure (one trick card) was not re-seen on the page; the other values were.
2. Smith 2026 (a26): 63 Kuhn runs, 33.5M tokens, 531K per run, 229.0M total, 2,151 runs, 49 runs with no accepted improvement, 0.664 stall. Confirmed. Added context: the text says the Phase 1 to Phase 2 gap "was not algorithmic" but infrastructure, and the Kuhn side-agents are listed as step 5 of five changes made together. No arm isolates the Kuhn agent. The paper's own note calls the structure non-load-bearing.
3. Huang 2024 (b01, b02): oracle GPT-3.5 75.9 to 84.3 (GSM8K), 75.8 to 89.7 (CSQA), 26.0 to 29.0 (HotpotQA); intrinsic GSM8K 74.7 after round 2; confirmed. Table text is garbled in extraction, so the GPT-4 rows were matched by position only.
4. Wang 2025 (b10, b11): 225% more tokens, 418% more switches, QwQ AIME24 38.3 to 44.1 (the table lists 44.1 for QwQ + TIP), R1-Distill 61.4 to 64.1. Confirmed.
5. Jhaveri 2026 (c01): 6% to 78% success and 42% to 56% prompt gain are in the abstract and intro. Confirmed. Per-model cells (0.21, 0.41, 0.61) not re-read.
6. FalsifyBench (c05, c25): 75% and 68% success, rho -0.779 p=0.003, +27.0 pp partial overlap, 97.6% surface features. Confirmed.
7. Alderete 2026 (c13): 1,085 trials, 73.3% (22/30), 93.9% (31/33), 95.3% (41/43), exactly-N 28.0% (14/50) vs 6.0% (3/50). Confirmed. Correction: the 95.3% vs 93.9% gain is not significant, and the 73.3% vs 93.9% comparison has small counts (30 and 33). The monitor's clear effect is on premature submission, not accuracy. Evidence line c13 should not be read as "the trigger improves accuracy".
8. Chu and Evans (b13, b14): 90,637,277 papers, 241 subjects, 0.25 to 0.74 confirmed. Correction: 0.25 to 0.74 is a model-predicted Spearman value, and the 8.6% / 11.9% / 16.7% top-1% shares are one example field (Electrical and Electronic Engineering), not an all-field figure.
9. Rios-Garcia (c14): 619 tasks, 68%, 53%, 26% confirmed, but only from a Science News article (the arXiv paper was not opened). Treat as a secondary report. The article describes materials and lab-equipment agents; the "chemistry" label in c14 is unchecked.
10. Chinn and Brewer (a14 to a16): the eScholarship PDF returned empty this pass, so the numbers (.97 vs .72, 6 of 10 vs 4 of 32, r=-.46) were NOT re-verified. They remain as the earlier agent read them. Dunbar's PDF link also failed (returned HTML); a19 (23 vs 176 interactions) not re-verified. Ecker replication (b18) page returned only the shell; not re-verified.

## Contradictions between sources
- Kuhn (and a07) say crisis ends when a rival is available. Chinn and Brewer (a14) found no effect of an available alternative on belief change (F<1, N=64). One small null study against a theory; do not treat as refutation.
- Dunbar (a19) shows scientists attend to surprise; Chinn and Brewer and Bruner and Postman show people discount it. Reconciled partly by a20: it depends on timing and whether the surprise hits a core or auxiliary assumption. Lab setting and student setting differ.
- Wang (b10/b11) says models switch too much; c15 and c14 say agents rarely switch on anomalies. Not a contradiction: they differ in what triggers the switch (internal drift vs external evidence), but it shows a switch trigger must be tied to evidence, not to token position.
- Smith (a26) uses a Kuhn trigger and the abstract frames it as a success, while the body says it was non-load-bearing. Cite the body.

## Weak spots
- No source tests "switch frame after n independent failures" with a measured threshold. The nearest are a26 (unisolated), c13 (monitor, synthetic task), and c19 (illustrative numbers).
- Kuhn 1962 was never opened (a01 to a07 are SEP and Wikipedia; b24, c21 from memory). All claims about what Kuhn said are secondary.
- Horner and Tung 2011 replication of Bruner and Postman (a11) was not read.
- Many 2026 LLM papers are single-author or recent preprints with no replication; model names in c15 are as printed and unchecked.
- Independence is often overstated: several "sources" share one paper (c01 to c04 are all Jhaveri).
- Several theory-modelling lines (a23, a24, c22 to c24) are from memory or Wikipedia.
- Seen only in snippets: a11, a24, b20, b21, b23, b24, b25, c21 to c24.

## GAPS
1. Does a frame-switch trigger at plateau (fresh context, no history) beat plain best-of-N at equal tokens when isolated in one arm? (Smith 2026 did not isolate it.)
2. What failure count N (1, 2, 3, 5) is best, and does it depend on whether failures are independent or repeated variants of one approach?
3. Does an external failure signal (tests, verifier) versus self-judged failure change whether the trigger helps? Evidence says self-judgment is unreliable; no study sets a trigger on both.
4. Should the trigger count only core-assumption failures? Dunbar says auxiliary surprises are rightly ignored; no LLM study separates them.
5. Does supplying a concrete alternative frame at the trigger help, given Chinn and Brewer found no effect of an alternative in people?
6. Did Horner and Tung 2011 replicate the Bruner and Postman incongruity effect, and with what numbers?
7. Kuhn 1962 primary text: what exactly does he say about the number or kind of anomalies, and what is Kuhn 1977 on rule-free choice?
8. Do reasoning models with built-in switching (R1, QwQ) already do this, so an extra trigger is redundant? Wang shows over-switching, so test an added trigger versus a switch penalty.
9. Can a Lakatos-style rule (progressive vs degenerating) be run on an LLM as a signal, and does it beat a failure counter?
10. Do the Chinn and Brewer response types (ignore, reject, exclude, abeyance, reinterpret, peripheral change, accept) appear in LLM transcripts at measurable rates?


## Gap search results

Run 2026-11-19. Search APIs (arXiv, Semantic Scholar, OpenAlex) were rate-limited and the WebSearch budget was used up, so coverage is thin. Evidence is in evidence_d.jsonl (d01 to d16). Sources opened: arXiv PDFs 2608.16951, 2604.20039, 2501.18585, 2310.01798, 2607.25152, 2609.01526, 2610.37649; Crossref record for Horner and Tung; Kuhn ch. IX transcription; SEP Lakatos.

1. Isolated trigger vs best-of-N at equal tokens: OPEN. Smith 2026 does compare loops against best-of-15 fresh draws (d05): 7 of 10 arms fail to beat it, and the full scaffold is below it, but no arm isolates the Kuhn agent (d04). New fact: the loop that won was the floor prompt with keep-if-better.
2. Best N (1, 2, 3, 5): OPEN. Smith does not report N (d04). Gawali's restart paper (d16) may bear on it but its text could not be opened. Nothing measured.
3. External vs self-judged failure signal: PARTLY CLOSED (direction). Park and Choi (d07) show self-verdicts are uninformative (56% zero-or-negative cycles called improvements; strong judge 44% regressions accepted, 38% gains rejected). Alderete's trigger is itself self-judged (d09). No study sets the same trigger on both. Pilot scale, one agent.
4. Core vs auxiliary failures: OPEN. Only a design note (core-assumption registry, d08, unvalidated) and a false-alarm figure (36.1% false anomaly claims, d15) bear on it. No study separates them.
5. Offering an alternative frame: PARTLY OPEN, weak lean toward yes for LLMs. A scene clue raised discovery 16.7% to 28.6% (d15); EvoSCM keeps about four competing hypotheses (K=1 63.27% vs K=4 74.86%, d14). No study tests the same trigger with and without an alternative, so the Chinn and Brewer null (K04) is unchallenged.
6. Horner and Tung 2011: CLOSED. A replication and critique; resistance to incongruity was not reproduced (d02). K01, K02 moved to contested, K28 added. Full-text numbers still unread.
7. Kuhn primary text: PARTLY CLOSED. Ch. IX and the postscript were read (d01): no anomaly count; criteria are predictive accuracy, problems solved, then simplicity, scope. Ch. VII-VIII and Kuhn 1977 were not opened.
8. Built-in switching in reasoning models: PARTLY CLOSED. Wang 2025 (d11, d12): a switch penalty helps (QwQ 38.3 to 44.1, R1 73.8 to 74.8) and persistence by prompt does not (R1 72.4). So extra switching triggers risk redundancy; the added-trigger vs penalty test was not found.
9. Lakatos-style signal on an LLM: OPEN. Definition read (d03); no LLM test found. K30 added as a design candidate.
10. Chinn and Brewer response types in LLM transcripts: OPEN. No study coding the seven response types was found. Nearest: ignoring evidence rates in c14 and c15, and the false-alarm rate in d15.

New claims: K26 to K30. Status changes: K01 and K02 to contested; K07 now three sources; K10 four.
Unresolved risks: many sources are 2026 preprints; d16 is unopened; the Chinn and Brewer numbers remain unverified.
