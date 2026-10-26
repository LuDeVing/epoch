# Critique and cross-check: C03.03 Library learning

Cross-checker pass. I re-opened (pdftotext of the arXiv PDFs, this session) DreamCoder, Stitch, LILO, ReGAL, TroVE, LEGO-Prover, "Library Learning Doesn't", "LLM Library Learning Fails" and the compute-matched TroVE re-evaluation (arXiv 2507.22069). PDFs deleted afterwards.

## Checked and confirmed
1. DreamCoder SyGuS text editing: 3.7% (235 s) before, 79.6% (40 s) after, CVC4 82.4%, DreamCoder at large budget 84.3%. Confirmed. Library depth vs solved r = 0.79 and physics 93% of 60 laws after 8 cycles: confirmed.
2. LILO Table 1: DreamCoder 43.93/94.50/28.53, LILO 77.07/96.76/48.95, LILO std 14.14 on REGEX, max 93.20/99.03/73.87. Confirmed. -30.60/-2.91/-11.11 for raw Stitch abstractions: confirmed. GPT-4 compression 998/5250 = 19.01%: confirmed.
3. LILO costs (Table 6): LILO LLM search $1.77/$1.87/$2.01. Confirmed.
4. ReGAL Table 1: CodeLlama-13B 45.6 to 57.1 (LOGO), 42.8 to 68.9 (Date), 18.8 to 26.9 (TextCraft). Confirmed.
5. LEGO-Prover: valid 48.0 to 57.0, test 45.5 to 50.0, 22,532 skills, ablation 47.1 vs 50.4. Confirmed.
6. Replication: DSP 35.9 +/- 0.9 vs LEGO-Prover 25.8 +/- 1.6 (4o-mini); 23.1 vs 29.3; 19.4 vs 27.8; GPU budget ratios 5.84/5.94/14.23. Confirmed. Authors say the 4o-mini baseline is close to 38.5% reported for GPT-3.5.
7. Compute-matched TroVE (Table 6): MATH P@15 0.24 vs T@15 0.25; per-category algebra .27/.29, precalculus .15/.20, geometry .08/.08. Confirmed. P@1 0.14, original-paper primitive 0.12.
8. TroVE reuse: 3 successful reuses in 3,201 test questions. Confirmed.
9. Stitch headline "3-4 orders of magnitude faster, 2 orders less memory": confirmed.

## Corrections
- b09 (and the cost sentence in c06 is fine) mislabels costs. $1.16/$0.71/$2.07 are the enumerative-search cost rows (DreamCoder, and LILO's own enumeration part), not the LILO total. LILO LLM-search total is $1.77/$1.87/$2.01. Use a19 and claim K09.
- c08 says GPT-3.5 "LOGO 15.4 to 18.4". Wrong. In ReGAL Table 1 GPT-3.5 columns are LOGO 36.9 to 49.3, Date 88.9 to 90.2, TextCraft 15.4 to 18.4, MATH 43.2 to 55.4, TabMWP 87.4 to 89.2. So b14 is right, c08 mislabelled one cell.
- c23 says GPT-3.5 gains are only +1.3 to +3.0 "on LOGO, Date, TabMWP-class". Wrong for LOGO (+12.4) and MATH (+12.2). Gains are small only on Date (+1.3), TextCraft (+3.0), TabMWP (+1.8). The conclusion "gain shrinks for strong models" is weaker than c23 states. Claim K10 carries the corrected figures.
- a32 says "57.0% (from 52.4%)". The paper abstract says 48.0% to 57.0%; 52.4% is the Subgoal-Learning row (a second Subgoal row says 55.3%). Use c11.
- Stitch Table 2 range: a13/b11 say 0.24-77.26 s and 684 MB; c03 says 0.19-60.16 s and 714.55 MB. The PDF I opened (v2) contains both: the castles row of Table 2 shows 77.26 s and 683.89 MB, while the text summary says 0.19-60.16 s and 714.55 MB. The paper is internally inconsistent; I cannot tell which is right. Use "under 2 minutes, under 1 GB" only.
- b23/c13 write "45.5% (50% with human proofs)" as LEGO-Prover's claim. The replication paper does say that, but the original paper's test number is 50.0% at 100 attempts (45.5% is the previous best). Flag as a possible mis-citation in the replication paper; not resolved.
- TroVE author order is Wang, Neubig, Fried in a28/b18 and Wang, Fried, Neubig in c10. Cosmetic.

## Contradictions between sources
- LEGO-Prover authors: library ablation +3.3 points and 24% of solved problems used skills. Replicators: no cross-task reuse, baseline wins at equal compute with the weakest model, LEGO-Prover wins at equal attempts with stronger models. Not resolved (K15, K16).
- TroVE authors: 30-120% relative gain. Compute-matched re-run: about 1 point, not significant. A bug fix in TroVE's selection step shifts results too. The gain is a compute effect.
- LILO vs LAPS on LOGO: LILO authors could not reproduce LAPS's DreamCoder baseline (28.53 vs 42.64) and LILO's best (73.87) is below LAPS best (92.79). Cross-paper LOGO comparisons are unreliable.

## Weak spots
- DreamCoder, LAPS, Stitch, LILO share authors and benchmarks. Their agreement is one source for independence purposes (K01, K02, K05-K10 are single-source).
- Only babble (Cao et al.) independently confirms Stitch-style speed, and only from its abstract-level claim; its numbers were not re-opened.
- ASI/AWM/Voyager gains are not compute-matched and use different models. No one has run the "more samples, no library" control on them.
- ARC-AGI numbers (77.1% / 26.0%) are self-reported on a blog/GitHub; the library's contribution is not ablated against the model.
- Human prospective-compression study (b29) is N=60, two experiments, 2026 preprint.
- Tziafas robot library (b30): table numbers not extracted. Predecessor 2018 paper (a34) and human naming paper (a35) were seen as abstract pages only (opened:false). Search-snippet only: a37.

## GAPS
1. At equal total tokens, does an LLM agent with a verified helper store beat the same agent spending those tokens on extra samples plus voting? Only TroVE and LEGO-Prover were compute-matched, and both lost the gain. No compute-matched test exists for ReGAL, LILO, ASI, AWM or Voyager.
2. Does the benefit scale down with model strength (ReGAL: CodeLlama-13B +26 on Date, GPT-3.5 +1.3)? Needs a dose-response across at least three model sizes on the same tasks.
3. Where does the gain come from if direct reuse is near zero: self-correction, example diversity, or soft reuse? An ablation separating retrieval-as-callable, retrieval-as-example and random-example is missing.
4. Does LLM-driven abstraction work on ARC specifically, and with what transfer between tasks? ARC evidence is a 36-task study (16 to 22 solved) and a self-reported 77.1%/26.0% without ablation.
5. What is the right unit for an agent without a trainable recognition net: retrieval by description (LAPS, LILO AutoDoc), by embedding (Voyager), or by task signature? No head-to-head exists.
6. How should the store be pruned and when? TroVE trimming helps, ReGAL pruning helps under shift, but no study gives a size or usage rule. What use-count threshold is optimal?
7. Does prospective compression (helpers built for anticipated tasks, b29) beat retrospective compression for LLM agents when the task stream drifts? Only a human study of N=60 exists.
8. Does Stitch-style symbolic compression of an agent's own natural-language or code traces (not lambda programs) give useful helpers? Stitch has only been tested on typed lambda corpora.
9. Library poisoning and error propagation: ReGAL lists wrong helper code as an error class (7 of 13 reverse cases are connector code, 4 wrong/undefined functions). How often does a stored wrong helper cause a loss, and does verification prevent it?
10. Cost of library building amortised over task count: LILO is about 48 CPU-hours per iteration. At what number of reuse tasks does it break even in tokens for a single agent session?

## Gap search results

Evidence is in evidence_d.jsonl (d01 to d23). Claims K10, K12, K15, K17, K20 and K21 were edited; K25 to K33 are new. Web search was out of quota for part of the run, so some papers were opened by arXiv id directly.

**Gap 1 (equal tokens, helper store vs sampling plus voting): still open, with sharper guidance.** No new compute-matched study was found. New facts: Dynamic Cheatsheet beat 3-sample voting, but its own footnote shows 1,831 output tokens (DC-Cu) vs 370 baseline, and its instruction-only arm already took half the gain (d08). ArcMemo on ARC is closer to matched (retries and parallel samples), and the gain fades: +4.2, +0.7, +1.8 points over baseline at 0, 1, 2 retries, inside noise (d12). With a verifier, repeated sampling scales log-linearly (d23). The right baseline is verified resampling plus an empty-memory arm with the same instructions. Added K32.

**Gap 2 (does benefit shrink with model strength): partly closed, then reopened.** CRAFT confirms ReGAL's direction on two backbones: GPT-3.5 gains +10.4 / +18.0 / +15.2, GPT-4 gains +4.2 / +2.3 / +2.5 (d05). K10 is now established for that narrow claim. But Dynamic Cheatsheet shows the opposite when the model writes its own memory (small models gain little or lose; d07), Evo-Memory says small models gain most (d11), and SkillWeaver shows a weak model gains more from a library a strong model built (d16, d21). The answer depends on who builds the library. Still no three-size test on one task set. Added K25 (contested).

**Gap 3 (where does the gain come from if direct reuse is near zero): mostly closed for the "not a callable" part, open for the random-example control.** Verified prose in memory gets 39.0 vs 40.1 for a callable (d01); rule-based dedupe equals LLM abstraction on WebArena (35.6 vs 35.5; d02); callable workflows are used in 18.5% of tasks (d02); raw past experiences beat AWM and DC in an independent benchmark (d10); CRAFT without abstraction keeps most of the OK-VQA gain (d06). Counter: abstract workflows beat retrieved concrete examples on Mind2Web (d03). Verification is the strongest single factor. Nobody ran a random verified example as a control. Added K26 (established), K27.

**Gap 4 (LLM abstraction on ARC and transfer): weak evidence found.** ArcMemo is the only peer-style study: 100 tasks, three runs, gain of 7.5% relative at no retry that fades with compute (d12, d13). ARC Prize 2024 had no library-learning entry among its top results (d14). SOAR reaches 52% with fine-tuning, a route we cannot use (d15). The 77.1% / 26.0% claim (K21) is still self-reported without ablation. Cross-task transfer was not isolated. Added K30.

**Gap 5 (how to find a stored helper): partly closed.** Plain embedding retrieval over abstract items is weak: ArcMemo 0.26 to 0.22 (d13), ToolRet under 52% recall@10 on 43k tools (d19), CRAFT's single-view baselines 8 to 10 points below multi-view (d06). Name plus description plus problem text, or an LLM selection step, work better. No study compares description, embedding and task signature on one small agent store. Added K29.

**Gap 6 (when and how to prune): partly closed.** One measured rule: delete after at least 5 retrievals if mean downstream utility is below a threshold, plus a periodic sweep; memory shrank about 4x at equal score on three of four agents (d18). It needs a reliable per-use outcome, and with a weak LLM judge it hurt one agent. It is for episodic records, not helper functions. Added K28 (single-source).

**Gap 7 (prospective vs retrospective compression): still open.** No new study. Only the N=60 human result (K22).

**Gap 8 (Stitch on an agent's own traces): still open; weak negative evidence.** Leroy ran Stitch on 122 short Python programs and got 1.04x compression with most candidates pruned (d20). ATLAS compresses agent traces with an LLM plus automata, not Stitch, in one pen-testing case study (d21). Added K31.

**Gap 9 (how often does a wrong stored item cause a loss): partly closed for episodic memory, open for helper code.** Add-all memory fell below a small fixed memory on four of four agents, by 3.7 to 12.1 points (d17). Dynamic Cheatsheet reports uncurated append hurting (d09). Voyager's self-verification matters most (-73% items without it; d04). No study counts wrong-helper reuse for stored code. Added K27.

**Gap 10 (payback in tokens): still open.** No break-even curve exists. Reported savings are in steps (AlfWorld 22.6 to 11.5; ASI 15.3% fewer), while reasoning-model runs used equal or more tokens (d08, d12). Added K33.

**Corrections to the notes above.**
- LEGO-Prover (d22): the replication's "45.5% (50% with human proofs)" matches the original paper. The original gives 52.4 valid / 45.5 test with model-written informal proofs and 55.3 / 50.0 with human-written ones. The earlier correction a32 was itself wrong: 52.4 is LEGO-Prover's model-proof valid score, and Subgoal-Learning is 48.0 / 45.5. K15 stays contested because the 4o-mini reproduction did not match.
- ASI: the "23.5%" in its abstract is relative (40.4 vs 32.7), not points. The paper text says verification adds 4.2 points while its table shows 3.8 (36.4 vs 32.6).
- SkillWeaver (d16): its text calls 39.8% the WebArena GPT-4o gain, but that is the live-site figure. WebArena GPT-4o is about +32%.
- AWM (d02): its text says callable workflows leave task success at 3.2, but the table shows 3.6 vs 4.8.

**Status changes.** K10 single-source to established (narrowed). K17 single-source to contested (Evo-Memory finds AWM and DC no better than ReAct in embodied tasks). K15 note added. New: K25 contested; K26, K27, K29, K32 established; K28, K30, K31, K33 single-source.

**Still unanswered after this pass.** A compute-matched run of helper store vs verified resampling on one task stream; a three-size model test on one task set; a random-example control; an ARC test with at least 100 tasks and a no-memory arm at equal tokens; a prospective-compression test; Stitch on LLM traces; a token break-even curve.
