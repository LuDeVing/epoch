# Chess and game expertise: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the status in claims.jsonl (two or more independent sources), after the source audit of 2026-10-26. Most chess findings are about humans; for the agent they are design hints until tested on our model. Many LLM findings here come from 2026 preprints. Contested and single-source claims are named only where they matter. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2.

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Thought process and progressive deepening | [DEEP](subfields/01_thought_process_and_progressive_deepening/DEEP.md) | 23 | 9 |
| 05 Chunks and templates | [DEEP](subfields/05_chunks_and_templates/DEEP.md) | 26 | 11 |
| **Total** | | **49** | **20** |

Contested: 10 (01: K02, K06, K07, K10, K22; 05: K05, K08, K10, K22, K26). Single-source: 19 (9 in 01, 10 in 05). Each subfield has 14 test rows in UNKNOWNS.md (28 in all).

Not yet researched (from SUBFIELDS.md): computational chunk models (EPAM, CHREST), pattern-recognition theory of search (touched in E16.05-K10, E16.01-K17), recognition-primed decisions (Klein), Einstellung as its own subfield (only E16.01-K08, single-source), computer chess and game AI (alpha-beta, MCTS, AlphaZero; only E16.01-K11 touches it), deliberate practice (low value). Folders 02 to 04 and 06 to 10 do not exist yet.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Human experts at every level go back to a move and look at it deeper. About 4 re-investigations per protocol; the pattern held in a second sample. It is normal, not a flaw. | E16.01-K01 | S4, S5 | partly (S5 has revise rounds and S6 subgoals; no revisit policy) |
| F2 | On an easy position solvable within about 9 plies, maximum depth, node count, nodes per minute and rate of generating moves do not reliably separate grandmasters from experts or Masters from weaker players, while move quality differs a lot. Mean depth shows only a small but significant slope of about 0.6 ply per 200 Elo (Masters 5.0 vs Class B 2.9 plies, only that pair reliably different). Do not copy "search deeper" as the expert trait. | E16.01-K03 | S4, G12 | partly (G12 spends by difficulty) |
| F3 | Skill is more than search. Elo still explains 17.6% of move quality after removing depth and nodes, and experts judge positions well after 5 s. Stored pattern knowledge acts before and instead of search. | E16.01-K05, E16.05-K13 | memory, S0 | partly (section 5 memory is a planned slot) |
| F4 | Asking a model to re-read and revise with no outside signal does not help and often hurts (GSM8K 95.5 to 89.0; CommonSenseQA 75.8 to 41.8). A revisit needs new information from a tool or check. | E16.01-K09 | G2, S5 | yes (G2; section 4b unstructured self-reflection) |
| F5 | Explicit tree search with evaluation, pruning and backtracking beats flat chain of thought at comparable tokens on lookahead tasks (Game of 24: 74% vs 49%; crosswords 60% vs 20% with no backtracking; MCTS adds about 68 Elo to a small chess model). | E16.01-K11 | S6, section 4 tree rules | partly (tree only at impasse; G12 limits search to where there is a foothold) |
| F6 | Spending more tokens on hard items and fewer on easy ones beats uniform spending. Four first samples and their disagreement are a cheap difficulty signal (+2.3% on average over uniform; 14 of 15 settings). | E16.01-K21 | G12, S0 | yes (G12) |
| F7 | How far the written trace drives the answer depends on the task (under 10% on three tasks, over 60% on AQuA). Planning and backtracking sentences have the most effect. Reasoning text is not evidence. | E16.01-K19 | G10, S4 | yes (G10) |
| F8 | General chat LLMs are weak at chess decisions; thinking helps much (ChessQA +14.7 points; GPT-5 79.3% with vs 44.0% without). No LLM beat a weak engine; board-state errors lead. | E16.01-K12 | none | no (domain fact; chess is a poor test bed for a text scaffold without an engine) |
| F9 | Training on search traces with dead ends and backtracking beats training on optimal paths (Countdown 51.3% vs 25.7%). Training only. | E16.01-K14 | none | no (see section 6) |
| F10 | Expert recall depends on meaningful structure. Large edge on real positions; small but real edge on random ones (r = .41, .29 after bias correction). The old "zero edge on random boards" is wrong. The meta-analysis shows high heterogeneity (I2 63%). | E16.05-K01 | memory (background) | no |
| F11 | Chunks are small groups found by a gap of about 2 s, mostly structural (pawn chains, castled kings). Absolute chunk size depends on the display medium (the 2 s boundary holds on physical boards). | E16.05-K02 | none | no |
| F12 | Chunks encode location, not just items. Mirror-image distortion costs about 10 recall points. A rival view says role similarity matters. | E16.05-K07 | memory (retrieval key) | no |
| F13 | The short-term-store-only theory fails (Charness: 6 to 8% loss after 30 s distraction; more pieces recalled on more boards). Long-term storage must be fast to reach. | E16.05-K04 | memory | no |
| F14 | Retrieved reusable templates raise LLM accuracy on repeat-structure tasks (Buffer of Thoughts Checkmate-in-One 36.4 to 86.4; Dynamic Cheatsheet AIME 23.3 to 50.0; +12.0 WebArena). Gains depend on repeated structure; the 99% on Game of 24 came from reusing a Python solver. | E16.05-K14 | memory | partly (section 5 subgoal library, marked D) |
| F15 | Skills and templates transfer across tasks with small positive gains (+2.6 to +5.1 on cross-domain pairs; HotpotQA to FEVER 58 to 70). All tests are agent tasks; no far-domain test. | E16.05-K16 | memory, O7 | no |
| F16 | Curated memory beats dumping history, and self-written memory can hurt. Full history fell to 6.7% (baseline 20.0%); self-generated skills -8.1 to -11.5 pp; curated +18.2 to +24.8 pp. | E16.05-K15 | memory, G7 | partly (section 5: a lesson is trusted only after helping on two problems) |
| F17 | Admit memory by outcome check, not self-judgment. Strict or held-out checks keep memory helpful (+3 to +22); add-all or model-graded memory hurts (-4 to -12). With no gate: 100% in-sample, 66.7% test. | E16.05-K20 | memory, G3, G5 | partly (G3 held-out; G5 code selects; no admission rule written) |
| F18 | Retrieval accuracy is weak and separate from end gain. BM25 Recall@1 is 7.0 to 57.2; top-1 retrieval captures about 30% of an oracle skill's gain. Models load a skill whether or not a good match exists. | E16.05-K21 | S0, memory, logging | no |
| F19 | Few retrieved items beat many (ReasoningBank: 0 items 39.0, 1 item 49.7, 4 items 44.4; 1 skill +18.0 vs 4 or more +10.1). No equal-token test exists. | E16.05-K23 | memory | partly (lessons are one line each) |

## 3. Contradictions between subfields

| # | Where the claims disagree | How to resolve |
|---|---|---|
| C1 | **Does search depth separate experts?** Not on easy positions (E16.01-K03, established). Yes, steeply, on hard ones needing 23 to 35 plies (E16.01-K04, single-source, N=4). E16.05-K10 (contested) says search size does not rise with skill. | Task difficulty decides. Same direction as G12. Do not build on K04 (N=4). Budget test: E16.01-U4, U9. |
| C2 | **Revisit: help or harm?** Self-revision with no new information hurts (E16.01-K09). Revisits with new information help (E16.01-K18, single-source). Forced "Wait" helps one model; underthinking hurts others (E16.01-K10, contested). | Both hold: the payload decides. Test the payload first: E16.01-U1, U2, U5. |
| C3 | **Deepen the same line or restart?** Sequential vs parallel depends on the task and difficulty (E16.01-K22, contested). Kotov advice (finish each candidate) vs de Groot's free jumping (E16.01-K02, K16). | No outcome study exists. Route by difficulty tier only after E16.01-U3. |
| C4 | **Time pressure.** Kasparov lost about 100 Elo; Chabris and Hearst blunders rose 36.5% (E16.01-K06, E16.05-K10, both contested). Same numbers, opposite reading. | Not decidable from chess. Use our own budget sweep (E16.01-U9). |
| C5 | **Selectivity.** Stronger players try fewer or more moves depending on the study (E16.01-K07, contested). | Width rule untested for LLMs: E16.01-U7. |
| C6 | **Extra time helps weak players, not experts?** Experts saturate near 3 s while weak players grow to 60 s (E16.05-K09, single-source). The meta-analysis finds no exposure-time effect (E16.05-K25, single-source). | Do not build a time rule on either. |
| C7 | **Template theory vs its rivals.** Slots and a fixed core (E16.05-K05, contested) vs constraint attunement (E16.05-K08, contested) vs abstract roles (E16.05-K26, contested). Slot-filled templates do not yet beat plain snippets (E16.05-K22, contested). | Run the format test: E16.05-U1, U6. |
| C8 | **Memory helps or hurts.** Templates raise accuracy (E16.05-K14, K16). Self-written or add-all memory lowers it (E16.05-K15, K20). | Not a real conflict: curation and an outcome gate decide. Test: E16.05-U3, U10, U11. |
| C9 | **Thinking pays less on unfamiliar items?** Gain per 1,000 reasoning tokens falls from 22.55% to 3.81% out of distribution (E16.05-K12, single-source), partly a token-count artifact. SCHEMA G11 and E16.01-K12 say thinking helps in chess. | Test by familiarity tier: E16.05-U8. |
| C10 | **With other fields.** A01 C3 (more thinking: help or harm) matches C2 and C9 here: depth pays only where something new can be found. A01 F10 (refinement plateaus after about 2 rounds, breadth beats it) fits E16.01-K09 and G2. A01 C4 (code-run search beats a model asked to search) fits F4 here. | Same remedy: code supplies the new information; spend by class. |

## 4. Recurring mechanisms

| Mechanism | Where it shows | What it means for the agent |
|---|---|---|
| **Recognise first, search second.** Stored patterns cue a candidate; search checks it. | E16.01-K05, E16.05-K13, E16.05-K10 (contested), E16.05-K14 | S0 and memory should run before S3. Keep the S4 check; the cue alone is only reliable in distribution (E16.05-K13). |
| **A revisit needs new information.** | E16.01-K01, K09, K18 (single-source), K19 | S5 and S6 should add a payload: failing output, retrieved case, tool result. |
| **Spend by difficulty.** | E16.01-K03, K04, K21; E16.05-K12 | Budget set per problem; easy items get little. |
| **Curate by outcome.** Memory pays only behind a held-out check. | E16.05-K15, K20, K21, K23 | Admission by code check, small retrieval, per-class on/off. |
| **Familiarity limits gain.** Gain falls out of distribution. | E16.05-K12, K13; E16.05-K01 (random edge small) | Match score is a candidate S0 field. |
| **The first idea blocks the better one (Einstellung).** | E16.01-K08 (single-source) | Single-source; fits SCHEMA section 5 (show lessons after the first attempt). |
| **Written reasoning is a weak guide to the choice.** | E16.01-K13 (single-source), K19 | G10 stays. |

## 5. Merged tests

| # | Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|---|
| T1 | **Trace ablation on logged runs** | E16.01-U8, E16.01-U12 | Drop each revisit step and the deepest unchosen branch from existing traces; measure how often the answer changes; test per-candidate notes. | High |
| T2 | **Difficulty-scaled budget and budget curve** | E16.01-U4, U9, U7, U13, E16.05-U8 | Uniform vs disagreement-scaled (with floor) depth; sweep 1x to 1/8 budget, plain vs scaffold; width 2/3/5 and 2x thinking by familiarity tier. | High |
| T3 | **Revisit payload and policy** | E16.01-U1, U2, U3, U5, U10 | Check again vs retrieved case vs mask-and-differ vs fresh context; stay-on-line gate; trigger-gated vs unconditional; split by 3 difficulty tiers. | High |
| T4 | **Best-so-far, stop rule and code pick** | E16.01-U6, U14 | Last state vs best-so-far by check vs confidence stop; model's final pick vs code pick from scored branches. | Med |
| T5 | **Paired memory on/off and cue hit rate** | E16.05-U3, U2, U7, U14 | Same problems with memory on and off; oracle vs top-1 vs top-3 vs none; hit rate, share of oracle gain, gain by match-score bin; match-score gate in S0. | High |
| T6 | **Template format and key** | E16.05-U1, U6, U12, U4 | Core plus slots vs flat example vs snippet at equal tokens, 100+ paired items with surface changes; keys by surface, role or both; rule vs example by task type; k = 1 rich / 3 / 8 small. | High |
| T7 | **Admission, retirement and transfer** | E16.05-U10, U11, U13 | Promote at 1/3/5 cases behind a held-out gate; retire by reuse utility; build on family A, test on B, C, D at rising distance. | Med |
| T8 | **Operator-cue table and cue-plus-check** | E16.05-U5, U9 | At S6: random vs model free choice vs table top-3; cue only vs cue plus one checked lookahead. | Med |
| T9 | **Exemplar style** | E16.01-U11 | Clean vs exemplars showing dropped branches, equal prompt tokens. | Low |

Run order from the UNKNOWNS files: T1, T2, then T3 (subfield 01); T5, then T6 only after T5 shows retrieval is good enough (subfield 05). Count tokens including retrieved text in every arm.

## 6. Not to add

| Idea | Why not | Claim ids |
|---|---|---|
| Copying "search deeper" as the expert trait | On easy positions depth barely separates skill; the steep slope rests on N=4 | E16.01-K03, E16.01-K04 |
| Unprompted "re-read and revise" with no new information | Lowers accuracy in several models; already in section 4b | E16.01-K09 |
| Training on search traces as a scaffold element | Needs training and a symbolic solver; a prompt cannot do it | E16.01-K14 |
| Chess as the main benchmark for a text scaffold | General LLMs lose to a weak engine; board-state errors dominate; no engine on the bench | E16.01-K12 |
| Chase-and-Simon chunk size (about 2 to 4 pieces, 2 s gap) as a memory limit | Size depends on the display medium; the hand-movement-artifact reading and its numbers (E16.05-K03) are single-source; a human limit, not ours | E16.05-K02 (established); K03 (single) |
| Short-term-store-only chunking as the memory model | Fails on interference and multi-board recall | E16.05-K04 |
| Dumping full history or add-all memory | Fell to 6.7% vs 20.0% baseline; below a fixed starting memory | E16.05-K15, E16.05-K20 |
| Self-written skills as trusted memory | -8.1 to -11.5 pp; solver often never reads them (single-source detail) | E16.05-K15, E16.05-K24 |
| Model-graded memory admission | Conflicts with G5; hurts when the judge is weak | E16.05-K20 |
| Many retrieved items | Gain peaks at 1 to 3 items | E16.05-K23 |
| Quoting the 99% Game of 24 template result as reasoning | It came from reusing a Python solver | E16.05-K14 |
| A rule that longer thinking time helps experts more | Exposure time did not moderate the effect | E16.05-K25 |
| Forced "Wait" revisits or a time-pressure rule | Contested; direction depends on model and task | E16.01-K06, E16.01-K10 |
| Kotov "finish each candidate" as a default | No outcome comparison exists | E16.01-K16 |

## 7. Gaps

- **Unresearched subfields:** see section 1. Computer chess and game AI (alpha-beta, MCTS, AlphaZero) is the most useful next one because F5 is the only claim in the tree-search slot (SCHEMA section 7).
- **Single lab only:** chunk size is partly a hand-movement artifact (Masters' median largest chunk 14.8 recall and 12.9 copy on a computer display vs 7.5 and 3.8 on a physical board; Chase and Simon's small chunks understate what masters store) (E16.05-K03). The expert-recall effect found in Go, gomoku, bridge, music, circuits, programs and basketball, with high heterogeneity (I2 63%) and publication bias (E16.05-K18). Both downgraded in the source audit (one opened source each).
- **Single-source claims that carry design weight:** E16.01-K04 (N=4), K08 (Einstellung, human, one lab), K13 (32.0% vs 1.2% branch ablation), K15, K16, K17, K18 (ThinkRetrieve), K20 (OTBench), K23 (Reasoning Memory); E16.05-K06, K09, K11 (CHUMP numbers not found), K12, K17, K19, K24, K25. Many are 2026 preprints on math, often with 30-problem sets.
- **No LLM test** of Einstellung, of a forced different second pass, or of a revisit policy at equal tokens.
- **No far-transfer test** for templates (chess to maths). All transfer tests are on neighbouring agent tasks.
- **No token-exact matching** in most memory and sampling studies; published gains cannot be trusted at equal tokens.
- **No ground truth for admission** on items without a check; held-out agreement or mutated-input checks are untested.
- **Chess needs an engine** for a live deliberation test; none on the bench machine.
- **Human-only limits** (chunk counts, 2 s gap, practice hours) cannot be tested on a training-free agent.
- **Unopened sources:** Chabris and Hearst original, Linhares and Brum full text (abstract only), Connors et al. 2011 (paywalled), CHUMP paper.

**Source audit, 2026-10-26:** 22 formerly established claims in E16 were re-opened. 19 confirmed, 1 reworded (E16.01-K03), 2 downgraded to single-source (E16.05-K03, E16.05-K18; one opened source each). Downgraded ids: E16.05-K03, E16.05-K18. Rows F10 and F11 keep only their still-established parts; the display-size and cross-domain recall details moved to section 7.
