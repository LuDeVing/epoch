# Resolution and saturation: deep document

*Subfield C06.01. Source files in this folder: evidence_a-d.jsonl (ids a01-a26, b01-b25, c01-c25, d01-d15), claims.jsonl (K01-K28), critique.md. All numbers below are from those files; the cross-check corrections in critique.md are applied. Time limits differ between papers, so solved counts from different papers are never comparable.*

## 1. What it is

Resolution is one inference rule for clause logic. Take two clauses that hold a complementary pair of literals. Unify the pair with a most general unifier. Merge what is left into a new clause. Robinson (1965) made this the single rule of a machine-oriented first-order logic. It replaced the Davis-Putnam (1960) approach of enumerating ground instances (a01, secondhand). [M]

The calculus is sound. It is refutation complete: a clause set is unsatisfiable if and only if the empty clause can be derived. With factoring added, a worked Wikipedia example reaches the empty clause in 7 steps. Without factoring it never gets there (a02). To prove a goal you negate it, add it to the axioms, and look for the empty clause.

Saturation is the way provers run this rule. The prover keeps a growing set of clauses. It picks an inference, applies it, adds the result, and repeats. It must be fair: every possible inference must eventually be considered, or completeness is lost. A run ends in one of three ways (a08, K01):
1. The empty clause appears. The goal is proved.
2. The set is saturated: no new non-redundant clause can be made. The clause set is satisfiable. The goal is not provable.
3. The run goes on forever, or hits a time limit.

The given-clause loop is the standard implementation. Clauses sit in two sets: active (already used for inference) and passive (waiting). Each round the prover picks one passive clause, the "given" clause. It infers with all active clauses, adds the new clauses to passive, and moves the given clause to active. The one decision that matters most is which passive clause to pick next. That is the clause selection problem. It is the part of this subfield that maps to our agent: choose the next thing to expand, from a growing pool, with a fixed budget.

Main systems (a04, a06, a07, a03):
- Otter (McCune, Argonne). First widely used high-performance prover. Resolution, paramodulation, hyperresolution, set of support, given-clause loop, term indexing. About 28,000 lines of C. Last change 14 Sep 2004. Successor: Prover9.
- E (Schulz). Equational superposition prover. Shared term rewriting, literal selection, ML-based search guidance. Part of Isabelle Sledgehammer. Won CASC CNF/MIX in 2000 and CNF in 2011.
- Vampire (Voronkov, Riazanov, Hoder, Kovacs, Reger, Suda). Ordered binary resolution and superposition, splitting, subsumption, KBO ordering. At least 53 CASC trophies since 1999. First version 1993. Vampire 2.6 had about 152,000 SLOC and 27 CASC wins (a08).
- SPASS and Prover9 are named in a02 but no numbers were gathered for them.

Superposition (Bachmair and Ganzinger 1994) joins resolution with ordered Knuth-Bendix completion for equality. E, SPASS, Vampire and Waldmeister use it (a03). The primary paper was not opened.

Scope note. This folder covers (1) the given-clause algorithm and clause selection, (2) learned clause guidance 2017-2026, and (3) LLM pipelines that call a resolution prover (Logic-LM, LINC). It has no study that uses saturation as a thinking schema for an LLM agent. See section 6 and section 10.

## 2. History and theories in depth

**1960-1965. From enumeration to unification.** Davis-Putnam needed all ground instances of the clauses. Robinson's most general unifier did the instantiation on demand. The lesson for an agent: a good representation removes blind enumeration (a01).

**1980s-1990s. Otter and the limits of the pure calculus.** Haken (1985) showed that pigeonhole formulas need exponential-size resolution refutations. This is recalled from memory, not opened (b13). McCune's EQP, an equational prover and not general Otter, proved the Robbins conjecture in 1996-97 after about 8 days of running; people had failed by hand since the 1930s. Dahn simplified the proof in 1998. The Wikipedia page is inconsistent on 1996 vs 1997 (a05, b14). Neither result is used for design decisions here (K18).

**The Otter loop and the Discount loop (a10).** In the Otter loop, passive clauses are also used to simplify others. Kept clauses pile up and processing slows. The Discount-style loop simplifies only against active clauses. Vampire's default is the limited resource strategy (LRS). It measures the time per given clause and estimates which passive clauses cannot be reached before the time limit. It drops them. LRS is incomplete by design and works only with a time limit. The authors call dropped clauses "unreachable", not "redundant". When any such clause is dropped, Vampire can no longer answer "satisfiable".

**Age and weight queues (a09).** The default selection mixes two priority queues. One serves the oldest clause. The other serves the lightest clause, where weight is the symbol count. With ratio (a, w), of each a+w picks, a come by age and w by weight. Example: 2:3 means 2 of 5 picks by age, 3 by weight. Age gives fairness (every clause is eventually picked). Weight is the greedy hedge toward small, general clauses. The ratio is hand-set; no learning.

**Layered clause selection, 2020 (a11, c12).** Gleiss and Suda group clauses by a cheap numeric feature (theory content, closeness to the goal, AVATAR split dependencies, closeness to Horn). The prover alternates between the groups, with age-weight inside each group. No learning. On TPTP, base about 9,108 solved (a rerun gives 9,204). Four single-feature layered strategies solve about 9,160 to 9,526. The union of the four reaches 10,297, which is +1,189 over base. On SMT-LIB, the base is about 39,943 to 41,841 and the union gains about 3,226. One feature (av) did worse than base on SMT-LIB. Tuning the split ratio gains +103 (TPTP, ratio 6:1) and +78 (SMT-LIB, ratio 1:1). Run-to-run variation is real (the default gave 9,512 and 9,525). The union gain is far larger than the best single feature.

**2017. Learned guidance arrives.** Two papers appeared within weeks.
- ENIGMA (Jakubuv and Urban, a14, a15, b01, c01, c02). A linear classifier (LIBLINEAR, hashed symbol features) learns from past E proofs which clauses were in a proof. E mixes its score into the weight function. Scoring costs about 10 microseconds per clause, close to the rate at which E makes clauses.
- Deep Network Guided Proof Search (Loos, Irving, Szegedy, Kaliszyk, a12, a13, b02, c03, c04). CNN and WaveNet models rank clauses in E on Mizar. Pure net guidance was too slow. A hybrid and then a two-phase switch fixed it.

**2019-2022. Trees, graphs, loops.** ENIGMA-NG (a17, b03, c05) added boosted trees and recursive nets. Hammering Mizar (a16, c06) looped prove-learn-prove on the whole Mizar library. ENIGMA Anonymous (a18, b05, c08) made scoring independent of symbol names with graph networks. Learning Theorem Proving Components (a19, c10) scored clauses in the context of clause-graph clusters. TRAIL (a21, b06, c07) tried reinforcement learning from scratch. Piepenbrock et al. (a24, b07, c11) proposed ground instances with a GNN and checked them with a SAT solver.

**2021. Suda: learn from history, mix with the stock rule (a20, b04, c09, b20).** Recursive net over derivation history. Net-only was weak. The mix with the stock rule won.

**2026. Teaching Vampire New Tricks (Chvalovsky, Suda, Urban, a22, a23, c13-c15).** Neural clause selection inside Vampire, tested on four datasets and in portfolios. Preprint, 14 Sep 2026, v1, not peer reviewed (critique correction 5).

**2023-2025. LLMs meet resolution provers.** Logic-LM (a25), LINC (a26), SATLM (b12, c21), LoGiPT (b11, c22), GFaiR (d02), CLOVER (d07), ProverQA (d03), LLM-First Search (d05), Dynamic Cheatsheet (d10), Overthinking (d11). In every one the prover is a back end. No LLM selects clauses (K28).

**Competing views.**
- Hand heuristics vs learning. A hand-tuned E still beats RL from scratch (TRAIL). Supervised, looped learning from the prover's own proofs (ENIGMA) beats hand portfolios. Difference: seed proofs (K10, K07).
- Neural vs tree scorers. Nets have better held-out recall. Trees solve more in real time because they are cheap (K06).
- Replacement vs mixing. Every success mixes learned and default queues (b15, K04).

## 3. Core findings with exact numbers

Status: E = established (two or more independent sources), S = single source, C = contested or mixed. Prover rows use the prover's own time limit; do not compare across rows.

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Resolution is sound and refutation complete; saturation must be fair; 3 outcomes | 7-step example with factoring; never ends without it | a02, a08, b08 | E |
| Default selection is an age:weight queue mix | ratio 2:3 = 2 of 5 picks by age | a09 | S |
| Layered selection: union of cheap-feature strategies | TPTP base 9,108 (rerun 9,204); singles 9,160-9,526; union 10,297 (+1,189). SMT-LIB union +3,226 | a11, c12 | S |
| Net-only clause selection fails; mix wins | Suda: net-only 25% of baseline (pure variants 55 and 190 solved vs 756 stock); layered mix 1,032 (136%) at 1:1, 1,036 (137%) at 1:2 | a20, b04, c09, b15 | E |
| Suda baseline, do not mix runs | rerun 756, first run 734; 137% is relative to 734; gains 411 or 430 depending on table | a20, b04, critique | E |
| Unswitched network guidance proves fewer hard theorems | without premise selection: unguided 145 vs guided 137; with: 458 vs 383 | a12, c04, b02 | E |
| Two-phase switch helps | 25,361 hard theorems: 7.36% (1,866) new proofs vs 2.33% unguided in the same table; coverage 56% to 59% | a12, b02, c03 | E |
| Guided search wins per clause; holdout within 1,000 processed clauses | Auto 89.0%, WaveNet 640 91.4%, WaveNet 256 92.3%; at 10,000: 94.3% vs 95.5-95.7%. Different test set from the row above | a12, critique | E |
| Net phase processes few clauses | about 1% of the clauses of a fast heuristic search | a13 | S |
| ENIGMA on AIM | CASC 2016, 200 problems, 180 s: S0 22; best mixed 41; all strategies 52; Vampire 47 (3x180 s); after boosting positives 57 | a14, c01, c02 | S (one family) |
| Boosting rare positives | positives repeated 10x: positive accuracy 12.5% to 81.8%; overall 98% to 93%; 5 more solved | c02, b18 | E |
| Scorer speed | about 10 microseconds per clause; trained in about 7 s on 6,821 positive vs 219,012 negative clauses | a15 | S |
| Looped learning on Mizar | 10 s: 14,933 to 25,397 (+70.0%); 60 s: 26,107 vs old 6-strategy portfolio 22,068 (+18.3%); Vampire CASC portfolio at 300 s 27,842 | a16, c06 | E |
| Trees beat nets in real time | MPTP2078 (2,078 problems, 10 s): baseline 1,086; best tree mix 1,256 (+15.7%); neural 1,197. Speed vs E: linear about 60%, trees about 40%, neural 6-7% | a17, b03, c05, b16 | E |
| Same pattern on Mizar40 | 10 s: baseline 14,966; LightGBM D2 24,347 (+62.7%); GNN N2 23,262 (+55.4%); at 5,000 generated clauses D2 22,661 vs N2 22,169; GNN training 1 d 8 h vs 40 min | a18, b05, c08 | E |
| Generalisation drop | on 232 newly solved problems true-positive rate falls about 15%, true-negative about 20% | a17, c05 | S |
| Learned guidance is dataset-specific | default to boosted, 32 billion instruction limit (about 12 s): TPTP 8,511 to 10,864 (+27.6%); Mizar40 1,543 to 3,101 (+101.0%); Isabelle 2,178 to 2,715 (+24.7%); CoqHammer 399 to 772 (+93.5%). A model trained on one set scores below default on others; combined model reaches 100.0/99.4/101.4/95.3% of dedicated ones | a22, c13-c15 | E (preprint) |
| Portfolios shrink the gain | per-strategy boost 24.0%; 5-strategy portfolio +13.9%; one model for all +23.8%; champion gain 15.7% unboosted vs 8.4% boosted | a23 | S |
| RL from scratch loses to hand-tuned E | solved M2k/MPTP2078: E 1922/998; TRAIL 1561/910; Beagle 1543/742; plCop 1359/782; rlCop 1235/733; mlCop 1034/502. Transfer loss 11% and 3% | a21, b06, c07 | E |
| Processed-clause context | MPTP2078: 910 with vs 854 without (+56, 6%); M2k 1,561 both | b19 | S |
| Confidence threshold plateau | -0.5: 1063 (140%); -0.25: 1066 (141%); 0.00: 1036 (137%); 0.25: 945 (125%); 0.5: 825 (109%) | b20 | S |
| Premise selection + clause guidance complement | union 1,712 (6.8%) vs neural 1,665 (6.6%); non-switched variants included 1,866 (7.36%) | b17 | S |
| Component context | k-means k=2 67 newly solved, k=3 78, soft k=2 63 (of about 32k unsolved) | c10 | S |
| ML proposes ground instances, solver checks | 10.59% vs 3.3% test; 10,543 in 42 rounds vs 9,923 in 100 random runs; 6.0 instances per solved problem, 3.9 with a skolem symbol | a24, b07, c11 | E |
| Prover back end, GPT-4 (standard / CoT / Logic-LM) | ProofWriter 52.67 / 68.11 / 79.66; FOLIO 69.11 / 70.58 / 78.92; PrOntoQA 77.40 / 98.79 / 83.20; LogicalDeduction 71.33 / 75.25 / 87.63; AR-LSAT 33.33 / 35.06 / 43.04 | a25, b10, c19 | E |
| Logic-LM gain, GPT-3.5 averages (not GPT-4) | +39.2% over standard, +18.4% over CoT. GPT-4: +24.98 over standard, +10.44 over CoT | a25, critique | E |
| LINC | FOLIO StarCoder+ 56.0 vs CoT 41.8; GPT-3.5 62.6 vs 54.9; GPT-4 72.5 vs 75.3 (McNemar p=0.58, so no difference). ProofWriter balanced: GPT-3.5 96.4, GPT-4 98.3 | a26, b09, c17 | E |
| Solver advantage grows with depth | ProofWriter: +7.1, +5.0, +12.7, +20.0, +39.4 points at depth 0, 1, 2, 4, 5 | b22 | S |
| Executability is the bottleneck | self-refinement: FOLIO GPT-3.5 66.7% to 84.3%, GPT-4 79.9% to 85.8%; AR-LSAT GPT-4 32.6% to 39.8%; mean +5.01 points | b23, c20 | S |
| Syntax errors by model | StarCoder+ 38%, GPT-3.5 24%, GPT-4 13% | c17, d01 | E |
| GPT-4o translation loss | AR-LSAT Logic-LM: execution rate 33.8%, accuracy when executable 51.3%, program accuracy 17.3%; CLOVER 59.7 / 78.3 / 46.8 | d07, d08 | S |
| Solver verdict can hide wrong meaning | GPT-4 FOLIO: LINC predicts 24% True / 17% False / 57% Uncertain; CoT 32 / 27 / 41 | d01 | S |
| Fine-tuned small translator | FOLIO logical correctness: GPT-4 LINC 4-shot 45.82; Phi-3.5 Mini SFT+KTO 61.52; syntax errors down 83.33% vs Logic-LM, 61.11% vs LINC | d09 | S |
| Fine-tune to emulate solver | LoGiPT: best is +9.84 points over Logic-LM GPT-4 on ProofWriter (79.66); Vicuna-13B 81.17 / 96.40 (ProofWriter / PrOntoQA); merged training about 79 | b11, c22, b24 | S |
| SAT/SMT back end (SATLM) | code-davinci-002 greedy: LSAT 35.0 vs CoT 23.5; ProofWriter 99.7 vs 80.1; with self-consistency LSAT 37.4 vs prior 30.9; +23% over PAL on hard GSM | b12, c21 | S |
| Long proofs break CoT | ProverQA hard: GPT-4o CoT 50.00, Claude-3.5 56.40, Mistral-Large 52.20; GPT-4o standard 46.20 (CoT gain +3.8 hard vs +7.0 easy) | d03 | S |
| Distractors and order cost accuracy | GPT-4o CoT hard 50.00; no distractors 57.40; also ordered 62.40. Medium 79.40 / 82.20 / 87.40. Easy 94.20 / 94.40 / 95.60 | d04 | S |
| Refutation reasoner holds at depth | RuleTaker depth 5 entailment/full: GFaiR 94.2 / 91.9; FaiRR 78.7 / 67.8; NLProofs 69.6 / 57.3; depth 3: 99.5 / 99.5 vs 98.4 / 96.0 | d02 | S |
| Iterative one-step proof generation | RuleTaker D5 proof accuracy ProofWriter 96.2% vs PRover 87.1%; depth 5 86.4% vs 65.1% | c16 | S |
| Greedy best-first collapses | Countdown diff 7, GPT-4o: BestFS 11.11, MCTS 32.63, LFS 47.37; o3-mini: 13.33, 41.05, 78.95. Diff 5: 49.47, 60.00, 63.16. Sudoku 4x4: 41.05, 100, 96.84 | d05, d06 | S |
| Efficiency profile | AUP win rate GPT-4o: BestFS 5.98, MCTS 7.09, LFS 8.99; efficiency 2.67 / 3.68 / 4.70 | d06 | S |
| Reuse of solved items | Claude 3.5 AIME 2024 23% to 50%; GPT-4o Game of 24 10% to 99%; GPQA-Diamond +9%; small models gain little | d10 | S |
| Redundant solution rounds | QwQ-32B 13 solutions for 2+3; 2-4 rounds in 76-80% of cases; removing repeats cut tokens 48.6% on MATH500 with accuracy kept | d11 | S |
| No LLM clause selector | 0 papers among about 20 titles scanned; searches limited by rate limits | d13, d14, c25 | open |

## 4. Mechanisms and models

### 4.1 The given-clause loop (implementable)

```
passive = initial clauses (axioms + negated goal)
active  = {}
loop:
  if empty clause in passive or active: return PROVED
  if passive is empty: return SATURATED (satisfiable; sound only if nothing was discarded incompletely)
  if budget out: return BUDGET
  given = select(passive)            # the control decision
  remove given from passive
  simplify given against active; if redundant (tautology, subsumed): drop, continue
  new = all inferences of given with active (and itself)
  simplify new; delete tautologies and subsumed clauses
  active += given
  passive += new
```

Redundancy rules (a03, a06): tautology deletion, subsumption (a clause is dropped if a more general one exists), demodulation by ordered rewriting. Otter vs Discount differ in whether passive clauses are used to simplify (a10).

### 4.2 Fairness and the age:weight mix (a09)

Keep two priority queues over the same passive set: by arrival time and by clause weight (symbol count). Pick counter n. In each window of a+w picks, serve a from the age queue and w from the weight queue. The age pick guarantees every clause is eventually taken. Drop the age queue and a light clause stream can starve an old, heavy, necessary clause. Starvation was not measured in the sources (gap 7). The LLM analogue is the failure in d05: greedy best-first expands the top-scored node and never returns to older options.

### 4.3 Layered selection (a11)

Define K cheap features f_1..f_K (each an integer or a bucket). Make a queue per feature value. Alternate among feature queues by a ratio, and use age-weight inside each queue. Run several such strategies and take the union. In the data the union gained far more than the best single strategy (+1,189 vs +417 best single, TPTP).

### 4.4 Learned scoring mixed into the queues (a14, a20, b15)

1. Run the prover on training problems. Mark each clause "in the final proof" (positive) or not (negative).
2. Train a classifier on clause features. Positives are rare (about 1 in 32), so repeat positives 10x (c02).
3. Add a third queue ordered by the classifier score, with a hand-set frequency (best AIM setting: frequency 30, eps 0.2). Keep the stock queues.
4. Run, collect new proofs, retrain, repeat (the ENIGMA loop). Gains: 22 to 41 (AIM), 14,933 to 25,397 (Mizar, 10 s).
5. Hold out test problems. Train-set accuracy overstates test quality (a17: TPR down 15%, TNR down 20% on newly solved problems).

Net-only queue: 25% of baseline (Suda). Layered 1:1 or 1:2 mix: 136-137%.

### 4.5 Cost accounting (a12, a13, a17, a18)

Evaluation cost per clause sets the winner. Neural scoring ran at 6-7% of E's clause rate, trees at about 40%, linear at about 60%. At equal generated-clause budget the GNN is close to the trees (22,169 vs 22,661); at equal wall time it is not. Fix used by Loos et al.: spend the slow scorer on a first phase (20 min), then switch to the fast heuristic (10 min).

### 4.6 Confidence gate (b20)

The learned score is used only if above a threshold. Thresholds -0.5 to 0 gave 1063, 1066, 1036 solved. At 0.25 it fell to 945 and at 0.5 to 825. Flat zone, then drop.

### 4.7 Propose and verify (a24, c11)

The learned model proposes ground instances. An exact solver (SAT plus congruence) checks them. A wrong proposal costs only a failed check. Learned: 10,543 solved in 42 rounds vs random 9,923 in 100 runs.

### 4.8 Offload to a prover (a25, a26)

Pipeline: LLM translates text to FOL; Prover9 (CNF plus resolution) decides; if translation does not run, fall back to CoT; optionally refine from the solver's error text; LINC samples 10 parses and votes over the prover outputs. Three failure modes (d01): L1 missing implicit information, L2 explicit information mis-encoded, L3 syntax errors (most common: one symbol with different arities).

### 4.9 Refutation mode (d02, K25)

Negate the hypothesis, add it, resolve toward a contradiction. This is complete where forward and backward chaining are not. In a trained XLNet/T5 system it held 94.2% at depth 5 where forward chaining fell to 78.7%.

## 5. What holds up

**Held under replication or across several independent papers.**
- Mixing learned and default queues beats replacing them. Five papers, no counterexample (b15, K04).
- Cheap scorers beat heavy ones at equal wall time. Two separate papers: ENIGMA-NG (1256 vs 1197) and ENIGMA Anonymous (24,347 vs 23,262), though the GNN had higher recall (TPR 90-92% vs about 80%). The gap narrows at equal clause budget, so the loss is mostly evaluation cost (b16).
- Looped learning from the prover's own proofs scales (ENIGMA, Hammering Mizar, Suda). Gains shrink at longer time limits and against portfolios (+70% at 10 s; +18.3% at 60 s vs a hand portfolio; Vampire portfolio at 300 s still ahead).
- Machine-proposed instances beat random ones (10.59% vs 3.3%; 10,543 vs 9,923).
- Prover offload helps where CoT is weak and when the model is small. LINC and Logic-LM agree on direction.

**Failures and losses.**
- Unswitched network guidance proved fewer hard theorems than unguided E (137 vs 145; 383 vs 458). More accurate WaveNets (79.9-81.5% clause accuracy) guided worse (a12).
- TRAIL RL from scratch lost to hand-tuned E on both sets. It reports the best iteration, which is a selection effect (a21).
- Cross-dataset transfer fails: a model trained on one set scored below default on the others. The TPTP model beat default on Mizar40 only because TPTP holds 1,840 Mizar problems (a22).
- GPT-4 PrOntoQA: CoT 98.79 vs Logic-LM 83.20. The solver route lost 15.59 points (a25).
- GPT-4 FOLIO LINC 72.5 vs CoT 75.3: slightly worse, not significant (p=0.58) (a26).
- Merged training (ProofWriter plus PrOntoQA) lowered LoGiPT accuracy a few points (b24).
- SMT-LIB layered feature av did worse than base (a11).

**Moderators.**
- Model strength. Small models gain from the solver (StarCoder+ FOLIO 56.0 vs 41.8). Strong models gain little or lose (GPT-4 FOLIO; PrOntoQA). Net gain depends on the base model and task depth.
- Proof depth. Solver advantage over CoT: +7.1 at depth 0, +39.4 at depth 5 (ProofWriter). CoT of GPT-3.5 sits at chance above depth 1. ProverQA hard: CoT stays near 50% for GPT-4o and Claude-3.5.
- Translation difficulty. Execution rate 33.8% on AR-LSAT vs near 100% on easy sets. Accuracy falls with formula complexity (CLOVER Fig. 1a).
- Time limit. Boost shrinks at longer limits and against portfolios (24.0% to 13.9%).
- Seed proofs. Loops need successful first proofs. RL from scratch has none; Dynamic Cheatsheet shows the same for small LLMs.
- Dataset similarity. Train and test come from the same library in most prover papers.

**Interventions that worked.**
- Repeat rare positives 10x (positive accuracy 12.5% to 81.8%).
- Two-phase schedule: slow scorer first, fast heuristic second.
- Layered mix 1:1 or 1:2 with the stock rule.
- Self-refinement from solver error text (+5.01 points executability on average, mostly syntax).
- Independent equivalence check of translation (CLOVER: AR-LSAT program accuracy 17.3 to 46.8, GPT-4o).
- Remove whole redundant solution rounds (48.6% fewer tokens, accuracy kept).

**Interventions that did not.**
- Writing the FOL but letting the model give the answer without calling the prover (c18). The prover call is what helps.
- Self-refinement beyond round 1 (accuracy stalls, c20).
- Solver error text for meaning errors: it catches syntax, not logically consistent mistranslation (d08).

**Source quality caveats (from critique).** Robinson 1965, Haken 1985 and McCune 1997 were not opened. Wikipedia was the only source for history and CASC counts. a19, a24, b07, c10, c11 were read from abstract and intro or secondary tables. LoGiPT, SATLM and Gleiss-Suda numbers were not re-opened by the cross-checker. Several tables came from two-column PDF text with inferred row alignment (CLOVER, GFaiR, Gleiss-Suda). Chvalovsky 2026 is a preprint.

## 6. Language models

**What exists.** All LLM work found uses a resolution prover as a back end, or borrows search ideas. No study puts an LLM in the clause-selection loop of E or Vampire, and none gives an LLM agent age and weight step queues (K28, d13, d14). The searches were limited by rate limits, so this is absence of evidence. Papers after mid-2025 may exist.

**Offload to Prover9 (translate, then decide).**
- Logic-LM, GPT-4: ProofWriter 68.11 (CoT) to 79.66 (+11.55); FOLIO 70.58 to 78.92 (+8.34); LogicalDeduction 75.25 to 87.63 (+12.38); AR-LSAT 35.06 to 43.04 (+7.98); PrOntoQA 98.79 to 83.20 (-15.59). Average over CoT +10.44 for GPT-4 (critique correction 1).
- LINC: StarCoder+ (15.5B) beats GPT-3.5 CoT by 38 points and GPT-4 CoT by 10 points on ProofWriter. FOLIO: 56.0 vs 41.8 (StarCoder+), 62.6 vs 54.9 (GPT-3.5), 72.5 vs 75.3 (GPT-4, not significant).
- GPT-4 LINC errors differ from CoT errors: misprediction similarity 0.14-0.22 vs 0.52-0.56 among in-context methods. This points to complementary failures (d01). The shift is to false "Uncertain": 57% vs 41% for CoT on FOLIO.
- GPT-4o, AR-LSAT, Logic-LM: only 33.8% of problems run; 51.3% accuracy on those; program accuracy 17.3. CLOVER lifts these to 59.7 / 78.3 / 46.8. On FOLIO Logic-LM execution accuracy is 94.2 vs CLOVER 92.7, so CLOVER gives nothing on easy sets (d07).

**What changed the result.**
- Model strength: syntax errors 38% -> 24% -> 13% (StarCoder+, GPT-3.5, GPT-4).
- A refinement round: executability +5.01 points on average.
- A verified, compositional translation: execution accuracy 51.3 -> 78.3 on AR-LSAT (GPT-4o).
- Fine-tuning a small translator: FOLIO logical correctness 61.52 (Phi-3.5 Mini SFT+KTO) vs 45.82 (GPT-4 LINC 4-shot). Their own manual annotation, small counts (d09).
- Fine-tuning to imitate solver traces: +9.84 on ProofWriter over Logic-LM GPT-4 (b11).

**Long proofs without a solver.**
- ProverQA hard: CoT near 50% for GPT-4o, Claude-3.5, Mistral-Large. Removing distractors +7.4, plus proof order +12.4 for GPT-4o. This 12-point gap is an upper bound on what better relevance and ordering can win for CoT agents; the order in d04 was set from the known proof, which a real agent does not have.
- Refutation-based training (GFaiR) holds 94.2% at depth 5 against 78.7% for forward chaining, with trained modules, not prompted LLMs (d02).

**Search policy.** LLM-First Search on Countdown difficulty 7, GPT-4o: greedy best-first 11.11%, MCTS 32.63%, self-guided 47.37%. o3-mini: 13.33 / 41.05 / 78.95. Greedy best-first with no fairness mechanism collapses on deep problems. On easier items the gap shrinks (diff 5: 49.47 vs 63.16). On 4x4 Sudoku MCTS reached 100 with C=0.5, and MCTS result depends on its constant (C=1.0 gave 2.22). This is indirect support for an age queue (K02, K24). It does not test an age:weight mix.

**Reuse.** Dynamic Cheatsheet: Claude 3.5 Sonnet on AIME 2024 23% to 50%; GPT-4o on Game of 24 about 10% to 99% once it stored a Python solution. Small models gain little. Same pattern as ENIGMA: reuse needs good seeds (d10, K27). Single group, no replication seen.

**Redundancy.** QwQ-32B uses 1,953% more tokens than conventional models on trivial arithmetic and produces 13 solutions for 2+3. Cutting repeats saves 48.6% of tokens with accuracy kept (MATH500). This is whole-solution dedupe, not step-level subsumption (d11).

**What we cannot say.** All LLM numbers come from GPT-3.5, GPT-4, GPT-4o, Claude-3.5, o3-mini, QwQ-32B or small open models. None are 2026 frontier models. The 2026 Vampire paper uses small neural nets, not LLMs.

## 7. What our agent should take

Schema parts: G = guardrail, S = state, O = operator, memory = section 5. Status: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Three-way stop outcome.** Report proved (a check passed), closed (all options exhausted, nothing left to expand), or budget out. Never merge "closed" and "timeout" into one failure. Part: S8 / S6 stop and G6. [E] K01. Evidence a02, a08, b08. Cost: near zero; a label.
2. **Keep a hand-built fallback when a learned or model-based scorer is used.** Do not let a learned step scorer replace the default order. Mix it in. Part: G7 / O. [E] K04. Evidence a20, b04, b15, c09.
3. **Charge the cost of every scorer and judge to the budget; cheap beats clever at equal tokens.** Count scoring tokens in the budget. Part: G7, G12. [E] K05, K06. Evidence a12, c04, a17, a18, b16. This agrees with the existing G7.
4. **Check a formal translation before trusting a solver verdict.** If the agent translates text to code or logic and a tool decides, test the translation on its own: does it run, and does it say what the text says. Part: G3 / S8. [E] K21. Evidence d01, d07, d09, c17. The check should be separate from the solver.
5. **Treat learned memory as dataset-specific.** Retrieved lessons from class A should not be applied to class B without a test. Part: memory (extends the rule "trusted after helping on two different problems"). [E] K08. Evidence a22, a21, b06.
6. **Seed-gate the memory loop.** A looped store of past traces is only worth it when seed traces are good. Part: memory / S9. [E] on the prover side (K07), [S] on the LLM side (d10). Evidence a14, a16, b18, c06, d10. Weight rare successes more than average ones (K20, c02).
7. **Solver offload is not free for strong models.** Do not add a Prover9-style path to the default route. Treat it as a routed option. Part: S0 gate / O. [E] K12, K13. Evidence a25, b10, a26, b09.

### Test first

| # | Candidate | Part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | Two-queue step selection: every k-th pick takes the oldest open candidate, the rest take the highest-ranked | O (select next step), S6 | [S] | K02, K24; a09, d05, d06 |
| T2 | Layered selection: rotate several cheap ranking rules, take the union | O / memory | [S] | K03; a11, c12 |
| T3 | Refutation mode: assume the goal false, look for a contradiction, as an alternative to forward-only reasoning | O5 variant (work backwards) | [S] | K25; d02, a02 |
| T4 | Depth routing: solver path only above a depth threshold | S0 gate | [S] | K14; b22, a25 (PrOntoQA loss) |
| T5 | Relevance and order step before deep chains | O / S2 | [S] single study | K23; d03, d04 |
| T6 | Duplicate-step check, step level | G11 / O | [S] | K26; d11 |
| T7 | Confidence gate with a flat zone, sweep the threshold | G, S6 | [S] | K19; b20 |
| T8 | Propose then verify with an exact checker | O | [E] on the prover side; LLM side [S] | K11; a24, b07, c11 |
| T9 | One repair round from verifier error text vs resample | S5 | [S] | K15; c20, d08 |
| T10 | Portfolio check: does a learned scorer help less when many diverse samples are already used | G4 / G12 | [S] | K09; a23 |
| T11 | Memory transfer across task families | memory | [E] on prover side | K08, K27; a22, d10 |
| T12 | Independent meaning check after a solver answer | G3 / S8 | [S] | K22; d01, d08, d07 |

Guardrail check. G9 (no debate), G4 (no persona voters) and G10 (reasoning text is not evidence) still apply. The LINC majority vote is over prover outputs of independent parses, so treat it as a hint, not proof (G4). Section 4b lists "unstructured self-reflection" as not to add; the repair step T9 uses real verifier output (G2).

## 8. Concrete tests on our bench

All arms get the same total token budget, counting scorer, judge and setup tokens (G7). Report solved per item and solved per 1,000 tokens (copy the efficiency design of d06). Use at least 3 seeds. Prover-side numbers are a guide only; expect smaller effects.

| Test | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| E1 age:weight step queue | multi-step tasks with a branching pool: Countdown-style depth ladder (diff 5 to 7), ProverQA-style hard FOL, ARC-style program search | A: best-first by model score. B: 1:k mix with oldest-open (k in 1, 2, 5). C: plain CoT | win rate by depth; win rate per token; step starvation count (oldest open item never expanded) | B above A at depth 7 (A = 11-13% in d05); gain near zero at depth 5 or lower |
| E2 layered rotation | same items | A: best single ranking rule. B: rotate 3-4 cheap rules (shortest, closest to goal, most reused fact, model score), union of outputs | solved by union vs best single | union beats best single by a margin like a11 (+1,189 vs +417 on 9,108, about +13% vs +4.6%); smaller on small pools |
| E3 refutation mode | RuleTaker / ProofWriter depth 3 and 5, ProverQA | A: forward only. B: assume goal false and derive a contradiction. C: both, code picks by a check | accuracy at depth 5 | B or C near +10 to 15 points at depth 5 if the d02 pattern holds for prompted LLMs; none at depth 3 |
| E4 solver routing | FOLIO, ProofWriter, PrOntoQA, AR-LSAT, plus our own deduction items | A: CoT. B: always translate and call a solver. C: route by depth or a probe | accuracy; share of items that translate; accuracy when translated | C at least equal to the better of A and B; B loses on PrOntoQA-like easy items |
| E5 translation audit | same | solver verdict alone vs verdict plus back-translation check | wrong-but-accepted rate | check cuts accepted wrong answers; compare 57% false Uncertain (d01) |
| E6 relevance and order | ProverQA hard, bench items with distractors | A: raw premises. B: code or model filter then order | accuracy | up to +7 (filter) to +12 (filter and order, but order was oracle in d04), so expect less |
| E7 step dedupe | long traces | A: none. B: drop a repeat step or round | tokens at equal accuracy | tokens down, accuracy flat; smaller on hard items |
| E8 confidence gate sweep | any step scorer | thresholds at 5 levels | solved | plateau then drop (b20) |
| E9 memory loop | classes A and B | none; memory from A tested on A; memory from A tested on B; memory from A+B | accuracy per episode; trace count curve | in-class gain, cross-class loss as in a22; small models gain little |
| E10 portfolio | many samples | N samples with/without scorer | gain over N=1 vs gain over N=5 | gain shrinks, as 24.0% to 13.9% (a23) |

## 9. What does not transfer, and why

- **Completeness proofs.** Refutation completeness holds for clause logic with a fair strategy. An LLM step is not an inference rule: it can be wrong, so soundness fails first. The 3-way outcome is useful as a label; "saturated means unprovable" is not valid for an agent.
- **Clause weight (symbol count).** Smaller clauses are more general in logic. A shorter reasoning step is not more general. The weight queue needs an LLM analogue that is not tested.
- **Subsumption and demodulation.** These are exact tests on syntactic structure. Step-level duplicates in natural language have no exact test. Only whole-solution dedupe has data (d11).
- **Learned scorers trained on millions of proofs.** ENIGMA used 63M training examples and Mizar-scale data. We do not train. Only the structure (mix, cost, seeds) transfers.
- **Absolute numbers.** Time limits differ (10 s, 12 s, 30 s, 180 s, instruction counts). Mizar, TPTP, SMT-LIB are formal. Word problems are not.
- **Symbol-name features.** ENIGMA-NG and others depend on consistent symbol names within a library (a14, c05). Word-problem tasks vary.
- **Haken bounds.** Exponential proof size for pigeonhole is a statement about one calculus. No link to LLM benchmark difficulty was found, and the source was not opened (K18).
- **Equality and the Robbins result.** A special equational prover on one problem. It says nothing about general agents.
- **Learned guidance as a full replacement.** Failed in the source domain (25% of baseline). Do not carry it over.
- **GNN and tree scorers.** Their cost advantage came from microsecond scoring. An LLM scoring call costs tokens and seconds. This favours cheap rules over LLM rating of every candidate.
- **Strong-model solver offload.** Gains seen on GPT-3.5 and StarCoder+ do not carry to strong models on easy items (PrOntoQA, FOLIO GPT-4).

## 10. Open questions

1. Does an LLM agent with explicit "given" and "passive" queues (age plus weight) beat best-first or CoT at equal tokens? No study (gap 1).
2. What is the best age:weight ratio for LLM steps, and does the flat-then-drop pattern of the confidence threshold (b20) reappear with LLM confidence scores (gap 2)?
3. Which tasks gain from solver routing, and what cheap probe predicts it? PrOntoQA shows a loss (gap 3).
4. Translation vs solving on 2026 models. Only GPT-4o-era data exists (gap 4).
5. Does an LLM as clause selector inside E or Vampire beat ENIGMA-style trees at equal wall time? None found (gap 5).
6. Is there a measured benefit for step-level redundancy elimination (gap 6)?
7. How often do greedy queues starve old items, in provers and in LLM agents (gap 7)?
8. Does looped reuse of past solved traces saturate, and when (gap 8)? Dynamic Cheatsheet gave no curve.
9. Do proof-size limits matter for any LLM benchmark with proof depth above 5 (gap 9)?
10. Does cross-benchmark degradation (a22) appear for LLM memory of past traces (gap 10)?
11. Unread: Bostrom et al. 2022 (search over statement compositions with a learned scorer), the closest natural-language given-clause loop (d15).
12. The Chvalovsky 2026 preprint needs peer review or replication.
13. Robinson 1965, Haken 1985, McCune 1997 and Bachmair-Ganzinger 1994 were not opened.

## 11. Sources

[V] = opened and read (page or PDF text) in this study. [M] = snippet, abstract only, or memory.

- [M] Robinson (1965) A machine-oriented logic based on the resolution principle. J. ACM 12(1):23-41. Via https://en.wikipedia.org/wiki/Resolution_(logic) (a01)
- [V] Wikipedia: Resolution (logic). https://en.wikipedia.org/wiki/Resolution_(logic) (a02, b08)
- [V] Wikipedia: Superposition calculus. https://en.wikipedia.org/wiki/Superposition_calculus (a03)
- [V] Wikipedia: Otter (theorem prover). https://en.wikipedia.org/wiki/Otter_(theorem_prover) (a04)
- [V] Wikipedia: Robbins algebra. https://en.wikipedia.org/wiki/Robbins_algebra (a05)
- [V] Wikipedia: Vampire (theorem prover). https://en.wikipedia.org/wiki/Vampire_(theorem_prover) (a06)
- [V] Wikipedia: E (theorem prover). https://en.wikipedia.org/wiki/E_(theorem_prover) (a07)
- [V] Kovacs and Voronkov (2013) First-Order Theorem Proving and Vampire, CAV 2013. https://link.springer.com/content/pdf/10.1007/978-3-642-39799-8_1.pdf (a08, a09, a10)
- [V] Gleiss and Suda (2020) Layered Clause Selection for Saturation-Based Theorem Proving. https://ceur-ws.org/Vol-2752/paper3.pdf (a11, c12; table text garbled in part)
- [V] Loos, Irving, Szegedy, Kaliszyk (2017) Deep Network Guided Proof Search. https://arxiv.org/abs/1701.06972 (a12, a13, b02, c03, c04)
- [V] Jakubuv and Urban (2017) ENIGMA. https://arxiv.org/abs/1701.06532 (a14, a15, b01, b18, c01, c02)
- [V] Jakubuv and Urban (2019) Hammering Mizar by Learning Clause Guidance. https://arxiv.org/abs/1904.01677 (a16, c06)
- [V] Chvalovsky, Jakubuv, Suda, Urban (2019) ENIGMA-NG. https://arxiv.org/abs/1903.03182 (a17, b03, c05)
- [V] Jakubuv et al. (2020) ENIGMA Anonymous. https://arxiv.org/abs/2002.05406 (a18, b05, c08)
- [M] Chvalovsky, Jakubuv, Olsak, Urban (2021) Learning Theorem Proving Components. https://arxiv.org/abs/2107.10034 (a19, c10; abstract and intro, or secondary table)
- [V] Suda (2021) Improving ENIGMA-Style Clause Selection While Learning From History. https://arxiv.org/abs/2102.13564 (a20, b04, b20, c09)
- [V] Crouse et al. (2019/2021) TRAIL. https://arxiv.org/abs/1911.02065 (a21, b06, b19, c07)
- [V] Chvalovsky, Suda, Urban (2026) Teaching Vampire New Tricks (preprint). https://arxiv.org/abs/2609.16228 (a22, a23, c13-c15)
- [M] Piepenbrock, Urban, Korovin, Olsak, Heskes, Janota (2022) Machine Learning Meets The Herbrand Universe. https://arxiv.org/abs/2210.03590 (a24, b07, c11; abstract and intro)
- [V] Pan, Albalak, Wang, Wang (2023) Logic-LM. https://arxiv.org/abs/2305.12295 (a25, b10, c19, c20)
- [V] Olausson et al. (2023) LINC. https://arxiv.org/abs/2310.15164 (a26, b09, b21, c17, c18, d01)
- [M] Feng et al. (2023) Language Models can be Logical Solvers (LoGiPT). https://arxiv.org/abs/2311.06158 (b11, b24, c22; not re-opened by cross-check)
- [M] Ye, Chen, Dillig, Durrett (2023) SATLM. https://arxiv.org/abs/2305.09656 (b12, b25, c21; not re-opened by cross-check)
- [M] Haken (1985) The intractability of resolution. Recalled from memory (b13). No URL.
- [M] McCune (1997) solution of the Robbins problem (b14). Via https://en.wikipedia.org/wiki/Robbins_algebra
- [V] Tafjord, Dalvi Mishra, Clark (2021) ProofWriter. https://arxiv.org/abs/2012.13048 (c16)
- [M] Han et al. (2024) FOLIO. https://arxiv.org/abs/2209.00840 (c23; abstract page)
- [V] Qi et al. (2025) ProverQA via ProverGen. https://arxiv.org/abs/2502.06563 (d03, d04; c24 was abstract only)
- [V] Sun et al. (2024) GFaiR. https://arxiv.org/abs/2404.01677 (d02; row alignment inferred)
- [V] Herr, Rocktaeschel, Raileanu (2025) LLM-First Search. https://arxiv.org/abs/2506.05213 (d05, d06)
- [V] CLOVER (2025). https://arxiv.org/abs/2410.08047 (d07, d08; row alignment inferred)
- [V] LOGICPO (2025). https://arxiv.org/abs/2506.18383 (d09)
- [V] Suzgun et al. (2025) Dynamic Cheatsheet. https://arxiv.org/abs/2504.07952 (d10)
- [V] Chen et al. (2025) Do NOT Think That Much for 2+3=? https://arxiv.org/abs/2412.21187 (d11)
- [M] Bostrom et al. (2022) Natural Language Deduction through Search over Statement Compositions. https://arxiv.org/abs/2201.06028 (d15; fetched, not read)
- [M] Suda (2021) arXiv 2102.03529, seen in search results only (d13). https://arxiv.org/abs/2102.03529
- [M] Search records c25, d13, d14 (no URL; negative results).

## Source audit (2026-11-03)

Fresh auditors re-opened the sources of 6 established claims: 2 confirmed as written, 4 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **C06.01-K04** (now single-source: the sources are not independent). All four listed sources are the one Suda 2021 paper (the 'cross-reading' entry cites other papers but links the same arXiv id), so the general 'helps most when mixed, fails as full replacement' rests on a single study; its numbers (net-only 190 solved = 25% of 756; layered 1:1 1032 = 136%, 1:2 1036 = 137%) are correct.
- **C06.01-K06** (now single-source: the sources are not independent). ENIGMA-NG (2019) and ENIGMA Anonymous (2020) are by the same group (Jakubuv, Chvalovsky, Suda, Urban), so they count as one lab; all numbers check out (1256 vs 1197 on MPTP2078; 24,347 vs 23,262 on Mizar40 at 10 s; GNN had higher TPR).
- **C06.01-K08** (reworded: the sources support less). The Vampire study notes one exception (a TPTP-trained model still improves over default elsewhere), and the TRAIL authors read their 11%/3% transfer losses as evidence of relatively domain-general features, which does not support 'dataset-specific'; TRAIL is also a different system (Beagle RL, Mizar-derived sets only). Corrected claim: In a Vampire neural-guidance study, a model trained on one benchmark family usually scores below the unguided default on the others (with one exception, a TPTP-trained model), and a single model trained on all four sets nearly matches the dedicated models (95-101%); in TRAIL (a Beagle-based RL prover) transfer between two Mizar-derived sets lost only 11% and 3%.
- **C06.01-K21** (reworded: the sources support less). Numbers match, but 'translation is the main loss' is general while the evidence is mainly AR-LSAT; on FOLIO the same Logic-LM pipeline executes and scores 94.2% of executable cases, so translation loss is not shown to dominate everywhere. Corrected claim: On hard first-order tasks, translation to formal logic is a major loss in LLM-plus-solver pipelines: GPT-4o Logic-LM on AR-LSAT produced executable programs for only 33.8% of problems (51.3% accuracy on those), its translation accuracy falls as formula complexity rises, and LINC syntax errors fall with model strength (13% GPT-4, 24% GPT-3.5, 38% StarCoder+) while missing-information and mis-encoding errors remain; on easier sets like FOLIO the loss is small.
- **C06.01-K05** (now single-source: only one opened source, code check).
- **C06.01-K07** (now single-source: only one opened source, code check).
- **C06.01-K10** (now single-source: only one opened source, code check).
- **C06.01-K12** (now single-source: only one opened source, code check).
- **C06.01-K13** (now single-source: only one opened source, code check).
- **C06.01-K20** (now single-source: only one opened source, code check).
- **C06.01-K23** (now single-source: only one opened source, code check).
