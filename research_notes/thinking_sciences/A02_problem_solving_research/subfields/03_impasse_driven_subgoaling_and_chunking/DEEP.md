# Impasse-driven subgoaling and chunking: deep document

*Subfield A02.03. Evidence files in this folder: evidence_a-d.jsonl (ids a01-d18), claims.jsonl (K01-K34), critique.md (cross-check of 2026-10-31). Status tags: [E] established, [S] single-source, [C] contested. Where this document and an early evidence line disagree, the critique corrections win (see section 5.6).*

## 1. What it is

Soar is a cognitive architecture (Newell, Laird, Rosenbloom). Its core idea has two halves.

**Impasse-driven subgoaling.** Soar runs a decision loop. Each cycle it proposes operators, compares them, picks one and applies it. Sometimes the loop cannot go on. That is an impasse. Soar then makes a new state, a substate, linked to the old one (the superstate). In the substate, the same decision loop runs, now about the stuck decision. Substates can nest. The impasse ends when a decision can be made again (a01, a02, b06).

Impasse types, by what is missing:
- State no-change: no operator was proposed. Nothing to try.
- Operator tie: several operators, no way to choose.
- Operator conflict: operators with contradicting preferences. The glossary splits this from tie, so the count is 3 in the text and 4 in the glossary (a01).
- Operator no-change: an operator was chosen but cannot be applied or makes no progress.

**Chunking.** When a substate creates a result for the superstate, Soar back-traces the rules that built the result. The superstate facts that were tested become the conditions of a new rule. The result becomes its action. Next time a similar state appears, the rule fires in one step and no substate is needed (a03, c01). The rule is built at once when the result is made, not when the impasse ends (a16, c01).

What kind of rule is learned depends on the impasse type (a04):
- tie or conflict gives evaluation rules (search control);
- state no-change gives operator-proposal rules;
- operator no-change gives operator-application rules;
- plus elaborations.

Laird reads this as slow deliberate work turning into fast rule firing, loosely System 2 becoming System 1, with the caution that this is suggestive and not tested (a06).

**Why it matters for our agent.** Our schema has S6 (IMPASSE, fired by code) and S9 (look back, memory). The subfield asks one question: if the agent solves a stuck point, should it store that solution so the stuck point does not recur, and under what conditions is the stored entry safe to reuse? Soar's answer is old and detailed. The LLM-agent literature of 2023-2026 reinvents parts of it (skill libraries, workflow memory, as-needed decomposition). As of the evidence here, no study ties the whole chain together or tests the impasse trigger (K25, K34).

Scope of this document: the founding Soar and chunking papers, the practice-law debate they rest on, the cost and correctness problems found inside Soar, and every LLM study found that tests a similar mechanism, with numbers.

## 2. History and theories in depth

### 2.1 Chunking as a theory of practice (1981-1987)

Newell and Rosenbloom (1981) claimed that human skill speeds up with practice by a power law, T = B * N^-a, and proposed chunking as the cause. This paper was not opened (b09). It is known only from summaries and from Heathcote et al.

Rosenbloom and Newell (1982) gave the model (a07, a08, b08). Three assumptions:
1. Performance: a chunk is processed faster than its parts, given a serial bottleneck plus a parallel part.
2. Learning: chunks are learned at a constant average rate.
3. Task structure: larger patterns recur less often.

Together these predict the power law. The test task was Seibel (1963): a 1023-choice reaction task, ten lights and ten buttons, human data over 76,725 trials. The model, Xaps2, is a pre-Soar production system with no goals and no impasses. The full model was too slow to run for many trials, so the long curve came from a meta-model: 13 production cycles per trial plus 31 per pattern used, simulated over 72,633 trials, 1023 trials per pass. A chunk was learned with fixed probability 0.01 whenever possible. Without that value the task would be learned perfectly in 3 to 4 passes. So the 0.01 is a free parameter added to match the data. The model is a demonstration, not a fit to human data (K09).

### 2.2 Chunking becomes part of Soar (1986-1988)

Laird, Rosenbloom and Newell (1986) "Chunking in Soar: the anatomy of a general learning mechanism" moved chunking into a goal-based problem solver (a10, a11, b01, b02). Key points:
- The problem solver supplies the opportunities (subgoal results), the relevance bias (only what the subgoal used) and the consumer. Rule memory integrates the result.
- Generality comes mainly from implicit generalisation. Only working-memory elements actually referenced during the subgoal become conditions. Only a small percentage of available elements ended up in the example chunk.
- The object representation bounds generality. If a representation bundles roles into one slot, chunks test irrelevant things and miss cases they should cover. If generality is lacking, the mechanism is just a caching scheme.
- Dead-end search and unneeded preparation inside the subgoal leak irrelevant conditions into the chunk.
- The authors state their own limits: conflict impasses had not yet been met, problem-space selection was not yet a problem, and the largest coverage gap was problem-space creation and change of representation. Strategy acquisition and operator implementation were shown; other subgoal types were not.

An independent small application (Allen 1988, NASA report, a21) ran Soar on the eight-puzzle in several representations. Learned runs had fewer decision cycles and rule firings, and a learned system did not chunk again on the same task. One run: 21 decision cycles and 46 elaboration cycles before learning. No statistics.

Newell (1990) Unified Theories of Cognition and Laird, Newell and Rosenbloom (1987) are the sources of "universal subgoaling" (any difficulty creates a goal automatically) and the "uniform learning hypothesis" (goal-based chunking is the one learning mechanism). Neither was opened (a20). No number is cited from them here.

### 2.3 Chunking as explanation-based learning (1990)

Rosenbloom and Aasman (1990) showed chunking is a form of explanation-based learning (a15). Rules come from a dependency analysis of the rule traces in a subgoal. If the domain theory is not fully believed, chunking can do rote learning and induction, which means it can learn knowledge not implied by what is known. Consequence for us: a solved subgoal can store an unverified guess as a belief (K07). Only the framing parts of the paper were read.

### 2.4 The utility problem inside Soar (1990-1996)

Tambe, Newell and Rosenbloom (1990) found that chunking cut steps in all eight tasks but total time rose in four (a12, a13, b03, b04). Cause: a few learned rules were very expensive to match. Matching such a rule is NP-hard in the worst case. Section 3 has the numbers. The fix was to restrict the rule language so match cost grows linearly (unique-attribute representation), at the price of more chunks and more training problems (a13, b05).

Kim and Rosenbloom (1996) found a second cause: the match structure of the learned rule differs from the structure of the problem solving it came from. Keeping the explanation structure (non-linear rules) removed the slowdown (a14). Doorenbos' work (more than one million rules can still be used efficiently) was cited but not opened.

### 2.5 The correctness problem and EBBS (2000s-2022)

Old chunks were over-specific. Soar 9.6 replaced them with explanation-based behavior summarization (EBBS, Assanie 2022). An arithmetic agent learned 1263 rules in Soar 9.4 and 8 rules in Soar 9.6 (a16, c02). The thesis claims 12 correctness issues each fixed or detected, tested on 14 agents in 8 domains. The thesis was not opened (a18, d17), so those figures are unconfirmed.

The Soar manual defines correctness: a chunk is correct if rerunning the substate would give the same result. An over-general rule is incorrect. Soar tracks relevant operator selection knowledge (ROSK) so the chunk includes the preferences that chose the operator (c03). The manual's list of causes of wrong or over-general learning is in d04 and is used in section 4.5. Learning is off by default (c01, a16). Soar has no general mechanism to delete a bad chunk (a17).

Laird (2022) reports that analysis overhead is minimal and the gains are much greater than the costs, citing Assanie (a05, b06). Tambe 1990 found the opposite for the old matcher. These are different eras and matchers (critique).

### 2.6 The power law dispute

Heathcote, Brown and Mewhort (2000) re-analysed practice data: 40 data sets, 7,910 learning series, 475 subjects, 24 experiments (a09). On unaveraged data the exponential fit better than the power function in all data sets. Averaging across learners biases toward the power law. On the Seibel averaged data for one subject the power law still looked good: R2 .9858 for power, .9584 for exponential, .9902 for APEX. In the Brown and Heathcote 4-key task, 76.4% of series fit the exponential better. The chunking authors' own later fit for a single Seibel subject also favoured exponential (Rosenbloom and Newell 1987b, secondhand, a27). Evans et al. (2018) propose a delayed exponential (slow-fast-slow), favoured in a clear majority of paradigms; not opened (b11, d16). This does not refute chunking itself. It weakens the data chunking was built to explain (K08).

### 2.7 Soar meets language models (2021-2026)

- Wray, Kirk, Laird (2021): position paper. Use LMs as a knowledge source for gaps, with agent-side verification (c05).
- Kirk, Wray, Lindes, Laird (2022): a Soar agent where search and GPT-3 fill impasses and chunking stores the result (b12, b13, c06). Details in section 6.
- Kirk, Wray, Laird (2023): LLM prompted for a specific gap, response verified, tried, reviewed, then chunked. Over 70% of LLM responses were not viable (c07).
- AAAI Spring Symposium 2024: proposal to query an LLM at an impasse and store soft-token embeddings; no experiments (b14).
- CoALA (Sumers et al. 2023/2024): describes Soar as a template (c23, a22, b15). No measured results.
- CogRec (2025): Soar tie impasse, LLM, chunk, fewer LLM calls (a23, c08, c09, d14).
- NL2GenSym (2025): LLM writes Soar rules, execution critic repairs (c10-c12).
- Fan and Lan (2026): mechanism review finds no LLM agent has the whole Soar chain (a24, c21, c22).

## 3. Core findings with exact numbers

Status: Est = established (two or more independent sources, or a stable mechanism); Single = single source; Contested = sources disagree. K-numbers are claim ids in claims.jsonl.

| Finding | Numbers | Source (ids) | Status |
|---|---|---|---|
| Soar raises typed impasses; each starts a substate that reuses the same loop | 3 types in text, 4 in glossary | Laird 2022 (a01, a02, b06, c23) | Est [K01] |
| Chunk conditions are only what the substate used; this gives generality | Eight Puzzle: 230 chunks (no transfer), 112 simple transfer, 83 within-column symmetry, 61 across-column symmetry, 54 if non-minimal macros (14% of problems +2 path length, 26% +4, 7% +6) | Laird et al. 1986 (a11, b01) | Single [K10] |
| Same, Tower of Hanoi | 3 disks: 8 chunks in one trial encode Korf's 6-macro table | a11 | Single |
| Full Eight Puzzle table needs few trials | 3 carefully chosen trials | b01 | Single, hand-picked |
| Chunking cuts steps in all 8 toy tasks (cognitive effect, steps before/after) | Eight-puzzle 6.53, 2-Queens 5.21, Grid 13.54, Magic-square 6.59, Syllogisms 11.59, Monkey-bananas 6.20, Water jug 9.13, Farmer 11.09 | Tambe et al. 1990 (a12, b03) | Est [K03] |
| Time per step rose in four tasks (computational effect, ratio before/after; below 1 means each step got slower) | 0.15, 0.06, 0.06, 0.04 in the four bad tasks; 0.89, 0.83, 0.57, 0.45 in the others; per-step cost up to 25x | a12, b03; ratio definition fixed in critique | Est |
| Total speedup (critique recomputation) | Eight-puzzle about 0.99, 2-Queens 0.32, Grid 0.85, Magic-square 0.25 (four-fold slowdown); Syllogisms 10.27, Monkey 5.16, Water jug 5.22, Farmer 5.04 | b03 + critique correction 1 | Est |
| Only four such expensive cases among several dozen Soar tasks | 4 of several dozen | b03 | Single |
| Cause is the match structure of a few rules, not rule count or size | Better condition ordering raised the computational effect about 2-3x; footprint explained only a minor part | b04 | Single |
| Restricting the rule language bounds cost but needs more chunks | Eight-puzzle: avg condition elements 34 to 22, computational effect 0.15 to 0.25. Grid: multi-attribute 17 chunks, about 9x slower per step; unique-attribute needed more chunks (count unreliable, do not cite). Extra trials were hand-picked | a13, b05 | Single [K04] |
| Keeping explanation structure removes the slowdown | Grid avg CPU: 0.46 s no learning, 1.42 s linear rules, 0.34 s non-linear rules. Magic Square: linear ran out of memory (over 8 million tokens for one rule); non-linear was 9x faster than no learning | Kim and Rosenbloom 1996 (a14) | Single |
| Over-specific rules multiply | Arithmetic agent: 1263 rules (Soar 9.4) vs 8 (Soar 9.6) | Soar manual (a16, c02) | Single [K05] |
| A chunk is correct if replaying the substate gives the same result; Soar cannot delete a bad chunk; needs deterministic substate decisions | Definitions | a17, c03, b06, d04 | Single [K06] |
| Chunking is EBL and can store unverified guesses | Qualitative | a15 | Single [K07] |
| Power law of practice vs exponential | 7,910 series, 475 subjects, 24 experiments; Seibel avg: power .9858, exp .9584; 76.4% of series better fit by exponential in one task | Heathcote et al. 2000 (a09) | Contested [K08] |
| Chunking model learning rate is a free parameter | p = 0.01; 72,633 simulated trials | a07, a08, b08 | Single [K09] |
| Curated skills raise LLM agent pass rate | 33.9% to 50.5% (+16.6 pp, range +4.1 to +25.7), 87 tasks, 8 domains, 18 configs, 9,396 trajectories | SkillsBench (b16) | Est [K11] |
| Partial replication of the above | 30 tasks, GPT-5.5 31.3% to 67.3% (+36.0 pp, CI +20.7 to +52.0); DeepSeek V4-Flash 26.0% to 50.7% (+24.7 pp) | Xu and Wu 2026 (b20) | Same sign, larger size |
| Self-written skills (authored before the task) hurt | -8.1 pp (Opus 4.7), -11.3 (GPT-5.5), -11.5 (Gemini 3.1 Pro); earlier version -1.3 pp average | b16, b17, a25, b26 | Single [K12] |
| Fewer, shorter skills work better | 1 skill +18.0, 2-3 +19.0, 4+ +10.1 pp. Compact +19.0, standard +21.5, detailed +14.5, comprehensive +0.7 pp | b18 | Single [K13] |
| Skills hurt on some tasks | 13 of 87 tasks; largest drops -7.4 pp (two tasks), -5.6 pp (four tasks) | b19 | Single |
| Availability beats presentation | Low vs high abstraction +0.7 and -6.7 pp, CIs cross zero; one worked example +0.7 and +1.3 | b20 | Single [K14] |
| Stored abstractions can carry errors; raw cases beat abstractions | Mean success over 9 settings: anti-persistence 59.9, trajectory memory 53.5, abstraction memory 49.0, joint 49.3, Reflexion 52.9 | Wang et al. 2026 (b21) | Contested [K15] |
| Distilled lessons beat raw trajectories and workflows | WebArena, Gemini-2.5-flash: none 40.5, Synapse 42.1, AWM 44.1, ReasoningBank 48.8; AWM below no-memory for Claude-3.7 (40.8 vs 41.7) | ReasoningBank (d07) | Contested [K33] |
| Failures help only if distilled | Success-only to success+failure: Synapse 40.6 to 41.7 (+1.1); ReasoningBank 46.5 to 49.7 (+3.2) | d08 | Single |
| Retrieval collisions | Within-group similarity 0.80-0.95 vs cross-group 0.57-0.63; late in a compound stream 52% and 46% foreign retrievals; one method fell 29.8% to 11.2% on BFCL-Base | Chen et al. 2026 (b22) | Est [K16] |
| Workflows from past successes raise web success | WebArena 35.5 vs 23.5 (+12.0 pp, +51.1% relative), about 2.0 fewer steps; Mind2Web +24.6% relative; online AWM edge 8.9 to 14.0 pp as train-test gap widened | AWM (b23, c16) | Single [K17] |
| Insights plus examples beat either alone (task dependent) | ALFWorld put: ReAct 50, insights 61, retrieve 73, ExpeL 83. Insights-only vs retrieve-only: HotpotQA 36 vs 31, ALFWorld 50 vs 55, WebShop 37 vs 38 | ExpeL (b24) | Single [K18] |
| Library maintenance helps | ALFWorld 79.5%, +8.8 pp over strongest baseline; plug-in +0.68 to +2.90 pp | SkillOps (b25) | Single [K19] |
| LLM proposals need verification before compiling | GPT-3 goal proposals accepted 30-40% by a human; Search+LLM completed 54% of subtasks; actions 96% correct first try; over 70% of LLM responses not viable (later paper) | Kirk et al. (b12, b13, c06, c07) | Est [K20] |
| Impasse to LLM to chunk cuts later LLM calls | CogRec: call frequency falls to a plateau with chunking; ML-1M HR@10 0.3124 vs Soar alone 0.2956 (+5.7%), LLM-Direct 0.2815; gains over best baseline 4.1-9.1% | CogRec (a23, c08, c09, d14) | Single [K21] |
| Execution-grounded critic is the key part when an LLM writes Soar rules | 100 water-jug cases: one-shot 55% (Gemini-2.5-Pro), 66% (Qwen-max); framework 86% and 91%; hard cases 20% vs 76.67% (Gemini), 46.67% vs 86.67% (Qwen); decision cycles 1.76x-1.98x optimal vs manual about 3390x; no critic -23%, no knowledge base -17%, no case base -14% | NL2GenSym (c10, c11) | Single [K22] |
| Retry scoped to the failed part beats whole-trial retry | ADaPT vs Reflexion (GPT-3.5): ALFWorld 71.6 vs 57.5, WebShop 44.0 vs 35.0, TextCraft 52.0 vs 32.0; GraSP local repair 79.7 vs global replan 77.4 (ALFWorld), 84.9 vs 81.8 (ScienceWorld) | c13, c14, c26, c20, c27 | Est [K23] |
| As-needed decomposition beats plan-then-execute | ALFWorld 71.6 vs ReAct 43.3 and Plan-and-Execute 43.3; Try Again 47.8; Pick2 52.9 vs 5.9 (Reflexion), 11.8 (ReAct); TextCraft 52.0 vs 27.0 (P&E) | ADaPT (c13, c14) | Single [K24] |
| Diagnosis is often wrong at the exact step | AgentDebugX strict attribution 28.8% vs 21.7% best baseline; GAIA repairs 13 of 73 failed tasks vs 4-6 | c17 | Est [K26] |
| Typed failure to retrieved recovery works with training | PALADIN recovery up to 89.68% vs CRITIC 76.34% | c18 | Est [K26] |
| Verification gate raises downstream success at equal induction budget | ASI shopping: 32.6 unverified text, 36.4 verified program in memory, 39.0 verified text, 40.1 verified program as action; gate admitted 15.6% of turns vs 31.4% | ASI (d12, d13) | Single [K28] |
| Gate strength matters | Strict selection stays near error-free memory; add-all and coarse filters widen the gap; AgentDriver with strict selection passed the error-free variant after about 2000 executions | Xiong et al. 2025 (d05) | Est [K29] |
| Demotion by use | Delete after n retrievals if mean utility is below a threshold; helps with a reliable judge, hurts with a coarse one | d06 | Single [K30] |
| In Voyager verification mattered more than the library | No self-verification -73% items; random curriculum -93%; GPT-3.5 5.7x fewer items. Tech tree mean iterations: Voyager wood 6, stone 11, iron 21, diamond 1/3; no library wood 7, stone 9, iron 29, diamond 0/3. Transfer to a new world: 19/18/21/18 vs 36/30/27/26 without library. Retrieval top-5 accuracy 96.5% | Voyager (d01-d03) | Single [K31] |
| Reasoning-task libraries: curated helps, append-all can fall below baseline | Dynamic Cheatsheet, Sonnet AIME 2024 23.3 to 50.0 (curated), 26.7 (append everything); AIME 2025 6.7 to 36.7; GPT-4o 20.0 to 6.7 under append-everything; GPQA-Diamond 59.6 to 68.7; GPT-4o Game of 24 10 to 99. LEGO-Prover 50.4% vs 47.1% (+3.3) | d09, d10, d11 | Est [K32] |
| No ablation separates typed impasse trigger from generic stuck trigger | DPR uses 5 low-progress steps; ALFWorld Qwen-3-8B 35.1 to 75.4, GPT-5 46.3 to 88.1; +2.7 over LATS (event page only) | d15 | Single [K34] |
| Compiling subgoals into a trained policy degrades less under compositional goals | HERAKLES -51% vs -64% to -92% at n=4 (Crafter 19.2) | b27 | Single, needs training [K27] |

## 4. Mechanisms and models

Each mechanism is written so it can be built as a program plus model slots. "Program" means code decides. "Model" means the LLM fills a slot.

### 4.1 Impasse detector (S6 trigger)

Soar detects impasses by what is missing in the decision. Map to our loop:

| Soar impasse | Detector (program) | Substate goal |
|---|---|---|
| State no-change: nothing proposed | S3 produced no candidate that parses, or all candidates fail to run | Find an approach; subgoal = pick an operator O1-O8 not yet used |
| Operator tie: several options, no way to choose | Two or more candidates pass S4 with different outputs and S7 cannot separate them | Find a discriminating test (run the one input where they differ) |
| Operator conflict | Two rules fit all examples but give different outputs on a fresh input | Same as tie; search for a counterexample |
| Operator no-change: chosen option stalls | Two S5 rounds with no change in the failing output, or the same error twice | Subgoal on the failed part only |

Guards from the evidence:
- Operator no-change can just mean a slow action. Wait for slow tool calls; do not subgoal (a01).
- A state no-change impasse produced an infinite loop in generated Soar code. Put a budget stop on repeated no-change states (c12).
- Never accept a result that depended only on a state no-change impasse with nothing else (EBBS rejects the condition-free rule, d04).
- The only numeric stuck trigger found in an LLM paper is "5 consecutive low-progress scores" (d15, event page only).

Whether typing the trigger beats one generic stuck trigger is unmeasured (K34).

### 4.2 Substate (protected, same loop)

- Re-enter the same loop (S1 to S9) with a state line naming the parent task, the impasse type and the one thing that is missing (a02, a19).
- Keep the substate narrow. Retrying only the failed subtask beat retrying the whole attempt (K23). The gap grows with task length: GraSP advantage over ExpeL grew from 6% at 10 steps to 18% at 20 steps (c27).
- Limit nesting depth. ADaPT used max depth 3 (4 for TextCraft) (c13). Soar does not cap depth in the text (a02).
- The parent state must not be altered by the substate; only a typed result returns. This is the "protected substate" link the 2026 review says no LLM agent has whole (a24, c21).
- Decompose only on failure, not on a schedule (G1; K24).

### 4.3 Result and chunk (compile step)

Soar's algorithm (a03, c01, c03, c04):
1. A substate creates a result that goes to a superstate.
2. Back-trace the rules that created it.
3. Superstate elements tested along the way become conditions. Elements never referenced are left out. This is implicit generalisation.
4. Include the preferences that selected operators (ROSK), or the rule will not match the real processing.
5. The result becomes the action.
6. Bottom-up: when a result passes through several nested substates, one chunk is made per level. Stop when a chunk writes only into the state it matched.

Engineer's version for our library:

```
entry = {
  impasse_type: one of {no_candidate, tie, conflict, stalled},
  trigger: ONLY the facts the solved subgoal used (program extracts; not the whole context),
  operator: O1..O8 or method name,
  result: the fix or sub-answer,
  check: runnable test that passed (held-out, G3),
  path: short record of the solution steps (a14: keep structure),
  inputs_justifying: list of facts to re-check at reuse (b07),
  uses: 0, post_use_failures: 0
}
```

Rules:
- Compile at result time, per level (c04).
- Admit only after a code check passes on something the answer was not fitted to (G3). Expect only a minority to pass: ASI's gate admitted 15.6% of turns vs 31.4% for the ungated method (d13).
- Do not admit results that depended on random choice, numeric or sampled choice, a recalled fact that may change, or an impasse alone (d04, b06). An LLM sampling step is not deterministic, so require a code check or a repeat run before compiling (d18, snippet only).
- Store the impasse type. A tie fix is a preference; a no-change fix is a method (a04).

### 4.4 Retrieval and match cost

The utility problem is the main engineering lesson (K03). Steps saved were lost to expensive matches in 4 of 8 tasks.

For an LLM, "match cost" is retrieval cost plus context length plus noise. Design rules from the evidence:
- Exact or near-exact lookup on a small, flat trigger schema. Restricted formats bound cost but need more entries (a13, b05). The extra training in that study was hand-picked, so treat the size of the trade-off with care.
- Cap entries shown per state. SkillsBench: 1 skill +18.0, 2-3 +19.0, 4+ +10.1 pp (b18). GraSP also found 2-3 focused skills beat dumping all (c20).
- Keep each entry short. Compact +19.0 vs comprehensive +0.7 pp (b18).
- Log total tokens and latency including retrieval, not just steps (b03).
- Voyager retrieved top-5 with 96.5% top-5 accuracy in a code-skills library (d02).
- Similar queries can need different fixes. Scope each entry to its trigger and impasse type; test collision rate (b22: 52% and 46% foreign late in a compound stream).

### 4.5 Correctness checks (when is an entry safe to reuse)

Soar's definition: correct if rerunning the substate gives the same result (c03). For us, rerun means run the entry's check on the new instance. Checklist from the Soar manual (d04), translated:

| Soar risk | Library rule |
|---|---|
| Over-general justification | Re-check at reuse; do not trust a match |
| Rule repair too specific | Prefer to subgoal again than to patch a stored entry |
| Operator selection knowledge not tracked | Store the preferences/reasons that chose the method |
| Random, numeric or learned operator choice | Do not compile a sampled choice without a check |
| Result depends only on a no-change impasse | Reject |
| Several rules collapsed into one result | Store one entry per independent result |
| Recalled knowledge may change or is opaque | Store with its inputs; re-check inputs |

Stale handling (a17): an entry that fails to match falls back to a fresh subgoal. An entry that matches and then fails should be demoted. Soar has no deletion, so this rule is ours. A measured design exists: delete after at least n retrievals when mean downstream utility is below a threshold. It works with a strict judge and hurts with a coarse one (d06). A code check is a strict judge, so the favourable case applies.

### 4.6 Generalise and merge

Old chunking made 1263 rules where EBBS made 8 (a16). Auto-saved entries will pile up as near-duplicates. Steps: group entries by (impasse type, operator, trigger skeleton); merge entries whose triggers differ only by constants; re-run the checks on the merged entry; count the near-duplicate rate before and after (K05 test).

SkillOps shows a rule-based maintenance layer (retire, merge, re-test) gives +8.8 pp on ALFWorld over the strongest baseline, with +0.68 to +2.90 pp as a plug-in (b25). Authors' own method.

### 4.7 The call-cost curve

CogRec: with chunking, LLM call frequency falls and settles on a low plateau; without chunking it stays high (a23, c09, d14). The plateau value is only in a figure. Use it as a health metric: model calls per task should fall as the library fills. Flat means compilation is failing. Voyager, LEGO-Prover and Dynamic Cheatsheet all show a flat-then-rising gain shape (d01, d11, d09), consistent with a delayed exponential, but none fitted a curve (d16).

### 4.8 Where the LLM sits

Soar fills impasses with search, rules or a human. In the LLM versions the model is the filler (CogRec, Kirk). The safe pattern, repeated in several papers: model proposes, program or environment checks, only passed results are compiled (b12, b13, c07, c10). The execution-grounded critic was the most important component in NL2GenSym (-23% without it, c11).

## 5. What holds up

### 5.1 Holds up (two or more sources, or a stable mechanism)

- Typed impasses and same-loop substates are a clear, well-documented design (K01). It is a design, not an experiment.
- Steps saved do not equal cost saved. Soar's own data (4 of 8 tasks slower in total) and the LLM-side analogue agree: 4+ skills is worse than 2-3, and comprehensive skills give about zero gain (K03, K13).
- Gate strength matters for any library. Xiong et al. (four agents) and Dynamic Cheatsheet (append-all can fall below baseline: GPT-4o 20.0 to 6.7) agree with ASI's +3.8-4.2 gate effect (K28, K29, K32).
- Retrieved memories collide on near-duplicate tasks, and agents copy retrieved records when inputs are similar (K16, K29).
- Scoping retry to the failed part beats whole-trial retry: ADaPT, GraSP (K23).
- LLM proposals are mostly unreliable until verified (K20): 30-40% of goal proposals accepted; over 70% of responses not viable.
- Curated skills help; availability matters more than wording. SkillsBench plus a 30-task partial replication agree on sign (K11, K14).

### 5.2 Failed or weak

- The power law of practice that chunking theory was built to explain does not survive unaveraged data (K08).
- Self-written skills hurt: -8.1 to -11.5 pp on three configs (K12). These skills were written before the task, not compiled after an impasse. It is a warning, not a test of chunking.
- Skills hurt on 13 of 87 tasks (a fixed pipeline with no applicability condition) (b19).
- Soar's cost claims conflict across eras: Tambe 1990 (4 of 8 slower) versus Laird 2022 (overhead minimal, secondhand).
- Founding Soar evidence is toy puzzles with hand-designed representations and hand-picked trials (a11, b01, b05).

### 5.3 Contradictions to carry forward

- Self-written skills hurt (SkillsBench) versus compiled workflows help (AWM, Voyager). Difference: AWM and Voyager induce from verified successes; SkillsBench skills were written before the task. Neither is an impasse-triggered test (critique).
- Distilled rule versus raw case (K15, K33). Wang 2026: raw trajectories 53.5 beat abstractions 49.0. ReasoningBank: distilled lessons 48.8 beat raw (Synapse 42.1). Different judges and benchmarks. ExpeL says insights plus examples is best and the split is task dependent. All are authors' own methods on web or household tasks.
- Power law versus exponential versus delayed exponential (K08). Matters only if we model library gains.

### 5.4 Moderators

- Domain: SkillsBench gains by domain (final version): natural science +28.8, media +24.1, cybersecurity +18.9, software engineering +11.6, mathematics +9.7 pp. An earlier version: healthcare +51.9, manufacturing +41.9, cybersecurity +23.2, software engineering +4.5, mathematics +6.0. Gains are big where pretraining coverage is thin (b18, a25). A strong base did not always mean a small gain: a config at 41.1% gained only +7.1.
- Template overlap: AWM gains depend on shared templates; offline AWM is best only when training data match the test distribution (b23). Yet online AWM kept an 8.9 to 14.0 pp edge as the gap widened.
- Task stage: in Voyager the library effect is small or negative early (stone 11 vs 9 iterations) and large for iron and diamond and for transfer (d01, d03).
- Model strength: small models gain little or fall in Dynamic Cheatsheet (GPT-4o-mini, Haiku); AWM fell below no-memory for Claude-3.7 (40.8 vs 41.7) (d09, d07).
- Judge quality: demotion by use helps only with a reliable judge (d06).
- Task length: the local repair advantage grows with horizon (c27).

### 5.5 Interventions that worked and did not

| Intervention | Worked? | Evidence |
|---|---|---|
| Curated, short skills, 1-3 per task | Yes | b16, b18 |
| Self-written skills before the task | No (-8.1 to -11.5 pp) | b16 |
| Verification gate before admitting | Yes (+3.8-4.2 pp, ASI) | d12 |
| Append every past item, no curation | No; can fall below baseline | d09 |
| Coarse LLM-judge selection of memory | No; widens error gap | d05 |
| Strict selection + deletion by use | Yes, with a reliable judge | d05, d06 |
| Execution-grounded critic | Yes (-23% when removed) | c11 |
| Local repair over global replan | Yes, about +2 to +3 points | c20, c27 |
| Whole-trial verbal reflection instead of subgoal scope | Weaker than scoped retry | c26 |
| Majority vote of 3 in the DC setting | No gain (23.3 on AIME 2024) | d09 |
| Fine-tuning on relabeled failures (AgentHER) | Yes, +7.6 to 11.4% over success-only SFT, but needs training | c19 |
| Abstraction level or one worked example in a skill | Small, CIs cross zero | b20 |

### 5.6 Corrections applied from the critique

1. Tambe total speedups: recomputed. The extracted table was shifted by half a row. Eight-puzzle is about break-even (0.99), not a clear slowdown, although it is grouped with the expensive four. Chunk counts of 142 and 86 in earlier lines are unreliable; do not cite them.
2. The "computational effect" is a ratio (before over after); below 1 means each step got slower.
3. NL2GenSym "one-shot" baselines are Gemini-2.5-Pro and Qwen-max; the framework used a cheaper Gemini variant. Manual: hard SR 46.67%, overall SR 84%.
4. SkillsBench: use the final version (-8.1 to -11.5 pp self-generated; +16.6 curated). The older +16.2 and -1.3 figures are from a survey citing an earlier version.
5. CogRec ML-1M HR@10: 0.3124 vs Soar alone 0.2956 vs LLM-Direct 0.2815. Gains over the best baseline 4.1 to 9.1%. No ablation numbers in the text.
6. Wang 2026: anti-persistence best in 7 of 9 settings; above joint memory in 8 of 9; above trajectory and abstraction memory in all 9.
7. Rows c24 and b09 are placeholders, not evidence. Heathcote et al. numbers are verified (a09), not snippet-only.

## 6. Language models

### 6.1 Does any LLM study test impasse-driven chunking?

No study tests the whole chain on a reasoning task. The nearest are pieces. A 2026 review of 10 architectures, 8 runtimes and 42 modern systems concludes that the Soar chain (typed impasse, protected substate, typed return, compiled chunk) is not found whole in any current LLM agent (c21). It lists failure conditions of such a design: misdiagnosis, unsafe compile, parent-state corruption, no drop in repeat failures. Its codes are judgments and no experiments were run (K25).

### 6.2 Soar plus an LLM filling impasses

**Kirk, Wray, Lindes, Laird (2022)** (b12, b13, c06): simulated tidy-kitchen robot, 35 goal assertions, GPT-3 text-davinci-002 at temperature 0. Conditions combined instruction, search and LLM. Every condition except Search+LLM learned all subtasks in one shot. Search+LLM completed 54%. GPT-3 goal proposals were accepted 30-40% of the time (30% in the depth-4 search condition). Actions were 96% correct on the first try but goals were weak. Instructor words fell about 50% in all LLM conditions. Inst+Search(d4)+LLM used 70 instructions vs 76 baseline, 43 of them yes/no. GPT-3 cost under 10 USD. Failures: closing a bin that has no lid, and putting empty bottles and cans in the fridge. Of 16 objects not tidied, 3 were due to each. Search plus chunking removed repeat cost; the LLM only cut human effort. Lesson: LLM answers are proposals; a yes/no check made them safe to store.

**Kirk, Wray, Laird (2023)** (c07): position paper. Prompt for one gap, verify, try, review, chunk. Over 70% of responses were not viable. The full pipeline was not evaluated at scale.

**CogRec (2025)** (a23, c08, c09, d14): Soar recommender. On a tie impasse, a structured query (context, impasse reason, task) goes to an LLM. The reply is parsed into a condition-action chunk and compiled. Datasets: ML-1M (6,040 users, 3,416 items, 999,611 interactions), Movies, Yelp. ML-1M HR@10 0.3124 vs 0.2956 Soar alone vs 0.2815 LLM-Direct (+5.7% over the Soar-alone figure). Ablations: no LLM bootstrap drops performance most; no chunking drops toward the LLM-only baseline; call frequency stays high without chunking and plateaus low with it. Single group, offline recommendation, no correctness measure for compiled rules.

**NL2GenSym (2025)** (c10-c12): LLM writes Soar rules for water jug, 100 cases. Zero-shot 0 for both models. One-shot 55% (Gemini-2.5-Pro) and 66% (Qwen-max). Framework 86% and 91%. Hard cases 20% vs 76.67% (Gemini), 46.67% vs 86.67% (Qwen). Decision cycles 1.76x and 1.98x optimal vs manual about 3390x. Ablation: no critic -23%, no knowledge base -17%, no case base -14%. Models differ between arms; one domain.

### 6.3 LLM agents with impasse-like triggers but no compile step

**ADaPT** (c13, c14, c26): try the task; only if the executor fails, a planner splits it, recursively. This is impasse-driven subgoaling with no learning step. GPT-3.5, ALFWorld 71.6 vs ReAct 43.3, Plan-and-Execute 43.3, Try Again 47.8, Reflexion 57.5. WebShop 44.0 vs 32.0 (ReAct), 35.0 (Reflexion), 38.0 (LATS). TextCraft 52.0 vs 19.0 (ReAct), 27.0 (P&E), 32.0 (Reflexion). Pick2 task 52.9 vs 5.9 (Reflexion) and 11.8 (ReAct). Authors' own prompts, text benchmarks, single model for headline numbers. It does not store decompositions, so a cache of solved subtasks is an untested extension.

**Reflexion** (c15): after a failed trial the agent stores a verbal lesson. ALFWorld 130 of 134 tasks in 12 trials; HumanEval 91% vs 80%. Whole-trial, needs repeated trials on the same task, lessons stored without conditions.

**DPR** (d15): a slow diagnostic fires after 5 consecutive low-progress scores. ALFWorld 134 tasks, 10 seeds; Qwen-3-8B 35.1 to 75.4; GPT-5 46.3 to 88.1; +2.7 over compute-matched LATS (p about 0.01). Event page only; no gate-versus-schedule ablation seen.

**AgentDebugX / PALADIN / AgentHER / GraSP** (c17-c20): typed failure to recovery. Exact-step attribution only 28.8%. PALADIN recovery up to 89.68% (training needed). GraSP local repair 79.7 vs global replan 77.4.

### 6.4 LLM agents with a compile step but no impasse trigger

| System | Trigger for adding | Gate | Result |
|---|---|---|---|
| Voyager (d01-d03) | After a task success | Self-verification | 63 items in 160 iterations, 3.3x baselines; verification removal -73%; library helps later tiers and transfer |
| AWM (b23, c16) | After a success | Rule-based or LM induction | WebArena 35.5 vs 23.5; fewer steps |
| ASI (d12, d13) | After a success | Execution check | +3.8-4.2 over ungated; admits 15.6% of turns |
| Dynamic Cheatsheet (d09) | After every query | Model curation | AIME 2024 23.3 to 50.0; append-all 26.7 |
| LEGO-Prover (d11) | After a proof | Isabelle checker | miniF2F-valid 50.4 vs 47.1 |
| ReasoningBank (d07, d08) | After successes and failures | LLM judge | WebArena 48.8 vs 40.5 none |
| SkillsBench (b16) | Authored before the task | None | -8.1 to -11.5 pp |
| SkillOps (b25) | Library maintenance | Rule-based | ALFWorld 79.5% |

### 6.5 What changed LLM behaviour, by how much

- Curation: +16.6 pp (curated skills, SkillsBench) versus -8.1 to -11.5 pp (self-written). A swing of about 25-28 pp from who wrote the skill and whether it was checked.
- Gate: about +4 pp (ASI). In DC the gap between curated (50.0) and append-all (26.7) on AIME 2024 is 23.3 points on 30 questions (noisy: one question is 3.3 points).
- Count: 2-3 skills +19.0 vs 4+ +10.1 pp.
- Scope: scoped retry +14.1 pp over Reflexion on ALFWorld (71.6 vs 57.5), +9.0 on WebShop, +20.0 on TextCraft (ADaPT's own runs).
- Model strength: weak models do not benefit from a notebook; strong ones do (DC).

### 6.6 Evidence gaps for LLMs

- No test separates trigger (impasse versus after every success) from gate (K34, critique gap 1).
- No counted false-reuse rate on near-duplicate tasks needing a different fix (gap 2).
- No sweep of entries retrieved per state outside SkillsBench (gap 3).
- No measure of typed versus generic trigger (gap 4).
- Raw case versus distilled rule unresolved (gap 5).
- Most LLM evidence is authors' own methods on ALFWorld, WebArena and similar. Reasoning-task evidence is thin: DC (AIME sets of 30 questions), LEGO-Prover (one run).

## 7. What our agent should take

Tags: status [E] established, [S] single-source, [C] contested. Schema parts: G = guardrail, S = state, O = operator, memory = S9 library.

### Add now (established)

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| 1 | Trigger a subgoal only on a code-detected signal, never on a schedule. Keep the existing S6 firing rules (no pass, two rounds no change, same error twice, budget fraction). | G1, S6 | [E] for scoped, failure-triggered retry; as-needed decomposition itself [S] | K23, K24; a01, c13 |
| 2 | Subgoal re-enters the same loop with a state line (parent, impasse type, what is missing); keep it narrow, scoped to the failed part. | S6 | [E] | K01, K23; a02, a19, c13, c14, c26, c20, c27 |
| 3 | A model proposal at an impasse is only a proposal. Store a result only after a code check on something the answer was not fitted to. | G3, G2, memory | [E] | K20, K29, K32; b12, b13, c07, d05, d09, d12 |
| 4 | Gate strength: use a code check, never a model judge, to admit entries. No append-everything library. | G5, memory | [E] | K29, K32; d05, d09, d12, d13 |
| 5 | Cap entries shown per state at 1 to 3 and keep each entry short. | memory | [E] on direction; the numbers come from one benchmark | K13 (single), K03; b18, c20, a12 |
| 6 | Scope each entry to its trigger and impasse type; test for collisions on near-duplicate tasks. | memory | [E] | K16; b22, d05, d10 |
| 7 | Count total cost (tokens, latency, retrieval), not steps; keep a no-library baseline in every comparison. | G7 | [E] | K03; a12, b03 |
| 8 | Do not compile a recovery from a diagnosis alone; require a passing re-run. | G2, G3 | [E] | K26; c17, c18 |
| 9 | Fix retrieval and availability before wording of entries. | memory | [S] | K14; b20, b16 |
| 10 | Budget stop on repeated no-change states in the detector. | G6, G7, S6 | [S] | c12 |

### Test first (not yet established; each maps to a row in UNKNOWNS.md)

| # | Item | Schema part | Status | Evidence | Unknown id |
|---|---|---|---|---|---|
| 11 | Impasse-triggered library versus a library filled after every success | S6, memory | [S] (trigger half untested) | K28, K32, K34; d02, d12 | U1 |
| 12 | Typed impasse trigger versus one generic stuck trigger | S6 | [S] | K01, K34; d15 | U2 |
| 13 | Store only the facts the subgoal used, not full context | memory | [S] | K02, K10; a03, a11, b02 | U3 |
| 14 | Raw checked case versus distilled rule per entry | memory | [C] | K15, K33, K18; b21, d07, b24 | U4 |
| 15 | Demotion after n uses with failed outcomes | memory | [S] | K30, K19; d06, b25 | U5 |
| 16 | Re-run entry check at reuse, versus trusting a match | G3, memory | [S] | K06, K07; c03, a15 | U6 |
| 17 | Generalise and merge near-duplicate entries | memory | [S] | K05; a16, c02 | U7 |
| 18 | Entries from failed attempts (lesson plus achieved partial result) | S9, memory | [C] | K33; d08, c19 | U8 |
| 19 | Retrieval cap sweep 1, 3, 6 on reasoning items | memory | [S] | K13; b18 | U9 |
| 20 | Calls per task fall as the library fills | S9, G7 | [S] | K21; a23, d14 | U10 |
| 21 | Store the solution path with the entry | memory | [S] | a14 | U11 |
| 22 | Cheap strict-schema trigger versus free-text trigger | memory | [S] | K04; a13, b05 | U12 |
| 23 | Library gain split by in-template versus new-structure items | memory | [S] | K17; b23 | U13 |

Notes:
- The library idea is new for our schema: S9 currently writes one lesson line. Items 11-13 are the core of the Soar contribution. Nothing is added to SCHEMA.md until its test passes (see UNKNOWNS.md).
- Keep section 4b of the schema in mind (what not to add). Do not add a separate meta-module. Soar's point is one mechanism for both levels (a19), which S6 already follows.

## 8. Concrete tests on our bench

All arms at equal tokens. Setup cost (library build, retrieval, checks) is counted in the budget (G7). Report mean and a 95% interval. Use at least 100 items for reasoning slices; AIME sets of 30 are too small (K32 caution).

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 trigger vs gate | Reasoning items with a code check, in families of related problems (ARC-like, puzzle classes), streamed in order | A: no library. B: library filled after every success with code gate. C: library filled only at impasses (S6) with the same gate. D: library filled after every attempt, no gate | Pass rate on held-out later items; tokens per solved item; library size | B and C beat A by a few points; D below B. C versus B unknown; C has a smaller library. Add the impasse trigger if C is within 1 point of B at 30% or fewer entries, or beats B |
| T2 typed vs generic trigger | Same stream | A: four typed triggers with typed substate goals. B: single "stuck" trigger with generic operator pick | Pass rate; rounds to solution | Small (0 to 3 points); typed may help tie and conflict cases |
| T3 minimal vs full trigger | Near-duplicate task pairs where a surface feature is irrelevant | A: trigger = facts the subgoal used. B: trigger = full state text | Reuse hit rate on held-out items; false-reuse rate | A hit rate higher; false reuse similar or lower |
| T4 false reuse | Pairs of near-duplicate tasks that need different fixes | Scoped entries vs unscoped; with and without re-check at reuse | Wrong-reuse rate (count); pass rate | Re-check cuts wrong reuse; scoping lowers collisions (b22 saw 46-52% foreign) |
| T5 case vs rule | Same stream | A: raw case plus checked outcome. B: distilled rule. C: both (rule + one example) | Pass rate; repeated-error rate | Contested; C expected best (ExpeL); split by task type |
| T6 demotion | Stream with a task shift midway | A: growing library. B: retire after n uses with mean utility below threshold. C: age-based deletion | Pass rate after the shift; size | B beats A after the shift; sweep n = 2, 3, 5 |
| T7 retrieval cap | Stream | Cap 1, 3, 6 entries per state | Pass rate; tokens | 1-3 best; 6 worse |
| T8 merge | Long stream | A: auto-saved entries. B: merge near-duplicates | Near-duplicate rate; reuse; pass rate | B fewer entries, equal or better pass |
| T9 call curve | Stream of 200+ items in families | Model calls per item over time, with and without the library | Calls per item | Falling curve with library, flat without; report plateau point |
| T10 failed-attempt entries | Stream | Success-only entries vs success plus checked failure lessons | Pass rate | +1 to +3 if distilled (d08); none if copied raw |
| T11 in-template vs new-structure | Test items labelled by template overlap | Library vs none | Gain per group | Gain larger in-template (b23) |
| T12 bad-seed injection | Stream | Seed one wrong but plausible entry in an ungated vs a code-gated library | Repeated-error rate | Ungated propagates; gated blocks (K07, d05) |
| T13 scope | Multi-part items | Subgoal on the failed part vs restart the whole attempt | Pass rate at equal tokens | Scoped wins by a few points (ADaPT 14 on ALFWorld, GraSP 2-3) |

## 9. What does not transfer, and why

- **Rule-matching speed-ups.** Soar's cost was Rete matching of learned rules. Our retrieval cost is context and noise. The lesson (steps saved can be lost in lookup) transfers; the numbers do not.
- **Automatic implicit generalisation.** Soar knows exactly which working-memory elements a rule firing tested, because its reasoning is rule traces. A language model's reasoning is text, and written reasoning is not evidence of what drove the answer (G10). Our program must extract "facts used" some other way (for example by checking which input features, when changed, change the result). This is a real gap, not a copy.
- **Deterministic substate.** Chunking requires deterministic substate decisions (b06, d18). LLM sampling is not deterministic. We replace determinism by a code check or a repeat run.
- **Power law of practice.** Contested for humans (K08); no basis to expect it in a library. Measure gains directly.
- **Impasse as a perfect signal.** In Soar the impasse is exact because the decision procedure reports it. For an LLM the stuck signal is a program heuristic (no pass, same error twice). Misdiagnosis is likely: exact-step failure attribution reached only 28.8% (c17).
- **Universal subgoaling and the uniform learning hypothesis.** Architecture-wide claims from Newell (1990). Not opened, not tested for us. Our schema uses subgoaling only at S6, by design.
- **Toy puzzle tasks.** Eight Puzzle and Hanoi with hand-designed representations (a11, b01). Counts such as 61 chunks do not predict library size on reasoning tasks.
- **Learning from human instructions.** Kirk et al.'s saved instructor words (about 50%) have no analogue in a single autonomous agent.
- **Training-based compile.** HERAKLES, PALADIN, AgentHER need training, so they are out of scope for a frozen-model scaffold (K27).
- **Web and household results.** Most LLM numbers are ALFWorld, WebArena, Minecraft: long action sequences. Our bench is reasoning problems with checks. Gains may be smaller (LEGO-Prover +3.3; SkillsBench mathematics +9.7 in the final version, +6.0 in the earlier one).
- **Learning off by default.** Soar ships with learning off because of correctness risk (c01). Treat the library as opt-in per task class, enabled after tests pass.

## 10. Open questions

1. Impasse trigger versus after-every-success at equal tokens, both with the same gate. Not measured anywhere (gap 1, trigger half).
2. False-reuse rate of compiled entries on near-duplicate tasks needing a different fix (gap 2). Only qualitative reports.
3. Best number of entries per state outside SkillsBench, and where retrieval cost passes the steps saved (gap 3).
4. Does typing the impasse beat one stuck trigger (gap 4)?
5. Raw case versus distilled rule (gap 5). Two groups, opposite results, different judges.
6. Assanie (2022): the 12-issue taxonomy and the 14 agents / 8 domains evaluation are unconfirmed (gap 6).
7. How much of Voyager's gain is verification versus library when verification also steers retry (gap 7)? Separate gate from retry control.
8. Does the CogRec call-frequency drop appear in a frozen-LLM scaffold, and after how many tasks does it plateau (gap 8)?
9. Which demotion rule is best head-to-head (gap 9)? Xiong et al. versus SkillOps have no comparison.
10. Which curve describes library gains (gap 10)? Evans et al. 2018 not opened; no LLM study fits a form.
11. Can the program extract "facts the subgoal used" without rule traces? Perturbation tests are a guess.
12. When a stored entry matches but the situation differs, how does the agent detect it before using it?
13. Do tie and conflict impasses behave differently from no-change impasses? Soar's authors had not met conflict impasses in 1986 (a10).
14. Does the library help on tasks where the base model already scores high? SkillsBench is mixed: a config at 41.1% gained only +7.1.
15. Do the 2026 single-group preprints (anti-persistence, self-evolving, SkillOps, AgentDebugX, mechanism review) replicate? None has been.

## 11. Sources

[V] = opened and read (full text or the relevant section). [M] = snippet or secondhand only.

**Soar and chunking (founding and Soar-internal)**
- [V] Laird (2022) Introduction to the Soar Cognitive Architecture. https://arxiv.org/abs/2205.03854 (a01-a06, a19, b06, b07). One later pass (d18) saw only a search summary; the earlier passes read it.
- [V] Rosenbloom and Newell (1982) Learning by chunking: summary of a task and a model. https://cdn.aaai.org/AAAI/1982/AAAI82-061.pdf (a07, a08, b08)
- [V] Heathcote, Brown, Mewhort (2000) The power law repealed. https://link.springer.com/content/pdf/10.3758/BF03212979.pdf (a09). Verified in the critique.
- [V] Laird, Rosenbloom, Newell (1986) Chunking in Soar: the anatomy of a general learning mechanism. https://link.springer.com/article/10.1023/A:1022639103969 (a10, a11, b01, b02)
- [V] Tambe, Newell, Rosenbloom (1990) The problem of expensive chunks and its solution by restricting expressiveness. https://link.springer.com/article/10.1007/BF00117107 (a12, a13, b03-b05)
- [V] Kim and Rosenbloom (1996) Learning efficient rules by maintaining the explanation structure. https://cdn.aaai.org/AAAI/1996/AAAI96-114.pdf (a14)
- [V] Rosenbloom and Aasman (1990) Knowledge level and inductive uses of chunking (EBL), framing parts only. https://cdn.aaai.org/AAAI/1990/AAAI90-123.pdf (a15)
- [V] Soar Manual ch. 4, Procedural Knowledge Learning. https://soar.eecs.umich.edu/soar_manual/04_ProceduralKnowledgeLearning/ (a16, a17, c01-c04, d04; d04 read the first 100,000 of 140,700 characters)
- [V] Allen (1988) Production system chunking in Soar: case studies in automated learning (NASA). https://ntrs.nasa.gov/api/citations/19890010689/downloads/19890010689.pdf (a21)
- [M] Assanie (2022) PhD thesis, University of Michigan. https://deepblue.lib.umich.edu/items/b5194e3a-68d2-449e-acf4-17ebae201b98 (a18, d17; blocked)
- [M] Newell (1990) Unified Theories of Cognition; Laird, Newell, Rosenbloom (1987) Soar. Seen only through citations. https://arxiv.org/abs/2205.03854 (a20)
- [M] Rosenbloom and Newell (1987b) Learning by chunking: a production system model of practice, via Heathcote et al. https://link.springer.com/content/pdf/10.3758/BF03212979.pdf (a27)
- [M] Newell and Rosenbloom (1981) Mechanisms of skill acquisition and the law of practice. https://cdn.aaai.org/AAAI/1982/AAAI82-061.pdf (b09; the URL in the evidence file points to the 1982 paper)
- [M] Evans, Brown, Mewhort, Heathcote (2018) Refining the law of practice. https://doi.org/10.1037/rev0000105 and https://figshare.utas.edu.au/articles/journal_contribution/Refining_the_Law_of_Practice/22964183 (b11, d16)
- [M] Lotem and Halpern (2025) chunking and evolution; out of scope. https://arxiv.org/abs/2501.11201 (a26)

**Soar plus language models**
- [V] Wray, Kirk, Laird (2021) Language Models as a Knowledge Source for Cognitive Agents. https://arxiv.org/abs/2109.08270 (c05)
- [V] Kirk, Wray, Lindes, Laird (2022) Integrating diverse knowledge sources for online one-shot learning of novel tasks. https://arxiv.org/abs/2208.09554 (b12, b13, c06)
- [V] Kirk, Wray, Laird (2023) Exploiting Language Models as a Source of Knowledge for Cognitive Agents. https://arxiv.org/abs/2310.06846 (c07)
- [V] Augmenting cognitive architectures with large language models (AAAI Spring Symposium 2024). https://ojs.aaai.org/index.php/AAAI-SS/article/download/27689/27462 (b14)
- [V] Sumers, Yao, Narasimhan, Griffiths (2024) CoALA. https://arxiv.org/abs/2309.02427 (a22, b15, c23)
- [V] Hu, Wang, Yang, Wang (2025) CogRec. https://arxiv.org/abs/2512.24113 (a23, c08, c09, d14). The d14 line carries the URL https://arxiv.org/pdf/2510.09355, which is the NL2GenSym paper; its CogRec numbers were confirmed against 2512.24113 in the critique.
- [V] Yuan et al. (2025) NL2GenSym. https://arxiv.org/abs/2510.09355 (c10-c12)
- [V] Fan and Lan (2026) From cognitive architectures to language agents: a mechanism-level review. https://arxiv.org/abs/2607.23942 (a24, c21, c22; partly skimmed)

**LLM agents: skills, memory, decomposition**
- [V] Li et al. (2026) SkillsBench. https://arxiv.org/abs/2602.12670 (b16-b19)
- [V] Xu and Wu (2026) Skill availability and presentation granularity. https://arxiv.org/abs/2605.31408 (b20)
- [V] Jiang et al. (2026) SoK: Agentic skills. https://arxiv.org/abs/2602.20867 (a25, b26; secondary, older SkillsBench numbers)
- [V] Wang, Panaganti, Zhou (2026) More memory, worse agents. https://arxiv.org/abs/2610.27406 (b21)
- [V] Chen et al. (2026) Are self-evolving agents continual learners? https://arxiv.org/abs/2610.25858 (b22)
- [V] Wang, Mao, Fried, Neubig (2024) Agent Workflow Memory. https://arxiv.org/abs/2409.07429 (b23, c16)
- [V] Zhao et al. (2024) ExpeL. https://arxiv.org/abs/2308.10144 (b24)
- [V] Song, Pu, Zhao (2026) SkillOps. https://arxiv.org/abs/2605.13716 (b25)
- [V] Carta et al. (2025) HERAKLES. https://arxiv.org/abs/2508.14751 (b27; results section partly read)
- [V] Prasad et al. (2024) ADaPT. https://arxiv.org/abs/2311.05772 (c13, c14, c26)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c15)
- [V] Zhu et al. (2026) AgentDebugX. https://arxiv.org/abs/2607.18754 (c17)
- [V] Vuddanti et al. (2026) PALADIN. https://arxiv.org/abs/2509.25238 (c18)
- [V] Ding (2026) AgentHER. https://arxiv.org/abs/2603.21357 (c19)
- [V] Xia et al. (2026) GraSP. https://arxiv.org/abs/2604.17870 (c20, c27)
- [V] Wang et al. (2023) Voyager. https://arxiv.org/pdf/2305.16291 (d01-d03; c25 was the earlier unverified pass)
- [V] Xiong et al. (2025) How memory management impacts LLM agents. https://arxiv.org/pdf/2505.16067 (d05, d06; table cells garbled, not cited)
- [V] Ouyang et al. (2025/2026) ReasoningBank. https://arxiv.org/pdf/2509.25140 (d07, d08)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/pdf/2504.07952 (d09, d10)
- [V] Wang et al. (2023) LEGO-Prover. https://arxiv.org/pdf/2310.00656 (d11)
- [V] Wang, Gandhi, Neubig, Fried (2025) Inducing Programmatic Skills (ASI). https://arxiv.org/pdf/2504.06821 (d12, d13)
- [M] Kadu and Krishnan (2026) Progress-Gated Dual-Process Routing (ICML 2026 workshop), event page only. https://icml.cc/virtual/2026/70400 (d15)
