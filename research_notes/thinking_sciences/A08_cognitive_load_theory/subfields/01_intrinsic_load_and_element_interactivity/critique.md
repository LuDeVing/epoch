# Critique: A08.01 Intrinsic load and element interactivity (cross-check)

## Numbers re-opened this session (PDF text in D:/research_scratch/A08.01/pdf)
Confirmed:
- CogniLoad (2509.18458): 12 of 22 models below 50% by d=5; gpt-5 0.82 and o3 0.80 at d=10; DS-R1-0528 ID50 19.07; gpt-5 1.00 to 0.97 and o3 0.96 to 0.93 from d=1 to d=3; decline flattens beyond d about 7.
- CLAI (2507.00653): GSM8K 92.5 at 485 tokens vs 92.3 at 310 (36.1%); MATH 53.5 at 525 tokens, 35.3% cut. The MATH CoT row (53.9, 812) was not re-read.
- GSM-Symbolic (2410.05229) Table: Gemma2-9b-it 84.4 (M1), 79.1 (Symbolic), 68.1 (P1), 41.8 (P2, SD 6.0), NoOp 22.3. Phi-3-mini drop over 65% on NoOp confirmed in text.
- Least-to-most (2205.10625): SCAN length split code-davinci-002: standard 16.7, CoT 16.2, L2M 99.7. Last-letter length 12: CoT 31.8, L2M 74.0 (a different model row gives CoT 38.4 vs 74.0).
- Illusion of Thinking (2506.06941): Hanoi N=8 needs 255 moves, failure near move 40 (about 15%); with temperature 0 R1 collapses at N=8, with sampling it keeps 18.2% at N=8 and collapses at N=9.

## Corrections made
1. c01 said "gpt-5 0.96 to 0.93 from d=1 to d=3". That is o3. gpt-5 is 1.00 to 0.97. Claims use the corrected figures.
2. b01 said "1,400 puzzles per config". Paper: 13 open models got 100 puzzles per (d,N,ratio) configuration (14,000 per model); gpt-5, Gemini-2.5 and DS-R1-0528 got 10 per configuration (1,400 per model). a24 is right.
3. a24/b01 describe d as "element interactivity". The paper cites Halford 1998 for this, and d bundles state space, entities, attributes, and clauses. Treat as a proxy.
4. The Tetzlaff meta-analysis numbers (d=0.505, -0.428) came from a blog summary; K05 is marked single-source and not used as established.

## Not re-opened (carried as reported by the evidence agents)
Leahy 2003 tables, Chen 2016 means, REL (Fesser 2026), ToolLoad-Bench, Dziri 2023, CoThinker tables, Hu and Lewis. A damaged file 2601.20412.pdf could not be parsed, so REL numbers are unconfirmed by me. Seen only in snippets or abstracts: a06, a07, a08, a10, a16, b16, b21, b22, b23, b24, c22 (c22 must not be cited).

## Contradictions and weak spots
- The human core claim (interaction of extraneous-load effects with interactivity) rests on a handful of small studies from one research group, with author-assigned counts and no second rater. Leahy's per-question counts are not monotone in the element count (7-element questions showed no gap) and Exp 2 showed a significant low-interactivity effect too.
- Chen 2016: key worked-example effect not significant; the interaction (F(1,45)=5.16, p=.028) is carried partly by a non-significant simple effect; N=47.
- de Jong (2010) says difficulty is not just count; CLT says intrinsic load is fixed, yet sequencing is called a way to manage it. Theory partly unfalsifiable via post hoc germane/extraneous labelling.
- LLM "complexity" papers use different constructs: relational arity (REL), entity/rule bundle (CogniLoad), solution length (Illusion, Hanoi), graph depth (Dziri), edge-weighted dependency (ToolLoad). They agree on direction (harder, worse) but not on one measurable quantity. Solution length is confounded with interactivity.
- Illusion of Thinking is disputed (Lawsen): token limits and unsolvable River Crossing. Lawsen is a short, non-peer-reviewed comment.
- CLAI and CoThinker: single-group or single-author, proxies, small or mixed gains, instruction following got worse with splitting.
- Distractor effect in CogniLoad is U-shaped, which CLT does not predict.
- No study found that measures element interactivity inside an LLM's own prompt and tests a count-then-split gate at equal tokens.

## GAPS
1. Does a model-made or rater-made element count predict LLM failure better than length, steps, or depth, on the same items (inter-rater agreement and predictive power)?
2. At equal tokens, does gating decomposition on estimated load (S0) beat always-decompose and never-decompose, and where is the break-even load?
3. Does splitting until each part has at most k interacting elements work for LLMs, and what is the best k per model class (ID50-style threshold on our own tasks)?
4. Is the human interaction (extraneous-load aids help only at high interactivity) replicable at larger N and by independent labs, and does the analogue hold for LLMs (extra context hurts on low-load items only)?
5. In LLMs, is the benefit of decomposition due to lower per-step arity (REL-type binding) or just shorter chains and more verification? An ablation separating them is missing.
6. Does a self-estimate of intrinsic load by the model itself correlate with true difficulty (calibration), given CLAI never ablated this step?
7. Why does CogniLoad show a U-shaped distractor curve, and does it appear with current frontier models?
8. How much of the Hanoi/long-output collapse is output-format, and does asking for a procedure instead of an enumeration restore the scaling across non-Hanoi tasks?
9. Does expertise reversal have an LLM analogue (scaffold depth should shrink for items the model already handles), and what does over-scaffolding cost at equal tokens?
10. Can the fixed-versus-changeable intrinsic load dispute (de Jong) be settled operationally for an agent: does restructuring the task (sequencing, isolated elements first) reduce failures beyond decomposition alone?


## Gap search results

Search budget note: the web search quota ran out partway; the rest used arXiv and direct PDF text. New evidence is in evidence_d.jsonl (d01 to d20). Claims K19 to K28 were added, and K03, K05, K08, K13, K14, K15 got new evidence ids.

Other correction: Tetzlaff et al. (2025) is in Learning and Instruction 98:102142, not Educational Psychology Review. Its effect sizes are still unverified (d02, opened false).

Status by gap:
1. Rater or model element count vs length, steps, depth: STILL OPEN. No study found. Indirect support only: BAPO bandwidth predicts failure independent of length (d09); LLM raters track human item difficulty at rho about 0.5 to 0.8 (d16) but fall below 0.50 on zero-shot absolute ratings (d15). No inter-rater agreement data for element counts.
2. Gated vs always vs never decomposition at equal tokens: PARTLY. ADaPT (d10) shows failure-gated beats both on three environments, but tokens are not matched and the gate is failure, not load. Break-even load not measured. Matched-token evidence on search vs CoT (d19) points the same way.
3. Best k per model class: STILL OPEN. Only CogniLoad ID50 (d20) gives per-model thresholds (below 0 to 19.07), and it is not a k. Needs own measurement.
4. Human interaction replication and LLM analogue: HUMAN SIDE STILL OPEN (d01 is moderator-level, second-hand d values, no independent preregistered test found). LLM SIDE ANSWERED IN PART: extra context hurts more at high load (GSM-IC step count, CogniLoad trough widens with d), so the "hurts only low-load items" version is not supported (d04, d20, d03).
5. Per-step arity vs chain length and verification: PARTLY. Wolf et al. (d08) show context sharing alone costs 10 to 20 times in generations with sub-answers fixed. Arity inside a step is still not separated.
6. Self-estimate of load: PARTLY. Self-rated effort and ability predict own failure (AUROC up to 0.83 to 0.89, d14); human-difficulty ratings do not (d15). CLAI's load step is still unablated. Depends on elicitation.
7. U-shaped distractor curve: PARTLY. Fades for gpt-5 and o3, widest at d = 5 and N = 20, gone by N = 250 (d20). No mechanism in the paper; a confound with effective chain length is my reading of the generator, untested.
8. Hanoi collapse and output format: PARTLY. Chunked output still fails near 8 disks (d05); procedure format works on Hanoi only (d06, no numbers); standard Hanoi is saturated but flat-to-flat is not (d07). Nothing outside Hanoi.
9. Expertise-reversal analogue and over-scaffolding cost: PARTLY. CoT gain is concentrated in symbolic tasks and can cost up to 23 points (d11, d12); R1 reportedly worse with few-shot (d13). No equal-token test across item difficulty within a model.
10. Fixed vs changeable intrinsic load: STILL OPEN. Demonstration ordering effects are small or mixed (d17, d18); recite-then-solve helps a lot at long length (d03). No test of isolated-elements-first inside a problem.

Caveats: many table rows in extracted text were misaligned and were used only where legible (flagged in the limits field). d19 was read at abstract and introduction level only. The mechanism note in d20 is a hypothesis.
