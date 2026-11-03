# C04.04 Transformational creativity: cross-check and critique

Checked on 2026-11-03 by re-opening full PDF text (pdftotext) of 8 papers. 24 claims are in claims.jsonl (C04.04-K01 to K24).

## 1. Numbers re-checked

Confirmed (source text matched the evidence line):
1. Si, Hashimoto, Yang 2025 (arXiv 2506.20803): after execution, human ideas change -0.010 novelty, +0.078 excitement, -0.052 effectiveness; AI ideas -1.049, -1.760, -1.879 (1-10 scale). b14 matches.
2. Yue et al. 2025 (2504.13837): pass@1 on training set 26.1 to 42.5 under RLVR. c07 matches.
3. Pan, Xie, Wilson 2025 (2501.18009): Little Alchemy 2, 500 trials: Llama3.1-70B 25, GPT-4o 35, DeepSeek-R1 85, o1 177, humans 42. c14 matches.
4. Jiang et al. 2025 Artificial Hivemind (2510.22954): 79 percent of cases above 0.8; min-p same-model pairs 81 percent above 0.7 and 61.2 percent above 0.8; open-endedness high 0.800 vs low 0.837 (42 models). b15, c08, c25 match.
5. Suzuki, Banaei-Kashani (2511.20471): Bridge human creativity T-UoT 0.680; HypoArena E-UoT BTD 1535.4 / 32.7 percent, T-UoT 1484.6 / 17.3 percent (6th); ablation preference 54.2 percent; rank #7 to #2 after forced mechanism. a12, a13, a14, c04 match.
6. Bhushan et al. 2026 (2608.30047): alpha 0.724, GPT-5 judge r = 0.732, 87.0 percent (80/92) REFINE, gold-medal human H-creativity 0.744 vs 1.423. b01, b03-b05 match.
7. OMEGA (2506.18880): only notable transformative OOD gain is Setting 7, +10 pp. a16 matches.
8. Si et al. 2024 (2409.04109): 4000 seeds, about 200 (5 percent) non-duplicate; novelty 4.84 / 5.64 / 5.81, N=49 per condition. b12, b13, c09 match.

Corrections and notes:
- Si 2024 novelty significance: b12 says p<0.05, c09 says p<0.01 for Test 1. The paper text gives p<0.05 as the headline after multiple-test correction; its table marks AI ideas ** and AI+rerank ***. Use "p<0.05 (corrected)". The 109 reviews per condition in the table differ from the 298 unique reviews in b12; both are in the paper (reviews counted per condition vs unique).
- Si 2024 "4000 seed ideas" is per topic, not in total (c09 says per topic; b13 wording is ambiguous).
- b15 says 79 percent is "in 79 percent of cases mean pairwise similarity exceeded 0.8"; c08 reports a different statistic (81 percent / 61.2 percent, min-p, same-model pairs). These are two different measures, not a contradiction. Do not merge them.
- Not re-opened: Beaty AGC-Bench (b10, b11), CreativeBench, InnoGym, Chakrabarty, Lu, MacGyver, DGM, ADAS numbers. They are single reads by the first agents.

## 2. Contradictions between sources
- Position papers (Franceschelli and Musolesi; Magrin-Chagnolleau) say transformational creativity is out of reach for LLMs. T-UoT and EscapeAgent show small measured gains from rule-change scaffolds on narrow tasks, and OMEGA shows no gain from RL. Nobody has run a direct test, so K05 is "contested".
- Hivemind says models are trapped in a shared space and inference-time fixes fall short. Schaeffer et al. 2026 reanalysis says prompting raised diversity and the flagship example does not hold (river 80.5 percent of 750). Unresolved.
- AGC-Bench: reasoning mode adds little for creativity (dz +0.34). CreativeBench: reasoning helps exploration, not combination. Different tasks; not resolved.
- Novelty is easy to get (Si: AI ideas rated more novel) but does not survive execution; Bhushan finds novelty and score changes uncorrelated. Consistent, which supports K12.

## 3. Weak spots
- The three LLM studies closest to Boden's transformation (OMEGA, T-UoT, EscapeBench) each have one author group, no replication, and a different meaning of "transformative" (new math tactic, edited task rules, unconventional tool use).
- T-UoT scoring and selection use the LLM itself (conflicts with G4, G8). Human sample: 10 generations per cell, 3 tasks. Gains of 0.03 to 0.2 have no confidence intervals.
- OMEGA is fine-tuning on Qwen 7B; it says nothing about prompt scaffolds on frontier models.
- Bhushan's level 4 is relative to the agent's own history (P-creativity), not a real rule change.
- Formal theory (Santo, Schapiro) is not tested at all; Wiggins 2006 and Toivanen 2018 only seen second-hand (a27, a28, c21).
- Many sources are arXiv preprints from 2026 with no peer review known.

## 4. Seen only in snippets / not opened
- Wiggins 2006, Ritchie 2006, Toivanen 2018, Boden's books: second-hand only (a02, a07, a27, a28, c21).
- Lenat EURISKO/AM, Cohen AARON, Langley BACON (c22): background knowledge, unverified.
- Magrin-Chagnolleau: a21 read, c23 title only.
- TwistBench (plot twists) and Spark not retrieved (a26).
- Marco et al. Pron vs Prompt: results tables not read (a24).
- a25 Nagarajan: abstract-level numbers only.

## GAPS
1. Does an O4 or O8 operator beat a plain "be creative" prompt, a temperature sweep and best-of-N at equal tokens on a task with a code check? No study has this control.
2. Is the T-UoT null result (6th of 7) caused by the rule edit or by failing to propagate its consequence? One diagnostic on 12 failures says propagation; needs a larger, code-checked test.
3. Does O6 (change representation) rescue OMEGA transformative items for prompted frontier models, as opposed to RL-trained small models?
4. What is the pass@k gap between a rule-change scaffold and the base model? Yue suggests sharpening only; no one has measured widening from a scaffold.
5. Does the Hivemind homogeneity hold under a matched null, and does a frame-change instruction beat temperature for frame diversity? (Schaeffer reanalysis is one author group.)
6. Can the "drop an upstream constraint first" rule (Schapiro DAG) be tested: do edits to high-dependency constraints yield more valid new solutions than random edits?
7. What triggers abandoning a novel but poor approach? Bhushan shows 6.5 percent abandonment; does an impasse detector (G1) raise it without losing score?
8. Is there a verifiable benchmark of real rule-change problems (not template maths) where the familiar frame provably fails? None found; TwistBench and Spark unchecked.
9. Do EscapeAgent's Foresight and Reflection gains replicate on a different environment and at equal tokens (single run averages, same benchmark for design and test)?
10. Can a non-LLM selector (execution, constraint check) replace the LLM scorer in T-UoT, and does the ranking change?

## Gap search results (2026-11-03, evidence_d.jsonl d01-d17)

Search limits: arXiv API, arXiv search, Semantic Scholar and OpenAlex returned HTTP 429; one WebSearch answered, then the shared budget ran out. Work used direct PDF reads of known papers (OMEGA, Yue, T-UoT, Baba Is AI, Schaeffer, Verbalized Sampling, Peeperkorn, EscapeBench, Bhushan, Schapiro).

Gap 1 (O4/O8 vs plain prompt, temperature, best-of-N at equal tokens): OPEN. No study has the control. New: plain prompt is last on Qwen3-14B and first on GLM-4-9B (d04); temperature is weakly tied to novelty (d12); verbalized sampling beats temperature on the diversity-quality front (d11). Best-of-N and a code check still missing.
Gap 2 (why T-UoT failed): PARTLY CLOSED. Dual cause: 7 of 12 failures were reasonable edits not converted, 5 of 12 were poor edits (d01); word-overlap does not separate wins from losses (d02); a forced consequence step lifted one case rank 7 to 2.5 (d03). Larger code-checked test not done. K09 reworded.
Gap 3 (O6 on prompted frontier models in OMEGA): OPEN. OMEGA only RL-trains Qwen2.5-7B on transformative items (d07).
Gap 4 (scaffold pass@k gap): OPEN. Only external teacher data (distillation) widens pass@k (d08); no scaffold measurement.
Gap 5 (Hivemind matched null; frame change vs temperature): PARTLY CLOSED. Matched-null reanalysis exists: 80.5 percent single vehicle, residual effect 2-3 times the different-idea null (d09); prompt rewording raises diversity (d10). Frame change vs temperature still not compared; reanalysis is still one author group, so K14 stays contested.
Gap 6 (upstream-constraint rule): OPEN. Theorem is true by counting dependents; no validity test (d15).
Gap 7 (abandoning a poor novel approach): OPEN. Search policies converge; no impasse-trigger arm (d14).
Gap 8 (verifiable rule-change benchmark): PARTLY CLOSED. Baba Is AI (d06) found; TwistBench and Spark still unretrieved (d16).
Gap 9 (EscapeAgent replication): OPEN. Numbers re-read (d13); no second environment, no token count.
Gap 10 (non-LLM selector): OPEN. Judges only moderately consistent (d05); no execution-based selector tried.

New claims K25-K28 added; K03, K04, K06-K11, K14, K16 got evidence ids and gap notes.
