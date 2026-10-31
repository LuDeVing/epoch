# Course-of-action development and analysis: deep document

*Source files in this folder: evidence_a-d.jsonl (ids a01-d20), claims.jsonl (K01-K36), critique.md. Evidence ids below are written without the prefix "E12.01-". Claim ids are K01 etc. Status tags: [E] established, [S] single-source, [C] contested.*

## 1. What it is

Course-of-action (COA) development and analysis is the core loop of military staff planning. The US Army calls it the Military Decision-Making Process (MDMP). Joint forces use JP 5-0. Steps 3 to 5 of the seven MDMP steps are the part that matters here (a01):

1. Receipt of mission.
2. Mission analysis.
3. COA development: write several distinct plans.
4. COA analysis (wargaming): play each plan against likely enemy moves.
5. COA comparison: score the plans against criteria.
6. COA approval.
7. Orders production.

A COA is "a broad potential solution to an identified problem" (a01). Doctrine wants two or more COAs in the best case (a03). Each one is screened on five tests: feasible, acceptable, suitable, distinguishable, complete (a02). "Distinguishable" means the COA must differ significantly from the others.

Why it matters for our agent. The loop has the same shape as our S3 generate, S4 test, S7 select. The questions are:

- Is it worth making several distinct plans, or one plan plus a check?
- Does testing a plan against an adversary reply change which plan wins?
- Which doctrine checks are cheap enough to run in code?

Important limit. The doctrine itself (FM 5-0, JP 5-0) was never opened. The only doctrine source is a secondary Army article (a01-a03, 2018). Doctrine is a prescription, not an evidence base. No opened source measured whether the five tests, or the multi-COA assumption, improve outcomes (K01, K36).

## 2. History and theories in depth

**Doctrinal model (analytic).** The staff builds many options, wargames each against the enemy's most likely and most dangerous courses, then picks by a weighted comparison. It assumes that comparing options finds a better one. Under time pressure doctrine allows a single COA. A practitioner reports staffs presenting one COA, or COA teams returning near-identical plans (a03). No counts exist (K02).

**Recognition-primed decision (RPD) challenge.** Klein, Calderwood and Clinton-Cirocco (1986) studied fireground commanders by critical-incident interview. The abstract (opened, d01) says comparison of two or more options occurred in under 12% of decision points. Commanders recognised the situation, imagined one workable option, checked it by mental simulation and acted. Often-quoted figures are weaker than they look:

- "80%" comes from a trade article citing a 1988 ARI report. It is per incident, not per decision point (d02). Different unit.
- "26 commanders, 156 decision points" is secondary only (d01).

**Military variant.** Ross, Klein, Thunholm and colleagues (2004, d06, opened) say research support for the MDMP assumption that comparing several COAs finds a better one is weak. They report Thunholm's Swedish division-level experiment: the recognitional planning group was about 20% faster, with plans "somewhat bolder and better adapted". There was no blind quality score. The authors are proponents of the model (K36).

**Option generation studies.** Klein et al. (1995) on chess and Johnson and Raab (2003) on handball ("take the first") say the first option is usually best and more options hurt. Neither original could be opened (d03, d04). A 2026 conceptual replication in chess (N=92, opened, d05) found no clear first-option edge at lower ratings. The effect depends on expertise (K27, contested).

**Dissent techniques.** Premortem (Mitchell, Russo, Pennington 1989) and devil's advocacy (Schwenk 1990 meta-analysis). The Mitchell abstract (opened, d07) does not contain the often-quoted "30% more reasons". Schwenk could not be opened (d08).

**Machine lineage.**

- Search-based COA generators: thousands of simulated placements, ranked by simulated losses (a06, a07).
- Diverse-pool generators: genetic algorithm plus learned sequencer (a08, a09).
- LLM COA writers: COA-GPT 2024 (a04, a05).
- Adversarial COA benchmarks: COA-Bench 2026 (a10), IFPV 2026 (c15).
- LLM wargame agents, studied mostly as behaviour (escalation, consistency) rather than plan quality (a13, a15, a17).
- General LLM planning critiques (Huang, Kambhampati, Valmeekam).

## 3. Core findings with exact numbers

| Finding | Numbers | Source | Status |
|---|---|---|---|
| MDMP steps and five COA tests | 7 steps; 5 tests | a01, a02 (Army article) | doctrine, no validity data |
| Fireground commanders rarely compare options | comparison in under 12% of decision points (abstract) | d01 Klein 1986 | [S] original, old, interview |
| "80%" figure | per incident, third-hand | d02 | unit differs; do not cite as the main number |
| Recognitional planning vs MDMP, Swedish division staffs | about 20% faster; bolder plans; no blind quality score | d06 | [S], proponents report |
| First-option edge in chess | N=92 (orig 34); F(3,992)=1.73, p=.159; first move picked as best 37.3% | d05 | [C] expertise-dependent |
| Text-only COA-GPT vs RL baselines (StarCraft II TigerClaw) | 50 rollouts per variant; beat both RL baselines on mean reward; RL needed 112k battles / 70M timesteps | a04, a05, c01 | [S] one scenario |
| Human feedback to COA-GPT | each round raised mean reward, cut spread; best variant 3.4% below expert human (15 trials) | a05, b02 | [S] |
| COA-GPT casualties | higher friendly casualties than baselines; expert human fewest | a05, c03 | [S] |
| Map image in COA-GPT | no gain before feedback | b03 | [S] |
| Best-of-k enemy reply lowers blue advantage | k=1/2/4/8/16: .516/.498/.490/.485/.479; win rate .920 to .820 at k=8; 50 synthetic scenarios | a10, c12 | [S] synthetic |
| Role council with red-team revision | advantage .509 [.504,.514] vs .485 greedy; revision lowered pressure by only .014; revised pick in 76% | c13 | [S] |
| Doctrine-rubric enemy reply | .488 advantage, .800 win rate; changed pick in 56%; regret 0.041 | c14 | [S] |
| Metadata framing had no effect until fixed | bug, no effect size | a11 | [S] |
| Static LLM ranking vs adversarial simulation | 7 plans; rankings disagree; ACSE suppressed one LLM plan set to 4.00% / 1.33% success | c16 | [E] with c15 (2 sources, both 2026 preprints) |
| Multi-agent planner with adversarial simulation (IFPV) | mission success 0.72 to 0.86 (+19.4%); attrition 2.28 to 1.33 (-41.7%); ablations 0.65 / 0.77 / 0.73 | c15 | [S]; baseline is single-step LLM (weak) |
| Non-LLM diverse pool | 20 COAs; MAPE 4.07% vs exact sequencing; 10 to 100x faster; best and worst keep rank under 5-20% noise | a08, a09 | [S] |
| LLMs escalate in wargames | GPT-3.5 neutral scenario 10.15 to 26.02 (a 2.56x ratio; paper says +256%); 5 models, 10 runs, 14 days | a13, b07 | [S] |
| Escalation interventions | mean 6.37 (t=1.0) to 3.96 (t=0.5, -38%), 3.33 (t=0.01, -48%); de-escalation prompt 2.76 (-57%); reflection 4.61 (-28%) | c09 | [S] 10 runs |
| LLM vs 214 experts | of 21 actions, GPT-3.5 matched human frequency on 16, GPT-4 on 10, GPT-4o on 9; persona prompts no effect | a15, b04, c06 | [S] |
| Cross-sample inconsistency | BERTScore-based score, max pair 0.73; concrete incident detail lowers it; anonymising does not | a17, a18 | [S] |
| Opponent modelling gap | humans 77.9-85.7 vs best LLM ~49; complex situation analysis 85.9% vs 37.5% | a21, b11, b12, c18 | [S] one benchmark, early-2025 models |
| LLM as world simulator | best 59.9% on non-trivial state changes; 92.1% with rules vs 61.5% without; 2954 transitions | d16 | [S] |
| Strategy library with trained evaluator | +85.35% over plain LLM planning in MicroRTS; LLMs lost 100% to solver-level engines in chess and Connect Four | d17, d18 | [S] |
| Self-correction without feedback | GPT-3.5 CSQA 75.8 to 38.1; GPT-4 GSM8K 95.5 to 89.0 | b13 | [E] |
| Debate vs self-consistency | GSM8K 6 responses: debate 83.2 vs self-consistency 85.3 (9 responses 88.2); Liang: 26.0 to 37.0 on Counter-Intuitive Arithmetic | b14, b15 | [C] |
| Reasoning model planning | o1-preview 97.8% (587/600) Blocksworld, 52.8% disguised, 37.3% randomized, 23.63% on 20-40 step plans | b16, c22 | [S] |
| LLM-Modulo | ~12% of LLM plans correct unaided; 82% Blocksworld subset, 70% Logistics with critics | b17 | [E] with b16 |
| Plan-level diversity | LiveCodeBench, Claude 3.5 Sonnet: pass@1 41.4; repeated sampling pass@200 60.6; PlanSearch pass@200 77.0; PlanSearch often lowers pass@1 | d14 | [S] needs verifier |
| Compute allocation | revision wins on easy items; parallel or tree on hard; about 4x less compute than best-of-N | d15 | [S] math |
| Escalation of commitment | peer deliberation 99.2% (249/251) vs hierarchical advisory 46.2% (115/249); N=6,500 | c25 | [S] |
| Premortem-like methods in LLMs | InvThink harmfulness 3.22 to 2.19; anticipatory reflection 23.5% vs 22.7% LATS (WebArena) | d10, d11 | [S] indirect |
| Devil's advocate in LLM groups | 0/80 initial to 57/80 (71.3%) correct after discussion, no control arm | d13 | [S] weak design |
| Framing bias in LLMs | GPT-4 admitted 40.5% more under reject framing; 13,465 prompts | d19 | [S] |
| Coverage of the field | only 20 of 223 AI-wargame papers (9%) let the LM act and adjudicate | a19, b10, c11 | scoping count |

## 4. Mechanisms and models

An engineer can build the following from the evidence. Each is a small, code-checkable piece.

**4.1 Generate-test loop with an external critic (K17, K13).** The LLM proposes candidates. A program checks them (validator, simulator, unit tests). Only failing output is fed back. LLM-Modulo (b17) and COA-GPT (a05) both have this shape. Search-based generators (a06, a07) add two rules: illegal moves get a severe penalty and the candidate is discarded; new alternatives are generated again as the situation changes.

**4.2 Distinctness filter (doctrine "distinguishable", K02, K31).**

1. Embed or tag each candidate by its core idea (not its wording).
2. Compute pairwise distance.
3. Drop or re-prompt any candidate within a threshold of another.
4. Report the diversity score next to the result.

PlanSearch (d14) supports this: diversity in idea space predicted the gain from search. Its gain needed a verifier. GenCOA (a08) reached diversity by changing the task allocation, with a GA that raised pool diversity about 10% over random allocation.

**4.3 Completeness and format screen (doctrine "complete").** Check that every required field exists (objective, steps, resources, assumptions, fallback). Pure code. Cheap.

**4.4 Adversary-reply test (K07, K08, K10).**

1. For each candidate, sample k replies from an opponent (LLM, rule table or simulator).
2. Score the candidate against the strongest reply, not the average.
3. Pick by the worst-case or best-of-k reply score.

COA-Bench (c12) shows scores fall as k rises (.516 to .479 at k=16). A candidate chosen at k=1 may not be chosen at k=8. A doctrine rubric for picking the reply gave about the same pressure as best-of-8 (.488 vs .485) and changed the pick in 56% of scenarios (c14). So a cheap rubric can stand in for sampling many replies. This is synthetic evidence.

**4.5 Simulate, do not only judge (K08).** IFPV (c16) shows an LLM's static ranking of seven plans disagrees with the ranking from adversarial simulation. Use a simulator or rule-based adjudicator where one exists. Do not use an LLM as adjudicator for multi-step outcomes (d16: errors compound, best 59.9% on non-trivial transitions).

**4.6 Structured opponent module (K34).** Strategy Evaluation Network (d17): keep a library of strategies, predict win chance of each against the observed opponent, let the LLM choose from the ranked list. It was trained, so it does not show that a prompted opponent model works.

**4.7 Vector scoring (K05).** COA-GPT won on reward but lost more units. Score candidates on a vector (reward, own losses, time, risk) and select in code (G5).

**4.8 Budget rule (K30, d15).** Easy item: one plan plus an externally checked revision. Hard item with several possible approaches: more distinct candidates plus a selector. Choose by a difficulty signal.

**4.9 Cross-sample inconsistency as a signal (K22).** Sample several plans, measure how far their meanings differ. High spread may flag a low-confidence item. Calibration of this signal is untested.

**4.10 Input-effect audit (K11).** Ablate each prompt section and confirm the output changes. COA-Bench found a metadata field with no effect only because of an inspectable trace.

## 5. What holds up

**Holds up (multiple sources).**

- Generate then test against an outside check beats unaided self-review. Huang et al. (b13) show self-correction without feedback hurts (CSQA 75.8 to 38.1). LLM-Modulo (b17, b16) shows a 12% unaided plan success rising to 70-82% with critics. [E]
- Static LLM ranking of plans is not a stand-in for simulating the plan against an opponent (c15, c16). [E] but both are 2026 preprints with synthetic or learned adversaries. Independence is weak.
- LLM wargame agents are poor at opponent modelling and complex situation analysis (a21, c18, d18). One benchmark plus MicroRTS and SPIN-Bench. Directionally consistent.

**Contested.**

- Take-the-first versus compare options (K27). The 1986 interview result is real but old. The 2026 chess replication (N=92) did not find the edge at lower ratings. It depends on expertise.
- Debate. Huang: no gain over self-consistency at matched responses (83.2 vs 85.3). Liang: 26.0 to 37.0 on hard arithmetic. Different tasks. Our G9 already says no debate.
- Premortem and devil's advocate (K28). Human data is thin. LLM data is indirect, and the one dissent-group test (d13) has no control arm.
- Tree search over candidates. Game of 24: 4% to 74% (c23) versus the claim it is prompt priming (b18).

**Failures and caveats.**

- COA-GPT: no independent replication found (d20); no token cost reported (K35). One scenario, scripted enemy, 50 rollouts, GPT-4-Turbo, baseline numbers copied from a prior paper.
- Rivera: the "+256%" is a 2.56x ratio, so +156%. Most start-vs-end differences were not significant (b07). The world model is GPT-3.5.
- Mitchell: the quoted "30% more reasons" is not in the abstract. Do not cite.
- Council: little gain (.509 vs .485), and revision lowered pressure by only .014 (c13).
- IFPV baseline is a single-step LLM, weaker than best-of-k at equal tokens. The 41.7% is a drop in platform attrition, not mission success.
- Evidence overcounting: COA-GPT lines (a04, a05, b01-b03, c01-c04) are one paper. COA-Bench lines (a10, c12-c14) are one paper. Valmeekam (b16, c22) is one paper.

**Moderators.**

- Expertise (RPD, chess).
- Time pressure (doctrine allows one COA).
- Task difficulty (Snell: revision on easy, search on hard).
- Presence of an external verifier (PlanSearch, LLM-Modulo).
- Concrete incident detail (lowers LLM inconsistency, a18).
- Group structure (peer deliberation 99.2% vs hierarchical 46.2% escalation of commitment, c25).

**Interventions that worked.**

- Low temperature and a de-escalation reflection prompt cut wargame escalation by 38-57% (c09).
- Short outside feedback to COA-GPT.
- A self-help rewrite prompt for framing bias (d19).
- A dissenter reduced LLM conformity (d12).

**Interventions that did not.**

- Persona prompts (c06).
- Anonymising country names (a18).
- A map image without feedback (b03).
- A role council (c13).
- 50 words of escalation context alone (-8%, c09).

## 6. Language models

**Writing COAs.** COA-GPT (GPT-4-Turbo) writes a full COA in seconds from doctrine excerpts and a mission (c01). In one StarCraft II scenario it beat two RL baselines on mean reward without retraining. It lost more friendly units. It remained 3.4% below an expert human even with feedback. Single scenario, so treat as an existence proof.

**Plan reliability.** Reasoning models are much better but brittle. o1-preview scored 97.8% on Blocksworld, 52.8% when symbols were disguised, 37.3% randomized, and 23.63% on 20-40 step plans (b16, c22). A classical planner got 100% faster and cheaper. In SPIN-Bench every LLM lost 100% of chess and Connect Four games to solver-level engines (d18).

**Self-check.** Unaided self-correction lowers accuracy (b13). Outside feedback raises it (a05, b17).

**Adversarial testing.** In COA-Bench (synthetic), more adversary samples lower the apparent score (.516 to .479), and a council gave only small gains. In IFPV, a multi-agent planner with adversarial simulation raised success 0.72 to 0.86 over a single-step LLM, with the adversary a fine-tuned world model.

**Wargame behaviour.** Off-the-shelf models escalate (a13). Temperature and a de-escalation prompt reduce it by 38-57% (c09). Persona prompts do nothing (c06). Simulated team dialog is "farcically harmonious" (a16, c07). Samples differ in meaning (a17). Models track the human action mix at a high level only (b04: 16, 10, 9 of 21).

**Opponent modelling and simulation.** LLMs trail humans by about 30-40 points in opponent modelling (c18). GPT-4 simulates state changes at 59.9% (d16). A trained evaluator added +85.35% over plain LLM planning (d17).

**Biases.** Framing and anchoring biases carry to non-military decisions (d19). Escalation of commitment is much stronger in peer-deliberation structures (c25). Whether escalation carries to non-geopolitical plan selection is untested.

**Diversity.** Repeated samples from one model are near-duplicates. Plan-level diversity beats resampling when a verifier exists (d14).

**What is missing.** No source compares, at equal tokens, 3 distinct COAs versus one plan plus self-check versus best-of-N on a planning task (K30). Nearest evidence is d14 and d15.

## 7. What our agent should take

### Add now (established)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Test candidate plans with a program or simulator, not only by LLM judgement. Feed back only real failing output. | S4, G2, G5 | [E] | K08, K14, K17; b13, b17, c15, c16 |
| No unaided self-review as the only check; use an external check. | G2, O verify | [E] | K14; b13 |
| Code-based completeness screen (required fields present). Zero model cost. | S3 / S4 | [E] as engineering; no validity data for the doctrinal form | a02 |
| Select in code over a score vector (reward, own losses, risk), not a model verdict. | G5, S7 | [E] for G5; vector idea from K05 is [S] | a05, c03 |
| Do not use an LLM to adjudicate multi-step outcomes where a rules check exists. | S4 | [E] direction (two sources) | K32; d16, d18 |
| Do not rely on persona prompts for diversity. | G4 | [E] from earlier series; here single | K21; c06 |

### Test first (single-source or contested)

| Item | Schema part | Status | Evidence |
|---|---|---|---|
| Three distinct COAs, compared, vs one plan plus check vs best-of-N at equal tokens. | S3, S7, G12 | [C] / untested | K27, K30, K36; d05, d06, d15 |
| Distinctness filter (doctrine "distinguishable") before testing. | G, S3 | [S] | K02, K31; a02, d14 |
| Best-of-k adversary reply test (k up to 8) before selecting. | S4, O select | [S] | K07; c12 |
| Cheap rubric to pick the enemy reply instead of sampling many. | S4 | [S] | K10; c14 |
| Structured opponent model ("most likely" and "most dangerous" reply). | S4 | [S] | K24, K34; c18, d17 |
| Premortem step vs a plain "list risks" prompt at equal length. | O critique | [C] | K28; d07-d13 |
| Low temperature and a reflect-first prompt for the choosing step. | G | [S] | K20; c09 |
| Randomise candidate order and framing in selection; measure flip rate. | G | [S] | K33; d19 |
| Single decider plus critic rather than peer vote for keep-or-drop decisions. | G9 | [S] | K26; c25 |
| Difficulty-routed budget: revision on easy, diverse candidates on hard. | G12 | [S] | K30; d15 |
| Cross-sample inconsistency as a confidence signal. | S0 / S9 | [S] | K22; a17 |
| Pool with fallbacks (keep a second valid plan for when a step fails). | memory | [S] | K12; a08, a09 |
| Input-effect ablation of prompt sections in our harness. | G7 | [S] | K11; a11 |

## 8. Concrete tests on our bench

All arms get the same total token budget (including setup and tests). Report per-difficulty results.

| # | Item type | Arms | Metric | Expected effect |
|---|---|---|---|---|
| T1 | Scored planning items with a validator (Blocksworld-like, scheduling, ARC-style multi-step plans) | A: one plan plus external check and repair. B: 3 distinct plans, code-selected after tests. C: best-of-N samples with tests | validated success rate | B beats C on hard items if candidates are distinct; A wins on easy items (K30, d15) |
| T2 | Same items | With vs without a code distinctness filter (pairwise idea distance) | success; diversity score | gain only when a verifier exists (d14); likely lowers pass@1, raises pass@k |
| T3 | Two-player or adversary-scored items (small game, toy wargame, or our own rule-based opponent) | A: static LLM ranking. B: pick by worst reply over k=1. C: k=4 or 8. D: rubric-picked reply | win rate vs held-out opponent; rank agreement with simulation | B/C/D beat A; C vs D near equal (c12, c14) |
| T4 | Same items | Prompted LLM opponent vs rule-based opponent vs static | win rate vs a stronger held-out opponent | gain uncertain; check against d17 |
| T5 | Plan items with hidden failure modes | Premortem prompt vs plain risk list vs no step, same added tokens | downstream success | small or null; premortem wins only if it exposes failures the plain list misses |
| T6 | Selection step on 100 candidate sets | Randomise order / reframe vs fixed | choice flip rate; success | flip rate above 10% would show a bias worth fixing (d19) |
| T7 | 100 COA-vs-reply pairs with a simulator | LLM adjudication vs simulator | agreement | below 80% agreement means keep the simulator (d16) |
| T8 | Multi-step tasks with failing steps | Pool with fallback plan vs single plan, re-plan after failure | completion rate | gain when failures are random (a09) |
| T9 | Choose-or-stay decisions | Peer vote vs single decider plus critic | rate of keeping a failing plan | critic arm lower (c25) |

## 9. What does not transfer, and why

- **Escalation findings.** They describe geopolitical simulation tendencies with fixed action menus (a13). They are not plan-quality evidence. Transfer to our bench is untested (K19, K33).
- **Persona and role councils.** No effect on LLM actions (c06), and the council gave a small gain (c13). We already have G4 and G9.
- **COA-GPT numbers.** One StarCraft scenario, scripted enemy, one-shot orders. The casualty result may come from the one-shot format (a guess by the authors).
- **Vision gain.** No gain before feedback (b03); our agent is text-first.
- **Real doctrine validity.** Not measured. Do not assume the five tests predict plan quality.
- **RPD "take the first".** Depends on expertise. A base LLM in a new scenario is not a fireground captain. The chess replication shows the edge fades at lower ratings (d05).
- **Human staff time pressure.** Doctrine's single-COA exception saves human hours. Our cost is tokens, so the trade is different.
- **Synthetic scores.** COA-Bench uses invented rubrics and a Lanchester-style win check. The authors warn they may reward things experts would not (a10).
- **IFPV's fine-tuned adversary.** We will not have one. See K34.
- **Non-LLM generators (GA, GNN).** Useful as templates, not as components for a prompt-only agent (a06, a08).

## 10. Open questions

1. At equal tokens, does generating 3 distinct COAs and comparing them beat one plan plus self-check or best-of-N? (K30)
2. Does adversarial wargaming against an untrained (prompted) opponent beat static ranking? (K34)
3. Do the five doctrinal tests predict outcomes? Pounds and Fallesen, Thunholm primary and the ARI reports remain unopened.
4. What are the real sizes in Klein 1995 and Johnson and Raab 2003? Not opened.
5. Does any LLM premortem test on plans exist at equal tokens? None found. (K28)
6. Does "most likely and most dangerous" enemy modelling improve a plan?
7. Do LLM COAs collapse to near-duplicates, and does forced diversity raise success without a verifier? (K31)
8. Do wargame biases (escalation, harmony) carry to non-geopolitical plan selection?
9. Can newer models adjudicate reliably? Only GPT-4 was tested (d16).
10. Is there any independent replication of COA-GPT, and what did it cost in tokens? (K35)
11. Do the 2026 results (COA-Bench, IFPV) survive peer review and stronger baselines such as best-of-k at equal tokens?

## 11. Sources

Marks: [V] opened by an evidence agent; [M] snippet or memory only. Numbers from [M] sources are not used above.

- [V] US Army article on developing multiple sustainment COAs (cites FM 6-0 / ADP 5-0), 2018. https://www.army.mil/article/209253/developing_multiple_sustainment_courses_of_action_in_support_of_a_maneuver_plan (a01-a03)
- [V] Goecks and Waytowich (2024) COA-GPT. https://arxiv.org/abs/2402.01786 (a04, a05, b01-b03, c01-c04)
- [V] Schubert, Hansen, Hoerling, Johansson (2025) Autonomous generation of different COAs in mechanized combat. https://arxiv.org/abs/2511.05182 (a06, a07)
- [V] Poddar, Esfahani, Dantu, Chowdhury (2025) GenCOA. https://arxiv.org/abs/2506.20031 (a08, a09, c17)
- [V] Vidra and Kanhai (2026) COA-Bench. https://arxiv.org/abs/2609.26059 (a10, a11, c12-c14)
- [V] Park, Shim, Kim (2026) AI-based automated COA generation architecture. https://arxiv.org/abs/2604.20862 (a12)
- [V] Rivera et al. (2024) Escalation risks from language models. https://arxiv.org/abs/2401.03408 (a13, a14, b07, b08, c08)
- [V] Lamparth et al. (2024) Human vs. Machine wargames. https://arxiv.org/abs/2403.03407 (a15, a16, b04-b06, c05-c07)
- [V] Shrivastava, Lamparth, Hullman (2024) Free-form decision inconsistency. https://arxiv.org/abs/2410.13204 (a17, a18)
- [V] Matlin et al. (2026) Shall we play a game? https://arxiv.org/abs/2509.17192 (a19, b10, c11)
- [V] Hogan and Brennen (2024) Snow Globe. https://arxiv.org/abs/2404.11446 (a20, b09, c10)
- [V] Yin et al. (2025) WGSR-Bench. https://arxiv.org/abs/2506.10264 (a21, b11, b12, c18)
- [M] Klein, Calderwood, Clinton-Cirocco (1986) full text. https://doi.org/10.1177/154193128603000616 (a22, b19; abstract opened in d01)
- [M] Thunholm (2004/2005) Planning under time pressure. https://doi.org/10.1201/b12472-6 (a23, b22)
- [M] Pounds and Fallesen (1998) ARI. https://doi.org/10.21236/ada359869 (a24)
- [M] Klein, Wolf, Militello, Zsambok (1995) chess option generation. https://doi.org/10.1006/obhd.1995.1031 (b20, d03)
- [M] Johnson and Raab (2003) Take the first. https://doi.org/10.1016/s0749-5978(03)00027-x (b21, d04)
- [M] Schwenk (1990) meta-analysis. https://doi.org/10.1016/0749-5978(90)90051-A (b24, d08)
- [M] Cheikes et al. (2004) ACH confirmation bias. https://www.mitre.org/ (b25)
- [V] Huang et al. (2024) LLMs cannot self-correct reasoning yet. https://arxiv.org/abs/2310.01798 (b13, b14)
- [V] Liang et al. (2024) Multi-agent debate for divergent thinking. https://arxiv.org/abs/2305.19118 (b15)
- [V] Valmeekam et al. (2024) Planning abilities of o1. https://arxiv.org/abs/2409.13373 (b16, c22)
- [V] Kambhampati et al. (2024) LLM-Modulo. https://arxiv.org/abs/2402.01817 (b17, b18)
- [V] Elbaum and Panter (2025) Managing escalation. https://arxiv.org/abs/2508.01056 (c09)
- [V] Palnitkar et al. (2026) Mil-SCORE. https://arxiv.org/abs/2601.21826 (c19; table garbled)
- [V] Huang et al. (2026) IFPV. https://arxiv.org/abs/2605.14851 (c15, c16)
- [V] Sun et al. (2023) Self generated wargame AI. https://arxiv.org/abs/2312.01090 (c20; table garbled)
- [V] Drinkall (2025) Red lines and grey zones. https://arxiv.org/abs/2510.03514 (c21)
- [V] Yao et al. (2023) Tree of Thoughts. https://arxiv.org/abs/2305.10601 (c23)
- [V] Kader and Lee (2024) Strategic reasoning of LLMs. https://arxiv.org/abs/2412.13013 (c24; abstract level)
- [V] Getting out of the Big-Muddy (2025). https://arxiv.org/abs/2508.01545 (c25)
- [V] Fire Engineering article citing ARI TR 796. https://www.fireengineering.com/?p=277352 (d02)
- [V] Raab et al. (2026) chess option-generation replication. https://www.journalofexpertise.org/articles/volume9_issue1/JoE_9_1_Raab_etal.pdf (d05)
- [V] Ross, Klein, Thunholm et al. (2004) RPD model, Military Review. https://pacdeff.com/pdfs/The%20Recognition%20Primed%20Decision%20Model.pdf (d06)
- [V] Mitchell, Russo, Pennington (1989) abstract. https://doi.org/10.1002/bdm.3960020103 (d07; b23 was [M])
- [V] Peabody (2017) premortem thesis, abstract. https://digitalcommons.mtu.edu/etdr/374 (d09)
- [V] Kim et al. InvThink. https://arxiv.org/abs/2510.01569 (d10)
- [V] Wang et al. (2024) Anticipatory reflection. https://arxiv.org/abs/2405.16334 (d11)
- [V] Zhu et al. (2025) Conformity in LLMs. https://arxiv.org/abs/2410.12428 (d12)
- [V] Ke et al. (2024) Multi-agent diagnosis with devil's advocate. https://arxiv.org/abs/2401.14589 (d13)
- [V] Wang et al. (2024) PlanSearch. https://arxiv.org/abs/2409.03733 (d14)
- [V] Snell et al. (2024) Scaling test-time compute. https://arxiv.org/abs/2408.03314 (d15)
- [V] Wang et al. (2024) LMs as text-based world simulators. https://arxiv.org/abs/2406.06485 (d16)
- [V] Xu et al. (2025) Strategy-augmented planning. https://arxiv.org/abs/2505.08459 (d17)
- [V] Yao et al. (2025) SPIN-Bench. https://arxiv.org/abs/2503.12349 (d18)
- [V] Echterhoff et al. (2024) BiasBuster. https://arxiv.org/abs/2403.00811 (d19)
- [V] arXiv 2511.10651 (report generation; no COA replication). https://arxiv.org/abs/2511.10651 (d20)

## Source audit (2026-11-01)

Fresh auditors re-opened the sources of 3 established claims: 1 confirmed as written, 2 changed. Where a row in sections 3 or 7 cites a claim below, the wording here wins. Current wording and status are in `claims.jsonl`.

- **E12.01-K08** (now single-source: the sources are not independent). Only IFPV (listed twice) supports it, on 7 plans from one simulator; Vidra et al. is a synthetic best-response benchmark that does not test static LLM ranking or rule-based checks, and 0.72 to 0.86 is single-step LLM vs the multi-agent planner (MPHA).
- **E12.01-K17** (now single-source: the sources are not independent). All numbers come from the Kambhampati/Valmeekam group (the 82%/70% figures are VAL back-prompting results from their earlier paper, cited in the position paper; obfuscated Blocksworld only about 10%); the only outside source (IFPV) does not give these numbers.
