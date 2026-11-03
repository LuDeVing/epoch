# A04.04 Metacognitive knowledge (declarative, procedural, conditional): cross-check critique

## 1. Numbers re-opened (PDF text this session)
Confirmed exactly: Zhang 2025 strategies (arXiv 2507.11423): Phi-4 TruthQuest no-strategy 47.2, oracle 82.9; R1-Distill 63.4 vs 90.1; ZebraLogic 27.3 vs 37.7 and 32.0 vs 36.4; adherence 99/88/81/64. MIRROR (2604.19809): CFR 0.600/0.605/0.514/0.143, 76 percent, p=0.90, 0.0004, <0.0001. Cao 2026 (2605.14186): 48.3 to 56.9; full 47.0 [37,57]; random retry 45.7 [43,48]; full context 40.0. Didolkar 2024 (2405.12205): MATH 42.2/50.30/50.31/53.88; GSM8K random 92.87, skill 94.31. AdaptThink: -12.7 / -79.9 percent for NoThinking, +2.4 / -53.0 percent. Think2: 69.55/80.71/77.98. Self-Discover: 10-40x, 74.7 percent, 87.5 percent. MRP (2406.11698): 0.772 vs ToT 0.725; GPT-3.5 MRP 0.433, SPP 0.469. SMART: +15.2, +11.0, +3.5. MC2: 78.93 to 85.13, 41.33 to 88.67, 1631 tokens, reasoner-only 72.67. MUSE (2411.13537): 84/90, random 68/69. Steyvers: 301 participants.

## 2. Corrections and sharper readings
- b13 text says an oracle "would roughly double accuracy". True only for TruthQuest Phi-4 (1.75x); ZebraLogic oracle gain is 1.1x to 1.4x. Claim K06 states this.
- c16 says MUSE "loses much of the gain" with random self-assessment. Numbers show random assessment keeps 68/69 vs ReAct 35/35, so self-assessment explains about 16 of 49 points. Reworded in K16.
- a23/Cao: the full harness (47.0) is not separable from random retry (45.7); the headline +8.6 is vs a single attempt, not vs matched random retry. Treat as weak support for confidence-guided control (K15).
- Evidence file ids: a25 (Luo prefix trap) is not about strategy knowledge; kept as motivation only, no claim built on it.
- b04 child inventory counts and b07-b09 effect sizes come from snippets; flagged.

## 3. Contradictions between sources
- MP (a17/b18) reports gains over CoT; Think2 (b17) shows a forced plan-monitor-evaluate prompt hurts a non-reasoning model. Resolution unclear: differences in model, task type and prompt design.
- Self-Discover and MRP (GPT-4) show model-side selection helps; Zhang 2025 and MRP with GPT-3.5 show it does not. Likely model strength; not tested within one design.
- MAI: original claims eight subscales; at least four replications (a09, b02, b03, b05) recover two factors; b05 EGA found three. Unsettled.
- Kargupta (c24): more self-awareness in humans yet negative association with success in models; direction of cause unknown.

## 4. Weak spots
- Almost every LLM result is one run, no CIs, mostly 2023-2024 models or small open models; the 2026 preprints (MIRROR, Cao, MC2, MaR, Think2) are unreplicated.
- Schraw and Dennison 1994, Schraw and Moshman 1995, Paris et al. 1983, Harrison and Vallin 2018 were not opened (a08, a10, a27, a28, b03). Declarative/procedural/conditional origin is background knowledge.
- Founding Flavell experiments are known only through the 1979 essay: no N, no recall rates.
- Many studies train weights (SMART, AdaptThink, MaR, Meta-R1); our scaffold cannot train, so only the selection logic transfers.
- Few comparisons are at matched tokens; MC2 and Self-Discover report tokens, others report time or calls.
- Snippet-only: b04, b05, b06, b07, b08, b09, c18, c30, c31.

## GAPS
1. At equal tokens, does a per-class operator record (measured pass rates) beat the best single fixed operator, and does it beat a random-operator control, on our own task classes?
2. How large is the per-class oracle gap (best operator per item) on our tasks? Where it is small, the record cannot pay.
3. Is the class record better enforced by code (routing) than shown to the model in the prompt? MIRROR says yes for confidence; no test exists for operator choice.
4. How many items per class are needed before a measured class record is more reliable than a prior (cold-start; MC2 ordering effect)?
5. Does the record transfer to mixed-class items, and to a different or cheaper model (MIRROR transfer index 0.02 to 0.18 vs Didolkar transfer success)?
6. Is conditional knowledge separable from procedural knowledge in an LLM (knows-how-to-run vs knows-when-to-pick)? Design an ablation.
7. Does random or inverted record content still keep most of the gain (MUSE suggests yes)? What part of any gain is the extra structure rather than the selection?
8. Which model strength makes self-selection (Self-Discover, MRP) work versus fail (GPT-3.5, Phi-4)? Is there a threshold we can measure for our model?
9. Original sources (Schraw 1994/1995, Paris 1983, Flavell 1970 studies) should be read for exact N and recall figures.
10. What is the rate of the four Flavell failures (wrong, not retrieved, ignored, unhelpful) when an LLM uses a written class record?


## Gap search results
Evidence file evidence_d.jsonl (17 lines, 13 opened). Search was limited: arXiv, Semantic Scholar and OpenAlex APIs were rate limited; 1 WebSearch worked, then the shared budget ran out. Paywalled human sources returned 403.

1. Equal-token record vs best fixed vs random: PARTLY CLOSED, still open for our tasks. Route to Reason (d06) has a random control (69.5 vs best model 80.0, router 82.5 at 40 percent of tokens). Select-then-Solve (d02) has router 53.1 vs best fixed 50.3 but no random arm and no equal-token arm. Router gain over best fixed is small (0.5 to 3 points) and noisy. No study uses a written class record. Claim K24, K25.
2. Oracle gap: CLOSED as literature (d01): +12.4 to +24.1 points over best fixed on a 10-benchmark mix; optimistic because oracle maxes over noisy runs. Our own tasks still need measuring. K06 upgraded to established.
3. Code vs prompt enforcement for operator choice: PARTLY. Code router beats self-route (d02, d04) and code gating halves tokens (d08), but the two arms differ in information, so confounded (d05). K26.
4. Cold start: OPEN. Training sizes known (300 to 400, about 1470) and a bandit warm-up recipe (d12), but no items-per-class curve. K29.
5. Transfer: PARTLY. Unseen easy sets transfer (d07); self-knowledge decays with distance (d11); mixed-class and cheaper-model transfer untested. K30.
6. Conditional vs procedural separable: STILL OPEN. KAPRO (d09) separates knowing-whether-to-act from acting, a partial proxy only. Ablation design to use: arm A model told operator (procedural), arm B model picks from list (conditional), arm C code picks from record; the B-A and C-B differences measure each part.
7. Random or inverted record content: OPEN. Only RTR's random control (d06) and MUSE from earlier. No inverted-record test found.
8. Model strength threshold: PARTLY. Self-route ties Direct only for GPT-5 and loses or ties for 3 weaker models (d04). Threshold for our model must be measured. K28.
9. Original sources: OPEN, not reachable (d17).
10. Flavell failure rates under a written record: OPEN. Only proxies (d16, d09: Kc/Aw 1.76 to 45.48 percent). K27.

Caveats: Select-then-Solve contradicts itself between text and tables (d01, d04); Route to Reason and PRISM too (d06, d13). Use direction, not exact figures. All new results are single-run, unreplicated 2025-2026 preprints.
