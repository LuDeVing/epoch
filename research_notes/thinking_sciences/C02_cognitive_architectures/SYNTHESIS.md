# Cognitive architectures: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl, set before the stricter independence re-check. Treat each row as a candidate until that check is done. Many "established" claims here are about LLM agent systems or Soar design facts, not about humans. A Soar design fact (K01, K02, K05) tells us how a mechanism is built. It does not show the mechanism helps an LLM agent. Schema column checked against `research_notes/single_agent/SCHEMA.md` (S6, SUBGOAL, section 5 Memory, S9, G1 to G12).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Soar: operator selection and impasses | [DEEP](subfields/01_soar_operator_selection_and_impasses/DEEP.md) | 31 | 8 (2 contested, 21 single-source) |
| 03 Soar: chunking and learning from impasses | [DEEP](subfields/03_soar_chunking/DEEP.md) | 30 | 9 (5 contested, 16 single-source) |
| **Total** | | **61** | **17** |

Each has a UNKNOWNS.md (13 and 14 test rows, 27 in all).

Not yet researched (from SUBFIELDS.md):

| Subfield | Planned use |
|---|---|
| 02 Soar: impasse types (folder missing; partly absorbed by 01, which covers the type count and constraint-failure) | S6 typed triggers |
| 04 Soar: other memories and RL (episodic, semantic, operator preference learning) | memory, S0 class record |
| 05 ACT-R: production selection (utility) | operator choice by success rate |
| 06 ACT-R: declarative memory (activation) | memory ranking |
| 07 ACT-R: production compilation (only touched through C02.03-K07) | lesson to routine |
| 08 Hybrid and connectionist (CLARION, Sigma) | background |
| 09 Global workspace, LIDA | background |
| 10 Language agents as architectures (CoALA, 2026 review) | design check; only touched through C02.01-K18 and C02.03-K21 |

## 2. Established findings, merged

Only status established. Most gain evidence is from one benchmark per system; read each row as a design hint.

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | A Soar impasse is raised by a fixed rule on the preference outcome, not by the system judging its own progress. | C02.01-K01 | S6 | yes (S6 "fired by code") |
| F2 | Model-side signals of being stuck are unreliable. Reasoning models spend 2x to 4x tokens on unsolvable questions and rarely abstain. Code-visible triggers plus a budget cap are favoured. | C02.01-K27 | S6 trigger | yes (S6 notes the unreliable "stuck" signal) |
| F3 | The number of impasse types is not canonical (3, 4 or 5 by source). Type impasses by what our checks can detect. | C02.01-K02 | S6 | partly (S6 has trigger types, no typing rule) |
| F4 | A Soar substate is isolated. It reads the superstate, runs its own cycle and returns only results, with the superstate facts that justify them. | C02.01-K05 | SUBGOAL, G3 | partly (SUBGOAL re-enters S1; S3 fresh context per attempt; no "return one typed line" rule) |
| F5 | LLM agents rarely have a typed impasse, an isolated substate and a compiled resolution as one package. | C02.01-K18, C02.03-K21 (single-source) | S6 | yes (S6 is that bundle; marked planned) |
| F6 | Self-correction without external feedback does not help (GSM8K 75.9 to 74.7, CommonSenseQA 75.8 to 41.8). Checks grounded in an executor or in the agent's own knowledge do. | C02.01-K13 | S5, G2, G1 | yes (G2, 4b) |
| F7 | The quality of the diagnosis is the bottleneck of generate-critique-repair loops. Stronger or human feedback beats own-feedback repair. | C02.01-K22 | S6 operator choice | partly (G2 needs real failing output; no diagnosis-accuracy check) |
| F8 | Impasse-time LLM calls compiled into reusable rules cut later LLM use. | C02.01-K09 | memory, S0 | partly (subgoal library "planned") |
| F9 | Chunking compiles a subgoal result into a rule whose conditions are only the pre-goal facts accessed. Same-task speed-up is large (R1-Soar 1731 to 485 decisions, 7 on rerun). Both sources are from the Soar group. | C02.03-K01 | memory | partly (library planned; no accessed-facts key) |
| F10 | One stored rule can cost more to match than it saves (3.1x slower in one case; over 8 million partial matches in another). Stores need a net-value rule. | C02.03-K04 | memory, G7 | partly (G7 general; no entry-level net-value rule) |
| F11 | Learned entries can be over-general and fire where the original reasoning would not. Causes include a missed near-satisfied condition and untracked random choices. | C02.03-K06, C02.03-K25 | G3, memory | partly (section 5 trusts a lesson only after 2 helped problems; no precondition check) |
| F12 | Wrong application of a stored entry is measurable. Looser keys raise hit rate and cut accuracy on hits (85.5 to 77.0). | C02.03-K25 | memory, S4 | no |
| F13 | Verifying a candidate by execution before storing it helps (Voyager -73% items without self-verification; verified beats unverified in ASI). | C02.03-K10 | memory, G3 | partly (G3 pass on unfitted data; no admission rule) |
| F14 | Adding every experience makes agents worse than a small fixed store; agents copy the outputs of similar stored items. | C02.03-K11 | memory | partly (lessons are one line; no size cap) |
| F15 | Short, compact skills beat comprehensive documentation (+17 to +19 vs -2.9). One to three skills beat four or more. | C02.03-K14 | memory | partly (one-line lessons) |
| F16 | A learned library can be handed to another agent. Gains are partial. | C02.03-K16 | memory | no |
| F17 | The maker of reusable entries must be strong. The user can be weak. | C02.03-K29 | memory | no |

## 3. Contradictions between subfields

| Topic | Side A | Side B | Resolution |
|---|---|---|---|
| Does revising help? | C02.01-K13: no gain without external feedback. | C02.01-K12 (STARS +25 to +57 points), K14 (critic worth 23 to 37 points). | Both agree once "grounded" is the split. STARS tokens are 3.4x to 5.9x baseline with no equal-token control, so the gain is not shown to beat resampling. |
| Repair vs resample at equal samples | C02.01-K12, K14, K15 favour repair loops. | C02.01-K23 (contested): code gains modest or absent; math wins only with a fine-tuned reviser and verifier. | Open. Tested in C02.01-U5. |
| Value of a stored library | C02.03-K08 (contested): AWM +12.0 points on GPT-4, +3.6 on Claude-3.5, a loss on Claude-3.7. C02.01-K28 quotes +51.1% relative. | C02.03-K16 and K29: weak models gain from strong-made stores. | Gain is gated by base model and by repeated structure (C02.03-K28). The +51.1% in C02.01-K28 and C02.03-K08 is the same AWM figure; do not count it twice. |
| Self-written skills | C02.03-K12 (contested): self-written about no gain (-1.3, -1.8). | C02.03-K10: execution-checked self-induction helps on web tasks. | Split is unverified vs executed. Reasoning items often lack a cheap execution check (C02.03 open questions). |
| Chunk cost | C02.03-K04: single rules can erase the savings. | C02.03-K05 (contested): average match cost flat over 10,112 chunks, though wall-clock per cycle still rose. | Real for single rules, not for the average rule. C02.01-K21 sides with K04. |
| Chunk transfer | C02.03-K01: large same-task gain. | C02.03-K03: only 10.3% of chunks transferred. | Gain is mostly same-task repeat. Cross-problem transfer is small. |
| Constraint-failure | C02.01-K03 (contested): Laird 2022 says all impasses can be removed by preferences; the Manual says not constraint-failure. | none | Manual wording taken. |
| Learning curve form | C02.03-K02 (contested): power law in Soar's averaged curves. | Human data: exponential at the individual level. | Averaging biases toward a power law. Fit per run (C02.03-U13). |
| Failure lessons | C02.03-K17 (contested): AWM -2.2, ReasoningBank +3.2, ExpeL +11 to +19. | | Depends on how memory is written. |

With other fields. A01 F10 (refinement patches and plateaus after about 2 rounds) and F12 (LLMs rarely find falsifying cases alone) agree with C02.01-K13 and K22. A01 F19 and F20 (more thinking can lower accuracy) agree with C02.01-K17 and K30 (gate search, cap depth). No conflict found. C02.01-K27 (model stuck signals unreliable) fits A01 F1 (confidence does not signal doubt).

## 4. Recurring mechanisms

| Mechanism | Where it shows up | Reading |
|---|---|---|
| Code decides, not the model | K01, K27 (trigger); C02.03-K10 (admission); K22 (diagnosis) | Same as G1, G2, G5. |
| Isolate, then return one short result | C02.01-K05, K24, K25 | Stated as Soar design; LLM evidence is single-source. |
| Verify before you store or trust | C02.01-K13, K14; C02.03-K10, K25 | The one rule behind both subfields. |
| Small, selective stores beat big ones | C02.03-K11, K14, K04; C02.01-K21 | Cost of use grows with size. |
| Gain is gated by the base model and by repeated structure | C02.03-K08, K28, K29; C02.01-K10 | A store or loop is worth it only on recurring classes. |
| Part of any gain is a format effect | C02.03-K23 (empty-memory control gave about half the gain) | Every store test needs a same-instruction empty arm. |
| Write on a miss or a resolved failure | C02.03-K22, K20; C02.01-K09 | Candidate rule, never compared (C02.03-U1). |

## 5. Merged tests

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T1 Impasse base rates and trigger false alarms | C02.01-U4, U3 | Log-only pass on all items; hand-label 100+ stall events; score precision and recall of each trigger. | High, run first |
| T2 Fresh vs shared context in a subgoal | C02.01-U2, U10, U12 | S6 events, arms: fresh context with typed result, shared context, no subgoal; add a depends_on arm. | High |
| T3 Typed vs generic recovery | C02.01-U1, U6 | Seeded cases per type; arms generic, typed table, random-typed; include contradictory constraints with exit. | High after T1 |
| T4 Repair vs best-of-N at equal tokens | C02.01-U5, U7, U11 | By difficulty bin; arms best-of-N plus check, repair loop, mix; add a gated-lookahead arm. | High |
| T5 Does a store help at all | C02.03-U5, U14 | Store vs same-instruction empty vs random entry; strong and weak base; split by class recurrence. | High, first for memory |
| T6 Admission rule and net token value | C02.03-U2, U4, U1, C02.01-U8, U13 | Append-all, execution-verified, outcome check, count threshold, write-on-resolved-impasse, typed library; log authoring and use tokens. | High |
| T7 Precondition check before reuse | C02.03-U3, U6, U8 | Seeded entries missing one precondition; arms no check, model check, code check; key by text vs accessed facts; literal vs slots. | High |
| T8 Store maintenance | C02.03-U9, U12, U13, U11 | Inject wrong entries at 0 to 25%; arms delete, repair, append lesson, probation; failure lesson vs raw trace; growth curve per run. | Med |
| T9 Grain and caps | C02.01-U9, C02.03-U7, U10 | Depth and token caps per subgoal; per-subgoal vs per-task entries; cached impasse decision. | Med |

## 6. Not to add

| Idea | Why | Claim ids |
|---|---|---|
| Model-stated "I am stuck" as a trigger | Unreliable; code triggers are favoured. | C02.01-K27 |
| Revision from the model's opinion with no real output | No gain without external feedback. | C02.01-K13 |
| Store every experience | Below a small fixed store on four agents. | C02.03-K11 |
| Long comprehensive skill documents | Net loss in SkillsBench. | C02.03-K14 |
| Unverified self-written skills | About no gain on average (contested). | C02.03-K12 |
| Typing impasses by Soar's count | Count is not canonical; type by what checks detect. | C02.01-K02 |
| Wider candidate trees without a repair step | No gain in STARS data (single-source). | C02.01-K11 |

Most of these repeat 4b. Only the store rules and the Soar-count point are new.

## 7. Gaps

- Most findings come from one lab per system (CogRec, NL2GenSym, STARS). None was replicated (C02.01-K31).
- No study compares an impasse-driven LLM agent with a plain one at equal tokens.
- Typing the impasse has no LLM test (C02.01-K19).
- No published precision and recall for stuck triggers (C02.01-K26).
- Subfields 02 and 04 to 10 are not researched. ACT-R utility, activation and compilation remain open.
- Human data on impasses and learning curves read as abstracts only.
- Our bench lacks long-horizon tasks, tool failures and a store large enough to see retrieval cost.
