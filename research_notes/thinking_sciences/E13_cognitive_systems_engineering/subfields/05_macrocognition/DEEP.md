# Macrocognition: deep document

*Subfield E13.05. Sources: evidence_a-d.jsonl, claims.jsonl (K01-K22), critique.md in this folder. Evidence ids (a01..d18) refer to those files. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Macrocognition is the study of thinking as it happens in real work: decisions, sensemaking, planning, coordination and expertise, under time pressure, uncertainty and with teams. It is defined against "microcognition" (working memory, attention, serial versus parallel search), which is studied in controlled labs (a04, b05).

It is a research stance, not one theory. The founders say it cares less about testing hypotheses and more about building useful descriptive models (a04). The method is cognitive task analysis (interviews, observation, think-aloud) mixed with experiments, aimed at "work as done" rather than "work as prescribed" (a08).

Core models that came out of it:
- Recognition-primed decision making (RPD): experts recognise a situation, take the first workable action, check it by mental simulation (a02).
- Data-frame model and plausibility-transition model of sensemaking: a frame defines what counts as data; anomalies trigger reframing (a17, a18, a19).
- Cue utilisation: a trait measure of how well a person uses stored pattern cues (a14, b20).
- Supervision and team-coordination results from operator studies (b12, b13).

Why it matters for our agent: it supplies candidate functions (frame, anomaly check, first-option-then-simulate, pattern memory) and a set of warnings (more information is not more understanding; narrated rationale is not the real process). But the evidence base is mostly human, descriptive and retrospective. Only one controlled LLM prompt study exists (Kopka and Feufel 2026). Treat everything here as hypotheses to test, not as spec (K17 [E]).

## 2. History and theories in depth

**Stage 1, field studies of decisions (1980s).** Rasmussen, Cohen, Beach and Mitchell, Klein and Noble studied real decisions outside the lab. About 30 researchers met in a 1989 workshop; the label Naturalistic Decision Making (NDM) followed. Book: Decision Making in Action (Klein et al. 1993). A Human Factors and Ergonomics Society technical group has existed since 1995; 12 NDM conferences were held by 2016 (a01).

**Founding study.** Klein, Calderwood and Clinton-Cirocco (1986) interviewed fireground commanders about real incidents. They said they seldom compared options. They recognised the situation as typical and acted. Klein and Wright (2016) say RPD "accounted for 80-90% of the decisions that firefighters made" and needs 10-20 years of experience (a02). We could not open the 1986 paper (DTIC returned 403), so N, coder agreement and the exact share are unknown (a29, K05 [C]). The share is a coder classification of retrospective interviews by the model's own authors.

**The "replications".** Cited: Schmitt and Klein 1999 (military leaders), Keren et al. 2013 (firefighters in virtual reality), Skriver 1998 (offshore oil platform managers), plus tests by Klein et al. 1995 and Johnson and Raab 2003 (a02). Our reference check: Schmitt and Klein is a Marine Corps Gazette article ("How we plan"), Skriver is a PhD thesis, and Keren is a stress and time-to-decision paper by its title (d06). None is confirmed as an independent test of the 80-90% share.

**Stage 2, macrocognition (2003 onward).** Klein, Klein and Klein (2000) defined the term; Cacciabue and Hollnagel (1995) used it earlier. A 2003 functions figure widened NDM from decisions to sensemaking, planning, coordination and more (a04).

**Stage 3, models to tools.** Examples: ShadowBox (trainee ranks options, then sees pooled expert ranking; five uses; no effect size in the source, a07); a railway signals-passed-at-danger diagnosis that found display design, not driver inattention, as cause (a06); a two-day CTA workshop for care outreach staff judged "highly successful" with no numbers (a06).

**The dispute with lab decision research.** Lipshitz et al. (2001) asked NDM to add controlled methods and drew 16 commentaries. NDM replied that controlled tests would stop it being NDM (a05). The founders concede "no correct answers" and hard scoring: "guilty as charged" (a04). Kahneman and Klein (2009) found common ground: trust intuition only where the environment is regular enough and the person had practice and feedback. We only read its abstract (b17, a32).

**Seven things NDM says are wrong (a03).** (1) Decisions need several options compared. (2) Expertise is rules. (3) Projects need a clear goal first. (4) Sensemaking builds up from data. (5) Insight needs breaking mental sets. (6) More information reduces uncertainty. (7) Teaching critical-thinking precepts such as listing assumptions helps. These are the founders' claims on case-study evidence. "More information does not help" means performance fell in specific conditions, not that data never helps.

**Internal critique.** Laurent and Bianchi (2016) argue macro and micro are levels of analysis, not separate kinds of cognition, and that motivated, need-driven cognition is a blind spot. They propose a multiscale enaction model (a12, b11). Sport RPD work is mostly after-the-event interviews with no controlled effect sizes (b19). The Norwegian armed-forces survey (N=225) found the 11 decision claims split into two factors (Planning/Structure; Analytic/Evidence-based), so even practitioners do not hold NDM as one belief (a23).

**Sensemaking models.** Data-frame model (Klein, Moon, Hoffman 2006; a17, not opened): a frame is a story or map that defines what counts as data. Cycle: connect data to frame, elaborate, question, preserve, compare, reframe, seek a new frame. Plausibility-transition model (Klein, Hoffman et al. 2023, a18): a surprise triggers a story; each state-to-state step is judged plausible; gaps are filled with assumptions; as anomalies pile up, confidence drops and a new story is built ("snap-back"). Built from 23 convenience cases of a 73-case corpus (Air France 447, USS Vincennes, Royal Majesty, AlphaGo), one coder, no predictions tested (K07 [S]).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| RPD accounts for most fireground decisions | "80-90%" of decisions; needs 10-20 years; coder classification of interviews | Klein and Wright 2016 (a02); 1986 paper not opened | [C] |
| NDM prompts raise LLM triage accuracy modestly | 13,500 assessments (10 models x 45 vignettes x 3 prompts x 10 runs). Default 63.3% (CI 61.9-64.7), RPD 67.6% (66.3-69), data-frame 66.7% (65.3-68). OR 2.26 (z 8.69), 2.05 (z 7.23) | Kopka and Feufel 2026 (a24, b23) | [S] |
| The gain sits in one class | Self-care 13.4% to 29.8% (RPD) / 24.6% (data-frame). Nonemergency 82.5 / 82.0 / 82.8%. Emergency (2 vignettes) 100 / 98 / 99%. 88% of errors (CI 87-88.9) were higher-than-necessary urgency. Class-balanced mean +4.6 / +3.5 (our arithmetic) | a25, d01-d03 | [E] within the paper |
| Prompt helps some cases, hurts others | RPD up in 18 of 45 vignettes (40%, median +18%, IQR 5-24), down in 13 (29%, median -5%). 12/13 decreases nonemergency (92%) | a26, b24 | [S] |
| Gain is not stable across models | GPT-4.1 mini 49.8 to 60.7 / 62.4; GPT-4.1 64.4 to 72.7 / 72.4; GPT-4.1 self-care 0% to 43.8% / 39.2%; GPT-5.2 Instant 57.8 to 56.4 / 55.3; GPT-5.2 Thinking 52.0 to 53.1 / 51.8. Run agreement (Fleiss kappa, median) 0.766 default, 0.717 RPD, 0.751 data-frame | d04, d05, a26 | [S] |
| Elite experts blunder more under time pressure | 20 grandmasters, 104 game pairs: blunder proportion t(19)=6.54, d=1.39; blunder size t(19)=4.23, d=0.96 (about half a pawn); Study 2: 7 world champions, same pattern | Vidulich and Tsang 2026 (a20, a21) | [S] |
| Cue utilisation lowers latency cost, not accuracy | Rail task N=58 (34 low, 24 high): latency 2079.7 ms (SD 395.7) vs 1527.4 (SD 498.6), F(1,56)=20.36, eta2=.267; accuracy no different. Exp 2 N=55; dual task slows low-cue more | Brouwers et al. 2016 (a14, a15) | [C] |
| Control-room cue use and workload | About 35 operators; eta2 .136 / .123 (prefrontal oxygenation); multivariate rated-workload effect not significant (eta2 about .013) | b20 | [C] |
| More messages did not give more shared SA | 213 staff, 19,168 emails; 3,191 calls among 132 staff; 89 nodes modelled; ties formed among similar-SA people; SA by self-report survey of core units | Buchler et al. 2016 (b12) | [S] |
| Supervise many, control few | One operator supervises about 15 UAS, controls 3. Health display redesign: fault-source detection 13 min (SD 6) to under 5 min in 95% of cases | Porat et al. 2016 (b13) | [S] |
| Human-AI teams lose to the best single party on decisions | 106 studies, 370 effects. Overall g=-0.23 (CI -0.39 to -0.07). Decision g=-0.27 (CI -0.44 to -0.10, P=.002). Creation g=+0.19 (CI -0.09 to 0.48, P=.18, n=34). Moderator F(1,104)=7.84, P=.006 | Vaccaro et al. 2024 (b21, d08) | [S] (bias handling disputed) |
| Sport RPD decision levels | 60-81% simple match, 13-28% diagnosis, 3-24% course-of-action evaluation (Macquet 2020 as cited) | b18 | [C] |
| ICU fluid decisions rely on heuristics | 11 of 23 eligible residents interviewed; premature closure, confirmation, status-quo bias seen; no outcome measure | a22 | [S] |
| Military endorsement is two-factor | N=225, KMO .741, chi2(36)=282.86, 29.24% variance (21.63 + 7.60), alpha .65 / .71 | a23 | [S] |
| LLM anchoring stronger than human | ChatGPT t(58)=8.78 vs humans t(58)=5.55; low anchor 20.83, high 105.97 (humans 22.5, 80.50); N=60 humans | Suri et al. 2023 (c02) | [E] (2 sources) |
| LLM recency and rare-event pattern | Match to pure recency player 78-91% for models vs 67% humans; models show no surprise-triggered switching; 160 agents per task vs 110 humans | Horowitz and Plonsky 2025 (c05, c06) | [S] |
| LLMs fail to leave early wrong frames | 15 LLMs, over 200,000 simulated conversations: multi-turn performance fell 39%; best-case skill -16%, unreliability +112%; restating all info recovers about 15-20% of gap | Laban et al. 2025 (d10) | [S] |
| Graph summaries win on global sensemaking | Comprehensiveness win 72-83% (podcast), 72-80% (news); diversity 75-82%, 62-71%; 125 questions per set; 47,075 claims; judge agreement 69-78% | Edge et al. 2024 (c15, c16) | [C] |
| Graph retrieval gain on correctness is small | MultiHop-RAG 70.27 vs 67.02; matched tokens 71.17 vs 71.01; textbook set 69.3-73.6 vs 70.68 no retrieval; graph construction 10-84M tokens | d14, d15 | [E] (2 sources) |
| Structured decision pipeline vs CoT | GPT-4o MTA 79.25 vs 69.25 best baseline; DeLLMa 70.70 vs 60.00; Llama-3.1-8B DeLLMa 72.36 vs 72.92 (loss). Prompt tokens 7938.6 vs 319.10; latency 27.67 vs 2.21 | DecisionFlow, Chen et al. 2025 (c10, d16) | [S] |
| Case-memory retrieval lifts web agents | WebArena 35.5% vs 23.5% (5.9 steps); Mind2Web cross-task step success 45.1 vs 36.2; gain within tens of examples, flat near 40 | Agent Workflow Memory (d17) | [S] |
| "Situation awareness" in agent papers means monitoring | SAUP AUROC 0.771 vs 0.702 (HotpotQA, Llama3-8B), 0.755 vs 0.669 (70B), 0.778 vs 0.772 (GPT-4o); Co-Gym SA failures 40% real, 47% simulated | d12, d13 | [E] |
| Small LLMs fail bandit tasks | Best-arm rate Qwen3-4B 89.2%, Thompson 51.1%, UCB 47.6%, random 31.8%, Qwen3-8B 37.5%, Llama-3.1-8B 31.6%; Qwen3-4B 6.53% with 5 arms | Lim et al. 2025 (c24) | [C] |
| LLM use in a SOC is uneven | 45 analysts, 3,090 queries, 532 conversations; 41% one-off; about 4% binary-judgement queries; one power user about 17% | Singh et al. 2025 (c13, c14) | [S] |
| Critic plus sensemaking module in multi-agent case | Argument quality 2.75 to 3.43; risk resolution 0% to 48.75%; critic alone 22.5%; LLM judge only | Kostka and Chudziak 2025 (b26) | [S] |

## 4. Mechanisms and models

### 4.1 RPD as an algorithm

Human version: (1) assess the situation; (2) match to a stored pattern that carries four things: expectations, relevant cues, plausible goals, a typical action; (3) if the match is typical, take the first action; (4) mentally simulate the action; if it works, act; if not, modify or take the next action; (5) if the situation does not match, diagnose further (a02, b18).

Implementable form for an agent:
```
retrieve k most similar solved cases for this problem class  (memory)
candidate = first workable answer or action from case or model prior
simulate: run the check in code if it exists; otherwise a short forward trace
if check passes: submit
else: take next candidate or call S6 (impasse)
```
Key property: comparison between options happens only after a failed check, not before. That matches G1 and the existing "direct / checked" modes.

Important boundary: the human mechanism depends on 10-20 years of tacit pattern memory. An LLM has broad pattern knowledge but no feedback-trained, task-specific library. So "first option" for an LLM is its prior, which can be biased (anchoring, over-urgency).

### 4.2 Data-frame and plausibility transition as a state machine

States: FRAME (one active story), ELABORATE (add data consistent with the frame), ANOMALY (count facts the frame cannot explain), QUESTION (anomaly count passes a threshold), REFRAME (build a new story that explains the anomalies).

Rules from a18 and a19:
- Surprise starts the loop.
- Plausibility is judged per step; gaps are filled with explicit assumptions (log them).
- Explaining-away cost rises with each anomaly; switch frames when cost passes a threshold.
- An anomaly is a violated expectation, not a statistical outlier (b15).

Implementation sketch: keep an anomaly log (fact, expectation it violates, explained yes/no). Code counts unexplained entries. If count >= T (try 2 or 3), fire S6 with operator O8 (reframe goal) or O6 (change representation), citing the log. This keeps G1 (signal-based doubt) and G2 (cite real output). No test of this rule on LLMs exists (K07, K20).

### 4.3 Cue utilisation and load

Cue utilisation is measured with the EXPERTise test battery; high-cue people hold response times steady under a secondary task and use less prefrontal resource on routine work (a15, b20). In the rail study high-cue people were slower and equally accurate (a14), so the benefit is effort saving, not speed. Agent analogue: retrieved similar cases may cut tokens at equal accuracy; this is a hypothesis (K08, K19).

### 4.4 Supervision limits and shared awareness

About 15 items can be supervised, about 3 actively controlled (b13). Broadcast messaging did not raise shared SA (b12). Agent analogue: a cap on concurrent hypotheses or sub-threads (G-level) and compact state passed between components instead of full transcripts. Not tested on agents (K09, K10).

### 4.5 Kopka and Feufel prompt design

Prompts told the model to reason like an RPD decision maker or by data-frame theory (full prompts in the paper, not copied here). Default temperature 1, no seed, no max-token cap, 10 repeats. Output lengths therefore differ between arms, so we cannot separate "structure" from "more thinking tokens" (a28, K01).

## 5. What holds up

**Holds with reasonable support**
- Narrated rationale and retrospective interviews are weak evidence of the real process (K06 [E]; a04, a16, a22, b19). Sport RPD is mostly qualitative.
- Where information format misleads, fix the format first (railway case, a06). Single narrative, not controlled.
- LLM heuristics are not just "human-like": anchoring stronger than humans (t=8.78 vs 5.55), recency far heavier (78-91% vs 67%), no surprise-triggered switching, no delayed rare-event pattern (K13 [E]).
- Graph-structured retrieval wins on LLM-judged comprehensiveness but its gain on correctness is small at matched tokens (K11 [C]).
- "Situation awareness" in agent papers is monitoring or error coding, not a thinking step (K21 [E]).

**Fails, is contested or is unverified**
- The 80-90% RPD share: founders' own coding, 1986 paper unread, cited replications are a magazine article, a thesis and a VR stress paper (K05 [C]).
- RPD's emphasis on intuition: grandmasters blunder more and by larger margins under time pressure (d=1.39, 0.96). This targets the intuition half only; RPD includes simulation (a20, d07).
- Cue utilisation: a strong latency effect in one lab study (eta2 .267) but no accuracy effect and a non-significant multivariate workload effect in another (K08 [C]).
- Human-AI teaming: g=-0.23 vs best single party. The main text says no publication bias was found; an earlier pass noted a small-study test (Egger beta 1.96, P=.002) that we did not relocate. Treat as [S] (K03).
- LLM prompt effect: in Kopka the gain is a threshold shift toward fewer over-urgent answers; it was zero or negative in the two newest models and negative in 29% of vignettes (K02 [E], K22 [S]). The text says reasoning models gained more (OR 2.15) while the table shows larger raw gains for non-reasoning models; unresolved (d04).
- Plausibility-transition model: untested predictions (K07).

**Moderators seen**: model strength (weaker models gain more), item class (self-care), task regularity (Kahneman and Klein), experience (10-20 years), time pressure (blunders up), concurrent load (cue use buffers), team similarity (ties among same-SA people).

**Interventions that worked (human)**: display redesign (13 min to under 5 min in 95%), CTA workshop (no numbers). **That did not**: more message sharing for SA; listing assumptions on schedule (founders' claim, no effect sizes); human review of AI decisions (g=-0.27).

**Interventions on LLMs**: NDM prompts +4 points overall (one study); Agent Workflow Memory +12 points on WebArena (not an NDM study, but a case-memory step); DecisionFlow beats CoT and 3-vote self-consistency with GPT-4o but at about 25 times the prompt tokens, and not on an 8B model. No token-matched test of any of these against a plain prompt exists.

## 6. Language models

**Direct tests of macrocognition ideas.** Only Kopka and Feufel (2026): 10 OpenAI models, 45 triage vignettes. RPD prompt +4.3 points, data-frame +3.4. Gain concentrated in self-care (13.4 to 29.8 / 24.6). 88% of all errors were over-urgent. Strongest gains in GPT-4.1 mini (+11 to +13); GPT-4.1 self-care 0% to 43.8%. No gain or small loss in GPT-5.2 Instant and Thinking. The prompts did not reduce run-to-run variability (Fleiss kappa 0.717 and 0.751 vs 0.766 default). Temperature-0 check on GPT-4.1 mini and GPT-5.2 Instant, authors say similar; appendix not read.

**Search coverage.** arXiv search "macrocognition": 1 paper (Jalaeian et al. 2025, 14 design heuristics from practitioner rounds, no LLM results). "recognition-primed" with language model: 0. "naturalistic decision making" with LLM: 1 (Mainali et al. 2025, case-based reasoning plus Bayes plus NDM matched GPT-5 at 0.892 vs 0.895 overall alignment; LLMs fell at risk 0.5). Absence is weak evidence because search tooling was patchy (d18, K21).

**How models behave on related tasks.**
- Anchoring and framing: ChatGPT chose the conjunction 18/20, kept an owned coin in 92.5% (humans 85%), framing 5 vs 4 in all trials with zero variance for GPT-3.5 (c02-c04).
- Repeated choice: GPT-4o mini and Gemini-1.5 Flash follow recent outcomes more than humans; context format and temperature (0.2, 1, 2) changed little (c05-c07).
- Predicting humans: Llama 70B and Mistral 7B matched an ACT-R IBL model; IBL won early, LLMs won over full episodes (0.542 / 0.602 vs 0.382 in the complex task) (c08).
- Bandits: small open models mostly fail from text feedback (c24).
- Early wrong frames: multi-turn drop 39% (d10); DeepSeek R1 on 100 MedQA cases scored 93% and its 7 errors showed anchoring and poor exploration of alternatives (d11, abstract only).
- Self-correction without feedback does not help (Huang et al. 2023, abstract only; d09), consistent with SCHEMA G2.

**Systems built on sensemaking or decision ideas.**
- GraphRAG: global-question comprehensiveness win 72-83%, but LLM-judged, and plain RAG wins on directness; correctness gain small at matched tokens (d14, d15).
- DecisionFlow: see section 3; the single-prompt version of the four steps did worse than separate calls; early extraction errors propagate; scoring and filtering weakest (c11).
- Multi-agent critic plus sensemaking module: LLM judge only (b26).
- Co-Gym: agents that plan around the user beat autonomous agents in real trials (win rate 86% travel, 74% tabular, 66% related work; 99 users, 150 trajectories), yet coded failures were communication 65% and situation awareness 40% of real trajectories (d13).
- SOC field study: GPT-4 used as an explainer; no accuracy data (c13).

**What this means.** The size of any macrocognition-prompt effect on a strong 2026 model is probably near zero on knowledge-heavy tasks, and the main documented effect is recalibration of a default bias. Whether a frame-and-anomaly step helps is untested.

## 7. What our agent should take

Schema parts: G guardrail, S state, O operator, memory.

### Add now (established)

1. **Treat written reasoning as not evidence of the true process.** Part G (already G10). Retrospective stories can be tidy and wrong. [E]. Evidence a04, a16, a22, b19, K06. No schema change except noting another independent line.
2. **Report per-class accuracy, not only overall, for any scaffold step, and check against a plain threshold shift or length-matched prompt first.** Part G7 / bench practice. [E]. Evidence a25, d01-d03, K02. A measurement rule, not a thinking step.
3. **Do not justify a new step by "situation awareness"; if used, it is a code-side monitor only.** Part G. [E]. Evidence d12, d13, d18, K21.
4. **Do not trust a first pattern unless the task class has a check or regular structure.** Part S0 gate (class record). [E] as a boundary. Evidence a20, a22, b17 (abstract only).

### Test first (not established)

| Item | Part | Status | Evidence |
|---|---|---|---|
| First-option-then-simulate route (RPD style) vs enumerate-all, at equal tokens | S3/S4, O | [S] | a24, a25, K01, K02, K22 |
| Data-frame style anomaly log with code-counted trigger, then O8 or O6 | S2 / S6 / O8 | [S] | a18, a19, d10, K07, K20 |
| Case-memory pre-retrieval of similar solved cases before first attempt | memory / S0 | [S] | d17, a14, K08, K19 |
| Cap on concurrent hypotheses or threads (3 vs 15) | G / S3 | [S] | b13, a09, K10 |
| Filtered versus full-broadcast context between components | G (multi-agent) | [S] | b12, K09 |
| Drift monitor (step distance to question) to predict failure | G / S4 | [S] | d12, K21 |
| Explore-or-exploit counter for text-feedback choice tasks | G / S3 | [C] | c24, c05, K14 |
| Re-derive without prior number to cut anchoring | S1 input hygiene / O | [E] bias exists, [S] fix works | c02, c05, K13 |
| Structured decision pipeline as separate calls, token-matched | O / S3 | [S] | c10, c11, d16, K12 |

Do not add: schedule-based assumption listing (founders themselves say it fails, a03; SCHEMA 4b already bars forced doubt).

## 8. Concrete tests on our bench

All tests: both arms at equal total tokens (input plus output; the plain arm gets the extra budget as extra independent attempts or longer thinking), seeded, temperature fixed, at least 2 model sizes, per-class accuracy plus overall with CIs.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Class-imbalanced classification items with a hidden prior bias (include items where the cautious answer is wrong) | plain vs RPD prompt vs length-matched "think carefully" vs plain with class-prior threshold shift | balanced accuracy, per-class accuracy | RPD gain mostly disappears against the threshold-shift arm; smaller on the stronger model |
| T2 | Puzzle or multi-turn items with a planted contradicting fact at turn k | plain vs anomaly log + code counter (T=2) + O8 reframe vs plain with restate-everything (Laban snowball) | rate of dropping the first frame; final accuracy | anomaly log beats plain on frame abandonment; may equal restate arm |
| T3 | Items with a code check and a first-answer prior (ARC-like, math) | first-option-then-check vs enumerate-3-then-pick vs 3 independent samples + vote | pass rate at equal tokens; tokens per solved item | first-option-then-check cheaper on easy items, equal on hard; enumerate worse |
| T4 | Problem classes with a solved-case library | 0 / 10 / 40 / 100 cases retrieved (after first attempt per SCHEMA memory rule, and before) | pass rate, steps, tokens | gain within about 40 cases then flat; "before" arm may fixate |
| T5 | Parallel sub-task bundles (3, 8, 15 sub-questions in one context) | cap threads vs no cap | error rate per sub-question | error rises past a small number; cap helps beyond about 5 |
| T6 | Multi-component pipeline with long shared state | full broadcast vs filtered compact state | accuracy at equal total tokens | filtered at least equal and cheaper |
| T7 | Anchoring probes (numeric estimates with planted anchor) | plain vs "ignore earlier numbers, recompute" vs recompute in a fresh context | anchor effect (high-anchor minus low-anchor mean) | fresh-context arm shrinks it most |
| T8 | Text-feedback bandit tasks, 2 and 5 arms | plain vs explicit pull/win counter kept in code | best-arm rate | counter helps small models; strong models near ceiling |
| T9 | Uncertain-outcome decision tasks (DeLLMa style) | DecisionFlow-style separate calls vs CoT vs 3-vote SC, all token-matched | accuracy | gain shrinks or vanishes once tokens matched |
| T10 | Any scaffolded step with a stated rationale | ablate the step vs keep it; compare stated reason with ablation result | rate where story and causal effect disagree | disagreement in a sizeable share of cases |

## 9. What does not transfer, and why

- **The 80-90% RPD share and 10-20 year threshold**: they describe humans with tacit pattern memory; the share is the founders' own coding of interviews. An LLM's "recognition" is its prior, which can be biased.
- **Team and network findings (Buchler, Porat, Vaccaro)**: about people and organisations. They support caution about message volume and human review, not a specific agent design. One agent has no social tie structure.
- **Field methods (CTA, critical decision interviews)**: we can read traces but cannot interview the model; its self-report is not the process (G10).
- **Sport, firefighting, ICU and rail results**: domains with feedback loops and stakes. Our bench is puzzles and benchmarks, where an explicit check often exists, which the founders' settings usually lack.
- **Kopka and Feufel's size**: +4 points on 45 triage vignettes with OpenAI models; two emergency vignettes; no token control. It does not generalise to ARC-like puzzles (authors' own limits, a28).
- **GraphRAG and DecisionFlow**: sensemaking or decision pipelines linked to macrocognition by analogy; their costs (10-84M tokens to build a graph; about 25x prompt tokens) conflict with G7 unless the gain survives token matching.
- **"Sensemaking" in HCI (314 arXiv hits)**: mostly human-tool interaction, not agent thinking.
- **Plausibility-transition descriptions**: built after the fact from famous disasters (hindsight), with no predictions.

## 10. Open questions

1. Does an RPD or data-frame prompt beat a length-matched plain prompt at equal tokens, on a non-medical task, seeded? (K01, no data)
2. Does an anomaly-log-then-reframe step raise the rate of abandoning a wrong frame? (K07, K20)
3. Do 2025-2026 reasoning models already do RPD-like steps internally? GPT-5.2 results say the gain is about zero; no Claude or Gemini data.
4. What N, coder agreement and RPD share did the 1986 fireground study and the true replications report?
5. Is the Kopka gain stable at temperature 0 across all models, and is it a threshold shift only? (appendix not read)
6. Does pre-attempt case retrieval cut tokens, and how does the effect scale with library size? (d17 gives steps, not tokens)
7. What is the publication-bias-corrected human-AI loss, and does it apply to an agent's own self-critique step?
8. Do graph concept summaries help reasoning when scored by correctness at matched tokens?
9. Does the DecisionFlow gain survive token-matched CoT with self-consistency?
10. Is the text-versus-table conflict in Kopka (reasoning models OR 2.15 vs larger raw gain in non-reasoning) a labelling error?

## 11. Sources

[V] opened (full text read), [M] snippet or abstract only.

- [V] Klein and Wright (2016) Macrocognition: From Theory to Toolbox. https://pmc.ncbi.nlm.nih.gov/articles/PMC4731510/ (a01-a07, b01-b05, d06)
- [V] Ward et al. (2017) Editorial: Macrocognition. https://pmc.ncbi.nlm.nih.gov/articles/PMC5398123/ (a08-a12, b06-b10)
- [V] Laurent and Bianchi (2016) Multiscale Enaction Model. https://pmc.ncbi.nlm.nih.gov/articles/PMC4961716/ (b11); [M] Frontiers page https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.01123/full (a13)
- [V] Brouwers et al. (2016) Cue utilization and cognitive load. https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00435/full (a14, a15)
- [V] Collins, Collins and Carson (2016) intuitive decision making in coaches. https://pmc.ncbi.nlm.nih.gov/articles/PMC4830814/ (a16)
- [M] Klein, Moon and Hoffman (2006) Making sense of sensemaking 2. https://doi.org/10.1109/MIS.2006.100 (a17)
- [V] Klein, Hoffman et al. (2023) Plausibility transition model. https://pmc.ncbi.nlm.nih.gov/articles/PMC10251660/ (a18, a19, b14, b15)
- [V] Vidulich and Tsang (2026) Intuition and deliberation in elite expertise. https://pmc.ncbi.nlm.nih.gov/articles/PMC13100097/ (a20, a21, d07)
- [V] Cognitive task analysis of ICU fluid resuscitation decisions (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12712819/ (a22)
- [V] Norwegian Armed Forces survey of Klein's claims (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13113691/ (a23)
- [V] Kopka and Feufel (2026) NDM prompts for care-seeking advice. https://pmc.ncbi.nlm.nih.gov/articles/PMC13061108/ (a24-a28, b23, b24, d01-d05); [M] https://biomedeng.jmir.org/2026/1/e88053 (c01, duplicate)
- [M] Klein, Calderwood and Clinton-Cirocco (1986) Rapid decision making on the fire ground. https://doi.org/10.1177/154193128603000616 (a29)
- [M] Johnson and Raab (2003) Take the first. https://doi.org/10.1016/s0749-5978(03)00027-x (a30)
- [M] Lipshitz et al. (2001) Taking stock of NDM. https://doi.org/10.1002/bdm.381 (a31)
- [M] Kahneman and Klein (2009) Conditions for intuitive expertise. https://doi.org/10.1037/a0016755 and https://pubmed.ncbi.nlm.nih.gov/19739881/ (a32, b17)
- [V] Buchler et al. (2016) Mission command in network-enabled operations. https://pmc.ncbi.nlm.nih.gov/articles/PMC4916213/ (b12)
- [V] Porat et al. (2016) Supervising and controlling unmanned systems. https://pmc.ncbi.nlm.nih.gov/articles/PMC4878290/ (b13)
- [M] Jalaeian, Morey, Rayo (2025) Joint activity design heuristics (abstract-level). https://arxiv.org/abs/2512.08036 (b16, c12)
- [V] NDM in sport review (2022). https://pmc.ncbi.nlm.nih.gov/articles/PMC9252097/ (b18, b19)
- [V] Control-room cue utilization (2019). https://pmc.ncbi.nlm.nih.gov/articles/PMC6718724/ (b20)
- [V] Vaccaro, Almaatouq, Malone (2024) Human-AI combinations. https://pmc.ncbi.nlm.nih.gov/articles/PMC11659167/ (b21, d08)
- [V] Human-AI teaming complementarity framework (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC12983458/ (b22)
- [V] Mainali et al. (2025) Classical AI vs LLMs for decision-maker alignment. https://arxiv.org/abs/2510.06093 (b25, c23)
- [V] Kostka and Chudziak (2025) cognitive synergy in LLM multi-agent systems. https://arxiv.org/abs/2507.21969 (b26)
- [M] Alacam et al. (2026) student sensemaking (title only, not used as evidence). https://arxiv.org/abs/2609.31046 (b27)
- [V] Team-science commentary (2025). https://pmc.ncbi.nlm.nih.gov/articles/PMC12529623/ (b28)
- [V] Jagpal et al. (2024) multidisciplinary model of critical thinking. https://pmc.ncbi.nlm.nih.gov/articles/PMC11102104/ (b29)
- [V] Suri et al. (2023) Do LLMs show decision heuristics similar to humans. https://arxiv.org/pdf/2305.04400 (c02-c04)
- [V] Horowitz and Plonsky (2025) LLM agents display human biases. https://arxiv.org/html/2503.10248 (c05-c07)
- [V] Nguyen, Jamale, Gonzalez (2024) Predicting human action decisions. https://arxiv.org/html/2407.09281 (c08, c09)
- [V] Chen et al. (2025) DecisionFlow. https://arxiv.org/html/2505.21397v2 (c10, c11, d16)
- [V] Singh et al. (2025) LLMs in the SOC. https://arxiv.org/html/2508.18947 (c13, c14)
- [V] Edge et al. (2024) GraphRAG. https://arxiv.org/html/2404.16130 (c15, c16)
- [M] Gullstrand Heander et al. (2025) Code review as decision-making. https://arxiv.org/abs/2507.09637 (c17)
- [M] Brown and Mulder (2025) LLMs as visualization agents. https://arxiv.org/abs/2508.13413 (c18)
- [M] Mastrianni et al. (2024) AI-enhanced sensemaking. https://arxiv.org/abs/2412.15444 (c19)
- [M] Suh et al. (2026) Atlas. https://arxiv.org/abs/2610.30548 (c20)
- [M] Storey (2026) Cognitive Tours. https://arxiv.org/abs/2611.08456 (c21)
- [M] Sindelar and Bojar (2025) ELOQUENT sensemaking. https://arxiv.org/abs/2507.12143 (c22)
- [V] Lim et al. (2025) TextBandit. https://arxiv.org/html/2510.13878 (c24)
- [M] Huh and Mohapatra (2025) multi-agent grounding. https://arxiv.org/abs/2508.07466 (c25)
- [V] arXiv search-result pages as coverage check. https://arxiv.org/search/ (c26, d18)
- [M] Huang et al. (2023) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (d09)
- [V] Laban et al. (2025) LLMs get lost in multi-turn conversation. https://arxiv.org/html/2505.06120 (d10)
- [M] Medical reasoning in LLMs: DeepSeek R1 analysis. https://arxiv.org/abs/2504.00016 (d11)
- [V] SAUP (2024). https://arxiv.org/html/2412.01033 (d12)
- [V] Collaborative Gym (2024). https://arxiv.org/html/2412.15701 (d13)
- [V] RAG vs GraphRAG systematic evaluation (2025). https://arxiv.org/html/2502.11371 (d14)
- [V] GraphRAG benchmark on textbook questions (2025). https://arxiv.org/html/2506.02404 (d15)
- [V] Wang et al. (2024) Agent Workflow Memory. https://arxiv.org/html/2409.07429 (d17)
