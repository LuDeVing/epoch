# Critique: D07.04 Experimental practice (cross-check)

## Corrections and confirmations (sources re-opened this session)
1. PaperBench (arXiv 2504.01848, PDF text): 21.0% Claude 3.5 Sonnet (New), 8,316 outcomes, humans 41.4% (best of 3, 48 h) vs o1 26.6% on a 3-paper subset, Code-Dev o1 43.4%. All CONFIRMED.
2. EXP-Bench (arXiv 2505.24785 abstract): 461 tasks from 51 papers; complete executable success 0.5%; single aspects reach 20-35%. CONFIRMED. The 1.4% "All" figure and failure shares (a14, a15) were not re-checked.
3. MLE-bench (arXiv 2410.07095 abstract): o1-preview with AIDE reaches bronze or better in 16.9% of 75 competitions. CONFIRMED. Note: it is "at least bronze medal", not just pass@1 wording; b20/c16 say pass@1. Minor.
4. Beel and Kan (arXiv 2502.14297 abstract): 42% of experiments failed on coding errors, 8% char change per iteration, median 5 citations, 5 of 34 from 2020 or later, micro-batching mislabelled novel. CONFIRMED. The "5 of 12" and "4 of 7 manuscripts" counts are from the body, not re-checked.
5. BED-LLM (arXiv 2508.21184 abstract): "substantial gains" on 20 Questions and preference elicitation. Direction CONFIRMED; the +37.4 pp mean was NOT re-checked (abstract has no number).
6. POPPER (arXiv 2502.09858 abstract): Type-I control, high power, about 10x faster than human scientists. Direction CONFIRMED. The c04 table values (0.152, 0.145, 0.248, 0.610) were NOT re-checked, and c04 itself says the last row is hard to align.
7. Errington et al. cancer biology (eLife 71601 abstract): 158 effects (136 positive, 22 null); median effect 85% smaller; 92% smaller than original. CONFIRMED. NEW detail not in b08: success by 3+ of 5 binary methods was 40% (39/97) for positive effects, 80% (12/15) for nulls, 46% (51/112) combined. Claim K07 uses these.
8. Errington protocol paper (eLife): 193 experiments, 53 papers, reagents requested for 136 of 193 (70%). Consistent with b07. Other b07 figures not re-checked.
9. Not re-opened (from memory of the abstracts, treated as consistent with the evidence files): OSC 2015 36% (35/97), Camerer 13/21, Many Labs 2 15/28 and d 0.60 to 0.15. No contradiction found, but these were not re-fetched here.
10. Cross-file duplicates agree (Beel appears in a16, b12, c11; PaperBench in a19, b14, c14; DiscoveryWorld in a21, c07). No numeric conflicts, but they are the same underlying papers, so they count as ONE source each in claims.
11. Correction to evidence wording: a19/b15 "Claude 21.0%" vs b14 "o1 13.2%" are different scaffold results and consistent. c18 year 2023 is a position paper, not a measured benchmark.

## Contradictions and tensions
- Experimenter regress: Collins (sociological) vs Franklin (epistemological strategies) vs Pickering (mutual support). Unresolved; K03 marked contested.
- Galison two traditions vs Staley (shared statistical form). K22 contested.
- Replication verdict depends on rule (18% to 62%), so "X% replicate" is not a single number.
- Scaffold effects point in both directions (IterativeAgent up for o3-mini, down for Claude), so no scaffold is uniformly better.
- AI Scientist: Lu et al. report a reviewer comparable to humans (F1 0.57 vs 0.49), while Beel and Kan find poor novelty checking and wrong numbers in outputs. Different questions, but together they say review scores do not prove soundness.

## Weak spots
- Historical core (Hacking, Galison, Collins, Pickering, Franklin) is read only through the Stanford Encyclopedia summary; no original book text was opened. Gooding (a10) and Steinle (a09) are unopened or snippet-only.
- Many LLM benchmark claims are single-author-group results with LLM judges (PaperBench judge F1 0.83; EXP-Bench monitor).
- Human baselines are tiny (8 PhDs on PaperBench; 9 experts in POPPER; 16 task sets in DiscoveryWorld).
- No study found of LLMs doing Hacking-style intervention or instrument calibration (c26). This was a limited search; absence is not proof.
- Psychology and cancer-biology replication evidence is about humans/labs; transfer to an agent test design is by analogy only.
- Claims counted as "established" with high source counts (K10) rest on benchmarks that share a style (agent writes and runs ML code), so they are not fully independent in setting.
- Newer 2026 work (CORE-Bench v1.1, arXiv 2606.26158) was seen only in its abstract: human-agent collaboration gave about 2x speedup, and accuracy on CORE-Bench Hard has saturated. This changes the picture in b16 (older 21.5% Hard figure is outdated).

## Seen only in snippets or abstracts
a09 (Steinle), a10 (Gooding, from background knowledge), c20 (blicket snippets), c21 (Robot Scientist Adam, no numbers), BED-LLM and POPPER abstracts in this check, CORE-Bench v1.1.

## GAPS
1. Does choosing tests by computed expected information gain still beat free-choice tests at equal token budget when the agent must also write the likelihood model itself (BED-LLM uses supplied settings)?
2. Does a run-and-check step (execute the test, read real output) cut the 40-50% execution failure rate seen in EXP-Bench and the Sakana evaluation, and at what token cost?
3. Does a calibration step (inject a case with a known answer before trusting a test) catch errors that independent resampling misses? No LLM study of this exists in our evidence.
4. What are the real BED-LLM and POPPER table numbers (re-open the PDFs); do POPPER Type-I results hold on non-permutation nulls?
5. How much does fixing the pass criterion before the run reduce post-hoc tuning (experimenter regress) in an LLM agent?
6. Are the 2025-2026 successors to PaperBench, EXP-Bench and MLE-bench (post-saturation versions, newer models) showing the same stage-wise failure pattern?
7. Original text of Hacking, Galison, Gooding: what do they say about the order of building apparatus and testing, beyond the encyclopedia summary?
8. What threshold rule (3-sigma to 5-sigma style) should an agent use when it tries many candidate tests, and what false-positive rate does it give on seeded nulls?
9. Does forced continuation (IterativeAgent style) help or hurt depending on base model, and is there a cheap way to predict which?
10. Do LLM-simulated replications (Aher et al.) predict real replication outcomes, or only recall known classics?


## Gap search results (evidence_d.jsonl, d01-d19)
Limits: WebSearch budget was exhausted after one call, and the arXiv, OpenAlex and Semantic Scholar search APIs returned HTTP 429. Papers were opened by direct arXiv PDF links only.

1. Information-gain tests at equal token budget: PARTLY CLOSED. BED-LLM (full text, d01-d03) has the LLM write its own prior and likelihood and still wins (mean +40.4 pp over prompt-only from Table 1 cells; paper says 37.4). The cheap "LLM picks the best candidate" variant gains only about 8 pp. No token-matched comparison; STILL OPEN on budget.
2. Run-and-check cutting execution failures: OPEN. PaperBench (d07) shows the weak stage is execution and result reading (Claude 35.4 code vs 1.8 execution vs 0.7 analysis); EXP-Bench (d10) gives failure shares. No study varied a run-and-check step alone.
3. Calibration with known answers: PARTLY. Luo et al. (d16) inject known label noise so the accuracy ceiling is known, and catch peeking. Evaluator side only; no agent-internal use. CORE-Bench (d13) shows agent confidence is useless (32.1% vs 93%).
4. Real BED-LLM and POPPER numbers: CLOSED for numbers (d04, d05). POPPER's 0.152 and 0.180 exceed 0.1 and pass by a 1-sd rule; K16 reworded. Non-permutation nulls: OPEN (d06).
5. Fixing the pass criterion before the run: PARTLY. Thomas et al. (d14) block 72-74% of p-hack transfer, 6 of 7 in their own preregistered test, but with human-tuned LLM pipelines, not an agent. New claim K26.
6. 2025-2026 successors: PARTLY. CORE-Bench v1.1 (d12) opened in full: saturation at 97.4-100%, 20 shortcut tasks, scaffold gap 44 pp. No post-saturation PaperBench or EXP-Bench successor found (search blocked). OPEN for those two.
7. Original Hacking, Galison, Gooding: OPEN (d19). Not reached.
8. Threshold rule for many candidate tests: OPEN. POPPER's e-value product with alpha is the only tested rule found (Type-I 0.145-0.18 on permutation nulls at alpha 0.1); no 3-sigma vs 5-sigma comparison for agents.
9. Forced continuation by base model: PARTLY CLOSED. Two benchmarks (d08, d11) show it is model-dependent. PaperBench authors note that all models but Claude often stopped early in plain runs; that is a candidate cheap predictor but was not tested. K24 raised to established.
10. LLM-simulated replications: OPEN (d18). Aher et al. only reproduce famous classics; nothing found on predicting unseen replications.

Claims changed: K11, K12, K13, K14, K16, K20, K24, K25 extended; K24 status now established; K26-K29 added. Note: the arithmetic of 40.4 pp vs 37.4 pp is unexplained.
