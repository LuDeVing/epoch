# Anytime search and restarts: deep document

*Subfield C05.11. Written 2026-10-26 from evidence_a-d.jsonl, claims.jsonl and critique.md in this folder. Evidence ids (a01 ... d20) and claim ids (K01 ... K31, short for C05.11-Kxx) point into those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.*

Honest summary up front. The classic result (restarts rescue heavy-tailed search) is solid but comes from SAT and CSP solvers with independent runs and checkable answers. For language models the evidence is thin. There is one direct restart study on an LLM search loop (steel-rolling heuristics, one model, one campaign), plus a larger body of indirect evidence (repeated sampling, short-vs-long chains, self-correction). Nobody has measured the finishing-time distribution of an LLM attempt. That one missing measurement decides restart versus continue, so most of what follows is "test first".

---

## 1. What it is

**Anytime algorithm.** It can be stopped at any moment and returns a usable answer. Quality rises with run time. Zilberstein (1996) and Dean and Boddy (1988) are the origin. Properties named in the literature: measurable quality, recognisable quality, interruptibility (can stop any time), and a performance profile (expected quality as a function of time). Monotone quality and diminishing returns are usually listed too, but we only confirmed measurable quality and interruptibility (d20, Wikipedia citing Zilberstein and Grass). A contract algorithm must be told its time in advance; an interruptible one need not. The primary texts of Zilberstein, Dean and Boddy were not opened (a17, a18, d19), so the full property list is from memory (K23).

**Randomised restart.** Run a randomised search for a fixed budget (the cutoff). If it has not finished, throw the run away, change the random seed, and start again. Total cost is a sum of short tries.

**Heavy-tailed run times.** For a fixed instance, the run time of a randomised complete solver varies hugely between seeds. Most runs are long; a few are very short. The survival curve is a straight line on a log-log plot (power law). This is what makes restarts pay.

**Luby schedule.** A restart schedule that needs no knowledge of the distribution: cutoffs 1, 1, 2, 1, 1, 2, 4, 1, 1, 2, 1, 1, 2, 4, 8, ... times a unit.

**Portfolio.** Run several algorithms, or several copies of one randomised algorithm, and take the first or best result.

**Iterative deepening.** Repeat depth-limited search with a growing bound (Korf 1985). It is the deterministic cousin of restarts: each round repeats earlier work and returns an answer at each depth. We did not open Korf (a19), so only the textbook fact is used.

**LLM equivalents.**
- A restart is a fresh attempt in a fresh context, seeded differently (temperature sampling). Repeated sampling is a restart policy.
- A cutoff is a token or step limit per attempt.
- "Continue" is extending the same chain, asking for revision, or appending "Wait".
- An LLM anytime property is the quality of the answer if the chain is cut at budget B and forced to answer (Zhang 2026, Qi 2025).

**Why the schema cares.** SCHEMA.md row 19 lists this field as feeding G6 (never abstain; best answer at any stop) and the S6 trigger (what to do at an impasse). Restart versus continue is the decision at S5/S6: revise the current attempt, or start over in a fresh context at S3.

---

## 2. History and theories in depth

### 2.1 Anytime algorithms (1980s to 1990s)

Dean and Boddy (1988) introduced time-dependent planning: an agent must choose between more deliberation and acting now. They used performance profiles, the expected quality of the result as a function of run time, to allocate time. Zilberstein (1996, AI Magazine 17(3)) surveyed how to compose several anytime algorithms into a system and control them at the meta level. The key idea for us: the controller needs a profile of how quality grows with time. This is the same object as a "hazard of success per token". Both papers are [M] here (abstract or memory only).

### 2.2 Heavy tails and randomised restarts (1997 to 2000)

**Gomes, Selman and Kautz (1998)** found that very hard deterministic-solver instances were not hard in themselves. The hardness lay in the pairing of one instance with one deterministic heuristic. Adding small random tie-breaking and restarting at a cutoff removed most variance (a01, a24). Table 1 (corrected in critique): logistics.d 108 min to 95 s; 3bit-adder-32 over 24 h to 165 s; 3bit-adder-31 over 24 h to 17 min; round-robin 14 411 s to 250 s; round-robin 16 over 24 h to 1.4 h; round-robin 18 over 48 h to 22 h; blocks-world.d 30 to 23 min. No row got slower. Cutoffs were found by trial and error on the same instances (selection effect, a25).

**Gomes, Selman, Crato and Kautz (2000)** gave the statistics (a05 to a07, b04, b05). Run-time survival on satisfiable structured instances follows Pareto-Levy tails. Hill-type tail-index estimates were below 1 (infinite mean): quasigroup order 15 at 40 percent pre-assigned 0.153; order 11 at 30 percent 0.466; logistics with Satz 0.360; register allocation 0.102. Left tail too: round-robin 14 teams, 70 percent of runs exceeded 25,000 backtracks but about 1 percent finished under 650. Restart at a tiny cutoff turns the cost geometric: failure falls exponentially in total work instead of as a power law.

**Boundary conditions found in the same work:** no heavy tail for unsolvable instances, for local search (Walksat), for easy solvable instances, and for blocks-world planning (a04, a06, b03, b05). Stronger propagation (all-different) removes the tail at small order, and it returns at larger order.

### 2.3 Theory (1993, 2017)

**Luby, Sinclair and Zuckerman (1993)** (a09, a10, a20, b06): with the full run-time distribution, the optimal strategy is one fixed cutoff t* repeated forever (Theorem 3). With no knowledge, the universal sequence is within a log factor of the best fixed cutoff: expected time at most 192 * l * (log l + 5) (Theorem 5), and no universal strategy beats a log factor (Theorem 7, lower bound (1/8) * l * log l). The authors say 192 is not tuned.

**Lorenz (2017)** (b11, c30): restarts help if and only if some quantile condition holds on the distribution. Weibull shape k below 1 helps, k equal to 1 (exponential) is neutral, k above 1 hurts. Generalised Pareto helps. Log-normal with sigma below 0.48 gave no useful restart in a numerical search. Scale does not matter; shape does.

**The decision rule in plain words.** If the chance of finishing in the next moment falls as the run ages (falling hazard), restart. If it is constant, restarting is neutral. If it rises, continue. Luby (1993) even gives a distribution where continuing beats every restart strategy (a20).

### 2.4 Portfolios (1997 to 2001)

Huberman, Lukose and Hogg (1997) framed algorithm portfolios with a mean-and-risk trade-off (a28, [M]). Gomes and Selman (1997) worked it through on quasigroup completion with 10,000 runs per strategy (a15, a16, b10). A portfolio helps only when the cumulative distributions cross. If one dominates everywhere, mixing adds cost. Counter-intuitive result: many copies of the single better stochastic algorithm can beat a mixed portfolio. With 20 processors all-Brelaz-S was best in mean and standard deviation. Gomes and Selman (2001, AIJ, a27) extended this to risk-seeking strategies, [M] only.

### 2.5 Dynamic restart policies (2002)

Kautz, Horvitz, Ruan, Gomes and Selman (a11, a26, b09, b26, c29): observe the first 10 to 1,000 solver choice points, predict whether the run will be short or long with a Bayesian decision tree, and set the cutoff by the prediction. Expected run time in choice points, dynamic n-ary versus the fixed-optimal policy: QCP via CSP 3,295 vs 17,617 (about 5x); QCP via Satz 5,220 vs 11,959; graph colouring 8,962 vs 10,157; planning 5,099 vs 5,366. The paper reports 40 to 65 percent better than the fixed-optimal policy and about 6 times better than knowledge-free Luby. A 10-choice-point window worked best. Naive use of the prediction without pruning predicted-long runs did poorly. Mixed distributions: with 10 or 100 steps at equal chance, always restart after 10; with instances from different distributions the best fixed cutoff can be none (b26).

### 2.6 Clause learning changed what a restart means (2004 to 2009)

Huang (2007) (a12, a13, b07, b08, c28, d04, d05): in the clause-learning solver TINISAT, 251 industrial instances in 22 families, 2-hour limit. Solved: no restarts 127; geometric (100,1.5) 164; fixed 700 -> 166; fixed 550 -> 168; geometric (32,1.1) 174; fixed 16000 -> 178; Luby unit 32 -> 180. MiniSat 1.14 solved 128 and Siege 4 solved 182. Total days: 11.28 none, 7.68 Luby. The worst restart policy saved 2.43 days and solved 37 more. Luby's edge over a well-chosen fixed cutoff is 2 instances of 251. Per family the gaps are bigger (fvp-unsat-2.0: Luby 469.3 s vs geometric 1193.24 s vs none 1383.53 s) but no policy wins every family.

Why: clause learning with unlimited restarts simulates general resolution, while plain DPLL is exponentially weaker (Beame et al. 2004, via a13). Audemard and Simon (2009) (a14): modern solvers restart so often that most restarts occur before conflict 1000. Restart no longer means "go elsewhere". It means "reorder variable priorities and re-enter the same space by a different path", helped by phase saving and kept learned clauses. So amnesia is not the modern solver's design.

Lecoutre, Sais, Tabary and Vidal (2007) (d06, d07): in a CSP solver, plain restarts can hurt; recorded nogoods fix it. 1064 competition instances, 30 min. Timeouts for MAC, MAC+restart, MAC+restart+nogoods: dom/ddeg 365, 378, 337 (avg time 125.0, 159.0, 109.1 s); brelaz 277, 298, 261; dom/wdeg 140, 123, 121. Restart also loses on instances with a small hidden unsatisfiable core when the heuristic does not point at it (27 or 32 fewer instances solved on the ehi series).

### 2.7 Parallel restarts (2013)

Truchet, Richoux and Codognet (a21, c31): speed-up of independent multi-walk runs is predicted by the minimum order statistic of the sequential run-time distribution. Exponential gives linear speed-up; shifted exponential or lognormal gives a ceiling. Fitted from about 650 sequential runs per benchmark; prediction matched actual speed-ups on Costas arrays up to 256 cores.

### 2.8 Restarts meet language models (2022 to 2026)

Four strands, each in section 6:
1. Repeated sampling as restart (self-consistency 2022, Large Language Monkeys 2024, Schaeffer 2025).
2. Continue versus restart (Snell 2024, Huang 2024 self-correction, Olausson 2024, ParaThinker, Hassid, Zeng, Ghosal, Madaan).
3. Anytime reasoning and budgets (Qi 2025, Zhang 2026, Wang 2026, BATS 2025, TALE).
4. The one direct LLM restart study: the steel-rolling heuristic search with a Luby schedule (2026).

---

## 3. Core findings with exact numbers

Status column: E established, S single-source, C contested (from claims.jsonl).

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Restarts only help with a falling hazard (heavy tail or mixed easy/hard runs). Neutral for exponential, harmful for rising hazard. | Weibull k<1 helps, k=1 neutral, k>1 harms. Blocks-world: 30 to 23 min (1.3x), no tail. No tail for unsolvable, Walksat, easy. | Lorenz 2017; Gomes 1998, 2000; Luby 1993 (K01) | E |
| Small cutoff turns hours or unsolved into minutes on structured instances | logistics.d 108 min to 95 s; 3bit-adder-32 >24 h to 165 s; round-robin 14 411 s to 250 s; RR16 >24 h to 1.4 h; RR18 >48 h to 22 h | Gomes 1998 Table 1 (K02) | E |
| Heavy-tail indices below 1 on satisfiable structured instances | alpha 0.102 (register allocation) to 0.670 (logistics Relsat); quasigroup order 15, 40% pre-assigned: 0.153 | Gomes 2000 Table II (a05) | E (same group) |
| Best cutoff is far below the median run; cost is U-shaped | logistics.d: cutoff 16 -> success 0.009, mean cost 1,861; cutoff 128,000 -> 307,550; cutoff 4 -> 147,816; cutoff 2 -> success 0 | Gomes 1998 (K03) | E |
| LLM loop: best fixed cutoff 12 to 24 iterations | 10 to 20 iteration runs match hindsight-optimal split; 5-iteration trail by 1.5 to 3.3 points; 30-iteration trail by 0.8 to 2.4 | steel-rolling LLM paper (K18, K03) | S |
| Luby needs no distribution knowledge and is within a log factor | Theorem 5: <= 192 l (log l + 5); LLM loop: Luby u=5 costs 1.1 to 1.8x best fixed cutoff, u=1 up to 2.8x | Luby 1993; steel paper (K04) | E |
| Luby edge over a good fixed cutoff is small | 251 instances: Luby 180, fixed 16000 178, geometric (32,1.1) 174, none 127; days 7.68 vs 7.80 vs 8.00 vs 11.28 | Huang 2007 (K04) | E |
| Dynamic policies using early run signals beat the best fixed cutoff | 40 to 65 percent faster; QCP-CSP 3,295 vs 17,617 choice points; Luby about 6x slower than best dynamic | Kautz 2002 (K05) | S |
| Mixed difficulty: best fixed cutoff can be none | 10-or-100-step example; cutoff <100 gives a finite chance of never solving the hard class | Kautz 2002 (K06) | S |
| Portfolios help when distributions cross; many copies of the better algorithm can win | Quasigroup order 20, 10,000 runs per strategy. LLM: K=4 portfolio 60.9 vs oracle 65.1 (90% of gain); OOD 59.9 vs oracle 67.3 vs best single 51.2 | Gomes and Selman 1997; steel paper (K07) | S |
| Parallel speed-up equals the order statistic of the sequential distribution | exponential gives linear; linear or better to 256 cores on Costas | Truchet 2013 (K08) | S |
| Resampling is an LLM restart; coverage grows log-linearly | SWE-bench Lite 15.9% to 56% at 250 samples; MATH Llama-3-8B 82.9% at 100 to 98.44% at 10,000; CodeContests Gemma-2B 0.02% to 7.1%; Pythia-160M MATH 0.27% to 57% | Brown 2024 (K09) | S |
| Selection is the bottleneck: vote and reward model plateau | MATH Llama-3-8B vote 40.50% to 41.41% (100 to 10,000 samples); vote can fall with more calls on hard queries | Brown 2024; Chen 2024; Setlur 2025 (K10) | E |
| Per item, failure falls exponentially with attempts; the heavy tail is in pass@1 spread across items | Pythia 70M to 12B; Llama 3 8B IT (no low-pass@1 tail) shows no aggregate power law | Schaeffer 2025 (K24) | S |
| Continue vs restart depends on difficulty, task and whether a check exists | Snell: 4x less compute than best-of-N; backtracking wins Sudoku, loses CountDown; o3-mini 76.9 / 81.5 / 86.7 | Snell; Backtracking; ParaThinker; Madaan; Hassid (K11, K30) | C |
| Self-critique with no outside signal hurts | GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; HotpotQA GPT-4 49.0 to 43.0 | Huang 2024 (K12) | E |
| Unit-test feedback plus self-explanation does not beat resampling at small budgets | GPT-4 APPS 1.05x (10 drafts + 1 repair), 0.97x (2 drafts + 10 repairs); human feedback 52.6% vs GPT-4 feedback 33.3% repair success | Olausson 2024 (K12) | E |
| Long chain locks in early errors; several short paths beat one long | ParaThinker AIME24: 1.5B 2x16K 34.8 vs 32K sequential 28.3; 8x16K 48.1 vs 128K 27.4; 7B 8x16K 68.8 vs 52.7. Shortest of k beats longest by up to 34.5% | ParaThinker; Hassid; Zeng (K13) | E |
| Stop at first finishers saves compute | short-1@k up to 40% fewer thinking tokens at majority-vote accuracy; short-3@k up to 33% faster | Hassid 2025 (K13) | E |
| Too many thought switches also hurts (underthinking) | wrong answers carry about 418% more switches; >70% contain a correct thought; AIME24 QwQ 38.3 to 44.1 with switch penalty | Wang 2025 (K14) | S |
| "Wait" extension gives small gains that flatten | s1-32B AIME24 50.0, 53.3, 53.3, 56.7 for 0, 1, 2, 4 Waits (30 items, 1 item = 3.3 points); GSM8K accuracy 82.2 to 87.3 then 70.3 at 15,980 tokens | s1; Ghosal 2025 (K15) | E |
| Visible budget lets small budgets match big ones | Gemini-2.5-Pro BrowseComp 10.3 (b10), 12.6 (b100), 12.8 (b10 + tracker, 31.3% lower cost); SWE-bench Verified 36.8 to 55.4 | BATS 2025 (K16) | S |
| Counter-evidence: stated budget too small can raise token use | token elasticity | Han 2024 (K31) | S |
| Verifier returning SUCCESS/CONTINUE/PIVOT doubled agent accuracy | BrowseComp 12.6 to 24.6; BrowseComp-ZH 31.5 to 46.0; HLE-Search 20.5 to 27.0; ablation no verification 15.4 vs full 18.7 | BATS 2025 (K17) | S |
| Restarts add depth as well as breadth | 14 of 15 Luby sub-runs had best result at iteration 3 to 9 | steel paper (K19) | S |
| What crosses a restart: verified failures help; unverified answers anchor | CSP nogoods: 378 to 337 timeouts. PDR: only-wrong summaries sharply cut accuracy. Seeded top-3: best 48.3 vs 51.6, median 43.2 vs 34.4 | Lecoutre 2007; Madaan 2025; steel paper (K20, K26, K27) | C |
| Answer-agreement stopping is a valid code-only stop | Adaptive-Consistency up to 7.9x fewer samples, <0.1% drop (17 datasets, 3 models); ESC -33.8% (MATH) to -84.2% (Coin Flip); consensus stop 52.8% fewer tokens | Aggarwal 2023; Li 2024; Fu 2025 (K28) | E |
| Windowed confidence aborts weak traces | 43 to 79% fewer tokens (low); 18 to 59% (high); up to 84.7% (GPT-OSS-120B AIME25) | DeepConf 2025 (K29) | S |
| Anytime LLM reasoning can be improved by prompting or RL | PDP: final accuracy +17.6% over LEAP for strong reasoning models; Llama-3.3-70B NaturalPlan 82.0 vs 76.2 | Zhang 2026; Qi 2025 (K21) | S |
| Modern CDCL restarts reorder, not escape | most restarts before conflict 1000; unlimited restarts simulate resolution | Huang 2007; Audemard 2009 (K22) | E |
| Equal TOTAL tokens: refinement with a check sits on the Pareto frontier; parallel drafts buy latency | o3-mini at 49k effective tokens: long CoT 76.9, sequential refinement 81.5, PDR 86.7 (matched sequential budget only) | Madaan 2025 (K30) | C |

---

## 4. Mechanisms and models

### 4.1 The restart model

Let T be the number of tokens (or steps) an attempt needs to produce a verified answer, and F its distribution. One attempt with cutoff c succeeds with probability p(c) = P(T <= c). Attempts with fresh seeds are independent trials, if the seeds really are independent (for LLMs, not guaranteed).

Expected total cost with fixed cutoff c:

    E[cost(c)] = ( integral from 0 to c of S(t) dt ) / p(c)        where S(t) = 1 - F(t)

The optimum c* minimises this. Luby (1993) Theorem 3: with F known, repeat c* forever.

Hazard: h(t) = f(t) / S(t), the chance of finishing next given not finished. Falling h means restart pays. Constant h means no difference. Rising h means continue.

Implementation recipe for our agent (engineer-level):
1. For each task family, log N >= 30 attempts per item with a code verifier. For each attempt record tokens-to-first-verified-answer, or "censored" at the attempt limit.
2. Estimate per-item success per attempt (pooled), and the empirical survival curve S(t) over tokens inside an attempt, with Kaplan-Meier handling censored attempts.
3. Compute E[cost(c)] for a grid of c using the formula above. If the minimum is interior and beats c = infinity by a margin, enable restarts at c*.
4. If S(t) is near exponential (hazard flat), do not restart; spend tokens on a different thing (a check, a different operator).

### 4.2 Luby schedule implementation

    def luby(i):            # i = 1, 2, 3, ...
        k = 1
        while (1 << k) - 1 < i: k += 1
        if i == (1 << k) - 1: return 1 << (k - 1)
        return luby(i - (1 << (k - 1)) + 1)

Gives 1,1,2,1,1,2,4,1,1,2,1,1,2,4,8. Attempt i gets luby(i) * unit tokens (or iterations). Huang 2007's definition: t_i = 2^(k-1) if i = 2^k - 1, else t_(i-2^(k-1)+1) if 2^(k-1) <= i < 2^k - 1.

Choosing the unit: pick it near the typical solved length. Huang used 32 conflicts; the LLM steel loop used 5 iterations, giving schedule [5,5,10,5,5,10,20,5,5,10,5,5,10,20,40] over 160 iterations. Unit 1 cost up to 2.8x the best fixed cutoff, unit 5 cost 1.1 to 1.8x. A unit that is too small gives near-zero success per try (logistics cutoff 4: success 0.00003).

### 4.3 Dynamic (predictive) restart

Kautz 2002 recipe, transferable in shape:
1. Offline: run many attempts. Label each short or long by a threshold. Extract features of the first W steps.
2. Train a small classifier (they used a Bayesian decision tree).
3. Online: after W steps, if P(short) < 0.6, kill the attempt and restart. Otherwise let it run to a longer cutoff.
4. Prune low-confidence leaves. Naive use without pruning was worse.

LLM analogue (DeepConf): per-token group confidence over a window of 2,048 tokens, threshold calibrated from 16 warm-up traces, abort a trace whose lowest window confidence drops below it. Requires logprobs. Our agent may not have logprobs; code-only features are tool-error count, length, repeated output, answer drift.

### 4.4 Portfolio / order statistic

For k independent attempts run in parallel and stopped at the first success, time is min(T1..Tk). With F known, E[min] is computable. Exponential T gives E[min] = E[T]/k (linear). For a shifted exponential, speed-up saturates at the shift. For equal total tokens on a sequential agent, k parallel attempts of length c cost k*c, so the question is whether P(min <= c) beats P(T <= k*c).

### 4.5 Coverage versus selection

Coverage(k) = share of items with at least one verified attempt in k. Brown 2024 fit exp(a k^b). Schaeffer 2025: per item, failure is geometric: (1 - p_i)^k. Aggregate coverage is the average over the items' p_i. So the left tail of the pass@1 distribution (items with tiny p_i) sets the aggregate power law. Coverage only turns into accuracy when a verifier selects. Without one, majority vote plateaus (40.50 to 41.41).

### 4.6 Stopping on agreement

Adaptive-Consistency: after each new answer, compute the chance (Dirichlet-multinomial over answer counts) that the leading answer stays the leader; stop if above a threshold. ESC: sample in windows of 5 (8 for MATH); stop when a window is unanimous. Cheap rule for us: stop at 2 matching code-checked answers among the first 3. These decide how many attempts, not whether to restart.

### 4.7 Anytime behaviour of an LLM attempt

Define quality Q(b) as the score if the chain is cut at budget b and forced to answer. Zhang 2026's Anytime Index averages quality per token across budgets (checkpoints 100 to 800 tokens). To use it: at several cut points (25, 50, 75, 100 percent of the attempt budget) force a final answer; code scores each. A flat or falling Q(b) beyond some b is the soft cutoff. GPT-4o on NaturalPlan peaks at a medium budget and then drops slightly by 800 tokens; larger GPT-4.1 variants plateau.

### 4.8 What to carry across a restart

Three options: nothing; a short note of code-verified failures; the prior best answer. CDCL carries learned clauses (verified consequences). CSP nogood recording carries failed decision sequences. Both are verified facts, not guesses. LLM evidence agrees in direction: summaries from wrong drafts hurt (Madaan 2025). The memory note should carry facts like "output X failed check Y", never "I believe the answer is Z".

---

## 5. What holds up

### 5.1 Replicated or multi-source

- **Restarts rescue heavy-tailed structured search** (Gomes 1998, 2000; Huang 2007; Lecoutre 2007 on hard real-world RLFAP instances: about one order of magnitude). Independent teams, different solvers. [E]
- **Falling-hazard condition** (Luby 1993 remark, Lorenz 2017 theorem, Gomes boundary cases). Theory and experiments agree. [E]
- **Best cutoff is short and the cost curve is U-shaped** (Gomes 1998 tables; LLM loop's 12 to 24 iterations). [E, but second source is a 2026 preprint]
- **Self-correction without feedback fails** (Huang 2024; Olausson 2024; Laban 2025 multi-turn: 15 LLMs, average drop about 39 percent (abstract; 35 in a figure caption), concatenating all info into one fresh prompt keeps 95.1 percent of full performance; OPPO agent paper: always-on reflection 55.15 vs baseline 55.76). [E]
- **Long single chain loses to several short chains** (ParaThinker, Hassid, Zeng, Ghosal). Models: reasoning models. [E]
- **Selection, not generation, is the bottleneck** (Brown, Chen, Setlur). [E]
- **Answer agreement as stop rule** (three independent groups). [E]

### 5.2 Failures, moderators and null results

- Blocks-world planning: no heavy tail, 30 to 23 min only. Unsolvable instances, local search and easy instances: no tail.
- Plain restart in CSP raised timeouts 365 to 378 and 277 to 298 (dom/ddeg, brelaz). With dom/wdeg restart already helped (140 to 123). So restart effect depends on the heuristic.
- Small hidden unsatisfiable core (ehi series): restart wasted effort.
- Luby is not magic: 180 vs 178 solved for a good fixed cutoff; the aggregate gap between policies shrinks (1.2x total vs 2.5x on one family) because each family prefers a different policy.
- Steel-rolling paper, critique correction: the ad-hoc pool of 52 runs found 55.5 vs 51.6 for Luby, but the Luby campaign sits at the 39th percentile of 20,000 simulated campaigns (mean best 50.9), and only 22 percent of simulated campaigns reach 55.5. So the gap is mostly luck of one 730-iteration pool. The 10+10 mix versus one run of 20 gave +1.6 with a CI of [-1.1, +5.2], not significant.
- Seeding restarts with the best earlier heuristics: best 48.3 vs 51.6, median 43.2 vs 34.4. One campaign each. No conclusion.
- Vote accuracy can fall with more calls (Chen 2024), versus plateau (Brown 2024). Different shapes, different settings.
- s1 "Wait": appendix shows one-item steps; MATH500 92.6, 92.8, 93.0, 92.2 is flat. Do not read one-item differences as effects.
- Refine with unit-test feedback and self-explanation: 1.05x and 0.97x of resampling. Only a stronger critic or a human helps (33.3 to 52.6 percent).
- Self-correction with an oracle label helps (GPT-3.5 GSM8K 75.9 to 84.3; GPT-4 HotpotQA 49 to 59) but oracle labels are not available at test time.
- Multi-agent debate: no better than self-consistency at equal calls (GSM8K GPT-3.5: self-consistency 82.5 / 85.3 / 88.2 at 3 / 6 / 9 responses; debate 83.2 at 6; the 9-response debate figure of 83.0 is unchecked).
- Think Twice (re-answer with prior answer, no verifier): AIME24 QwQ-32B 80.3 to 82.1 to 83.1; R1 79.7 to 82.0; MATH-500 flat at 97.6; no equal-token control, twice the tokens.
- Underthinking (switches too often) and tunnel vision (never switches) both exist. They fit together only if the restart sits at an attempt boundary after a check. No study tests this directly.

### 5.3 Interventions that worked

- Random seeds plus a short cutoff on heavy-tailed instances.
- Luby schedule with a unit near typical solved length.
- Nogood recording across restarts (CSP) and clause retention (SAT).
- Stopping on agreement (7.9x fewer samples, under 0.1 point loss).
- Budget display in an agent (BATS tracker): 31.3 percent lower cost at equal accuracy.
- Verifier-gated PIVOT with summary (BATS): 12.6 to 24.6. Model-made verdict.
- Switch-token penalty (QwQ 38.3 to 44.1).

### 5.4 Interventions that did not work

- Self-critique with no signal; always-on reflection; debate; plain "Wait" beyond a few repeats; very small cutoffs; restarts on easy or unsolvable items; plain restart with amnesia in some CSP solvers; passing wrong candidates forward; stated budgets that are too tight.

---

## 6. Language models

### 6.1 Repeated sampling as restart

- Large Language Monkeys (Brown 2024): coverage is roughly log-linear in samples over four orders of magnitude (a22, b12, c14, c15). SWE-bench Lite DeepSeek-Coder-V2: 15.9 to 56 percent at 250 samples (single-attempt SOTA 43 percent). Exceptions: Pythia on CodeContests stayed at 0 coverage at 10,000; Llama-3-8B on MiniF2F deviates from the fit.
- Schaeffer 2025 (d01): per item, geometric failure; the heavy tail is in the pass@1 spread across items. This means restart gains come from item heterogeneity. Llama 3 8B IT in jailbreaking has no low-pass@1 tail and no aggregate power law. The within-attempt token hazard is still unmeasured.
- Self-consistency (Wang 2022, abstract only [M]): GSM8K +17.9, SVAMP +11.0, AQuA +12.2, StrategyQA +6.4, ARC-challenge +3.9 over greedy chain of thought.
- Chen 2024: vote accuracy rises then falls with calls as hard queries get worse (MMLU Physics: 53 percent easy, 47 percent hard under Vote).

### 6.2 Continue versus restart

- Snell 2024 (a23, b15, c16): on easy questions sequential revisions win; on hard ones parallel or tree search wins. Compute-optimal by difficulty needs up to 4x less compute than best-of-N (64 vs 256 samples), and test-time compute on a smaller model can beat a 14x larger one on easy and intermediate questions. The revision model was trained for revision. Naive revision flipped about 38 percent of correct answers to incorrect. Difficulty bins used pass@1 from many samples, which we cannot afford.
- Backtracking paper (c24): task dependent. CountDown 17M model: best-of-n beats backtracking; Sudoku 38M: backtracking wins and the gap shrinks with budget.
- Equal total tokens (d08 Madaan 2025): o3-mini at 49k effective tokens, Long CoT 76.9, SR 81.5, PDR 86.7 (PDR only at matched sequential budget; counting all tokens, SR is on the frontier and parallel drafts buy latency).
- Wait-extension without a check (d11 Ghosal): parallel thinking about 22 percent higher at 16K budget; hump-shaped accuracy driven by rising variance.
- Inverse-entropy voting (c35, snippet only [M]): sequential wins GPQA-Diamond 74.2 vs 70.2 at 6 chains. Not verified.
- Art of Scaling (c27): no strategy wins everywhere. R1 easy items 0.95 with short traces vs 0.72 with long. Over 30 billion tokens, eight models 7B to 235B.
- **Reading.** The deciding factor is whether the continuation contains a real check. With a check, refinement is on the frontier. Without one, fresh short attempts win. Contested (K11, K30).

### 6.3 One long attempt versus several short

- ParaThinker (c25): flawed prefixes of 0 to 1,600 tokens lowered accuracy ("tunnel vision"). Average gain with 8 paths 12.3 percent (1.5B), 7.5 percent (7B) at about 7.1 percent extra latency; beats majority vote by 4.3 and 2.0 percent.
- Hassid (b18, c18): shortest-of-k beats random by up to 18.8 percent and the longest by up to 34.5 percent (gaps reported as percentages), chains 50 and 67 percent shorter. short-1@k saves up to 40 percent of thinking tokens.
- Zeng (d12): correct solutions are shorter than wrong ones for the same question. Self-revisions rarely turn wrong into right. Some models degrade with reflection length (QwQ, R1-Distill-1.5b); others improve early then oscillate.
- s1 rejection sampling for short length (d13): average tries needed 655, 97, 8, 3, 2, 1 for the listed length limits; accuracy fell as allowed length rose (inverse scaling). This is indirect support for a falling hazard of success per token (K25).

### 6.4 Direct LLM restart study: steel-rolling heuristics

(c01 to c06, b20, b21, critique item 4.) Gemini 2.5 Pro, temperature 1.0, fresh context per sub-run, an LLM writes control heuristics, reward scored by simulator.

- 52 independent ad-hoc runs, 730 iterations. Half of runs found their best by iteration 4 (mean 8). Median best-so-far reward about 30 at iteration 5 and about 40 at iteration 17. Fresh restart gains more than continuing for the first few iterations; curves meet near iteration 4.
- Luby unit 5, 15 sub-runs, 160 iterations: unseeded best 51.6, median 34.4; seeded best 48.3, median 43.2. Ad-hoc best 55.5 median 30.4 (730 iterations, 27 h vs 4.1 h).
- Time-to-threshold at five reward targets: best fixed cutoff 12 to 24 iterations. Luby u=5 needs 1.1 to 1.8x; u=1 up to 2.8x. u=5 beats fixed-30 on 3 of 5 targets and is at most 13 percent worse on the others.
- Simulation: Luby trails the optimum by at most 1.3 reward points up to 160 iterations.
- 14 of 15 sub-runs peaked at iteration 3 to 9: restarts add depth and breadth.
- Portfolio: K=4 gives 60.9 vs oracle 65.1; held-out half 61.7 vs 60.6 same-half. Out of distribution (42 cases): Luby pool of 156 heuristics: best single 51.2, K=4 59.9, oracle 67.3. Ad-hoc pool of 18: 41.8, 58.7, 63.6.
- Mode collapse inside a run: the LLM converged on conventional controllers. Restarts counter it. Conversation compaction caused amnesia (tweaks rediscovered several times).
- Limits: one domain, one model, one real campaign, one preprint, not peer reviewed; no verifier-free setting.

### 6.5 Budgets, stopping and anytime reasoning

- BATS (c11 to c13): Gemini-2.5-Pro BrowseComp ReAct b10 10.3, b100 12.6 (saturates); with tracker at b10 12.8, 40.4 percent fewer search calls, 19.9 percent fewer browse calls, 31.3 percent lower cost. tau2-bench Retail Gemini-2.5-Flash b10 Avg@4 47.8 to 55.5. SWE-bench Verified Gemini-3-Flash-Preview b50 36.8 to 55.4. Full BATS BrowseComp 24.6. Claude-Sonnet-4 12.2 to 19.1. Note: the pivot decision is model-made, which conflicts with our rule that code decides.
- TALE (d17): telling the model a budget compresses chains (about 67 percent fewer output tokens with under 3 percent accuracy loss for TALE-EP) but a budget that is too small makes the model overshoot (token elasticity).
- DeepConf (d14): 43 to 79 percent fewer tokens at about equal accuracy; 52.8 percent saving with the consensus stop at threshold 0.95; threshold 0.90 cost accuracy. Overconfident wrong traces defeat it.
- Anytime reasoning training/prompting (Qi 2025 abstract only; Zhang 2026 PDP): final accuracy +17.6 percent, average +11.4 percent, Anytime Index +7.9 over LEAP for strong reasoning models; PDP better than LEAP in 6 of 7 models; Llama-3.3-70B NaturalPlan 82.0 vs 76.2.
- Conformal Thinking (Wang 2026): two-threshold stop calibrated on 50 validation samples keeps error under target; the lower threshold saves tokens mainly when unsolvable items are common (1:1 and 1:3 mixes).
- Setlur 2025 (d18): verifier-free methods do not scale as well as verifier-guided search, and the gap widens with compute.

### 6.6 What changed LLM behaviour, by how much (ranked by size and reliability)

1. A real verifier (coverage 15.9 to 56; repair success 33.3 to 52.6 with a better critic). Large.
2. Restart at the right length vs very long runs (ParaThinker 8x16K 48.1 vs 128K 27.4). Large, reasoning models.
3. Correct memory across restarts (CSP 378 to 337 timeouts). Moderate, non-LLM.
4. Agreement-based stopping (33.8 to 84.2 percent fewer samples). Large saving, no accuracy change.
5. Budget visibility (31.3 percent cost). Moderate, single source.
6. Wait extension, forced re-answer (+1 to 4 points). Small and flat.
7. Self-critique with no signal (negative, up to minus 34 points on one set).

---

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory. Evidence ids in brackets.

### Add now (established [E])

1. **[E] G6/S5 rule: no unsupported self-critique as a revision.** S5 REVISE already requires real failing output (G2). This is confirmed from a new angle: self-critique with no signal lowered GPT-4 GSM8K 95.5 to 89.0 and GPT-3.5 CommonSenseQA 75.8 to 41.8; unit-test plus self-explanation repair gave 0.97x to 1.05x of resampling. Part G2/S5. Claim K12. Evidence b16, c21, d02, d03.
2. **[E] G11 wording: prefer several short independent attempts over one long one, and do not extend a chain by forcing "Wait" without a check.** Evidence ParaThinker (c25), Hassid (b18), Zeng (d12), Ghosal (d11), s1 (d13). Part G11, S3. Claim K13, K15. The schema already says this; the new content is that "Wait" gains flatten and the one-item steps in s1 are noise.
3. **[E] Selection by a check, not by vote, is the bottleneck.** Coverage grows with attempts while vote plateaus (40.50 to 41.41). Spend on verification quality (S4/S8) before attempt count. Part G5, S4, S7. Claim K10. Evidence b13, c15, b14, d18.
4. **[E] Stop sampling on code-visible agreement.** Rule: stop at S3 when the same code-checked answer appears in 2 of the first 3 attempts; keep G4 (agreement is a hint, not proof). Part G12, S3, S7. Claim K28. Evidence d14, d15, d16. This answers "how many attempts", not "restart or continue".
5. **[E] Restart is a conditional tool.** Restart helps only with a falling hazard (heavy tail, mixed easy/hard). Do not restart on easy, unsolvable, or local-search-like tasks. Part G12 note, S6. Claim K01. Evidence a04, a06, b05, b11.
6. **[E] If restarts are used, use a short cutoff below the median attempt length, and a Luby-style schedule when the distribution is unknown.** Part S6/S3 parameters. Claims K03, K04. Evidence a02, b02, a10, d04. Mark the unit as [D] until measured on our items.
7. **[E] Cap attempt length and restart at attempt boundaries, not mid-thought.** Combine K13 (long chains lock in errors) with K14 (frequent switching harms). Part G11, S3. Note K14 itself is [S].
8. **[E] Log the data that makes the restart decision measurable.** Per attempt: tokens used, tokens to first verified answer, whether censored, round of the best answer, number of switches. Part section 6 of SCHEMA (logging). Claim K24 (test).

### Test first ([S] single-source or [C] contested)

1. **[C] Restart vs continue vs hybrid at equal total tokens.** K11, K30. Evidence d08, d11, d12, a23, b15, c24. Part S5/S6. Needs the 30+ attempts experiment (section 8, T1).
2. **[S] Luby-scheduled fresh attempts, unit near typical solved length.** K04, K18. Evidence b20, c03, c04. Part S6.
3. **[C] What crosses a restart: nothing / verified-facts note / prior answer.** K20, K26, K27. Evidence d06, d09, d10, c06. Part memory, S6. Working rule only: carry code-verified failures, not unverified answers.
4. **[S] Within-attempt hazard and soft cutoff.** K24, K25. Evidence d01, d12, d13. Part S6, G12.
5. **[S] Early-signal abort from code-only features.** K05, K29. Evidence a11, b09, d14. Part S6. LLM version needs logprobs or code-visible features such as repeated tool error.
6. **[S] Portfolio K=2 to 4 of candidates selected by a cheap verifier on held-out items.** K07. Evidence c06, b21, a15. Part S7.
7. **[S] Budget line in the prompt (tokens or attempts left).** K16, K31. Evidence c11, c13, d17. Part G12/S0. Risk: early give-up and token elasticity.
8. **[S] Code rules replacing BATS's model-made PIVOT verdict.** K17. Evidence c12. Part S6.
9. **[S] Forced answer at 25/50/75/100 percent of budget (anytime profile).** K21. Evidence c07, c08, c09. Part G6, S8.
10. **[S] Difficulty-routed sequential versus parallel.** K11. Evidence a23, d12. Part S0, G12. No usable cheap router exists yet.

---

## 8. Concrete tests on our bench

All arms get the same total tokens per item, counting setup, verifier calls and every retry (G7). Items: ARC items with code-checkable outputs and BrainTeaser items with checkable answers, split into a pilot set (choose parameters) and a held-out set (report). Report with bootstrap CIs; one item is a unit of analysis.

| # | Test | Item type | Arms (equal total tokens) | Metric | Expected effect |
|---|---|---|---|---|---|
| T1 | Hazard measurement | 20 ARC and 20 BrainTeaser items per family, 30+ fresh attempts each | no arms; descriptive | tokens-to-first-verified, per-item geometric rate, Kaplan-Meier S(t), fitted Weibull shape | Shape k<1 on hard ARC items (restart pays); k near 1 on BrainTeaser (neutral). Prior: spread of per-item pass@1 is wide. |
| T2 | One long vs k short vs Luby | same items | A one attempt of full budget; B k=4 fresh attempts of B/4; C Luby with unit = median solved length; D continue with "Wait" rounds | solved share at equal tokens; tokens to first verified | B and C beat A on hard ARC items by 5 to 15 points; D flat. If hazard flat, all within noise. |
| T3 | Cutoff sweep | same | attempt length 0.25x, 0.5x, 1x, 2x of median solved length at fixed total tokens | solved share | Interior optimum at 0.5x to 1x (U-shape). |
| T4 | What crosses a restart | same | A none; B verified-facts note (code-verified failed approaches and error tags); C prior best answer shown | solved share; rate at which next answer equals the carried wrong answer (anchoring) | B >= A > C. C raises repeat-of-wrong-answer rate. |
| T5 | Refine vs fresh | items with a code check result | A refine with self-critique only; B refine with the check output (S5 as designed); C fresh restart; D 1 revision then fresh | solved share | A < C; B >= C on easy and medium; D best on mixed. |
| T6 | Early abort from code features | same, 30+ attempts per item | A Luby; B abort when features predict long: repeated tool error, no new verified fact for N steps, answer unchanged | tokens per solved item; AUC of the feature for final success | B saves 20 to 40 percent tokens at equal solved share if AUC > 0.7. |
| T7 | Agreement stop | same | A fixed 4 attempts; B stop when 2 of first 3 attempts agree on a code-checked answer | accuracy and tokens | B saves 30 to 50 percent tokens, accuracy within 1 point. |
| T8 | Portfolio of candidates | pool from T2 on a validation slice; held-out items | A best single candidate; B K=2; C K=4 chosen by cheap verifier | held-out solved share | K=4 captures 60 to 90 percent of oracle gain on held-out; much less if selection overfits. |
| T9 | Budget display | same | A hidden; B "attempts left / tokens left" line | solved share; share of items abandoned before the first failed check | B equal or better, with early-giveup rate watched. |
| T10 | Anytime profile | same | force answer at 25/50/75/100% of attempt budget | accuracy by cut point | monotone then flat. Where it turns down, set the soft cutoff. |

Order of run: T1 (it decides whether T2, T3 and T6 are worth running), then T2, T4, T5.

---

## 9. What does not transfer, and why

- **Independence of runs.** Solver restarts use independent seeds on a deterministic function. LLM attempts share a prompt, temperature and a model whose samples are alike (G4). Per-item geometric failure (Schaeffer) is consistent with independence only if p_i is constant per item, which is assumed, not tested.
- **Run-time units.** Backtracks and conflicts are clean progress units. Tokens are not: a long chain may contain no progress, a short one may contain the answer.
- **Hazard.** SAT run times are measured to the first solution. LLM attempts end with an answer of unknown quality. Without a verifier there is no "finish" event.
- **Learned clauses.** Modern SAT restarts work because learned clauses persist. An LLM restart in a fresh context has no automatic equivalent (a note must be written, and wrong notes anchor).
- **Heavy tail evidence is for satisfiable, structured instances.** Unsolvable instances, local search and easy instances show none. ARC items that are too easy, or BrainTeaser items solved by direct answer, will behave like those.
- **Luby's guarantee is about expected time with an unknown but fixed distribution.** It says nothing about token cost of overhead per restart (re-reading the task, S1/S2 setup). Our G7 says setup cost counts; at small cutoffs it can dominate.
- **Trained revision models.** Snell's sequential-revision gains used a model fine-tuned for revision. A prompted model flips about 38 percent of correct answers to wrong on naive revision.
- **Parallel speed-up.** Truchet's linear speed-up needs real parallel cores. We count tokens, not wall time, so parallelism buys latency only (d08).
- **Verifier-dependence.** Coverage gains need an automatic verifier. Open-ended tasks and ARC tests with weak hold-outs do not have one (G3).
- **Anytime properties from the classic literature** (monotone quality, diminishing returns) are not guaranteed for LLM chains: quality can fall with length (GPT-4o NaturalPlan, Ghosal hump).
- **Model-made verdicts.** BATS's PIVOT is decided by a model; our schema forbids that unless the signal is code. The gain may not survive.

---

## 10. Open questions

1. What is the finishing-time distribution of an LLM attempt (same prompt, different seeds) on ARC and BrainTeaser? Heavy tail, flat, or rising hazard? (Gap 1, nobody has measured it.)
2. At equal total tokens, which wins: one long, k short, or Luby? What unit size? (Gap 2; no Luby arm on ARC or BrainTeaser exists.)
3. With no or weak verifier, is any restart schedule better than continuing? What is the best code-only stop (repeated tool error, no new fact for N steps, same answer across restarts)? (Gap 3; no evidence for the first two signals.)
4. Does a verified-facts note cross restarts without anchoring? Is there a direct anchoring-versus-diversity trade-off? (Gap 4)
5. Can features from the first few hundred tokens predict failure, and how much does that beat Luby at equal tokens? (Gap 5; DeepConf used 2,048-token windows.)
6. Does the continue-vs-restart rule flip with first-attempt difficulty, and can a cheap pilot attempt route? (Gap 6; nothing found.)
7. Does external-feedback refinement beat fresh restart on reasoning models, with tool results other than unit tests? (Gap 7; only 2023-era models tested.)
8. How much of a K=2 to 4 portfolio's gain holds on held-out items? (Gap 8; nothing new.)
9. Does an attempt counter make the agent quit early when restarts are allowed? (Gap 9)
10. Foundations still unopened: Zilberstein 1996, Dean and Boddy 1988, Korf 1985, Luby 1993 (theorems read only via secondary quotes and an earlier agent's local copy), Huberman 1997, Gomes and Selman 2001. (Gap 10)
11. Is the steel-rolling result a general LLM pattern? It is one domain, one model, one campaign.
12. Do the 2026 anytime-reasoning preprints (Zhang, Conformal Thinking) replicate?

---

## 11. Sources

[V] opened as full paper or page text this run (including earlier agent passes and the critique re-open). [M] snippet, abstract only, or memory only.

**Classic search and restarts**
- [V] Gomes, Selman, Kautz (1998) Boosting Combinatorial Search Through Randomization. https://www.cs.cornell.edu/gomes/pdf/1998_gomes_aaai_iaai_boosting.pdf (a01 to a04, a24, a25, b01 to b03; re-opened in critique)
- [V] Gomes, Selman, Crato, Kautz (2000) Heavy-Tailed Phenomena in Satisfiability and Constraint Satisfaction Problems. https://www.cs.princeton.edu/courses/archive/fall13/cos402/readings/jar.pdf and https://www.cs.cornell.edu/gomes/pdf/2000_gomes_jar_phenomena.pdf (a05 to a08, b04, b05)
- [V] Luby, Sinclair, Zuckerman (1993) Optimal speedup of Las Vegas algorithms. https://cs.utexas.edu/~diz/Sub%20Websites/Research/optimal_speedup_of_las_vegas_algorithms.pdf (a09, a10, a20, b06; critique could not re-open; c32 secondary only)
- [V] Kautz, Horvitz, Ruan, Gomes, Selman (2002) Dynamic Restart Policies. https://www.erichorvitz.com/drestart.pdf (a11, a26, b09, b26, c29)
- [V] Huang (2007) The Effect of Restarts on the Efficiency of Clause Learning. https://users.cecs.anu.edu.au/~jinbo/07-ijcai-restarts.pdf and https://www.ijcai.org/Proceedings/07/Papers/373.pdf (a12, a13, b07, b08, c28, d04, d05)
- [V] Audemard, Simon (2009) Predicting Learnt Clauses Quality in Modern SAT Solvers. https://www.ijcai.org/Proceedings/09/Papers/074.pdf (a14)
- [V] Lecoutre, Sais, Tabary, Vidal (2007) Nogood Recording from Restarts. https://www.ijcai.org/Proceedings/07/Papers/019.pdf (d06, d07)
- [V] Lorenz (2017) Runtime Distributions and Criteria for Restarts. https://arxiv.org/pdf/1709.10405 (b11, c30)
- [V] Truchet, Richoux, Codognet (2013) Prediction of Parallel Speed-ups for Las Vegas Algorithms. https://arxiv.org/pdf/1212.4287 (a21, c31)
- [V] Gomes, Selman (1997) Algorithm Portfolio Design: Theory vs. Practice. https://arxiv.org/pdf/1302.1541 (a15, a16, b10)
- [M] Gomes, Selman (2001) Algorithm portfolios, Artificial Intelligence 126. http://www.cs.cornell.edu/gomes/gomesAIJ01.pdf (a27, text not extractable)
- [M] Huberman, Lukose, Hogg (1997) An economics approach to hard computational problems, Science. https://doi.org/10.1126/science.275.5296.51 (a28)

**Anytime algorithms and foundations**
- [M] Zilberstein (1996) Using Anytime Algorithms in Intelligent Systems, AI Magazine 17(3). https://www.doi.org/10.1609/AIMAG.V17I3.1232 and https://ojs.aaai.org/aimagazine/index.php/aimagazine/article/view/1232 (a17, d19; abstract only, PDF returned empty)
- [M] Dean, Boddy (1988) An analysis of time-dependent planning, AAAI-88. https://aaai.org/papers/00049-an-analysis-of-time-dependent-planning/ (a18)
- [M] Korf (1985) Depth-first iterative-deepening, Artificial Intelligence 27. https://doi.org/10.1016/0004-3702(85)90084-0 (a19)
- [V] Wikipedia, Anytime algorithm (accessed 2026-10-26). https://en.wikipedia.org/wiki/Anytime_algorithm (d20; secondary)

**LLM repeated sampling, selection, verification**
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (a22, b12, b13, c14, c15; re-opened in critique)
- [V] Schaeffer et al. (2025) How Do Large Language Monkeys Get Their Power (Laws)? https://arxiv.org/abs/2502.17578 (d01)
- [V] Chen et al. (2024) Are More LLM Calls All You Need? https://arxiv.org/abs/2403.02419 (b14, c17)
- [M] Wang et al. (2022) Self-Consistency Improves Chain of Thought Reasoning. https://arxiv.org/abs/2203.11171 (b25, abstract only)
- [V] Setlur et al. (2025) Scaling Test-Time Compute Without Verification or RL is Suboptimal. https://arxiv.org/abs/2502.12118 (d18)
- [V] Aggarwal, Madaan, Yang, Mausam (2023) Let's Sample Step by Step: Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d15)
- [V] Li et al. (2024) Escape Sky-high Cost: Early-stopping Self-Consistency. https://arxiv.org/abs/2401.10480 (d16)
- [V] Fu et al. (2025) Deep Think with Confidence. https://arxiv.org/abs/2508.15260 (d14)

**LLM continue versus restart**
- [V] Snell, Lee, Xu, Kumar (2024) Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters. https://arxiv.org/abs/2408.03314 (a23, b15, c16; re-opened in critique)
- [V] Huang et al. (2024) Large Language Models Cannot Self-Correct Reasoning Yet. https://arxiv.org/abs/2310.01798 (b16, c21, c22; re-opened in critique)
- [V] Olausson et al. (2024) Is Self-Repair a Silver Bullet for Code Generation? https://arxiv.org/abs/2306.09896 (d02, d03)
- [V] Laban et al. (2025) LLMs Get Lost In Multi-Turn Conversation. https://arxiv.org/abs/2505.06120 (c23)
- [V] OPPO AI Agent Team (2025) Scaling Test-time Compute for LLM Agents. https://arxiv.org/abs/2506.12928 (b19)
- [V] To Backtrack or Not to Backtrack (2025). https://arxiv.org/abs/2504.07052 (c24)
- [V] Wen et al. (2025) ParaThinker. https://arxiv.org/abs/2509.04475 (c25)
- [V] Hassid, Synnaeve, Adi, Schwartz (2025) Don't Overthink it. https://arxiv.org/abs/2505.17813 (b18, c18; re-opened in critique)
- [V] Zeng et al. (2025) Revisiting the Test-Time Scaling of o1-like Models. https://arxiv.org/abs/2502.12215 (d12)
- [V] Ghosal et al. (2025) Does Thinking More Always Help? Mirage of Test-Time Scaling. https://arxiv.org/abs/2506.04210 (d11)
- [V] Muennighoff et al. (2025) s1: Simple test-time scaling. https://arxiv.org/abs/2501.19393 (b17, c26, d13)
- [V] Madaan et al. (2025) Rethinking Thinking Tokens: LLMs as Improvement Operators (Parallel-Distill-Refine). https://arxiv.org/abs/2510.01123 (d08, d09)
- [V] Think Twice: Enhancing LLM Reasoning by Scaling Multi-round Test-time Thinking (2025). https://arxiv.org/abs/2503.19855 (d10)
- [V] The Art of Scaling Test-Time Compute for Large Language Models (2025). https://arxiv.org/abs/2512.02008 (c27)
- [M] The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency (2025). https://arxiv.org/abs/2511.02309 (c35, snippet only)
- [V] Wang et al. (2025) Thoughts Are All Over the Place: On the Underthinking of o1-Like LLMs. https://arxiv.org/abs/2501.18585 (c19, c20)

**LLM budgets, anytime reasoning, direct restart study**
- [V] LLM-Driven Heuristic Synthesis for Industrial Process Control / From Language Models to Control Policies (steel rolling, 2026). https://arxiv.org/abs/2603.20537 (b20, b21, c01 to c06; re-opened in critique)
- [V] BATS authors (2025) Budget-Aware Tool-Use Enables Effective Agent Scaling. https://arxiv.org/abs/2511.17006 (c11 to c13; re-opened in critique)
- [V] Han et al. (2024) Token-Budget-Aware LLM Reasoning (TALE). https://arxiv.org/abs/2412.18547 (d17)
- [V] Zhang et al. (2026) Budget-Aware Anytime Reasoning with LLM-Synthesized Preference Data. https://arxiv.org/abs/2601.11038 (b23, c07 to c09; no replication)
- [V] Wang et al. (2026) Conformal Thinking: Risk Control for Reasoning on a Compute Budget. https://arxiv.org/abs/2602.03814 (b24, c10; no replication)
- [M] Qi et al. (2025) Optimizing Anytime Reasoning via Budget Relative Policy Optimization. https://arxiv.org/abs/2505.13438 (b22, c33; abstract only, no numbers)
- [M] Romera-Paredes et al. (2024) FunSearch. https://www.nature.com/articles/s41586-023-06924-6 (c34, snippets only: islands periodically reset and refilled from the best)
