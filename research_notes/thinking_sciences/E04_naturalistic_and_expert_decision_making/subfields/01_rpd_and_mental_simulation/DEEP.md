# Recognition-primed decision and mental simulation: deep document

*Subfield E04.01. Built from evidence_a to evidence_d.jsonl, claims.jsonl (K01-K31) and critique.md in this folder. Evidence ids (a01, b14, c09, d06 ...) point to those files. Status marks follow SCHEMA.md: [E] established, [S] single-source, [C] contested. Items marked "unverified" must not be cited with a number.*

---

## 1. What it is

Recognition-primed decision (RPD) is Gary Klein's model of how experienced people decide in the field, under time pressure, with unclear goals and changing conditions. It came from interviews with urban fireground commanders (FGCs) in the 1980s. The commanders said they were not choosing between options. They said they saw the situation as a typical case, and a typical action came to mind. They then checked that action by imagining it being carried out. (a01, a02, a32)

The model has two parts. Klein says both are needed, and that a "recognition only" build is incomplete (a08).

1. **Situation recognition.** The situation is matched to a prototype. The match brings four things: plausible goals, critical cues, expectancies, and a typical action. (a02)
2. **Mental simulation.** The person runs the chosen action forward in the head, to find problems before acting. (a02, a10)

There are three variants (a02):

| Variant | What happens |
|---|---|
| A. Simple match | Situation is familiar. Typical action is carried out. |
| B. Diagnose | Situation is unclear. The person looks for more cues, builds a story, then matches. |
| C. Evaluate a course of action | The action is simulated. If a flaw shows, repair it, or reject it and take the next most typical action. |

Klein's seven features (a03): first option is usually workable; options are evaluated one at a time (serial); satisficing, not optimising; evaluation by mental simulation; the effort goes into improving one option, not choosing between several; focus on situation assessment, not on the choice event; the person is primed to act.

Lipshitz restates the model as a queue of actions ordered by typicality. Simulation has four outcomes: implement as is, modify, reject and take the next, or reassess the situation because the imagined future exposed something missed (a37). The "reassess" outcome is the link back to diagnosis.

**Why this matters for our agent.** The model is a template for a loop that is cheap on easy items and checks on hard ones: propose the first workable option, walk it through, repair or move to the next option, and go back to diagnosis when an expectation breaks. Our schema already has most parts (S3 generate, S4 test, S5 revise, S6 impasse). This subfield asks four things.

- How often is the first candidate good enough?
- When is it safe to trust?
- Does a "simulated walk-through" add anything over a plain candidate?
- What does the language-model literature say about simulation as a check?

**The short answer from the evidence.**

- The first option is good only for experts, on pattern-type tasks (K04, K05, K06).
- A model-run walk-through is a weak check. It helps when the simulator is external or sound, or when the rollout is grounded and short (K15, K16, K27).
- Most of the gain in check-and-revise loops comes from the quality of the check (K27).
- Part of the gain in search and rollout methods is simply more samples (K13).
- No controlled human experiment isolates the mental-simulation step (K09, b29).

---

## 2. History and theories in depth

### 2.1 Origin (1985-1993)

- **1985-1988.** Klein, Calderwood and Clinton-Cirocco studied fireground commanders. The report is ARI Technical Report 796 (1988), with a short paper in 1986. Commanders were asked about non-routine incidents. The team expected option comparison. They found none that the commanders reported. Quote: "We found no evidence for extensive option generation. Rarely were even two options concurrently evaluated." (a01) The founding counts (26 commanders, 156 decision points, over 80% prototype match, under 12% comparison) come only from search summaries. The DTIC report could not be opened. Do not treat them as verified. (a15, opened:false)
- **1989.** About 30 researchers met at a US Army Research Institute workshop (Orasanu's program). The book *Decision Making in Action* (1993) followed. Naturalistic decision making (NDM) became a field. (a07)
- **1993.** Chapter 6 gives the full model (a32). Klein admits he cannot show that commanders were not comparing options below awareness. He says the burden of proof is on those who claim hidden comparison. Quote: "We have no way of demonstrating that the fireground commanders weren't contrasting alternative options, but the burden of proof is not on us." (a32)

### 2.2 The framing: matching versus choice

Lipshitz (1993) answers the objection that RPD is a nondeliberate choice. He says matching means the action comes from recognition, and reassessment means testing it by simulation. He proposes to define a decision as an action argument ("do A because R"), not as a choice (a38). For code this split is clean. Either the program holds a scored list and picks (choice), or it holds one candidate and keeps or repairs it (matching). We can log which one a run used.

### 2.3 Rival and companion accounts

| Account | Claim | Relation to RPD | Source |
|---|---|---|---|
| Take-the-first heuristic (Johnson and Raab 2003; Raab and Gigerenzer 2015) | Generate options in order of validity. Stop at the first feasible one. | Narrower, testable form of RPD's "first option is workable". | a17, b12 |
| Long-term working memory (North et al. 2011) | More options generated means better performance. | Predicts the opposite of take-the-first. Option count versus quality separates them. | b12 |
| Hammond's cognitive continuum | Intuitive and analytic modes lie on one scale. | Klein adopts it: recognition and analysis are ends of one continuum. | a05 |
| Kahneman and Klein (2009) | Intuition is valid where the environment is regular and feedback allows learning. Confidence is not a guide to accuracy. | Gives the validity condition for trusting a first answer. | a24, b26 |
| Resource-rational / value of computation | Skilled people think longer where thought changes the answer. | Explains how experts switch between the fast and slow modes. Sibling subfield. | a30, d09 |
| Computational RPD agents | Recognition as multiple-trace memory (RPDm), Markov logic network, or instance-based learning. Simulation as a Bayesian network. | Formal builds. They report no hard accuracy numbers. | a27, a28, c19 |

### 2.4 Critique of the evidence base

- **Method.** Retrospective interviews, coders from the research group, a liberal criterion for what counts as analytic, no outcome control, and few decision points (a33, K03). Inter-coder agreement was 87-94% (a04, a33). That is agreement on coding, not evidence that the model predicts choices.
- **Falsifiability.** Klein replies that random-quality first options would have falsified the model, and the 1995 chess study shows the first options were of high quality (a09). The primary chess papers (Calderwood et al. 1988; Klein et al. 1995) were not retrieved. We have no numbers from them (d16, opened:false).
- **Field versus lab.** Lipshitz et al. (2001) drew 16 commentaries asking for controlled methods. Klein replies that lab studies remove the 10-20 years of experience that make the effect appear. (a07)
- **No direct test of simulation.** Direct tests exist for take-the-first (sport, chess) and for reflection (medicine). None isolates the walk-through step (b29, K09). The search was narrow and ran out of budget, so this is absence of evidence in one search, not proof of absence.

### 2.5 Language-model literature that touches RPD

Only one paper uses RPD language directly (a26). The rest is "simulation as checking" work in planning and agents: RAP, Tree of Thoughts, WebDreamer, WMA, MENSA, SwiftSage, LATS, Reflexion, LLM-Modulo, and probes of LLMs as world simulators. They are covered in section 6.

---

## 3. Core findings with exact numbers

Status uses claims.jsonl labels. "Human" rows come from people. "LLM" rows come from language-model studies. Unverified details are flagged.

### 3.1 Frequency of recognition (human)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RPD frequency is a range of 42-80%, not a constant 80% | Klein 1993 Table 6.1, coded by research team, intercoder agreement 87-94%. Urban FGC-1: 156 decision points, 80% (includes trivial points; mean 23 years). FGC-2 hard points: experts 48 points 58%, novices 33 points 46%. Wildfire commanders: 110 points, 51% (functional 56%, organisational 39%). Tank platoon cadets: 55 points, 42%. Design engineers: 51 points, 60%. | a33 (re-checked in critique) | [E] K01 |
| Other quoted ranges | Ambur's digest of Klein 1998: 46-96% across studies (no study-level breakdown). Klein and Wright 2016: "80 to 90 percent" of firefighter decisions, no N. | a13, a06 | Reported, loose |
| Sport review | Simple match 60-81%, diagnose 13-28%, evaluate by simulation 3-24% (Macquet 2020 as cited). First option kept in about 80% of athlete decisions. | a18 | Secondary |
| Pilots in a simulator used RPD far less | 120 airline pilots; 34% RPD vs 66% analytical among 108 classifiable (abstract says "about one third"; the 34/66/108 split was not re-checked). | b04 | [S] K01 |
| Experience and time pressure raise recognitional use; novices and organisational decisions lower it | Expert 58% vs novice 46%; functional 56% vs organisational 39%. Klein says novices use RPD "less than half the time". | a33, a34, a08 | [S] K02 |
| The frequency is process description, not evidence of quality | Retrospective, coder-involved, liberal analytic criterion, no outcome control. | a33, a15, b04 | [E] K03 |
| Neither experience nor remote-associates skill predicted RPD use in pilots; RPD and analytic crews rated equal overall; analytic crews rated higher on planning and on review-and-modify | Logistic model p=.66. Overall rating U=1294, p=.49. Planning U=1032, p=.02. Review and Modify U=952, p=.004. | b05 | [S] |
| Fireground "80% of incidents" is unit-unclear | Two headline numbers circulate: 80% and 58%. | b07 | Caution |
| Unverified | Over 80% prototype match, under 12% comparison, 26 commanders (1986 study); AEGIS officers share (Kaempf 1996); "87% feature matching" (1993 naval snippet). | a15, a16, b27 | Do not cite |

### 3.2 Is the first option good? (human)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Handball: first options rated better than later ones | N=85 (ages 13-18, 6-11 years' experience), 31 frozen scenes, 4.23 options per scene, 107 distinct solutions rated by 4 coaches. Quality fell with each new option. Players switched from a good first choice to a poor final one more than the reverse. Read through a summary page, not the paper. | a17, b11 | [E] K04 |
| Strong chess players often pick the first generated move; move quality fell from the first to the third option | Original study N=34, three Elo groups (under 2000, M=1659; over 2000, M=2227; GMs over 2399, M=2506); M=3.11 options. | b02 | [E] K04 (secondhand) |
| Take-the-first fails in weaker players | N=92 (Elo under 2000), M=2.2 options, first generated move judged best 37.3%, no effect of serial position F(3,992)=1.73, p=.159. | b01 | [E] K05 |
| Moxley et al. (2012): first move often not kept | Mean Elo 2194 vs 1836; first move kept as final in 45% overall; hard positions 22% (stronger) and 25% (weaker); easy positions 73% and 50%. Five minutes per position. Second-hand. | a21 | [E] K05 |
| First-move quality depends on task type | Under time pressure: strategic +2.32 vs tactical -1.14 (t=5.66, p<.001, d=0.62 [0.40, 0.84]). No time pressure: +2.93 vs -0.60 (d=0.52). | b03 | [E] K06 |
| Time pressure hurts even grandmasters | N=20 GMs (Elo 2540-2812, mean 2671), 3 min vs 7.5 s per move; blunders per move nearly doubled; t(19)=-5.79, p<.001, d=1.30. The detail "18 of 20 worse" was not found in the page text. Unverified. | a22 | [E] K07 |
| World champions: fast moves with under 5 minutes left had more blunders than fast moves with ample time | 7 champions; counts by time band 2934, 2905, 2859, 2849, 1250. Time per move partly reflects difficulty. | a23 | [E] K07 |
| Old "masters are immune to time pressure" claim rested on a tiny sample | Calderwood et al. 1988: 3 class B vs 3 masters. Chabris and Hearst: GMs (Elo 2530-2790) blundered more in rapid than standard games. | a20 | [E] K07 |
| Creativity link | Klatt et al. (2019, as cited): a positive correlation between creativity score and first-option quality in soccer. No effect sizes. | a19 | Weak |
| Unverified | Calderwood, Klein and Crandall (1988) and Klein et al. (1995) chess numbers. | d16 | Do not cite |

### 3.3 Mental simulation and checking (human)

| Finding | Numbers | Source | Status |
|---|---|---|---|
| Simulation is small | Max about 3 moving parts and about 6 transitions (Sources of Power p. 52, via a digest). | a11 | [S] K08 |
| Failure modes named by Klein | "Fall in love with it"; explain away contradicting cues; patch until the patches pile up (Cohen's snap-back, a hypothesis). | a12 | [S] K08 |
| Commanders rarely used specific past cases | Team expected analogue retrieval and found rare use. Recognition was of typicality. | a35 | [S] K22 |
| No direct controlled test of the simulation step was found | Zero experiments found in a narrow search. | b29, a39 | [S] K09 |
| Reflection helps residents when salient features mislead, not students | Residents N=34: correct 43% vs 52%, p=.03; salient-feature errors 0.85 vs 0.47 per resident, p=.02. Students N=50: 24% vs 25%, p=.76. | b08 | [E] K10 |
| Teaching reflection did not transfer | 44 GP residents (control 14, practice 11, models 19); same-day p=.649, one-week p=.747. | b09 | [E] K10 |
| Reflection helps only on complex cases | Mamede 2008, search snippet only. | b10 | Pointer |
| Premature closure in residents (ICU fluids) | 11 of 23 eligible residents interviewed; premature closure, confirmation bias and status-quo bias; seldom sought refuting information. | a25 | Qualitative |
| Prospective hindsight (premortem): thin human evidence | Mitchell et al. (1989) abstract: temporal perspective had little effect in experiment 1. The "30% more reasons" figure was not in the abstract. Klein's HBR page has no controlled test. | d13, d14 | [S] K29 |
| Value of computation: deliberation pays only where it changes the answer | Fixed position, zero value: 12,384 moves, quality independent of time. High-value position: 12,786 moves, quality rose with time, weaker players gained most. | d09, a30 | [S] K26 |

### 3.4 Boundary conditions (Klein 1993, a34)

Recognition is more likely with more experience, greater time pressure and less stable conditions. Analysis prevails when data are abstract and alphanumeric, when the problem is very combinatorial, when constituencies disagree, or when the choice must be justified. For predicting an enemy's plan, recognition can give tunnel vision. This is Klein's own summary, not one controlled comparison.

### 3.5 LLM results

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RPD prompt raised care-advice accuracy modestly; a data-frame prompt did nearly as well; no token-matched control | 10 ChatGPT models x 45 vignettes x 3 prompts x 10 runs = 13,500 assessments. Plain 63.3% (CI 61.9-64.7); RPD 67.6% (66.3-69); data-frame 66.7% (65.3-68). OR 2.26 and 2.05, p<.001. Self-care accuracy 13.4% to 29.8% (RPD), 24.6% (data-frame). Largest model gain +13 points (GPT-4.1 mini, data-frame). | a26 | [S] K11 |
| Search with model rollouts beats single-chain CoT (not token-matched) | Blocksworld, LLaMA-33B, 2/4/6 steps: CoT 17/2/0%; RAP(10) 100/86/26; RAP(20) 100/88/42. GPT-4 CoT 50/63/40. RAP average 64%, "33% relative" over GPT-4 CoT. Game of 24: IO 7.3, CoT 4.0, CoT-SC(k=100) 9.0, ToT b=1 45, ToT b=5 74. | b14, c01, b15, c03 | [E] K12 |
| Part of the gain is more samples | Game of 24: CoT best-of-100 49%. Stechly: 25 samples 42% vs sound-verifier loops 36-38%. Graph colouring sampling 40/44% vs verifier 34-38%. Snell: on easy questions heavier verifier-guided search lowered accuracy, best-of-N did not. | b15, b22, c27, c14, d04 | [E] K13 |
| Search needs a capable model | ToT Game of 24: 74% with GPT-4, 19% with GPT-3.5. IO+Refine k=10 27%; IO best-of-100 33%. | c25, c03 | [S] K14 |
| Intrinsic self-checking fails | GPT-3.5 CommonSenseQA 75.8 to 41.8 after two rounds; GSM8K 75.9 to 74.7; GPT-4 GSM8K 95.5 to 89.0. Oracle labels GPT-3.5 GSM8K 75.9 to 95.5 (the trap). Game of 24 critic loop 5% to 3%; graph colouring 16% to 2%. | b21, b22, c14 | [E] K15 |
| Check quality drives the gain | Blocksworld GPT-4, n=100: generator alone 40; LLM critic 55; sound verifier (VAL) 88. Web tree search (VWA, 200 tasks, GPT-4o): no value function 24.5; LLaVA n=20 30.0; GPT-4o no consistency 28.5; n=5 32.5; n=20 37.0; ground truth 43.5. Survey: no success with prompted-LLM feedback except in exceptionally suited tasks. | d06, d05, d07 | [E] K27 |
| Executable plus sound verifier is the best-evidenced form | GPT-4 about 12% executable plans alone. With VAL and back-prompting: Blocksworld 82% in 15 rounds, Logistics 70%, Mystery Blocksworld about 10%. | c13, c23 | [S] |
| LLMs are weak world simulators | 76,369 transitions; best 59.9% on non-trivial changes; action-driven changes up to 77.1%, environment-driven up to 49.7%; humans 80% vs GPT-4 49% on a matched subset. 0.599^10 is under 1%. PlanBench GPT-4: plan generation 34.3%, plan verification 31.8%, execution reasoning 28.2%. | b17, b23 | [E] K16 |
| Grounding closes much of the long-horizon gap | Next-state identification 77.0 / 81.0 / 86.0 (Qwen-2.5-VL-72B / Claude-3.5 / Claude-3.7). Plan alignment 50 / 55 / 65 without retrieval, 90 / 85 / 95 with. OSWorld end-to-end: vanilla 28.47, RAG 27.76, WebDreamer 31.24, R-WoM 38.54 (+23.4%). Probe samples are small (about 20 tasks, not confirmed); alignment judged by an LLM. | c07, d10, d11 | [E] K16, K31 |
| Next-state prediction in web tasks | 54.75% average vs a distractor; GPT-4o action selection 53% with state only, 73% with true next state. | c06 | [S] |
| Imagine then score candidates is modestly better than reactive and cheaper than real search | WebDreamer GPT-4o: VWA 23.6 vs reactive 17.6 (tree search 26.2); Online-Mind2Web 37.0 vs 26.0; Mind2Web-Live 25.0 vs 20.2. Untrained Qwen2-VL-7B 17.2 on VWA (no gain). WMA GPT-4o-mini WebArena 16.6 vs CoT 13.1; cost $0.4 vs $2.7, 140 s vs 748 s. Shopping: WMA 20.8 vs tree search 28.1. | c05, c06, c24, c28 | [E] K17 |
| Fast default plus slow planner on trouble | ScienceWorld (GPT-4): SwiftSage 84.7, Reflexion 45.3, ReAct 36.4, SayCan 33.8; tokens per action 757 vs 1856-2983. Fast module is fine-tuned on oracle trajectories; switch rule hand-written. | b19, c10 | [S] K18 |
| Step-wise execution in a real simulator gave little | 102 IPC Blocksworld instances: Fast Downward 85.3%, direct LLM (Claude Haiku 4.5) 63.7%, agentic 66.7%, 5.7x tokens. | c11 | [C] K19 |
| Rollout depth is not settled | MENSA (GPT-4o-mini, ScienceWorld): ReAct 22.4, Reflexion 25.9, SSO 54.5, MENSA 70.3; NetHack 12 / 10 / 50; depth beyond 3 hurt; single seed 42. Web tree search improved to depth 5. Four-in-a-row reasoning models: mean depth 1.78 plies, depth beta=-0.015 (p=.82), breadth beta=0.075 (p=.0025). | c09, d05, d08 | [C] K20 |
| Reflection needs a trustworthy signal | HumanEval 80% to 91%; MBPP 80% to 77%; test-suite false-positive rate 0.01 vs 0.16. LATS HotpotQA: full 0.63, no reflection 0.58, no LM heuristic 0.37, DFS 0.42. | b24, c17, c16 | [S] K21 |
| A real simulator beats imagination | Mind's Eye: +27.9% zero-shot, +46.0% few-shot on 39 physics tasks. Chain of Code: 84% on BIG-Bench Hard, +12 over CoT. | b20, c04, c15 | [S] |
| Cheap first-sample gate exists on reasoning benchmarks | Bottom-10% group confidence AUROC 0.860. GSM8K 49-61% of items accepted at 91.3-98.6% accuracy; MATH500 7-38% at 86.1-97.3%. Cross-modal agreement (CoT vs program) solved 78.6% of items with two samples, 9.3x fewer samples. Bayesian stopping cut calls 58% at -0.4 pp (fails on GPQA). | d01, d02, d03 | [E] K25 |
| Difficulty-adaptive compute | Over 4x more efficient than best-of-N (Snell). | d04 | [E] (used in G12) |
| Failure-enumeration prompt (premortem) | Harmfulness 3.22 to 2.19 vs safety prompt 2.62; a forward-structure control tied it under SFT. Accuracy not tested. | d12 | [S] K28 |
| Strategy-level memory beat trajectory and workflow memory | WebArena 684 tasks, Gemini-2.5-flash: none 40.5; trajectories 42.1; workflows 44.1; ReasoningBank 48.8. Confounded. | d15 | [S] K30 |
| No LLM test on Klein-style incident decisions scored against experts | COA-GPT (StarCraft II): best variant 3.4% below the human expert on mean reward, more friendly casualties. | c26, c20 | [S] K24 |

---

## 4. Mechanisms and models

This section describes each mechanism so that an engineer can build it. Items marked "design" are our reading, not a published algorithm.

### 4.1 RPD as a state machine

```
SITUATION -> RECOGNISE (match to prototype) -> brings goals, cues, expectancies, action queue
   match weak or cues missing  -> DIAGNOSE (collect more cues; build a story; re-match)
   match good                  -> take head of action queue
HEAD ACTION -> SIMULATE (short walk-through)
   no flaw                     -> ACT
   flaw, repairable            -> MODIFY -> SIMULATE again
   flaw, not repairable        -> REJECT -> next action in queue
   story cannot be built / contradicts a cue -> REASSESS (back to DIAGNOSE)
ACT -> watch EXPECTANCIES; if reality departs from them -> REASSESS
```

Sources: a02, a37, a14, a36. Mapping to our schema:

| RPD part | Schema part |
|---|---|
| Recognise | S0 gate and S3 generate (first candidate) |
| Diagnose | S1 and S2 (understand, represent) |
| Simulate | S4 test (preferably executed), else a short labelled walk-through |
| Modify | S5 revise |
| Reject, take next | S3 next attempt, or S6 operator |
| Reassess | S6 impasse back to S2 |
| Expectancy watch | S8 verify (compare what was predicted with what happened) |

### 4.2 Recognition: what the store holds

Klein's team expected commanders to retrieve past cases. They found that commanders rarely named an analogue, and no past incident matched a whole new one. Analogues helped only for parts. Klein reads this as experience merged into a judgement of typicality (a35). Implications for a build:

- Store prototypes (typical situation, cues, expectancy, action), not only raw cases. Evidence is weak. Strategy-level memory beat raw trajectories in one confounded test (d15, K30). MENSA retrieves past experiences by forecast and found target-based retrieval 45.0 vs state-based 41.4 (c09).
- Design: the action queue is ordered by similarity or typicality. Code keeps the queue and its position.
- Computational RPD builds use a multiple-trace memory (RPDm), a Markov logic network, or instance-based learning (a27, a28, c19). None report accuracy against a baseline.

### 4.3 The gate: when is the first candidate safe?

Humans use "years of experience". A model has no such stored trait, so a measured signal has to replace it. Candidate signals, with evidence:

| Signal | Evidence | Source |
|---|---|---|
| First-sample token confidence (bottom-10% group confidence), threshold calibrated on 128 held-out items | AUROC 0.860 vs 0.801 for self-certainty; accepted answers 91.3-98.6% accurate on GSM8K; quintile accuracy for Qwen2.5-7B 20.0, 40.2, 51.9, 82.9, 93.3% | d01 |
| Agreement of a reasoning answer and an executed-program answer | P(safe given agreement) near 1; 78.6% of items resolved with two samples | d03 |
| Bayesian stopping on answer confidence | 58% fewer calls at -0.4 pp; fails on GPQA | d02 |
| "Does a deeper look change the answer?" (value of computation) | Human chess: time helped only where depth changed the move | d09 |
| Difficulty estimate from the model's own pass rate | Easy: sequential revision; hard: breadth. Over 4x efficiency | d04 |
| Familiarity by retrieval similarity to solved cases | Not tested for LLMs. Design from K02 and K05 | none |

Limits: thresholds need per-model and per-task calibration; accepted share falls fast on harder sets (MATH500 as low as 7%); the signals were tested on math and QA, not on open or tactical tasks. Verbal confidence is not on the list because it is known to be unreliable (SCHEMA 4b).

### 4.4 The check: three kinds of "simulation"

Whether a walk-through helps depends on who runs it.

| Kind | What it is | Reliability | Evidence |
|---|---|---|---|
| Sound external check | Run the code, the tests, a plan validator (VAL), a constraint checker, a physics engine | High. Blocksworld 40 to 88%. Mind's Eye +27.9 to +46.0 points | d06, c13, b20 |
| Hybrid | Execute what can be executed; let the model emulate only the rest; mark which parts were imagined | +12 points on BIG-Bench Hard (Chain of Code) | c15 |
| Imagined by the same model | A written walk-through of its own plan | Poor alone. Self-correction lowers accuracy. Plan verification 31.8%. Next-state accuracy about 55-60% on hard changes | b21, b22, b23, b17 |

The imagined kind helps when one or more of these hold:

1. The world is rule-bound and the state is crisp (Blocksworld, ALFWorld; consistency ratios 0.96 and 0.91, but WebShop 0.67, c21).
2. The rollout is short (2-3 steps).
3. The rollout is anchored in retrieved real material (R-WoM, MENSA).
4. The model is strong enough that its evaluation is usable (GPT-4 vs GPT-3.5 in ToT).

### 4.5 Expectancy check (cheap, code-checkable)

Klein: if the reading is right, expectancies match events; if wrong, anomalies get noticed (a14). Build: at S3, the model writes "if this is right, I expect X on the check." Code then compares X with the real output. A mismatch routes to S6 as a signal. This is not in the LLM literature as a named method. It is a design idea (see U-items in UNKNOWNS.md).

### 4.6 Three uses of simulation seen in Klein's cases (a36)

1. **Check a plan** (forest fire): a staff member imagined a wind shift that closed the key road; the prime option was replaced.
2. **Test a reading by building a story** (Libyan airliner): the general could not build a plausible innocent-pilot story and treated that failure as evidence of hostile intent.
3. **Expectancy violation forces re-diagnosis** (laundry-chute fire): crews reported they were too late; smoke under the eaves shifted the reading to a building-wide fire.

Our check state can have all three: plan check, hypothesis test, and expectancy break.

### 4.7 LLM mechanisms to know

- **RAP** (b14, c01): one model plays agent and world model; MCTS with self-scored rewards; 10-20 iterations. Costly. Not Klein's single walk-through.
- **ToT** (b15, c03): propose several thoughts, value each as sure/maybe/impossible, search with backtracking. Breadth plus self-evaluation.
- **WebDreamer** (b18, c05): propose candidates, imagine each outcome in words, score, act. Closest to RPD step 3.
- **WMA** (c06, c24): a trained world model writes only state differences, used to rank a few sampled actions.
- **MENSA** (c09): forecast the next 3 action-state pairs, use the forecast to retrieve similar past experience. It is recognition by simulation.
- **SwiftSage** (b19, c10): a fast module acts by default; a large planner is called on a code-detected trouble signal (exception or no progress).
- **LLM-Modulo** (c13): the model proposes, an external sound verifier checks, the critique goes back.
- **LATS** (b16, c16): MCTS with environment feedback and reflection. The model-based value heuristic is the largest part (HotpotQA 0.63 to 0.37 when removed; reflection adds about 5 points).
- **R-WoM** (c07, d10): ground imagined rollouts in retrieved tutorials.

---

## 5. What holds up

### 5.1 Replications and independent tests of RPD

| Claim | Replicated by | Result | Verdict |
|---|---|---|---|
| Experts mostly use recognition | Klein's own studies across domains (a33); handball and basketball (a17, b12); a 4-person fireground video study (a29, student paper, N=4) | Frequency 42-80%. Independent labs mostly test take-the-first, not the full model. | Supported as a description. The headline "80%" does not hold. |
| Pilots use recognition | Gontar et al. (b04, b05) | 34%, not higher than a third. | Contradicts the headline in a drilled-procedure culture. |
| First option is best | Johnson and Raab (a17) | Yes for experienced youth handball players | Supported, boundary: familiar tasks with feedback. |
| Take-the-first in chess | Original N=34 (b02); replication N=92 weaker players (b01) | Replication: no quality advantage for the first move (p=.159) | Fails for weaker players. Needs expertise. |
| Masters unaffected by time pressure | Calderwood 1988 (3 vs 3); GM data (a22, a23) | Elite players blunder about twice as much in blitz (d=1.30) | Original claim does not hold. |
| Mental simulation as the causal checker | None found | Only descriptive | Untested (K09). |

### 5.2 Moderators that survive

- **Expertise.** Needed for the first option to be best (b01 vs b02).
- **Task type.** Pattern-heavy (strategic) beats calculation-heavy (tactical) for first moves (d=0.62, b03).
- **Difficulty.** In Moxley et al., first move was kept 73% (stronger) and 50% (weaker) on easy positions but only 22-25% on hard positions (a21). LLM side: easy items favour one answer plus revision; hard items favour search (d04).
- **Training doctrine and accountability.** Pilots, drilled in an analytic procedure, used recognition one-third of the time (b04).
- **Environment validity.** Intuition is reliable only where cues are valid and feedback allows learning (a24).
- **Data type.** Abstract, alphanumeric, combinatorial and adversarial problems favour analysis (a34).

### 5.3 What worked as an intervention

- **Sound external verification.** Plan accuracy 40 to 88% (d06); VAL-driven loop 82% (c13); VWA success 24.5 to 43.5 as the value signal improved (d05); Mind's Eye +27.9 to +46.0 (b20).
- **Grounding rollouts in retrieved real material.** Plan alignment 50-65% to 85-95% (c07, d10).
- **Short forecast depth with retrieval (MENSA).** 22.4 to 70.3 (single seed).
- **Fast default with a code-owned switch (SwiftSage).** 84.7 vs 36.4, but fine-tuned fast module.
- **Calibrated first-sample gates.** 49-61% of GSM8K items accepted at 91-99% accuracy (d01), fewer samples (d02, d03).
- **Reflection when features mislead.** Residents 43% to 52% (b08).
- **Imagine then score a few candidates.** WebDreamer +6.0 points on VWA at much lower cost than tree search (c05, c24).

### 5.4 What did not work

- **LLM self-critique without an external signal.** CommonSenseQA 75.8 to 41.8; Game of 24 5% to 3%; graph colouring 16% to 2% (b21, b22, c14).
- **Reflection with a noisy signal.** MBPP 80% to 77% (b24).
- **Teaching reflection to residents.** No transfer (b09).
- **Step-wise real-simulator execution judged by the model.** 63.7% to 66.7% at 5.7x tokens (c11).
- **Small untrained world models.** Qwen2-VL-7B 17.2 vs reactive 17.6 on VWA (c05). Untrained 72B no better than 7B on Mind2Web-Live (c28).
- **Generator-verifier on unfamiliar problems.** Mystery Blocksworld about 10% (c23): the verifier cannot rescue a generator with no plausible candidates.
- **Deeper rollouts beyond 3 in MENSA.** Performance and token cost both got worse (c09).
- **Premortem as a proven human technique.** Primary abstract says little effect (d13). The forward-structure control tied the premortem under SFT (d12).

### 5.5 Competing explanations

- **Search gains versus sample count.** Best-of-100 CoT reaches 49% on Game of 24, where ToT b=1 gets 45% (b15). Sampling beats verifier loops at 25 samples (b22). Content of feedback hardly matters (c14, c27). Most RAP/ToT comparisons are not token-matched. (K13)
- **RPD prompt gain versus extra reasoning text.** The data-frame prompt did nearly as well (a26). No length-matched neutral control. (K11)
- **Recognition versus hidden comparison.** Klein cannot rule out unconscious comparison (a32). Lipshitz's definition move avoids the question (a38).
- **Why rollouts fail.** Compounding error (b17, c08) versus self-evaluation quality (c25) versus weak breadth (d08).

### 5.6 Contradictions between sources (from critique.md)

- Klein 80% vs expert 58% vs pilots about 34% vs Ambur 46-96%. Causes: decision-point definition, coding, domain, training culture.
- Take-first holds in handball and strong chess; fails in weaker chess (b01) and in Moxley's hard positions (a21).
- Klein presents simulation as the check. LLM self-simulation checks are poor (b17, b21, b22, b23). Environment-grounded or retrieval-grounded simulation helps (c07, c04). The analogue works when the simulator is external or sound.
- Depth: MENSA says 3 (c09); web tree search says up to 5 (d05); reasoning models search 1.8 plies and depth does not predict wins (d08).

---

## 6. Language models

### 6.1 Direct test of RPD as a prompt

One study (a26). Ten ChatGPT models, 45 patient vignettes (2 emergency and 30 non-emergency cases per the page, which leaves 13 self-care by subtraction), three prompts, 10 runs each. The RPD prompt raised accuracy from 63.3% to 67.6% (OR 2.26). The data-frame prompt gave 66.7% (OR 2.05). Gains were bigger for self-care advice (13.4% to 29.8%) and for reasoning models than for non-reasoning models. Caveats: one domain, no token-matched control, small absolute gain (about 4 points), the gain may come from added reasoning text. Status [S].

No study was found that puts an LLM on Klein-style incident decisions scored against experts (c26). COA-GPT is the nearest, in StarCraft II, and it had more friendly casualties than the human expert (c20).

### 6.2 First workable option plus a walk-through

| System | Setup | Result | Token matched? |
|---|---|---|---|
| RAP | Model as agent and world model, MCTS | Blocksworld 33B 6-step: CoT 0% to RAP(20) 42% | No |
| ToT | Propose, value, backtrack | Game of 24: 4% CoT to 74% (GPT-4) | No (best-of-100 gets 49%) |
| WebDreamer | Imagine each candidate action | VWA 17.6 to 23.6 | Cost reported |
| WMA | Trained world model ranks candidates | WebArena 13.1 to 16.6 (GPT-4o-mini); $0.4 vs $2.7 | Cost reported |
| MENSA | Forecast 3 steps, retrieve experience | ScienceWorld 54.5 (SSO) to 70.3; NetHack 10 to 50 | Not matched; token cost discussed |
| SwiftSage | Fast default, slow on trouble | ScienceWorld 36.4 (ReAct) to 84.7 | Fewer tokens per action |
| LLM-Modulo | Generate, external verify, back-prompt | Blocksworld 12% to 82% | Rounds capped |
| Step-wise PDDL | Execute one action at a time | 63.7% to 66.7% at 5.7x tokens | Reported tokens |
| Pre-execution checks | WebShop checks before acting | GPT-4-turbo 17.73 to 33.33 (2 checks); GPT-4o 29.36 to 32.41 (2 checks), 36.70 (50 checks); not monotonic | Number of checks varied |

### 6.3 Behaviour of the models as simulators

- Single transition: strong where rules are crisp (next-state 77-86% in R-WoM; fine-tuned 7B near 99% in ALFWorld, c21).
- Hard transitions: about 55-60% (b17, c06). Environment-driven changes about 50%.
- Long procedures: drift. Plan alignment 50-65% without retrieval (d10).
- Zero-shot Claude-sonnet-4.5 next-state exact match: ALFWorld 64.73, SciWorld 56.83, TextWorld 17.70, WebShop 58.80. Three-shot: 77.04, 73.08, 49.12, 56.65 (c21).
- Rollout consistency with the real environment for a fine-tuned 7B: 0.96, 0.91, 0.92 and 0.67 for WebShop (c21).
- Implicit world models are less coherent than test accuracy suggests (Vafa et al.; abstract only, c22).
- Reasoning models search about 1.8 plies in four-in-a-row. Breadth predicts wins, not depth (d08).

### 6.4 What changed behaviour, and by how much

| Change | Effect |
|---|---|
| Sound verifier instead of LLM critic | 55% to 88% (Blocksworld GPT-4) |
| Value function quality | 24.5 / 30.0 / 37.0 / 43.5 (none, small LLM, GPT-4o n=20, ground truth) |
| Retrieval grounding of the rollout | Plan alignment +25 to +40 points |
| Real simulator instead of imagination | +27.9 / +46.0 points (physics) |
| Stronger base model | ToT 19% (GPT-3.5) to 74% (GPT-4) |
| Trained small world model | +4.0 to +4.8 over untrained 7B (WebDreamer) |
| Shorter forecast (3 vs more) | Better and cheaper (MENSA) |
| Difficulty-aware allocation | Over 4x efficiency (Snell) |
| Premortem-style prompt | Safety score only; accuracy untested |

### 6.5 Model-side caveats

- Many results mix scale, tuning and token budget. Almost none are token-matched. MENSA used one seed (42). The RPD prompt study uses one benchmark.
- Several papers use older models (GPT-3, GPT-3.5, GPT-4 in 2023). Later models improved on planning (PlanBench replanning 76.8%; Haiku 4.5 reaches 63.7% on Blocksworld without simulation).
- ProAct (c08) offers a training fix for compounding error. It is outside our no-training rule, so it is a reference only.

---

## 7. What our agent should take

Mark: schema part G (guardrail), S (state), O (operator), memory; status [E] established, [S] single-source, [C] contested.

### 7.1 Add now (established)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| N1 | **Log the route per item.** Record whether the run kept one candidate and repaired it (match) or compared several (choice), the accuracy of each route, and how often the first candidate was the final answer. Do not hard-code a recognise-first prior. | Section 6 logging; S0 | [E] | K01, K03; a33, a13, b04 |
| N2 | **Judge by outcome, not by the model's account.** The route a model reports is a retrospective story, as Klein's commanders' reports were. Use behaviour: which candidate was first, what changed. | G10 (restate) | [E] | K03; a32 |
| N3 | **Prefer executed checks over imagined ones.** Order of trust at S4: executed code or validator, rule-based or constraint check, retrieval-grounded walk-through, model's own walk-through (lowest, never alone). Mark imagined steps as imagined. | S4, G2, G3 | [E] | K15, K27; d06, d05, d07, b21, b22 |
| N4 | **Treat the model's own walk-through as a hint.** It can open a candidate or flag a contradiction, but it never certifies a pass. | G2, G10 | [E] | K15, K16; b17, b23, c14 |
| N5 | **Keep unreferenced rollouts short.** Cap at about 3 steps by default as a placeholder until U-tests set it per class. Anchor rollouts in retrieved real facts where a reference exists. | S4, O | [E] for the need to cap and ground; [C] for the number (see 7.2) | K16, K31; b17, c07, d10 |
| N6 | **Every search or rollout element needs a best-of-N arm at equal tokens.** Gains from RAP and ToT shrink against sampling (49% best-of-100; 42% at 25 samples vs verifier loops). | G7 | [E] | K13; b15, b22, c27, d04 |
| N7 | **Do not assume the first option is safe for calculation-type items.** Route exact-answer and combinatorial items to checking, and allow the fast path for pattern-type items where the class pass rate is high. | S0 | [E] | K06, K05; b03, b01 |
| N8 | **Trigger extra checking on a signal, not always.** Signals: a salient-but-possibly-irrelevant cue, a high difficulty estimate, disagreement, a failed check. Reflection helped only when features misled, and unprompted-reflection training did not transfer. Code must trigger it. | G1, G12, S6 | [E] | K10; b08, b09, d04 |
| N9 | **Any fast-path gate is calibrated per task class on a small labelled set and switched off where it does not separate right from wrong.** The gate options (first-sample confidence, cross-route agreement) work on math and QA but fail on GPQA. | S0, G12 | [E] for the existence on reasoning benchmarks; untested on our tasks | K25; d01, d02, d03 |
| N10 | **Cutting thinking has a cost even for experts.** Report the loss curve of accuracy against thinking budget per class. | G11, G12 | [E] | K07; a22, a23, d04 |

### 7.2 Test first (not yet in the schema)

| # | Item | Schema part | Status | Evidence ids |
|---|---|---|---|---|
| T1 | **One candidate plus a short sound check, versus best-of-N with majority or sound-verifier pick, at equal tokens.** The central RPD question. No token-matched study found. | S3/S4/S7 | [S] indirect | K04, K13; d04, d05, a39 |
| T2 | **Familiarity or confidence gate on the first candidate** (first-sample confidence, 2-3 sample agreement, retrieval similarity to solved cases). Gate decides: accept with one check, or widen to more candidates. | S0 | [S] human, [E] on math benchmarks | K02, K05, K25; d01, d03, b01 |
| T3 | **Option count scaled by familiarity.** Fixed one option versus familiarity-scaled count. | S0, S3 | [S] | K05; b01, b12 |
| T4 | **Rollout depth per task class** (1, 2, 3, 5). Default 3 is a hypothesis. | O | [C] | K20; c09, d05, d08 |
| T5 | **RPD-style prompt versus length-matched neutral reasoning prompt.** | S0, S1 | [S] | K11; a26 |
| T6 | **Forced counter-cue step** (list one cue that contradicts the simulation) before accepting a walk-through, versus a length-matched neutral step, on accuracy. | S4 / counter-cue | [S] | K08, K28, K29; a12, d12, d13 |
| T7 | **Expectancy check.** The model writes the expected output before the check runs; a mismatch triggers S6. | S3/S8 | [D] | a14, a36 |
| T8 | **Value-of-computation skip.** A cheap second look agrees with the first, so skip the rollout. | G12, S6 | [S] | K26; d09 |
| T9 | **Prototype memory versus exemplar memory** at equal tokens. | memory | [S] | K22, K30; a35, d15 |
| T10 | **Code-owned fast/slow router** (escalate on stuck or exception signal) versus always-slow, at equal total tokens. | S0, S6, G1 | [S] | K18; b19, c10 |
| T11 | **Retrieval-grounded rollout** versus ungrounded at the same depth, on items where a reference exists. | O | [S] | K31; c07, d10 |
| T12 | **Sound-check ablation.** How much of any gain comes from check quality versus from the act of simulating. | S4 | [E] direction, size unknown for our tasks | K27; d06, d05 |
| T13 | **Self-evaluation accuracy of our model on labelled partial states**, before any tree rollout is built. | O | [S] | K14; c25, c03 |
| T14 | **Reassess-on-broken-expectancy as an S6 trigger** versus other triggers. | S6 | [D] | a36, a37 |

---

## 8. Concrete tests on our bench

All arms are run at equal total tokens (setup, retries, checks and judge calls counted). Each test logs the route, the path and tokens per state (SCHEMA section 6). Use at least three seeds. Use the held-out part of each item (G3) as the metric where a check exists.

| Test | Item type | Arms (equal tokens) | Metric | Expected effect |
|---|---|---|---|---|
| B1 (T1) | Code and exact-answer items with an executable check; ARC-like items; arithmetic or constraint puzzles | (a) one candidate plus one sound check plus up to 2 repairs; (b) best-of-N with majority; (c) best-of-N with sound-verifier pick; (d) plain single pass | Held-out pass rate; tokens to first pass | (a) wins on easy and mid items (d04: sequential revision wins when easy). (c) wins on hard items. Expect no win for (a) on calculation-heavy items. |
| B2 (T2, T3) | Mixed classes labelled easy/hard | (a) fixed 1 candidate; (b) fixed 4 candidates; (c) count scaled by first-sample confidence or by cross-route agreement; (d) count scaled by retrieval similarity | Accuracy; tokens; AUROC of the gate per class | (c) at or above (b) at fewer tokens, on classes where AUROC is above about 0.75. No gain where AUROC is near chance. |
| B3 (T4) | Multi-step planning items (Blocksworld-type, grid, constraint chains) with an executable simulator | Rollout depth 1, 2, 3, 5 (imagined), against executed rollouts of the same depth | Plan validity; accuracy per depth; error compounding curve | Imagined rollouts peak at 2-3 steps then fall; executed ones keep rising. |
| B4 (T5) | Judgement items (triage-style, diagnosis-style) | (a) plain; (b) RPD prompt; (c) data-frame prompt; (d) length-matched neutral reasoning prompt | Accuracy; calibration | If (b) minus (d) is under 1 point, the earlier gain was reasoning length. |
| B5 (T6) | Items where a plausible first plan fails on a hidden cue | (a) walk-through only; (b) walk-through plus forced contradicting cue; (c) walk-through plus length-matched neutral step | Held-out pass rate; rate of "love of simulation" (accepted plans that failed the real check) | (b) beats (c) only if it lowers false accepts. Prior: small. |
| B6 (T7, T14) | Items with an executable check | (a) check only; (b) model writes expected result first, mismatch triggers S6 | Held-out pass rate; tokens | Gain from earlier detection of a wrong reading. Prior: small to medium. |
| B7 (T8) | Mixed difficulty | Full rollout always vs cheap second look; skip if both agree | Accuracy; tokens saved | No accuracy loss, 30-60% tokens saved on easy items (d09, d01-d03 as priors). |
| B8 (T9) | Items drawn from a class with prior solved examples | Memory as prototype summary vs raw cases vs both vs none, same stored content volume | Accuracy on later items; tokens | Prototype at least equal to raw at fewer tokens. Prior: weak (d15 confounded). |
| B9 (T10) | Long multi-step tasks with a stuck signal | Always-slow vs fast with code switch on stuck/exception | Accuracy; total tokens | Same accuracy at lower tokens (c10 prior), not fine-tuned here. |
| B10 (T11) | Items where reference notes exist | Rollout depth 5 with vs without retrieved reference | Plan alignment against executed truth | Alignment up 20+ points (d10). |
| B11 (T12) | Items with checks of graded quality | Same loop with no check / model critic / sound checker | Accuracy gain over no check | Ordering none < critic < sound (K27). The size on our tasks is unknown. |
| B12 (T13) | Labelled partial states from our tasks | Model rates partial states; compare with ground truth | Rank correlation; AUROC | Under about 0.65 means do not build tree rollouts on this model. |
| B13 (N1) | All | Log first-candidate-final rate per class | Fraction of items where the first candidate is the final one, and its accuracy | Needed to set priors for B1 and B2. |

---

## 9. What does not transfer, and why

1. **The 80% figure.** It is the top of a 42-80% range, from interviews with research-team coding and no outcome control (K01, K03). For a model, the frequency of recognition is a design variable, not a fact to copy.
2. **"Years of experience" as the gate.** A model has no such trait. The proxies (confidence, agreement) are untested on our tasks (K25).
3. **Retrospective interview evidence.** What a person said about their process is not what a model's reasoning text says about its own (G10). Klein himself cannot rule out hidden comparison (a32).
4. **Mental imagery.** People simulate with perceptual imagery and long expertise. A model writes tokens, and each token is a possible error. Human limits (3 parts, 6 steps) come from working memory, not from the same constraint as context (a11). The numbers happen to point the same way: MENSA found depth 3 best, but other work shows depth is not the key (K20).
5. **Expert-only effect.** Take-the-first works for high-expertise players. A generic model is the weaker case (b01). Gate it.
6. **Time pressure as the driver.** Klein's model arose under minutes-long time pressure. Our harness is token-limited, not time-limited. The analogue is the token budget (K07, d04).
7. **Embodied and perceptual domains.** Fireground cues are seen and felt. Klein says analysis prevails when data are abstract and alphanumeric (a34). Many of our tasks are abstract and combinatorial (ARC-like, puzzles). Expect the fast path to be weaker there.
8. **Team and multi-agent RPD.** The team evidence is second-hand (a40) and debate is excluded by G9.
9. **High-stakes domain tests.** Fireground, naval and military results do not carry over without a domain test (K24).
10. **Premortem.** Human outcome evidence is thin (K29). Do not import the 30% figure.
11. **Computational RPD agents.** They give architecture, not accuracy numbers (a27, a28, c19).
12. **Training-based fixes** (SwiftSage fine-tuned fast module, ProAct, trained world models) are outside the no-training rule. They are reference points only.

---

## 10. Open questions

1. At equal tokens, does one candidate plus a short sound check beat best-of-N with a majority or sound-verifier pick? On which item classes? (critique gap 1; only indirect evidence)
2. Which cheap signal predicts when the first answer is safe on our tasks: first-sample confidence, 2-3 sample agreement, retrieval similarity? (gap 2; works on math and QA, fails on GPQA)
3. What rollout depth is best per task class? Is the cap of 3 real? (gap 3; contested)
4. Which checks are sound for each of our task types, and how much gain is check quality versus simulation? (gap 4; direction clear, size unknown)
5. Does an RPD-style prompt beat a length-matched neutral prompt? (gap 5; no study)
6. Does a forced counter-cue step reduce false accepts at equal tokens? (gap 6)
7. Prototype-level memory versus exemplar retrieval, with the same content at two abstraction levels? (gap 7; d15 is confounded)
8. What are the real numbers in Calderwood, Klein and Crandall (1988) and Klein et al. (1995)? Not retrieved; needs library access. (gap 8)
9. Any human experiment where a premortem changed decision quality? (gap 9)
10. Does LLM next-state accuracy set a ceiling on how far rollouts help, and does retrieval grounding close it on our tasks? (gap 10; mostly closed in R-WoM-type settings, small probes)
11. Does the first sample from the model beat a random sample from its own distribution? That is the falsification test Klein proposes (a09, a39). Not measured.
12. Does Klein's "reassess" outcome (the imagined future exposed something unnoticed) map to a useful S6 trigger in an LLM?
13. Is recognition in an LLM retrieval of cases, or typicality? Klein's commanders showed the second. Models might do either (a35, c18).
14. What do newer models (2026 class) do on planning probes where 2023 models failed? The source numbers are mostly from older models.
15. Does the cross-route agreement gate (reasoning vs program) transfer to non-numeric items?

---

## 11. Sources

[V] = opened and read this session (some only the abstract page, noted). [M] = snippet or citation only.

**Klein and the RPD model**

- [V] Klein G, Klinger D (1991) Naturalistic decision making. Human Systems IAC Gateway 2(1). https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.191.833&rep=rep1&type=pdf (a01-a05)
- [V] Klein GA (1993) A recognition-primed decision (RPD) model of rapid decision making; Lipshitz (1993); Klein (1993) Twenty questions; Orasanu and Salas (1993). In *Decision Making in Action*. https://www.shadowboxtraining.com/wp-content/uploads/2024/09/Klein-et-al-1993-Decision-Making-in-Action-Models-and-Methods.pdf (a32-a40)
- [V] Klein G, Wright C (2016) Macrocognition: from theory to toolbox. Frontiers in Psychology 7:54. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00054/pdf (a06, a07)
- [V] Klein G (2021) The RPD model: criticisms and confusions. Psychology Today. https://www.psychologytoday.com/ca/blog/seeing-what-others-dont/202102/the-rpd-model-criticisms-and-confusions (a08, a09, b06)
- [V] Ambur O (2004) digest of Klein 1998 Sources of Power. http://ambur.net/rpd.pdf (a10-a14; secondary, quotes not checked against the book)
- [M] Klein G, Calderwood R, Clinton-Cirocco A (1986/1988) Rapid decision making on the fire ground. https://apps.dtic.mil/sti/pdfs/ADA199492.pdf (a15; blocked)
- [M] Kaempf, Klein, Thordsen, Wolf (1996) Decision making in complex naval command-and-control environments. https://journals.sagepub.com/toc/hfs/38/2 and https://doi.org/10.1518/001872096778701962 (a16, b27)
- [V] Fire Engineering summary of Klein et al. (1988). https://www.fireengineering.com/?p=277352 (b07)
- [V] Klein GA, gary-klein.com RPD page. https://www.gary-klein.com/rpd (b29)
- [M] Lipshitz, Klein, Orasanu, Salas (2001) Taking stock of naturalistic decision making. https://doi.org/10.1002/bdm.381 (b25)
- [M] Bond and Cooper (2006) review of RPD in emergency care. https://www.science.gov/topicpages/c/critical+decision+method (b28)
- [V, abstract] Kahneman D, Klein G (2009) Conditions for intuitive expertise. https://pubmed.ncbi.nlm.nih.gov/19739881/ and https://doi.org/10.1037/a0016755 (a24; b26 was the failed PDF fetch)

**Take-the-first, chess, sport, other domains**

- [V, summary page] Johnson JG, Raab M (2003) Take the first. https://www.psychologytoday.com/gb/blog/points-the-board/201911/when-your-first-choice-is-your-best-choice (a17); [M] https://lida.sport-iat.de/dbb/Record/4002191 (b11)
- [V] Raab M, Klenk, Medvegy et al. (2026) conceptual replication in chess, Journal of Expertise 9(1). https://www.journalofexpertise.org/articles/volume9_issue1/JoE_9_1_Raab_etal.pdf (b01-b03)
- [V] Raab M, Gigerenzer G (2015) The power of simplicity. Frontiers in Psychology. https://www.frontiersin.org/articles/10.3389/fpsyg.2015.01672/pdf (b12, b13)
- [V] Bossard et al. (2022) NDM in sport. https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/ (a18, a19)
- [V] Intuition and deliberation in elite expertise (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13100097/ (a20-a23; includes Moxley et al. 2012 second-hand)
- [V, abstract] Time spent thinking in online chess reflects the value of computation (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12553403/ (a30)
- [V] Kuperwajs et al. (2025) resource-rational planning under time pressure in online chess, CogSci 2025. https://escholarship.org/ (d09)
- [M] Calderwood, Klein, Crandall (1988); Klein, Wolf, Militello, Zsambok (1995). https://doi.org/10.1006/obhd.1995.1031 (d16)
- [V] Gontar, Porstner, Hoermann, Bengler (2015) Pilots' decision-making under high workload. https://elib.dlr.de/98017 (b04, b05; 34/66/108 not re-checked)
- [V] Carrigan (undated) fireground decision-making study. https://apps.usfa.fema.gov/pdf/efop/efo48927.pdf (a29; N=4, not peer reviewed)
- [V, abstract] Military professionals' endorsement of decision-making assumptions (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13113691/ (a31)
- [V] ICU resident cognitive task analysis (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12712819/ (a25)
- [V] Hybrid BDI / Markov-logic RPD implementation (2019). https://link.springer.com/article/10.1186/s13673-019-0197-2 (a27); Danial et al. (2019) https://doi.org/10.1186/s13673-019-0197-2 (c19)
- [M] Warwick et al. (2001); Stanard et al. (2001); Lebiere, Gonzalez, Warwick (2009); Sokolowski (2003). https://www.cmu.edu/dietrich/sds/ddmlab/papers/JCEDM_Lebiere_Gonzalez_Warwick.pdf (a28)

**Reflection, premortem (human)**

- [V] Mamede et al. (2012) salient distracting features. https://qualitysafety.bmj.com/content/21/4/295 (b08)
- [V, abstract page] Kuhn et al. (2020) teaching reflective reasoning. https://pure.eur.nl/en/publications/can-we-teach-reflective-reasoning-in-general-practice-training-th/ (b09)
- [M] Mamede et al. (2008). https://repub.eur.nl/pub/17793 (b10)
- [V, abstract] Mitchell, Russo, Pennington (1989). https://doi.org/10.1002/bdm.3960020103 (d13)
- [V] Klein (2007) Performing a project premortem, HBR. https://hbr.org/2007/09/performing-a-project-premortem (d14)

**LLM studies**

- [V] Hao et al. (2023) RAP. https://arxiv.org/abs/2305.14992 (b14, c01, c02)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (b15, c03, c25)
- [V] Zhou et al. (2023/2024) LATS. https://arxiv.org/abs/2310.04406 (b16, c16)
- [V] Wang et al. (2024) LLMs as text-based world simulators. https://arxiv.org/abs/2406.06485 (b17)
- [V] Gu et al. (2024/2025) WebDreamer. https://arxiv.org/abs/2411.06559 (b18, c05, c28)
- [V] Lin et al. (2023) SwiftSage. https://arxiv.org/abs/2305.17390 (b19, c10)
- [V] Liu et al. (2022) Mind's Eye. https://arxiv.org/abs/2210.05359 (b20, c04)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b21)
- [V] Stechly, Valmeekam, Kambhampati (2024) self-verification limitations. https://arxiv.org/abs/2402.08115 (b22)
- [V] Valmeekam et al. (2023) PlanBench. https://arxiv.org/abs/2206.10498 (b23)
- [V] Shinn et al. (2023) Reflexion. https://arxiv.org/abs/2303.11366 (b24, c17)
- [V] Chae et al. (2025) Web agents with world models (WMA). https://arxiv.org/abs/2410.13232 (c06, c24)
- [V] Mei et al. (2026) R-WoM. https://arxiv.org/abs/2510.11892 (c07, d10)
- [V, abstract/intro/part] Yu et al. (2026) ProAct. https://arxiv.org/abs/2602.05327 (c08)
- [V] Chang et al. (2026) MENSA. https://ifaamas.org/Proceedings/aamas2026/pdfs/BBRH3447.pdf (c09)
- [V] Goebel et al. (2026) Agentic LLM planning via step-wise PDDL simulation. https://arxiv.org/abs/2603.06064 (c11)
- [V] Valmeekam et al. (2023) On the planning abilities of LLMs. https://arxiv.org/abs/2302.06706 (c12)
- [V] Kambhampati et al. (2024) LLM-Modulo. https://arxiv.org/abs/2402.01817 (c13, c23)
- [V] Stechly et al. (2023) GPT-4 doesn't know it's wrong. https://arxiv.org/abs/2310.12397 (c14, c27)
- [V] Li et al. (2024) Chain of Code. https://arxiv.org/abs/2312.04474 (c15)
- [V, abstract/intro] Yasunaga et al. (2024) LLMs as analogical reasoners. https://arxiv.org/abs/2310.01714 (c18)
- [V] Goecks and Waytowich (2024) COA-GPT. https://arxiv.org/abs/2402.01786 (c20)
- [V, first 100k of 135k chars] From Word to World (2025). https://arxiv.org/abs/2512.18832 (c21)
- [M] Vafa et al. (2024) Evaluating the world model implicit in a generative model. https://arxiv.org/abs/2406.03689 (c22)
- [M] Search for LLM tests of RPD (c26, negative result). https://arxiv.org/
- [V, JMIR] Increasing LLM accuracy for care-seeking advice using prompts reflecting human reasoning (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ (a26; re-checked in critique)
- [V] Kim et al. (2026) ReASC. https://arxiv.org/abs/2601.02970 (d01)
- [V] Aghazadeh et al. (2026) CGES. https://arxiv.org/abs/2511.02603 (d02)
- [V] Saparkhan et al. (2026) CoT-PoT ensembling. https://arxiv.org/abs/2604.17433 (d03)
- [V] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314 (d04)
- [V] Koh et al. (2025) Tree search for LM agents. https://arxiv.org/abs/2407.01476 (d05)
- [V] Valmeekam, Marquez, Kambhampati (2023) Self-critiquing plans. https://arxiv.org/abs/2310.08118 (d06)
- [V, abstract/intro] Kamoi et al. (2024) critical survey on self-correction. https://arxiv.org/abs/2406.01297 (d07)
- [V] Chen et al. (2026) Extracting search trees from LLM reasoning traces. https://arxiv.org/abs/2605.06840 (d08)
- [V, secondary] Li et al. (2026) Text world models survey. https://arxiv.org/abs/2606.09032 (d11)
- [V] Kim et al. (2026) InvThink. https://arxiv.org/abs/2510.01569 (d12)
- [V] Ouyang et al. (2026) ReasoningBank. https://arxiv.org/abs/2509.25140 (d15)

**Not re-checked or flagged in critique.md:** a15 (do not cite), b07, b04 percentages, Mamede 2008, Johnson and Raab N and summary, a22 "18 of 20", a26 OR values and CIs.

**Related subfields run in parallel (links only):** Conditions for valid intuition; Resource-rational analysis; Analogical access; Library learning; Anytime search and restarts; Bandits for operator selection; Chess thought process and progressive deepening; Chunking and template theory; Proofs and refutations.
