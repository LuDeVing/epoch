# Go-Explore and archives: deep document

*Subfield C07.08. Sources: evidence_a-d.jsonl (ids a01-a34, b01-b28, c01-c27, d01-d18), claims.jsonl (K01-K36), critique.md in this folder. Numbers were re-checked against full PDF text by the critic pass unless marked "figure" or "approximate". Budgets in almost every LLM study are environment steps, calls or candidates, not tokens. Links to sibling subfields (not covered here): Quality-diversity and novelty search, Anytime search and restarts, Bandits and Thompson sampling, Library learning, Conflict-driven clause learning, Resource-rational analysis.*

## 1. What it is

An archive method keeps a store of promising states and returns to them on purpose. Go-Explore (Ecoffet, Huizinga, Lehman, Stanley, Clune) is the best-known case. Its rule is "first return, then explore". The agent picks a stored state, goes back to it exactly, and only then explores from it. New states go into the archive.

The idea comes from a diagnosis of why curiosity-driven agents fail on hard-exploration games (a01, c07):

- **Detachment.** An agent driven by intrinsic reward leaves a frontier once the reward there is used up. It forgets how to get back. The frontier is lost.
- **Derailment.** The noise that makes the agent explore also stops it from reaching a state it already knows is good.

The fix has three parts. Keep an archive of "cells" (classes of state), each with the best known path to it. Return with no exploration noise. Explore after arrival. Phase 2 then turns the best found path into a policy that survives noise ("robustification").

Why we care. Our agent is a scaffold around a language model. A partial solution (a partial plan, a half-built program, a proof prefix) is just text. Restoring it is free and exact. That makes the archive idea unusually cheap for us, but it also raises hard questions that the research has only begun to test: what counts as "the same state", who picks the resume point, how much it costs in tokens, and whether it beats plain resampling at equal budget.

Scope of this document:

1. Go-Explore on Atari and robotics (the original evidence and theory).
2. Variants that remove hand-built cells (Latent Go-Explore, Time-Myopic Go-Explore).
3. Other archive methods (MAP-Elites style archives, Darwin Godel Machine, ShinkaEvolve, Huxley-Godel Machine, Go-Browse).
4. LLM agents with archives of promising states (Intelligent Go-Explore, GLoW, a sandbox-snapshot study) and neighbouring checker-guided search (AB-MCTS, SOAR, Mind Evolution, repeated sampling).

## 2. History and theories in depth

### 2.1 Roots: why restarting from stored states helps

Salimans and Chen (2018, a33) gave the cleanest theory. On a toy "blind cliff walk" with N states between rewards, plain RL needs time that grows exponentially in N, about 2^N random steps to see a reward. If each episode starts from a state on a stored demonstration and the start moves backward along it, the cost is about quadratic in N. They used one human demonstration and reached 74,500 on Montezuma's Revenge, above all earlier published results (and above the demonstrator, 71,500). Limits: needs a restorable emulator and one good demonstration.

Reading for us: a stored path turns one long search into a sum of short searches. Our version is "restart from the last verified step, not from the beginning".

### 2.2 Go-Explore (2019 preprint, 2021 Nature)

Phase 1 (explore until solved), a02, a03, a09:

- Archive of cells. Each cell stores a full trajectory, simulator state, score and length.
- Loop: pick a cell, restore it, take random actions, add any new cell.
- Exploration: k = 100 frames of random actions, 95% chance to repeat the previous action (Atari). The Nature version uses 30 actions and 90% repeat in robotics.
- Update rule: a new cell is added when first seen. An existing cell is replaced if the new path has a higher score, or is shorter at equal score. On replacement the selection counters (times chosen, times since progress) reset, so the cell is tried again. The times-visited counter does not reset. Cells built on the old path are not rewritten (limit: a better path may break those).
- Selection: weight built from counts (times chosen, times visited, how often a pick led to new cells). With domain knowledge, a neighbour bonus (fewer horizontal neighbours gives more weight), a key bonus, and a level factor 0.1 to the power (max level minus level).
- No neural network was used in Phase 1 in any experiment. Entirely random exploration worked.

Phase 2 (robustify): the backward algorithm trains a policy from demonstrations so it works under noise (sticky actions in the Nature version).

Cell representations (a04, a06, a10):

- No domain knowledge: grayscale, downscale to 11 x 8, pixel values rescaled to integers 0 to 8. Parameters by grid search. In the Nature version the downscaling is tuned during the run: target a cell count (a fixed share of the sample) plus the normalised entropy of how recent frames spread over cells.
- With domain knowledge: (x, y in 16x16 blocks, room, level, keys held) for Montezuma; (room, x, y) for Pitfall; MuJoCo internal state for the robot.

### 2.3 The theory and what tests it

Detachment and derailment are hypotheses. The papers do not isolate each by ablation (b08). Rival explanations that are not excluded: determinism plus restore, the cell key, and raw compute. What exists:

- Direct derailment evidence: one robot analysis. In 20 count-based intrinsic-reward runs, all found touch and grasp, but in 18 (90%) the visit count of the grasp step was at least 10 times lower than for touch (a12). Rarely visited cells should have had the highest bonus, yet were not revisited.
- A written argument that small fixed epsilon avoids derailment but under-explores, and annealed epsilon explores early with heavy derailment. Proposed fix: low noise in known areas, high noise at the frontier (a13). No measured effect size.
- The "explore after arrival" half is isolated by Yang et al. (a17, a18, b20) and Latent Go-Explore ablations (a20, b18). See section 5.

### 2.4 Cell-free and learned keys (2022-2023)

- **Latent Go-Explore** (a19, a20, b17, c09): learned latent space, goals picked from low-density regions, follow a subgoal path, then explore. In the maze only LGE and Go-Explore clearly beat random exploration; ICM-style curiosity, Skew-Fit and DIAYN did not. Quote: "If the cell partitioning is not informative enough, Go-Explore can completely fail to explore the environment". But full Go-Explore with domain knowledge found more cells (about 5k Montezuma cells for LGE).
- **Time-Myopic Go-Explore** (a21, a22, b19, c10): embedding where states close in time cluster. A state enters the archive only if it is far in predicted time from every cell. Archive is far smaller (Montezuma at score 2500: 2,838.9 native cells vs 566.0 and 248.3; Gravitar: 7,376 vs 381).

### 2.5 From games to language models (2020-2026)

- **Yuan et al. 2020** (c08): first Go-Explore on text games. Cells are binned word-embedding sums of room text plus cumulative reward; found trajectories are imitated by a Seq2Seq model.
- **Intelligent Go-Explore, IGE** (Lu, Hu, Clune; a23-a29): a language model replaces the three hand heuristics: which archived state to return to, which action to try, whether a new state is interesting enough to archive.
- **GLoW** (Kim and Hwang 2025; c18, c19, d04-d06): value-ranked frontier of best trajectories; the model reads patterns across them to pick where to resume; short bursts with multi-path reflection.
- **Archives of whole agents or programs**: Darwin Godel Machine (a34, c15-c17, d10), ShinkaEvolve (d08), Huxley-Godel Machine (d09), ADAS meta-agents (d07), Rainbow Teaming (c20, c21).
- **Archives of environment states for data**: Go-Browse (c22, d17).
- **First equal-token test**: Graviet and Shah 2026 (d01-d03). It is negative.

### 2.6 Relation to quality-diversity

The archive is close to MAP-Elites: one best elite per cell (a15). Differences: Go-Explore extends trajectories, not mutates policies, and cells index reachable places, not behaviour descriptors. No experiment compares them directly. See sibling subfield "Quality-diversity and novelty search".

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested. Numbers are from the critic-checked set unless marked.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Archive plus return solves Montezuma where curiosity fails (no domain knowledge) | Phase 1 mean 57,439 (CI 47,843-67,224), level 1 solved in 57% of 100 runs, mean 640M frames, 10.8 h; prior intrinsic best about 17,500 and 10% level 1 | a01, a05, b01 (Ecoffet 2019) | E (K01) |
| Same idea from one demonstration | 74,500 on Montezuma; exponential to quadratic on toy cliff walk | a33 (Salimans and Chen 2018) | E (K01) |
| Cell design is the main lever | domain-knowledge cell: mean 148,220 (CI 144,580-151,730, 50 runs), level 1 after 57.6M frames (0.9 h); about 11x cheaper than 640M | a06, b02 | E (K02) |
| Generic image cell fails on Pitfall | 22 rooms, no positive reward; with (room,x,y) 40 rooms, mean 70,264 | a04, a07 | E (K02) |
| Nature version: robustified scores | Montezuma 1,731,645; Pitfall 102,571; beats SOTA on all 11 hard games (Freeway tie); beats Agent57 on 7 of 11; exploration alone beats SOTA in 83.6% of 55 games | a08, b05 | S (one group) |
| Robustified arXiv version (do not mix with Nature) | Montezuma 666,474 with domain knowledge, 43,763 without; Pitfall 59,494 mean, max 107,363 | b02, c07 | S |
| Robustification from one demo is fragile | 40% success single demo; 5 of 5 with 10 demos; 51 of 57 best paths used a game bug | a05, b03 | E (K06) |
| Robot pick-and-place | exploration found a path in 198 of 200 runs (99%); robustified 99%; plain PPO and count-based PPO found no reward (control had 50x more frames) | a11, b07 | S |
| Policy-based return (no restore) still works but scores less | Montezuma 97,728; Pitfall 20,093 (vs 102,571 with restore); sampling the policy found 4x more cells than random | a14, b06 | S (K18) |
| Derailment, direct count | 18 of 20 robot control runs: grasp visit count at least 10x lower than touch | a12 | S (K05) |
| Post-exploration helps | on beat off in all three MiniGrid tasks; effect larger than tuning epsilon; fixed 20 steps or 0.8 of path length best; decay 0.01-0.05 slightly better than always; decay 1.0 hurts | a17, a18, b20, b21 | E (K04) |
| Ablating post-goal exploration lowers coverage | significant drop in maze (figure) | a20, b18 | E (K04) |
| Archive bloat | Montezuma native cells at score 100/400/500/2500: 126/198/1,812/2,839 vs 160/203/450/566 (time-myopic); Gravitar 7,376 vs 381 | a22, c10 | E (K09) |
| Native beats learned key on raw score | Montezuma at 1M frames 2,303 native vs 695 (time-myopic); Frostbite 11,721 vs 3,543; Gravitar 2,130 vs 2,533 (time-myopic ahead) | a21 | C (K17) |
| IGE on Game of 24 | 100% in 150 ops, 70.8% faster than DFS (p<0.05); GPT-4 naive 70, ReAct 82, Reflexion 83 | a23, a27 | E (K07, with GLoW) |
| IGE on TextWorld (25 seeds, 240 steps) | Cooking 92 vs ReAct 56, Reflexion 52, naive 40; Treasure Hunter 96 vs 84, 80, 64; Coin Collector about 88 (figure, approximate) vs 0 for all others | a24 | E (K07) |
| IGE on BabyAI (250 steps) | text Put Next To 84 vs ReAct 48; Open Door 64 (equal to best); vision Put Next To 52 vs 8; RL baseline GLAM needed 1.5M steps (4%) | a25 | E (K07) |
| IGE ablation (Game of 24 / BabyAI / Cooking) | full 100/84/92; no action choice 68/24/0; no state choice 96/48/76; no filter 93/64/64; none of the three 61/4/0; no action history 33/72/72; classic Go-Explore 38/4/0 | a26, critique | S (K08) |
| IGE archive size | BabyAI 203.5 to 25.5 states with filter; Cooking 22.4 to 4.4; Game of 24 18.5 to 15.6 (ratio 8.0x, 5.1x, 1.2x) | a28, critique | E (K09) |
| IGE across base models (Game of 24) | GPT-4 70 to 100; Llama-3 400B 44 to 98; Sonnet 3.5 24 to 86 (vs Reflexion 80, not significant) | a27, b14 | S (K10) |
| IGE with generic prompts | 96% vs 100% tuned; malformed outputs under 0.1% | a29, b27 | S (K11) |
| IGE at near-equal cost on Jericho (GPT-4.1-mini, 1,000 steps, 3 seeds) | IGE vs ReAct: Zork1 44.3 vs 48.3; Deephome 71.3 vs 11.0; Detective 316.7 vs 113.3; Enchanter 50.0 vs 46.7; Ludicorp 28.3 vs 19.7; Pentari 30.0 vs 30.0; Ztuu 15.0 vs 18.7; cost $4-6 per run for all | d04 | S (mixed) |
| GLoW beats IGE on most Jericho games | Zork1 73.0; Ludicorp 73.7 vs 32.0 (ICRL); Enchanter 61.7 vs 50.0 (IGE); GLoW beat IGE on 8 of 10 | c18, d04, d05 | S |
| Burst length after resume | 50-step bursts, 3 per selection best: Zork1 59.0/67.3/73.0/63.0/59.3 for n=1..5; Ludicorp 34.0/66.0/73.7/62.0/53.3 | d06 | S (K29) |
| Archive of agents beats greedy and no archive (DGM, 80 iterations) | SWE-bench 50.0 vs greedy 39.7 vs no-archive 23.0 vs no self-improvement 39.0; Polyglot 38.0 vs 30.0 vs 14.0 vs 28.0; working-agent share 51.3% vs 32.5% | a34, b15, c15, c16 | S (K12, one run per arm) |
| Resume rule by code beats best-score-only | DGM weight = sigmoid(10*(score-0.5)) / (1+children); HGM clade score correlation 0.778 / 0.626 vs DGM 0.285 / 0.383 and SICA 0.444 / 0.274; ShinkaEvolve weighted sampling beats hill climbing | d08, d09, d10 | E (K26, 3 sources) |
| Low-scoring parents seed good lineages | parent score vs descendant productivity correlation 0.28-0.44; dips at DGM iterations 4 and 56 led to later bests (anecdote) | b16, d09, d10 | S (K13) |
| Cheap code dedupe does most of the filter job | embedding similarity reject above 0.95 gave substantial gain; extra LLM novelty judge marginal (figure only) | d08 | S (K27) |
| Showing the whole archive to the generator hurts | ADAS-style: all prior designs 55.0, ignore prior 60.0, top-7 60.3 (MGSM 41.4 / 56.2 / 56.5) | d07 | S (K28) |
| Equal-token test, snapshot archive vs retry (Haiku 4.5, Terminal-Bench 2.0, 5 tasks x 5 seeds, 1M tokens) | retry 17/25 (68%) vs snapshot branching 6/25 (24%); resumed children rescued 67% of failed roots on extract-elf (retry 38% on that task) | d01, d02 | S (K23) |
| Wide first, deep later (ARC, checker) | 128 calls: GPT-4o repeated sampling 15.0 vs tree 8.7-14.0; DeepSeek-V3 18.6 vs 10.0-18.3. At 6,000 candidates: refine beats sample, 7B 14.25 vs 5.63, 72B 25.62 vs 18.50 | d11, d13 | E (K24) |
| Checker-guided population search (planning) | TravelPlanner 95.6% vs best-of-N 55.6% ($0.29 vs $0.47); Trip Planning 96.2% vs 77.2% ($0.17 vs $0.10); Meeting Planning 85.0% vs 69.4% ($0.52 vs $0.39) | d12 | S (K25) |
| Coverage keeps rising with independent samples | log-linear over 4 orders of magnitude: CodeContests Gemma-2B 0.02% to 7.1% at 10,000; SWE-bench Lite 15.9% to 56% at 250; MATH coverage 82.9% to 98.44% | d14 | E (K32) |
| Final pick must be a real check | MATH majority vote or reward model 40.50% to 41.41% while coverage hit 98.44%; SWE-Search value 73% vs separate discriminator 84% | d14, d16 | E (K33) |
| Seed variance can exceed algorithm effect (red-team archive, GPT-4o-mini) | 0 to 16 findings over 5 seeds; seed 42 gave 16 vs mean 4.6; 3-4 seeds to stabilise | a30, b23, c13 | S (K15) |
| State key collapse | 96% of attack intents in one cell under tool-name hash | b24, c14 | E (K03, with Pitfall) |
| Reward add-ons interfere | reward bonus plus granular signatures: findings down 94% (161); reward alone 18 false positives, 0 attacks; all three: 0 findings | a31, b24, c13 | S (K14) |
| Returning to stored pages widens coverage (Go-Browse) | 1 reset 183 URLs, 5 resets 214, 15 resets 260; feasibility check saved 13% of steps; resume benefit larger for weaker solver (figure) | c22, d17 | S (K35) |
| Mid-chain return in RL training (FR3E) | +1.8, +3.0, +3.1 average points over GRPO++ on 8 math benchmarks; no gain on AIME24 for the math-specialised base | d15 | S (K36) |
| Plain LLM agents explore poorly | Reflexion no better than ReAct on long text games; Qwen3-235B maze coverage 52.7% easy, 23.0% medium, 29.1% hard | b13, c03, c24 | E (K20) |

## 4. Mechanisms and models

Each mechanism is written so an engineer can build it. All of it is code unless marked "model slot".

### 4.1 Archive entry

```
Entry {
  key        : string          # the cell id (see 4.3)
  state      : text            # partial solution, restorable verbatim
  path       : list            # steps/prompts that produced it (shortest known)
  score      : number          # from a code check, never from the model (K33, G8)
  length     : int             # tokens or steps used to reach it
  n_chosen   : int             # times picked as a resume point
  n_seen     : int             # times a run re-found this key
  n_children : int             # entries created from resuming here
  child_best : number          # best child score so far
  verified   : bool            # passed the check on unfitted input (G3)
  why        : string          # one line, model slot: why believed good (K30)
}
```

### 4.2 Update rule (from Go-Explore, a03)

1. Compute the key of a new partial result.
2. If the key is new: add the entry.
3. If the key exists: replace only if score is higher, or score is equal and length is shorter. On replacement reset n_chosen and the "since progress" counter, but not n_seen.
4. Known limit: cells that were built on the old path keep the old path. For us, re-verify children when a parent path changes.

### 4.3 State key (cell) design

This is the main lever (K02: about 11x on Montezuma). Design rules that follow from the evidence:

- Use a few facts about progress, not raw similarity. In Montezuma (room, level, keys, coarse position) beat the downscaled image (a06).
- Too coarse merges states that need different actions. Pitfall had identical-looking screens (a04). The red-team hash merged 96% of attack intents into one cell (b24).
- Too fine fills the archive. Native Go-Explore grew to 2,839 cells where 566 sufficed (a22).
- Keep the cell count near a target and the items spread evenly: the Nature rule scores a key by distance from a target count plus normalised entropy of how recent items spread over cells (a10). This works for any abstraction.
- Where the task offers a natural key, use it (URL in Go-Browse, d17; test id or file diff in coding, d03).
- Behaviour keys work for programs: group by output on the checker inputs (SOAR groups by output grid, d13).
- Where progress is hidden outside the saved state, the key and state must include it (database-style progress needed a full snapshot: 4/5 vs 0/5, d03). For a model, progress that lives only in hidden reasoning cannot be restored. Write it out.
- No head-to-head test of keys for a reasoning agent exists (K31).

### 4.4 Selection (which entry to resume)

Three designs have been tested:

- **Count-based** (Go-Explore): weight from times chosen, times seen, how often a pick led to new cells; bonuses by hand. Cheap, no model call. IGE shows it collapses in text tasks when paired with random actions (classic Go-Explore 38 / 4 / 0), but the weight vs uniform ablation is "data not shown" in the original (b04).
- **Code formula on score and children** (DGM): `w = sigmoid(10*(score - 0.5)) * 1/(1 + children)`; every non-perfect entry keeps a non-zero chance. Greedy best-only lost 10 points (39.7 vs 50.0; 30.0 vs 38.0). ShinkaEvolve and HGM agree in direction (K26). HGM improves on it by scoring the whole clade (descendant results) with Thompson sampling.
- **Model-chosen** (IGE; GLoW): the model picks. GLoW shows a model that reads whole top trajectories beats a model that judges single states (Zork1 73.0 vs 62.0 vs IGE 44.3). Nobody compared a model selector with a code rule.

Safe default for us: a code rule (G8 holds by construction). Use the DGM formula first, then switch to descendant results once an entry has a few children.

### 4.5 Return (restore)

- For text states, restore is a re-prompt with the stored state. It is exact and free in tokens except the prompt itself.
- Restoring also restores mistakes (K30): plausible but wrong partial solutions are sticky, and a fresh agent re-pays the understanding cost (child 190k tokens over 26 steps vs 90k over 11 for a fresh retry, d02). Pass a short summary of why the entry is believed good, and let the resumed run challenge it once.
- No exploration noise while returning. Explore only after arrival (a13).

### 4.6 Explore after arrival (burst)

- Original: 100 random actions with sticky repeats (not applicable to text).
- RL study: post-explore a fixed 20 steps or 0.8 of the path length; adaptive decay of 0.01-0.05 on visit count slightly better; full decay hurts (a18).
- LLM study: about 3 bursts of 50 steps per selected state, then re-select (d06). Part of the effect is the reflection step that needs more than one burst.
- Fresh context per attempt matters too (SCHEMA S3). A burst should start from the stored state alone, not from the whole history (K28).

### 4.7 Filtering and size control

- Native Go-Explore filters by cell identity only.
- IGE asks a model "is this new state interestingly new?" and prunes exhausted states. That cut archives 8x on BabyAI and 5x on Cooking, but only 1.2x on Game of 24 (K09).
- ShinkaEvolve: reject candidates above 0.95 embedding similarity. The extra model novelty judge was marginal (K27).
- Rainbow Teaming: text similarity 0.6 dropped about 24% of candidates (c21).
- Default for us: code dedupe on a normalised form, a size cap, deletion of exhausted entries (all children failed). A model novelty judge only if an equal-token test shows it pays (K27).

### 4.8 Robustify step (G3)

The raw best archive path is not a result. It must be re-run under variation. For us: re-run every archived solution on a mutated or held-out input before it can be resumed or returned (K06, K34). Strong search finds exploits (51 of 57 runs used a bug; DGM shows objective hacking in an appendix, c17). The checker must sit outside the model's reach.

### 4.9 Budget: wide, then deep

Evidence for a two-stage budget:

- Independent sampling coverage rises log-linearly (K32), and wide sampling beat tree refinement at 128 calls on ARC (K24).
- Refinement beat fresh sampling at 6,000 candidates (K24). Plateaus: repeated sampling on ARC beyond about 500 calls; SOAR 7B near 5.2k attempts.
- Archive overhead: the root run and each resume cost tokens, so a weak root means a weak archive (K23).

Design: spend the first slice on independent attempts (these become the first archive entries), then spend the rest on resumes from the best entries, with the switch point logged.

### 4.10 What the model does and does not do

Model slots: write an attempt from a stored state, name what is wrong in a failing output, write the one-line "why believed good". Code does: key, score, selection, dedupe, restore, budget, verification. This matches SCHEMA section 1. IGE's own design gives the model the three choices; our schema keeps the choices in code unless an equal-token test says otherwise.

## 5. What holds up

### 5.1 Replications and independent confirmations

- **Return-then-explore principle.** Independent groups reached the same shape: Salimans and Chen (2018) before Go-Explore, Latent Go-Explore and Time-Myopic Go-Explore after it, stress testing for cars (a32). K01 is established.
- **Post-exploration.** Yang et al. (a17) and the LGE ablation (a20) agree. Both are small environments, curves not tables (K04 established, small effect sizes).
- **Archive size control.** Native Go-Explore bloats (time-myopic), IGE's model filter cuts archives, ShinkaEvolve's code filter does most of the same (K09, K27).
- **Resume rule beyond best score.** DGM, ShinkaEvolve and HGM all beat best-score-only (K26 established, three sources).
- **Wide first, deep later.** AB-MCTS and SOAR agree (K24 established).
- **Selector must be a real check.** MATH coverage vs vote, and SWE-Search value vs discriminator (K33 established).

### 5.2 Failures, negative results, contested items

- **Equal-token test is negative.** Haiku 4.5 on Terminal-Bench: retry 17/25 vs snapshot archive 6/25 (d01). The authors expected the opposite. Named causes: budget fragmentation, wrong-state attractors, handoff cost, weak progress signals (d02). Limits: heuristic selector, not IGE's model; baseline is retry only; five tasks; preprint.
- **IGE is not uniformly better than ReAct** at near-equal cost: Zork1 44.3 vs 48.3 and Ztuu 15.0 vs 18.7 (ReAct ahead), Pentari 30.0 vs 30.0 (d04). It wins by large margins on Deephome and Detective. Pattern: helps on long dead ends, not elsewhere.
- **Learned keys: contested.** Authors report parity or gains. The tables show native Go-Explore ahead on Montezuma (2,303 vs 695) and Frostbite (11,721 vs 3,543), and LGE finds about 5k cells (K17).
- **Reflexion.** IGE says it hurts on long text games (the context-length reason is untested). On Game of 24 it was second best (83; 80 for Sonnet). It is one paper's reading (critique).
- **Reward add-ons can destroy an archive search** (red-team: -94%, all combined 0 findings, K14). Seed 42 gave 16 findings vs mean 4.6 (K15). Single-seed conclusions are unsafe. This paper is a preprint: 28 runs, mostly one seed, one model, 70-90% false positives.
- **Show-all-archive hurts the generator** (K28, single source).
- **Model-based IGE gains shrink against a strong reflector.** On Sonnet 3.5, IGE 86 vs Reflexion 80 was not significant (K10).
- **DGM caveats.** One run per arm, about 22,000 USD for a SWE-bench run, objective hacking appendix. The headline gap (50.0 vs 23.0) is the largest archive-vs-no-archive gap for an LLM loop but has no variance estimate.
- **Restore is not the whole story, and is not free for real tasks.** Policy-based Go-Explore scores 5x lower on Pitfall (20,093 vs 102,571). Text-game restore replays a command list, which is cheap and exact. Restoring a model's reasoning state is not possible. Only written-out state can be restored.
- **Derailment** has one direct test (robot, 18 of 20). In Atari it is argued, not measured.

### 5.3 Moderators

- **Horizon.** Gain grows with horizon: short Game of 24 benefits most from LLM action choice; long BabyAI and Cooking benefit most from state selection and filtering (K08). Stress testing: archives win on long horizons, MCTS wins at medium, deep RL wins when there is a dense reward (K19). No archive gain on some Jericho games.
- **Base model.** Larger gain for weaker models in IGE (24 to 86 vs 70 to 100). Mixed neighbours: SOAR gain does not shrink 7B to 123B (+6.5 to +12.4 points). SWE-Search relative gain smallest for GPT-4o. The one 2026 test (Haiku 4.5) was negative. Not measured at the current frontier.
- **Cell design.** Order of magnitude on Montezuma.
- **Checker availability.** Population and refine loops need an exact evaluator (K25). Without one the gain should vanish; model value picks 73% vs discriminator 84% (K33).
- **Seeds.** Variance can exceed algorithm effects (K15).

### 5.4 Interventions that worked and did not

| Worked | Did not work or hurt |
|---|---|
| Archive of stored states with return first | Curiosity bonus alone (Montezuma, Pitfall, robot) |
| Cheap easy domain facts in the key | Raw image similarity on partially observed screens (Pitfall 22 rooms) |
| Explore after arrival (about 20 steps in RL; about 3 bursts of 50 in LLM text games) | Decay of post-exploration to zero |
| Parent weight by score and few children (code) | Best-score-only (greedy), latest-only |
| Code embedding dedupe at 0.95; size cap | Giving the generator the whole archive |
| Model filter in long text tasks (IGE) | Reward bonuses stacked on granular signatures (red team) |
| Wide sampling first, refinement later | Tree refinement at small budgets (ARC at 128 calls) |
| Code-run checker as picker | Majority vote or reward model as picker at high N |
| Robustify under variation | Trusting the single best raw trajectory |

## 6. Language models

How they behave on these tasks, what changed it, by how much.

**Plain agents.** Reasoning-tuned models reach the goal in text mazes but not efficiently, and open-weight reasoning models loop: Qwen3-235B coverage 52.73% easy, 23.04% medium, 29.11% hard; direction biases (UP/RIGHT); few-shot demos cut GPT-5-mini path length from 60 to 28 on the easy layout (c24). Reflexion did not beat ReAct on long text games (b13). Without frontier bookkeeping the model drifts and forgets.

**What an archive loop changed (IGE).** Game of 24: GPT-4 70 to 100; Llama-3 400B 44 to 98; Sonnet 3.5 24 to 86 (a27). TextWorld Cooking 92 vs ReAct 56. BabyAI Put Next To 84 vs 48, and vision 52 vs 8. Coin Collector about 88 vs 0 (approximate, from a figure). 250 environment steps against 1.5M for the RL baseline (a25). Domain-general prompts lost 4 points on Game of 24 (96 vs 100); malformed outputs under 0.1%.

**Which part of the loop carries it.** Short task: model action choice and per-state action history. Long task: model state selection and archive filtering (K08). Random actions as in classic Go-Explore collapse in text (4 on BabyAI, 0 on Cooking).

**Independent re-run (GLoW, GPT-4.1-mini, 1,000 steps, 3 seeds, about $4-6 per run for all LLM methods).** IGE beats ReAct on Deephome (71.3 vs 11.0) and Detective (316.7 vs 113.3). It ties or loses on Zork1, Ztuu, Pentari, Enchanter (small gains). GLoW's frontier plus model reading of whole trajectories beat IGE on 8 of 10 games. Standard errors of 10 to 26 points on some games, so small gaps are noise (d05).

**Where it goes wrong.**

- Equal-token coding test, Haiku 4.5: retry 68% vs archive 24% (d01). Cost of building and resuming the archive was not repaid.
- Model-judged "interesting" is a bias risk (b27: a model that thinks nothing "purple" is interesting would never explore purple states). Not measured.
- A model judge for novelty added little over code dedupe (d08).
- Model value picks 73% vs discriminator 84% (d16); majority vote or reward model stalls at 41% while coverage reaches 98% on MATH (d14).
- Meta-agents shown the whole archive did worse than those shown none (d07).

**Closest neighbours with a checker (reasoning and code).**

- ARC as program synthesis: at 128 calls, repeated sampling beat tree variants (GPT-4o 15.0 vs 8.7-14.0; DeepSeek-V3 18.6 vs 10.0-18.3). At 6,000 candidates, half refinements beat all fresh (7B 5.63 to 14.25; 72B 18.50 to 25.62; Mistral-Large-2 19.75 to 26.25). One-shot references: GPT-4.1 8.00, Claude-4-Sonnet 20.75, o3-mini 38.25 (d11, d13, d18).
- Planning with a checker: Mind Evolution beat best-of-N by +15 to +40 points at comparable cost per instance (d12).
- Math inside one chain: FR3E restarts from high-entropy prefixes gave +1.8 to +3.1 points in RL training (d15).

**Not found.** A measured IGE-style archive of partial reasoning steps (proof steps, math chains) with a model picking the resume point (K21). This is an absence in the search tools used, not proof.

**Budget note.** Almost every LLM number is at equal steps, calls or candidates, not tokens, and uses 2024 to early 2025 models. Only Graviet and Shah used a 2026 model, and it was negative. Treat every positive number as "unverified at equal tokens".

## 7. What our agent should take

Schema parts: G (guardrail), S (state), O (operator), memory. Status: [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

These are small, code-side and low-risk. None of them needs a model call. Each is also consistent with G7: if the equal-token run says otherwise, it goes.

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| A1. Keep partial results that passed a check in a code-held store, with the shortest path to each; show the model only a filtered few, never the whole store | memory, S6 | [E] | K01, K07, K20; a01, a23, c03, d07 |
| A2. Resume rule runs in code, not by the generating model: weight = sigmoid(score) / (1 + children), every non-perfect entry keeps a non-zero chance | S6, G8 | [E] | K26; d08, d09, d10 |
| A3. Dedupe by code on a normalised form and cap the store size; delete exhausted entries | memory, G7 | [E] | K09; a22, a28, c10, d08 |
| A4. Re-check every stored solution on a mutated or held-out input before it can be resumed or returned (the Go-Explore robustify step) | G3, S8 | [E] | K06; a05, b03, a16 |
| A5. Final answer is picked by a code-run check where one exists; a vote or the generator's own score never picks | G5, G8, S7 | [E] | K33; d14, d16 |
| A6. Budget order: first slice for independent attempts (breadth), then resume and refine the best (depth); log the switch point | G12, S3 | [E] | K24, K32; d11, d13, d14 |
| A7. Do not cap independent attempts at 20 when a checker exists; choose N from a pilot coverage curve | G12 | [E] | K32; d14 |
| A8. Evaluate every archive variant on at least 25 problems and 3 to 5 repeats; never conclude from one run | G7 | [S] but cheap and also consistent with IGE's own design (25 to 100 seeds) | K15; a30, b23 |

A8 is single-source as a finding, but we are adopting it as an evaluation rule, not a schema element.

Also keep the already-established limits of SCHEMA 4b: no model-opinion revision, no debate. The archive loop must not become a second place where the model judges itself.

### 7.2 Test first (not yet allowed into SCHEMA.md)

| Item | Schema part | Status | Evidence | Why it waits |
|---|---|---|---|---|
| T1. Whole archive-of-partials loop (return to the best stored partial instead of restarting) vs repeated sampling vs best-of-N vs retry-with-reflection | S6, memory | [C] (positive on games, negative at equal tokens) | K07, K23; d01, d04 | Only equal-token test is negative |
| T2. Model-picked resume point vs code rule | S6, G8 | [S] | K26, d05, K08 | Never compared |
| T3. Model novelty/filter judge vs code dedupe | memory | [S] | K09, K27; a26, d08 | Model filter mattered on long tasks in IGE; marginal in Shinka |
| T4. State key: normalised answer vs plan skeleton vs execution output on checker inputs | memory | [S] | K02, K03, K31 | No head-to-head |
| T5. Burst length after resume: about 3 short attempts | S6 | [S] | K04, K29; d06 | RL and games only; no root-restart control |
| T6. Resume from lower-scoring entry once | S6 | [S] | K13; d09 | Count missing |
| T7. Resume point inside a chain at a high-disagreement step | O3 | [S] | K36; d15 | Training result only |
| T8. "Why believed good" line plus one challenge step on resume | G3, S5 | [S] | K30; d02 | Single trajectory evidence |
| T9. Gate by horizon: use archive only when expected depth is high or the class is stuck | S0, G12 | [S] | K19, K08, d04 | Needs the class pass-rate data |
| T10. Show the resumed run its own entry only (or entry plus top 3) | G8, S3 | [S] | K28; d07 | Other domain |
| T11. Reward-style bonuses on entry scores (novelty, causality) | memory | [S] negative | K14 | Default to none; add one at a time |
| T12. Gain by model strength | G7 | [S] | K10; d18 | Frontier not measured |

## 8. Concrete tests on our bench

All arms use equal total tokens: root runs, selection calls, resume calls, filter calls, verification and setup all counted (G7). Use at least 25 items and 3 repeats per arm (K15). Log, for every resume, the source entry's score, child count and result (this yields tests T6 and the failure-share count for free).

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 (T1, gap 1) | ARC-style items with a checker (at least 40) plus a math or code set with a checker (at least 40) | (a) repeated sampling; (b) best-of-N with checker; (c) retry with reflection; (d) archive: first 40% budget breadth, then resume from the best entries by the DGM rule, about 3 short bursts | solved items at equal total tokens; tokens per solved item | Archive wins on hard ARC items (K24 at larger budgets) and loses or ties on easy ones. Expect no win on the easy half (d01, d11). Keep only if it wins on the hard half by at least 5 points over (b) |
| E2 (gap 7) | same sets | arm (d) vs best of (a)-(c) with two model strengths (nano and our strongest) | gain by strength | Gain shrinks with a stronger model (K10); SOAR suggests it may not |
| E3 (T4, gap 3) | the E1 set | archive with three keys: normalised final answer; plan skeleton; execution output on checker inputs | distinct useful entries per 100k tokens; cell count; share in largest cell; solved items | Execution-output key best; answer key collapses (K03, d13). Largest-cell share above 50% flags collapse |
| E4 (T2, gap 4) | the E1 set | resume point by code rule vs by model choice vs uniform | solved items; tokens | Code rule within 2 points of the model rule at lower cost; model rule favors familiar states |
| E5 (T3, gap 5) | long multi-step planning items | no filter vs code dedupe at 0.95 plus size cap vs code dedupe plus model novelty judge | solved items; archive size; tokens per step | Code dedupe gets most of the gain (K27). Keep the model judge only if it adds at least 3 points at equal tokens |
| E6 (T5, gap 6) | the E1 set | resume with 1, 3, 5 short attempts per selection; plus a restart-from-root control | solved items | 3 best (d06); root-restart control is the missing comparison |
| E7 (T6, gap 8) | the E1 set | resume only from top scorers vs allow one resume from a lower scorer | share of final answers whose lineage includes a low scorer | At least 10% of wins pass through a lower scorer (HGM r about 0.3 to 0.4) |
| E8 (T8, gap 10) | the E1 set | archive without re-check vs with mutated-input re-check on entry | failure share of archived solutions on mutated input; final accuracy | A non-trivial failure share (SOAR notes brittle hard-coded programs); re-check raises final accuracy |
| E9 (T8) | stuck items (plain pass rate zero after 2 rounds) | resume with summary only vs summary plus one challenge step vs fresh | rescue rate of stuck items | Challenge step reduces wrong-state sticking (d02) |
| E10 (T10) | the E1 set | resumed run sees: own entry only; own plus top 3; entire archive | solved items; diversity of final candidates | Whole archive worst (K28) |
| E11 (T7) | multi-step math chains | resume inside chain at disagreement step vs restart | solved items | Small gain (+2 to 3 points, d15) |
| E12 (T9) | mixed difficulty | always archive vs archive only when class pass rate is low or the impasse detector fires | solved items; tokens | Gated archive wins at equal tokens; always-on loses on easy items (G11) |

## 9. What does not transfer, and why

- **Atari scores and frame counts.** Numbers such as 1.7M on Montezuma do not map to reasoning. Use the shape of the result (archive beat curiosity, key quality gave 11x), not the size.
- **Random exploration.** Entirely random actions worked in Atari. In text, classic Go-Explore (random actions) collapsed (38 / 4 / 0). Language needs model-generated extensions.
- **Simulator restore as a scarce asset.** For Go-Explore it was the strong assumption (policy-based version 5x lower on Pitfall). For us a stored text state is free to restore. But restore does not return the model's hidden reasoning, and restoring a state brings back its mistakes (K30).
- **Derailment.** It is about noise stopping a return. Returning to a stored text prompt is deterministic. Derailment as a mechanism does not apply. Only the consequence matters: a resample-from-scratch loop loses partial progress (K05 is single-source and not directly testable).
- **Cell hand-design by game facts.** A key like (room, level, keys) has no counterpart for open reasoning. We must find our own cheap progress facts (K31).
- **Backward-algorithm robustification as a training step.** There is no policy to train. Only the principle transfers (re-test under variation, keep several diverse solved paths).
- **Training-time data collection.** Go-Browse and FR3E are training methods. Their inference-time value is unmeasured.
- **Safety red-teaming counts (N=20 saturation).** That counts attack types; solved-problem coverage keeps rising on checkable tasks (K16 vs K32).
- **Self-modifying agent archives (DGM, HGM).** They improve agent code over 80 iterations at 22,000 USD per run. We keep only the parent rule.
- **IGE comparison with Tree of Thoughts.** 74% is from another setting. Not comparable (b11).
- **Games with admissible action lists and known walkthroughs.** Jericho may be partly known to the model (contamination probe under 20%), and valid-action lists ease exploration.

## 10. Open questions

The ten gaps from the critique, with their status after the gap pass:

1. Does an IGE-style archive of partial solutions beat best-of-N and ReAct at equal total tokens, including state-selection and novelty calls? One negative result (heuristic selector, retry baseline only). Open for IGE selection.
2. Does an archive loop help on pure reasoning or code-step tasks with a checker beyond Game of 24? Partly answered for neighbours (K24, K25), not for Go-Explore itself (K21).
3. Which state key works: raw text, normalised answer, plan skeleton, execution trace? Open as a head-to-head (K31).
4. Does model-picked resume bias toward familiar states, and does G8 apply to archive choice? Mostly closed for code rules (K26), open for a model-vs-code comparison.
5. How large should the archive be and who deletes? Partly closed: code dedupe plus cap (K27), one task, figure only.
6. How long a burst after resuming? Partly closed: 3 bursts of 50 steps (K29). Missing: short burst vs root restart at equal tokens.
7. Does the gain shrink with stronger models? Not measured at the current frontier (K10, d18).
8. Is resuming from a lower scorer useful, as a count over many runs? Mechanism supported (r about 0.3 to 0.4), count missing.
9. How many parallel runs before diversity saturates? Closed for checkable tasks (K32); the N=20 point is for attack types.
10. What share of archived solutions fail on a mutated input? Open. No study reports a rate (K34).

New questions raised by this pass:

- How much of the DGM and Jericho gains come from the archive and how much from extra samples? No source separates them at equal tokens.
- Does a written-out "why believed good" line reduce wrong-state sticking (K30)? Single trajectory only.
- Does archive value depend on whether the check is dense (score) or sparse (pass/fail)? Stress testing says archives win without dense reward; DRL wins with it (K19).
- Can the clade-score idea (HGM) be made cheap for small archives?
- Do shared archives across problems of one class help (a library of solved subgoals; link to Library learning)?

## 11. Sources

[V] opened (full text read); [M] snippet only.

1. [V] Ecoffet, Huizinga, Lehman, Stanley, Clune (2019, v4 2021) Go-Explore: a New Approach for Hard-Exploration Problems. https://arxiv.org/abs/1901.10995 (a01-a07, b01-b04, b08, b09, b26 partly, c07)
2. [V] Ecoffet et al. (2021) First return, then explore. Nature 590. https://arxiv.org/abs/2004.12919 (a08-a16, b05-b07, b26)
3. [V] Salimans and Chen (2018) Learning Montezuma's Revenge from a Single Demonstration. https://arxiv.org/abs/1812.03381 (a33)
4. [V] Yang, Moerland, Preuss, Plaat (2022) When to Go, and When to Explore: The Benefit of Post-Exploration in Intrinsic Motivation. https://arxiv.org/abs/2203.16311 (a17, a18, b20, b21, c11)
5. [V] Galloudec and Dellandrea (2023) Cell-Free Latent Go-Explore. https://arxiv.org/abs/2208.14928 (a19, a20, b17, b18, c09)
6. [V] Hoftmann, Robine, Harmeling (2023) Time-Myopic Go-Explore. https://arxiv.org/abs/2301.05635 (a21, a22, b19, c10)
7. [V] Koren and Kochenderfer (2020) Adaptive Stress Testing without Domain Heuristics using Go-Explore. https://arxiv.org/abs/2004.04292 (a32, b22, c12)
8. [V] Badia et al. (2020) Agent57. https://arxiv.org/abs/2003.13350 (b10; per-game values not extracted)
9. [V] Yuan et al. (2020) Exploration Based Language Learning for Text-Based Games. https://ar5iv.labs.arxiv.org/html/2001.08868 (c08; HTML page, not PDF; text and table disagree slightly)
10. [V] Lu, Hu, Clune (2025, ICLR) Intelligent Go-Explore. https://arxiv.org/abs/2405.15143 (a23-a29, b11-b14, b27, c01-c06)
11. [V] Zhang, Hu, Lu, Lange, Clune (2026, ICLR) Darwin Godel Machine. https://arxiv.org/abs/2505.22954 (a34, b15, b16, c15-c17, d10). Appendix safety case (b28) was a heading only: [M].
12. [V] Bhatt, Wood, Habler, Al-Kahfah (2026) Large Empirical Case Study: Go-Explore adapted for AI Red Team Testing. https://arxiv.org/abs/2601.00042 (a30, a31, b23-b25, c13, c14)
13. [V] Kim and Hwang (2025) Dual-scale world models for LLM agents towards hard-exploration problems (GLoW). https://arxiv.org/abs/2509.24116 (c18, c19, d04-d06). Ablation table not cleanly extracted in the first pass (c19); d05 and d06 read it.
14. [V] Samvelyan et al. (2024) Rainbow Teaming. https://arxiv.org/abs/2402.16822 (c20, c21). Not re-opened by the critic.
15. [V] Gandhi and Neubig (2026) Go-Browse. https://arxiv.org/abs/2506.03533 (c22, d17). Prefixed-vs-unprefixed result is in a figure only.
16. [V] Zhang et al. (2023) Large language models are semi-parametric reinforcement learning agents (Rememberer). https://arxiv.org/abs/2306.07929 (c23). Not re-opened by the critic.
17. [V] Sandfuchs, Melchert, Frochte (2026) LLMs for text-based exploration and navigation under partial observability. https://arxiv.org/abs/2604.09604 (c24). Not re-opened by the critic.
18. [V] Graviet and Shah (2026) Returning to Development States: When Full Sandbox Snapshots Help Coding Agents. https://arxiv.org/abs/2610.13841 (d01-d03)
19. [V] El, Yuksekgonul, Zou (2025) Inefficiencies of Meta Agents for Agent Design. https://arxiv.org/abs/2510.06711 (d07)
20. [V] Lange, Imajuku, Cetin (2025) ShinkaEvolve. https://arxiv.org/abs/2509.19349 (d08; effect sizes from text, figures not read as numbers)
21. [V] Wang et al. (2025) Huxley-Godel Machine. https://arxiv.org/abs/2510.21614 (d09)
22. [V] Inoue et al. (2025) Adaptive Branching Tree Search (AB-MCTS). https://arxiv.org/abs/2503.04412 (d11)
23. [V] Lee et al. (2025) Evolving Deeper LLM Thinking (Mind Evolution). https://arxiv.org/abs/2501.09891 (d12)
24. [V] Pourcel, Colas, Oudeyer (2026) SOAR, Self-Improving Language Models for Evolutionary Program Synthesis. https://arxiv.org/abs/2507.14172 (d13, d18)
25. [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d14)
26. [V] Zheng et al. (2025) First Return, Entropy-Eliciting Explore (FR3E). https://arxiv.org/abs/2507.07017 (d15)
27. [V] Antoniades et al. (2025) SWE-Search. https://arxiv.org/abs/2410.20285 (d16). Compute-matched table garbled, not used.
28. [M] Arumugam and Griffiths (2025) Toward efficient exploration by LLM agents. https://arxiv.org/abs/2504.20997 (c25; search summary only)
29. [M] Third-party descriptions of AlphaEvolve, FunSearch, OpenEvolve program databases. https://arxiv.org/abs/2511.23473 (c26; secondary description only)
30. [M] Absence check for Go-Explore on code or reasoning chains (c27): two web searches, https://arxiv.org. Absence in the tools used is not proof.

Caveats on the source list: the critic re-opened the full text of items 1, 2, 10, 11, 6, 12. Items 14-17 were opened by the evidence agent and taken on trust. Search quota ran out during the gap pass, so the sweep of recent LLM archive work is not complete.
