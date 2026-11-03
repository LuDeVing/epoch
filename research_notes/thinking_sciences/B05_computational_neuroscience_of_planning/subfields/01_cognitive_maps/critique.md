# B05.01 Cognitive maps: cross-check critique

## Corrections made (sources re-opened this session)
- Momennejad 2017 (PMC6941356): t(57)=2.89 (reward vs transition) and t(57)=10.14 (reward vs control) confirmed. Evidence a05 says p<0.01; b05 says Bonferroni p=0.016. Both are consistent (raw vs corrected). Use the corrected value.
- CogEval (arXiv 2309.15129): GPT-4 Table values 0.99/0.82/0.55/0.47/0.21/0.67/0.60 confirmed. "0 of 30" line: the text says that in the same 30 runs the success rate cannot exceed 10 percent; "0 of 30 at temperature 0" was not re-found by me. Treat "never above 10 percent" as the safe number.
- Kim 2024 (arXiv 2406.15275): 19.0, 26.5, 76.5, 32.1, 33.9, 88.5, 94.5, 42.3 to 85.2 confirmed. Correction: the backtrack ablation (42.3 to 85.2) is for forward construction. Key boundary: the gain is from fine-tuning; prompting a map gave 0-1 percent (b13). Do not cite 76.5 as a prompting result.
- Li 2023 Othello-GPT: 0.01, 5.17, 93.29 percent confirmed.
- Wu 2024 VoT: 59.00 vs 35.50 (+23.5) confirmed; CoT about 54.00 and p<0.16 confirmed, so the gain over CoT is not significant.
- Yan 2025 (2512.18190): 64.40, 81.20, 2.52 rounds, 59.80 confirmed.
- MAP 2026 (2605.13037): 31.8 to 61.1, 31.8 to 71.9, 13.9 to 24.3 confirmed for Qwen3-4B-Instruct.
- Qin 2026 (2610.25596): abstract confirmed; about 1 percent of keys/values sparse binding confirmed. Its main finding is pairwise links composed on demand, NOT a global coordinate map. This weakens any reading of "LLMs hold cognitive maps" as geometry.
- Gurnee and Tegmark R2 values: my grep of the arXiv text did not find the numbers (table layout). Not re-verified; a17/b19/c09 agree with each other except a17 lists Llama-2-70b world 0.896 vs b19/c09 0.911 (0.911 is the largest-model row). Use 0.911 and flag as unverified. Proximity error held-out: a17 0.170, c10 0.164; unresolved.
- Stangl 2018 and Constantinescu 2016 were not re-opened (wrong PMC id fetched; not retried). Their numbers rest on single readings agreed between a08/b01 only.

## Contradictions between sources
- Gurnee numbers above (0.896 vs 0.911; 0.170 vs 0.164).
- a08 says vmPFC hexagonal strength vs performance r=0.43, p=0.039; b02 says r=0.432 (same). Consistent.
- Kim: baseline claim that cognitive-map prompting can work (abstract) vs prompting results of 0-1 percent (b13, c07). The real result needs training.

## Weak spots
- The grid-like code in abstract space is a small-N fMRI finding with mixed replication (older adults null, 2024 ROI inconsistent, 2019 vmPFC preprint null not opened). Nothing in the schema should depend on it.
- Latent-learning evidence is second-hand (Tolman 1948 summary), no statistics.
- Most prompt-only LLM results are on weak or small models; MAP and Yan gains vanish on strong models. Our agent is strong, so expected gain is small.
- No source tests an explicit written map against an equal-token plain chain of thought on a strong model. Most positive studies do not control tokens.
- CogEval is 2023 and used GPT-4; no 2025-26 reasoning-model rerun was found.

## Only seen in snippets or not read
- a23 (O'Keefe, Hafting), a24 (Stachenfeld 2017), a25 (Behrens 2018), b23 (Gershman 2018), b24 and b25 (preprints) were not opened by the finders; Stangl, Constantinescu not re-opened by me.

## GAPS
1. Does a written explicit state-move map (S2) beat plain chain of thought at equal tokens for a STRONG current model on CogEval-style graph tasks? No source controls tokens.
2. Does the map benefit shrink with model strength (MAP, Yan hint yes)? What is the break-even model size?
3. Has CogEval been rerun with reasoning models (o1/o3, Claude, Gemini thinking) in 2025-26, and does the multi-step and policy revaluation collapse persist?
4. Which map format works for prompt-only use: relation list, adjacency, coordinates, or diagram? Qin 2026 suggests pairwise composition; no format comparison exists.
5. How accurate is the agent's own written map (edge hallucination rate) and does an edge-verification step (G) repair planning?
6. After a transition change (blocked move), does a re-plan operator restore success? Human data show transition revaluation is the hard case.
7. Does goal-skewing (marking goal and predecessors in the map) help search, as rodent grid data suggest (Butler 2019)?
8. Do the 6-fold grid replications (Stangl, Wu 2024, 2019 preprint) settle, and are there any larger-N replications of conceptual grid coding?
9. Does the VoT redraw-state step help once state-tracking accuracy is checked, given only 24-26 percent visualisation accuracy?
10. Do trained-map benefits (Kim) transfer to scaffolds via few-shot map-then-plan with many shots, or does it need gradient training as the authors claim?

## Gap search results (2026-11-03, evidence_d.jsonl d01-d16, claims K25-K33 added)
Limits: arXiv, Semantic Scholar and OpenAlex APIs returned 429 for most calls; 3 WebSearch calls were used (the budget then ran out). No 2025-26 reasoning-model rerun of CogEval was found.

1. Written map vs plain CoT at equal tokens, strong model: STAYS OPEN. No source controls tokens for a prompt-only map. Closest: Kim 2024 few-shot (d06): o1 with no map prompt 38 percent at 4-shot vs 10 percent with a map prompt; trained DFS 94.5 vs trained map 88.5 (d16). Hybrid-WM (d03) reports tokens per success, where the grounded hybrid used fewer than CoT (15021 vs 21301), but its transition model is trained.
2. Does the benefit shrink with strength: PARTLY CLOSED, direction yes. Hybrid-WM gain +26 (Llama-3-8B) to +4 (GPT-4o-mini) (d04). But GAVEL (d01) shows a checked graph model still lifts Claude Sonnet 5 from 38.6 to 99.4. The difference: GAVEL adds an external verifier, not map text. Break-even size not located.
3. CogEval rerun with reasoning models: STAYS OPEN. Search found no 2025-26 follow-up. Only indirect evidence: o1 in Kim 2024 (d06).
4. Map format for prompt-only use: STAYS OPEN. No format comparison found. Priors: pairwise links composed on demand (Qin 2026, d15), humans use both vector and adjacency views (d14), a hierarchical map beat a flat grid in a trained model (d08).
5. Accuracy of the agent's own written map and edge verification: PARTLY CLOSED. Self-imagined states wrong on 17-32 percent for weak backbones; self-verification barely helped but external grounding did (d03, d04); perception-built maps are poor (landmark IoU below 5 percent, d08); external repair beat re-asking the LLM (d02). Not measured: a frontier model's text-graph edge error rate.
6. Re-plan after a changed transition: PARTLY CLOSED. Graph-derived repair beat LLM-feedback replanning (67.7 vs 55.4, 1 vs 3.4 calls, d02) in a symbolic setting. No human-style detour test on an LLM.
7. Goal-skewing of the map: STAYS OPEN. No LLM or human test found; GAVEL's belief reordering by expected cost cut distance 5.4 percent (d02 context) but that is scheduling, not goal marking.
8. Grid replications: CLOSED as "fragile, small N". Positive: Park 2021 N=21 (d11), Theves 2020 N=25 (d10, mPFC null). Null: Kransberg 2026 N=110 passive spatial (d09). Baram 2021 and 2026 did not test hexagonal coding (d12, d13). No abstract-space replication above N=30.
9. VoT redraw step: STAYS OPEN. No new VoT replication found.
10. Few-shot transfer of trained-map benefit: CLOSED for up to 4 shots (0-10 percent, d06); many-shot untested.

Not re-opened: Stangl 2018 and Constantinescu 2016 numbers still rest on earlier readings. Hybrid-WM mostly uses simulated benchmarks with weak backbones; GAVEL, GraphThink and Hybrid-WM are single preprints (2026) and none is a pure prompt-only map test.
