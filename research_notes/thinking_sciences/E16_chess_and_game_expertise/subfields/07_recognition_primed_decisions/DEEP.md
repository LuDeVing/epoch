# Recognition-primed decisions: deep document

*Subfield E16.07. Written 2026-11-01 from evidence_a-d.jsonl (a01-a27, b01-b26, c01-c25, d01-d27), claims.jsonl (K01-K23) and critique.md. Evidence ids in brackets. Numbers were re-checked against the sources in critique.md; where a number could not be re-checked, the text says so.*

## 1. What it is

Recognition-primed decision making (RPD) is a model of how experts choose in real settings. It was built by Gary Klein and colleagues from interviews with fireground commanders. The claim: an expert does not list options and compare them. The expert sees the situation, recognises it as a typical case, and a typical action comes to mind. The expert checks that action by imagining it play out. If it works, the expert does it. If not, the expert changes it or takes the next one. [a01, a04, a19]

Three variants are described [a04]:

- **V1, simple match.** Situation known, action known. An if-then.
- **V2, diagnose.** The situation is unclear. The expert builds a diagnosis, then acts.
- **V3, simulate.** The situation is understood but the response is not. The expert mentally runs candidate actions one at a time and stops at the first that seems to work.

A pattern in memory holds four things: cues, expectancies, plausible goals, and typical actions [a19]. Klein says the model has two parts: fast pattern matching and slower mental simulation. He equates them with Kahneman's System 1 and System 2. He says RPD is not limited to time pressure [a06].

The subfield row in SUBFIELDS.md lists chess players among groups that use the first workable option, says it needs experience, and says it fails in unusual situations. That row comes from the Wikipedia RPD page, which has a needs-more-citations tag and a single source (Klein 1998). It carries no evidential weight [a04, b23]. This document tests the claim properly.

Why it matters for our agent: the schema has a mode choice at S0 (direct, short reason, checked, open) and a rule at G11/G12 about spending by difficulty. RPD is the human version of "answer fast when the case is familiar, deliberate when it is not". The questions are: how often is fast enough, what tells you it is not, and does an LLM benefit from RPD-style prompting.

**Bottom line up front.**

1. The founding numbers (under 12% option comparison, over 80% direct recognition) come from one retrospective interview study and have no independent replication outside RPD's own coding [a01, K23].
2. In chess, fast pattern knowledge explains most of skill, but time pressure still hurts elite players and extra thinking helps on hard positions. RPD alone does not describe expert chess [b01, b07, a08].
3. Fast pattern policies can be very strong (a 270M transformer without search reaches tournament Elo 2299), yet a little search adds a lot [b13, b14, c04].
4. The only direct LLM test of an RPD prompt gave +4.3 points on one task, with no proof that the simulation step matters [a13, d23].
5. The practical lesson for a scaffold is the switch signal: agreement across short attempts is the best-tested trigger for leaving the cheap mode [d20, d21, d22].

## 2. History and theories in depth

### 2.1 Origins

- **1985 fireground study.** Klein, Calderwood and Clinton-Cirocco interviewed experienced fireground commanders about non-routine incidents. The work began as an attempt to confirm classical decision theory (generate options, weigh, choose). It found little option comparison. The first report was a technical report; the short paper is Klein et al. (1986), Proc. Human Factors Society 30, 576-580 (not opened; DTIC report ADA199492) [a02]. The full study with a postscript was published in 2010 [a01].
- **Numbers.** 26 commanders, mean 23 years of experience, 156 decision points probed. Under 12% showed simultaneous comparison of two or more options. Over 80% used direct recognition of situation and action. Checked from the 2010 abstract only [a01].
- **Number drift.** Later retellings say RPD "accounted for 80-90% of decisions" [a20]. The original says "over 80%". The figure inflates with each retelling.

### 2.2 Naturalistic decision making (NDM)

NDM grew out of a 1989 conference in Dayton, Ohio and the book Klein, Orasanu, Calderwood and Zsambok (1993), *Decision Making in Action* [a03, a05]. It studies expert decisions in real settings: time pressure, high stakes, ill-defined goals. Klein (2008) is the founder's own account [a03]. RPD is NDM's flagship model.

### 2.3 Rival views

- **Classical decision theory.** Generate options, rate them, choose the best. RPD was a reaction to this.
- **Heuristics and biases (Kahneman).** Intuition is often wrong. In 2009 Kahneman and Klein wrote a joint paper, "Conditions for intuitive expertise: a failure to disagree". They agree that intuition can be trusted when (1) the environment is regular enough to be predictable and (2) the person had a real chance to learn it. Felt confidence is not a guide to accuracy [a07, b22]. This is the best boundary statement for RPD.
- **Fast-and-frugal heuristics (Gigerenzer, Raab).** The formal cousin is "take the first" (TTF): options come to mind in order of learned validity, search stops at the first feasible one. TTF predicts that more options generated means lower quality. The long-term working memory view predicts the opposite [a21]. Another subfield of this run covers fast and frugal heuristics in depth; here only the RPD link is noted.
- **Search-based models of chess (de Groot, Chase and Simon).** Chess skill comes from large stores of chunks (pattern recognition) plus search. See the parallel subfields "Chunking and templates" and "Pattern-recognition theory of search".
- **Dreyfus.** Experts grasp a situation as a whole, without parts. Chassy et al. say their complexity effect contradicts this (error rose with piece count) [a08].

### 2.4 Klein's own defence

Klein (2021) answers six criticisms [a06]. Key points:

- RPD is falsifiable. Inexperienced people use the RPD tactic "less than half the time" (no N given).
- In chess, Klein et al. (1995) found skilled players' first-generated option was of high quality, which random first options would not be (paper not opened; Klein's summary only) [a12].
- The work was "replicated several times" (not itemised, so it cannot be checked) [a06].
- RPD is easy to model only if mental simulation is ignored. Reinforcement-learning models learn from reward, while people also diagnose what went wrong and build stronger mental models [a25].

### 2.5 Extensions

- **Crossword solving.** Thanasuan and Mueller (2014) built a computational model of expert crossword solving on recognitional decision making. Fast, fluent retrieval explained experts. Error correction and backtracking mattered less. They say classic RPD needs amending for domains with exact answers: the decision becomes "do I know it?" and how to continue search [a14].
- **Fuzzy-logic RPD model** (Ji et al. 2007): named only, not opened [a24].
- **Sport.** Many applications; see sections 3 and 5 [a15, a16].
- **Medicine and nursing.** Surgeons, pharmacists, ICU nurses, residents; mostly qualitative and coded with RPD's own scheme [a17, a18, d10, d11, d27].
- **Training critique.** Vidulich and Tsang (2026) warn that training by repeated exposure, as RPD suggests, may leave experts unprepared for unfamiliar events. Deliberation needs deep organised knowledge. They cite Sullenberger's Hudson landing as an example of using limited time to deliberate [a26, b24].

## 3. Core findings with exact numbers

Status key: **replicated** = two or more independent sources; **single** = one source; **contested** = sources disagree; **circular** = used RPD's own coding; **second-hand** = number reported by a different paper than the one that produced it.

### 3.1 Founding and cross-domain findings

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Fireground commanders rarely compared options | 26 commanders, mean 23 years, 156 decision points; under 12% comparison; over 80% direct recognition | Klein et al. 1985/2010 [a01] | single, retrospective interviews, authors coded, no control group |
| Sport: most expert decisions are simple matches | 60-81% simple match, 13-28% diagnosis, 3-24% evaluating a course of action | Macquet 2020 via [a15] | circular (RPD coding scheme) |
| Prior sport work: preferred first option chosen in about 80% of decisions | about 80%, uncited | [a15] | unverified |
| Pharmacists used pattern recognition, went analytic on atypical items | N=12, qualitative | Elgebli et al. 2025 [d10, a17] | circular, tiny |
| Residents show premature closure and rule-of-thumb errors | 11 of 23 interviewed; 71 cues; kappa 0.64 | Mansoori et al. 2025 [d11] | circular, recall after days |
| ICU nurses recognised four bleeding types | N=39, no counts | Lavoie et al. 2024 [d27] | circular, qualitative |
| Handball goalkeeper: recognition did not change with distance, micro-decisions did | 83 accounts, 419 feature units, one goalkeeper | Le Menn et al. 2019 [a16] | single case |
| Belief survey: Klein's 11 claims do not form one belief | N=225; two factors explain 29.24% of variance; KMO 0.741 | Mattingsdal 2026 [d26] | measures beliefs, not decisions; not a replication |
| Independent replication of the 80% figure | none found | [K23] | zero sources |

### 3.2 Take-the-first (TTF) in sport and other tasks

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Students used TTF on most basketball video trials; earlier options were better | N=72, 13 trials per task; TTF on 70% of trials | Hepler and Feltz 2012 [d01] | single; abstract only, no effect sizes |
| Acute stress did not change TTF use or quality | N=68, 8 trials per condition | Hepler and Kovacs 2017 [d06] | same first author as d01 |
| Children pick the first option; older children more so | N=73, ages 6-13, four waves | Musculus et al. 2019 [d02] | same network |
| Caffeine cut options and time but not the take-the-first tendency; familiarity made no difference | N=47, 300 mg vs placebo | Haeusser et al. 2014 [d03] | takes-first held in low-familiarity scenarios, which cuts against "needs expertise" |
| Handball videos: TTF replicated across expertise and mood | 30 + 30 + 30 between, 30 within | Laborde and Raab 2013 [d04] | same lab |
| Intuitive handball players faster and better; experts more intuitive | N=54 | Raab and Laborde 2011 [d07] | questionnaire, correlational |
| Knowledge-free option task did not follow TTF | N=44 healthy + 54 depressed; uniqueness fell with option index | Chen et al. 2025 [d05] | boundary case, not a sport or expert sample |
| Scoping review of heuristics in sport | 38 studies; 16 on fast-and-frugal; 8 on TTF | Ramanayaka et al. 2024 [d08] | thin evidence base |
| Johnson and Raab 2003 (handball experts, more options led to worse choices) | not obtained | [a22, b26] | not opened |

### 3.3 Chess

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Five-second evaluation error falls with skill | N=63; mean error 1.58 / 1.52 / 1.39 / 1.17 (candidate masters 2106, masters 2314, internationals 2486, world-class 2691); F(3,59)=14.56 (14.558 in critique), eta squared 0.425; r=0.664 so Elo explains 44% of variance | Chassy et al. 2023 [a08] | single; confirmed in critique |
| Error rose with position complexity | simple 1.31 vs complex 1.50, F(1,59)=34.27 | [a08] | single |
| Response time did not differ by skill | F(3,59)=0.713 | [a08] | single |
| Blitz rank predicts standard rank | 64-81% of variance (19-36% unexplained) | Burns 2004 via [b04, a10] | second-hand |
| Grandmasters blunder more in blitz | 20 GMs; blunder proportion 0.20 to 0.27 (t(19)=6.54, d=1.39); blunder size d=0.96, t(19)=4.23; expected blunder per move d=1.30 | Vidulich and Tsang 2026 [a09, b01] | single paper; the group means (e.g. 0.98 vs 1.45) could not be re-found in the text this pass, and "higher in blitz for 18 of 20" was not found either; t and d confirmed |
| Within long games, time per move and blunder rate move in opposite directions | 11 world championship matches, 7 champions; moves 11-20 over 6 min; last five before time control under 2 min | [b02] | archival, correlational |
| Chabris and Hearst: GMs blunder more in rapid play | GM Elo 2530-2790; blunder size about half a pawn larger in 15-min rapid | via [b06] | second-hand |
| Kasparov in simultaneous play | rating-equivalent 2750 to 2646 | via [b05, a10] | second-hand; read as small by some, large by others |
| Moxley et al.: extra deliberation helps both groups on easy and hard tactics | Elo 2194 vs 1836; first move kept as final only 45% overall, 22% (stronger) and 25% (weaker) on hard positions | Moxley et al. 2012 [b07, b06] | abstract read; 45/22/25 are second-hand |
| Calderwood et al. 1988: masters seemed immune to blitz | 3 class B vs 3 masters; blitz vs 40 moves in 90 min | via [b03, d12] | second-hand, N=6, not opened; contradicted by the larger study |
| Skill predicts results less as time controls shorten | direction only | van Harreveld et al. 2007 [b08] | abstract only; luck is a rival explanation |
| De Groot replication: stronger players search faster | 6 GMs, 5 IMs, 6 experts, 5 class A; 2 positions | Connors et al. 2011 [b09] | abstract only |
| Speed and quality in elite chess | about 80,000 moves, 1,592 games, 54 tournaments, Elo 2500+, Stockfish 14; faster decisions better within player and game; fast = better when the evaluation gap is large | Sunde et al. 2022 [b10, b11, b12] | observational; read as drift-diffusion, not recognition |
| Klein et al. 1995: skilled players' first option was high quality | numbers not obtained | via [a06, a12] | not opened |

### 3.4 Machine analogues of recognition

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Chess transformer with no search | 270M: Lichess blitz Elo 2895 vs humans, 2299 vs bots; tournament Elo 2299; puzzles 95.4%. 136M: 2259, 94.5%. 9M: 2025, 88.9%. Stockfish 16 (50 ms) 2711 | Ruoss et al. 2024 [b13, b14, c01, c02] | single paper |
| Adding search to the same networks | AlphaZero puzzles: policy only 56.1%, value only 82.0%, 400 simulations 95.6%. Leela: 88.6%, 95.9%, 99.6%. Leela Elo 2292 policy only vs 2858 with 400 simulations | [c04, b14] | single paper, computed from Table 1 |
| General chat LLM on PGN is far weaker | GPT-3.5-turbo-instruct 66.5% puzzles, Lichess 1755 vs bots | [c02] | single |
| Blind spot of pure recognition | cannot see threefold repetition (no history); patch sets win estimate of a repetition move to 50% | [b15, c03] | single |
| Language-model chess with search | searchless external Elo 2923 (mean), 2875 (max); +68 internal Elo at 100 simulations; about +290 to +340 at 500-2000 simulations (row pairing inferred) | Schultz et al. 2025 [b16, b18, d13] | single; the paper's "+300 with limited search" is a loose summary |
| Chessformer | policy-only Elo 2347, 93.5% puzzles at 12.8B FLOPS vs 427B for the Ruoss 270M | Monroe and Chalmers 2024 [c11, d14] | the 93.5% for the Ruoss model is Monroe's re-run, not Ruoss's 95.4% |
| Transcendence | model trained on human games beats its best player at low temperature (about 1500 from 1000 and 1300 models; the 1500 model did not) | Zhang et al. 2024 [b19] | abstract level; small models |
| Look-ahead in a policy network | probe predicts best move two turns ahead with 92%; 22.5k puzzles kept from 900k | Jenner et al. 2024 [c05, c25] | filtered set |
| Board and skill representation | probes 99.6% (random-weights baseline 74.7%), skill probe 90.5%; win rate vs Stockfish level 0: 64% (16-layer), 46% (8-layer); skill vector up to 2.6 times | Karvonen 2024 [b20, c06] | one paper |
| Legal-move rate on a modified board | 41% without the intervention, 92.0% (16-layer) and 90.4% (8-layer) with it | [c06] corrected in critique | not an edit-success rate |
| Chess state tracking in LLMs | BigBench chess: LLaMA-7B 29.5%, ChessGPT-Base 99.5%; UCI-to-FEN: 2.2% vs 95.1% | Feng et al. 2023 [c07] | state tracking, not move quality |
| Engines predict humans poorly | best Stockfish at most 46% move match; Maia over 52% (lowest 46% when a 1900 model predicts 1100) | McIlroy-Young et al. 2020 [c08] | tree search on top of Maia lowers match |
| Predicting human blunders | residual CNN 67.7% (board only), 71.7% with more input | [c09] | modest |
| Maia-2 | about 2 points over Maia; perplexity 4.67 to 4.07 bits | [c10] | abstract level |

### 3.5 Boundary of recognition

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Referees: experts equal in both styles, novices better analytic | N=60 (30 + 30). Experts .851 intuitive vs .835 analytic (n.s.); novices .643 vs .690 (p<.05); style x level F(1,58)=20.09; style main effect F(1,58)=5.291, p=.025; overall expert .843 vs novice .666 | [d09] | single; the best measured boundary. Experts were also more overconfident under the intuitive style |
| Novices use RPD "less than half the time" | no N, no source | Klein 2021 [a06] | unsourced |
| Intuition is valid only in regular environments with learning chances | argument | Kahneman and Klein 2009 [a07, b22] | consensus statement |
| Memory agent falls off coverage | DiLu with 40 items: 70% success at home setting, 35% in denser, wider setting (10 scenarios each); RL baseline fell 85% relative | [d15] | three settings, no curve |

## 4. Mechanisms and models

### 4.1 RPD as an algorithm

```
situation <- observe
pattern  <- match(situation, library)        # cues, expectancies, goals, typical actions
if pattern is None:              diagnose (V2): gather cues, build story, retry match
action   <- pattern.typical_actions[0]       # ordered by learned validity
loop:
    outcome <- simulate(action, situation)   # mental simulation, step 3
    if outcome acceptable:  return action
    action <- modify(action) or next typical action
    if no actions left: treat as unfamiliar -> analytic mode
```

Key properties: options are generated one at a time, in order of experience-based validity; the stopping rule is "first that survives a check", not "best of a list". The same structure is TTF [a21].

### 4.2 Take-the-first

Order options by learned validity. Evaluate one. Stop at the first feasible one. It predicts that quality falls as more options are generated [a21]. Evidence for it sits in one research network (see 3.2 and 5.4).

### 4.3 Recognition quality in chess

Chassy et al. show evaluation error falls with skill after only 5 seconds, so a store of chunks gives accurate fast judgement [a08]. Complexity raises the error for everyone. An engineer's reading: fast accuracy is a property of the stored library, and it degrades with the number of pieces or interacting parts, not with the player's speed.

### 4.4 Fast policy plus search (the engine analogue)

- **Policy only:** one forward pass, no search. A 270M transformer imitating Stockfish values reaches tournament Elo 2299 [b13].
- **Policy plus value plus MCTS:** Leela goes from 2292 (policy only) to 2858 with 400 simulations [c04].
- **Language model as policy, value and search:** Elo grows roughly with the log of simulations [b16, b18].
- **Internal search:** the model writes a linearised tree in text and then picks a move. It needs training on search traces; it does not appear from prompting alone [b17].

Implementation reading: the fast policy gives a prior over actions. Search spends compute where the prior is uncertain. Return per doubling falls [b18]. Search helps most where the fast policy is weakest, such as tactical puzzles [c04].

### 4.5 Switching between fast and slow

| System | Trigger | Result |
|---|---|---|
| SwiftSage [c14, c15] | stuck (5 consecutive steps with zero reward), invalid action, critical decision, unexpected observation; returns to fast when plan buffer is empty | 84.7 average on 30 ScienceWorld task types vs SayCan 33.8, ReAct 36.4, Reflexion 45.3 |
| System-1.x [c16] | controller splits into sub-goals, labels each easy or hard; parameter x sets the mix | 70.4% valid plans at 13.6 states vs 48.7% (fast only) and 37.2% (search only); x=0.75 gives 75.7% at 16.6 states. Which of the two tasks was not confirmed |
| Dualformer [c17] | random dropping of trace parts in training; fast, slow or auto mode | 30x30 maze: slow 97.6% optimal; fast 80% vs 30% solution-only; auto 96.6% optimal with 59.9% fewer steps |
| Searchformer [c18] | trained on A* traces | 93.7% of unseen Sokoban solved optimally; up to 26.8% fewer search steps |
| Thinkless [c19] | RL-trained control token short or think | cuts long reasoning 50-90% on Minerva Algebra, MATH-500, GSM8K with accuracy kept |

All of these train the router or use a hand rule. None is an RPD test.

### 4.6 Switch signals that were tested for leaving the cheap mode

| Signal | Result | Source |
|---|---|---|
| Agreement of sampled answers (Dirichlet stopping) | up to 7.9x fewer samples, average 3.3x, accuracy drop under 0.1%; 17 datasets, 3 LLMs | Adaptive-Consistency [d20] |
| Window unanimity | samples cut by MATH 33.8%, GSM8K 80.1%, StrategyQA 76.8%, CommonsenseQA 78.5%, Coin Flip 84.2%, Last Letters 67.4% | ESC [d21] |
| Confidence-weighted voting | over 40% fewer paths; 9 models, 4 datasets | CISC [d22] |
| Stuck counter | used in SwiftSage; not ablated | [c15] |
| Model re-checks its own first answer | harmful (see 5.3) | [d19] |

### 4.7 Case memory as the library

Recognition needs a library of cases. LLM analogues:

- **DiLu:** retrieves similar past scenes and reasons from them. 40 memory items match RL trained over 600,000 episodes in the home setting; success drops 70% to 35% in a harder setting [c22, d15].
- **Voyager:** skill library indexed by description embedding. 3.3 times more unique items, 2.3 times longer distances, milestones up to 15.3 times faster. Gains are for the whole system, not retrieval alone [c23].
- **Reflexion:** verbal reflection carried into the next trial. HumanEval pass@1 91% vs GPT-4 80%. ALFWorld 130 of 134 tasks [c24].

## 5. What holds up

### 5.1 Replications and agreement

- **Established:** fast pattern knowledge accounts for a large share of chess skill (Elo explains 44% of 5-second error variance; blitz rank explains 64-81% of standard rank) [K03].
- **Established:** time pressure hurts even elite players. Three or more sources: Vidulich and Tsang (d=1.39 on blunder proportion), Chabris and Hearst (about half a pawn larger blunders in rapid), Kasparov's simultaneous-play drop (2750 to 2646) [K04].
- **Established but circular:** simple match is the most common coded decision type in sport (60-81%) [K02].
- **Established:** switching signals based on sample agreement save samples at little loss [K21].

### 5.2 Failures, contradictions and weak spots

- **No independent replication of the 80% finding.** Klein says "several times" without citation. Sport and medical studies use RPD's own coding, so they cannot refute it. A military survey (N=225) measures beliefs only [a06, d26, K23].
- **The chess evidence does not test RPD's specific claim** (one option, simulate it, accept if it works). It shows intuition matters and time pressure hurts. The closest tests (Connors 2011, Klein 1995) are thin or unopened [b09, a12].
- **Calderwood 1988 contradicted.** Three class B vs three masters, "masters seemed immune". The large sample of grandmasters shows blitz harms experts too [d12, b01].
- **Number drift.** "Over 80%" became "80-90%" [a01, a20].
- **+68 vs +300 Elo in Schultz et al.** Reconciled with one inference: +68 is at 100 simulations, about +300 at 500-2000. Check the paper figure before citing [d13].
- **93.5% vs 95.4%.** Monroe re-ran the Ruoss model on a different puzzle subset. Keep apart [d14].
- **Engine and transformer evidence is not recognition by experience.** These systems imitate engine labels. The analogy to an LLM scaffold is loose [critique].
- **Wikipedia's chess claim has no real source.** [a04]

### 5.3 What did and did not work as an intervention (LLMs)

| Intervention | Outcome | Source |
|---|---|---|
| RPD-style prompt for care-seeking advice | worked a little: 63.3% to 67.6%, but see Section 6 | [a13] |
| Self-check of own first answer with no feedback | failed: GPT-4 GSM8K 95.5 to 91.5 to 89.0; GPT-3.5 CommonSenseQA 75.8 to 38.1 to 41.8; with oracle labels GPT-4 reached 97.5 (row order inferred from garbled text) | Huang et al. 2024 [d19] |
| Generate, test, repair vs more samples at equal budget | mixed: 0.97x pass@22 in one config, 1.05x pass@20 in another; GPT-4 on APPS up to +8%; GPT-3.5 up to +34% relative on competition problems; human feedback lifted repair success 1.58x (33.3% to 52.6%) | Olausson et al. 2024 [d17] |
| Verifier plus many samples | worked: SWE-bench Lite 15.9% with 1 sample to 56% with 250; without a verifier, majority vote and reward models plateau | Brown et al. 2024 [d25] |
| Execute code for real | worked: BIG-Bench Hard text-davinci-003 direct 55, CoT 72, Chain of Code 84; PaLM 2-S 49, 61, 78 | [d24] |
| Trim later rounds on easy math | worked: first round correct in over 92% of cases; MATH500 tokens cut 48.6% with accuracy kept | Chen et al. 2024 [d18] |

### 5.4 Moderators and boundary conditions

- **Experience.** Referees: experts equal in both styles, novices better analytic (d09). Residents show premature closure (d11).
- **Atypical cases.** Pharmacists shift to analysis (d10).
- **Regularity and learnability of the environment** (Kahneman and Klein) [a07].
- **Difficulty.** Chess: extra deliberation helps both groups on easy and hard tactics [b07]. Fast play does better when the evaluation gap is large [b10, b12]. Test-time compute: easy items want sequential checking, medium-hard items want search, the hardest items gain little [d16].
- **Complexity.** Chess error rises with piece count [a08]. Search budget needed rises with complexity [b11].
- **Time pressure.** Raises blunders in elite chess [b01]. Did not change TTF use in basketball video [d06].
- **Domain with exact answers.** Crosswords turn the question into "do I know it?" [a14].
- **Moderators of TTF** reported by Raab: situation, emotion, personality [a21]. TTF itself appears in low-familiarity everyday scenarios and children, so "needs experience" is not firmly shown for the heuristic [d03, d02].
- **Source concentration.** Many lines repeat one paper: a09, a10, a26, b01-b06, b24 are Vidulich and Tsang; b10-b12 are Sunde; b13-b15 and c01-c04 are Ruoss; b20 and c06 are Karvonen. Independent counts are lower than line counts suggest [critique].

### 5.5 Candidate switch signals, ranked on evidence

1. Agreement of two to three short attempts (tested at scale) [d20, d21].
2. Confidence-weighted agreement (tested, uses the model's own score) [d22].
3. Stuck counter in multi-step tasks (one system) [c15].
4. First-answer survival through S4-S8 (our own planned log; the chess figure of 45% is second-hand) [b06].
5. Self-check of the first answer: do not use [d19].

No head-to-head comparison of these exists [critique gap 4].

## 6. Language models

### 6.1 The one direct test: RPD prompt for care-seeking advice

Kopka and Feufel (2026) [a13, a27, d23]:

- **Setup:** 45 real vignettes (2 emergency, 30 non-emergency, 13 self-care), 10 models, 3 prompts, 10 runs each, 13,500 assessments.
- **RPD prompt:** check whether the case matches a familiar typical case, simulate whether the usual action works, revise if not.
- **Results:** default 63.3% (CI 61.9-64.7); RPD 67.6% (CI 66.3-69); data-frame prompt 66.7% (CI 65.3-68). Odds ratios: RPD 2.26, data-frame 2.05 (p<.001).
- **Where the gain is:** self-care 13.4% to 29.8% (RPD), 24.6% (data-frame). GPT-4.1 self-care advice 0% to 43.8%; GPT-5.2 stayed at 0%. 88% of errors were over-triage. Non-emergency accuracy about 82-83% across prompts.
- **By model type:** larger for reasoning models (RPD OR 2.15, data-frame 1.70, p=.008). Biggest single gain +13 points (GPT-4.1 mini with the data-frame prompt, CI 9.7 to 16.1).
- **Emergency cases:** 100% default, 98% RPD, 99% data-frame. Only 2 vignettes; the 1-2 point drop was not tested.
- **Consistency:** Fleiss kappa 0.766 default, 0.717 RPD. At least one correct in 10 runs: 73.1% default vs 82.2% RPD.
- **Limits:** one domain, ChatGPT models only, more output tokens, no equal-token comparison. The gain moves the model away from over-triage, so it may be a prompt-format effect rather than recognition. RPD vs data-frame is not an ablation of the simulation step (overlapping CIs).

### 6.2 Models without chess-specific training

- General open LLMs track chess state poorly: LLaMA-7B 29.5% on BigBench chess state tracking; chess-trained models reach 95-99.5% [c07].
- GPT-3.5-turbo-instruct reading PGN: 66.5% puzzles and Lichess 1755 vs bots, far below a chess-specific policy [c02].
- Models trained on game text only build a board representation (probe 99.6%) and a skill estimate (probe 90.5%). A skill direction raised win rate up to 2.6 times [b20, c06].
- Train-time knowledge, not prompting, is what supplies the "pattern library" here.

### 6.3 Fast versus slow thinking in LLMs

Hagendorff, Fabi and Kosinski (2023) [c20, c21] on cognitive reflection and semantic illusion items:

| Model | Correct | Intuitive wrong answer |
|---|---|---|
| GPT-3 davinci-003 | 5% | 80% |
| Humans | 38% | 55% |
| ChatGPT-3.5 | 59% | 15% |
| ChatGPT-4 | 96% (95% in the Study 2 baseline; different task subsets) | 0% |

Chain of thought on davinci-003: correct 5% to 28%, intuitive wrong 80% to 29%. Blocking chain of thought: ChatGPT-4 95% to 88% (p<.05), ChatGPT-3.5 unchanged (p=.49). Small item sets; contamination possible.

- Overthinking: reasoning models spend 1,953% more tokens than conventional models on "2+3"; one example made 13 solutions; the first round was correct in over 92% of cases and used under 60% of tokens [d18].
- Switching: SwiftSage 84.7 vs 33.8-45.3 (baselines had different budgets) [c14]; Thinkless saves 50-90% [c19]; System-1.x 70.4% vs 48.7% and 37.2% [c16].
- Difficulty-adaptive compute: allocation matches best-of-N with up to 4x less compute; in a FLOPs-matched test, test-time compute beat a 14x larger model only where the small model had non-trivial success [d16].
- Cheap stopping by agreement: see 4.6 [d20-d22].

### 6.4 Case-memory agents

DiLu (40 items = RL at 600,000 episodes in the home setting; 70% to 35% off coverage) [c22, d15]. Voyager and Reflexion: see 4.7.

### 6.5 What is missing

No LLM study tests RPD's failure on unusual cases directly. No study runs an RPD arm with a real check at equal tokens. No study ablates only the simulation step (K22). Chain of Code is the nearest: real execution beats imagined execution [d24].

## 7. What our agent should take

Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested.

### Add now (established)

1. **Cheap first attempt for easy classes, with a code check, as the direct and checked mode default.** Schema part: S0 gate, G11, G12. Status [E] for the principle that spending should follow difficulty (already G12); numbers from Snell et al. (up to 4x less compute) and Chen et al. (over 92% first-round correct, 48.6% tokens cut). Evidence: d16, d18, K19. This confirms G11/G12; no change to SCHEMA.md text beyond a possible citation. Note K19 itself is marked single-source in claims.jsonl, so treat the support as two papers, not a broad consensus.
2. **Use agreement of two to three short attempts as the default switch from the cheap mode to deliberation.** Schema part: S0 and G1 (doubt only on a signal). Status [E]: three independent sources (Adaptive-Consistency, ESC, CISC). Evidence: d20, d21, d22, K21. Caveat: the sources are about stopping sampling, not about switching modes. This is the safest reading of the signal literature.
3. **Do not use the model's own re-check of its first answer as the signal.** Schema part: G1, 4b (already listed). Status [E]. Evidence: d19, K21.
4. **Time or token pressure hurts even strong systems, and extra thinking helps on hard items.** Schema part: G12. Status [E]. Evidence: b01, b05, b06, b07, K04. Keep allocation by difficulty, not uniform.
5. **Log how often the cheap first attempt passes the check.** Coded simple-match share in sport is 60-81%; use that only as a sanity band. Schema part: S0 logging. Status [E] but circular. Evidence: a15, K02.
6. **Pair pure recognition with a check.** The Ruoss policy could not see repetition and needed a hand patch; search adds about 11 points on tactical puzzles. Schema part: S4/S8 and G3. Status [E] as a design principle (already G3). Evidence: b15, c03, c04.

### Test first

| # | Item | Schema part | Status | Evidence |
|---|---|---|---|---|
| T1 | Prompt to name the typical case before acting (RPD-style S1) | S1/S3 | [S] | a13, a27, d23, K12 |
| T2 | Add the "simulate the chosen option" step (RPD step 3) only if it beats naming the typical case | S4 | [S] | d23, d24, K22 |
| T3 | Stuck counter (5 steps, no gain) as the trigger for the impasse mode in multi-step tasks | S6/G1 | [S] | c14, c15, K13 |
| T4 | First-answer survival through S4-S8 as an extra difficulty signal | S0/G12 | [S] | b06, K05 |
| T5 | Margin or gap between top two candidates as a gate | S0/G12 | [S] | b10, b11, b12, K06 |
| T6 | Fall-back rule: no matching stored case means full S1-S3, not a guess | S0/memory | [S] | d15, d09, d10, K16, K17 |
| T7 | Nearest-solved-case retrieval before generating | memory | [S] | c22, c23, K16 |
| T8 | Take-the-first versus generate-many on our items | S3 | [C] | d01-d08, K18 |
| T9 | Router trained or coded for fast vs slow | S0 | [S] | c16, c19, K15 |
| T10 | Fast attempt plus code check vs plain resampling at equal tokens, per difficulty bin | S4/S5 | [S] | d17, d25, K20 |

Notes:

- T1 and T2 are the direct RPD tests. Kopka's gain was mostly on self-care items and could be a format effect.
- T6 is the RPD "fails in unusual situations" claim made operational. The only measured data are DiLu (70% to 35%) and referees (novice vs expert). We have no threshold.
- T8 is contested. TTF evidence comes from one network; one knowledge-free task contradicts it. Generating several isolated attempts (S3) is already the schema's choice, so TTF would conflict with it. Test before changing anything.
- Do not add "slow down" or "be careful" prompts (4b). Do not add a self-check.

## 8. Concrete tests on our bench

All arms get the same token budget per item, setup cost included (G7). Report per-category gains, not only the mean.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 RPD prompt | mixed items, easy and atypical | (a) default; (b) "name the typical case, then act"; (c) "name the typical case, simulate the action, then act" | accuracy by difficulty bin; output tokens | b over a by 1-5 points on easy and mid items; c over b about 0; either loses on atypical items |
| B2 Simulation vs real check | items with a runnable check (code, ARC-style) | (a) name case only; (b) name case plus imagined simulation; (c) name case plus real execution | accuracy at equal tokens | c over b over a; c beats b (Chain of Code gap 84 vs 72) |
| B3 Agreement gate | items with graded difficulty | (a) fixed 4 attempts; (b) 2 short attempts, stop if they agree, else deliberate; (c) first attempt, then check only | accuracy and total tokens | b matches a with about 30-50% fewer tokens on easy bins; no loss on hard bins |
| B4 Switch signal comparison | same items | switch on (a) two-attempt agreement; (b) confidence-weighted agreement; (c) stuck counter; (d) margin between top two; (e) first-answer survival | area under accuracy vs tokens curve | a and b best; e worst |
| B5 Off-coverage items | items from classes absent from the memory | (a) retrieval-then-generate; (b) fresh generate; (c) retrieval with a similarity threshold that falls back to (b) | accuracy on off-coverage items; harm on in-coverage items | c best; a worst on off-coverage |
| B6 Take the first vs many | open and closed items | (a) first idea only; (b) 3 isolated ideas, code selects; (c) 6 isolated ideas, code selects | accuracy and distinctness | b or c over a on hard items; a ties on easy items |
| B7 Difficulty break-even | items bucketed by plain pass rate | cheap path vs full scaffold | accuracy gap by bin | cheap path wins or ties above a pass rate to be measured; scaffold wins below |
| B8 Recognition share log | all items | none (log only) | share solved by the first attempt and passing the check, per class | within or below the 60-81% band is plausible; above 90% means the bench is easy |

## 9. What does not transfer, and why

- **The 80% figure.** One retrospective study of one domain, coded by the authors. It says nothing about how often an LLM's first answer is right [K01, K23].
- **Experience as the library.** Human recognition rests on 10-20 years of experience [a20]. An LLM has a training distribution and no personal history. Its "typical case" is a statistical average, closer to Transcendence-style denoising than to a firefighter's memory [b19].
- **Mental simulation.** Humans simulate from a causal model. An LLM's imagined run is text and, in Chain of Code, loses to real execution (84 vs 72) [d24]. Real simulation in our agent is code execution at S4.
- **Time pressure.** Humans are forced by clocks. Our agent pays tokens. The right analogue is a token cap per mode (G11), not an urgency prompt.
- **Chess results as proof of RPD.** Elo rankings, blitz correlations and no-search networks show pattern knowledge is powerful. They do not test one-option-then-simulate. The networks imitate engine labels [critique].
- **Engine search gains.** MCTS on a value network has a trained value to guide it. Our agent's idea tree uses a code check, not a learned value [b16, c04].
- **Take-the-first in sport videos.** Participants were students or players in verbal option tasks with no exact check [d01]. Our items often have checks, so a fast first answer can be verified instead of trusted.
- **Human novice-expert split.** For an LLM the split is by item class, not by person. The referee data say experts did not need the analytic style and novices did. The LLM analogue is a class with a high plain pass rate vs a class with a low one. That mapping is untested [d09].
- **Qualitative medical studies.** Coded with RPD's own scheme; they describe, they do not test [d10, d11, d27].

## 10. Open questions

1. Is there any independent replication of the 80% finding, from a count of recognition vs comparison decisions in a non-fire domain, coded without the RPD scheme? [K23]
2. What do Klein et al. (1995), Calderwood et al. (1988) and Johnson and Raab (2003) report in numbers? [a12, a22, d12]
3. Does the simulation step add anything for an LLM beyond naming the typical case? [K22]
4. What is the cheapest reliable switch signal, head to head? [critique gap 4]
5. How does accuracy decay with distance from stored cases? DiLu has three settings only. [d15]
6. Does an RPD prompt change accuracy on atypical items, where the human model predicts failure? No LLM study tests this. [critique]
7. Are the Kopka gains a format effect? The data-frame prompt works almost as well. [d23]
8. Is TTF a real expert effect or a default habit? Children, caffeine and low-familiarity cases show it too. [d02, d03]
9. Reconcile +68 vs +300 Elo in Schultz et al. and the 93.5% vs 95.4% puzzle figures at the source. [d13, d14]
10. Do the unverified group means in Vidulich and Tsang (0.98 vs 1.45 and similar) match the paper's tables? [critique]
11. Does the 45% / 22% / 25% first-move survival figure hold in the primary Moxley paper? [b06]

## 11. Sources

[V] = opened and read this session (full text, PDF, or the abstract page as noted). [M] = snippet or second-hand only.

**RPD founding and theory**

- [V, abstract via Crossref] Klein, Calderwood, Clinton-Cirocco (1985/2010) Rapid decision making on the fire ground. https://api.crossref.org/works/10.1518/155534310x12844000801203 (a01)
- [M] Klein, Calderwood, Clinton-Cirocco (1986) Proc. Human Factors Society 30, 576-580. https://doi.org/10.1177/154193128603000616 (a02, b25)
- [V, abstract] Klein (2008) Naturalistic decision making. https://api.crossref.org/works/10.1518/001872008x288385 (a03)
- [V] Wikipedia, Recognition primed decision. https://en.wikipedia.org/wiki/Recognition_primed_decision (a04, b23)
- [V] Wikipedia, Naturalistic decision making. https://en.wikipedia.org/wiki/Naturalistic_decision_making (a05)
- [V] Klein (2021) The RPD model: criticisms and confusions. https://www.psychologytoday.com/us/blog/seeing-what-others-dont/202102/the-rpd-model-criticisms-and-confusions (a06, a25)
- [V, abstract] Kahneman and Klein (2009) Conditions for intuitive expertise. https://pubmed.ncbi.nlm.nih.gov/19739881/ (a07, b22)
- [V] Macrocognition: from theory to toolbox (2016). https://pmc.ncbi.nlm.nih.gov/articles/PMC4731510/ (a20)
- [V] Raab and Gigerenzer (2015) The power of simplicity. https://pmc.ncbi.nlm.nih.gov/articles/PMC4625029/ (a21)
- [V] Thanasuan and Mueller (2014) Crossword expertise as recognitional decision making. https://pmc.ncbi.nlm.nih.gov/articles/PMC4161049/ (a14)
- [M] Ji et al. (2007) fuzzy logic RPD model. https://doi.org/10.1016/j.ins.2007.02.021 (a24)
- [M] Klein, Wolf, Militello, Zsambok (1995) Characteristics of skilled option generation in chess. https://doi.org/10.1006/obhd.1995.1031 (a12)
- [M] Calderwood, Klein, Crandall (1988) Time pressure, skill, and move quality in chess. https://doi.org/10.2307/1423226 (a11, b03, d12)

**Chess and human expertise**

- [V] Chassy, Lahaye, Didierjean, Gobet (2023) Intuition in chess. https://pmc.ncbi.nlm.nih.gov/articles/PMC10497664/ (a08)
- [V] Vidulich and Tsang (2026) Intuition and deliberation in elite expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC13100097/ (a09, a10, a26, b01-b06, b24; about 100,000 of 119,588 characters read)
- [V, abstract] Moxley, Ericsson, Charness, Krampe (2012). https://pubmed.ncbi.nlm.nih.gov/22541584/ (b07)
- [V, abstract] van Harreveld, Wagenmakers, van der Maas (2007). https://doi.org/10.1007/s00426-006-0076-0 (b08)
- [V, abstract] Connors, Burns, Campitelli (2011). https://pubmed.ncbi.nlm.nih.gov/21981829/ (b09)
- [V] Sunde, Zegners, Strittmatter (2022) Speed, quality, and the optimal timing of complex decisions. https://arxiv.org/abs/2201.10808 (b10-b12)
- [M] Burns (2004), Chabris and Hearst (2003), Gobet and Simon, Montero, as quoted in Vidulich and Tsang (a10, b04-b06)

**Sport, medicine, other domains**

- [V] Naturalistic decision-making in sport (2022), citing Macquet (2020). https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/ (a15)
- [V] Le Menn et al. (2019) Handball goalkeeper. https://pmc.ncbi.nlm.nih.gov/articles/PMC6942481/ (a16)
- [V] Community pharmacists' decision-making (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC11833647/ (a17, d10)
- [V] How do surgeons make intraoperative decisions? (2007). https://pmc.ncbi.nlm.nih.gov/articles/PMC2464983/ (a18)
- [V] Practice-Primed Decision Model for acute care nursing (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6414081/ (a19)
- [V] Soccer referees (2024). https://pmc.ncbi.nlm.nih.gov/articles/PMC11322511/ (d09)
- [V] Mansoori et al. (2025) residents, septic shock. https://pmc.ncbi.nlm.nih.gov/articles/PMC12712819/ (d11)
- [V, abstract] Lavoie et al. (2024) ICU nurses. https://pubmed.ncbi.nlm.nih.gov/38993090/ (d27)
- [V] Mattingsdal (2026) military decision-making assumptions. https://pmc.ncbi.nlm.nih.gov/articles/PMC13113691/ (d26)
- [V, abstract] Hepler and Feltz (2012). https://pubmed.ncbi.nlm.nih.gov/22545930/ (d01); [M] https://doi.org/10.1037/a0027807 (a23)
- [V, abstract] Musculus et al. (2019). https://pubmed.ncbi.nlm.nih.gov/30570294/ (d02)
- [V, abstract] Haeusser et al. (2014). https://pubmed.ncbi.nlm.nih.gov/24682504/ (d03)
- [V, abstract] Laborde and Raab (2013). https://pubmed.ncbi.nlm.nih.gov/23966445/ (d04)
- [V, abstract] Chen et al. (2025). https://pubmed.ncbi.nlm.nih.gov/40166816/ (d05)
- [V, abstract] Hepler and Kovacs (2017). https://pubmed.ncbi.nlm.nih.gov/27391409/ (d06)
- [V, abstract] Raab and Laborde (2011). https://pubmed.ncbi.nlm.nih.gov/21462689/ (d07)
- [V, abstract] Ramanayaka et al. (2024) scoping review. https://pubmed.ncbi.nlm.nih.gov/38163513/ (d08)
- [M] Johnson and Raab (2003). https://doi.org/10.1016/S0749-5978(03)00027-X (a22, b26)

**AI and LLM studies**

- [V] Ruoss et al. (2024) Amortized planning. https://arxiv.org/abs/2402.04494 (b13-b15, c01-c04)
- [V] Schultz et al. (2025) External and internal planning with language models. https://arxiv.org/abs/2412.12119 (b16-b18, d13)
- [V, abstract] Zhang et al. (2024) Transcendence. https://arxiv.org/abs/2406.11741 (b19)
- [V] Karvonen (2024) Emergent world models in chess LMs. https://arxiv.org/abs/2403.15498 (b20, c06)
- [V, abstract and head] Toshniwal et al. (2022). https://arxiv.org/abs/2102.13249 (b21)
- [V] Jenner et al. (2024) Learned look-ahead. https://arxiv.org/abs/2406.00877 (c05, c25)
- [V, abstract] Feng et al. (2023) ChessGPT. https://arxiv.org/abs/2306.09200 (c07)
- [V] McIlroy-Young et al. (2020) Maia. https://arxiv.org/abs/2006.01855 (c08, c09)
- [V, abstract] Tang et al. (2024) Maia-2. https://arxiv.org/abs/2409.20553 (c10)
- [V abstract; table numbers from an earlier agent] Monroe and Chalmers (2024) Chessformer. https://arxiv.org/abs/2409.12272 (c11, d14)
- [V, abstract and intro] McGrath et al. (2022) AlphaZero knowledge. https://arxiv.org/abs/2111.09259 (c12)
- [V, abstract] Schut et al. (2023). https://arxiv.org/abs/2310.16410 (c13)
- [V abstract; numbers from an earlier agent] Lin et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390 (c14, c15)
- [V] Saha et al. (2025) System-1.x. https://arxiv.org/abs/2407.14414 (c16)
- [V, abstract] Su et al. (2025) Dualformer. https://arxiv.org/abs/2410.09918 (c17)
- [V, abstract and intro] Lehnert et al. (2024) Searchformer. https://arxiv.org/abs/2402.14083 (c18)
- [V, abstract] Fang et al. (2025) Thinkless. https://arxiv.org/abs/2505.13379 (c19)
- [V] Hagendorff, Fabi, Kosinski (2023). https://arxiv.org/abs/2212.05206 (c20, c21)
- [V] Wen et al. (2024) DiLu. https://arxiv.org/abs/2309.16292 (c22, d15)
- [V, abstract] Wang et al. (2023) Voyager. https://arxiv.org/abs/2305.16291 (c23)
- [V, abstract] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (c24)
- [V] Kopka and Feufel (2026) care-seeking advice. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ (a13, a27, d23)
- [V] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314 (d16)
- [V] Olausson et al. (2024) Self-repair. https://arxiv.org/abs/2306.09896 (d17)
- [V] Chen et al. (2024) Overthinking of o1-like LLMs. https://arxiv.org/abs/2412.21187 (d18)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d19)
- [V] Aggarwal et al. (2023) Adaptive-Consistency. https://arxiv.org/abs/2305.11860 (d20)
- [V] Li et al. (2024) ESC. https://arxiv.org/abs/2401.10480 (d21)
- [V, abstract] Taubenfeld et al. (2025) CISC. https://arxiv.org/abs/2502.06233 (d22)
- [V] Li et al. (2024) Chain of Code. https://arxiv.org/abs/2312.04474 (d24)
- [V] Brown et al. (2024) Large Language Monkeys. https://arxiv.org/abs/2407.21787 (d25)

*Links to parallel subfields (not covered here): Chunking and templates; Pattern-recognition theory of search; Fast and frugal heuristics, ecological rationality; Expert-novice differences; Computer chess and game AI; Test-time compute scaling; Overthinking; Bounded rationality and satisficing; Case-based reasoning; Retrieval and similarity; Metareasoning, value of computation; Optimal stopping.*

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 5 established claims: 2 confirmed as written, 3 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E16.07-K02** (now single-source: the sources are not independent). Only a15 (a secondary report of Macquet 2020) gives the 60-81/13-28/3-24 figures; a16 is a single-goalkeeper case study (simple match 46%, simulation 34%, diagnosis 20%) that does not support them, and neither source mentions firefighting or circularity.
- **E16.07-K03** (reworded: the sources support less). Numbers check out (N=63, r=0.664, 44% of variance in evaluation error; Burns 64-81% of variance, via secondary report), but 'skill is largely fast pattern knowledge' is stronger than the sources: 44% leaves most error variance unexplained and blitz-standard overlap is a correlation, not proof of pattern knowledge. Corrected claim: In chess, quick judgement improves with skill: Elo accounted for 44% of the variance in position-evaluation error after 5 seconds (N=63, r=0.664; Chassy et al. 2023), and rank scores in 5-min blitz tournaments accounted for 64-81% of the variance in rank scores based on standard games (Burns 2004, as reported by Vidulich and Tsang 2026), which leaves 19-36% unexplained.
- **E16.07-K15** (reworded: the sources support less). System-1.x numbers confirmed (Maze Navigation, 70.4% at 13.6 states vs 48.7 and 37.2). Thinkless abstract says it cuts the USE of long-chain thinking by 50-90%, not reasoning cost; Table 1 shows tokens falling only about 40-70% and some accuracy loss (e.g. MATH-500 0.861 to 0.795, Minerva 0.958 to 0.925 for the efficient row). Corrected claim: Learned switching between fast and slow reasoning can sharply cut slow reasoning: Thinkless reduces the use of long-chain thinking by 50-90% on Minerva Algebra, MATH-500 and GSM8K, with token savings smaller than that and a small accuracy drop on some benchmarks; and on Maze Navigation a tuned mix of fast and slow planning (System-1.x, x=0.5) gets 70.4% valid plans at 13.6 states vs 48.7% (System-1) and 37.2% (System-2).
- **E16.07-K04** (now single-source: only one opened source, code check).
