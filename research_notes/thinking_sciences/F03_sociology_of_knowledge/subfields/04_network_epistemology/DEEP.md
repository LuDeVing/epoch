# Network epistemology: deep document

*Subfield F03.04. Scope: how the communication structure of a group of learners changes what the group learns, how fast and how reliably. Built from evidence_a-d.jsonl, claims.jsonl (K01-K32) and critique.md in this folder. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Network epistemology asks one question. If many agents each gather evidence and also see what their neighbours found, which pattern of who-sees-whom gives the best group belief?

The core model is the Bala-Goyal bandit, brought into philosophy of science by Zollman (2007). Agents choose between an old action (A1, known payoff) and a new action (A2, unknown but possibly better). Each agent sees its own results and its neighbours' results and updates by Bayes. The group is "right" when everyone ends up on the better action.

The headline result is the Zollman effect. A sparsely connected group is more often right than a fully connected group. The price is speed: the sparse group takes much longer. More communication can hurt reliability. It buys speed.

Why it matters for our agent. Our agent is one language model run through a scaffold. Its "community" is a set of attempts, drafts and checks inside one task. State S3 (generate) and guardrail G4 (samples from one model are not independent) ask: should attempts be fresh and isolated, or should they see each other? This subfield gives the best formal and empirical answer we have, and it also shows where that answer does not carry over.

Honest summary. The effect is real in its original model. It is fragile: it needs a hard-to-detect better option and a small group. Human experiments are mixed. For language models no study runs the real Zollman design. There is indirect evidence from debate studies, and it mostly says: independent samples plus a vote or a checker beat free-form talk at equal tokens.

## 2. History and theories in depth

**Information cascades and herding (background).** Lab work by Anderson and Holt 1997, Hung and Plott 2001, Kubler and Weizsacker 2004/2005 and Ziegelmeyer et al 2010 shows people ignore private information when public information is available, and overpay for private information. Reviewed in Zollman 2025 (a06, a07) [V]. This is the human root of "seeing others makes us stop looking".

**Bala and Goyal (1998), Learning from Neighbours.** The founding economic model (opened as the 1996 working-paper version, d01, d02).
- A "Royal Family" is a small set of agents seen by everyone. In the example each agent on an integer line sees both neighbours plus a royal family of 5. With positive probability all five give a bad first draw. Every agent then switches to the safe action at t=2 and learning stops.
- Simulations (N=100, royal family size 1 to 10, Bernoulli and Normal payoffs): the chance of incomplete learning reaches about 0.2. On a ring, log probability of incomplete learning is near linear in N (R-squared above 0.99 Bernoulli, 0.94 to 0.98 Normal).
- Caution from critique.md: this paper is not the Zollman speed-versus-reliability model. Do not cite it for that.

**Zollman (2007, 2010).** Imports the model into philosophy of science (a01-a05, b01, b02). Payoffs 0.5 vs 0.501; networks of 2 to 12 agents; 10,000 runs each. Cycle beats wheel beats complete in reliability at every size. Complete is fastest, cycle slowest. The 2010 paper (beta priors) reports the same ordering and calls it robust.

**Mayo-Wilson, Zollman and Danks (2011, 2013).** "The independence thesis": individual rationality and group rationality can come apart. Not opened (a17, d20). An open foundation.

**Landscape-search models.**
- Lazer and Friedman (2007): on rugged landscapes, slow networks do better in the long run because they keep diversity. Not opened (a18, b14).
- Mason and Watts (2012) ran the human version and found the opposite: efficient networks did better (d03, d04).
- Barkoczi and Galesic (2016) reconciled the two in simulation (a13, b12, b13). The copying rule decides the winner. Copy-the-best favours slow networks (r = +0.83 between diameter and payoff). Conformity favours fast networks (r = -0.77). This is a model result, not a human replication.

**Critiques and boundary work.**
- Rosenstock, Bruner and O'Connor (2017) re-ran Zollman over a wide sweep (a09-a12, b04-b08). The effect is real but lives in a narrow corner: nearly identical options, few trials per round, small groups.
- Kummerfeld and Zollman (2016): with exploratory (epsilon-greedy) agents the effect reverses and dense networks win. Rosenstock et al re-ran this; it also shrinks under wider payoff settings (a11, b07).
- Weatherall and O'Connor (2020) added conformity (a14, b11). If agents dislike disagreeing with neighbours, consensus gets rarer and wrong consensus more common.
- Holman and Bruner (2015): when biased agents try to sway a community, connected networks do better (b08, b18; not opened). The best structure depends on the threat.
- Zollman (2025) handbook review (a06-a08, a25, b09, b10): sparse structure is one of several ways to keep diversity. Others: extreme initial opinions, ignoring subcommunities, confirmation bias. Some polarise (Wu and O'Connor 2023).

**Human experiments on structure.**
- Mason and Watts 2012 (d03, d04): networked beat independent; efficient beat inefficient.
- Derex and Boyd 2016 (d05): partial connectivity helped cumulative innovation.
- Becker, Brackbill and Centola 2017 (d06): decentralised networks improved estimates through social influence even while diversity fell.
- Jonsson, Hahn and Olsson 2015: a small-world network beat the complete one (b10, snippet).

**The LLM turn (2023-2026).** Three streams. (1) Multi-agent debate (Du et al 2023, a24) and its critics (Choi, Zhang, Wang, Tran and Kiela). (2) Topology work on agent graphs (Li 2024, MacNet, AgentPrune, Wang 2025/2026). (3) Collective-dynamics studies that borrow network theory (Han 2026, Zheng 2026, Hirota 2026, Ann 2026). None runs the Bala-Goyal bandit with independent versus shared LLM agents. The nearest single-agent fact is Krishnamurthy et al 2024 (d07).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Sparse network learns the better arm more reliably than dense (hard case) | pA=0.5, pB=0.501; cycle > wheel > complete at sizes 3-12; 10,000 runs per network | Zollman 2007 (a01, b01) | [E] K01 |
| Cost of sparsity is speed | Size 100: complete about 20 rounds, cycle about 1,977; 99.12% vs 100% correct | Rosenstock 2017 (a10, b06) | [E] K02 |
| Effect is parameter-fragile | Gap 0 for pB >= 0.525; under 2 points at pB=0.51; largest for groups of 6-20 and few trials per round | Rosenstock 2017 (a09, b04, b05) | [S] K03 (one paper, not re-opened) |
| Effect reverses with exploratory agents | 8 agents; eps=0.05 cycle better; eps=0.35 complete better; shrinks when better-arm mean 1 to 4 or SD 9 to 3 | Kummerfeld-Zollman via Rosenstock (a11, b07) | [S] K04 |
| Density, not hub centrality, predicts failure | Degree variance uncorrelated with success on all graphs of size 3-6; cycle beats wheel | Zollman 2007 (a03, b02) | [S] K05 |
| Mechanism is containment | After bad luck about 4x more agents switch in dense networks; with one A2 player left, dense is almost 3x as likely to lose it | Zollman 2007 (a04) | [S] K06 |
| Misleading pooled evidence is common | Four negative results pooled: posteriors 0.18-0.46; misleading outcome probability 0.16 | Zollman 2007 (a02) | [S] |
| Royal Family lock-in | Wrong-action lock-in up to about 0.2 (N=100, family of 5) | Bala and Goyal (d01, d02) | [S] K25 |
| Best network depends on copying rule | Diameter vs payoff r = +0.83 (best-member), r = -0.77 (conformity); 100 agents, 10 networks | Barkoczi and Galesic 2016 (a13, b12) | [E] K07 (simulation only) |
| Conformity raises wrong consensus | k=0: 96% true consensus. k=0.1: consensus about 16% of runs; correct 55%, incorrect 44% (10,016 sims per cell) | Weatherall and O'Connor (a14, b11) | [S] K08 |
| Humans: efficient networks better | 256 experiments, groups of 16, 8 topologies; path-length beta = -4.63; networked 68 vs independent 39 when peak found; peak found in 138 of 232 sessions | Mason and Watts 2012 (d03, d04) | [C] K09 |
| Humans: temporary isolation helps recombination | 12 groups of 6 per arm; both 3rd-level innovations 58.3% vs 0%; A3 91.7% vs 50% | Derex and Boyd 2016 (d05) | [S] K24 |
| Humans: decentralised influence helps | Diversity down 43%, individual error down 23%, median error 0.76 to 0.67 SD | Becker et al 2017 (d06) | [S] |
| Sparse LLM debate matches or beats full | GPT-3.5 MATH: sparse +3.0 to +7.5 over self-consistency, full +4.0; neighbour-connected about +2% over full; input tokens -41.5% (MATH), -43.5% (GSM8K) | Li et al 2024 (a19, b19, c06) | [E] K10 |
| Random edge pruning is nearly free | 10-30% of links pruned gained up to 2.83% MMLU; 28.1-72.8% token cut | AgentPrune (b24) | [E] K10 |
| Debate gain is mostly voting | Majority vote on par with debate; debate is a martingale in expectation (Theorem 2) | Choi et al 2025 (a23) | [E] K11 |
| Debate rarely beats plain CoT | 36 configs; four frameworks beat CoT in about 15% of cases; GPT-4o-mini SoM below CoT on all 9 datasets | Zhang et al 2025 (b25, c13) | [E] K11 |
| Talk flips right answers to wrong | A lone correct agent facing a wrong majority recovers 3.6% to 34.4%; inside a correct majority stays correct over 97% | Wynn 2025; Wu 2025 (a22, c15) | [E] K12 |
| Interaction homogenises | Pairwise distance 0.315 to 0.229 after one round; Debate -0.078 diverse vs +0.012 same-model; diversity effect +0.188 [0.073, 0.299] but +0.014 without the Erdos task | Ann et al 2026 (c01-c03) | [S] K13 |
| Dense graphs spread planted errors; sparse pass planted truth less | Error spread cut up to 19% Full to Chain; correct uptake up 10.5% Chain to Full | Shen et al 2025 (a20) | [E] K14 |
| Dense LLM networks converge faster, risk wrong-but-sure cascades | Qualitative (the 0.70 vs 0.75 figure is unverified) | Han et al 2026 (a21) | [C] K15 |
| LLMs under-report failures | Negatives disclosed 35-53% (Qwen), 69-84% (GPT); excess critical degree vs report rate r = -0.91; forced reporting brings d_c to 6.2-6.9 vs theory 6.10 | Zheng et al 2026 (c04, d14) | [C] K15 |
| Topology rank is task-dependent | Random topologies about 51.92% less time than mesh; chain best for software, tree for creative writing | MacNet (b22) | [E] K16 |
| Fresh-peer random routing is a strong baseline | Ring 90.67% at 35.99k tokens vs random no-duplicate 92.67% at 8.04k | Wang et al 2026 (c08) | [E] K16 |
| Teams fall below their best member | HLE best individual 29.0%, team 28.0%, expert revealed 36.0%; synergy gap 6.3% (MMLU Pro), 14.4%, 18.1%, 41.1% (HLE), 20.3% (MATH-500) | Pappu et al 2026 (c09, c17) | [E] K18 |
| Independent sampling scales without talk | GSM8K +12 to +24; MATH +6 to +10; MMLU +5 to +11; HumanEval +4 to +9; plateau near 8 agents in MacNet | Li 2024 Agent Forest (c12); MacNet (b23) | [E] K19 |
| Equal tokens: single agent holds up | 100 tokens: single 0.290, debate 0.370, sequential 0.364, ensemble 0.280. 500 tokens: single 0.390, debate 0.380, sequential 0.376, ensemble 0.310 | Tran and Kiela 2026 (c10) | [E] K20 |
| Effort and low temperature herd | Unique literals tested 25.5 to 11.3 (TCAS), 14.2 to 8.8 (physics); coupling 0.221 to 0.468-0.489 (gpt-5-mini) | Zheng; Hirota (b29, c05, d15) | [C] K21 |
| Samples are alike even at high temperature | Within-prompt similarity typically above 0.8 at T=1; 81% of pairs above 0.7 at T=2 with min-p | Jiang et al 2025 (d16) | [S] |
| Chains pass errors on | Error amplification chain 2094 vs mesh 1241 vs star 1184 (100 trials, Qwen2.5-7B) | Parks and Alharthi 2026 (c18) | [C] K22 |
| Unchecked independent runs amplify errors | 17.2x vs 4.4x with a central validator; negative returns above about 45% single-agent accuracy (beta -0.236, p=0.004) | Kim et al 2025 (d13) | [S] K30 |
| A single LLM under-explores a bandit | GPT-4, K=5, gap 0.2: suffix failure in over 60% of replicates | Krishnamurthy et al 2024 (d07) | [S] K26 |
| Easy items favour revision, hard items parallel | MATH, PaLM 2-S* reviser; interior optimum on hard questions; revision up to 4x less compute than best-of-N | Snell et al 2024 (d08, d09) | [S] K27 |
| Self-repair without a check does not beat fresh samples | Self-correction CommonSenseQA 75.8 to 38.1; GSM8K 75.9 to 74.7; self-consistency 76.7 / 82.5 / 85.3 / 88.2 for 1 / 3 / 6 / 9 | Olausson; Huang (d10, d11) | [C] K28 |
| Refinement beats a long chain at matched sequential tokens | AIME 2024 o3-mini: long CoT 76.9, refinement 81.5, parallel-distill-refine 86.7 | Madaan et al 2025 (d12) | [S] |
| Anchoring on wrong candidates | Admitting only incorrect candidates to the workspace causes large drops, larger for o3-mini | Madaan (d12) | [S] K29 |
| Voting plateaus; a verifier does not | MATH, Llama-3-8B: coverage 82.9% to 98.44% (100 to 10,000 samples), vote 40.50% to 41.41%; SWE-bench Lite 15.9% to 56% with a perfect verifier | Brown et al 2024 (d19) | [E] K31 |
| Confidence-weighted vote saves samples | 41% fewer at budget 5; 46% at 10 | Taubenfeld 2025 CISC (d18) | [E] K31 |
| Multi-agent failures are mostly misalignment | 14 failure modes, annotator kappa 0.88 | Cemri et al 2025 (b30) | [S] K23 |

## 4. Mechanisms and models

### 4.1 Bala-Goyal / Zollman bandit (implementable)
- World: action A1 pays with probability pA (0.5). Action A2 pays with probability pB (0.501, better). Agents do not know pB.
- Each agent holds a belief that A2 is better (Zollman: prior uniform on the interior; the agent believes pB is 0.499 or 0.501).
- Each round an agent plays the action it currently thinks best. A2 players run n trials (n=1000 in Zollman) and see the success count.
- Every agent updates by Bayes on its own results and those of its graph neighbours.
- Stop when all play A1, or all believe state 2 with p > 0.9999.
- Output per network: share of runs ending on the better action (reliability) and mean rounds (speed). Use 10,000 runs per network. Graphs: cycle, wheel, complete, plus all graphs of size 3-6 for regressions.

### 4.2 Why density hurts (the inertia mechanism)
- A bad run of luck makes a few A2 players look bad.
- In a dense graph everyone sees the same bad data at once. Many switch to A1 together (about 4x more switchers). The pool of A2 testers can fall to zero, and then nobody produces new A2 data. The error is absorbing.
- In a sparse graph, agents far from the bad data keep testing A2. Their good data later pulls the others back.
- Worked example (a02): four agents each have a negative result with likelihood 0.4 if A2 is better and 0.6 if not. Pooled posteriors are 0.18, 0.30, 0.32 and 0.46. All fall below 0.5, so no one tries A2. This misleading outcome has probability 0.16.
- Containment is about density, not hubs: removing the hub (cycle versus wheel) helps, and degree variance does not predict success.

### 4.3 Why the effect is fragile
- Signal gap: if pB is clearly better (gap 0.025 or more) a bad round rarely misleads. The sparse advantage drops to 0.
- Trials per round: with many trials each agent's own data is already informative, so sharing matters less (a05, b05).
- Group size: strongest at 6-20 agents. At 100, the complete graph is right 99.12% of the time.
- Time cost: the speed gap is huge (20 vs 1,977 rounds). A time-limited group may prefer dense.
- Exploration: with epsilon-greedy agents (eps 0.35) the dense network wins, because random exploration restores the diversity sparsity would give.

### 4.4 Landscape search with copying rules (Barkoczi and Galesic)
- 100 agents on a rugged NK landscape (N=15), 200 steps, 10 network shapes.
- Each step an agent samples s=3 contacts, then (a) copies the best-scoring one if better than its own (best-member), or (b) copies the majority option (conformity). Otherwise it explores locally.
- Best-member copying drives everyone to one local optimum, so slow networks (long path length) delay that and win.
- Conformity converges slowly and to several solutions, so fast networks win.
- To implement: set diameter via the graph; log final mean payoff; correlate with diameter.

### 4.5 Conformity extension (Weatherall and O'Connor)
- Add a penalty k when an agent's belief differs from its neighbours'. At k=0.1 on random graphs of 10 with pB=0.55, n=5, edge probability 0.5: consensus appears in only about 16% of runs, correct 55%, incorrect 44%.
- Stable polarisation needs clique-like subgroups. Cycle, wheel and complete graphs cannot hold it.

### 4.6 Phase-transition view for LLM search (Zheng et al 2026)
- Collective search is an absorbing-state process. Each agent proposes candidates and reports verdicts to neighbours. When all candidates are tested or dead, the process stops.
- There is a critical degree d_c. Theory gives 6.10 (synthetic), 10.90 (TCAS), 6.10 (physics). Deterministic agents match theory (Lin's CCC 0.93, 0.97, 0.94).
- LLMs need more links. Qwen3.5-4B synthetic: Team-Auto 6.55, Team-Free 12.82, Individual-Free 13.47. The cause is under-reporting of failures. Sending every verdict automatically brings d_c back to 6.2-6.9.
- Higher reasoning effort raises d_c: agents test fewer unique candidates (herding).

### 4.7 Engineering recipe
1. Generate K attempts with no visibility of each other (fresh context).
2. Optionally allow one bounded merge round where each attempt sees at most 2 neighbours' final results, deduplicated and verifier-checked (Li 2024; Madaan 2025).
3. Select by a verifier or confidence-weighted vote, not by averaging views (Brown 2024; Taubenfeld 2025; Pappu 2026).
4. If sharing is used, force failed-attempt reports into the channel (Zheng 2026).
5. Measure diversity (mean pairwise distance) before and after any sharing step (Ann 2026).

## 5. What holds up

**Replications.**
- Sparse-is-more-reliable replicates in its original corner (Rosenstock 2017: 99.12% vs 100%, with 20 vs 1,977 rounds). [E]
- It does not generalise: gone for pB >= 0.525, small elsewhere. Rosenstock wins on generality; Zollman wins in the hard regime.
- Zollman 2010's claim that the ordering "remains the same" holds only at hard parameters.

**Failed or mixed replications.**
- Humans: Mason and Watts found efficient networks better (beta -4.63). Derex and Boyd found partial connectivity better, but only with temporary isolation (first 36 of 72 trials). No clean human replication of the Zollman bandit effect exists.
- Reversal: Kummerfeld-Zollman (eps 0.35, complete wins) itself shrinks under wider parameters.
- LLMs: Li 2024 (sparse equal or better) agrees in direction. Han 2026 (denser converges faster) and Zheng 2026 (LLMs need more links than theory) pull the other way.

**Meta-analyses and large audits.**
- Zhang 2025 (36 configs): fancy debate beats CoT in about 15% of cases.
- Choi 2025: debate is a martingale; voting explains most gains.
- Tran and Kiela 2026: at 500 thinking tokens single agent 0.390 vs debate 0.380.
- Pappu 2026: teams lose to their best member by 6.3% to 41.1% relative.

**Moderators.**
- Signal gap (indirect, K32 contested): easy items favour revision, hard items parallel (Snell); no gain where a single agent already exceeds about 45% (Kim); little herding where the clue is obvious (Zheng).
- Copying rule: best-member copying wants slow networks; conformity wants fast ones (Barkoczi).
- Exploration level: low exploration wants sparse; high wants dense (Kummerfeld-Zollman).
- Model heterogeneity: helps debate and ensembles (Zhang: Heter-SoM +6.4%, Heter-EoT +8.2%) but hurts naive full-solution talk (Ann: Debate -0.078). [C]
- Reasoning effort: more effort, less diversity (Zheng, Hirota).
- Threat model: biased or adversarial agents favour connected networks (Holman and Bruner 2015, not opened).

**Interventions that worked.**
- Neighbour-only visibility and edge pruning: cost down 41-73% with equal or better accuracy (Li; AgentPrune).
- Independent proposers plus a selector (MoA stays positive in Ann: +0.012 same, +0.016 diverse).
- Forced reporting of negative results (Zheng).
- Confidence-weighted vote (CISC) and real verifiers (Brown).
- Temporary isolation then merge (Derex and Boyd, humans; Madaan parallel-distill-refine, LLMs: 76.9 / 81.5 / 86.7).
- A strong model at the hub in a mixed group: 67.0 vs 64.0 self-consistency (Li 2024, b21).
- Majority-consensus stopping beat consistent-output stopping by 4.01% to 7.56% on AQuA (Yin 2023, b27).

**Interventions that did not work.**
- Free-form debate between same-model agents without a check (Choi, Zhang, Wang, Tran and Kiela).
- Intrinsic self-correction: CommonSenseQA 75.8 to 38.1 (Huang).
- Majority vote past about 8 agents (MacNet: +0.9% only) and past about 100 samples on MATH (Brown).
- Averaging views in teams (Pappu).
- Reversing edge direction (MacNet).
- Learned topology over random fresh-peer routing (Wang 2026).
- Higher temperature as a diversity fix: samples stay alike (Jiang).

## 6. Language models

No study runs the real Bala-Goyal bandit with independent versus shared LLM agents (GAP 1, open). What exists is indirect.

**Debate and accuracy.** Du et al 2023 (gpt-3.5-turbo) reported debate gains: arithmetic single 67.0, reflection 72.1, debate 81.8; GSM8K 77.0, 75.0, 85.0; chess pawn-score 91.4, 102.1, 122.9 (a24). The majority-vote cells of that table (69.0, 81.0) were not verified. Later work cut this down: majority vote is on par (Choi), fancy debate beats CoT in about 15% of cases (Zhang), single agent equals or beats multi-agent at matched thinking tokens (Tran and Kiela), and a single strong agent matches workflows across seven benchmarks (Xu 2026).

**Topology.**
- Sparse versus full (Li 2024): GPT-3.5 MATH sparse +3.0 to +7.5 over self-consistency vs full +4.0; GSM8K +3.5 to +6.5 vs +4.5. MathVista (GPT-4o) best sparse +1.2 over full. Helpfulness: full +1.5 (GPT-3.5), +2.9 (Mistral 7B); sparse adds 0.5-1.5 more; cost down 50.0% and 53.3%.
- Mechanism (b20): wrong neighbours mislead; sparse debates last more rounds before all agree; once all agree almost none changes.
- Planted-error spread (Shen 2025, GPT-3.5, MMLU, six role agents, 500 items each way): Full to Chain cuts wrong-answer spread up to 19%; Chain to Full raises correct uptake 10.5%.
- Random re-sampled peers (Wang 2026): 92.67% at 8.04k tokens vs ring 90.67% at 35.99k.
- Task dependence: no topology wins everywhere (MacNet; Wang 2025).

**Failure of communication.**
- Wynn 2025: accuracy often falls over debate rounds on MMLU and CSQA; flips to wrong peak when an agent is alone.
- Wu 2025: a lone agent facing a wrong majority corrects 34.4% (gemini-2.5-flash), 30.0% (gpt-5-mini), 3.6% (gemini-2.5-flash-lite).
- Weng 2025: independence rate 19.6% (Qwen2-7B) to 57.6% (72B); Llama-3.1-405B 56.1%. A smaller majority helps more than fewer prior rounds (69.9% to 32.6% vs to 62.7%).
- Becker 2026: a relevant false passage costs a single agent 0.12-0.43 accuracy; interaction recovers up to 0.24 over voting.
- Ann 2026 (Claude Sonnet 4, GPT-4o, Gemini 2.5 Flash; 11 verifier-scored tasks, 5 seeds): interaction shrinks diversity; no protocol beat the best single-agent baseline in aggregate. Knapsack feasibility under Debate: 10/10 diverse vs 2/10 same; 3AP-Free: 0/10 diverse vs 6/10 same. The sign flips by task.

**Herding with strong reasoning models.**
- Zheng 2026: higher effort cuts unique candidates; low temperature (0.2 vs 1) hurt communication gains mostly where the clue is not obvious.
- Hirota 2026 (340 trials): gpt-5-mini coupling 0.221 to 0.468-0.489 with higher effort; all 20 higher-effort trials twisted; every rewired panel synchronised, matched rings stayed heterogeneous.
- Jiang 2025: within-prompt similarity above 0.8 at T=1.

**Single-agent exploration.** Krishnamurthy 2024: GPT-4 with a basic prompt never retried the best arm late in over 60% of runs (K=5, gap 0.2). Only chain-of-thought with an externally summarised history worked. This is the Zollman failure inside one head. It argues for restarts and external history.

**What changed results, by how much.**
- Sparse visibility: cost -41.5% to -73%, accuracy equal or +1 to +7.
- Heterogeneous models: +6.4% to +8.2% over the homogeneous debate average (Zhang), but negative cells down to -10.8%.
- Forced failure reporting: critical degree from 7-16 down to 6.2-6.9.
- Verifier: coverage 98.44% converted, against a vote plateau of 41.41%.
- Confidence weighting: 41-46% fewer samples.
- Validator in a multi-agent run: error amplification 17.2x down to 4.4x.

**Caveats.** Many studies use GPT-3.5 or 7B-8B models, 100-500 items, 3-5 seeds. Strong reasoning models herd more. Network models count rounds; our agent pays tokens, and only Tran and Kiela, Choi and Ann match tokens. Several 2026 preprints draw large effects from few tasks (Ann's diversity effect needs the Erdos task).

## 7. What our agent should take

### Add now (established)
- **G4/S3: Make attempts fresh and isolated by default.** Each independent attempt starts in clean context and does not see other attempts' reasoning. [E]. Evidence: K10, K11, K12, K14, K20; a19, a22, a23, a20, c10, c15.
- **G4 / O-vote: Beat debate with independent samples plus a vote or checker.** Any sharing step must beat "N independent samples + vote" and "one long attempt" at equal tokens. [E]. K11, K20; a23, b25, c10.
- **S3 visibility: if attempts do share, keep it sparse.** At most 2 neighbours or a checked, deduplicated summary; never everyone's full transcript. [E]. K10, K14, K16; b19, c06, b24, c08.
- **G4: Do not let a lone correct answer be overruled by headcount.** Weight by evidence or check. [E]. K12, K18; c15, a22, c09.
- **O-aggregate: Select by verifier when one exists; else confidence-weighted vote; do not average.** [E]. K18, K31; d19, d18, c09.
- **S3 budget: Do not tune topology.** Default to no visibility or random few-peer visibility. [E]. K16; b22, c08.
- **Memory/trace: Log the vote plateau.** Stop adding independent attempts at the measured plateau (MacNet about 8; plain vote on MATH about 100). [E]. K19, K31; b23, d19.
- **G4/G12: Skip extra attempts on easy items** where single-agent accuracy is already high (about 45% ceiling in Kim). Number is [S]; direction consistent with G12 spend-by-difficulty. K30; d13.

### Test first
- **Isolate, then one bounded merge** (S3/merge). [S]/[C]. K24, K28, K29; d05, d12. Risk: anchoring on wrong drafts.
- **Forced reporting of failed attempts into any shared channel** (S3/O-share-negatives). [C]. K15; c04, d14. Token cost unknown.
- **Route by first-sample agreement** (S3/O-revise): high agreement, revise once; low, fresh attempts. [S]. K27; d08.
- **Diversity monitor**: pairwise distance before and after sharing. [S]. K13; c01-c03.
- **Prompt or persona diversity** across attempts. [C]. K17; b25, c02. G4 already bans persona voters on single-answer problems; test only for generation breadth.
- **Effort and temperature versus diversity** (G4/temperature). [C]. K21; b29, d15, d16.
- **Restarts versus one long run** on a bandit-like hidden-rule task. [S]. K26; d07.
- **Hardness scaling of the isolation benefit.** [C]. K32; d08, d10, d13, d15.

## 8. Concrete tests on our bench

All arms get the same total token budget. Report accuracy per token, not per round. Paired design on the same items. At least 3 seeds.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| T1 Isolation vs sharing | Mixed-difficulty reasoning items with exact answers | (a) N independent attempts + vote or verifier; (b) N attempts each seeing all earlier answers; (c) one long attempt | Accuracy; correct-to-wrong flips | (a) >= (b) by 2+ points on hard items; (b) has more flips |
| T2 Visibility breadth | Same | Revision round with no peers, 2 neighbours, all peers | Accuracy, tokens | 2 neighbours >= all peers at about 40% fewer tokens |
| T3 Planted error | Items with one planted wrong or right sketch | Seen under full vs 2-neighbour vs none | Spread of planted error; uptake of planted truth | Error spread falls with sparsity; truth uptake falls too |
| T4 Hardness split | Same benchmark binned by single-agent pass rate | Independent vs shared by bin | Gap by bin | Isolation advantage grows with hardness; zero on easy bin |
| T5 Isolate then merge | Items with checkable partial results | (a) independent then one merge over checked, deduplicated results; (b) shared from start; (c) independent + vote | Accuracy | (a) >= (c) when a verifier exists; (a) > (b) |
| T6 Forced failure reports | Search tasks with many dead ends (hidden rule) | Shared channel with free reports vs forced failure reports vs none | Candidates tested, duplicates, accuracy, tokens | Forced reports cut duplicates; net gain only if token cost is below saved tests |
| T7 Diversity vs effort | Open-ended and single-answer items | Low vs high effort; T 0.2 vs 1.0; with and without a prompt-variation list | Mean pairwise distance, unique candidates, accuracy | Higher effort lowers diversity; prompt variation raises it |
| T8 Restarts | Small bandit or hidden-rule game | N fresh restarts vs one long run vs one run with external summary | Late best-arm pull rate | Restarts and summaries fix suffix failure |
| T9 Selection rule | Items with a checker and items without | Average vs majority vs confidence-weighted vs verifier | Accuracy at fixed N | Verifier > confidence-weighted > vote > average |
| T10 Plateau | Own tasks | N = 1, 2, 4, 8, 16, 32 independent | Accuracy curve | Plain vote plateaus near 8; coverage keeps rising |
| T11 Anchoring | Merge step | Merge seeing wrong-heavy vs right-heavy drafts, with and without a filter | Accuracy drop | Large drop when wrong drafts dominate and there is no filter |

## 9. What does not transfer, and why

- **Bandit payoffs are noisy coin flips; our items often are not.** The effect needs a nearly undetectable better option. Many of our items have deterministic answers and checkers. Rosenstock: the effect is zero when the gap is 0.025 or more.
- **Model agents hold separate data; our attempts share one model and its priors.** Samples are correlated (Jiang: similarity above 0.8 at T=1), so isolation gives less diversity than the model assumes (G4).
- **Rounds versus tokens.** The sparse net's cost is rounds (1,977 vs 20). We pay tokens. Token-matched results (Tran and Kiela, Choi) favour doing less.
- **Absorbing lock-in needs agents who stop experimenting.** A scaffold can force exploration or restart. The Kummerfeld-Zollman case shows exploration removes the effect.
- **Group size.** Strongest at 6-20 agents; our budgets usually allow 3-8 attempts.
- **Human motives.** Conformity and reputation costs (Weatherall and O'Connor's k) do not apply to one model, though sycophantic conformity does appear in LLMs (Weng 2025).
- **Network formation, trust, funding and credit.** Parts of the literature model these. Our scaffold has none.
- **Single-model exploration failure is a separate problem.** GPT-4's suffix failure (Krishnamurthy) is not a network effect. Restarts and external summaries address it.

## 10. Open questions

1. Does a Zollman-style effect appear in LLM agents on a real two-armed bandit, independent versus shared, at equal tokens? (GAP 1)
2. Does the isolation benefit scale with the signal gap for LLMs? (GAP 2; only indirect support)
3. For one agent, fresh attempt versus revision at equal tokens, per task type, for current reasoning models. (GAP 3)
4. What does forced sharing of negative results cost in tokens, and is the net positive? (GAP 4)
5. Does prompt or persona variation restore diversity on reasoning tasks? (GAP 5)
6. Exact numbers from Mayo-Wilson, Zollman, Danks 2011/2013, Lazer and Friedman 2007 and Holman and Bruner 2015 (not opened). (GAP 6)
7. Does the Kummerfeld-Zollman reversal appear for LLMs at high temperature? (GAP 7)
8. Does a verifier or confidence weighting avoid expert dilution better than averaging, at equal tokens? (GAP 8)
9. Where is the break-even between independent voting and one limited-visibility revision round? (GAP 9)
10. Do 2026 reasoning models behave like the GPT-3.5 and 7B-8B models that dominate the debate literature?
11. Rosenstock 2017 could not be re-opened; the fragility numbers (K03) rest on one paper.

## 11. Sources

[V] opened and read; [M] snippet or abstract only.

- [V] Zollman (2007) The Communication Structure of Epistemic Communities, Phil Sci 74:574-587. https://eudora.phl.univie.ac.at/hyperkitty/list/iris@lists.philo.at/message/BHDXWQQN47IWXURJ2EUNK54O63EYMLTL/attachment/4/zollman_communication_structure.pdf
- [V] Zollman (2025) Beliefs and Social Networks, Oxford Handbook of Belief. https://philsci-archive.pitt.edu/25858/
- [V] Rosenstock, Bruner, O'Connor (2017) In Epistemic Networks, Is Less Really More? https://cailinoconnor.com/wp-content/uploads/2015/03/In_Epistemic_Networks_Is_Less_Really_More.pdf (link later dead; not re-opened in cross-check)
- [V] Barkoczi, Galesic (2016) Social learning strategies modify the effect of network structure. https://www.nature.com/articles/ncomms13109
- [V] Weatherall, O'Connor (2020) Conformity in Scientific Networks. https://arxiv.org/abs/1803.09905
- [V] Bala, Goyal (1998) Learning from Neighbours (1996 working-paper version). https://repub.eur.nl/pub/1362/eeb19960111120062.pdf
- [V] Mason, Watts (2012) Collaborative learning in networks, PNAS. https://pmc.ncbi.nlm.nih.gov/articles/PMC3271930/
- [V] Derex, Boyd (2016) Partial connectivity increases cultural accumulation. https://pmc.ncbi.nlm.nih.gov/articles/PMC4801235/
- [V] Becker, Brackbill, Centola (2017) Network dynamics of social influence in the wisdom of crowds. https://pmc.ncbi.nlm.nih.gov/articles/PMC5495222/
- [M] Mayo-Wilson, Zollman, Danks (2011) The Independence Thesis. https://philarchive.org/rec/MAYTIT
- [M] Lazer, Friedman (2007) The network structure of exploration and exploitation. https://doi.org/10.2189/asqu.52.4.667
- [M] Holman, Bruner (2015); Grim (2009); Kummerfeld, Zollman (2016), as cited by Rosenstock et al
- [V] Du et al (2023) Improving Factuality and Reasoning through Multiagent Debate. https://arxiv.org/abs/2305.14325
- [V] Li et al (2024) Improving Multi-Agent Debate with Sparse Communication Topology. https://arxiv.org/abs/2406.11776
- [V] Li et al (2024) More Agents Is All You Need. https://arxiv.org/abs/2402.05120
- [V] Qian et al (2025) MacNet. https://arxiv.org/abs/2406.07155
- [V] Zhang et al (2024) AgentPrune. https://arxiv.org/abs/2410.02506
- [V] Zhang et al (2025) Stop Overvaluing Multi-Agent Debate. https://arxiv.org/abs/2502.08788
- [V] Wang et al (2024) Rethinking the bounds of LLM reasoning. https://arxiv.org/abs/2402.18272
- [V] Yin et al (2023) Exchange-of-Thought. https://arxiv.org/abs/2312.01823
- [V] Choi, Zhu, Li (2025) Debate or Vote. https://arxiv.org/abs/2508.17536
- [V] Smit et al (2024) Should We Be Going MAD? https://arxiv.org/abs/2311.17371 (abstract and introduction only)
- [V] Shen et al (2025) Information propagation effects of communication topologies. https://aclanthology.org/2025.emnlp-main.623.pdf
- [V] Han et al (2026) Conformity Dynamics in LLM Multi-Agent Systems. https://arxiv.org/pdf/2601.05606
- [V] Wynn, Satija, Hadfield (2025) Talk Isn't Always Cheap. https://arxiv.org/pdf/2509.05396
- [V] Wu, Li, Li (2025) Can LLM Agents Really Debate? https://arxiv.org/abs/2511.07784
- [V] Weng, Chen, Wang (2025) Conformity of LLMs (BenchForm). https://arxiv.org/abs/2501.13381
- [V] Becker et al (2026) Misinformation Propagation in Benign Multi-Agent Systems. https://arxiv.org/abs/2606.16710
- [V] Ann, Liu, Tan (2026) The Interaction Tax. https://arxiv.org/abs/2608.23541
- [V] Zheng et al (2026) Absorbing state phase transitions in multi-agent search. https://arxiv.org/abs/2609.38327
- [V] Hirota et al (2026) Collective Regimes in Multi-Agent LLMs. https://arxiv.org/abs/2609.35885
- [V] Wang et al (2025) Multi-agent intelligence through small-world networks. https://arxiv.org/abs/2512.18094
- [V] Wang et al (2026) Do We Need Complex Topology Control? https://arxiv.org/abs/2609.27150
- [V] Pappu et al (2026) Multi-Agent Teams Hold Experts Back. https://arxiv.org/abs/2602.01011
- [V] Tran, Kiela (2026) Single-Agent LLMs Outperform Multi-Agent Systems. https://arxiv.org/abs/2604.02460
- [V] Xu et al (2026) Rethinking the Value of Multi-Agent Workflow. https://arxiv.org/abs/2601.12307
- [V] Parks, Alharthi (2026) Predictive Maps of Multi-Agent Reasoning. https://arxiv.org/abs/2605.11453
- [V] Cemri et al (2025) Why do multi-agent LLM systems fail? https://arxiv.org/abs/2503.13657
- [V] Krishnamurthy et al (2024) Can LLMs explore in-context? https://arxiv.org/abs/2403.15371
- [V] Snell et al (2024) Scaling LLM test-time compute optimally. https://arxiv.org/abs/2408.03314
- [V] Olausson et al (2023) Is self-repair a silver bullet for code generation? https://arxiv.org/abs/2306.09896
- [V] Huang et al (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798
- [V] Madaan et al (2025) Rethinking thinking tokens. https://arxiv.org/abs/2510.01123
- [V] Kim et al (2025) Towards a science of scaling agent systems. https://arxiv.org/abs/2512.08296
- [V] Jiang et al (2025) Artificial Hivemind. https://arxiv.org/abs/2510.22954
- [V] Zhang et al (2025) Verbalized Sampling. https://arxiv.org/abs/2510.01171
- [V] Taubenfeld et al (2025) Confidence improves self-consistency (CISC). https://arxiv.org/abs/2502.06233
- [V] Brown et al (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787
- [M] Bala and Goyal 1998, journal version. https://doi.org/10.1111/1467-937X.00059
- [M] Wang et al (2024) Mixture-of-Agents. https://arxiv.org/abs/2406.04692
- [M] Romera-Paredes et al (2024) FunSearch. https://www.nature.com/articles/s41586-023-06924-6
- [M] Hagag et al (2026) Architecture matters for multi-agent security. https://arxiv.org/abs/2604.23459

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 10 established claims: 10 confirmed as written, 0 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **F03.04-K01** (now single-source: only one opened source, code check).
- **F03.04-K07** (now single-source: only one opened source, code check).
