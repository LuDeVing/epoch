# Critique: Resilience engineering (E13.08)

## Corrections made (sources re-opened this session)

Re-opened full text of: Cemri et al. MAST (arXiv 2503.13657), Huang et al. (2310.01798), Laban et al. (2505.06120), tau-bench (2406.12045), Liu et al. resilience for embodied agents (2608.23839), Rabanser et al. (2602.16666, only partly), AIR (2602.11749), LoopBench (2601.05693), Moerman et al. (Springer PDF).

Confirmed: tau-bench gpt-4o pass^1 61.2 retail / 35.2 airline, pass^8 below 25%; Laban 39% drop, -15% aptitude, +112% unreliability, CONCAT 95.1%; Huang GPT-3.5 CommonSenseQA 75.8 to 38.1 (round 1) and 41.8 (round 2), GSM8K 75.9/75.1/74.7, GPT-4 GSM8K 95.5/91.5/89.0, debate 83.2 and 83.0 vs self-consistency 85.3 and 88.2, oracle GSM8K 75.9 to 84.3 and HotpotQA 49 to 59; Liu et al. 56.3% vs 55.8%, 57.3 vs 11.9 recovery cost, 59.11 to 33.73, 36.70 to 99.59, 11.6 to 36.3, Spearman 0.82; AIR 92.308% vs 80.952%, 97.727% vs 76.596%, 54 to 6 to 0; LoopBench 62.00%, 17.14% numeric, 44.86% statement, gemini-2.5-pro 7.43%; Moerman 176 items, S1 and S8 2%, S6 18%, 31% share.

Corrections and clarifications:
1. MAST category totals appear in two forms inside the same paper. Figure 1 gives system design 44.2%, inter-agent 32.3%, verification 23.5% (these match the per-mode sums in c02-c04). A later bar figure gives 41.8%, 36.9%, 21.3% (the numbers used in b06 and b23). Both are in the NeurIPS version; they likely count differently (modes vs failed traces). Claims cite both.
2. b06 listed "proceeding on wrong assumption 6.8%". The 6.8% mode is "fail to ask for clarification" (FM-2.2). Fix when merging.
3. Huang et al. Llama-2 numbers (b10) were not rechecked here. GPT-4 CommonSenseQA baseline is 82.0 and falls only to 79.5 and 80.0, so "fell" holds mostly for GPT-3.5.
4. a16 and a17/b17 and c21 are the same paper (Liu et al.) counted three times; independent_sources is 1 in the claims.
5. Rabanser metrics and the 15-model, p_fault 0.2 setup confirmed; per-model consistency values (0.52 to 0.86) still read from a garbled figure.
6. Dates: arXiv IDs 2602.* and 2608.* are 2026 papers; not independently verifiable by me beyond downloading them.

## Contradictions between sources
- Self-correction: Huang (2024) says no gain without outside feedback; Reflexion (c27, abstract only) reports gains. Reconciled by Huang's own point that gains need an external signal, but Liu and Meng (2026, abstract only) show a few newer models gain a little. Contested for new models.
- LLM monitors: loop reduction 52% on one task (Cognitive Companion) versus mean effect about zero over tasks; supporting probe results come from 35 examples with proxy labels.
- Multi-agent redundancy helps resilience (ResMAS) while G9 and Huang say debate does not beat sampling at equal cost. Different measurements (random failure vs accuracy at matched responses).

## Weak spots
- No source tests Woods's framework on LLMs with a control. The "learn, monitor, anticipate, respond" mapping is our own reading.
- Founding sources (Woods and Branlat 2011, Woods 2015, 2018, Hollnagel 2014 book, Rasmussen 1997, Carlson and Doyle 2000) were not opened: paywalls or 403. Claims on them rest on slides and citing papers.
- Single-author-group preprints (Liu et al.; AIR; Cognitive Companion; MTTR-A) with self-defined metrics and no replication.
- Many agent numbers come from simulated users or LLM judges (tau-bench, MAST labels kappa 0.77, MIRAGE).
- Resilience engineering evidence from health care is counts from single cases with no control (37 threats in 24 sessions).

## Seen only in snippets or abstracts
a19, a20, a21, a22, a23, a24, a25, b21, c09, c12, c25, c26, c27, c28. Reflexion (91% vs 80%) and Wang et al. (+17%, +24%) are abstract-level only.

## GAPS (most decision-relevant first)
1. Does the S6 impasse trigger (same error twice, no change for two rounds) fire early enough, and does the chosen operator actually change output? Measure fire rate and change rate on our own traces; compare with the 3-or-6-repeat loops in MIRAGE and MAST step repetition 15.7%.
2. Does pass^k (consistency over repeated trials) improve with the scaffold at equal tokens, or only pass@1? tau-bench-style test on our nano loop.
3. Is code-side loop detection (repeat hashes, no-progress counters) at least as good as an LLM monitor or hidden-state probe? Existing tests are tiny.
4. Do newer reasoning models still lose accuracy under blind self-review, and does a located-failure S5 revise beat it? Only abstract-level evidence for 2026 models.
5. Does a written lesson line (S9) reused later reduce repeat failures on held-out problems of the same class, and does a self-invented remedy lose to a rule-specified one as AIR reports (92.3 vs 81.0)?
6. Does recovery cost (tokens after a failed check) separate arms that have equal accuracy, as Reflexion vs CoPAL did? Test on our data.
7. Open the paywalled founding sources (Woods and Branlat 2011; Woods 2018 theorems; Hollnagel RAG) to check whether any states testable predictions about decompensation timing.
8. Is the MAST category split 44.2/32.3/23.5 or 41.8/36.9/21.3, and which counts traces vs modes? Check the dataset on Hugging Face.
9. Do the three Woods patterns map onto separable, countable failure signatures in single-agent traces (no multi-agent cross purposes), or collapse into loops plus stale assumptions?
10. Does stress or long-run drift (steps per solved item rising across a long session) appear for our agent, as Rasmussen/Cook predict for systems that lose buffers?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d17). Search budget was exhausted early (shared limit reached; arXiv, Semantic Scholar and OpenAlex APIs rate-limited), so some gaps got no new targeted search.

- Gap 8 CLOSED. Recounted the MAST-Data release (1642 traces, 1237 with a failure). Mode-share split is 37.0 / 33.3 / 29.9 (spec / inter-agent / verification); share of traces touching each category is 58.1 / 53.3 / 55.2. Neither paper split is reproduced; the release was re-annotated and step repetition is on 40.4% of traces, not 15.7%. Cite with version and counting unit (d01).
- Gap 4 PARTLY. Blind review still hurts non-thinking and open models (d02, d03, d10): single self-verification breaks 10.9% of correct answers; locating the first wrong step with a confidence exit gives net +3.9%, without it -49.3%. No frontier reasoning model tested blind; stays open for 2026 reasoning models (d17).
- Gap 5 PARTLY. Written lessons did not beat the raw failed transcript (-1.7 [-8.7,+4.9]) and need 100+ tasks to confirm 7-point effects (d06); unverified lessons carry the agent's own errors (d08); verified or trigger-fetched lessons did better and transferred to held-out tasks once (d09, d15). The AIR comparison of self-invented vs rule-specified remedy (92.3 vs 81.0) has no independent replication.
- Gap 3 OPEN. Only a different-system comparison (rule-based AgentGuard +52% on one benchmark, 0 on another; Sentry LLM detector larger) and no detector ablation (d05). Over-triggering hurts.
- Gap 1 OPEN. Change rate is evidenced (33.5% to 60.5%, d16); how early the trigger fires is not reported anywhere. Needs our own traces.
- Gap 2 OPEN. No source tests a scaffold on pass^k at equal tokens; tau2-bench shows pass^k falls with k (d11); EDV and EvoCUE report pass@1 only.
- Gap 6 OPEN (needs our data). Related: Sentry reports tokens 1.54x base (d04).
- Gap 7 OPEN. Woods 2018 is closed access (d14); RAG and other founding texts blocked.
- Gap 9 OPEN (our traces). Sentry splits failures into action validity, progress, reasoning and grounding (d05) which is a code-countable analogue, not Woods's three patterns.
- Gap 10 OPEN (our traces). No new source.

New claims K21 to K25 added; K08, K10, K11, K13, K14, K04, K06 extended; K14 changed to contested.
