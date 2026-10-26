# Computational cognitive science: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the status in claims.jsonl as of 2026-10-26. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Only two of the field's ten subfields are researched, so this is a partial view. Many established claims are about LLM agent systems, not humans. Where a claim is about humans, it is a design hint until tested on our model. Both subfields stress one fact: the large effects come from one lab (Ellis/Tenenbaum for library learning, Lieder/Griffiths for strategy selection). Independent re-tests of the LLM library papers found the gain gone at matched compute.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 03 Library learning (DreamCoder, LILO and successors) | [DEEP](subfields/03_library_learning/DEEP.md) | 33 | 9 (4 contested, 20 single-source) |
| 06 Resource-rational strategy selection | [DEEP](subfields/06_resource_rational_strategy_selection/DEEP.md) | 22 | 6 (1 contested, 14 single-source, 1 hold) |
| **Total** | | **55** | **15** |

Each researched subfield has an UNKNOWNS.md with 15 test rows (30 in all).

Not yet researched (from SUBFIELDS.md): Bayesian models of cognition; program induction and language of thought; language-guided library learning (LILO is covered inside 03, but not as its own subfield); probabilistic programming; intuitive theories and simulation; metacognition models; LLMs as cognitive subjects. Note: SUBFIELDS.md lists "Language-guided library learning" and "Rational strategy selection" as separate rows, while the researched folders are 03 (all library learning, LILO included) and 06 (resource-rational analysis and strategy selection together).

## 2. Established findings, merged

Only claims with status established. "Yes" means the point is already in SCHEMA.md.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Reported gains of LLM library methods mostly vanish at matched compute. TroVE on MATH: primitive 0.24 vs TroVE 0.25, not significant. LEGO-Prover costs 5.8x to 14.2x the baseline per attempt, and the baseline matched or beat it at equal cost (4o-mini 35.9 vs 25.8). Memory-vs-sampling comparisons published so far are not compute matched (Dynamic Cheatsheet used about 5x the output tokens of its baseline, and its 3-sample vote is a weak control). With a verifier, repeated sampling scales log-linearly (15.9% to 56% from 1 to 250 samples) while voting plateaus. The right control for any store is verified resampling at equal tokens. | C03.03-K14, C03.03-K32 | G7, memory | partly (G7: must win at equal tokens, setup counted; no rule that the control is verified resampling) |
| F2 | Unverified accumulation hurts, and a verification gate is the most consistent single ingredient. Add-all episodic memory scored 3.7 to 12.1 points below a small fixed seed memory on all four agents. Append-all cheatsheet 26.7 vs curated 50.0 (Sonnet). Voyager without self-verification lost 73% of items. ASI unverified text 32.6 vs verified 39.0. Cheap LLM judges of memory quality were mixed. | C03.03-K27, C03.03-K12 | memory, G3 | partly (G3: pass on unfitted data; section 5 says a lesson is trusted after helping two problems; no admission gate for helpers, no ban on append-all) |
| F3 | Untrimmed libraries hurt. Always-add baselines made hundreds to thousands of tools and fell below primitive-only. TroVE kept 16/38/8 tools and matched CRAFT's 282/181/525. Pruning and small stores are needed. | C03.03-K12 | memory | no (lessons are one line; no size cap or prune rule) |
| F4 | Direct reuse of learned helpers is nearly absent in LEGO-Prover and TroVE. 1,233 of over 20,000 lemmas (6%) reached a prompt and one was reused verbatim. TroVE had 3 successful reuses in 3,201 questions. Blocking sharing cost 1 of 12 problems. Library growth is not library use. | C03.03-K13 | memory, section 6 log | no (section 6 logs operators, not helper reuse) |
| F5 | Most of the gain from stored experience survives without a callable abstraction. Rule-based dedupe matched LLM induction on WebArena (35.6 vs 35.5). Verified text in memory 39.0 vs 40.1 for a callable. Agents call workflow actions in 18.5% of tasks. Raw past experience beat AWM and Dynamic Cheatsheet in Evo-Memory. Counter: abstract workflows beat concrete examples on Mind2Web (+4.0 step success, gpt-3.5). No study compares callable, in-prompt example and random example on one task set. | C03.03-K26 | memory | no |
| F6 | Reasoning-based or multi-view retrieval beats a single embedding. ArcMemo embedding retrieval of abstract concepts dropped o3-mini 0.26 to 0.22. CRAFT without the function-name view lost 9.0 (GQA) and 6.6 (OK-VQA). ToolRet: all retrievers under 52% recall@10 on 43k tools. No head-to-head on one agent store. | C03.03-K29 | memory, S3 | no (S3 mentions retrieved analogues for open mode only) |
| F7 | A helper store helps weaker models more than stronger ones when it is built for or with a fixed backbone. ReGAL: CodeLlama-13B +26.1 on Date vs GPT-3.5 +1.3. CRAFT: GPT-3.5 +10.4 to +18.0 vs GPT-4 +2.3 to +4.2. Only two backbones per study. The sign flips when the agent writes its own memory (C03.03-K25, contested). | C03.03-K10 | memory, S0, G12 | no |
| F8 | Compression-based library learning scales: Stitch (top-down, pruned) is 3 to 4 orders of magnitude faster than DreamCoder's compression with equal or better ratio. babble (e-graphs) agrees. Both need typed lambda terms or an equational theory. Stitch on short Python reached only 1.04x (single-source C03.03-K31). | C03.03-K03 | memory | no (engineering fact; not transferable to prose, see section 6) |
| F9 | Adaptive allocation of reasoning effort or model choice, learned from logged outcomes, cuts cost at about equal quality across independent labs. ARES: Retail 54.8 = High 54.8 with 52.7% fewer reasoning tokens. RouteLLM: 95% of GPT-4 at over 2x lower cost. FrugalGPT: up to 98% cost cut. R2-Router: 4 to 5x cheaper. Thinkless: 50 to 90% fewer long chains. Most need training and an answer scorer, and some gains over fixed-high are small. | C03.06-K10 | S0, G12 | partly (G12 spends by difficulty; S0 is a placeholder, no learned gate) |
| F10 | More thinking is not always better, so fixed high effort is not the optimum. Airline High 38.0 vs Medium 42.0 (about 50 tasks). Named strategies did not beat no strategy (47.2% vs 45.1 to 49.0%). Beam search against a process reward model gets worse with budget on easy MATH bins. First solution round correct in over 92% of cases with under 60% of tokens. | C03.06-K11 | G11 | yes (G11 think briefly; 4b bars "slow down" prompts) |
| F11 | Asking the model to choose its own mode fails. Qwen3 judges chose reasoning 99.5 to 99.9% of the time (cost 6.25 to 19.07x all-instruct, accuracy equal to all-reasoning). GPT-5 as router 40.0 vs ARES 54.8. Direct LLM arm selection 82 vs LinUCB 89 (Game of 24). | C03.06-K12 | S0, G5 | partly (section 1 and G5: code decides; S0 is code-run lookup; no explicit ban on a model gate) |
| F12 | Bandit or UCB selection of thinking strategies per question beats CoT and best-of-N (Game of 24: 89 vs ToT 65; MetaScale Arena-Hard 93.14 vs 84.72). Both score rewards with an LLM or LLM judge, which G5 and G8 distrust. | C03.06-K16 | S6, O1 to O8 | partly (S6 picks an unused operator in code; tree ranked by test result; no learned operator preference) |
| F13 | On homogeneous streams a simple context-free per-mode average ties or beats feature-based metareasoning (MSE 0.0050 vs 0.0048 in 2015; BIC 60.70 vs 68.94 in 2017). Features pay only when classes mix. The two papers disagree on how close the tie is. Human data on a small task. | C03.06-K03 | S0 | partly (class record exists [D]; no rule on when to add features) |
| F14 | Pure cost-benefit and pure reinforcement accounts each fail a human test. People start with the costly full-information strategy and switch slowly and asymmetrically after an environment change (27% moved to compensatory, 65% to TTB). Reanalyses by the SSL author. Human only. | C03.06-K04 | S0 | no (design hint: expect slow adaptation, add forgetting) |

## 3. Contradictions between subfields

| # | Point | Side A | Side B | Reading |
|---|---|---|---|---|
| C1 | Does a library help at all? | Original papers: ASI 40.4 vs vanilla 32.7; LEGO-Prover 48.0 to 57.0; TroVE 30 to 120% relative (C03.03-K17 contested, K15 contested, K12 single-source reading). | Compute-matched re-tests: TroVE +1 point, not significant; LEGO-Prover baseline wins or ties (C03.03-K14 established). Evo-Memory: AWM no better than ReAct (K17). | Treat every published store gain as unproven until a verified-resampling arm at equal tokens exists. Evo-Memory authors re-implemented the methods and have their own, so the counter-evidence is itself not clean. |
| C2 | Who gains from a store? | Weak models gain more when the library is built for them (C03.03-K10 established). | When the agent writes its own memory, a small model can fall (GPT-4o-mini 16.7 to 13.3; Haiku gain mostly from instructions alone) while Evo-Memory says small models gain most (C03.03-K25 contested). | Probably "who builds" decides, not "who uses": a strong builder and a weak user is the safe case (SkillWeaver, ATLAS, C02.03-K29). Open. |
| C3 | Abstract vs concrete memory | Abstraction helps on Mind2Web (+4.0 step success) and DreamCoder's compression beats memorising (C03.03-K26 counter, K02). | Raw experience retrieval beats AWM and Dynamic Cheatsheet in Evo-Memory; rule-based dedupe equals LLM induction (K26). | DreamCoder's memorise baseline pollutes the primitives of an enumerative search; an LLM reads examples in context. Different mechanisms. |
| C4 | Learned routers vs "models cannot route" | Trained routers on logged outcomes cut tokens 42 to 53% at equal quality (C03.06-K10). | Asking the model itself picks the long mode 99.5 to 99.9% and a GPT-5 router loses 14.8 points (C03.06-K12). | Consistent once split: the mode choice must come from logged outcomes in code, not from a prompt. But K10 routers are trained neural models, not tables; the table form is untested (C03.06-U1). |
| C5 | Can difficulty be routed cheaply? | Five difficulty bins beat uniform allocation by about 4x (C03.06-K20 single-source). | Within C01: coarse bins are cheap, fine bins need about 16 samples, and routing can lose to a fixed policy (C01.08-K20 contested). In A04: the router classifier is only 54.5% accurate (A04 F9). | Bin quality is the limit. 2048 pre-samples per question were not counted in K20. |
| C6 | Chunk or helper transfer | C02.03-K01 (Soar chunking): large same-task speed-up. | C02.03-K03: only 10.3% of chunks transferred. C03.03-K13: 6% of lemmas reached a prompt; reuse near zero on math and proofs; C03.03-K17: ASI reuses a skill in 42.5% of cases. | Reuse is high on repeated templates (web) and near zero on one-off reasoning. Same-task repeat is not cross-task transfer. |
| C7 | Store size | C03.03-K12: bigger stores hurt, prune. | C02 F15 (SkillsBench): 1 to 3 skills gain +17.8 to +18.6, 4+ skills gain +5.9 (v1; the v4 re-run shrinks it further). | Agree. Both say keep the store small. |
| C8 | Spend by difficulty vs more thinking helps | C03.06-K11 and C01 F10: first round right in over 92% of cases; cap and restart. | C03.03-K32: instruction-only and memory arms use more tokens (DC-Cu 1831 vs 370) for gains. | Not a conflict: gains at 5x tokens are not evidence for memory (see F1). |
| C9 | Cue direction | C03.06-K14 (single-source): sign of entropy/benefit link flips across 12 environment-backbone pairs. | G1 uses "the impasse detector fires" as a fixed signal. | Do not hard-code cue signs; estimate per class (C03.06-U7). |

## 4. Recurring mechanisms

| Mechanism | Where it shows | Why it matters for the schema |
|---|---|---|
| A table keyed by class, updated from logged outcomes, decides what to do next | 06 (class table, Thompson sampling, F9, F11, F13); 03 (retrieval index from which helpers solved which task; S0 store gate) | One machinery can drive both S0 (mode) and memory (which helper to offer). Code, not the model, owns it (G5). |
| Verify before you keep | 03 (F2, execution gate, held-out check); 06 (code-checked reward is required; LLM-scored rewards distrusted, F12) | Same rule as G3 and G2: the check, not the model's opinion, is the signal. |
| Cost must be counted against gain | 03 (F1, setup tokens, break-even unknown); 06 (VOC = reward minus lambda * cost, F9) | G7 and the VOC formula are the same idea. Library upkeep is part of the cost side. |
| Forget or prune | 03 (F3, prune after 5 retrievals, single-source C03.03-K28); 06 (decayed Beta or windowed UCB, single-source C03.06-K19) | A store or a table that never forgets stops exploring or fills with stale items. |
| Gain depends on repeated structure | 03 (task similarity Pearson 0.56 to 0.72, single-source; reuse near zero on math); 06 (features pay only in mixed streams, F13) | Both need a cheap test for "is this class repetitive or mixed" before spending. |
| Strong builder, weak user | 03 (F7, SkillWeaver, ATLAS); C02.03-K29 | A strong model can write the store once; a weak model reads it. |
| Effort tracks difficulty, but the model cannot report difficulty itself | 06 (F10, F11); 03 (stored items copied by similarity, "experience-following") | The difficulty signal comes from the running class pass rate, not from model opinion. |
| Names and readable keys | 03 (anonymous items hurt, single-source C03.03-K05; function-name view in retrieval, F6) | Every stored item has a readable name and one example. |

## 5. Merged tests

All arms at equal total tokens, setup and upkeep counted (G7). Per-claim detail is in each UNKNOWNS.md.

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1 Store vs verified resampling, with break-even | C03.03-U1, C03.03-U9 | On a repeated class (100+ items, held-out half): plain vs plain + extra verified resamples vs store; plot cumulative tokens vs items solved. | High |
| T2 Callable vs example vs random example vs none | C03.03-U2 | Same stream as T1: callable, same source as example text, random verified example, empty memory with identical instructions. | High |
| T3 Store by model size and by builder | C03.03-U3 | Three sizes, 60+ items: empty memory, self-built store, store built by the strongest. | High |
| T4 Entry gate, doc check and prune rule | C03.03-U4, C03.03-U5, C03.03-U6 | Add-all vs run-gated vs run-gated + held-out; name vs name + doc + doc-check; no prune vs random prune vs use-count rule on a 200+ item stream. | High (gate), Med (prune, doc) |
| T5 Retrieval head-to-head | C03.03-U7 | BM25 on name + doc + problem vs embedding vs task signature vs BM25 top 10 + model pick on a 20 to 100 helper store. | Med |
| T6 Class table vs fixed modes (plus model-gate arm) | C03.06-U1, C03.06-U2, C03.06-U3, C03.06-U6 | Mixed stream, 4+ classes with different best modes: always-direct, always-checked, always-step, class table, model-chosen mode; add cue-keyed vs feature-free and fixed vs dual-variable lambda. | High |
| T7 Forgetting rule by log replay | C03.06-U4, C03.06-U15 | Replay logs with a mid-log shift; no decay vs window vs Beta decay (gamma 0.01, 0.05) vs reset; record recovery asymmetry by shift direction. No model calls. | High |
| T8 Short vs long per class and free difficulty | C03.06-U5, C03.06-U9, C03.06-U10 | Per class, three token caps, 3 runs per item; compare difficulty from running class pass rate vs 8 and 32 pre-samples vs uniform cap. | High |
| T9 Store-use gate at S0 | C03.03-U10 (with C03.03-U3) | Pairwise class similarity vs store gain across high- and low-similarity streams; use the T6 table to decide "build a store or not". | Med |
| T10 Cue direction stability | C03.06-U7 | Paired runs with and without extra compute per class; hard-coded vs learned cue sign vs always-trigger. | Med |
| T11 Oracle gap vs sampling noise | C03.06-U8 | 3 runs of one mode vs one run each of 3 modes; compare any-of-3 and vote at equal samples. | Med |
| T12 Process-level log | C03.06-U11 | Replay: table built from pass/fail only vs pass/fail + tokens after first correct candidate + cheapest passing mode. | Med |
| T13 Hypothesis-first | C03.03-U8 | Abstract rule in words then code vs direct samples at equal tokens, 100+ ARC-style items. | Med |
| T14 Operator bandit and cost-aware impasse trigger | C03.06-U12, C03.06-U14 | At S6: uniform vs LLM-chosen vs Thompson with pass-on-subgoal reward; fixed trigger vs expected-gain minus lambda*cost. Likely data-starved (impasses about 8% of problems). | Med/Low |
| T15 Low-priority variants | C03.03-U11, C03.03-U12, C03.03-U13, C03.03-U14, C03.03-U15, C03.06-U13 | Prospective helpers; stepwise hint feeding; mechanical dedup; softmax sampling and hindsight relabel; easy-first order; fifth mode in the table. | Low |

Suggested order: T7 and T8 (no or cheap model calls) first, then T6, then T1 with T2.

## 6. Not to add

| Idea | Why not | Status |
|---|---|---|
| Neural recognition model, dreaming, DreamCoder-style training from scratch | Need weight training and millions of tokens (about 5 days on 64 CPUs). Our scaffold does not train. | single-source C03.03-K01 (one group); cost single-source C03.03-K09 |
| Stitch or lambda-calculus compression on prose traces | Needs typed terms; 1.04x on short Python; untested on traces. | engineering fact established (F8); transfer failure single-source C03.03-K31 |
| Asking the LLM to do the compression step | GPT-4 gave 19.01% valid abstractions at about 1.0x compression. Do it in code. | single-source C03.03-K04 |
| Anonymous library items | Lowered LILO's solve rate (-30.60, -2.91, -11.11); readable name + example needed. | single-source C03.03-K05 |
| Append-all memory or an unbounded store | See F2, F3. | established C03.03-K12, C03.03-K27 |
| Callable helpers as the default form | About 1 point over verified text; called in 18.5% of tasks (F5). | established C03.03-K26 |
| Counting library gain from papers that are not compute matched | See F1. | established C03.03-K14, C03.03-K32 |
| Letting the model pick its own mode or effort | See F11. | established C03.06-K12 |
| Naming a strategy in the prompt ("use supposition-following") | No gain over no strategy. | established C03.06-K11 |
| Fine-tuned effort routers (ARES, RaM) | Need training per setting; closed to a scaffold. Use only the idea (a table from logged outcomes). | established C03.06-K10; RaM single-source C03.06-K09 |
| Full BMPS metalevel policy | Needs an exact model of the agent's own belief updates. | single-source C03.06-K18 |
| LLM-scored or LLM-judged rewards in a strategy bandit | G5 and G8. | established C03.06-K16 |
| Online discovery of new modes | Humans find a new useful strategy in 28.57% of cases after 120 trials. Keep a small fixed set. | single-source C03.06-K08 |
| Small single-author router numbers (n=50 or one run) | Within noise. | single-source C03.06-K17 |
| Self-reported ARC 77.1% / 26.0% as proof of library learning | No library ablation. | single-source C03.03-K21 |
| Fine-tuning routes (SOAR 52%, test-time training 53.5%) | Need weight updates. | single-source C03.03-K30 |

## 7. Gaps

- **Eight of ten subfields unresearched** (section 1). Program induction and language of thought, and Bayesian models, may feed S2 REPRESENT and S3 GENERATE and are not covered.
- **No independent replication of DreamCoder-style gains.** All large numbers come from one group (C03.03-K01, K02, K05 to K09 single-source).
- **No independent replication of the 2017 human strategy-selection experiments.** The search was blocked (C03.06-K22 on hold). Absence of evidence only.
- **No token break-even curve for a store** (single-source C03.03-K33). Reported efficiency is in steps, not tokens.
- **The pure Lieder-Griffiths form (per-mode reward and time regression with Thompson sampling) has not been run on an LLM with code-only rewards.** Established routing work (F9) uses trained routers.
- **Model-strength effect for self-built memory is contested** (C03.03-K25) and no study uses three sizes on one task set.
- **Class keys for new items.** How to assign a class to an unseen item cheaply is unsolved (S0 slot in SCHEMA section 7).
- **Wrong stored helpers.** Harm is counted only for episodic memory, not helper code.
- **Retrieval on a small store.** No head-to-head of description, embedding and task signature (F6).
- **Single-source claims that matter and need tests:** hypothesis-first (C03.03-K19), pruning rule (C03.03-K28), forgetting (C03.06-K19), difficulty bins (C03.06-K20), lambda from the budget (C03.06-K21), cue direction flips (C03.06-K14).
- **Cross-field overlap to reconcile later.** C02.03 (Soar chunking, SkillsBench) and C01.08 (adaptive compute) repeat parts of F2 to F7 and F9. The merged tests T1, T2 and T6 should be run once and credited to all.
- **Evidence quality.** Several LLM routing papers are 2026 preprints on small test sets or LLM-judged rewards (C03.06 DEEP section 5.7). Treat their numbers as directions, not targets.

**Audit (code check, 2026-10-26):** C03.03-K13, C03.06-K03 had only one opened source and are now single-source, not established. Treat their rows above as unconfirmed.
