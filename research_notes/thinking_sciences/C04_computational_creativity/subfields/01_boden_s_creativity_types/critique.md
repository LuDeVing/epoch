# Critique: C04.01 Boden's creativity types (cross-check)

## Re-checked numbers (PDF text opened this session, all confirmed)
1. UoT (arXiv 2511.20471): E-UoT 1535.4 rating, 32.7% vs ToT 1515.8 / 25.5% (Qwen3-14B, Gemma-3-12B judge). Confirmed.
2. UoT ablation: C-UoT full preferred 58.3%, T-UoT 54.2%. Confirmed.
3. UoT Bridge T-UoT 0.680, Electricity 0.620; GPT-4o is the backbone for these tasks. Confirmed.
4. UoT token costs ToT 27.1k (7.4x), T-UoT 193.3k (52.5x). Confirmed. GLM-4-9B: OnePrompt first, 1560.4 / 46.3%. Confirmed.
5. UoT stage diagnosis strong transfer 52% vs 32%. Confirmed.
6. OMEGA (2506.18880): Zebra Logic 30%, +61 ID / +53 OOD; geometry +31 / +8; matrix-rank OOD 70% then a drop; DP solver 36 states at level 6. Confirmed.
7. Si et al. (2409.04109): novelty 4.84 / 5.64 / 5.81, 49 ideas per condition, 79 reviewers, 4000 seeds -> 200 non-duplicate, reviewer agreement 56.1% vs NeurIPS 66.0%. Confirmed.
8. Chakrabarty et al. (2309.14556): New Yorker stories pass 84.7% (11.9 of 14). Confirmed. The "3-10x fewer" figure is the paper's own abstract wording.
9. CreativeBench (2603.11863): Qwen2.5-7B Combo 9.21% / 0.168, Explore 4.11% / 0.0146; Flash-Lite 36.41% / 0.509 and 23.51% / 0.1681; GEPA 0.188 / 0.0182; EvoRePE 0.193 / 0.0169. Confirmed.
10. Bhushan et al. (2608.30047): alpha 0.724, judge r 0.732, H-creativity gold/silver/bronze 0.744/0.524/0.293, GPT-5 1.423. Confirmed. KOMBINE: 2,070 concepts, 412 reused (19.9%), 10-16 points, panel 75% unanimous (n=96) / 66% majority. Confirmed. Schaeffer et al.: pairs exceed 0.8 at 20% (LLM labels) and 32% (clusters); ratio 3.1 and 1.9. Confirmed.

## Corrections and wording fixes
- a21 says "One in five" and the paper says 19.9% at a similarity threshold; fine. The line "14x more likely" and "provider effect 2.3x" were not re-opened.
- Backbone is not stated in a12-a13: low-constraint tasks used GPT-4o (not Qwen3-14B); hypothesis tasks used Qwen3-14B. Any claim mixing them is wrong; claims K02 keeps them apart.
- a13/b10 name only the "Gemma-3-12B judge"; the other two judges give agreement 0.59-0.79 on rank contrasts (not on the 0.616/0.604 table values alone).
- c19 and a19: EvoRePE is "training-free steering" but needs weight access. K11 says so.
- b16 is a critical re-analysis, not a replication of the Hivemind data; it re-labels it "replication" only loosely.

## Duplicates (do not count as independent)
The three evidence files overlap heavily. Same paper, different ids: UoT (a11-14, b10-11, c05-09), OMEGA (a15-16, b06-07, c01-04), CreativeBench (a17-19, b08-09), Franceschelli and Musolesi (a01-03, b18, c10), Si et al. (b17, c17-18), Chakrabarty (b12, b26, c13). Claims count independent papers, not ids. Result: most Boden-typed LLM results rest on one paper each (UoT, OMEGA, CreativeBench, Bhushan, KOMBINE). None has been replicated by a different group.

## Contradictions between sources
- Hivemind (b15) says strong homogeneity; Schaeffer (b16) says real but 2-3x smaller than claimed. Verbalized sampling (c19) and random-prefix (b13) say it is fixable cheaply; Luo (b27) says gains cap at answer-space size.
- UoT says exploratory search is best with Qwen3-14B but the ranking flips on GLM-4-9B (plain prompt best). OMEGA says RL transfers within exploratory only. CreativeBench says scaling helps combination, not exploration. No single mode is "the answer".
- Franceschelli and Musolesi say transformational is out of reach; UoT T-UoT scored best on two low-constraint tasks. These do not conflict directly: the tasks are low-constraint and human-rated with 10 PhD students, so "transformational" there means rule change inside a prompt, not new conceptual space in Boden's sense.
- Judge reliability: Chakrabarty (LLM raters near zero correlation, 2024) versus Bhushan (GPT-5 judge Spearman 0.732, 2026). Task, model generation and rubric differ.

## Weak spots
- Boden (1990/2004), Wiggins (2006), Ritchie (2007), Lehman and Stanley (2011) were NOT opened (opened:false). Everything about them is second-hand.
- No human-subject study tests Boden's three types as categories. The "types" are used as labels on LLM operators, not validated as separable mechanisms. Claim K19 is therefore single-source at best.
- UoT task sets are small (3 tasks, 10 generations, 10 raters); HypoArena judge is a 12B model.
- Human creativity ratings and "novelty" in LLM benchmarks differ; CreativeBench Explore creativity is tiny in absolute terms (0.0146).
- AlphaEvolve and Sodarace need automatic evaluators; open-mode tasks usually lack one.
- Items c26-c29 were seen only in search listings, not read. b24, b25 are second-hand quotes. a24-a27 (Fanelli, Gangloff, Yu et al., Boriceanu) were read only for their positions; no numbers extracted.
- Arxiv ids in 2026 papers were taken from the evidence files and opened here; no independent check that these papers have been peer reviewed.

## GAPS
1. Does an explicit Boden-mode generator (combine / explore / rule-drop) beat a plain search wrapper at equal tokens on a second backbone and on tasks with a checkable answer (not only LLM-judged)?
2. Is there any independent replication of Universe of Thoughts, with a different judge family and a larger human panel?
3. When does rule-dropping (Denial Prompting, T-UoT) help versus hurt correctness, and what is the cheapest check that a "new rule" is still valid (G-level guardrail)?
4. How can the agent detect, without ground truth, which mode a task needs (constraint level routing), and how accurate is such routing?
5. What is a reliable, cheap novelty judge for conceptual (not stylistic) novelty, and how stable is it under paraphrase (Lu et al. 2026, Beaty AGC-Bench were only second-hand)?
6. Does verbalized sampling or a duplicate filter raise non-duplicate yield per token inside a scaffolded open mode, and where does the yield plateau (answer-space cap)?
7. Do the primary texts (Boden 2004; Wiggins 2006) define transformational creativity in a way that a prompt-level rule change can satisfy, or only changes of a representation (Schapiro et al. 2025 DAG model)?
8. Do humans show the same iteration pattern (novelty falls as performance rises) and is a scheduled explore-then-refine policy better than constant mixing for agents?
9. What do the unread items (TwistBench, Training Reasoning Models for diversity, long-tail output measure) report, and do they change K05, K09 or K14?

## Gap search results

Evidence in evidence_d.jsonl (d01-d19). Claims K21-K29 added; K09, K11, K12, K14, K15, K16, K17, K20 got new evidence ids and some wording. Limits of this pass: the web search quota ran out early; Semantic Scholar and OpenAlex rate-limited; only arXiv title/abstract pages and PDFs were readable.

1. Boden-mode generator vs plain search wrapper at equal tokens, second backbone, checkable tasks. STILL OPEN. Only new item is Magellan (d14): a search wrapper beat ToT on one 1.7B model with an LLM judge, no equal-token check. Long-tail paper (d01) adds that persona, branch-solve-merge, self-consistency and meta-prompting lowered quality in the novel region versus the plain model (K25).
2. Independent replication of Universe of Thoughts. STILL OPEN (negative search, d17, K24). No citing paper found.
3. Rule dropping: help or hurt correctness, cheapest validity check. LARGELY CLOSED for checkable code tasks (d08, d09, K21, K22): correctness falls with each added rule, divergence rises, stop after about 2-3 rules; check = unit tests plus a separate technique detector. For prose tasks no cheap check was found; Whiteboard (d10) shows humans license about one fifth of unsupported content, so a goal check is needed.
4. Routing by constraint level without ground truth. STILL OPEN. No paper on mode routing found. AGC-Bench (d05, K26) suggests backbone dominates, which explains the flips.
5. Cheap, reliable judge of conceptual novelty, stable under paraphrase. PARTLY CLOSED. AGC-Bench opened: register-only paraphrase moved scores +0.40/+0.52 on a 10-50 scale (d=0.15-0.29) on 50 cells (d06), but the judge agrees more with LLM gold (0.80) than human gold (0.65) (d07). Semantic entropy (d13) is a cheap judge-free diversity signal (rho 0.56 with humans). No test of conceptual (not register) paraphrase. Lu et al. 2026 execution audit still not located.
6. Verbalized sampling / duplicate filter yield and plateau. PARTLY CLOSED. Without memory, yield saturates near batch 60 and duplicate memory removes collapse (d11); self-rated obviousness filter is weak and overlaps 3% with dedup (d12); set prompting trades quality for distance (d03). Per-token yield was not reported anywhere; so no exact cost figure.
7. Primary texts and transformational definition. PARTLY CLOSED. Boden 1998/2004 and Wiggins 2006 could not be opened (d19, 403/404). Through Wiggins-coauthored work (d15) and Schapiro et al. (d16), transformation means editing the rule set or axioms; a technique ban is a weak form (K23, contested; the leaf-rule point is our inference).
8. Human novelty-performance pattern; explore-then-refine vs constant mix. STILL OPEN. DCE (d12) uses a 40/60 schedule with no comparison. No human study found.
9. Unread items. TwistBench: not found (d18). Diversity-training paper read (d02-d04): trained set-level reward gives CU 0.64 vs Opus 0.38, but it needs training; it supports K09/K14 direction (diversity can be fixed, judge is LLM) without changing them. Long-tail paper read (d01): supports K14 that creative scoring must look at quality in the tail; gives no mode-level result so K05 unchanged. AGC-Bench read (d05): general factor 81.5%; weakens any claim that mode differences are large across models.

Remaining priority gaps: 1, 2, 4, 8, and the TwistBench / Lu et al. 2026 items. Items 1, 2 and 8 need our own experiment.
