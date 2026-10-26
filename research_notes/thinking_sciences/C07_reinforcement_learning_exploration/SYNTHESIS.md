# Reinforcement learning, exploration: synthesis

*One view across the field's researched subfields. Built from each subfield's DEEP.md, claims.jsonl and UNKNOWNS.md.*

Notes on use. "Established" means the claim's status in claims.jsonl (two or more independent sources). Single-source and contested claims are named only where they matter for a contradiction, a "not to add" row or a gap. Schema column checked against `research_notes/single_agent/SCHEMA.md` v0.2. Most evidence is from 2024-25 LLM systems and from RL games. Gains are rarely measured at equal tokens, so every row is a design hint until tested on our model (section 5). The source audit of 2026-10-26 re-opened the papers behind all 21 established claims; four were reworded and none were downgraded (see the end).

## 1. Coverage

| Subfield | DEEP.md | Claims | Established |
|---|---|---|---|
| 01 Bandits and Thompson sampling for operator selection | [DEEP](subfields/01_bandits_for_operator_selection/DEEP.md) | 29 | 9 (16 single-source, 4 contested) |
| 08 Go-Explore and archives | [DEEP](subfields/08_go_explore_and_archives/DEEP.md) | 36 | 12 (23 single-source, 1 contested) |
| **Total** | | **65** | **21** |

Each researched subfield has an UNKNOWNS.md (12 test rows for 01, 14 for 08; 26 in all).

Not yet researched (from SUBFIELDS.md; the folder numbers for these are not yet created):

- Count-based exploration, unified with intrinsic motivation (S3 history of directions tried).
- Knowledge-based intrinsic motivation (learning progress; background).
- Information-theoretic motivation: empowerment, predictive information (S7 probe choice). Rated High, so this is the biggest hole.
- Competence-based motivation (background).
- Novelty search and open-endedness (open mode; overlaps C04).
- Language-guided exploration (iLLM; S3 priors).
- Curiosity in RL training of LLMs (CDE; training-time, low use).

Thompson sampling has its own row in SUBFIELDS.md but is covered inside 01. The "information-gain tests" item (which input best splits two rules at S7) is not covered by any subfield.

## 2. Established findings, merged

| # | Finding | Claim ids | Schema part | In SCHEMA.md? |
|---|---|---|---|---|
| F1 | Bandit regret has a log-in-pulls lower bound. UCB1 and Thompson sampling reach it. The guarantees are asymptotic and say nothing at tens of pulls. Our S6 horizon is tens of pulls, so theory gives framing only. | C07.01-K01, C07.01-K02 | S6 | no |
| F2 | Thompson sampling needs no tuning constant, matches or beats UCB in simulation at thousands of pulls, and copes better with delayed feedback (UCB/TS regret ratio 2.65 at delay 1 to 3.82 at delay 1000). Our feedback is delayed (a branch is scored later). | C07.01-K03 | S6, O1-O8 | no (S6 says "pick one operator not used yet", no selector) |
| F3 | Tuned simple rules (epsilon-greedy, Boltzmann) can beat untuned UCB1. The hidden cost of any bandit is tuning. Compare untuned defaults. | C07.01-K04 | S6 | no |
| F4 | When the best operator changes, stationary bandits lag. Windowed, discounted or restart variants recover, with total regret of order sqrt(T times the number of breakpoints times log T) (a sqrt(T) lower bound holds in a two-breakpoint game), and need a window or discount that depends on the unknown number of changes. Our own simulation (not a published source) shows count caps of 5 to 50 changed regret by at most about 0.15 at 30 to 60 pulls. | C07.01-K05 | memory | no |
| F5 | When candidates outnumber the budget, sharing information across similar candidates (embeddings, clustering) beat independent-arm baselines in TRIPLE (21% and 28% over BO-EI on GPT-3.5, with different margins on Llama2), and Thompson sampling that models shared structure beat independent TS in a shortest-path tutorial. The advantage shrinks as budget grows. How much depends on embedding quality is untested here (inference only). | C07.01-K14 | memory, S0 | partly (class record exists; no shared features) |
| F6 | In LLM-driven search, bandit operator selection gives a small or unmeasured gain over random or uniform (LLaMEA 0.8453 vs 0.8304 at N=6; mixed in ShinkaEvolve and TIDE). Beat a uniform-random baseline before building a learner. | C07.01-K16 | S6 | no |
| F7 | LLMs used as bandit agents mostly fail to explore in context (Krishnamurthy et al.: GPT-4 with a basic prompt had suffix failure in more than 60% of replicates) and are biased by arm labels (Semantic Bandits). Among the prompt designs they tested only GPT-4 with chain of thought and externally summarised statistics worked; other remedies (reasoning models, algorithm-guided prompts, fine-tuning) also improve exploration, and numeric contextual bandits on text embeddings often match or beat LLM agents (Berdica et al.). Keep operator selection in code with counts and means. | C07.01-K20 | G5, section 1 | yes (section 1: the program decides; G5 code selects) |
| F8 | The reported LLM-bandit gains rest on 3 to 6 seeds, no significance tests, and weak or author-tuned baselines. Headline numbers come from near-zero baselines. We need 10 or more seeds or paired items and a stated minimum effect. | C07.01-K21 | G7 | partly (G7 equal tokens; no seed or effect-size rule) |
| F9 | Keeping an archive of promising states and returning to them before exploring solves hard-exploration problems that curiosity-driven agents fail (Montezuma: 57,439 mean, 57% of runs solved level 1; prior best about 17,500). | C07.08-K01 | S6, memory | partly (S5 "keep best-so-far"; no archive or return operator) |
| F10 | The state key (cell design) is the main lever. Easy domain knowledge cut the cost of Montezuma level 1 about 11x (640M to 57.6M frames). A generic image key found only 22 Pitfall rooms. | C07.08-K02 | memory | no |
| F11 | A key that is too coarse merges different states and starves the archive (96% of red-team intents in one cell under a tool-name hash; look-alike Pitfall screens needing different actions). | C07.08-K03 | memory | no |
| F12 | Exploring freely for a short burst after reaching an archived state helps (MiniGrid, three environments; about 20 steps in Yang et al.). It mattered more than tuning epsilon. | C07.08-K04 | S3, S6 | no |
| F13 | Raw archive entries are not valid results. They must be re-run on a changed or held-out input. Robustification worked in 40% of attempts; in 51 of 57 level-1 runs the best path used a game bug. | C07.08-K06 | G3, S8 | yes (G3 unfitted check); archive gate not stated |
| F14 | A language model that picks the archived state to resume, the action and what to archive (IGE) beats ReAct and Reflexion on long text tasks (Cooking 92 vs 56 and 52; Coin Collector 88 vs 0). A re-implementation at equal steps and about equal API cost won on some Jericho games and lost on others. All comparisons are at equal steps, not equal tokens. | C07.08-K07 | S6, S3, memory | no |
| F15 | Plain LLM agents explore poorly. Reflexion did not beat ReAct on long text games and sometimes hurt. Open-weight reasoning models loop in text mazes (Qwen3-235B coverage 52.7% easy, 23.0% medium). | C07.08-K20 | G1, S6 | yes (4b unstructured self-reflection; G1) |
| F16 | Archive bloat is real. Filtering controls it (IGE: 203.5 to 25.5 states on BabyAI, 22.4 to 4.4 on Cooking, but only 18.5 to 15.6 on Game of 24). | C07.08-K09 | memory, G7 | no |
| F17 | Choosing the resume point by best score alone loses to rules that also credit few children or descendant results (DGM greedy 39.7 vs 50.0 on SWE-bench; HGM clade score correlates 0.78 and 0.63 with true descendant productivity vs 0.29 to 0.44). Selection in all three is by code. | C07.08-K26 | S6, G8 | partly (G8 and G5 say code selects; no resume rule) |
| F18 | On ARC-style synthesis with a checker, breadth is the strong baseline at small budgets (128 calls: repeated sampling 15.0 vs tree variants 8.7 to 14.0). Refinement gains appear at large budgets (6,000 candidates). Budgets are in calls, not tokens. | C07.08-K24 | G12, S3 | partly (G12 spends by difficulty; no switch point) |
| F19 | Coverage keeps rising with independent samples far past 20, roughly log-linear over several orders of magnitude (CodeContests Gemma-2B 0.02% to 7.1% at 10,000; SWE-bench Lite 15.9% to 56% at 250). Plateaus come later and depend on model and method (repeated sampling on ARC begins to plateau around 200 to 500 calls, budget tested up to 512; SOAR's 7B search flattens near 5.2k attempts). Pick N from a pilot coverage curve. | C07.08-K32 | G12 | partly (G12 foothold rule; no N rule) |
| F20 | The picker of the final answer must be a real check, not a vote or a model score. MATH, Llama-3-8B: coverage 82.9% to 98.44% at 100 to 10,000 samples, but vote or reward model only 40.50% to 41.41%. SWE-Search: model value estimate right 73%, a separate discriminator 84%. | C07.08-K33 | G8, S7 | yes (G5, G8, S7 group by behaviour) |

## 3. Contradictions between subfields

| # | Contradiction | Ids | Reading |
|---|---|---|---|
| C1 | Who picks the next thing. 08 reports that a model choosing the resume point and action beats ReAct (F14). 01 reports that LLM bandits fail to explore (F7, established) and that letting the LLM choose its strategy does worse than a bandit (contested). SCHEMA G5 and G8 say code selects. | C07.08-K07, C07.01-K20, C07.01-K11 (contested), C07.08-K26 | Partly resolved: IGE's gain is on text worlds with weaker models, and the strongest resume rules (F17) are in code. No test compares model-picked and code-picked resume at equal tokens. Test C07.08-U5. |
| C2 | Archive vs plain sampling. F9 and F14 say return-then-extend wins. F18 says breadth is the strong baseline at small budgets. One 2026 test with a coding agent (Haiku 4.5, 17/25 vs 6/25) found plain independent retry beat the archive at equal total tokens. | C07.08-K01, C07.08-K24, C07.08-K23 (single-source), C07.08-K07 | Not settled. Archive wins are on long horizons and hard games, at equal steps. Our bench is short-horizon. Test C07.08-U1. |
| C3 | Does learning to select operators pay? F6 says gain over uniform is small or unmeasured. Single-source results report +1.79 points (DE) and +0.60 (GA, not significant) for Thompson over uniform in OPTS, and a hand table of states beat uniform 23x. Own simulation (single-source) says a fixed best-guess order beats flat Thompson at 8 arms and under 60 pulls. | C07.01-K16, C07.01-K22, C07.01-K24, C07.01-K29 | Evidence is thin and mostly not at our scale. Do not build a learner before T1. |
| C4 | Learned selector vs forced switch. Bandit-only gave 0.011 and meta-guidance 0.108 in one 3-run system; another reports state policy 23x vs stagnation 1.8x. Neither tests a plain forced switch. SCHEMA S6 already has a code trigger. | C07.01-K17 (contested) | Open. Test C07.01-U4. |
| C5 | Parallel independent runs: F19 says coverage keeps rising past 20 samples. One single-source red-team study says only duplicates grow after N=20. | C07.08-K32 vs C07.08-K16 (single-source) | Not a real conflict: duplicates in an attack-type space vs solved items with a checker. Trust K32 when a checker exists. |
| C6 | Window or reset on posterior counts. F4 says stationary bandits lag after a change and variants recover. Own simulation (not a published source) at 30 to 60 pulls shows caps change regret by at most about 0.15 (12.54 vs 12.69). | C07.01-K05 vs C07.01-K26 (single-source) | Likely the same fact at different horizons. Test C07.01-U9 is low priority. |
| C7 | With other fields: restart vs resume. C01 F10 says cap and restart rather than extend. E09 says failure accumulates in context, so keep best and restart clean. 08 says resuming a stored state beats re-deriving it, most for deep states (single-source), and a single-source claim says restoring a state restores its mistakes. | C01.08-K08, E09 F11, C07.08-K35, C07.08-K30 | Compatible if resume means a fresh context seeded with the stored entry, not an extended chain. The resume protocol must say so. Tests C07.08-U9, U11. |
| C8 | With other fields: A02 F14 says a bandit-like controller over a per-task record cut cost by up to 83% at comparable accuracy (LIMBO). F6 says accuracy gains are small. | A02 F14, C07.01-K16 | Different metric (cost vs accuracy). A learner may pay in tokens before it pays in pass rate. Log both in T1. |
| C9 | With other fields: A02 F7 and C01 (selector is the bottleneck) agree with F18, F19 and F20. No conflict. | A02.01-K22, C01 | Agreement worth keeping: sample wide, select with a real check. |

## 4. Recurring mechanisms

| Mechanism | Where | What it means for the agent |
|---|---|---|
| Sample wide, pick with a real check | F18, F19, F20 (08), F6 (01) | Breadth plus a code check is the baseline every learner or archive must beat at equal tokens. |
| Code selects, the model does not | F7 (01), F17 and F20 (08) | Operator choice, resume choice and final choice all run in code. A model picker is allowed only after a blind test. |
| The key or arm definition decides everything | F10, F11 (08), F5 (01) | What counts as "the same state" or "the same operator context" matters more than the selection rule. |
| Small-sample regime | F1, F2, F3, F8 (01) | Tens of pulls, 8 arms. Asymptotic theory is silent. Fewest tuning knobs wins. |
| Value depends on search state | F5 (01), F17 (08) | Neither "best operator" nor "best entry" is fixed. Credit descendants, not just the current score. |
| Gain depends on base-model strength and horizon | F14, F15, F18 (08) | Gate by class pass rate or model strength (links to SCHEMA G12). |
| Entries need re-checking before they count | F13 (08), G3 | An archived or selected solution must pass an unfitted check. |
| Bloat control | F16 (08) | Archive and pool need a size cap and dedupe, or tokens per step grow. |

## 5. Merged tests

All tests at equal total tokens (selection, resume, filter and check calls counted). Use 10 seeds or paired items (F8).

| Merged test | Unknown ids covered | One-line design | Priority |
|---|---|---|---|
| T0 Noise floor and full-factorial operator log | open questions of C07.01 (seed noise, real reward tables) | Run all 8 operators on every item once (about 8x one pass) and repeat one arm 10 times; this unblocks T1 and gives the SD. | High (first) |
| T1 Operator selector: uniform vs fixed order vs flat Thompson vs prior | C07.01-U1, U2, U3, U5, U6, U9, U11, U12 | Replay T0 logs at 20, 40, 60 pulls; add priors (4 to 8 pseudo-counts) and credit-rule variants; log tokens as well as pass rate (C8). | High |
| T2 Stall switch vs bandit vs both | C07.01-U4 | On items that stall at S5, compare bandit only, forced operator switch only, both, uniform. | High |
| T3 Archive vs sampling, with a gate | C07.08-U1, U2, U10, U14, C07.01-U10 | Arms: repeated sampling, best-of-N with checker, retry with reflection, archive (about 40% breadth then resume); split easy and hard; run with nano and strongest model; try a gated archive and a breadth-to-depth switch at 20, 40, 60% at three budgets. | High |
| T4 Archive key and entry hygiene | C07.08-U3, U7, U6, U12, U11 | Compare keys (normalised answer, plan skeleton, execution output); re-check each entry on a mutated input; compare code dedupe plus cap with a model filter; show the resumed run only its own entry. | High |
| T5 Resume rule and burst | C07.08-U4, U5, U8, U9, U13 | Resume by DGM formula vs descendant score vs blind model pick; 1, 3, 5 short attempts vs root restart; low-score resume; summary plus challenge line for wrong-state entries. | High for U4, Med for the rest |
| T6 LLM as prior, not chooser | C07.01-U7 | Arms: flat Thompson, LLM chooses, LLM prior capped at 4, hand prior. | Med |
| T7 Final pick: halving vs Thompson vs uniform | C07.01-U8 | Replay ARC and BRAINTEASER candidate sets with about 5 checks per candidate; metric P(final pick correct). | Med |

Order to run: T0, then T1 and T2 (cheapest, decide if any learner is worth building), then T3 (the only direct test so far is negative), with T4's re-check logged in the same runs.

## 6. Not to add

| Idea | Why not | Status |
|---|---|---|
| A model choosing operators by free-text judgment | LLM bandits fail to explore and are label-biased; keep counts and means in code | established (C07.01-K20) |
| A bandit learner with no uniform-random baseline | Published gains are small and rest on 3 to 6 seeds | established (C07.01-K16, K21) |
| Generic image or tool-name hash as the archive key | Collapses or starves the archive | established (C07.08-K02, K03) |
| Using archive entries without re-checking them | Raw entries are not valid results | established (C07.08-K06, with G3) |
| A model value score or vote as the final pick | Coverage rises, vote and score stay flat | established (C07.08-K33) |
| Capping parallel independent runs at a small fixed N when a checker exists | Coverage keeps rising (plateaus appear only at hundreds of calls on ARC) | established (C07.08-K32) |
| Reflexion-style plain retry as the exploration method | No better than ReAct on long tasks | established (C07.08-K20) |
| Training-time curiosity (CDE, iLLM) | Needs weight updates; no fixed-weight transfer | from SUBFIELDS.md, not yet researched |
| Entry-score bonuses (novelty, causality) on the archive | One preprint, one seed: large drop in findings. Do not add without a win at equal tokens | single-source (C07.08-K14), hold |
| Showing the generator the whole archive | One result in another domain says it hurts | single-source (C07.08-K28), hold |
| Window or discount on counts at 30 to 60 pulls | Own simulation shows at most about 0.15 change in regret; not yet tested on real logs | single-source (C07.01-K26), hold |
| Whole-agent archives (DGM style, about 22,000 USD per run) | Out of budget; borrow only the parent rule | single-source (C07.08-K12), cost |

## 7. Gaps

- Seven of nine listed subfields are not researched (section 1). Information-gain probe choice (S7) and count-based history for S3 are the ones the schema most needs.
- We have no real operator reward table. Every number about selectors at our scale comes from one own simulation (single-source).
- All LLM archive gains use 2024 to early 2025 models. The only 2026 test is negative and single-source (C07.08-K23). Whether the gain shrinks with a stronger base model is open (C07.08-U2).
- Archive gains are at equal steps or calls, not equal tokens, and no source separates archive structure from simply spending more calls.
- Our bench is short-horizon with exact checkers. The strongest archive results are on long text worlds. Tasks with no checker are untested; expect the gain to vanish (C07.08-K25, K33).
- Single-source claims worth a second source: lineage credit beating selector choice (C07.01-K08), state-dependent operator value (C07.01-K15), prior strength at 30 pulls (C07.01-K24, K25), brittle archived programs (C07.08-K34), wrong-state restore (C07.08-K30), burst length (C07.08-K29), archive helps weaker models (C07.08-K10), reasoning-chain resume (C07.08-K36).
- Contested claims not settled: dynamic Thompson vs windowed UCB (C07.01-K09), LLM-chosen strategy vs bandit (C07.01-K11), halving vs UCB for prompts (C07.01-K13), stall-triggered change vs bandit (C07.01-K17), learned state keys vs hand cells (C07.08-K17).
- Rare-breakthrough operators (O7, O8) may be missed by a mean-based bandit. No published credit method for heavy-tailed value (C07.01-U11).
- Operator interaction (sequence effects) has no study (C07.01-U12).
- Cross-field: restarts (anytime search), quality-diversity (C04) and library learning may replace operator choice by choice of start state. Compare once those fields' syntheses exist (C05 has none yet).

**Source audit, 2026-10-26:** the papers behind all 21 established claims of this field were re-opened. 17 confirmed, 4 reworded (C07.01-K05, K14, K20, C07.08-K32), 0 downgraded. No section 2 row was removed or moved to Gaps, and no merged test or schema conclusion depended on a downgraded claim.
